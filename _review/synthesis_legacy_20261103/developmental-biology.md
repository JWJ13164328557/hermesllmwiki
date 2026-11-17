---

title: "发育生物学 — Synthesis"
created: 2026-06-01
total_evidence: 224
total_papers: 48
library_papers: 779  # 全库按themes归类该主题文献数
type: synthesis
body_status: legacy-prose
tags: [synthesis, development]


soybean_relevance: ⭐高
---

# 发育生物学 知识综合

<!-- AUTO-EVIDENCE-STRENGTH:START -->

## 证据覆盖与强度（自动统计，可复算）

| 指标 | 值 | 读法 |
|---|---|---|
| 证据条目 | 224 | 本主题归属的证据对象数 |
| 独立论文 | 48 | 去重后的 PMID/DOI 数 |
| 平均每篇证据数 | 4.67 | <1.0 说明多数论文只贡献 1 条结论 |
| 单条证据论文占比 | 25% | 越高说明"每篇论文一个结论"，系统性弱 |
| 主要物种 | Arabidopsis thaliana(186)、Oryza sativa(95)、Zea mays(73)、Nicotiana tabacum(44)、Citrus spp.(32)、Solanum lycopersicum(21) | 物种过度集中则外推性受限 |
| 证据类型 | expression/regulation 172；protein interaction 21；genetic perturbation 19；DNA binding/regulation 6；omics/co-occurrence 5；phenotypic/association 1 | 表达/关联类居多时，因果结论需打折扣 |

> 归属依据：`themes.py` 标签别名表（高置信）+ 关键词兜底（低置信）。本段由脚本生成，不构成结论；结论性文字须回原文核对。

