---

title: "单细胞与空间组学 — Synthesis"
created: 2026-06-01
total_evidence: 79
total_papers: 41
library_papers: 405  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [synthesis, single-cell, spatial-omics, transcriptomics, plant-atlas]


soybean_relevance: ⭐中
legacy_archive: _review/synthesis_legacy_20261103/single-cell-spatial-omics.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 单细胞与空间组学 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 79 | 本主题归属的证据对象数 |
| 独立论文 | 41 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 1.93 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 59% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Zea mays(41)、Oryza sativa(38)、Arabidopsis thaliana(32)、Ficus carica(11)、Solanum lycopersicum(6)、Glycine max(5) | 物种过度集中则外推性受限 |
| 证据类型 | omics/co-occurrence 51；expression/regulation 13；genetic perturbation 11；protein interaction 2；DNA binding/regulation 1；descriptive/observational 1 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-978-1-4939-8657-6_9-f1` | 10.1007/978-1-4939-8657-6_9 | 1830, https://doi.org/10.1007/978-1-4939-8657-6_9, © Springer Science+Business Media, LLC, |
| `ref-j-tplants-2019-10-008-f6` | 10.1016/j.tplants.2019.10.008 | However, current methods do allow the capture and identification of QC cells [9,10], highl |
| `ref-s13059-015-0580-x-f2` | 10.1186/s13059-015-0580-x | We found several examples of low level marker expression in ‘unexpected’ cell types, inclu |
| `ms-10-1371_journal-pgen-1012300-f1` | 10.1371/journal.pgen.1012300 | Together, this study provides the first highresolution single-cell atlas of cellular organ |
| `ref-erae107-f4` | 10.1093/jxb/erae107 | Another scRNA-seq study reported that a significant portion of Toll/interleukin-1 receptor |
| `ref-pbi-14097-f1` | 10.1111/pbi.14097 | This study provides not only a global view of maize cell fate determination during root de |
| `rice-root-cell-types-10x` | 10.1016/j.molp.2020.12.014 | Single-cell RNA-seq of root tips from two agronomically important rice cultivars (Nipponba |
| `differential-accessibility-regulates-cell-type-expression` | 10.1016/j.molp.2021.01.001 | Integrative analysis of snATAC-seq and scRNA-seq data demonstrates that cell-type-specific |
| `maize-ear-cell-types-scrna-seq` | 10.1016/j.devcel.2020.12.015 | Single-cell RNA-seq of developing maize ears (1-5 mm immature ears) resolves cell-type div |
| `ref-science-aaa6090-f3` | 10.1126/science.aaa6090 | Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imagi |
| `root-cluster-hormone-response-patterns` | 10.1016/j.molp.2019.04.004 | The 24 root cell clusters defined by scRNA-seq exhibit distinct expression patterns for ho |
| `ref-s41467-023-44369-7-f4` | 10.1038/s41467-023-44369-7 | Large-scale profiling of TF-binding sites using ampDAP-seq The transcriptomic identities o |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 11 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 2 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 1 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 13 | 表达相关（转录组/qPCR，不能单独推因果） |
| omics/co-occurrence | 51 | 组学共现（单细胞簇/共表达网络，非调控） |
| descriptive/observational | 1 | 描述性观察（无扰动/互作/关联设计） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `rice-root-cell-types-10x` | 10.1016/j.molp.2020.12.014 | Single-cell RNA-seq of root tips from two agronomically important rice cultivars (Nipponbare and Azu |
| `maize-ear-cell-types-scrna-seq` | 10.1016/j.devcel.2020.12.015 | Single-cell RNA-seq of developing maize ears (1-5 mm immature ears) resolves cell-type diversity inc |
| `ref-science-aaa6090-f3` | 10.1126/science.aaa6090 | Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method  |
| `ref-j-tplants-2019-10-008-f1` | 10.1016/j.tplants.2019.10.008 | Once encapsulated in a droplet, cells are immediately lysed, releasing RNA that binds to primers on  |
| `ref-science-aaa6090-f1` | 10.1126/science.aaa6090 | Here, we report multiplexed errorrobust FISH (MERFISH), a single-molecule imaging method that allows |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **79 条证据对象 / 41 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 79 |
| 独立文献（DOI/PMID 去重） | 41 |
| 平均每篇证据数 | 1.93 |
| 证据类型构成 | omics/co-occurrence(51)、expression/regulation(13)、genetic perturbation(11)、protein interaction(2)、DNA binding/regulation(1)、descriptive/observational(1) |
| 主要物种 | Zea mays(41)、Oryza sativa(38)、Arabidopsis thaliana(32)、Ficus carica(11)、Solanum lycopersicum(6)、Glycine max(5) |
| 子主题覆盖 | 6 个（其中证据 <5 条的 3 个） |

因果级证据共 **14 条**，占本主题证据的 **17.7%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 12 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 图集构建与细胞类型注释

**规模**：52 条证据 / 36 篇文献。**证据构成**：omics/co-occurrence(33)、expression/regulation(10)、genetic perturbation(6)、DNA binding/regulation(1)、protein interaction(1)、descriptive/observational(1)。

**形态判断**：以组学共现为主（63%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 8 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 44 条仅支持关联。

**主要物种**：Zea mays(26)、Oryza sativa(24)、Arabidopsis thaliana(19)、Ficus carica(5)、Glycine max(4)。

**代表断言（原文摘录，未改写）**

- “Single-cell RNA-seq of root tips from two agronomically important rice cultivars (Nipponbare and Azucena) resolves major cell types including epidermis, cortex, endodermis, exoderm…” — [[rice-root-cell-types-10x]]（`10.1016/j.molp.2020.12.014`，genetic perturbation）
- “Single-cell RNA-seq of developing maize ears (1-5 mm immature ears) resolves cell-type diversity including inflorescence meristem (IM), spikelet pair meristem (SPM), spikelet meris…” — [[maize-ear-cell-types-scrna-seq]]（`10.1016/j.devcel.2020.12.015`，genetic perturbation）
- “In conclusion, single-cell transcriptome studies confirmed the importance of different cell types of the root epidermis for establishing the interaction with rhizobia, and provided…” — [[ref-erae107-f1]]（`10.1093/jxb/erae107`，protein interaction）

### 2.2 空间转录组与位置映射

**规模**：5 条证据 / 3 篇文献。**证据构成**：genetic perturbation(3)、omics/co-occurrence(2)。

**形态判断**：以遗传扰动为主（60%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 3 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 2 条仅支持关联。

**主要物种**：Ficus carica(3)、Solanum tuberosum(1)、Solanum lycopersicum(1)、Zea mays(1)、Arabidopsis thaliana(1)。

**代表断言（原文摘录，未改写）**

- “Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method that substantially increases the number of RNA species that can be simultaneousl…” — [[ref-science-aaa6090-f3]]（`10.1126/science.aaa6090`，genetic perturbation）
- “Future research will focus on the novel genes that are only highlighted in single-cell spatial transcriptomics and their underlying working mechanisms, providing clues to engineer …” — [[dpdf-10-1038-s41477025-02181-9-f3]]（`10.1038/s41477-025-02181-9`，omics/co-occurrence）
- “In summary, we generated a high-quality spatial transcriptome cell atlas of tomato callus during shoot regeneration.” — [[ref-pnas-2310163120-f6]]（`10.1073/pnas.2310163120`，omics/co-occurrence）

### 2.3 发育轨迹与拟时序推断

**规模**：3 条证据 / 3 篇文献。**证据构成**：omics/co-occurrence(3)。

**形态判断**：以组学共现为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Plant (unspecified)(1)、Arabidopsis thaliana(1)、Ficus carica(1)。

**代表断言（原文摘录，未改写）**

- “We show in this work that optimal transport can be applied in a natural way to the case of a single stationary snapshot, further establishing optimal transport as a widely applicab…” — [[ref-journal-pcbi-1009466-f4]]（`10.1371/journal.pcbi.1009466`，omics/co-occurrence）
- “To move from descriptive toward predictive trajectory models, additional information is required to constrain the space of possible dynamics that could give rise to the same trajec…” — [[ref-s41587-020-0591-3-f3]]（`10.1038/s41587-020-0591-3`，omics/co-occurrence）
- “The ordering in ‘‘pseudotime’’ identified genes with switch-like behavior that are crucial for muscle differentiation (Trapnell et al., 2014).” — [[ref-j-molcel-2015-04-005-f4]]（`10.1016/j.molcel.2015.04.005`，omics/co-occurrence）

### 2.4 技术平台与建库方法

**规模**：5 条证据 / 3 篇文献。**证据构成**：omics/co-occurrence(3)、DNA binding/regulation(1)、descriptive/observational(1)。

**形态判断**：以组学共现为主（60%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 4 条仅支持关联。

**主要物种**：Zea mays(2)、Oryza sativa(2)、Arabidopsis thaliana(2)、Glycine max(1)。

**代表断言（原文摘录，未改写）**

- “Validation of the obtained protoplast is required to determine the composition of retrieved cell types; this could be performed by quantitative real-time PCR analysis to determine …” — [[cr-annurev-arplant-0817-f5]]（`10.1146/annurev-arplant-081720-010120`，DNA binding/regulation）
- “Integrative analysis of snATAC-seq and scRNA-seq data demonstrates that cell-type-specific gene expression is significantly associated with differential chromatin accessibility at …” — [[differential-accessibility-regulates-cell-type-expression]]（`10.1016/j.molp.2021.01.001`，omics/co-occurrence）
- “We conclude that the snRNA-Seq studies identified at least three different outer integument cell types: hourglass, parenchyma vascular, and parenchyma thick-walled cells ( Fig.” — [[b5-QQGRDlevUx_vfZRV-iYuwA-f3]]（`10.1073/pnas.2416987121`，omics/co-occurrence）

### 2.5 细胞类型特异性胁迫与免疫响应

**规模**：3 条证据 / 3 篇文献。**证据构成**：omics/co-occurrence(3)。

**形态判断**：以组学共现为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Solanum tuberosum(1)、Triticum aestivum(1)、Oryza sativa(1)、Zea mays(1)。

**代表断言（原文摘录，未改写）**

- “This study provides not only a global view of maize cell fate determination during root development but also insights into the immune regulatory networks in major cell types of mai…” — [[ref-pbi-14097-f1]]（`10.1111/pbi.14097`，omics/co-occurrence）
- “Infestans interface proposed on the basis of the single-cell atlas: PTCs initiate defence via cell wall reinforcement while SPCs amplify immune signals, probably through intercellu…” — [[dpdf-10-1038-s41477025-02181-9-f4]]（`10.1038/s41477-025-02181-9`，omics/co-occurrence）
- “Cell-Type-Specific and Variety-Specific Responses to Salt Stress in Wheat Root Revealed by Single-Cell Transcriptomics” — [[ev-41133438-01]]（`10.1038/s41586-025-08941-z`，omics/co-occurrence）

### 2.6 细胞间通讯与信号推断

**本知识库当前无归属证据**（子主题已定义但未被任何证据命中）。这是覆盖缺口，不是“该方向不重要”。

### 2.7 多组学整合与调控网络

**规模**：6 条证据 / 4 篇文献。**证据构成**：omics/co-occurrence(5)、descriptive/observational(1)。

**形态判断**：以组学共现为主（83%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Oryza sativa(3)、Zea mays(3)、Triticum aestivum(2)、Arabidopsis thaliana(1)。

**代表断言（原文摘录，未改写）**

- “This study provides not only a global view of maize cell fate determination during root development but also insights into the immune regulatory networks in major cell types of mai…” — [[ref-pbi-14097-f1]]（`10.1111/pbi.14097`，omics/co-occurrence）
- “Integrative analysis of snATAC-seq and scRNA-seq data demonstrates that cell-type-specific gene expression is significantly associated with differential chromatin accessibility at …” — [[differential-accessibility-regulates-cell-type-expression]]（`10.1016/j.molp.2021.01.001`，omics/co-occurrence）
- “Large-scale profiling of TF-binding sites using ampDAP-seq The transcriptomic identities of cell clusters are largely defined by their underlying gene regulatory networks (GRNs), i…” — [[ref-s41467-023-44369-7-f4]]（`10.1038/s41467-023-44369-7`，omics/co-occurrence）

## 3. 可直接引用的因果级证据（自动筛选）

以下 14 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[b3-G2N-JJNNVwoyPpAiZEWa8w-f6]] | `10.1093/plcell/koaa060` | genetic perturbation | In summary, our single-cell RNA-sequencing analysis provides a wide range of information into the leaf vasculature and t… |
| [[cr-annurev-arplant-0817-f4]] | `10.1146/annurev-arplant-081720-010120` | genetic perturbation | Multiplexing Using Lipid-Tagged Indices for single-cell and single-nucleus RNA-seq (MULTI-Seq) uses lipid-or cholesterol… |
| [[cr-annurev-arplant-0817-f5]] | `10.1146/annurev-arplant-081720-010120` | DNA binding/regulation | Validation of the obtained protoplast is required to determine the composition of retrieved cell types; this could be pe… |
| [[maize-ear-cell-types-scrna-seq]] | `10.1016/j.devcel.2020.12.015` | genetic perturbation | Single-cell RNA-seq of developing maize ears (1-5 mm immature ears) resolves cell-type diversity including inflorescence… |
| [[ref-erae107-f1]] | `10.1093/jxb/erae107` | protein interaction | In conclusion, single-cell transcriptome studies confirmed the importance of different cell types of the root epidermis … |
| [[ref-erae107-f4]] | `10.1093/jxb/erae107` | protein interaction | Another scRNA-seq study reported that a significant portion of Toll/interleukin-1 receptor/resistance protein-NLRs (TIR-… |
| [[ref-ijms23094497-f2]] | `10.3390/ijms23094497` | genetic perturbation | Starting from dissociating target cells from the tissue, cell isolation, RNA extraction, cDNA synthesis by reverse trans… |
| [[ref-j-tplants-2019-10-008-f1]] | `10.1016/j.tplants.2019.10.008` | genetic perturbation | Once encapsulated in a droplet, cells are immediately lysed, releasing RNA that binds to primers on the bead surface whe… |
| [[ref-science-1153795-f5]] | `10.1126/science.1153795` | genetic perturbation | (E) DREB2A overexpression (OE) targets tend to be regulated in multiple cell types by salt. |
| [[ref-science-aaa6090-f1]] | `10.1126/science.aaa6090` | genetic perturbation | Here, we report multiplexed errorrobust FISH (MERFISH), a single-molecule imaging method that allows thousands of RNA sp… |
| [[ref-science-aaa6090-f2]] | `10.1126/science.aaa6090` | genetic perturbation | Here, we report multiplexed error-robust fluorescence in situ hybridization (MERFISH), a single-molecule imaging approac… |
| [[ref-science-aaa6090-f3]] | `10.1126/science.aaa6090` | genetic perturbation | Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method that substantially i… |
| [[ref-science-aav6428-f6]] | `10.1126/science.aav6428` | genetic perturbation | We found that marker genes up-regulated during early meiotic prophase reached expression levels comparable with that of … |
| [[rice-root-cell-types-10x]] | `10.1016/j.molp.2020.12.014` | genetic perturbation | Single-cell RNA-seq of root tips from two agronomically important rice cultivars (Nipponbare and Azucena) resolves major… |

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **未被覆盖的子主题 1 个**：细胞间通讯与信号推断。这些方向在本库中没有可引用证据，任何涉及它们的论述都必须另行检索。
- **证据单薄的子主题 2 个**：发育轨迹与拟时序推断 3 条、细胞类型特异性胁迫与免疫响应 3 条（各 <5 条，单篇论文即可左右结论）。
- **未能归入任何子主题的证据 20 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。
- **单篇证据物种 5 个**（Daucus carota、Populus spp.、Camellia sinensis、Plant (unspecified)、Physcomitrium patens…）：跨物种外推缺乏支撑。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
