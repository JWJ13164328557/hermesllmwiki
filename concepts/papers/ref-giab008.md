title: Twelve years of SAMtools and BCFtools.
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/gigascience/giab008
confidence: medium
aliases: ["Twelve years of SAMtools and BCFtools."]
status: draft
updated: "2026-05-29"

# Twelve years of SAMtools and BCFtools.




**期刊**: 
**DOI**: [10.1093/gigascience/giab008](https://doi.org/10.1093/gigascience/giab008)
**作者**: 

## 摘要
<h4>Background</h4>SAMtools and BCFtools are widely used programs for processing and analysing high-throughput sequencing data. They include tools for file format conversion and manipulation, sorting, querying, statistics, variant calling, and effect analysis amongst other methods.<h4>Findings</h4>The first version appeared online 12 years ago and has been maintained and further developed ever since, with many new features and improvements added over the years. The SAMtools and BCFtools packages represent a unique collection of tools that have been used in numerous other software projects and countless genomic pipelines.<h4>Conclusion</h4>Both SAMtools and BCFtools are freely available on GitHub under the permissive MIT licence, free for both non-commercial and commercial use. Both packages have been installed >1 million times via Bioconda. The source code and documentation are available from https://www.htslib.org.


## 全文 (PMC)

### PERMALINK

Correspondence address. Andrew Whitwham, Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, Cambridgeshire, CB10 1SA, UK. Tel: +44 (0)1223 834244; E-mail:samtools@sanger.ac.uk Received 2020 Dec 16; Revised 2021 Jan 18; Accepted 2021 Jan 28; Collection date 2021 Feb. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. SAMtools and BCFtools are widely used programs for processing and analysing high-throughput sequencing data. They include tools for file format conversion and manipulation, sorting, querying, statistics, variant calling, and effect analysis amongst other methods. The first version appeared online 12 years ago and has been maintained and further developed ever since, with many new features and improvements added over the years. The SAMtools and BCFtools packages represent a unique collection of tools that have been used in numerous other software projects and countless genomic pipelines. Both SAMtools and BCFtools are freely available on GitHub under the permissive MIT licence, free for both non-commercial and commercial use. Both packages have been installed >1 million times via Bioconda. The source code and documentation are available fromhttps://www.htslib.org. Keywords:samtools, bcftools, high-throughput sequencing, next generation sequencing, variant calling, data analysis With the advancement of genome sequencing technologies and large-scale sequencing projects, new data formats became necessary for interoperability, compact storage, and efficient analysis of the data. Among the most common formats used in this field today are SAM [1] and VCF [2], developed by the 1000 Genomes Project [3]. These specialized formats for storing read alignments (SAM) and genetic variants (VCF) are row-oriented tab-delimited text files, wh

### Petr Danecek

Correspondence address. Andrew Whitwham, Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, Cambridgeshire, CB10 1SA, UK. Tel: +44 (0)1223 834244; E-mail:samtools@sanger.ac.uk Received 2020 Dec 16; Revised 2021 Jan 18; Accepted 2021 Jan 28; Collection date 2021 Feb. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### Correspondence address

Correspondence address. Andrew Whitwham, Wellcome Sanger Institute, Wellcome Genome Campus, Hinxton, Cambridgeshire, CB10 1SA, UK. Tel: +44 (0)1223 834244; E-mail:samtools@sanger.ac.uk Received 2020 Dec 16; Revised 2021 Jan 18; Accepted 2021 Jan 28; Collection date 2021 Feb. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/4.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/gigascience/article-pdf/10/2/giab008/36332246/giab008.pdf


## 相关文献

- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b4-0Ai2UdSwKz-GbYdfit26vw]]
- [[b4-78WuUWiztOxRe4n5MS2Pag]]
- [[b4-ZKYanCM-ZalgHteLOaJErw]]
- [[b4-_dqlLGuPZxhNXXs6caCEwg]]
- [[b4-uZ39cWEaJqczzAZtUK3Iww]]
- [[b4-ys8H9kH4cFVbPEuMHCg4nA]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC7931819

### Discussion
SAMtools and BCFtools represent a unique collection of tools useful for processing and analysis of sequencing data. Their development has been driven by the need of both large projects and individual user requests issued via GitHub. The code has been installed 1 million times via Bioconda [ 25 ] and GitHub releases [ 9 , 14 ], and 1600 support and feature requests have been resolved on GitHub.
The programs are written in the C programming language and optimized for low memory consumption and high speed. For example, the “bcftools csq” command for prediction of functional consequences in a haplotype-aware manner requires only a fraction of the memory required by VEP and is 2 orders of magnitude faster [ 26 ].
Much work has been done to increase the reliability of SAMtools and BCFtools. The test harnesses now include ∼700 tests in SAMtools and ∼1,400 in BCFtools. Continuous integration services run all of the tests on a variety of platforms (including Linux, MacOS, and Windows) whenever code is checked into the source repository, ensuring that bugs are discovered and fixed rapidly. Code quality is also assured by checking for memory errors, originally using Valgrind memcheck [ 27 ] and more recently with AddressSanitizer [ 28 ]. Additionally, UndefinedBehaviorSanitizer is used to detect violations of the C standard.
Despite the ever-growing sample sizes and rapid increases in the amount of sequenced data, the programs have withstood the test of time. However, extremely big file

## 深度提炼

**物种**: Plant (unspecified)
**方法**: computational method
**来源**: DOI:10.1093/gigascience/giab008
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (cleaned)

### 核心发现
_（全文信号句不足）_