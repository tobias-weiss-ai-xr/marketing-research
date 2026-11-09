---
title: 'Quantum Spectral Model: Data Reuploading with Input-Conditioned Frequency Support'
url: https://arxiv.org/abs/2607.22516
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Peiyong Wang
- Udaya Parampalli
- Casey R. Myers
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.22516
pages: 52
chars: 154788
fetched_at: '2026-11-08T13:26:44+00:00'
kb_version: 1
---

# Quantum Spectral Model: Data Reuploading with Input-Conditioned Frequency Support

Quantum Spectral Model: Data Reuploading with
Input-Conditioned Frequency Support
Peiyong Wang∗
CSIRO Technology
Research Way, Clayton VIC 3168, Australia
Peiyong.Wang at csiro.au
Udaya Parampalli
School of Computing and Information Systems
The University of Melbourne
Grattan Street, Parkville, VIC 3010, Australia
udaya at unimelb.edu.au
Casey R. Myers†
School of Physics, Mathematics and Computing
The University of Western Australia
35 Stirling Hwy, Crawley W A, 6009, Australia
casey.myers at uwa.edu.au
Abstract
A central design principle in modern machine learning and artificial intelligence is
to align a model’s inductive bias with the structure of its input data. For matrix-
valued inputs, relevant matrix-level relationships can be characterised through
spectral values and spectral subspaces; however, common coordinate-wise rotation-
gate data-encoding unitaries used in most quantum machine learning models do
not explicitly construct such a matrix-level representation. We introduce Quantum
Spectral Models (QSMs), in which we construct the generator of the data-encoding
unitary directly from each input matrix. We study three QSM variants based on
symmetric, global block, and non-overlapping patch-local block Hamiltonians.
Their outputs admit truncated Fourier representations in which input-dependent
spectral gaps supply candidate phase carriers, while spectral subspaces help deter-
mine their coefficients. We evaluate the QSMs and comparison quantum models on
two matrix representations of Pendigits and two controlled synthetic tasks defined
by spectral statistics. At the largest evaluated circuit depth, QSM variants lead
the tested quantum models in mean test accuracy across all four benchmarks. The
patch-local QSM leads on Pendigits, whereas the global block-Hamiltonian QSM
leads on the controlled spectral tasks. Ablations show a task-dependent reversal:
subspace-preserving controls perform better on Pendigits, whereas spectral-value-
only controls lead among the tested ablations on the synthetic tasks. Together, these
results shed new light on quantum machine-learning model design by showing how
input-conditioned spectral representations can provide an analysable inductive bias,
while offering a broader perspective on structure-aware model design in machine
learning and artificial intelligence.
1 Introduction
The design of modern deep neural networks often reflects inductive biases about the structure of
their input data. Convolutional neural networks encode spatial locality [ 27], while graph neural
networks encode relational structure [ 3]. Decoder-only Transformers impose an autoregressive
∗Corresponding author. Also available ataddwater0315 at gmail.com
†Also with Pawsey Supercomputing Centre, 1 Bryce Avenue, Kensington W A, 6151, Australia
Preprint.
arXiv:2607.22516v1  [quant-ph]  24 Jul 2026

Frequency
Amplitude
3. Available Tones
2. Oscillator Bank
5. Output Sound 4. Mixer / Filter
2. Hamiltonian
 5. Measurement /
Prediction
1. Control Signal
Eigenvalues
1. Input Matrix
Music
Synthesiser
Quantum
Spectral
Model
3. Spectrum & Gaps 4. Trainable Block
Probability / logit
Basis states / class label
control
 input oscillators
 Hamiltonian tones
 spectral
content
mixer /
filter
trainable
mixing
output
sound
 measurement
The input-dependent Hamiltonian determines available spectral components, while trainable quantum blocks
mix and expose them to measurement, analogous to how a music synthesiser shapes available tones into sound.
Figure 1:Synthesiser view of the quantum spectral model. Top, conceptual signal flow in a
music synthesiser; bottom, the corresponding flow in a quantum spectral model.Reading the
panels from left to right, the control signal corresponds to the input matrix, the oscillator bank to the
input-derived Hamiltonian, the available tones to its spectrum and spectral gaps, the mixer and filter
to the trainable quantum block, and the output sound to quantum measurement and prediction. A
matrix input M defines a Hamiltonian H(M) whose spectrum supplies sample-conditioned candidate
phase carriers and whose spectral projectors help determine their coefficients through the trainable
mixer and quantum measurement. Unlike a coordinate-wise rotation-gate data-encoding unitary with
globally determined candidate frequency support, the quantum spectral model conditions both its
candidate carriers and coefficient structure on each input matrix.
ordering through masked self-attention, preventing each token from accessing future tokens during
language modelling [42]. Operator-learning architectures, meanwhile, learn maps between function
spaces rather than between fixed-dimensional vectors [ 24]. The same representational decision
arises in quantum machine learning before training begins: classical data must first be mapped to
data-dependent quantum operations [46]. This encoding specifies the quantum representation on
which the trainable circuit acts.
Quantum models represent data through unitary evolution, whose dependence on a Hermitian
generator can be understood through its spectral decomposition. Data reuploading circuits alternate
data-encoding unitaries with trainable quantum layers [41]. A quantum Fourier model (QFM) is a
data-reuploading model whose observable outputs can be analysed as truncated Fourier series: the
spectra of the data-encoding generators determine the candidate frequencies, while the trainable
circuit controls their coefficients and interference at measurement [46]. From this perspective, encoder
design determines which frequencies, modes or basis functions are made available to the model.
Common data-encoding unitaries in reuploading circuits inject individual scalar features through
single-qubit rotation gates [46]. Trainable-frequency rotation-gate data-encoding unitaries can adjust
their globally shared candidate frequency support during optimisation [21]. Once trained, that support
remains shared across samples. These encoders process matrix entries through coordinate-wise
rotations rather than explicitly constructing a generator from matrix-level spectral values, spectral
subspaces, trajectory order or local organisation.
In this work, we instead construct the generator of the data-encoding unitary directly from each
input matrix. We call the resulting model class aQuantum Spectral Model(QSM). A QSM maps
a matrix-structured input to a Hamiltonian and uses the corresponding time evolution as the data-
encoding unitary. The resulting candidate frequency support is therefore conditioned on the input
matrix rather than determined solely by the generator family or globally learned frequency parameters.
In the synthesiser analogy in Figure 1, a conventional rotation-gate data-encoding unitary provides a
fixed oscillator bank, whereas a QSM allows each input to determine the available components; the
trainable mixer then combines these components before measurement.
2

Hamiltonian embedding changes both the candidate support and the coefficients of the resulting
truncated Fourier series. We refer to each application of a data-encoding unitary as an upload.
The one-upload candidate support comprises eigengaps of the symmetrised input matrix for the
symmetric-Hamiltonian QSM and signed singular-value gaps, including gaps involving zero modes,
for the block-Hamiltonian QSM. In both cases, the candidate support varies across samples, while
the Fourier coefficients depend on input-derived spectral projectors or subspaces together with the
initial state, trainable mixer and quantum measurement observable (see Equations (19), (20), (23)
and (24)). A particular observable output may realise only a subset of the candidate support when
coefficients vanish or cancel. A QSM therefore does more than pass eigenvalues or singular values to
a classifier: its distinguishing feature is the coupling of sample-conditioned candidate phase carriers
and sample-conditioned spectral subspaces through the trainable mixer and quantum measurement.
This construction makes quantum data encoding a choice of inductive bias, because the input-
derived operator determines which spectral information is made available to the trainable circuit.
We therefore focus on the representational consequences of this operator choice within a common
upload–mixer framework. Frequency-related learning phenomena have been studied in classical
neural networks, where spectral bias interacts with data-manifold geometry [ 51, 43]. In quantum
neural networks, trainable-frequency QFMs make the candidate frequency support itself optimisable
[21]. Spectral representations also depend on the choice of transform, operator and basis [4]. Classical
architectures obtain spectral structure from fixed Fourier transforms [28], spectral parameterisations
of convolutional networks [44], graph-Laplacian bases [5] or Fourier-space operators learned across
a training distribution [30, 17]. In a QSM, the current input matrix instead defines the Hamiltonian,
whose spectral decomposition supplies sample-conditioned candidate phase carriers and coefficient-
forming subspaces for unitary evolution.
We study two global QSM variants. The symmetric-Hamiltonian QSM follows our earlier Hamiltonian
embedding, Hsym(M) = (M+M T )/2 [49]. We additionally study the block-Hamiltonian QSM,
which uses Hblock(M) =
 0M
M T 0

(see Equations (14) and (15)). We also evaluate fixed and
trainable patch-SU(4) data-encoding unitaries and a quantum spectral model with a non-overlapping
patch-local block-Hamiltonian-based data-encoding unitary to test the effect of local structure; their
definitions are given in Appendix Section E.
We investigate how sample-conditioned candidate frequency support changes representation, op-
timisation and final-state geometry within a common upload–mixer modelling framework. We
compare the three QSM variants with fixed rotation-gate, trainable-frequency rotation-gate, fixed
patch-SU(4) and trainable patch-SU(4) data-encoding unitaries on two matrix representations of
Pendigits [1] and two controlled spectral tasks. At depth 32, a QSM variant attains the largest mean
among the tested quantum models in all four cases: the patch-local block-Hamiltonian QSM leads
on both Pendigits representations, while the block-Hamiltonian QSM leads on both synthetic tasks
(see Figure 3 and table 1). The gradient diagnostics show that the coordinate-wise rotation-gate
data-encoding unitaries have much more strongly suppressed mixer-gradient variance at high-depth
initialisation, whereas several high-performing QSMs retain larger final gradient scales (see Figure 4).
Their final-state fidelity kernels also show more label-aligned geometry in the fixed diagnostic batch,
while the patch-SU(4) controls demonstrate that gradient magnitude or fidelity-kernel spectral spread
alone does not determine accuracy (see Figure 5).
We further use ablations to distinguish the roles of spectral values and subspaces. On Pendigits,
spectrum-only controls perform poorly, whereas controls that preserve the input-dependent spectral
subspaces retain substantially higher accuracy. The ordering reverses on the synthetic tasks, whose
labels are defined by eigenvalue or singular-value statistics: spectral-value-only controls are strong,
while vector-only controls are weaker (Tables 2 and 7). This reversal establishes a task-dependent
division of labour within the sample-conditioned representation: Pendigits relies more strongly
on input-dependent subspace geometry and its interaction with the trainable mixer, whereas the
controlled tasks reward the relevant spectral values directly.
We make four contributions that connect the QSM construction, its Fourier analysis and the empirical
comparisons. First, we formulate QSMs as matrix-conditioned models with Hamiltonian-based
data-encoding unitaries and identify their representational distinction from encoders with globally
shared frequency support. Second, we derive the eigengap and signed-singular-gap candidate supports
of the symmetric- and block-Hamiltonian QSMs, together with the dependence of their coefficients
3

on input-derived spectral projectors or subspaces. Third, controlled quantum-model comparisons
across reuploading depths, complemented by gradient and fidelity diagnostics, characterise depth-
dependent performance, optimisation behaviour and final-state geometry across four benchmark
cases. Fourth, value-versus-subspace and structure-destroying ablations identify which component of
the sample-conditioned QSM representation is informative for each task.
2 Related Work
Variational quantum learning.Variational quantum circuits (VQCs), trained with classical optimi-
sation algorithms, are widely studied as models for near-term quantum applications [8]. In quantum
machine learning, they have been applied to classification [13] and generative modelling [11, 20]
tasks. However, their optimisation can be impeded by barren plateaus [ 39, 26] and by poor local
minima even in shallow regimes without barren plateaus [2].
Quantum data encoding.When learning from classical data, the encoding map determines the
quantum representation [45]. Common schemes represent features through rotation angles, state
amplitudes or computational-basis states [ 45]. Hamiltonian embedding constructs an evolution
generator from a matrix-valued sample [49]. Block encodings provide a related but distinct matrix
representation: they embed a scaled matrix as a subblock of a larger unitary used as an algorithmic
primitive [6, 7]. Our block-Hamiltonian construction instead uses the matrix to define the generator of
the data-encoding evolution. In reuploading models, the encoding generator constrains the frequency
set available to the trainable circuit [46].
Hamiltonian learning and recognition.Hamiltonian learning infers an unknown physical generator
from controlled measurements, using either structural assumptions or ansatz-free black-box protocols
[18, 16, 19]. Hamiltonian recognition instead selects a generator from a finite candidate set, including
through quantum-signal-processing and variational protocols [52]. Both address inverse problems for
a fixed unknown generator, whereas a QSM constructs H(M) from each input matrix for forward
prediction, making its candidate gap support and projector-dependent coefficients sample-conditioned.
Data reuploading and quantum Fourier models.Data reuploading circuits interleave data-encoding
and trainable unitaries and were introduced as universal quantum classifiers [ 41]. Their outputs
admit truncated Fourier-series representations whose frequencies are determined by the spectrum
of the encoding generator. In particular, Pauli-generated rotation gates provide a finite grid of
integer-spaced coordinate frequencies, with the spacing set by the coefficient multiplying each input
feature, such as α in Ry(αx) [46]. When we analyse their observable outputs through this finite
Fourier representation, we refer to these data-reuploading models as quantum Fourier models (QFMs).
Trainable-frequency models optimise the generator spectrum [21], while recent theory quantifies the
depth needed for fixed-frequency encodings to approximate tunable ones [32]. Linear-combination-
of-unitaries-inspired architectures can instead select prescribed Fourier components [ 47]. These
constructions therefore provide architecture-fixed or globally learned candidate support shared across
samples. Other analyses identify coefficient constraints and vanishing expressivity in QFMs [ 40].
Moreover, for high-dimensional inputs, limited-qubit reuploading models can approach random-
guessing performance as the encoding depth grows, motivating wider architectures rather than deeper
and narrower ones [50]. QSMs instead construct the data-encoding generator from each input, so
their candidate frequency support varies across samples.
Spectral methods in quantum machine learning.Classical neural networks often learn low-
frequency components before high-frequency ones, although the geometry of the data manifold can
modify this bias [51, 43]. A recent framework derives an analogous low-frequency bias for quantum
neural networks [ 38]. Model spectra have also been proposed as objects that quantum routines
can learn, regularise or manipulate [4]. QSMs address an earlier representational choice: the input
determines which candidate phase carriers are available to the model.
Classical spectral architectures.Classical spectral architectures can obtain spectral structure from
fixed transforms, Fourier-space maps learned across a training distribution, or domain- and graph-
derived operators. Fourier neural operators parameterise integral kernels directly in Fourier space to
learn maps between function spaces [30]. Spectral representations support pooling, regularisation
and filter parameterisation in convolutional networks [44]. FNet uses fixed, unparameterised Fourier
transforms for token mixing [28], whereas adaptive Fourier neural operators learn token mixing in
the Fourier domain [17]. Graph networks derive spectral bases from graph shift operators, commonly
4

a Laplacian; because the operator is tied to graph structure, the basis can change when the graph
structure changes, while filters are learned over its spectrum [ 5, 12, 29, 31]. Within this broader
landscape, QSMs take an input-adaptive route: each matrix sample defines a Hermitian generator
whose spectral subspaces and gap-derived candidate phase carriers enter the unitary representation.
3 Preliminaries
Circuit architecture and projector readout.A depth- L data-reuploading circuit alternates data-
encoding unitaries with trainable mixers [41]:
|ψ(x;Θ)⟩=V L(θL)SL(x;ϕ L)· · ·V1(θ1)S1(x;ϕ 1)|ψ 0⟩.(1)
Here Θ={(θ ℓ,ϕ ℓ)}L ℓ=1 collects the mixer and encoder parameters, with ϕℓ omitted for fixed
encoders. We use |ψ0⟩=|+⟩ ⊗n on n qubits. For N classes, let m=⌈log 2 N⌉ and associate class j
with the projector [49]
Pj =|j⟩ ⟨j| ⊗I⊗(n−m),j∈ {0,. . .,N−1},(2)
where |j⟩ is an m-qubit computational-basis state. The raw projector mass qj and the conditional
class probabilityp j used in the experiments are
qj(x;Θ) =⟨ψ(x;Θ)|P j |ψ(x;Θ)⟩,
pj(x;Θ) = qj(x;Θ)PN−1
k=0 qk(x;Θ)
,
N−1X
k=0
qk >0. (3)
If N= 2 m, the projectors exhaust the label register and pj =q j. Otherwise, pj conditions the
measurement distribution on the named class outcomes and leaves the predicted class unchanged.
The Fourier analysis below concerns the observable outputs qj: the nonlinear normalisation in
Equation (3) need not preserve a finite Fourier representation.
Fourier representation of observable outputs.For fixed generator parameters, an observable output
of a data-reuploading circuit admits a truncated Fourier expansion [46]
fθ(x) =
X
ω∈Ω
cω(θ)e−iω·x, Ω⊆R d.(4)
The generator eigenvalues and upload pattern determine the maximal candidate support Ω; the
corresponding spectral projectors, initial state, trainable mixers and quantum measurement observable
determine the coefficients. Equal candidate support therefore need not imply equal observable outputs.
Consequently, the realised Fourier support of a particular output may be smaller than Ω, because
candidate frequencies with zero coefficients do not appear in the output [40].
For one upload of a single scalar input feature, let S(x) =e −ixK, where K is Hermitian with distinct
eigenvaluesκ a and eigenspace projectorsΠ a. Then
K=
X
a
κaΠa,S(x) =
X
a
e−ixκa Πa, X
a
Πa =I, Π aΠb =δ abΠa.(5)
DefiningO θ =V(θ) †OV(θ), the one-upload output is
f1(x;θ) =⟨ψ 0|S(x) †OθS(x)|ψ 0⟩
=
X
a,b
e−ix(κb−κa) ⟨ψ0|Π aOθΠb |ψ0⟩
=
X
a,b
cab(θ)e−ix(κb−κa).
(6)
The maximal one-upload support is therefore
Ω1 ={κ b −κ a :a,b}.(7)
For frequency sets A,B⊆R d, we denote their Minkowski sum byA⊕B={a+b:a∈A,b∈B}
and use LL ℓ=1 Aℓ for its repeated application. For layer-dependent generators, let Ω1,ℓ denote the
5

corresponding gap set at uploadℓ. Because the phase factors multiply across uploads, their frequencies
add; hence, the maximal L-upload candidate support and the Fourier support of a particular output
satisfy [46]
ΩL =
LM
ℓ=1
Ω1,ℓ, supp F(f)⊆Ω L.(8)
If every upload uses the same generator, this reduces to
ΩL = Ω1 ⊕ · · · ⊕Ω1| {z }
Luploads
.(9)
Frequency support of rotation encoders.We summarise the maximal one-upload supports of the
three rotation encoders used in the experiments for d scalar features x= (x 1,. . .,xd). Appendix B
gives the derivations.
ForS Ry (x) = Nd j=1 Ry(αxj), the support is
ΩRy 1 = n α(n1,. . .,nd) :n j ∈ {−1, 0, 1} o .(10)
ForS RyRz (x) = Nd j=1 Rz(βxj)Ry(αxj), the one-feature support is
ΩRyRz local = n nα+mβ:n,m∈ {−1, 0, 1} o ,(11)
and the full vector-valued support is
ΩRyRz 1 = n (ω1,. . .,ωd) :ω j =n jα+m jβ,n j,m j ∈ {−1, 0, 1} o .(12)
For the component-wise trainable-frequency encoder, upload scale γj enters the rotation Ry(γjxj)
for featurej[21]. Its one-upload support is
ΩTF 1 (γ) = n (n1γ1,. . .,ndγd) :n j ∈ {−1, 0, 1} o .(13)
The experiments use a separate scale vector γℓ at each upload. Once α, β or the γℓ are fixed, these
maximal supports are shared across samples: changing x changes the evaluation point but not the
available frequency set. This sample-independent support provides the baseline for the Hamiltonian
embeddings introduced in Section 4.
4 Hamiltonian Embedding Produces Sample-Conditioned Frequency Support
Let M=M x ∈R p×q denote the matrix representation of an input x, with p≥q for the layouts
considered here. In our previous work, we adopted the symmetric Hamiltonian embedding as the
generator of a data-encoding unitary for classification [49]:
Hsym(M) =
fM+ fM T
2 ,(14)
where fM is the square matrix obtained by zero-column padding when M is rectangular. Symmetrisa-
tion removes the skew-symmetric component offM. We therefore also consider the block-Hamiltonian
embedding
Hblock(M) =
0p×p M
M T 0q×q

,(15)
which retains M as an off-diagonal block. This construction has the same Hermitian block form used
in the quantum polar decomposition algorithm, with A=M T for real M [33]. Here it serves as a
sample-derived generator of a data-encoding unitary rather than as a subroutine for implementing the
polar factors.
When required by the circuit dimension or projector readout, either Hamiltonian is promoted by
direct-sum padding, H7→H⊕0 ; we retain the same symbol for the padded operator. This convention
6

