title: Extracting multiple interacting root systems using X-ray microcomputed tomograph
created: 2026-05-28
type: concept
tags: [#stress-immunity, papers]
doi: 10.1111/tpj.13047
confidence: medium
aliases: ["Extracting multiple interacting root systems using X-ray microcomputed tomograph"]
status: draft
updated: "2026-05-29"

# Extracting multiple interacting root systems using X-ray microcomputed tomograph




**期刊**: 
**DOI**: [10.1111/tpj.13047](https://doi.org/10.1111/tpj.13047)
**作者**: 

## 摘要
Root system interactions and competition for resources are active areas of research that contribute to our understanding of how roots perceive and react to environmental conditions. Recent research has shown this complex suite of processes can now be observed in a natural environment (i.e. soil) through the use of X-ray microcomputed tomography (μCT), which allows non-destructive analysis of plant root systems. Due to their similar X-ray attenuation coefficients and densities, the roots of different plants appear as similar greyscale intensity values in μCT image data. Unless they are manually and carefully traced, it has not previously been possible to automatically label and separate different root systems grown in the same soil environment. We present a technique, based on a visual tracking approach, which exploits knowledge of the shape of root cross-sections to automatically recover from X-ray μCT data three-dimensional descriptions of multiple, interacting root architectures growing in soil. The method was evaluated on both simulated root data and real images of two interacting winter wheat Cordiale (Triticumaestivum L.) plants grown in a single soil column, demonstrating that it is possible to automatically segment different root systems from within the same soil sample. This work supports the automatic exploration of supportive and competitive foraging behaviour of plant root systems in natural soil environments.


## 全文 (PMC)

### PERMALINK

For correspondence (e‐mailstefan.mairhofer@nottingham.ac.uk). Received 2015 Jul 29; Revised 2015 Sep 21; Accepted 2015 Sep 28; Issue date 2015 Dec. This is an open access article under the terms of theCreative Commons AttributionLicense, which permits use, distribution and reproduction in any medium, provided the original work is properly cited. Root system interactions and competition for resources are active areas of research that contribute to our understanding of how roots perceive and react to environmental conditions. Recent research has shown this complex suite of processes can now be observed in a natural environment (i.e. soil) through the use of X‐ray microcomputed tomography (μCT), which allows non‐destructive analysis of plant root systems. Due to their similar X‐ray attenuation coefficients and densities, the roots of different plants appear as similar greyscale intensity values in μCT image data. Unless they are manually and carefully traced, it has not previously been possible to automatically label and separate different root systems grown in the same soil environment. We present a technique, based on a visual tracking approach, which exploits knowledge of the shape of root cross‐sections to automatically recover from X‐ray μCT data three‐dimensional descriptions of multiple, interacting root architectures growing in soil. The method was evaluated on both simulated root data and real images of two interacting winter wheat Cordiale (TriticumaestivumL.) plants grown in a single soil column, demonstrating that it is possible to automatically segment different root systems from within the same soil sample. This work supports the automatic exploration of supportive and competitive foraging behaviour of plant root systems in natural soil environments. Keywords:X‐ray computed tomography, root system interaction, multiple target tracking, technical advance Imaging roots in their natural soil environment is important for understanding their growth, developmen

### Stefan Mairhofer

For correspondence (e‐mailstefan.mairhofer@nottingham.ac.uk). Received 2015 Jul 29; Revised 2015 Sep 21; Accepted 2015 Sep 28; Issue date 2015 Dec. This is an open access article under the terms of theCreative Commons AttributionLicense, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.

### 

For correspondence (e‐mailstefan.mairhofer@nottingham.ac.uk). Received 2015 Jul 29; Revised 2015 Sep 21; Accepted 2015 Sep 28; Issue date 2015 Dec. This is an open access article under the terms of theCreative Commons AttributionLicense, which permits use, distribution and reproduction in any medium, provided the original work is properly cited.


**OA PDF**: https://onlinelibrary.wiley.com/doi/pdfdirect/10.1111/tpj.13047


## 深度提炼

**物种**: Oryza sativa, Zea mays, Brassica napus, Triticum aestivum, Ficus carica
**方法**: molecular biology / biochemistry
**来源**: DOI:10.1111/tpj.13047
**来源类型**: PDF全文 (10.1111_tpj.13047.pdf)

### 核心发现
1. Importantly, the method proposed here is not limited to recovering and separating two plants, but can work on a number of root systems that interact with each other.
2. From this and previous work we found a resolu- tion of 25 lm3 and below to be suitable for the detection of wheat root systems.
3. Keywords: X-ray computed tomography, root system interaction, multiple target tracking, technical advance.
4. Each root cross- section is thought of as a moving target belonging to and emerging from a root system.
5. This means that if a new target appears from an emerging lateral root, it will be considered an individual object to be tracked, while at the same time being associated with the root system from which it originated.
6. The problem of ‘coalescence’ of interacting targets is a widespread feature of multiple target tracking and an active research topic in computer vision (Milan et al., 2013).
7. All visual trackers rely heavily on an appearance model of some form; similar targets will always be tracked with a similar, and often identical, model.
8. When targets interact, each tracker will tend to lock on the tar- get that best ﬁts the model.

## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC4949686

### Introduction
Plants use their root systems to explore the heterogeneous and complex soil environment for water and nutrient sources which, in the field, are shared with other, neighbouring plants. Each plant must compete for its survival, especially under stressful conditions, when these resources are limited. Root system interaction and belowground competition in plant communities are subjects of wide interest (Mahall and Callaway, 1992 ; Casper and Jackson, 1997 ; Rubio et al ., 2001 ; Maina et al ., 2002 ). Root competition is considered a negative aspect of root interaction, in which plants can limit each other's growth. However, root interaction can also have positive effects, for example by simultaneously decreasing the availability of one resource while increasing the availability of another or by influencing the composition of the bacterial flora in the rhizosphere, which may affect the availability of nutrients to neighbouring plants (Schenk, 2006 ). These interactions are of particular concern for intercrop cultivation, which is of significant and increasing interest at present (Brooker et al ., 2014 ); here the aim is to find the optimal combination of plants for a certain field environment. Planting strategy can have a large effect on crop yield (Mead and Willey, 1980 ; Willey, 1985 ; Anil et al ., 1998 ). It is commonly believed that root systems have the ability to sense neighbouring plants, though the process is complicated and not yet fully understood due to an inability t
### RooTrak results
The root system descriptions recovered from the experiment performed on the simulated roots are shown in Figure 3 . On the left side of each pair is the result obtained using the original extraction method (Mairhofer et al ., 2012 ), while on the right side the proposed mechanism was activated each time it was triggered by two interacting targets. In samples 1–12 there were a total of three, two, two, four, one, one, two, two, three, three, two and one interactions, respectively; interactions were of varying duration with varying degrees of overlap between objects. For all the samples, the tracker correctly labelled the objects during collision. Figure 4 shows the results of the experiment performed on real images of the root systems of two interacting wheat plants; each root system is rendered in a different colour. Figure 5 shows the same root systems, but from viewpoints closer to interacting roots, illustrating the difference between the original version of RooTrak and the proposed mechanism to deal with root object collisions. Figure 6 shows a sequence of cross‐sectional images in which the roots of the two interacting wheat plants were identified, while at the same time kept separate and assigned to the correct originating plant by to the mechanism proposed here. The time needed to recover the root systems from the CT images depends on the number of data and the number of root objects being tracked. The 