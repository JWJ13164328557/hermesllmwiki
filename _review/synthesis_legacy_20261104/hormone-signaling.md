---

title: "激素与信号转导 — Synthesis"
created: 2026-06-01
total_evidence: 2362
total_papers: 383
library_papers: 473  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [hormone, signaling, synthesis]
legacy_archive: _review/synthesis_legacy_20261103/hormone-signaling.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 激素与信号转导 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 2362 | 本主题归属的证据对象数 |
| 独立论文 | 383 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 6.17 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 3% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(692)、Arabidopsis thaliana(629)、Zea mays(483)、Solanum lycopersicum(417)、Nicotiana tabacum(244)、Triticum aestivum(236) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 1391；protein interaction 309；expression/regulation 262；phenotypic/association 154；genetic perturbation 119；DNA binding/regulation 65 | 表达/关联类居多时，因果结论需打折扣 |

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
| `daily-42423212-f4` | 10.1080/15592324.2026.2700909 | Wheat evidence does support its functional relevance: manipulation of ABA receptor signali |
| `daily-42273211-f6` | 10.3389/fpls.2026.1834029 | The auxin signaling mutant tir1afb2 exhibits reduced accumulation of H2O2 and superoxide a |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 119 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 309 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 65 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 262 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 154 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 62 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1391 | 描述性/背景陈述（未报告可核验的实验设计） |

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

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **1320 条证据对象 / 223 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **1320 条证据 / 223 篇文献**。规则判定为因果或直接调控的 **283 条（21.4%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **170 条**。可判定程度最高的结论集中在PbrARF13、PbrMYB132、PsnSAUR6：Overexpression of PbrARF13 decreased stone cell content in pear fruit and secondary cell wall (SCW) thickness in transgenic Arabidopsis plan…（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f5]]）；As expected, overexpression or knockdown of PbrMYB132 increased or decreased stone cell content in pear fruit and SCW thickness in Arabidops…（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f6]]）；Overexpression of PsnSAUR6 in transgenic tobacco conferred superior drought tolerance, evidenced by increased biomass, enhanced root elongat…（[[daily-42122890-f4]]）。研究重心位于“逆境中的激素调控”（162 条证据，占 12%）。证据的物种分布以 Oryza sativa 为首（555 条，42%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 1320 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 223 | 去重后的论文数 |
| 平均每篇证据数 | 5.92 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 8%（18/223） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(832)、protein interaction(168)、expression/regulation(153)、genetic perturbation(66)、DNA binding/regulation(49)、omics/co-occurrence(35)、phenotypic/association(17) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(912)、medium(331)、high(77) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(555)、Arabidopsis thaliana(483)、Zea mays(417)、Solanum lycopersicum(312)、Nicotiana tabacum(289)、Triticum aestivum(142) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 862（65%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **283 条**，占本主题证据的 **21.4%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 555 条证据（42%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 75 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 受体感知与早期信号转导

**规模** 68 条证据 / 43 篇文献；**构成** protein interaction(28)、descriptive/observational(28)、expression/regulation(5)、genetic perturbation(4)、DNA binding/regulation(2)、phenotypic/association(1)；**因果层** 34 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Arabidopsis thaliana，反复出现的实体为BIN2、PCK1、auxin、brassinosteroid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]）。
- **证据层级的张力**：34 条属于遗传扰动/蛋白互作/DNA 结合，34 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]）。
- **可检验缺口**：组学共现在本组缺证据；在补齐这些设计前，BIN2、PCK1、auxin 与“受体感知与早期信号转导”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f7]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Oryza sativa | 2 | 15 | 1 | 2 | 0 | 7 | 27 |
| Solanum lycopersicum | 0 | 8 | 1 | 3 | 0 | 12 | 24 |
| Arabidopsis thaliana | 2 | 7 | 1 | 1 | 0 | 13 | 24 |
| Zea mays | 1 | 13 | 1 | 2 | 1 | 4 | 22 |
| Nicotiana tabacum | 1 | 7 | 1 | 0 | 0 | 8 | 17 |

**基因实体（自动标注，前 5）**：BIN2(6)、PCK1(4)、CLV1(3)、MAX2(3)、BRI1(3)（标注覆盖 42/68）。

**化合物实体（自动标注，前 5）**：auxin(3)、brassinosteroid(2)、sucrose(1)、strigolactone(1)（标注覆盖 7/68）。

