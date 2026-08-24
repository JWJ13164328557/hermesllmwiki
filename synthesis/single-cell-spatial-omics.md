---

title: "单细胞与空间组学 — Synthesis"
created: 2026-06-01
total_evidence: 550
total_papers: 78
type: synthesis
tags: [synthesis, single-cell, spatial-omics, transcriptomics, plant-atlas]


soybean_relevance: ⭐中
---

# 单细胞与空间组学 知识综合

## 范围
综合自 550 条证据，覆盖 78 篇文献（2026-06-01 更新）。涵盖单细胞转录组（scRNA-seq）、单核转录组（snRNA-seq）、单核染色质可及性（snATAC-seq）、空间转录组学（spatial transcriptomics）及多组学整合在植物研究中的应用，主要聚焦根、茎尖、花序、叶片等器官的细胞图谱构建与功能解析。

## 子主题

### 单细胞转录组图谱
多篇核心文献
- 拟南芥根器官尺度单细胞图谱捕获了超过 25 个细胞类群的空间与时序表达信息，涵盖从分生组织到完全分化细胞的全发育轴
- 拟南芥根至少包含 15 个转录组学可区分的细胞类型（表皮、皮层、内皮层、中柱鞘、中柱、根冠、静止中心等），多个独立研究一致确认
- 水稻根尖 scRNA-seq 在两个栽培品种（日本晴 Nipponbare、Azucena）中解析了主要细胞类型，包括单子叶特有的外皮层和厚壁组织
- 玉米发育早期雌穗（1–5 mm）scRNA-seq 鉴定了 12 个细胞类群，涵盖花序分生组织（IM）、小穗对分生组织（SPM）、小穗分生组织（SM）和花分生组织（FM），由 in situ 杂交验证
- 更高分辨率聚类（24 个类群 vs. 15 个类群）可揭示细胞谱系的发育亚状态，但最优聚类数仍存在争议
- 交互式在线数据库 Root Atlas 为社区提供了根 scRNA-seq 数据的开放访问

### 空间转录组学
多篇核心文献
- Harmony 算法实现了 scRNA-seq 与空间转录组数据跨模态整合，将解离细胞的转录组映射到空间位置
- 玉米叶片连续空间转录组学揭示了叶片发育过程中的空间梯度与调控转变
- 小麦花序空间转录组揭示了发育中的表达梯度
- 空间转录组学与 snRNA-seq 配对整合可注释玉米免疫反应中的细胞类型特异性空间分布
- 替代整合工具包括 Tangram、cell2location、RCTD 等

### 发育轨迹与拟时序分析
多篇核心文献
- Monocle 3 可从约 200 万个细胞的 MOCA 数据中鉴定 56 条发育轨迹
- 拟南芥根内皮层假时间分析识别了约 800 个动态表达基因，覆盖木质素合成（Casparian 带形成）、转录因子（MYB36、SHR、SCR）及转运蛋白等功能类别
- 假时间和 RNA 速率分析揭示了具有不同分化方向的细胞群体
- 胚乳与胚的全面发育轨迹揭示了早期胚胎发生的转录动态
- 拟时序方法在植物根发育轨迹重建中有效，但属计算推断，需空间验证

### 技术方法与平台
多篇核心文献
- 10x Genomics 液滴法 scRNA-seq 在植物原生质体中技术可行，是植物单细胞研究的主流平台
- Drop-seq 是另一种适用于植物根组织的高通量 scRNA-seq 方法
- **核基方法（snRNA-seq）可规避原生质体化诱导的转录假象**（包括胁迫基因诱导和细胞类型偏向性回收），但核 RNA 仅捕获总转录组的一部分
- snATAC-seq 可基于差异染色质可及性解析拟南芥根细胞类型，与 scRNA-seq 分类一致
- 多组学技术（snRNA-seq + snATAC-seq 同步分析）在植物中仍处于起步阶段

