---
title: Quantum kernel methods for marketing analytics with convergence theory and separation bounds
url: https://arxiv.org/abs/2510.11744
category: analytics
subcategory: measurement
date: 2026-01
venue: Scientific Reports
authors:
- Laura Sáez Ortuño
- Santiago Forgas Coll
- Массимилиано Феррара
source: arxiv
pdf_url: https://arxiv.org/pdf/2510.11744
pages: 14
chars: 33928
fetched_at: '2026-11-08T12:57:11+00:00'
kb_version: 1
---

# Quantum kernel methods for marketing analytics with convergence theory and separation bounds

Quantum Kernel Methods: Convergence Theory,
Separation Bounds and Applications to Marketing
Analytics
Laura Sáez Ortuño 1, Santiago Forgas Coll 1, Massimiliano Ferrara 2
1Facultat Economia i Empresa, Universitat de Barcelona, Spain
2Department of Law and Economics, University Mediterranea of Reggio Calabria, Italy
Abstract
This work studies the feasibility of applying quantum kernel methods to a real con-
sumer classification task in the NISQ regime. We present a hybrid pipeline that combines a
quantum-kernel Support Vector Machine (Q-SVM) with a quantum feature extraction mod-
ule (QFE), and benchmark it against classical and quantum baselines in simulation and with
limited shallow-depth hardware runs. With fixed hyperparameters, the proposed Q-SVM
attains 0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83 ROC AUC, ex-
hibiting higher sensitivity while maintaining competitive precision relative to classical SVM.
We interpret these results as an initial indicator and a concrete starting point for NISQ-era
workflows and hardware integration, rather than a definitive benchmark. Methodologically,
our design aligns with recent work that formalizes quantum-classical separations and verifies
resources via XEB-style approaches, motivating shallow yet expressive quantum embeddings
to achieve robust separability despite hardware noise constraints.
Keywords:Quantum Machine Learning; Quantum Kernels; Support Vector Machines; Conver-
gence Theory; Separation Bounds; NISQ Algorithms; Feature Extraction; Classification Theory
1 Introduction
Quantum machine learning (QML) has emerged as one of the most promising near-term appli-
cations of quantum computing, with quantum kernel methods representing a particularly ele-
gant bridge between classical machine learning theory and quantum computational advantages
[17, 8, 18]. The fundamental insight underlying quantum kernels is that quantum circuits can
efficiently compute inner products in exponentially large Hilbert spaces, potentially capturing
data relationships that are intractable for classical methods [12].
This study presents an end-to-end feasibility test of a quantum-enhanced method for su-
pervised classification on a real consumer dataset, evaluated with ROC analysis. We examine
whether shallow, NISQ-compatible quantum embeddings and kernels can improve class separa-
bility and enable threshold-based operation along the ROC curve without retraining. We report
0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83 AUC.
Recent work has demonstrated empirical success of quantum support vector machines (Q-
SVM) in various domains, from particle physics [21] to bioinformatics [19]. However, the the-
oretical foundations explainingwhenandwhyquantum advantage emerges remain incomplete.
While pioneering studies by Schuld and Killoran [17] established the mathematical equivalence
between variational quantum circuits and kernel methods, and Liu et al. [12] proved uncondi-
tional quantum advantage for specifically constructed problems, several fundamental questions
remain open:
1. What are the convergence guarantees for variational quantum kernel optimization?
1
arXiv:2510.11744v1  [quant-ph]  11 Oct 2025

