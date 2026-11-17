#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""主题词表 = 知识库唯一的"主题↔证据标签"契约（2026-11-02）。

为什么需要它
------------
本轮体检发现，报告层的三个脚本各自用一套隐式规则把证据归到主题，结果互不一致：

  * 证据页真实标签是  single-cell-spatial(253) / developmental-biology(253) /
    metabolism-np(162) / stress-immunity(110) / epigenetics-gr(109) /
    hormone-signaling(108) / genomics-evolution(83) / methods-tools(75)；
  * 但 synthesis 页 frontmatter 写的是  tags: [hormone, signaling, synthesis]，
    与证据标签零交集；
  * batch_hypotheses 因此只匹配到 9 条证据（应是 250+），
    于是"单细胞与空间组学"的假说页从 9 条证据里硬凑 5 条假说。

同一批证据在不同脚本里得出不同数字，任何"综述/假说"都不可能可信。
本模块把主题定义收敛到一处：别名归一化 + 主标签匹配 + 关键词兜底，
并显式区分"高置信（标签）"与"低置信（关键词）"两档，写进产物供人工复核。

设计约束
--------
1. 纯函数、无 IO、无第三方依赖 —— 可被三个脚本和测试同时导入。
2. 不引入新的隐式规则：别名表就是全部规则，改这里即改全局。
3. 通用大桶标签（papers / metabolism / development）**不进主标签**：
   papers 是"全部文献"的同义词，metabolism/development 覆盖上千页，
   把它们当主标签会让主题退化成"整个库"。
