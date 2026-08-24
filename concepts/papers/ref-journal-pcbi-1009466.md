title: Optimal transport analysis reveals trajectories in steady-state systems.
created: 2026-05-28
type: concept
tags: [#single-cell-spatial, papers]
doi: 10.1371/journal.pcbi.1009466
confidence: medium
aliases: ["Optimal transport analysis reveals trajectories in steady-state systems."]
status: draft
updated: "2026-05-29"

# Optimal transport analysis reveals trajectories in steady-state systems.




**期刊**: 
**DOI**: [10.1371/journal.pcbi.1009466](https://doi.org/10.1371/journal.pcbi.1009466)
**作者**: 

## 摘要
Understanding how cells change their identity and behaviour in living systems is an important question in many fields of biology. The problem of inferring cell trajectories from single-cell measurements has been a major topic in the single-cell analysis community, with different methods developed for equilibrium and non-equilibrium systems (e.g. haematopoeisis vs. embryonic development). We show that optimal transport analysis, a technique originally designed for analysing time-courses, may also be applied to infer cellular trajectories from a single snapshot of a population in equilibrium. Therefore, optimal transport provides a unified approach to inferring trajectories that is applicable to both stationary and non-stationary systems. Our method, StationaryOT, is mathematically motivated in a natural way from the hypothesis of a Waddington's epigenetic landscape. We implement StationaryOT as a software package and demonstrate its efficacy in applications to simulated data as well as single-cell data from Arabidopsis thaliana root development.


## 全文 (PMC)

### PERMALINK

The authors have declared that no competing interests exist. * E-mail:geoff@math.ubc.ca Received 2021 Mar 9; Accepted 2021 Sep 20; Collection date 2021 Dec. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited. Understanding how cells change their identity and behaviour in living systems is an important question in many fields of biology. The problem of inferring cell trajectories from single-cell measurements has been a major topic in the single-cell analysis community, with different methods developed for equilibrium and non-equilibrium systems (e.g. haematopoeisis vs. embryonic development). We show that optimal transport analysis, a technique originally designed for analysing time-courses, may also be applied to infer cellular trajectories from a single snapshot of a population in equilibrium. Therefore, optimal transport provides a unified approach to inferring trajectories that is applicable to both stationary and non-stationary systems. Our method, StationaryOT, is mathematically motivated in a natural way from the hypothesis of a Waddington’s epigenetic landscape. We implement StationaryOT as a software package and demonstrate its efficacy in applications to simulated data as well as single-cell data fromArabidopsis thalianaroot development. Many important biological phenomena involve populations of cells that undergo changes in behaviour over time to achieve a desired state or function. Modern experimental technologies are able to measure aspects of cell state but cannot observe a cell at more than a single instant in time, since the cell is necessarily destroyed in the measurement process. Therefore, the relationship between the present and future states of a cell, which we call itstrajectory, must be inferred from observable data. Since biological processes are naturally noisy,

### Stephen Zhang

The authors have declared that no competing interests exist. * E-mail:geoff@math.ubc.ca Received 2021 Mar 9; Accepted 2021 Sep 20; Collection date 2021 Dec. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Roles

The authors have declared that no competing interests exist. * E-mail:geoff@math.ubc.ca Received 2021 Mar 9; Accepted 2021 Sep 20; Collection date 2021 Dec. This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Douglas A Lauffenburger

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Roles

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Douglas A Lauffenburger

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Roles

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Douglas A Lauffenburger

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### Roles

This is an open access article distributed under the terms of theCreative Commons Attribution License, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.

### 

This section collects any data citations, data availability statements, or supplementary materials included in this article.


**OA PDF**: https://journals.plos.org/ploscompbiol/article/file?id=10.1371/journal.pcbi.1009466&type=printable


## 深度提炼

**物种**: Arabidopsis thaliana, Ficus carica
**方法**: single-cell RNA-seq, ATAC-seq
**来源**: DOI:10.1371/journal.pcbi.1009466
**来源类型**: PDF全文 (10.1371_journal.pcbi.1009466.pdf)

### 核心发现
1. We show that optimal transport analysis, a technique originally designed for analysing time-courses, may also be applied to infer cellular trajecto- ries from a single snapshot of a population in equilibrium.
2. We show that for datasets drawn from a population of cells in equilibrium and when esti- mates of cell growth rates are available, cellular trajectories can be estimated by solving an optimal transport problem.
3. In this paper we show that optimal transport analysis, a technique originally applied to ana- lyse time-courses [3], may also be applied to infer cellular trajectories from a single snapshot of a population in equilibrium.
4. We show in this work that optimal transport can be applied in a natural way to the case of a single stationary snapshot, further establishing optimal transport as a widely applicable and robust framework for single-cell trajectory inference.
5. We conclude that the coupling γΔt recovered by solving the entropy minimisation problem Eq (8) is an approximation to the true evolution of Eq (1), corresponding to the drift-diffusion step Eq (5) of the splitting scheme.
6. As we discuss in more detail later, we found that ε = 0.026 best matched the ground truth in terms of average fate probability correlation across the three lineages.
7. In Fig 3D we show the inferred process for k = 1, 5, 10, 20 where we have taken π0 to be uniform on the source sites.
8. Since the transition probabilities encode the displace- ment law of the underlying process over a time interval Δt, we can also recover an estimate ^v of the velocity field v by computing the expected time-Δt displacement of each cell: ^vðxiÞ ¼ EPðXDt   X0jX0 ¼ xiÞ Dt : In Fig 4F we show the estimated velocity field ^v alongside the ground truth v, and we measure Fig 4.
## 相关文献

- [[b3-L7GZnhJuEotGMug-3oD2oA]]
- [[b3-hec2f2m1kP9Y-33yozL7Bg]]
- [[b3-lAocrXAzQRs_pNTy-8Ac1g]]
- [[b4-A4eRtTpTuVLrP6mvHWMndA]]
- [[b5-I9J_3tEggQGIGk7z9SmwOw]]
- [[cr-btt656]]
- [[cr-s13059-014-0550-8]]



## PMC 全文

**PMC ID**: PMC8691649

### Introduction
Biological processes at the cellular level are driven by stochastic dynamics—cellular populations evolve through time, driven by regulation at the cellular and tissue level and intrinsic noise arising from thermal fluctuations. In the context of developmental biology, these processes have been classically described by Waddington’s metaphor of an epigenetic landscape [ 1 ], in which differentiating cells can be thought of as evolving from regions of high differentiation potential into valleys corresponding to differentiated cell types. In the last decade, this metaphor has evolved to be much more quantitative [ 2 , 3 ]. Modern high-throughput assays such as single-cell RNA sequencing (scRNA-seq) [ 4 , 5 ], scATAC-seq [ 6 ] and CyTOF [ 7 ] now allow the molecular states of thousands of single cells to be profiled in a single experiment. With the ability to make these precision measurements of cell state, new challenges emerge in analysing these new types of high-dimensional data.
Single-cell measurements are destructive in nature, so the state of any individual cell cannot be observed at more than one instant. Therefore, information about the trajectories taken by cells over time is lost and must instead be inferred from data. A large collection of trajectory inference methods have been developed in recent years [ 2 ] to address this issue. These methods broadly fall into two classes [ 8 ]: (1) methods that deal with a single stationary snapshot observed from a cellular populat
### Overview of results
To motivate