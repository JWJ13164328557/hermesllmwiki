#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase 8: 从证据簇生成"可证伪的假说"与"可执行的实践方案"。

2026-11-02 重写说明（旧版为何必须废弃）
----------------------------------------
旧版对每条证据簇套模板，输出形如：
    ### Hypothesis 3: ABRE
    **Statement**: ABRE induce ABA to control [process]
    **Support**: Supported by 1 independent evidence objects
问题不是"风格不好"，而是三类硬错误：
  1. **实体不是基因**：正则把顺式元件（ABRE）、激素缩写（IAA/ABA/ETH）、
     蛋白片段（GP2）当成靶基因，再拼成"ABRE 诱导 ABA"这种不存在的关系；
  2. **字面占位符**：`[process]` / `[model species]` / `[phenotype]` 直接落盘，
     读者无法判断"该做什么实验"，等于没有实践方案；
  3. **证据不足也发言**：单条证据、单篇论文就生成一条假说，且不给证据 ID，
     无法回溯。旧版 8 个主题里"单细胞与空间组学"只匹配到 9 条证据
     （真实 253 条），因为主题标签与证据标签对不上。

新版的三条硬约束
----------------
A. **只用可信实体**：靶基因优先取证据页 `genes:` 前端字段，且过黑名单
   （顺式元件/激素/技术缩写/物种缩写一律拒绝）；正文正则只作补充。
B. **零占位符**：所有槽位必须由证据填充；填不满的簇直接丢弃，不生成假说。
C. **每条假说必须可证伪**：给出"操纵变量 / 对照 / 读出 / 若为真应观察到 /
   若为假应观察到"，并列出支撑证据 ID（>=3 条、>=2 篇独立论文）。

另加 `--check` 门禁：对已落盘的页面做同一套校验，失败返回非零，
供 daily_full_pipeline 当作质量闸门（而不是"跑完就算成功"）。
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import date

from kb_paths import BASE, CONCEPTS_DIR
import themes as th
from organism_scope import (
    GENERIC_SPECIES, ANIMAL_TERMS, PLANT_TERMS,
    classify_text as classify_organism,
    clean_abstract as _clean_abstract,
    evidence_verdict,
    evidence_in_theme,
    paper_scope_table,
)

EVIDENCE_DIR = os.path.join(BASE, 'evidence')
SYNTHESIS_DIR = os.path.join(BASE, 'synthesis')
HYPOTHESES_DIR = os.path.join(BASE, 'hypotheses')
PROGRAMS_DIR = os.path.join(BASE, 'research-programs')

TODAY = date.today().isoformat()

# 每条假说至少需要的支撑量（防止"一条证据一条假说"）
MIN_EVIDENCE_PER_HYPOTHESIS = 3
MIN_PAPERS_PER_HYPOTHESIS = 2
MIN_HYPOTHESES_PER_THEME = 3   # 目标值：达到即视为证据充足
HARD_MIN_HYPOTHESES = 1        # 硬下限：1 条 + 证据不足声明 也算合格产物
MAX_HYPOTHESES_PER_THEME = 6

# ── 非基因符号黑名单 ────────────────────────────────────────────────
# 来源：旧版实际误判案例 + 常见顺式元件/激素/技术缩写/物种缩写。
NON_GENE = frozenset('''
ABRE DRE CRT GCC GBOX EBOX TATA CAAT MYC1 WBOX G-BOX ABREs
IAA ABA JA SA BR CK GA GA3 GA4 ETH ACC ROS NO H2O2 BL CS
PCR QPCR RTPCR RNA DNA CDNA ATP GTP GFP GUS LUC YFP CFP RFP
WT KO OE CHIP SEQ MS HPLC GC LC FDR GO KEGG PCA DEG SNP QTL
RIL BAC CDS UTR ORF TF TFS MUTANT TRANSGENE
AT OS ZM GM SL NT PT MT TA BN VV GH AL
FIG TABLE SUPP DATASET GEO SRA NCBI PMC DOI PMID
II III IV V VI VII MM CM ML MG KG MIN
'''.split())

# 明显是动物/医学模式系统的基因：KB 物种字段全部为植物，
# 这些名字只会出现在"比较/引用"语境，不能当植物假说靶标。
# 化学试剂/处理名称，常被误判为基因
CHEMICALS = frozenset('''
FESO4 ZNSO4 CUSO4 MGSO4 CACL2 NACL KCL H2O2 NO SA_MEJA TSA SB
BAP NAA 2_4D IAA_KINETIN GA3 ABA_MEJA MOCK DMSO
'''.split())

ANIMAL_GENES = frozenset("""
PROX1 MZF1 EOMES SOX2 SOX9 OCT4 POU5F1 PAX6 PAX3 MYOD MYF5 MYOG
FOXA1 FOXA2 FOXG1 MKI67 NANOG KLF4 CMYC MEF2C GATA1 GATA2 GATA3
HAND2 NKX25 TBX5 ISL1 OLIG2 GFAP NESTIN S100B CD34 CD44 EPCAM
AER ZIC1 ZIC2 USF1 XBP1 SHH IHH DHH FGF8 BMP4 NODAL LEFTY
MFGE8 ZBTB33 LGR5 CDX2 HNF4A TP53 BRCA1 KRAS PTEN AKT1 MTOR
IL6 TNF CXCL8 CD68 CD163 ACTA2 VIM DES S100A4 PECAM1 CDH5

""".split())

# 明显是"过程/表型"而非基因的名词，避免把表型当靶点
PROCESS_NOUNS = (
    'lignin', 'cellulose', 'anthocyanin', 'flavonoid', 'carotenoid',
    'chlorophyll', 'starch', 'sucrose', 'sugar', 'lipid', 'auxin',
    'cytokinin', 'gibberellin', 'ethylene', 'abscisic acid', 'jasmon',
    'salicylic acid', 'brassinosteroid', 'nitrate', 'phosphate',
)

# ── 关系抽取模式：(类别, 正则) ───────────────────────────────────────
POS_VERBS = r'(?:positively\s+)?(?:regulat\w*|promot\w*|enhanc\w*|induc\w*|activat\w*|increas\w*|up-?regulat\w*)'
NEG_VERBS = r'(?:negatively\s+)?(?:regulat\w*|inhibit\w*|repress\w*|suppress\w*|reduc\w*|decreas\w*|down-?regulat\w*)'


# ============================================================
# 读取证据
# ============================================================
def _parse_list_field(content, key):
    """解析 `key: [a, b]` 或块状 `key:\n  - a\n  - b` 两种写法。"""
    m = re.search(r'^%s:\s*\[(.*?)\]' % re.escape(key), content, re.M | re.S)
    if m:
        raw = m.group(1)
        return [x.strip().strip('"\'') for x in raw.split(',') if x.strip()]
    m = re.search(r'^%s:\s*\n((?:[ \t]*-[ \t]*.+\n?)+)' % re.escape(key), content, re.M)
    if m:
        return [x.strip().lstrip('-').strip().strip('"\'')
                for x in m.group(1).splitlines() if x.strip()]
    m = re.search(r'^%s:\s*"?([^"\n]+)"?\s*$' % re.escape(key), content, re.M)
    if m:
        v = m.group(1).strip().strip('"\'')
        return [v] if v else []
    return []


def _parse_str_field(content, key):
    m = re.search(r'^%s:\s*"?(.*?)"?\s*$' % re.escape(key), content, re.M)
    return m.group(1).strip() if m else ''


def load_evidence():
    """读全部证据对象，字段与 batch_synthesis 保持一致（同一份定义）。"""
    out = []
    if not os.path.isdir(EVIDENCE_DIR):
        return out
    for fname in sorted(os.listdir(EVIDENCE_DIR)):
        if not fname.endswith('.md'):
            continue
        path = os.path.join(EVIDENCE_DIR, fname)
        try:
            with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                content = fh.read()
        except OSError:
            continue

        claim = ''
        m = re.search(r'^##\s*Claim\s*\n(.+?)(?=\n##|\Z)', content, re.S | re.M)
        if m:
            claim = ' '.join(m.group(1).split())
        if not claim:
            m = re.search(r'^claim:\s*"?(.+?)"?\s*$', content, re.M)
            if m:
                claim = ' '.join(m.group(1).split())
        if not claim:
            continue
        claim = strip_line_numbers(normalize_claim(claim))

        # 与 batch_synthesis.load_all_evidence 保持一致：老格式证据页没有
        # tags，但有 claim_type（method/observation/…）与 species/tissue。
        # 缺这一步会让 37 篇无标签页里 17 篇真正的
        # 方法学论文（DESeq2/Harmony/featureCounts）永远进不了
        # methods-tools，两个脚本算出的主题规模也因此对不上。
        title = _parse_str_field(content, 'title').strip('"')
        tags = _parse_list_field(content, 'tags')
        if not tags:
            _ct = _parse_str_field(content, 'claim_type')
            _ct_map = {'methodological': 'method', 'method': 'method',
                       'observation': 'observation', 'functional': 'functional'}
            if _ct:
                tags = [_ct_map.get(_ct, _ct)]
            _sp = _parse_list_field(content, 'species') or _parse_list_field(content, 'primary_species')
            _ti = _parse_list_field(content, 'tissue')
            tags = tags + [x for x in _sp[:3]] + [x for x in _ti[:2]]
        species = _parse_list_field(content, 'species')
        if not species:
            species = _parse_list_field(content, 'primary_species')
        genes = _parse_list_field(content, 'genes')
        compounds = _parse_list_field(content, 'compounds')
        doi = _parse_str_field(content, 'doi')
        pmid = _parse_str_field(content, 'pmid')
        ev_type = _parse_str_field(content, 'evidence_type')
        quality = _parse_str_field(content, 'quality')
        source = _parse_str_field(content, 'source')

        # 证据池卫生：没有 DOI 的页面不是"某篇论文的一条证据"
        # （历史上 concepts 页被误放进 evidence/，会污染假说溯源）
        if not doi:
            continue

        # 与 batch_synthesis 同一道论断角色闸门：背景/方法句不进证据池。
        role = _parse_str_field(content, 'claim_role') or 'finding'
        if role in ('method', 'background'):
            continue

        primary = _parse_str_field(content, 'primary_species')
        _theme_text = (title or '') + ' ' + claim
        # 主题归属优先级（2026-11-03 第 14 轮）：
        #   1) 证据页 frontmatter 的 themes:（由源论文继承，已过 claim 守卫）
        #   2) 退回 themes.assign_themes(tags + claim 文本)
        # 过去只走 (2)，而证据页 tags 常是检索关键词（papers/dpdf/metabolism），
        # 于是 12291 条证据里只有 13.2% 能归属，而它们的源论文 66.8% 已归属。
        # 现在 (1) 是权威来源，(2) 只服务没有 themes 字段的历史页。
        _has_decl = re.search(r'^themes:', content, re.M) is not None
        _declared = _parse_list_field(content, 'themes')
        if _has_decl:
            theme_set = set()
            for _t in th.normalize_tags(_declared):
                _tid = th.THEME_TAG_ALIASES.get(_t)
                if _tid:
                    theme_set.add(_tid)
            theme_set = th.filter_supported_themes(theme_set, _theme_text)
            basis = 'declared'
        else:
            theme_set, basis = th.assign_themes(tags, _theme_text)
            theme_set = th.filter_supported_themes(theme_set, _theme_text)

        out.append({
            'primary_species': primary,
            'id': fname[:-3],
            'claim': claim,
            'title': title,
            'tags': th.normalize_tags(tags),
            'species': [s for s in species if s],
            'genes': [g for g in genes if g],
            'compounds': [c for c in compounds if c],
            'doi': doi,
            'pmid': pmid,
            'evidence_type': ev_type,
            'quality': quality,
            'source': source,
            'themes': theme_set,
            'theme_basis': basis,
        })
    return out


# 导入层被拦下的非植物证据（供日志与审计，不静默丢弃）
NONPLANT_DROPPED = []

# ── 领域判定：实现已迁到 organism_scope.py（2026-11-02 第 24 轮）──────
# 此前主题层与导入层各有一套词表，同一篇论文在两层得到不同结论
# （实测一致率仅 51/97），于是"导入层放进来、主题层再丢"变成静默丢数据。
# 现在两边共用 organism_scope：导入层写盘前判一次、主题层按 DOI 查同一张表。
_PAPER_ORG = None


def load_paper_organism():
    """DOI -> {'label','method','species','title'}；进程内缓存一次全库扫描。"""
    global _PAPER_ORG
    if _PAPER_ORG is None:
        _PAPER_ORG = paper_scope_table(CONCEPTS_DIR)
    return _PAPER_ORG


def paper_organism(doi):
    rec = load_paper_organism().get((doi or "").lower())
    return rec["label"] if rec else "unknown"


def paper_is_method(doi):
    """通用方法学论文（概念页标 methods-tools）——即便演示数据来自动物，
    方法本身对植物研究可用，允许只进 methods-tools 主题。"""
    rec = load_paper_organism().get((doi or "").lower())
    return bool(rec and rec.get("method"))


def paper_is_nonarticle(doi):
    """更正/撤稿/社论/勘误等（article_kind 不在 research/review 内）。

    这类页面没有可迁移的方法，因此 **不能** 享受 methods-tools 豁免。
    上一版只在 `is_nonplant()` 里把它归入 nonplant，而 group_by_theme 的
    method 豁免分支在此之后生效，于是“某方法学论文的勘误”仍会漏进
    methods-tools，与 batch_synthesis 的结论分叉。
    """
    rec = load_paper_organism().get((doi or "").lower())
    if not rec:
        return False
    return (rec.get("article_kind") or "research") not in ("research", "review")


def is_nonplant(ev):
    """该证据是否属于非植物研究。论文级优先，判不了才退回证据级。"""
    verdict, _reason = evidence_verdict(ev, load_paper_organism())
    # 'nonarticle'（更正/撤稿/社论/勘误）与 'nonplant' 一样不得进入假说层：
    # 二者都不是"可作为机制依据的研究证据"。
    return verdict in ('nonplant', 'nonarticle')


def group_by_theme(evidence):
    """按主题分组；一个证据进 >2 个主题视为泛化证据并丢弃。

    领域纯度与“能不能进这个主题”统一交给
    organism_scope.evidence_in_theme（2026-11-03），与 batch_synthesis、
    rebuild_synthesis_body 共用同一份规则。之前这里单独维护
    “org==nonplant 则看 method 标记”的分支，与综述层口径不一致，
    methods-tools 的证据数在两层不同。
    """
    groups = defaultdict(list)
    dropped = 0
    scope = load_paper_organism()
    for ev in evidence:
        tset = ev['themes']
        if len(tset) > th.MAX_THEMES_PER_EVIDENCE:
            dropped += 1
            continue
        kept_any = False
        for t in tset:
            ok, _verdict, _why = evidence_in_theme(ev, t, scope)
            if ok:
                groups[t].append(ev)
                kept_any = True
        if not kept_any:
            NONPLANT_DROPPED.append(ev['id'])
    return groups, dropped


# ============================================================
# 实体与关系抽取
# ============================================================
def is_gene_symbol(token):
    """判定是否为可信基因符号。"""
    if not token:
        return False
    t = re.sub(r'[^A-Za-z0-9\-]', '', token)
    if len(t) < 2 or len(t) > 12:
        return False
    up = t.upper().replace('-', '')
    if up in NON_GENE:
        return False
    if up.isdigit():
        return False
    # 图表/补充材料编号常被误当基因：S2、C1、A1、B3、F2 …
    # 真基因极少只有 1–2 个字母 + 1–2 个数字，宁可漏标不要误标。
    if re.match(r'^[A-Z]{1,2}\d{1,2}$', up):
        return False
    # 必须有数字（ARR1 / YUC4 / GATA6 / BZR1）或全大写 >=3 且不是英文词
    has_digit = any(c.isdigit() for c in t)
    all_upper = t.isupper() and len(t) >= 3
    if not (has_digit or all_upper):
        return False
    # 纯英文全大写且长度>=4 的常见词（含元音交替）仍可能是缩写，保守拒绝
    if all_upper and not has_digit and len(t) >= 5:
        return False
    return True


def candidate_genes(ev):
    """优先用证据页 genes 字段；其次从 claim 严格正则挖掘，再交叉校验。"""
    out = []
    for g in ev.get('genes') or []:
        # 支持 "Mdα-GP2" / "AtWRKY33" 这类带前缀写法
        base = g.split('/')[0].strip()
        if (is_gene_symbol(base)
                and base.upper().replace('-', '') not in ANIMAL_GENES
                and base.upper() not in NON_GENE
                and not any(p in base.lower() for p in PROCESS_NOUNS[:3])):
            out.append(base)
    if not out:
        claim = ev['claim']
        label_spans = [(m.start(), m.end()) for m in re.finditer(
            r'(?:Table|Fig\.?|Figure|Supplementary\s+Table|Supplementary\s+Fig\.?)\s*S?\d+',
            claim, re.I)]
        for m in re.finditer(r'\b([A-Z][A-Za-z]{0,4}\d{1,3}[A-Z]?)\b', claim):
            tok = m.group(1)
            if any(a <= m.start() < b for a, b in label_spans):
                continue
            if (is_gene_symbol(tok)
                    and tok.upper().replace('-', '') not in ANIMAL_GENES):
                out.append(tok)
    seen, uniq = set(), []
    for g in out:
        k = g.upper()
        if k not in seen:
            seen.add(k)
            uniq.append(g)
    return uniq[:4]


def candidate_objects(ev):
    """过程名词：用于"X 影响 Y"里的 Y。直接从证据自身字段与正文取。"""
    out = []
    for c in ev.get('compounds') or []:
        if c and c.lower() not in ('', 'none'):
            out.append(c)
    low = normalize_claim(ev['claim']).lower()
    for p in PROCESS_NOUNS:
        if re.search(r'\b' + re.escape(p) + r'\b', low):
            out.append(p)
    # 结构化名词短语：<adj>? <noun> (biosynthesis|accumulation|elongation|...)
    for m in re.finditer(
            r'\b((?:[a-z\-]+\s+){0,2}(?:biosynthesis|accumulation|elongation|'
            r'formation|development|growth|differentiation|expression|'
            r'formation|localization|transport|signaling|responses?))\b', low):
        phrase = m.group(1).strip()
        if 3 <= len(phrase) <= 60:
            out.append(phrase)
    seen, uniq = set(), []
    for o in out:
        cleaned = clean_object(o) or ''
        if len(cleaned.split()) < 2 and o in PROCESS_NOUNS:
            cleaned = o  # 单词过程名词（flowering）本身可用
        k = cleaned.lower()
        if cleaned and k not in seen:
            seen.add(k)
            uniq.append(cleaned)
    return uniq[:6]


_PRECEDING_BLOCKERS = frozenset('''
of by for to on in with via through from into onto than as at
repression overexpression knockdown knockout mutation loss gain
regulation expression activation inhibition induction reduction
antagonizes antagonize blocks block attenuates attenuate prevents
prevent disrupts disrupt competes compete suppresses suppress inhibits
inhibit represses repress activates activate induces induce enhances
enhance promotes promote increases increase decreases decrease
'''.split())

# 宾语尾部常见截断残渣
_TAIL_STOP = frozenset('''
under over during caused causing resulting leading thereby versus
compared relative due respectively including such also
'''.split())

_REL_ADV = (r'(?:\s*,\s*|\s+)'
            r'(?:(?:also|directly|positively|negatively|specifically|'
            r'strongly|dramatically|significantly|further|thereby|'
            r'consequently|mutually)\s+){0,3}')

_POS_VERB = (r'(?:promotes?|promoted|enhances?|enhanced|induces?|induced|'
             r'activates?|activated|increases?|increased|up-?regulates?|'
             r'up-?regulated|drives?|drove|stimulates?|stimulated)')
_NEG_VERB = (r'(?:inhibits?|inhibited|represses?|repressed|suppress(?:es|ed)?|'
             r'reduces?|reduced|decreases?|decreased|down-?regulates?|'
             r'down-?regulated|blocks?|blocked|prevents?|prevented|'
             r'attenuates?|attenuated|restricts?|restricted)')

# 句首"报道框架"剥离：综述/摘要里几乎都写成
# "Taken together, these results suggest that <真正的断言>"。
_META_LEAD = [
    r'^(?:taken\s+together|collectively|together|overall|in\s+summary|'
    r'in\s+conclusion|in\s+short|in\s+brief|thus|therefore|hence|'
    r'accordingly|moreover|furthermore|however|nevertheless|nonetheless|'
    r'importantly|notably|interestingly|consequently|'
    r'consistent\s+with\s+(?:these|this|previous)\s+\w+)[,:]?\s+',
    r'^(?:these|our|the|such|those)\s+(?:results?|data|findings?|analyses|'
    r'experiments?|observations?|studies|work|evidence)\s*',
    r'^(?:suggest|suggests|suggested|show|shows|showed|shown|indicate|'
    r'indicates|indicated|demonstrate|demonstrates|demonstrated|reveal|'
    r'reveals|revealed|found|find|report|reported|propose|proposed|'
    r'hypothesi[sz]e|hypothesi[sz]ed|conclude|concluded|confirm|confirmed)\s*',
    r'^(?:that|which|it\s+(?:is|was)\s+(?:shown|found|demonstrated|reported))\s+',
    r'^(?:we|here\s+we|i)\s+(?:found|show|showed|shown|report|reported|'
    r'demonstrate|demonstrated|reveal|revealed|observe|observed|propose|'
    r'proposed|conclude|concluded|identified|identify|provide)\s*',
    r'^[:;,\-–—]+\s*',
]

_MANI_GOF = ('overexpression', 'over-expression', 'over expression',
             'ectopic expression', 'constitutive expression',
             'gain-of-function', 'gain of function', 'complementation')
_MANI_LOF = ('knockdown', 'knock-down', 'knockout', 'knock-out', 'silencing',
             'rna-i', 'rnai', 'suppression', 'mutation', 'deletion',
             'loss-of-function', 'loss of function', 'repression')
_MANI_RE = (r'(?:over-?expression|ectopic\s+expression|constitutive\s+'
            r'expression|knock-?down|knock-?out|silencing|rna-?i|'
            r'suppression|mutation|deletion|loss-?of-?function|'
            r'gain-?of-?function|complementation)')


def _strip_meta(text):
    """循环剥掉报道框架（"These data suggest that ..."），最多 5 层。"""
    cur = text.strip()
    for _ in range(5):
        before = cur
        for pat in _META_LEAD:
            m = re.match(pat, cur, re.I)
            if m and m.end() > 0:
                cur = cur[m.end():].lstrip()
                break
        if cur == before:
            break
    return cur


def _subject_positions(text):
    """返回 (start, end, symbol)，仅保留"不是前一个动词/介词的宾语"的候选。"""
    out = []
    for m in re.finditer(r'\b([A-Za-z\u03b1-\u03c9][A-Za-z0-9\u03b1-\u03c9\-]{1,14})\b',
                         text):
        sym = m.group(1)
        if not is_gene_symbol(sym):
            continue
        if sym.upper().replace('-', '') in ANIMAL_GENES:
            continue
        prev = text[:m.start()].rstrip()
        prev_word = re.search(r'([A-Za-z]+)$', prev)
        if prev_word and prev_word.group(1).lower() in _PRECEDING_BLOCKERS:
            continue
        out.append((m.start(), m.end(), sym))
    return out


def _sv_patterns(adv):
    """主语之后的"动词 + 宾语"骨架；宾语上限 70 字符。"""
    return (
        ('positive', r'^' + adv + _POS_VERB + r'\b\s+(.{3,70})'),
        ('negative', r'^' + adv + _NEG_VERB + r'\b\s+(.{3,70})'),
        ('reg', r'^' + adv + r'(?:is|was|are|were)\s+(?:a\s+|an\s+)?'
                r'(positive|negative)\s+(?:regulator|modulator|mediator)\s+of\s+(.{3,70})'),
        ('req', r'^' + adv + r'(?:is|was|are|were)\s+(?:required|essential|'
                r'necessary)\s+for\s+(.{3,70})'),
    )


def _match_after(rest, adv):
    """在 rest 中匹配骨架，返回 (polarity, object) 或 None。"""
    for kind, pat in _sv_patterns(adv):
        m = re.search(pat, rest, re.I)
        if not m:
            continue
        if kind == 'reg':
            obj = clean_object(m.group(2))
            pol = 'positive' if m.group(1).lower() == 'positive' else 'negative'
        else:
            obj = clean_object(m.group(1))
            pol = 'positive' if kind in ('positive', 'req') else 'negative'
        if obj:
            return pol, obj
    return None


def _mutation_polarity(mani, verb_pol):
    """过表达→方向同向；敲低/敲除/沉默→方向反转；无法识别→保持原方向。

    早期实现在"既不是 GOF 也没识别出 LOF"时也做反转，等于把
    "treatment with X up-regulates Y" 读成"处理会降低 Y"。
    现在只有明确命中 LOF 词表才反转。
    """
    low = re.sub(r'[\s\-]+', ' ', mani.lower()).strip()
    norm = lambda s: re.sub(r'[\s\-]+', ' ', s.lower()).strip()
    if not low:
        return verb_pol
    if low in {norm(g) for g in _MANI_GOF}:
        return verb_pol
    if low in {norm(g) for g in _MANI_LOF}:
        return 'negative' if verb_pol == 'positive' else 'positive'
    return verb_pol


_PASSIVE_POS = (r'(?:activated|induced|enhanced|up-?regulated|promoted|'
                r'stabilized|stimulated)')
_PASSIVE_NEG = (r'(?:repressed|inhibited|suppressed|down-?regulated|'
                r'destabilized|blocked)')


