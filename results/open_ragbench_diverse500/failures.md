# OpenRAGBench diverse_500 — Failure Report (top 20)

## 0722fef4-627d-40b8-aca6-c551a40f737e  [right_doc_wrong_section]
- query: What is the attractive force formula in the Fruchterman-Reingold force model?
- source/type: text / extractive
- expected doc_id: 2412.20317v3
- expected section_id: 30
- expected section preview: '### 8.3.1 Problem Formulation\n\nLet $G=(V, E)$ be a graph with vertex set $V=\\{1, \\ldots, n\\}$ and edge set $E$. Each edge $(i, j) \\in E$ has weight $a_{i, j}$. For convenience, we set $a_{i, j}=0$ for $(i, j) \\notin E$. Note that $G$ can be a disconnected directed graph, and $a_{i, j}$ can be negati'
- top 5 returned:
  - rank 1 doc=2412.20317v3 sec=2 score=1.0 stage=hybrid :: '## 2 Fruchterman-Reingold Force Model\n\nFruchterman and Reingold [8] proposed the FR force model for graph drawing based on the physical analogy of the system of'
  - rank 2 doc=2412.20317v3 sec=27 score=0.666667 stage=hybrid :: '### 8.1 Fruchterman-Reingold Algorithm\n\nThe Fruchterman-Reingold algorithm [8] is the original force-directed algorithm and the most standard approach for the F'
  - rank 3 doc=2412.20317v3 sec=0 score=0.25 stage=hybrid :: '#### Abstract\n\nGraph drawing is a fundamental task in information visualization, with the Fruchterman-Reingold (FR) force model being one of the most popular ch'
  - rank 4 doc=2412.09393v2 sec=11 score=0.25 stage=hybrid :: '## A. The lattice BUU transport model\n\nThe time evolution of the one-body phase-space distribution function (Wigner function) $f_{\\tau}=f_{\\tau}(\\vec{r}, \\vec{p'
  - rank 5 doc=2411.12375v3 sec=18 score=0.2 stage=hybrid :: '## B. Extend to other AMM case\n\n1) Example of application in Uniswap V2: In the case of Uniswap V2, as the liquidity bounds (LH) approach zero and infinity, the'

## 0cc52d57-c698-481f-8113-2eebdc3799e1  [right_doc_wrong_section]
- query: What is a social welfare function in economics?
- source/type: text-image / extractive
- expected doc_id: 2408.04814v3
- expected section_id: 3
- expected section preview: "# 3 Existence of a positive protected income \n\nNot all social welfare functions guarantee Ana against complete sacrifice for the sake of Ben's stratospheric income. Actually, many of the most commonly used social welfare functions do not protect against complete sacrifice.\n\nProposition 1. For all $y"
- top 5 returned:
  - rank 1 doc=2410.09555v2 sec=9 score=0.611111 stage=hybrid :: '# 4.2 Welfare Maximization \n\nNext, I consider the objective of maximizing social welfare, which takes into account the total net benefit to all users across all'
  - rank 2 doc=2408.04814v3 sec=0 score=0.533333 stage=hybrid :: '#### Abstract\n\nWe discover a fundamental and previously unrecognized structure within the class of additively separable social welfare functions that makes it s'
  - rank 3 doc=2408.04814v3 sec=9 score=0.5 stage=hybrid :: '# 9 References \n\nAboudi, R., \\& Thon, D. (2003). Transfer principles and relative inequality aversion a majorization approach. Mathematical social sciences, 45('
  - rank 4 doc=2408.04814v3 sec=2 score=0.375 stage=hybrid :: '# 2 Setting and main definitions \n\nConsider a population of $n$ individuals, each individual $i$ enjoying income $y_{i} \\geq 0$, and an additively separable soc'
  - rank 5 doc=2406.14174v3 sec=2 score=0.333333 stage=hybrid :: '# 2 Model \n\nA monopolistic seller (she) supplies a good to a unit mass of buyers. Buyers have a unit demand and differ in their willingness to pay for the good,'

