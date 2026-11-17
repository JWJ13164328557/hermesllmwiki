---
title: "代谢与天然产物 — Synthesis"
created: 2026-06-01
total_evidence: 270
total_papers: 88
library_papers: 858  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, metabolism]


soybean_relevance: ⭐中
legacy_archive: _review/synthesis_legacy_20261103/metabolism-natural-products.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 代谢与天然产物 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 270 | 本主题归属的证据对象数 |
| 独立论文 | 88 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 3.07 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 42% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(109)、Solanum lycopersicum(84)、Zea mays(73)、Oryza sativa(64)、Plant (unspecified)(42)、Malus domestica(30) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 184；protein interaction 28；genetic perturbation 26；DNA binding/regulation 24；phenotypic/association 6；omics/co-occurrence 2 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f8` | 10.1111/nph.19530 | Combined genome-wide transcriptomic proﬁling and promoter-binding experiments unveiled a c |
| `the-flavour-of-grape-colour-anthocyanin-f8` | 10.1093/jxb/erad223 | Remarkably, the DEGs identified in any of the cultivars and tissues overlapping with the s |
| `daily-42926806-f4` | 10.1016/j.fochx.2026.104567 | KEGG enrichment analysis indicated that differential metabolites were mainly enriched in a |
| `ref-fpls-2015-00206-f1` | 10.3389/fpls.2015.00206 | Here we report that, by labeling dividing stem cells with 5-ethynyl-2′- deoxyuridine (EdU) |
| `the-flavour-of-grape-colour-anthocyanin-f7` | 10.1093/jxb/erad223 | While white grapes and wines tend to display more flowery and white-fruit notes (Petronilh |
| `cmnac25-targets-cmmyb6-to-positively-regulate-f1` | 10.1186/s12915-023-01719-7 | An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anth |
| `ref-978-1-60327-563-7_16-f1` | 10.1007/978-1-60327-563-7_16 | For example, there is little in common morphologically between the emergent shoot of dicot |
| `ms-10-1007_s44372-026-00770-2-f3` | 10.1007/s44372-026-00770-2 | However, comparative evi dence suggests that, although terpenoid metabolism plays a centra |
| `cmnac25-targets-cmmyb6-to-positively-regulate-f2` | 10.1186/s12915-023-01719-7 | Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R |
| `daily-42927300-f5` | 10.1016/j.fochx.2026.104646 | Collectively, these results demonstrate that BS processing induces distinct chemical chang |
| `oslesv-and-osesv1-promote-transitory-and-f4` | 10.1016/j.xplc.2024.100893 | In this 412 study, we found that OsLESV and OsESV1 directly interact with GBSSI, GBSSII, a |
| `uv-b-promotes-flavonoid-biosynthesis-in-ginkgo-f2` | 10.1093/hr/uhad118 | In this study, we found that the phenotypes of 5-year-old ginkgo trees from low-altitude ( |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 26 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 28 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 24 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 184 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 6 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 2 | 组学共现（单细胞簇/共表达网络，非调控） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `oslesv-and-osesv1-promote-transitory-and-f4` | 10.1016/j.xplc.2024.100893 | In this 412 study, we found that OsLESV and OsESV1 directly interact with GBSSI, GBSSII, and PPDKB,  |
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2` | 10.1111/nph.19530 | We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene |
| `oslesv-and-osesv1-promote-transitory-and-f2` | 10.1016/j.xplc.2024.100893 | Taken together, our data suggest that OsLESV and OsESV1 play an important role in 181 transitory sta |
| `ref-35079635-f7` | 10.1038/35079635 | Levels of PHB transcript are also higher in mutant than in wild-type tissue; less than 2 h of incuba |
| `sel-advs-75436-f7` | 10.1002/advs.75436 | Collectively, these findings indicate that the mutant’s SAinsensitive phenotype primarily reflects r |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **270 条证据对象 / 88 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 270 |
| 独立文献（DOI/PMID 去重） | 88 |
| 平均每篇证据数 | 3.07 |
| 证据类型构成 | expression/regulation(184)、protein interaction(28)、genetic perturbation(26)、DNA binding/regulation(24)、phenotypic/association(6)、omics/co-occurrence(2) |
| 主要物种 | Arabidopsis thaliana(109)、Solanum lycopersicum(84)、Zea mays(73)、Oryza sativa(64)、Plant (unspecified)(42)、Malus domestica(30) |
| 子主题覆盖 | 7 个（其中证据 <5 条的 1 个） |

