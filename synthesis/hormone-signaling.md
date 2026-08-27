---

title: "激素与信号转导 — Synthesis"
created: 2026-06-01
total_evidence: 47
total_papers: 33
type: synthesis
tags: [hormone, signaling, synthesis]

---

# 激素与信号转导知识综合

## 范围
基于 309 条证据对象，覆盖 108 篇文献（2026-06-01 导入），涵盖生长素、细胞分裂素、油菜素内酯、赤霉素、脱落酸、茉莉酸、乙烯、水杨酸八大经典激素通路及光信号转导、磷酸化级联与泛素-蛋白酶体降解等交叉信号模块。

---

## 子主题结构

### 1. 生长素 (Auxin) — 细胞命运与器官建成的空间坐标

**证据数量**: 约 19 条

#### 合成与极性运输
- 生长素合成基因（*YUC* 家族）在根分生组织细胞中富集表达，basipetal 运输是干细胞补充的必要条件 ([[ref-gb-2009-10-2-210]], [[rice-root-hormone-celltype-map]])
- 梨中 *PbYUC4* 编码吲哚-3-丙酮酸单加氧酶，受细胞分裂素 Type-B RR 直接转录激活，将 CK 信号耦合至 auxin 生物合成 ([[gibberellin-biosynthesis-is-required-for-cppu-induced]])

#### 信号转导核心模块
- **TIR1/AFB–Aux/IAA–ARF** 共受体-转录抑制子-响应因子模块是生长素转录调控的核心开关
- *SHY2/IAA3* 是 ARR1（细胞分裂素 Type-B RR）的直接靶基因，构成 CK-auxin 在根分生组织大小调控中的交叉节点 ([[ref-gb-2009-10-2-210]])
- *PbrARF13* 介导生长素对梨木质素和纤维素生物合成的抑制，揭示 auxin 信号在次生细胞壁代谢中的负调控功能 ([[auxin-inhibits-lignin-and-cellulose-biosynthesis]])

#### 细胞类型特异性
- 水稻根 scRNA-seq 揭示，生长素合成基因在分生组织细胞中富集，而响应基因在过渡/伸长区激活 ([[rice-root-hormone-celltype-map]])
- 拟南芥根 24 个细胞簇中，QC 和干细胞簇展现出独特的生长素信号谱 ([[root-cluster-hormone-response-patterns]])

---

### 2. 细胞分裂素 (Cytokinin, CK) — 分生组织维持与多激素代谢开关

**证据数量**: 约 9 条

#### 信号转导核心模块
- **AHK–AHP–Type-B ARR** 磷酸中继系统：Type-B ARR（ARR1/ARR10/ARR12）是 CK 信号的直接转录效应器
- ARR1 通过直接激活 *SHY2/IAA3* 实现 CK→auxin 信号交叉对话，调控根分生组织细胞分裂与分化平衡 ([[ref-gb-2009-10-2-210]])

#### CK 作为三激素代谢开关（H6 假说）
- **PbRR9-like** 通过双重转录调控同时激活 auxin 合成（*PbYUC4*↑）和抑制 ABA 合成（*PbNCED6*↓），实现单一转录因子对 auxin/ABA 比率的重新编程 ([[gibberellin-biosynthesis-is-required-for-cppu-induced-f2]])
- 该机制在蔷薇科果树中可能广泛保守——CPPU（CK 类似物）诱导的单性结实依赖下游 auxin 和 GA 生物合成
- KNOX 转录因子下游同时靶向 CK 和 GA 两条激素通路 ([[ref-tpc-110-073924]])

#### CK-SA 协同与表观遗传调控
- CK 与 SA 信号在从头芽再生中协同作用：ARR10/ARR12 和 NPR1 是 HDAC 抑制的表观遗传靶点 ([[hormone-signaling]] H3)

---

### 3. 油菜素内酯 (Brassinosteroid, BR) — 生长-防御代谢阀门

**证据数量**: 约 7 条

#### 信号转导核心模块
- **BRI1–BAK1 → BIN2 → BES1/BZR1** 磷酸化级联：BR 结合受体后，BIN2 激酶失活，去磷酸化的 BES1/BZR1 入核调控数千靶基因
- SlBIN2 与 SlBZR1 物理互作负调控 BR 信号，SlBZR1 促进番茄果实成熟和类胡萝卜素积累 ([[the-brassinosteroid-signaling-component-slbzr1-promotes]])