## 1d585069-a446-47fa-a74d-0387316ea330  [right_doc_wrong_section]
- query: In what areas do syllabic embeddings show potential for improvement based on current research findings?
- source/type: text-table / abstractive
- expected doc_id: 2410.07168v2
- expected section_id: 30
- expected section preview: '## A.2.4 General Representational Power of Sylber\n\nThough the universal utility of our model is not of our focus, we evaluate and benchmark downstream tasks using SUPERB (Yang et al., 2021). First of all, to find the optimal merge threshold, we train a phoneme recognition (PR) model with syllabic em'
- top 5 returned:
  - rank 1 doc=2410.07168v2 sec=33 score=0.5 stage=hybrid :: '# A.2.7 Visualization of Sylber Embedding \n\nTo provide a better sense of embedding structure in Sylber, we apply t-SNE to syllabic embeddings obtained from Sylb'
  - rank 2 doc=2410.06188v2 sec=14 score=0.5 stage=hybrid :: '## 5 Conclusion\n\nThis work demonstrates the transformative potential of directly utilizing raw DNA signals in the analysis of Nanopore sequencing data, particul'
  - rank 3 doc=2411.04694v1 sec=7 score=0.333333 stage=hybrid :: '# 4. Conclusion \n\nCurrently, the conventional HE staining procedure is widely preferred to separate the essential zones in placental tissue evaluation for mice.'
  - rank 4 doc=2410.07168v2 sec=1 score=0.333333 stage=hybrid :: '## 1 INTRODUCTION\n\nSelf-supervised learning (SSL) approaches have been successful in learning speech representations that encode rich speech contents useful for'
  - rank 5 doc=2410.07168v2 sec=11 score=0.25 stage=hybrid :: '# 6 EMERGENT CATEGORICAL PERCEPTION IN SYLBER \n\nThe results shown in Section 5.2 suggest that HuBERT features might densely tile the embedding space, requiring '

## 2bac52cd-23d5-4128-a321-c325f49e59d9  [wrong_doc]
- query: What is a pitchfork bifurcation in dynamical systems?
- source/type: text / extractive
- expected doc_id: 2410.15824v2
- expected section_id: 8
- expected section preview: "# 5 Applications\n### 5.1 Pitchfork Bifurcation\n\nIn certain deterministic dynamical systems, a notable phenomenon called the 'phase transition' takes place in the steady state behavior, depending on a critical parameter as its value shifts from one regime to another. While shifting, the previously st"
- top 5 returned:
  - rank 1 doc=2410.05454v2 sec=23 score=0.666667 stage=hybrid :: '## E. 2 Hopf Bifurcation\n\nLatent trajectories were generated from the following two-dimensional dynamical system,\n\n$$\n\\dot{z}_{1}=z_{2}+5 \\mathrm{~d} W_{t}, \\qu'
  - rank 2 doc=2412.02459v2 sec=2 score=0.5 stage=hybrid :: "# Prigogine's dissipative structures becoming chaotic. Role of water \n\nIlya Prigogine's dissipative structures describe systems far from thermodynamic equilibri"
  - rank 3 doc=2404.09796v2 sec=11 score=0.5 stage=hybrid :: '# Proof of Lemma 3: \n\nSuppose there exists a value of $\\phi=\\phi_{b} \\in(0,1)$ such that $\\frac{d \\Delta u}{d h}\\left(\\frac{1}{2} ; \\phi_{b}\\right)=t^{\\prime}\\l'
  - rank 4 doc=2411.15293v2 sec=8 score=0.25 stage=hybrid :: "# 2.2. Numerical Simulations \n\nUsing MATLAB's ode89 program, we can simulate the system and compare the numerical results to the theoretical predictions. All si"
  - rank 5 doc=2412.02459v2 sec=5 score=0.25 stage=hybrid :: '# Figure legends \n\nFigure 1. 3D plots depicting the behaviour of the Lorenz system at different Rayleigh numbers ( $\\rho$ lrho): A) $\\rho$ (rho) $=10.0$ (Low En'

