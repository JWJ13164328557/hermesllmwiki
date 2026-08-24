---
type: evidence
claim: "scRNA-seq co-expression networks predict genetic redundancy in maize ear development"
claim_type: prediction
status: reviewed
consensus_level: emerging
confidence: medium
species:
  - Zea mays
tissue:
  - developing ear
cell_type:
  - inflorescence meristem
  - spikelet pair meristem
development_stage:
  - early reproductive
condition:
  - field-grown
support:
  - "[[xr-10-1016-j-devcel-2020-12-015]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2020-12-015#figure-5"
experiments:
  - scRNA-seq
  - co-expression network analysis
  - genetic redundancy prediction
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# scRNA-seq Co-expression Networks Predict Genetic Redundancy

## Claim

Co-expression network analysis of scRNA-seq data from developing maize ears identifies highly correlated gene modules that predict genetic redundancy — gene pairs whose individual knockout mutants show no phenotype due to functional compensation by co-expressed paralogs.

## Biological Context

Maize underwent whole-genome duplication, creating many paralogous gene pairs. Identifying which paralogs are functionally redundant vs sub-functionalized is critical for reverse genetics and crop improvement. Co-expression patterns may predict redundancy.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2020-12-015]] | WGCNA co-expression + mutant phenotyping | Closely co-expressed paralogs (e.g., FEA4 and its paralog) show functional redundancy; single mutants lack phenotype, double mutants show defects | ~12,500 (scRNA-seq) |

## Evidence Quality

**Tier 3** — Partial Functional Support (one gene pair validated by mutant analysis; broader predictability not systematically tested)

## Contradictory Evidence

Not all co-expressed paralogs may be redundant; some may have diverged in function despite similar expression patterns.

## Consensus Assessment

**Emerging** — Principle demonstrated with one well-validated example; broader systematic testing needed.

## Alternative Models

Co-expression could reflect shared regulatory elements rather than shared function. Redundancy may occur at the protein level even when genes are not co-expressed.

## Open Questions

- What co-expression threshold best predicts functional redundancy?
- Does prediction accuracy vary by gene family or cell type?
- Can this approach scale to genome-wide redundancy prediction?

## Next Critical Experiment

Systematic CRISPR double-knockout of predicted redundant paralog pairs across multiple cell types to quantify prediction accuracy and identify false positives.
