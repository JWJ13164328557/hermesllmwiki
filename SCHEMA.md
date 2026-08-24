# Plant Single-Cell Research Operating System (PSC-ROS)

Version: 3.0

---

## Metadata

```yaml
type: guide
tags:
  - schema
  - knowledge-management
  - plant-single-cell
  - spatial-transcriptomics
  - research-os

version: 3.0
status: stable
updated: 2026-05-29
```

---

# 1. Vision

## 1.1 What This System Is

PSC-ROS (Plant Single-Cell Research Operating System) is a long-term scientific knowledge system designed for:

* Plant single-cell transcriptomics
* Spatial transcriptomics
* Developmental biology
* Gene regulatory networks
* Cell fate specification
* Comparative plant genomics

The system is not a literature manager.

The system is not a note-taking application.

The system is not a PDF archive.

The system is a structured scientific reasoning framework that continuously transforms literature into reusable knowledge.

---

## 1.2 Long-Term Goal

Transform:

```text
Paper Collection
```

into

```text
Scientific Understanding
```

and ultimately into

```text
Plant Single Cell Expert System
```

capable of:

* Literature QA
* Knowledge retrieval
* Cross-paper synthesis
* Consensus detection
* Contradiction discovery
* Hypothesis generation
* Research planning
* Review writing

---

## 1.3 Core Principle

Every statement in the system must be traceable.

```text
Overview
    ↓
Research Program
    ↓
Hypothesis
    ↓
Synthesis
    ↓
Relationship
    ↓
Entity
    ↓
Evidence
    ↓
Paper
    ↓
Raw Literature
```

Knowledge without evidence is prohibited.

Hypotheses must never be stored as facts.

Consensus must never be confused with observation.

---

# 2. Knowledge Philosophy

## 2.1 The Problem with Traditional Literature Notes

Most literature systems stop at:

```text
Paper
↓
Summary
```

This creates a collection of disconnected notes.

After reading 500 papers, users still cannot answer:

* What is the strongest evidence for WOX5 function?
* What is the current consensus on QC maintenance?
* Which conclusions remain controversial?
* What experiments should be performed next?

---

## 2.2 Knowledge Must Be Reorganized

Knowledge should not remain inside papers.

Knowledge should be extracted into:

```text
Paper
↓
Evidence
↓
Entity
↓
Relationship
↓
Synthesis
↓
Hypothesis
```

This allows knowledge to accumulate across publications.

---

## 2.3 Scientific Knowledge Is Hierarchical

Different knowledge objects serve different purposes.

### Observation

What was observed?

Example:

```text
WOX5 transcripts are enriched in QC cells.
```

---

### Interpretation

What does the observation suggest?

Example:

```text
WOX5 may regulate QC identity.
```

---

### Mechanism

What causal relationship is proposed?

Example:

```text
WOX5 maintains QC identity through downstream transcriptional regulation.
```

---

### Consensus

What does the field collectively believe?

Example:

```text
WOX5 is a central regulator of QC maintenance.
```

---

### Hypothesis

What remains to be tested?

Example:

```text
WOX5 directly activates PLT1.
```

These layers must remain separated.

---

# 3. Repository Architecture

## 3.1 Top-Level Structure

```text
wiki/

├── index.md
├── log.md

├── papers/
├── evidence/

├── entities/
│   ├── genes/
│   ├── proteins/
│   ├── pathways/
│   ├── cell-types/
│   ├── tissues/
│   ├── species/
│   ├── datasets/
│   └── labs/

├── relationships/

├── datasets/

├── methods/

├── comparisons/

├── synthesis/

├── hypotheses/

├── research-programs/

├── overviews/

└── reports/
```

---

## 3.2 Knowledge Flow

```text
Raw Literature
        ↓
Paper Analysis
        ↓
Evidence Extraction
        ↓
Entity Update
        ↓
Relationship Construction
        ↓
Cross-Paper Synthesis
        ↓
Hypothesis Generation
        ↓
Research Program Formation
        ↓
Field-Level Overview
```

This pipeline defines how knowledge enters and evolves within the system.

---

# 4. Knowledge Object Definitions

## 4.1 Paper

Represents one scientific publication.

Purpose:

```text
Reconstruct Scientific Reasoning
```

Paper pages answer:

* What question was asked?
* Why was it important?
* What evidence was generated?
* What conclusions were drawn?
* How did the paper change the field?

---

## 4.2 Evidence

Represents one scientific claim.

Purpose:

```text
Store Verifiable Knowledge
```

Example:

```text
WOX5 maintains QC identity
```

One evidence page corresponds to one claim.

---

## 4.3 Entity

Represents a biological object.

Examples:

```text
WOX5
PLT1
QC
Endodermis
Arabidopsis
```

Purpose:

```text
Aggregate Knowledge
```

Entities collect all evidence relevant to that object.

---

## 4.4 Relationship

Represents a connection between entities.

Example:

```text
WOX5 activates PLT1
```

Purpose:

```text
Construct Biological Networks
```

---

## 4.5 Synthesis

Represents current understanding of a topic.

Example:

```text
Root Stem Cell Niche
```

Purpose:

```text
Build Scientific Consensus
```

---

## 4.6 Hypothesis

Represents a testable scientific proposition.

Purpose:

```text
Generate Future Research
```

Every hypothesis must include:

* supporting evidence
* missing evidence
* validation strategy

---

## 4.7 Research Program

Represents a long-term scientific agenda.

Purpose:

```text
Guide Future Discovery
```

Examples:

```text
Root Stem Cell Program

Plant Cell Fate Program

Spatial Regulation Program
```

---

## 4.8 Overview

Represents field-level understanding.

Purpose:

```text
Map The Entire Research Landscape
```

Examples:

```text
Stem Cell Niche

Cell Fate Transition

Spatial Patterning

Root Development
```

---

# 5. Evidence-Based Knowledge Policy

## Allowed

```text
Observation
Evidence
Validated Relationship
Consensus
```

---

## Restricted

```text
Interpretation
Speculation
Inference
```

Must be clearly labeled.

---

## Prohibited

```text
Unsupported Conclusions
AI-Generated Facts
Untraceable Knowledge
```

Any statement without a traceable source should not enter the knowledge layer.

---

# 6. Hermes Agent Responsibilities

The Agent must:

1. Preserve traceability
2. Preserve original evidence
3. Distinguish facts from hypotheses
4. Detect contradictions
5. Update entity knowledge
6. Update relationship knowledge
7. Update synthesis pages
8. Record all modifications
9. Maintain wikilinks
10. Never overwrite conflicting evidence

---

# 7. Golden Rule

Every knowledge object must answer:

```text
Where did this come from?
```

Every hypothesis must answer:

```text
How can this be tested?
```

Every synthesis page must answer:

```text
What does the field currently believe?
```

Every overview page must answer:

```text
Where is the field going?
```

If these questions cannot be answered, the page is incomplete.

```
```
