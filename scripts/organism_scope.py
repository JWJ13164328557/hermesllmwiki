#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""organism_scope.py — 研究对象（植物 / 非植物）判定的唯一实现。

为什么单独成模块（2026-11-02 第 24 轮）
--------------------------------------
同一件事此前有四份实现，阈值各不相同：

  theme_filter.is_relevant_plant_paper  下载层：期刊黑名单，默认放行
  purity_gate.classify                  下载层：主体词命中，默认放行
  batch_hypotheses.ANIMAL_TERMS         主题层：计数比，默认保留
  species_patterns.*                    物种归属（正交问题）

后果是"下载层拦了、导入层没拦"：2026-11-02 当日 156 篇里 7 篇明显非植物
（肉鸡生产性能、4D 打印组织再生、人参外泌体治结肠炎、Corosolic acid 治 MASLD）
仍然写进了 evidence/ 与主题综述页，因为 batch_evidence_objects 在
write_paper() 里只检查"有没有 ### 核心发现"，从不问"研究对象是什么"。

本模块只回答一个问题：**这篇论文的研究对象是植物吗？**
三层调用方共用同一份词表，但**阈值分层**（宁可漏判，不可误杀）：

  classify_text(text)                 纯文本计数比判定，供主题层沿用
  page_verdict(...)                   概念页级判定（文本 + 期刊先验 + 物种列表），
                                      供导入层落盘与审计，附可复核的 reasons
  paper_scope_table(concepts_dir)     DOI -> {label, method} 缓存，供主题层查表