#### BR-BES1 类黄酮代谢阀门（H4 假说）
- **BES1 直接结合并抑制 PFG MYB（MYB11/MYB12/MYB111）启动子**：BR 水平高时阀门关闭，碳流转向生长；BR 低/UV-B 胁迫时阀门开放，碳流转入类黄酮合成 ([[brassinosteroid-activated-bri1-ems-suppressor-1-inhibits-fla]])
- ACbHLH144 (*Actinidia chinensis*) 响应 BR 信号，结合 *GA2ox7* 启动子增强 GA 失活，构成 BR→GA 的负反馈交叉 ([[acbhlh144-transcription-factor-negatively-regulates-phenolic]])

---

### 4. 赤霉素 (Gibberellin, GA) — DELLA 中枢与蛋白滴定调控

**证据数量**: 约 13 条

#### 信号转导核心模块
- **GID1–SCF^SLY1–DELLA** 降解模块：GA 结合受体 GID1 后，促进 SCF^SLY1 E3 连接酶泛素化 DELLA，靶向 26S 蛋白酶体降解

#### DELLA 蛋白作为多激素整合中枢（H1 假说）
- DELLA 在不同浓度阈值下切换互作伙伴：低浓度优先结合生长促进型转录因子（PIF、BZR1），高浓度转向胁迫响应型因子（JAZ、MYC2）
- **MdRGL2a**（苹果 DELLA）直接与 MdbHLH162 互作，桥接 GA 和 JA 信号调控花青素合成 ([[mdbhlh162-connects-the-gibberellin-and-jasmonic]])

#### DELLA-bHLH-bHLH 三元蛋白滴定（H7 假说）
- **MdbHLH162** 通过扣押正调控因子 MdbHLH3/MdbHLH33 抑制花青素合成
- MdRGL2a 竞争性结合 MdbHLH162，释放 MdbHLH3/MdbHLH33 恢复 *MdDFR/MdUF3GT* 转录
- GA 促进 MdRGL2a 降解，因此 GA 水平通过 DELLA 蛋白丰度调谐 bHLH 二聚体组成——构成蛋白滴定式调控网络 ([[mdbhlh162-connects-the-gibberellin-and-jasmonic-f4]], [[mdbhlh162-connects-the-gibberellin-and-jasmonic-f5]])

#### 器官发育中的 GA 功能
- GA 生物合成是 CPPU 诱导单性结实的必要条件 ([[gibberellin-biosynthesis-is-required-for-cppu-induced]])
- GA 在棉花纤维发育、根与地上部的差异响应中发挥关键作用 ([[comparative-transcriptome-profiling-reveals-the-multiple]])

---

### 5. 茉莉酸 (JA) 与乙烯 (ET) — 胁迫响应的时序分工

**证据数量**: JA 约 12 条，ET 约 17 条

#### JA 信号核心模块
- **COI1–JAZ–MYC2** 模块：COI1 与 SKP1-LIKE PROTEIN1/2、CULLIN 1、RING-box PROTEIN 1 形成 SCF^COI1 E3 连接酶复合体，感知 JA 后靶向 JAZ 蛋白泛素化降解，释放 MYC2 等转录因子 ([[mdbhlh162-connects-the-gibberellin-and-jasmonic-f7]])
- MdbHLH162 是 JA 信号的下游靶标——JA 激活其表达，通过 bHLH 二聚体扣押调控花青素

#### JA-ET 时序分工假说（H5）
- 伤口响应中，JA 信号在 0–6h 首先激活（"快速预警"），驱动 MYC2-MYB-WRKY 级联启动早期防御基因
- 乙烯信号在 6–24h 延迟激活（"持续防御"），通过 ERF/ERF003 启动次生代谢加固
- 时序分离依赖于 JA 诱导的 JAZ 降解先于乙烯诱导的 EIN3 蛋白稳定 ([[hormone-signaling]] H5)

#### 乙烯信号核心模块
- **ETR–CTR1–EIN2–EIN3/EIL1** 线性信号通路
- VviERF003 调控单萜糖苷合成，SlEIL2 调控类胡萝卜素积累

---

### 6. 脱落酸 (ABA) — 胁迫响应的核心介质

**证据数量**: 约 23 条

- ABA 是证据库中占比最高的激素，主要在胁迫响应（干旱、盐）背景下被讨论
- *PbNCED6*（ABA 合成关键酶 9-顺式-环氧类胡萝卜素双加氧酶）的启动子受 Type-B RR 直接抑制——CK 信号通过抑制 ABA 合成使细胞处于"生长许可"状态 ([[gibberellin-biosynthesis-is-required-for-cppu-induced-f2]])
- 激素 crosstalk 分析显示 ABA 与 CK、auxin、GA 存在复杂的网络级交叉对话 ([[comparative-transcriptome-profiling-reveals-the-multiple]])

