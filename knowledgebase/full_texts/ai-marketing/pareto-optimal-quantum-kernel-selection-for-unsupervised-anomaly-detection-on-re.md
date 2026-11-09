---
title: Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing
  data
url: https://arxiv.org/abs/2610.09717
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Boaz Micah
- Nadia Milazzo
- Maissa Beji
- Borja Aizpurua
- Llorenç Espinosa-Portalés
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.09717
pages: 13
chars: 63867
fetched_at: '2026-11-08T13:25:43+00:00'
kb_version: 1
---

# Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real malware beaconing data

Pareto-optimal quantum kernel selection for unsupervised anomaly detection on real
malware beaconing data
Boaz Micah, 1 Nadia Milazzo, 2,∗ Maissa Beji, 3 Borja Aizpurua, 1, 4 Lloren¸ c Espinosa-Portal´ es,1,† Esteban
Payares,2 Ghada Ben Slama, 2 Luc Andrea, 3 Michel Kurek, 3 Thomas Cope, 5 and Olivier Salomon 6,‡
1Multiverse Computing, Parque Cient´ ıfico y Tecnol´ ogico de Gipuzkoa,
Paseo de Miram´ on 170, Planta 2, 20014 Donostia / San Sebasti´ an, Spain
2IQM Quantum Computers, 4 rue Royale, 75008 Paris, France
3Multiverse Computing, 7 rue de la Croix Martre, 91120 Palaiseau, Paris, France
4Department of Basic Sciences, Tecnun – University of Navarra, San Sebasti´ an, Spain
5IQM Quantum Computers, Georg-Brauchle-Ring 23-25, 80992 Munich, Germany
6Allianz Quantum Hub, Paris, France
Quantum kernel methods are leading candidates for a practical quantum advantage in machine
learning, but assessing that potential requires two quantities usually reported separately: how well
a kernel performs on the task, and how far its geometry departs from the classical kernels available
for the same problem. We introduce a fully unsupervised, multi-objective protocol that optimises
simultaneously the normalised pseudo discrepancy (NPD), a label-free proxy for anomaly detection
quality, and the geometric difference (GD) to a tuned classical reference kernel, selecting models
from the resulting Pareto front. We apply it to malware beaconing detection in real network traffic,
using a one-class support vector machine with fidelity and projected quantum kernels over four data
encodings, on simulators and on IQM’s 20-qubit Garnet processor. NPD-guided selection alone finds
a fidelity kernel that beats the tuned classical baseline, but with a geometric difference too small to
certify the gain as quantum. Projected kernels reach far larger geometric differences; the Pareto-
selected one only marginally exceeds the baseline (AUC 0.782 versus 0.765,g C→Q ≈89>
√
N
relative to that reference kernel), still below the NPD-selected fidelity kernel (0.840).
I. INTRODUCTION
Quantum machine learning (QML) is one of the most
active research areas in quantum computing, and a key
space for the search of quantum advantage in the noisy
intermediate-scale quantum (NISQ) era [1–3]. Models
based on variational quantum circuits have been pro-
posed, such as quantum neural networks, but their appli-
cability remains limited due to the barren plateau prob-
lem, an issue suffered generally by variational quantum
algorithms [4]. In contrast, quantum kernel methods of-
fer an alternative approach in which a quantum circuit
estimates a kernel matrix and the resulting kernel is used
by a classically trained support vector machine [5]. Here,
we use such a quantum kernel within a classical one-class
SVM, rather than a fully quantum SVM algorithm [6].
Quantum kernels use quantum circuits to define data-
dependent similarity measures whose induced geometry
may differ from that of the classical kernel families con-
sidered for a given task, potentially providing a useful
task-dependent inductive bias.
Despite their promise, quantum kernels have yet to
demonstrate a practical advantage. Furthermore, they
present a fundamental trade-off in expressivity. A highly
expressive kernel exploring a large Hilbert space can eas-
ily lead to an exponential concentration of fidelity kernel
values, which vanish for most data points as the number
∗ nadia.milazzo@iqm.tech
† llorenc.espinosa@multiversecomputing.com
‡ olivier.salomon@allianz.fr
of qubits increases [7, 8]; the very feature hypothesized
to provide advantage thus leads, when scaled up, to an
essentially useless model.
This can be mitigated by optimizing the kernel band-
width, as shown in [9], or by using projected quantum
kernels (PQK), introduced in [10], where the embedding
quantum state is projected back to an approximate clas-
sical representation before computing the kernel. At the
opposite extreme, however, a quantum kernel with low
expressivity may not be distinguishable at all from a
classical kernel. The data-dependent notion of geometric
difference (GD) was introduced in [10] to quantify the
separation between classical and quantum kernels, and
gives a recipe to construct artificial learning problems
that best separate the corresponding models. We distin-
guish this structural separation from predictive quantum
advantage: a large GD indicates that a quantum kernel
is not well approximated, in the relevant geometric sense,
by the chosen classical reference kernel, but it does not
guarantee superior task performance. Prior works have
tuned quantum kernels for predictive performance [11]
or characterized their potential advantage over classi-
cal kernels through their spectral properties [12], while
label-free hyperparameter selection, in which an inter-
nal quality proxy computed from the data replaces a la-
beled validation set, has been developed only for clas-
sical detectors: Dai and Fan introduced the normalized
pseudo discrepancy (NPD) as such a proxy for unsuper-
vised anomaly detection [13]. To our knowledge, no prior
work has jointly optimized predictive performance and
separation from classical kernels under a fully unsuper-
vised protocol.
arXiv:2610.09717v1  [quant-ph]  7 Oct 2026

