title: Reversed graph embedding resolves complex single-cell trajectories.
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1038/nmeth.4402
confidence: medium
aliases: ["Reversed graph embedding resolves complex single-cell trajectories."]
status: draft
updated: "2026-05-29"

# Reversed graph embedding resolves complex single-cell trajectories.




**期刊**: 
**DOI**: [10.1038/nmeth.4402](https://doi.org/10.1038/nmeth.4402)
**作者**: 

## 摘要
Single-cell trajectories can unveil how gene regulation governs cell fate decisions. However, learning the structure of complex trajectories with multiple branches remains a challenging computational problem. We present Monocle 2, an algorithm that uses reversed graph embedding to describe multiple fate decisions in a fully unsupervised manner. We applied Monocle 2 to two studies of blood development and found that mutations in the genes encoding key lineage transcription factors divert cells to alternative fates.


## 全文 (PMC)

### PERMALINK

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms Single-cell trajectories can unveil how gene regulation governs cell fate decisions. However, learning the structure of complex trajectories with two or more branches remains a challenging computational problem. We present Monocle 2, which uses reversed graph embedding to describe multiple fate decisions in a fully unsupervised manner. Applied to two studies of blood development, Monocle 2 revealed that mutations in key lineage transcription factors diverts cells to alternative fates. Most cell state transitions, whether in development, reprogramming, or disease, are characterized by cascades of gene expression changes. We recently introduced a bioinformatics technique called “pseudotemporal ordering”, which applies machine learning to single-cell transcriptome sequencing (RNA-Seq) data to order cells by progression and reconstruct their “trajectory” as they differentiate or undergo some other type of biological transition1. Despite intense efforts to develop scalable, accurate pseudotime reconstruction algorithms (recently reviewed at2), state-of-the-art tools have several major limitations. Most pseudotime methods can only reconstruct linear trajectories, while others such as Wishbone3or DPT4support branch identification with heuristic procedures, but either are unable to identify more than one branch point in the trajectory or require that the user specify the number of branches and cell fates as an input parameter. Here, we describe Monocle 2 (Supplementary Softwareandhttps://github.com/cole-trapnell-lab/monocle-release), which applies reversed graph embedding (RGE)5,6, a recently developed machine learning strategy, to accurately reconstruct complex single-cell trajectories. Monocle 2 

### Xiaojie Qiu

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### 

Corresponding author:coletrap@uw.edu Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use:http://www.nature.com/authors/editorial_policies/license.html#terms

### Author Contributions

X.Q., Q.M., and C.T. designed and implemented Monocle 2. X.Q. performed the analysis. Y.T. and L.W. contributed to technical design. R.C. and H.P. performed testing. C.T. conceived the project. All authors wrote the manuscript. Competing Final Interests Statement The authors declare no competing financial interests. Code availability.A version of monocle 2 (version: 2.2.0) used in this study is provided asSupplementary Software. The newest Monocle 2 is available through Bioconductor as well as GitHub (https://github.com/cole-trapnell-lab/monocle-release). DDRTree, SimplePPT, SGL-tree/L1 graph are implemented in DDRTree (version: 0.1.5), simplePPT (version 0.1.0) and L1Graph (version: 0.1.0), respectively (Available (DDRTree) or will be (simplePPT, L1Graph) available from CRAN). Density peak algorithm is available fromhttps://github.com/Xiaojieqiu/densityClust/tree/knn_dp(densityClust: version 0.3). All those packages are included inSupplementary Software, which also includes a helper package, xacHelper, containing helper functions as well as all other analysis code that can be used to reproduce all figures and data in this study. Jupyter notebooks for reproducing analysis related Olsson and Paul datasets are included inSupplementary Softwaretoo. In addition, we deposited the same data athttps://github.com/cole-trapnell-lab/monocle2-rge-paper. Data availability.Four public sc RNA-seq data sets are used in this study. HSMM dataset:GSE525291; Lung dataset:GSE525837; Paul et. al dataset9:http://compgenomics.weizmann.ac.il/tanay/?pageid=649. Olsson dataset8: synapse idsyn4975060. Data for neuron simulation, results of least action paths as well as the complicate tree structure are included asSupplementary Data 1, 2, 3, respectively.


**OA PDF**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5764547


## 深度提炼

**物种**: Ficus carica
**方法**: single-cell RNA-seq, knockout/mutant
**来源**: DOI:10.1038/nmeth.4402
**来源类型**: PDF全文 (10.1038_nmeth.4402.pdf)

### 核心发现
1. Here we show that cells from mice that lack transcription factors required for estab­ lishing specific myeloid fates were diverted onto alternative fates of the same trajectory without altering its structure.
2. Thus, whereas Gfi1 and Irf8 are required for generating normal granulocytes and monocytes, other regu­ lators must contribute to activating the specific programs of these cell types.
3. Notably, f i G( ) z is optimized as one single variable instead of two separate sets of variables.
## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC5764547

### Introduction
Most cell state transitions, whether in development, reprogramming, or disease, are characterized by cascades of gene expression changes. We recently introduced a bioinformatics technique called “pseudotemporal ordering”, which applies machine learning to single-cell transcriptome sequencing (RNA-Seq) data to order cells by progression and reconstruct their “trajectory” as they differentiate or undergo some other type of biological transition 1 . Despite intense efforts to develop scalable, accurate pseudotime reconstruction algorithms (recently reviewed at 2 ), state-of-the-art tools have several major limitations. Most pseudotime methods can only reconstruct linear trajectories, while others such as Wishbone 3 or DPT 4 support branch identification with heuristic procedures, but either are unable to identify more than one branch point in the trajectory or require that the user specify the number of branches and cell fates as an input parameter.
### Results
Monocle 2 begins by identifying genes that define biological process using an unsupervised procedure we term “dpFeature”. The procedure works by selecting the genes differentially expressed between clusters of cells identified with tSNE dimension reduction followed by density peak clustering. When applied to four different datasets 1 , 7 – 9 most of the genes returned by dpFeature were also recovered by a semi-supervised selection method guided by aspects of the experimental design and were highly enriched for Gene Ontology relevant to myogenesis, confirming that dpFeature is a powerful and general unsupervised feature selection approach. ( Supplementary Figures 1–3 )
We next sought to develop a pseudotime trajectory reconstruction algorithm that does not require the number of cell fates or branches as an input parameter. To do so, we employed reversed graph embedding 5 , 6 , a machine learning technique to learn a parsimonious principal graph . Informally, a principal graph is like a principal curve 10 that passes through the “middle” of a dataset but is allowed to have branches 11 . However, learning a principal graph that describes a population of single-cell RNA-Seq profiles is very challenging because each expressed gene adds an additional dimension to the space. In general, learni