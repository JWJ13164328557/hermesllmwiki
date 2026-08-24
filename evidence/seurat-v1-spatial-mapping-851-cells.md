---
type: evidence
claim: "Seurat v1 spatially maps 851 dissociated zebrafish embryo cells using in situ reference patterns"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Danio rerio
tissue:
  - whole embryo
cell_type:
  - embryonic cells
development_stage:
  - mid-gastrula to early somitogenesis (shield to 3-somite)
condition:
  - standard
support:
  - "[[xr-10-1038-nbt-3192]]"
supporting_figures:
  - "xr-10-1038-nbt-3192#figure-2"
  - "xr-10-1038-nbt-3192#figure-3"
experiments:
  - scRNA-seq
  - spatial mapping
  - in situ hybridization validation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Seurat v1 Spatially Maps 851 Zebrafish Embryo Cells

## Claim

Seurat v1 reconstructs the spatial origin of 851 dissociated zebrafish embryo cells by integrating scRNA-seq profiles with a reference map of 47 landmark genes from whole-mount in situ hybridization patterns.

## Methodological Context

Spatial information is typically lost during tissue dissociation for scRNA-seq. Seurat v1 introduced a computational framework that infers the spatial location of each cell by comparing its transcriptome to a binarized in situ reference, assigning cells to spatial domains based on the posterior probability of expression pattern matching.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-nbt-3192]] | Seurat spatial inference | 851 cells mapped to 9 spatial domains with 92% agreement to manual annotation | 851 cells, 47 in situ genes |

## Evidence Quality

**Tier 1** — Computational method with experimental validation (in situ hybridization ground truth)

## Contradictory Evidence

None. The approach was validated against manual annotation of in situ patterns.

## Consensus Assessment

**Established** — Foundational method that pioneered computational spatial reconstruction in scRNA-seq.

## Alternative Models

Alternative spatial reconstruction methods include novoSpaRc and DistMap.

## Open Questions

- How does performance degrade with fewer landmark genes?
- Can the approach generalize to tissues lacking comprehensive in situ atlases?

## Next Critical Experiment

Benchmark Seurat spatial mapping against spatially resolved transcriptomics (Stereo-seq/MERFISH) in the same tissue.