2
We address this gap with a multi-objective optimiza-
tion framework that simultaneously maximizes the nor-
malized pseudo discrepancy (NPD) [13], a label-free
anomaly detection quality proxy, and the GD to the ref-
erence classical kernel. This provides a systematic frame-
work for balancing predictive performance and geometric
separation. To showcase the application of the method
in a realistic scenario, we test it on the unsupervised
anomaly detection problem on real malware beaconing
data – the periodic communication between an infected
host and a command-and-control server used to receive
commands or exfiltrate data. We explore different fi-
delity kernels and PQKs, computed on noisy simulators
and IQM’s quantum hardware. Our results show that
some projected quantum kernels achieve a large geomet-
ric difference (formalized in Section III B), indicating that
a learning problem with potential quantum prediction
advantage can be constructed from the data. However,
this geometric separation brings at most a marginal per-
formance gain on the malware detection task considered
here.
The choice of malware beaconing as a proof of concept
is deliberate, as the application of unsupervised quantum
kernels to real cybersecurity data remains underexplored.
The scarcity of malware data makes unsupervised mod-
els a requirement, while data fragmentation across the
industry due to privacy and security concerns motivates
the search for models that can identify complex patterns
in limited data, a regime in which quantum kernels are
more likely to generalize from few samples and separate
from classical kernels [10, 14].
Our contributions can be summarized as follows:
(i) A multi-objective (NPD + GD) Pareto framework
for systematically searching for empirical, but not
provable, quantum advantage in kernel methods,
applicable beyond this use case.
(ii) NPD as a fully label-free criterion for quantum ker-
nel hyperparameter tuning.
(iii) The first unsupervised quantum kernel benchmark
on real malware beaconing data.
(iv) Empirical characterization of the performance–
separability trade-off: fidelity kernels achieve the
strongest detection performance while remaining
below the geometric-difference scale beyond which
classical kernels are no longer guaranteed to match
quantum performance, whereas projected kernels
exceed this scale without a corresponding gain in
detection.
(v) Hardware deployment on the 20-qubit IQM Gar-
net processor with simulator-vs-QPU comparison,
showing that, at current noise levels, neither kernel
family yet reaches the classical baseline.
The rest of the paper is organized as follows. Sec-
tion II discusses related work and background relevant to
the results presented here. Section III describes all the
methods, particularly the multi-objective kernel selection
based on Pareto optimality and the feature engineering
procedure. Section IV describes our results, including
classical baselines, quantum kernels run on noisy simu-
lators, and quantum kernels run on quantum hardware.
We finish with a discussion of the results and our conclu-
sions in Section V.
II. RELA TED WORK
The question of whether quantum kernels offer a gen-
uine advantage over classical ones predates our work
and remains unsettled. On the positive side, rigorous
constructions show that quantum kernels can yield a
provable speedup for carefully designed learning prob-
lems [15, 16], and the geometric difference of Huang et
al. [10] provides the theoretical lens through which such
separations are usually argued. On the negative side,
the picture on realistic data is far less encouraging. Fi-
delity kernels are prone to exponential concentration as
expressivity grows [7], and systematic numerical com-
parisons repeatedly find that classical kernels match or
exceed their quantum counterparts on standard bench-
marks [17], while analyses of their generalization in the
NISQ era further temper expectations [18]. Even where
a large geometric difference is present, it is necessary but
not sufficient for advantage: the induced feature space
must also carry an inductive bias aligned with the task at
hand [12]. This literature motivates our stance of treat-
ing geometric separation and predictive quality as two
distinct criteria that must be assessed together, rather
than assuming that one implies the other.
A second body of work concerns unsupervised anomaly
detection and, in particular, the difficulty of model se-
lection when labels are unavailable. One-class sup-
port vector machines [19], isolation forests [20], and
reconstruction-based autoencoders [21] are long-standing
baselines that are normally used as classical references.
In all of them, performance is highly sensitive to hyperpa-
rameters, including the threshold used to flag anomalies,
yet the usual practice of tuning against a labeled vali-
dation set is precisely what an unsupervised setting for-
bids. Label-free surrogates have therefore been proposed
to guide model selection; among these, the normalized
pseudo discrepancy (NPD) of Dai and Fan [13] measures
the separation between anomaly scores on held-out nor-
mal data and on synthetic out-of-distribution samples,
and correlates with detection quality without any access
to labels. Such surrogates, however, have so far guided
only classical model selection.
Applications of quantum machine learning to cyberse-
curity, finally, remain comparatively sparse, and the ex-
isting efforts fall into categories that do not overlap with
the regime we study. A first line addresses supervised
classification of malware and network attacks, compar-
ing quantum and classical models where labels are abun-

3
dant [22–25], or relaxes the requirement only to the semi-
supervised case [26]. A second line does operate without
labels, building on quantum autoencoders for network-
traffic anomaly detection [27]; such reconstruction-based
pipelines are not organized around a quantum kernel, and
so do not expose the kernel matrix that the geometric dif-
ference requires. A third line applies the combination of
quantum kernels and unsupervised anomaly detection to
non-cybersecurity (financial and physics) data [28], and
evaluates detection across a controlled range of anomaly
ratios, treating the contamination level as a known quan-
tity rather than unknown, as required in an operational
deployment. None of the above works combines all three
ingredients at once: an unsupervised protocol, a quan-
tum kernel amenable to geometric analysis, and real cy-
bersecurity data. This intersection is where malware
beaconing detection sits, and where labeled data is gen-
uinely scarce and quickly rendered obsolete by concept
drift [29, 30], so that a fully unsupervised treatment is
not a convenience but a requirement. Our work is, to our
knowledge, the first to occupy it.
III. METHODS
A. Kernel methods
Kernel methods are widely used in machine learning
to solve, e.g., classification and regression problems. The
key idea of these techniques is to map data, by means of
a non-linear feature map, from an input space to a (usu-
ally higher dimensional) feature space, where the learning
task becomes easier to analyze, i.e. linear. The data can
then be processed in the feature space by accessing solely
the kernel values, which represent a similarity measure
between data, without explicitly computing the feature
map. This is usually referred to as thekernel trick.
We now define the notation for the quantum kernels
used in the following sections [31]. A kernelk:X×X→
Ris a positive definite function in two data pointsx,x ′.
Letϕ:x→ρ(x) be a data-encoding feature map over the
input spaceX, whereρis a density matrix. A quantum
kernel can then be defined as the inner product of the
feature vectors:
k(x,x′) = Tr (ρ(x′)ρ(x)) =|⟨ϕ(x′)|ϕ(x)⟩| 2.(1)
where the second equality holds if the data-encoding
quantum state is pure. We will refer to the kernel in
Eq. (1) as thefidelity kernel. The second kernel consid-
ered in this work is the projected quantum kernel intro-
duced in [10]:
k(x,x′) = exp
(
−γ
∑
k
∥ρk(x)−ρ k(x′)∥2 F
)
(2)
whereγ >0 is a hyperparameter,∥·∥ F is the Frobe-
nius norm andρ k(x) = Tr j̸=k(ρ(x)) is the single-qubit
reduced density matrix. The hyperparameterγacts as
an inverse lengthscale in the space of reduced density ma-
trices, setting the distance over which two encoded states
count as similar; it plays the role of the bandwidth of a
classical RBF kernel, whose tuning is known to mitigate
exponential kernel concentration [9].
Given the kernel function, for a finite set of data points
we can define the kernel matrix as the square matrix
whose entries are given by the inner product between
all possible pairs. This matrix is then fed to a classical
anomaly detection algorithm. In our case, we use a One-
Class Support Vector Machine (OCSVM) which learns a
decision boundary that encloses normal data given a ker-
nel matrix [32]. In the quantum case, the data-encoding
feature map is a unitaryU(x) implemented by a quantum
circuit. Previous works have studied how to design clas-
sically difficult feature maps to get a provable advantage
over classical kernels [15] or have identified a promising
class of learning problems for quantum kernels [33]. As
the focus of this work is to present a fully unsupervised
pipeline for anomaly detection with quantum kernels, we
do not engineer a new feature map, but use encodings
already present in the literature. The choice of the op-
timal encoding becomes part of the multi-objective opti-
misation presented in Sec. III B below. We consider four
different data-encoding circuits, whose definition and de-
tails can be found in Appendix A.
B. Multi-objective quantum kernel selection
The main methodological contribution of this work is
the development of a fully unsupervised quantum kernel
selection that simultaneously optimizes quantum kernel
performance via the NPD score and separation with re-
spect to classical kernels via the GD.
Starting with the quantum kernel performance, the ab-
sence of labels in unsupervised settings poses a challenge
for hyperparameter tuning of ML models. To address this
issue, we use the normalized pseudo-discrepancy (NPD)
score, first introduced in Ref. [13], which measures the
discrepancy between the anomaly scores of a validation
set drawn from the training data and a validation set
drawn from an axis-aligned Gaussian fitted to the train-
ing data.
More precisely, given an unsupervised anomaly de-
tection modelMwith hyperparameters Θ, the train-
ing datasetXis randomly split into a training subset
Xtrn and a validation subsetX val, where|X val|=m.
The model is trained only onX trn. Letµ trn∈R d and
σ2 trn∈R d denote the empirical mean and variance vec-
tors ofX trn, respectively. A generated datasetX gen of
sizemis then sampled from an axis-aligned Gaussian
distribution with diagonal covariance
Xgen∼N
(
µtrn,diag(σ 2 trn) ) ,
whose per-dimension variances match those ofX trn.

