---
type: evidence
claim: "Total RNA expression increases along developmental trajectories in root cells"
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
  - epidermis
development_stage:
  - seedling
condition:
  - standard growth
support:
  - "[[xr-10-1016-j-devcel-2019-02-022]]"
supporting_figures:
  - "xr-10-1016-j-devcel-2019-02-022#figure-3"
  - "xr-10-1016-j-devcel-2019-02-022#figure-4"
experiments:
  - pseudotime analysis
  - total UMI count vs. pseudotime
  - gene detection analysis
contradictions: []
contradiction_type: null
updated: "2026-05-29"
---

# Total RNA Increases Along Developmental Trajectories

## Claim

Total RNA expression (measured as total UMI counts per cell) increases monotonically along pseudotime trajectories in Arabidopsis root cells, indicating that differentiated cells have larger transcriptomes than meristematic cells.

## Biological Context

Meristematic cells are small, cytoplasmically dense, and rapidly dividing — potentially limiting total transcriptional output. Differentiating cells enlarge, become more metabolically active, and may upregulate tissue-specific gene programs. An increase in total mRNA content with differentiation would be consistent with this biology, but could also reflect technical factors.

## Supporting Evidence

| Paper | Cell Types | Trend Observed | Magnitude |
|-------|-----------|---------------|-----------|
| [[xr-10-1016-j-devcel-2019-02-022]] | Endodermis, epidermis | UMI counts increase with pseudotime | ~1.5–2× from early to late pseudotime |

## Evidence Quality

**Tier 5** — Pre/Correlative Observations. The observation is consistent but may be confounded by technical or biological covariates.

### Important Caveats
- UMI count is a proxy for total mRNA, not a direct measurement
- Larger cells may simply yield more RNA during library preparation (technical bias)
- Pseudotime ordering may place larger/older cells at later positions regardless of differentiation state
- Normalization choices can obscure or exaggerate this trend

## Contradictory Evidence

Not all cell types may show this trend with the same magnitude. Some studies report flat or even decreasing UMI counts in terminally differentiated cells (e.g., mature xylem).

## Consensus Assessment

**Tentative** — The trend is observed in at least one major dataset, but it is unclear whether this reflects biology, technical artifact, or a combination.

## Alternative Models

- **Technical artifact**: Protoplasting efficiency or RNA capture efficiency scales with cell size
- **Cell-cycle effect**: Early pseudotime cells are enriched for cycling cells with proportionally fewer UMIs per cell volume
- **True biological increase**: Differentiation involves genome-wide transcriptional activation

## Open Questions

- Does total mRNA per cell increase or does UMI count increase reflect cell size?
- Can this trend be replicated with spike-in–normalized data?
- Does the trend hold across all root cell types?

## Next Critical Experiment

scRNA-seq with ERCC spike-ins to normalize for technical variation and dissociate true biological changes in total mRNA from cell-size–dependent capture efficiency.