"""
from __future__ import annotations

import re

# ── 8 个固定主题（与 synthesis/*.md 文件名一致，禁止随意增删）───────────
THEMES = (
    'single-cell-spatial-omics',
    'developmental-biology',
    'metabolism-natural-products',
    'hormone-signaling',
    'stress-immunity',
    'epigenetics-gene-regulation',
    'methods-tools',
    'genomics-evolution',
)

# ── 主题元数据（标题只用于展示，不参与匹配）───────────────────────────
THEME_META = {
    'single-cell-spatial-omics': {
        'title': 'Single-Cell & Spatial Omics',
        'title_zh': '单细胞与空间组学',
    },
    'developmental-biology': {
        'title': 'Plant Developmental Biology',
        'title_zh': '植物发育生物学',
    },
    'metabolism-natural-products': {
        'title': 'Metabolism & Natural Products',
        'title_zh': '代谢与天然产物',
    },
    'hormone-signaling': {
        'title': 'Hormone Signalling',
        'title_zh': '激素与信号转导',
    },
    'stress-immunity': {
        'title': 'Stress & Immunity',
        'title_zh': '逆境与免疫',
    },
    'epigenetics-gene-regulation': {
        'title': 'Epigenetics & Gene Regulation',
        'title_zh': '表观遗传与基因调控',
    },
    'methods-tools': {
        'title': 'Methods & Tools',
        'title_zh': '方法与工具',
    },
    'genomics-evolution': {
        'title': 'Genomics & Evolution',
        'title_zh': '基因组学与演化',
    },
}

# ── 别名表：标签写法归一化 → 主题 ─────────────────────────────────────
# 线上历史标签存在 `#metabolism-np`、`metabolism-np` 两种写法（105 + 162 条），
# 缩写 `epigenetics-gr` / `single-cell-spatial` 也在用，这里全部收敛。
THEME_TAG_ALIASES = {
    # 单细胞 / 空间
    'single-cell-spatial': 'single-cell-spatial-omics',
    'single-cell-spatial-omics': 'single-cell-spatial-omics',
    'single-cell': 'single-cell-spatial-omics',
    'singlecell': 'single-cell-spatial-omics',
    'spatial': 'single-cell-spatial-omics',
    'spatial-transcriptomics': 'single-cell-spatial-omics',
    'scrnaseq': 'single-cell-spatial-omics',
    'scrna-seq': 'single-cell-spatial-omics',
    'stereo-seq': 'single-cell-spatial-omics',
    # 发育
    'developmental-biology': 'developmental-biology',
    'regeneration': 'developmental-biology',
    'meristem': 'developmental-biology',
    'organogenesis': 'developmental-biology',
    'embryogenesis': 'developmental-biology',
    'somatic-embryogenesis': 'developmental-biology',
    # 2026-11-02：development/cambium 在全库均 0 页使用，加进来只为与
    # tests 夹具和旧 CORE_THEMES 的语义对齐，不改变线上归属数量。
    # vascular/xylem/phloem 刻意不加：它们会让 developmental-biology 的
    # 证据量从 272 涨到 848（含大量次生壁合成类），属超范围重分类。
    'development': 'developmental-biology',
    'cambium': 'developmental-biology',
    # 代谢
    'metabolism-np': 'metabolism-natural-products',
    'metabolism-natural-products': 'metabolism-natural-products',
    'secondary-metabolism': 'metabolism-natural-products',
    'flavonoid': 'metabolism-natural-products',
    'terpenoid': 'metabolism-natural-products',
    'alkaloid': 'metabolism-natural-products',
    'phenylpropanoid': 'metabolism-natural-products',
    'starch-sugar': 'metabolism-natural-products',
    # 激素
    'hormone-signaling': 'hormone-signaling',
    'hormone': 'hormone-signaling',
    'signaling': 'hormone-signaling',
    'auxin': 'hormone-signaling',
    'cytokinin': 'hormone-signaling',
    'gibberellin': 'hormone-signaling',
    'brassinosteroid': 'hormone-signaling',
    'abscisic': 'hormone-signaling',
    'jasmonic': 'hormone-signaling',
    'salicylic': 'hormone-signaling',
    'ethylene': 'hormone-signaling',
    'strigolactone': 'hormone-signaling',
    # 逆境 / 免疫
    'stress-immunity': 'stress-immunity',
    'stress': 'stress-immunity',
    'immunity': 'stress-immunity',
    'defense': 'stress-immunity',
    'pathogen': 'stress-immunity',
    'drought': 'stress-immunity',
    'salt': 'stress-immunity',
    'heat': 'stress-immunity',
    'cold': 'stress-immunity',
    # 表观
    'epigenetics-gr': 'epigenetics-gene-regulation',
    'epigenetics-gene-regulation': 'epigenetics-gene-regulation',
    'epigenetics': 'epigenetics-gene-regulation',
    'epigenetic': 'epigenetics-gene-regulation',
    'chromatin': 'epigenetics-gene-regulation',
    'transcription-factor': 'epigenetics-gene-regulation',
    'gene-regulation': 'epigenetics-gene-regulation',
    'atac': 'epigenetics-gene-regulation',
    # 方法
    'methods-tools': 'methods-tools',
    'method': 'methods-tools',
    'methodological': 'methods-tools',
    'tool': 'methods-tools',
    'database': 'methods-tools',
    'pipeline': 'methods-tools',
    'benchmark': 'methods-tools',
    'protocol': 'methods-tools',
    # 基因组 / 演化
    'genomics-evolution': 'genomics-evolution',
    'genomics': 'genomics-evolution',
    'evolution': 'genomics-evolution',
    'genome': 'genomics-evolution',
    'polyploidy': 'genomics-evolution',
    'comparative': 'genomics-evolution',
}

# ── 主标签匹配时排除的"大桶"标签 ─────────────────────────────────────
# 只排除"等于全部文献"的标签：papers 3850 页、metabolism 2956 页，
# 覆盖整个库的 40%+，拿它当主题依据等于没有依据。
#
# 2026-11-02 修正：曾把 'development' 也列进来，但全库实际 0 页使用该标签，
# 排掉它没有降噪作用，反而让 tests 里 [development, cambium] 这类
# 合法发育标签无法归属主题。现在 'development'/'cambium' 作为正式别名。
GENERIC_TAGS = frozenset({
    'papers', 'paper', 'reference', 'dpdf', 'pmc', 'synthesis',
    'metabolism',
})

# ── 关键词兜底（只在标签缺失时使用）──────────────────────────────
# 两级词表（2026-11-03 分级）：
#   HI = 领域专有词，单个命中即足以判定主题；
#   LO = 泛化词（自然界/化学/统计里随处可见），必须 >=2 个不同词命中。
# 旧规则"任意 2 个关键词"把 4469/5722 条证据判成无主题（77.7%）；
# 无条件放宽到"单个命中"又会把 'salt'、'ethylene'、'differentiation'
# 这类歧义词判错。分级是唯一兼顾召回与精度的做法。
THEME_KEYWORDS_HI = {
    'single-cell-spatial-omics': [
        'single-cell', 'single cell', 'scrna-seq', 'scrna', 'snrna-seq',
        'spatial transcript', 'stereo-seq', 'merfish', 'visium', 'slide-seq',
        'cell atlas', 'pseudotime', 'cell-type', 'cell type', 'spatial omics',
    ],
    'developmental-biology': [
        'meristem', 'organogenesis', 'embryogenesis', 'somatic embryogenesis',
        'stem cell niche', 'primordium', 'morphogenesis', 'regeneration',
        'floral meristem', 'root apical meristem', 'shoot apical meristem',
        'leaf development', 'root development',
        # 2026-11-03 第 16 轮：生殖发育词汇缺口。
        # 事故：'PELOTA ... tomato fertility and viral resistance'
        # （New Phytologist, 10.1111/nph.71715）被判 out-of-scope，摘要里有
        # floral defects / male and female fertility / complete sterility。
        # 只收带限定的复合词：裸 'fertility' 会命中「soil fertility」这类
        # 农艺论文（实测 1 例误判），故不收。
        'gametophyte', 'sporogenesis', 'floral organ', 'flower development',
        'pollen development', 'seed development', 'embryo development',
        'male sterility', 'male fertility', 'female fertility',
        'fertility restoration',
        # 2026-11-03 第 17 轮：清掉"沿用旧 themes"兜底后暴露的词表缺口。
        # 依据是被降级页面里摘要完整（>=500 字符）的那 229 篇人工抽样：
        # ovule 发育、叶片衰老、成花转变、气孔分布、自交不亲和、嫁接等
        # 明确属于发育主题，却一个词都不在表里。
        'ovule', 'anther', 'pollen', 'endosperm', 'embryo sac',
        'grain size', 'grain weight', 'seed size', 'flowering time',
        'floral transition', 'photoperiod', 'stomata', 'stomatal development',
        'self-incompatibility', 'trichome', 'root hair', 'tiller', 'panicle',
        'cytoplasmic male sterility', 'heading date', 'cms line',
        'leaf senescence', 'xylem', 'phloem', 'vascular tissue', 'graft',
    ],
    'metabolism-natural-products': [
        'biosynthesis', 'secondary metabolite', 'secondary metabolism',
        'flavonoid', 'anthocyanin', 'terpenoid', 'alkaloid', 'lignin',
        'phenylpropanoid', 'glycoside', 'triterpene', 'sesquiterpene',
        'monoterpene', 'carotenoid', 'glucosinolate', 'natural product',
        # 2026-11-03 第 17 轮：代谢组 / 初生代谢词汇缺口。
        # 注意：'starch'/'sugar'/'lipid'/'wax'/'fatty acid' 曾一并加入，
        # 实测把"亚热带人工林土壤磷库分层""以 Phaeodactylum 替代豆粕饲喂"
        # 这类土壤/饲料论文拉进代谢主题——这类词在非植物语境同样高频。
        # 只保留植物次生代谢与角质层特异的词。
        'metabolom', 'phenolic', 'flavonol', 'cutin', 'suberin',
    ],
    'hormone-signaling': [
        'auxin', 'cytokinin', 'gibberellin', 'brassinosteroid',
        'abscisic acid', 'jasmon', 'salicylic acid', 'strigolactone',
        'ethylene signaling', 'ethylene response', 'hormone signaling',
        'hormone signalling', 'signal transduction',
    ],
    'stress-immunity': [
        'drought stress', 'salt stress', 'cold stress', 'heat stress',
        'pathogen', 'defense response', 'immune', 'nlr', 'effector',
        'ros burst', 'pattern-triggered immunity',
        'effector-triggered immunity', 'hypersensitive response',
        'systemic acquired resistance',
        # 2026-11-03 第 16 轮：病毒学词汇缺口。
        # 同一篇 PELOTA 论文摘要写满 TYLCV / near-immunity / viral resistance，
        # 一个词都不在表里 —— 注意 'immune' 不是 'immunity' 的子串。
        # 这组词歧义低，只补漏，不改口径。
        'virus', 'viral', 'antiviral', 'immunity', 'tylcv', 'geminivirus',
        'potyvirus', 'tospovirus', 'begomovirus', 'nbs-lrr', 'rna silencing',
        'disease resistance', 'pathogen resistance',
        # 2026-11-03 第 17 轮：重金属/非生物胁迫词汇缺口（同一次抽样）
        'abiotic stress', 'cadmium', 'heavy metal', 'drought', 'salinity',
        'salt tolerance', 'drought tolerance', 'heat tolerance',
        'cold tolerance', 'osmotic stress', 'water deficit',
    ],
    'epigenetics-gene-regulation': [
        'chromatin', 'histone modification', 'h3k27me3', 'h3k4me3',
        'polycomb', 'enhancer', 'atac-seq', 'chip-seq', 'regulatory element',
        'dna methylation', 'transcription factor', 'small rna',
        # 2026-11-03 第 17 轮：昼夜节律属于转录调控层
        'circadian', 'epigenome', 'epigenomic', 'cut&tag', 'cut-and-tag',
        'chip-atlas', 'multiome',
    ],
    'methods-tools': [
        'we present', 'we developed', 'we describe a', 'pipeline', 'workflow',
        'benchmark', 'database', 'toolkit', 'software', 'algorithm',
        'protocol', 'web server',
        'machine learning', 'deep learning',
    ],
    'genomics-evolution': [
        'genome assembly', 'pangenome', 'pan-genome', 'polyploid', 'phylogen',
        'comparative genomic', 'whole-genome', 'synteny',
        'gene family expansion', 'domestication', 'selection signature',
        'gwas', 'qtl', 'genome-wide association', 'copy number variation',
        'transposable element', 'evolutionary analysis',
        'resequencing', 'population structure', 'genomic selection', 'haplotype',

    ],
}

# ── 非研究标题守卫（2026-11-03 第 17 轮）────────────────────────────
# 事故：Corrigendum / Erratum 页在批量重算后拿到了主题标签，随后作为
# "证据"进入主题统计。非研究实体没有可引用的结论，任何主题归属都是噪声，
# 而下游 synthesis / hypotheses 不读 article_kind，只读主题。
# 规则：只看首行标题（正文里出现 "erratum" 字样不算）。
NONRESEARCH_TITLE_RE = re.compile(
    r"^\s*(corrigendum|erratum|retraction|retracted|expression of concern|"
    r"editorial|commentary|reply to|publisher.?s note|correction to|"
    r"publisher correction|published correction|correction:|"
    r"book review|author correction|table of contents|in this issue|"
    r"addendum|letter to the editor)\b",
    re.I)

# ── 病毒类词需要植物宿主上下文（2026-11-03 第 17 轮）───────────────
# 事故：为补 PELOTA 那篇（TYLCV / viral resistance）加入 viro 词后，
# 人副流感病毒融合蛋白、猴痘传播网络、抗病毒药物化学、海绵内共生藻
# 等非植物论文被一并拉进 stress-immunity。
# 规则：若某文本对 stress-immunity 的命中"全部"落在下面这组通用病毒词里，
# 且全文没有任何植物线索，则该命中作废；只要同时出现植物宿主/组织/模式
# 物种词（或 pathogen / NLR / PTI 等非病毒专有免疫词），即保留。
VIRUS_ONLY_WORDS = {
    "virus", "viral", "antiviral", "immunity", "tylcv", "geminivirus",
    "potyvirus", "tospovirus", "begomovirus",
}

# ── 中文关键词（2026-11-03 第 17 轮）────────────────────────────────
# 事故：中文标题页（"热胁迫处理玉米根单细胞转录组差异基因分析"）在纯英文
# 词表下永远 out-of-scope，形成结构性覆盖盲区；实测这类页面约 300 个。
# 只收"在中文语境下歧义可接受"的复合词，避免单字/泛词。
ZH_KEYWORDS = {
    "single-cell-spatial-omics": [
        "单细胞", "空间转录组", "空间组学", "单核", "细胞图谱", "拟时序",
    ],
    "developmental-biology": [
        "花药", "愈伤组织", "体细胞胚", "胚胎发育", "分生组织", "花发育",
        "种子发育", "果实发育", "器官发生", "形态建成", "育性",
    ],
    "metabolism-natural-products": [
        "黄酮", "花青素", "生物合成", "次生代谢", "萜类", "木质素",
        "苯丙烷", "类胡萝卜素", "生物碱", "天然产物",
    ],
    "hormone-signaling": [
        "生长素", "细胞分裂素", "赤霉素", "油菜素内酯", "脱落酸",
        "茉莉酸", "水杨酸", "独脚金内酯", "乙烯信号", "激素信号",
    ],
    "stress-immunity": [
        "干旱胁迫", "盐胁迫", "冷胁迫", "热胁迫", "抗病", "病原菌",
        "免疫反应", "系统获得性抗性", "活性氧迸发",
    ],
    "epigenetics-gene-regulation": [
        "染色质", "组蛋白修饰", "DNA甲基化", "转录因子", "表观遗传",
        "增强子", "小RNA",
    ],
    "methods-tools": [
        "分析流程", "工具包", "数据库", "算法", "基准测试", "软件",
    ],
    "genomics-evolution": [
        "基因组", "泛基因组", "多倍体", "系统发育", "进化分析",
        "驯化", "全基因组关联", "共线性",
    ],
}

# ── 主题强度排序（2026-11-03 第 17 轮）──────────────────────────────
# 旧写法 set(list(tset)[:2]) 依赖 set 迭代顺序，而 CPython 对 str 的哈希
# 每进程随机化 → 同一页面两次运行可能留下不同主题，造成每日 diff 抖动。
# 现在按"HI 命中数 > LO 命中数 > 主题名"确定性排序后再截断。

THEME_KEYWORDS_LO = {
    'single-cell-spatial-omics': ['cluster', 'marker gene', 'trajectory',
                                  'in situ sequencing'],
    'developmental-biology': ['differentiation', 'cell division', 'patterning',
                              'stem cell'],
    'metabolism-natural-products': ['metabolite', 'metabolic pathway',
                                    'enzyme activity'],
    'hormone-signaling': ['ethylene', 'hormone', 'receptor kinase',
                          'phosphorylation'],
    'stress-immunity': ['stress', 'drought', 'salinity', 'oxidative stress',
                        'cold', 'heat'],
    'epigenetics-gene-regulation': ['methylation', 'acetylation', 'promoter',
                                    'gene expression', 'epigenetics'],
    'methods-tools': ['tool', 'method', 'framework'],
    'genomics-evolution': ['genomics', 'evolution', 'genome-wide',
                           'chromosome'],
}

# 中文关键词并入 HI 表：中英同权，但中文词只在中文文本里出现，
# 不会稀释英文匹配（子串匹配对英文摘要无副作用）。
for _zh_theme, _zh_kws in ZH_KEYWORDS.items():
    THEME_KEYWORDS_HI[_zh_theme] = list(THEME_KEYWORDS_HI[_zh_theme]) + list(_zh_kws)

# 兼容旧接口：外部若仍按 THEME_KEYWORDS 遍历，拿到的是两级合并视图。
THEME_KEYWORDS = {
    t: THEME_KEYWORDS_HI[t] + THEME_KEYWORDS_LO[t] for t in THEMES
}

# 软标签：这些标签过于宽泛，不能单独作为主题依据；但当 claim/title 同时
# 命中该主题的 HI 关键词时，说明它确实是这个主题的文献（而不是"全库"）。
SOFT_TAGS = {'metabolism': 'metabolism-natural-products'}

# 主题之间允许共享关键词造成的重复计数，最多允许一个证据同时进 2 个主题；
# 超过则视为"泛化证据"，三个脚本都忽略（避免同一结论出现在 5 个报告里）。
MAX_THEMES_PER_EVIDENCE = 2

# ── 元数据充分性下限（2026-11-03 第 17 轮）───────────────────────────
# 事故：删掉"沿用旧 themes"的兜底后，802 个页面被判 out-of-scope，其中
# 569 个的"摘要"不足 100 字符（多为只有一行标题 + "详见原始文献"）。
# 这类页面不是"确定不属于八主题"，而是"信息量不足以下判断"。
# 两者混用一个 out-of-scope，等于把"未知"说成"已知的不相关"。
# 单列 unclassified，让报告同时暴露三个数：mapped / unclassified / out-of-scope。
THEME_EVIDENCE_MIN_CHARS = 300
UNCLASSIFIED_BASIS = "insufficient-metadata"


def evidence_sufficient(text):
    """文本是否长到可以下"相关/不相关"的结论。"""
    return len((text or "").strip()) >= THEME_EVIDENCE_MIN_CHARS

_WS = re.compile(r'\s+')


_LIGATURES = {
    '\ufb00': 'ff', '\ufb01': 'fi', '\ufb02': 'fl', '\ufb03': 'ffi',
    '\ufb04': 'ffl', '\ufb05': 'ft', '\ufb06': 'st',
    '\u00ad': '',
    '\u2019': "'", '\u2018': "'", '\u201c': '"', '\u201d': '"',
    '\u00a0': ' ',
    '\u2013': '-', '\u2014': '-',
}


def fold(text):
    """PDF 抽取的合字与特殊字符归一化。"""
    if not text:
        return ''
    out = []
    for ch in text:
        out.append(_LIGATURES.get(ch, ch))
    return ''.join(out)


def normalize_tag(tag):
    """标签归一化：去 #、去引号、小写、空格/下划线→连字符。"""
    if not tag:
        return ''
    t = fold(tag).strip().strip('"\'#').strip()
    t = t.lower().replace('_', '-')
    t = _WS.sub('-', t)
    return t.strip('-')


