#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PlantSciKB 每日文献流水线 —— 单一入口。

设计原则
--------
1. 一个入口：cron、手动、复现实验都调用本脚本。
2. 阶段可枚举：--list-stages 查看全部阶段；--only/--skip/--from 精确控制。
3. 失败可见：子进程非零退出不再被吞掉，最终以退出码反映。
4. 可观测：每次运行生成 logs/pipeline/<run_id>/ 下的 pipeline.log 与 summary.json。
5. 可重入：文件锁防止并发；--resume 从当日已成功阶段之后继续。
6. 可移植：所有路径由 kb_paths 解析（KB_BASE 环境变量优先）。

退出码
------
0  成功（允许 optional 阶段被跳过或软失败）
1  至少一个 required 阶段失败
2  参数错误或预检失败
3  已有实例在运行
"""
import argparse
import fcntl
import glob
import json
import os
import re
import shutil
import subprocess
import sys
import time
import traceback
from dataclasses import dataclass, field
from datetime import datetime

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

from kb_paths import (  # noqa: E402
    BASE, CONCEPTS_DIR, EVIDENCE_DIR, ENTITIES_DIR, RELATIONSHIPS_DIR,
    SYNTHESIS_DIR, HYPOTHESES_DIR, PROGRAMS_DIR, RAW_DIR, PDF_DIR,
    STATE_DIR, LOG_DIR, ensure_runtime_dirs, METHODS_DIR,
)
from text_utils import yaml_str  # noqa: E402

PYTHON = sys.executable or 'python3'
PDF_PYTHON = '/usr/bin/python3' if os.path.exists('/usr/bin/python3') else PYTHON
# 阶段脚本所在目录：优先用本流水线自身所在的 scripts/，
# 这样仓库可作为「纯代码」对任意 KB_BASE 运行；
# 若脚本被部署进知识库内（BASE/scripts），两者是同一目录，行为不变。
SCRIPTS = os.environ.get('KB_SCRIPTS') or SCRIPT_DIR
CONCEPTS_TOP = os.path.join(BASE, 'concepts')


# ────────────────────────────── 日志 ──────────────────────────────
class RunLogger:
    def __init__(self, run_dir):
        self.run_dir = run_dir
        self.log_fh = open(os.path.join(run_dir, 'pipeline.log'), 'a', encoding='utf-8')
        self.ev_fh = open(os.path.join(run_dir, 'events.jsonl'), 'a', encoding='utf-8')

    def _emit(self, msg, level='INFO', **extra):
        stamp = datetime.now().strftime('%H:%M:%S')
        line = '[%s] %s' % (stamp, msg)
        print(line, flush=True)
        self.log_fh.write(line + '\n')
        self.log_fh.flush()
        event = {'ts': datetime.now().isoformat(timespec='seconds'),
                 'level': level, 'msg': msg}
        event.update(extra)
        self.ev_fh.write(json.dumps(event, ensure_ascii=False) + '\n')
        self.ev_fh.flush()

    def info(self, msg, **kw):
        self._emit(msg, 'INFO', **kw)

    def warn(self, msg, **kw):
        self._emit(msg, 'WARN', **kw)

    def error(self, msg, **kw):
        self._emit(msg, 'ERROR', **kw)

    def close(self):
        for fh in (self.log_fh, self.ev_fh):
            try:
                fh.close()
            except Exception:
                pass


class StageFailure(RuntimeError):
    pass


# ────────────────────────────── 阶段定义 ──────────────────────────────
@dataclass
class Stage:
    key: str
    title: str
    func: object
    timeout: int = 600
    required: bool = True
    needs: tuple = ()
    default_enabled: bool = True
    when: object = None


@dataclass
class Context:
    args: object
    log: RunLogger
    run_id: str
    today: str
    state: dict = field(default_factory=dict)
    today_pages: list = field(default_factory=list)
    pre_pages: set = field(default_factory=set)
    stats: dict = field(default_factory=dict)
    temp_files: list = field(default_factory=list)
    has_new: bool = False

    def degrade(self, msg):
        """记录"跑完了但质量不达标"的情况，进 summary 而不是被静默吞掉。"""
        self.stats.setdefault('degraded', []).append(msg)
        self.log.warn('  ⚠ DEGRADED: %s' % msg)

    def script(self, name):
        return os.path.join(SCRIPTS, name)


# ────────────────────────────── 子进程 ──────────────────────────────
def run_cmd(ctx, key, cmd, timeout, cwd=BASE, check=True, env=None):
    """运行子进程；日志完整落盘，失败抛出 StageFailure。"""
    if isinstance(cmd, (list, tuple)):
        pretty = ' '.join(cmd)
        shell = False
    else:
        pretty = cmd
        shell = True
    ctx.log.info('  → %s' % pretty)
    out_path = os.path.join(ctx.log.run_dir, '%s.out' % key)
    started = time.time()
    try:
        proc = subprocess.run(
            cmd, shell=shell, cwd=cwd, timeout=timeout,
            stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
            text=True, errors='replace', env=env,
        )
    except subprocess.TimeoutExpired as exc:
        tail = (exc.stdout or '')
        if isinstance(tail, bytes):
            tail = tail.decode('utf-8', 'replace')
        with open(out_path, 'a', encoding='utf-8') as fh:
            fh.write(tail)
        raise StageFailure('timeout after %ss' % timeout)
    elapsed = time.time() - started
    with open(out_path, 'a', encoding='utf-8') as fh:
        fh.write(proc.stdout or '')
    tail = (proc.stdout or '').strip().splitlines()[-6:]
    for line in tail:
        ctx.log.info('    %s' % line[:220])
    if proc.returncode != 0 and check:
        raise StageFailure('exit code %d' % proc.returncode)
    ctx.log.info('  完成 (%.1fs, exit=%d)' % (elapsed, proc.returncode))
    return proc.returncode


def snapshot_pages():
    pages = set(glob.glob(os.path.join(CONCEPTS_DIR, '*.md')))
    pages |= set(glob.glob(os.path.join(CONCEPTS_TOP, 'daily-*.md')))
    return pages


def page_doi(path):
    try:
        head = open(path, encoding='utf-8', errors='ignore').read(3000)
    except Exception:
        return ''
    # 用 raw string 一次写完，避免 '\s' 触发 DeprecationWarning（2026-11-03）
    m = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s"\n`]+)', head, re.M)
    return m.group(1).strip().rstrip('./') if m else ''


# ────────────────────────────── 阶段实现 ──────────────────────────────
def is_plant_content(text):
    try:
        from species_registry import CONTENT_SPECIES
    except Exception:
        CONTENT_SPECIES = ('plant', 'crop', 'leaf', 'root', 'flower', 'seed',
                           'rice', 'maize', 'wheat')
    t = (text or '').lower()
    return any(term in t for term in CONTENT_SPECIES)


def phase3_pubmed(ctx):
    timeout = ctx.args.phase3_timeout
    # 软预算 = 硬超时 - 120s：让 daily_update 自己收尾落盘并打印 PARTIAL/SUMMARY，
    # 而不是被 SIGKILL（线上 41/50 次被 300s 硬超时杀掉，输出只剩 "TIMEOUT"）。
    budget = max(60, timeout - 120)
    cmd = [PYTHON, '-u', ctx.script('daily_update.py'),
           '--days', str(ctx.args.lookback_days),
           '--max', str(ctx.args.max_papers),
           '--budget', str(budget), '--import']
    run_cmd(ctx, 'phase3_pubmed', cmd, timeout=timeout)


def phase3b_multisource(ctx):
    run_cmd(ctx, 'phase3b_multisource',
            [PYTHON, '-u', ctx.script('multi_source_search.py'),
             '--days', '365', '--max', '20',
             '--skip-s2', '--skip-web', '--skip-openalex'],
            timeout=900, check=False)
    import_multisource_candidates(ctx)


def import_multisource_candidates(ctx):
    candidates_file = ctx.script('multi_source_candidates.json')
    if not os.path.exists(candidates_file):
        ctx.log.warn('  多源检索无候选文件，跳过导入')
        return
    with open(candidates_file, encoding='utf-8') as fh:
        payload = json.load(fh)
    existing = {page_doi(p) for p in snapshot_pages()}
    existing.discard('')

    try:
        from theme_filter import is_relevant_plant_paper
    except Exception:
        is_relevant_plant_paper = None
    try:
        from purity_gate import classify as _purity
    except Exception:
        _purity = None
    try:
        from topic_gate import is_core_topic
    except Exception:
        is_core_topic = None

    imported = rejected = 0
    _oos_rows = []
    for paper in payload.get('candidates', []):
        doi = (paper.get('doi') or '').strip()
        if not doi or doi in existing:
            continue
        journal = paper.get('journal', '') or ''
        title = paper.get('title', '') or ''
        abstract = paper.get('abstract', '') or ''
        # 1) 主题相关性：所有来源统一执行。JCR 只是期刊先验，不是内容豁免。
        if is_relevant_plant_paper is not None:
            ok, why = is_relevant_plant_paper(title, abstract, journal)
            if not ok:
                ctx.log.info('  ⛔ 主题过滤拒绝 (%s): %s' % (why[:24], title[:48]))
                rejected += 1
                continue
        elif not is_plant_content(title + ' ' + abstract):
            rejected += 1
            continue

        # 2) 八主题相关性：挡住食品微生物、环境修复、材料等"植物相关但非本库主题"。
        if is_core_topic is not None:
            core_ok, core_why = is_core_topic(title, abstract, journal)
            if not core_ok:
                ctx.log.info('  ⛔ 主题相关性拒收 (%s): %s' % (core_why[:24], title[:48]))
                rejected += 1
                continue

        # 3) 领域纯度闸门（研究对象判定）：非植物研究一律不导入。
        #    必须在 JCR 分支之外，否则植物期刊里的动物/医学论文会直接绕过。
        if _purity is not None:
            verdict, preasons = _purity(title, abstract, journal, doi)
            if verdict == 'suspect' and 'insufficient-text' in preasons:
                # 判定不了（无标题/摘要过短/页面不可读）不能当 plant 放行。
                ctx.log.info('  \u26d4 文本不足拒收: %s' % (title[:48] or doi))
                rejected += 1
                continue
            if verdict == 'nonplant':
                ctx.log.info('  ⛔ 纯度闸门拒收 (%s): %s'
                             % (','.join(preasons[:2])[:24], title[:48]))
                rejected += 1
                continue
            if verdict == 'suspect':
                ctx.log.warn('  ⚠ 纯度待审 (%s): %s'
                             % (','.join(preasons[:2])[:24], title[:48]))
        slug = 'ms-' + re.sub(r'[^a-zA-Z0-9]+', '-', doi)[:60].strip('-')
        path = os.path.join(CONCEPTS_DIR, slug + '.md')
        if os.path.exists(path):
            continue
        authors = paper.get('authors') or []
        if authors and isinstance(authors[0], dict):
            authors = [a.get('name', '') for a in authors[:5]]
        year = paper.get('year', '')
        source = paper.get('source', 'unknown')
        # 2026-11-03：入库即写主题标签。旧实现硬写 tags: [papers]，
        # 之后证据页原样继承 → 全库 96.8% 的论文页无主题，八主题综述
        # 只能覆盖 22% 的证据。主题归属必须在入口处算一次，而不是靠
        # 事后回填。
        _tset, _tstat, _tbasis = _assign_import_themes(title, abstract)
        # 2026-11-03：out-of-scope 不再写 `themes: [other]`。
        # `other` 不是主题，写进去会被下游当成"已归属但无意义"，也是
        # 论文页 96.8% 无主题的由来之一。空就是空，如实写 []。
        _themes_fm = '[%s]' % ', '.join(sorted(_tset)) if _tset else '[]'
        if _tstat != 'mapped':
            _oos_rows.append({'doi': doi, 'pmid': '', 'title': title})
        with open(path, 'w', encoding='utf-8') as fh:
            fh.write('---\n')
            fh.write('title: %s\n' % yaml_str(title))
            fh.write('created: %s\n' % ctx.today)
            fh.write('type: concept\ntags: [papers]\n')
            fh.write('themes: %s\n' % _themes_fm)
            fh.write('theme_status: %s\ntheme_basis: %s\n'
                     % (_tstat, _tbasis or 'none'))
            fh.write('doi: %s\n' % doi)
            fh.write('confidence: moderate\nsource: %s\n---\n\n' % source)
            fh.write('# %s\n\n' % title)
            fh.write('## 论文信息\n')
            fh.write('- **期刊**: %s (%s)\n' % (journal, year))
            fh.write('- **DOI**: [%s](https://doi.org/%s)\n' % (doi, doi))
            fh.write('- **作者**: %s\n' % (', '.join(authors[:5]) or '—'))
            fh.write('- **来源**: %s\n\n' % source)
            fh.write('## 摘要\n%s\n\n' % (abstract or '（摘要需从原文获取）'))
            fh.write('## 深度提炼\n\n**物种**: —\n**来源**: %s | DOI:%s\n' % (source, doi))
        existing.add(doi)
        imported += 1
    if _oos_rows:
        _oos_path = os.path.join(BASE, '_review', 'out_of_scope_intake.tsv')
        os.makedirs(os.path.dirname(_oos_path), exist_ok=True)
        _new = not os.path.exists(_oos_path)
        with open(_oos_path, 'a', encoding='utf-8', newline='\n') as fh:
            if _new:
                fh.write('date\tdoi\tpmid\ttitle\n')
            for r in _oos_rows:
                fh.write('%s\t%s\t%s\t%s\n' % (
                    ctx.today, r.get('doi', ''), r.get('pmid', ''),
                    (r.get('title', '') or '').replace('\t', ' ')))
    ctx.stats['multisource_out_of_scope'] = len(_oos_rows)
    ctx.stats['multisource_imported'] = imported
    ctx.stats['multisource_rejected'] = rejected
    ctx.log.info('  多源导入 %d 篇（拒绝 %d，候选 %d）'
                 % (imported, rejected, payload.get('total', 0)))


def phase3c_journal(ctx):
    disabled = os.path.exists(os.path.join(BASE, '.phase3c_disable'))
    if disabled and not ctx.args.force_phase3c:
        raise SkipStage('存在 .phase3c_disable，已禁用（--force-phase3c 可强制）')
    run_cmd(ctx, 'phase3c_journal',
            [PYTHON, '-u', ctx.script('journal_focus_search.py'),
             '--core-only', '--days', str(ctx.args.lookback_days),
             '--max', '10', '--import'],
            timeout=2400)


def _assign_import_themes(title, abstract, keywords=None):
    """入库主题归属 —— 直接调用 themes.assign_for_import（唯一契约）。

    2026-11-03：这里原本是 themes.assign_themes 的复制实现，与
    daily_update.py 各写一套，规则必然漂移。现在只做转发。
    """
    try:
        import themes as _th
    except ImportError:
        return set(), 'out-of-scope', None
    return _th.assign_for_import(title, abstract, keywords)


def doi_slug(doi):
    """与 fetch_epmc_fulltext.doi_slug 保持一致（只做 '/'->'_'）。"""
    return doi.rstrip('./').replace('/', '_')


def _pdf_doi_index(outdir=None):
    """all_pdfs 下 PDF 文件名 -> 规范化 DOI 集合。

    2026-11-07：OA 通道（oa_locate.py）下载的 PDF 以 DOI 命名，不产生
    fulltext/*.txt。若覆盖率只认 .txt，"PDF 已到手"仍会被记成 0 篇全文，
    再次触发假 DEGRADED。覆盖率必须同时认两种载体。
    """
    d = outdir or PDF_DIR
    keys = set()
    try:
        names = os.listdir(d)
    except OSError:
        return keys
    for name in names:
        if not name.lower().endswith('.pdf'):
            continue
        m = re.search(r'(10\.\d{4,}[A-Za-z0-9._\-/]+)', name)
        if m:
            keys.add(m.group(1).lower().replace('_', '/').rstrip('.'))
    return keys


def text_coverage(dois, outdir=None):
    """返回"这些 DOI 中已有全文"的数量（覆盖率口径，不是增量口径）。

    2026-11-02 事故：阶段统计用"本次新增文件数"，当文件早已抓过时 delta=0，
    于是 40 篇全文在手却打印 "全文获取: 0/156" 并触发 DEGRADED——指标不可证伪。
    覆盖率必须直接按 DOI 查文件是否存在。

    2026-11-07：载体从"仅 JATS .txt"扩展为 ".txt 或 PDF"，避免 OA 通道
    下载成功后仍报 0。
    """
    d = outdir or os.path.join(RAW_DIR, 'papers', 'fulltext')
    pdf_keys = _pdf_doi_index()
    n = 0
    for doi in dois:
        p = os.path.join(d, doi_slug(doi) + '.txt')
        try:
            if os.path.getsize(p) > 0:
                n += 1
                continue
        except OSError:
            pass
        if doi.lower().rstrip('./').replace('_', '/') in pdf_keys:
            n += 1
    return n


def _pdf_snapshot():
    try:
        return set(n for n in os.listdir(PDF_DIR) if n.lower().endswith('.pdf'))
    except OSError:
        return set()


def _text_snapshot():
    """Europe PMC JATS 转写的全文（raw/papers/fulltext/*.txt）快照。"""
    d = os.path.join(RAW_DIR, 'papers', 'fulltext')
    try:
        return set(n for n in os.listdir(d) if n.endswith('.txt') and not n.startswith('_'))
    except OSError:
        return set()


def phase4_fulltext(ctx):
    dois = _today_dois(ctx)
    if not dois:
        raise SkipStage('今日无新增 DOI')
    tmp = os.path.join(BASE, '.phase4_today_dois.txt')
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(dois))
    ctx.temp_files.append(tmp)
    ctx.stats['pdf_candidates'] = len(dois)
    before = _pdf_snapshot()
    run_cmd(ctx, 'phase4_fulltext',
            [PDF_PYTHON, '-u', ctx.script('download_epmc.py'),
             '--from-file', tmp, '--outdir', os.path.join(RAW_DIR, 'papers', 'all_pdfs')],
            timeout=2400, check=False)
    gained = len(_pdf_snapshot() - before)
    ctx.stats['pdf_acquired'] = gained

    # 第二通道：Europe PMC JATS 全文 -> 纯文本。
    # 2026-11-02 线上实证：两个 PDF 端点对脚本请求均返回 403，PDF 成功率 0/37；
    # 同一天 fullTextXML 仍是 200。没有这一通道，整天只能产出摘要级页面。
    base = _text_snapshot()
    run_cmd(ctx, 'phase4_fulltext_xml',
            [PYTHON, '-u', ctx.script('fetch_epmc_fulltext.py'),
             '--from-file', tmp, '--outdir', os.path.join('raw', 'papers', 'fulltext')],
            timeout=1800, check=False)
    text_gained = len(_text_snapshot() - base)
    ctx.stats['fulltext_text_acquired'] = text_gained

    # 第三通道：Unpaywall + OpenAlex（开放获取定位）。
    # 2026-11-07 起：前两条通道都依赖 PMC 收录，订阅制期刊必然 0 命中；
    # 当天 21 篇全部 no_pmc，导致"全文 0/21、深度提炼 0/21"连续两天出现。
    # 本通道只针对仍未拿到全文的 DOI，避免重复请求。
    still_missing = [d for d in dois if text_coverage([d]) == 0]
    ctx.stats['fulltext_oa_candidates'] = len(still_missing)
    if still_missing:
        tmp_oa = os.path.join(BASE, '.phase4_oa_dois.txt')
        with open(tmp_oa, 'w', encoding='utf-8') as fh:
            fh.write('\n'.join(still_missing))
        ctx.temp_files.append(tmp_oa)
        run_cmd(ctx, 'phase4_oa_locate',
                [PYTHON, '-u', ctx.script('oa_locate.py'),
                 '--from-file', tmp_oa,
                 '--outdir', os.path.join(RAW_DIR, 'papers', 'all_pdfs')],
                timeout=1800, check=False)
    oa_covered = text_coverage(still_missing) if still_missing else 0
    ctx.stats['fulltext_oa_acquired'] = oa_covered

    covered = text_coverage(dois)
    ctx.stats['fulltext_text_covered'] = covered
    ctx.stats['fulltext_acquired'] = covered
    ctx.log.info('  全文可用(XML): %d/%d；本次新增 PDF %d 篇、新增 XML %d 篇'
                 % (covered, len(dois), gained, text_gained))
    if covered == 0 and gained == 0:
        ctx.degrade('全文获取 0/%d（Europe PMC + OA 通道均未取得全文，'
                    '后续提炼退化为摘要级）' % len(dois))
    elif covered < len(dois):
        ctx.degrade('全文仅覆盖 %d/%d（其余为摘要级）' % (covered, len(dois)))


def phase4b_fallback(ctx):
    script = ctx.script('fill_missing_pdfs.py')
    if not os.path.exists(script):
        raise SkipStage('fill_missing_pdfs.py 未随公开仓库发布（非 OA 通道）')
    dois = _today_dois(ctx)
    if not dois:
        raise SkipStage('今日无新增 DOI')
    tmp = os.path.join(BASE, '.phase4_today_dois.txt')
    cmd = [PDF_PYTHON, '-u', script, '--from-file', tmp, '--workers', '4',
           '--skip-deep', '--outdir', os.path.join(RAW_DIR, 'papers', 'daily_new')]
    if ctx.args.allow_scihub:
        cmd.append('--scihub')
    run_cmd(ctx, 'phase4b_fallback', cmd, timeout=2400, check=False)


def phase4c_merge(ctx):
    daily_new = os.path.join(RAW_DIR, 'papers', 'daily_new')
    if not os.path.isdir(daily_new):
        raise SkipStage('无 daily_new 暂存目录')
    try:
        from download_epmc import is_plant_doi
    except Exception:
        is_plant_doi = lambda doi: True
    known = set()
    for name in os.listdir(PDF_DIR):
        m = re.search(r'(10\.\d{4,}[^\s/]+)', name)
        if m:
            known.add(m.group(1).replace('_', '/').rstrip('.').lower())
    moved = dropped = 0
    for name in os.listdir(daily_new):
        if not name.lower().endswith('.pdf'):
            continue
        src = os.path.join(daily_new, name)
        m = re.search(r'(10\.\d{4,}[^\s/]+)', name)
        if not m:
            continue
        doi = m.group(1).replace('_', '/').rstrip('.')
        if not is_plant_doi(doi):
            dropped += 1
            continue
        if doi.lower() in known:
            os.remove(src)
            continue
        shutil.move(src, os.path.join(PDF_DIR, name))
        known.add(doi.lower())
        moved += 1
    ctx.stats['pdf_merged'] = moved
    ctx.log.info('  daily_new 归并 %d 个，拦截非植物 %d 个' % (moved, dropped))


def phase5_deep_curate(ctx):
    dois = _today_dois(ctx)
    if not dois:
        raise SkipStage('今日无新增 DOI')
    tmp = os.path.join(BASE, '.temp_new_dois.txt')
    with open(tmp, 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(dois))
    ctx.temp_files.append(tmp)
    run_cmd(ctx, 'phase5_deep_curate',
            [PDF_PYTHON, '-u', ctx.script('deep_curate_all.py'), '--dois', tmp],
            timeout=3600)
    curated = 0
    for path in ctx.today_pages:
        try:
            text = open(path, encoding='utf-8', errors='ignore').read()
        except Exception:
            continue
        if '**物种**:' in text and '### 核心发现' in text:
            curated += 1
    ctx.stats['curated_new'] = curated
    ctx.stats['curated_ratio'] = '%d/%d' % (curated, len(ctx.today_pages))
    ctx.log.info('  今日深度提炼 %d/%d 篇' % (curated, len(ctx.today_pages)))
    if ctx.today_pages and curated == 0:
        # 线上实测: 45 次运行中 30 次提炼 0 篇，但提交信息仍写 "curated X/Y"，
        # 读者无法区分"没有全文可提炼"与"提炼流程坏了"。必须显式降级记账。
        ctx.degrade('深度提炼 0/%d 篇（无全文或提炼失败）' % len(ctx.today_pages))
    elif ctx.today_pages and curated < len(ctx.today_pages):
        ctx.degrade('深度提炼仅覆盖 %d/%d 篇' % (curated, len(ctx.today_pages)))


def _today_page_paths(ctx):
    """当日概念页集合：优先用本次运行的导入结果，否则回落到磁盘。

    2026-11-03 第 9 轮修复：`--only phase5_5_purity` 这类定向补跑时
    ctx.today_pages 为空（它只在 phase3 导入后填充），两个闸门于是静默
    SKIP——"闸门改了但真实运行里没生效"正是这么来的。定向补跑必须扫磁盘。
    """
    if ctx.today_pages:
        return list(ctx.today_pages)
    try:
        return pages_created_on(ctx.today)
    except Exception:
        return []


def phase5_5_purity(ctx):
    """导入层纯度闸门（2026-11-02 新增，必须在 phase6 之前）。

    为什么不在 phase8_5 做：那里只打印告警、不移动页面，且排在
    synthesis/hypotheses 之后 —— 污染页早已产出证据、进入登记表与人工浏览。
    用户原话：「纯度闸门只在下载层，导入层没拦」，2026-11-02 的 156 篇里
    仍有肉鸡生产性能、4D 打印组织再生、人参外泌体治结肠炎等明显非植物论文。

    判定与 organism_scope.paper_scope_table 同源（label + method 两维），
    只移动 A 类（label=nonplant 且 method=False）；B 类零信号页仅写待审清单。
    """
    pages = _today_page_paths(ctx)
    if not pages:
        raise SkipStage('今日无新增页')
    run_cmd(ctx, 'phase5_5_purity',
            [PYTHON, '-u', ctx.script('quarantine_nonplant_pages.py'),
             '--date', ctx.today, '--apply'],
            timeout=600, check=False)
    tsv = os.path.join(BASE, '_review', 'nonplant_quarantine_%s.tsv' % ctx.today)
    n = 0
    if os.path.exists(tsv):
        with open(tsv, encoding='utf-8') as fh:
            n = max(0, sum(1 for _ in fh) - 1)
    ctx.stats['purity_quarantined'] = n
    if n:
        # TSV 记录的是"当日累计隔离"，多次运行会重复计数同一批页，
        # 因此措辞必须写"当日累计"，不能写成"本次隔离"。
        ctx.log.warn('  纯度闸门：当日累计隔离 %d 篇非植物页（已归档，可回滚）' % n)


def phase5_6_topic_quarantine(ctx):
    """主题越界回抓（2026-11-03 第 9 轮新增，紧接 phase5_5 之后）。

    phase5_5 只处理"研究对象不是植物"。它挡不住"研究的是植物，但科学问题
    不属于本库八个主题"的论文：鲜食微生物与沙门氏菌、茶多酚抑菌、苹果汁
    保鲜膜、酸性矿山废水、纳米塑料等。2026-11-03 当日 69 页里有 15 页属于
    这一类，自检 FAIL 的根因就在这里。

    判据与 pipeline_selfcheck.today_pages_scope 完全同源（直接 import
    organism_scope / topic_gate），只移动不删除，产物落入
    _review/archive/topic_<date>/，可整目录回滚。
    """
    pages = _today_page_paths(ctx)
    if not pages:
        raise SkipStage('今日无新增页')
    run_cmd(ctx, 'phase5_6_topic_quarantine',
            [PYTHON, '-u', ctx.script('quarantine_offtopic_pages.py'),
             '--date', ctx.today, '--apply'],
            timeout=900, check=False)
    tsv = os.path.join(BASE, '_review', 'topic_quarantine_%s.tsv' % ctx.today)
    n = 0
    if os.path.exists(tsv):
        with open(tsv, encoding='utf-8') as fh:
            n = max(0, sum(1 for _ in fh) - 1)
    ctx.stats['topic_quarantined'] = n
    if n:
        ctx.log.warn('  主题闸门：当日累计隔离 %d 篇非八主题页（已归档，可回滚）' % n)


def phase6_evidence(ctx):
    """证据对象与实体增量更新。

    2026-11-02 线上事故：全量重写在 9p 挂载（G:）上偶发超过 900s 被杀，
    导致当天 phase6 之后的全部阶段（关系、假设、校验、commit）都没有执行。
    证据层是派生数据、且脚本幂等，因此改为：
      1) 默认只处理最近 2 天改动过的概念页（--changed-only），实体页仍按全库索引聚合；
      2) 超时/失败重试一次；
      3) 仍失败则降级并继续，而不是让整条管线停摆。
    """
    cmd = [PYTHON, '-u', ctx.script('batch_evidence_objects.py'),
           '--changed-only', '--since-days', '2', '--report-orphans']
    last = None
    for attempt in (1, 2):
        try:
            run_cmd(ctx, 'phase6_evidence', cmd, timeout=1800, check=True)
            return
        except StageFailure as exc:
            last = exc
            ctx.log.warn('  phase6_evidence 第 %d 次尝试失败: %s' % (attempt, exc))
    ctx.degrade('证据对象更新失败（已重试 1 次）：%s；关系/假设层沿用上一版证据' % last)


def phase6a_nonplant_repair(ctx):
    """证据层非植物残留回抓（2026-11-02 第 25 轮接入）。

    为什么需要单独一步：phase5_5 闸门只拦"今日页面 → 证据"的主通路。
    repair_nonplant_import.py 早在第 24 轮就写好了，但**从未接入任何管线**
    （全仓 grep 只命中自身与一处注释），属于"写了不跑"。
    它负责两件事：
      1) drop 类（label=nonplant 且 method=False）论文残留的证据对象 → 归档；
      2) 对应概念页打 scope_status: excluded-nonplant + 顶部横幅（不移动页面，
         避免一次性打断大量链接）。
    不做的后果（线上实测）：孤儿证据虚高 281 条、人工浏览 KB 会看到肉鸡/
    结肠炎/4D 打印的断言。

    幂等且便宜：全库概念页索引 ~25s，无残留时 0 条。
    """
    rc = run_cmd(ctx, 'phase6a_nonplant_repair',
                 [PYTHON, '-u', ctx.script('repair_nonplant_import.py'), '--apply'],
                 timeout=600, check=False)
    if rc != 0:
        ctx.degrade('非植物证据回抓失败（exit=%s），孤儿证据统计可能虚高' % rc)


def phase6b_relationships(ctx):
    run_cmd(ctx, 'phase6b_relationships',
            [PYTHON, '-u', ctx.script('batch_relationships_v2.py')],
            timeout=600, check=False)


def _verified_generate(ctx, key, script, update_timeout, label, allow_degraded=True):
    """生成 → 校验 的两段式执行。

    之前这三步一律 check=False，导致"生成失败/生成了不自洽的页面"都能让流水线
    显示成功。现在把失败分成三档：
      - 退出码 1（--check 发现页面与证据不一致）→ degrade，不静默通过；
      - 退出码 2（--update 报 failures/degraded）→ degrade（可配置为致命）；
      - 退出码 >=3 / 超时 → StageFailure，由调度层报警。
    """
    pre = run_cmd(ctx, key + '_precheck',
                  [PYTHON, '-u', ctx.script(script), '--check'],
                  timeout=600, check=False)
    if pre == 1:
        ctx.degrade('%s：刷新前已存在不自洽页面（本次刷新会覆盖，但请核查历史原因）' % label)
    rc = run_cmd(ctx, key,
                 [PYTHON, '-u', ctx.script(script), '--update'],
                 timeout=update_timeout, check=False)
    if rc == 1:
        raise StageFailure('%s --update 失败（exit=1）' % label)
    if rc == 2 and not allow_degraded:
        raise StageFailure('%s --update 报告 degraded/failures（exit=2）' % label)
    if rc == 2:
        ctx.degrade('%s：部分页面降级输出（证据不足，已写诊断页）' % label)
    post = run_cmd(ctx, key + '_check',
                   [PYTHON, '-u', ctx.script(script), '--check'],
                   timeout=600, check=False)
    if post == 1:
        ctx.degrade('%s：刷新后仍有不自洽页面（校验未通过）' % label)
    return rc


def phase7_synthesis(ctx):
    _verified_generate(ctx, 'phase7_synthesis', 'batch_synthesis.py',
                       1200, '综合页刷新')
    # 正文重建（2026-11-03）：batch_synthesis 只重写统计块与范围句，
    # 正文仍是历史手写/旧 LLM 内容，会出现“数字新、正文旧”。
    # 这一步按当前证据确定性重建 8 页正文，并把旧正文归档到
    # _review/synthesis_legacy_<date>/。不进此步的话，#5 的修复次日就会被覆盖回去。
    rc = run_cmd(ctx, 'phase7b_synthesis_body',
                 [PYTHON, '-u', ctx.script('rebuild_synthesis_body.py'), '--apply'],
                 timeout=900, check=False)
    if rc != 0:
        ctx.degrade('综合页正文重建失败（rc=%d）' % rc)


def phase8_hypotheses(ctx):
    _verified_generate(ctx, 'phase8_hypotheses', 'batch_hypotheses.py',
                       900, '假说与研究方案生成')


def phase8_5_pollution(ctx):
    try:
        from theme_filter import is_relevant_plant_paper
    except Exception as exc:
        raise SkipStage('theme_filter 不可用: %s' % exc)
    try:
        from purity_gate import classify_page as _classify_page
    except Exception:
        _classify_page = None
    flagged = []
    suspect = []
    for path in ctx.today_pages:
        try:
            content = open(path, encoding='utf-8', errors='ignore').read(3000)
        except Exception:
            continue
        tm = re.search(r'^#\s+(.+)$', content, re.M)
        title = tm.group(1).strip() if tm else ''
        am = re.search(r'## 摘要\s*\n+(.*?)(?=\n##|\Z)', content, re.DOTALL)
        abstract = re.sub(r'\s+', ' ', am.group(1)) if am else ''
        jm = re.search(r'期刊\*\*:?\s*(.+)', content)
        journal = re.sub(r'\*\*DOI\*\*.*', '', jm.group(1)).split('(')[0].strip() if jm else ''
        if not title and not abstract:
            continue
        ok, why = is_relevant_plant_paper(title, abstract, journal)
        if _classify_page is not None:
            verdict, preasons = _classify_page(path)
            if verdict == 'nonplant':
                flagged.append((os.path.basename(path),
                                'nonplant:' + ','.join(preasons[:2]), title[:50]))
                continue
            if verdict == 'suspect':
                suspect.append((os.path.basename(path), ','.join(preasons[:2]), title[:50]))
                continue
        if not ok:
            flagged.append((os.path.basename(path), why, title[:50]))
    ctx.stats['pollution_flagged'] = len(flagged)
    ctx.stats['purity_suspect'] = len(suspect)
    if suspect:
        ctx.log.warn('  纯度待审：%d 篇信号冲突（已导入，需人工确认）' % len(suspect))
        for name, why, title in suspect:
            ctx.log.warn('    [%s] %s' % (why[:26], title))
    if flagged:
        ctx.log.warn('  污染自检：%d 篇被标非植物，需人工复核' % len(flagged))
        for name, why, title in flagged:
            ctx.log.warn('    [%s] %s' % (why[:26], title))
    else:
        ctx.log.info('  污染自检通过：0 篇被标非植物')


def phase8_6_registry(ctx):
    run_cmd(ctx, 'phase8_6_registry',
            [PDF_PYTHON, '-u', ctx.script('pdf_concept_registry.py'),
             '--concepts', CONCEPTS_DIR, '--pdfs', PDF_DIR,
             '--out-dir', os.path.join(RAW_DIR, 'papers', 'maps')],
            timeout=900, check=False)


def phase8_7_validate(ctx):
    """知识库体检：只读，发现问题只记录不阻断当日更新。

    两个互补的检查：
      1. validate_kb.py      —— 全库结构（断链/字段/占位符/覆盖率）
      2. batch_synthesis.py --check —— synthesis 页面的数字自洽性
         （frontmatter 与正文计数必须同源；不得残留占位符或拼接残骸）
    """
    script = ctx.script('validate_kb.py')
    if not os.path.exists(script):
        raise SkipStage('validate_kb.py 不存在')
    rc = run_cmd(ctx, 'phase8_7_validate', [PYTHON, '-u', script], timeout=900, check=False)
    if rc != 0:
        ctx.log.warn('体检未通过（见上方输出），已记录但不阻断流水线')

    synth = ctx.script('batch_synthesis.py')
    if os.path.exists(synth):
        rc2 = run_cmd(ctx, 'phase8_7_validate', [PYTHON, '-u', synth, '--check'],
                      timeout=900, check=False)
        if rc2 != 0:
            ctx.log.warn('synthesis 页面存在数字不一致/占位符残留（见上方输出），已记录但不阻断')
    return rc


def phase8_8_titles(ctx):
    """H1 标题修复（2026-11-03 第 9 轮）。

    为什么需要独立一步：phase8_7 只做只读体检，标题坏了没人修；而标题是
    Obsidian 里唯一可见的入口。这里用 frontmatter 的 title 回填 H1，
    只用已有元数据、不造句；确实补不上的登记 title_status: unresolved。
    """
    script = ctx.script('repair_page_titles.py')
    if not os.path.exists(script):
        raise SkipStage('repair_page_titles.py 不存在')
    run_cmd(ctx, 'phase8_8_titles', [PYTHON, '-u', script,
                                     '--date', ctx.today, '--apply'],
            timeout=900, check=False)


def phase9_translate(ctx):
    script = ctx.script('batch_translate_metabolism.py')
    if not os.path.exists(script):
        raise SkipStage('batch_translate_metabolism.py 不存在')
    run_cmd(ctx, 'phase9_translate', [PYTHON, '-u', script, '--today'],
            timeout=1200, check=False)


QSTART = '<!-- QUARANTINE:START -->'
QEND = '<!-- QUARANTINE:END -->'


def _read_tsv_rows(path, ncol):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, encoding='utf-8') as fh:
        head = fh.readline()
        for line in fh:
            parts = line.rstrip('\n').split('\t')
            if len(parts) >= 2:
                rows.append(parts[:ncol] + [''] * (ncol - len(parts[:ncol])))
    return rows


def append_quarantine_block(ctx):
    """把当日隔离结果写进 daily_report.md（2026-11-03 第 9 轮）。

    为什么必须写进报告：日报此前只在导入时记账，隔离发生在导入之后，
    于是"已导入"的坏页被移走后报告仍显示"待审已导入"，读者无法判断
    到底有没有处置。这里按当日两份 TSV（非植物 / 主题越界）汇总。
    """
    report = os.path.join(BASE, 'daily_report.md')
    if not os.path.exists(report):
        return
    nonplant = _read_tsv_rows(os.path.join(
        BASE, '_review', 'nonplant_quarantine_%s.tsv' % ctx.today), 5)
    topic = _read_tsv_rows(os.path.join(
        BASE, '_review', 'topic_quarantine_%s.tsv' % ctx.today), 4)
    lines = [QSTART, '', '## 当日隔离与回抓（自动生成）', '']
    lines.append('| 类别 | 篇数 | 归档位置 |')
    lines.append('|---|---:|---|')
    lines.append('| 非植物研究对象（phase5_5） | %d | `_review/archive/nonplant_%s/` |'
                 % (len(nonplant), ctx.today))
    lines.append('| 非八主题（phase5_6） | %d | `_review/archive/topic_%s/` |'
                 % (len(topic), ctx.today))
    lines.append('')
    if topic:
        lines.append('### 非八主题隔离明细')
        lines.append('')
        for r in topic:
            lines.append('- `%s` — %s' % (r[0], r[1]))
        lines.append('')
    if nonplant:
        lines.append('### 非植物隔离明细')
        lines.append('')
        for r in nonplant:
            lines.append('- `%s` %s — %s' % (r[4], r[0], r[3]))
        lines.append('')
    lines.append('> 隔离=移动到 `_review/archive/` 下按日期分目录，未删除、可整目录回滚；'
                 '证据对象同步归档。')
    lines.append('')
    lines.append(QEND)
    block = '\n'.join(lines)

    with open(report, encoding='utf-8') as fh:
        text = fh.read()
    import re as _re
    if QSTART in text and QEND in text:
        text = _re.sub(_re.escape(QSTART) + r'.*?' + _re.escape(QEND), block, text, flags=_re.S)
    else:
        text = text.rstrip() + '\n\n' + block + '\n'
    with open(report, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(text)
    ctx.log.info('  隔离登记：非植物 %d 篇，非八主题 %d 篇' % (len(nonplant), len(topic)))


def phase9_5_selfcheck(ctx):
    """运行后闭环自检（2026-11-03 第 9 轮新增，排在翻译之后、git 之前）。

    为什么必须进流水线：前面已多次出现"脚本改了、日报还是老文案"的事故，
    根因是没有人真的在真实运行里看见结果。把 7 项检查（闸门回放、当日越界
    复查、文献类型分层、综合/假说证据一致、标题异常、证据类型完整性、日报
    计数诚实性）挂到日报末尾，第二天的 08:00 运行会自己证明闸门是否生效。
    """
    try:
        append_quarantine_block(ctx)
    except Exception as exc:
        ctx.log.warn('  隔离登记写入失败（不阻断）：%s' % exc)
    script = ctx.script('pipeline_selfcheck.py')
    if not os.path.exists(script):
        raise SkipStage('pipeline_selfcheck.py 不存在')
    # --strict：有 FAIL 就以非 0 退出，才能被下面的 degrade 捕获；
    # 旧版不带 --strict 时脚本恒返回 0，FAIL 只写进报表末尾，cron 永远看不到。
    rc = run_cmd(ctx, 'phase9_5_selfcheck', [PYTHON, '-u', script, '--strict'],
                 timeout=1800, check=False)
    if rc != 0:
        ctx.degrade('闭环自检存在 FAIL 项（详见 daily_report.md 末段）')
    return rc


def git_commit(ctx):
    if not os.path.isdir(os.path.join(BASE, '.git')):
        raise SkipStage('非 git 仓库')
    # raw/ 在 .gitignore 中；把 raw/papers/maps 混进 git add 会让整次 add 返回 1，
    # 知识层当天完全不进版本历史。逐个检查 ignored，只提交可跟踪目录。
    # 知识层 + 审计层。审计层（_review/、日报、索引、日志）此前不在白名单，
    # 导致每天固定漏提交 10+ 个文件，脏工作区长期累积。_review/ 下的 PDF 由
    # .gitignore 的 *.pdf 排除，git add 会自动跳过，不会把二进制带进仓库。
    paths = ['concepts', 'evidence', 'entities', 'relationships', 'synthesis',
             'hypotheses', 'research-programs', 'raw/papers/maps',
             'comparisons', 'diagrams', 'queries',
             'daily_report.md', 'index.md', 'log.md', '.epmc_fail.log',
             'scripts/multi_source_candidates.json', 'journal_focus_search.ids',
             '_review']
    existing = []
    for rel in paths:
        if not os.path.exists(os.path.join(BASE, rel)):
            continue
        ignored = subprocess.run(['git', 'check-ignore', '-q', '--', rel],
                                 cwd=BASE).returncode == 0
        if ignored:
            ctx.log.info('  git ignored, skip: %s' % rel)
            continue
        existing.append(rel)
    if not existing:
        raise SkipStage('无可提交目录（全部被 gitignore）')
    # -A: 必须能暂存删除；只用 `git add --` 时被删除的页面永远进不了版本历史。
    run_cmd(ctx, 'git_commit', ['git', 'add', '-A', '--'] + existing, timeout=600)
    status = subprocess.run(['git', 'diff', '--cached', '--name-only'],
                            cwd=BASE, capture_output=True, text=True)
    if not (status.stdout or '').strip():
        raise SkipStage('无待提交变更')
    msg = 'daily: %s — %s new papers, curated %s' % (
        ctx.today, ctx.stats.get('new_pages', 0), ctx.stats.get('curated_ratio', '0/0'))
    # 提交信息必须反映真实质量：0/N 提炼不能写得像正常完成。
    if ctx.stats.get('degraded'):
        msg += ' [degraded: %d]' % len(ctx.stats['degraded'])
    staged_count = sum(1 for ln in status.stdout.splitlines() if ln.strip())
    if staged_count > 3000:
        # 治理保护：单次提交超过 3000 个路径说明前面积压未提交，需人工分批。
        raise RuntimeError('待提交路径 %d 超过阈值 3000，需人工分批提交'
                           % staged_count)
    run_cmd(ctx, 'git_commit', ['git', 'commit', '-m', msg, '--no-verify'], timeout=300)
    ctx.stats['git_committed'] = True
    ctx.stats['git_staged'] = staged_count
    # 提交后闭环校验：若仍有非忽略的未提交变更，说明白名单又漏了路径。
    # 不抛错（避免一天的知识因子目录遗漏而整轮判失败），但要留痕并进 stats，
    # 由自检/日报暴露，防止"每天漏几个文件"再次静默复发。
    residual = subprocess.run(['git', 'status', '--porcelain'],
                              cwd=BASE, capture_output=True, text=True).stdout.strip()
    if residual:
        lines = residual.splitlines()
        ctx.stats['git_residual'] = len(lines)
        ctx.log.warn('  提交后仍有 %d 项未提交变更（白名单可能遗漏路径）：' % len(lines))
        for ln in lines[:12]:
            ctx.log.warn('    ' + ln)


def _proxy_env():
    """返回注入了 HTTP(S) 代理的环境变量副本。

    背景（2026-11-17 实测）：本机 github.com:443 直连不可达，需经 Windows 侧
    Clash 混合端口 7897。WSL 的默认网关 IP 每次重启都会变，因此这里每次动态
    解析，绝不把代理写进 git config（否则换网关即失效，且污染仓库配置）。
    """
    env = dict(os.environ)
    if env.get('HTTPS_PROXY') or env.get('https_proxy'):
        return env
    gw = ''
    try:
        route = subprocess.run(['ip', 'route'], capture_output=True,
                               text=True, timeout=10).stdout
    except Exception:
        route = ''
    for line in (route or '').splitlines():
        if line.startswith('default'):
            parts = line.split()
            if len(parts) > 2:
                gw = parts[2]
                break
    if gw:
        proxy = 'http://%s:7897' % gw
        for k in ('HTTPS_PROXY', 'HTTP_PROXY', 'ALL_PROXY',
                  'https_proxy', 'http_proxy', 'all_proxy'):
            env[k] = proxy
    return env


def _report_append_notice(ctx, text):
    """把收尾阶段（git_push）的问题追加到日报末尾。

    日报正文由 phase9_5_selfcheck 生成，早于 git_commit/git_push，因此推送失败
    无法通过 ctx.degrade 进入当天日报。这里直接追加，保证失败在日报里可见，
    而不是只躺在 logs/pipeline/ 里。
    """
    path = os.path.join(BASE, 'daily_report.md')
    marker = '<!-- postrun-notice -->'
    try:
        with open(path, encoding='utf-8', errors='ignore') as fh:
            body = fh.read()
    except OSError:
        return
    if marker in body:
        body = body.split(marker)[0].rstrip() + '\n'
    stamp = datetime.now().strftime('%Y-%m-%d %H:%M')
    body += '\n%s\n## ⚠ 收尾阶段未完成（%s）\n\n%s\n' % (marker, stamp, text)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(body)
    os.replace(tmp, path)


def git_push(ctx):
    if not ctx.stats.get('git_committed'):
        raise SkipStage('本次未产生提交')
    env = _proxy_env()
    if env.get('HTTPS_PROXY'):
        ctx.log.info('  git push 使用代理 %s' % env['HTTPS_PROXY'])
    rc = run_cmd(ctx, 'git_push', ['git', 'push'], timeout=600,
                 check=False, env=env)
    # 2026-11-17 修复「假绿」：此前 check=False 且不看返回码，推送失败
    # （日志里同时出现 "RPC failed; curl 28" 与 "Everything up-to-date"）
    # 仍被记成 ok，导致「每天提交、实际没推上去」长期无人发现。
    head = subprocess.run(['git', 'rev-parse', 'HEAD'], cwd=BASE,
                          capture_output=True, text=True).stdout.strip()
    remote = subprocess.run(['git', 'rev-parse', 'origin/main'], cwd=BASE,
                            capture_output=True, text=True).stdout.strip()
    pushed = (rc == 0 and bool(head) and head == remote)
    ctx.stats['git_push_rc'] = rc
    ctx.stats['git_pushed'] = pushed
    if not pushed:
        detail = ('git push 未把当日提交送上远端：exit=%d，HEAD=%s，origin/main=%s。'
                  '当日知识未进入 GitHub 版本历史，违反可回滚前提。'
                  '日志目录：%s'
                  % (rc, head[:10] or '?', remote[:10] or '?', ctx.log.run_dir))
        ctx.degrade(detail)
        _report_append_notice(ctx, detail)
        raise StageFailure('git push 失败（exit=%d）' % rc)
    ctx.log.info('  git push 已确认：HEAD == origin/main (%s)' % head[:10])


class SkipStage(Exception):
    """阶段被有意跳过（非失败）。"""


def page_created(path):
    try:
        head = open(path, encoding='utf-8', errors='ignore').read(1200)
    except Exception:
        return ''
    m = re.search(r'^created:\s*(\d{4}-\d{2}-\d{2})', head, re.M)
    return m.group(1) if m else ''


def pages_created_on(day):
    """返回 frontmatter created 日期等于 day 的概念页（回放/补跑共用）。"""
    return sorted(p for p in snapshot_pages() if page_created(p) == day)


def _today_dois(ctx):
    dois = []
    for path in ctx.today_pages:
        doi = page_doi(path)
        if doi and doi not in dois:
            dois.append(doi)
    return dois


def build_stages(args):
    return [
        Stage('phase3_pubmed', 'PubMed 主题×物种检索与导入', phase3_pubmed,
              1800, True, ('daily_update.py',)),
        Stage('phase3b_multisource', 'OpenAlex/Crossref 补充检索与导入', phase3b_multisource,
              900, False, ('multi_source_search.py',)),
        Stage('phase3c_journal', '白名单期刊×主题双限定检索', phase3c_journal,
              2400, False, ('journal_focus_search.py',)),
        Stage('phase4_fulltext', 'Europe PMC 开放获取全文下载', phase4_fulltext,
              2400, False, ('download_epmc.py',), when=lambda c: c.has_new),
        Stage('phase4b_fallback', '非 OA 兜底通道（可选）', phase4b_fallback,
              2400, False, ('fill_missing_pdfs.py',), default_enabled=False,
              when=lambda c: c.has_new),
        Stage('phase4c_merge', 'daily_new 归并去重', phase4c_merge,
              600, True, (), when=lambda c: c.has_new),
        Stage('phase5_deep_curate', '当日新增文献深度提炼', phase5_deep_curate,
              3600, True, ('deep_curate_all.py',), when=lambda c: c.has_new),
        # 2026-11-03：去掉 when=has_new。定向补跑(--only)时 has_new 恒为 False，
        # 闸门会被无声跳过；是否执行改由函数内部按磁盘当日页面判断。
        Stage('phase5_5_purity', '导入层纯度闸门（非植物隔离）', phase5_5_purity,
              600, True, ('quarantine_nonplant_pages.py',)),
        Stage('phase5_6_topic_quarantine', '主题越界回抓（非八主题隔离）',
              phase5_6_topic_quarantine, 1200, False,
              ('quarantine_offtopic_pages.py',)),
        Stage('phase6_evidence', '证据对象与实体增量更新', phase6_evidence,
              1800, False, ('batch_evidence_objects.py',)),
        Stage('phase6a_nonplant_repair', '非植物证据残留回抓（打标+归档）',
              phase6a_nonplant_repair, 600, False,
              ('repair_nonplant_import.py',)),
        Stage('phase6b_relationships', '关系层增量生成', phase6b_relationships,
              600, False, ('batch_relationships_v2.py',)),
        Stage('phase7_synthesis', '综合页增量刷新', phase7_synthesis,
              2100, False, ('batch_synthesis.py', 'rebuild_synthesis_body.py')),
        Stage('phase8_hypotheses', '假说与研究方案生成', phase8_hypotheses,
              900, False, ('batch_hypotheses.py',)),
        Stage('phase8_5_pollution', '当日新增页污染自检', phase8_5_pollution,
              300, True, ()),
        Stage('phase8_6_registry', 'PDF↔概念页溯源登记表', phase8_6_registry,
              900, False, ('pdf_concept_registry.py',)),
        Stage('phase8_7_validate', '知识库结构体检 + 综合页自洽（只读）', phase8_7_validate,
              900, False, ('validate_kb.py',)),
        Stage('phase8_8_titles', 'H1 标题修复（回填/登记待补）',
              phase8_8_titles, 900, False,
              ('repair_page_titles.py',)),
        Stage('phase9_translate', '标题翻译与交叉引用（可选）', phase9_translate,
              1200, False, ('batch_translate_metabolism.py',)),
        Stage('phase9_5_selfcheck', '运行后闭环自检（写入日报）',
              phase9_5_selfcheck, 1800, False,
              ('pipeline_selfcheck.py',)),
        Stage('git_commit', '提交知识层变更', git_commit, 300, False, ()),
        Stage('git_push', '推送远端', git_push, 600, False, ()),
    ]


# ────────────────────────────── 预检 ──────────────────────────────
def preflight(ctx, stages, args):
    problems = []
    warnings = []
    for key in ('concepts', 'evidence', 'entities', 'relationships', 'synthesis',
                'hypotheses', 'research-programs'):
        if not os.path.isdir(os.path.join(BASE, key)):
            warnings.append('目录缺失，将自动创建: %s' % key)
    only = {x.strip() for x in (args.only or '').split(',') if x.strip()}
    skip = {x.strip() for x in (args.skip or '').split(',') if x.strip()}
    for stage in stages:
        if not _selected(stage, args, only, skip):
            continue
        for dep in stage.needs:
            if not os.path.exists(os.path.join(SCRIPTS, dep)):
                msg = '%s: 缺少依赖脚本 scripts/%s' % (stage.key, dep)
                (problems if stage.required else warnings).append(msg)
    if os.path.exists('/usr/bin/python3'):
        probe = subprocess.run([PDF_PYTHON, '-c', 'import fitz'],
                               capture_output=True, text=True)
        if probe.returncode != 0:
            problems.append('深度提炼依赖 PyMuPDF(fitz)，但 %s 无法 import' % PDF_PYTHON)
    else:
        warnings.append('未找到 /usr/bin/python3，PDF 阶段将使用 %s' % PYTHON)
    try:
        import theme_filter  # noqa: F401
        import species_registry  # noqa: F401
    except Exception as exc:
        problems.append('防污染模块导入失败: %s' % exc)
    # 2026-11-17：raw/papers/all_pdfs 已改为指向外置归档（H:\hermes_archive）
    # 的目录联接，用于给 99% 占用的 G: 腾空间。移动硬盘未插上时必须显式降级，
    # 不能让「PDF 目录不存在」被静默当成「今天没有 PDF」，也不能直接崩。
    try:
        n_pdf = len([n for n in os.listdir(PDF_DIR) if n.lower().endswith('.pdf')])
    except OSError as exc:
        n_pdf = -1
        warnings.append('PDF 归档目录不可达（%s）：%s —— 全文/深度提炼阶段将无素材，'
                        '若为外置归档请确认已插上并挂载' % (PDF_DIR, exc))
    else:
        if n_pdf == 0:
            warnings.append('PDF 归档目录为空：%s' % PDF_DIR)
        else:
            ctx.log.info('PDF 归档目录可达：%d 个 PDF（%s）' % (n_pdf, PDF_DIR))
    for item in warnings:
        ctx.log.warn('预检: ' + item)
    if problems:
        for item in problems:
            ctx.log.error('预检失败: ' + item)
        return False
    ctx.log.info('预检通过（BASE=%s, pdf_python=%s）' % (BASE, PDF_PYTHON))
    return True


def ensure_dirs():
    for path in (CONCEPTS_DIR, EVIDENCE_DIR, ENTITIES_DIR, RELATIONSHIPS_DIR,
                 SYNTHESIS_DIR, HYPOTHESES_DIR, PROGRAMS_DIR):
        os.makedirs(path, exist_ok=True)
    try:
        os.makedirs(PDF_DIR, exist_ok=True)
    except OSError:
        # PDF_DIR 可能是指向外置归档的 junction；归档未挂载时不要在这里炸掉，
        # 由 preflight 记 WARNING、由阶段自身降级。
        pass


# ────────────────────────────── 主流程 ──────────────────────────────
def parse_args(argv=None):
    ap = argparse.ArgumentParser(
        description='PlantSciKB 每日文献流水线（单一入口）',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='示例:\n'
               '  python3 scripts/daily_full_pipeline.py --dry-run\n'
               '  python3 scripts/daily_full_pipeline.py --only phase3_pubmed,phase5_deep_curate\n'
               '  python3 scripts/daily_full_pipeline.py --resume\n')
    ap.add_argument('--dry-run', action='store_true', help='只打印阶段计划，不执行')
    ap.add_argument('--list-stages', action='store_true', help='列出全部阶段后退出')
    ap.add_argument('--only', help='仅运行指定阶段（逗号分隔）')
    ap.add_argument('--skip', help='跳过指定阶段（逗号分隔）')
    ap.add_argument('--from', dest='from_stage', help='从指定阶段开始')
    ap.add_argument('--resume', action='store_true', help='跳过当日已成功的阶段')
    ap.add_argument('--keep-going', action='store_true', help='必需阶段失败后继续执行后续阶段')
    ap.add_argument('--lookback-days', type=int, default=1,
                    help='检索回溯天数（默认 1 天；补漏请显式给大值或用 --backfill）')
    ap.add_argument('--backfill', action='store_true',
                    help='回溯补漏模式：lookback 取 --backfill-days（默认 1095 天）')
    ap.add_argument('--backfill-days', type=int, default=1095,
                    help='--backfill 使用的回溯天数（默认 1095）')
    ap.add_argument('--phase3-timeout', type=int, default=3600,
                    help='PubMed 检索导入阶段超时秒数（默认 3600）')
    ap.add_argument('--max-papers', type=int, default=50, help='每通道最大导入数（默认 50）')
    ap.add_argument('--python', default=PYTHON, help='通用 Python 解释器')
    ap.add_argument('--pdf-python', default=PDF_PYTHON, help='带 PyMuPDF 的解释器')
    ap.add_argument('--no-git', action='store_true', help='不提交、不推送')
    ap.add_argument('--no-push', action='store_true', help='提交但不推送')
    ap.add_argument('--allow-scihub', action='store_true',
                    help='允许非 OA 兜底通道使用 Sci-Hub（默认关闭）')
    ap.add_argument('--force-phase3c', action='store_true', help='忽略 .phase3c_disable')
    ap.add_argument('--skip-preflight', action='store_true', help='跳过预检')
    ap.add_argument('--check', action='store_true', help='仅执行预检后退出')
    ap.add_argument('--date', help='按概念页 created 日期回放某一天（配合 --from/--only 使用）')
    ap.add_argument('--keep-temp', action='store_true', help='保留临时 DOI 文件')
    ap.add_argument('--quiet', action='store_true', help='减少控制台输出')
    ap.add_argument('--strict', action='store_true',
                    help='存在 degraded（跑完但质量不达标）时以非 0 退出，供 cron 报警')
    return ap.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    if args.backfill:
        args.lookback_days = args.backfill_days
    global PYTHON, PDF_PYTHON
    PYTHON = args.python
    PDF_PYTHON = args.pdf_python
    stages = build_stages(args)

    if args.list_stages:
        for s in stages:
            print('%-22s required=%-5s default=%-5s %s'
                  % (s.key, s.required, s.default_enabled, s.title))
        return 0

    only = set(x.strip() for x in (args.only or '').split(',') if x.strip())
    skip = set(x.strip() for x in (args.skip or '').split(',') if x.strip())
    unknown = (only | skip) - {s.key for s in stages}
    if unknown:
        print('未知阶段: %s' % ', '.join(sorted(unknown)), file=sys.stderr)
        return 2

    ensure_runtime_dirs()
    today = args.date or datetime.now().strftime('%Y-%m-%d')
    if args.date:
        try:
            datetime.strptime(args.date, '%Y-%m-%d')
        except ValueError:
            print('--date 需为 YYYY-MM-DD', file=sys.stderr)
            return 2
    run_id = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    run_dir = os.path.join(LOG_DIR, run_id)
    os.makedirs(run_dir, exist_ok=True)
    log = RunLogger(run_dir)
    state_path = os.path.join(STATE_DIR, today + '.json')
    state = {}
    if args.resume and os.path.exists(state_path):
        try:
            state = json.load(open(state_path, encoding='utf-8'))
        except Exception:
            state = {}
    ctx = Context(args=args, log=log, run_id=run_id, today=today, state=state)
    ctx.stats['base'] = BASE

    lock_fh = open(os.path.join(STATE_DIR, '.run.lock'), 'w')
    try:
        fcntl.flock(lock_fh, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        log.error('已有流水线实例在运行（锁: %s）' % os.path.join(STATE_DIR, '.run.lock'))
        return 3

    log.info('=' * 62)
    log.info('PlantSciKB 流水线 %s  run=%s' % (today, run_id))
    log.info('BASE=%s' % BASE)
    log.info('SCRIPTS=%s' % SCRIPTS)

    if args.dry_run:
        log.info('DRY-RUN：仅展示计划')
        # 2026-11-02 修正：原先 dry-run 不认 --from，会把 --from 之前的阶段也印成 RUN，
        # 让人误以为会重跑检索导入。计划输出必须和真实执行一致，否则"预览"是假的。
        _keys = [s.key for s in stages]
        if args.from_stage and args.from_stage not in _keys:
            log.error('--from 指定的阶段不存在: %s' % args.from_stage)
            log.close()
            return 2
        _start = _keys.index(args.from_stage) if args.from_stage else 0
        for _i, s in enumerate(stages):
            enabled = _selected(s, args, only, skip) and _i >= _start
            deps = ','.join(s.needs) or '-'
            exists = all(os.path.exists(os.path.join(SCRIPTS, d)) for d in s.needs)
            if _i < _start:
                label = 'BEFORE'
            else:
                label = 'RUN' if enabled else 'SKIP'
            log.info('  %-22s %-8s deps=%-28s %s'
                     % (s.key, label, deps, '' if exists else '(缺少依赖)'))
        log.close()
        try:
            lock_fh.close()          # 2026-11-02：dry-run 提前返回时原来不释放 fd
        except Exception:
            pass
        return 0

    ensure_dirs()
    if not args.skip_preflight:
        if not preflight(ctx, stages, args):
            log.error('预检未通过，终止')
            log.close()
            return 2

    if args.check:
        log.info('预检完成（--check），未执行任何阶段')
        log.close()
        return 0

    if args.date:
        ctx.today_pages = pages_created_on(args.date)
        ctx.has_new = bool(ctx.today_pages)
        ctx.pre_pages = set()
        ctx.stats['new_pages'] = len(ctx.today_pages)   # 回放模式：摘要需反映命中数
        log.info('回放 %s：命中 %d 个概念页' % (args.date, len(ctx.today_pages)))
    elif args.from_stage:
        # 2026-11-02 修正：has_new 只在 phase3 执行后赋值，而 phase4/phase5 的
        # when=lambda c: c.has_new 依赖它。于是 `--from phase4_fulltext` 必然打印
        # "今日无新增文献"并跳过全文与提炼——补跑通道形同虚设（当天 149 篇因此
        # 一直没有全文/提炼）。补跑时按概念页 created 日期重建当天集合。
        ctx.today_pages = pages_created_on(today)
        ctx.has_new = bool(ctx.today_pages)
        ctx.stats['new_pages'] = len(ctx.today_pages)
        log.info('补跑 %s：命中 %d 个当日概念页' % (today, len(ctx.today_pages)))

    state.setdefault('date', today)
    state.setdefault('stages', {})
    start_idx = 0
    if args.from_stage:
        keys = [s.key for s in stages]
        if args.from_stage not in keys:
            log.error('--from 指定的阶段不存在: %s' % args.from_stage)
            return 2
        start_idx = keys.index(args.from_stage)

    ctx.pre_pages = snapshot_pages()
    failures = []
    for stage in stages[start_idx:]:
        if not _selected(stage, args, only, skip):
            log.info('[SKIP] %s — 未选中' % stage.key)
            continue
        if stage.when is not None:
            # has_new 在 phase3 之后才能确定
            if stage.key.startswith(('phase4', 'phase5')) and not ctx.has_new:
                log.info('[SKIP] %s — 今日无新增文献' % stage.key)
                state['stages'][stage.key] = {'status': 'skipped'}
                continue
        prev = state['stages'].get(stage.key, {})
        if args.resume and prev.get('status') == 'ok':
            log.info('[SKIP] %s — --resume 已完成' % stage.key)
            continue
        if stage.key == 'phase3_pubmed':
            ctx.pre_pages = snapshot_pages()

        if stage.key == 'phase9_5_selfcheck':
            # 2026-11-16 修正：自检在 summary.json 写入之前运行，导致「运行健康（非降级）」
            # 恒定读不到本轮 summary 而 FAIL。先落一份 provisional summary。
            _dump_summary(run_dir, ctx, state, failures, provisional=True)
        log.info('▶ %s — %s' % (stage.key, stage.title))
        state['stages'][stage.key] = {'status': 'running', 'started': datetime.now().isoformat(timespec='seconds')}
        started = time.time()
        try:
            stage.func(ctx)
            status = 'ok'
        except SkipStage as exc:
            status = 'skipped'
            log.info('[SKIP] %s — %s' % (stage.key, exc))
        except StageFailure as exc:
            status = 'failed'
            msg = '%s 失败: %s' % (stage.key, exc)
            (log.error if stage.required else log.warn)(msg)
            failures.append((stage.key, stage.required, str(exc)))
        except Exception as exc:
            status = 'failed'
            log.error('%s 异常: %s' % (stage.key, exc))
            log.error(traceback.format_exc(limit=4))
            failures.append((stage.key, stage.required, str(exc)))

        elapsed = round(time.time() - started, 1)
        state['stages'][stage.key] = {'status': status, 'seconds': elapsed,
                                      'finished': datetime.now().isoformat(timespec='seconds')}
        _save_state(state_path, state)

        if stage.key == 'phase3_pubmed':
            ctx.today_pages = sorted(snapshot_pages() - ctx.pre_pages)
            ctx.has_new = bool(ctx.today_pages)
            ctx.stats['new_pages'] = len(ctx.today_pages)
            log.info('  今日新增概念页: %d' % len(ctx.today_pages))

        hard = [f for f in failures if f[1]]
        if hard and not args.keep_going:
            log.error('必需阶段失败，终止后续阶段（--keep-going 可继续）')
            break

    # 收尾
    if not ctx.today_pages:
        ctx.today_pages = sorted(snapshot_pages() - ctx.pre_pages)
        ctx.stats['new_pages'] = len(ctx.today_pages)
    ctx.stats['finished'] = datetime.now().isoformat(timespec='seconds')
    _save_state(state_path, state)
    _dump_summary(run_dir, ctx, state, failures)

    if not args.keep_temp:
        for path in ctx.temp_files:
            try:
                os.remove(path)
            except OSError:
                pass

    hard = [f for f in failures if f[1]]
    soft = [f for f in failures if not f[1]]
    log.info('=' * 62)
    log.info('完成：新增 %d 篇，提炼 %s，失败 %d（必需 %d）'
             % (ctx.stats.get('new_pages', 0), ctx.stats.get('curated_ratio', '—'),
                len(failures), len(hard)))
    degraded = ctx.stats.get('degraded') or []
    if degraded:
        log.warn('降级记录 %d 条：' % len(degraded))
        for d in degraded:
            log.warn('  - %s' % d)
    log.info('日志目录: %s' % run_dir)
    log.close()
    if hard:
        return 1
    # 2026-11-17：推送失败必须让外层（Windows 计划任务 / cron）看到非 0，
    # 否则「本地有提交、远端没内容」会和成功无法区分。注意这里不受 --strict
    # 影响：版本化失败是治理级问题，不是质量降级。
    if ctx.stats.get('git_pushed') is False:
        log.error('推送未完成（exit=%s）：当日提交未进入远端' % ctx.stats.get('git_push_rc'))
        return 1
    if args.strict and degraded:
        return 1
    return 0


def _selected(stage, args, only, skip):
    """判定阶段是否执行；--skip 与 --no-git 等开关优先于 --only。"""
    if stage.key in skip:
        return False
    if stage.key in ('git_commit', 'git_push') and args.no_git:
        return False
    if stage.key == 'git_push' and args.no_push:
        return False
    if stage.key == 'phase4b_fallback' and not args.allow_scihub:
        return False
    if only:
        return stage.key in only
    if not stage.default_enabled and not args.allow_scihub:
        return False
    return True


def _dump_summary(run_dir, ctx, state, failures, provisional=False):
    """落盘 summary.json。

    2026-11-16：phase9_5_selfcheck 需要在阶段循环内读取本轮 summary，
    因此先写 provisional 版本；收尾时用最终版覆盖。
    """
    st = dict(ctx.stats)
    st['stages'] = {k: v.get('status') for k, v in state.get('stages', {}).items()}
    st['failures'] = [{'stage': k, 'required': r, 'error': e} for k, r, e in failures]
    if provisional:
        st['provisional'] = True
    with open(os.path.join(run_dir, 'summary.json'), 'w', encoding='utf-8') as fh:
        json.dump(st, fh, ensure_ascii=False, indent=2)


def _save_state(path, state):
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8') as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2)
    os.replace(tmp, path)


if __name__ == '__main__':
    sys.exit(main())