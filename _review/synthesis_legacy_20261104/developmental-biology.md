---

title: "发育生物学 — Synthesis"
created: 2026-06-01
total_evidence: 3871
total_papers: 663
library_papers: 779  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, development]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261103/developmental-biology.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference
rebuild_version: v3

---
# 植物发育生物学 知识综合（证据重建版 v3）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 3871 | 本主题归属的证据对象数 |
| 独立论文 | 663 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 5.84 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 3% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(1220)、Oryza sativa(1176)、Zea mays(763)、Solanum lycopersicum(522)、Triticum aestivum(447)、Nicotiana tabacum(412) | 物种过度集中则外推性受限 |
| 证据类型 | descriptive/observational 2547；expression/regulation 417；protein interaction 320；phenotypic/association 241；genetic perturbation 167；omics/co-occurrence 112 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated o |
| `daily-42588892-f3` | 10.3390/plants15152389 | Strategies such as ‘ExpressEdit’, in which preassembled Cas9–sgRNA ribonucleoprotein compl |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to  |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenoty |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked c |
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication compl |
| `daily-42635641-f5` | 10.1007/s00299-026-03945-z | A Schematic representation of the T-DNA region of AtU6-26_pRGEB31 gRNAs multiplex construc |
| `ms-10-1007_s00344-026-12266-0-f2` | 10.1007/s00344-026-12266-0 | While novel_47 (targeting the DNA repair gene BRCA2) was upregulated in both genotypes, it |
| `daily-42514563-f2` | 10.3390/plants15142197 | The Arabidopsis argonaute 10 ( ago10 ) mutant exhibits defects in AM initiation, and in th |
| `blue-light-photoreceptor-cryptochrome-1-promotes-f1` | 10.1111/pce.14866 | The WT accumulated much higher anthocyanin under blue light than the other light treatment |
| `daily-42958739-f5` | 10.1111/tpj.71175 | When dipinoculated with Pst DC3000, the impa1 mutants exhibited increased susceptibility,  |
| `daily-42304209-f6` | 10.1186/s12870-026-09279-y | Although both EgMADS03 and EgMADS45 influenced flowering time, EgMADS03 was ultimately sel |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 167 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 320 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 67 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 417 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 241 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 112 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 2547 | 描述性/背景陈述（未报告可核验的实验设计） |

> 读法：`genetic perturbation` / `protein interaction` / `DNA binding/regulation` 可支持因果或直接调控；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能单独证明调控或因果。

### 遗传扰动类证据（仅高置信规则命中，前 5 条；仍须回原文核实）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `daily-42211481-f2` | 10.3389/fpls.2026.1815995 | Collectively, the enriched GO terms induced by idr1–1 mutation appear to be concentrated on alterati |
| `daily-42588892-f3` | 10.3390/plants15152389 | Strategies such as ‘ExpressEdit’, in which preassembled Cas9–sgRNA ribonucleoprotein complexes are d |
| `daily-42211481-f4` | 10.3389/fpls.2026.1815995 | Collectively, these results provide a clear demonstration that idr1–1 mutation is able to largely al |
| `daily-42452228-f6` | 10.3390/plants15132022 | Neither RTNLB16 Overexpression nor RTNLB16 Knockout Alone Reproduces the rtnlb16-1 Phenotype To test |
| `daily-42211481-f3` | 10.3389/fpls.2026.1815995 | The enhanced tolerance of idr1–1 mutant seedlings to osmotic stress may stem from marked changes in  |

### 正文状态

> frontmatter 标记 `body_status: rebuilt-*` 的页面，其子主题正文由 `rebuild_synthesis_body.py` 按本页证据确定性重建；本自动段是该快照的统计摘要。未标记的页面保留历史正文，机制性表述须逐条回原文核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **1306 条证据对象 / 231 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 0. 综述提要（受控生成）

本主题当前纳入 **1306 条证据 / 231 篇文献**。规则判定为因果或直接调控的 **210 条（16.1%）**；剔除方法描述、相关性措辞与无基因实体标注的条目后，可用于提要的 **96 条**。可判定程度最高的结论集中在GmERFA、PagCRY1、KO4：Knocking out GmERFA and its homologue by genome editing increased seed total fatty acid content, while overexpression of GmERFA leads to a r…（[[b5-iZzyxHmz_WpXAsbrHTBStw-f3]]）；The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abolished the anthocyani…（[[blue-light-photoreceptor-cryptochrome-1-promotes-f1]]）；In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly increased in cry1 mu…（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]）。研究重心位于“分生组织维持与干细胞稳态”（132 条证据，占 10%）。证据的物种分布以 Arabidopsis thaliana 为首（760 条，58%）。七类证据均有覆盖，主要瓶颈从“类型缺失”转为“同一结论的独立复现不足”。阅读时须区分两类陈述：因果级证据支撑的“已证机制”，以及表达/组学/描述性证据提示的“候选关联”；后者不得改写成调控或因果。