4
Lets val =f M(Xval |Θ) ands gen =f M(Xgen |Θ)
denote the anomaly score vectors produced by the model
for the validation and generated samples, respectively.
The NPD metric is then defined as
VNPD(M,X) = (Mean(sgen)−Mean(s val))2 2 (Var(sgen) + Var(sval)) +ε,
whereε>0 is a small constant to ensure numerical sta-
bility.
Intuitively, NPD measures how well the model sep-
arates the validation samples, assumed to be predomi-
nantly normal, from synthetically generated samples that
are more diverse and likely to lie outside the normal
data manifold. A larger NPD indicates a clearer separa-
tion in anomaly scores, which empirically correlates with
better detection performance on unseen test data. Im-
portantly, NPD is hyperparameter-free, translation- and
scale-invariant with respect to the scoring function, and
mitigates overfitting by relying on data (X val andX gen)
that are independent of model training.
On the other hand, the potential advantage offered by
a quantum model over a classical model can be evaluated
by means of the geometric difference, as introduced in
Ref. [10] and defined as
gC→Q =
√‖‖‖ √ KQK−1 C √ KQ ‖‖‖ ∞ ,(3)
whereK C andK Q denote the classical and quantum
kernel matrices, respectively, withK C taken as the ker-
nel of the tuned classical OCSVM baseline, both nor-
malised such that Tr(KQ) = Tr(KC) =N. The notation
∥·∥∞ represents the matrix spectral norm. Intuitively, if
KC(xi,x j) is small (large) wheneverK Q(xi,x j) is small
(large), then the geometric difference takes a small value.
A small geometric difference indicates that the classical
model is guaranteed to achieve performance similar to,
or better than, the quantum model. Conversely, the ge-
ometric difference increases as the two kernels deviate
from one another.
Furthermore, it is shown in [10] that the classical model
is expected to provide similar or better performance when
gC→Q≪
√
N,(4)
whereNis the number of samples in the training dataset.
With both objectives defined, we search over feature
maps and OCSVM hyperparameters for the Pareto front,
i.e. the set of non-dominated solutions: a solution is non-
dominated when no other candidate is at least as good in
both objectives and strictly better in one, so neither NPD
nor GD can be improved without degrading the other.
We apply this approach to both the fidelity and the pro-
jected quantum kernels. Table I gives the list of hyper-
parameters that were optimised. To obtain the Pareto
front, we used the open-source package Optuna [34] in
addition to the NSGA-II sampler [35]. NSGA-II is a ge-
netic multi-objective optimisation algorithm. It begins
optimisation loop
Sample hyperparameters
NSGA-II sampler
Feature map: Z, IQP, CNOT, Hamiltonian
Number of layers: 1-5
nu (OCSVM): 0-1
gamma (projected kernel): 100µ to 10
Build quantum kernel matrix
Fidelity or projected
Maximize NPD Maximize GD Maximize NPD and GD
Evaluate best model per objective
AUC, F1(A), F1(N)
NPD objective GD objective Joint objective
FIG. 1. The unsupervised optimisation pipeline: a hyper-
parameter search over quantum kernels selected under three
objectives (NPD, GD, and their joint Pareto knee) and eval-
uated on the test set.
from an initial population of candidate solutions sampled
from the search space and evolves it over successive gen-
erations, evaluating each candidate on both objectives
and carrying the best ones forward. Here, a candidate
solution is a choice of hyperparameters from the search
space in Table I. From the Pareto frontier of the final pop-
ulation, we select as the best solution the knee point, i.e.
the best-compromise configuration: both objectives are
rescaled to [0,1] across the front, and we retain the solu-
tion with the smallest Euclidean distance to the utopia
point (1,1) at which both NPD and GD would be si-
multaneously maximal. This avoids the extremes of the
front, where one objective is optimised at the expense of
the other.
In addition to the joint multi-objective optimisation of
the NPD and GD scores, we also optimised each objec-
tive independently. For these single-objective runs, Op-
tuna defaults to the Tree-structured Parzen Estimator
(TPE) [36], a Bayesian sampler that models the promis-
ing and unpromising regions of the search space sepa-
rately and proposes new configurations by maximising
their density ratio. This yields three sets of optimised hy-
perparameters per kernel—one maximising NPD alone,
one maximising GD alone, and one balancing both. Fig-
ure 1 shows a summary of the three optimisations.
C. Dataset
To test our systematic approach of finding the opti-
mal quantum kernel model, we decided to test it on a
real-world malware beaconing dataset. Malware beacon-
ing represents periodic communication between an in-
fected host and an external C&C (command-and-control)
server. These signals are difficult to detect as they can
easily blend in with benign network traffic. As such, a

5
Model Hyperparameter Search Space
Projected Quantum Kernel (RBF) Feature map Z, IQP, CNOT, Hamiltonian
Number of layers{1,2,3,4,5}
K-RDM{1}
Gamma (γ) [100µ,10]
ν[0,1]
Fidelity Kernel Feature map Z, IQP, CNOT, Hamiltonian
Number of layers{1,2,3,4,5}
ν(0,1]
TABLE I. Hyperparameter search space for quantum kernel methods. The description of the considered feature maps is given
in Appendix A. The number of layers ranged from 1 to 5. We only considered the single-qubit reduced density matrix for
the projected quantum kernels, andγis the hyperparameter of the projected quantum kernel.νis a hyperparameter of the
OCSVM model, which represents an upper bound on the fraction of training errors and a lower bound of the fraction of support
vectors. Curly brackets{}denote discrete values, while square brackets [] denote continuous ranges.
high-quality dataset is essential for network traffic anal-
ysis. The Stratosphere Research Laboratory is dedicated
to capturing real malware traffic and providing open-
access network traffic datasets to support the develop-
ment of robust machine learning models for malware
detection [37]. We first obtain normal network traffic
datasets from their platform to define what it is normal
for a typical user.
The laboratory also provides the CTU-13 dataset,
which is a beacon network traffic dataset consisting of
large-scale captures of real botnet activity mixed with
normal and background traffic. The dataset comprises
thirteen scenarios, each corresponding to a different bot-
net sample. In each scenario, a specific malware instance
was executed, using multiple protocols and performing
diverse actions. For each capture, the laboratory pro-
vides a list of external control IP addresses, which en-
abled us to filter out normal and background traffic from
the botnet-related traffic.
Since we are focused on unsupervised learning, the
training dataset only contains normal network traffic.
The beacon traffic is all kept in the test dataset.
Network traffic was aggregated into unique flows
(source IP address, destination IP address, protocol and
external port number), each described by a set of statis-
tical features. From this initial set, we retained a non-
redundant subset of 6 features, given in Table II; the
full feature list and the selection procedure, which is un-
supervised and uses no label information, are detailed
in Appendix B. The training set contains 200 randomly
sampled normal flows, while the testing set contains 1,000
flows, of which 457 are anomalous flows and 543 are nor-
mal flows. All malicious flows are included exclusively
in the testing set. For the simulator results, detection
scores are aggregated per unique source–destination pair,
keeping the lowest score of each pair, which gives 777
evaluation samples (255 anomalous and 522 normal); the
hardware results are evaluated on the 1,000 flows.
TABLE II. Feature set obtained from the feature engineering
procedure
F eature Name
Forward packets per second
Backward packets per second
Standard deviation of the FFT of forward traffic
Standard deviation of forward inter-arrival time
Standard deviation of packet lengths
Mean forward packet length
IV. RESUL TS
To evaluate the performance of the models, we use
two metrics: the area under the ROC curve (AUC) and
the F1 score. The AUC measures the model’s ability to
rank anomalies above normal instances across all deci-
sion thresholds, while the F1 score is the harmonic mean
of precision and recall at a fixed threshold. Because the
F1 score depends on which class is designated positive,
we report it twice, treating anomalies (A) and normal
instances (N) as the positive class in turn. In our view,
reporting both provides a balanced and transparent view
of model performance.
A. Classical baselines
Here, we present the performance of the classical
OCSVM on the malware dataset. Tuning the model
to maximise the NPD score selects an RBF kernel with
γ= 8.99 andν= 0.472.
TABLE III. Performance of the classical OCSVM on the mal-
ware dataset.
AUC F1 (A) F1 (N)
0.765 0.599 0.561
The performance of this configuration on the test set