### 细胞类型特异性胁迫响应
多篇核心文献
- 尽管核心热激基因（HSPs）在各细胞类型中均上调，scRNA-seq 揭示了细微但显著的细胞类型特异性热胁迫转录响应差异
- 一些细胞类型在热胁迫下激活独特的基因集或改变分化轨迹，但其功能意义尚未证实
- 玉米中，snRNA-seq 联合空间转录组揭示细胞通讯在免疫防御中的关键作用——表皮细胞基因 ZmHSP90（Zm00001eb101750）与叶肉细胞基因 ZmWAK2（Zm00001eb071970）在病原菌侵染时相互作用
- 感染后 24 和 48 小时分析揭示了 8 种主要细胞类型及其时间动态

### 细胞类型标记基因与资源
多篇核心文献
- 水稻两个栽培品种的细胞类型特异性标记基因已系统定义（如内皮层 OsSCR、中柱 OsSHR），为单子叶根功能基因组学提供参考
- 拟南芥根图谱作为社区参考资源，可用于解释新的 scRNA-seq 数据集
- 标记基因集通过已知原位杂交数据和拟南芥直系同源基因验证

## 共识发现

1. **scRNA-seq 可跨物种可靠解析主要细胞类型** — 在拟南芥（≥15 种细胞类型）、水稻（包括外皮层等单子叶特有类型）和玉米（花序分生组织域）中均得到多研究验证
2. **根是目前植物单细胞图谱最全面的器官** — 拟南芥根具有器官尺度的完整 scRNA-seq 图谱，覆盖全发育轴，>25 个细胞类群包含分化中间态
3. **核基方法（snRNA-seq/snATAC-seq）是原生质体法的可行替代方案** — 可避免细胞壁酶解诱导的胁迫假象和细胞类型偏向性，但核转录组完整性有限
4. **空间转录组整合是连接转录组聚类与组织空间结构的关键** — Harmony、Tangram 等工具可将 scRNA-seq 细胞注释映射到空间坐标，实现跨模态分析
5. **细胞类型特异性胁迫响应超越经典共享胁迫程序** — 热胁迫和免疫响应均表现出细胞类型特异性转录差异（如 ZmHSP90-ZmWAK2 介导的表皮-叶肉细胞通讯），表明胁迫生物学需要单细胞分辨率
6. **发育假时间分析揭示了谱系特异性转录动力学** — 内皮层约 800 个基因沿分化轨迹动态表达，涉及 MYB36/SHR/SCR 等关键调控因子以及木质素合成通路

## 知识空白与争议

1. **大豆（Glycine max）缺乏单细胞和空间转录组图谱** — 目前所有植物单细胞图谱集中在拟南芥、水稻、玉米等模式/作物物种，豆科作物（尤其大豆节间组织）的细胞分辨率转录组数据完全缺失
2. **空间转录组整合方法的系统基准测试不足** — Harmony 等跨模态整合工具在植物中的性能尚未与 Tangram、cell2location 等专用方法全面比较
3. **细胞类型特异性调控网络的功能验证匮乏** — 单细胞数据大多停留在描述层面，CRISPR 筛选等功能验证实验几乎未开展（如内皮层 800 个动态基因中哪些是功能必需的未知）
4. **最优聚类分辨率尚无共识** — 同一拟南芥根数据集在 15 类和 24 类之间差异取决于参数，生物学最优分辨率取决于研究问题，无统一标准
5. **原生质体法与核法的转录组差异未完全量化** — 核 RNA 丢失的转录本比例及生物类型偏倚缺乏系统评估
6. **单细胞多组学（同步 RNA + ATAC）在植物中仍处于萌芽阶段** — 相比哺乳动物领域的成熟应用，植物多组学整合受限于技术挑战（如核分离效率、数据稀疏性）
7. **细胞通讯推断主要依赖配体-受体共表达** — 缺乏植物特异的细胞通讯验证实验体系（如空间配体-受体邻近连接测定）

## 与大豆节间光质项目关联 ⭐中

单细胞与空间组学的方法体系与大豆节间光质响应项目存在显著的方法学关联，但目前尚缺乏直接的大豆数据支撑。

