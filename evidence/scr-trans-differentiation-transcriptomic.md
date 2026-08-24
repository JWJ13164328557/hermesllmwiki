---
type: evidence
claim: "Transcriptomic evidence supports tissue trans-differentiation in scarecrow mutant roots"
claim_type: observation
status: reviewed
consensus_level: emerging
confidence: high
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - endodermis
  - cortex
development_stage:
  - seedling
condition:
  - scarecrow (scr) mutant
support:
  - "[[xr-10-1016-j-devcel-2022-01-008]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2022-01-008#figure-6"
experiments:
  - scRNA-seq
  - mutant analysis
  - trajectory inference
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Transcriptomic Evidence Supports Trans-Differentiation in scr Mutants

## Claim

scRNA-seq analysis of scarecrow (scr) mutant roots reveals a mixed endodermis-cortex transcriptional identity in the mutant ground tissue layer, providing transcriptomic evidence for tissue trans-differentiation rather than simple loss of endodermis identity.

## Biological Context

SCR is a GRAS-family transcription factor required for asymmetric cell division in the ground tissue. In scr mutants, the endodermis-cortex initial fails to divide, producing a single ground tissue layer. Whether this layer has a mixed identity or simply becomes cortex was debated.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2022-01-008]] | scRNA-seq of scr mutants + trajectory analysis | scr mutant ground tissue shows co-expression of endodermis and cortex markers; positioned between WT endodermis and cortex in transcriptomic space | Thousands |

## Evidence Quality

**Tier 3** — Spatial Support (transcriptomic evidence; validated by in vivo imaging in companion study)

## Contradictory Evidence

None. Prior literature suggested potential mixed identity; scRNA-seq provides direct transcriptomic evidence.

## Consensus Assessment

**Emerging** — Strong transcriptomic evidence supported by imaging; represents a shift from the "cortex-only" model to the "mixed identity" model.

## Alternative Models

The mixed identity could reflect a failure to fully differentiate rather than active trans-differentiation — cells may stall in an intermediate transcriptional state.

## Open Questions

- Is the mixed identity stable or does it resolve over developmental time?
- What transcription factors maintain cortex gene expression in the scr mutant ground tissue?
- Do other ground tissue mutants (e.g., shr) show similar trans-differentiation signatures?

## Next Critical Experiment

Time-course scRNA-seq of scr mutant roots to determine whether the mixed identity is a stable state or a transient developmental arrest.