def extract_relation(claim):
    """从 claim 抽 (subject, polarity, object_phrase)。

    处理四类真实句式（综述/摘要的高频写法）：
      1. "Taken together, these results suggest that S V O"
      2. "Overexpression | knockdown | knockout of X V O"（按扰动类型翻转方向）
      3. "O (is|was) repressed|activated by S"（被动语态）
      4. "S V O"（主语在句首或 that 之后，动词与主语紧邻）

    主语前若是 of/by/repression/antagonizes 等，视为宾语而非主语，
    以免把 "repression of BIN2 by BSU1" 读成 "BIN2 正向调控"。
    抽不到时返回 (None, None, '')，由调用方降级为关联型假说。
    """
    text = normalize_claim(claim)
    if not text:
        return None, None, ''
    core = _strip_meta(text)
    adv = _REL_ADV

    # ---- 被动语态：O is repressed|activated by S ----
    for pol, verbs in (('negative', _PASSIVE_NEG), ('positive', _PASSIVE_POS)):
        m = re.search(r'^(.{3,70}?)\s+(?:is|was|are|were)\s+' + adv +
                      verbs + r'\s+by\s+([A-Za-z\u03b1-\u03c9]'
                      r'[A-Za-z0-9\u03b1-\u03c9\-]{1,14})\b', core, re.I)
        if m:
            obj = clean_object(m.group(1))
            if obj and is_gene_symbol(m.group(2)) and \
                    m.group(2).upper().replace('-', '') not in ANIMAL_GENES:
                return m.group(2), pol, obj

    # ---- 扰动句式：Overexpression / knockdown of X V O ----
    m = re.search(r'^(?:the\s+)?(' + _MANI_RE + r')\s+of\s+'
                  r'([A-Za-z\u03b1-\u03c9][A-Za-z0-9\u03b1-\u03c9\-]{1,14})\b'
                  r'(.*)$', core, re.I)
    if m:
        mani, sym, rest = m.group(1), m.group(2), m.group(3)
        if is_gene_symbol(sym) and sym.upper().replace('-', '') not in ANIMAL_GENES:
            hit = _match_after(rest, adv)
            if hit:
                return sym, _mutation_polarity(mani, hit[0]), hit[1]

    # ---- 主动句式：S（可带前置状语）V O ----
    for start, end, sym in _subject_positions(core):
        hit = _match_after(core[end:], adv)
        if hit:
            return sym, hit[0], hit[1]
    return None, None, ''


FUNCTION_WORDS = frozenset('''
a an the this that these those each every either neither both all any some no
none another other others such what which whichever who whom whose whatever
i you he she it we they me him her us them my your his its our their mine yours
and or but nor so yet for because since as if unless until while whereas although
though even when whenever where wherever whether after before once than then
thus hence therefore however moreover furthermore besides also too very just only
even still already always never often sometimes usually rather quite almost
about above across after against along among around at before behind below
beneath beside between beyond by despite down during except for from in inside
into like near of off on onto out outside over past per regarding round since
through throughout till to toward towards under underneath unlike until up upon
via with within without
is are was were be been being am do does did done doing have has had having
will would shall should may might must can could not
here there now ago else otherwise instead perhaps maybe indeed actually
process processes aspect aspects factor factors feature features component
components element elements part parts subset sets set number numbers
'''.split())


def _first_is_content(word):
    w = (word or '').strip(',;:()[]"').lower()
    if not w:
        return False
    if w in FUNCTION_WORDS:
        return False
    if len(w) <= 2 and not w.isupper():
        return False
    return True

SOFT_HYPHEN_CHARS = ('\u00ad', '\u2010', '\u2011', '\u00a0')


def normalize_claim(text):
    """清理 PDF 抽取噪声：软连字符断词、连字、弯引号、多余空白。

    "develop<U+00AD> ment" / "chro- mosome" 一律拼回一个词；
    这是文献库里最常见的脏数据形态，不清理会直接污染假说主语/宾语。
    """
    if not text:
        return ''
    t = text
    # 软连字符后紧跟空格 → 是换行断词，直接拼接
    t = re.sub(r'([A-Za-z])\u00ad\s*([a-z])', r'\1\2', t)
    for ch in SOFT_HYPHEN_CHARS:
        t = t.replace(ch, ' ')
    # 普通连字符 + 空格 + 小写续词 → 判定为换行断词
    t = re.sub(r'\b([a-z]{3,})-\s+([a-z]{2,})\b', r'\1-\2', t)
    t = re.sub(r'\b([A-Za-z]{3,})-\s+([A-Z]{3,})\b', r'\1\2', t)
    t = t.replace('\u2019', "'").replace('\u2018', "'")
    t = t.replace('\u201c', '"').replace('\u201d', '"')
    t = t.replace('\ufb01', 'fi').replace('\ufb02', 'fl')
    t = ' '.join(t.split())
    # PDF 分栏/页眉重复造成的连续重复词："Arabidopsis Arabidopsis lines"
    for _ in range(3):
        t2 = re.sub(r'\b([A-Za-z][A-Za-z\-]{2,})\s+\1\b', r'\1', t)
        if t2 == t:
            break
        t = t2
    return t


# ── PDF 分栏行号清理（保守，只影响生成的假说页，不改写证据原文）───────────
# 两栏 PDF 抽取会在句子中间插入行号："In summary, 179 cadmium stress ... overall
# 180 impairment ..."。判定为行号的三个必要条件（缺一不可）：
#   1) 恰好 3 位数字，两侧均为空格，右侧紧跟小写单词；
#   2) 右侧单词不是可被计数的名词/单位（genes、cells、mM…）；
#   3) 左侧不是 of/at/approximately/to 这类"取值引导词"。
# 命中率低但精确；宁可保留少量行号，也不删掉真实的计量数值。
_LINE_NO = re.compile(r'(?<=[A-Za-z,;:] )\d{3}(?= [a-z])')
_LINE_NO_KEEP = re.compile(
    r'^(genes?|proteins?|transcripts?|sequences?|contigs?|scaffolds?|cells?|clusters?|'
    r'samples?|accessions?|SNPs?|QTLs?|metabolites?|compounds?|families|members?|species|'
    r'lines?|cultivars?|varieties|replicates?|reads?|DEGs?|modules?|pathways?|types?|'
    r'stages?|sites?|positions?|bases?|nucleotides?|residues?|pairs?|targets?|landmarks?|'
    r'bp|aa|kDa|mM|nM|mg|g|kg|mL|d|h|min|s)\b')
_LINE_NO_PRE = re.compile(
    r'(?:\bof|\bat|\bvalue|approximately|about|around|range|between|than|\bto)\s*$', re.I)


def strip_line_numbers(text):
    if not text:
        return text
    def _rep(m):
        if _LINE_NO_KEEP.match(text[m.end() + 1:m.end() + 14]):
            return m.group(0)
        if _LINE_NO_PRE.search(text[:m.start()]):
            return m.group(0)
        return ''
    t2 = _LINE_NO.sub(_rep, text)
    return ' '.join(t2.split()) if t2 != text else text


NOUN_HEADS = frozenset('''
development growth elongation differentiation formation biosynthesis accumulation
expression abundance transport localization signalling signaling response responses
tolerance resistance susceptibility yield biomass length number density activity
content level levels flowering senescence germination emergence rooting architecture
branching tillering height width area weight quality vigour vigor fertility
maturation regeneration proliferation expansion division migration patterning
'''.split())

ADVERBS = frozenset('''
positively negatively significantly markedly strongly greatly substantially
dramatically slightly moderately severely mildly rapidly slowly transiently
constitutively ectopically notably remarkably consistently
'''.split())

_LEADING_VERB_RE = re.compile(
    r'^(?:regulat|promot|enhanc|induc|activat|increas|inhibit|repress|suppress|'
    r'reduc|decreas|modulat|mediat|control|affect)\w*$')


def clean_object(obj):
    """把抽取到的宾语清洗为可信名词短语；不可信则返回空串（宁缺勿滥）。"""
    if not obj:
        return ''
    s = normalize_claim(obj)
    s = re.split(r'[.;,]|\b(?:by|via|through|which|that|whereas|while|'
                 r'resulting|leading)\b', s)[0]
    words = [w for w in s.split() if w]
    while words and words[-1].lower().strip(',;:') in ADVERBS:
        words.pop()
    # 尾随介词/连词是抽取截断的残渣："maize root growth under" /
    # "tolerance to sheath blight caused"
    while words and (words[-1].lower().strip(',;:') in FUNCTION_WORDS
                     or words[-1].lower().strip(',;:') in _TAIL_STOP):
        words.pop()
    while words and not _first_is_content(words[0]):
        words.pop(0)
    words = [w for w in words if w.lower().strip(',;:') not in ADVERBS]
    s = ' '.join(words).strip(' ,;:')
    if not s or len(s) < 5 or len(s.split()) > 7:
        return ''
    low = s.lower()
    if re.search(r'\b(?:fig|figure|table|supplementary|lane|panel)\b', low):
        return ''
    if s.count('(') != s.count(')'):
        return ''
    if re.search(r'\bet\s+al\b', low):
        return ''
    if _LEADING_VERB_RE.match(low.split()[0] if low.split() else ''):
        return ''
    heads = [h for h in NOUN_HEADS if re.search(r'\b' + h + r'\b', low)]
    if not heads:
        return ''
    # 单一泛化中心词（"development"）没有信息量，要求至少 2 个词
    if len(s.split()) < 2:
        return ''
    # 不能残留另一个动词（方向已由 polarity 表达）
    if re.search(r'\b(?:' + POS_VERBS + '|' + NEG_VERBS + r')\b', low):
        return ''
    return s[:70]


# ============================================================
# 聚类
# ============================================================
STOP = frozenset('''
the and for with from that this these those have has been were was are is of in
on to by as at or not also more than such which while both into after more less
we our here show shown results result revealed found using used can may suggest
suggesting indicating consistent contrast however moreover additionally thus
'''.split())


def tokens(text):
    return {w for w in re.findall(r'[a-z][a-z\-]{3,}', (text or '').lower())
            if w not in STOP}


def _anchors(ev):
    """返回 (genes, procs)：聚类用的"生物实体锚点"。

    为什么不用词袋 Jaccard：不同论文表述同一条结论时措辞差异极大
    （"BZR1 promotes cell elongation" vs "brassinosteroid signalling
    enhances hypocotyl growth"），词袋相似度常 <0.05，会把同一机制
    的证据拆成单条，导致"证据簇不足"而无法生成假说。
    同一基因/同一代谢物才是"同一个机制"的可靠锚点。
    """
    genes = {g.upper() for g in candidate_genes(ev)}
    procs = set()
    low = ev['claim'].lower()
    for p in PROCESS_NOUNS:
        if p in low:
            procs.add(p)
    for c in ev.get('compounds') or []:
        c = c.strip().lower()
        if c and c not in ('none', 'unknown'):
            procs.add(c)
    return genes, procs


def _ngrams(text, n=3):
    words = re.findall(r'[a-z0-9\-]+', (text or '').lower())
    return {tuple(words[i:i + n]) for i in range(max(0, len(words) - n + 1))}


# 论文里高频出现但与生物学无关的套话：抽到它们做假说主语毫无意义。
BOILERPLATE = frozenset("""
the of and in to with for by as at on from that this these those we our
figure fig table supplementary data shown show result results study studies
were was are is has have had been being here also such than which while both
significantly significant respectively identified identify detected observed
reported suggest suggests suggested indicate indicates indicated however
moreover additionally thus therefore between among using used can may could
not no all any each other others well might must shall will would
""".split())

JUNK_SUBSTRINGS = (
    'as shown in', 'in the', 'of the', 'was identi', 'were identi',
    'data not shown', 'et al', 'p <', 'p =', 'according to',
    'in this study', 'in contrast', 'taken together', 'these results',
    'our results', 'of apa',
)


def _phrase_ok(phrase):
    """真短语判定：无套话、>=2 个内容词、至少 1 个 >=5 字母的实词。"""
    if not phrase:
        return False
    low = ' '.join(phrase.lower().split())
    if any(j in low for j in JUNK_SUBSTRINGS):
        return False
    words = [w for w in low.split() if w]
    if len(words) < 3:
        return False
    content = [w for w in words if w not in BOILERPLATE and len(w) >= 4]
    if len(content) < 2:
        return False
    if not any(len(w) >= 5 and not w.isdigit() for w in content):
        return False
    # 首尾须是内容词，避免 "of ... the" 这类残句
    if words[0] in BOILERPLATE or words[-1] in BOILERPLATE:
        return False
    return True


def common_phrase(claims, min_words=4, max_words=8):
    """取簇内多数断言共有的最长词序列，并过滤论文套话。

    短语逐字来自证据正文，因此最坏情况是"不够精确"，不会是幻觉；
    过滤 figure/table/et al 一类套话，避免生成
    "as shown in figure regulates [process]" 这种垃圾。
    """
    if len(claims) < 2:
        return ''
    counts = Counter()
    for c in claims[:40]:
        words = re.findall(r'[A-Za-z0-9\-]+', c)
        seen = set()
        for n in range(min_words, min(max_words, len(words)) + 1):
            for i in range(len(words) - n + 1):
                seen.add(' '.join(words[i:i + n]).lower())
        counts.update(seen)
    need = max(2, int(len(claims) * 0.5 + 0.5))
    cands = [p for p, v in counts.items()
             if v >= need and len(p.split()) >= min_words and _phrase_ok(p)]
    if not cands:
        return ''
    return max(cands, key=lambda p: (len(p.split()), -len(p)))


def cluster_subject(cluster, theme_id):
    """为证据簇选主语：基因 > 主题术语 > 共有短语 > 无。

    主题术语取自 themes.THEME_KEYWORDS，且必须逐字出现在证据里，
    这样方法学/演化类主题能得到具体主语（benchmark / polyploid …），
    而不是被迫编一个不存在的基因名。
    """
    genes = Counter()
    for ev in cluster:
        for g in candidate_genes(ev):
            genes[g] += 1
    if genes:
        return genes.most_common(1)[0][0], 'gene'

    text = ' '.join(e['claim'].lower() for e in cluster)
    terms = Counter()
    for kw in list(th.THEME_KEYWORDS.get(theme_id, [])) + list(PROCESS_NOUNS):
        c = text.count(kw.lower())
        if c >= 2:
            terms[kw] += c
    if terms:
        return terms.most_common(1)[0][0], 'term'

    phrase = common_phrase([e['claim'] for e in cluster])
    if _phrase_ok(phrase):
        return phrase, 'phrase'
    return '', None


def _ngram_clusters(items, min_size, max_groups=12):
    """词 3-gram 贪心聚类（兜底无基因/无代谢物锚点的主题）。

    先一次性算好重叠矩阵（O(n^2) 次集合交），再贪心取稠密点分组，
    避免旧写法每轮重算导致的 O(n^3)（343 条证据时直接卡死）。
    """
    grams = [_ngrams(e['claim']) for e in items]
    n = len(grams)
    adj = [set() for _ in range(n)]
    for i in range(n):
        gi = grams[i]
        if not gi:
            continue
        for j in range(i + 1, n):
            if len(gi & grams[j]) >= 2:
                adj[i].add(j)
                adj[j].add(i)

    remaining = set(range(n))
    out = []
    while remaining and len(out) < max_groups:
        seed = max(remaining, key=lambda i: (len(adj[i] & remaining), i))
        group = [seed] + sorted(adj[seed] & remaining)
        if len(group) < min_size:
            # 旧写法在这里 break，导致"最稠密点不成簇"时后面全部丢弃
            # （methods-tools 78 条证据只出 1 个 4 条簇的直接原因）。
            remaining.discard(seed)
            continue
        out.append([items[i] for i in group])
        remaining -= set(group)
    out.sort(key=len, reverse=True)
    return out


def cluster_evidence(items, min_size=MIN_EVIDENCE_PER_HYPOTHESIS):
    """两段式聚类：实体锚点优先，词序列兜底。

    1) 共享基因符号 → 合并（强锚点：同一调控因子）；
    2) 共享"具体"过程锚点（本主题内出现 3~25%）→ 合并；
    3) 仍未成簇的剩余条目，用 3-gram 相似度兜底；
    4) 孤立证据一律不成簇 —— 宁可不生成假说，也不拿 1 条证据编故事。
    """
    n = len(items)
    if n < min_size:
        return []

    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    gene_idx = defaultdict(list)
    proc_idx = defaultdict(list)
    for i, ev in enumerate(items):
        genes, procs = _anchors(ev)
        for g in genes:
            gene_idx[g].append(i)
        for p in procs:
            proc_idx[p].append(i)

    for g, idx in gene_idx.items():
        for j in idx[1:]:
            union(idx[0], j)

    lo, hi = 3, max(4, int(n * 0.25))
    for p, idx in proc_idx.items():
        if lo <= len(idx) <= hi:
            for j in idx[1:]:
                union(idx[0], j)

    comp = defaultdict(list)
    for i in range(n):
        comp[find(i)].append(i)

    clusters, leftovers = [], []
    for k in comp:
        evs = [items[i] for i in comp[k]]
        (clusters if len(evs) >= min_size else leftovers).append(evs)

    # 词序列兜底：只处理未成簇的散点
    flat = [e for grp in leftovers for e in grp]
    if len(flat) >= min_size:
        clusters.extend(_ngram_clusters(flat, min_size))

    # 过大的分量按主导基因再拆（避免"整个主题一个大簇"）
    out = []
    for evs in clusters:
        if len(evs) <= 40:
            out.append(evs)
            continue
        by_gene = defaultdict(list)
        rest = []
        for e in evs:
            gs, _ = _anchors(e)
            if gs:
                by_gene[sorted(gs)[0]].append(e)
            else:
                rest.append(e)
        for g in sorted(by_gene, key=lambda k: -len(by_gene[k])):
            if len(by_gene[g]) >= min_size:
                out.append(by_gene[g])
            else:
                rest.extend(by_gene[g])
        if len(rest) >= min_size:
            out.append(rest)

    out.sort(key=len, reverse=True)
    return [c for c in out if len(c) >= min_size]


def paper_key(ev):
    return ev.get('pmid') or ev.get('doi') or ev.get('source') or ev['id']


# ============================================================
# 假说构造
# ============================================================
def _top(counter, n=3):
    return [k for k, _ in counter.most_common(n) if k]


MIN_SPECIES_CONSENSUS = 0.6


def resolve_species(cluster, target=''):
    """裁决这条假说属于哪个物种；证据不一致时返回空串（不硬派物种）。

    只用 primary_species 优先、物种列表兜底，并要求占主导（>=60%）；
    旧版直接取众数，会把"论文同时涉及 3 个物种"错判为单一物种。
    """
    pool = [e for e in cluster
            if target and target in (e.get('genes') or [])] or list(cluster)
    c = Counter()
    for e in pool:
        prim = (e.get('primary_species') or '').strip()
        if prim in GENERIC_SPECIES:
            prim = ''
        cand = ([prim] if prim else
                [x for x in (e.get('species') or [])
                 if x and x not in GENERIC_SPECIES])
        for s in cand:
            c[s] += 1
    if not c:
        return ''
    top, n = c.most_common(1)[0]
    if len(pool) >= 2 and n < max(1, MIN_SPECIES_CONSENSUS * len(pool)):
        return ''
    if len(c) > 2:
        return ''
    return top


def _claim_relevance(claim, target, obj):
    """断言与假说的相关性：命中靶标计 3 分，命中宾语内容词各计 1 分。"""
    score = 0
    if target and re.search(r'\b' + re.escape(target) + r'\b', claim, re.I):
        score += 3
    toks = tokens(claim)
    for w in (obj or '').lower().split():
        if len(w) >= 4 and w in toks:
            score += 1
    return score


# ============================================================
# 基因家族 → 判别性实验设计
# 同一个"必要性未检验"的缺口，落到不同蛋白家族上，
# 需要的实验读数完全不同：TF 要区分结合与支架，激酶要区分催化活性，
# 组蛋白修饰酶要检测修饰位点，泛素连接酶要检测底物稳定性。
# 这样每条假说都给出可执行的差异化检验，而不是同一句模板。
# ============================================================

_GENE_CLASSES = (
    (r'^(VND|SND|ANAC|NAC|NAM)\d*$', 'NAC 家族转录因子',
     '构建 DNA 结合域缺陷突变体，区分“转录激活”与“蛋白支架”作用，'
     '并对直接靶基因做 ChIP-qPCR 与表达检测',
     'DNA 结合缺陷突变体不能回补表型，且直接靶基因表达不发生相应改变'),
    (r'^MYB\d*\w*$', 'MYB 类转录因子',
     '用 MYB 结构域点突变体配合靶启动子 EMSA/ChIP，判定是否为直接转录调控',
     'MYB 结构域突变体丧失结合能力后不再改变靶基因表达'),
    (r'^(WRKY)\d*\w*$', 'WRKY 转录因子',
     '以 W-box 结合缺陷突变体配合靶基因表达与染色质占据检测，判定直接性',
     'W-box 结合缺陷突变体不能回补表型'),
    (r'^(ERF|WIND|AP2|DREB|ERF)\d*\w*$', 'AP2/ERF 类转录因子',
     '用 AP2 结构域突变体配合 GCC/DRE 元件报告系统，判定直接转录调控',
     'AP2 结构域突变体丧失回补能力'),
    (r'^(ARF|IAA)\d*\w*$', 'ARF/Aux-IAA 生长素响应因子',
     '以 DNA 结合缺陷 ARF 突变体配合生长素响应报告系（DR5）检测',
     'DNA 结合缺陷突变体不再改变生长素响应输出'),
    (r'^SPL\d*\w*$', 'SPL 转录因子',
     '用 SBP 结构域突变体配合靶基因表达检测，并检验 miR156 调控层级是否必需',
     'SBP 结构域突变体不能回补表型'),
    (r'^(HDA|HDAC|HST|SRT)\d*\w*$', '组蛋白去乙酰化酶',
     '构建催化死（HDA 结构域）突变体，比较蛋白水平与靶位点 H3K9ac/H4K16ac 变化',
     '催化死突变体蛋白稳定但不回补表型，靶位点乙酰化水平不下降'),
    (r'^(GCN5|HAG|HAC)\d*\w*$', '组蛋白乙酰转移酶',
     '构建乙酰转移酶催化死突变体，检测靶位点 H3K9ac 与转录变化',
     '催化死突变体不回补表型且靶位点乙酰化不升高'),
    (r'^(SDG|SUVH|SUVR|CLF|SWN|ATX|JMJ|LHP1)\d*\w*$',
     '组蛋白甲基转移酶/去甲基化酶或 Polycomb 组分',
     '用催化死突变体配合 H3K4me3/H3K27me3 ChIP，判定修饰活性是否为必需',
     '催化死突变体不回补表型，且靶位点组蛋白修饰不改变'),
    (r'^(SKP|PSI?SKP|FBX|FBOX)\d*\w*$', 'SCF 泛素连接酶底物受体',
     '检测候选底物的蛋白稳定性与泛素化水平，并构建底物结合缺陷（F-box 突变）突变体',
     '底物结合缺陷突变体稳定底物却不改变表型，或表型由底物降解速率决定'),
    (r'^(BIN2|GSK\d*\w*|MPK\d*\w*|MAPK\d*\w*|CDPK|CPK\d*\w*|SnRK\w*|'
     r'CIPK\d*\w*|BIK1|BAK1|SERK\d*\w*|CLV1|FER|RLK\d*\w*)\d*$',
     '蛋白激酶或受体激酶',
     '用激酶死（K→E/M）突变体判定催化活性是否必需，并做磷酸化位点回补与'
     '配体/下游响应检测',
     '激酶死突变体不回补表型，而磷酸化位点回补可部分或完全恢复'),
    (r'^(CESA|CSL)\d*\w*$', '纤维素合酶',
     '用催化死突变体配合细胞壁组分定量（纤维素含量、结晶度）与同位素标记通量测定',
     '催化死突变体细胞壁纤维素含量不变，说明表型来自非催化功能'),
    (r'^(KCS|FAE|CER|PAS2)\d*\w*$', '脂肪酸延伸/蜡质合成酶',
     '用催化死突变体配合超长链脂肪酸与蜡质组分定量，判定酶活必需性',
     '催化死突变体不回补蜡质或 VLCFA 缺陷'),
    (r'^(CYP\w*|P450)$', '细胞色素 P450 单加氧酶',
     '体外重组酶活测定 + 底物喂养实验，判定其催化步骤在通路中的位置',
     '重组酶在体外不能转化推定底物，或底物喂养绕过该步骤'),
    (r'^GSNOR\d*\w*$', 'S-亚硝基谷胱甘肽还原酶',
     '测定 SNO 水平与蛋白亚硝基化程度，并用催化死突变体分离酶活与支架作用',
     '催化死突变体不回补表型且 SNO 水平不下降'),
    (r'^GST\w*$', '谷胱甘肽 S-转移酶',
     '比较底物结合与催化活性缺陷突变体，并测定细胞内底物/结合物比值',
     '催化缺陷突变体回补能力丧失，而底物结合缺陷体表型不变'),
    (r'^(PSY|PDS|PAL|CAD|CHS|CHI|F3H|DFR|ANS|UFGT|GT\d*)\w*$',
     '次生代谢通路关键酶',
     '用催化死突变体配合代谢物定量与同位素标记通量测定，定位限速步骤',
     '催化死突变体导致上游底物累积、下游产物缺失'),
    (r'^(TOC1|PRR\d*|CCA1|LHY|ELF\d*|GI|ZTL|FKF1)\w*$', '生物钟组分',
     '在恒温恒光/恒暗条件下测自由运行周期，并用节律相位回补实验判定功能',
     '突变体周期或相位改变，且只在特定光周期下产生表型差异'),
    (r'^ARR\d*\w*$', '双组分响应调节因子',
     '用磷酸化接受域（D→N）突变体分离磷酸化依赖与非依赖功能，并测下游响应基因',
     '磷酸化缺陷突变体不回补表型'),
    (r'^E2F\w*$', 'E2F 类转录因子',
     '用 DNA 结合缺陷与 RB 结合缺陷突变体分别判定转录激活与细胞周期调控',
     '两类突变体分别丧失不同子集的表型'),
)