def normalize_tags(tags):
    """把标签序列归一化并去重（保持顺序）。"""
    seen, out = set(), []
    for t in tags or ():
        n = normalize_tag(t)
        if n and n not in seen:
            seen.add(n)
            out.append(n)
    return out


def themes_from_tags(tags):
    """标签 → 主题集合（只认别名表，不做关键词猜测）。"""
    hits = set()
    for t in normalize_tags(tags):
        if t in GENERIC_TAGS:
            continue
        theme = THEME_TAG_ALIASES.get(t)
        if theme:
            hits.add(theme)
    return hits


def _has_plant_context(low):
    """文本里是否有植物线索（复用 purity_gate 的词表，避免第二套规则）。"""
    try:
        import purity_gate as _pg
    except Exception:              # 独立导入 themes 时的降级路径
        return bool(re.search(r"plant|crop|arabidopsis|rice|maize|tomato", low))
    cues = (_pg.PLANT_HOST_CUES + _pg.PLANT_ORGANISM
            + _pg.PLANT_GENERIC_CUES)
    return any(c in low for c in cues)


def _theme_hits(low):
    """已过守卫的主题命中：返回 (themes, {theme: (hi_n, lo_n)})。"""
    hits, detail = set(), {}
    plant_ok = None
    for theme in THEMES:
        hi = [kw for kw in THEME_KEYWORDS_HI[theme] if kw in low]
        lo = [kw for kw in THEME_KEYWORDS_LO[theme] if kw in low]
        ok = bool(hi) or len(lo) >= 2
        if ok and theme == "stress-immunity":
            matched = set(hi) | set(lo)
            # 仅由通用病毒词支撑 → 必须有植物宿主上下文
            if matched and matched <= VIRUS_ONLY_WORDS:
                if plant_ok is None:
                    plant_ok = _has_plant_context(low)
                ok = plant_ok
        if ok:
            hits.add(theme)
            detail[theme] = (len(hi), len(lo))
    return hits, detail


