---
type: evidence
claim: "featureCounts is an order of magnitude faster than existing read summarization methods"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - multiple
tissue:
  - not applicable
cell_type:
  - not applicable
development_stage:
  - not applicable
condition:
  - standard
support:
  - "[[featurecounts-an-efficient-general-purpose-program-for-assigning-seque]]"
supporting_figures:
  - "xr-10-1093-bioinformatics-btt656#figure-3"
  - "xr-10-1093-bioinformatics-btt656#figure-4"
experiments:
  - read counting
  - speed benchmarking
contradictions: []
contradiction_type: null
updated: "2026-05-29"
doi: "10.1093/bioinformatics/btt656"
evidence_type: "descriptive/observational"
evidence_type_basis: "rule-v9-20261107"
evidence_type_confidence: "low"
quality: "low"
quality_basis: "rule-v9-20261107"
tags: [methods-tools]
theme_status: mapped
theme_basis: keyword
claim_role: "finding"
non_finding_kind: ""
evidence_type_prior: ""

---

# featureCounts Is an Order of Magnitude Faster Than Other Summarization Methods

## Claim

featureCounts, a read summarization program that assigns mapped sequencing reads to genomic features, is an order of magnitude faster than existing methods (htseq-count, BEDTools, multicov) while producing nearly identical count results.

## Methodological Context

After alignment, RNA-seq reads must be counted against gene annotations for downstream differential expression analysis. This step was a major computational bottleneck. featureCounts achieves its speed through efficient chromosome-by-chromosome processing that minimizes disk I/O and avoids maintaining the entire alignment file in memory.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[featurecounts-an-efficient-general-purpose-program-for-assigning-seque]] | featureCounts benchmark | 10–30× faster than htseq-count; comparable accuracy; minimal memory footprint | Multiple RNA-seq datasets |

## Evidence Quality

**Tier 1** — Systematic benchmark with reproducible metrics

## Contradictory Evidence

None. featureCounts performance advantage is consistently observed.

## Consensus Assessment

**Established** — featureCounts is the default counting method in the subread package and widely used in RNA-seq pipelines.

## Alternative Models

htseq-count, Salmon/Alevin (alignment-free), and genomic ranges-based counting in R are alternatives.

## Open Questions

- Does featureCounts' advantage persist with single-cell UMI-deduplicated BAM files?
- How well does it handle overlapping genes on opposite strands?

## Next Critical Experiment

Benchmark featureCounts against alignment-free quantification (Salmon/Alevin) for single-cell UMI count matrices.
