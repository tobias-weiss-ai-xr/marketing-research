---
title: 'Quantum Kernel Methods: Convergence Theory, Separation Bounds and Applications to Marketing Analytics'
url: https://doi.org/10.21203/rs.3.rs-7842283/v1
category: analytics
subcategory: theory
date: 2025-10
venue: Research Square
authors:
- Laura Sáez‐Ortuño
- Santiago Forgas‐Coll
- Массимилиано Феррара
source: openalex-oa
pdf_url: https://www.nature.com/articles/s41598-026-35793-y_reference.pdf
pages: 12
chars: 31397
fetched_at: '2026-11-08T17:47:45+00:00'
kb_version: 1
---

# Quantum Kernel Methods: Convergence Theory, Separation Bounds and Applications to Marketing Analytics

ARTICLE IN PRESS
Article in Press
Quantum kernel methods for marketing
analytics with convergence theory and
separation bounds
Scientific Reports
Received: 12 October 2025
Accepted: 8 January 2026
Cite this article as: Ortuño L.S., Coll S.F. &
Ferrara M. Quantum kernel methods for
marketing analytics with convergence
theory and separation bounds. Sci
Rep (2026). https://doi.org/10.1038/
s41598-026-35793-y
Laura Sáez Ortuño, Santiago Forgas Coll & Massimiliano Ferrara
We are providing an unedited version of this manuscript to give early access to its
findings. Before final publication, the manuscript will undergo further editing. Please
note there may be errors present which affect the content, and all legal disclaimers
apply.
If this paper is publishing under a Transparent Peer Review model then Peer
Review reports will publish with the final article.
https://doi.org/10.1038/s41598-026-35793-y
© The Author(s) 2026. Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit
to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do
not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this
article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the
article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain
permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licenses/by-nc-nd/4.0/.

Quantum kernel methods for marketing analytics
with convergence theory and separation bounds
Laura S ´a e z Ortu n˜o1 , Santiago Forgas Coll 1, Massimiliano Ferrara 2

1Facultat Economia i Empresa, Universitat de Barcelona, Spain
2Department of Law, Economics and Human Sciences, University Mediterranea of Reggio Calabria, Italy

Abstract
This work studies the feasibility of applying quantum kernel methods to a real con-
sumer classification task in the NISQ regime. We present a hybrid pipeline that combines a
quantum-kernel Support Vector Machine (Q-SVM) with a quantum feature extraction mod-
ule (QFE), and benchmark it against classical and quantum baselines in simulation (hardware
validation remains future work). Hyperparameters were selected via nested cross-validation
on the training partition and then fixed for test evaluation; under these settings, the pro-
posed Q-SVM attains 0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83
ROC AUC, exhibiting higher sensitivity while maintaining competitive precision relative to
classical SVM. All headline metrics are obtained via high-fidelity simulation. We interpret
these results as an initial indicator and a concrete starting point for NISQ-era workflows
and hardware integration, rather than a definitive benchmark. Methodologically, our design
aligns with recent work that formalizes quantum–classical separations and verifies resources
via XEB-style (Cross-Entropy Benchmarking) approaches, motivating shallow yet expressive
quantum embeddings to achieve robust separability despite hardware noise constraints.
Keywords: Quantum Machine Learning; Quantum Kernels; Support Vector Machines;
Convergence Theory; Separation Bounds; NISQ Algorithms; Feature Extraction; Classification
Theory

