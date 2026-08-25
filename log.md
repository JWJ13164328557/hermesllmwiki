# Wiki Log

> 按时间顺序的操作记录。只追加。
> 格式: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete

## [2026-05-28] create | Wiki initialized
- Domain: 科学研究与技术笔记
- Vault: G:\hermes_obsidian\hermes
- GitHub: JWJ13164328557/hermesllmwiki
- Structure created with SCHEMA.md, index.md, log.md, raw/, entities/, concepts/, comparisons/, queries/

## [2026-05-28] ingest | OsbHLH150水稻耐冷机制 (Plant Communications 2026)
- Source: https://mp.weixin.qq.com/s/0kDqKHw6faI2sBLWvQfGXA
- Created:
  - raw/articles/osbhlh150-rice-chilling-tolerance-wechat.md
  - entities/osbhlh150.md
  - entities/osmapk3-rice.md
  - entities/osnced3-rice.md
  - entities/guangxi-university-luo-lab.md
  - concepts/rice-chilling-tolerance.md
  - concepts/aba-biosynthesis-stress.md
- Updated: index.md

## [2026-05-28] ingest | 地钱单细胞细胞周期 (The Plant Cell, Cambridge)
- Source: https://mp.weixin.qq.com/s/ksd5PLavrhDzQO1XnHwCEg
- Created:
  - raw/articles/marchantia-cell-cycle-scrna-plantcell.md
  - entities/marchantia-polymorpha.md
  - entities/mpcycd1.md
  - entities/mpcyca.md
  - entities/mpcycb1.md
  - concepts/plant-cell-cycle-control.md
  - concepts/cell-cycle-scrna-seq.md
- Updated: index.md
- Core: 地钱极简系统—每时期单一cyclin主导(MpCYCD;1/MpCYCA/MpCYCB;1), scRNA-seq + 活体成像

## [2026-05-28] ingest | 植物单细胞/空间组学文献批量入库 (15篇)
- Sources: 15篇微信文章 (mp.weixin.qq.com)
- Created: 15 raw + 15 concept pages
- 涵盖主题:
  - 发育: QC发育轨迹, 茶叶茸毛, 番木瓜假种皮, 杨树木质部, 拟南芥SAM, 水稻节点
  - 胁迫: 水稻稻瘟病, 烟草抗虫, 珍珠粟热应激, 苜蓿镉胁迫, 小麦盐胁迫
  - 代谢/工具: 丹参丹参酮空间代谢, 烟草叶角代谢, PlantCellChat R包
  - 进化/基因组: 葡萄泛基因组+snRNA, 水稻节点多组学
- Updated: index.md

## [2026-05-28] ingest | 植物单细胞/空间文献批量入库 batch2 (19篇)
- Sources: 19篇微信文章
- Created: 19 raw + 19 concept pages
- 亮点: Nature Plants干旱, Mol Plant兰花+根再生, Genome Biol芦苇B+杨树木质部
- Updated: index.md

## [2026-05-28] ingest | 植物单细胞/空间文献批量入库 batch3 (39篇)
- Sources: 39篇微信文章
- Created: 39 raw + 39 concept pages
- Highlights: Nat Methods FlowSig, Cell尼古丁, Nat Plants×2, Genome Biol×3, PBJ×3, Plant Cell×3, Adv Sci×2
- Updated: index.md

## [2026-05-28] ingest | 植物单细胞/空间文献批量入库 batch4 (23篇)
- Sources: 25篇微信文章 (2篇被反爬拦截)
- Created: 23 raw + 23 concept pages
- Highlights: Nat Comm玉米胚胎sc+空间, Nature Plant水稻scATAC, Nature种子萌发sc, 艾蒿/青蒿素/麦穗
- Updated: index.md

## [2026-05-28] organize | 知识库主题整理
- 创建 plant-sc-landscape 全景综述页
- 重组织 index.md: 按六大主题归类
- 统计: 100篇, scRNA-seq(91)+空间(22), 15+物种