> 提要由脚本按证据类型与实体计数生成，不含跨证据的机制外推；逐条依据见第 2–3 节。

## 1. 主题概览（自动统计）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据对象 | 1306 | 本主题归属的证据条目数 |
| 独立文献（DOI/PMID 去重） | 231 | 去重后的论文数 |
| 平均每篇证据数 | 5.65 | 接近 1.0 说明每篇论文只贡献一条结论，系统性弱 |
| 单条证据论文占比 | 8%（19/231） | 越高说明证据碎片化越严重 |
| 证据类型构成 | descriptive/observational(861)、expression/regulation(180)、protein interaction(128)、genetic perturbation(49)、omics/co-occurrence(47)、DNA binding/regulation(33)、phenotypic/association(8) | 描述性占多数时机制结论需打折扣 |
| 类型标注置信度 | low(976)、medium(273)、high(57) | 低置信度标注须回原文核对 |
| 主要物种 | Arabidopsis thaliana(760)、Oryza sativa(461)、Zea mays(362)、Solanum lycopersicum(224)、Nicotiana tabacum(190)、Glycine max(117) | 物种过度集中则外推性受限 |
| 子主题覆盖 | 7/7（证据 <5 条的 0 个） | 覆盖缺口见第 7 节 |
| 未命中任何子主题的证据 | 884（68%） | 占比高说明子主题词表或证据文本需扩表 |

因果级证据共 **210 条**，占本主题证据的 **16.1%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

物种主导度：**Arabidopsis thaliana** 出现在 760 条证据（58%）。分布较分散，单物种主导风险较低，但需注意各物种证据层级是否可比。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 98 条跨组），因此各子主题计数之和大于总证据数。物种×类型交叉表只统计已标注字段，空单元格表示该组合无证据，不等于不存在相应生物学过程。凡“因果层 0 条”的子主题，其代表断言只能读作相关性，不得改写为调控或因果。

### 2.1 分生组织维持与干细胞稳态

