---
type: entity
entity_type: gene
name: "MpCYCD;1"
aliases: ["Cyclin D1", "MpCYCD1", "MpCYCD;1 cyclin", "Marchantia G1-phase cyclin"]
summary: "MpCYCD;1 is the sole G1-phase cyclin in Marchantia polymorpha and the key proliferation gatekeeper in its minimalist cell cycle system. Unlike MpCYCA and MpCYCB;1 (whose overexpression arrests growth), MpCYCD;1 overexpression is sufficient to drive cell cycle re-entry, proliferation, and dedifferentiation — making it the master switch for cell division in Marchantia."
status: reviewed
confidence: high
updated: "2026-05-29"
related_papers:
  - "[[plant-cell-cycle-control]]"
  - "[[cell-cycle-scrna-seq]]"
related_evidence:
  - "[[snRNA-seq-valid-plant-transcriptomics]]"
  - "[[snRNA-seq-additional-plant-cell-subtypes]]"
related_synthesis: []
---

# MpCYCD;1

## Summary

MpCYCD;1 is the D-type cyclin in *Marchantia polymorpha* (common liverwort) and the **sole G1-phase-dominant cyclin** in its minimalist cell cycle system. It is the most functionally distinctive of the three Marchantia core cyclins: while MpCYCA (S) and MpCYCB;1 (G2/M) overexpression causes growth arrest, **MpCYCD;1 overexpression is sufficient to drive cell cycle re-entry, promote proliferation, and induce dedifferentiation**. This asymmetry — G1 cyclin as proliferation driver vs. S/M cyclins as temporal executors — reveals a fundamental design principle of the eukaryotic cell cycle: the G1/S decision is the primary commitment point. In flowering plants, multiple CYCD paralogs buffer this function; Marchantia retains a single non-redundant CYCD;1, making it an exceptionally clean experimental system. Evidence is from Romani & Haseloff et al. (*The Plant Cell*), integrating scRNA-seq, live fluorescent reporter imaging, and overexpression phenotyping (Romani & Haseloff et al., 2025).

---

## Biological Roles

### G1-phase Cyclin and Cell Cycle Re-entry Gatekeeper

MpCYCD;1 is the single cyclin that dominates G1 in Marchantia and is uniquely capable of driving cells from quiescence back into the proliferative cycle.

Evidence:
- scRNA-seq: MpCYCD;1 expression specifically enriched in G1-phase cells, with clean temporal boundaries
- Live fluorescent reporter: G1-specific protein accumulation
- Overexpression: sufficient to drive cell cycle re-entry and proliferation

Confidence: **Strong** (scRNA-seq + live imaging + gain-of-function)

### Proliferation Driver — Promotes Cell Division

Unlike MpCYCA and MpCYCB;1, MpCYCD;1 overexpression actively promotes proliferation rather than causing growth arrest. This functional asymmetry is a defining feature of the minimalist system.

Evidence:
- OE-MpCYCD;1 lines show enhanced cell proliferation
- OE-MpCYCD;1 promotes dedifferentiation of mature cells
- Contrasts with OE-MpCYCA (arrest) and OE-MpCYCB;1 (arrest)

Confidence: **Strong** (clear phenotypic contrast between three cyclins)

### Promotes Dedifferentiation

Overexpression of MpCYCD;1 can drive differentiated cells back into a proliferative state, indicating a role in cellular reprogramming.

Evidence:
- OE-MpCYCD;1 induces dedifferentiation in thallus tissue
- Suggests MpCYCD;1 may override differentiation-state maintenance

Confidence: **Moderate** (observed phenotype; mechanism uncharacterized)

---

## Expression Pattern

### Tissue
Expressed in proliferating cells of the vegetative thallus (gametophyte), with enrichment in meristematic regions (apical notch) and gemma cups where active cell division occurs.

### Phase Specificity
G1-phase-specific — scRNA-seq shows MpCYCD;1 expression marks G1 cells with minimal overlap with S or G2/M phases.

### Protein Dynamics
- G1-specific accumulation
- Protein levels decline at G1/S transition as MpCYCA expression rises
- Protein turnover and subcellular localization contribute to phase specificity

### Evidence
- scRNA-seq of Marchantia thallus (Romani & Haseloff et al., 2025)
- Live fluorescent reporter imaging

### Caveats
Expression data is from whole-thallus scRNA-seq. Cell-type-specific variation in MpCYCD;1 levels across different proliferating cell populations has not been resolved. The factors that maintain MpCYCD;1 expression in meristematic cells versus repress it in differentiated cells are unknown.

---

## Functional Evidence Matrix

