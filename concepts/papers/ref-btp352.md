title: "序列对齐/映射格式和SAMtools。"
created: 2026-05-28
type: concept
tags: [#genomics-evolution, papers]
doi: 10.1093/bioinformatics/btp352
confidence: medium
aliases: ["序列对齐/映射格式和SAMtools。"]
status: draft
updated: "2026-05-29"

# 序列对齐/映射格式和SAMtools。




**期刊**: 
**DOI**: [10.1093/bioinformatics/btp352](https://doi.org/10.1093/bioinformatics/btp352)
**作者**: 

## 摘要
<h4>Summary</h4>The Sequence Alignment/Map (SAM) format is a generic alignment format for storing read alignments against reference sequences, supporting short and long reads (up to 128 Mbp) produced by different sequencing platforms. It is flexible in style, compact in size, efficient in random access and is the format in which alignments from the 1000 Genomes Project are released. SAMtools implements various utilities for post-processing alignments in the SAM format, such as indexing, variant caller and alignment viewer, and thus provides universal tools for processing read alignments.<h4>Availability</h4>http://samtools.sourceforge.net.


## 全文 (PMC)

### PERMALINK

To whom correspondence should be addressed. †The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Associate Editor: Alfonso Valencia Received 2009 Apr 28; Revised 2009 May 28; Accepted 2009 May 30; Issue date 2009 Aug 15. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.0/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited. Summary:The Sequence Alignment/Map (SAM) format is a generic alignment format for storing read alignments against reference sequences, supporting short and long reads (up to 128 Mbp) produced by different sequencing platforms. It is flexible in style, compact in size, efficient in random access and is the format in which alignments from the 1000 Genomes Project are released. SAMtools implements various utilities for post-processing alignments in the SAM format, such as indexing, variant caller and alignment viewer, and thus provides universal tools for processing read alignments. Availability:http://samtools.sourceforge.net With the advent of novel sequencing technologies such as Illumina/Solexa, AB/SOLiD and Roche/454 (Mardis,2008), a variety of new alignment tools (Langmeadet al.,2009; Liet al.,2008) have been designed to realize efficient read mapping against large reference sequences, including the human genome. These tools generate alignments in different formats, however, complicating downstream processing. A common alignment format that supports all sequence types and aligners creates a well-defined interface between alignment and downstream analyses, including variant detection, genotyping and assembly. The Sequence Alignment/Map (SAM) format is designed to achieve this goal. It supports single- and paired-end reads and combining reads of different types, including color

### Heng Li

To whom correspondence should be addressed. †The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Associate Editor: Alfonso Valencia Received 2009 Apr 28; Revised 2009 May 28; Accepted 2009 May 30; Issue date 2009 Aug 15. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.0/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

To whom correspondence should be addressed. †The authors wish it to be known that, in their opinion, the first two authors should be regarded as Joint First Authors. Associate Editor: Alfonso Valencia Received 2009 Apr 28; Revised 2009 May 28; Accepted 2009 May 30; Issue date 2009 Aug 15. This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/by-nc/2.0/uk/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/25/16/2078/48994296/bioinformatics_25_16_2078.pdf


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC2723002

### Abstract
Summary: The Sequence Alignment/Map (SAM) format is a generic alignment format for storing read alignments against reference sequences, supporting short and long reads (up to 128 Mbp) produced by different sequencing platforms. It is flexible in style, compact in size, efficient in random access and is the format in which alignments from the 1000 Genomes Project are released. SAMtools implements various utilities for post-processing alignments in the SAM format, such as indexing, variant caller and alignment viewer, and thus provides universal tools for processing read alignments.
Availability: http://samtools.sourceforge.net

### 1 INTRODUCTION
With the advent of novel sequencing technologies such as Illumina/Solexa, AB/SOLiD and Roche/454 (Mardis, 2008 ), a variety of new alignment tools (Langmead et al. , 2009 ; Li et al. , 2008 ) have been designed to realize efficient read mapping against large reference sequences, including the human genome. These tools generate alignments in different formats, however, complicating downstream processing. A common alignment format that supports all sequence types and aligners creates a well-defined interface between alignment and downstream analyses, including variant detection, genotyping and assembly.
The Sequence Alignment/Map (SAM) format is designed to achieve this goal. It supports single- and paired-end reads and combining reads of different types, including color space reads from AB/SOLiD. It is designed to scale to alignment sets of 10 11 or more base pairs, which is typical for the deep resequencing of one human individual.

## 深度提炼

**物种**: Plant (unspecified)
**方法**: molecular biology
**来源**: DOI:10.1093/bioinformatics/btp352
**来源类型**: PMC全文
**文本来源**: NCBI PMC HTML (cleaned)

### 核心发现
1. SAMtools implements various utilities for post-processing alignments in the SAM format, such as indexing, variant caller and alignment viewer, and thus provides universal tools for processing read alignments.