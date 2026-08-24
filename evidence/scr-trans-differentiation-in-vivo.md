---
type: evidence
claim: "In vivo confocal imaging validates mixed cell identity phenotype in scarecrow mutants"
claim_type: observation
status: reviewed
consensus_level: established
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
  - confocal microscopy
  - reporter gene imaging
  - mutant analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# In Vivo Imaging Validates Mixed Cell Identity in scr Mutants

## Claim

In vivo confocal imaging of scarecrow (scr) mutant roots expressing cell-type-specific fluorescent reporters demonstrates co-expression of endodermis and cortex markers in the single ground tissue layer, validating the mixed identity phenotype inferred from scRNA-seq.

## Biological Context

The scr mutant was historically described as lacking endodermis identity. scRNA-seq revealed a mixed transcriptional state; in vivo imaging of dual reporter lines provides direct spatial confirmation that individual cells express both endodermis and cortex markers.

## Supporting Evidence

| Paper | Method | Key Finding | Cells |
|-------|--------|-------------|-------|
| [[xr-10-1016-j-devcel-2022-01-008]] | Confocal imaging of SCRpro::GFP + CO2pro::mCherry in scr mutants | Single ground tissue cells co-express both GFP (cortex marker) and mCherry (endodermis marker) | Live imaging |

## Evidence Quality

**Tier 1** — Direct Visualization (live imaging of dual reporters in intact tissue; gold standard for spatial validation)

## Contradictory Evidence

None. Imaging directly confirms the transcriptomic prediction of mixed identity.

## Consensus Assessment

**Established** — Direct in vivo visualization confirms mixed cell identity; resolves prior ambiguity about scr mutant phenotype.

## Alternative Models

Co-expression of reporters could reflect perdurance of fluorescent proteins rather than active transcription, though the scRNA-seq evidence supports active co-expression.

## Open Questions

- Is the mixed identity uniform across all cells in the mutant ground tissue layer?
- Do endodermis and cortex markers co-localize to the same subcellular compartments or show spatial segregation within the cell?
- Does mixed identity persist in older root regions?

## Next Critical Experiment

Longitudinal live imaging of dual reporter scr mutants over developmental time to track the stability and uniformity of the mixed identity phenotype.