| Function | Species | Tissue | Evidence Type | Evidence Object | Strength |
|---|---|---|---|---|---|
| G1 cyclin — non-redundant | Marchantia | Vegetative thallus | scRNA-seq + live reporter | [[plant-cell-cycle-control]] | Strong |
| Cell cycle re-entry driver | Marchantia | Vegetative thallus | Overexpression phenotyping | [[plant-cell-cycle-control]] | Strong |
| Proliferation promotion | Marchantia | Vegetative thallus | OE phenotyping (enhanced cell division) | [[plant-cell-cycle-control]] | Strong |
| Dedifferentiation induction | Marchantia | Vegetative thallus | OE phenotyping (mature → proliferative) | [[plant-cell-cycle-control]] | Moderate |
| G1 specificity (clean temporal boundaries) | Marchantia | Vegetative thallus | scRNA-seq phase assignment | [[cell-cycle-scrna-seq]] | Strong |

---

## Regulatory Network

### Upstream Regulators

| Regulator | Relationship | Evidence | Confidence |
|---|---|---|---|
| Developmental/proliferation signals | Transcriptional activation in meristematic cells | Inferred from spatial expression pattern | Moderate (mechanism uncharacterized) |
| G1/S checkpoint machinery | Presumptive regulation at G1/S transition to allow CYCA expression | Inferred from phase transition logic | Low (not directly tested) |

### Downstream Targets

| Target | Relationship | Evidence | Confidence |
|---|---|---|---|
| CDK partners | MpCYCD;1 binds and activates G1 CDKs to drive G1/S transition | Inferred from cyclin-CDK paradigm | Low |
| S-phase entry machinery | Drives cell cycle progression into S-phase | Implied by overexpression phenotype | Low |

### Feedback Loops

| Loop | Evidence | Confidence |
|---|---|---|
| Proliferation → sustained MpCYCD;1 expression | Implied by meristematic expression pattern | Low |

---

## Cell-Type Associations

| Cell Type | Role | Evidence | Confidence |
|---|---|---|---|
| Meristematic/proliferating thallus cells | G1 progression; cell cycle re-entry gatekeeper | scRNA-seq + reporter | Moderate |
| Mature differentiated cells | Target of OE-induced dedifferentiation | OE phenotyping | Moderate |
| Not resolved at individual cell-type level | — | — | — |

*Marchantia thallus cell types have not been fully catalogued at single-cell resolution. MpCYCD;1 may have differential roles in distinct proliferating cell populations (stem cells, transit-amplifying cells, gemma initials).*

---

## Developmental Context

### Vegetative Gametophyte (Thallus)
MpCYCD;1 function demonstrated in the vegetative thallus — the dominant haploid life stage. MpCYCD;1 is the key driver of cell proliferation in the apical notch meristem and gemma cups.

### Dedifferentiation Context
OE-MpCYCD;1 can re-activate proliferation in mature thallus tissue, suggesting it can override developmental cell cycle exit. The natural context where dedifferentiation occurs (wounding, regeneration) and whether endogenous MpCYCD;1 mediates it is unknown.

### Reproductive Stages
Role in gametangia development, sporophyte growth, or meiosis not characterized.

---

## Stress or Environmental Context

### Normal Proliferation (Primary Context)
MpCYCD;1 characterized under standard growth conditions.

### Stress Responses
No data on whether stress signals (nutrient limitation, wounding, cold) modulate MpCYCD;1 expression or activity. In flowering plants, CYCD expression is often growth-condition-responsive; whether the minimalist Marchantia system retains this coupling is unknown.

---

## Cross-Species Conservation

### Arabidopsis
Arabidopsis has multiple CYCD genes (CYCD1-CYCD7) with tissue-specific and condition-specific expression and partial functional redundancy. No single Arabidopsis CYCD is the sole G1 driver — the redundant system makes functional dissection more difficult. MpCYCD;1 represents the ancestral, non-redundant state.

### Other Bryophytes
*Physcomitrium patens* has more CYCD paralogs than Marchantia, though fewer than Arabidopsis. Marchantia's single CYCD;1 represents the most reduced state known among land plants.

### Other Eukaryotes
D-type cyclins (animal Cyclin D1-3) are conserved G1 regulators. However, metazoan cyclin Ds also have CDK-independent functions; whether MpCYCD;1 has non-catalytic roles is unknown.

### Conservation Assessment: **Ancestral** — The single CYCD;1 in Marchantia represents the predicted ancestral land plant state. CYCD family expansion in flowering plants is derived. Functional conservation of CYCD as a proliferation driver is deeply conserved across eukaryotes.

---

## Evidence Strength