---

### 7. 水杨酸 (SA) — 免疫与再生的表观遗传协同

**证据数量**: 约 7 条

- SA 主要出现在免疫应答和芽再生上下文中
- CK-SA 协同芽再生中，NPR1 是 SA 信号核心介导因子，ARR10/ARR12 是 CK 信号核心效应器——两者在 HDAC 抑制后通过染色质开放协同激活再生程序 ([[hormone-signaling]] H3)

---

### 8. 光信号转导 — 环境信号的分子解码

#### 红光/远红光 — phyB-PIF 模块
- 活性光敏色素（phyB）直接与 bHLH 转录因子 PIF 互作，引起 PIF 磷酸化和降解——这是光形态建成的核心分子开关 ([[the-redfar-red-light-photoreceptor-fvephyb-regulates]])
- TCP21 作为负调控因子整合 phyB 和 HY5 介导的信号通路，抑制光形态建成 ([[b6-JtU6BLa8oL57zgnlWnzO_Q]])
- PRC2 亚基 MSI1 与 HY5 互作抑制下胚轴伸长，连接表观遗传与光信号 ([[b6-_4lVabIoRyC91sLMxSI_ig]])

#### 蓝光 — CRY-COP1-HY5 模块
- 隐花色素 CRY1 C 端与 COP1/SPA E3 连接酶直接互作，稳定其泛素化靶标 HY5 和 CONSTANS——HY5 是光形态建成和花青素合成的核心调控枢纽 ([[blue-light-photoreceptor-cryptochrome-1-promotes]])
- CRY1 促进杨树木材形成和花青素积累

#### 光-激素交叉对话
- phyB-PIF 模块与 DELLA 蛋白直接互作——PIF 是 DELLA 低浓度时的优先结合伙伴，光信号通过 phyB 降解 PIF 和 GA 促进 DELLA 降解两条平行途径协同调控下胚轴伸长 ([[hormone-signaling]] H1)
- 红光和蓝光通过 phyB/CRY 上调 HY5，HY5 直接激活花青素合成酶基因（如 *CHS*、*DFR*），实现光→色素的无激素依赖代谢调控

---

### 9. 磷酸化级联与泛素-蛋白酶体系统 — 信号转导的通用"语法"

#### 泛素-蛋白酶体降解
- **SCF 复合体**（Skp1–Cullin–F-box）是多种激素信号的共用 E3 连接酶平台：SCF^TIR1（auxin）、SCF^COI1（JA）、SCF^SLY1（GA）使用相同骨架但不同的 F-box 受体蛋白实现信号特异性 ([[b3--bs1tAYpaCxa0fWZ49R6kw]])
- KRP1（细胞周期抑制子）是泛素/蛋白酶体途径的靶标，连接激素信号与细胞周期调控 ([[ref-j-1365-313X-2007-03370-x]])
- APC/C 泛素连接酶靶向关键细胞周期蛋白和激素信号组分 ([[sel-joe-14-0025]])

#### 磷酸化中继
- BR 信号中的 **BRI1→BIN2→BES1/BZR1** 磷酸化级联是植物中研究最透彻的激酶级联之一
- CK 信号的 **AHK→AHP→Type-B ARR** 磷酸中继系统使用 His-Asp 磷酸化，不同于经典的 Ser/Thr 激酶

---

## 共识发现

### 1. DELLA 蛋白是多激素信号的"物理整合中枢"
GA、JA、auxin、BR、光信号均通过 DELLA 蛋白进行交叉对话。DELLA 通过蛋白-蛋白互作扣押（sequester）多种转录因子，其蛋白丰度由 GA 促进的泛素化降解决定，因此 GA 水平间接调控所有 DELLA 互作伙伴（PIF、BZR1、JAZ、MYC2、bHLH 等）的活性——这是当前最核心的激素信号整合模型。

### 2. 细胞类型特异性激素响应能力由染色质预配置决定
拟南芥和水稻根的 scRNA-seq 一致表明，激素通路基因的表达和响应能力是细胞类型固有的（而非仅由激素梯度决定）。染色质可及性预配置是决定细胞是否"有能力"响应特定激素的关键因素——这与 H2（细胞激素响应能力假说）的核心预测一致。

