---
title: Can Entanglement-Induced Feature-Map Designs Improve Projected Quantum Kernels?
url: https://arxiv.org/abs/2610.31260
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Ravi Kumar Jha
- Hsuan-Yin Lin
- Eirik Rosnes
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.31260
pages: 6
chars: 33086
fetched_at: '2026-11-08T13:31:22+00:00'
kb_version: 1
---

# Can Entanglement-Induced Feature-Map Designs Improve Projected Quantum Kernels?

Can Entanglement-Induced Feature-Map Designs
Improve Projected Quantum Kernels?
Ravi Kumar Jha, Hsuan-Yin Lin, and Eirik Rosnes
Simula UiB, N–5006 Bergen, Norway
Emails:{ravi, lin, eirikrosnes}@simula.no
Abstract—Projected quantum kernels (PQKs) have emerged
as a notable approach to circumvent the hardness of machine
learning tasks arising from the exponential dimensionality of
the quantum Hilbert space. However, recent PQK studies often
rely heavily on extensive classical hyperparameter tuning of the
radial basis function (RBF) kernel parameter and the support
vector machine regularization parameter. The extensive tuning
can mask the true representational power of the underlying
PQKs induced by quantum feature maps, which has not been
explored in detail. Thus, this work aims to expose the structural
capabilities of PQKs by isolating and evaluating their native
inductive bias through comparisons between untuned and tuned
PQKs against the RBF baseline. Furthermore, we propose novel
quantum feature maps that leverage two-qubit entanglement
to capture multivariate correlations in IoT data. The results
show that extensive tuning can lead to competitive performance
architectures, while our proposed entanglement topologies exhibit
a significantly stronger native inductive bias. This reveals that
superior quantum architectural design can yield structurally bet-
ter PQKs with improvements arising from quantum-mechanical
properties rather than from classical hyperparameter tuning.
I. INTRODUCTION
Quantum computing (QC) for machine learning (ML), also
known as quantum machine learning (QML), has emerged as
a promising research direction for ML tasks [1], [2]. This
development is primarily driven by the need for computa-
tionally efficient paradigms to address complex systems, data
modeling and simulation, data structures and design patterns,
and energy estimation. QML leverages intriguing quantum-
mechanical phenomena, such as information processing using
quantum bits (qubits), superposition, and entanglement [3].
Notable algorithms have been developed over the last decade
to enhance existing ML capabilities by leveraging these
quantum properties. In the vicinity of ML, algorithms such
as quantum neural networks, quantum principal component
analysis (PCA), and quantum kernels have been developed
to explore various advancements [4]. This work focuses on
quantum kernels.
The mathematical framework of quantum kernels is straight-
forward and aligns with kernel theory, in which information
is processed by mapping it to state vectors living in a large
quantum feature space [5], [6]. The high-dimensional feature
vectors need not be computed explicitly, and instead, a quan-
tum device directly evaluates the inner products of quantum
states. This overlap forms a quantum kernel, providing the
similarity measure that drives kernel-based methods [4]–[6].
The authors acknowledge the financial support provided in part by the
SURE-AI Centre Grant 357482, Research Council of Norway.
One ongoing challenge in QML is how to effectively encode
classical inputs into quantum states through aquantum feature
map, or simply afeature map[5]–[7]. In kernel methods,
feature maps are crucial because kernel performance depends
on how effectively they capture task-relevant structure through
pairwise inner products of mapped inputs. A feature map
typically consists of single- and two-qubit gates together with
entangling operations [5]–[8]. An early demonstration of quan-
tum advantage was achieved using a quantum fidelity kernel
on synthetic data, executed on an IBM quantum device. This
work remains influential in introducing theZZfeature map[9].
This has inspired many useful formulations of quantum kernels
in various applications, such as solving differential equations,
hybrid neuro-inspired modeling, and data analysis [1], [10]–
[12].
Standard quantum kernels assess data similarity by comput-
ing the global inner product between quantum states in a high-
dimensional Hilbert space. However, as the number of qubits
increases, these global states become increasingly orthogonal,
causing the kernel values of data points to decay exponentially
toward zero, calledexponential concentration[13]. Thus,
exponential concentration severely hinders learning by dimin-
ishing the variance of the kernel matrix, making data points
nearly indistinguishable and thereby limiting the model’s
predictive capability. To mitigate the exponential scaling of
the Hilbert space, theprojected quantum kernel(PQK) was
introduced [14]. Instead of relying on global state overlap, a
PQK projects the quantum state back into a lower-dimensional
classical feature space via local observable measurements, pre-
serving relevant nonlinear quantum correlations while main-
taining the discriminative power required for effective kernel
estimation [14]–[16]. However, the PQK formulation appears
to rely heavily on extensive classical hyperparameter tuning
of theradial basis function (RBF)kernel parameterγand
the support vector machine (SVM) regularization parameter
ξ. Therefore, this work critically examines current literature
practices by addressing the following key objectives:
•To assess the extensive classical tuning influences on both
PQKs and the RBF, we isolate their native inductive bi-
ases by comparing their tuned and untuned performances.
•To introduce two novel entanglement-induced feature
maps that achieve empirical gains while demonstrating
reduced hyperparameter sensitivity over untuned PQKs.
To this end, we evaluate the models under two distinct
settings: untuned baselines and robustly tuned models. This
arXiv:2610.31260v1  [quant-ph]  22 Oct 2026