# 常见物种前缀：At/Os/Ta/Md/Hv/Sl/... 剥掉后再判家族
_SPECIES_PREFIX = frozenset('''
AT OS TA MD HV SL GM ZM PP VV CM NT PBR POP PS PSI SI BN GH CU CS JR MI PG RC
HB EG DL MA PD PY SO SH TH TP RC PP
'''.split())


def _gene_class(sym):
    """按基因符号推断蛋白家族；推测不到时返回 ('', '')，不硬猜。"""
    u = (sym or '').upper().strip()
    if not u:
        return '', ''
    cands = [u]
    for n in (3, 2):
        if len(u) > n + 1 and u[:n] in _SPECIES_PREFIX:
            cands.append(u[n:])
    for pat, cls, test, pred in _GENE_CLASSES:
        for c in cands:
            try:
                if re.search(pat, c):
                    return cls, (test, pred)
            except re.error:
                break
    return '', ''



# --- 术语表：把英文过程名词统一为中文，避免中英混排与术语漂移 ---
_OBJECT_ZH = {
    'root growth': '根生长',
    'root elongation': '根伸长',
    'hypocotyl elongation': '下胚轴伸长',
    'hypocotyl growth': '下胚轴生长',
    'hormone responses': '激素响应',
    'hormone response': '激素响应',
    'auxin response': '生长素响应',
    'cytokinin response': '细胞分裂素响应',
    'cytokinin response genes': '细胞分裂素响应基因',
    'aba response': '脱落酸响应',
    'brassinosteroid signaling': '油菜素内酯信号',
    'defence response': '防御响应',
    'defense response': '防御响应',
    'pathogen resistance': '病原抗性',
    'drought tolerance': '耐旱性',
    'salt tolerance': '耐盐性',
    'seed germination': '种子萌发',
    'flowering time': '开花时间',
    'stomatal development': '气孔发育',
    'lateral root formation': '侧根形成',
    'lateral root development': '侧根发育',
    'cell elongation': '细胞伸长',
    'cell division': '细胞分裂',
    'programmed cell death': '程序性细胞死亡',
    'gene expression': '基因表达',
    'transcript accumulation': '转录本积累',
    'protein accumulation': '蛋白积累',
    'secondary cell wall biosynthesis': '次生细胞壁合成',
    'cell wall biosynthesis': '细胞壁合成',
    'lignin biosynthesis': '木质素合成',
    'anthocyanin accumulation': '花青素积累',
    'chlorophyll content': '叶绿素含量',
    'photosynthetic rate': '光合速率',
    'grain yield': '产量',
    'seed size': '种子大小',
    'fruit ripening': '果实成熟',
    'senescence': '衰老',
    'nodulation': '结瘤',
    'meristem activity': '分生组织活性',
    'shoot branching': '分枝',
    'trichome development': '表皮毛发育',
    'root architecture': '根系构型',
    'nitrogen use efficiency': '氮利用效率',
    'water use efficiency': '水分利用效率',
}

_MODIFIER_ZH = {
    'jasmonate': '茉莉酸', 'salicylate': '水杨酸', 'auxin': '生长素',
    'cytokinin': '细胞分裂素', 'abscisic acid': '脱落酸', 'aba': '脱落酸',
    'ethylene': '乙烯', 'brassinosteroid': '油菜素内酯', 'gibberellin': '赤霉素',
    'strigolactone': '独脚金内酯',
    'abiotic stress': '非生物胁迫', 'biotic stress': '生物胁迫',
    'flavonol': '黄酮醇', 'monolignol': '单木质醇', 'terpenoid': '萜类',
    'phenylpropanoid': '苯丙烷', 'glucosinolate': '硫苷',
    'cuticular wax': '角质层蜡质', 'seed oil': '种子油',
    'nitric oxide': '一氧化氮', 'reactive oxygen species': '活性氧', 'ros': '活性氧',
    'secondary metabolites': '次生代谢物', 'secondary metabolite': '次生代谢物',
    'phenolic': '酚类', 'flavonoid': '类黄酮', 'anthocyanin': '花青素',
    'lignin': '木质素', 'cellulose': '纤维素', 'starch': '淀粉',
    'sucrose': '蔗糖', 'sugar': '糖', 'nitrogen': '氮', 'phosphorus': '磷',
    'iron': '铁', 'cadmium': '镉', 'arsenic': '砷', 'salt': '盐', 'drought': '干旱',
    'cold': '低温', 'heat': '高温', 'pathogen': '病原', 'fungal': '真菌',
    'bacterial': '细菌', 'viral': '病毒', 'wound': '创伤', 'herbivory': '虫害',
    'seed': '种子', 'root': '根', 'shoot': '地上部', 'leaf': '叶',
    'hypocotyl': '下胚轴', 'pollen': '花粉', 'floral': '花', 'stomatal': '气孔',
    'trichome': '表皮毛', 'cell wall': '细胞壁', 'chloroplast': '叶绿体',
    # 2026-11-03：形容词/属性修饰词补齐，否则 "soluble sugars accumulation"
    # 这类常见过程名词会原样留在中文标题里（未翻译过程名词的回归测试失败）。
    'soluble': '可溶性', 'insoluble': '不可溶性', 'total': '总',
    'free': '游离', 'reducing': '还原性', 'stored': '储藏',
    'photosynthetic': '光合', 'antioxidant': '抗氧化', 'lipid': '脂质',
    'fatty acid': '脂肪酸', 'protein': '蛋白', 'amino acid': '氨基酸',
    'carotenoid': '类胡萝卜素', 'vitamin': '维生素', 'organic acid': '有机酸',
}

_GENERIC_HEAD_ZH = {
    'responses': '响应', 'response': '响应',
    'expression': '表达', 'accumulation': '积累',
    'growth': '生长', 'elongation': '伸长',
    'development': '发育', 'biosynthesis': '合成',
    'signaling': '信号', 'signalling': '信号',
    'pathway': '通路', 'levels': '水平',
    'content': '含量', 'activity': '活性',
    'production': '产生', 'tolerance': '耐受性',
    'resistance': '抗性', 'formation': '形成',
    # 2026-11-04：'gene'/'rate'/'yield' 在 _HEAD_RE 里是中心词，却不在译表，
    # 于是 "distinct gene expression" 这类短语整串翻译失败、英文漏进正文。
    'gene': '基因', 'genes': '基因',
    'rate': '速率', 'yield': '产量',
}


# 2026-11-04 补：降级抽样中反复出现的修饰词，缺失会让整条短语退回英文。
_MODIFIER_ZH.update({
    'distinct': '差异', 'differential': '差异', 'altered': '改变的',
    'reduced': '降低的', 'increased': '升高的', 'elevated': '升高的',
    'decreased': '降低的', 'enhanced': '增强的', 'impaired': '受损的',
    'delayed': '延迟的', 'accelerated': '加速的', 'ectopic': '异位的',
    'constitutive': '组成型的', 'transient': '瞬时的', 'sustained': '持续的',
})


_HEAD_RE = re.compile(
    r'^(.*?)\s*(biosynthesis|accumulation|expression|growth|elongation|'
    r'development|signaling|signalling|pathway|levels|content|activity|'
    r'production|tolerance|resistance|formation|responses|response|'
    r'genes|gene|rate|yield)$', re.I)


def _object_zh(obj):
    """英文过程名词统一为中文（精确表 + 组合式翻译）。"""
    if not obj:
        return obj
    low = re.sub(r'\s+', ' ', obj.strip().lower())
    if low in _OBJECT_ZH:
        return _OBJECT_ZH[low]
    if re.search(r'[\u4e00-\u9fff]', obj):
        return obj
    # "soluble sugars accumulation in pear fruits" 这类带场所后缀的短语：
    # 先剥离 " in/of <场所>"，翻译前半段过程名词，场所保留在括号里。
    # 旧实现整串匹配失败 → 英文原样进入中文标题（未翻译过程名词）。
    _loc = re.match(r'^(.*?)\s+(?:in|of)\s+(.{3,})$', low)
    if _loc:
        left = _object_zh(_loc.group(1))
        if left != _loc.group(1):
            return '%s（%s）' % (left, _loc.group(2))
    m = _HEAD_RE.match(low)
    if m:
        mod, head = m.group(1).strip(), m.group(2).lower()
        head_zh = _GENERIC_HEAD_ZH.get(head)
        if mod and head_zh:
            if mod in _MODIFIER_ZH:
                return _MODIFIER_ZH[mod] + head_zh
            # "distinct gene expression"：mod 自身是 "distinct gene"，先递归译它
            mod_zh = _object_zh(mod)
            if mod_zh != mod and re.search(r'[一-鿿]', mod_zh):
                return mod_zh + head_zh
            words = mod.split()
            # 复数形态（soluble sugars / soluble sugar）都要能命中：
            # 旧实现只查单数，导致 "soluble sugars accumulation" 原样漏到
            # 中文标题里，触发未翻译过程名词的回归测试。
            def _zw(w):
                return _MODIFIER_ZH.get(w) or _MODIFIER_ZH.get(w.rstrip('s'))
            if words and all(_zw(w) for w in words):
                return ''.join(_zw(w) for w in words) + head_zh
    # 兜底：译不出来就不要把英文塞进中文句子。返回空串 -> 上游走其他问题形态。
    return ''

def _clip(text, n):
    """按词边界截断并显式标注省略，避免 'for the nu' 这类断词。"""
    t = ' '.join(str(text or '').split())
    if len(t) <= n:
        return t
    cut = t[:n]
    if ' ' in cut:
        cut = cut[:cut.rfind(' ')]
    cut = cut.rstrip(' ,;:.(-')
    return cut + '…'


def _is_woody(sp):
    return bool(sp) and bool(re.search(
        r'poplar|populus|apple|malus|grape|vitis|citrus|peach|prunus|pear|'
        r'pine|pinus|eucalyptus|willow|salix|jatropha|rubber|hevea|camellia|tea',
        sp, re.I))


# ============================================================
# 假说框架：由证据簇的"结构事实"决定，而不是套同一句模板。
# 每个框架都对应一类真实的证据缺口与一种可执行的判别性实验。
# ============================================================

_BAD_OBJECT_WORDS = frozenset("""
triggers triggered triggering promotes promoted induces induced
inhibits inhibited represses repressed activates activated enhances enhanced
suppresses suppressed reduces reduced decreases decreased increases increased
mediates mediated regulates regulated controls controlled causes caused
requires required confers conferred provides provided leads led results resulted
impaired improved altered elevated depleted enriched accumulated
ectopic exogenous transient constitutive overexpression knock-down knockdown
knockout knock-out silencing mutant mutants transgenic complementation
calculate calculated calculates calculating
show showed shown shows showing
measure measured measuring
determine determined determining
detect detected detecting
analyse analyse analyzed analysed analysing analyzing
compare compared comparing
observe observed observing
evaluate evaluated evaluating
assess assessed assessing
quantify quantified quantifying
normalise normalize normalized normalised normalized
estimated estimate estimating
obtain obtained obtaining
found find finding findings
used using perform performed performing
identified identify
""".split())


def _object_usable(obj):
    """宾语必须是"可测量的生物学过程/性状"，不能是流程动词残句。"""
    if not obj:
        return False
    low = obj.lower()
    words = re.findall(r"[a-z][a-z\-]*", low)
    if not words:
        return False
    if words[0] in _BAD_OBJECT_WORDS:
        return False
    if any(w in _BAD_OBJECT_WORDS for w in words):
        return False
    if re.match(r'^(?:origin|members?|these|those|such|both|either)\b', low):
        return False
    tok0 = words[0]
    if len(tok0) <= 3 and tok0.islower() and tok0 not in (
            'aba', 'ga', 'ja', 'sa', 'br', 'ck', 'eth', 'acc', 'ros', 'no'):
        return False
    if low in ('expression', 'transcript levels', 'relative expression',
               'direct downstream response', 'downstream response',
               'gene expression', 'activity', 'protein levels', 'mrna levels'):
        return False
    return True


def _cluster_facts(cluster):
    """证据簇的结构画像：决定用哪种假说框架。"""
    papers = {paper_key(e) for e in cluster}
    types = Counter((e.get('evidence_type') or '').strip() for e in cluster)
    prim = Counter((e.get('primary_species') or '').strip() for e in cluster)
    prim.pop('', None)
    dom, dom_n = (prim.most_common(1)[0] if prim else ('', 0))
    n = max(1, len(cluster))
    species = {s for e in cluster for s in e['species'] if s}
    return {
        'n_ev': len(cluster),
        'n_papers': len(papers),
        'papers': papers,
        'types': types,
        'perturb': types.get('genetic perturbation', 0),
        'interaction': (types.get('protein interaction', 0)
                        + types.get('DNA binding/regulation', 0)),
        'expr_only': types.get('expression/regulation', 0),
        'n_compounds': sum(len(e['compounds']) for e in cluster),
        'dom_species': dom,
        'dom_frac': (float(dom_n) / n) if n else 0.0,
        'n_species': len(species),
    }


def _in_papers(n):
    if n <= 2:
        return '在两项研究中'
    return '在 %d 项研究中' % n


def _papers_word(n):
    if n >= 8:
        return '%d 项独立研究' % n
    if n >= 3:
        return '%d 项研究' % n
    return '两项研究'


_FRAMING_ZH = {
    'dose-response': '剂量—响应',
    'directional': '方向裁决',
    'conflict': '分歧裁决',
    'perturbation-unresolved': '扰动归一',
    'interaction-required': '互作必需性',
    'flux': '通量检验',
    'conservation': '跨物种保守',
    'common-upstream': '共同上游排除',
    'dose-response': '剂量—效应',
    'necessity': '必要性检验',
    'method-reproducibility': '方法可复现',
    'assembly-robustness': '组装稳健性',
    'replication': '独立复现',
    'method-sensitivity': '方法敏感性',
    'family-redundancy': '家族冗余',
    'process-conservation': '跨物种保守',
    'annotation-consistency': '注释一致性',
    'assembly-contiguity': '组装连续性',
    'dissociation-artifact': '解离偏好',
    'spatial-validation': '空间核实',
    'trajectory-robustness': '轨迹稳健性',
    'marker-specificity': '标记特异性',
    # 2026-11-03 第 12 轮：代谢与激素的领域专用框架
    'regulatory-linkage': '调控连接',
    'flux-attribution': '通量归因',
    'enzyme-kinetics': '酶动力学',
    'compartment-transport': '区室转运',
    'receptor-ligand-binding': '受体结合',
    'crosstalk-epistasis': '互作上位性',
    'dose-response-quantitative': '剂量定量',
    'protein-turnover': '蛋白周转',
}


def _zh_tight(s):
    """去掉两汉字之间多余的空格（'与 激素响应' -> '与激素响应'），保留中英间距。"""
    if not s:
        return s
    prev = None
    while prev != s:
        prev = s
        s = re.sub('(?<=[\u4e00-\u9fff]) (?=[\u4e00-\u9fff])', '', s)
    return s


def _framed(framing, statement, pred_true, pred_false):
    return {'framing': framing,
            'statement': _zh_tight(statement),
            'pred_true': _zh_tight(pred_true),
            'pred_false': _zh_tight(pred_false)}


def build_hypothesis(cluster, theme_id):
    """由证据簇构造一条可证伪假说；无法落地则返回 None。

    框架选择是**证据驱动的**：different clusters 有不同的证据构成，
    因而得到不同的问题形态（方向裁决 / 必要性 / 互作必需性 / 通量 /
    跨物种保守 / 共同上游 / 剂量-效应），而不是同一句模板换词。
    """
    facts = _cluster_facts(cluster)
    if (facts['n_ev'] < MIN_EVIDENCE_PER_HYPOTHESIS
            or facts['n_papers'] < MIN_PAPERS_PER_HYPOTHESIS):
        return None

    genes = Counter()
    for ev in cluster:
        for g in candidate_genes(ev):
            genes[g] += 1
    species = Counter(s for ev in cluster for s in ev['species'] if s)
    target = _top(genes, 1)[0] if genes else ''
    sp = resolve_species(cluster, target)

    relations = []
    for ev in cluster:
        s, pol, obj = extract_relation(ev['claim'])
        if s and pol and _object_usable(obj):
            relations.append((s, pol, obj, ev))
    conflict = len({r[1] for r in relations}) > 1 if relations else False
    polarity = Counter(r[1] for r in relations).most_common(1)[0][0] if relations else None

    # 宾语优先取"与靶标同篇共现"的过程名词：这样关联断言是真的共现，
    # 而不是把簇里另一篇论文的宾语硬贴到这个基因上。
    objects = Counter()
    for ev in cluster:
        same_paper_target = (not target) or target in (ev.get('genes') or []) \
            or re.search(r'\b' + re.escape(target) + r'\b', ev['claim'] or '')
        if not same_paper_target:
            continue
        for o in candidate_objects(ev):
            if _object_usable(o):
                objects[o] += 1
    obj = ''
    if relations:
        obj = Counter(r[2] for r in relations).most_common(1)[0][0]
    elif objects:
        obj = _top(objects, 1)[0]
    if obj and obj.lower() in PROCESS_NOUNS:
        obj = ''
    if obj and not _object_usable(obj):
        obj = ''
    obj_en = obj
    obj = _object_zh(obj)

    in_sp = (' %s 中' % sp) if sp else '同一物种中'
    framed = None

    if target and obj and relations and not conflict and polarity == 'positive':
        framed = _framed('directional',
            '%s 正向促进 %s。判别性检验：在%s敲低或敲除 %s，%s 应下降；'
            '恢复表达应使其回升。' % (target, obj, in_sp, target, obj),
            '敲低/敲除株系中 %s 显著下降且可被回补，过表达株系上升' % obj,
            '遗传操纵后 %s 无方向一致的变化，或变化与 %s 的表达量无关' % (obj, target))
    elif target and obj and relations and not conflict and polarity == 'negative':
        framed = _framed('directional',
            '%s 负向抑制 %s。判别性检验：在%s敲低或敲除 %s，%s 应上升；'
            '过表达应使其下降。' % (target, obj, in_sp, target, obj),
            '敲低/敲除株系中 %s 显著上升且可被回补，过表达株系下降' % obj,
            '遗传操纵后 %s 无方向一致的变化，或变化与 %s 的表达量无关' % (obj, target))
    elif target and obj and relations and conflict:
        framed = _framed('conflict',
            '%s 对 %s 的效应在不同研究中方向相反。判别性检验：把各研究的物种、'
            '组织与处理条件对齐后重做操纵实验，看方向是否由这些条件系统决定。'
            % (target, obj),
            '在统一遗传背景与同一读出下，%s 的效应方向由组织或处理条件稳定预测' % target,
            '条件对齐后方向差异消失，说明原分歧来自体系差异或统计噪声')
    elif target and obj and facts['perturb'] >= 2:
        framed = _framed('perturbation-unresolved',
            '%s 在本主题内已有遗传扰动证据，但扰动结果尚未被同一读出体系归一，'
            '因此它对 %s 的作用方向仍是空白。判别性检验：用等位基因系列在同一背景下'
            '定量 %s。' % (target, obj, obj),
            '等位基因强度与 %s 的变化呈单调关系，方向在所有等位系中一致' % obj,
            '不同等位系方向相反，或效应量随背景随机波动')
    elif target and obj and facts['interaction'] >= 2:
        framed = _framed('interaction-required',
            '%s 与 %s 的直接结合/互作已有报道，但"结合是否为功能所必需"未被检验。'
            '判别性检验：引入破坏结合界面的点突变，比较蛋白丰度与 %s 的变化。'
            % (target, obj, obj),
            '互作缺陷突变体中 %s 不再被改变，而 %s 蛋白丰度与野生型相当' % (obj, target),
            '互作缺陷突变体仍改变 %s，说明结合非必需或存在旁路' % obj)
    elif target and obj and facts['n_compounds'] >= 3:
        framed = _framed('flux',
            '%s 与 %s 的稳态水平在多项研究中同时被报道，但本簇证据中没有直接测定'
            '通量的结果（受检索覆盖限制，需回溯原文复核）。'
            '判别性检验：用同位素标记比较合成速率与稳态浓度。'
            % (target, obj),
            '%s 操纵改变 %s 的合成通量，且通量变化先于稳态浓度变化'
            % (target, obj),
            '仅稳态浓度变化而通量不变，说明效应来自降解或转运而非合成')
    elif target and obj and facts['dom_frac'] >= 0.75 and facts['n_species'] <= 6 \
            and facts['n_papers'] >= 4:
        framed = _framed('conservation',
            '现有 %s几乎全部基于 %s，%s 对 %s 的调控是否保守未知。'
            '判别性检验：在近缘物种中用同源基因做同向操纵与同一读出。'
            % (_papers_word(facts['n_papers']),
               facts['dom_species'] or '单一物种', target, obj),
            '近缘物种中同源基因的操纵产生方向一致的 %s 变化' % obj,
            '近缘物种中同源基因操纵无效，或方向相反')
    elif target and obj:
        framed = _framed('common-upstream',
            '%s 与 %s 在本主题的多项研究中被同时报道，但二者目前只是表达层面的共变。'
            '判别性检验：阻断 %s，看 %s 是否随之改变，而非二者共受上游驱动。'
            % (target, obj, target, obj),
            '阻断 %s 后 %s 发生可测变化，而共同上游因子的活性或丰度未同步改变'
            % (target, obj),
            '阻断 %s 后 %s 不变，或共同上游因子改变时两者同步变化（提示平行而非上下游）'
            % (target, obj))
    elif target and facts['n_papers'] >= 8:
        n_grad = _count_re(cluster, GRADIENT_RE)
        framed = _framed('dose-response',
            '%s 已有 %s；但其中仅 %d 条给出不同表达/活性水平的梯度或剂量—响应参数，'
            '效应量随水平变化的定量关系无法从现有文献取得'
            '（受检索覆盖限制，需系统检索复核）。'
            '判别性检验：构建梯度表达系并做定量表型曲线。'
            % (target, _papers_word(facts['n_papers']), n_grad),
            '表型随 %s 表达或活性单调变化，半数效应点可在独立实验室复现' % target,
            '表型与表达量无单调关系（阈值型或非单调），提示存在缓冲或旁路')
    elif target:
        cls, test = _gene_class(target)
        n_ev = facts['n_ev']
        expr = facts['expr_only']
        if expr >= 0.6 * n_ev:
            lead = ('%s 在本主题内由 %d 条证据支持，其中 %d 条为表达/调控型；'
                    '本簇证据中没有出现遗传操纵的结果，功能必要性因此未在本知识库内'
                    '被直接检验（受检索覆盖限制，需回溯原文与系统检索复核）。'
                    % (target, n_ev, expr))
        elif facts['perturb']:
            lead = ('%s 已有 %d 条遗传扰动证据，但读出体系不一致，'
                    '方向与必要性仍未确定。' % (target, facts['perturb']))
        else:
            lead = ('%s %s被提名参与本主题，但本簇证据中未见在统一背景下检验其'
                    '必要性的操纵实验（受检索覆盖限制，需回溯原文复核）。'
                    % (target, _in_papers(facts['n_papers'])))
        if test:
            sep = ' ' if cls[:1].isascii() else ''
            statement = lead + ('%s 属%s%s；判别性检验：%s。'
                                % (target, sep, cls, test[0]))
            pred_true = test[1]
            pred_false = '催化/结合缺陷与野生型表现无差异，说明该结构域非必需或存在旁路'
        else:
            statement = lead + ('判别性检验：获得功能缺失等位基因，'
                                '做表型、回补与组织特异性验证。')
            pred_true = '功能缺失等位基因产生稳定、可回补的表型缺陷'
            pred_false = '功能缺失无表型，或表型不可回补（提示脱靶或冗余基因补偿）'
        framed = _framed('necessity', statement, pred_true, pred_false)
    else:
        subj, subj_kind = cluster_subject(cluster, theme_id)
        if not subj:
            return None
        if subj_kind != 'gene' and theme_id not in ('methods-tools', 'genomics-evolution'):
            return None
        target = subj
        obj = '可重复性'
        if theme_id == 'methods-tools':
            framed = _framed('method-reproducibility',
                '本主题中 "%s" 被反复采用，但缺少跨数据集的独立评测。'
                '判别性检验：在留出数据集上按预注册指标复现其性能。' % subj,
                '留出数据集上复现已发表性能，差异在预注册容差内',
                '留出数据集上性能显著低于报告值，或流程无法运行')
        elif theme_id == 'genomics-evolution':
            framed = _framed('assembly-robustness',
                '"%s" 相关结论主要来自有限物种与有限组装质量的数据。'
                '判别性检验：在新增独立基因组中复检，并检验信号是否随组装碎片化而消失。'
                % subj,
                '新增独立基因组中检出方向一致的信号，且与组装质量指标无关',
                '新增基因组中信号消失，或完全可由组装碎片化解释')
        else:
            framed = _framed('replication',
                '在 %s 中，"%s" 这一结论尚未在独立样本或独立平台上重复。'
                '判别性检验：用同物种独立数据按预注册指标复现。'
                % (sp or '当前证据物种', subj),
                '独立数据中以预注册指标复现该结论，一致性高于预设阈值',
                '独立数据无法复现该结论，或效应量低于预设阈值')

    ev_ids = [e['id'] for e in sorted(cluster, key=lambda x: -len(x['claim']))[:8]]
    dois = [e['doi'] for e in cluster if e.get('doi')][:3]
    q0, qid0 = _cluster_quote(cluster, target, obj)

    # 缺口：只写"证据里真的缺什么"，不写套话
    gaps = []
    if facts['n_species'] == 1 and species:
        gaps.append('全部支撑证据来自单一物种（%s），跨物种保守性未知' % sp)
    if facts['n_papers'] <= 2:
        gaps.append('仅 %d 篇独立论文支撑，复现性未经第三方验证' % facts['n_papers'])
    if facts['perturb'] == 0:
        gaps.append('现有证据以表达/关联为主，缺少遗传操纵的因果证据')
    if facts['interaction'] == 0 and theme_id not in ('methods-tools', 'genomics-evolution'):
        gaps.append('缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知')
    if theme_id != 'single-cell-spatial-omics' and not any(
            'single-cell' in t or 'spatial' in t for e in cluster for t in e['tags']):
        gaps.append('缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞')
    if theme_id != 'methods-tools' and any('method' in t for e in cluster for t in e['tags']):
        gaps.append('方法学证据与生物学结论混在一起，需分离验证')

    return {
        'target': target,
        'object': obj,
        'species': sp,
        'framing': framed['framing'],
        'statement': framed['statement'],
        'polarity': polarity,
        'conflict': conflict,
        'support_evidence': facts['n_ev'],
        'support_papers': facts['n_papers'],
        'evidence_ids': ev_ids,
        'dois': dois,
        'pred_true': framed['pred_true'],
        'pred_false': framed['pred_false'],
        'gaps': gaps,
        'confidence': ('高' if facts['n_papers'] >= 6 else
                       '中' if facts['n_papers'] >= 3 else '低'),
        'core_claim': q0,
        'quote_id': qid0,
    }


