---
type: entity
entity_type: gene
name: "OsMAPK3"
aliases: ["OsMAPK3 kinase", "MAPK3", "rice MAP kinase 3"]
summary: "OsMAPK3 is a rice mitogen-activated protein kinase that phosphorylates the transcription factor OsbHLH150 at residues S669, S674, and S734 under cold stress, enhancing OsbHLH150 protein stability and driving ABA-mediated chilling tolerance."
status: reviewed
confidence: medium
updated: "2026-05-29"
related_papers:
  - "[[rice-chilling-tolerance]]"
  - "[[osbhlh150-rice-chilling-tolera]]"
  - "[[aba-biosynthesis-stress]]"
related_evidence:
  - "[[rice-root-cell-types-10x]]"
  - "[[rice-root-marker-genes]]"
related_synthesis: []
---

# OsMAPK3

## Summary

OsMAPK3 is a rice mitogen-activated protein kinase (MAPK) that functions as the upstream signaling component of the cold-responsive **OsMAPK3 → OsbHLH150 → OsNCED3 → ABA** cascade. Under chilling stress, OsMAPK3 physically interacts with and phosphorylates the bHLH transcription factor OsbHLH150 at three serine residues (S669, S674, S734). This phosphorylation stabilizes OsbHLH150 by inhibiting ubiquitin-mediated degradation, enabling sustained transcriptional activation of OsNCED3 and ABA biosynthesis. Loss of OsMAPK3 function exacerbates cold sensitivity, while its activity is required for the full cold tolerance conferred by the japonica OsbHLH150 allele. Current evidence is from one study (Luo et al., 2026, *Plant Communications*), with the broader role of OsMAPK3 in rice stress signaling beyond cold not yet characterized in this context.

---

## Biological Roles

### Cold Stress Signaling Kinase

OsMAPK3 phosphorylates OsbHLH150 in response to cold, serving as the signal transduction link between cold perception and transcriptional reprogramming.

Evidence:
- Y2H screen identified OsbHLH150 as OsMAPK3 interactor
- In vitro kinase assay: OsMAPK3 directly phosphorylates OsbHLH150
- In vivo phosphorylation: Cold stress enhances phosphorylation at S669/S674/S734
- Phosphorylation enhances OsbHLH150 protein stability (inhibits ubiquitination)

Confidence: **Strong** (Y2H + in vitro + in vivo phospho-evidence)

### Protein Stability Regulation

OsMAPK3-mediated phosphorylation prevents OsbHLH150 ubiquitination and degradation.

Evidence:
- Phospho-dead mutant (S3A) shows reduced stability and cold sensitivity
- Phospho-mimetic mutant (S3D) partially restores cold tolerance
- Indica-type OsbHLH150 shows weaker OsMAPK3 binding → lower phosphorylation → reduced stability

Confidence: **Moderate** (single study, biochemical mechanism plausible)

---

## Expression Pattern

### Tissue
Not specifically characterized in the Luo et al. (2026) study. MAPK3 is broadly expressed in plant tissues.

### Stress Responsiveness
Cold stress enhances OsMAPK3-mediated phosphorylation activity toward OsbHLH150.

### Evidence
- Co-immunoprecipitation under cold vs. control conditions

### Caveats
Tissue-level and cell-type expression of OsMAPK3 not profiled. The mechanism by which cold activates OsMAPK3 kinase activity (upstream cold sensor) is unknown. No scRNA-seq or spatial data available for OsMAPK3 in rice under cold stress.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| Physical interaction with OsbHLH150 | Rice (*O. sativa*) | — | Y2H | [[rice-chilling-tolerance]] | Strong |
| Phosphorylation of OsbHLH150 (S669/S674/S734) | Rice (*O. sativa*) | — | In vitro + in vivo kinase assay | [[rice-chilling-tolerance]] | Strong |
| Protein stabilization of OsbHLH150 | Rice (*O. sativa*) | — | Protein stability assay (CHX chase) | [[rice-chilling-tolerance]] | Moderate |
| Genetic requirement for cold tolerance | Rice (*O. sativa*) | Seedling | CR-OsMAPK3 × CR-OsbHLH150 double mutant epistasis | [[rice-chilling-tolerance]] | Strong |
| Cold-induced kinase activity | Rice (*O. sativa*) | Seedling | Phosphorylation level comparison (cold vs. control) | [[rice-chilling-tolerance]] | Moderate |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| Unknown cold sensor | Cold stress activates OsMAPK3 kinase activity toward OsbHLH150 | Implied by cold-induced phosphorylation | Low (mechanism unresolved) |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| OsbHLH150 | Direct phosphorylation at S669/S674/S734 → protein stabilization | Y2H + in vitro/in vivo phosphorylation | Strong |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| None identified | — | — |

### Co-expression Modules

| Module | Dataset | Evidence | Confidence |
|---|---|---|
| Cold-responsive ABA biosynthesis module | Bulk RNA under cold stress | Co-regulation with [[osbhlh150]] and [[osnced3-rice]] under cold | Moderate |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Not characterized at single-cell resolution | — | — | — |