6
TABLE IV. Best fidelity quantum kernel configuration found
for the three objectives on the dataset using the statevector
simulator. The GD objective depends only on the kernel ma-
trix, soνis not defined for that column (–).
NPD GD Pareto
Feature map Hamiltonian Hamiltonian Hamiltonian
Layers 2 1 5
ν0.322 – 0.266
gC→Q 4.297 7.14 5.94
NPD 2.34 0.592 0.72
TABLE V. Best projected quantum kernel configurations
found for the three objectives on the six features dataset using
the statevector simulator. The GD objective depends only on
the kernel matrix, soνis not defined for that column (–).
NPD GD Pareto
Feature map Z Hamiltonian IQP-style
Layers 5 1 5
ν0.385 – 0.104
γ2.37 9.99 0.000395
gC→Q 32.0 272 88.6
NPD 2.94 0.603 1.42
is summarised in Table III. The classical OCSVM at-
tains an AUC of 0.765, indicating a moderate ability to
rank anomalous flows above normal ones. The F1 scores
are more modest: 0.599 with anomalies as the positive
class and 0.561 with normal flows as the positive class.
Taken together, these results establish a non-trivial base-
line against which we assess the quantum kernels.
B. Fidelity and projected quantum kernels: NPD,
GD, and Pareto optimization
For the quantum kernel models, we performed a hyper-
parameter search to identify the optimal quantum kernel.
We are interested in three objectives: (1) the NPD score,
(2) GD between the quantum kernel and the reference
classical kernel, and (3) a Pareto frontier that jointly
maximises both the NPD and GD.
Table I gives the hyperparameter search space for both
the fidelity and projected quantum kernels. For each op-
timisation objective, we conducted 100 trials of hyper-
parameter search (150 for the fidelity kernel). The best
quantum model for each objective was then evaluated on
the test dataset. Using the statevector simulator, Tables
IV and V present the best configurations chosen for the
three objectives for the fidelity and projected quantum
kernels, respectively.
From Table IV, the Hamiltonian feature map is se-
lected across all three objectives for the fidelity quan-
tum kernel. Maximising the geometric difference (GD)
yields a maximum GD of 7.14. This demonstrates that
the fidelity quantum kernel achieves only small geometric
differences (GD) on this dataset. Hence, even when the
fidelity quantum kernel models perform well, a classical
model can match its performance due to these consis-
tently small GD values across all three objectives.
We observe a different behaviour, however, for the
projected quantum kernel, as shown in Table V. Max-
imising the GD yields a value of 272, which is greater
than
√
N= 14.14, demonstrating that, at least for this
dataset, the projected quantum kernel can lead to new
kernels that are distinct from the reference classical ker-
nel (the NPD-tuned RBF).
At first sight it may seem counter-intuitive that the
projected kernels, which discard all but the single-qubit
marginals of the encoded state, are the ones reaching
large GD values; the same effect was reported in Ref. [10],
where the GD was introduced. The reason is that GD
measures how well the classical kernel matrix can repro-
duce thegeometryof the quantum one, not how much
quantum information the kernel retains. The fidelity ker-
nel has no hyperparameter beyond the encoding circuit
itself: its entries are state overlaps Tr(ρ(x′)ρ(x)), and for
the shallow circuits considered here the resulting simi-
larity structure remains close to that of a smooth clas-
sical kernel on the same six features, which bounds the
attainable GD. The projected kernel instead composes
the encoding with an RBF kernel of tunable bandwidth
γacting on the reduced density matrices, so the opti-
miser can reshape the spectrum ofK Q directly. Largeγ
drivesK Q towards the identity: the diagonal is always
one, while the off-diagonal entries vanish, so no pair of
distinct points is regarded as similar. This is the regime
in which the reference kernelK C, whose bandwidth was
tuned for NPD and which retains non-trivial off-diagonal
structure, lies furthest fromK Q: forK Q =I N one has
g2 C→Q =∥K −1 C ∥∞, which is set by the smallest eigen-
value ofK C. The GD-maximising configuration indeed
sits at the top of theγrange (γ= 9.99,g C→Q = 272).
A large GD is therefore a property of the pair (K Q,K C)
and not evidence of quantum structure: a classical RBF
kernel with a larger bandwidth parameter would repro-
duce the same identity-like geometry. The same narrow-
bandwidth limit is the memorising regime in which gen-
eralisation deteriorates [9].
Figure 2 shows the Pareto fronts obtained when the
NPD and GD are maximised jointly, for both the fidelity
and projected quantum kernels on the statevector simu-
lator. For the fidelity kernel, the GD stays low through-
out (GD≲7), decreasing as the NPD increases, with
the knee at NPD = 0.725, GD = 5.936. This indicates
that, at least for this dataset, the fidelity kernel never
leaves the regime GD≪
√
Nin which a classical kernel
is guaranteed to match its performance. The projected
quantum kernel behaves very differently. Its front is a
broad, monotonic trade-off: the GD reaches≈110 at low
NPD and falls as the NPD improves, passing through the
knee at NPD = 1.421, GD = 88.6, down to GD≈20 at
NPD≈2. Even the front with the lowest GD remains

