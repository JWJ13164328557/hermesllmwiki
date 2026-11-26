---

title: "激素与信号转导 — Synthesis"
created: 2026-06-01
total_evidence: 2050
total_papers: 385
library_papers: 473  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-26
tags: [hormone, signaling, synthesis]
legacy_archive: _review/synthesis_legacy_20261126/hormone-signaling.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 激素与信号转导 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 2050 | 本主题归属的证据对象数 |
| 独立论文 | 385 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 5.32 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 5% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(594)、Arabidopsis thaliana(545)、Zea mays(423)、Solanum lycopersicum(362)、Nicotiana tabacum(210)、Triticum aestivum(193) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1214；protein interaction 293；expression/regulation 160；phenotypic/association 143；genetic perturbation 115；DNA binding/regulation 68 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated o |
| `daily-42967137-f2` | 10.1093/hr/uhag234 | Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the exp |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to  |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenoty |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked c |
| `daily-42588902-f1` | 10.3390/plants15152398 | In summary, STA1 (Category II) establishes a relatively complete chain from cold-induced e |
| `daily-42967137-f7` | 10.1093/hr/uhag234 | The tiny-plant phenotype of the oeNtMYB1 narcissus bulb and Arabidopsis partially recovere |
| `daily-42299846-f3` | 10.1093/plcell/koag187 | We found that CESA particle speeds in the plasma membrane were relatively insensitive to i |
| `daily-42122890-f4` | 10.3390/plants15091398 | Overexpression of PsnSAUR6 in transgenic tobacco conferred superior drought tolerance, evi |
| `daily-42227011-f3` | 10.1093/hr/uhag047 | In the sdg8 mutant, the levels of H3K36me2/me3 on the chromatin of target genes such as FL |
| `daily-42273211-f6` | 10.3389/fpls.2026.1834029 | The auxin signaling mutant tir1afb2 exhibits reduced accumulation of H2O2 and superoxide a |
| `daily-42213848-f7` | 10.1126/sciadv.adz4776 | Collectively, these findings indicate that the mutant’s SA-insensitive phenotype primarily |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 115 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 293 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 68 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 160 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 143 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 57 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1214 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated on alterati |
| `daily-42967137-f2` | 10.1093/hr/uhag234 | Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to largely al |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenotype To test |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked changes in  |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-26 由 `rebuild_synthesis_body.py` 从 **2050 条证据对象 / 385 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261126`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **2050 条证据 / 385 篇文献**。规则判定为因果或直接调控的 **476 条（23.2%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **257 条**。可判定程度最高的结论集中在PnCYP710A、SOC1、PsnSAUR6：Overexpression of PnCYP710A in tobacco enhanced resistance to F.（[[daily-40898642-f2]]）；These results indicated that overexpression of ZmGRAS46 inhibited the expression of CO, FT, SOC1, and LFY genes.（[[daily-41376114-f7]]）；Overexpression of PsnSAUR6 in transgenic tobacco conferred superior drought tolerance, evidenced by increased biomass, enhanced root elongat…（[[daily-42122890-f4]]）。研究重心位于“逆境中的激素调控”（312 条证据，占 15%）。证据的物种分布以 Oryza sativa 为首（594 条，29%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 2050 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 385 | 去重后的论文数 |
| 平均每篇证据数 | 5.32 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 5%（19/385） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(1214)、protein interaction(293)、expression/regulation(160)、phenotypic/association(143)、genetic perturbation(115)、DNA binding/regulation(68)、omics/co-occurrence(57) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(1248)、medium(645)、high(129)、未标(28) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(594)、Arabidopsis thaliana(545)、Zea mays(423)、Solanum lycopersicum(362)、Nicotiana tabacum(210)、Triticum aestivum(193) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1344（66%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **476 条**，占本主题证据的 **23.2%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 594 条证据（29%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 112 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 受体感知与早期信号转导

**规模** 103 条证据 / 68 篇文献；**构成** descriptive/observational(47)、protein interaction(38)、expression/regulation(7)、genetic perturbation(5)、DNA binding/regulation(3)、phenotypic/association(3)；**因果层** 46 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Solanum lycopersicum、Oryza sativa、Arabidopsis thaliana，反复出现的实体为BIN2、BAK1、auxin、melatonin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]）。
- **证据层级的张力**：46 条属于遗传扰动/蛋白互作/DNA 结合，57 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]）。
- **可检验缺口**：组学共现在本组缺证据；在补齐这些设计前，BIN2、BAK1、auxin 与“受体感知与早期信号转导”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Solanum lycopersicum | 3 | 11 | 1 | 4 | 0 | 16 | 35 |
| Oryza sativa | 1 | 19 | 1 | 2 | 1 | 6 | 30 |
| Arabidopsis thaliana | 2 | 12 | 1 | 0 | 0 | 13 | 28 |
| Zea mays | 1 | 12 | 2 | 1 | 1 | 5 | 22 |
| Nicotiana tabacum | 1 | 5 | 1 | 0 | 1 | 6 | 14 |

**基因实体（自动标注，前 5）**：BIN2(6)、BAK1(5)、BRI1(4)、PP2C(3)、HvPMTR1(3)（标注覆盖 59/103）。

**化合物实体（自动标注，前 5）**：auxin(4)、melatonin(3)、brassinosteroid(2)、abscisic acid(2)、sucrose(1)（标注覆盖 13/103）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42719693-f5]]。

**代表断言（原文摘录，未改写）**

- “Generally, the initial step in PHY signal transduction involves PHYA perceiving FR light or PHYB-PHYE perceiving red light, leading to conforma tional changes between Pr and Pfr, u…” — [[ms-10-1186_s12870-026-08649-w-f3]]（`10.1186/s12870-026-08649-w`，protein interaction）
- “In Arabidopsis thaliana, ARF activity is dynamically regulated by AUX/IAA proteins: in the absence of auxin, AUX/IAAs (e.g., IAA9) interact with ARFs (e.g., ARF7) to inhibit their …” — [[ms-10-3389_fpls-2026-1830107-f3]]（`10.3389/fpls.2026.1830107`，protein interaction）
- “Briefly, ABA binds to intercellular Pyrabactin Resistance/ Regulatory Component of ABA Receptor (PYR/RCAR) receptors to inhibit the PP2C.A type protein phosphatases, which leads to…” — [[ref-mcz160-f4]]（`10.1093/aob/mcz160`，protein interaction）

### 2.2 转录调控与激素响应基因

**规模** 167 条证据 / 96 篇文献；**构成** descriptive/observational(69)、protein interaction(56)、DNA binding/regulation(17)、genetic perturbation(11)、expression/regulation(8)、omics/co-occurrence(3)；**因果层** 84 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Arabidopsis thaliana，反复出现的实体为ARF2、CsbZIP44、auxin、anthocyanin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[biology-and-function-of-mir159-in-f2]]；[[biology-and-function-of-mir159-in-f5]]；[[biology-and-function-of-mir159-in-f6]]）。
- **证据层级的张力**：84 条属于遗传扰动/蛋白互作/DNA 结合，83 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[cotton-fiber-development-molecular-regulation-f3]]；[[cotton-fiber-development-molecular-regulation-f4]]；[[daily-40954952-f4]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[cotton-fiber-development-molecular-regulation-f3]]；[[cotton-fiber-development-molecular-regulation-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 4 | 25 | 4 | 3 | 1 | 0 | 19 | 56 |
| Zea mays | 4 | 11 | 5 | 0 | 0 | 0 | 28 | 48 |
| Arabidopsis thaliana | 1 | 21 | 3 | 3 | 0 | 1 | 19 | 48 |
| Nicotiana tabacum | 4 | 9 | 4 | 1 | 0 | 0 | 15 | 33 |
| Solanum lycopersicum | 3 | 12 | 3 | 1 | 0 | 1 | 12 | 32 |

**基因实体（自动标注，前 5）**：ARF2(5)、CsbZIP44(5)、PIN1(4)、ARF3(4)、BZR1(4)（标注覆盖 115/167）。

**化合物实体（自动标注，前 5）**：auxin(14)、anthocyanin(4)、ethylene(4)、carotenoid(3)、phenylpropanoid(2)（标注覆盖 31/167）。

**标注一致性提示**：本组 4 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-40954952-f6]]。

**代表断言（原文摘录，未改写）**

- “Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of upstream genes NtKS1 and NtGA20ox in the GA biosynthesis pathway; however, NtMY…” — [[daily-42967137-f2]]（`10.1093/hr/uhag234`，genetic perturbation）
- “The regulation of fiber initiation versus elongation involves specific interactions; for instance, MYB16 (GhMML4_D12), a MIXTA-like TF, does not interact with a bHLH but with a div…” — [[cotton-fiber-development-molecular-regulation-f4]]（`10.1186/s42397-026-00264-2`，protein interaction）
- “Beyond OsBZR1, OsGSK2 and its homologs phosphorylate ricespecific transcription factors such as DWARF AND LOWTILLERING (DLT), LEAF AND TILLER ANGLE INCREASED CONTROLLER (LIC), REDU…” — [[daily-42244175-f7]]（`10.1111/nph.71320`，protein interaction）

### 2.3 激素合成与稳态

**规模** 109 条证据 / 84 篇文献；**构成** descriptive/observational(63)、protein interaction(17)、expression/regulation(10)、phenotypic/association(8)、DNA binding/regulation(6)、genetic perturbation(3)；**因果层** 26 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Solanum lycopersicum、Oryza sativa，反复出现的实体为ERF109、ERF013、auxin、carotenoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]；[[comparative-transcriptome-profiling-reveals-the-multiple-f2]]；[[daily-40702403-f1]]）。
- **证据层级的张力**：26 条属于遗传扰动/蛋白互作/DNA 结合，83 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-40853041-f6]]；[[daily-42244175-f8]]；[[comparative-transcriptome-profiling-reveals-the-multiple-f2]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-40853041-f6]]；[[daily-42244175-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 6 | 1 | 3 | 2 | 1 | 22 | 36 |
| Solanum lycopersicum | 0 | 2 | 3 | 5 | 2 | 0 | 15 | 27 |
| Oryza sativa | 1 | 6 | 1 | 1 | 2 | 1 | 12 | 24 |
| Zea mays | 0 | 4 | 1 | 0 | 0 | 0 | 15 | 20 |
| Nicotiana tabacum | 1 | 1 | 1 | 0 | 0 | 0 | 8 | 11 |

**基因实体（自动标注，前 5）**：ERF109(4)、ERF013(3)、ZmLOX2(2)、MAM1(2)、MdbHLH162(2)（标注覆盖 51/109）。

**化合物实体（自动标注，前 5）**：auxin(14)、carotenoid(5)、anthocyanin(5)、phenylpropanoid(4)、flavonoid(3)（标注覆盖 42/109）。

**代表断言（原文摘录，未改写）**

- “PbRR9-like directly activates the expression of the auxin biosynthesis gene indole-3- pyruvate monooxygenase 4 (PbYUC4) to increase the content of IAA (auxin) while directly inhibi…” — [[gibberellin-biosynthesis-is-required-for-cppu-induced-f2]]（`10.1093/hr/uhad084`，DNA binding/regulation）
- “Studies have found that Aux/IAA proteins not only indirectly influence ABA signal transduction by regulating auxin and ABA biosynthesis/metabolic pathways but also that some member…” — [[daily-42245099-f7]]（`10.3389/fpls.2026.1823723`，protein interaction）
- “Activated ethylene signaling can also reduce levels of bioactive GAs by inhibiting GA biosynthesis enzymes such as GA20ox (Achard et al., 2007), and the ethylene-regulated transcri…” — [[ms-10-3389_fpls-2026-1905836-f3]]（`10.3389/fpls.2026.1905836`，protein interaction）

### 2.4 激素间互作与权衡

**规模** 48 条证据 / 44 篇文献；**构成** descriptive/observational(27)、protein interaction(14)、DNA binding/regulation(2)、omics/co-occurrence(2)、phenotypic/association(1)、genetic perturbation(1)；**因果层** 17 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Solanum lycopersicum，反复出现的实体为GSK2、OsDLA、auxin、gibberellin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]；[[daily-40702403-f3]]；[[daily-40853041-f6]]）。
- **证据层级的张力**：17 条属于遗传扰动/蛋白互作/DNA 结合，31 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-40853041-f6]]；[[daily-42244175-f5]]；[[daily-41922966-f2]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-40853041-f6]]；[[daily-42244175-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 7 | 1 | 1 | 0 | 0 | 8 | 18 |
| Zea mays | 0 | 2 | 1 | 1 | 0 | 0 | 3 | 7 |
| Solanum lycopersicum | 0 | 1 | 2 | 0 | 0 | 0 | 4 | 7 |
| Nicotiana tabacum | 1 | 0 | 1 | 0 | 0 | 0 | 5 | 7 |
| Arabidopsis thaliana | 0 | 2 | 0 | 1 | 0 | 0 | 4 | 7 |

**基因实体（自动标注，前 5）**：GSK2(1)、OsDLA(1)、OsWRKY53(1)、PpGS2(1)、OsBRI1(1)（标注覆盖 19/48）。

**化合物实体（自动标注，前 5）**：auxin(3)、gibberellin(1)、sucrose(1)、phenylpropanoid(1)、terpenoid(1)（标注覆盖 7/48）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[the-redfar-red-light-photoreceptor-fvephyb-regulates-f1]]。

**代表断言（原文摘录，未改写）**

- “The physical interaction between COM2 and the consensus DNAbinding motif of its downstream targets had been validated in previous studies (Li, Li, et al.,; Lin et al.,; Wang et al.…” — [[daily-42490165-f3]]（`10.1111/tpj.71040`，protein interaction）
- “Combined with the significant upregulation of JA biosynthesisand signaling-related genes in the OE lines, these findings suggest that the interaction between ZmLOX2 and AOS1 may fa…” — [[daily-42588762-f3]]（`10.3390/plants15152258`，protein interaction）
- “However, the available evidence suggests that the reduction in KBC symptoms severity observed in CAR-treated plants is likely attributable primarily to the direct interaction betwe…” — [[daily-42654935-f6]]（`10.3390/plants15162533`，protein interaction）

### 2.5 生长发育中的激素功能

**规模** 47 条证据 / 35 篇文献；**构成** descriptive/observational(22)、protein interaction(9)、phenotypic/association(8)、genetic perturbation(5)、DNA binding/regulation(2)、expression/regulation(1)；**因果层** 16 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Nicotiana tabacum，反复出现的实体为FRO6、RTNLB16、ethylene、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[circadian-rheostat-proton-gradient-arabidopsis-f3]]；[[daily-42026737-f1]]；[[daily-42026737-f2]]）。
- **证据层级的张力**：16 条属于遗传扰动/蛋白互作/DNA 结合，31 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42226098-f1]]；[[daily-42244175-f7]]；[[daily-42315982-f4]]）。
- **可检验缺口**：组学共现在本组缺证据；在补齐这些设计前，FRO6、RTNLB16、ethylene 与“生长发育中的激素功能”的方向性关系应作为待检验命题（[[circadian-rheostat-proton-gradient-arabidopsis-f3]]；[[daily-42026737-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 3 | 1 | 1 | 1 | 13 | 22 |
| Oryza sativa | 0 | 4 | 0 | 0 | 2 | 6 | 12 |
| Nicotiana tabacum | 1 | 3 | 1 | 0 | 0 | 2 | 7 |
| Malus domestica | 1 | 3 | 1 | 0 | 0 | 1 | 6 |
| Solanum lycopersicum | 0 | 2 | 1 | 0 | 2 | 1 | 6 |

**基因实体（自动标注，前 5）**：FRO6(3)、RTNLB16(2)、SlBZR1(2)、CCA1(1)、PsnSAUR6(1)（标注覆盖 20/47）。

**化合物实体（自动标注，前 5）**：ethylene(3)、auxin(2)、sucrose(1)、phenolic(1)、salicylic acid(1)（标注覆盖 8/47）。

**代表断言（原文摘录，未改写）**

- “Mild heat stress can also induce ethylene production in leaves, which interacts with auxin and ROS pathways (Huang et al., ) and can affect reproductive development by promoting pr…” — [[daily-42432422-f1]]（`10.1111/nph.71422`，protein interaction）
- “Combined transcriptome deep sequencing and chromatin immunoprecipitation followed by sequencing identified 73 SlBZR1repressed targets and 203 SlBZR1induced targets involving major …” — [[the-brassinosteroid-signaling-component-slbzr1-promotes-f3]]（`10.1111/jipb.13491`，DNA binding/regulation）
- “Loss-of-function mutants of SCL30a displayed reduced ABA sensitivity in both root growth and seed germination assays, whereas complementation or overexpression of three stable isof…” — [[daily-42280772-f6]]（`10.3390/plants15111735`，genetic perturbation）

### 2.6 逆境中的激素调控

**规模** 312 条证据 / 145 篇文献；**构成** descriptive/observational(155)、phenotypic/association(51)、protein interaction(32)、expression/regulation(30)、genetic perturbation(26)、omics/co-occurrence(11)；**因果层** 65 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Solanum lycopersicum，反复出现的实体为IbbHLH129、CsBT2、auxin、phenylpropanoid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f1]]；[[daily-40629672-f3]]；[[daily-40702403-f4]]）。
- **证据层级的张力**：65 条属于遗传扰动/蛋白互作/DNA 结合，247 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-40853041-f6]]；[[daily-42122890-f4]]；[[daily-40898642-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-40853041-f6]]；[[daily-42122890-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 6 | 18 | 0 | 6 | 12 | 2 | 46 | 90 |
| Arabidopsis thaliana | 9 | 12 | 1 | 8 | 3 | 3 | 22 | 58 |
| Solanum lycopersicum | 6 | 5 | 0 | 10 | 11 | 0 | 24 | 56 |
| Triticum aestivum | 2 | 3 | 0 | 6 | 9 | 1 | 34 | 55 |
| Zea mays | 3 | 9 | 1 | 3 | 7 | 3 | 21 | 47 |

**基因实体（自动标注，前 5）**：IbbHLH129(5)、CsBT2(4)、SnRK2(4)、SlbHLH70(4)、ERF013(4)（标注覆盖 117/312）。

**化合物实体（自动标注，前 5）**：auxin(8)、phenylpropanoid(5)、dopamine(4)、terpenoid(3)、salicylic acid(3)（标注覆盖 35/312）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42490165-f1]]。

**代表断言（原文摘录，未改写）**

- “Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated on alterations of photosynthetic systems, responses to water deficiency, heat as well as ph…” — [[daily-42211481-f2]]（`10.3389/fpls.2026.1815995`，genetic perturbation）
- “The ABA-dependent regulation of the circadian clock gene GIGANTEA (GI) facilitates drought escape (DE) mechanisms by modulating FT., The OST1 homolog SlOST1 in tomato, accelerates …” — [[daily-42249761-f6]]（`10.1080/15592324.2026.2684387`，protein interaction）
- “In summary, STA1 (Category II) establishes a relatively complete chain from cold-induced expression and splicing to target splicing events and cold-sensitive phenotypes, although t…” — [[daily-42588902-f1]]（`10.3390/plants15152398`，genetic perturbation）

### 2.7 信号转导的定量与动态特征

**规模** 47 条证据 / 40 篇文献；**构成** descriptive/observational(33)、expression/regulation(6)、phenotypic/association(3)、protein interaction(2)、omics/co-occurrence(2)、DNA binding/regulation(1)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Solanum lycopersicum、Zea mays、Arabidopsis thaliana，反复出现的实体为CLV1、CLV3、auxin、dopamine；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f6]]；[[daily-41189573-f5]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，44 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42197561-f3]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]）。
- **可检验缺口**：遗传扰动在本组缺证据；在补齐这些设计前，CLV1、CLV3、auxin 与“信号转导的定量与动态特征”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Solanum lycopersicum | 0 | 0 | 3 | 1 | 0 | 8 | 12 |
| Zea mays | 0 | 1 | 2 | 0 | 0 | 7 | 10 |
| Arabidopsis thaliana | 0 | 0 | 1 | 0 | 0 | 7 | 8 |
| Triticum aestivum | 1 | 0 | 0 | 0 | 0 | 5 | 6 |
| Oryza sativa | 0 | 0 | 3 | 0 | 0 | 2 | 5 |

**基因实体（自动标注，前 5）**：CLV1(1)、CLV3(1)、ARF5(1)、PIN1(1)、TMO5(1)（标注覆盖 10/47）。

**化合物实体（自动标注，前 5）**：auxin(5)、dopamine(1)、lignin(1)、flavonoid(1)、melatonin(1)（标注覆盖 9/47）。

**代表断言（原文摘录，未改写）**

- “Molecular dynamics modeling and the study of the UV–visible spectral characteristics of HSs in the presence of IAA revealed the ability of HSs to bind to this auxin, which helps ma…” — [[ms-10-3390_ijms27125494-f3]]（`10.3390/ijms27125494`，protein interaction）
- “These phytohormonal gradients interact with the TDIF - PXY - WOX pathway, maintaining cambial homeostasis and adapting to environmental cues such as temperature and photoperiod [ ]…” — [[daily-41829741-f6]]（`10.3390/plants15050710`，protein interaction）
- “Such hierarchical regulation (WRKY33 and MYB51) directly regulates the dynamics of camalexin and related indolic pathways in Arabidopsis.” — [[daily-42197561-f3]]（`10.3390/plants15101424`，DNA binding/regulation）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| SnRK2 | 6 | 12 | 信号转导的定量与动态特征、受体感知与早期信号转导、激素合成与稳态、激素间互作与权衡、转录调控与激素响应基因、逆境中的激素调控 |
| NPR1 | 5 | 8 | 受体感知与早期信号转导、激素合成与稳态、激素间互作与权衡、转录调控与激素响应基因、逆境中的激素调控 |
| CsbZIP44 | 4 | 9 | 信号转导的定量与动态特征、激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| CsHB5 | 4 | 8 | 信号转导的定量与动态特征、激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| ABI5 | 4 | 5 | 受体感知与早期信号转导、激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| SnRK2s | 4 | 5 | 受体感知与早期信号转导、激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| ERF013 | 3 | 8 | 激素合成与稳态、生长发育中的激素功能、逆境中的激素调控 |
| IbbHLH129 | 3 | 7 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| CmBHLH93 | 3 | 6 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| PIN1 | 3 | 6 | 信号转导的定量与动态特征、受体感知与早期信号转导、转录调控与激素响应基因 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| auxin | 7 | 50 | 信号转导的定量与动态特征、受体感知与早期信号转导、激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |
| sucrose | 6 | 8 | 受体感知与早期信号转导、激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |
| ethylene | 4 | 12 | 激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |
| phenylpropanoid | 4 | 12 | 激素合成与稳态、激素间互作与权衡、转录调控与激素响应基因、逆境中的激素调控 |
| anthocyanin | 4 | 11 | 激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因 |
| carotenoid | 4 | 10 | 激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |

### 3.1 跨子主题受控叙述

- **交叉实体**：SnRK2、NPR1、CsbZIP44、CsHB5、ABI5 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转录调控与激素响应基因”（84 条），最低为“信号转导的定量与动态特征”（3 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 受体感知与早期信号转导 | 5 | 38 | 3 | 7 | 3 | — | 47 |
| 转录调控与激素响应基因 | 11 | 56 | 17 | 8 | 3 | 3 | 69 |
| 激素合成与稳态 | 3 | 17 | 6 | 10 | 8 | 2 | 63 |
| 激素间互作与权衡 | 1 | 14 | 2 | 1 | 1 | 2 | 27 |
| 生长发育中的激素功能 | 5 | 9 | 2 | 1 | 8 | — | 22 |
| 逆境中的激素调控 | 26 | 32 | 7 | 30 | 51 | 11 | 155 |
| 信号转导的定量与动态特征 | — | 2 | 1 | 6 | 3 | 2 | 33 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 476 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[10-1146-annurev-arplant-042817-f3]] | `10.1146/annurev-arplant-042817-040549` | DNA binding/regulation | More in-depth studies found that WUS directly regulates additional cytokininand auxin-related genes, possibly controllin… |
| [[10-1146-annurev-arplant-042817-f4]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | HOMEODOMAIN LEUCINE ZIPPER (HD-ZIP III) genes, whose protein products interact with the type-B RRs and bind the same WUS… |
| [[10-1146-annurev-arplant-042817-f7]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CIKs also interact with other CLV receptors and are phosphorylated by CLV1, suggesting that they act as a direct downstr… |
| [[10-1146-annurev-arplant-042817-f8]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged meristems and function … |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f1]] | `10.1111/tpj.70902` | protein interaction | All these data imply that TCP21 directly interacts with phyB likely in a light-dependent manner. |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f2]] | `10.1111/tpj.70902` | protein interaction | Further, we found that the N-terminal region of HY5 was required for its interaction with TCP21 (Figure S6). |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f3]] | `10.1111/tpj.70902` | protein interaction | These findings strongly suggest that TCP21 inhibits the transcriptional activity of HY5, probably by impairing its abili… |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f4]] | `10.1111/tpj.70902` | protein interaction | These findings strongly support the conclusion that phyB inhibits TCP21’s transcriptional activity, likely by interferin… |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f7]] | `10.1111/tpj.70902` | protein interaction | PhyB physically interacts with TCP21 and inhibits its transcriptional activity. |
| [[biology-and-function-of-mir159-in-f2]] | `10.3390/plants8080255` | genetic perturbation | Then, overexpression of miR159 in Arabidopsis [ecotype Landsberg erecta, (Ler)] resulted in down-regulation of MYB33 exp… |
| [[circadian-rheostat-proton-gradient-arabidopsis-f7]] | `10.1016/j.cell.2025.12.056` | protein interaction | Regulation of hypocotyl growth by CCA1 relies on multiple entry points as CCA1 activates PIFs and interacts with auxin-r… |
| [[comparative-transcriptome-profiling-reveals-the-multiple-f7]] | `10.1111/pbi.14063` | DNA binding/regulation | Y1H and EMSA results indicated that BnaC2.FUS3 could directly bind to the P1 site of the BnaA6.KO promoter (Figure 3g,h)… |
| [[cotton-fiber-development-molecular-regulation-f1]] | `10.1186/s42397-026-00264-2` | DNA binding/regulation | DNA Affinity Purification Sequencing (DAP-seq) analysis revealed that GhSBP1 binds to the GTAC motif and directly activa… |
| [[cotton-fiber-development-molecular-regulation-f3]] | `10.1186/s42397-026-00264-2` | DNA binding/regulation | Journal of Cotton Research (2026) 9:18 demonstrated that GhMYB212 directly activates the sucrose transporter gene SUGARS… |
| [[cotton-fiber-development-molecular-regulation-f4]] | `10.1186/s42397-026-00264-2` | protein interaction | The regulation of fiber initiation versus elongation involves specific interactions; for instance, MYB16 (GhMML4_D12), a… |
| [[cotton-fiber-development-molecular-regulation-f6]] | `10.1186/s42397-026-00264-2` | protein interaction | Homeobox-leucine zipper protein 3 (GhHOX3), which is highly expressed during the elongation stage, interacts with the TC… |
| [[cotton-fiber-development-molecular-regulation-f8]] | `10.1186/s42397-026-00264-2` | protein interaction | (2020) demonstrated that GhTCP4 interacts with GhHOX3 and represses its transcriptional activity. |
| [[daily-39996429-f1]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Our findings suggest that the enhanced immunity observed in Arabidopsis cds1cds2 mutant was attributable to multiple fac… |
| [[daily-39996429-f2]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Here, we found that knock-down of the CDS gene enhanced the resistance of Arabidopsis thaliana to multiple pathogens, wi… |
| [[daily-39996429-f3]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Our data suggest that AtS40, NGAL2, RGL3, and other genes associated with embryonic development and growth in plants wer… |

（另有 456 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 5 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| PIN1 | regulation direction dispute | [[daily-41829741]]；[[daily-42122902]]；[[daily-42243683]] |
| PP2C | regulation direction dispute | [[daily-42220070]]；[[daily-42423212]]；[[ref-mcz160]] |
| PP2A | regulation direction dispute | [[daily-42226070]]；[[daily-42665660]] |
| BZR1 | regulation direction dispute | [[daily-42237121]]；[[daily-42422551]]；[[daily-42514610]] |
| SNF1 | regulation direction dispute | [[daily-42249761]]；[[ref-mcz160]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **1344 条证据（66%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261126`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4769 个中文字符，行内证据链接 118 处，密度 **12.4 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
