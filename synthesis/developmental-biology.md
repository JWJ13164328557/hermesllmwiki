---

title: "发育生物学 — Synthesis"
created: 2026-06-01
total_evidence: 3308
total_papers: 658
library_papers: 779  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-24
tags: [synthesis, development]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261124/developmental-biology.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 植物发育生物学 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 3308 | 本主题归属的证据对象数 |
| 独立论文 | 658 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 5.03 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 6% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(1037)、Oryza sativa(994)、Zea mays(649)、Solanum lycopersicum(440)、Triticum aestivum(381)、Nicotiana tabacum(346) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 2247；protein interaction 285；expression/regulation 231；phenotypic/association 219；genetic perturbation 162；omics/co-occurrence 102 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated o |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to  |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenoty |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked c |
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication compl |
| `daily-42635641-f5` | 10.1007/s00299-026-03945-z | A Schematic representation of the T-DNA region of AtU6-26_pRGEB31 gRNAs multiplex construc |
| `ms-10-1007_s00344-026-12266-0-f2` | 10.1007/s00344-026-12266-0 | While novel_47 (targeting the DNA repair gene BRCA2) was upregulated in both genotypes, it |
| `daily-42317260-f4` | 10.3389/fgene.2026.1850332 | The results showed that a total of 16 QTLs associated with pod number, notably, overlappin |
| `daily-42514563-f2` | 10.3390/plants15142197 | The Arabidopsis argonaute 10 ( ago10 ) mutant exhibits defects in AM initiation, and in th |
| `blue-light-photoreceptor-cryptochrome-1-promotes-f1` | 10.1111/pce.14866 | The WT accumulated much higher anthocyanin under blue light than the other light treatment |
| `daily-42958739-f5` | 10.1111/tpj.71175 | When dipinoculated with Pst DC3000, the impa1 mutants exhibited increased susceptibility,  |
| `daily-42304209-f6` | 10.1186/s12870-026-09279-y | Although both EgMADS03 and EgMADS45 influenced flowering time, EgMADS03 was ultimately sel |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 162 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 285 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 62 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 231 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 219 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 102 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 2247 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated on alterati |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to largely al |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenotype To test |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked changes in  |
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are suf |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-24 由 `rebuild_synthesis_body.py` 从 **3308 条证据对象 / 658 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261124`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **3308 条证据 / 658 篇文献**。规则判定为因果或直接调控的 **509 条（15.4%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **233 条**。可判定程度最高的结论集中在PagCRY1、KO4：The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abolished the anthocyani…（[[blue-light-photoreceptor-cryptochrome-1-promotes-f1]]）；In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly increased in cry1 mu…（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]）；Overexpression of PagCRY1 substantially inhibited plant growth and promoted secondary xylem development in Populus, while CRISPR/Cas9 mediat…（[[blue-light-photoreceptor-cryptochrome-1-promotes-f4]]）。研究重心位于“激素与发育信号整合”（149 条证据，占 5%）。证据的物种分布以 Arabidopsis thaliana 为首（1037 条，31%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 3308 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 658 | 去重后的论文数 |
| 平均每篇证据数 | 5.03 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 6%（37/658） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(2247)、protein interaction(285)、expression/regulation(231)、phenotypic/association(219)、genetic perturbation(162)、omics/co-occurrence(102)、DNA binding/regulation(62) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(2333)、medium(788)、high(170)、未标(17) | 低置信度标注须回原文核对 |
| 主要物种 | Arabidopsis thaliana(1037)、Oryza sativa(994)、Zea mays(649)、Solanum lycopersicum(440)、Triticum aestivum(381)、Nicotiana tabacum(346) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 2715（82%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **509 条**，占本主题证据的 **15.4%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Arabidopsis thaliana** 出现在 1037 条证据（31%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 102 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 分生组织维持与干细胞稳态

**规模** 129 条证据 / 76 篇文献；**构成** descriptive/observational(81)、expression/regulation(21)、protein interaction(9)、omics/co-occurrence(7)、DNA binding/regulation(5)、genetic perturbation(4)；**因果层** 18 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为CLV3、WOX5、auxin、gibberellin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b3-peg1lwq2yaEXfDY9yfqzZg-f4]]；[[b5-iZzyxHmz_WpXAsbrHTBStw-f5]]；[[daily-41481480-f2]]）。
- **证据层级的张力**：18 条属于遗传扰动/蛋白互作/DNA 结合，111 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-41481480-f2]]；[[daily-42558264-f3]]；[[daily-41829741-f8]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-41481480-f2]]；[[daily-42558264-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 5 | 3 | 14 | 1 | 3 | 46 | 75 |
| Oryza sativa | 2 | 3 | 3 | 8 | 1 | 1 | 29 | 47 |
| Zea mays | 0 | 6 | 1 | 10 | 0 | 1 | 16 | 34 |
| Solanum lycopersicum | 0 | 2 | 1 | 6 | 0 | 0 | 7 | 16 |
| Nicotiana tabacum | 1 | 0 | 0 | 0 | 0 | 0 | 11 | 12 |

**基因实体（自动标注，前 5）**：CLV3(6)、WOX5(4)、ARR15(3)、ARR7(3)、TCX2(3)（标注覆盖 48/129）。

**化合物实体（自动标注，前 5）**：auxin(7)、gibberellin(1)、ethylene(1)（标注覆盖 9/129）。

**代表断言（原文摘录，未改写）**

- “Growth habit is regulated by the interaction between the Dt1 gene, which encodes the TFL1 protein that suppresses floral meristem formation ( ), and the Dt2 gene, which encodes a M…” — [[daily-42558264-f3]]（`10.1270/jsbbs.25075`，DNA binding/regulation）
- “Overexpression of CDS (35S:: CDS ) caused severe growth inhibition, disrupted root meristem organization, reduced cell number, enlarged cell size, and decreased CYCB1;1 activity, i…” — [[daily-41481480-f2]]（`10.1080/15592324.2025.2611175`，genetic perturbation）
- “These findings demonstrate that the tw mutation not only disrupts the organization and fertility of the barley spike but also causes variable effects on floral organ identity and m…” — [[daily-42717293-f3]]（`10.1111/nph.71533`，genetic perturbation）

### 2.2 细胞分裂与细胞周期

**规模** 50 条证据 / 28 篇文献；**构成** descriptive/observational(25)、protein interaction(11)、genetic perturbation(5)、DNA binding/regulation(4)、expression/regulation(3)、omics/co-occurrence(1)；**因果层** 20 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为CDK8、OE12、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[blue-light-photoreceptor-cryptochrome-1-promotes-f3]]；[[daily-41481480-f3]]）。
- **证据层级的张力**：20 条属于遗传扰动/蛋白互作/DNA 结合，30 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[daily-42260696-f5]]；[[blue-light-photoreceptor-cryptochrome-1-promotes-f3]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[daily-42260696-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 5 | 1 | 3 | 0 | 0 | 14 | 24 |
| Oryza sativa | 2 | 3 | 1 | 1 | 0 | 0 | 5 | 12 |
| Zea mays | 1 | 4 | 0 | 1 | 0 | 0 | 6 | 12 |
| Nicotiana tabacum | 1 | 3 | 0 | 0 | 0 | 0 | 6 | 10 |
| Solanum lycopersicum | 3 | 3 | 0 | 1 | 0 | 0 | 2 | 9 |

**基因实体（自动标注，前 5）**：CDK8(6)、OE12(2)、RBR1(2)、KO4(1)、PagCRY1aOE(1)（标注覆盖 23/50）。

**化合物实体（自动标注，前 5）**：lignin(1)（标注覆盖 1/50）。

**代表断言（原文摘录，未改写）**

- “Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are sufficient to increase ploidy level in trichomes (Castellano et al., 2001; Castella…” — [[ref-tab-0120-f2]]（`10.1199/tab.0120`，genetic perturbation）
- “In tobacco, NtmybA1 and NtmybA2 bind to mitosis-specific activator (MSA) elements; two structurally related genes— MYB3R1 and MYB3R4, which encode homologs of NtmybA1 and NtmybA2 i…” — [[daily-42581385-f6]]（`10.1186/s43897-026-00272-5`，protein interaction）
- “In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly increased in cry1 mutant plants, we found a group of cell cy…” — [[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]（`10.1111/pce.14866`，genetic perturbation）

### 2.3 细胞命运决定与分化

**规模** 123 条证据 / 75 篇文献；**构成** descriptive/observational(77)、expression/regulation(20)、phenotypic/association(8)、protein interaction(7)、omics/co-occurrence(6)、genetic perturbation(3)；**因果层** 12 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为WIND1、LEC2、auxin、coumarin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f3]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f5]]；[[b3-qnkDB6_AeT3N0ZaAwqrgng-f4]]）。
- **证据层级的张力**：12 条属于遗传扰动/蛋白互作/DNA 结合，111 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]]；[[daily-42580706-f5]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]]；[[daily-42580706-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 4 | 1 | 15 | 3 | 3 | 47 | 74 |
| Oryza sativa | 0 | 3 | 0 | 2 | 1 | 2 | 21 | 29 |
| Zea mays | 0 | 3 | 1 | 7 | 2 | 1 | 11 | 25 |
| Nicotiana tabacum | 0 | 1 | 0 | 2 | 1 | 0 | 12 | 16 |
| Solanum lycopersicum | 1 | 0 | 1 | 4 | 0 | 0 | 7 | 13 |

**基因实体（自动标注，前 5）**：WIND1(5)、LEC2(2)、CLV3(2)、EpSC(2)、VND6(2)（标注覆盖 31/123）。

**化合物实体（自动标注，前 5）**：auxin(5)、coumarin(1)、phenylpropanoid(1)、gibberellin(1)、brassinosteroid(1)（标注覆盖 9/123）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[plant-stem-cell-organization-and-differentiation-at-single-cell-resolution-f3]]。

**代表断言（原文摘录，未改写）**

- “The GRAS-type transcription factor SHR is synthesized in the stele and moves through plasmodesmata into the adjacent cell layer ( ), where it interacts with its downstream target S…” — [[daily-43013668-f4]]（`10.1126/sciadv.aeh6396`，protein interaction）
- “We found that irreversible differentiation of guard cells involves RETINOBLASTOMA-RELATED (RBR) recruitment to regulatory regions of master regulators of stomatal initiation, facil…” — [[ref-eLife-03271-f4]]（`10.7554/eLife.03271`，protein interaction）
- “This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot apical meristem and demonstrates that genes expressed in org…” — [[ref-35050091-f5]]（`10.1038/35050091`，protein interaction）

### 2.4 器官发生与形态建成

**规模** 73 条证据 / 57 篇文献；**构成** descriptive/observational(45)、phenotypic/association(8)、genetic perturbation(7)、expression/regulation(6)、protein interaction(5)、omics/co-occurrence(1)；**因果层** 13 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为TgSWO、ZmASB1、auxin、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42026737-f1]]；[[daily-42026737-f2]]；[[daily-42026737-f4]]）。
- **证据层级的张力**：13 条属于遗传扰动/蛋白互作/DNA 结合，60 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42430664-f8]]；[[daily-42625500-f8]]；[[daily-42241415-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42430664-f8]]；[[daily-42625500-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 3 | 1 | 4 | 0 | 1 | 21 | 33 |
| Oryza sativa | 1 | 3 | 1 | 3 | 1 | 1 | 16 | 26 |
| Zea mays | 3 | 2 | 1 | 0 | 2 | 0 | 7 | 15 |
| Solanum lycopersicum | 1 | 0 | 0 | 1 | 1 | 0 | 5 | 8 |
| Rosa spp. | 1 | 0 | 0 | 3 | 0 | 0 | 3 | 7 |

**基因实体（自动标注，前 5）**：TgSWO(3)、ZmASB1(3)、GPM1(1)、SbiGRF1(1)、SbiMIR396d(1)（标注覆盖 25/73）。

**化合物实体（自动标注，前 5）**：auxin(8)、sucrose(1)、phenolic(1)、terpenoid(1)、ethylene(1)（标注覆盖 13/73）。

**代表断言（原文摘录，未改写）**

- “The coexpression network analysis between OsERF48 and root-specific overexpression of ERF48 root RNA-seq data showed that calmodulinlike protein genes, OsCML16, is a direct target …” — [[ref-ppl-13651-f3]]（`10.1111/ppl.13651`，DNA binding/regulation）
- “MsNAC17 significantly enhances the root growth capacity of apple rootstocks under drought stress, and the growth advantage conferred by its overexpression constitutes an important …” — [[daily-42430664-f8]]（`10.1093/plphys/kiag488`，genetic perturbation）
- “In rice root architecture regulation, SLs interact with IAA by regulating primary and adventitious root elongation, lateral root formation, secondary root growth, and AR initiation…” — [[daily-42710900-f4]]（`10.1111/ppl.71099`，protein interaction）

### 2.5 激素与发育信号整合

**规模** 149 条证据 / 96 篇文献；**构成** descriptive/observational(84)、protein interaction(22)、expression/regulation(16)、phenotypic/association(11)、genetic perturbation(7)、DNA binding/regulation(7)；**因果层** 36 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Zea mays、Oryza sativa，反复出现的实体为PIN1、PIN3、auxin、ethylene；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41829741-f4]]；[[daily-41829741-f5]]；[[daily-41829741-f8]]）。
- **证据层级的张力**：36 条属于遗传扰动/蛋白互作/DNA 结合，113 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42122902-f2]]；[[daily-42234526-f1]]；[[daily-41829741-f8]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42122902-f2]]；[[daily-42234526-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 5 | 7 | 6 | 8 | 3 | 2 | 43 | 74 |
| Zea mays | 2 | 10 | 4 | 2 | 1 | 0 | 15 | 34 |
| Oryza sativa | 2 | 6 | 3 | 1 | 2 | 1 | 19 | 34 |
| Solanum lycopersicum | 0 | 2 | 4 | 2 | 0 | 0 | 14 | 22 |
| Glycine max | 1 | 2 | 0 | 1 | 0 | 0 | 8 | 12 |

**基因实体（自动标注，前 5）**：PIN1(5)、PIN3(3)、AHP6(3)、ERF115(3)、EIN3(2)（标注覆盖 71/149）。

**化合物实体（自动标注，前 5）**：auxin(89)、ethylene(18)、gibberellin(6)、brassinosteroid(6)、jasmonic acid(3)（标注覆盖 118/149）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42243683-f8]]。

**代表断言（原文摘录，未改写）**

- “In Arabidopsis thaliana, ARF activity is dynamically regulated by AUX/IAA proteins: in the absence of auxin, AUX/IAAs (e.g., IAA9) interact with ARFs (e.g., ARF7) to inhibit their …” — [[ms-10-3389_fpls-2026-1830107-f3]]（`10.3389/fpls.2026.1830107`，protein interaction）
- “Genetic data further place SPL/NZZ within an auxin-linked competence module: an miR160 target ARF17 promotes MMC specification through interaction with SPL/NZZ and helps delimit PI…” — [[daily-42122902-f2]]（`10.3390/plants15091410`，protein interaction）
- “In this capacity, phytomelatonin modulates antioxidant enzyme systems, regulates stomatal behavior, influences the expression of ion transporters, and interacts with major phytohor…” — [[daily-42243187-f4]]（`10.1038/s41598-026-55742-z`，protein interaction）

### 2.6 表观调控与发育可塑性

**规模** 73 条证据 / 47 篇文献；**构成** descriptive/observational(45)、protein interaction(9)、expression/regulation(9)、DNA binding/regulation(4)、omics/co-occurrence(3)、genetic perturbation(2)；**因果层** 15 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为GL2、HAC1；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f1]]；[[b4-0Ai2UdSwKz-GbYdfit26vw-f1]]；[[daily-42075434-f7]]）。
- **证据层级的张力**：15 条属于遗传扰动/蛋白互作/DNA 结合，58 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42244175-f6]]；[[daily-42514591-f5]]；[[daily-42239049-f6]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42244175-f6]]；[[daily-42514591-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 6 | 3 | 5 | 0 | 0 | 17 | 32 |
| Oryza sativa | 1 | 2 | 0 | 3 | 0 | 2 | 12 | 20 |
| Zea mays | 0 | 2 | 1 | 1 | 0 | 1 | 9 | 14 |
| Nicotiana tabacum | 1 | 3 | 1 | 1 | 0 | 0 | 8 | 14 |
| Glycine max | 0 | 0 | 0 | 1 | 0 | 2 | 5 | 8 |

**基因实体（自动标注，前 5）**：GL2(3)、HAC1(2)、AtGCN5(2)、AGO9(1)、RDR6(1)（标注覆盖 27/73）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42452277-f1]]。

**代表断言（原文摘录，未改写）**

- “Thebromodomain binds to acetylated histone lysine motifs (Zeng and Zhou, 2002), and therefore can be considered as a reader of histoneacetylationmarkers.T-DNAinsertionsingcn5-1andg…” — [[ref-ssq018-f8]]（`10.1093/mp/ssq018`，protein interaction）
- “Quantitative detection, correlation analysis, luciferase reporter assays, and chromatin immunoprecipitation confirmed that TGF-β1 induces miR-184 transcription in a SMAD4-dependent…” — [[ms-10-24272_j-issn-2095-8137-2025-578-f5]]（`10.24272/j.issn.2095-8137.2025.578`，DNA binding/regulation）
- “In transcriptionally active regions, i.e., open chromatin regions, nucleosome arrays are relatively loosely arranged [ ], and the intervening DNA sequences frequently interact with…” — [[daily-42075434-f7]]（`10.3390/plants15081233`，protein interaction）

### 2.7 再生与愈伤组织形成

**规模** 109 条证据 / 62 篇文献；**构成** descriptive/observational(76)、phenotypic/association(12)、omics/co-occurrence(8)、protein interaction(5)、expression/regulation(4)、genetic perturbation(3)；**因果层** 9 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Solanum lycopersicum、Oryza sativa，反复出现的实体为WIND1、ERF115、auxin、flavonoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[cr-10-1038-nature08152-f1]]；[[cr-10-1038-nature08152-f2]]；[[cr-10-1038-nature08152-f6]]）。
- **证据层级的张力**：9 条属于遗传扰动/蛋白互作/DNA 结合，100 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42643750-f1]]；[[ms-10-1371_journal-pgen-1012300-f2]]；[[daily-42330275-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42643750-f1]]；[[ms-10-1371_journal-pgen-1012300-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 3 | 1 | 1 | 1 | 4 | 26 | 37 |
| Solanum lycopersicum | 0 | 1 | 0 | 0 | 3 | 2 | 22 | 28 |
| Oryza sativa | 1 | 4 | 1 | 0 | 2 | 3 | 13 | 24 |
| Zea mays | 1 | 2 | 1 | 0 | 1 | 3 | 13 | 21 |
| Pinus spp. | 0 | 0 | 0 | 3 | 2 | 0 | 6 | 11 |

**基因实体（自动标注，前 5）**：WIND1(4)、ERF115(3)、CB037(2)、OsBBM1(1)、OsGS3(1)（标注覆盖 21/109）。

**化合物实体（自动标注，前 5）**：auxin(7)、flavonoid(3)、ascorbic acid(1)（标注覆盖 11/109）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-1007_s12374-026-09525-8-f4]]。

**代表断言（原文摘录，未改写）**

- “In conclusion, the observed physical interaction between ERF115 and PAT1 combined with the co-expression of their genes and additive effects of the double mutants and overexpressio…” — [[ref-nplants-2016-165-f2]]（`10.1038/nplants.2016.165`，protein interaction）
- “Under hypoxic conditions created by limited gas exchange in developing calli, the hypoxia-activated RELATED TO APETALA 2.12 (RAP2.12) directly binds to the promoter of the ICS1 gen…” — [[ref-nph-70171-f4]]（`10.1111/nph.70171`，DNA binding/regulation）
- “The interaction between 6-BA and IAA had a predominant effect on the incidence of embryogenic cells, which were identified based on the classic morphological criteria for plant som…” — [[daily-42491681-f7]]（`10.7717/peerj.21520`，protein interaction）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| WIND1 | 5 | 12 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、激素与发育信号整合、细胞命运决定与分化、表观调控与发育可塑性 |
| ERF115 | 3 | 8 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、激素与发育信号整合 |
| PIN1 | 3 | 7 | 分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合 |
| GL2 | 3 | 5 | 细胞分裂与细胞周期、细胞命运决定与分化、表观调控与发育可塑性 |
| ARR1 | 3 | 4 | 激素与发育信号整合、细胞命运决定与分化、表观调控与发育可塑性 |
| CYCD3 | 3 | 4 | 分生组织维持与干细胞稳态、激素与发育信号整合、细胞分裂与细胞周期 |
| LEC2 | 3 | 4 | 分生组织维持与干细胞稳态、细胞命运决定与分化、表观调控与发育可塑性 |
| WOX11 | 3 | 4 | 器官发生与形态建成、激素与发育信号整合、细胞命运决定与分化 |
| ABPH1 | 3 | 3 | 分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合 |
| AtE2Fc | 3 | 3 | 分生组织维持与干细胞稳态、细胞分裂与细胞周期、细胞命运决定与分化 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| auxin | 5 | 116 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合、细胞命运决定与分化 |
| ethylene | 3 | 20 | 分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合 |
| gibberellin | 3 | 8 | 分生组织维持与干细胞稳态、激素与发育信号整合、细胞命运决定与分化 |
| brassinosteroid | 2 | 7 | 激素与发育信号整合、细胞命运决定与分化 |
| flavonoid | 2 | 4 | 再生与愈伤组织形成、器官发生与形态建成 |
| jasmonic acid | 2 | 4 | 器官发生与形态建成、激素与发育信号整合 |

### 3.1 跨子主题受控叙述

- **交叉实体**：WIND1、ERF115、PIN1、GL2、ARR1 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（摘要 et al., 2016 [[10-7554-elife-17214-001-f1]]；摘要 et al., 2016 [[10-7554-elife-17214-001-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“激素与发育信号整合”（36 条），最低为“再生与愈伤组织形成”（9 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 分生组织维持与干细胞稳态 | 4 | 9 | 5 | 21 | 2 | 7 | 81 |
| 细胞分裂与细胞周期 | 5 | 11 | 4 | 3 | 1 | 1 | 25 |
| 细胞命运决定与分化 | 3 | 7 | 2 | 20 | 8 | 6 | 77 |
| 器官发生与形态建成 | 7 | 5 | 1 | 6 | 8 | 1 | 45 |
| 激素与发育信号整合 | 7 | 22 | 7 | 16 | 11 | 2 | 84 |
| 表观调控与发育可塑性 | 2 | 9 | 4 | 9 | 1 | 3 | 45 |
| 再生与愈伤组织形成 | 3 | 5 | 1 | 4 | 12 | 8 | 76 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 509 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[10-7554-elife-17214-001-f4]] | `10.7554/eLife.17214` | protein interaction | PWR binds to the same genomic regions as HDA9 at HDA9 targets. |
| [[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]] | `10.1007/s44412-025-00004-4` | protein interaction | In tetraploid wheat, AGL6 interacts with multiple classes of MADS-box genes within the ABCDE model, coordinating their f… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f3]] | `10.1111/pbi.70348` | protein interaction | They interact with A-, B-, and C-class genes to form complexes, a mechanism known as the “tetramer model”. |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f4]] | `10.1111/pbi.70348` | protein interaction | For instance, it may bind to specific promoter regions of target genes, where it can recruit other transcriptional machi… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f5]] | `10.1111/pbi.70348` | genetic perturbation | The flowers of plants with miR172 target site mutations show phenotypes with enlarged meristems and excessive stamens. |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f7]] | `10.1111/pbi.70348` | protein interaction | It interacts with other genes to jointly regulate processes such as cell division, differentiation, and elongation, ther… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f8]] | `10.1111/pbi.70348` | protein interaction | TGA9 and TGA10 can directly interact with ROXY1 and ROXY2 [ ]. |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f1]] | `10.1111/pce.14866` | genetic perturbation | The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abol… |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f2]] | `10.1111/pce.14866` | genetic perturbation | In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly … |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f4]] | `10.1111/pce.14866` | genetic perturbation | Overexpression of PagCRY1 substantially inhibited plant growth and promoted secondary xylem development in Populus, whil… |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f5]] | `10.1111/pce.14866` | genetic perturbation | Overexpression of PagCRY1 dramatically increased anthocyanin accumulation. |
| [[daily-39710817-f1]] | `10.1007/s13353-024-00927-3` | protein interaction | It was reported that WOX9 can directly bind to ARF5 via its C-terminal domain (CTDW) to form the WOX9-ARF5 complex, whic… |
| [[daily-40635304-f1]] | `10.1111/pbi.70217` | DNA binding/regulation | In summary, these findings suggest that the normal GoPGF protein directly binds to the promoters of multiple WRKY genes,… |
| [[daily-40635304-f4]] | `10.1111/pbi.70217` | protein interaction | This leads to production of GoPGF that in turn binds to Gbox and MYC elements within the promoters of WRKY genes thereby… |
| [[daily-40635304-f6]] | `10.1111/pbi.70217` | protein interaction | Together, these results conclusively demonstrate that GoSPGF can directly and specifically bind to the ‘AGAC’ motif in t… |
| [[daily-40893112-f4]] | `10.1080/21645698.2025.2555037` | genetic perturbation | Reported that overexpression of the NsVP1 gene from Nitraria sibirica, significantly enhanced salt tolerance in Arabidop… |
| [[daily-40893112-f5]] | `10.1080/21645698.2025.2555037` | genetic perturbation | These findings suggest that the overexpression of LfVP1 enhances the ability of yeast strains to withstand osmotic stres… |
| [[daily-40893112-f7]] | `10.1080/21645698.2025.2555037` | genetic perturbation | For example, overexpression of the AVP1 gene, which encodes the H + -pyrophosphatase pump in Arabidopsis thaliana, signi… |
| [[daily-40893112-f8]] | `10.1080/21645698.2025.2555037` | genetic perturbation | In another study, the knockdown of the HVP1 gene inhibited growth and increased Na + accumulation in barley, while its o… |
| [[daily-41132147-f4]] | `10.1080/21645698.2025.2578048` | genetic perturbation | We found that overexpression suppressed antioxidant enzyme activities and promoted senescence, whereas the NtBAG5 mutant… |

（另有 489 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 5 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| CYCB1 | regulation direction dispute | [[daily-41481480]]；[[ref-tpc-106-044834]] |
| PIN1 | regulation direction dispute | [[daily-41829741]]；[[daily-42122902]]；[[daily-42243683]] |
| TFL1 | regulation direction dispute | [[daily-42266649]]；[[daily-42327663]]；[[daily-42558264]] |
| CLV3 | regulation direction dispute | [[daily-42319924]]；[[ref-annurev-arplant-042811-10]]；[[ref-annurev-cellbio-100617-06]] |
| BRC1 | regulation direction dispute | [[daily-42324804]]；[[daily-42324804]]；[[daily-42430661]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **2715 条证据（82%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261124`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4610 个中文字符，行内证据链接 120 处，密度 **13.0 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