因果级证据共 **78 条**，占本主题证据的 **28.9%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 87 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 次生代谢物生物合成途径

**规模**：128 条证据 / 73 篇文献。**证据构成**：expression/regulation(96)、DNA binding/regulation(11)、protein interaction(10)、genetic perturbation(9)、omics/co-occurrence(1)、phenotypic/association(1)。

**形态判断**：以表达相关为主（75%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 30 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 98 条仅支持关联。

**主要物种**：Arabidopsis thaliana(43)、Solanum lycopersicum(36)、Oryza sativa(34)、Zea mays(30)、Plant (unspecified)(19)。

**代表断言（原文摘录，未改写）**

- “Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R3 MYB transcription factor CmMYB#7, which can interact with CmbHLH2, disrupted the MBW pro…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f2]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “Taken together, our data suggest that OsLESV and OsESV1 play an important role in 181 transitory starch biosynthesis in rice leaves, and that OsLESV and OsESV1 may have partially 1…” — [[oslesv-and-osesv1-promote-transitory-and-f2]]（`10.1016/j.xplc.2024.100893`，genetic perturbation）
- “PbrMYB24 binds to the AC elements and MBS in the promoters of SCW biosynthesis genes In order to determine the regulatory relationship between PbrMYB24 and genes involved in SCW bi…” — [[the-transcription-factor-pbrmyb24-regulates-lignin-f6]]（`10.1093/plphys/kiad200`，DNA binding/regulation）

### 2.2 转录调控与代谢工程

