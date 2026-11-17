---

title: "胁迫与免疫 — Synthesis"
created: 2026-06-01
total_evidence: 116
total_papers: 31
library_papers: 1346  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, stress, immunity, abiotic-stress, biotic-stress, hormone]


soybean_relevance: ⭐高
legacy_archive: _review/synthesis_legacy_20261103/stress-immunity.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 逆境与免疫 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 116 | 本主题归属的证据对象数 |
| 独立论文 | 31 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 3.74 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 39% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(82)、Oryza sativa(72)、Zea mays(51)、Solanum lycopersicum(29)、Nicotiana tabacum(27)、Glycine max(9) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 67；protein interaction 24；genetic perturbation 13；DNA binding/regulation 9；phenotypic/association 3 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `pdf-koag153-f7` | 10.1093/plcell/koag153 | Without OsNPR1 expression, the plants no longer 34 showed autoimmune/hyperactive immunity  |
| `accumulation-of-tocopherols-and-transcriptional-regulation-f3` | 10.1016/j.postharvbio.2021.111594 | We have recently reported that the concentration of total carotenoids in the flavedo of ‘N |
| `ms-10-1038_s41598-026-67627-2-f5` | 10.1038/s41598-026-67627-2 | Previous studies have shown that purine biosynthesis is required for immune effector progr |
| `ref-nph-17594-f1` | 10.1111/nph.17594 | ALD1 also shows WRKY33-dependent expression manner, and importantly, plants defective in t |
| `ref-nph-70171-f4` | 10.1111/nph.70171 | Under hypoxic conditions created by limited gas exchange in developing calli, the hypoxia- |
| `accumulation-of-tocopherols-and-transcriptional-regulation-f2` | 10.1016/j.postharvbio.2021.111594 | They seem to play a crucial role in the adaptation of plants to low temperatures, and muta |
| `banana-manac1-activates-secondary-cell-wall-f6` | 10.1111/pbi.14195 | The interaction between a NAC domain TF Vascular-Related NAC-Domain7 (VND7) and a VND Inte |
| `ref-15592324-2015-1011949-f6` | 10.1080/15592324.2015.1011949 | Unexpectedly, we also found that the receptor kinase ERECTA is required for ROS-induced co |
| `accumulation-of-tocopherols-and-transcriptional-regulation-f1` | 10.1016/j.postharvbio.2021.111594 | Collectively, results suggest that the concentration of tocopherols at harvest may play a  |
| `potato-leaf-heat-scrna-f5` | 10.1111/pbi.70546 | Node 1 corresponds to the differenti­ ation of PLCs toward MCs, while Node 2 is associated |
| `ms-10-20900_cbgg20260021-f7` | 10.20900/cbgg20260021 | Late Blight For late blight, CRISPR knockout of SlPMR4 reduced susceptibility [45], while  |
| `pdf-koag153-f1` | 10.1093/plcell/koag153 | 20 In conclusion, this study provides evidence for a novel regulatory interaction 21 betwe |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 13 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 24 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 9 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 67 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 3 | 表型关联（GWAS/QTL/自然变异/田间） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `pdf-koag153-f7` | 10.1093/plcell/koag153 | Without OsNPR1 expression, the plants no longer 34 showed autoimmune/hyperactive immunity phenotypes |
| `ms-10-1038_s41598-026-67627-2-f5` | 10.1038/s41598-026-67627-2 | Previous studies have shown that purine biosynthesis is required for immune effector programs, inclu |
| `accumulation-of-tocopherols-and-transcriptional-regulation-f2` | 10.1016/j.postharvbio.2021.111594 | They seem to play a crucial role in the adaptation of plants to low temperatures, and mutants impair |
| `ref-15592324-2015-1011949-f6` | 10.1080/15592324.2015.1011949 | Unexpectedly, we also found that the receptor kinase ERECTA is required for ROS-induced cortex proli |
| `ms-10-20900_cbgg20260021-f7` | 10.20900/cbgg20260021 | Late Blight For late blight, CRISPR knockout of SlPMR4 reduced susceptibility [45], while simultaneo |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **116 条证据对象 / 31 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 116 |
| 独立文献（DOI/PMID 去重） | 31 |
| 平均每篇证据数 | 3.74 |
| 证据类型构成 | expression/regulation(67)、protein interaction(24)、genetic perturbation(13)、DNA binding/regulation(9)、phenotypic/association(3) |
| 主要物种 | Arabidopsis thaliana(82)、Oryza sativa(72)、Zea mays(51)、Solanum lycopersicum(29)、Nicotiana tabacum(27)、Glycine max(9) |
| 子主题覆盖 | 6 个（其中证据 <5 条的 4 个） |