## [2026-05-28] ingest | 大豆专题文献批量入库 (16篇)
- Cell×3(Mol Cell), MP Soybean Atlas, PBJ×2, Plant Commun, Adv Sci, JIPB综述
- 涵盖: 大豆时空图谱/sc图谱、异黄酮/油脂代谢、根瘤、SMV胁迫、叶形态
- 127页

## [2026-05-29] organize | SCHEMA 全库重组 — 目录分层 + wikilink 修复

### Moved
- concepts/*.md (924 files) → concepts/papers/ (884) + concepts/methods/ (40)
- entities/*.md (8 files) → entities/genes/ (6) + entities/species/ (1) + entities/labs/ (1)
- overview/*.md (10 files) → overview/species/ (5) + overview/themes/ (4) + overview/tissues/ (1)

### Created
- 15 directories per SCHEMA.md spec (concepts/papers, concepts/methods, entities/genes, entities/proteins, entities/cell-types, entities/species, entities/datasets, entities/labs, datasets/, overview/species, overview/tissues, overview/themes, raw/supplements, raw/figures, raw/datasets)

### Updated
- deep_curate_fulltext.py: scan papers/ + methods/ subdirs
- daily_update.py: write to concepts/papers/
- 5 files with path-based wikilinks → slug-only format
- index.md: rewritten per SCHEMA template
- log.md: this entry

### Lint
- 0 broken links (verified)
- SCHEMA compliance: 12% → 100%

### Metadata
- 924 concepts (884 papers + 40 methods)
- 1,133 total markdown files

## [2026-05-29] create | AGENT.md P0 activation — Denyer 2019 full Paper Spec trial

### Created
- evidence/ (3 objects), relationships/, synthesis/, hypotheses/, research-programs/

### Updated
- concepts/papers/xr-10-1016-j-devcel-2019-02-022.md → full Paper Spec (9 sections)
- entities/cell-types/quiescent-center.md → Entity Spec format
- index.md + log.md

### Evidence Created
- [[evidence/arabidopsis-root-has-15-cell-types]] (observation, consensus=established)
- [[evidence/qc-cells-transcriptionally-distinct]] (observation, consensus=established)
- [[evidence/root-differentiation-continuous-trajectories]] (association, consensus=strong)

### Notes
- Establishes template for future AGENT.md-compliant paper ingests
- 2 evidence objects pending (TF waves, lineage-specific networks)

## 2026-05-30 | P1-P4 全量知识库整理完成

### Added
- P1: 80篇 PMID 论文 → 9-section Paper Spec (33 PMC全文 + 47 PubMed摘要)
- P2: 56篇 DOI 论文 → 54篇发现 PMID 升级至 P1
- P3: 214篇无标识论文 → Enhanced Frontmatter + 结构化摘要
- P4a: 5 Synthesis pages (Root/Methods/Regeneration/Vascular/Hormone)
- P4b: 4 Entity hubs (Soybean/Vascular/Methods/Root Development)
- P4c: 3 Relationship matrices (Species×CellType, Gene×Function, Method×App)
- P4d: 1 Hypothesis Portfolio (soybean internode light quality)
- P4e: 1 Research Program (soybean internode light quality)

### Updated
- Evidence Objects: 68 → 486 (+615%)
- Deep papers (>5KB): 25 → 248+
- Synthesis pages: 2 → 7
- Entity hubs: 8 → 12
- Relationship pages: 1 → 4

### Notes
- PMC full text 成功下载 33 篇
- 54 篇论文通过 DOI→PMID 转换发现新 PMID
- GitHub push 因 WSL 网络不稳定部分超时，commit 已保存本地
- 15 篇论文仍仅 frontmatter（<1KB），需人工处理

### Evidence Created (2026-05-30)
- Metabolism papers: 1275 evidence objects from 153 papers
- Top genes: MeJA, VvMYBA1, CsGGT2, OsESV1, OsLESV, VviERF003, PbrNSC, CsGGT4, CsMYB73, VviGT14...
- Top compounds: anthocyanin, flavonoid, ethylene, carotenoid, lignin, starch, auxin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Relationships Created (2026-05-30)
- 0 relationship pages from metabolism evidence
- Types: regulation, interaction, requirement

### Synthesis Created (2026-05-30)
- plant-metabolism.md: synthesis from 1,275 evidence objects
- 9 thematic areas, 40 regulatory genes, 20 metabolites

### Relationships (2026-05-30)
- metabolism-gene-compound: 188 gene-compound pairs
- metabolism-gene-network: gene co-occurrence from 1275 evidence
- Top gene: MeJA (15 evidence)

### New Batch Evidence (2026-05-30)
- 103 papers → 1173 evidence objects
- 14 gene entity pages
- Top genes: PtrCCC, GmZF, OsSPL9, NaCl, AtHD2C, MetaNeighbor, OsGATA6, ChIP, MacAlister, NuRD...

### Evidence Created (2026-05-31)
- Metabolism papers: 1275 evidence objects from 153 papers
- Top genes: MeJA, VvMYBA1, CsGGT2, OsLESV, OsESV1, VviERF003, PbrNSC, CsGGT4, CsMYB73, VviGT14...
- Top compounds: anthocyanin, flavonoid, ethylene, carotenoid, lignin, starch, auxin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-05-31)
- Metabolism papers: 1275 evidence objects from 153 papers
- Top genes: MeJA, VvMYBA1, CsGGT2, OsESV1, OsLESV, VviERF003, PbrNSC, CsGGT4, CsMYB73, VviGT14...
- Top compounds: anthocyanin, flavonoid, ethylene, carotenoid, lignin, starch, auxin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-05-31)
- Metabolism papers: 1275 evidence objects from 153 papers
- Top genes: MeJA, VvMYBA1, CsGGT2, OsLESV, OsESV1, VviERF003, PbrNSC, CsMYB73, CsGGT4, VviGT14...
- Top compounds: anthocyanin, flavonoid, ethylene, carotenoid, lignin, starch, auxin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-05-31)
- Metabolism papers: 1275 evidence objects from 153 papers
- Top genes: MeJA, VvMYBA1, CsGGT2, OsLESV, OsESV1, VviERF003, PbrNSC, CsGGT4, CsMYB73, VviGT14...
- Top compounds: anthocyanin, flavonoid, ethylene, carotenoid, lignin, starch, auxin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-01)
- Metabolism papers: 1050 evidence objects from 153 papers
- Top genes: VvMYBA1, MeJA, CsGGT2, OsLESV, OsESV1, CsMYB73, VviGT14, VviERF003, CsAN1, SlBEL11...
- Top compounds: anthocyanin, ethylene, flavonoid, starch, carotenoid, auxin, lignin, phenolic, cellulose, flavonol...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-01)
- Papers with findings: 443
- Evidence objects: 2765
- Top genes: VvMYBA1, MeJA, CsGGT2, OsESV1, OsLESV, CsMYB73, ChIP, VviERF003, VviGT14, CsAN1...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, carotenoid, cellulose, phenolic...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-01)
- Papers with findings: 288
- Evidence objects: 1648
- Top genes: NuRD, ChIP, GoHSFA4a, GmZF, DcbHLH2, DcbHLH5, PsbZIP10, PsbZIP1, FunTFBS, AtGCN5...
- Top compounds: auxin, ethylene, flavonoid, terpenoid, sucrose, suberin, phenylpropanoid, abscisic acid, ginsenoside, anthocyanin...
- Entity pages: 38 (genes + compounds)

### Evidence Created (2026-06-01)
- Papers with findings: 539
- Evidence objects: 3514
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsLESV, OsESV1, CsMYB73, VviERF003, VviGT14...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-01)
- Papers with findings: 550
- Evidence objects: 3584
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsESV1, OsLESV, CsMYB73, VviGT14, VviERF003...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-01)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsESV1, OsLESV, CsMYB73, VviGT14, VviERF003...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-03)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsESV1, OsLESV, CsMYB73, VviERF003, VviGT14...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-03)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsLESV, OsESV1, CsMYB73, VviGT14, VviERF003...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-03)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsLESV, OsESV1, CsMYB73, VviERF003, VviGT14...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-03)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsESV1, OsLESV, CsMYB73, VviERF003, VviGT14...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-04)
- Papers with findings: 557
- Evidence objects: 3712
- Top genes: ChIP, VvMYBA1, MeJA, AtGCN5, CsGGT2, OsLESV, OsESV1, CsMYB73, VviGT14, VviERF003...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, cellulose, carotenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-04)
- Papers with findings: 604
- Evidence objects: 4270
- Top genes: ChIP, VvMYBA1, OpAVT1, SlSPY, MeJA, AtGCN5, CsGGT2, SlSEC1, OsLESV, OsESV1...
- Top compounds: auxin, anthocyanin, ethylene, flavonoid, lignin, starch, sucrose, wax, cellulose, carotenoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-05)
- Papers with findings: 344
- Evidence objects: 2264
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, flavonoid, sucrose, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-06)
- Papers with findings: 344
- Evidence objects: 2263
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-07)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-09)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-10)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-15)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-16)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-17)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-18)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-19)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-06-20)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-07-23)
- Papers with findings: 340
- Evidence objects: 2259
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-07-25)
- Papers with findings: 339
- Evidence objects: 2252
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-07-26)
- Papers with findings: 339
- Evidence objects: 2252
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-07-27)
- Papers with findings: 339
- Evidence objects: 2252
- Top genes: ChIP, AtGCN5, OpAVT1, PeCHYR1, AtE2Fc, NuRD, AnaII, GoHSFA4a, VvNPF3, LhG4...
- Top compounds: auxin, ethylene, suberin, sucrose, flavonoid, terpenoid, abscisic acid, lignin, wax, phenylpropanoid...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-08-24)
- Papers with findings: 872
- Evidence objects: 5339
- Top genes: ChIP, TfR1, AtGCN5, OpAVT1, NaCl, PeCHYR1, SphK2, AtE2Fc, NuRD, HepG2...
- Top compounds: auxin, glucose, ethylene, flavonoid, sucrose, cellulose, phenylpropanoid, lignin, terpenoid, wax...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-08-24)
- Papers with findings: 1549
- Evidence objects: 9738
- Top genes: ChIP, TfR1, VvMYBA1, MeJA, OpAVT1, AtGCN5, CsGGT2, NaCl, OsESV1, OsLESV...
- Top compounds: auxin, anthocyanin, glucose, ethylene, flavonoid, lignin, starch, sucrose, cellulose, phenolic...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-08-24)
- Papers with findings: 1603
- Evidence objects: 10127
- Top genes: ChIP, TfR1, VvMYBA1, MeJA, OpAVT1, AtGCN5, CsGGT2, NaCl, OsLESV, OsESV1...
- Top compounds: auxin, anthocyanin, glucose, ethylene, flavonoid, lignin, starch, sucrose, cellulose, phenolic...
- Entity pages: 45 (genes + compounds)

### Evidence Created (2026-08-25)
- Papers with findings: 1627
- Evidence objects: 10282
- Top genes: ChIP, TfR1, VvMYBA1, MeJA, OpAVT1, AtGCN5, CsGGT2, NaCl, OsLESV, OsESV1...
- Top compounds: auxin, anthocyanin, glucose, ethylene, flavonoid, lignin, starch, sucrose, cellulose, phenolic...
- Entity pages: 45 (genes + compounds)

### Relationships (2026-08-25)
- metabolism-gene-compound: 240 gene-compound pairs
- metabolism-gene-network: gene co-occurrence from 9949 evidence
- Top gene: ChIP (26 evidence)
