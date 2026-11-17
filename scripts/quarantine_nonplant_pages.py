# -*- coding: utf-8 -*-
"""quarantine_nonplant_pages.py — 导入层纯度闸门（2026-11-02 第 24 轮）

为什么需要它
------------
用户反复指出「纯度闸门只在下载层，导入层没拦」。核查后确认三点：
  1. 下载层 purity_gate.classify 是**黑名单**：只认命中的动物/临床词，
     末尾 `return 'plant', ['ok']` 是默认放行。实测它对
     「Reversible Thermoactuation ... Soft Bioelectronics」「Lipedema ...」
     「preterm birth ... in the human species」全部返回 plant/ok。
  2. 导入后唯一的检查 phase8_5_pollution **只打印告警**，不移动任何页面，
     且排在 synthesis/hypotheses 之后。
  3. 因此污染页一直留在 KB，参与登记表、孤儿统计与人工浏览。

判定（白名单思路，宁可漏放不误杀）
----------------------------------
A. 硬判据：organism_scope.page_verdict == 'nonplant'
   （研究对象明确是人/动物/临床，且方法不可迁移）
B. 零信号判据：plant_terms == 0 且 无具体物种 且 物种字段无真物种
   且 标题/摘要不含任何植物邻近词（crop/agronom/grain/forage/weed/...）
   —— 即整篇找不到任何"这是植物研究"的正面证据。
   这条专门对付"没有任何动物词"的软生物电子 / 医学综述类误入。
C. 豁免：概念页 themes 含 methods-tools（方法可迁移）→ 一律不隔离。

保守性：B 的植物邻近词表刻意放宽（只要沾边就放行），
并额外要求摘要非空，避免"摘要未获取"的页面被误伤。
**B 只进待审清单，不自动移动**：实测 B 会把「Rooibos 提取物」
（Rooibos = Aspalathus linearis，真植物）判成零信号，
说明 B 的假阳性率不可忽略，自动化不成立。

动作：移到 _review/archive/nonplant_<date>/papers/，文件名不变，可整目录回滚；
同时写 _review/nonplant_quarantine_<date>.tsv（doi/标题/判据/理由）。

用法
----
    python3 scripts/quarantine_nonplant_pages.py --date 2026-11-02          # 干跑
    python3 scripts/quarantine_nonplant_pages.py --date 2026-11-02 --apply
    python3 scripts/quarantine_nonplant_pages.py --all --dry-run | head     # 全库评估
"""
import argparse
import datetime as _dt
import json
import os
import re
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from kb_paths import BASE

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
REVIEW_DIR = os.path.join(BASE, '_review')
DOI_RE = re.compile(r'^doi:\s*"?([^"\n]+?)"?\s*$', re.M)
THEMES_RE = re.compile(r'^themes:\s*\n((?:\s*-\s*.+\n)+)', re.M)

# 植物邻近词：PLANT_TERMS 的漏网（crop/grain/forage/weed…在 organism_scope 里
# 都没有），用于"零信号"判据的保守豁免。只在本脚本用，不改 organism_scope，
# 以免漂移既有主题计数。
PLANT_ADJACENT = re.compile(
    r"(crop|cropping|agricultur|agronom|horticultur|forage|pasture|"
    r"\bgrain\b|\bseed\b|\bfruit\b|\bfloral?\b|\bflower\b|\btree\b|forest|"
    r"\bweed\b|herbicid|pesticid|fertiliz|\bsoil\b|orchard|greenhouse|"
    r"cultivar|germplasm|breeding|genotype[ds]?\b|field trial|"
    r"phytopathogen|\bfungus\b|fungal|mycorrhiz|rhizob|photosynth|"
    r"\bleaf\b|\bleaves\b|\bstem\b|\bstalk\b|\bspike\b|kernel|"
    r"vegetative|reproductive stage|biomass|yield|salin|drought|"
    r"larval|pollen|nectar|herbivor|endophyt|allelopath)", re.I)


def yaml_scalar(value, limit=None):
    """把任意文本写成安全的 YAML 双引号标量。

    实测：excluded_reason 里带论文标题（"… heterogeneity: insights from …"），
    未加引号时冒号让 YAML 认为这是嵌套映射，整页 frontmatter 解析失败。
    用 JSON 转义（YAML 是 JSON 的超集）最省事，也不怕引号与换行。
    """
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', ' ', str(value or ''))
    text = re.sub(r'\s+', ' ', text).strip()
    if limit:
        text = text[:limit]
    return json.dumps(text, ensure_ascii=False)

