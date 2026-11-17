---
title: "Hypotheses: Metabolism & Natural Products"
title_zh: "代谢与天然产物：可证伪假说"
type: hypothesis
topic: "metabolism-natural-products"
theme_basis: "tag"
total_evidence: 270
total_papers: 88
total_hypotheses: 6
specificity_domain: 6
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Metabolism & Natural Products — 可证伪假说（6 条）

> 生成口径：主题内 270 条证据 / 88 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Metabolism & Natural Products |
| 证据条目 | 270 |
| 独立论文 | 88 |
| 生成假说 | 6 |
| 其中主题专用方案 | 6 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：VvSBP8 → 黄酮醇合成（方向裁决）

**假说**：VvSBP8 正向促进黄酮醇合成。判别性检验：在 Plant (unspecified) 中敲低或敲除 VvSBP8，黄酮醇合成应下降；恢复表达应使其回升。

**为什么值得做（证据缺口）**

- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同发育期材料；必要时用异源宿主（酵母/大肠杆菌）表达体系 |
| 操纵或比较变量 | VvSBP8 的敲除/敲低、过表达，或体外酶促反应（底物浓度梯度） |
| 对照 | 野生型 + 空载体；体外反应设热失活酶与无底物对照 |
| 读出 | LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性（至少两项独立读出交叉验证） |
| 若假说为真 | 敲低/敲除株系中黄酮醇合成显著下降且可被回补，过表达株系上升 |
| 若假说为假 | 遗传操纵后黄酮醇合成无方向一致的变化，或变化与 VvSBP8 的表达量无关 |

