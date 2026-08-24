# Research Program Specification

Version: 1.0

Purpose:

Define how scientific knowledge is transformed into actionable long-term research strategy.

This layer bridges knowledge synthesis and future discovery.

It is the highest operational layer of the Plant Single-Cell Research Operating System.

---

# 1 Philosophy

## What Is a Research Program?

A research program is not a project.

A research program is not a hypothesis.

A research program is not a grant proposal.

A research program is:

```text
A coherent scientific agenda
designed to resolve a major biological problem.
```

---

## Knowledge Hierarchy Position

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
    ↓
Research Program
```

---

## Core Question

Synthesis asks:

```text
What do we know?
```

Research Program asks:

```text
What should we do next?
```

---

# 2 Program Scope

A research program should address:

* One major biological system
* One major unresolved problem
* Multiple connected hypotheses
* Multi-year scientific goals

---

## Good Examples

```text
Root Stem Cell Maintenance

Cell Fate Specification

Root Regeneration

Plant Spatial Organization

Long-Distance Signaling

Stress Adaptation Networks
```

---

## Bad Examples

```text
WOX5

Figure 3 Analysis

Single Dataset
```

Too narrow.

---

# 3 Research Program Metadata

```yaml
---
type: research-program

title:

theme:

status:

priority:

confidence:

created:

updated:

related_synthesis:

related_hypotheses:

related_entities:

related_datasets:
---
```

---

# 4 Biological Problem Definition

Purpose:

Clearly define the scientific challenge.

---

## Problem Statement

One paragraph.

Example:

```text
Despite extensive characterization of WOX5,
the mechanisms maintaining long-term stem cell
identity within the root niche remain unresolved.
```

---

## Why This Matters

Explain:

* Biological importance
* Agricultural importance
* Theoretical importance

---

## Current State of Knowledge

Link to synthesis pages.

Summarize:

```text
Known

Partially Known

Unknown
```

---

# 5 Big Questions

Every program must define:

```text
3–10 major scientific questions
```

---

Example:

### Question 1

How is QC identity maintained?

---

### Question 2

How is stem-cell renewal coordinated?

---

### Question 3

How is positional information encoded?

---

Each question becomes a research axis.

---

# 6 Knowledge Map

Purpose:

Map current understanding.

---

## Established Knowledge

High-confidence facts.

---

## Emerging Knowledge

Supported but incomplete.

---

## Controversial Areas

Conflicting evidence.

---

## Unknown Areas

Major gaps.

---

# 7 Hypothesis Portfolio

A program should contain multiple hypotheses.

---

## Hypothesis Entry

```text
Observation

↓

Inference

↓

Hypothesis

↓

Prediction

↓

Experiment
```

---

Example:

```text
Observation:
WOX5 and PLT1 co-localize.

Inference:
Potential direct regulation.

Hypothesis:
WOX5 activates PLT1.

Prediction:
WOX5 binding near promoter.

Validation:
CUT&Tag.
```

---

# 8 Critical Knowledge Gaps

Purpose:

Identify bottlenecks.

---

## Mechanistic Gaps

Missing causal mechanisms.

---

## Cellular Gaps

Missing cell-state information.

---

## Spatial Gaps

Missing spatial resolution.

---

## Temporal Gaps

Missing developmental information.

---

## Comparative Gaps

Missing species-level evidence.

---

# 9 Experimental Roadmap

Most important section.

---

## Immediate Experiments

1–2 years.

Example:

```text
Spatial validation

Genetic perturbation

Reporter validation
```

---

## Mid-Term Experiments

3–5 years.

Example:

```text
Lineage tracing

Regulatory network reconstruction

Multi-omics integration
```

---

## Long-Term Experiments

5–10 years.

Example:

```text
Whole-organ simulation

Predictive developmental modeling
```

---

# 10 Dataset Roadmap

Purpose:

Define required datasets.

---

## Existing Datasets

List available resources.

---

## Missing Datasets

Examples:

```text
Spatial atlas

Time-course atlas

Mutant atlas

Stress atlas
```

---

## Priority Ranking

```text
Critical

High

Medium

Low
```

---

# 11 Technology Roadmap

Purpose:

Identify technological needs.

---

## Current Methods

Available approaches.

---

## Limitations

Current bottlenecks.

---

## Required Innovations

Needed advances.

Examples:

```text
Higher-resolution spatial methods

Longitudinal single-cell tracking

In vivo lineage recording
```

---

# 12 Species Expansion Plan

Purpose:

Avoid Arabidopsis bias.

---

## Arabidopsis

Current status.

---

## Rice

Current status.

---

## Maize

Current status.

---

## Other Crops

Knowledge gaps.

---

## Comparative Priorities

Identify where new studies are needed.

---

# 13 Risk Assessment

Every program should evaluate risk.

---

## Scientific Risk

Hypothesis may be incorrect.

---

## Technical Risk

Technology may fail.

---

## Resource Risk

Data collection difficulty.

---

## Interpretation Risk

Alternative explanations.

---

# 14 Milestone Framework

Purpose:

Track progress.

---

## Milestone 1

Foundational evidence.

---

## Milestone 2

Mechanistic validation.

---

## Milestone 3

Network reconstruction.

---

## Milestone 4

Predictive model.

---

## Milestone 5

Field-level consensus.

---

# 15 Expected Impact

Evaluate:

---

## Biological Impact

Knowledge advancement.

---

## Methodological Impact

Technology development.

---

## Agricultural Impact

Crop improvement relevance.

---

## Community Impact

Broader significance.

---

# 16 Program Dashboard

Every program should contain:

| Category             | Status |
| -------------------- | ------ |
| Knowledge Level      |        |
| Evidence Coverage    |        |
| Consensus Strength   |        |
| Dataset Availability |        |
| Technology Readiness |        |
| Hypothesis Count     |        |
| Critical Gaps        |        |
| Progress Score       |        |

---

# 17 Integration With Other Layers

---

## Inputs

Research Program consumes:

```text
Synthesis

Hypotheses

Evidence

Entities
```

---

## Outputs

Research Program generates:

```text
Research Priorities

Experimental Plans

Dataset Requirements

Technology Needs
```

---

# 18 Agent Responsibilities

The Agent must:

1. Continuously update program status
2. Track unresolved questions
3. Identify emerging opportunities
4. Link new evidence to existing programs
5. Create new programs when fields emerge
6. Rank research priorities
7. Track milestone completion
8. Generate future experiment suggestions
9. Maintain dataset roadmaps
10. Maintain technology roadmaps

---

# 19 Completion Criteria

A Research Program is complete only if it contains:

* Problem Definition
* Big Questions
* Knowledge Map
* Hypothesis Portfolio
* Critical Knowledge Gaps
* Experimental Roadmap
* Dataset Roadmap
* Technology Roadmap
* Species Expansion Plan
* Risk Assessment
* Milestones
* Impact Analysis
* Program Dashboard

Without these sections, the Research Program is incomplete.

---

# 20 Ultimate Goal

The purpose of a Research Program is not merely to organize knowledge.

Its purpose is to transform:

```text
Scientific Literature
    ↓
Scientific Understanding
    ↓
Scientific Strategy
    ↓
Scientific Discovery
```

into a continuously evolving framework that guides future research.

```
```