def themes_from_text(text):
    """文本 → 主题集合。

    规则（2026-11-03 分级版）：
      * 命中任意 HI 词 → 该主题成立；
      * 未命中 HI，但命中 >=2 个不同 LO 词 → 该主题成立；
      * 仅 1 个 LO 词 → 不成立（歧义词不可单独作证）；
      * 非研究标题（Corrigendum/Erratum/Editorial…）→ 一律不归属；
      * stress-immunity 仅由通用病毒词支撑时，要求全文含植物线索。
    """
    low = fold(text).lower()
    if not low:
        return set()
    if NONRESEARCH_TITLE_RE.match(low.split("\n", 1)[0]):
        return set()
    hits, _detail = _theme_hits(low)
    return hits


def rank_themes(theme_set, text=""):
    """按证据强度确定性排序（HI 命中 > LO 命中 > 字母序）。"""
    if not theme_set:
        return []
    _hits, detail = _theme_hits(fold(text or "").lower())
    def key(t):
        hi_n, lo_n = detail.get(t, (0, 0))
        return (-hi_n, -lo_n, t)
    return sorted(theme_set, key=key)


def theme_keyword_evidence(text):
    """返回 {theme: (hi_hits, lo_hits)}，供审计与报告解释归属依据。"""
    low = fold(text).lower()
    out = {}
    for theme in THEMES:
        hi = sum(1 for kw in THEME_KEYWORDS_HI[theme] if kw in low)
        lo = sum(1 for kw in THEME_KEYWORDS_LO[theme] if kw in low)
        if hi or lo:
            out[theme] = (hi, lo)
    return out