**规模** 132 条证据 / 63 篇文献；**构成** descriptive/observational(74)、expression/regulation(31)、protein interaction(13)、DNA binding/regulation(4)、omics/co-occurrence(4)、genetic perturbation(3)；**因果层** 20 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为CLV3、WOX5、auxin、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f4]]）。
- **证据层级的张力**：20 条属于遗传扰动/蛋白互作/DNA 结合，112 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]；[[daily-41481480-f2]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f8]]；[[daily-41481480-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 8 | 3 | 21 | 3 | 0 | 48 | 86 |
| Oryza sativa | 2 | 6 | 4 | 14 | 2 | 0 | 33 | 61 |
| Zea mays | 0 | 8 | 3 | 14 | 0 | 0 | 19 | 44 |
| Solanum lycopersicum | 0 | 4 | 1 | 9 | 1 | 0 | 13 | 28 |
| Citrus spp. | 2 | 3 | 0 | 4 | 2 | 1 | 12 | 24 |

**基因实体（自动标注，前 5）**：CLV3(6)、WOX5(5)、ARR15(3)、ARR7(3)、TCX2(3)（标注覆盖 51/132）。

**化合物实体（自动标注，前 5）**：auxin(12)、sucrose(1)、gibberellin(1)（标注覆盖 14/132）。

**代表断言（原文摘录，未改写）**

- “While it has been shown that SHR-SCR can bind to JACKDAW and MAGPIE (and may be required to do so for SHR-SCR DNA-binding function), the expression domains of JACKDAW and MAGPIE ar…” — [[ref-j-tig-2017-05-002-f6]]（`10.1016/j.tig.2017.05.002`，protein interaction）
- “Overexpression of CDS (35S:: CDS ) caused severe growth inhibition, disrupted root meristem organization, reduced cell number, enlarged cell size, and decreased CYCB1;1 activity, i…” — [[daily-41481480-f2]]（`10.1080/15592324.2025.2611175`，genetic perturbation）
- “This genetic pathway de®nes a mechanism for differentiating between stem cells and organ founder cells within the shoot apical meristem and demonstrates that genes expressed in org…” — [[ref-35050091-f5]]（`10.1038/35050091`，protein interaction）

### 2.2 细胞分裂与细胞周期

**规模** 39 条证据 / 20 篇文献；**构成** descriptive/observational(20)、protein interaction(9)、expression/regulation(5)、genetic perturbation(3)、DNA binding/regulation(2)；**因果层** 14 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为OE12、RBR1、lignin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[blue-light-photoreceptor-cryptochrome-1-promotes-f3]]；[[daily-41481480-f3]]）。
- **证据层级的张力**：14 条属于遗传扰动/蛋白互作/DNA 结合，25 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[ref-j-pbi-2019-03-010-f1]]；[[blue-light-photoreceptor-cryptochrome-1-promotes-f3]]）。
- **可检验缺口**：表型关联、组学共现在本组缺证据；在补齐这些设计前，OE12、RBR1、lignin 与“细胞分裂与细胞周期”的方向性关系应作为待检验命题（[[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]；[[blue-light-photoreceptor-cryptochrome-1-promotes-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 6 | 1 | 4 | 12 | 24 |
| Oryza sativa | 1 | 4 | 1 | 1 | 5 | 12 |
| Zea mays | 1 | 4 | 0 | 1 | 6 | 12 |
| Nicotiana tabacum | 1 | 3 | 0 | 0 | 6 | 10 |
| Solanum lycopersicum | 2 | 3 | 0 | 1 | 2 | 8 |

**基因实体（自动标注，前 5）**：OE12(2)、RBR1(2)、AtE2Fc(2)、KO4(1)、PagCRY1aOE(1)（标注覆盖 15/39）。

**化合物实体（自动标注，前 5）**：lignin(1)（标注覆盖 1/39）。

**代表断言（原文摘录，未改写）**

- “Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are sufficient to increase ploidy level in trichomes (Castellano et al., 2001; Castella…” — [[ref-tab-0120-f2]]（`10.1199/tab.0120`，genetic perturbation）
- “In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly increased in cry1 mutant plants, we found a group of cell cy…” — [[blue-light-photoreceptor-cryptochrome-1-promotes-f2]]（`10.1111/pce.14866`，genetic perturbation）
- “ICK/KRP proteins are generally thought to interact with CDKA and CYCDs (Wang et al., 1998; De Veylder et al., 2001), although two recent reports indicate that some family members m…” — [[ref-tpc-106-044834-f4]]（`10.1105/tpc.106.044834`，protein interaction）

### 2.3 细胞命运决定与分化

**规模** 100 条证据 / 55 篇文献；**构成** descriptive/observational(62)、expression/regulation(25)、protein interaction(4)、omics/co-occurrence(4)、genetic perturbation(2)、DNA binding/regulation(2)；**因果层** 8 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为WIND1、EpSC、auxin、gibberellin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f3]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f5]]；[[b3-qnkDB6_AeT3N0ZaAwqrgng-f4]]）。
- **证据层级的张力**：8 条属于遗传扰动/蛋白互作/DNA 结合，92 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]]；[[ref-annurev-cellbio-100617-06-f8]]；Manuel et al., 2022 [[a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f5]]）。
- **可检验缺口**：本组七类证据均有覆盖，主要缺口从“类型缺失”转为“同一结论的独立复现与条件分层不足”，应以跨实验室重复和统一条件比较来检验（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]]；[[ref-annurev-cellbio-100617-06-f8]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 1 | 3 | 1 | 19 | 1 | 1 | 44 | 70 |
| Oryza sativa | 0 | 3 | 0 | 6 | 1 | 1 | 21 | 32 |
| Zea mays | 0 | 4 | 1 | 8 | 0 | 0 | 11 | 24 |
| Solanum lycopersicum | 1 | 0 | 1 | 4 | 0 | 0 | 7 | 13 |
| Nicotiana tabacum | 0 | 0 | 0 | 2 | 0 | 0 | 10 | 12 |

**基因实体（自动标注，前 5）**：WIND1(6)、EpSC(2)、VND6(2)、VND7(2)、AP2(2)（标注覆盖 28/100）。

**化合物实体（自动标注，前 5）**：auxin(4)、gibberellin(1)、brassinosteroid(1)（标注覆盖 6/100）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ref-tpc-107-056069-f6]]。

**代表断言（原文摘录，未改写）**

