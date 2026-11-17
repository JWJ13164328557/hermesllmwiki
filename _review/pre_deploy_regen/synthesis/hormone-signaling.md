---

title: "激素与信号转导 — Synthesis"
created: 2026-06-01
total_evidence: 141
total_papers: 52
library_papers: 473  # 全库按themes归类该主题文献数
type: synthesis
body_status: rebuilt-2026-11-03
tags: [hormone, signaling, synthesis]
legacy_archive: _review/synthesis_legacy_20261103/hormone-signaling.md
rebuild_rule: evidence-fields-only; no-cross-evidence-inference

---
# 激素与信号转导 知识综合（证据重建版）

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 141 | 本主题归属的证据对象数 |
| 独立论文 | 52 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 2.71 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 63% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(77)、Zea mays(64)、Oryza sativa(59)、Solanum lycopersicum(32)、Citrus spp.(27)、Nicotiana tabacum(14) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 105；protein interaction 21；genetic perturbation 5；DNA binding/regulation 5；omics/co-occurrence 3；phenotypic/association 2 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `dpdf-10-1146-annurev-arplant-083123073106-f11` | 10.1146/annurev-arplant-083123-073106 | Beyond Auxin: Cytokinin and Ethylene Finite-element model: uses meshed geometric elements  |
| `ms-10-67693_bjcr-3jqlrcre-f7` | 10.67693/bjcr-3jqlrcre | Elaeocarpus grandiflorus callus cultures exhibited differential growth responses on MS med |
| `far-red-light-suppresses-glucosinolate-profiles-of-f4` | 10.1016/j.envexpbot.2021.104507 | The transcription factors (TFs) such as PHYTOCHROME INTERACTING FACTORs (PIFs), ELONGATED  |
| `ref-jcs-228551-f1` | 10.1242/jcs.228551 | Datasets generated using these techniques include profiles of plants enriched or depleted  |
| `ref-msb-2013-40-f2` | 10.1038/msb.2013.40 | This included xp pericycle-specific induction of pLBD33::GUS and p TMO6::GFP (TARGET OF MO |
| `ms-10-1007_s44372-026-00844-1-f7` | 10.1007/s44372-026-00844-1 | Ethylene, jasmonic acid, and brassinosteroids further fine-tune stress responses including |
| `gibberellin-biosynthesis-is-required-for-cppu-induced-f2` | 10.1093/hr/uhad084 | PbRR9-like directly activates the expression of the auxin biosynthesis gene indole-3- pyru |
| `ms-10-1038_s41467-026-77029-7-f8` | 10.1038/s41467-026-77029-7 | Results Strigolactone signaling represses FOD gene expression through BRC1 upregulation In |
| `ref-pnas-0709559105-f3` | 10.1073/pnas.0709559105 | We found a total of four cytokinin-responsive transcriptional activators (B type ARRs), fo |
| `ms-10-47191_ijmra_v9-i7-41-f3` | 10.47191/ijmra/v9-i7-41 | The mechanism behind the peptide's ability to enhance generative components is related to  |
| `comparative-transcriptome-profiling-reveals-the-multiple-f8` | 10.1111/pbi.14063 | For instance, DELLA proteins act as repressors of a central growth regulatory pathway that |
| `ref-tpc-110-073924-f1` | 10.1105/tpc.110.073924 | CLV3 is active as a 13–amino acid arabinosylated peptide that diffuses until it binds to i |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 5 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 21 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 5 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 105 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 2 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 3 | 组学共现（单细胞簇/共表达网络，非调控） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-jcs-228551-f1` | 10.1242/jcs.228551 | Datasets generated using these techniques include profiles of plants enriched or depleted in the sto |
| `biology-and-function-of-mir159-in-f2` | 10.3390/plants8080255 | Then, overexpression of miR159 in Arabidopsis [ecotype Landsberg erecta, (Ler)] resulted in down-reg |
| `10-1146-annurev-arplant-042817-f8` | 10.1146/annurev-arplant-042817 | CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged mer |
| `ref-jcs-228551-f5` | 10.1242/jcs.228551 | A change in stomatal density or pattern can be attributed to experimental manipulation of nearly all |
| `ref-science-1086391-f2` | 10.1126/science.1086391 | We found preferred sites of T-DNA integration or “hot spots,” as well as “cold spots” [Fig. |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

> 本页正文于 2026-11-03 由 `rebuild_synthesis_body.py` 从 **141 条证据对象 / 52 篇文献**确定性重建：所有陈述均可回溯到下列证据页；英文为原文摘录，未经改写；不含跨证据的推测性归纳。历史人工正文已归档至 `_review/synthesis_legacy_20261103`，不再作为本页结论来源。
>
> 阅读约定：`遗传扰动` / `蛋白互作` / `DNA 结合` 三类证据才支持“因果”或“直接调控”的表述；`表达相关` 与 `组学共现` 只能提出关联性假说。

## 1. 主题概览（自动统计）

| 指标 | 值 |
|---|---|
| 证据对象 | 141 |
| 独立文献（DOI/PMID 去重） | 52 |
| 平均每篇证据数 | 2.71 |
| 证据类型构成 | expression/regulation(105)、protein interaction(21)、genetic perturbation(5)、DNA binding/regulation(5)、omics/co-occurrence(3)、phenotypic/association(2) |
| 主要物种 | Arabidopsis thaliana(77)、Zea mays(64)、Oryza sativa(59)、Solanum lycopersicum(32)、Citrus spp.(27)、Nicotiana tabacum(14) |
| 子主题覆盖 | 7 个（其中证据 <5 条的 3 个） |

因果级证据共 **31 条**，占本主题证据的 **22.0%**。这一比例决定本主题哪些结论可以写成机制，哪些只能写成相关性。

## 2. 子主题分解（按证据重建）

> 一条证据可同时命中多个子主题（共 3 条跨组），因此各子主题计数之和大于总证据数。

### 2.1 受体感知与早期信号转导

**规模**：8 条证据 / 6 篇文献。**证据构成**：expression/regulation(6)、protein interaction(1)、genetic perturbation(1)。

**形态判断**：以表达相关为主（75%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 2 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 6 条仅支持关联。

**主要物种**：Zea mays(5)、Solanum lycopersicum(4)、Oryza sativa(4)、Arabidopsis thaliana(3)、Citrus spp.(2)。

**代表断言（原文摘录，未改写）**

- “CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged meristems and function in CLV signaling, through interactions with the RPK2 recepto…” — [[10-1146-annurev-arplant-042817-f8]]（`10.1146/annurev-arplant-042817`，genetic perturbation）
- “CLV3 is active as a 13–amino acid arabinosylated peptide that diffuses until it binds to its receptors: the LRR receptor kinase CLV1, the receptor-like kinase CLV2, and the Ser-Thr…” — [[ref-tpc-110-073924-f1]]（`10.1105/tpc.110.073924`，expression/regulation）
- “First, the effect of CLE40 is mediated by a receptor kinase unrelated to CLV1/2: ARA- BIDOPSIS CRINKLY4 (ACR4), which restricts cell division in the columella [14], is required for…” — [[ref-j-pbi-2010-08-001-f1]]（`10.1016/j.pbi.2010.08.001`，expression/regulation）

### 2.2 转录调控与激素响应基因

**规模**：16 条证据 / 9 篇文献。**证据构成**：expression/regulation(12)、protein interaction(2)、genetic perturbation(1)、omics/co-occurrence(1)。

**形态判断**：以表达相关为主（75%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 3 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 13 条仅支持关联。

**主要物种**：Solanum lycopersicum(8)、Zea mays(8)、Arabidopsis thaliana(8)、Oryza sativa(7)、Brassica napus(2)。

**代表断言（原文摘录，未改写）**

- “The transcription factors (TFs) such as PHYTOCHROME INTERACTING FACTORs (PIFs), ELONGATED HYPOCOTYL 5 (HY5), and CONSTANS (CO) play central roles in regu lating the expression of r…” — [[far-red-light-suppresses-glucosinolate-profiles-of-f4]]（`10.1016/j.envexpbot.2021.104507`，protein interaction）
- “Then, overexpression of miR159 in Arabidopsis [ecotype Landsberg erecta, (Ler)] resulted in down-regulation of MYB33 expression, which correlated with a decrease in LEAFY expressio…” — [[biology-and-function-of-mir159-in-f2]]（`10.3390/plants8080255`，genetic perturbation）
- “Koizumi K, Wu S, MacRae-Crerar A, Gallagher KL: An essential protein that interacts with endosomes and promotes movement of the SHORT–ROOT transcription factor.” — [[ref-j-pbi-2014-11-002-f7]]（`10.1016/j.pbi.2014.11.002`，protein interaction）

### 2.3 激素合成与稳态

**规模**：13 条证据 / 11 篇文献。**证据构成**：expression/regulation(11)、protein interaction(1)、omics/co-occurrence(1)。

**形态判断**：以表达相关为主（85%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 12 条仅支持关联。

**主要物种**：Arabidopsis thaliana(7)、Solanum lycopersicum(5)、Brassica napus(4)、Zea mays(2)、Citrus spp.(2)。

**代表断言（原文摘录，未改写）**

- “It is considered a vital precursor for a group of important compounds, most notably polyamines and nitric oxide, which play a pivotal role in regulating cell division and elongatio…” — [[ms-10-14719_pst-15678-f2]]（`10.14719/pst.15678`，protein interaction）
- “PbRR9-like directly activates the expression of the auxin biosynthesis gene indole-3- pyruvate monooxygenase 4 (PbYUC4) to increase the content of IAA (auxin) while directly inhibi…” — [[gibberellin-biosynthesis-is-required-for-cppu-induced-f2]]（`10.1093/hr/uhad084`，expression/regulation）
- “The 24 root cell clusters defined by scRNA-seq exhibit distinct expression patterns for hormone biosynthesis, signaling, and response genes — including auxin, cytokinin, gibberelli…” — [[root-cluster-hormone-response-patterns]]（`10.1016/j.molp.2019.04.004`，omics/co-occurrence）

### 2.4 激素间互作与权衡

**规模**：3 条证据 / 3 篇文献。**证据构成**：expression/regulation(2)、protein interaction(1)。

**形态判断**：以表达相关为主（67%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：含 1 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 2 条仅支持关联。

**主要物种**：Oryza sativa(2)、Zea mays(2)、Arabidopsis thaliana(2)、Solanum lycopersicum(1)、Vitis vinifera(1)。

**代表断言（原文摘录，未改写）**

- “The signaling molecule jasmonate plays a central role in this process, and studies indicate that the interaction between jasmonate signaling and other hormones (e.g., salicylic aci…” — [[ms-10-3389_fpls-2026-1815183-f1]]（`10.3389/fpls.2026.1815183`，protein interaction）
- “More in-depth studies found that WUS directly regulates additional cytokininand auxin-related genes, possibly controlling the balance between these two hormones, and also regulates…” — [[10-1146-annurev-arplant-042817-f3]]（`10.1146/annurev-arplant-042817`，expression/regulation）
- “The balance between the stem cell population and the differentiating daughter cells is essential to the iterative production of new leaves.” — [[ref-tpc-110-073924-f6]]（`10.1105/tpc.110.073924`，expression/regulation）

### 2.5 生长发育中的激素功能

**规模**：1 条证据 / 1 篇文献。**证据构成**：expression/regulation(1)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Oryza sativa(1)、Arabidopsis thaliana(1)、Cicer arietinum(1)。

**代表断言（原文摘录，未改写）**

- “Ethylene, jasmonic acid, and brassinosteroids further fine-tune stress responses including root growth under compacted or drying soils, growth-defence trade-offs, and stomatal and …” — [[ms-10-1007_s44372-026-00844-1-f7]]（`10.1007/s44372-026-00844-1`，expression/regulation）

### 2.6 逆境中的激素调控

**规模**：8 条证据 / 7 篇文献。**证据构成**：protein interaction(4)、expression/regulation(3)、genetic perturbation(1)。

**形态判断**：以蛋白互作为主（50%），该子主题的机制表述有一手实验支撑，但结论边界受物种与处理条件限制。

**推断上限**：含 5 条因果/直接互作级证据（遗传扰动、蛋白互作或 DNA 结合），可支持有限的机制表述；其余 3 条仅支持关联。

**主要物种**：Oryza sativa(7)、Arabidopsis thaliana(6)、Zea mays(5)、Quercus spp.(1)、Populus spp.(1)。

**代表断言（原文摘录，未改写）**

- “ABI5-ZAT10-SLAH3 module (Clefflux); CPK10/30/32 kinases (root cap) [32–36] Jasmonic Acid (JA) Positive Part of ABA-independent pathways; interacts with other hormones (ETH, SA) to …” — [[ms-10-70737_8avhs053-f7]]（`10.70737/8avhs053`，protein interaction）
- “Auxin, cytokinin, and gibberellin signaling generally decline during osmotic stress and interact with ABA, SA, ET, and JA as resources are redirected from growth toward defense.” — [[ms-10-21926_obm-genet-2603356-f6]]（`10.21926/obm.genet.2603356`，protein interaction）
- “Ethylene interacts with hormones like jasmonic acid and ABA and helps in the regulation of drought stress.” — [[ms-10-1007_s44372-026-00856-x-f2]]（`10.1007/s44372-026-00856-x`，protein interaction）

### 2.7 信号转导的定量与动态特征

**规模**：2 条证据 / 1 篇文献。**证据构成**：expression/regulation(2)。

**形态判断**：以表达相关为主（100%），该子主题当前只能回答“是否相关/在何时何处出现”，不能回答“由谁驱动”；要升级为机制结论须补扰动或互作实验。

**推断上限**：本组全部为表达/关联/描述级证据，**不支持因果或直接调控结论**；任何“X 调控 Y”的写法都必须补做扰动实验。

**主要物种**：Solanum lycopersicum(2)、Oryza sativa(2)、Zea mays(2)。

**代表断言（原文摘录，未改写）**

- “Another target gene of WUS is CLV1, but its expression is repressed by WUS, not activated as predicted by the CLV–WUS feedback model; therefore, this regulation is likely only for …” — [[10-1146-annurev-arplant-042817-f5]]（`10.1146/annurev-arplant-042817`，expression/regulation）

## 3. 可直接引用的因果级证据（自动筛选）

以下 31 条证据的实验设计属于扰动或直接互作，可作为机制论断的一手依据；引用时须核对原文的物种、组织与处理条件。

| 证据页 | DOI | 类型 | 断言（摘录） |
|---|---|---|---|
| [[10-1146-annurev-arplant-042817-f4]] | `10.1146/annurev-arplant-042817` | protein interaction | HOMEODOMAIN LEUCINE ZIPPER (HD-ZIP III) genes, whose protein products interact with the type-B RRs and bind the same WUS… |
| [[10-1146-annurev-arplant-042817-f7]] | `10.1146/annurev-arplant-042817` | protein interaction | CIKs also interact with other CLV receptors and are phosphorylated by CLV1, suggesting that they act as a direct downstr… |
| [[10-1146-annurev-arplant-042817-f8]] | `10.1146/annurev-arplant-042817` | genetic perturbation | CT2/Gα interacts with the β and γ subunits, and, indeed, Gβ mutants in Arabidopsis have enlarged meristems and function … |
| [[biology-and-function-of-mir159-in-f2]] | `10.3390/plants8080255` | genetic perturbation | Then, overexpression of miR159 in Arabidopsis [ecotype Landsberg erecta, (Ler)] resulted in down-regulation of MYB33 exp… |
| [[comparative-transcriptome-profiling-reveals-the-multiple-f7]] | `10.1111/pbi.14063` | DNA binding/regulation | Y1H and EMSA results indicated that BnaC2.FUS3 could directly bind to the P1 site of the BnaA6.KO promoter (Figure 3g,h)… |
| [[far-red-light-suppresses-glucosinolate-profiles-of-f4]] | `10.1016/j.envexpbot.2021.104507` | protein interaction | The transcription factors (TFs) such as PHYTOCHROME INTERACTING FACTORs (PIFs), ELONGATED HYPOCOTYL 5 (HY5), and CONSTAN… |
| [[ms-10-1007_s00299-026-03946-y-f4]] | `10.1007/s00299-026-03946-y` | DNA binding/regulation | Collectively, this promoter analysis revealed that NtMADS-box family genes are extensively involved in mediating plant h… |
| [[ms-10-1007_s44372-026-00675-0-f3]] | `10.1007/s44372-026-00675-0` | protein interaction | Discover Plants (2026) 3:227 5 Conclusion This study demonstrates that indirect organogenesis in Ficus lyrata can be eff… |
| [[ms-10-1007_s44372-026-00856-x-f2]] | `10.1007/s44372-026-00856-x` | protein interaction | Ethylene interacts with hormones like jasmonic acid and ABA and helps in the regulation of drought stress. |
| [[ms-10-14719_pst-15678-f2]] | `10.14719/pst.15678` | protein interaction | It is considered a vital precursor for a group of important compounds, most notably polyamines and nitric oxide, which p… |
| [[ms-10-21926_obm-genet-2603356-f6]] | `10.21926/obm.genet.2603356` | protein interaction | Auxin, cytokinin, and gibberellin signaling generally decline during osmotic stress and interact with ABA, SA, ET, and J… |
| [[ms-10-33545_2618060x-2026-v9-i9sa-6455-f1]] | `10.33545/2618060x.2026.v9.i9sa.6455` | protein interaction | Ethylene interacts with auxin and other hormonal pathways to regulate cell division, root primordium initiation and subs… |
| [[ms-10-3389_ffgc-2026-1818494-f2]] | `10.3389/ffgc.2026.1818494` | protein interaction | Hormonal regulation associated with apical dominance—particularly auxin–cytokinin–strigolactone interactions—also plays … |
| [[ms-10-3389_fpls-2026-1815183-f1]] | `10.3389/fpls.2026.1815183` | protein interaction | The signaling molecule jasmonate plays a central role in this process, and studies indicate that the interaction between… |
| [[ms-10-3389_fpls-2026-1897976-f2]] | `10.3389/fpls.2026.1897976` | protein interaction | Fine-tuning of this balance is achieved through ROS-dependent signaling cascades that interact with phytohormones such a… |

（另有 16 条未列出，可在 `evidence/` 按 evidence_type 过滤。）

## 4. 张力与矛盾（自动检测）

在当前证据集上未检出方向性冲突。注意：这只说明“没有互相矛盾的摘录”，不说明领域内不存在争议——多数争议需要全文级的实验条件比对才能发现。

## 5. 覆盖缺口（由证据分布直接导出）

- **证据单薄的子主题 3 个**：激素间互作与权衡 3 条、生长发育中的激素功能 1 条、信号转导的定量与动态特征 2 条（各 <5 条，单篇论文即可左右结论）。
- **未能归入任何子主题的证据 93 条**：多为方法描述或跨领域摘录，已计入主题总量但未参与分组。
- **单篇证据物种 10 个**（Plant (unspecified)、Picea spp.、Vaccinium spp.、Rosa spp.、Fragaria × ananassa…）：跨物种外推缺乏支撑。

## 6. 历史正文说明

本页 2026-11-03 之前的正文为人工/LLM 撰写，未与证据逐条对齐，含不可核的行内断言缺引用、格式残留与跨主题内容混入。该正文已原样归档至 `_review/synthesis_legacy_20261103`，保留供追溯，**不得再作为结论来源**。原“与大豆项目关联”的定性判断保留在 frontmatter 的 `soybean_relevance` 字段，其论证过程同样需重新取证。
