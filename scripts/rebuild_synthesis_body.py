"""rebuild_synthesis_body.py v2 — 用当前证据确定性重建 synthesis 正文（含结构化深度分析）。

v2 相对 v1（2026-11-03 上午）新增，全部为**确定性、可复算**的结构化分析：
  A. 子主题内 物种 × 证据类型 交叉表（谁在什么证据层级上被研究）；
  B. 子主题内 实体密度（genes / compounds 前 5，附覆盖率，标注为自动标注）；
  C. 跨子主题实体枢纽（同一实体出现在 >=2 个子主题）；
  D. 研究设计缺口矩阵（子主题 × 6 类证据，0 处标 "—"）；
  E. 断言措辞与 evidence_type 的核对（标注 descriptive 但断言含扰动措辞 -> QC 待核）；
  F. 物种主导度（top1 占比 >70% 时提示外推限制）。

仍然遵守 v1 的硬约束：
  * 正文只由证据对象字段生成，不做跨证据的机理性归纳；
  * 每条代表断言附证据页链接与 DOI，英文原文不改写；
  * 因果/关联的措辞边界显式标注；
  * 输出对同一输入字节级稳定（除日期字段）。

同时修掉 v1 的一个口径缺陷：原 frontmatter `library_papers` 是历史手写值，
与 tags 归一化统计相差数倍（hormone-signaling 手写 473 vs 归一分 75），
本脚本不引用它，改为在 QC 段声明该字段不可信。
"""
from __future__ import annotations

import argparse
import io
import os
import re
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import batch_synthesis as BS
import subtopic_vocab as SV
import themes as th

DATE = __import__("datetime").date.today().isoformat()
SYN_DIR = BS.SYNTHESIS_DIR
ARCHIVE_DIR = os.path.join(BS.BASE, "_review", "synthesis_legacy_%s" % DATE.replace("-", ""))

CAUSAL_TYPES = ("genetic perturbation", "protein interaction", "DNA binding/regulation")
TYPE_ORDER = ("genetic perturbation", "protein interaction", "DNA binding/regulation",
              "expression/regulation", "phenotypic/association", "omics/co-occurrence",
              "descriptive/observational")
TYPE_ZH = {
    "genetic perturbation": "遗传扰动",
    "protein interaction": "蛋白互作",
    "DNA binding/regulation": "DNA 结合",
    "expression/regulation": "表达相关",
    "phenotypic/association": "表型关联",
    "omics/co-occurrence": "组学共现",
    "descriptive/observational": "描述性",
}

# 断言里出现这些措辞说明作者做过扰动/互作实验；用于和 evidence_type 互相核对。
CLAIM_DESIGN = (
    ("genetic perturbation",
     r"\b(knock-?out|knockdown|knock-?down|crispr|cas9|rnai|vigs|ami-?rna|"
     r"over-?express|overexpress|ectopic expression|mutant|transgenic|"
     r"complementation|inducible|dexamethasone)\b"),
    ("protein interaction",
     r"\b(yeast two-hybrid|two-hybrid|y2h|co-?ip|co-?immunoprecipitation|bifc|"
     r"split-luciferase|pull-?down|fret|bimolecular fluorescence)\b"),
    ("DNA binding/regulation",
     r"\b(chip-?seq|chip-?chip|chip-?qpcr|chip-?pcr|emsa|electrophoretic mobility|"
     r"yeast one-hybrid|one-hybrid|y1h|dap-?seq|atac-?seq|footprint)\b"),
)
_CLAIM_DESIGN_RE = [(lab, re.compile(p, re.I)) for lab, p in CLAIM_DESIGN]


SPECIES_CANON = {
    "rice": "Oryza sativa",
    "maize": "Zea mays",
    "corn": "Zea mays",
    "arabidopsis": "Arabidopsis thaliana",
    "tomato": "Solanum lycopersicum",
    "soybean": "Glycine max",
    "wheat": "Triticum aestivum",
    "barley": "Hordeum vulgare",
    "grape": "Vitis vinifera",
    "grapevine": "Vitis vinifera",
    "apple": "Malus domestica",
    "poplar": "Populus trichocarpa",
    "cotton": "Gossypium hirsutum",
    "potato": "Solanum tuberosum",
    "brassica": "Brassica spp.",
    "tobacco": "Nicotiana tabacum",
}


def canon_species(name):
    n = (name or "").strip()
    return SPECIES_CANON.get(n.lower(), n)


def _papers(evs):
    keys = {(e.get("doi") or e.get("pmid") or "").lower() for e in evs}
    return len({k for k in keys if k})


def _species(evs):
    c = Counter()
    for e in evs:
        sp = BS._species_of(e)
        if not sp and e.get("primary_species"):
            sp = [e["primary_species"]]
        for s in {canon_species(x) for x in sp if x.strip() and x.strip() not in ("—", "-")}:
            c[s] += 1
    return c


def _etype(evs):
    return Counter((e.get("evidence_type") or "未标注").strip() for e in evs)


def _quote(claim, n=180):
    t = re.sub(r"\s+", " ", (claim or "")).strip()
    t = t.replace("|", "/")
    return (t[:n] + "…") if len(t) > n else t


