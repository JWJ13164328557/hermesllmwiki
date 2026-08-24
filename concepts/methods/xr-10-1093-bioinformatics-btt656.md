---
title: "featureCounts: an efficient general purpose program for assigning sequence reads to genomic features"
type: paper
journal: "Bioinformatics"
year: 2014
authors:
  - Liao Y
  - Smyth GK
  - Shi W
doi: "10.1093/bioinformatics/btt656"
species:
  - Homo sapiens
  - Mus musculus
  - Drosophila melanogaster
technology:
  - RNA-seq (Illumina)
  - DNA-seq (genomic)
  - Subread aligner
  - featureCounts
  - Rsubread (Bioconductor)
dataset_accession: "GEO/SRA for benchmark datasets; see paper supplementary"
status: reviewed
confidence: high
updated: "2026-05-29"
tags:
  - featureCounts
  - read-summarization
  - RNA-seq
  - read-counting
  - Subread
  - Rsubread
  - gene-expression
  - differential-expression
source: "methods/xr-10-1093-bioinformatics-btt656"
---

# featureCounts: an efficient general purpose program for assigning sequence reads to genomic features

---

## 1. Scientific Context

### Existing Consensus (Before This Paper)

By 2013, RNA-seq differential expression analysis had become a standard genomics workflow, typically following the pipeline: align reads → count reads per gene → test for differential expression. While alignment algorithms (STAR [[xr-10-1093-bioinformatics-bts635]], TopHat2, BWA) and differential expression methods (DESeq [[xr-10.1186/gb-2010-11-10-r106]], edgeR [[xr-10.1093/bioinformatics/btp616]], limma-voom) had matured substantially, the intermediate step — read summarization (counting) — had received surprisingly little systematic attention. Key prior consensus:

- **Read summarization was a solved problem in principle**: Counting reads overlapping annotated genomic features (exons, genes) sounds trivial — find all reads that overlap each feature
- **Existing tools were slow**: The most widely used counting tool, **htseq-count** (part of HTSeq [[xr-10.1093/bioinformatics/btu638|Anders 2015]]), used a naive algorithm: for each read, iterate over all features to find overlaps. This was $O(NR)$ where $R$ is read count and $N$ is feature count — prohibitively slow for large datasets
- **Memory usage was high**: Some counting tools loaded all alignment data into memory, limiting scalability to large projects
- **Multi-mapping reads were handled inconsistently**: Different tools used different heuristics for reads mapping to multiple genomic locations — some discarded them entirely, others counted them fractionally, with no consensus on best practice
- **Feature hierarchies were poorly supported**: Most tools counted at a single level (genes or exons) and required separate runs for each level; meta-feature hierarchies (genes containing exons) were not natively handled
- **Paired-end counting was ambiguous**: Reads from paired-end sequencing that spanned feature boundaries (e.g., one mate in an exon, the other in an intron) were handled differently across tools

### Existing Models

- **htseq-count** (HTSeq): Python-based counter; iterates over each read and checks overlap with all features. Strengths: easy to use, Python ecosystem. Weaknesses: $O(NR)$ complexity — extremely slow on large datasets; no multi-threading
- **BEDTools coverage/intersect**: General-purpose interval overlap tool. Strengths: fast for simple counting. Weaknesses: not specialized for RNA-seq; no handling of multi-mapping, strandedness, or feature hierarchies; requires multiple piped commands
- **summarizeOverlaps** (GenomicAlignments, Bioconductor): R-based counting using GAlignment objects. Strengths: integrated with Bioconductor ecosystem; flexible. Weaknesses: R-based — memory-intensive and slower than C implementations
- **Cufflinks/Cuffquant**: Part of the Tuxedo suite for transcript-level quantification. Strengths: transcript-level resolution. Weaknesses: FPKM-based, not raw counts; complex pipeline; transcript assembly could be unstable

### Knowledge Gaps