preserves its nonzero spectrum and introduces additional zero modes. Within a QSM, the two global
data-encoding unitaries are
SHsym (t;M) =e −iHsym(M)t/2 ,S Hblock (t;M) =e −iHblock(M)t/2 .(16)
We also consider a QSM with a non-overlapping patch-local block-Hamiltonian-based data-encoding
unitary. This variant partitions M into R patches P1,. . .,PR and applies Hblock(Pr) on disjoint
registers. The experiments use four2×2patches, defined in Appendix E.
For each fixed M, the analysis below treats the upload time t, or the vector of patch times, as
the Fourier variable. Accordingly, Ω1(M) denotes sample-conditioned candidate support in the
upload-time variables; the entries of M condition the generator and remain fixed throughout this
expansion. Appendix C gives the full derivations, including padding, degeneracies and layer-specific
upload times.
Symmetric embedding produces eigengap carriers.Let Asym(M) denote the index set of distinct
eigenvalues ofH sym(M). For eacha∈ Asym(M), letλ a(M)be the corresponding eigenvalue and
letΠ sym a (M)project onto its full eigenspace. Then
Hsym(M) =
X
a∈Asym(M)
λa(M)Π sym a (M),S Hsym (t;M) = X
a
e−iλa(M)t/2 Πsym a (M).(17)
For a quantum measurement observable O, with the trainable mixer absorbed into Oθ, the resulting
one-upload observable output is
f Hsym 1 (M;t,θ) = X
a,b
AHsym ab (M,θ)e −i[λb(M)−λ a(M)]t/2 ,(18)
where the pair amplitudes and the coefficient at frequencyωare
AHsym ab (M,θ) =⟨ψ 0|Π sym a (M)O θΠsym b (M)|ψ 0⟩,
C Hsym ω (M,θ) = X
a,b:
(λb(M)−λ a(M))/2=ω
AHsym ab (M,θ). (19)
The maximal one-upload candidate support therefore satisfies
ΩHsym 1 (M) =
 λb(M)−λ a(M)
2 :a,b∈ Asym(M)

,
suppF(f Hsym 1 )⊆Ω Hsym 1 (M).
(20)
Thus, for the symmetric-Hamiltonian QSM, the candidate frequencies depend on the eigengaps of
the sample-derived Hamiltonian, while the realised coefficients also depend on its eigenspaces, the
initial state, the trainable mixer and the readout.
Block-Hamiltonian embedding produces signed singular-value gaps.If the nonzero singular
values of M are σj(M), then the nonzero eigenvalues of Hblock(M) are ±σj(M). Let Ablock(M)
denote the index set of distinct eigenvalues of Hblock(M). For each a∈ Ablock(M), let µa(M) be
the corresponding eigenvalue, including zero when present, and let Πblock a (M) project onto its full
eigenspace:
Hblock(M) =
X
a∈Ablock(M)
µa(M)Π block a (M),µ a(M)∈ {+σj(M),−σ j(M), 0}.(21)
The corresponding observable output has the expansion
f Hblock 1 (M;t,θ) = X
a,b
AHblock ab (M,θ)e −i[µb(M)−µ a(M)]t/2 ,(22)
with
AHblock ab (M,θ) =⟨ψ 0|Π block a (M)O θΠblock b (M)|ψ 0⟩,
C Hblock ω (M,θ) = X
a,b:
(µb(M)−µ a(M))/2=ω
AHblock ab (M,θ). (23)
7

Its maximal one-upload candidate support is
ΩHblock 1 (M) =
 µb(M)−µ a(M)
2 :a,b∈ Ablock(M)

,
suppF(f Hblock 1 )⊆Ω Hblock 1 (M).
(24)
For the block-Hamiltonian QSM, these gaps include half-differences and half-sums of singular values;
when a zero eigenspace is present, they also include ±σj(M)/2. The coefficients depend on the
associated singular subspaces together with the initial state, mixer and readout.
Patch-local embedding factorises support across patches.For patch Pr, let ΩHblock 1 (Pr) be the
candidate set in Equation (24). Because the patch uploads act on disjoint registers with independent
timest= (t 1,. . .,tR), their maximal one-upload support is
Ωpatch-Hblock 1 (M) = Ω Hblock 1 (P1)× · · · ×ΩHblock 1 (PR).(25)
This Cartesian product arises because the patches have independent upload-time variables. If they
instead shared a single scalar time, the corresponding scalar support would be the Minkowski sum
of the patch-level candidate sets. The patch-local carriers are therefore determined by the singular
spectra of individual patches rather than that of the full matrix. Their amplitudes depend on the
corresponding local singular subspaces, while the trainable mixer and readout can couple modes
from different patches. The joint data-encoding unitary, its coefficients and the extension to layer-
and patch-specific timest ℓ,r are derived in Equations (113), (115) and (116).
These three QSM data-encoding variants determine two coupled parts of the representation. Spectral
values determine the maximal candidate phase carriers, whereas spectral projectors or singular
subspaces participate in forming the realised coefficients through their interaction with the initial
state, trainable mixer and readout. The global variants condition these quantities on the full matrix,
while the patch variant conditions them separately on non-overlapping patches. The choice of data-
encoding unitary therefore determines both the available sample-conditioned phase carriers and the
subspaces through which the circuit forms their realised coefficients.
5 Experiments
Benchmark datasets.We use Pendigits [ 1] as a compact real-world benchmark. Each digit is
represented either by a DYN8×2 pen-trajectory matrix or by a STA44×4 bitmap-like matrix,
providing two structurally different views of the same ten-class task (Figure 2a). We also consider two
binary synthetic tasks: SYNTHETIC EIGENGAP , based on noisy observations of latent4×4 symmetric
matrices, and SYNTHETIC SINGULAR , based on noisy 8×2 rectangular matrices (Figure 2b). Their
labels are determined from the clean latent eigenvalues or singular values, making them controlled
tests of sensitivity to spectral structure. Preprocessing, data splits and data-generation settings are
given in Appendix Section D.
Encoders and training protocol.All models follow the upload–mixer template in Equation (1), with
|ψ0⟩=|+⟩ ⊗n. We compare eight data-encoding constructions: fixed- Ry, fixed-RyRz, trainable-
frequency Ry, fixed patch-SU(4) , trainable patch-SU(4) , patch-local block-Hamiltonian, symmetric
Hamiltonian and block Hamiltonian. They are defined in Sections 3 and 4 and Appendix Section E.
For each construction, we evaluate reuploading depths L∈ {1, 2, 4, 8, 16, 32}over 20 random
parameter-initialisation seeds. Block ℓ applies the upload Sℓ(x) followed by the trainable mixer
Vℓ(θℓ).
The comparison controls the dataset splits, upload–mixer template, optimiser, training budget and
number of random initialisation seeds, allowing us to examine how different data-encoding con-
structions behave under a common experimental protocol. However, the constructions differ in
both qubit and parameter count: rotation-gate data-encoding unitaries use 16 qubits, patch-local
data-encoding unitaries use eight, and the global QSMs use two to four qubits before any label-
register expansion, with the Pendigits global QSMs promoted to four qubits. The mixer therefore
contributes 15(n−1) parameters per layer, while the trainable data-encoding unitaries introduce
different additional parameter groups. These resource differences follow from the register layouts
and parameterisations adopted by the respective data-encoding constructions. We therefore compare
the predictive performance and inductive biases of the complete encoder–mixer configurations under
8

DYN
Class 1
STA4
Class 2
 Class 3
 Class 4
 Class 5
 Class 6
 Class 7
 Class 8
 Class 9
 Class 10
0
2
4
6
8
Raw value
(a)
Eigengap
Class 0
 Class 1
0.6
0.4
0.2
0.0
0.2
0.4
0.6
Entry
Singular
1.0
0.5
0.0
0.5
1.0
Entry
(b)
Figure 2:Representative training samples from the real-world and controlled synthetic bench-
marks. (a) Pendigits.One example from each of the ten original classes is shown using two paired
representations. The upper row shows theDYN representation, in which eight ordered two-dimensional
pen coordinates are connected in their recorded sequence. The lower row shows the corresponding
STA4 representation as a 4×4 bitmap-like matrix. Raw feature values are displayed for visualisation,
whereas the model inputs are standardised using statistics computed from the training split; the colour
bar reports the raw STA4 entry values.(b) Synthetic spectral benchmarks.One noisy training input
from each class is shown for the SYNTHETIC EIGENGAP task (top, 4×4 observations generated
from latent symmetric matrices) and the SYNTHETIC SINGULAR task (bottom, 8×2 rectangular
observations). For SYNTHETIC EIGENGAP , class 1 indicates that the gap between the two largest
eigenvalues of the latent clean matrix exceeds τeig = 0.75 . For SYNTHETIC SINGULAR , class 1
indicates that the sum of the two leading latent singular values exceeds τsv = 2; class 0 denotes the
complementary condition in each task. The displayed inputs include relative Gaussian noise with
ϵ= 0.05 , while the labels are computed from the corresponding clean latent spectra. Colours encode
the noisy matrix entries using a separate zero-centred scale for each task.
a common experimental protocol, treating data encoding as a central architectural choice. The results
compare the models as implemented, rather than isolating the encoder from all resource differences
or measuring performance per qubit or trainable parameter. Appendix Section E gives the padding
rules and exact depth-32 trainable-parameter counts.
For the two global QSMs, the data-encoding unitary at layerℓis
Ssym,ℓ(M) = exp
"
− i 2 Hsym(M)t ℓ
#
,S block,ℓ(M) = exp
"
− i 2 Hblock(M)t ℓ
#
,(26)
where Hsym(M) and Hblock(M) are defined in Equations (14) and (15). The trainable upload time
tℓ scales the input-derived Hamiltonian and is initialised to1/Lunless a fixed time is specified.
The patch-local data-encoding constructions divide each input into four non-overlapping2×2 patches
and assign each patch to a disjoint qubit pair. For fixed patch-SU(4) , a patch Pr ∈R 2×2 is flattened
9

and mapped linearly to 15 coefficients of the two-qubit unitary
Upatch(Pr) = exp
"
i
15X
a=1
θa(Pr)Ga
#
,(27)
where Ga are the 15 non-identity two-qubit Pauli generators. The fixed map is shared across layers
and patches; the trainable variant uses a separate linear map for each layer and patch. The patch-
local block-Hamiltonian QSM instead applies Equation (15) to each patch, with trainable times tℓ,r
initialised to1/Lunless fixed.
After each upload, Vℓ applies nearest-neighbour SU(4) blocks in a brick-wall pattern. The even pairs
(1, 2), (3, 4),. . .precede the odd pairs (2, 3), (4, 5),. . .. Each block has 15 trainable parameters, so
an n-qubit mixer layer contains n−1 blocks. Mixer parameters are initialised from a zero-mean
Gaussian with scale0.01.
All trainable parameters are optimised jointly. We use Adam [22] with learning rate 0.01, no weight
decay and 2000 optimisation steps. Pendigits runs use training and evaluation batch sizes of 32 and
128, respectively; the corresponding synthetic-task sizes are 64 and 256.
6 Results and Analysis
We organise the analysis in four stages: we first compare final test accuracy across reuploading depth,
then examine gradient behaviour, next analyse the final-state fidelity geometry of the trained models,
and finally use value–subspace and structure-destruction ablations to identify which components of
the sample-conditioned spectral representation are informative for each task.
QSMs attain the largest depth-32 mean test accuracy among the tested quantum models.At
depth 32, the patch-local block-Hamiltonian QSM has the largest mean accuracy on Pendigits
DYN (92.75%±0.84% ) and STA4 (86.14%±1.33% ), while the global block-Hamiltonian QSM
has the largest mean on SYNTHETIC EIGENGAP (85.15%±2.40% ) and SYNTHETIC SINGULAR
(92.72%±4.04% ). Thus, a QSM attains the largest depth-32 mean among the tested quantum models
in each of the four benchmark cases (Figure 3 and Table 1).
Across the six test-accuracy-versus-depth curves, the global block-Hamiltonian QSM has the largest
observed mean for all four cases, occurring at depth 16 with 93.81%±1.06% , 86.66%±2.17% ,
86.65%±1.18% and 95.24%±1.53% , respectively. These values summarise the observed depth
sweeps rather than performance at a validation-selected depth; the full curves and depth-32 results
provide the corresponding depth-specific comparisons. Appendix Section F reports the validation
summaries and validation-accuracy AUCs.
The depth-32 comparisons show that the largest mean test accuracy is obtained by a QSM across
structurally different inputs and spectral rules. TheDYN input is an ordered 8×2 trajectory, and its four
non-overlapping 2×2 patches correspond to consecutive trajectory segments. By contrast, STA4 is a
4×4 bitmap-like representation whose patches preserve local two-dimensional neighbourhoods, while
the two synthetic labels depend on full-matrix eigengap or singular-value statistics. These contrasting
input structures and task definitions provide the context for the encoder-specific performance patterns
discussed below.
The rotation-gate baselines attain larger means on DYN than on STA4, both at depth 32 and at their
highest observed means. This difference may reflect how DYN exposes coordinate values in their
recorded sequence, whereas STA4 organises them within a two-dimensional bitmap neighbourhood.
The strongest rotation-gate result on DYN, 81.37%±2.36% for trainable-frequency Ry at depth 32,
remains below the depth-32 means of all three QSMs. On STA4, the explicit 2×2 locality of the
patch-local block-Hamiltonian QSM offers a possible interpretation of its performance, paralleling
the spatial locality encoded by convolutional networks [27]. Taken together, these patterns suggest an
interaction between data-encoding construction and input layout; the specific contribution of locality
remains unresolved.
QSMs with Hamiltonian-based data-encoding unitaries retain stronger high-depth gradient
signals, while gradient scale alone does not determine accuracy.At L= 32 , the median log10
mixer-gradient variance [39] of the fixed and trainable-frequency rotation-gate data-encoding unitaries
is approximately −11 on Pendigits and −20 on the synthetic tasks. For Hblock, the corresponding
10

20 21 22 23 24 25
Re-upload depth
0.2
0.4
0.6
0.8
1.0
final test accuracy
DYN
20 21 22 23 24 25
Re-upload depth
0.2
0.4
0.6
0.8
final test accuracy
STA4
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(a)
20 21 22 23 24 25
Re-upload depth
0.50
0.55
0.60
0.65
0.70
0.75
0.80
0.85
final test accuracy
SYNTHETIC EIGENGAP
20 21 22 23 24 25
Re-upload depth
0.60
0.65
0.70
0.75
0.80
0.85
0.90
0.95
final test accuracy
SYNTHETIC SINGULAR
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(b)
Figure 3:(a) Final test accuracy on the Pendigits benchmark as a function of reuploading depth.
The two panels show the DYN8×2 trajectory representation and the STA44×4 matrix representation.
Each point is the mean over 20 parameter-initialisation seeds, and error bars show one standard
deviation across seeds. QSMs lead the tested depth-32 comparisons. The global block-Hamiltonian
QSM has the largest observed mean across the six depths on both representations, while the patch-
local block-Hamiltonian QSM has the largest mean at depth 32.(b) Final test accuracy on the two
synthetic spectral benchmarks as a function of reuploading depth.The SYNTHETIC EIGENGAP
task uses noisy 4×4 symmetric matrices with labels determined by the largest latent eigengap, while
the SYNTHETIC SINGULAR task uses noisy 8×2 matrices with labels determined by the sum of the
two leading latent singular values. Each point is the mean over 20 seeds, and error bars show one
standard deviation across seeds. The global block-Hamiltonian QSM has the largest mean at depth
32 and the largest observed mean across the six depths on both tasks.
values are −1.05±0.05 on Pendigits DYN, 0.05±0.20 on STA4, −3.72±0.05 on SYNTHETIC
EIGENGAP and −3.64±0.04 on SYNTHETIC SINGULAR . We compute these training-loss gradients
on a fixed diagnostic batch of 32 examples and separate the shared SU(4) mixer parameters from
encoder-specific parameters. Within each run seed, the initialisation statistic measures the coordinate-
wise variance of each parameter gradient across 20 parameter initialisations; we take the median log
variance across a parameter group and then aggregate the run-level values over 20 run seeds, with
sample-standard-deviation error bars. The coordinate-wise rotation encoders therefore show much
more strongly suppressed parameter-wise variation across initialisations at high depth. Appendix
Section G defines this statistic and the remaining gradient diagnostics.
The final-checkpoint root-mean-square (RMS) gradient gives a separate snapshot after optimisation
(Figure 4b). At depth 32, the mixer-gradient RMS values for Hsym and Hblock are 0.079±0.034
and 0.071±0.034 on Pendigits DYN, 0.164±0.053 and 0.194±0.169 on STA4, 0.108±0.019
and 0.062±0.011 on SYNTHETIC EIGENGAP , and 0.061±0.015 and 0.036±0.009 on SYNTHETIC
SINGULAR. On the synthetic tasks these values exceed the rotation-gate baseline values, which are
11

Re-upload depth
30
20
10
0
SU(4) mixer
median log10
gradient variance
Pendigits DYN
Re-upload depth
30
20
10
0
Pendigits STA4
Re-upload depth
30
20
10
Synthetic eigengap
Re-upload depth
30
20
10
Synthetic singular
Re-upload depth
30
25
20
15
Trainable
frequencies
median log10
gradient variance
 Re-upload depth
30
25
20
15
Re-upload depth
30
28
26
24
22
Re-upload depth
30
28
26
24
22
Re-upload depth
5
4
3
2
1
Upload times
median log10
gradient variance
 Re-upload depth
4
2
0
Re-upload depth
30
20
10
Re-upload depth
30
20
10
21 23 25
Re-upload depth
4.0
3.5
3.0
2.5
Patch map
median log10
gradient variance
 21 23 25
Re-upload depth
3.50
3.25
3.00
2.75
2.50
21 23 25
Re-upload depth
30
20
10
21 23 25
Re-upload depth
30
20
10
fixed-ry
fixed-ry-rz
trainable-frequency-ry
patch-su4
trainable-patch-su4
non-overlap-patch-block-hamiltonian
symmetric-hamiltonian
block-hamiltonian
(a)
Re-upload depth
10 1
SU(4) mixer
mean RMS
gradient
Pendigits DYN
Re-upload depth
10 1
Pendigits STA4
Re-upload depth
10 2
10 1
Synthetic eigengap
Re-upload depth
10 2
Synthetic singular
Re-upload depth
10 1
Trainable
frequencies
mean RMS
gradient
Re-upload depth
2 × 10 2
3 × 10 2
4 × 10 2
Re-upload depth
10 2
3 × 10 3
4 × 10 3
6 × 10 3
Re-upload depth
10 2
Re-upload depth
10 2
10 1
Upload times
mean RMS
gradient
Re-upload depth
10 1
Re-upload depth
10 2
Re-upload depth
10 3
10 2
21 23 25
Re-upload depth
10 1
4 × 10 2
6 × 10 2
Patch map
mean RMS
gradient
21 23 25
Re-upload depth
10 1
4 × 10 2
6 × 10 2
21 23 25
Re-upload depth
10 2
21 23 25
Re-upload depth
10 2
2 × 10 2
fixed-ry
fixed-ry-rz
trainable-frequency-ry
patch-su4
trainable-patch-su4
non-overlap-patch-block-hamiltonian
symmetric-hamiltonian
block-hamiltonian
(b)
Figure 4:(a) Gradient variance at initialisation as a function of reuploading depth.For each run
configuration, gradients are computed on a fixed diagnostic training batch of size 32 for 20 random
initialisations. The plotted quantity is the median log10 variance across parameters within each
parameter group, averaged over 20 run seeds; error bars show one standard deviation across run seeds.
The coordinate-wise rotation-gate data-encoding unitaries exhibit strongly suppressed mixer-gradient
variance at large depth, whereas the QSMs retain substantially larger initialisation variance.(b)
Final-checkpoint RMS gradient as a function of reuploading depth.Gradients are computed
at the final trained checkpoint using the same diagnostic-batch procedure as in the initialisation
diagnostics. The RMS is computed within each parameter group, and plotted values are means over
20 run seeds with one-standard-deviation error bars. The QSMs retain finite gradients at high depth,
while the rotation-gate data-encoding unitaries generally show smaller final mixer-gradient scales,
especially on the synthetic spectral tasks.
12

