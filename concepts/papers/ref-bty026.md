title: "特征特定分位数归一化使分子亚型的跨平台分类成为可能"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/bty026
confidence: medium
aliases: ["特征特定分位数归一化使分子亚型的跨平台分类成为可能"]
status: draft
updated: "2026-05-29"

# 特征特定分位数归一化使分子亚型的跨平台分类成为可能




**期刊**: 
**DOI**: [10.1093/bioinformatics/bty026](https://doi.org/10.1093/bioinformatics/bty026)
**作者**: 

## 摘要
<h4>Motivation</h4>Molecular subtypes of cancers and autoimmune disease, defined by transcriptomic profiling, have provided insight into disease pathogenesis, molecular heterogeneity and therapeutic responses. However, technical biases inherent to different gene expression profiling platforms present a unique problem when analyzing data generated from different studies. Currently, there is a lack of effective methods designed to eliminate platform-based bias. We present a method to normalize and classify RNA-seq data using machine learning classifiers trained on DNA microarray data and molecular subtypes in two datasets: breast invasive carcinoma (BRCA) and colorectal cancer (CRC).<h4>Results</h4>Multiple analyses show that feature specific quantile normalization (FSQN) successfully removes platform-based bias from RNA-seq data, regardless of feature scaling or machine learning algorithm. We achieve up to 98% accuracy for BRCA data and 97% accuracy for CRC data in assigning molecular subtypes to RNA-seq data normalized using FSQN and a support vector machine trained exclusively on DNA microarray data. We find that maximum accuracy was achieved when normalizing RNA-seq datasets that contain at least 25 samples. FSQN allows comparison of RNA-seq data to existing DNA microarray datasets. Using these techniques, we can successfully leverage information from existing gene expression data in new analyses despite different platforms used for gene expression profiling.<h4>Availability and implementation</h4>FSQN has been submitted as an R package to CRAN. All code used for this study is available on Github (https://github.com/jenniferfranks/FSQN).<h4>Contact</h4>michael.l.whitfield@dartmouth.edu.<h4>Supplementary information</h4>Supplementary data are available at Bioinformatics online.


## 全文 (PMC)

### PERMALINK

To whom correspondence should be addressed. Email:michael.l.whitfield@dartmouth.edu Received 2017 Jul 18; Revised 2018 Jan 8; Accepted 2018 Jan 16; Issue date 2018 Jun 1. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/about_us/legal/notices) Molecular subtypes of cancers and autoimmune disease, defined by transcriptomic profiling, have provided insight into disease pathogenesis, molecular heterogeneity and therapeutic responses. However, technical biases inherent to different gene expression profiling platforms present a unique problem when analyzing data generated from different studies. Currently, there is a lack of effective methods designed to eliminate platform-based bias. We present a method to normalize and classify RNA-seq data using machine learning classifiers trained on DNA microarray data and molecular subtypes in two datasets: breast invasive carcinoma (BRCA) and colorectal cancer (CRC). Multiple analyses show that feature specific quantile normalization (FSQN) successfully removes platform-based bias from RNA-seq data, regardless of feature scaling or machine learning algorithm. We achieve up to 98% accuracy for BRCA data and 97% accuracy for CRC data in assigning molecular subtypes to RNA-seq data normalized using FSQN and a support vector machine trained exclusively on DNA microarray data. We find that maximum accuracy was achieved when normalizing RNA-seq datasets that contain at least 25 samples. FSQN allows comparison of RNA-seq data to existing DNA microarray datasets. Using these techniques, we can successfully leverage information from existing gene expression data in new analyses despite different platforms used for gene expression profiling. FSQN has been submitted as an R package to CRAN. All code used for this study is available on Github (https://github.com/jenniferfranks/FSQN). Supplementary dataare available atBioinform

### Jennifer M Franks

To whom correspondence should be addressed. Email:michael.l.whitfield@dartmouth.edu Received 2017 Jul 18; Revised 2018 Jan 8; Accepted 2018 Jan 16; Issue date 2018 Jun 1. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/about_us/legal/notices)

### Roles

To whom correspondence should be addressed. Email:michael.l.whitfield@dartmouth.edu Received 2017 Jul 18; Revised 2018 Jan 8; Accepted 2018 Jan 16; Issue date 2018 Jun 1. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/about_us/legal/notices)


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/34/11/1868/25121531/bty026.pdf


## 相关文献

- [[alfalfa-cadmium-sc-multiomics]]
- [[artemisinin-scrna-glandular-trichomes]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-Gz0p6FMAVxjOjgCBDZI1Pw]]
- [[b3-Oe9xghJ07Ub3C93cYl12oQ]]
- [[b3-T3lqrTfEAP0t0_6MU5AAxA]]
- [[b3-it6oy82r7gvXVA0U03AlnA]]


## 深度提炼

**物种**: Ficus carica
**方法**: transcriptomics (RNA-seq)
**来源**: DOI:10.1093/bioinformatics/bty026
**来源类型**: PDF全文 (10.1093_bioinformatics_bty026.pdf)

### 核心发现
1. The methods we have chosen for our analyses are those that either are explicitly designed to use DNA microarray data as the target distribution (e.g.
2. 2.3 Normalization procedures For quantile normalization (QN), we utilized the normalize.quanti- les.use.target function from the preprocessCore package (Bolstad, 2016) in R with the entire microarray dataset matrix as the target distribution.
3. 2.4 Feature specific quantile normalization (FSQN) For each corresponding feature (gene), we quantile normalized log2RPKM counts from RNA-seq data using DNA microarray data as the target distribution.
4. When N ¼ number of samples in the target distribution, d is the 1 x N unit diagonal: 1ﬃﬃﬃﬃ N p ; .
5. −10 −5 0 5 10 Microarray RNA-seq Expression Value A −10 −5 0 5 10 BRCA1 CDH1 ERBB2 TP53 PTEN Expression Value B Microarray (Target Distribution) RNA-seq (LOG2) Fig.
6. For each sample size, we randomly selected samples from the RNA- seq dataset, used each normalization method to normalize the values using the full DNA microarray dataset as the target distribution, and classified the samples to assess accuracy.
7. Taken together, these results support FSQN as the most robust normalization method in our analysis.
8. Our study shows that datasets with small sample numbers and datasets with no matched samples both benefit from FSQN normalization, espe- cially when comparing to a large target distribution that contains the full spectrum of interest; in this case, all subtypes of breast inva- sive carcinoma or colorectal cancer.