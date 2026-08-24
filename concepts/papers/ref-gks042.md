title: Differential expression analysis of multifactor RNA-Seq experiments with respect
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/nar/gks042
confidence: medium
aliases: ["Differential expression analysis of multifactor RNA-Seq experiments with respect"]
status: draft
updated: "2026-05-29"

# Differential expression analysis of multifactor RNA-Seq experiments with respect




**期刊**: 
**DOI**: [10.1093/nar/gks042](https://doi.org/10.1093/nar/gks042)
**作者**: 

## 摘要
A flexible statistical framework is developed for the analysis of read counts from RNA-Seq gene expression studies. It provides the ability to analyse complex experiments involving multiple treatment conditions and blocking variables while still taking full account of biological variation. Biological variation between RNA samples is estimated separately from the technical variation associated with sequencing technologies. Novel empirical Bayes methods allow each gene to have its own specific variability, even when there are relatively few biological replicates from which to estimate such variability. The pipeline is implemented in the edgeR package of the Bioconductor project. A case study analysis of carcinoma data demonstrates the ability of generalized linear model methods (GLMs) to detect differential expression in a paired design, and even to detect tumour-specific expression changes. The case study demonstrates the need to allow for gene-specific variability, rather than assuming a common dispersion across genes or a fixed relationship between abundance and variability. Genewise dispersions de-prioritize genes with inconsistent results and allow the main analysis to focus on changes that are consistent between biological replicates. Parallel computational approaches are developed to make non-linear model fitting faster and more reliable, making the application of GLMs to genomic data more convenient and practical. Simulations demonstrate the ability of adjusted profile likelihood estimators to return accurate estimators of biological variability in complex situations. When variation is gene-specific, empirical Bayes estimators provide an advantageous compromise between the extremes of assuming common dispersion or separate genewise dispersion. The methods developed here can also be applied to count data arising from DNA-Seq applications, including ChIP-Seq for epigenetic marks and DNA methylation analyses.


## 全文 (PMC)

### PERMALINK

*To whom correspondence should be addressed. Tel: +61 3 9345 2555; Fax: +61 3 9347 0852; Email:smyth@wehi.edu.au The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Received 2011 Aug 12; Revised 2012 Jan 5; Accepted 2012 Jan 10; Issue date 2012 May; Collection date 2012 May. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited. A flexible statistical framework is developed for the analysis of read counts from RNA-Seq gene expression studies. It provides the ability to analyse complex experiments involving multiple treatment conditions and blocking variables while still taking full account of biological variation. Biological variation between RNA samples is estimated separately from the technical variation associated with sequencing technologies. Novel empirical Bayes methods allow each gene to have its own specific variability, even when there are relatively few biological replicates from which to estimate such variability. The pipeline is implemented in the edgeR package of the Bioconductor project. A case study analysis of carcinoma data demonstrates the ability of generalized linear model methods (GLMs) to detect differential expression in a paired design, and even to detect tumour-specific expression changes. The case study demonstrates the need to allow for gene-specific variability, rather than assuming a common dispersion across genes or a fixed relationship between abundance and variability. Genewise dispersions de-prioritize genes with inconsistent results and allow the main analysis to focus on changes that are consistent between biological replicates. Parallel computational approaches are developed to make non-linear model fitting faster an

### Davis J McCarthy

*To whom correspondence should be addressed. Tel: +61 3 9345 2555; Fax: +61 3 9347 0852; Email:smyth@wehi.edu.au The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Received 2011 Aug 12; Revised 2012 Jan 5; Accepted 2012 Jan 10; Issue date 2012 May; Collection date 2012 May. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

*To whom correspondence should be addressed. Tel: +61 3 9345 2555; Fax: +61 3 9347 0852; Email:smyth@wehi.edu.au The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Received 2011 Aug 12; Revised 2012 Jan 5; Accepted 2012 Jan 10; Issue date 2012 May; Collection date 2012 May. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/3.0), which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/nar/article-pdf/40/10/4288/25335174/gks042.pdf


## 深度提炼

**物种**: Plant (unspecified)
**方法**: transcriptomics (RNA-seq), ChIP-seq/qPCR, qRT-PCR validation
**来源**: DOI:10.1093/nar/gks042
**来源类型**: PDF全文 (10.1093_nar_gks042.pdf)

### 核心发现
1. BCV is therefore likely to be the dominant source of uncertainty for high-count genes, so reliable estimation of BCV is crucial for realistic assess- ment of differential expression in RNA-Seq experiments.
2. When less replication is available, sharing information between genes is essential for reliable inference.
## 相关文献

- [[arabidopsis-root-sc-atlas-review]]
- [[b3-Ke_NSLIGVqOSAUr7v-xJ6A]]
- [[b3-MweGEIei1VoObhk3boSJog]]
- [[b3-peg1lwq2yaEXfDY9yfqzZg]]
- [[b3-w-DzDSMZddBs1e1p3-Ak0A]]
- [[b3-wjlHUzpHYhRHyfMVnBq8Sg]]
- [[b4-0Ai2UdSwKz-GbYdfit26vw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC3378882

### INTRODUCTION
The cost of DNA sequencing continues to decrease at a staggering rate ( 1 ). As it does, sequencing technologies become more and more attractive as platforms for studying gene expression. Current ‘next-generation’ sequencing technologies measure gene expression by generating short reads or sequence tags, that is, sequences of 35–300 base pairs that correspond to fragments of the original RNA. There are a number of technologies and many different protocols. Popular approaches are either tag-based methods including Tag-Seq ( 2 ), deepSAGE ( 3 ), SAGE-Seq ( 4 ), which sequence from one or more anchored positions in each gene, or RNA-Seq ( 5 – 8 ), which sequences random fragments from the entire transcriptome. Both approaches have proven successful in investigating gene expression and regulation ( 9 – 11 ). In this article, we will use the term RNA-Seq generically to include any of the tag-based or RNA-Seq variants in which very high-throughput sequencing is applied to RNA fragments.
For the purposes of evaluating differential expression between conditions, read counts are summarized at the genomic level of interest, such as genes or exons. Although RNA-Seq can be used to search for novel exons or for splice-variants and isoform-specific expression ( 7 , 12 – 14 ), transcript assembly ( 15 ) or allele-specific expression ( 16 , 17 ), our focus in this article is on differential expression for pre-determined genomic features. Nevertheless, the methods developed here are relevant 

### DISCUSSION
The methods described in this article are implemented in the software package edgeR ( 24 ), available as part of the Bioconductor project for open-source genomic software ( 56 ). The methods provide a flexible and powerful approach to analyse read