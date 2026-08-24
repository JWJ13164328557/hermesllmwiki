---
source_url: https://mp.weixin.qq.com/s/_igXoh0eWZRAu9l6Lg-fJg
ingested: 2026-05-28
sha256: placeholder
---

# 文献分享|代谢组学与单细胞转录组学分析揭示艾蒿腺毛的次生代谢物谱及潜在发育动态

文献分享

论文信息

期刊：Plant Biotechnology Journal
题目：Metabolomic and Single-Cell Transcriptomic Analyses Shed Light on Secondary Metabolite Profiling and Potential Developmental Dynamics of Glandular Trichomes in Artemisia argyi
作者：Shuting Dong, Hongyu Chen, Sijie Sun , Miaoxian Guo, Chao Sun, Shilin Chen,  Hongmei Luo
DOI:10.1111/pbi.70362

摘要

    该研究结合代谢组学与单细胞转录组学，解析艾草分泌型腺毛（GTs）的次生代谢特征及发育分子机制。通过 液相色谱 - 质谱（LC-MS） 和 气相色谱 - 质谱（GC-MS） 鉴定出 969 种 GTs 与非分泌型非腺毛（NGTs）的差异积累代谢物，GTs 富集萜类、黄酮类等次生代谢物，其中倍半萜类为最丰富的萜类亚型。构建艾草叶片单细胞转录组图谱，注释出叶肉细胞、表皮细胞等 5 类细胞，并通过亚群分析明确 GTs 细胞类型。拟时间轨迹分析揭示 GTs 连续发育轨迹，筛选出参与 GT 发育的候选转录因子。基于细胞类型特异性共表达网络，鉴定并功能验证了 4 个萜类合酶（TPS）基因：GT 特异性 AarTPS77 催化 β- 石竹烯合成，表皮细胞特异性 AarTPS52 催化 β- 法尼烯合成，AarTPS95 和 AarTPS96 催化吉马酮 A 及 12 种倍半萜合成。研究为艾草次生代谢物合成及 GT 发育的分子机制提供新见解，为提升艾草药材质量奠定基础。

研究思路与方法

一、研究思路
1. 第一阶段：代谢组学对比 —— 明确 GTs 与 NGTs 的代谢差异，锁定核心研究靶标

2. 第二阶段：单细胞转录组构建 —— 解析艾蒿叶片细胞异质性，定位 GTs 对应的细胞群

3. 第三阶段：伪时间轨迹分析 —— 溯源 GTs 发育路径，筛选关键调控转录因子（TFs）

4. 第四阶段：细胞特异性共表达网络与功能验证 —— 解析倍半萜合成机制，确认关键 TPS（萜类合酶） 基因
二、研究方法
代谢组学分析：采用优化的机械分离法（结合蔗糖梯度离心）获取高纯度 GTs 和 NGTs，用 LC-MS 和 GC-MS 检测代谢物；通过 PCA、OPLS-DA 等统计分析筛选 DAMs，KEGG 富集分析解析代谢通路，明确 GTs 代谢特征。
单细胞转录组建库与分析：取艾草组培苗幼叶，酶解（纤维素酶 R-10 + 离析酶 R-10）获得原生质体，用 10X Genomics 平台建库测序；Alevin pipeline 定量数据，Seurat 过滤质控、聚类注释细胞类型，Harmony 校正批次效应。
GTs 发育轨迹解析：采用 Monocle2 工具对 ECs 和 GTs 细胞进行拟时间分析，识别伪时间依赖基因（PDGs）；通过 GO 富集分析 PDGs 功能，结合 TF 家族分类筛选调控 GTs 发育的候选基因。
TPS 基因功能验证：克隆候选 TPS 基因（如 AarTPS77、AarTPS52），构建 phylogenetic 树预测功能；将基因导入大肠杆菌表达重组蛋白，用 HS-SPME-GC/MS 检测酶活产物，验证其催化合成特定萜类的功能。

实验结果

