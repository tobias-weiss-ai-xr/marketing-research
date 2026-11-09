---
title: Enhancing Quantum Machine Learning with Anyons
url: https://arxiv.org/abs/2606.16090
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Da Zhang
- Wen-Qiang Liu
- Zhaohui Wei
- Zhang-Qi Yin
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.16090
pages: 19
chars: 40098
fetched_at: '2026-11-08T13:28:12+00:00'
kb_version: 1
---

# Enhancing Quantum Machine Learning with Anyons

Enhancing Quantum Machine Learning with Anyons
Da Zhang, 1 Wen-Qiang Liu,2 Zhaohui Wei,3, 4 and Zhang-Qi Yin 1,∗
1Center for Quantum Technology Research and Key Laboratory of
Advanced Optoelectronic Quantum Architecture and Measurements (MOE),
School of Physics, Beijing Institute of Technology, Beijing 100081, China
2Department of Mathematics and Physics,
Shijiazhuang Tiedao University, Shijiazhuang 050043, China
3Yau Mathematical Sciences Center,
Tsinghua University, Beijing 100084, China
4Yanqi Lake Beijing Institute of Mathematical
Sciences and Applications, Beijing 100407, China
Abstract
The power of quantum computing and quantum machine learning relies on harnessing uniquely
quantum phenomena as computational resources. While superposition, coherence and entangle-
ment have been central to this effort, the role of particle exchange statistics remains largely un-
explored. Here, we introduce a quantum kernel framework that unifies bosonic, fermionic, and
anyonic (fractional) exchange statistics within a single learning paradigm. We study this family
of kernels from three perspectives. At the representation level, Haar-averaged effective-dimension
analysis shows that fractional exchange phases access feature-space directions inaccessible to the
purely symmetric or antisymmetric limits. At the level of kernel geometry, the corresponding
Gram matrices show greater separation from the distinguishable-particle baseline and reduced
label-dependent model complexity. Finally, on learning benchmarks, anyonic kernels consistently
outperform their bosonic and fermionic counterparts, with stronger target alignment and more
favorable class geometry. Together, these findings show that exchange statistics reshape the struc-
ture and geometry of quantum feature space, leading to enhanced learning performance. Our
work identifies particle exchange statistics as an overlooked computational ingredient for quantum
machine learning and provides the first systematic comparison of quantum learning models across
exchange phases.
∗ zqyin@bit.edu.cn
1
arXiv:2606.16090v1  [quant-ph]  15 Jun 2026

I. INTRODUCTION
Quantum computation aims to harness fundamental quantum-mechanical principles into
computational power. In recent years, this idea has evolved from a theoretical possibility
into experimental demonstrations, including random-circuit sampling with programmable
superconducting processors, photonic boson sampling, and large-scale simulations of many-
body dynamics [1–6]. These experiments exploit phenomena with no direct classical counter-
part, such as coherent superposition, many-body entanglement and multiphoton interference
among identical particles[7–11]. These developments suggest a broader principle: the intrin-
sic physical properties of quantum systems can be converted into computational resources
when embedded in an appropriate information-processing architecture.
Quantum machine learning provides a natural setting in which to ask whether physical
properties of quantum systems can become useful for data analysis [12, 13]. One established
route is to impose symmetry directly on the learning model. In classical machine learning,
this principle underlies permutation-invariant and group-equivariant architectures [14, 15],
while covariant quantum kernels have shown how group structure in data can be encoded
into quantum feature spaces [16, 17]. These approaches predominantly rely on top-down
mathematical constraints, where symmetries must be artificially engineered into the model
architecture or the embedding map. This contrast reveals a fundamentally distinct and
deeply physical paradigm where the intrinsic properties of the quantum particles themselves
naturally supply the required symmetry structure.
Particle exchange statistics [18, 19] is a natural candidate for such an intrinsic symmetry
structure, yet it remains much less explored as an elementary property of quantum sys-
tems in quantum learning. Exchange statistics specifies how a many-particle wave function
responds when identical particles are exchanged. Bosons and fermions correspond to the
two familiar endpoints, with symmetric and antisymmetric exchange responses. More gen-
eral exchange phases are possible for Abelian anyons in two-dimensional topological matter,
where an exchange can imprint a fractional statistical phase [20–22]. Recent interferomet-
ric experiments in fractional quantum Hall devices have made this exchange phase directly
observable through anyonic interference and braiding signatures [23–26]. This progress mo-
tivates a simple question for quantum learning: Can exchange statistics be turned from a
classification of particles into a design principle for learning machines?
2

