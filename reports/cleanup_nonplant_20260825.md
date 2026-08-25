# 知识库非植物期刊污染清理报告 (2026-08-25)

## 清理总量

| 批次 | 判定口径 | 概念页 | evidence |
|------|----------|--------|----------|
| 第1批 | 非植物期刊 + 内容无植物 | 264 | 502 |
| 第2批 | 肿瘤/分子医学等明确医学期刊 | 74 | 368 |
| 第3批 | 垃圾期刊 + 内容二次校验无植物 | 209 | 495 |
| **合计** | | **547** | **1365** |

## 清理后规模

- 概念页: 3714 → **3167**
- Evidence: 13232 → **11867**
- Entities: 128（不变）
- Synthesis: 8（不变）

## 已删典型污染期刊

Fuel(燃料)、Oncology系列(肿瘤)、Molecular Medicine/Hepatology/Diabetes/Immunology(医学)、Materials Science/Chemical Engineering(材料化工)、To Improve the Academy(教育学)、Zenodo(预印本AI垃圾)、Drug Delivery、Nuclear Engineering 等。

## 保留(未删)的边界类别

- **期刊非植物但内容含植物物种词** 的论文(可能为植物免疫/植物药/植物生物质跨界研究)
- **植物相关期刊**：PNAS、Frontiers in Microbiology(部分)、Food Chemistry、Chem Ecology、Ethnopharmacology 等

## 隔离与恢复

- 所有删除文件移至 `.trash_nonplant_20260825/{concepts,second_batch/concepts,third_batch/concepts,evidence,...}`
- 恢复：`mv .trash_nonplant_20260825/<batch>/concepts/<file> concepts/papers/`

## 验证

- 断链检查: 0 条 evidence 引用残留
- evidence 可追溯性: 11,867 条中 96%+ 有 source wikilink

## 遗留待办

- 仍有 ~2059 概念页未深度提炼(空壳)，其中相当比例可能是低质量导入，需进一步甄别
- 8 个 synthesis 页的 evidence 计数需用 `batch_synthesis.py --update` 刷新
- 建议加固 daily_update.py 的非植物期刊过滤，防止新污染