−2 0 2 4
−2
0
2
4
6
Principal Component 1
Principal Component 2
Nonoccupied (56.5%)
Occupied (43.5%)
Fig. 1. An illustration of the complex class separation of IoT data using PCA.
framework ensures reliable assessment, aiming to provide a
missing understanding of how structurally aligned quantum
topologies can natively separate complex data and improve
understanding of PQK models.
II. PRELIMINARIES
A. Notation
NandRdenote the sets of positive integers and reals,
respectively. Moreover,[a]≜{1,2, . . . , a}fora∈N. Vectors
are boldfaced, e.g.,x. Matrices and sets are represented by
capital sans serif letters and calligraphic uppercase letters,
respectively, e.g.,XandX. The single-qubit rotation operators
about thex-,y-, andz-axes are denoted byR X,R Y, andR Z,
respectively, andHis the Hadamard gate. We useρto denote
a density operator, andtr(X)andtr A(X)for the trace ofX
and the partial trace ofXover a subsystemA, respectively.
Tensor products of Pauli operators are written without the
tensor-product symbol, e.g.,XXdenotesX⊗X.
B. Internet of Things Data
Internet of Things (IoT) platforms capture real-time en-
vironmental changes across a network of connected devices
and sensors. The idea of using IoT data in this work is to
extend the real-world applications of current quantum mod-
els beyond synthetic datasets, demonstrating how a quantum
method handles complex, nonlinear correlations in sensor
networks. Moreover, the inclusion of this data facilitates a fair
comparison with ML models, as it does not require any feature
reduction or selection method, given the moderate sample
size and dimensionality, and it has previously been used in
QML work [16], [17]. The data is open access on the IoT
platform COGITO [16]. The dataset containsN= 2865sam-
ples and the six featuresilluminance,blinds,lamps,relative
humidity (rh),carbon dioxide (CO2), andtemperature (temp)
for classifying room occupancy. Standard data pre-processing
was used to remove irrelevant variables, such as levels and
timestamps, and redundant records. The binary classification
task ofoccupied vs nonoccupiedwas normalized before being
used in distinct PQKs and classical models. Fig. 1 visualizes
the IoT data using the first two principal components obtained
by PCA. The plot shows that the two classes are partially
separable but remain noticeably overlapping, illustrating the
nontrivial structure of the classification task.
C. Data Encoding
Encoding classical inputs into quantum states, commonly
referred to asdata encoding, is a critical step in QML. A data-
encoding scheme that maps classical feature inputs into high-
dimensional quantum states is known as a quantum feature
map. In a basic formulation, ad-dimensional feature inputx∈
Rd is encoded into ann-qubit quantum state|ϕ(x)⟩through
a data-dependent unitaryU(x), namely,|ϕ(x)⟩≜U(x)|0⟩ ⊗n.
The corresponding density matrix is denoted byρ(x). This
encoding via feature maps transforms the input data into a
high-dimensional Hilbert space. Finding a suitable feature map
is therefore a central component of quantum kernel models,
where predictions can be made through kernel evaluations [5],
[9], [12], [13]. In this work, following the IoT setting in [16],
the number of qubits is chosen to be the same as the number
of IoT input features, namelyn= 6. In general, however,
the input dimension, the number of qubits, and the projected
feature dimension need not coincide.
D. Projected Quantum Kernel
PQKs are a class of quantum models that project quan-
tum states into an approximate classical space [14]. In the
PQK framework, rather than computing the fidelity between
quantum states, the output quantum states are measured to
extract the expectation values of Pauli observables, further
discussed in Sec. III. Fig. 2 shows a schematic design of the
PQK formulation. The original idea of this formulation was
to address the challenges posed by the exponential dimension-
ality of the quantum Hilbert space endured by the standard
quantum kernel approach [13]–[16]. The PQK formulation
demonstrated merit in computational efficiency, with linear
scaling of the required QC resources. However, PQKs still
utilize the quantum Hilbert space and therefore can still pose
a hardness barrier to classical simulation. We use the PQK
formulation from [16, eq. (14)] (see also [14, Supplementary
information]):
κPQK(x,x ′)
≜exp

