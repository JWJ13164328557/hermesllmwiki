---
type: evidence
claim: "Single-nucleus RNA-seq is a valid alternative to protoplast-based scRNA-seq for plant transcriptomics"
claim_type: observation
status: reviewed
consensus_level: emerging
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
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2021-01-001]]"
supporting_figures:
  - "xr-10-1016-j-molp-2021-01-001#figure-1"
experiments:
  - snRNA-seq
  - scRNA-seq
  - method comparison
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# snRNA-seq Is a Valid Alternative to Protoplast-Based scRNA-seq

## Claim

Single-nucleus RNA-seq (snRNA-seq) of Arabidopsis roots recovers all major cell types identified by protoplast-based scRNA-seq, demonstrating that nuclear transcriptomes are sufficient for plant cell-type resolution without the biases of enzymatic cell wall digestion.

## Biological Context

Protoplasting — required for most plant scRNA-seq protocols — can induce stress responses and bias cell-type recovery (e.g., underrepresentation of certain cell types). snRNA-seq bypasses cell wall digestion, potentially capturing a more representative cell population.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2021-01-001]] | snRNA-seq (10x) vs scRNA-seq comparison | snRNA-seq recovers all major cell types; nuclear transcriptomes correlate well with whole-cell transcriptomes | Thousands of nuclei |

## Evidence Quality

**Tier 3** — Spatial Support (cell types identified by snRNA-seq match those from scRNA-seq with known spatial markers)

## Contradictory Evidence

None. snRNA-seq shows comparable cell-type resolution to scRNA-seq in direct comparisons.

## Consensus Assessment

**Emerging** — One well-powered study demonstrates validity; broader adoption across plant species and tissues is ongoing.

## Alternative Models

Some researchers argue that snRNA-seq may miss cytoplasmic transcripts important for certain biological processes, making it complementary rather than fully equivalent to scRNA-seq.

## Open Questions

- Does snRNA-seq systematically underrepresent certain transcript classes (e.g., stress-responsive mRNAs)?
- Is nuclear transcript recovery consistent across all cell types?
- How does snRNA-seq perform in non-root tissues?

## Next Critical Experiment

Multi-tissue, multi-species comparison of snRNA-seq and scRNA-seq from the same samples to quantify transcript recovery biases.