Here we address this question using a photonic simulation route, in which entangled
photons and linear optics emulate anyon-like exchange statistics [27–30]. On this basis, we
construct a quantum kernel family that continuously interpolates between bosonic, fermionic
and fractional-statistics exchange responses[31–35]. The resulting framework provides a con-
trolled setting for studying how an intrinsically quantum symmetry structure reshapes the
geometry of a feature map, the complexity of the induced learning model and its predic-
tive performance [36]. Scanning the exchange phase across this kernel family allows us to
track how particle statistics reshapes the data-dependent kernel geometry and the result-
ing learning behaviour. We find that intermediate fractional phases produce advantageous
kernel geometries: the effective dimension is enhanced, the separation from a classical,
distinguishable-particle kernel is increased, and the label-dependent model complexity is
reduced. To demonstrate practical relevance, we benchmark these kernels on standard clas-
sification datasets, MNIST and Fashion-MNIST [37, 38]. Across these tasks, kernels incor-
porating anyonic exchange consistently outperform both bosonic and fermionic limits. These
results identify exchange statistics as a fundamental ingredient that can enhance quantum
machine learning, suggesting that the structure imposed by particle exchange may play a
wider role in quantum information processing and simulation.
II. FRACTIONAL-ST A TISTICS QUANTUM KERNEL
Exchange symmetry is a defining characteristic of quantum systems, providing the under-
lying mechanism that reshapes many-particle interference. In nature, this exchange phase
is restricted to 0 andπfor bosons and fermions. However, more general exchange statistics
can be realized if the amplitude of the many-body system under particle exchange carries
a tunable phase. Although naturally associated with anyonic excitations, these fractional
statistics can be effectively engineered and simulated using photonic platforms [29, 30, 39].
Figure 1a illustrates the two-particle case. The measured correlations arise from two
indistinguishable alternatives: the direct assignment of inputs to outputs, and the exchanged
assignment. For two input modesq i andq j, the initial state coherently superposes these
alternatives with a tunable exchange phase:
|Ψ(2) ϕ ⟩= 1√ 2  ˆa†(1) qi ˆa†(2) qj +e −iϕˆa†(1) qj ˆa†(2) qi  |0⟩.(1)
3

qi
qj
ri
rj
exchanged
b
ϕ
U(x)
Entangled
input
Correlation
detection
a
ϕ=π
ϕ= 0
Bosonic
F ermionic
+
Anyonic
+eiϕ
-
| {z }
0<ϕ<π
U(x i)⊗N
Datax i
U(x j )⊗N
Datax j
...
...
...
...
...
Gram matrix
Kϕ
Linear SVM
N particle entangled input
c
Kernel estimation
(Kϕ)ij =|⟨Φ ϕ(xi)|Φ ϕ(xj )⟩|2
|Ψϕ⟩
|Φϕ(xi)⟩=U(x i)⊗N |Ψϕ⟩
|Φϕ(xj )⟩=U(x j )⊗N |Ψϕ⟩
PCA
|Ψ2 ϕ⟩
FIG. 1.a, Two-particle implementation of the encoded exchange phase. The entangled input con-
tains direct and exchange components, which are mapped byU(x) and read out by label-unresolved
correlation detection, giving the two-path response in equation (2).b, Exchange responses selected
by the encoded phaseϕ. The casesϕ= 0, 0< ϕ < π, andϕ=πcorrespond to bosonic, any-
onic, and fermionic responses, respectively.c,N-particle fractional quantum kernel workflow.
PCA-preprocessed data are encoded into programmable linear-optical unitariesU(x). Acting on
the permutation-entangled input|Ψ ϕ⟩, these unitaries generate fractional-statistics feature states.
Their pairwise overlaps define the kernel Gram matrixK ϕ used by a classical SVM with a precom-
puted quantum kernel.
Here, the superscripts label the internal degrees of freedom of the two photons. After both
components evolve through the same data-dependent linear-optical unitaryU(x), the cor-
relation measurement detects only the output modes, leaving the internal labels unresolved.
The two alternatives therefore interfere coherently.
The corresponding two-mode correlation probability is
P ϕ rirj (x) = 1 2

Uriqi(x)Urj qj (x)| {z }
direct
+e −iϕUriqj (x)Urj qi(x)| {z }
exchanged

 2 .(2)
Intermediate phases 0< ϕ < πproduce anyon-like exchange statistics. This corresponds to
the two-particle Abelian anyon case, in which a single generator ofB 2 contributes a phase
4

eivθ to the exchanged amplitude [40, 41]. Here,θis the statistical exchange angle acquired in
a single elementary exchange, andvcounts the number of such exchanges. The photonicS 2
construction implements the identity and transposition alternatives, weighting the latter by
e−iϕ. In this way, Abelian-anyon–like interference is realized without physical braiding, with
the phase encoded in the entangled input and revealed through label-unresolved correlation
detection.
The two-particle construction above shows how an exchange phase can be programmed
and read out through interference. We now use it to build a quantum kernel in which
fractional exchange statistics is embedded directly into the feature map. As illustrated
in Fig. 1c, we generalize the direct–exchange superposition to anN-particle state defined
over particle-to-mode assignments. For an input spatial configurationq= (q 1, . . . , qN ), we
prepare
|Ψϕ⟩= 1√ N! X σ∈SN e−iϕπ(σ) NY k=1 ˆa†(k) qσ(k) |0⟩.(3)
Here,S N is the permutation group,π(σ) is the inversion number ofσ, and ˆa †(k) q creates
a photon with internal labelkin spatial modeq. The input modes are assumed distinct,
qi ̸=q j fori̸=j. ForN= 2, equation (3) reduces to equation (1). For largerN, the phase
factore −iϕπ(σ) assigns a controllable phase to each permutation according to the number of
adjacent exchanges needed to generate it. Because the measurement does not resolve the
internal labels, these permutation components interfere coherently in the output.
To construct the quantum kernel, classical data pointsxare first compressed via principal
component analysis (PCA) and subsequently encoded into a programmable linear-optical
unitary transformationU(x). Applying this unitary to anN-particle vacuum state yields
the quantum feature state
|Φϕ(x)⟩= 1√ N! X σ∈SN e−iϕπ(σ) NY k=1  X rk Urk,qσ(k) (x)ˆa†(k) rk ! |0⟩.(4)
The overlap between two such feature states evaluates to
⟨Φϕ(xi)|Φϕ(xj)⟩= 1 N! X σ,τ∈S N eiϕ[π(σ)−π(τ)] NY k=1 Mqσ(k) ,qτ(k) (xi,x j),(5)
whereM(x i,x j) =U †(xi)U(x j) represents the relative single-particle unitary. By introduc-
ing the relative permutationα=τ◦σ −1, the double sum reduces to a single-sum interference
5