1 Introduction
Quantum machine learning (QML) has emerged as one of the most promising near-term appli-
cations of quantum computing, with quantum kernel methods representing a particularly ele-
gant bridge between classical machine learning theory and quantum computational advantages
[20, 9, 21]. The fundamental insight underlying quantum kernels is that quantum circuits can
efficiently compute inner products in exponentially large Hilbert spaces, potentially capturing
data relationships that are intractable for classical methods [14].
This study presents an end-to-end feasibility test of a quantum-enhanced method for su-
pervised classification on a real consumer dataset, evaluated with ROC analysis. We examine
whether shallow, NISQ-compatible quantum embeddings and kernels can improve class separa-
bility and enable threshold-based operation along the ROC curve without retraining. We report
0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83 AUC.
Recent work has demonstrated empirical success of quantum support vector machines (Q-
SVM) in various domains, from particle physics [24] to bioinformatics [22]. However, the the-
oretical foundations explaining when and why quantum advantage emerges remain incomplete.
While pioneering studies by Schuld and Killoran [20] established the mathematical equivalence
between variational quantum circuits and kernel methods, and Liu et al. [14] proved uncondi-
tional quantum advantage for specifically constructed problems, several fundamental questions
remain open:
ARTICLE IN PRESS
ARTICLE IN PRESS

√
1. What are the convergence guarantees for variational quantum kernel optimization?
2. Can we rigorously bound the separation advantage of quantum feature extraction?
3. How do circuit depth and approximation methods affect computational complexity?
This paper addresses these questions through three main theoretical contributions and em-
pirical validation on real consumer data.

1.1 Main contributions
We empirically validate convergence and separation principles on a real consumer classification
case. The Q-SVM achieves 0.83 AUC and 0.8609 recall, with 0.81 F1 and 0.7790 accuracy,
reinforcing the suitability of shallow embeddings under NISQ constraints.
We present proposed theoretical contributions with outlined proofs and explicit assumptions
for quantum kernel methods, as follows:
Theorem 3.1 (Convergence of Variational Quantum Kernels): We prove that vari-
ational quantum kernel optimization converges polynomially fast to optimal parameters under
Lipschitz-smooth loss functions and shallow circuit constraints. We propose and outline proofs
for convergence rates under smoothness and shallow-depth assumptions; these results align with
recent variational optimization theory and, to our knowledge, provide one of the first explicit
convergence rate statements tailored to quantum kernels in the NISQ setting.
Theorem 4.1 (Quantum Feature Extraction Separation Bounds): We derive sepa-
ration bounds under specific circuit and data assumptions indicating potential margin improve-
ments for shallow embeddings; these results are suggestive rather than definitive across arbitrary
datasets, showing that shallow circuits with L ≥ log2(d) + 1 layers can achieve separation ad-
vantages scaling as Ω( 2L/d) over classical kernels in the worst case.
Proposition 4.3 (Complexity of Approximate  QFE): We characterize the computa-
tional complexity of Nystr ¨om- approximated quantum feature extraction, proving that landmark
sampling with m points reduces complexity from O(N 2 · 4n) to O(Nm2 + m3) while maintaining
ϵ-approximation guarantees.

1.2 Marketing analytics applications and business impact
Our results could have direct implications for marketing analytics: recall-first regimes (retention,
proactive sales) benefit from 0.8609 recall, which reduces false negatives in high-value cohorts;
precision-first regimes can operate at higher thresholds while maintaining 0.7647 precision for
cost-sensitive outreach; and flexible thresholding is supported by a 0.83 AUC, enabling thresh-
olding without retraining and allowing ROC-guided policy selection across cohorts and time.

1.3 Related work
Kernel methods in quantum computing build upon decades of classical kernel theory [19]. The
quantum kernel framework was formalized by Schuld and Killoran [20], who showed that quan-
tum feature maps induce kernels through state overlap measurements. Ha vl´ıˇce k et al. [9]
provided the first experimental demonstration on superconducting hardware, while Liu et al.
[14] proved unconditional quantum advantages for classification via communication complexity
arguments.
Recent advances include quantum kernel alignment methods [11, 17], covariant kernels for
structured data [8], and large-scale benchmarking studies [18]. Recent advances also include
hardware-aware approaches to quantum kernel design. Liu et al. [13] propose using graph neural
networks to optimize quantum kernel circuits by directly incorporating hardware connectivity
constraints and noise characteristics, enabling automated discovery of device-specific ans ¨atze
ARTICLE IN PRESS
ARTICLE IN PRESS

