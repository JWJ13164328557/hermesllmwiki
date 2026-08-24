title: "Cell-type-specific immune programs orchestrate spatial defense in the Arabidopsis leaf epidermis."
pmid: "41864960"
doi: "10.1038/s41586-019-0969-x"
pmcid: "PMC6434952"
journal: "Nature communications"
year: "2026"
authors: "Jingpu Song, Mahsa Modareszadeh, Dinithi Kumarapeli, Wilson Andres Acosta, Yuhai Cui"
type: paper
tags: [#single-cell-spatial, papers]
species: [Arabidopsis thaliana]
methods: [scRNA-seq, RNA-seq, reporter assay, RNA-FISH, pseudotime]
status: curated
curation_depth: PMC全文
updated: 2026-05-30

## 1. Scientific Context

Sessile plants rely on individual cells to perceive pathogens and coordinate defense. Guard cells (GCs), best known for regulating stomatal aperture, have poorly understood intrinsic immune roles. Here, we integrate single-cell and spatial analyses of Arabidopsis thaliana leaves infected with diverse phytopathogens, combining live and fixed imaging of transgenic immune reporters with single cell transcriptomic data. Powdery mildew infection triggers strong salicylic acid (SA) biosynthesis and tr

**研究领域**: development, stress, hormone
**物种**: Arabidopsis thaliana
**技术方法**: scRNA-seq, RNA-seq, reporter assay, RNA-FISH, pseudotime
**期刊**: Nature communications (2026)

## 2. Research Questions

基于摘要和全文分析，本文主要关注以下科学问题:

1. 阐明Arabidopsis thaliana中development的分子机制
2. 鉴定关键调控因子并验证其功能
3. 整合多组学数据揭示调控网络

> ⚠️ 注: 本节基于自动分析生成，需人工审查补充具体研究问题

## 3. Experimental Logic

**研究策略**:
- 核心方法: scRNA-seq, RNA-seq, reporter assay, RNA-FISH, pseudotime
- 物种系统: Arabidopsis thaliana
- 实验设计: 从中推断

**关键实验体系**:
- scRNA-seq
- RNA-seq
- reporter assay
- RNA-FISH
- pseudotime

## 4. Figure-by-Figure Analysis

**Jay Shendure**: Author Contributions J.C. developed techniques and performed sci-RNA-seq3 experiments with assistance from M.S., F.Z., L.C., F.S.; M.S. performed embryo collection and in-situ hybridization validations with assistance from D.I. and S.M.; J.C. and C.T. performed computation analysis with assistance from M.S., X.Q. and A.H.; X.Q. and C.T. developed Monocle 3. X.H. developed website with assistance f
**Main**: Most studies of mammalian organogenesis rely on model organisms, and in particular, the mouse. Mice develop quickly, with just 21 days between fertilization and birth. The implantation of the blastocyst (E4.0) is followed by gastrulation and the formation of germ layers (E6.5-E7.5) 1 , 2 . At the early-somite stages, the embryo transits from gastrulation to early organogenesis, forming the neural 
**Single cell RNA-seq of 2 million cells**: Single cell combinatorial indexing (‘sci-’) is a methodological framework involving split-pool barcoding of cells or nuclei 12 – 19 . We previously developed sci-RNA-seq and applied it to generate 50-fold shotgun coverage of the cellular content of L2 stage Caenorhabditis elegans 17 . A conceptually identical method was recently termed Split-Seq 20 . To increase the throughput, we explored &gt;1,0
**Fig. 1. sci-RNA-seq3 enables profiling of 2,072,011 cells from 61 mouse embryos across 5 developmental stages in a single experiment.**: ( a ) sci-RNA-seq3 workflow and experimental scheme. ( b ) Bar plot showing number of cells profiled from each of 61 mouse embryos. ( c ) Pseudotime trajectory of pseudobulk RNA-seq profiles of mouse embryos. From one experiment, we recovered 2,058,652 cells from mouse embryos and 13,359 cells from HEK293T or NIH/3T3 cells (UMI (unique molecular identifier) count ≥ 200). Transcriptomes from human/
**Identification of cell types and subtypes**: We subjected the 2,058,652 single cell transcriptomes to Louvain clustering and t-SNE visualization ( Fig. 2a ). Reassuringly, cells from replicate embryos of the same developmental stage were similarly distributed, whereas cells from different stages were not ( Extended Data Figs. 2a–f ). Based on genes specific to each of 40 clusters, we manually annotated cell types ( Supplementary Table 2 ). M
**Fig. 2. Identifying the major cell types of mouse organogenesis.**: ( a ) t-SNE visualization of 2,026,641 mouse embryo cells, colored by cluster id from Louvain clustering (in Fig. 2b), and annotated based on marker genes. The same t-SNE is plotted below, showing only cells from each stage (cell numbers from left to right: n = 151,000 for E9.5; 370,279 for E10.5; 602,784 for E11.5; 468,088 for E12.5; 434,490 for E13.5). Primitive erythroid (transient) and definit
**Characterization of the apical ectodermal ridge**: We annotated all subtypes of epithelium and endothelium (clusters 6 and 20, respectively; Fig. 3a ; Extended Data Fig. 6a–c ; Supplementary Table 2 ). For example, epithelial subtype 6.8 was marked by Oc90 , exclusively expressed in the epithelium of the otic vesicle 33 ; epithelial subtype 6.23 by Fgf8, Msx2 . and Rspo2 , known markers of the apical ectodermal ridge (AER) 34 ; and endothelial sub
**Fig. 3. Identification and characterization of epithelial cell subtypes and the limb apical ectodermal ridge (AER).**: ( a ) t-SNE visualization and marker-based annotation of epithelial cell subtypes (74,651 cells). ( b ) t-SNE visualization of all epithelial cells colored by expression level of Fgf8 . “High” indicates cells with UMI count for Fgf8 &gt; 1. ( c ) In situ hybridization images of Fgf8 in embryos from E9.5 to E13.5. Arrow: site of gene expression. n = 5 ( d, e ) t-SNE visualization of all epithelial 

> 注: 图表-段落对应关系需人工审查

## 5. Evidence Extraction

以下为自动提取的核心声明 (需人工审查确认):


**E1** [ev-41864960-01]
- 声明: Together, these findings uncover distinct immune programs among epidermal cell types, highlight GC-autonomous defense mechanisms, and provide a framework for understanding spatial immune coordination in plants
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E2** [ev-41864960-02]
- 声明: performed embryo collection and in-situ hybridization validations with assistance from D.I
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E3** [ev-41864960-03]
- 声明: Nuclei from each embryo were isolated and deposited to different wells, such that the first index identified the originating embryo of any given cell
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E4** [ev-41864960-04]
- 声明: ( b ) Bar plot showing number of cells profiled from each of 61 mouse embryos
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E5** [ev-41864960-05]
- 声明: From one experiment, we recovered 2,058,652 cells from mouse embryos and 13,359 cells from HEK293T or NIH/3T3 cells (UMI (unique molecular identifier) count ≥ 200)
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E6** [ev-41864960-06]
- 声明: The same t-SNE is plotted below, showing only cells from each stage (cell numbers from left to right: n = 151,000 for E9.5; 370,279 for E10.5; 602,784 for E11.5; 468,088 for E12.5; 434,490 for E13.5)
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E7** [ev-41864960-07]
- 声明: ( b ) Dot plot showing expression of one selected marker gene per cell type
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026


**E8** [ev-41864960-08]
- 声明: Amongst these, we identified 2,863 cell type-specific marker genes (mean 75; those with &gt;2-fold expression difference between first and second ranked cell type; a cutoff of &gt;5-fold yielded 932 marker genes; Extended Data Fig
- 证据类型: 转录组 / 遗传 / 生化 (需审查确认)
- 证据强度: 中等 (自动分析，需人工评级)
- 来源: Nature communications 2026



## 6. Knowledge Graph Extraction

**实体**:
- 物种: Arabidopsis thaliana
- 关键基因: TDE1, VM11

**关系类型**:
- 调控关系: 待提取
- 功能关系: 待提取
- 比较关系: 待提取

**MeSH关键词**: Arabidopsis, Plant Leaves, Colletotrichum, Plant Diseases, Pseudomonas syringae, Plant Epidermis, Salicylic Acid, Gene Expression Regulation, Plant

> 知识图谱需人工审查完善

## 7. Critical 