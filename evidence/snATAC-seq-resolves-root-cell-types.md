---
type: evidence
claim: "snATAC-seq resolves Arabidopsis root cell types based on differential chromatin accessibility"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2021-01-001]]"
supporting_figures:
  - "xr-10-1016-j-molp-2021-01-001#figure-1"
experiments:
  - snATAC-seq
  - clustering
  - chromatin accessibility profiling
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# snATAC-seq Resolves Arabidopsis Root Cell Types by Chromatin Accessibility

## Claim

Single-nucleus ATAC-seq (snATAC-seq) of Arabidopsis roots resolves major cell types based on differential chromatin accessibility profiles, demonstrating that the regulatory landscape is cell-type-specific and sufficient for cell-type classification.

## Biological Context

While scRNA-seq captures the transcriptome, snATAC-seq captures the regulatory landscape — which regions of the genome are accessible for transcription factor binding in each cell type. This provides complementary information about the gene regulatory networks underlying cell identity.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2021-01-001]] | snATAC-seq (combinatorial indexing) | ~15 cell types resolved; chromatin accessibility profiles cluster by cell type and correlate with known marker gene promoters | Thousands of nuclei |

## Evidence Quality

**Tier 3** — Spatial Support (cell-type assignment validated by accessibility at known marker gene loci)

## Contradictory Evidence

None. Cell-type resolution by snATAC-seq is consistent with scRNA-seq-based cell-type classifications.

## Consensus Assessment

**Established** — Single study demonstrates clear cell-type resolution; the principle that chromatin accessibility is cell-type-specific is well-established from mammalian systems.

## Alternative Models

N/A — This is a descriptive observation of cell-type-resolved chromatin accessibility.

## Open Questions

- What is the resolution limit of snATAC-seq compared to scRNA-seq for discriminating closely related cell types?
- How does chromatin accessibility change across developmental trajectories within a cell type?
- What fraction of accessible peaks are cell-type-specific vs shared?

## Next Critical Experiment

Multiome (simultaneous snRNA-seq + snATAC-seq) in the same nuclei to directly link chromatin accessibility to gene expression at single-cell resolution in plants.
