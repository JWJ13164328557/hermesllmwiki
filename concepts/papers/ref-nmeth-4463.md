---
title: 'SCENIC: single-cell regulatory network inference and clustering.'
created: 2026-05-28
type: concept
themes: []
tags: [single-cell-spatial-omics, papers]
doi: 10.1038/nmeth.4463
confidence: medium
aliases: ['SCENIC: single-cell regulatory network inference and clustering.']
status: draft
updated: '2026-05-29'
theme_status: out-of-scope
theme_basis: purity:suspect-no-plant-cue
scope_status: excluded-nonplant
excluded_reason: "nonplant|SCENIC: single-cell regulatory network inference and clustering."
---
> [!warning] 已排除（非植物研究对象）
> 本文研究对象为动物/临床/工业体系，其生物学断言不得进入植物学主题。
> 保留本页仅为追溯 DOI 与排除理由；证据对象已归档。

# SCENIC: single-cell regulatory network inference and clustering.




**期刊**: 
**DOI**: [10.1038/nmeth.4463](https://doi.org/10.1038/nmeth.4463)
**作者**: 

## 摘要
We present SCENIC, a computational method for simultaneous gene regulatory network reconstruction and cell-state identification from single-cell RNA-seq data (http://scenic.aertslab.org). On a compendium of single-cell data from tumors and brain, we demonstrate that cis-regulatory analysis can be exploited to guide the identification of transcription factors and cell states. SCENIC provides critical biological insights into the mechanisms driving cellular heterogeneity.


## 全文 (PMC)

### PERMALINK

Correspondence to:stein.aerts@kuleuven.vib.be Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms Although single-cell RNA-seq is revolutionizing biology, data interpretation remains a challenge. We present SCENIC for the simultaneous reconstruction of gene regulatory networks and identification of cell states. We apply SCENIC to a compendium of single-cell data from tumors and brain, and demonstrate that the genomic regulatory code can be exploited to guide the identification of transcription factors and cell states. SCENIC provides critical biological insights into the mechanisms driving cellular heterogeneity. The transcriptional state of a cell emerges from an underlying gene regulatory network (GRN) in which a limited number of transcription factors and co-factors regulate each other and their downstream target genes. Recent advances in single-cell transcriptome profiling have provided exciting opportunities for a high-resolution identification of transcriptional states, and to identify trajectories of transitions between states, for example during differentiation1,2. Statistical techniques and bioinformatics methods have been optimized for single-cell RNA-seq, including methods for expression normalization, differential expression analysis, clustering, dimensionality reduction, rare cell type identification, and trajectory inference3. Although these methods have led to significant new biological insights, it is still unclear whether specific and robust GRNs underlying stable cell states can be established. This may indeed be challenging given that at the single cell level, gene expression may be partially disconnected from the dynamics of transcription factor inputs due to stochastic variation of gene expression consecutive to, for example, transcriptional bursting4. A fe

### Sara Aibar

Correspondence to:stein.aerts@kuleuven.vib.be Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### 

Correspondence to:stein.aerts@kuleuven.vib.be Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### Author contributions

SAe and SAi conceived the study; SAi implemented SCENIC and related packages with help of VA and PG for GENIE3, and GH for RcisTarget; SAi and CBG analyzed the data, with help of ZKA and HI; TM and JA implemented GRNBoost; JW performed the IHC and knock-down experiments; FR, JCM, and JvdO contributed reagents and helped with the interpretation of the melanoma analyses; SAi, JW, and SAe and wrote the manuscript. Competing financial interests The authors declare no competing financial interests.


**OA PDF**: https://lirias.kuleuven.be/bitstream/123456789/588424/1/Aibar%20BioRXIV%202017.pdf


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[xr-10-1016-j-molp-2019-04-004]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[featurecounts-an-efficient-general-purpose-program-for-assigning-seque]]
- [[moderated-estimation-of-fold-change-and-dispersion-for-rna]]



## PMC 全文

**PMC ID**: PMC5937676

### Abstract
Although single-cell RNA-seq is revolutionizing biology, data interpretation remains a challenge. We present SCENIC for the simultaneous reconstruction of gene regulatory networks and identification of cell states. We apply SCENIC to a compendium of single-cell data from tumors and brain, and demonstrate that the genomic regulatory code can be exploited to guide the identification of transcription factors and cell states. SCENIC provides critical biological insights into the mechanisms driving cellular heterogeneity.
The transcriptional state of a cell emerges from an underlying gene regulatory network (GRN) in which a limited number of transcription factors and co-factors regulate each other and their downstream target genes. Recent advances in single-cell transcriptome profiling have provided exciting opportunities for a high-resolution identification of transcriptional states, and to identify trajectories of transitions between states, for example during differentiation 1 , 2 . Statistical techniques and bioinformatics methods have been optimized for single-cell RNA-seq, including methods for expression normalization, differential expression analysis, clustering, dimensionality reduction, rare cell type identification, and trajectory inference 3 . Although these methods have led to significant new biological insights, it is still unclear whether specific and robust GRNs underlying stable cell states can be established. This may indeed be challenging given that at the singl

## 深度提炼

**物种**: Plant (unspecified)
**方法**: scRNA-seq, transcriptomics (RNA-seq), genetic perturbation, computational method
**来源**: DOI:10.1038/nmeth.4463
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (cleaned)

### 核心发现
1. The transcriptional state of a cell emerges from an underlying gene regulatory network (GRN) in which a limited number of transcription factors and co-factors regulate each other and their downstream target genes.