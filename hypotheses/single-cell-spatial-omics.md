---
title: "Hypotheses: Single-Cell & Spatial Omics"
title_zh: "单细胞与空间组学：可证伪假说"
type: hypothesis
topic: "single-cell-spatial-omics"
theme_basis: "tag"
total_evidence: 276
total_papers: 138
total_hypotheses: 6
specificity_domain: 6
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-28
---

# 💡 Single-Cell & Spatial Omics — 可证伪假说（6 条）

> 生成口径：主题内 276 条证据 / 138 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Single-Cell & Spatial Omics |
| 证据条目 | 276 |
| 独立论文 | 138 |
| 生成假说 | 6 |
| 其中主题专用方案 | 6 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：RCI2A（剂量—效应）

**假说**：RCI2A 已有 8 项独立研究；但其中仅 0 条给出不同表达/活性水平的梯度或剂量—响应参数，效应量随水平变化的定量关系无法从现有文献取得（受检索覆盖限制，需系统检索复核）。判别性检验：构建梯度表达系并做定量表型曲线。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织在 >=2 个独立数据集（不同物种/平台/实验室）中的注释结果 |
| 操纵或比较变量 | 注释方案与聚类参数（参照标记集 vs 数据集自有注释），或细胞类型特异扰动 |
| 对照 | 同一批数据换用第二套标记集/第二平台复核，作为内部对照 |
| 读出 | 细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位（至少两项独立读出交叉验证） |
| 若假说为真 | 表型随 RCI2A 表达或活性单调变化，半数效应点可在独立实验室复现 |
| 若假说为假 | 表型与表达量无单调关系（阈值型或非单调），提示存在缓冲或旁路 |

**证据基础**：8 条证据 / 8 篇独立论文（置信度：高）
- `ms-10-1038_s41598-026-75301-w-f2`
- `daily-42302294-f2`
- `salvia-tanshinone-sc-spatial-f2`
- `cr-j-molp-2020-06-010-f7`
- `cell-specialization-and-coordination-in-arabidopsis-leaves-upon-pathogenic-attac-f1`
- `single-cell-rna-sequencing-profiles-reveal-the-developmental-landscape-of-the-i-f1`

**领域特异性**：领域特异读出：细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位