# ============================================================
# 模式级假说（2026-11-02 新增）
# ------------------------------------------------------------
# 已有的簇级生成器要求"同一个基因被 >=3 条证据、>=2 篇论文反复研究"。
# 在单细胞/空间组学、方法学、基因组学这类主题里，每篇论文研究不同基因、
# 不同物种、不同管线，簇级聚类因此几乎不产出（实测：299 条证据只出 1 条）。
# 下面四类生成器改从"跨论文的结构性模式"出发，不依赖某个基因被重复研究：
#   1. 方法敏感性：同组工具被并行使用，但从未在同一批数据上对照；
#   2. 家族冗余：同一基因家族的多个成员分别被提名，但无人同时操纵；
#   3. 过程保守：同一过程在多物种被观察，但因果操纵只在单一物种完成；
#   4. 注释一致性：同一组织的细胞类型划分粒度不一致（仅单细胞主题）。
# 每条仍强制 >=3 条证据、>=2 篇独立论文，并附证据 ID 与证伪条件。
# ============================================================

PATTERN_MIN_EV = 3
PATTERN_MIN_PAPERS = 2

# 同组工具/平台：组内不同实现给出不一致结论的风险，正是需要 benchmark 的地方。
# 只收录在植物文献中确实会被"择一使用"的实现，避免把偶然出现的词当工具。
METHOD_GROUPS = {
    '单细胞建库平台': {
        '10x Chromium': r'10x|chromium', 'Drop-seq': r'drop-?seq',
        'Smart-seq': r'smart-?seq', 'MATQ-seq': r'matq',
        'snmC-seq': r'snmc-?seq', 'snRNA-seq': r'sn(?:rna)?-?seq',
    },
    '空间转录组平台': {
        'Visium': r'visium', 'MERFISH': r'merfish', 'Slide-seq': r'slide-?seq',
        'Stereo-seq': r'stereo-?seq', 'seqFISH': r'seqfish', 'CosMx': r'cosmx',
    },
    '长读长组装': {
        'PacBio HiFi': r'pacbio|hifi', 'Oxford Nanopore': r'nanopore',
        'hifiasm': r'hifiasm', 'Canu': r'\bcanu\b', 'Flye': r'\bflye\b',
    },
    '差异表达统计': {
        'DESeq2': r'deseq2?', 'edgeR': r'edger', 'limma-voom': r'limma',
    },
    '序列比对': {
        'STAR': r'\bstar\b', 'HISAT2': r'hisat2', 'Bowtie2': r'bowtie2?',
        'BWA': r'\bbwa\b', 'minimap2': r'minimap2',
    },
    '系统发育重建': {
        'IQ-TREE': r'iq-?tree', 'RAxML': r'raxml', 'ASTRAL': r'astral',
        'MrBayes': r'mrbayes',
    },
    '同源基因推断': {
        'OrthoFinder': r'orthofinder', 'OrthoMCL': r'orthomcl',
        'Broccoli': r'broccoli',
    },
    '数据整合': {
        'Harmony': r'harmony', 'Seurat CCA/RPCA': r'\bcca\b|\brpca\b',
        'Scanorama': r'scanorama', 'scVI': r'\bscvi\b',
    },
}

CELLTYPE_NUM_RE = re.compile(
    r'(\d{1,3})\s*(?:distinct\s+|major\s+|different\s+)?'
    r'(?:cell\s+types?|cell\s+states?|cell\s+clusters?|clusters|subtypes)', re.I)


def _ev_text(ev):
    return ((ev.get('title') or '') + ' ' + (ev.get('claim') or '')).lower()


def _mk_pattern(framing, target, obj, statement, pred_true, pred_false,
                evs, gaps, species='', detail='', design='', manip='',
                readout='', keywords=(), avoid=()):
    """构造统一字段的模式级假说，供渲染与实践方案页复用。"""
    evs = sorted(evs, key=lambda e: -len(e.get('claim') or ''))
    papers = {paper_key(e) for e in evs}
    d_design, d_manip, d_readout = _PATTERN_DEFAULTS.get(framing, ('', '', ''))
    kw = [k.lower() for k in keywords]
    quote, quote_id = _pick_quote(evs, kw, avoid=avoid)
    return {
        'target': target,
        'object': obj,
        'species': species,
        'framing': framing,
        'pattern': True,
        'detail': detail,
        'design': design or d_design,
        'manip': manip or d_manip,
        'readout': readout or d_readout,
        'quote': quote,
        'quote_id': quote_id,
        'all_ids': [e['id'] for e in evs],
        'statement': statement,
        'polarity': None,
        'conflict': False,
        'support_evidence': len(evs),
        'support_papers': len(papers),
        'evidence_ids': [e['id'] for e in evs[:8]],
        'dois': [e['doi'] for e in evs if e.get('doi')][:3],
        'pred_true': pred_true,
        'pred_false': pred_false,
        'gaps': gaps,
        'confidence': ('高' if len(papers) >= 6 else
                       '中' if len(papers) >= 3 else '低'),
        'core_claim': quote,
    }


# ── 小分子/代谢物：不适用"同源基因跨物种保守"框架 ─────────────────────
SMALL_MOLECULES = frozenset([
    'auxin', 'cytokinin', 'gibberellin', 'abscisic acid', 'ethylene',
    'jasmon', 'jasmonate', 'salicylic acid', 'brassinosteroid',
    'strigolactone', 'melatonin', 'nitrate', 'phosphate', 'sucrose',
    'sugar', 'starch', 'lignin', 'cellulose', 'anthocyanin', 'flavonoid',
    'carotenoid', 'chlorophyll', 'lipid', 'nitric oxide', 'reactive oxygen',
    # 2026-11-03 第 12 轮：代谢物"类别"同样不是基因，不能套家族冗余/
    # 跨物种互补/剂量—效应三类基因框架。此前 "terpenoid（跨物种保守）"、
    # "flavonoid（剂量—效应）" 就是由此产生的模板化假说。
    'phenylpropanoid', 'terpenoid', 'terpene', 'alkaloid', 'phenolic',
    'suberin', 'cutin', 'wax', 'saponin', 'stilbene', 'lignan', 'flavonol',
    'proanthocyanidin', 'triterpenoid', 'sesquiterpenoid', 'monoterpenoid',
    'glucosinolate', 'cyanogenic glycoside', 'betacyanin', 'tocopherol',
])


# 抽取层产生过的伪影物种（"Fig. 1"→Ficus、"orange"→Citrus），不参与任何计数。
ARTIFACT_SPECIES = frozenset(['Ficus carica', 'Citrus spp.', 'Citrus sinensis'])


def paper_species(evs):
    """论文级物种集合。

    实测：`species` 字段是"全文提到过的物种"，一篇拟南芥论文只要在引言里
    提一句水稻就会被计入，导致"22 个物种"这类虚高计数。假说里的物种数
    一律用 primary_species（每篇论文一个主物种）。
    """
    out = set()
    for e in evs:
        sp = (e.get('primary_species') or '').strip()
        if sp and sp not in GENERIC_SPECIES and sp not in ARTIFACT_SPECIES:
            out.add(sp)
    return out


def _is_small_molecule(name):
    k = (name or '').strip().lower()
    if k in SMALL_MOLECULES:
        return True
    return any(k.startswith(x) for x in
               ('auxin', 'cytokinin', 'gibberellin', 'jasmon', 'brassinosteroid',
                'strigolactone', 'abscisic'))


def _count_re(evs, pattern):
    """统计有多少条证据自身的断言命中某个正则（用于把"没有研究"变成可核对的计数）。"""
    rx = re.compile(pattern, re.I)
    return sum(1 for e in evs if rx.search(e.get('claim') or ''))

MULTI_MUT_RE = (r'\b(?:double|triple|quadruple)\s+mutant|'
                r'\b(?:double|triple)[- ]knock|'
                r'\b(?:two|three|multiple)\s+(?:independent\s+)?mutants')
GRADIENT_RE = (r'dose[- ]?dependent|dose[- ]?response|concentration[- ]?dependent|'
               r'\bEC50\b|\bIC50\b|\bED50\b|concentration gradient|gradient of|'
               r'(?:var(?:y|ying|ious)|different|increasing|series of|range of)\s+'
               r'concentrations?|concentrations?\s+(?:of|ranging|from)|'
               r'titrat\w*|\d+\s*(?:nM|µM|μM|mM)[^.]{0,60}'
               r'\d+\s*(?:nM|µM|μM|mM)')
FRAGMENT_RE = (r'fragment\w*|simulated contig|broken into contigs|scaffold[- ]level|'
               r'assembly quality|contiguity')
LABELTRANS_RE = (r'label transfer|marker[- ]based annotation|integration|'
                 r'integrated (?:dataset|analysis)|batch[- ]correct')
CO_MENTION_TOOLS = r''

JUNK_SENT_RE = re.compile(
    r'^(?:figure|fig\.|table|box|scheme|supplementary)\b|'
    r'\|.*\||^see also|^https?://', re.I)


def _sentences(text):
    text = re.sub(r'\s+', ' ', (text or '')).strip()
    if not text:
        return []
    parts = re.split(r'(?<=[.;!?])\s+(?=[A-Z0-9“(])', text)
    return [p.strip() for p in parts if p.strip()]


def _quote_ok(sent):
    if len(sent) < 40 or JUNK_SENT_RE.match(sent):
        return False
    if sent.count(':') >= 2:          # PDF 小标题与正文被粘在一起
        return False
    if len(re.findall(r'[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+:', sent)) >= 1:
        return False
    letters = len(re.findall(r'[A-Za-z]', sent))
    if letters < 30 or letters / float(len(sent)) < 0.6:
        return False
    return True


def _pick_quote(evs, keywords, avoid=()):
    """挑一句"确实提到该关键词、且不像 PDF 抽取残渣"的原句，并附来源证据 ID。

    旧实现取最长断言的前 300 字符，常给出半句话，或给出与假说主语无关的片段
    （例如讲 QC cell 的段落被用来支撑"表皮身份"）。这里改为按关键词检索句子。
    """
    keys = [k for k in keywords if k]
    avoid = set(avoid)
    ordered = sorted((e for e in evs if e.get('id') not in avoid),
                     key=lambda e: -len(e.get('claim') or ''))
    for need in (True, False):
        for ev in ordered:
            for s in _sentences(ev.get('claim')):
                if not _quote_ok(s):
                    continue
                if need and keys and not any(k in s.lower() for k in keys):
                    continue
                q = s if len(s) <= 320 else s[:317].rstrip() + '…'
                return q, ev.get('id') or ''
    for ev in ordered:
        c = re.sub(r'\s+', ' ', ev.get('claim') or '').strip()
        if c:
            return (c if len(c) <= 320 else c[:317].rstrip() + '…'), ev.get('id') or ''
    return '', ''


_PATTERN_DEFAULTS = {
    'method-sensitivity': (
        '同一输入数据 + 同一预处理，仅替换待比较的实现',
        '实现（唯一变量）：组内各工具/平台版本',
        '效应量、显著性排名、关键对象方向的一致性'),
    'family-redundancy': (
        '原报道物种，同遗传背景、同生育期',
        '家族成员的敲除/敲低，单突变 vs 双/多突变',
        '定量表型效应量与同源成员表达水平'),
    'process-conservation': (
        '至少两个物种（原报道物种 + 一个独立谱系）',
        '同源因子的遗传操纵（突变/敲低/过表达）',
        '同一过程的定量读出与跨物种互补结果'),
    'assembly-contiguity': (
        '同一份染色体级组装 + 梯度碎片化版本（contig/scaffold 级）',
        '组装连续性（唯一变量），注释与家族推断流程保持不变',
        '基因家族拷贝数、共线性区块数、旁系同源分组的一致性'),
    'annotation-consistency': (
        '至少两个独立数据集（不同物种或不同平台），同一组织部位',
        '注释方案（参照标记集 vs 目标数据集自有注释），唯一变量',
        '标签转移一致率、独立标记阳性率、空间位置吻合度'),
    'dose-response': (
        '原报道物种 + 一个独立物种；同遗传背景、同生育期',
        '外源施加的浓度梯度（≥5 个剂量）± 合成抑制剂；受体突变体作对照',
        '剂量—响应曲线、EC50、下游响应的动态范围'),
    'dissociation-artifact': (
        '同一组织的同一样本分半，分别做原生质体与细胞核建库',
        '解离方式（唯一变量）：原生质体酶解 vs 细胞核提取；建库与聚类流程保持一致',
        '类型比例偏差、标记基因表达相关性、类型级召回率'),
    'spatial-validation': (
        '同一组织的 >=2 个独立空间转录组数据集（尽可能含两个平台）',
        '空间平台与样本来源（唯一变量）；重注释使用同一标记集',
        '类型—位置对应率、空间邻域富集、跨数据集一致性'),
    'trajectory-robustness': (
        '同一份预处理后的表达矩阵（同一基因过滤与归一化）',
        '轨迹推断实现（唯一变量）：>=3 种（如 Monocle / Slingshot / PAGA）',
        '分支数、分支点位置、关键基因沿伪时间的顺序一致性'),
    'marker-specificity': (
        '原报道数据集 + 一个独立数据集（不同实验室或平台）',
        '标记基因集（唯一变量）：原报道标记集 vs 交叉验证后收窄的标记集',
        '跨类型表达泄漏率、类型判别 AUC、原位或空间位置吻合度'),
    'regulatory-linkage': (
        '原报道物种；同遗传背景、同生育期、同组织部位',
        '转录因子的功能缺失与回补（唯一变量），代谢物定量方法保持一致',
        'TF 与靶启动子的直接结合、靶基因转录变化、代谢物含量的时间先后'),
    'flux-attribution': (
        '原报道物种；同一组织、同一生育期，标记喂养条件一致',
        '稳定同位素喂养（13C/14C）与目标基因操纵（唯一变量）',
        '合成通量、降解速率与稳态库大小的分解'),
    'enzyme-kinetics': (
        '异源表达系统（大肠杆菌/酵母/本氏烟草）与纯化蛋白',
        '候选酶及其底物特异性突变体（唯一变量）',
        'kcat/Km、底物特异性与产物鉴定'),
    'compartment-transport': (
        '原报道物种；同一组织，原生质体与完整组织并行',
        '转运蛋白功能缺失（唯一变量）与液泡/质体分离',
        '代谢物在区室间的分配比例与转运速率'),
    'receptor-ligand-binding': (
        '体外重组受体蛋白与合成配体；另设体内报告系统',
        '配体类似物与受体结合位点突变（唯一变量）',
        '解离常数、结合化学计量与下游响应 EC50 的对应关系'),
    'crosstalk-epistasis': (
        '原报道物种；同遗传背景，单、双、三突变并列',
        '两条激素通路的遗传操纵（唯一变量）：单突变 vs 双突变',
        '双突变相对单突变的效应偏离（上位性指数）与剂量矩阵响应面'),
    'dose-response-quantitative': (
        '原报道物种 + 一个独立物种；同一施加方式与取样时间',
        '外源激素浓度梯度（≥5 个剂量，覆盖生理与超生理范围）',
        '剂量—响应曲线、EC50 与 Hill 系数'),
    'protein-turnover': (
        '原报道物种；同一组织，蛋白合成抑制剂处理的时间序列',
        '降解信号突变（唯一变量）与蛋白酶体抑制剂对照',
        '蛋白半衰期、泛素化修饰状态与降解速率常数'),
}


# ── 单细胞与空间组学：领域专用模式 ────────────────────────────────
# 通用生成器在本主题几乎全空：全部证据中约八成是 omics/co-occurrence，
# 同一基因很少被两篇以上论文重复研究，簇级与家族级生成器因此无从下手。
# 但这不等于没有问题可问——该领域真正的分歧集中在四类方法学决定上：
# 怎么解离、空间上是否落实、轨迹怎么推、标记基因是否特异。
# 下面四条只陈述证据中确实存在的分歧或空白，不做跨证据推断。

SC_MODE_ARMS = {
    '原生质体解离': r'protoplast',
    '细胞核解离': (r'single[- ]nucle(?:us|i)|snrna|snatac|sn[ -]?seq|'
                r'nuclei isolat|nuclear suspension'),
}
SC_SPATIAL_RE = (r'spatial transcriptom|merfish|visium|stereo-?seq|smfish|'
                 r'seqfish|cosmx|in situ hybrid|spatial reconstru')
SC_TRAJ_RE = (r'trajector|pseudotime|rna velocity|monocle|slingshot|paga|'
              r'optimal transport')
SC_TRAJ_TOOLS = {
    'Monocle': r'monocle',
    'Slingshot': r'slingshot',
    'PAGA': r'paga',
    'RNA velocity': r'rna velocity',
    '最优传输': r'optimal transport',
    '伪时间（未指明实现）': r'pseudotime',
}
SC_MARKER_RE = r'marker gene|marker genes|markers'
SC_NONEXCLUSIVE_RE = (r'not expressed exclusively|not exclusively expressed|'
                      r'not exclusive|also expressed in|expressed in multiple'
                      r'|low specificity|not specific')


def pattern_singlecell_hypotheses(theme_id, items, taken):
    """单细胞/空间组学专用：解离方式、空间核实、轨迹稳健性、标记特异性。

    与通用 pattern 生成器的区别在于：待检验项不是某个基因，而是该领域
    四类会改变结论的方法学决定。每条仍强制 >=3 条证据、>=2 篇独立论文，
    并给出预注册的对照与证伪条件。
    """
    if theme_id != 'single-cell-spatial-omics':
        return []
    out = []
    texts = [(ev, _ev_text(ev)) for ev in items]

    def hits(pat):
        rx = re.compile(pat)
        return [ev for ev, t in texts if rx.search(t)]

    # 1) 解离方式：原生质体 vs 细胞核
    key = 'sc:dissociation-mode'
    if key not in taken:
        arms = {name: hits(pat) for name, pat in SC_MODE_ARMS.items()}
        union = {}
        for evs in arms.values():
            for e in evs:
                union[e['id']] = e
        evs = list(union.values())
        papers = {paper_key(e) for e in evs}
        both = [e for e in evs
                if all(re.search(p, _ev_text(e)) for p in SC_MODE_ARMS.values())]
        if (len(evs) >= PATTERN_MIN_EV and len(papers) >= PATTERN_MIN_PAPERS
                and all(arms.values())):
            taken.add(key)
            n_pro = len(arms['原生质体解离'])
            n_nuc = len(arms['细胞核解离'])
            out.append(_mk_pattern(
                'dissociation-artifact', '组织解离方式（原生质体 vs 细胞核）', '',
                '本主题 %d 条证据涉及组织解离，其中原生质体法 %d 条、细胞核法 %d 条，'
                '而在同一份组织内并列比较两者的仅 %d 条。因此"原生质体法报告的细胞'
                '类型比例能否在细胞核法数据中重现"在本库中没有对照证据；解离偏好与'
                '真实的生物学差异目前不可分离。判别性检验：同一样本分半，分别建库，'
                '比较类型比例与标记基因表达的一致性。'
                % (len(evs), n_pro, n_nuc, len(both)),
                '两种方式给出的类型比例偏差落在预注册容差内（例如每类 ±10 个百分点），'
                '且标记基因表达高度相关',
                '某一类细胞在原生质体数据中系统性富集或缺失，且偏差随酶解时间或'
                '渗透压条件变化，说明是解离偏好而非生物学差异',
                evs,
                ['原生质体法 %d 条、细胞核法 %d 条，直接并列比较仅 %d 条'
                 % (n_pro, n_nuc, len(both)),
                 '缺少同一样本分半的设计，解离偏好与组织真实构成无法区分'],
                detail='原生质体法 %d 条 / 细胞核法 %d 条（并列比较 %d 条）'
                       % (n_pro, n_nuc, len(both)),
                keywords=['protoplast'],
            ))

    # 2) 空间核实：单细胞注释是否在空间上落实
    key = 'sc:spatial-validation'
    if key not in taken:
        evs = hits(SC_SPATIAL_RE)
        papers = {paper_key(e) for e in evs}
        if len(evs) >= PATTERN_MIN_EV and len(papers) >= PATTERN_MIN_PAPERS:
            both = [e for e in evs
                    if re.search(r'scrna[- ]?seq|single[- ]cell', _ev_text(e))]
            taken.add(key)
            out.append(_mk_pattern(
                'spatial-validation', '细胞类型的空间定位', '',
                '本主题 %d 条证据（%d 篇）涉及空间转录组或原位杂交，其中 %d 条同时'
                '描述单细胞数据与空间数据。本库中未见报道在两个独立空间数据集上'
                '比较同一类型空间分布的条目（受检索覆盖限制），因此"scRNA-seq 定义的类型在组织中占据'
                '可复现位置"这一前提在本库中仍属单向支持。判别性检验：在两个独立'
                '空间数据集上用同一标记集重注释，比较类型—位置对应关系。'
                % (len(evs), len(papers), len(both)),
                '关键类型在两个独立空间数据集中的分布（层、区、邻域富集）一致，'
                '且与标记基因表达位置吻合',
                '同一类型在不同数据集定位到不同区域，或某类型在空间数据中缺乏'
                '对应信号，说明注释粒度或取样存在偏差',
                evs,
                ['空间证据仅来自 %d 篇论文，跨数据集比较为 0 条' % len(papers),
                 '缺少统一的类型—位置映射标准，平台间分辨率差异未评估'],
                detail='%d 篇论文 / %d 条证据，其中 %d 条同时含单细胞与空间描述'
                       % (len(papers), len(evs), len(both)),
                keywords=['spatial', 'merfish', 'in situ', 'visium'],
            ))

    # 3) 轨迹稳健性：不同推断实现是否给出一致分支
    key = 'sc:trajectory-robustness'
    if key not in taken:
        evs = hits(SC_TRAJ_RE)
        papers = {paper_key(e) for e in evs}
        tools = {}
        for name, pat in SC_TRAJ_TOOLS.items():
            rx = re.compile(pat)
            got = [e for e in evs if rx.search(_ev_text(e))]
            if got:
                tools[name] = got
        if (len(evs) >= PATTERN_MIN_EV and len(papers) >= PATTERN_MIN_PAPERS
                and len(tools) >= 2):
            taken.add(key)
            names = sorted(tools, key=lambda k: -len(tools[k]))[:4]
            out.append(_mk_pattern(
                'trajectory-robustness', '细胞状态转变轨迹', '',
                '本主题 %d 条证据（%d 篇）做过轨迹或伪时间推断，涉及 %s，'
                '但本库中没有一条在同一份数据上比较过两种以上实现的分支拓扑（受检索覆盖限制）。'
                '"发育顺序与分支点"因此只是单一实现的产物，其对实现选择的'
                '敏感性无法判定。判别性检验：固定预处理，换用三种以上推断'
                '实现，比较分支数与关键基因排序。'
                % (len(evs), len(papers), '、'.join(names)),
                '各实现给出的分支数一致，分支点上调基因的重叠显著高于随机，'
                '关键基因沿伪时间的顺序相关高于预注册阈值',
                '分支数或分支位置随实现改变，说明原结论依赖算法而非数据',
                evs,
                ['轨迹证据 %d 条、实现 %d 种，同一数据上的对照为 0 条'
                 % (len(evs), len(tools)),
                 '伪时间顺序缺少独立时间序列数据的外部校准'],
                detail='、'.join(names),
                keywords=['trajector', 'pseudotime', 'rna velocity', 'optimal transport'],
            ))

    # 4) 标记基因特异性
    key = 'sc:marker-specificity'
    if key not in taken:
        evs = hits(SC_MARKER_RE)
        papers = {paper_key(e) for e in evs}
        nonex = [e for e in evs if re.search(SC_NONEXCLUSIVE_RE, _ev_text(e))]
        if len(evs) >= PATTERN_MIN_EV and len(papers) >= PATTERN_MIN_PAPERS:
            taken.add(key)
            out.append(_mk_pattern(
                'marker-specificity', '细胞类型标记基因的特异性', '',
                '本主题 %d 条证据（%d 篇）以标记基因定义细胞类型，其中 %d 条'
                '明确报告所涉标记基因并非只在单一类型中表达。标记基因在独立'
                '数据集与非目标类型中的特异性尚未被系统交叉验证，因此'
                '"某类型 = 某标记组合"的等式在本库中只有单侧支持。判别性检验：'
                '在独立数据集与原位/空间数据上量化每个标记基因的跨类型泄漏。'
                % (len(evs), len(papers), len(nonex)),
                '多数标记基因在非目标类型中的表达低于预注册阈值，类型判别 AUC '
                '在留出数据上保持在原报道水平',
                '相当比例的标记基因存在广泛跨类型表达，类型判别实质上依赖少数'
                '高变异基因，则该类型划分需降级或合并',
                evs,
                ['%d/%d 条证据自陈标记基因非特异，其余未报告特异性检验'
                 % (len(nonex), len(evs)),
                 '缺少"独立数据集 + 原位"双重验证，特异性只有训练集内证据'],
                detail='%d 条证据自陈非特异' % len(nonex),
                keywords=['marker gene', 'markers', 'not expressed exclusively'],
            ))
    return out


