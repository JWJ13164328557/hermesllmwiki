---
title: "代谢与天然产物 — Synthesis"
created: 2026-06-01
total_evidence: 271
total_papers: 89
library_papers: 858  # 全库按themes归类该主题文献数
type: synthesis
body_status: legacy-prose
tags: [synthesis, metabolism]


soybean_relevance: ⭐中
---

# 代谢与天然产物 知识综合

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 271 | 本主题归属的证据对象数 |
| 独立论文 | 89 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 3.04 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 43% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(109)、Solanum lycopersicum(84)、Zea mays(74)、Oryza sativa(65)、Plant (unspecified)(42)、Malus domestica(30) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 185；protein interaction 28；genetic perturbation 26；DNA binding/regulation 24；phenotypic/association 6；omics/co-occurrence 2 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `the-slgras9slzhd17-transcriptional-cascade-regulates-chlorop-f8` | 10.1111/nph.19530 |  Combined genome-wide transcriptomic proﬁling and promoter-binding experiments unveiled a |
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
| expression/regulation | 185 | 表达相关（转录组/qPCR，不能单独推因果） |
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

## 范围
本页当前登记 271 条证据对象、89 篇文献（统计于 2026-11-03；子主题正文为历史人工/LLM 文本，未由本次证据重建）。涵盖植物初生与次生代谢通路，包括类黄酮/花青素、苯丙烷/木质素、萜类/类胡萝卜素、生物碱、脂质/蜡质、淀粉/糖、细胞壁多糖等代谢分支的转录调控与代谢物谱。

## 子主题

### 类黄酮与花青素生物合成
约 40 篇相关文献
- **MBW 复合体 (MYB-bHLH-WD40)** 是类黄酮/花青素合成的核心调控模块：FaMYB5 作为 R2R3-MYB 激活子调控草莓花青素与原花青素组成；CmNAC25 靶向 CmMYB6 正调控甜瓜花青素积累；EsMYB90 显著提升多种类黄酮代谢物水平
- AtbHLH113 与 PAP1/MYB75 互作调控拟南芥花青素生物合成
- MYB30 与 MYB75 形成复合体但不直接互作，RHA2B 介导的 MYB30 降解促进 MYB75 调控的花青素合成
- 多组学整合（转录组+代谢组）揭示类黄酮途径在不同物种/组织中的保守与分化调控机制
- 光质与 UV-B 通过 ZmCRYs 调控 UV-B 保护性类黄酮化合物的合成

### 木质素、纤维素与细胞壁
约 15 篇相关文献
- 生长素 (NAA) 通过 **PbrARF13-PbrNSC-PbrMYB132** 级联抑制梨果实石细胞中木质素与纤维素合成
- PbrARF13 直接结合 PbrNSC 启动子；PbrNSC 正调控 PbrMYB132 表达；PbrMYB132 过表达/敲低分别增加/减少石细胞含量
- PbrMYB24 不仅直接激活木质素和纤维素合成基因的转录，还参与更广泛的次生壁调控网络
- 香蕉 MaNAC1 激活次生细胞壁沉积
- 苯丙烷通路是木质素单体的上游来源，与类黄酮途径共享前体

### 萜类与类胡萝卜素
约 8 篇相关文献
- 番茄中两个 APETALA2 家族成员组成的转录级联调控类胡萝卜素生物合成
- 柑橘冷藏期间生育酚积累及其转录调控
- 生姜基因组揭示 6-姜辣素（萜类衍生物）生物合成进化
- 薄荷呋喃等单萜类化合物具有物种特异性调控

### 苯丙烷与酚类
约 10 篇相关文献
- AcbHLH144 转录因子负调控酚类生物合成，调节菠萝内部褐变
- 酚类化合物谱与转录组的综合分析揭示类黄酮在不同物种子叶绿化中的作用
- 苯丙烷代谢是连接初生代谢（莽草酸途径）与次生代谢的关键节点