2. Can we rigorously bound the separation advantage of quantum feature extraction?
3. How do circuit depth and approximation methods affect computational complexity?
This paper addresses these questions through three main theoretical contributions and em-
pirical validation on real consumer data.
1.1 Main Contributions
We empirically validate convergence and separation principles on a real consumer classification
case. The Q-SVM achieves 0.83 AUC and 0.8609 recall, with 0.81 F1 and 0.7790 accuracy,
reinforcing the suitability of shallow embeddings under NISQ constraints.
Our work establishes rigorous theoretical foundations for quantum kernel methods with the
following contributions:
Theorem 1 (Convergence of Variational Quantum Kernels):We prove that varia-
tional quantum kernel optimization converges polynomially fast to optimal parameters under
Lipschitz-smooth loss functions and shallow circuit constraints. This provides the first conver-
gence rate guarantee for practical Q-SVM training.
Theorem 2 (Quantum Feature Extraction Separation Bounds):We establish tight
bounds on the margin improvement achievable through quantum feature extraction, showing
that shallow circuits withL≥log 2(d) + 1layers can achieve separation advantages scaling as
Ω(
p
2L/d)over classical kernels in the worst case.
Proposition 1 (Complexity of Approximate QFE):We characterize the computational
complexity of Nyström-approximated quantum feature extraction, proving that landmark sam-
pling withmpoints reduces complexity fromO(N 2 ·4 n)toO(N m 2 +m 3)while maintaining
ϵ-approximation guarantees.
1.2 Marketing Analytics Applications and Business Impact
Our results have direct implications for marketing analytics:
•Recall-first regimes(retention, proactive sales): 0.8609 recall reduces false negatives in
high-value cohorts.
•Precision-first regimes:Operate at higher thresholds while maintaining 0.7647 precision
for cost-sensitive outreach.
•Flexible thresholding:0.83 AUC supports thresholding without retraining, enabling
ROC-guided policy selection across cohorts and time.
1.3 Related Work
Kernel methods in quantum computing build upon decades of classical kernel theory [16]. The
quantumkernelframeworkwasformalizedbySchuldandKilloran[17], whoshowedthatquantum
feature maps induce kernels through state overlap measurements. Havlíček et al. [8] provided
the first experimental demonstration on superconducting hardware, while Liu et al. [12] proved
unconditional quantum advantages for classification via communication complexity arguments.
Recent advances include quantum kernel alignment methods [10, 14], covariant kernels for
structured data [7], and large-scale benchmarking studies [15]. However, most work focuses on
empirical performance or existence proofs of advantage, leaving convergence rates and practical
separation bounds unaddressed.
Our work complements these efforts by providing rigorous convergence theory and construc-
tive separation bounds applicable to NISQ devices. The proofs leverage recent techniques from
variational quantum algorithm optimization [6] and quantum circuit expressivity analysis [5].
2

2 Preliminaries
2.1 Quantum Feature Maps and Kernels
LetX ⊆Rd denote the classical input space. Aquantum feature mapis a mappingϕθ :X → H
to a quantum Hilbert spaceH= (C2)⊗n, typically realized by a parameterized quantum circuit:
ϕθ(x) =U(x, θ)|0⟩⊗n,(1)
whereU(x, θ)is a unitary operator encoding dataxand variational parametersθ∈Θ⊆R p.
The inducedquantum kernelis defined as:
kθ(xi, xj) =|⟨ϕ θ(xi)|ϕθ(xj)⟩|2.(2)
For a training datasetD={(x i, yi)}N i=1 withy i ∈ {−1,+1}, the Q-SVM optimization prob-
lem is:
min
α
1
2
NX
i,j=1
αiαjyiyjkθ(xi, xj)−
NX
i=1
αi,(3)
subject to PN i=1 αiyi = 0and0≤α i ≤C.
2.2 Circuit Ansatz
We employ a data re-uploading ansatz with alternating data encoding and parameterized rota-
tions:
U(x, θ) =
LY
ℓ=1
Uent Urot(θℓ)Uenc(x),(4)
where:
•U enc(x) = Nn i=1 RY (xi)encodes data with per-feature RY rotations,
•U rot(θℓ) = Nn i=1 RY (θℓ,i)RZ(θ′ ℓ,i)applies parameterized single-qubit rotations,
•U ent implements sparse nearest-neighbor controlled-Z entangling gates.
This ansatz hasp= 2nLparameters and effective depth≈2, making it NISQ-compatible.
The kernel is computed via state overlapsk(x, x′) =|⟨ϕ(x)|ϕ(x ′)⟩|2 in high-fidelity simulation.
For quantum feature extraction (QFE), Pauli-Z expectations are measured across multiple
re-uploading slices to form an explicit feature vector with dimensionalitydQFE = 128, selected
via cross-validation.
3 Main Theoretical Results
3.1 Convergence of Variational Quantum Kernels
Our first main result establishes polynomial convergence rates for variational quantum kernel
optimization.
Theorem3.1(ConvergenceofVariationalQuantumKernels).Consider the variational quantum
kernel optimization problem:
min
θ∈Θ
L(θ) = min
θ
LSVM(kθ) +λR(θ),(5)
whereL SVM(kθ)is the SVM hinge loss with quantum kernelk θ, andR(θ)is anℓ 2 regularizer
with strengthλ >0.
Assume:
3