## 2cc9bf85-7258-45b7-b8a8-e1888c793c1f  [right_doc_wrong_section]
- query: What type of processes do individual idiosyncratic noises form in classical mean field games?
- source/type: text / abstractive
- expected doc_id: 2403.01012v4
- expected section_id: 4
- expected section preview: '# 3. Coupled Controlled Stochastic Evolution Equations in Hilbert Space \n\nIn classical mean field games (MFGs), the dynamics of the relevant $N$-player game is modeled as a system of finite-dimensional SDEs, the regularities of which are well-studied in the literature. However, in this paper, the dy'
- top 5 returned:
  - rank 1 doc=2403.01012v4 sec=0 score=0.833333 stage=hybrid :: '#### Abstract\n\nThis paper presents a comprehensive study of linear-quadratic (LQ) mean field games (MFGs) in Hilbert spaces, generalizing the classic LQ MFG the'
  - rank 2 doc=2403.01012v4 sec=5 score=0.7 stage=hybrid :: '# 4. Hilbert Space-Valued LQ Mean Field Games\n### 4.1. $N$-Player Game in Hilbert Space\n\nWe consider a differential game in Hilbert spaces defined on $\\left(\\Om'
  - rank 3 doc=2403.01012v4 sec=1 score=0.583333 stage=hybrid :: '## 1. Introduction\n\nMean field game (MFG) theory concerns the study and analysis of dynamic games involving a large number of indistinguishable agents who are a'
  - rank 4 doc=2403.01012v4 sec=15 score=0.375 stage=hybrid :: '## References\n\n[1] M. Huang, R. P. Malhamé, P. E. Caines, Large population stochastic dynamic games: Closedloop McKean-Vlasov systems and the Nash certainty equ'
  - rank 5 doc=2408.11773v1 sec=7 score=0.2 stage=hybrid :: '### 4.1 The zero noise case\n\nWhen $\\sigma=10^{-9}$ we model the interaction of both agents in a limiting situation when the market is very illiquid and almost n'

## 3de6cbbd-b28f-49f6-9e13-45df9264bb07  [right_doc_wrong_section]
- query: What were the long-term socio-economic effects on individuals who experienced centralized admissions during their schooling years in Japan?
- source/type: text-table-image / abstractive
- expected doc_id: 2402.04429v3
- expected section_id: 23
- expected section preview: "# A. 3 Additional Tables and Figures \n\nFigure A.1: College Admissions around the World Today\n\n![img-5.jpeg](img-5.jpeg)\n\nNotes: This figure summarizes each country and territory's college admission system today. Dark red color (e.g. Norway): Regionally- or nationally-centralized college admissions w"
- top 5 returned:
  - rank 1 doc=2402.04429v3 sec=1 score=0.5 stage=hybrid :: '# 1 Introduction \n\nOne major trend in college admissions around the world is a growing degree of centralization. Today, over thirty countries use regionally- or'
  - rank 2 doc=2402.04429v3 sec=3 score=0.5 stage=hybrid :: '# 2.2 Political Economy of the Admission Reforms \n\nThis institutional innovation was short-lived, however. Due to the opposition detailed below, the government '
  - rank 3 doc=2402.04429v3 sec=11 score=0.444444 stage=hybrid :: "# 4.1 Regional Distribution of Elites\n## Personnel Inquiry Records Data\n\nTo analyze the long-run effects of centralization on students' career outcomes, we merg"
  - rank 4 doc=2402.04429v3 sec=9 score=0.333333 stage=hybrid :: '# 3.6 Other Institutional Changes \n\nWe finish the short-run analysis by discussing potential threats. In particular, if changes in other institutional and polic'
  - rank 5 doc=2402.04429v3 sec=13 score=0.325 stage=hybrid :: '# Urban-Rural Disparity in Producing Elites \n\nWe estimate the long-run impacts of the centralized admission system by conducting a difference-in-differences ana'

