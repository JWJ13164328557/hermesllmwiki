---
type: evidence
claim: "FACS-sorted RNA-seq independently validates scRNA-seq cluster annotations in maize ears"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Zea mays
tissue:
  - developing ear
cell_type:
  - inflorescence meristem
  - spikelet pair meristem
  - developing vasculature
development_stage:
  - early reproductive
condition:
  - field-grown
support:
  - "[[xr-10-1016-j-devcel-2020-12-015]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2020-12-015#figure-3"
experiments:
  - FACS
  - bulk RNA-seq
  - scRNA-seq
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# FACS-Sorted RNA-seq Independently Validates scRNA-seq Clusters

## Claim

Fluorescence-activated cell sorting (FACS) of maize ear cell populations using reporter lines, followed by bulk RNA-seq, independently validates scRNA-seq cluster annotations by confirming that sorted populations express the expected marker gene sets.

## Biological Context

scRNA-seq cluster annotation can be subjective. Orthogonal validation by FACS-based enrichment of known cell populations provides independent confirmation that computationally defined clusters correspond to biologically meaningful cell types.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2020-12-015]] | FACS + bulk RNA-seq of KN1-YFP, FEA4-YFP, and vasculature reporters | Sorted populations cluster with their predicted scRNA-seq groups; marker gene enrichment confirmed | Sorted populations, ~12,500 (scRNA-seq) |

## Evidence Quality

**Tier 2** — Orthogonal Validation (independent method confirms scRNA-seq annotations)

## Contradictory Evidence

None. FACS-sorted transcriptomes match scRNA-seq cluster identities.

## Consensus Assessment

**Established** — Orthogonal validation by FACS-sorting strongly supports cluster annotation accuracy.

## Alternative Models

N/A — Validation experiment confirms computational predictions.

## Open Questions

- Can FACS-sorted populations capture rare cell types that scRNA-seq clustering may miss or merge?
- How pure are FACS-sorted populations, and does impurity affect validation conclusions?
- Does the stress response from cell sorting alter transcriptional profiles?

## Next Critical Experiment

Combine FACS enrichment with scRNA-seq on sorted populations to profile cell-type heterogeneity within reporter-defined domains.
