---
title: Integrated omics networks reveal the temporal signaling events of brassinosteroid response in Arabidopsis
created: 2026-05-30
type: concept
themes: [hormone-signaling]
tags: [hormone-signaling, papers]
doi: 10.1038/s41467-021-26165-3
pmid: ''
aliases: [集成组学网络揭示拟南芥类固醇反应的时间信号事件]
theme_status: mapped
theme_basis: tag+keyword

---

# Integrated omics networks reveal the temporal signaling events of brassinosteroid response in Arabidopsis

## 论文信息
- **期刊**: Nature Communications (2021)
- **DOI**: [10.1038/s41467-021-26165-3](https://doi.org/10.1038/s41467-021-26165-3)

- **作者**: Natalie M. Clark, Trevor M. Nolan, Ping Wang, Gaoyuan Song, Christian Montes, Conner T. Valentine

## 物种
Arabidopsis thaliana

## 摘要
Abstract Brassinosteroids (BRs) are plant steroid hormones that regulate cell division and stress response. Here we use a systems biology approach to integrate multi-omic datasets and unravel the molecular signaling events of BR response in Arabidopsis . We profile the levels of 26,669 transcripts, 9,533 protein groups, and 26,617 phosphorylation sites from Arabidopsis seedlings treated with brassinolide (BL) for six different lengths of time. We then construct a network inference pipeline called Spatiotemporal Clustering and Inference of Omics Networks (SC-ION) to integrate these data. We use our network predictions to identify putative phosphorylation sites on BES1 and experimentally validate their importance. Additionally, we identify BRONTOSAURUS (BRON) as a transcription factor that regulates cell division, and we show that BRON expression is modulated by BR-responsive kinases and transcription factors. This work demonstrates the power of integrative network analysis applied to multi-omic data and provides fundamental insights into the molecular signaling events occurring during BR response.

> [!note] 全文去重
> 本页原始抓取在重试循环中重复追加了同一份 PMC 全文 1112 次，已折叠为最长的一份（41499 字符）。原始文件见备份。

## PMC 全文

**来源**: PMC PMC8494934
**下载日期**: 2026-08-23

### Full Text

Integrated omics networks reveal the temporal signaling events of brassinosteroid response in Arabidopsis - PMC

### Natalie M Clark
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA
Find articles by Natalie M Clark

### Trevor M Nolan
2 Department of Genetics, Developmental, and Cell Biology, Iowa State University, Ames, IA 50011 USA
4 Present Address: Department of Biology, Duke University, Durham, NC 27708 USA
Find articles by Trevor M Nolan

### Ping Wang
2 Department of Genetics, Developmental, and Cell Biology, Iowa State University, Ames, IA 50011 USA

### Gaoyuan Song
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA

### Christian Montes
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA
Find articles by Christian Montes

### Conner T Valentine
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA
Find articles by Conner T Valentine

### Hongqing Guo
2 Department of Genetics, Developmental, and Cell Biology, Iowa State University, Ames, IA 50011 USA

### Rosangela Sozzani
3 Department of Plant and Microbial Biology, North Carolina State University, Raleigh, NC 27695 USA
Find articles by Rosangela Sozzani

### Yanhai Yin
2 Department of Genetics, Developmental, and Cell Biology, Iowa State University, Ames, IA 50011 USA

### Justin W Walley
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA
Find articles by Justin W Walley
Copyright and License information
1 Department of Plant Pathology and Microbiology, Iowa State University, Ames, IA 50011 USA
2 Department of Genetics, Developmental, and Cell Biology, Iowa State University, Ames, IA 50011 USA
3 Department of Plant and Microbial Biology, North Carolina State University, Raleigh, NC 27695 USA
4 Present Address: Department of Biology, Duke University, Durham, NC 27708 USA
Received 2020 Sep 22; Accepted 2021 Sep 22; Collection date 2021.
Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ .
PMCID: PMC8494934 PMID: 34615886

### Abstract
Brassinosteroids (BRs) are plant steroid hormones that regulate cell division and stress response. Here we use a systems biology approach to integrate multi-omic datasets and unravel the molecular signaling events of BR response in Arabidopsis . We profile the levels of 26,669 transcripts, 9,533 protein groups, and 26,617 phosphorylation sites from Arabidopsis seedlings treated with brassinolide (BL) for six different lengths of time. We then construct a network inference pipeline called Spatiotemporal Clustering and Inference of Omics Networks (SC-ION) to integrate these data. We use our network predictions to identify putative phosphorylation sites on BES1 and experimentally validate their importance. Additionally, we identify BRONTOSAURUS (BRON) as a transcription factor that regulates cell division, and we show that BRON expression is modulated by BR-responsive kinases and transcription factors. This work demonstrates the power of integrative network analysis applied to multi-omic data and provides fundamental insights into the molecular signaling events occurring during BR response.
Subject terms: Brassinosteroid, Plant signalling, Regulatory networks

### Introduction
Brassinosteroids (BRs) are involved in a number of important biological processes including cell elongation and division, photomorphogenesis, reproduction, and both biotic and abiotic stress responses. The BR-signaling pathway has been well-established in Arabidopsis 1 – 3 . BRs are first sensed by the plasma membrane-localized receptor BRASSINOSTEROID INSENSITIVE 1 (BRI1) 4 – 6 . Upon BR binding, BRI1 recruits co-receptors including BRI1-ASSOCIATED RECEPTOR KINASE 1 (BAK1) that are required for its activation 7 , 8 . In the absence of BR, the GSK3 kinase BRASSINOSTEROID INSENSITIVE 2 (BIN2) phosphorylates numerous substrates including the transcription factors (TFs) BRI1-EMS-SUPPRESSOR 1 (BES1), and BRASSINAZOLE-RESISTANT 1 (BZR1) 7 , 9 – 12 . This phosphorylation inactivates BES1 and BZR1 through cytoplasmic retention, degradation, and/or reduced DNA binding. When BRs are present, the BRI1/BAK1 complex activates a kinase-signaling cascade resulting in the inactivation of BIN2 and the dephosphorylation of BES1 and BZR1. This allows BES1 and BZR1 to regulate target gene expression in the nucleus 12 – 18 . While there are many conserved GSK3 phosphorylation sites in BES1 and BZR1 proteins, the exact sites that are phosphorylated by BIN2 and the sites responsible for negative regulation of BES1 activity are not fully defined 19 , 20 .
The role of BR in modulating cell division is well-documented, particularly in the Arabidopsis root. It has been shown that BL has a dose-dependent effect on cell division in the root meristem: roots treated with higher levels of BL have more meristematic cells. In addition, the bes1-D gain-of-function and bri1-116 loss-of-function mutants have altered cell cycle progression, which implicates that plant cyclins may be involved. Accordingly, it has been shown that CYCLIN D3;1 (CYCD3;1) is induced by BL and can rescue cell division defects in the bri1-116 mutant 21 , 22 . BR has also been implicated in stem cell division and maintenance: r

### Generating an integrated omics time course of BR response
To investigate the temporal response to BRs, we established a treatment system in which seedlings were sensitized to BRs by pre-treatment with 1 μM of the BR biosynthesis inhibitor brassinazole (BRZ) 25 for 7 days to reduce background BR signaling. The 7-day-old seedlings were then treated with a mock solvent or 1 μM BL for six different lengths of time (15 min, 30 min, 1 h, 2 h, 4 h, 8 h) (Fig. 1a ). To confirm the efficacy of the BL treatment, we assayed BES1 by western blot (Supplementary Figure 1 ). In BRZ-treated seedlings, we found that BES1 predominantly exists in its phosphorylated form, while BL-treated seedlings showed an accumulation of dephosphorylated BES1 over time. Specifically, we observed an increase in the amount of dephosphorylated BES1 as early as 15 min after treatment, and the phosphorylated form of BES1 was undetectable by 1 h after treatment (Supplementary Figure 1 ). This demonstrates the expected BES1 response and thus the efficacy of BL treatment.
Fig. 1. An integrated omics time course of BR response.
a Samples were collected at six timepoints (15 min, 30 min, 1 h, 2 h, 4 h, 8 h) from Mock and BL-treated seedlings. b TMT-NEAT analysis pipeline for quantitative proteomics. c (left) Total number of transcripts, proteins, and phosphosites/phosphoproteins quantified at each time point. (right) The number of DE transcript, proteins, and phosphosites/phosphoproteins at each time point. Colored bars represent the relative number of DE gene products within each data type. Based on the dynamic nature of BL response, we expected many transcripts, proteins, and phosphosites would have differential responses depending on the length of BL treatment. Thus, we performed multi-omics profiling of BL-treated and mock-treated seedlings at each of the six timepoints (Fig. 1a ). We used 3′ QuantSeq 26 to measure transcript levels and quantified protein abundance and phosphorylation level by performing two-dimensional liquid chromatography-tandem mass spectrom

### Predictive networks illustrate the BR temporal cascade
We have previously shown that integrating mRNA, protein, and phosphorylation data sets greatly improves the predictive power of reconstructed GRNs 34 . However, integrating these multi-omics data types remains challenging. Thus, we next developed a network inference pipeline, which we named SC-ION, to integrate any number of different types of expression profiles into one cohesive, predictive GRN (Fig. 2a , see Methods). SC-ION builds on our MATLAB-based pipeline Regression Tree Pipeline for Spatial, Temporal, and Replicate data (RTP-STAR) 35 , 36 , which is an adaptation of the GENIE3 37 network inference method and functions only on transcriptomic data sets. In SC-ION, we further improve on RTP-STAR by: (1) incorporating Dynamic Time Warping (DTW) clustering for temporal data 38 and Independent Component Analysis (ICA) clustering for non-temporal data 39 ; (2) allowing the user to provide separate regulator and target matrices for integration of DE gene products; (3) integrating any number of different types of expression profiles into one GRN; and (4) providing our pipeline as an RShiny GUI (Fig. 2a ).
Fig. 2. Timepoint-specific, integrative omics networks of BR response.
a SC-ION pipeline. b Timepoint-specific networks using TF abundance (left) or TF phosphosite intensity (right). Edge color represents the time point that regulation is predicted to occur. Nodes represent individual genes. The nodes are arranged in a circular layout relative to timing—genes differentially expressed at the earliest time point (15 min) are placed at the top of the circle, and time increases as one moves clockwise through the layout. Here, we used SC-ION to infer two separate TF-centered networks of BR response. In these TF-centered GRNs, TFs serve as “regulators” used to infer their “target” genes. In the first network, which we call the abundance network (blue, solid edges, Fig. 3 ), TF protein abundance (when quantified) or TF transcript abundance (when cognate protein was not qu

### Multi-omics networks reveal the BIN2-BES1 signaling cascade
We extracted the first-neighbor network of BES1 to illustrate how our multi-omics profiling and integrative network inference can elucidate the signaling events that occur in response to BR (Fig. 3 ). This network contains kinases that are predicted to be upstream of BES1 phosphorylation, TFs that are predicted to transcriptionally regulate BES1, and downstream targets of BES1. Our kinase-signaling network predicted that Serine 179 and Serine 180 (S179, S180) on BES1 is downstream of known BR-responsive kinases such as BIN2, BAK1, and BSK1 8 , 9 , 44 (Supplementary Figure 3a ). The sites are largely conserved in BES1 and its homologs (Supplementary Figure 3b ). In order to test if they are BIN2 kinase phosphorylation sites, we mutated the two sites from serine to alanine (phosphorylation null, designated as BES1 S2A ) and tested phosphorylation by BIN2 in an in the vitro kinase assay. While both BES1 and BES1 S2A were phosphorylated by BIN2, BES1 S2A was phosphorylated to a lesser extent (Supplementary Figure 3e ), suggesting that S179 and S180 are BIN2 phosphorylation sites. We also transiently expressed BES1-FLAG and BES1 S2A -FLAG in Nicotiana benthamiana . Although a significant amount of BES1-FLAG is phosphorylated 1 day after transfection, BES1 S2A -FLAG exists mainly in dephosphorylated form. In addition, when co-expressed with BIN2, the phosphorylated form of wild-type BES1-FLAG was increased, whereas the phosphorylated form of BES1 S2A -FLAG was increased to a lesser extent, which further supports the conclusion that S179 and S180 are BIN2 phosphorylation sites (Supplementary Figure 3c ).
In order to elucidate the functional consequences of the phosphorylation on S179, S180, we generated transgenic Arabidopsis plants overexpressing BES1-FLAG or BES1 S2A -FLAG . The majority (20/26: 77%) of the BES1 S2A -FLAG T1 plants have longer leaf petiole and curly leaves, a characteristic of gain-of-function mutants in BR signaling 12 . Conversely, 13 of 14 (93%) BES1-

### Network motif analysis predicts TFs involved in BR response
We next leveraged the network prediction to identify candidate genes involved in mediating the response to BR. We used the Network Motif Score (NMS) 35 , 36 to classify genes in the TF-centered networks based on their presence in certain biological motifs, such as feedback and feed-forward loops. Genes with higher NMS have been shown to have a more important role in the biological process of interest 35 , 36 , 47 – 49 . Accordingly, BES1 had the 25th highest NMS score (top 5%), illustrating that we could use the NMS to identify BR-response regulators. We chose three TFs, ANTHOCYANLESS 2 (ANL2), TCX2, and BRONTOSAURUS (BRON; AT1G75710), that had high (all in the top 35%) NMS in either the TF abundance or phosphosite GRNs (Supplementary Data 5 ). We then examined subnetworks for each of these TFs, starting with kinase signaling and ending with transcriptional regulation.
SC-ION predicts that our first TF of interest, TCX2, and BES1/BZR1 HOMOLOG 2 (BEH2) regulate each other in a feedback loop (Supplementary Figure 4 ). In addition, TCX2 has a documented root stem cell division phenotype 35 . Thus, we reasoned that TCX2 may regulate cell division in response to BR and treated the tcx2-2 and tcx2-3 mutants with 100 nM BL. In WT plants, the addition of BL causes a dramatic reduction in the root length. However, we did not find a significant difference in BL response in either of the tcx2 mutant alleles compared to WT (Supplementary Figure 4 , Supplementary Table 2 ).

### BRONTOSAURUS regulates cell division in response to BR
Our last TF of interest, BRON, is predicted to be regulated by TFs whose phosphorylation is dependent on multiple BR-signaling kinases such as BAK1, BSKs, and SERKs in our network (Fig. 4a ). We obtained a weak ( bron-1 ) and a strong ( bron-2 ) allele for BRON (Supplementary Figure 5 ) and examined their BR response as well as their root development. We found that roots from both alleles shorten more in response to BL than the wild type, demonstrating that bron mutant roots are hypersensitive to BL treatment (Fig. 4b , Supplementary Table 2 ). In addition, we observed that bron mutants have longer roots with more meristematic cells (Supplementary Figure 5 ), as well as significantly more divisions in the QC (Fig. 4c–e ). bron-2 also displays excessive columella divisions and a higher number of undivided (i.e., actively dividing) cortex endodermis initials (CEI), whereas bron-1 only shows excessive endodermis divisions, potentially due to its weaker effect on BRON expression (Fig. 4e ). This led us to hypothesize that BRON could regulate cell division in response to BR.
Fig. 4. bron mutant roots are hypersensitive to BL treatment and display excessive cell divisions.
a BRON subnetwork. Edge labels represent the phosphosite used to predict that regulation. b
bron mutants are hypersensitive to 100 nM BL treatment ( n &gt; 27). c Representative images of Col-0 wild type, bron-1 , and bron-2 root stem cell niches. * denote Quiescent Center (QC) cells. d The number of meristematic cells in 5-day-old roots ( n = 18). e Average number of columella cell layers, QC divisions, undivided Cortex Endodermis Initials (CEI), and endodermis division in 5-day old roots ( n = 18). d , e the centerline represents median; box bounds represent 25th and 75th percentiles; whiskers represent minimum and maximum. Colored dots represent individual data points. b , d , e * denotes p &lt; 0.05, ** p &lt; 0.01, *** p &lt; 0.001 using a generalized linear model ( b ) or two-tailed Wilcoxon test 

### Discussion
Here, we used a systems biology approach to unravel the temporal response to BR in Arabidopsis . By generating and integrating omics data sets, we were able to quantify how transcript, protein, and phosphorylation levels change in response to BR over time. We found that most of the (phospho)protein response occurs in the earlier timepoints (before 1 h), whereas there are sets of early- and late-responsive transcripts (Fig. 1 ). This suggested that BR first triggers the phosphorylation of TFs, which then go on to regulate transcripts at later timepoints. Our predictive network reconstructed using SC-ION corroborated this hypothesis, illustrating how BR-responsive kinase signaling leads to phosphorylation of TFs and downstream transcriptional regulation (Fig. 3 ). Further, our timepoint-specific networks allow us to predict which regulations occur early and late in BR response (Fig. 2 ).
One well-known example of BR response involves the TFs BES1 and BZR1, which are dephosphorylated in response to BR, allowing them to move to the nucleus and transcriptionally regulate downstream genes. It is well-established that the GSK3 kinase BIN2 phosphorylates BES1 and BZR1 negatively regulate their functions through the promotion of cytoplasmic retention, inhibition of DNA binding, and protein degradation of BES1 and BZR1 1 . Although there are &gt;20 predicted sites, the exact BIN2 phosphorylation sites on BES1 are not functionally characterized. Through our omics profiling and network analysis, we predicted that S179 and S180 in BES1 are potentially phosphorylated by BIN2. Further mutational analysis indicated that the phosphorylation of the two sites contributed to BES1 phosphorylation by BIN2 and are important for BES1 activity. Our study, therefore, identified two key BIN2 phosphorylation sites that negatively regulate BES1 activity and hence BR signaling (Supplementary Figure 1 ).
We further used our network to predict novel roles for the TFs ANL2 and BRON in BR response (

### Plant materials and growth conditions
The Arabidopsis accession Columbia-0 was used as the wild-type control in all experiments. The T-DNA insertion mutants tcx2-2 (SAIL_808_H08), tcx2-3 (SALK_021952) , anl2-2 (SALK_000196C) , anl2-3 (SAIL_418_C10), kin10 (SALK_127939C) , mpk6-4 (SALK_062471C), and tmk1-1 (SALK_016360) were described previously 35 , 58 – 60 . The bes1-D and bri1-301 mutants were also described previously 4 , 12 , 23 , 61 . The T-DNA insertion mutants at1g75710/bron-1 (SALK_048268), at1g75710/bron-2 (SALK_046220C), bak1-4 (SALK_116202C) , map4ka1 (SALK_033601C), and vdof2 (SALK_130584) were obtained from the Arabidopsis Biological Resource Center (ABRC: https://abrc.osu.edu/ ).
For the BL time-series profiling experiments, WT seeds were sterilized with 70% EtOH + 0.1% Triton for 15 min, washed with 100% EtOH three times, and plated on 1/2 LS plates with 1% sucrose and 1000 nM BRZ with nylon mesh overlaid on top of the agar. After 3 days of stratification at 4 °C, the plates were placed under continuous light at 22 °C for 7 days. BL treatments were performed by transferring the seedlings on the nylon mesh to 1/2 LS liquid medium with either 1 µM BL or dimethyl sulfoxide (DMSO) for 15 min, 30 min, 1 h, 2 h, 4 h, or 8 h. Four biological replicates were collected for BL- and mock-treated samples at each time point (48 samples total). Samples were blotted dry with Kimwipes, flash-frozen in liquid nitrogen, and ground for 15 min under liquid nitrogen using a mortar and pestle.
For the bron-2 RNAseq experiment, seeds were wet sterilized using 50% bleach, 10% Tween, and water and stratified at 4 °C for 2 days. Seeds were plated on 1× MS, 1% sucrose plates with Nitex mesh, and grown under long-day conditions (16 h light/8 h dark) at 22 °C for 5 days. Three biological replicates of 10 plates each were collected in RLT buffer, and RNA extraction was immediately performed.

### RNA sequencing and data analysis
For the BR timecourse, total RNA was extracted using Zymo Direct-zol kit (Zymo Research). RNA concentration was measured with Qubit RNA HS assays (ThermoFisher # Q10213 ) and integrity checked with AATI Fragment Analyzer with Standard Sensitivity RNA Analysis Kit (DNF-489-0500). Approximately 500 ng of RNA was used for library construction via the QuantSeq 3′ mRNA-Seq Library Prep FWD Kit for Illumina. Sequencing was performed on a HiSeq 3000 with 50 bp single-end reads. Raw sequencing data are deposited at the Gene Expression Omnibus ( https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE147589 ). Reads were mapped to the TAIR10 genome using the STAR aligner 63 . Differential expression between BL-treated and mock seedlings at each time point was performed using PoissonSeq 64 using a q value cutoff of 0.05 and a fold-change cutoff of 1.25.

### LC-MS/MS
An Agilent 1260 quaternary HPLC was used to deliver a flow rate of ~600 nL min −1 via a splitter. All columns were packed in-house using a Next Advance pressure cell, and the nanospray tips were fabricated using a fused silica capillary that was pulled to a sharp tip using a laser puller (Sutter P-2000). In all, 25 μg of TMT-labeled peptides (non-modified proteome), or ~10 μg TiO 2 -enriched peptides (phosphoproteome), were loaded onto 20 cm capillary columns packed with 5 μM Zorbax SB-C18 (Agilent), which was connected using a zero dead volume 1 μm filter (Upchurch, M548) to a 5 cm long strong cation exchange (SCX) column packed with 5 μm PolySulfoethyl. The SCX column was then connected to a 20 cm nanospray tip packed with 2.5 μM C18 (Waters). The three sections were joined and mounted on a Nanospray Flex ion source (Thermo) for online nested peptide elution. A new set of columns was used for every sample. Peptides were eluted from the loading column onto the SCX column using a 0 to 80% acetonitrile gradient over 60 min. Peptides were then fractionated from the SCX column using a series of 18 and 6 salt steps (ammonium acetate) for the non-modified proteome and phosphoproteome analysis, respectively. For these analyses, buffers A (99.9% H 2 O, 0.1% formic acid), B (99.9% ACN, 0.1% formic acid), C (100 mM ammonium acetate, 2% formic acid), and D (2 M ammonium acetate, 2% formic acid) were utilized. For each salt step, a 150-minute gradient program comprised of a 0–5 min increase to the specified ammonium acetate concentration, 5–10 min hold, 10–14 min at 100% buffer A, 15–120 min 10–35% buffer B, 120–140 min 35–80% buffer B, 140–145 min 80% buffer B, and 145–150 min buffer A was employed.

### Proteomics data analysis
The raw data were analyzed using MaxQuant version 1.6.7.0 66 . Spectra were searched, using the Andromeda search engine in MaxQuant 67 against the Tair10 proteome file entitled “TAIR10_pep_20101214” that was downloaded from the TAIR website ( https://www.arabidopsis.org/download_files/Proteins/TAIR10_protein_lists/TAIR10_pep_20101214 ) and was complemented with reverse decoy sequences and common contaminants by MaxQuant. Carbamidomethyl cysteine was set as a fixed modification while methionine oxidation and protein N-terminal acetylation were set as variable modifications. The phosphoproteome “Phospho STY” was also set as a variable modification. The sample type was set to “Reporter Ion MS2” with “10plex TMT selected for both lysine and N-termini”. TMT batch-specific correction factors were configured in the MaxQuant modifications tab (TMT Lot UD280154). Digestion parameters were set to “specific” and “Trypsin/P;LysC”. Up to two missed cleavages were allowed. A false discovery rate, calculated in MaxQuant using a target-decoy strategy 68 , less than 0.01 at both the peptide spectral match and protein identification level was required. The “second peptide” option to identify co-fragmented peptides was not used. The match between runs feature of MaxQuant was not utilized. Raw proteomics data have been deposited on MassIVEand can be accessed at the link ftp://massive.ucsd.edu/MSV000085606/

### GRN inference and validation
TF-centered GRNs were inferred using SC-ION version 2.1 (10.5281/zenodo.5237310). SC-ION builds on the RTP-STAR pipeline 35 , 36 by incorporating DTW and ICA clustering 38 , 39 and integration of different data types. SC-ION uses an adapted version of GENIE3 37 , which allows for the separate regulator and target data matrices 34 . This allows the user, for example, to use protein abundance data for regulators (TFs) and transcript data for targets (all genes). SC-ION takes regulator and target lists and regulator and target data matrices as input. In addition, SC-ION takes a clustering data matrix, which can be different from the regulator and target data matrices. This allows the user to cluster genes based on different data types. A version of SC-ION without this clustering step is also available. SC-ION outputs a table of the predicted regulations as well as a weight for each edge, where a higher weight indicates higher confidence in that inferred edge 37 . This table can be imported into software such as Cytoscape 70 for network visualization. Test input files for SC-ION are provided on GitHub.
Two TF-centered networks were inferred (Supplementary Figure 7 ). In the first network, TF protein abundance (when quantified) or TF transcript abundance (when cognate protein was not quantified) was used as the “regulator” value to infer their “target” genes’ transcript abundance. In the second phosphosite network, we inferred the transcript levels of “target” genes using TF phosphosite intensities as “regulators.” In both the networks, only the regulators and targets DE at each time point were used in these individual subnetworks. Next, the clustering matrix was constructed by combining the “regulator” (TF abundance) and “target” (transcript levels) data so that genes were clustered based on the protein/phosphosite levels of the regulators and transcript levels of the targets. So, for example, TF protein abundance is clustered with the transcript abundance of its potent

### Mutant BES1 cloning and protein level detection
The two Serine (S179 and S180) to Alanine mutations were introduced by two-step PCR using the primers provided in Supplementary Table 6 . Two BES1 fragments were generated and combined to form the full-length mutant BES1. The full-length mutant BES1 was then cloned to Pro35S:FLAG vector to generate Pro35S:BES1 S2A -FLAG . Pro35S:BES1-FLAG was subcloned from Pro35S:BES1-GFP 12 .
The in vitro kinase assay was based on ref. 74 . Specifically, 0.2 µg of GST-BIN2 and 2 µg of MBP-BES1 or MBP-BES1 S2A were used in 20 µl reactions, and the reactions were stopped by adding an equal volume of 2× SDS buffer at different time points (5 min, 10 min, 20 min, 30 min, 60 min) to observe the phosphorylation dynamics. The in vitro kinase reactions were then resolved on 8% SDS-PAGE incorporated with phostag reagent. The phostag gel was made following the manufacturer’s instructions (AAL-107, http://www.Phos-tag.com ). SYPRO Ruby protein gel stain was used to stain the gel following the manufacturer’s instructions (Invitrogen). The quantification of BES1-P/BES1 ratio and BES1 S2A -P/BES1 S2A ratio was performed in ImageJ.

### BR phenotyping methods
BL phenotyping was carried out as based on 75 as follows. Seeds were sterilized for 4 h in a Nalgene Acrylic Desiccator Cabinet (Fisher Scientific, 08-642-22) by mixing 200 mL bleach (8.25% sodium hypochlorite) with 8 mL concentrated hydrochloric acid to generate chlorine gas. Seeds were then resuspended using 0.1% agarose solution for plating. Control (BL0; DMSO solvent only) or BL100-treated (100 nM Brassinolide; BL, Wako chemicals) were plated on ½ LS plates supplemented with 1% (w/v) sucrose. After seeds were plated, the plates were sealed with breathable tape (3 M Micropore) and placed in the dark at 4 °C for 5 days for stratification. Plants were grown for 7 days at 22 °C under continuous light. Plates were imaged with an Epson Perfection V600 Flatbed Photo scanner at a resolution of 1200 DPI and root length was then measured in ImageJ.

### Supplementary information
Supplementary Information (2MB, pdf)
41467_2021_26165_MOESM3_ESM.pdf (382.3KB, pdf) Description of Additional Supplementary Files
Supplementary Data 1 (14.7MB, xlsx)
Supplementary Data 2 (39.7MB, xlsx)
Supplementary Data 3 (94.1MB, xlsx)
Supplementary Data 4 (144KB, xlsx)
Supplementary Data 5 (4.7MB, xlsx)
Supplementary Data 6 (711.2KB, xlsx)
Supplementary Data 7 (2MB, xlsx)
Supplementary Data 8 (170KB, xlsx)
Supplementary Data 9 (25.1KB, xlsx)

### Footnotes
Nature Communications thanks Rumyana Karlova, Sun Tae Kim, Jianming Li, and the other, anonymous, reviewer(s) for their contribution to the peer review of this work. Peer reviewer reports are available.
Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.

### References
1. Nolan TM, Vukašinović N, Liu D, Russinova E, Yin Y. Brassinosteroids: multidimensional regulators of plant growth, development, and stress responses. Plant Cell. 2020;32:295–318. doi: 10.1105/tpc.19.00335. [ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
2. Planas-Riverola, A. et al. Brassinosteroid signaling in plant development and adaptation to stress. Development 146 , dev151894 (2019). [ DOI ] [ PMC free article ] [ PubMed ]
3. Kim E-J, Russinova E. Brassinosteroid signalling. Curr. Biol. 2020;30:R294–R298. doi: 10.1016/j.cub.2020.02.011. [ DOI ] [ PubMed ] [ Google Scholar ]
4. Friedrichsen DM, Joazeiro CAP, Li J, Hunter T, Chory J. Brassinosteroid-insensitive-1 is a ubiquitously expressed leucine-rich repeat receptor serine/threonine kinase. Plant Physiol. 2000;123:1247–1256. doi: 10.1104/pp.123.4.1247. [ DOI ] [ PMC free article ] [ PubMed ] [ Google Scholar ]
5. He Z, et al. Perception of brassinosteroids by the extracellular domain of the receptor kinase BRI1. Science. 2000;288:2360–2363. doi: 10.1126/science.288.5475.2360. [ DOI ] [ PubMed ] [ Google Scholar ]
6. Li J, Chory J. A putative leucine-rich repeat receptor kinase involved in brassinosteroid signal transduction. Cell. 1997;90:929–938. doi: 10.1016/S0092-8674(00)80357-8. [ DOI ] [ PubMed ] [ Google Scholar ]
7. Nam KH, Li J. BRI1/BAK1, a receptor kinase pair mediating brassinosteroid signaling. Cell. 2002;110:203–212. doi: 10.1016/S0092-8674(02)00814-0. [ DOI ] [ PubMed ] [ Google Scholar ]
8. Li J, et al. BAK1, an Arabidopsis LRR receptor-like protein kinase, interacts with BRI1 and modulates brassinosteroid signaling. Cell. 2002;110:213–222. doi: 10.1016/S0092-8674(02)00812-7. [ DOI ] [ PubMed ] [ Google Scholar ]
9. He J-X, Gendron JM, Yang Y, Li J, Wang Z-Y. The GSK3-like kinase BIN2 phosphorylates and destabilizes BZR1, a positive regulator of the brassinosteroid signaling pathway in Arabidopsis. Proc. Natl. Acad. Sci. 2002;99:10185–10190. doi: 10.1073/pnas.152342599. [ DOI ] [ 

### Associated Data
This section collects any data citations, data availability statements, or supplementary materials included in this article.

### Supplementary Materials
Supplementary Information (2MB, pdf)
41467_2021_26165_MOESM3_ESM.pdf (382.3KB, pdf) Description of Additional Supplementary Files
Supplementary Data 1 (14.7MB, xlsx)
Supplementary Data 2 (39.7MB, xlsx)
Supplementary Data 3 (94.1MB, xlsx)
Supplementary Data 4 (144KB, xlsx)
Supplementary Data 5 (4.7MB, xlsx)
Supplementary Data 6 (711.2KB, xlsx)
Supplementary Data 7 (2MB, xlsx)
Supplementary Data 8 (170KB, xlsx)
Supplementary Data 9 (25.1KB, xlsx)

### Data Availability Statement
Raw sequencing data are deposited at the Gene Expression Omnibus with accession numbers GSE147589 and GSE15700 . Raw proteomics data have been deposited on MassIVE with accession number MSV000085606 . Source data are provided with this paper.
Quantitative proteomics statistical analysis was performed using TMT-NEAT Analysis Pipeline version 1.4 (10.5281/zenodo.5237316) 79 . TF-centered GRNs were inferred using SC-ION version 2.1 (10.5281/zenodo.5237310) 80 .
Articles from Nature Communications are provided here courtesy of Nature Publishing Group

## 深度提炼

**物种**: Nicotiana tabacum
**方法**: transcriptomics (RNA-seq), metabolomics (LC-MS/GC-MS), multi-omics integration, ChIP-seq/qPCR, qRT-PCR validation, overexpression, knockout/mutant, Western blot
**来源**: DOI:10.1038/s41467-021-26165-3
**来源类型**: PDF全文 (10.1038_s41467-021-26165-3.pdf)

### 核心发现
1. Taken together, our results support our kinase-signaling network prediction that S179 and S180 are BIN2 phosphorylation sites whose phosphorylation negatively impacts BES1 function.
2. Taken together, these results validated our GRN-predicted upstream regulators and informed us about downstream targets of BRON (Fig.
3. Additionally, we identify BRONTOSAURUS (BRON) as a transcription factor that regulates cell division, and we show that BRON expression is modulated by BR-responsive kinases and transcription factors.
4. In BRZ- treated seedlings, we found that BES1 predominantly exists in its phosphorylated form, while BL-treated seedlings showed an accumulation of dephosphorylated BES1 over time.
5. We found that the number of differentially expressed (DE) transcripts, proteins, and phosphosites varied depending on the time point.
6. When we examined the transcript data, we found that only 208 transcripts (17 up, 191 down) were DE in response to BL within the ﬁrst 15 min, whereas 454 protein groups (214 up, 250 down) and 590 phosphosites (237 up, 353 down) were DE at this same time point.
7. We found that multiple BR- response terms are enriched at different time points and for different DE gene products.
8. When connecting the timepoint-speciﬁc networks, we found that there were distinct clusters of early and late predictions.