Table 1:Final test accuracy for the main Pendigits and synthetic benchmark runs.Values are
mean ± standard deviation over 20 random seeds, reported in percentages. The largest-observed-
mean columns report the depth and value of the maximum mean test accuracy across the six evaluated
depths for each dataset–encoder pair, providing a descriptive summary of the depth sweep. The
depth-32 column reports the same metric at the largest reuploading depth used in the experiments.
Boldface marks the largest mean within each dataset block and accuracy column.
Dataset Encoder
Depth of largest
observed mean
Largest observed mean
test acc. (%)
Depth-32 test
acc. (%)
Pendigits DYN fixed-R y 1675.02±2.63 72.29±2.77
fixed-RyRz 864.14±2.26 55.84±5.30
trainable-frequency(TF)-Ry 3281.37±2.36 81.37±2.36
patch-SU(4)448.60±1.87 9.96±0.44
trainable patch-SU(4)274.70±2.04 9.84±0.47
patchH block 3292.75±0.8492.75±0.84
Hsym 3291.89±3.71 91.89±3.71
Hblock 1693.81±1.0692.35±5.95
Pendigits STA4 fixed-R y 861.10±4.35 40.22±4.40
fixed-RyRz 1652.47±3.49 32.79±4.28
TF-Ry 870.11±2.35 46.85±6.39
patch-SU(4)434.51±1.08 16.41±1.88
trainable patch-SU(4)254.94±2.88 10.27±0.62
patchH block 3286.14±1.3386.14±1.33
Hsym 1670.14±8.29 59.79±14.90
Hblock 1686.66±2.1776.38±16.84
Synthetic eigengap fixed-R y 867.57±0.98 65.40±1.69
fixed-RyRz 866.47±1.18 65.55±1.22
TF-Ry 868.24±1.62 67.42±1.33
patch-SU(4)463.19±1.72 54.58±1.97
trainable patch-SU(4)271.12±1.33 50.16±2.36
patchH block 1674.37±2.59 71.44±2.11
Hsym 1683.42±1.37 82.81±3.16
Hblock 1686.65±1.18 85.15±2.40
Synthetic singular fixed-R y 1685.00±1.15 84.34±1.24
fixed-RyRz 3284.54±1.01 84.54±1.01
TF-Ry 3285.40±0.63 85.40±0.63
patch-SU(4)477.50±2.00 63.41±2.03
trainable patch-SU(4)486.45±1.52 61.75±1.91
patchH block 3287.50±2.06 87.50±2.06
Hsym 890.16±1.08 88.75±2.69
Hblock 1695.24±1.53 92.72±4.04
near 10−2, showing that several high-performing QSMs retain larger mixer-gradient scales at the
final checkpoint.
The empirical-Fisher diagnostic is the Gram matrix of per-example, ground-truth-label loss gradients,
following the common machine-learning convention [25]. We use its effective rank as a finite-batch
summary of how the sampled gradient energy is distributed across parameter-space directions. At
depth 32 on Pendigits DYN, patch-SU(4) has empirical-Fisher effective rank 29.25±0.52 but test
accuracy 9.96%±0.44% . The corresponding values for Hblock are 9.39±2.72 and 92.35%±5.95%
(Appendix Section G and Table 4). In this comparison, the empirical-Fisher effective-rank ordering
does not match the test-accuracy ordering.
The gradient results establish two complementary observations: extreme initialisation-variance sup-
pression accompanies the lower high-depth accuracy of the rotation-gate data-encoding unitaries,
while the patch-SU(4) controls show that larger gradient variance or empirical-Fisher rank is in-
sufficient for high accuracy. These diagnostics describe the optimisation geometry of the tested
runs but do not establish a causal mechanism or a necessary gradient condition for the QSM results.
Appendix Section G gives the complete metric definitions, while Figures 8 and 9 reports additional
initialisation-RMS and empirical-Fisher results.
13

Several high-performing quantum spectral models develop more label-aligned fidelity geometry.
At high depth, several of these models show largerwithin-minus-between fidelity gaps and stronger
kernel-target alignment than the coordinate-wise rotation and patch-SU(4)baselines (see Figure 5).
We form the pure-state fidelity kernel Kij =| ⟨ψi|ψj⟩ |2 from the final post-mixer states of a fixed
32-example validation batch. Centred kernel-target alignment [10, 9, 23] compares this kernel with
the label-equality kernel, while thewithin-minus-between fidelity gap, motivated by class separation
in quantum metric learning [ 34], is the mean same-label fidelity minus the mean different-label
fidelity after excluding self-pairs (Equation (171)). Positive gaps indicate greater average similarity
within classes on the diagnostic batch. Except for the 20-seed test accuracies in Table 5, all latent
diagnostics use seed 0 and have no cross-seed uncertainty estimates; the appendix expands this
provenance and scope.
At depth 32 on Pendigits DYN, Hblock has diagnostic-batch accuracy 1.000, target alignment 0.900
and fidelity gap 0.561; Hsym gives 1.000, 0.887 and 0.538, respectively (Table 5). On STA4, patch
Hblock has diagnostic-batch accuracy 0.938, target alignment 0.694 and gap 0.173. On SYNTHETIC
SINGULAR, Hsym and Hblock give target alignments of 0.508 and 0.461 and gaps of 0.163 and 0.159.
These observations show that several high-performing QSMs form visibly class-separated fidelity
geometry within the diagnostic batch.
The fidelity gap and participation-ratio effective rank describe complementary aspects of the kernel
geometry: the former measures label separation, while the latter measures how broadly the kernel
eigenvalue mass is distributed across eigenmodes. At depth 32, the rotation-gate data-encoding
unitaries have kernel effective rank near the batch-size maximum of 32 while their gaps are approxi-
mately zero (see Figure 11). The patch-SU(4) data-encoding unitaries show the same combination
of high effective rank, near-zero gap and low diagnostic-batch accuracy. Near-maximal effective rank
in a fidelity kernel is consistent with an identity-like Gram matrix, a limiting geometry that can arise
through exponential concentration and impair generalisation in quantum kernel methods [48]. The
positive gaps of several QSMs instead indicate class-dependent off-diagonal structure within this
diagnostic batch.
Appendix Section H gives the corresponding layerwise and checkpoint trajectories, including the
fidelity gap, target alignment and adjacent-layer CKA.
Classical baselines probe which representations make each task accessible.The synthetic
labels are defined by spectral statistics of the clean latent matrices. On SYNTHETIC EIGENGAP ,
the Hsym-eigenvalue MLP reaches 98.01%±0.35% , compared with the largest observed QSM
mean of 86.65%±1.18% . On SYNTHETIC SINGULAR , the Hblock-singular-value MLP reaches
98.50%±0.20%, compared with 95.24%±1.53%. These near-ceiling accuracies provide an empirical
check that the noisy observations retain the intended label-defining spectral signal, supporting the use
of these benchmarks as controlled tests of eigenvalue- and singular-value-dependent learning.
On Pendigits, one-hidden-layer MLPs trained on raw entries reach 96.88%±0.24% on DYN and
91.32%±0.46% on STA4 (see Table 6). By contrast, MLPs trained only on Hsym eigenvalues
reach 59.98%±0.60% and 39.80%±0.50% , while those trained on Hblock singular values reach
39.67%±0.48% and 30.62%±0.53% . Under this protocol, reducing each input to its spectral values
therefore removes substantial task-relevant information available in the raw matrices. The classical
baselines reveal a task-dependent contrast: spectral values are almost sufficient for the controlled
synthetic tasks, but not for Pendigits. The value–subspace ablations below examine how this contrast
appears within the QSM representations.
Ablations reveal task-dependent roles for spectral values and subspaces.The central ablation
result is a reversal between the real-world and controlled tasks (see Table 2). The spectral-value
controls retain each sample’s values while using fixed reference bases derived from the training split.
The spectral-subspace controls instead retain each sample’s eigenvectors or singular vectors while
replacing its values by coordinate-wise training-set medians. On Pendigits, the subspace-retaining
controls preserve much more accuracy than the spectral-value controls. On the synthetic tasks, where
the labels are defined by the corresponding spectral statistics, the spectral-value controls become
strongest and the subspace-retaining controls are much weaker. This reversal shows that the useful
component of sample-conditioned spectral geometry depends on the structure of the learning problem.
To summarise performance across depth, we compare the largest mean test accuracy observed for
each ablation over the six evaluated depths.
14

1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
0.25 0.02 0.00
0.17 0.00 0.00
0.27 0.03 0.00
0.06 0.00 -0.00
0.14 0.00 -0.00
0.35 0.31 0.26
0.14 0.45 0.54
0.19 0.47 0.56
Pendigits DYN
1 8 32
Re-upload depth
0.07 0.00 0.00
0.06 0.00 -0.00
0.07 0.02 0.00
0.01 0.01 -0.00
0.10 0.00 -0.00
0.11 0.20 0.17
0.17 0.26 0.21
0.22 0.31 0.29
Pendigits STA4
1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
0.00 0.00 -0.00
-0.00 -0.00 -0.00
-0.00 0.00 -0.00
0.00 0.00 -0.00
0.00 -0.00 0.00
0.02 0.01 -0.00
-0.00 0.05 0.08
-0.00 0.04 0.05
Synthetic eigengap
1 8 32
Re-upload depth
0.05 0.00 0.00
0.06 0.00 0.00
0.06 0.00 0.00
0.02 0.00 0.00
0.02 0.00 0.00
0.11 0.04 0.06
0.04 0.13 0.16
0.08 0.22 0.16
Synthetic singular
0.0
0.1
0.2
0.3
0.4
0.5
(a)
1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
0.74 0.56 0.54
0.70 0.54 0.54
0.75 0.56 0.54
0.60 0.54 0.54
0.67 0.54 0.54
0.77 0.79 0.76
0.53 0.80 0.89
0.55 0.83 0.90
Pendigits DYN
1 8 32
Re-upload depth
0.60 0.54 0.54
0.60 0.54 0.54
0.60 0.55 0.54
0.55 0.54 0.53
0.63 0.54 0.53
0.59 0.69 0.69
0.41 0.65 0.59
0.51 0.71 0.69
Pendigits STA4
1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
0.15 0.18 0.18
0.16 0.18 0.18
0.14 0.18 0.18
0.18 0.18 0.18
0.18 0.18 0.18
0.16 0.18 0.17
0.07 0.19 0.26
0.07 0.23 0.26
Synthetic eigengap
1 8 32
Re-upload depth
0.31 0.19 0.18
0.33 0.18 0.18
0.28 0.19 0.18
0.23 0.18 0.18
0.23 0.18 0.18
0.40 0.27 0.32
0.21 0.41 0.51
0.34 0.53 0.46
Synthetic singular
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
(b)
Figure 5:(a) Within-minus-between fidelity gap of the final quantum states.For each trained
model, we compute the pure-state fidelity kernel Kij =| ⟨ψi|ψj⟩ |2 on a fixed 32-example validation
diagnostic batch and report the mean same-label off-diagonal fidelity minus the mean different-label
off-diagonal fidelity. Larger values indicate stronger class separation in quantum-state geometry.
At high depth, the global QSMs and the patch-local block-Hamiltonian QSM produce substantially
larger gaps than the coordinate-wise rotation-gate and patch- SU(4) baselines.(b) Kernel-target
alignment of the final quantum-state fidelity kernel.The plotted metric is the centred alignment
between the final fidelity kernel and the label-equality kernel on the same batch. Larger values
indicate that the geometry of the trained quantum states is more aligned with class membership.
Several high-performing QSMs show stronger alignment in the high-depth regime; this is a descriptive
association rather than evidence that the data-encoding unitary causes the accuracy ordering. Both
panels use the final checkpoint from seed 0 and contain no across-seed uncertainty estimate.
15

Table 2:Value–subspace ablation summary.Entries give the depth and largest observed mean final
test accuracy (mean± standard deviation over 20 random seeds, in percentage) for the original encoder
and the corresponding value-only and subspace-only controls. Every entry is a descriptive maximum
across the tested depths rather than performance at a depth selected by independent validation; each
control is retrained on its transformed dataset. Pendigits depends primarily on sample-dependent
subspaces, whereas the controlled spectral tasks reverse the ordering. The complete ablation and
permutation results are reported in Appendix Table 7.
Task
(reference encoder)
Original
(depth, acc.)
Spectral values only
(depth, acc.)
Spectral subspaces only
(depth, acc.)
Primary observed
dependence
Pendigits DYN
(Hblock) L16,93.81±1.06L4,31.65±2.44L16,93.56±0.84subspaces
Pendigits STA4
(Hblock) L16,86.66±2.17L4,25.25±2.02L16,84.74±4.51subspaces
Synthetic eigengap
(Hsym) L16,83.42±1.37L8,97.92±0.38L1,61.28±0.07values
Synthetic singular
(Hblock) L16,95.24±1.53L32,98.42±0.30L16,49.88±1.96values
On Pendigits DYN and STA4, the Hblock spectral-value controls reach 31.65%±2.44% and 25.25%±
2.02%, whereas the spectral-subspace controls retain 93.56%±0.84% and 84.74%±4.51% . The
Hsym controls show the same ordering: spectral-value accuracies are 48.87%±3.90% and 28.35%±
2.11%, compared with 89.80%±4.56% and 64.30%±2.02% when sample-dependent eigenvectors
are retained. Within these ablations, the Pendigits results therefore depend much more strongly on
sample-dependent spectral subspaces than on spectral values alone.
The synthetic controls reverse this performance ordering. The Hsym spectral-value control reaches
97.92%±0.38% on SYNTHETIC EIGENGAP , whereas its spectral-subspace counterpart reaches
61.28%±0.07% . On SYNTHETIC SINGULAR , the corresponding Hblock values are 98.42%±0.30%
and 49.88%±1.96% . This reversal agrees with the data-generating rules and demonstrates that
spectral values and subspaces can play different roles under the same upload–mixer architecture.
Fixed row and column permutations preserve singular values, whereas a general entry permutation
does not. On SYNTHETIC SINGULAR , the largest observed mean for globalHblock is 95.06%±2.30%
after row/column permutation, 0.18 percentage points below the original, and 90.55%±0.58% after
entry permutation, 4.69 points below. For patch Hblock on STA4, entry and row/column permutations
reduce the largest observed means by 3.04 and 2.22 points. This sensitivity is compatible with the
use of fixed 2×2 patches, but does not isolate locality as its cause. The complete value/subspace and
permutation results are given in Appendix Table 7.
7 Discussion and Outlook
Quantum Spectral Models (QSMs) operate in the spectral domain of each matrix input: we construct
an input-dependent Hermitian generator from the matrix and use its time-evolution operator as the
data-encoding unitary. For the symmetric- and block-Hamiltonian data-encoding unitaries, eigengaps
or signed singular-value gaps determine the sample-conditioned candidate phase carriers. The
associated spectral projectors represent the input-dependent subspaces that enter the corresponding
Fourier coefficients. Candidate support specifies the carriers that are available in principle, whereas
realised support contains only those whose coefficients remain nonzero after the initial state, trainable
mixing and measurement observable are taken into account. Common coordinate-wise quantum
Fourier models (QFMs) instead use architecture-defined candidate support, while trainable-frequency
rotation-gate QFMs learn support that remains globally shared across samples after training [46, 21].
The key difference is that, in a QSM, both the candidate phase carriers and the spectral subspaces
entering the corresponding Fourier coefficients depend on the individual input matrix.
At the largest evaluated depth, a QSM variant attains the highest mean test accuracy among the tested
quantum models on each of the four benchmarks. The patch-local block-Hamiltonian QSM leads
on the two Pendigits representations, whereas the global block-Hamiltonian QSM leads on the two
controlled spectral tasks (see Figure 3 and Table 1). Together with the differing trends across the full
16

depth sweeps, this task-dependent ordering shows that the effect of circuit depth is specific to the
encoder and dataset.
One possible, non-causal interpretation of the change in the depth-32 winner concerns the scale of
structure exposed by each encoder. The two synthetic labels are defined by spectral statistics of the
complete clean latent matrix, whereas each Pendigits input contains an explicit local organisation. For
DYN, the four non-overlapping 2×2 patches are four consecutive two-point segments of the ordered
pen trajectory; for STA4, they are four contiguous2×2 quadrants of the bitmap-like matrix. The patch-
local QSM therefore preserves these trajectory segments or spatial neighbourhoods, while the global
block-Hamiltonian QSM retains relations across the full matrix. This correspondence is consistent
with a locality-based inductive-bias interpretation and motivates future controlled comparisons that
isolate locality from other encoder differences and clarify its contribution to the observed accuracy
ordering.
The gradient and fidelity diagnostics add complementary descriptive evidence. At large depth, we
observe extreme suppression of mixer-gradient variance across initialisations for the coordinate-
wise rotation-gate encoders, whereas the QSMs retain greater variance and several high-performing
variants retain larger final gradient scales (see Figure 4). In the fixed diagnostic batch, several QSMs
also develop larger fidelity gaps and stronger kernel-target alignment (see Figure 5). The patch-SU(4)
controls further show that the gradient and fidelity diagnostics capture different aspects of the learned
model geometry. Future work could investigate how these measures interact throughout training and
whether their joint behaviour provides a more complete account of predictive performance.
The value-versus-subspace ablations provide the most direct representational evidence. On Pendigits,
value-only controls lose most of the original accuracy, while controls that preserve sample-dependent
eigenvectors or singular vectors retain much more performance (Tables 2 and 7). The ordering
reverses on the controlled spectral tasks, where the labels are defined by an eigengap or a leading-
singular-value sum and the value-only controls become strongest. This task-dependent division
of labour shows that spectral values make the synthetic rules directly accessible, whereas spectral
subspaces and trainable mixing carry much of the useful information for Pendigits.
These results point to a general representation-design question: should a spectral representation be
shared across a dataset or adapted to each input? Coordinate-wise QFMs use architecture-defined
carriers, trainable-frequency QFMs learn support shared across samples, and several classical spectral
architectures use fixed or domain-derived operators or Fourier-space maps learned across a training
distribution [5, 30]. A QSM takes a different approach by constructing the data-encoding generator
from each input matrix, so that both the gap-derived candidate phase carriers and the spectral
subspaces entering the Fourier coefficients adapt to the input. Because the time evolution of a
Hermitian generator is governed by its eigenvalues and spectral projectors, using the input matrix
as the generator makes spectral structure intrinsic to the data-encoding dynamics. This provides a
particularly direct route to input-adaptive spectral representation learning in quantum models and
motivates further investigation of when such representations are useful across quantum and classical
models.
Building on these results, future work can test how broadly the observed representation effects persist
across model scales, datasets and resource constraints. Resource-matched comparisons could hold
qubit count, parameter count and locality fixed, select depth through independent validation, retain
the task-appropriate classical baselines that lead on the present benchmarks, and extend the analysis
to larger matrix-structured datasets. The nonzero fidelity gaps of several QSMs at the studied sizes
also motivate qubit-scaling and finite-shot analyses of whether Hamiltonian-based data encodings
resist exponential kernel concentration [48]. Multi-seed latent-state diagnostics across independent
batches, together with controlled global-versus-patch-local and structure-destroying ablations, could
further clarify how spectral subspaces, locality and trainability interact. Together, these directions
provide a path towards hardware-relevant, resource-normalised evaluations of whether the observed
representation effects can support end-to-end quantum advantage.
A complementary direction for future work is to develop scalable implementations of dense input-
dependent matrix operations. This would involve specifying the data-access or block-encoding
assumptions [35, 36], accounting for data-loading and circuit costs, and examining noise in hardware-
relevant settings. At the representation level, quantum singular value transformation or eigenvalue
processing could provide controlled tests of spectral values while variational operations act on the
17

associated subspaces [15, 37]. Investigating how these approaches depend on matrix structure and
access cost could connect QSM representation design with scalable quantum implementations.
Taken together, our formal analysis and experiments establish QSMs as an analysable framework
for input-adaptive spectral representation learning. The input-derived Hamiltonian supplies sample-
conditioned candidate phase carriers through its spectral gaps, while the associated spectral subspaces
interact with the initial state, trainable mixer and measurement observable to determine which carriers
are realised and with what coefficients. This support–coefficient perspective provides a concrete
principle for designing quantum models around matrix-valued data and offers a new lens for studying
how data-dependent structure can be embedded directly into model dynamics.
18

