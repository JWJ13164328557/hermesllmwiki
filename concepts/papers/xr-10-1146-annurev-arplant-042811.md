title: "Plant Stem Cell Niches"
type: paper
journal: "Annual Review of Plant Biology"
year: 2012
authors:
  - Aichinger E
  - Kornet N
  - Friedrich T
  - Laux T
pmid: "22224452"
doi: "10.1146/annurev-arplant-042811-105555"
paper_type: review
species:
  - Arabidopsis thaliana
  - Oryza sativa
  - Zea mays
  - Pinus spp.
technology:
  - genetic perturbation (mutant analysis)
  - clonal analysis
  - live imaging (confocal)
  - in situ hybridization
  - reporter gene analysis
  - laser ablation
  - peptide application
cell_number: null
dataset_accession: null
status: reviewed
confidence: high
updated: "2026-05-29"
tags:
  - stem-cell-niche
  - meristem
  - SAM
  - RAM
  - vascular-cambium
  - WUSCHEL
  - WOX5
  - WOX4
  - CLV3
  - CLE-peptides
  - mobile-signals
  - transcriptional-modules
  - stem-cell-maintenance
  - cell-fate
  - review
  - arabidopsis
resource:
  - ""
tags: [#developmental-biology, papers]
---

# Plant Stem Cell Niches

---

## 1. Scientific Context

### Existing Consensus (Before This Paper)

By 2012, two decades of Arabidopsis genetics had established the outlines of plant stem cell biology, but the field was fragmented. Individual meristems were studied largely in isolation by separate research communities. Key consensus:

- **Plants have lifelong, postembryonic organogenesis** from meristems — the shoot apical meristem (SAM), root apical meristem (RAM), and vascular cambium — each containing pluripotent stem cells maintained in specialized microenvironments called niches
- **SAM**: The *WUSCHEL* (*WUS*) homeodomain transcription factor is the central stem cell regulator, expressed in the organizing center (OC). *CLAVATA3* (*CLV3*), a secreted CLE peptide ligand expressed in overlying stem cells, signals through CLV1/CLV2 receptors to restrict *WUS* expression — forming a negative feedback loop
- **RAM**: The quiescent center (QC) is the niche organizer; *WOX5* (a *WUS*-related homeobox gene) is expressed in the QC and maintains surrounding initials. *PLETHORA* (AP2/ERF) transcription factors confer stem cell competence. *SHORTROOT* (*SHR*) moves from stele to activate *SCARECROW* (*SCR*) in the endodermis, enabling asymmetric division
- **Vascular cambium**: *WOX4* was recently identified as a cambium-specific *WUS*-related gene; TDIF/CLE41/CLE44 peptides from phloem signal through TDR/PXY receptor in procambium to promote cambium proliferation
- **Mobile signals**: *SHR* protein movement and CLE peptide diffusion were known as intercellular signals, but systematic analysis of mobile signals across niches was lacking
- **Plant stem cells are flexible**: Unlike animals, plant cells can respecify identity based on position — laser ablation of QC causes adjacent cells to adopt QC fate, demonstrating non-cell-autonomous regulation
- **The WOX gene family** (15 members in Arabidopsis) was known, with *WUS*, *WOX5*, *WOX4*, and others showing meristem-specific expression but no unified framework for their roles across niches

### Existing Models

- **CLV3-WUS feedback loop (SAM)**: A negative feedback model where CLV3 signaling restricts WUS expression, and WUS promotes CLV3 expression — self-regulating homeostasis of the stem cell pool
- **QC-centered niche (RAM)**: The QC maintains surrounding initials via short-range signals; ablation causes loss of stem cell identity and differentiation
- **Positional information model**: Plant cell fate is determined by position within the meristem rather than by lineage — distinct from animal stem cell lineage models
- **TDIF-TDR/PXY pathway (vascular)**: A peptide-receptor module promoting cambial cell proliferation while inhibiting xylem differentiation
- **Single-niche-centric view**: Each meristem was studied in isolation, with limited cross-niche conceptual integration

### Knowledge Gaps

- No systematic, integrative comparison of SAM, RAM, and vascular cambium stem cell niches
- Unclear which molecular principles are shared across niches and which are niche-specific
- Mobile signals (CLE peptides, mobile transcription factors, hormonal signals) catalogued separately — no integrated framework for how mobile signals feed into transcriptional modules to balance cell fates
- The WOX family's role across niches was recognized but not synthesized
- No conceptual bridge between the detailed molecular models of Arabidopsis and agricultural/forestry implications of long-term meristem activity (e.g., thousand-year-old trees)
- The concept of "stem cell niche" itself — borrowed from animal biology — had not been critically examined across plant meristems

### Why This Paper Matters

This is the **definitive review synthesizing plant stem cell niche biology at the molecular, cell-biological, and conceptual levels**. Written by Thomas Laux's group — the lab that discovered *WUSCHEL* and has been central to SAM and RAM niche research for two decades — it provides an authoritative framework that:

1. **Unifies SAM, RAM, and vascular cambium** under a common conceptual framework of mobile signals → transcriptional modules → cell fate balance
2. **Establishes WOX-CLE regulatory modules** as a recurring principle across all three niches
3. **Provides the critical cross-niche comparison** (shared features vs. niche-specific differences) that had been missing from the literature
4. **Bridges the Arabidopsis molecular genetics tradition** with broader evolutionary, agricultural, and developmental perspectives
5. **Serves as the conceptual foundation** for all subsequent plant stem cell single-cell transcriptomic studies — it defined the questions that scRNA-seq studies (2019 onward) would address at higher resolution

The review is Arabidopsis-centered but explicitly discusses rice, maize, and gymnosperms where comparative data existed, establishing an evolutionary framework.

---

## 2. Research Questions

### Primary Questions (for the Review)

1. What are the common organizational principles shared by shoot, root, and vascular stem cell niches in plants?
2. How do mobile signals (CLE peptides, mobile transcription factors, hormones) feed into transcriptional modules to balance stem cell maintenance with differentiation in each niche?
3. What are the key differences between niches that reflect their distinct developmental contexts and evolutionary origins?

### Secondary Questions

1. How is the WOX-CLE negative feedback module conserved and adapted across SAM, RAM, and vascular cambium?
2. What is the role of the organizing center / niche center in each meristem, and how does it maintain surrounding stem cells?
3. How do hormonal signals (auxin, cytokinin) integrate with peptide signaling to control niche activity?
4. What distinguishes the plant stem cell concept from the animal stem cell niche concept?
5. How do developmental time and longevity (seasonal dormancy vs. continuous growth; annual vs. perennial life cycles) interface with stem cell maintenance mechanisms?
6. What are the open questions and future directions for plant stem cell niche research?

### Explicit Conceptual Framework

- **Mobile signals → transcriptional modules → cell fate balance**: A unifying framework whereby extracellular signals (CLE peptides, hormones, mobile TFs) modulate transcription factor modules (WOX family, GRAS family, AP2/ERF family) that control the balance between stem cell proliferation and differentiation
- **WOX-CLE negative feedback**: A recurrent regulatory logic — WOX TFs promote stem cell identity in the niche center; CLE peptides produced by stem cells or differentiating descendants signal back to restrict WOX expression — creating self-regulating homeostasis
- **Niche center concept**: Each meristem has a small group of slowly dividing cells (OC in SAM, QC in RAM, cambial initials) that serve as a signaling center — but the cellular mechanisms differ across niches

### Implicit Research Agenda

- Single-cell transcriptomic resolution would be needed to fully dissect the mobile signal → transcriptional module → cell fate logic
- Cross-spec

## 深度提炼

**方法**: Microscopy

### 核心发现


**全文来源**: PubMed摘要
