---
type: evidence
claim: "Harmony integrates scRNA-seq with spatial transcriptomics data enabling cross-modality analysis"
claim_type: method
status: reviewed
consensus_level: emerging
confidence: medium
species:
  - multiple
tissue:
  - multiple
cell_type:
  - multiple
development_stage:
  - multiple
condition:
  - standard
support:
  - "[[xr-10-1038-s41592-019-0619-0]]"
supporting_figures:
  - "xr-10-1038-s41592-019-0619-0#figure-5"
experiments:
  - cross-modality integration
  - spatial transcriptomics
  - Harmony
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Harmony Integrates scRNA-seq With Spatial Transcriptomics Data

## Claim

Harmony can integrate scRNA-seq data with spatial transcriptomics data, creating a unified embedding that enables mapping of dissociated cell transcriptomes to spatial locations and cross-modality analysis of tissue organization.

## Methodological Context

Spatial transcriptomics methods (Slide-seq, Visium) provide gene expression with spatial context but often at lower resolution or gene coverage than scRNA-seq. Integrating these modalities allows high-resolution cell-type annotation of spots and imputation of spatial gene expression patterns across the full transcriptome.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-s41592-019-0619-0]] | Harmony cross-modality | scRNA-seq and spatial transcriptomics data integrated; cell-type annotations transferred to spatial coordinates | Multiple tissue types |

## Evidence Quality

**Tier 2** — Computational demonstration with biological plausibility

## Contradictory Evidence

None reported, but systematic benchmarks of cross-modality integration quality are limited.

## Consensus Assessment

**Emerging** — Cross-modality integration with Harmony is feasible but requires further benchmarking.

## Alternative Models

Tangram, cell2location, RCTD, and stereoscope are specialized scRNA-seq-to-spatial mapping methods.

## Open Questions

- Does Harmony outperform specialized spatial mapping methods for cell-type deconvolution?
- How does integration quality vary with spatial resolution and gene coverage?

## Next Critical Experiment

Benchmark Harmony against Tangram and cell2location for cell-type deconvolution in spatial transcriptomics using matched scRNA-seq and MERFISH ground truth.
