---
name: plant-kb-operations
description: >
  Operate and maintain the Plant Single-Cell Knowledge Base. Use for paper ingestion,
  evidence extraction, entity management, synthesis generation, hypothesis formulation,
  research program planning, quality assurance checks, and pipeline automation.
  Triggers: knowledge base update, paper curation, evidence extraction, literature
  ingestion, synthesis generation, entity management, research program creation.
category: knowledge-base
version: 1.0.0
---

# Plant Single-Cell Knowledge Base Operations

## Overview

This skill governs all interactions with the Plant Single-Cell Knowledge Base — a multi-layer research operating system that transforms raw literature into structured, traceable, synthesis-ready scientific knowledge.

The knowledge base is located at the path specified in the user's environment (typically `hermes/` under the Obsidian vault). Before any operation, confirm the correct base path.

## When to Use

Load this skill when the user requests:
- Paper ingestion or literature curation
- Evidence extraction or quality assessment
- Entity page creation or update
- Synthesis page generation or refresh
- Hypothesis formulation or research program planning
- Knowledge base quality audit
- Pipeline or batch processing script execution
- Daily update cycle management
- Cross-reference or wikilink validation

## Core Rules (Must Follow)

1. **Traceability**: Every claim must trace through `Claim → Evidence Object → Paper Page → Raw Literature`. If this chain breaks, reject the claim.

2. **Atomic Evidence**: One Evidence Object = one scientific claim. Never bundle multiple claims.

3. **Preserve Contradictions**: Conflicting evidence must be recorded, not deleted. Note context differences (species, tissue, condition, methodology).

4. **Label Confidence**: Every claim must carry an evidence strength rating. Never present correlation as mechanism.

5. **Never Modify `raw/`**: The raw literature directory is immutable. All processed content lives in `concepts/`, `evidence/`, `entities/`, etc.

6. **Log Everything**: Every operation must append to `log.md` with date, additions, updates, and open questions.

## Ingest Workflow

When ingesting a new paper, follow this sequence. Each step produces verifiable output.

### Step 1: Pre-Ingest Validation

Verify:
- DOI/PMID is valid and resolvable
- Paper is not already in `concepts/papers/`
- PDF is readable (check for scanned-image-only)
- Paper contains primary research data
- Species is within the knowledge base scope

If any check fails, report and skip.

### Step 2: Paper Analysis

Create a paper page at `concepts/papers/{paper-id}.md` with frontmatter:

```yaml
---
type: paper
title: ""
doi: ""
year: ""
journal: ""
authors: []
species: []
tissue: []
technology: []
tags: []
status: draft
confidence: medium
---
```

Process through 8 mandatory levels:
1. **Metadata** — DOI, journal, year, authors, species, tissue, technology, cell count
2. **Scientific Context** — Pre-existing consensus, models, knowledge gaps, why this paper matters
3. **Research Questions** — Primary question, secondary questions, explicit and implicit hypotheses
4. **Experimental Logic** — Question→Experiment→Observation→Interpretation chain for each major result
5. **Figure Analysis** — Per-figure: purpose, question, methods, observations, conclusions, strength rating, alternative explanations
6. **Evidence Extraction** — Convert each key claim to an atomic Evidence Object
7. **Knowledge Extraction** — Identify entities, relationships, regulatory networks
8. **Research Insight** — Critical evaluation, novelty assessment, future opportunities, open questions

### Step 3: Evidence Extraction

For each major claim in the paper:

```yaml
---
type: evidence
claim: "Single atomic scientific statement"
claim_type: observation | association | function | mechanism | consensus
species: []
tissue: []
cell_type: []
evidence_tier: 1-5
confidence: low | medium | high
support: ["[[paper-id]]"]
contradictions: []
---
```

Required sections:
- **Claim** — One sentence, atomic
- **Biological Context** — System, condition, developmental stage
- **Supporting Evidence** — Source paper, figures, experiments
- **Evidence Quality** — Tier (T1-T5) and justification
- **Contradictory Evidence** — If any exists (never leave blank if contradictions exist)
- **Consensus Assessment** — emerging | moderate | strong | established
- **Alternative Models** — Competing explanations
- **Open Questions** — What remains unresolved

Evidence pages go to `evidence/{claim-slug}.md`.

### Step 4: Entity Updates

For every biological entity referenced in the paper (genes, proteins, cell types, tissues, species, pathways):

