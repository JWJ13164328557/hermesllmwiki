---
type: evidence
claim: "Multimodal WNN analysis identifies previously unreported lymphoid subpopulations"
claim_type: observation
status: reviewed
consensus_level: emerging
confidence: medium
species:
  - Homo sapiens
tissue:
  - peripheral blood
  - bone marrow
cell_type:
  - lymphoid cells
development_stage:
  - adult
condition:
  - standard
support:
  - "[[integrated-analysis-of-multimodal-single-cell-data]]"
supporting_figures:
  - "xr-10-1016-j-cell-2021-04-048#figure-4"
  - "xr-10-1016-j-cell-2021-04-048#figure-5"
experiments:
  - CITE-seq
  - WNN analysis
  - differential expression
contradictions: []
contradiction_type: null
updated: "2026-05-29"
doi: "10.1016/j.cell.2021.04.048"
evidence_type: "omics/co-occurrence"
evidence_type_basis: "rule-v9-20261107"
evidence_type_confidence: "medium"
quality: "medium"
quality_basis: "rule-v9-20261107"
tags: [single-cell-spatial-omics]
theme_status: mapped
theme_basis: keyword
claim_role: "finding"
non_finding_kind: "result"
evidence_type_prior: ""

---

# Multimodal WNN Identifies Novel Lymphoid Subpopulations

## Claim

Seurat v4's WNN analysis of multimodal CITE-seq data reveals previously unreported lymphoid subpopulations that are not detectable by transcriptome-only or protein-only analyses, demonstrating the added value of joint multimodal analysis for cell-type discovery.

## Methodological Context

Lymphoid cell populations, particularly innate lymphoid cells (ILCs) and transitional B cell states, can be difficult to resolve because transcriptional differences may be subtle while protein-level differences are more pronounced. WNN's ability to weight modalities per cell allows it to detect populations that are supported by one modality more than the other.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[integrated-analysis-of-multimodal-single-cell-data]] | WNN multimodal analysis | Novel CD8+ T cell subsets and transitional B cell states identified; validated by independent protein markers | 211K PBMCs + bone marrow cells |

## Evidence Quality

**Tier 2** — Computational discovery with protein marker validation

## Contradictory Evidence

Awaiting independent replication. The subpopulations require validation in external cohorts.

## Consensus Assessment

**Emerging** — Single-study finding requiring replication in independent datasets.

## Alternative Models

The subpopulations may represent continuous differentiation states rather than discrete cell types.

## Open Questions

- Do these subpopulations exist in vivo or are they artifacts of the CITE-seq assay?
- What are the functional roles of these newly identified populations?

## Next Critical Experiment

Validate novel populations by flow cytometry with the defining surface markers, and test functional properties in vitro.
