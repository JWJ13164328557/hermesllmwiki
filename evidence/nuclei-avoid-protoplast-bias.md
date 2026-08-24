---
type: evidence
claim: "Nuclei-based single-cell methods avoid transcriptional artifacts induced by protoplasting"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard
support:
  - "[[xr-10-1104-pp-18-01482]]"
  - "[[nuclei-scRNA-seq-plant-paper]]"
supporting_figures:
  - "nuclei-scRNA-seq-plant-paper#figure-1"
  - "nuclei-scRNA-seq-plant-paper#figure-2"
experiments:
  - snRNA-seq
  - scRNA-seq comparison
  - protoplast vs. nuclei
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Nuclei-Based Methods Avoid Protoplasting Transcriptional Artifacts

## Claim

Nuclei-based single-cell RNA-seq (snRNA-seq) methods avoid transcriptional artifacts induced by protoplasting — the enzymatic cell wall digestion required for plant scRNA-seq — including stress-responsive gene induction and biased cell-type recovery.

## Methodological Context

Plant scRNA-seq typically requires protoplast generation via cell wall digestion, which takes hours and can induce wound/stress responses that alter the transcriptome. It also selectively recovers cell types that survive the digestion process. snRNA-seq bypasses this by isolating nuclei directly from frozen tissue, capturing the nuclear transcriptome without enzymatic stress.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1104-pp-18-01482]] | Protoplast scRNA-seq | Some cell types may be underrepresented in protoplast-based methods | >10,000 cells |
| [[nuclei-scRNA-seq-plant-paper]] | snRNA-seq vs. scRNA-seq comparison | Nuclei methods reduce stress gene induction and improve cell-type representation | Plant tissues |

## Evidence Quality

**Tier 2** — Method comparison with biological validation

## Contradictory Evidence

Some studies report that nuclear RNA captures only a subset of the total transcriptome, potentially missing cytoplasmic-enriched transcripts.

## Consensus Assessment

**Established** — snRNA-seq is a widely accepted complement to protoplast-based scRNA-seq in plants.

## Alternative Models

Protoplast-based scRNA-seq with transcriptional inhibitor treatment to minimize stress response.

## Open Questions

- What proportion of the transcriptome is lost in nuclear vs. whole-cell RNA?
- Can nuclear and cytoplasmic transcriptomes be jointly analyzed?

## Next Critical Experiment

Paired nuclear and whole-cell RNA-seq from the same tissue to quantify transcript loss and artifact magnitude.
