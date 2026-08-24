---
title: 植物单细胞知识库 Workflow SOP
created: 2026-05-29
type: overview
tags: [sop, workflow]
---
安装教程参考 https://jishuzhan.net/article/2050778754440560641
Hermes Agent LLM Wiki + Obsidian Git 免费替代 Obsidian Sync：保姆级配置教程

# 植物单细胞知识库 Workflow SOP

## 一、知识库终态

| 指标 | 数值 |
|------|------|
| 总文献 | 761 篇 (+ 用户补充) |
| 含 DOI | 90% |
| PMC 全文 | 289 |
| 深度提炼 | 100% |
| 语义链接 | 100% (6454 links) |
| 中文别名 | 99.7% |
| 主题标签 | 16色 |

## 二、完整搭建流程

### Phase 1: 初始化

```
1. 安装 Obsidian + 初始化 Vault @ G:\hermes_obsidian\hermes
2. git init + GitHub私有仓库 (JWJ13164328557/hermesllmwiki)
3. 创建基础结构: concepts/, raw/, entities/, overview/, diagrams/
4. 编写 SCHEMA.md + index.md + log.md
```

### Phase 2: 文献导入 (微信→知识库)

```
1. 微信推文 URL → curl 抓取正文
2. 提取论文标题/作者/期刊/DOI
3. 保存 raw/articles/ (原始微信正文)
4. 创建 concepts/ (文献笔记)
5. PubMed/Crossref 匹配 DOI → 补全完整元数据
```

### Phase 3: 参考文献与交叉引用

```
1. 从已匹配DOI的论文 → Crossref获取参考文献列表
2. 去重 → 导入高引用文献为concepts/
3. 基于物种+主题建立语义交叉引用 (wikilinks)
4. 配置16色主题图谱 (graph.json)
```

### Phase 4: 全文与深度提炼

```
1. PMC OA → 下载完整全文 HTML
2. Europe PMC → 补充OA论文
3. Semantic Scholar → 检测OA状态
4. 基于完整标题/摘要 → 自动提取物种+方法+核心发现
```

### Phase 5: 自动化流水线

```
1. daily_update.py: PubMed API 检索 (11组策略)
2. pubmed_fulltext.py: PMC全文下载
3. deep_curate_fulltext.py: 基于正文的深度提炼
4. 语义交叉引用重建
5. cron 每天 8:00 → daily_cron.sh --backfill
```

## 三、脚本清单

| 脚本 | 位置 | 功能 |
|------|------|------|
| `pubmed_爬虫.py` | G:/hermes_obsidian/ | PubMed HTML 爬虫 (BeautifulSoup) |
| `daily_update.py` | scripts/ | PubMed API 检索+导入 (11策略×3年) |
| `daily_cron.sh` | scripts/ | cron 入口, 6步流水线 |
| `pubmed_fulltext.py` | scripts/ | PMC完整全文下载 |
| `deep_curate_fulltext.py` | scripts/ | 基于正文的深度提炼 |
| `batch_translate.py` | scripts/ | 批量中文翻译 (mymemory API) |
| `pubmed_enrich.py` | scripts/ | PubMed爬虫补全元数据 |

## 四、文献标准模板

```yaml
---
title: "文献标题"
created: YYYY-MM-DD
type: concept
tags: [development, metabolism]
doi: 10.xxxx/xxxxx
pmid: 12345678
aliases: ["中文标题"]
confidence: high
---

# 文献标题 (中文优先)

## 论文信息
- 期刊/DOI/PMID/作者

## 摘要

## 深度提炼
**物种**: Arabidopsis, rice
**方法**: scRNA-seq
### 核心发现
- 发现1

## 相关文献
- [[linked-paper]] 🌱shared-species
```

## 五、每日维护操作

| 操作 | 命令 |
|------|------|
| 每日自动 | cron 8:00 (无需手动) |
| 手动回填 | `./scripts/daily_cron.sh --backfill` |
| 补全全文 | `python3 scripts/pubmed_fulltext.py --enrich-all` |
| 重建链接 | `python3 -c "..."` (语义交叉引用脚本) |
| 导入新论文 | 提供 DOI/PMID/PDF |

## 六、图谱配置

```
1. .obsidian/graph.json → 16色主题 (自动生成)
2. 设置 → 图谱 → Show aliases ✅ + Show tags ✅
3. 颜色: 发育#27AE60 胁迫#DC143C 代谢#8B008B 光#DAA520 等16色
4. 交叉引用: 物种×5 + 主题标签×3
```

## 七、目录结构

```
hermes_obsidian/
├── concepts/         ← 文献笔记 (含深度提炼+语义链接)
├── raw/articles/     ← 微信/PubMed 原始正文
├── raw/papers/       ← PDF原文
├── overview/         ← 10篇全景综述
├── entities/         ← 基因/蛋白/课题组
├── diagrams/         ← 6幅 Excalidraw 通路图
├── research_proposals/ ← 研究方案
├── scripts/          ← 自动化脚本
├── .obsidian/graph.json ← 图谱16色
├── SCHEMA.md         ← 知识库规范
├── index.md          ← 文献索引
└── SOP.md            ← 本文档
```