1. The lossLisβ-smooth:∥∇L(θ)− ∇L(θ ′)∥ ≤β∥θ−θ ′∥.
2. The circuit depth satisfiesL≤L max whereL max =O(logn).
3. Gradients are estimated via parameter-shift rules with sample varianceσ2.
Then gradient descent with learning rateη≤1/βachieves:
E[L(θT )]− L(θ∗)≤ ∥θ0 −θ ∗∥2 2ηT +ησ 2,(6)
whereθ ∗ is the global minimum. Forη= Θ(1/ √ T), this yieldsO(1/ √ T)convergence.
Proof.We establish convergence through four key steps:
Step 1: Smoothness of Quantum Kernels.The quantum kernelk θ(xi, xj)is twice
differentiable with respect toθ. For shallow circuits withL=O(logn)layers, the partial
derivative satisfies:

 ∂kθ ∂θℓ

 =

 ∂ ∂θℓ |⟨ϕθ(xi)|ϕθ(xj)⟩|2

 ≤2,(7)
by the parameter-shift rule. The second derivative is bounded as:

 ∂2kθ ∂θ 2 ℓ

 ≤4.(8)
SinceL SVM is a convex combination of kernel values through the dual variablesαi, and the
regularizerR(θ) = λ 2 ∥θ∥2 is smooth, the composite loss inherits smoothness with constant:
β≤4N C 2 +λ,(9)
whereCis the SVM regularization parameter andNis the sample size.
Step 2: Descent Lemma.Forβ-smooth functions, gradient descent with step sizeη≤1/β
satisfies:
L(θt+1)≤ L(θt)− η 2 ∥∇L(θt)∥2.(10)
Summing overTiterations:
T−1X
t=0
∥∇L(θt)∥2 ≤ 2 η [L(θ0)− L(θT )].(11)
Step 3: Convexity in Kernel Space.AlthoughL(θ)is non-convex in the parameter space
Θ, the SVM objective is convex in the kernel matrixK= [kθ(xi, xj)]. For shallow circuits, the
kernel landscape has no barren plateaus due to bounded gradients [6]. This ensures:
∥∇L(θ)∥2 ≥µ(L(θ)− L(θ∗)),(12)
for someµ >0related to the Polyak-Łojasiewicz condition.
Step 4: Stochastic Gradient Noise.In practice, gradients are estimated via finite-shot
quantum measurements. Letg t =∇L(θ t) +ϵ t denote the noisy gradient withE[ϵ t] = 0and
E[∥ϵt∥2]≤σ 2. The expected update satisfies:
E[L(θt+1)]≤E[L(θ t)]− η 2 E[∥∇L(θt)∥2] + η2βσ 2 2 .(13)
Telescoping and choosingη= Θ(1/
√
T)yields:
E[L(θT )]− L(θ∗) =O
 1√
T

.(14)
This completes the proof.
4

Remark 3.2.Theorem 3.1 provides the first polynomial convergence guarantee for practical Q-
SVM training. TheO(1/
√
T)rate matches classical non-convex optimization but applies specifi-
cally to quantum kernel landscapes with shallow circuits, avoiding barren plateau issues. In our
binary consumer setting, the stable optimizer and shallow architecture align with smoothness and
non-plateau assumptions; the observed 0.83 AUC and 0.8609 recall are consistent with improved
separation and the 0.81 F1.
3.2 Quantum Feature Extraction Separation Bounds
Our second main result establishes tight bounds on the margin improvement achievable through
quantum feature extraction.
Theorem 3.3(Quantum Feature Extraction Separation Bounds).LetD={(x i, yi)}N i=1 be a
binary classification dataset that is not linearly separable inRd with maximum classical margin
γclassical. Consider a quantum feature mapϕ:R d → Hwithdim(H) = 2 n implemented by a
circuit of depthL≥log 2(d) + 1with non-commuting layers.
Then there exists a quantum kernelkq such that the quantum margin satisfies:
γquantum ≥γ classical ·
s
2L
d·poly(logd) ,(15)
wherepoly(logd)accounts for encoding overhead.
Moreover, this bound is tight up to logarithmic factors for the worst-case dataset geometry.
Proof.We establish the separation bound through geometric and information-theoretic argu-
ments.
Step 1: Quantum Embedding Dimensionality.A quantum circuit withnqubits and
Llayers embeds classical data into a subspace ofH= (C2)⊗n with effective dimension:
deff = min(2nL/2,2 n),(16)
due to the parameterization and entangling structure. ForL≥log2(d), we havedeff ≥d.
Step 2: Classical Margin Limitation.In classical SVM with RBF or polynomial kernels,
the data is implicitly embedded in a reproducing kernel Hilbert space (RKHS)Hclassical with
dimensiond RKHS =O(d k)for degree-kpolynomials ord RKHS =∞for RBF. However, the
effectivedimension for finite samples is:
dclassical eff ≤N≪2 n,(17)
since the kernel matrix has rank at mostN.
The classical margin scales as:
γclassical = Θ

 1q
dclassical eff

 = Θ
 1√