### 3. 激素信号之间存在"代谢层面"的交叉对话（不通过蛋白互作）
CK 信号通过 Type-B RR 直接结合并调控 auxin（*YUC*）和 ABA（*NCED*）生物合成酶基因的启动子——这种"代谢层面"的交叉对话补充了传统的蛋白-蛋白互作交叉模型。BR 通过 BES1 直接抑制类黄酮合成酶启动子，构成类似的"代谢阀门"逻辑。

### 4. 蛋白滴定（Protein Titration）是激素调控代谢输出的新兴范式
MdbHLH162-MdbHLH3-MdRGL2a 三元体系表明，bHLH 转录因子间的抑制性二聚体扣押和被 DELLA 解救构成一个"蛋白滴定"网络——激素信号通过改变 DELLA 丰度调谐二聚体组成，实现梯度式的代谢输出控制，而非简单的开/关切换。

### 5. 光信号与激素信号在多个节点深度耦合
phyB-PIF-DELLA 三者在蛋白互作层面紧密连接，HY5 既是光信号核心因子又是花青素合成的直接调控者。光-激素耦合是理解植物环境适应性的关键框架。

---

## 知识空白

### 1. 大豆节间光质响应中 auxin-CK-BR 空间耦合的直接证据
现有证据主要来自拟南芥（下胚轴/根）和水稻（根），大豆（*Glycine max*）节间组织中这三类激素的空间梯度、细胞类型特异性响应及其在光质（R/FR 比率）变化下的动态耦合缺乏单细胞分辨率数据。auxin-CK-BR 空间耦合是理解大豆株型和光竞争适应的核心调控机制，但该假设尚无大豆节间组织 scRNA-seq 或空间转录组数据支撑。

### 2. DELLA 剂量-互作组切换的定量证据不足
虽然 DELLA 与多个转录因子（PIF、BZR1、JAZ、MYC2）互作的定性证据充分，但在不同 GA/DELLA 蛋白浓度下互作组的定量组成变化——特别是是否存在阈值"切换"行为——尚缺乏系统的 Co-IP/MS 或 FRET 定量数据支撑。

### 3. CK→auxin/ABA 代谢开关的跨物种保守性未验证
PbRR9-like 在梨中对 *PbYUC4* 和 *PbNCED6* 的双向调控是单一物种的单基因发现。该机制是否在拟南芥（ARR10/ARR12）、番茄（SlRR）和其他作物中保守、Type-B RR 对两靶基因启动子产生反向调控的染色质结构基础均未知。

### 4. 光信号-激素信号的空间整合机制
phyB/PIF/DELLA 互作主要在核内发生，但光受体（phyB、CRY）的亚细胞定位是光依赖的。光质变化（R/FR、蓝光强度）如何在空间上（不同组织、不同细胞类型）调制激素信号输出的细胞类型特异性图谱尚不清楚。

### 5. JA-ET 时序分工的细胞水平直接证据
JA-ET 时序分工假说基于整体叶片转录组数据推断，但在单细胞/细胞类型水平上，不同细胞类型是否遵循相同的时序逻辑、两类信号的激活在细胞水平上是否存在空间差异（如伤口边缘 vs 远端的时序差异）均缺乏数据。

### 6. BR-BES1 代谢阀门的代谢流直接证据
BES1 ChIP-seq 和突变体代谢组提供了 BES1 调控类黄酮合成的强相关性证据，但 BR 梯度下碳流在初级代谢（纤维素/生长）和次生代谢（类黄酮/UV 防护）之间的定量分配变化——即阀门开度的代谢流直接测量——尚未完成。

---

## 核心调控基因

| 基因 | 功能 | 关联通路 |
|------|------|----------|
| *SHY2/IAA3* | Auxin 响应抑制子，ARR1 靶基因 | Auxin, CK |
| *PbRR9-like* | Type-B RR，双重调控 YUC4/NCED6 | CK, Auxin, ABA |
| *ARR1/ARR10/ARR12* | Type-B ARR，CK 信号效应器 | CK, Auxin, SA |
| *PbYUC4* | Auxin 生物合成酶 | Auxin, CK |
| *PbNCED6* | ABA 生物合成酶 | ABA, CK |
| *BES1/BZR1* | BR 信号终端转录因子 | BR, 类黄酮 |
| *SlBZR1* | 番茄 BZR1 同源基因，促果实成熟 | BR, ET |
| *MdRGL2a* | DELLA 蛋白，GA-JA 交叉节点 | GA, JA |
| *MdbHLH162* | 花青素负调控 bHLH | JA, GA |
| *MdbHLH3/MdbHLH33* | 花青素正调控 bHLH | 花青素, GA |
| *HY5* | 光形态建成核心转录因子 | 光, 花青素 |
| *PIF* (PIF3/4/5) | phyB 互作 bHLH，光/GA 整合 | 光, GA |
| *CRY1* | 蓝光受体，调控 COP1-HY5 | 蓝光 |
| *TCP21* | 光形态建成负调控因子 | 光 |
| *COI1* | JA 受体，SCF^COI1 的 F-box 亚基 | JA |
| *EIN2/EIN3* | 乙烯信号核心组分 | ET |
| *NPR1* | SA 信号核心介导因子 | SA |
| *ACbHLH144* | 调控 GA2ox7，BR-GA 交叉 | BR, GA |
| *PbrARF13* | Auxin 响应因子，调控木质素/纤维素 | Auxin |

