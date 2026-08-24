title: "scDAPA ：从单细胞RNA-seq检测和可视化动态替代多聚腺苷酸化"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btz701
confidence: medium
aliases: ["scDAPA ：从单细胞RNA-seq检测和可视化动态替代多聚腺苷酸化"]
status: draft
updated: "2026-05-29"

# scDAPA ：从单细胞RNA-seq检测和可视化动态替代多聚腺苷酸化




**期刊**: 
**DOI**: [10.1093/bioinformatics/btz701](https://doi.org/10.1093/bioinformatics/btz701)
**作者**: 

## 摘要
<h4>Motivation</h4>Alternative polyadenylation (APA) plays a key post-transcriptional regulatory role in mRNA stability and functions in eukaryotes. Single cell RNA-seq (scRNA-seq) is a powerful tool to discover cellular heterogeneity at gene expression level. Given 3' enriched strategy in library construction, the most commonly used scRNA-seq protocol-10× Genomics enables us to improve the study resolution of APA to the single cell level. However, currently there is no computational tool available for investigating APA profiles from scRNA-seq data.<h4>Results</h4>Here, we present a package scDAPA for detecting and visualizing dynamic APA from scRNA-seq data. Taking bam/sam files and cell cluster labels as inputs, scDAPA detects APA dynamics using a histogram-based method and the Wilcoxon rank-sum test, and visualizes candidate genes with dynamic APA. Benchmarking results demonstrated that scDAPA can effectively identify genes with dynamic APA among different cell groups from scRNA-seq data.<h4>Availability and implementation</h4>The scDAPA package is implemented in Shell and R, and is freely available at https://scdapa.sourceforge.io.<h4>Supplementary information</h4>Supplementary data are available at Bioinformatics online.


## 全文 (PMC)

### PERMALINK

Congting Ye and Qian Zhou wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. To whom correspondence should be addressed.yec@xmu.edu.cn Received 2019 Jun 22; Revised 2019 Jul 23; Accepted 2019 Sep 4; Collection date 2020 Feb 15. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model) Alternative polyadenylation (APA) plays a key post-transcriptional regulatory role in mRNA stability and functions in eukaryotes. Single cell RNA-seq (scRNA-seq) is a powerful tool to discover cellular heterogeneity at gene expression level. Given 3′ enriched strategy in library construction, the most commonly used scRNA-seq protocol—10× Genomics enables us to improve the study resolution of APA to the single cell level. However, currently there is no computational tool available for investigating APA profiles from scRNA-seq data. Here, we present a package scDAPA for detecting and visualizing dynamic APA from scRNA-seq data. Taking bam/sam files and cell cluster labels as inputs, scDAPA detects APA dynamics using a histogram-based method and the Wilcoxon rank-sum test, and visualizes candidate genes with dynamic APA. Benchmarking results demonstrated that scDAPA can effectively identify genes with dynamic APA among different cell groups from scRNA-seq data. The scDAPA package is implemented in Shell and R, and is freely available athttps://scdapa.sourceforge.io. Supplementary dataare available atBioinformaticsonline. Alternative polyadenylation (APA) is increasingly recognized as an important regulation mechanism for many biological processes (e.g. cell development, differentiation and proliferation) and molecular functions (e.g. mRNA stability, translation efficiency and localization) via dynamically using different polyadenylation sites during maturation of

### Congting Ye

Congting Ye and Qian Zhou wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. To whom correspondence should be addressed.yec@xmu.edu.cn Received 2019 Jun 22; Revised 2019 Jul 23; Accepted 2019 Sep 4; Collection date 2020 Feb 15. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model)

### Roles

Congting Ye and Qian Zhou wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. To whom correspondence should be addressed.yec@xmu.edu.cn Received 2019 Jun 22; Revised 2019 Jul 23; Accepted 2019 Sep 4; Collection date 2020 Feb 15. This article is published and distributed under the terms of the Oxford University Press, Standard Journals Publication Model (https://academic.oup.com/journals/pages/open_access/funder_policies/chorus/standard_publication_model)


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/36/4/1262/38712506/btz701.pdf


## 相关文献

- [[alfalfa-anther-sc-atlas]]
- [[alfalfa-cadmium-sc-multiomics]]
- [[andrographis-msi-sc-spatial]]
- [[arabidopsis-root-regeneration-sc-multi]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]


## 深度提炼

**来源**: 知识库文献