N

,(18)
under standard assumptions on data distribution.
Step 3: Quantum Margin Amplification.The quantum embeddingϕ(x) =U(x, θ)|0⟩
distributes the classical features across2n complex amplitudes. For a depth-Lcircuit with data
re-uploading:
ϕ(x) =
 LY
ℓ=1
Uent Urot(θℓ)Uenc(x)
!
|0⟩.(19)
5

Each layer contributes a factor of
√
2to the effective dimensionality expansion. The quantum
state amplitudes encode the data as:
ϕ(x) =
X
z∈{0,1}n
αz(x, θ)|z⟩,(20)
where the coefficientsαz depend on the product of rotation angles across layers.
The distance between quantum states for opposite classes is:
dq(xi, xj) =∥ϕ(x i)−ϕ(x j)∥2 (21)
= 2(1−Re[⟨ϕ(x i)|ϕ(xj)⟩])(22)
≥2(1− |⟨ϕ(xi)|ϕ(xj)⟩|).(23)
For well-separated classes in the quantum Hilbert space:
|⟨ϕ(xi)|ϕ(xj)⟩| ≤exp

− ∥xi −x j∥2
2σ2 ·2 L

,(24)
whereσis the encoding bandwidth. This exponential decay implies:
dq(xi, xj)≥2

1−exp

− ∥xi −x j∥2 ·2 L
2σ2

.(25)
Step 4: Margin Bound.The quantum margin is defined as:
γquantum = min i:yi=+1,j:yj =−1 dq(ϕ(xi), ϕ(xj)).(26)
By the Johnson-Lindenstrauss lemma applied to quantum embeddings [8], the margin im-
provement scales with the square root of the dimension ratio:
γquantum ≥γ classical ·
s
2nL/2
dclassical eff .(27)
For shallow circuits withL=O(logd)andn=d, this simplifies to:
γquantum ≥γ classical ·
s
2L
d·poly(logd) ,(28)
where the polynomial factor accounts for encoding fidelity and measurement overhead.
Step 5: Tightness.To show tightness, consider a dataset where classical and quantum
kernels both achieve their respective VC dimensions. The classical VC dimension isO(d), while
the quantum VC dimension isO(2n)[12]. The margin scales inversely with √ VC-dim, yielding
the stated bound up to logarithmic factors.
Remark 3.4.Theorem 3.3 formalizes why shallow quantum circuits can provide separation ad-
vantages even on NISQ devices. The
p
2L/dscaling explains empirical observations that modest
circuit depths (L= 3–5) suffice for many practical problems. In our binary consumer case, the
shallow, expressive embedding is consistent with the improved separability observed (AUC 0.83,
recall 0.8609), aligning with the theorem’s intuition for NISQ-depth circuits.
6

3.3 Complexity of Approximate Quantum Feature Extraction
Our final theoretical result addresses the computational complexity of approximate QFE meth-
ods.
Proposition 3.5(Complexity of Nyström-Approximated QFE).LetNbe the dataset size and
nthe number of qubits. Define the Quantum Feature Extraction (QFE) kernel matrix:
Kij =⟨ϕ(x i)|Ok|ϕ(xj)⟩,(29)
for observables{O k}4n k=1.
Exact QFE requiresO(N2 ·4 n)quantum measurements. The Nyström approximation withm
landmark points andm′ selected observables achieves anϵ-approximate kernel:
∥K− ˜K∥F ≤ϵ,(30)
usingO(N m·m ′ +m 2m′)quantum measurements andO(N m2 +m 3)classical post-processing.
Form=O(
√
N)andm ′ =O(poly(n))selected via Fisher information maximization, this
yields anϵ-approximation withϵ=O(1/
√
N).
Proof.ExactQFEComplexity.ComputingthefullQFEkernelrequiresevaluating⟨ϕ(x i)|Ok|ϕ(xj)⟩
for alli, j∈[N]and all Pauli observablesk∈[4 n]. Each measurement requires preparing|ϕ(xi)⟩,
evolving under|ϕ(x j)⟩†, and measuringOk. With shot noiseσ2 shot =O(1/S)forSshots, achiev-
ing accuracyϵrequires:
S=O
 1
ϵ2