# ── 代谢与激素：领域专用模式（2026-11-03 第 12 轮）────────────────
# 这两个主题此前的假说是"剂量—效应 / 家族冗余 / 跨物种保守"三件套，
# 主语常常是化合物类别（terpenoid、flavonoid、auxin），既不可操纵也无因果。
# 下面八个生成器只统计本库证据里真实存在的"主张—方法"错配，并把计数写进
# 陈述句；任一计数不达标就不生成，绝不为了凑数降低门槛。

METAB_TF_RE = re.compile(
    r'transcription factor|\bMYB|bHLH|\bWRKY|\bERF\b|\bNAC\b|bZIP|'
    r'\bARF\b|\bHY5\b|\bPIF\b', re.I)
METAB_DNA_BINDING_RE = re.compile(
    r'chip[- ]?seq|chip[- ]?qpcr|\bEMSA\b|electrophoretic mobility|'
    r'yeast one[- ]hybrid|\bY1H\b|promoter binding|binds (?:the |a )?promoter|'
    r'transactivation assay|dual[- ]luciferase', re.I)
METAB_METABOLITE_RE = re.compile(
    r'flavonoid|anthocyanin|lignin|terpen|alkaloid|carotenoid|stilbene|'
    r'saponin|phenolic|suberin|cutin|wax|phenylpropanoid|glucosinolate|'
    r'tocopherol|vitamin|steroid', re.I)
METAB_QUANT_RE = re.compile(
    r'hplc|lc[- ]?ms|gc[- ]?ms|metabolom|quantif|content of|'
    r'accumulat|level of|concentration of', re.I)
METAB_FLUX_RE = re.compile(
    r'\bflux\b|isotope|13c|14c|metabolic labeling|turnover|'
    r'de novo synthesis rate|labeling pattern', re.I)
METAB_ENZYME_RE = re.compile(
    r'\b(PAL|C4H|4CL|CHS|CHI|F3H|F3\'H|DFR|ANS|UFGT|CAD|COMT|CCR|HCT|'
    r'C3H|F5H|TPS|DXS|DXR|HMGR|GGPPS|SQS|BAS|PAS|CYP7\d\d[A-Z]\d)\b')
METAB_ASSAY_RE = re.compile(
    r'in vitro (?:assay|activity|enzymatic)|enzyme activity|recombinant|'
    r'purified protein|kinetic parameter|\bkcat\b|\bKm\b|\bVmax\b', re.I)
METAB_COMPARTMENT_RE = re.compile(
    r'subcellular|plastid|endoplasmic reticulum|\bER\b|vacuole|tonoplast|'
    r'cytosol|chloroplast|peroxisome|mitochondri', re.I)
METAB_TRANSPORT_RE = re.compile(
    r'transporter|\bABC\b|\bMFS\b|efflux|influx|vesicle|'
    r'transport assay|uptake assay', re.I)

HORM_RECEPTOR_RE = re.compile(r'receptor', re.I)
HORM_BINDING_ASSAY_RE = re.compile(
    r'binding assay|isothermal titration|\bITC\b|surface plasmon|\bSPR\b|'
    r'pull[- ]down|affinity (?:measurement|constant)|\bKd\b|'
    r'dissociation constant|radioligand|photoaffinity', re.I)
HORM_EXOGENOUS_RE = re.compile(
    r'exogenous|applied externally|treated with|treatment with|'
    r'supplement(?:ed|ation)|sprayed with|added to the medium', re.I)
HORM_GRADIENT_RE = re.compile(
    r'dose[- ]?response|dose[- ]?dependent|concentration[- ]?dependent|'
    r'\bEC50\b|\bIC50\b|concentration gradient|series of concentrations|'
    r'range of concentrations', re.I)
HORM_MULTI_RE = re.compile(
    r'auxin|cytokinin|ethylene|abscisic|\bABA\b|gibberellin|\bGA\b|'
    r'brassinosteroid|jasmon|salicylic|strigolactone', re.I)
HORM_EPISTASIS_RE = re.compile(
    r'epistas|double mutant|triple mutant|quadruple mutant|'
    r'genetic interaction|synergis|antagonis', re.I)
HORM_DEGRADATION_RE = re.compile(
    r'ubiquitin|proteasome|degradation|degron|26S', re.I)
HORM_TURNOVER_RE = re.compile(
    r'half[- ]life|cycloheximide|\bCHX\b|chase assay|turnover rate|'
    r'degradation rate|pulse[- ]chase', re.I)


def _fill_counts(template, vals):
    # 把模板里的 %d 按出现顺序依次替换；多余的占位符保持原样不报错。
    it = iter(vals)

    def repl(_m):
        try:
            return str(next(it))
        except StopIteration:
            return '%d'
    return re.sub(r'%d', repl, template)


def _domain_gap(evs, gap_re, label, min_gap=3):
    """返回 (gap_hits, ok)：缺口命中数低于阈值才允许生成假说。"""
    gap = [e for e in evs if gap_re.search(_ev_text(e))]
    return gap, len(gap) < min_gap


def pattern_metabolism_hypotheses(theme_id, items, taken):
    """代谢主题：TF 连接、通量归因、酶动力学、区室转运四类真实缺口。"""
    if theme_id != 'metabolism-natural-products':
        return []
    out = []
    texts = [(ev, _ev_text(ev)) for ev in items]

    def hits(rx):
        return [ev for ev, s in texts if rx.search(s)]

    specs = [
        ('meta:tf-linkage', 'regulatory-linkage',
         '转录因子—代谢物连接的直接证据',
         (METAB_TF_RE, METAB_METABOLITE_RE), METAB_DNA_BINDING_RE,
         '直接结合证据（ChIP/EMSA/Y1H/反式激活）',
         '本主题 %d 条证据（%d 篇）把转录因子与某类代谢物联系起来，但其中只有 %d 条'
         '给出启动子直接结合或反式激活证据。也就是说，"该 TF 调控该代谢分支"在本库中'
         '主要建立在表达相关与突变体表型之上，结合事件本身多为推定。缺失环节是：'
         '结合位点是否真实、是否在同一组织与生育期发生、以及结合强度是否足以解释'
         '代谢物变化幅度。',
         'ChIP 峰与候选靶基因启动子共定位，EMSA 证实结合，反式激活报告系统给出'
         '剂量依赖，且 tf 突变体中靶基因转录先于代谢物变化',
         'TF 结合位点突变后代谢物含量不变，或结合事件发生在与代谢变化不同的组织，'
         '说明该连接是间接的（经发育或胁迫程序）',
         ['%d 条证据中仅 %d 条报告直接结合或反式激活', '缺少同一组织内的结合—转录—代谢物时间序列'],
         ['transcription factor', 'MYB', 'bHLH', 'promoter'],
         'ChIP-seq + EMSA + 反式激活 + 突变体代谢物定量'),
        ('meta:flux-attribution', 'flux-attribution',
         '代谢物含量变化的通量归因',
         (METAB_METABOLITE_RE, METAB_QUANT_RE), METAB_FLUX_RE,
         '同位素标记或通量测量',
         '本主题 %d 条证据（%d 篇）报告了代谢物含量或积累量的变化，但仅 %d 条给出'
         '同位素标记、通量或周转测量。含量是合成、降解与转运三者叠加的稳态结果，'
         '因此"某基因提高某代谢物含量"无法区分是合成增强、降解减少还是外排受阻。'
         '这一缺口直接限制了代谢工程的靶点选择。',
         '标记喂养显示合成通量按预期改变，且降解速率与转运速率不变；'
         '通量变化的时间早于稳态含量变化',
         '含量升高但合成通量不变、降解或外排速率下降，说明原靶点并非限速步骤',
         ['%d 条证据报告含量，%d 条报告通量/周转', '缺少合成—降解—转运的分解测量'],
         ['content', 'accumulation', 'biosynthesis'],
         '13C/14C 标记喂养 + 通量建模 + 降解/转运速率测定'),
        ('meta:enzyme-kinetics', 'enzyme-kinetics',
         '候选酶的体外动力学',
         (METAB_ENZYME_RE, METAB_METABOLITE_RE), METAB_ASSAY_RE,
         '重组酶体外动力学',
         '本主题有 %d 条证据（%d 篇）直接点名具体代谢酶家族成员并关联代谢物，'
         '但仅 %d 条报告重组酶或体外酶活。缺少 kcat/Km 与底物特异性，就无法判断'
         '该酶在体内的通量贡献，也无法解释同家族成员之间的功能分工。',
         '重组酶的 kcat/Km 与体内通量量级相容，底物特异性突变体在体内重现相应的'
         '代谢物谱改变',
         '体外动力学显示该酶对目标底物效率极低，或体内敲除后代谢物不变，'
         '说明命名来自序列相似而非功能',
         ['%d 条涉及具体酶，%d 条有体外动力学', '家族成员间的底物特异性未在统一体系中比较'],
         ['enzyme', 'kinetics', 'recombinant'],
         '异源表达 + 纯化 + 稳态动力学 + 底物特异性谱'),
        ('meta:compartment', 'compartment-transport',
         '代谢物的区室分配与转运',
         (METAB_COMPARTMENT_RE, METAB_METABOLITE_RE), METAB_TRANSPORT_RE,
         '转运蛋白或区室分离证据',
         '本主题 %d 条证据（%d 篇）涉及代谢物的亚细胞区室，但仅 %d 条涉及转运蛋白'
         '或直接的区室分离测量。多数"在液泡/质体中积累"的判断来自共定位或间接'
         '推论，区室间的实际分配比例与转运速率未被测定。',
         '非水相分离或同位素示踪给出区室浓度，转运蛋白突变体中分配比例发生'
         '可预测的改变',
         '区室标记与代谢物定位不一致，或转运蛋白突变不影响分配，'
         '说明原定位判断来自成像伪影或抗体交叉反应',
         ['%d 条涉及区室，%d 条有转运/分离证据', '缺少区室浓度的直接测量'],
         ['vacuole', 'plastid', 'transporter'],
         '液泡/质体分离 + 转运蛋白突变体 + 区室特异报告'),
    ]
    for key, framing, target, (rx_a, rx_b), gap_rx, gap_label, stmt, pt, pf, gaps, kw, detail in specs:
        if key in taken:
            continue
        evs = [ev for ev, s in texts if rx_a.search(s) and rx_b.search(s)]
        papers = {paper_key(e) for e in evs}
        gap_hits, gap_ok = _domain_gap(evs, gap_rx, gap_label)
        if (len(evs) < PATTERN_MIN_EV or len(papers) < PATTERN_MIN_PAPERS
                or not gap_ok):
            continue
        taken.add(key)
        _vals = (len(evs), len(papers), len(gap_hits))
        gaps = [_fill_counts(g, (len(evs), len(gap_hits))) for g in gaps]
        out.append(_mk_pattern(
            framing, target, '',
            stmt % (len(evs), len(papers), len(gap_hits)),
            pt, pf, evs, gaps,
            detail='%d 条证据 / %d 篇；%s %d 条'
                   % (len(evs), len(papers), gap_label, len(gap_hits)),
            keywords=list(kw),
        ))
    return out


def pattern_hormone_hypotheses(theme_id, items, taken):
    """激素主题：受体结合、互作上位性、剂量定量、蛋白周转四类真实缺口。"""
    if theme_id != 'hormone-signaling':
        return []
    out = []
    texts = [(ev, _ev_text(ev)) for ev in items]

    specs = [
        ('horm:receptor-binding', 'receptor-ligand-binding',
         '受体—配体结合的定量证据',
         HORM_RECEPTOR_RE, HORM_BINDING_ASSAY_RE,
         '结合常数或体外结合实验',
         '本主题 %d 条证据（%d 篇）提到受体，但仅 %d 条报告结合常数或体外结合实验。'
         '"受体感知该激素"因此多来自遗传学推断（受体突变体不响应），而非结合化学。'
         '缺少 Kd 与结合化学计量，就无法判断受体亚型的配体偏好，也无法解释'
         '跨物种剂量阈值差异。',
         '重组受体的 Kd 与体内响应 EC50 量级相容；结合位点突变体丧失结合且'
         '体内响应右移',
         '受体突变体表型来自通路组分的间接效应，重组受体无特异结合，'
         '说明原受体的配体归属被误判',
         ['%d 条提到受体，%d 条有结合实验', '缺少 Kd 与 EC50 的对应关系'],
         ['receptor', 'binding', 'ligand'],
         '重组受体 + ITC/SPR + 结合位点突变 + 体内剂量响应'),
        ('horm:crosstalk', 'crosstalk-epistasis',
         '激素互作的遗传上位性',
         HORM_MULTI_RE, HORM_EPISTASIS_RE,
         '双/多突变上位性实验',
         '本主题 %d 条证据（%d 篇）同时涉及两种以上激素，但仅 %d 条做过双突变或'
         '上位性分析。"协同/拮抗"在本库中多由平行处理的表型比较得出，'
         '两条通路在同一细胞内的先后关系与必要性未被区分。',
         '双突变效应显著偏离单突变效应的加和，上位性指数稳定；'
         '剂量矩阵显示响应面非加和',
         '双突变效应等于单突变加和，说明所谓互作只是两条独立通路作用于同一表型',
         ['%d 条涉及多激素，%d 条有上位性实验', '缺少同一遗传背景下的剂量矩阵'],
         ['crosstalk', 'synergy', 'antagonism'],
         '单/双/三突变 + 激素剂量矩阵 + 上位性指数'),
        ('horm:dose-quant', 'dose-response-quantitative',
         '外源激素处理的定量剂量—响应',
         HORM_EXOGENOUS_RE, HORM_GRADIENT_RE,
         '剂量梯度与 EC50',
         '本主题 %d 条证据（%d 篇）涉及外源激素处理，但仅 %d 条给出剂量梯度或'
         'EC50。单浓度处理只能判断"有响应"，无法区分亲和力差异、受体冗余与'
         '组织阈值差异，也无法在不同实验室之间比较敏感度。',
         '≥5 个剂量的响应曲线可拟合，EC50 在独立批次间可复现，'
         '受体突变体中曲线右移',
         '响应在测试浓度范围内始终饱和或始终无响应，说明所选浓度落在'
         '非生理区间，原结论不能外推到体内',
         ['%d 条外源处理，%d 条有剂量梯度', '缺少统一施加方式与取样时间'],
         ['exogenous', 'concentration', 'treated'],
         '≥5 剂量梯度 + EC50 拟合 + 受体突变体对照'),
        ('horm:turnover', 'protein-turnover',
         '信号蛋白的降解动力学',
         HORM_DEGRADATION_RE, HORM_TURNOVER_RE,
         '半衰期或降解速率测量',
         '本主题 %d 条证据（%d 篇）涉及泛素化或蛋白酶体降解，但仅 %d 条测量了'
         '半衰期或降解速率。"降解介导的信号关闭"因此缺少时间常数，'
         '无法与转录层面的变化区分先后。',
         'CHX 追踪给出可复现的半衰期；降解信号突变体半衰期显著延长，'
         '且下游响应持续时间相应延长',
         '半衰期不受降解信号突变影响，说明该蛋白的丰度主要由转录而非降解决定',
         ['%d 条涉及降解，%d 条有半衰期测量', '缺少降解速率与响应动力学的时间对齐'],
         ['ubiquitin', 'proteasome', 'degradation'],
         'CHX 追踪 + 泛素化检测 + 降解信号突变体'),
    ]
    for key, framing, target, rx_a, gap_rx, gap_label, stmt, pt, pf, gaps, kw, detail in specs:
        if key in taken:
            continue
        evs = [ev for ev, s in texts if rx_a.search(s)]
        papers = {paper_key(e) for e in evs}
        gap_hits, gap_ok = _domain_gap(evs, gap_rx, gap_label)
        if (len(evs) < PATTERN_MIN_EV or len(papers) < PATTERN_MIN_PAPERS
                or not gap_ok):
            continue
        taken.add(key)
        _vals = (len(evs), len(papers), len(gap_hits))
        gaps = [_fill_counts(g, (len(evs), len(gap_hits))) for g in gaps]
        out.append(_mk_pattern(
            framing, target, '',
            stmt % (len(evs), len(papers), len(gap_hits)),
            pt, pf, evs, gaps,
            detail='%d 条证据 / %d 篇；%s %d 条'
                   % (len(evs), len(papers), gap_label, len(gap_hits)),
            keywords=list(kw),
        ))
    return out


def pattern_method_hypotheses(theme_id, items, taken):
    """同组工具被并行使用、却从未在同一批数据上对照 -> 可执行的 benchmark。"""
    out = []
    texts = [(ev, _ev_text(ev)) for ev in items]
    for group, variants in METHOD_GROUPS.items():
        hits = {}
        for name, pat in variants.items():
            rx = re.compile(pat)
            evs = [ev for ev, t in texts if rx.search(t)]
            # 单个工具名在正文中出现得很少（实测 1-3 条），
            # 因此只要求"该工具被用到"，成簇门槛放在整个工具组上。
            if evs:
                hits[name] = evs
        if len(hits) < 2:
            continue
        names = sorted(hits, key=lambda k: -len(hits[k]))[:3]
        union = {}
        for n in names:
            for e in hits[n]:
                union[e['id']] = e
        evs = list(union.values())
        papers = len({paper_key(e) for e in evs})
        if papers < PATTERN_MIN_PAPERS or len(evs) < PATTERN_MIN_EV:
            continue
        key = 'benchmark:' + group
        if key in taken:
            continue
        taken.add(key)
        side_by_side = sum(1 for e in evs
                           if sum(1 for nm, pt in variants.items()
                                  if nm in names and re.search(pt, _ev_text(e))) >= 2)
        out.append(_mk_pattern(
            'method-sensitivity', group, '',
            '在%s组内，%s 都被用于支撑本主题结论，但在本知识库 %d 条相关证据中，'
            '仅 %d 条在同一断言内同时比较了两种以上实现；结论对实现选择的敏感性'
            '因此在现有文献中无法判定（受检索覆盖限制，需系统检索复核）。'
            '判别性检验：固定输入数据与预处理，只替换实现，比较效应量与显著性排名，'
            '并报告实现间分歧。'
            % (group, '、'.join(names), len(evs), side_by_side),
            '两种实现在留出数据上方向一致，关键对象的排名相关性高于预注册阈值',
            '两种实现的关键结论方向相反，或排名相关性低于阈值，说明原结论依赖实现',
            evs,
            ['本主题 %d 条证据涉及该组工具，其中 %d 条做过多实现对照' % (len(evs), side_by_side),
             '缺少统一数据与预注册指标，无法区分分歧来自数据还是实现'],
            detail='、'.join(names),
            keywords=list(variants.values()),
        ))
    return out


def _family_of(sym):
    """SKP2B->SKP2->SKP；WRKY40->WRKY。取前导字母，至少 3 个才视为家族名。"""
    s = re.sub(r'[^A-Za-z0-9]', '', sym or '')
    m = re.match(r'^([A-Za-z]{3,}?)\d+[A-Za-z]?$', s)
    if m:
        return m.group(1).upper()
    return ''


def pattern_family_hypotheses(theme_id, items, taken):
    """同家族多个成员分别被提名、却无人同时操纵 -> 冗余度可检验。"""
    fam_members = defaultdict(set)
    fam_evs = defaultdict(list)
    for ev in items:
        for g in candidate_genes(ev):
            fam = _family_of(g)
            if not fam:
                continue
            fam_members[fam].add(g)
            fam_evs[fam].append(ev)
    out = []
    ranked = sorted(fam_members, key=lambda k: -len(fam_members[k]))
    for fam in ranked:
        members = sorted(fam_members[fam])
        if len(members) < 2:
            continue
        evs = {e['id']: e for e in fam_evs[fam]}
        evs = list(evs.values())
        papers = len({paper_key(e) for e in evs})
        if len(evs) < PATTERN_MIN_EV or papers < PATTERN_MIN_PAPERS:
            continue
        key = 'family:' + fam
        if key in taken:
            continue
        taken.add(key)
        shown = '、'.join(members[:4])
        n_multi = _count_re(evs, MULTI_MUT_RE)
        out.append(_mk_pattern(
            'family-redundancy', fam, '',
            '%s家族在本主题内有 %d 个成员（%s）分别被提名参与同一过程；'
            '在 %d 条相关证据中仅 %d 条涉及双/多突变，家族内功能冗余与剂量补偿'
            '因此未被定量刻画（受检索覆盖限制，需系统检索复核）。'
            '判别性检验：构建双突变与三突变体，比较单突变与多突变的表型强度，'
            '并测定单突变体中同源成员的表达补偿。'
            % (fam, len(members), shown, len(evs), n_multi),
            '多突变体表型显著强于单突变，且单突变体中同源成员表达上调（补偿成立）',
            '多突变体与单突变表型相当、同源成员表达不变，说明成员功能已分化',
            evs,
            ['成员证据分散在不同论文，%d 条中仅 %d 条做过双/多突变' % (len(evs), n_multi),
             '家族成员间的表达补偿缺少同遗传背景下的并行测定'],
            species=resolve_species(evs, members[0]),
            detail=shown,
            keywords=[m.lower() for m in members[:4]],
        ))
        if len(out) >= 2:
            break
    return out


def pattern_process_hypotheses(theme_id, items, taken):
    """同一过程多物种被观察、因果操纵只在单一物种 -> 保守性可检验。"""
    proc_evs = defaultdict(list)
    for ev in items:
        _genes, procs = _anchors(ev)
        for p in procs:
            proc_evs[p].append(ev)
    out = []
    for proc, evs in sorted(proc_evs.items(),
                            key=lambda kv: -len({paper_key(e) for e in kv[1]})):
        papers = {paper_key(e) for e in evs}
        if len(evs) < PATTERN_MIN_EV or len(papers) < PATTERN_MIN_PAPERS:
            continue
        sp_counter = Counter((e.get('primary_species') or '') for e in evs)
        sp_counter.pop('', None)
        species = paper_species(evs)
        if len(species) < 2 or not sp_counter:
            continue
        dom, dom_n = sp_counter.most_common(1)[0]
        if float(dom_n) / max(1, len(evs)) > 0.7:
            continue
        # 激素/小分子没有"同源基因"，不能套"跨物种保守 + 互补"框架。
        if _is_small_molecule(proc):
            continue
        key = 'process:' + proc.lower()
        if key in taken:
            continue
        taken.add(key)
        out.append(_mk_pattern(
            'process-conservation', proc, '',
            '"%s" 在本主题内已有 %d 篇论文、%d 个主要研究物种的证据，但 %d 条证据中有 %d 条'
            '来自 %s；该过程在其他物种中是否由同一调控逻辑驱动，现有文献无法判定。'
            '判别性检验：在第二个物种中操纵同源因子，用同一读出量化该过程，'
            '并做跨物种互补。'
            % (proc, len(papers), len(species), len(evs), dom_n, dom),
            '第二物种中同源因子的操纵产生方向一致的效应，跨物种互补可恢复表型',
            '第二物种中操纵无效或方向相反，说明该过程的调控逻辑发生了谱系特异分化',
            evs,
            ['%d 个物种中出现该过程，但 %d 条证据来自 %s，其余物种仅有观察性描述'
             % (len(species), dom_n, dom),
             '缺少跨物种的同源操纵与统一读出'],
            species=dom,
            detail='、'.join(sorted(species)[:4]),
            keywords=[proc.lower()],
        ))
        if len(out) >= 2:
            break
    return out


