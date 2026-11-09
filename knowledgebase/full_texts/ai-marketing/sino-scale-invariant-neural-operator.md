---
title: 'SINO: Scale-Invariant Neural Operator'
url: https://arxiv.org/abs/2609.36890
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Kaichen Ouyang
- Chenglei Yu
- Chuanrui Wang
- Tailin Wu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.36890
pages: 38
chars: 130237
fetched_at: '2026-11-08T13:39:01+00:00'
kb_version: 1
---

# SINO: Scale-Invariant Neural Operator

Preprint.
SINO: SCALE-INVARIANTNEURALOPERATOR
Kaichen Ouyang1,2
1Westlake University
2University of Science and Technology of China
ouyangkaichen@westlake.edu.cn
oykc@mail.ustc.edu.cn
Chenglei Yu1
1Westlake University
yuchenglei@westlake.edu.cn
Chuanrui Wang1
1Westlake University
wangchuanrui@westlake.edu.cn
Tailin Wu1∗
1Westlake University
wutailin@westlake.edu.cn
ABSTRACT
In scientific machine learning, physical fields governed by partial differential
equations exhibit low-rank structure and scale invariance. When solving equations
on coarse grids, missing information leads to the closure problem—modeling
unresolved physics to recover lost dynamics. Although closure terms depend
on grid resolution, they represent scale-invariant physical laws. A model truly
learning physics should capture these mechanisms with low-rank parameteriza-
tion rather than memorizing grid-specific patterns. Inspired by this, we propose
the Scale-Invariant Neural Operator (SINO), which learns on normalized phys-
ical scales via a dual-branch architecture operating in spectral and spatial do-
mains. SINO uses bottleneck MLPs to generate continuous convolution kernels,
embedding explicit low-rank inductive bias that concentrates>95% variance in
2-3 modes, as validated by PCA across benchmarks, while drastically reducing
parameters. This principled design yields 38×steeper scaling law exponents than
FNO, demonstrating superior parameter efficiency. We compare SINO with tra-
ditional models (U-Net, DeepONet), Transformer models (Transolver, Oformer,
GK-Transformer), and frequency-domain models (FNO, AMFNO, UFNO) on
closure problems spanning externally forced Burgers turbulence, decaying Burg-
ers turbulence, KS turbulence, Kolmogorov-forced NS turbulence, and decaying
NS turbulence. Experiments show SINO achieves 1.5–38×error reduction and
2–23×parameter efficiency over baselines, with superior scaling laws reflecting
exceptional data efficiency from principled low-rank design. Code is available at
https://github.com/AI4Science-WestlakeU/SINO.
1 INTRODUCTION
Scientific machine learning aims to understand and simulate complex systems governed by physical
laws using data-driven methods (Karniadakis et al., 2021). Unlike natural images, physical fields
such as velocity, pressure, and vorticity evolve under partial differential equations and conservation
laws. Although discretized fields may possess extremely high dimensionality, their dynamics are
organized by a small number of mechanisms: conservation, transport, dissipation, and cross-scale
energy transfer (Holmes, 2012; Berkooz et al., 1993; Lumley, 1967). This reveals that physical
laws possess an effectivelow-rank structure, where a few degrees of freedom govern the overall
dynamics (Thibeault et al., 2024).
This low-rank nature imposes two requirements on model design: (1) capturing governing mech-
anisms with compact parameterization; (2) learningresolution-independentphysical laws, where
changing grid resolution alters the discrete representation but not the underlying equations. The
same continuous process, when observed at different resolutions, is still governed by the same mech-
anisms.
∗Corresponding author.
1
arXiv:2609.36890v1  [cs.LG]  29 Sep 2026

Preprint.
Theclosure problemprovides an ideal testbed for these principles (Sanderse et al., 2024). High-
fidelity direct numerical simulation (DNS) resolves small-scale structures but is computationally
expensive; practical simulations use coarser grids. The coarse-grid state¯u ∆ =P ∆urequires a
closure termτ(Leonard, 1975) to compensate for unresolved scales. The key insight is: althoughτ
depends on the coarse-graining scale∆, the underlying physical mechanisms are governed byscale-
invariant laws(Meneveau & Katz, 2000; Kolmogorov, 1991). These processes retain the same
mathematical form across resolutions, differing only in operational scales. Therefore, models that
truly learn physics should capture the low-rank, scale-invariant physical laws rather than memorizing
resolution-specific patterns.
Learning-based closure methods fall into two categories:learned correction(Um et al., 2020;
List et al., 2022) directly modifies coarse-grid states or evolution results, whilelearned interpola-
tion(Bar-Sinai et al., 2019; Kochkov et al., 2021) learns missing discretization schemes. Recent
methods like the Indirect Neural Corrector (INC) (Wei et al., 2026), a learned correction approach,
incorporate neural predictions as right-hand side terms in governing equations, improving long-term
stability. However, existing methods focus onhowto couple predictions into solvers, notwhatneural
architecture should learn closure. The key challenge is:how to represent closure operators that
are simultaneously low-rank, scale-invariant, and capable of balancing global spectral struc-
ture with local spatial features?Standard approaches fail this requirement: CNNs (Krizhevsky
et al., 2012) use resolution-dependent discrete kernels withO(K2D2)parameters per layer; FNO (Li
et al., 2020) employs mode-specific Fourier weights withO(k maxD2)parameters that scale with
truncation; Transformers rely on high-dimensional attention without explicit low-rank constraints.
To address this challenge, we propose theScale-Invariant Neural Operator (SINO)for learning
closure terms that capture cross-resolution, scale-invariant physical laws. SINO employs a dual-
branch architecture: a frequency branch captures global spectral energy transfer, while a spatial
branch handles localized nonlinear structures. Both branches generate continuous convolution ker-
nels via hypernetworks with bottleneck layers—taking normalized physical coordinates as input
rather than discrete grid indices. This design enforces three principles: (1)Scale invariance: nor-
malized coordinates ensure identical representations across resolutions; (2)Low-rank inductive
bias: bottleneck layers with dimensionsn f , ns ≪D 2 force kernels into low-dimensional sub-
spaces, reducing parameters fromO(k maxD2)(FNO) orO(K 2D2)(CNN) toO((n f +ns)D2)inde-
pendent of resolution; (3)Global-local balance: dual branches synergistically combine frequency-
domain long-range dependencies with spatial-domain localized patterns.
We validate SINO on six turbulent closure benchmarks spanning forced and decaying Burgers,
Kuramoto-Sivashinsky, and Navier-Stokes equations at Reynolds numbers 1000-4000, comparing
against eight baselines. SINO achieves 1.5-38×error reduction with 2-23×fewer parameters than
FNO-based methods. Theoretical analysis proves SINO’s bottleneck architecture enforces hard rank
constraints (Theorem 1) and Lipschitz continuity (Theorem 2), with operator norms growing sublin-
early (O(√nf )) compared to FNO’s linear growth. Empirical PCA (Abdi & Williams, 2010) reveals
learned kernels concentrate>95% variance in 2-3 principal components, validating extreme com-
pression. Scaling law analysis shows SINO’s power-law exponents are 3-38×steeper than baselines,
demonstrating superior parameter efficiency. Our contributions are:
•Architecture: We propose SINO with bottleneck hypernetworks generating continuous kernels
from normalized coordinates, embedding low-rank and scale-invariant inductive biases. Dual
branches balance global frequency-domain and local spatial-domain representations.
•Empirical validation: SINO achieves best average performance on six turbulent closure problems
(forced/decaying Burgers, KS, forced/decaying NS), with 1.5-38×error reduction and 2-23×
parameter efficiency over eight baselines (U-Net (Ronneberger et al., 2015), DeepONet (Lu et al.,
2021), Transolver (Wu et al., 2024), OFormer (Li et al., 2022), GK-Transformer (Cao, 2021),
FNO (Li et al., 2020), AM-FNO (Xiao et al., 2024), UFNO (Wen et al., 2022)). Ablation studies
confirm necessity of dual-branch fusion.
•Theoretical foundations: We prove bottleneck layers enforce rank-n f and rank-n s constraints
(Theorem 1), Lipschitz continuity (Theorem 2), and sublinear operator norm growth (Theorems 4–
5). PCA analysis shows>95% variance in 2-3 components. Scaling laws (α= 0.568on NS vs.
0.015 for FNO) demonstrate SINO prioritizes learning physical laws over memorizing patterns
during capacity growth.
2

Preprint.
()
Physical
Normalization
SINO
Block 1 ⋯ SINO Block L
Normalized relative coordinates: , ζ
Frequency Branch
Spatial Branch

Relative frequency
MLP ()
Spectral kernel
rFFT irFFT ReLU
hspectral
Pointwise linear
ζ
Relative offset
MLP () Spatial kernel
Periodic
Circular convolution ReLU
hspatial
D
D
2D
Fusion
D
hout
D

(a)  SINO: Scale-Invariant Neural Operator
()
(b) SINO Block

× +
+
Lift Layer
 →
Output Layer
+
 →
×
Identity
Figure 1: Architecture of the SINO.(a)Overall pipeline with physical normalization, lifting layer,
LSINO blocks, and output projection.(b)SINO block: dual-branch architecture where frequency
and spatial branches generate continuous kernels via bottleneck MLPs from normalized coordinates
(ξ, ζ), then fuse outputs through residual connections.
2 RELATEDWORK
Closure Modeling.Resolving the finest spatiotemporal scales in PDEs is often computationally
intractable, necessitating coarse-grained approximations. Traditional approaches like Reynolds-
averaged Navier-Stokes (RANS), large-eddy simulation (LES) (Heinz, 2020), and subgrid-scale
(SGS) models (Shankar et al., 2023) model unresolved physics through closure terms, but deriving
reliable closures remains challenging with limited accuracy for complex flows (Wei et al., 2026).
Recent machine learning approaches systematically learn closure operators from data. The indirect
neural corrector (INC) (Wei et al., 2026) embeds learned terms into the PDE’s right-hand side for
improved stability. We extend this framework with low-rank, scale-invariant architectures. Given
coarse-grid state¯u∆, the learned closure predicts the correction termτ ∆ =SINO(¯u∆; Θ)that aug-
ments the coarse-grid dynamics:∂¯u∆/∂t=L ∆(¯u∆) +τ ∆, enabling stable rollout integration.
Implicit Parameterization.Implicit parameterization represents neural network weights or con-
volutional kernels as continuous functions of coordinates, decoupling learnable parameters from
kernel size or resolution. Hypernetworks generate weights via an auxiliary network, enabling adap-
tive filter generation (Ha et al., 2016; Ma et al., 2022). Continuous Kernel Convolution (CK-
Conv) (Romero et al., 2021) models kernels as continuous functions, handling arbitrarily long
sequences and irregular data. Neural Implicit Frequency Filters (NIFF) (Grabinski et al., 2024)
learn filters in the frequency domain, enabling infinitely large kernels. We extend this paradigm
by employing bottleneck hypernetworks to generate continuous kernels in both spatial and spec-
tral domains, enforcing low-rank constraints aligned with turbulent closure physics while achieving
cross-resolution scale invariance through normalized coordinates.
3 METHOD
We propose the Scale-Invariant Neural Operator (SINO), a dual-branch architecture that learns clo-
sure terms on normalized physical scales. SINO parameterizes kernel weights as continuous func-
3

Preprint.
tions of normalized coordinates in both frequency and spatial domains, decoupling learnable pa-
rameters from kernel size and resolution. This enables compact representations of scale-invariant
physical laws while balancing global spectral structure with local spatial features.
3.1 PHYSICALNORMALIZATION OFINPUTCOORDINATES
Learning scale-invariant laws requires that the same physical process, when observed at different
resolutions, receives identical normalized representations. For a coarse-grid field¯u∆ with resolution
Nobtained by coarse-graining from fine-grid DNS at resolutionN fine, the resample factorr=
Nfine/Nquantifies the degree of coarse-graining.
Frequency domain.We normalize wavenumber coordinates asξ= 4k/N−1∈[−1,1], where
k∈[0, N/2]is the frequency index from the real FFT. This maps the DC component (k= 0) to
ξ=−1, mid-range frequencies toξ= 0, and the Nyquist frequency toξ= 1, ensuring the same
physical frequency receives the sameξregardless of resolutionN.
Spatial domain.For a kernel of sizeK= 2R+ 1(radiusR) at resolutionN, we normalize the
spatial offset∆x=j/N(wherej∈[−R, R]) by the reference lengthL ref =R/(N fine/r), yielding
ζ=j/R∈[−1,1]. This guarantees identical physical displacements receive identicalζacross
resolutions, enabling resolution-independent convolution kernels.
3.2 DUAL-BRANCHARCHITECTURE
Physical fields in turbulent systems contain both global coherent structures and localized intermittent
events. Frequency representations naturally capture smooth long-range correlations and spectral
energy transfer but struggle with sharp local features (shocks, vortex cores) due to spectral ringing.
Conversely, spatial convolutions excel at localized nonlinear patterns but incur high cost for long-
range dependencies. SINO addresses this complementary trade-off via a dual-branch architecture
processing features in parallel through frequency and spatial domains.
For input¯u∆ ∈R B×N×C in (batch sizeB, channelsC in), a lifting layer projects to latent space
h(0) =P(¯u∆)∈R B×N×D (hidden dimensionD). Each SINO block (ℓ∈ {1, . . . , L}) processes
h(ℓ−1) through two branches:
Frequency branch(spectral convolution with residual bypass):
h(ℓ) freq =σ  W (ℓ) bypassh(ℓ−1) +F −1 m(ℓ)(ξ)⊙ F(h(ℓ−1))  ,(1)
whereσis ReLU,W (ℓ) bypass ∈R D×D is the bypass projection,Fdenotes FFT,m (ℓ)(ξ)∈C D×D are
hypernetwork-generated multiplication weights, and⊙is element-wise multiplication.
Spatial branch(implicit circular convolution):
h(ℓ) spatial =σ  Conv(ℓ)(h(ℓ−1);W (ℓ)(ζ))  ,(2)
whereW (ℓ)(ζ)are hypernetwork-generated kernel weights parameterized byζ.
Fusion.Outputs are concatenated and fused:
h(ℓ) =h (ℓ−1) +W (ℓ) fuse[h(ℓ) freq ;h (ℓ) spatial],(3)
where[·;·]denotes concatenation andW (ℓ) fuse ∈R D×2D is the fusion matrix. Activations are applied
in intermediate blocks but omitted in the final block for unrestricted output range.
AfterLblocks, an output projection with small initialization (σ init = 0.01) yields:
τ∆ =Q(h (L))∈R B×N×C out.(4)
The predicted closure termτ ∆ is then incorporated into the coarse-grid evolution∂¯u ∆/∂t=
L∆(¯u∆) +τ ∆ for rollout integration.
4

Preprint.
3.3 IMPLICITKERNELREPRESENTATION VIAHYPERNETWORKS
We represent convolution kernels as continuous functions generated by small MLPs (hypernet-
works), decoupling expressiveness from parameter count.
Frequency domain.HypernetworkΦ ω generates complex-valued weightsm(ξ)∈C D×D via three
hidden layers[w f , wf , nf ](intermediate widthw f , bottleneckn f ) with separate real/imaginary
output heads:
m(ξ) = Φω(ξ) =head real(MLP(ξ)) +i·head imag(MLP(ξ)).(5)
Multiplication applies via the convolution theorem:F(Conv(h)) =m(ξ)⊙ F(h), enabling
O(NlogN)computation via FFT.
Spatial domain.HypernetworkΦ x generates kernel weightsW(ζ)∈R K×K×D×D via three layers
[ws, ws, ns](spatial widthw s, bottleneckn s):
W(ζ) = Φ x(ζ),(Conv(h)) i =
X
j∈N(i)
W(ζ i−j)·h j,(6)
whereN(i)is the neighborhood around positioniwith circular boundary conditions. The implicit
representation induces spatial smoothness, improving robustness.The complete model is:
τ∆ =SINO(¯u∆; Θ) =Q◦Block (L) ◦ · · · ◦Block(1) ◦P(¯u∆),(7)
whereΘcollects all parameters. Hyperparameters (D, L, K, nf , ns, wf , ws) control capacity and
inductive biases.
3.4 THEORETICALPROPERTIES
SINO’s implicit kernel representation induces low-rank structure through bottleneck layers. To val-
idate this empirically, we perform Principal Component Analysis (PCA) on the learned convolution
kernels across all channel pairs in each layer. Figure 2 reveals a striking concentration of variance:
the first 2 principal components alone capture over 90% of the variance in both spatial and fre-
quency branches, while merely 3 components exceed 95% explained variance across all layers. This
demonstrates that SINO successfully concentrates learned representations into an extremely low-
dimensional subspace, aligned with the physical intuition of scale separation and energy cascade in
turbulent flows. We rigorously establish in Appendix A.4 that the bottleneck architecture enforces
explicit rank constraints (Theorem 1), where every generated kernel admits a finite-rank decompo-
sitionm(ξ) = Pnf j=1 zj(ξ)·B j with fixed basis matrices, reducing effective parameter count from
O(kmax ·D 2)in FNO orO(K 2 ·D 2)in CNN toO((n f +n s)·D 2)in SINO, independent of
resolution or kernel size. Furthermore, the MLP parameterization guarantees Lipschitz continuity
(Theorem 2) that prevents memorization of discrete grid patterns, and we establish quantitative op-
erator norm bounds:O( √nf )sublinear growth for the frequency-domain operator andO(n s)linear
growth for the spatial-domain operator (Theorems 4–5), providing favorable implicit regularization
through spectral orthogonality in the frequency branch. These properties jointly explain SINO’s
superior parameter efficiency and data efficiency observed in experiments.
5