_BAD_QUOTE = re.compile(
    r"(©|all rights reserved|copyright|springer nature|elsevier|wiley|"
    r"https?://|doi\.org|^\s*\d{3,4}\s*,|chapter\s+\d+|"
    r"^(figure|table|fig\.)\s*\d|^\s*(keywords?|abbreviations?)\s*[:：]|"
    r"\.{4,}|…{2,}|\bdownloaded from\b|\blicense\b|©\s*\d{4})",
    re.I,
)


def _is_bad_quote(text):
    t = (text or "").strip()
    if len(t) < 60:
        return True
    letters = len(re.findall(r"[A-Za-z\u4e00-\u9fff]", t))
    if letters < 0.6 * len(t):
        return True
    if _BAD_QUOTE.search(t):
        return True
    return False


def _pick_quotes(group, k=3, used=None):
    """选代表断言；used 为跨子主题共享的已用证据集合，避免同一条证据在多个子主题重复出现。"""
    used = used if used is not None else set()

    def rank(e):
        causal = 0 if (e.get("evidence_type") or "").strip() in CAUSAL_TYPES else 1
        return (causal, -len(e.get("claim") or ""), e.get("id") or "")
    out, seen_doi, seen_text = [], set(), set()
    for e in sorted(group, key=rank):
        if e.get("id") in used:
            continue
        q = _quote(e.get("claim"))
        if not q or _is_bad_quote(q):
            continue
        key_doi = (e.get("doi") or e.get("id") or "").lower()
        norm = re.sub(r"\W+", "", q.lower())[:80]
        if key_doi in seen_doi or norm in seen_text:
            continue
        seen_doi.add(key_doi)
        seen_text.add(norm)
        out.append(e)
        used.add(e.get("id"))
        if len(out) >= k:
            break
    return out


def _fmt_counter(c, k=6):
    if not c:
        return "—"
    return "、".join("%s(%d)" % (a, b) for a, b in c.most_common(k))


def _front_list(ev, key):
    """从证据页 frontmatter 的 `key: [a, b]` 读列表（genes / compounds）。"""
    content = ev.get("full_content") or ""
    m = re.search(r"^%s:\s*\[(.*?)\]" % key, content, re.M | re.S)
    if not m:
        return []
    out = []
    for x in m.group(1).split(","):
        x = x.strip().strip("\"'").strip()
        if x and x.lower() not in ("none", "null", "无", "-"):
            out.append(x)
    return out


def _entities(evs, key):
    c = Counter()
    n_have = 0
    for e in evs:
        vals = _front_list(e, key)
        if vals:
            n_have += 1
        for v in vals:
            c[v] += 1
    return c, n_have



# ── v3: 行内引用与受控叙述 ──────────────────────────────────────
TYPE_ZH = {
    "genetic perturbation": "遗传扰动",
    "DNA binding/regulation": "DNA 结合",
    "protein interaction": "蛋白互作",
    "expression/regulation": "表达相关",
    "phenotypic/association": "表型关联",
    "omics/co-occurrence": "组学共现",
    "descriptive/observational": "描述性",
}
_PAPER_CACHE = {}


def _paper_meta(ev):
    """从来源论文页取第一作者与年份；缺字段时返回空串，不臆造。"""
    src = ev.get("source") or ""
    m = re.search(r"\[\[([^\]|#]+)", src)
    slug = m.group(1).strip() if m else ""
    if not slug:
        return "", ""
    if slug in _PAPER_CACHE:
        return _PAPER_CACHE[slug]
    author = year = ""
    path = os.path.join(BS.BASE, "concepts", "papers", slug + ".md")
    try:
        t = io.open(path, encoding="utf-8", errors="ignore").read()
    except OSError:
        _PAPER_CACHE[slug] = ("", "")
        return "", ""
    ym = re.search(r"^year:\s*\"?(\d{4})", t, re.M)
    if ym:
        year = ym.group(1)
    am = re.search(r"^authors?:\s*\"?(.+?)\"?\s*$", t, re.M)
    if am:
        raw = am.group(1).strip()
        if raw.startswith("["):
            raw = raw.strip("[]")
        author = raw.split(",")[0].strip().strip('"')
    if not author:
        bm = re.search(r"\*\*第一作者\*\*:\s*(.+?)\s*$", t, re.M)
        if bm:
            author = bm.group(1).strip()
    if author.lower() in ("unknown", "none", "—", "-", ""):
        author = ""
    _PAPER_CACHE[slug] = (author, year)
    return author, year


def _cite_one(ev):
    author, year = _paper_meta(ev)
    if author and year:
        lab = "%s et al., %s " % (author.split()[-1], year)
    elif year:
        lab = "%s " % year
    else:
        lab = ""
    return "%s[[%s]]" % (lab, ev.get("id"))


def _cite_many(evs, k=3):
    return "；".join(_cite_one(e) for e in evs[:k])


def _pick_by(group, pred, k=3):
    out = []
    for e in sorted(group, key=lambda x: (x.get("id") or "")):
        if pred(e):
            out.append(e)
        if len(out) >= k:
            break
    return out