−γ
X
M∈S
X
O∈P
h
tr

Oρ M(x)

−tr

Oρ M(x′) i2
!
,
whereγ >0is a kernel hyperparameter,Sdenotes a
collection of subsystems of then-qubit system, andPdenotes
a set of nontrivial Pauli observables whose locality is chosen
consistently with the subsystems inS. For a subsystemM,
ρM(x)≜tr Mc (ρ(x))is the reduced density operator ob-
tained by tracing out the complement subsystemM c.
The PQKκ PQK(x,x ′)evaluates similarity using the expec-
tation values of selected observables computed from the re-
duced density matricesρ M(x). It can therefore be interpreted
as a classical RBF kernel applied to quantum-projected feature
vectors. Different projection strategies can be used to extract
these features from the quantum states.

ϕ(x)
Feature
map
Project to
classical space
by measurements
Fig. 2. A schematic design of the PQK architecture, where the raw inputs are first mapped into quantum feature space using a quantum feature mapϕ, and
finally projected back into a classical space through measurement.
In this work, we follow the same choices of subsys-
tems and observable sets as in [16] to computeκ PQK(x,x ′)
according to the locality levelm. The measurement set-
tings are as follows. (a) Single-qubit local measurements
(m= 1): We setS=S 1 ≜{{1},{2}, . . . ,{6}}and
P=P 1 ≜{X,Y,Z}, yielding18observables. (b) Two-
qubit measurements on adjacent qubit pairs (m= 2): We set
S=S 2 ≜{{1,2},{2,3},{3,4},{4,5},{5,6},{6,1}}and
P=P 2 ≜{XX,YY,ZZ}, again yielding18observables. (c)
Combined single- and two-qubit measurements (m∈ {1,2}):
We concatenate the projected features obtained usingS=S 1
andP=P 1 form= 1, with those obtained usingS=S 2
andP=P 2 form= 2, yielding36observables [16].
As a simple example for computingκ PQK, consider two
input samplesx 1 andx 2 encoded into density operatorsρ(x 1)
andρ(x 2). We takeS=S ′ ={{1},{2}}, and use the simple
observable setP=P ′ ={Z}for illustration. Suppose that
the corresponding expectation values are
tr(Zρ{1}(x1)) = 0.8,tr(Zρ {2}(x1)) =−0.2,
tr(Zρ{1}(x2)) = 0.5,tr(Zρ {2}(x2)) = 0.4.
Applying the PQK definition withγ= 1, we obtain
κPQK(x1,x 2) = exp (−[(0.8−0.5) 2 + (−0.2−0.4) 2]) =
exp (−[0.09 + 0.36]) = exp(−0.45)≈0.6376.
III. METHODOLOGY
A. Projected Quantum Kernel Classifier
The IoT input features are encoded into high-dimensional
quantum states using6-qubit quantum feature-map circuits,
where each qubit encodes one input feature. The resulting
quantum states are then measured using local Pauli observables
to extract information from localized subsystems. Following
the subsystem measurement strategies described above, these
quantum states are projected into a classical feature space
by evaluating the expectation values of the selected local
observables. The resulting expectation values are concatenated
to form lower-dimensional classical feature vectors, which are
then used to compute all pairwise PQKκ PQK(x,x ′)values.
After all pairwise PQK values are computed, the remaining
classification stage is entirely classical. In particular, PQK
classification follows the standard SVM-kernel pipeline [14]–
[16], with the classical feature map replaced by the PQK
pipeline described above.
Consider the binary training setD={(x i, yi)}N i=1 with
labelsy i ∈ {−1,+1}. The valuesκ PQK(xi,x j),i, j∈[N],
are supplied to a classical soft-margin SVM classifier, which
learns the dual coefficientsα= (α 1, . . . , αN ), by solving the
optimization problem
α⋆ = argmin
α



