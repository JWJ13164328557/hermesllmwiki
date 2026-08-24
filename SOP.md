# Plant Single-Cell Knowledge Base — Standard Operating Procedure

Version: 1.0

## 1. Architecture Overview

The knowledge base transforms raw literature into a multi-layer research operating system. It is not a note repository — it is a structured knowledge graph designed to support hypothesis generation and research program planning.

### 1.1 Directory Map

```
hermes/
├── concepts/papers/       # Paper analysis pages (one per paper)
├── evidence/              # Atomic scientific claims (Evidence Objects)
├── entities/              # Biological entity hubs
│   ├── genes/             #   Gene-centric knowledge
│   ├── cell-types/        #   Cell-type definitions and markers
│   ├── proteins/          #   Protein function and interactions
│   ├── species/           #   Species-level knowledge
│   ├── datasets/          #   Dataset metadata
│   └── labs/              #   Research group tracking
├── relationships/         # Entity-to-entity relationship pages
├── synthesis/             # Topic-level knowledge integration
├── hypotheses/            # Testable, falsifiable hypotheses
├── research-programs/     # Long-term research agendas
├── overview/              # Top-level navigation and summaries
│   ├── themes/            #   Thematic overview pages
│   ├── tissues/           #   Tissue-level overviews
│   └── species/           #   Species-level overviews
├── raw/                   # Immutable source material
│   ├── papers/            #   PDF files (never modified)
│   ├── articles/          #   Full-text markdown extracts
│   ├── figures/           #   Extracted figures
│   ├── datasets/          #   Raw data files
│   └── supplements/       #   Supplementary materials
├── queries/               # Saved search/query definitions
├── reports/               # Generated analysis reports
├── diagrams/              # Visual outputs (graph, flowcharts)
├── comparisons/           # Cross-paper comparisons
├── sources/               # External source tracking
├── scripts/               # Automation and curation scripts
├── index.md               # Knowledge base entry point
├── log.md                 # Operation log
└── AGENT.md               # Agent operational instructions
```

### 1.2 Knowledge Transformation Pipeline

```
Raw Literature (PDF)
    ↓
Paper Analysis (concepts/papers/)
    ↓
Evidence Objects (evidence/)
    ↓
Entity Updates (entities/)
    ↓
Relationship Updates (relationships/)
    ↓
Synthesis (synthesis/)
    ↓
Hypotheses (hypotheses/)
    ↓
Research Programs (research-programs/)
```

Every layer preserves full traceability back to the source paper. No claim may exist without a verifiable evidence chain.

---

## 2. Paper Ingestion Standard

### 2.1 Pre-Ingestion Checks

Before processing a paper, verify:
- DOI/PMID is valid and not already ingested
- PDF is readable (not scanned image-only)
- Species is plant-relevant
- The paper contains primary research data (not commentary/erratum)

### 2.2 Paper Analysis Levels

Every paper must be processed through eight mandatory levels:

| Level | Name | Purpose |
|-------|------|---------|
| L1 | Metadata | DOI, PMID, journal, year, authors, species, tissue, technology |
| L2 | Scientific Context | Pre-existing consensus, models, knowledge gaps |
| L3 | Research Questions | Primary question, secondary questions, explicit/implicit hypotheses |
| L4 | Experimental Logic | Question→Experiment→Observation→Interpretation chain |
| L5 | Figure Analysis | Per-figure: purpose, question, methods, observations, conclusions, strength |
| L6 | Evidence Extraction | Convert claims to atomic Evidence Objects |
| L7 | Knowledge Extraction | Identify entities, relationships, regulatory networks |
| L8 | Research Insight | Critical evaluation, future opportunities, open questions |

No level may be skipped. A paper page containing only a summary is incomplete.

### 2.3 Minimum Output Per Paper

| Artifact | Minimum |
|----------|---------|
| Paper page | 1 (full analysis) |
| Evidence Objects | 3–20 |
| Entity pages | All referenced entities updated |
| Relationship pages | All extracted relationships |
| Synthesis pages | At least 1 if topic-relevant |
| log.md entry | Updated |