representation. This rigorously isolates the coherent contributions from distinct permutation
structures, yielding
⟨Φϕ(xi)|Φϕ(xj)⟩= 1 N! X α∈SN C(α, ϕ) NY k=1 Mqk,qα(k)(xi,x j),(6)
with the phase-dependent weight function defined as
C(α, ϕ) =
X
σ∈SN
eiϕ[π(σ)−π(α◦σ)] .(7)
Finally, the generalized particle quantum kernel is defined as the squared fidelity between
the encoded states, formulated as
Kϕ(xi,x j) =|⟨Φ ϕ(xi)|Φϕ(xj)⟩|2 .(8)
Evaluating these entries produces the Gram matrixK ϕ, which serves as a precomputed
kernel for a classical support-vector machine [42, 43]. For a multiclass classification task
with labelsy i ∈ {1, . . . , L}, we use a one-vs-rest multiclass SVM with a precomputed kernel.
The classifier assigns a decision scoref c(x) to each classc, and predicts
ˆy(x) = arg max
c∈{1,...,L}
fc(x).(9)
III. EFFECTIVE DIMENSION FOR QUANTUM KERNEL
The representational capacity of a quantum kernel depends on the Hilbert-space subspace
explored by its encoded states. This accessible space sets a basic, data-independent limit on
what the kernel can represent before any particular learning task is specified. In multiparticle
photonic systems, this space is not arbitrary. It is constrained by exchange statistics [44].
ForNdistinguishable particles inMmodes, the full tensor-product space has dimension
M N . Identical particles explore much smaller symmetry sectors. Bosons are confined to
the symmetric subspace, whose dimension is
M+N−1
N

, whereas fermions are confined to
the antisymmetric subspace, whose dimension is
M
N

. The fractional-statistics feature map
relaxes this binary constraint. By introducing a fractional exchange phase, it allows the
encoded states to move beyond the purely bosonic or fermionic sectors. To isolate the role
of exchange statistics, we use a statistics-only diagnostic based on Haar twirling over the
unitary groupU(M) [45]. To remove dependence on the data distribution and encoding
6

scheme, we replaceU(x) with a Haar-random unitaryU. For a given exchange phaseϕ, the
density matrix averaged by the ensemble is defined as
ρ(ϕ) =E U∼Haar [|Φϕ(U)⟩⟨Φ ϕ(U)|].(10)
Diagonalizingρ(ϕ) gives the spectrump i(ϕ). From this spectrum we compute the von
Neumann entropy
S(ϕ) =−
X
i
pi(ϕ) lnpi(ϕ).(11)
We then define the effective dimension as
Deff(ϕ) = exp[S(ϕ)].(12)
This quantity estimates how many orthogonal directions are effectively accessed by the
fractional-statistics feature map.
The effective dimension forN= 2,3, and 4 particles distributed acrossM= 6 modes is
illustrated in Fig. 2a. The expected boson and fermion limits are faithfully reproduced at the
boundaries. In the fractional statistical region, a pronounced increase inD eff(ϕ) is observed.
This enhancement becomes more pronounced for larger particle numbers, indicating that
fractional phases provide access to regions of the feature space that pure bosons and fermions
cannot reach.
The physical origin of this effective-dimension enhancement can be understood from the
permutation sector structure of the feature state. At the bosonic and fermionic endpoints,
the exchange phase reduces to the trivial and sign characters ofS N . For intermediate ex-
change phases, the phase factor is no longer a single character ofS N , and the feature state
develops support on mixed-symmetry sectors. These sectors obey partial-Pauli occupation
constraints: a sector labeled by the Young diagramλpermits at mostn max =λ 1 particles
in one mode [46]. Fractional exchange phases therefore access several sector-resolved oc-
cupation structures, opening additional feature-space directions. The corresponding central
projector decomposition, sector-resolved entropy contributions, and partial-Pauli bounds are
given in the Supplementary Information section III.
The effective dimension thus provides a data-independent signature of the enlarged rep-
resentational capacity generated by fractional statistics. In the following, we show that a
distinct kernel geometry accompanies this enlarged support and, in turn, improves classifi-
cation performance.
7