1. Create entity page if missing at the appropriate subdirectory
2. Add evidence-backed claims with source links
3. Update functional evidence matrix
4. Add expression pattern only if directly supported
5. Add regulatory relationships only if directly supported
6. Record contradictions when present
7. Add open questions when unresolved

Entity pages follow type-specific templates defined in the SOP. Minimum frontmatter:

```yaml
---
type: entity
entity_type: gene | protein | pathway | cell-type | tissue | species | dataset | lab
name: ""
status: seed | draft | reviewed | stable | deprecated
confidence: low | medium | high | mixed
---
```

### Step 5: Relationship Extraction

For every entity-to-entity relationship discovered:

```
Entity A → [relationship_type] → Entity B
```

Supported types: `activates`, `represses`, `interacts_with`, `expressed_in`, `marks`, `required_for`, `sufficient_for`, `correlates_with`, `maintains`, `promotes`, `inhibits`.

Record: relationship type, biological context, evidence support level, confidence.

### Step 6: Synthesis Integration

If the paper affects broader topic understanding, update the relevant synthesis page at `synthesis/{topic}.md`.

Update: current consensus, evidence synthesis, regulatory network, competing models, knowledge gaps, future directions.

Do not update synthesis with weak claims unless clearly labeled as "emerging" or "speculative."

### Step 7: Index and Log

Update `index.md` if new topics or entities are introduced. Append to `log.md`:

```markdown
## YYYY-MM-DD
### Added
- {paper-id}: {title}
### Evidence Created
- {claim-slug} (×N)
### Entity Updates
- {entity-name}: {change summary}
### Notes
- {any observations}
```

## Evidence Quality Assessment

When assigning evidence tiers, use this rubric:

| Tier | Name | Signal Methods | Confidence |
|------|------|---------------|------------|
| T1 | Mechanistic Proof | ChIP, CUT&Tag, genetic rescue, reporter validation | Highest |
| T2 | Functional Validation | Mutant phenotype, overexpression, knockdown | High |
| T3 | Spatial Support | Spatial transcriptomics, ISH, reporter lines | Medium |
| T4 | Correlative | scRNA-seq, co-expression, trajectory inference | Low-Medium |
| T5 | Speculative | Discussion claims only | Not consensus |

Evidence strength upgrade rules:
- Low→Medium: Multiple observations OR one functional experiment
- Medium→High: Independent studies + multiple methods + no unresolved contradictions
- High→Consensus: Independent replication + mechanistic support + synthesis consensus

## Batch Processing

When running batch curation (multiple papers):

1. Process papers sequentially, verifying output at each step
2. Do NOT skip evidence extraction for speed — every paper must produce 3+ Evidence Objects
3. Synthesis rebuild is always **full-scale** (not incremental) — all synthesis pages are regenerated from all evidence
4. Monitor for: DOI deduplication failures, PDF text extraction errors, species misattribution
5. Log per-paper statistics: evidence count, entity count, any failures

## Quality Gates

A paper ingest is complete only when all of these are true:
- [ ] Paper page follows the 8-level analysis standard
- [ ] All main figures are analyzed
- [ ] All key claims are converted to atomic Evidence Objects (minimum 3)
- [ ] All referenced entities have updated pages
- [ ] All extracted relationships are recorded
- [ ] Contradictions are checked and preserved
- [ ] Relevant synthesis pages are updated
- [ ] Open questions are recorded
- [ ] `log.md` and `index.md` are updated

## Common Pitfalls

1. **Claim bundling** — "WOX5 and PLT1 regulate root development" is two claims. Split them.
2. **Trajectory = lineage** — Pseudotime is computational inference, not lineage tracing. Label accordingly.
3. **Correlation = regulation** — Co-expression does not prove direct regulation. Require T1/T2 evidence.
4. **Arabidopsis generalization** — Do not assume Arabidopsis mechanisms apply to all plants without evidence.
5. **Deleting contradictions** — Conflicting evidence must be preserved, not removed.
6. **Skipping figure analysis** — Figures contain the primary evidence. Every main figure must be analyzed.
7. **Modifying raw/** — Raw files are immutable. All curation output goes to `concepts/`, `evidence/`, `entities/`.

## Reference

Full operating procedures, entity templates, and evidence specifications are documented in `SOP.md`. Load that file for detailed field definitions, template structures, and edge case handling.