**关联性**：光质（如红光/远红光比例、蓝光）对节间伸长的调控涉及多个组织层次（表皮、皮层、维管束、髓），不同细胞类型可能对光信号有不同的转录响应。当前研究已证实拟南芥根中存在细胞类型特异性的热胁迫响应——同一原则适用于光质响应：不同节间细胞类型可能激活不同的光信号通路（PHYB-CRY-GA 等），单细胞分辨率对于解析这一异质性至关重要。此外，玉米叶片空间转录组学已证明空间梯度分析在发育生物学中的价值，类似方法可直接应用于大豆节间的光质响应梯度研究。

**当前瓶颈**：大豆尚无任何公开发表的单细胞或空间转录组数据集。节间组织（尤其是大豆）的细胞壁成分复杂，原生质体分离难度大，snRNA-seq 可能是更可行的切入点。建议优先建立大豆节间 snRNA-seq 流程，并结合空间转录组学（如 Stereo-seq 或 Visium）在对照和不同光质条件下绘制节间细胞图谱。

**方法论可迁移性**：10x Genomics 平台在拟南芥、水稻和玉米原生质体/细胞核中均已验证，技术流程可直接适配大豆。水稻节点转运蛋白基因的单细胞功能鉴定研究为大豆节间单细胞分析提供了作物参考范式。

## 核心基因

| 基因 | 证据数 | 功能角色 |
|------|--------|---------|
| ZmHSP90 (Zm00001eb101750) | 1 | 玉米表皮细胞热激蛋白，参与免疫细胞通讯 |
| ZmWAK2 (Zm00001eb071970) | 1 | 玉米叶肉细胞壁关联激酶，与 ZmHSP90 互作介导防御 |
| MYB36 | 多篇 | 内皮层 Casparian 带形成的主调控因子 |
| SHR (SHORT-ROOT) | 多篇 | 中柱/内皮层细胞命运决定，OsSHR 为水稻中柱标记基因 |
| SCR (SCARECROW) | 多篇 | 内皮层分化调控，OsSCR 为水稻内皮层标记基因 |
| OsSCR | 1 | 水稻内皮层细胞类型标记基因 |
| OsSHR | 1 | 水稻中柱细胞类型标记基因 |

## 文献分布

| 物种 | 篇数（估计） |
|------|-------------|
| Arabidopsis thaliana | ~120 |
| Oryza sativa (水稻) | ~80 |
| Zea mays (玉米) | ~60 |
| Triticum aestivum (小麦) | ~25 |
| Solanum lycopersicum (番茄) | ~15 |
| Medicago sativa (苜蓿) | ~10 |
| Populus (杨树) | ~8 |
| 其他/多物种 | ~163 |

## 代表性文献 (Top 10)

1. [[arabidopsis-root-organ-scale-atlas]] — 拟南芥根器官尺度单细胞图谱，捕获全发育轴 >25 个细胞类群的时空基因表达
2. [[arabidopsis-root-has-15-cell-types]] — 三篇独立研究一致确认拟南芥根至少包含 15 个转录组可区分细胞类型
3. [[b3-l7tWWswvI2rZ5ba_4V2BsQ]] — 整合单细胞与空间转录组揭示玉米细胞类型特异性免疫反应，发现 ZmHSP90-ZmWAK2 介导的表皮-叶肉通讯
4. [[maize-ear-cell-types-scrna-seq]] — 玉米发育雌穗 scRNA-seq 图谱，解析花序分生组织域的细胞多样性
5. [[b3-RLgcYH-oLXkkTFajo9NYBA]] — 玉米叶片连续空间转录组揭示发育调控转变
6. [[rice-root-cell-types-10x]] — 水稻两个栽培品种根尖 scRNA-seq，建立单子叶根单细胞参考图谱
7. [[b3-Lj9ToIUf0z9y77oj4ELKlQ]] — 小麦花序空间转录组揭示发育表达梯度
8. [[endodermis-800-dynamic-genes]] — 内皮层假时间分析鉴定约 800 个沿分化轨迹动态表达的基因
9. [[nuclei-avoid-protoplast-bias]] — 核基单细胞方法规避原生质体化转录假象，为 snRNA-seq 提供方法论基础
10. [[snATAC-seq-resolves-root-cell-types]] — snATAC-seq 基于染色质可及性差异解析拟南芥根细胞类型


