---
title: Chromosome-scale genome, together with transcriptome and metabolome, provides insights into the evolution and anthocyanin biosynthesis of Rubus rosaefolius Sm. (Rosaceae)
created: 2026-05-30
type: concept
themes: [genomics-evolution]
tags:
- genomics-evolution
- papers
doi: 10.1093/hr/uhae064
pmid: ''
aliases:
- 染色体规模的基因组与转录组和代谢组一起，为玫瑰叶石竹（玫瑰科）的进化和花青素生物合成提供了见解。
title_fixed_from: Chromosome-scale genome, together with transcriptome and metabolome, provides in
theme_status: mapped
theme_basis: tag+keyword

---

# Chromosome-scale genome, together with transcriptome and metabolome, provides insights into the evolution and anthocyanin biosynthesis of Rubus rosaefolius Sm. (Rosaceae)

## 论文信息
- **期刊**: Horticulture Research (2024)
- **DOI**: [10.1093/hr/uhae064](https://doi.org/10.1093/hr/uhae064)

- **作者**: Yunsheng Wang, Jiyuan Guan, Qunying Zhang

## 物种
Rosa

## 摘要
Abstract Rubus rosaefolius is a kind of red raspberry possessing high nutritional and pharmaceutical value. Here we present a chromosome-level draft genome of R. rosaefolius. Of the total 131 assembled scaffolds, 70 with a total size of 219.02 Mb, accounting for 99.33% of the estimated genome size, were anchored to seven pseudochromosomes. We traced a whole-genome duplication (WGD) event shared among members of the Rosaceae family, from which were derived 5090 currently detectable duplicated gene pairs (dgps). Of the WGD-dgps 75.09% underwent purifying selection, and approximately three-quarters of informative WGD-dgps expressed their two paralogs with significant differences. We detected a wide variety of anthocyanins in the berries of R. rosaefolius, and their total concentration remained relatively stable during berry development but increased rapidly during the ripening stage, mainly because of the contributions of pelargonidin-3-O-glucoside and pelargonidin-3-O-(6″-O-malonyl)glucoside. We identified many structural genes that encode enzymes, such as RrDFR, RrF3H, RrANS, and RrBZ1, and play key roles in anthocyanin biosynthesis. The expression of some of these genes significantly increased or decreased with the accumulation of pelargonidin-3-O-glucoside and pelargonidin-3-O-(6″-O-malonyl)glucoside. We also identified some transcription factors and specific methylase-encoding genes that may play a role in regulating anthocyanin biosynthesis by targeting structural genes. In conclusion, our findings provide deeper insights into the genomic evolution and molecular mechanisms underlying anthocyanin biosynthesis in berries of R. rosaefolius. This knowledge may significantly contribute to the targeted domestication and breeding of Rubus species.

> [!note] 全文去重
> 本页原始抓取在重试循环中重复追加了同一份 PMC 全文 1358 次，已折叠为最长的一份（30185 字符）。原始文件见备份。

## PMC 全文

**来源**: PMC PMC11060340
**下载日期**: 2026-08-23

### Full Text

Chromosome-scale genome, together with transcriptome and metabolome, provides insights into the evolution and anthocyanin biosynthesis of Rubus rosaefolius Sm. (Rosaceae) - PMC

### Yunsheng Wang
1 School of Health and Life Science, Kaili University, Kaili city, Guizhou Province 566011, China

### Jiyuan Guan
Botanic Garden of Guizhou Province, Guiyang city, Guizhou Province 550081, China

### Qunying Zhang
Botanic Garden of Guizhou Province, Guiyang city, Guizhou Province 550081, China
Copyright and License information
1 School of Health and Life Science, Kaili University, Kaili city, Guizhou Province 566011, China
Botanic Garden of Guizhou Province, Guiyang city, Guizhou Province 550081, China
Botanic Garden of Guizhou Province, Guiyang city, Guizhou Province 550081, China
✉ Corresponding authors. E-mail: wys3269@126.com ; 2390721318@qq.com
Received 2023 Sep 18; Accepted 2024 Feb 18; Collection date 2024 Apr.
© The Author(s) 2024. Published by Oxford University Press on behalf of Nanjing Agricultural University.
This is an Open Access article distributed under the terms of the Creative Commons Attribution License ( https://creativecommons.org/licenses/by/4.0/ ), which permits unrestricted reuse, distribution, and reproduction in any medium, provided the original work is properly cited.
PMCID: PMC11060340 PMID: 38689697

### Introduction
Rubus (Rosaceae) contains 12 subgenera with more than 700 species that are scattered around the world except Antarctica [ 1 , 2 ]. Eastern Asia or western North America is speculated to be the origin center, and southwestern China is hypothesized to be the diversity center of Rubus species [ 1 , 3 ]. Tissues, especially mature berries, of Rubus species usually contain a variety of health-promoting compounds (e.g. anthocyanins, phenolic acids, and flavonoids) and nutrient substances (e.g. cellulose, vitamin E, and natural pigments) [ 4 , 5 ]. They have been used as medicine and fruit since ancient times [ 6 ]. Some Rubus species (e.g. Rubus occidentalis and Rubus idaeus ) have been domesticated and cultivated, and their planting area and production have increased rapidly in the past two decades [ 7 ]. Although most Rubus fruits are underutilized despite their high commercial value, cultivating these fruits can better satisfy people’s needs. Many researchers have investigated Rubus , and studies have focused mainly on taxonomy [ 2 , 8 ], phytochemistry, pharmacology [ 9 , 10 ], and genomics [ 11 , 12 ]. Information on the genomic evolution and molecular basis of important biological properties of Rubus species is limited to a few members.
Rubus rosaefolius (syn. Rubus rosifolius Sm.) is a kind of red raspberry that grows naturally in East Asia, Southeast Asia, South Asia, Oceania, Africa, and Madagascar ( Flora of China : http://www.iplant.cn/foc ). The twigs, leaves, and roots of R. rosaefolius have long been used for relieving cough, dispelling wind, hemostasis and dampness [ 13 ]. The mature berry of R. rosaefolius is rich in bioactive ingredients, such as anthocyanins [ 14 ], phenolics [ 15 ], triterpenes, and sterols [ 13 , 16 ]. As a result, it has multiple pharmacological effects, including antioxidant [ 15 ], analgesic [ 17 ], antimicrobial [ 18 ], anticorrosive [ 19 ], antiproliferative [ 13 ], and anticancer effects [16 ], diuresis [ 20 ], and the mitigation

### Draft genome assembly
We first constructed and sequenced a short-read library (350 bp) of R. rosaefolius , and harvested 59.76 Gb of data and 97.53% of qualified reads (&gt;Q20) ( Supplementary Data Table S1 ). We performed a K -mer analysis using these qualified reads and estimated that the genome size of R. rosaefolius is 220.50 Mb, with a repetition ratio of 33.31% and heterozygosity of 1.64% ( Supplementary Data Table S2 ; Supplementary Data Fig. S1 ). This result indicates that the genome size of R. rosaefolius was smaller than that of R. occidentalis [ 22 ], Rubus chingii [ 12 ], and R. idaeus [ 23 ]. Then, a long-read library of R. rosaefolius was constructed and sequenced, and 672 954 clean long reads with an average length of 17 004 bp were obtained ( Supplementary Data Table S3 ). These long reads were assembled into a preliminary draft genome of 241.76 Mb, which consisted of 141 contiguous sequences (contigs) (N50 = 15.36 Mb) ( Supplementary Data Table S4 ). Finally, we constructed and sequenced a Hi-C library of R. rosaefolius and obtained &gt;165 million read pairs ( Supplementary Data Table S5 ). Using these valid interaction read pairs to correct the preliminary draft genome, we obtained a final draft genome with a total of 221.95 Mb, containing 138 contigs (N50 = 16.13 Mb). These contigs were further clustered into 131 scaffolds (N50 = 30.0 Mb) ( Table 1, Supplementary Data Table S6 ). Seventy scaffolds with a total of 219.02 Mb, accounting for 98.68% of the total assembly sequences and 99.33% of the estimated genome size, were anchored to seven pseudochromosomes. Among them, 20 scaffolds (211.23 Mb) that represent 96.44% of anchored sequences were determined with respect to position and direction ( Supplementary Data Table S7 ; Supplementary Data Fig. S2 ). We estimated the assembly integrity of this draft genome by blasting the cluster of essential genes (CEG) database and the Benchmarking Universal Single-Copy Orthologs (BUSCO) database; 456 (99.56%) homologs of 458 CE

### Draft genome annotation
From the assembled draft genome of R. rosaefolius , we identified 56.39 Mb (25.41%) of interspersed repeats, 68.5% (38.62 Mb) of which were retroelements dominated by the LTR/Copia, LTR/Gypsy, and LINE families, and 31.5% (17.75 Mb) of which were DNA transposons dominated by the PIF-Harbinger, hAT, and Helitron families ( Supplementary Data Table S12 ). We also identified 22.85 Mb of tandem repeat sequences composed of microsatellite, mini-satellite, and satellite units, accounting for 10.29% of the final draft genome sequence ( Supplementary Data Table S13 ). By integrating ab initio prediction, homology-based prediction, and RNA-seq prediction, we identified 28 067 protein-coding genes, 3062.13 bp in length, 5.16 exons, and 4.16 introns on average, indicating there were fewer genes in R. rosaefolius than in R. chingii (28 877 genes), R. idaeus (33 865 genes), and R. occidentalis (33 248 genes) ( Table 1; Supplementary Data Tables S14 and S15 ; Supplementary Data Fig. S4 ). Of these predicted protein-coding genes, 1584 (98.14%) were homologs of BUSCOs (1614) ( Supplementary Data Table S16 ), and 26 173 (93.25%) could be annotated for biological or molecular functions ( Supplementary Data Table S17 ; Supplementary Dataset 1 ). These annotated transposable elements and protein-coding genes were unevenly distributed on the chromosomes of R. rosaefolius ( Fig. 1 ) . We also identified more than one and a half thousand RNA genes, mainly rRNA and tRNA genes, and some pseudogenes from the R. rosaefolius draft genome ( Supplementary Data Table S18 ; Supplementary Dataset 2 ).

### Phylogenetic relationships and gene family dynamics of R. rosaefolius and nine other species
To elucidate the evolutionary dynamics of the genome of R. rosaefolius , we comprehensively analyzed and compared the gene set data of R. rosaefolius , Coptis chinensis , Liriodendron chinense , Oryza sativa , Arabidopsis thaliana , Rosa chinensis , Fragaria vesca , Prunus persica , R. chingii , and R. occidentalis. In total, 242 905 genes, whose encoded proteins contain &gt;100 amino acids, from the above 10 species were clustered into 38 785 orthogroups (families) ( Supplementary Data Table S19 ; Supplementary Dataset 3 ). Among them, 702 genes that were clustered into 159 families were found to be specific to R. rosaefolius ( Supplementary Data Table S19 ; Supplementary Data Fig. S5 ; Supplementary Dataset 4 ). These genes were mainly enriched in metabolic pathways such as ‘biosynthesis of amino acids’, ‘other types of O -glycan biosynthesis’, ‘glucosinolate biosynthesis’, and ‘valine, leucine, and isoleucine biosynthesis’ ( Supplementary Data Fig. S6 ). These specific families might have imparted some characteristics to R. rosaefolius that were different from those of the other nine species. A phylogenetic tree of the above-mentioned species constructed using 901 single-copy gene families ( Supplementary Dataset 5 ) showed that Rosaceae appeared in the Cretaceous period, raspberry appeared in the Paleogene, and R. rosaefolius and another red raspberry, R. chingii , diverged from the recent common ancestor 17.28–36.44 million years ago (mya), then 211 and 36 gene families of R. rosaefolius expanded and contracted, respectively ( Fig. 2 ; Supplementary Dataset 6 ). The genes in these expanded families were enriched mainly in metabolic pathways, such as ‘DNA polymerase’, ‘photosynthesis’, ‘circadian rhythm’, and ‘galactose metabolism’ ( Supplementary Data Fig. S7 ; Supplementary Dataset 6 ). Of the 901 single-copy genes used for constructing the phylogenetic tree, 156 (17.31%) underwent positive selection and were enriched in metabolic pathways such as ‘porphyrin a

### Genome collinearity between R. rosaefolius and its five relatives
All plants come from a far or near common ancestor. Therefore, their genomes appear more or less collinear. The pattern of collinearity is strongly influenced by chromosomal variation (e.g. whole or segmental chromosome duplication, loss, inversion, or translocation events) that occurred during an evolutionary process after differentiation from recent common ancestors. In turn, the dynamics of chromosome variation between species can be speculated based on the pattern of genomic collinearity. We found complete and parallel syntenic orthologs at one end of chromosome 1 and on the other six chromosomes of R. rosaefolius and R. chingii , but macrosyntenic blocks were missing at the other end of chromosome 1 ( Fig. 3a ). These findings indicated that no large variant of the chromosome occurred between R. rosaefolius and R. chingii , but a fault was hidden in the assembly or annotation of the draft genome of R. rosaefolius or R. chingii . We found that the collinearity across all chromosomes between R. rosaefolius and R. occidentalis was almost intact ( Fig. 3b ), which indicated that the above-mentioned fault in the assembly or annotation of chromosome 1 probably did not occur in R. rosaefolius . When the interference caused by the direction of the scaffolds assembled in the chromosome haplotypes was ignored, nearly complete and parallel collinearity was found for chromosomes 1, 2, 3, 5, and 7, a large inversion probably occurred on chromosome 4, and three or fewer inversions probably occurred on chromosome 6 ( Fig. 3b ). For R. rosaefolius and F. vesca , chromosomes 1, 2, 3, 4, and 6 exhibited intact and parallel collinearity, but one end of chromosomes 5 and 7 underwent a large inversion event, the inversion event on chromosome 5 occurred at the same end, while on chromosome 7, it occurred at the opposite end ( Fig. 3c ). The genomes of R. chinensis and R. rosaefolius , and particularly the genomes of P. persica and R. rosaefolius , appeared less collinear than those 

### Anthocyanins in berries and their accumulation dynamics
Previous studies have demonstrated that anthocyanins are abundant in the berries of R. rosaefolius , particularly cyanidin and pelargonidin [ 15 , 29 ]. In this study, we utilized UPLC–MS/MS wide-targeted metabolite profiling to measure the levels of 1330 metabolites, including 121 amino acids and derivatives, 248 phenolic acids, 241 flavonoids, 78 alkaloids, and 151 terpenoids and organic acids ( Supplementary Dataset 8 ). Among the flavonoids, 17 anthocyanins were detected in nine berries at different stages: three at the young (N1) stage, three at the coloring (N2) stage, and three at the mature (N3) stage ( Supplementary Dataset 8 ). During the transition from N1 to N2 (representing the developmental stage), the concentrations of total and most kinds of anthocyanins remained relatively stable, and only pelargonidin-3- O -glucoside, cyanidin 3-xyloside, and pelargonidin-3- O -(6″- O -malonyl)glucoside continued to increase ( Fig. 5 ; Supplementary Dataset 8 ). From N2 to N3 (representing the developmental stage), the concentrations of five kinds of anthocyanins (e.g. pelargonidin-3- O -(6″- O -acetyl)glucoside and peonidin-3- o -glucoside) remained relatively stable, and two kinds of anthocyanins (pelargonidin-3- O -rutinoside and delphinidin-3- O -(6″- O -caffeoyl)glucoside) slightly decreased; in addition, the total and 10 other kinds of anthocyanins showed increasing trends. Eight (e.g. cyanidin-3- O -galactoside and pelargonidin-3- O -(6″- O -acetyl)glucoside) increased slightly, and two (pelargonidin-3- O -glucoside and pelargonidin-3- O -(6″- O -malonyl)glucoside) increased sharply ( Fig. 5 ; Supplementary Dataset 8 ). These results clearly indicate that the production of anthocyanins in R. rosaefolius berries occurs primarily during the ripening stage, and the main contributors are the reddish pigments pelargonidin-3- O -glucoside and pelargonidin-3- O -(6″- O -malonyl)glucoside.

### Structural genes related to biosynthesis of anthocyanins
A total of 23 997 genes were expressed at different levels in R. rosaefolius berries ( Supplementary Dataset 9 ). According to the KEGG annotation, we identified 11 structural genes, including six anthocyanidin 3- O -glucosyltransferase (RrBZ1) genes belonging to five families; two anthocyanidin 3- O -glucoside 2″- O -xylosyltransferase (RrUGT79B1) genes belonging to one family; one anthocyanidin 3- O -glucoside 5- O -glucosyltransferase (RrUGT75C1) gene and two anthocyanidin 3- O -glucoside 6″-O-acyltransferase (Rr3AT) genes belonging to two families, which are involved in the ‘anthocyanin biosynthesis’ pathway. Furthermore, we identified 22 structural genes, including 10 chalcone isomerase (RrCHI) genes, which belong to six families; five chalcone synthases (RrCHS) genes, which belong to four families; four bifunctional dihydroflavonol 4-reductase/flavanone 4-reductase (RrDFR) genes, which belong to three families; one flavonoid 3′-monooxygenase (RrCYP75B1) gene; one naringenin 3-dioxygenase (RrF3H) gene; and one anthocyanidin synthase (RrANS) gene ( Supplementary Data Fig. S10 ; Supplementary Dataset 10 ), which are involved in ‘flavonoid biosynthesis’ and play crucial upstream roles in anthocyanin biosynthesis [ 30 ]. Of these 33 structural genes, Rro07G000520.1 (RrBZ1), Rro04G036130.1 (RrBZ1), Rro01G021400.1 (RrF3H), Rro07G031240.1 (RrDFR), Rro04G035990.1 (RrCHS), Rro04G036130.1 (RrCHS), Rro07G006550.1 (RrCHI), and Rro05G014010.1 (RrANS) were expressed at relatively high levels in berry tissues ( Fig. 6a ; Supplementary Dataset 10 ). We speculate that these eight genes are the main players involved in the biosynthesis of anthocyanins in the berries of R. rosaefolius. A total of 33 structural genes were also expressed in the flower, leaf, and root tissues of R. rosaefolius , but none were exclusively expressed in berries (Supplementary Dataset S7). This finding indicates that anthocyanin metabolism occurs in various tissues of R. rosaefolius and is not limited t

### Discussion
The genus Rubus contains more than 700 species [ 1 , 2 ]. This number is considerably greater than the average number of members at the genus level in the plant kingdom (67; http://www.theplantlist.org/statistics/ ). Therefore, Rubus has probably experienced evolutionary radiation. Complex apomixis, polyploidization, and frequent hybridization have been found in Rubus species [ 1 , 2 , 8 ]. These events can at least partly explain the biological and genetic mechanisms underlying the relatively frequent speciation events that have occurred in the Rubus genus. In this study, a few large chromosome inversions were found between the genomes of R. rosaefolius and F. vesca according to collinearity analysis, suggesting that large chromosome inversion events occurred in the common ancestor of the Rubus lineage or in the common ancestor of the Fragaria lineage. Large chromosome inversion events, which are highly likely to have occurred in the ancestor of the Rubus lineage, caused unstable inheritance of the genome, which differentiated rapidly and was therefore likely to also promote the evolutionary radiation of Rubus species as well as apomixis, polyploidization, and hybridization. WGD and other genetic mechanisms, such as transposon activity and asymmetric replication of chromosomes, produce a large number of dgps, which provide key resources for producing new genes, allowing the organism to acquire genetic novelty [ 28 ]. We identified 5090 WGD-dgps from the draft genome of R. rosaefolius , which was smaller than the number produced by theoretical WGD events. Hence, most dgps of R. rosaefolius that were produced by WGD events have silenced one or two genes during the evolutionary process. A neutrality test revealed that about three-quarters of the WGD-dgps underwent purifying selection. Therefore, solely based on the above results, the fate of duplicated gene pairs that occurred due to WGD in R. rosaefolius matched that of Homo sapiens , Caenorhabditis elegans , Drosoph

### DNA and total RNA extraction, library construction, and sequencing
DNA was extracted using a plant genomic DNA extraction kit (Thermo Fisher Scientific, Inc., Rockford, IL, USA) following the manufacturer’s protocol. Total RNA was extracted using the RNeasy Plant Mini Kit (Qiagen, Hilden, Germany) following the manufacturer’s guidelines. The quality and content of the extracted DNA and total RNA were checked using a Qubit 2.0 fluorometer (Thermo Fisher Scientific, Waltham, MA, USA) and an Agilent 2100 bioanalyzer (Agilent Technologies, Santa Clara, CA, USA). The genomic short-read library, genomic long-read library, short-read transcriptome library, and full-length transcriptome library were constructed following the standard protocol provided by the sequencer manufacturer and have been ‘described earlier [ 47 , 48 ]. The Hi-C library of R. rosaefolius was constructed following the protocols proposed by Rao et al . [ 49 ]. The qualified genomic short-read library, Hi-C library and short-read transcriptome library were sequenced using a HiSeq 4000 sequencer (Illumina Inc., San Diego, CA, USA) with the PE150 model. The qualified genomic long-read library and full-length transcriptome library were sequenced using a Pacific Biosciences RSII system via single-molecule real-time (SMRT) technology (PacBio, Menlo Park, CA).
K -mer analysis using genomic short-read data

### Annotation of predicted protein-coding genes
The predicted protein-coding genes were functionally annotated by blasting with a P value (&lt;1E5) against the databases of NR ( https://www.ncbi.nlm.nih.gov/refseq/about/nonredundantproteins/ ), eggNOG ( http://eggnog5.embl.de/#/app/home ), GO ( http://geneontology.org/ ), KEGG ( https://www.genome.jp/kegg/ ), InterPro ( https://www.ebi.ac.uk/interpro/ ), TrEMBL ( http://www.bioinfo.pte.hu/more/TrEMBL.htm ), KOG ( http://genome.jgi-psf.org/help/kogbrowser.jsf ), Swiss-Prot ( https://www.expasy.org/resources/uniprotkb-swiss-pro ), and Pfam ( http://pfam-legacy.xfam.org/ ).

### Supplementary Material
web_material_uhae064.zip (15.6MB, zip)

### Contributor Information
Yunsheng Wang, School of Health and Life Science, Kaili University, Kaili city, Guizhou Province 566011, China.
Botanic Garden of Guizhou Province, Guiyang city, Guizhou Province 550081, China.

### References
Alice LA, Campbell CS. Phylogeny of Rubus (Rosaceae) based on nuclear ribosomal DNA internal transcribed spacer region sequences. Am J Bot. 1999;86:81–97
Phylogenetic insights into Chinese Rubus (Rosaceae) from multiple chloroplast and nuclear DNAs. Front Plant Sci. 2016;7:968.
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
Lu LT. A study on the genus Rubus of China. J Syst Evol. 1983;21:13–25 [ Google Scholar ]
Rubus chingii Hu: a review of the phytochemistry and pharmacology. Front Pharmacol. 2019;10:799.
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
Kim C, Dai W. Plant regeneration of red raspberry ( Rubus idaeus ) cultivars ‘JoanJ’ and ‘Polana’. In Vitro Cell Dev Biol Plant. 2020;56:390–7 [ Google Scholar ]
Tristan F, Kraft B, Dey M. et al.
Phytochemical composition and metabolic performance enhancing activity of dietary berries traditionally used by native North Americans. J Agric Food Chem. 2008;56:654–60
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
Foster TM, Bassil NV, Dossett M. et al.
Genetic and genomic resources for Rubus breeding: a roadmap for the future. Hortic Res. 2019;6:116.
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
Complete chloroplast genomes of Rubus species (Rosaceae) and comparative analysis within the genus. Genomics. 2022;23:32.
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
Rocabado GO, Bedoya LM, Abad MJ. et al.
Rubus – a review of its phytochemical and pharmacological profile. Nat Prod Commun. 2008;3:423–36 [ Google Scholar ]
Hummer KE. Rubus pharmacology: antiquity to the present. HortScience. 2010;45:1587–91 [ Google Scholar ]
Jibran R, Dzierzon H, Bassil N. et al.
Chromosome-scale scaffolding of the black raspberry ( Rubus occidentalis L.) genome based on chromatin interaction data. Hortic Res. 2018;5:8.
[ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
The chromosome-scale reference genome of Rubus chingii Hu provides insight into the biosynthetic pathway of 

### Associated Data
This section collects any data citations, data availability statements, or supplementary materials included in this article.

### Supplementary Materials
web_material_uhae064.zip (15.6MB, zip)

### Data Availability Statement
The draft genome sequence was deposited in the China National Center for Bioinformation Database ( https://bigd.big.ac.cn/gsub/, accession number CRA011290). The clean raw data of the long-read and short-read transcriptomes of young stems, young roots, young leaves, calyxes, petals, stamens, young berries, coloring berries, and mature berries were also deposited in the China National Center for Bioinformation Database ( https://bigd.big.ac.cn/gsub/ , accession numbers CRA011285 and CRA012463).
Articles from Horticulture Research are provided here courtesy of Oxford University Press

## 深度提炼

**主要物种**: Rubus spp.
**物种**: Rubus spp., Coptis spp., Fragaria × ananassa, Prunus persica, Arabidopsis thaliana
**方法**: transcriptomics (RNA-seq), metabolomics (LC-MS/GC-MS), genomics, CRISPR/Cas9, phylogenetics
**来源**: DOI:10.1093/hr/uhae064
**来源类型**: PDF全文 (10-1093_hr_uhae064.pdf)

### 核心发现
1. We found complete and parallel syntenic orthologs at one end of chromosome 1 and on the other six chromosomes of R.
2. We found that the collinearity across all chromosomes between R.
3. We found some genes encoding transcription factors, including MYB and bHLH, whose expres- sion significantly increased or decreased, respectively, with the accumulation of anthocyanin biosynthesis, implying that these transcription factors play a role in the regulation of anthocyanin biosynthesis in the berries of R.
4. In conclusion, our findings provide deeper insights into the genomic evolution and molecular mechanisms underlying anthocyanin biosynthesis in berries of R.
5. rosaefolius Whole-genome duplication (WGD) plays a key role in adaptation and speciation.
6. By protein–protein interaction (PPI) analysis, we observed that the Rro4G033620 protein (RrBZ1) directly interacts with the enzyme trimethylguanosine synthase 1 (RrTGS1); that the Rro5G003920 protein (RrBZ1) directly interacts with ferredoxin C1 (RrFDX1), CCAAT-binding transcription factor (RrNFYA), glu- tamate synthase 1 (RrGLU1) and histone-like transcription factor (RrCBF/NF-Y); and that the Rr
7. In summary, there is a strong consistency in the evolutionary dynamics of WGD-dgps across different species.
8. In summary, we provided a multidimensional perspective on the genetic foundation and molecular mechanisms underlying anthocyanin biosynthesis and regulation in R.