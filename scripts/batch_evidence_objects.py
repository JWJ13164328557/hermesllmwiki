#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 Evidence Objects + Entity 页面。

设计约束（2026-11 整改）
------------------------
1. **确定性**：同一输入必须产出逐字节相同的文件。所有集合输出都经过排序，
   不再依赖 set 迭代顺序（旧实现 list(genes)[:5] 会随 PYTHONHASHSEED 变化，
   既制造 git 噪音，也让"哪 5 个基因被保留"随机漂移）。
2. **幂等**：内容未变化时不重写文件，避免每次运行都刷新 mtime 与 git diff。
3. **时间戳可信**：created 只在首次创建时写入；已有文件的 created 沿用它自己的值，
   旧实现每次都写成"今天"，导致历史证据的时间信息被抹掉。
4. **不伪造分析**：不再输出 "Contradictory Evidence: None identified" 与空的
   "Open Questions"。这两段从未真正做过检索，留着会让读者误以为核对过。
   现在改为明确标注字段来源（自动标注 + 启发式），把"未做"和"做了没发现"区分开。
"""
import argparse, io, json, os, re, time
from collections import defaultdict, Counter
from datetime import datetime

from kb_paths import BASE  # 统一根目录解析: KB_BASE/APP_DIR 环境变量优先
from species_patterns import primary_species
from organism_scope import import_decision, clean_abstract, is_method_paper

CONCEPTS_DIR = os.path.join(BASE, 'concepts', 'papers')
EVIDENCE_DIR = os.path.join(BASE, 'evidence')
ENTITIES_DIR = os.path.join(BASE, 'entities')

os.makedirs(EVIDENCE_DIR, exist_ok=True)
os.makedirs(ENTITIES_DIR, exist_ok=True)

TODAY = datetime.now().strftime('%Y-%m-%d')

MAX_GENES = 10       # 每条证据最多标注的基因数（按出现频次取前 N，确定性）
MAX_COMPOUNDS = 8    # 同上，化合物

# 迁移到句首常见的废话，提取结论时应剥离
LEADIN = re.compile(
    r'^(?:It (?:should|is|must) (?:also )?be (?:noted|mentioned|emphasized) that|'
    r'It is worth noting that|Notably|Interestingly|Importantly|Moreover|Furthermore|'
    r'In addition|Additionally|Consistently|Taken together|Together,? these results? '
    r'(?:suggest|indicate|show) that|These results? (?:suggest|indicate|show) that)\s*[,:]?\s*',
    re.I)


def slugify(text):
    """Create URL-friendly slug from text"""
    s = re.sub(r'[^\w\s-]', '', text.lower())
    s = re.sub(r'\s+', '-', s.strip())
    return s[:80].rstrip('-')


def _ranked_counts(pattern_counts):
    """{名称: 出现次数} -> 按 (次数降序, 名称升序) 的确定性列表。"""
    return [name for name, _n in sorted(pattern_counts.items(), key=lambda kv: (-kv[1], kv[0]))]


def extract_gene_compounds(text):
    """从结论句中抽取基因符号与化合物，按出现频次排序后截断。

    旧实现返回 list(set)[:5]：顺序随进程随机，且截断保留了哪 5 个也不固定。
    """
    gene_counts = Counter()
    compound_counts = Counter()

    gene_patterns = [
        r'\b([A-Z][a-z]{1,3}[A-Z][A-Za-z0-9]{1,8})\b',   # AtMYB2, OsNAC1
        r'\b([a-z]{2,4}[A-Z][a-z]{2,4}[A-Z][A-Za-z0-9]{0,6})\b',  # SlBZR1, MdBT2
        r'\b([A-Z]{2,6}[0-9]{1,3}[A-Z]?)\b',  # WRKY33, MPK3, NAC1（补全全大写基因符号）
        r'\b([A-Z]{2,6}[0-9]{1,3}[A-Z]?)\b',  # WRKY33, MPK3, NAC1（补全全大写基因符号）
    ]
    stopwords = {
        'the', 'and', 'for', 'was', 'were', 'with', 'that', 'this', 'from', 'have',
        'been', 'also', 'into', 'more', 'after', 'such', 'than', 'while', 'over',
        'both', 'each', 'most', 'some', 'many', 'between', 'these', 'those', 'other',
        'which', 'their', 'about', 'could', 'would', 'should', 'during', 'within',
        'through', 'however', 'furthermore', 'moreover', 'therefore', 'because',
        'although', 'typically', 'including', 'whereas',
        # 全大写基因模式容易命中方法与统计缩写，显式排除
        'fdr', 'pca', 'pcd', 'log2', 'ppi', 'atp', 'abc', 'cds', 'mz',
        # 全大写基因模式容易命中方法与统计缩写，显式排除
        'fdr', 'pca', 'pcd', 'log2', 'ppi', 'atp', 'abc', 'cds', 'mz',
    }
    for pat in gene_patterns:
        for match in re.finditer(pat, text):
            gene = match.group(1)
            if gene.lower() not in stopwords:
                gene_counts[gene] += 1

    compound_patterns = [
        r'\b(flavonoid|flavonol|anthocyanin|proanthocyanidin|carotenoid)\b',
        r'\b(terpenoid|monoterpene|sesquiterpene|diterpene|triterpene)\b',
        r'\b(alkaloid|caffeine|theanine|nicotine)\b',
        r'\b(lignin|cellulose|hemicellulose|xylan|xyloglucan)\b',
        r'\b(starch|sucrose|glucose|fructose|maltose)\b',
        r'\b(phenylpropanoid|phenolic|coumarin)\b',
        r'\b(ginsenoside|tanshinone|artemisinin|taxol|saponin)\b',
        r'\b(wax|cutin|suberin)\b',
        r'\b(jasmonic acid|salicylic acid|abscisic acid|gibberellin|auxin|ethylene|brassinosteroid|strigolactone)\b',
        r'\b(melatonin|serotonin|dopamine)\b',
        r'\b(ascorbic acid|tocopherol|vitamin)\b',
        r'\b(chlorophyll|carotene|lycopene|zeaxanthin)\b',
    ]
    for pat in compound_patterns:
        for match in re.finditer(pat, text, re.I):
            compound_counts[match.group(1).lower()] += 1

    genes = _ranked_counts(gene_counts)[:MAX_GENES]
    compounds = _ranked_counts(compound_counts)[:MAX_COMPOUNDS]
    return genes, compounds


def extract_findings_from_concept(content):
    """Extract numbered findings from the 深度提炼 section"""
    depth_sec = re.search(r'### 核心发现\n(.+?)(?=\n## (?!###)|## 相关|\n---|\Z)', content, re.DOTALL)
    if not depth_sec:
        return []

    findings = []
    for line in depth_sec.group(1).split('\n'):
        line = line.strip()
        m = (re.match(r'^\d+\.\s+(.*)$', line)
             or re.match(r'^[-*+]\s+(.*)$', line))
        if not m:
            continue
        finding = normalize_finding(m.group(1))
        if not finding_quality_ok(finding):
            continue
        finding = LEADIN.sub('', finding).strip()
        # 剥离句首废话后首字母变小时补回大写，避免出现 "the expression of ..."
        if finding and finding[0].islower():
            finding = finding[0].upper() + finding[1:]
        if len(finding) > 30:
            findings.append(finding)
    return findings


# ── 证据行质量控制（2026-11-02 第六轮）────────────────────────────
# 42 个概念页的"核心发现"是无序列表，但内容直接来自 PDF 断行文本：
#   "corre­ sponding"（软连字符断词）、"Here we report 36 that brassinosteroid…"
#   （行号被当作正文）、"## 深度提炼 **物种**: …"（元数据倾倒）。
# 这些行不是可证伪的发现，导入会污染证据层，宁缺勿滥。
_PDF_BREAK = re.compile(r'[\u00ad-]\s+(?=[a-z])|\b\w+\s\d{1,3}\s+(?:that|the|and|in|of|to|is|was)\b')
_META_DUMP = re.compile(r'^#|^\*\*(物种|方法|来源|期刊)\*\*|\*\*(物种|方法|来源)\*\*:')
_CITATION_TAIL = re.compile(r'\s\d{1,3}\.?$')
_LOWER_START_OK = re.compile(r'^(?:[a-z]{1,3}\d|miR|lncRNA|siRNA)')

# PDF 抽取常见的字形损伤：软连字符断词、连字、行内行号。
_SOFT_HYPHEN = re.compile(r'[\u00ad\u2010\u2011]')
_LIGATURES = {'\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl',
              '\ufb03': 'ffi', '\ufb04': 'ffl', '\ufb05': 'st', '\ufb06': 'st'}
# 行号残留：PDF 两栏排版把行号插进句子（"In summary, 179 cadmium stress … 180 impairment"）。
# 必须限定 2–3 位数字且前面是空白/标点：单个数字多是基因名后缀
# （wer-1、cpc-1、lzy1;2;3），把它们当行号会误删真实机制论断。
_RUNNING_NUM = re.compile(r'(?<=[\s.,;)])\d{2,3}\s+(?=[a-z]{2,})')
_FIG_TAIL = re.compile(r'\((?:Fig|Table|Supplementary)\.?\s*[^)]*$|\bFig\.\s*\d+[A-Za-z]?$')
_TERMINAL = re.compile(r'[.!?。！？)"\']$')


def normalize_finding(text):
    """修复 PDF 文本损伤：软连字符断词、连字、多余空白、行号残留。"""
    t = text or ''
    for bad, good in _LIGATURES.items():
        t = t.replace(bad, good)
    t = _SOFT_HYPHEN.sub('', t)
    # "con- trolling"：真连字符跨行断词，去掉连字符与空格重新拼接
    t = re.sub(r'([A-Za-z])-\s+([a-z]{2,})', r'\1\2', t)
    # 行内参考文献编号 "… biosynthesis (52, 134)." → 去掉括号内纯编号
    t = re.sub(r'\s*\(\s*\d{1,3}(?:\s*[,;]\s*\d{1,3})*\s*\)', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def finding_quality_ok(text):
    """严格质量闸门：只放行完整、干净、可独立引用的句子。"""
    t = normalize_finding(text)
    if len(t) < 60:
        return False
    if not _TERMINAL.search(t):
        return False
    if _FIG_TAIL.search(t):
        return False
    if _RUNNING_NUM.search(t):
        return False
    if _META_DUMP.search(t):
        return False
    return True


def _is_clean_finding(text):
    """判断一行文本是否可作为证据：拒绝元数据倾倒、PDF 断词、行号污染。"""
    t = (text or '').strip()
    if len(t) < 40:
        return False
    if _META_DUMP.search(t):
        return False
    if _PDF_BREAK.search(t):
        return False
    # 句尾孤立数字多半是 PDF 行号残留（"… by 37"）
    if _CITATION_TAIL.search(t):
        return False
    # 未剥净的引用上标/断词残留
    if t.count('  ') > 0:
        return False
    return True


def generate_evidence_id(paper_slug, finding_idx):
    """Generate unique evidence ID"""
    return f"{paper_slug}-f{finding_idx + 1}"


def short_title(text, limit=90):
    """截断到词边界，避免出现 "... obviously up- r" 这种断词。"""
    text = _flat(text)
    if len(text) <= limit:
        return text
    cut = text[:limit]
    space = cut.rfind(' ')
    if space > limit * 0.6:
        cut = cut[:space]
    return cut.rstrip(' ,;:-') + ' …'


# YAML 标量里不允许出现 C0/C1 控制字符。PDF 抽取会把连字符、上下标字形留成
# \x01-\x03 这类字符，直接拼进 title: 会让整页 frontmatter 无法解析
# （2026-11-04 自检发现 11 页）。这里在压平阶段就清掉。
_CTRL_CHARS = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]')


def _flat(text):
    """把多行/多余空白压成一行，供 YAML 单行字段使用。

    清控制字符 + 双引号转单引号：两者都会破坏 YAML 标量。
    """
    text = _CTRL_CHARS.sub('', text or '')
    return re.sub(r'\s+', ' ', text).replace('"', "'").strip()


def read_created(path):
    """读取已有文件 frontmatter 里的 created，用于保留原始时间戳。"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            head = f.read(600)
    except OSError:
        return None
    m = re.search(r'^created:\s*(\d{4}-\d{2}-\d{2})', head, re.M)
    return m.group(1) if m else None