- “Using genetic loss-of-function experiments and pharmacological inhibition of FAO both in vitro and in vivo, we show that blocking this metabolic pathway disrupts EpSC differentiati…” — [[ms-10-1038_s41467-026-77023-z-f3]]（`10.1038/s41467-026-77023-z`，genetic perturbation）
- “Towards the differentiation pathway, MP directly regulates LEAFY (LFY), AINTEGUMENTA (ANT) and ANTEGUMENTA-LIKE6 (AIL6) transcription factors, which are required for floral fate ac…” — [[ref-j-pbi-2014-11-002-f2]]（`10.1016/j.pbi.2014.11.002`，DNA binding/regulation）
- “Unlike CLV3, which is expressed in shoot stem cells, CLE40 is expressed in differentiated columella cells and binds to receptors that are expressed in the overlying columella stem …” — [[ref-annurev-cellbio-100617-06-f8]]（`10.1146/annurev-cellbio-100617-062459`，protein interaction）

### 2.4 器官发生与形态建成

**规模** 44 条证据 / 31 篇文献；**构成** descriptive/observational(27)、expression/regulation(9)、genetic perturbation(5)、protein interaction(2)、DNA binding/regulation(1)；**因果层** 8 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Rosa spp.，反复出现的实体为WOX11、SbiGRF1、auxin、sucrose；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[daily-42026737-f1]]；[[daily-42026737-f2]]；[[daily-42026737-f4]]）。
- **证据层级的张力**：8 条属于遗传扰动/蛋白互作/DNA 结合，36 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42430664-f8]]；[[daily-42773404-f5]]；[[daily-42245747-f7]]）。
- **可检验缺口**：表型关联、组学共现在本组缺证据；在补齐这些设计前，WOX11、SbiGRF1、auxin 与“器官发生与形态建成”的方向性关系应作为待检验命题（[[daily-42026737-f1]]；[[daily-42026737-f2]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 2 | 1 | 7 | 14 | 27 |
| Oryza sativa | 2 | 1 | 1 | 3 | 10 | 17 |
| Rosa spp. | 1 | 0 | 0 | 4 | 3 | 8 |
| Citrus spp. | 0 | 0 | 0 | 2 | 6 | 8 |
| Zea mays | 3 | 1 | 1 | 0 | 2 | 7 |

**基因实体（自动标注，前 5）**：WOX11(2)、SbiGRF1(1)、SbiMIR396d(1)、MsNAC17(1)、PH16(1)（标注覆盖 17/44）。

**化合物实体（自动标注，前 5）**：auxin(9)、sucrose(1)、flavonoid(1)（标注覆盖 11/44）。

**代表断言（原文摘录，未改写）**

- “Overexpression of ZmSPL12 suppresses maize root growth under normal, wellwatered (WW) conditions, but this effect was substantially attenuated under soil compaction stress, resulti…” — [[daily-42773404-f5]]（`10.1111/nph.71592`，genetic perturbation）
- “The coexpression network analysis between OsERF48 and root-specific overexpression of ERF48 root RNA-seq data showed that calmodulinlike protein genes, OsCML16, is a direct target …” — [[ref-ppl-13651-f3]]（`10.1111/ppl.13651`，DNA binding/regulation）
- “MsNAC17 significantly enhances the root growth capacity of apple rootstocks under drought stress, and the growth advantage conferred by its overexpression constitutes an important …” — [[daily-42430664-f8]]（`10.1093/plphys/kiag488`，genetic perturbation）

### 2.5 激素与发育信号整合

**规模** 102 条证据 / 60 篇文献；**构成** descriptive/observational(65)、expression/regulation(17)、protein interaction(9)、DNA binding/regulation(7)、genetic perturbation(2)、omics/co-occurrence(2)；**因果层** 18 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Oryza sativa、Zea mays，反复出现的实体为AHP6、WOX11、auxin、gibberellin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]；[[10-1146-annurev-arplant-070225-032745-f1]]）。
- **证据层级的张力**：18 条属于遗传扰动/蛋白互作/DNA 结合，84 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[daily-42773404-f3]]；[[ref-annurev-arplant-042811-10-f2]]；[[ms-10-21674_2448-0479-121-38-47-f3]]）。
- **可检验缺口**：表型关联在本组缺证据；在补齐这些设计前，AHP6、WOX11、auxin 与“激素与发育信号整合”的方向性关系应作为待检验命题（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f3]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 2 | 7 | 6 | 13 | 2 | 40 | 70 |
| Oryza sativa | 1 | 3 | 4 | 3 | 1 | 25 | 37 |
| Zea mays | 0 | 3 | 6 | 3 | 0 | 17 | 29 |
| Solanum lycopersicum | 0 | 1 | 3 | 2 | 0 | 12 | 18 |
| Citrus spp. | 1 | 0 | 0 | 2 | 0 | 8 | 11 |