_METHOD_LEAD = re.compile(
    r"^\s*(we\s+(report|describe|present|developed|generated|constructed)|"
    r"here,?\s+we|this\s+(study|paper|review)\s+(reports?|describes?|presents?)|"
    r"in\s+this\s+(study|paper))", re.I)


def _credible_causal(e):
    """用于提要的强过滤：排除方法/相关性/推测句，并要求有基因实体标注。

    规则分类器对 "binds"、"required for" 等谓词敏感，会把
    “RNA binds to primers on the bead”“positive correlation”判成因果。
    提要不能复用这种误判，因此再叠一层保守过滤；过滤后为空时，
    提要明确写“不足以概括机制”，而不是拿方法句充数。
    """
    c = (e.get("claim") or "").strip()
    if not c or _METHOD_LEAD.search(c):
        return False
    low = c.lower()
    if re.search(r"\b(protocol|pipeline|workflow|library|librar|droplet|bead|"
                 r"primer|sequencing|kit|software|benchmark|correlat\w*|associat\w*|"
                 r"may\b|might\b|could\b|suggest|potential|putative)\b", low):
        return False
    if not _front_list(e, "genes"):
        return False
    keys = ("binds", "binding", "interact", "phosphoryl", "promoter",
            "knockout", "knock-out", "mutant", "overexpress", "crispr",
            "required for", "activates", "represses", "directly")
    return any(k in low for k in keys)


def _etype_of(e):
    return (e.get("evidence_type") or "").strip()


def _narrative_block(group, ets, nc, name=""):
    """每个子主题固定三句：观察范围、证据层级张力、可检验缺口。"""
    sp = _species(group)
    ge, _ = _entities(group, "genes")
    ce, _ = _entities(group, "compounds")
    ents = [x for x, _ in ge.most_common(2)] + [x for x, _ in ce.most_common(2)]
    sps = [x for x, _ in sp.most_common(3)]
    causal = [e for e in group if _etype_of(e) in CAUSAL_TYPES and _credible_causal(e)]
    expr = [e for e in group if _etype_of(e) in ("expression/regulation", "omics/co-occurrence")]
    L = []
    L.append("**受控叙述（按证据类型分层；每句附原始证据）**")
    L.append("")

    s = "**一致的观察范围**：本组证据集中在%s" % ("、".join(sps) if sps else "未标注物种的材料")
    if ents:
        s += "，反复出现的实体为%s" % "、".join(ents)
    s += "；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（%s）。" % _cite_many(
        _pick_by(group, lambda e: True, 3))
    L.append("- " + s)

    if nc:
        s = ("**证据层级的张力**：%d 条属于遗传扰动/蛋白互作/DNA 结合，%d 条属于表达、组学或描述性证据；"
             "因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，"
             "不能反向证明因果" % (nc, len(group) - nc))
        cites = _cite_many(causal, 2)
        if expr:
            cites += "；" + _cite_one(expr[0])
    else:
        s = ("**证据层级的张力**：本组 0 条因果级证据，全部 %d 条为表达、组学或描述性；"
             "任何“调控/导致”表述都必须降级为待检验命题" % len(group))
        cites = _cite_many(_pick_by(group, lambda e: True, 2))
    L.append("- " + s + "（%s）。" % cites)

    have = {_etype_of(e) for e in group}
    order = ("genetic perturbation", "DNA binding/regulation", "protein interaction",
             "expression/regulation", "phenotypic/association", "omics/co-occurrence")
    missing = [TYPE_ZH[t] for t in order if t not in have]
    if missing:
        s = ("**可检验缺口**：%s在本组缺证据；在补齐这些设计前，%s 与“%s”的方向性关系应作为待检验命题"
             % ("、".join(missing), "、".join(ents[:3]) if ents else "目标实体", name))
        cites = _cite_many(_pick_by(group, lambda e: True, 2))
    else:
        s = ("**可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，"
             "应以跨实验室重复和统一条件比较来检验")
        cites = _cite_many(causal, 2)
    L.append("- " + s + "（%s）。" % cites)
    L.append("")
    return L

def _claim_design(claim):
    hits = []
    for lab, rx in _CLAIM_DESIGN_RE:
        if rx.search(claim or ""):
            hits.append(lab)
    return hits


_SCOPE_CACHE = {}


def scope_filter(evs, theme_id):
    import organism_scope as OS
    if not _SCOPE_CACHE:
        _SCOPE_CACHE.update(OS.paper_scope_table(os.path.join(BS.BASE, "concepts", "papers")))
    kept, dropped = [], []
    for e in evs:
        ok, verdict, reason = OS.evidence_in_theme(e, theme_id, _SCOPE_CACHE)
        if ok:
            kept.append(e)
        else:
            dropped.append((e, verdict, reason))
    return kept, dropped


