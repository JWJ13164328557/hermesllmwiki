title: "WUSCHEL-dependent chromatin regulation in maize inflorescence development at single-cell resolution."
pmid: "41039501"
doi: "10.1093/bioinformatics/btp352"
pmcid: "PMC12492591"
journal: "Genome biology"
year: "2025"
authors: "Sohyun Bang, Xuan Zhang, Jason Gregory, Ziliang Luo, Zongliang Chen"
type: paper
tags: [#single-cell-spatial, papers]
species: [Arabidopsis thaliana, Zea mays (maize)]
methods: [scATAC-seq, ChIP-seq, RNA-seq, ChIP-qPCR, EMSA]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

BACKGROUND: WUSCHEL (WUS) is a homeodomain transcription factor vital for stem cell proliferation in plant meristems. In maize, ZmWUS1 is expressed in the inflorescence meristem, including the central zone reservoir of stem cells. ZmWUS1 overexpression in the Barren inflorescence3 (Bif3) mutant perturbs inflorescence development due to stem cell over-proliferation.
RESULTS: Single-cell Assay for Transposase Accessible Chromatin sequencing (scATAC-seq) shows that Bif3 alters central zone chromati

**研究领域**: development, hormone, signaling
**物种**: Arabidopsis thaliana, Zea mays (maize)
**技术方法**: scATAC-seq, ChIP-seq, RNA-seq, ChIP-qPCR, EMSA
**期刊**: Genome biology (2025)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明Arabidopsis thaliana中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scATAC-seq, ChIP-seq, RNA-seq, ChIP-qPCR, EMSA
- 物种系统: Arabidopsis thaliana
- 实验设计: 从中推断

**关键实验体系**:
- scATAC-seq
- ChIP-seq
- RNA-seq
- ChIP-qPCR
- EMSA

## 4. Figure-by-Figure Analysis

**Robert J Schmitz**: Received 2025 Feb 4; Accepted 2025 Sep 15; Collection date 2025. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the C
**Background**: In maize, similar to Arabidopsis, a functional homolog of CLV3 , ZmCLE7 , is implicated in the regulation of inflorescence stem cell proliferation [ 14 ]. Diminished ZmCLE7 expression increases kernel count, producing kernels that are narrower and less round, whereas ZmCLE7 upregulation lowers kernel yield in ears [ 15 ]. In Arabidopsis, CLV3 is expressed in the three uppermost cell layers, L1, L2
**scATAC-seq captures central zone nuclei in the immature maize ear**: We hypothesized that Bif3 ZmWUS1 overexpression alters cis- regulatory element activity, and the accessible chromatin landscape, with ZmWUS1 binding cis -regulatory elements that are not targeted in WT. To assess this, we compared the chromatin accessibility landscape across cell types by performing scATAC-seq, with two biological replicates, on developing WT and Bif3 female inflorescences. After 
**Fig. 1.**: Unlike Arabidopsis WUS, which has organizing center exclusive expression [ 38 ], the expression domain of ZmWUS1 (Zm00001eb067310) in maize female inflorescence spans a broader area than the organizing center [ 11 ], covering multiple cell layers 1 through 10 across the meristem (Fig. 1 B). Further distinguishing maize from Arabidopsis, the inflorescence central zone stem cells, which express the 
**Intergenic chromatin accessibility specifically differs in the Bif3 central zone**: To understand the differences in Accessible Chromatin Regions (ACRs) that underlie the meristem morphological variation, we identified cell-type-level differential ACRs between WT and Bif3 . Using the union of all ACRs identified from each cell type, the total number of ACRs was 91,386 in WT and 77,393 in Bif3 (Additional file 2: Table S5), each spanning 500 bp from the peak summit. In WT, approxi
**Regions with increased chromatin accessibility in Bif3 were enriched for the CAATAATGC motif**: To uncover TFs potentially involved in the Bif3 altered chromatin accessibility landscape, we identified enriched motifs using a de novo motif search in differential ACRs with increased and decreased central zone cell accessibility in Bif3 compared to WT samples. The increases in Bif3 ACRs were enriched for a single significant motif (CAATAATGC), whereas the decreases in Bif3 ACRs showed enrichmen
**Fig. 3.**: Characteristics of differentially Accessible Chromatin Regions (differential ACRs) between WT and Bif3 by cell types. A The Position Weight Matrix (PWM) illustrates significant motifs discovered within differential ACRs in the central zone (E-value &lt; 1). The ratio indicates the number of differential ACRs containing the motif divided by the total number of differential ACRs. The color denotes w
**Accessible chromatin regions with decreased accessibility due to overexpressed ZmWUS1 are associated with ARFs**: We next examined ACRs with decreased central zone chromatin accessibility in Bif3 vs WT female inflorescence; these ACRs were associated with five different motifs: GCACAGCAGC, GCAGCATGC, CGCGCCGCGCC, GCTAGCTAGC, and AG repeats (Fig. 3 A). The multiple motifs present in the decreased ACR set suggest that distinct TF families may be active in the Bif3 central zone, each recognizing their specific m

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-41039501-01]
- 声明: RESULTS: Single-cell Assay for Transposase Accessible Chromatin sequencing (scATAC-seq) shows that Bif3 alters central zone chromatin accessibility compared to normal inflorescence meristems
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E2** [ev-41039501-02]
- 声明: The CAATAATGC motif, a known homeodomain recognition site, is enriched within regions with increased chromatin accessibility in Bif3, suggesting ZmWUS1 could function as a transcriptional activator in the central zone
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E3** [ev-41039501-03]
- 声明: This motif differs from the TGAATGAA motif identified by DNA Affinity Purification sequencing (DAP-seq) of ZmWUS1, which showed low enrichment in the central zone
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E4** [ev-41039501-04]
- 声明: Conversely, regions with decreased chromatin accessibility in Bif3 are instead adjacent to AUXIN RESPONSE FACTOR genes, suggesting possible reduced auxin signaling in the Bif3 central zone
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E5** [ev-41039501-05]
- 声明: CONCLUSIONS: This study characterized how Bif3 overexpression of ZmWUS1 influences chromatin accessibility in the central zone, reducing auxin signaling, while raising questions about differential ZmWUS1 motif usage in distinct cellular contexts
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E6** [ev-41039501-06]
- 声明: Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and 
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E7** [ev-41039501-07]
- 声明: The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2025


**E8** [ev-41039501-08]
- 声明: However, CLV3 is not co-expressed with WUS in the organizing center, and some have suggested that the WUS transcriptional regulation may vary by cellular context; in the central zone, WUS promotes CLV3 expression, but in the organizing center, it could repress CLV3 [ 20 ]
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)