**基因实体（自动标注，前 5）**：AHP6(4)、WOX11(3)、ARR1(3)、ERF115(3)、IPT7(2)（标注覆盖 49/102）。

**化合物实体（自动标注，前 5）**：auxin(68)、gibberellin(6)、ethylene(6)、abscisic acid(4)、jasmonic acid(3)（标注覆盖 80/102）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[daily-42243683-f8]]。

**代表断言（原文摘录，未改写）**

- “Short-chain peptides (oligopeptides) applied through the leaf canopy are readily absorbed through stomata and then bind to kinase receptors on the cell membrane to activate endogen…” — [[ms-10-47191_ijmra_v9-i7-41-f2]]（`10.47191/ijmra/v9-i7-41`，protein interaction）
- “Since oxylipins are known to interact with auxin and gibberellin signaling pathways, which are major regulators of cell expansion and fruit growth, the modulation of RiLOX3 express…” — [[daily-42452253-f3]]（`10.3390/plants15132055`，protein interaction）
- “STM directly activates transcription of the cytokinin biosynthetic enzyme gene IPT7 in the shoot meristem, and exogenous application of cytokinins or expression of a cytokinin bios…” — [[ref-annurev-arplant-042811-10-f2]]（`10.1146/annurev-arplant-042811-105555`，DNA binding/regulation）

### 2.6 表观调控与发育可塑性

