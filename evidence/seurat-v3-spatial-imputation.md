---
type: evidence
claim: "scRNA-seq integration with in situ data enables transcriptome-wide spatial imputation"
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
  - shield to early somitogenesis
condition:
  - standard
support:
  - "[[comprehensive-integration-of-single-cell-data]]"
experiments:
  - scRNA-seq
  - spatial mapping
  - transcriptome imputation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
doi: "10.1016/j.cell.2019.05.031"
needs_review: "supporting_figures removed: previously pointed at the UMAP paper (10.1038/nbt.4314) instead of the Seurat v3 source; verify figure indices"
evidence_type: "omics/co-occurrence"
evidence_type_basis: "rule-v9-20261107"
evidence_type_confidence: "medium"
quality: "medium"
quality_basis: "rule-v9-20261107"
tags: [single-cell-spatial-omics]
theme_status: mapped
theme_basis: keyword
claim_role: "finding"
non_finding_kind: ""
evidence_type_prior: ""

---

# scRNA-seq Integration With in situ Data Enables Spatial Imputation

## Claim

Seurat v3 integrates scRNA-seq data with in situ hybridization patterns to impute transcriptome-wide spatial expression maps, predicting the spatial location of every gene profiled by scRNA-seq, not just the landmark genes with in situ data.

## Methodological Context

Spatial transcriptomics methods are limited by either gene throughput (in situ hybridization) or spatial resolution (array-based capture). Seurat v3's integration approach bridges this gap: it learns a mapping between scRNA-seq transcriptomes and spatial landmark genes via anchor-based transfer, then imputes the spatial expression of all other genes.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[dimensionality-reduction-for-visualizing-single-cell-data-using-umap]] | Anchor-based spatial imputation | Spatial expression of 12,000+ genes imputed across the zebrafish embryo; validated by independent in situ patterns | ~851 cells mapped, >12K genes imputed |

## Evidence Quality

**Tier 1** — Computational method with experimental validation (independent in situ hybridizations confirm imputed patterns)

## Contradictory Evidence

None. Imputed patterns were validated against known expression patterns.

## Consensus Assessment

**Established** — Spatial imputation is a core use case for anchor-based integration in Seurat.

## Alternative Models

Tangram, novoSpaRc, and DistMap offer alternative approaches to spatial transcriptome imputation.

## Open Questions

- How does imputation accuracy vary with tissue complexity and cell density?
- Can co-expression-based imputation capture spatial patterns absent from the landmark set?

## Next Critical Experiment

Systematic comparison of imputation accuracy using spatial transcriptomics (Merfish/Stereo-seq) as ground truth.
