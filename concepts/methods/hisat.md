---
title: "HISAT: a fast spliced aligner with low memory requirements"
type: paper
journal: "Nature Methods"
year: 2015
authors:
  - Kim D
  - Langmead B
  - Salzberg SL
doi: "10.1038/nmeth.3317"
technology:
  - RNA-seq alignment
  - Burrows-Wheeler Transform
  - FM-index
  - hierarchical indexing
status: reviewed
confidence: high
updated: "2026-05-29"
tags:
  - alignment
  - RNA-seq
  - bioinformatics-tool
aliases: ["xr-10-1038-nmeth-3317"]
---
# HISAT

## 1. Scientific Context

### Existing Consensus (Before HISAT)
RNA-seq alignment was dominated by TopHat2 (splice-aware, Bowtie2-based) and STAR (suffix array-based). TopHat2 was slow; STAR was fast but memory-intensive. A method combining speed AND low memory was needed.

### Knowledge Gaps
- Genome-scale FM-index was memory-efficient but slow for spliced alignment
- Local indexes were fast but fragmented
- No method combined the two strategies

### Why This Paper Matters
HISAT pioneered hierarchical indexing — one global FM-index for rapid anchor placement + thousands of local FM-indexes for rapid spliced extension. HISAT2 (2019) became the most widely-used RNA-seq aligner.

---

## 2. Research Questions
- **Primary**: Can a two-level (global + local) indexing scheme provide both speed and memory efficiency for spliced alignment?
- **Secondary**: Can HISAT match STAR's accuracy with less memory?

---

## 3. Experimental Logic
```
Whole-genome FM-index → anchor alignment
    ↓
48,000 local FM-indexes (~64 kb each) → spliced extension
    ↓
Result: 4.3 GB memory, speed comparable to STAR
```

---

## 4. Method Analysis
### Hierarchical Indexing
1. **Global FM-index**: Whole-genome, for initial read anchoring
2. **Local FM-indexes**: 48,000 indexes covering ~64 kb regions each
3. **Two-stage alignment**: (a) anchor search with global index → (b) spliced extension with local index

### Key Innovation
Hierarchical decomposition of the alignment problem. The global index finds candidate regions; local indexes extend alignments with splice-aware logic. This decouples memory (fixed at 4.3 GB for human) from genome complexity.

---

## 5. Evidence Extraction
| # | Claim | Type | Level |
|---|-------|------|-------|
| E1 | HISAT is faster than TopHat2 with equal or better accuracy | observation | Strong |
| E2 | HISAT requires only 4.3 GB for human genome | observation | Strong |
| E3 | HISAT supports genomes >4 billion bases | observation | Moderate |

---

## 6. Knowledge Graph
**Entities**: HISAT, HISAT2, TopHat2, STAR, FM-index, Burrows-Wheeler Transform
**Relationships**: HISAT → successor → HISAT2; HISAT → competitor → STAR

---

## 7. Critical Evaluation
- **Strengths**: Low memory, fast, supports any genome size, open source
- **Weaknesses**: Index building is slow; performance for very long reads limited
- **Legacy**: HISAT (2015) was superseded by HISAT2 (2019, graph-based)

---

## 8. Research Insight
HISAT2 + StringTie + Ballgown formed the "new Tuxedo" pipeline, replacing TopHat2 + Cufflinks. HISAT-genotype extended the framework to variant-aware alignment.

---

## 9. Future Opportunities
Deprecated — HISAT2 is the current standard. Future work should reference HISAT2 paper (Kim et al., 2019, Nature Biotechnology).
## 摘要
HISAT (hierarchical indexing for spliced alignment of transcripts) is a highly efficient system for aligning reads from RNA sequencing experiments. HISAT uses an indexing scheme based on the Burrows-Wheeler transform and the Ferragina-Manzini (FM) index, employing two types of indexes for alignment: a whole-genome FM index to anchor each alignment and numerous local FM indexes for very rapid extensions of these alignments. HISAT's hierarchical index for the human genome contains 48,000 local FM indexes, each representing a genomic region of ∼64,000 bp. Tests on real and simulated data sets showed that HISAT is the fastest system currently available, with equal or better accuracy than any other method. Despite its large number of indexes, HISAT requires only 4.3 gigabytes of memory. HISAT supports genomes of any size, including those larger than 4 billion bases.

**OA PDF**: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4655817

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
## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[xr-10-1016-j-molp-2019-04-004]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[featurecounts-an-efficient-general-purpose-program-for-assigning-seque]]
- [[moderated-estimation-of-fold-change-and-dispersion-for-rna]]

