---
title: HISAT: a fast spliced aligner with low memory requirements.
created: 2026-05-28
type: concept
tags: [metabolism]
doi: 10.1038/nmeth.3317
confidence: medium
aliases: ["HISAT: a fast spliced aligner with low memory requirements."]
status: draft
updated: "2026-05-29"
---

# HISAT: a fast spliced aligner with low memory requirements.




**期刊**: 
**DOI**: [10.1038/nmeth.3317](https://doi.org/10.1038/nmeth.3317)
**作者**: 

## 摘要
HISAT (hierarchical indexing for spliced alignment of transcripts) is a highly efficient system for aligning reads from RNA sequencing experiments. HISAT uses an indexing scheme based on the Burrows-Wheeler transform and the Ferragina-Manzini (FM) index, employing two types of indexes for alignment: a whole-genome FM index to anchor each alignment and numerous local FM indexes for very rapid extensions of these alignments. HISAT's hierarchical index for the human genome contains 48,000 local FM indexes, each representing a genomic region of ∼64,000 bp. Tests on real and simulated data sets showed that HISAT is the fastest system currently available, with equal or better accuracy than any other method. Despite its large number of indexes, HISAT requires only 4.3 gigabytes of memory. HISAT supports genomes of any size, including those larger than 4 billion bases.



## 全文 (PMC)

### ### PERMALINK

Correspondence should be addressed to D.K. (infphilo@gmail.com), B.L. (langmea@cs.jhu.edu) or S.L.S. (salzberg@jhu.edu) Reprints and permissions information is available online athttp://www.nature.com/reprints/index.html. HISAT (hierarchical indexing for spliced alignment of transcripts) is a highly efficient system for aligning reads from RNA sequencing experiments. HISAT uses an indexing scheme based on the Burrows-Wheeler transform and the Ferragina-Manzini (FM) index, employing two types of indexes for alignment: a whole-genome FM index to anchor each alignment and numerous local FM indexes for very rapid extensions of these alignments. HISAT’s hierarchical index for the human genome contains 48,000 local FM indexes, each representing a genomic region of ~64,000 bp. Tests on real and simulated data sets showed that HISAT is the fastest system currently available, with equal or better accuracy than any other method. Despite its large number of indexes, HISAT requires only 4.3 gigabytes of memory. HISAT supports genomes of any size, including those larger than 4 billion bases. Since its introduction in 2008, RNA-seq1has become ubiquitous as a tool for the study of gene expression, transcript structure and the identification of long noncoding RNAs and fusion transcripts2–5As RNA-seq has matured, sequencing throughput and read lengths have increased dramatically to 100–500 million reads per run with lengths of 100 bp or longer. These large and ever-increasing data volumes nec

### Daehwan Kim

Correspondence should be addressed to D.K. (infphilo@gmail.com), B.L. (langmea@cs.jhu.edu) or S.L.S. (salzberg@jhu.edu) Reprints and permissions information is available online athttp://www.nature.com/reprints/index.html.

### AUTHOR CONTRIBUTIONS

Note: Any Supplementary Information and Source Data files are available in theonline version of the paper. D.K., B.L. and S.L.S. performed the analysis and discussed the results of HISAT. D.K. implemented HISAT. D.K., B.L. and S.L.S. wrote the manuscript. All authors read and approved the final manuscript. COMPETING FINANCIAL INTERESTS The authors declare no competing financial interests.


**OA PDF**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4655817


## 深度提炼

**物种**: Homo sapiens

**方法**: bulk RNA-seq

### 核心发现

- Tests on real and simulated data sets showed that HISAT is the fastest system currently available, with equal or better accuracy than any other method.
- RNA-seq analysis begins by aligning reads against a reference genome to determine the location from which the reads originated6–8a step that has become a time-consuming bottleneck; for example, widely used alignment programs such as TopHat2 (ref.9) a
- The recently introduced STAR program11uses suffix arrays to provide substantially faster processing than most other met Correspondence should be addressed to D.K.

**全文来源**: PMC全文