7
above the threshold, so every configuration along the pro-
jected front lies in the regime where the reference classical
kernel is not guaranteed to reproduce its geometry.
Table VI reports the test performance of the configu-
rations selected under each objective. Selecting for ge-
ometric difference neither helps nor substantially hurts
detection: the GD-maximising projected kernel, which
attains the largest GD in our study (g C→Q = 272),
reaches an AUC of 0.738, close to the classical baseline
(0.765) and to the NPD-selected projected kernel (0.777,
gC→Q = 32), despite an almost tenfold larger GD. The
best model overall is instead the NPD-selected fidelity
kernel, which outperforms the classical baseline with an
AUC of 0.840 at a GD of just 4.297. This shows that,
at least for this dataset, a large GD does not translate
into better performance. Figures 3 and 4 examine this
relation across all explored configurations.
Figure 3 plots the test AUC of every configuration ex-
plored during the GD-maximisation run against its ge-
ometric differenceg k. The fidelity kernels (blue) stay
confined to smallg k, below theg k =
√
N≈14.14 thresh-
old (green dashed), and reach the highest AUC in the
run (≈0.84), with multiple configurations also above the
classical baseline (orange dotted). The projected kernels
(red) extend tog k∼270, far beyond the threshold, but
their AUC shows no systematic trend withg k: beyond
the threshold they scatter between≈0.46 and 0.81, and
the poorest models in the run (AUC<0.5) mostly sit at
smallg k. A handful of projected configurations do oc-
cupy the upper-right region, combiningg k≫
√
Nwith
an AUC above the baseline, yet none of them reaches the
best fidelity kernels. The extreme configurations make
the point sharply: the GD-maximising projected ker-
nel (green) lands close to the baseline, no better than
configurations withg k ten times smaller, while the GD-
maximising fidelity kernel (yellow) is among the weakest
fidelity models at AUC≈0.67. Within the projected
family, configurations with small GD generally perform
poorly, but increasing the GD does not reliably improve
detection. The best model overall is a fidelity kernel, with
a GD below 7. This confirms that, on this dataset, a large
GD is not required for good detection performance.
Figure 4 shows the test AUC against the NPD for all
configurations of the NPD-maximisation run. The two
families are stratified: the fidelity kernels (blue) con-
centrate between AUC≈0.6 and 0.88, with many con-
figurations above the classical baseline (orange dotted),
while the projected kernels (red) are spread more widely,
from AUC≈0.33 to 0.86, and mostly lie below it, so
the attainable performance here depends strongly on the
kernel type. Within each family the relation is weak:
neither family shows a systematic trend in AUC over
0≲NPD≲2. The extremes nonetheless behave broadly
as the criterion intends. The largest-NPD fidelity config-
uration (yellow, AUC 0.840) and the largest-NPD pro-
jected configuration (green, AUC 0.777) are both above
the classical baseline, although neither is the single best
configuration of its family, with a few models reaching
AUC≈0.87 and≈0.86, respectively. The NPD is there-
fore best understood as a criterion that identifies a good
region of the hyperparameter space rather than as a fine-
grained ranking of configurations. This behaviour is con-
sistent with the original study of NPD [13]: across 38
benchmark datasets, NPD-guided Bayesian optimisation
of a classical OCSVM came close to the best attainable
AUC (84.0 versus 85.8, against 78.7 with default hyper-
parameters) and outperformed the other label-free crite-
ria tested, while the authors note that the highest NPD
did not always correspond to the best model. Our results
extend this picture to quantum kernels. The distinction
between identifying a good region and ranking configura-
tions within it is worth stating explicitly, since in a fully
unsupervised setting the NPD is the only selection signal
available; establishing how far label-free proxies track de-
tection performance is an open question that our results
suggest deserves dedicated study.
Returning to the joint optimisation, the fronts in Fig. 2
should be read as the non-dominated set reached after a
finite budget of 100 NSGA-II trials, not as converged ap-
proximations of the true Pareto frontier. More tellingly,
the single-objective TPE runs find configurations out-
side the joint fronts. The NPD-maximising projected
kernel (NPD = 2.94,g C→Q = 32.0, Table V) domi-
nates the high-NPD end of the projected front, where
NPD≈2 andg C→Q ≈20, and the GD-maximising
run reachesg C→Q = 272, above the front’s maximum
of about 120. Likewise, the GD-maximising fidelity con-
figuration (NPD = 0.592,g C→Q = 7.14, Table IV) dom-
inates the low-NPD end of the fidelity front. The joint
search has therefore not fully explored either extreme.
However, the separation between the two kernel families
relative to
√
Nholds across all three optimisation runs
and does not depend on the front being converged.
We also train the selected models with the IQM noisy
simulator, which contains information about the IQM
systems, like the number of qubits and their connectivity,
and several noise parameters (relaxation and dephasing
times, gate infidelities and readout errors). Comparing
the IQM noisy simulator results with the noiseless stat-
evector ones reveals that the impact of noise depends
less on the kernel family than on the circuit behind each
configuration. The fidelity kernel degrades moderately
under NPD selection, with its AUC falling from 0.840
to 0.790, and only slightly for the Pareto configuration,
from 0.812 to 0.798, while the shallow GD configuration
in fact improves, from 0.666 to 0.752. The projected ker-
nel is entirely unaffected under NPD and GD selection,
with AUCs of 0.777 and 0.738 in both settings, but drops
sharply for the Pareto configuration, from 0.782 to 0.647.
As a result, the clear advantage the fidelity kernel holds
on the statevector simulator under NPD selection (AUC
0.840 versus 0.777) narrows to a small margin under noise
(0.790 versus 0.777). Under noise, the best model is the
Pareto-selected fidelity kernel (0.798), closely followed
by the NPD-selected one, and both remain above the
classical baseline of 0.765. The robustness of the NPD-

8
0.0 0.2 0.4 0.6 0.8 1.0 1.2
NPD  (  better)
4.5
5.0
5.5
6.0
6.5
7.0GD
Fidelity Kernel
Pareto front
Knee  NPD=0.725  GD=5.936
0.6 0.8 1.0 1.2 1.4 1.6 1.8 2.0
NPD  (  better)
20
40
60
80
100GD
PQK
Pareto front
Knee  NPD=1.421  GD=88.617
GD threshold ( N = 14.14)
FIG. 2. Pareto fronts of the fidelity (blue) and projected (red) quantum kernels under joint maximisation of the NPD and GD,
evaluated on the statevector simulator. Circles mark the non-dominated configurations of each front; stars mark the selected
knee points. The fidelity kernel maintains a low GD across the front, whereas the projected kernel trades a high GD at low
NPD for improved NPD, exposing the tension between the two objectives. Each front contains only the configurations that
remained non-dominated during the optimisation, which is why the two kernels contribute different numbers of points.
TABLE VI. Performance of the optimised quantum kernels obtained from the optimisation of the three objectives: NPD, GD
and Pareto frontier using the statevector simulator. We re-run the optimal hyperparameters selected by each optimisation
using the IQM noisy simulator; the OCSVM parameterνwas additionally re-tuned on the noisy simulator by maximising the
NPD. The classical OCSVM baseline achieves AUC = 0.765. The best value of each metric is shown in bold.
Method NPD GD Pareto (NPD & GD)
AUC F1(A) F1(N) AUC F1(A) F1(N) AUC F1(A) F1(N)
Statevector Simulator
Fidelity0.8400.657 0.715 0.666 0.4940.800 0.8120.6710.773
Projected 0.777 0.599 0.563 0.738 0.542 0.340 0.782 0.638 0.736
IQM Noisy Simulator
Fidelity 0.790 0.600 0.582 0.752 0.5820.630 0.7980.600 0.576
Projected 0.7770.6090.554 0.738 0.541 0.334 0.647 0.525 0.620
and GD-selected projected kernels is consistent with their
shallow circuits—a separableZfeature map and a single-
layer Hamiltonian encoding—and their reliance on local
observables, whereas the Pareto-selected projected ker-
nel uses a five-layer entangling IQP-style encoding, whose
depth makes it far more sensitive to noise.
Overall, these results show that the best-performing
model in our study is a fidelity quantum kernel, the
NPD-selected Hamiltonian encoding (AUC 0.840), but
its geometric difference (g k ≲7) remains well below√
N≈14.14, so a classical kernel cannot be ruled out
from matching its performance. Conversely, several pro-
jected quantum kernels combine a large geometric differ-
ence with an AUC above the classical baseline as seen
in Fig. 3. None of them, however, reaches the best-
performing fidelity kernel, whose performance a classical
kernel may in principle recover. Performance and geo-
metric separation are therefore never achieved together
at the top of the ranking: the kernels that are clearly
distinct from the classical reference are not the best de-
tectors, and the best detector is not clearly distinct. At
least for this dataset, we thus find no quantum kernel in
our search space that both certifiably departs from the
classical reference and outperforms every model a classi-
cal kernel could plausibly reach.
C. Hardware results
We complete our study with a benchmark of the best
quantum models on IQM’s QPUs to investigate the ef-
fect of noise on quantum kernel calculations and corre-
sponding performance. We used IQM Garnet, a 20-qubit
QPU based on superconducting transmon qubits. The