## 4126e457-bb00-4de0-8202-3d5e2de4713f  [right_doc_wrong_section]
- query: How does an even number of switch errors influence the output in diploid genome assembly using a greedy approach?
- source/type: text-image / abstractive
- expected doc_id: 2405.05734v3
- expected section_id: 7
- expected section preview: '## 4) Proof for the sufficiency of Conditions G1-G3:\n\nClaim 3. The number of strings left at the end of the while loop in the greedy algorithm cannot be greater than 2.\nProof. Let $\\mathcal{R}^{\\prime}$ be the maximal subset of $\\mathcal{R}$ such that the reads belonging to $\\mathcal{R}^{\\prime}$ do'
- top 5 returned:
  - rank 1 doc=2405.05734v3 sec=1 score=1.0 stage=hybrid :: '## I. INTRODUCTION\n\nThe problem of reconstructing genomes, i.e., de novo genome assembly, is a fundamental problem in computational biology. DNA sequencing inst'
  - rank 2 doc=2405.05734v3 sec=10 score=0.583333 stage=hybrid :: '## V. EXPERIMENTS\n\nWe apply our theoretical analysis to compute the coverage depth and read length requirements for the assembly of human chromosome 19. For thi'
  - rank 3 doc=2405.05734v3 sec=11 score=0.424242 stage=hybrid :: '## VI. CONCLUSIONS AND FUTURE WORK\n\nIn this paper, we present the first rigorous informationtheoretic analysis for the problem of diploid genome assembly. Diplo'
  - rank 4 doc=2405.05734v3 sec=4 score=0.366667 stage=hybrid :: '## III. INFORMATION THEORETIC NECESSARY CONDITIONS\n\nThese following conditions are necessary to ensure correct reconstruction of the haplotypes up to switch err'
  - rank 5 doc=2405.05734v3 sec=9 score=0.25 stage=hybrid :: '## C. Overlap graph\n\n1) Algorithm: A read overlap graph is constructed by adding directed edges between a pair of nodes (reads) if they share a suffix-prefix ov'

## 52694833-7001-4896-a030-e767eec3467b  [right_doc_wrong_section]
- query: What is the role of symmetric matrices in algebraic K-theory with involution?
- source/type: text-image / abstractive
- expected doc_id: 2405.02054v2
- expected section_id: 11
- expected section preview: '# A The trace map for rings with involution \n\nLet us finish the paper with a construction of a $\\mathbb{Z} / 2$-equivariant lift of the trace map tr: $\\mathrm{K} \\rightarrow$ $\\mathrm{TC}(-; p)$, for every prime $p$. The trace was first constructed by Bökstedt-Hsiang-Madsen in [BHM93] as a natural t'
- top 5 returned:
  - rank 1 doc=2405.02054v2 sec=12 score=1.0 stage=hybrid :: '# References \n\n[AN21] Benjamin Antieau and Thomas Nikolaus, Cartier modules and cyclotomic spectra, J. Amer. Math. Soc. 34 (2021), no. 1, 1-78. MR 4188814\n[Ara2'
  - rank 2 doc=2407.04378v2 sec=9 score=0.5 stage=hybrid :: '# REFERENCES \n\n[AHW17] Aravind Asok, Marc Hoyois, and Matthias Wendt, Affine representability results in $\\mathbb{A}^{1}$-homotopy theory, I: Vector bundles, Du'
  - rank 3 doc=2405.02054v2 sec=1 score=0.5 stage=hybrid :: '## Introduction\n\nLet $k$ be a field. Let us recall that Milnor conjectured, in [Mil71], [Mil70], that a certain canonical map of graded rings\n\n$$\n\\mathrm{K}_{*}'
  - rank 4 doc=2402.12350v3 sec=1 score=0.333333 stage=hybrid :: '## 1. INTRODUCTION\n\nRees valuations and rational powers of ideals play a central role in many results in algebraic geometry and commutative algebra $[3,12,13,20'
  - rank 5 doc=2409.09862v3 sec=24 score=0.2 stage=hybrid :: '# 2.2 Algebraic and Spectral Graph Theory \n\nAlgebraic graph theory is concerned with translating properties of graphs into algebraic properties, such as matrice'

## 5dccd210-faae-48b0-8052-b959455ccaf1  [right_doc_wrong_section]
- query: How does the performance of noise-based local learning compare with traditional algorithms like backpropagation?
- source/type: text / abstractive
- expected doc_id: 2412.12783v2
- expected section_id: 1
- expected section preview: '#### Abstract\n\nBrain-inspired learning in physical hardware has enormous potential to learn fast at minimal energy expenditure. One of the characteristics of biological learning systems is their ability to learn in the presence of various noise sources. Inspired by this observation, we introduce a n'
- top 5 returned:
  - rank 1 doc=2412.12783v2 sec=2 score=1.0 stage=hybrid :: '## I. INTRODUCTION\n\nRealizing learning in hardware by harnessing the physical properties of neuromorphic devices is currently a very active field of research ow'
  - rank 2 doc=2412.15021v4 sec=8 score=0.458333 stage=hybrid :: '# 4 Discussion \n\nThis work reports on the first, proof-of-concept implementation of event-based backpropagation on SpiNNaker2. While our results are limited by '
  - rank 3 doc=2412.12783v2 sec=13 score=0.333333 stage=hybrid :: '# C. Training multi-layer sMTJ networks \n\nNext, we wished to determine whether multilayer neural networks can be trained with real-world sampled noise. We there'
  - rank 4 doc=2412.15021v4 sec=1 score=0.253968 stage=hybrid :: '# 1 Introduction \n\nNeuromorphic computing seeks to emulate the unparalleled efficiency of biological neural networks by implementing spiking neural networks whi'
  - rank 5 doc=2406.18306v11 sec=10 score=0.25 stage=hybrid :: '## C. Results\n\nWe conduct a comparative performance analysis of the proposed learning-based method (with different DoA regression structures) and manifold optim'