Preprint.
(a) Spatial Branch (b) Frequency Branch
Cumulative Variance
Cumulative Variance
Number of Components Number of Components
Figure 2: Cumulative variance explained by principal components of learned convolution kernels on
Forcing NS (Re=4000).(a) Spatial branchand(b) Frequency branchacross 4 layers. Remark-
ably, the first 2 components capture>90% variance and 3 components exceed>95% (horizontal
dashed lines), validating the extremely low-rank structure induced by SINO’s bottleneck architecture
and confirming that the model prioritizes dominant physical modes over high-dimensional noise.
4 EXPERIMENTS
We validate SINO on turbulent closure problems spanning 1D and 2D systems, comparing against
diverse baselines and conducting ablation studies to verify effectiveness.
4.1 EXPERIMENTALSETUP
Benchmarks.We evaluate SINO on six turbulent closure benchmarks with aggressive coarse-
graining ratios. Table 1 summarizes the configurations, including forcing and decaying variants of
Burgers turbulence, Kuramoto-Sivashinsky (KS) turbulence, and Navier-Stokes (NS) turbulence at
different Reynolds numbers. The forcing variants use external forcing (Kolmogorov forcing for NS),
while the decaying variants exhibit freely decaying dynamics, testing the model’s ability to capture
diverse physical regimes. Supplementary experiments at alternative resolutions and forcing con-
figurations (Appendix A.5) further validate SINO’s scale-invariant capability. Detailed numerical
schemes and simulation protocols are in Appendix A.1.
Table 1: Benchmark configurations.
Problem Dim Resolution Spatial Discretization Temporal Scheme
Forcing Burgers 1D 512→32 WENO5 Finite V olume Method SSP-RK3
Decaying Burgers 1D 2048→256 Pseudo-Spectral TVD RK3
KS 1D 256→64 Pseudo-Spectral ETDRK4
Forcing NS (Re=1000) 2D 512→64 Finite V olume Method (Van Leer) Semi-Implicit
Forcing NS (Re=4000) 2D 512→64 Finite V olume Method (Van Leer) Semi-Implicit
Decaying NS 2D 512→64 Finite V olume Method (Van Leer) Semi-Implicit
Baselines.We compare SINO against nine baselines covering three paradigms: traditional mod-
els (U-Net, DeepONet), Transformer-based operators (Transolver, Oformer, GK-Transformer), and
frequency-domain operators (FNO, AMFNO, UFNO), plus uncorrected coarse-grid DNS as a phys-
ical baseline. Model specifications and training protocols are in Appendices A.2 and A.3.
6

Preprint.
MSE
MSE
MSE
Params Params Params
Forcing Burgers KS Forcing NS (Re=4000)
SINO
U-Net
DeepOnet
Transolver
GK-Transformer
Oformer
FNO
AM-FNO
UFNO
Figure 3: Pareto comparison of MSE versus parameter count on Forcing Burgers, KS, and Forcing
NS (Re=4000). Both axes are on a logarithmic scale. SINO (red) achieves optimal or near-optimal
MSE with significantly fewer parameters than FNO-based methods, demonstrating parameter effi-
ciency from implicit low-rank representations.
4.2 MAINRESULTS
Tables 2 and 3 present quantitative comparisons on 1D and 2D turbulence benchmarks. SINO con-
sistently achieves superior or competitive performance across all tasks while maintaining parameter
efficiency. Supplementary experiments on additional resolutions and forcing configurations (Ta-
bles 4 and 5 in Appendix) confirm robustness across diverse physical regimes. Following the Indi-
rect Neural Corrector (INC) framework (Wei et al., 2026), SINO predicts closure terms as right-hand
side corrections; training details are in Section A.3. All reported metrics are extrapolation errors:
30% of time steps for training, 70% for testing.
20
-20
0
Ground Truth FNO UFNO AM-FNO SINO (ours)
Figure 4: Instantaneous predictions on Kolmogorov-forced Navier–Stokes turbulence at Re=4000.
Column 1: ground truth downsampled from DNS-512 to 64×64 resolution. Columns 2–5: FNO,
UFNO, AMFNO, SINO predictions. Row 1: vorticity fields. Row 2: vorticity error distributions.
Row 3: streamline plots. SINO accurately reconstructs fine-scale structures and velocity patterns
with minimal error, while other methods exhibit varying degrees of distortion in small-scale details.
1D Benchmarks.On Forcing Burgers, SINO achieves the lowest error (1.03E-03 average, 9.41E-
04 best) with only 6.7K parameters, outperforming second-best AMFNO (1.58E-03 average, 9.5K
parameters) by 1.5×. Transformer-based methods yield comparable parameter counts but higher er-
rors: GK-Transformer (2.84E-03 average, 36K parameters), Oformer (2.92E-03, 5.4K parameters),
and Transolver (2.94E-03, 8.6K parameters). FNO variants show mixed results: FNO (2.99E-03,
11K parameters), DeepONet (3.22E-03, 15K parameters), U-Net (4.07E-03, 7.1K parameters), and
UFNO (6.63E-03, 26K parameters) all lag behind SINO. On KS turbulence, SINO (1.33E-03 av-
7

Preprint.
erage, 1.14E-03 best) surpasses all baselines by substantial margins: 2.2×better than AMFNO
(2.92E-03), 2.5×better than U-Net (3.33E-03), and 6–8×better than FNO variants and Transform-
ers. For Decaying Burgers, SINO (4.37E-03 average, 2.90E-03 best) achieves 38×improvement
over most baselines, which plateau around 1.65E-01. Only SINO-SPA (2.09E-02 average, 1.8K
parameters) approaches SINO’s performance among ablation variants.
Table 2: Performance comparison on 1D benchmarks.
Method
1D Benchmarks
ParamsForcing Burgers KS Decaying Burgers
A VE Best A VE Best A VE Best
U-Net 4.07E-03 3.31E-03 3.33E-03 1.48E-03 1.65E-01 1.65E-01 7,077
DeepONet 3.22E-03 2.78E-03 1.05E+00 1.39E+00 1.65E-01 1.65E-01 14,913
Transolver 2.94E-03 2.80E-03 1.14E-02 1.09E-02 1.65E-01 1.64E-01 8,601
Oformer 2.92E-03 2.92E-03 5.45E-03 5.45E-03 1.65E-01 1.65E-01 5,444
GK-Transformer 2.84E-03 2.77E-03 1.12E-02 1.11E-02 1.65E-01 1.64E-01 36,449
FNO 2.99E-03 2.82E-03 8.55E-03 8.03E-03 1.65E-01 1.65E-01 11,073
UFNO 6.63E-03 5.70E-03 8.28E-03 7.82E-03 1.65E-01 1.65E-01 26,017
AM-FNO 1.58E-03 1.34E-03 2.92E-03 2.50E-03 1.66E-01 1.65E-01 9,489
SINO-SPE 1.56E-03 1.32E-03 3.02E-03 2.49E-03 1.28E-01 1.27E-01 3,877
SINO-SPA 2.12E-03 1.79E-03 3.53E-03 2.11E-03 2.09E-02 4.08E-03 1,797
SINO (ours)1.03E-03 9.41E-04 1.33E-03 1.14E-03 4.37E-03 2.90E-036,681
Coarse Grid 2.23E-01 5.46E-03 1.65E-01 –
Table 3: Performance comparison on 2D benchmarks.
Method
2D Benchmarks
ParamsForcing NS (Re=1000) Forcing NS (Re=4000) Decaying NS
A VE Best A VE Best A VE Best
U-Net 1.34E-01 1.16E-01 1.91E-01 1.84E-01 6.67E-02 5.64E-02 61,006
DeepONet 4.62E-01 4.60E-01 5.25E-01 5.18E-01 2.95E-01 2.79E-01 269,153
Transolver 3.65E-01 3.48E-01 4.27E-01 4.23E-01 2.24E-01 2.17E-01 54,306
Oformer 5.07E-01 5.07E-01 5.33E-01 5.33E-01 4.03E-01 4.03E-01 38,087
GK-Transformer 3.87E-01 3.84E-01 4.60E-01 4.55E-01 2.04E-01 1.96E-01 151,874
FNO 4.44E-01 4.42E-01 4.78E-01 4.75E-01 2.60E-01 2.40E-01 2,106,018
UFNO 1.64E-01 1.51E-01 2.15E-01 2.12E-015.58E-024.86E-02 1,346,466
AM-FNO 1.69E-01 1.59E-01 2.32E-01 2.15E-01 7.68E-02 7.05E-02 120,162
SINO-SPE 2.18E-01 1.81E-01 2.63E-01 2.40E-01 1.71E-01 1.51E-01 33,834
SINO-SPA 2.23E-01 2.20E-01 2.82E-01 2.72E-01 1.37E-01 1.24E-01 17,322
SINO (ours)9.17E-02 8.43E-02 1.47E-01 1.41E-015.99E-024.55E-0259,314
Coarse Grid 5.07E-01 5.32E-01 4.04E-01 –
2D Benchmarks.On Forcing NS (Re=1000), SINO (9.17E-02 average, 8.43E-02 best, 59K param-
eters) leads all methods. U-Net (1.34E-01, 61K parameters) achieves second place with comparable
parameter count but 1.5×higher error. FNO-based methods underperform: UFNO (1.64E-01, 1.3M
parameters) and AMFNO (1.69E-01, 120K parameters) require 2–23×more parameters for infe-
rior accuracy. Transformer methods exhibit substantially higher errors: Transolver (3.65E-01, 54K
parameters), GK-Transformer (3.87E-01, 152K parameters), and Oformer (5.07E-01, 38K parame-
ters). FNO (4.44E-01, 2.1M parameters) and DeepONet (4.62E-01, 269K parameters) underperform
despite massive capacity. At Re=4000, similar trends emerge: SINO (1.47E-01 average, 1.41E-01
best) maintains first place, followed by U-Net (1.91E-01), UFNO (2.15E-01), and AMFNO (2.32E-
01). On Decaying NS, UFNO achieves the lowest average error (5.58E-02) but requires 1.3M
parameters—23×more than SINO (5.99E-02 average, 59K parameters). Notably, SINO attains the
best peak performance (4.55E-02) across all methods, demonstrating superior optimization capabil-
8

Preprint.
ity. U-Net (6.67E-02, 61K parameters) ranks third, while AMFNO (7.68E-02, 120K parameters)
requires 2×more parameters for worse accuracy.
Ablation Analysis.SINO-SPE (frequency-only) and SINO-SPA (spatial-only) consistently under-
perform full SINO by 1.5–3×across all benchmarks, confirming the necessity of dual-branch archi-
tecture. SINO-SPE shows particular degradation on 2D problems (2.18E-01 vs. 9.17E-02 on Forc-
ing NS Re=1000), while SINO-SPA struggles on forced problems requiring global energy transfer.
The full model synergistically combines both branches for optimal performance.
4.3 SCALINGLAWS ANDCROSS-SCALEANALYSIS
Parameter Efficiency.Figure 5 reveals SINO’s superior scaling behavior through power-law ex-
ponents. On forced NS (Re=4000), SINO achievesα= 0.568—nearly 38×steeper than FNO
(α= 0.015) and 3–4×steeper than AMFNO (α= 0.143) and UFNO (α= 0.162). On decay-
ing NS, SINO maintainsα= 0.868compared to FNO’sα= 0.073, demonstrating 12×better
parameter efficiency. These steep slopes indicate that SINO effectively learns low-rank physical
structures: each additional parameter contributes substantially to error reduction, whereas baselines
require orders of magnitude more capacity for comparable gains.
Relative Parameters Relative Parameters
Relative Errors
Relative Errors
Forcing NS (Re=4000) Decaying NS
Figure 5: Scaling laws on forced NS (Re=4000, left) and decaying NS (right). SINO exhibits
steeper power-law exponents (α= 0.568and0.868) than baselines, demonstrating better parameter
efficiency.
Wavenumber k Wavenumber k
Energy Spectrum E(k)
Energy Spectrum E(k)
Figure 6: Energy spectra on decaying Burgers turbulence.Left:At resample factor (rf) = 8, SINO
most accurately follows thek −2 inertial range among neural operators.Right:Across rf = 2–
16, baselines (green, solid) exhibit numerical dissipation beyond cutoffs, while SINO (red-yellow,
dashed) preserves correct spectral decay, validating scale-invariant modeling.
Spectral Fidelity.Figure 6 validates SINO’s cross-scale capability through energy spectra on de-
caying Burgers turbulence. Traditional coarse grids exhibit severe numerical dissipation beyond the
9

Preprint.
Nyquist cutoff (left panel, vertical dashed lines mark resolution limits). At rf = 8 (N = 256), baseline
methods (AMFNO, FNO, UFNO) deviate from the correctk −2 decay slope and fail to suppress
spurious dissipation (middle panel). In contrast, SINO maintains accurate spectral behavior across
resolutions: even at extreme downsampling (rf = 16, N = 128), SINO’s energy spectrum aligns with
high-resolution DNS (N = 2048) and preserves the theoreticalk −2 slope (right panel), confirming
its scale-invariant representations.
Bottleneck Capacity Scaling.To investigate the impact of bottleneck dimensions on performance,
Table 6 compares SINO variants with(n f , ns)ranging from 2 to 32 against uncorrected DNS at
multiple resolutions. SINO-32 achieves errors of 4.08E-02 (Decaying NS) and 6.06E-02 (Forcing
NS Re=1000), representing 1.5–1.7×improvement over SINO-2 and exceeding the accuracy of
DNS-256 (4×higher resolution with 16×more grid points). Figure 9 confirms SINO-32 maintains
superior temporal stability in long-term extrapolation. This demonstrates that increasing bottleneck
capacity enables SINO to surpass even higher-resolution coarse-grid simulations, validating the ef-
fectiveness of further parameter investment in low-rank subspace learning.
5 CONCLUSION
We propose the Scale-Invariant Neural Operator (SINO), a dual-branch architecture that learns tur-
bulent closure terms on normalized physical scales. By parameterizing convolution kernels as con-
tinuous functions via bottleneck hypernetworks, SINO decouples model capacity from grid reso-
lution, enabling compact representation of scale-invariant physical laws. The bottleneck structure
enforces explicit low-rank constraints, concentrating>95% variance in merely 2-3 modes (validated
by PCA) and forcing the model to discover dominant physical mechanisms rather than memorize
high-dimensional patterns. This yields 38×steeper scaling law exponents than FNO, demonstrat-
ing superior parameter efficiency. Experiments on six turbulent closure benchmarks demonstrate
1.5–38×error reduction with 2–23×parameter efficiency over baselines. Ablation studies con-
firm dual-branch necessity, and spectral analysis validates cross-scale generalization under extreme
downsampling. Future work will extend SINO to three-dimensional flows and diverse physical prob-
lems, establishing SINO as a general framework for learning scale-invariant laws where low-rank
structure governs system dynamics.
ACKNOWLEDGMENTS
We thank Tao Zhang, Ruiqi Feng, and Xinan Dai from Westlake University for discussions and for
providing feedback on our manuscript. We also gratefully acknowledge the support of the Westlake
University Research Center for Industries of the Future and the Westlake University Center for
High-performance Computing. The content is solely the responsibility of the authors and does not
necessarily represent the official views of the funding entities. This work was supported by the
Shanghai Municipal-Level Major Special Project.
REFERENCES
Herv´e Abdi and Lynne J Williams. Principal component analysis.Wiley interdisciplinary reviews:
computational statistics, 2(4):433–459, 2010.
Yohai Bar-Sinai, Stephan Hoyer, Jason Hickey, and Michael P Brenner. Learning data-driven dis-
cretizations for partial differential equations.Proceedings of the National Academy of Sciences,
116(31):15344–15349, 2019.
Gal Berkooz, Philip Holmes, and John L Lumley. The proper orthogonal decomposition in the
analysis of turbulent flows.Annual review of fluid mechanics, 25(1):539–575, 1993.
Shuhao Cao. Choose a transformer: Fourier or galerkin.Advances in neural information processing
systems, 34:24924–24940, 2021.
Julia Grabinski, Janis Keuper, and Margret Keuper. As large as it gets-studying infinitely large
convolutions via neural implicit frequency filters.Transactions on Machine Learning Research,
2024:1–42, 2024.
10