shots per matrix entry. (31)
Total complexity:O(N 2 ·4 n/ϵ2)quantum measurements.
Nyström Approximation.Selectmlandmark points{x i1, . . . , xim}uniformly or via lever-
age score sampling. Compute the submatrix:
C=K[:,[i 1, . . . , im]]∈R N×m·m ′ ,(32)
and
W=K[[i 1, . . . , im],[i 1, . . . , im]]∈R m·m′×m·m′ .(33)
The Nyström approximation is:
˜K=CW †CT ,(34)
whereW † is the Moore-Penrose pseudoinverse.
Measurement Complexity.ComputingCrequiresO(N m·m ′)quantum evaluations.
ComputingWrequiresO(m 2m′)evaluations. Classical reconstruction via ˜K=CW †CT requires
O(N m2 +m 3)operations for pseudoinverse and matrix products.
Approximation Error.By the Nyström approximation theory [20], the Frobenius norm
error is bounded as:
∥K− ˜K∥2 F ≤ ∥K−Km∥2 F + ∥K∥2 F m ,(35)
whereK m is the best rank-mapproximation. For kernels with polynomial eigenvalue decay:
λk =O(k −α), α >1,(36)
we have:
∥K−K m∥2 F =O(m 1−α).(37)
Form=O(
√
N)andα= 2(typical for smooth kernels), this yieldsϵ=O(1/
√
N).
7

Observable Selection.Instead of all4 n Pauli observables, selectm′ =O(n 2)observables
via Fisher information:
I(O k) =
X
i,j

 ∂Kij ∂⟨Ok⟩

 2 ,(38)
and keep the top-m′ observables. This reduces the observable dimension from exponential to
polynomial while preserving kernel expressivity [9].
Remark 3.6.Proposition 3.5 shows that QFE can be made practical for NISQ devices through
landmark sampling and observable selection, reducing complexity from exponential to polynomial
in most relevant quantities. Theϵ=O(1/
√
N)approximation is sufficient for classification tasks
where decision boundaries are robust to small kernel perturbations. Linking to the consumer re-
sults, QFE provides a practical path to enhance separability under NISQ constraints, with scalable
approximations mitigating measurement and processing costs.
4 Methodology
4.1 Task, Data, and Metrics
We consider a binary classification problem on individual-level consumer records and prioritize
receiver operating characteristic (ROC) analysis to accommodate recall-first and precision-first
operating regimes. Quantum embeddings are instantiated via a shallow, hardware-aware feature
map tailored to the NISQ setting [13].
Specifically, we employ a data-reuploading, single-axis rotation architecture: each input vec-
torx∈R d0 is linearly mapped to anglesθi; ad-qubit register is initialized with Hadamard gates,
followed by element-wiseRY (θi)rotations and a sparse nearest-neighbor CZ entangling pattern,
yielding an overall circuit depth of 2.
For kernel-based learning, state overlapsK(x,x′) =|⟨ϕ(x)|ϕ(x ′)⟩|2 are computed by simula-
tion to construct a positive-definite quantum kernel used by a classical SVM. For the quantum
feature extraction (QFE) variant, Pauli-Z expectation values are measured from the same circuit
across multiple reuploading slices and concatenated into an explicit feature representation; after
slice aggregation and polynomial cross-terms, the resulting feature dimensionality isdQFE = 128,
chosen via nested cross-validation to balance separability and computational cost.
Data preprocessing follows standard procedures for mixed-type consumer features, with cate-
gorical variables encoded and numeric variables standardized. Model development uses stratified
70/15/15 train/validation/test splits, with the test set held out for final assessment. Hyperpa-
rameters for the SVM (C), classical RBF baselines (kernel bandwidth), and quantum circuits
(depth) are selected via nested cross-validation on the training partition.
Evaluation metrics include accuracy, precision, recall, F1, and ROC AUC, reported with
per-class statistics and macro/weighted aggregates. Post hoc ROC analysis is applied to deter-
mine decision thresholds aligned with recall-first or precision-first policies, enabling sensitivity-
specificity adjustments without retraining. Emphasis on ROC AUC provides a distribution-level
criterionsupportiveofverifiabilitywithoutintractablereconstruction, consistentwithpopulation-
mean benchmarking practices in quantum sampling validations [3, 2].
4.2 Model Suite
The classical baseline models comprise support vector machines (SVMs) with linear, radial basis
function (RBF), and polynomial kernels trained on standardized inputs. Quantum baselines in-
clude simulated quantum kernels that mirror linear, RBF-like, and polynomial-like constructions,
as well as executions on superconducting hardware with up to five qubits and shallow circuit
depths.
8

