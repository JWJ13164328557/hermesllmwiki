title: Best practices for the execution, analysis, and data storage of plant single-cel
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1093/plcell/koae003
confidence: medium
aliases: ["Best practices for the execution, analysis, and data storage of plant single-cel"]
status: draft
updated: "2026-05-29"

# Best practices for the execution, analysis, and data storage of plant single-cel




**期刊**: 
**DOI**: [10.1093/plcell/koae003](https://doi.org/10.1093/plcell/koae003)
**作者**: 

## 摘要
Single-cell and single-nucleus RNA-sequencing technologies capture the expression of plant genes at an unprecedented resolution. Therefore, these technologies are gaining traction in plant molecular and developmental biology for elucidating the transcriptional changes across cell types in a specific tissue or organ, upon treatments, in response to biotic and abiotic stresses, or between genotypes. Despite the rapidly accelerating use of these technologies, collective and standardized experimental and analytical procedures to support the acquisition of high-quality data sets are still missing. In this commentary, we discuss common challenges associated with the use of single-cell transcriptomics in plants and propose general guidelines to improve reproducibility, quality, comparability, and interpretation and to make the data readily available to the community in this fast-developing field of research.


## 全文 (PMC)

### PERMALINK

Author for correspondence:libaultm@missouri.edu(M.T) Author for correspondence:bert.derybel@psb.vib-ugent.be(B.D.R.) The authors responsible for distribution of materials integral to the findings presented in this article in accordance with the policy described in the Instructions for Authors (https://academic.oup.com/plcell/pages/General-Instructions) are: Marc Libault (libaultm@missouri.edu) and Bert De Rybel (bert.derybel@psb.vib-ugent.be) Conflict of interest statement.None declared. Received 2023 May 2; Accepted 2023 Oct 24; Collection date 2024 Apr. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Single-cell and single-nucleus RNA-sequencing technologies capture the expression of plant genes at an unprecedented resolution. Therefore, these technologies are gaining traction in plant molecular and developmental biology for elucidating the transcriptional changes across cell types in a specific tissue or organ, upon treatments, in response to biotic and abiotic stresses, or between genotypes. Despite the rapidly accelerating use of these technologies, collective and standardized experimental and analytical procedures to support the acquisition of high-quality data sets are still missing. In this commentary, we discuss common challenges associated with the use of single-cell transcriptomics in plants and propose general guidelines to improve reproducibility, quality, comparability, and interpretation and to make the data readily available to the community in this fast-developing field of research. Plant molecular and developmental biologists are fully embracing single-cell applications. Specifically, single-cell RNA-sequencing (scRNA-seq) and single-nucleus RNA-sequencing (snRNA-seq) are gaining a lot of traction while spatial transcriptom

### Carolin Grones

Author for correspondence:libaultm@missouri.edu(M.T) Author for correspondence:bert.derybel@psb.vib-ugent.be(B.D.R.) The authors responsible for distribution of materials integral to the findings presented in this article in accordance with the policy described in the Instructions for Authors (https://academic.oup.com/plcell/pages/General-Instructions) are: Marc Libault (libaultm@missouri.edu) and Bert De Rybel (bert.derybel@psb.vib-ugent.be) Conflict of interest statement.None declared. Received 2023 May 2; Accepted 2023 Oct 24; Collection date 2024 Apr. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

Author for correspondence:libaultm@missouri.edu(M.T) Author for correspondence:bert.derybel@psb.vib-ugent.be(B.D.R.) The authors responsible for distribution of materials integral to the findings presented in this article in accordance with the policy described in the Instructions for Authors (https://academic.oup.com/plcell/pages/General-Instructions) are: Marc Libault (libaultm@missouri.edu) and Bert De Rybel (bert.derybel@psb.vib-ugent.be) Conflict of interest statement.None declared. Received 2023 May 2; Accepted 2023 Oct 24; Collection date 2024 Apr. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (https://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/plcell/advance-article-pdf/doi/10.1093/plcell/koae003/56168407/koae003.pdf


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC10980355

### Introduction: plant-specific challenges for single-cell approaches
Plant molecular and developmental biologists are fully embracing single-cell applications. Specifically, single-cell RNA-sequencing (scRNA-seq) and single-nucleus RNA-sequencing (snRNA-seq) are gaining a lot of traction while spatial transcriptomics is emerging as a promising complementary technology ( Fig. 1 ). Despite an increase in the use and publication of plant single-cell experimentation ( Fig. 1A ), it is fair to say that the plant field has, so far, not settled on common strategies, protocols, or analysis methods. Given the high complexity of the different technologies and sample types ( Fig. 1, B and C ), we feel it is important to provide a best-practice workflow and guidelines that will help in establishing a collectively accepted quality cutoff. These guidelines will aid in the evaluation of experimental approaches and computational analyses of single-cell transcriptomic data, while also offering solutions to commonly observed challenges, thereby improving the reproducibility and comparability of experiments in the broader field of plant research. The present coauthors collectively accept these guidelines and commit to applying them to their research. We also highlight examples where consensus has not yet been achieved between coauthors, which will need to be resolved when both the technologies and the field develop further. As one example, single-cell multiomics and spatial transcriptomics are, in our opinion, not established enough in the plant field to propose

## 深度提炼

**物种**: Arabidopsis thaliana, Oryza sativa, Zea mays, Solanum lycopersicum, Glycine max
**方法**: transcriptomics (RNA-seq), multi-omics integration, single-cell RNA-seq
**来源**: DOI:10.1093/plcell/koae003
**来源类型**: PDF全文 (10.1093_plcell_koae003.pdf)

### 核心发现
1. Such shallow sequencing allows evaluating the per­ formance of cell cluster analysis and annotation and is sufficient to capture the entire cell-type heterogeneity of the sample (Zhang et al.
2. Downloaded from https://academic.oup.com/plcell/article/36/4/812/7564676 by Forest Product Lab user on 01 June 2026 result, it is necessary to implement scRNA-seq-specific normal­ ization and batch correction protocols (see Luecken and Theis 2019 for a review on this specifically).