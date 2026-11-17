---
title: Transcriptome co-expression network analysis identifies key genes and regulators of ripening kiwifruit ester biosynthesi
created: 2026-05-30
type: concept
themes: [epigenetics-gene-regulation, metabolism-natural-products]
tags: [metabolism-natural-products, papers]
doi: 10.1186/s12870-020-2314-9
pmid: ''
aliases: [Transcriptome co-表达 网络 分析 identifies 关键 genes and regulators of ripening kiwifruit ester 生物合成]
theme_status: mapped
theme_basis: tag+keyword

---

# Transcriptome co-expression network analysis identifies key genes and regulators of ripening kiwifruit ester biosynthesis

## 论文信息
- **期刊**: BMC Plant Biology (2020)
- **DOI**: [10.1186/s12870-020-2314-9](https://doi.org/10.1186/s12870-020-2314-9)

- **作者**: Aidi Zhang, Qiuyun Zhang, Jianzhao Li, Hansheng Gong, Xinguang Fan, Yanqing Yang

## 物种
Actinidia

## 摘要
Abstract Background Aroma is an important organoleptic quality for fruit and has a large influence on consumer preference. Kiwifruit esters undergo rapid and substantial changes contributing to the flavor during fruit ripening. Part of enzymes and their coding genes have been indicated potential candidates for flavor-related esters synthesis. However, there still exist obvious gaps in the biosynthetic pathways of esters and the mechanisms regulating ester biosynthesis in kiwifruit remain unknown. Results Using gas chromatography-mass spectrometry (GC-MS), volatile compounds of kiwifruit were quantified in response to ethylene (ETH, 100 μl/l, 24 h, 20 °C) and 1-methylcyclopropene (1-MCP, 1 μl/l, 24 h, 20 °C). The results indicated that esters showed the most substantial changes enhanced by ethylene and were inhibited by 1-MCP. Correlations between RNA-seq results and concentrations of esters, constructed using Weighted Gene Co-Expression Network Analysis (WGCNA) indicated that three structural genes (fatty acid desaturase, AdFAD1 ; aldehyde dehydrogenase, AdALDH2 ; alcohol acyltransferase, AdAT17 ) had similar expression patterns that paralled the changes in total ester content, and AdFAD1 transcripts exhibited the highest correlation. In order to search for potential regulators for ester biosynthesis, 14 previously reported ethylene-responsive transcription factors (TFs) were included in the correlation analysis with esters and their biosynthetic genes. Using dual-luciferase assay, the in vivo regulatory activities of TFs on ester biosynthetic gene promoters were investigated and the results indicated that AdNAC5 and AdDof4 (DNA binding with one finger) trans-activated and trans-suppressed the AdFAD1 promoter. Conclusions The present study advanced the molecular basis of ripening-related ester biosynthesis in kiwifruit by identifying three biosynthetic related genes AdFAD1 , AdALDH2 and AdAT17 by transcriptome analysis, and highlighted the function of two TFs by transactivation studies.

> [!note] 全文去重
> 本页原始抓取在重试循环中重复追加了同一份 PMC 全文 1252 次，已折叠为最长的一份（55315 字符）。原始文件见备份。

## PMC 全文

**来源**: PMC PMC7059668
**下载日期**: 2026-06-15

### Full Text

Transcriptome co-expression network analysis identifies key genes and regulators of ripening kiwifruit ester biosynthesis - PMC
data-tes

### Aidi Zhang
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Qiuyun Zhang
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China

### Jianzhao Li
4 School of Agriculture, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Hansheng Gong
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Xinguang Fan
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Yanqing Yang
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Xiaofen Liu
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China

### Xueren Yin
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China
Copyright and License information
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China
4 School of Agriculture, Ludong University, Yantai, Shandong 264025 People’s Republic of China
Received 2019 Dec 11; Accepted 2020 Feb 27; Collection date 2020.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ . The Creative Commons Public Domain Dedication waiver ( http://creativecommons.org/publicdomain/zero/1.0/ ) applies to the data made available in this article, unless otherwise stated in a credit line to the data.
PMCID: PMC7059668 PMID: 32138665

### Background
Kiwifruit ( Actinidia deliciosa ) is one of the most recently developed and economically important fruit crops that is native to China and now has a global commercial distribution [ 1 ]. Kiwifruit are widely preferred by consumers due to their flavor and high value of nutrient compounds (eg. vitamin C) [ 2 ]. Aroma, together with sweetness and acidity generate the unique flavor of kiwifruit. The production of aroma volatile compounds is strongly ethylene-dependent [ 3 ]. In ethylene-suppressed kiwifruit, fruit softening was significantly delayed and aroma volatile production was dramatically reduced, which could be re-initiated by application of exogenous ethylene [ 4 ]. The aroma of kiwifruit is produced by a mixture of various volatile compounds, including alcohols, aldehydes, ketones, and esters [ 5 ], which makes kiwifruit a good model for understanding the biosynthesis and regulation of different volatile compounds.
Kiwifruit have long been used as material for volatile studies. The early reports on kiwifruit volatile compounds published by Young et al., identified ethyl butanoate, (E)-2-hexenal, (E)-2-hexenol, methyl and ethyl benzoate as the major components of kiwifruit aroma, by using simultaneous distillation extraction of volatiles [ 6 ]. Since then, kiwifruit volatiles have been extensively studied and expanded with 80 to 90 compounds identified so far [ 7 , 8 ]. In general, aldehydes are more abundant in unripe fruit with green notes and esters with fruity notes are abundant in ripe fruit and n-hexanal, (E)-2-hexenal and ethyl butanoate have been identified as specific kiwifruit volatiles [ 8 ]. Until now, many different methods have been developed and used for the analysis of the aroma compounds in kiwifruit, such as gas chromatography-mass spectrometry (GC-MS), which have further enlarged the categories of known volatile compounds in kiwifruit [ 9 , 10 ].
Esters are major aromatic components responsible for the fruity aroma, which increases drasticall

### Volatile compounds analysis in ripening kiwifruit
Alcohols, terpenes, aldehydes, ketones and esters were analyzed in the postharvest kiwifruit treated with ethylene, 1-MCP or control, respectively. Among total alcohols, terpenes, aldehydes, ketones and esters, esters were the most numerous compounds present at the ripening stage, with the values increasing from 236.23 μg/kg at 0 d and reaching peaks of 47,373.07 μg/kg in ETH (10 d), 23,232.26 in control (18 d) and 499.82 μg/kg in 1-MCP treated samples (18 d), respectively (Fig. 1 a). Concentrations of main volatile compounds can be found in Additional file 1 . ( E )-2-Hexenal stayed high level in most unripen fruit and identified as the major contributors to kiwifruit aroma with green notes [ 21 ]. Besides, methyl butanoate, methyl benzoate, ethyl butanoate and ethyl benzoate were the most abundant compounds in ripen fruit (Additional file 2 : Figure S1). During storage, these four esters showed similar changes: induced by ethylene and repressed by 1-MCP. The production of esters increased sharply in control (17 d, 18 d) and ETH fruit (8 d, 10 d), concomitantly with endogenous climacteric ethylene production, while they all remained at the basal level throughout storage in 1-MCP treated fruit (Fig. 1 b). Other volatiles contributed much less to the aroma profile, compared with these four esters (Fig. 1 c). PCA analysis showed that esters compounds located the nearest with ethylene, suggesting the strongly correlations between them and the possibility of esters associated with kiwifruit ripening (Additional file 2 : Figure S2).

### WGCNA of RNA-seq data
The WGCNA was performed to investigate the co-expression networks, in which all co-expressed genes were connected to each other with varying correlation strengths. Genes were partitioned into twenty-two co-expression modules (Fig. 2 a). The content of esters was positively correlated with gene expression in the ‘blue’ module and negatively correlated in the ‘magenta’ module, with a coefficient of 0.82 ( P = 4 × 10 − 5 ) and − 0.78 ( P = 1 × 10 − 4 ), respectively (Fig. 2 b). The coefficients for modules with the other four types of volatile compounds were all lower than 0.7 (Fig. 2 b). Based on correlation ( r &gt; 0.7) between genes in the two modules and ester content, a total of 1896 genes were identified.
Co-expression network analysis of transcriptomes in relation to aroma contents during ‘Hayward’ kiwifruit fruit ripening. a Hierarchical cluster tree showing 22 modules of co-expressed genes. Each leaf represents one gene in the tree. b Module-flavor correlations and corresponding p -values. Each row corresponds to a cluster. Each column corresponds to a volatile compound. The left panel shows 22 modules and the right panel is a color scale for module trait correlation from − 1 to 1 Using the 1896 genes, GO annotation was carried out. GO annotation analysis revealed that genes could be summarized in three main functional categories, including cellular component, molecular function and biological process. Five groups, including cell, cell part, cellular process, metabolic process and organelle, were the main classifications for more than 60% of the genes (Fig. 3 ).

### Identification and expression of ester biosynthesis genes during kiwifruit ripening
Based on WGCNA narrowed the scope of differentially expressed genes (DEGs) from RNA-seq and focused on biosynthetic pathways for esters, two aldehyde dehydrogenases ( AdALDH1 , AdALDH2 ), two fatty acid desaturases ( AdFAD1 , AdFAD2 ), one alcohol dehydrogenase ( AdADH3 ) and one alcohol acyltransferase ( AdAT17 ) [ 22 ] were identified. Using TBTools software, gene transcripts abundance is indicated with a heatmap (Fig. 4 a). Among the genes, AdAT17 , AdALDH2 and AdFAD1 exhibited similar pattern, which were obviously induced by exogenous ethylene and suppressed by 1-MCP treatment, while AdADH3 , AdALDH1 and AdFAD2 were less responsive to two treatments (Fig. 4 a). Increases in abundance of transcripts of AdAT17 , AdALDH2 and AdFAD1 were confirmed by real-time PCR in postharvest ‘Hayward’ kiwifruit. The results indicated that AdAT17 , AdALDH2 and AdFAD1 were all responsive to exogenous ethylene at 1 d and were also accumulated in parallel with endogenous ethylene in both ETH and control fruit (Fig. 4 b). 1-MCP treatment kept expression of AdAT17 and AdALDH2 at basal level, while it only delayed the increase in expression of AdFAD1 (Fig. 4 b). The most significant difference was observed for AdAT17 , its relative expression reaching the maximum (186.53) at 8 d in ETH, compared to 0.93 for CK and 0.05 for 1-MCP at 8 d (Fig. 4 ).

### Regulatory effects of transcription factors on two main ester biosynthesis genes (AdFAD1 and AdAT17)
Correlation analysis with ester content, and three candidate genes ( AdFAD1 , AdAT17 and AdALDH2 ) potentially being involved in ester biosynthesis with 14 previously characterized ripening related TFs [ 20 ], were conducted and visualized by Cytoscape (v3.7.1, USA). As shown in Fig. 5 , all three ester biosynthesis genes exhibit positive correlations with ester content, with AdFAD1 showing the highest positive correlation. For the 14 TFs, the transcript changes in AdBEE1 , AdERF10 , AdNAC6 , AdGT1 , AdDof3 and AdNAC5 positively correlated with ester content, while AdDof4 , AdHB1 and AdbZIP1 showed negative correlations (Fig. 5 ). Between ester biosynthesis genes and TFs, the highest positive correlation was observed between AdBEE1 and AdAT17 , followed by AdBEE1 and AdFAD1 , while the highest negative correlation was found between AdDof4 and AdFAD1 (Fig. 5 ).
Correlation network analysis for structural genes, transcription factors and esters content. The colors of arrows represent the correlations, as indicated by colored bar To extend beyond the digital analysis of the relationship between TFs, structural genes, and ester content, the in vivo regulatory roles of TFs on the promoters of two of the main candidate targets ( AdAT17 and AdFAD1 ) were tested, using dual-luciferase assay. Unfortunately, the failure of amplification of the AdALDH2 promoter precluded its inclusion in this analysis. The results indicated that AdNAC5 could significantly trans-activate the AdFAD1 promoter, with over 2-fold induction (Fig. 6 a), whereas for the AdFAD1 promoter, AdDof4 acted as a repressor, reducing the transcriptional activity to 0.67, compared to the basal activity set as 1 (Fig. 6 a). None of the examined TFs showed significant regulatory effects (neither activation nor repression) on the AdAT17 promoter, (Fig. 6 b).

### Regulatory roles of ethylene and 1-MCP on esters accumulation
Understanding aroma formation is critical for kiwifruit quality and marketability, especially the production of esters, which are the main components for aroma in ripening kiwifruit (Fig. 1 a). During kiwifruit ripening, the flavor changes from ‘grassy’ and ‘green’ to ‘fruity’, and this is manifested by increases in esters and decreases in aldehydes [ 21 ]. It was suggested that the accumulation of esters during ripening were likely driven by ethylene [ 8 , 12 ]. The production of esters, especially ethyl butanoate and methyl butanoate, appeared to be strongly dependent on ethylene signal [ 3 ]. Additionally, in ethylene-suppressed transgenic lines kiwifruit, esters were dramatically reduced, while the major volatiles produced in ethylene-unsuppressed fruit were ethyl butanoate, methyl butanoate, and ethyl acetate [ 4 ]. The present study also found that ethylene treatment accelerated esters accumulation compared with control fruit, and 1-MCP treatment showed the opposite effects on ester production. Four ester compounds (methyl butanoate, methyl benzoate, ethyl butanoate and ethyl benzoate) were found as the main contributors to the total ester for ripening ‘Hayward’ kiwifruit (Fig. 1 c), which were similar to previous findings [ 8 , 9 ]. During ‘Hayward’ storage at 0 °C, the total esters, which consisted mainly of methyl and ethyl butanoate, increased after 9 weeks storage but dropped after 21 weeks storage, and methyl and ethyl benzoate showed similar trends [ 8 ]. Butanoates were the main fruity esters in both ‘Hayward’ and ‘Hort16A’ fruit, which significantly increased during ripening and in over-ripe fruit. Butanoates contributed to less than 40% of the esters in ‘Hayward’ fruit but greater than 60% in ‘Hort16A’ [ 9 ]. Zhang et al. reported ethyl and methyl butanoate levels increased late in the ripening process of ‘Bruno’ [ 12 ]. In ‘Hort16A’ kiwifruit, ethylene treatment (100 ppm, 24 h) can restore the significant reduction of aroma-related esters by cold st

### The proposed transcriptional mechanism for fruit ester biosynthesis
Beyond the biosynthesis pathway, there is very little information about the TFs involved in transcriptional control of ester metabolism and recent investigations have mainly been conducted on terpene biosynthesis. For instance, kiwifruit AaNAC2/3/4 are involved in the transcriptional regulation of TPS genes ( AaTPS1 ) and monoterpene production [ 18 ]; citrus CitAP2.10 and CitERF71 regulate corresponding TPS genes ( CsTPS1 and CitTPS16 ) and contributed to (+)-valencene and E -geraniol metabolism, respectively [ 16 , 17 ]. Moreover, in strawberry, an ERF-MYB transcription complex was found to regulate furaneol biosynthesis and the FaQR promoter [ 35 ]. However, few TFs have been reported that have regulatory effects on biosynthesis of esters. The present finding indicated that one of the key biosynthetic genes ( AdFAD1 ) could be activated by AdNAC5 and suppressed by AdDof4 (Fig. 6 ), which provided an elementary example of a transcriptional regulatory module for esters metabolism. NAC transcription factors ( AaNAC2/3/4 ) are involved in kiwifruit terpene biosynthesis [ 18 ], however, the phylogenetic tree aligned the AdNAC5 sequence with the reported NACs in A. chinensis and A. arguta and AdNAC5 does not have high homology to the kiwifruit NACs involved in terpene biosynthesis and the more closely related genes (AT5G61430.1, AT5G07680.1 and AT3G18400.1) in Arabidopsis thaliana are all functionally uncharacterized (Additional file 2 : Figure S5).

### RNA-seq, WGCNA and gene network visualization
The details of RNA-seq were described by Zhang et al [ 20 ]. The SRA accession number are SRR6885590-SRR6885601, SRR7630964-SRR7630969.

### Gene isolation and promoter cloning
Based on the RNA-Seq results, differentially expressed genes (DEGs) associated with ester biosynthesis were isolated and verified by PCR with gene-specific primers (Additional file 3 : Table S2) using cDNA from cv. ‘Hayward’. The transcription factors were derived from our previous report [ 20 ].

### Dual-luciferase assays
Full length sequences of eleven transcription factors were integrated into pGreen II 0029 62-SK vector (SK) [ 20 ], while promoters of AdAT17 and AdFAD1 were inserted into the pGreen II 0800-LUC vector (LUC).

### Supplementary information
12870_2020_2314_MOESM1_ESM.xlsx (39.2KB, xlsx) Additional file 1. Concentrations of volatile compounds detected in ‘Hayward’ kiwifruit during storage (ng/g FW).
12870_2020_2314_MOESM2_ESM.docx (1.1MB, docx) Additional file 2: Figure S1. An heatmap of volatile compounds detected in ‘Hayward’ kiwifruit in response to ethylene or 1-MCP treatment during storage. Figure S2. PCA analysis of the volitial compounds and ethylene production in kiwifruit treated with control, ethylene (100 μl l − 1 , 24 h) and 1-MCP (1 μl l − 1 , 24 h). Figure S3. Phylogenetic tree analysis of kiwifruit AdAT17 and AAT sequences in other species. Figure S4. Phylogenetic tree of kiwifruit AdFAD1 with Arabidopsis thaliana AtFAD2–8 , tomato SlFAD3 / StFAD7 and PpFAD . Figure S5. Phylogenetic tree of AdNAC5 with kiwifruit ( A. chinensis and A. arguta ) reported NACs and Arabidopsis thaliana NACs .
12870_2020_2314_MOESM3_ESM.docx (24.4KB, docx) Additional file 3: Table S1. Aroma biosynthesis structural genes. Table S2. Primers for real-time PCR. Table S3. Sequences (5′ to 3′) for promoter isolation. Table S4. Primers for vector construction for dual-luciferase assays.

### Abbreviations
Gas chromatography-mass spectrometry
Weighted Gene Co-Expression Network Analysis

### Footnotes
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

### Contributor Information
Aidi Zhang, Email: aidi2012@126.com.
Qiuyun Zhang, Email: swuzqy@163.com.
Jianzhao Li, Email: zhaojianli95@163.com.
Hansheng Gong, Email: hsgong_221@126.com.
Xinguang Fan, Email: firelighting@126.com.
Yanqing Yang, Email: yangyanqing.1986@163.com.
Xiaofen Liu, Email: liuxiaofen@zju.edu.cn.

### References
1. Huang H, Ferguson AR. Kiwifruit in China. N Z J Crop Hortic. 2001;29:1–14. doi: 10.1080/01140671.2001.9514154. [ DOI ] [ Google Scholar ]
2. Rassam M, Laing W. Variation in ascorbic acid and oxalate levels in the fruit of Actinidia chinensis tissues and genotypes. J Agric Food Chem. 2005;53:2322–2326. doi: 10.1021/jf048197s. [ DOI ] [ PubMed ] [ Google Scholar ]
3. Mitalo OW, Tokiwa S, Kondo Y, Otsuki T, Galis L, Suezawa K, Kataoka L, Doan AT, Nakano R, Ushijima K, Kubo Y. Low temperature storage stimulates fruit softening and sugar accumulation without ethylene and aroma volatile production in kiwifruit. Front Plant Sci. 2019;10:888. doi: 10.3389/fpls.2019.00888. [ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
4. Atkinson RG, Gunaseelan K, Wang MY, Luo L, Wang TC, Norling CL, Johnston SL, Maddumage R, Schröder R, Schaffer RJ. Dissecting the role of climacteric ethylene in kiwifruit (Actinidia chinensis) ripening using a 1-aminocyclopropane-1-carboxylic acid oxidase knockdown line. J Exp Bot. 2011;62:3821–3835. doi: 10.1093/jxb/err063. [ DOI ] [ PubMed ] [ Google Scholar ]
5. Marsh KB, Friel EN, Gunson A, Lund C, MacRae E. Perception of flavor in standardised fruit pulps with additions of acids or sugars. Food Qual Prefer. 2006;17:376–386. doi: 10.1016/j.foodqual.2005.04.011. [ DOI ] [ Google Scholar ]
6. Young H, Paterson VJ, Burns DJW. Volatile aroma constituents of kiwifruit. J Sci Food Agric. 1983;34:81–85. doi: 10.1002/jsfa.2740340112. [ DOI ] [ Google Scholar ]
7. Friel EN, Wang M, Taylor AJ, MacRae EA. In vitro and in vivo release of aroma compounds from yellow-fleshed kiwifruit. J Agric Food Chem. 2007;55:6664–6673. doi: 10.1021/jf063733x. [ DOI ] [ PubMed ] [ Google Scholar ]
8. Young H, Paterson VJ. The effects of harvest maturity, ripeness and storage on kiwifruit aroma. J Sci Food Agric. 1985;36:352–358. doi: 10.1002/jsfa.2740360507. [ DOI ] [ Google Scholar ]
9. Wang MY, MacRae E, Wohlers M, Marsh K. Changes in volatile production and sens

### Associated Data
This section collects any data citations, data availability statements, or supplementary materials included in this article.

### Supplementary Materials
12870_2020_2314_MOESM1_ESM.xlsx (39.2KB, xlsx) Additional file 1. Concentrations of volatile compounds detected in ‘Hayward’ kiwifruit during storage (ng/g FW).
12870_2020_2314_MOESM2_ESM.docx (1.1MB, docx) Additional file 2: Figure S1. An heatmap of volatile compounds detected in ‘Hayward’ kiwifruit in response to ethylene or 1-MCP treatment during storage. Figure S2. PCA analysis of the volitial compounds and ethylene production in kiwifruit treated with control, ethylene (100 μl l − 1 , 24 h) and 1-MCP (1 μl l − 1 , 24 h). Figure S3. Phylogenetic tree analysis of kiwifruit AdAT17 and AAT sequences in other species. Figure S4. Phylogenetic tree of kiwifruit AdFAD1 with Arabidopsis thaliana AtFAD2–8 , tomato SlFAD3 / StFAD7 and PpFAD . Figure S5. Phylogenetic tree of AdNAC5 with kiwifruit ( A. chinensis and A. arguta ) reported NACs and Arabidopsis thaliana NACs .
12870_2020_2314_MOESM3_ESM.docx (24.4KB, docx) Additional file 3: Table S1. Aroma biosynthesis structural genes. Table S2. Primers for real-time PCR. Table S3. Sequences (5′ to 3′) for promoter isolation. Table S4. Primers for vector construction for dual-luciferase assays.

### Data Availability Statement
The raw data have been submitted [ 20 ]. The SRA accession number are SRR6885590-SRR6885601, SRR7630964-SRR7630969.
Articles from BMC Plant Biology are provided here courtesy of BMC

### Aidi Zhang
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Qiuyun Zhang
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China

### Jianzhao Li
4 School of Agriculture, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Hansheng Gong
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Xinguang Fan
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Yanqing Yang
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China

### Xiaofen Liu
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China

### Xueren Yin
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China
Copyright and License information
1 School of Food Engineering, Ludong University, Yantai, Shandong 264025 People’s Republic of China
2 BioNanotechnology Institute, Ludong University, Yantai, Shandong 264025 People’s Republic of China
3 College of Agriculture &amp; Biotechnology, Zhejiang University, Zijingang Campus, Hangzhou, 310058 People’s Republic of China
4 School of Agriculture, Ludong University, Yantai, Shandong 264025 People’s Republic of China
Received 2019 Dec 11; Accepted 2020 Feb 27; Collection date 2020.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if changes were made. The images or other third party material in this article are included in the article's Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article's Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by/4.0/ . The Creative Commons Public Domain Dedication waiver ( http://creativecommons.org/publicdomain/zero/1.0/ ) applies to the data made available in this article, unless otherwise stated in a credit line to the data.
PMCID: PMC7059668 PMID: 32138665

### Background
Kiwifruit ( Actinidia deliciosa ) is one of the most recently developed and economically important fruit crops that is native to China and now has a global commercial distribution [ 1 ]. Kiwifruit are widely preferred by consumers due to their flavor and high value of nutrient compounds (eg. vitamin C) [ 2 ]. Aroma, together with sweetness and acidity generate the unique flavor of kiwifruit. The production of aroma volatile compounds is strongly ethylene-dependent [ 3 ]. In ethylene-suppressed kiwifruit, fruit softening was significantly delayed and aroma volatile production was dramatically reduced, which could be re-initiated by application of exogenous ethylene [ 4 ]. The aroma of kiwifruit is produced by a mixture of various volatile compounds, including alcohols, aldehydes, ketones, and esters [ 5 ], which makes kiwifruit a good model for understanding the biosynthesis and regulation of different volatile compounds.
Kiwifruit have long been used as material for volatile studies. The early reports on kiwifruit volatile compounds published by Young et al., identified ethyl butanoate, (E)-2-hexenal, (E)-2-hexenol, methyl and ethyl benzoate as the major components of kiwifruit aroma, by using simultaneous distillation extraction of volatiles [ 6 ]. Since then, kiwifruit volatiles have been extensively studied and expanded with 80 to 90 compounds identified so far [ 7 , 8 ]. In general, aldehydes are more abundant in unripe fruit with green notes and esters with fruity notes are abundant in ripe fruit and n-hexanal, (E)-2-hexenal and ethyl butanoate have been identified as specific kiwifruit volatiles [ 8 ]. Until now, many different methods have been developed and used for the analysis of the aroma compounds in kiwifruit, such as gas chromatography-mass spectrometry (GC-MS), which have further enlarged the categories of known volatile compounds in kiwifruit [ 9 , 10 ].
Esters are major aromatic components responsible for the fruity aroma, which increases drasticall

### Volatile compounds analysis in ripening kiwifruit
Alcohols, terpenes, aldehydes, ketones and esters were analyzed in the postharvest kiwifruit treated with ethylene, 1-MCP or control, respectively. Among total alcohols, terpenes, aldehydes, ketones and esters, esters were the most numerous compounds present at the ripening stage, with the values increasing from 236.23 μg/kg at 0 d and reaching peaks of 47,373.07 μg/kg in ETH (10 d), 23,232.26 in control (18 d) and 499.82 μg/kg in 1-MCP treated samples (18 d), respectively (Fig. 1 a). Concentrations of main volatile compounds can be found in Additional file 1 . ( E )-2-Hexenal stayed high level in most unripen fruit and identified as the major contributors to kiwifruit aroma with green notes [ 21 ]. Besides, methyl butanoate, methyl benzoate, ethyl butanoate and ethyl benzoate were the most abundant compounds in ripen fruit (Additional file 2 : Figure S1). During storage, these four esters showed similar changes: induced by ethylene and repressed by 1-MCP. The production of esters increased sharply in control (17 d, 18 d) and ETH fruit (8 d, 10 d), concomitantly with endogenous climacteric ethylene production, while they all remained at the basal level throughout storage in 1-MCP treated fruit (Fig. 1 b). Other volatiles contributed much less to the aroma profile, compared with these four esters (Fig. 1 c). PCA analysis showed that esters compounds located the nearest with ethylene, suggesting the strongly correlations between them and the possibility of esters associated with kiwifruit ripening (Additional file 2 : Figure S2).

### WGCNA of RNA-seq data
The WGCNA was performed to investigate the co-expression networks, in which all co-expressed genes were connected to each other with varying correlation strengths. Genes were partitioned into twenty-two co-expression modules (Fig. 2 a). The content of esters was positively correlated with gene expression in the ‘blue’ module and negatively correlated in the ‘magenta’ module, with a coefficient of 0.82 ( P = 4 × 10 − 5 ) and − 0.78 ( P = 1 × 10 − 4 ), respectively (Fig. 2 b). The coefficients for modules with the other four types of volatile compounds were all lower than 0.7 (Fig. 2 b). Based on correlation ( r &gt; 0.7) between genes in the two modules and ester content, a total of 1896 genes were identified.
Co-expression network analysis of transcriptomes in relation to aroma contents during ‘Hayward’ kiwifruit fruit ripening. a Hierarchical cluster tree showing 22 modules of co-expressed genes. Each leaf represents one gene in the tree. b Module-flavor correlations and corresponding p -values. Each row corresponds to a cluster. Each column corresponds to a volatile compound. The left panel shows 22 modules and the right panel is a color scale for module trait correlation from − 1 to 1 Using the 1896 genes, GO annotation was carried out. GO annotation analysis revealed that genes could be summarized in three main functional categories, including cellular component, molecular function and biological process. Five groups, including cell, cell part, cellular process, metabolic process and organelle, were the main classifications for more than 60% of the genes (Fig. 3 ).

### Identification and expression of ester biosynthesis genes during kiwifruit ripening
Based on WGCNA narrowed the scope of differentially expressed genes (DEGs) from RNA-seq and focused on biosynthetic pathways for esters, two aldehyde dehydrogenases ( AdALDH1 , AdALDH2 ), two fatty acid desaturases ( AdFAD1 , AdFAD2 ), one alcohol dehydrogenase ( AdADH3 ) and one alcohol acyltransferase ( AdAT17 ) [ 22 ] were identified. Using TBTools software, gene transcripts abundance is indicated with a heatmap (Fig. 4 a). Among the genes, AdAT17 , AdALDH2 and AdFAD1 exhibited similar pattern, which were obviously induced by exogenous ethylene and suppressed by 1-MCP treatment, while AdADH3 , AdALDH1 and AdFAD2 were less responsive to two treatments (Fig. 4 a). Increases in abundance of transcripts of AdAT17 , AdALDH2 and AdFAD1 were confirmed by real-time PCR in postharvest ‘Hayward’ kiwifruit. The results indicated that AdAT17 , AdALDH2 and AdFAD1 were all responsive to exogenous ethylene at 1 d and were also accumulated in parallel with endogenous ethylene in both ETH and control fruit (Fig. 4 b). 1-MCP treatment kept expression of AdAT17 and AdALDH2 at basal level, while it only delayed the increase in expression of AdFAD1 (Fig. 4 b). The most significant difference was observed for AdAT17 , its relative expression reaching the maximum (186.53) at 8 d in ETH, compared to 0.93 for CK and 0.05 for 1-MCP at 8 d (Fig. 4 ).

### Regulatory effects of transcription factors on two main ester biosynthesis genes (AdFAD1 and AdAT17)
Correlation analysis with ester content, and three candidate genes ( AdFAD1 , AdAT17 and AdALDH2 ) potentially being involved in ester biosynthesis with 14 previously characterized ripening related TFs [ 20 ], were conducted and visualized by Cytoscape (v3.7.1, USA). As shown in Fig. 5 , all three ester biosynthesis genes exhibit positive correlations with ester content, with AdFAD1 showing the highest positive correlation. For the 14 TFs, the transcript changes in AdBEE1 , AdERF10 , AdNAC6 , AdGT1 , AdDof3 and AdNAC5 positively correlated with ester content, while AdDof4 , AdHB1 and AdbZIP1 showed negative correlations (Fig. 5 ). Between ester biosynthesis genes and TFs, the highest positive correlation was observed between AdBEE1 and AdAT17 , followed by AdBEE1 and AdFAD1 , while the highest negative correlation was found between AdDof4 and AdFAD1 (Fig. 5 ).
Correlation network analysis for structural genes, transcription factors and esters content. The colors of arrows represent the correlations, as indicated by colored bar To extend beyond the digital analysis of the relationship between TFs, structural genes, and ester content, the in vivo regulatory roles of TFs on the promoters of two of the main candidate targets ( AdAT17 and AdFAD1 ) were tested, using dual-luciferase assay. Unfortunately, the failure of amplification of the AdALDH2 promoter precluded its inclusion in this analysis. The results indicated that AdNAC5 could significantly trans-activate the AdFAD1 promoter, with over 2-fold induction (Fig. 6 a), whereas for the AdFAD1 promoter, AdDof4 acted as a repressor, reducing the transcriptional activity to 0.67, compared to the basal activity set as 1 (Fig. 6 a). None of the examined TFs showed significant regulatory effects (neither activation nor repression) on the AdAT17 promoter, (Fig. 6 b).

### Regulatory roles of ethylene and 1-MCP on esters accumulation
Understanding aroma formation is critical for kiwifruit quality and marketability, especially the production of esters, which are the main components for aroma in ripening kiwifruit (Fig. 1 a). During kiwifruit ripening, the flavor changes from ‘grassy’ and ‘green’ to ‘fruity’, and this is manifested by increases in esters and decreases in aldehydes [ 21 ]. It was suggested that the accumulation of esters during ripening were likely driven by ethylene [ 8 , 12 ]. The production of esters, especially ethyl butanoate and methyl butanoate, appeared to be strongly dependent on ethylene signal [ 3 ]. Additionally, in ethylene-suppressed transgenic lines kiwifruit, esters were dramatically reduced, while the major volatiles produced in ethylene-unsuppressed fruit were ethyl butanoate, methyl butanoate, and ethyl acetate [ 4 ]. The present study also found that ethylene treatment accelerated esters accumulation compared with control fruit, and 1-MCP treatment showed the opposite effects on ester production. Four ester compounds (methyl butanoate, methyl benzoate, ethyl butanoate and ethyl benzoate) were found as the main contributors to the total ester for ripening ‘Hayward’ kiwifruit (Fig. 1 c), which were similar to previous findings [ 8 , 9 ]. During ‘Hayward’ storage at 0 °C, the total esters, which consisted mainly of methyl and ethyl butanoate, increased after 9 weeks storage but dropped after 21 weeks storage, and methyl and ethyl benzoate showed similar trends [ 8 ]. Butanoates were the main fruity esters in both ‘Hayward’ and ‘Hort16A’ fruit, which significantly increased during ripening and in over-ripe fruit. Butanoates contributed to less than 40% of the esters in ‘Hayward’ fruit but greater than 60% in ‘Hort16A’ [ 9 ]. Zhang et al. reported ethyl and methyl butanoate levels increased late in the ripening process of ‘Bruno’ [ 12 ]. In ‘Hort16A’ kiwifruit, ethylene treatment (100 ppm, 24 h) can restore the significant reduction of aroma-related esters by cold st

### The proposed transcriptional mechanism for fruit ester biosynthesis
Beyond the biosynthesis pathway, there is very little information about the TFs involved in transcriptional control of ester metabolism and recent investigations have mainly been conducted on terpene biosynthesis. For instance, kiwifruit AaNAC2/3/4 are involved in the transcriptional regulation of TPS genes ( AaTPS1 ) and monoterpene production [ 18 ]; citrus CitAP2.10 and CitERF71 regulate corresponding TPS genes ( CsTPS1 and CitTPS16 ) and contributed to (+)-valencene and E -geraniol metabolism, respectively [ 16 , 17 ]. Moreover, in strawberry, an ERF-MYB transcription complex was found to regulate furaneol biosynthesis and the FaQR promoter [ 35 ]. However, few TFs have been reported that have regulatory effects on biosynthesis of esters. The present finding indicated that one of the key biosynthetic genes ( AdFAD1 ) could be activated by AdNAC5 and suppressed by AdDof4 (Fig. 6 ), which provided an elementary example of a transcriptional regulatory module for esters metabolism. NAC transcription factors ( AaNAC2/3/4 ) are involved in kiwifruit terpene biosynthesis [ 18 ], however, the phylogenetic tree aligned the AdNAC5 sequence with the reported NACs in A. chinensis and A. arguta and AdNAC5 does not have high homology to the kiwifruit NACs involved in terpene biosynthesis and the more closely related genes (AT5G61430.1, AT5G07680.1 and AT3G18400.1) in Arabidopsis thaliana are all functionally uncharacterized (Additional file 2 : Figure S5).

### RNA-seq, WGCNA and gene network visualization
The details of RNA-seq were described by Zhang et al [ 20 ]. The SRA accession number are SRR6885590-SRR6885601, SRR7630964-SRR7630969.

### Gene isolation and promoter cloning
Based on the RNA-Seq results, differentially expressed genes (DEGs) associated with ester biosynthesis were isolated and verified by PCR with gene-specific primers (Additional file 3 : Table S2) using cDNA from cv. ‘Hayward’. The transcription factors were derived from our previous report [ 20 ].

### Dual-luciferase assays
Full length sequences of eleven transcription factors were integrated into pGreen II 0029 62-SK vector (SK) [ 20 ], while promoters of AdAT17 and AdFAD1 were inserted into the pGreen II 0800-LUC vector (LUC).

### Supplementary information
12870_2020_2314_MOESM1_ESM.xlsx (39.2KB, xlsx) Additional file 1. Concentrations of volatile compounds detected in ‘Hayward’ kiwifruit during storage (ng/g FW).
12870_2020_2314_MOESM2_ESM.docx (1.1MB, docx) Additional file 2: Figure S1. An heatmap of volatile compounds detected in ‘Hayward’ kiwifruit in response to ethylene or 1-MCP treatment during storage. Figure S2. PCA analysis of the volitial compounds and ethylene production in kiwifruit treated with control, ethylene (100 μl l − 1 , 24 h) and 1-MCP (1 μl l − 1 , 24 h). Figure S3. Phylogenetic tree analysis of kiwifruit AdAT17 and AAT sequences in other species. Figure S4. Phylogenetic tree of kiwifruit AdFAD1 with Arabidopsis thaliana AtFAD2–8 , tomato SlFAD3 / StFAD7 and PpFAD . Figure S5. Phylogenetic tree of AdNAC5 with kiwifruit ( A. chinensis and A. arguta ) reported NACs and Arabidopsis thaliana NACs .
12870_2020_2314_MOESM3_ESM.docx (24.4KB, docx) Additional file 3: Table S1. Aroma biosynthesis structural genes. Table S2. Primers for real-time PCR. Table S3. Sequences (5′ to 3′) for promoter isolation. Table S4. Primers for vector construction for dual-luciferase assays.

### Abbreviations
Gas chromatography-mass spectrometry
Weighted Gene Co-Expression Network Analysis

### Footnotes
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

### Contributor Information
Aidi Zhang, Email: aidi2012@126.com.
Qiuyun Zhang, Email: swuzqy@163.com.
Jianzhao Li, Email: zhaojianli95@163.com.
Hansheng Gong, Email: hsgong_221@126.com.
Xinguang Fan, Email: firelighting@126.com.
Yanqing Yang, Email: yangyanqing.1986@163.com.
Xiaofen Liu, Email: liuxiaofen@zju.edu.cn.

### References
1. Huang H, Ferguson AR. Kiwifruit in China. N Z J Crop Hortic. 2001;29:1–14. doi: 10.1080/01140671.2001.9514154. [ DOI ] [ Google Scholar ]
2. Rassam M, Laing W. Variation in ascorbic acid and oxalate levels in the fruit of Actinidia chinensis tissues and genotypes. J Agric Food Chem. 2005;53:2322–2326. doi: 10.1021/jf048197s. [ DOI ] [ PubMed ] [ Google Scholar ]
3. Mitalo OW, Tokiwa S, Kondo Y, Otsuki T, Galis L, Suezawa K, Kataoka L, Doan AT, Nakano R, Ushijima K, Kubo Y. Low temperature storage stimulates fruit softening and sugar accumulation without ethylene and aroma volatile production in kiwifruit. Front Plant Sci. 2019;10:888. doi: 10.3389/fpls.2019.00888. [ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
4. Atkinson RG, Gunaseelan K, Wang MY, Luo L, Wang TC, Norling CL, Johnston SL, Maddumage R, Schröder R, Schaffer RJ. Dissecting the role of climacteric ethylene in kiwifruit (Actinidia chinensis) ripening using a 1-aminocyclopropane-1-carboxylic acid oxidase knockdown line. J Exp Bot. 2011;62:3821–3835. doi: 10.1093/jxb/err063. [ DOI ] [ PubMed ] [ Google Scholar ]
5. Marsh KB, Friel EN, Gunson A, Lund C, MacRae E. Perception of flavor in standardised fruit pulps with additions of acids or sugars. Food Qual Prefer. 2006;17:376–386. doi: 10.1016/j.foodqual.2005.04.011. [ DOI ] [ Google Scholar ]
6. Young H, Paterson VJ, Burns DJW. Volatile aroma constituents of kiwifruit. J Sci Food Agric. 1983;34:81–85. doi: 10.1002/jsfa.2740340112. [ DOI ] [ Google Scholar ]
7. Friel EN, Wang M, Taylor AJ, MacRae EA. In vitro and in vivo release of aroma compounds from yellow-fleshed kiwifruit. J Agric Food Chem. 2007;55:6664–6673. doi: 10.1021/jf063733x. [ DOI ] [ PubMed ] [ Google Scholar ]
8. Young H, Paterson VJ. The effects of harvest maturity, ripeness and storage on kiwifruit aroma. J Sci Food Agric. 1985;36:352–358. doi: 10.1002/jsfa.2740360507. [ DOI ] [ Google Scholar ]
9. Wang MY, MacRae E, Wohlers M, Marsh K. Changes in volatile production and sens

### Associated Data
This section collects any data citations, data availability statements, or supplementary materials included in this article.

### Supplementary Materials
12870_2020_2314_MOESM1_ESM.xlsx (39.2KB, xlsx) Additional file 1. Concentrations of volatile compounds detected in ‘Hayward’ kiwifruit during storage (ng/g FW).
12870_2020_2314_MOESM2_ESM.docx (1.1MB, docx) Additional file 2: Figure S1. An heatmap of volatile compounds detected in ‘Hayward’ kiwifruit in response to ethylene or 1-MCP treatment during storage. Figure S2. PCA analysis of the volitial compounds and ethylene production in kiwifruit treated with control, ethylene (100 μl l − 1 , 24 h) and 1-MCP (1 μl l − 1 , 24 h). Figure S3. Phylogenetic tree analysis of kiwifruit AdAT17 and AAT sequences in other species. Figure S4. Phylogenetic tree of kiwifruit AdFAD1 with Arabidopsis thaliana AtFAD2–8 , tomato SlFAD3 / StFAD7 and PpFAD . Figure S5. Phylogenetic tree of AdNAC5 with kiwifruit ( A. chinensis and A. arguta ) reported NACs and Arabidopsis thaliana NACs .
12870_2020_2314_MOESM3_ESM.docx (24.4KB, docx) Additional file 3: Table S1. Aroma biosynthesis structural genes. Table S2. Primers for real-time PCR. Table S3. Sequences (5′ to 3′) for promoter isolation. Table S4. Primers for vector construction for dual-luciferase assays.

### Data Availability Statement
The raw data have been submitted [ 20 ]. The SRA accession number are SRR6885590-SRR6885601, SRR7630964-SRR7630969.
Articles from BMC Plant Biology are provided here courtesy of BMC

## 深度提炼

**主要物种**: Actinidia spp.
**物种**: Actinidia spp., Solanum lycopersicum, Malus domestica, Fragaria × ananassa, Pyrus spp.
**方法**: transcriptomics (RNA-seq), metabolomics (LC-MS/GC-MS), qRT-PCR validation, dual-luciferase reporter, overexpression, phylogenetics
**来源**: DOI:10.1186/s12870-020-2314-9
**来源类型**: PDF全文 (10.1186_s12870-020-2314-9.pdf)

### 核心发现
1. Candidate target genes for ester biosynthesis Beyond the physiology studies, the molecular aspects underlying ester biosynthesis were also widely studied.
2. Moreover, overexpression of FAD (FAD3 and FAD7) in tomato fruit promoted lino- lenic acid content and enhanced an accumulation of vol- atiles [33].
3. Banana MaDof23 can interact with MaERF9 in regulating fruit ripening [38], however, the roles of Dof transcription factors in aroma production have rarely been investigated.
4. Conclusions In summary, using GC-MS the present study indicated the role of the four main esters (methyl butanoate, me- thyl benzoate, ethyl butanoate and ethyl benzoate) in ripening ‘Hayward’ kiwifruit.
5. The network of ester content, transcription factors and candidate target genes were visualized by Cytoscape (v3.7.1, USA).
6. The banana fruit Dof transcription factor MaDof23 acts as a repressor and interacts with MaERF9 in regulating ripening-related genes.
7. Discussion Regulatory roles of ethylene and 1-MCP on esters accumulation Understanding aroma formation is critical for kiwifruit quality and marketability, especially the production of esters, which are the main components for aroma in rip- ening kiwifruit (Fig.
8. Overall, these find- ings provide new insights into the production of volatiles in ripening kiwifruit and the roles of specific structural genes and TFs in ester metabolism.