def write_if_changed(path, content):
    """内容一致就不落盘：返回 True 表示确实写入。"""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            if f.read() == content:
                return False
    except OSError:
        pass
    with open(path, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    return True


# 证据语义类型（2026-11-03 扩展）
# 目的不是给论文贴标签，而是让下游知道"这条证据能支持什么强度的论断"：
#   genetic perturbation  因果最强：扰动后表型/表达改变
#   protein interaction   物理互作：Co-IP/Y2H/BiFC/pull-down
#   DNA binding/regulation 直接调控：ChIP/EMSA/启动子报告
#   expression/regulation 表达相关：转录组/qPCR，不能单独推因果
#   phenotypic/association 表型关联：GWAS/QTL/自然变异/田间表型
#   omics/co-occurrence   组学共现：单细胞簇、共表达网络、图谱，非调控
#   descriptive/observational 描述性观察：无扰动、无互作、无关联设计
EVIDENCE_TYPES = (
    'genetic perturbation',
    'protein interaction',
    'DNA binding/regulation',
    'expression/regulation',
    'phenotypic/association',
    'omics/co-occurrence',
    'descriptive/observational',
)

_PERT_TERMS = re.compile(
    r'\b(knockout|knock-out|knockdown|knock-down|mutant|mutants|crispr|'
    r'overexpression|over-expression|rna[iI]?|t-dna|complementation|'
    r'loss-of-function|gain-of-function|silencing|transgenic|gene[- ]edited|'
    r'genome[- ]edited|edited lines?)\b', re.I)
_CAUSAL_VERBS = re.compile(
    r'\b(resulted in|led to|caused|increased|decreased|reduced|enhanced|'
    r'impaired|affected|altered|promoted|inhibited|suppressed|conferred|'
    r'abolished|restored|accumulation|tolerance|resistance|sensitivity|'
    r'phenotype|phenotypic|revealed|demonstrated|showed that|indicated that)\b', re.I)
_PERT_DESIGN = re.compile(
    r'\b(we (generated|constructed|created|performed|knocked out|knocked down)|'
    r'(was|were) (generated|constructed|knocked out|knocked down)|'
    r'knockout (lines?|plants?|mice)|mutant (lines?|plants?)|'
    r'mutants?.{0,50}(reveal|show|demonstrate|indicate|suggest))\b', re.I)
_PHYSICAL_INTERACTION = re.compile(
    r'\b(co-?ip|coimmunoprecipitation|y2h|yeast two-hybrid|bifc|'
    r'pull-down|pulldown|affinity purification|fret|split-luciferase|'
    r'surface plasmon resonance|spr|microscale thermophoresis|mst|'
    r'protein[- ]protein interaction|directly interacts? with|'
    r'physical interaction)\b', re.I)
_DIRECT_REGULATION = re.compile(
    r'\b(chip(?:-seq)?|chip-qpcr|emsa|dap-seq|transactivation|'
    r'promoter binding|binds? (?:to )?the promoter|'
    r'chromatin immunoprecipitation)\b', re.I)
_REPORTER_PROMOTER = re.compile(
    r'\b((luciferase|reporter).{0,60}promoter|promoter.{0,60}(luciferase|reporter))\b', re.I)
_EXPRESSION = re.compile(
    r'\b((?:rt-)?qpcr|quantitative pcr|gene expression analysis|'
    r'expression analysis|transcript (?:level|abundance)|'
    r'mrna (?:level|abundance)|differentially expressed genes?|\bdegs?\b|'
    r'ex(?:pressed|pression).{0,40}(higher|lower|increased|decreased|up-?regulated|down-?regulated)|'
    r'(up-?regulated|down-?regulated).{0,30}(genes?|transcripts?))\b', re.I)
_ASSOCIATION = re.compile(
    r'\b(gwas|genome-wide association|qtl|association mapping|'
    r'natural variation|allelic variation|field trial|'
    r'phenotypic variation|correlat(?:ed|ion) with|'
    r'genomic prediction|selection signature|'
    r'(promoted|increased|decreased|reduced|enhanced).{0,30}accumulation)\b', re.I)
_OMICS = re.compile(
    r'\b(single[- ]cell|scrna[- ]?seq|snrna[- ]?seq|spatial transcriptom|'
    r'stereo-seq|visium|xenium|merfish|smfish|in situ sequencing|'
    r'cluster(?:s|ing)?|marker genes?|cell atlas|co-?expression|'
    r'co-?occurrence|pseudotime|trajectory|module eigengene|'
    r'weighted gene co-expression|network analysis|transcriptom(?:e|ic)|'
    r'rna-?seq|rna sequencing|microarray|atac[- ]?seq|cut&tag|'
    r'metabolom(?:e|ic)|proteom(?:e|ic)|multi-omics)\b', re.I)


# ── rule-v3 词表（2026-11-03）───────────────────────────────────────
# rule-v2 的判别力不足：descriptive/observational 占 89.2%，因果级仅 3.8%。
# 实测反例：CLV3「diffuses until it binds CLV1/CLV2/CRK」——明确的受体结合
# 陈述，被判成"描述性观察"。根因是词表只认"方法名"，不认**论断谓词**：
#   "binds to / interacts with / phosphorylates" 本身就是互作证据的表述，
#   论文是否写全 "Co-IP" 是次要的。
# rule-v3 因此改为「论断谓词为主、方法先验为辅」的两路打分。

_V3_INTERACTION_PRED = re.compile(
    r'(\b(binds?\s+to|bound\s+to|binds?\s+the|binds?\s+\S+\s+receptors?|'
    r'interacts?\s+with|interacting\s+with|'
    r'forms?\s+(?:a\s+)?(?:complex|heterodimer|homodimer|receptor\s+complex)\s+with|'
    r'heterodimeri[sz]es?|homodimeri[sz]es?|dimeri[sz]es?|'
    r'phosphorylates?|dephosphorylates?|ubiquitinates?|'
    r'(?:phosphorylated|ubiquitinated|acetylated|methylated)\s+by|'
    r'associates?\s+with\s+the\s+(?:receptor|kinase|protein))\b'
    # 名词化表述同样是互作证据："binding of CLV3p to its receptors"、
    # "interaction between CLV1 and CLV2"。rule-v2 只认动词，漏掉这一类。
    r'|\bbinding\s+of\s+\S+(?:\s+\S+)?\s+(?:to|with)\s+\S+'
    r'|\binteraction\s+between\s+\S+(?:\s+\S+)?\s+and\s+\S+'
    r'|\bco-?receptors?\b)', re.I)
_V3_PHYS_METHOD = re.compile(
    r'\b(co-?ip|co-?immunoprecipitation|y2h|yeast\s+two-hybrid|bifc|'
    r'pull-?down|affinity\s+purification|fret|bret|split-luciferase|'
    r'nano?bit|surface\s+plasmon|microscale\s+thermophoresis|phage\s+display|'
    r'protein[- ]protein\s+interaction)\b', re.I)

_V3_DNA_PRED = re.compile(
    r'\b(binds?\s+(?:to\s+)?the\s+\S*\s*promoter|promoter\s+binding|'
    r'directly\s+(?:activates?|represses?|regulates?)|'
    r'directly\s+binds?\s+(?:to\s+)?(?:the\s+)?(?:\S+\s+){0,2}'
    r'(?:promoter|enhancer|cis-?element|regulatory\s+(?:region|element)|motif)|'
    r'directly\s+binds?\s+(?:to\s+)?the\s+promoters?\s+of|'
    r'is\s+a\s+direct\s+target\s+of|direct\s+target\s+of|transactivates?|'
    r'chromatin\s+immunoprecipitation|recruits?\s+(?:the\s+)?(?:pol\s*ii|rna\s+polymerase))\b', re.I)
_V3_DNA_METHOD = re.compile(
    r'\b(chip(?:-seq|-qpcr)?|emsa|dap-seq|yeast\s+one-hybrid|'
    r'promoter\s+(?:assay|reporter)|transactivation\s+assay|'
    r'dual-luciferase|atac-seq|dnase\s+footprint)\b', re.I)

_V3_PERT_NOUN = re.compile(
    r'\b(mutants?|mutations?|knock-?outs?|knock-?downs?|crispr|cas9|rna-?i|rnai|vigs|'
    r't-dna|transgenic|over-?express(?:ion|ing|ed)?|complementation|'
    r'loss-of-function|gain-of-function|silencing|gene[- ]edited|'
    r'genome[- ]edited|indels?|allelic\s+series)\b', re.I)
_V3_EFFECT_VERB = re.compile(
    r'\b(increas\w*|decreas\w*|reduc\w*|enhanc\w*|promot\w*|inhibit\w*|'
    r'suppress\w*|impair\w*|abolish\w*|restor\w*|confer\w*|lead\w*\s+to|'
    r'result\w*\s+in|caus\w*|alter\w*|affect\w*|accumulat\w*|tolerance|'
    r'resistance|sensitiv\w*|phenotyp\w*|delay\w*|accelerat\w*|'
    r'reduc\w*\s+levels?|elevat\w*)\b', re.I)
_V3_PERT_DESIGN = re.compile(
    r'\b(we\s+(?:generated|constructed|created|made|knocked)|'
    r'(?:was|were)\s+(?:generated|constructed|knocked)|'
    r'knockout\s+(?:lines?|plants?|mice)|mutant\s+(?:lines?|plants?|alleles?)|'
    r'site[- ]directed\s+mutagenesis)\b', re.I)

_V3_OMICS = re.compile(
    r'\b(single[- ]cell|scrna[- ]?seq|snrna[- ]?seq|spatial\s+transcriptom|'
    r'stereo[- ]?seq|visium|merfish|smfish|cell\s+atlas|pseudotime|'
    r'trajectory\s+inference|marker\s+genes?|clusters?\s+of\s+cells?|'
    r'co-?expression|module\s+eigengene|wgcna|'
    r'transcriptom\w*|rna-?seq|rna\s+sequencing|microarray|'
    r'atac[- ]?seq|cut&tag|proteom\w*|metabolom\w*|multi-?omics)\b', re.I)
_V3_ASSOC = re.compile(
    r'\b(gwas|genome-wide\s+association|\bqtl\b|association\s+mapping|'
    r'natural\s+variation|allelic\s+variation|haplotype|field\s+trial|'
    r'phenotypic\s+variation|correlat\w*\s+with|genomic\s+prediction|'
    r'selection\s+signature)\b', re.I)
_V3_EXPR = re.compile(
    r'\b((?:rt-)?qpcr|quantitative\s+pcr|gene\s+expression|'
    r'expression\s+(?:level|levels|analysis|pattern|profile|profiling)|'
    r'transcript\s+(?:level|levels|abundance)|mrna\s+(?:level|levels|abundance)|'
    r'up-?regulated|down-?regulated|up-?regulation|down-?regulation|'
    r'differentially\s+expressed|\bdegs?\b|induced\s+by|repressed\s+by|'
    r'expression\s+increas\w*|expression\s+decreas\w*|'
    # 2026-11-04 rule-v5：裸 "increased the expression of X" 旧词表不认，
    # 表达句会被后置的处理规则抢成 phenotypic（单测实测复现）。
    # 这里补三个真正的表达句式，只认带"变化动词"的，避免把
    # "the expression of X in roots" 这种中性名词短语误判。
    r'(?:increas|decreas|reduc|enhanc|elevat|alter|induc|repress)\w*\s+'
    r'(?:the\s+)?expression\s+of|'
    r'expression\s+of\s+\S+\s+(?:was|were)\s+'
    r'(?:increas|decreas|reduc|enhanc|elevat|alter|induc|repress)\w*|'
    r'(?:level|levels|abundance)\s+of\s+\S+\s+(?:was|were)\s+'
    r'(?:increas|decreas|reduc|enhanc|elevat|alter)\w*)\b', re.I)
_V3_FUNCTIONAL = re.compile(
    r'\b(is|are)\s+(required|essential|necessary|sufficient)\s+(for|to)\b', re.I)

# ── rule-v5 词表（2026-11-04）───────────────────────────────────────
# 判别力专项：对 descriptive 池做 60 条人工裁定 + 全库探针量化，结论是
# rule-v4 的漏判集中在三处**词法缺口**，而非分类体系缺档：
#   (a) 翻译后修饰用名词式："phosphorylation at Ser240 serves as a readout"
#       —— rule-v4 只认 "phosphorylates" 动词，130 条 PTM 论断被判 descriptive；
#   (b) 因果基因认定："Os09g0369500 is the causal gene at qSS-9, designated SAG9"
#       —— 无量词表条目，被整句丢掉；
#   (c) 处理—效应："drought treatment increased ..."、"exogenous ABA enhanced ..."
#       —— 词表只认 genetic perturbation，非遗传处理的实验证据全落进 descriptive
#       （探针命中 957 条，人工裁定样本里约 42% 是真漏判）。
# 上限已量化：descriptive 中最多 1119 条（8.6%）可能被误标，即因果级占比
# 的规则修复天花板约 19%。v5 只摘低垂果实，不动分类体系。

# 2026-11-04：PTM 名词式规则曾试做（把 "phosphorylation at Ser240" 判为
# 物理互作），留出验证精度仅 5/15 = 33%——命中的多是教科书定义
# （"SUMOylation involves attachment to lysine residues"）和甲基化方法句
# （"DNA methylation status at single-base resolution"）。已撤销，
# 保留此注记以免后人重复踩坑。
_V5_CAUSAL_GENE = re.compile(
    r'\b(causal\s+gene|candidate\s+gene|gene\s+underlying|'
    r'underlying\s+gene|causative\s+gene|responsible\s+gene|'
    r'(?:was|were)\s+designated\s+(?:as\s+)?[A-Z][A-Za-z0-9-]{2,}|'
    r'fine[- ]mapped\s+to|cloned\s+the\s+gene)\b', re.I)

_V5_TREAT_STRONG = re.compile(
    r'\b(treat(?:ed|ment|ments)|applications?|supplementation|supplemented|'
    r'exogenous|exposure\s+to|subjected\s+to|imposed|sprayed|irrigated|'
    r'drought|salt\s+stress|salinity|heat\s+stress|cold\s+stress|'
    r'chilling|freezing|osmotic\s+stress|water\s+stress|wounding|'
    r'high[- ]light|low[- ]light|shading|shade\s+treatment|UV-?B|'
    r'elevated\s+(?:CO2|CO\s*2|ozone|O3|temperature)|'
    r'nitrogen\s+deficien\w+|phosph\w+\s+deficien\w+|'
    r'nanoparticle\w*|biochar|fertiliz\w*|inoculat\w*)\b', re.I)

# 弱族：激素/信号分子本身不是实验设计。教科书句 "Auxin promotes cell
# elongation" 与实验句 "exogenous auxin promoted root elongation" 必须区分，
# 否则会把背景知识批量升格成证据。弱族必须同时出现处理语境才算。
_V5_TREAT_WEAK = re.compile(
    r'\b(GA3?|gibberellin\w*|ABA|abscisic|IAA|auxin\w*|jasmon\w*|'
    r'salicylic|brassinosteroid\w*|cytokinin\w*|ethylene|melatonin|'
    r'nitric\s+oxide|H2O2|hydrogen\s+peroxide)\b', re.I)
_V5_TREAT_CONTEXT = re.compile(
    r'\b(exogenous|applied|application|applications|treatment|treatments|'
    r'treated|sprayed|supplement\w*|addition|added|supply|supplied|'
    r'foliar|root\s+drench|pretreat\w*|co-?treat\w*)\b', re.I)

# 展望/设计说明语：用效应动词描述"可能性"或"研究设计意图"，不是观察到的事实。
_V5_OUTLOOK = re.compile(
    r'\b(may\s+help|might\s+help|could\s+help|can\s+facilitat\w*|'
    r'can\s+be\s+used|should\s+not|should\s+be|further\s+refinement|'
    r'enable\s+the\s+separation|providing\s+the\s+capacity|'
    r'future\s+studies|remains?\s+to\s+be|need\s+to\s+be)\b', re.I)

_V5_TREAT_EFFECT = re.compile(
    r'\b(increas\w*|decreas\w*|reduc\w*|enhanc\w*|improv\w*|'
    r'promot\w*|inhibit\w*|suppress\w*|alleviat\w*|mitigat\w*|'
    r'alter\w*|affect\w*|induc\w*|elevat\w*|accumulat\w*|'
    r'highest|lowest|greater|lower|higher|significant\w*|'
    r'confer\w*|restor\w*|impair\w*|abolish\w*|delay\w*|accelerat\w*)\b', re.I)



def _confidence(etype, finding, methods=''):
    """规则置信度（rule-v3）：表示**该论断在文本中的证据完备度**，不是统计概率。

    与 rule-v2 的区别：不再与类型绑定（旧实现让 descriptive 必然 low，
    于是低质量占比与类型占比完全同构，无法分别诊断）。
    """
    text = finding or ''
    if etype == 'descriptive/observational':
        return 'low'
    if etype == 'genetic perturbation':
        if _V3_PERT_DESIGN.search(text):
            return 'high'
        # 论断本身同时点名"扰动手段 + 效应"时，文本已具备因果三要素
        # （操纵、对照隐含、表型），与是否在方法字段写出 CRISPR 无关。
        # 2026-11-03：旧实现在 methods 为空时一律 medium，把
        # "CRISPR knockout of X reduced Y" 降成 medium，与规则语义不符。
        if _V3_PERT_NOUN.search(text) and _V3_EFFECT_VERB.search(text):
            return 'high'
        return 'high' if _V3_PERT_NOUN.search(methods or '') else 'medium'
    if etype in ('protein interaction', 'DNA binding/regulation'):
        return 'high' if (_V3_PHYS_METHOD.search(text) or _V3_DNA_METHOD.search(text)) else 'medium'
    if etype == 'expression/regulation':
        return 'medium' if _V3_EXPR.search(text) else 'low'
    return 'medium'


def _classify_base(finding, methods=''):
    """启发式证据类型（rule-v3，2026-11-03）。

    返回 (evidence_type, quality)。类型描述**该条 claim 能支持多强的推断**：
      protein interaction      物理互作（含"binds to/interacts with/磷酸化"谓词）
      DNA binding/regulation   直接结合/直接调控（promoter/ChIP/EMSA/反式激活）
      genetic perturbation     扰动—表型因果（mutant/knockout/CRISPR + 效应动词）
      omics/co-occurrence      组学共现（单细胞簇、共表达、图谱）
      phenotypic/association   关联（GWAS/QTL/自然变异/相关）
      expression/regulation    表达相关（qPCR/转录水平/上调下调）
      descriptive/observational 无设计、无谓词、无关联的陈述

    与 rule-v2 的差别：谓词优先。论文写没写 "Co-IP" 不该决定
    「CLV3 binds CLV1」这句话是不是互作证据。methods 仅作质量的先验，
    不把关联类论断升级成因果类。
    """
    text = (finding or '').strip()
    if not text:
        return 'descriptive/observational', 'low'

    # 1) 直接结合 / 直接调控 —— 必须排在物理互作之前。
    #    rule-v3 把互作放在前面，`binds?\s+the` 会先吃掉 "binds the promoter"，
    #    于是 ChIP-qPCR/promoter 结合被记成 protein interaction（实测复现）。
    if _V3_DNA_PRED.search(text) or _V3_DNA_METHOD.search(text):
        return 'DNA binding/regulation', _confidence('DNA binding/regulation', text, methods)

    # 2) 物理互作：谓词 or 方法名，二者之一即可（方法名单独出现也算设计证据）
    if _V3_INTERACTION_PRED.search(text) or _V3_PHYS_METHOD.search(text):
        return 'protein interaction', _confidence('protein interaction', text, methods)

    # 3) 扰动—因果：必须有扰动名词，且有效应动词或明确的构建语句
    if _V3_PERT_NOUN.search(text) and (
            _V3_EFFECT_VERB.search(text) or _V3_PERT_DESIGN.search(text)):
        return 'genetic perturbation', _confidence('genetic perturbation', text, methods)

    # 4) 组学共现
    if _V3_OMICS.search(text):
        return 'omics/co-occurrence', 'medium'

    # 4.6) rule-v5：因果/候选基因认定（QTL 克隆、图位克隆的结论句）
    if _V5_CAUSAL_GENE.search(text):
        return 'phenotypic/association', _confidence('phenotypic/association', text, methods)

    # 5) 关联
    if _V3_ASSOC.search(text):
        return 'phenotypic/association', 'medium'

    # 6) 表达
    if _V3_EXPR.search(text):
        return 'expression/regulation', _confidence('expression/regulation', text, methods)

    # 7) "X is required for Y"：功能性必要性陈述。没有扰动设计就不能算因果，
    #    但也不是纯描述——归入 expression/regulation 的低置信档。
    if _V3_FUNCTIONAL.search(text):
        return 'expression/regulation', 'low'

    # 7.5) rule-v5：非遗传处理 → 效应（本族规模最大，故置于最后，
    #      让表达类先命中，只有"处理改变性状/生理指标"才落到这里）。
    #      与 genetic perturbation 明确区分：本族只支持"该处理可改变该性状"，
    #      不支持"该基因必要/充分"。弱族（激素名）必须伴随处理语境。
    if _V5_TREAT_EFFECT.search(text) and (
            _V5_TREAT_STRONG.search(text)
            or (_V5_TREAT_WEAK.search(text) and _V5_TREAT_CONTEXT.search(text))):
        # 留出验证（30 条）中 4 条假阳性全是"展望/设计说明"句：
        # "further refinement may help improve"、"nano-formulations can
        # facilitate delivery"、"these strategies enable the separation"、
        # "should not be presented as direct endophyte evidence"。
        # 它们用效应动词描述可能性，不是本研究观察到的事实。
        if not _V5_OUTLOOK.search(text):
            return 'phenotypic/association', 'medium'

    return 'descriptive/observational', 'low'

_V8_NEG = re.compile(
    r'\b(did\s+not|does\s+not|do\s+not|failed\s+to|unable\s+to|cannot|'
    r'could\s+not|no\s+evidence\s+(?:for|of)|neither|not\s+significantly)\b', re.I)


_V8_PROMOTER_BG = re.compile(
    r'\b(promoter|cis-?element|transcription\s+start\s+site|enhancer)\b', re.I)
_V8_PERT_BG = re.compile(
    r'\b(mutants?|knock-?outs?|knock-?downs?|crispr|cas9|'
    r'over-?express\w*|rna[iI]|t-?dna|complementation|transgenic|'
    r'edited\s+lines?|loss-of-function|gain-of-function|silencing|'
    r'antisense|null\s+alleles?|allelic\s+series)\b', re.I)
_V8_PHYS_BG = re.compile(
    r'\b(co-?ip|coimmunoprecipitation|y2h|yeast\s+two-hybrid|bifc|'
    r'pull-?down|fret|split-luciferase|spr|mst|two-hybrid|'
    r'affinity\s+purification|protein-?protein)\b', re.I)
_V8_DNA_BG = re.compile(
    r'\b(chip(?:-seq|-qpcr)?|emsa|dap-?seq|transactivation\s+assay|'
    r'chromatin\s+immunoprecipitation|dna-?binding)\b', re.I)
_V8_DNA_WORD = re.compile(r'\b(dna|chromatin|nucleosome|histone|promoter)\b', re.I)
_V8_PARTNER = re.compile(
    r'\b([A-Z][A-Za-z0-9]{1,9}\d[A-Za-z0-9]*|[A-Z]{2,}[0-9]*|'
    r'protein|receptor|kinase|phosphatase|ligand|peptide|transcription\s+factor)\b')


# ── rule-v9 收紧（2026-11-07）────────────────────────────────────────
# v8 首轮实跑的教训（382 条迁移逐条审计）：
#   * 182 条 expression/regulation -> genetic perturbation 是错的，
#     例："GSH1 and GSH2 are essential for GSH biosynthesis"（背景句）、
#     "hormone balance is necessary for callus induction"（教科书陈述）；
#   * 根因是"方法字段含 CRISPR"被当成"这句话做了遗传扰动"；
#   * 另有 "phytochrome B interaction ... over PIF7" 被读成 DNA 结合。
# v9 因此规定：
#   1) 只有 claim_role=finding 的句子可回收，background/outlook 一律不动；
#   2) 表达量变化不升级为遗传扰动（它是表达证据，不是因果扰动证据）；
#   3) "is required/essential for" 只在**句内**出现扰动线索 + 基因符号时升级；
#   4) 物理互作必须给出具名伙伴或互作方法背景，不靠"promoter"字样碰运气。
_V8_DNA_TARGET = re.compile(
    r'\b(binds?|bound\s+by|targets?|recogni[sz]es?)\s+(?:the\s+)?'
    r'(?:promoters?|cis-?elements?|enhancers?|regulatory\s+regions?)\b', re.I)
_V8_STRONG_PHYS = re.compile(
    r'(\b(binds?\s+to\s+[A-Z][A-Za-z0-9]*|binds?\s+[A-Z][A-Za-z0-9]*[0-9]|'
    r'interacts?\s+with|interaction\s+with|forms?\s+(?:a\s+)?(?:hetero)?complex\s+with|'
    r'phosphorylates|dephosphorylates|ubiquitinates|sumoylates|'
    r'is\s+phosphorylated\s+by|is\s+ubiquitinated\s+by)\b)', re.I)
_V8_DIRECT_REG = re.compile(
    r'(\b((?:directly\s+)?(?:activates|represses|suppresses|induces|enhances)\s+'
    r'(?:the\s+)?(?:expression|transcription)\s+of|'
    r'directly\s+(?:activates|represses|targets|regulates)|'
    r'transactivates|transactivated\s+by|'
    r'negatively\s+regulates|positively\s+regulates)\b)', re.I)
_V8_REQ_FOR = re.compile(
    r'\b(is|are|was|were)\s+(required|essential|necessary)\s+for\b', re.I)
_V8_MUTANT_SUBJECT = re.compile(
    r'(\b[A-Za-z]{2,}[a-z]?\d+-\d+\b|\bSTTM\b|\bOE-?\d|\b35S:|\bamiR|'
    r'\b[A-Z]{2,}\d+[a-z]?-\d+\b|\b[A-Z]{2,}\d+(?:ox|OE)\b)')
_V8_PHENO_VERB = re.compile(
    r'\b(exhibits?|exhibited|shows?|showed|display(?:s|ed)?|confer(?:s|red)?|'
    r'reduces?|reduced|increases?|increased|impairs?|impaired|restores?|restored|'
    r'abolishes?|abolished|attenuates?|attenuated|enhances?|enhanced)\b', re.I)


def _recover_causal(finding, methods='', role='finding'):
    """descriptive -> 因果类的保守回收（rule-v9）。命中返回新类型，否则 ''。"""
    text = (finding or '').strip()
    if not text:
        return ''
    # 1) 非 finding 句（背景/展望/方法）不得升级
    if role and role != 'finding':
        return ''
    if _V5_OUTLOOK.search(text) or _V8_NEG.search(text):
        return ''
    prior = methods or ''
    has_phys = bool(_V8_PHYS_BG.search(prior))
    has_dna = bool(_V8_DNA_BG.search(prior))
    has_pert_in_text = bool(_V8_PERT_BG.search(text))

    # 2) 明确的启动子/DNA 靶标陈述
    if _V8_DNA_TARGET.search(text) and _V8_PROMOTER_BG.search(text):
        return 'DNA binding/regulation'

    # 3) 物理互作/修饰：需要互作方法背景，或句内点名分子伙伴
    if _V8_STRONG_PHYS.search(text):
        if has_phys:
            return 'protein interaction'
        if _V8_PARTNER.search(text):
            return 'protein interaction'
        return ''

    # 4) 直接转录调控：只在有启动子/DNA 语境时归为 DNA 结合调控
    if _V8_DIRECT_REG.search(text):
        if _V8_PROMOTER_BG.search(text) or has_dna:
            return 'DNA binding/regulation'
        return ''

    # 5) 必要性陈述：仅句内自带扰动线索 + 基因符号，才视为遗传扰动证据
    if _V8_REQ_FOR.search(text):
        if has_pert_in_text and re.search(r'\b[A-Z][A-Za-z0-9]{1,9}\d', text):
            return 'genetic perturbation'
        return ''

    # 6) 突变体/转基因株系作主语 + 表型动词
    if _V8_MUTANT_SUBJECT.search(text) and _V8_PHENO_VERB.search(text):
        return 'genetic perturbation'
    return ''


def classify_ex(finding, methods='', role=None):
    """返回 (evidence_type, quality, prior_type)。

    prior_type 非空表示该条经 rule-v9 回收，原值为 descriptive/observational。
    rule-v9 起不再回收 expression/regulation：表达量变化属于表达证据，
    不是遗传因果关系，把它改写成 genetic perturbation 会系统性高估因果强度。
    """
    etype, quality = _classify_base(finding, methods)
    if role is None:
        role, _nf = claim_role_kind(finding or '')
    if etype == 'descriptive/observational':
        rec = _recover_causal(finding, methods, role)
        if rec and rec != etype:
            return rec, _confidence(rec, finding, methods), etype
    return etype, quality, ''


def classify(finding, methods='', role=None):
    etype, quality, _prior = classify_ex(finding, methods, role)
    return etype, quality


# ── 论断角色（rule-v6，2026-11-04）──────────────────────────────────
# rule-v4 的 claim_role 事实上没有分层能力：finding 占 95.3%
# （17386/18239）。根因是结构性的，不是词表不够——
#   _ROLE_FINDING 排在第一位，且它宽到涵盖 "suggest that"、"was associated"、
#   "significantly"，于是 method / background 两个分支几乎永远轮不到执行。
# rule-v6 把判定顺序反过来：
#   1) 明确的**结果句**（第一人称结果、results/数据主语、统计标记、直接互作、
#      变化动词、observed in this study）→ finding，且优先级最高，
#      防止"真结果 + 一句 textbook 尾巴"被降级；
#   2) 明确的方法句 → method；
#   3) 目的 / 展望 / 推测 / 教科书共识 / 定义 → background（非发现）；
#   4) 只有弱发现措辞（suggest that、in conclusion…）才兜底成 finding。
# 取值域保持不变（finding / method / background）：下游 batch_synthesis 与
# batch_hypotheses 用 role in ('method','background') 剔除，新增取值会**绕过**
# 闸门，故另用 non_finding_kind 记录细分原因，供审计而不影响闸门。
_ROLE_STRONG_FINDING = re.compile(
    r'(here\s+we\s+(show|demonstrate|report|find)|'
    r'\bwe\s+(found|show|demonstrate|report|observed|identified|detected|'
    r'measured|quantified|compared|tested|confirmed|established|determined|'
    r'revealed|discovered|isolated|obtained|produced|generated|cloned)\b|'
    # 2026-11-04：#22 类样本是"标题与正文粘连"，结果动词前有很长的从句，
    # 固定窗口 12 词内允许，仍要求 and + 结果动词这一形态，不做无限放宽。
    r'\bwe\s+\S+(\s+\S+){0,14}\s+and\s+(identified|found|observed|detected|confirmed)\b|'
    # "the results of this study demonstrate…" 与 "results consistently identify…"
    r'\b(results?|findings?|data|analyses)\s+(of|from)\s+(this|the|our)\s+'
    r'(study|work|analysis|experiment\w*)?[\s,]*'
    r'(consistently\s+)?(show|indicate|demonstrate|reveal|confirm|suggest|'
    r'provide|identif\w+|support\w*)|\b(results?|findings?|data)\s+'
    r'(consistently\s+)?(show|indicate|demonstrate|reveal|confirm|identif\w+)|'
    r'\b(these|our)\s+(results?|findings?|data|analyses)\s+'
    r'(show|showed|indicate|indicated|demonstrate|demonstrated|reveal|'
    r'revealed|confirm|confirmed|support|supported|suggest|suggested|'
    r'identify|identified|provide|provided)\b|'
    r'\bobserved\s+in\s+(this|the\s+present)\s+study\b|'
    r'\b(this|these)\s+(further\s+)?(indicates?|indicated)\s+that\b|'
    r'\b(this|our|the\s+present)\s+(study|work|paper|analysis|research|'
    r'survey)\s+(reveals?|shows?|demonstrates?|indicates?|confirms?|'
    r'establishes?|identifies?)\b|'
    r'\bwe\s+conclude\s+that\b|'

    # 2026-11-04：单个强度副词不足以压过"教科书背景/目的"家族。
    # 反例 "Cluster roots … dramatically increase root absorbing area … play a
    # key role in nutrient scavenging" 被误抬成结果句。强度副词下沉到
    # _ROLE_RESULT_MID；"was significantly higher" 这类系动词形态仍在第一层。
    r'\b\d+(\.\d+)?[- ]?fold\s+(higher|lower|increase\w*|decrease\w*|'
    r'reduction|change\w*|up-?regulat\w*|down-?regulat\w*)|'
    r'\bdirectly\s+(binds?|activates?|represses?|regulates?|interacts?)\b|'
    r'\b(is|are|was|were)\s+(significantly\s+)?(higher|lower|greater|reduced|'
    r'increased|enhanced|suppressed|induced|promoted|inhibited|decreased|'
    r'elevated|abolished|impaired|restored|accelerated|delayed|detected|'
    r'identified|observed|found|enriched|up-?regulated|down-?regulated)\b|'
    r'\bexhibit(ed|s)\b|\bresulted\s+in\b|'
    r'\bresults?\s+in\s+(?:a|an|the|higher|lower|increased|decreased|reduced|'
    r'enhanced|significant|marked|substantial)\b'
    r'|\bled\s+to\b)'
    r'|(?<![\w-])p\s*[<=]\s*0\.0[0-9]', re.I)

# 中等结果信号（rule-v6 第二层）：单独出现不足以压过"目的/展望/推测"，
# 但排除掉那些之后，仍指向结果句。专门接收两类被证明不能放进第一层的形式：
#   (a) 互作/结合动词——"interact with other components" 常见于展望句；
#   (b) 主动语态变化动词 + 宾语——"for reduced ANFs"/"elevated temperatures"
#       这类分词作形容词的用法必须排除，故要求后接宾语或性状名词。
# 2026-11-04 抽样证据：放宽这两族到第一层会让 4/40 条非发现句被误判为结果。
_ROLE_RESULT_MID = re.compile(
    r'(\bsignificantly\b|\bmarkedly\b|\bdramatically\b|\bsubstantially\b|'
    r'\b(binds?|binds?\s+to|interacts?\s+with|co-?immunoprecipitat\w*|'
    r'co-?purif\w*)\b|'
    r'\b(increas|decreas|reduc|enhanc|elevat|improv|promot|suppress|inhibit|'
    r'abolish|impair|restor|accelerat|delay)(ed|es)\s+'
    r'(the|a|an|its|their|this|these|expression|level|levels|content|'
    r'accumulation|tolerance|growth|yield|biomass|activity|resistance|'
    r'sensitivity|germination|seed|seedling|root|shoot|flowering)\b)', re.I)

# 弱发现措辞：单独出现不足以证明是结果（"…, suggesting that"常见于讨论），
# 但在排除掉目的/展望/推测/教科书/方法之后，仍是结果句的最可能来源。
_ROLE_WEAK_FINDING = re.compile(
    r'\b(show(ed|s)?\s+that|reveal(ed|s)?\s+that|indicat\w+\s+that|'
    r'suggest\w*\s+that|demonstrat\w+\s+that|consistent\s+with|'
    r'in\s+conclusion|in\s+summary|collectively|taken\s+together|'
    r'(positive|negative)\s+correlat\w+|correlat\w+\s+with|'
    r'(was|were)\s+(identified|detected|observed|found|enriched|associated))\b', re.I)

_ROLE_METHOD = re.compile(
    r'\b((were|was)\s+(analy[sz]ed|performed|measured|collected|extracted|'
    r'quantified|purified|incubated|centrifuged|sequenced|amplified|'
    r'determined|cultured|grown|harvested|cloned|transformed|transfected|'
    r'ligated|constructed|inserted)\b|'
    r'sds-?page|coomassie|sodium\s+dodecyl|according\s+to\s+the\s+manufacturer|'
    r'molecular\s+docking|ligand\s+structures\s+were\s+obtained|'
    r'we\s+(used|performed|conducted|carried\s+out)\b|'
    r'\b(we|they)\s+(then\s+)?(examined|assessed|compared|screened)\b|'
    r'\b(were|was)\s+(designed|synthesi[sz]ed|selected|ordered|chosen|used)\b|'
    r'\busing\s+(an?|the)\s+(kit|antibody|primer|protocol|software|plasmid|'
    r'vector)\b|'
    r'materials?\s+and\s+methods?|'
    r'\b(ensured|enabled|allowed|permitted)\s+the\s+(subsequent|accurate|'
    r'reliable|robust)\b)\b', re.I)

# 研究目的/设问：说的是"要研究什么"，不是结果
_ROLE_AIM = re.compile(
    r'(\b(to|in\s+order\s+to)\s+(investigate|elucidate|understand|determine|'
    r'explore|assess|evaluate|examine|characteri[sz]e|identify|reveal|'
    r'clarify|uncover|unravel|dissect|gain\s+insight)\b|'
    r'\b(we|here|this\s+study)\s+(aim|aimed|aims|attempt|attempted|'
    r'set\s+out|sought|seek)\b|'
    r'\b(the|our)\s+(aim|objective|goal|purpose)\s+of\b|'
    r'\bwas\s+designed\s+to\b|\bwe\s+ask(ed)?\s+(whether|how|if)\b|'
    r'\bis\s+necessary\s+to\b|'
    r'\b(further|additional|more)\s+\w+\s+(is|are)\s+required\b|'
    r'\bis\s+(crucial|important|essential)\s+to\s+(?:\w+ly\s+)?'
    r'(understand|elucidat|clarif|identify|determine|study|explore|ensur|'
    r'maintain|delineate|quantify|provide|develop|establish|gain\s+insight))',
    re.I)

# 展望：未来工作 / 应用建议，不是已完成的发现
_ROLE_OUTLOOK = re.compile(
    r'(\bfuture\s+(studies|work|research|investigations|efforts)\b|'
    r'\bfurther\s+(studies|work|research|investigations|analyses|'
    r'genetic\s+confirmation)\b|'
    r'\bwarrant(s|ed)?\s+(further|additional)?\b|'
    r'\bremains?\s+to\s+be\s+(determined|elucidated|tested|established|'
    r'clarified|explored)\b|'
    r'\bshould\s+be\s+(further\s+)?(investigated|explored|studied|tested|'
    r'validated|confirmed|examined)\b|'
    r'\b(have|has)\s+yet\s+to\s+be\s+(studied|examined|explored|tested|'
    r'determined|investigated|elucidated)\b|'
    r'\bshould\s+(conform|match|correspond|align|coincide|coin)\b|'
    r'\bshould\s+include\b|'
    r'\blimitations?\s+remain\b|'
    r'\bopens?\s+(up\s+)?(new\s+)?(avenues|possibilities|directions)\b|'
    r'\bholds?\s+promise\b|'
    r'\b(can|could|may|might)\s+be\s+(used|applied|evaluated|exploited|'
    r'employed|utilized|harnessed)\b|'
    r'\b(can|could|may|might)\s+(also\s+)?serve\s+as\b|'
    r'\bpromising\s+(candidate|target|strategy|approach)\b)', re.I)

# 推测/假设：无实验支撑的可能性陈述
_ROLE_SPECULATION = re.compile(
    r'(\bwe\s+(hypothesi[sz]e|speculate|postulate)\b|'
    r'\bit\s+is\s+(likely|possible|plausible|probable|conceivable|'
    r'anticipated|unclear)\s+that\b|'
    r'\b(may|might|could)\s+(be|play|serve|represent|contribute|reflect|act|'
    r'function|account|underlie|mediate|explain|result)\b|'
    r'\b(are|is|was|were)\s+(thought|likely)\s+to\b|'
    r'\bhave\s+been\s+(proposed|suggested)\s+to\b|'
    # 2026-11-04："<标题> Hybridization proposes combining…" 是设想不是结果
    r'\bproposes?\s+(a|an|the|that|combining|to)\b)', re.I)

# 教科书式背景：领域共识/转载引用，不是本文结果
_ROLE_TEXTBOOK = re.compile(
    r'(\b(is|are)\s+(known|well\s+documented|well\s+established|'
    r'widely\s+reported|generally\s+accepted)\b|'
    r'\bit\s+is\s+(generally|widely|well)\s+(accepted|known|recogni[sz]ed|'
    r'documented|established)\b|'
    r'\bhas\s+(long\s+)?been\s+(known|recogni[sz]ed|reported|studied|'
    r'documented)\b|'
    # 2026-11-04："was reported to interact with…" 是文献转述，不是本文结果
    r'\b(is|are|was|were|has\s+been|have\s+been|had\s+been)\s+'
    r'(reported|shown|demonstrated|found|suggested|proposed)\s+to\b|'
    r'\bplay(s|ed)?\s+(a|an)\s+(crucial|key|central|important|pivotal|'
    r'critical|vital|essential|fundamental)\s+role\b|'
    r'\bis\s+(key|critical|essential|crucial|central|vital)\s+to\s+'
    r'(determining|ensuring|maintaining|achieving|understanding)\b|'
    r'\bis\s+(one|among)\s+of\s+the\s+(most|major|key)\b|'
    # 2026-11-04 升级样本：#13-#16/#18/#49 一类\"承接共识\"的系表句
    r'\b(is|are)\s+(the\s+)?(dominant|major|main|principal)\s+\w+|'
    r'\b(is|are)\s+(essential|required|necessary)\s+for\b|'
    r'\b(is|are)\s+(critical|essential|important|key|vital|central)\s+for\s+'
    r'(the|successful|reliable|accurate|effective|proper)\b|'
    r'\b(is|are)\s+(essential|critical|necessary)\s*(?=[.;])|'
    r'\bremains?\s+(a|an|the)\s+(primary|major|main|key|common|important)\b|'
    r'\b(is|are)\s+(maintained|kept)\s+at\s+a\s+(low|constant|steady|stable)\b|'
    # 2026-11-04：is highly conserved / is often referred to as 是共识句
    r'\b(is|are|was|were)\s+(highly|strongly|well|widely|evolutionarily|'
    r'largely|relatively)\s+(conserved|maintained|preserved|homologous)\b|'
    r'\b(is|are)\s+(often|commonly|generally|usually|typically)\s+'
    r'(referred\s+to\s+as|regarded\s+as|considered\s+as|described\s+as|'
    r'known\s+as)\b|'
    r'\bin\s+our\s+(previous|earlier|prior)\s+(research|study|work|studies|'
    r'paper|analyses)\b|'
    r'\brequire(s|d)?\s+risk\s+assessment\b|'
    r'\b(have|has)\s+been\s+(extensively|widely|intensively)\s+'
    r'(studied|investigated|reported|reviewed)\b)', re.I)

# 定义/分类学陈述
_ROLE_DEFINITION = re.compile(
    r'(\bis\s+defined\s+as\b|\brefers?\s+to\b|\bconsists?\s+of\b|'
    r'\bis\s+characteri[sz]ed\s+by\b|'
    r'\bbelongs?\s+to\s+the\s+(family|genus|class|order|group)\b|'
    r'\bis\s+a\s+(member|type|kind|class)\s+of\b|^the\s+phrase\b|'
    r'\b(is|are)\s+a\s+(?:\w+\s+){0,2}(strategy|approach|method|technique|'
    r'tool|process|phenomenon)\b|'
    r'\([ACGT]{4,}\)|'
    r'\bconvert(s|ed)?\s+\w+\s+(information|signals?)\s+into\b)', re.I)

# 2026-11-04：图注/表注（"Sample image of …: (a) … (b) …"）是说明文字，不是发现
_ROLE_CAPTION = re.compile(
    r'^\s*\d{1,3}\s+[A-Z][^.]{0,90}\(\w\)\s')

_ROLE_BACKGROUND = re.compile(
    r'\b(is|are)\s+(critical|essential|important|crucial|key|vital|central)\s+'
    r'(to|for)\s+'
    r'(understand|elucidat|clarif|breed|develop|improv|ensur|maintain|'
    r'calibrat|model\w*|increas|reduc|enhanc)|'
    r'\bSDGs?\s?\d?\b|'
    r'\bwe\s+still\s+(largely\s+)?(lack|do\s+not\s+know)|'
    r'\bremains?\s+(largely\s+)?(unknown|elusive|unclear)|'
    r'\btherefore,?\s+(clarifying|understanding|elucidating)|'
    r'\bin\s+this\s+context\b|'
    r'\bwill\s+be\s+discussed\b|'
    r'\bthese\s+(observations|findings)\s+highlight\s+the\s+potential\b|'
    r'\bof\s+(specific|particular|great|special)\s+interest\s+'
    r'(were|was|is|are)\b', re.I)

# 2026-11-04 事故：'325 These results indicate that...' 被 '^\d+ +[A-Z]\w+' 判成
# 小标题 → 结果句被打成 method。标题是短名词短语，不含从句连接词。
_ROLE_HEADING = re.compile(
    r'^\s*\d{1,3}(\.\d{1,3}){0,2}\s+[A-Z][A-Za-z]+(?![a-z])')
_ROLE_HEADING_MAXLEN = 90
_ROLE_HEADING_STOP = re.compile(
    r'\b(that|which|who|is|are|was|were|indicate|indicating|suggest|'
    r'suggesting|show|showing|reveal|revealing|may|might|could)\b', re.I)

# 2026-11-04 抽样：\"3.2.3 Analysis of genes expression in response to drought
# To gain insight into…\" 这类\"编号标题 + 首句\"粘连片段，长度超出
# _ROLE_HEADING_MAXLEN 而漏过标题判定，随后被中等信号抬成结果句。
# 处理方式是\"剥掉编号标题前缀后再判一次\"，且只在剥完后命中非发现家族、
# 且剥完后不含强结果标记时才降级——方向只有向下，不会把方法句抬成结果。
_ROLE_SECTION_NUM = re.compile(r'^\s*\d{1,3}(\.\d{1,3}){0,2}[.):]?\s+')


def _heading_split_kind(t):
    m = _ROLE_SECTION_NUM.match(t)
    if not m:
        return ''
    rest = t[m.end():]
    for i in range(8, min(len(rest), 120)):
        if rest[i - 1] in ' )\u201d\u2019' and rest[i].isupper() \
                and not rest[i:i + 2].isupper():
            tail = rest[i:].strip()
            if len(tail) < 15:
                continue
            if _ROLE_STRONG_FINDING.search(tail):
                return ''
            for kind, rx in _NONFINDING_ORDER:
                if rx.search(tail):
                    return kind
    return ''


# 强度副词单独出现不构成结果（见上），但当它与弱发现措辞同现时，
# 说明作者在报道本研究的量级变化，此时被动式方法族（"was performed"）不得抢占。
_ROLE_RESULT_ADVERB = re.compile(
    r'\b(significantly|markedly|dramatically|substantially)\b', re.I)

# 2026-11-04 降级抽查发现的 3/30 误判：
#   "These results suggests that the SHR:GR fusion protein fully complements …
#    and that … can be used to identify …"          → 目的措辞在从句里
#   "… greatly enhanced soil moisture …, which are essential for …"  → 从句里的教科书措辞
#   "As with FAMA targets, RBR is required for repression of SCR target genes …
#    Figure 3."                                     → 有图表指涉，是本文结果
# 处理：非发现措辞若处在关系从句里、或整句带图表指涉、或出现在结果措辞之后，
# 都不足以覆盖句子主干，继续往下判。
_ROLE_CLAUSE_LINK = re.compile(r'(?:which|that|whereby|thereby)\s*$', re.I)
# 关系从句让位的前提是"主句已经陈述了本研究的观察"：
#   "… greatly enhanced soil moisture …, which are essential for …"  → 让位
#   "… glnA encodes …, while glnB encodes …, which plays a central role"  → 不让位
# 2026-11-04：本条只负责"主句是否已经陈述了观察"。旧版把分词/形容词
# （Predefined、regulated、related、ensured、encoded）也算进来，导致
# "…, which are essential for …" 的教科书从句被强行放行。现改为先掩掉
# 分词式归属（_mask_participle）再匹配，正则本身保持宽松，避免把
# "…is indicative of enhanced activity…" 这类主动过去式一起否掉。
_ROLE_MAIN_ASSERTION = re.compile(
    r'(?<!-)\b\w{3,}ed\b|\b(?:was|were)\b', re.I)
_ROLE_DATAREF = re.compile(r'\b(fig(?:ure)?s?\.?|tables?)\s*\d', re.I)
# 只有"报道动词"才算句子主干；"Collectively"/"in conclusion" 这类话语标记
# 不构成结果主干（patch13 首版用 _ROLE_WEAK_FINDING 导致 #14/#27 误升）。
_ROLE_REPORT_CORE = re.compile(
    r'\b(?:show|shows|showed|shown|reveal|reveals|revealed|indicate|indicates|'
    r'indicated|demonstrate|demonstrates|demonstrated|identify|identifies|'
    r'identified|detect|detects|detected|found|observe|observes|observed|'
    r'measure[sd]?|quantif\w+|confirm(?:s|ed)?|complement(?:s|ed)?)\b', re.I)


# 2026-11-04：分词式归属。修饰语里的报道动词不构成句子主干；
# 若把它当报道核心，目的/展望/推测家族会被 core.start() < m.start() 挡掉。
_PARTICIPLE_ATTR = re.compile(
    r'\b(identified|detected|observed|found|measured|quantified|predicted|'
    r'selected|annotated|reported|described|encoded|obtained|derived|'
    r'generated|regulated|related)\s+(in|from|by|during|across|among|using|'
    r'with|under|for|through)\b|'
    # 定语式分词：副词 + -ed + 名词（"newly identified marker genes"）
    r'\b(?:newly|recently|previously)\s+\w+(?:ed|en)\s+\w+', re.I)


def _mask_participle(text):
    # 把分词式归属整段替换为等长空白，位置不变，便于跨正则比对 offset
    return _PARTICIPLE_ATTR.sub(lambda m: ' ' * (m.end() - m.start()), text)


# 文献归属句：作者在转述他人工作，不是本文结果。
# 只认"非第一人称主语 + 已经/已被/近期研究"两类框架；从句里的归属让位给主句。
_ROLE_LIT_REPORT = re.compile(
    r'(\b(has|have)\s+(also\s+|recently\s+|previously\s+|long\s+|'
    r'already\s+)?(been\s+)?(shown|reported|demonstrated|identified|'
    r'revealed|suggested|proposed|documented|described|established)\b|'
    r'\b(recent|previous|earlier|prior|several|many|other)\s+'
    r'(research|studies|study|work|works|reports?|authors?)\s+(has|have)?\s*'
    r'(identified|shown|reported|demonstrated|revealed|found|suggested|'
    r'described|established)\b)', re.I)
_ROLE_FIRST_PERSON = re.compile(r'\b(we|our|us|i)\b', re.I)
# 总结标记出现时，句子的主体是本文自己的结果：
# "In summary, gene expression profiling has revealed that …" 不是转述他人。
_ROLE_SUMMARY_MARK = re.compile(
    r'\b(in\s+summary|in\s+conclusion|collectively|taken\s+together|'
    r'to\s+sum\s+up)\b', re.I)

# 非发现原因的判定顺序（与 claim_role 一致，用于诊断字段）
_NONFINDING_ORDER = (
    ('method', _ROLE_METHOD),
    ('aim', _ROLE_AIM),
    ('outlook', _ROLE_OUTLOOK),
    ('speculation', _ROLE_SPECULATION),
    ('textbook', _ROLE_TEXTBOOK),
    ('definition', _ROLE_DEFINITION),
    ('background', _ROLE_BACKGROUND),
    ('background', _ROLE_CAPTION),
)


_ROLE_METHOD_KINDS = ('method', 'aim')


def _role_for_kind(kind):
    """非发现细分原因 -> 三元 role。

    rule-v6 把 role 保持为 finding/method/background 三个取值，细分原因写进
    non_finding_kind。映射必须保住 rule-v5 的语义：程序性陈述（方法/研究设计）
    归 method，知识性/推测性陈述（教科书、定义、背景、展望、推测）归 background。
    上游若把 textbook 也塞进 method，会让"方法句"统计虚高，且丢失
    "这是背景铺垫"的原始含义。
    """
    return 'method' if kind in _ROLE_METHOD_KINDS else 'background'


def claim_role_kind(text):
    """返回 (role, kind)。

    kind ∈ {result, method, aim, outlook, speculation, textbook, definition,
            background, ''}。role 仍只有三个取值，保证下游闸门语义不变。
    """
    t = (text or '').strip()
    if not t:
        return 'background', 'background'
    if _ROLE_HEADING.match(t) and len(t) <= _ROLE_HEADING_MAXLEN \
            and not _ROLE_HEADING_STOP.search(t):
        return 'method', 'method'
    split_kind = _heading_split_kind(t)
    if split_kind:
        return _role_for_kind(split_kind), split_kind
    if _ROLE_STRONG_FINDING.search(t):
        return 'finding', 'result'
    t_main = _mask_participle(t)
    _lit = _ROLE_LIT_REPORT.search(t_main)
    # 第一人称出现在句中任意位置都不算纯转述：
    # "While previous studies have shown X, our study provides Y" 是本文贡献。
    if _lit and not _ROLE_FIRST_PERSON.search(t_main) \
            and not _ROLE_SUMMARY_MARK.search(t_main) \
            and not _ROLE_CLAUSE_LINK.search(t_main[:_lit.start()]) \
            and not _ROLE_DATAREF.search(t):
        return 'background', 'background'
    _adv = _ROLE_RESULT_ADVERB.search(t)
    _weak = _ROLE_WEAK_FINDING.search(t)
    _core = _ROLE_REPORT_CORE.search(t_main)
    _data = _ROLE_DATAREF.search(t)
    for kind, rx in _NONFINDING_ORDER:
        m = rx.search(t)
        if not m:
            continue
        if kind == 'method' and _adv and _weak:
            continue
        if kind in ('textbook', 'definition'):
            _prefix = t_main[:m.start()]
            if _ROLE_CLAUSE_LINK.search(_prefix) \
                    and _ROLE_MAIN_ASSERTION.search(_prefix):
                continue
            if _data and _ROLE_MAIN_ASSERTION.search(t_main):
                continue
        if kind in ('aim', 'outlook', 'speculation') \
                and _core and _core.start() < m.start():
            continue
        return _role_for_kind(kind), kind
    if _ROLE_RESULT_MID.search(t):
        return 'finding', 'result'
    if _ROLE_WEAK_FINDING.search(t):
        return 'finding', 'result'
    return 'finding', ''


def claim_role(text):
    """论断角色：finding / method / background（rule-v6 判定顺序见上）。"""
    return claim_role_kind(text)[0]


def non_finding_kind(text):
    """非发现的细分原因；是结果句时返回空串。"""
    return claim_role_kind(text)[1]


def _set_frontmatter_field(text, key, value):
    """只改 frontmatter 的单个字段，缺字段则追加；正文保持字节不变。"""
    if not text.startswith('---'):
        return text
    end = text.find('\n---', 3)
    if end < 0:
        return text
    fm, rest = text[3:end], text[end:]
    pat = re.compile(r'^%s\s*:.*$' % re.escape(key), re.M)
    line = '%s: "%s"' % (key, value)
    if pat.search(fm):
        fm = pat.sub(line, fm, count=1)
    else:
        fm = fm.rstrip('\n') + '\n' + line + '\n'
    return '---' + fm + rest


RULE_VERSION = 'rule-v9-20261107'


# rule-v8：方法先验的第二来源。论文页里只有 30% 带 ``方法`` 字段，
# 但 164 条"含因果谓词的 descriptive"证据中，有 106 条的源论文正文明确出现了
# ≥2 类实验方法关键词（Co-IP / CRISPR / ChIP / 突变体 …）。字段缺失不代表
# 没做实验，因此增加正文兜底：只有命中 ≥2 个不同方法族才生效，避免把引言里
# 顺带一提的 CRISPR 当成实验设计证据。
_METHOD_FAMILIES = (
    ('interaction', re.compile(
        r'\b(co-?ip|coimmunoprecipitation|yeast\s+two-hybrid|y2h|bifc|'
        r'pull-?down|split-luciferase|fret|spr|itc|mst)\b', re.I)),
    ('dna', re.compile(
        r'\b(chip(?:-seq|-qpcr)?|emsa|dap-?seq|transactivation\s+assay|'
        r'chromatin\s+immunoprecipitation)\b', re.I)),
    ('perturbation', re.compile(
        r'\b(crispr|cas9|knock-?outs?|knock-?downs?|rna[iI]|vigs|t-?dna|'
        r'over-?express\w*|transgenic|mutants?|complementation)\b', re.I)),
    ('expression', re.compile(
        r'\b(rna-?seq|transcriptom\w+|qrt-?pcr|microarray|single-?cell)\b', re.I)),
    ('imaging', re.compile(
        r'\b(confocal|gfp|yfp|fluorescen\w+|in\s+situ\s+hybridization)\b', re.I)),
)


def _methods_from_body(text):
    """从论文正文提取方法族标签；少于 2 族返回空串（保守）。"""
    hits = [name for name, rx in _METHOD_FAMILIES if rx.search(text)]
    return ', '.join(hits) if len(hits) >= 2 else ''


def _paper_methods_index():
    """DOI -> 论文方法先验（方法字段优先，正文方法族兜底）。

    rule-v2 只看 claim 一句话，看不到"这篇论文用了 Co-IP/CRISPR"这一层
    设计信息；rule-v8 补上正文兜底，修"字段缺失 = 无实验"的假阴性。
    """
    idx = {}
    for d in (CONCEPTS_DIR, os.path.join(BASE, 'concepts')):
        if not os.path.isdir(d):
            continue
        for fn in os.listdir(d):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(d, fn)
            try:
                head = io.open(p, encoding='utf-8', errors='ignore').read(6000)
            except OSError:
                continue
            dm = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s\n"\]\]]+)', head, re.M | re.I)
            if not dm:
                continue
            mm = re.search(r'^\*\*方法\*\*:\s*(.+?)$', head, re.M)
            methods = mm.group(1).strip() if mm else ''
            if not methods:
                try:
                    methods = _methods_from_body(
                        io.open(p, encoding='utf-8', errors='ignore').read())
                except OSError:
                    methods = ''
            idx.setdefault(dm.group(1).rstrip('/.'), methods)
    return idx


def _sync_annotation_block(text, etype, quality, role=''):
    """把正文「标注信息」块里的类型/等级同步成 frontmatter 的值。

    2026-11-03 发现的不一致：frontmatter 写 descriptive/observational，
    正文仍写「证据类型: expression/regulation」——同一页两套说法，
    读者与下游都会被误导。术语一致性必须由写入者保证。
    """
    text = re.sub(r'(- 证据类型:\s*).*$', lambda m: m.group(1) + etype, text, count=1, flags=re.M)
    # 术语一致性：'质量等级' 会被读成"研究质量高/低"，实际语义是"这条论断的
    # 文本完备度"。改名而不改值，避免下游脚本与历史页面出现两套口径。
    text = re.sub(r'- 质量等级:\s*.*$',
                  '- 论断证据完备度: %s（该条论断的文本完备度，不代表研究质量）' % quality,
                  text, count=1, flags=re.M)
    text = re.sub(r'- 论断证据完备度:\s*.*$',
                  '- 论断证据完备度: %s（该条论断的文本完备度，不代表研究质量）' % quality,
                  text, count=1, flags=re.M)
    if '- claim_role:' not in text:
        text = re.sub(r'(- 证据类型:\s*.*)$', r'\1\n- 论断角色: %s' % role, text, count=1, flags=re.M)
    else:
        text = re.sub(r'- 论断角色:\s*.*$', '- 论断角色: %s' % role, text, count=1, flags=re.M)
    return text


def _iter_evidence_paths(root=None):
    """遍历 evidence 下的证据页（含 _orphan 等归档子目录）。

    主集合在 evidence/ 顶层；归档孤儿在 evidence/_orphan/。两者都可能被
    reclassify 改写，所以这里统一递归，保证 basis 字段在全库口径一致。
    """
    root = root or EVIDENCE_DIR
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames.sort()
        for fn in sorted(filenames):
            if fn.endswith('.md'):
                yield os.path.join(dirpath, fn)


def reclassify_evidence_types(dry_run=False):
    """按 Claim + 论文方法先验重算既有 evidence 页的类型（当前 RULE_VERSION）。

    幂等：已达标（类型/等级/basis/角色全一致）的页面不重写。
    """
    from collections import Counter
    changed = scanned = 0
    before, after = Counter(), Counter()
    methods_idx = _paper_methods_index()
    for path in _iter_evidence_paths():
        try:
            text = io.open(path, encoding='utf-8', errors='replace').read()
        except OSError:
            continue
        scanned += 1
        m = re.search(r'^evidence_type:\s*"?([^"\n]+)"?', text, re.M)
        old = (m.group(1).strip() if m else '') or '未标注'
        before[old] += 1
        cm = re.search(r'^## Claim\s*\n(.+?)(?=\n## |\Z)', text, re.M | re.S)
        claim = re.sub(r'\s+', ' ', cm.group(1)).strip() if cm else ''
        dm = re.search(r'^doi:\s*"?\s*(10\.\d{4,}/[^\s\n"]+)', text, re.M)
        doi = dm.group(1).rstrip('/.') if dm else ''
        methods = methods_idx.get(doi, '')
        etype, quality, prior_type = classify_ex(claim, methods)
        conf = _confidence(etype, claim, methods)
        role, nfkind = claim_role_kind(claim)
        after[etype] += 1
        qm = re.search(r'^quality:\s*"?([^"\n]+)', text, re.M)
        old_quality = qm.group(1).strip() if qm else ''
        bm = re.search(r'^evidence_type_basis:\s*"?([^"\n]+)', text, re.M)
        old_basis = bm.group(1).strip() if bm else ''
        rm = re.search(r'^claim_role:\s*"?([^"\n]+)', text, re.M)
        old_role = rm.group(1).strip() if rm else ''
        pm = re.search(r'^evidence_type_prior:\s*"?([^"\n]*)"?\s*$', text, re.M)
        old_prior = pm.group(1).strip() if pm else None
        new_prior = prior_type or ''
        nm = re.search(r'^non_finding_kind:\s*"?([^"\n]*)', text, re.M)
        # None 表示"字段缺失"，与空串（finding 且无显式结果标记）不是同一状态：
        # 缺字段 -> 需要补写，空串 -> 已经是目标值。用 None 做哨兵，避免
        # 6012 条默认 finding 被永久跳过、字段永远缺席。
        old_nfkind = nm.group(1).strip() if nm else None
        # prior 字段：None=缺字段，''=已确认无需回收。语义等价，
        # 但规则回退时必须清空，否则旧的回收痕迹会一直留在页面上。
        prior_ok = (old_prior == new_prior) or (old_prior is None and new_prior == '')
        if (etype == old and quality == old_quality and old_basis == RULE_VERSION
                and old_role == role and old_nfkind == nfkind and prior_ok):
            continue
        changed += 1
        if dry_run:
            continue
        text = _set_frontmatter_field(text, 'evidence_type', etype)
        text = _set_frontmatter_field(text, 'quality', quality)
        text = _set_frontmatter_field(text, 'quality_basis', RULE_VERSION)
        text = _set_frontmatter_field(text, 'evidence_type_confidence', conf)
        text = _set_frontmatter_field(text, 'evidence_type_basis', RULE_VERSION)
        # rule-v8：保留原判定；回收撤销后清空，避免历史 trace 说谎。
        text = _set_frontmatter_field(text, 'evidence_type_prior', new_prior)
        text = _set_frontmatter_field(text, 'claim_role', role)
        # 细分原因必须落盘：只有 role 三元组时，审计无法区分"教科书背景"与
        # "作者推测"，也无法量化规则改动到底删掉了哪一类句子。
        text = _set_frontmatter_field(text, 'non_finding_kind', nfkind)
        text = _sync_annotation_block(text, etype, quality, role)
        tmp = path + '.tmp'
        io.open(tmp, 'w', encoding='utf-8', newline='\n').write(text)
        os.replace(tmp, path)
    print(json.dumps({'scanned': scanned, 'changed': changed,
                      'dry_run': bool(dry_run), 'rule': RULE_VERSION,
                      'before': dict(before), 'after': dict(after)},
                     ensure_ascii=False, indent=1))
    return changed


THEME_BASIS = 'inherit-source-20261103'


def evidence_themes(paper, finding):
    """证据页主题 = 源论文主题（claim 守卫过滤后，最多 MAX_THEMES_PER_EVIDENCE 个）。

    2026-11-03 修复：旧实现只写 paper['tags'][:4]，tags 为空还兜底成
    'metabolism'（themes.GENERIC_TAGS，永不产生归属）。结果 12291 条证据里
    只有 13.2% 能归到主题，而其中 8398 条的源论文其实已有 themes。
    主题归属必须是论文级的继承 + 声明级守卫，而不是靠 tags 撞运气。
    """
    import themes as th
    raw = paper.get('themes') or []
    canon, seen = [], set()
    for t in th.normalize_tags(raw):
        tid = th.THEME_TAG_ALIASES.get(t)
        if tid and tid not in seen:
            seen.add(tid)
            canon.append(tid)
    ok = th.filter_supported_themes(set(canon), finding)
    return [t for t in canon if t in ok][:th.MAX_THEMES_PER_EVIDENCE]


def _fm_list(items, limit=None, default=None):
    """frontmatter inline 列表的安全序列化。

    2026-11-03 事故：species 直接用 ", ".join 拼进 `species: [...]`，而概念页
    `**物种**:` 行尾混入了整段正文（含 `**方法**:` 与冒号），frontmatter 因此
    变成非法 YAML，整页字段静默丢失（PyYAML: expected ',' or ']'）。
    这里：去控制字符/换行、剔除抓取垃圾（含 **）、逐项加双引号。
    """
    if limit is not None:
        items = list(items)[:limit]
    out = []
    for it in items:
        x = str(it or '')
        x = ''.join(' ' if (ord(c) < 32 or ord(c) == 127) else c for c in x)
        x = ' '.join(x.split()).strip().strip('"')
        if not x or '**' in x:
            continue
        out.append('"%s"' % x.replace('"', ' '))
    if not out and default:
        out = ['"%s"' % default]
    return '[%s]' % ', '.join(out)


def _fm_scalar(value, default=None):
    r"""frontmatter 标量字段的安全序列化（始终带引号）。

    2026-11-03 第 15 轮：上一轮把 primary_species 也改成了 inline 列表
    `primary_species: ["Musa spp."]`，但下游读它是**标量**语义：
      * batch_hypotheses._parse_str_field  → 取到 '["Musa spp."]'
      * batch_synthesis 正则 `^primary_species:\s*"?(.*?)"?$` → 同上
    两个消费者都会带着方括号做事，按物种聚类的假说因此被拆散。
    列表字段用 _fm_list，标量字段一律用本函数，不要混用。
    """
    x = str(value or '')
    x = ''.join(' ' if (ord(c) < 32 or ord(c) == 127) else c for c in x)
    x = ' '.join(x.split()).strip().strip('"')
    if not x:
        x = default or ''
    return '"%s"' % x.replace('"', ' ')


def render_evidence(ev_id, paper, finding, genes, compounds, created, primary):
    evidence_type, quality, prior_type = classify_ex(finding)
    role, nfkind = claim_role_kind(finding)
    prior_fm = ('\nevidence_type_prior: "%s"' % prior_type) if prior_type else ''
    # 兜底改为 'papers'：'metabolism' 是 GENERIC_TAGS，写进去等于没有主题。
    tags_fm = _fm_list(paper['tags'], limit=4, default='papers')
    species_fm = _fm_list(paper['species'], limit=3, default='Plant')
    th_list = evidence_themes(paper, finding)
    themes_fm = _fm_list(th_list)
    genes_fm = _fm_list(genes)
    compounds_fm = _fm_list(compounds)
    # primary_species 是标量字段（下游 _parse_str_field / 正则都按标量读）
    primary_fm = _fm_scalar(primary, default='Plant')
    return f"""---
title: "{short_title(finding)}"
created: {created}
type: evidence
themes: {themes_fm}
theme_status: {'mapped' if th_list else 'unmapped'}
theme_basis: {THEME_BASIS if th_list else 'inherit-claim-guard'}
tags: {tags_fm}
source: "[[{paper['slug']}]]"
doi: "{paper['doi']}"
species: {species_fm}
primary_species: {primary_fm}
evidence_type: "{evidence_type}"{prior_fm}
claim_role: "{role}"
non_finding_kind: "{nfkind}"
quality: "{quality}"
quality_basis: "keyword-heuristic"   # 由关键词推断，非人工评级；用于分诊，不用于结论
evidence_type_basis: "{RULE_VERSION}"
genes: {genes_fm}
compounds: {compounds_fm}
---

# {short_title(finding)}

## Claim
{finding}

## Source
- 文献: [[{paper['slug']}]]
- DOI: {paper['doi'] or '（缺）'}
- 主要物种: {primary}

## 标注信息
- 证据类型: {evidence_type}
- 论断证据完备度: {quality}（指该条论断的文本完备度，**不代表研究质量**）
- 自动标注基因: {', '.join(genes) if genes else '（无）'}
- 自动标注化合物: {', '.join(compounds) if compounds else '（无）'}

> 说明: 基因/化合物/物种均为正则自动标注，可能漏标或误标；引用前请回原文核对。
"""


# ---------------------------------------------------------------------------
# 增量与索引（2026-11-02 追加）
# ---------------------------------------------------------------------------
# 背景：2026-11-02 08:13 的每日任务在 phase6 卡死 900s 被杀。全量重写在 9p/G:
# 挂载上会被杀毒与磁盘抖动放大，且每天重写数千个文件既无必要（脚本本身幂等），
# 也会把 git 工作区搅脏。这里引入"选择集 + 索引缓存"：
#   * 每日运行只重算 mtime 落在窗口内的页面（--changed-only）
#   * 实体页仍按全库索引聚合，所以统计口径与全量运行一致
#   * 索引缺失时自动退回全量，保证冷启动可用

INDEX_VERSION = 1




# ---------------------------------------------------------------------------
# 增量与索引（2026-11-02 追加）
# ---------------------------------------------------------------------------
# 背景：2026-11-02 08:13 的每日任务在 phase6 卡死 900s 被杀。全量重写在 9p/G:
# 挂载上会被杀毒与磁盘抖动放大，且每天重写数千个文件既无必要（脚本本身幂等），
# 也会把 git 工作区搅脏。这里引入"选择集 + 索引缓存"：
#   * 每日运行只重算 mtime 落在窗口内的页面（--changed-only）
#   * 实体页仍按全库索引聚合，所以统计口径与全量运行一致
#   * 索引缺失时自动退回全量，保证冷启动可用

INDEX_VERSION = 1


def _cutoff(days):
    """N=0 表示"今天 0 点以来"；N>=1 表示"最近 N 个 24h"。"""
    if days <= 0:
        lt = time.localtime()
        return time.mktime((lt.tm_year, lt.tm_mon, lt.tm_mday, 0, 0, 0, 0, 0, -1))
    return time.time() - days * 86400


def parse_args():
    ap = argparse.ArgumentParser(
        description='生成 evidence objects 与 entity 页面（默认全量）')
    g = ap.add_mutually_exclusive_group()
    g.add_argument('--full', action='store_true', help='全量重建（默认）')
    g.add_argument('--changed-only', action='store_true',
                   help='只重算 mtime 在 --since-days 天内的概念页')
    ap.add_argument('--since-days', type=int, default=2,
                    help='--changed-only 的时间窗（天），默认 2')
    ap.add_argument('--dois-file',
                    help='只处理该文件中列出的 DOI（每行一个，可带逗号分隔）')
    ap.add_argument('--index', default=os.path.join(BASE, '.pipeline_state',
                                                    'evidence_index.json'),
                    help='索引缓存路径')
    ap.add_argument('--no-index', action='store_true',
                    help='不读写索引缓存，等价于纯全量扫描')
    ap.add_argument('--report-orphans', action='store_true',
                    help='报告不再被任何概念页引用的历史 evidence 对象')
    ap.add_argument('--orphan-list',
                    default=os.path.join(BASE, '_review', 'orphan_evidence.txt'))
    ap.add_argument('--prune-index', action='store_true',
                    help='剔除概念页已不存在的索引条目（防止 active 数虚高）')
    ap.add_argument('--prune-dry-run', action='store_true',
                    help='配合 --prune-index 只报告不修改')
    ap.add_argument('--archive-pruned', action='store_true',
                    help='配合 --prune-index：把牵连的 evidence 文件移到 _review/archive')
    ap.add_argument('--archive-orphans', action='store_true',
                    help='维护模式：归档不在索引中且全库无 wikilink 引用的 evidence')
    ap.add_argument('--orphan-dry-run', action='store_true',
                    help='配合 --archive-orphans 只报告不移动')
    ap.add_argument('--orphan-keep-entity-refs', action='store_true',
                    help='配合 --archive-orphans：连"仅被陈旧实体页引用"的也保留')
    ap.add_argument('--repair-entity-links', action='store_true',
                    help='维护模式：摘除实体页证据表中指向已不存在的 ev 的行')
    ap.add_argument('--repair-dry-run', action='store_true',
                    help='配合 --repair-entity-links 只报告不修改')
    ap.add_argument('--reclassify-types', action='store_true',
                    help='只按 Claim 重算既有 evidence 的 evidence_type（不重扫论文）')
    ap.add_argument('--reclassify-dry-run', action='store_true',
                    help='配合 --reclassify-types 只报告不写盘')
    return ap.parse_args()


def load_index(path):
    if not path or not os.path.exists(path):
        return None
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (OSError, ValueError):
        return None
    if not isinstance(data, dict) or data.get('version') != INDEX_VERSION:
        return None
    if not isinstance(data.get('papers'), dict):
        return None
    return data


def save_index(path, data):
    if not path:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + '.tmp'
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(data, f, ensure_ascii=False, sort_keys=True, indent=0)
        f.write('\n')
    os.replace(tmp, path)


def _read_dois(path):
    out = set()
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                for tok in re.split(r'[,\s]+', line.strip()):
                    tok = tok.strip().lower()
                    if tok.startswith('10.'):
                        out.add(tok.rstrip('.'))
    except OSError:
        pass
    return out


def scan_paper(path):
    """解析单个概念页 -> dict 或 None（无核心发现时）。"""
    try:
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    except OSError:
        return None
    if '### 核心发现' not in content:
        return None

    slug = os.path.basename(path)[:-3]
    title_m = re.search(r'^# (.+)$', content, re.M)
    title = title_m.group(1) if title_m else slug

    species = []
    # 止于下一个 ** 标记：概念页里 `**物种**: ... **方法**: ...` 可能同行
    sm = re.search(r'\*\*物种\*\*:\s*([^\n*]+)', content, re.M)
    if sm:
        species = [s.strip() for s in sm.group(1).split(',') if s.strip()]

    primary = ''
    pm = re.search(r'\*\*主要物种\*\*:\s*(.+?)$', content, re.M)
    if pm:
        primary = pm.group(1).strip()

    tags = []
    tm = re.search(r'tags:\s*\[(.*?)\]', content)
    if tm:
        tags = [t.strip() for t in tm.group(1).split(',')]

    doi = ''
    dm = re.search(r'doi:\s*(10\.\d{4,}/[^\s\n]+)', content, re.I)
    if dm:
        doi = dm.group(1).rstrip('/')

    journal = ''
    jm = re.search(r'^\s*-\s*\*\*期刊\*\*:\s*(.+?)$', content, re.M)
    if jm:
        journal = jm.group(1).strip()

    theme_hits = []
    thm = re.search(r'^themes:\s*\[(.*?)\]', content, re.M)
    if thm:
        theme_hits = [t.strip().strip('"\'') for t in thm.group(1).split(',') if t.strip()]

    findings = extract_findings_from_concept(content)
    if not findings:
        return None
    if not primary:
        primary = primary_species(title=title, abstract=content, fulltext='')
    # 2026-11-04：论文页的领域标注必须被构建层消费。此前 organism_scope 只把
    # scope_status 写进概念页 frontmatter，batch_evidence_objects 从不读取，
    # 导致已判"排除-非植物"的论文照样生成证据页（实测 62 条：副流感病毒、
    # SIRT1 人类综述、食品过敏 ELISA、猪 IMF ATAC-seq、大肠杆菌合成、
    # BRCA1 肿瘤、21 世纪技能教育框架…）。标签只写不消费 = 闸门形同虚设。
    scope_status = ''
    ssm = re.search(r'^scope_status:\s*"?([^\s"]+)', content, re.M)
    if ssm:
        scope_status = ssm.group(1).strip()
    return {'slug': slug, 'title': title, 'species': species, 'primary': primary,
            'tags': tags, 'doi': doi, 'findings': findings, 'path': path,
            'journal': journal, 'abstract': clean_abstract(content),
            'themes': theme_hits, 'scope_status': scope_status}


_SUPERSEDED_DIR = os.path.join(BASE, '_review', 'archive',
                               'superseded_evidence_' + TODAY.replace('-', ''))
_EV_BY_SLUG = None
_EV_SLUG_RE = re.compile(r'^(.*)-f\d+$')
_ARCHIVED_TOTAL = 0


def _evidence_by_slug():
    """一次性建立 slug -> {ev_id} 索引，避免每篇概念页都扫描 7000 个文件。"""
    global _EV_BY_SLUG
    if _EV_BY_SLUG is None:
        idx = defaultdict(set)
        for fn in os.listdir(EVIDENCE_DIR):
            if not fn.endswith('.md'):
                continue
            m = _EV_SLUG_RE.match(fn[:-3])
            if m:
                idx[m.group(1)].add(fn[:-3])
        _EV_BY_SLUG = idx
    return _EV_BY_SLUG


def _unique_dst(directory, name):
    """归档目标重名时加序号，绝不覆盖既有归档文件。"""
    dst = os.path.join(directory, name + '.md')
    n = 1
    while os.path.exists(dst):
        dst = os.path.join(directory, '%s.%d.md' % (name, n))
        n += 1
    return dst


def _read_text(path):
    """一次性读文本并立刻关闭句柄（长跑进程里 open().read() 会泄漏 fd）。"""
    with open(path, encoding='utf-8', errors='ignore') as fh:
        return fh.read()


def archive_superseded(slug, keep_evs):
    """归档该概念页下不再被索引引用的旧 evidence 文件（只移动，不删除）。

    根因（2026-11-02）：write_paper() 只写新 ev 文件，从不清理旧的。重建时
    严格闸门把 8 条发现砍到 4 条，-f5..-f8 便残留磁盘却不进索引，形成孤儿
    证据（1405 条，其中 1341 条页面仍然存在）。
    """
    global _ARCHIVED_TOTAL
    have = _evidence_by_slug().get(slug, set())
    stale = sorted(have - set(keep_evs))
    if not stale:
        return 0
    os.makedirs(_SUPERSEDED_DIR, exist_ok=True)
    moved = 0
    for ev in stale:
        src = os.path.join(EVIDENCE_DIR, ev + '.md')
        try:
            os.replace(src, _unique_dst(_SUPERSEDED_DIR, ev))
        except OSError as e:
            print('  [warn] 归档失败 %s: %s' % (ev, e), flush=True)
            continue
        have.discard(ev)
        moved += 1
    _ARCHIVED_TOTAL += moved
    return moved


def _classify_referrers(base, want):
    """返回 {ev_id: set(引用它的目录名)}；ROOT 表示知识库根目录的 md。"""
    dirs = ['evidence', 'relationships', 'entities', 'hypotheses', 'synthesis',
            'research-programs', 'concepts']
    rx = re.compile(r'\[\[([^\]|#]+)')
    out = defaultdict(set)
    for d in dirs:
        root = os.path.join(base, d)
        if not os.path.isdir(root):
            continue
        for dp, dn, fn in os.walk(root):
            dn[:] = [x for x in dn if not x.startswith('.')]
            for name in fn:
                if not name.endswith('.md'):
                    continue
                try:
                    body = _read_text(os.path.join(dp, name))
                except OSError:
                    continue
                for s in rx.findall(body):
                    s = s.strip()
                    if s in want:
                        out[s].add(d)
    try:
        names = os.listdir(base)
    except OSError:
        names = []
    for name in names:
        if not name.endswith('.md'):
            continue
        try:
            body = _read_text(os.path.join(base, name))
        except OSError:
            continue
        for s in rx.findall(body):
            s = s.strip()
            if s in want:
                out[s].add('ROOT')
    return out


def archive_orphans(index_papers, dry_run=False, include_entity_only=True):
    """维护模式：归档孤儿 evidence。

    分级（2026-11-02）：孤儿里只有一部分是"没人要"的。
      * 无任何 wikilink 引用              -> 直接归档
      * 只被 entities/ 引用                -> 陈旧实体页（可由索引重建）-> 归档
      * 被 synthesis/relationships/concepts 引用 -> 真实引用，保留
    归档后必须 rebuild_entities()，否则 entity 页会留下断链。
    """
    expected = set()
    for slug in index_papers:
        for ent in index_papers[slug].get('entities', []):
            expected.add(ent['ev'])
    actual = sorted(f[:-3] for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md'))
    orphans = [e for e in actual if e not in expected]
    refdirs = _classify_referrers(BASE, set(orphans))

    movable, entity_only, protected = [], [], []
    for ev in orphans:
        ds = refdirs.get(ev, set())
        if not ds:
            movable.append(ev)
        elif ds == {'entities'} and include_entity_only:
            entity_only.append(ev)
        else:
            protected.append((ev, sorted(ds)))
    movable_all = movable + entity_only
    print('孤儿证据: %d（活跃 %d / 磁盘 %d）'
          % (len(orphans), len(expected), len(actual)))
    print('  无引用            : %d' % len(movable))
    print('  仅陈旧实体页引用  : %d%s'
          % (len(entity_only), '' if include_entity_only else '（本次保留）'))
    print('  真实引用需保留    : %d' % len(protected))
    if dry_run:
        for e in movable_all[:20]:
            print('  [dry-run] -', e)
        for e, ds in protected[:10]:
            print('  [keep] %s <- %s' % (e, '+'.join(ds)))
        return len(movable_all), len(protected)
    os.makedirs(_SUPERSEDED_DIR, exist_ok=True)
    moved = 0
    for ev in movable_all:
        try:
            os.replace(os.path.join(EVIDENCE_DIR, ev + '.md'),
                       _unique_dst(_SUPERSEDED_DIR, ev))
            moved += 1
        except OSError as e:
            print('  [warn] 归档失败 %s: %s' % (ev, e), flush=True)
    print('  已归档 %d -> %s' % (moved, _SUPERSEDED_DIR), flush=True)
    return moved, len(protected)


_EV_LINK_ROW = re.compile(r'^\|\s*\[\[([^\]|#]+)\]\]')
_TOTAL_EV = re.compile(r'(\*\*Total evidence objects\*\*:\s*)(\d+)')


def repair_entity_links(dry_run=False):
    """摘掉实体页证据表里指向"已不在磁盘"的 ev 行，并同步总数。

    2026-11-02：实体页只重建 top-30 基因 / top-15 化合物，其余 135 页是旧
    构建器遗留。证据归档后这些页面会留下断链，必须做一次表格级修复
    （只删表格行，不重写页面正文，保留人工编辑内容）。
    """
    have = {f[:-3] for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md')}
    changed = dropped = 0
    for dp, dn, fn in os.walk(ENTITIES_DIR):
        dn[:] = [x for x in dn if not x.startswith('.')]
        for name in sorted(fn):
            if not name.endswith('.md'):
                continue
            path = os.path.join(dp, name)
            try:
                body = _read_text(path)
            except OSError:
                continue
            lines = body.split('\n')
            out, local = [], 0
            for ln in lines:
                m = _EV_LINK_ROW.match(ln)
                if m and m.group(1).strip() not in have:
                    local += 1
                    continue
                out.append(ln)
            if not local:
                continue
            new = '\n'.join(out)
            n_ev = sum(1 for ln in out if _EV_LINK_ROW.match(ln))
            new = _TOTAL_EV.sub(lambda mm: mm.group(1) + str(n_ev), new, count=1)
            if dry_run:
                print('  [dry-run] %s: 摘除 %d 行' % (name, local))
                changed += 1
                dropped += local
                continue
            if write_if_changed(path, new):
                changed += 1
                dropped += local
    print('实体页失效链接修复: %d 文件 / %d 行' % (changed, dropped), flush=True)
    return changed, dropped


def _article_kind_of(path):
    """读取概念页的 article_kind（缺省 research）。"""
    try:
        from article_kind import audit_page
        return audit_page(path)[0]
    except Exception:
        return 'research'


def _non_evidence_kind(path):
    """True 表示该页不是可用于推理的研究证据（但页面保留）。"""
    return _article_kind_of(path) not in ('research', 'review')


def write_paper(paper, index_papers):
    """写一个概念页派生的全部 evidence 对象，并记录到索引。"""
    written = unchanged = 0
    ents = []
    for idx, finding in enumerate(paper['findings']):
        ev_id = generate_evidence_id(paper['slug'], idx)
        genes, compounds = extract_gene_compounds(finding)
        ev_path = os.path.join(EVIDENCE_DIR, ev_id + '.md')
        created = read_created(ev_path) or TODAY
        content = render_evidence(ev_id, paper, finding, genes, compounds,
                                  created, paper['primary'])
        if write_if_changed(ev_path, content):
            written += 1
        else:
            unchanged += 1
        ents.append({'ev': ev_id, 'title': short_title(finding, 100),
                     'genes': genes, 'compounds': compounds})
    index_papers[paper['slug']] = {'doi': paper['doi'], 'primary': paper['primary'],
                                   'title': paper['title'], 'entities': ents}
    # 只写新文件不清旧文件会累积孤儿证据，这里补上归档
    archive_superseded(paper['slug'], [e['ev'] for e in ents])
    return written, unchanged


def rebuild_entities(index_papers):
    gene_map = defaultdict(list)
    comp_map = defaultdict(list)
    for slug in sorted(index_papers):
        for ent in index_papers[slug]['entities']:
            for g in ent['genes']:
                gene_map[g].append((ent['ev'], ent['title']))
            for c in ent['compounds']:
                comp_map[c].append((ent['ev'], ent['title']))

    entity_written = 0
    gene_counter = Counter({k: len(v) for k, v in gene_map.items()})
    top_genes = [g for g, c in sorted(gene_counter.items(),
                                      key=lambda kv: (-kv[1], kv[0])) if c >= 2][:30]
    for gene in top_genes:
        ev_list = gene_map[gene]
        gene_path = os.path.join(ENTITIES_DIR, gene.lower().replace(' ', '-') + '.md')
        created = read_created(gene_path) or TODAY
        ev_rows = '\n'.join('| [[%s]] | %s |' % (ev_id, snippet[:80])
                            for ev_id, snippet in ev_list[:10])
        gene_content = f"""---
title: "{gene}"
created: {created}
type: entity
entity_type: gene
tags: [metabolism, gene]
---

# {gene}

## Evidence Summary
**Total evidence objects**: {len(ev_list)}

## Evidence Table
| Evidence | Finding |
|----------|---------|
{ev_rows}

## Functional Roles
_（待从证据深入提炼）_

## Regulatory Network
_（见 relationships/）_
"""
        if write_if_changed(gene_path, gene_content):
            entity_written += 1

    comp_counter = Counter({k: len(v) for k, v in comp_map.items()})
    top_comps = [c for c, n in sorted(comp_counter.items(),
                                      key=lambda kv: (-kv[1], kv[0])) if n >= 3][:15]
    for compound in top_comps:
        ev_list = comp_map[compound]
        comp_path = os.path.join(ENTITIES_DIR, slugify(compound) + '.md')
        created = read_created(comp_path) or TODAY
        ev_rows = '\n'.join('| [[%s]] | %s |' % (ev_id, snippet[:80])
                            for ev_id, snippet in ev_list[:10])
        comp_content = f"""---
title: "{compound}"
created: {created}
type: entity
entity_type: compound
tags: [metabolism, compound]
---

# {compound}

## Evidence Summary
**Total evidence objects**: {len(ev_list)}

## Evidence Table
| Evidence | Finding |
|----------|---------|
{ev_rows}

## Biosynthetic Pathway
-

## Regulatory Genes
-
"""
        if write_if_changed(comp_path, comp_content):
            entity_written += 1

    return entity_written, len(top_genes), len(top_comps)


def prune_index(index_papers, archive_dir=None, dry_run=False):
    """剔除"概念页已不存在"的索引条目（页面被隔离/删除后索引会残留）。

    2026-11-02：索引里有 75 篇概念页已不存在，却仍挂着 476 条 ev_id，导致
    index.md 的 active 数虚高（7082 vs 磁盘 6871）。孤儿指标因此失真。

    只从**索引**移除并报告；磁盘上的 evidence 文件默认原样保留（可能有
    synthesis 引用），除非显式给 --archive-pruned 才移动到 _review/archive。
    """
    on_disk = {f[:-3] for f in os.listdir(CONCEPTS_DIR) if f.endswith('.md')}
    gone = sorted(slug for slug in index_papers if slug not in on_disk)
    removed_ev = [ent['ev'] for slug in gone
                  for ent in index_papers[slug].get('entities', [])]

    # 2026-11-02：第二类残留 —— 概念页还在，但它引用的 evidence 文件已被
    # repair_nonplant_import / 孤儿归档移走。这些 ev_id 若留在索引里，
    # index.md 的 active 数会永远大于磁盘（实测 5879 vs 5752，差 127），
    # 使"孤儿=0"这类指标失去意义。这里按 ev_id 反向清理。
    ev_on_disk = {f[:-3] for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md')}
    stale_pairs = []   # (slug, ev_id)
    for slug, rec in index_papers.items():
        if slug in gone:
            continue
        kept = []
        for ent in rec.get('entities', []):
            if ent.get('ev') and ent['ev'] not in ev_on_disk:
                stale_pairs.append((slug, ent['ev']))
            else:
                kept.append(ent)
        if len(kept) != len(rec.get('entities', [])):
            rec['entities'] = kept
    stale_ev = [e for _, e in stale_pairs]
    print('索引剪枝: %d 篇概念页已不存在（牵连 %d 条 ev_id）；'
          '%d 个 ev_id 的 evidence 文件已不在磁盘（牵连 %d 篇概念页）'
          % (len(gone), len(removed_ev), len(stale_ev), len({s for s, _ in stale_pairs})),
          flush=True)
    if dry_run:
        for slug in gone[:20]:
            print('  [dry-run] -', slug)
        for slug, ev in stale_pairs[:20]:
            print('  [dry-run] stale-ev', ev, '<-', slug)
        return gone, removed_ev + stale_ev
    for slug in gone:
        index_papers.pop(slug, None)
    if archive_dir and removed_ev:
        os.makedirs(archive_dir, exist_ok=True)
        moved = 0
        for ev in removed_ev:
            src = os.path.join(EVIDENCE_DIR, ev + '.md')
            if os.path.exists(src):
                os.replace(src, os.path.join(archive_dir, ev + '.md'))
                moved += 1
        print('  归档 evidence 文件: %d -> %s' % (moved, archive_dir), flush=True)
    return gone, removed_ev


def report_orphans(index_papers, out_path):
    expected = set()
    for slug in index_papers:
        for ent in index_papers[slug]['entities']:
            expected.add(ent['ev'])
    actual = sorted(f[:-3] for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md'))
    orphans = [e for e in actual if e not in expected]
    try:
        from purity_scan import collect_references
        refs = collect_references(BASE)
    except Exception:
        refs = {}
    true_orphans = [e for e in orphans if e not in refs]
    shadowed = [e for e in orphans if e in refs]
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8', newline='\n') as f:
        f.write('# 未被任何概念页引用的 evidence 对象\n\n')
        f.write('生成于 %s；共 %d 条（活跃 %d / 全库 %d）。\n'
                '其中**真孤儿 %d 条**（全库无任何 [[wikilink]] 指向，可安全归档），'
                '%d 条仍被 synthesis/relationships/entities 引用（保留原地）。\n'
                '这些对象来自旧命名方案或已被改写/删除的页面。默认不删除，'
                '仅供归档决策。\n\n' % (TODAY, len(orphans), len(expected), len(actual),
                                       len(true_orphans), len(shadowed)))
        f.write('## 真孤儿（可归档）\n\n')
        for e in true_orphans:
            f.write('- %s\n' % e)
        f.write('\n## 概念页未引但其他层仍引用（保留）\n\n')
        for e in shadowed:
            f.write('- %s\n' % e)
    return len(true_orphans), len(expected), len(actual)


def main():
    args = parse_args()
    if args.reclassify_types:
        reclassify_evidence_types(dry_run=args.reclassify_dry_run)
        return
    index = None if args.no_index else load_index(args.index)

    if (args.repair_entity_links
            and not (args.full or args.changed_only or args.dois_file)):
        repair_entity_links(dry_run=args.repair_dry_run)
        return

    # 维护模式：--archive-orphans 只清理磁盘，不重建任何页面。
    if (args.archive_orphans and index is not None
            and not (args.full or args.changed_only or args.dois_file)):
        moved, kept = archive_orphans(
            index['papers'], dry_run=args.orphan_dry_run,
            include_entity_only=not args.orphan_keep_entity_refs)
        if not args.orphan_dry_run:
            # 归档后实体页里会残留指向已归档 ev 的 wikilink，必须重建
            ew, ng, nc = rebuild_entities(index['papers'])
            print('Entity pages rewritten: %d (genes %d / compounds %d)'
                  % (ew, ng, nc), flush=True)
            repair_entity_links()
            save_index(args.index, {'version': INDEX_VERSION, 'generated': TODAY,
                                    'papers': index['papers']})
        return

    # 纯维护模式：--prune-index 且未要求重建时，只动索引、不动证据层后立即返回。
    # （此前 --prune-dry-run 会继续走全量重建并写盘，等于预演变真跑。）
    if (args.prune_index and index is not None
            and not (args.full or args.changed_only or args.dois_file)):
        archive = (os.path.join(BASE, '_review', 'archive',
                                'pruned_evidence_' + TODAY.replace('-', ''))
                   if args.archive_pruned else None)
        # 必须传引用：传 dict(...) 副本会让剪枝结果写不回索引（本轮实测踩到）
        prune_index(index['papers'], archive_dir=archive,
                    dry_run=args.prune_dry_run)
        if not args.prune_dry_run:
            save_index(args.index, {'version': INDEX_VERSION, 'generated': TODAY,
                                    'papers': index['papers']})
            if args.report_orphans:
                n, act, tot = report_orphans(index['papers'], args.orphan_list)
                print('Orphan evidence objects: %d (active %d / on disk %d) -> %s'
                      % (n, act, tot, args.orphan_list))
        return
    if args.report_orphans and index is not None and not (
            args.full or args.no_index or args.dois_file or args.changed_only):
        # 只出孤儿清单时不必重扫全库，直接用索引
        n, act, tot = report_orphans(index['papers'], args.orphan_list)
        print('Orphan evidence objects: %d (active %d / on disk %d) -> %s'
              % (n, act, tot, args.orphan_list))
        return
    full = (args.full or args.no_index or args.dois_file is not None
            or not args.changed_only or index is None)
    if args.changed_only and index is None and not args.no_index:
        print('[warn] 索引缺失或版本不符，本次退回全量扫描', flush=True)

    index_papers = dict(index['papers']) if index else {}

    if args.prune_index and index_papers:
        archive = (os.path.join(BASE, '_review', 'archive',
                                'pruned_evidence_' + TODAY.replace('-', ''))
                   if args.archive_pruned else None)
        prune_index(index_papers, archive_dir=archive, dry_run=args.prune_dry_run)

    all_pages = [os.path.join(CONCEPTS_DIR, f)
                 for f in sorted(os.listdir(CONCEPTS_DIR)) if f.endswith('.md')]

    if full:
        targets = all_pages
        if args.dois_file:
            wanted = _read_dois(args.dois_file)
            keep = []
            for p in all_pages:
                try:
                    head = open(p, 'r', encoding='utf-8', errors='replace').read(4000)
                except OSError:
                    continue
                m = re.search(r'doi:\s*"?\s*(10\.\d{4,}/[^\s"\n]+)', head, re.I)
                if m and m.group(1).lower().rstrip('.') in wanted:
                    keep.append(p)
            targets = keep
    else:
        cutoff = _cutoff(args.since_days)
        targets = []
        for p in all_pages:
            try:
                if os.stat(p).st_mtime >= cutoff:
                    targets.append(p)
            except OSError:
                continue

    print('模式: %s | 候选概念页 %d | 待处理 %d'
          % ('全量' if full else '增量(最近 %d 天)' % args.since_days,
             len(all_pages), len(targets)), flush=True)

    written = unchanged = processed = 0
    rejected = []      # (slug, doi, action, reasons)
    for path in targets:
        paper = scan_paper(path)
        if not paper:
            continue
        # 文献类型闸门（2026-11-03）：更正/撤稿/社论/勘误/目录页/会员表
        # 不是研究证据。页面本体保留（frontmatter 已写 article_kind），
        # 但不再为它生成 evidence 对象；既有 evidence 移入 _review/archive（不删除）。
        # 之前只在消费端过滤，证据池里仍有 186 条来自非研究页面。
        if _non_evidence_kind(path):
            rejected.append((paper['slug'], paper['doi'], 'drop-nonarticle',
                             _article_kind_of(path)))
            if paper['slug'] in index_papers:
                archive_superseded(paper['slug'], [])
                del index_papers[paper['slug']]
            continue
        # 领域标注闸门（2026-11-04）：概念页已被审计判为"排除-非植物"时，
        # 不再生成证据对象。标注由 organism_scope 写入（193 篇），此前构建层
        # 从不读取，闸门只在下载层生效。方法可迁移的仍保留（只进 methods-tools）。
        if (paper.get('scope_status') or '') == 'excluded-nonplant':
            _m = is_method_paper(
                (paper['title'] or '') + ' ' + (paper.get('abstract') or ''),
                paper.get('themes') or (), paper.get('tags') or (),
                paper['title'] or '')
            if not _m:
                rejected.append((paper['slug'], paper['doi'],
                                 'drop-scope-status', 'scope_status=excluded-nonplant'))
                if paper['slug'] in index_papers:
                    archive_superseded(paper['slug'], [])
                    del index_papers[paper['slug']]
                continue
            rejected.append((paper['slug'], paper['doi'], 'keep-methods',
                             'scope_status=excluded-nonplant;method-transferable'))
        action, reasons = import_decision(
            paper['title'], paper.get('abstract') or '', paper.get('journal') or '',
            paper.get('species') or (), paper.get('themes') or (), paper.get('tags') or ())
        if action == 'drop':
            # 研究对象是人/动物（或临床终点），植物只是药物/材料来源：
            # 不生成任何证据对象，并落盘审计清单（可复核、可回滚）。
            # 2026-11-04：此前只跳过写入，不清既有证据页 —— 已导入的非植物
            # 文献证据永久留在池子里（"闸门只在入口、存量不回收"）。现与
            # 非研究页分支一致：既有证据归档到 _review/archive，索引同步剔除。
            rejected.append((paper['slug'], paper['doi'], action, ';'.join(reasons)))
            if paper['slug'] in index_papers:
                archive_superseded(paper['slug'], [])
                del index_papers[paper['slug']]
            continue
        if action == 'keep-methods':
            # 通用方法学论文：证据保留（methods-tools 主题需要），
            # 但主题层与综述层都会把它限制在 methods-tools 内。
            rejected.append((paper['slug'], paper['doi'], action, ';'.join(reasons)))
        w, u = write_paper(paper, index_papers)
        written += w
        unchanged += u
        processed += 1

    total_findings = sum(len(index_papers[s]['entities']) for s in index_papers)
    print('Papers with findings: %d (本次扫描 %d)' % (len(index_papers), processed))
    print('Total findings: %d' % total_findings)
    print('Evidence objects written: %d (unchanged: %d)' % (written, unchanged))

    if rejected:
        rej_path = os.path.join(BASE, '_review', 'nonplant_rejected_%s.tsv'
                                % TODAY.replace('-', ''))
        try:
            os.makedirs(os.path.dirname(rej_path), exist_ok=True)
            with open(rej_path, 'w', encoding='utf-8') as fh:
                fh.write('slug\tdoi\taction\treasons\n')
                for row in rejected:
                    fh.write('\t'.join(x or '' for x in row) + '\n')
            print('Nonplant gate: drop=%d keep-methods=%d -> %s'
                  % (sum(1 for r in rejected if r[2].startswith('drop')),
                     sum(1 for r in rejected if r[2] == 'keep-methods'), rej_path))
        except OSError as exc:
            print('WARN: 拒收清单写入失败: %s' % exc)

    entity_written, ng, nc = rebuild_entities(index_papers)
    print('Entity pages written: %d (genes: %d, compounds: %d)'
          % (entity_written, ng, nc))

    if not args.no_index:
        save_index(args.index, {'version': INDEX_VERSION, 'generated': TODAY,
                                'papers': index_papers})

    ev_count = len([f for f in os.listdir(EVIDENCE_DIR) if f.endswith('.md')])
    active_count = sum(len(index_papers[s]['entities']) for s in index_papers)
    idx_path = os.path.join(BASE, 'index.md')
    if os.path.exists(idx_path):
        with open(idx_path, 'r', encoding='utf-8') as f:
            idx_content = f.read()
        # 页面上"总数"应指活跃对象；孤儿另计，避免把死文件算成知识量
        label = ('Evidence Objects — %d active' % active_count
                 if active_count == ev_count
                 else 'Evidence Objects — %d active (%d files on disk)'
                      % (active_count, ev_count))
        new_idx = re.sub(r'Evidence Objects.*?\n', label + '\n', idx_content)
        write_if_changed(idx_path, new_idx)

    if args.report_orphans:
        n, act, tot = report_orphans(index_papers, args.orphan_list)
        print('Orphan evidence objects: %d (active %d / on disk %d) -> %s'
              % (n, act, tot, args.orphan_list))

    if _ARCHIVED_TOTAL:
        print('Superseded evidence archived: %d -> %s'
              % (_ARCHIVED_TOTAL, _SUPERSEDED_DIR))

    print('\n=== PHASE 6 COMPLETE ===')
    print('Evidence objects: %d' % ev_count)
    print('Top genes: %d  Top compounds: %d' % (ng, nc))


if __name__ == '__main__':
    main()