### 可复核证据索引（前 12 条，按断言长度）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-s13007-019-0417-9-f4` | 10.1186/s13007-019-0417-9 | Focusing on the TA zone data (positions 2–15), we found significant differences in tissue- |
| `ref-s13059-021-02537-2-f5` | 10.1186/s13059-021-02537-2 | We found that the suberin biosynthetic gene, ASFT (ALIPHATIC SUBERIN FERULOYL TRANSFERASE) |
| `ref-j-molp-2026-03-005-f3` | 10.1016/j.molp.2026.03.005 | Molecular Plant 19, 1019–1035, May 4 2026 1021 WIND1 controls cell fate transition Molecul |
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication compl |
| `ref-s41586-018-0839-y-f2` | 10.1038/s41586-018-0839-y | Our data establish that during root procambial development there exists a network in which |
| `ref-15592324-2020-1820681-f1` | 10.1080/15592324.2020.1820681 | Combination of 0.5 µM TSA and 200 µM SB had no apparent effect on wheat regeneration effic |
| `ms-10-3390_cells15121049-f1` | 10.3390/cells15121049 | The sex-specific maternally or paternally inherited DNA marks at imprinted genes are essen |
| `ref-j-pbi-2019-09-003-f2` | 10.1016/j.pbi.2019.09.003 | CYCD6;1 is required for the division of cortex/endodermis initial cells and their progenit |
| `ref-science-1146265-f1` | 10.1126/science.1146265 | With a computational pipeline we developed to analyze this immense data set, we show the o |
| `ref-ppl-13651-f2` | 10.1111/ppl.13651 | The role of ROS, particularly in signal transduction under drought stress, is well studied |
| `ref-j-pbi-2011-10-008-f7` | 10.1016/j.pbi.2011.10.008 | Function of WUS in stem cell homeostasis: molecular perspective WUS-mediated transcription |
| `ref-j-tig-2017-05-002-f6` | 10.1016/j.tig.2017.05.002 | While it has been shown that SHR-SCR can bind to JACKDAW and MAGPIE (and may be required t |

### 证据语义分层

| 证据类型 | 条目数 | 可支持的推断强度 |
|---|---:|---|
| genetic perturbation | 19 | 遗传因果（扰动后表型/表达改变） |
| protein interaction | 21 | 物理互作（Co-IP/Y2H/BiFC/pull-down） |
| DNA binding/regulation | 6 | 直接调控（ChIP/EMSA/启动子报告） |
| expression/regulation | 172 | 表达相关（转录组/qPCR，不能单独推因果） |
| phenotypic/association | 1 | 表型关联（GWAS/QTL/自然变异/田间） |
| omics/co-occurrence | 5 | 组学共现（单细胞簇/共表达网络，非调控） |

> 读法：`genetic perturbation` 才是因果证据；`expression/regulation` 与 `omics/co-occurrence` 只能提出假说，不能证明调控或因果。

### 遗传扰动类证据（关键词命中，前 5 条；需回原文核实实验设计）

| 证据 ID | DOI | 断言（截断） |
|---|---|---|
| `ref-tab-0120-f2` | 10.1199/tab.0120 | Overexpression of CDC6 or CDT1, E2F targets encoding subunits of the pre-replication complex are suf |
| `ref-ppl-13651-f3` | 10.1111/ppl.13651 | The coexpression network analysis between OsERF48 and root-specific overexpression of ERF48 root RNA |
| `ref-nrm3790-f4` | 10.1038/nrm3790 | Inducible overexpression of PLT1 or PLT2 is sufficient for the formation of ectopic root stem cell n |
| `ref-pnas-2201350119-f8` | 10.1073/pnas.2201350119 | Consistent with this, our transcriptome analysis identified that ROS homeostasis and cell wall-modif |
| `ref-j-pbi-2013-11-011-f1` | 10.1016/j.pbi.2013.11.011 | Expression of both PIN1 and DR5 diminishes in lfy mutant floral primordia, increases after inducible |

### 正文状态

> 本页子主题正文为历史人工/LLM 文本，**未由本次证据重建**；只有本自动段与 frontmatter 计数反映当前证据快照。正文中的机制性表述须逐条回到原始研究核对，不得仅凭本页引用。

<!-- AUTO-EVIDENCE-STRENGTH:END -->

## 范围
本页当前登记 224 条证据对象、48 篇文献（统计于 2026-11-03；子主题正文为历史人工/LLM 文本，未由本次证据重建）。涵盖植物发育的核心过程，包括根发育与再生、维管形成层与次生生长、分生组织维持、细胞命运决定、胚胎发生及光/激素信号调控，涉及拟南芥、水稻、玉米、杨树、番茄等多个模式与作物物种。

## 子主题

### 根发育与再生
约 60 篇相关文献
- 愈伤组织在转录组层面类似于根尖分生组织，即使来源于地上部组织也同样呈现根端特征（ev-20230752）
- 拟南芥叶片外植体离体根从头发生依赖于内源生长素的极性运输与不对称分布（ref-erw213）
- 根尖切除后，邻近细胞中生长素被特异性激活，启动干细胞微环境的分子与功能重建（ref-pnas-2003346117, ref-nature07597）
- ERF115–PAT1 转录因子复合体在干细胞微环境完全恢复中发挥关键作用（ref-nplants-2016-165）
- miR165/6 在根部分生组织中转录后限制 PHB 的表达域，调控根尖辐射状模式建成（ref-nature08977）
- 中柱鞘细胞的局部径向扩张对于侧根原基正确定位是必需的（ref-pnas-1820882116）
- 光照条件下根尖细胞周期中位时间缩短至约 12.57 小时，显著快于黑暗条件（ref-s13007-019-0417-9）

### 维管发育与次生生长
约 45 篇相关文献
- AtHB8 标记木质部导管分子前体，S17 标记韧皮部筛分子前体，二者可在单细胞分辨率下区分维管细胞谱系（cr-10-1242-dev-106104）
- 蓝光受体隐花色素 CRY1 过表达导致杨树形成层区细胞层数显著减少，表明光质直接参与维管形成层活性的调控（blue-light-photoreceptor-cryptochrome-1）
- PXY/TMO5 信号模块调控原形成层/形成层中木质部与韧皮部的比例平衡（ref-pp-18-00463）
- 开发了在木质部中选择性抑制靶基因转录的方法，实现维管细胞类型特异的遗传操作（ev-33822225）
- 对杨树初生到次生生长转变过程中主要细胞类型进行了系统解剖学鉴定和功能表征（ref-j-molp-2023-03-005）

### 分生组织与干细胞维持
约 40 篇相关文献
- 拟南芥营养期茎尖分生组织的单细胞转录组分析揭示了不同功能域的细胞异质性（arabidopsis-sam-scrna）
- 静止中心细胞通过第三代测序技术实现单细胞转录组分析，鉴定出维持干细胞微环境的关键调控因子（b3-yRRSlByPuOxXKvXBl0_LZg）
- 植物细胞具有广泛的发育可塑性，分化的体细胞在合适条件下可重新获得干细胞属性并完成整个器官再生（ref-nature07597）

### 细胞命运决定与再生
约 50 篇相关文献
- WIND1 是控制细胞命运转变的关键转录因子，在愈伤组织形成和芽再生中起核心开关作用（ref-j-molp-2026-03-005）
- 创伤诱导的愈伤组织形成通路与激素诱导的通路在分子机制上不同，表明伤口信号是独立的再生触发因素（ref-j-cub-2011-02-020）
- PIN1 蛋白在细胞中的极性定位总是朝向未来细胞扩张的方向，建立生长素流动方向以预测器官发生位点（ref-j-pbi-2009-11-001）
- 玉米根发育过程中的细胞命运决定在单细胞分辨率下被全局性描述，鉴定了各发育轨迹的关键调控因子（ref-pbi-14097）
- 愈伤组织诱导涉及细胞分裂、胁迫响应和内源信号（包括跨膜转运）等多类基因的协同激活（ref-j-molp-2021-05-028）

### 胚胎发生
约 20 篇相关文献
- 植物胚胎发育呈现"沙漏"模式——早期和晚期物种间转录组差异较大，而中间阶段高度保守，为进化发育生物学提供新证据（b4-tQ-g_5fH-4YwC8OyEwkrYg）

### 光信号与发育调控
约 30 篇相关文献
- 蓝光受体 CRY1 不仅调控下胚轴伸长，还直接影响维管形成层活性和次生细胞壁沉积
- 光照通过加速根尖分生组织细胞分裂速率来促进根生长，建立了光-细胞周期-发育的直接联系
- 成熟与衰老叶片细胞中的基因表达比较揭示发育阶段转换受光信号和年龄信号的双重调控（ev-40764913）

## 共识发现

1. **植物细胞具有显著的发育可塑性** — 多条证据表明分化细胞可通过创伤或激素信号重新进入细胞周期并获得干细胞属性，愈伤组织本质上是异位激活的根端分生组织程序
2. **生长素的极性运输和局部积累是器官从头发生的核心驱动力** — PIN 蛋白极性定位决定生长素流方向，伤口邻近细胞中生长素的特异性激活是再生启动的关键
3. **维管发育受多种转录因子层级调控** — HD-ZIP III（如 PHB）、TMO5、PXY 等形成调控网络，miR165/6 通过转录后限制来精细化维管模式
4. **光信号不仅调控光合作用，还直接参与发育过程的时空调控** — 蓝光受体 CRY1 影响形成层活性，光照加速根尖细胞周期
5. **单细胞组学技术正在革新发育生物学研究范式** — 单细胞 RNA-seq、空间转录组学使得以细胞类型分辨率解析发育轨迹和基因调控网络成为可能

## 知识空白与争议

1. **形成层活性调控的分子机制尚未完全阐明** — 虽然已知 PXY/TMO5/WOX4 等信号通路，但光质（如 R:FR 比率）如何精确调控形成层细胞分裂与分化的平衡仍需深入研究
2. **创伤再生与正常发育程序的异同** — 愈伤组织是否完全等同于根端分生组织，还是具有独立的分子特征？不同物种和组织来源的再生能力差异的遗传基础仍不清楚
3. **从单细胞数据到功能验证的鸿沟** — 大量单细胞图谱已生成，但从中提取可验证的功能性假说并转化为作物改良策略的路径仍不成熟
4. **节间发育的纵向模式尚未被充分研究** — 茎的初生生长向次生生长的转变在纵轴（节间位置）上如何被差异化调控，目前缺乏系统研究
5. **多物种比较发育生物学的整合框架缺失** — 拟南芥中的发现如何推广到大豆、杨树等具有显著次生生长的物种？保守机制与物种特化机制的边界尚不清晰

## 与大豆节间光质项目关联

本主题与大豆节间光质响应项目高度相关。首先，维管形成层发育和次生生长是节间伸长的核心细胞学基础——蓝光受体 CRY1 已被证实直接调控杨树形成层活性，这一机制在大豆节间中是否保守是项目的关键科学问题之一。其次，光质（特别是 R:FR 比率和蓝光比例）通过光受体信号网络调控细胞分裂速率和细胞伸长方向，这与大豆节间对密植遮荫的响应直接相关。第三，多项证据表明生长素极性运输、PIN 蛋白定位与维管模式建成紧密耦合，这为理解光质如何重编程节间维管组织发育提供了分子切入点。最后，单细胞/空间转录组学方法在本主题中被广泛采用，为项目提供了可直接借鉴的技术路线和分析框架，特别是在解析节间不同组织层次（表皮、皮层、形成层、髓）对光质的差异化响应方面。

## 核心基因

| 基因 | 证据数 | 功能角色 |
|------|--------|---------|
| WIND1 | 12 | 细胞命运转变主调控因子，愈伤组织形成和芽再生的核心开关 |
| PIN1 | 10 | 生长素外流载体，极性定位决定生长素流方向和器官发生位点 |
| PHB (HD-ZIP III) | 9 | 根和维管辐射模式建成，受 miR165/6 转录后调控 |
| CRY1 | 8 | 蓝光受体，调控下胚轴伸长和形成层活性 |
| ERF115 | 7 | 干细胞微环境再生，与 PAT1 协同激活伤口响应程序 |
| PXY/TDR | 7 | 原形成层/形成层中调控细胞分裂方向与维管组织比例 |
| TMO5 | 6 | bHLH 转录因子，与 LHW 形成异源二聚体调控维管发育 |
| miR165/6 | 6 | 转录后限制 HD-ZIP III 表达域，精细化维管和根辐射模式 |
| SGR6 | 3 | 液泡相关蛋白，参与细胞膨大和器官大小调控 |
| SKP2B | 3 | F-box 蛋白，调控细胞周期进程和核内复制 |

## 代表性文献 (Top 10)

1. [[ref-j-molp-2026-03-005]] — WIND1 控制细胞命运转变的分子机制，是愈伤组织形成和植物再生的核心调控因子
2. [[ref-nature08977]] — miR165/6 通过限制 PHB 表达域调控根和维管的辐射状模式建成
3. [[ref-pnas-2003346117]] — 揭示根尖伤口邻近细胞中生长素的特异性激活是再生启动的分子基础
4. [[ref-nature07597]] — 证明分化植物细胞保留完整的器官再生能力，干细胞属性在损伤后被重新激活
5. [[ref-j-cub-2011-02-020]] — 发现创伤诱导愈伤组织形成的分子通路独立于激素诱导通路
6. [[ref-nplants-2016-165]] — ERF115–PAT1 复合体在根干细胞微环境重建中的核心功能
7. [[blue-light-photoreceptor-cryptochrome-1-promotes]] — 蓝光受体 CRY1 直接影响杨树形成层区细胞层数和次生生长
8. [[ref-pp-18-00463]] — PXY/TMO5 信号模块在原形成层发育中调控木质部与韧皮部比例的机制
9. [[ref-pbi-14097]] — 单细胞分辨率下玉米根发育过程中细胞命运决定的全局图谱
10. [[arabidopsis-sam-scrna]] — 拟南芥营养期茎尖分生组织单细胞分析揭示功能域异质性