# ── 主题级 claim 守卫（2026-11-03）──────────────────────────────────
# 标签可能来自论文级误标：一个 `single-cell-spatial` 标签会把 Cas9 通用综述
# 拉进单细胞 synthesis。标签命中仍然优先，但 claim/title 必须至少一处
# 真正谈该主题的核心对象；否则视为"泛化标签"，不进入该主题的统计与假说。
# 说明（2026-11-03 第 17 轮）：守卫的目的只是"挡掉被错误标签拉进来的
# 泛化文献"，因此其正则必须覆盖同主题的关键词表本身 —— 否则关键词命中
# 会被守卫反手清空（中文页 300+ 全部踩中：`单细胞` 命中后被英文正则删掉）。
# 现在两个守卫的正则 ⊇ 对应 HI/LO 词表（中英双语），语义是
# "正文至少提到该主题的核心对象"，不是第二道主题判定。
THEME_CLAIM_GUARDS = {
    'single-cell-spatial-omics': re.compile(
        r'(single[- ]cell|scrna|snrna|spatial transcript|stereo[- ]?seq|'
        r'merfish|visium|slide[- ]?seq|cell atlas|cell[- ]type|cell type|'
        r'cluster|marker gene|pseudotime|trajectory|spatial omics|'
        # 2026-11-03 第 17 轮：中文页此前永远过不了这道守卫
        r'单细胞|单核|空间转录组|空间组学|细胞图谱|拟时序)', re.I),
    'genomics-evolution': re.compile(
        r'(genom|pangenome|pan-genome|phylogen|synteny|gene family|'
        r'domestication|polyploid|gwas|qtl|selection signature|evolution|'
        r'copy number variation|transposable element|'
        # 2026-11-03 第 17 轮：中文词补齐，否则中文基因组页被守卫清空
        r'基因组|泛基因组|系统发育|进化|驯化|多倍体|共线性|'
        r'全基因组关联|转座子)', re.I),
}