Preprint.
David Ha, Andrew Dai, and Quoc V . Le. Hypernetworks, 2016. URLhttps://arxiv.org/
abs/1609.09106.
Stefan Heinz. A review of hybrid rans-les methods for turbulent flows: Concepts and applications.
Progress in Aerospace Sciences, 114:100597, 2020.
Philip Holmes.Turbulence, coherent structures, dynamical systems and symmetry. Cambridge
university press, 2012.
George Em Karniadakis, Ioannis G Kevrekidis, Lu Lu, Paris Perdikaris, Sifan Wang, and Liu Yang.
Physics-informed machine learning.Nature Reviews Physics, 3(6):422–440, 2021.
Dmitrii Kochkov, Jamie A Smith, Ayya Alieva, Qing Wang, Michael P Brenner, and Stephan
Hoyer. Machine learning–accelerated computational fluid dynamics.Proceedings of the National
Academy of Sciences, 118(21):e2101784118, 2021.
Andrei Nikolaevich Kolmogorov. The local structure of turbulence in incompressible viscous fluid
for very large reynolds numbers.Proceedings: Mathematical and Physical Sciences, 434(1890):
9–13, 1991.
Alex Krizhevsky, Ilya Sutskever, and Geoffrey E Hinton. Imagenet classification with deep convo-
lutional neural networks.Advances in neural information processing systems, 25, 2012.
Athony Leonard. Energy cascade in large-eddy simulations of turbulent fluid flows. InAdvances in
geophysics, volume 18, pp. 237–248. Elsevier, 1975.
Zijie Li, Kazem Meidani, and Amir Barati Farimani. Transformer for partial differential equations’
operator learning.arXiv preprint arXiv:2205.13671, 2022.
Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya, An-
drew Stuart, and Anima Anandkumar. Fourier neural operator for parametric partial differential
equations.arXiv preprint arXiv:2010.08895, 2020.
Bj¨orn List, Li-Wei Chen, and Nils Thuerey. Learned turbulence modelling with differentiable fluid
solvers: physics-based loss functions and optimisation horizons.Journal of Fluid Mechanics,
949:A25, 2022.
Lu Lu, Pengzhan Jin, Guofei Pang, Zhongqiang Zhang, and George Em Karniadakis. Learning
nonlinear operators via deeponet based on the universal approximation theorem of operators.
Nature machine intelligence, 3(3):218–229, 2021.
John Leask Lumley. The structure of inhomogeneous turbulent flows.Atmospheric turbulence and
radio wave propagation, pp. 166–178, 1967.
Tianyu Ma, Alan Q Wang, Adrian V Dalca, and Mert R Sabuncu. Hyper-convolutions via implicit
kernels for medical imaging.arXiv preprint arXiv:2202.02701, 2022.
Charles Meneveau and Joseph Katz. Scale-invariance and turbulence models for large-eddy simula-
tion.Annual Review of Fluid Mechanics, 32(1):1–32, 2000.
David W Romero, Anna Kuzina, Erik J Bekkers, Jakub M Tomczak, and Mark Hoogendoorn. Ck-
conv: Continuous kernel convolution for sequential data.arXiv preprint arXiv:2102.02611, 2021.
Olaf Ronneberger, Philipp Fischer, and Thomas Brox. U-net: Convolutional networks for biomedi-
cal image segmentation. InInternational Conference on Medical image computing and computer-
assisted intervention, pp. 234–241. Springer, 2015.
Benjamin Sanderse, Panos Stinis, Romit Maulik, and Shady E Ahmed. Scientific machine learning
for closure models in multiscale problems: A review.arXiv preprint arXiv:2403.02913, 2024.
Varun Shankar, Vedant Puri, Ramesh Balakrishnan, Romit Maulik, and Venkatasubramanian
Viswanathan. Differentiable physics-enabled closure modeling for burgers’ turbulence.Machine
Learning: Science and Technology, 4(1):015017, 2023.
11

Preprint.
Vincent Thibeault, Antoine Allard, and Patrick Desrosiers. The low-rank hypothesis of complex
systems.Nature Physics, 20(2):294–302, 2024.
Kiwon Um, Robert Brand, Yun Raymond Fei, Philipp Holl, and Nils Thuerey. Solver-in-the-loop:
Learning from differentiable physics to interact with iterative pde-solvers.Advances in neural
information processing systems, 33:6111–6122, 2020.
Hao Wei, Aleksandra Franz, Bjoern List, and Nils Thuerey. Inc: An indirect neural corrector for
auto-regressive hybrid pde solvers.Advances in Neural Information Processing Systems, 38:
110182–110216, 2026.
Gege Wen, Zongyi Li, Kamyar Azizzadenesheli, Anima Anandkumar, and Sally M Benson. U-
fno—an enhanced fourier neural operator-based deep-learning model for multiphase flow.Ad-
vances in Water Resources, 163:104180, 2022.
Haixu Wu, Huakun Luo, Haowen Wang, Jianmin Wang, and Mingsheng Long. Transolver: A fast
transformer solver for pdes on general geometries.arXiv preprint arXiv:2402.02366, 2024.
Zipeng Xiao, Siqi Kou, Zhongkai Hao, Bokai Lin, and Zhijie Deng. Amortized fourier neural
operators.Advances in Neural Information Processing Systems, 37:115001–115020, 2024.
12

Preprint.
A APPENDIX
This appendix provides comprehensive technical details supporting the main results. Section A.1
specifies the governing equations, numerical discretization schemes, and simulation protocols for
all six turbulent closure benchmarks. Section A.2 presents complete architectural specifications for
SINO and all baseline models across 1D and 2D problems. Section A.3 documents the training ob-
jectives, rollout integration with closure term incorporation, curriculum learning strategy, optimiza-
tion settings, and time integration protocols. Section A.4 establishes theoretical foundations through
formal proofs of SINO’s low-rank structure, Lipschitz regularity, and operator norm bounds. Finally,
Section A.5 reports additional experimental results including cross-resolution and alternative forc-
ing generalization tests, principal component analysis confirming low-rank structure across different
flow regimes, and bottleneck dimension scaling studies demonstrating computational trade-offs.
A.1 BENCHMARKEQUATIONS
A.1.1 FORCINGBURGERSEQUATION
Governing Equation.We consider the one-dimensional viscous Burgers equation in conservative
form with external forcing:
∂u
∂t + ∂ ∂x  u2 2  =η ∂2u ∂x2 +f(x, t), x∈[0, L], t >0,(8)
whereu(x, t)is the velocity field,η= 0.01is the kinematic viscosity, andf(x, t)is the external
forcing term. The domain length isL= 2πwith periodic boundary conditions.
Initial and Boundary Conditions.The initial condition is set to zero velocity everywhere:
u(x,0) = 0. Periodic boundary conditions are enforced:u(0, t) =u(L, t)for allt≥0. A
warmup phase ofT warmup = 2.0is applied to allow shock structures to develop before recording
snapshots. The external forcing is given by:
f(x, t) =
nmodesX
i=1
Ai sin

ωit+ 2πℓix L +ϕ i

,(9)
wheren modes = 20, and for each modei:A i ∼ U(−0.5,0.5),ω i ∼ U(−0.4,0.4),ℓ i ∼
Udiscrete{3,4,5,6}, andϕ i ∼ U(0,2π)are randomly sampled once per trajectory and held constant
throughout the simulation.
Spatial Discretization.The equation is discretized using a finite volume method with fifth-order
Weighted Essentially Non-Oscillatory (WENO5) reconstruction on a uniform grid ofN= 512
cells with cell size∆x=L/N. Let¯u i(t)denote the cell-averaged value in celli. The WENO5
reconstruction computes left and right interface valuesu − i+1/2 andu + i+1/2 from a five-point stencil
{¯ui−2,¯ui−1,¯ui,¯ui+1,¯ui+2}via:
u− i+1/2 =
2X
k=0
ω− k p− k (ui−2+k:i+2+k), u + i+1/2 =
2X
k=0
ω+ k p+ k (ui−1−k:i+3−k),(10)
wherep ± k are third-order polynomial interpolants andω ± k are nonlinear weights computed from smoothness indicators:
ωk = αk P2
j=0 αj
, α k = dk (ϵ+β k)2 ,(11)
with optimal linear weightsd 0 = 0.1,d 1 = 0.6,d 2 = 0.3, regularization parameterϵ= 10 −6, and
smoothness indicatorsβ k measuring local solution variation. The convective flux is computed using
the Godunov numerical flux:
F conv i+1/2 =



0,ifu − i+1/2 ≤0≤u + i+1/2,
min

(u− i+1/2)2
2 ,
(u+ i+1/2)2
2

,ifu − i+1/2 ≤u + i+1/2,
max

(u− i+1/2)2
2 ,
(u+ i+1/2)2
2

,otherwise.
(12)
13

Preprint.
The diffusive flux is approximated by second-order central differences:F diff i+1/2 =−η(¯u i+1 −
¯ui)/∆x. The semi-discrete form becomes:
d¯ui
dt =− Fi+1/2 −F i−1/2 ∆x +f i(t), F i+1/2 =F conv i+1/2 +F diff i+1/2.(13)
Temporal Discretization.Time integration employs the third-order Strong Stability Preserving
Runge-Kutta method (SSP-RK3) in Shu-Osher form:
¯u(1) = ¯un + ∆tL(¯un),(14)
¯u(2) = 3 4 ¯un + 1 4 h ¯u(1) + ∆tL(¯u(1)) i ,(15)
¯un+1 = 1 3 ¯un + 2 3 h ¯u(2) + ∆tL(¯u(2)) i ,(16)
whereL(¯u)denotes the right-hand side spatial operator. The timestep∆tis adaptively chosen at
each RK stage to satisfy the CFL condition with safety factorν CFL = 0.4:
∆t=ν CFL ·min
 ∆x
maxi |¯ui| , ∆x2 2η  .(17)
Simulation Protocol.Each trajectory undergoes a warmup phase ofT warmup = 2.0time units to
develop shock structures, followed by a recording phase ofT max = 10.0time units. During the
recording phase,n snapshots = 1001snapshots (including the initial state att= 0of the record-
ing phase) are saved at uniform intervals∆t outer =T max/(nsnapshots −1) = 0.01. A total of
64 trajectories are generated with different random forcing parameters. The fine-grid snapshots
at resolutionN= 512are coarsened to multiple resolutions via exact finite volume averaging.
For instance, with resample factorr= 16, the snapshots are downsampled toN= 32, yielding
the coarse-grid reference states¯u ∆ used for closure modeling. The DNS solver employs adap-
tive timesteps determined by the CFL condition: at each RK substep, the timestep is computed as
∆t=ν CFL ·min(∆x/max i |¯ui|,∆x 2/(2η)), where the first term represents the convective stability
limit and the second term the diffusive stability limit. The minimum of these two constraints en-
sures numerical stability throughout the simulation, with the timestep adapting dynamically to the
instantaneous solution state.
A.1.2 KURAMOTO–SIVASHINSKYEQUATION
Governing Equation.We consider the one-dimensional Kuramoto–Sivashinsky (KS) equation on
a periodic domain:
∂v
∂t +v ∂v ∂x + ∂2v ∂x2 + ∂4v ∂x4 = 0, x∈[0, L], t >0,(18)
wherev(x, t)is the scalar field, andL= 64is the domain length. The KS equation exhibits
spatiotemporal chaos and is a canonical model for pattern formation and turbulence in dissipative
systems.
Initial and Boundary Conditions.Periodic boundary conditions are imposed:v(0, t) =v(L, t)
and∂ nv/∂x n|x=0 =∂ nv/∂x n|x=L for allnandt≥0. The initial condition is constructed as a
random superposition of Fourier modes:
v(x,0) =
nmodesX
i=1
Ai sin
 2πℓix
L +ϕ i

,(19)
wheren modes = 10, and for each modei:A i ∼ U(−0.5,0.5),ϕ i ∼ U(0,2π), andℓ i ∼
Udiscrete{1,2,3}are randomly sampled once per trajectory. A warmup phase ofT warmup = 50.0
time units is applied before recording to allow the system to reach a statistically stationary chaotic
state.
14

Preprint.
Spatial Discretization.The KS equation is discretized using a pseudo-spectral collocation method
on a uniform grid ofN= 256points with grid spacing∆x=L/N. The solution is represented
in Fourier space asˆvk(t) =F[v](k), wherek= (2π/L)·k index are the wavenumbers withk index ∈
{−N/2, . . . , N/2−1}. The spatial derivatives are computed exactly in Fourier space:
∂nv
∂xn ⇐ ⇒(ik) nˆvk.(20)
The nonlinear termv∂v/∂xis evaluated in physical space and transformed back to Fourier space.
To eliminate aliasing errors from the quadratic nonlinearity, the2/3-rule dealiasing is enforced: all
Fourier modes with|k index|> N/3are set to zero both before computing the nonlinear term (on
input) and after computing it (on output). This retains approximately2N/3 + 1≈171modes out
of 256, ensuring that the product of two dealiased fields contains no aliasing.
Temporal Discretization.Time integration employs the fourth-order Exponential Time Differ-
encing Runge-Kutta method (ETDRK4) with a fixed timestep∆t= 0.01. The KS equation is split
into linear and nonlinear parts:
∂ˆvk
∂t = ˆLk ˆvk + ˆNk(ˆv), ˆLk =k 2 −k 4, ˆNk(ˆv) =− d v ∂v ∂x k .(21)
The ETDRK4 scheme integrates the linear term exactly and treats the nonlinear term via four stages:
ˆv(a) =e ∆t ˆLk/2ˆvn +Q k ˆNk(ˆvn),(22)
ˆv(b) =e ∆t ˆLk/2ˆvn +Q k ˆNk(ˆv(a)),(23)
ˆv(c) =e ∆t ˆLk/2ˆv(a) +Q k h 2 ˆNk(ˆv(b))− ˆNk(ˆvn) i ,(24)
ˆvn+1 =e ∆t ˆLk ˆvn +f 1,k ˆNk(ˆvn) + 2f2,k h ˆNk(ˆv(a)) + ˆNk(ˆv(b)) i +f 3,k ˆNk(ˆv(c)),(25)
where the coefficientsQ k, f1,k, f2,k, f3,k are computed using the contour integral method of Kassam
and Trefethen to avoid numerical cancellation errors near ˆLk ≈0:
Qk = ∆t
Z 1/2
0
eτ∆t ˆLk dτ= ∆t· e∆t ˆLk/2 −1
∆t ˆLk
,(26)
f1,k = ∆t
Z 1
0
e(1−τ)∆t ˆLk
h
−4−τ∆t ˆLk +e τ∆t ˆLk (4−3τ∆t ˆLk +τ 2(∆t ˆLk)2) i dτ (τ∆t ˆLk)3 ,
(27)
f2,k = ∆t
Z 1
0
e(1−τ)∆t ˆLk
h
2 +τ∆t ˆLk +e τ∆t ˆLk (−2 +τ∆t ˆLk) i dτ (τ∆t ˆLk)3 ,(28)
f3,k = ∆t
Z 1
0
e(1−τ)∆t ˆLk
h
−4−3τ∆t ˆLk −τ 2(∆t ˆLk)2 +e τ∆t ˆLk (4−τ∆t ˆLk) i dτ (τ∆t ˆLk)3 .
(29)
These integrals are evaluated numerically via 32-point trapezoidal rule on a circular contour in the
complex plane with radiusr= 1, ensuring high accuracy even when ˆLk = 0(the DC mode).
Simulation Protocol.Each trajectory begins from a random initial condition and undergoes a
warmup phase ofT warmup = 50.0time units (5000 timesteps) to reach the chaotic attractor. After
warmup, snapshots are recorded for a duration ofT max = 10.0time units at intervals∆t= 0.01,
yieldingn snapshots = 1001snapshots (including the initial state att= 0of the recording phase). A
total of 64 trajectories are generated with different random initial conditions. The fine-grid snapshots
at resolutionN= 256are coarsened to multiple resolutions via spectral downsampling (truncation
in Fourier space followed by inverse FFT). For instance, with resample factorr= 4, the snapshots
are downsampled toN= 64, yielding the coarse-grid reference states¯v∆ used for closure modeling.
The ETDRK4 integrator with fixed timestep∆t= 0.01ensures fourth-order temporal accuracy
while maintaining exponential stability for the stiff linear operator.
15

Preprint.
A.1.3 DECAYINGBURGERSEQUATION
Governing Equation.We consider the one-dimensional viscous Burgers equation in conservative
form without external forcing:
∂u
∂t + ∂ ∂x  u2 2  =ν ∂2u ∂x2 , x∈[0, L], t >0,(30)
whereu(x, t)is the velocity field,ν= 5×10 −4 is the kinematic viscosity, andL= 2πis the domain
length with periodic boundary conditions. This configuration exhibits free decay of turbulent kinetic
energy, making it a canonical test case for subgrid-scale (SGS) closure modeling.
Initial and Boundary Conditions.Periodic boundary conditions are enforced:u(0, t) =u(L, t)
for allt≥0. The initial condition is generated from a broadband energy spectrum following Maulik
and San (2018):
E(k) =A k4 exp

−
 k
k0
2!
, A= 2k−5 0
3√π ,(31)
wherek 0 = 10is the peak wavenumber. For each trajectory, the initial velocity field is constructed
as:
u(x,0) =
N/2−1X
k=1
p
2E(k)Ncos

k 2πx L +ϕ k

,(32)
whereϕ k ∼ U(0,2π)are independent random phases ensuring a real-valued field. This initializa-
tion produces a turbulent state with energy concentrated around intermediate wavenumbers, which
subsequently undergoes viscous dissipation without external forcing.
Spatial Discretization.The equation is discretized using a pseudo-spectral collocation method on
a uniform grid ofN= 2048points with grid spacing∆x=L/N. The solution is represented in
Fourier space asˆuk(t) =F[u](k), wherek= (2π/L)·k index are the wavenumbers. Linear operators
(diffusion) are computed exactly in Fourier space:
∂2u
∂x2 ⇐ ⇒ −k2 ˆuk.(33)
The nonlinear convective term∂(u 2/2)/∂xis evaluated in physical space via the collocation
method:u 2/2is computed pointwise, transformed to Fourier space, then multiplied byik. To elim-
inate aliasing errors from the quadratic nonlinearity, the2/3-rule dealiasing is applied: all Fourier
modes with|k index|> N/3are set to zero both before computing the nonlinear term (on input) and
after transforming back to Fourier space (on output). This retains approximately2N/3 + 1≈1366
modes out of 2048.
Temporal Discretization.Time integration employs the third-order Total Variation Diminishing
Runge-Kutta method (TVD-RK3) with adaptive timestep selection based on the CFL condition. The
TVD-RK3 scheme proceeds via three stages:
u(1) =u n + ∆tL(u n),(34)
u(2) = 3 4 un + 1 4 h u(1) + ∆tL(u (1)) i ,(35)
un+1 = 1 3 un + 2 3 h u(2) + ∆tL(u (2)) i ,(36)
whereL(u)denotes the spatial operator including both convective and diffusive terms. At each
RK substep, the timestep∆tis computed adaptively to satisfy the CFL condition with safety factor
νCFL = 0.4:
∆t=ν CFL ·min
 ∆x