9
0 50 100 150 200 250
Geometric Difference gk
0.4
0.5
0.6
0.7
0.8T est AUC
Geometric Difference vs T est AUC
across all hyperparameter configurations (statevector)
Fidelity kernel
Projected QK
Largest GD (Fidelity)
Largest GD (PQK)
gk = N 14.14
Classical baseline AUC = 0.765
FIG. 3. Test AUC versus geometric differenceg k for all
hyperparameter configurations evaluated during the GD-
maximisation run (statevector simulation). Blue: fidelity ker-
nels; red: projected quantum kernels. The green dashed line
marksg k =
√
N≈14.14, below which a classical kernel is
guaranteed to match the quantum model; the orange dotted
line is the tuned classical OCSVM baseline (AUC = 0.765).
Fidelity kernels stay below the threshold yet reach the highest
AUC in the run (≈0.84), whereas projected kernels extend to
gk∼270 with an AUC that shows no systematic trend with
gk. A few projected configurations combineg k≫
√
Nwith
an AUC above the baseline, but none reaches the best fidelity
kernels, and the two largest-GD models (yellow, green) per-
form at or below the baseline.
0.0 0.5 1.0 1.5 2.0 2.5 3.0
NPD  (  better)
0.4
0.5
0.6
0.7
0.8
0.9T est AUC
NPD vs T est AUC across all hyperparameter configurations
(statevector simulation)
Fidelity kernel
Projected QK
Largest NPD (Fidelity)
Largest NPD (PQK)
Classical baseline AUC = 0.765
FIG. 4. Test AUC versus NPD for all hyperparameter config-
urations evaluated during the NPD-maximisation run (stat-
evector simulation). Blue: fidelity kernels; red: projected
quantum kernels. The orange dotted line marks the tuned
classical OCSVM baseline (AUC = 0.765). Fidelity kernels
concentrate at higher AUC, with a substantial fraction above
the baseline, while projected kernels spread widely between
AUC≈0.33 and 0.86 and mostly lie below it. Within each
family the NPD–AUC relation is weak. The largest-NPD con-
figuration of each family (yellow: fidelity; green: projected)
lies above the baseline, at AUC = 0.840 and 0.777 respec-
tively.
qubits are arranged in a square lattice (see Fig. 5) and
connected by tunable couplers (more details about the
coupling scheme can be found in [38]). We performed
two different experiments, using both fidelity and pro-
jected kernels and the optimal hyperparameters given by
the optimization of the NPD score. In fact, this choice
allowed us to have the best balance between quality of
the results and practical implementation of the circuits
on current hardware (i.e., shallower circuits). The results
for the three performance metrics considered in this work
are presented in Table VII. The hardware results are com-
puted on the 1,000 test flows without per-pair aggrega-
tion, and are therefore not directly comparable to Table
VI. For the projected kernel,νwas chosen as the value
maximising the test scores, so its figures should be read
as optimistic.
For fidelity kernels we implemented the Hamiltonian fea-
ture map with 2 layers (i.e. 2 Trotter steps - see App. A
for more details) as reported in Table IV. The optimal
way to choose the qubits on IQM Garnet QPU is high-
lighted in Fig. 5: the nearest-neighbour interactions of
the Hamiltonian suggest the use of physically connected
qubits in a 1D chain to optimize the depth of the tran-
spiled circuits. Kernel entries in Eq. 1 can be calculated
with theadjointmethod (see e.g. [11] and references
therein), which doubles the depth of the circuit, but does
not need auxiliary qubits. The number of circuits to run
on the QPU to construct the training kernel matrix scales
asO(N 2), whereN= 200 in our case; the number of
shots per circuit was fixed to 1000. To take into account
measurement errors, we applied readout error mitigation
to the probability distribution of bitstrings obtained with
the QPU [39, 40]. Finally, following [11], we further ap-
plied regularization techniques to ensure positivity of the
kernel matrix and applied mitigation techniques tailored
to depolarizing noise. Both the AUC score and the F1(N)
decrease considerably when running the fidelity kernel on
real hardware, while the F1(A) only differs slightly from
the result in Table VI. In this case, more advanced error
mitigation and suppression techniques should be applied
to improve the results, but this goes beyond the scope of
the current work.
In the case of projected kernels, the data-encoding cir-
cuit is the Z separable map with 5 layers (see Table V).
To calculate the single-qubit reduced density matrices in
Eq. 2 on the QPU, we used the classical shadows protocol
introduced in [41]. In this case, the number of circuits to
evaluate scales linearly in the number of data. Neverthe-
less, we limited the size of the shadow to 100, as the the-
oretical bounds in [41] are not practically implementable
on hardware (and are also expected to be much smaller
in practice). The results reported in Table VII show that
the AUC metric is lower than the simulated value, while
the F1 scores are higher. We believe that this behavior is
due to the small size of the shadow rather than noise on
the QPU, as the Z feature map only includes single-qubit
gates and the circuits have low depth. To get higher pre-
cision for these results, one could use a bigger shadow

10
FIG. 5. Layout of the IQM Garnet QPU. The color map in-
dicates single and two-qubit gate errors (darker=higher error,
lighter=lower error). We highlight the optimal way to choose
a qubit patch to implement a Hamiltonian evolution feature
map with nearest-neighbour interactions. The specific patch
needs to be adjusted depending on re-calibration of the QPU.
size or apply a more recent protocol, multi-shots clas-
sical shadows, which has proven advantageous for Pauli
measurements [42] over the original method.
The results presented in this section leave room for future
improvements, not only on the hardware run optimiza-
tion side, but also on the search for optimal hyperparam-
eters under more hardware-realistic noise models.
TABLE VII. Performance of the quantum kernels obtained
from the IQM Garnet QPU using the optimal configurations
for the hyperparameters as given by the NPD score; for the
projected kernel,νwas selected to maximise the test scores.
Method Feature Map AUC F1(A) F1(N)
Fidelity Hamiltonian 0.5320.6400.151
Projected Z0.6120.6300.656
V. DISCUSSION
The picture that emerges from our experiments is con-
sistent but not the one a search for quantum advantage
would hope for. The two objectives of our protocol are,
on this dataset, in direct tension. Fidelity kernels sit
at one end: NPD-guided selection finds a Hamiltonian-
evolution feature map that improves on the tuned clas-
sical OCSVM baseline (AUC 0.840 versus 0.765), yet
its geometric difference never exceedsg C→Q≃7, below√
N= 14.14. By the criterion of Ref. [10], this separation
is too small to certify the improvement as quantum: the
bound allows the reference classical kernel to close the
gap with more training data (up to a factorg 2≈49 in
the worst case), so the improvement carries no evidence
of quantum origin.
Projected kernels sit at the other end, reachingg C→Q
up to 272. Unlike in a purely negative picture, several of
them also detect better than the classical baseline. How-
ever, none of them beats the best fidelity kernel. The
best-performing knee point of the Pareto optimisations
is the fidelity kernel (AUC 0.812), which recovers most
of the NPD-selected performance (0.840) but stays in the
low-GD regime. The projected knee point reaches a lower
AUC (0.782), though still the highest of the three pro-
jected selections, at a GD well above
√
N; it remains
below the best fidelity kernel and is the projected config-
uration most sensitive to noise (AUC 0.647 on the IQM
noisy simulator).
This is the behaviour that the theoretical literature an-
ticipates. A large geometric difference is necessary but
not sufficient for a prediction advantage [10, 12]: it certi-
fies that the quantum feature space is not well approxi-
mated by the chosen classical reference, but says nothing
about whether the inductive bias it encodes is the one this
task rewards. Our results are a concrete instance of that
gap on real data, and they suggest that the missing ingre-
dient is alignment between the feature map and the struc-
ture of network flows, not more expressivity. Trainable
and data-dependent embeddings [11, 33, 43] offer a route
to such alignment; in a fully unsupervised setting, the
NPD could play the role that label-based kernel-target
alignment plays in those works. The largest GD values in
our study are also the least informative: they are reached
by the projected kernel at the top of its bandwidth range,
whereK Q approaches the identity (Sec. IV B), so a large
geometric difference can be produced by a single classical
hyperparameter [9] and, on its own, is weak evidence of
useful quantum structure.
Two aspects of the protocol itself are worth separat-
ing from these negative findings. First, NPD behaves as
a usable label-free selection criterion for quantum ker-
nels: the NPD-optimised configuration gave the best-
performing model in two of the four settings (statevector
fidelity and IQM projected) and came within 0.01 AUC
of the best in the other two (Table VI), which is the prop-
erty one needs when labelled validation data is unavail-
able by construction. This should not be read as a mono-
tonic relation between NPD and detection quality, within
a family the two are only weakly related (Fig. 4), but as
evidence that maximising NPD lands in a good region
of the search space. Second, making GD a co-objective
rather than a post-hoc diagnostic is what exposes the
trade-off at all. A study reporting only NPD would have
announced a quantum kernel beating the classical base-
line; one reporting only GD would have announced a
kernel outside the reach of the reference classical kernel.
Both statements are true here, and neither on its own is
informative.
The scope of these conclusions is limited in ways that
matter. They rest on a single dataset withN= 200 train-

