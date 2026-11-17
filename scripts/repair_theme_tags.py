# -*- coding: utf-8 -*-
"""主题标签回填：修 2026-11-03 体检发现的三个结构性问题。

问题
----
1. 入库时 `daily_full_pipeline.py` 硬写 `tags: [papers]`，之后由
   `batch_evidence_objects.py` 原样继承 → 全库 96.8% 的论文页无主题标签；
2. 证据页标签退化成 `metabolism`（宽桶）或 `papers`，`assign_themes` 判不出
   主题，77.7% 的证据"不属于任何八主题"；
3. 历史标签存在别名并存：`metabolism-np` / `epigenetics-gr` /
   `single-cell-spatial` 与规范名混用，同一主题在不同脚本里数出不同数字。

做法
----
* 以"论文标题 + 摘要（+ 证据 Claim）"为上下文，调用 themes.assign_themes；
* 论文页写规范 `themes: [...]`；
* 证据页追加规范主题标签（保留原标签，不删除，便于追溯）；
* 无法归属者写 `theme_status: out-of-scope`，**不再默认塞进 other**：
  八主题覆盖率的真实分母由此可算，报告不得再宣称"覆盖全库"。

用法
----
    python3 scripts/repair_theme_tags.py --dry-run
    python3 scripts/repair_theme_tags.py --apply
"""
import argparse
import collections
import io
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import themes as th
import purity_gate as pg
import frontmatter as _fm
from kb_paths import BASE

PAPERS_DIR = os.path.join(BASE, 'concepts', 'papers')
TOP_DIR = os.path.join(BASE, 'concepts')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')


def _fm_split(text):
    if not text.startswith('---'):
        return '', text
    end = text.find('\n---', 3)
    if end < 0:
        return '', text
    return text[3:end], text[end:]


def _set_field(fm, key, value):
    """2026-11-03：改用 frontmatter.set_field。

    旧实现只替换键行，原块列表续行（缩进项 / 顶格 `- item`）被留在
    原地，产出非法 YAML，1189 个论文页字段被 Obsidian 静默丢弃。
    set_field 会连带清除该键的续行。
    """
    return _fm.set_field(fm, key, value)
def _get_field(fm, key):
    m = re.search(r'^%s\s*:\s*(.*)$' % re.escape(key), fm, re.M)
    return m.group(1).strip() if m else ''


def _parse_list(raw):
    raw = raw.strip()
    if raw.startswith('[') and raw.endswith(']'):
        raw = raw[1:-1]
    return [x.strip().strip('"\'') for x in raw.split(',') if x.strip()]


def paper_text(path):
    """返回 (title, context, tags)。

    context = 摘要；摘要缺失或过短时回退到 ## 深度提炼 / ## 关键信息。
    2026-11-03 第 17 轮：实测 1414 个页面**没有** `## 摘要` 段、772 个页面
    摘要为空，但不少页面的 `## 深度提炼` 有上千字真实内容
    （例：10-1146-annurev-arplant-070225-032745，深度提炼 1664 字符）。
    旧实现只读摘要 → 这些论文的主题只用标题判定，几乎必然落空，
    于是被判 unclassified，实际是"读错了字段"。
    """
    try:
        t = io.open(path, encoding='utf-8', errors='replace').read(12000)
    except OSError:
        return '', '', []
    fm, body = _fm_split(t)
    tags = _parse_list(_get_field(fm, 'tags'))
    m = re.search(r'^# (.+)$', body, re.M)
    title = m.group(1) if m else ''
    am = re.search(r'## 摘要\s*\n(.{0,2500}?)\n## ', body, re.S)
    abstract = am.group(1).strip() if am else ''
    if len(abstract) < 200:
        parts = []
        for head in ('## 深度提炼', '## 关键信息', '## 摘要要点', '## 核心发现'):
            dm = re.search(head + r'[^\n]*\n(.+?)(?=\n## |\Z)', body, re.S)
            if dm:
                parts.append(dm.group(1).strip()[:2000])
        deep = '\n'.join(parts)
        if len(deep) > len(abstract):
            abstract = deep
    return title, abstract, tags


