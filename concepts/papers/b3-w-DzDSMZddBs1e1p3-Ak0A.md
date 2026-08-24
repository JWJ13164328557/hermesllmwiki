title: "Integrating scRNA-seq and snRNA-seq with spatial transcriptomics to unlock the xylem puzzle."
pmid: "41724975"
doi: "10.1093/nar/gkae978"
pmcid: "PMC13036908"
journal: "Genome biology"
year: "2026"
authors: "Mingke Wei, Jo-Wei Allison Hsieh, Jr-Fong Dang, Botong Tong, Hui Li"
type: paper
tags: [#single-cell-spatial, papers]
species: [Arabidopsis thaliana, Populus (poplar)]
methods: [scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, RNA-FISH, machine learning]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

BACKGROUND: Xylem development is a dynamic, continuous process fundamental to secondary growth in woody plants and to biomass accumulation on earth. While single-cell RNA sequencing (scRNA-seq) enables reconstruction of early xylem differentiation trajectories, its reliance on protoplast isolation excludes late-stage cells with thickened secondary cell walls, leaving key phases such as secondary cell wall deposition and programmed cell death poorly characterized.
RESULTS: We perform single-nucle

**研究领域**: development, hormone, metabolism
**物种**: Arabidopsis thaliana, Populus (poplar)
**技术方法**: scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, RNA-FISH
**期刊**: Genome biology (2026)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明Arabidopsis thaliana中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, RNA-FISH, machine learning
- 物种系统: Arabidopsis thaliana
- 实验设计: 从中推断

**关键实验体系**:
- scRNA-seq
- snRNA-seq
- spatial transcriptomics
- RNA-seq
- RNA-FISH
- machine learning

## 4. Figure-by-Figure Analysis

**Quanzi Li**: Received 2025 May 15; Accepted 2026 Feb 10; Collection date 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the 
**Background**: In multicellular organisms, development is fundamentally a continuous and dynamic process [ 1 ]. From the earliest cell fate decisions to terminal differentiation, cells undergo gradual and coordinated transitions in gene expression, morphology, and function. Capturing these transitions with high resolution is essential for uncovering the mechanisms that drive tissue patterning, organogenesis, and
**Complementary sampling properties of protoplast-scRNAseq and SDX-snRNAseq revealed by anatomical analysis**: Building upon our previously reported scRNA-seq (protoplast-scRNAseq) datasets, we conducted SDX-snRNAseq in this study to enable direct comparative analyses between the two platforms [ 31 ]. To compare the developmental stages captured by single-cell and single-nucleus transcriptomics in xylem tissue, we first examined the sample preparation workflows underlying protoplast-scRNAseq and SDX-snRNAs
**Integration of protoplast-scRNAseq and SDX-snRNAseq datasets reveals a continuous xylem developmental trajectory**: We conducted SDX-snRNAseq on the SDX from two individual poplar trees. A total of 26,925 (13,496 in Bio1 and 13,429 in Bio2) nuclei were recovered, with ~ 26,500 genes detected (26,511 in Bio1 and 26,589 in Bio2) (Additional file 1: Fig. S1a). The numbers of the UMI (Unique molecular identifier) per nucleus obtained in the two replicates were 13,496 and 13,429, respectively (Additional file 1: Fig
**Fig. 2.**: Integrated analysis of xylem single-cell and single-nucleus transcriptomes. a Density overlay of two biological replicates ( n = 2) in single-nucleus RNA sequencing (SDX-snRNAseq), demonstrating high reproducibility across xylem cell populations. Densities from 0 to 1 are divided into 500 bins with different color shading, with proportions of different densities shown in a pie chart in each panel.
**Identification of the SCW deposition zone captured by SDX-snRNAseq**: Given that SDX-snRNAseq preferentially captures thick-walled, late-stage xylem cells, we next sought to investigate how the protoplast-scRNAseq–defined libriform fiber, vessel element, and ray parenchyma cell types further develop at later stages. Specifically, we asked which downstream cell states these early-identified clusters transition into, as revealed by the extended coverage of SDX-snRNAse
**Transcriptomic signature of SCW deposition and onset of programmed cell death**: To gain further biological insights into the cells within the SCW deposition region, we identified the genes that were differentially expressed in this population and subsequently performed Gene Ontology (GO) enrichment analysis. By integrating LCM RNAseq and SDX-snRNAseq data through correlation analysis, we annotated the subpopulations in the SDX-snRNAseq dataset and identified two distinct clus
**Fig. 5.**: Expression of cell-type-specific genes in clusters associated with identified early and late developmental stages. a Twelve cell clusters, 1 to 12, were obtained through unsupervised K -means clustering and visualized by UMAP. 1-V, vessel element. 2-FuIP, fusiform intermediate precursor. 3-RO, ray organizer. 4-FuEP, fusiform early precursor. 5-RP, ray precursor. 6-FuO, fusiform organizer. 7-F, lib

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-41724975-01]
- 声明: While single-cell RNA sequencing (scRNA-seq) enables reconstruction of early xylem differentiation trajectories, its reliance on protoplast isolation excludes late-stage cells with thickened secondary cell walls, leaving key phases such as secondary cell wall deposition and programmed cell death poo
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E2** [ev-41724975-02]
- 声明: Anatomical validation confirms that scRNA-seq profiles predominantly represent early-stage stem-developing xylem, while snRNA-seq enriches for deeper, secondary cell wall depositing layers
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E3** [ev-41724975-03]
- 声明: Integrated analysis reveals a spatially and transcriptionally defined secondary cell wall zone, supported by both lignin autofluorescence and its correlation with laser capture microdissection-derived transcriptomes
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E4** [ev-41724975-04]
- 声明: Differential expression and gene ontology analyses uncover enrichment for lignin biosynthesis and programmed cell death associated genes, suggesting that secondary cell wall formation and programmed cell death initiation are transcriptionally coordinated
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E5** [ev-41724975-05]
- 声明: Unsupervised clustering and machine learning by support vector machine classification further reveal greater transcriptomic heterogeneity among early-stage xylem cells compared to late-stage cells
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E6** [ev-41724975-06]
- 声明: CONCLUSIONS: Our findings demonstrate the high compatibility and complementarity of scRNA-seq and snRNA-seq platforms
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E7** [ev-41724975-07]
- 声明: Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and 
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Genome biology 2026


**E8** [ev-41724975-08]
- 声明: The images or other third party material in this article are inclu