**规模** 39 条证据 / 23 篇文献；**构成** descriptive/observational(23)、expression/regulation(9)、protein interaction(3)、DNA binding/regulation(3)、omics/co-occurrence(1)；**因果层** 6 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Zea mays、Nicotiana tabacum，反复出现的实体为AtGCN5、GL2、auxin；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f1]]；[[b4-0Ai2UdSwKz-GbYdfit26vw-f1]]；[[cr-10-1016-j-tcb-2010-12-004-f3]]）。
- **证据层级的张力**：6 条属于遗传扰动/蛋白互作/DNA 结合，33 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[ref-gb-2009-10-2-210-f2]]；[[ref-j-molp-2026-03-005-f2]]；[[cr-10-1016-j-tcb-2010-12-004-f3]]）。
- **可检验缺口**：遗传扰动、表型关联在本组缺证据；在补齐这些设计前，AtGCN5、GL2、auxin 与“表观调控与发育可塑性”的方向性关系应作为待检验命题（[[b3-qnkDB6_AeT3N0ZaAwqrgng-f1]]；[[b4-0Ai2UdSwKz-GbYdfit26vw-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 3 | 8 | 0 | 11 | 25 |
| Zea mays | 1 | 1 | 2 | 1 | 11 | 16 |
| Nicotiana tabacum | 2 | 1 | 1 | 0 | 6 | 10 |
| Oryza sativa | 0 | 0 | 1 | 0 | 7 | 8 |
| Citrus spp. | 0 | 0 | 4 | 0 | 1 | 5 |

**基因实体（自动标注，前 5）**：AtGCN5(5)、GL2(3)、HAC1(2)、CoTSK(1)、ZmSPL12(1)（标注覆盖 18/39）。

**化合物实体（自动标注，前 5）**：auxin(1)（标注覆盖 1/39）。

**代表断言（原文摘录，未改写）**

- “Thebromodomain binds to acetylated histone lysine motifs (Zeng and Zhou, 2002), and therefore can be considered as a reader of histoneacetylationmarkers.T-DNAinsertionsingcn5-1andg…” — [[ref-ssq018-f8]]（`10.1093/mp/ssq018`，protein interaction）
- “[1] use chromatin immunoprecipitation and electrophoretic mobility shift experiments to show that the ARR1 protein interacts with the SHY2 promoter in vivo and with a GATC-containi…” — [[ref-gb-2009-10-2-210-f2]]（`10.1186/gb-2009-10-2-210`，DNA binding/regulation）
- “When compared with the YFP fluorescence observed for the class II histone deacetylase HDA5, which is known to localize to the nucleus but does not directly interact with WIND1 (Ali…” — [[ref-j-molp-2026-03-005-f2]]（`10.1016/j.molp.2026.03.005`，protein interaction）

### 2.7 再生与愈伤组织形成

**规模** 78 条证据 / 42 篇文献；**构成** descriptive/observational(59)、expression/regulation(11)、omics/co-occurrence(4)、protein interaction(3)、DNA binding/regulation(1)；**因果层** 4 条（可支撑有限机制表述）。


**受控叙述（按证据类型分层；每句附原始证据）**

- **一致的观察范围**：本组证据集中在Arabidopsis thaliana、Zea mays、Oryza sativa，反复出现的实体为WIND1、EMF2、auxin、jasmonic acid；可共同确认的是这些实体或过程在上述物种与条件下被观察到，而不是其跨物种普遍性（[[cr-10-1016-j-tcb-2010-12-004-f2]]；[[cr-10-1038-nature08152-f1]]；[[cr-10-1038-nature08152-f2]]）。
- **证据层级的张力**：4 条属于遗传扰动/蛋白互作/DNA 结合，74 条属于表达、组学或描述性证据；因此本组最强只能写到“扰动或直接结合与该表型/表达变化相关”，其余条目用于提出候选关系，不能反向证明因果（[[ref-nph-70171-f4]]；[[ref-nph-70171-f7]]；[[cr-10-1016-j-tcb-2010-12-004-f2]]）。
- **可检验缺口**：遗传扰动、表型关联在本组缺证据；在补齐这些设计前，WIND1、EMF2、auxin 与“再生与愈伤组织形成”的方向性关系应作为待检验命题（[[cr-10-1016-j-tcb-2010-12-004-f2]]；[[cr-10-1038-nature08152-f1]]）。

**物种 × 证据类型（前 5 物种）**

| 物种 | 蛋白互作 | DNA 结合 | 表达相关 | 组学共现 | 描述性 | 合计 |
|---|---|---|---|---|---|---|
| Arabidopsis thaliana | 3 | 1 | 6 | 3 | 26 | 39 |
| Zea mays | 2 | 1 | 0 | 2 | 14 | 19 |
| Oryza sativa | 3 | 1 | 0 | 0 | 12 | 16 |
| Solanum lycopersicum | 0 | 0 | 0 | 2 | 12 | 14 |
| Pinus spp. | 0 | 0 | 3 | 0 | 9 | 12 |

**基因实体（自动标注，前 5）**：WIND1(4)、EMF2(2)、CB037(2)、ERF115(2)、OsBBM1(1)（标注覆盖 19/78）。

**化合物实体（自动标注，前 5）**：auxin(7)、jasmonic acid(1)（标注覆盖 8/78）。

**标注一致性提示**：本组 1 条证据标注为描述性，但断言含扰动/互作措辞（genetic perturbation），类型可能被低估，需回原文确认；例如 [[ms-10-1007_s12374-026-09525-8-f4]]。

**代表断言（原文摘录，未改写）**

- “In conclusion, the observed physical interaction between ERF115 and PAT1 combined with the co-expression of their genes and additive effects of the double mutants and overexpressio…” — [[ref-nplants-2016-165-f2]]（`10.1038/nplants.2016.165`，protein interaction）
- “Under hypoxic conditions created by limited gas exchange in developing calli, the hypoxia-activated RELATED TO APETALA 2.12 (RAP2.12) directly binds to the promoter of the ICS1 gen…” — [[ref-nph-70171-f4]]（`10.1111/nph.70171`，DNA binding/regulation）
- “Remarkably, the fundamental questions of which tissues contribute to the blastema, and whether blastema cells are a multipotent or pluripotent cell type have remained largely unans…” — [[cr-10-1038-nature08152-f6]]（`10.1038/nature08152`，descriptive/observational）

## 3. 跨子主题实体枢纽（自动统计）

下列实体在 **≥2 个子主题**中被独立证据提及。它们本身**不构成机制结论**，但说明该实体是本主题多条研究线的交叉点，值得优先核对证据层级。

| 基因 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| WIND1 | 5 | 14 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、激素与发育信号整合、细胞命运决定与分化、表观调控与发育可塑性 |
| WOX11 | 5 | 9 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合、细胞命运决定与分化 |
| ERF115 | 4 | 8 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、激素与发育信号整合、细胞命运决定与分化 |
| ARR1 | 4 | 6 | 器官发生与形态建成、激素与发育信号整合、细胞命运决定与分化、表观调控与发育可塑性 |
| ZmSPL12 | 4 | 5 | 分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合、表观调控与发育可塑性 |
| GL2 | 3 | 5 | 细胞分裂与细胞周期、细胞命运决定与分化、表观调控与发育可塑性 |
| AtE2Fc | 3 | 4 | 分生组织维持与干细胞稳态、细胞分裂与细胞周期、细胞命运决定与分化 |
| CYCD3 | 3 | 4 | 分生组织维持与干细胞稳态、激素与发育信号整合、细胞分裂与细胞周期 |
| PAT1 | 3 | 4 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、细胞命运决定与分化 |
| PIN1 | 3 | 4 | 分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合 |

| 化合物 | 命中子主题数 | 证据条数 | 涉及子主题 |
|---|---|---|---|
| auxin | 6 | 101 | 再生与愈伤组织形成、分生组织维持与干细胞稳态、器官发生与形态建成、激素与发育信号整合、细胞命运决定与分化、表观调控与发育可塑性 |
| gibberellin | 3 | 8 | 分生组织维持与干细胞稳态、激素与发育信号整合、细胞命运决定与分化 |
| jasmonic acid | 2 | 4 | 再生与愈伤组织形成、激素与发育信号整合 |
| brassinosteroid | 2 | 3 | 激素与发育信号整合、细胞命运决定与分化 |
| sucrose | 2 | 2 | 分生组织维持与干细胞稳态、器官发生与形态建成 |

### 3.1 跨子主题受控叙述

- **交叉实体**：WIND1、WOX11、ERF115、ARR1、ZmSPL12 等实体在 ≥2 个子主题中重复出现；这只能说明多条研究线指向同一候选，不能说明同一机制（摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f1]]；摘要 et al., 2019 [[10-1146-annurev-arplant-042817-f2]]）。
- **层级不均**：因果层证据在子主题间分布不均，最高为“分生组织维持与干细胞稳态”（20 条），最低为“再生与愈伤组织形成”（4 条）；跨子主题比较结论强度前须先对齐这一差异。
- **共同缺口**：七类证据齐全，瓶颈是同一结论的独立复现与条件分层，而非证据类型。

## 4. 研究设计缺口矩阵（子主题 × 证据类型）

> 单元格为证据条数，`—` 表示该组合在本主题无证据。最后一列之后按行读：一行里若前三列全为 `—`，该子主题**没有任何因果层证据**。

| 子主题 | 遗传扰动 | 蛋白互作 | DNA 结合 | 表达相关 | 表型关联 | 组学共现 | 描述性 |
|---|---|---|---|---|---|---|---|
| 分生组织维持与干细胞稳态 | 3 | 13 | 4 | 31 | 3 | 4 | 74 |
| 细胞分裂与细胞周期 | 3 | 9 | 2 | 5 | — | — | 20 |
| 细胞命运决定与分化 | 2 | 4 | 2 | 25 | 1 | 4 | 62 |
| 器官发生与形态建成 | 5 | 2 | 1 | 9 | — | — | 27 |
| 激素与发育信号整合 | 2 | 9 | 7 | 17 | — | 2 | 65 |
| 表观调控与发育可塑性 | — | 3 | 3 | 9 | — | 1 | 23 |
| 再生与愈伤组织形成 | — | 3 | 1 | 11 | — | 4 | 59 |

所有已有证据的子主题都至少含 1 条因果/直接互作级证据，机制表述具备最低限度的实验托底。

## 5. 可直接引用的因果级证据（自动筛选）

以下 210 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[10-1146-annurev-arplant-042817-f3]] | `10.1146/annurev-arplant-042817-040549` | DNA binding/regulation | More in-depth studies found that WUS directly regulates additional cytokininand auxin-related genes, possibly controllin… |
| [[10-1146-annurev-arplant-042817-f4]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | HOMEODOMAIN LEUCINE ZIPPER (HD-ZIP III) genes, whose protein products interact with the type-B RRs and bind the same WUS… |
| [[10-1146-annurev-arplant-042817-f7]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CIKs also interact with other CLV receptors and are phosphorylated by CLV1, suggesting that they act as a direct downstr… |
| [[10-1146-annurev-arplant-042817-f8]] | `10.1146/annurev-arplant-042817-040549` | protein interaction | CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged meristems and function … |
| [[10-7554-elife-17214-001-f4]] | `10.7554/eLife.17214` | protein interaction | PWR binds to the same genomic regions as HDA9 at HDA9 targets. |
| [[b3-qnkDB6_AeT3N0ZaAwqrgng-f5]] | `10.1007/s44412-025-00004-4` | protein interaction | In tetraploid wheat, AGL6 interacts with multiple classes of MADS-box genes within the ABCDE model, coordinating their f… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f1]] | `10.1111/pbi.70348` | protein interaction | Collectively, these results demonstrate that GmERFA physically interacts with GmNFYA for possible regulation of seed oil… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f3]] | `10.1111/pbi.70348` | genetic perturbation | Knocking out GmERFA and its homologue by genome editing increased seed total fatty acid content, while overexpression of… |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f4]] | `10.1111/pbi.70348` | protein interaction | GmERFA interacts with GmNFYA to inhibit its transcriptional activation of GmbZIP123 and GmZF392, both of which promotes … |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f5]] | `10.1111/pbi.70348` | DNA binding/regulation | The GmERFA also directly binds to the promoter regions of GmbZIP123 and GmZF392 and represses their gene expression. |
| [[b5-iZzyxHmz_WpXAsbrHTBStw-f8]] | `10.1111/pbi.70348` | protein interaction | GmMYB73 interacts with GL3 and EGL3 to suppress the expression of GL2, thus promoting the conversion of phosphatidylchol… |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f1]] | `10.1111/pce.14866` | genetic perturbation | The WT accumulated much higher anthocyanin under blue light than the other light treatments, while the cry1 mutants abol… |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f2]] | `10.1111/pce.14866` | genetic perturbation | In supportive to the significantly reduced cell layers in the cambium zone of PagCRY1aOE plants, which is significantly … |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f4]] | `10.1111/pce.14866` | genetic perturbation | Overexpression of PagCRY1 substantially inhibited plant growth and promoted secondary xylem development in Populus, whil… |
| [[blue-light-photoreceptor-cryptochrome-1-promotes-f5]] | `10.1111/pce.14866` | genetic perturbation | Overexpression of PagCRY1 dramatically increased anthocyanin accumulation. |
| [[daily-40635304-f1]] | `10.1111/pbi.70217` | DNA binding/regulation | In summary, these findings suggest that the normal GoPGF protein directly binds to the promoters of multiple WRKY genes,… |
| [[daily-40635304-f4]] | `10.1111/pbi.70217` | protein interaction | This leads to production of GoPGF that in turn binds to Gbox and MYC elements within the promoters of WRKY genes thereby… |
| [[daily-40635304-f6]] | `10.1111/pbi.70217` | protein interaction | Together, these results conclusively demonstrate that GoSPGF can directly and specifically bind to the ‘AGAC’ motif in t… |
| [[daily-41481480-f2]] | `10.1080/15592324.2025.2611175` | genetic perturbation | Overexpression of CDS (35S:: CDS ) caused severe growth inhibition, disrupted root meristem organization, reduced cell n… |
| [[daily-41481480-f4]] | `10.1080/15592324.2025.2611175` | protein interaction | This gene family was first discovered and identified in Drosophila via the yeast two-hybrid assays, and the protein enco… |