- No counting tool specifically optimized for speed via algorithmic innovations (as opposed to just being written in C/C++)
- No rigorous investigation of how counting parameters (multi-mapping handling, feature overlap resolution, strand specificity) affect downstream differential expression results
- The concept of **chromosome-level hashing** to accelerate read-to-feature overlap queries was unexplored for RNA-seq counting
- No tool simultaneously supported gene-level, exon-level, and custom feature counting in a single run with meta-feature aggregation
- No systematic benchmarking of counting speed across tools on realistic large-scale RNA-seq datasets

### Why This Paper Matters

This paper introduced **featureCounts**, a read summarization program that achieved a >10-fold speed improvement over existing methods through two key algorithmic innovations: **chromosome hashing** (partitioning reads and features by chromosome to avoid cross-chromosome overlap checks) and **feature blocking** (grouping overlapping features into blocks for efficient overlap resolution). featureCounts became the standard counting tool for RNA-seq differential expression pipelines, used in conjunction with DESeq2 [[xr-10.1186/s13059-014-0550-0|Love 2014]] and edgeR/limma-voom [[xr-10.1093/bioinformatics/btp616|Robinson 2010]] in virtually every RNA-seq study. It is integrated into the Subread/Rsubread package and remains one of the most widely used bioinformatics tools.

---

## 2. Research Questions

### Primary Question

Can algorithmic innovations — specifically chromosome hashing and feature blocking — dramatically accelerate RNA-seq read summarization while maintaining high accuracy and usability?

### Secondary Questions

1. Does chromosome hashing reduce the computational complexity of read-to-feature overlap queries from $O(NR)$ to approximately $O(R \cdot \bar{F}_{chr})$, where $\bar{F}_{chr}$ is the average number of features per chromosome?
2. Does feature blocking efficiently resolve reads overlapping multiple features by limiting detailed overlap checks to features within the same block?
3. Can featureCounts achieve an order-of-magnitude speed improvement over htseq-count and other existing tools on gene-level summarization?
4. Does featureCounts' memory efficiency (avoiding loading all reads into memory) enable counting on very large datasets that would exhaust memory in other tools?
5. Can featureCounts handle both RNA-seq and genomic DNA-seq counting in a unified framework?
6. Does featureCounts' support for meta-feature aggregation (exon → gene) simplify multi-level counting workflows?

### Explicit Hypotheses

- Partitioning reads by chromosome reduces the effective feature set per read from all genomic features to only features on the same chromosome, an ~25-fold reduction for the human genome (24 chromosomes)
- Overlapping features on the same chromosome can be grouped into blocks; reads only need detailed overlap resolution within the blocks they hit, not against all chromosome features
- Avoiding loading all alignment data into memory (streaming reads chromosome-by-chromosome) will keep memory usage low and near-constant regardless of dataset size

### Implicit Hypotheses

- The read summarization step, while conceptually simple, is a significant practical bottleneck in RNA-seq analysis that algorithmic optimization can address
- A well-designed, highly optimized C implementation can outperform workflow-based approaches (htseq-count + samtools pipes) by an order of magnitude
- Standardized, efficient counting will improve reproducibility across RNA-seq studies by reducing the temptation to use ad hoc counting scripts

---

## 3. Experimental Logic

```
Question: Can chromosome hashing and feature blocking make read summarization
           an order of magnitude faster?
    ↓
Method: Implement featureCounts in C with (1) chromosome hashing,
        (2) feature blocking, (3) streaming read processing.
        Benchmark against htseq-count, BEDTools, summarizeOverlaps.
    ↓
Benchmark 1: Gene-level counting — human RNA-seq (20M reads, ~25,000 genes)
             on various hardware configurations
    ↓
Benchmark 2: Exon-level counting — same dataset with ~250,000 exons
    ↓
Benchmark 3: Paired-end counting — 40M paired-end reads
    ↓
Benchmark 4: Multi-mapping read handling — compare counting strategies
             (discard, fractional, primary-only) on simulated data
    ↓
Validation: Compare featureCounts counts with htseq-count on the same
            dataset; concordance analysis; DE gene overlap analysis
    ↓
Conclusion: featureCounts is >10× faster at gene-level, requires far less
            memory, and produces equivalent counts to established tools
```