1
2
NX
i=1
NX
j=1
αiαjyiyjκPQK(xi,x j)−
NX
i=1
αi



subject to0≤α i ≤ξ, i∈[N],
NX
i=1
αiyi = 0.
The support vectors are the training samples withα ⋆ i >0. For
the classical RBF kernel, the optimization formulation remains
unchanged, withκ PQK replaced by the RBF kernelκ RBF =
exp (−γ∥xi −x j∥2)before hyperparameter tuning.
B. Quantum Feature Map Circuit
In QML, quantum feature map circuits are used to im-
plement the data encoding process on a quantum device.
In kernel methods, high-order nonlinear feature maps are
employed to approximate complex target functions. In the
quantum domain, this is widely achieved with instantaneous
quantum polynomial (IQP) designs such as theZZfeature
map, which enables nonlinear feature interactions using single-
qubit transformations and multi-qubit entanglements [9]. Ear-
lier studies have introduced useful encoding designs, properly
renamed as Rot(X), a single qubitR X rotation, and IQP. Later
work also introduced variants of mapping designs, such as
Rot(X,Y,Z),R X,R Y,R Z rotations; and Rot(X,Y,Z)+CNOT,
Rot(X,Y,Z)with circular entanglement, to develop PQKs for
benchmarking and real-world IoT applications [14]–[16]. The
common idea behind such variants is to introduce a broader
class of entanglements, either linear or fully entangled, or
additional complexity through additional rotation gates [16].
Moreover, a PQK employs distinct measurement strategies
described in Sec. II-D.
These previous studies support the merit of PQK formula-
tions and their applicability, to some extent, toward developing
useful quantum models. However, we observe two major
shortcomings: (a) the performance is highly dependent on
extensive classical hyperparameter tuning of the RBF kernel
parameterγand the SVM regularization parameterξ; and (b)
there is a lack of structural explainability in quantum feature-
map designs for real-world data. Through this work, we aim