分层理由：导入层一旦误杀，论文永久丢失且不易察觉（比漏放代价高）；
因此 page_verdict 只在"明确的医学/动物研究对象 + 完全没有植物本体证据"
时才判 nonplant，并在 reasons 里写明命中的是哪个词，便于人工复核。
"""
from __future__ import annotations

import os
import re

# ── 泛称物种：不构成"这是植物研究"的证据 ─────────────────────────
GENERIC_SPECIES = ('', 'Plant', 'Plant (unspecified)', '未识别', 'Unknown')

# ── ① 动物/医学"领域词"：出现即说明论文语境偏向人/动物 ────────────
# 沿用于主题层的历史词表（未改动，保证 366→189 等既有计数不漂移），
# 只用于 classify_text 的比例判定。
ANIMAL_TERMS = re.compile(
    r"\b(mouse|mice|murine|rat|rats|human|humans|patient|patients|clinical|"
    r"zebrafish|drosophila|caenorhabditis|pig|pigs|porcine|bovine|cattle|"
    r"sheep|goat|rabbit|monkey|macaque|marmoset|chicken|chick|embryoid|"
    r"tumou?r|carcinoma|adenocarcinoma|xenograft|organoid|organoids|"
    r"neuron|neurons|neuronal|neural|glia|astrocyte|microglia|cortex|cortical|"
    r"hippocampus|hippocampal|brain|spinal|retina|retinal|embryonic stem cell|"
    r"induced pluripotent|biopsy|serum|plasma|cancer cell)\b", re.I)

# ── ② 植物"领域词" ────────────────────────────────────────────────
PLANT_TERMS = re.compile(
    r"\b(plant|plants|arabidopsis|oryza|rice|wheat|triticum|maize|zea|"
    r"soybean|glycine max|tomato|solanum|tobacco|nicotiana|poplar|populus|"
    r"grape|vitis|apple|malus|citrus|cotton|gossypium|brassica|rapeseed|"
    r"medicago|alfalfa|lucerne|sorghum|barley|hordeum|cucumber|cucumis|"
    r"potato|pepper|capsicum|tea plant|camellia sinensis|banana|mango|"
    r"cassava|sugarcane|moss|physcomitrella|selaginella|chlorella|"
    r"seedling|seedlings|leaf|leaves|root|roots|shoot|shoots|pollen|"
    r"stomata|chloroplast|photosynthesis|xylem|phloem|meristem|"
    r"endosperm|panicle|inflorescence|silique|tuber|corm|rhizome)\b", re.I)

# ── ③ "研究对象明确是人/动物"的强标记（导入层专用，比 ① 更严）──────
# 只收"只能是人/动物机体或临床终点"的词。刻意**不收** serum/plasma/brain
# 这类在植物文献里也会出现的词（"plasma membrane"、"brain of the root"）。
ANIMAL_SUBJECT = re.compile(
    r"\b(?:(broilers?|laying hens?|layer chicks?|piglets?|dairy cows?|calves|"
    r"(mouse|mice|murine|rats?|rabbits?|monkeys?|macaques?|zebrafish|"
    r"livestock|poultry|swine|ruminants?|broiler|aquafeed|fish meal|polar bear|ursus maritimus)\b|"
    r"layers?'|laying flock|breeder flocks?|broiler breeders?|"
    r"nude mice|sd rats|wistar|sprague[- ]dawley|"
    r"hela|hek293|hepg2|caco-2|raw ?264|thp-1|a549|mcf-7|"
    r"mesenchymal stem cell|adipose[- ]derived stem cell|"
    r"randomized controlled|randomised controlled|"
    r"volunteers|healthy adults|human subjects|cohort study|"
    r"ulcerative colitis|colitis|inflammatory bowel|"
    r"wound healing|wound dressing|skin wound|hypertrophic scar|"
    r"tissue regeneration|tissue engineering|4d printing|"
    r"atheroscleros|myocardial infarct|ischemia[- ]reperfusion|"
    r"alzheimer|parkinson|masld|nafld|steatotic liver|"
    r"hepatoprotective|nephroprotect|neuroprotect|"
    r"colorectal cancer|breast cancer|lung cancer|gastric cancer|"
    r"hepatocellular carcinoma|leukemia|lymphoma|melanoma|"
    r"tumor microenvironment|prognosis|survival analysis|"
    # 2026-11-03 补：医学/神经语境（此前漏收，导致 Lipedema 脂肪组织、
    # 脑体细胞突变综述被记为 unknown，进而混入植物单细胞主题正文）。
    r"lipedema|adipose tissue|adipocytes?|obesity|overweight|"
    r"\bbrain\b|\bneurons?\b|\bneuronal\b|\bastrocytes?\b|"
    r"\bsomatic mutation|\bhot spots linked to\b|"
    r"gut microbiome|gut microbiota|intestinal barrier|"
    r"production performance|feed conversion ratio|growth performance|"
    r"average daily gain|body weight gain|feed efficiency|"
    r"sars-cov|covid-19|influenza vaccine|"
    r"hermetia|illucens|black soldier fly|tenebrio|"
    r"galleria mellonella|drosophila melanogaster|"
    r"bombyx mori|silkworm))"
    , re.I)
# ── ④ "研究对象是植物本身"的强标记（用于对冲 ③ 的误杀）──────────────
PLANT_SUBJECT = re.compile(
    r"\b(?:(germination|root elongation|lateral root|root hair|nodulation|"
    r"mycorrhiza|rhizosphere|field trial|agronomic|cultivar|germplasm|"
    r"heterosis|vernalization|photoperiod|tillering|panicle|spikelet|"
    r"flowering time|fruit ripening|leaf senescence|stomatal|"
    r"thylakoid|cell wall|xylem|phloem|cambium|meristem|trichome|"
    r"pollen tube|anther|ovule|embryo sac|vascular bundle|cuticle|suberin|"
    r"lignin biosynthesis|plant immunity|effector-triggered|"
    r"salicylic acid signaling|jasmonate signaling|auxin transport|"
    r"brassinosteroid|abscisic acid|gibberellin|strigolactone|"
    r"auxin|cytokinin|jasmonate|salicylic acid|ethylene signaling|"
    r"photosynth|chlorophyll|flavonoid|anthocyanin|terpenoid biosynthesis|"
    r"agrobacterium|transgenic plant|protoplast|hairy root|adventitious root|"
    r"plant cell culture|cell suspension culture|callus induction|"
    r"phytopathogen|root-knot nematode|cyst nematode|"
    r"kelp|seaweed|macrocystis|nereocystis|laminaria|saccharina|ulva|porphyra|"
    r"brown alga|red alga|green alga|diatom|"
    r"biofertiliz|biostimulant|foliar spray))"
    , re.I)
# ── ⑤ 具体物种名：可作"植物自证"（排除泛组织词）────────────────────
CONCRETE_SPECIES = re.compile(
    r"\b(?:(arabidopsis|thaliana|oryza|rice|wheat|triticum|maize|zea mays|"
    r"sorghum|soybean|glycine max|tomato|solanum lycopersicum|potato|"
    r"tobacco|nicotiana|barley|hordeum|medicago|alfalfa|lotus|"
    r"brassica|rapeseed|cotton|gossypium|citrus|vitis|grape|malus|apple|"
    r"populus|poplar|eucalyptus|camellia sinensis|tea plant|cassava|"
    r"sugarcane|saccharum|physcomitrella|marchantia|selaginella|"
    r"chlorella|chlamydomonas|duckweed|lemna|"
    r"cucumis|cucumber|capsicum|pepper|mango|banana|strawberry|"
    r"pinus|picea|quercus|ficus|carica papaya|ginseng|panax|"
    r"amentotaxus|ginkgo|taxus|catharanthus|artemisia|salvia|"
    r"nereocystis|saccharina|laminaria|macrocystis|undaria|porphyra|"
    r"eisenia|ulva|gracilaria|chondrus))"
    , re.I)
# ── ⑤b 否定"标题权威"的语境：标题虽点名作物，但研究对象不是作物 ────
# 两类反例（2026-11-02 实测）：
#   anu/9006952  "Dietary Substitution of Soybean Meal ... in Grass Carp"
#                -> 研究对象是鱼，大豆只是饲料原料
#   adma.73441   "Multicolor ... Phosphorescence in Rice-Derived Carbon Dots"
#                -> 研究对象是发光材料，稻壳只是碳源
# 因此：标题出现饲喂/水产/营养**终点**词，或材料/衍生**加工**词时，
# 不启用"标题点名作物即植物"的规则（退回原有阈值判定，通常为 unknown，
# 而 unknown 仍会被主题层收录，不会造成丢失）。
FEED_CONTEXT = re.compile(
    r"(dietary|\bdiet\b|\bfeed\b|feeding|\bmeal\b|aquaculture|grass carp|"
    r"\bfish\b|shrimp|growth performance|nutrient retention|feed efficiency|"
    r"broiler|poultry|livestock|\brumen\b|silage|\bmilk\b|egg production)", re.I)

MATERIAL_CONTEXT = re.compile(
    r"(derived|carbon dots?|doping|doped|phosphorescence|encryption|"
    r"nanoparticles?|nanocomposite|thin films?|hydrogel|surfactant|"
    r"\bMXene\b|electrode|battery|photocatalys|adsorption isotherm)", re.I)

# ── ⑤c 第三类否决语境：研究对象是"人/动物疾病或环境暴露" ──────────────
# 与 FEED_CONTEXT（饲喂终点）、MATERIAL_CONTEXT（材料加工）并列。
# 2026-11-02 实测的 6 个误升级反例（标题点名作物 -> 被升为 plant，实为医学/环境）：
#   10.1002/jsfa.70858  黑大豆肽缓解乳糜泻氧化损伤   (celiac)
#   10.1007/s11356-...  稻米加工厂 PM 的空气暴露健康风险 (airborne/particulate)
#   10.1016/j.foodres.. 稻米中真菌毒素的人体暴露        (human exposure)
#   10.1016/j.mmr.....  烟草疾病负担 GBD               (disease burden/tobacco)
#   10.1016/j.mtbio.... 米糠肽靶向 BMSC 治骨质疏松      (osteoporo/BMSC)
#   10.1186/s40643-...  Hermetia illucens 产月桂酸     (昆虫，已由 ③ 拦截)
# 刻意**不收** disease 单字：植物病理学大量使用 "disease resistance/tolerance/
# management"，收单字会大面积误杀抗病研究。
BIOMED_CONTEXT = re.compile(
    r"\bceliac\b|\bcolitis\b|\bosteoporo|\bcancer\b|\btumou?rs?\b|"
    r"\bdiabet|\bpatients?\b|\bclinical trial\b|\bcohort\b|"
    r"\bepidemiolog|\bglobal burden of disease\b|\bdisease burden\b|"
    r"\bmortality\b|\bmorbidit|\bhuman exposure\b|\bhealth risk\b|"
    r"\brisk assessment\b|\bairborne\b|\bparticulate matter\b|"
    r"\btobacco\b|\bcaco-?2\b|\bbmsc\b|\bin vitro digestion\b|"
    r"\bbioaccessib|\bbioavailab", re.I)

# ── ⑥ 通用方法学标记：演示数据来自动物但方法本身对植物可用 ──────────
METHOD_MARKERS = re.compile(
    r"(single[- ]cell|scrna|snrna|spatial transcriptom|atac|"
    r"deep[\s-]learning|machine[\s-]learning|neural network|transformer|"
    r"benchmark|pipeline|workflow|toolkit|algorithm|software|database|"
    r"web server|framework|differential expression|normalization method|"
    r"negative binomial|statistical framework|imputation)", re.I)


def _hits(pattern, text):
    return sorted({m.group(1).lower() for m in pattern.finditer(text or '')})


def classify_text(text):
    """纯文本判定：plant / nonplant / unknown（主题层沿用，比例规则不变）。

    规则（与 2026-11-02 主题层一致，勿单独调参）：
      只有动物词且 >=2 个 -> nonplant；只有植物词且 >=2 个 -> plant；
      两者都有时，一方 >= 2 倍另一方且 >=4 个才算胜出；否则 unknown。
    """
    if not text:
        return 'unknown'
    animals = _hits(ANIMAL_TERMS, text)
    plants = _hits(PLANT_TERMS, text)
    if animals and not plants:
        return 'nonplant' if len(animals) >= 2 else 'unknown'
    if plants and not animals:
        return 'plant' if len(plants) >= 2 else 'unknown'
    if len(plants) >= 2 * len(animals) and len(plants) >= 4:
        return 'plant'
    if len(animals) >= 2 * len(plants) and len(animals) >= 4:
        return 'nonplant'
    return 'unknown'


def page_verdict(title, abstract, journal='', species=(), themes=(), tags=()):
    """概念页级判定，返回 (verdict, reasons)。

    verdict: 'plant' | 'nonplant' | 'unknown'
    reasons: 命中词列表，形态如 'subject=colitis'，便于人工逐条复核。

    判定顺序（先否定，再肯定）：
      1. 文本里出现"植物本体"强标记或具体物种 -> plant（医学词不再一票否决）
      2. 只有动物/医学研究对象强标记，且无任何植物本体证据 -> nonplant
      3. 其余 -> unknown（导入层放行，交由主题层按证据复核）
    """
    title = title or ''
    abstract = abstract or ''
    journal = journal or ''
    text = title + ' ' + abstract

    subj = _hits(ANIMAL_SUBJECT, text)
    plant_subj = _hits(PLANT_SUBJECT, text)
    concrete = _hits(CONCRETE_SPECIES, text)
    # 物种字段：只有"具体物种"才算自证；泛称（Plant/未识别）不算
    sp_concrete = [s for s in species
                   if s and s not in GENERIC_SPECIES and CONCRETE_SPECIES.search(s)]

    plants_all = _hits(PLANT_TERMS, text)
    # 判定为植物研究需要"成体系的植物语境"，而非一次物种名出现：
    #   - 命中植物本体过程词（光合/分生组织/激素信号…），或
    #   - 至少 2 个具体物种，或
    #   - 1 个具体物种且全文植物领域词 >= 3
    # 2026-11-02 反例：Febuxostat-人血清白蛋白的摘要提了一次 cotton（染料），
    # 旧规则据此把整篇化学论文判成植物研究。
    # 标题权威性（2026-11-02 新增）：标题里点名的具体作物 + 标题里没有动物主体词
    # -> 研究对象就是该作物。摘要里提一次 broiler（例如"用陈化小麦淀粉喂肉鸡"）
    # 不足以否定它 —— 反例 10.1016/j.fochx.2026.104303「陈化小麦淀粉与蛋白的
    # 结构演化」被判 nonplant（因为摘要出现 broiler），整篇植物论文被永久丢弃。
    # 反向保护：若标题同时含动物词（"Artemisia extract on broiler performance"），
    # 仍按动物研究处理，植物只充当药物来源。
    concrete_title = _hits(CONCRETE_SPECIES, title)
    animal_title = _hits(ANIMAL_SUBJECT, title)
    # 饲喂/水产语境 与 材料衍生语境 下，标题里的作物名不代表研究对象
    off_topic = bool(FEED_CONTEXT.search(title) or MATERIAL_CONTEXT.search(title)
                    or BIOMED_CONTEXT.search(title))
    title_is_plant = bool(concrete_title) and not animal_title and not off_topic

    if title_is_plant or plant_subj or len(concrete) >= 2 or (concrete and len(plants_all) >= 3):
        reasons = []
        if concrete:
            reasons.append('plant-species=' + ','.join(concrete[:3]))
        if plant_subj:
            reasons.append('plant-subject=' + ','.join(plant_subj[:3]))
        if title_is_plant:
            reasons.append('plant-title=' + ','.join(concrete_title[:2]))
        return 'plant', reasons

    plants = _hits(PLANT_TERMS, text)
    # 领域词占绝对优势时仍判植物：至少 3 个植物领域词、动物主体词不超过 1 个。
    # 收窄到 3:1 是为了不放过"Capparis 提取物治创面"（plant=2, anim=1）这类
    # 植物只是药物来源的论文 —— 它们的研究对象是创面，不是植物。
    if len(plants) >= 3 and len(subj) <= 1 and len(plants) > 2 * max(len(subj), 1):
        return 'plant', ['plant-domain=%d' % len(plants)]

    if subj:
        # 标题明写 "in plants" 的窄救援（第 25 轮）。只作用于"即将判非植物"
        # 的这一个出口，且要求标题不含具体动物物种，因此不改变任何 plant /
        # unknown 结论，全库影响面实测 1 页。
        # 反例 10.1016/j.pbi.2019.09.003《A single-cell view of tissue
        # regeneration in plants》：ANIMAL_SUBJECT 为收纳"再生医学"语境
        # 收了 `tissue regeneration`，把一篇植物综述判成非植物；加严
        # is_method_paper 后它会被整篇丢弃，故在此按标题权威性救回。
        # 用复数 `in plants`（不是 `in plant`）：单数会命中
        # "in plant-based diets"（10.1186/s12917-026-05625-2 饲用植酸酶），
        # 那是动物营养研究，必须仍判非植物。
        if (re.search(r'\bin plants\b', title, re.I)
                and not _hits(CONCRETE_SPECIES, title)
                and not ANIMAL_NOUN_TITLE.search(title)):
            return 'plant', ['plant-title=in-plants']
        return 'nonplant', ['subject=' + ','.join(subj[:4])]

    # 只有"物种字段"能自证时才认植物，且必须放到动物主体词之后判断。
    # 2026-11-02 的教训：`**物种**` 字段由 deep_curate 按提及位置加权生成，
    # 并被图注正则污染过（Ficus carica 虚标 970 页）。把它放在动物主体词
    # **之前**，会让"人血清白蛋白""大鼠脑辐射"这类论文仅凭一个错标物种
    # 就被判成植物研究。
    if sp_concrete:
        # 只记录、不定性：物种字段是 deep_curate 按提及位置加权的产物，
        # 曾被 `\bfig\b` 正则污染（"Fig. 1" -> Ficus carica），
        # 实测 324 页仍带该虚标值。作为"植物"证据会直接放过动物论文。
        return 'unknown', ['species-field-unverified=' + ','.join(sp_concrete[:3])]

    # 退化到计数比（此处只用 ①/② 两张宽表）
    return classify_text(text), []


# 临床/疾病终点：即使通篇是算法，也说明研究对象不是植物
CLINICAL_OBJECT = re.compile(
    r"(patient|patients|clinical|trial|cancer|carcinoma|tumou?r|leukemia|"
    r"lymphoma|melanoma|prognosis|survival|biopsy|cohort|vaccine|"
    r"colitis|wound|cartilage|osteoarthrit|alzheimer|parkinson|diabet|"
    r"broiler|poultry|livestock|cattle|pig|bovine|ovine|rumen)", re.I)


# 技术名词（用于识别"某技术本身"的论文标题）
TECHNIQUE_MARKERS = re.compile(
    r"(spatial transcriptom|single[- ]cell (?:rna[- ]?seq|transcriptom|sequencing|atlas)|"
    r"scrna[- ]?seq|snrna[- ]?seq|atac[- ]?seq|chip[- ]?seq|"
    r"mass spectrometr|proteomic|metabolomic|lipidomic|"
    r"crispr|base editing|prime editing|"
    r"super[- ]resolution|light[- ]sheet|cryo[- ]?em|"
    r"merfish|seqfish|visium|stereo[- ]?seq)", re.I)

# 器官/组织名词：标题里出现时说明研究对象是某个器官，不是技术
ORGAN_TERMS = re.compile(
    r"(brain|cortex|hippocamp|kidney|renal|liver|hepat|lung|pulmonary|heart|cardiac|"
    r"blood|serum|plasma|bone|cartilage|skin|retina|muscle|gut|intestin|colon|"
    r"placenta|embryo of|organoid|tumou?r)", re.I)

# "in plants" 标题救援时用于否决的动物**名词**表。
# 与 ANIMAL_SUBJECT 的区别：ANIMAL_SUBJECT 为收纳"再生医学/动物实验"语境
# 收了 `tissue regeneration`、`4d printing` 这类**过程/技术**词，用它们
# 否决会把 "tissue regeneration in plants" 这样的植物综述挡在门外。
# 这里只留真正的动物名词，用于判断"研究对象是不是被拿去喂动物/做动物实验"。
ANIMAL_NOUN_TITLE = re.compile(
    r"\b(mouse|mice|murine|rats?|rabbits?|pig|piglets?|swine|cattle|bovine|"
    r"ovine|chickens?|broilers?|poultry|layers?|zebrafish|fish|humans?|patients?)\b",
    re.I)

# "用某技术做某事"的句式标记
INSTRUMENTAL_CUE = re.compile(
    r"(\bby\b|\busing\b|\bvia\b|based on|\bmethod\b|\bapproach\b|"
    r"\btool\b|\bframework\b|\bworkflow\b|\bpipeline\b|\balgorithm\b|"
    r"\bplatform\b|\bsoftware\b|\bpackage\b)", re.I)

# 注：曾尝试用"工具名冒号前缀"（`^\w+: ...`）作为正向信号，第 25 轮实测否决：
# 该式样同样命中 `SIRT1: Protean roles at the nexus of health, disease…`、
# `Sepiapterin: A Distinct, Dual Mechanism of Action…` 这类综述/药物论文。
# 冒号后的副标题本身就在标题里，由 METHOD_NOUN_TITLE 覆盖即可
# （scTrends / clusterProfiler / movAPA / MFPD 全部经由方法名词命中），
# 因此不再保留单独的 TOOL_NAME_TITLE 判据。

# 方法/操作名词：标题里出现才说明"这篇在讲怎么做"，而不是"讲什么对象"。
# 刻意**不收** profiling / identification / characterization / mechanism /
# landscape —— 它们在生物学论文标题里是对象描述。实测把 "spatial profiling
# of podocytopathies"、"Integrated identification of CYP1A1 ... lung cancer"
# 放进方法类，正是非植物论文绕过闸门的主要通路。
METHOD_NOUN_TITLE = re.compile(
    r"(analysis|framework|pipeline|workflow|algorithm|\btool\b|toolkit|"
    r"software|database|platform|web server|package|benchmark|method|approach|"
    r"deconvolution|binning|denoising|normalization|imputation|quantification|"
    r"classification|prediction|integration|modeling|\bmodels?\b|"
    r"visuali[sz]ation|mapping)", re.I)


def title_is_technique(title):
    """标题是否在讲"某技术/方法本身"，而不是"某物种/器官的生物学"。

    2026-11-02 反例：Stahl 2016（10.1126/science.aaf2403）
    "Visualization and analysis of gene expression in tissue sections by
    spatial transcriptomics" —— 这是空间转录组的奠基论文，摘要里只有 1 个
    方法学标记，按"标记数 >= 2"的规则被整篇 drop。硬编码 DOI 白名单会不断
    膨胀，改用句式判据：技术名词 + 工具性介词 + 无物种/器官/疾病。
    """
    t = title or ''
    if not TECHNIQUE_MARKERS.search(t):
        return False
    if CONCRETE_SPECIES.search(t) or ORGAN_TERMS.search(t):
        return False
    if CLINICAL_OBJECT.search(t):
        return False
    return bool(INSTRUMENTAL_CUE.search(t))


def is_method_paper(text, themes=(), tags=(), title=''):
    """通用方法学论文：方法本身可迁移到植物，允许只进 methods-tools 主题。

    判定顺序（第 25 轮定稿，顺序有语义，勿调换）：
      1. 主题/标签已标 `methods-tools` -> 是（最可靠，来自策展）；
      2. 标题点名研究对象（临床对象 / 具体物种）-> 否决；
      3. 标题自我描述为方法（技术名词句式，或方法名词 + 摘要 >=2 个
         方法学标记）-> 是；
      4. 其余 -> 否。

    第 2 步必须早于第 3 步：先否定"研究对象"，再要求"方法自我描述"。
    第 25 轮之前的实现把"摘要出现 >=2 个方法学标记"当作**充分条件**，
    44 篇非植物论文里因此有 13 篇被误判为"方法可迁移"而绕过非植物闸门
    （CYP1A1 驱动肺癌、Prdm15 造血干细胞稳态、podocytopathies 单细胞图谱…）。
    方法学标记描述的是**手段**，不能反推研究**对象**是方法。

    刻意**不**把"标题含动物主体词"作为否决项：`A deep learning framework
    for single-cell atlas integration of mouse brain` 是合法的方法论文
    （鼠脑只是演示数据），对象纯度由 verdict=nonplant + 正向方法信号
    共同把关；再加动物否决会把这类真方法论文误杀。

    2026-11-02 三次迭代的反例：
      * 只看"有无方法学标记" -> "Curcuma 纳米囊泡水凝胶修复软骨"（hydrogel
        这类材料学词）被放行；
      * 改成"摘要任意位置出现临床词即否决"后反向误杀：edgeR
        (10.1093/nar/gks042) 摘要举例提到 carcinoma/tumour/patients，
        SCALEX (10.1038/s41467-022-33758-z) 提到 patient，两篇通用算法论文
        被整篇归档。方法学论文拿临床数据集做基准是常态。
      * 定稿：临床词只在**标题**出现才否决；摘要层不再一票否决，但要求
        "无具体物种 + >=2 个方法学标记"，仍能挡住"某植物提取物治病"。
    """
    joined = ' '.join(list(themes) + list(tags)).lower()
    if 'methods-tools' in joined:
        return True
    text = text or ''
    title = title or ''

    # ── 否决项：标题点名研究对象，就不是"方法本身"的论文 ──────────
    if CLINICAL_OBJECT.search(title):
        return False
    # 物种否决只看标题：方法学论文在摘要里跨物种演示是常态。
    # 反例 movAPA（10.1093/bioinformatics/btaa997）摘要提了一句 mouse、
    # 演示用 rice，按"全文含物种即否决"被整篇 drop；而"Curcuma 纳米囊泡
    # 水凝胶修复创面"的物种写在标题里，仍会被正确否决。
    if _hits(CONCRETE_SPECIES, title):
        return False

    # ── 正向项：标题必须自我描述为方法/工具 ────────────────────────
    if title_is_technique(title):
        return True
    if METHOD_NOUN_TITLE.search(title):
        return len(_hits(METHOD_MARKERS, text)) >= 2
    return False


# ── 概念页解析 ───────────────────────────────────────────────────
def clean_abstract(content):
    """正文摘要，明确排除 `## 深度提炼` 元数据块。

    早期实现取"第一个二级标题"，在这些页面上取到的是自动生成的
    `## 深度提炼`（含 **物种** 等占位/污染值），把它当成摘要喂给领域判定，
    会把柑橘论文判成拟南芥、把图注误标带进分类。
    """
    for head in ("摘要", "Abstract"):
        m = re.search(r"^##\s*%s\s*\n(.+?)(?=\n##|\Z)" % head, content, re.S | re.M)
        if m:
            body = m.group(1).strip()
            return '' if body in ('—', '-', '–') else body
    return ''


def page_title(content, fallback=''):
    """概念页标题：优先一级标题，其次 front-matter。两处必须同源。

    2026-11-02 的分歧根因之一：概念页写盘的标题在 `# ` 一级标题，
    而 load_paper_organism 读的是 front-matter 的 `title:`。
    当 front-matter 仍是 DOI 占位符时，同一篇论文在导入层与主题层
    会得到不同判定。这里统一为"一级标题优先，占位符则退回 front-matter"。
    """
    m = re.search(r'^#\s+(.+?)\s*$', content, re.M)
    head = m.group(1).strip() if m else ''
    if head and not re.fullmatch(r'10\.\d{4,}/\S+', head):
        return head
    m = re.search(r'^title:\s*"?(.*?)"?\s*$', content, re.M)
    fm = m.group(1).strip() if m else ''
    if fm and not re.fullmatch(r'10\.\d{4,}/\S+', fm):
        return fm
    return head or fm or fallback


def page_fields(content):
    """从概念页一次性取出判定所需的全部字段。"""
    def front_list(key):
        m = re.search(r'^%s:\s*\[(.*?)\]' % key, content, re.M)
        return [x.strip().strip('"\'') for x in m.group(1).split(',') if x.strip()] if m else []

    doi = ''
    m = re.search(r'^doi:\s*"?(10\.\d{4,}/\S+?)"?\s*$', content, re.M)
    if m:
        doi = m.group(1).rstrip('/').lower()

    journal = ''
    m = re.search(r'^\s*-\s*\*\*期刊\*\*:\s*(.+?)$', content, re.M)
    if m:
        journal = m.group(1).strip()

    species = []
    m = re.search(r'^\*\*物种\*\*:\s*(.+?)$', content, re.M)
    if m:
        species = [s.strip() for s in m.group(1).split(',') if s.strip()]

    scope_status = ''
    m = re.search(r'^scope_status:\s*"?([^\s"\n]+)', content, re.M)
    if m:
        scope_status = m.group(1).strip()

    # 文献类型（2026-11-03）：更正/撤稿/社论/目录页等不进入证据池。
    # 缺省 research；判定模块见 article_kind.py（唯一规则来源）。
    try:
        from article_kind import kind_of
    except Exception:
        kind_of = None
    article_kind = kind_of(content) if kind_of else 'research'

    return {'doi': doi, 'title': page_title(content, doi),
            'abstract': clean_abstract(content), 'journal': journal,
            'species': species, 'scope_status': scope_status,
            'article_kind': article_kind,
            'themes': front_list('themes'), 'tags': front_list('tags')}

def import_decision(title, abstract='', journal='', species=(), themes=(), tags=()):
    """导入层裁决，返回 (action, reasons)。

    action:
      'keep'         正常导入（plant / unknown）
      'keep-methods' 非植物，但方法可迁移 -> 只写入 methods-tools 用途
      'drop'         非植物研究对象 -> 不生成证据对象
    reasons 供审计落盘（`_review/nonplant_rejected_<date>.tsv`），逐条可复核。
    """
    verdict, reasons = page_verdict(title, abstract, journal, species, themes, tags)
    if verdict != 'nonplant':
        return 'keep', reasons
    if is_method_paper(title + ' ' + abstract, themes, tags, title):
        return 'keep-methods', reasons + ['method-transferable']
    return 'drop', reasons


def paper_scope_table(concepts_dir):
    """DOI -> {'label','method','species','title'} 缓存。

    输入统一为"一级标题 + 摘要"（page_title / clean_abstract），
    因此导入层与主题层对同一篇论文必然得到同一结论 —— 这是 2026-11-02
    两套判定器一致率只有 51/97 的根因修复。
    """
    table = {}
    if not os.path.isdir(concepts_dir):
        return table
    for fname in os.listdir(concepts_dir):
        if not fname.endswith('.md'):
            continue
        try:
            with open(os.path.join(concepts_dir, fname), encoding='utf-8',
                      errors='replace') as fh:
                content = fh.read()
        except OSError:
            continue
        f = page_fields(content)
        if not f['doi']:
            continue
        text = f['title'] + ' ' + f['abstract']
        verdict, _ = page_verdict(f['title'], f['abstract'], f['journal'],
                                 f['species'], f['themes'], f['tags'])
        method = is_method_paper(text, f['themes'], f['tags'], f['title'])
        # 显式排除标记优先于启发式判定：人工/离线扫描已经判定非植物，
        # 下游必须消费这个结论，否则 191 页打标只是装饰。
        if f.get('scope_status') == 'excluded-nonplant':
            table[f['doi']] = {
                'label': 'nonplant', 'method': method,
                'scope_status': 'excluded-nonplant',
                'article_kind': f.get('article_kind', 'research'),
                'species': f['species'], 'title': f['title'],
                'journal': f['journal'],
            }
            continue
        rec = {'label': verdict, 'method': method,
               'scope_status': f.get('scope_status', ''),
               'article_kind': f.get('article_kind', 'research'),
               'species': f['species'], 'title': f['title'],
               'journal': f['journal']}
        # 同一 DOI 多份概念页时，"非 unknown"的结论优先（不被空摘要页覆盖）
        if verdict != 'unknown' or f['doi'] not in table:
            table[f['doi']] = rec
    return table


def evidence_verdict(ev, scope=None):
    """单条证据的领域判定（主题层兜底），返回 (verdict, reason)。

    论文级能判定就直接用论文级结论；判不了（多为通用方法学论文）
    才退回证据级保守判定：命中 >=2 个动物词、或标题命中动物词，
    且没有任何具体物种自证 —— 语义与 2026-11-02 主题层实现完全一致。
    verdict 另含 'methods'：论文对象非植物但方法可迁移，只允许进入
    methods-tools 主题。
    """
    doi = (ev.get('doi') or '').lower()
    rec = (scope or {}).get(doi)
    if rec:
        # 0) 文献类型闸门（2026-11-03）：更正/撤稿/社论/勘误/目录页/会议纪要
        #    不是研究证据。放在最前面，因为它与"研究对象是否植物"正交：
        #    一篇植物学 Corrigendum 既不是植物证据，也不是非植物证据。
        _kind = rec.get('article_kind') or 'research'
        if _kind not in ('research', 'review'):
            return 'nonarticle', 'article-kind=%s' % _kind
        if rec.get('scope_status') == 'excluded-nonplant':
            if rec.get('method'):
                return 'methods', 'paper-scope-excluded-method'
            return 'nonplant', 'paper-scope-excluded'
        # 判定顺序（2026-11-02 第 24 轮定稿，顺序有语义，勿调换）：
        #   1) 论文级确认是植物 -> 植物研究。
        #      不因"标题像技术论文"或"概念页带 methods-tools 标签"被剥夺
        #      生物学归属。反例：单细胞类证据页普遍带 methods-tools 标签，
        #      若 methods 判在前面，single-cell 主题会从 174 条骤降到 90 条（实测）。
        #   2) 非植物 + 方法可迁移 -> 'methods'，只允许进 methods-tools。
        #   3) 非植物 -> 'nonplant'。
        #   4) unknown -> 落到下面的证据级兜底，**不得**直接判 'methods'。
        #      unknown 的含义是"标题+摘要没写清物种"，不等于"非植物"。
        #      反例：ijms23094497《Single-cell sequencing in plant research》
        #      是植物综述，只因标题无物种被判 unknown；若把 unknown+method
        #      直接判 methods，它会被踢出 single-cell 主题，而假说层却保留，
        #      两层再次分叉（实测 123 vs 174，51 条差）。
        if rec['label'] == 'plant':
            return 'plant', 'paper-plant'
        if rec['label'] == 'nonplant':
            if rec.get('method'):
                return 'methods', 'paper-method-transferable'
            return 'nonplant', 'paper-nonplant'
    text = (ev.get('title') or '') + ' ' + (ev.get('claim') or '')
    # 证据级兜底用"研究对象强标记"，不用宽表 ANIMAL_TERMS。
    # 宽表里的 cortex / brain / neuron 在植物文献里同样高频
    # （root cortex、vascular cortex、neuronal-like 描述），
    # 而论文级判不了时（多为摘要为空的方法学论文），
    # 用宽表会把整批"根皮层单细胞"证据误杀 —— 实测 single-cell
    # 主题从 218 条掉到 171 条，属于明显过杀。
    hits = _hits(ANIMAL_SUBJECT, text)
    if not hits:
        return 'unknown', ''
    sp = (ev.get('primary_species') or '').strip()
    specifics = [x for x in (ev.get('species') or []) if x not in GENERIC_SPECIES]
    # 2026-11-03：物种字段是 deep_curate 按提及位置加权的产物，存在跨页污染
    # （实测：Nat Rev Genet《Integrative single-cell analysis》被标成
    # Citrus spp./Pisum sativum）。因此"物种自证"必须能在本条证据的
    # 标题+断言原文中找到属名，否则不予采信。
    low = text.lower()
    def _supported(name):
        genus = re.split(r'[\s.(]', (name or '').strip())[0].lower()
        return bool(genus) and genus in low
    if (sp not in GENERIC_SPECIES and _supported(sp)) or any(_supported(x) for x in specifics):
        return 'plant', 'species-field-supported'
    if (sp not in GENERIC_SPECIES) or specifics:
        return 'nonplant', 'species-field-unverified+evidence=' + ','.join(hits[:3])
    return 'nonplant', 'evidence=' + ','.join(hits[:3])

# ────────────────────────── 主题层唯一判定（2026-11-03）──────────────────────────
# 背景：batch_synthesis / batch_hypotheses / rebuild_synthesis_body 各自实现了一份
# "这条证据能不能进这个主题"的判断，规则细节略有出入，导致同一主题在三处给出
# 不同证据数（实测 methods-tools 80 vs 81；此前 84 vs 83）。差异全部来自
# 边界情形：非植物但方法可迁移的论文、勘误/撤稿页。
# 现在只保留这一份判定，三个消费方一律调用它。
def evidence_in_theme(ev, theme_id, scope=None):
    """返回 (ok, verdict, reason)。

    ok=True 表示该证据可作为 theme_id 主题的研究证据（假设调用方已确认
    证据标签/关键词把该证据归入 theme_id；这里只回答"领域纯度"这一问）。

    规则（顺序有语义）：
      1. nonarticle（更正/撤稿/社论/勘误/目录页）：任何主题都不收，
         包括 methods-tools —— 勘误页没有可迁移的方法。
      2. plant：收。
      3. nonplant 且 paper.method=True 且 theme==methods-tools：收
         （方法可迁移，生物学断言仍不得进入其他主题）。
      4. nonplant：不收。
      5. methods（对象非植物但方法可迁移）：只在 methods-tools 收。
      6. unknown：收（未知不等于非植物；交给主题标签去决定归属）。
    """
    verdict, reason = evidence_verdict(ev, scope)
    if verdict == 'nonarticle':
        return False, verdict, reason
    if verdict == 'plant':
        return True, verdict, reason
    if verdict == 'nonplant':
        if theme_id == 'methods-tools' and _paper_method(ev, scope):
            return True, 'methods', reason + '+method-transferable'
        return False, verdict, reason
    if verdict == 'methods':
        return (theme_id == 'methods-tools'), verdict, reason
    return True, verdict, reason


def _paper_method(ev, scope):
    """论文级 method 标记（概念页标 methods-tools）。"""
    doi = (ev.get('doi') or '').lower()
    rec = (scope or {}).get(doi) or {}
    return bool(rec.get('method'))