### 脂质与蜡质
约 6 篇相关文献
- 种子油脂生物合成的综合调控网络
- 玉米 ZmCRY1 调控表皮蜡质合成相关基因的转录
- 野生大豆种子发育的时空转录组与代谢组图谱揭示油脂积累动态

### 生物碱与氨基酸
约 5 篇相关文献
- 喜树碱生物合成中的细胞特异性表达与细胞区室化调控
- 长春花 (Catharanthus roseus) 萜类吲哚生物碱途径的细胞类型特异性
- 青蒿素生物合成中的腺毛细胞特异性转录调控

### 淀粉与糖代谢
约 8 篇相关文献
- PpbZIP44 调控梨果实碳水化合物代谢、氨基酸和类黄酮积累
- 光呼吸与气孔行为及发育的关联涉及糖代谢信号
- miR156a-StSPL9 模块在碳代谢分配中发挥调节作用

### 激素交叉调控
约 10 篇相关文献
- 生长素信号 (ARF) 直接调控次生代谢（如 PbrARF13 → 木质素/纤维素）
- 茉莉酸甲酯 (MeJA) 广泛诱导萜类、生物碱和苯丙烷类代谢物积累
- 乙烯与类胡萝卜素、花青素积累存在交叉调控
- 光信号 (CRYs) 与激素信号在代谢调控中汇聚

## 共识发现

1. **MBW 转录复合体是类黄酮代谢的通用主调控器** — 多条证据在草莓、甜瓜、拟南芥、梨等多个物种中验证了 MYB-bHLH-WD40 复合体对花青素和原花青素合成的核心调控作用

2. **生长素通过 ARF-NSC-MYB 级联抑制次生壁合成** — 梨果实石细胞中发现的 PbrARF13-PbrNSC-PbrMYB132 模块为激素调控细胞壁代谢提供了完整机制框架

3. **多组学整合是当前代谢研究的主流方法** — 几乎所有近期文献均采用转录组+代谢组的联合分析策略，KEGG 富集分析显示差异代谢物主要富集于代谢通路和次生代谢物合成

4. **苯丙烷途径是初生与次生代谢的关键分叉点** — 磷酸烯醇式丙酮酸 (PEP) 和赤藓糖-4-磷酸 (E4P) 经莽草酸途径进入苯丙烷代谢，下游分支为类黄酮和木质素两条主要路径

5. **CRISPR/Cas9 验证和瞬时表达系统成为调控机制验证的标准手段** — 多个研究通过过表达/敲低实验确认了转录因子的功能

## 知识空白与争议

1. **MBW 复合体如何实现细胞类型和发育阶段特异性调控** — 虽然 MBW 复合体在多种物种中保守，但其在不同细胞类型中激活不同靶基因的机制尚不清晰

2. **激素信号与特化代谢之间的完整信号链路缺失** — 激素（如 MeJA、乙烯）诱导次生代谢物积累的中间信号组分和转录级联尚未完全阐明

3. **代谢流 (metabolic flux) 在转录调控下的动态变化** — 目前研究多停留在转录水平和代谢物稳态水平，缺乏对代谢通路流量的实时测量

4. **天然产物生物合成中的细胞区室化与转运机制** — 喜树碱、长春碱等复杂生物碱的跨细胞器和跨细胞转运机制所知甚少

5. **从转录调控网络到代谢工程预测的鸿沟** — 能否仅基于转录网络预测代谢工程改造的效果仍是一个开放问题

## 与大豆节间光质项目关联

本主题与大豆节间光质响应项目在多个代谢层面存在交叉。首先，**类黄酮和花青素途径**是光质（特别是 UV-B 和蓝光）响应的核心代谢输出——ZmCRYs 调控 UV-B 保护性化合物的合成机制提示大豆节间中可能存在类似的 CRY 介导的光质-类黄酮调控通路。野生大豆种子发育的时空代谢组研究为大豆代谢物分析提供了方法学参考。