因果级证据共 **46 条**，占本主题证据的 **39.7%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 6 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 病原识别与免疫受体

**规模**：12 条证据 / 9 篇文献。**证据构成**：expression/regulation(6)、genetic perturbation(3)、phenotypic/association(1)、DNA binding/regulation(1)、protein interaction(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占50%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 5 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 7 条仅支持关联。

**主要物种**：Oryza sativa(9)、Arabidopsis thaliana(8)、Solanum lycopersicum(6)、Nicotiana tabacum(3)、Zea mays(3)。

**代表断言（原文摘录，未改写）**

- “Previous studies have shown that purine biosynthesis is required for immune effector programs, including T-cell functional states, supporting an association between PRPS1-related p…” — [[ms-10-1038_s41598-026-67627-2-f5]]（`10.1038/s41598-026-67627-2`，genetic perturbation）
- “Unexpectedly, we also found that the receptor kinase ERECTA is required for ROS-induced cortex proliferation.2 No cortex proliferation could be induced in plants with a mutation in…” — [[ref-15592324-2015-1011949-f6]]（`10.1080/15592324.2015.1011949`，genetic perturbation）
- “Late Blight For late blight, CRISPR knockout of SlPMR4 reduced susceptibility [45], while simultaneous CRISPR/Cas9 editing of miR482b and miR482c enhanced resistance to Phytophthor…” — [[ms-10-20900_cbgg20260021-f7]]（`10.20900/cbgg20260021`，genetic perturbation）

### 2.2 免疫信号传导与活性氧

**规模**：10 条证据 / 7 篇文献。**证据构成**：expression/regulation(7)、genetic perturbation(2)、protein interaction(1)。

**形态判断**：以表达相关为主（70%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 3 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 7 条仅支持关联。

**主要物种**：Arabidopsis thaliana(8)、Oryza sativa(6)、Zea mays(4)、Nicotiana tabacum(2)、Citrus spp.(1)。

**代表断言（原文摘录，未改写）**

- “Unexpectedly, we also found that the receptor kinase ERECTA is required for ROS-induced cortex proliferation.2 No cortex proliferation could be induced in plants with a mutation in…” — [[ref-15592324-2015-1011949-f6]]（`10.1080/15592324.2015.1011949`，genetic perturbation）
- “One RPD3/ HDA1 family protein, HDA6, is involved in plantpathogen interactions and has been shown to interact with an F-box protein involved in jasmonic acidmediated plant defense …” — [[ref-pp-107-111674-f6]]（`10.1104/pp.107.111674`，protein interaction）
- “Whether this is common is not well known, but at least these data suggest coordination of C allocation across the growing season, which may be mediated by both aboveand below-groun…” — [[ref-nph-13111-f1]]（`10.1111/nph.13111`，expression/regulation）

### 2.3 抗病基因与数量抗性

**规模**：1 条证据 / 1 篇文献。**证据构成**：genetic perturbation(1)。

**形态判断**：以遗传扰动为主（100%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 0 条仅支持关联。

**主要物种**：Ficus carica(1)。

**代表断言（原文摘录，未改写）**

- “Previous studies have shown that purine biosynthesis is required for immune effector programs, including T-cell functional states, supporting an association between PRPS1-related p…” — [[ms-10-1038_s41598-026-67627-2-f5]]（`10.1038/s41598-026-67627-2`，genetic perturbation）

### 2.4 非生物逆境响应

**规模**：19 条证据 / 10 篇文献。**证据构成**：expression/regulation(8)、genetic perturbation(6)、protein interaction(2)、phenotypic/association(2)、DNA binding/regulation(1)。

**形态判断**：证据类型分散（最大一类表达相关仅占42%），说明该子主题尚无统一研究范式，横向比较不同证据前须先核对其数据类型与实验层级。

**推断上限**：含 9 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 10 条仅支持关联。

**主要物种**：Arabidopsis thaliana(10)、Oryza sativa(10)、Solanum lycopersicum(8)、Zea mays(7)、Nicotiana tabacum(6)。

**代表断言（原文摘录，未改写）**

- “They seem to play a crucial role in the adaptation of plants to low temperatures, and mutants impaired in tocopherol synthesis have shown a cold-sensitive phenotype, with retarded …” — [[accumulation-of-tocopherols-and-transcriptional-regulation-f2]]（`10.1016/j.postharvbio.2021.111594`，genetic perturbation）
- “The interaction between a NAC domain TF Vascular-Related NAC-Domain7 (VND7) and a VND Interacting 2 (VNI2) TF contributes to the regulation of Coldregulated (Marquez-Garcıa et al.,…” — [[banana-manac1-activates-secondary-cell-wall-f6]]（`10.1111/pbi.14195`，protein interaction）
- “Furthermore, we found that MdASMT9 overexpression was associated with decreased ABA content and increased stomatal aperture under heat stress, which may enable leaves to sustain a …” — [[mdasmt9mediated-melatonin-biosynthesis-enhances-basal-thermo-f1]]（`10.1111/pce.14791`，genetic perturbation）

### 2.5 激素与免疫的权衡

**规模**：1 条证据 / 1 篇文献。**证据构成**：protein interaction(1)。

**形态判断**：以蛋白互作为主（100%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 0 条仅支持关联。

**主要物种**：Triticum aestivum(1)、Capsicum annuum(1)、Beta vulgaris(1)。

**代表断言（原文摘录，未改写）**

- “Such metabolic reprogramming of receiver plants plays a central role in plant–microbe interactions by priming plant defense responses against subsequent pathogen or herbivore attac…” — [[daily-42928643-f3]]（`10.1111/ppl.71160`，protein interaction）

### 2.6 微生物组与根际互作

**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。

### 2.7 逆境记忆与表观调控

**规模**：4 条证据 / 2 篇文献。**证据构成**：protein interaction(2)、expression/regulation(2)。

**形态判断**：以蛋白互作为主（50%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 2 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 2 条仅支持关联。

**主要物种**：Zea mays(3)、Oryza sativa(3)、Arabidopsis thaliana(3)、Triticum aestivum(1)、Capsicum annuum(1)。

**代表断言（原文摘录，未改写）**

- “We show that MPK3 interacts directly with and phosphorylates the histone deacetylase HD2B, which has been shown to deacetylate the lysine 9 residue of histone 3 (H3K9), a modificat…” — [[ref-s13059-017-1261-8-f1]]（`10.1186/s13059-017-1261-8`，protein interaction）
- “Such metabolic reprogramming of receiver plants plays a central role in plant–microbe interactions by priming plant defense responses against subsequent pathogen or herbivore attac…” — [[daily-42928643-f3]]（`10.1111/ppl.71160`，protein interaction）

## 3. 可直接引用的因果级证据（自动筛选）

以下 46 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[accumulation-of-tocopherols-and-transcriptional-regulation-f2]] | `10.1016/j.postharvbio.2021.111594` | genetic perturbation | They seem to play a crucial role in the adaptation of plants to low temperatures, and mutants impaired in tocopherol syn… |
| [[banana-manac1-activates-secondary-cell-wall-f6]] | `10.1111/pbi.14195` | protein interaction | The interaction between a NAC domain TF Vascular-Related NAC-Domain7 (VND7) and a VND Interacting 2 (VNI2) TF contribute… |
| [[banana-manac1-activates-secondary-cell-wall-f7]] | `10.1111/pbi.14195` | protein interaction | The expression of Ma06_g28730 in postharvest banana peel was obviously upregulated under chilling stress (Figure 2d), an… |
| [[daily-42928643-f3]] | `10.1111/ppl.71160` | protein interaction | Such metabolic reprogramming of receiver plants plays a central role in plant–microbe interactions by priming plant defe… |
| [[lamyc7-a-positive-regulator-of-linalool-f1]] | `10.1093/hr/uhae044` | DNA binding/regulation | The results of the Y1H and LUC assays showed that LaMYC7 can only bind to the LaTPS76 promoter, indicating that LaMYC7 r… |
| [[lamyc7-a-positive-regulator-of-linalool-f5]] | `10.1093/hr/uhae044` | DNA binding/regulation | LaMYC7 directly binds to the LaTPS76 promoter Because LaMYC7,LaTPS27,and LaTPS76 were related to caryophyllene biosynthe… |
| [[lamyc7-a-positive-regulator-of-linalool-f6]] | `10.1093/hr/uhae044` | DNA binding/regulation | This implied that LaMYC7 could directly bind to the LaTPS76 promoter but was unable to bind to the LaTPS26 promoter. |
| [[lamyc7-a-positive-regulator-of-linalool-f7]] | `10.1093/hr/uhae044` | DNA binding/regulation | LaMYC7 binds to the LaTPS76 promoter and activates its transcription. |
| [[lamyc7-a-positive-regulator-of-linalool-f8]] | `10.1093/hr/uhae044` | protein interaction | Arabidopsis MYC2 interacts with DELLA proteins in regulating sesquiterpene synthase gene expression. |
| [[mdasmt9mediated-melatonin-biosynthesis-enhances-basal-thermo-f1]] | `10.1111/pce.14791` | genetic perturbation | Furthermore, we found that MdASMT9 overexpression was associated with decreased ABA content and increased stomatal apert… |
| [[mdbt2-regulates-nitrogen-mediated-cuticular-wax-biosynthesis-f4]] | `10.1038/s41477-023-01587-7` | DNA binding/regulation | In apple, the R2R3-MYB transcription factor MdMYB30 binds to the promoter of MdKCS1 to regulate epidermal wax biosynthes… |
| [[mdsnrk11-interacts-with-mdglk1-to-regulate-f2]] | `10.1093/hr/uhad288` | DNA binding/regulation | MdSnRK1.1-mediated phosphorylation was critical for MdGLK1 binding to the target gene MdHEMA1 promoters. |
| [[mdsnrk11-interacts-with-mdglk1-to-regulate-f3]] | `10.1093/hr/uhad288` | DNA binding/regulation | In general, MdSnRK1.1-mediated phosphorylation was critical for MdGLK1 binding to the target gene promoters. |
| [[ms-10-1007_s44372-026-00698-7-f2]] | `10.1007/s44372-026-00698-7` | protein interaction | 5.2 Salt stress Although drought and heat are the dominant climatic stresses, salinity often interacts with these factor… |
| [[ms-10-1038_s41467-026-76840-6-f5]] | `10.1038/s41467-026-76840-6` | DNA binding/regulation | The difference in drought resistance is unlikely to be explained by NLR8 transcript abundance under drought or by the ef… |

（另有 31 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **未被覆盖的子主题 1 个**：微生物组与根际互作。这些方向在本库中没有可引用证据，任何涉及它们的论述都必须另行检索。
- **证据单薄的子主题 3 个**：抗病基因与数量抗性 1 条、激素与免疫的权衡 1 条、逆境记忆与表观调控 4 条（各 <5 条，单篇论文即可左右结论）。
- **未能归入任何子主题的证据 75 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。
- **单篇证据物种 6 个**（Beta vulgaris、Malus domestica、Ficus carica、Plant (unspecified)、Picea spp.…）：跨物种外推缺乏支撑。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