i=1
i=1
i=1
Y
i=1 ℓ,i
α 2 i j i j θ i j i i,j=1 i=1
that outperform generic designs. This approach complements our theoretical framework by
providing practical tools for hardware deployment. However, most work focuses on empirical
performance or existence proofs of advantage, leaving convergence rates and practical separation
bounds unaddressed.
Our work complements these efforts by providing rigorous convergence theory and construc-
tive separation bounds applicable to NISQ devices. The proofs leverage recent techniques from
variational quantum algorithm optimization [7] and quantum circuit expressivity analysis [3],
which introduced the effective dimension concept based on the Fisher information matrix.

2 Preliminaries
2.1 Quantum Feature Maps and Kernels
Let X ⊆ Rd denote the classical input space, where d is the number of features in the original
dataset.  A quantum feature map is a mapping ϕθ : X → H to a quantum Hilbert space
H = (C2)⊗n, typically realized by a parameterized quantum circuit:
ϕθ(x) = U (x, θ)|0⟩⊗n, (1)
where U (x, θ) is a unitary operator encoding data x and variational parameters θ ∈ Θ ⊆ Rp.
The induced quantum kernel is defined as:
kθ(xi, xj) = |⟨ϕθ(xi)|ϕθ(xj)⟩|2. (2)

For a training dataset D = {(xi, yi)}N with yi ∈ {− 1, +1}, the Q-SVM optimization
problem is: N N
1 Σ Σ min α α y y k (x , x ) − α , (3)

subject to ΣN  αiyi = 0 and 0 ≤ αi ≤ C.

2.2 Circuit Ansatz
Specifically, we employ a data re-uploading ansatz with alternating data encoding and parame-
terized rotations:

where:
• Uenc(x) = Nn
L
U (x, θ) =  UentUrot(θℓ)Uenc(x), (4)
ℓ=1

RY (xi) encodes data with per-feature RY rotations,
• Urot(θℓ) = Nn RY (θℓ,i)RZ(θ′ ) applies parameterized single-qubit rotations,
• Uent implements sparse nearest-neighbor controlled-Z entangling gates. Specifically, controlled-
Z (CZ) gates are applied between adjacent qubits in a linear topology, i.e., CZ gates
between qubit pairs (qi, qi+1) for i = 1, . . . , n − 1. This nearest-neighbor connectivity
mirrors the physical constraints of many NISQ devices (e.g., superconducting processors
with linear or ladder topologies) and avoids the overhead of SWAP operations required
for all-to-all connectivity. For n = 4 qubits, each entangling layer applies 3 CZ gates:
CZ(q1, q2), CZ( q2, q3), CZ( q3, q4).
This structure balances expressivity and trainability for NISQ devices.
ARTICLE IN PRESS
ARTICLE IN PRESS

i=1

t+1 t 2β t β t
3 Convergence Theory for Variational Quantum Kernels
3.1 Setup and assumptions
Consider the kernel optimization objective:
L(θ) = E(x,y)∼D [ℓ(y, fθ(x))] , (5)
where fθ(x) = ΣN  αiyikθ(x, xi) is the Q-SVM decision function.
We make the following assumptions:
• (β-smoothness): The loss L(θ) is β-smooth: ∇L(θ) − ∇L(θ′)  ≤ β  θ − θ′  .
• (PL condition): The loss satisfies a Polyak-L- ojasiewicz condition: ∇L(θ)  2 ≥ 2µ(L(θ)−
L∗) for some µ > 0.
• (Shallow circuits): The circuit depth satisfies L ≤ c log(n) for some constant c.
• (Bounded gradients): ∇θkθ(xi, xj)  ≤ G uniformly.
Theorem 3.1 (Convergence of Variational Quantum Kernels) . Under Assumptions 1-4, gradi-
ent descent with step size η = 1/β satisfies:

L(θt) − L∗ ≤ µ  t 1 − (L(θ0) − L∗). (6) β
Thus, achieving L(θt) −L∗ ≤ ϵ requires O(κ log(1/ϵ)) iterations, where κ = β/µ is the condition
number.
Proof. For a β-smooth function, the standard descent lemma gives:
L(θt+1) ≤ L(θt) − η  ∇L(θt)  2 +
With step size η = 1/β:
βη2
2 ∇L(θt)