def _created(path):
    try:
        head = open(path, encoding='utf-8', errors='ignore').read(1500)
    except Exception:
        return None
    m = re.search(r'^created:\s*"?(\d{4}-\d{2}-\d{2})', head, re.M)
    return m.group(1) if m else None


def all_pages():
    for n in sorted(os.listdir(CONCEPTS_DIR)):
        if n.endswith('.md'):
            yield os.path.join(CONCEPTS_DIR, n)


def pages_created_on(day):
    return [p for p in all_pages() if _created(p) == day]


def is_method_page(path):
    try:
        head = open(path, encoding='utf-8', errors='ignore').read(3000)
    except Exception:
        return False
    m = THEMES_RE.search(head)
    return bool(m and 'methods-tools' in m.group(1))


def _parse(path):
    c = open(path, encoding='utf-8', errors='ignore').read()
    tm = re.search(r'^#\s+(.+)$', c, re.M)
    title = tm.group(1).strip() if tm else ''
    am = re.search(r'## 摘要\s*\n+(.*?)(?=\n##|\Z)', c, re.DOTALL)
    abstract = re.sub(r'\s+', ' ', am.group(1)).strip() if am else ''
    jm = re.search(r'期刊\*\*:?\s*(.+)', c)
    journal = jm.group(1).split('(')[0].strip() if jm else ''
    sp = re.search(r'\*\*物种\*\*:\s*(.+)', c)
    species = [s.strip() for s in sp.group(1).split(',')] if sp else []
    dm = DOI_RE.search(c[:2000])
    return title, abstract, journal, species, (dm.group(1) if dm else '')


def judge(path):
    """返回 (action, rule, reason)。action ∈ {'quarantine','keep'}

    判定语义**必须**与 organism_scope.paper_scope_table 一致，否则出现
    "页面被判 nonplant 但它的证据被当 methods 保留"的自相矛盾。
    要点：label 与 method 是两个独立维度 —— 方法学论文（用小鼠/临床数据
    做基准演示）label 常为 nonplant，但 method=True，只能改道
    methods-tools，绝不能整篇隔离。
    """
    import organism_scope as osc
    try:
        from purity_gate import PLANT_JOURNALS
    except Exception:
        PLANT_JOURNALS = None

    content = open(path, encoding='utf-8', errors='ignore').read()
    f = osc.page_fields(content)
    title, abstract = f['title'], f['abstract']
    journal, species = f['journal'], f['species']
    if not title and not abstract:
        return 'keep', '', 'empty'
    if is_method_page(path):
        return 'keep', '', 'method-transferable(theme)'

    text = title + ' ' + abstract
    # 方法学论文豁免：与 paper_scope_table 的 method 维度同源
    try:
        if osc.is_method_paper(text, f['themes'], f['tags'], title):
            return 'keep', '', 'method-transferable(paper)'
    except Exception:
        pass
    # 植物学期刊豁免：实测 10.3389/fpls.2026.1827397（Frontiers in Plant
    # Science，植被-土壤酶活性）因摘要出现 livestock 被判 nonplant。
    if PLANT_JOURNALS and journal and any(
            j in journal.lower() for j in PLANT_JOURNALS):
        return 'keep', '', 'plant-journal'

    v, why = osc.page_verdict(title, abstract, journal, species,
                              f['themes'], f['tags'])
    if v == 'nonplant':
        return 'quarantine', 'A-nonplant', '; '.join(why[:2])

    text = title + ' ' + abstract
    has_plant = bool(osc._hits(osc.PLANT_TERMS, text)) or \
        bool(osc._hits(osc.CONCRETE_SPECIES, text))
    concrete_sp = [s for s in species
                   if s and s not in osc.GENERIC_SPECIES
                   and osc.CONCRETE_SPECIES.search(s)]
    if has_plant or concrete_sp:
        return 'keep', '', 'plant-signal'
    if len(abstract) < 40:
        # 摘要缺失时不做零信号判定：宁可漏放
        return 'keep', '', 'no-abstract'
    if PLANT_ADJACENT.search(text):
        return 'keep', '', 'plant-adjacent'
    return 'quarantine', 'B-no-plant-signal', 'plant_terms=0; no species; no adjacent term'