Data and Code Availability
Code available athttps://github.com/peiyong-addwater/QuantumSpectralModel.
References
[1] E. Alpaydin and Fevzi. Alimoglu. Pen-Based Recognition of Handwritten Digits. UCI Machine
Learning Repository, 1996. DOI: https://doi.org/10.24432/C5MG6K.
[2] Eric R Anschuetz and Bobak T Kiani. Quantum variational algorithms are swamped with
traps.Nat. Commun., 13(1):7760, 15 December 2022. ISSN 2041-1723. doi: 10.1038/
s41467-022-35364-5. URLhttp://dx.doi.org/10.1038/s41467-022-35364-5.
[3] Peter W Battaglia, Jessica B Hamrick, Victor Bapst, Alvaro Sanchez-Gonzalez, Vinicius Zam-
baldi, Mateusz Malinowski, Andrea Tacchetti, David Raposo, Adam Santoro, Ryan Faulkner,
Caglar Gulcehre, Francis Song, Andrew Ballard, Justin Gilmer, George Dahl, Ashish Vaswani,
Kelsey Allen, Charles Nash, Victoria Langston, Chris Dyer, Nicolas Heess, Daan Wierstra,
Pushmeet Kohli, Matt Botvinick, Oriol Vinyals, Yujia Li, and Razvan Pascanu. Relational
inductive biases, deep learning, and graph networks.arXiv [cs.LG], 4 June 2018. doi:
10.48550/arXiv.1806.01261. URLhttp://arxiv.org/abs/1806.01261.
[4] Vasilis Belis, Joseph Bowles, Rishabh Gupta, Evan Peters, and Maria Schuld. Spectral methods:
crucial for machine learning, natural for quantum computers?arXiv [quant-ph], 25 March
2026. doi: 10.48550/arXiv.2603.24654. URLhttp://arxiv.org/abs/2603.24654.
[5] Joan Bruna, Wojciech Zaremba, Arthur Szlam, and Yann LeCun. Spectral networks and locally
connected networks on graphs, 2014. URLhttps://arxiv.org/abs/1312.6203.
[6] Daan Camps and Roel Van Beeumen. Fable: Fast approximate quantum circuits for block-
encodings. In2022 IEEE International Conference on Quantum Computing and Engineering
(QCE), pages 104–113. IEEE, September 2022. doi: 10.1109/qce53715.2022.00029. URL
http://dx.doi.org/10.1109/QCE53715.2022.00029.
[7] Daan Camps, Lin Lin, Roel Van Beeumen, and Chao Yang. Explicit quantum circuits for block
encodings of certain sparse matrices, 2023. URLhttps://arxiv.org/abs/2203.10236.
[8] M Cerezo, Andrew Arrasmith, Ryan Babbush, Simon C Benjamin, Suguru Endo, Keisuke
Fujii, Jarrod R McClean, Kosuke Mitarai, Xiao Yuan, Lukasz Cincio, and Patrick J Coles.
Variational quantum algorithms.Nat. Rev. Phys., 3(9):625–644, 12 August 2021. ISSN 2522-
5820,2522-5820. doi: 10.1038/s42254-021-00348-9. URL http://dx.doi.org/10.1038/
s42254-021-00348-9.
[9] Corinna Cortes, Mehryar Mohri, and Afshin Rostamizadeh. Algorithms for learning kernels
based on centered alignment.J. Mach. Learn. Res., 13(1):795–828, March 2012. ISSN
1532-4435.
[10] Nello Cristianini, John Shawe-Taylor, Andre Elisseeff, and Jaz Kandola. On kernel-target align-
ment. InProceedings of the 15th International Conference on Neural Information Processing
Systems: Natural and Synthetic, NIPS’01, page 367–373, Cambridge, MA, USA, 2001. MIT
Press.
[11] Pierre-Luc Dallaire-Demers and Nathan Killoran. Quantum generative adversarial networks.
Phys. Rev. A, 98(1):012324, 23 July 2018. doi: 10.1103/PhysRevA.98.012324. URL http:
//dx.doi.org/10.1103/PhysRevA.98.012324.
[12] Michaël Defferrard, Xavier Bresson, and Pierre Vandergheynst. Convolutional neural networks
on graphs with fast localized spectral filtering. InProceedings of the 30th International
Conference on Neural Information Processing Systems, NIPS’16, page 3844–3852, Red Hook,
NY , USA, 2016. Curran Associates Inc. ISBN 9781510838819.
[13] Edward Farhi and Hartmut Neven. Classification with quantum neural networks on near term
processors, 2018. URLhttps://arxiv.org/abs/1802.06002.
19

[14] Peiran Gao, Eric Trautmann, Byron Yu, Gopal Santhanam, Stephen Ryu, Krishna Shenoy,
and Surya Ganguli. A theory of multineuronal dimensionality, dynamics and measurement.
bioRxiv preprint, November 2017. URL https://www.biorxiv.org/content/10.1101/
214262v2.
[15] András Gilyén, Yuan Su, Guang Hao Low, and Nathan Wiebe. Quantum singular value
transformation and beyond: exponential improvements for quantum matrix arithmetics. In
Proceedings of the 51st Annual ACM SIGACT Symposium on Theory of Computing, New York,
NY , USA, 23 June 2019. ACM. ISBN 9781450367059. doi: 10.1145/3313276.3316366. URL
http://dx.doi.org/10.1145/3313276.3316366.
[16] Andi Gu, Lukasz Cincio, and Patrick J Coles. Practical hamiltonian learning with uni-
tary dynamics and gibbs states.Nat. Commun., 15(1):312, 8 January 2024. ISSN 2041-
1723,2041-1723. doi: 10.1038/s41467-023-44008-1. URL http://dx.doi.org/10.1038/
s41467-023-44008-1.
[17] John Guibas, Morteza Mardani, Zongyi Li, Andrew Tao, Anima Anandkumar, and Bryan
Catanzaro. Efficient token mixing for transformers via adaptive fourier neural operators. In
International Conference on Learning Representations, 2022. URL https://openreview.
net/forum?id=EXHG-A3jlM.
[18] Jeongwan Haah, Robin Kothari, and Ewin Tang. Learning quantum hamiltonians from high-
temperature gibbs states and real-time evolutions.Nat. Phys., 20(6):1027–1031, 6 June 2024.
ISSN 1745-2473,1745-2481. doi: 10.1038/s41567-023-02376-x. URL http://dx.doi.org/
10.1038/s41567-023-02376-x.
[19] Hong-Ye Hu, Muzhou Ma, Weiyuan Gong, Qi Ye, Yu Tong, Steven T Flammia, and Susanne F
Yelin. Ansatz-free hamiltonian learning with heisenberg-limited scaling.PRX quantum, 6(4):
040315, 22 October 2025. ISSN 2691-3399. doi: 10.1103/j7b8-pb77. URLhttp://dx.doi.
org/10.1103/j7b8-pb77.
[20] He-Liang Huang, Yuxuan Du, Ming Gong, Youwei Zhao, Yulin Wu, Chaoyue Wang, Shaowei
Li, Futian Liang, Jin Lin, Yu Xu, Rui Yang, Tongliang Liu, Min-Hsiu Hsieh, Hui Deng, Hao
Rong, Cheng-Zhi Peng, Chao-Yang Lu, Yu-Ao Chen, Dacheng Tao, Xiaobo Zhu, and Jian-Wei
Pan. Experimental quantum generative adversarial networks for image generation.Physical
Review Applied, 16(2), August 2021. ISSN 2331-7019. doi: 10.1103/physrevapplied.16.024051.
URLhttp://dx.doi.org/10.1103/PhysRevApplied.16.024051.
[21] Ben Jaderberg, Antonio A Gentile, Youssef Achari Berrada, Elvira Shishenina, and Vincent E
Elfving. Let quantum neural networks choose their own frequencies.Phys. Rev. A, 109(4):
042421, 22 April 2024. ISSN 2469-9926,2469-9934. doi: 10.1103/physreva.109.042421. URL
http://dx.doi.org/10.1103/PhysRevA.109.042421.
[22] Diederik P Kingma and Jimmy Ba. Adam: A method for stochastic optimization.arXiv [cs.LG],
22 December 2014. doi: 10.48550/arXiv.1412.6980. URL http://arxiv.org/abs/1412.
6980.
[23] Simon Kornblith, Mohammad Norouzi, Honglak Lee, and Geoffrey Hinton. Similarity of
neural network representations revisited. InInternational Conference on Machine Learning,
pages 3519–3529. PMLR, 24 May 2019. URL https://proceedings.mlr.press/v97/
kornblith19a.html.
[24] Nikola Kovachki, Zongyi Li, Burigede Liu, Kamyar Azizzadenesheli, Kaushik Bhattacharya,
Andrew Stuart, and Anima Anandkumar. Neural operator: learning maps between function
spaces with applications to pdes.J. Mach. Learn. Res., 24(1), January 2023. ISSN 1532-4435.
[25] Frederik Kunstner, Lukas Balles, and Philipp Hennig. Limitations of the em-
pirical fisher approximation for natural gradient descent. InAdvances in Neu-
ral Information Processing Systems, volume 32, pages 4156–4167. Curran Asso-
ciates, Inc., 2019. URL https://proceedings.neurips.cc/paper/2019/hash/
46a558d97954d0692411c861cf78ef79-Abstract.html.
20

[26] Martín Larocca, Supanut Thanasilp, Samson Wang, Kunal Sharma, Jacob Biamonte, Patrick J
Coles, Lukasz Cincio, Jarrod R McClean, Zoë Holmes, and M Cerezo. Barren plateaus in
variational quantum computing.Nat. Rev. Phys., 7(4):174–189, 26 March 2025. ISSN 2522-
5820,2522-5820. doi: 10.1038/s42254-025-00813-9. URL http://dx.doi.org/10.1038/
s42254-025-00813-9.
[27] Y Lecun, L Bottou, Y Bengio, and P Haffner. Gradient-based learning applied to docu-
ment recognition.Proc. IEEE Inst. Electr. Electron. Eng., 86(11):2278–2324, 1998. ISSN
0018-9219,1558-2256. doi: 10.1109/5.726791. URL https://ieeexplore.ieee.org/
document/726791.
[28] James Lee-Thorp, Joshua Ainslie, Ilya Eckstein, and Santiago Ontañón. FNet: Mixing tokens
with Fourier transforms. In Marine Carpuat, Marie-Catherine de Marneffe, and Ivan Vladimir
Meza Ruiz, editors,Proceedings of the 2022 Conference of the North American Chapter of the
Association for Computational Linguistics: Human Language Technologies, pages 4296–4313,
Seattle, United States, July 2022. Association for Computational Linguistics. doi: 10.18653/v1/
2022.naacl-main.319. URLhttps://aclanthology.org/2022.naacl-main.319/.
[29] Ron Levie, Federico Monti, Xavier Bresson, and Michael M. Bronstein. Cayleynets: Graph
convolutional neural networks with complex rational spectral filters.Trans. Sig. Proc., 67(1):
97–109, January 2019. ISSN 1053-587X. doi: 10.1109/TSP.2018.2879624. URL https:
//doi.org/10.1109/TSP.2018.2879624.
[30] Zongyi Li, Nikola Borislavov Kovachki, Kamyar Azizzadenesheli, Burigede liu, Kaushik
Bhattacharya, Andrew Stuart, and Anima Anandkumar. Fourier neural operator for parametric
partial differential equations. InInternational Conference on Learning Representations, 2021.
URLhttps://openreview.net/forum?id=c8P9NQVtmnO.
[31] Ya-Wei Eileen Lin, Ronen Talmon, and Ron Levie. Equivariant machine learning on graphs
with nonlinear spectral filters. InThe Thirty-eighth Annual Conference on Neural Information
Processing Systems, 2024. URLhttps://openreview.net/forum?id=y8P633E5HQ.
[32] Anthony Yuezhang Liu and Lirandë Pira. The cost of removing tunability in quantum data
re-uploading.arXiv [quant-ph], 24 June 2026. doi: 10.48550/ARXIV .2606.25598. URL
http://arxiv.org/abs/2606.25598.
[33] Seth Lloyd, Samuel Bosch, Giacomo De Palma, Bobak Kiani, Zi-Wen Liu, Milad Marvian,
Patrick Rebentrost, and David M. Arvidsson-Shukur. Quantum polar decomposition algorithm,
2020. URLhttps://arxiv.org/abs/2006.00841.
[34] Seth Lloyd, Maria Schuld, Aroosa Ijaz, Josh Izaac, and Nathan Killoran. Quantum embeddings
for machine learning, 2020. URLhttps://arxiv.org/abs/2001.03622.
[35] Guang Hao Low and Isaac L. Chuang. Optimal hamiltonian simulation by quantum signal
processing.Physical Review Letters, 118(1), January 2017. ISSN 1079-7114. doi: 10.1103/
physrevlett.118.010501. URLhttp://dx.doi.org/10.1103/PhysRevLett.118.010501.
[36] Guang Hao Low and Isaac L. Chuang. Hamiltonian simulation by qubitization.Quantum, 3:
163, July 2019. ISSN 2521-327X. doi: 10.22331/q-2019-07-12-163. URL http://dx.doi.
org/10.22331/q-2019-07-12-163.
[37] Guang Hao Low and Yuan Su. Quantum eigenvalue processing.SIAM J. Comput., 55(1):
135–215, February 2026. ISSN 0097-5397,1095-7111. doi: 10.1137/24m1689363. URL
http://dx.doi.org/10.1137/24M1689363.
[38] Rundi Lu, Ruiqi Zhang, Weikang Li, Zhaohui Wei, Dong-Ling Deng, and Zhengwei Liu. A
unified frequency principle for quantum and classical machine learning.arXiv [quant-ph],
6 January 2026. doi: 10.48550/arXiv.2601.03169. URL http://arxiv.org/abs/2601.
03169.
[39] Jarrod R McClean, Sergio Boixo, Vadim N Smelyanskiy, Ryan Babbush, and Hartmut Neven.
Barren plateaus in quantum neural network training landscapes.Nat. Commun., 9(1):4812,
16 November 2018. ISSN 2041-1723,2041-1723. doi: 10.1038/s41467-018-07090-4. URL
https://www.nature.com/articles/s41467-018-07090-4.
21

[40] Hela Mhiri, Leo Monbroussou, Mario Herrero-Gonzalez, Slimane Thabet, Elham Kashefi, and
Jonas Landman. Constrained and vanishing expressivity of quantum fourier models.Quantum,
9(1847):1847, 3 September 2025. ISSN 2521-327X. doi: 10.22331/q-2025-09-03-1847. URL
http://dx.doi.org/10.22331/q-2025-09-03-1847.
[41] Adrián Pérez-Salinas, Alba Cervera-Lierta, Elies Gil-Fuster, and José I Latorre. Data re-
uploading for a universal quantum classifier.Quantum, 4:226, 6 February 2020. ISSN 2521-
327X. doi: 10.22331/q-2020-02-06-226. URL https://quantum-journal.org/papers/
q-2020-02-06-226/.
[42] Alec Radford, Karthik Narasimhan, Tim Salimans, and Ilya Sutskever. Improving language
understanding by generative pre-training. Online, 2018. URL https://cdn.openai.com/
research-covers/language-unsupervised/language_understanding_paper.pdf.
[43] Nasim Rahaman, Aristide Baratin, Devansh Arpit, Felix Draxler, Min Lin, Fred A Hamprecht,
Yoshua Bengio, and Aaron Courville. On the spectral bias of neural networks.arXiv [stat.ML],
22 June 2018. doi: 10.48550/arXiv.1806.08734. URL http://arxiv.org/abs/1806.08734.
[44] Oren Rippel, Jasper Snoek, and Ryan P Adams. Spectral representations for convolu-
tional neural networks. InAdvances in Neural Information Processing Systems, volume 28,
pages 2449–2457, 2015. URL https://proceedings.neurips.cc/paper/2015/hash/
536a76f94cf7535158f66cfbd4b113b6-Abstract.html.
[45] Maria Schuld and Francesco Petruccione. Representing data on a quantum computer. In Maria
Schuld and Francesco Petruccione, editors,Machine Learning with Quantum Computers, pages
147–176. Springer International Publishing, Cham, 2021. ISBN 9783030830984. doi: 10.1007/
978-3-030-83098-4\_4. URLhttps://doi.org/10.1007/978-3-030-83098-4_4.
[46] Maria Schuld, Ryan Sweke, and Johannes Jakob Meyer. Effect of data encoding on the
expressive power of variational quantum-machine-learning models.Phys. Rev. A, 103(3):
032430, 24 March 2021. ISSN 1050-2947. doi: 10.1103/PhysRevA.103.032430. URL
https://link.aps.org/doi/10.1103/PhysRevA.103.032430.
[47] Jialiang Tang, Jialin Zhang, and Xiaoming Sun. SAQNN: Spectral adaptive quantum neural
network as a universal approximator.arXiv [quant-ph], 10 February 2026. doi: 10.48550/arXiv.
2602.09718. URLhttp://arxiv.org/abs/2602.09718.
[48] Supanut Thanasilp, Samson Wang, M Cerezo, and Zoë Holmes. Exponential concentra-
tion in quantum kernel methods.Nat. Commun., 15(1):5200, 18 June 2024. ISSN 2041-
1723,2041-1723. doi: 10.1038/s41467-024-49287-w. URL http://dx.doi.org/10.1038/
s41467-024-49287-w.
[49] Peiyong Wang, Casey R Myers, Lloyd C L Hollenberg, and Udaya Parampalli. Quantum
hamiltonian embedding of images for data reuploading classifiers.Quantum Mach. Intell., 7
(1):35, June 2025. ISSN 2524-4906,2524-4914. doi: 10.1007/s42484-025-00247-7. URL
http://dx.doi.org/10.1007/s42484-025-00247-7.
[50] Xin Wang, Hanxiao Tao, and Rebing Wu. Predictive performance of deep quantum data
re-uploading models. In Aarti Singh, Maryam Fazel, Daniel Hsu, Simon Lacoste-Julien,
Felix Berkenkamp, Tegan Maharaj, Kiri Wagstaff, and Jerry Zhu, editors,Proceedings of
the 42nd International Conference on Machine Learning, volume 267 ofProceedings of
Machine Learning Research, pages 64491–64524. PMLR, 13–19 Jul 2025. URL https:
//proceedings.mlr.press/v267/wang25cw.html.
[51] Zhi-Qin John Xu, Yaoyu Zhang, Tao Luo, Yanyang Xiao, and Zheng Ma. Frequency principle:
Fourier analysis sheds light on deep neural networks.arXiv [cs.LG], 19 January 2019. URL
http://arxiv.org/abs/1901.06523.
[52] Chengkai Zhu, Shuyu He, Yu-Ao Chen, Lei Zhang, and Xin Wang. Optimal hamiltonian
recognition of unknown quantum dynamics.NPJ Quantum Inf., 12(1):36, 21 January 2026.
ISSN 2056-6387,2056-6387. doi: 10.1038/s41534-026-01182-6. URL http://dx.doi.org/
10.1038/s41534-026-01182-6.
22

Appendix
A Preliminaries on Quantum Computing
This appendix introduces the quantum-computing notation and basic linear-algebraic objects needed
to follow the paper, assuming no prior background in quantum computing or quantum information.
A.1 Quantum states and bra-ket notation
A quantum state is represented by a complex vector. The standard notation for a column vector is a
ket, written as|ψ⟩. Its conjugate transpose is abra, written as⟨ψ|. If
|ψ⟩=


ψ0
ψ1
...
ψd−1

 ∈C d,(28)
then
⟨ψ|=
ψ⋆ 0 ψ⋆ 1 · · ·ψ⋆ d−1, (29)
where ⋆ denotes complex conjugation. The inner product between the two states is written as
⟨ϕ|ψ⟩=
d−1X
j=0
ϕ⋆ j ψj.(30)
This is the usual complex inner product from linear algebra. The squared norm of a state is therefore
⟨ψ|ψ⟩=
d−1X
j=0
|ψj|2.(31)
A valid pure quantum state is normalised:
⟨ψ|ψ⟩= 1.(32)
The entries of |ψ⟩ are calledamplitudes, not probabilities. Measurement probabilities are obtained
by taking squared magnitudes. For example, if
|ψ⟩=α|0⟩+β|1⟩,(33)
then the probability of observing outcome 0 is |α|2, and the probability of observing outcome 1 is
|β|2. Normalisation requires
|α|2 +|β| 2 = 1.(34)
The notation
|ϕ⟩ ⟨ψ|(35)
denotes anouter product, hence a matrix. In particular,
|ψ⟩ ⟨ψ|(36)
is the rank-one projector onto the one-dimensional subspace spanned by |ψ⟩. Projectors of this
type appear throughout quantum machine learning because measurements and readouts are naturally
written as projections onto subspaces.
A.2 Computational basis states
A single qubit is a two-dimensional complex vector. The standard basis vectors are
|0⟩=

1
0

,|1⟩=

0
1

.(37)
23

These are called the computational basis states. A general one-qubit pure state is
|ψ⟩=α|0⟩+β|1⟩=

α
β

,(38)
with|α| 2 +|β| 2 = 1.
For n qubits, the state space has dimension 2n. The computational basis consists of all binary strings
of lengthn:
|b1b2 · · ·bn⟩,b j ∈ {0, 1}.(39)
For example, for two qubits the computational basis is
|00⟩,|01⟩,|10⟩,|11⟩.(40)
A general two-qubit state is
|ψ⟩=α 00 |00⟩+α 01 |01⟩+α 10 |10⟩+α 11 |11⟩,(41)
where
|α00|2 +|α 01|2 +|α 10|2 +|α 11|2 = 1.(42)
More generally, ann-qubit state can be written as
|ψ⟩=
X
b∈{0,1}n
αb |b⟩,
X
b∈{0,1}n
|αb|2 = 1.(43)
Thus ann-qubit state is a length-2 n complex vector indexed by binary strings.
A useful single-qubit state used in the paper is
|+⟩= |0⟩+|1⟩√ 2 .(44)
The initial state in our experiment is
|+⟩⊗n ,(45)
which means that every qubit starts in the |+⟩ state. This is the uniform superposition over all
computational basis states:
|+⟩⊗n = 1√ 2n X b∈{0,1}n |b⟩.(46)
A.3 Tensor products
The tensor product is the operation used to combine quantum systems. If
|a⟩=