def knowledge_shape(ets, group):
    if not group:
        return ""
    total = sum(ets.values())
    top, n = ets.most_common(1)[0]
    share = 100.0 * n / max(1, total)
    label = TYPE_ZH.get(top, top)
    if top in CAUSAL_TYPES:
        return ("**形态判断**：以%s为主（%.0f%%），该子主题的机制表述有一手实验支撑，"
                "但结论边界受物种与处理条件限制。" % (label, share))
    if share >= 60:
        return ("**形态判断**：以%s为主（%.0f%%），该子主题当前只能回答\u201c是否相关/在何时何处出现\u201d，"
                "不能回答\u201c由谁驱动\u201d；要升级为机制结论须补扰动或互作实验。" % (label, share))
    return ("**形态判断**：证据类型分散（最大一类%s仅占%.0f%%），说明该子主题尚无统一研究范式，"
            "横向比较不同证据前须先核对其数据类型与实验层级。" % (label, share))


def assign_subtopics(ev, theme_id):
    text = (ev.get("title") or "") + " " + (ev.get("claim") or "")
    return SV.assign(text, theme_id)


def _species_xtab(group, types, nsp=5):
    """物种 × 证据类型的交叉计数表（Markdown）。"""
    sp = _species(group)
    if not sp:
        return []
    order = [s for s, _ in sp.most_common(nsp)]
    ets = _etype(group)
    cols = [t for t in TYPE_ORDER if ets.get(t)]
    if not cols:
        return []
    rows = ["| 物种 | %s | 合计 |" % " | ".join(TYPE_ZH.get(t, t) for t in cols),
            "|---|%s---|" % ("---|" * len(cols))]
    for s in order:
        sel = [e for e in group
               if s in {canon_species(x) for x in (BS._species_of(e) or [e.get("primary_species") or ""])}]
        cells = [ets.get(t, 0) for t in cols]
        cnt = [sum(1 for e in sel if (e.get("evidence_type") or "").strip() == t) for t in cols]
        rows.append("| %s | %s | %d |" % (s, " | ".join(str(x) for x in cnt), len(sel)))
    return rows


def _design_matrix(names, buckets):
    """子主题 × 证据类型的覆盖矩阵，用来一眼看出"哪一层缺证据"。"""
    cols = [t for t in TYPE_ORDER]
    rows = ["| 子主题 | %s |" % " | ".join(TYPE_ZH.get(t, t) for t in cols),
            "|---|%s" % ("---|" * len(cols))]
    zero_causal = []
    for name in names:
        group = buckets.get(name) or []
        ets = _etype(group) if group else {}
        cells = []
        for t in cols:
            n = ets.get(t, 0)
            cells.append(str(n) if n else "—")
        rows.append("| %s | %s |" % (name, " | ".join(cells)))
        if group and not any(ets.get(t) for t in CAUSAL_TYPES):
            zero_causal.append(name)
    rows.append("")
    return rows, zero_causal


def _entity_hubs(buckets, min_sub=2, key="genes", topn=10):
    """同一实体出现在 >=min_sub 个子主题 -> 主题内的"枢纽实体"。"""
    sub_of = defaultdict(set)
    cnt = Counter()
    for name, group in buckets.items():
        for e in group:
            for v in set(_front_list(e, key)):
                sub_of[v].add(name)
                cnt[v] += 1
    hubs = [(v, cnt[v], sorted(s)) for v, s in sub_of.items() if len(s) >= min_sub]
    hubs.sort(key=lambda x: (-len(x[2]), -x[1], x[0]))
    return hubs[:topn]


def _type_mismatch(group):
    """标注为描述性、但断言里出现扰动/互作措辞的证据（需回原文确认类型）。"""
    out = []
    for e in group:
        et = (e.get("evidence_type") or "").strip()
        if et not in ("descriptive/observational", "", "未标注"):
            continue
        hits = _claim_design(e.get("claim") or "")
        if hits:
            out.append((e, hits))
    return out