def claim_supports_theme(theme_id, text):
    rx = THEME_CLAIM_GUARDS.get(theme_id)
    return bool(rx.search(text or '')) if rx else True


def filter_supported_themes(theme_set, text):
    return {t for t in (theme_set or set()) if claim_supports_theme(t, text)}


def assign_themes(tags, text=''):
    """返回 (themes, basis)。

    basis ∈ {'tag', 'keyword', 'tag+keyword', None}
      tag         精确主题标签命中（最高置信）
      keyword     正文 HI 关键词（或 >=2 个 LO 关键词）命中
      None        无法归属 —— 调用方必须显式记为 unclassified，
                  不得默认塞进"其他主题"来制造覆盖假象
    """
    if NONRESEARCH_TITLE_RE.match((text or "").split("\n", 1)[0]):
        # 非研究实体（更正/撤稿/社论）：没有可引用结论，不归属任何主题
        return set(), None

    by_tag = themes_from_tags(tags)
    by_kw = themes_from_text(text)

    if by_tag:
        merged = by_tag | by_kw
        if len(merged) > MAX_THEMES_PER_EVIDENCE:
            merged = by_tag          # 标签优先，关键词只做补位，不能扩张
        return merged, ('tag+keyword' if by_kw - by_tag else 'tag')
    if by_kw:
        return by_kw, 'keyword'

    # 说明（2026-11-03）：曾设计 'soft-tag' 兜底（metabolism 宽标签 + 正文 HI
    # 词佐证），但 by_kw 非空时已在上方返回 'keyword'，该分支永远不可达，
    # 属死代码，故移除。metabolism 桶的回收改由 repair_theme_tags.py 用
    # "论文标题+摘要"作上下文，命中 HI 词即按 'keyword' 归属。
    return set(), None