Stage 1
Data Loading &
Preparation
Min-max to [0,1]
Cat. encoding
y∈ {−1,+1}
Stage 2
Circuit Ex-
ecution &
Q Feature Extr.
H + RY(θ)
Batched exec
Measurement
Stage 3
Decoding, SVM
Train & Eval
Linear SVM
Acc, Prec, Rec, F1
ROC analysis
Input dataset Quantum features Performance
Figure 1: End-to-end workflow for quantum-enhanced classification.
The proposed quantum SVM (Q-SVM) employs a shallow variational feature map that in-
duces a positive-definite quantum kernel via simulated state overlaps; the downstream SVM
is trained classically with hinge loss andL 2 regularization. The quantum feature extraction
(QFE) module applies a parameterized circuit whose amplitudes and measurement outcomes are
mapped into an expanded interaction-feature space that serves as input to a classical SVM. Given
itsO(n 2)scaling, QFE is evaluated in simulation with batching and approximation strategies.
The emphasis on shallow circuits follows hardware-aware design principles analogous to those
enabling high-fidelity Clifford layers in experimental separations, where measurement templates
with classical control reduce depth while preserving the relevant observables [11].
4.3 Training, Evaluation, and Infrastructure
Hyperparameters are tuned on the training set via nested cross-validation, adjusting regulariza-
tion strength, kernel parameters, and circuit depth. The default decision threshold is 0.5, after
which operating points are moved along the ROC curve to meet recall-first or precision-first
objectives. Class imbalance is handled through stratified sampling and per-class reporting.
Simulated models are executed on high-fidelity backends, while hardware baselines employ
shallow circuits and limited shot counts with batched submissions to minimize latency. Su-
percomputing resources coordinate parameter sweeps, kernel estimation, and post-processing;
related variational routines are GPU-accelerated, whereas the primary classification experiments
rely on CPU-accelerated simulators and classical SVM solvers. This simulator-first approach fol-
lows device-level guidance: train parameterized ansätze against realistic gate- and memory-error
models before conducting limited hardware runs to maintain fidelity targets [11].
Figure 1 summarizes the end-to-end workflow for quantum-enhanced classification.
5 Experimental Validation
5.1 Dataset and Experimental Setup
•Real consumer dataset; binary classification with mixed numerical and categorical features.
•Splits: stratified 70/15/15 for train/validation/test.
•Preprocessing: standardize numerical features; encode categorical features; min-max scale
encoded angles to[0, π].
•Q-SVM: kernel via simulated state overlaps from the shallow embedding.
•QFE:d QFE = 128via re-uploading slices and Pauli-Z expectations.
•Decision policy: default threshold 0.5 with ROC analysis to support threshold selection
without retraining.
9

5.2 Results
The Q-SVM achieves an accuracy of 0.7790, precision 0.7647, recall 0.8609, F1 0.8100, and ROC
AUC 0.83. The negative class reaches 0.8019 precision, 0.6800 recall, and 0.7359 F1 with support
125; the positive class reaches 0.7647 precision, 0.8609 recall, and 0.8100 F1 with support 151.
Macro averages are 0.7833 precision, 0.7705 recall, and 0.7729 F1; weighted averages are 0.7815
precision, 0.7790 recall, and 0.7764 F1.
Table 1: Q-SVM headline metrics on test set.
Quantum SVM Metrics Value
Test Accuracy 0.7790
Test Precision 0.7647
Test Recall 0.8609
Test F1 0.8100
ROC AUC 0.83
Table 2: Q-SVM classification report.
Class Precision Recall F1-score Support
0.0 0.8019 0.6800 0.7359 125
1.0 0.7647 0.8609 0.8100 151
accuracy 0.7790 276
macro avg 0.7833 0.7705 0.7729 276
weighted avg 0.7815 0.7790 0.7764 276
5.3 ROC Analysis and Operating Points
The ROC AUC of 0.83 indicates robust separability across thresholds and enables policy-driven
operation without retraining. Lowering the threshold supports recall-first regimes where the
value at risk is high and outreach costs are acceptable. Raising the threshold supports precision-
first regimes where capacity, regulation, or customer experience concerns dominate. In line with
verification practices used in supremacy-style work, operating points are chosen on the basis of
averaged outcomes rather than worst cases, improving statistical power and governance [1, 11].
5.4 Comparison with Classical and Quantum Baselines
Classical SVMs are competitive in accuracy but underperform in recall and F1 relative to Q-
SVM. Quantum kernels on real hardware trail simulated counterparts due to depth constraints
and noise. The proposed Q-SVM consistently delivers the best recall, strong precision, and
leading F1, with accuracy above most alternatives [11].
5.5 Quantum Feature Extraction
QFE improves validation margins and qualitative separability; practical scaling via batching,
Nyström, and sparse selection.
6 Discussion
Convergence guarantees and separation bounds are consistent with the observed binary results:
0.83 AUC and 0.8609 recall, particularly valuable in recall-first regimes. QFE indicates potential
10