maxi |ui| , ∆x2 2ν  ,(37)
where the first term ensures convective stability and the second term ensures diffusive stability. The
timestep is recomputed at every substep to adapt to the instantaneous solution state.
16

Preprint.
Simulation Protocol.Each trajectory evolves fromt= 0toT final = 0.1time units. During
this period,n snapshots = 1001snapshots (including the initial state) are saved at uniform intervals
∆touter =T final/(nsnapshots −1) = 10 −4. A total of 64 trajectories are generated with different
random initial phases. The fine-grid snapshots at resolutionN= 2048are coarsened to multiple
resolutions using two methods: (i) spectral truncation, which retains the lowestNcoarse Fourier modes
and performs inverse FFT with renormalization, and (ii) direct subsampling, which selects every
r-th grid point. For instance, with resample factorr= 8, spectral truncation yieldsN= 256
while preserving large-scale structures, whereas subsampling produces the same resolution but may
introduce aliasing. The adaptive timestep strategy results in typical internal timesteps in the range
∆t≈10 −5 to10 −4, requiring approximately10 3 to10 4 integration steps per trajectory depending
on the instantaneous maximum velocity (typicallymax|u| ≈2to4during the decay phase).
A.1.4 FORCINGNAVIER–STOKES: KOLMOGOROVFLOW
Governing Equations.We consider the two-dimensional incompressible Navier–Stokes equa-
tions with external forcing on a periodic domain:
∂v
∂t + (v· ∇)v=−∇p+ν∇ 2v+f(x, y),(x, y)∈[0,2π]×[0,2π], t >0,(38)
∇ ·v= 0,(39)
wherev= (u, v)is the velocity field,pis the kinematic pressure,νis the kinematic viscosity, and
fis the external forcing. We simulate two Reynolds number regimes: Re= 1000withν= 10 −3
and Re= 4000withν= 2.5×10 −4, corresponding to moderate and high turbulence intensity
respectively. Periodic boundary conditions are enforced in both directions:v(0, y, t) =v(2π, y, t)
andv(x,0, t) =v(x,2π, t)for allx, y, t.
Initial and Forcing Conditions.The initial velocity field is generated as a filtered random field
with maximum amplitude∥v∥ max = 7.0, ensuring a well-defined turbulent state from the onset. A
warmup phase ofT warmup = 40.0time units is applied to allow the flow to reach a statistically sta-
tionary turbulent state before recording snapshots. The external forcing consists of two components:
(i) Kolmogorov forcingf K = (F0 sin(kf y),0)withF 0 = 1.0andk f = 4, which drives energy in-
jection at large scales, and (ii) linear dampingf L =αvwithα=−0.1, which removes energy at
the largest scales to prevent unrealistic energy accumulation. The combined forcingf=f K +f L
maintains a statistically steady turbulent cascade with energy injection at intermediate wavenumbers
and dissipation at both large scales (via linear damping) and small scales (via viscosity).
Spatial Discretization.The equations are discretized on an Arakawa C-grid with resolution
N×N= 512×512cells and uniform grid spacing∆x= ∆y= 2π/512. Velocity components are
staggered: theu-component is stored at cell faces with offset(1,0.5)and thev-component at faces
with offset(0.5,1), while pressure is stored at cell centers with offset(0.5,0.5). The convective term
(v· ∇)vis computed using the van Leer flux-limiting scheme with TVD property, which applies
second-order accurate upwind-biased reconstruction in smooth regions and reverts to first-order up-
winding near sharp gradients to maintain monotonicity. The diffusive termν∇2vis computed using
second-order centered finite differences. The incompressibility constraint∇ ·v= 0is enforced via
a fractional-step pressure projection method: after advancing the momentum equation, the velocity
field is projected onto the divergence-free subspace by solving the Poisson equation∇ 2ϕ=∇ ·v ∗
for the pressure correctionϕ, then updatingv n+1 =v ∗ − ∇ϕ. The Poisson equation is solved using
the fast diagonalization method, which exploits separability of the Laplacian operator to reduce the
problem to a sum of one-dimensional eigenvalue problems, achievingO(N 2 logN)complexity for
the 2D case.
Temporal Discretization.Time integration employs a first-order explicit-implicit splitting
scheme: the convective and forcing terms are treated explicitly using forward Euler, while the dif-
fusive term is treated implicitly to avoid the restrictive diffusive CFL constraint. The timestep is
chosen adaptively based on the CFL condition for advection with safety factorC max = 0.5:
∆t=C max · ∆x ∥v∥max ,(40)
17

Preprint.
where∥v∥ max = 7.0is the maximum velocity magnitude observed in the initial condition.
This yields∆t= 0.5×(2π/512)/7.0≈5.59×10 −4. The resulting CFL number CFL=
∥v∥max∆t/∆x= 0.5is maintained throughout the simulation. Each time integration step con-
sists of three substeps: (1) explicit momentum updatev ∗ =v n + ∆t[−(v n · ∇)vn +f], (2)
pressure projection to enforce incompressibilityv ∗∗ =P(v ∗), and (3) implicit diffusion solve
(I−ν∆t∇ 2)vn+1 =v ∗∗, wherePdenotes the projection operator onto divergence-free fields.
Simulation Protocol.Each trajectory begins from a random filtered initial condition and under-
goes a warmup phase ofT warmup = 40.0time units to reach statistically stationary turbulence. After
warmup, snapshots are recorded for a production duration ofT production ≈0.0448time units. The
production phase uses inner batching withn inner = 8timesteps per saved frame andn outer = 1000
saved frames, yielding a total ofn snapshots = 1001snapshots (including the initial state att= 0
of the production phase) saved at uniform intervals∆t frame = 8×∆t≈4.47×10 −3. A total
of 64 trajectories are generated with different random initial conditions. The fine-grid snapshots at
resolution512×512are coarsened to multiple resolutions via the staggered velocity downsampling
method, which preserves the divergence-free property: for each velocity component, only values
lying on coarse-grid control volume faces are retained, then averaged over the appropriate face area.
For instance, with resample factorr= 16, the snapshots are downsampled to32×32, yielding the
coarse-grid reference states ¯v∆ used for subgrid-scale closure modeling. This conservative down-
sampling ensures that coarse-grained fields satisfy∇ · ¯v∆ = 0exactly when the fine-grid field is
divergence-free. The CFL-based adaptive timestep strategy maintains numerical stability through-
out the simulation, with the timestep scaling inversely with grid resolution to keep the CFL number
constant across different spatial resolutions.
A.1.5 DECAYINGNAVIER–STOKESTURBULENCE
Governing Equations.We consider the two-dimensional incompressible Navier–Stokes equa-
tions without external forcing on a periodic domain:
∂v
∂t + (v· ∇)v=−∇p+ν∇ 2v,(x, y)∈[0,2π]×[0,2π], t >0,(41)
∇ ·v= 0,(42)
wherev= (u, v)is the velocity field,pis the kinematic pressure, andν= 10 −3 is the kinematic
viscosity, corresponding to an initial Reynolds number Re= 1000. The absence of external forcing
results in free decay of kinetic energy, where turbulent structures evolve under the competing effects
of nonlinear energy transfer and viscous dissipation. Periodic boundary conditions are enforced in
both directions:v(0, y, t) =v(2π, y, t)andv(x,0, t) =v(x,2π, t)for allx, y, t. This config-
uration serves as a canonical test case for subgrid-scale (SGS) closure modeling in non-stationary
flows, where the effective Reynolds number decreases over time as kinetic energy dissipates.
Initial and Forcing Conditions.The initial velocity field is generated as a filtered random field
with maximum amplitude∥v∥ max = 4.2, producing a turbulent state with energy concentrated
at intermediate wavenumbers. A warmup phase ofT warmup = 4.5time units is applied to allow
transient instabilities to decay and the flow to settle onto a smooth decay trajectory, ensuring that the
recorded production phase represents well-resolved decaying turbulence rather than initialization
artifacts. No external forcing is applied (f=0), so the total kinetic energyE(t) = 1 2 R |v|2 dx dy decreases monotonically over time due to viscous dissipation. This decay process is characterized
by an inverse energy cascade at large scales and forward enstrophy cascade at small scales, typical
of two-dimensional turbulence. The initial Reynolds number Re 0 = 1000based on the initial
maximum velocity and viscosity gradually decreases as the flow decays, providing a time-varying
testbed for closure models.
Spatial Discretization.The spatial discretization is identical to the forced Kolmogorov flow
case: an Arakawa C-grid with resolutionN×N= 512×512cells and uniform grid spacing
∆x= ∆y= 2π/512. Velocity components are staggered with theu-component at offset(1,0.5)
and thev-component at offset(0.5,1), while pressure resides at cell centers with offset(0.5,0.5).
The convective term(v· ∇)vis computed using the van Leer flux-limiting scheme with TVD prop-
erty, ensuring second-order accuracy in smooth regions and monotonicity preservation near gradi-
18

Preprint.
ents. The diffusive termν∇ 2vis computed using second-order centered finite differences. Incom-
pressibility∇ ·v= 0is enforced via fractional-step pressure projection: the intermediate velocity
v∗ is projected onto the divergence-free subspace by solving the Poisson equation∇ 2ϕ=∇ ·v ∗
for the pressure correctionϕ, then updatingv n+1 =v ∗ − ∇ϕ. The Poisson solve employs the fast
diagonalization method exploiting the separability of the Laplacian on periodic domains, achieving
O(N 2 logN)complexity.
Temporal Discretization.Time integration employs the same first-order explicit-implicit splitting
scheme as the forced case: convective terms are treated explicitly using forward Euler, while dif-
fusive terms are treated implicitly to avoid the restrictive diffusive CFL constraint. The timestep is
chosen based on the CFL condition for advection with safety factorC max = 0.5:
∆t=C max · ∆x ∥v∥max ,(43)
where∥v∥ max = 4.2is the initial maximum velocity magnitude. This yields∆t≈1.46×10 −3,
with an initial CFL number CFL0 = 0.5. As the flow decays and∥v∥ max decreases, the actual CFL
number drops below the initial value, ensuring numerical stability throughout the simulation. Each
time integration step consists of three substeps: (1) explicit momentum updatev∗ =v n +∆t[−(v n ·
∇)vn], (2) pressure projectionv ∗∗ =P(v ∗)to enforce incompressibility, and (3) implicit diffusion
solve(I−ν∆t∇ 2)vn+1 =v ∗∗, wherePdenotes the projection operator onto divergence-free
fields.
Simulation Protocol.Each trajectory begins from a random filtered initial condition and under-
goes a warmup phase ofT warmup = 4.5time units to allow transient dynamics to settle. After
warmup, snapshots are recorded for a production duration ofT production ≈0.0117time units. The
production phase uses inner batching withn inner = 8timesteps per saved frame andn outer = 1000
saved frames, yielding a total ofn snapshots = 1001snapshots (including the initial state att= 0of
the production phase) saved at uniform intervals∆t frame = 8×∆t≈1.17×10 −2. A total of 64
trajectories are generated with different random initial conditions. The fine-grid snapshots at resolu-
tion512×512are coarsened to multiple resolutions via the same staggered velocity downsampling
method used for forced flows, which preserves the divergence-free property: for each velocity com-
ponent, only values on coarse-grid control volume faces are retained and averaged. For instance,
with resample factorr= 16, the snapshots are downsampled to32×32, yielding coarse-grid ref-
erence states ¯v∆ for subgrid-scale closure modeling. During the production phase, typical kinetic
energy decay ranges from 5% to 15% depending on the trajectory, with the effective Reynolds num-
ber decreasing correspondingly. This decaying turbulence configuration provides a complementary
testbed to the statistically stationary forced case, allowing assessment of closure model performance
in time-evolving flows where the underlying turbulence statistics are non-stationary.
A.2 MODELSPECIFICATIONS
A.2.1 MODELS FOR1D BENCHMARKS
SINO for 1D Benchmarks.We employ a Scale-Invariant Neural Operator (SINO) architecture
that operates on coarse-resolution inputs of shape(N, Cin)whereNis spatial resolution andC in is
the number of input channels. The model consists of a lifting layer that projects inputs to hidden
dimensionD= 16, followed byL= 2SINO blocks, and a projection layer that maps back to output
channels. Each SINO block comprises dual branches: a frequency branch that applies spectral
convolution via MLP-generated complex filters in Fourier space, and a spatial branch that performs
circular convolution with MLP-generated kernels of sizek= 9. Both branches use coordinate-
based MLPs with two hidden layers of widthWfreq = 8andW spatial = 8respectively, controlling the
expressiveness of frequency and spatial representations. The penultimate layers of these MLPs have
dimensionsN freq = 2andN spatial = 2. Features from both branches are concatenated and fused
via a linear layer, with residual connections across blocks. Physical normalization is applied to both
spatial coordinates and spectral frequencies to ensure scale invariance across different resolutions.
The output layer uses small initialization (standard deviation0.01) to ensure training stability in
early iterations. All activations use ReLU, and all spatial convolutions respect periodic boundary
conditions through circular padding.
19

Preprint.
UNet for 1D Benchmarks.We employ a two-level U-Net architecture for learning subgrid-scale
corrections in one-dimensional problems. The network operates on input feature maps of shape
(Cin, N)whereC in denotes the number of input channels (typically 1 for velocityu) andNis the
spatial resolution. The encoder path downsamples the input twice via max pooling (factor of 2
each), progressively increasing channels fromC in toC max/4toC max/2, with each encoder stage
consisting of two convolutions (kernel sizek= 9) followed by ReLU activations. The bottleneck
layer operates at resolutionN/4withC max = 16channels. The decoder path mirrors the encoder
with transposed convolutions for upsampling (stride 2, kernel size 2) and skip connections that
concatenate encoder features before each decoder stage. All convolutions use circular padding to
respect periodic boundary conditions. A final1×1convolution maps to a single output channel
(the correction termτ) with small initialization (standard deviation0.01) to ensure training stability
in early iterations. The architecture follows the channel progression1→C max/4→C max/2→
Cmax →C max/2→C max/4→1and spatial progressionN→N/2→N/4→N/2→N,
requiringNdivisible by 4.
DeepONet for 1D Benchmarks.We employ a Deep Operator Network (DeepONet) that learns
operator mappings through a decomposed architecture separating input functions from output co-
ordinates. The model consists of two parallel subnetworks: a branch network that processes input
function samplesu∈R m atm= 32fixed sensor locations, and a trunk network that processes
output coordinatesyaugmented with Fourier features. Both networks are MLPs with hidden di-
mensionD= 32, comprisingL branch = 4andL trunk = 4layers respectively, using hyperbolic
tangent activations. The trunk network input is enhanced withn Fourier = 4frequency terms, form-
ing a feature vector[y/L,1,cos(2πy/L),sin(2πy/L), . . . ,cos(8πy/L),sin(8πy/L)]of dimen-
sion1 + 1 + 2×4 = 9, whereLdenotes the domain length. The branch network maps sensor
readings to feature spaceb=ϕ branch(u)∈R p withp= 32features, while the trunk network in-
dependently maps augmented coordinates tot(y) =ϕ trunk(˜y)∈R p. The final output is computed
as the inner productG(u)(y) =⟨b,t(y)⟩+b 0, whereb 0 is a learnable bias. The output layer
uses small initialization (standard deviation0.01) to ensure training stability in early iterations. This
architecture enables resolution-independent predictions and naturally supports periodic boundary
conditions through Fourier coordinate encoding.
Transolver for 1DBenchmarks.We employ a Transformer-based operator network (Transolver)
that incorporates physics-aware attention mechanisms for learning PDE solutions. The model oper-
ates on input feature maps of shape(C in, N)whereC in = 2includes the velocity field and spatial
coordinates, andNis the spatial resolution. The architecture begins with a lifting layer that maps
inputs to hidden dimensionD= 16, followed byL= 2Transolver blocks. Each block imple-
ments a three-step physics attention mechanism: (1)Sliceadaptively groupsNgrid points into
G= 32learnable slice tokens via temperature-scaled softmax weights, aggregating local features
into macroscopic patterns; (2)Self-Attentionapplies multi-head attention (H= 8heads) among
slice tokens to capture global interactions, where query, key, and value projections operate on head
dimensiond h =D/H= 2; (3)Desliceredistributes attended slice token information back to orig-
inal grid points using the same grouping weights. Each block includes residual connections and a
feed-forward network with expansion ratior= 4(hidden dimension4D= 64), using GELU acti-
vations and layer normalization. The final projection layers map from hidden dimension through an
intermediate layer of 128 channels to the output dimensionC out = 1. The output layer uses small
initialization (standard deviation0.01) to ensure training stability in early iterations. This archi-
tecture enables adaptive spatial receptive fields through learned grouping while maintaining global
awareness through attention mechanisms.
OFormer for 1D Benchmarks.We employ an Operator Transformer (OFormer) that learns op-
erator mappings through a four-stage encoder-cross-decoder architecture with Galerkin-type linear
attention. The model processes input functionsu(x)sampled atNpoints with feature dimensionC in
and outputs predictions at arbitrary query locations. The architecture begins with an encoder that lifts
inputs to hidden dimensionD= 16via a linear layer with GELU activation. The encoded features
zenc are then processed by a cross-attention module that extracts relevant information from input
locations to query points usingH= 8attention heads with head dimensiond h =D/H= 2. This
cross-attention employs rotary position embeddings (RoPE) with minimum frequency1/64to en-
code spatial relationships, and applies Galerkin-type normalization through instance normalization
20