### Why Chromosome Hashing?

In the human genome, ~25,000 genes are distributed across 24 chromosomes (~1,000 genes/chromosome on average). A naive read-to-feature overlap check scans all 25,000 genes for every read. Chromosome hashing reduces this: after determining which chromosome a read maps to (trivial from alignment), only features on that chromosome are checked — a ~24-fold reduction.

### Why Feature Blocking?

Genes often overlap (especially on opposite strands, or nested genes). A block is a set of features where each feature overlaps at least one other feature in the block. Reads that map entirely within one block only need to be checked against features in that block — not against all features on the chromosome. For genes, blocks are typically small (1–5 genes), yielding an additional ~200–1,000-fold reduction in overlap checks.

### Why Three Benchmark Scenarios?

- **Gene-level**: The most common use case — tests basic counting speed
- **Exon-level**: Far more features (~250,000 vs. ~25,000) — tests scalability with feature count
- **Paired-end**: Tests whether paired-end logic (fragment-based counting) adds significant overhead

---

## 4. Method Analysis

### Core Algorithm: featureCounts

**Problem formulation**: Given a set of aligned reads $R$ (in SAM/BAM format) and a set of genomic features $F$ (in GTF/GFF/SAF format), assign each read to zero, one, or more features based on their genomic overlap, producing a count matrix $C$ where $C_{ij}$ is the count of reads assigned to feature $j$ in sample $i$.

**Algorithm overview**:

#### Step 1: Chromosome Hashing — Partition Reads and Features

The genome is partitioned by chromosome (and optionally by strand). For each chromosome:

- Extract all features on that chromosome from the annotation
- When processing reads, reads mapping to chromosome $i$ are only checked against features on chromosome $i$

In the SAM/BAM format, each read carries its mapping chromosome (RNAME field). The hashing is therefore $O(1)$: given a read, look up the chromosome-specific feature list.

- **Innovation**: This simple optimization leverages the natural chromosomal organization of genomes. It reduces the feature search space by a factor roughly equal to the number of chromosomes (~24 for human). The key insight is that a read from chromosome 1 cannot possibly overlap a gene on chromosome 2 — but htseq-count checked anyway.

#### Step 2: Feature Ordering and Blocking

Within each chromosome, features are sorted by their genomic start position. Then, **feature blocks** are constructed:

A feature block is a maximal set of features such that:
1. Every feature in the block overlaps (by genomic coordinates) at least one other feature in the block
2. No feature in the block overlaps any feature outside the block

Algorithmically: iterate through sorted features; start a new block when the next feature's start coordinate exceeds the maximum end coordinate of all features in the current block.

- **Innovation**: Feature blocking creates disjoint genomic intervals. A read can overlap features in at most one block (since blocks are disjoint). This means the read only needs detailed overlap checking against features in the block it overlaps — typically 1–5 features for gene annotations, not all features on the chromosome.

#### Step 3: Streaming Read Processing

Reads are processed chromosome-by-chromosome in a **streaming** fashion:

1. Load features for the current chromosome and construct blocks
2. Stream through the BAM file, extracting reads mapping to the current chromosome
3. For each read:
   a. Identify which feature block the read overlaps (binary search on block boundaries)
   b. Within that block, check overlap with each feature
   c. Assign the read to one or more features based on user-specified multi-overlap resolution strategy
4. Flush counts, move to next chromosome

- **Innovation**: Streaming avoids loading all reads into memory. Memory usage depends only on the largest chromosome's feature set and the BAM read buffer — not on total read count. This enables counting on datasets with hundreds of millions of reads on modest hardware.