def evidence_text(path):
    try:
        t = io.open(path, encoding='utf-8', errors='replace').read(8000)
    except OSError:
        return None
    fm, body = _fm_split(t)
    tags = _parse_list(_get_field(fm, 'tags'))
    m = re.search(r'source:\s*"?\[\[([^\]]+)\]\]', fm)
    src = m.group(1) if m else ''
    cm = re.search(r'^## Claim\s*\n(.+?)(?=\n## |\Z)', body, re.M | re.S)
    claim = re.sub(r'\s+', ' ', cm.group(1)).strip() if cm else ''
    return {'fm': fm, 'body': body, 'tags': tags, 'source': src, 'claim': claim,
            'text': t}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    # 2026-11-03 第 16 轮：证据页默认跳过，必须显式 --include-evidence。
    # 原因：证据页的主题写在 `themes:` 字段（且多为 inherit-source-20261103
    # 的论文继承），本脚本却把主题当 tag 写进 `tags:`。两者存储约定不同，
    # 直接跑会把 11482 条证据的主题复制成 tag —— 标签精确计数被灌水，
    # 同时用关键词结果覆盖掉更可靠的论文继承，主题覆盖率会从 77% 掉回 ~15%。
    ap.add_argument('--include-evidence', action='store_true',
                    help='同时重算证据页主题（默认关闭，见函数内说明）')
    args = ap.parse_args()
    dry = not args.apply

    # 1. 论文页：先建索引（证据页需要论文上下文）
    paper_files = []
    for d in (PAPERS_DIR, TOP_DIR):
        if not os.path.isdir(d):
            continue
        for fn in sorted(os.listdir(d)):
            if fn.endswith('.md'):
                paper_files.append(os.path.join(d, fn))
    paper_ctx = {}
    paper_tags = {}
    for p in paper_files:
        slug = os.path.basename(p)[:-3]
        title, abstract, tags = paper_text(p)
        paper_ctx[slug] = title + '\n' + abstract
        paper_tags[slug] = tags

    stats = collections.Counter()
    per_theme = collections.Counter()
    changed_papers = 0
    changed_evidence = 0

    for p in paper_files:
        slug = os.path.basename(p)[:-3]
        title, abstract, tags = paper_text(p)
        tset, basis = th.assign_themes(tags, title + '\n' + abstract)
        tset = th.filter_supported_themes(tset, title + '\n' + abstract)
        tset = set(th.rank_themes(tset, title + '\n' + abstract)[:th.MAX_THEMES_PER_EVIDENCE])
        # 2026-11-03 第 16 轮：纯度守卫。
        # 实测：34 个页面带着主题标签，purity_gate 却判 nonplant
        # （茶多酚抑制金黄色葡萄球菌、E. coli 合成生物学、小鼠肿瘤、白血病 TCGA…）。
        # 它们的证据会顺着论文主题进入八主题，等于用动物/微生物论文写植物综述。
        # 只拦 'nonplant'；'suspect'（176 页）不动 —— 疑罪不能当定罪。
        purity_verdict = 'plant'
        if tset:
            purity_verdict, _pr = pg.classify_page(p)
            if purity_verdict == 'nonplant':
                tset, basis = set(), 'purity:nonplant'
            elif purity_verdict == 'suspect':
                # 2026-11-03 第 17 轮：suspect 页面此前可以带主题进库。
                # 实测受害例：Optimizing oral contraceptive timing（药代动力学）
                # 因正文出现 circadian 拿到 epigenetics 主题。
                # 口径不变（不移动、不删除 176 个 suspect 页），但要求它
                # 至少有一处植物线索才允许归属主题 —— 用 purity_gate 自己的
                # 词表，不引入第二套规则。
                # 只认标题级特异锚点（属名 / "plant immunity" 这类短语）。
                # 用正文泛词（含 'stem'、'seed'）判定会放过
                # "Optimizing oral contraceptive timing"（正文有 circadian 与
                # 'stem'? 这类泛词），实测确实漏过一例。
                _ttl = title.lower()
                _plant_signal = any(
                    c in _ttl for c in (pg.PLANT_ORGANISM + pg.PLANT_TITLE_ANCHOR))
                if not _plant_signal:
                    tset, basis = set(), 'purity:suspect-no-plant-cue'
        # 2026-11-03 第 17 轮：这里曾有一段 `evidence_eligible == 'false'
        # → tset 清空` 的死逻辑。它与下面的 ne 判定重复且更旧：227 个
        # eligible=false 页面里有 219 个只是缺 DOI 的真论文（alfalfa 花药
        # 单细胞图谱、拟南芥根再生…），却被这段代码压成 out-of-scope，
        # 于是 assign_themes 明明返回了主题也不写回。已删除，唯一判定下方 ne。
        try:
            raw = io.open(p, encoding='utf-8').read()
        except OSError:
            continue
        fm, body = _fm_split(raw)
        old = set(_parse_list(_get_field(fm, 'themes')))
        old_norm = {th.THEME_TAG_ALIASES.get(th.normalize_tag(x), th.normalize_tag(x))
                    for x in old if th.normalize_tag(x) != 'other'}
        # 2026-11-03 第 16 轮：`evidence_eligible:false` 不等于"非研究页"。
        # 实测 227 页里有 219 页是正常植物论文，只是没拿到 DOI
        # （alfalfa 花药单细胞图谱、拟南芥根再生…）。旧写法把它们一律
        # 改写成 theme_status: non-research，等于用元数据缺口抹掉真论文。
        # 现在只认 eligible_reason（classify_eligibility.py 写入）或明确的
        # 非研究 article_kind。
        _NON_RESEARCH_KINDS = {
            'corrigendum', 'erratum', 'retraction', 'expression-of-concern',
            'editorial', 'commentary', 'book-review', 'meeting-report', 'news',
            'front-matter', 'publisher-note', 'non-article', 'letter', 'reply',
        }
        # 2026-11-03 第 17 轮：农艺管理型标题 + 标题无主题词 → 主题外。
        if tset and th.management_scope_block(title):
            tset, basis = set(), th.MANAGEMENT_SCOPE_BASIS
        ne = (_get_field(fm, 'eligible_reason') == 'non-research'
              or (_get_field(fm, 'evidence_eligible') == 'false'
                  and _get_field(fm, 'eligible_reason') == ''
                  and _get_field(fm, 'article_kind') in _NON_RESEARCH_KINDS))
        if ne:
            new_raw, status = [], 'non-research'
        elif tset:
            new_raw = sorted(tset)
            status = 'mapped'
        else:
            # 2026-11-03 第 17 轮：删掉"关键词判不出就沿用旧 themes"的兜底。
            # 旧兜底看似保守，实则循环自证：旧 themes 正是同一套关键词引擎写的，
            # 沿用等于把手误永久固化。实测它让 76 个页面"关键词为空却仍 mapped"，
            # 其中包含 Corrigendum / Erratum / 人副流感病毒 / 猴痘流行学 /
            # 抗病毒药物化学等 —— 非研究页与非植物页靠这条兜底持续进主题。
            # 标签命中已在上方 by_tag 分支处理，故这里不再沿用旧值。
            #
            # 同时区分两个不同结论：
            #   out-of-scope  文本足够，判断为"不属于八主题"
            #   unclassified  文本不足（多为只有标题），无法判断
            new_raw = []
            status = ('out-of-scope' if th.evidence_sufficient(title + '\n' + abstract)
                      else 'unclassified')
            if status == 'unclassified':
                basis = th.UNCLASSIFIED_BASIS
        if purity_verdict == 'nonplant':
            # 打标不移动（与 A 类历史页同一口径）：页面保留，便于人工复核与回滚。
            new_raw, status = [], 'excluded-nonplant'
        # 2026-11-03 第 15 轮：非研究页要顺手清掉 tags 里的主题别名。
        # 旧实现把这段清理放在"是否变更"的早退之后，于是
        # `themes: []` + `theme_status: non-research` 已经正确的页面
        # （如 book-review 页）永远不会被清到，别名在 tags 里长期残留，
        # 自检因 `别名残留 2` 判 FAIL。
        tags_cleaned = False
        if ne:
            keep = [t for t in tags
                    if th.THEME_TAG_ALIASES.get(th.normalize_tag(t)) is None]
            if keep != tags:
                fm = _set_field(fm, 'tags', '[%s]' % ', '.join(keep))
                tags_cleaned = True
        if (new_raw == sorted(old_norm)
                and _get_field(fm, 'theme_status') == status
                and not tags_cleaned):
            stats['paper_unchanged'] += 1
            continue
        stats['paper_changed'] += 1
        for t in new_raw:
            per_theme[t] += 1
        if dry:
            continue
        fm2 = _set_field(fm, 'themes', '[%s]' % ', '.join(new_raw))
        fm2 = _set_field(fm2, 'theme_status', status)
        fm2 = _set_field(fm2, 'theme_basis', basis or 'none')
        if purity_verdict == 'nonplant':
            fm2 = _set_field(fm2, 'scope_status', 'nonplant')
        tmp = p + '.tmp'
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write('---' + fm2 + body)
        os.replace(tmp, p)
        changed_papers += 1

    # 2. 证据页（默认跳过：见 --include-evidence 的说明）
    ev_files = []
    if args.include_evidence and os.path.isdir(EVIDENCE_DIR):
        ev_files = [os.path.join(EVIDENCE_DIR, f) for f in sorted(os.listdir(EVIDENCE_DIR))
                    if f.endswith('.md')]
    for p in ev_files:
        rec = evidence_text(p)
        if rec is None:
            continue
        src = rec['source']
        ctx = paper_ctx.get(src, '')
        text = rec['claim'] + '\n' + ctx
        tset, basis = th.assign_themes(rec['tags'], text)
        tset = th.filter_supported_themes(tset, text)
        tset = set(th.rank_themes(tset, text)[:th.MAX_THEMES_PER_EVIDENCE])
        fm = rec['fm']
        cur = _parse_list(_get_field(fm, 'tags'))
        cur_norm = {th.normalize_tag(x) for x in cur}
        add = [t for t in sorted(tset) if t not in cur_norm]
        status = 'mapped' if tset else 'out-of-scope'
        already = (_get_field(fm, 'theme_status') == status and not add)
        if already:
            stats['ev_unchanged'] += 1
            continue
        stats['ev_changed'] += 1
        for t in add:
            per_theme[t] += 1
        if dry:
            continue
        new_tags = cur + add
        fm2 = _set_field(fm, 'tags', '[%s]' % ', '.join(new_tags))
        fm2 = _set_field(fm2, 'theme_status', status)
        fm2 = _set_field(fm2, 'theme_basis', basis or 'none')
        tmp = p + '.tmp'
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write('---' + fm2 + rec['body'])
        os.replace(tmp, p)
        changed_evidence += 1
        if args.limit and changed_evidence >= args.limit:
            break

    print(json.dumps({
        'dry_run': dry,
        'papers_total': len(paper_files),
        'evidence_total': len(ev_files),
        'paper_would_change': stats['paper_changed'],
        'paper_changed': changed_papers,
        'evidence_would_change': stats['ev_changed'],
        'evidence_changed': changed_evidence,
        'per_theme': dict(per_theme),
    }, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
