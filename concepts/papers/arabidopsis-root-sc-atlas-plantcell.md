---
title: A single-cell Arabidopsis root atlas reveals developmental trajectories in wild-type and cell identity mutants
journal: unknown
year: ''
type: paper
themes: [single-cell-spatial-omics]
tags:
- single-cell-spatial
- papers
species:
- Arabidopsis thaliana
status: frontmatter-enhanced
curation_depth: 基础整理
updated: 2026-05-30
doi: 10.1016/j.devcel.2022.01.008
title_fixed_from: A single-cell Arabidopsis root atlas reveals developmental trajectories in wild-
theme_status: mapped
theme_basis: tag

---

# A single-cell Arabidopsis root atlas reveals developmental trajectories in wild-type and cell identity mutants
## 摘要
In all multicellular organisms, transcriptional networks orchestrate organ development. The Arabidopsis root, with its simple structure and indeterminate growth, is an ideal model for investigating the spatiotemporal transcriptional signatures underlying developmental trajectories. To map gene expression dynamics across root cell types and developmental time, we built a comprehensive, organ-scale atlas at single-cell resolution. In addition to estimating developmental progressions in pseudotime, we employed the mathematical concept of optimal transport to infer developmental trajectories and identify their underlying regulators. To demonstrate the utility of the atlas to interpret new datasets, we profiled mutants for two key transcriptional regulators at single-cell resolution, shortroot and scarecrow. We report transcriptomic and in vivo evidence for tissue trans-differentiation underlying a mixed cell identity phenotype in scarecrow. Our results support the atlas as a rich community resource for unraveling the transcriptional programs that specify and maintain cell identity to regulate spatiotemporal organ development.
## 论文信息