#### Step 4: Overlap Resolution

For reads overlapping multiple features, featureCounts provides several resolution strategies:

| Strategy | Description | Use Case |
|----------|-------------|----------|
| `-M` (multi-mapping) | Include multi-mapping reads in counts | When multi-mapped reads carry biological signal |
| `--primary` | Only count primary alignments | Standard RNA-seq (discards secondary/supplementary) |
| `-O` (allowMultiOverlap) | Count read for all overlapping features | When counting non-overlapping feature types |
| `--fraction` | Assign fractional count (1/$k$) to each of $k$ overlapping features | When exact feature assignment is ambiguous |
| `--largestOverlap` | Assign to feature with largest overlap | Simple heuristic for ambiguous cases |

- **Innovation**: Unlike htseq-count (which had fixed overlap resolution), featureCounts makes the strategy configurable, recognizing that different biological questions require different counting approaches.

#### Step 5: Paired-End Read Handling

For paired-end reads, featureCounts counts **fragments** rather than individual reads:

1. Both mates must be properly paired and map to the same chromosome
2. The fragment is defined as the genomic interval from the leftmost aligned base to the rightmost aligned base (accounting for insert size)
3. The fragment (not individual reads) is checked for feature overlap

This avoids double-counting and correctly handles cases where one mate falls in an exon and the other in an intron.

- **Innovation**: Fragment-based counting provides a more accurate representation of the library molecule than read-based counting.

#### Step 6: Meta-Feature Aggregation

featureCounts supports **meta-features**: hierarchical feature relationships where lower-level features (e.g., exons) are aggregated into higher-level features (e.g., genes). The GTF annotation specifies `gene_id` and `transcript_id` attributes; featureCounts sums exon-level counts to gene-level counts.

- **Innovation**: This enables a single run to produce both exon-level and gene-level counts, eliminating the need for separate counting runs and post hoc aggregation scripts.

### Key Algorithmic Contributions

| Innovation | Significance |
|---|---|
| **Chromosome hashing** | ~24× reduction in feature search space for human genome — the single largest speed contributor |
| **Feature blocking** | Additional ~200–1,000× reduction for gene-level counting by limiting detailed overlap checks to small blocks |
| **Streaming BAM processing** | Constant memory usage regardless of dataset size; enables counting on memory-constrained systems |
| **Configurable overlap resolution** | Adapts counting strategy to biological question rather than imposing a single heuristic |
| **Fragment-based paired-end counting** | More accurate than read-based counting for paired-end data |
| **Meta-feature aggregation** | Single-pass counting at multiple annotation levels |
| **C implementation with POSIX threads** | Compiled code + multi-threading for maximum performance |

### Algorithm Complexity

- **Without chromosome hashing**: $O(R \cdot |F|)$ — each read checked against all features
- **With chromosome hashing**: $O(R \cdot |F_{chr}|)$ — each read checked against features on its chromosome only; $|F_{chr}| \approx |F| / 24$
- **With blocking**: $O(R \cdot (1 + \bar{B}))$ where $\bar{B}$ is the average block size (~1–5 features for genes) — reads only undergo detailed overlap checks within one block
- **Memory**: $O(\max(|F_{chr}|) + \text{buffer})$ — depends on largest chromosome, not total read count

### Comparison with Contemporary Methods

| Aspect | featureCounts | htseq-count | BEDTools | summarizeOverlaps |
|--------|---------------|-------------|----------|-------------------|
| **Implementation** | C | Python | C++ | R |
| **Algorithm** | Chromosome hashing + blocking | Naive $O(NR)$ | Interval overlap | Interval overlap |
| **Speed (gene-level)** | >10× faster | Baseline | ~3–5× faster | ~2× slower |
| **Memory** | Low (streaming) | High (loads all reads) | Moderate | High (GAlignment objects) |
| **Multi-threading** | Yes (POSIX threads) | No | Limited | Limited |
| **Multi-mapping** | Configurable | Fixed (discard) | None | Configurable |
| **Paired-end** | Fragment-based | Read-based | Requires scripting | Read-based |
| **Meta-features** | Built-in (exon → gene) | Manual aggregation | Manual | Manual |
| **Annotation format** | GTF, GFF, SAF | GTF, GFF | BED, GTF | GTF via TxDb |

