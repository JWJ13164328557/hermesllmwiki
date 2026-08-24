---
type: evidence
claim: "scRNA-seq resolves major cell types in rice root tips across two agronomically important cultivars"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Oryza sativa
tissue:
  - root tip
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2020-12-014]]"
supporting_figures:
  - "xr-10-1016-j-molp-2020-12-014#figure-1"
experiments:
  - scRNA-seq
  - clustering
  - marker gene annotation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# scRNA-seq Resolves Major Cell Types in Rice Root Tips

## Claim

Single-cell RNA-seq of root tips from two agronomically important rice cultivars (Nipponbare and Azucena) resolves major cell types including epidermis, cortex, endodermis, exodermis, sclerenchyma, stele, and root cap, demonstrating that monocot root cell-type diversity is accessible by droplet-based scRNA-seq.

## Biological Context

Rice has a fibrous root system with a distinct anatomy compared to dicot taproots, including an exodermis layer and sclerenchyma fibers. This study established the first single-cell transcriptomic atlas of rice roots, enabling cross-species comparisons with Arabidopsis.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2020-12-014]] | 10x scRNA-seq | Major cell types resolved in both Nipponbare and Azucena cultivars | 27,469 (Nipponbare), ~10,000 (Azucena) |

## Evidence Quality

**Tier 3** — Spatial Support (scRNA-seq with known marker validation)

## Contradictory Evidence

None. Cell-type resolution is consistent with expectations from rice root anatomy.

## Consensus Assessment

**Established** — Major cell types independently identified in two genetically distinct cultivars with conserved transcriptional signatures.

## Alternative Models

N/A — This is a descriptive observation of cell-type diversity.

## Open Questions

- Are there additional rare cell types in rice roots below current detection limits?
- How do cell-type proportions change across different root zones?
- What is the transcriptomic distinction between exodermis and other outer cell layers?

## Next Critical Experiment

Spatial transcriptomics or multiplexed in situ hybridization to confirm the spatial localization of computationally defined rice root cell clusters.