0 π/4 π/2 3π/4 π
Exchange phase ϕ
102
103
Effective dimension, Deff
a
0 π/4 π/2 3π/4 π
Exchange phase ϕ
2.5
5.0
7.5
10.0
12.5
15.0
17.5
Geometric difference, gCϕ
b
0 π/4 π/2 3π/4 π
Exchange phase ϕ
0
1
2
3
4
Complexity ratio, Rϕ
c
a : N = 2 N = 3 N = 4 Boson limit Fermion limit b−c : MNIST Fashion−MNIST
FIG. 2.a, Effective dimensionD eff of the fractional-statistics feature map as a function of the
exchange phaseϕfor different particle numbersN. The bosonic and fermionic limits correspond to
ϕ= 0 andϕ=π, respectively, whereas intermediate exchange phases access additional symmetry
sectors and enlarge the effective feature space.b, Label-independent geometric differenceg Cϕ
between the fractional-statistics kernelK ϕ and the distinguishable-photon baselineK C. This
quantity characterizes the maximum geometry-level separation from the classical baseline and
provides an upper bound on the model-complexity reduction thatK ϕ can support.c, Realized
label-dependent model-complexity ratioR ϕ =s C(y)/sϕ(y) for MNIST and Fashion-MNIST. Values
Rϕ >1 indicate that the fractional-statistics kernel reduces the model complexity relative to the
distinguishable-photon baseline for the given labels. Inbandc, solid curves denote the mean over
ten independent runs, and shaded regions indicate one standard deviation.
IV. KERNEL GEOMETR Y INDUCED BY EXCHANGE ST A TISTICS
The effective-dimension analysis shows that fractional exchange phases enlarge the acces-
sible feature space by relaxing symmetry constraints. A larger feature space, however, does
not by itself determine whether a kernel is useful for learning. What also matters is how
data points are arranged within that space. We therefore examine the geometry encoded in
the Gram matrix of the fractional-statistics kernel.
To isolate the role of exchange statistics in shaping this geometry, we establish a baseline
using the distinguishable-photon kernel introduced in Ref. [47]. In the absence of quantum
8

interference, this reference kernel reduces to
KC(xi,x j) =
X
σ∈SN
NY
k=1

Mqk,qσ(k) (xi,x j)

 2 .(13)
We first compareK ϕ with this baseline at the level of kernel geometry alone. For Gram
matrices, the label-independent geometric difference is defined as
gCϕ =
rK 1/2 ϕ K −1 C K 1/2 ϕ  ∞ .(14)
This quantity characterizes the largest possible separation between the two kernels in the
model-complexity framework of Ref. [36]. In this framework, the complexity of representing
a label vectorywith a kernelKis
sK(y) =y T K −1y.(15)
A smaller value ofs K(y) means that the labels are represented more simply in the fea-
ture space induced byK. The geometric difference bounds the corresponding complexity
reduction through
sC(y)≤g 2 Cϕsϕ(y),(16)
and therefore gives a label-independent upper bound on the improvement that the fractional-
statistics kernel can provide relative to the distinguishable-photon baseline.
To determine how much of this geometric potential is realized for a given supervised task,
we further compute the model-complexity ratio
Rϕ = sC(y) sϕ(y) .(17)
HereR ϕ >1 indicates that the fractional-statistics kernel represents the target labels with
lower complexity than the distinguishable-photon kernel. The bound above impliesR ϕ ≤
g2 Cϕ.
Having established the geometric and model-complexity measures defined above, we now
benchmark these quantities on two standard real-data image classification datasets, MNIST
and Fashion-MNIST. A non-monotonic dependence on the exchange phase is observed in
Fig. 2b,c, indicating that the fractional-statistics regime cannot be reduced to a simple
interpolation between the bosonic and fermionic endpoints. Starting from the bosonic limit,
the geometric differenceg Cϕ rises rapidly as soon as a fractional exchange phase is introduced,
9

showing that even a small departure from bosonic symmetry can substantially reshape the
induced feature-space geometry. The maximum is reached at intermediate phases, where
the fractional-statistics kernel is most strongly separated from the distinguishable-photon
baseline.
The model-complexity ratioR ϕ follows the same qualitative trend, with its largest values
also appearing in the intermediate-phase regime. This agreement is important because
gCϕ is independent of the labels, whereasR ϕ depends on the specific classification task.
Their simultaneous enhancement shows that the geometric separation induced by fractional
statistics is not only a formal property of the kernel. Part of this separation is converted
into a lower-complexity representation of the target labels.
V. CLASSIFICA TION WITH FRACTIONAL-ST A TISTICS KERNEL
Having characterized how exchange statistics enlarge the effective feature space and re-
shape the induced kernel geometry, here we ask whether these changes improve the perfor-
mance of quantum kernels on classification tasks. As shown in Fig. 3a,b, the classification
accuracies on both the MNIST and the Fashion-MNIST datasets are plotted forN= 2,3
and 4 particles, with exchange phaseϕ∈[0, π]. For both datasets, it turns out that the
highest accuracies are obtained at intermediate fractional exchange phases.
In addition, Fig. 3a,b also show that increasing the particle number improves the per-
formance of both the bosonic and fractional-statistics kernels. This trend indicates that
many-particle exchange interference can generate increasingly useful feature representations.
However, the fermionic kernel behaves differently. Its performance does not improve with
particle number, and the lowest accuracy is found forN= 4 fermions. This is consistent
with the effective-dimension analysis: the fermionic limit remains strongly constrained by
antisymmetry and therefore accesses a smaller part of the available feature space. The op-
timal performance at intermediate exchange phases points to a favourable balance between
exchange-induced interference and feature-space expressivity.
Meanwhile, we observe that the optimal phase is shifted towards the fermionic side of the
fractional-statistics regime, rather than coinciding with the maxima of the geometry-only
diagnostics discussed above. To understand this shift, we quantify both label alignment
and class separation in the kernel-induced feature space. For a multiclass target matrix
10

