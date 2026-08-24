---
type: evidence
claim: "Harmony integrates approximately 1 million cells on a personal computer"
claim_type: method
status: reviewed
consensus_level: established
confidence: high
species:
  - Homo sapiens
tissue:
  - multiple
cell_type:
  - multiple
development_stage:
  - multiple
condition:
  - standard
support:
  - "[[xr-10-1038-s41592-019-0619-0]]"
supporting_figures:
  - "xr-10-1038-s41592-019-0619-0#figure-4"
experiments:
  - scalability benchmarking
  - Harmony integration
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Harmony Integrates ~1 Million Cells on a Personal Computer

## Claim

Harmony integrates approximately 1 million single cells on a standard personal computer, demonstrating linear runtime scaling with cell count and memory efficiency suitable for large-scale single-cell atlases.

## Methodological Context

As scRNA-seq datasets grow to millions of cells, integration methods must scale beyond the memory and compute constraints of high-performance clusters. Harmony's iterative soft-clustering approach is inherently scalable because it operates on a low-dimensional PCA embedding rather than the full expression matrix, and its correction step is linear in the number of cells.

## Supporting Evidence

| Paper | Method | Key Finding | Scale |
|-------|--------|-------------|-------|
| [[xr-10-1038-s41592-019-0619-0]] | Harmony scalability test | Integrated ~1M cells on a personal computer; runtime scales linearly with cell count; memory efficient | ~1,000,000 cells |

## Evidence Quality

**Tier 1** — Empirical scalability measurement with reproducible benchmarking

## Contradictory Evidence

None. Harmony's scalability has been independently verified across multiple atlas projects.

## Consensus Assessment

**Established** — Harmony is routinely used for million-cell atlas integration.

## Alternative Models

BBKNN, Scanorama, and online iNMF (LIGER) also offer scalable integration approaches.

## Open Questions

- What is the practical upper limit of Harmony on a personal computer (10M? 100M cells)?
- How does performance degrade with extremely heterogeneous datasets?

## Next Critical Experiment

Benchmark Harmony integration of the complete Human Cell Atlas (tens of millions of cells) across tissue contexts.
