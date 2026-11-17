---

title: "胁迫与免疫 — Synthesis"
created: 2026-06-01
total_evidence: 5647
total_papers: 977
library_papers: 1346  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, stress, immunity, abiotic-stress, biotic-stress, hormone]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261103/stress-immunity.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 逆境与免疫 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 5647 | 本主题归属的证据对象数 |
| 独立论文 | 977 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 5.78 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 4% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Oryza sativa(1619)、Zea mays(1010)、Solanum lycopersicum(1007)、Arabidopsis thaliana(980)、Triticum aestivum(946)、Nicotiana tabacum(727) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 3469；expression/regulation 630；protein interaction 584；phenotypic/association 447；genetic perturbation 305；omics/co-occurrence 137 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, lea |
| `daily-42729520-f4` | 10.3389/fpls.2026.1942553 | Our results indicate that GmSHMT05 sustains overall soybean growth and development in the  |
| `daily-42231161-f1` | 10.1186/s12870-026-09156-8 | Stable overexpression of PavNHX37 in Nicotiana benthamiana significantly improved salt tol |
| `daily-42644387-f7` | 10.1093/nar/gkag849 | Beyond CRISPR-Cas9, the prototypical module of the CRISPR system known for target gene rec |
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag dr |
| `daily-42357205-f7` | 10.3390/plants15121886 | Although the identified candidate genes provide solid genetic targets for salinity toleran |
| `daily-42588902-f1` | 10.3390/plants15152398 | In summary, STA1 (Category II) establishes a relatively complete chain from cold-induced e |
| `daily-42683150-f1` | 10.1093/hr/uhag166 | Overexpression of the candidate gene Psat4g213640 CW9-8 in the hairy root system significa |
| `daily-42341170-f1` | 10.1093/plphys/kiag413 | In this study, we show that loss-of-function mutations in MLO2, MLO6, and MLO12 result in  |
| `daily-42204672-f5` | 10.1186/s12870-026-09089-2 | 1C), the changes in the scopoletin content of the four overexpression-positive lines were  |
| `daily-42319077-f1` | 10.1093/plcell/koag190 | Overexpression of the GhPsbO protein, driven by a constitutive promoter, significantly enh |
| `ms-10-1007_s00344-026-12266-0-f2` | 10.1007/s00344-026-12266-0 | While novel_47 (targeting the DNA repair gene BRCA2) was upregulated in both genotypes, it |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 305 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 584 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 75 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 630 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 447 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 137 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 3469 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42410657-f1` | 10.1186/s43897-026-00238-7 | Transgenic plants expressing miR858 target mimics effectively blocked miR858 activity, leading to th |
| `daily-42729520-f4` | 10.3389/fpls.2026.1942553 | Our results indicate that GmSHMT05 sustains overall soybean growth and development in the absence of |
| `daily-42231161-f1` | 10.1186/s12870-026-09156-8 | Stable overexpression of PavNHX37 in Nicotiana benthamiana significantly improved salt tolerance: tr |
| `daily-42644387-f7` | 10.1093/nar/gkag849 | Beyond CRISPR-Cas9, the prototypical module of the CRISPR system known for target gene recognition,  |
| `daily-42228685-f1` | 10.1371/journal.pbio.3003811 | When we introduced intact or mutated HIPP19 at the miR408-5p target site with a GFP tag driven by th |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **2954 条证据对象 / 555 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **2954 条证据 / 555 篇文献**。规则判定为因果或直接调控的 **493 条（16.7%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **224 条**。可判定程度最高的结论集中在CcLTCS、MdNAC29、SlUGT73C1：Simultaneous overexpression of CcNFYB3 and CcLTCS further increased Al resistance.（[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f5]]）；In apple, overexpression of MdNAC29 reduced drought tolerance in apple, callus, and tobacco plants, showing higher relative conductivity, MD…（[[daily-39819332-f3]]）；In tomato, overexpression of the tomato SlUGT73C1 gene in Arabidopsis increased the seed germination rate, increased SOD and POD activities,…（[[daily-39819332-f4]]）。研究重心位于“非生物逆境响应”（651 条证据，占 22%）。证据的物种分布以 Oryza sativa 为首（1119 条，38%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 2954 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 555 | 去重后的论文数 |
| 平均每篇证据数 | 5.32 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 9%（48/555） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(2050)、expression/regulation(331)、protein interaction(321)、genetic perturbation(129)、omics/co-occurrence(56)、DNA binding/regulation(43)、phenotypic/association(24) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(2263)、medium(549)、high(142) | 低置信度标注须回原文核对 |
| 主要物种 | Oryza sativa(1119)、Zea mays(751)、Arabidopsis thaliana(719)、Solanum lycopersicum(711)、Triticum aestivum(701)、Nicotiana tabacum(502) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 1902（64%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **493 条**，占本主题证据的 **16.7%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Oryza sativa** 出现在 1119 条证据（38%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 145 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 病原识别与免疫受体

**规模** 148 条证据 / 86 篇文献；**构成** descriptive/observational(77)、protein interaction(37)、expression/regulation(19)、omics/co-occurrence(6)、genetic perturbation(5)、phenotypic/association(2)；**因果层** 44 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Solanum lycopersicum、Arabidopsis thaliana，反复出现的实体为NLR8、NbTOL9a、lignin、phenolic；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f3]]；[[daily-39996429-f6]]；[[daily-40898604-f8]]）。
- **证据层级的张力**：44 条属于遗传扰动/蛋白互作/DNA 结合，104 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42247512-f1]]；[[daily-42247512-f2]]；[[daily-40904198-f7]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-42247512-f1]]；[[daily-42247512-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 3 | 16 | 2 | 8 | 2 | 3 | 23 | 57 |
| Solanum lycopersicum | 0 | 13 | 0 | 5 | 1 | 2 | 29 | 50 |
| Arabidopsis thaliana | 2 | 13 | 2 | 4 | 1 | 3 | 23 | 48 |
| Zea mays | 1 | 11 | 2 | 2 | 0 | 3 | 26 | 45 |
| Nicotiana tabacum | 0 | 9 | 0 | 5 | 2 | 1 | 22 | 39 |

**基因实体（自动标注，前 5）**：NLR8(6)、NbTOL9a(4)、NtabCrRLK47(4)、NLRP3(3)、CrRLK1L(2)（标注覆盖 66/148）。

**化合物实体（自动标注，前 5）**：lignin(1)、phenolic(1)、salicylic acid(1)、phenylpropanoid(1)、abscisic acid(1)（标注覆盖 5/148）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42712539-f4]]。

**代表断言（原文摘录，未改写）**

- “In the cytosol, calcium-dependent effectors such as calcium-dependent protein kinases (CPKs), CBL-CIPK complexes, and MAPK cascades are activated and propagate signals to the nucle…” — [[ms-10-3389_fpls-2026-1810324-f6]]（`10.3389/fpls.2026.1810324`，protein interaction）
- “By delivering hydrolytic enzymes, antimicrobial effectors, signaling molecules, and immunomodulatory proteins, SSs enable bioagents not only to suppress pathogens directly, but als…” — [[daily-42437521-f8]]（`10.1002/bit.70303`，protein interaction）
- “Wheat evidence does support its functional relevance: manipulation of ABA receptor signaling in wheat can improve water-use efficiency and overexpression of an ABA receptor increas…” — [[daily-42423212-f4]]（`10.1080/15592324.2026.2700909`，genetic perturbation）

### 2.2 免疫信号传导与活性氧

**规模** 243 条证据 / 179 篇文献；**构成** descriptive/observational(159)、protein interaction(35)、expression/regulation(29)、genetic perturbation(13)、omics/co-occurrence(5)、phenotypic/association(1)；**因果层** 49 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Solanum lycopersicum，反复出现的实体为SlERF26、MPK3、salicylic acid、jasmonic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f1]]；[[daily-39996429-f6]]；[[daily-40898604-f2]]）。
- **证据层级的张力**：49 条属于遗传扰动/蛋白互作/DNA 结合，194 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-41622404-f4]]；[[daily-42046478-f1]]；[[daily-40904198-f8]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[daily-41622404-f4]]；[[daily-42046478-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 8 | 21 | 1 | 13 | 1 | 0 | 64 | 108 |
| Triticum aestivum | 3 | 12 | 0 | 11 | 0 | 2 | 45 | 73 |
| Solanum lycopersicum | 4 | 15 | 0 | 6 | 0 | 1 | 44 | 70 |
| Zea mays | 5 | 9 | 1 | 9 | 0 | 1 | 40 | 65 |
| Arabidopsis thaliana | 4 | 10 | 1 | 7 | 0 | 1 | 29 | 52 |

**基因实体（自动标注，前 5）**：SlERF26(3)、MPK3(3)、TaMAP3K17(2)、LpCbDR1(2)、NPR1(2)（标注覆盖 53/243）。

**化合物实体（自动标注，前 5）**：salicylic acid(7)、jasmonic acid(6)、sucrose(5)、auxin(4)、ethylene(4)（标注覆盖 32/243）。

**标注一致性提示**：本组 2 条证据标注为描述性，但断言含扰动/互作措辞（DNA binding/regulation、genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42203758-f5]]。

**代表断言（原文摘录，未改写）**

- “In PFAS-contaminated systems, HAs may interact with PFAS through competing mechanisms: PFAS-DOM complexation can reduce the freely available fraction through hydrophobic and electr…” — [[daily-42483507-f2]]（`10.3389/fpls.2026.1791472`，protein interaction）
- “ABA promotes leaf senescence through a pathway distinct from ethylene signaling: activated SnRK2s phosphorylate not only ABFs (ABA RESPONSIVE ELEMENT-BINDING FACTORs) but also RAV1…” — [[ms-10-1186_s43897-026-00236-9-f6]]（`10.1186/s43897-026-00236-9`，protein interaction）
- “We propose that SbIMP-4 represents a prime target for functional validation through CRISPR/Cas9-mediated knockout, transgenic overexpression, or base editing approaches (Peng et al…” — [[ms-10-3389_fpls-2026-1941259-f7]]（`10.3389/fpls.2026.1941259`，genetic perturbation）

### 2.3 抗病基因与数量抗性

**规模** 25 条证据 / 17 篇文献；**构成** descriptive/observational(15)、phenotypic/association(4)、expression/regulation(3)、protein interaction(3)；**因果层** 3 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Glycine max、Brassica napus，反复出现的实体为RIN4、RPS2；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-39996429-f4]]；[[daily-42245095-f5]]；[[daily-42267126-f8]]）。
- **证据层级的张力**：3 条属于遗传扰动/蛋白互作/DNA 结合，22 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42413037-f1]]；[[daily-42413037-f8]]；[[daily-42245095-f5]]）。
- **可检验缺口**：遗传扰动、DNA 结合、组学共现在本组缺证据；在补齐这些设计前，RIN4、RPS2 与“抗病基因与数量抗性”的方向性关系应作为待检验命题（[[daily-39996429-f4]]；[[daily-42245095-f5]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 表型关联 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 0 | 2 | 7 | 12 |
| Glycine max | 2 | 0 | 1 | 6 | 9 |
| Brassica napus | 2 | 0 | 1 | 4 | 7 |
| Triticum aestivum | 0 | 1 | 0 | 4 | 5 |
| Hordeum vulgare | 1 | 0 | 1 | 3 | 5 |

**基因实体（自动标注，前 5）**：RIN4(5)、RPS2(4)、RPM1(2)、ACP2(1)、ACP3(1)（标注覆盖 10/25）。

**代表断言（原文摘录，未改写）**

- “NDR1 recruits ACP2 to the proximity of RPS2, and compatibility between ACP2 and ACP3 is required for ACP2 to overcome suppression by ACP3, indicating that ACP2 likely interacts wit…” — [[daily-42413037-f1]]（`10.1093/plcell/koag204`，protein interaction）
- “Plant J 48: 138–152 Takahashi A, Casais AC, Ichimura K, Shirasu K (2003) HSP90 interacts with RAR1 and SGT1 and is essential for RPS2-mediated disease resistance in Arabidopsis.” — [[pdf-pp-107-111740-f2]]（`10.1104/pp.107.111740`，protein interaction）
- “Previous studies have shown that purine biosynthesis is required for immune effector programs, including T-cell functional states, supporting an association between PRPS1-related p…” — [[ms-10-1038_s41598-026-67627-2-f5]]（`10.1038/s41598-026-67627-2`，expression/regulation）

### 2.4 非生物逆境响应

**规模** 651 条证据 / 250 篇文献；**构成** descriptive/observational(431)、expression/regulation(74)、genetic perturbation(65)、protein interaction(53)、omics/co-occurrence(13)、phenotypic/association(8)；**因果层** 125 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Zea mays，反复出现的实体为NaCl、CaAAP6、melatonin、chlorophyll；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[accumulation-of-tocopherols-and-transcriptional-regulation-f1]]；[[banana-manac1-activates-secondary-cell-wall-f6]]；[[ccnfyb3ccmate35-and-lncrna-ccltcscccs-modules-jointly-f3]]）。
- **证据层级的张力**：125 条属于遗传扰动/蛋白互作/DNA 结合，526 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[banana-manac1-activates-secondary-cell-wall-f6]]；[[daily-39819332-f3]]；[[daily-40904198-f1]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[banana-manac1-activates-secondary-cell-wall-f6]]；[[daily-39819332-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Oryza sativa | 25 | 30 | 3 | 33 | 7 | 3 | 162 | 263 |
| Triticum aestivum | 11 | 14 | 1 | 21 | 1 | 8 | 129 | 185 |
| Zea mays | 17 | 15 | 3 | 20 | 3 | 1 | 111 | 170 |
| Arabidopsis thaliana | 23 | 12 | 2 | 19 | 1 | 2 | 87 | 146 |
| Solanum lycopersicum | 13 | 8 | 2 | 24 | 2 | 2 | 94 | 145 |

**基因实体（自动标注，前 5）**：NaCl(7)、CaAAP6(5)、TaCOMT1A(5)、CsBT2(4)、SnRK2(4)（标注覆盖 220/651）。

**化合物实体（自动标注，前 5）**：melatonin(12)、chlorophyll(9)、phenylpropanoid(7)、lignin(5)、abscisic acid(5)（标注覆盖 55/651）。

**标注一致性提示**：本组 3 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-40893112-f3]]。

**代表断言（原文摘录，未改写）**

- “Studies have found that Aux/IAA proteins not only indirectly influence ABA signal transduction by regulating auxin and ABA biosynthesis/metabolic pathways but also that some member…” — [[daily-42245099-f7]]（`10.3389/fpls.2026.1823723`，protein interaction）
- “Although the identified candidate genes provide solid genetic targets for salinity tolerance, further downstream functional validation, including qRT-PCR expression profiling, VIGS…” — [[daily-42357205-f7]]（`10.3390/plants15121886`，genetic perturbation）
- “We then obtained HDT4 T-DNA insertion line (hdt4-1) and explored its drought phenotype (S5B–S5D Fig) Fig We found that hdt4-1 was more drought tolerant than Col-0 (Fig 5D), and HDT…” — [[ref-journal-pgen-1010473-f7]]（`10.1371/journal.pgen.1010473`，genetic perturbation）

### 2.5 激素与免疫的权衡

**规模** 28 条证据 / 18 篇文献；**构成** descriptive/observational(25)、protein interaction(1)、omics/co-occurrence(1)、expression/regulation(1)；**因果层** 1 条（可支撑有限机制表述）。

> 本组仅 1 条因果级证据，机制表述只在该证据覆盖的物种与条件下成立，不可外推到其余 27 条。

**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Triticum aestivum、Oryza sativa、Rosa spp.，反复出现的实体为PsnSAUR6、PR1、auxin、phenolic；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42122890-f3]]；[[daily-42122890-f6]]；[[daily-42268341-f2]]）。
- **证据层级的张力**：1 条属于遗传扰动/蛋白互作/DNA 结合，27 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42514492-f6]]）。
- **可检验缺口**：遗传扰动、DNA 结合、表型关联在本组缺证据；在补齐这些设计前，PsnSAUR6、PR1、auxin 与“激素与免疫的权衡”的方向性关系应作为待检验命题（[[daily-42122890-f3]]；[[daily-42122890-f6]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|
| Triticum aestivum | 1 | 0 | 1 | 11 | 13 |
| Oryza sativa | 0 | 0 | 0 | 12 | 12 |
| Rosa spp. | 0 | 0 | 0 | 8 | 8 |
| Solanum lycopersicum | 1 | 0 | 0 | 7 | 8 |
| Nicotiana tabacum | 0 | 0 | 0 | 3 | 3 |

**基因实体（自动标注，前 5）**：PsnSAUR6(1)、PR1(1)、PR3(1)、PR5(1)、NPR1(1)（标注覆盖 6/28）。

**化合物实体（自动标注，前 5）**：auxin(1)、phenolic(1)（标注覆盖 2/28）。

**代表断言（原文摘录，未改写）**

- “MT has been increasingly recognised as an integrative regulator of root system architecture through crosstalk with phytohormones, ROS and stress-responsive signalling pathways [, ]…” — [[daily-42410340-f2]]（`10.1186/s12870-026-09436-3`，protein interaction）
- “While our observations are consistent with the growth-defense tradeoff hypothesis, direct experimental validation—such as carbon/nitrogen partitioning analysis, stable isotope trac…” — [[daily-42514492-f6]]（`10.3390/plants15142124`，omics/co-occurrence）
- “Collectively, these findings demonstrate that both hostand virus-encoded circRNAs are induced following VSV infection and uncover a previously uncharacterized layer of virushost cr…” — [[daily-42482987-f7]]（`10.3389/fcimb.2026.1881266`，descriptive/observational）

### 2.6 微生物组与根际互作

**规模** 75 条证据 / 38 篇文献；**构成** descriptive/observational(59)、protein interaction(6)、expression/regulation(6)、DNA binding/regulation(1)、phenotypic/association(1)、omics/co-occurrence(1)；**因果层** 8 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Zea mays、Oryza sativa、Arabidopsis thaliana，反复出现的实体为NtabCrRLK47、ZT13、melatonin、jasmonic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-41589633-f1]]；[[daily-42249284-f2]]；[[daily-42249284-f4]]）。
- **证据层级的张力**：8 条属于遗传扰动/蛋白互作/DNA 结合，67 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（；[[daily-42436619-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Zea mays | 1 | 4 | 0 | 4 | 0 | 0 | 20 | 29 |
| Oryza sativa | 1 | 2 | 0 | 4 | 1 | 0 | 19 | 27 |
| Arabidopsis thaliana | 0 | 1 | 0 | 4 | 0 | 0 | 14 | 19 |
| Solanum lycopersicum | 1 | 1 | 0 | 1 | 0 | 0 | 15 | 18 |
| Nicotiana tabacum | 0 | 0 | 0 | 1 | 0 | 0 | 15 | 16 |

**基因实体（自动标注，前 5）**：NtabCrRLK47(3)、ZT13(2)、MAX3(2)、SynBio(1)、ZT1(1)（标注覆盖 9/75）。

**化合物实体（自动标注，前 5）**：melatonin(3)、jasmonic acid(1)、salicylic acid(1)（标注覆盖 5/75）。

**代表断言（原文摘录，未改写）**

- “Simi larly, biotechnological approaches that target the endo symbiont Buchnera aphidicola via RNAi or CRISPR-Cas remain technically challenging but conceptually prom ising, particu…” — [[ms-10-1186_s44399-026-00048-8-f3]]（`10.1186/s44399-026-00048-8`，genetic perturbation）
- “Recent studies suggest that melatonin not only directly regulates plant stress physiology but may also enhance drought tolerance by reshaping the structure and function of rhizosph…” — [[daily-42249284-f4]]（`10.1186/s12870-026-09179-1`，DNA binding/regulation）
- “Beyond nutrient exchange, AMF interact with bacterial and other fungal endophytes, and are suggested to contribute indirectly to root signalling and microbiome community establishm…” — [[daily-42435223-f2]]（`10.1007/s00253-026-13955-2`，protein interaction）

### 2.7 逆境记忆与表观调控

**规模** 36 条证据 / 23 篇文献；**构成** descriptive/observational(25)、expression/regulation(5)、protein interaction(3)、DNA binding/regulation(2)、omics/co-occurrence(1)；**因果层** 5 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Oryza sativa、Triticum aestivum、Arabidopsis thaliana，反复出现的实体为LSD1、HD2B、phenolic；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Bae et al., 2026 [[daily-42169378-f1]]；Bae et al., 2026 [[daily-42169378-f2]]；Bae et al., 2026 [[daily-42169378-f5]]）。
- **证据层级的张力**：5 条属于遗传扰动/蛋白互作/DNA 结合，31 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（Bae et al., 2026 [[daily-42169378-f2]]；[[daily-42725159-f6]]；[[daily-42412868-f1]]）。
- **可检验缺口**：遗传扰动、表型关联在本组缺证据；在补齐这些设计前，LSD1、HD2B、phenolic 与“逆境记忆与表观调控”的方向性关系应作为待检验命题（Bae et al., 2026 [[daily-42169378-f1]]；Bae et al., 2026 [[daily-42169378-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Oryza sativa | 3 | 1 | 3 | 1 | 16 | 24 |
| Triticum aestivum | 2 | 0 | 2 | 1 | 10 | 15 |
| Arabidopsis thaliana | 3 | 1 | 0 | 0 | 7 | 11 |
| Rosa spp. | 0 | 0 | 0 | 0 | 6 | 6 |
| Zea mays | 1 | 1 | 0 | 0 | 3 | 5 |

**基因实体（自动标注，前 5）**：LSD1(2)、HD2B(2)、GH1(1)、PR1(1)、PR3(1)（标注覆盖 9/36）。

**化合物实体（自动标注，前 5）**：phenolic(1)（标注覆盖 1/36）。

**代表断言（原文摘录，未改写）**

- “Such a specific structure enables H1 to bind to nucleosomes at their entry and exit sites, interact with linker DNA, and facilitate chromatin compaction.,,, Among species, the GH1 …” — [[daily-42169378-f2]]（`10.1080/15592324.2026.2677313`，protein interaction）
- “Chromatin immunoprecipitation assays can identify the transcription factors that bind to the ABRE motifs in the promoters of LbaSOD5 and LbaSOD10, whereas promoter deletion and mut…” — [[daily-42725159-f6]]（`10.3389/fpls.2026.1897912`，DNA binding/regulation）
- “We show that MPK3 interacts directly with and phosphorylates the histone deacetylase HD2B, which has been shown to deacetylate the lysine 9 residue of histone 3 (H3K9), a modificat…” — [[ref-s13059-017-1261-8-f1]]（`10.1186/s13059-017-1261-8`，protein interaction）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| LpCbDR1 | 3 | 6 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| BAM1 | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| COOL1 | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| HD2B | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、逆境记忆与表观调控 |
| LpERF1B | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| SnRK2s | 3 | 4 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| BAK1 | 3 | 3 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| HSP90 | 3 | 3 | 抗病基因与数量抗性、病原识别与免疫受体、非生物逆境响应 |
| OsPRO1 | 3 | 3 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| PBS1 | 3 | 3 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| phenolic | 5 | 9 | 免疫信号传导与活性氧、激素与免疫的权衡、病原识别与免疫受体、逆境记忆与表观调控、非生物逆境响应 |
| salicylic acid | 4 | 10 | 免疫信号传导与活性氧、微生物组与根际互作、病原识别与免疫受体、非生物逆境响应 |
| phenylpropanoid | 3 | 9 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| abscisic acid | 3 | 7 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |
| auxin | 3 | 7 | 免疫信号传导与活性氧、激素与免疫的权衡、非生物逆境响应 |
| lignin | 3 | 7 | 免疫信号传导与活性氧、病原识别与免疫受体、非生物逆境响应 |

### 3.1 跨子主题受控叙述

- **交叉实体**：LpCbDR1、BAM1、COOL1、HD2B、LpERF1B 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（[[accumulation-of-tocopherols-and-transcriptional-regulation-f1]]；[[accumulation-of-tocopherols-and-transcriptional-regulation-f3]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“非生物逆境响应”（125 条），最低为“激素与免疫的权衡”（1 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 病原识别与免疫受体 | 5 | 37 | 2 | 19 | 2 | 6 | 77 |
| 免疫信号传导与活性氧 | 13 | 35 | 1 | 29 | 1 | 5 | 159 |
| 抗病基因与数量抗性 | — | 3 | — | 3 | 4 | — | 15 |
| 非生物逆境响应 | 65 | 53 | 7 | 74 | 8 | 13 | 431 |
| 激素与免疫的权衡 | — | 1 | — | 1 | — | 1 | 25 |
| 微生物组与根际互作 | 1 | 6 | 1 | 6 | 1 | 1 | 59 |
| 逆境记忆与表观调控 | — | 3 | 2 | 5 | — | 1 | 25 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 493 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

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
| [[daily-40893112-f4]] | `10.1080/21645698.2025.2555037` | genetic perturbation | Reported that overexpression of the NsVP1 gene from Nitraria sibirica, significantly enhanced salt tolerance in Arabidop… |
| [[daily-40893112-f5]] | `10.1080/21645698.2025.2555037` | genetic perturbation | These findings suggest that the overexpression of LfVP1 enhances the ability of yeast strains to withstand osmotic stres… |
| [[daily-40893112-f7]] | `10.1080/21645698.2025.2555037` | genetic perturbation | For example, overexpression of the AVP1 gene, which encodes the H + -pyrophosphatase pump in Arabidopsis thaliana, signi… |
| [[daily-40893112-f8]] | `10.1080/21645698.2025.2555037` | genetic perturbation | In another study, the knockdown of the HVP1 gene inhibited growth and increased Na + accumulation in barley, while its o… |
| [[daily-40898604-f4]] | `10.1111/pbi.70349` | genetic perturbation | Both overexpression and silencing of GmSWEET8 enhanced resistance to nematode infection without affecting developmental … |
| [[daily-40898604-f8]] | `10.1111/pbi.70349` | protein interaction | The integrated analyses of Cleavage Under Targets and Tagmentation (CUT&Tag) and RNA sequencing (RNAseq) indicated that … |
| [[daily-41085122-f6]] | `10.1080/21645698.2025.2569162` | protein interaction | Glutamine, a central amino acid, modulates nitrate reductase activity and interacts with signaling pathways linked to ni… |
| [[daily-41622404-f2]] | `10.1111/ppl.70760` | protein interaction | Water availability critically interacts with heat stress, often worsening its effects. |

（另有 473 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

未筛查到方向相反的表述。注意：这**不等于**结论一致——多数证据只报告单一方向的观察，缺少反证不等于已被重复验证。

## 7. 覆盖与代表性缺口

- **1902 条证据（64%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4420 个中文字符，行内证据链接 99 处，密度 **11.2 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
