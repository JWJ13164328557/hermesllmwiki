title: "Single-nucleus transcriptomics reveal the morphogenesis and artemisinin biosynthesis in Artemisia annua glandular trichomes."
pmid: "41028755"
doi: "10.1016/j.crmeth.2023.100498"
pmcid: "PMC10326379"
journal: "Nature communications"
year: "2025"
authors: "Minghui Zhang, Mingyu Li, Yanyan An, Chang Liu, Qiaojuan Zhao"
type: paper
tags: [#single-cell-spatial, papers]
species: [unknown]
methods: [scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, GWAS, GRN, pseudotime]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

Artemisinin, the key antimalarial drug, is synthesized in Artemisia annua glandular secretory trichomes (GSTs), yet their development and artemisinin's precise cellular origins are unclear. Utilizing single-nucleus RNA sequencing and spatial transcriptomics, we construct a high-resolution cellular atlas mapping metabolic dynamics across GST development. We define three developmental states: the initiation phase, transcriptional activation of core metabolic pathways establishes fundamental cellul

**研究领域**: development, stress, hormone
**物种**: unknown
**技术方法**: scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, GWAS
**期刊**: Nature communications (2025)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明unknown中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scRNA-seq, snRNA-seq, spatial transcriptomics, RNA-seq, GWAS, GRN
- 物种系统: unknown
- 实验设计: 从中推断

**关键实验体系**:
- scRNA-seq
- snRNA-seq
- spatial transcriptomics
- RNA-seq
- GWAS
- GRN
- pseudotime

## 4. Figure-by-Figure Analysis

**Vivek Swarup**: Corresponding author vswarup@uci.edu Received 2022 Oct 5; Revised 2023 Feb 13; Accepted 2023 May 16; Collection date 2023 Jun 26. This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/).
**Summary**: Biological systems are immensely complex, organized into a multi-scale hierarchy of functional units based on tightly regulated interactions between distinct molecules, cells, organs, and organisms. While experimental methods enable transcriptome-wide measurements across millions of cells, popular bioinformatic tools do not support systems-level analysis. Here we present hdWGCNA, a comprehensive f
**Highlights**: hdWGCNA constructs co-expression networks in high-dimensional transcriptomics data hdWGCNA provides tools for statistics, visualization, and downstream interpretation hdWGCNA is an open-source R package that uses Seurat data structures hdWGCNA in human diseases demonstrates real-world analysis in complex datasets
**Motivation**: Single-cell and spatial transcriptomics assays are commonly used to profile the molecular signatures of biological systems, yielding high-dimensional datasets that can be used to model gene regulation across cell types, cell states, and spatial niches. Many statistical tools for high-dimensional transcriptomics data analysis focus on individual features rather than the underlying network structure
**Introduction**: The development and widespread adoption of single-cell and spatial genomics approaches has led to routine generation of high-dimensional datasets in a variety of biological systems. These technologies are frequently used to study developmental stages, evolutionary trajectories, disease states, drug perturbations, and other experimental conditions. Despite the inherent complexity and interconnected
**Constructing co-expression networks from high-dimensional transcriptomics data**: Here we describe hdWGCNA, a comprehensive framework for constructing and analyzing co-expression networks in high-dimensional transcriptomic data ( Figure 1 A). Given a gene expression dataset as input, co-expression network analysis typically consists of the following analysis steps: computing pairwise correlations of input features, weighting correlations with a soft-power threshold ( β ) , comp
**Figure 1.**: Overview of the hdWGCNA workflow and application in the human prefrontal cortex (A) Schematic overview of the standard hdWGCNA workflow on a scRNA-seq dataset. UMAP plot shows 36,671 cells from 11 cognitively normal donors in the Zhou et al. human prefrontal cortex (PFC) dataset. ASC, astrocytes; EX, excitatory neurons; INH, inhibitory neurons; MG, microglia; ODC, oligodendrocytes; OPC, oligodendr
**Algorithm 1. ConstructMetacells.**: Require: X such that dim ( X ) = N g , N c ⊳ gene expression matrix of N g genes and N c cells Require: D such that dim ( D ) = c , d ⊳ dimensional reduction of X , with N c cells and d dimensions Require: C ⊳ the set of unique cell barcodes K ← KNN ( D , k ) ⊳ K is a matrix of N c rows and k columns with the k nearest neighbors of each cell S ← [ ∅ ] ⊳ list containing barcodes of cells selected f

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-41028755-01]
- 声明: Single-nucleus transcriptomics reveal the morphogenesis and artemisinin biosynthesis in Artemisia annua glandular trichomes
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E2** [ev-41028755-02]
- 声明: We define three developmental states: the initiation phase, transcriptional activation of core metabolic pathways establishes fundamental cellular machinery; the intermediate phase, marked lipid metabolism activation with coordinated fatty acid and wax biosynthesis, accompanied by active photosynthe
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E3** [ev-41028755-03]
- 声明: Notably, we discover that six specific secretory cells within the 10-cell GSTs constitute the primary site for artemisinin production
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E4** [ev-41028755-04]
- 声明: We identify hundreds of hub genes potentially contributing to trichome development or artemisinin biosynthesis
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E5** [ev-41028755-05]
- 声明: Overall, this study systematically elucidates GST development and artemisinin biosynthesis, revealing its spatial production mechanism and providing essential cellular and genetic foundations for metabolic engineering and fundamental trichome biology
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E6** [ev-41028755-06]
- 声明: hdWGCNA provides functions for network inference, gene module identification, gene enrichment analysis, statistical tests, and data visualization
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E7** [ev-41028755-07]
- 声明: We showcase hdWGCNA using data from autism spectrum disorder and Alzheimer’s disease brain samples, identifying disease-relevant co-expression network modules
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025


**E8** [ev-41028755-08]
- 声明: hdWGCNA is directly compatible with Seurat, a widely used R package for single-cell and spatial transcriptomics analysis, and we demonstrate the scalability of hdWGCNA by analyzing a dataset containing nearly 1 million cells
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2025



## 6. Knowledge Graph Extraction

**实体**:
- 物种: unknown
- 关键基因: VM23, PLP1, CD34

**关系类型**:
- 调控关系: 待提取
- 功能关系: 待提取
- 比较关系: 待提取

**MeSH关键词**: Artemisia annua, Artemisinins, Trichomes, Transcriptome, Gene Expression Regulation, Plant, Cell Nucleus, Morphogenesis, Gene Expression Profiling

> 知识图谱需人工审查完善

## 7. Critical Evaluation

**优势**:
- 使用scRNA-seq, snRNA-seq, spatial transcriptomics等先进技术
- 发表于Nature communications

**局限**:
- 基于PMC全文分析，可靠性较高
- 自动分析可能遗漏关键细节
- 统计方法和重复性待人工审查

**证据质量**: 中等 (需人工评级)

## 8. Research Insight

本文的核心贡献在于:
1. 提供了unknowndevelopment的新