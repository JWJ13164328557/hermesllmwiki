#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""validate_kb.py — 知识库只读体检。

它不写任何知识内容，只回答三个问题：
  1. 结构性：证据 → 概念页链接是否都能解析，ID 是否重复。
  2. 元数据：frontmatter 是否能解析、必填字段是否齐全、日期是否合法。
  3. 信息密度：自动化字段（基因/化合物/物种）的覆盖率，以及是否残留
     "看起来查过其实没查" 的占位符。

用法:
    python3 scripts/validate_kb.py                 # 体检 KB_BASE
    python3 scripts/validate_kb.py --json          # 机器可读
    python3 scripts/validate_kb.py --strict        # 有 WARN 也返回非 0

退出码: 0 通过 / 1 有 ERROR / 2 参数或路径错误（--strict 下 WARN 也算 1）
"""
import argparse
import json
import os
import re
import sys

from kb_paths import BASE

EVIDENCE_DIR = os.path.join(BASE, 'evidence')
CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
ENTITIES_DIR = os.path.join(BASE, 'entities')

REQUIRED_EVIDENCE_FIELDS = ('type', 'source', 'doi')
# 真正的「假检索」占位符：写了但没查。
NOT_SEARCHED = ('全文需通过VPN', '全文需通过 VPN', '全文需VPN')
# 合法结论标记：明确表示「检索后未发现」，不得计入缺陷。
LEGIT_ABSENT = ('_None identified_',)
# 概念页 frontmatter 必须能被严格 YAML 解析；parse_frontmatter 只取一层
# key: value，遇到非法引号/注释残留不会报错，因此历史上出现「parse 通过、
# Obsidian 与查询脚本全挂」的假绿，这里补上严格校验。
try:
    import yaml as _yaml
except Exception:  # pragma: no cover
    _yaml = None

# 空小节：标题下只剩一个空 bullet，等于没写。
EMPTY_SECTION = re.compile(r'^##+[ \t]*(.+?)[ \t]*\n[ \t]*-[ \t]*(?=\n|$)', re.M)


def parse_frontmatter(text):
    """极简 frontmatter 解析：只取一层 key: value，足够做体检，不引入依赖。"""
    if not text.startswith('---'):
        return None
    end = text.find('\n---', 3)
    if end < 0:
        return None
    fm = {}
    for line in text[3:end].split('\n'):
        m = re.match(r'^([A-Za-z_][\w-]*):\s*(.*)$', line)
        if m:
            fm[m.group(1)] = m.group(2).strip()
    return fm


def unquote(v):
    v = v.strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in '"\'':
        return v[1:-1]
    return v



# ───────────────── 覆盖度体检（只读） ────────────
CONCEPTS_TOP = os.path.join(BASE, 'concepts')
CONCEPTS_PAPERS = os.path.join(BASE, 'concepts', 'papers')
CONCEPTS_METHODS = os.path.join(BASE, 'concepts', 'methods')

# 标题以这些词收尾，基本可断定被截断（实测来自旧版 XML 取文本的属性 .text）。
DANGLING_TAIL = re.compile(
    r'(?i)(?:\b(?:of|in|on|at|for|with|by|from|to|and|or|the|a|an|via|using|'
    r'through|between|among|into|onto|as|than|that|which|is|are|was|were))\s*$')


def _page_doi(text):
    # 注意：不能用 \s*，否则空 doi 行会吞掉换行、把下一行的 key 当成 DOI。
    m = re.search(r'^doi:[ \t]*["\']?([^\s"\'\n]+)', text, re.M)
    return m.group(1).lower().rstrip('.') if m else None


def _abstract_body(text):
    # 注意: \s* 会跳行，把空的「## 摘要」后一个分区误当正文，因此只允许 [ \t]*。
    m = re.search(r'^##[ \t]*摘要[ \t]*\n(.+?)(?=\n##[ \t]|\Z)', text, re.M | re.S)
    return m.group(1).strip() if m else ''


def _title_line(text):
    m = re.search(r'^title:[ \t]*(.*)$', text, re.M)
    if m:
        v = m.group(1).strip()
        if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
            v = v[1:-1]
        return v
    m = re.search(r'^#\s+(.+)$', text, re.M)
    return m.group(1).strip() if m else ''


_HTML_SOUP = re.compile(r'@media\s*screen|data:image/svg\+xml|class="usa-|aria-label=')

# 翻译服务在配额耗尽时把错误说明写进 translatedText（responseStatus 仍是 200）。
# 旧 phase9 只判 len>5，于是这些字符串被当成中文别名写入（实测 711 条）。
FM_NOISE = re.compile(r'MYMEMORY|TRANSLATED\.NET|GOOGLE TRANSLATE|\bDEEPL\b|'
                       r'TRANSLATIONS? FOR TODAY|QUOTA (?:EXCEEDED|EXHAUSTED)|'
                       r'INVALID API KEY|TOO MANY REQUESTS', re.I)
_CJK = re.compile(r'[\u4e00-\u9fff]')
# 逐词机翻的 H1 有三个可证伪的签名（2026-11-02 用 145 页修复前快照做过召回/误报复核）：
#   S1 同一标题里出现>=3 个互异小写词（正常中文标题极少如此）
#   S2 中文标题里夹着英文虚词 of/and/with...（中文标题不会含 of/and）
#   S3 中文标题紧跟一行纯英文引用（旧变换把原英文标题挪到引用行的残留）
_LOW_WORD = re.compile(r'\b[a-z]{2,}\b')
_EN_FUNC = re.compile(r'\b(?:of|and|the|with|for|from|by|to|on|as|at|that|this|which|using|based|into|under|between|during|via)\b')

MAX_PAGE_BYTES = 400_000   # 单页正文硬上限：正常的 9-section 提炼远低于此值
_oversize = []


def h1_is_salad(h1, text):
    """判定一级标题是否为逐词机翻残留（S1/S2/S3 任一成立）。

    纯中文源页（微信/博客）不会命中：它们既无英文虚词，也无英文引用行。
    """
    if len(set(_LOW_WORD.findall(h1))) >= 3:
        return True
    if _EN_FUNC.search(h1):
        return True
    lines = text.split(chr(10))
    idx = None
    for i, line in enumerate(lines):
        if line.startswith('# '):
            idx = i
            break
    if idx is None:
        return False
    nxt = None
    for line in lines[idx + 1:idx + 6]:
        if line.strip():
            nxt = line.strip()
            break
    return bool(nxt and nxt.startswith('> ') and not _CJK.search(nxt) and len(nxt) > 25)


def coverage_health(limit_days=None):
    """回答'库里的知识有多少是真全文提炼的'，而不只是'链接通不通'。"""
    out = {'pages_top': 0, 'pages_papers': 0, 'pages_methods': 0,
           'dup_doi': 0, 'dup_doi_cross': 0, 'dup_doi_extra': 0,
           'abstract_only': 0,
           'fulltext_curated': 0, 'short_abstract': 0, 'dangling_title': 0,
           'no_terminal_punct': 0, 'curated_stall_days': None,
           'oversize_pages': 0, 'repeated_fulltext': 0, 'html_soup': 0,
           'yaml_bad': 0, 'bare_frontmatter': 0, 'no_h1': 0, 'bad_pmid': 0,
           'placeholder_title': 0, 'empty_abstract': 0,
           'dup_fm_key': 0, 'fm_noise': 0, 'h1_salad': 0}
    seen = {}
    dups = []
    _newbad = []
    newest_curated = 0.0
    for root, depth in ((CONCEPTS_TOP, 'top'), (CONCEPTS_PAPERS, 'papers'),
                        (CONCEPTS_METHODS, 'methods')):
        if not os.path.isdir(root):
            continue
        for name in os.listdir(root):
            if not name.endswith('.md'):
                continue
            if depth == 'top' and os.path.isdir(os.path.join(root, name)):
                continue
            out['pages_%s' % depth] += 1
            path = os.path.join(root, name)
            try:
                if os.path.getsize(path) > MAX_PAGE_BYTES:
                    out['oversize_pages'] += 1
                    _oversize.append(os.path.relpath(path, BASE))
            except OSError:
                pass
            try:
                with open(path, encoding='utf-8', errors='ignore') as fh:
                    text = fh.read()
            except OSError:
                continue
            if not text.startswith('---'):
                out['bare_frontmatter'] += 1
                _newbad.append(('bare_frontmatter', depth, name))
            else:
                end = text.find('\n---', 3)
                fmtext = text[3:end] if end > 0 else None
                ok = True
                if fmtext is None:
                    ok = False
                elif _yaml is not None:
                    try:
                        ok = isinstance(_yaml.safe_load(fmtext), dict)
                    except Exception:
                        ok = False
                else:
                    ok = parse_frontmatter(text) is not None
                if not ok:
                    out['yaml_bad'] += 1
                    _newbad.append(('yaml_bad', depth, name))
                else:
                    _pm = re.search(r'^pmid:[ \t]*["\']?([^\s"\'\n]*)', fmtext, re.M)
                    if _pm and _pm.group(1) and not _pm.group(1).isdigit():
                        out['bad_pmid'] += 1
                        _newbad.append(('bad_pmid', depth, name))
                    _ti = re.search(r'^title:[ \t]*(.*)$', fmtext, re.M)
                    _do = re.search(r'^doi:[ \t]*["\']?([^\s"\'\n]+)', fmtext, re.M)
                    if (_ti and _do and _ti.group(1).strip().strip('"\'')
                            == _do.group(1).strip().strip('"\'')):
                        out['placeholder_title'] += 1
                        _newbad.append(('placeholder_title', depth, name))
            # —— 重复顶层键：PyYAML 静默「后者覆盖前者」，safe_load 不报错，
            #    但字段已经丢了。2026-11-02 实测：这是格式校验的假绿点。
            if fmtext is not None:
                _keys = re.findall(r'^([A-Za-z_][\w-]*):', fmtext, re.M)
                _dupk = sorted({k for k in _keys if _keys.count(k) > 1})
                if _dupk:
                    out['dup_fm_key'] += 1
                    _newbad.append(('dup_fm_key', depth, name))
                if FM_NOISE.search(fmtext):
                    out['fm_noise'] += 1
                    _newbad.append(('fm_noise', depth, name))
            # —— 中英混杂的一级标题：逐词机翻产物，原文标题已丢失（见 _LOW_WORD 注释）
            _m_h1 = re.search(r'^#[ \t]+(.+)$', text, re.M)
            if _m_h1 and _CJK.search(_m_h1.group(1)) and h1_is_salad(_m_h1.group(1), text):
                out['h1_salad'] += 1
                _newbad.append(('h1_salad', depth, name))
            if not re.search(r'^#[ \t]+\S', text, re.M):
                out['no_h1'] += 1
                _newbad.append(('no_h1', depth, name))
            doi = _page_doi(text)
            if doi:
                if doi in seen:
                    dups.append((doi, seen[doi], (depth, name)))
                else:
                    seen[doi] = (depth, name)
            if text.count('## PMC 全文') > 1:
                out['repeated_fulltext'] += 1
            # 抓取器把 PMC 网页 CSS/HTML 原样写进正文的残留检测
            if _HTML_SOUP.search(text):
                out['html_soup'] += 1
            curated = '### 核心发现' in text
            if curated:
                out['fulltext_curated'] += 1
                newest_curated = max(newest_curated, os.path.getmtime(path))
            else:
                out['abstract_only'] += 1
            title = _title_line(text)
            if title.endswith(' ') or DANGLING_TAIL.search(title):
                out['dangling_title'] += 1
            body = _abstract_body(text)
            if body and len(body) < 700:
                out['short_abstract'] += 1
            if body and body[-1] not in '.!?。！？”"’)）]」』】':
                out['no_terminal_punct'] += 1
    # 语义修正：dup_doi 表示「同一 DOI 的多余副本页数」（可由去重直接消化）；
    # dup_doi_cross 表示其中「幸存页与被删页分处不同目录」的组数（真正的跨目录重复）。
    groups = {}
    for doi, first, other in dups:
        groups.setdefault(doi, [first]).append(other)
    out['dup_doi'] = len(dups)
    out['dup_doi_groups'] = len(groups)
    out['dup_doi_cross'] = sum(
        1 for doi, members in groups.items()
        if len({m[0] for m in members}) > 1)
    out['dup_doi_extra'] = len(dups)
    if newest_curated:
        import time as _t
        out['curated_stall_days'] = round((_t.time() - newest_curated) / 86400, 1)
    out['_dup_examples'] = [list(x) for x in dups[:5]]
    out['_newbad_examples'] = [list(map(str, x)) for x in _newbad[:10]]
    out['_newbad_counts'] = {}
    for _k, _d, _n in _newbad:
        out['_newbad_counts'][_k] = out['_newbad_counts'].get(_k, 0) + 1
    out['_oversize_examples'] = _oversize[:5]
    return out


def main():
    ap = argparse.ArgumentParser(description='知识库只读体检')
    ap.add_argument('--json', action='store_true', help='输出 JSON')
    ap.add_argument('--strict', action='store_true', help='WARN 也视为失败')
    ap.add_argument('--limit', type=int, default=10, help='每类问题最多列举几条')
    args = ap.parse_args()

    for d in (EVIDENCE_DIR, CONCEPTS_DIR):
        if not os.path.isdir(d):
            print(f'[ERROR] 目录不存在: {d}', file=sys.stderr)
            return 2

    concept_slugs = set()
    for _root, _dirs, _files in os.walk(CONCEPTS_TOP):
        for _f in _files:
            if _f.endswith('.md'):
                concept_slugs.add(_f[:-3])
    errors, warns = [], []
    stats = {'evidence': 0, 'no_genes': 0, 'no_compounds': 0,
             'no_species': 0, 'placeholder': 0, 'bad_frontmatter': 0,
             'broken_link': 0, 'bad_date': 0, 'auto_only': 0,
             'empty_section': 0}

    evidence_slugs = {f[:-3] for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md')}
    seen_ids = set()
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'):
            continue
        stats['evidence'] += 1
        path = os.path.join(EVIDENCE_DIR, fname)
        ev_id = fname[:-3]
        if ev_id in seen_ids:
            errors.append(f'重复证据 ID: {ev_id}')
        seen_ids.add(ev_id)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
        except OSError as exc:
            errors.append(f'读取失败 {fname}: {exc}')
            continue

        fm = parse_frontmatter(text)
        if fm is None:
            stats['bad_frontmatter'] += 1
            errors.append(f'frontmatter 无法解析: {fname}')
            continue

        # 两种证据 schema 并存：
        #   A) 单文献证据：必须有 source + doi
        #   B) 多来源 claim 证据：用 support: [[...]] 汇总，本就没有单一 DOI
        # 用同一把尺子量两套 schema 会产生大量假 ERROR，这里按 schema 分别校验。
        has_support = bool(re.search(r'^support:[ \t]*\n(?:[ \t]*-[ \t]*\S.*\n)+', text, re.M))
        # pending_source 表示「已知来源缺失、已显式登记待补」，不同于静默留空。
        has_pending = bool(re.search(r'^pending_source:[ \t]*\n(?:[ \t]*-[ \t]*\S.*\n)+', text, re.M))
        if has_support or has_pending:
            stats['claim_evidence'] = stats.get('claim_evidence', 0) + 1
            if not fm.get('claim'):
                warns.append(f'claim 型证据缺 claim 字段: {fname}')
        else:
            for field in REQUIRED_EVIDENCE_FIELDS:
                if not fm.get(field):
                    errors.append(f'缺字段 {field}: {fname}')

        created = unquote(fm.get('created', ''))
        if created and not re.match(r'^\d{4}-\d{2}-\d{2}$', created):
            stats['bad_date'] += 1
            errors.append(f'created 非法日期 "{created}": {fname}')

        if 'genes: []' in text or re.search(r'^genes:\s*\[\s*\]', text, re.M):
            stats['no_genes'] += 1
        if 'compounds: []' in text or re.search(r'^compounds:\s*\[\s*\]', text, re.M):
            stats['no_compounds'] += 1
        if re.search(r'^species:\s*\[\s*\]', text, re.M):
            stats['no_species'] += 1
        if any(p in text for p in NOT_SEARCHED):
            stats['placeholder'] += 1
        if EMPTY_SECTION.search(text):
            stats['empty_section'] += 1

        # 断链检查：source 与 support 两种写法都要查；目标可以是概念页或另一条证据。
        targets = []
        src = unquote(fm.get('source', ''))
        m = re.match(r'^\[\[(.+?)\]\]$', src)
        if m:
            targets.append(m.group(1))
        for t in re.findall(r'\[\[([^\]|#]+)', text):
            if t not in targets:
                targets.append(t)
        for t in targets:
            if t not in concept_slugs and t not in evidence_slugs:
                stats['broken_link'] += 1
                warns.append(f'证据断链: {fname} -> {t}')

    if stats['placeholder']:
        errors.append(f'残留「假检索」占位符（全文需VPN）的证据: {stats["placeholder"]} 条'
                      '（写了但从未真正读取全文）')
    if stats['empty_section']:
        warns.append(f'存在空小节（标题下仅一个空 bullet）的证据: {stats["empty_section"]} 条'
                     '（应补齐内容或删除该小节）')

    health = coverage_health()
    if health['repeated_fulltext']:
        errors.append(
            '检测到重复追加的 PMC 全文页: %d 个（写入器缺少幂等保护；'
            '这是 2026-11 体积事故的复发信号）' % health['repeated_fulltext'])
    if health['html_soup']:
        errors.append('正文残留 PMC 网页 CSS/HTML 垃圾: %d 页（抓取器未剥离样式）'
                      % health['html_soup'])
    if health['oversize_pages']:
        errors.append(
            '单页体积超限(>%dKB): %d 个，最大示例 %s'
            % (MAX_PAGE_BYTES // 1000, health['oversize_pages'],
               health['_oversize_examples'][0] if health['_oversize_examples'] else '-'))

    # 每类只展示自己的示例：旧实现共用 _newbad_examples[:2]，导致
    # "缺一级标题"和"pmid 非数字"两条 WARN 打印出同一批文件名（计数是对的，示例是错的）。
    _ex = health.get('_newbad_examples') or []
    for _k, _label in (('yaml_bad', 'frontmatter 无法被 YAML 解析'),
                       ('bare_frontmatter', 'frontmatter 缺少 --- 围栏'),
                       ('no_h1', '正文缺少一级标题'),
                       ('bad_pmid', 'pmid 非数字')):
        if health.get(_k):
            _own = [e for e in _ex if e[0] == _k][:2]
            _suffix = ('（示例 %s）' % _own) if _own else ''
            warns.append('%s: %d 页%s' % (_label, health[_k], _suffix))

    dens_g = 1 - stats['no_genes'] / max(stats['evidence'], 1)
    dens_c = 1 - stats['no_compounds'] / max(stats['evidence'], 1)

    report = {
        'base': BASE,
        'stats': stats,
        'coverage': {
            'genes': round(dens_g, 4),
            'compounds': round(dens_c, 4),
        },
        'health': health,
        'errors': errors,
        'warnings': warns,
    }

    if args.json:
        print(json.dumps(report, ensure_ascii=False, indent=2))
    else:
        print(f'BASE = {BASE}')
        print(f'证据文件      : {stats["evidence"]}')
        print(f'基因标注覆盖  : {dens_g:.1%}')
        print(f'化合物标注覆盖: {dens_c:.1%}')
        print(f'无物种标注    : {stats["no_species"]}')
        print(f'假检索占位符  : {stats["placeholder"]}')
        print(f'空小节        : {stats["empty_section"]}')
        print(f'frontmatter 坏: {stats["bad_frontmatter"]}')
        print(f'断链          : {stats["broken_link"]}')
        pages = (health['pages_top'] + health['pages_papers'] + health['pages_methods'])
        full = health['fulltext_curated']
        print('\n—— 覆盖度 ——')
        print(f'概念页        : {pages} (顶层 {health["pages_top"]} / papers {health["pages_papers"]}'
              f' / methods {health["pages_methods"]})')
        print('全文提炼      : %d (%.1f%%)' % (full, 100.0 * full / max(pages, 1)))
        print(f'仅摘要        : {health["abstract_only"]}')
        print(f'摘要过短(<700): {health["short_abstract"]}')
        print(f'标题截断      : {health["dangling_title"]}')
        print(f'摘要无结束标点: {health["no_terminal_punct"]}')
        print(f'超限页(>400KB): {health["oversize_pages"]}')
        print(f'重复全文块    : {health["repeated_fulltext"]}')
        print(f'HTML垃圾残留  : {health["html_soup"]}')
        print(f'frontmatter 坏(概念页): {health["yaml_bad"]}')
        print(f'无 --- 围栏   : {health["bare_frontmatter"]}')
        print(f'无一级标题    : {health["no_h1"]}')
        print(f'pmid 非法     : {health["bad_pmid"]}')
        print(f'标题==DOI占位 : {health["placeholder_title"]}')
        print(f'重复frontmatter键: {health["dup_fm_key"]}')
        print(f'翻译服务垃圾  : {health["fm_noise"]}')
        print(f'中英混杂H1    : {health["h1_salad"]}')
        print(f'重复 DOI      : {health["dup_doi"]} 个多余副本 / {health["dup_doi_groups"]} 组'
              f'（其中跨目录 {health["dup_doi_cross"]} 组）')
        if health['curated_stall_days'] is not None:
            print(f'最新深度提炼距今: {health["curated_stall_days"]} 天')
        if errors:
            print(f'\nERROR ({len(errors)}):')
            for e in errors[:args.limit]:
                print(f'  - {e}')
            if len(errors) > args.limit:
                print(f'  ... 其余 {len(errors) - args.limit} 条省略')
        if warns:
            print(f'\nWARN ({len(warns)}):')
            for w in warns[:args.limit]:
                print(f'  - {w}')
            if len(warns) > args.limit:
                print(f'  ... 其余 {len(warns) - args.limit} 条省略')
        print('\n结果:', 'FAIL' if errors else ('WARN' if warns else 'PASS'))

    if errors:
        return 1
    if warns and args.strict:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())