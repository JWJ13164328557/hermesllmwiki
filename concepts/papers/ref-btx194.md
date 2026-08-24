title: "SCODE ：一种来自单细胞RNA-Seq的有效调控网络推断算法，在不同的"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btx194
confidence: medium
aliases: ["SCODE ：一种来自单细胞RNA-Seq的有效调控网络推断算法，在不同的"]
status: draft
updated: "2026-05-29"

# SCODE ：一种来自单细胞RNA-Seq的有效调控网络推断算法，在不同的




**期刊**: 
**DOI**: [10.1093/bioinformatics/btx194](https://doi.org/10.1093/bioinformatics/btx194)
**作者**: 

## 摘要
<h4>Motivation</h4>The analysis of RNA-Seq data from individual differentiating cells enables us to reconstruct the differentiation process and the degree of differentiation (in pseudo-time) of each cell. Such analyses can reveal detailed expression dynamics and functional relationships for differentiation. To further elucidate differentiation processes, more insight into gene regulatory networks is required. The pseudo-time can be regarded as time information and, therefore, single-cell RNA-Seq data are time-course data with high time resolution. Although time-course data are useful for inferring networks, conventional inference algorithms for such data suffer from high time complexity when the number of samples and genes is large. Therefore, a novel algorithm is necessary to infer networks from single-cell RNA-Seq during differentiation.<h4>Results</h4>In this study, we developed the novel and efficient algorithm SCODE to infer regulatory networks, based on ordinary differential equations. We applied SCODE to three single-cell RNA-Seq datasets and confirmed that SCODE can reconstruct observed expression dynamics. We evaluated SCODE by comparing its inferred networks with use of a DNaseI-footprint based network. The performance of SCODE was best for two of the datasets and nearly best for the remaining dataset. We also compared the runtimes and showed that the runtimes for SCODE are significantly shorter than for alternatives. Thus, our algorithm provides a promising approach for further single-cell differentiation analyses.<h4>Availability and implementation</h4>The R source code of SCODE is available at https://github.com/hmatsu1226/SCODE.<h4>Contact</h4>hirotaka.matsumoto@riken.jp.<h4>Supplementary information</h4>Supplementary data are available at Bioinformatics online.



**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/33/15/2314/25158052/btx194.pdf


## 相关文献

- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b4-0Ai2UdSwKz-GbYdfit26vw]]
- [[b4-78WuUWiztOxRe4n5MS2Pag]]
- [[b4-ZKYanCM-ZalgHteLOaJErw]]
- [[b4-_dqlLGuPZxhNXXs6caCEwg]]
- [[b4-ys8H9kH4cFVbPEuMHCg4nA]]
- [[b5-bYBJQMR-CaDgOnXivhTmGQ]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC5860123

### 1 Introduction
Conventional bulk RNA-Seq reveals the average gene expression of an ensemble of cells, and therefore does not permit the analysis of detailed states of individual cells. With the advancement of single-cell RNA-Seq (scRNA-Seq), we can now quantify the expression of individual cells and analyze detailed differences among cells ( Kolodziejczyk et al. , 2015 ). This enables several analyses such as the identification of cell types ( Buettner et al. , 2015 ; Zeisel et al. , 2015 ), especially of rare cells ( Grun et al. , 2015 ; Jiang et al. , 2016 ) and the estimation of cellular lineages ( Burns, 2015 ; Treutlein et al. , 2014 ).
In analyses by scRNA-Seq, the reconstruction of cellular differentiation processes attracts attention as a novel approach to revealing differentiation mechanisms ( Trapnell, 2015 ). The differentiation process can be reconstructed using dimension reduction ( Ji and Ji, 2016 ; Trapnell et al. , 2014 ) and stochastic processes ( Matsumoto and Kiryu, 2016 ), for example, and the degree of differentiation (in pseudo-time) of each cell is characterized by the position in the reconstructed process. By investigating the expression pattern in pseudo-time, genes can be clustered into multiple groups with different biological functions ( Trapnell et al. , 2014 ). Moreover, the regulatory cascade of cellular state transitions, such as differentiation, can be inferred by comparing the timings of up- and down-regulation ( Eckersley-Maslin et al. , 2016 ; Li et al. ,

### 3 Results
3.1 Selection of the size of z ( D ) and reproducibility of A
Our model was overfitted to the training data, and the inferred A was unstable with needlessly large D . Additionally, the model cannot reconstruct expression dynamics with insufficiently small values of D . Therefore, the selection of appropriate values for D is necessary, and we applied SCODE to training data and evaluated the validity of the optimized model on the basis of the RSS of independent test data for various values of D ( D = 2, 4, 6 and 8). For each D , we executed SCODE 100 times independently, and the first, second and third quantiles of the RSS values of test data are shown in Figure 2(a) . For every dataset, the median of RSS is almost saturated at D = 4.

### 4 Discussion
The advancement of scRNA-Seq and the analysis of differentiation reconstruction and pseudo-time have elucidated differentiation mechanisms. The inference of regulatory networks associated with differentiation is necessary to further our understanding of differentiation and development. In the inference of regulatory networks, it is important to fully use pseudo-time information and expression dynamics. However, there are no efficient algorithms for inferring the regulatory networks of many TFs from continuous time expression data. Thus, we developed SCODE, an efficient algorithm based on linear ODEs. SCODE is based on the transformation of linear ODEs and linear regression, and the time complexity is significantly small.
We applied SCODE to three scRNA-Seq datasets during differentiation and showed that SCODE can successfully optimize ODEs so that these ODEs can reconstruct observed expression dynamics. In the validation of the inferred network, the AUC values of SCODE were higher than those of other methods in almost of all cases. The runtime of SCODE is significantly smaller than that of Jump3, which also infers networks from time-course data. Additionally, SCODE is faster than GENIE3, which does not use time information. These performance results show the efficiency of SCODE.
Single-cell sequencing technologies are developing rapidly, and the number of scRNA-Seq datasets produced from differentiating cells will therefore increase. Our novel and efficient method for inferri

## 深度提炼

**物种**: Plant (unspecified)
**方法**: scRNA-seq, transcriptomics (RNA-seq), computational method
**来源**: DOI:10.1093/bioinformatics/btx194
**来源类型**: PMC全文
**基因**: —

### 核心发现
1. Therefore, a novel algorithm is necessary to infer networks from single-cell RNA-Seq during differentiation.<h4>Results</h4>In this study, we developed the novel and efficient algorithm SCODE to infer regulatory networks, based on ordinary differential equations.