2. (7)
 L(θ 1 2 1 2 1 ) ≤ L(θ ) − ∇L(θ ) + ∇L(θ ) = L(θ ) −  ∇L(θ )  2 . (8)
t+1 t β t 2β t t 2β t
Applying the Polyak-L- ojasiewicz (PL) condition  ∇L(θ)  2 ≥ 2µ(L(θ) − L∗):
L(θ ) − L∗ ≤ L(θ ) − L∗ −  1  · 2µ(L(θ ) − L∗) =   1 − µ  (L(θ ) − L∗). (9)

Iterating yields the result. The iteration complexity O(κ log(1/ϵ)) follows from solving (1 −
µ/β)t ≤ ϵ/(L(θ0) − L∗).
Remark 3.2. The observed AUC and recall are consistent with the qualitative intuition of the
bounds, but do not constitute validation of the theoretical claims.

3.2 Complexity analysis
The total computational cost per iteration is:
Titer = O(N 2 · p · Tcircuit), (10)
where Tcircuit = O(nL) for shallow circuits. Total training cost becomes:
Ttotal = O(κ log(1/ϵ) · N 2pnL). (11)
For shallow circuits with L = O(log n), this scales as O(κN 2pn log n log(1/ϵ)).
ARTICLE IN PRESS
ARTICLE IN PRESS

j j=1
i=1
d
√
d d
4 Separation Bounds for Quantum Feature Extraction
4.1 Geometric margin analysis
Define the quantum feature extraction (QFE) operator:
Φ : Rd → R4n , Φ(x) = [⟨ϕ(x)|P |ϕ(x)⟩]4n , (12)
where {Pj} is a basis of observables (e.g., Pauli strings).
The geometric margin γQFE measures the normalized distance of the closest correctly clas-
sified point to the decision hyperplane in the quantum feature space. Specifically, for linearly
separable data after QFE, it is defined as:

γQFE = min
i
yiwT Φ(xi) , (13)
where w is the optimal separating hyperplane normal vector, Φ( xi) is the quantum feature
representation, and yi ∈ {−1, +1} is the class label. The numerator yiwT Φ(xi) is positive for
correctly classified points.
Theorem 4.1 (Quantum Feature Extraction Separation Bounds). Let D = {(xi, yi)}N be a
dataset with xi ∈ Rd (where d is the classical feature dimension) and classical margin γ classical.
For a quantum feature map with:
• Circuit depth L ≥ log2(d) + 1,
• Non-commuting observable basis {Pj} with deff = Ω(2L),
there exists a choice of parameters θ such that:
γQFE ≥ γclassical + Ω
 r
2L
!
. (14)

Proof sketch. The quantum feature space dimension is dQFE = 4n. For data-encoding circuits
with sufficient entanglement, the effective dimension satisfies deff ≥ 2L (Abbas et al. [3]). The
bound follows from random projection theory (specifically, the Johnson-Lindenstrauss lemma
and its extensions to feature maps). When projecting data from a d-dimensional space into
an effective deff-dimensional space via a sufficiently expressive quantum circuit, the margin can
increase by a factor proportional to  deff/d. The key insight is that quantum feature maps
with L layers and sufficient entanglement generate an effective representation space of dimension
deff = Ω(2L). Combining these results:
γQFE ≥ γclassical + Ω
 r
deff
!
= γclassical + Ω
 r
2L
!
. (15)

Remark 4.2. The observed AUC and recall are consistent with the qualitative intuition of the
bounds, but do not constitute validation of the theoretical claims.

4.2 Computational complexity of approximate QFE
Exact QFE requires measuring all 4n Pauli observables—exponential in qubit count. We analyze
Nystr ¨om approximation:

ARTICLE IN PRESS
ARTICLE IN PRESS

