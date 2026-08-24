title: "Integrated single-nucleus and spatial transcriptomics captures transitional states in soybean nodule maturation."
pmid: "37055554"
doi: "10.1186/s13059-021-02577-8"
pmcid: "8805324"
journal: "Nature plants"
year: "2023"
authors: "Zhijian Liu, Xiangying Kong, Yanping Long, Sirui Liu, Hong Zhang"
type: paper
tags: [#single-cell-spatial, papers]
species: [Glycine max (soybean)]
methods: [scRNA-seq, spatial transcriptomics, scATAC-seq, multi-omics, RNA-seq]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

Legumes form symbiosis with rhizobium leading to the development of nitrogen-fixing nodules. By integrating single-nucleus and spatial transcriptomics, we established a cell atlas of soybean nodules and roots. In central infected zones of nodules, we found that uninfected cells specialize into functionally distinct subgroups during nodule development, and revealed a transitional subtype of infected cells with enriched nodulation-related genes. Overall, our results provide a single-cell perspecti

**研究领域**: development, gene regulation, cell type
**物种**: Glycine max (soybean)
**技术方法**: scRNA-seq, spatial transcriptomics, scATAC-seq, multi-omics, RNA-seq
**期刊**: Nature plants (2023)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明Glycine max (soybean)中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scRNA-seq, spatial transcriptomics, scATAC-seq, multi-omics, RNA-seq
- 物种系统: Glycine max (soybean)
- 实验设计: 从中推断

**关键实验体系**:
- scRNA-seq
- spatial transcriptomics
- scATAC-seq
- multi-omics
- RNA-seq

## 4. Figure-by-Figure Analysis

**Oliver Stegle**: Received 2021 Jun 14; Accepted 2021 Dec 14; Collection date 2022. Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indic
**Abstract**: Advances in multi-omics have led to an explosion of multimodal datasets to address questions from basic biology to translation. While these data provide novel opportunities for discovery, they also pose management and analysis challenges, thus motivating the development of tailored computational solutions. Here, we present a data standard and an analysis framework for multi-omics, MUON, designed t
**Background**: Multi-omics designs, that is the simultaneous profiling of multiple omics or other modalities for the same sample or cells, have recently gained traction across different biological domains. Multi-omics approaches have been applied to enable new insights in basic biology and translational research [ 1 , 2 ]. On the one hand, the emerging multi-omics datasets result in novel opportunities for advan
**Fig. 2.**: Example multi-omics analysis workflows implemented using MUON. a Construction and processing of individual modalities of a multi-omics scRNA-seq and scATAC-seq dataset. Processing steps for individual omics from left to right. Rectangles denote count matrices following each processing step, which are stored in a shared MUON data container. MUON provides processing functionalities for a wide range 
**Fig. 3.**: Single-cell multi-omics datasets processed and visualised using MUON. a MOFA factors estimated from simultaneous scRNA-seq and scATAC-seq profiling of PBMCs, with cells coloured by either left: coarse-grained cell type; or right: gene expression (in blue) and peak accessibility (in red). Displayed genes and peaks are selected to represent cell-type-specific variability along factor axes. b UMAP la
**Discussion**: Multimodal omics designs are increasingly accessible, allowing for characterising and integrating different dimensions of cellular variation, including gene expression, DNA methylation, chromatin accessibility, and protein abundance [ 3 , 40 , 41 ]. MUON directly addresses the computational needs posed by such multi-omics designs, including data processing, analysis, interpretation, and sharing (F
**Implementation of MuData**: The reference MuData implementation is written in the Python programming language and builds on AnnData [ 17 ]. A MuData object can be cast as a collection of single-omics modalities, each of which is represented as an AnnData object. Additionally, the MuData object provides basic selector operations, including access to individual modalities, subsetting of samples and/or features. When subsetting
**Comparison of MuData with alternative data formats**: *Deserialized to MAE or Seurat objects †With SeuratDisk library, in-memory Seurat objects can be constructed from parts of the data stored in HDF5 files ‡Only possible with HDF5Array library for matrices stored in external HDF5 files ††With SeuratDisk library, in-memory Seurat objects can be exported to HDF5 files ‡‡Only matrices stored in external HDF5 files, exported with HDF5Array library, can 

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-37055554-01]
- 声明: By integrating single-nucleus and spatial transcriptomics, we established a cell atlas of soybean nodules and roots
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E2** [ev-37055554-02]
- 声明: In central infected zones of nodules, we found that uninfected cells specialize into functionally distinct subgroups during nodule development, and revealed a transitional subtype of infected cells with enriched nodulation-related genes
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E3** [ev-37055554-03]
- 声明: Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the C
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E4** [ev-37055554-04]
- 声明: The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E5** [ev-37055554-05]
- 声明: While these data provide novel opportunities for discovery, they also pose management and analysis challenges, thus motivating the development of tailored computational solutions
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E6** [ev-37055554-06]
- 声明: On the one hand, the emerging multi-omics datasets result in novel opportunities for advanced analysis and biological discovery [ 3 ]
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E7** [ev-37055554-07]
- 声明: While specialised frameworks for the analysis of different omics data types have been proposed, including for bulk and single-cell RNA-seq [ 6 – 9 ] or epigenetic variation data [ 10 – 13 ], there is a lack of comprehensive solutions that specifically address multi-omics designs
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023


**E8** [ev-37055554-08]
- 声明: Shown are canonical workflows from left to right: dimensionality reduction, definition of cell neighbourhood graphs, followed by either nonlinear estimation of cell embeddings or clustering
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature plants 2023



## 6. Knowledge Graph Extraction

**实体**:
- 物种: Glycine max (soybean)
- 关键基因: HDF5, BSD3

**关系类型**:
- 调控关系: 待提取
- 功能关系: 待提取
- 比较关系: 待提取

**MeSH关键词**: Glycine max, Nitrogen Fixation, Transcriptome, Fabaceae, Plant Roots, Symbiosis

> 知识图谱需人工审查完善

## 7. Critical Evaluation

**优势**