0 0.2 0.4 0.6 0.8 10
0.2
0.4
0.6
0.8
1
False Positive Rate
True Positive Rate
ROC Curve (AUC = 0.83)
No skill
Q-SVM
Figure 2: ROC curve for Q-SVM with no skill diagonal.
additional gains under scalable approximations. These findings support NISQ-era workflows
emphasizing shallow yet expressive embeddings and ROC-guided thresholding.
6.1 Implications of Theoretical Results
Our convergence theorem (Theorem 3.1) provides the first polynomial-time guarantee for prac-
tical Q-SVM training. TheO(1/
√
T)rate implies that quantum kernel optimization is not
fundamentally harder than classical non-convex optimization, despite the exponential Hilbert
space.
The separation bound (Theorem 3.3) formalizes the intuition that quantum advantage arises
from high-dimensional embeddings. The
p
2L/dscaling suggests that even modest circuit depths
(L= 3–5) can provide significant advantages whendis small-to-moderate, explaining why recent
experiments on 5–10 qubit devices show promise [19].
The Nyström approximation complexity (Proposition 3.5) demonstrates that QFE can be
practical even on NISQ hardware.
6.2 Connection to Prior Work
Our results complement Liu et al.’s [12] unconditional quantum advantage proof, which focused
on worst-case separation for a constructed problem. We provide average-case convergence and
separation guarantees applicable to natural datasets.
The convergence rate matches recent results on variational quantum algorithms [6], extending
them specifically to kernel methods. Our margin analysis connects to the work of Havlíček et al.
[8] by quantifying their empirical observations of quantum separability improvements.
6.3 Applications to Marketing Analytics
The theoretical and empirical results have direct implications for marketing analytics, particu-
larly in domains requiring automated consumer classification and decision-making under uncer-
tainty.
11

Accuracy Precision Recall F1
0
0.2
0.4
0.6
0.8
1
Metric
Value
Classical Lin Classical RBF
Classical Poly Q-Lin (sim)
Q-RBF (sim) Q-Poly (sim)
Q-Lin (hw) Q-RBF (hw)
Q-Poly (hw) Q-SVM
Figure 3: Performance comparison across different methods.
6.3.1 Customer Segmentation and Churn Prediction
Quantum kernel methods offer particular advantages for high-dimensional consumer behavior
data where classical methods struggle with non-linear interactions. The separation bound in
Theorem 3.3 implies that Q-SVM can identify subtle behavioral patterns that distinguish churn-
ers from retainers even when classical features exhibit high overlap.
For imbalanced churn datasets (typically 5–20% positive class), Q-SVM’s superior recall
directly translates to business value by reducing false negatives—the costliest errors in retention
campaigns.
6.3.2 Decision-Making Under Quantum-Enhanced Classification
The convergence guarantees in Theorem 3.1 enable principled decision-making frameworks where
classification confidence directly informs action thresholds. Marketing managers can use ROC-
based operating point selection to align model predictions with business policies.
6.4 Limitations and Future Work
Several limitations warrant further investigation:
Dataset Scope:Dataset heterogeneity and size may limit generalization. External valida-
tion on diverse consumer cohorts is needed.
Hardware Constraints:Shallow depth constraints driven by NISQ hardware fidelity. Our
experiments relied primarily on high-fidelity simulation; hardware runs were limited and shallow.
12

Noise Effects:Our theoretical results assume noiseless quantum operations. On real hard-
ware, gate errors and decoherence degrade kernel fidelity. Future work should extend Theorems
3.1–3.3 to noisy settings using quantum error mitigation techniques [4].
QFE Complexity:QFE’s quadratic complexity in features/observables without approxi-
mation. Nyström and sparse selection strategies require further optimization for production-scale
deployment.
Future Directions:
•Calibration-aware thresholding by segment and channel
•Multi-cohort external validation and online A/B testing
•Targeted hardware pilots with error mitigation
•Extensions to quantum kernel regression and causal inference
•Barren plateau characterization for deeper circuits
7 Conclusion
This work establishes rigorous theoretical foundations for quantum kernel methods through three
main contributions: (1) polynomial convergence guarantees for variational quantum kernel op-
timization, (2) tight separation bounds that explain quantum advantage in feature extraction,
and (3) complexity analysis of approximate QFE via Nyström methods.
A shallow, hardware-aware Q-SVM delivers a favorable precision-recall balance on a real
consumer task: 0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83 AUC. Ben-
efits are most notable in recall-critical use cases; ROC-guided thresholding enables policy-driven
operation without retraining.
These results bridge the gap between the theoretical promise of quantum machine learning
andpracticalNISQimplementations. Byformalizingwhenandwhyquantumadvantageemerges,
we provide a principled foundation for designing quantum kernel methods for real-world classi-
fication tasks in the near term.
Acknowledgments
We thank the QuantumKT program. This work was supported by RES grant IM-2025-2-0052
for Quantum Machine ONA access at Barcelona Supercomputing Center (BSC).
References
[1] S. Aaronson and A. Arkhipov. The computational complexity of linear optics.Theory of
Computing, 9(4):143–252, 2013.
[2] S. Aaronson and S. Gunn. On the classical hardness of spoofing linear cross-entropy bench-
marking.Theory of Computing, 16(11):1–8, 2020.
[3] F. Arute, K. Arya, R. Babbush, et al. Quantum supremacy using a programmable super-
conducting processor.Nature, 574:505–510, 2019.
[4] Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, and
T. E. O’Brien. Quantum error mitigation.Reviews of Modern Physics, 95(4):045005, 2023.
[5] M. C. Caro, E. Gil-Fuster, J. J. Meyer, J. Eisert, and R. Sweke. Encoding-dependent
generalization bounds for parametrized quantum circuits.Quantum, 5:582, 2021.
13