---

## 3. Evidence Standard

### 3.1 Philosophy

Evidence is not a paper. Evidence is not a figure. Evidence is a single scientific claim with supporting observations and experiments.

**Rule: One Evidence Object = One Claim.**

### 3.2 Evidence Hierarchy

| Level | Name | Definition | Example |
|-------|------|-----------|---------|
| L1 | Observation | Direct measurement, no interpretation | "WOX5 transcripts are enriched in QC cells" |
| L2 | Association | Observed relationship | "WOX5 expression correlates with QC identity" |
| L3 | Function | Perturbation-supported role | "WOX5 is required for QC maintenance" |
| L4 | Mechanism | Causal mechanism identified | "WOX5 directly activates PLT1" |
| L5 | Consensus | Multiple independent confirmations | "WOX5 is a core QC regulator" |

### 3.3 Evidence Quality Tiers

| Tier | Name | Examples | Confidence |
|------|------|----------|------------|
| T1 | Mechanistic Proof | ChIP, CUT&Tag, reporter validation, genetic rescue | Highest |
| T2 | Functional Validation | Mutant phenotype, overexpression, knockdown | High |
| T3 | Spatial Support | Spatial transcriptomics, ISH, reporter lines | Medium |
| T4 | Correlative Evidence | scRNA-seq, co-expression, trajectory inference | Low-Medium |
| T5 | Speculative | Discussion-only claims | Not consensus |

### 3.4 Evidence Strength Assessment

Evidence strength = Quality Tier + Replication Count + Source Independence.

| Strength | Conditions |
|----------|-----------|
| Weak | Single paper, single method |
| Moderate | Multiple experiments, single group |
| Strong | Multiple groups, multiple methods |
| Established | Independent replication, mechanistic support |

---

## 4. Entity Management

### 4.1 Entity Categories

Entities are organized by biological type: genes, proteins, pathways, cell-types, tissues, species, datasets, labs.

### 4.2 Entity Page Standard

An entity page is not an encyclopedia entry. It is an evidence-centered knowledge hub that answers:
- What is known about this object?
- What evidence supports that knowledge?
- In what biological context is it true?
- What remains unknown?

### 4.3 Required Sections (Gene Entity)

1. Summary — One paragraph: function, strongest evidence, context, uncertainty
2. Biological Roles — Grouped by function with evidence links
3. Expression Pattern — Tissue, cell type, stage, evidence type, caveats
4. Functional Evidence Matrix — Tabular: function × species × tissue × evidence × strength
5. Regulatory Network — Upstream regulators, downstream targets, feedback loops
6. Cell-Type Associations — Table: cell type, role, evidence, confidence
7. Cross-Species Conservation — Per-species status, conservation assessment
8. Contradictions — Conflicting claims, species/tissue/technical differences (never delete)
9. Open Questions — Question, why it matters, missing evidence, suggested experiment

### 4.4 Confidence Values

`low` | `medium` | `high` | `mixed`

Use `mixed` when evidence depends on species, tissue, condition, or methodology.

### 4.5 Status Lifecycle

`seed` → `draft` → `reviewed` → `stable` → `deprecated`

---

## 5. Synthesis and Hypothesis Generation

### 5.1 Synthesis Standard

A synthesis page integrates evidence across papers to answer: "What does the field currently believe?"

Required sections:
- Historical Evolution
- Current Consensus
- Core Biological Questions
- Evidence Synthesis
- Regulatory Network
- Competing Models
- Knowledge Gaps
- Future Directions
- Linked Hypotheses
- Linked Research Programs

### 5.2 Hypothesis Standard

A hypothesis must be:
- Testable and falsifiable
- Linked to supporting evidence
- Accompanied by a specific prediction
- Paired with a validation experiment
- Paired with a failure condition

### 5.3 Research Program Standard

A research program answers: "What should we do next?"