Nm
mm
mm
Proposition 4.3 (Complexity of Approximate QFE) . Let m ≪ N be the number of landmark
points. Nystr ¨om approximation of QFE:
Φ˜ (x) ≈ Kxm(Kmm)−1/2, (16)
where Kxm and Kmm are kernel submatrices, defined as follows:
• Kmm ∈ Rm×m is the kernel matrix restricted to the m landmark points, with entries
(Kmm)ij = kθ(zi, zj) for landmark points {z1, . . . , zm} ⊂ {x1, . . . , xN };
• Kxm ∈ R1×m (for a single query point x) or KNm ∈ RN×m (for all training points) con-
tains the kernel evaluations between query/training points and landmarks, with (KNm)ij =
kθ(xi, zj);
• KmN = KT is the transpose, completing the low-rank factorization.
The Nystr ¨om method approximates the full N × N kernel matrix as K ≈ KNmK−1 KmN ,
exploiting the fact that well-chosen landmarks capture the dominant spectral structure of the
kernel. This reduces complexity from O(N2 · 4n) to O(Nm2 + m3), achieving ϵ-approximation
with m = O(rank(K)/ϵ2).
Proof. The Nystr ¨om method approximates the full kernel matrix K ≈ KNmK−1 KmN . Eigen-
decomposition of Kmm requires O(m3). Computing Kxm for all x requires O(Nm2) kernel
evaluations. The approximation error is bounded by the tail eigenvalue decay (Williams &
Seeger, 2001).

5 Empirical Validation
5.1 Task, data, and metrics
The datasets analyzed in this study belong to the European projects DT4H and AI4HF. Due
to strict privacy, data protection, and governance requirements, they are not publicly available.
Although these European projects focus on digital health and artificial intelligence for health-
related applications, our specific classification task concerns the prediction of user engagement
and service adoption behavior—which we refer to as “consumer classification”—rather than clin-
ical or diagnostic outcomes. The features characterize user interaction patterns, demographic at-
tributes, and behavioral indicators derived from anonymized platform usage data. This framing
is consistent with marketing analytics terminology while respecting the health-adjacent context
of the original data collection.
We evaluate on a binary consumer classification task with N = 500 training samples, Ntest =
125 test samples (20% holdout), d = 8 features, and balanced classes. Features are normalized
to [0, 2π] for quantum encoding.
We report accuracy, precision, recall, F1 score, and ROC AUC. Hyperparameters are tuned
via 5-fold cross-validation on the training set.

5.2 Quantum circuit implementation
We use n = 4 qubits with L = 3 layers, resulting in p = 24 variational parameters. The circuit
is implemented using Qiskit with:
• Ideal statevector simulator (Aer)
• Noisy simulator with realistic error models calibrated from IBM device specifications
All reported metrics are obtained via high-fidelity simulation. Hardware validation on physical
devices remains a direction for future work.
ARTICLE IN PRESS
ARTICLE IN PRESS

5.3 Results: Comparison with classical and quantum baselines
Table 1 presents the performance comparison, including the generalization gap (difference be-
tween training and test accuracy).

Method Train Acc. Test Acc. Precision Recall F1 AUC
Classical SVM (RBF) 0.7920 0.7600 0.7800 0.7300 0.7540 0.79
Classical SVM (poly) 0.7880 0.7550 0.7750 0.7250 0.7493 0.78
Q-SVM (fixed) 0.8150 0.7790 0.7647 0.8609 0.8100 0.83
Q-SVM + QFE 0.8220 0.7850 0.7900 0.8350 0.8118 0.83
Table 1: Performance comparison. Q-SVM achieves the highest recall and AUC. Generalization
gaps are comparable across methods (3.2–3.7%), indicating that Q-SVM does not exhibit sig-
nificant overfitting relative to classical baselines despite the higher-dimensional feature space.
In our experiment, the Q-SVM achieved higher recall and F1 on this dataset relative to our
classical baselines; broader claims require additional benchmarks and significance testing.
The Q-SVM shows particular strength in recall (0.8609), indicating superior identification
of positive cases—critical for marketing applications prioritizing customer retention.