# ---------------------------------------------------------------------------
# --tag-pages：A 类历史页打标（只标记、不移动）
# 2026-11-02 第 26 轮。为什么打标而不移动：A 类页可能已被 synthesis /
# relationships / hypotheses 引用，移动会打断 wikilink 并让综合页指向空链。
# 打标保留页面与链接，同时给读者与下游脚本一个显式排除信号
# （scope_status: excluded-nonplant），与 repair_nonplant_import 的
# stamp_concept 完全同格式。
# ---------------------------------------------------------------------------
FM_RE = re.compile(r'^---\n(.*?)\n---\n', re.S)
BANNER = ('> [!warning] 已排除（非植物研究对象）\n'
          '> 本文研究对象为动物/临床/工业体系，其生物学断言不得进入植物学主题。\n'
          '> 保留本页仅为追溯 DOI 与排除理由。\n\n')
WIKI_RE = re.compile(r'\[\[([^\]\|#]+)')
SKIP_DIRS = {'.git', '.trash', '.obsidian', '_review', 'archive', 'tmp', 'mnt'}


def _iter_markdown(root):
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS and not d.startswith('.')]
        for fn in fns:
            if fn.endswith('.md'):
                yield os.path.join(dp, fn)


def build_link_index():
    """wikilink 目标 stem -> 引用它的文件相对路径集合。"""
    idx = {}
    for p in _iter_markdown(BASE):
        try:
            txt = open(p, encoding='utf-8', errors='ignore').read()
        except OSError:
            continue
        if '[[' not in txt:
            continue
        rel = os.path.relpath(p, BASE)
        for m in WIKI_RE.finditer(txt):
            t = m.group(1).strip().split('/')[-1].strip()
            if t:
                idx.setdefault(t, set()).add(rel)
    return idx


def _stem(path):
    return os.path.basename(path)[:-3]


def stamp_page(path, reason, apply=False):
    txt = open(path, encoding='utf-8').read()
    if 'scope_status: excluded-nonplant' in txt:
        return 'already'
    fm = FM_RE.match(txt)
    if not fm:
        return 'no-frontmatter'
    new_fm = (fm.group(1).rstrip('\n')
              + '\nscope_status: excluded-nonplant\nexcluded_reason: '
              + yaml_scalar(reason, limit=160) + '\n')
    body = txt[fm.end():]
    if not body.lstrip().startswith('> [!warning] 已排除'):
        body = BANNER + body.lstrip('\n')
    if apply:
        open(path, 'w', encoding='utf-8').write('---\n' + new_fm + '\n---\n' + body)
    return 'stamped'


