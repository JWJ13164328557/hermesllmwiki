---
type: evidence
claim: "Substantial differences exist between rice and Arabidopsis cell-type transcript profiles"
claim_type: observation
status: reviewed
consensus_level: established
confidence: high
species:
  - Oryza sativa
  - Arabidopsis thaliana
tissue:
  - root tip
cell_type:
  - all root cell types
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-molp-2020-12-014]]"
supporting_figures:
  - "xr-10-1016-j-molp-2020-12-014#figure-4"
experiments:
  - scRNA-seq
  - cross-species comparison
  - ortholog expression correlation
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Substantial Differences Between Rice and Arabidopsis Cell-Type Transcript Profiles

## Claim

Cross-species comparison of scRNA-seq data reveals substantial divergence in cell-type transcript profiles between rice and Arabidopsis roots, despite conservation of major cell-type categories and key developmental regulators.

## Biological Context

Rice and Arabidopsis diverged ~150 million years ago and have fundamentally different root architectures (fibrous vs taproot). Understanding transcriptomic divergence reveals which aspects of cell-type identity are evolutionarily constrained and which are lineage-specific.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-molp-2020-12-014]] | Ortholog-based cross-species correlation | Cell-type transcriptomes are more similar within species than between species for homologous cell types; substantial divergence in gene expression programs | >40,000 total |

## Evidence Quality

**Tier 3** — Spatial Support (cell-type identity validated by conserved marker orthologs in both species)

## Contradictory Evidence

None. Divergence is expected given the evolutionary distance and anatomical differences between monocot and dicot roots.

## Consensus Assessment

**Established** — Single comprehensive cross-species study; consistent with known anatomical and physiological differences between monocot and dicot roots.

## Alternative Models

N/A — This is a descriptive observation of evolutionary divergence.

## Open Questions

- Which cell-type transcript programs are most conserved (deep homology) vs most divergent?
- Is divergence driven by cis-regulatory changes, gene family expansion, or both?
- How does the monocot-specific exodermis transcriptome relate to Arabidopsis cell types?

## Next Critical Experiment

Multi-species scRNA-seq across diverse angiosperms to map the evolutionary trajectory of root cell-type transcriptomes.