def pattern_dose_hypotheses(theme_id, items, taken):
    """激素/小分子主题：外源剂量—响应曲线在多物种间是否可迁移。

    为什么单列：这类实体不是基因，没有"同源基因互补"可言；真正可检验的
    是剂量—响应关系（EC50）与受体特异性，因此必须有独立的生成器与设计表。
    """
    if theme_id not in ('hormone-signaling', 'metabolism-natural-products',
                        'stress-immunity', 'developmental-biology'):
        return []
    ent_evs = defaultdict(list)
    for ev in items:
        for p in _anchors(ev)[1]:
            if _is_small_molecule(p):
                ent_evs[p].append(ev)
    out = []
    used_quotes = set()
    for ent, evs in sorted(ent_evs.items(),
                           key=lambda kv: -len({paper_key(e) for e in kv[1]})):
        papers = {paper_key(e) for e in evs}
        if len(evs) < PATTERN_MIN_EV or len(papers) < PATTERN_MIN_PAPERS:
            continue
        sp_counter = Counter((e.get('primary_species') or '') for e in evs)
        sp_counter.pop('', None)
        for bad in ARTIFACT_SPECIES:
            sp_counter.pop(bad, None)
        species = paper_species(evs)
        if not sp_counter or len(species) < 2:
            continue
        dom, dom_n = sp_counter.most_common(1)[0]
        key = 'dose:' + ent.lower()
        if key in taken:
            continue
        taken.add(key)
        n_grad = _count_re(evs, GRADIENT_RE)
        out.append(_mk_pattern(
            'dose-response', ent, '',
            '"%s" 在本主题 %d 篇论文、%d 个主要研究物种中被报道，其中 %d 条证据来自 %s；'
            '%d 条证据中仅 %d 条报告了浓度梯度或剂量—响应参数，因此剂量—响应关系'
            '的定量可比性不足（受检索覆盖限制，需系统检索复核）。判别性检验：'
            '外源施加 ≥5 个浓度梯度并配合合成抑制剂，拟合剂量—响应曲线与 EC50，'
            '再在受体突变体中检验曲线是否右移。'
            % (ent, len(papers), len(species), dom_n, dom, len(evs), n_grad),
            '同一响应在两个物种中给出方向一致、EC50 差异 <1 个数量级的剂量—响应曲线，'
            '且受体突变体中曲线右移',
            'EC50 跨物种相差 >2 个数量级，或受体突变体中曲线不移位，'
            '说明该激素的响应阈值由谱系特异的受体组成决定',
            evs,
            ['%d 条证据中仅 %d 条给出浓度梯度或 EC50' % (len(evs), n_grad),
             '缺少跨物种统一施加方式与统一读出，无法比较响应阈值'],
            species=dom,
            detail='、'.join(sorted(species)[:4]),
            keywords=[ent],
            avoid=used_quotes,
        ))
        used_quotes.add(out[-1].get('quote_id') or '')
        if len(out) >= 2:
            break
    return out


ASSEMBLY_RE = re.compile(
    r'assembly|assembled|scaffold|contig|\bn50\b|chromosome-level|hi-?c', re.I)


# 组织/细胞身份同义词组：同一解剖学身份在不同论文中被独立注释。
IDENTITY_GROUPS = {
    '表皮': (r'\bepidermis\b', r'\bepidermal\b'),
    '叶肉': (r'\bmesophyll\b',),
    '木质部': (r'\bxylem\b',),
    '韧皮部': (r'\bphloem\b',),
    '内皮层': (r'\bendodermis\b',),
    '中柱': (r'\bstele\b',),
    '皮层': (r'\bcortex\b', r'\bcortical\b'),
    '分生组织': (r'\bmeristem\b', r'\bmeristematic\b'),
    '原形成层': (r'\bprocambium\b',),
    '伴胞': (r'\bcompanion\s+cell\b',),
    '根毛': (r'\broot\s+hair\b',),
    '绒毡层': (r'\btapetum\b',),
}


def pattern_identity_hypotheses(theme_id, items, taken):
    """同一解剖学身份被多篇论文独立注释，但标记集与边界定义不共享
    -> 跨数据集标签可迁移性可检验。"""
    if theme_id not in ('single-cell-spatial-omics', 'developmental-biology'):
        return []
    out = []
    for ident, pats in IDENTITY_GROUPS.items():
        evs = [e for e in items
               if any(re.search(p, _ev_text(e)) for p in pats)]
        papers = {paper_key(e) for e in evs}
        if len(papers) < 2 or len(evs) < PATTERN_MIN_EV:
            continue
        species = paper_species(evs)
        if len(species) < 2:
            continue
        key = 'identity:' + ident
        if key in taken:
            continue
        taken.add(key)
        out.append(_mk_pattern(
            'annotation-consistency', '%s细胞身份' % ident, '',
            '“%s”在本主题的 %d 篇论文（%d 个主要研究物种）中都被独立注释，但各研究使用'
            '不同的标记基因集与聚类参数，同一身份是否指向同一细胞群体未知。'
            '判别性检验：以其中一套标记集为参照，对另一数据集做标签转移，'
            '再用独立标记与空间位置做正交验证。'
            % (ident, len(papers), len(species)),
            '标签转移后 %s 与参照注释高度重合，且被独立标记与空间位置共同支持' % ident,
            '标签转移后 %s 与参照注释大面积错配，说明同名身份实为不同细胞群体' % ident,
            evs,
            ['%d 篇论文各自定义 %s，缺少共享标记集与统一聚类参数' % (len(papers), ident),
             '同名身份的跨数据集一致性缺少定量评估；%d 条证据中仅 %d 条涉及标签转移或整合'
             % (len(evs), _count_re(evs, LABELTRANS_RE))],
            species=sorted(species)[0],
            detail='、'.join(sorted(species)[:4]),
            design='至少两个独立数据集（不同物种或不同平台），同一组织部位',
            manip='注释方案（参照标记集 vs 目标数据集自有注释），唯一变量',
            readout='标签转移一致率、独立标记阳性率、空间位置吻合度',
            keywords=[ident],
        ))
        if len(out) >= 2:
            break
    return out


def pattern_assembly_hypotheses(theme_id, items, taken):
    """组装连续性 vs 结论稳健性：碎片化组装是否会改变基因家族/共线性结论。"""
    if theme_id not in ('genomics-evolution', 'methods-tools'):
        return []
    evs = [e for e in items if ASSEMBLY_RE.search(_ev_text(e))]
    papers = {paper_key(e) for e in evs}
    if len(evs) < PATTERN_MIN_EV or len(papers) < PATTERN_MIN_PAPERS:
        return []
    key = 'assembly:contiguity'
    if key in taken:
        return []
    taken.add(key)
    sp = Counter((e.get('primary_species') or '') for e in evs)
    sp.pop('', None)
    dom = sp.most_common(1)[0][0] if sp else ''
    return [_mk_pattern(
        'assembly-contiguity', '组装连续性', '',
        '本主题 %d 篇论文的组装相关结论依赖各自的组装版本；%d 条相关证据中仅 %d 条'
        '对组装连续性本身做过敏感性分析。把同一份染色体级组装人工打断到 contig 级后，'
        '基因家族拷贝数、共线性区块与旁系同源分组是否稳定，现有文献无法判定'
        '（受检索覆盖限制，需系统检索复核）。'
        '判别性检验：对同一组装做梯度碎片化，重跑注释与家族推断，比较结论。'
        % (len(papers), len(evs), _count_re(evs, FRAGMENT_RE)),
        '梯度碎片化后基因家族拷贝数与共线性区块保持稳定，仅边界精度下降',
        '碎片化后拷贝数或共线性结论发生系统性改变，说明原结论依赖组装质量',
        evs,
        ['组装类结论分散在 %d 篇论文中，但无统一的碎片化敏感性测试' % len(papers),
         '缺少"同一数据、不同连续性"的对照，无法区分生物学信号与组装伪影'],
        species=dom,
        detail='%d 篇论文' % len(papers),
        design='同一份染色体级组装 + 梯度碎片化版本（contig/scaffold 级）',
        manip='组装连续性（唯一变量），注释与家族推断流程保持不变',
        readout='基因家族拷贝数、共线性区块数、旁系同源分组的一致性',
        keywords=['assembly', 'assembled', 'contig', 'scaffold'],
    )]


def pattern_annotation_hypotheses(theme_id, items, taken):
    """单细胞主题专用：同一组织的细胞类型划分粒度不一致 -> 注释稳定性可检验。"""
    if theme_id != 'single-cell-spatial-omics':
        return []
    evs = []
    nums = set()
    for ev in items:
        m = CELLTYPE_NUM_RE.search(_ev_text(ev))
        if m:
            evs.append(ev)
            nums.add(int(m.group(1)))
    papers = len({paper_key(e) for e in evs})
    if len(nums) < 2 or len(evs) < PATTERN_MIN_EV or papers < PATTERN_MIN_PAPERS:
        return []
    key = 'annotation:celltype'
    if key in taken:
        return []
    taken.add(key)
    return [_mk_pattern(
        'annotation-consistency', '细胞类型注释', '',
        '同一组织在本主题的 %d 篇研究中被划分为 %s 个细胞类型，划分粒度不一致；'
        '跨数据集标签转移能否收敛到稳定类型集合未知。判别性检验：用统一标记基因集'
        '与标签转移对同一批数据重注释，用 bootstrap 报告类型数的稳定性。'
        % (papers, '/'.join(str(n) for n in sorted(nums))),
        '重注释后类型数在不同重采样间稳定，且与原始注释的主要类型一一对应',
        '类型数随重采样大幅波动，或主要类型无法对应，说明原划分依赖聚类参数',
        evs,
        ['各研究使用不同标记集与聚类参数，类型数不可直接比较',
         '缺少跨数据集的标签转移与稳定性评估'],
        detail='类型数 %s' % '/'.join(str(n) for n in sorted(nums)),
        keywords=['cell type', 'cell types', 'clusters'],
    )]


# 这些问题的主语不是某个基因，而是"证据设计"本身（结合实验、通量测量、
# 上位性设计……）。它们与基因中心假说共用同一批文献是合理的：同一批论文
# 既可能支持"某基因影响某性状"，也可能暴露"从未做过结合实验"。因此只与
# 同类设计型假说去重，不与基因假说互相吞并。
_DESIGN_FRAMINGS = frozenset([
    'regulatory-linkage', 'flux-attribution', 'enzyme-kinetics',
    'compartment-transport', 'receptor-ligand-binding', 'crosstalk-epistasis',
    'dose-response-quantitative', 'protein-turnover',
    'method-sensitivity', 'dissociation-artifact', 'spatial-validation',
    'trajectory-robustness', 'marker-specificity', 'assembly-contiguity',
])


def _dedupe_patterns(pats, overlap=0.8, existing=()):
    """去掉证据集高度重叠的假说：同一批证据不能同时支撑两个不同论断。

    旧版实测出现过 CLV1→激素与 CLV 家族冗余共用完全相同的 6 条证据，
    等于用一次观察冒充两个独立发现。
    """
    kept = []
    for p in pats:
        ids = set(p.get('all_ids') or p.get('evidence_ids') or [])
        dup = False
        for k in list(kept) + list(existing):
            kids = set(k.get('all_ids') or k.get('evidence_ids') or [])
            if not ids or not kids:
                continue
            inter = len(ids & kids)
            frac = inter / float(min(len(ids), len(kids)))
            # 与簇级假说比对时更严：小集合须几乎完全被吞并才算重复，
            # 否则会把"借用同一批证据的另一类问题"误删。
            # 设计型假说 vs 基因型假说：问题不同，不做互相吞并。
            if (p.get('framing') in _DESIGN_FRAMINGS) != (
                    k.get('framing') in _DESIGN_FRAMINGS):
                continue
            need = 0.9 if (k in tuple(existing)) else overlap
            if inter >= 4 and frac >= need:
                dup = True
                break
        if not dup:
            kept.append(p)
    return kept


def _cluster_quote(cluster, target, obj):
    """簇级假说的示例断言：优先取同时提到主语与对象、且不是抽取残渣的句子。"""
    keys = [k.lower() for k in (target, obj) if k]
    q, qid = _pick_quote(cluster, keys)
    if not q:
        best = max((e['claim'] for e in cluster),
                   key=lambda c: (_claim_relevance(c, target, obj), -len(c)))
        return best[:300], ''
    return q, qid


def build_hypotheses(theme_id, items):
    """返回 (hypotheses, diagnostics)。

    diagnostics 记录"为什么没生成更多假说"，用于在页面上写证据不足声明，
    而不是像旧版那样靠调低门槛硬凑数量。单篇论文独占的断言单独列出，
    组成"待复现清单"——这本身就是有价值的产出。
    """
    clusters = cluster_evidence(items)
    hyps = []
    singles = []
    reasons = Counter()
    for cluster in clusters:
        h = build_hypothesis(cluster, theme_id)
        if h:
            hyps.append(h)
        else:
            papers = len({paper_key(e) for e in cluster})
            if papers < MIN_PAPERS_PER_HYPOTHESIS:
                reasons['仅单篇论文支撑（无法构成独立证据）'] += 1
                singles.extend(cluster)
            elif len(cluster) < MIN_EVIDENCE_PER_HYPOTHESIS:
                reasons['支撑证据不足 %d 条' % MIN_EVIDENCE_PER_HYPOTHESIS] += 1
            else:
                subj, kind = cluster_subject(cluster, theme_id)
                if subj and kind != 'gene' and theme_id not in (
                        'methods-tools', 'genomics-evolution'):
                    reasons['主语是泛化术语，不构成因果假说（已拒绝编造）'] += 1
                else:
                    reasons['未抽到可信实体（基因/共有短语）'] += 1
        # 2026-11-03 第 12 轮：代谢与激素的簇级假说多为"化合物类别 + 模板"，
        # 先给领域专用模式留出 3 个名额，避免簇级把 6 个位置占满。
        _cap = MAX_HYPOTHESES_PER_THEME
        if theme_id in ('metabolism-natural-products', 'hormone-signaling'):
            _cap = MAX_HYPOTHESES_PER_THEME - 3
        if len(hyps) >= _cap:
            break

    # 簇级证据不足时，用模式级生成器补齐：这类假说不依赖
    # "同一个基因被多篇论文反复研究"，因此能覆盖每篇论文研究不同基因的大主题。
    taken = set('gene:' + h['target'].lower() for h in hyps)
    if len(hyps) < MAX_HYPOTHESES_PER_THEME:
        pats = (pattern_metabolism_hypotheses(theme_id, items, taken)
                + pattern_hormone_hypotheses(theme_id, items, taken)
                + pattern_singlecell_hypotheses(theme_id, items, taken)
                + pattern_method_hypotheses(theme_id, items, taken)
                + pattern_identity_hypotheses(theme_id, items, taken)
                + pattern_family_hypotheses(theme_id, items, taken)
                + pattern_process_hypotheses(theme_id, items, taken)
                + pattern_dose_hypotheses(theme_id, items, taken)
                + pattern_assembly_hypotheses(theme_id, items, taken)
                + pattern_annotation_hypotheses(theme_id, items, taken))
        pats = _dedupe_patterns(pats, existing=hyps)
        for p in pats:
            if len(hyps) >= MAX_HYPOTHESES_PER_THEME:
                break
            hyps.append(p)

    diag = {
        'n_clusters': len(clusters),
        'largest_cluster': max([len(c) for c in clusters] or [0]),
        'reasons': reasons,
        'singles': singles,
        'type_dist': Counter(e.get('evidence_type') or 'unknown' for e in items),
        'insufficient': len(hyps) < MIN_HYPOTHESES_PER_THEME,
    }
    return hyps, diag


def render_insufficiency_section(theme_id, hyps, diag, n_evidence, n_papers):
    """证据不足声明 + 待复现清单（诚实产物，替代"硬凑假说"）。"""
    if not diag['insufficient']:
        return ''
    lines = [
        '## 证据不足声明（自动判定，不是敷衍）',
        '',
        '本主题当前只能支撑 **%d 条**可证伪假说（目标 %d 条）。'
        '脚本不会为了凑数而降低门槛，因此如实报告缺口：'
        % (len(hyps), MIN_HYPOTHESES_PER_THEME),
        '',
        '| 项目 | 值 |',
        '|---|---|',
        '| 主题内证据 | %d |' % n_evidence,
        '| 独立论文 | %d |' % n_papers,
        '| 形成的证据簇 | %d |' % diag['n_clusters'],
        '| 最大簇规模 | %d |' % diag['largest_cluster'],
        '',
    ]
    if diag['reasons']:
        lines += ['| 未成假说的原因 | 簇数 |', '|---|---|']
        for r, c in diag['reasons'].most_common():
            lines.append('| %s | %d |' % (r, c))
        lines.append('')

    lines += [
        '### 为什么会出现这种局面',
        '',
        '本主题证据中 `evidence_type` 高度集中于表达/关联类断言，且同一机制'
        '的证据分散在不同论文的不同表述里，缺少"同一基因 × 同一表型"的'
        '重复测量。要生成更多假说，缺的不是算法，而是**可比的重复证据**。',
        '',
        '### 补齐证据的具体做法（可直接落到检索式）',
        '',
        '1. 对每个候选机制追加检索式：`"<基因名>" AND ("mutant" OR "knockout" '
        'OR "overexpression" OR "CRISPR")`，把表达关联升级为遗传证据；',
        '2. 强制要求同一机制至少 2 篇独立论文（不同实验室或不同物种）；',
        '3. 方法学/工具类主题应改按"工具名 + benchmark + comparison"检索，'
        '而不是按生物学关键词，否则会把大量表达研究误并入该主题；',
        '4. 补采后在下一轮自动重算；本页会随证据增长自动升级。',
        '',
    ]

    if diag['singles']:
        seen, rows = set(), []
        for e in sorted(diag['singles'], key=lambda x: -len(x['claim'])):
            if e['id'] in seen:
                continue
            seen.add(e['id'])
            rows.append('| `%s` | %s | %s |'
                        % (e['id'], e.get('doi') or '—',
                           _clip(' '.join(e['claim'].split()), 110).replace('|', '/')))
            if len(rows) >= 12:
                break
        lines += ['### 待复现清单（单篇论文独占的断言，优先补重复）', '',
                  '| 证据 ID | DOI | 断言（截断） |', '|---|---|---|'] + rows + ['']
    return '\n'.join(lines)



# ============================================================
# 落盘
# ============================================================
def _evidence_bullets(h, limit=6):
    return '\n'.join('- `%s`%s' % (eid, '')
                     for eid in h['evidence_ids'][:limit])


# ── 主题特异读出词表（2026-11-03）────────────────────────────────────
# 目的：区分"领域内可执行的读出"与"任何主题都能套的通用水位"。
# 判据只用于**标注**，不改变假说门槛：命中为零的假说照常输出，
# 但在页面上明确标为"通用模板，需人工改写"，避免读者误以为是领域方案。
THEME_READOUTS = {
    'single-cell-spatial-omics': [
        r'标签转移', r'注释一致', r'聚类分辨', r'细胞类型比例', r'marker|标记基因',
        r'空间(定位|共定位|映射)', r'解离偏好|核偏好', r'批次|平台(偏差|一致)',
        r'scrna|snrna|spatial|单细胞', r'umap|leiden|louvain',
    ],
    'developmental-biology': [
        r'分生组织|茎尖|根尖', r'器官原基|原基', r'细胞分裂(面|率)', r'细胞命运|分化',
        r'茎尖|花芽|叶序', r'原位杂交|组织切片', r'共聚焦|显微', r'再生|愈伤',
    ],
    'metabolism-natural-products': [
        r'lc-?ms|gc-?ms|hplc|质谱|色谱', r'代谢(组|物)含量|含量测定', r'酶活|动力学|km|kcat',
        r'底物特异', r'异源表达|体外酶促', r'途径|合成酶|糖基转移酶|p450',
    ],
    'hormone-signaling': [
        r'受体(结合|亲和)|配体', r'磷酸化|激酶', r'剂量|浓度梯度|ec50',
        r'响应元件|启动子|转录激活', r'突变体|敲除|过表达', r'激素(含量|水平)测定',
    ],
    'stress-immunity': [
        r'活性氧|ros|氧化爆发', r'病斑|病情指数|菌量|cfu', r'抗性(评价|鉴定)|接种',
        r'免疫(反应|信号)|ptI|etI', r'电解质渗漏|丙二醛|叶绿素荧光', r'效应子|无毒基因',
    ],
    'epigenetics-gene-regulation': [
        r'atac|chip|cut&?tag|dnase', r'峰(质量|分布)|peak', r'dna甲基化|bs-seq|wgbS',
        r'组蛋白修饰|h3k\d+|h4k\d+', r'染色质(可及|构象)|hi-c', r'多梳|polycomb',
    ],
    'methods-tools': [
        r'基准|benchmark', r'消融|ablation', r'敏感性分析', r'运行时间|内存|cpu',
        r'准确率|f1|auc|召回|精确率', r'可重复|复现', r'容器|docker|版本',
    ],
    'genomics-evolution': [
        r'组装(连续性|质量)|contig|scaffold|ng50', r'busco|lai|qv', r'共线性|synteny',
        r'基因家族(扩张|收缩)|拷贝数', r'选择(清除|信号)|fst|pi|tajima', r'系统发育|分化时间',
        r'重测序|gwas|snp',
    ],
}


# 非模式（基因中心）假说的"数据/体系 + 操纵变量 + 对照"三段，
# 旧版对所有主题都写"敲除/敲低与过表达 + 野生型 + 空载体"，
# 对单细胞注释、方法学基准、基因组组装三类主题完全不成立。
THEME_DESIGN = {
    'single-cell-spatial-omics': {
        'system': '同一组织在 >=2 个独立数据集（不同物种/平台/实验室）中的注释结果',
        'manip': '注释方案与聚类参数（参照标记集 vs 数据集自有注释），或细胞类型特异扰动',
        'control': '同一批数据换用第二套标记集/第二平台复核，作为内部对照',
        'readout': '细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位',
    },
    'methods-tools': {
        'system': '固定 >=3 个公开数据集 + 统一预处理与评价脚本',
        'manip': '待评估实现（唯一变量）：本方法 vs >=2 个现行方法，含消融版本',
        'control': '预注册指标与随机种子固定；数据集层面留一验证',
        'readout': '基准指标（准确率/F1/AUC）、运行时间与内存、消融前后差值',
    },
    'genomics-evolution': {
        'system': '同物种 >=2 份独立组装/重测序数据，含近缘外类群',
        'manip': '组装连续性、注释流程、或群体分组（唯一变量）',
        'control': '不同组装版本互为对照；群体结构作协变量',
        'readout': 'contig NG50/BUSCO/LAI、共线性区块、Fst/pi/Tajima D、分化时间',
    },
    'epigenetics-gene-regulation': {
        'system': '同组织、同发育期的染色质图谱 + 转录组，生物学重复 >=2',
        'manip': '目标因子扰动（敲除/诱导降解）或修饰酶抑制剂',
        'control': '输入对照（input/IgG）与非靶向对照 sgRNA',
        'readout': '峰质量与分布、差异可及性、H3K27me3/H3K4me3 富集、靶基因表达',
    },
    'developmental-biology': {
        'system': '同物种、同遗传背景、同生育期的突变体与野生型材料（>=2 个独立株系）',
        'manip': '{t} 的敲除/敲低、过表达或诱导型表达（{o}相关发育表型）',
        'control': '野生型 + 空载体/非靶向 sgRNA 转化体，同批播种',
        'readout': '分生组织/器官原基大小与细胞分裂面、原位杂交定位、花期与叶序',
    },
    'metabolism-natural-products': {
        'system': '同物种、同发育期材料；必要时用异源宿主（酵母/大肠杆菌）表达体系',
        'manip': '{t} 的敲除/敲低、过表达，或体外酶促反应（底物浓度梯度）',
        'control': '野生型 + 空载体；体外反应设热失活酶与无底物对照',
        'readout': 'LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性',
    },
    'hormone-signaling': {
        'system': '同物种、同生育期突变体与野生型；外源激素处理梯度',
        'manip': '{t} 的敲除/敲低、过表达，或受体/激酶活性突变体',
        'control': '野生型 + 空载体；溶剂 mock 处理',
        'readout': '激素含量、响应元件驱动报告基因、磷酸化状态、剂量—响应 EC50',
    },
    'stress-immunity': {
        'system': '同物种、同生育期材料；标准化接种/胁迫处理（>=3 生物学重复）',
        'manip': '{t} 的敲除/敲低、过表达，或效应子/无毒基因组合',
        'control': '野生型 + 空载体；mock 接种与未胁迫对照',
        'readout': '病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达',
    },
}


def _design_triplet(theme_id, h):
    """非模式假说的 体系/操纵/对照/读出。

    设计词表按主题给出，不再依赖"假说正文是否恰好命中读出词"来决定是否使用。
    正文是由证据模板拼出的基因级陈述，天然不含 LC-MS、BUSCO 这类读出词，
    用命中与否做闸门会让除激素外的主题全部回退到"敲除/过表达 + 野生型 + 空载体"，
    这正是上一版被判为模板化的原因。是否领域特异改由主题归属决定。
    """
    d = THEME_DESIGN.get(theme_id)
    obj = _object_zh(h.get('object')) if h.get('object') else '目标表型/过程'
    if d:
        return (d['system'].format(t=h['target'], o=obj),
                d['manip'].format(t=h['target'], o=obj),
                d['control'].format(t=h['target'], o=obj),
                d['readout'].format(t=h['target'], o=obj))
    return ('%s 的同遗传背景材料（同生育期、同环境）' % h['target'],
            '%s 的敲除/敲低与过表达（至少 2 个独立株系）' % h['target'],
            '野生型 + 空载体转化体',
            '经注释的定量读出（表达/蛋白/表型至少两项）')


def specificity(theme_id, h):
    """返回 (label, hits)。

    label 由"该主题是否登记了专用设计/读出词表"决定；hits 只用于展示
    这条假说的正文里恰好出现了哪些本主题读出词，供人工快速判断。
    """
    d = THEME_DESIGN.get(theme_id)
    if not d:
        return 'generic', []
    pats = THEME_READOUTS.get(theme_id) or []
    text = ' '.join(str(h.get(k) or '') for k in
                    ('statement', 'readout', 'manip', 'design', 'detail',
                     'object', 'target', 'pred_true', 'pred_false'))
    hits = []
    for pat in pats:
        m = re.search(pat, text, re.I)
        if m and m.group(0) not in hits:
            hits.append(m.group(0))
    return 'domain', hits[:4]


def _spec_line(theme_id, h):
    label, hits = specificity(theme_id, h)
    d = THEME_DESIGN.get(theme_id)
    if label == 'domain':
        # 2026-11-03 第 12 轮：模式假说自带针对该问题的读出（如"结合常数"、
        # "上位性指数"），比主题级常量更准确；只有缺省时才回落到主题词表。
        own = (h.get('readout') or '').strip()
        line = '领域特异读出：%s' % (own or d['readout'])
        if hits:
            line += '（本条正文命中：%s）' % '、'.join(hits)
        return line
    return ('**缺省回退方案**（该主题未登记专用设计词表）。该条只能说明缺什么，'
            '不构成可执行方案。')