def tag_main(pages, args):
    day = args.date or _dt.date.today().isoformat()
    rows, stamped, already, nofm = [], 0, 0, 0
    for p in pages:
        try:
            action, rule, reason = judge(p)
        except Exception as exc:
            print('  !! %s: %s' % (os.path.basename(p), exc))
            continue
        if action != 'quarantine' or rule != 'A-nonplant':
            continue
        title, abstract, journal, species, doi = _parse(p)
        rows.append(dict(path=p, doi=doi, title=title, reason=reason))
    print('A 类候选：%d 篇（B 类不打标，只进待审清单）' % len(rows))
    if not rows:
        return 0
    lk = build_link_index()
    impact = {0: 0, 1: 0, 2: 0}
    for r in rows:
        st = _stem(r['path'])
        refs = sorted(lk.get(st, ()))
        r['n_in'] = len(refs)
        r['sample'] = '; '.join(refs[:3])
        r['from_synth'] = any(
            x.startswith(('synthesis', 'relationships', 'hypotheses'))
            or '/synthesis' in x for x in refs)
        impact[min(r['n_in'], 2)] += 1
    print('入链分布：0 条 = %d 篇，1 条 = %d 篇，>=2 条 = %d 篇'
          % (impact[0], impact[1], impact[2]))
    n_synth = sum(1 for r in rows if r['from_synth'])
    print('被 synthesis/relationships/hypotheses 引用：%d 篇（打标即可，不可移动）' % n_synth)
    top = sorted(rows, key=lambda r: -r['n_in'])[:10]
    for r in top:
        print('  in=%2d  %s' % (r['n_in'], r['title'][:70]))
        if r['n_in']:
            print('        <- %s' % r['sample'][:120])

    os.makedirs(REVIEW_DIR, exist_ok=True)
    outp = os.path.join(REVIEW_DIR, 'nonplant_tagplan_%s.tsv' % day)
    with open(outp, 'w', encoding='utf-8') as fh:
        fh.write('doi\ttitle\tfile\tn_inbound\tinbound_sample\treason\n')
        for r in rows:
            fh.write('\t'.join(str(x).replace('\t', ' ') for x in (
                r['doi'], r['title'], os.path.basename(r['path']), r['n_in'],
                r['sample'], r['reason'])) + '\n')
    print('打标计划：%s（%d 条）' % (outp, len(rows)))

    if not args.tag_apply:
        print('干跑：加 --tag-apply 才写盘。')
        return 0
    for r in rows:
        res = stamp_page(r['path'], 'nonplant|' + r['title'][:80], apply=True)
        stamped += res == 'stamped'
        already += res == 'already'
        nofm += res == 'no-frontmatter'
    print('已打标 %d 篇（已存在 %d，无 frontmatter %d）' % (stamped, already, nofm))
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument('--date', default=None)
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--apply', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--limit', type=int, default=0)
    ap.add_argument('--tag-pages', action='store_true',
                    help='A 类历史页打标：先干跑评估入链影响')
    ap.add_argument('--tag-apply', action='store_true',
                    help='配合 --tag-pages 真正写 scope_status')
    args = ap.parse_args(argv)
    day = args.date or _dt.date.today().isoformat()

    pages = list(all_pages()) if args.all else pages_created_on(day)
    if args.limit:
        pages = pages[:args.limit]
    print('检查范围：%s（%d 页）' % ('全库' if args.all else day, len(pages)))
    if args.tag_pages or args.tag_apply:
        return tag_main(pages, args)

    rows, n_q = [], 0
    arch = os.path.join(REVIEW_DIR, 'archive', 'nonplant_%s' % day, 'papers')
    for p in pages:
        try:
            action, rule, reason = judge(p)
        except Exception as exc:
            print('  !! %s: %s' % (os.path.basename(p), exc))
            continue
        if action != 'quarantine':
            continue
        title, abstract, journal, species, doi = _parse(p)
        rows.append((doi, rule, title[:90], reason, os.path.basename(p)))
        n_q += 1
    n_a = sum(1 for r in rows if r[1] == 'A-nonplant')
    print('判定命中：%d/%d 篇（A 自动隔离 %d，B 待审 %d）'
          % (n_q, len(pages), n_a, n_q - n_a))
    for r in rows[:60]:
        print('  [%s] %-34s %s' % (r[1], r[0] or '(no-doi)', r[2]))
        print('        %s' % r[3][:100])
    if len(rows) > 60:
        print('  ... 其余 %d 条见 TSV' % (len(rows) - 60))

    auto = [r for r in rows if r[1] == 'A-nonplant']
    cand = [r for r in rows if r[1] != 'A-nonplant']
    os.makedirs(REVIEW_DIR, exist_ok=True)
    if cand:
        ctsv = os.path.join(REVIEW_DIR, 'nonplant_candidates_%s.tsv' % day)
        with open(ctsv, 'w', encoding='utf-8') as fh:
            fh.write('doi\trule\ttitle\treason\tfile\n')
            for r in cand:
                fh.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')
        print('待审清单（不自动移动）：%s -> %d 条' % (ctsv, len(cand)))

    if args.apply and auto:
        os.makedirs(arch, exist_ok=True)
        for r in auto:
            src = os.path.join(CONCEPTS_DIR, r[4])
            if os.path.exists(src):
                shutil.move(src, os.path.join(arch, r[4]))
        tsv = os.path.join(REVIEW_DIR, 'nonplant_quarantine_%s.tsv' % day)
        with open(tsv, 'w', encoding='utf-8') as fh:
            fh.write('doi\trule\ttitle\treason\tfile\n')
            for r in auto:
                fh.write('\t'.join(x.replace('\t', ' ') for x in r) + '\n')
        print('已隔离 %d 篇（A 规则）-> %s' % (len(auto), arch))
        print('清单：%s' % tsv)
    elif not args.apply:
        print('干跑：将隔离 %d 篇（A 规则），待审 %d 篇（B 规则）'
              % (len(auto), len(cand)))
    else:
        print('本次无新增可隔离页（A 规则 0 篇，待审 %d 篇）' % len(cand))
    return 0


if __name__ == '__main__':
    sys.exit(main())
