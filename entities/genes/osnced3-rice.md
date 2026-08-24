---
type: entity
entity_type: gene
name: "OsNCED3"
aliases: ["NCED3", "OsNCED3 dioxygenase", "9-cis-epoxycarotenoid dioxygenase 3"]
summary: "OsNCED3 encodes the rate-limiting enzyme in ABA biosynthesis in rice. It is directly transcriptionally activated by OsbHLH150 under cold stress, serving as the effector node of the OsMAPK3-OsbHLH150-OsNCED3 cold tolerance cascade."
status: reviewed
confidence: medium
updated: "2026-05-29"
related_papers:
  - "[[rice-chilling-tolerance]]"
  - "[[osbhlh150-rice-chilling-tolera]]"
  - "[[aba-biosynthesis-stress]]"
related_evidence:
  - "[[rice-root-hormone-celltype-map]]"
  - "[[rice-root-cell-types-10x]]"
related_synthesis: []
---

# OsNCED3

## Summary

OsNCED3 encodes a 9-cis-epoxycarotenoid dioxygenase (NCED), the rate-limiting enzyme of the ABA biosynthetic pathway in rice. Under cold stress, OsNCED3 is transcriptionally activated by the bHLH transcription factor OsbHLH150, which binds directly to the E-box (CACATG) motif in the OsNCED3 promoter. OsNCED3 upregulation increases ABA levels, which in turn confers chilling tolerance. OsNCED3 is the downstream effector of the **OsMAPK3 → OsbHLH150 → OsNCED3 → ABA** module. Overexpression of OsNCED3 can rescue the cold-sensitive phenotype of OsbHLH150 knockout lines, confirming its position as the terminal biosynthetic enzyme in this cascade. Evidence is from Luo et al. (2026, *Plant Communications*); the broader role of OsNCED3 in drought and other ABA-mediated stress responses is established in other studies but not integrated here.

---

## Biological Roles

### ABA Biosynthesis — Rate-Limiting Step

OsNCED3 catalyzes the oxidative cleavage of 9-cis-epoxycarotenoids to xanthoxin, the first committed and rate-limiting step in ABA biosynthesis.

Evidence:
- NCED enzymes are established as the key regulatory step in ABA biosynthesis (multiple species)
- OsNCED3 expression correlates with ABA levels under cold stress

Confidence: **Strong** (well-established enzyme function across plant species)

### Chilling Tolerance via ABA Accumulation

OsNCED3 upregulation under cold stress increases ABA content, which activates downstream cold-responsive genes.

Evidence:
- OsNCED3-KO: reduced ABA under cold → cold-sensitive phenotype
- OE-OsNCED3: rescues cold-sensitive phenotype of CR-OsbHLH150
- OsNCED3 expression cold-inducible and OsbHLH150-dependent

Confidence: **Strong** (genetic epistasis + biochemical pathway logic)

---

## Expression Pattern

### Tissue
Not specifically profiled at single-cell resolution in Luo et al. (2026). NCED genes are typically expressed in vascular tissues and guard cells where ABA biosynthesis occurs.

### Stress Responsiveness
Cold-inducible expression, dependent on OsbHLH150 transcriptional activation.

### Evidence
- qRT-PCR: cold-induced OsNCED3 expression
- ChIP + LUC: OsbHLH150 directly activates OsNCED3 promoter

### Caveats
Tissue- and cell-type-level expression in cold-treated rice not characterized by scRNA-seq or spatial approaches.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| ABA biosynthesis — rate-limiting enzyme | Rice (*O. sativa*) | — | Biochemical pathway (established) | [[aba-biosynthesis-stress]] | Strong |
| OsbHLH150 direct target — E-box binding | Rice (*O. sativa*) | — | ChIP + LUC reporter | [[rice-chilling-tolerance]] | Strong |
| Cold-induced expression (OsbHLH150-dependent) | Rice (*O. sativa*) | Seedling | qRT-PCR (WT vs. CR-OsbHLH150) | [[rice-chilling-tolerance]] | Moderate |
| Genetic rescue of CR-OsbHLH150 | Rice (*O. sativa*) | Seedling | OE-OsNCED3 in CR-OsbHLH150 background | [[rice-chilling-tolerance]] | Strong |
| KO phenotype — cold sensitive, low ABA | Rice (*O. sativa*) | Seedling | CRISPR knockout | [[rice-chilling-tolerance]] | Moderate |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| OsbHLH150 | Direct transcriptional activation via E-box (CACATG) in OsNCED3 promoter; phosphorylation of OsbHLH150 enhances activation | ChIP + LUC + genetic epistasis | Strong |
| Cold stress | Induces expression via OsbHLH150-dependent pathway | qRT-PCR (cold vs. control) | Moderate |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| ABA biosynthesis pathway | OsNCED3 is the rate-limiting enzyme; product (ABA) activates downstream stress-responsive genes | Biochemical pathway + ABA measurement | Strong |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| ABA may feedback-regulate upstream components (not tested in this study) | Speculative | Low |

### Co-expression Modules

| Module | Dataset | Evidence | Confidence |
|---|---|---|
| Cold-induced ABA biosynthesis | Bulk RNA under cold stress | Co-expression with OsbHLH150, OsMAPK3 under cold | Moderate |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Not characterized at single-cell resolution | — | — | — |

*NCED genes in other species are associated with vascular tissue, guard cells, and root tissues. OsNCED3 cell-type expression under cold stress remains to be profiled.* Possible relevance: [[rice-root-hormone-celltype-map]] for hormone-related gene cell-type mapping.