*No cell-type-specific expression or functional data available. MAPK cascades are generally active in multiple cell types.*

---

## Developmental Context

### Seedling Stage
OsMAPK3-OsbHLH150 interaction and cold-responsive phosphorylation demonstrated at seedling stage.

### Other Stages
Not tested at booting, flowering, or grain filling stages.

---

## Stress or Environmental Context

### Chilling Stress (Primary)
OsMAPK3 phosphorylation activity toward OsbHLH150 is cold-induced. This is the only stress context characterized for OsMAPK3-OsbHLH150 interaction.

### Other Stresses
OsMAPK3 is a broadly conserved MAPK likely involved in multiple stress responses (pathogen, drought, salt), but its role beyond cold tolerance in rice has not been specifically characterized in this study.

---

## Cross-Species Conservation

### Arabidopsis
AtMPK3 and AtMPK6 are the closest Arabidopsis orthologs. These MAPKs are involved in diverse stress and developmental signaling (pathogen response, stomatal development, etc.) but a direct AtMPK3 → bHLH → NCED cold tolerance cascade has not been described in Arabidopsis. Arabidopsis cold tolerance primarily uses the CBF/DREB pathway.

### Other Cereals
MAPK3 orthologs are conserved across Poaceae, but functional characterization in cold tolerance not yet performed.

### Conservation Assessment: **Partially conserved** — The kinase activity and interaction domain are conserved, but the specific OsbHLH150-OsNCED3 wiring appears to be a rice-specific or Poaceae-specific adaptation for cold tolerance.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Biochemical (Y2H, phosphorylation) | Strong | Multiple complementary assays |
| Genetic (double mutant epistasis) | Strong | Clean epistasis with OsbHLH150 |
| Protein stability mechanism | Moderate | Single study, CHX chase assay |
| Expression | Weak | No tissue/cell-type expression data |
| Upstream activation mechanism | Weak | Cold sensor unknown |

**Overall Confidence: Medium** — The kinase-substrate relationship (OsMAPK3 → OsbHLH150) is biochemically well-supported. However, (1) all evidence is from a single study, (2) the upstream cold sensor activating OsMAPK3 is unknown, and (3) OsMAPK3's broader role in rice cold signaling beyond the OsbHLH150 substrate has not been explored.

---

## Contradictions and Context Dependence

### Contradiction 1: Single-substrate model may oversimplify
- **Claim**: OsMAPK3 functions specifically through OsbHLH150 in cold tolerance.
- **Context**: Only OsbHLH150 was tested as a substrate. MAPKs typically have multiple substrates.
- **Caveat**: OsMAPK3 may have additional cold-relevant substrates not identified in this study.

### Context Dependence
- **Stress specificity**: Only tested under cold stress; role under normal growth or other stresses unknown.
- **Genetic background**: Interaction tested primarily in japonica background.

---

## Open Questions

### Question 1: What is the cold sensor that activates OsMAPK3?

- **Why It Matters**: The most upstream component of the cold signaling cascade is unknown; understanding it could reveal cold perception mechanisms.
- **Missing Evidence**: Upstream kinase (MAPKKK → MAPKK → MAPK), calcium channel, or membrane fluidity sensor.
- **Suggested Experiment**: Phosphoproteomics of cold-treated rice to identify OsMAPK3-activating kinases; candidate MAPKK screening by Y2H.

### Question 2: Does OsMAPK3 have additional substrates in the cold response?

- **Why It Matters**: MAPKs are signaling hubs; additional substrates would provide a fuller picture of cold response.
- **Missing Evidence**: Phosphoproteome of OsMAPK3-KO vs. WT under cold.
- **Suggested Experiment**: Quantitative phosphoproteomics comparing WT and OsMAPK3-KO under cold stress.

### Question 3: Is OsMAPK3-OsbHLH150 interaction conserved across Oryza species?

- **Why It Matters**: Determines whether this module can be deployed in wild rice relatives and other cereals.
- **Missing Evidence**: Ortholog testing in O. rufipogon, O. glaberrima, and other AA-genome species.
- **Suggested Experiment**: Test OsMAPK3-OsbHLH150 Y2H interaction across Oryza accessions.

---

## Key References

1. Luo J. et al. (2026). Natural variation in OsbHLH150 confers chilling tolerance in rice by increasing ABA biosynthesis. *Plant Communications*. DOI: [10.1016/j.xplc.2026.101919](https://doi.org/10.1016/j.xplc.2026.101919) — [[rice-chilling-tolerance]]

---

## Knowledge Graph Links

### Related Genes
- [[osbhlh150]] — Phosphorylation substrate; downstream TF
- [[osnced3-rice]] — Indirect downstream target (via OsbHLH150)

### Related Pathways
- [[aba-biosynthesis-stress]] — ABA biosynthesis pathway

### Related Entities
- [[guangxi-university-luo-lab]] — Research group