## 6e2c7363-89ae-4430-95fb-da8a4e9c04d7  [right_doc_wrong_section]
- query: What role does vapor pressure data play in understanding boiling points of materials like iron?
- source/type: text-image / abstractive
- expected doc_id: 2409.02293v3
- expected section_id: 5
- expected section preview: '# B. Cluster energetics \n\nTo quantify the melting behavior of iron clusters, caloric curves of total energy ( $\\mathrm{eV} /$ atom) vs. temperature (K) were obtained for each cluster size. Each data point corresponds to a stitchedtogether (reordered) parallel tempering (PT) MD trajectory at one clus'
- top 5 returned:
  - rank 1 doc=2412.02269v2 sec=4 score=0.5 stage=hybrid :: '# B. Normal phase \n\nIn the normal phase, that is above the transition temperature, the condensed fraction is zero, and consequently, all atoms remain in excited'
  - rank 2 doc=2412.07042v1 sec=9 score=0.5 stage=hybrid :: '# 5. Conclusion \n\nThis study examined the growing demand for ChatGPT-related skills in the U.S. labor market, revealing the extent to which Gen AI technologies '
  - rank 3 doc=2409.02293v3 sec=18 score=0.333333 stage=hybrid :: '# REFERENCES \n\n${ }^{1}$ F. Tao, Metal Nanoparticles for Catalysis: Advances and Applications (Royal Society of Chemistry, 2014).\n${ }^{2}$ T. Imaoka, H. Kitaza'
  - rank 4 doc=2410.08642v2 sec=2 score=0.333333 stage=hybrid :: "## Related Work\n\nVisuals play an important role for the communication of CTs: images appear to provide immediate 'knowledge', and are powerful means in presenti"
  - rank 5 doc=2409.04439v3 sec=7 score=0.25 stage=hybrid :: '## 5. DISCUSSION \\& CONCLUSION\n### 5.1. Caveats and Previous State-of-the-art\n\nComputations of the pressure broadening coefficients for the aforementioned trans'

## 7b3343a0-8ec0-4d68-a3a6-81de181ed836  [right_doc_wrong_section]
- query: Why might TM-score be preferred over RMSD for evaluating RNA structures?
- source/type: text-image / abstractive
- expected doc_id: 2406.13839v2
- expected section_id: 17
- expected section preview: '## A. 3 RhoFold Length Bias\n\nWe investigate the performance of RhoFold on a representative subset of the training dataset used to train RNA-FrameFlow. Figure 8 shows that RhoFold has a sequence length bias where it predicts accurate structures with low RMSDs (to the ground truth) for specific sequen'
- top 5 returned:
  - rank 1 doc=2406.13839v2 sec=8 score=0.5 stage=hybrid :: '# 4.3 Generation quality across sequence lengths \n\nWe next investigate how sequence length affects the global realism of generated samples (measured by scTM). F'
  - rank 2 doc=2406.13839v2 sec=5 score=0.5 stage=hybrid :: '# 3 Experiments \n\n3D RNA structure dataset. RNAsolo (Adamczyk et al., 2022) is a recent dataset of RNA 3D structures extracted from isolated RNAs, protein-RNA c'
  - rank 3 doc=2406.13839v3 sec=7 score=0.392857 stage=hybrid :: '### 4.2 Local evaluation with structural measurements\n\nFor our best-performing model using diffusion timesteps $N_{T}=50$, we plot histograms of bond distance, '
  - rank 4 doc=2406.13839v2 sec=7 score=0.366667 stage=hybrid :: '### 4.2 Local evaluation with structural measurements\n\nFor our best-performing model using diffusion timesteps $N_{T}=50$, we plot histograms of bond distance, '
  - rank 5 doc=2406.13839v2 sec=22 score=0.340909 stage=hybrid :: '# C Additional Results\n## C. 1 Evaluation of MMDiff Samples\n\nHere, we document global and local metrics from samples generated by MMDiff. MMDiff has a validity '