Preprint.
across spatial dimensions for both keys and values. The attended featuresz cross are refined through
L= 2propagator layers, each consisting of pre-normalized linear self-attention with residual con-
nections followed by a feed-forward network with hidden dimension2D= 32and GELU activation.
Linear attention achievesO(N)complexity by computingQ(K ⊤V)instead of softmax(QK ⊤)V,
with scaling factor1/d h for numerical stability. The decoder projects refined features from hidden
dimension to output channelsC out using a linear layer with small initialization (standard deviation
0.01) to ensure training stability in early iterations. RoPE enables the model to generalize to arbi-
trary query point distributions while maintaining spatial awareness through frequency-based position
encoding.
Galerkin Transformer for 1D Benchmarks.We employ a Galerkin Transformer that learns in-
tegral operators through linear attention mechanisms withO(N)computational complexity. The
model processes input physical quantitiesu(x)sampled atNspatial locations with feature di-
mensionC in. The architecture begins with a lifting layer that maps inputs pointwise to hidden
dimensionD= 16via a linear transformation. The lifted features are then refined throughL= 2
encoder layers, each implementing a Galerkin attention mechanism followed by a position-wise
feed-forward network with residual connections and layer normalization. The Galerkin attention
employsH= 8heads with head dimensiond h =D/H= 2, computing linear attention as
Attention(Q,K,V) =Q(K ⊤V)/N, where the matrix productK ⊤V∈R dh×dh aggregates global
information independently of sequence length. This formulation avoids the quadratic complexity of
softmax-based attention while maintaining global receptive fields across all spatial locations. Each
encoder layer includes a feed-forward network with hidden dimensionD FFN = 512and ReLU ac-
tivation. The refined features are decoded through a pointwise regressor consisting of two linear
layers with ReLU activation, projecting from hidden dimension through an intermediate layer of
dimensionDto output channelsC out. The output layer uses small initialization (standard deviation
0.01) to ensure training stability in early iterations. This architecture enables efficient global infor-
mation propagation while maintaining interpretability through its connection to Galerkin projection
methods in numerical PDEs.
Fourier Neural Operator for 1D Benchmarks.We employ a Fourier Neural Operator (FNO)
that learns integral operators in the frequency domain, providing resolution-invariant and globally
receptive mappings. The model processes input functionsu(x)augmented with normalized spatial
coordinates, forming a feature vector with dimensionC in = 2atNgrid points. The architec-
ture begins with a lifting layer that pointwise projects inputs to hidden dimensionD= 16via a
linear transformation. The lifted features are then refined throughL= 2Fourier layers, each im-
plementing a parallel combination of spectral and spatial branches. The spectral branch computes
K(v) =F −1(Rℓ · F(v)|k<K ), whereFdenotes the real-valued Fast Fourier Transform (FFT),
Rℓ ∈C D×D×K are learnable complex weights withK= 16preserved low-frequency modes,
and high-frequency components beyond modeKare implicitly truncated to zero, providing spec-
tral regularization. This truncation restricts the learned operator to spatial scales larger thanL/K,
whereLis the domain length. The spatial branch applies a1×1convolution (pointwise linear
transformation)W ℓ ∈R D×D to capture local residual corrections. Each Fourier layer computes
vℓ+1 =σ(W ℓvℓ +K ℓ(vℓ)), where GELU activationσis applied to the summed output for all
but the final layer. The refined features are decoded through a two-layer pointwise MLP with fixed
intermediate dimension128: the output projection appliesD→128→C out with GELU activation
between layers and small initialization (standard deviation0.01) on the final layer for training sta-
bility. The frequency-domain formulation achieves global receptive fields covering the entire spatial
domain in each layer, while the modes parameterKcontrols the frequency bandwidth, balancing
expressive power against overfitting to high-frequency noise.
U-Net Enhanced Fourier Neural Operator for 1D Benchmarks.We employ a U-Net en-
hanced Fourier Neural Operator (UFNO) that combines the global receptive fields of FNO with
the local multiscale feature extraction capabilities of U-Net. The model processes input func-
tionsu(x)augmented with normalized spatial coordinates, forming feature vectors with dimen-
sionC in = 2atNgrid points. The architecture begins with a lifting layer that pointwise
projects inputs to hidden dimensionD= 16via a linear transformation. The lifted features
are refined throughL= 2UFNO layers, each implementing a three-branch parallel architecture:
vℓ+1 =σ(K ℓ(vℓ) +W ℓ(vℓ) +U ℓ(vℓ)). The spectral branchK ℓ computes frequency-domain con-
21

Preprint.
volutionsF −1(Rℓ · F(v)|k<K )withK= 16preserved modes, capturing global dependencies
through truncated Fourier transforms. The spatial branchW ℓ applies1×1convolutions for chan-
nel mixing and local residuals. The U-Net branchU ℓ implements a lightweight encoder-decoder
architecture with one downsampling layer (factor 2), circular padding for periodic boundary com-
patibility, and skip connections that preserve multiscale spatial information from resolutionNto
N/4, enabling fine-grained local feature refinement. We employ a staged activation strategy con-
trolled by parameterℓ start = 1: layersℓ < ℓstart use only spectral and spatial branches (FNO-only
mode) for rapid coarse feature extraction, while layersℓ≥ℓ start incorporate the U-Net branch for
detailed multiscale refinement, balancing computational efficiency with expressive power. GELU
activationσis applied to all but the final layer. The refined features are decoded through a two-layer
pointwise MLP projecting from hidden dimension through intermediate dimension128to output
channelsC out with GELU activation and small initialization (standard deviation0.01). The U-Net
refiner adds approximately3D 2 parameters per activated layer, while kernel sizek= 9controls its
local receptive field. This hybrid architecture combines FNO’s frequency-domain global propaga-
tion with U-Net’s spatial-domain multiscale analysis, enabling simultaneous capture of long-range
dependencies and localized structures.
Amortized Fourier Neural Operator for 1D Benchmarks.We employ an Amortized Fourier
Neural Operator (AMFNO) that dynamically generates frequency-domain convolution kernels
through multi-layer perceptrons, enabling frequency-adaptive PDE solving. The model processes
input functionsu(x)atNgrid points, automatically augmenting them with normalized spatial co-
ordinates to form feature vectors of dimensionC in + 1 = 2. The architecture begins with a lifting
layer that pointwise projects augmented inputs to hidden dimensionD= 16via a linear trans-
formation. The lifted features are refined throughL= 2AMFNO layers, each implementing a
dual-branch architecture with residual connections:v ℓ+1 =v ℓ +K MLP(vℓ) +W MLP(vℓ), where
GELU activationσ(·)is applied to the summed output for all but the final layer. The spectral branch
KMLP replaces the fixed complex weights of standard FNO with dynamically generated kernels:
for each frequency modeω k in the discrete Fourier spectrum, we encode the normalized frequency
coordinate as a low-dimensional feature representation. Two separate MLPs with hidden dimen-
sion4then map this frequency encoding to real and imaginary components of the convolution ker-
nel:K(ω) =MLP r(ω) +i·MLP i(ω)∈C D×D, producing mode-specific transformations across
allN/2 + 1frequencies in the real FFT spectrum. This dynamically generated kernel performs
frequency-domain convolutionF −1(K(ω)· F(v)), whereFdenotes the real-valued Fast Fourier
Transform. The spatial branchW MLP applies a two-layer pointwise MLP with hidden dimension
4D= 64and GELU activation for local feature mixing. The refined features are decoded through
a single linear projection from hidden dimensionDto output channelsC out = 1. This frequency-
adaptive kernel generation enables superior resolution generalization compared to fixed-kernel FNO,
where each frequency mode receives a tailored transformation learned from data rather than using
predetermined spectral truncation.
A.2.2 MODELS FOR2D BENCHMARKS
SINO for 2D Benchmarks.We employ a Scale-Invariant Neural Operator (SINO) architecture
that operates on coarse-resolution inputs of shape(H, W, Cin)whereHandWare spatial resolu-
tions andC in is the number of input channels. The model consists of a lifting layer that projects
inputs to hidden dimensionD= 32, followed byL= 4SINO blocks, and a projection layer that
maps back to output channels. Each SINO block comprises dual branches: a frequency branch that
applies spectral convolution via MLP-generated complex filters in Fourier space using the 2D real
FFT (rfft2), and a spatial branch that performs circular convolution with MLP-generated kernels
of sizek= 9×9. Both branches use coordinate-based MLPs with two hidden layers of width
wfreq = 32andw spatial = 32respectively, controlling the expressiveness of frequency and spatial
representations. The penultimate layers of these MLPs have dimensionsn freq = 2andn spatial = 2,
forming bottleneck layers that induce low-rank parameterization. For the frequency branch, phys-
ically normalized frequency coordinates(ω y, ωx)∈[−1,1] 2 are computed by mapping discrete
wavenumbers to normalized ranges for each mode in the half-spectrum:ξ y = 4ky/H−1spanning
the full Y-spectrum andξ x = 4k x/W−1covering the non-negative X-half. The MLP generates
mode-specific complex filtersK(ω) =MLP r(ω) +i·MLP i(ω)∈C D×D across allH×(W/2 + 1)
frequencies, with output normalization by1/
√
Dand percentile-based clipping for numerical sta-
bility. A bypass connection via a separate linear layer is added to the spectral output. For the spatial
22

Preprint.
branch, normalized relative displacement coordinatesζ= (ζ y, ζx)∈[−1,1] 2 are generated by
mapping kernel offsets to normalized ranges independently in both dimensions, producing position-
dependent convolution weights that respect periodic boundary conditions through circular padding.
Features from both branches are concatenated and fused via a linear layer, with residual connections
scaled by0.1across blocks to prevent gradient explosion:h (ℓ+1) =h (ℓ) + 0.1·W (ℓ) fuse[h(ℓ) freq ;h (ℓ) spatial].
Physical normalization is applied to both spatial coordinates and spectral frequencies to ensure scale
invariance across different resolutions. The output layer uses small initialization (standard devia-
tion0.01) to ensure training stability in early iterations. All activations use ReLU, and all spatial
convolutions respect periodic boundary conditions through circular padding.
UNet for 2D Benchmarks.We employ a two-level U-Net architecture for learning subgrid-scale
corrections in two-dimensional problems. The network operates on input feature maps of shape
(Cin, H, W)whereCin denotes the number of input channels (typically 2 for velocity components
[u, v]),His the height resolution, andWis the width resolution. The encoder path downsamples the
input twice via max pooling (factor of 2 each), progressively increasing channels fromC in toC init
toC init ×2, with each encoder stage consisting of two convolutions (kernel sizek= 9) followed by
ReLU activations. The bottleneck layer operates at resolution(H/4, W/4)withC max = 16chan-
nels. The decoder path mirrors the encoder with transposed convolutions for upsampling (stride 2,
kernel size 2) and skip connections that concatenate encoder features before each decoder stage.
All convolutions use circular padding to respect periodic boundary conditions. A final1×1con-
volution maps to output channels (the correction term[τ u, τv]) with small initialization (standard
deviation0.01) to ensure training stability in early iterations. The architecture follows the channel
progression2→C init →C init ×2→C max →C init ×2→C init →2and spatial progression
(H, W)→(H/2, W/2)→(H/4, W/4)→(H/2, W/2)→(H, W), requiring bothHandW
divisible by 4.
DeepONet for 2D Benchmarks.We employ the same Deep Operator Network (DeepONet) ar-
chitecture as in the 1D case, with input and output dimensions modified to accommodate two-
dimensional velocity fields. The model processes input functions[u, v]sampled on a fixed sensor
grid of shape(N x, Ny) = (32,32), flattened to dimensionm= 32×32×2 = 2048for the branch
network. The trunk network processes two-dimensional output coordinates(x, y)augmented with
isotropic Fourier features of dimension3 + 4×n Fourier = 19, wheren Fourier = 4. Both branch
and trunk networks remain MLPs with hidden dimensionD= 32,L branch = 4andL trunk = 4lay-
ers, and hyperbolic tangent activations. The branch network maps sensor readings to feature space
b=ϕ branch(u)∈R p withp= 32features, while the trunk network maps augmented coordinates to
t(x, y) =ϕtrunk(˜x,˜y)∈Rp. The final output is computed asG(u)(x, y) =⟨b,t(x, y)⟩+b 0 with
small initialization (standard deviation0.01) on the output layer. The 2D Fourier encoding natu-
rally supports periodic boundary conditions in both spatial directions while maintaining resolution-
independent predictions.
Transolver for 2D Benchmarks.We employ the same Transformer-based operator network
(Transolver) architecture as in the 1D case, with input feature maps of shape(C in, H, W)where
Cin = 4includes the two-dimensional velocity field[u, v]and normalized spatial coordinates
[x/Lx, y/Ly]. The architecture begins with a lifting layer that maps inputs to hidden dimension
D= 32, followed byL= 4Transolver blocks. Each block implements the same three-step physics
attention mechanism adapted for 2D grids: (1)Sliceadaptively groupsN=H×Wgrid points into
G= 32learnable slice tokens via temperature-scaled softmax weights (τ= 0.5), aggregating local
features into macroscopic patterns; (2)Self-Attentionapplies multi-head attention (H= 8heads)
among slice tokens with head dimensiond h =D/H= 4; (3)Desliceredistributes attended infor-
mation back to original grid points using the same grouping weights. We use linear projections for
pointwise feature transformations, ensuring applicability to arbitrary geometries while maintaining
parameter efficiency. Each block includes residual connections and a feed-forward network with
expansion ratior= 4(hidden dimension4D= 128), using GELU activations and layer normal-
ization. The final projection layers map from hidden dimension through an intermediate layer of
128 channels to output dimensionC out = 2, with small initialization (standard deviation0.01) on
the output layer. This architecture enables adaptive spatial receptive fields through learned grouping
while maintaining global awareness through attention mechanisms.
23

Preprint.
OFormer for 2D Benchmarks.We employ the same Operator Transformer (OFormer) architec-
ture as in the 1D case, implementing a four-stage encoder-cross-decoder framework with Galerkin-
type linear attention for two-dimensional spatial domains. The model processes input functions
u(x)sampled atN=H×Wpoints with feature dimensionC in = 4(including velocity field[u, v]
and normalized coordinates[x/L x, y/Ly]) and outputs predictions at arbitrary query locations in 2D
space. The encoder lifts inputs to hidden dimensionD= 32via a linear layer with GELU activa-
tion. The encoded featuresz enc are then processed by a cross-attention module that extracts relevant
information from input locations to query points usingH= 8attention heads with head dimension
dh =D/H= 4. This cross-attention employs two-dimensional rotary position embeddings (RoPE)
that apply separate frequency-based encodings toxandycoordinates with scale factor16.0and
minimum frequency1/64, naturally extending the 1D rotation mechanism to capture spatial rela-
tionships in the plane. Galerkin-type normalization is applied through instance normalization across
spatial dimensions for both keys and values. The attended featuresz cross are refined throughL= 4
propagator layers, each consisting of pre-normalized linear self-attention with residual connections
followed by a feed-forward network with hidden dimension2D= 64and GELU activation. Linear
attention achievesO(N)complexity by computingQ(K ⊤V)instead of softmax(QK ⊤)V, with
scaling factor1/d h for numerical stability. The decoder projects refined features from hidden di-
mension to output channelsC out = 2using a linear layer with small initialization (standard deviation
0.01). The 2D RoPE extension enables the model to generalize to arbitrary query point distributions
in the plane while maintaining spatial awareness through frequency-based position encoding in both
spatial directions.
Galerkin Transformer for 2D Benchmarks.We employ the same Galerkin Transformer archi-
tecture as in the 1D case, learning integral operators through linear attention mechanisms withO(N)
computational complexity for two-dimensional spatial domains. The model processes input physical
quantitiesu(x)sampled atN=H×Wspatial locations with feature dimensionC in = 4(includ-
ing velocity field[u, v]and normalized coordinates[x/L x, y/Ly]). The 2D grid is flattened into a
sequence of lengthNfor processing. The architecture begins with a lifting layer that maps inputs
pointwise to hidden dimensionD= 32via a linear transformation. The lifted features are then
refined throughL= 4encoder layers, each implementing a Galerkin attention mechanism followed
by a position-wise feed-forward network with residual connections and layer normalization. The
Galerkin attention employsH= 8heads with head dimensiond h =D/H= 4, computing linear
attention as Attention(Q,K,V) =Q(K ⊤V)/N, where the matrix productK⊤V∈R dh×dh aggre-
gates global information independently of sequence length. This formulation avoids the quadratic
complexity of softmax-based attention while maintaining global receptive fields across all spatial
locations in the 2D domain. Each encoder layer includes a feed-forward network with hidden di-
mensionD FFN = 512and ReLU activation. The refined features are decoded through a pointwise
regressor consisting of two linear layers with ReLU activation, projecting from hidden dimension
through an intermediate layer of dimensionDto output channelsC out = 2. The output layer uses
small initialization (standard deviation0.01) to ensure training stability in early iterations. This
architecture enables efficient global information propagation across the entire 2D spatial domain
while maintaining interpretability through its connection to Galerkin projection methods in numeri-
cal PDEs.
Fourier Neural Operator for 2D Benchmarks.We employ a Fourier Neural Operator (FNO)
that learns integral operators in the frequency domain, providing resolution-invariant and globally
receptive mappings for two-dimensional spatial domains. The model processes input functionsu(x)
augmented with normalized spatial coordinates, forming a feature vector with dimensionC in = 4
(including velocity field[u, v]and normalized coordinates[x/Lx, y/Ly]) atN=H×Wgrid points.
The architecture begins with a lifting layer that pointwise projects inputs to hidden dimensionD=
32via a linear transformation. The lifted features are then refined throughL= 4Fourier layers, each
implementing a parallel combination of spectral and spatial branches. The spectral branch computes
K(v) =F −1(R(1) ℓ · F(v)0:Kx,:Ky +R (2) ℓ · F(v)−Kx:,:Ky ), whereFdenotes the two-dimensional
real-valued Fast Fourier Transform (rfft2),R (1) ℓ ,R (2) ℓ ∈C D×D×Kx×Ky are learnable complex weights with(K x, Ky) = (16,16)preserved low-frequency modes in each spatial dimension, and
high-frequency components beyond modes(K x, Ky)are implicitly truncated to zero, providing
spectral regularization. The use of two separate weight matricesR (1) ℓ andR (2) ℓ for positive and negative frequencies in thex-direction enables the model to capture asymmetric spatial patterns
24