| Evidence Category | Strength | Basis |
|---|---|---|
| Transcriptional (scRNA-seq) | Strong | Single-cell resolution, G1-specific pattern |
| Protein (live reporter) | Strong | Protein dynamics validated |
| Functional — overexpression (proliferation) | Strong | Robust, reproducible phenotype |
| Functional — overexpression (dedifferentiation) | Moderate | Clear phenotype but mechanism unresolved |
| Biochemical (CDK partners) | Weak | Not characterized |
| Cross-species | Moderate | Phylogenetic inference; functional parallels |

**Overall Confidence: High** — MpCYCD;1's role as the G1 cyclin and proliferation gatekeeper is well-supported. The unique functional asymmetry (OE drives proliferation, unlike OE-MpCYCA/MpCYCB;1) is the most striking finding. Independent replication, CDK partner identification, and characterization of endogenous dedifferentiation role are needed.

---

## Contradictions and Context Dependence

### Functional Asymmetry: Why does CYCD;1 OE promote proliferation while CYCA/CYCB;1 OE arrests growth?
- **Observation**: MpCYCD;1 overexpression drives proliferation; MpCYCA and MpCYCB;1 overexpression causes arrest.
- **Interpretation**: This suggests a fundamental design principle — G1 is the commitment gateway (permissive), while S and M are execution phases (must be temporally restricted). Constitutive S/M cyclin activity disrupts the oscillatory cycle; constitutive G1 cyclin activity simply keeps the gateway open.
- **Caveat**: The mechanistic basis of this asymmetry (differential CDK substrate specificity? differential degradation machinery? different checkpoint coupling?) is not resolved.

### Context Dependence
- **Life stage**: Only tested in vegetative gametophyte; sporophyte and reproductive cell cycle regulation unknown.
- **Growth conditions**: Standard laboratory conditions; environmental modulation of CYCD;1-driven proliferation untested.
- **Genetic background**: Single Marchantia accession.

---

## Open Questions

### Question 1: What is the mechanistic basis for CYCD;1 OE driving proliferation while CYCA/CYCB;1 OE causes arrest?
- **Why It Matters**: Understanding this functional asymmetry could reveal universal principles of cell cycle commitment vs. execution.
- **Missing Evidence**: Comparative CDK substrate identification; differential degradation kinetics; checkpoint coupling differences.
- **Suggested Experiment**: Phosphoproteomics comparing OE-CYCD;1 vs. OE-CYCA/CYCB;1 lines; CDK substrate identification for each cyclin.

### Question 2: Does endogenous MpCYCD;1 mediate natural dedifferentiation (e.g., during regeneration)?
- **Why It Matters**: MpCYCD;1's dedifferentiation ability could be a regeneration tool if it mediates natural regenerative responses.
- **Missing Evidence**: MpCYCD;1 expression during wounding or regeneration; loss-of-function effect on regeneration.
- **Suggested Experiment**: Wounding assay + MpCYCD;1 reporter; CR-MpCYCD;1 regeneration assay.

### Question 3: What transcription factors regulate MpCYCD;1 expression in meristematic vs. differentiated cells?
- **Why It Matters**: Understanding the upstream control of this proliferation gatekeeper would identify the regulatory logic that confines cell division to meristems.
- **Missing Evidence**: Promoter analysis; transcription factor identification.
- **Suggested Experiment**: Promoter deletion analysis; Y1H screen for MpCYCD;1 promoter-binding TFs.

### Question 4: Can MpCYCD;1 be ported to crops for growth engineering?
- **Why It Matters**: A single-gene proliferation driver could simplify crop growth engineering compared to manipulating redundant multi-gene CYCD families.
- **Missing Evidence**: Heterologous expression in Arabidopsis or rice; functional complementation.
- **Suggested Experiment**: Express MpCYCD;1 in Arabidopsis cycd multiple mutant; assess proliferation rescue.

---

## Key References

1. Romani F. & Haseloff J. et al. (2025). A simple cell-cycle control system in Marchantia polymorpha provides a framework for understanding plant cell proliferation. *The Plant Cell*. — [[plant-cell-cycle-control]] — **Primary evidence for all claims on this page.**

---

## Knowledge Graph Links

### Related Genes
- [[mpcyca]] — S-phase cyclin; DNA replication (downstream in cell cycle)
- [[mpcycb1]] — G2/M cyclin; mitotic entry (further downstream)

### Related Concepts
- [[plant-cell-cycle-control]] — Plant cell cycle regulatory framework
- [[cell-cycle-scrna-seq]] — scRNA-seq methodology for cell cycle analysis

### Related Entities
- [[marchantia-polymorpha]] — Host species; minimalist cell cycle system
- Evidence: [[snRNA-seq-valid-plant-transcriptomics]]
