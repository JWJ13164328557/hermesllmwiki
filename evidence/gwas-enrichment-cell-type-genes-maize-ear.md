---
type: evidence
claim: "GWAS signals for crop yield traits enrich in cell-type-specific gene sets from scRNA-seq"
claim_type: observation
status: reviewed
consensus_level: emerging
confidence: medium
species:
  - Zea mays
tissue:
  - developing ear
cell_type:
  - inflorescence meristem
  - spikelet pair meristem
  - floral meristem
development_stage:
  - early reproductive
condition:
  - field-grown
support:
  - "[[xr-10-1016-j-devcel-2020-12-015]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2020-12-015#figure-4"
experiments:
  - GWAS enrichment
  - scRNA-seq
  - cell-type-specific gene set analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# GWAS Signals for Yield Traits Enrich in Cell-Type-Specific Gene Sets

## Claim

Genome-wide association study (GWAS) signals for maize yield-related traits (kernel row number, ear length) are enriched in cell-type-specific gene sets derived from scRNA-seq, linking crop trait genetics to specific meristem cell populations.

## Biological Context

Linking GWAS loci — which are often in non-coding regions — to causal cell types and genes is a major challenge in crop genomics. scRNA-seq enables testing whether trait-associated variants preferentially affect genes expressed in specific cell types.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2020-12-015]] | GWAS enrichment (MAGMA) of cell-type-specific gene sets | Kernel row number GWAS signals enriched in SPM genes; ear length signals enriched in IM genes | ~12,500 (scRNA-seq) |

## Evidence Quality

**Tier 4** — Computational Inference (statistical enrichment; causal validation of individual loci not performed)

## Contradictory Evidence

None reported. Enrichment is statistically significant but effect sizes for individual loci are small (polygenic traits).

## Consensus Assessment

**Emerging** — Single study demonstrates the principle; requires replication in independent GWAS cohorts and functional validation of specific loci.

## Alternative Models

GWAS enrichment could reflect linkage disequilibrium rather than causal cell-type-specific effects. Alternatively, broadly expressed genes in enriched gene sets could drive the signal.

## Open Questions

- Which specific GWAS loci act through cell-type-specific regulatory elements?
- Do similar enrichments hold for other tissues and traits?
- Can cell-type-specific gene networks predict causal genes for GWAS loci?

## Next Critical Experiment

CRISPR editing of candidate GWAS-linked regulatory elements in specific meristem types to test causal effects on ear architecture traits.