0 RX
1 RX
2 RX
3 RX
4 RX
5 RX
(a) Rot(X)
RX
RX
RX
RX
RX
RX
(e) Rot(X)en
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
(b) Rot(X,Y,Z)
H
H
H
RZ
RZ
RZ
RZ
RZ
(c) IQP
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
RX RY RZ
(d) Rot(X,Y,Z)+CNOT
H RZ RX RZ
RZ
H RZ RX RZ
RZ
H RZ RX RZ
RZ
H RZ RX RZ
RZ
H RZ RX RZ
RZH RZ RX RZ RZ
(f) Rot(X,Y,Z) en
Fig. 3. Schematic diagram of the distinct feature maps used for PQKs: (a) Rot(X), a single qubitR X rotation, inspired the designing of (e) Rot(X) en, Rot(X)
with a specific pair of entanglement; (b) Rot(X,Y,Z),R X,R Y,R Z rotations; (c) IQP, standard design, for simplicity, only ann= 3qubits circuit is shown;
(d) Rot(X,Y,Z)+CNOT, Rot(X,Y,Z)with circular entanglement, conceptually formed (f) Rot(X,Y,Z) en, with a specific pair of entanglement.
to assess the impact of different feature maps without tuning
the hyperparametersγandξ, thereby more precisely isolating
the representational capabilities of the quantum feature maps.
We also propose a structured approach to feature-map design
based on selected entanglement pairs. Based on this selection
procedure, we propose two new tailor-made feature maps,
Rot(X)en and Rot(X,Y,Z) en, for IoT data classification, as
illustrated in Fig. 3 (e) and (f).
The proposed feature maps aim to explore potential em-
pirical advantage by designing entanglement-induced PQKs
within our framework. A crucial component of our frame-
work is the intended structural design of the entanglement
layer. Rather than fixing an arbitrary entangling pattern,
we systematically evaluate pairwise entanglement candidate
topologies constructed from all possible two-qubit feature-
interaction pairs. We then select the topology that yields
the best empirical performance. In this way, the proposed
feature maps test whether carefully chosen pairwise entan-
glement can improve the resulting PQK on real-world IoT
data. Specifically, Rot(X)en and Rot(X,Y,Z) en couple selected
qubit pairs through feature-dependent two-qubit interactions,
thereby encoding multivariate input-feature correlations into
the quantum Hilbert space. Since previous benchmark studies
have suggested thatquantumnessvia entanglement may not be
a decisive performance driver for smaller learning tasks [18],
our experiment evaluates whether such selected entanglement
structures are beneficial for real-world IoT data.
C. Evaluation Criteria
To examine the influence of classical hyperparameter tuning,
we compare PQKs and the classical RBF baseline before and
after tuning. For the untuned PQK baselines, we fixξ= 1and
use the data-dependent heuristicγ= 1/(|S||P|σ 2), motivated
by the variance-scaled bandwidth grid in [14, Supplementary
information, eq. (S115)], with the multiplicative factor fixed to
one. Here,SandPare defined in Sec. II-D, andσ 2 is the em-
pirical variance of the projected features over the training data.
For the combined setting, the heuristic uses the36-dimensional
concatenated training representation. For the untuned classical
RBF baseline, we also fixξ= 1and useγ= 1/(dσ 2 x ),
whered= 6is the input dimension andσ 2 x is the empirical
variance of the input features over the training data. This
TABLE I
IOTDATA CLASSIFICATION EVALUATION FOR CLASSICAL MODELS.
Models Accuracy F1-score MCC
Lin 0.792±0.014 0.798±0.015 0.626±0.023
RBF 0.826±0.017 0.820±0.021 0.670±0.033
0.893±0.008 0.881±0.009 0.785±0.017
LDA 0.792±0.012 0.798±0.013 0.627±0.017
RF 0.902±0.006 0.891±0.008 0.804±0.013
AB 0.863±0.010 0.839±0.016 0.720±0.023
MLP 0.891±0.007 0.878±0.008 0.781±0.014
prescribed rule provides a reproducible baseline without grid-
search tuning, although the resulting performance comparisons
may still depend on the selected baseline hyperparameters. For
the PQKs only, each feature-map circuit is repeated twice to
increase its expressivity and circuit complexity, which may
make classical simulation more demanding as the system size
increases [9], [12]. Thereafter, we tune each feature map
circuit to quantify its impact and assess the need for tuning.
We have used10-fold cross-validation, in which10%of
the data is used for testing, with95%confidence intervals
(CIs) to assess the performance of untuned and tuned models,
and report test accuracy. The optimal values for the tuning
hyperparameters are determined through a grid search over the
setsξ∈ {0.006,0.015,0.03,0.0625} ∪ {2r |r=−3, . . . ,10}
andγ∈ {0.03,0.0625}∪{2 r |r=−3, . . . ,2}∪{5,7,8}[16].
The PQKs performances are evaluated using distinct sta-
tistical metrics such asaccuracy,F1-score, andMatthews
correlation coefficient (MCC). MCC provides valuable consid-
eration, given that IoT data is slightly imbalanced and reported
within the standard range[−1,+1][12], [19]. In addition to
linear (Lin) and RBF kernels, other non-kernel ML models
such as linear discriminant analysis (LDA), random forest
(RF), AdaBoost (AB), and multilayer perceptron (MLP), are
included for a robust and realistic comparison beyond the
kernel methods. These non-kernel models are also optimized
(tuned) to achieve their best performance. The experiments are
conducted in a noiseless quantum PennyLane simulator [20].