def assign_for_import(title, abstract='', keywords=None):
    """入库时的主题归属（唯一入口契约，两个 importer 都调用这里）。

    2026-11-03：daily_update.py 导入时只写 tags: [papers]，不写 themes，
    于是新入库论文 100% 没有主题，只能靠事后 repair_theme_tags 回填；
    而 daily_full_pipeline 里另有一份 _assign_import_themes 的复制品，
    两边规则漂移。统一到本函数：关键词与正文同权，再做 claim 守卫与上限。

    返回 (themes:set, status:str, basis:str|None)，
    status ∈ {'mapped', 'out-of-scope'}。
    """
    kw = [k for k in (keywords or []) if k]
    text = '\n'.join(x for x in (title or '', abstract or '', ' '.join(kw)) if x)
    tset, basis = assign_themes([], text)
    tset = filter_supported_themes(tset, text)
    if len(tset) > MAX_THEMES_PER_EVIDENCE:
        tset = set(rank_themes(tset, text)[:MAX_THEMES_PER_EVIDENCE])
    if tset and management_scope_block(title):
        return set(), 'out-of-scope', MANAGEMENT_SCOPE_BASIS
    return tset, ('mapped' if tset else 'out-of-scope'), basis


# ── 农艺管理类论文的"主题外"判定（2026-11-03 第 17 轮）────────────────
# 用户反复指出的问题："植物相关"被当成了"八个植物科学主题相关"。
# 实测受害例：分施钾肥对产量/品质的影响（被判 developmental-biology，
# 只因摘要里出现 tiller/panicle）、亚热带人工林土壤磷库分层（被判
# metabolism，只因出现 metabolomics）、热带雨林养分梯度（同理）。
# 这些是农艺/生态管理研究，研究对象是群体与田块，不是八主题的分子机制。
# 规则：标题命中管理措施词、且标题本身不含任何主题词 → 判 out-of-scope。
# 标题含主题词的（如 "Fertilization alters auxin distribution in roots"）不受影响。
SCOPE_MANAGEMENT_TITLE_RE = re.compile(
    r"(fertiliz|irrigation|tillage|sowing date|sowing density|plant density|"
    r"intercropping|inter-cropping|crop rotation|mulch|plastic film|"
    r"nitrogen use efficiency|yield trial|multi-environment trial|"
    r"multi-location|compost|soil amendment|soil organic|"
    r"conservation tillage|water use efficiency|crop wild relatives|"
    r"planting pattern|row width|ridge|film mulching)", re.I)