a0
a1

,|b⟩=

b0
b1

,(47)
then
|a⟩ ⊗ |b⟩=


a0b0
a0b1
a1b0
a1b1

 .(48)
For example,
|0⟩ ⊗ |1⟩=|01⟩=


0
1
0
0

 .(49)
It is common to omit the tensor-product symbol for the basis states, so
|0⟩ ⊗ |1⟩(50)
is written simply as
|01⟩.(51)
24

Tensor products also combine operators. If A acts on the first qubit and B acts on the second qubit,
then
A⊗B(52)
acts on the two-qubit system. For example, X⊗I means “apply X to the first qubit and do nothing
to the second,” whileI⊗Xmeans ”do nothing to the first qubit and applyXto the second."
For n qubits, a local single-qubit operator acting on qubit j is implicitly tensored with identities on
all other qubits, such as the Yj operator in the main text, which means Pauli Y applied to qubit j,
with identity operators on the remaining qubits.
A.4 Pauli matrices
The Pauli matrices are four2×2matrices that form a basic operator basis for one qubit:
I=

1 0
0 1

,X=

0 1
1 0

,
Y=

0−i
i0

,Z=

1 0
0−1

.
(53)
HereIis the identity. The other three are the PauliX,Y,andZoperators.
The PauliXmatrix flips the computational basis states:
X|0⟩=|1⟩,X|1⟩=|0⟩.(54)
The PauliZmatrix leaves|0⟩unchanged and changes the sign of|1⟩:
Z|0⟩=|0⟩,Z|1⟩=− |1⟩.(55)
The PauliYis similar to a bit flip but includes complex phases:
Y|0⟩=i|1⟩Y|1⟩=−i|0⟩.(56)
All Pauli matrices are Hermitian and unitary. Hermitian means
P † =P,(57)
and unitary means
P †P=I.(58)
Each of X,Y,Z has eigenvalues +1 and −1. This simple spectrum is why Pauli rotations generate
Fourier-like factors in data reuploading circuits.
Multi-qubit Pauli strings are tensor products of one-qubit Pauli operators. For example,
X⊗Z,Y⊗I,Z⊗X⊗Y(59)
are Pauli strings. In this paper, the trainable two-qubit SU(4) blocks are parameterised using the 15
non-identity two-qubit Pauli strings. These are all tensor products of I,X,Y,Z on two qubits except
I⊗I.
A.5 Quantum gates and unitary evolution
A quantum gate is a unitary matrixU. Applying a gate to a state gives
|ψ′⟩=U|ψ⟩.(60)
Unitary preserves normalisation:
⟨ψ′|ψ′⟩=⟨ψ|U †U|ψ⟩=⟨ψ|ψ⟩.(61)
Many gates are written as matrix exponentials of Hermitian generators. IfHis Hermitian, then
U(t) = exp

−iHt

(62)
is unitary. In this paper, the QSM data-encoding unitaries use the convention
U(t;M) = exp

− i 2 H(M)t  ,(63)
25

where H(M) is a Hamiltonian constructed from the input matrix M, and t is a trainable upload-time
scale.
Single-qubit rotation gates are also matrix exponentials. For example,
Ry(θ) = exp

− i 2 θY  ,R z(θ) = exp  − i 2 θZ  .(64)
These gates rotate a qubit state by an angle θ around the Y or Z axis of the Bloch sphere. For the
purposes of this paper, the important point is that the data value can appear inside the rotation angle.
A typical coordinate-wise rotation-gate encoding has the form
Ry(αxj),(65)
wherex j is one input feature andαis a fixed scale.
A.6 Observables, measurement, and projector readout
An observable is a Hermitian matrixO. Given a state|ψ⟩, the expected value ofOis
⟨O⟩ψ =⟨ψ|O|ψ⟩.(66)
This is a real number whenOis Hermitian.
For a task with N classes, let m=⌈log 2 N⌉. The leading m qubits form the label register, and class
jis associated with the computational-basis projector
Pj =|j⟩ ⟨j| ⊗I⊗(n−m),j∈ {0,. . .,N−1},(67)
where |j⟩ is an m-qubit basis state and the identity acts on the remaining qubits. The corresponding
raw projector mass is
qj =⟨ψ|P j |ψ⟩.(68)
If N= 2 m, the projectors exhaust the label register and P j qj = 1. Otherwise, some label states are
unused. The experiments condition on the named class outcomes,
pj = qj PN−1
k=0 qk
,
N−1X
k=0
qk >0,(69)
and predict the class with the largest pj, equivalently the largest qj. As noted in Section 3, the Fourier
analysis concerns the raw expectation valuesq j rather than the normalised ratiosp j.
B Derivation of the Frequency Support of Common Data-Encoding Unitaries
This section derives the maximal one-upload frequency supports stated in Equations (10) to (13).
Throughout, the input consists ofdscalar featuresx= (x 1,. . .,xd).
B.1 Fixed single-qubitR y encoding
For fixed single-qubitR y rotation-gate encoding, the encoding layer is
SRy (x) =
dO
j=1
Ry(αxj),(70)
whereαis a constant scaling factor and
Ry(αxj) =e −iαxj Yj /2,(71)
with Yj denoting the Pauli-Y operator on the j-th qubit. Its eigenvalues satisfy sj ∈ {+1,−1}, with
Yj |sj⟩Y =s j |sj⟩Y . The corresponding jointY-basis is
|s⟩Y =|s 1⟩Y ⊗ · · · ⊗ |sd⟩Y ,s= (s 1,. . .,sd)∈ {±1}d.(72)
26

The joint generator is
K(x) =
dX
j=1
αxj
2 Yj.(73)
Because the Yj operators act on different qubits, they commute, and hence SRy (x) =e −iK(x). In
the jointY-basis,
K(x)|s⟩ Y =

 α
2
dX
j=1
sjxj

 |s⟩Y .(74)
Because the joint Y -eigenstates form a complete orthonormal basis, the spectral theorem gives the
operator identity
SRy (x) =
X
s∈{±1}d
exp

− iα 2
dX
j=1
sjxj

 ΠY s ,(75)
whereΠ Y s is the rank-one projector onto|s⟩ Y . In particular, when applied to a joint eigenstate,
SRy (x)|s⟩ Y = exp

− iα 2
dX
j=1
sjxj

 |s⟩Y .
The phase-carrier vector is
ηs = α 2 s=  αs1 2 ,. . .,αsd 2  .(76)
When this encoding is used in a one-upload raw projector output qj of the form in Equation (3), the
phase factors from the bra and ket combine. Consequently, the candidate frequency vectors in its
Fourier expansion are the pairwise differences
ηs′ −η s = α 2 (s′ −s).(77)
Since (s′ j −s j)/2∈ {−1, 0, 1}, setting nj = (s′ j −s j)/2 yields the full vector-valued support in
Equation (10).
B.2 Fixed single-qubitR yRz encoding
For fixed single-qubitR yRz encoding,
SRyRz (x) =
dO
j=1
Rz(βxj)Ry(αxj).(78)
For one feature,
Sj(xj) =R z(βxj)Ry(αxj).(79)
The individual spectral decompositions are
Ry(αxj) =
X
s=±1
ΠY s e−isαxj /2,R z(βxj) = X
r=±1
ΠZ r e−irβx j /2.(80)
Therefore,
Sj(xj) =
 X
r=±1
ΠZ r e−irβx j /2
!  X
s=±1
ΠY s e−isαxj /2
!
=
X
r,s=±1
ΠZ r ΠY s e−i(rβ+sα)x j /2.
(81)
This is a finite carrier expansion with carrier rates
ηr,s = rβ+sα 2 .(82)
The candidate one-feature frequencies in the model output are the pairwise differences
ηr′,s′ −η r,s = (r′ −r)β+ (s ′ −s)α 2 .(83)
Setting m= (r ′ −r)/2 and n= (s ′ −s)/2 , where m,n∈ {−1, 0, 1}, yields the local support in
Equation (11). Taking the Cartesian product over the d independently encoded features gives the full
vector-valued support in Equation (12).
27

B.3 Component-wise trainable-frequencyR y encoding
For component-wise trainable-frequency Ry encoding, generalising the scalar-value version in [21],
STF(x,γ) =
dO
j=1
Ry(γjxj) =
dO
j=1
e−iγj xj Yj /2,(84)
where γ= (γ 1,. . .,γd) contains the trainable scaling parameters. The same joint Y -basis derivation
gives the carrier vectors
ηs(γ) =
 s1γ1
2 ,. . .,sdγd 2  .(85)
Forn j = (s′ j −s j)/2∈ {−1, 0, 1}, the pairwise differences are
ηs′(γ)−η s(γ) = (n1γ1,. . .,ndγd),(86)
which yields the full one-upload vector support in Equation (13).
C Derivations for Hamiltonian-Embedding Frequency Support
C.1 Conditioning variable, padding and coefficient convention
The Hamiltonian-embedding expansions differ from the coordinate-wise Fourier expansions in
Section 3. Here the matrix M is fixed and the upload time is the Fourier variable. Let H (0)(M)∈
RdH ×dH denote a matrix-derived Hamiltonian before Hilbert-space padding. For a circuit dimension
D= 2 n ≥d H, the implemented operator is
H(M) =H (0)(M)⊕0 D−dH .(87)
The main text uses the same symbol for the unpadded and padded operators. Direct-sum padding
preserves every nonzero eigenvalue and enlarges the zero eigenspace.
Let {νa(M)} a∈A(M) be the distinct eigenvalues of H(M) , and let Πa(M) be the corresponding
spectral projectors. The spectral theorem gives
H(M) =
X
a∈A(M)
νa(M)Π a(M),S H (t;M) =
X
a∈A(M)
e−iνa(M)t/2 Πa(M).(88)
For an initial state |ψ0⟩ and an observable Oθ that includes the trainable mixer, direct substitution
gives
f H 1 (M;t,θ) =⟨ψ 0|S H (t;M) †OθSH (t;M)|ψ 0⟩
=
X
a,b
AH ab(M,θ)e −i[νb(M)−ν a(M)]t/2 , (89)
where
AH ab(M,θ) =⟨ψ 0|Π a(M)O θΠb(M)|ψ 0⟩.(90)
Several ordered pairs (a,b) can produce the same gap. The Fourier coefficient at frequency ω is
therefore
C H ω (M,θ) = X
a,b:
(νb(M)−ν a(M))/2=ω
AH ab(M,θ).(91)
Consequently,
suppF(f H 1 )⊆Ω H 1 (M) =
 νb(M)−ν a(M)
2 :a,b∈ A(M)

.(92)
The inclusion can be strict because individual amplitudes can vanish or different amplitudes at the
same frequency can cancel. Using eigenspace projectors rather than chosen eigenvectors also makes
Equation (89) invariant under basis changes within a degenerate eigenspace.
28

The implemented global encoders use an independent time tℓ at each reuploading layer. Expanding
every upload in a depth-Lcircuit gives a multivariate trigonometric polynomial of the form
f H L (M;t,Θ) = X
a,b
AH ab(M,Θ) exp
"
− i 2
LX
ℓ=1

νbℓ (M)−ν aℓ (M)

tℓ
#
,(93)
where the amplitudes contain the ordered products of spectral projectors and intervening mixers. Its
maximal candidate support in t= (t 1,. . .,tL) is the Cartesian product [ΩH 1 (M)] ×L. If all layer
times are instead constrained to one scalar variable, the exponents combine and the corresponding
scalar candidate set is theL-fold Minkowski sum ofΩ H 1 (M).
C.2 Global symmetric Hamiltonian embedding
For the symmetric encoder, M is first zero-column padded to a square matrix fM when p > q. The
natural Hamiltonian is
H (0) sym(M) = fM+ fM T 2 ,(94)
followed by the direct-sum padding in Equation (87). Let
Hsym(M) =
X
a∈Asym(M)
λa(M)Π sym a (M)(95)
be its decomposition into distinct eigenvalues and their eigenspace projectors. Its upload unitary is
SHsym (t;M) =
X
a
e−iλa(M)t/2 Πsym a (M).(96)
Substitution into the observable output yields
f Hsym 1 (M;t,θ) = X
a,b
e+iλa(M)t/2 e−iλb(M)t/2
× ⟨ψ0|Π sym a (M)O θΠsym b (M)|ψ 0⟩,
(97)
which gives the pair amplitudes, aggregated coefficients and eigengap candidate set in Equations (18)
to (20).
When the eigenspaces indexed by a and b are one-dimensional, one may choose normalised eigenvec-
tors|v a(M)⟩and|v b(M)⟩. Writingd a(M) =⟨v a(M)|ψ 0⟩gives
AHsym ab (M,θ) =d a(M) ⋆db(M)⟨v a(M)|O θ |vb(M)⟩.(98)
This rank-one expression illustrates the eigenvector dependence but is basis-dependent when an
eigenvalue is degenerate. The projector expression in Equation (19) is the invariant statement used in
the main text. Any natural or padding-induced zero eigenspaces are combined into a single projector
associated withλ= 0.
C.3 Global block-Hamiltonian embedding
ForM∈R p×q, define the natural block Hamiltonian
H (0) block(M) =
0p×p M
M T 0q×q

(99)
on Rp⊕Rq. Lloydet al.use the Hermitian Hamiltonian  0A † A0  in their quantum polar decomposition
algorithm [33]. For real M, setting A=M T gives Equation (99). Their construction uses access to
this Hamiltonian to implement transformations associated with the polar decomposition; the present
model instead uses its time evolution directly as a data-encoding unitary.
Let the compact singular value decomposition ofMbe
M=
rX
j=1
σj(M)|u j(M)⟩ ⟨vj(M)|,r= rank(M),(100)
29

whereσ j(M)>0,u j(M)∈R p andv j(M)∈R q. The singular-vector equations are
M|v j⟩=σ j |uj⟩,M T |uj⟩=σ j |vj⟩.(101)
Introduce the direct-sum vectors
|uj ⊕0⟩=

uj
0q

,|0⊕v j⟩=

0p
vj

.(102)
Equation (99) then gives
H (0) block |uj ⊕0⟩=σ j |0⊕v j⟩,H (0) block |0⊕v j⟩=σ j |uj ⊕0⟩.(103)
Hence its restriction to
Sj = span{|uj ⊕0⟩,|0⊕v j⟩}(104)
isσ jX. The normalised eigenvectors on this subspace are
|j, +⟩= |uj ⊕0⟩+|0⊕v j⟩√ 2 ,|j,−⟩= |uj ⊕0⟩ − |0⊕vj⟩√ 2 ,(105)
and satisfy
H (0) block(M)|j, +⟩= +σ j(M)|j, +⟩,H (0) block(M)|j,−⟩=−σ j(M)|j,−⟩.(106)
The natural zero eigenspace is
kerH (0) block = ker(M T )⊕ker(M).(107)
Direct-sum Hilbert-space padding adds a further zero subspace of dimension D−(p+q) . Let
Πblock 0 (M)project onto their combined span. For a chosen orthonormal singular-vector basis,
Hblock(M) =
rX
j=1
σj(M) (|j, +⟩ ⟨j, +| − |j,−⟩ ⟨j,−|) + 0 Πblock 0 (M).(108)
If singular values are repeated, the rank-one projectors associated with each common eigenvalue are
summed to obtain the invariant spectral projectors Πblock a (M) used in the main text. Exponentiating
Equation (108) gives
SHblock (t;M) =
rX
j=1
h
e−iσj (M)t/2 |j, +⟩ ⟨j, +|+e+iσj (M)t/2 |j,−⟩ ⟨j,−| i + Πblock 0 (M).(109)
The generic expansion in Equation (89) now has eigenvalue labelsµa(M)∈ {+σj(M),−σ j(M), 0}.
Pairwise differences give
ΩHblock 1 (M) ={0} ∪

± σj(M)−σ k(M) 2 ,± σj(M) +σ k(M) 2 :j,k= 1,. . .,r  ∪Ω 0(M),
(110)
where
Ω0(M) =
{±σj(M)/2 :j= 1,. . .,r}, Π block 0 (M)̸= 0,
∅, Π block 0 (M) = 0. (111)
The terms with j=k in the half-sum set include ±σj(M). Equations (23) and (24) give the invariant
coefficient and candidate-support forms; the realised support can again be smaller.
C.4 Patch-local block-Hamiltonian embedding
Partition M into R non-overlapping patches P1,. . .,PR as defined in Appendix E. For patch r, write
Hr ≡H block(Pr) =
X
ar∈Ar
µr,ar (Pr)Πr,ar (Pr),(112)
30

where the distinct eigenvalues consist of the signed singular values of Pr and zero when present.
Because the local uploads act on disjoint registers, their joint one-upload unitary is
Spatch-Hblock (t;M) =
RO
r=1
exp

− i 2 Hrtr

=
X
a
exp
"
− i 2
RX
r=1
µr,ar (Pr)tr
#
Πa(M),
(113)
wheret= (t 1,. . .,tR),a= (a 1,. . .,aR)and
Πa(M) =
RO
r=1
Πr,ar (Pr).(114)
The one-upload observable output is
f patch-Hblock 1 (M;t,θ) = X
a,b
Apatch-Hblock ab (M,θ)
×exp
"
− i 2
RX
r=1

µr,br (Pr)−µ r,ar (Pr)

tr
#
,
(115)
with pair amplitudes
Apatch-Hblock ab (M,θ) =⟨ψ 0|Π a(M)O θΠb(M)|ψ 0⟩.(116)
The frequency vector associated with(a,b)is
1
2 (µ1,b1 (P1)−µ 1,a1 (P1),. . .,µR,bR (PR)−µ R,aR (PR)) .(117)
Taking all index pairs gives the Cartesian-product candidate set in Equation (25). At layer ℓ, tr is
replaced by the implemented parameter tℓ,r. For a depth-L circuit, the maximal support in the LR
independent time variables is the Cartesian product of the R local candidate sets over all L layers;
particular frequencies can still be absent through zero or cancelling amplitudes.
D Additional Information on the Benchmark Datasets
We evaluate the models on one real-world-data benchmark and two controlled synthetic benchmarks.
The real-world data benchmark tests whether the proposed encoders are useful for a small, nontrivial
handwritten-digit classification problem with matrix-valued inputs. The synthetic benchmarks are
designed to isolate spectral structure: one task is controlled by eigenvalue gaps, and the other by
singular values. Together, these datasets let us compare performance on realistic matrix-structured
inputs and on tasks where the relevant decision is explicitly spectral.
D.1 Pendigits benchmark
The Pendigits dataset [1] is used as the benchmark for real-world classification tasks. We use two
matrix-valued representations of each handwritten digit: the DYN representation, arranged as an
8×2 rectangular trajectory matrix, and the STA4 representation, arranged as a 4×4 bitmap. These
two representations provide complementary views of the same underlying object. DYN retains an
ordered pen-trajectory structure, whereas STA4 gives a compact square matrix representation. The
two representations are useful for testing whether a QFM data-encoding unitary benefits from treating
the input as a structured matrix rather than an unstructured feature vector.
For all Pendigits experiments, we use the original train/test split supplied with the dataset. A validation
set is formed by holding out 10% of the original training data. This validation is class-stratified so
that each class remains represented in both the training and validation subsets. The final split used in
the full 10-class experiments contains 6744 training examples, 750 validation examples, and 3498
test examples.
31

