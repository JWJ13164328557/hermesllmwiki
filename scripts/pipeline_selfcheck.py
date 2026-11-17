#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pipeline_selfcheck.py — 每日流水线运行后的闭环自检。

为什么需要它
------------
过去"修好了"只体现在单元测试和手工回放里，日报上看不到。第二天 cron 一跑，
用户仍然无法判断闸门是否真的生效。本脚本把可复核的断言写进当天日报：

  1. 闸门离线回放：7 个历史坏例必须拒收，5 个正当植物论文必须放行；
  2. 当日新增页逐页复查：研究对象非植物或不属于八主题的，必须为 0；
  3. 文献类型分层：更正/撤稿/社论等页面保留，但证据池泄漏必须为 0；
  4. synthesis 与 hypotheses 的证据数逐主题相等，正文已重建；
  5. 标题异常（空标题 / 标题就是 DOI）必须为 0；
  6. 日报“实际新增页面”与磁盘 created 计数不得倒挂；
  7. evidence_type 空值必须为 0。

只读知识内容，唯一写入是日报的自检段与 _review/selfcheck 审计文件。
"""
from __future__ import annotations

import argparse
import io
import json
import os
import re
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import (BASE, CONCEPTS_DIR, EVIDENCE_DIR, SYNTHESIS_DIR,
                      HYPOTHESES_DIR, RELATIONSHIPS_DIR)

TODAY = datetime.now().strftime('%Y-%m-%d')
# 漏斗表由 commit a13ed33（2026-11-03 19:51:21 +0800「入口层主题归属 + 日报检索
# 漏斗对账」）引入生产。此前的运行段没有该表，数据也无法补齐。
# 2026-11-04 修正：旧实现用"整天日期"做分界（FUNNEL_REQUIRED_SINCE='2026-11-04'），
# 于是新规则上线的第一天，自检读到的是**前一天**的合并日报（2026-11-03），
# 把其中 11:17、09:10 两次漏斗上线前的运行段判成 FAIL，报出 1 项假警报。
# 现在改为按**运行时刻**分界：只有 19:51:21 之后的运行段才被要求提供漏斗表，
# 且分界时刻来自真实上线提交，不是为了让告警消失而临时挪动。
FUNNEL_REQUIRED_AT = datetime(2026, 11, 3, 19, 51, 21)
START = '<!-- PIPELINE-SELFCHECK:START -->'
END = '<!-- PIPELINE-SELFCHECK:END -->'

BAD_CASES = [
    ('Carbon quantum dots from apple juice for detection of Fe3+', 'apple juice carbon dots sensor'),
    ('Tea polyphenols inhibit Staphylococcus aureus biofilm formation', 'Staphylococcus aureus biofilm'),
    ('Microbial quality and Salmonella contamination of fresh-cut produce', 'Salmonella fresh food'),
    ('Bacteriophage therapy against Yersinia enterocolitica', 'Yersinia enterocolitica phage'),
    ('Effects of dietary supplementation on broiler chicken production performance', 'broiler chicken growth performance'),
    ('4D printing in tissue regeneration', '4D printing tissue regeneration'),
    ('Ginsenoside Rg3 alleviates colitis in mice', 'mouse colitis ginsenoside'),
]
GOOD_CASES = [
    ('Single-cell transcriptomics of rice root', 'Oryza sativa root scRNA-seq'),
    ('Drought stress response in Arabidopsis thaliana', 'Arabidopsis drought tolerance'),
    ('CRISPR knockout of SlGRAS9 in tomato fruit', 'Solanum lycopersicum fruit ripening'),
    ('Phytophthora resistance in potato', 'Solanum tuberosum late blight resistance'),
    ('Maize leaf development transcriptome', 'Zea mays leaf development'),
]


def _read(path):
    return io.open(path, encoding='utf-8', errors='replace').read()


def _fm(text):
    if not text.startswith('---'):
        return ''
    end = text.find('\n---', 3)
    return text[3:end] if end > 0 else ''


def _field(fm, key):
    m = re.search(r'^%s\s*:\s*"?([^"\n]*)"?\s*$' % re.escape(key), fm, re.M)
    return m.group(1).strip() if m else ''


def _title_body(text):
    fm, body = _fm(text), text
    t = _field(fm, 'title')
    if not t:
        m = re.search(r'^#\s+(.+)$', body, re.M)
        t = m.group(1).strip() if m else ''
    return t, fm, body


def gate_replay():
    import organism_scope as OS
    from topic_gate import is_core_topic
    bad_ok = 0
    bad_detail = []
    for title, abstract in BAD_CASES:
        org = OS.import_decision(title, abstract, 'Food Chemistry')[0]
        topic_ok, why = is_core_topic(title, abstract, 'Food Chemistry')
        rejected = (org == 'drop') or (not topic_ok)
        bad_ok += int(rejected)
        if not rejected:
            bad_detail.append(title + ' -> organism=%s topic=%s' % (org, why or 'pass'))
    good_ok = 0
    good_detail = []
    for title, abstract in GOOD_CASES:
        org = OS.import_decision(title, abstract, 'Plant Cell')[0]
        topic_ok, why = is_core_topic(title, abstract, 'Plant Cell')
        passed = (org != 'drop') and topic_ok
        good_ok += int(passed)
        if not passed:
            good_detail.append(title + ' -> organism=%s topic=%s' % (org, why))
    ok = bad_ok == len(BAD_CASES) and good_ok == len(GOOD_CASES)
    detail = '坏例拒收 %d/%d，正例放行 %d/%d' % (
        bad_ok, len(BAD_CASES), good_ok, len(GOOD_CASES))
    if bad_detail or good_detail:
        detail += '；' + '；'.join((bad_detail + good_detail)[:4])
    return ok, detail


def today_pages_scope():
    import organism_scope as OS
    from topic_gate import is_core_topic
    bad = []
    n = 0
    for fn in sorted(os.listdir(CONCEPTS_DIR)):
        if not fn.endswith('.md'):
            continue
        p = os.path.join(CONCEPTS_DIR, fn)
        text = _read(p)
        fm = _fm(text)
        if _field(fm, 'created') != TODAY:
            continue
        n += 1
        f = OS.page_fields(text)
        org = OS.import_decision(f['title'], f['abstract'], f['journal'],
                                 f['species'], f['themes'], f['tags'])[0]
        topic_ok, why = is_core_topic(f['title'], f['abstract'], f['journal'])
        if org == 'drop' or not topic_ok:
            bad.append('%s -> organism=%s topic=%s' % (fn, org, why or 'pass'))
    return (not bad), '当日新增 %d 页，越界 %d 页%s' % (
        n, len(bad), ('；' + '；'.join(bad[:4])) if bad else '')


def article_kind_layer():
    import article_kind as AK
    import organism_scope as OS
    counts = {}
    non_evidence = 0
    for fn in os.listdir(CONCEPTS_DIR):
        if not fn.endswith('.md'):
            continue
        text = _read(os.path.join(CONCEPTS_DIR, fn))
        kind = AK.kind_of(_fm(text))
        counts[kind] = counts.get(kind, 0) + 1
        if not AK.is_evidence_eligible(kind):
            non_evidence += 1
    table = OS.paper_scope_table(CONCEPTS_DIR)
    leaks = []
    for fn in sorted(os.listdir(EVIDENCE_DIR)):
        if not fn.endswith('.md'):
            continue
        text = _read(os.path.join(EVIDENCE_DIR, fn))
        doi = _field(_fm(text), 'doi').lower().rstrip('.')
        rec = table.get(doi) or {}
        if (rec.get('article_kind') or 'research') not in ('research', 'review'):
            leaks.append(fn)
    ok = not leaks
    detail = '非研究页 %d 页（保留不删）；证据池泄漏 %d 条' % (non_evidence, len(leaks))
    if leaks:
        detail += '；' + '、'.join(leaks[:5])
    return ok, detail


def synthesis_hypothesis_consistency():
    syn = {}
    for fn in os.listdir(SYNTHESIS_DIR):
        if not fn.endswith('.md'):
            continue
        fm = _fm(_read(os.path.join(SYNTHESIS_DIR, fn)))
        syn[fn[:-3]] = (_field(fm, 'total_evidence'), _field(fm, 'body_status'))
    hyp = {}
    for fn in os.listdir(HYPOTHESES_DIR):
        if not fn.endswith('.md'):
            continue
        fm = _fm(_read(os.path.join(HYPOTHESES_DIR, fn)))
        hyp[fn[:-3]] = _field(fm, 'total_evidence')
    diffs, not_rebuilt = [], []
    for k, (ev, status) in sorted(syn.items()):
        if k not in hyp:
            diffs.append('%s: 缺 hypotheses' % k)
        elif ev != hyp[k]:
            diffs.append('%s: syn=%s hyp=%s' % (k, ev, hyp[k]))
        if not status.startswith('rebuilt-'):
            not_rebuilt.append(k)
    ok = not diffs and not not_rebuilt
    detail = '主题数 %d；证据数不一致 %d；正文未重建 %d' % (
        len(syn), len(diffs), len(not_rebuilt))
    if diffs or not_rebuilt:
        detail += '；' + '；'.join((diffs + not_rebuilt)[:4])
    return ok, detail


def relationship_layer():
    """关系层语义体检。

    2026-11-03 第 12 轮：关系页只由"同一证据对象中同时出现"生成，属于共现，
    不是调控。此前页面标题写成 Regulatory Relationships，下游与读者都会把它
    当作因果证据。本检查保证：标题不含 regulat*；frontmatter 明确声明
    relationship_kind=co-occurrence 且 causal_claim=false；正文含使用限制。
    """
    bad = []
    n = 0
    if not os.path.isdir(RELATIONSHIPS_DIR):
        return True, '关系层目录不存在（跳过）'
    for fn in sorted(os.listdir(RELATIONSHIPS_DIR)):
        if not fn.endswith('.md'):
            continue
        n += 1
        text = _read(os.path.join(RELATIONSHIPS_DIR, fn))
        fm = _fm(text)
        title = (_field(fm, 'title') or '') + ' ' + (_title_body(text)[0] or '')
        problems = []
        if re.search(r'regulat', title, re.I):
            problems.append('标题含 regulat*')
        if (_field(fm, 'relationship_kind') or '').strip('"') != 'co-occurrence':
            problems.append('缺 relationship_kind=co-occurrence')
        if (_field(fm, 'causal_claim') or '').strip('"').lower() != 'false':
            problems.append('缺 causal_claim=false')
        if '不是调控' not in text:
            problems.append('正文缺语义边界说明')
        if problems:
            bad.append('%s(%s)' % (fn, '、'.join(problems)))
    ok = not bad
    detail = '关系页 %d 个；语义越权 %d 个' % (n, len(bad))
    if bad:
        detail += '；' + '；'.join(bad[:4])
    return ok, detail


def title_anomalies():
    """标题体检。</p>

    2026-11-03 第 9 轮修正：旧实现只看 frontmatter 的 title:，于是"自检 PASS、
    读者仍看到 DOI 当 H1"——13 篇页面的 H1 是 DOI/Abstract/截断串。Obsidian 展示
    的是 H1，所以必须两个都查。另加"标题串被参考文献粘连"的检测（Crossref 导入
    偶发把 reference list 写进 title，最长一条 26k 字符）。
    """
    DOI_ONLY = re.compile(r'^10\.\d{4,9}/\S+$', re.I)
    PLACEHOLDER = {'abstract', 'untitled', 'no title', 'unknown', '摘要'}
    bad, unresolved = [], 0
    for fn in os.listdir(CONCEPTS_DIR):
        if not fn.endswith('.md'):
            continue
        text = _read(os.path.join(CONCEPTS_DIR, fn))
        fm = _fm(text)
        fm_title = (_field(fm, 'title') or '').strip()
        h1 = (_title_body(text)[0] or '').strip()
        h1 = re.sub(r'^#+\s*', '', h1)
        if _field(fm, 'title_status') == 'unresolved':
            unresolved += 1
        if not h1:
            bad.append(fn + ': h1-empty')
        elif DOI_ONLY.match(h1):
            bad.append(fn + ': h1-doi')
        elif h1.lower() in PLACEHOLDER:
            bad.append(fn + ': h1-placeholder')
        # "参考文献粘连"判据：真标题可以很长（ESC 共识声明就 155 字符），
        # 但不会内嵌多个 DOI 链接或出版社的 "Available from:" 串。
        if fm_title.count('https://doi.org') >= 2 or 'Available from' in fm_title \
                or len(fm_title) > 1200:
            bad.append(fn + ': title-blob')
    return (not bad), '标题异常 %d 条；标题待补 %d 条%s' % (
        len(bad), unresolved,
        ('；' + '；'.join(bad[:4])) if bad else '')


def evidence_type_health():
    empty, total, nonarticle = 0, 0, 0
    for fn in os.listdir(EVIDENCE_DIR):
        if not fn.endswith('.md'):
            continue
        total += 1
        fm = _fm(_read(os.path.join(EVIDENCE_DIR, fn)))
        if not _field(fm, 'evidence_type'):
            empty += 1
        if RULE_VERSION not in fm:
            nonarticle += 1
    # 未按当前规则重标的页面同样是"类型字段不可信"，必须计入失败，
    # 否则规则升级后旧标签会一直冒充合格（2026-11-04 修正）。
    return (empty == 0 and nonarticle == 0), \
        'evidence %d 条；类型空值 %d 条；未按 %s 重标 %d 条' % (
            total, empty, RULE_VERSION, nonarticle)


def report_honesty():
    runs_dir = os.path.join(BASE, '_review', 'daily_runs')
    if not os.path.isdir(runs_dir):
        return True, '无 daily_runs 目录（本次未执行导入）'
    files = sorted(f for f in os.listdir(runs_dir)
                   if f.startswith(TODAY + '_') and f.endswith('.md'))
    imported = 0
    for fn in files:
        text = _read(os.path.join(runs_dir, fn))
        for m in re.finditer(r'^实际新增页面:\s*(\d+)\s*篇', text, re.M):
            imported += int(m.group(1))
        if re.search(r'^候选（通过过滤）:\s*(\d+)\s*篇', text, re.M) and '实际新增页面' not in text:
            return False, '%s 只有候选数、没有实际写入数' % fn
    created = 0
    for fn in os.listdir(CONCEPTS_DIR):
        if fn.endswith('.md') and _field(_fm(_read(os.path.join(CONCEPTS_DIR, fn))), 'created') == TODAY:
            created += 1
    ok = created >= imported
    detail = '日报累计实际新增 %d 篇；磁盘当日 created %d 篇；差额 %+d（正数=其他通道）' % (
        imported, created, created - imported)
    return ok, detail



CAUSAL_TYPES = ('genetic perturbation', 'protein interaction', 'DNA binding/regulation')
# 2026-11-04：此前这里硬编码 rule-v5-20261104。规则升级到 v6 以后，自检仍按 v5
# 判"已重标"，把"18k 页未按当前规则重标"静默报成 0 条——这是典型的自检与被检
# 对象脱钩。改为直接从规则模块读取，规则改版本号时自检自动跟随。
from batch_evidence_objects import RULE_VERSION  # noqa: E402
# 只把“同一主题的旧 ID”算作别名残留。single-cell / spatial / scrnaseq /
# epigenetics 这类是检索关键词，不是主题 ID，归到主题时由 THEME_TAG_ALIASES
# 处理即可，不应算残留（否则每轮都会因为关键词标签而假 FAIL）。
ALIAS_TAGS = frozenset({
    'single-cell-spatial', 'metabolism-np', 'epigenetics-gr',
})

_LEGACY_THEME_ID = re.compile(r'^(single-cell-spatial|metabolism-np|epigenetics-gr)$')


def _alias_hits(tags):
    """返回该页标签里的别名残留数（含 '#metabolism-np' 这类带井号的脏标签）。"""
    n = 0
    for t in tags:
        raw = (t or '').strip()
        if raw.startswith('#'):
            n += 1
            continue
        if _LEGACY_THEME_ID.match(raw.lower().replace('_', '-')):
            n += 1
    return n


def _tags(fm):
    raw = _field(fm, 'tags') or _field(fm, 'themes') or ''
    if raw.startswith('['):
        return [x.strip().strip('"\'') for x in raw.strip('[]').split(',') if x.strip()]
    return []


def _tags_both(fm):
    """论文页同时有 tags(检索关键词) 与 themes(主题归属)，两者都要看。"""
    out = []
    for key in ('tags', 'themes'):
        raw = _field(fm, key) or ''
        if raw.startswith('['):
            out.extend(x.strip().strip('"\'') for x in raw.strip('[]').split(',')
                       if x.strip())
    return out


def evidence_semantics():
    """证据语义体检：不仅看空值，还看判别力。

    只检查“字段非空”会放过 89% descriptive 的旧状态——字段填满但没有判别力。
    本检查同时报告因果级占比与规则置信度分布，阈值设在“描述性 <= 85%、
    因果级 >= 10%”，低于阈值直接 FAIL。
    """
    total = empty = descriptive = causal = lowconf = norole = nonfinding = 0
    for fn in os.listdir(EVIDENCE_DIR):
        if not fn.endswith('.md'):
            continue
        total += 1
        fm = _fm(_read(os.path.join(EVIDENCE_DIR, fn)))
        et = (_field(fm, 'evidence_type') or '').strip()
        if not et:
            empty += 1
        if et == 'descriptive/observational':
            descriptive += 1
        if et in CAUSAL_TYPES:
            causal += 1
        if (_field(fm, 'evidence_type_confidence') or '').strip() == 'low':
            lowconf += 1
        role = (_field(fm, 'claim_role') or '').strip()
        if not role:
            norole += 1
        elif role != 'finding':
            nonfinding += 1
    d_pct = 100.0 * descriptive / max(1, total)
    c_pct = 100.0 * causal / max(1, total)
    ok = empty == 0 and d_pct <= 85.0 and c_pct >= 10.0 and norole == 0
    return ok, ('evidence %d；空类型 %d；描述性 %.1f%%；因果级 %.1f%%；低置信 %d（%.0f%%）；'
                '论断角色缺字段 %d；非发现句 %d 条（已排除出证据池）'
                % (total, empty, d_pct, c_pct, lowconf, 100.0 * lowconf / max(1, total),
                   norole, nonfinding))


def theme_coverage():
    """八主题覆盖率与标签别名体检。

    2026-11-03 第 13 轮：旧口径只统计“有标签”的页面，把 papers/metabolism 这类
    泛化桶也算成覆盖，导致 22% 被说成“覆盖面广”。本检查要求：
      * 证据主题归属 >= 65%（theme_status=mapped 或规范主题标签）；
      * 论文主题归属 >= 60%；
      * 证据/论文标签中不得残留别名（metabolism-np、single-cell-spatial 等）。
    """
    import themes as th
    ev_total = ev_mapped = paper_total = paper_mapped = alias = 0
    # 归属来源分层（2026-11-03 第 14 轮）：同一个"77% 覆盖"里混着两种性质
    # 完全不同的归属 —— tag 精确命中（逐条）与论文级继承（逐篇）。
    # 不给这两个数，覆盖率高就只是一句好听的话。
    by_tag = by_inherit = 0
    for fn in os.listdir(EVIDENCE_DIR):
        if not fn.endswith('.md'):
            continue
        ev_total += 1
        fm = _fm(_read(os.path.join(EVIDENCE_DIR, fn)))
        tags = _tags_both(fm)
        alias += _alias_hits(tags)
        mapped = ((_field(fm, 'theme_status') or '') == 'mapped'
                  or th.themes_from_tags(tags))
        if mapped:
            ev_mapped += 1
            if (_field(fm, 'theme_basis') or '').startswith('inherit-'):
                by_inherit += 1
            else:
                by_tag += 1
    # 注意：CONCEPTS_DIR 本身已经是 <BASE>/concepts/papers（见 kb_paths.py）。
    # 旧实现又拼了一层 'papers'，目录不存在 → 论文归属恒为 0/0（假 FAIL）。
    pdir = CONCEPTS_DIR
    elig_total = elig_mapped = 0
    if os.path.isdir(pdir):
        for fn in os.listdir(pdir):
            if not fn.endswith('.md'):
                continue
            paper_total += 1
            fm = _fm(_read(os.path.join(pdir, fn)))
            tags = _tags_both(fm)
            alias += _alias_hits(tags)
            mapped = ((_field(fm, 'theme_status') or '') == 'mapped'
                      or th.themes_from_tags(tags))
            if mapped:
                paper_mapped += 1
            # 第二个分母（2026-11-03 第 15 轮）：220 个无可用 DOI 的页面
            # 已被标 evidence_eligible: false，它们永远进不了证据池，
            # 却仍占着"主题覆盖率"的分母。只报一个数，就会把
            # "页面不可回溯"当成"主题没覆盖"。两个数都摆出来。
            if (_field(fm, 'evidence_eligible') or '') != 'false':
                elig_total += 1
                if mapped:
                    elig_mapped += 1
    ev_pct = 100.0 * ev_mapped / max(1, ev_total)
    p_pct = 100.0 * paper_mapped / max(1, paper_total)
    elig_pct = 100.0 * elig_mapped / max(1, elig_total)
    # 2026-11-03 第 17 轮：把"判断不了"从"不相关"里拆出来单独计数。
    # 旧口径只报 mapped/(全部)，于是 2243 个只有标题、无摘要的页面
    # 被默默算进分母，读者既看不到它们、也无法据此要求补元数据。
    unc = oos = 0
    if os.path.isdir(pdir):
        for fn in os.listdir(pdir):
            if not fn.endswith('.md'):
                continue
            st = (_field(_fm(_read(os.path.join(pdir, fn))), 'theme_status') or '')
            if st == 'unclassified':
                unc += 1
            elif st == 'out-of-scope':
                oos += 1
    judgeable = paper_mapped + oos
    unc_pct = 100.0 * unc / max(1, paper_total)
    j_pct = 100.0 * paper_mapped / max(1, judgeable)
    # 断言口径：只在"可判断"的页面里要求归属比例，同时给 unclassified
    # 设上限——否则靠"什么都不判"就能把比例做上去。
    ok = (ev_pct >= 65.0 and j_pct >= 65.0 and unc_pct <= 35.0
          and alias == 0)
    return ok, ('证据主题归属 %d/%d（%.1f%%）＝tag 精确 %d + 论文继承 %d；'
                '论文三态：mapped %d／out-of-scope %d／unclassified %d'
                '（可判断页归属 %.1f%%，未判定占比 %.1f%%）；'
                '可作证据分母 %d/%d（%.1f%%）；别名残留 %d'
                % (ev_mapped, ev_total, ev_pct, by_tag, by_inherit,
                   paper_mapped, oos, unc, j_pct, unc_pct,
                   elig_mapped, elig_total, elig_pct, alias))


_SUBS_ERR = ''
try:
    from repair_species_artifact import SUBS as _SUBS
except Exception as _exc:  # 缺失时不得静默跳过：记录错误并让本项 FAIL
    _SUBS = {}
    _SUBS_ERR = '%s: %s' % (type(_exc).__name__, _exc)


def species_field_health():
    """物种字段失真体检（2026-11-03 第 17 轮）。

    "文献描述与实际不符"里最硬的一类是物种错标：whale shark 行为谱被写成
    Ficus carica、乳腺钼靶论文被写成无花果。根因是提炼层裸子串匹配（'fig' 命中
    "Fig. 1" 与 "configuration"，'orange' 命中颜色词），已在提炼脚本侧修复；
    本项负责让复发当天可见。

    判据（逐条可复核，不做统计推断）
    --------------------------------
    取页面 **物种** 行；含伪影物种（Ficus carica / Citrus spp. / Citrus sinensis）时，
    在「标题 + 摘要」（排除 深度提炼 块，防自证）中按整词/中文同义词查找支持证据。
    找不到 → 计入失真。真·无花果论文（摘要写 fig/无花果）不会被计入。

    同时暴露 物种: plant 占位率：这是"摘要缺失判不出物种"的可见指标，不是失败项，
    但数字必须露出来，否则又是"覆盖广但不可判定"。
    """
    ART = {
        'Ficus carica': re.compile(
            r'\bficus\b|\bcommon\s+fig\b|\bedible\s+fig\b|\bfig\s+tree\b|'
            r'\bfigs?\b(?!\s*[.\-]?\s*\d)|无花果', re.I),
        'Citrus spp.': re.compile(r'\bcitrus\b|柑橘|柑|橘|橙|柚|\borange\b|\blemon\b', re.I),
        'Citrus sinensis': re.compile(
            r'\bcitrus\b|\bsweet\s+orange\b|\bnavel\s+orange\b|柑橘|脐橙|甜橙', re.I),
    }
    SP_RE = re.compile(r'^\*\*物种\*\*:\s*(.+)$', re.M)

    bad, placeholder, total, unverified = [], 0, 0, 0
    unverified_pages, unflagged = set(), []
    for fn in os.listdir(CONCEPTS_DIR):
        if not fn.endswith('.md'):
            continue
        text = _read(os.path.join(CONCEPTS_DIR, fn))
        m = SP_RE.search(text)
        if not m:
            continue
        total += 1
        raw = m.group(1).strip()
        if raw.lower() in ('plant', 'plant (unspecified)', '未识别', 'unknown', '—', ''):
            placeholder += 1
            continue
        names = [x.strip() for x in re.split(r'[;；,/、]', raw) if x.strip()]
        risky = any(n in ART or n in _SUBS for n in names)
        if not risky:
            continue
        support = paper_text_without_curation(text)
        abstract = _abstract_only(text)
        page_unverified = False
        for n in names:
            if n in ART and not ART[n].search(support):
                if abstract:
                    bad.append('%s: %s' % (fn, n))
                else:
                    unverified += 1
                    page_unverified = True
            elif abstract and n in _SUBS:
                sub, whole = _SUBS[n]
                # 同一根因第二类：俗名只以子串出现（price→rice、appear→pear、cornerstone→corn）
                if re.search(sub, support, re.I) and not re.search(whole, support, re.I):
                    bad.append('%s: %s(子串)' % (fn, n))
        if page_unverified:
            unverified_pages.add(fn)
            # 未标记不算“无法判定”，而是“清理未落地”：必须失败，否则脏数据静默留存
            if not re.search(r'^species_status:\s*unverified', text, re.M):
                unflagged.append(fn)
    ok = len(bad) <= 40 and not unflagged and not _SUBS_ERR
    detail = ('含物种行 %d 页；伪影物种无正文支持 %d 条（阈值 40）；'
              '无摘要无法判定 %d 页 / %d 条，已标 species_status: unverified %d 页、漏标 %d 页；'
              '物种为占位 plant/未识别 %d 页（%.1f%%，摘要缺失导致，非失败项）%s%s'
              % (total, len(bad), len(unverified_pages), unverified,
                 len(unverified_pages) - len(unflagged), len(unflagged),
                 placeholder, 100.0 * placeholder / max(total, 1),
                 ('；例：' + '；'.join(bad[:3])) if bad else '',
                 ('；子串规则不可用！' + _SUBS_ERR) if _SUBS_ERR else ''))
    return ok, detail


def _abstract_only(text):
    body = text.split('## 深度提炼')[0]
    m = re.search(r'^##\s*(?:摘要|Abstract)\s*\n(.+?)(?=\n##|\Z)', body, re.S | re.M)
    return (m.group(1).strip() if m else '')


def paper_text_without_curation(text):
    """标题 + 摘要，剔除 深度提炼 块（防止用被检对象自证）。"""
    body = text.split('## 深度提炼')[0]
    title = ''
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', body, re.M)
    if m:
        title = m.group(1)
    m = re.search(r'^##\s*(?:摘要|Abstract)\s*\n(.+?)(?=\n##|\Z)', body, re.S | re.M)
    return title + ' ' + (m.group(1) if m else '')


def synthesis_quality():
    """综合页是否仍是“数据摘要”而非可读综述。

    只查计数器会得到“0/8 问题”的假绿。本检查要求每页：
      * body_status 为 rebuilt-*（正文已重建，不是历史正文）；
      * 含第 0 节“综述提要”；
      * 行内证据链接 >= 1 处/500 中文字符。
    """
    bad = []
    n = 0
    for fn in sorted(os.listdir(SYNTHESIS_DIR)):
        if not fn.endswith('.md'):
            continue
        n += 1
        t = _read(os.path.join(SYNTHESIS_DIR, fn))
        fm = _fm(t)
        status = (_field(fm, 'body_status') or '')
        zh = len(re.findall(r'[\u4e00-\u9fff]', t))
        links = len(re.findall(r'\[\[[^\]]+\]\]', t))
        density = 500.0 * links / max(1, zh)
        problems = []
        if not status.startswith('rebuilt-'):
            problems.append('未重建')
        if '## 0. 综述提要' not in t:
            problems.append('缺提要')
        if density < 1.0:
            problems.append('引用密度 %.1f<1' % density)
        if problems:
            bad.append('%s(%s)' % (fn[:-3], '、'.join(problems)))
    return (not bad), '综合页 %d；不合格 %d%s' % (
        n, len(bad), ('；' + '；'.join(bad[:4])) if bad else '')


def hypothesis_balance():
    """假说分布与模板化体检。"""
    import themes as th
    counts, bad = {}, []
    for theme_id in th.THEMES:
        path = os.path.join(HYPOTHESES_DIR, theme_id + '.md')
        if not os.path.exists(path):
            bad.append('%s(缺页)' % theme_id)
            continue
        fm = _fm(_read(path))
        try:
            n = int(_field(fm, 'total_hypotheses') or 0)
        except ValueError:
            n = 0
        counts[theme_id] = n
        generic = (_field(fm, 'specificity_generic') or '0').strip('"')
        if n < 3:
            bad.append('%s(仅%d条)' % (theme_id, n))
        if generic not in ('0', ''):
            bad.append('%s(通用方案%s条)' % (theme_id, generic))
    spread = '、'.join('%s=%d' % (th.THEME_META[k]['title_zh'], v)
                      for k, v in counts.items())
    return (not bad), '假说分布：%s%s' % (spread, ('；问题：' + '；'.join(bad[:4])) if bad else '')


BANNER_START = '<!-- SELFCHECK-FAIL-BANNER:START -->'
BANNER_END = '<!-- SELFCHECK-FAIL-BANNER:END -->'


def build_banner(rows, failed):
    """FAIL 时在日报**顶部**插入可见横幅；全 PASS 时返回空串（横幅被移除）。

    为什么需要：自检表在日报末尾，08:00 的 cron 报告被截断/被只看开头时，
    FAIL 会被埋掉。横幅把"今天有 N 项没通过"放到第一屏，且不改动正文统计。
    """
    if not failed:
        return ''
    bad = ['%s（%s）' % (n, d.replace('|', '/')) for n, ok, d in rows if not ok]
    return '\n'.join([
        BANNER_START,
        '> [!WARNING] 本次运行有 **%d 项自检未通过**，结果需在下一轮前处理：' % failed,
    ] + ['> - %s' % b for b in bad] + [
        '>',
        '> 详见文末「运行后闭环自检」表与 `_review/selfcheck/%s.json`。' % TODAY,
        BANNER_END,
    ])


def build_report(rows):
    lines = [START, '', '## 运行后闭环自检（自动生成，可复核）', '',
             '| 检查项 | 结果 | 说明 |', '|---|---|---|']
    for name, ok, detail in rows:
        lines.append('| %s | %s | %s |' % (name, 'PASS' if ok else 'FAIL', detail.replace('|', '/')))
    lines += ['', '> 本段由 `pipeline_selfcheck.py` 在流水线末尾生成；'
              'FAIL 不等于当天数据一定不可用，但必须在下一轮运行前处理。', '', END]
    return '\n'.join(lines)


def _strip_banner(text):
    """移除横幅并归一化空行，保证"先删后插"幂等（重复运行不叠加空行）。"""
    text = re.sub(re.escape(BANNER_START) + r'.*?' + re.escape(BANNER_END) + r'\n*',
                  '', text, flags=re.S)
    return re.sub(r'\n{3,}', '\n\n', text)


def _insert_banner(text, banner):
    """插在一级标题（及其后的日期行）之后，保证出现在第一屏。"""
    lines = text.split('\n')
    pos = 0
    for i, ln in enumerate(lines[:8]):
        if ln.startswith('# '):
            pos = i + 1
            break
    while pos < len(lines) and (not lines[pos].strip()
                                or re.match(r'^\d{4}-\d{2}-\d{2}$', lines[pos].strip())):
        pos += 1
    head = '\n'.join(lines[:pos]).rstrip('\n')
    tail = '\n'.join(lines[pos:])
    return head + '\n\n' + banner + '\n\n' + tail.lstrip('\n')


def frontmatter_parseable():
    """全库 frontmatter 必须能被 YAML 解析。

    2026-11-03 事故：1203 个页面（1189 论文页 + 14 证据页）的 frontmatter
    因"孤儿列表项"（`themes: [x]` 后残留顶格 `- item`）与控制字符而非法，
    Obsidian/Dataview 静默丢弃整段字段——而当天自检 12/12 全 PASS，
    因为没有任何一项检查 YAML 可解析性。此检查补上这一层。
    """
    import yaml
    import frontmatter as F
    subs = ('concepts/papers', 'concepts/methods', 'evidence', 'entities',
            'relationships', 'synthesis', 'hypotheses', 'research-programs')
    scanned = 0
    bad = []
    for sub in subs:
        d = os.path.join(BASE, sub)
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.md'):
                continue
            scanned += 1
            raw = _read(os.path.join(d, fn))
            # 2026-11-04：只验 YAML 可解析不够。"---scope_status: x" 这种粘连围栏
            # 在 YAML 眼里是合法映射（键就是 scope_status），整页字段在 Obsidian
            # 里根本不是属性，自检却判 PASS。围栏必须独占一行。
            if raw.startswith('---') and not raw.startswith('---\n'):
                bad.append(sub + '/' + fn + '(围栏未独占一行)')
                continue
            fm, _body = F.split(raw)
            if not fm:
                bad.append(sub + '/' + fn + '(无 frontmatter)')
                continue
            try:
                parsed = yaml.safe_load(fm)
            except Exception:
                bad.append(sub + '/' + fn)
                continue
            if not isinstance(parsed, dict):
                bad.append(sub + '/' + fn + '(非映射)')
    ok = not bad
    detail = '扫描 %d 页；不可解析 %d 页' % (scanned, len(bad))
    if bad:
        detail += '；' + '、'.join(bad[:5])
    return ok, detail


_DOI_RE = re.compile(r"^10\.\d{4,9}/[^\s]+$")


def evidence_traceability():
    """证据可回溯性：每条证据都必须能靠 DOI 回到原始文献。

    2026-11-03 第 15 轮。此前的自检只数"字段是否为空"，从没断言过
    "这条证据能不能被第三方核到"。本次实测：12291 条证据中 1 条无 doi
    （人工共识页），0 条指向无 DOI 的论文页。把这条不变量写死：

      * 论文派生证据（未标 evidence_source: consensus）必须带合法 DOI；
      * 它的来源论文页也必须带合法 DOI —— 否则引用的是不可验证页面；
      * 共识页（evidence_source: consensus）必须至少 2 条 support 链接。
    """
    paper_doi = {}
    pdir = CONCEPTS_DIR
    if os.path.isdir(pdir):
        for fn in os.listdir(pdir):
            if fn.endswith('.md'):
                fm = _fm(_read(os.path.join(pdir, fn)))
                paper_doi[fn[:-3]] = (_field(fm, 'doi') or '').strip().strip('"\'')
    no_doi, bad_source, weak_consensus = [], [], []
    total = consensus = 0
    for fn in os.listdir(EVIDENCE_DIR):
        if not fn.endswith('.md'):
            continue
        total += 1
        text = _read(os.path.join(EVIDENCE_DIR, fn))
        fm = _fm(text)
        doi = (_field(fm, 'doi') or '').strip().strip('"\'')
        if (_field(fm, 'evidence_source') or '') == 'consensus':
            consensus += 1
            n_sup = len(re.findall(r'\[\[', _field(fm, 'support') or text[:2000]))
            if n_sup < 2:
                weak_consensus.append('%s(%d)' % (fn, n_sup))
            continue
        if not doi:
            no_doi.append(fn)
            continue
        if not _DOI_RE.match(doi):
            no_doi.append(fn + '(非法)')
            continue
        m = re.search(r'source:\s*"?\[\[([^\]|]+)', text)
        if m:
            src = m.group(1).strip()
            sdoi = paper_doi.get(src, None)
            if sdoi is not None and not _DOI_RE.match(sdoi or ''):
                bad_source.append(fn + '->' + src)
    ok = not no_doi and not bad_source and not weak_consensus
    detail = ('证据 %d 条；无 DOI %d；来源页无 DOI %d；共识页 %d（support 不足 %d）'
              % (total, len(no_doi), len(bad_source), consensus, len(weak_consensus)))
    extra = no_doi[:3] + bad_source[:3] + weak_consensus[:3]
    if extra:
        detail += '；' + '、'.join(extra)
    return ok, detail



def funnel_reconcile():
    """日报漏斗对账：每个检索到的 PMID 必须落入且仅落入一个桶。

    2026-11-03 第 16 轮。线上实测 11:17 那次运行写着"检索 86 篇 / 候选 1 篇"，
    而当日没有人在日志里说得清另外 85 篇去了哪 —— 事后查明是 09:10 刚导入过、
    被 dup_existing 挡下，属正常去重。但"正常"是事后查出来的，日报本身不自证。
    所以把可审计性写死：

      * 当日每个生产运行段必须有「检索漏斗」表；
      * 表中合计必须等于"检索命中"，否则判 FAIL 并报差额；
      * 生产日报里不得出现"未执行（未启用 --import）"——演练要落
        _review/daily_runs_dry/，不该混进生产底账。
    """
    report = os.path.join(BASE, 'daily_report.md')
    if not os.path.exists(report):
        return False, '找不到 daily_report.md'
    text = _read(report)
    # 报告日期以**报告自身**为准，不能用 TODAY：新规则上线的第一天，自检读到的
    # 往往还是前一天合并生成的日报，用 TODAY 比较会把历史底账当当日生产来判。
    m_day = re.search(r'^#\s*每日文献更新报告\s*\n+\s*(\d{4}-\d{2}-\d{2})', text, re.M)
    report_day = m_day.group(1) if m_day else TODAY
    # 只取当日所有「## 运行 HH:MM:SS」段
    parts = re.split(r'^## 运行 ', text, flags=re.M)[1:]
    if not parts:
        return True, '当日无生产运行记录（0 段），无需对账'
    bad, dry_leak, legacy, checked = [], [], 0, 0
    for seg in parts:
        if '未执行（未启用 --import）' in seg:
            dry_leak.append(seg.split('\n', 1)[0])
            continue
        m_hms = re.match(r'(\d{2}):(\d{2}):(\d{2})', seg)
        seg_at = None
        if m_hms:
            try:
                seg_at = datetime.strptime(report_day, '%Y-%m-%d').replace(
                    hour=int(m_hms.group(1)), minute=int(m_hms.group(2)),
                    second=int(m_hms.group(3)))
            except ValueError:
                seg_at = None
        if seg_at is not None and seg_at < FUNNEL_REQUIRED_AT:
            # 漏斗上线前的运行段：数据无法补齐，如实计为 legacy 并在明细里报出，
            # 不做静默丢弃，也不会让"缺表"变成永久盲区——分界之后仍一律 FAIL。
            legacy += 1
            continue
        m_ret = re.search(r'检索:\s*(\d+)\s*篇', seg)
        if not m_ret:
            bad.append('段缺检索数')
            continue
        ret = int(m_ret.group(1))
        if '检索漏斗' not in seg:
            bad.append('检索 %d 篇：缺漏斗表' % ret)
            continue
        m_tot = re.search(r'\|\s*合计\s*\|\s*(\d+)\s*\|', seg)
        if not m_tot:
            bad.append('检索 %d 篇：漏斗表缺合计行' % ret)
            continue
        tot = int(m_tot.group(1))
        checked += 1
        if tot != ret:
            bad.append('检索 %d ≠ 合计 %d（差额 %d 无归属）' % (ret, tot, ret - tot))
        elif 'INCONSISTENT' in seg or '漏斗对账不平' in seg:
            bad.append('检索 %d：正文标注对账不平' % ret)
    ok = not bad and not dry_leak
    detail = '生产运行 %d 段，对账通过 %d 段' % (len(parts), checked)
    if legacy:
        detail += '；%d 段早于漏斗上线（%s），按历史底账豁免' % (
            legacy, FUNNEL_REQUIRED_AT.strftime('%Y-%m-%d %H:%M'))
    if bad:
        detail += '；问题 ' + '；'.join(bad[:4])
    if dry_leak:
        detail += '；演练污染 %d 段（%s）' % (len(dry_leak), '、'.join(dry_leak[:3]))
    return ok, detail



def orphan_pdf_health():
    """孤儿 PDF（磁盘有全文、库里无页面）不得再增长。

    2026-11-03 实测：raw/ 下 2469 份 PDF 里 477 份的正文章 DOI 在
    concepts/papers 找不到任何页面，抽样全是非植物（Arthritis &
    Rheumatology、Frontiers in Allergy、Psychopharmacology）。这些是历史
    导入被拒/隔离后留在磁盘上的废料，占 598MB 以上，且会让"全文覆盖率"
    这类指标看起来比实际好。

    已把 156 份 purity 确认非植物的移到 _review/pdf_quarantine/（可回滚），
    剩 169 份（plant/unresolved/suspect）**故意不动** —— 标题级 purity 对
    "Glucocorticoids in Rheumatoid Arthritis" 这类无对象词的标题会误判 plant，
    在拿不到摘要的前提下宁可留着。所以这里只设阈值，不做自动清理。

    阈值 200 的来历：清理后实测 169。留出约 30 份的正常波动（当日新下载但
    尚未写页面的 PDF），超过就说明又有"下载了但没入库"的路径在漏。
    """
    known = set()
    cdir = os.path.join(BASE, 'concepts', 'papers')
    if not os.path.isdir(cdir):
        return False, '找不到 concepts/papers'
    for fn in os.listdir(cdir):
        if not fn.endswith('.md'):
            continue
        head = _read(os.path.join(cdir, fn))[:2000]
        m = re.search(r'^doi:\s*"?([^"\n]+)"?\s*$', head, re.M)
        if m:
            known.add(m.group(1).strip().lower().replace('_', '/').rstrip('.-'))
    raw_dir = os.path.join(BASE, 'raw')
    rx = re.compile(r'(10[._]\d{4,}[._/][A-Za-z0-9_.\-]+)')
    total = 0
    orphans = []
    for root, _d, files in os.walk(raw_dir):
        for f in files:
            if not f.lower().endswith('.pdf'):
                continue
            total += 1
            m = rx.search(f)
            if not m:
                continue
            d = m.group(1).lower().replace('_', '/')
            d = re.sub(r'\.pdf$', '', d).rstrip('.-')
            if d in known:
                continue
            if any(k.startswith(d) or d.startswith(k) for k in known
                   if abs(len(k) - len(d)) < 40):
                continue
            orphans.append(f)
    ok = len(orphans) <= 200
    detail = ('raw PDF %d 份；孤儿（有全文无页面）%d 份（阈值 200）' % (total, len(orphans)))
    if orphans:
        detail += '；例：' + '、'.join(orphans[:3])
    return ok, detail


def run_health_not_degraded():
    """运行健康度：把 summary.json 的 degraded 升级为一等 FAIL。

    2026-11-07 的教训：11-06 与 11-07 连续两天"全文获取 0/31、0/21"，
    深度提炼 0 篇，但自检 17/17 全 PASS——因为 17 项全是**结构一致性**检查
    （字段有没有、数字对不对），没有一项检查**能力是否还在**。
    于是出现"自检说全通过、同一天 degraded 说深度为 0"的假绿。

    本检查把流水线自己写的 degraded/failures 直接提升为 FAIL，
    并在 detail 里回显原文，让人在第一屏就能看见"今天做不到什么"。
    """
    d = os.path.join(BASE, 'logs', 'pipeline')
    if not os.path.isdir(d):
        return True, '无 logs/pipeline（非定时运行环境，跳过）'
    runs = sorted([n for n in os.listdir(d) if n.startswith(TODAY)], reverse=True)
    if not runs:
        return False, '今日（%s）无流水线运行记录' % TODAY
    # 2026-11-16 修正：若最新目录只有 provisional summary（如 --only 试跑），
    # 则回退到最近一次已完成的运行，避免用空统计误导。
    chosen = None
    chosen_s = None
    for name in runs:
        fp = os.path.join(d, name, 'summary.json')
        if not os.path.exists(fp):
            continue
        try:
            cand = json.loads(_read(fp))
        except Exception:
            continue
        if chosen is None:
            chosen, chosen_s = name, cand
        if not cand.get('provisional'):
            chosen, chosen_s = name, cand
            break
    if chosen is None:
        return False, '%s 缺 summary.json' % runs[0]
    s = chosen_s
    degraded = s.get('degraded') or []
    failures = s.get('failures') or []
    if failures:
        return False, '运行失败 %d 项：%s' % (
            len(failures), '；'.join(str(x)[:60] for x in failures[:3]))
    if degraded:
        return False, '降级 %d 项：%s' % (
            len(degraded), '；'.join(str(x)[:80] for x in degraded[:3]))
    return True, '新增 %s 篇；curated %s；无降级项' % (
        s.get('new_pages', '?'), s.get('curated_ratio', '?'))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--strict', action='store_true', help='有 FAIL 时返回非零退出码')
    ap.add_argument('--no-append', action='store_true', help='只打印，不写日报')
    a = ap.parse_args()

    checks = [
        # 放在第一位：能力是否还在，比结构是否自洽更重要。
        ('运行健康（非降级）', run_health_not_degraded),
        ('闸门离线回放', gate_replay),
        ('当日新增页领域复查', today_pages_scope),
        ('文献类型分层', article_kind_layer),
        ('综合页/假说页证据一致', synthesis_hypothesis_consistency),
        ('标题异常', title_anomalies),
        ('关系层语义', relationship_layer),
        ('证据类型完整性', evidence_type_health),
        ('证据语义判别力', evidence_semantics),
        ('主题覆盖与标签别名', theme_coverage),
        ('综合页综述质量', synthesis_quality),
        ('假说分布与模板化', hypothesis_balance),
        ('日报计数诚实性', report_honesty),
        ('frontmatter 可解析', frontmatter_parseable),
        ('证据可回溯（DOI）', evidence_traceability),
        ('日报漏斗对账', funnel_reconcile),
        ('物种字段失真', species_field_health),
        ('孤儿 PDF', orphan_pdf_health),
    ]
    rows, failed = [], 0
    for name, fn in checks:
        try:
            ok, detail = fn()
        except Exception as exc:
            ok, detail = False, '检查异常: %s: %s' % (type(exc).__name__, exc)
        rows.append((name, ok, detail))
        failed += int(not ok)
        print(('PASS' if ok else 'FAIL'), name, '|', detail)

    block = build_report(rows)
    out_dir = os.path.join(BASE, '_review', 'selfcheck')
    os.makedirs(out_dir, exist_ok=True)
    io.open(os.path.join(out_dir, TODAY + '.md'), 'w', encoding='utf-8', newline='\n').write(block + '\n')
    io.open(os.path.join(out_dir, TODAY + '.json'), 'w', encoding='utf-8', newline='\n').write(
        json.dumps({'date': TODAY, 'failed': failed,
                    'checks': [{'name': n, 'ok': ok, 'detail': d} for n, ok, d in rows]},
                   ensure_ascii=False, indent=1))
    if not a.no_append:
        report = os.path.join(BASE, 'daily_report.md')
        if os.path.exists(report):
            text = _read(report)
            if START in text and END in text:
                text = re.sub(re.escape(START) + r'.*?' + re.escape(END), block, text, flags=re.S)
            else:
                text = text.rstrip() + '\n\n' + block + '\n'
            text = _strip_banner(text)
            banner = build_banner(rows, failed)
            if banner:
                text = _insert_banner(text, banner)
            io.open(report, 'w', encoding='utf-8', newline='\n').write(text)
    print('SELFCHECK failed=%d -> %s' % (failed, os.path.join(out_dir, TODAY + '.json')))
    return 1 if (a.strict and failed) else 0


if __name__ == '__main__':
    sys.exit(main())
