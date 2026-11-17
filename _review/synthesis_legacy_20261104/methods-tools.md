---
title: "Synthesis: #Methods-Tools"
total_evidence: 1882
total_papers: 401
library_papers: 656  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
topics: ["#methods-tools"]


relevance_soybean: "低 — 间接关联"
auto_discovered: true
cluster_size: 1 tags
status: auto-generated
updated: 2026-11-04
legacy_archive: _review/synthesis_legacy_20261103/methods-tools.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 方法与工具 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 1882 | 本主题归属的证据对象数 |
| 独立论文 | 401 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.69 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 11% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(408)、Zea mays(275)、Triticum aestivum(261)、Arabidopsis thaliana(243)、Plant (unspecified)(227)、Ficus carica(192) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1491；expression/regulation 176；protein interaction 84；phenotypic/association 58；omics/co-occurrence 43；genetic perturbation 20 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42720300-f1` | 10.1111/pbi.70752 | Specifically, we introduced mutations in three target genes MsALS1, MsALS2 and MsACC1 to c |
| `daily-41788331-f6` | 10.3389/fmicb.2026.1743670 | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect  |
| `ms-10-3389_fgeed-2026-1815812-f1` | 10.3389/fgeed.2026.1815812 | Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CR |
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
| genetic perturbation | 20 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 84 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 10 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 176 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 58 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 43 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1491 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42720300-f1` | 10.1111/pbi.70752 | Specifically, we introduced mutations in three target genes MsALS1, MsALS2 and MsACC1 to confer herb |
| `daily-41788331-f6` | 10.3389/fmicb.2026.1743670 | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect tractable  |
| `ms-10-3389_fgeed-2026-1815812-f1` | 10.3389/fgeed.2026.1815812 | Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CRISPR/Cas9  |
| `daily-42049231-f1` | 10.1093/nar/gkag380 | Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial  |
| `daily-41788331-f7` | 10.3389/fmicb.2026.1743670 | For antifungal resistance (AFR), new resources and models are arriving: curated datasets of resistan |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **1540 条证据对象 / 338 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **1540 条证据 / 338 篇文献**。规则判定为因果或直接调控的 **98 条（6.4%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **14 条**。可判定程度最高的结论集中在WB02、SlPMR4、SlMAPK3：Compared to the parental strain WB02, all strains overexpressing the tested tolerance-related genes, particularly Pdr5, exhibited improved c…（[[ms-10-1016_j-synbio-2026-03-017-f6]]）；Late Blight For late blight, CRISPR knockout of SlPMR4 reduced susceptibility [45], while simultaneous CRISPR/Cas9 editing of miR482b and mi…（[[ms-10-20900_cbgg20260021-f7]]）；Knockout of SlMAPK3 resulted in enhanced drought sensitivity, confirming its role in coordinating ROS detoxification and stress-induced tran…（[[ms-10-20900_cbgg20260021-f8]]）。研究重心位于“计算工具与数据整合”（82 条证据，占 5%）。证据的物种分布以 Oryza sativa 为首（445 条，29%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 1540 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 338 | 去重后的论文数 |
| 平均每篇证据数 | 4.56 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 17%（58/338） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(1224)、expression/regulation(145)、protein interaction(74)、omics/co-occurrence(52)、phenotypic/association(21)、genetic perturbation(15)、DNA binding/regulation(9) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(1345)、medium(174)、high(21) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(445)、Zea mays(365)、Arabidopsis thaliana(280)、Triticum aestivum(254)、Solanum lycopersicum(216)、Glycine max(178) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1259（82%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **98 条**，占本主题证据的 **6.4%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 445 条证据（29%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 25 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 测序与文库构建