---

## Developmental Context

### Seedling Stage
OsNCED3 function in cold tolerance demonstrated at seedling stage; expression cold-inducible.

### Other Stages
Role of OsNCED3 in ABA-mediated cold tolerance at booting stage implied by OsbHLH150 overexpression effect but not directly tested for OsNCED3.

---

## Stress or Environmental Context

### Chilling Stress (Primary)
OsNCED3 is cold-inducible and its upregulation is required for ABA accumulation and cold tolerance.

### Other Abiotic Stresses
NCED3 orthologs in other species (Arabidopsis AtNCED3) are well-known drought-responsive genes. OsNCED3's role in rice drought response is plausible but not specifically tested in this study.

### Hormonal Context
OsNCED3 is the biosynthetic gateway to ABA, a key stress hormone with roles in cold, drought, salt, and seed dormancy.

---

## Cross-Species Conservation

### Arabidopsis
AtNCED3 is the major stress-inducible NCED in Arabidopsis, primarily associated with drought-induced ABA accumulation. The bHLH → NCED3 regulatory connection is not conserved in Arabidopsis cold response (which uses CBF/DREB → COR genes). However, NCED3 function as a stress-inducible ABA biosynthetic enzyme is highly conserved.

### Rice
Multiple OsNCED genes exist; OsNCED3 is the cold-responsive isoform in this cascade. Other OsNCED paralogs may handle drought and developmental ABA.

### Other Cereals
NCED3 orthologs are present across Poaceae; stress-inducible function conserved.

### Conservation Assessment: **Partially conserved** — NCED3 enzyme function and stress-inducibility are deeply conserved. The specific bHLH150 → NCED3 cold-regulatory wiring appears to be a rice innovation.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Enzymatic function (NCED = ABA rate-limiting enzyme) | Strong | Conserved across plants |
| OsbHLH150 → OsNCED3 direct regulation | Strong | ChIP + LUC + genetic epistasis |
| Cold-induced expression | Moderate | Single study, qRT-PCR |
| KO phenotype | Moderate | Single study |
| Cell-type expression | Weak | Not profiled |

**Overall Confidence: Medium** — The role of OsNCED3 as the downstream effector of the cold cascade is well-supported. However, (1) data is from a single study, (2) expression is only at the bulk tissue level, and (3) the broader role of OsNCED3 in rice ABA biology beyond cold is not fully synthesized here.

---

## Contradictions and Context Dependence

### Contradiction 1: Which NCED paralog is most important?
- **Claim**: OsNCED3 is the primary cold-responsive ABA biosynthetic gene in rice.
- **Context**: Other OsNCED paralogs may also contribute to ABA levels under cold or other stresses.
- **Caveat**: Functional redundancy among NCED family members was not systematically tested.

### Context Dependence
- **Stress type**: Directly tested only under cold; drought role plausible but untested in this study.
- **Tissue**: Whole-seedling level; tissue-specific ABA dynamics unknown.
- **Genetic background**: Tested in japonica background; indica response uncharacterized.

---

## Open Questions

### Question 1: Where is OsNCED3 expressed at cell-type resolution during cold stress?

- **Why It Matters**: ABA may act locally (site of synthesis) or systemically. Cell-type resolution would clarify whether ABA is produced in cold-sensing cells, vascular tissue, or broadly.
- **Missing Evidence**: scRNA-seq or in situ hybridization of cold-treated rice.
- **Suggested Experiment**: Spatial transcriptomics (Stereo-seq) of cold-treated seedlings + OsNCED3 promoter-reporter lines.

### Question 2: What other transcription factors regulate OsNCED3 beyond OsbHLH150?

- **Why It Matters**: Promoters of stress-responsive genes typically integrate multiple signals. OsbHLH150 may not be the sole regulator.
- **Missing Evidence**: Promoter deletion analysis, TF binding site prediction, Y1H screen.
- **Suggested Experiment**: Promoter bashing + Y1H library screen for OsNCED3 promoter-binding TFs.

### Question 3: Is OsNCED3 the only ABA biosynthetic gene induced by cold?

- **Why It Matters**: ABA biosynthesis involves multiple steps (NCED, ABA2, AAO3, etc.). Understanding the full biosynthetic activation would clarify rate-limitation.
- **Missing Evidence**: Expression profiling of all ABA biosynthesis genes under cold.
- **Suggested Experiment**: qRT-PCR panel for all ABA biosynthetic genes (OsNCED1-5, OsABA2, OsAAO3) under cold time course.

---

## Key References

1. Luo J. et al. (2026). Natural variation in OsbHLH150 confers chilling tolerance in rice by increasing ABA biosynthesis. *Plant Communications*. DOI: [10.1016/j.xplc.2026.101919](https://doi.org/10.1016/j.xplc.2026.101919) — [[rice-chilling-tolerance]]

---

## Knowledge Graph Links

### Related Genes
- [[osbhlh150]] — Upstream transcription factor; directly activates OsNCED3
- [[osmapk3-rice]] — Upstream kinase; phosphorylates OsbHLH150 to enhance OsNCED3 activation

### Related Pathways
- [[aba-biosynthesis-stress]] — ABA biosynthesis and stress response pathway

### Related Entities
- [[rice-chilling-tolerance]] — Paper concept
- [[guangxi-university-luo-lab]] — Research group
