---
type: evidence
claim: "Cell-type transcriptional programs are well conserved between the two rice cultivars"
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
  - "xr-10-1016-j-molp-2020-12-014#figure-3"
experiments:
  - scRNA-seq
  - cross-dataset integration
  - correlation analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Cell-Type Transcriptional Programs Conserved Between Rice Cultivars

## Claim

Comparison of scRNA-seq data from Nipponbare (japonica) and Azucena (japonica) rice cultivars shows high conservation of cell-type transcriptional programs, indicating that root cell-type identity is robust across genetic backgrounds.

## Biological Context

Cultivar-level variation could affect cell-type transcriptomic signatures. Demonstrating conservation validates the generalizability of cell-type atlases and supports cross-cultivar transfer of functional genomic knowledge.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2020-12-014]] | Cross-cultivar integration (CCA, LIGER) | Cell-type transcriptomes highly correlated between Nipponbare and Azucena; same major clusters identified in both | 27,469 + ~10,000 |

## Evidence Quality

**Tier 3** — Spatial Support (cell-type identity confirmed by conserved marker expression in both cultivars)

## Contradictory Evidence

None. High conservation was observed across all major cell types.

## Consensus Assessment

**Established** — Two-cultivar comparison shows robust conservation, consistent with expectations of strong developmental constraint on cell-type identity.

## Alternative Models

N/A — Conservation is a descriptive observation. Functional divergence, if any, likely lies in quantitative trait loci rather than qualitative cell-type identity.

## Open Questions

- Would cell-type conservation hold across more divergent rice subspecies (indica vs japonica)?
- Are there cultivar-specific cell subtypes or proportions?
- Do stress-responsive genes show cultivar-specific expression within shared cell types?

## Next Critical Experiment

Multi-cultivar scRNA-seq including indica and wild rice accessions to test whether cell-type transcriptional conservation extends across the Oryza genus.