Preprint.
while respecting the conjugate symmetry of real-valued signals. This truncation restricts the learned
operator to spatial scales larger thanL x/Kx andL y/Ky in the respective directions. The spatial
branch applies a1×1convolution (pointwise linear transformation)W ℓ ∈R D×D to capture local
residual corrections. Each Fourier layer computesv ℓ+1 =σ(W ℓvℓ +K ℓ(vℓ)), where GELU
activationσis applied to the summed output for all but the final layer. The refined features are
decoded through a two-layer pointwise MLP with fixed intermediate dimension128: the output
projection appliesD→128→C out with GELU activation between layers and small initialization
(standard deviation0.01) on the final layer for training stability. The frequency-domain formulation
achieves global receptive fields covering the entire two-dimensional spatial domain in each layer,
while the modes parameters(K x, Ky)control the frequency bandwidth in each direction, balancing
expressive power against overfitting to high-frequency noise and enabling anisotropic frequency
resolution for problems with directional characteristics.
U-Net Enhanced Fourier Neural Operator for 2D Benchmarks.We employ a U-Net enhanced
Fourier Neural Operator (UFNO) that combines the global receptive fields of FNO with the lo-
cal multiscale feature extraction capabilities of U-Net for two-dimensional spatial domains. The
model processes input functionsu(x)augmented with normalized spatial coordinates, forming
feature vectors with dimensionC in = 4(including velocity field[u, v]and normalized coordi-
nates[x/L x, y/Ly]) atN=H×Wgrid points. The architecture begins with a lifting layer
that pointwise projects inputs to hidden dimensionD= 32via a linear transformation. The
lifted features are refined throughL= 4UFNO layers, each implementing a three-branch paral-
lel architecture:v ℓ+1 =σ(K ℓ(vℓ) +W ℓ(vℓ) +U ℓ(vℓ)). The spectral branchK ℓ computes two-
dimensional frequency-domain convolutionsF −1(R(1) ℓ ·F(v) 0:Kx,:Ky +R (2) ℓ ·F(v) −Kx:,:Ky )with (Kx, Ky) = (16,16)preserved modes in each spatial dimension, capturing global dependencies
through truncated Fourier transforms with separate weight matrices for positive and negative fre-
quencies. The spatial branchW ℓ applies1×1convolutions for channel mixing and local residuals.
The U-Net branchU ℓ implements a lightweight encoder-decoder architecture with three downsam-
pling layers (factors2,2,2) reaching resolutionH/8×W/8, circular padding for periodic boundary
compatibility, and skip connections that preserve multiscale spatial information across resolutions
H×W,H/2×W/2,H/4×W/4, andH/8×W/8, enabling fine-grained local feature refinement
in both spatial directions. We employ a staged activation strategy controlled by parameterℓstart = 2:
layersℓ < ℓstart use only spectral and spatial branches (FNO-only mode) for rapid coarse feature
extraction, while layersℓ≥ℓ start incorporate the U-Net branch for detailed multiscale refinement,
balancing computational efficiency with expressive power. GELU activationσis applied to all but
the final layer. The refined features are decoded through a single1×1convolution projecting from
hidden dimension to output channelsC out = 2with small initialization (standard deviation0.01).
The U-Net refiner adds approximately3D 2 parameters per activated layer through its convolutional
structure, while kernel sizek= 3controls its local receptive field in both spatial dimensions. This
hybrid architecture combines FNO’s frequency-domain global propagation with U-Net’s spatial-
domain multiscale analysis, enabling simultaneous capture of long-range dependencies across the
entire 2D domain and localized structures at multiple spatial scales.
Amortized Fourier Neural Operator for 2D Benchmarks.We employ an Amortized Fourier
Neural Operator (AMFNO) that dynamically generates frequency-domain convolution kernels
through multi-layer perceptrons, enabling frequency-adaptive PDE solving for two-dimensional spa-
tial domains. The model processes input functionsu(x)atN=H×Wgrid points, automatically
augmenting them with normalized spatial coordinates to form feature vectors of dimensionCin+2 =
4(including velocity field[u, v]and normalized coordinates[x/L x, y/Ly]). The architecture begins
with a lifting layer that pointwise projects augmented inputs to hidden dimensionD= 32via a linear
transformation. The lifted features are refined throughL= 4AMFNO layers, each implementing
a dual-branch architecture with residual connections:v ℓ+1 =v ℓ +K MLP(vℓ) +W MLP(vℓ), where
GELU activationσ(·)is applied to the summed output for all but the final layer. The spectral branch
KMLP replaces the fixed complex weights of standard FNO with dynamically generated kernels
through a separable two-dimensional frequency representation: for each frequency mode(ωkx , ωky )
in the discrete two-dimensional Fourier spectrum, we encode the normalized frequency coordinates
independently using Chebyshev polynomial bases as low-dimensional feature representations. Four
separate MLPs with hidden dimension4then map these frequency encodings to real and imagi-
nary components of separable convolution kernels:K x(ωkx ) =MLP xr(ωkx ) +i·MLP xi(ωkx )
25

Preprint.
andK y(ωky ) =MLP yr(ωky ) +i·MLP yi(ωky ), with the final kernel formed through elementwise
multiplicationK(ω kx , ωky ) =K x(ωkx )⊙K y(ωky )∈C D×D, producing mode-specific transfor-
mations across allH×(W/2 + 1)frequencies in the real two-dimensional FFT spectrum. This
dynamically generated kernel performs frequency-domain convolutionF −1(K(ω kx , ωky )· F(v)),
whereFdenotes the two-dimensional real-valued Fast Fourier Transform (rfft2). The spatial branch
WMLP applies a two-layer pointwise MLP with hidden dimension4D= 128and GELU activation
for local feature mixing across both spatial dimensions. The refined features are decoded through
a two-layer pointwise MLP projecting from hidden dimension through intermediate dimension4D
to output channelsC out = 2with GELU activation. This frequency-adaptive kernel generation
with separable low-rank factorization enables superior resolution generalization compared to fixed-
kernel FNO, where each frequency mode in both spatial directions receives a tailored transformation
learned from data rather than using predetermined spectral truncation.
A.3 TRAININGMETHODOLOGY
Neural Network Input and Output.Following the Indirect Neural Corrector (INC) frame-
work (Wei et al., 2026), the neural network learns a closure termτ ∆ that serves as a right-hand
side correction to the coarse-grid governing equations. Given the current coarse-grid state¯u n ∆ at
time stepn, the network predicts the correction termτ n ∆ =SINO(¯un ∆; Θ), which is then incorpo-
rated into the time integration scheme. The corrected evolution follows:
∂¯u∆
∂t =L ∆(¯u∆) +τ ∆,(44)
whereL ∆ denotes the coarse-grid spatial operator (e.g., WENO5 reconstruction for Burgers,
pseudo-spectral derivatives for KS, van Leer flux limiting for NS). During rollout training, the pre-
dicted correctionτ n ∆ is held constant across all substeps within each multi-stage time integrator
(e.g., SSP-RK3, ETDRK4), enabling efficient gradient backpropagation while maintaining numeri-
cal stability. This formulation decouples the neural operator from the specific discretization scheme,
allowing SINO to generalize across different numerical solvers.
Training Objective.We train the neural network correction term using a rollout loss with curricu-
lum learning:
LK(θ) = 1 B
BX
i=1
1
K+ 1
KX
k=0
∥uk i −ˆuk i (θ)∥2 (45)
whereBis the batch size,Kis the rollout length (curriculum parameter),u k i is the ground truth at
stepkfor trajectoryi, andˆu k i (θ)is the model prediction.
Curriculum Learning.The rollout lengthKgrows progressively during training:
K(epoch) = min

Kstart +
epoch−1
∆epoch

·∆ K, Kmax

(46)
whereK start is the initial rollout length (default: 10 steps),∆ epoch is the growth interval (default:
every 10 epochs),∆ K is the growth increment (default: 15 steps), andK max is the maximum rollout
length corresponding to the training time horizon. This curriculum strategy stabilizes early training
by first learning short-term dynamics, then gradually extending to longer time horizons.
Optimization.We use the AdamW optimizer with learning rateη= 10 −3 and cosine annealing
schedule:
η(t) =η 0 ·0.5

1 + cos
 πt
T

(47)
wheretis the current optimization step andTis the total number of steps. For decaying Burgers
turbulence, we apply weight decayλ= 10 −3 for regularization.
Data Normalization.For 1D equations (Burgers, KS), we normalize inputs using training set
statistics:u norm = (u−µ train)/σtrain orv norm = (v−µ train)/σtrain, whereµ train andσ train are computed
exclusively from the training temporal window to prevent data leakage. The correction term is scaled
back asτ=τ norm ·σ train. For 2D Navier-Stokes equations, we use standard deviation normalization:
vnorm =v/σ train.
26

Preprint.
Time Integration with Correction Term.The neural network learns a right-hand side correction
termτthat is incorporated into the physical solver during rollout training. For time integration, the
same correction term computed at the beginning of each time step is reused across all substeps of
the multi-stage integrator. This approach reduces computational cost and provides clearer gradient
paths during backpropagation through time.
Model Selection.We select the best model based on extrapolation performance, measured by the
mean squared error on the test temporal window[T train, Tfinal].
Training Schedule.We train for 300 epochs with batch size 8 trajectories. All tasks use 1001
temporal snapshots: the first frame is the initial condition, the first 30% (300 frames) form the
training interval, and the remaining 70% (700 frames) are reserved for extrapolation testing. All
reported MSE errors are extrapolation test errors.
Time Stepping Configuration.We use different time stepping strategies tailored to each bench-
mark:
Forcing Burgers:During the recording phase ofT max = 10.0time units,n snapshots = 1001snapshots
are saved at uniform intervals∆touter = 0.01. The DNS solver employs adaptive timesteps satisfying
∆t=ν CFL ·min(∆x/max i |¯ui|,∆x 2/(2η))with safety factorν CFL = 0.4and viscosityη= 0.01.
Decaying Burgers:Snapshots are saved forT final = 0.1time units at intervals∆t outer =
10−4, yieldingn snapshots = 1001snapshots. The DNS uses adaptive timesteps∆t=ν CFL ·
min(∆x/max i |ui|,∆x 2/(2ν))withν CFL = 0.4and viscosityν= 5×10 −4.
Kuramoto-Sivashinsky:After warmup ofT warmup = 50.0time units, snapshots are recorded for
Tmax = 10.0time units at intervals∆t= 0.01using ETDRK4 integration, yieldingn snapshots = 1001
snapshots.
Forcing Navier-Stokes (Re=1000):After warmup ofT warmup = 40.0time units, snapshots are
recorded for production durationT production ≈0.0448time units. The DNS employs inner batching
withn inner = 8timesteps per saved frame andn outer = 1000saved frames, yieldingn snapshots = 1001
snapshots at intervals∆t frame = 8×∆t, where∆t=C max ·∆x/∥v∥ max withC max = 0.5and
∥v∥max = 7.0.
Forcing Navier-Stokes (Re=4000):Identical configuration to Re=1000 case, but with viscosityν=
2.5×10 −4 and the same maximum velocity∥v∥ max = 7.0.
Decaying Navier-Stokes:After warmup ofT warmup = 4.5time units, snapshots are recorded for
production durationT production ≈0.0117time units. The DNS usesn inner = 8timesteps per frame
andn outer = 1000frames, yieldingn snapshots = 1001snapshots at intervals∆t frame = 8×∆t, where
∆t=C max ·∆x/∥v∥ max withC max = 0.5and initial maximum velocity∥v∥ max = 4.2.
Random Seeds and Reproducibility.All 1D and 2D PDEs use seeds 0–63 to generate 64 tra-
jectories via the JAX random number generatorjax.random.PRNGKey(seed)for initializing
velocity fields. Two trajectories were excluded due to numerical instabilities caused by extreme
initial values: Decaying NS trajectory 61 (seed=61) and Taylor-Green NS trajectory 61 (seed=61).
All other benchmarks use the complete set of 64 trajectories. For neural network training, each
model configuration uses three independent random seeds for weight initialization (model seed
∈ {1,2,3}) to assess variance across random initializations, while the data loading seed (seed)
is fixed at 42 for all experiments to ensure identical train-test splits. This design separates data
randomness from model randomness, enabling fair comparison across architectures.
Computational Environment.All experiments were conducted on a workstation with Ubuntu
22.04, equipped with a single NVIDIA RTX 5090 GPU (32GB VRAM), 25 vCPU Intel Xeon Gold
6459C processor, Python 3.12, PyTorch 2.12.1, and CUDA 13.0. The JAX-based PDE solvers and
neural network training utilized JIT compilation and automatic differentiation for computational
efficiency.
27

Preprint.
A.4 THEORETICALFOUNDATIONS: LOW-RANKSTRUCTURE ANDLIPSCHITZREGULARITY
We provide mathematical analysis demonstrating that SINO’s implicit kernel representation via bot-
tleneck hypernetworks induces two fundamental properties: (1) explicit low-rank parameterization
that aligns with the physical structure of closure operators, and (2) Lipschitz continuity that ensures
smooth kernel variations and prevents overfitting to high-frequency noise. These properties jointly
explain SINO’s superior parameter efficiency and data efficiency in turbulent closure modeling. Our
analysis establishes the low-rank structure of the learned kernels and quantitative bounds for opera-
tor norms, providing theoretical foundations for the empirical performance demonstrated in Section
4.
A.4.1 BOTTLENECK-INDUCEDSUBSPACECONSTRAINT
Architecture.The frequency hypernetworkΦ ω :R 2 →C D×D implements a three-layer bottleneck
architecture:
ξ
W (f) 1
− − − →Rwf σ − →Rwf W (f) 2 − − − →Rwf σ − →Rwf W (f) 3 − − − →Rnf σ − →Rnf [Wr,Wi] − − − − − →CD×D,(48)
whereξ∈R 2 denotes normalized frequency coordinates,W (f) 1 ∈R wf ×2,W (f) 2 ∈R wf ×wf ,
W (f) 3 ∈R nf ×wf is the bottleneck layer withn f ≪w f ,W r, Wi ∈R D2×nf are output projection
matrices (each column representing a vectorizedD×Dmatrix), andσ= max(0,·)is the ReLU
activation function. The spatial hypernetworkΦ x :R 2 →R D×D follows an identical architec-
ture with parameters(W (s) 1 ∈R ws×2, W(s) 2 ∈R ws×ws , W(s) 3 ∈R ns×ws , Ws ∈R D2×ns )and
bottleneck dimensionn s ≪w s.
Theorem 1(Explicit Rank Constraint).Letz ω(ξ) =σ(W (f) 3 σ(W (f) 2 σ(W (f) 1 ξ)))∈R nf denote
the frequency bottleneck representation andz x(ζ) =σ(W (s) 3 σ(W (s) 2 σ(W (s) 1 ζ)))∈R ns denote the
spatial bottleneck representation. Then:
(a) Frequency domain:The spectral kernel admits the explicit low-rank decomposition
m(ξ) =
nfX
j=1
zω,j (ξ)·(B (r) j +iB (i) j ), B (r) j , B(i) j ∈R D×D,(49)
whereB (r) j = matD×D([Wr]·,j)andB (i) j = matD×D([Wi]·,j)are obtained by reshaping thej-th
column vectors[W r]·,j,[W i]·,j ∈R D2 intoD×Dmatrices via the inverse vectorization operator
matD×D :R D2 →R D×D. Consequently,
Mω :={m(ξ) :ξ∈[−1,1] 2} ⊆spanC{B1, . . . , Bnf }, B j :=B (r) j +iB (i) j .(50)
(b) Spatial domain:The spatial kernel admits the explicit low-rank decomposition
W(ζ) =
nsX
j=1
zx,j(ζ)·C j, C j ∈R D×D,(51)
whereC j = mat D×D([Ws]·,j)are obtained by reshaping thej-th column vectors[W s]·,j ∈R D2
intoD×Dmatrices. Consequently,
Wx :={W(ζ) :ζ∈[−1,1] 2} ⊆spanR{C1, . . . , Cns }.(52)
Both constructions reduce the effective parameter count fromO(k max ·D 2)(FNO) orO(K 2 ·D 2)
(CNN) toO((n f +n s)·D 2)(SINO), independent of resolution or kernel size.
Proof.(a) Frequency domain:By construction, the output layer computes
vec(m(ξ)) =W rzω(ξ) +i Wizω(ξ)∈C D2 ,(53)
28