**代表断言（原文摘录，未改写）**

- “Generally, the initial step in PHY signal transduction involves PHYA perceiving FR light or PHYB-PHYE perceiving red light, leading to conforma tional changes between Pr and Pfr, u…” — [[ms-10-1186_s12870-026-08649-w-f3]]（`10.1186/s12870-026-08649-w`，protein interaction）
- “In Arabidopsis thaliana, ARF activity is dynamically regulated by AUX/IAA proteins: in the absence of auxin, AUX/IAAs (e.g., IAA9) interact with ARFs (e.g., ARF7) to inhibit their …” — [[ms-10-3389_fpls-2026-1830107-f3]]（`10.3389/fpls.2026.1830107`，protein interaction）
- “Briefly, ABA binds to intercellular Pyrabactin Resistance/ Regulatory Component of ABA Receptor (PYR/RCAR) receptors to inhibit the PP2C.A type protein phosphatases, which leads to…” — [[ref-mcz160-f4]]（`10.1093/aob/mcz160`，protein interaction）

### 2.2 转录调控与激素响应基因

**规模** 138 条证据 / 74 篇文献；**构成** descriptive/observational(59)、protein interaction(42)、DNA binding/regulation(12)、genetic perturbation(11)、expression/regulation(8)、phenotypic/association(3)；**因果层** 65 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Arabidopsis thaliana、Nicotiana tabacum，反复出现的实体为PbrARF13、CsbZIP44、auxin、cellulose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f1]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f2]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f3]]）。
- **证据层级的张力**：65 条属于遗传扰动/蛋白互作/DNA 结合，73 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f5]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f6]]；[[daily-40523045-f7]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f5]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 5 | 21 | 4 | 3 | 2 | 2 | 24 | 61 |
| Arabidopsis thaliana | 5 | 17 | 3 | 5 | 0 | 1 | 23 | 54 |
| Nicotiana tabacum | 6 | 14 | 4 | 1 | 1 | 0 | 27 | 53 |
| Zea mays | 2 | 14 | 4 | 3 | 0 | 2 | 24 | 49 |
| Solanum lycopersicum | 4 | 10 | 3 | 1 | 1 | 2 | 18 | 39 |

**基因实体（自动标注，前 5）**：PbrARF13(6)、CsbZIP44(6)、PbrNSC(4)、EgrARF10(4)、CsHB5(4)（标注覆盖 100/138）。

**化合物实体（自动标注，前 5）**：auxin(13)、cellulose(4)、lignin(4)、ethylene(4)、carotenoid(4)（标注覆盖 30/138）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42243683-f8]]。

**代表断言（原文摘录，未改写）**

- “This domain enables bZIP transcription factors to specifically recognize and bind to particular DNA sequences, thereby regulating the expression of downstream genes., With the incr…” — [[daily-40523045-f3]]（`10.1080/21645698.2025.2510715`，protein interaction）
- “Overexpression of NtMYB1 and NtMYB1 / NtbZIP53 in transgenic narcissus upregulated the expression of upstream genes NtKS1 and NtGA20ox in the GA biosynthesis pathway; however, NtMY…” — [[daily-42967137-f2]]（`10.1093/hr/uhag234`，genetic perturbation）
- “The regulation of fiber initiation versus elongation involves specific interactions; for instance, MYB16 (GhMML4_D12), a MIXTA-like TF, does not interact with a bHLH but with a div…” — [[cotton-fiber-development-molecular-regulation-f4]]（`10.1186/s42397-026-00264-2`，protein interaction）

### 2.3 激素合成与稳态