---

## 关键代谢物/信号分子

| 分子 | 关联通路 |
|------|----------|
| IAA（吲哚-3-乙酸） | Auxin |
| tZ/cZ/iP（细胞分裂素类） | CK |
| BL/CS（油菜素内酯/栗甾酮） | BR |
| GA₃/GA₄ | GA |
| JA/JA-Ile | JA |
| ACC/乙烯 | ET |
| ABA | ABA |
| SA | SA |
| 花青素/类黄酮 | 次生代谢（多激素调控靶标） |

---

## 方法论演化
植物激素信号转导研究已从单一激素通路的遗传学解析（突变体筛选→基因克隆→生化验证）推进到多激素网络的系统生物学层面。当前的研究前沿包括：
- **单细胞/空间转录组**：揭示细胞类型特异性激素响应和染色质预配置
- **ChIP-seq/CUT&Tag**：在全基因组尺度鉴定激素信号终端转录因子的结合靶点
- **蛋白互作组学**：Co-IP/MS、邻近标记（TurboID）定量激素依赖性互作组变化
- **代谢流分析**：¹³C 标记追踪激素调控下碳流在初生/次生代谢间的分配
- **CRISPR/Cas9 验证**：从相关性到因果性的标准工具

---

## 大豆项目关联

### 大豆节间光质响应中的 auxin-CK-BR 空间耦合假说

在大豆（*Glycine max*）密植/遮荫条件下，R/FR 比率降低通过 phyB-PIF 模块触发避荫综合征（shade avoidance syndrome），表现为节间伸长加速。该过程中：

- **Auxin** 提供细胞伸长的"方向性"和"幅度"信息（通过 PIN 极性运输建立空间梯度）
- **CK** 通过 Type-B RR 调控分生组织活性和 auxin 生物合成（*YUC* 基因），维持节间基部的细胞增殖潜能
- **BR** 通过 BES1/BZR1 促进细胞壁松弛和扩展，同时通过 PIF-DELLA 节点整合光和 GA 信号

三者在大豆节间中沿纵轴的空间耦合（顶端→中部→基部）可能是理解光质调控节间伸长的核心机制框架。当前该假说依赖的模式植物（拟南芥下胚轴、水稻节间）证据充分，但大豆中：
- 节间组织的单细胞/空间转录组图谱缺失
- 光质梯度下三种激素的原位定量和空间分布未知
- 大豆 *PIN*、*YUC*、*BZR1* 同源基因在节间中的细胞类型表达模式未鉴定

这些构成了当前知识体系中与大豆项目最直接相关的关键空白。

---

## 相关合成页面
- [[plant-metabolism]]
- [[root-development]]
- [[vascular-development]]


## Absorbed Sub-Themes


### hormone-signaling-hormone-signaling (absorbed)
o_discovered: true
cluster_size: 2 tags
status: auto-generated
updated: 2026-06-01
---

# 📄 Synthesis: #Hormone-Signaling & Hormone-Signaling

## Domain Overview

自动发现主题 — 核心: #hormone-signaling, hormone-signaling | 全部标签: #hormone-signaling, hormone-signaling

**统计**:
- 涵盖论文: ~33 篇
- 证据条目: 47 条
- 共识发现: 0 项
- 潜在争议: 0 项
- 核心标签: #hormone-signaling, hormone-signaling

**与大豆项目的关联**: 低 — 可提供背景知识

---

## Consensus Findings (跨论文共识)



---

## Contradictions & Controversies (争议与矛盾)

\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n

---

## Knowledge Gaps (知识空白)

- 跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足\n- 空间维度: 缺乏空间转录组级别的发育轨迹分析\