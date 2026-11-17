---

title: "oddSNP: a predictive framework for optimizing multiplexed single-cell RNA-seq experiments"
created: 2026-11-05
type: concept
tags: [papers]
themes: [single-cell-spatial-omics]
theme_status: mapped
theme_basis: keyword
doi: 10.1093/bioadv/vbag317
confidence: moderate
source: crossref
aliases:
- "oddSNP ：用于优化多重单细胞RNA-seq实验的预测框架"
---

# oddSNP: a predictive framework for optimizing multiplexed single-cell RNA-seq experiments

## 论文信息
- **期刊**: Bioinformatics Advances ()
- **DOI**: [10.1093/bioadv/vbag317](https://doi.org/10.1093/bioadv/vbag317)
- **作者**: Rodolfo S Allendes Osorio, Toshiya Nishimura, Yuichi Shigihara, Masaki Kimura, Takanori Takebe
- **来源**: crossref

## 摘要
Abstract
                  
                    Motivation
                    Donor multiplexing is a powerful strategy to increase scale, lower the costs, and reduce batch effects in single-cell RNA sequencing (scRNAseq), but clear guidelines for experimental design are lacking, forcing researchers to risk costly demultiplexing failures.
                  
                  
                    Results
                    We introduce SNP-Information Content (SNP-IC), a quantitative metric computable from simple unpooled pilot data that accurately predicts the success of genotype-based demultiplexing. Across multiple large-scale datasets using stem cell and organoid models, we establish a robust SNP-IC threshold of approximately 50, above which cells can be reliably assigned to their donor of origin. For more challenging genotype-free approaches, we define a pairwise metric, cpSNP-IC, and demonstrate a much higher requirement of approximately 3,000.
                  
                  
                    Availability and Implementation
                    Our open-source framework, oddSNP, implements this predictive model to enable in-silico titration of sequencing depth and donor complexity, allowing researchers to optimize study design before large-scale deployment, while managing costs and minimizing the risk of catastrophic data loss. oddSNP can be installed directly from PyPI and Bioconda. Source code is also freely available from GitHub at https://www.github.com/nemoto-lab/oddSNP (with release versions also available in Zenodo at DOI 10.5281/zenodo.19378022). Novel scRNAseq data used as part of this study is available at the Gene Expression Omnibus (GEO) website under accession GSE334633.
                  

## 深度提炼

**物种**: —
**来源**: crossref | DOI:10.1093/bioadv/vbag317