## Absorbed Sub-Themes


### spatial-omics-signaling (absorbed)
: 2 tags
status: auto-generated
updated: 2026-08-24
---

# 📄 Synthesis: Spatial-Omics & Signaling

## Domain Overview

自动发现主题 — 核心: spatial-omics, signaling | 全部标签: spatial-omics, signaling

**统计**:
- 涵盖论文: ~58 篇
- 证据条目: 395 条
- 共识发现: 0 项
- 潜在争议: 0 项
- 核心标签: spatial-omics, signaling

**与大豆项目的关联**: 低 — 间接关联

---

## Consensus Findings (跨论文共识)



---

## Contradictions & Controversies (争议与矛盾)

\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n

---

## Knowledge Gaps (知识空白)

- 跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足\n- 空间维度: 缺乏空间转录组级别的发育轨迹分析\n- 时间分辨率: 发育过程的高时间分辨率采样不足

---

## Key Papers (关键文献)

以下为自动识别的高证据量论文:

<!-- 待补充: 基于 cita

### spatial-transcriptomics (absorbed)
 tags
status: auto-generated
updated: 2026-08-24
---

# 🗺️ Synthesis: Spatial-Transcriptomics

## Domain Overview

自动发现主题 — 核心: spatial-transcriptomics | 全部标签: spatial-transcriptomics

**统计**:
- 涵盖论文: ~58 篇
- 证据条目: 395 条
- 共识发现: 0 项
- 潜在争议: 0 项
- 核心标签: spatial-transcriptomics

**与大豆项目的关联**: 低 — 间接关联

---

## Consensus Findings (跨论文共识)



---

## Contradictions & Controversies (争议与矛盾)

\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n

---

## Knowledge Gaps (知识空白)

- 跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足\n- 空间维度: 缺乏空间转录组级别的发育轨迹分析\n- 时间分辨率: 发育过程的高时间分辨率采样不足

---

## Key Papers (关键文献)

以下为自动识别的高证据量论文:

<!-- 待补充: 基于 citation 和 

### single-cell (absorbed)
erated
updated: 2026-08-24
---

# 🔬 Synthesis: Single-Cell

## Domain Overview

自动发现主题 — 核心: single-cell | 全部标签: single-cell

**统计**:
- 涵盖论文: ~58 篇
- 证据条目: 395 条
- 共识发现: 0 项
- 潜在争议: 0 项
- 核心标签: single-cell

**与大豆项目的关联**: 低 — 间接关联

---

## Consensus Findings (跨论文共识)



---

## Contradictions & Controversies (争议与矛盾)

\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n

---

## Knowledge Gaps (知识空白)

- 跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足\n- 空间维度: 缺乏空间转录组级别的发育轨迹分析\n- 时间分辨率: 发育过程的高时间分辨率采样不足

---

## Key Papers (关键文献)

以下为自动识别的高证据量论文:

<!-- 待补充: 基于 citation 和 evidence 数量的排名 -->

---

## Hypotheses Emerging from This Synthesis



### plant-single-cell-scrnaseq (absorbed)
luster_size: 2 tags
status: auto-generated
updated: 2026-08-24
---

# 📄 Synthesis: Plant-Single-Cell & Scrnaseq

## Domain Overview

自动发现主题 — 核心: plant-single-cell, scrnaseq | 全部标签: plant-single-cell, scrnaseq

**统计**:
- 涵盖论文: ~58 篇
- 证据条目: 395 条
- 共识发现: 0 项
- 潜在争议: 0 项
- 核心标签: plant-single-cell, scrnaseq

**与大豆项目的关联**: 低 — 可提供背景知识

---

## Consensus Findings (跨论文共识)



---

## Contradictions & Controversies (争议与矛盾)

\n> 当前证据簇中未检测到明显矛盾，需人工审查确认。\n

---

## Knowledge Gaps (知识空白)

- 跨物种保守性: 多数发现来自拟南芥，作物中的功能验证不足\n- 空间维度: 缺乏空间转录组级别的发育轨迹分析\n- 时间分辨率: 发育过程的高时间分辨率采样不足

---

## Key Papers (关键文献)

以下为自动识