[6] M. Cerezo, A. Sone, T. Volkoff, L. Cincio, and P. J. Coles. Cost function dependent barren
plateaus in shallow parametrized quantum circuits.Nature Communications, 12(1):1791,
2021.
[7] J. R. Glick, T. P. Gujarati, A. D. Corcoles, Y. Kim, A. Kandala, J. M. Gambetta, and
K. Temme. Covariant quantum kernels for data with group structure.Nature Physics,
20:142–150, 2024.
[8] V. Havlíček, A. D. Córcoles, K. Temme, A. W. Harrow, A. Kandala, J. M. Chow, and
J. M. Gambetta. Supervised learning with quantum-enhanced feature spaces.Nature,
567(7747):209–212, 2019.
[9] H.-Y. Huang, M. Broughton, M. Mohseni, R. Babbush, S. Boixo, H. Neven, and J. R. Mc-
Clean. Power of data in quantum machine learning.Nature Communications, 12(1):2631,
2021.
[10] T. Hubregtsen, J. Pichlmeier, P. Stecher, and K. Bertels. Training quantum embedding
kernels on near-term quantum computers. arXiv preprint arXiv:2105.02276, 2021.
[11] W. Kretschmer, S. Grewal, M. DeCross, J. A. Gerber, K. Gilmore, D. Gresh, N. Hunter-
Jones, K. Mayer, B. Neyenhuis, D. Hayes, and S. Aaronson. Demonstrating an uncon-
ditional separation between quantum and classical information resources. arXiv preprint
arXiv:2509.07255, 2025.
[12] Y. Liu, S. Arunachalam, and K. Temme. A rigorous and robust quantum speed-up in
supervised machine learning.Nature Physics, 17(9):1013–1017, 2021.
[13] M. A. Nielsen and I. L. Chuang.Quantum Computation and Quantum Information. Cam-
bridge University Press, 2010.
[14] M. E. Sahin, B. C. B. Symons, P. Pati, F. Minhas, D. Millar, M. Gabrani, S. Mensa, and
J. L. Robertus. Efficient parameter optimisation for quantum kernel alignment.Quantum,
8:1502, 2024.
[15] L. Schnabel, M. F. Perelló, F. Ibarrondo, and V. Dunjko. Quantum kernel methods under
scrutiny: a benchmarking study.Quantum Machine Intelligence, 7(1):16, 2025.
[16] B. Schölkopf and A. J. Smola.Learning with Kernels. MIT Press, 2002.
[17] M. Schuld and N. Killoran. Quantum machine learning in feature Hilbert spaces.Physical
Review Letters, 122(4):040504, 2019.
[18] M. Schuld. Supervised quantum machine learning models are kernel methods. arXiv preprint
arXiv:2101.11020, 2021.
[19] T. Suzuki, T. Hasebe, and T. Miyazaki. Quantum support vector machines for classification
and regression on a trapped-ion quantum computer.Quantum Machine Intelligence, 6(1):31,
2024.
[20] C. K. Williams and M. Seeger. Using the Nyström method to speed up kernel machines. In
Advances in Neural Information Processing Systems, volume 13, pages 682–688, 2001.
[21] S. L. Wu, S. Chan, W. Guan, S. Sun, A. Wang, C. Zhou, M. Livny, F. Carminati,
A. Di Meglio, and A. C. Li. Application of quantum machine learning using the quantum
kernel algorithm on high energy physics analysis at the LHC.Physical Review Research,
3(3):033221, 2021.
14
