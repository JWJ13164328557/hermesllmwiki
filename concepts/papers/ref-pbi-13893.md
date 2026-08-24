title: PlantPhoneDB: A manually curated pan-plant database of ligand-receptor pairs inf
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1111/pbi.13893
confidence: medium
aliases: ["PlantPhoneDB: A manually curated pan-plant database of ligand-receptor pairs inf"]
status: draft
updated: "2026-05-29"

# PlantPhoneDB: A manually curated pan-plant database of ligand-receptor pairs inf




**期刊**: 
**DOI**: [10.1111/pbi.13893](https://doi.org/10.1111/pbi.13893)
**作者**: 

## 摘要
Ligand-receptor pairs play important roles in cell-cell communication for multicellular organisms in response to environmental cues. Recently, the emergence of single-cell RNA-sequencing (scRNA-seq) provides unprecedented opportunities to investigate cellular communication based on ligand-receptor expression. However, so far, no reliable ligand-receptor interaction database is available for plant species. In this study, we developed PlantPhoneDB (https://jasonxu.shinyapps.io/PlantPhoneDB/), a pan-plant database comprising a large number of high-confidence ligand-receptor pairs manually curated from seven resources. Also, we developed a PlantPhoneDB R package, which not only provided optional four scoring approaches that calculate interaction scores of ligand-receptor pairs between cell types but also provided visualization functions to present analysis results. At the PlantPhoneDB web interface, the processed datasets and results can be searched, browsed, and downloaded. To uncover novel cell-cell communication events in plants, we applied the PlantPhoneDB R package on GSE121619 dataset to infer significant cell-cell interactions of heat-shocked root cells in Arabidopsis thaliana. As a result, the PlantPhoneDB predicted the actively communicating AT1G28290-AT2G14890 ligand-receptor pair in atrichoblast-cortex cell pair in Arabidopsis thaliana. Importantly, the downstream target genes of this ligand-receptor pair were significantly enriched in the ribosome pathway, which facilitated plants adapting to environmental changes. In conclusion, PlantPhoneDB provided researchers with integrated resources to infer cell-cell communication from scRNA-seq datasets.


## 全文 (PMC)

### PERMALINK

Correspondence(Tel +86 0592‐2185175; fax +86 0592‐2185175; emailyingzhou@xmu.edu.cn(Y.Z.); Tel +86 0592‐2181005; fax +86 0592‐2185889; emailzhenghl@xmu.edu.cn(H.‐L.)) These authors contributed equally to this article. Revised 2022 Jul 10; Received 2021 Nov 18; Accepted 2022 Jul 13; Collection date 2022 Nov. This is an open access article under the terms of thehttp://creativecommons.org/licenses/by-nc/4.0/License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes. Ligand‐receptor pairs play important roles in cell–cell communication for multicellular organisms in response to environmental cues. Recently, the emergence of single‐cell RNA‐sequencing (scRNA‐seq) provides unprecedented opportunities to investigate cellular communication based on ligand‐receptor expression. However, so far, no reliable ligand‐receptor interaction database is available for plant species. In this study, we developed PlantPhoneDB (https://jasonxu.shinyapps.io/PlantPhoneDB/), a pan‐plant database comprising a large number of high‐confidence ligand‐receptor pairs manually curated from seven resources. Also, we developed a PlantPhoneDB R package, which not only provided optional four scoring approaches that calculate interaction scores of ligand‐receptor pairs between cell types but also provided visualization functions to present analysis results. At the PlantPhoneDB web interface, the processed datasets and results can be searched, browsed, and downloaded. To uncover novel cell–cell communication events in plants, we applied the PlantPhoneDB R package onGSE121619dataset to infer significant cell–cell interactions of heat‐shocked root cells inArabidopsis thaliana. As a result, the PlantPhoneDB predicted the actively communicating AT1G28290‐AT2G14890 ligand‐receptor pair in atrichoblast–cortex cell pair inArabidopsis thaliana. Importantly, the downstream target genes of this ligand‐receptor pair w

### Chaoqun Xu

Correspondence(Tel +86 0592‐2185175; fax +86 0592‐2185175; emailyingzhou@xmu.edu.cn(Y.Z.); Tel +86 0592‐2181005; fax +86 0592‐2185889; emailzhenghl@xmu.edu.cn(H.‐L.)) These authors contributed equally to this article. Revised 2022 Jul 10; Received 2021 Nov 18; Accepted 2022 Jul 13; Collection date 2022 Nov. This is an open access article under the terms of thehttp://creativecommons.org/licenses/by-nc/4.0/License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes.

### 

Correspondence(Tel +86 0592‐2185175; fax +86 0592‐2185175; emailyingzhou@xmu.edu.cn(Y.Z.); Tel +86 0592‐2181005; fax +86 0592‐2185889; emailzhenghl@xmu.edu.cn(H.‐L.)) These authors contributed equally to this article. Revised 2022 Jul 10; Received 2021 Nov 18; Accepted 2022 Jul 13; Collection date 2022 Nov. This is an open access article under the terms of thehttp://creativecommons.org/licenses/by-nc/4.0/License, which permits use, distribution and reproduction in any medium, provided the original work is properly cited and is not used for commercial purposes.


**OA PDF**: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/pbi.13893


## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC9616517

### Introduction
In order to adapt to environmental changes, plants achieve controlled short and long ranges of cell–cell communication to perceive environmental cues in many ways, including mobile transcriptome, transcription factors, phytohormones, and small signalling peptides (Busch and Benfey, 2010 ; Murphy et al ., 2012 ). In recent years, the importance of secreted signalling peptides in cell–cell communication has received massive attention in plants, coordinating cellular functions to sustain plant growth and development (Jeon et al ., 2021 ; Oh et al ., 2018 ; Takahashi et al ., 2018 ; Zhong et al ., 2022 ). Similar to mammals, plants have evolved a large number of secreted peptides, which are considered to be intercellular signalling molecules (Lease and Walker, 2006 ). Secreted peptide ligands have been considered as the first messenger to bind to cell surface receptors that are transmembrane proteins with extracellular and intracellular kinase domains for signalling transduction. For instance, Phytosulfokine (PSK) peptide may interact with PSK receptor gene 1 (PSKR1) and PSK receptor gene 2 (PSKR2) to regulate root growth in Arabidopsis (Kutschmar et al ., 2009 ), and the pathway of AtPep3 peptide and membrane‐receptor kinase gene PEPR1 is associated with salt tolerance in Arabidopsis (Nakaminami et al ., 2018 ). Many cell surface receptors are composed of receptor‐like proteins and receptor‐like kinases, which contain more than 610 receptor‐like kinase members in Arabidopsis tha
### Results
Statistics of PlantPhoneDB
The current PlantPhoneDB website contains 3514 unique ligand‐receptor pairs for Arabidopsis thaliana , which are curated from seven resources, including plant.MAP, Interactome v2.0, IntAct, BioGRID, Text‐mining from literature, STRING, and Orthologs resources (Figure 1a ). Ligand‐receptor pairs in PlantPhoneDB include 574 ligands and 585 receptors in Arabidopsis thaliana , respectively. scTensor, an R package automatically generates 12 organisms' ligand‐receptor pairs from the STRING database using 36 approaches. scTensor generates 3014 ligand‐receptor pairs involving 671 ligands and 645 receptors for Arabidopsis thaliana (Figure S1 a). Compared with scTensor, only 26.11% (787/3014) ligand‐receptor pairs from scTensor were covered in t