- **期刊**: Developmental cell (2022)
- **PMID**: 35134336
- **DOI**: [10.1016/j.devcel.2022.01.008](https://doi.org/10.1016/j.devcel.2022.01.008)
- **作者**: Rachel Shahan, Che-Wei Hsu, Trevor M Nolan, Benjamin J Cole, Isaiah W Taylor, Laura Greenstreet, Stephen Zhang, Anton Afanassiev, Anna Hendrika Cornelia Vlot, Geoffrey Schiebinger

## 摘要

In all multicellular organisms,

## 相关文献

- [[alfalfa-anther-sc-atlas]]
- [[arabidopsis-root-sc-atlas-review]]
- [[b3-9WavxKoXaOzbDzGmHSgUqw]]
- [[b3-Ke_NSLIGVqOSAUr7v-xJ6A]]
- [[b3-peg1lwq2yaEXfDY9yfqzZg]]
- [[b3-peg1lwq2yaEXfDY9yfqzZg]

## 关键信息

- **物种**: Arabidopsis thaliana
- **研究主题**: development, single-cell
- **期刊**: unknown ()

## 待升级

> ⚠️ 本文缺少 PMID/DOI，无法自动获取全文。
> 建议:
> 1. 补充 DOI 或 PMID 后可升级为 5-section 精简 Paper Spec
> 2. 提供 PDF 后可人工转换为 9-section 完整 Paper Spec
> 3. 对于非学术来源（微信公众号等），保持当前格式即可

---
*P3 自动增强于 2026-05-30 | 需人工审查*
## 深度提炼

**来源**: 知识库文献

## 1. Scientific Context

### Existing Consensus (Before This Paper)

By 2022, single-cell RNA-seq had been established in plants by pioneering studies including Denyer et al. 2019 (first 10x plant scRNA-seq, ~4,700 cells) and several contemporaneous root atlases. Key prior consensus:

- **Root cell types were well-defined** anatomically: QC, columella, lateral root cap, epidermis (hair/non-hair), cortex, endodermis, pericycle, phloem, xylem
- **Key regulators established**: WOX5 (QC), SHR/SCR (endodermis/cortex radial patterning), PLT1/PLT2 (stem cell maintenance), SMB/BRN (root cap maturation)
- **Pseudotime was standard** for trajectory inference (Monocle 2, Slingshot)
- **Denyer 2019** had shown scRNA-seq could detect rare QC cells and reconstruct differentiation trajectories
- **Mutant phenotypes** of *shortroot* (shr) and *scarecrow* (scr) were well-characterized at anatomical level: shr lacks endodermis and has mixed radial identity; scr has a mixed cortex-endodermis layer

### Existing Models

- **Pseudotime-based trajectory inference**: cells ordered along a one-dimensional axis of "developmental progress"
- **QC-centered stem cell niche model**: QC maintains surrounding initials; SHR moves from stele to activate SCR in endodermis
- **Lineage-based differentiation**: cells follow fixed, irreversible lineages from stem cell → transit-amplifying → differentiated

### Knowledge Gaps

- No **organ-scale** atlas integrating multiple developmental time points
- Pseudotime limited to **one-dimensional trajectories**; cannot model branching or convergence
- No single-cell characterization of root identity mutants — unknown how loss of key regulators reshapes transcriptional landscape
- **Trans-differentiation** (cells switching from one identity to another) had not been systematically investigated at transcriptomic scale
- No community-accessible interactive atlas for root scRNA-seq data

### Why This Paper Matters

This paper introduced **optimal transport** (Waddington-OT) to plant developmental biology, replacing pseudotime with a mathematically rigorous framework that models **branching and converging trajectories** — essentially reconstructing the Waddington landscape from single-cell data. It also established the first **organ-scale root atlas** (>100,000 cells), demonstrated the atlas's utility by profiling two key mutants, and provided **transcriptomic and in vivo evidence for tissue trans-differentiation** in *scarecrow*. The data is publicly accessible through an interactive web portal, making it a lasting community resource.

---

## 2. Research Questions

### Primary Question

Can optimal transport-based trajectory inference reconstruct developmental lineages and reveal regulatory programs at organ scale in the Arabidopsis root?

### Secondary Questions

1. How do gene expression dynamics unfold across root cell types and developmental time at organ scale?
2. Can optimal transport (Waddington-OT) identify transcriptional regulators of developmental transitions more effectively than pseudotime?
3. What happens to the transcriptional landscape when key cell-identity regulators (*SHORTROOT*, *SCARECROW*) are mutated?
4. Does the *scarecrow* mutant exhibit transcriptomic and in vivo evidence of tissue trans-differentiation?
5. Can the atlas serve as a reference to interpret new experimental datasets?

### Explicit Hypotheses

- Optimal transport will recover known developmental lineages and reveal novel branching/convergence patterns that pseudotime misses
- An organ-scale atlas (multiple time points) will capture temporal gene expression dynamics inaccessible to single-time-point studies
- Mutant profiling will reveal wholesale transcriptional reprogramming rather than just loss of a single cell type
- *scarecrow* mutants will show evidence of tissue trans-differentiation (cells adopting alternative identities)

### Implicit Hypotheses

- Regulators of developmental transitions can be identified by coupling genes to transport-derived transition probabilities
- The transcriptional consequences of *shr* and *scr* loss extend beyond the anatomically affected cell layers
- A community-accessible interactive atlas will accelerate root developmental biology research

---

## 3. Experimental Logic

```
Question: What are the developmental trajectories across root cell types at organ scale?
    ↓
Experiment: 10x scRNA-seq on Arabidopsis root tips across multiple developmental
            time points, integrating >100,000 cells
    ↓
Observation: Cells cluster by cell type and developmental stage; all known root cell
             types recovered with high resolution
    ↓
New Question: Can optimal transport reconstruct developmental trajectories better
               than pseudotime?
    ↓
Experiment: Apply Waddington-OT (optimal transport) to the integrated atlas
    ↓
Observation: Optimal transport recovers known lineages (e.g., stem cell → columella)
             and reveals branching patterns; identifies transition-associated regulators
    ↓
New Question: How do key cell-identity mutants alter this landscape?
    ↓
Experiment: scRNA-seq on shortroot (shr) and scarecrow (scr) mutants;
            map mutant cells onto wild-type atlas
    ↓
Observation: shr lacks endodermis and shows mixed radial identity at transcriptomic
             level; scr shows mixed cortex-endodermis layer PLUS evidence of
             trans-differentiation toward epidermal identity
    ↓
Validation: Confocal imaging of scr mutants confirms cells expressing epidermal
            markers in ground tissue position → in vivo trans-differentiation
    ↓
Conclusion: Optimal transport + organ-scale atlas + mutant profiling reveals
            developmental trajectories and trans-differentiation; atlas is a
            generalizable community resource
```

### Why 10x Genomics?

- High throughput needed for organ-scale atlas (>100,000 cells across multiple time points)
- Droplet-based capture enables detection of rare populations and transitional states
- Commercial platform ensures reproducibility and data comparability with prior studies (Denyer 2019)

### Why Waddington-OT (Optimal Transport)?

- Pseudotime forces cells along a **single one-dimensional axis** — cannot model branching lineages or convergent differentiation
- Optimal transport provides a **probabilistic coupling** between cell distributions at different time points, modeling how populations of cells transition over time
- Identifies **transition-associated genes** by correlating expression with transport probabilities
- Mathematically grounded in the Waddington landscape metaphor: cells descend through branching valleys of a developmental potential surface

---

## 4. Figure-by-Figure Analysis

