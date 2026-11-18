---

title: "单细胞与空间组学 — Synthesis"
created: 2026-06-01
total_evidence: 276
total_papers: 138
library_papers: 405  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-17
tags: [synthesis, single-cell, spatial-omics, transcriptomics, plant-atlas]


soybean_relevance: ⭐中
legacy_archive: _review/synthesis_legacy_20261117/single-cell-spatial-omics.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 单细胞与空间组学 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 276 | 本主题归属的证据对象数 |
| 独立论文 | 138 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 2.00 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 50% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(110)、Oryza sativa(90)、Zea mays(62)、—(24)、Plant (unspecified)(23)、Triticum aestivum(23) | 物种过度集中则外推性受限 |
| 证据类型 | omics/co-occurrence 155；descriptive/observational 96；expression/regulation 15；protein interaction 4；phenotypic/association 2；genetic perturbation 2 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42255287-f1` | 10.3389/fpls.2026.1809797 | In summary, while current systems offer specific advantages, inherent limitations–namely,  |
| `daily-42530009-f2` | 10.1093/plphys/kiag560 | Using single-cell microfluidics, transcriptomics, and metabolomics, we show that Δ glgC mu |
| `ref-j-tplants-2019-10-008-f1` | 10.1016/j.tplants.2019.10.008 | Once encapsulated in a droplet, cells are immediately lysed, releasing RNA that binds to p |
| `cr-annurev-arplant-0817-f4` | 10.1146/annurev-arplant-081720-010120 | Multiplexing Using Lipid-Tagged Indices for single-cell and single-nucleus RNA-seq (MULTI- |
| `b3-l7tWWswvI2rZ5ba_4V2BsQ-f5` | 10.1002/advs.202512295 | For instance, the snRNA-seq data demonstrated that the epidermal cell gene Zm00001eb101750 |
| `daily-42288963-f2` | 10.1093/plphys/kiag372 | Although SLIM1, RVE1, and RVE8 bind to the promoters of OAS cluster genes, only SLIM1 play |
| `root-cell-type-specific-chromatin-accessibility` | 10.1016/j.molp.2021.01.001 | Single-cell ATAC-seq of Arabidopsis roots reveals that each major cell type exhibits a dis |
| `snATAC-seq-resolves-root-cell-types` | 10.1016/j.molp.2021.01.001 | Single-nucleus ATAC-seq (snATAC-seq) of Arabidopsis roots resolves major cell types based  |
| `dpdf-10-1111-tpj-f11` | 10.1111/tpj | To the known regulators of the leaf vein, we also found novel marker genes, such as HEAVY  |
| `ref-s41477-025-02072-z-f5` | 10.1038/s41477-025-02072-z | Examining the expression of these silique guard cell markers in the context of whole-plant |
| `daily-40904198-f8` | 10.1111/pbi.70351 | The raw count data for the tissue specific target genes at each randomly sampled bin ID (l |
| `poplar-xylem-sc-spatial-gb-f5` | 10.1186/s13059-026-04007-z | Given the complementary nature of these two technologies—scRNA-seq offering high-resolutio |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 2 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 4 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 2 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 15 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 2 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 155 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 96 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42255287-f1` | 10.3389/fpls.2026.1809797 | In summary, while current systems offer specific advantages, inherent limitations–namely, a reliance |
| `daily-42530009-f2` | 10.1093/plphys/kiag560 | Using single-cell microfluidics, transcriptomics, and metabolomics, we show that Δ glgC mutants exhi |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-17 由 `rebuild_synthesis_body.py` 从 **276 条证据对象 / 138 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261117`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **276 条证据 / 138 篇文献**。规则判定为因果或直接调控的 **8 条（2.9%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **1 条**。可判定程度最高的结论集中在SLIM1：Although SLIM1, RVE1, and RVE8 bind to the promoters of OAS cluster genes, only SLIM1 plays a role in their regulation by OAS, and its effec…（[[daily-42288963-f2]]）。研究重心位于“图集构建与细胞类型注释”（183 条证据，占 66%）。证据的物种分布以 Arabidopsis thaliana 为首（110 条，40%）。七类证据均有覆盖，但遗传扰动、DNA 结合、表型关联各仅 1–2 条；主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 276 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 138 | 去重后的论文数 |
| 平均每篇证据数 | 2.00 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 49%（68/138） | 越高说明证据碎片化越严重 |
| 证据类型构成 | omics/co-occurrence(155)、descriptive/observational(96)、expression/regulation(15)、protein interaction(4)、phenotypic/association(2)、genetic perturbation(2)、DNA binding/regulation(2) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | medium(174)、low(98)、high(4) | 低置信度标注须回原文核对 |
| 主要物种 | Arabidopsis thaliana(110)、Oryza sativa(90)、Zea mays(62)、Plant (unspecified)(23)、Triticum aestivum(23)、Nicotiana tabacum(22) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 6/7（证据 <5 条的 1 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 58（21%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **8 条**，占本主题证据的 **2.9%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Arabidopsis thaliana** 出现在 110 条证据（40%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 32 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 图集构建与细胞类型注释

**规模** 183 条证据 / 102 篇文献；**构成** descriptive/observational(87)、omics/co-occurrence(78)、expression/regulation(13)、phenotypic/association(2)、DNA binding/regulation(2)、protein interaction(1)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为ZmWUS1、RVE1、sesquiterpene、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f4]]；Ruilian et al., 2024 [[a-single-cell-transcriptome-atlas-reveals-the-trajectory-of-early-cell-fate-tran-f5]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，180 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42288963-f2]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]）。
- **可检验缺口**：遗传扰动在本组缺证据；在补齐这些设计前，ZmWUS1、RVE1、sesquiterpene 与“图集构建与细胞类型注释”的方向性关系应作为待检验命题（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 0 | 8 | 1 | 28 | 36 | 74 |
| Oryza sativa | 0 | 0 | 3 | 0 | 32 | 19 | 54 |
| Zea mays | 0 | 0 | 2 | 0 | 21 | 11 | 34 |
| Plant (unspecified) | 0 | 0 | 1 | 0 | 2 | 12 | 15 |
| Nicotiana tabacum | 0 | 0 | 1 | 0 | 11 | 3 | 15 |

**基因实体（自动标注，前 5）**：ZmWUS1(2)、RVE1(2)、RVE8(2)、SLIM1(2)、OpAVT1(2)（标注覆盖 32/183）。

**化合物实体（自动标注，前 5）**：sesquiterpene(2)、lignin(2)、ginsenoside(1)、theanine(1)、suberin(1)（标注覆盖 7/183）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[time-series-single-cell-transcriptional-atlases-reveal-cell-fate-differentiation-f1]]。

**代表断言（原文摘录，未改写）**

- “Single-cell ATAC-seq of Arabidopsis roots reveals that each major cell type exhibits a distinct genome-wide chromatin accessibility landscape, with differential accessibility at ge…” — [[root-cell-type-specific-chromatin-accessibility]]（`10.1016/j.molp.2021.01.001`，DNA binding/regulation）
- “Although SLIM1, RVE1, and RVE8 bind to the promoters of OAS cluster genes, only SLIM1 plays a role in their regulation by OAS, and its effects are gene specific.” — [[daily-42288963-f2]]（`10.1093/plphys/kiag372`，protein interaction）
- “To the known regulators of the leaf vein, we also found novel marker genes, such as HEAVY METAL ASSOCIATED ISOPRENYLATED PLANT PROTEIN 36 (HIPP36), ARABIDOPSIS THALIANA HISTIDINE-C…” — [[dpdf-10-1111-tpj-f11]]（`10.1111/tpj`，omics/co-occurrence）

### 2.2 空间转录组与位置映射

**规模** 16 条证据 / 12 篇文献；**构成** omics/co-occurrence(15)、descriptive/observational(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Hordeum vulgare、Triticum aestivum、Arabidopsis thaliana，反复出现的实体为RA2、RAMOSA2、theanine；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-40904198-f1]]；[[daily-40904198-f3]]；[[daily-42028465-f4]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 16 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-40904198-f1]]；[[daily-40904198-f3]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表达相关、表型关联在本组缺证据；在补齐这些设计前，RA2、RAMOSA2、theanine 与“空间转录组与位置映射”的方向性关系应作为待检验命题（[[daily-40904198-f1]]；[[daily-40904198-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|
| Hordeum vulgare | 5 | 0 | 5 |
| Triticum aestivum | 4 | 1 | 5 |
| Arabidopsis thaliana | 5 | 0 | 5 |
| Oryza sativa | 4 | 1 | 5 |
| Zea mays | 2 | 1 | 3 |

**基因实体（自动标注，前 5）**：RA2(1)、RAMOSA2(1)（标注覆盖 1/16）。

**化合物实体（自动标注，前 5）**：theanine(1)（标注覆盖 1/16）。

**代表断言（原文摘录，未改写）**

- “Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method that substantially increases the number of RNA species that can be simultaneousl…” — [[ref-science-aaa6090-f3]]（`10.1126/science.aaa6090`，omics/co-occurrence）
- “Spatial Omics: From Two-Dimensional Sections to Thick Tissues Dissociation-based methods discard position; spatial omics recovers it, and for rice the recovered information determi…” — [[daily-42653123-f2]]（`10.3390/ijms27167114`，descriptive/observational）
- “Nevertheless, despite these limitations, technical improvements in Stereo-seq are expected to provide new insights into tissue composition and function by combining single cell tra…” — [[introducing-single-cell-stereo-sequencing-technology-to-transform-the-plant-tran-f5]]（`10.1016/j.tplants.2023.10.002`，omics/co-occurrence）

### 2.3 发育轨迹与拟时序推断

**规模** 19 条证据 / 16 篇文献；**构成** descriptive/observational(9)、omics/co-occurrence(8)、expression/regulation(2)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Gossypium hirsutum、Plant (unspecified)，反复出现的实体为EPF1、ERL1；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b3-Oe9xghJ07Ub3C93cYl12oQ-f2]]；[[b4-_dqlLGuPZxhNXXs6caCEwg-f2]]；Renhui et al., 2023 [[combining-single-cell-rna-sequencing-with-spatial-transcriptome-analysis-reveals-f1]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 19 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[b3-Oe9xghJ07Ub3C93cYl12oQ-f2]]；[[b4-_dqlLGuPZxhNXXs6caCEwg-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表型关联在本组缺证据；在补齐这些设计前，EPF1、ERL1 与“发育轨迹与拟时序推断”的方向性关系应作为待检验命题（[[b3-Oe9xghJ07Ub3C93cYl12oQ-f2]]；[[b4-_dqlLGuPZxhNXXs6caCEwg-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|
| Arabidopsis thaliana | 0 | 4 | 5 | 9 |
| Gossypium hirsutum | 2 | 1 | 1 | 4 |
| Plant (unspecified) | 0 | 1 | 2 | 3 |
| Populus spp. | 0 | 1 | 1 | 2 |
| Medicago spp. | 0 | 1 | 1 | 2 |

**基因实体（自动标注，前 5）**：EPF1(1)、ERL1(1)、HDG2(1)（标注覆盖 1/19）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[time-series-single-cell-transcriptional-atlases-reveal-cell-fate-differentiation-f1]]。

**代表断言（原文摘录，未改写）**

- “Given the complementary nature of these two technologies—scRNA-seq offering high-resolution transcriptomic profiles but restricted to thin-walled, wall-degradable cells, and snRNA-…” — [[poplar-xylem-sc-spatial-gb-f5]]（`10.1186/s13059-026-04007-z`，omics/co-occurrence）
- “Through reconstructing the differentiation process of the HF epidermal cell lineage, we found that HS and IRS are predominantly located in the later stages of the differentiation t…” — [[ms-10-3389_fcell-2026-1764812-f4]]（`10.3389/fcell.2026.1764812`，descriptive/observational）
- “Pseudotime analysis of endodermis scRNA-seq data identifies approximately 800 genes with dynamically changing expression levels as cells progress from meristematic to fully differe…” — [[endodermis-800-dynamic-genes]]（`10.1016/j.devcel.2019.02.022`，omics/co-occurrence）

### 2.4 技术平台与建库方法

**规模** 19 条证据 / 16 篇文献；**构成** omics/co-occurrence(15)、protein interaction(1)、genetic perturbation(1)、descriptive/observational(1)、DNA binding/regulation(1)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为ZmHSP90、ZmWAK2；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]；[[b3-l7tWWswvI2rZ5ba_4V2BsQ-f5]]；[[b4-B6ORjNkH1VSkcVpnv9C7xQ-f7]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，16 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]）。
- **可检验缺口**：表达相关、表型关联在本组缺证据；在补齐这些设计前，ZmHSP90、ZmWAK2 与“技术平台与建库方法”的方向性关系应作为待检验命题（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2]]；[[b3-l7tWWswvI2rZ5ba_4V2BsQ-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 0 | 1 | 0 | 6 | 1 | 8 |
| Oryza sativa | 0 | 0 | 0 | 5 | 1 | 6 |
| Zea mays | 0 | 1 | 0 | 3 | 1 | 5 |
| Glycine max | 0 | 0 | 0 | 3 | 0 | 3 |
| Plant (unspecified) | 1 | 0 | 0 | 1 | 0 | 2 |

**基因实体（自动标注，前 5）**：ZmHSP90(1)、ZmWAK2(1)（标注覆盖 1/19）。

**代表断言（原文摘录，未改写）**

- “Single-nucleus ATAC-seq (snATAC-seq) of Arabidopsis roots resolves major cell types based on differential chromatin accessibility profiles, demonstrating that the regulatory landsc…” — [[snATAC-seq-resolves-root-cell-types]]（`10.1016/j.molp.2021.01.001`，DNA binding/regulation）
- “For instance, the snRNA-seq data demonstrated that the epidermal cell gene Zm00001eb101750 ( ZmHSP90, Heat shock protein 90 ) interacts with the mesophyll cell gene Zm00001eb071970…” — [[b3-l7tWWswvI2rZ5ba_4V2BsQ-f5]]（`10.1002/advs.202512295`，protein interaction）
- “Using single-cell microfluidics, transcriptomics, and metabolomics, we show that Δ glgC mutants exhibit pronounced light sensitivity.” — [[daily-42530009-f2]]（`10.1093/plphys/kiag560`，genetic perturbation）

### 2.5 细胞类型特异性胁迫与免疫响应

**规模** 6 条证据 / 5 篇文献；**构成** omics/co-occurrence(5)、descriptive/observational(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Solanum tuberosum；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Yibo et al., 2022 [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f5]]；2026 [[dpdf-10-1038-s41477025-02181-9-f1]]；2026 [[dpdf-10-1038-s41477025-02181-9-f4]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 6 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（Yibo et al., 2022 [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f5]]；2026 [[dpdf-10-1038-s41477025-02181-9-f1]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表达相关、表型关联在本组缺证据；在补齐这些设计前，目标实体 与“细胞类型特异性胁迫与免疫响应”的方向性关系应作为待检验命题（Yibo et al., 2022 [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f5]]；2026 [[dpdf-10-1038-s41477025-02181-9-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|
| Oryza sativa | 2 | 0 | 2 |
| Arabidopsis thaliana | 2 | 0 | 2 |
| Solanum tuberosum | 1 | 1 | 2 |
| Fragaria × ananassa | 1 | 0 | 1 |
| Triticum aestivum | 1 | 0 | 1 |

**代表断言（原文摘录，未改写）**

- “This study provides not only a global view of maize cell fate determination during root development but also insights into the immune regulatory networks in major cell types of mai…” — [[ref-pbi-14097-f1]]（`10.1111/pbi.14097`，omics/co-occurrence）
- “This is the first report to document the single-cell transcriptional landscape of the plant pathogenic invasion process; it provides new insights into the holistic dynamics of host…” — [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f5]]（`10.1093/hr/uhab055`，omics/co-occurrence）
- “Based on cell-type identification using marker genes, we found that the dominant pathways in 2M root were mainly associated with transporters and signaling molecules involved in en…” — [[salvia-tanshinone-sc-spatial-f2]]（`10.1111/nph.71285`，omics/co-occurrence）

### 2.6 细胞间通讯与信号推断

**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。

### 2.7 多组学整合与调控网络

**规模** 11 条证据 / 8 篇文献；**构成** omics/co-occurrence(7)、descriptive/observational(2)、DNA binding/regulation(2)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 9 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Zea mays，反复出现的实体为AHL23；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Yibo et al., 2022 [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f3]]；[[differential-accessibility-regulates-cell-type-expression]]；George et al., 2024 [[introducing-single-cell-stereo-sequencing-technology-to-transform-the-plant-tran-f5]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，9 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[differential-accessibility-regulates-cell-type-expression]]）。
- **可检验缺口**：遗传扰动、蛋白互作、表达相关、表型关联在本组缺证据；在补齐这些设计前，AHL23 与“多组学整合与调控网络”的方向性关系应作为待检验命题（Yibo et al., 2022 [[development-of-a-single-cell-atlas-for-woodland-strawberry-i-fragaria-vesca-i-f3]]；[[differential-accessibility-regulates-cell-type-expression]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | DNA 结合 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 0 | 5 | 2 | 7 |
| Arabidopsis thaliana | 0 | 2 | 2 | 4 |
| Zea mays | 0 | 3 | 0 | 3 |
| Solanum lycopersicum | 0 | 1 | 1 | 2 |
| Triticum aestivum | 0 | 2 | 0 | 2 |

**基因实体（自动标注，前 5）**：AHL23(1)（标注覆盖 1/11）。

**代表断言（原文摘录，未改写）**

- “Peanut tissue ontology regarding transcriptional dynamic illustrating has entered a single-cell era, such as by using scRNA-seq approaches in conjunction with high-throughput multi…” — [[ref-pbi-14306-f4]]（`10.1111/pbi.14306`，omics/co-occurrence）
- “Integrative analysis of snATAC-seq and scRNA-seq data demonstrates that cell-type-specific gene expression is significantly associated with differential chromatin accessibility at …” — [[differential-accessibility-regulates-cell-type-expression]]（`10.1016/j.molp.2021.01.001`，omics/co-occurrence）
- “Large-scale profiling of TF-binding sites using ampDAP-seq The transcriptomic identities of cell clusters are largely defined by their underlying gene regulatory networks (GRNs), i…” — [[ref-s41467-023-44369-7-f4]]（`10.1038/s41467-023-44369-7`，omics/co-occurrence）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| theanine | 2 | 2 | 图集构建与细胞类型注释、空间转录组与位置映射 |

### 3.1 跨子主题受控叙述

- **层级不均**：因果层证据在子主题间分布不均，最高为“图集构建与细胞类型注释”（3 条），最低为“空间转录组与位置映射”（0 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 图集构建与细胞类型注释 | — | 1 | 2 | 13 | 2 | 78 | 87 |
| 空间转录组与位置映射 | — | — | — | — | — | 15 | 1 |
| 发育轨迹与拟时序推断 | — | — | — | 2 | — | 8 | 9 |
| 技术平台与建库方法 | 1 | 1 | 1 | — | — | 15 | 1 |
| 细胞类型特异性胁迫与免疫响应 | — | — | — | — | — | 5 | 1 |
| 细胞间通讯与信号推断 | — | — | — | — | — | — | — |
| 多组学整合与调控网络 | — | — | 2 | — | — | 7 | 2 |

**零因果层子主题（3/7）**：空间转录组与位置映射、发育轨迹与拟时序推断、细胞类型特异性胁迫与免疫响应。

这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，属于超越证据的表达，须在方案中降级为待验证命题。

## 5. 可直接引用的因果级证据（自动筛选）

以下 8 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[b3-l7tWWswvI2rZ5ba_4V2BsQ-f5]] | `10.1002/advs.202512295` | protein interaction | For instance, the snRNA-seq data demonstrated that the epidermal cell gene Zm00001eb101750 ( ZmHSP90, Heat shock protein… |
| [[cr-annurev-arplant-0817-f4]] | `10.1146/annurev-arplant-081720-010120` | protein interaction | Multiplexing Using Lipid-Tagged Indices for single-cell and single-nucleus RNA-seq (MULTI-Seq) uses lipid-or cholesterol… |
| [[daily-42255287-f1]] | `10.3389/fpls.2026.1809797` | genetic perturbation | In summary, while current systems offer specific advantages, inherent limitations–namely, a reliance on transgenic overe… |
| [[daily-42288963-f2]] | `10.1093/plphys/kiag372` | protein interaction | Although SLIM1, RVE1, and RVE8 bind to the promoters of OAS cluster genes, only SLIM1 plays a role in their regulation b… |
| [[daily-42530009-f2]] | `10.1093/plphys/kiag560` | genetic perturbation | Using single-cell microfluidics, transcriptomics, and metabolomics, we show that Δ glgC mutants exhibit pronounced light… |
| [[ref-j-tplants-2019-10-008-f1]] | `10.1016/j.tplants.2019.10.008` | protein interaction | Once encapsulated in a droplet, cells are immediately lysed, releasing RNA that binds to primers on the bead surface whe… |
| [[root-cell-type-specific-chromatin-accessibility]] | `10.1016/j.molp.2021.01.001` | DNA binding/regulation | Single-cell ATAC-seq of Arabidopsis roots reveals that each major cell type exhibits a distinct genome-wide chromatin ac… |
| [[snATAC-seq-resolves-root-cell-types]] | `10.1016/j.molp.2021.01.001` | DNA binding/regulation | Single-nucleus ATAC-seq (snATAC-seq) of Arabidopsis roots resolves major cell types based on differential chromatin acce… |

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **因果级证据占比仅 2.9%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。
- **3 个子主题完全没有因果层证据**（空间转录组与位置映射、发育轨迹与拟时序推断、细胞类型特异性胁迫与免疫响应）：这些方向目前只能写相关性。
- **单篇证据物种 9 个**（Coffea spp.、未识别、Cucumis spp.、Crocus sativus、Helianthus annuus…）：跨物种外推缺乏支撑。
- **1 个子主题零证据**（细胞间通讯与信号推断）：需按子主题关键词补检索，否则主题综述会出现结构性空洞。
- **58 条证据（21%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261117`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 3689 个中文字符，行内证据链接 69 处，密度 **9.4 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
