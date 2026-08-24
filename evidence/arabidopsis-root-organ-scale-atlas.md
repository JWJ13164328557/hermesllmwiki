---
type: evidence
claim: "An organ-scale Arabidopsis root atlas captures spatiotemporal gene expression at single-cell resolution"
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
  - "[[xr-10-1016-j-devcel-2022-01-008]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2022-01-008#figure-1"
experiments:
  - scRNA-seq
  - spatial reconstruction
  - trajectory inference
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Organ-Scale Arabidopsis Root Atlas at Single-Cell Resolution

## Claim

A comprehensive organ-scale single-cell atlas of the Arabidopsis root integrates scRNA-seq with spatial reconstruction to capture gene expression across all cell types, developmental stages, and longitudinal root zones at unprecedented resolution.

## Biological Context

Previous root scRNA-seq studies profiled root tips only. This atlas extends to the entire organ, capturing maturing and differentiated cell states along the longitudinal axis, providing a complete transcriptomic picture of root development.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2022-01-008]] | 10x scRNA-seq + spatial reconstruction (novoSpaRc) | Complete root atlas with all major cell types across developmental zones; >25 cell clusters including differentiation intermediates | Organ-scale (tens of thousands) |

## Evidence Quality

**Tier 3** — Spatial Support (gene expression mapped to spatial coordinates via computational reconstruction; validated with known spatial markers)

## Contradictory Evidence

None. The atlas is consistent with and extends prior root scRNA-seq datasets.

## Consensus Assessment

**Established** — Most comprehensive root atlas to date; represents the current reference standard for the field.

## Alternative Models

N/A — This is a descriptive resource, not a mechanistic model.

## Open Questions

- How well does computational spatial reconstruction match physical spatial transcriptomics (e.g., MERFISH, Stereo-seq)?
- Can the atlas capture stress-responsive cell states?
- How generalizable is the atlas to different growth conditions?

## Next Critical Experiment

Integration of the atlas with spatial transcriptomics methods to validate computational spatial assignments and achieve subcellular resolution of gene expression patterns.
