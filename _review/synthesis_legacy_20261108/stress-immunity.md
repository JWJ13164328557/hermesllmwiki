---

title: "胁迫与免疫 — Synthesis"
created: 2026-06-01
total_evidence: 4774
total_papers: 961
library_papers: 1346  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-07
tags: [synthesis, stress, immunity, abiotic-stress, biotic-stress, hormone]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261107/stress-immunity.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 逆境与免疫 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 4774 | 本主题归属的证据对象数 |
| 独立论文 | 961 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.97 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 7% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(1365)、Solanum lycopersicum(869)、Zea mays(830)、Arabidopsis thaliana(828)、Triticum aestivum(777)、Nicotiana tabacum(619) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 3014；protein interaction 523；phenotypic/association 402；expression/regulation 341；genetic perturbation 293；omics/co-occurrence 119 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, lea |
| `daily-42729520-f4` | 10.3389/fpls.2026.1942553 | Our results indicate that GmSHMT05 sustains overall soybean growth and development in the  |
| `daily-42231161-f1` | 10.1186/s12870-026-09156-8 | Stable overexpression of PavNHX37 in Nicotiana benthamiana significantly improved salt tol |
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag dr |
| `daily-42357205-f7` | 10.3390/plants15121886 | Although the identified candidate genes provide solid genetic targets for salinity toleran |
| `daily-42588902-f1` | 10.3390/plants15152398 | In summary, STA1 (Category II) establishes a relatively complete chain from cold-induced e |
| `daily-42341170-f1` | 10.1093/plphys/kiag413 | In this study, we show that loss-of-function mutations in MLO2, MLO6, and MLO12 result in  |
| `daily-42204672-f5` | 10.1186/s12870-026-09089-2 | 1C), the changes in the scopoletin content of the four overexpression-positive lines were  |
| `daily-42319077-f1` | 10.1093/plcell/koag190 | Overexpression of the GhPsbO protein, driven by a constitutive promoter, significantly enh |
| `ms-10-1007_s00344-026-12266-0-f2` | 10.1007/s00344-026-12266-0 | While novel_47 (targeting the DNA repair gene BRCA2) was upregulated in both genotypes, it |
| `daily-41788331-f6` | 10.3389/fmicb.2026.1743670 | In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect  |
| `daily-42958739-f5` | 10.1111/tpj.71175 | When dipinoculated with Pst DC3000, the impa1 mutants exhibited increased susceptibility,  |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 293 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 523 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 82 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 341 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 402 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 119 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 3014 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, leading to th |
| `daily-42729520-f4` | 10.3389/fpls.2026.1942553 | Our results indicate that GmSHMT05 sustains overall soybean growth and development in the absence of |
| `daily-42231161-f1` | 10.1186/s12870-026-09156-8 | Stable overexpression of PavNHX37 in Nicotiana benthamiana significantly improved salt tolerance: tr |
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag driven by th |
| `daily-42357205-f7` | 10.3390/plants15121886 | Although the identified candidate genes provide solid genetic targets for salinity tolerance, furthe |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-07 由 `rebuild_synthesis_body.py` 从 **4774 条证据对象 / 961 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261107`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **4774 条证据 / 961 篇文献**。规则判定为因果或直接调控的 **880 条（18.4%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **408 条**。可判定程度最高的结论集中在CcLTCS、MdNAC29、SlUGT73C1：Simultaneous overexpression of CcNFYB3 and CcLTCS further increased Al resistance.（[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f5]]）；In apple, overexpression of MdNAC29 reduced drought tolerance in apple, callus, and tobacco plants, showing higher relative conductivity, MD…（[[daily-39819332-f3]]）；In tomato, overexpression of the tomato SlUGT73C1 gene in Arabidopsis increased the seed germination rate, increased SOD and POD activities,…（[[daily-39819332-f4]]）。研究重心位于“非生物逆境响应”（912 条证据，占 19%）。证据的物种分布以 Oryza sativa 为首（1365 条，29%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 4774 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 961 | 去重后的论文数 |
| 平均每篇证据数 | 4.97 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 7%（71/961） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(3032)、protein interaction(518)、phenotypic/association(402)、expression/regulation(341)、genetic perturbation(291)、omics/co-occurrence(119)、DNA binding/regulation(71) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | 未标(4770)、medium(3)、low(1) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(1365)、Solanum lycopersicum(869)、Zea mays(830)、Arabidopsis thaliana(828)、Triticum aestivum(777)、Nicotiana tabacum(619) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 3200（67%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **880 条**，占本主题证据的 **18.4%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 1365 条证据（29%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 219 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 病原识别与免疫受体

**规模** 242 条证据 / 147 篇文献；**构成** descriptive/observational(126)、protein interaction(61)、omics/co-occurrence(18)、expression/regulation(14)、genetic perturbation(13)、phenotypic/association(7)；**因果层** 77 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Arabidopsis thaliana，反复出现的实体为NLR8、NbTOL9a、auxin、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Etienne et al., 2023 [[cell-specialization-and-coordination-in-arabidopsis-leaves-upon-pathogenic-attac-f1]]；Etienne et al., 2023 [[cell-specialization-and-coordination-in-arabidopsis-leaves-upon-pathogenic-attac-f4]]；Etienne et al., 2023 [[cell-specialization-and-coordination-in-arabidopsis-leaves-upon-pathogenic-attac-f5]]）。
- **证据层级的张力**：77 条属于遗传扰动/蛋白互作/DNA 结合，165 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-40954952-f8]]；[[daily-41100018-f4]]；Etienne et al., 2023 [[cell-specialization-and-coordination-in-arabidopsis-leaves-upon-pathogenic-attac-f1]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-40954952-f8]]；[[daily-41100018-f4]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 2 | 18 | 2 | 3 | 4 | 8 | 35 | 72 |
| Solanum lycopersicum | 3 | 19 | 0 | 7 | 2 | 6 | 33 | 70 |
| Arabidopsis thaliana | 4 | 13 | 2 | 1 | 2 | 2 | 29 | 53 |
| Nicotiana tabacum | 4 | 10 | 0 | 4 | 3 | 7 | 24 | 52 |
| Triticum aestivum | 3 | 11 | 0 | 2 | 3 | 0 | 26 | 45 |

**基因实体（自动标注，前 5）**：NLR8(5)、NbTOL9a(4)、BAK1(4)、NtabCrRLK47(4)、CrRLK1L(3)（标注覆盖 104/242）。

**化合物实体（自动标注，前 5）**：auxin(4)、lignin(2)、phenylpropanoid(2)、ethylene(1)、brassinosteroid(1)（标注覆盖 10/242）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-40954952-f6]]。

**代表断言（原文摘录，未改写）**

- “By analyzing our previously reported SIEC-Arabidopsis interactome in more detail, we found that SIECs interact with more host proteins associated with abiotic stress compared with …” — [[daily-42710057-f1]]（`10.1093/plphys/kiag664`，protein interaction）
- “The first plant RCC1 member to be functionally characterized as a non-canonical photoreceptor was UV RESISTANCE LOCUS 8 ( UVR8 ) in Arabidopsis thaliana; upon UV-B absorption, UVR8…” — [[daily-42280745-f4]]（`10.3390/plants15111709`，protein interaction）
- “While novel_47 (targeting the DNA repair gene BRCA2) was upregulated in both genotypes, its silencing effect appeared specific to the sensitive cultivar, implying that Perola posse…” — [[ms-10-1007_s00344-026-12266-0-f2]]（`10.1007/s00344-026-12266-0`，genetic perturbation）

### 2.2 免疫信号传导与活性氧

**规模** 377 条证据 / 283 篇文献；**构成** descriptive/observational(250)、protein interaction(42)、phenotypic/association(32)、genetic perturbation(23)、expression/regulation(18)、omics/co-occurrence(9)；**因果层** 68 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Triticum aestivum，反复出现的实体为CmVQ23、SlERF26、sucrose、salicylic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f1]]；[[daily-39996429-f6]]；[[daily-40304972-f7]]）。
- **证据层级的张力**：68 条属于遗传扰动/蛋白互作/DNA 结合，309 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-41622404-f4]]；[[daily-41978356-f3]]；[[daily-42197717-f4]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-41622404-f4]]；[[daily-41978356-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 11 | 23 | 2 | 5 | 13 | 1 | 73 | 128 |
| Solanum lycopersicum | 4 | 11 | 0 | 5 | 8 | 2 | 46 | 76 |
| Triticum aestivum | 4 | 6 | 1 | 7 | 10 | 2 | 42 | 72 |
| Arabidopsis thaliana | 7 | 10 | 1 | 3 | 4 | 1 | 37 | 63 |
| Zea mays | 3 | 9 | 1 | 3 | 6 | 2 | 35 | 59 |

**基因实体（自动标注，前 5）**：CmVQ23(4)、SlERF26(3)、GhPPOs(2)、SbRBOHG(2)、TaMAP3K17(2)（标注覆盖 97/377）。

**化合物实体（自动标注，前 5）**：sucrose(17)、salicylic acid(9)、jasmonic acid(8)、lignin(5)、auxin(5)（标注覆盖 55/377）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42203758-f5]]。

**代表断言（原文摘录，未改写）**

- “In PFAS-contaminated systems, HAs may interact with PFAS through competing mechanisms: PFAS-DOM complexation can reduce the freely available fraction through hydrophobic and electr…” — [[daily-42483507-f2]]（`10.3389/fpls.2026.1791472`，protein interaction）
- “In parallel, CRISPR is pairing with single-cell/spatial readouts to make cause-and-effect tractable in native contexts: pooled editing and barcoded screening in Candida now resolve…” — [[daily-41788331-f6]]（`10.3389/fmicb.2026.1743670`，genetic perturbation）
- “In the cytosol, calcium-dependent effectors such as calcium-dependent protein kinases (CPKs), CBL-CIPK complexes, and MAPK cascades are activated and propagate signals to the nucle…” — [[ms-10-3389_fpls-2026-1810324-f6]]（`10.3389/fpls.2026.1810324`，protein interaction）

### 2.3 抗病基因与数量抗性

**规模** 44 条证据 / 31 篇文献；**构成** descriptive/observational(25)、phenotypic/association(8)、protein interaction(6)、genetic perturbation(4)、omics/co-occurrence(1)；**因果层** 10 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Triticum aestivum、Glycine max，反复出现的实体为RIN4、PdRPM1；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f4]]；[[daily-41829717-f1]]；[[daily-42110912-f5]]）。
- **证据层级的张力**：10 条属于遗传扰动/蛋白互作/DNA 结合，34 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42280680-f3]]；[[daily-42413037-f8]]；[[daily-42588787-f3]]）。
- **可检验缺口**：DNA 结合、表达相关在本组缺证据；在补齐这些设计前，RIN4、PdRPM1 与“抗病基因与数量抗性”的方向性关系应作为待检验命题（[[daily-39996429-f4]]；[[daily-41829717-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 0 | 1 | 1 | 1 | 6 | 9 |
| Triticum aestivum | 0 | 1 | 3 | 0 | 5 | 9 |
| Glycine max | 0 | 2 | 1 | 0 | 6 | 9 |
| Oryza sativa | 2 | 1 | 0 | 0 | 3 | 6 |
| Hordeum vulgare | 0 | 0 | 2 | 0 | 4 | 6 |

**基因实体（自动标注，前 5）**：RIN4(5)、PdRPM1(4)、RPS2(2)、RPM1(2)、PB1(2)（标注覆盖 13/44）。

**代表断言（原文摘录，未改写）**

- “This review details how resistance in plant pathogenic bacteria predominantly arises through horizontally acquired determinants such as strAB and aadA, as well as point mutations i…” — [[daily-42427100-f2]]（`10.1093/gbe/evag174`，genetic perturbation）
- “These QTLs may also interact with osmotic adjustment processes through osmolyte accumulation (discussed in ), representing key genomic targets for drought-tolerant crop development…” — [[daily-42278532-f2]]（`10.3390/ijms27115008`，protein interaction）
- “Given that the PB1 domain mediates PB1dependent protein–protein interactions, we hypothesised that poplar encodes one or more proteins that interact with PdRPM1 via this domain.” — [[daily-42649622-f8]]（`10.1111/mpp.70329`，protein interaction）

### 2.4 非生物逆境响应

**规模** 912 条证据 / 380 篇文献；**构成** descriptive/observational(409)、phenotypic/association(216)、genetic perturbation(117)、expression/regulation(71)、protein interaction(70)、omics/co-occurrence(18)；**因果层** 198 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Zea mays，反复出现的实体为NaCl、SnRK2、melatonin、chlorophyll；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[banana-manac1-activates-secondary-cell-wall-f6]]；[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3]]；[[daily-39819332-f2]]）。
- **证据层级的张力**：198 条属于遗传扰动/蛋白互作/DNA 结合，714 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[banana-manac1-activates-secondary-cell-wall-f6]]；[[daily-39819332-f3]]；[[daily-41589633-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[banana-manac1-activates-secondary-cell-wall-f6]]；[[daily-39819332-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 40 | 39 | 6 | 24 | 68 | 6 | 126 | 309 |
| Triticum aestivum | 16 | 18 | 2 | 16 | 50 | 8 | 111 | 221 |
| Zea mays | 26 | 21 | 5 | 17 | 35 | 4 | 96 | 204 |
| Arabidopsis thaliana | 31 | 14 | 4 | 20 | 29 | 3 | 76 | 177 |
| Solanum lycopersicum | 23 | 8 | 3 | 20 | 43 | 2 | 59 | 158 |

**基因实体（自动标注，前 5）**：NaCl(10)、SnRK2(6)、CaAAP6(5)、TaCOMT1A(5)、ZmSWEET11(4)（标注覆盖 334/912）。

**化合物实体（自动标注，前 5）**：melatonin(14)、chlorophyll(12)、phenylpropanoid(7)、lignin(6)、auxin(6)（标注覆盖 72/912）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ref-pcu020-f4]]。

**代表断言（原文摘录，未改写）**

- “Studies have found that Aux/IAA proteins not only indirectly influence ABA signal transduction by regulating auxin and ABA biosynthesis/metabolic pathways but also that some member…” — [[daily-42245099-f7]]（`10.3389/fpls.2026.1823723`，protein interaction）
- “Stable overexpression of PavNHX37 in Nicotiana benthamiana significantly improved salt tolerance: transgenic lines exhibited lower Na + accumulation, higher K + retention, and a re…” — [[daily-42231161-f1]]（`10.1186/s12870-026-09156-8`，genetic perturbation）
- “Although the identified candidate genes provide solid genetic targets for salinity tolerance, further downstream functional validation, including qRT-PCR expression profiling, VIGS…” — [[daily-42357205-f7]]（`10.3390/plants15121886`，genetic perturbation）

### 2.5 激素与免疫的权衡

**规模** 59 条证据 / 48 篇文献；**构成** descriptive/observational(51)、phenotypic/association(4)、protein interaction(1)、omics/co-occurrence(1)、genetic perturbation(1)、expression/regulation(1)；**因果层** 2 条（可支撑有限机制表述）。

> 本组仅 2 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 57 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Triticum aestivum、Oryza sativa、Solanum lycopersicum，反复出现的实体为DRM2、RdDM、phenolic、salicylic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42122860-f1]]；[[daily-42122860-f8]]；[[daily-42122890-f3]]）。
- **证据层级的张力**：2 条属于遗传扰动/蛋白互作/DNA 结合，57 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42514492-f6]]）。
- **可检验缺口**：DNA 结合在本组缺证据；在补齐这些设计前，DRM2、RdDM、phenolic 与“激素与免疫的权衡”的方向性关系应作为待检验命题（[[daily-42122860-f1]]；[[daily-42122860-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Triticum aestivum | 0 | 0 | 0 | 1 | 1 | 17 | 19 |
| Oryza sativa | 0 | 0 | 0 | 2 | 0 | 17 | 19 |
| Solanum lycopersicum | 0 | 0 | 0 | 1 | 0 | 11 | 12 |
| Rosa spp. | 0 | 0 | 0 | 0 | 0 | 8 | 8 |
| Nicotiana tabacum | 0 | 0 | 0 | 0 | 0 | 6 | 6 |

**基因实体（自动标注，前 5）**：DRM2(1)、RdDM(1)、PsnSAUR6(1)、SNF1(1)、SnRK1(1)（标注覆盖 10/59）。

**化合物实体（自动标注，前 5）**：phenolic(2)、salicylic acid(2)、auxin(1)、brassinosteroid(1)、phenylpropanoid(1)（标注覆盖 7/59）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42689114-f6]]。

**代表断言（原文摘录，未改写）**

- “Our results indicate that GmSHMT05 sustains overall soybean growth and development in the absence of GmSHMT08; however, GmSHMT08’s gain-of-function in SCN resistance negatively inf…” — [[daily-42729520-f4]]（`10.3389/fpls.2026.1942553`，genetic perturbation）
- “This is due to the fact that different priming agents affect the physiological and biochemical traits in plants differently due to the unique ways they interact with the plant’s ce…” — [[daily-42280673-f5]]（`10.3390/plants15111636`，protein interaction）
- “Thermopriming differentially regulates a defined set of microRNAs including osa-miR156b-3p, osa-miR167e-3p, osa-miR168a-5p, osa-miR531b, osa-miR1846d-5p, osa-miR5077, and osa-miR51…” — [[daily-42689139-f2]]（`10.3389/fpls.2026.1924558`，descriptive/observational）

### 2.6 微生物组与根际互作

**规模** 111 条证据 / 65 篇文献；**构成** descriptive/observational(89)、phenotypic/association(10)、protein interaction(5)、expression/regulation(4)、DNA binding/regulation(1)、omics/co-occurrence(1)；**因果层** 7 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Zea mays、Solanum lycopersicum，反复出现的实体为NtabCrRLK47、MAX3、melatonin、jasmonic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41375325-f6]]；[[daily-41589633-f1]]；[[daily-41645062-f1]]）。
- **证据层级的张力**：7 条属于遗传扰动/蛋白互作/DNA 结合，104 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42122860-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 0 | 3 | 0 | 0 | 3 | 0 | 26 | 32 |
| Zea mays | 0 | 3 | 0 | 1 | 1 | 0 | 22 | 27 |
| Solanum lycopersicum | 0 | 1 | 0 | 0 | 0 | 0 | 21 | 22 |
| Nicotiana tabacum | 1 | 0 | 0 | 0 | 0 | 0 | 15 | 16 |
| Glycine max | 0 | 0 | 0 | 0 | 1 | 0 | 14 | 15 |

**基因实体（自动标注，前 5）**：NtabCrRLK47(3)、MAX3(2)、GXD2(1)、NSP2(1)、CELK12(1)（标注覆盖 11/111）。

**化合物实体（自动标注，前 5）**：melatonin(3)、jasmonic acid(1)、phenolic(1)、salicylic acid(1)（标注覆盖 6/111）。

**代表断言（原文摘录，未改写）**

- “By delivering hydrolytic enzymes, antimicrobial effectors, signaling molecules, and immunomodulatory proteins, SSs enable bioagents not only to suppress pathogens directly, but als…” — [[daily-42437521-f8]]（`10.1002/bit.70303`，protein interaction）
- “Recent studies suggest that melatonin not only directly regulates plant stress physiology but may also enhance drought tolerance by reshaping the structure and function of rhizosph…” — [[daily-42249284-f4]]（`10.1186/s12870-026-09179-1`，DNA binding/regulation）
- “Specifically, we show that the mutation of NtabCrRLK47 leads to significant alterations in plant growth, including enhanced plant height, root length, leaf area, and an enriched mi…” — [[daily-42491367-f2]]（`10.3389/fpls.2026.1864982`，genetic perturbation）

### 2.7 逆境记忆与表观调控

**规模** 72 条证据 / 40 篇文献；**构成** descriptive/observational(53)、protein interaction(7)、phenotypic/association(5)、expression/regulation(3)、DNA binding/regulation(2)、genetic perturbation(1)；**因果层** 10 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Arabidopsis thaliana，反复出现的实体为ALKBH5、RdDM、phenolic、abscisic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41494571-f6]]；[[daily-42122860-f1]]；[[daily-42122860-f2]]）。
- **证据层级的张力**：10 条属于遗传扰动/蛋白互作/DNA 结合，62 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-41494571-f6]]；[[daily-42227011-f3]]；[[daily-42412868-f3]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-41494571-f6]]；[[daily-42227011-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 0 | 2 | 1 | 1 | 2 | 1 | 19 | 26 |
| Triticum aestivum | 1 | 3 | 0 | 1 | 1 | 1 | 17 | 24 |
| Arabidopsis thaliana | 0 | 4 | 1 | 2 | 2 | 0 | 11 | 20 |
| Hordeum vulgare | 0 | 0 | 1 | 0 | 0 | 0 | 8 | 9 |
| Rosa spp. | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 9 |

**基因实体（自动标注，前 5）**：ALKBH5(3)、RdDM(2)、LSD1(2)、HD2B(2)、HSP70(1)（标注覆盖 15/72）。

**化合物实体（自动标注，前 5）**：phenolic(1)、abscisic acid(1)（标注覆盖 2/72）。

**代表断言（原文摘录，未改写）**

- “In the sdg8 mutant, the levels of H3K36me2/me3 on the chromatin of target genes such as FLC, MAF4, and MAF5 significantly decreased, whereas H3K36me1 significantly increased, resul…” — [[daily-42227011-f3]]（`10.1093/hr/uhag047`，genetic perturbation）
- “Chromatin immunoprecipitation assays can identify the transcription factors that bind to the ABRE motifs in the promoters of LbaSOD5 and LbaSOD10, whereas promoter deletion and mut…” — [[daily-42725159-f6]]（`10.3389/fpls.2026.1897912`，DNA binding/regulation）
- “We show that MPK3 interacts directly with and phosphorylates the histone deacetylase HD2B, which has been shown to deacetylate the lysine 9 residue of histone 3 (H3K9), a modificat…” — [[ref-s13059-017-1261-8-f1]]（`10.1186/s13059-017-1261-8`，protein interaction）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| CmVQ23 | 4 | 7 | 免疫信号传导与活性氧、抗病基因与数量抗性、激素与免疫的权衡、病原识别与免疫受体 |
| SnRK2 | 3 | 8 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| BAK1 | 3 | 6 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| LpCbDR1 | 3 | 6 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| MAC5A | 3 | 6 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| SbRBOHG | 3 | 5 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| StuPPO9 | 3 | 5 | 免疫信号传导与活性氧、激素与免疫的权衡、非生物逆境响应 |
| COOL1 | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| HD2B | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、逆境记忆与表观调控 |
| LpERF1B | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| phenolic | 5 | 10 | 免疫信号传导与活性氧、微生物组与根际互作、激素与免疫的权衡、逆境记忆与表观调控、非生物逆境响应 |
| auxin | 4 | 16 | 免疫信号传导与活性氧、激素与免疫的权衡、病原识别与免疫受体、非生物逆境响应 |
| salicylic acid | 4 | 13 | 免疫信号传导与活性氧、微生物组与根际互作、激素与免疫的权衡、病原识别与免疫受体 |
| phenylpropanoid | 4 | 12 | 免疫信号传导与活性氧、激素与免疫的权衡、病原识别与免疫受体、非生物逆境响应 |
| jasmonic acid | 4 | 11 | 免疫信号传导与活性氧、微生物组与根际互作、激素与免疫的权衡、非生物逆境响应 |
| abscisic acid | 4 | 8 | 免疫信号传导与活性氧、激素与免疫的权衡、逆境记忆与表观调控、非生物逆境响应 |

### 3.1 跨子主题受控叙述

- **交叉实体**：CmVQ23、SnRK2、BAK1、LpCbDR1、MAC5A 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[accumulation-of-tocopherols-and-transcriptional-regulation-f3]]；[[banana-manac1-activates-secondary-cell-wall-f1]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“非生物逆境响应”（198 条），最低为“激素与免疫的权衡”（2 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 病原识别与免疫受体 | 13 | 61 | 3 | 14 | 7 | 18 | 126 |
| 免疫信号传导与活性氧 | 23 | 42 | 3 | 18 | 32 | 9 | 250 |
| 抗病基因与数量抗性 | 4 | 6 | — | — | 8 | 1 | 25 |
| 非生物逆境响应 | 117 | 70 | 11 | 71 | 216 | 18 | 409 |
| 激素与免疫的权衡 | 1 | 1 | — | 1 | 4 | 1 | 51 |
| 微生物组与根际互作 | 1 | 5 | 1 | 4 | 10 | 1 | 89 |
| 逆境记忆与表观调控 | 1 | 7 | 2 | 3 | 5 | 1 | 53 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 880 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[banana-manac1-activates-secondary-cell-wall-f6]] | `10.1111/pbi.14195` | protein interaction | The interaction between a NAC domain TF Vascular-Related NAC-Domain7 (VND7) and a VND Interacting 2 (VNI2) TF contribute… |
| [[banana-manac1-activates-secondary-cell-wall-f7]] | `10.1111/pbi.14195` | protein interaction | The expression of Ma06_g28730 in postharvest banana peel was obviously upregulated under chilling stress (Figure 2d), an… |
| [[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3]] | `10.1111/pbi.14179` | genetic perturbation | In our experiments, we found the double RNAi line exhibited a further increase in callose concentration and a decrease i… |
| [[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f5]] | `10.1111/pbi.14179` | genetic perturbation | Simultaneous overexpression of CcNFYB3 and CcLTCS further increased Al resistance. |
| [[daily-39819332-f3]] | `10.1080/21645698.2024.2448869` | genetic perturbation | In apple, overexpression of MdNAC29 reduced drought tolerance in apple, callus, and tobacco plants, showing higher relat… |
| [[daily-39819332-f4]] | `10.1080/21645698.2024.2448869` | genetic perturbation | In tomato, overexpression of the tomato SlUGT73C1 gene in Arabidopsis increased the seed germination rate, increased SOD… |
| [[daily-39819332-f5]] | `10.1080/21645698.2024.2448869` | genetic perturbation | For example, the overexpression of MdABI5 enhanced ABA sensitivity and drought tolerance by directly activating the expr… |
| [[daily-39996429-f1]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Our findings suggest that the enhanced immunity observed in Arabidopsis cds1cds2 mutant was attributable to multiple fac… |
| [[daily-39996429-f2]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Here, we found that knock-down of the CDS gene enhanced the resistance of Arabidopsis thaliana to multiple pathogens, wi… |
| [[daily-39996429-f3]] | `10.1080/15592324.2025.2471503` | genetic perturbation | Our data suggest that AtS40, NGAL2, RGL3, and other genes associated with embryonic development and growth in plants wer… |
| [[daily-39996429-f5]] | `10.1080/15592324.2025.2471503` | protein interaction | In plants, PA interacts with proteins that function in or outside cell nucleus to regulate cellular and physiological pr… |
| [[daily-39996429-f6]] | `10.1080/15592324.2025.2471503` | protein interaction | PA binds to respiratory burst oxidase homolog D (RBOHD), which generates reactive oxygen species (ROS) in plant immunity… |
| [[daily-40304972-f3]] | `10.1007/s13353-025-00963-7` | protein interaction | In animals, GPCR interacts with a G-protein composed of Gα and a Gβγ dimer, with Gα bound to guanosine diphosphate (GDP)… |
| [[daily-40304972-f4]] | `10.1007/s13353-025-00963-7` | protein interaction | The dissociated Gα and Gβγ dimer then interact with various intracellular effectors, such as transcription factors and e… |
| [[daily-40304972-f6]] | `10.1007/s13353-025-00963-7` | protein interaction | Upon activation, the final kinase translocates within the cell to phosphorylate various targets, including transcription… |
| [[daily-40304972-f8]] | `10.1007/s13353-025-00963-7` | protein interaction | At higher concentrations, melatonin interacts with calmodulin, inhibiting NOS activity and reducing NO production in mit… |
| [[daily-40455831-f2]] | `10.1146/annurev-phyto-121823-032335` | genetic perturbation | Similarly, overexpression of the ECT homolog in apple, MhYTP2, enhances the translation efficiency of its target transcr… |
| [[daily-40455831-f4]] | `10.1146/annurev-phyto-121823-032335` | protein interaction | One notable example of IRES-dependent translation involves the AtLa1 protein, which binds to the 5′ LS of WUSCHEL (WUS) … |
| [[daily-40455831-f7]] | `10.1146/annurev-phyto-121823-032335` | protein interaction | COP1 binds to and ubiquitinates the spliceosome component DOMINANT COP1-6 SUPPRESSOR 1 (DCS1) to control intron retentio… |
| [[daily-40893112-f4]] | `10.1080/21645698.2025.2555037` | genetic perturbation | Reported that overexpression of the NsVP1 gene from Nitraria sibirica, significantly enhanced salt tolerance in Arabidop… |

（另有 860 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 1 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| SOS2 | regulation direction dispute | [[daily-42232517]]；[[daily-42284136]]；[[ms-10-21926_obm-genet-2603356]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **3200 条证据（67%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261107`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4600 个中文字符，行内证据链接 103 处，密度 **11.2 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
