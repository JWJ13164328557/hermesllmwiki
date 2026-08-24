title: Single-cell mRNA quantification and differential analysis with Census.
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1038/nmeth.4150
confidence: medium
aliases: ["Single-cell mRNA quantification and differential analysis with Census."]
status: draft
updated: "2026-05-29"

# Single-cell mRNA quantification and differential analysis with Census.




**期刊**: 
**DOI**: [10.1038/nmeth.4150](https://doi.org/10.1038/nmeth.4150)
**作者**: 

## 摘要
Single-cell gene expression studies promise to reveal rare cell types and cryptic states, but the high variability of single-cell RNA-seq measurements frustrates efforts to assay transcriptional differences between cells. We introduce the Census algorithm to convert relative RNA-seq expression levels into relative transcript counts without the need for experimental spike-in controls. Analyzing changes in relative transcript counts led to dramatic improvements in accuracy compared to normalized read counts and enabled new statistical tests for identifying developmentally regulated genes. Census counts can be analyzed with widely used regression techniques to reveal changes in cell-fate-dependent gene expression, splicing patterns and allelic imbalances. We reanalyzed single-cell data from several developmental and disease studies, and demonstrate that Census enabled robust analysis at multiple layers of gene regulation. Census is freely available through our updated single-cell analysis toolkit, Monocle 2.


## 全文 (PMC)

### PERMALINK

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms Single-cell gene expression studies promise to unveil rare cell types and cryptic states in development and disease through a stunningly high-resolution view of gene regulation. However, measurements from single-cell RNA-Seq are highly variable, frustrating efforts to assay how expression differs between cells. We introduce Census, an algorithm available through our single-cell analysis toolkit Monocle 2, which converts relative RNA-Seq expression levels into relative transcript counts without the need for experimental spike-in controls. We show that analyzing changes in relative transcript counts leads to dramatic improvements in accuracy compared to normalized read counts and enables new statistical tests for identifying developmentally regulated genes. We explore the power of Census through reanalysis of single-cell studies in several developmental and disease contexts. Census counts can be analyzed with widely used regression techniques to reveal changes in cell fate-dependent gene expression, splicing patterns, and allelic imbalances, demonstrating that Census enables robust single-cell analysis at multiple layers of gene regulation. Differential gene expression analysis, typically powered by statistical regression, is central to nearly all single-cell transcriptomic studies. As experiments now capture tens of thousands of cells1,2, such regressions could in principle be used to detect gene regulatory changes across individual cells as a function of developmental progression, position in an embryo, or genetic sequence. However, they report measurements with high variability, frustrating efforts to build models that can detect such changes3,4. Numerous studies have reported high rates o

### Xiaojie Qiu

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### 

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### Author Contributions

X.Q. and C.T. designed Census and the regression methods. X.Q. implemented the methods. X.Q. and A.H performed the analysis. J.P, D.L, and Y.M contributed to technical design. C.T. conceived the project. All authors wrote the manuscript. Competing Financial Interest Statement The authors declare no relevant financial interests.


**OA PDF**: https://europepmc.org/articles/pmc5330805?pdf=render


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC5330805

### Introduction
Differential gene expression analysis, typically powered by statistical regression, is central to nearly all single-cell transcriptomic studies. As experiments now capture tens of thousands of cells 1 , 2 , such regressions could in principle be used to detect gene regulatory changes across individual cells as a function of developmental progression, position in an embryo, or genetic sequence. However, they report measurements with high variability, frustrating efforts to build models that can detect such changes 3 , 4 . Numerous studies have reported high rates of “drop-out”, wherein some cells of a nominally homogeneous population express high levels of a gene and others none at all. Drop-outs have spurred the deployment of hurdle models 5 that overcome limitations over simpler regression approaches, typically at a cost in speed, numerical stability, or design flexibility for the user.
Single-cell protocols that use exogenous RNA “spike-in” standards 6 or unique molecular identifiers 7 , 8 (UMIs) enable analysis to be performed at the level of transcript counts rather than read counts. Previous work by Grun et al. suggested that comparing UMIs, rather than read counts, between cells would improve regression analysis. However, because UMI protocols work by counting 3’ end tags, they are limited to measuring gene expression and do not report expression at allele- or isoform-resolution. Spike-in-based protocols, which convert a cell’s relative abundances to transcript counts t
### Discussion
Efforts to detect changes in gene regulation in development have grappled with high technical and biological variability, demanding specialized statistical methods that explicitly model drop-outs and other nuisance variation. Here, we show that analyzing changes in relative transcript counts leads to dramatic reductions in apparent technical variability compared to normalized read counts, making single-cell RNA-Seq compatible with widely used regression techniques. We have developed Census, a normalization algorithm that can convert relative expression levels from read counts into per-cell transcript counts without the need for spike-in standards or UMIs. The algorithm requires only that genes are most frequently present at 1 cDNA molecule in each cell’s library. We show through reanalysis of several datasets that this is the case with most current protocols, owing to mRNA capture rates lower than 50% and their generation of full-length cDNAs during reverse transcription. Census cannot control for amplification biases, and thus does not produce estimates of lysate mRNA abundances that perfectly match those derived with spike-ins or UMIs. When spike-ins or UMIs are available, transcript counts should be recovered using them rather than Census. However, we show through extensive benchmarking that differential analysis results with Census counts are highly concordant with those from spike-ins. Importantly, tools widely used for bulk RNA-Seq analysis that perform poorly when prov

## 深度提炼

**物种**: Plant (unspecified)
**方法**: scRNA-seq, transcriptomics (RNA-seq), computational method
**来源**: DOI:10.1038/nmeth.4150
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (clea