Required sections:
- Problem Definition
- Big Questions (3–10)
- Knowledge Map (Established / Emerging / Controversial / Unknown)
- Hypothesis Portfolio
- Critical Knowledge Gaps
- Experimental Roadmap (Immediate / Mid-Term / Long-Term)
- Dataset Roadmap
- Technology Roadmap
- Species Expansion Plan
- Risk Assessment
- Milestones

---

## 6. Quality Assurance

### 6.1 Golden Rule

Every claim must be traceable through:

```
Claim → Evidence Object → Paper Page → Raw Literature
```

If this chain breaks at any point, the knowledge cannot be accepted.

### 6.2 Anti-Hallucination Rules

Never:
- Infer mechanism from correlation without labeling it
- Treat scRNA-seq expression as functional proof
- Treat trajectory inference as lineage proof
- Treat co-expression as direct regulation
- Generalize Arabidopsis findings to all plants without evidence
- Convert speculation into consensus
- Delete contradictory evidence
- Modify raw/ files

### 6.3 Contradiction Handling

When contradictory evidence appears:
1. Add contradiction to the evidence page
2. Record context difference (species, tissue, condition)
3. Record technical difference (methodology)
4. Add note to relevant synthesis page
5. Add unresolved question if needed
6. Never overwrite the older claim

### 6.4 Confidence Upgrade Rules

| Upgrade | Conditions Required |
|---------|-------------------|
| Low → Medium | Multiple observations OR one functional experiment |
| Medium → High | Independent studies + multiple methods + no unresolved contradictions |
| High → Consensus | Independent replication + mechanistic/functional validation + synthesis support |

### 6.5 Task Completion Checklist

Before completing any knowledge base task:
- [ ] All new claims have verifiable sources
- [ ] All evidence links resolve correctly
- [ ] All entity pages are linked
- [ ] All contradictions are preserved
- [ ] index.md is updated
- [ ] log.md is updated with date, additions, updates, and open questions
- [ ] No raw/ file was modified

---

## 7. Automation Pipeline

### 7.1 Daily Update Cycle

The knowledge base supports automated daily ingestion through cron-scheduled pipelines. The standard cycle:

1. **Literature discovery** — Query publication databases for new plant single-cell/spatial papers
2. **Deduplication** — Check DOI against existing concept pages
3. **Full-text acquisition** — Download PDF where available (OA or institutional access)
4. **Deep curation** — Extract claims, evidence, entities, and relationships
5. **Synthesis rebuild** — Update synthesis pages with new evidence (full rebuild, no threshold gating)
6. **Hypothesis refresh** — Update or generate hypotheses based on new synthesis
7. **Research program update** — Adjust roadmaps and knowledge gaps

### 7.2 Batch Processing Rules

- Full-text extraction uses first 15 pages (≤50,000 characters) via pymupdf
- Evidence extraction uses weighted signal sentence patterns
- Synthesis rebuild is always full-scale (not incremental) to prevent drift
- All pipeline scripts log to stdout for monitoring

---

## 8. Cross-Reference Architecture

### 8.1 Wikilink Strategy

- Evidence → Source paper: `source: "[[paper-id]]"` in frontmatter
- Entity ↔ Entity: Wikilinks in body text
- Synthesis ↔ Evidence: Aggregated by theme tags

### 8.2 Tag System

Paper pages use frontmatter tags for thematic grouping. Tags enable:
- Obsidian graph visualization with color-grouped nodes
- Co-occurrence-based theme discovery via Jaccard similarity clustering
- Filtered queries and cross-referencing

### 8.3 Graph Configuration

The Obsidian graph supports `showTags` and `colorGroups` for visual navigation. Theme colors are configured in `.obsidian/graph.json`.

---

## 9. Logging and Version Control

### 9.1 Log Format

Every operation appends to `log.md`:

```markdown
## YYYY-MM-DD
### Added
### Updated
### Evidence Created
### Entity Updates
### Relationship Updates
### Synthesis Updates
### Open Questions
### Notes
```

### 9.2 Git Strategy

- All knowledge base changes are tracked via git
- `raw/` directory is in `.gitignore` (PDFs stored externally)
- Commits are descriptive and grouped by operation type
- Automated commits use standardized message formats