Before training, Pendigits features are standardised using statistics computed only from the post-
split training set. The resulting training-set mean and standard deviation are then applied to the
training, validation and test sets. After standardisation, each sample is reshaped into its corresponding
matrix representation for the Hamiltonian-based and patch-local data-encoding unitaries. The visual
examples shown in the main text (Figure 2a) display raw feature values for visual interpretation; the
models are trained on the standardised inputs described above.
The Pendigits task is included to provide a compact, real-world benchmark whose input dimension
is small enough for exact statevector simulation, especially for rotation-gate-based data-encoding
unitaries, while still retaining nontrivial matrix structure. The DYN and STA4 representations also
test different notions of structure: trajectory geometry in the former and spatially arranged pixel-
feature geometry in the latter. This makes Pendigits a useful test case for comparing coordinate-wise
rotation-gate data-encoding unitaries, patch-local data-encoding unitaries and global QSMs under the
same training protocol.
D.2 Synthetic spectral benchmarks
In addition to Pendigits, we use two controlled binary classification tasks whose labels are defined by
spectral properties of latent clean matrices. These tasks are designed to test whether the model can
exploit eigenvalue and singular-value structure rather than only component-value-level features. In
both tasks, the classifier observes a noisy matrix, while the label is determined by the spectrum used
to construct the corresponding clean matrix. The main experiments use 4096 samples per task, a data
generation seed of0, a validation fraction of0.1, and a relative noise level of0.05.
For the SYNTHETIC EIGENGAP task, each clean sample is generated as a random symmetric matrix
with prescribed eigenvalues. For sample index i, a Gaussian random matrix is first drawn and
factorised to obtain an orthogonal matrix Q. Independently, a vector of real eigenvalues is sampled
from a standard normal distribution and sorted in ascending order,
λi,1 ≤λ i,2 ≤ · · · ≤λi,d.(118)
The clean matrix is then
Si =Q idiag(λi,1,λ i,2,· · ·,λi,d)QT .(119)
In the main experiments,d= 4. The binary label is determined by the largest eigengap:
yi =1
h
|λi,d −λ i,d−1|> τeig
i
,(120)
withτ eig = 0.75.
The observed input matrix is obtained by adding scaled Gaussian noise to the clean matrix. Specifi-
cally, for each clean matrixSi, an independent Gaussian noise matrix Zi of the same shape is sampled
and rescaled as
Ei =ϵ ||Si||F max(||Zi||F , 10−12) Zi,(121)
where|| · ||F denotes for Frobenius norm. Then the input data becomes
Xi =S i +E i.(122)
The main experiments use ϵ= 0.05 , so the added noise has Frobenius norm equal to 5% of the clean
sample norm, up to the numerical denominator guard. The label is still computed from the latent
clean eigenvalues, not from the noisy input data matrix.
This construction is aligned with the symmetric Hamiltonian embedding. In the clean limit, the
input-derived symmetric Hamiltonian has eigenvalues λj(Si), and one upload has phase-difference
carriers proportional to
λk(Si)−λ j(Si)
2 .(123)
Thus the label depends directly on one of the spectral gaps that can appear in the sample-conditioned
Hamiltonian frequency support. The task is therefore a controlled probe of whether the model can
use eigengap information rather than only raw matrix entries.
For the SYNTHETIC SINGULAR value task, each clean sample is generated as a rectangular matrix
with prescribed singular values. For sample index i, independent Gaussian matrices are factorised
32

to obtain orthogonal factors Ui and Vi. A vector of singular values is sampled uniformly on [0, 2],
sorted in descending order,
σi,1 ≥σ i,2 ≥ · · · ≥σi,r,r=min(p,q),(124)
and placed on the diagonal of a rectangularp×qmatrixΣ i. The clean matrix is
Ri =U iΣiV T i .(125)
In the main experiments,p= 8,q= 2, and hencer= 2. The label is
yi =1
h
σi,1 +σ i,2 > τsv
i
,(126)
whereτ sv = 2.
As the eigengap task, the observed SYNTHETIC SINGULAR value task input is a noisy version of the
clean latent matrix. The label is determined by the latent singular values, not by the singular values
of the noisy observed matrix. The main experiments again useϵ= 0.05.
This task is aligned with the block Hamiltonian embedding. For a rectangular matrix M, the block
Hamiltonian
Hblock(M) =
 0M
M T 0

(127)
has nonzero eigenvalues ±σj(M), where σj(M) are the singular values of M. The one-upload
phase-difference support therefore contains singular-value differences and sums, including the terms
of the form
± σj(M)−σ k(M) 2 ,± σj(M) +σ k(M) 2 .(128)
The singular-value task uses a decision rule based onσ1+σ2, which is one of the spectral combinations
naturally exposed by this block construction in the clean setting.
For both synthetic tasks, the train/validation/test split is generated by randomly permuting the 4096
samples with the fixed data seed. The first 20% of the permuted samples are assigned to the test set.
A validation set is then formed from the 10% of the remaining samples, and the rest are used for
training. This yields 819 test examples, 328 validation examples, and 2949 training examples per
synthetic task.
The two synthetic benchmarks therefore play complementary diagnostic roles. The eigengap task tests
whether a model can exploit eigenvalue-gap information in a matrix whose clean signal is symmetric.
The singular-value task tests whether a model can exploit singular-value sums in a rectangular matrix.
Since the latent spectral rule is known by construction, these tasks provide controlled evidence about
spectral inductive bias, while the added matrix noise prevents the benchmarks from reducing to
noiseless spectral lookup.
E Additional Information on the Patch-Local Encoders and Mixer
Parameterisation
E.1 Patch-local SU(4) and block-Hamiltonian data-encoding unitaries
The patch-local data-encoding unitaries operate on four non-overlapping 2×2 patches. For a 4×4
matrix
M=

M1:2,1:2 M1:2,3:4
M3:4,1:2 M3:4,3:4

,(129)
we define
P1 =M 1:2,1:2,P 2 =M 1:2,3:4,P 3 =M 3:4,1:2,P 4 =M 3:4,3:4.(130)
For an8×2matrix, the patches are
Pr =M 2r−1:2r,1:2,r= 1, 2, 3, 4.(131)
Each patch is represented by a flattened vector
pr = vec(Pr)∈R 4 (132)
and is uploaded to a dedicated two-qubit system. Patch r acts on qubits 2r−1 and 2r, so all four
patch uploads together act on eight qubits. This applies to fixed patch-SU(4) , trainable patch-SU(4) ,
and non-overlap patch block-Hamiltonian embedding.
33

E.2 SU(4) convention
Both patch-SU(4) data-encoding unitaries and the brick-wall mixer use the same two-qubit SU(4)
parametrisation. Let
G= (G 1,· · ·,G15)(133)
be the ordered list of all non-identity two-qubit Pauli strings,
I⊗X,I⊗Y,I⊗Z,X⊗I,X⊗X,X⊗Y,X⊗Z,Y⊗I,Y⊗X,Y⊗Y,Y⊗Z,Z⊗I,Z⊗X,Z⊗Y,Z⊗Z.
(134)
For a coefficient vectorθ∈R 15, the corresponding two-qubit unitary is
USU(4) (θ) = exp
"
i
15X
a=1
θaGa
#
.(135)
The sign convention is therefore +i for the SU(4) parametrisation, different from the Hamiltonian
embedding unitaries.
E.3 Fixed patch-SU(4) encoder
The fixed patch-SU(4) encoder maps each flattened patch pr ∈R 4 to an SU(4) coefficient vector by
θ(Pr) =A 0pr,(136)
whereA 0 ∈R 15×4 is a fixed matrix. In the main experiments, the fixed map is
A0 = 1 2


1 0 0 0
0 1 0 0
0 0 1 0
0 0 0 1
1 1 0 0
0 0 1 1
1 0 1 0
0 1 0 1
1 0 0−1
0 1−1 0
1−1 0 0
0 0 1−1
1 1−1−1
1−1 1−1
1−1−1 1

 (137)
The patch upload is then
Upatch(Pr) = exp

i
15X
a=1
[A0pr]aGa
!
.(138)
The sameA 0 is used for every patch and every reuploading layer.
E.4 Trainable patch-SU(4) encoder
The trainable patch-SU(4) encoder uses the same four-patch decomposition and the same local SU(4)
exponential, but the linear patch map is made trainable. For layerℓand patchr, let
Aℓ,r ∈R 15×4.(139)
The patch angles are
θℓ,r(Pr) =A ℓ,rpr,(140)
and the upload is
Utrainable−patch,ℓ,r(Pr) = exp

i
15X
a=1
[Aℓ,rpr]aGa
!
.(141)
34

The trainable parameter tensor has shape

Aℓ,r
L,4
ℓ=1,r=1 ∈R L×4×15×4.(142)
It is initialised near the fixed patch map:
Aℓ,r =A 0 + ∆ℓ,r,(143)
where the entries of ∆ℓ,r are initialised as zero-mean Gaussian noise. The main experiments use a
noise scale of 0.01. With zero initialisation noise, the trainable patch encoder exactly reproduces the
fixed patch-SU(4) angle map at initialisation.
E.5 Non-overlapping patch-local block-Hamiltonian data-encoding unitary
The non-overlapping patch-local block-Hamiltonian data-encoding unitary replaces the local SU(4)
patch map with structured Hamiltonian evolution. For each2×2patchP r, define
Hpatch(Pr) =
 0P r
P T r 0

∈R 4×4.(144)
At layerℓ, the patch upload is
Upatch−block,ℓ,r(Pr) = exp
"
− i 2 Hpatch(Pr)tℓ,r
#
.(145)
This unitary is applied to the two-qubit subsystem assigned to patch r. When trainable upload times
are enabled, the parameter tensor is
t∈R L×4.(146)
Thus the model has one scalar Hamiltonian upload time for each layer and each patch. If no fixed
time is supplied, all entries are initialised to1/L.
The patch-local block-Hamiltonian QSM differs from its global counterpart. The global QSM
constructs one block Hamiltonian from the full matrix M, so its spectral structure is determined by
the singular values and singular vectors of the whole input matrix. The patch-local QSM instead
computes four independent 2×2 block Hamiltonians, preserving local patch singular geometry while
discarding cross-patch singular-vector coupling.
E.6 Brick-wall SU(4) mixer
After every application of a data-encoding unitary, the model applies a trainable nearest-neighbour
brick-wall mixer. Fornqubits, define the ordered pair set
Bn =

