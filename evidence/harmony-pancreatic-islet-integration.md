---
type: evidence
claim: "Harmony integrates five pancreatic islet scRNA-seq studies into a unified embedding by cell type"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Homo sapiens
tissue:
  - pancreatic islet
cell_type:
  - alpha cells
  - beta cells
  - delta cells
  - PP cells
  - acinar cells
  - ductal cells
development_stage:
  - adult
condition:
  - standard
support:
  - "[[xr-10-1038-s41592-019-0619-0]]"
supporting_figures:
  - "xr-10-1038-s41592-019-0619-0#figure-1"
  - "xr-10-1038-s41592-019-0619-0#figure-2"
experiments:
  - scRNA-seq integration
  - Harmony embedding
  - batch correction benchmarking
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Harmony Integrates Five Pancreatic Islet Studies Into a Unified Embedding

## Claim

Harmony integrates scRNA-seq data from five independent pancreatic islet studies (generated with different protocols: inDrop, CEL-Seq2, Smart-seq2, SMARTer, Fluidigm C1) into a unified low-dimensional embedding where cells cluster by cell type rather than by study of origin.

## Methodological Context

Pancreatic islet scRNA-seq datasets from different labs show strong batch effects due to differences in cell isolation, library preparation, and sequencing platforms. Harmony iteratively corrects PCA embeddings by soft-clustering cells and applying dataset-specific corrections that remove batch effects while preserving biological cell-type distinctions.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-s41592-019-0619-0]] | Harmony integration | Cells cluster by cell type (alpha, beta, delta, PP, acinar, ductal) across 5 studies with different protocols | 5 datasets, 6+ cell types, ~15K cells |

## Evidence Quality

**Tier 1** — Computational method with strong biological ground truth (well-characterized islet cell types)

## Contradictory Evidence

None. Harmony outperformed MNN, BBKNN, and CCA in this benchmark.

## Consensus Assessment

**Established** — Harmony is one of the most widely used scRNA-seq integration methods.

## Alternative Models

Seurat CCA/anchor-based, BBKNN, Scanorama, and LIGER are primary alternatives.

## Open Questions

- At what point does biological variation overwhelm the correction?
- How does Harmony handle datasets with largely non-overlapping cell types?

## Next Critical Experiment

Test Harmony integration on tissues with continuous differentiation gradients rather than discrete cell types.