TABLE II
IOTDATA CLASSIFICATION ACCURACY, F1-SCORE,ANDMCCVALUE FORPQKMODELS BEFORE AND AFTER HYPERPARAMETER TUNING.
Models m= 1 m= 2 m∈ {1,2}
Accuracy F1-score MCC Accuracy F1-score MCC Accuracy F1-score MCC
Rot(X) 0.853±0.015 0.842±0.017 0.711±0.030 0.855±0.013 0.847±0.012 0.720±0.026 0.859±0.015 0.850±0.016 0.726±0.030
0.893±0.009 0.881±0.009 0.786±0.018 0.895±0.009 0.883±0.010 0.789±0.018 0.896±0.009 0.884±0.010 0.792±0.019
Rot(X,Y,Z) 0.864±0.012 0.858±0.015 0.742±0.023 0.852±0.013 0.843±0.015 0.714±0.026 0.864±0.013 0.857±0.015 0.740±0.026
0.895±0.011 0.883±0.012 0.789±0.022 0.892±0.010 0.880±0.012 0.784±0.021 0.897±0.010 0.885±0.013 0.793±0.021
Rot(X,Y,Z)
+CNOT
0.844±0.013 0.832±0.015 0.693±0.027 0.839±0.013 0.829±0.016 0.688±0.022 0.857±0.014 0.849±0.017 0.724±0.027
0.894±0.008 0.883±0.010 0.789±0.017 0.890±0.006 0.878±0.009 0.780±0.011 0.896±0.008 0.886±0.010 0.794±0.016
IQP 0.836±0.014 0.828±0.018 0.685±0.024 0.838±0.015 0.826±0.020 0.683±0.029 0.838±0.013 0.829±0.017 0.687±0.023
0.872±0.008 0.856±0.011 0.741±0.017 0.868±0.008 0.854±0.011 0.736±0.017 0.873±0.011 0.862±0.013 0.750±0.021
Rot(X)en 0.848±0.015 0.838±0.018 0.703±0.031 0.855±0.015 0.845±0.016 0.717±0.027 0.856±0.016 0.846±0.018 0.720±0.031
0.902±0.009 0.891±0.010 0.803±0.019 0.898±0.012 0.887±0.015 0.796±0.024 0.903±0.011 0.892±0.013 0.806±0.022
Rot(X,Y,Z) ∗ 0.850±0.010 0.844±0.013 0.716±0.019 0.854±0.012 0.849±0.016 0.726±0.024 0.856±0.010 0.850±0.014 0.727±0.019
0.893±0.010 0.883±0.011 0.789±0.020 0.890±0.010 0.879±0.009 0.782±0.019 0.894±0.008 0.883±0.009 0.789±0.015
Rot(X,Y,Z) en 0.865±0.014 0.857±0.017 0.740±0.028 0.867±0.015 0.855±0.020 0.737±0.032 0.868±0.014 0.860±0.018 0.746±0.028
0.900±0.006 0.889±0.008 0.801±0.012 0.896±0.010 0.884±0.015 0.791±0.022 0.903±0.008 0.892±0.010 0.806±0.016
IV. NUMERICALRESULTS ANDDISCUSSION
The performance on the IoT data is analyzed from two
perspectives: (a) the evaluation of classical models to establish
baseline performance, with particular emphasis on the RBF
kernel under both untuned and tuned settings, as reported
in Table I; and (b) the evaluation of different PQKs feature
maps with and without hyperparameter tuning, as reported in
Table II. This structure allows us to separate the effect of
classical hyperparameter tuning from the intrinsic representa-
tional capability of the feature maps. For both Tables I and II,
untuned results are highlighted in blue.
As shown in Table I, the simple linear kernel, Lin, gives
the lowest baseline performance, with an accuracy of0.792±
0.014and an MCC of0.626±0.023. The LDA model, which
is also linear, performs similarly, achieving an accuracy of
0.792±0.012and an MCC of0.627±0.017. These results
indicate that the classification is not well captured by a purely
linear decision boundary.
To examine the role of native inductive bias, we focus on
the RBF as the classical nonlinear kernel baseline, since its
behavior provides a natural reference point for contextualizing
the formulation and potential advantages of PQKs. Table I
compares the untuned RBF performance with the optimized
RBF performance after hyperparameter tuning. Before tuning,
the RBF achieves moderate performance, with an accuracy of
0.826±0.017and an MCC of0.670±0.033. After grid-search
optimization, the performance improves substantially, reaching
an accuracy of0.893±0.008and an MCC of0.785±0.017.
Overall, the optimized RBF outperforms the Lin baseline by
approximately10% in accuracy,8% in F1-score, and16% in
MCC, while also reducing the CIs across the metrics. This
large improvement shows that the RBF is highly sensitive to
hyperparameter tuning.
Among the remaining classical models, AB and MLP per-
form better than the linear baselines, with AB achieving an
accuracy of0.863±0.010and an MCC of0.720±0.023, and
MLP achieving an accuracy of0.891±0.007and an MCC
of0.781±0.014. The RF model gives the strongest classical
performance, with an accuracy of0.902±0.006, an F1-score
of0.891±0.008, and an MCC of0.804±0.013. Note that RF
is a more complex ensemble model than the kernel methods, as
it can capture nonlinear and higher-order feature interactions.
Hence, it provides a strong classical benchmark for assessing
the empirical competitiveness of the PQKs.
Table II reports the performance of six PQK models de-
rived from distinct feature maps. The untuned PQK results
already reveal a meaningful native inductive bias. For example,
the untuned Rot(X)withm= 1achieves an accuracy of
0.853±0.015and an MCC of0.711±0.030, outperforming
the untuned RBF kernel. Similarly, the untuned Rot(X,Y,Z)
feature map achieves an accuracy of0.864±0.012and an
MCC of0.742±0.023underm= 1. These results suggest
that the induced quantum feature spaces can provide useful
geometric separation even before classical hyperparameter
tuning is applied.
After hyperparameter tuning, the standard PQK feature
maps become comparable to the tuned RBF baseline. For
Rot(X), the best performance is obtained underm∈ {1,2},
with an accuracy of0.896±0.009, an F1-score of0.884±
0.010, and an MCC of0.792±0.019. The Rot(X,Y,Z)feature
map achieves a similar trend, with its best-tuned performance
underm∈ {1,2}reaching an accuracy of0.897±0.010and an
MCC of0.793±0.021. These results indicate that increasing
the measurement-based feature representation from individual
mvalues to combined valuesm∈ {1,2}yields consistent,
although marginal improvements.
The entanglement-based standard feature maps do not
automatically lead to better performance. In particular,
Rot(X,Y,Z)+CNOT performs similarly to Rot(X,Y,Z)after
tuning, while the IQP feature map performs worse compared
to the other PQKs, reaching an accuracy of0.873±0.011
and an MCC of0.750±0.021underm∈ {1,2}. This
observation suggests that simply adding entanglement or using
a dense entangling architecture is not useful in improving PQK
performance. Rather, the structure of the entanglement pattern
appears to be important.
The proposed feature maps, based on selected pairwise

