title: "Cellular Heterogeneity and Developmental Dynamics of Aril in Papaya."
pmid: "42123537"
doi: "10.1038/nmeth.4150"
pmcid: "PMC5330805"
journal: "International journal of molecular sciences"
year: "2026"
authors: "Jin Shi, Yuxin Wang, Ruirong Hu, Yujie Fang, Wen Wang"
type: paper
tags: [#single-cell-spatial, papers]
species: [unknown]
methods: [scRNA-seq, multi-omics, RNA-seq, pseudotime]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

The papaya aril is a specialized seed appendage that has been reported to contain germination-inhibiting substances and usually requires removal before seed germination, thereby limiting breeding efficiency. However, the cellular origin and candidate molecular regulators of papaya aril development remain poorly understood. To investigate the early developmental process and candidate regulatory genes of the papaya aril, we combined histological analysis, bulk RNA-seq, and single-cell RNA-seq. His

**研究领域**: development, signaling, gene regulation
**物种**: unknown
**技术方法**: scRNA-seq, multi-omics, RNA-seq, pseudotime
**期刊**: International journal of molecular sciences (2026)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明unknown中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scRNA-seq, multi-omics, RNA-seq, pseudotime
- 物种系统: unknown
- 实验设计: 从中推断

**关键实验体系**:
- scRNA-seq
- multi-omics
- RNA-seq
- pseudotime

## 4. Figure-by-Figure Analysis

**Cole Trapnell**: Corresponding author: coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#terms
**Introduction**: Differential gene expression analysis, typically powered by statistical regression, is central to nearly all single-cell transcriptomic studies. As experiments now capture tens of thousands of cells 1 , 2 , such regressions could in principle be used to detect gene regulatory changes across individual cells as a function of developmental progression, position in an embryo, or genetic sequence. How
**Estimating relative transcript counts in spike-in-free experiments**: Census exploits two properties of single-cell RNA-Seq datasets produced with current protocols ( Figure 1a ). First, mRNA degradation following cell lysis and inefficiencies in the reverse transcription reaction result in the capture of as few as 10% of the transcripts in a cell as cDNA. Second, most protocols rely on template-switching reverse transcriptases primed at the polyA tail of mRNAs and 
**Census counts improve differential analysis accuracy**: We next assessed whether using Census counts improved downstream differential analysis. We tested several popular tools 16 , 17 for differential expression with both read counts and relative transcript counts, including two tools specifically developed for single-cell data, Monocle 18 , and SCDE 19 ( Figure 2a , Supplementary Figure 5 ). When provided with read counts as a measure of expression, c
**Differential analysis of branch points in developmental trajectories reveals regulators of cell fate**: Many single-cell gene expression studies aim to identify gene regulatory circuits that control cell-fate decisions made during development 20 , 21 . We recently developed Monocle, an algorithm that organizes single cells along trajectories and can describe the gene expression changes executed during cell differentiation. Monocle introduced the concept of “pseudotime”, which quantifies each cell’s 
**Disruption of interferon signaling induces a branch in the dendritic cell LPS stimulation trajectory**: Branch points in single-cell trajectories represent steps in a program of transcriptional change in which cells must choose between one of several mutually exclusive gene expression programs. Branches could arise not only during development, but also in response to mutations, treatment with drugs, or other cellular perturbations. We reanalyzed a recent study 36 from Shalek and colleagues, which di
**Census counts enable single-cell differential splicing analysis**: Methods for detecting splicing changes in single-cell RNA-Seq experiments are beginning to appear, but have grappled with isoform-level measurement variability. For example, Welch et al. described SingleSplice 41 , which uses a hurdle model to compare observed variation in isoform frequencies against expected technical variation, but its contrasts are limited to tests for excess variability within
**Census counts enable allelic balance analysis in single cells**: Single-cell analysis could in principle shed light on the degree to which the two alleles of each gene are regulated in a coordinated manner. Recently, Deng et al. tracked gene expression genome wide in single-cells from pre-implantation mouse embryos of mixed genetic background (CAST/EiJ × C57BL/6J) 45 . Coupling allele-level relative abundances from Kallisto 46 with Census produced relative alle

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-42123537-01]
- 声明: Histological observations suggested that aril differentiation begins around 10 days after pollination (DAP) in the funiculus region
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E2** [ev-42123537-02]
- 声明: Based on this initiation stage, bulk RNA-seq profiling of seeds at 5, 10, and 15 DAP identified genes with initiation-stage-specific expression and prioritized candidate genes potentially related to seed appendage development, including CpRING-like, CpMBR2, and CpNDR8
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E3** [ev-42123537-03]
- 声明: Single-cell RNA-seq of seeds at 10 and 15 DAP annotated a putative aril cell population and reconstructed its developmental trajectory, revealing five trajectory-associated genes: CpATJ3, CpDYL1, CpGRP-like, CpHIRD11, and CpERD15
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E4** [ev-42123537-04]
- 声明: Integrative analysis of bulk and single-cell transcriptomic datasets further identified three candidate genes potentially involved in aril development: CpFER3, CpUVI4, and CpCEP1
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E5** [ev-42123537-05]
- 声明: These findings support the funiculus region as the likely anatomical origin of the papaya aril and provide candidate genes for future functional validation
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E6** [ev-42123537-06]
- 声明: Single-cell protocols that use exogenous RNA “spike-in” standards 6 or unique molecular identifiers 7 , 8 (UMIs) enable analysis to be performed at the level of transcript counts rather than read counts
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E7** [ev-42123537-07]
- 声明: suggested that comparing UMIs, rather than read counts, between cells would improve regression analysis
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026


**E8** [ev-42123537-08]
- 声明: Tools designed for bulk RNA-Seq analysis, such as DESeq2 17 , produce false discovery rates as high as 61%
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: International journal of molecular sciences 2026



## 6. Knowledge Graph Extraction

**实体**:
- 物种: unknown
- 关键基因: ACTA2, AT1, ACTA1, AT2, TPM1

**关系类型**:
- 调控关系: 待提取
- 功能关系: 待提取
- 比较关系: 待提取

**MeSH关键词**: Carica, Fruit, Gene Regulatory Networks, Genes, Plant, Single-Cel