**规模** 77 条证据 / 56 篇文献；**构成** descriptive/observational(50)、protein interaction(10)、expression/regulation(8)、DNA binding/regulation(6)、phenotypic/association(1)、genetic perturbation(1)；**因果层** 17 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为PbrARF13、ERF109、auxin、anthocyanin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f1]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f2]]）。
- **证据层级的张力**：17 条属于遗传扰动/蛋白互作/DNA 结合，60 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f8]]；[[comparative-transcriptome-profiling-reveals-the-multiple-f2]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]]；[[auxin-inhibits-lignin-and-cellulose-biosynthesis-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 0 | 4 | 3 | 6 | 0 | 1 | 23 | 37 |
| Oryza sativa | 1 | 2 | 2 | 3 | 1 | 1 | 16 | 26 |
| Zea mays | 0 | 3 | 2 | 4 | 0 | 0 | 11 | 20 |
| Solanum lycopersicum | 0 | 0 | 3 | 2 | 0 | 0 | 13 | 18 |
| Nicotiana tabacum | 1 | 2 | 1 | 0 | 1 | 0 | 12 | 17 |

**基因实体（自动标注，前 5）**：PbrARF13(4)、ERF109(4)、PbrNSC(3)、PbrMYB132(2)、BZR1(2)（标注覆盖 46/77）。

**化合物实体（自动标注，前 5）**：auxin(21)、anthocyanin(5)、cellulose(4)、lignin(4)、ethylene(4)（标注覆盖 42/77）。

**代表断言（原文摘录，未改写）**

- “PbRR9-like directly activates the expression of the auxin biosynthesis gene indole-3- pyruvate monooxygenase 4 (PbYUC4) to increase the content of IAA (auxin) while directly inhibi…” — [[gibberellin-biosynthesis-is-required-for-cppu-induced-f2]]（`10.1093/hr/uhad084`，DNA binding/regulation）
- “Studies have found that Aux/IAA proteins not only indirectly influence ABA signal transduction by regulating auxin and ABA biosynthesis/metabolic pathways but also that some member…” — [[daily-42245099-f7]]（`10.3389/fpls.2026.1823723`，protein interaction）
- “Activated ethylene signaling can also reduce levels of bioactive GAs by inhibiting GA biosynthesis enzymes such as GA20ox (Achard et al., 2007), and the ethylene-regulated transcri…” — [[ms-10-3389_fpls-2026-1905836-f3]]（`10.3389/fpls.2026.1905836`，protein interaction）

### 2.4 激素间互作与权衡

**规模** 26 条证据 / 23 篇文献；**构成** descriptive/observational(14)、expression/regulation(5)、protein interaction(4)、DNA binding/regulation(2)、genetic perturbation(1)；**因果层** 7 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Nicotiana tabacum，反复出现的实体为BrKAN2、NtMYB1、auxin、phenolic；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]；[[daily-42122890-f6]]；[[daily-42226109-f8]]）。
- **证据层级的张力**：7 条属于遗传扰动/蛋白互作/DNA 结合，19 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42967137-f2]]；[[red-and-blue-light-promote-tomato-f1]]；[[daily-42403402-f1]]）。
- **可检验缺口**：表型关联、组学共现在本组缺证据；在补齐这些设计前，BrKAN2、NtMYB1、auxin 与“激素间互作与权衡”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]；[[daily-42122890-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Oryza sativa | 1 | 2 | 1 | 4 | 6 | 14 |
| Zea mays | 0 | 1 | 1 | 4 | 5 | 11 |
| Nicotiana tabacum | 1 | 0 | 1 | 1 | 4 | 7 |
| Solanum lycopersicum | 0 | 1 | 2 | 1 | 2 | 6 |
| Arabidopsis thaliana | 0 | 1 | 0 | 2 | 3 | 6 |

**基因实体（自动标注，前 5）**：BrKAN2(1)、NtMYB1(1)、NtGA3ox2(1)、NtbZIP53(1)、NtGA20ox(1)（标注覆盖 5/26）。

**化合物实体（自动标注，前 5）**：auxin(2)、phenolic(1)、anthocyanin(1)、salicylic acid(1)（标注覆盖 5/26）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[the-redfar-red-light-photoreceptor-fvephyb-regulates-f1]]。

**代表断言（原文摘录，未改写）**

- “The signaling molecule jasmonate plays a central role in this process, and studies indicate that the interaction between jasmonate signaling and other hormones (e.g., salicylic aci…” — [[ms-10-3389_fpls-2026-1815183-f1]]（`10.3389/fpls.2026.1815183`，protein interaction）
- “Hypoxia signals induced by flooding can interact with bZIP proteins via ERF transcription factors to synergistically regulate the expression of downstream genes, thereby enabling a…” — [[daily-42226109-f8]]（`10.1186/s12870-026-09081-w`，protein interaction）
- “More in-depth studies found that WUS directly regulates additional cytokininand auxin-related genes, possibly controlling the balance between these two hormones, and also regulates…” — [[10-1146-annurev-arplant-042817-f3]]（`10.1146/annurev-arplant-042817-040549`，DNA binding/regulation）

### 2.5 生长发育中的激素功能

**规模** 39 条证据 / 29 篇文献；**构成** descriptive/observational(18)、protein interaction(7)、genetic perturbation(6)、expression/regulation(3)、DNA binding/regulation(2)、phenotypic/association(2)；**因果层** 15 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Nicotiana tabacum，反复出现的实体为SlBZR1、CCA1、ethylene、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[circadian-rheostat-proton-gradient-arabidopsis-f3]]；[[daily-42026737-f1]]；[[daily-42026737-f2]]）。
- **证据层级的张力**：15 条属于遗传扰动/蛋白互作/DNA 结合，24 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42226098-f1]]；[[daily-42244154-f3]]；[[daily-42410097-f3]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42226098-f1]]；[[daily-42244154-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 4 | 3 | 0 | 2 | 0 | 0 | 7 | 16 |
| Oryza sativa | 2 | 3 | 1 | 1 | 2 | 1 | 5 | 15 |
| Nicotiana tabacum | 2 | 3 | 2 | 0 | 1 | 0 | 4 | 12 |
| Malus domestica | 2 | 4 | 1 | 0 | 0 | 0 | 2 | 9 |
| Solanum lycopersicum | 0 | 2 | 1 | 0 | 0 | 0 | 5 | 8 |

**基因实体（自动标注，前 5）**：SlBZR1(2)、CCA1(1)、PsnSAUR6(1)、CsBT2(1)、OsNAP(1)（标注覆盖 21/39）。

**化合物实体（自动标注，前 5）**：ethylene(3)、auxin(2)、sucrose(1)、phenolic(1)、salicylic acid(1)（标注覆盖 10/39）。

**代表断言（原文摘录，未改写）**

- “Overexpression of ZmSPL12 suppresses maize root growth under normal, wellwatered (WW) conditions, but this effect was substantially attenuated under soil compaction stress, resulti…” — [[daily-42773404-f5]]（`10.1111/nph.71592`，genetic perturbation）
- “The direct effect of CO2 on root biomass may be weaker, and its effect often interacts with environmental factors such as water status or temperature, for example, CO2 can indirect…” — [[ms-10-3389_fpls-2026-1830107-f1]]（`10.3389/fpls.2026.1830107`，protein interaction）
- “Combined transcriptome deep sequencing and chromatin immunoprecipitation followed by sequencing identified 73 SlBZR1repressed targets and 203 SlBZR1induced targets involving major …” — [[the-brassinosteroid-signaling-component-slbzr1-promotes-f3]]（`10.1111/jipb.13491`，DNA binding/regulation）

### 2.6 逆境中的激素调控

**规模** 162 条证据 / 75 篇文献；**构成** descriptive/observational(91)、genetic perturbation(23)、expression/regulation(22)、protein interaction(18)、omics/co-occurrence(5)、DNA binding/regulation(2)；**因果层** 43 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Solanum lycopersicum，反复出现的实体为CsBT2、CmBHLH93、phenolic、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Renhui et al., 2023 [[combining-single-cell-rna-sequencing-with-spatial-transcriptome-analysis-reveals-f1]]；[[daily-39996429-f1]]；[[daily-40523045-f8]]）。
- **证据层级的张力**：43 条属于遗传扰动/蛋白互作/DNA 结合，119 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42122890-f4]]；[[daily-42197717-f6]]；[[daily-42218724-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42122890-f4]]；[[daily-42197717-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 8 | 9 | 1 | 8 | 1 | 3 | 46 | 76 |
| Zea mays | 8 | 3 | 2 | 4 | 0 | 0 | 25 | 42 |
| Solanum lycopersicum | 3 | 3 | 0 | 7 | 1 | 0 | 25 | 39 |
| Arabidopsis thaliana | 7 | 3 | 1 | 9 | 0 | 1 | 16 | 37 |
| Nicotiana tabacum | 9 | 8 | 1 | 1 | 0 | 1 | 17 | 37 |

**基因实体（自动标注，前 5）**：CsBT2(4)、CmBHLH93(4)、PeCHYR1(4)、MdD53(3)、NAC17(3)（标注覆盖 74/162）。

**化合物实体（自动标注，前 5）**：phenolic(5)、auxin(5)、dopamine(4)、abscisic acid(2)、lignin(1)（标注覆盖 18/162）。

**代表断言（原文摘录，未改写）**

- “The head domain interacts with RNA polymerase II and general transcription factors (TFs) while the tail domain interacts with specific TFs (reviewed in Freytes et al., ), and conta…” — [[daily-42732616-f8]]（`10.1111/tpj.71107`，protein interaction）
- “Our previous studies preliminarily identified a HTH-responsive transcription factor, GmPHD3, which interacts with the key HTH stress regulator GmSBH1 and exhibits distinct expressi…” — [[daily-42588879-f5]]（`10.3390/plants15152376`，protein interaction）
- “Overexpression of PsnSAUR6 in transgenic tobacco conferred superior drought tolerance, evidenced by increased biomass, enhanced root elongation, improved stomatal regulation, and f…” — [[daily-42122890-f4]]（`10.3390/plants15091398`，genetic perturbation）

### 2.7 信号转导的定量与动态特征

**规模** 30 条证据 / 26 篇文献；**构成** descriptive/observational(22)、omics/co-occurrence(3)、expression/regulation(2)、protein interaction(2)、DNA binding/regulation(1)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Zea mays、Arabidopsis thaliana、Solanum lycopersicum，反复出现的实体为CLV1、CLV3、auxin、dopamine；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f6]]；Renhui et al., 2023 [[combining-single-cell-rna-sequencing-with-spatial-transcriptome-analysis-reveals-f1]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，27 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42197561-f3]]；[[daily-42654832-f7]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]）。
- **可检验缺口**：遗传扰动、表型关联在本组缺证据；在补齐这些设计前，CLV1、CLV3、auxin 与“信号转导的定量与动态特征”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f5]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Zea mays | 0 | 1 | 2 | 1 | 8 | 12 |
| Arabidopsis thaliana | 0 | 0 | 0 | 0 | 9 | 9 |
| Solanum lycopersicum | 0 | 0 | 2 | 0 | 5 | 7 |
| Triticum aestivum | 1 | 0 | 0 | 0 | 6 | 7 |
| Oryza sativa | 0 | 0 | 2 | 1 | 3 | 6 |

