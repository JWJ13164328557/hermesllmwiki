---
type: evidence
claim: "Arabidopsis root contains at least 15 transcriptionally distinct cell types detectable by scRNA-seq"
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
  - seedling (5-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[xr-10-1016-j-molp-2019-04-004]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-1"
  - "xr-10-1104-pp-18-01482#figure-1"
experiments:
  - scRNA-seq
  - clustering
  - marker gene validation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Arabidopsis Root Has ≥15 Transcriptionally Distinct Cell Types

## Claim

Single-cell RNA-seq of Arabidopsis root resolves at least 15 transcriptionally distinct cell populations, covering all major cell types (epidermis, cortex, endodermis, pericycle, stele, columella, lateral root cap, quiescent center) and developmental stages.

## Biological Context

The Arabidopsis root has a stereotyped radial organization with concentric cell layers surrounding the vasculature. Prior to scRNA-seq, cell-type resolution required reporter lines or microdissection. This evidence establishes the baseline cell-type diversity detectable by transcriptomic profiling.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2019-02-022]] | 10x scRNA-seq | 15 clusters, all major types + QC | 4,727 |
| [[xr-10-1104-pp-18-01482]] | 10x scRNA-seq | All major tissues, rare QC population | >10,000 |
| [[xr-10-1016-j-molp-2019-04-004]] | 10x scRNA-seq | 24 putative clusters | ~7,500 |

## Evidence Quality

**Tier 3** — Spatial Support (scRNA-seq with known marker validation)

## Contradictory Evidence

None. All studies consistently identify the same major cell types.

## Consensus Assessment

**Established** — Confirmed by 3+ independent studies using different protocols and analysis pipelines.

## Alternative Models

N/A — This is a descriptive observation, not a mechanistic claim.

## Open Questions

- What is the optimal clustering resolution for root scRNA-seq data?
- Do protoplasting-based methods introduce cell-type biases?
- Are there additional rare cell types below current detection limits?

## Next Critical Experiment

Spatial transcriptomics (Stereo-seq/MERFISH) to validate that transcriptional clusters correspond to spatially defined cell types without dissociation bias.
