"""subtopic_vocab.py — 主题内的子主题词表（唯一来源，供 synthesis 正文重建使用）。

设计原则
  1. 子主题是"研究问题域"，不是标签；因此用关键词/短语匹配证据正文，
     而不是复用 evidence 的 tags（tags 只有主题级粒度）；
  2. 每个主题 6–8 个子主题，必须能覆盖该主题典型问题域，且互斥性足够高
     —— 一条证据可命中多个子主题，重建时按"最强命中"归入首个；
  3. 词表只用于**分组与检索**，不产生任何生物学断言；正文所有断言均来自
     证据页原文摘录，并附证据页链接。
"""
from __future__ import annotations

import re

VOCAB = {
    "single-cell-spatial-omics": [
        ("图集构建与细胞类型注释",
         r"(cell ?type|cell-type|cluster|annotat|atlas|cell identity|marker gene|cell population)"),
        ("空间转录组与位置映射",
         r"(spatial transcriptom|spatial omic|visium|stereo-?seq|merfish|smfish|in situ|spatially resolved|positional)"),
        ("发育轨迹与拟时序推断",
         r"(trajector|pseudotime|rna velocity|lineage|differentiation path|monocle|slingshot)"),
        ("技术平台与建库方法",
         r"(10x|drop-?seq|protoplast|nuclei isolation|snrna|snatac|scrna-?seq protocol|microfluidic|combinatorial indexing)"),
        ("细胞类型特异性胁迫与免疫响应",
         r"(stress response|heat stress|salt stress|immune|defen[cs]e|pathogen|cell-type-specific response)"),
        ("细胞间通讯与信号推断",
         r"(cell[- ]cell communication|ligand[- ]receptor|cellchat|intercellular signaling)"),
        ("多组学整合与调控网络",
         r"(multi-?omic|integrative|chromatin accessibility|regulatory network|gene regulatory)"),
    ],
    "developmental-biology": [
        ("分生组织维持与干细胞稳态",
         r"(meristem|stem cell|wuschel|\bwus\b|clavata|organ initiation|shoot apex|root apical)"),
        ("细胞分裂与细胞周期",
         r"(cell cycle|mitosis|cyclin|cdk|cytokinesis|division plane|endoreduplication)"),
        ("细胞命运决定与分化",
         r"(cell fate|differentiat|identity|lineage commitment|asymmetric division)"),
        ("器官发生与形态建成",
         r"(organogenesis|morphogenesis|leaf (shape|development)|root (growth|patterning)|flower development|trichome)"),
        ("激素与发育信号整合",
         r"(auxin|cytokinin|gibberellin|brassinosteroid|abscisic|ethylene|jasmon|strigolactone)"),
        ("表观调控与发育可塑性",
         r"(epigenetic|chromatin|histone|dna methylation|polycomb|plasticity|phase transition)"),
        ("再生与愈伤组织形成",
         r"(regeneration|callus|de novo shoot|somatic embryogenesis|adventitious root)"),
    ],
    "metabolism-natural-products": [
        ("次生代谢物生物合成途径",
         r"(biosynthesis|biosynthetic pathway|secondary metabol|alkaloid|terpenoid|flavonoid|phenylpropanoid)"),
        ("转录调控与代谢工程",
         r"(transcription factor|myb|bhlh|wrky|metabolic engineering|heterologous expression)"),
        ("代谢物运输与储存",
         r"(transporter|transport|vacuolar|sequestration|accumulation)"),
        ("品质形成与营养成分",
         r"(quality|nutrition|vitamin|anthocyanin|sugar|oil content|starch)"),
        ("酶学与催化机制",
         r"(enzyme|enzymatic|catalytic|kinetic|substrate specificity|in vitro assay)"),
        ("多组学解析代谢网络",
         r"(metabolom|multi-?omic|flux|network reconstruction|co-?expression)"),
        ("逆境代谢重编程",
         r"(stress-induced metabol|elicitor|wound|jasmonate-induced|defence metabol)"),
    ],
    "hormone-signaling": [
        ("受体感知与早期信号转导",
         r"(receptor|perception|ligand|kinase cascade|phosphorylation|early signaling)"),
        ("转录调控与激素响应基因",
         r"(transcription factor|response element|aux\/iaa|arf|bzip|myb|transcriptional regulation)"),
        ("激素合成与稳态",
         r"(biosynthesis|homeostasis|conjugation|catabolism|precursor|transport of hormone)"),
        ("激素间互作与权衡",
         r"(crosstalk|interaction between|antagonis|synerg|balance between|integration of)"),
        ("生长发育中的激素功能",
         r"(root growth|shoot growth|senescence|fruit ripening|seed germination|organ size)"),
        ("逆境中的激素调控",
         r"(drought|salt|cold|heat|stress response|abiotic stress|defen[cs]e)"),
        ("信号转导的定量与动态特征",
         r"(gradient|dynamics|dose|threshold|spatiotemporal|feedback)"),
    ],
    "stress-immunity": [
        ("病原识别与免疫受体",
         r"(pattern recognition|receptor|rlk|nlr|r gene|effector|pamp|mamp)"),
        ("免疫信号传导与活性氧",
         r"(ros|reactive oxygen|mapk|calcium signal|salicylic|jasmonic|ethylene signal)"),
        ("抗病基因与数量抗性",
         r"(resistance gene|qtl|quantitative resistance|broad-spectrum|rps|rpm)"),
        ("非生物逆境响应",
         r"(drought|salt|heat|cold|osmotic|abiotic stress|tolerance)"),
        ("激素与免疫的权衡",
         r"(trade-?off|growth[- ]defen[cs]e|crosstalk|priming|systemic acquired)"),
        ("微生物组与根际互作",
         r"(microbiome|rhizosphere|mycorrhiz|symbio|endophyte|microbiota)"),
        ("逆境记忆与表观调控",
         r"(priming|memory|epigenetic|chromatin|stress recall)"),
    ],
    "epigenetics-gene-regulation": [
        ("DNA 甲基化与去甲基化",
         r"(dna methylation|methylome|demethyl|cmt|met1|ros1|5mc)"),
        ("组蛋白修饰与染色质状态",
         r"(histone|h3k4|h3k27|h3k9|acetylation|methylation of histone|chromatin state)"),
        ("染色质重塑与三维构象",
         r"(remodeler|chromatin remodel|hic|tdna|3d genome|loop|topolog)"),
        ("非编码 RNA 与转录沉默",
         r"(small rna|mirna|sirna|lncrna|rnai|transposon silencing|argonaute)"),
        ("转录因子与顺式调控元件",
         r"(transcription factor|cis-element|promoter|enhancer|binding site|chip-?seq)"),
        ("表观遗传与发育/逆境可塑性",
         r"(development|differentiation|stress|plasticity|vernalization|imprinting)"),
        ("表观编辑与工程化改造",
         r"(epigenome editing|crispr|dcas9|targeted methylation|synthetic)"),
    ],
    "methods-tools": [
        ("测序与文库构建",
         r"(sequencing|library prep|long-read|nanopore|pacbio|hi-?c library|rna-?seq protocol)"),
        ("成像与空间定位技术",
         r"(imaging|microscop|confocal|super-?resolution|live imaging|fish)"),
        ("基因编辑与遗传转化",
         r"(crispr|cas9|base editing|transformation|agrobacterium|protoplast transformation)"),
        ("计算工具与数据整合",
         r"(algorithm|pipeline|software|toolkit|benchmark|workflow|machine learning|deep learning)"),
        ("单细胞与组学方法",
         r"(single-?cell|spatial|multi-?omic|atac|proteomic|metabolomic method)"),
        ("表型组与高通量筛选",
         r"(phenotyp|high-?throughput|screen|image-based|robot)"),
        ("数据库与知识资源",
         r"(database|repository|portal|resource|web server|knowledge base)"),
    ],
    "genomics-evolution": [
        ("基因组组装与注释",
         r"(genome assembly|annotation|telomere-to-telomere|t2t|haplotype|gap-free)"),
        ("比较基因组与共线性",
         r"(comparative genomic|synteny|collinear|ortholog|paralog|gene family evolution)"),
        ("群体遗传与选择信号",
         r"(population genomic|gwas|selection|domestication|snp|haplotype block|diversity)"),
        ("多倍化与亚基因组演化",
         r"(polyploid|allopolyploid|subgenome|whole-genome duplication|wgd|diploidization)"),
        ("转座子与基因组可塑性",
         r"(transposon|te|retrotransposon|genome size|rearrangement|structural variation)"),
        ("进化发育与性状起源",
         r"(evo-?devo|origin of|evolution of|adaptive|convergent|phylogen)"),
        ("泛基因组与作物改良",
         r"(pangenome|pan-genome|resequencing|breeding|germplasm|core collection)"),
    ],
}


def subtopics(theme_id):
    return VOCAB.get(theme_id, [])


def assign(text, theme_id):
    """返回命中的子主题名列表（按词表顺序，保持稳定）。"""
    t = text or ""
    hits = []
    for name, pat in subtopics(theme_id):
        if re.search(pat, t, re.I):
            hits.append(name)
    return hits