**基因实体（自动标注，前 5）**：CLV1(1)、CLV3(1)、MYB51(1)、WRKY33(1)、SlARF8B(1)（标注覆盖 10/30）。

**化合物实体（自动标注，前 5）**：auxin(3)、dopamine(1)、anthocyanin(1)、flavonoid(1)（标注覆盖 6/30）。

**代表断言（原文摘录，未改写）**

- “A recent study further reveals that MdLBD37 binds to the lateral organ boundaries (LOB) element in the promoter of MdBZR1, forming a MdBZR1-MdLBD37 positive feedback regulatory loo…” — [[daily-42654832-f7]]（`10.3390/plants15162429`，protein interaction）
- “Molecular dynamics modeling and the study of the UV–visible spectral characteristics of HSs in the presence of IAA revealed the ability of HSs to bind to this auxin, which helps ma…” — [[ms-10-3390_ijms27125494-f3]]（`10.3390/ijms27125494`，protein interaction）
- “Such hierarchical regulation (WRKY33 and MYB51) directly regulates the dynamics of camalexin and related indolic pathways in Arabidopsis.” — [[daily-42197561-f3]]（`10.3390/plants15101424`，DNA binding/regulation）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| CsbZIP44 | 4 | 10 | 信号转导的定量与动态特征、激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| CsHB5 | 4 | 8 | 信号转导的定量与动态特征、激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| CmBHLH93 | 3 | 6 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| NtMYB1 | 3 | 6 | 激素合成与稳态、激素间互作与权衡、转录调控与激素响应基因 |
| ABI5 | 3 | 5 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| NAC17 | 3 | 5 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| OsMYB305 | 3 | 5 | 激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| PP2C | 3 | 5 | 受体感知与早期信号转导、转录调控与激素响应基因、逆境中的激素调控 |
| PUB30 | 3 | 5 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |
| ZmSPL12 | 3 | 5 | 激素合成与稳态、生长发育中的激素功能、逆境中的激素调控 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| auxin | 7 | 49 | 信号转导的定量与动态特征、受体感知与早期信号转导、激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |
| anthocyanin | 5 | 10 | 信号转导的定量与动态特征、激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因 |
| phenolic | 5 | 10 | 激素合成与稳态、激素间互作与权衡、生长发育中的激素功能、转录调控与激素响应基因、逆境中的激素调控 |
| sucrose | 4 | 5 | 受体感知与早期信号转导、激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| ethylene | 3 | 11 | 激素合成与稳态、生长发育中的激素功能、转录调控与激素响应基因 |
| lignin | 3 | 9 | 激素合成与稳态、转录调控与激素响应基因、逆境中的激素调控 |