## 96356cf3-afe2-4230-b1f3-d7caa31c1fde  [right_doc_wrong_section]
- query: What is the best performing method for audio inpainting at a gap length of 10 ms?
- source/type: text-image / extractive
- expected doc_id: 2403.04433v3
- expected section_id: 8
- expected section preview: '## D. Testing on a mid-scale dataset, including increased window/context length\n\nAn additional, mid-scale comparison was performed, using 60 signals selected from the IRMAS database [34], [35]. The\n![img-4.jpeg](img-4.jpeg)\n\nFig. 5. Comparison of the AR-based methods with SPAIN in terms of SDR, usin'
- top 5 returned:
  - rank 1 doc=2403.04433v3 sec=1 score=0.833333 stage=hybrid :: '## I. InTRODUCTION\n\nAudio inpainting is a challenging signal processing task, where missing parts of an audio signal have to be completed. For a human listener,'
  - rank 2 doc=2403.04433v3 sec=4 score=0.642857 stage=hybrid :: '## IV. EXPERIMENTS \\& RESULTS\n\nThe first dataset consists of 9 recordings of individual musical instruments ${ }^{2}$, taken from the EBU SQAM database [28]. Th'
  - rank 3 doc=2403.04433v3 sec=7 score=0.45 stage=hybrid :: '## C. Comparison with other methods\n\nTo provide a context for the results of AR-based methods, selected variants are compared with the methods that belong to th'
  - rank 4 doc=2403.04433v3 sec=9 score=0.45 stage=hybrid :: '## V. CONCLUSION\n\nA novel gap-wise modification of the Janssen method was proposed and evaluated against popular audio inpainting methods based on autoregressiv'
  - rank 5 doc=2403.04433v3 sec=3 score=0.333333 stage=hybrid :: '## III. AUDIO INPAINTING USING AUTOREGRESSION\n\nTo formalize the problem of audio inpainting, assume that the observed signal $\\mathbf{x} \\in \\mathbb{R}^{N}$ con'

## a6c723b4-b7c7-4269-b1bb-1e245f433ff5  [right_doc_wrong_section]
- query: What does "J-AM-NoSpec-epsilon" refer to in terms of program counter (pc) conditions?
- source/type: text-image / extractive
- expected doc_id: 2405.10089v2
- expected section_id: 46
- expected section preview: '# F. 1 Taint semantics \n\n![img-31.jpeg](img-31.jpeg)\n\n![img-32.jpeg](img-32.jpeg)\n\nNote that speculation only happens on indirect jumps in Rule J:AM-Jmp-att. An indirect jump happens when the address to jump to has to be fetched. This can happen if the jump address/label is inside a register. All ot'
- top 5 returned:
  - rank 1 doc=2410.15824v2 sec=29 score=0.5 stage=hybrid :: '### 14.2 Proof of Lemma 9.2(b)\n\nSince first term of $R_{t}^{(2)}$ i.e $\\left(\\prod_{k=1}^{g_{t}^{j}} L_{k}^{j}\\right) Q_{0}^{j} \\xrightarrow{P} 0$ as $t \\righta'
  - rank 2 doc=2405.10089v2 sec=50 score=0.5 stage=hybrid :: '# H Speculative Semantics SLS \n\nModern CPUs can speculatively bypass ret instructions. This kind of speculation is called straightline speculation (SLS) [5, 7].'
  - rank 3 doc=2405.10089v2 sec=127 score=0.333333 stage=hybrid :: '# T. 2 The Problem \n\nWe now explain why the model of Patrignani and Guarnieri [46] does not capture this vulnerability. Here is the program taken from [56, List'
  - rank 4 doc=2403.19186v2 sec=18 score=0.333333 stage=hybrid :: '# Appendix G. ALTERNATIVE MODELS. \n\nIn our formulation of the generalized Lotka-Volterra model Eq. A1, the role of the condition number $\\kappa$ on the interact'
  - rank 5 doc=2405.10089v2 sec=4 score=0.285714 stage=hybrid :: '# 2.3 Speculative Semantics \n\nThe target languages of the compilers we consider all have different speculative semantics modeling the effects of speculatively e'