**规模** 32 条证据 / 22 篇文献；**构成** descriptive/observational(24)、omics/co-occurrence(4)、phenotypic/association(2)、DNA binding/regulation(1)、protein interaction(1)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 30 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Plant (unspecified)、Citrus spp.、Oryza sativa，反复出现的实体为ChIP、MuA3；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41601394-f5]]；[[daily-41601394-f6]]；[[daily-42079774-f5]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，30 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[ms-10-1038_s41525-026-00617-5-f1]]）。
- **可检验缺口**：遗传扰动、表达相关在本组缺证据；在补齐这些设计前，ChIP、MuA3 与“测序与文库构建”的方向性关系应作为待检验命题（[[daily-41601394-f5]]；[[daily-41601394-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Plant (unspecified) | 1 | 1 | 0 | 1 | 8 | 11 |
| Citrus spp. | 0 | 0 | 1 | 1 | 4 | 6 |
| Oryza sativa | 0 | 0 | 0 | 0 | 5 | 5 |
| Arabidopsis thaliana | 0 | 0 | 0 | 0 | 4 | 4 |
| Ficus carica | 0 | 0 | 1 | 2 | 1 | 4 |

**基因实体（自动标注，前 5）**：ChIP(1)、MuA3(1)、InDel(1)、scDblFinder(1)（标注覆盖 4/32）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-3389_fmicb-2026-1843102-f4]]。

**代表断言（原文摘录，未改写）**

- “Very few of the potential target sites are utilized in cells7, however, and the actual number of bound sites, as measured by chromatin immunoprecipitation sequencing followed by se…” — [[ms-10-1038_s41592-026-03177-9-f3]]（`10.1038/s41592-026-03177-9`，DNA binding/regulation）
- “This alternative primer (MuA3'F) was designed to bind to the MuA recognition sequence inserted into the DNA by the transposase in the fragmentation step (Figure 1B) (Oxford Nanopor…” — [[ms-10-1038_s41598-026-55253-x-f7]]（`10.1038/s41598-026-55253-x`，protein interaction）
- “Investigating further, we found this was correlated with an increase in UMIs with two errors in which the single error intermediate was not observed, as detected by counting the nu…” — [[ref-gr-209601-116-f2]]（`10.1101/gr.209601.116`，phenotypic/association）

### 2.2 成像与空间定位技术

**规模** 22 条证据 / 15 篇文献；**构成** descriptive/observational(16)、omics/co-occurrence(2)、expression/regulation(2)、protein interaction(2)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 20 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为TipTracker、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42241290-f2]]；[[daily-42306252-f3]]；[[daily-42306421-f3]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，20 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42241290-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联在本组缺证据；在补齐这些设计前，TipTracker、lignin 与“成像与空间定位技术”的方向性关系应作为待检验命题（[[daily-42241290-f2]]；[[daily-42306252-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Arabidopsis thaliana | 2 | 1 | 1 | 7 | 11 |
| Oryza sativa | 0 | 0 | 0 | 7 | 7 |
| Zea mays | 2 | 0 | 0 | 5 | 7 |
| Ficus carica | 0 | 0 | 0 | 4 | 4 |
| Nicotiana tabacum | 0 | 0 | 1 | 1 | 2 |

**基因实体（自动标注，前 5）**：TipTracker(3)（标注覆盖 3/22）。

**化合物实体（自动标注，前 5）**：lignin(1)（标注覆盖 1/22）。

**代表断言（原文摘录，未改写）**

- “TipTracker can interact with the graphical user interfaces of various commercial microscope software programs.” — [[sel-elife-26792-001-f1]]（`10.7554/eLife.26792.001`，protein interaction）
- “Opti mized acquisition and postprocessing techniques, including QSM, fast gray matter acquisition T1 inversion recovery (FGATIR), and advanced diffusion imaging of tracts such as t…” — [[ms-10-1007_s12311-026-02054-7-f5]]（`10.1007/s12311-026-02054-7`，descriptive/observational）
- “Finally, the workflow provides a uniquely versatile multidimensional detection toolkit, enabling researchers to seamlessly transition from global biochemical quantification to spec…” — [[daily-42241290-f2]]（`10.1016/j.xpro.2026.104619`，omics/co-occurrence）

### 2.3 基因编辑与遗传转化

**规模** 57 条证据 / 29 篇文献；**构成** descriptive/observational(45)、genetic perturbation(9)、protein interaction(2)、expression/regulation(1)；**因果层** 11 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Arabidopsis thaliana，反复出现的实体为OsBBM1、OsGS3；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42049231-f1]]；[[daily-42231171-f1]]；[[daily-42234790-f3]]）。
- **证据层级的张力**：11 条属于遗传扰动/蛋白互作/DNA 结合，46 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[ms-10-20900_cbgg20260021-f7]]；[[ms-10-1007_s11240-026-03486-z-f2]]）。
- **可检验缺口**：DNA 结合、表型关联、组学共现在本组缺证据；在补齐这些设计前，OsBBM1、OsGS3 与“基因编辑与遗传转化”的方向性关系应作为待检验命题（[[daily-42049231-f1]]；[[daily-42231171-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Oryza sativa | 3 | 1 | 0 | 27 | 31 |
| Zea mays | 2 | 1 | 0 | 19 | 22 |
| Arabidopsis thaliana | 3 | 1 | 1 | 11 | 16 |
| Solanum lycopersicum | 5 | 0 | 0 | 8 | 13 |
| Glycine max | 0 | 0 | 1 | 7 | 8 |

**基因实体（自动标注，前 5）**：OsBBM1(2)、OsGS3(1)、OsROC5(1)、CDA1(1)、SpRY(1)（标注覆盖 12/57）。

**标注一致性提示**：本组 26 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42231171-f1]]。