def render_hypotheses_page(theme_id, hyps, n_evidence, n_papers, basis, diag=None):
    title = th.display_title(theme_id)
    title_zh = th.display_title(theme_id, 'zh')
    blocks = []
    for i, h in enumerate(hyps, 1):
        gap_md = ''.join('\n- %s' % g for g in h['gaps']) or '\n- （未识别到明显缺口）'
        gap_md = gap_md.lstrip('\n')
        head = h['target'] + (' → ' + _object_zh(h['object']) if h.get('object') else '')
        framing_zh = _FRAMING_ZH.get(h.get('framing') or '', '')
        if h.get('pattern'):
            test_table = ('| 要素 | 内容 |\n|---|---|\n'
                          '| 数据/体系 | %s |\n'
                          '| 操纵或比较变量 | %s |\n'
                          '| 读出 | %s |\n'
                          '| 若假说为真 | %s |\n'
                          '| 若假说为假 | %s |'
                          % (h.get('design') or '见假说正文',
                             h.get('manip') or '见假说正文',
                             h.get('readout') or '预注册的定量指标',
                             h['pred_true'], h['pred_false']))
        else:
            d_sys, d_manip, d_ctrl, d_read = _design_triplet(theme_id, h)
            test_table = ('| 要素 | 内容 |\n|---|---|\n'
                          '| 数据/体系 | %s |\n'
                          '| 操纵或比较变量 | %s |\n'
                          '| 对照 | %s |\n'
                          '| 读出 | %s（至少两项独立读出交叉验证） |\n'
                          '| 若假说为真 | %s |\n'
                          '| 若假说为假 | %s |'
                          % (d_sys, d_manip, d_ctrl, d_read,
                             h['pred_true'], h['pred_false']))
        blocks.append("""### H%d：%s%s

**假说**：%s

**为什么值得做（证据缺口）**

%s

**可证伪检验**
%s

**证据基础**：%d 条证据 / %d 篇独立论文（置信度：%s）
%s

**领域特异性**：%s

**原始断言（摘自证据页，供核对）**
> %s
> <sub>来源：`%s`</sub>

""" % (i, head, ('（%s）' % framing_zh) if (framing_zh and framing_zh not in head) else '',
       h['statement'], gap_md.strip(), test_table,
       h['support_evidence'], h['support_papers'], h['confidence'],
       _evidence_bullets(h), _spec_line(theme_id, h),
       h['core_claim'] or '（该组证据的断言均为图表/标题碎片，未摘录）',
       h.get('quote_id') or '—'))

    body = '\n'.join(blocks)
    n_domain = sum(1 for h in hyps if specificity(theme_id, h)[0] == 'domain')
    n_generic = len(hyps) - n_domain
    insufficiency = render_insufficiency_section(theme_id, hyps, diag, n_evidence, n_papers) if diag else ''
    return """---
title: "Hypotheses: %s"
title_zh: "%s：可证伪假说"
type: hypothesis
topic: "%s"
theme_basis: "%s"
total_evidence: %d
total_papers: %d
total_hypotheses: %d
specificity_domain: %d
specificity_generic: %d
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: %s
---

# 💡 %s — 可证伪假说（%d 条）

> 生成口径：主题内 %d 条证据 / %d 篇独立论文（主题归属依据：%s）。
> 每条假说只在"≥%d 条证据且 ≥%d 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | %s |
| 证据条目 | %d |
| 独立论文 | %d |
| 生成假说 | %d |
| 其中主题专用方案 | %d |
| 其中缺省回退方案（需改写） | %d |
| 主题归属依据 | %s |

%s

%s

## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 %s；生成器版本 2026-11-02-evidence-grounded*
""" % (title, title_zh, theme_id, basis, n_evidence, n_papers, len(hyps),
       n_domain, n_generic, TODAY,
       title, len(hyps), n_evidence, n_papers,
       '证据标签' if basis == 'tag' else '关键词兜底',
       MIN_EVIDENCE_PER_HYPOTHESIS, MIN_PAPERS_PER_HYPOTHESIS,
       title, n_evidence, n_papers, len(hyps), n_domain, n_generic,
       '证据标签' if basis == 'tag' else '关键词兜底',
       body, insufficiency, TODAY)


def _sc_aim_plan(h, t, d):
    """单细胞四条领域假说的最小可行方案（不套用遗传转化模板）。"""
    fr = h.get('framing')
    if fr == 'dissociation-artifact':
        return {
            'title': '同一样本分半比较原生质体与细胞核建库',
            'system': '同一组织的同一样本分半，两半处理条件一致（同株系、同生育期）',
            'materials': '配对的两套文库（原生质体 / 细胞核）+ 统一标记集与聚类参数（%s）' % d,
            'steps': ['同一样本分半，一半酶解原生质体、一半提取细胞核',
                      '两套文库在同一流程下建库、比对、过滤与聚类',
                      '以核法结果为参照，计算每类的比例偏差与类型级召回',
                      '对偏差最大的类型用原位或空间数据裁定哪一方更接近真实构成',
                      '报告偏差随酶解时间或渗透压的变化曲线'],
            'period': '6-12 个月',
        }
    if fr == 'spatial-validation':
        return {
            'title': '在两个独立空间数据集上核实细胞类型的空间位置',
            'system': '同一组织的 >=2 个独立空间转录组数据集（尽可能含两个平台）',
            'materials': '统一标记集与标签转移模型；两个平台的分辨率与捕获效率参数（%s）' % d,
            'steps': ['用同一标记集对空间数据做类型级去卷积或注释',
                      '把单细胞注释映射到空间坐标，得到类型—位置矩阵',
                      '在两个数据集间比较类型的层/区分布与邻域富集',
                      '对不一致的类型回到原始切片核查组织形态',
                      '输出"可空间复现"与"仅单数据集成立"两张类型清单'],
            'period': '6-12 个月',
        }
    if fr == 'trajectory-robustness':
        return {
            'title': '同一数据上比较多种轨迹推断的分支拓扑',
            'system': '同一份预处理后的表达矩阵（同基因过滤、同归一化）',
            'materials': '>=3 种推断实现与统一的评价脚本（%s）' % d,
            'steps': ['固定预处理，分别运行各实现并记录分支数与分支点',
                      '用 bootstrap 重采样评估分支拓扑的稳定性',
                      '比较各实现给出的分支点上调基因集合的重叠',
                      '用独立时间序列或标记染色数据做外部校准',
                      '公布对实现稳健的分支与依赖实现的伪时间排序'],
            'period': '3-6 个月',
        }
    if fr == 'marker-specificity':
        return {
            'title': '标记基因特异性的跨数据集与原位双重验证',
            'system': '原报道数据集 + 一个独立数据集（不同实验室或平台）',
            'materials': '原报道标记集与收窄后的候选集；原位或空间数据作裁定（%s）' % d,
            'steps': ['逐基因统计在非目标类型中的表达与检出率',
                      '在独立数据集中重算类型判别 AUC 与泄漏率',
                      '对高风险标记基因做原位杂交或空间定位核实',
                      '按泄漏率重新排序标记集，去掉只在训练集有效的基因',
                      '给出该类型的最小充分标记组合'],
            'period': '6-12 个月',
        }
    return None


def _pattern_aim_plan(h):
    """模式级假说的实践方案：benchmark / 多突变 / 跨物种 / 重注释。"""
    fr = h.get('framing')
    t = h['target']
    d = h.get('detail') or t
    _sc = _sc_aim_plan(h, t, d)
    if _sc:
        return _sc
    if fr == 'method-sensitivity':
        return {
            'title': 'benchmark：%s 组内实现的结论一致性' % t,
            'system': '>=2 个公开数据集的留出集（不参与任何调参）',
            'materials': '%s 的并行运行环境与统一评价指标' % d,
            'steps': ['固定输入数据与预处理，只替换实现',
                      '比较效应量、显著性排名与关键对象的方向',
                      '用 bootstrap 报告实现间分歧的置信区间',
                      '按预注册阈值判定原结论是否稳健'],
            'period': '3-6 个月',
        }
    if fr == 'family-redundancy':
        sp = h.get('species') or '原报道物种'
        return {
            'title': '检验 %s 家族的功能冗余' % t,
            'system': '%s，对照同遗传背景、同生育期' % sp,
            'materials': '%s 的单突变、双突变与三突变系（成员：%s）' % (t, d),
            'steps': ['获得各成员的单突变系并确认操纵有效',
                      '构建双突变与三突变系',
                      '比较单突变与多突变的表型效应量',
                      '测定单突变体中同源成员的表达，判断是否存在剂量补偿'],
            'period': '18-24 个月',
        }
    if fr == 'assembly-contiguity':
        return {
            'title': '检验组装连续性对结论的影响',
            'system': '同一份染色体级组装的梯度碎片化版本',
            'materials': '原始组装 + contig 级/scaffold 级模拟版本（%s）' % d,
            'steps': ['按预设梯度把组装打断到不同连续性',
                      '在每份版本上重跑同一套注释与家族推断',
                      '比较基因家族拷贝数、共线性区块与分组结果',
                      '报告结论随连续性变化的敏感度曲线'],
            'period': '3-6 个月',
        }
    if fr == 'regulatory-linkage':
        return {
            'title': '把 %s 从表达相关推进到直接结合' % t,
            'system': '原报道物种；同遗传背景、同生育期、同组织部位',
            'materials': '候选 TF 的诱导型敲低/敲除系、靶启动子报告系统、'
                         '结合位点突变版启动子（%s）' % d,
            'steps': ['用 ChIP-seq 或 CUT&Tag 定位体内结合位点',
                      '对候选位点做 EMSA 与染色质免疫沉淀 qPCR 验证',
                      '双荧光素酶报告系统检验结合位点突变后的转录变化',
                      '在 tf 突变体与回补系中定量靶基因转录与代谢物含量',
                      '按时间序列确定"结合—转录—代谢物"的先后'],
            'period': '12-18 个月',
        }
    if fr == 'flux-attribution':
        return {
            'title': '分解 %s 的合成、降解与转运' % t,
            'system': '原报道物种；同一组织、同一生育期，标记喂养条件一致',
            'materials': '13C/14C 标记喂养体系、目标基因操纵系、'
                         '代谢物绝对定量方法（%s）' % d,
            'steps': ['建立标记喂养与绝对定量流程并做回收率校正',
                      '在目标基因操纵系中测标记掺入速率（合成通量）',
                      '用脉冲—追踪估算降解速率常数',
                      '测定组织外排或区室转运速率',
                      '把稳态含量变化分解为三者贡献，判定限速步骤'],
            'period': '12-24 个月',
        }
    if fr == 'enzyme-kinetics':
        return {
            'title': '测定 %s 的体外动力学与底物特异性' % t,
            'system': '异源表达系统（大肠杆菌/酵母/本氏烟草）',
            'materials': '候选酶与同家族成员的表达构建、'
                         '底物类似物库、纯化标签（%s）' % d,
            'steps': ['异源表达并纯化候选酶，确认分子量与折叠状态',
                      '测定 kcat、Km 与催化效率，覆盖生理底物浓度范围',
                      '比较同家族成员的底物特异性谱',
                      '在体内敲除系中回补催化死突变体作为对照',
                      '把体外效率与体内通量量级对照，判断是否限速'],
            'period': '9-15 个月',
        }
    if fr == 'compartment-transport':
        return {
            'title': '测定 %s 的区室分配与转运' % t,
            'system': '原报道物种；原生质体与完整组织并行',
            'materials': '液泡/质体分离体系、区室特异荧光报告、'
                         '候选转运蛋白突变体（%s）' % d,
            'steps': ['用非水相分离或区室特异报告测定代谢物区室浓度',
                      '在转运蛋白突变体中重测分配比例与转运速率',
                      '用异源系统做转运活性实验（酵母/卵母细胞）',
                      '把分配变化与表型变化做剂量对应',
                      '排除抗体交叉反应与荧光渗漏造成的定位伪影'],
            'period': '12-18 个月',
        }
    if fr == 'receptor-ligand-binding':
        return {
            'title': '测定 %s 的受体结合化学' % t,
            'system': '体外重组受体蛋白；另设体内报告系统',
            'materials': '重组受体胞外域、配体类似物系列、'
                         '结合位点突变受体（%s）' % d,
            'steps': ['表达并纯化受体配体结合域，确认单体状态',
                      '用 ITC 或 SPR 测定 Kd 与结合化学计量',
                      '用配体类似物系列比较受体亚型偏好',
                      '在结合位点突变体中测体内响应 EC50 是否右移',
                      '把 Kd 与 EC50 对照，判断是否存在信号放大'],
            'period': '12-18 个月',
        }
    if fr == 'crosstalk-epistasis':
        return {
            'title': '用上位性实验判定 %s 的互作方向' % t,
            'system': '原报道物种；同遗传背景，单、双、三突变并列',
            'materials': '两条通路的单突变与双突变系、'
                         '激素剂量矩阵（%s）' % d,
            'steps': ['构建两条通路的单突变与双突变，确认操纵有效',
                      '在统一读出下测各基因型对两种激素的响应面',
                      '计算上位性指数，判定加和、协同或拮抗',
                      '用组织特异操纵区分细胞自主与非细胞自主效应',
                      '检验互作是否依赖某一方的下游转录程序'],
            'period': '18-24 个月',
        }
    if fr == 'dose-response-quantitative':
        return {
            'title': '建立 %s 的定量剂量—响应曲线' % t,
            'system': '原报道物种 + 一个独立物种；同一施加方式与取样时间',
            'materials': '≥5 个浓度的外源激素系列、受体突变体、'
                         '统一读出体系（%s）' % d,
            'steps': ['确定生理浓度范围并设 ≥5 个剂量点',
                      '统一施加方式（根部/叶面/培养基）与取样时间',
                      '拟合剂量—响应曲线，报告 EC50 与 Hill 系数',
                      '在受体突变体中重复，检验曲线右移',
                      '在第二个物种中重复，比较阈值差异'],
            'period': '9-15 个月',
        }
    if fr == 'protein-turnover':
        return {
            'title': '测定 %s 的降解动力学' % t,
            'system': '原报道物种；同一组织，蛋白合成抑制剂处理的时间序列',
            'materials': 'CHX 处理时间序列、降解信号突变体、'
                         '蛋白酶体抑制剂对照（%s）' % d,
            'steps': ['用 CHX 追踪目标蛋白丰度，拟合半衰期',
                      '在降解信号突变体中重测半衰期',
                      '检测泛素化修饰状态与多聚泛素链类型',
                      '用蛋白酶体抑制剂确认降解途径',
                      '把半衰期与下游响应持续时间做时间对齐'],
            'period': '9-15 个月',
        }
    if fr == 'process-conservation':
        return {
            'title': '检验 %s 的跨物种调控逻辑' % t,
            'system': '原报道物种与第二个可转化物种并列（%s）' % d,
            'materials': '两个物种中的同源因子敲除系与交叉互补系',
            'steps': ['在第二物种中获得同源因子敲除系',
                      '用同一读出量化该过程',
                      '做交叉互补：物种 A 的基因回补物种 B 的突变体',
                      '比较效应量并给出保守/分化的判定'],
            'period': '18-30 个月',
        }
    return {
        'title': '细胞类型注释的跨数据集一致性',
        'system': '同一组织的 >=2 个独立单细胞或空间数据集',
        'materials': '统一标记基因集、标签转移模型与 bootstrap 重采样（%s）' % d,
        'steps': ['用统一标记集对每个数据集重注释',
                  'bootstrap 重采样，报告类型数的稳定性',
                  '把重注释结果与原始注释做类型级对应',
                  '公布稳定类型集合与不稳定边界'],
        'period': '6-12 个月',
    }


def _aim_plan(h, sp):
    """按假说框架给出"最小可行实验"，而不是对所有假说都套 CRISPR+表型。"""
    t = h['target']
    o = h.get('object') or '目标性状'
    fr = h.get('framing') or 'necessity'
    if fr in ('method-sensitivity', 'family-redundancy',
              'process-conservation', 'annotation-consistency',
              'assembly-contiguity',
              # 2026-11-03 第 12 轮：代谢/激素领域框架不得落回遗传转化模板
              'regulatory-linkage', 'flux-attribution', 'enzyme-kinetics',
              'compartment-transport', 'receptor-ligand-binding',
              'crosstalk-epistasis', 'dose-response-quantitative',
              'protein-turnover'):
        return _pattern_aim_plan(h)
    cls, test = _gene_class(t)
    sp_name = sp if sp and sp != '待定' else '原报道物种'
    gap = ' ' if sp_name[:1].isascii() else ''
    sys_ = ('%s%s与对照同遗传背景、同生育期；如无该物种转化体系，改用近缘可转化物种'
            % (sp_name, gap))
    period = ('18–24 个月（木本/多年生物种需 30 个月）' if _is_woody(sp_name)
              else '12–18 个月')

    if fr == 'directional':
        return {
            'title': '验证 %s 对 %s 的因果方向' % (t, o),
            'system': sys_,
            'materials': ('%s 的敲除/敲低系 ≥2 个独立株系、过表达系 ≥2 个、'
                          '野生型与空载体对照' % t),
            'steps': ['基因型鉴定与表达量测定（确认操纵有效）',
                      '统一取样部位、生育期与光温条件下定量 %s' % o,
                      '剂量梯度（杂合/纯合/过表达强弱）检验方向是否随剂量改变',
                      '互补实验排除脱靶与背景效应'],
            'period': period,
        }
    if fr == 'conflict':
        return {
            'title': '裁决 %s 对 %s 的方向分歧' % (t, o),
            'system': sys_,
            'materials': ('%s 的同一套遗传材料在 ≥2 种组织 × ≥2 种处理条件下并行测试' % t),
            'steps': ['复现分歧双方各自的实验条件（组织、处理、生育期）',
                      '在同一实验室、同一读出下重做双向条件',
                      '分层分析方向是否由条件系统决定',
                      '报告条件 × 方向的交互效应量而非单一均值'],
            'period': '12–20 个月',
        }
    if fr == 'perturbation-unresolved':
        return {
            'title': '归一 %s 的扰动结果' % t,
            'system': sys_,
            'materials': '等位基因系列（强/弱/缺失）+ 野生型与空载体对照',
            'steps': ['收集或构建 ≥3 个等位系并测残余表达/活性',
                      '在同一读出体系下量化 %s' % o,
                      '检验等位强度与效应量的单调关系',
                      '互补实验确认效应来自目标位点'],
            'period': period,
        }
    if fr == 'interaction-required':
        return {
            'title': '检验 %s 的互作是否为功能必需' % t,
            'system': sys_,
            'materials': ('互作界面点突变系（结合缺陷但蛋白稳定）+ 野生型回补系'
                          '（%s）' % (cls or '目标蛋白')),
            'steps': ['结构建模定位互作界面并设计 2–3 个点突变',
                      '验证突变体蛋白丰度与亚细胞定位不变、结合能力丧失',
                      '检测 %s 是否仍被改变' % o,
                      '野生型回补确认表型可恢复'],
            'period': period,
        }
    if fr == 'flux':
        return {
            'title': '区分 %s 对 %s 的通量效应与稳态效应' % (t, o),
            'system': sys_,
            'materials': '同位素标记（13C/15N）喂养体系 + 目标基因操纵系',
            'steps': ['建立标记喂养与代谢物定量流程',
                      '同时测定合成速率（通量）与稳态浓度',
                      '比较通量变化与浓度变化的时间先后',
                      '排除降解/转运速率的混杂'],
            'period': '12–24 个月',
        }
    if fr == 'conservation':
        return {
            'title': '检验 %s 的跨物种保守性' % t,
            'system': '%s 与其近缘可转化物种并列' % (sp if sp and sp != '待定' else '原报道物种'),
            'materials': '两个物种中的同源基因敲除系与互补系（互相回补）',
            'steps': ['在两物种中分别获得同源基因敲除系',
                      '用同一读出量化 %s' % o,
                      '做交叉互补：物种 A 的基因回补物种 B 的突变体',
                      '比较效应量差异并给出保守性判定'],
            'period': '18–30 个月',
        }
    if fr == 'common-upstream':
        return {
            'title': '排除 %s 与 %s 的共同上游解释' % (t, o),
            'system': sys_,
            'materials': '%s 的条件性敲低/诱导系统（可精确控制时间）' % t,
            'steps': ['建立可诱导的 %s 敲低体系' % t,
                      '做时间序列采样，比较 %s 变化的先后顺序' % o,
                      '在共同上游因子被抑制时重复同一时间序列，检验两者是否解耦',
                      '若 %s 的变化稳定滞后于 %s，判定为下游；同步则为平行' % (o, t)],
            'period': period,
        }
    if fr == 'dose-response':
        return {
            'title': '建立 %s 的剂量—效应曲线' % t,
            'system': sys_,
            'materials': '梯度表达系（强/中/弱启动子或诱导剂浓度梯度）≥4 个水平',
            'steps': ['构建 ≥4 个表达水平的独立株系并定量表达量',
                      '在统一条件下测表型并拟合剂量—效应曲线',
                      '估计半数效应点（EC50）与置信区间',
                      '在独立批次/独立实验室复现 EC50'],
            'period': '12–18 个月',
        }
    # necessity（默认）
    if test:
        return {
            'title': '检验 %s 的必要性（%s）' % (t, cls),
            'system': sys_,
            'materials': ('%s 的功能缺失系（CRISPR 敲除 ≥2 株系）+ '
                          '结构域缺陷（结合/催化死）突变系 + 野生型回补系' % t),
            'steps': ['获得功能缺失系并确认无全长转录本/蛋白',
                      '构建结构域缺陷突变体并验证蛋白稳定表达',
                      '按家族特异读出检验：%s' % test[0],
                      '用野生型基因回补，确认表型由该位点导致'],
            'period': period,
        }
    return {
        'title': '检验 %s 的必要性' % t,
        'system': sys_,
        'materials': '%s 的 CRISPR 敲除系 ≥2 个独立株系、过表达系 ≥2 个、野生型与空载体对照' % t,
        'steps': ['基因型鉴定与表达量测定（确认操纵有效）',
                  '统一取样条件下定量 %s' % o,
                  '互补实验排除脱靶与背景效应',
                  '组织特异性表达检验，判断效应发生的部位'],
        'period': period,
    }