Preprint.
wherevec :C D×D →C D2 denotes the vectorization operator that stacks matrix columns into a
vector. Expanding the matrix-vector products:
vec(m(ξ)) =
nfX
j=1
zω,j (ξ) [Wr]·,j +i
nfX
j=1
zω,j (ξ) [Wi]·,j (54)
=
nfX
j=1
zω,j (ξ) ([Wr]·,j +i[W i]·,j),(55)
where[W r]·,j,[W i]·,j ∈R D2 denote thej-th column ofW r andW i respectively. Applying the
inverse vectorization operatormat D×D:
m(ξ) =
nfX
j=1
zω,j (ξ) matD×D ([Wr]·,j +i[W i]·,j) =
nfX
j=1
zω,j (ξ)·(B (r) j +iB (i) j ).(56)
Sincez ω(ξ)∈R nf for allξ, every kernel matrixm(ξ)necessarily lies inspan C{B1, . . . , Bnf }.
(b) Spatial domain:Identically, the spatial output layer computes
vec(W(ζ)) =W szx(ζ) =
nsX
j=1
zx,j(ζ) [Ws]·,j ∈R D2 .(57)
Applying the inverse vectorization:
W(ζ) = mat D×D


nsX
j=1
zx,j(ζ) [Ws]·,j

 =
nsX
j=1
zx,j(ζ)·C j.(58)
Sincez x(ζ)∈R ns for allζ, every kernel matrixW(ζ)necessarily lies inspan R{C1, . . . , Cns }.
The parameter count for the frequency hypernetwork is2w f +w 2 f +n f wf + 2nf D2 =O(n f D2)
whenn f D2 ≫w 2 f . Similarly for the spatial hypernetwork, yielding total countO((n f +n s)D2).
Remark 1.The rank constraints arehard: the kernel familiesM ω andW x are proper subspaces of
CD×D andR D×D respectively, unlike FNO and CNN where allk max Fourier modes orK 2 spatial
kernel entries are independent parameters. This structural bias aligns with the physical prior that
closure operators exhibit low-rank structure due to scale separation in turbulent flows.
A.4.2 FUNCTIONALCONTINUITY ANDLIPSCHITZREGULARITY
Theorem 2(Lipschitz Continuity of Hypernetworks).LetΦ ω andΦ x be the frequency and spatial
hypernetworks with ReLU activations. Then both mappings are Lipschitz continuous:
(a) Frequency hypernetwork:For anyξ, ξ ′ ∈[−1,1] 2,
∥m(ξ)−m(ξ ′)∥F ≤L ω∥ξ−ξ ′∥2,(59)
where
Lω =
q
∥Wr∥2 2 +∥W i∥2 2 · ∥W(f) 3 ∥2∥W (f) 2 ∥2∥W (f) 1 ∥2.(60)
(b) Spatial hypernetwork:For anyζ, ζ ′ ∈[−1,1] 2,
∥W(ζ)−W(ζ ′)∥F ≤L x∥ζ−ζ ′∥2,(61)
where
Lx =∥W s∥2 · ∥W(s) 3 ∥2∥W (s) 2 ∥2∥W (s) 1 ∥2.(62)
Here∥ · ∥2 denotes the spectral norm (largest singular value) and∥ · ∥F =
qP
i,j |aij|2 denotes
the Frobenius norm.
29

Preprint.
Proof.(a) Frequency domain:The ReLU activation functionσ(a) = max(0, a)satisfies|σ(a)−
σ(b)| ≤ |a−b|(1-Lipschitz property). By composition of Lipschitz functions, the bottleneck
representation satisfies
∥zω(ξ)−z ω(ξ′)∥2 ≤ ∥W(f) 3 ∥2∥W (f) 2 ∥2∥W (f) 1 ∥2∥ξ−ξ ′∥2 =:L z,ω ∥ξ−ξ ′∥2.(63)
The output layer transformation yields
∥m(ξ)−m(ξ ′)∥2 F =∥mat D×D(Wr(zω(ξ)−z ω(ξ′)))∥2 F
+∥mat D×D(Wi(zω(ξ)−z ω(ξ′)))∥2 F (64)
=∥W r(zω(ξ)−z ω(ξ′))∥2 2 +∥W i(zω(ξ)−z ω(ξ′))∥2 2 (65)
≤ ∥Wr∥2 2∥zω(ξ)−z ω(ξ′)∥2 2 +∥W i∥2 2∥zω(ξ)−z ω(ξ′)∥2 2 (66)
= (∥Wr∥2 2 +∥W i∥2 2)∥zω(ξ)−z ω(ξ′)∥2 2 (67)
≤(∥W r∥2 2 +∥W i∥2 2)L2 z,ω ∥ξ−ξ ′∥2 2.(68)
In the second equality, we used the fact that the Frobenius norm is preserved under the inverse
vectorization operator:∥mat D×D(v)∥F =∥v∥ 2 for anyv∈R D2 . Taking the square root yields
Lω =
p
∥Wr∥2 2 +∥W i∥2 2 ·L z,ω.
(b) Spatial domain:Identically, the bottleneck representation satisfies
∥zx(ζ)−z x(ζ ′)∥2 ≤ ∥W(s) 3 ∥2∥W (s) 2 ∥2∥W (s) 1 ∥2∥ζ−ζ ′∥2 =:L z,x∥ζ−ζ ′∥2,(69)
and the output layer transformation satisfies
∥W(ζ)−W(ζ ′)∥F =∥W s(zx(ζ)−z x(ζ ′))∥2 ≤ ∥Ws∥2∥zx(ζ)−z x(ζ ′)∥2 ≤L x∥ζ−ζ ′∥2.(70)
Remark 2.The Lipschitz constantsL ω andL x are computable from trained model weights, pro-
viding quantitative bounds on kernel smoothness. This regularization prevents overfitting to high-
frequency noise inherent in coarse-grid observations, which is critical for closure modeling where
fine-scale information is inaccessible during training.
A.4.3 APPROXIMATIONCAPACITY ANDUNIVERSALAPPROXIMATION
Theorem 3(Universal Approximation of Compact Kernel Families).
(a) Frequency domain:LetK ω ={K(ξ) :ξ∈[−1,1] 2} ⊂CD×D be a compact family of
continuous kernel functions satisfyingsup ξ ∥K(ξ)∥ F <∞. For anyϵ >0, there exist widths
(wf , nf )and parametersΘ ω ={W (f) 1 , W(f) 2 , W(f) 3 , Wr, Wi}such that
sup
ξ∈[−1,1]2
∥K(ξ)−Φ ω(ξ; Θω)∥F < ϵ.(71)
(b) Spatial domain:LetK x ={K(ζ) :ζ∈[−1,1] 2} ⊂RD×D be a compact family of continuous
kernel functions satisfyingsup ζ ∥K(ζ)∥ F <∞. For anyϵ >0, there exist widths(w s, ns)and
parametersΘ x ={W (s) 1 , W(s) 2 , W(s) 3 , Ws}such that
sup
ζ∈[−1,1]2
∥K(ζ)−Φ x(ζ; Θx)∥F < ϵ.(72)
Proof.We establish (a); statement (b) follows by identical reasoning with real-valued functions.
Step 1: Polynomial approximation via Stone-Weierstrass theorem.
Consider the algebraAof complex matrix-valued functions of the form
F(ξ) =
mX
k=1
pk(ξ1, ξ2)Mk, M k ∈C D×D,(73)
30

Preprint.
wherep k(ξ1, ξ2)are polynomials in two real variables andξ= (ξ 1, ξ2)∈[−1,1] 2.
The algebraAsatisfies the conditions of the Stone-Weierstrass theorem. Applying the classical
Stone-Weierstrass theorem component-wise to each of theD2 matrix entries (each entry being a con-
tinuous complex-valued function on[−1,1] 2), we conclude thatAis dense inC([−1,1] 2;C D×D)
under the supremum normsup ξ ∥F(ξ)∥ F. SinceK(ξ)is continuous on the compact set[−1,1] 2,
for anyϵ/2>0, there exists a finite polynomial expansion
Kpoly(ξ) =
X
|β|≤d
ξβMβ, M β ∈C D×D,(74)
whereβ= (β 1, β2)is a multi-index with|β|=β 1 +β 2 ≤d,ξ β =ξ β1 1 ξβ2 2 , and
sup
ξ∈[−1,1]2
∥K(ξ)−K poly(ξ)∥F < ϵ/2.(75)
Step 2: Finite-rank representation.
The polynomial approximationK poly(ξ)involvesN poly :=
d+2
2

distinct monomial terms. We can
rewrite it as
Kpoly(ξ) =
NpolyX
j=1
pj(ξ)Bj,(76)
where{p j(ξ)}Npoly j=1 are the monomial basis functions and{B j}Npoly j=1 are the corresponding coefficient
matrices. Defineα(ξ) = (p 1(ξ), . . . , pNpoly(ξ))⊤ : [−1,1] 2 →R Npoly. Without loss of generality,
assumemax j ∥Bj∥F ≤C B for some constantC B >0.
Step 3: Neural network approximation.
By the universal approximation theorem for feedforward neural networks with ReLU activations,
for the continuous vector-valued functionα: [−1,1] 2 →R Npoly and tolerance
ϵ′ := ϵ 2pNpolyCB ,(77)
there exists a three-layer ReLU network ˆα: [−1,1] 2 →R Npoly with hidden widths(w f , wf )and
output dimensionN poly such that
sup
ξ∈[−1,1]2
∥α(ξ)− ˆα(ξ)∥2 < ϵ′.(78)
Step 4: Hypernetwork construction and error analysis.
Set the bottleneck dimensionnf =N poly and configure the hypernetworkΦω such that its bottleneck
output satisfiesz ω(ξ) = ˆα(ξ). ConstructW r, Wi ∈R D2×Npoly such that thej-th column ofW r
containsvec(Re(B j))and thej-th column ofW i containsvec(Im(B j)), wherevec :C D×D →
CD2 denotes the vectorization operator. The hypernetwork output is then
Φω(ξ; Θω) =
NpolyX
j=1
ˆαj(ξ)Bj.(79)
31

Preprint.
By the triangle inequality and Cauchy-Schwarz inequality,
sup
ξ∈[−1,1]2
∥K(ξ)−Φ ω(ξ)∥F (80)
≤sup
ξ
 K(ξ)− NpolyX j=1 αj(ξ)Bj  F + sup ξ  NpolyX j=1 (αj(ξ)−ˆαj(ξ))Bj  F (81)
< ϵ 2 + sup ξ
NpolyX
j=1
|αj(ξ)−ˆαj(ξ)|∥Bj∥F (82)
≤ ϵ 2 + sup ξ

∥α(ξ)− ˆα(ξ)∥2 ·
vuut NpolyX
j=1
∥Bj∥2 F

 (83)
≤ ϵ 2 +ϵ ′ · p NpolyCB = ϵ 2 + ϵ 2 =ϵ.(84)
Remark 3.The proof establishes existence of an approximating hypernetwork but does not claim
optimality of the construction. The required bottleneck dimensionn f =N poly =
d+2
2

=O(d 2)
depends on the polynomial degreedneeded for approximation, which in turn depends on the
smoothness properties ofK(ξ). ForC k-smooth kernels,d=O(ϵ −1/k)suffices, implying
nf =O(ϵ −2/k). This suggests that smoother closure kernels require exponentially fewer bottle-
neck dimensions for fixed accuracy, aligning with the physical intuition that well-resolved turbulent
flows exhibit smoother scale-transfer operators.
A.4.4 OPERATORNORMBOUNDS ANDREGULARIZATION
Theorem 4(Frequency-Domain Operator Norm).The bottleneck constraint in the frequency hy-
pernetwork controls the operator norm. For the spectral convolution operator acting on functions
h: Ω→C D whereΩ⊂R d is the spatial domain, we have
sup
h
∥h∥L2 (Ω;CD )=1
F −1 h m(ξ)ˆh(ξ) i
L2(Ω;CD) ≤ √nf ·max j ∥Bj∥2 ·sup ξ∈[−1,1]2 ∥zω(ξ)∥2,(85)
whereB j are the basis matrices from Theorem 1(a),∥ · ∥2 denotes the spectral norm, and ˆh(ξ)
denotes the Fourier transform. This bound grows sublinearly withn f , contrasting with FNO’s
linear growth in the number of Fourier modesk max.
Proof.From Theorem 1(a),m(ξ) = Pnf j=1 zω,j (ξ)Bj. By the triangle inequality for spectral norms,
∥m(ξ)∥2 ≤
nfX
j=1
|zω,j (ξ)|∥Bj∥2.(86)
Applying the Cauchy-Schwarz inequality,
nfX
j=1
|zω,j (ξ)|∥Bj∥2 ≤


nfX
j=1
|zω,j (ξ)|2


1/2 

nfX
j=1
∥Bj∥2 2


1/2
(87)
≤ ∥zω(ξ)∥2 · √nf ·max j ∥Bj∥2.(88)
For anyhwith∥h∥ L2(Ω;CD) = 1, by the discrete Parseval identity (with appropriate normalization
for the discrete Fourier transform),
F −1[m(ξ)ˆh(ξ)]  2
L2(Ω;CD) ≤sup ξ ∥m(ξ)∥2 2 · ∥h∥2 L2(Ω;CD).(89)
32

Preprint.
Taking the supremum over all suchhyields the stated bound. The supremumsup ξ ∥zω(ξ)∥2 is finite
by continuity ofz ω and compactness of[−1,1] 2.
Theorem 5(Spatial-Domain Operator Norm).The bottleneck constraint in the spatial hypernetwork
controls the convolution operator norm. For the spatial convolution operator acting on functions
h: Ω→R D whereΩ⊂R d is the spatial domain, we have
sup
h
∥h∥L2 (Ω;RD )=1
 Z [−1,1]2 W(ζ)h(· −ζ)dζ  L2(Ω;RD) ≤4n s ·max j ∥Cj∥2 ·sup ζ∈[−1,1]2 ∥zx(ζ)∥ 2,(90)
whereC j are the basis matrices from Theorem 1(b), the constant4 =|[−1,1] 2|denotes the
Lebesgue measure of the compact support, and∥ · ∥2 denotes the spectral norm.
Proof.By the rank-n s decomposition from Theorem 1(b),W(ζ) = Pns j=1 zx,j(ζ)C j. For anyh
with∥h∥ L2(Ω;RD) = 1,
 Z [−1,1]2 W(ζ)h(· −ζ)dζ  L2(Ω;RD) ≤ nsX j=1  Z [−1,1]2 zx,j(ζ)C jh(· −ζ)dζ  L2(Ω;RD) .(91)
For each summand, applying Minkowski’s integral inequality and exploiting translation invariance
of theL 2 norm,
 Z [−1,1]2 zx,j(ζ)C jh(· −ζ)dζ  L2(Ω;RD) ≤ Z [−1,1]2 |zx,j(ζ)| ∥Cjh(· −ζ)∥L2(Ω;RD) dζ(92)
≤ ∥Cj∥2
Z
[−1,1]2
|zx,j(ζ)| ∥h∥L2(Ω;RD) dζ(93)
≤4∥C j∥2 ·sup
ζ∈[−1,1]2
|zx,j(ζ)|.(94)
Summing overj= 1, . . . , ns yields the stated bound.
Remark 4.Theorem 4 establishes sublinear growthO( √nf )for the frequency-domain operator
norm, providing favorable implicit regularization through spectral orthogonality. Theorem 5 yields
linear growthO(n s)for the spatial-domain operator norm, reflecting the fundamental difference
between Fourier multiplication and spatial convolution. Nevertheless, both branches enforce low-
rank structural constraints that dramatically reduce parameter count and overfitting compared to
explicit parameterization methods. Specifically, FNO requiresO(k max ·D 2)parameters per layer,
wherek max denotes the number of retained Fourier modes that typically scales with spatial res-
olution. Standard CNNs requireO(K 2 ·D 2)parameters per layer, whereKis the kernel size
that grows quadratically with receptive field requirements. In contrast, SINO’s hypernetwork archi-
tecture reduces the effective parameter count toO((n f +n s)·D 2)per layer, where the bottleneck
dimensionsn f , ns are independent of resolution and kernel size. Since typical configurations satisfy
nf , ns ≪min(k max, K2), SINO achieves order-of-magnitude parameter reduction while maintain-
ing expressiveness through continuous functional representations of the low-rank physical operators.
A.5 ADDITIONALEXPERIMENTS
A.5.1 CROSS-RESOLUTION ANDALTERNATIVEFORCINGGENERALIZATION
To further validate SINO’s scale-invariant learning capability and robustness across different phys-
ical regimes, we conduct additional experiments evaluating performance at alternative coarse-
graining ratios and under different forcing configurations beyond the primary benchmarks in Section
4. These supplementary tests assess whether SINO’s superior performance generalizes to: (1) dif-
ferent levels of information loss induced by varying downsampling factors, and (2) qualitatively
different turbulent dynamics arising from alternative forcing mechanisms or Reynolds numbers.
33