MANAGEMENT_SCOPE_BASIS = "scope:agronomy-management"


def management_scope_block(title):
    """标题是"管理措施型"研究且标题本身无主题词 → 不属于八主题。"""
    t = title or ""
    if not SCOPE_MANAGEMENT_TITLE_RE.search(t):
        return False
    return not themes_from_text(t)


def is_theme(theme_id):
    return theme_id in THEME_META


def display_title(theme_id, lang='en'):
    meta = THEME_META.get(theme_id, {})
    if lang == 'zh':
        return meta.get('title_zh') or theme_id
    return meta.get('title') or theme_id

# ── PDF 抽取噪声清洗 ──────────────────────────────
# 两个生成器都必须用同一份清洗，否则同一页在一边命中关键词、
# 在另一边不命中，主题证据数就对不上。
SOFT_HYPHEN_CHARS = ('\u00ad', '\u2010', '\u2011', '\u00a0')


def normalize_claim(text):
    """清理 PDF 抽取噪声：软连字符断词、合字、弯引号、多余空白。"""
    if not text:
        return ''
    t = text
    t = re.sub(r'([A-Za-z])\u00ad\s*([a-z])', r'\1\2', t)
    for ch in SOFT_HYPHEN_CHARS:
        t = t.replace(ch, ' ')
    t = re.sub(r'\b([a-z]{3,})-\s+([a-z]{2,})\b', r'\1-\2', t)
    t = re.sub(r'\b([A-Za-z]{3,})-\s+([A-Z]{3,})\b', r'\1\2', t)
    t = t.replace('\u2019', "'").replace('\u2018', "'")
    t = t.replace('\u201c', '"').replace('\u201d', '"')
    t = fold(t)
    t = ' '.join(t.split())
    for _ in range(3):
        t2 = re.sub(r'\b([A-Za-z][A-Za-z\-]{2,})\s+\1\b', r'\1', t)
        if t2 == t:
            break
        t = t2
    return t