0 π/4 π/2 3π/4 π
Exchange phase ϕ
0.82
0.84
0.86
0.88
0.90
0.92
0.94
Accuracy
a MNIST
0 π/4 π/2 3π/4 π
Exchange phase ϕ
0.79
0.80
0.81
0.82
0.83
0.84
Accuracy
b Fashion−MNIST
0 π/4 π/2 3π/4 π
Exchange phase ϕ
0.40
0.42
0.44
0.46
0.48
0.50
Kernel-target alignment
c
0 π/4 π/2 3π/4 π
Exchange phase ϕ
1.20
1.25
1.30
1.35
intra-class distance, dinter
d
MNIST Fashion−MNIST N = 2 N = 3 N = 4
FIG. 3.a, Test accuracy of kernel SVM classifiers on MNIST as a function of the exchange phase
ϕ. Solid, dashed, and dotted curves correspond toN= 2,3 and 4 particles, respectively.b, Test
accuracy on Fashion-MNIST under the same kernel-SVM protocol and particle-number settings.
c, Kernel-target alignment between the fractional-statistics kernelK ϕ and the multiclass target
matrix, shown for the two-particle kernel.d, Mean inter-class distanced inter in the kernel-induced
feature space for the same setting. Blue and red curves denote MNIST and Fashion-MNIST,
respectively. Shaded regions indicate one standard deviation over independent data splits.
Tij =I(y i =y j), whereIis the indicator function, the kernel-target alignment (KTA) is
defined through the Frobenius inner product⟨A, B⟩ F = Tr(AT B) as
KTA(Kϕ, T) =
P
i,j(Kϕ)ijTij qP
i,j(Kϕ)2 ij
qP
i,j T 2 ij
.(18)
We also evaluate the separation between samples using the kernel-induced distance
D(ϕ) ij = q (Kϕ)ii + (Kϕ)jj −2(K ϕ)ij.(19)
The mean inter-class distanced inter is obtained by averagingD (ϕ) ij over all sample pairs be-
longing to different classes,P diff ={(i, j) :i < j, y i ̸=y j}. These quantities measure,
11

respectively, how well the kernel is aligned with the target labels and how strongly different
classes are separated in the induced kernel space [48, 49]. As shown in Fig. 3c,d, both quan-
tities favour an intermediate exchange phase biased towards the fermionic side, matching
the regime in which the highest test accuracy is observed.
Physically, the fermionic endpoint suppresses class separation through Pauli exclusion,
whereas the bosonic endpoint enhances separation through bunching but yields weaker agree-
ment with the target labels. Fractional statistics balance these two limits, preserving sub-
stantial inter-class separation through partial bunching while reshaping the kernel into a
more label-compatible similarity structure through partial exclusion. The concurrent en-
hancement of KTA andd inter therefore suggests that the classification advantage arises from
a fractional-statistics kernel geometry that is both well separated and well aligned with the
learning task. Photon-number-resolved analyses of KTA and class-distance geometry for
N= 2,3 and 4 are provided in the Supplementary Information section IV.
VI. DISCUSSION AND OUTLOOK
In this work, we identify exchange statistics as a structural ingredient for quantum ma-
chine learning. The analysis proceeds from data-independent geometry to supervised learn-
ing performance. Using Haar-random unitary transformations, we first show that fractional
exchange phases enlarge the effective feature space. For real-world datasets, this enlarged
space is accompanied by a distinct kernel geometry. The fractional-statistics kernel dis-
plays the strongest label-independent separation from the distinguishable-photon baseline
and can reduce the model complexity required to represent the observed labels. In classifica-
tion tasks, the same intermediate fractional-statistics regime yields higher test accuracy and
stronger kernel-target alignment on MNIST and Fashion-MNIST. Together, these results
show that geometric diagnostics, evaluated before supervised training, can provide useful
guidance for designing quantum kernels with improved predictive performance.
The fractional-statistics kernels studied here are also compatible with near-term integrated-
photonic platforms. Entangled photon inputs with a tunable relative phase have already
been used to emulate a continuous interpolation between bosonic and fermionic behavior
under linear optical evolution [29], including on programmable silicon photonic proces-
sors [39]. The two-particle regime is therefore directly accessible with existing technology.
12