RBF Rot(X)Rot(X,Y,Z)
Rot(X,Y,Z)+CNOT
IQPRot(X)
en
Rot(X,Y,Z)
en2
4
6
8
10
12
∆Acc
∆Acc
2
4
6
8
10
12
∆MCC
∆MCC
Fig. 4. Sensitivity analysis of PQK and RBF hyperparameter tuning.
entanglement structures, yield the strongest PQK results.
The proposed Rot(X) en feature map achieves an accuracy of
0.902±0.009, an F1-score of0.891±0.010, and an MCC
of0.803±0.019underm= 1. Underm∈ {1,2}, it
further reaches an accuracy of0.903±0.011and an MCC of
0.806±0.022. Similarly, Rot(X,Y,Z) en achieves competitive
performance, with an accuracy of0.900±0.006, an F1-score
of0.889±0.008, and an MCC of0.801±0.012underm= 1,
and its best overall performance underm∈ {1,2}reaches an
accuracy of0.903±0.008, an F1-score of0.892±0.010, and an
MCC of0.806±0.016. These results show that the proposed
selected-entanglement feature maps outperform the standard
PQK designs and are competitive with the strongest classical
baseline model, the RF. As an ablation study, we also report
numerical results for an unentangled variant of Rot(X,Y,Z) en,
denoted by Rot(X,Y,Z) ∗, to isolate and quantify the perfor-
mance gains attributable to entanglement.
To quantify the effect of hyperparameter tuning, Fig. 4
presents a sensitivity analysis based on the performance dif-
ferences between the tuned and untuned settings. We define
∆Acc as the change in accuracy and∆ MCC as the improvement
in MCC after tuning. The RBF exhibits the highest tuning
sensitivity, indicating that its strong performance depends
heavily on grid-search tuning. In contrast, the PQK models
generally show lower sensitivity, suggesting that their feature
maps provide a stronger native inductive bias before tuning.
The proposed entanglement-induced feature maps maintain
strong performance while requiring less tuning-induced cor-
rection than the RBF. The results support two main obser-
vations. First, all untuned PQKs can induce useful native
geometric separation in IoT data classification, as evidenced
by their performance relative to the untuned RBF baseline.
Second, carefully selected pairwise entanglement structures
can improve PQK performance more effectively than generic
entanglement patterns, such as circular CNOT layers or IQP-
style dense entanglement. These findings suggest that the
empirical usefulness of entanglement in PQKs depends not
only on the presence of entanglement, but also on how the
entanglement topology is selected and aligned with the data.
V. CONCLUSION ANDFUTUREWORK
This study compared six quantum feature maps for IoT
classification before and after classical hyperparameter tuning.
The proposed circuits, Rot(X) en and Rot(X,Y,Z) en, achieved
the strongest PQK performance and were competitive with
the strongest classical baseline. Under the prescribed untuned
settings, PQKs outperformed the untuned RBF and generally
showed smaller tuning-related gains, suggesting useful task-
specific inductive biases.
This study is limited to heuristic feature-map designs
evaluated on a single, relatively small dataset. Future work
should assess robustness across multiple baseline hyperparam-
eter choices and datasets, and examine how circuit-induced
inductive biases shape the geometry and expressivity of the
projected feature space.
REFERENCES
[1] P. Rebentrost, M. Mohseni, and S. Lloyd, “Quantum support vector
machine for big data classification,”Phys. Rev. Lett., vol. 113, no. 13,
Sep. 2014, Art. no. 130503.
[2] J. Biamonteet al., “Quantum machine learning,”Nature, vol. 549, no.
7671, pp. 195–202, Sep. 2017.
[3] M. A. Nielsen and I. L. Chuang,Quantum Computation and Quantum
Information, 10th ed. Cambridge, U.K.: Cambridge University Press,
2010.
[4] F. Rodr ´ıguez-D´ıaz, D. Guti ´errez-Avil´es, A. Troncoso, and F. Mart ´ınez-
´Alvarez, “A survey of quantum machine learning: Foundations, algo-
rithms, frameworks, data and applications,”ACM Comput. Surv., vol. 58,
no. 4, pp. 1–35, Oct. 2025.
[5] M. Schuld and N. Killoran, “Quantum machine learning in feature
Hilbert spaces,”Phys. Rev. Lett., vol. 122, no. 4, Feb. 2019, Art. no.
040504.
[6] M. Schuld, “Supervised quantum machine learning models are kernel
methods,” Jan. 2021, arXiv:2101.11020v2 [quant-ph].
[7] M. A. Khan, M. N. Aman, and B. Sikdar, “Beyond bits: A review of
quantum embedding techniques for efficient information processing,”
IEEE Access, vol. 12, pp. 46 118–46 137, 2024.
[8] N. Nguyen and K.-C. Chen, “Quantum embedding search for quantum
machine learning,”IEEE Access, vol. 10, pp. 41 444–41 456, 2022.
[9] V . Havl´ıˇceket al., “Supervised learning with quantum-enhanced feature
spaces,”Nature, vol. 567, no. 7747, pp. 209–212, Mar. 2019.
[10] Y . Liu, S. Arunachalam, and K. Temme, “A rigorous and robust quantum
speed-up in supervised machine learning,”Nature Phys., vol. 17, no. 9,
pp. 1013–1017, Jul. 2021.
[11] A. E. Paine, V . E. Elfving, and O. Kyriienko, “Quantum kernel methods
for solving regression problems and differential equations,”Phys. Rev.
A, vol. 107, no. 3, Mar. 2023, Art. no. 032428.
[12] R. K. Jha, N. Kasabov, S. Bhattacharyya, D. Coyle, and G. Prasad, “A
hybrid spiking neural network - quantum framework for spatio-temporal
data classification: A case study on EEG data,”EPJ Quantum Technol.,
vol. 12, no. 1, Nov. 2025, Art. no. 130.
[13] S. Thanasilp, S. Wang, M. Cerezo, and Z. Holmes, “Exponential
concentration in quantum kernel methods,”Nature Commun., vol. 15,
no. 1, Jun. 2024, Art. no. 5200.
[14] H.-Y . Huanget al., “Power of data in quantum machine learning,”Nature
Commun., vol. 12, no. 1, May 2021, Art. no. 2631.
[15] J. Schnabel and M. Roth, “Quantum kernel methods under scrutiny: A
benchmarking study,”Quantum Mach. Intell., vol. 7, no. 1, Apr. 2025,
Art. no. 58.
[16] F. D’Amoreet al., “Assessing projected quantum kernels for the classi-
fication of IoT data,”Array, vol. 29, Mar. 2026, Art. no. 100695.
[17] I. Khanet al., “Leveraging distributed AI for multi-occupancy prediction
in Cognitive Buildings,”Internet of Things, vol. 26, Jul. 2024, Art. no.
101181.
[18] J. Bowles, S. Ahmed, and M. Schuld, “Better than classical? The subtle
art of benchmarking quantum machine learning models,” Mar. 2024,
arXiv:2403.07059v2 [quant-ph].
[19] D. Chicco and G. Jurman, “The advantages of the Matthews correlation
coefficient (MCC) over F1 score and accuracy in binary classification
evaluation,”BMC Genomics, vol. 21, no. 1, Jan. 2020, Art. no. 6.
[20] V . Bergholmet al., “Pennylane: Automatic differentiation of hy-
brid quantum-classical computations,” Nov. 2018, arXiv:1811.04968v4
[quant-ph].
