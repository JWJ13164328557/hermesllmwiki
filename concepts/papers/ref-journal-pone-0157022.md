title: SARTools: A DESeq2- and EdgeR-Based R Pipeline for Comprehensive Differential An
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1371/journal.pone.0157022
confidence: medium
aliases: ["SARTools: A DESeq2- and EdgeR-Based R Pipeline for Comprehensive Differential An"]
status: draft
updated: "2026-05-29"

# SARTools: A DESeq2- and EdgeR-Based R Pipeline for Comprehensive Differential An




**期刊**: 
**DOI**: [10.1371/journal.pone.0157022](https://doi.org/10.1371/journal.pone.0157022)
**作者**: 

## 摘要
<h4>Background</h4>Several R packages exist for the detection of differentially expressed genes from RNA-Seq data. The analysis process includes three main steps, namely normalization, dispersion estimation and test for differential expression. Quality control steps along this process are recommended but not mandatory, and failing to check the characteristics of the dataset may lead to spurious results. In addition, normalization methods and statistical models are not exchangeable across the packages without adequate transformations the users are often not aware of. Thus, dedicated analysis pipelines are needed to include systematic quality control steps and prevent errors from misusing the proposed methods.<h4>Results</h4>SARTools is an R pipeline for differential analysis of RNA-Seq count data. It can handle designs involving two or more conditions of a single biological factor with or without a blocking factor (such as a batch effect or a sample pairing). It is based on DESeq2 and edgeR and is composed of an R package and two R script templates (for DESeq2 and edgeR respectively). Tuning a small number of parameters and executing one of the R scripts, users have access to the full results of the analysis, including lists of differentially expressed genes and a HTML report that (i) displays diagnostic plots for quality control and model hypotheses checking and (ii) keeps track of the whole analysis process, parameter values and versions of the R packages used.<h4>Conclusions</h4>SARTools provides systematic quality controls of the dataset as well as diagnostic plots that help to tune the model parameters. It gives access to the main parameters of DESeq2 and edgeR and prevents untrained users from misusing some functionalities of both packages. By keeping track of all the parameters of the analysis process it fits the requirements of reproducible research.


## 全文 (PMC)

### PERMALINK

Competing Interests:The authors have declared that no competing interests exist. Analyzed the data: HV MAD. Contributed reagents/materials/analysis tools: HV LBG MAD. Wrote the paper: HV LBG JYC MAD. * E-mail:marie-agnes.dillies@pasteur.fr Received 2016 Apr 6; Accepted 2016 May 23; Collection date 2016. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Several R packages exist for the detection of differentially expressed genes from RNA-Seq data. The analysis process includes three main steps, namely normalization, dispersion estimation and test for differential expression. Quality control steps along this process are recommended but not mandatory, and failing to check the characteristics of the dataset may lead to spurious results. In addition, normalization methods and statistical models are not exchangeable across the packages without adequate transformations the users are often not aware of. Thus, dedicated analysis pipelines are needed to include systematic quality control steps and prevent errors from misusing the proposed methods. SARTools is an R pipeline for differential analysis of RNA-Seq count data. It can handle designs involving two or more conditions of a single biological factor with or without a blocking factor (such as a batch effect or a sample pairing). It is based on DESeq2 and edgeR and is composed of an R package and two R script templates (for DESeq2 and edgeR respectively). Tuning a small number of parameters and executing one of the R scripts, users have access to the full results of the analysis, including lists of differentially expressed genes and a HTML report that (i) displays diagnostic plots for quality control and model hypotheses checking and (ii) keeps track of the whole analysis process, parameter values and versions of the R packages used. SARTool

### Hugo Varet

Competing Interests:The authors have declared that no competing interests exist. Analyzed the data: HV MAD. Contributed reagents/materials/analysis tools: HV LBG MAD. Wrote the paper: HV LBG JYC MAD. * E-mail:marie-agnes.dillies@pasteur.fr Received 2016 Apr 6; Accepted 2016 May 23; Collection date 2016. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Competing Interests:

Competing Interests:The authors have declared that no competing interests exist. Analyzed the data: HV MAD. Contributed reagents/materials/analysis tools: HV LBG MAD. Wrote the paper: HV LBG JYC MAD. * E-mail:marie-agnes.dillies@pasteur.fr Received 2016 Apr 6; Accepted 2016 May 23; Collection date 2016. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.


**OA PDF**: https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0157022&type=printable


## 深度提炼

**物种**: Ficus carica
**方法**: transcriptomics (RNA-seq), ChIP-seq/qPCR
**来源**: DOI:10.1371/journal.pone.0157022
**来源类型**: PDF全文 (10.1371_journal.pone.0157022.pdf)

### 核心发现
1. The target file contains one row per sample and at least three columns with head- ers: a unique sample identifier or label, the name of the associated raw counts file and the sam- ple biological condition (see Table 1).
2. Finally, in the context of developing reproducible research it is essential to fully describe and explore the data and keep track of the full analysis process with the associated parameter values and software versions.
## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC4900645

### Introduction
DESeq2 [ 1 ] and edgeR [ 2 ] are very popular Bioconductor [ 3 ] packages for differential expression analysis of RNA-Seq, SAGE-Seq, ChIP-Seq or HiC count data. They are very well documented and easy-to-use, even for inexperienced R users. In recent years edgeR and a previous version of DESeq2, DESeq [ 4 ], have been included in several benchmark studies [ 5 , 6 ] and have shown to perform well in replicated experiments. However, running these packages, users can analyse their own dataset without entering important steps of the analysis process such as controlling the quality of the data, exploring its structure or checking some hypotheses of the statistical model. Although these steps are strongly recommended by the authors of the packages [ 7 ], they can be skipped by the users without stopping the analysis process.
In an attempt to provide a user friendly access to the whole analysis process of RNA-Seq data, the RNASeqGUI R package has been proposed to provide users with a graphical interface and help R beginners to run a differential analysis without writing R code [ 8 ]. The analysis is divided into six main steps among which the pre-analysis section proposes no less than 12 possible figures to explore the data. Similarly, systemPipeR is a R package that proposes a pipeline to process raw fastq RNA-Seq reads from quality filtering to the alignment and counting and to perform a differential analysis using either the edgeR or DESeq2 package [ 9 ].
Normalization is another 
### Results and Discussion
As soon as the script parameters have been given proper values, and assuming that input files fulfill the format requirements described above, the R script can be run. Using a standard desktop computer, the running time is usually lower than one minute to perform the analysis of 10 samples containing about 50 000 features each. Two types of output files are then made available:
a HTML report that describes the whole analysis process in four main steps:
data quality control : numerous plots are proposed to provide a