**证据基础**：112 条证据 / 66 篇独立论文（置信度：高）
- `the-flavour-of-grape-colour-anthocyanin-f8`
- `daily-42926806-f4`
- `the-flavour-of-grape-colour-anthocyanin-f7`
- `cmnac25-targets-cmmyb6-to-positively-regulate-f1`
- `ms-10-1007_s44372-026-00770-2-f3`
- `cmnac25-targets-cmmyb6-to-positively-regulate-f2`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> This results in the decrease of its key downstream target genes VvSBP8 and VvSVP13, thereby inhibiting its role as a competitor to displace the VvMYBA1 or VvMYC1 protein from the MBW complex, resulting in the intensive MBW complex formation and activities that are required for anthocyanin accumulation (Fig.
> <sub>来源：`mir156b-targeted-vvsbp813-functions-downstream-of-the-f3`</sub>


### H2：PBRMYB（家族冗余）

**假说**：PBRMYB家族在本主题内有 3 个成员（PbrMYB132、PbrMYB169、PbrMYB24）分别被提名参与同一过程；在 9 条相关证据中仅 0 条涉及双/多突变，家族内功能冗余与剂量补偿因此未被定量刻画（受检索覆盖限制，需系统检索复核）。判别性检验：构建双突变与三突变体，比较单突变与多突变的表型强度，并测定单突变体中同源成员的表达补偿。

**为什么值得做（证据缺口）**

- 成员证据分散在不同论文，9 条中仅 0 条做过双/多突变
- 家族成员间的表达补偿缺少同遗传背景下的并行测定

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种，同遗传背景、同生育期 |
| 操纵或比较变量 | 家族成员的敲除/敲低，单突变 vs 双/多突变 |
| 读出 | 定量表型效应量与同源成员表达水平 |
| 若假说为真 | 多突变体表型显著强于单突变，且单突变体中同源成员表达上调（补偿成立） |
| 若假说为假 | 多突变体与单突变表型相当、同源成员表达不变，说明成员功能已分化 |

**证据基础**：9 条证据 / 2 篇独立论文（置信度：低）
- `auxin-inhibits-lignin-and-cellulose-biosynthesis-f3`
- `the-transcription-factor-pbrmyb24-regulates-lignin-f6`
- `auxin-inhibits-lignin-and-cellulose-biosynthesis-f9`
- `the-transcription-factor-pbrmyb24-regulates-lignin-f1`
- `auxin-inhibits-lignin-and-cellulose-biosynthesis-f2`
- `the-transcription-factor-pbrmyb24-regulates-lignin-f4`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> Taken together, our study highlights the important role of the 'PbrARF13-PbrNSC-PbrMYB132' signal-ling cascade in the inhibition of lignin and cellulose biosynthesis in stone cells and provides novel insights for studying the roles of phytohormones on stone cells formation in pear fruit and SCW formation in plants.
> <sub>来源：`auxin-inhibits-lignin-and-cellulose-biosynthesis-f3`</sub>


### H3：MDMYB（家族冗余）

**假说**：MDMYB家族在本主题内有 3 个成员（MdMYB1、MdMYB10、MdMYB8）分别被提名参与同一过程；在 5 条相关证据中仅 0 条涉及双/多突变，家族内功能冗余与剂量补偿因此未被定量刻画（受检索覆盖限制，需系统检索复核）。判别性检验：构建双突变与三突变体，比较单突变与多突变的表型强度，并测定单突变体中同源成员的表达补偿。

**为什么值得做（证据缺口）**

- 成员证据分散在不同论文，5 条中仅 0 条做过双/多突变
- 家族成员间的表达补偿缺少同遗传背景下的并行测定

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种，同遗传背景、同生育期 |
| 操纵或比较变量 | 家族成员的敲除/敲低，单突变 vs 双/多突变 |
| 读出 | 定量表型效应量与同源成员表达水平 |
| 若假说为真 | 多突变体表型显著强于单突变，且单突变体中同源成员表达上调（补偿成立） |
| 若假说为假 | 多突变体与单突变表型相当、同源成员表达不变，说明成员功能已分化 |

**证据基础**：5 条证据 / 4 篇独立论文（置信度：中）
- `psbzip1-and-psbzip10-induce-anthocyanin-synthesis-f2`
- `mdmyb8-is-associated-with-flavonol-biosynthesis-f2`
- `mdmyb8-is-associated-with-flavonol-biosynthesis-f3`
- `integrated-analysis-of-the-metabolome-and-f3`
- `transcription-factor-nnmyb5-controls-petal-color-f3`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> (2022) have reported that MdHY5-like interacts with bZIP transcription factor gene MdHY5 and plays an important role in the light-induced anthocyanin accumulation in apple peel by regulating the expression of MdMYB10 and downstream anthocyanin biosynthesis genes.
> <sub>来源：`psbzip1-and-psbzip10-induce-anthocyanin-synthesis-f2`</sub>


### H4：phenylpropanoid（跨物种保守）

**假说**："phenylpropanoid" 在本主题内已有 11 篇论文、9 个主要研究物种的证据，但 12 条证据中有 2 条来自 Oryza sativa；该过程在其他物种中是否由同一调控逻辑驱动，现有文献无法判定。判别性检验：在第二个物种中操纵同源因子，用同一读出量化该过程，并做跨物种互补。

**为什么值得做（证据缺口）**

- 9 个物种中出现该过程，但 2 条证据来自 Oryza sativa，其余物种仅有观察性描述
- 缺少跨物种的同源操纵与统一读出

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 至少两个物种（原报道物种 + 一个独立谱系） |
| 操纵或比较变量 | 同源因子的遗传操纵（突变/敲低/过表达） |
| 读出 | 同一过程的定量读出与跨物种互补结果 |
| 若假说为真 | 第二物种中同源因子的操纵产生方向一致的效应，跨物种互补可恢复表型 |
| 若假说为假 | 第二物种中操纵无效或方向相反，说明该过程的调控逻辑发生了谱系特异分化 |

**证据基础**：12 条证据 / 11 篇独立论文（置信度：高）
- `the-flavour-of-grape-colour-anthocyanin-f8`
- `ms-10-1007_s44372-026-00770-2-f3`
- `daily-42958626-f8`
- `daily-42959494-f4`
- `integration-of-metabolomics-and-transcriptomics-reveals-f2`
- `the-flavour-of-grape-colour-anthocyanin-f2`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> Remarkably, the DEGs identified in any of the cultivars and tissues overlapping with the specific hemizygous intervals of TB compared to TT did not include any known regulator of metabolism pathways, apart from the phenylpropanoid regulators VviMYBA1 and VviMYBA2 (Vitvi02g01015), and the pseudogene VvMYBA8 (Vitvi02g…
> <sub>来源：`the-flavour-of-grape-colour-anthocyanin-f8`</sub>


### H5：terpenoid（跨物种保守）

**假说**："terpenoid" 在本主题内已有 6 篇论文、5 个主要研究物种的证据，但 8 条证据中有 2 条来自 Glycine max；该过程在其他物种中是否由同一调控逻辑驱动，现有文献无法判定。判别性检验：在第二个物种中操纵同源因子，用同一读出量化该过程，并做跨物种互补。

**为什么值得做（证据缺口）**

- 5 个物种中出现该过程，但 2 条证据来自 Glycine max，其余物种仅有观察性描述
- 缺少跨物种的同源操纵与统一读出

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 至少两个物种（原报道物种 + 一个独立谱系） |
| 操纵或比较变量 | 同源因子的遗传操纵（突变/敲低/过表达） |
| 读出 | 同一过程的定量读出与跨物种互补结果 |
| 若假说为真 | 第二物种中同源因子的操纵产生方向一致的效应，跨物种互补可恢复表型 |
| 若假说为假 | 第二物种中操纵无效或方向相反，说明该过程的调控逻辑发生了谱系特异分化 |

**证据基础**：8 条证据 / 6 篇独立论文（置信度：高）
- `ms-10-1007_s44372-026-00770-2-f3`
- `ref-j-molp-2023-10-008-f8`
- `daily-42959494-f4`
- `ref-j-molp-2023-10-008-f3`
- `integrating-gc-ms-and-ssrna-seq-analysis-to-f2`
- `deep-sequencing-identifies-mirnas-and-their-f2`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> However, comparative evi dence suggests that, although terpenoid metabolism plays a central role in hormonal sig naling and rapid stress responses, its contribution to drought adaptation is more variable across genotypes than phenylpropanoid-driven structural protection, indicating path way-specific specialization i…
> <sub>来源：`ms-10-1007_s44372-026-00770-2-f3`</sub>


### H6：flavonoid（剂量—效应）

**假说**："flavonoid" 在本主题 36 篇论文、20 个主要研究物种中被报道，其中 8 条证据来自 Ginkgo biloba；57 条证据中仅 1 条报告了浓度梯度或剂量—响应参数，因此剂量—响应关系的定量可比性不足（受检索覆盖限制，需系统检索复核）。判别性检验：外源施加 ≥5 个浓度梯度并配合合成抑制剂，拟合剂量—响应曲线与 EC50，再在受体突变体中检验曲线是否右移。

**为什么值得做（证据缺口）**

- 57 条证据中仅 1 条给出浓度梯度或 EC50
- 缺少跨物种统一施加方式与统一读出，无法比较响应阈值

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 原报道物种 + 一个独立物种；同遗传背景、同生育期 |
| 操纵或比较变量 | 外源施加的浓度梯度（≥5 个剂量）± 合成抑制剂；受体突变体作对照 |
| 读出 | 剂量—响应曲线、EC50、下游响应的动态范围 |
| 若假说为真 | 同一响应在两个物种中给出方向一致、EC50 差异 <1 个数量级的剂量—响应曲线，且受体突变体中曲线右移 |
| 若假说为假 | EC50 跨物种相差 >2 个数量级，或受体突变体中曲线不移位，说明该激素的响应阈值由谱系特异的受体组成决定 |

**证据基础**：57 条证据 / 36 篇独立论文（置信度：高）
- `daily-42926806-f4`
- `daily-42927300-f5`
- `uv-b-promotes-flavonoid-biosynthesis-in-ginkgo-f2`
- `integrated-metabolomic-and-transcriptomic-analysis-reveals-f5`
- `integrative-analysis-of-metabolome-and-transcriptome-f4`
- `morus-alba-l-leaves-integration-of-f5`

**领域特异性**：领域特异读出梯度：LC-MS/GC-MS 代谢物含量、酶活与动力学参数（Km/kcat）、底物特异性

**原始断言（摘自证据页，供核对）**
> KEGG enrichment analysis indicated that differential metabolites were mainly enriched in amino acid biosynthesis and flavonoid metabolism pathways, suggesting that amino acid metabolic remodeling is strongly associated with quality differentiation in hybrid offspring, thereby providing metabolic targets for improvin…
> <sub>来源：`daily-42926806-f4`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
