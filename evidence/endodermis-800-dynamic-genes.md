---
type: evidence
claim: "Nearly 800 genes show dynamic expression patterns during endodermis development"
claim_type: observation
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - endodermis
development_stage:
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-2"
  - "xr-10-1016-j-devcel-2019-02-022#figure-3"
experiments:
  - pseudotime analysis (Monocle 2)
  - differential expression along trajectory
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# ~800 Genes Show Dynamic Expression in Endodermis Development

## Claim

Pseudotime analysis of endodermis scRNA-seq data identifies approximately 800 genes with dynamically changing expression levels as cells progress from meristematic to fully differentiated endodermis, revealing the transcriptional programs underlying Casparian strip formation and endodermal maturation.

## Biological Context

The endodermis is the innermost cortical layer that forms the Casparian strip — a lignin-based apoplastic barrier essential for selective nutrient uptake. Endodermis differentiation involves coordinated expression of lignin biosynthesis genes, transcription factors (e.g., MYB36, SHR, SCR), and transporters. scRNA-seq provides the first transcriptome-wide view of the temporal sequence of this differentiation program.

## Supporting Evidence

| Paper | Method | Genes Identified | Key Functional Categories |
|-------|--------|-----------------|--------------------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Monocle 2 pseudotime | ~800 dynamic genes | Lignin biosynthesis, transporters, TFs, cell wall modification |

## Evidence Quality

**Tier 4** — Correlative Evidence. Gene dynamics are inferred from pseudotime ordering of static snapshots, not direct temporal measurement.

### Important Caveats
- Pseudotime ordering is computational, not directly validated
- The 800-gene estimate is clustering-resolution and threshold-dependent
- Post-transcriptional regulation not captured

## Contradictory Evidence

None directly. Other studies have focused on different cell types or used different trajectory algorithms, but genes identified in endodermis are consistent with known function.

## Consensus Assessment

**Tentative** — Strongly supported within the primary study but not yet independently replicated at this level of cell-type-specific resolution.

## Alternative Models

- Some dynamic expression may reflect cell-cycle effects rather than differentiation
- A subset of genes may represent stress responses to protoplasting rather than developmental programs

## Open Questions

- How many of these 800 genes are functionally required for endodermis differentiation?
- Do these genes form coherent regulatory modules (e.g., co-expression networks)?
- How does the endodermis differentiation trajectory compare across root zones?

## Next Critical Experiment

CRISPR knockout screen of top candidate dynamic genes combined with scRNA-seq readout to identify genes functionally required for endodermal differentiation.