11
ing flows and six engineered features, a regime dictated
by theO(N 2) circuit cost of fidelity kernels on hardware;
the
√
Nthreshold is itself a function of this sample size,
and a larger training set would raise the
√
Nthreshold
that the projected kernels currently exceed, although the
geometric difference itself also depends onN. The Pareto
fronts also reflect a finite budget of 100 trials per objec-
tive (150 for the fidelity kernel). The classical reference
in the GD is the best kernel we found within a bounded
family, so the separation is relative to that family and
not to classical methods in general. Finally, the feature
maps were taken from the literature rather than designed
for network traffic, which is precisely the design freedom
that our results identify as the binding constraint. In
simulation the fidelity kernel outperforms the projected
kernel (AUC 0.840 versus 0.777), but on IQM Garnet the
situation is reversed (AUC 0.532 versus 0.612, on a differ-
ent evaluation set, Sec. IV C): projected kernels degrade
much less under hardware noise, consistent with shal-
lower circuits and their reliance on local observables, al-
though neither yet reaches the classical baseline (0.765).
We therefore read this work less as a negative result
about quantum kernels on cybersecurity data than as a
blueprint with an honest first application. The natu-
ral continuations are to construct feature maps informed
by the periodicity and burstiness that characterise bea-
coning, rather than sampling generic encodings; to push
Nupward using tensor-network or shadow-based kernel
approximations [41] so that the
√
Ncriterion becomes
harder to satisfy trivially; and to apply the NPD–GD
front to other unsupervised problems where labels are
structurally unavailable. Whether any quantum kernel
eventually occupies the upper-right corner of that front
remains open; our contribution is a protocol that will
make it visible when one does.
ACKNOWLEDGMENTS
This work was supported by the R´ egion ˆIle-de-
France under the Pack Quantique programme (Grant
No. 23002667). The authors gratefully acknowledge this
financial support.
The authors thank the Allianz SE Cybersecurity and
NextGen IT Think Tank, which led this collaboration,
for domain expertise and critical review of the findings’
relevance to industry security practice. The research was
carried out by Multiverse Computing and IQM Quan-
tum Computers using only publicly available data; no
Allianz data, networks or production environments were
examined. This exploratory work implies no control as-
sessment, deployment, procurement or endorsement de-
cision, and the views expressed are those of the authors
and do not necessarily represent Allianz or its affiliates.
[1] J. Biamonte, P. Wittek, N. Pancotti, P. Rebentrost,
N. Wiebe, and S. Lloyd, Nature549, 195 (2017).
[2] M. Cerezo, G. Verdon, H.-Y. Huang, L. Cincio, and P. J.
Coles, Nature computational science2, 567 (2022).
[3] Y. Wang and J. Liu, Reports on Progress in Physics87,
116402 (2024).
[4] M. Larocca, S. Thanasilp, S. Wang, K. Sharma, J. Bia-
monte, P. J. Coles, L. Cincio, J. R. McClean, Z. Holmes,
and M. Cerezo, Nature Reviews Physics7, 174 (2025).
[5] V. Havl´ ıˇ cek, A. D. C´ orcoles, K. Temme, A. W. Harrow,
A. Kandala, J. M. Chow, and J. M. Gambetta, Nature
567, 209 (2019).
[6] P. Rebentrost, M. Mohseni, and S. Lloyd, Physical review
letters113, 130503 (2014).
[7] S. Thanasilp, S. Wang, M. Cerezo, and Z. Holmes, Nature
Communications15, 5200 (2024).
[8] P. Kairon, J. J¨ ager, and R. V. Krems, arXiv preprint
arXiv:2501.07433 (2025).
[9] R. Shaydulin and S. M. Wild, Physical Review A106,
042407 (2022).
[10] H.-Y. Huang, M. Broughton, M. Mohseni, R. Babbush,
S. Boixo, H. Neven, and J. R. McClean, Nature Commu-
nications12, 2631 (2021).
[11] T. Hubregtsen, D. Wierichs, E. Gil-Fuster, P.-J. H.
Derks, P. K. Faehrmann, and J. J. Meyer, Physical Re-
view A106, 042431 (2022).
[12] J. K¨ ubler, S. Buchholz, and B. Sch¨ olkopf, Advances in
Neural Information Processing Systems34, 12661 (2021).
[13] W. Dai and J. Fan, inThe Thirteenth International Con-
ference on Learning Representations (ICLR)(2025).
[14] M. C. Caro, H.-Y. Huang, M. Cerezo, K. Sharma,
A. Sornborger, L. Cincio, and P. J. Coles, Nature com-
munications13, 4919 (2022).
[15] Y. Liu, S. Arunachalam, and K. Temme, Nature Physics
17, 1013 (2021).
[16] T. Muser, E. Zapusek, V. Belis, and F. Reiter, Physical
Review A110, 032434 (2024).
[17] L. Slattery, R. Shaydulin, S. Chakrabarti, M. Pistoia,
S. Khairy, and S. M. Wild, Physical Review A107,
062417 (2023).
[18] X. Wang, Y. Du, Y. Luo, and D. Tao, Quantum5, 531
(2021).
[19] B. Sch¨ olkopf, J. C. Platt, J. Shawe-Taylor, A. J. Smola,
and R. C. Williamson, Neural Computation13, 1443
(2001).
[20] F. T. Liu, K. M. Ting, and Z.-H. Zhou, in2008 Eighth
IEEE International Conference on Data Mining(IEEE,
2008) pp. 413–422.
[21] G. E. Hinton and R. R. Salakhutdinov, Science313, 504
(2006).
[22] G. Barru´ e and T. Quertier, inJoint European Confer-
ence on Machine Learning and Knowledge Discovery in
Databases (ECML PKDD)(Springer, 2023) pp. 245–260,
arXiv:2305.09674 [cs.CR].
[23] E. Payares and J. C. Mart´ ınez-Santos, inQuantum Com-
puting, Communication, and Simulation (SPIE), Vol.
11699 (SPIE, 2021) pp. 35–43.
[24] R. Kumar and M. Swarnkar, Journal of Network and
Computer Applications234, 104072 (2025).
[25] T. Cultice, M. S. H. Onim, A. Giani, and H. Thap-