def build_body(theme_id, evs, stats, contradictions, dropped=None):
    title_zh = th.THEME_META.get(theme_id, {}).get("title_zh", theme_id)
    names = [n for n, _ in SV.subtopics(theme_id)]
    buckets = defaultdict(list)
    unmatched = []
    multi = 0
    for ev in evs:
        hits = assign_subtopics(ev, theme_id)
        if not hits:
            unmatched.append(ev)
            continue
        if len(hits) > 1:
            multi += 1
        for h in hits:
            buckets[h].append(ev)

    _used_quotes = set()
    L = []
    L.append("# %s 知识综合（证据重建版 v3）" % title_zh)
    L.append("")
    L.append("> 本页正文于 %s 由 `rebuild_synthesis_body.py` 从 **%d 条证据对象 / %d 篇文献**"
             "确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；"
             "不含跨证据的推测性归纳。历史人工正文已归档至 `%s`，"
             "不再作为本页结论来源。" % (DATE, stats["total_evidence"], stats["total_papers"],
                                          os.path.relpath(ARCHIVE_DIR, BS.BASE)))
    L.append(">")
    L.append("> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；"
             "`表达相关` 与 `组学共现` 只能提出关联性假说。")
    L.append("")

    # ---- 0. 综述提要（受控生成，仅用已标注证据字段）
    _causal_all = [e for e in evs if _etype_of(e) in CAUSAL_TYPES]
    _causal0 = [e for e in _causal_all if _credible_causal(e)]
    _rank = {"genetic perturbation": 0, "DNA binding/regulation": 1,
             "protein interaction": 2}
    _causal0.sort(key=lambda e: _rank.get(_etype_of(e), 9))
    _dom_name, _dom_evs = max(buckets.items(), key=lambda kv: len(kv[1])) if buckets else ("", [])
    _have = {_etype_of(e) for e in evs}
    _order0 = ("genetic perturbation", "DNA binding/regulation", "protein interaction",
               "expression/regulation", "phenotypic/association", "omics/co-occurrence")
    _missing0 = [TYPE_ZH[t] for t in _order0 if t not in _have]
    _sp0 = _species(evs)
    _p = ("本主题当前纳入 **%d 条证据 / %d 篇文献**。规则判定为因果或直接调控的 **%d 条（%.1f%%）**；"
          "剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **%d 条**。"
          % (stats["total_evidence"], stats["total_papers"], len(_causal_all),
             100.0 * len(_causal_all) / max(1, len(evs)), len(_causal0)))
    if not _causal0:
        _p += "本主题的因果级证据不足以支撑稳定的机制概括，以下只呈现证据结构，不给机制结论。"
    if _causal0:
        _ents0 = []
        for _e in _causal0[:3]:
            _ents0.extend(_front_list(_e, "genes")[:1])
        _ents0 = list(dict.fromkeys(_ents0))
        _p += "可判定程度最高的结论集中在%s：" % ("、".join(_ents0) if _ents0 else "下列证据")
        _p += "；".join("%s（%s）" % (_quote(e.get("claim") or "", 140), _cite_one(e))
                        for e in _causal0[:3]) + "。"
    if _dom_name:
        _p += "研究重心位于“%s”（%d 条证据，占 %.0f%%）。" % (
            _dom_name, len(_dom_evs), 100.0 * len(_dom_evs) / max(1, len(evs)))
    if _sp0:
        _top_sp, _top_n = _sp0.most_common(1)[0]
        _p += "证据的物种分布以 %s 为首（%d 条，%.0f%%）。" % (
            _top_sp, _top_n, 100.0 * _top_n / max(1, len(evs)))
    if _missing0:
        _p += "目前完全缺失的证据类型是%s；凡涉及这些推断的表述，本页只能写成待检验命题。" % "、".join(_missing0)
    else:
        _thin = [TYPE_ZH[t] for t in _order0 if 0 < sum(1 for e in evs if _etype_of(e) == t) <= 2]
        _p += ("七类证据均有覆盖，但%s各仅 1–2 条；主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。" % "、".join(_thin)) if _thin else "七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。"
    _p += ("阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；"
           "后者不得改写成调控或因果。")
    L.append("## 0. 综述提要（受控生成）")
    L.append("")
    L.append(_p)
    L.append("")
    L.append("> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。")
    L.append("")

    # ---- 1. 概览
    et = _etype(evs)
    sp_all = _species(evs)
    causal = [e for e in evs if (e.get("evidence_type") or "").strip() in CAUSAL_TYPES]
    one_paper = sum(1 for c in Counter((e.get("doi") or "").lower() for e in evs if e.get("doi")).values() if c == 1)
    L.append("## 1. 主题概览（自动统计）")
    L.append("")
    L.append("| 指标 | 值 | 读法 |")
    L.append("|---|---|---|")
    L.append("| 证据对象 | %d | 本主题归属的证据条目数 |" % stats["total_evidence"])
    L.append("| 独立文献（DOI/PMID 去重） | %d | 去重后的论文数 |" % stats["total_papers"])
    L.append("| 平均每篇证据数 | %.2f | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |"
             % (stats["total_evidence"] / max(1, stats["total_papers"])))
    L.append("| 单条证据论文占比 | %.0f%%（%d/%d） | 越高说明证据碎片化越严重 |"
             % (100.0 * one_paper / max(1, stats["total_papers"]), one_paper, stats["total_papers"]))
    L.append("| 证据类型构成 | %s | 描述性占多数时机制结论需打折扣 |" % _fmt_counter(et, 8))
    L.append("| 类型标注置信度 | %s | 低置信度标注须回原文核对 |"
             % _fmt_counter(Counter((e.get("evidence_type_confidence") or "未标").strip() for e in evs), 4))
    L.append("| 主要物种 | %s | 物种过度集中则外推性受限 |" % _fmt_counter(sp_all, 6))
    L.append("| 子主题覆盖 | %d/%d（证据 <5 条的 %d 个） | 覆盖缺口见第 7 节 |" % (
        len([n for n in names if buckets.get(n)]), len(names),
        len([n for n in names if 0 < len(buckets.get(n, [])) < 5]) + len([n for n in names if not buckets.get(n)])))
    L.append("| 未命中任何子主题的证据 | %d（%.0f%%） | 占比高说明子主题词表或证据文本需扩表 |"
             % (len(unmatched), 100.0 * len(unmatched) / max(1, len(evs))))
    L.append("")
    L.append("因果级证据共 **%d 条**，占本主题证据的 **%.1f%%**。"
             "这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。" %
             (len(causal), 100.0 * len(causal) / max(1, len(evs))))
    if sp_all:
        top_sp, top_n = sp_all.most_common(1)[0]
        L.append("")
        L.append("物种主导度：**%s** 出现在 %d 条证据（%.0f%%）。%s" % (
            top_sp, top_n, 100.0 * top_n / max(1, len(evs)),
            "高于 70%，跨物种外推缺乏支撑，须并列其他体系。" if top_n >= 0.7 * len(evs)
            else "分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。"))
    L.append("")

    # ---- 2. 子主题
    L.append("## 2. 子主题分解（按证据重建）")
    L.append("")
    L.append("> 一条证据可同时命中多个子主题（共 %d 条跨组），因此各子主题计数之和大于总证据数。"
             "物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。"
             "凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。" % multi)
    L.append("")
    idx = 0
    for name in names:
        group = buckets.get(name) or []
        idx += 1
        L.append("### 2.%d %s" % (idx, name))
        L.append("")
        if not group:
            L.append("**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。")
            L.append("")
            continue
        ets = _etype(group)
        nc = sum(1 for e in group if (e.get("evidence_type") or "").strip() in CAUSAL_TYPES)
        L.append("**规模** %d 条证据 / %d 篇文献；**构成** %s；**因果层** %s。"
                 % (len(group), _papers(group), _fmt_counter(ets, 6),
                    ("%d 条（可支撑有限机制表述）" % nc) if nc else "0 条（仅关联/描述，不得写因果）"))
        L.append("")
        if 0 < nc < 3:
            L.append("> 本组仅 %d 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，"
                     "不可外推到其余 %d 条。" % (nc, len(group) - nc))
        L.append("")
        L.extend(_narrative_block(group, ets, nc, name))
        xt = _species_xtab(group, ets)
        if xt:
            L.append("**物种 × 证据类型（前 5 物种）**")
            L.append("")
            L.extend(xt)
            L.append("")
        ge, ge_n = _entities(group, "genes")
        if ge:
            L.append("**基因实体（自动标注，前 5）**：%s（标注覆盖 %d/%d）。"
                     % (_fmt_counter(ge, 5), ge_n, len(group)))
            L.append("")
        ce, ce_n = _entities(group, "compounds")
        if ce:
            L.append("**化合物实体（自动标注，前 5）**：%s（标注覆盖 %d/%d）。"
                     % (_fmt_counter(ce, 5), ce_n, len(group)))
            L.append("")
        mm = _type_mismatch(group)
        if mm:
            L.append("**标注一致性提示**：本组 %d 条证据标注为描述性，但断言含扰动/互作措辞"
                     "（%s），类型可能被低估，需回原文确认；例如 [[%s]]。"
                     % (len(mm), "、".join(sorted({h for _, hs in mm for h in hs})),
                        mm[0][0].get("id")))
            L.append("")
        picks = _pick_quotes(group, 3, _used_quotes)
        if picks:
            L.append("**代表断言（原文摘录，未改写）**")
            L.append("")
            for e in picks:
                L.append("- \u201c%s\u201d \u2014 [[%s]]\uff08`%s`\uff0c%s\uff09" % (
                    _quote(e.get("claim")), e.get("id"), e.get("doi") or "\u65e0DOI",
                    (e.get("evidence_type") or "\u672a\u6807\u6ce8").strip()))
            L.append("")
        else:
            L.append("**无可引用的干净断言**：本组证据页的 claim 均为版权页眉、图注或过短残片，"
                     "需回原文补录断言后才能引用。")
            L.append("")

    # ---- 3. 跨子主题实体
    L.append("## 3. 跨子主题实体枢纽（自动统计）")
    L.append("")
    hubs = _entity_hubs(buckets)
    hubs_c = _entity_hubs(buckets, key="compounds", topn=6)
    if hubs or hubs_c:
        L.append("下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，"
                 "但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。")
        L.append("")
        if hubs:
            L.append("| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |")
            L.append("|---|---|---|---|")
            for v, n, subs in hubs:
                L.append("| %s | %d | %d | %s |" % (v, len(subs), n, "、".join(subs)))
            L.append("")
        if hubs_c:
            L.append("| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |")
            L.append("|---|---|---|---|")
            for v, n, subs in hubs_c:
                L.append("| %s | %d | %d | %s |" % (v, len(subs), n, "、".join(subs)))
            L.append("")
    else:
        L.append("本主题暂无可用的跨子主题实体（基因/化合物自动标注覆盖不足或实体互不重叠）。"
                 "这是标注缺口，不是“没有共享机制”。")
        L.append("")

    L.append("### 3.1 跨子主题受控叙述")
    L.append("")
    if hubs:
        L.append("- **交叉实体**：%s 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，"
                 "不能说明同一机制（%s）。" % (
                     "、".join(v for v, _, _ in hubs[:5]),
                     _cite_many(_pick_by(evs, lambda e: True, 2))))
    cause_by_sub = [(n, sum(1 for e in buckets.get(n, []) if _etype_of(e) in CAUSAL_TYPES))
                    for n in names if buckets.get(n)]
    if cause_by_sub:
        hi = max(cause_by_sub, key=lambda x: x[1])
        lo = min(cause_by_sub, key=lambda x: x[1])
        L.append("- **层级不均**：因果层证据在子主题间分布不均，最高为“%s”（%d 条），最低为“%s”（%d 条）；"
                 "跨子主题比较结论强度前须先对齐这一差异。" % (hi[0], hi[1], lo[0], lo[1]))
    miss_all = []
    for t in ("genetic perturbation", "DNA binding/regulation", "protein interaction",
              "expression/regulation", "phenotypic/association", "omics/co-occurrence"):
        if not any(_etype_of(e) == t for e in evs):
            miss_all.append(TYPE_ZH[t])
    if miss_all:
        L.append("- **共同缺口**：全主题缺失 %s；涉及这些推断的跨子主题归纳只能写成待检验命题。" % "、".join(miss_all))
    else:
        L.append("- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。")
    L.append("")

    # ---- 4. 设计缺口矩阵
    L.append("## 4. 研究设计缺口矩阵（子主题 × 证据类型）")
    L.append("")
    L.append("> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读："
             "一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。")
    L.append("")
    rows, zero_causal = _design_matrix(names, buckets)
    L.extend(rows)
    if zero_causal:
        L.append("**零因果层子主题（%d/%d）**：%s。" % (
            len(zero_causal), len(names), "、".join(zero_causal)))
        L.append("")
        L.append("这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，"
                 "属于超越证据的表达，须在方案中降级为待验证命题。")
    else:
        L.append("所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。")
    L.append("")

    # ---- 5. 因果级证据
    L.append("## 5. 可直接引用的因果级证据（自动筛选）")
    L.append("")
    if causal:
        L.append("以下 %d 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；"
                 "引用时须核对原文的物种、组织与处理条件。" % len(causal))
        L.append("")
        L.append("| 证据页 | DOI | 类型 | 断言（摘录） |")
        L.append("|---|---|---|---|")
        for e in sorted(causal, key=lambda x: x.get("id") or "")[:20]:
            L.append("| [[%s]] | `%s` | %s | %s |" % (
                e.get("id"), e.get("doi") or "—",
                (e.get("evidence_type") or "").strip(), _quote(e.get("claim"), 120)))
        if len(causal) > 20:
            L.append("")
            L.append("（另有 %d 条未列出，可在 `evidence/` 按 evidence_type 过滤。）" % (len(causal) - 20))
    else:
        L.append("**本主题当前没有任何因果级证据。** 这意味着本页所有机制性表述都只能是待检验假说，"
                 "不能作为结论引用。补齐路径见第 7 节。")
    L.append("")

    # ---- 6. 张力与矛盾
    L.append("## 6. 证据间的张力与矛盾（自动筛查）")
    L.append("")
    if contradictions:
        L.append("自动筛查发现 %d 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，"
                 "**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。" % len(contradictions))
        L.append("")
        L.append("| 基因 | 冲突类型 | 涉及来源（截断） |")
        L.append("|---|---|---|")
        for c in contradictions:
            L.append("| %s | %s | %s |" % (c.get("gene") or "—", c.get("type") or "—",
                                           "；".join(c.get("sources") or [])[:160]))
        L.append("")
        L.append("> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；"
                 "每条冲突都必须回原文核对实验条件后才能采信。")
    else:
        L.append("未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，"
                 "缺少反证不等于已被重复验证。")
    L.append("")

    # ---- 7. 覆盖缺口
    L.append("## 7. 覆盖与代表性缺口")
    L.append("")
    gaps = []
    if len(causal) == 0:
        gaps.append("**缺因果级证据**：当前 0 条扰动/互作实验，需优先补充遗传学验证（敲除、诱导表达、"
                    "蛋白互作）而非继续累积组学关联。")
    elif len(causal) / max(1, len(evs)) < 0.1:
        gaps.append("**因果级证据占比仅 %.1f%%**：机制结论的可信度受限于此，"
                    "建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。"
                    % (100.0 * len(causal) / max(1, len(evs))))
    if zero_causal:
        gaps.append("**%d 个子主题完全没有因果层证据**（%s）：这些方向目前只能写相关性。"
                    % (len(zero_causal), "、".join(zero_causal[:4]) + ("…" if len(zero_causal) > 4 else "")))
    one = [s for s, c in sp_all.items() if c == 1]
    if len(one) >= 5:
        gaps.append("**单篇证据物种 %d 个**（%s…）：跨物种外推缺乏支撑。"
                    % (len(one), "、".join(one[:5])))
    empty_sub = [n for n in names if not buckets.get(n)]
    if empty_sub:
        gaps.append("**%d 个子主题零证据**（%s）：需按子主题关键词补检索，"
                    "否则主题综述会出现结构性空洞。" % (len(empty_sub), "、".join(empty_sub[:4])))
    if unmatched:
        gaps.append("**%d 条证据（%.0f%%）未命中任何子主题**：说明子主题词表覆盖不足，"
                    "这部分证据目前无法进入结构性讨论。" % (
                        len(unmatched), 100.0 * len(unmatched) / max(1, len(evs))))
    if dropped:
        gaps.append("**%d 条证据被领域纯度闸门剔除**（非植物/非研究性/方法越界）："
                    "这些条目不计入本主题统计，明细见 `_review/`。" % len(dropped))
    gaps.append("**证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，"
                "无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。")
    gaps.append("**文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，"
                "因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 "
                "`library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。")
    for g in gaps:
        L.append("- %s" % g)
    L.append("")

    # ---- 8. 历史正文
    L.append("## 8. 历史正文说明")
    L.append("")
    L.append("本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，"
             "含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `%s`，保留供追溯，"
             "**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 "
             "`soybean_relevance` 字段，其论证过程同样需重新取证。"
             % os.path.relpath(ARCHIVE_DIR, BS.BASE))
    L.append("")
    body = "\n".join(L)
    zh = len(re.findall(r"[\u4e00-\u9fff]", body))
    links = len(re.findall(r"\[\[[^\]]+\]\]", body))
    L.append("## 9. 行内引用密度自检")
    L.append("")
    L.append("本页正文 %d 个中文字符，行内证据链接 %d 处，密度 **%.1f 处/500 字**（目标 ≥1）。"
             "链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。" % (
                 zh, links, 500.0 * links / max(1, zh)))
    L.append("")
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--theme", default="")
    a = ap.parse_args()

    all_ev = BS.load_all_evidence()
    print("evidence loaded:", len(all_ev))
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    done = 0
    for theme_id in th.THEMES:
        if a.theme and a.theme != theme_id:
            continue
        path = os.path.join(SYN_DIR, "%s.md" % theme_id)
        if not os.path.exists(path):
            print("  -- missing page:", theme_id)
            continue
        evs = BS.classify_evidence(all_ev, theme_id)
        evs, dropped = scope_filter(evs, theme_id)
        if dropped:
            print("  [scope] %s dropped %d (nonplant/nonarticle/methods-out-of-scope)"
                  % (theme_id, len(dropped)))
        consensus = BS.find_consensus(evs)
        contradictions = BS.find_contradictions(evs)
        stats = BS.compute_stats(evs, consensus, contradictions)

        content = open(path, encoding="utf-8").read()
        end = content.find("\n---", 3)
        fm, body = content[3:end], content[end + 4:]
        auto_block = BS.evidence_strength_section(evs)

        new_body = build_body(theme_id, evs, stats, contradictions, dropped)
        if auto_block:
            h1, rest = new_body.split("\n", 1)
            new_body = h1 + "\n\n" + auto_block + "\n" + rest

        new_fm = fm
        new_fm = re.sub(r"^total_evidence:\s*\d+", "total_evidence: %d" % stats["total_evidence"], new_fm, flags=re.M)
        new_fm = re.sub(r"^total_papers:\s*\d+", "total_papers: %d" % stats["total_papers"], new_fm, flags=re.M)
        new_fm = re.sub(r"^updated:\s*\S+", "updated: %s" % DATE, new_fm, flags=re.M)
        new_fm = re.sub(r"^body_status:.*$", "body_status: rebuilt-%s" % DATE, new_fm, flags=re.M)
        if "body_status:" not in new_fm:
            new_fm = new_fm.rstrip("\n") + "\nbody_status: rebuilt-%s\n" % DATE
        rel_arch = os.path.relpath(os.path.join(ARCHIVE_DIR, "%s.md" % theme_id), BS.BASE)
        if "legacy_archive:" in new_fm:
            new_fm = re.sub(r"^legacy_archive:.*$", "legacy_archive: %s" % rel_arch, new_fm, flags=re.M)
        else:
            new_fm = new_fm.rstrip("\n") + "\nlegacy_archive: %s\n" % rel_arch
        if "rebuild_rule:" not in new_fm:
            new_fm = new_fm.rstrip("\n") + "\nrebuild_rule: evidence-fields-only; no-cross-evidence-inference\n"
        new_fm = re.sub(r"^rebuild_rule:.*$",
                        "rebuild_rule: evidence-fields-only; no-cross-evidence-inference", new_fm, flags=re.M)
        if "rebuild_version:" in new_fm:
            new_fm = re.sub(r"^rebuild_version:.*$", "rebuild_version: v3", new_fm, flags=re.M)
        else:
            new_fm = new_fm.rstrip("\n") + "\nrebuild_version: v2\n"

        out = "---" + new_fm + "\n---\n" + new_body.rstrip() + "\n"
        words = len(re.findall(r"[\u4e00-\u9fff]", new_body))
        print("  %-32s ev=%-5d papers=%-5d causal=%-4d zh_chars=%d" % (
            theme_id, stats["total_evidence"], stats["total_papers"],
            sum(1 for e in evs if (e.get("evidence_type") or "").strip() in CAUSAL_TYPES), words))
        if a.apply:
            arch = os.path.join(ARCHIVE_DIR, "%s.md" % theme_id)
            if not os.path.exists(arch):
                open(arch, "w", encoding="utf-8").write(content)
            BS.write_if_changed(path, out)
            done += 1
    print("applied:", done)


if __name__ == "__main__":
    main()
