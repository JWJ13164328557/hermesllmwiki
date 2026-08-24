title: "Trimmomatic ： Illumina序列数据的灵活修剪器。"
created: 2026-05-28
type: concept
tags: [#methods-tools, papers]
doi: 10.1093/bioinformatics/btu170
confidence: medium
aliases: ["Trimmomatic ： Illumina序列数据的灵活修剪器。"]
status: draft
updated: "2026-05-29"

# Trimmomatic ： Illumina序列数据的灵活修剪器。




**期刊**: 
**DOI**: [10.1093/bioinformatics/btu170](https://doi.org/10.1093/bioinformatics/btu170)
**作者**: 

## 摘要
<h4>Motivation</h4>Although many next-generation sequencing (NGS) read preprocessing tools already existed, we could not find any tool or combination of tools that met our requirements in terms of flexibility, correct handling of paired-end data and high performance. We have developed Trimmomatic as a more flexible and efficient preprocessing tool, which could correctly handle paired-end data.<h4>Results</h4>The value of NGS read preprocessing is demonstrated for both reference-based and reference-free tasks. Trimmomatic is shown to produce output that is at least competitive with, and in many cases superior to, that produced by other tools, in all scenarios tested.<h4>Availability and implementation</h4>Trimmomatic is licensed under GPL V3. It is cross-platform (Java 1.5+ required) and available at http://www.usadellab.org/cms/index.php?page=trimmomatic<h4>Contact</h4>usadel@bio1.rwth-aachen.de<h4>Supplementary information</h4>Supplementary data are available at Bioinformatics online.


## 全文 (PMC)

### PERMALINK

*To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2013 Jul 13; Revised 2014 Mar 9; Accepted 2014 Mar 25; Issue date 2014 Aug 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/3.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited. Motivation:Although many next-generation sequencing (NGS) read preprocessing tools already existed, we could not find any tool or combination of tools that met our requirements in terms of flexibility, correct handling of paired-end data and high performance. We have developed Trimmomatic as a more flexible and efficient preprocessing tool, which could correctly handle paired-end data. Results:The value of NGS read preprocessing is demonstrated for both reference-based and reference-free tasks. Trimmomatic is shown to produce output that is at least competitive with, and in many cases superior to, that produced by other tools, in all scenarios tested. Availability and implementation:Trimmomatic is licensed under GPL V3. It is cross-platform (Java 1.5+ required) and available athttp://www.usadellab.org/cms/index.php?page=trimmomatic Contact:usadel@bio1.rwth-aachen.de Supplementary information:Supplementary dataare available atBioinformaticsonline. The presence of poor quality or technical sequences such as adapters in next-generation sequencing (NGS) data can easily result in suboptimal downstream analyses. Nonetheless, it is not trivial to precisely identify such sequences, including partial adapter sequences, while leaving valid sequence data intact (Liet al., 2013). Furthermore, given the rate with which NGS sequence data are currently being produced (Mardis, 2008), the additional burden of sequence preprocessing must be kept relatively modest so as to avoid adding undue overhead to the bioinformatics pipeline. The preprocessing appro

### Anthony M Bolger

*To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2013 Jul 13; Revised 2014 Mar 9; Accepted 2014 Mar 25; Issue date 2014 Aug 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/3.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.

### 

*To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2013 Jul 13; Revised 2014 Mar 9; Accepted 2014 Mar 25; Issue date 2014 Aug 1. This is an Open Access article distributed under the terms of the Creative Commons Attribution License (http://creativecommons.org/licenses/by/3.0/), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/30/15/2114/48924714/bioinformatics_30_15_2114.pdf


## 相关文献

- [[aba-biosynthesis-stress]]
- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-root-sc-atlas-plantcell]]
- [[arabidopsis-root-sc-atlas-review]]
- [[arabidopsis-sam-scrna]]
- [[b3--bs1tAYpaCxa0fWZ49R6kw]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]



## PMC 全文


**来源类型**: PMC全文
**PMC ID**: PMC4103590

### Abstract
Motivation: Although many next-generation sequencing (NGS) read preprocessing tools already existed, we could not find any tool or combination of tools that met our requirements in terms of flexibility, correct handling of paired-end data and high performance. We have developed Trimmomatic as a more flexible and efficient preprocessing tool, which could correctly handle paired-end data.
Results: The value of NGS read preprocessing is demonstrated for both reference-based and reference-free tasks. Trimmomatic is shown to produce output that is at least competitive with, and in many cases superior to, that produced by other tools, in all scenarios tested.
Availability and implementation: Trimmomatic is licensed under GPL V3. It is cross-platform (Java 1.5+ required) and available at http://www.usadellab.org/cms/index.php?page=trimmomatic
usadel@bio1.rwth-aachen.de
Supplementary information:

### 1 INTRODUCTION
The presence of poor quality or technical sequences such as adapters in next-generation sequencing (NGS) data can easily result in suboptimal downstream analyses.
Nonetheless, it is not trivial to precisely identify such sequences, including partial adapter sequences, while leaving valid sequence data intact ( Li et al. , 2013 ). Furthermore, given the rate with which NGS sequence data are currently being produced ( Mardis, 2008 ), the additional burden of sequence preprocessing must be kept relatively modest so as to avoid adding undue overhead to the bioinformatics pipeline.
The preprocessing approach must also not interfere with the downstream analysis of the data. For example, NGS data often come in the form of paired-end reads, and typically, the forward and reverse reads are stored in two separate FASTQ files, which contain reads from each DNA fragment in the same order. Many downstream tools use this positional relationship between pairs, so it must be maintained when preprocessing the sequence data.
The wide range of available NGS library preparations combined with the range of downstream applications demand a flexible approach. It should be possible to choose a set of processing steps to be applied in a user-defined order, and ideally even allow some steps to be included more than once. In other domains, this can be achieved using a shell pipeline to combine multiple tools as required, e.g. in Newick ( Junier and Zdobnov, 2010 ). However, the need for ‘pair awareness

### 4 RESULTS
To illustrate the value of data preprocessing, we evaluated two different scenarios: reference-based alignment using Bowtie 2 ( Langmead and Salzberg, 2012 ) and BWA ( Li and Durbin, 2009 ) against the Escherichia coli K-12/MG1655 reference (NCBI sequence NC_000913.2 ), and de novo assembly using Velvet ( Zerbino and Birney, 2008 ), on public E.coli K-12/MG1655 datasets (SRA datasets SRX131047 and SRR519926), as described in the Supplementary Methods .

## 深度提炼

**物种**: Ficus carica
**方法**: molecular biology / biochemistry
**来源**: DOI:10.1093/bioinformatics/btu170
**来源类型**: PDF全文 (10.1093_bioinformatics_btu170.pdf)

### 核心发现
1. Intuitively, it is clear that short reads are almost worthless because they occur multiple times within the target sequence and thus they give only ambiguous information.
2. On the other hand, most long reads can be mapped to few loca- tions in the target sequence.
3. Given a target length t, the putative trimming to length l would give a length threshold score: ScoreLTðlÞ ¼ 1 1 þ etl ð Þ The second factor models ‘coverage’, and provides a linear score based on retained sequence length: ScoreCovðlÞ ¼ l This reflects that, given reasonably high-accuracy bases, a longer read contains more information that is useful for most applications.
4. Notably, the optimal results for strict alignment and tolerant alignment were found using widely different quality stringency settings.
5. Not surprisingly, trimming is even more critical to achieving acceptable alignment rates with these data.
6. Perhaps surprisingly, no adapter sequences were found in the assembly of the untrimmed version of this dataset.