**代表断言（原文摘录，未改写）**

- “The most rapidly growing technology is a bacterial monomeric DNA endonuclease called CRISPR/Cas9 (Clustered Regularly Interspaced Short Palindromic Repeats-associated protein 9), w…” — [[ms-10-3389_fgeed-2026-1815812-f2]]（`10.3389/fgeed.2026.1815812`，protein interaction）
- “Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial conjugation (oriT), a single guide-RNA expression cassette for Cas9 (sgRNA), sgR…” — [[daily-42049231-f1]]（`10.1093/nar/gkag380`，genetic perturbation）
- “Collectively, CRISPR-based technologies are advancing an integrated and mechanism-driven framework, linking perturbation data with transcriptomic, metabolomic, and epigenomic datas…” — [[ms-10-20900_cbgg20260021-f1]]（`10.20900/cbgg20260021`，genetic perturbation）

### 2.4 计算工具与数据整合

**规模** 82 条证据 / 62 篇文献；**构成** descriptive/observational(61)、expression/regulation(9)、protein interaction(6)、omics/co-occurrence(3)、phenotypic/association(2)、genetic perturbation(1)；**因果层** 7 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Ficus carica，反复出现的实体为AutoGluon、TipTracker；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42079774-f2]]；[[daily-42221886-f1]]；[[daily-42221886-f6]]）。
- **证据层级的张力**：7 条属于遗传扰动/蛋白互作/DNA 结合，75 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42079774-f2]]）。
- **可检验缺口**：DNA 结合在本组缺证据；在补齐这些设计前，AutoGluon、TipTracker 与“计算工具与数据整合”的方向性关系应作为待检验命题（[[daily-42079774-f2]]；[[daily-42221886-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 1 | 1 | 0 | 1 | 22 | 26 |
| Zea mays | 1 | 4 | 1 | 0 | 0 | 14 | 20 |
| Ficus carica | 0 | 1 | 5 | 0 | 0 | 12 | 18 |
| Arabidopsis thaliana | 1 | 3 | 1 | 0 | 2 | 9 | 16 |
| Triticum aestivum | 0 | 0 | 1 | 0 | 0 | 12 | 13 |

**基因实体（自动标注，前 5）**：AutoGluon(2)、TipTracker(2)、ToMaToS(1)、VirBinn(1)、CatBoost(1)（标注覆盖 12/82）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-30574_wjarr-2026-31-1-1883-f1]]。

**代表断言（原文摘录，未改写）**

- “Collectively, this study demonstrates the feasibility of marker-free biolistic-mediated CRISPR/Cas9 editing in pigeonpea and expands the available genome-editing toolkit for this c…” — [[ms-10-3389_fgeed-2026-1815812-f1]]（`10.3389/fgeed.2026.1815812`，genetic perturbation）
- “The fitted model indicates that this overhead interacts with tool count ( ̂βO%×T = −0.033, P = 0.211), a directional pattern that is not retained under cluster-robust inference in …” — [[ms-10-1038_s42256-026-01268-y-f5]]（`10.1038/s42256-026-01268-y`，protein interaction）
- “Lobato (2019) contextualized Netflix’s recommendation infrastructure within the broader geography of digital distribution, showing how algorithmic systems interact with licensing r…” — [[ms-10-3389_fcomm-2026-1830832-f2]]（`10.3389/fcomm.2026.1830832`，protein interaction）

### 2.5 单细胞与组学方法

