---
type: evidence
claim: "CCA integration aligns human and mouse pancreatic islet scRNA-seq datasets revealing conserved cell states"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Homo sapiens
  - Mus musculus
tissue:
  - pancreatic islet
cell_type:
  - alpha cells
  - beta cells
  - delta cells
  - PP cells
development_stage:
  - adult
condition:
  - standard
support:
  - "[[xr-10-1038-nbt-4096]]"
supporting_figures:
  - "xr-10-1038-nbt-4096#figure-4"
experiments:
  - CCA integration
  - cross-species scRNA-seq
  - cell-type homology assessment
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# CCA Integration Aligns Human and Mouse Pancreatic Islet Data

## Claim

Seurat v2's CCA-based integration framework successfully aligns human and mouse pancreatic islet scRNA-seq datasets into a shared latent space, revealing conserved transcriptional programs in alpha, beta, delta, and PP cells across ~75 million years of evolutionary divergence.

## Methodological Context

Cross-species scRNA-seq alignment is challenging because of gene orthology drift, differences in expression levels, and cell-type composition. Seurat v2 addresses this by performing CCA on orthologous genes, identifying shared correlation structures that correspond to conserved cell-type programs regardless of species-level expression differences.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-nbt-4096]] | CCA cross-species integration | Human and mouse islet cells cluster by cell type, not species; conserved programs identified | 2 species, 4 conserved cell types |

## Evidence Quality

**Tier 1** — Computational method with strong biological ground truth (well-characterized islet cell types)

## Contradictory Evidence

None. The clustering-by-cell-type-not-species pattern is widely reproduced.

## Consensus Assessment

**Established** — Cross-species CCA integration is a widely used approach for evolutionary cell biology.

## Alternative Models

SAMap, SATURN, and homology-based gene set conversion offer alternatives for cross-species alignment.

## Open Questions

- Can CCA detect species-specific cell types or states?
- How does orthology mapping quality affect integration results?

## Next Critical Experiment

Compare CCA cross-species alignment with recently evolved tissues (e.g., primate-specific brain regions) to identify evolutionary innovations.