Extending the approach to larger particle numbers will require multipartite entangled inputs
and mode-matched optical networks, but it does not require physical anyons or real-space
braiding.
The encoding architecture provides another important direction for future work. Here
we used a universal Clements interferometer as a generic photonic encoder. This is experi-
mentally natural, but universality alone does not guarantee that the resulting feature map
is well matched to a given learning problem. More structured encodings, including shallow,
hierarchical, locality-preserving or trainable photonic circuits, may provide stronger induc-
tive biases while retaining exchange-induced interference. More broadly, our results suggest
that exchange structure should be treated as a tunable design variable in quantum machine
learning, alongside system size, circuit architecture and data encoding.
ACKNOWLEDGMENTS
We thank Junkai Dong for helpful discussions. Z.Y. was supported by the Beijing Institute
of Technology Research Fund Program under Grant No. 2024CX01015, National Natural
Science Foundation of China under Grant No. 12441502, and the Fundamental Research
Funds for the Central Universities. W.L. was supported by the National Natural Science
Foundation of China under Grant No. 12505028, and the Science Research Project of Hebei
Education Department under Grant No. QN2025054. Z.W. was supported by National
Natural Science Foundation of China (Grant Nos. 62272259 and 62332009), Beijing Natural
Science Foundation (Grant No. Z220002), and Beijing Science and Technology Planning
Project (Grant No. Z25110100810000).
13

Appendix A: Photonic data encoding and numerical evaluation protocol
Classical data preprocessing and photonic feature encoding
The photonic encoder was implemented as a programmable Clements-type interferome-
ter composed of a sequence of Mach-Zehnder interferometers (MZIs) [50]. Since the original
image data have a much higher dimension than the number of independently tunable pa-
rameters in the interferometer, we first applied PCA to obtain a compact feature vector
x. After PCA, each retained feature component was normalized to the interval [0,1] before
being assigned to the optical parameters. For theℓth MZI acting on modes (m ℓ, nℓ), two
assigned feature components determine the beamsplitter angle and internal phase according
toθ ℓ =πx 2ℓ−1 andφ ℓ = 2πx2ℓ, respectively. The global unitaryU(x) is obtained by cascad-
ing the corresponding MZI transfer matrices according to the chosen interferometer layout,
with an individual MZI represented as
Tm,n(θℓ, φℓ) =

eiφℓ cos(θℓ)−sin(θ ℓ)
eiφℓ sin(θℓ) cos(θ ℓ)

 .(A1)
Numerical simulation setup and evaluation protocol
All numerical experiments were simulated using a linear optical network comprising six
spatial modes. To isolate the effects of exchange statistics in the effective-dimension analysis,
the initial occupation strings were configured according to the total particle number: we
utilized the input state|0,0,1,1,0,0⟩for two particles,|0,0,1,1,1,0⟩for three particles,
and|0,1,1,1,1,0⟩for four particles.
The learning tasks were evaluated under two distinct data configurations. To compute the
geometric-difference and model-complexity ratio, we constructed binary classification tasks
restricted to classes 0 and 3 from both the MNIST and Fashion-MNIST datasets [37, 38].
Each of these random instances comprised 100 class-balanced samples. To assess the full
supervised classification performance — specifically, accuracy, kernel-target alignment, and
inter-class distance — the evaluation was expanded to include all 10 classes from both
datasets. In these multiclass scenarios, the models were trained on 6,000 class-balanced
samples and subsequently evaluated on 1,000 class-balanced test samples. For classifica-
14

tion evaluations, the input occupation strings followed the same particle-number-dependent
configurations used in the effective-dimension analysis.
To ensure robust statistical reliability, ten independent random dataset splits were gen-
erated for every task. All reported graphical curves display the mean values across ten
independent splits, with the corresponding standard deviations to accurately quantify run-
to-run variability.
Appendix B: Scope of the optical fractional-statistics feature map
For two photons, the optical simulation reproduces the exchange-phase-dependent inter-
ference expected for Abelian anyonic exchange at the level of measured correlation probabil-
ities. ForN >2, the construction should be interpreted more narrowly as an anyon-inspired
feature map defined on particle permutations. Unlike physical anyons, which are described
by braid-group representations, our model does not resolve braid histories, exchange orien-
tations, or winding processes that can carry distinct topological information even when they
induce the same final particle permutation. Instead, it retains only the induced element of
the permutation groupS N and assigns an exchange phase through the inversion number
π(σ).
This permutation-level formulation is a simplification of the full braid-group description
of physical anyons. Nevertheless, it retains the feature of fractional statistics most relevant
to the present kernel construction. By reducing the braid structure to permutations, the
model focuses on the role of fractional exchange phases themselves. This simplification also
makes the theoretical analysis more transparent and provides a direct route to a well-defined
quantum kernel. The permutation-level description further implies the phase symmetry
Kϕ =K −ϕ. Thus, although the model does not capture the full topological structure of
physical anyons, it preserves the central exchange-statistical ingredient needed here and
offers a controlled framework for studying how fractional statistics affects quantum-kernel
geometry and learning performance.
[1] F. Arute, K. Arya, R. Babbush, D. Bacon, J. C. Bardin, R. Barends, R. Biswas, S. Boixo, F. G.
Brandao, D. A. Buell,et al., Quantum supremacy using a programmable superconducting
15