## b76a0e45-7cbb-4608-b8ee-2c771ea27ef0  [right_doc_wrong_section]
- query: What conditions make ultrametric balls equivalent to other geometric shapes like boxes or singletons?
- source/type: text-image / abstractive
- expected doc_id: 2401.07317v2
- expected section_id: 8
- expected section preview: '# 2.3 Geometry of the Ultrametric Ball \n\nIn the following, let $B_{\\boxplus}(x, r)=\\left\\{z \\in \\mathbb{R}^{n}: d_{\\boxplus}(x, z)<r\\right\\}$ and $B_{\\boxplus}(x, r]=\\left\\{z \\in \\mathbb{R}^{n}: d_{\\boxplus}(x, z) \\leq r\\right\\}$ respectively denote the open and closed balls centered at $x$ with rad'
- top 5 returned:
  - rank 1 doc=2412.15576v4 sec=12 score=0.5 stage=hybrid :: '## D. Latency-Free Performance Analysis\n\nThis part explores strategies for coping with delays in dynamic environments by comparing the performance of QUART and '
  - rank 2 doc=2401.07317v2 sec=7 score=0.5 stage=hybrid :: '# 2.2 Generalized Norms and Ultrametric in Limit. \n\nLet $\\|\\cdot\\|$ be the Euclidean norm defined for all $x \\in \\mathbb{R}^{n}$ as $\\|x\\|=\\left(\\sum_{i \\in[n]}'
  - rank 3 doc=2406.04259v2 sec=2 score=0.333333 stage=hybrid :: '# 1. InTRODUCTION \n\nIn the last two decades, the problem of shape reconstruction has received increasing attention in theoretical and applied communities alike.'
  - rank 4 doc=2403.08977v2 sec=2 score=0.333333 stage=hybrid :: '# 1.1 Related work \n\nMotivated by the study of geometric matchings of planar point sets, Huemer et al. [8] proved that for any finite bichromatic point set $R \\'
  - rank 5 doc=2412.00566v2 sec=6 score=0.25 stage=hybrid :: '## VI. CONCLUSIONS AND OUTLOOK\n\nWe have studied the suitability of Conditional Variational Autoencoders (CVAE) to conduct parameter inference of microlensed GWs'

## b9f96e77-09e0-4795-ab19-9353bbac0f7e  [right_doc_wrong_section]
- query: How do different infrared wavelengths perform in cyclone prediction models?
- source/type: text-image / abstractive
- expected doc_id: 2409.16507v2
- expected section_id: 42
- expected section preview: '# 7. Importance-ranking of individual IR channels \n\nTo quantify the importance of individual IR channels, we train 10 different CNNs, each with one channel in the predictors. Other than IR channels, these models use the same hyperparameters as those in the final GeoCenter ensemble: a 600-by-600-km d'
- top 5 returned:
  - rank 1 doc=2409.16507v2 sec=10 score=0.5 stage=hybrid :: '# b. Predictors: IR satellite data \n\nOur first source of predictor data is IR imagery from geostationary sensors: the GOES-16 Advanced Baseline Imager (ABI) for'
  - rank 2 doc=2401.03345v2 sec=18 score=0.5 stage=hybrid :: '# 5 Empirical results: predicting future SPX smiles \n\nWe now look at how well each model can predict the future SPX volatility surface, using the methodology de'
  - rank 3 doc=2409.16507v2 sec=39 score=0.333333 stage=hybrid :: '# c. Further details on case studies \n\nFor every case study in the main text (Figures 13-16), only one random first guess is shown, along with all IR predictors'
  - rank 4 doc=2411.15519v1 sec=10 score=0.333333 stage=hybrid :: '# 2.5 Combination of GBM and Time Series Models \n\nWe aim to leverage the strengths of both the GBM and time series models while mitigating their respective weak'
  - rank 5 doc=2409.16507v2 sec=24 score=0.3 stage=hybrid :: '# b. Homogeneous comparison with ARCHER-2 \n\nWe perform a homogeneous comparison between GeoCenter and ARCHER-2, using the same TC samples to evaluate both model'