**规模**：74 条证据 / 26 篇文献。**证据构成**：expression/regulation(36)、protein interaction(18)、DNA binding/regulation(10)、genetic perturbation(9)、omics/co-occurrence(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占49%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 37 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 37 条仅支持关联。

**主要物种**：Arabidopsis thaliana(30)、Plant (unspecified)(24)、Solanum lycopersicum(19)、Malus domestica(18)、Zea mays(15)。

**代表断言（原文摘录，未改写）**

- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “PbrMYB24 binds to the AC elements and MBS in the promoters of SCW biosynthesis genes In order to determine the regulatory relationship between PbrMYB24 and genes involved in SCW bi…” — [[the-transcription-factor-pbrmyb24-regulates-lignin-f6]]（`10.1093/plphys/kiad200`，DNA binding/regulation）
- “We further demonstrated that both VvSBP8 and VvSBP13, encoding transcriptional repressors, displayed sufficient ability to interact with VvMYC1 and VvMYBA1, thereby interfering wit…” — [[mir156b-targeted-vvsbp813-functions-downstream-of-the-f7]]（`10.1093/hr/uhad293`，protein interaction）

### 2.3 代谢物运输与储存

**规模**：37 条证据 / 25 篇文献。**证据构成**：expression/regulation(18)、genetic perturbation(11)、protein interaction(4)、DNA binding/regulation(2)、phenotypic/association(1)、omics/co-occurrence(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占49%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 17 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 20 条仅支持关联。

**主要物种**：Solanum lycopersicum(12)、Arabidopsis thaliana(12)、Plant (unspecified)(10)、Malus domestica(6)、Nicotiana tabacum(6)。

**代表断言（原文摘录，未改写）**

- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “We show that SlGRAS9 is highly expressed in tomato fruit and knockout or downregulation of this gene via CRISPR/Cas9 genome editing and RNA interfer- ence approaches, respectively,…” — [[the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f2]]（`10.1111/nph.19530`，genetic perturbation）
- “Taken together, these findings demonstrated that the PgbHLH28 TF regulated the expression of the saponin biosynthesis pathway functional genes, PgDXS2 and PgHMGR2, via directly bin…” — [[rna-sequencing-analysis-reveals-pgbhlh28-as-f9]]（`10.1093/hr/uhae058`，DNA binding/regulation）

### 2.4 品质形成与营养成分

**规模**：59 条证据 / 27 篇文献。**证据构成**：expression/regulation(34)、protein interaction(11)、genetic perturbation(7)、DNA binding/regulation(5)、phenotypic/association(1)、omics/co-occurrence(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占58%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 23 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 36 条仅支持关联。

**主要物种**：Solanum lycopersicum(18)、Arabidopsis thaliana(17)、Malus domestica(15)、Oryza sativa(11)、Vitis vinifera(11)。

**代表断言（原文摘录，未改写）**

- “Combined genome-wide transcriptomic proﬁling and promoter-binding experiments unveiled a complex mechanism in which the SlGRAS9/SlZHD17 regulatory module modulates the expression o…” — [[the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f8]]（`10.1111/nph.19530`，DNA binding/regulation）
- “An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysanthemum, we have known that CmNAC25 directly binds to the pr…” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]]（`10.1186/s12915-023-01719-7`，protein interaction）
- “Taken together, our data suggest that OsLESV and OsESV1 play an important role in 181 transitory starch biosynthesis in rice leaves, and that OsLESV and OsESV1 may have partially 1…” — [[oslesv-and-osesv1-promote-transitory-and-f2]]（`10.1016/j.xplc.2024.100893`，genetic perturbation）

### 2.5 酶学与催化机制

**规模**：8 条证据 / 7 篇文献。**证据构成**：expression/regulation(4)、genetic perturbation(3)、DNA binding/regulation(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占50%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 4 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 4 条仅支持关联。

**主要物种**：Solanum lycopersicum(3)、rice(2)、Arabidopsis thaliana(2)、Arabidopsis(1)、maize(1)。

**代表断言（原文摘录，未改写）**

- “In this 412 study, we found that OsLESV and OsESV1 directly interact with GBSSI, GBSSII, and PPDKB, and 413 the transcript levels, protein abundance, and enzymatic activities of GB…” — [[oslesv-and-osesv1-promote-transitory-and-f4]]（`10.1016/j.xplc.2024.100893`，genetic perturbation）
- “Taken together, these findings indicated that MdbZIP44 overexpression enhanced the accumulation of starch and sucrose in tomato fruits by regulating the activities of enzymes invol…” — [[mdbzip44mdcprf2-likemdα-gp2-regulate-starch-and-sugar-metabo-f7]]（`10.1093/hr/uhae072`，genetic perturbation）
- “CmNAC25 also directly activates the promoter of CmDFR, which encodes the key enzyme in anthocyanin biosynthesis.” — [[cmnac25-targets-cmmyb6-to-positively-regulate-f6]]（`10.1186/s12915-023-01719-7`，DNA binding/regulation）

### 2.6 多组学解析代谢网络

**规模**：5 条证据 / 5 篇文献。**证据构成**：expression/regulation(4)、protein interaction(1)。

**形态判断**：以表达相关为主（80%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 4 条仅支持关联。

**主要物种**：Arabidopsis thaliana(3)、Vitis vinifera(1)、Rosa spp.(1)、Solanum lycopersicum(1)、Zea mays(1)。

**代表断言（原文摘录，未改写）**

- “Result VviERF003 and VviGT14 exhibit co-expression patterns Our prior research indicated that VviERF003 binds to the promoter of VviGT14 under DNA pull-down [27].” — [[ethylene-responsive-vvierf003-modulates-glycosylated-monoter-f4]]（`10.1093/hr/uhae065`，protein interaction）
- “Differences in the flavonoid and anthocyanin synthesis pathways were key to distinguishing the metabolomes of the five varieties, and the specific upregulation of anthocyanins such…” — [[daily-42926806-f1]]（`10.1016/j.fochx.2026.104567`，expression/regulation）
- “We found that the expression levels of flavonoid biosynthesis-related unigenes also increased when harvested at a delayed time, which was consistent with the flavonoid accumulation…” — [[morus-alba-l-leaves-integration-of-f1]]（`10.3389/fpls.2021.736332`，expression/regulation）

### 2.7 逆境代谢重编程

**规模**：1 条证据 / 1 篇文献。**证据构成**：expression/regulation(1)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Solanum lycopersicum(1)、Oryza sativa(1)、Glycine max(1)。

**代表断言（原文摘录，未改写）**

- “Microbial elicitors molecules secreted by bacteria and fungi bind to plant cell receptors and trigger signaling pathways that induce synthesis of terpenoids, pheno lic acids, and f…” — [[ms-10-1007_s11084-026-09761-5-f3]]（`10.1007/s11084-026-09761-5`，expression/regulation）

## 3. 可直接引用的因果级证据（自动筛选）

以下 78 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f4]] | `10.1093/hr/uhad185` | genetic perturbation | Overexpression of AcbHLH144 decreased phenolic accumulation in pineapple To check whether AcbHLH144 TF functions in regu… |
| [[acbhlh144-transcription-factor-negatively-regulates-phenolic-f5]] | `10.1093/hr/uhad185` | genetic perturbation | Overexpression of AcbHLH144 decreased phenolic accumulation in Arabidopsis Arabidopsis lines that overexpress AcbHLH144 … |
| [[analysis-of-lncrna43234-associated-cerna-network-reveals-f3]] | `10.1021/acs.jafc.3c00993` | protein interaction | The miRNAs predicted to interact with these targeted protein-coding genes showed upregulated expression levels. |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f5]] | `10.1111/pbi.14046` | genetic perturbation | Overexpression of PbrARF13 decreased stone cell content in pear fruit and secondary cell wall (SCW) thickness in transge… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f6]] | `10.1111/pbi.14046` | genetic perturbation | As expected, overexpression or knockdown of PbrMYB132 increased or decreased stone cell content in pear fruit and SCW th… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f8]] | `10.1111/pbi.14046` | DNA binding/regulation | We showed that PbrARF13 directly binds to the promoter of PbrNSC, a key gene for lignin and cellulose biosynthesis in st… |
| [[auxin-inhibits-lignin-and-cellulose-biosynthesis-f9]] | `10.1111/pbi.14046` | DNA binding/regulation | We also provide evidence that PbrNSC positively regulates the expression of PbrMYB132, which encodes a protein that can … |
| [[cmnac25-targets-cmmyb6-to-positively-regulate-f1]] | `10.1186/s12915-023-01719-7` | protein interaction | An MBW complex formed by the CmMYB6-CmbHLH2 protein complex is crucial for activating anthocyanin accumulation in chrysa… |
| [[cmnac25-targets-cmmyb6-to-positively-regulate-f2]] | `10.1186/s12915-023-01719-7` | protein interaction | Found that the reason for white appearance of ‘Jinba’ at the blooming stage was that the R3 MYB transcription factor CmM… |
| [[cmnac25-targets-cmmyb6-to-positively-regulate-f3]] | `10.1186/s12915-023-01719-7` | DNA binding/regulation | We found two ACGT elements in the promoter region of CmMYB6 at the − 400 ~ 0 bp region. |
| [[cmnac25-targets-cmmyb6-to-positively-regulate-f5]] | `10.1186/s12915-023-01719-7` | genetic perturbation | Meanwhile, we found some candidate differentially expressed TFs in RNAi-CmNAC25 transgenic line compared with WT, such a… |
| [[cmnac25-targets-cmmyb6-to-positively-regulate-f6]] | `10.1186/s12915-023-01719-7` | DNA binding/regulation | CmNAC25 also directly activates the promoter of CmDFR, which encodes the key enzyme in anthocyanin biosynthesis. |
| [[combined-analysis-of-the-metabolome-and-f3]] | `10.3390/ijms21041337` | protein interaction | AtbHLH113 in Arabidopsis interacts with PAP1/MYB75 modulating anthocyanin biosynthesis [74]. |
| [[daily-42965050-f7]] | `10.1093/hr/uhag216` | genetic perturbation | Collectively, gainand loss-of-function analyses establish IbWRKY24 as a key regulator of flavonoid biosynthesis, contrib… |
| [[ethylene-responsive-vvierf003-modulates-glycosylated-monoter-f1]] | `10.1093/hr/uhae065` | DNA binding/regulation | The VviERF003 protein can directly bind to the promoter fragment P7 of VviGT14, although the exact motifs involved are u… |

（另有 63 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **证据单薄的子主题 1 个**：逆境代谢重编程 1 条（各 <5 条，单篇论文即可左右结论）。
- **未能归入任何子主题的证据 79 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。
- **单篇证据物种 9 个**（Hordeum vulgare、Juglans regia、Ficus carica **方法**: transcriptomics (RNA-seq)、metabolomics (LC-MS/GC-MS)、Capsicum annuum…）：跨物种外推缺乏支撑。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