其次，**木质素和细胞壁多糖代谢**与节间伸长和机械强度直接相关。生长素信号通过 ARF-NSC-MYB 级联调控次生壁合成的机制可能在大豆节间光质响应中同样适用——不同光质（红光/远红光/蓝光）通过改变生长素分布和信号传导，进而影响节间细胞的木质素沉积和纤维素合成，最终决定节间长度和抗倒伏性。

此外，**淀粉与糖代谢**为光质调控节间生长提供能量和碳骨架基础。光合产物分配和糖信号（如 SnRK1 通路）在不同光质条件下可能调节节间碳代谢流方向，影响是走向结构多糖（细胞壁）还是储存化合物。

## 核心基因
| 基因 | 证据数 | 功能角色 |
|------|--------|---------|
| PbrARF13 | 6 | 生长素响应因子，负调控梨石细胞木质素/纤维素合成 |
| PbrNSC | 8 | PbrARF13 下游靶基因，正调控次生壁合成 |
| PbrMYB132 | 5 | MYB 转录因子，直接激活木质素/纤维素合成基因 |
| PbrMYB24 | 7 | R2R3-MYB，激活木质素/纤维素合成并参与次生壁网络 |
| FaMYB5 | 5 | R2R3-MYB 激活子，调控草莓花青素和原花青素 |
| EsMYB90 | 4 | MYB 因子，显著提升多种类黄酮代谢物水平 |
| CmNAC25 | 4 | NAC 转录因子，靶向 CmMYB6 正调控花青素合成 |
| CmMYB6 | 4 | CmNAC25 下游靶标，花青素合成调控 |
| MaNAC1 | 4 | NAC 转录因子，激活香蕉次生细胞壁沉积 |
| AcbHLH144 | 7 | bHLH 因子，负调控酚类生物合成 |
| PpbZIP44 | 7 | bZIP 转录因子，调控碳水化合物、氨基酸和类黄酮 |
| ZmCRY1 | 3 | 蓝光受体，调控 UV-B 保护性化合物和蜡质合成 |
| miR156a | 3 | miRNA，通过 StSPL9 模块调控代谢分配 |
| MYB75/PAP1 | 5 | 拟南芥花青素调控核心 MYB 因子 |

## 代表性文献 (Top 10)
1. [[auxin-inhibits-lignin-and-cellulose-biosynthesis]] — 揭示生长素通过 PbrARF13-PbrNSC-PbrMYB132 级联抑制梨果实木质素和纤维素合成的完整机制
2. [[a-novel-r2r3myb-transcription-factor-famyb5]] — FaMYB5 正调控栽培草莓花青素和原花青素生物合成
3. [[cmnac25-targets-cmmyb6-to-positively-regulate]] — CmNAC25 靶向 CmMYB6 正调控甜瓜采后花青素生物合成
4. [[integrated-metabolomic-and-transcriptomic-analysis-reveals]] — EsMYB90 通过调控类黄酮途径显著提升多种代谢物水平
5. [[the-transcription-factor-pbrmyb24-regulates-lignin]] — PbrMYB24 直接激活木质素和纤维素合成基因转录
6. [[a-transcriptional-cascade-mediated-by-two]] — AP2 家族成员转录级联调控番茄类胡萝卜素生物合成
7. [[zmcry1-gl2-wax-maize]] — 玉米隐花色素调控 UV-B 保护性化合物和蜡质合成
8. [[acbhlh144-transcription-factor-negatively-regulates-phenolic]] — AcbHLH144 负调控酚类生物合成调节菠萝褐变
9. [[b5-EshzCwiRQQAcBvprSyR5VA]] — 野生大豆种子发育的时空转录组与代谢组图谱
10. [[rha2b-mediated-myb30-degradation-facilitates-myb75-regulated]] — RHA2B 介导 MYB30 降解促进 MYB75 调控的花青素合成
