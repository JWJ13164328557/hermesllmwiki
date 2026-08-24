---
type: evidence
claim: "snRNA-seq uncovers additional root cell subtypes not identified by protoplast-based scRNA-seq"
claim_type: observation
status: reviewed
consensus_level: emerging
confidence: medium
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
  - "[[xr-10-1016-j-molp-2021-01-001]]"
supporting_figures:
  - "xr-10-1016-j-molp-2021-01-001#figure-2"
experiments:
  - snRNA-seq
  - clustering
  - sub-clustering
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# snRNA-seq Uncovers Additional Root Cell Subtypes

## Claim

snRNA-seq of Arabidopsis roots identifies cell subtypes (e.g., trichoblast subpopulations within the epidermis) that were not resolved by protoplast-based scRNA-seq, suggesting that dissociation methods can mask biologically relevant heterogeneity.

## Biological Context

Protoplasting involves enzymatic cell wall digestion that may selectively lose fragile cell types or induce transcriptional changes that obscure subtle subtype distinctions. snRNA-seq avoids these artifacts, potentially providing a more complete view of cellular diversity.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2021-01-001]] | snRNA-seq sub-clustering | Additional epidermal subtypes and rare populations detected that were not found in matched scRNA-seq | Thousands of nuclei |

## Evidence Quality

**Tier 4** — Computational Inference (subtype discovery based on clustering resolution; independent spatial validation needed)

## Contradictory Evidence

None directly. However, subtype detection is highly sensitive to clustering parameters, and reproducibility across independent datasets is needed.

## Consensus Assessment

**Emerging** — Promising finding from one study; requires validation in independent datasets and with spatial methods.

## Alternative Models

The additional subtypes may reflect transient transcriptional states captured by snRNA-seq rather than stable cell types; or they may be artifacts of nuclear transcript sampling.

## Open Questions

- Are these additional subtypes stable or transient?
- Do they exist in intact tissue by spatial validation?
- Are similar subtypes found in other plant species?

## Next Critical Experiment

Spatial transcriptomics or single-molecule FISH to confirm that snRNA-seq-identified subtypes correspond to spatially distinct cell populations in intact roots.