# ── 主题特异研究路线（2026-11-03）────────────────────────────────────
# 旧模板把“遗传转化 + ChIP-qPCR + 跨物种验证”套到所有主题，
# 对单细胞注释一致性、方法学 benchmark、基因组组装都不成立。
# 这里按主题给出最小可行路线；通用模板只作为兜底。
_PROGRAM_ROUTES = {
    'single-cell-spatial-omics': (
        '| P0 参考与注释 | 0–6 月 | 统一参考图谱、marker 集与聚类分辨率；做批次/平台一致性审计 | 同一组织在 ≥2 个数据集中的主要细胞类型可重复注释 |\n'
        '| P1 平台互验 | 6–12 月 | scRNA-seq / snRNA-seq / spatial 交叉映射；评估解离偏好与核偏好 | 主要细胞类型的比例与标记基因一致，偏差可量化 |\n'
        '| P2 空间定位 | 12–20 月 | 用空间转录组或原位杂交验证候选细胞群的位置 | 至少 2 个关键细胞群获得空间证据 |\n'
        '| P3 功能扰动 | 20–30 月 | 对候选调控因子做细胞类型特异扰动，读出组成/状态变化 | 扰动引起可重复的细胞状态或比例改变 |',
        '本路线不把 ChIP-qPCR 当作单细胞主题的核心验证；注释一致性、平台偏差和空间定位优先。'),
    'methods-tools': (
        '| P0 基准数据 | 0–4 月 | 固定 ≥3 个公开数据集与统一预处理；锁定评价指标 | 基准可一键复现，版本与参数留档 |\n'
        '| P1 基线比较 | 4–10 月 | 与 ≥2 个现行方法同条件比较；做消融与敏感性分析 | 优势在预注册指标上成立，而非只挑有利数据集 |\n'
        '| P2 泛化测试 | 10–18 月 | 跨物种/跨平台/低质量数据压力测试 | 性能下降有边界，失败模式可解释 |\n'
        '| P3 交付 | 18–24 月 | 容器化、文档、版本化与社区复现 | 第三方按文档可复现主结果 |',
        '方法学主题以 benchmark、消融和复现为骨架；不以生物表型或转化体系作为验收标准。'),
    'genomics-evolution': (
        '| P0 组装与注释 | 0–8 月 | 多平台组装、BUSCO/LAI 质控、重复序列与基因注释 | 组装连续性与注释完整度达到预设阈值 |\n'
        '| P1 比较基因组 | 8–16 月 | 共线性、基因家族扩张/收缩、全基因组复制与分化 | 关键家族变化有系统发育与拷贝数双重支持 |\n'
        '| P2 变异与选择 | 16–24 月 | 重测序/GWAS/选择清除扫描，控制群体结构 | 候选区间在独立群体中可重复 |\n'
        '| P3 功能验证 | 24–36 月 | 对候选基因做表达、单倍型与遗传关联验证 | 至少 1 个候选获得独立功能或关联证据 |',
        '本路线从组装质控开始；没有合格组装与注释，不做“基因组演化”结论。'),
    'epigenetics-gene-regulation': (
        '| P0 染色质图谱 | 0–6 月 | ATAC-seq/ChIP-seq/CUT&Tag 建图；设置生物学重复与输入对照 | 峰质量、重复一致性与背景可控 |\n'
        '| P1 扰动因果 | 6–15 月 | 表观修饰酶或顺式元件扰动；读出表达与染色质变化 | 扰动后目标位点与表达变化同向且可重复 |\n'
        '| P2 多组学整合 | 15–24 月 | 转录组、染色质可及性、组蛋白修饰联合分析 | 调控链有 ≥2 类独立证据支持 |\n'
        '| P3 保守性 | 24–30 月 | 跨物种比较关键顺式元件与修饰 | 保守性与功能差异可区分 |',
        '本路线要求染色质证据与扰动证据配对；仅相关性的组蛋白修饰差异不单独作为因果结论。'),
    'metabolism-natural-products': (
        '| P0 代谢物定位 | 0–6 月 | 靶向/非靶向代谢组，建立组织与时序基线 | 关键代谢物可定量、批间 CV 达标 |\n'
        '| P1 酶功能 | 6–15 月 | 候选酶体外活性、异源表达与底物特异性 | 体外反应可复现，产物结构确认 |\n'
        '| P2 通路通量 | 15–24 月 | 同位素示踪/前体喂养/突变体组合 | 通量改变与代谢物积累方向一致 |\n'
        '| P3 工程化 | 24–36 月 | 在目标作物中重构或调节通路 | 目标化合物产量提升且农艺性状可接受 |',
        '本路线以代谢物定量与酶功能为核心；转录共表达只用于候选排序，不作为通路证明。'),
    'hormone-signaling': (
        '| P0 剂量-时间 | 0–4 月 | 外源激素梯度与时间序列；建立剂量-响应曲线 | 响应窗口与饱和/抑制区间明确 |\n'
        '| P1 受体与信号 | 4–14 月 | 受体/信号组件突变体、抑制剂与报告系 | 遗传与药理证据同向 |\n'
        '| P2 交叉通路 | 14–24 月 | 与其它激素或环境信号的析因实验 | 交互效应可量化，非单因素外推 |\n'
        '| P3 田间/株型 | 24–36 月 | 田间或温室群体验证株型与产量效应 | 至少一个生长季可重复 |',
        '本路线先做剂量-时间，再做遗传因果；不能把外源喷施的表型直接等同于内源信号机制。'),
    'stress-immunity': (
        '| P0 表型与胁迫量化 | 0–6 月 | 多梯度胁迫、盲法定量、田间/温室分层 | 表型差异可重复，胁迫强度可校准 |\n'
        '| P1 遗传因果 | 6–16 月 | 候选基因扰动与等位变异；病原/逆境挑战 | 扰动与表型同向，至少 2 个独立株系 |\n'
        '| P2 信号机制 | 16–24 月 | ROS、钙信号、激素与防御标记时序 | 机制链有时间顺序与遗传依赖 |\n'
        '| P3 田间验证 | 24–36 月 | 多点田间/病圃试验，评估产量与抗性权衡 | 抗性提升不以不可接受减产为代价 |',
        '本路线把田间/病圃验证前置到设计阶段；温室表型不能单独外推。'),
    'developmental-biology': (
        '| P0 分期与谱系 | 0–6 月 | 统一发育分期、标记基因与谱系追踪 | 关键阶段的细胞身份可重复注释 |\n'
        '| P1 遗传扰动 | 6–16 月 | 候选调控因子突变/诱导系统；定量器官表型 | 表型与表达域一致，至少 2 个独立株系 |\n'
        '| P2 活体与空间 | 16–24 月 | 活体成像、原位杂交或空间组学验证 | 关键细胞行为获得时空证据 |\n'
        '| P3 株型外推 | 24–36 月 | 田间株型/产量性状评估 | 发育效应可转化且无重大负效应 |',
        '本路线以发育分期与谱系为核心；跨物种验证放在最后，不能替代本物种的因果实验。'),
}

_DEFAULT_ROUTE = (
    '| P0 可行性 | 0–3 月 | 材料准备、体系建立、预实验（表达量与表型基线） | 体系效率达标，基线数据可复现 |\n'
    '| P1 因果验证 | 3–15 月 | 逐条执行目标的遗传操纵与表型定量 | 每个靶点至少 2 个独立株系数据 |\n'
    '| P2 机制解析 | 12–24 月 | 转录组、互作验证与通路定位 | 至少 1 条上下游调控链有直接证据 |\n'
    '| P3 外推与转化 | 24–36 月 | 跨物种/跨环境验证，材料与数据发布 | 数据提交公共库，材料可共享 |',
    '通用路线：仅在该主题没有专门路线时使用。')


def _program_route(theme_id):
    return _PROGRAM_ROUTES.get(theme_id, _DEFAULT_ROUTE)


def render_program_page(theme_id, hyps, n_evidence, n_papers, basis, diag=None):
    title = th.display_title(theme_id)
    if not hyps:
        return render_evidence_first_program(theme_id, n_evidence, n_papers, basis, diag)
    title_zh = th.display_title(theme_id, 'zh')
    species = Counter(h['species'] for h in hyps if h['species'])
    sp = species.most_common(1)[0][0] if species else '原报道物种'
    targets = ', '.join(h['target'] for h in hyps)

    aims = []
    for i, h in enumerate(hyps, 1):
        plan = _aim_plan(h, sp)
        for _k in ('title', 'system', 'materials'):
            plan[_k] = _zh_tight(plan[_k])
        plan['steps'] = [_zh_tight(_s) for _s in plan['steps']]
        steps_md = '\n'.join('  %d. %s' % (j, s) for j, s in enumerate(plan['steps'], 1))
        aims.append("""### 目标 %d：%s

- **对应假说**：%s
- **体系**：%s
- **材料**：%s
- **关键实验**
%s
- **判定标准**：%s
- **止损条件**：%s
- **预计周期**：%s

""" % (i, plan['title'], h['statement'], plan['system'], plan['materials'],
       steps_md, h['pred_true'], h['pred_false'], plan['period']))

    risks = []
    for h in hyps:
        if h['conflict']:
            risks.append('%s 的效应方向在文献中不一致 → 必须先做条件分层（组织/处理/生育期）再下结论。' % h['target'])
        if h['support_papers'] <= 2:
            risks.append('%s 仅 %d 篇论文支撑 → 存在"单实验室效应"风险，需独立重复。' % (h['target'], h['support_papers']))
        if h['species'] and species and len(set(h['species'] for h in hyps)) == 1:
            break
    if len(set(h['species'] for h in hyps if h['species'])) == 1:
        risks.append('全部假说建立在同一物种（%s）上 → 结论外推需谨慎，建议并列一个远缘体系。' % sp)
    if not risks:
        risks.append('未从证据层识别到显著风险；仍应按标准做法设置生物学重复与盲法测量。')

    route_table, route_note = _program_route(theme_id)
    return """---
title: "Research Program: %s"
title_zh: "%s：研究方案"
type: research-program
topic: "%s"
theme_basis: "%s"
total_evidence: %d
total_papers: %d
total_aims: %d
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: %s
---

# 🔬 %s：从证据到可执行研究方案

> 本方案由 %d 条证据 / %d 篇独立论文中提炼的 %d 条假说直接展开，
> 每个目标都绑定一条可证伪假说及其止损条件。**这不是经费申请书**，
> 而是"如果要做这件事，最小可行实验是什么"的清单。

## 一、问题界定

- **主题**：%s
- **证据规模**：%d 条证据 / %d 篇独立论文
- **候选靶点**：%s
- **主体系**：%s
- **主题归属依据**：%s

## 二、研究目标（每个目标对应一条假说）

%s
## 三、分阶段路线

| 阶段 | 时间 | 内容 | 里程碑（可验收） |
|---|---|---|---|
%s

> %s

## 四、风险与对策

%s

## 五、产出与验收

- **数据**：转录组/表型原始数据提交 GEO/SRA；代码与分析流程随文公开。
- **材料**：编辑系与过表达系在发表后按惯例共享。
- **论文**：按目标拆分，每个目标至少可支撑 1 篇以因果证据为核心的研究论文。
- **负结果**：若某目标触发止损条件，应作为负结果报告，而不是静默删除。

## 六、与综述的关系

本方案的所有靶点均可回溯到 `synthesis/%s.md` 的主题段落与 `evidence/` 下的证据页。
若综述更新后某靶点的支撑证据被撤回或减弱，本方案对应目标应同步降级——
**方案的有效期与证据同步，不做无限期承诺**。

---
*由 Phase 8 生成于 %s；生成器版本 2026-11-02-evidence-grounded*
""" % (title, title_zh, theme_id, basis, n_evidence, n_papers, len(hyps),
       TODAY, title, n_evidence, n_papers, len(hyps),
       title, n_evidence, n_papers, targets, sp,
       '证据标签' if basis == 'tag' else '关键词兜底',
       '\n'.join(aims), route_table, route_note,
       '\n'.join('- %s' % r for r in risks),
       theme_id, TODAY)


def render_evidence_first_program(theme_id, n_evidence, n_papers, basis, diag=None):
    """0 条假说时的方案页：不编造实验，而是给出"主题审计 + 先补证据"的执行清单。

    这是一个**诊断产物**：program_status 标为 evidence-first，total_aims 只统计
    "证据获取目标"，不是生物学实验目标，避免下游把诊断页当成研究计划。
    """
    title = th.display_title(theme_id)
    title_zh = th.display_title(theme_id, 'zh')
    diag = diag or {}
    reasons = diag.get('reasons') or {}
    singles = diag.get('singles') or []
    type_dist = diag.get('type_dist') or {}

    reason_md = '\n'.join(
        '| %s | %d |' % (r, c)
        for r, c in sorted(reasons.items(), key=lambda kv: (-kv[1], kv[0]))
    ) or '| 未形成可用证据簇 | 0 |'

    type_md = '\n'.join(
        '| `%s` | %d | %.0f%% |' % (t, c, 100.0 * c / max(1, n_evidence))
        for t, c in sorted(type_dist.items(), key=lambda kv: (-kv[1], kv[0]))
    ) or '| （无） | 0 | 0% |'

    # 单篇论文独占的断言 → 待复现清单（真实证据 ID + DOI，可回原文核对）
    seen, rows = set(), []
    for e in sorted(singles, key=lambda x: -len(x['claim'])):
        if e['id'] in seen:
            continue
        seen.add(e['id'])
        rows.append('| `%s` | %s | %s |' % (
            e['id'], e.get('doi') or '—',
            _clip(' '.join(e['claim'].split()), 120).replace('|', '/')))
        if len(rows) >= 12:
            break
    if rows:
        list_md = ('| 证据 ID | DOI | 断言（截断，需回原文核对） |\n|---|---|---|\n'
                   + '\n'.join(rows))
    else:
        list_md = '（本主题本次运行未产生单篇独占断言；这不代表证据充分，只说明本次未聚类出可诊断的簇。）'

    # 主题内部异质性诊断：类型高度集中 + 主题词缺失 = 很可能是"检索式错配"
    top_type = max(type_dist.items(), key=lambda kv: kv[1])[0] if type_dist else '未知'
    top_share = (100.0 * max(type_dist.values()) / max(1, n_evidence)) if type_dist else 0.0
    hetero_flag = '是（疑似检索式错配，主题桶被相邻领域证据稀释）' if top_share >= 70 else '否（证据类型较分散）'

    return """---
title: "Research Program: %s"
title_zh: "%s：先补证据再立项（诊断页）"
type: research-program
topic: "%s"
theme_basis: "%s"
total_evidence: %d
total_papers: %d
total_aims: 3
program_status: "evidence-first"
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: %s
---

# 🔬 %s：先补证据，再立项

> 本主题当前**无法**生成任何可证伪假说（0 条），因此不提供实验方案。
> 给出一个"零证据不立项"的审计页，比编造 3 条假说更有价值。
> 本页 `program_status: evidence-first`，三个目标均为**证据获取目标**，不是生物学实验目标。

## 一、为什么不立项

| 项目 | 值 |
|---|---|
| 主题内证据 | %d |
| 独立论文 | %d |
| 主题归属依据 | %s |
| 形成的证据簇 | %d |
| 最大簇规模 | %d |
| 单篇论文独占的断言 | %d 条 |
| 主题内部是否异质 | %s |

**未成假说的原因分布**

| 原因 | 簇数 |
|---|---|
%s

## 二、主题内容审计（这批证据到底是什么）

证据类型分布（`evidence_type`）：

| 类型 | 条数 | 占比 |
|---|---|---|
%s

- 主导类型：`%s`（占 %.0f%%）。
- 判定口径：少于 %d 条证据或少于 %d 篇独立论文的簇**一律不生成假说**；
  这不是算法失败，而是拒绝把单篇论文的孤立断言包装成"假说"。
- 若主导类型为表达/关联类且与主题名称不符，说明**检索式按生物学关键词命中、
  而非按该领域的核心问题命中**，应回到检索层修，而不是在这一层硬凑。

## 三、待复现清单（单篇论文独占的断言，优先补重复）

以下每条断言目前只有 1 篇论文支撑。它们的价值不是"结论"，而是**待验证的线索**：
先找到第二篇独立论文，或自己做一次重复，再谈机制。

%s

## 四、执行清单（3 个证据获取目标）

### 目标 1：主题去污染——把误并入的证据踢出去

- **做法**：按 `evidence_type` 与主题核心词共同过滤，对本主题保留率低于阈值的证据标记
  `theme_suspect`，不参与假说生成；
- **判定标准**：主题内主导类型占比降至 70%% 以下，或与主题名称语义一致；
- **止损条件**：连续 2 轮补采后主导类型占比仍 >85%%，则暂停本主题的假说生成，
  只保留审计页，直到检索式被改写。

### 目标 2：补遗传/因果证据——把关联升级为因果

- **做法**：对每个候选实体追加检索式
  `"<实体>" AND ("mutant" OR "knockout" OR "CRISPR" OR "overexpression")`；
- **判定标准**：每个候选簇至少 1 条遗传操纵证据，且来自 ≥2 篇独立论文；
- **止损条件**：补采 3 轮仍无遗传证据，则该实体降级为"关联性候选"，不进入实验方案。

### 目标 3：补独立重复——打破"单篇独占"

- **做法**：对上表每条断言，检索不同实验室/不同物种的重复报道；
- **判定标准**：表中至少一半断言获得 ≥2 篇独立论文支撑；
- **止损条件**：若某断言在 5 年内无任何独立重复，标注"孤证"并移出待复现清单。

## 五、验收条件（何时可以升级为正式研究方案）

- 至少 3 个证据簇满足"≥%d 条证据 + ≥%d 篇独立论文"；
- 每个簇能抽出可信实体（基因符号或逐字共有短语，不含顺式元件/激素缩写）；
- 每个候选靶点至少 1 条遗传操纵证据。

满足后重跑 `python3 scripts/batch_hypotheses.py --update --only %s` 即可自动升级；
不满足则维持本页，不做"看起来有方案"的输出。

## 六、止损条件（本页自身的退出条件）

- 若连续 3 轮补采后仍为 0 条假说，且主导证据类型未改变 → 判定该主题的**检索式无效**，
  标记 `theme_status: broken-query`，在综述层同步删除对该主题的过度承诺；
- 若审计发现主题桶内 >50%% 证据属于其他领域 → 直接拆分/合并主题，而不是继续补采；
- 任何情况下不得为提高假说数量而降低 %d 条证据 / %d 篇论文的门槛。

---
*由 Phase 8 生成于 %s；生成器版本 2026-11-02-evidence-grounded*
""" % (title, title_zh, theme_id, basis, n_evidence, n_papers, TODAY,
       title, n_evidence, n_papers,
       '证据标签' if basis == 'tag' else '关键词兜底',
       diag.get('n_clusters', 0), diag.get('largest_cluster', 0),
       len(singles), hetero_flag, reason_md, type_md,
       top_type, top_share,
       MIN_EVIDENCE_PER_HYPOTHESIS, MIN_PAPERS_PER_HYPOTHESIS,
       list_md,
       MIN_EVIDENCE_PER_HYPOTHESIS, MIN_PAPERS_PER_HYPOTHESIS, theme_id,
       MIN_EVIDENCE_PER_HYPOTHESIS, MIN_PAPERS_PER_HYPOTHESIS, TODAY)


# ============================================================
# 质量门禁
# ============================================================
PLACEHOLDER_RE = re.compile(r'(?<!\[)\[(?:[a-z][a-z /\-]{2,30})\](?!\])')


def page_issues(text, kind='hypothesis'):
    """返回问题列表；空列表表示通过。供 --check 与落盘前双重使用。"""
    issues = []
    if PLACEHOLDER_RE.search(text):
        issues.append('残留占位符: %s' % ', '.join(sorted(set(PLACEHOLDER_RE.findall(text)))[:5]))
    if len(re.findall(r'^# ', text, re.M)) != 1:
        issues.append('H1 数量不为 1（%d）' % len(re.findall(r'^# ', text, re.M)))
    if len(re.findall(r'^title:', text, re.M)) != 1:
        issues.append('frontmatter title 数量不为 1')
    if ' — Synthesis' in text:
        issues.append('标题误用 synthesis 标题')
    if re.search(r'Supported by \d+ independent evidence', text):
        issues.append('残留旧版模板句（Supported by N independent evidence）')
    if kind == 'hypothesis':
        m = re.search(r'^total_hypotheses:\s*(\d+)', text, re.M)
        if not m:
            issues.append('缺少 total_hypotheses')
        else:
            n_h = int(m.group(1))
            if n_h < HARD_MIN_HYPOTHESES:
                # 允许"诊断型页面"：0 条假说 + 明确声明 + 待复现清单，
                # 但绝不允许空的、假装有结论的页面。
                if '证据不足声明' not in text or '待复现清单' not in text:
                    issues.append('假说数为 0 且缺少"证据不足声明/待复现清单"')
            elif n_h < MIN_HYPOTHESES_PER_THEME and '证据不足声明' not in text:
                issues.append('假说数 %d < 目标 %d 且缺少"证据不足声明"'
                              % (n_h, MIN_HYPOTHESES_PER_THEME))
        ID_RE = r'`[A-Za-z0-9_.\-]+`'
        n_backticked = len(re.findall(r'^- ' + ID_RE, text, re.M))
        n_backticked += len(re.findall(r'^\| ' + ID_RE, text, re.M))
        if n_h >= HARD_MIN_HYPOTHESES:
            if n_backticked < 3 * n_h:
                issues.append('可回溯证据 ID 少于 %d 条（%d）'
                              % (3 * n_h, n_backticked))
            if '若假说为假' not in text:
                issues.append('缺少证伪条件')
        else:
            # 诊断型页面：必须列出可回溯的孤证清单，或显式说明为何没有
            if n_backticked < 3 and '未产生单篇独占断言' not in text:
                issues.append('诊断页可回溯证据 ID 少于 3 条且未显式说明（%d）'
                              % n_backticked)
    if kind == 'program':
        evidence_first = re.search(r'^program_status:\s*"?evidence-first"?',
                                   text, re.M) is not None
        if '止损条件' not in text:
            issues.append('缺少止损条件')
        if not re.search(r'^total_aims:\s*[1-9]', text, re.M):
            issues.append('缺少有效 total_aims')
        if evidence_first:
            if '证据获取目标' not in text:
                issues.append('evidence-first 页未声明目标是"证据获取"而非生物学实验')
            if '验收条件' not in text:
                issues.append('evidence-first 页缺少升级验收条件')
    return issues


def check_pages(verbose=True):
    bad = 0
    for theme_id in th.THEMES:
        for kind, d in (('hypothesis', HYPOTHESES_DIR), ('program', PROGRAMS_DIR)):
            path = os.path.join(d, '%s.md' % theme_id)
            if not os.path.exists(path):
                if verbose:
                    print('  ? %s/%s 缺失' % (kind, theme_id))
                bad += 1
                continue
            with open(path, 'r', encoding='utf-8', errors='replace') as fh:
                text = fh.read()
            issues = page_issues(text, kind)
            if issues:
                bad += 1
                if verbose:
                    print('  ✗ %s/%s' % (kind, theme_id))
                    for it in issues:
                        print('      - %s' % it)
            elif verbose:
                print('  ✓ %s/%s' % (kind, theme_id))
    total = len(th.THEMES) * 2
    if verbose:
        print('\nDONE: %d/%d 页面不合格' % (bad, total))
    return 1 if bad else 0


# ============================================================
# 主流程
# ============================================================
def write_if_changed(path, content):
    try:
        with open(path, 'r', encoding='utf-8') as fh:
            if fh.read() == content:
                return False
    except OSError:
        pass
    with open(path, 'w', encoding='utf-8', newline='\n') as fh:
        fh.write(content)
    return True


def main(argv=None):
    ap = argparse.ArgumentParser(description='证据驱动的假说与研究方案生成')
    ap.add_argument('--update', action='store_true', help='生成并落盘（默认）')
    ap.add_argument('--check', action='store_true', help='只校验已落盘页面')
    ap.add_argument('--dry-run', action='store_true', help='只打印统计，不写盘')
    ap.add_argument('--only', default='', help='逗号分隔的主题 id')
    args = ap.parse_args(argv)

    if args.check:
        print('Phase 8 check: 假说/方案页面质量门禁')
        return check_pages()

    for d in (HYPOTHESES_DIR, PROGRAMS_DIR):
        os.makedirs(d, exist_ok=True)

    only = {x.strip() for x in args.only.split(',') if x.strip()}
    themes_to_run = [t for t in th.THEMES if not only or t in only]

    print('Phase 8: evidence-grounded hypothesis generation')
    evidence = load_evidence()
    # 2026-11-04：与 batch_synthesis 同一条硬闸门——0 证据时拒绝生成，
    # 否则会在错误的 BASE（如仓库根）下写出整批"证据不足"空壳假说页。
    if not evidence:
        sys.stderr.write(
            "ERROR: 加载到 0 条证据，拒绝写入假说页。\n"
            "       当前 BASE=%s，应指向含 evidence/ 的知识库根。\n" % BASE)
        # 用 4 而不是 2：main 的 2 已被"主题降级"占用，上游据此只做记录不报警。
        # 空库属于必须被看见的致命错误，不能与降级混用同一退出码。
        return 4
    groups, dropped = group_by_theme(evidence)
    print('  evidence objects: %d (dropped as too-generic: %d, non-plant: %d)'
          % (len(evidence), dropped, len(NONPLANT_DROPPED)))

    written_h = written_p = 0
    summary = []
    failures = 0
    degraded = 0
    for theme_id in themes_to_run:
        items = groups.get(theme_id, [])
        papers = {paper_key(e) for e in items}
        basis = 'tag'
        if items and sum(1 for e in items if e['theme_basis'] == 'keyword') > len(items) / 2:
            basis = 'keyword'
        hyps, diag = build_hypotheses(theme_id, items)
        print('  %-32s evidence=%-4d papers=%-4d hypotheses=%d'
              % (theme_id, len(items), len(papers), len(hyps)))
        if diag['insufficient']:
            print('    ~ 假说数 %d < 目标 %d：写入"证据不足声明 + 待复现清单"'
                  % (len(hyps), MIN_HYPOTHESES_PER_THEME))
        diagnostic_only = len(hyps) < HARD_MIN_HYPOTHESES
        if diagnostic_only:
            if not diag['singles'] and not diag['reasons']:
                print('    ! 0 条假说且无可诊断的证据簇：保留上一版')
                failures += 1
                summary.append({'theme': theme_id, 'evidence': len(items),
                                'papers': len(papers), 'hypotheses': 0,
                                'status': 'no-evidence'})
                continue
            print('    ! 0 条可证伪假说：改写为"诊断页 + 待复现清单"（degraded）')

        h_text = render_hypotheses_page(theme_id, hyps, len(items), len(papers),
                                       basis, diag)
        p_text = render_program_page(theme_id, hyps, len(items), len(papers),
                                    basis, diag)
        problems = page_issues(h_text, 'hypothesis') + page_issues(p_text, 'program')
        if problems:
            print('    ✗ 生成结果未过门禁，拒绝写盘：')
            for p in problems:
                print('        - %s' % p)
            failures += 1
            summary.append({'theme': theme_id, 'evidence': len(items),
                            'papers': len(papers), 'hypotheses': len(hyps),
                            'status': 'rejected: ' + '; '.join(problems[:2])})
            continue

        if args.dry_run:
            summary.append({'theme': theme_id, 'evidence': len(items),
                            'papers': len(papers), 'hypotheses': len(hyps),
                            'status': 'dry-run-ok'})
            continue

        if write_if_changed(os.path.join(HYPOTHESES_DIR, '%s.md' % theme_id), h_text):
            written_h += 1
        if write_if_changed(os.path.join(PROGRAMS_DIR, '%s.md' % theme_id), p_text):
            written_p += 1
        summary.append({'theme': theme_id, 'evidence': len(items),
                        'papers': len(papers), 'hypotheses': len(hyps),
                        'status': 'diagnostic-only' if diagnostic_only else 'ok'})
        if diagnostic_only:
            degraded += 1

    stats_path = os.path.join(BASE, 'logs', 'hypothesis_stats.json')
    if not args.dry_run:
        try:
            os.makedirs(os.path.dirname(stats_path), exist_ok=True)
            with open(stats_path, 'w', encoding='utf-8') as fh:
                json.dump({'date': TODAY, 'themes': summary}, fh,
                          ensure_ascii=False, indent=2)
        except OSError:
            pass

    print('\nDONE: hypotheses written=%d programs written=%d failures=%d degraded=%d'
          % (written_h, written_p, failures, degraded))
    if args.dry_run:
        for s in summary:
            print('  %-32s %s' % (s['theme'], s['status']))
    # 2 = 存在"证据不足/诊断型"主题：让上游记录降级，但不算致命失败
    return 2 if (failures or degraded) else 0


if __name__ == '__main__':
    sys.exit(main())