### 3.1 跨子主题受控叙述

- **交叉实体**：CsbZIP44、CsHB5、CmBHLH93、NtMYB1、ABI5 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“转录调控与激素响应基因”（65 条），最低为“信号转导的定量与动态特征”（3 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 受体感知与早期信号转导 | 4 | 28 | 2 | 5 | 1 | — | 28 |
| 转录调控与激素响应基因 | 11 | 42 | 12 | 8 | 3 | 3 | 59 |
| 激素合成与稳态 | 1 | 10 | 6 | 8 | 1 | 1 | 50 |
| 激素间互作与权衡 | 1 | 4 | 2 | 5 | — | — | 14 |
| 生长发育中的激素功能 | 6 | 7 | 2 | 3 | 2 | 1 | 18 |
| 逆境中的激素调控 | 23 | 18 | 2 | 22 | 1 | 5 | 91 |
| 信号转导的定量与动态特征 | — | 2 | 1 | 2 | — | 3 | 22 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 283 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[10-1146-annurev-arplant-042817-f3]] | `10.1146/annurev-arplant-042817-040549` | DNA binding/regulation | More in-depth studies found that WUS directly regulates additional cytokininand auxin-related genes, possibly controllin… |
| [[10-1146-annurev-arplant-042817-f4]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | HOMEODOMAIN LEUCINE ZIPPER (HD-ZIP III) genes, whose protein products interact with the type-B RRs and bind the same WUS… |
| [[10-1146-annurev-arplant-042817-f7]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CIKs also interact with other CLV receptors and are phosphorylated by CLV1, suggesting that they act as a direct downstr… |
| [[10-1146-annurev-arplant-042817-f8]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged meristems and function … |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f4]] | `10.1111/pbi.14046` | protein interaction | PbrNSC was shown to bind to an auxin response factor, PbrARF13. |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f5]] | `10.1111/pbi.14046` | genetic perturbation | Overexpression of PbrARF13 decreased stone cell content in pear fruit and secondary cell wall (SCW) thickness in transge… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f6]] | `10.1111/pbi.14046` | genetic perturbation | As expected, overexpression or knockdown of PbrMYB132 increased or decreased stone cell content in pear fruit and SCW th… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f7]] | `10.1111/pbi.14046` | protein interaction | For example, SlARF6 regulates chlorophyll biosynthesis, photosynthesis, sugar accumulation and fruit development in toma… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f8]] | `10.1111/pbi.14046` | DNA binding/regulation | We showed that PbrARF13 directly binds to the promoter of PbrNSC, a key gene for lignin and cellulose biosynthesis in st… |
| [[b6-JtU6BLa8oL57zgnlWnzO_Q-f1]] | `10.1111/tpj.70902` | protein interaction | All these data imply that TCP21 directly interacts with phyB likely in a light-dependent manner. |
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

（另有 263 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 5 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| PIN1 | regulation direction dispute | [[daily-42243683]]；[[ms-10-3389_fpls-2026-1830107]]；[[ref-tpc-110-073924]] |
| BZR1 | regulation direction dispute | [[daily-42325906]]；[[daily-42665660]]；[[daily-42665660]] |
| PP2C | regulation direction dispute | [[daily-42423212]]；[[ref-mcz160]]；[[ref-s41477-025-01910-4]] |
| BIN2 | regulation direction dispute | [[daily-42665660]]；[[daily-42665660]]；[[daily-42665660]] |
| IAA9 | regulation direction dispute | [[ms-10-1007_s11295-026-01747-8]]；[[ms-10-3389_fpls-2026-1830107]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **862 条证据（65%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4595 个中文字符，行内证据链接 118 处，密度 **12.8 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