12
liyal, in2024 IEEE Computer Society Annual Sympo-
sium on VLSI (ISVLSI)(IEEE, 2024) pp. 619–624,
arXiv:2409.04935 [quant-ph].
[26] K. Tscharke, S. Issel, and P. Debus, in2023 IEEE
International Conference on Quantum Computing and
Engineering (QCE), Vol. 1 (IEEE, 2023) pp. 611–620,
arXiv:2308.00583 [quant-ph].
[27] M. Hdaib, S. Rajasegarar, and L. Pan, Quantum Machine
Intelligence6, 10.1007/s42484-024-00163-2 (2024).
[28] D. Pranji´ c, F. Kn¨ able, P. Kunst, D. Kutzias, D. Klau,
C. Tutschku, L. Simon, M. Kraus, and A. Abedi, arXiv
preprint arXiv:2411.16970 (2024), arXiv:2411.16970
[quant-ph].
[29] J. Gama, I. ˇZliobait˙ e, A. Bifet, M. Pechenizkiy, and
A. Bouchachia, ACM Computing Surveys46, 44 (2014).
[30] A. Shalaginov, K. Franke, and X. Huang, in18th In-
ternational Conference on Computational Intelligence in
Security Information Systems. WASET(2016).
[31] M. Schuld, arXiv preprint arXiv:2101.11020 (2021),
arXiv:2101.11020 [quant-ph].
[32] A. Bounsiar and M. G. Madden, in2014 interna-
tional conference on information science & applications
(ICISA)(IEEE, 2014) pp. 1–4.
[33] J. R. Glick, T. P. Gujarati, A. D. Corcoles, Y. Kim,
A. Kandala, J. M. Gambetta, and K. Temme, arXiv
preprint arXiv:2105.03406 (2021).
[34] T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama,
inProceedings of the 25th ACM SIGKDD international
conference on knowledge discovery & data mining(2019)
pp. 2623–2631.
[35] K. Deb, A. Pratap, S. Agarwal, and T. Meyarivan,
IEEE Transactions on Evolutionary Computation6, 182
(2002).
[36] S. Watanabe, arXiv preprint arXiv:2304.11127 (2023).
[37] Stratosphere Lab, Stratosphere normal traffic datasets
(2025).
[38] F. Marxer, A. Veps¨ al¨ ainen, S. W. Jolin, J. Tuorila,
A. Landra, C. Ockeloen-Korppi, W. Liu, O. Ahonen,
A. Auer, L. Belzane,et al., PRX Quantum4, 010314
(2023).
[39] F. B. Maciejewski, Z. Zimbor´ as, and M. Oszmaniec,
Quantum4, 257 (2020).
[40] S. Bravyi, S. Sheldon, A. Kandala, D. C. Mckay, and
J. M. Gambetta, Physical Review A103, 042605 (2021).
[41] H.-Y. Huang, R. Kueng, and J. Preskill, Nature Physics
16, 1050 (2020).
[42] Y. Zhou and Q. Liu, Quantum7, 1044 (2023).
[43] S. Altares-L´ opez, A. Ribeiro, and J. J. Garc´ ıa-Ripoll,
Quantum Science & Technology6, 045015 (2021).
[44] D. Shepherd and M. J. Bremner, Proceedings: Mathe-
matical, Physical and Engineering Sciences , 1413 (2009).
[45] M. J. Bremner, R. Jozsa, and D. J. Shepherd, Proceed-
ings: Mathematical, Physical and Engineering Sciences ,
459 (2011).
[46] F. Nielsen, inIntroduction to HPC with MPI for Data
Science(Springer, 2016) pp. 195–211.
[47] P. J. Rousseeuw, Journal of computational and applied
mathematics20, 53 (1987).
Appendix A: Data-encoding feature maps
We considered four different feature maps for encoding
classical data into quantum states; in the following, the
input dataxis an-dimensional vector andx j is thej-th
entry ofx;Ldenotes the number of layers.
Z feature mapThis feature map applies a wall of
Hadamard gates and then parametrized Z-rotations to
each qubit individually. It contains no entangling gates,
thus the state at the end of the circuit is fully separable
when applied to|0 n⟩state fornqubits:
|ϕ(x)⟩=




n⨂
j=1
e−iZj
xj
2

H⊗n


L
|0n⟩,(A1)
IQP-style feature mapThis embedding was pro-
posed in [5], where the authors conjecture that the inner
product resulting from this encoding is hard to compute
classically, suggesting the possibility for a quantum ad-
vantage. The data-dependent state is defined as:
|ϕ(x)⟩=
[
UZ(x)H⊗n]L |0n⟩,(A2)
whereH ⊗n applies Hadamard gates to all qubits in par-
allel, and
UZ(x) = exp

−i 2


n∑
j=1
xjZj +
∑
j<j ′
xjxj′ZjZj′



,
(A3)
withZ j denoting the Pauli-Zoperator acting on the
j-th qubit. The name IQP refers toinstantaneous quan-
tum polynomial-timecircuits [44, 45]: sinceU Z(x) is gen-
erated exclusively by Pauli-Zterms, it is diagonal in the
computational basis and all of its gates mutually com-
mute. They can therefore be applied in any order, or
formally as a single simultaneous (hence “instantaneous”)
interaction, so the data-dependent part of the circuit car-
ries no temporal structure. The only non-commuting el-
ements are the two data-independent Hadamard walls,
which are what prevent the whole circuit from being clas-
sically simulable by sampling the diagonal generator di-
rectly.
Hamiltonian evolution feature mapThis feature
map is inspired by quantum many-body dynamics and is
implemented using a trotterization of the time evolution.
It requiresn+ 1 qubits to embednfeatures and is de-
fined as follows (see [10] for more details and references
therein):
|ϕ(x)⟩=
[ n∏
j=1
exp
(
−it Txj ( XjXj+1 +Y jYj+1 +Z jZj+1 ))
]T n+1⨂
j=1
|ψj⟩.(A4)
whereX j,Y j, andZ j are the paulis acting on thej-
th qubit, and|ψ j⟩are fixed Haar-random single-qubit

13
quantum states.tandTare hyperparameters represent-
ing the total evolution time and the number of Trotter
steps, respectively.
CNOT feature mapWe also consider a hardware-
inspired feature map based on single-qubit rotations
and nearest-neighbour entanglement using controlled-X
(CNOT) gates. For a classical input vectorx, the corre-
sponding quantum state is prepared as
|ϕ(x)⟩=
[ L∏
ℓ=1


n∏
j=1
CNOTj,j+1




n∏
j=1
RZ(xj)

H⊗n
]
|0n⟩.(A5)
whereLdenotes the number of layers,His the Hadamard
gate,R Z(xj) is a rotation around theZaxis applied to
thej-th qubit, and CNOT j,j+1 denotes a controlled-X
gate acting on neighboring qubits in a ladder-like topol-
ogy.
Appendix B: F eature engineering and feature
selection
Network traffic was aggregated into unique flows de-
fined by the tuple consisting of thesource IP address,
destination IP address,external destination port number,
andprotocol. For each unique flow, statistical features
were then extracted. The objective here is to construct
an effective set of features capable of capturing the com-
plex patterns that separate benign network flows from
malicious ones. The features generated for each flow are
summarised below.
Flow duration.Total flow duration (seconds).
Packet counts.Total, forward, backward packets.
Packet length statistics.Mean, std. dev., min, max, me-
dian, skewness, MAD (overall/fwd/bwd).
Flow rates.Packets/s, bytes/s.
Inter-arrival time (IAT).Min, max, mean, std. dev., total,
coeff. of variation (overall/fwd/bwd).
Time-delta robustness.Median, MAD, skewness.
Frequency-domain (FFT).Mean, std. dev., max (over-
all/fwd/bwd).
Directional durations.Forward and backward flow dura-
tion.
Directional rates.Fwd/bwd packets/s and bytes/s.
Directional ratios.Downstream/upstream (bwd-to-fwd)
packet ratio.
Next, we need to select an optimal set of features from
this list. This was achieved using hierarchical cluster-
ing [46]. The process can be described in two steps: 1)
divide the large set of features into smaller groups of sim-
ilar ones and 2) reduce the number of redundant features
by selecting the most representative feature from each
group.
We stress that this criterion is unsupervised: no label
information enters the feature selection. We selected the
optimal number of clusters for the hierarchical clustering
using the silhouette score, which provides a quantitative
measure of cluster quality by balancing intra-cluster co-
hesion and inter-cluster separation [47]. Specifically, we
evaluated candidate numbers of clusterskby cutting the
hierarchical dendrogram intokclusters and computing
the silhouette score for each partition. The value ofk
that maximised the silhouette score was chosen as the
optimal number of clusters, as it corresponds to the par-
tition with the best overall separation structure. The
motivation for this approach is that hierarchical cluster-
ing does not inherently determine the optimal cut level,
and the silhouette score offers an objective, data-driven
criterion to guide this choice.
From each cluster we then keep the medoid, i.e. the
feature with the smallest average correlation distance to
the other features in its cluster. This reduces the feature
set to the 6 features listed in Table II.