5.4 ROC analysis and threshold selection
Figure 1 shows the ROC curves for Q-SVM and classical SVM-RBF. The high AUC (0.83)
indicates robust separability across operating points. Marketing teams can select thresholds
based on campaign objectives:
• High-recall mode (threshold=0.3): 0.8609 recall, 0.7647 precision
• Balanced mode (threshold=0.5): 0.8100 F1
• High-precision mode (threshold=0.7): 0.8500 precision, 0.7200 recall

1

0.8

0.6

0.4

0.2

0
0 0 .2 0 .4 0 .6 0 .8 1
False Positive Rate

Figure 1: ROC curves for Q-SVM (AUC = 0.83) and classical SVM-RBF (AUC = 0.79). Operat-
ing points are marked for threshold selection: high-recall mode (circle), balanced mode (square),
and high-precision mode (triangle).

True Positive Rate
ARTICLE IN PRESS
ARTICLE IN PRESS

6 Limitations and Future Work
This study should be interpreted as a first experiment and an initial feasibility indicator rather
than as definitive evidence of quantum advantage or on-device performance. Several limita-
tions constrain the scope, generalizability, and interpretability of our findings. First, results are
derived from a single, real consumer dataset without external validation across cohorts, geogra-
phies, or time. We did not conduct statistical significance testing or drift analysis. Consequently,
any observed gains should be viewed as preliminary signals that require confirmation through
multi-cohort validation and temporal robustness checks.
Second, all headline metrics were obtained via high-fidelity simulation. Hardware valida-
tion on physical devices remains a direction for future work. We did not perform systematic
error-mitigation studies or robustness tests across device configurations, so our empirical results
provide suggestive indications under simulation, not validated on-device outcomes.
Third, the theoretical results rely on assumptions (e.g., β-smoothness, PL-like conditions,
non-commutativity, shallow depth, and effective dimensionality) that were not empirically ver-
ified across settings and presume noiseless operations. These statements should be read as
assumption-bound and illustrative. Extending Theorem 3.1–4.1 to noisy regimes with quantum
error mitigation techniques [5] and empirically validating the assumptions remain open tasks.
Fourth, the practicality and scaling of QFE pose challenges. Without approximations, QFE
entails substantial measurement and processing overhead. Our Nystr ¨om and sparse observable
selection strategies were explored in simulation without end-to-end profiling of hardware latency,
cost, or throughput, and the criteria for landmark/observable selection were only partially char-
acterized. As such, QFE-related improvements should be regarded as indicative and contingent
on scalable approximations.
Future research should prioritize confirmation and generalization of these preliminary indi-
cations: calibration-aware thresholding by segment and channel with cohort-wise governance;
multi-cohort external validation and online A/B testing to quantify lift; targeted hardware pilots
with error mitigation and shallow circuits; inclusion of stronger classical baselines with signifi-
cance testing; extensions to quantum kernel regression and causal inference for uplift modeling;
and characterization of barren plateaus for deeper circuits  (L ≫ log n). Hardware-aware cir-
cuit optimization using machine learning approaches [13] represents a promising direction for
bridging the gap between our theoretical bounds and practical device deployment.

7 Conclusion
This work proposes and outlines theoretical results for quantum kernel methods under explicit
assumptions, presented as initial steps rather than definitive, general guarantees: first, polyno-
mial convergence rates for variational quantum kernel optimization under smoothness and PL
conditions; second, constructive separation bounds showing potential quantum advantage for
shallow circuits; third, complexity analysis demonstrating the feasibility of approximate quan-
tum feature extraction.
A shallow, hardware-aware Q-SVM delivers a favorable precision–recall balance on a real
consumer task: 0.7790 accuracy, 0.7647 precision, 0.8609 recall, 0.8100 F1, and 0.83 AUC.
Benefits are most notable in recall-critical use cases; ROC-guided thresholding enables policy-
driven operation without retraining. QFE indicates additional upside contingent on scalable
approximations.
These results should be interpreted as feasibility indicators for NISQ-era workflows rather
than as evidence of broad quantum advantage. By formalizing when and why quantum advantage
emerges, we provide a principled foundation for designing quantum kernel methods for real-world
classification tasks in the near term.
Future work will extend these results to noisy quantum devices, explore the barren plateau
ARTICLE IN PRESS
ARTICLE IN PRESS

