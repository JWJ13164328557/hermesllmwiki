title: Doublet identification in single-cell sequencing data using <i>scDblFinder</i>.
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.12688/f1000research.73600.2
confidence: medium
aliases: ["使用scDblFinder进行单细胞测序数据中的Doublet鉴<i>定</i>。"]
aliases_extra: ["Doublet identification in single-cell sequencing data using <i>scDblFinder</i>."]
status: draft
updated: "2026-05-29"

# Doublet identification in single-cell sequencing data using <i>scDblFinder</i>.




**期刊**: 
**DOI**: [10.12688/f1000research.73600.2](https://doi.org/10.12688/f1000research.73600.2)
**作者**: 

## 摘要
Doublets are prevalent in single-cell sequencing data and can lead to artifactual findings. A number of strategies have therefore been proposed to detect them. Building on the strengths of existing approaches, we developed <i>scDblFinder</i>, a fast, flexible and accurate Bioconductor-based doublet detection method. Here we present the method, justify its design choices, demonstrate its performance on both single-cell RNA and accessibility (ATAC) sequencing data, and provide some observations on doublet formation, detection, and enrichment analysis. Even in complex datasets, <i>scDblFinder</i> can accurately identify most heterotypic doublets, and was already found by an independent benchmark to outcompete alternatives.


## 全文 (PMC)

### PERMALINK

Email:pierre-luc.germain@uzh.ch Email:mark.robinson@mls.uzh.ch No competing interests were disclosed. Accepted 2022 Apr 28; Collection date 2021. This is an open access article distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited. We worked to make all the improvements suggested by the reviewers, as well as clarifying the text (especially the methods) and figures. Major changes to the manuscript are especially to the sections on artificial doublet generation, on thresholding, and on scATAC. Regarding scATAC, we increased the number of benchmark datasets and compared to AMULET and variations of the approach. Doublets are prevalent in single-cell sequencing data and can lead to artifactual findings. A number of strategies have therefore been proposed to detect them. Building on the strengths of existing approaches, we developedscDblFinder, a fast, flexible and accurate Bioconductor-based doublet detection method. Here we present the method, justify its design choices, demonstrate its performance on both single-cell RNA and accessibility (ATAC) sequencing data, and provide some observations on doublet formation, detection, and enrichment analysis. Even in complex datasets,scDblFindercan accurately identify most heterotypic doublets, and was already found by an independent benchmark to outcompete alternatives. Keywords:single-cell sequencing, doublets, multiplets, filtering High-throughput single-cell sequencing, in particular single-cell/nucleus RNA-sequencing (scRNAseq), has provided an unprecedented resolution on biological phenomena. A particularly popular approach uses oil droplets or wells to isolate single cells along with barcoded beads. Depending on the cell density loaded, a proportion of reaction volumes (i.e. droplets or wells) will capture more than one cell, forming ‘doublets’ (or ‘multiplets’), i.e. two or more cel

### Pierre-Luc Germain

Email:pierre-luc.germain@uzh.ch Email:mark.robinson@mls.uzh.ch No competing interests were disclosed. Accepted 2022 Apr 28; Collection date 2021. This is an open access article distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### Roles

Email:pierre-luc.germain@uzh.ch Email:mark.robinson@mls.uzh.ch No competing interests were disclosed. Accepted 2022 Apr 28; Collection date 2021. This is an open access article distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

[version 2; peer review: 2 approved]

### Zev J Gartner

Competing interests:No competing interests were disclosed. This is an open access peer review report distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### Competing interests:

Competing interests:No competing interests were disclosed. This is an open access peer review report distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### Dennis Kostka

Competing interests:No competing interests were disclosed. This is an open access peer review report distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### Competing interests:

Competing interests:No competing interests were disclosed. This is an open access peer review report distributed under the terms of the Creative Commons Attribution Licence, which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.

### Pierre-Luc Germain

Competing interests:No competing interests were disclosed.

### Competing interests:

Competing interests:No competing interests were disclosed.


**OA PDF**: https://f1000research.com/articles/10-979/v2/pdf


## 深度提炼

**物种**: Plant (unspecified)
**方法**: single-cell RNA-seq, ATAC-seq
**来源**: DOI:10.12688/f1000research.73600.2
**来源类型**: PDF全文 (10.12688_f1000research.73600.2.pdf)

### 核心发现
1. We found that 2-3 iterations provided the best performance (Extended data – Figure 1B).
2. In most cases, we found the scDblFinder scores to change rapidly from high to low very close to the inflection point of the ROC curve (Figure 5A), indicating that a fixed threshold (e.g.
3. In conclusion, we believe that scDblFinder, with its flexibility, accuracy and scalability, represents a key resource for doublet detection in high-throughput single-cell sequencing data.
4. Interestingly, despite several new publications, the initial benchmark found the oldest method, DoubletFinder (McGinnis, Murrow, and Gartner 2019), to outperform others.
5. Any further responses from the reviewers can be found at the end of the article Page 3 of 26 F1000Research 2022, 10:979 Last updated: 13 NOV 2025 Results Simulation of artificial doublets As most approaches rely on some comparison of real droplets to artificial doublets, it is crucial to appropriately simulate doublets.
6. This strategy did not lead to a clear overall improvement across the datasets (Extended data – Figure 1A) over the simple sum (both of which were clearly superior to averaging), suggesting that most of the difference is anyway within the wide variability in library sizes, and/or that the normalization and dimensionality reduction steps are sufficient to remove remaining differences between real an
7. More importantly, SNPs-based labels do not include heterotypic doublets that are the result of the combination of different cell types from the same individual.
## 相关文献

- [[b3-9WavxKoXaOzbDzGmHSgUqw]]
- [[b3-BGiBJfPQalD0XaTAW6WgjQ]]
- [[b3-G2N-JJNNVwoyPpAiZEWa8w]]
- [[b3-Ke_NSLIGVqOSAUr7v-xJ6A]]
- [[b3-w-DzDSMZddBs1e1p3-Ak0A]]
- [[b3-wjlHUzpHYhRHyfMVnBq8Sg]]
- [[b3-yRRSlByPuOxXKvXBl0_LZg]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC9204188

### Abstract
Doublets are prevalent in single-cell sequencing data and can lead to artifactual findings. A number of strategies have therefore been proposed to detect them. Building on the strengths of existing
approaches, we developed
scDblFinder , a fast, flexible and accurate Bioconductor-based doublet detection method. Here we present the method, justify its design choices, demonstrate its performance on both single-cell RNA and accessibility (ATAC) sequencing data, and provide some observations on doublet formation, detection, and enrichment analysis. Even in complex datasets,
scDblFinder can accurately identify most heterotypic doublets, and was already found by an independent benchmark to outcompete alternatives.

### Introduction
High-throughput single-cell sequencing, in particular single-cell/nucleus RNA-sequencing (scRNAseq), has provided an unprecedented resolution on biological phenomena. A particularly popular approach uses oil droplets or wells to isolate single cells along with barcoded beads. Depending on the cell density loaded, a proportion of reaction volumes (i.e. droplets or wells) will capture more than one cell, forming ‘doublets’ (or ‘multiplets’), i.e. two or more cells captured by a single reaction volume and thus sequenced as a single-cell artifact. The proportion of doublets has been shown to be proportional to the number of cells captured (
et al. 2018 ). It is therefore at present common in single-cell experiments to have 10-20% doublets, making accurate doublet detection critical.
To avoid confusion, we will denote as ‘droplet’ the reads that are assigned to one barcode (either doublet or singlet), and reserve the term ‘cells’ to talk about original (singlet) cells. ‘Homotypic’ doublets, which are formed by cells of the same type (i.e. similar transcriptional state), are very difficult to identify on the basis of their transcriptome alone (
McGinnis, Murrow, and Gartner 2019 ). They are also, however, relatively in