艾草腺毛（GTs）与非腺毛（NGTs）代谢组分析
通过显微镜观察到艾草叶片上 GTs 为多细胞盾形、NGTs 为 T 型，且 NGTs 在叶背密度更高；优化机械分离法获取高纯度 GTs 和 NGTs 后，用 LC-MS 和 GC-MS 共鉴定出 969 种差异积累代谢物（DAMs），其中 GTs 富集 650+103 种 DAMs。GTs 中萜类（占 14.65%，倍半萜为最丰富亚型）、黄酮类（黄酮苷和黄酮醇为主）、脂肪酰类（类二十烷酸和脂肪酸为主）含量显著高于 NGTs，KEGG 富集显示 GTs 在倍半萜 / 三萜合成等次生代谢通路中作用关键。
艾草叶片单细胞转录组图谱构建
以组培苗幼叶为材料，酶解获得原生质体后用 10X Genomics 建库，经质控保留 22032 个高质量细胞，UMAP 聚类得到 18 个细胞簇。通过同源标记基因（如 MCs 的 RBCS1A、ECs 的 FDH）结合 RNA 原位杂交，注释出叶肉细胞（MCs，占比最高）、表皮细胞（ECs）、维管细胞（VCs）等 5 类主要细胞；GO 富集分析显示 MCs 富集光合与萜类合成通路、ECs 富集脂质代谢通路，验证了细胞类型功能特异性。
艾草 GT 细胞类型鉴定
对图 2 中 ECs（Cluster 8）重聚类得到 5 个亚群，发现 EC_1 亚群特异性表达 GT 标记基因（MIXTA1、HD1 等），RT-qPCR 验证这些基因在手动刮取的毛状体（TR）中表达远高于无表皮组织（PNE），确认 EC_1 为 GTs。 bulk RNA-seq 对比显示，含 GTs 的叶柄表皮（PE）在脂肪酸合成、脂质运输通路富集；公共 trichome 转录组数据中，8 个高表达基因（如脂质转移蛋白基因）也在 EC_1 特异表达，进一步佐证 GTs 身份。
艾草 GT 发育轨迹解析
用 Monocle2 对 ECs 和 GTs 进行拟时间分析，构建从 ECs（pre-branch）经分化节点（node 1）向 GTs（State 3）过渡的连续发育轨迹，State 2 为 ECs 与 GTs 的过渡态。识别出 3 个模块的伪时间依赖基因（PDGs），均富集次生代谢相关 GO term；从中筛选出 12 个候选转录因子（如 HD-ZIP 家族 HB-7_1、MYB 家族 MYB306_2、bHLH 家族 MYC2_1），其表达动态与 GT 发育阶段匹配，推测调控 GT 分化。
艾草细胞特异性倍半萜合成验证
代谢组显示 GTs 中倍半萜（如 β- 石竹烯、β- 法尼烯）含量显著高于 NGTs；构建 MVA 通路与 TPS-a 亚家族基因共表达网络，发现 GT 特异性模块含 9 个 MVA 基因和 7 个 TPS 基因。Phylogenetic 分析预测 AarTPS77 为 β- 石竹烯合酶、AarTPS52 为 β- 法尼烯合酶、AarTPS95/96 为吉马酮 A 合酶；体外酶活实验（HS-SPME-GC/MS）验证了它们的催化功能，且 AarTPS95/96 还能微量合成单萜，体现酶功能多样性。
艾草叶片单细胞景观整合示意图
综合前述结果，展示艾草叶片横切面上的主要细胞类型（叶肉细胞、维管细胞、表皮细胞、保卫细胞、GTs/NGTs）；标注 GTs 从表皮细胞分化的发育轨迹，以及细胞特异性倍半萜合成通路（如 GTs 中 AarTPS77、ECs 中 AarTPS52 的作用）；用虚线标注预测的调控 GT 发育的候选转录因子（MYB、bHLH 等），直观呈现 GT 发育与次生代谢的关联。

结论

    本研究阐明，艾蒿腺毛起源于表皮细胞，经 MYB、MYC、HD-ZIP、WRKY 等转录因子动态调控，经历 “表皮维持 - 过渡分化 - 腺毛成熟” 三阶段完成功能特化。代谢上，其作为倍半萜合成核心位点，通过甲羟戊酸（MVA）通路与特异性萜类合酶（TPS）基因（AarTPS77、AarTPS52、AarTPS95/96）协同作用，定向合成 β- 法尼烯、β- 石竹烯、吉玛烯 A 等倍半萜，其中AarTPS95/96兼具多功能催化特性。最终形成 “发育调控与代谢合成耦合” 的分子机制，不仅解析了艾蒿腺毛的代谢特化逻辑，也为植物次生代谢的细胞特异性调控及萜类合成酶功能研究提供了典型范式，同时为合成生物学改造萜类合成提供了靶点与思路。