transition in deeper circuits, and investigate quantum advantage for regression and other learning
tasks. As quantum hardware scales to 100-1000 qubits, the theoretical tools developed here will
be essential for characterizing the limits of quantum-enhanced machine learning.

Acknowledgments
We thank the QuantumKT program. This work was supported by RES grant IM-2025-2-0052
for Quantum Machine ONA access at Barcelona Supercomputing Center (BSC). We gratefully
acknowledge the support of the European projects DT4H and AI4HF, without which this work
would not have been possible. We extend our special thanks to researchers Jorge Refugio
Fabila Fabian, Carlos Mart´ın Isla, Karim Lekadir, and Giampaolo Viglia for their valuable
contributions, scientific guidance, and commitment throughout all phases of the study.

Declarations
Ethics compliance
This study analysed fully anonymized consumer data. In line with the EU General Data Pro-
tection Regulation (GDPR, Regulation (EU) 2016/679), Recital 26 clarifies that information
which does not relate to an identified or identifiable natural person—i.e., data irreversibly
anonymized so that identification is not reasonably possible—falls outside the scope of the
GDPR. Consistent with Spanish Organic Law 3/2018 on Personal Data Protection and Digital
Rights (LOPDGDD), which applies only to personal data, the dataset used in this research does
not constitute personal data. Consequently, and given that the study involved no interaction
with human participants and no processing of identifiable personal data, review by a Research
Ethics Committee/Institutional Review Board was not required. All analyses adhered to appli-
cable institutional policies, good research governance, and the non-profit research terms of the
Spanish Supercomputing Network (RES) and the Barcelona Supercomputing Center (BSC).

Ethics and regulatory compliance
This study used fully anonymised consumer data and, according to the applicable institutional
policies and regulations, did not require review by a Research Ethics Committee/Institutional
Review Board. No identifiable personal data were used and no re-identification was attempted.

Informed consent
Data used in this study were provided to the authors in fully anonymized form under the
governance of the European projects DT4H and AI4HF and their data-sharing terms. No
identifiable personal data were accessible to the authors, and no re-identification was attempted.

Computational resources and data handling (RES/BSC)
Use of RES/BSC facilities complied with their non-profit research mandate and applicable Usage
Terms Conditions. Access credentials were kept strictly confidential. Any use for profit purposes
would require a prior commercial agreement.

References
[1] S. Aaronson and A. Arkhipov. The computational complexity of linear optics. Theory of
Computing, 9(4):143–252, 2013.
ARTICLE IN PRESS
ARTICLE IN PRESS

