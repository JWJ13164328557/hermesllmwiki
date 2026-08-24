title: "edgeR ：用于数字基因表达数据差异表达分析的生物导体包。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btp616
confidence: medium
aliases: ["edgeR ：用于数字基因表达数据差异表达分析的生物导体包。"]
status: draft
updated: "2026-05-29"

# edgeR ：用于数字基因表达数据差异表达分析的生物导体包。




**期刊**: 
**DOI**: [10.1093/bioinformatics/btp616](https://doi.org/10.1093/bioinformatics/btp616)
**作者**: 

## 摘要
<h4>Summary</h4>It is expected that emerging digital gene expression (DGE) technologies will overtake microarray technologies in the near future for many functional genomics applications. One of the fundamental data analysis tasks, especially for gene expression studies, involves determining whether there is evidence that counts for a transcript or exon are significantly different across experimental conditions. edgeR is a Bioconductor software package for examining differential expression of replicated count data. An overdispersed Poisson model is used to account for both biological and technical variability. Empirical Bayes methods are used to moderate the degree of overdispersion across transcripts, improving the reliability of inference. The methodology can be used even with the most minimal levels of replication, provided at least one phenotype or experimental condition is replicated. The software may have other applications beyond sequencing data, such as proteome peptide count data.<h4>Availability</h4>The package is freely available under the LGPL licence from the Bioconductor web site (http://bioconductor.org).


## 全文 (PMC)

### PERMALINK

* To whom correspondence should be addressed †The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Associate Editor: Joaquin Dopazo Received 2009 Mar 29; Revised 2009 Oct 19; Accepted 2009 Oct 23; Issue date 2010 Jan 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.5/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited. Summary:It is expected that emerging digital gene expression (DGE) technologies will overtake microarray technologies in the near future for many functional genomics applications. One of the fundamental data analysis tasks, especially for gene expression studies, involves determining whether there is evidence thatcountsfor a transcript or exon are significantly different across experimental conditions.edgeRis a Bioconductor software package for examining differential expression of replicated count data. An overdispersed Poisson model is used to account for both biological and technical variability. Empirical Bayes methods are used to moderate the degree of overdispersion across transcripts, improving the reliability of inference. The methodology can be used even with the most minimal levels of replication, provided at least one phenotype or experimental condition is replicated. The software may have other applications beyond sequencing data, such as proteome peptide count data. Availability:The package is freely available under the LGPL licence from the Bioconductor web site (http://bioconductor.org). Contact:mrobinson@wehi.edu.au Modern molecular biology data present major challenges for the statistical methods that are used to detect differential expression, such as the requirement of multiple testing procedures and increasingly, empirical Bayes or similar methods that share inf

### Mark D Robinson

* To whom correspondence should be addressed †The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Associate Editor: Joaquin Dopazo Received 2009 Mar 29; Revised 2009 Oct 19; Accepted 2009 Oct 23; Issue date 2010 Jan 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.5/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

* To whom correspondence should be addressed †The authors wish it to be known that, in their opinion, the first two authors should be regarded as joint First Authors. Associate Editor: Joaquin Dopazo Received 2009 Mar 29; Revised 2009 Oct 19; Accepted 2009 Oct 23; Issue date 2010 Jan 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.5/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/26/1/139/48851299/bioinformatics_26_1_139.pdf


## 相关文献

- [[alfalfa-cadmium-sc-multiomics]]
- [[andrographis-msi-sc-spatial]]
- [[arabidopsis-root-regeneration-sc-multi]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[artemisinin-scrna-glandular-trichomes]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC2796818

### Abstract
Summary: It is expected that emerging digital gene expression (DGE) technologies will overtake microarray technologies in the near future for many functional genomics applications. One of the fundamental data analysis tasks, especially for gene expression studies, involves determining whether there is evidence that counts for a transcript or exon are significantly different across experimental conditions. edgeR is a Bioconductor software package for examining differential expression of replicated count data. An overdispersed Poisson model is used to account for both biological and technical variability. Empirical Bayes methods are used to moderate the degree of overdispersion across transcripts, improving the reliability of inference. The methodology can be used even with the most minimal levels of replication, provided at least one phenotype or experimental condition is replicated. The software may have other applications beyond sequencing data, such as proteome peptide count data.
Availability: The package is freely available under the LGPL licence from the Bioconductor web site ( http://bioconductor.org ).

### 1 INTRODUCTION
Modern molecular biology data present major challenges for the statistical methods that are used to detect differential expression, such as the requirement of multiple testing procedures and increasingly, empirical Bayes or similar methods that share information across all observations to improve inference. For microarrays, the abundance of a particular transcript is measured as a fluorescence intensity, effectively a continuous response, whereas for digital gene expression (DGE) data the abundance is observed as a count. Therefore, procedures that are successful for microarray data are not directly applicable to DGE data.

### 4 DISCUSSION
We have developed a Bioconductor package edgeR that addresses one of the fundamental downstream data analysis tasks for count-based expression data: determining differential expression. The package and methods are general, and can work on other sources of count data, such as barcoding experiments and peptide counts. To the authors' knowledge, edgeR is the only software for SAGE or DGE data at this time which can account for biological variability when there are only one or two replicate samples.
Funding : National Health and Medical Research Council Program (Grant 406657 to G.K.S.); NHMRC, Independent Research Institutes Infrastructure Support Scheme (Grant 361646); Victorian State Government OIS grant (awarded to the WEHI); a Melbourne International Research Scholarship (to M.D.R.); Belz, Harris and IBS Honours scholarships (to D.J.M.).

## 深度提炼

**物种**: Ficus carica
**方法**: transcriptomics (RNA-seq), ChIP-seq/qPCR
**来源**: DOI:10.1093/bioinformatics/btp616
**来源类型**: PDF全文 (10.1093_bioinformatics_btp616.pdf)

### 核心发现
_（无显著信号句）_