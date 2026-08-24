title: "大规模的高性能单细胞基因调控网络推断： Inferelator 3.0。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btac117
confidence: medium
aliases: ["大规模的高性能单细胞基因调控网络推断： Inferelator 3.0。"]
status: draft
updated: "2026-05-29"

# 大规模的高性能单细胞基因调控网络推断： Inferelator 3.0。




**期刊**: 
**DOI**: [10.1093/bioinformatics/btac117](https://doi.org/10.1093/bioinformatics/btac117)
**作者**: 

## 摘要
<h4>Motivation</h4>Gene regulatory networks define regulatory relationships between transcription factors and target genes within a biological system, and reconstructing them is essential for understanding cellular growth and function. Methods for inferring and reconstructing networks from genomics data have evolved rapidly over the last decade in response to advances in sequencing technology and machine learning. The scale of data collection has increased dramatically; the largest genome-wide gene expression datasets have grown from thousands of measurements to millions of single cells, and new technologies are on the horizon to increase to tens of millions of cells and above.<h4>Results</h4>In this work, we present the Inferelator 3.0, which has been significantly updated to integrate data from distinct cell types to learn context-specific regulatory networks and aggregate them into a shared regulatory network, while retaining the functionality of the previous versions. The Inferelator is able to integrate the largest single-cell datasets and learn cell-type-specific gene regulatory networks. Compared to other network inference methods, the Inferelator learns new and informative Saccharomyces cerevisiae networks from single-cell gene expression data, measured by recovery of a known gold standard. We demonstrate its scaling capabilities by learning networks for multiple distinct neuronal and glial cell types in the developing Mus musculus brain at E18 from a large (1.3 million) single-cell gene expression dataset with paired single-cell chromatin accessibility data.<h4>Availability and implementation</h4>The inferelator software is available on GitHub (https://github.com/flatironinstitute/inferelator) under the MIT license and has been released as python packages with associated documentation (https://inferelator.readthedocs.io/).<h4>Supplementary information</h4>Supplementary data are available at Bioinformatics online.


## 全文 (PMC)

### PERMALINK

Claudia Skok Gibbs, Christopher A. Jackson and Giuseppe-Antonio Saldi contributed equally, are listed alphabetically by last name, and may be re-ordered when citing this work. To whom correspondence should be addressed.cj59@nyu.eduorrb133@nyu.edu Received 2021 May 25; Revised 2021 Dec 8; Accepted 2022 Feb 17; Collection date 2022 May 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Gene regulatory networks define regulatory relationships between transcription factors and target genes within a biological system, and reconstructing them is essential for understanding cellular growth and function. Methods for inferring and reconstructing networks from genomics data have evolved rapidly over the last decade in response to advances in sequencing technology and machine learning. The scale of data collection has increased dramatically; the largest genome-wide gene expression datasets have grown from thousands of measurements to millions of single cells, and new technologies are on the horizon to increase to tens of millions of cells and above. In this work, we present the Inferelator 3.0, which has been significantly updated to integrate data from distinct cell types to learn context-specific regulatory networks and aggregate them into a shared regulatory network, while retaining the functionality of the previous versions. The Inferelator is able to integrate the largest single-cell datasets and learn cell-type-specific gene regulatory networks. Compared to other network inference methods, the Inferelator learns new and informativeSaccharomyces cerevisiaenetworks from single-cell gene expression data, measured by recovery of a known gold standard. We demonstrate its scaling capabilities by learning networks for multiple distinct neuronal and glia

### Claudia Skok Gibbs

Claudia Skok Gibbs, Christopher A. Jackson and Giuseppe-Antonio Saldi contributed equally, are listed alphabetically by last name, and may be re-ordered when citing this work. To whom correspondence should be addressed.cj59@nyu.eduorrb133@nyu.edu Received 2021 May 25; Revised 2021 Dec 8; Accepted 2022 Feb 17; Collection date 2022 May 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### Roles

Claudia Skok Gibbs, Christopher A. Jackson and Giuseppe-Antonio Saldi contributed equally, are listed alphabetically by last name, and may be re-ordered when citing this work. To whom correspondence should be addressed.cj59@nyu.eduorrb133@nyu.edu Received 2021 May 25; Revised 2021 Dec 8; Accepted 2022 Feb 17; Collection date 2022 May 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9048651


## 深度提炼

**物种**: Oryza sativa, Citrus spp., Ficus carica
**方法**: transcriptomics (RNA-seq), single-cell RNA-seq, ATAC-seq, ChIP-seq/qPCR, knockout/mutant
**来源**: DOI:10.1093/bioinformatics/btac117
**来源类型**: PDF全文 (10.1093_bioinformatics_btac117.pdf)

### 核心发现
1. Associate Editor: Anthony Mathelier Received on May 25, 2021; revised on December 8, 2021; editorial decision on February 14, 2022; accepted on February 17, 2022 Abstract Motivation: Gene regulatory networks deﬁne regulatory relationships between transcription factors and target genes within a biological system, and reconstructing them is essential for understanding cellular growth and func- tion.
2. We show that the Inferelator 3.0 is a state-of-the-art method by testing against SCENIC and CellOracle on model organisms with reliable ground truth networks, and show that the Inferelator 3.0 can generate a mouse neuronal GRN from a publicly available dataset containing 1.3 million cells.
3. We show this by applying the Inferelator to a large (1.3 million cells of scRNAseq data), publicly available dataset of mouse brain cells (10 genomics) that is accom- panied by 15 000 single-cell ATAC (scATAC) measurements.
4. Transcriptional regulation is principally con- trolled by transcription factors (TFs) that bind to DNA and effect chromatin remodeling (Zaret, 2020) or directly modulate the output of RNA polymerases (Kadonaga, 2004).
5. Learning the true regulatory network that connects regulatory TFs to target genes is a key problem in biology (Chasman et al., 2016; Thompson et al., 2015).
6. (B) Gal4 and Gal80 regulation represented as an unsigned directed graph connecting regulatory TFs to target genes.
7. Both B.subtilis (Arrieta-Ortiz et al., 2015; Nicolas et al., 2012) and S.cerevisiae (Hackett et al., 2020; Tchourine et al., 2018) have large bulk RNA-seq and microarray gene expression datasets, in addition to a relatively large number of experimentally determined TF–target gene interactions that can be used as a gold standard for assessing network inference.
8. In these cases, using chromatin accessibility determined by a standard ATAC in combination with the known DNA-binding pref- erences for TFs to identify putative target genes is a viable alterna- tive (Miraldi et al., 2019).
## 相关文献

- [[b4-5L8yUIeARXqlhtyk-pgTZw]]
- [[b4-8J0XFUMWJe2u7rSw83Jx2w]]
- [[b5-5zHSnJtV5ZteWrZhr7-Zfg]]
- [[cotton-fiber-development-molecular-regulation]]
- [[alfalfa-anther-sc-atlas]]
- [[alfalfa-cadmium-sc-multiomics]]
- [[arabidopsis-root-regeneration-sc-multi]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC9048651

### 3 Discussion
We have developed the Inferelator 3.0 software package to scale to match the size of any network inference problem, with no organism-specific requirements that preclude easy application to non-mammalian organisms. Model baselines can be easily established by shuffling labels or generating noised datasets, and cross-validation and scoring on holdout genes is built directly into the pipeline. We believe this is particularly important as evaluation of single-cell network inference tools on real-world problems has lagged behind the development of inference methods themselves. Single-cell data collection has focused on complex higher eukaryotes and left the single-cell network inference field bereft of reliable standards to test against. Recent collection of scRNAseq data from traditional model organisms provides an opportunity to identify successful and unsuccessful strategies for network inference. For example, we find that performance differences between our methods of model selection may be smaller than differences caused by data cleaning and preprocessing. Benchmarking using model organism data should be incorporated in all single-cell method development, as it mitigates cherry-picking from complex network results and can prevent use of flawed performance metrics, which are the only option when no reliable gold standard exists. In organisms without a reliable gold standard, network inference predictions should not be assumed correct and must be validated experimentally ( Alla

### 4 Materials and methods
Additional methods available in Supplementary Methods .
4.1 Network inference in B.subtilis
Microarray expression data for B. subtilis were obtained from NCBI GEO; GSE67023 ( Arrieta-Ortiz et al. , 2015 ) ( n = 268) and GSE27219 ( Nicolas et al. , 2012 ) ( n = 266). GRNs were learned using each expression dataset separately in conjunction w