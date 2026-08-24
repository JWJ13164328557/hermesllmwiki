---
type: evidence
claim: "Sucrose supplementation alters relative cell-type proportions in Arabidopsis root"
claim_type: association
status: reviewed
consensus_level: tentative
confidence: medium
species:
  - Arabidopsis thaliana
tissue:
  - root
cell_type:
  - multiple root cell types
development_stage:
  - seedling
condition:
  - sucrose supplementation
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-supplement"
experiments:
  - scRNA-seq with sucrose treatment
  - cell-type proportion analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Sucrose Shifts Root Cell-Type Proportions

## Claim

Supplementing growth media with sucrose alters the relative cell-type proportions captured by scRNA-seq in Arabidopsis roots, suggesting that metabolic conditions influence either cell-type representation or protoplasting efficiency.

## Biological Context

Many Arabidopsis root scRNA-seq studies grow seedlings on sucrose-supplemented media (typically 1% w/v), which provides exogenous carbon. In nature, roots are heterotrophic and rely on shoot-derived photosynthate. Sucrose in the medium may alter root meristem activity, cell division rates, or cell-type composition.

## Supporting Evidence

| Paper | Treatment | Observed Shift | Proposed Mechanism |
|-------|-----------|----------------|-------------------|
| [[xr-10-1016-j-devcel-2019-02-022]] | ± Sucrose | Proportional changes in epidermal and cortical clusters | Altered meristem activity or protoplasting efficiency |

## Evidence Quality

**Tier 4** — Correlative Evidence. Observed proportion shifts may reflect biological changes or technical biases in protoplasting efficiency under different metabolic states.

### Important Caveats
- Single study observation; not independently replicated
- Cannot distinguish biological from technical effects
- Proportion shifts uncalibrated against absolute cell counts

## Contradictory Evidence

Not directly contradicted, but no other study has systematically tested this variable.

## Consensus Assessment

**Tentative** — Plausible and consistent with known effects of sucrose on root development, but limited to one dataset without independent replication.

## Alternative Models

- **Technical bias**: Sucrose alters cell wall composition, changing protoplasting efficiency per cell type
- **No effect**: Observed differences are within normal biological variation

## Open Questions

- Do sucrose-induced proportion shifts reflect in vivo changes or protoplasting artifacts?
- Is the effect linear with sucrose concentration?
- Do other metabolites (e.g., nitrate, phosphate) produce similar shifts?

## Next Critical Experiment

Time-course scRNA-seq with and without sucrose, paired with direct cell counting by confocal microscopy of intact roots, to disentangle biological vs. technical effects on cell-type proportions.