## f9ce4d40-606e-41e3-9f74-938ad0810117  [right_doc_wrong_section]
- query: Are matrix techniques used in the improvements of Heron and Heinz inequalities?
- source/type: text / extractive
- expected doc_id: 2409.16171v2
- expected section_id: 0
- expected section preview: "## - M.H.M. Rashid*\n\nDepartment of Mathematics\\&Statistics\nFaculty of Science P.O.Box(7)\nMu'tah University University\nMu'tah-Jordan\nmrash@mutah.edu.jo\n\nWael Mahmoud Mohammad Salameh\nFaculty of Information Technology\nAbu Dhabi University, Abu Dhabi 59911\nUnited Arab Emirates\nwael.salameh1@adu.ac.ae\n\n"
- top 5 returned:
  - rank 1 doc=2409.16171v2 sec=8 score=0.833333 stage=hybrid :: '## References\n\nFuad Kittaneh and Yousef Manasrah. Improved young and heinz inequalities for matrices. Journal of Mathematical Analysis and Applications, 361(1):'
  - rank 2 doc=2409.16171v2 sec=2 score=0.833333 stage=hybrid :: '## 1 Introduction\n\nConsider the algebra of complex matrices of size $n \\times n$, denoted as $M_{n}(\\mathbb{C})$. A matrix $T$ in $M_{n}(\\mathbb{C})$ is conside'
  - rank 3 doc=2409.16171v2 sec=7 score=0.45 stage=hybrid :: '# 6 Conclusion and Future Work \n\nIn conclusion, this paper has embarked on an extensive investigation into the domain of matrix means interpolation and comparis'
  - rank 4 doc=2409.16171v2 sec=1 score=0.366667 stage=hybrid :: '## ABSTRACT\n\nThis paper undertakes a thorough investigation of matrix means interpolation and comparison. We expand the parameter $\\vartheta$ beyond the closed '
  - rank 5 doc=2411.18627v2 sec=1 score=0.25 stage=hybrid :: '## 2 Introduction\n\nPhysics-based dynamical system modeling is a very powerful and interpretable tool that can be used to make predictions and can provide relati'

## faa2bf74-b122-487f-972c-3f3e37b20e38  [right_doc_wrong_section]
- query: How does chemical homeostasis influence branching patterns in engineered cell clusters?
- source/type: text-image / abstractive
- expected doc_id: 2407.06295v3
- expected section_id: 42
- expected section preview: '# C \n\nChemical Homeostasis\n![img-11.jpeg](img-11.jpeg)\n\nFIG. S5. Elongation, Branching and Chemical Regulation of Homeostasis. Final losses for a range of pruning thresholds shown on the left for gene network learned for (a) Elongation, (b) Branching, and (c) Chemical Homeostasis. Losses are average'
- top 5 returned:
  - rank 1 doc=2407.06295v3 sec=36 score=0.7 stage=hybrid :: '## Branching\n\nWe simulate the growth of a cluster from a single cell to 130 cells, restricting ourselves to the 2-dimensional case for computational simplicity.'
  - rank 2 doc=2407.06295v3 sec=4 score=0.625 stage=hybrid :: '# CHEMICAL REGULATION OF TISSUE HOMEOSTASIS \n\nMaintaining stable ratios of different cell populations is crucial for tissue function, and disruptions of this ba'
  - rank 3 doc=2407.06295v3 sec=34 score=0.5 stage=hybrid :: '## Chemical Regulation of Cellular Adhesion\n\nThe differential adhesion hypothesis posits that populations of cells can adopt specific morphologies based on diff'
  - rank 4 doc=2407.06295v3 sec=3 score=0.5 stage=hybrid :: '## SPATIAL CONTROL OF TISSUE GROWTH\n\nUnderstanding how to program the growth of complex shapes can aid in our comprehension of developmental body plans driven b'
  - rank 5 doc=2407.06295v3 sec=0 score=0.433333 stage=hybrid :: '#### Abstract\n\nUnderstanding the rules underlying organismal development is a major unsolved problem in biology. Each cell in a developing organism responds to '