### Limitations of the Algorithm

- **Genome annotation-dependent**: Requires accurate, complete gene annotation (GTF/GFF). Novel genes or unannotated features cannot be counted
- **No transcript-level resolution**: Counts at the gene or exon level, not at the transcript-isoform level — users needing isoform quantification must use Salmon, kallisto, or RSEM
- **Alignment-dependent**: Relies on external alignment (STAR, BWA, etc.); alignment errors propagate to counting
- **Chromosome hashing assumes chromosome-level assembly**: Less effective for highly fragmented assemblies (e.g., thousands of scaffolds)
- **No built-in quality control**: Does not assess whether the library is suitable for counting (e.g., 3' bias, rRNA contamination)
- **No normalization**: Raw counts only; normalization must be performed downstream (DESeq2, edgeR, limma-voom)

---

## 5. Evidence Extraction

| # | Claim | Claim Type | Evidence Level | Supporting Figure | Evidence Object |
|---|-------|-----------|----------------|-------------------|-----------------|
| E1 | featureCounts is an order of magnitude (>10×) faster than htseq-count for gene-level counting | observation | Strong | Fig 1, Table 1 | [[featureCounts-speed-10x]] |
| E2 | featureCounts requires far less memory than htseq-count and summarizeOverlaps | observation | Strong | Fig 1, Table 2 | [[featureCounts-memory-low]] |
| E3 | Chromosome hashing and feature blocking are the primary algorithmic contributions enabling the speedup | method | Strong | Methods, Fig 1 | [[featureCounts-hashing-blocking]] |
| E4 | featureCounts produces equivalent gene-level counts to htseq-count (high concordance, $R^2 > 0.99$) | validation | Strong | Fig 2, Supplementary | [[featureCounts-htseq-concordance]] |
| E5 | featureCounts' paired-end fragment-based counting improves accuracy over read-based counting | method | Moderate | Fig 3 | [[featureCounts-paired-end-fragment]] |
| E6 | featureCounts' multi-mapping read handling strategies affect count distributions differently; user choice is important | observation | Moderate | Fig 4 | [[featureCounts-multimapping-strategies]] |
| E7 | featureCounts supports both RNA-seq and DNA-seq (ChIP-seq, ATAC-seq) counting in a unified framework | method | Moderate | Methods, Supplementary | [[featureCounts-universal]] |
| E8 | featureCounts' meta-feature aggregation (exon → gene) simplifies multi-level counting without separate runs | method | Moderate | Methods | [[featureCounts-meta-features]] |

---

## 6. Knowledge Graph Extraction

### Entities Identified

| Entity | Type | Role |
|--------|------|------|
| featureCounts | method | Core read summarization (counting) program |
| Chromosome Hashing | method | Partitioning reads and features by chromosome |
| Feature Blocking | method | Grouping overlapping features into disjoint blocks |
| Subread | package | Parent software package containing featureCounts and the Subread aligner |
| Rsubread | package | Bioconductor R package providing R interface to featureCounts |
| Read Summarization | concept | Process of assigning aligned reads to genomic features |
| htseq-count | method | Baseline counting tool for comparison |
| BEDTools | method | General-purpose interval overlap tool |
| summarizeOverlaps | method | Bioconductor-based counting method |
| SAM/BAM Format | data_format | Standard alignment format — input to featureCounts |
| GTF/GFF Format | data_format | Gene annotation format — feature definitions |
| SAF (Simplified Annotation Format) | data_format | featureCounts-native tabular annotation format |
| Multi-mapping Reads | concept | Reads mapping to multiple genomic locations |
| Fragment-Based Counting | method | Paired-end counting using insert fragment rather than individual reads |
| Meta-Features | concept | Hierarchical feature aggregation (exons → transcripts → genes) |
| DESeq2 | method | Downstream differential expression tool consuming featureCounts output |
| edgeR | method | Downstream differential expression tool consuming featureCounts output |
| limma-voom | method | Downstream differential expression tool consuming featureCounts output |

### Relationships

| Entity A | Relationship | Entity B | Evidence |
|----------|-------------|----------|----------|
| featureCounts | implements | chromosome hashing | Methods (partition by chromosome) |
| featureCounts | implements | feature blocking | Methods (group overlapping features) |
| Chromosome hashing | reduces search space by | ~24× (human) | Fig 1 (speed improvement) |
| Feature blocking | reduces overlap checks by | ~200–1,000× | Fig 1 |
| featureCounts | is faster than | htseq-count | Fig 1 (>10×) |
| featureCounts | uses less memory than | htseq-count | Table 2 |
| featureCounts | is part of | Subread package | Introduction |
| featureCounts | provides input to | DESeq2, edgeR, limma-voom | Methods (standard workflow) |
| Rsubread | wraps | featureCounts | Introduction (Bioconductor interface) |
| Fragment-based counting | improves accuracy over | read-based counting | Fig 3 (paired-end) |
| Meta-feature aggregation | enables | multi-level counting in one run | Methods |

---

## 7. Critical Evaluation

### Strengths

- **Genuine algorithmic innovation in a neglected step**: Read summarization was treated as trivial, yet featureCounts showed that algorithmic innovation could produce dramatic (>10×) improvements
- **Rigorous benchmarking**: Systematic comparison with htseq-count, BEDTools, and summarizeOverlaps on realistic datasets with multiple metrics (speed, memory, accuracy)
- **Solid C implementation**: Pure C with POSIX threads — compiled, optimized, and fast, unlike Python or R implementations
- **Streaming design**: Memory usage is constant regardless of dataset size — critical for scaling to large projects
- **Configurable and flexible**: Multiple overlap resolution strategies, support for both single-end and paired-end, both RNA-seq and DNA-seq, and multiple annotation formats
- **Ecosystem integration**: As part of Subread, featureCounts is integrated with the Subread aligner; as part of Rsubread, it is integrated with the Bioconductor ecosystem (DESeq2, edgeR, limma)
- **De facto standard status**: featureCounts became the default counting tool in virtually all RNA-seq processing pipelines (nf-core/rnaseq, ENCODE)
- **Meta-feature support**: Built-in handling of gene-exon hierarchies — a practical feature that simplified many workflows

### Weaknesses

- **No transcript-level quantification**: Counting at the gene level loses isoform-resolution information — users must switch to Salmon/kallisto for isoform analysis
- **Annotation-dependent**: Completely dependent on the quality and completeness of gene annotations; novel genes, unannotated isoforms, or poorly annotated organisms are problematic
- **No statistical model for count uncertainty**: Unlike RSEM or Salmon (which use expectation-maximization with probabilistic models), featureCounts produces hard assignment counts without uncertainty estimates
- **Strand-specificity handling could be confusing**: The `-s` parameter (stranded, reverse-stranded, unstranded) was sometimes misinterpreted by users, leading to incorrect counting
- **Multi-mapping resolution is heuristic**: No probabilistic framework for assigning multi-mapped reads; the choice of strategy can affect results, and no systematic guidance was provided on when to use which strategy
- **Limited quality control**: No built-in diagnostics for assessing counting quality (e.g., proportion of reads assigned, feature body coverage, 3' bias)
- **Speed gains are workflow-specific**: The 10× speedup was most dramatic for gene-level counting; for exon-level or custom features, the relative improvement was smaller

### Missing Controls

- No comparison of downstream differential expression results using featureCounts vs. htseq-count counts — do the different counting tools lead to different DE gene lists?
- No evaluation of counting accuracy on simulated data with known true counts (similar to what was done for differential expression methods)
- No assessment of the impact of annotation version/quality on counting results
- No comparison with transcript-level quantification methods (RSEM, eXpress) for gene-level aggregate counts
- No evaluation of counting accuracy for overlapping genes on opposite strands — a known challenge

---

## 8. Research Insight

### What Changed After This Paper

- **featureCounts became the standard RNA-seq counting tool**: Integrated into all major pipelines (nf-core/rnaseq, ENCODE, GTEx), featureCounts is the default counting method in most RNA-seq workflows
- **Read summarization became a solved problem**: After featureCounts, the community stopped debating how to count reads and converged on a standard approach — simplifying reproducibility across studies
- **The Subread ecosystem was established**: featureCounts, together with the Subread aligner, created a complete alignment + counting pipeline that rivalled the STAR + featureCounts combination
- **Rsubread brought fast counting to R**: The Rsubread Bioconductor package made featureCounts' speed available within R, reducing the need for external tool calls and enabling more integrated workflows
- **Counting speed was no longer a bottleneck**: Differential expression pipelines could process hundreds of samples without the counting step being the rate-limiting factor
- **Multi-mapping awareness increased**: featureCounts' multiple strategies for handling multi-mapped reads raised awareness that this choice could affect results, spurring investigation into optimal strategies

### How It Connects to Current Knowledge

- featureCounts is part of the **standard RNA-seq workflow**: STAR alignment → featureCounts counting → DESeq2/edgeR differential expression. This pipeline is the most common analysis pathway in RNA-seq
- **nf-core/rnaseq** uses featureCounts as the default quantification engine, processing >10,000 public datasets through this pipeline
- The **Bioconductor ecosystem** includes featureCounts via Rsubread, enabling interactive R-based counting within the same session as downstream analysis
- **Single-cell RNA-seq** introduced new counting challenges (UMI-based counting) that featureCounts was not designed for, but STARsolo and Cell Ranger adopted similar algorithmic principles
- **Long-read RNA-seq** has revived interest in read summarization for full-length transcripts, but featureCounts' exon-overlap counting is less relevant for isoform-resolution analysis
- featureCounts demonstrated that **algorithmic optimization of "solved" problems** can have enormous practical impact — a lesson applicable across bioinformatics

---

## 9. Future Research Opportunities

- **Transcript-level featureCounts**: Extend the chromosome hashing + blocking approach to transcript-level counting, competing with Salmon/kallisto on speed for isoform quantification
- **UMI-aware counting**: Adapt the algorithm for single-cell RNA-seq with unique molecular identifiers (UMIs), handling the additional UMI deduplication step efficiently
- **Long-read featureCounts**: Counting support for PacBio and ONT long reads, where reads span multiple exons and the overlap logic is fundamentally different
- **Probabilistic featureCounts**: Incorporate a statistical model of multi-mapping uncertainty, producing posterior count distributions rather than hard assignments
- **GPU-accelerated featureCounts**: Port the overlap detection and counting to GPU for ultra-fast counting on massive datasets (hundreds of thousands of single cells)
- **Quality control integration**: Built-in QC metrics (read assignment rates, feature body coverage, 5'/3' bias) as part of the counting output
- **Annotation-free counting**: Counting against k-mer sets or transcriptome references without requiring full GTF annotation — useful for non-model organisms
- **Streaming featureCounts**: Counting reads as they are aligned, eliminating the need to write and re-read BAM files — an integrated alignment + counting pipeline
- **Multi-omics counting**: Unified counting for RNA-seq, ATAC-seq, ChIP-seq, and CUT&RUN, with modality-appropriate overlap logic
- **Cloud-native featureCounts**: Counting as a service, with BAM files streamed from cloud storage and counts stored in cloud-native formats (TileDB, Zarr)