（另有 190 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 6. 证据间的张力与矛盾（自动筛查）

自动筛查发现 5 组“同一基因、方向相反”的表述。这类冲突通常来自物种、组织或处理条件不同，**不宜简单判定一方错误**，而应作为条件分层实验的设计依据。

| 基因 | 冲突类型 | 涉及来源（截断） |
|---|---|---|
| CLV3 | regulation direction dispute | [[10-1146-annurev-arplant-042817]]；[[10-1146-annurev-arplant-042817]]；[[ref-annurev-arplant-042811-10]] |
| CYCB1 | regulation direction dispute | [[daily-41481480]]；[[ref-tpc-106-044834]] |
| BRC1 | regulation direction dispute | [[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]] |
| TB1 | regulation direction dispute | [[ms-10-1038_s41467-026-77029-7]]；[[ms-10-1038_s41467-026-77029-7]]；[[ref-s13059-025-03811-3]] |
| MYB36 | regulation direction dispute | [[ref-Chapter-Three---Defining-the-P]]；[[ref-j-tig-2017-05-002]]；[[ref-j-tig-2017-05-002]] |

> 筛查规则为“激活/抑制”等对立动词共现，属关键词启发式，可能误报；每条冲突都必须回原文核对实验条件后才能采信。

## 7. 覆盖与代表性缺口

- **884 条证据（68%）未命中任何子主题**：说明子主题词表覆盖不足，这部分证据目前无法进入结构性讨论。
- **证据类型以摘要级断言为主**：本知识库对多数文献仅收录摘要/图表级断言，无法支撑实验条件比较与因果推断；全文覆盖率是当前深度的上限约束。
- **文献元数据不全**：论文页 `year` / `journal` 字段覆盖率极低，因此本页不给出发表年份分布，也无法用年份评估时效性；frontmatter 的 `library_papers` 为历史手写值，与 tags 归一化统计相差数倍，**不可引用**。

## 8. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。

## 9. 行内引用密度自检

本页正文 4552 个中文字符，行内证据链接 119 处，密度 **13.1 处/500 字**（目标 ≥1）。链接指向证据页，不直接指向出版社；引用前须沿证据页回到原文核对。
