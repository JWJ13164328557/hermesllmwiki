---
title: "Hypotheses: Stress & Immunity"
title_zh: "逆境与免疫：可证伪假说"
type: hypothesis
topic: "stress-immunity"
theme_basis: "tag"
total_evidence: 116
total_papers: 31
total_hypotheses: 3
specificity_domain: 3
specificity_generic: 0
auto_generated: true
generator: "batch_hypotheses.py (evidence-grounded, 2026-11-02)"
updated: 2026-11-03
---

# 💡 Stress & Immunity — 可证伪假说（3 条）

> 生成口径：主题内 116 条证据 / 31 篇独立论文（主题归属依据：证据标签）。
> 每条假说只在"≥3 条证据且 ≥2 篇独立论文"时生成，并附证据 ID 与证伪条件。
> 本页是**机器生成的候选清单**，不是经同行评议的结论；引用前须回原文核对。

## 主题覆盖概览

| 项目 | 值 |
|---|---|
| 主题 | Stress & Immunity |
| 证据条目 | 116 |
| 独立论文 | 31 |
| 生成假说 | 3 |
| 其中主题专用方案 | 3 |
| 其中缺省回退方案（需改写） | 0 |
| 主题归属依据 | 证据标签 |

### H1：HDA6 → 茉莉酸响应（方向裁决）

**假说**：HDA6 正向促进茉莉酸响应。判别性检验：在 Arabidopsis thaliana 中敲低或敲除 HDA6，茉莉酸响应应下降；恢复表达应使其回升。

**为什么值得做（证据缺口）**

- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同生育期材料；标准化接种/胁迫处理（>=3 生物学重复） |
| 操纵或比较变量 | HDA6 的敲除/敲低、过表达，或效应子/无毒基因组合 |
| 对照 | 野生型 + 空载体；mock 接种与未胁迫对照 |
| 读出 | 病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达（至少两项独立读出交叉验证） |
| 若假说为真 | 敲低/敲除株系中茉莉酸响应显著下降且可被回补，过表达株系上升 |
| 若假说为假 | 遗传操纵后茉莉酸响应无方向一致的变化，或变化与 HDA6 的表达量无关 |

**证据基础**：7 条证据 / 4 篇独立论文（置信度：中）
- `ref-tpc-104-028514-f8`
- `ref-pp-107-111674-f6`
- `ref-psb-5-10-13168-f3`
- `ref-psb-5-10-13168-f2`
- `ref-psb-5-10-13168-f1`
- `ref-nph-70171-f5`

**领域特异性**：领域特异读出梯度：病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达

**原始断言（摘自证据页，供核对）**
> Recently, it was demonstrated that HDA6 can interact with CORONATINE-INSENSITIVE1 (COI1), an F-box protein that is involved in jasmonate (JA)-mediated plant defense responses, suggesting a possible role for HDA6 in plant–pathogen interaction (Devoto et al., 2002).
> <sub>来源：`ref-tpc-104-028514-f8`</sub>


### H2：BAK1（必要性检验）

**假说**：BAK1 在本主题内由 3 条证据支持，其中 3 条为表达/调控型；本簇证据中没有出现遗传操纵的结果，功能必要性因此未在本知识库内被直接检验（受检索覆盖限制，需回溯原文与系统检索复核）。BAK1 属蛋白激酶或受体激酶；判别性检验：用激酶死（K→E/M）突变体判定催化活性是否必需，并做磷酸化位点回补与配体/下游响应检测。

**为什么值得做（证据缺口）**

- 仅 2 篇独立论文支撑，复现性未经第三方验证
- 现有证据以表达/关联为主，缺少遗传操纵的因果证据
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同生育期材料；标准化接种/胁迫处理（>=3 生物学重复） |
| 操纵或比较变量 | BAK1 的敲除/敲低、过表达，或效应子/无毒基因组合 |
| 对照 | 野生型 + 空载体；mock 接种与未胁迫对照 |
| 读出 | 病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达（至少两项独立读出交叉验证） |
| 若假说为真 | 激酶死突变体不回补表型，而磷酸化位点回补可部分或完全恢复 |
| 若假说为假 | 催化/结合缺陷与野生型表现无差异，说明该结构域非必需或存在旁路 |

**证据基础**：3 条证据 / 2 篇独立论文（置信度：低）
- `ref-nph-70171-f8`
- `ref-j-freeradbiomed-2012-10-5-f6`
- `ref-j-freeradbiomed-2012-10-5-f1`

**领域特异性**：领域特异读出梯度：病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达

**原始断言（摘自证据页，供核对）**
> It is also noteworthy that BAK1 (also known as SERK3), a co-receptor involved in recognizing many microbederived molecules, plays a key role in transducing immune signals (Chinchilla et al., 2009).
> <sub>来源：`ref-nph-70171-f8`</sub>


### H3：AtCESA1（必要性检验）

**假说**：AtCESA1 在本主题内由 3 条证据支持，其中 2 条为表达/调控型；本簇证据中没有出现遗传操纵的结果，功能必要性因此未在本知识库内被直接检验（受检索覆盖限制，需回溯原文与系统检索复核）。AtCESA1 属纤维素合酶；判别性检验：用催化死突变体配合细胞壁组分定量（纤维素含量、结晶度）与同位素标记通量测定。

**为什么值得做（证据缺口）**

- 仅 2 篇独立论文支撑，复现性未经第三方验证
- 缺少蛋白—DNA 或蛋白—蛋白互作证据，调控是直接还是间接未知
- 缺少细胞类型/空间分辨率，无法判定效应发生在哪类细胞

**可证伪检验**
| 要素 | 内容 |
|---|---|
| 数据/体系 | 同物种、同生育期材料；标准化接种/胁迫处理（>=3 生物学重复） |
| 操纵或比较变量 | AtCESA1 的敲除/敲低、过表达，或效应子/无毒基因组合 |
| 对照 | 野生型 + 空载体；mock 接种与未胁迫对照 |
| 读出 | 病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达（至少两项独立读出交叉验证） |
| 若假说为真 | 催化死突变体细胞壁纤维素含量不变，说明表型来自非催化功能 |
| 若假说为假 | 催化/结合缺陷与野生型表现无差异，说明该结构域非必需或存在旁路 |

**证据基础**：3 条证据 / 2 篇独立论文（置信度：低）
- `banana-manac1-activates-secondary-cell-wall-f2`
- `ref-15592324-2015-1011949-f3`
- `banana-manac1-activates-secondary-cell-wall-f5`

**领域特异性**：领域特异读出梯度：病情指数/菌量 CFU、活性氧爆发、电解质渗漏、抗性基因表达

**原始断言（摘自证据页，供核对）**
> We found that the expression levels of AtCESA1, 2, 3, Figure 5.
> <sub>来源：`banana-manac1-activates-secondary-cell-wall-f5`</sub>





## 使用方式

1. 先按"证据缺口"排序：单一物种、单篇论文、缺因果证据的假说优先补验证；
2. 每条假说的"若假说为假"一栏即为**止损条件**，实验设计阶段就应确定样本量；
3. 证据 ID 可直接在 `evidence/` 下打开原文摘要核对，禁止跳过核对直接引用。

---
*由 Phase 8 生成于 2026-11-03；生成器版本 2026-11-02-evidence-grounded*
