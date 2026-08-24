---
type: evidence
claim: "Cell-type-specific marker gene expression correlates with cell-type-specific chromatin accessibility patterns"
claim_type: observation
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
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2021-01-001]]"
supporting_figures:
  - "xr-10-1016-j-molp-2021-01-001#figure-2"
experiments:
  - snATAC-seq
  - scRNA-seq
  - integrative analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Marker Gene Expression Correlates with Chromatin Accessibility

## Claim

Cell-type-specific marker genes show concordant cell-type-specific chromatin accessibility at their promoters and distal regulatory elements, providing cross-modal validation of both cell-type identity and the regulatory basis of marker gene expression.

## Biological Context

Marker genes define cell-type identity at the transcriptomic level. If chromatin accessibility underlies transcriptional regulation, then marker gene loci should show matching cell-type-specific accessibility patterns — a prediction confirmed by this analysis.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2021-01-001]] | Cross-modal correlation (snATAC-seq accessibility vs scRNA-seq expression) | Known marker genes (e.g., CO2, SCR, SHR) show cell-type-matched accessibility at promoters | Thousands of nuclei |

## Evidence Quality

**Tier 3** — Spatial Support (marker gene identity validated by both expression and chromatin accessibility at known loci)

## Contradictory Evidence

None. Concordance between marker expression and chromatin accessibility is robust.

## Consensus Assessment

**Established** — Consistent with extensive evidence from mammalian systems and mechanistically expected from the role of chromatin in gene regulation.

## Alternative Models

Some marker genes may be regulated post-transcriptionally rather than at the chromatin level, but this does not contradict the overall correlation.

## Open Questions

- What proportion of marker genes show discordant expression-accessibility patterns?
- Are there cases where chromatin is accessible but the gene is not expressed (poised state)?
- How do distal regulatory elements contribute to marker gene specificity?

## Next Critical Experiment

CRISPR perturbation of cell-type-specific accessible elements at marker gene loci to test whether accessibility is required for marker expression.
