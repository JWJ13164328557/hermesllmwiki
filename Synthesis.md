# Synthesis Specification

Version: 1.0

Purpose:

Define how scientific knowledge is synthesized across papers, evidence objects, entities, and relationships to construct field-level understanding.

This layer transforms evidence into consensus and enables review writing, hypothesis generation, and research planning.

---

# 1 Philosophy

## What Is Synthesis?

Synthesis is not a summary.

Synthesis is not a literature review.

Synthesis is:

```text
Evidence
+
Consensus
+
Contradictions
+
Knowledge Gaps
+
Future Directions
```

organized around a biological question.

---

## Why Synthesis Exists

Papers answer:

```text
What did this study discover?
```

Evidence answers:

```text
Is this claim supported?
```

Synthesis answers:

```text
What does the field currently believe?
```

---

# 2 Synthesis Object

Each synthesis page focuses on one scientific topic.

Examples:

```text
root-stem-cell-niche

cell-fate-transition

lateral-root-initiation

vascular-development

spatial-patterning

stress-response
```

---

# 3 Synthesis Metadata

```yaml
---
type: synthesis

topic:

status:

confidence:

updated:

related_entities:

related_evidence:

related_hypotheses:
---
```

---

# 4 Topic Definition

Every synthesis page begins with:

## Biological Scope

Define:

```text
Species

Tissues

Cell Types

Developmental Context

Environmental Context
```

Example:

```text
Arabidopsis Root

Stem Cell Niche

QC

Early Development
```

---

# 5 Historical Evolution

Purpose:

Knowledge changes over time.

The synthesis page must document how understanding evolved.

---

## Historical Timeline

Format:

```markdown
Year

Discovery

Impact
```

Example:

```text
2004

WOX5 identified

QC marker established

↓

2011

WOX5 loss-of-function phenotype

Functional evidence

↓

2020

Single-cell atlas

Cell-state diversity discovered

↓

2026

Spatial atlas

Microenvironment model proposed
```

---

## Paradigm Shifts

Record major changes.

Example:

```text
Old Model

Static QC

↓

New Model

Dynamic stem-cell niche
```

---

# 6 Current Consensus

Most important section.

---

## Consensus Statements

Each statement must be evidence-backed.

Format:

```markdown
Consensus Statement

Supporting Evidence

Confidence
```

Example:

```text
WOX5 is a core regulator of QC maintenance.

Supporting Evidence:
17 studies

Confidence:
Strong
```

---

## Consensus Categories

Separate:

```text
Established

Strong

Emerging

Controversial
```

---

# 7 Core Biological Questions

Break topic into sub-questions.

Example:

```text
How is QC maintained?

How are stem cells renewed?

How is positional information encoded?

How is regeneration initiated?
```

---

Each question gets its own subsection.

---

# 8 Evidence Synthesis

For every biological question:

---

## Supporting Evidence

List evidence objects.

---

## Contradictory Evidence

List opposing evidence.

---

## Evidence Strength

Evaluate:

```text
Weak

Moderate

Strong

Established
```

---

## Remaining Uncertainty

Explicitly describe unknowns.

---

# 9 Regulatory Network Model

Purpose:

Construct field-level mechanistic model.

---

## Key Entities

Genes

Proteins

Cell Types

Signals

---

## Key Relationships

Example:

```text
SHR
 ↓
activates
 ↓
SCR

SCR
 ↓
activates
 ↓
WOX5

WOX5
 ↓
maintains
 ↓
QC identity
```

---

## Confidence Annotation

Every edge must have confidence.

```text
Observed

Validated

Mechanistic

Consensus
```

---

# 10 Competing Models

Critical section.

Most reviews ignore this.

---

## Model A

Description.

Supporting evidence.

Weaknesses.

---

## Model B

Description.

Supporting evidence.

Weaknesses.

---

## Comparison

What evidence discriminates them?

---

## Missing Experiment

What experiment would resolve disagreement?

---

# 11 Cross-Species Perspective

Required whenever possible.

---

## Arabidopsis

Current understanding.

---

## Rice

Current understanding.

---

## Maize

Current understanding.

---

## Comparative Conclusions

Evaluate:

```text
Conserved

Partially Conserved

Species-Specific

Unknown
```

---

# 12 Technology Perspective

Knowledge often depends on technology.

---

## Evidence by Method

Examples:

```text
Genetics

Reporter

scRNA-seq

Spatial Transcriptomics

ATAC-seq

CUT&Tag
```

---

## Technology Biases

Potential limitations.

---

## Missing Technologies

What methods are still needed?

---

# 13 Knowledge Gaps

Most important future-oriented section.

---

## Known Unknowns

Questions everyone agrees remain unresolved.

---

## Suspected Missing Mechanisms

Likely but unproven mechanisms.

---

## Missing Datasets

Required future datasets.

---

## Missing Species

Species lacking evidence.

---

## Missing Developmental Stages

Uncharacterized stages.

---

# 14 Future Directions

Convert gaps into opportunities.

---

## Immediate Priorities

1–3 year horizon.

---

## Medium-Term Opportunities

3–5 year horizon.

---

## Long-Term Challenges

5–10 year horizon.

---

# 15 Hypothesis Generation

Every synthesis page must generate hypotheses.

---

## Observation

Current evidence.

---

## Inference

Reasoning.

---

## Hypothesis

Explicit statement.

---

## Prediction

Expected result.

---

## Validation Strategy

Required experiment.

---

## Impact

Why it matters.

---

# 16 Review-Writing Block

Purpose:

Enable automatic review generation.

---

## Executive Summary

1 page summary.

---

## Key Concepts

Important biological concepts.

---

## Major Evidence

Most important evidence objects.

---

## Consensus Table

Current field consensus.

---

## Controversy Table

Open debates.

---

## Future Outlook

Research trajectory.

---

# 17 Research Program Interface

Every synthesis page must connect to:

```text
research-programs/
```

---

Example:

```text
root-stem-cell-niche
    ↓
root-stem-cell-program
```

---

The synthesis page answers:

```text
What do we know?
```

The research program answers:

```text
What should we do next?
```

---

# 18 Agent Rules

The Agent must:

1. Synthesize across papers, not summarize papers
2. Preserve contradictory evidence
3. Separate consensus from speculation
4. Update historical timelines
5. Track paradigm shifts
6. Maintain regulatory models
7. Generate testable hypotheses
8. Identify knowledge gaps
9. Link synthesis to evidence
10. Link synthesis to research programs

---

# 19 Completion Criteria

A synthesis page is complete only if it contains:

* Topic Definition
* Historical Evolution
* Current Consensus
* Core Biological Questions
* Evidence Synthesis
* Regulatory Network
* Competing Models
* Cross-Species Analysis
* Technology Analysis
* Knowledge Gaps
* Future Directions
* Hypotheses
* Review-Writing Block
* Research Program Links

Without these sections, the synthesis page is incomplete.

```
```