processor, Nature574, 505 (2019).
[2] D. Gao, D. Fan, C. Zha,et al., Establishing a new benchmark in quantum computational
advantage with 105-qubit zuchongzhi 3.0 processor, Phys. Rev. Lett.134, 090601 (2025).
[3] C. S. Hamilton, R. Kruse, L. Sansoni, S. Barkhofen, C. Silberhorn, and I. Jex, Gaussian boson
sampling, Phys. Rev. Lett.119, 170501 (2017).
[4] H.-S. Zhong, H. Wang, Y.-H. Deng, M.-C. Chen, L.-C. Peng, Y.-H. Luo, J. Qin, D. Wu,
X. Ding, Y. Hu, P. Hu, X.-Y. Yang, W.-J. Zhang, H. Li, Y. Li, X. Jiang, L. Gan, G. Yang,
L. You, Z. Wang, L. Li, N.-L. Liu, C.-Y. Lu, and J.-W. Pan, Quantum computational advan-
tage using photons, Science370, 1460 (2020).
[5] F. Alam, J. L. Bosse, I. ˇCepait˙ e, A. Chapman, L. Clinton, M. Crichigno, E. Crosson, T. Cubitt,
C. Derby, O. Dowinton,et al., Fermionic dynamics on a trapped-ion quantum computer
beyond exact classical simulation (2025), arXiv:2510.26300 [quant-ph].
[6] F. Alam, J. L. Bosse, I. ˇCepait˙ e, A. Chapman, L. Clinton, M. Crichigno, E. Crosson, T. Cu-
bitt, C. Derby, O. Dowinton,et al., Programmable digital quantum simulation of 2D Fermi–
Hubbard dynamics using 72 superconducting qubits (2025), arXiv:2510.26845 [quant-ph].
[7] T. Theurer, N. Killoran, D. Egloff, and M. B. Plenio, Resource theory of superposition, Phys.
Rev. Lett.119, 230401 (2017).
[8] A. Streltsov, G. Adesso, and M. B. Plenio, Colloquium: Quantum coherence as a resource,
Rev. Mod. Phys.89, 041003 (2017).
[9] R. Jozsa and N. Linden, On the role of entanglement in quantum-computational speed-up,
Proceedings of the Royal Society of London. Series A: Mathematical, Physical and Engineering
Sciences459, 2011 (2003).
[10] Q. Zhao, Y. Zhou, and A. M. Childs, Entanglement accelerates quantum simulation, Nat.
Phys.21, 1338 (2025).
[11] D. Stahlke, Quantum interference as a resource for quantum speedup, Phys. Rev. A90, 022302
(2014).
[12] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost, N. Wiebe, and S. Lloyd, Quantum machine
learning, Nature549, 195 (2017).
[13] M. Cerezo, G. Verdon, H.-Y. Huang, L. Cincio, and P. J. Coles, Challenges and opportunities
in quantum machine learning, Nat. Comput. Sci.2, 567 (2022).
[14] M. Zaheer, S. Kottur, S. Ravanbakhsh, B. Poczos, R. R. Salakhutdinov, and A. Smola, Deep
16

sets, inAdvances in Neural Information Processing Systems, Vol. 30, edited by I. Guyon,
U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vishwanathan, and R. Garnett (Curran
Associates, Inc., 2017).
[15] T. Cohen and M. Welling, Group equivariant convolutional networks, inProceedings of The
33rd International Conference on Machine Learning, Proceedings of Machine Learning Re-
search, Vol. 48, edited by M. F. Balcan and K. Q. Weinberger (PMLR, New York, New York,
USA, 2016) pp. 2990–2999.
[16] J. R. Glick, T. P. Gujarati, A. D. C´ orcoles, Y. Kim, A. Kandala, J. M. Gambetta, and
K. Temme, Covariant quantum kernels for data with group structure, Nat. Phys.20, 479
(2024).
[17] G. Agliardi, G. Cortiana, A. Dekusar, K. Ghosh, N. Mohseni, C. O’Meara, V. Valls, K. Yo-
garaj, and S. Zhuk, Mitigating exponential concentration in covariant quantum kernels for
subspace and real-world data, npj Quantum Information12, 12 (2025).
[18] W. Pauli, The connection between spin and statistics, Phys. Rev.58, 716 (1940).
[19] J. M. Leinaas and J. Myrheim, On the theory of identical particles, Il Nuovo Cimento B37,
1 (1977).
[20] F. Wilczek, Quantum mechanics of fractional-spin particles, Phys. Rev. Lett.49, 957 (1982).
[21] F. Wilczek, Magnetic flux, angular momentum, and statistics, Phys. Rev. Lett.48, 1144
(1982).
[22] F. D. M. Haldane, “fractional statistics” in arbitrary dimensions: A generalization of the pauli
principle, Phys. Rev. Lett.67, 937 (1991).
[23] K. T. Law, D. E. Feldman, and Y. Gefen, Electronic mach–zehnder interferometer as a tool
to probe fractional statistics, Phys. Rev. B74, 045319 (2006).
[24] D. E. Feldman and A. Kitaev, Detecting non-abelian statistics with an electronic mach–
zehnder interferometer, Phys. Rev. Lett.97, 186803 (2006).
[25] H. K. Kundu, S. Biswas, N. Ofek, V. Umansky, and M. Heiblum, Anyonic interference and
braiding phase in a mach-zehnder interferometer, Nat. Phys.19, 515 (2023).
[26] B. Ghosh, M. Labendik, L. Musina, V. Umansky, M. Heiblum, and D. F. Mross, Anyonic
braiding in a chiral mach–zehnder interferometer, Nat. Phys.21, 1392 (2025).
[27] Y. Omar, N. Paunkovi´ c, L. Sheridan, and S. Bose, Quantum walk on a line with two entangled
particles, Phys. Rev. A74, 042304 (2006).
17

