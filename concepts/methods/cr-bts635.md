---
title: STAR: ultrafast universal RNA-seq aligner.
created: 2026-05-28
type: concept
tags: [development, metabolism, single-cell]
doi: 10.1093/bioinformatics/bts635
confidence: medium
aliases: ["STAR: ultrafast universal RNA-seq aligner."]
status: draft
updated: "2026-05-29"
---

# STAR: ultrafast universal RNA-seq aligner.




**期刊**: 
**DOI**: [10.1093/bioinformatics/bts635](https://doi.org/10.1093/bioinformatics/bts635)
**作者**: 

## 摘要
<h4>Motivation</h4>Accurate alignment of high-throughput RNA-seq data is a challenging and yet unsolved problem because of the non-contiguous transcript structure, relatively short read lengths and constantly increasing throughput of the sequencing technologies. Currently available RNA-seq aligners suffer from high mapping error rates, low mapping speed, read length limitation and mapping biases.<h4>Results</h4>To align our large (>80 billon reads) ENCODE Transcriptome RNA-seq dataset, we developed the Spliced Transcripts Alignment to a Reference (STAR) software based on a previously undescribed RNA-seq alignment algorithm that uses sequential maximum mappable seed search in uncompressed suffix arrays followed by seed clustering and stitching procedure. STAR outperforms other aligners by a factor of >50 in mapping speed, aligning to the human genome 550 million 2 × 76 bp paired-end reads per hour on a modest 12-core server, while at the same time improving alignment sensitivity and precision. In addition to unbiased de novo detection of canonical junctions, STAR can discover non-canonical splices and chimeric (fusion) transcripts, and is also capable of mapping full-length RNA sequences. Using Roche 454 sequencing of reverse transcription polymerase chain reaction amplicons, we experimentally validated 1960 novel intergenic splice junctions with an 80-90% success rate, corroborating the high precision of the STAR mapping strategy.<h4>Availability and implementation</h4>STAR is implemented as a standalone C++ code. STAR is free open source software distributed under GPLv3 license and can be downloaded from http://code.google.com/p/rna-star/.



## 全文 (PMC)

### ### PERMALINK

*To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2012 May 29; Revised 2012 Oct 17; Accepted 2012 Oct 19; Issue date 2013 Jan. Motivation:Accurate alignment of high-throughput RNA-seq data is a challenging and yet unsolved problem because of the non-contiguous transcript structure, relatively short read lengths and constantly increasing throughput of the sequencing technologies. Currently available RNA-seq aligners suffer from high mapping error rates, low mapping speed, read length limitation and mapping biases. Results:To align our large (>80 billon reads) ENCODE Transcriptome RNA-seq dataset, we developed the Spliced Transcripts Alignment to a Reference (STAR) software based on a previously undescribed RNA-seq alignment algorithm that uses sequential maximum mappable seed search in uncompressed suffix arrays followed by seed clustering and stitching procedure. STAR outperforms other aligners by a factor of >50 in mapping speed, aligning to the human genome 550 million 2 × 76 bp paired-end reads per hour on a modest 12-core server, while at the same time improving alignment sensitivity and precision. In addition to unbiasedde novodetection of canonical junctions, STAR can discover non-canonical splices and chimeric (fusion) transcripts, and is also capable of mapping full-length RNA sequences. Using Roche 454 sequencing of reverse transcription polymerase chain reaction amplicons, we experimentally validated 1960 novel intergenic splice jun

### Alexander Dobin

*To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2012 May 29; Revised 2012 Oct 17; Accepted 2012 Oct 19; Issue date 2013 Jan.

### *To whom correspondence should be addressed. Associate Editor: Inanc Birol Received 2012 May 29; Revised 2012 Oct 17; Accepted 2012 Oct 19; Issue date 2013 Jan.

**OA PDF**: https://academic.oup.com/bioinformatics/article-pdf/29/1/15/17101697/bts635.pdf


## 深度提炼

**物种**: Homo sapiens

**方法**: bulk RNA-seq

### 核心发现

- In addition to unbiasedde novodetection of canonical junctions, STAR can discover non-canonical splices and chimeric (fusion) transcripts, and is also capable of mapping full-length RNA sequences.
- Using Roche 454 sequencing of reverse transcription polymerase chain reaction amplicons, we experimentally validated 1960 novel intergenic splice junctions with an 80–90% success rate, corroborating the high precision of the STAR mapping strategy.
- Although genomes are composed of linearly ordered sequences of nucleic acids, eukaryotic cells generally reorganize the information in the transcriptome by splicing together non-contiguous exons *To whom correspondence should be addressed.

**全文来源**: PMC全文