**原始断言（摘自证据页，供核对）**
> Broadly assessing overall signaling strength within cell types longitudinally, we found that the magnitude of incoming and outgoing signaling was reduced during peak fibrosis compared to saline-treated control lungs, with further relative decline in signaling strength by day 63 (Supplemental Fig.
> <sub>来源：`ms-10-1038_s41598-026-75301-w-f2`</sub>


### H2：EPF1（必要性检验）

**假说**：EPF1 在 4 项研究中被提名参与本主题，但本簇证据中未见在统一背景下检验其必要性的操纵实验（受检索覆盖限制，需回溯原文复核）。判别性检验：获得功能缺失等位基因，做表型、回补与组织特异性验证。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织在 >=2 个独立数据集（不同物种/平台/实验室）中的注释结果 |
| 操纵或比较变量 | 注释方案与聚类参数（参照标记集 vs 数据集自有注释），或细胞类型特异扰动 |
| 对照 | 同一批数据换用第二套标记集/第二平台复核，作为内部对照 |
| 读出 | 细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位（至少两项独立读出交叉验证） |
| 若假说为真 | 功能缺失等位基因产生稳定、可回补的表型缺陷 |
| 若假说为假 | 功能缺失无表型，或表型不可回补（提示脱靶或冗余基因补偿） |

**证据基础**：4 条证据 / 4 篇独立论文（置信度：中）
- `ref-s41586-025-08941-z-f3`
- `daily-40904198-f6`
- `ref-pbi-13891-f1`
- `cr-j-molp-2020-06-010-f3`

**领域特异性**：领域特异读出：细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位

**原始断言（摘自证据页，供核对）**
> Our results show that SPCH displays a pattern similar to that of ERL1, EPF1, and HDG2 along pseudotime progression (Figure 7A and 7B).
> <sub>来源：`cr-j-molp-2020-06-010-f3`</sub>


### H3：RVE1（必要性检验）

**假说**：RVE1 在两项研究中被提名参与本主题，但本簇证据中未见在统一背景下检验其必要性的操纵实验（受检索覆盖限制，需回溯原文复核）。判别性检验：获得功能缺失等位基因，做表型、回补与组织特异性验证。

**为什么值得做（证据缺口）**

- 仅 2 篇独立论文支撑，复现性未经第三方验证
- 现有证据以表达/关联为主，缺少遗传操纵的因果证据

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织在 >=2 个独立数据集（不同物种/平台/实验室）中的注释结果 |
| 操纵或比较变量 | 注释方案与聚类参数（参照标记集 vs 数据集自有注释），或细胞类型特异扰动 |
| 对照 | 同一批数据换用第二套标记集/第二平台复核，作为内部对照 |
| 读出 | 细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位（至少两项独立读出交叉验证） |
| 若假说为真 | 功能缺失等位基因产生稳定、可回补的表型缺陷 |
| 若假说为假 | 功能缺失无表型，或表型不可回补（提示脱靶或冗余基因补偿） |

**证据基础**：4 条证据 / 2 篇独立论文（置信度：低）
- `daily-42288963-f5`
- `arabidopsis-sam-scrna-f7`
- `daily-42288963-f2`
- `daily-42288963-f1`

**领域特异性**：领域特异读出：细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位

**原始断言（摘自证据页，供核对）**
> Although SLIM1, RVE1, and RVE8 bind to the promoters of OAS cluster genes, only SLIM1 plays a role in their regulation by OAS, and its effects are gene specific.
> <sub>来源：`daily-42288963-f2`</sub>


### H4：B104（必要性检验）

**假说**：B104 在 3 项研究中被提名参与本主题，但本簇证据中未见在统一背景下检验其必要性的操纵实验（受检索覆盖限制，需回溯原文复核）。判别性检验：获得功能缺失等位基因，做表型、回补与组织特异性验证。

**为什么值得做（证据缺口）**

- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织在 >=2 个独立数据集（不同物种/平台/实验室）中的注释结果 |
| 操纵或比较变量 | 注释方案与聚类参数（参照标记集 vs 数据集自有注释），或细胞类型特异扰动 |
| 对照 | 同一批数据换用第二套标记集/第二平台复核，作为内部对照 |
| 读出 | 细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位（至少两项独立读出交叉验证） |
| 若假说为真 | 功能缺失等位基因产生稳定、可回补的表型缺陷 |
| 若假说为假 | 功能缺失无表型，或表型不可回补（提示脱靶或冗余基因补偿） |

**证据基础**：3 条证据 / 3 篇独立论文（置信度：中）
- `ref-s41477-025-02072-z-f3`
- `ref-pbi-14097-f2`
- `ref-s12915-022-01473-2-f4`

**领域特异性**：领域特异读出：细胞类型比例、标记基因特异度、聚类稳定性（ARI/NMI）、空间共定位

**原始断言（摘自证据页，供核对）**
> In each of the homologous cell types, we found that 79%–95% of expressed genes were shared between B104 and Qi319 for the seven cell types upon Fv treatment and mock condition (Figure S2e,f).
> <sub>来源：`ref-pbi-14097-f2`</sub>


### H5：组织解离方式（原生质体 vs 细胞核）（解离偏好）

**假说**：本主题 19 条证据涉及组织解离，其中原生质体法 7 条、细胞核法 16 条，而在同一份组织内并列比较两者的仅 4 条。因此"原生质体法报告的细胞类型比例能否在细胞核法数据中重现"在本库中没有对照证据；解离偏好与真实的生物学差异目前不可分离。判别性检验：同一样本分半，分别建库，比较类型比例与标记基因表达的一致性。

**为什么值得做（证据缺口）**

- 原生质体法 7 条、细胞核法 16 条，直接并列比较仅 4 条
- 缺少同一样本分半的设计，解离偏好与组织真实构成无法区分

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织的同一样本分半，分别做原生质体与细胞核建库 |
| 操纵或比较变量 | 解离方式（唯一变量）：原生质体酶解 vs 细胞核提取；建库与聚类流程保持一致 |
| 读出 | 类型比例偏差、标记基因表达相关性、类型级召回率 |
| 若假说为真 | 两种方式给出的类型比例偏差落在预注册容差内（例如每类 ±10 个百分点），且标记基因表达高度相关 |
| 若假说为假 | 某一类细胞在原生质体数据中系统性富集或缺失，且偏差随酶解时间或渗透压条件变化，说明是解离偏好而非生物学差异 |

**证据基础**：19 条证据 / 15 篇独立论文（置信度：高）
- `poplar-xylem-sc-spatial-gb-f5`
- `ref-s41592-025-02900-2-f2`
- `differential-accessibility-regulates-cell-type-expression`
- `a-3d-gene-expression-atlas-of-the-floral-meristem-based-on-spatial-reconstructio-f2`
- `ref-erae107-f3`
- `poplar-xylem-sc-spatial-gb-f6`

**领域特异性**：领域特异读出：类型比例偏差、标记基因表达相关性、类型级召回率（本条正文命中：细胞类型比例、标记基因、解离偏好）

**原始断言（摘自证据页，供核对）**
> The snRNA-seq data from intact leaves exhibited slight upregulation of wound-response genes, part of the protoplasting-induced gene set, suggesting that nuclear isolation during snRNA-seq preparation can also elicit a mild protoplasting response (that is, part of the protoplasting-affecting genes;
> <sub>来源：`ref-s41592-025-02900-2-f2`</sub>


### H6：细胞类型的空间定位（空间核实）

**假说**：本主题 16 条证据（12 篇）涉及空间转录组或原位杂交，其中 8 条同时描述单细胞数据与空间数据。本库中未见报道在两个独立空间数据集上比较同一类型空间分布的条目（受检索覆盖限制），因此"scRNA-seq 定义的类型在组织中占据可复现位置"这一前提在本库中仍属单向支持。判别性检验：在两个独立空间数据集上用同一标记集重注释，比较类型—位置对应关系。

**为什么值得做（证据缺口）**

- 空间证据仅来自 12 篇论文，跨数据集比较为 0 条
- 缺少统一的类型—位置映射标准，平台间分辨率差异未评估

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同一组织的 >=2 个独立空间转录组数据集（尽可能含两个平台） |
| 操纵或比较变量 | 空间平台与样本来源（唯一变量）；重注释使用同一标记集 |
| 读出 | 类型—位置对应率、空间邻域富集、跨数据集一致性 |
| 若假说为真 | 关键类型在两个独立空间数据集中的分布（层、区、邻域富集）一致，且与标记基因表达位置吻合 |
| 若假说为假 | 同一类型在不同数据集定位到不同区域，或某类型在空间数据中缺乏对应信号，说明注释粒度或取样存在偏差 |

**证据基础**：16 条证据 / 12 篇独立论文（置信度：高）
- `ref-science-aaa6090-f3`
- `ref-science-aaa6090-f1`
- `introducing-single-cell-stereo-sequencing-technology-to-transform-the-plant-tran-f5`
- `arabidopsis-root-organ-scale-atlas`
- `daily-42028465-f4`
- `seurat-v3-spatial-imputation`

**领域特异性**：领域特异读出：类型—位置对应率、空间邻域富集、跨数据集一致性（本条正文命中：标记基因、空间定位、单细胞）

**原始断言（摘自证据页，供核对）**
> Here, we report multiplexed error-robust FISH (MERFISH), a highly multiplexed smFISH imaging method that substantially increases the number of RNA species that can be simultaneously imaged in single cells by using combinatorial labeling and sequential imaging with error-robust encoding schemes.
> <sub>来源：`ref-science-aaa6090-f3`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-28；生成器版本 2026-11-02-evidence-grounded*