[28] P. K. Pathak and G. S. Agarwal, Quantum random walk of two photons in separable and
entangled states, Phys. Rev. A75, 032351 (2007).
[29] J. C. Matthews, K. Poulios, J. D. Meinecke, A. Politi, A. Peruzzo, N. Ismail, K. W¨ orhoff,
M. G. Thompson, and J. L. O’Brien, Observing fermionic statistics with photons in arbitrary
processes, Sci. Rep.3, 1539 (2013).
[30] L. Sansoni, F. Sciarrino, G. Vallone, P. Mataloni, A. Crespi, R. Ramponi, and R. Osellame,
Two-particle bosonic-fermionic quantum walk via integrated photonics, Phys. Rev. Lett.108,
010502 (2012).
[31] M. Schuld and N. Killoran, Quantum machine learning in feature hilbert spaces, Phys. Rev.
Lett.122, 040504 (2019).
[32] V. Havl ´ ıˇ cek, A. D. C´ orcoles, K. Temme, A. W. Harrow, A. Kandala, J. M. Chow, and
J. M. Gambetta, Supervised learning with quantum-enhanced feature spaces, Nature567,
209 (2019).
[33] M. Schuld, Supervised quantum machine learning models are kernel methods (2021),
arXiv:2101.11020 [quant-ph].
[34] Z. Li, X. Liu, N. Xu, and J. Du, Experimental realization of a quantum support vector machine,
Phys. Rev. Lett.114, 140504 (2015).
[35] Y. Liu, S. Arunachalam, and K. Temme, A rigorous and robust quantum speed-up in super-
vised machine learning, Nat. Phys.17, 1013 (2021).
[36] H.-Y. Huang, M. Broughton, M. Mohseni, R. Babbush, S. Boixo, H. Neven, and J. R. McClean,
Power of data in quantum machine learning, Nat. Commun.12, 2631 (2021).
[37] Y. LeCun, L. Bottou, Y. Bengio, and P. Haffner, Gradient-based learning applied to document
recognition, Proceedings of the IEEE86, 2278 (1998).
[38] H. Xiao, K. Rasul, and R. Vollgraf, Fashion-MNIST: a Novel Image Dataset for Benchmarking
Machine Learning Algorithms, arXiv e-prints (2017), arXiv:1708.07747 [cs.LG].
[39] X. Qiang, Y. Wang, S. Xue, R. Ge, L. Chen, Y. Liu, A. Huang, X. Fu, P. Xu, T. Yi, F. Xu,
M. Deng, J. B. Wang, J. D. A. Meinecke, J. C. F. Matthews, X. Cai, X. Yang, and J. Wu,
Implementing graph-theoretic quantum algorithms on a silicon photonic quantum walk pro-
cessor, Science Advances7, eabb8375 (2021).
[40] E. Artin, Theory of braids, Annals of Mathematics48, 101 (1947).
[41] M. Greiter and F. Wilczek, Fractional statistics, Annu. Rev. Condens. Matter Phys.15, 131
18

(2024).
[42] B. E. Boser, I. M. Guyon, and V. N. Vapnik, A training algorithm for optimal margin classi-
fiers, inProceedings of the Fifth Annual Workshop on Computational Learning Theory, COLT
’92 (Association for Computing Machinery, New York, NY, USA, 1992) p. 144–152.
[43] C. Cortes and V. Vapnik, Support-vector networks, Machine learning20, 273 (1995).
[44] A. M. L. Messiah and O. W. Greenberg, Symmetrization postulate and its experimental
foundation, Phys. Rev.136, B248 (1964).
[45] K. G. H. Vollbrecht and R. F. Werner, Entanglement measures under symmetry, Phys. Rev.
A64, 062307 (2001).
[46] M. C. Tichy and K. Mølmer, Extending exchange symmetry beyond bosons and fermions,
Phys. Rev. A96, 022119 (2017).
[47] Z. Yin, I. Agresti, G. de Felice, D. Brown, A. Toumi, C. Pentangelo, S. Piacentini, A. Crespi,
F. Ceccarelli, R. Osellame, B. Coecke, and P. Walther, Experimental quantum-enhanced
kernel-based machine learning on a photonic processor, Nat. Photonics19, 1020 (2025).
[48] N. Cristianini, J. Shawe-Taylor, A. Elisseeff, and J. Kandola, On kernel-target alignment,
inAdvances in Neural Information Processing Systems, Vol. 14, edited by T. Dietterich,
S. Becker, and Z. Ghahramani (MIT Press, 2001).
[49] B. Sch¨ olkopf and A. J. Smola,Learning with Kernels: Support Vector Machines, Regulariza-
tion, Optimization, and Beyond(MIT Press, 2002).
[50] W. R. Clements, P. C. Humphreys, B. J. Metcalf, W. S. Kolthammer, and I. A. Walmsley,
Optimal design for universal multiport interferometers, Optica3, 1460 (2016).
19
