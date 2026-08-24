---
type: evidence
claim: "scRNA-seq resolves distinct developmental trajectories for root-hair and non-hair epidermal cells"
claim_type: observation
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - epidermis
  - root-hair-cell
  - non-hair-cell
development_stage:
  - seedling (5–7-day-old)
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-3"
  - "xr-10-1016-j-devcel-2019-02-022#figure-4"
experiments:
  - pseudotime analysis (Monocle 2)
  - differential expression
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Distinct Trajectories for Hair and Non-Hair Epidermis

## Claim

Single-cell RNA-seq pseudotime analysis resolves two distinct developmental trajectories within the root epidermis: one leading to hair cell (trichoblast) identity and the other to non-hair cell (atrichoblast) identity, recapitulating the known positional patterning of the root epidermis.

## Biological Context

Root epidermal cells differentiate into two alternating cell files: hair cells (overlying two cortical cells, expressing GL2, CPC) and non-hair cells (overlying a single cortical cell file, expressing WER, GLABRA2). This patterning depends on positional signals from the underlying cortex and a lateral inhibition network of MYB/bHLH/WD40 transcription factors. scRNA-seq allows both trajectories to be observed simultaneously.

## Supporting Evidence

| Paper | Trajectories Identified | Key Bifurcation Genes | Validation |
|-------|------------------------|----------------------|------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | 2 (hair + non-hair) | GL2, CPC, WER, EGL3, TTG1 | Branch point corresponds to known patterning decision |

## Evidence Quality

**Tier 4** — Correlative Evidence. Trajectory bifurcation is computational and not validated by lineage tracing or live imaging.

### Important Caveats
- Bifurcation may be imposed by the trajectory algorithm rather than reflecting a genuine binary decision
- Early pseudotime cells before branch point may be transcriptionally ambiguous
- Branch assignment may be influenced by cell-cycle state

## Contradictory Evidence

None. The two-trajectory model is consistent with decades of genetic and molecular data on root epidermal patterning.

## Consensus Assessment

**Tentative** — Consistent with known biology and supported by scRNA-seq data, but trajectory structure has not been independently validated across datasets.

## Alternative Models

- **Continuous gradient**: Hair vs. non-hair identity may represent extremes of a continuous spectrum rather than truly discrete trajectories
- **Trifurcation**: Additional epidermal subtypes (e.g., lateral root cap–adjacent cells) may represent a third trajectory

## Open Questions

- At what pseudotime point do hair and non-hair trajectories irreversibly diverge?
- How does positional information from the cortex translate into the transcriptional bifurcation?
- Do mutant backgrounds (wer, cpc, gl2) collapse the two trajectories into one?

## Next Critical Experiment

Pseudotime analysis of scRNA-seq data from epidermal patterning mutants (wer, cpc, gl2) to test whether trajectory bifurcation is lost or altered, confirming the genetic basis of the bifurcation.
