---
type: evidence
claim: "Mouse Organogenesis Cell Atlas defines hundreds of cell types across E9.5-E13.5 development"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Mus musculus
tissue:
  - whole embryo
cell_type:
  - hundreds of cell types
development_stage:
  - E9.5
  - E10.5
  - E11.5
  - E12.5
  - E13.5
condition:
  - standard
support:
  - "[[xr-10-1038-s41586-019-0969-x]]"
supporting_figures:
  - "xr-10-1038-s41586-019-0969-x#figure-1"
  - "xr-10-1038-s41586-019-0969-x#figure-2"
experiments:
  - sci-RNA-seq3
  - clustering
  - cell-type annotation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Mouse Organogenesis Cell Atlas Defines Hundreds of Cell Types

## Claim

The Mouse Organogenesis Cell Atlas (MOCA) provides a single-cell transcriptomic survey of mouse development from E9.5 to E13.5, defining hundreds of transcriptionally distinct cell types across all major organ systems and germ layers.

## Methodological Context

Mammalian organogenesis involves the coordinated emergence of diverse cell types from the three germ layers. MOCA used combinatorial indexing (sci-RNA-seq3) to profile ~2 million cells from 61 mouse embryos across 5 developmental stages, enabling systematic cataloging of cell-type diversity during the peak of organ formation.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-s41586-019-0969-x]] | sci-RNA-seq3 | Hundreds of cell types identified across E9.5–E13.5; covers all major organ systems and germ layers | ~2M cells, 61 embryos, 5 timepoints |

## Evidence Quality

**Tier 3** — Large-scale observational atlas

## Contradictory Evidence

None. The atlas has been independently validated and used extensively as a reference.

## Consensus Assessment

**Established** — MOCA is a foundational reference for mammalian developmental biology.

## Alternative Models

N/A — This is a descriptive atlas, not a mechanistic model.

## Open Questions

- How many cell types remain undiscovered at deeper sequencing depths?
- What is the spatial organization of newly identified cell types?

## Next Critical Experiment

Spatially resolved transcriptomics of mouse embryos at matching developmental stages to assign spatial coordinates to MOCA cell types.
