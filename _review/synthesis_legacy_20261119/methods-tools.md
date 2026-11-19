---
title: "Synthesis: #Methods-Tools"
total_evidence: 1647
total_papers: 386
library_papers: 656  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-18
topics: ["#methods-tools"]


relevance_soybean: "低 — 间接关联"
auto_discovered: true
cluster_size: 1 tags
status: auto-generated
updated: 2026-11-19
legacy_archive: _review/synthesis_legacy_20261118/methods-tools.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 方法与工具 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 1647 | 本主题归属的证据对象数 |
| 独立论文 | 386 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.27 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 15% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(350)、Zea mays(239)、Triticum aestivum(225)、Arabidopsis thaliana(217)、Plant (unspecified)(202)、—(162) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1373；protein interaction 81；expression/regulation 70；phenotypic/association 51；omics/co-occurrence 40；genetic perturbation 22 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-41788331-f6` | 10.3389/fmicb.2026.1743670 | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect  |
| `ms-10-3389_fgeed-2026-1815812-f1` | 10.3389/fgeed.2026.1815812 | Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CR |
| `daily-43020961-f1` | 10.1007/s44297-026-00091-6 | Citrulli Resistance development cases in 2007 in Georgia and South Carolina [10, 63] Demet |
| `daily-42049231-f1` | 10.1093/nar/gkag380 | Donor DNA fragments are carried on circular plasmids containing an origin of transfer for  |
| `daily-41788331-f7` | 10.3389/fmicb.2026.1743670 | For antifungal resistance (AFR), new resources and models are arriving: curated datasets o |
| `daily-42328087-f4` | 10.3389/fpls.2026.1807632 | In contrast to RNAi-based approaches that result in partial and variable gene silencing, C |
| `daily-42280721-f1` | 10.3390/plants15111684 | Overexpression of PmSND4 significantly promoted the vegetative growth of transgenic poplar |
| `daily-42306252-f1` | 10.1093/aobpla/plag023 | We show how this approach can be used qualitatively and quantitatively to study cell shape |
| `daily-42110912-f6` | 10.3389/fgene.2026.1800699 | Similarly, RNA interference-mediated silencing of MsSGR in alfalfa produced stay-green tra |
| `daily-42281831-f5` | 10.1039/d6sc03368g | Therefore, we further selected Vpg (replication), Hc-pro (silencing suppression) and CP (a |
| `daily-42496959-f6` | 10.1007/s44307-026-00124-9 | Overexpression of DGAT1 from Vernonia, soybean or castor bean in Arabidopsis resulted in s |
| `daily-42427441-f1` | 10.21769/BioProtoc.5734 | Dual-gRNA CRISPR/Cas9 strategy provides an effective alternative by inducing two double-st |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 22 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 81 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 10 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 70 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 51 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 40 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1373 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-41788331-f6` | 10.3389/fmicb.2026.1743670 | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect tractable  |
| `ms-10-3389_fgeed-2026-1815812-f1` | 10.3389/fgeed.2026.1815812 | Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CRISPR/Cas9  |
| `daily-43020961-f1` | 10.1007/s44297-026-00091-6 | Citrulli Resistance development cases in 2007 in Georgia and South Carolina [10, 63] Demethylation i |
| `daily-42049231-f1` | 10.1093/nar/gkag380 | Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial  |
| `daily-41788331-f7` | 10.3389/fmicb.2026.1743670 | For antifungal resistance (AFR), new resources and models are arriving: curated datasets of resistan |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-18 由 `rebuild_synthesis_body.py` 从 **1647 条证据对象 / 386 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261118`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **1647 条证据 / 386 篇文献**。规则判定为因果或直接调控的 **113 条（6.9%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **27 条**。可判定程度最高的结论集中在OsFZP、PmSND4：Overexpression of either OsSAMS1 or OsFZP resulted in a significant reduction in panicle branch number compared to the wild-type.（[[daily-42260361-f1]]）；Overexpression of PmSND4 significantly promoted the vegetative growth of transgenic poplar, increased stem xylem cell wall thickness, and si…（[[daily-42280721-f1]]）；PmSND4 overexpression significantly promotes vegetative growth in poplar.（[[daily-42280721-f7]]）。研究重心位于“计算工具与数据整合”（93 条证据，占 6%）。证据的物种分布以 Oryza sativa 为首（350 条，21%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 1647 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 386 | 去重后的论文数 |
| 平均每篇证据数 | 4.27 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 15%（58/386） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(1373)、protein interaction(81)、expression/regulation(70)、phenotypic/association(51)、omics/co-occurrence(40)、genetic perturbation(22)、DNA binding/regulation(10) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(1423)、medium(193)、high(25)、未标(6) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(350)、Zea mays(239)、Triticum aestivum(225)、Arabidopsis thaliana(217)、Plant (unspecified)(202)、Glycine max(155) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1367（83%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **113 条**，占本主题证据的 **6.9%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 350 条证据（21%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 34 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 测序与文库构建

**规模** 30 条证据 / 22 篇文献；**构成** descriptive/observational(25)、omics/co-occurrence(3)、phenotypic/association(2)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Plant (unspecified)、Rosa spp.、Triticum aestivum，反复出现的实体为RTS11、scDblFinder；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41601394-f5]]；[[daily-41601394-f6]]；[[daily-42222011-f4]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 30 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-41601394-f5]]；[[daily-41601394-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表达相关在本组缺证据；在补齐这些设计前，RTS11、scDblFinder 与“测序与文库构建”的方向性关系应作为待检验命题（[[daily-41601394-f5]]；[[daily-41601394-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|
| Plant (unspecified) | 0 | 1 | 7 | 8 |
| Rosa spp. | 0 | 0 | 3 | 3 |
| Triticum aestivum | 0 | 0 | 3 | 3 |
| Oryza sativa | 0 | 0 | 3 | 3 |
| Malus domestica | 1 | 0 | 2 | 3 |

**基因实体（自动标注，前 5）**：RTS11(1)、scDblFinder(1)（标注覆盖 2/30）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-1038_s41598-026-67892-1-f5]]。

**代表断言（原文摘录，未改写）**

- “More recent genomic approaches, including target enrichment-based datasets [, ] and Genotyping-by-Sequencing (GBS) methods [ ], have expanded the number of nuclear loci dramaticall…” — [[daily-42436402-f1]]（`10.1186/s12870-026-09510-w`，descriptive/observational）
- “Investigating further, we found this was correlated with an increase in UMIs with two errors in which the single error intermediate was not observed, as detected by counting the nu…” — [[ref-gr-209601-116-f2]]（`10.1101/gr.209601.116`，phenotypic/association）
- “Regarding previous studies, apart from the draft human pangenome reference, we found the best genotype concordance with the most recent multiplatform analysis ( ), although ONT seq…” — [[daily-42680553-f4]]（`10.1101/gr.280867.125`，descriptive/observational）

### 2.2 成像与空间定位技术

**规模** 16 条证据 / 12 篇文献；**构成** descriptive/observational(12)、protein interaction(2)、omics/co-occurrence(1)、expression/regulation(1)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 14 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为TipTracker、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42241290-f2]]；[[daily-42280777-f1]]；[[daily-42293015-f2]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，14 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42241290-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联在本组缺证据；在补齐这些设计前，TipTracker、lignin 与“成像与空间定位技术”的方向性关系应作为待检验命题（[[daily-42241290-f2]]；[[daily-42280777-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Arabidopsis thaliana | 2 | 1 | 1 | 5 | 9 |
| Oryza sativa | 0 | 0 | 0 | 4 | 4 |
| Zea mays | 2 | 0 | 0 | 2 | 4 |
| Nicotiana tabacum | 0 | 0 | 1 | 1 | 2 |
| Triticum aestivum | 0 | 0 | 0 | 1 | 1 |

**基因实体（自动标注，前 5）**：TipTracker(3)（标注覆盖 3/16）。

**化合物实体（自动标注，前 5）**：lignin(1)（标注覆盖 1/16）。

**代表断言（原文摘录，未改写）**

- “TipTracker can interact with the graphical user interfaces of various commercial microscope software programs.” — [[sel-elife-26792-001-f1]]（`10.7554/eLife.26792.001`，protein interaction）
- “Opti mized acquisition and postprocessing techniques, including QSM, fast gray matter acquisition T1 inversion recovery (FGATIR), and advanced diffusion imaging of tracts such as t…” — [[ms-10-1007_s12311-026-02054-7-f5]]（`10.1007/s12311-026-02054-7`，descriptive/observational）
- “2, these results suggest that the main contribution of the present study lies not in proposing a fundamentally new universal architecture, but in building a task-oriented framework…” — [[daily-42323598-f4]]（`10.1186/s13007-026-01558-x`，descriptive/observational）

### 2.3 基因编辑与遗传转化

**规模** 45 条证据 / 27 篇文献；**构成** descriptive/observational(38)、genetic perturbation(5)、expression/regulation(1)、protein interaction(1)；**因果层** 6 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Arabidopsis thaliana，反复出现的实体为SpCas9、OsBBM1；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41788331-f6]]；[[daily-42049231-f1]]；[[daily-42231171-f1]]）。
- **证据层级的张力**：6 条属于遗传扰动/蛋白互作/DNA 结合，39 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42974074-f1]]）。
- **可检验缺口**：DNA 结合、表型关联、组学共现在本组缺证据；在补齐这些设计前，SpCas9、OsBBM1 与“基因编辑与遗传转化”的方向性关系应作为待检验命题（[[daily-41788331-f6]]；[[daily-42049231-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 2 | 1 | 0 | 17 | 20 |
| Zea mays | 1 | 1 | 0 | 12 | 14 |
| Arabidopsis thaliana | 3 | 1 | 1 | 5 | 10 |
| Plant (unspecified) | 0 | 0 | 0 | 6 | 6 |
| Sorghum bicolor | 0 | 0 | 0 | 5 | 5 |

**基因实体（自动标注，前 5）**：SpCas9(3)、OsBBM1(2)、OsGS3(1)、OsROC5(1)、CDA1(1)（标注覆盖 12/45）。

**标注一致性提示**：本组 18 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42231171-f1]]。

**代表断言（原文摘录，未改写）**

- “The most rapidly growing technology is a bacterial monomeric DNA endonuclease called CRISPR/Cas9 (Clustered Regularly Interspaced Short Palindromic Repeats-associated protein 9), w…” — [[ms-10-3389_fgeed-2026-1815812-f2]]（`10.3389/fgeed.2026.1815812`，protein interaction）
- “In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect tractable in native contexts: pooled editing and barcoded screening in Candida now resolve…” — [[daily-41788331-f6]]（`10.3389/fmicb.2026.1743670`，genetic perturbation）
- “Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial conjugation (oriT), a single guide-RNA expression cassette for Cas9 (sgRNA), sgR…” — [[daily-42049231-f1]]（`10.1093/nar/gkag380`，genetic perturbation）

### 2.4 计算工具与数据整合

**规模** 93 条证据 / 73 篇文献；**构成** descriptive/observational(74)、expression/regulation(7)、protein interaction(5)、omics/co-occurrence(4)、phenotypic/association(2)、genetic perturbation(1)；**因果层** 6 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Plant (unspecified)，反复出现的实体为AutoGluon、TipTracker；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41607079-f1]]；[[daily-41788331-f3]]；[[daily-42079774-f2]]）。
- **证据层级的张力**：6 条属于遗传扰动/蛋白互作/DNA 结合，87 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42079774-f2]]）。
- **可检验缺口**：DNA 结合在本组缺证据；在补齐这些设计前，AutoGluon、TipTracker 与“计算工具与数据整合”的方向性关系应作为待检验命题（[[daily-41607079-f1]]；[[daily-41788331-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 1 | 1 | 0 | 0 | 20 | 23 |
| Zea mays | 1 | 4 | 0 | 0 | 0 | 9 | 14 |
| Plant (unspecified) | 0 | 0 | 1 | 0 | 1 | 12 | 14 |
| Glycine max | 0 | 0 | 0 | 0 | 0 | 12 | 12 |
| Triticum aestivum | 0 | 0 | 0 | 0 | 0 | 12 | 12 |

**基因实体（自动标注，前 5）**：AutoGluon(2)、TipTracker(2)、ToMaToS(1)、LiDAR(1)、VirBinn(1)（标注覆盖 14/93）。

**代表断言（原文摘录，未改写）**

- “Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CRISPR/Cas9 editing in pigeonpea and expands the available genome-editing toolkit for this c…” — [[ms-10-3389_fgeed-2026-1815812-f1]]（`10.3389/fgeed.2026.1815812`，genetic perturbation）
- “Lobato (2019) contextualized Netflix’s recommendation infrastructure within the broader geography of digital distribution, showing how algorithmic systems interact with licensing r…” — [[ms-10-3389_fcomm-2026-1830832-f2]]（`10.3389/fcomm.2026.1830832`，protein interaction）
- “For each new system, the AutoIt scripts must be modified to correctly interact with the crucial control buttons of the software GUI, and we provide an illustration of this process …” — [[sel-elife-26792-001-f4]]（`10.7554/eLife.26792.001`，protein interaction）

### 2.5 单细胞与组学方法

**规模** 46 条证据 / 35 篇文献；**构成** descriptive/observational(31)、omics/co-occurrence(14)、genetic perturbation(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 45 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Plant (unspecified)、Triticum aestivum、Oryza sativa，反复出现的实体为MaxViT、BRI1、auxin、brassinosteroid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41788331-f6]]；[[daily-41905980-f3]]；[[daily-42218405-f2]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，45 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42218405-f2]]）。
- **可检验缺口**：DNA 结合、蛋白互作、表达相关、表型关联在本组缺证据；在补齐这些设计前，MaxViT、BRI1、auxin 与“单细胞与组学方法”的方向性关系应作为待检验命题（[[daily-41788331-f6]]；[[daily-41905980-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|
| Plant (unspecified) | 0 | 5 | 5 | 10 |
| Triticum aestivum | 1 | 2 | 5 | 8 |
| Oryza sativa | 0 | 1 | 6 | 7 |
| Arabidopsis thaliana | 0 | 3 | 3 | 6 |
| Malus domestica | 0 | 0 | 5 | 5 |

**基因实体（自动标注，前 5）**：MaxViT(1)、BRI1(1)、TIR1(1)、SlotDeconv(1)、scDblFinder(1)（标注覆盖 4/46）。

**化合物实体（自动标注，前 5）**：auxin(1)、brassinosteroid(1)（标注覆盖 1/46）。

**代表断言（原文摘录，未改写）**

- “MaxViT-Tiny (Transformer Branch): MaxViT (Multi-Axis Vision Transformer) utilizes a unique grid and block attention mechanism that allows the model to capture the global dependenci…” — [[daily-42230993-f6]]（`10.1038/s41598-026-56162-9`，descriptive/observational）
- “Finally, the workflow provides a uniquely versatile multidimensional detection toolkit, enabling researchers to seamlessly transition from global biochemical quantification to spec…” — [[daily-42241290-f2]]（`10.1016/j.xpro.2026.104619`，omics/co-occurrence）
- “The overall computation process can be expressed as follows: Here, x l denotes a pixel position on the “input feature map” x, k encoder represents the reassembly kernel, and N ( x …” — [[daily-42234768-f7]]（`10.1371/journal.pone.0349237`，descriptive/observational）

### 2.6 表型组与高通量筛选

**规模** 57 条证据 / 36 篇文献；**构成** descriptive/observational(48)、omics/co-occurrence(3)、expression/regulation(2)、protein interaction(2)、genetic perturbation(1)、phenotypic/association(1)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Triticum aestivum、Zea mays、Oryza sativa，反复出现的实体为MsDG1、FunTFBS；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41788331-f5]]；[[daily-41788331-f6]]；[[daily-42249571-f1]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，54 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42249571-f1]]）。
- **可检验缺口**：DNA 结合在本组缺证据；在补齐这些设计前，MsDG1、FunTFBS 与“表型组与高通量筛选”的方向性关系应作为待检验命题（[[daily-41788331-f5]]；[[daily-41788331-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Triticum aestivum | 1 | 2 | 1 | 1 | 1 | 14 | 20 |
| Zea mays | 0 | 0 | 0 | 1 | 1 | 15 | 17 |
| Oryza sativa | 0 | 0 | 0 | 1 | 0 | 12 | 13 |
| Glycine max | 0 | 0 | 0 | 0 | 0 | 10 | 10 |
| Plant (unspecified) | 0 | 0 | 0 | 0 | 2 | 5 | 7 |

**基因实体（自动标注，前 5）**：MsDG1(1)、FunTFBS(1)、scDblFinder(1)（标注覆盖 3/57）。

**代表断言（原文摘录，未改写）**

- “A measure of when anthesis occurs in days after sowing does not provide a stable phenotype because different genotypes respond to temperature and photoperiod (Pp) in different ways…” — [[daily-42249571-f2]]（`10.1093/jxb/erag278`，protein interaction）
- “Yida Chen [ ] was among the first to apply deep learning to outdoor soil image segmentation, achieving high-accuracy and real-time segmentation using Mask R-CNN and laying a founda…” — [[daily-42280777-f7]]（`10.3390/plants15111740`，descriptive/observational）
- “We do not attempt a comprehensive review of a broad and often diffuse literature, but rather highlight promising breeding targets based on the magnitude of potential benefits given…” — [[ref-s11104-023-06301-2-f4]]（`10.1007/s11104-023-06301-2`，phenotypic/association）

### 2.7 数据库与知识资源

**规模** 31 条证据 / 27 篇文献；**构成** descriptive/observational(25)、omics/co-occurrence(3)、genetic perturbation(1)、expression/regulation(1)、DNA binding/regulation(1)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 29 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Arabidopsis thaliana，反复出现的实体为FungAMR、ResFungi；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41788331-f5]]；[[daily-41788331-f7]]；[[daily-42225647-f1]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，29 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42661863-f5]]）。
- **可检验缺口**：蛋白互作、表型关联在本组缺证据；在补齐这些设计前，FungAMR、ResFungi 与“数据库与知识资源”的方向性关系应作为待检验命题（[[daily-41788331-f5]]；[[daily-41788331-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Oryza sativa | 0 | 0 | 0 | 1 | 6 | 7 |
| Triticum aestivum | 1 | 1 | 1 | 0 | 3 | 6 |
| Arabidopsis thaliana | 0 | 1 | 0 | 1 | 3 | 5 |
| Glycine max | 0 | 0 | 0 | 0 | 4 | 4 |
| Plant (unspecified) | 0 | 0 | 0 | 1 | 3 | 4 |

**基因实体（自动标注，前 5）**：FungAMR(1)、ResFungi(1)、ChEMBL(1)、PhosPhAt(1)、scDblFinder(1)（标注覆盖 4/31）。

**代表断言（原文摘录，未改写）**

- “For antifungal resistance (AFR), new resources and models are arriving: curated datasets of resistance mutations (FungAMR, ResFungi) and ML methods to predict AFR biomarkers and ta…” — [[daily-41788331-f7]]（`10.3389/fmicb.2026.1743670`，genetic perturbation）
- “Comparing DAP-seq-derived motifs to curated motif databases (Transfac, JASPAR, and AGRIS), we found most DAP-seq motifs were highly similar to published data (Table S1C).” — [[ref-j-cell-2016-04-038-f2]]（`10.1016/j.cell.2016.04.038`，DNA binding/regulation）
- “The core idea — that each organism thrives within a specific niche defined by multiple environmental dimensions — maps onto the educational setting where each learner occupies a co…” — [[ms-10-1038_s41598-026-56933-4-f2]]（`10.1038/s41598-026-56933-4`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| scDblFinder | 4 | 4 | 单细胞与组学方法、数据库与知识资源、测序与文库构建、表型组与高通量筛选 |
| TipTracker | 2 | 5 | 成像与空间定位技术、计算工具与数据整合 |
| SpCas9 | 2 | 4 | 基因编辑与遗传转化、计算工具与数据整合 |
| FunTFBS | 2 | 2 | 表型组与高通量筛选、计算工具与数据整合 |
| MsDG1 | 2 | 2 | 基因编辑与遗传转化、表型组与高通量筛选 |
| RTS11 | 2 | 2 | 基因编辑与遗传转化、测序与文库构建 |

### 3.1 跨子主题受控叙述

- **交叉实体**：scDblFinder、TipTracker、SpCas9、FunTFBS、MsDG1 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（Thomas et al., 2023 [[charting-plant-gene-functions-in-the-multi-omics-and-single-cell-era-f2]]；Thomas et al., 2023 [[charting-plant-gene-functions-in-the-multi-omics-and-single-cell-era-f3]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“基因编辑与遗传转化”（6 条），最低为“测序与文库构建”（0 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 测序与文库构建 | — | — | — | — | 2 | 3 | 25 |
| 成像与空间定位技术 | — | 2 | — | 1 | — | 1 | 12 |
| 基因编辑与遗传转化 | 5 | 1 | — | 1 | — | — | 38 |
| 计算工具与数据整合 | 1 | 5 | — | 7 | 2 | 4 | 74 |
| 单细胞与组学方法 | 1 | — | — | — | — | 14 | 31 |
| 表型组与高通量筛选 | 1 | 2 | — | 2 | 1 | 3 | 48 |
| 数据库与知识资源 | 1 | — | 1 | 1 | — | 3 | 25 |

**零因果层子主题（1/7）**：测序与文库构建。

这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，属于超越证据的表达，须在方案中降级为待验证命题。

## 5. 可直接引用的因果级证据（自动筛选）

以下 113 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[charting-plant-gene-functions-in-the-multi-omics-and-single-cell-era-f4]] | `10.1016/j.tplants.2022.09.008` | DNA binding/regulation | They identified direct regulatory targets of MYC2, a JA-response master regulator, alongside its genetic interaction par… |
| [[charting-plant-gene-functions-in-the-multi-omics-and-single-cell-era-f5]] | `10.1016/j.tplants.2022.09.008` | protein interaction | For example, using an in vitro kinase assay and transient expression in Nicotiana benthamiana, a predicted kinase signal… |
| [[daily-41788331-f2]] | `10.3389/fmicb.2026.1743670` | protein interaction | Field studies show that drought legacies interact with wildfires to restructure microbial communities, often reducing fu… |
| [[daily-41788331-f6]] | `10.3389/fmicb.2026.1743670` | genetic perturbation | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect tractable in native contexts: … |
| [[daily-41788331-f7]] | `10.3389/fmicb.2026.1743670` | genetic perturbation | For antifungal resistance (AFR), new resources and models are arriving: curated datasets of resistance mutations (FungAM… |
| [[daily-41905980-f2]] | `10.1038/s41598-026-44501-9` | protein interaction | SEC3A directly embeds into the plasma membrane via its N-terminal transmembrane domain, whereas EXO70 subunits (e.g., EX… |
| [[daily-42049231-f1]] | `10.1093/nar/gkag380` | genetic perturbation | Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial conjugation (oriT), … |
| [[daily-42110912-f6]] | `10.3389/fgene.2026.1800699` | genetic perturbation | Similarly, RNA interference-mediated silencing of MsSGR in alfalfa produced stay-green transgenic lines with enhanced ch… |
| [[daily-42110912-f7]] | `10.3389/fgene.2026.1800699` | protein interaction | These effectors interact with host proteins and trigger immune responses, cell death and hormonal signaling changes (;; … |
| [[daily-42126179-f1]] | `10.1080/15592324.2026.2672221` | DNA binding/regulation | Redox status directly regulates the activity of key metabolic enzymes and transcription factors, thereby linking metabol… |
| [[daily-42228902-f1]] | `10.2196/88125` | protein interaction | First, they wanted TAMI to be able to smoothly interact with them by picking up social cues (eg, using and responding to… |
| [[daily-42231177-f2]] | `10.1186/s12870-026-09155-9` | genetic perturbation | A positive correlation was observed between Cry1Ac protein level and the reduction in leaf consumption among the transge… |
| [[daily-42237187-f1]] | `10.1186/s13007-026-01548-z` | protein interaction | Plant biological rhythms operate beyond diurnal scales; in perennials, circadian rhythms interact with and are modulated… |
| [[daily-42241290-f7]] | `10.1016/j.xpro.2026.104619` | protein interaction | Milk contains high levels of endogenous biotin and biotinylated proteins that strongly interact with Streptavidin-HRP. |
| [[daily-42243690-f4]] | `10.1186/s12870-026-09148-8` | protein interaction | The phylogenetic patterns observed in PQS frequency raise the question of what biological machinery might interact with … |
| [[daily-42243690-f5]] | `10.1186/s12870-026-09148-8` | protein interaction | G4 structures in cpDNA could therefore interact with both plastid-encoded and nuclear-encoded components. |
| [[daily-42243690-f6]] | `10.1186/s12870-026-09148-8` | protein interaction | Whether PPR proteins or other imported RNA-binding factors interact with G4 motifs in cpDNA remains to be directly demon… |
| [[daily-42249571-f2]] | `10.1093/jxb/erag278` | protein interaction | A measure of when anthesis occurs in days after sowing does not provide a stable phenotype because different genotypes r… |
| [[daily-42249571-f4]] | `10.1093/jxb/erag278` | protein interaction | In short, the phenotyping scheme and CAMP model provide a valid framework for quantifying genotypic differences and esti… |
| [[daily-42251534-f5]] | `10.1111/tpj.70952` | protein interaction | Here we show the reproducible detection of TSP9 bound to PetD of the cytochrome b 6 f complex. |

（另有 93 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **因果级证据占比仅 6.9%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。
- **1 个子主题完全没有因果层证据**（测序与文库构建）：这些方向目前只能写相关性。
- **1367 条证据（83%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261118`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4060 个中文字符，行内证据链接 91 处，密度 **11.2 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
