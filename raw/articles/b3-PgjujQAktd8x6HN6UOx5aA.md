---
source_url: https://mp.weixin.qq.com/s/PgjujQAktd8x6HN6UOx5aA
ingested: 2026-05-28
sha256: placeholder
---

# 综述：单细胞测序在植物再生研究中的应用：揭示愈伤组织的细胞异质性

单细胞测序 、scRNA-seq高级分析、scATAC-seq、 R包开发、源码拆解、 测试、RNA-seq 、其它生信分析、 R语言 、Python 、环境配置 、文献分享 、 一只羊的碎碎念
愈伤组织作为植物组织培养技术中重要的离体组织，通常由幼嫩的组织在特定激素诱导下脱分化形成，其具有旺盛的分裂能力，并具备分化为不同类型组织及再生完整植株的潜能。它在研究植物细胞多能性、植株再生的分子机制、遗传育种、种质资源保存及工厂化育苗等方面具有重要意义。然而，愈伤组织内部存在高度异质性，传统批量测序难以揭示其细胞类型组成、起源及命运转变的动态调控网络。近年来，单细胞与空间转录组测序（scRNA-seq, ST）技术的应用，为在单细胞分辨率下解析愈伤组织诱导、增殖、再分化和从头器官再生的全过程提供了前所未有的工具，极大地推进了我们对植物细胞全能性和再生机制的理解。缩写
scRNA-seq Single-cell RNA sequencing
单细胞RNA测序
在单个细胞水平上测定其全部转录本（RNA）的技术，用于分析基因表达异质性、鉴定细胞类型和状态。
ST Spatial Transcriptomics
空间转录组学
一种能在保留组织空间位置信息的同时，测量基因表达的技术。
CIM Callus Induction Medium
愈伤组织诱导培养基
含有特定植物激素（通常以生长素为主），用于诱导外植体脱分化形成愈伤组织的培养基。
QC Quiescent Center
静止中心
位于根尖分生组织中心的一小群分裂不活跃的细胞，对维持周围干细胞活性至关重要。
LRPI Lateral Root Primordium Initiation
侧根原基起始
侧根发育的早期阶段，涉及特定细胞的分裂和原基形成。
SE Somatic Embryogenesis
体细胞胚胎发生
体细胞不经过配子融合，直接发育成完整胚胎并再生植株的过程。
NEC Non-Embryogenic Callus
非胚性愈伤组织
缺乏或丧失胚胎发生能力的愈伤组织，通常结构松散，难以再生。
PEC Primary Embryogenic Callus
初级胚性愈伤组织
具有胚胎发生潜能的愈伤组织，是体细胞胚胎发生的关键起始材料。
EC Embryogenic Cells
胚性细胞
具有发育为体细胞胚胎潜力的细胞。
Pro-EC Proembryogenic Cells
前胚性细胞
胚性细胞分化前的过渡状态细胞，对获得胚性能力至关重要。
XPP Xylem Pole Pericycle
木质部极中柱鞘
位于根木质部辐射线外侧的中柱鞘细胞，是侧根和某些愈伤组织形成的重要起源细胞。
TFRN Transcription Factor Regulatory Network
转录因子调控网络
由转录因子及其靶基因构成的，控制特定生物学过程的基因表达调控系统。解析愈伤组织的细胞异质性
多篇研究利用单细胞RNA测序（scRNA-seq）技术，系统绘制了不同植物物种愈伤组织诱导过程中的高分辨率细胞图谱，揭示了愈伤组织内部复杂的细胞组成。
在模式植物拟南芥中，研究表明在愈伤组织诱导培养基上形成的愈伤组织，其细胞结构类似于根原基或根顶端分生组织，包含外层、中间层和内层。其中，中间层细胞表现出类似于根静止中心的转录特征，共表达SCARECROW、WOX5、PLETHORA1/2等标志性基因，并且富集了分生组织和生长素相关的基因本体条目，被证明是能够再生成器官的多能性细胞群。进一步的时间序列单细胞转录组分析（CIM培养0、1、4天）发现了两种关键的过渡细胞类型：具有侧根原基起始类似特征的细胞（LRPI-like cells）和具有根静止中心类似特征的细胞（QC-like cells）。LRPI-like细胞保留了起源组织的部分特征，而QC-like细胞则表现出更高的可塑性（Pluripotency）和更丰富的转录活性，是获得再生能力的关键细胞状态。gura等人的研究揭示，WUSCHEL-RELATED HOMEOBOX 13 (WOX13) 通过抑制 WUS和其他茎尖分生组织调节因子的表达，并激活细胞壁修饰基因，在愈伤组织中负调控从头芽再生。他们的单细胞转录组分析（基于Quartz-Seq2平台）构建了异质愈伤组织的细胞图谱，发现WOX13在决定愈伤细胞群体细胞身份中发挥关键作用，并提出了WUS和WOX13之间的相互抑制构成了多潜能细胞群体中关键的细胞命运决定机制。
在木本植物龙眼的胚性愈伤组织研究中，单细胞转录组分析同样揭示了其高度异质性，共鉴定出12个细胞簇，包括增殖细胞、分生细胞、维管细胞和表皮细胞等群体。其中，增殖细胞簇高表达细胞周期相关基因，而表皮细胞簇则特异表达与角质层蜡质合成和脂肪酸代谢相关的基因（如LTPG、GDSL）。
在棉花中，研究者利用单细胞测序技术对下胚轴组织进行了分析，识别出表皮、皮层、初生木质部、初生韧皮部、形成层和薄壁细胞等多种细胞类型。研究发现，初生维管组织细胞（特别是形成层和维管薄壁细胞）是响应激素诱导、启动细胞重编程的主要细胞类型。在棉花体细胞胚胎发生研究中，通过对非胚性愈伤组织和初级胚性愈伤组织进行scRNA-seq分析，成功区分出胚性细胞、前胚性细胞和脱分化细胞等六个不同的细胞簇，其中前胚性细胞对胚性能力的获得至关重要。
在作物番茄中，Song等人利用空间转录组技术揭示了愈伤组织在芽再生过程中存在高度异质的细胞群体，包括表皮、维管组织、芽原基、内部愈伤和生长中的芽。他们特别鉴定出芽原基周围富集光合作用相关基因的细胞，称为“绿色薄壁细胞”，并证明这些由光诱导的细胞通过可能由糖驱动的TOR信号通路促进芽原基形成和随后的芽再生。这项研究明确了芽原基、绿色薄壁细胞和内部愈伤是受光促进的主要细胞类型，并展示了空间转录组在解析植物再生中细胞类型特异性光调控机制方面的巨大潜力。
上述研究共同表明，愈伤组织并非均一的细胞团，而是由功能各异的细胞亚群构成的空间有序结构，其中某些稀有或特定位置的细胞类型是驱动再生的核心。参考文献
[1]Tang L P, Zhai L M, Li J, et al. Time-resolved reprogramming of single somatic cells into totipotent states during plant regeneration[J]. Cell, 2025, 188(24): 6923-6938.e18.
[2]Liu Z, Zhang Y, Zhao Q, et al. Single-cell RNA sequencing reveals developmental trajectories and environmental regulation of callus formation in Arabidopsis[J]. Stress Biology, 2025, 5(1): 57.
[3]Yin R, Chen R, Xia K, et al. A single-cell transcriptome atlas reveals the trajectory of early cell fate transition during callus induction in Arabidopsis[J]. Plant Communications, 2024, 5(8): 100941.
[4]Zhai N, Xu L. Pluripotency acquisition in the middle cell layer of callus is required for organ regeneration[J]. Nature Plants, 2021, 7(11): 1453-1460.
[5]Ogura N, Sasagawa Y, Ito T, et al. WUSCHEL-RELATED HOMEOBOX 13 suppresses de novo shoot regeneration via cell fate control of pluripotent callus[J]. Science Advances, 2023, 9(27): eadg6983.
[6]Guo H, Zhang L, Guo H, et al. Single-cell transcriptome atlas reveals somatic cell embryogenic differentiation features during regeneration[J]. Plant Physiology, 2024, 195(2): 1414-1431.
[7]Zhu X, Xu Z, Wang G, et al. Single-cell resolution analysis reveals the preparation for reprogramming the fate of stem cell niche in cotton lateral meristem[J]. Genome Biology, 2023, 24(1): 194.
[8] Zhang S, Zhu C, Zhang X, et al. Single-cell RNA sequencing analysis of the embryogenic callus clarifies the spatiotemporal developmental trajectories of the early somatic embryo in dimocarpus longan[J]. The Plant Journal, 2023, 115(5): 1277-1297.
[9]Song X, Guo P, Xia K, et al. Spatial transcriptomics reveals light-induced chlorenchyma cells involved in promoting shoot regeneration in tomato callus[J]. Proceedings of the National Academy of Sciences of the United States of America, 2023, 120(38): e2310163120.
END

#
付费资源
#
推荐阅读
后台发送“目录”，即可获取本公众号已发表文章链接

#
关于我
分享内容：分子标记开发及种质资源鉴定、单细胞多组学数据分析、生信编程、算法原理、文献分享与复现等...

点个赞再走！