[2] S. Aaronson and S. Gunn. On the classical hardness of spoofing linear cross-entropy bench-
marking. Theory of Computing, 16(11):1–8, 2020.
[3] A. Abbas, D. Sutter, C. Zoufal, A. Lucchi, A. Figalli, and S. Woerner. The power of
quantum neural networks. Nat. Comput. Sci., 1:403–409, 2021.
[4] F. Arute, K. Arya, R. Babbush, et al. Quantum supremacy using a programmable super-
conducting processor. Nature, 574:505–510, 2019.
[5] Z. Cai, R. Babbush, S. C. Benjamin, S. Endo, W. J. Huggins, Y. Li, J. R. McClean, and
T. E. O’Brien. Quantum error mitigation. Reviews of Modern Physics, 95(4):045005, 2023.
[6] M. C. Caro, E. Gil-Fuster, J. J. Meyer, J. Eisert, and R. Sweke. Encoding-dependent
generalization bounds for parametrized quantum circuits. Quantum, 5:582, 2021.
[7] M. Cerezo, A. Sone, T. Volkoff, L. Cincio, and P. J. Coles. Cost function dependent barren
plateaus in shallow parametrized quantum circuits. Nature Communications, 12(1):1791,
2021.
[8] J. R. Glick, T. P. Gujarati, A. D. Corcoles, Y. Kim, A. Kandala, J. M. Gambetta, and
K. Temme. Covariant quantum kernels for data with group structure. Nature Physics ,
20:142–150, 2024.
[9] V. Ha vl´ıˇc ek, A. D. C´orcoles,  K. Temme, A. W. Harrow, A. Kandala, J. M. Chow, and
J. M. Gambetta. Supervised learning with quantum-enhanced feature spaces. Nature,
567(7747):209–212, 2019.
[10] H.-Y. Huang, M. Broughton, M. Mohseni, R. Babbush, S. Boixo, H. Neven, and J. R.
McClean. Power of data in quantum machine learning. Nature Communications , 12(1):2631,
2021.
[11] T. Hubregtsen, J. Pichlmeier, P. Stecher, and K. Bertels. Training quantum embedding
kernels on near-term quantum computers. arXiv preprint arXiv:2105.02276, 2021.
[12] W. Kretschmer, S. Grewal, M. DeCross, J. A. Gerber, K. Gilmore, D. Gresh, N. Hunter-
Jones, K. Mayer, B. Neyenhuis, D. Hayes, and S. Aaronson. Demonstrating an uncon-
ditional separation between quantum and classical information resources. arXiv preprint
arXiv:2509.07255, 2025.
[13] H. Liu, Y. Zhang, J. Chen, et al. Hardware-aware quantum kernel design based on graph
neural networks. arXiv preprint arXiv:2506.21161, 2025.
[14] Y. Liu, S. Arunachalam, and K. Temme. A rigorous and robust quantum speed-up in
supervised machine learning. Nature Physics , 17(9):1013–1017, 2021.
[15] M. A. Nielsen and I. L. Chuang. Quantum Computation and Quantum Information: 10th
Anniversary Edition. Cambridge University Press, 2010.
[16] L. S´aez- Ortu n˜o, R. Huertas-Garcia, S. Forgas-Coll, J. S´anc hez- Garc´ıa, and E. Puertas-
Prats. Quantum computing for market research. Journal of Innovation & Knowledge,
9(3):100510, 2024.
[17] M. E. Sahin, B. C. B. Symons, P. Pati, F. Minhas, D. Millar, M. Gabrani, S. Mensa,
and J. L. Robertus. Efficient parameter optimisation for quantum kernel alignment: A
sub-sampling approach in variational training. Quantum, 8:1502, 2024.
[18] L. Schnabel, M. F. Perell ´o, F. Ibarrondo, and V. Dunjko. Quantum kernel methods under
scrutiny: a benchmarking study. Quantum Machine Intelligence , 7(1):16, 2025.
ARTICLE IN PRESS
ARTICLE IN PRESS

[19] B. Sch¨olkopf  and A. J. Smola. Learning with Kernels: Support Vector Machines, Regular-
ization, Optimization, and Beyond. MIT Press, Cambridge, MA, 2002.
[20] M. Schuld and N. Killoran. Quantum machine learning in feature Hilbert spaces. Physical
Review Letters, 122(4):040504, 2019.
[21] M. Schuld. Supervised quantum machine learning models are kernel methods. arXiv
preprint arXiv:2101.11020, 2021.
[22] T. Suzuki, T. Hasebe, and T. Miyazaki. Quantum support vector machines for classifica-
tion and regression on a trapped-ion quantum computer. Quantum Machine Intelligence ,
6(1):31, 2024.
[23] C. K. Williams and M. Seeger. Using the Nystr ¨om method to speed up kernel machines.
In Advances in Neural Information Processing Systems, volume 13, pages 682–688, 2001.
[24] S. L. Wu, S. Chan, W. Guan, S. Sun, A. Wang, C. Zhou, M. Livny, F. Carminati, A. Di
Meglio, A. C. Li, et al. Application of quantum machine learning using the quantum
kernel algorithm on high energy physics analysis at the LHC. Physical Review Research ,
3(3):033221, 2021.
ARTICLE IN PRESS
ARTICLE IN PRESS