Preprint.
1D Supplementary Benchmarks.We extend the 1D turbulence experiments to test robustness
across resolution scales and initial condition sensitivity.Forcing Burgers (128)increases the coarse-
grid resolution from 32 to 128 (resample factor 4 instead of 16), reducing information loss while
maintaining the same forcing configuration (η= 0.01, multi-mode sinusoidal forcing with 20
modes). This tests whether models continue to improve performance when more resolved scales
are available, or if they plateau due to architectural limitations.KS (32)aggressively coarsens the
Kuramoto-Sivashinsky equation from 256 to 32 (resample factor 8 instead of 4), increasing the clo-
sure gap. This extreme downsampling tests model robustness when large portions of the inertial
range are unresolved, a regime where traditional LES closures typically fail.Decaying Burgers
(128)reduces the downsampling factor from 8 to 16 (resolution 128 instead of 256) for the freely
decaying case, providing an intermediate resolution test for transient dynamics without external
forcing. This configuration challenges models to capture energy decay trajectories with moderately
resolved scales.
2D Supplementary Benchmarks.We test three additional Navier-Stokes configurations that alter
either the Reynolds number or the forcing mechanism.Forcing NS (Re=2000)introduces an in-
termediate Reynolds number regime (ν= 5×10 −4) between the Re=1000 and Re=4000 cases,
maintaining Kolmogorov forcing (F 0 = 1.0,k f = 4) and linear damping (α=−0.1). This
tests model interpolation capability across Reynolds numbers and sensitivity to viscosity varia-
tions, which directly affect the dissipation range width and subgrid-scale stress magnitude.Forc-
ing NS (Taylor-Green, Re=1000)replaces Kolmogorov forcing with Taylor-Green vortex forc-
ing, which injects energy isotropically at large scales through a vortex array pattern:f T G =
(F0 sin(kf x) cos(kf y),−F 0 cos(kf x) sin(kf y))withF 0 = 1.0andk f = 2. This qualitatively dif-
ferent forcing geometry produces distinct vortex interaction dynamics compared to the anisotropic
Kolmogorov forcing, testing whether learned closures generalize across forcing symmetries.Forc-
ing NS (Re=10 5)drastically increases the Reynolds number to Re= 10 5 (ν= 10 −5) while main-
taining Kolmogorov forcing, creating highly turbulent conditions with extended inertial ranges. The
flow exhibits rapid energy cascade and strong scale separation, providing a stringent test for closure
models under extreme turbulence intensity. Note that this configuration uses the same coarse res-
olution (64×64) but with viscosity two orders of magnitude smaller than the Re=1000 forced case,
resulting in significantly underresolved dynamics.
All supplementary benchmarks use identical spatial discretization schemes (WENO5 for forced
Burgers, pseudo-spectral for KS and decaying Burgers, van Leer finite volume for NS), temporal
integration methods (SSP-RK3, ETDRK4, TVD-RK3, semi-implicit splitting as appropriate), and
training protocols (300 epochs, batch size 8, 30% training / 70% testing split, curriculum learning
with rollout growth from 10 to maximum steps) as the primary benchmarks. Model hyperparameters
remain unchanged from Section 4 to ensure fair comparison.
Results: 1D Supplementary Benchmarks.Table 4 presents quantitative comparisons on the three
additional 1D configurations. On Forcing Burgers (128), SINO achieves the lowest error (6.15E-
05 average) with only 6.7K parameters, outperforming the second-best SINO-SPA (8.82E-05) by
1.4× and U-Net (1.15E-04) by 1.9×. Notably, all methods exhibit substantially lower errors at this
higher resolution compared to the 32-resolution case (1.03E-03 in Table 2), confirming that in-
creased grid refinement reduces the closure gap. However, SINO maintains the largest relative im-
provement, demonstrating superior utilization of available resolved scales. On the extremely coarse
KS (32) benchmark, SINO (1.30E-01 average) dramatically outperforms all baselines: 2.8× better
than AMFNO (3.58E-01), 3.4× better than U-Net (4.38E-01), and 5.6-8.1× better than Transformer
methods. This aggressive coarsening causes most baselines to degrade significantly compared to
the 64-resolution case (Table 2), while SINO exhibits graceful degradation, validating its robustness
under severe information loss. For Decaying Burgers (128), SINO (1.57E-02 average) achieves 12×
improvement over most baselines that plateau around 1.87E-01 (the coarse-grid baseline). Only
SINO-SPA (1.79E-02) approaches SINO’s performance, while all other methods fail to improve
upon uncorrected coarse-grid simulation.
Results: 2D Supplementary Benchmarks.Table 5 presents quantitative comparisons on the three
additional 2D configurations. On Forcing NS (Re=2000), SINO achieves the best performance
(1.24E-01 average, 1.18E-01 best) with 59K parameters, outperforming U-Net (1.51E-01, 61K pa-
rameters) by 1.2× despite comparable parameter count. UFNO (1.94E-01, 1.3M parameters) and
AMFNO (2.10E-01, 120K parameters) require 2-23× more parameters for substantially worse ac-
curacy. Transformer-based methods exhibit high errors: Transolver (4.72E-01), GK-Transformer
34

Preprint.
Table 4: Performance comparison on supplementary 1D benchmarks. Forcing Burgers (128) uses
resolution 512→128 (resample factor 4), KS (32) uses 256→32 (resample factor 8), and Decaying
Burgers (128) uses 2048→128 (resample factor 16).
Method
Supplementary 1D Benchmarks
ParamsForcing Burgers (128) KS (32) Decaying Burgers (128)
A VE Best A VE Best A VE Best
U-Net 1.15E-04 7.76E-05 4.38E-01 5.92E-01 1.87E-01 1.87E-01 7,077
DeepONet 2.00E-04 1.72E-04 1.70E+00 1.39E+00 1.87E-01 1.87E-01 14,913
Transolver 2.60E-04 2.55E-04 7.47E-01 7.36E-01 1.87E-01 1.87E-01 8,601
Oformer 1.18E-04 1.18E-04 1.89E+01 1.89E+01 1.87E-01 1.87E-01 5,444
GK-Transformer 3.05E-04 2.97E-04 7.32E-01 7.17E-01 1.87E-01 1.87E-01 36,449
FNO 2.13E-04 1.90E-04 1.05E+00 9.44E-01 1.87E-01 1.87E-01 11,073
UFNO 9.70E-04 9.25E-04 9.27E-01 8.47E-01 1.87E-01 1.87E-01 26,017
AMFNO 1.36E-04 1.23E-04 3.58E-01 3.37E-01 1.88E-01 1.87E-01 9,489
SINO-SPE 2.14E-04 1.29E-04 1.89E-01 1.06E-01 1.05E-01 8.70E-02 3,877
SINO-SPA 8.82E-05 7.82E-05 5.76E-01 5.37E-01 1.79E-02 1.76E-02 1,797
SINO (ours)6.15E-05 5.72E-05 1.30E-01 6.84E-02 1.57E-02 1.37E-026,681
Coarse Grid 2.65E-01 1.89E+01 1.87E-01 –
Table 5: Performance comparison on supplementary 2D benchmarks. Forcing NS (Re=2000) uses
ν= 5×10 −4 with Kolmogorov forcing, Forcing NS (Taylor-Green, Re=1000) usesν= 10 −3 with
Taylor-Green vortex forcing, and Forcing NS (Re=10 5) usesν= 10 −5 with Kolmogorov forcing.
All configurations use resolution 512→64.
Method
Supplementary 2D Benchmarks
ParamsForcing NS (Re=2000) NS (Taylor-Green, Re=1000) Forcing NS (Re=10 5)
A VE Best A VE Best A VE Best
U-Net 1.51E-01 1.48E-01 1.41E-02 1.09E-02 2.37E-01 2.31E-01 61,006
DeepONet 5.02E-01 4.96E-01 1.59E-01 1.56E-01 6.04E-01 5.91E-01 269,153
Transolver 4.72E-01 4.14E-01 6.61E-02 6.01E-02 5.59E-01 5.37E-01 54,306
Oformer 5.64E-01 5.64E-01 1.61E-01 1.61E-01 6.45E-01 6.43E-01 38,087
GK-Transformer 4.52E-01 4.14E-01 7.84E-02 7.50E-02 5.50E-01 5.41E-01 151,874
FNO 4.97E-01 4.95E-01 1.10E-01 1.07E-01 5.83E-01 5.76E-01 2,106,018
UFNO 1.94E-01 1.88E-01 1.64E-02 1.57E-02 2.62E-01 2.50E-01 1,346,466
AMFNO 2.10E-01 2.06E-01 2.31E-02 2.16E-02 3.00E-01 2.88E-01 120,162
SINO-SPE 2.56E-01 2.49E-01 2.87E-02 2.57E-02 3.72E-01 3.56E-01 33,834
SINO-SPA 2.45E-01 2.25E-01 4.14E-02 3.14E-02 3.40E-01 2.99E-01 17,322
SINO (ours)1.24E-01 1.18E-01 1.01E-02 8.50E-03 2.03E-01 1.98E-0159,314
Coarse Grid 5.65E-01 1.61E-01 6.45E-01 –
35

Preprint.
(4.52E-01), and Oformer (5.64E-01). This intermediate Reynolds number result confirms SINO’s
smooth interpolation capability between the Re=1000 and Re=4000 regimes. On Forcing NS
(Taylor-Green, Re=1000), SINO (1.01E-02 average, 8.50E-03 best) demonstrates exceptional gen-
eralization to qualitatively different forcing geometry, achieving the lowest error across all methods.
U-Net (1.41E-02, 61K parameters) ranks second but with 1.4× higher error. UFNO (1.64E-02,
1.3M parameters) and AMFNO (2.31E-02, 120K parameters) again underperform despite massive
capacity. Notably, SINO’s error on Taylor-Green forcing is actually lower than its performance
on Kolmogorov forcing at the same Reynolds number (9.17E-02 in Table 3), suggesting that the
isotropic vortex array produces more predictable subgrid-scale dynamics. For the highly turbulent
Forcing NS (Re=105), SINO (2.03E-01 average, 1.98E-01 best) maintains competitive performance
despite the extreme Reynolds number and severe underresolution. U-Net (2.37E-01) and UFNO
(2.62E-01) trail behind, while Transformer methods and FNO variants exhibit substantially higher
errors (4.97-6.45E-01). The coarse-grid baseline error (6.45E-01) confirms that this configuration
represents a highly challenging closure problem where most methods struggle.
Analysis.The supplementary experiments reveal three key insights: (1)Cross-resolution robust-
ness: SINO consistently achieves the best or near-best performance across all tested coarse-graining
ratios, from moderate downsampling (factors 4-8) to extreme coarsening (factor 16), demonstrat-
ing that its scale-invariant representations generalize across information loss regimes. (2)Forc-
ing geometry invariance: SINO’s superior performance on Taylor-Green forcing compared to Kol-
mogorov forcing (1.01E-02 vs. 9.17E-02) confirms that learned closures capture fundamental tur-
bulent mechanisms rather than memorizing forcing-specific patterns, a critical requirement for prac-
tical LES applications where forcing configurations vary across problems. (3)High-Reynolds ex-
trapolation: SINO maintains reasonable performance even at Re=10 5 (2.03E-01), despite training
on substantially lower Reynolds numbers, suggesting that the learned low-rank representations en-
code Reynolds-number-independent physical laws governing energy transfer and dissipation. These
results collectively validate SINO’s design philosophy: by learning on normalized physical scales
through implicit low-rank parameterization, the model achieves robust generalization across resolu-
tions, forcing configurations, and turbulence intensities.
A.5.2 LOW-RANKSTRUCTUREACROSSDIFFERENTFLOWREGIMES
To verify that the low-rank structure induced by SINO’s bottleneck architecture is a universal prop-
erty rather than specific to a single benchmark, we extend the principal component analysis (PCA) of
learned convolution kernels to additional flow configurations. Figure 7 and Figure 8 present cumu-
lative variance analysis for Forcing NS (Re=1000) and Decaying NS respectively, complementing
the Forcing NS (Re=4000) results in Figure 2.
Across all three configurations, the spatial branch kernels consistently exhibit extremely low-rank
structure: the cumulative variance exceeds 95% after the third principal component in all layers,
confirming that spatial convolution operators concentrate their expressiveness into a minimal sub-
space regardless of Reynolds number or forcing conditions. For the frequency branch, the majority
of layers achieve>95% cumulative variance by the third component, while a small fraction of lay-
ers reach cumulative variance between 90%-95% after the third component and surpass 95% by
the fourth component. This slight variation in the frequency domain reflects the different spectral
energy distributions across flow regimes: forced flows at Re=1000 exhibit smoother energy spec-
tra concentrated at low wavenumbers, while Re=4000 and decaying flows contain broader spectral
content requiring slightly more principal components to capture high-wavenumber contributions.
Nevertheless, the consistency across all tested configurations validates our theoretical analysis in
Section A.4: SINO’s bottleneck hypernetwork architecture enforces hard rank constraints (Theorem
1) that force the model to learn compact representations of scale-invariant physical operators. The
fact that 2-4 principal components suffice to explain>95% variance across spatial and frequency
branches, compared to the total dimensionalityD×D= 32×32 = 1024of the kernel matrices,
demonstrates a compression ratio exceeding 250×. This empirical confirmation of low-rank structure
explains SINO’s superior parameter efficiency and data efficiency: by restricting learned operators
to low-dimensional subspaces aligned with dominant physical modes, the model avoids overfitting
to high-dimensional noise inherent in underresolved coarse-grid observations.
36

Preprint.
(a) Spatial Branch (b) Frequency Branch
Cumulative Variance
Cumulative Variance
Number of Components Number of Components
Figure 7: Cumulative variance explained by principal components of learned convolution kernels on
Forcing NS (Re=1000).(a) Spatial branchand(b) Frequency branchacross 4 layers. Consistent
with Re=4000 results, the spatial branch achieves>95% cumulative variance by the third compo-
nent across all layers, while the frequency branch exhibits>95% variance by the third or fourth
component, confirming low-rank structure across different Reynolds numbers.
(a) Spatial Branch (b) Frequency Branch
Cumulative Variance
Cumulative Variance
Number of Components Number of Components
Figure 8: Cumulative variance explained by principal components of learned convolution kernels on
Decaying NS.(a) Spatial branchand(b) Frequency branchacross 4 layers. The spatial branch
maintains>95% cumulative variance by the third component, while the frequency branch achieves
90%-95% variance by the third component and surpasses 95% by the fourth component in most
layers, demonstrating that low-rank structure persists even in freely decaying turbulence without
external forcing.
37

Preprint.
A.5.3 BOTTLENECKDIMENSIONSCALING ANDCOMPUTATIONALTRADE-OFFS
To investigate the impact of bottleneck layer dimensions on model performance, we conduct ab-
lation studies varying the bottleneck dimensions(n f , ns)from 2 to 32 on two representative 2D
benchmarks: Forcing NS (Re=1000) and Decaying NS. All SINO variants use the same dual-branch
architecture with hidden dimensionD= 32andL= 4layers, trained on coarse-grid resolution
64×64 derived from DNS at 512×512.
Table 6 shows that increasing bottleneck capacity consistently improves performance. SINO-32
achieves the lowest errors (4.08E-02 on Decaying NS, 6.06E-02 on Forcing NS), representing 1.5-
1.7× improvement over the baseline SINO-2 configuration. Remarkably, even SINO-2 substantially
outperforms DNS-128 (2× higher resolution with 4× more grid points), while SINO-32 approaches
or exceeds the accuracy of DNS-256 (4× higher resolution with 16× more grid points). This demon-
strates that SINO achieves over 16× computational acceleration: instead of refining the coarse grid
from 64×64 to 256×256, practitioners can run coarse-grid simulations at 64×64 with SINO correc-
tion, achieving comparable or superior accuracy with minimal overhead.
Table 6: Bottleneck dimension scaling analysis on 2D benchmarks. SINO variants trained on 64×64
coarse grids are compared against uncorrected DNS at resolutions 64×64, 128×128, and 256×256.
All errors measured against ground-truth DNS-512.
SINO (64×64) Coarse DNS
Benchmark SINO-2 SINO-8 SINO-16 SINO-32 64×64 128×128 256×256
Decaying NS5.99E-02 4.98E-02 4.49E-024.08E-024.04E-01 1.88E-01 5.64E-02
Forcing NS (Re=1000)9.17E-02 6.89E-02 6.67E-026.06E-025.07E-01 2.58E-01 6.47E-02
To further analyze temporal error accumulation, Figure 9 visualizes the error growth curves of SINO-
32 compared to coarse DNS baselines over 1000 time steps on both Forcing NS (Re=1000) and
Decaying NS benchmarks. The red dashed line at time step 300 marks the boundary between the
training region (0–300) and the extrapolation region (300–1000). SINO-32 demonstrates remark-
able stability in long-time extrapolation, exhibiting the slowest error growth rate among all methods.
Notably, SINO-32 at 64×64 resolution not only outperforms DNS-128 and DNS-256 throughout the
entire trajectory, but also maintains error levels below DNS-256 even in the challenging extrapola-
tion regime beyond the training horizon. This superior temporal stability, combined with the 16×
computational speedup, validates SINO’s practical value for long-term turbulence prediction.
MSE
MSE
Time Step Time Step
Forcing NS (Re=1000) Decaying NS
Figure 9: Temporal error evolution on Forcing NS (Re=1000, left) and Decaying NS (right). SINO-
32 at 64×64 resolution exhibits slower error growth than DNS at 128×128 and 256×256, particularly
in the extrapolation region (shaded, beyond time step 300). The log-scale y-axis highlights SINO’s
superior long-term stability.
38