(1, 2), (3, 4),· · ·
	 [ 
(2, 3), (4, 5),· · ·

,(147)
where the even-starting pairs are applied before the odd-starting pairs. For each layer ℓ and each pair
b∈ Bn, the model applies
Vℓ,b = exp

i
15X
a=1
θSU(4) ℓ,b,a Ga
!
.(148)
The full mixer layer is the ordered product of these local blocks:
Vℓ =
Y
b∈Bn
Vℓ,b.(149)
For the n-qubit model used here, |Bn|=n−1 , so the mixer contributes 15(n−1) trainable
parameters per uploading layer. The mixer parameter tensor has shape
θSU(4) ∈R L×(n−1)×15.(150)
It is initialised from a zero-mean Gaussian distribution with scale 0.01.
The number of qubits in the QFM circuit depends on the data-encoding unitary. Matrix-value-wise
rotation-gate data-encoding unitaries use one qubit per scalar feature, so both 4×4 and 8×2 inputs
35

use 16 qubits. The three patch-local data-encoding unitaries split the input into four 2×2 patches and
assign each patch to two qubits, giving 8 qubits in total. The global QSMs instead use the dimension
of the input-derived Hamiltonian: Hsym uses 2 qubits for 4×4 inputs and 3 qubits for 8×2 inputs,
while Hblock uses 3 and 4 qubits, respectively, before any label-register expansion. For the ten-class
Pendigits task, the projector readout requires label qubits, so the global QSMs are promoted to 4
qubits when their natural Hamiltonian dimension is smaller. This promotion is implemented as
direct-sum padding H7→H⊕0 , equivalently U7→U⊕I , rather than by tensoring extra idle qubits.
Binary synthetic tasks require only one label qubit, so no additional expansion is needed for the
global QSM data-encoding unitaries.
At L= 32 , the resulting total numbers of trainable scalars, including the mixer and any trainable
encoder parameters, are 7200 for fixed- Ry, 7200 for fixed- RyRz, 7712 for trainable-frequency
Ry, 3360 for fixed patch- SU(4) , 11040 for trainable patch- SU(4) and 3488 for the patch-local
block-Hamiltonian QSM. For the four-qubit Pendigits global QSMs, both Hsym and Hblock contain
1472 trainable scalars. On SYNTHETIC EIGENGAP , the corresponding totals are 512 for the two-qubit
symmetric-Hamiltonian QSM and 992 for the three-qubit block-Hamiltonian QSM; on SYNTHETIC
SINGULAR, they are 992 for the three-qubit symmetric-Hamiltonian QSM and 1472 for the four-qubit
block-Hamiltonian QSM. The projector readout adds no trainable parameters. These totals make the
resource mismatch explicit: the main comparison holds the data and optimisation protocol fixed, but
it does not normalise circuit width or trainable-parameter count.
F Additional Performance Results on the Pendigits and Synthetic Datasets
The main performance archive contains 3840 complete records with finite reported metrics. Of these
records, 319 are marked as having been generated from a dirty implementation worktree. However,
all 20 records contributing to each of the four depth-32 winner aggregates quoted in the main text,
and all 20 records contributing to each of the four global Hblock maxima across the tested depths,
have git_dirty=False. We therefore retain those headline aggregates while disclosing the broader
archive provenance.
In this Appendix section, we report two additional validation-set summaries for the same training runs
shown in the main text (Figure 3). The first is the best validation accuracy reached during training, see
Figure 6. This metric records the largest validation accuracy observed at any evaluation checkpoint
for a given run. It is useful for separating the model’s best achieved validation performance from the
final checkpoint used for the main held-out test evaluation.
The second metric is the validation-accuracy area under the training curve (AUC), as shown in
Figure 7. Let the validation checkpoints for one run be
(t1,a 1), (t2,a 2),· · ·, (tm,a m),(151)
where ti is the optimisation step and ai is the validation accuracy recorded at that step. The reported
AUC is calculated by the trapezoidal rule,
AUCval =
m−1X
i=1
ai +a i+1
2 (ti+1 −t i).(152)
This is the raw area in units of optimisation steps, not a normalised curve. In the main runs, validation
is evaluated every 100 steps over 2000 training steps, so the maximum raw AUC is 1900 if validation
accuracy is 1 at every recorded interval. A summary of these results can also be found in Table 3.
The validation curves support the same qualitative conclusion as the final test results. On Pendigits
DYN, the three QSMs achieve the highest best validation accuracies, with the global block-Hamiltonian
QSM reaching 97.29%±0.53% , the symmetric-Hamiltonian QSM reaching 96.74%±0.57% , and
the patch-local block-Hamiltonian QSM reaching 96.30%±0.66% . On Pendigits STA4, the global
and patch-local block-Hamiltonian QSMs again lead, reaching92.25%±0.86% and 90.78%±0.64% ,
respectively.
The AUC plots provide a complementary view of training efficiency and sustained validation per-
formance. A model can obtain a high best validation accuracy late in training but a smaller AUC
if it learns slowly or is unstable. On DYN, the global block-Hamiltonian QSM achieves the highest
mean validation AUC, closely followed by the patch-local block-Hamiltonian QSM. On STA4, the
36

20 21 22 23 24 25
Re-upload depth
0.2
0.4
0.6
0.8
1.0
best validation accuracy
DYN
20 21 22 23 24 25
Re-upload depth
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9
best validation accuracy
STA4
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(a)
20 21 22 23 24 25
Re-upload depth
0.55
0.60
0.65
0.70
0.75
0.80
0.85
0.90
best validation accuracy
SYNTHETIC EIGENGAP
20 21 22 23 24 25
Re-upload depth
0.65
0.70
0.75
0.80
0.85
0.90
0.95
best validation accuracy
SYNTHETIC SINGULAR
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(b)
Figure 6:(a)Best validation accuracy on the Pendigits benchmark as a function of reuploading depth.
Each point is the mean over 20 seeds, and the error bars show one standard deviation. The metric
is the maximum validation accuracy observed over the 2000-step training trajectory for each run.
The QSMs achieve the highest best-validation accuracies on both DYN and STA4.(b)Best validation
accuracy on the two synthetic spectral benchmarks as a function of reuploading depth. Each point is
the mean over 20 seeds, and the error bars show one standard deviation. The global QSMs achieve
the strongest validation performance on both SYNTHETIC EIGENGAP and SYNTHETIC SINGULAR ,
with the block-Hamiltonian QSM giving the best overall validation accuracy.
patch-local block-Hamiltonian QSM achieves the highest mean validation AUC, indicating more
sustained validation performance throughout training. On SYNTHETIC EIGENGAP and SYNTHETIC
SINGULAR, the global block-Hamiltonian QSM gives the largest validation AUC.
G Additional Information on the Gradient Analysis
This section defines the gradient statistics used in the main text and reports the supplementary
diagnostics.
G.1 Details for the Gradient Diagnostics Metrics
Let B=

(xi,y i)
	m
i=1 be the diagnostic training batch, with m= 32 in the reported experiments. The batch is selected deterministically using diagnostic seed 0 and held fixed within each run
configuration. Let L(θ;B) be the mean cross-entropy loss on this batch. For a parameter group q, let
gq(θ;B) =∇ θq L(θ;B)∈R Pq ,(153)
where Pq is the number of parameters in group q. The parameter groups used in the plots are the
shared mixer layer parameters θSU(4) , trainable frequency parameters γ, Hamiltonian-embedding
upload timest ℓ ort ℓ,r, and trainable patch-map parameters.
37

20 21 22 23 24 25
Re-upload depth
200
400
600
800
1000
1200
1400
1600
1800
validation accuracy auc
DYN
20 21 22 23 24 25
Re-upload depth
200
400
600
800
1000
1200
1400
1600
validation accuracy auc
STA4
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(a)
20 21 22 23 24 25
Re-upload depth
1000
1100
1200
1300
1400
1500
1600
validation accuracy auc
SYNTHETIC EIGENGAP
20 21 22 23 24 25
Re-upload depth
1100
1200
1300
1400
1500
1600
1700
1800
validation accuracy auc
SYNTHETIC SINGULAR
block-hamiltonian
fixed-ry
fixed-ry-rz
non-overlap-patch-block-hamiltonian
patch-su4
symmetric-hamiltonian
trainable-frequency-ry
trainable-patch-su4
(b)
Figure 7:(a)Area under the validation-accuracy training curve on Pendigits. For each run, AUC
is computed by trapezoidal integration of validation accuracy over recorded evaluation steps. The
plotted values are means over 20 seeds with one-standard-deviation error bars. The patch-local and
global block-Hamiltonian QSMs achieve the highest AUCs, indicating stronger sustained valida-
tion performance throughout training.(b)Area under the validation-accuracy training curve on
SYNTHETIC EIGENGAP and SYNTHETIC SINGULAR . AUC is computed by trapezoidal integration
over validation checkpoints and is reported in step units. Each point is the mean over 20 seeds, with
error bars showing one standard deviation. The global block-Hamiltonian QSM gives the largest
AUC on both synthetic tasks.
For each run seed s, the initialisation diagnostic evaluates R= 20 parameter draws, generated with
seedss+r−1forr= 1,. . .,R, on the same diagnostic batch. Let
gq,r =g q(θ(r);B),r= 1,· · ·,R.(154)
For each parameter coordinatep, the initialisation gradient variance is
vq,p = 1 R
RX
r=1
(gq,r,p −¯gq,p)2, ¯g q,p = 1 R
RX
r=1
gq,r,p.(155)
The plotted initialisation-variance statistic is
medianp=1,···,P q log10(vq,p +ϵ),(156)
withϵ= 10 −30. The RMS-gradient statistic for a single gradient vector is
RMS(gq) =
vuut 1
Pq
PqX
p=1
|gq,p|2.(157)
38

Table 3:Additional validation-set performance summaries for the Pendigits and synthetic
benchmark runs.Best validation accuracy is the largest validation accuracy reached during training
for each run. Validation AUC is the unnormalised trapezoidal area under the validation-accuracy
curve over recorded evaluation steps. Values are mean±standard deviation over 20 random seeds.
Dataset Encoder Best-val depth Best val. acc. (%) Best-AUC depth Val. AUC Val. AUC / 1900
Pendigits DYN fixed-R y 1678.84±1.3481315.0±25.3 0.692
fixed-RyRz 1667.27±3.5441161.2±18.2 0.611
TF-Ry 3284.41±2.2281424.4±31.8 0.750
patch-SU(4)451.61±2.164859.0±32.2 0.452
trainable patch-SU(4)279.97±1.8521387.0±31.0 0.730
patchH block 3296.30±0.66321772.6±16.5 0.933
Hsym 3296.74±0.57161740.2±26.4 0.916
Hblock 3297.29±0.53161780.7±15.8 0.937
Pendigits STA4 fixed-R y 865.05±3.4381046.4±50.9 0.551
fixed-RyRz 1654.63±3.234903.2±25.1 0.475
TF-Ry 874.04±2.0381177.8±35.2 0.620
patch-SU(4)438.31±1.342632.7±32.4 0.333
trainable patch-SU(4)259.87±3.162972.9±32.6 0.512
patchH block 3290.78±0.64321664.0±11.7 0.876
Hsym 1676.95±1.7181283.8±41.7 0.676
Hblock 3292.25±0.8681631.4±34.9 0.859
Synthetic eigengap fixed-R y 870.64±1.0381262.0±15.5 0.664
fixed-RyRz 869.63±1.0281248.3±20.5 0.657
TF-Ry 871.51±1.1881281.6±15.8 0.675
patch-SU(4)266.62±1.2621216.9±20.3 0.640
trainable patch-SU(4)273.35±1.0921338.0±19.5 0.704
patchH block 1677.65±3.02161378.2±42.6 0.725
Hsym 3285.66±2.01321512.4±52.5 0.796
Hblock 1688.81±1.19161599.3±20.2 0.842
Synthetic singular fixed-R y 1683.60±1.28161536.5±18.6 0.809
fixed-RyRz 1682.82±1.38161523.6±19.9 0.802
TF-Ry 3284.60±1.1581556.2±14.8 0.819
patch-SU(4)477.09±1.2321409.7±11.0 0.742
trainable patch-SU(4)486.68±1.3841591.1±18.4 0.837
patchH block 3287.74±1.90321569.2±38.4 0.826
Hsym 1690.87±1.2481654.2±19.0 0.871
Hblock 1696.19±1.11161772.0±25.5 0.933
For initialisation, each run first averages the RMS over its R draws. For the final mode, each trained
run contributes one final-checkpoint gradient vector. The reported means and error bars then aggregate
these run-level statistics over 20 run seeds; the error bars are sample standard deviations across those
seeds.
The aggregate initialisation-diagnostic records do not store a git_dirty field. Their clean-state
provenance therefore cannot be checked from the archived aggregate files, although the records used
in the reported summaries are present and complete. The final-checkpoint diagnostic records do store
this field, allowing the affected comparisons to be qualified below.
For the empirical-Fisher diagnostic, the implementation computes one observed-label loss gradient
per diagnostic-batch element:
gi =∇ θℓ(θ;x i,y i),i= 1,· · ·,m,(158)
whereℓis the per-sample cross-entropy loss andθdenotes the full trainable parameter vector. Let
G=


gT 1
...
gT m

 ∈R m×P .(159)
The sample-space gradient Gram matrix is
ˆF= 1 m GGT .(160)
39

This is the common machine-learning empirical-Fisher construction based on ground-truth labels
[25]. It has the same nonzero eigenvalues as the parameter-space matrix GT G/m but is smaller
because m= 32 . It is not the true Fisher information, which averages over labels drawn from the
model distribution, or the quantum Fisher information used in quantum natural-gradient methods.
Nor should it be assumed to represent general loss curvature [25]. We use it only as a finite-batch
diagnostic of the sampled gradient directions. At initialisation, each run contributes the first of its 20
parameter draws to this calculation; at the final checkpoint, each run contributes its trained parameters.
Its trace is
tr( ˆF) = X
j
λj,(161)
and its participation-ratio effective rank [14] is
reff =
 P
j λj
2
max
 P
j λ2 j ,δ  ,(162)
and the condition number is
κ= maxλj >δλj
max

minλj >δλj,δ
 ,(163)
with damping thresholdδ= 10 −8.
G.2 Additional Gradient Diagnostics Plots and Results
Figure 8 reports the absolute RMS gradient scale at initialisation. It should be read together with the
initialisation-variance plot in Figure 4a. At depth 32, for example, fixed- Ry on Pendigits DYN has
mixer-gradient RMS 0.527±0.081 but median log10 mixer-gradient variance−11.04±0.08. Nonzero
gradient magnitude can therefore coexist with little coordinate-wise variation across initialisations;
the two diagnostics measure different properties.
Figure 9 reports the trace, effective rank and condition number of the empirical-Fisher gradient
Gram matrix at initialisation. These quantities describe total squared per-example gradient scale, the
participation of sampled gradient directions and their anisotropy, respectively. At depth 32, the initial
effective ranks of Hsym and Hblock are 1.42±0.04 and 1.52±0.02 on SYNTHETIC EIGENGAP , and
1.10±0.02 and 1.18±0.03 on SYNTHETIC SINGULAR . These low ranks coexist with relatively high
test accuracies, so initial empirical-Fisher rank does not track the performance ordering.
Figure 10 reports the same summaries at the final checkpoint. OnSYNTHETIC EIGENGAP at depth 32,
trainable patch-SU(4) has effective rank 30.65±0.23 and test accuracy 50.16%±2.36% ; Hblock
has effective rank 10.86±1.72 and accuracy 85.15%±2.40% . The effective rank therefore does
not reproduce the accuracy ordering. This example has a provenance limitation: all 20 trainable
patch-SU(4) final-gradient records are marked git_dirty=True, whereas all 20 Hblock records are
marked git_dirty=False. We therefore treat it as a descriptive archived comparison rather than a
clean-state reproduction. By contrast, all 20 records in each group used for the depth-32 Pendigits
DYNpatch-SU(4)versusH block comparison in the main text havegit_dirty=False.
H Additional Information on Latent Diagnostics
H.1 Additional details on the latent diagnostic metrics
Except for the 20-seed test accuracies in Table 5, the latent diagnostics use the final checkpoint
from seed 0 and a fixed 32-example validation batch. They do not estimate variation across training
seeds and should therefore be interpreted as illustrative within-run diagnostics rather than seed-
robust estimates. The batched latent archive contains 864 complete records, of which 63 are marked
git_dirty=True. Among the final-checkpoint depth-32 records, only two are dirty: Pendigits DYN
with trainable patch-SU(4) and SYNTHETIC EIGENGAP with trainable patch-SU(4) . The depth-32
QSM examples quoted in the main text—Pendigits DYN with Hsym and Hblock, Pendigits STA4 with
patch Hblock, and SYNTHETIC SINGULAR with Hsym and Hblock—all have git_dirty=False. Let

|ψ(s) i ⟩ 	m i=1 (164)
40

Re-upload depth
100
SU(4) mixer
mean RMS
gradient
Pendigits DYN
Re-upload depth
100
2 × 10 1
3 × 10 1
4 × 10 1
6 × 10 1
Pendigits STA4
Re-upload depth
10 2
10 1
Synthetic eigengap
Re-upload depth
10 2
10 1
Synthetic singular
Re-upload depth
3 × 10 1
4 × 10 1
6 × 10 1
Trainable
frequencies
mean RMS
gradient
Re-upload depth
2 × 10 1
3 × 10 1
4 × 10 1
Re-upload depth
10 1
2 × 10 2
3 × 10 2
4 × 10 2
6 × 10 2
Re-upload depth
10 1
Re-upload depth
2 × 10 1
3 × 10 1
4 × 10 1
Upload times
mean RMS
gradient
Re-upload depth
10 1
100
Re-upload depth
10 3
10 2
Re-upload depth
10 2
21 23 25
Re-upload depth
1.95 × 10 1
2 × 10 1
2.05 × 10 1
2.1 × 10 1
2.15 × 10 1
2.2 × 10 1
2.25 × 10 1
2.3 × 10 1
Patch map
mean RMS
gradient
21 23 25
Re-upload depth
2.2 × 10 1
2.4 × 10 1
2.6 × 10 1
2.8 × 10 1
3 × 10 1
3.2 × 10 1
3.4 × 10 1
3.6 × 10 1
3.8 × 10 1
21 23 25
Re-upload depth
3.4 × 10 2
3.6 × 10 2
3.8 × 10 2
4 × 10 2
4.2 × 10 2
4.4 × 10 2
4.6 × 10 2
21 23 25
Re-upload depth
2.2 × 10 2
2.4 × 10 2
2.6 × 10 2
2.8 × 10 2
3 × 10 2
fixed-ry
fixed-ry-rz
trainable-frequency-ry
patch-su4
trainable-patch-su4
non-overlap-patch-block-hamiltonian
symmetric-hamiltonian
block-hamiltonian
Figure 8: Initialisation RMS gradient as a function of reuploading depth. For each run configuration,
gradients are computed on a fixed diagnostic training batch for 20 random initialisations. The plotted
value is the RMS gradient within each parameter group, averaged over initialisation draws and then
over 20 run seeds; error bars show one standard deviation across seeds. This plot complements
the initialisation-variance diagnostic (Figure 4a) by measuring absolute gradient scale rather than
parameter-wise variance across initialisations.
Re-upload depth
102
103
104
105
Fisher
trace
Pendigits DYN
Re-upload depth
102
103
104
105
106
 Pendigits STA4
Re-upload depth
101
102
103
Synthetic eigengap
Re-upload depth
101
102
103
Synthetic singular
Re-upload depth
5
10
Fisher
effective rank
Re-upload depth
5
10
15
Re-upload depth
5
10
15
Re-upload depth
5
10
15
20 21 22 23 24 25
Re-upload depth
102
104
106
108
1010
Fisher
condition number
 20 21 22 23 24 25
Re-upload depth
102
104
106
108
1010
20 21 22 23 24 25
Re-upload depth
102
104
106
108
1010
20 21 22 23 24 25
Re-upload depth
101
104
107
1010
fixed-ry
fixed-ry-rz
trainable-frequency-ry
patch-su4
trainable-patch-su4
non-overlap-patch-block-hamiltonian
symmetric-hamiltonian
block-hamiltonian
Figure 9: Empirical-Fisher diagnostics at initialisation. For each diagnostic batch, per-sample
gradients are collected into a gradient matrix, and the empirical Fisher is summarised by its trace,
effective rank, and condition number. Each point is the mean over 20 run seeds, and error bars show
one standard deviation. The plot characterises the initial tangent-space geometry introduced by each
encoder but should not be interpreted as a direct predictor of final test accuracy.
41

Re-upload depth
102
103
Fisher
trace
Pendigits DYN
Re-upload depth
102
103
104
Pendigits STA4
Re-upload depth
101
102
Synthetic eigengap
Re-upload depth
100
101
102
Synthetic singular
Re-upload depth
10
20
30
Fisher
effective rank
Re-upload depth
10
20
30
Re-upload depth
0
10
20
30
Re-upload depth
10
20
20 21 22 23 24 25
Re-upload depth
101
102
103
104
105
Fisher
condition number
 20 21 22 23 24 25
Re-upload depth
102
104
106
20 21 22 23 24 25
Re-upload depth
101
103
105
107
20 21 22 23 24 25
Re-upload depth
102
104
106
108
fixed-ry
fixed-ry-rz
trainable-frequency-ry
patch-su4
trainable-patch-su4
non-overlap-patch-block-hamiltonian
symmetric-hamiltonian
block-hamiltonian
Figure 10: Empirical-Fisher diagnostics at the final trained checkpoint. The trace, effective rank, and
condition number are computed from per-sample gradients on the fixed diagnostic batch. Each point
is the mean over 20 run seeds, and error bars show one standard deviation. High final Fisher effective
rank does not by itself imply high predictive performance; several patch-SU(4) models have high
final Fisher rank but low depth-32 test accuracy.
Table 4:Summary of the depth-32 performance and gradient analysis.. Values are mean ±
standard deviation over 20 run seeds. Test accuracy is reported in percentages. Init logVar is the
median log10 variance of the shared SU(4) mixer gradients across initialisation draws. Init RMS and
final RMS are RMS gradients of the shared mixer group. Fisher ranks are empirical-Fisher effective
ranks computed from per-sample gradients on the diagnostic batch.
Dataset Encoder Test acc. (%) Init logVar Init RMS Final RMS Init Fisher rank Final Fisher rank
Pendigits DYN fixed-R y 72.29±2.77−11.04±0.08 0.527±0.081 0.054±0.010 5.71±3.11 10.20±3.23
fixed-RyRz 55.84±5.30−11.00±0.04 0.333±0.033 0.050±0.004 6.63±3.46 15.83±3.88
TF-Ry 81.37±2.36−11.03±0.09 0.473±0.060 0.044±0.006 5.92±2.72 8.92±2.98
patch-SU(4) 9.96±0.44−1.56±0.02 0.385±0.006 0.050±0.002 9.37±4.82 29.25±0.52
trainable patch-SU(4) 9.84±0.47−1.50±0.02 0.359±0.004 0.050±0.002 10.71±3.34 28.46±1.08
patchH block 92.75±0.84−2.38±0.04 0.201±0.003 0.048±0.005 6.42±1.21 10.82±2.00
Hsym 91.89±3.71−1.42±0.07 0.312±0.016 0.079±0.034 5.60±0.63 8.23±2.00
Hblock 92.35±5.95−1.05±0.05 0.380±0.022 0.071±0.034 5.22±1.81 9.39±2.72
Pendigits STA4 fixed-R y 40.22±4.40−11.33±0.03 0.396±0.012 0.040±0.006 3.52±1.72 20.51±2.92
fixed-RyRz 32.79±4.28−11.19±0.07 0.220±0.013 0.033±0.007 9.73±3.90 19.98±3.49
TF-Ry 46.85±6.39−11.31±0.03 0.401±0.028 0.045±0.007 3.52±1.88 18.86±2.81
patch-SU(4) 16.41±1.88−1.55±0.02 0.374±0.009 0.054±0.002 9.96±4.81 27.81±0.85
trainable patch-SU(4) 10.27±0.62−1.55±0.03 0.384±0.017 0.050±0.002 10.50±5.02 28.02±1.06
patchH block 86.14±1.33−2.09±0.08 0.244±0.008 0.079±0.013 6.36±1.78 7.04±1.71
Hsym 59.79±14.90−1.37±0.04 0.302±0.013 0.164±0.053 5.40±0.76 9.27±3.07
Hblock 76.38±16.84 0.05±0.20 0.779±0.078 0.194±0.169 4.18±1.97 6.34±3.96
Synthetic eigengap fixed-R y 65.40±1.69−19.73±0.06 0.088±0.002 0.011±0.002 3.47±0.73 9.22±2.03
fixed-RyRz 65.55±1.22−20.15±0.05 0.046±0.000 0.011±0.001 8.97±1.34 11.50±1.47
TF-Ry 67.42±1.33−19.73±0.06 0.088±0.002 0.010±0.001 3.55±0.76 7.59±1.19
patch-SU(4) 54.58±1.97−4.91±0.04 0.074±0.000 0.017±0.003 10.17±2.34 27.02±1.58
trainable patch-SU(4) 50.16±2.36−4.92±0.04 0.075±0.001 0.012±0.000 11.59±2.81 30.65±0.23
patchH block 71.44±2.11−9.44±0.03 0.035±0.004 0.023±0.004 1.50±0.03 7.93±1.23
Hsym 82.81±3.16−3.01±0.06 0.094±0.006 0.108±0.019 1.42±0.04 7.52±1.87
Hblock 85.15±2.40−3.72±0.05 0.052±0.004 0.062±0.011 1.52±0.02 10.86±1.72
Synthetic singular fixed-R y 84.34±1.24−19.69±0.09 0.084±0.002 0.012±0.002 4.48±1.01 7.86±1.20
fixed-RyRz 84.54±1.01−20.04±0.05 0.053±0.001 0.011±0.002 8.02±1.71 9.13±1.28
TF-Ry 85.40±0.63−19.69±0.09 0.085±0.002 0.013±0.003 4.40±1.02 6.38±1.44
patch-SU(4) 63.41±2.03−5.07±0.02 0.061±0.000 0.026±0.004 14.15±2.61 20.22±1.67
trainable patch-SU(4) 61.75±1.91−5.06±0.02 0.061±0.001 0.018±0.001 14.71±2.95 22.66±2.47
patchH block 87.50±2.06−9.29±0.04 0.036±0.005 0.023±0.009 1.26±0.03 5.49±1.55
Hsym 88.75±2.69−3.62±0.05 0.069±0.005 0.061±0.015 1.10±0.02 6.92±1.72
Hblock 92.72±4.04−3.64±0.04 0.070±0.003 0.036±0.009 1.18±0.03 6.53±1.17
42

denote the quantum states of the m= 32 diagnostic data examples at a particular stages of the circuit.
In the final-state summary plots, s is the final post-mixer state. In the layerwise plots, s indexes the
post-mixer state after each reuploading layer. We then compute the pure-state fidelity kernel
K (s) ij =

 ⟨ψ(s) i |ψ(s) j ⟩

2 .(165)
Lety i be the class label of examplei. The label-equality kernel is
Yij =1[y i =y j].(166)
This is the target kernel used in the kernel-target alignment calculation.
For a square matrixA∈R m×m, define the centering operator
C=I m − 1 m 11T ,1=


1
1
...
1

 ∈R m,(167)
so the centred Gram matrix is
˜A=CAC.(168)
The centred kernel-target alignment [23] used in the plots is
KT A(K,Y) = ⟨CKC,CY C⟩ F
||CKC|| F ||CY C||F
,(169)
with a small numerical guard in the denominator. This is the centred-kernel alignment (CKA) between
the fidelity and label kernels.
The within-minus-between fidelity gap uses only off-diagonal pairs. Let
W=

(i,j) :i < j,yi =y j

,B=

(i,j) :i < j,yi ̸=y j

.(170)
Then
∆fid = 1 |W| X (i,j)∈W Kij − 1 |B| X (i,j)∈B Kij.(171)
Positive values mean same-label examples are closer in quantum-state fidelity than different-label
data examples.
The participation-ratio effective rank [14] of the fidelity kernel is computed from the non-negative
eigenvaluesλ 1,. . .,λm of the symmetrised kernel:
reff (K) =
(P j λj)2 P
j λ2 j .(172)
This scale-invariant participation ratio summarises how broadly the kernel eigenvalue mass is spread:
it equals the number of equally weighted nonzero eigenmodes in the special case where those
eigenvalues are equal. It does not use the class labels and, by itself, does not measure class separation
or predictive accuracy. The centred effective rank uses the same expression after centring the kernel.
For adjacent-layer CKA, we apply the same centred-alignment formula to fidelity kernels from
consecutive post-mixer layers:
CKAℓ,ℓ+1 = ⟨CK (ℓ)C,CK (ℓ+1)C⟩ F ||CK (ℓ)C|| F ||CK (ℓ+1)C|| F ,(173)
This measures similarity between consecutive batch geometries; values near one indicate little
layer-to-layer change.
The trajectory plots evaluate the same final-state metrics at saved checkpoints rather than only at the
final checkpoint. Ifcindexes training checkpoints, the trajectory target alignment is
KT A(K(c) final,Y),(174)
whereK (c) final is the fidelity kernel of the final post-mixer state at checkpointc.
The diagnostic-batch projector accuracy reported in Table 5 is computed by applying the same
projector readout used for the classifier to the final quantum states and comparing the argmax
prediction with the diagnostic labels.
43

H.2 Additional figures and tables
The final kernel effective-rank plot in Figure 11 measures spectral spread in the final quantum-state
fidelity kernel. This is useful as a control because it separates broad participation across kernel
eigenmodes from class-aligned kernel geometry. In Figure 11, rotation-gate data-encoding unitaries
often have an effective rank of approximately 32 (the diagnostic batch size), but their fidelity gap is
approximately zero. Patch-SU(4) data-encoding unitaries also often have high effective rank while
performing poorly at depth 32. High effective rank is therefore insufficient for good classification in
these runs. The label-aware evidence instead comes from the fidelity gap and kernel-target alignment,
which must still be interpreted as associations rather than causes.
1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
24.7 31.9 32.0
27.5 32.0 32.0
23.3 31.7 32.0
30.4 31.9 32.0
28.0 31.9 32.0
16.0 23.0 24.9
1.71 11.1 15.5
1.88 14.2 15.3
Pendigits DYN
1 8 32
Re-upload depth
30.2 32.0 32.0
30.6 32.0 32.0
30.3 31.6 32.0
31.7 31.9 32.0
29.2 32.0 32.0
20.1 23.4 27.0
2.09 14.2 12.2
2.85 14.3 13.2
Pendigits STA4
1 8 32
Re-upload depth
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
12.7 32.0 32.0
22.6 32.0 32.0
13.5 32.0 32.0
31.2 32.0 32.0
31.3 32.0 32.0
2.41 24.7 29.2
1.64 6.09 6.64
2.13 13.2 12.0
Synthetic eigengap
1 8 32
Re-upload depth
5.78 31.9 32.0
12.7 32.0 32.0
7.70 31.9 32.0
29.5 32.0 32.0
29.5 31.9 32.0
3.15 25.7 21.5
5.70 7.39 6.00
4.95 7.82 11.2
Synthetic singular
5
10
15
20
25
30
Figure 11:Effective rank of the final quantum-state fidelity kernel.Effective rank is computed as
tr(K) 2/tr(K 2) from the eigenvalues of the final fidelity kernel. A high effective rank indicates that
the kernel spectrum is spread across many eigenmodes rather than concentrated in a few; it does not,
by itself, imply label alignment or high predictive performance.
The layerwise fidelity-gap plot (Figure 12) shows how class separation evolves across the circuit
layers at the final trained checkpoint. For each layer, the diagnostic computes the same within-
minus-between fidelity gap used in the main text, but on the post-mixer state at that layer. This plot
is useful because it shows whether class separation appears early or is progressively built by the
reuploading architecture. The QSMs tend to produce larger layerwise gaps than the rotation-gate
baselines, especially at depth 32. The patch-local block-Hamiltonian QSM is particularly relevant on
STA4, where its local patch structure produces strong class separation in later layers.
The layerwise target-alignment plot Figure 13 gives a complementary view of representation forma-
tion. Instead of measuring only the within-minus-between fidelity gap, it compares the full layerwise
fidelity kernel with the label-equality kernel using centred kernel alignment. This plot is useful when
the label structure is not captured solely by a mean gap. The main caveat is the same as for the final
target-alignment plot: target alignment can be nonzero for high-rank kernels even when off-diagonal
44

0.050
 0.025
0.000 0.025 0.050
Layer index
0.1
0.2
0.3
Layerwise
within-between
fidelity gap
Pendigits DYN, L=1
0 2 4 6
Layer index
0.0
0.2
0.4
Pendigits DYN, L=8
0 10 20 30
Layer index
0.0
0.2
0.4
Pendigits DYN, L=32
0.050
 0.025
0.000 0.025 0.050
Layer index
0.05
0.10
0.15
0.20
Layerwise
within-between
fidelity gap
Pendigits STA4, L=1
0 2 4 6
Layer index
0.0
0.1
0.2
0.3
Pendigits STA4, L=8
0 10 20 30
Layer index
0.0
0.1
0.2
0.3
Pendigits STA4, L=32
0.050
 0.025
0.000 0.025 0.050
Layer index
0.00
0.01
0.02
Layerwise
within-between
fidelity gap
Synthetic eigengap, L=1
0 2 4 6
Layer index
0.00
0.02
0.04
Synthetic eigengap, L=8
0 10 20 30
Layer index
0.00
0.02
0.04
0.06
0.08
Synthetic eigengap, L=32
0.050
 0.025
0.000 0.025 0.050
Layer index
0.025
0.050
0.075
0.100
Layerwise
within-between
fidelity gap
Synthetic singular, L=1
0 2 4 6
Layer index
0.00
0.05
0.10
0.15
0.20
Synthetic singular, L=8
0 10 20 30
Layer index
0.00
0.05
0.10
0.15
Synthetic singular, L=32
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
Figure 12:Layerwise within-minus-between fidelity gap.For each post-mixer layer, we compute
the pure-state fidelity kernel on the diagnostic validation batch and report the mean same-label
off-diagonal fidelity minus the mean different-label off-diagonal fidelity. The curves show where
class separation emerges inside the reuploading circuit. QSMs generally build larger class-separating
fidelity gaps than the coordinate-wise rotation-gate and patch-SU(4)baselines.
45

class separation is weak, so it should be interpreted together with the fidelity-gap and effective-rank
plots.
0.050
 0.025
 0.000 0.025 0.050
Layer index
0.6
0.7
Layerwise kernel
target alignment
Pendigits DYN, L=1
0 2 4 6
Layer index
0.5
0.6
0.7
0.8
Pendigits DYN, L=8
0 10 20 30
Layer index
0.5
0.6
0.7
0.8
0.9
Pendigits DYN, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
0.40
0.45
0.50
0.55
0.60
Layerwise kernel
target alignment
Pendigits STA4, L=1
0 2 4 6
Layer index
0.4
0.5
0.6
0.7
Pendigits STA4, L=8
0 10 20 30
Layer index
0.4
0.5
0.6
0.7
Pendigits STA4, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
0.10
0.15
Layerwise kernel
target alignment
Synthetic eigengap, L=1
0 2 4 6
Layer index
0.10
0.15
0.20
0.25
Synthetic eigengap, L=8
0 10 20 30
Layer index
0.05
0.10
0.15
0.20
0.25
Synthetic eigengap, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
0.25
0.30
0.35
0.40
Layerwise kernel
target alignment
Synthetic singular, L=1
0 2 4 6
Layer index
0.2
0.4
Synthetic singular, L=8
0 10 20 30
Layer index
0.2
0.4
Synthetic singular, L=32
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
Figure 13:Layerwise kernel-target alignment.At each post-mixer layer, the fidelity kernel of the
diagnostic validation states is centred and aligned with the label-equality kernel. The resulting curves
show how class-aligned quantum-state geometry develops across depth. This diagnostic complements
the layerwise fidelity-gap plot by comparing the full kernel structure to the label kernel.
The layerwise effective-rank plot shown in Figure 14 tracks how the fidelity-kernel eigenvalue mass
is distributed across modes as the circuit depth increases. It is most useful as a negative control.
Rotation-gate data-encoding unitaries can maintain very high effective rank across layers, but this
does not imply strong class separation or high test accuracy. Conversely, QSMs can have a lower
effective rank while achieving larger fidelity gaps and higher test accuracy. The layerwise result
therefore shows that broad kernel spectral spread alone does not reproduce the observed accuracy
pattern.
The trajectory plot in Figure 15 shows how final-state kernel-target alignment changes during training,
using the stored sequence of checkpoints. This helps distinguish a model that starts with label-aligned
geometry from one that learns it during optimisation. In Figure 15, the global block-Hamiltonian QSM
on Pendigits DYN increases target alignment from 0.558 at initialisation to 0.900 at the final checkpoint,
while fixed-Ry remains flat at 0.535. On SYNTHETIC SINGULAR , the global block-Hamiltonian QSM
46

0.050
 0.025
 0.000 0.025 0.050
Layer index
10
20
30
Layerwise kernel
effective rank
Pendigits DYN, L=1
0 2 4 6
Layer index
0
10
20
30
Pendigits DYN, L=8
0 10 20 30
Layer index
0
10
20
30
Pendigits DYN, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
10
20
30
Layerwise kernel
effective rank
Pendigits STA4, L=1
0 2 4 6
Layer index
10
20
30
Pendigits STA4, L=8
0 10 20 30
Layer index
0
10
20
30
Pendigits STA4, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
10
20
30
Layerwise kernel
effective rank
Synthetic eigengap, L=1
0 2 4 6
Layer index
0
10
20
30
Synthetic eigengap, L=8
0 10 20 30
Layer index
0
10
20
30
Synthetic eigengap, L=32
0.050
 0.025
 0.000 0.025 0.050
Layer index
10
20
30
Layerwise kernel
effective rank
Synthetic singular, L=1
0 2 4 6
Layer index
0
10
20
30
Synthetic singular, L=8
0 10 20 30
Layer index
0
10
20
30
Synthetic singular, L=32
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
Figure 14:Layerwise effective rank of the fidelity kernel.Effective rank is computed from the
post-mixer fidelity kernel at each layer. The plot measures spectral spread in the kernel, not label
alignment. High effective rank alone is not sufficient for high test accuracy in these runs, as several
rotation-gate and patch- SU(4) models produce high-rank kernels without strong class-separated
fidelity geometry.
47

increases from 0.093 at initialisation to 0.461 at the final checkpoint, while fixed- Ry remains at
0.180. This supports the interpretation that the QSMs learn class-aligned quantum-state geometry
over training, rather than merely starting with it.
0 500 1000 1500 2000
Checkpoint step
0.5
0.6
0.7
Final kernel
target alignment
Pendigits DYN, L=1
0 500 1000 1500 2000
Checkpoint step
0.5
0.6
0.7
0.8
Pendigits DYN, L=8
0 500 1000 1500 2000
Checkpoint step
0.5
0.6
0.7
0.8
0.9
Pendigits DYN, L=32
0 500 1000 1500 2000
Checkpoint step
0.40
0.45
0.50
0.55
0.60
Final kernel
target alignment
Pendigits STA4, L=1
0 500 1000 1500 2000
Checkpoint step
0.4
0.5
0.6
0.7
Pendigits STA4, L=8
0 500 1000 1500 2000
Checkpoint step
0.4
0.5
0.6
0.7
Pendigits STA4, L=32
0 500 1000 1500 2000
Checkpoint step
0.10
0.15
Final kernel
target alignment
Synthetic eigengap, L=1
0 500 1000 1500 2000
Checkpoint step
0.05
0.10
0.15
0.20
0.25
Synthetic eigengap, L=8
0 500 1000 1500 2000
Checkpoint step
0.10
0.15
0.20
0.25
Synthetic eigengap, L=32
0 500 1000 1500 2000
Checkpoint step
0.1
0.2
0.3
0.4
Final kernel
target alignment
Synthetic singular, L=1
0 500 1000 1500 2000
Checkpoint step
0.2
0.4
Synthetic singular, L=8
0 500 1000 1500 2000
Checkpoint step
0.2
0.4
0.6
Synthetic singular, L=32
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
Figure 15:Training trajectory of kernel-target alignment.The curves show centred alignment
between the final-state fidelity kernel and the label-equality kernel at saved checkpoints. The
diagnostic is evaluated on the same validation batch used in the final latent-state summaries. QSMs
tend to increase target alignment during optimisation, whereas several coordinate-wise rotation-gate
baselines remain comparatively flat.
The scatter plot in Figure 16 relates the fidelity-gap diagnostic to diagnostic-batch accuracy. It
directly connects the latent-state geometry to prediction quality on the diagnostic batch. Points with
larger within-minus-between fidelity gap generally correspond to better diagnostic-batch accuracy,
especially in the Pendigits panels. The plot also makes the negative-control cases visible: some
encoders may have a high effective rank, but without a positive fidelity gap, they do not form a
label-separated quantum-state geometry.
The adjacent-layer CKA plot in Figure 17 measures representational shifts between consecutive
post-mixer states. A high value means that the fidelity kernel changes little from one layer to the next.
This diagnostic could assess whether deeper circuits are repeatedly reshaping the batch geometry
or have entered a stable representation regime. In Figure 17, adjacent-layer CKA is often high at
48

0.0 0.1 0.2 0.3 0.4 0.5
Final within-between
fidelity gap
0.2
0.4
0.6
0.8
1.0
Logit final
accuracy
Pendigits DYN
0.00 0.05 0.10 0.15 0.20 0.25 0.30
Final within-between
fidelity gap
0.2
0.4
0.6
0.8
Logit final
accuracy
Pendigits STA4
0.00 0.02 0.04 0.06 0.08
Final within-between
fidelity gap
0.5
0.6
0.7
0.8
Logit final
accuracy
Synthetic eigengap
0.00 0.05 0.10 0.15 0.20
Final within-between
fidelity gap
0.7
0.8
0.9
1.0
Logit final
accuracy
Synthetic singular
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
L=1
L=8
L=32
Figure 16:Relationship between fidelity gap and diagnostic-batch accuracy.Each point cor-
responds to one encoder-depth configuration on the diagnostic validation batch. The horizontal
axis is the final within-minus-between fidelity gap, and the vertical axis is final projector accuracy
on the same batch. Larger positive fidelity gaps generally correspond to stronger diagnostic-batch
classification.
large depths, with final depth-32 values averaging about 0.986 across complete records, but this high
stability does not, by itself, distinguish successful from unsuccessful encoders.
I Additional Information on Classical Baseline and Ablation Study
Table 6 reports the classical controls described in the main text. For every quantum ablation in Table 7,
the transformation is constructed before training, applied to the training, validation and test splits,
and followed by retraining. Labels are unchanged. Any reference basis or spectrum is computed
from the training split only.
The entry-permutation control generates one fixed permutation of the flattened matrix entries and
applies it to every sample in all three splits. The row/column control similarly generates one fixed
row permutation and one fixed column permutation. The permutations are therefore dataset-level
transformations, not independently sampled perturbations of individual examples.
For the symmetric-Hamiltonian controls, let Q0 be the eigenvector matrix of the mean training-
set Hsym and let λ0 be the coordinatewise median of the ordered training-set eigenvalues. The
spectrum-only control retains each sample’s eigenvalues and replaces its eigenvectors byQ0. The
eigenvectors-only control retains each sample’s eigenvectors and replaces its eigenvalues byλ0.
For the block-Hamiltonian controls, let U0 and V0 be the left and right singular-vector matrices of the
mean training matrix, and let σ0 be the coordinatewise median of the ordered training-set singular
values. The singular-values-only control combines each sample’s singular values with U0 and V0.
49

0 2 4 6
Layer index
0.7
0.8
0.9
1.0
CKA
Pendigits DYN, L=8
0 10 20 30
Layer index
0.80
0.85
0.90
0.95
1.00
Pendigits DYN, L=32
0 2 4 6
Layer index
0.85
0.90
0.95
1.00
CKA
Pendigits STA4, L=8
0 10 20 30
Layer index
0.7
0.8
0.9
1.0
Pendigits STA4, L=32
0 2 4 6
Layer index
0.4
0.6
0.8
1.0
CKA
Synthetic eigengap, L=8
0 10 20 30
Layer index
0.4
0.6
0.8
1.0
Synthetic eigengap, L=32
0 2 4 6
Layer index
0.4
0.6
0.8
1.0
CKA
Synthetic singular, L=8
0 10 20 30
Layer index
0.4
0.6
0.8
1.0
Synthetic singular, L=32
Fixed Ry
Fixed Ry/Rz
Trainable-frequency Ry
Patch SU(4)
Trainable patch SU(4)
Patch H_block
H_sym
H_block
Figure 17:Adjacent-layer CKA of post-mixer fidelity kernels.For each trained model, we
compute centred kernel alignment between the fidelity kernels of consecutive post-mixer layers. High
values indicate that adjacent layers preserve a similar batch geometry. These diagnostic measures
representational stability across depth and are included as a supplementary control rather than as a
direct predictor of test accuracy.
50

Table 5:Summary of the latent diagnostic results.Test accuracy is the mean ± standard deviation
over 20 random seeds, reported in percentage. The remaining columns are final-checkpoint diagnos-
tics computed on the fixed 32-example validation diagnostic batch for seed 0. Diagnostic accuracy is
the projector accuracy on this batch. KTA is centred kernel-target alignment between the final fidelity
kernel and the label-equality kernel. Gap is the mean within-class off-diagonal fidelity minus the
mean between-class off-diagonal fidelity. Effective rank is computed from the final fidelity kernel.
Dataset Encoder Test acc. (%) Diag. acc. KTA Gap Eff. rank
Pendigits DYN fixed-R y 72.29±2.770.688 0.535 0.000 32.00
fixed-RyRz 55.84±5.300.562 0.535 0.000 32.00
TF-Ry 81.37±2.360.719 0.535 0.000 32.00
patch-SU(4) 9.96±0.440.062 0.535−0.00031.97
trainable patch-SU(4) 9.84±0.470.094 0.535−0.00031.97
patchH block 92.75±0.840.938 0.761 0.260 24.87
Hsym 91.89±3.711.000 0.887 0.538 15.46
Hblock 92.35±5.951.000 0.900 0.561 15.29
Pendigits STA4 fixed-R y 40.22±4.400.438 0.535 0.000 32.00
fixed-RyRz 32.79±4.280.312 0.535−0.00032.00
TF-Ry 46.85±6.390.562 0.535 0.000 32.00
patch-SU(4) 16.41±1.880.094 0.535−0.00031.97
trainable patch-SU(4) 10.27±0.620.094 0.534−0.00131.97
patchH block 86.14±1.330.938 0.694 0.173 27.03
Hsym 59.79±14.900.562 0.592 0.208 12.18
Hblock 76.38±16.840.719 0.694 0.285 13.20
Synthetic eigengap fixed-R y 65.40±1.690.594 0.180−0.00032.00
fixed-RyRz 65.55±1.220.625 0.180−0.00032.00
TF-Ry 67.42±1.330.594 0.180−0.00032.00
patch-SU(4) 54.58±1.970.562 0.179−0.00031.97
trainable patch-SU(4) 50.16±2.360.531 0.181 0.000 31.97
patchH block 71.44±2.110.625 0.168−0.00329.21
Hsym 82.81±3.160.812 0.259 0.077 6.64
Hblock 85.15±2.400.750 0.261 0.053 11.95
Synthetic singular fixed-R y 84.34±1.240.812 0.180 0.000 32.00
fixed-RyRz 84.54±1.010.844 0.180 0.000 32.00
TF-Ry 85.40±0.630.812 0.180 0.000 32.00
patch-SU(4) 63.41±2.030.625 0.180 0.000 31.95
trainable patch-SU(4) 61.75±1.910.625 0.181 0.000 31.97
patchH block 87.50±2.060.906 0.323 0.059 21.50
Hsym 88.75±2.690.844 0.508 0.163 6.00
Hblock 92.72±4.040.906 0.461 0.159 11.17
The singular-vectors-only control retains each sample’s left and right singular vectors and replaces
its singular values by σ0. Because bases within degenerate spectral subspaces are not unique, the
vector-only controls are implementation-dependent in those subspaces.
Table 6:Classical baseline results.Each baseline is a one-hidden-layer MLP trained on either
flattened raw entries or spectral-value descriptors. Values are mean ± standard deviation over 20
random seeds, reported in percentage. ∆ is the test-accuracy difference, in percentage points, between
the classical baseline and the largest observed QSM mean on the same dataset panel.
Dataset Feature source Feature dim. Params Val. acc. (%) Test acc. (%)
∆vs. largest
QSM mean
Pendigits DYN raw entries 16 146899.31±0.22 96.88±0.24 +3.07
Hsym eig. 8 147366.97±1.12 59.98±0.60−33.83
Hblock sing. 2 146642.75±0.70 39.67±0.48−54.14
Pendigits STA4 raw entries 16 146895.46±0.47 91.32±0.46 +4.66
Hsym eig. 4 146538.53±0.95 39.80±0.50−46.86
Hblock sing. 4 146531.39±1.00 30.62±0.53−56.04
Synthetic eigengap raw entries 16 51575.20±2.51 74.88±1.27−11.76
Hsym eig. 4 51398.28±0.28 98.01±0.35 +11.36
Hblock sing. 4 98967.21±1.03 67.56±0.60−19.08
Synthetic singular raw entries 16 146590.37±0.80 91.32±0.60−3.92
Hsym eig. 8 99298.29±0.51 97.28±0.23 +2.04
Hblock sing. 2 147298.57±0.36 98.50±0.20 +3.25
51

Table 7:Ablation-study summary for Hamiltonian-based QSMs.Values are mean ± standard
deviation over 20 random seeds, reported in percentage. “Original” gives the depth and largest
observed mean test accuracy of the unablated QSM variant on the same dataset panel; “Ablated” gives
the corresponding descriptive maximum after retraining under the specified ablation. These maxima
are computed across the tested depths rather than at depths selected by independent validation. ∆ is
the ablated-minus-original difference in percentage points. Spectrum/eigenvector controls are run
for Hsym; singular-value/vector controls are run for Hblock; permutation controls are shown for the
global QSMs and the patch-local block-Hamiltonian QSM.
Dataset Encoder Original Ablation Ablated∆
Pendigits DYNH sym L32,91.89±3.71spectrum only L8,48.87±3.90−43.02
Hsym L32,91.89±3.71eigenvectors only L16,89.80±4.56−2.08
Hsym L32,91.89±3.71entry permutation L16,89.49±10.42−2.39
Hsym L32,91.89±3.71row/column permutation L32,92.69±3.79 +0.80
Hblock L16,93.81±1.06singular values only L4,31.65±2.44−62.16
Hblock L16,93.81±1.06singular vectors only L16,93.56±0.84−0.24
Hblock L16,93.81±1.06entry permutation L32,93.94±2.34 +0.13
Hblock L16,93.81±1.06row/column permutation L32,94.82±1.59 +1.01
patchH block L32,92.75±0.84entry permutation L32,92.77±1.31 +0.03
patchH block L32,92.75±0.84row/column permutation L32,92.09±1.40−0.66
Pendigits STA4H sym L16,70.14±8.29spectrum only L4,28.35±2.11−41.79
Hsym L16,70.14±8.29eigenvectors only L4,64.30±2.02−5.84
Hsym L16,70.14±8.29entry permutation L32,72.45±6.58 +2.31
Hsym L16,70.14±8.29row/column permutation L16,70.73±4.05 +0.59
Hblock L16,86.66±2.17singular values only L4,25.25±2.02−61.41
Hblock L16,86.66±2.17singular vectors only L16,84.74±4.51−1.91
Hblock L16,86.66±2.17entry permutation L16,84.59±4.05−2.07
Hblock L16,86.66±2.17row/column permutation L16,86.16±2.85−0.50
patchH block L32,86.14±1.33entry permutation L16,83.10±1.03−3.04
patchH block L32,86.14±1.33row/column permutation L16,83.92±1.38−2.22
Synthetic eigengapH sym L16,83.42±1.37spectrum only L8,97.92±0.38 +14.50
Hsym L16,83.42±1.37eigenvectors only L1,61.28±0.07−22.14
Hsym L16,83.42±1.37entry permutation L8,67.83±1.41−15.59
Hsym L16,83.42±1.37row/column permutation L4,69.80±1.39−13.62
Hblock L16,86.65±1.18singular values only L16,65.54±1.07−21.11
Hblock L16,86.65±1.18singular vectors only L8,68.66±1.65−17.99
Hblock L16,86.65±1.18entry permutation L16,74.46±1.35−12.19
Hblock L16,86.65±1.18row/column permutation L16,83.47±1.18−3.18
patchH block L16,74.37±2.59entry permutation L16,72.85±1.46−1.52
patchH block L16,74.37±2.59row/column permutation L16,74.74±1.33 +0.37
Synthetic singularH sym L8,90.16±1.08spectrum only L8,97.25±0.48 +7.08
Hsym L8,90.16±1.08eigenvectors only L2,51.29±1.04−38.87
Hsym L8,90.16±1.08entry permutation L8,88.35±1.00−1.81
Hsym L8,90.16±1.08row/column permutation L16,88.64±1.27−1.53
Hblock L16,95.24±1.53singular values only L32,98.42±0.30 +3.17
Hblock L16,95.24±1.53singular vectors only L16,49.88±1.96−45.36
Hblock L16,95.24±1.53entry permutation L8,90.55±0.58−4.69
Hblock L16,95.24±1.53row/column permutation L16,95.06±2.30−0.18
patchH block L32,87.50±2.06entry permutation L32,87.04±2.04−0.46
patchH block L32,87.50±2.06row/column permutation L32,86.43±3.37−1.06
52