**规模** 38 条证据 / 28 篇文献；**构成** descriptive/observational(19)、omics/co-occurrence(18)、expression/regulation(1)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Triticum aestivum，反复出现的实体为scDblFinder；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42038471-f1]]；[[daily-42038471-f2]]；[[daily-42038471-f3]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 38 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42038471-f1]]；[[daily-42038471-f2]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作、表型关联在本组缺证据；在补齐这些设计前，scDblFinder 与“单细胞与组学方法”的方向性关系应作为待检验命题（[[daily-42038471-f1]]；[[daily-42038471-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|
| Oryza sativa | 1 | 8 | 4 | 13 |
| Arabidopsis thaliana | 1 | 5 | 5 | 11 |
| Triticum aestivum | 0 | 5 | 5 | 10 |
| Zea mays | 1 | 4 | 3 | 8 |
| Glycine max | 0 | 3 | 2 | 5 |

**基因实体（自动标注，前 5）**：scDblFinder(1)（标注覆盖 1/38）。

**代表断言（原文摘录，未改写）**

- “Haar wavelet transform can explicitly separate features of different frequencies, ensuring that the model accurately anchors the canopy baseline and captures local spectralspatial …” — [[daily-42293002-f4]]（`10.3389/fpls.2026.1838598`，descriptive/observational）
- “The problem of PCR duplicates is more acute when greater numbers of PCR cycles are required to increase the library concentration, as in single-cell RNA-seq, or when the alignment …” — [[ref-gr-209601-116-f4]]（`10.1101/gr.209601.116`，omics/co-occurrence）
- “Particular emphasis is placed on artificial intelligence (AI)-assisted approaches that integrate genomic, epigenomic, chromatin-accessibility, and multi-omics datasets to improve t…” — [[daily-42452277-f6]]（`10.3390/plants15132080`，omics/co-occurrence）

### 2.6 表型组与高通量筛选

**规模** 42 条证据 / 32 篇文献；**构成** descriptive/observational(33)、expression/regulation(3)、omics/co-occurrence(3)、phenotypic/association(3)；**因果层** 0 条（仅关联/描述，不得写因果）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Zea mays、Oryza sativa、Triticum aestivum，反复出现的实体为MsDG1、InDel；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42218724-f4]]；[[daily-42255293-f1]]；[[daily-42255293-f4]]）。
- **证据层级的张力**：本组 0 条因果级证据，全部 42 条为表达、组学或描述性；任何“调控/导致”表述都必须降级为待检验命题（[[daily-42218724-f4]]；[[daily-42255293-f1]]）。
- **可检验缺口**：遗传扰动、DNA 结合、蛋白互作在本组缺证据；在补齐这些设计前，MsDG1、InDel 与“表型组与高通量筛选”的方向性关系应作为待检验命题（[[daily-42218724-f4]]；[[daily-42255293-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Zea mays | 1 | 2 | 1 | 14 | 18 |
| Oryza sativa | 1 | 1 | 0 | 14 | 16 |
| Triticum aestivum | 0 | 2 | 1 | 12 | 15 |
| Glycine max | 1 | 0 | 0 | 11 | 12 |
| Solanum lycopersicum | 1 | 0 | 0 | 6 | 7 |

**基因实体（自动标注，前 5）**：MsDG1(1)、InDel(1)、FunTFBS(1)、scDblFinder(1)（标注覆盖 4/42）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-3389_fpls-2026-1852363-f6]]。

**代表断言（原文摘录，未改写）**

- “By integrating multivariate statistical analysis, diﬀerential metabolites screening, chemical classiﬁcation, and KEGG pathway enrichment analysis, we aimed to characterize stage-de…” — [[ms-10-3389_fmicb-2026-1921106-f2]]（`10.3389/fmicb.2026.1921106`，descriptive/observational）
- “We do not attempt a comprehensive review of a broad and often diffuse literature, but rather highlight promising breeding targets based on the magnitude of potential benefits given…” — [[ref-s11104-023-06301-2-f4]]（`10.1007/s11104-023-06301-2`，phenotypic/association）
- “This shows that only a small number of manually screened high-quality pseudo-masks (without any pixel-level annotation) can significantly enhance model generalization in the target…” — [[daily-42662556-f4]]（`10.1016/j.plaphe.2026.100267`，descriptive/observational）

### 2.7 数据库与知识资源

**规模** 38 条证据 / 32 篇文献；**构成** descriptive/observational(27)、expression/regulation(5)、omics/co-occurrence(4)、phenotypic/association(1)、DNA binding/regulation(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 37 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Triticum aestivum、Oryza sativa、Arabidopsis thaliana，反复出现的实体为GenBank、StDND2；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42110912-f3]]；[[daily-42238888-f2]]；[[daily-42247588-f5]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，37 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42238888-f2]]）。
- **可检验缺口**：遗传扰动、蛋白互作在本组缺证据；在补齐这些设计前，GenBank、StDND2 与“数据库与知识资源”的方向性关系应作为待检验命题（[[daily-42110912-f3]]；[[daily-42238888-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Triticum aestivum | 1 | 3 | 0 | 0 | 6 | 10 |
| Oryza sativa | 0 | 1 | 0 | 2 | 7 | 10 |
| Arabidopsis thaliana | 1 | 2 | 0 | 2 | 3 | 8 |
| Glycine max | 0 | 1 | 0 | 0 | 6 | 7 |
| Zea mays | 1 | 0 | 0 | 0 | 6 | 7 |

**基因实体（自动标注，前 5）**：GenBank(1)、StDND2(1)、TarBase(1)、GeneCards(1)、MS2(1)（标注覆盖 7/38）。

**代表断言（原文摘录，未改写）**

- “Comparing DAP-seq-derived motifs to curated motif databases (Transfac, JASPAR, and AGRIS), we found most DAP-seq motifs were highly similar to published data (Table S1C).” — [[ref-j-cell-2016-04-038-f2]]（`10.1016/j.cell.2016.04.038`，DNA binding/regulation）
- “Compared with previous studies focused on global diversity panels or historical germplasm collections (Wang et al., 2020; Li et al., 2022), our study specifically targets contempor…” — [[daily-42500473-f5]]（`10.3389/fpls.2026.1872682`，descriptive/observational）
- “The core idea — that each organism thrives within a specific niche defined by multiple environmental dimensions — maps onto the educational setting where each learner occupies a co…” — [[ms-10-1038_s41598-026-56933-4-f2]]（`10.1038/s41598-026-56933-4`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| scDblFinder | 4 | 4 | 单细胞与组学方法、数据库与知识资源、测序与文库构建、表型组与高通量筛选 |
| TipTracker | 2 | 5 | 成像与空间定位技术、计算工具与数据整合 |
| FunTFBS | 2 | 2 | 表型组与高通量筛选、计算工具与数据整合 |
| InDel | 2 | 2 | 测序与文库构建、表型组与高通量筛选 |
| MsDG1 | 2 | 2 | 基因编辑与遗传转化、表型组与高通量筛选 |

### 3.1 跨子主题受控叙述

- **交叉实体**：scDblFinder、TipTracker、FunTFBS、InDel、MsDG1 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[cr-omi-2011-0118-f1]]；[[cr-omi-2011-0118-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“基因编辑与遗传转化”（11 条），最低为“单细胞与组学方法”（0 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 测序与文库构建 | — | 1 | 1 | — | 2 | 4 | 24 |
| 成像与空间定位技术 | — | 2 | — | 2 | — | 2 | 16 |
| 基因编辑与遗传转化 | 9 | 2 | — | 1 | — | — | 45 |
| 计算工具与数据整合 | 1 | 6 | — | 9 | 2 | 3 | 61 |
| 单细胞与组学方法 | — | — | — | 1 | — | 18 | 19 |
| 表型组与高通量筛选 | — | — | — | 3 | 3 | 3 | 33 |
| 数据库与知识资源 | — | — | 1 | 5 | 1 | 4 | 27 |

**零因果层子主题（2/7）**：单细胞与组学方法、表型组与高通量筛选。

这些子主题目前只能产出相关性假说；若研究方案把它们写成“X 调控 Y”，属于超越证据的表达，须在方案中降级为待验证命题。

## 5. 可直接引用的因果级证据（自动筛选）

以下 98 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[daily-42049231-f1]] | `10.1093/nar/gkag380` | genetic perturbation | Donor DNA fragments are carried on circular plasmids containing an origin of transfer for bacterial conjugation (oriT), … |
| [[daily-42110912-f6]] | `10.3389/fgene.2026.1800699` | genetic perturbation | Similarly, RNA interference-mediated silencing of MsSGR in alfalfa produced stay-green transgenic lines with enhanced ch… |
| [[daily-42110912-f7]] | `10.3389/fgene.2026.1800699` | protein interaction | These effectors interact with host proteins and trigger immune responses, cell death and hormonal signaling changes (;; … |
| [[daily-42197561-f3]] | `10.3390/plants15101424` | DNA binding/regulation | Such hierarchical regulation (WRKY33 and MYB51) directly regulates the dynamics of camalexin and related indolic pathway… |
| [[daily-42197561-f5]] | `10.3390/plants15101424` | protein interaction | The most beneficial future models for plant immunity will likely be those that predict when and where specific metabolic… |
| [[daily-42222136-f1]] | `10.3389/frmbi.2026.1803341` | protein interaction | In conventional flow-through, free stall-designed facilities, cattle are not restricted to a single stall and have the o… |
| [[daily-42241290-f7]] | `10.1016/j.xpro.2026.104619` | protein interaction | Milk contains high levels of endogenous biotin and biotinylated proteins that strongly interact with Streptavidin-HRP. |
| [[daily-42255304-f1]] | `10.3389/fpls.2026.1848562` | protein interaction | In compatible (nonself) pollination, individual SLF proteins recognize and interact with non-self S-RNases, assembling f… |
| [[daily-42255304-f3]] | `10.3389/fpls.2026.1848562` | protein interaction | Functional studies confirm that HT-B directly interacts with S-RNases in stylar transmitting tissues, regulating their a… |
| [[daily-42262665-f3]] | `10.1007/s44297-026-00078-3` | protein interaction | This iron plaque interacts with root-exuded organic carbon to form stable Fe-organic complexes, which effectively protec… |
| [[daily-42281572-f1]] | `10.1093/nsr/nwag095` | protein interaction | Together, these findings suggest that ZmRR2 may interact with ZmEhd1 to form an inactive complex that suppresses the tra… |
| [[daily-42281572-f5]] | `10.1093/nsr/nwag095` | protein interaction | [ ] showed that ZmRR1 interacts with ZmEhd1 to repress its activity, thereby reducing the expression of downstream flori… |
| [[daily-42285939-f2]] | `10.1038/s41467-026-73922-3` | protein interaction | Overall, these findings demonstrate that Zn2+ effectively interacts with carboxyl groups, altering the intrinsic gelatio… |
| [[daily-42292990-f5]] | `10.3389/fpls.2026.1824871` | protein interaction | In plants, gibberellins bind to the GID1 receptor, promoting degradation of DELLA proteins, which are negative regulator… |
| [[daily-42292990-f7]] | `10.3389/fpls.2026.1824871` | protein interaction | The CBL1–CIPK23 complex phosphorylates AKT1, thereby enhancing K+ uptake during salt stress (Chen et al., 2007; 2024; Ya… |
| [[daily-42305134-f1]] | `10.21769/BioProtoc.5707` | protein interaction | Subsequently, a swellable polyelectrolyte gel is synthesized throughout the biological sample, while the modified biomol… |
| [[daily-42306252-f1]] | `10.1093/aobpla/plag023` | genetic perturbation | We show how this approach can be used qualitatively and quantitatively to study cell shape and lignin deposition during … |
| [[daily-42306252-f2]] | `10.1093/aobpla/plag023` | protein interaction | Congo red and calcofluor white are two commonly used dyes that bind to cellulose ( ). |
| [[daily-42306421-f5]] | `10.3389/fpls.2026.1833157` | protein interaction | Although the concentrations of these compounds are typically much lower than that of DA, they may rise significantly und… |
| [[daily-42306421-f6]] | `10.3389/fpls.2026.1833157` | protein interaction | For instance, high concentrations of L-DOPA (the precursor of DA) and tyramine may weakly interact with GRAB-DA2h, albei… |

（另有 78 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **因果级证据占比仅 6.4%**：机制结论的可信度受限于此，建议对排名靠前的子主题定向补做扰动实验或查找已有突变体表型数据。
- **2 个子主题完全没有因果层证据**（单细胞与组学方法、表型组与高通量筛选）：这些方向目前只能写相关性。
- **1259 条证据（82%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4100 个中文字符，行内证据链接 95 处，密度 **11.6 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
