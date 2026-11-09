---
title: 'NEMORA: Neural Equivariant Multipole Operators for Long-Range Atomistic Learning'
url: https://arxiv.org/abs/2610.10776
category: ai-marketing
subcategory: measurement
date: 2026-10
venue: ''
authors:
- Jay L. Kaplan
- Samuel Varner
- Rebecca Willett
- Juan J. de Pablo
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.10776
pages: 59
chars: 153625
fetched_at: '2026-11-08T13:25:54+00:00'
kb_version: 1
---

# NEMORA: Neural Equivariant Multipole Operators for Long-Range Atomistic Learning

NEMORA: Neural Equivariant Multipole Operators for
Long-Range Atomistic Learning
Jay L. Kaplan1, Samuel Varner2, Rebecca Willett3,4,5, Juan J. de Pablo1,2,6,*
1Courant Institute School of Mathematics, Computing, and Data Science,
New York University, New York, NY 10012, USA
2Department of Chemical and Biomolecular Engineering, Tandon School of Engineering,
New York University, Brooklyn, NY 11201, USA
3Department of Statistics, The University of Chicago, Chicago, IL 60637, USA
4Department of Computer Science, The University of Chicago, Chicago, IL 60637, USA
5NSF-Simons National Institute for Theory and Mathematics in Biology, Chicago, IL 60611, USA
6Department of Physics, New York University, New York, NY 10012, USA
*Corresponding author: Juan J. de Pablo, jjd8110@nyu.edu
Abstract
Equivariant graph neural networks have emerged as foundational architectures for machine-
learned interatomic potentials, approaching quantum-chemical accuracy at a fraction of the
computational cost. These models describe local atomic environments accurately, but finite
spatial cutoffs truncate long-range information flow, and stacking message-passing layers can
lead to over-smoothing and over-squashing. Existing long-range extensions either prescribe
a fixed analytical propagation kernel, restrict long-range communication to scalars or degree-
preserving channels, are only approximately equivariant, or incur super-linear computational cost.
Combining learnable long-range equivariant transport with multiscale many-body expressivity and
efficient scaling for larger systems remains a central challenge. We introduce Neural Equivariant
Multipole Operators (NEMORA), a neural equivariant extension of the Fast Multipole Method
(FMM) for learning long-range tensorial representations. NEMORA generalizes the FMM’s
analytical multipole expansion and translation operators to learned equivariant counterparts
on an adaptive spatial hierarchy. Its operators couple angular degrees and form many-body
interactions across length scales, retaining the FMM’s hierarchical organization and analytical
radial factors as physical inductive biases while learning data-dependent long-range couplings.
NEMORA evaluates in linear time and memory complexity, allowing it to treat larger systems
than other long-range methods reaching hundreds of thousands of atoms, and it augments both
symmetry-constrained and unconstrained short-range backbones. On non-local benchmarks,
it reduces force and energy errors relative to the short-range backbones by over an order of
magnitude and up to three orders of magnitude, respectively, which is better than or competitive
with existing long-range extensions in accuracy.
1 Introduction
Modeling atomic interactions underpins central tasks in computational science, from finding low-
energy conformations to computing thermodynamic and kinetic properties by molecular simulation.
Classical force fields enable large simulations at modest cost, but their prescribed functional
forms limit the chemistry they can represent. Machine-learned interatomic potentials (MLIPs)
learn potential energy surfaces from quantum-chemical data, approaching this same accuracy
1
arXiv:2610.10776v1  [cs.LG]  7 Oct 2026

Preprint
at a fraction of the cost [7, 13, 94, 110]. Equivariant architectures are especially accurate and
data-efficient because they build the symmetries of atomic environments into their representations
[8, 12, 31, 70, 74, 92, 116].
However, these architectures rely on finite spatial cutoffs for efficiency, which limits their
treatment of long-range interactions such as electrostatics, charge transfer, dispersion, polarization
and other non-local electronic effects. These interactions govern interfaces, charged systems, polar
condensed phases and biomolecular assemblies, among others [52, 77, 81, 82, 114, 125, 130]. Stacking
message-passing layers extends the receptive field on connected graphs, but increases cost, causes
over-smoothing and over-squashing [1, 24, 79], and cannot connect fragments that are disconnected
in the cutoff graph. These limitations motivate dedicated long-range channels with tractable scaling.
Long-range extensions include latent scalar methods [16, 64], charge equilibration [33, 43, 61],
latent tensor fields [91, 127], polarizable multipoles [11, 80], global attention and aggregation [15,
32, 88], matrix-function representations [9], and multiscale representations [48, 95, 129] (Appendix
Table 5). These advances extend non-local modeling, but do not jointly learn the long-range
propagation kernel with a physics-inductive bias, cross-degree angular coupling, or explicit higher-
body-order interactions among distant sources on an adaptive hierarchy withO(N)time and memory.
The Fast Multipole Method (FMM) is a natural foundation for these requirements [17, 39]. It
represents well-separated source clusters by compact multipole expansions across a spatial hierarchy
with linear complexity. For the Coulomb kernel, spherical harmonics and analytical radial factors
give a physically grounded basis for equivariant transport, built from the same ingredients as
equivariant message passing [10, 17].
We introduceNeural Equivariant Multipole Operators (NEMORA), a neural equivariant extension
of the FMM for learning long-range many-body interactions (Figure 1). NEMORA replaces scalar
source charges with learned equivariant tensor charges, and the analytical expansion and translation
operators with learnableE(3)-equivariant counterparts on an adaptive spatial hierarchy. Its operators
learn weights over Clebsch–Gordan paths, coupling angular degrees in the long-range channel.
Learnable non-linear radial modulations and invariant gates adapt the analytical Green’s-function
kernels to the data. Symmetric tensor contractions [8, 25] on the aggregated fields form explicit
higher-body-order interactions among distant collections of particles. The long-range messages then
update the short-range backbone features and are passed through a readout layer as a residual energy
term, with forces obtained via automatic differentiation of the energy (Section 4.5). Evaluation is
O(N)in time and memory for both periodic and non-periodic systems. Our contributions are:
• Learnable equivariant FMM.Learned angular (degree-coupling) transport and symmetric
tensor contractions build multiscale long-range many-body representations withO(N)time and
memory cost over an adaptive spatial hierarchy that preserves equivariance up to eigenframe
degeneracy.
• Global reaction-field channel.Inspired by continuum electrostatics [14, 60, 78], a learnable
Kelvin transform [2] inverts globally pooled multipoles into a same-center local expansion, an
equivariant continuum boundary response broadcast to atoms that complements hierarchical
transport (Appendix K.2).
• Accuracy, portability, and scaling.NEMORA reduces force and energy errors by over an
order of magnitude and up to three orders of magnitude, respectively, relative to short-range
models on non-local benchmarks, which is better than or competitive with other long-range
methods. Additionally, improvements on four short-range backbones demonstrate NEMORA’s
portability to both symmetry-constrained and -unconstrained architectures, where the lift for
scalar-only hosts recovers part of the native-equivariant gain. We show that NEMORA is
linear in evaluation runtime and memory up to approximately 340,000 atoms on a single GPU.
2

Preprint
2 Background
2.1 Equivariant Machine-Learned Interatomic Potentials
Machine-Learned Interatomic PotentialsAn MLIP maps atomic positions {ri}N i=1⊂R 3
and species{Zi}N i=1 to an invariant potential energyE =∑ iEi, with forcesFi =−∇riE [12, 13].
Species embeddings initialize scalar node featuresh(0) i , and a cutoff graph definesN (i) ={j̸ =i :
∥rj−ri∥<r cut}. Withrij =rj−ri, message-passing layert∈{ 1,...,T} updates these features
as [37]
h(t) i =U t ( h(t−1) i , ⨁
j∈N(i)
Mt
(
h(t−1) i ,h (t−1) j ,rij )) ,(1)
where Mt and Ut are learned message and update functions, and⨁ is permutation-invariant
aggregation. Invariant readouts giveEi =∑T t=1Rt(h(t) i ).
Equivariant Graph Neural NetworksEquivariant features are organized into blocksh(ℓ) i,km
with channelk, angular degreeℓ, and magnetic componentm∈{−ℓ,...,ℓ} . Under a rotation
R∈SO (3), h(ℓ) i,km↦→∑ m′D(ℓ) mm′(R)h(ℓ) i,km′, whereD(ℓ) is a Wigner D-matrix. The Clebsch–Gordan
(CG) tensor product couples feature blocks [63]:
(
f (ℓ1)⊗g (ℓ2))(ℓ) m = ∑
m1,m2
Cℓm ℓ1m1,ℓ2m2f (ℓ1) m1 g(ℓ2) m2 ,|ℓ 1−ℓ 2|≤ℓ≤ℓ 1 +ℓ 2.(2)
Learned weights, which may depend on invariants such as pair distances, combine channels along
the allowed coupling paths [35, 101]. Pooling these tensor-product messages over neighbors gives
the one-particle featuresai. Atomic cluster expansions build higher-body-order features fromai by
symmetric tensor contractions, where correlation orderν gives terms of up toν + 1atoms [8, 25, 26].
2.2 Fast Multipole Method
For scalar chargesqs, the Coulomb potentialV (ri) = (4πε0)−1∑ s̸=iqs/|ri−rs| costsO(N 2)to
evaluate directly. The FMM reduces this toO(N)by grouping particles in a spatial hierarchy
and summarizing each distant group by a truncated multipole expansion [17, 39]. It rests on the
Laplace expansion of1/|r>−r<|, wherer< =rs−cs is a particle’s offset from its source center and
r> =ct−cs is the separation of source and target centers. This expansion splits each interaction
into a regular factor|r<|ℓY⋆ ℓm(ˆr<)and an irregular factor Yℓm(ˆr>)/|r>|ℓ+1. The regular factor
builds and re-centers expansions. Particle-to-multipole (P2M) and multipole-to-multipole (M2M)
aggregate source moments up the tree, and local-to-local (L2L) and local-to-particle (L2P) carry
local expansions down and evaluate them. The irregular factor performs the single long-range
step, multipole-to-local (M2L), which converts the multipoles of well-separated clusters into a local
expansion. For the source listNτ(t)at stage τ∈{P2M,M2M,M2L,L2L,L2P} , each operator has
the form:
Φ(ℓτ t ) t = ∑
s∈Nτ (t)
[
Φ(ℓτ s ) s ⊗cτ
pτ⨁
ℓ=0
R(ℓ) τ (r)Y (ℓ)(ˆr) ](ℓτ t ) . (3)
HereΦ (ℓτ s ) s is the source state at stageτ: the particle chargeqs at P2M and the multipole or local
coefficients thereafter. The target stateΦ (ℓτ t ) t contains multipole coefficients at P2M and M2M,
local coefficients at M2L and L2L, and the scalar far-field output after L2P. Adding the directly
evaluated near field and applying the electrostatic prefactor gives the total Coulomb potential.
3

Preprint
The superscriptsℓτ s,ℓτ t label degree-block collections rather than single degrees:ℓP2M s ={0} and
ℓP2M t ={0,...,p} , with these reversed at L2P; both collections contain degrees0,...,p at M2M,
M2L and L2L. Herer points from the target particle or center to the source particle or center,
r =∥r∥, and ˆr =r/r. The stage definitions arepτ =p and R(ℓ) τ (r) =rℓ for P2M, M2M, L2L and
L2P, andpτ = 2p and R(ℓ) τ (r) =r−(ℓ+1) for M2L. M2L requires filter degrees through2p because
its input and output spatial degrees each extend top, while stored expansions still stop atp. At
L2P, filter degrees throughp contract with the local coefficients to yield a scalar. The vectorY (ℓ)
contains all2ℓ + 1real spherical-harmonic components. Scalar FMM has scalar particle charges and
output potentials, but its intermediate degree-ℓ coefficient blocks transform as irreducible tensors.
The weighted tensor product performs magnetic-component contractions and compatible-path
sums, with fixed addition-theorem and normalization weightscτ (Appendix A.2). Coulomb and
scalar-FMM equivariance are proved in Appendix A.1. The far-field series converges for separated
source and target enclosures,(Rs +Rt)/∥r>∥< θ < 1. At fixed p, with a linear-size hierarchy,
bounded leaf occupancy and bounded interaction lists, evaluation takesO(N)time and memory [17]
(Appendix H).
3 Related Work
ScalarLong-RangeChannelsandChargeEquilibrationPhysics-informedcorrectionspredict
per-atom scalars and couple them through prescribed Coulomb or damped dispersion potentials
[55, 83, 108, 109, 121]. Reciprocal-space approaches communicate the same invariant channels
through Ewald [27] or particle-mesh [21, 49] sums [16, 64, 72, 115]. Sum-of-Gaussians networks
instead learn the reciprocal-space decay tail at near-linear cost via non-uniform FFTs [53, 54], and
prolatespheroidalmollificationrepresentsprescribedinverse-powerchannelswithfewerFouriermodes
[69]. Charge equilibration redistributes globally coupled scalar charges [33, 36, 57, 61, 73, 85, 90].
Dense solves costO(N 3)time and O(N 2)memory [ 33, 43], and particle-mesh, iterative, and
variational formulations improve scaling [43, 58, 62, 93, 112]. NEMORA transmits scalar and
higher-degree tensor charges through a learned kernel atO(N)cost, on a real-space hierarchy that
requires neither a Fourier grid nor periodicity.
Tensorial Transport and Many-Body RepresentationsDensity-based descriptors encode
non-local environments through atomic density and potential representations [28, 42]. Multipolar
corrections [11, 46, 80, 103, 104] and multipole embeddings of environmental charges [6] capture
directional electrostatics but keep prescribed interaction kernels. Tensorial long-range extensions
use fixed componentwise radial kernels or degree-preserving spectral filters [91, 127]. For equivariant
linear maps conditioned only on invariants, Schur’s lemma restricts learned weights to channel mixing
within each degree [35, 91]. Global matrix-function approaches give non-local equivariant many-body
representations, but atO(N 3)time andO(N 2)memory [9]. NEMORA’s operators condition on
directions throughY (ℓ)(ˆr), so learned CG paths couple degrees, and symmetric contractions of the
aggregated tensors add many-body terms at each level, at linear cost.
Global and Hierarchical CommunicationGlobal all-to-all attention learns non-local coupling
atO(N 2)cost [ 88]. Scalar virtual-node aggregation is linear but transmits only invariants [15].
Tensorial global attention is linear at a fixed spherical quadrature, but its rotational equivariance
is exact only up to the quadrature degree, which must grow with frequency and spatial extent
[32]. Equivariant atom–fragment attention transmits directional features over an enlarged finite
cutoff [113]. Graph hierarchies communicate across scales through coarsening, message passing and
4

Preprint
pooling, including equivariant constructions [48, 51, 76, 89, 95, 120, 123]. Tree-based architectures
combine spatial partitioning with local attention [129], fragment-based corrections couple atoms
and chemistry-defined fragments [67], and hierarchical particle models canonicalize two-level local
and global graphs in PCA frames, with predefined groups aggregated into averaged invariant nodes
[71]. NEMORA instead builds its hierarchy on the FMM well-separation criterion, so its analytical
limit inherits multipole convergence guarantees.
FMM-Inspired Neural ArchitecturesMultilevel graph kernels andH2-matrix [47] networks
learn non-local operators on graphs and point clouds [68,99]. Neural FMMs learn hierarchical transla-
tion stages for PDE solution operators, including point-cloud variants [29, 30], and multipole-inspired
attention cuts global attention cost [20, 56]. Differentiable FMM solvers give gradients for inverse
problems with prescribed kernels [98]. For atomistic potentials, NEMORA translates multipole
features between well-separated regions of an adaptive hierarchy with equivariant tensor transport,
learned angular coupling, modulated analytical radial factors, and many-body contractions.
4 NEMORA Architecture
NEMORA FrameworkNEMORA makes the FMM operators (P2M, M2M, M2L, L2L, L2P)
learnable, passing equivariant tensor features up to a chosenℓmax through an adaptive hierarchy.
Unless stated otherwise, NEMORA is attached to a MACE backbone [8].
4.1 Neural Equivariant Multipole Operators
Learnable equivariant tensor charges.We replace the scalar FMM charges qj with an
equivariant tensor chargeQ(ℓQ) j . In a coupled real spherical-harmonic basis, each stage has the
same form as Equation 3, with tensor-valued source states and the corresponding fixed re-coupling
weights. The component-wise Coulomb kernel is unchanged:
Φ(ℓτ t ) t = ∑
s∈Nτ (t)
[
Φ(ℓτ s ) s ⊗cτ
pτ⨁
ℓ=0
R(ℓ) τ (r)Y (ℓ)(ˆr) ](ℓτ t ) . (4)
At P2M, the particle input hasℓP2M s ={ℓQ}. For each spatial order n = 0,...,p , the target
expansion retains every coupled degreeL satisfying|ℓQ−n|≤L≤ℓ Q +n. These blocks form both
the source and target representations for M2M, M2L and L2L, with repeated degrees arising from
different spatial orders retained as distinct multiplicity channels. At L2P, the source contains these
expansion blocks and the target returns toℓL2P t ={ℓQ}. ThusℓQ labels the original charge, not
every intermediate source degree. The weighted tensor product performs the magnetic-component
contractions and sums over compatible input blocks and coupling paths;⨁ ℓ retains the harmonic
blocks, rather than summing them to a scalar. Kernel and expansion equivariance are proved in
Appendix B.1, with fixed stage weights and phase conventions in Appendix B.2. This is an analytical
subset of NEMORA: long-range operators that approximate an analytical long-range kernel to
transmit learned charges, which are scalar monopoles atℓQ = 0and tensor-valued sources at higher
degree, with physical atomic multipoles requiring kernel derivatives. These tensor-valued charges,
which can be read as learned atomic multipoles, add angular degrees of freedom that distributed
scalar charges lack. The source degreeℓQ sets expressivity and the expansion orderp sets accuracy.
Latent-Ewald-based methods [16, 91] evaluate learned charges with Ewald sums, whereas analytical
NEMORA uses the adaptive,O(N)FMM algorithm.
5

Preprint
Figure 1: NEMORA: a learnable Fast Multipole Method for atomistic ML. (1) NEMORA
module(top).Givenbackbonefeatures h(ℓQ,t⋆) i andpositions{ri}, NEMORAreturnsequivariantcorrections
∆h(ℓQ,t⋆) i and a scalar contribution∆E(t⋆). An upward sweep (P2M, M2M) builds cluster moments; at
each downward level, the M2L far field is fused with a local Kelvin self-correction (LKT) and a many-body
contraction (MBC) before L2L. Leaf L2P outputs are summed with a global Kelvin reaction-field branch
(GKT).(2) NEMORA–MLIP integration (bottom left).NEMORA updates the backbone equivariants
at iterationt⋆, and per-iteration readouts add∆E(t⋆) to the atomic energy.(3, 4) Classical FMM (right).
Translation of multipole (blue) and local (red) expansions, and the correspondingH2 factorization [47]
K=K NEAR +K F ARwithK F AR≈L2P·L2L·M2L·M2M·P2M.
4.2 MLIP Messages and Multipole Expansions
Centered on atomt with backbone features as sources, the P2M coupling underlying Equation 4
takes the form of an equivariant MLIP message:
a(˜ℓt) t = ∑
s∈Nt
[
h(˜ℓs) s ⊗θ ℓmax⨁
ℓ=0
R(ℓ) θ (r)Y (ℓ)(ˆr) ](˜ℓt) .(5)
Herer =rs−rt,r =∥r∥, ˆr =r/r, andNt is the local neighborhood oft. The tildes in˜ℓs, ˜ℓt denote
architecture-configured source and target degree-block collections and multiplicities, rather than
analytically prescribed ones. This is the pooled tensor-product message of Section 2.1, read as a
learnable local multipole expansion: the source featurehs plays the role of the tensor chargeQs, the
channel-wise radial weightsR(ℓ) θ (r)replace the regular radial factorrℓ, and the learned path weights
6

Preprint
replace the fixed analytical coupling weights. Settingh(0) s =qs andR(ℓ) θ (r) =rℓ1, with matching
harmonic normalization, path weights and retained degrees, recovers the classical moments about
atom t. As in Equation 4, the concatenated harmonic blocks retain their angular degrees, and the
tensor product combines compatible coupling paths into the configured target blocks. We therefore
read the pooled features of the one-particle basis [10] as learnable local multipole expansions, whose
symmetric contractions build body order, and let the FMM carry them across length scales. This
correspondence is NEMORA’s design principle: local message passing already makes P2M learnable,
and NEMORA does the same for every other FMM stage.
4.3 Learnable Equivariant Multipole Operators
Equations 3–4 describe individual analytical FMM stages, and Equation 5 gives their analogy with
local message-passing. Following this correspondence, we replace each analytical operator with a
learnable equivariant one:
Ψ(˜ℓτ t ) t = ∑
s∈Nτ (t)
α(˜ℓτ t ) θ,st [ WV Ψ(˜ℓτ s ) s ⊗θτ p⨁
ℓ=0
R(ℓ) τ (r)R (ℓ) θ (r)Y (ℓ)(ˆr) ](˜ℓτ t ) .(6)
HereΨ s contains the tensor charges at P2M and the learned multipole or local features thereafter.
The targetΨ t contains the corresponding updated features, with L2P returning particle-level
equivariant features for energy fusion and readout, rather than a prescribed Coulomb potential. The
tilded source and target degree-block collections are architecture-configured as in Equation 5, with
τ identifying the FMM operator stage. The displacementr, radiusr and scalar radial factorR(ℓ) τ (r)
follow the stage definitions in Section 2.2; numerical implementations normalize and regularize the
radial coordinates.
The mapWV mixes channels within each degree, while⊗θτ learns weights over compatible CG
coupling paths, incorporating the magnetic-component sums and generalizing the fixed analytical
stage coefficients. Harmonic-normalization and recoupling factors can be absorbed into these weights
on the represented paths. The channelwise functionR(ℓ) θ (r)provides a bounded multiplicative
modulation of the analytical radial factor, evaluated using a sinc–Bessel basis [34]. As in the MLIP
equation, this notation includes the radial-basis evaluation and does not imply parameter sharing
between models or stages. A gateα(ℓM) θ,st = ϕθ(Gst⊕M st⊕A st)(ℓM) weights each source using
geometric invariantsGst, normalized featuresMst and alignment invariantsAst, acting blockwise
for each target degreeℓM in ˜ℓτ t. It serves as a learned analogue of damping and polarization
factors [86, 97, 100] (Appendix C.2).
Setting WV = I, R(ℓ) θ =1, αθ = 1and the analytical path weights formally recovers the
analytical operator when the required intermediate representations, filter degrees and normalizations
are retained. At each downward level, symmetric contractions of the pooled M2L field add explicit
many-body features (MBC; Appendices K.1 and D), and a learnable Kelvin transform adds a
continuum boundary response (LKT/GKT; Appendices K.2 and F). Under periodic boundary
conditions, a finite-shell, degree-diagonal correction at the root accounts for periodic images
(Equation 30).
4.4 Energy Fusion and Readout
NEMORA acts at chosen layerst⋆ of the backbone (Section 2.1) and takes its tensor charges from
these features. An input projection mixes channels within each degree,Q(ℓQ) i =W (ℓQ) in h(ℓQ,t⋆) i , and
the operators couple degrees along the hierarchy. A degree-preserving projectionW (ℓQ) out and an
7

Preprint
invariant gate return the far-field update∆h(ℓQ,t⋆) i . The corrected features replaceh(ℓQ,t⋆) i in the
layer-t⋆ readout and all later layers, and a scalar readout of the update adds∆E(t⋆) i to the energy:
˜h(ℓQ,t⋆) i =h (ℓQ,t⋆) i + ∆h(ℓQ,t⋆) i , E i = T∑
t=1
Rt(h(t) i ) + MLP ( ∆h(0,t⋆) i ) /bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
∆E(t⋆) i
.(7)
The equivariance and invariant-readout arguments are given in Appendices C.1 and C.3.
4.5 AdaptiveE(3)-Equivariant Hierarchy
The hierarchy is built by top-down adaptive subdivision [5, 117, 122]. Each cluster splits along
the PCA eigenframe of its centered atomic offsets, or the Gram–Schmidt lattice frame under PBC.
An axis is active when its eigenvalue ratioλk/λmax exceeds a threshold, and the fanout2nactive
gives binary, quadtree, or octree splits for chain, slab, and bulk geometries. A cluster becomes
a leaf when its predicted child diameter falls below the backbone receptive fieldnSRrcut or its
atom count drops below a threshold. Equivariance requires frame selection and cluster assignment
to transform with the geometry, including periodic cells, with symmetry-consistent handling of
degenerate eigenframes and sign or partition ties (Appendix A.1). At levelL, the near set is
NearL(B) ={A :∥cA−cB∥MIC≤ρ near(RA +RB)} with ρnear≥ 1, so every far pair has separation
ratio(RA +RB)/∥cA−cB∥MIC< 1/ρnear≤ 1, ensuring convergence of the analytical expansion. The
M2L listIL(B)holds the children of the parent’s near clusters that are not nearB. Near leaf pairs
also use M2L, weighted by an envelope of their gap distancedmin = max(∥cA−cB∥MIC−RA−RB, 0)
so that the short- and long-range channels hand off smoothly [34]. Evaluation is linear inN when
the hierarchy hasO(N)nodes and bounded interaction lists (Appendix H).
5 Results
We evaluate NEMORA on molecular and periodic systems that probe different forms of nonlocal
interaction. Unless otherwise stated, tables report means over three independent training runs, with
energy in meV/atom and force in meV/Å. Training details are in Appendix N.
5.1 Cumulene
Two cumulene experiments probe long-range electronic delocalization and its dependence on ge-
ometry [9]. The first trains onnC = 3–10, 13, 14and tests on these lengths (in-distribution, ID),
on the unseen lengths 11 and 12 (semi-out-of-distribution, SOD), and on the longer chains 15 and
16 (out-of-distribution, OOD). The second covers the end-group torsional angle energy profile at
a fixed chain length as well as the chain-length dependence of the energy at fixed torsional angle
on a separate 3–64 carbon set. Both of these benchmarks test the ability of models to effectively
transmit angular information over long range and learn the effect that local angular structure has
on the long-range interactions.
The first section of Table 1 shows that NEMORA substantially improves energy and force
predictions over short-range MACE and scalar long-range models, as well as equivariant long-range
models that are sub-cubic in complexity. NEMORA has the lowest ID energy error and is second
only to MACE–MFN, which scales asON 3, on the remaining splits and metrics. NEMORA has
lower energy and similar force ID errors to LOREM and EFA, the other tensor long-range models,
but on unseen chain lengths LOREM and EFA degrade to higher errors than short-range MACE,
8

Preprint
Table 1:Cumulene chain-length, nonlocal charge-transfer, and MD22 benchmark errors. Each entry is E
RMSE (meV/atom)/F RMSE (meV/Å). Cumulene splits are defined in Section 5.1. Nonlocal charge-transfer
datasets and training protocols are detailed in Appendices M and N.7. MD22 entries are means over three
seeds; protocol exceptions are given in Appendix N.7.5. In each row and metric, lowest means are bold and
second-lowest underlined (ties retained).
System MACE MACE–LES MACE–RANGE LOREM EFA MACE–MFNNEMORA (Ours)
E RMSE/F RMSE E RMSE/F RMSE E RMSE/F RMSE E RMSE/F RMSE E RMSE/F RMSE E RMSE/F RMSE E RMSE/F RMSE
Cumulene
ID16.898/85.07 17.235/84.82 19.505/95.60 6.756/29.36 5.918/30.28 3.231 /13.83 3.203/26.85
SOD16.709/102.16 16.560/102.17 18.796/112.98 27.251/166.70 27.884/158.170.643/14.250.744 /47.87
OOD11.994/72.26 11.180/72.36 16.411/94.90 25.008/133.06 20.810/93.922.812/15.283.770 /57.01
Nonlocal charge transfer
Carbon chain0.425/15.00 0.524/20.15 0.932/12.38 0.640/4.62 0.502/5.640.156/1.90 0.175/1.88
NaCl1.600/43.89 0.380/7.21 0.622/2.930.243/1.76 0.861/18.13 0.361 /2.75 0.412/1.75
Au2/MgO2.385/110.07 1.696/21.85 0.207 /12.18 0.235/4.641.890/13.03—0.197/5.26
MD22
Ac-Ala3-NHMe0.405/7.44 0.348 /7.08 0.461/12.45 1.367/13.96 1.146/53.63—0.323/6.93
DHA0.575 /5.640.586/5.87 0.747/9.08 1.273/9.74 0.735/41.51—0.455/5.70
Stachyose0.375 /6.64 0.463/6.24 0.309/10.15 1.271/12.36 0.604/53.19—0.401/6.45
AT-AT1.168/10.78 1.005/8.04 0.739/15.88 1.475/14.90 1.043/63.83—0.340/7.85
AT-AT-CG-CG0.766/10.26 0.927/8.120.647/16.73 1.241/18.10 0.606 /63.28—0.341/8.60
buckyball-catcher1.099/8.22 1.087/7.96 1.200/17.91 1.350/10.420.731/102.00—1.081 /7.54
Nanotube1.406/24.75 1.806/28.91 5.551/45.57 1.361 /28.071.086/174.25—1.362/22.32
whereas NEMORA remains well below the MACE error. This indicates that NEMORA is learning
a more effective representation of the features that determine the energy in the long-range cumulene
system. Degradation of performance upon extrapolation in chain-length can indicate overfitting
to training data, rather than learning correct representations. MACE–MFN remains the most
accurate on these splits except for ID energy, at the cost of cubic time and quadratic memory scaling
(Figure 4). Together with the additional scalar NEMORA ablations provided in Appendix L.5, these
results indicate that transmitting angular information is vital to performance in cumulene.
Figure 2(a,b) presents the separate angular and chain-length experiments. Rotating the terminal
groups changes the energy significantly, even when the terminal groups lie beyond the short-range
receptive field. Short-range MACE and the scalar long-range models, MACE–LES and MACE–
RANGE, predict flat torsional profiles, missing this angular dependence. The higher-order long-range
models are able to follow the DFT angular profile, with NEMORA and MACE–MFN being closest.
Similar results are obtained for the even–odd (zig-zag) energy variation with chain length, with
short-range models and scalar long-range models failing to capture the energy of the different
angular conformations beyond their receptive field. Long-range models with higher-order angular
information, however, are able to capture the zig-zag profile to differing degrees, with NEMORA
and MACE–MFN matching the DFT profile best over the full range of chain lengths while the
torsional profile of LOREM and EFA degrade, partially and completely, respectively, after seventeen
carbons. The corresponding energy and force errors are provided in Table 8 in the Appendix.
5.2 Nonlocal charge transfer
The nonlocal charge transfer benchmark datasets introduced by Ko et al.[61] test the effect of
nonlocal charge transfer in different contexts. In the C10H2/C10H+ 3 system, protonation changes the
charge distribution and electronic structure along a conjugated carbon chain. In the Na8Cl+ 8 /Na9Cl+ 8
(NaCl) cluster, an additional neutral sodium atom affects the binding of another sodium atom on
the opposite side of the cluster. The Au2/MgO dataset tests the effect of substrate doping on an
adsorbed gold dimer under periodic boundary conditions.
As shown in the second section of Table 1, NEMORA substantially improves upon MACE
9

Preprint
Figure 2:Cumulene angular and chain-length benchmarks [ 9] and a charged sodium chloride cluster
benchmark [61]. (a) Torsional energy profile for a 12-carbon chain. (b) Energy as a function of chain length
at φ = 5◦. (c) Energy versus Na displacement in Na8Cl+ 8 and Na9Cl+ 8 , where an extra neutral Na atom
∼21 Å away changes the binding profile. Gray curves are DFT references, and model curves are shifted
vertically for visual clarity.
across all three datasets and, among the long-range models, ranks first or second on five out of six
metrics, with the lowest force errors on the carbon chain and NaCl and the lowest energy error
on Au2/MgO. While some other long-range models do compete for accuracy on these benchmarks,
we stress the ability of NEMORA to achieve this state-of-the-art accuracy while retainingO(N)
time and memory scaling in both periodic and non-periodic systems alike. Figure 2(c) illustrates
the energy profile along the sodium removal pathway for the NaCl cluster, with and without the
additional neutral sodium on the opposing side. Unsurprisingly, short-range models are unable to
accurately capture the shape and minimum of the energy profile in both cases, while all models
with long-range information generally capture these effects. These benchmarks combined with the
cumulene benchmarks indicate that NEMORA is capable of capturing different types of long-range
interactions ranging from highly angular (cumulene) to scalar charge redistribution (nonlocal charge
transfer).
Table 1 excludes charge-equilibration and explicitly electrostatic models (CELLI, 4G–HDNNP
and SpookyNet) [33, 61, 109], which add reference-charge terms to the loss or use supervision through
total charge and spin inputs. Using these extra inputs and loss terms, CELLI and SpookyNet
reach lower NaCl and Au2/MgO energy errors but perform worse than short-range benchmarks on
cumulene (Table 6, Appendix L).
5.3 MD22
Table 1 also includes MACE–RANGE, LOREM and EFA evaluated on the same MD22 test splits,
with three seeds per model and system. Their checkpoint-selection and numerical-evaluation
protocols are given in Appendix N.7.5. MACE–MFN is omitted on MD22 because the native
training campaign was stopped before completion owing to computational cost; early-epoch timings
on L40S/H200 indicated multi-day runs. Training also developed exploding losses on the buckyball
catcher system.
To test whether NEMORA degrades accuracy when a short-range model already performs
well owing to relatively weak long-range interactions, we train and evaluate it on all seven MD22
systems [18], comparing MACE, MACE–LES, MACE–RANGE, LOREM, EFA, and NEMORA
(Appendix N.7.5). As shown in Table 1, NEMORA lowers energy errors on six systems and force
10

Preprint
errors on six systems relative to MACE, and achieves the lowest energy and force error among
MACE, MACE–LES and NEMORA on four systems. The largest gains occur in the DNA base-
pair systems, where energy errors fall from 1.168 to 0.340 meV/atom (AT-AT) and from 0.766 to
0.341 meV/atom (AT-AT-CG-CG). For the nanotube system, NEMORA reduces the force error from
24.75 to 22.32 meV/Å, whereas MACE–LES increases it to 28.91 meV/Å. MACE–RANGE, LOREM,
and EFA also have higher force errors on all seven systems relative to the short-range baseline and
higher energy errors on four to seven systems. The two NEMORA performance regressions relative
to MACE are minor: an increase of 0.06 meV/Å in force on DHA and 0.026 meV/atom in energy
on Stachyose. NEMORA therefore generally preserves or improves the accuracy of the short-range
backbone on these systems. These results are consistent with a largely non-disruptive extension,
contributing when long-range interactions become non-negligible rather than interfering with the
underlying short-range backbone’s learned representations.
5.4 Portability across backbones and the role of angular features
Table 2:Backbone and source-degree ablations, mean validation E/F RMSE (meV/atom/meV/Å). SR is
the short-range backbone, andℓQ = 0and ℓQ = 2are scalar and degree-two NEMORA sources, lifted for
scalar and untyped hosts. Bold and underline mark the lowest and second-lowest of the three settings per
host, dataset and metric (Appendix L.4).
NaCl Cumulene
Backbone Host SRℓ Q = 0ℓ Q = 2SRℓ Q = 0ℓ Q = 2
MACE [8] Native1.597/43.92 0.457 /3.45 0.406/1.8013.672 /109.82 13.767/105.93 3.776/65.93
Scalar1.600/44.51 0.475 /7.56 0.437/1.8852.466 /196.28 53.357/195.93 4.134/77.32
NequIP [12] Native1.565/43.89 0.664 /6.39 0.258/1.8554.699 /203.77 55.097/206.563.916/46.06
Scalar1.774/62.70 0.561 /11.40 0.242/2.2355.939 /239.69 56.752/239.29 5.567/81.59
ViSNet [116] Native1.533/42.02 0.230 /4.04 0.145/1.6714.630 /120.86 25.020/150.243.723/46.35
Scalar1.711/59.46 0.876 /8.12 0.302/2.3056.132 /240.12 56.871/239.85 4.150/70.53
PET [87] Untyped1.524/38.910.260/5.64 0.485/4.5554.814/241.43 45.183 /221.56 9.363/112.11
Although we attach NEMORA to MACE throughout this work for consistency, it can be attached
to a variety of architecturally distinct short-range architectures. To demonstrate this ability, we
test MACE, NequIP, ViSNet, and PET [8, 12, 87, 116], while varying the degree of the short-range
features and the NEMORA expansions (Table 2). For MACE, NequIP, and ViSNet, we compare the
native equivariant backbone with a scalar-only variant. Each is trained without NEMORA, with
scalar NEMORA (ℓQ = 0), and with degree-two NEMORA (ℓQ = 2). When the backbone supplies
only scalar features, a geometry-based lift constructs the tensorial sources by performing a tensor
product of the source features with the concatenated spherical harmonics in the P2M operator. The
same interface allows attachment to the rotationally unconstrained PET architecture.
On the charged NaCl cluster (Na8Cl+ 8 /Na9Cl+ 8 ), where the nonlocal interaction is predominantly
electrostatic, scalar NEMORA (ℓQ = 0) already captures most of the improvement over the short-
range models. Degree-two sources (ℓQ = 2) further reduce force errors for every backbone, and
energy errors for all but PET. On cumulene, scalar long-range communication gives little or no
improvement, while degree-two sources reduce errors substantially for every backbone. Surprisingly,
the geometry-based lift recovers much of this improvement when the short-range backbone contains
only scalar features. These results show that the NEMORA channel can supply angular information
missing from the backbone, across all four backbones tested. Interestingly, PET is not equivariant
by construction, but the higher degree NEMORA attachment is able to significantly improve its
11

Preprint
performance by incorporating an equivariant long-range correction.
5.5 Periodic ions and water
Table 3:Periodic-ion and water test errors, E RMSE (meV/atom)/F RMSE (meV/Å). Ion models are
trained onN = 256–1024. Water models are trained on 128 and 256 molecules. The analytical NEMORA
with scalar (ℓQ = 0) or scalar-plus-dipole (ℓQ = 1) sources is used (Appendix K.4).
System MACE MACE–LES NEMORA (ℓ Q = 0) NEMORA (ℓQ = 1)
Periodic ions
N= 256 43.43/168.6 0.308/9.80 0.284 /9.64 0.237/8.41
N= 512 24.59/195.8 0.203 /10.01 0.211/9.83 0.173/8.58
N= 1024 65.90/265.2 0.155/9.88 0.133 /9.69 0.123/8.46
N= 2048(OOD)97.24/329.8 0.142/9.95 0.109 /9.78 0.080/8.53
N= 4096(OOD)110.63/363.5 0.120/9.95 0.090 /9.79 0.067/8.54
Water0.415/20.83 0.400 /14.35 0.405/14.440.305/11.86
We next consider a synthetic periodic binary ionic melt benchmark with Lennard-Jones inter-
actions and fixed charges of±0.6e, using Ewald/PPPM [27, 49] for reference energies and forces.
For this pairwise system, we use analytical NEMORA and compare it directly to MACE and
MACE–LES. As shown in Table 3, both MACE–LES and NEMORA reduce the errors of short-range
MACE by two to three orders of magnitude in energy, and by more than an order of magnitude in
force. Furthermore, both models extrapolate to larger, unseen system sizes without losing accuracy,
with NEMORA remaining slightly more accurate at nearly every size. Additionally, both models
recover the±0.6e charge within their latent scalar features (Table 12). Thus, both successfully learn
the true potential energy and forces arising from long-range Coulomb interactions, alongside the
short-range interactions, without explicit supervision.
We trained MACE, MACE–LES, and NEMORA on a periodic system of water labeled at the
revPBE-D3 level, as described in Appendices L.7 and M.7. In this case, dipolar NEMORA (ℓQ = 1)
has the lowest energy and force errors (Table 3) among the tested models. With scalar sources,
NEMORA matches MACE–LES (Table 13), indicating that the accuracy gain comes from the
dipoles.
To test NEMORA in molecular dynamics, we simulate water in the NVE and NVT ensembles
with the scalar model (ℓQ = 0). NVE trajectories test the numerical energy conservation of the
learned potential. Over 200 ps of velocity-Verlet integration with a 0.5 fs timestep, deuterium
masses and a temperature of about 300 K, a cubic box of 512 water molecules has an overall drift
of6 · 10−4 meV/atom (Figure 3). In the timestep scan from 0.5 to 2 fs, the root-mean-square
fluctuation of the total energy grows approximately as∆t2, as expected for the velocity-Verlet
integrator (Figure 5, Appendix L.9).
Figure 3(a,b,d,e) shows NVT molecular dynamics of 2048 water molecules, eight times the largest
training system, in an elongated periodic box whose long axis gives access to small wavevectors
(Appendix L.10). Importantly, we find that the potential energy and temperature remain stable
along the trajectory (b). Both NEMORA and MACE–LES reproduce the long-wavelength behavior
of the polarization density correlation function,gL(k)(d), whereas short-range MACE rises sharply
as k→ 0. On the other hand, all three models give nearly identical O–O radial distributions,
indicating that standard structural observables cannot distinguish them, and highlighting the need
for dedicated long-range benchmarks.
12

Preprint
Figure 3:Water molecular dynamics. (a) 2048 water molecules in a24.84× 24.84× 99.35Å box at 300 K.
(b) NEMORA potential energy and temperature along the NVT trajectory. (c) Total energy drift during
NVE simulation of 512 water molecules in a cubic box. (d) Longitudinal dipole correlationgL(k). (e) O–O
radial distributiong OO(r). Models are those of Table 3.
5.6 Time and memory scaling
We next test the evaluation time and GPU memory scaling over a broad range of system sizes using
randomized configurations of particles in non-periodic clusters and periodic cubic boxes. As shown in
Figure 4, NEMORA scales linearly in both time and memory, in non-periodic and periodic systems
alike, and we ran it to about340,000atoms on a single H200, where one energy and force evaluation
takes about 1.2–1.3 s at262,144atoms. The fitted exponents of the long-range component are
0.89–1.00; values slightly below one reflect fixed per-call overhead rather than a sublinear algorithm.
The long-range models closest to NEMORA in accuracy on the benchmarks above do not scale
in this way. Dense MFN has quadratic memory scaling and exhausts the memory of the H200
beyond roughly 512 atoms, where computation times are already intractable with cubic scaling.
LOREM and LES evaluate the long-range energy with an Ewald sum in periodic systems and a direct
pairwise sum in non-periodic ones, and both scale asO(N 2)in the tested backends; an optimally
tuned periodic Ewald sum would scale asO(N 3/2)and particle-mesh variants asO(NlogN ), as
demonstrated for LOREM by its authors [91], although that backend is not used here. LOREM
exhausts the memory of an H200 at about11,500atoms in periodic boxes, and100,000atoms in
non-periodic clusters.
RANGE and EFA also scale linearly in time and memory (Tables 15–18), but they are less
accurate on the long-range benchmarks as demonstrated in previous sections, and RANGE uses more
13

Preprint
memory than NEMORA at fixed backbone capacity. In large non-periodic systems EFA uses more
memory and more time per step than NEMORA, owing to its Lebedev-grid attention; in periodic
systems the Lebedev grid is not used and EFA needs less memory. EFA and LOREM use different
backbones and feature representations from NEMORA’s correlation-order-three MACE backbone,
so these costs are not an accuracy-matched comparison. For non-periodic EFA, our fixed 194-point
grid andbmax = 4π imply ωmax = 4π/rmax, which decreases as the cluster diameterrmax grows;
maintaining a fixed physical frequency range and quadrature accuracy would require increasingbmax
and the grid size, with additional time and memory costs [32], whereas our NEMORA benchmark
grows its hierarchy at fixed expansion order.
Figure 4:(a) Time and (b) peak GPU memory of one energy and force evaluation on fixed-density periodic
and non-periodic particle configurations, run fromN = 64up to about340 ,000atoms on one H200. Curves
ending before the upperN limit exhausted the GPU memory. Raw data is summarized in Tables 15–18. All
models share the MACE short-range backbone except EFA and LOREM, which use their own short-range
architectures.
6 Discussion and Conclusion
NEMORA extends short-range interatomic potentials with an equivariant multipole hierarchy that
learns to transmit and combine angular information over long distances. On cumulene, scalar
long-range models miss the response to terminal-group rotation, while NEMORA captures the
torsional profile and, on unseen chain lengths, is second only to MACE–MFN at linear rather than
cubic cost. The backbone and component ablations support this across architectures. On ionic
clusters, where scalar charges describe much of the interaction, scalar NEMORA already offers a
significant improvement.
Fixing the transport operators gives analytical NEMORA with learned atomic charges and
dipoles. The scalar model evaluated on the synthetic ionic melt benchmark and water is comparable
to MACE-LES, but higher-degree atomic dipoles improve water predictions. The learned NEMORA
operators have linear runtime and memory. NEMORA generally preserves or improves short-range
accuracy on MD22, augments a variety of symmetry-constrained and -unconstrained short-range
backbones, and supports stable periodic-water dynamics, at twice and eight times the largest training
size on NVE and NVT ensembles, respectively. Its hierarchy is equivariant only up to eigenframe
degeneracy, and learned operators forgo the convergence guarantees of the analytical FMM. Next
steps are broader chemical tests on more complex systems.
14

Preprint
Reproducibility, data, and code availability
The reported experiments use both PyTorch and JAX implementations. Benchmark run counts and
exclusions are recorded in Appendix L; differences in training schedules and the backbone, optimizer
and NEMORA settings for each benchmark are given in Tables 22 and 23 and Appendix N.7.
Additional experiment protocols accompany their results. Across-run uncertainties are SEMs unless
explicitly identified as block estimates for molecular dynamics. Single-run measurements and
selected-seed profiles are identified separately.
Datasets originate from the cited primary sources, except the synthetic ionic datasets and
periodic water dataset generated in this work. Code and both datasets will be released upon
publication at https://github.com/JayLKap/nemora. Trained NEMORA models will be made
publicly available in a future release. Training and simulation scripts will be made available by the
corresponding author upon reasonable request.
Generative AI tools assisted with code implementation, experiment execution, figure preparation,
literature review, and manuscript editing under author supervision. The authors reviewed the
AI-assisted work and take full responsibility for the final content.
References
[1] Uri Alon and Eran Yahav. On the bottleneck of graph neural networks and its practical
implications. InInternational Conference on Learning Representations, 2021. URLhttps:
//arxiv.org/abs/2006.05205.
[2] R. L. P. G. Amaral, O. S. Ventura, and N. A. Lemos. Kelvin transformation and inverse
multipoles in electrostatics.European Journal of Physics, 38(2):025206, March 2017. ISSN 0143-
0807, 1361-6404. doi: 10.1088/1361-6404/aa55a0. URLhttp://arxiv.org/abs/1611.05942.
arXiv:1611.05942 [physics].
[3] Dylan M. Anstine and Olexandr Isayev. Machine Learning Interatomic Potentials and Long-
Range Physics.The Journal of Physical Chemistry A, 127(11):2417–2431, March 2023. ISSN
1089-5639. doi: 10.1021/acs.jpca.2c06778. URL https://doi.org/10.1021/acs.jpca.2c0
6778.
[4] B. M. Axilrod and E. Teller. Interaction of the van der Waals Type Between Three Atoms.
The Journal of Chemical Physics, 11(6):299–300, June 1943. ISSN 0021-9606. doi: 10.1063/1.
1723844. URL https://pubs.aip.org/aip/jcp/article/11/6/299/182086/Interaction
-of-the-van-der-Waals-Type-Between.
[5] Josh Barnes and Piet Hut. A hierarchical O(N log N) force-calculation algorithm.Nature,
324(6096):446–449, December 1986. ISSN 1476-4687. doi: 10.1038/324446a0. URLhttps:
//www.nature.com/articles/324446a0.
[6] Rhyan Barrett, Johannes C. B. Dietschreit, and Julia Westermayr. Incorporating long-range
interactions via the multipole expansion into ground and excited-state molecular simulations.
npj Computational Materials, 12(1):135, March 2026. ISSN 2057-3960. doi: 10.1038/s41524-0
26-02048-3. URLhttps://www.nature.com/articles/s41524-026-02048-3.
[7] Albert P. Bartók, Mike C. Payne, Risi Kondor, and Gábor Csányi. Gaussian Approximation
Potentials: The Accuracy of Quantum Mechanics, without the Electrons.Physical Review
Letters, 104(13):136403, April 2010. doi: 10.1103/PhysRevLett.104.136403. URL https:
//link.aps.org/doi/10.1103/PhysRevLett.104.136403.
15

Preprint
[8] Ilyes Batatia, Dávid Péter Kovács, Gregor N. C. Simm, Christoph Ortner, and Gábor Csányi.
MACE: Higher Order Equivariant Message Passing Neural Networks for Fast and Accurate
Force Fields. InAdvances in Neural Information Processing Systems, volume 35, pp. 11423–
11436, December 2022. doi: 10.52202/068431-0830. URLhttp://arxiv.org/abs/2206.076
97.
[9] Ilyes Batatia, Lars L. Schaaf, Gábor Csányi, Christoph Ortner, and Felix A. Faber. Equivariant
matrix function neural networks. InInternational Conference on Learning Representations,
2024. URL https://proceedings.iclr.cc/paper_files/paper/2024/hash/0d5bfa7cb4
d570b23a0088e508020843-Abstract-Conference.html.
[10] Ilyes Batatia, Simon Batzner, Dávid Péter Kovács, Albert Musaelian, Gregor N. C. Simm,
Ralf Drautz, Christoph Ortner, Boris Kozinsky, and Gábor Csányi. The design space of
E(3)-equivariant atom-centred interatomic potentials.Nature Machine Intelligence, 7:56–
67, January 2025. ISSN 2522-5839. doi: 10.1038/s42256-024-00956-x. URL https:
//www.nature.com/articles/s42256-024-00956-x.
[11] Ilyes Batatia, William J. Baldwin, Domantas Kuryla, Joseph Hart, Elliott Kasoar, Alin M.
Elena, HarryMoore, MikołajJ.Gawkowski, BenjaminX.Shi, VenkatKapil, PanagiotisKourtis,
Ioan-Bogdan Magdău, and Gábor Csányi. MACE-POLAR-1: A Polarisable Electrostatic
Foundation Model for Molecular Chemistry, February 2026. URLhttp://arxiv.org/abs/
2602.19411. arXiv:2602.19411 [physics].
[12] Simon Batzner, Albert Musaelian, Lixin Sun, Mario Geiger, Jonathan P. Mailoa, Mordechai
Kornbluth, Nicola Molinari, Tess E. Smidt, and Boris Kozinsky. E(3)-equivariant graph neural
networks for data-efficient and accurate interatomic potentials.Nature Communications,
13(1):2453, May 2022. ISSN 2041-1723. doi: 10.1038/s41467-022-29939-5. URL https:
//www.nature.com/articles/s41467-022-29939-5.
[13] Jörg Behler and Michele Parrinello. Generalized Neural-Network Representation of High-
Dimensional Potential-Energy Surfaces.Physical Review Letters, 98(14):146401, April 2007.
doi: 10.1103/PhysRevLett.98.146401. URL https://link.aps.org/doi/10.1103/PhysRev
Lett.98.146401.
[14] M. Born. Volumen und Hydratationswärme der Ionen.Zeitschrift für Physik, 1(1):45–48,
February 1920. ISSN 1434-6001, 1434-601X. doi: 10.1007/BF01881023. URL http:
//link.springer.com/10.1007/BF01881023.
[15] Alessandro Caruso, Jacopo Venturin, Lorenzo Giambagli, Edoardo Rolando, Zakariya El-
Machachi, Frank Noé, and Cecilia Clementi. Extending the range of graph neural networks
with global encodings.Nature Communications, 17(1):1855, February 2026. ISSN 2041-1723.
doi: 10.1038/s41467-026-69715-3. URL https://www.nature.com/articles/s41467-026-6
9715-3.
[16] Bingqing Cheng. Latent Ewald summation for machine learning of long-range interactions.
npj Computational Materials, 11(1):80, March 2025. ISSN 2057-3960. doi: 10.1038/s41524-0
25-01577-7. URLhttps://www.nature.com/articles/s41524-025-01577-7.
[17] H. Cheng, L. Greengard, and V. Rokhlin. A Fast Adaptive Multipole Algorithm in Three
Dimensions.Journal of Computational Physics, 155(2):468–498, November 1999. ISSN
00219991. doi: 10.1006/jcph.1999.6355. URL https://linkinghub.elsevier.com/retrie
ve/pii/S0021999199963556.
16

Preprint
[18] Stefan Chmiela, Valentin Vassilev-Galindo, Oliver T. Unke, Adil Kabylda, Huziel E. Sauceda,
Alexandre Tkatchenko, and Klaus-Robert Müller. Accurate global machine learning force fields
for molecules with hundreds of atoms.Science Advances, 9(2):eadf0873, January 2023. doi:
10.1126/sciadv.adf0873. URLhttps://www.science.org/doi/10.1126/sciadv.adf0873.
[19] Indranil Chowdhury and Vikram Jandhyala. Single level multipole expansions and operators
for potentials of the formr−λ.SIAM Journal on Scientific Computing, 26(3):930–943, 2005.
doi: 10.1137/030602241.
[20] Alex Colagrande, Paul Caillon, Eva Feillet, and Alexandre Allauzen. Linear Attention with
Global Context: A Multipole Attention Mechanism for Vision and Physics. InIEEE/CVF
International Conference on Computer Vision Workshops (ICCVW), pp. 3130–3139, October
2025. doi: 10.1109/ICCVW69036.2025.00326. URLhttp://arxiv.org/abs/2507.02748.
[21] Tom Darden, Darrin York, and Lee Pedersen. Particle mesh Ewald: AnN·log (N)method
for Ewald sums in large systems.The Journal of Chemical Physics, 98(12):10089–10092, June
1993. ISSN 0021-9606, 1089-7690. doi: 10.1063/1.464397. URLhttps://doi.org/10.1063/
1.464397.
[22] S. W. de Leeuw, J. W. Perram, and E. R. Smith. Simulation of electrostatic systems in periodic
boundary conditions. I. Lattice sums and dielectric constants.Proceedings of the Royal Society
of London. A. Mathematical and Physical Sciences, 373(1752):27–56, October 1980. ISSN
0080-4630. doi: 10.1098/rspa.1980.0135. URL https://doi.org/10.1098/rspa.1980.0135.
[23] Walter Dehnen. A hierarchicalO(N)force calculation algorithm.Journal of Computational
Physics, 179(1):27–42, June 2002. doi: 10.1006/jcph.2002.7026.
[24] Francesco Di Giovanni, Lorenzo Giusti, Federico Barbero, Giulia Luise, Pietro Liò, and Michael
Bronstein. On Over-Squashing in Message Passing Neural Networks: The Impact of Width,
Depth, andTopology. InProceedings of the 40th International Conference on Machine Learning,
volume 202 ofPMLR, pp. 7865–7885, July 2023. URLhttp://arxiv.org/abs/2302.02941.
[25] Ralf Drautz. Atomic cluster expansion for accurate and transferable interatomic potentials.
Physical Review B, 99(1):014104, January 2019. doi: 10.1103/PhysRevB.99.014104. URL
https://link.aps.org/doi/10.1103/PhysRevB.99.014104.
[26] Geneviève Dusson, Markus Bachmayr, Gábor Csányi, Ralf Drautz, Simon Etter, Cas van der
Oord, and Christoph Ortner. Atomic cluster expansion: Completeness, efficiency and stability.
Journal of Computational Physics, 454:110946, April 2022. ISSN 0021-9991. doi: 10.1016/j.jc
p.2022.110946. URL https://www.sciencedirect.com/science/article/pii/S0021999
122000080.
[27] P. P. Ewald. Die Berechnung optischer und elektrostatischer Gitterpotentiale.Annalen der
Physik, 369(3):253–287, 1921. ISSN 1521-3889. doi: 10.1002/andp.19213690304.
[28] Carolin Faller, Merzuk Kaltak, and Georg Kresse. Density-Based Long-Range Electrostatic
Descriptors for Machine Learning Force Fields.The Journal of Chemical Physics, 161(21):
214701, December 2024. doi: 10.1063/5.0245615. URLhttp://arxiv.org/abs/2406.17595.
[29] Emilio McAllister Fognini, Marta M. Betcke, and Ben T. Cox. Learning Green’s Operators
through Hierarchical Neural Networks Inspired by the Fast Multipole Method, September
2025. URLhttp://arxiv.org/abs/2509.20591. arXiv:2509.20591 [cs].
17

Preprint
[30] Emilio McAllister Fognini, Marta M. Betcke, and Ben T. Cox. CloudNFMM: A hybrid
hierarchical and local neural operator inspired by the fast multipole method. In5th Annual
AAAI Workshop on AI to Accelerate Science and Engineering, 2026. URLhttps://ai-2-a
se.github.io/papers/CameraReadys%203-41/26/CameraReady/26.pdf.
[31] J. Thorben Frank, Oliver T. Unke, Klaus-Robert Müller, and Stefan Chmiela. A Euclidean
transformer for fast and stable machine learned force fields.Nature Communications, 15(1):
6539, 2024. ISSN 2041-1723. doi: 10.1038/s41467-024-50620-6. URLhttps://doi.org/10.1
038/s41467-024-50620-6.
[32] J. Thorben Frank, Stefan Chmiela, Klaus-Robert Müller, and Oliver T. Unke. Machine learning
global atomic representations with Euclidean fast attention.Nature Machine Intelligence,
8(3):388–402, March 2026. ISSN 2522-5839. doi: 10.1038/s42256-026-01195-y. URL
https://www.nature.com/articles/s42256-026-01195-y.
[33] Paul Fuchs, Michał Sanocki, and Julija Zavadlav. Learning non-local molecular interactions
via equivariant local representations and charge equilibration.npj Computational Materials,
11(1):287, September 2025. ISSN 2057-3960. doi: 10.1038/s41524-025-01790-4. URL
https://www.nature.com/articles/s41524-025-01790-4.
[34] Johannes Gasteiger, Janek Groß, and Stephan Günnemann. Directional message passing for
molecular graphs. InInternational Conference on Learning Representations (ICLR), 2020.
[35] Mario Geiger and Tess Smidt. e3nn: Euclidean Neural Networks, July 2022. URLhttp:
//arxiv.org/abs/2207.09453. arXiv:2207.09453 [cs].
[36] S. Alireza Ghasemi, Albert Hofstetter, Santanu Saha, and Stefan Goedecker. Interatomic
potentials for ionic systems with density functional accuracy based on charge densities obtained
by a neural network.Physical Review B, 92(4):045131, July 2015. doi: 10.1103/PhysRevB.92.
045131. URLhttps://link.aps.org/doi/10.1103/PhysRevB.92.045131.
[37] Justin Gilmer, Samuel S. Schoenholz, Patrick F. Riley, Oriol Vinyals, and George E. Dahl.
Neural message passing for Quantum chemistry. InProceedings of the 34th International
Conference on Machine Learning - Volume 70, ICML’17, pp. 1263–1272, Sydney, NSW,
Australia, August 2017. JMLR.org.
[38] Stefan Goedecker, Michael Teter, and Jürg Hutter. Separable dual-space Gaussian pseudopo-
tentials.Physical Review B, 54(3):1703–1710, 1996. doi: 10.1103/PhysRevB.54.1703. URL
https://doi.org/10.1103/PhysRevB.54.1703.
[39] L Greengard and V Rokhlin. A fast algorithm for particle simulations.Journal of Computa-
tional Physics, 73(2):325–348, December 1987. ISSN 0021-9991. doi: 10.1016/0021-9991(87)901
40-9. URLhttps://www.sciencedirect.com/science/article/pii/0021999187901409.
[40] Leslie Greengard, Michael O’Neil, Manas Rachh, and Felipe Vico. Fast multipole methods for
the evaluation of layer potentials with locally-corrected quadratures.Journal of Computational
Physics: X, 10:100092, 2021. doi: 10.1016/j.jcpx.2021.100092.
[41] Stefan Grimme, Jens Antony, Stephan Ehrlich, and Helge Krieg. A consistent and accurate ab
initio parametrization of density functional dispersion correction (DFT-D) for the 94 elements
H–Pu.The Journal of Chemical Physics, 132(15):154104, 2010. doi: 10.1063/1.3382344. URL
https://doi.org/10.1063/1.3382344.
18

Preprint
[42] Andrea Grisafi and Michele Ceriotti. Incorporating long-range physics in atomic-scale machine
learning.The Journal of Chemical Physics, 151(20):204105, November 2019. ISSN 0021-9606.
doi: 10.1063/1.5128375. URL https://pubs.aip.org/aip/jcp/article/151/20/204105/1
97247/Incorporating-long-range-physics-in-atomic-scale.
[43] Moritz Gubler, Jonas A. Finkler, Moritz R. Schäfer, Jörg Behler, and Stefan Goedecker.
Accelerating Fourth-Generation Machine Learning Potentials Using Quasi-Linear Scaling
Particle Mesh Charge Equilibration.Journal of Chemical Theory and Computation, 20
(16):7264–7271, August 2024. ISSN 1549-9618. doi: 10.1021/acs.jctc.4c00334. URL
https://doi.org/10.1021/acs.jctc.4c00334.
[44] Nail A. Gumerov and Ramani Duraiswami.Fast Multipole Methods for the Helmholtz Equation
in Three Dimensions. Elsevier, 2005. ISBN 9780080443713.
[45] Nail A. Gumerov and Ramani Duraiswami. Fast multipole method for the biharmonic
equation in three dimensions.Journal of Computational Physics, 215(1):363–383, 2006. doi:
10.1016/j.jcp.2005.10.029.
[46] Zhiyue Guo, Junjie Wang, Haoting Zhang, Zhixin Liang, Ziyang Yang, Yujian Pan, and Jian
Sun. Differentiable particle-mesh Ewald with Cartesian tensor message passing for learning
long-range electrostatics and dipole response.arXiv preprint arXiv:2606.01598, June 2026.
URLhttps://arxiv.org/abs/2606.01598.
[47] W. Hackbusch. A Sparse Matrix Arithmetic Based onH-Matrices. Part I: Introduction toH-
Matrices.Computing, 62(2):89–108, April 1999. ISSN 1436-5057. doi: 10.1007/s006070050015.
URLhttps://doi.org/10.1007/s006070050015.
[48] Jiaqi Han, Wenbing Huang, Tingyang Xu, and Yu Rong. Equivariant Graph Hierarchy-Based
Neural Networks. InAdvances in Neural Information Processing Systems, volume 35, pp. 9176–
9187, December 2022. doi: 10.52202/068431-0667. URLhttp://arxiv.org/abs/2202.10643.
[49] R. W. Hockney and J. W. Eastwood.Computer Simulation Using Particles. Taylor & Francis,
1988. ISBN 978-0-85274-392-8. doi: 10.1201/9781439822050.
[50] Kevin K. Huguenin-Dumittan, Philip Loche, Ni Haoran, and Michele Ceriotti. Physics-Inspired
Equivariant Descriptors of Nonbonded Interactions.The Journal of Physical Chemistry
Letters, 14(43):9612–9618, November 2023. doi: 10.1021/acs.jpclett.3c02375. URLhttps:
//doi.org/10.1021/acs.jpclett.3c02375.
[51] Truong Son Hy and Risi Kondor. Multiresolution equivariant graph variational autoencoder.
Machine Learning: Science and Technology, 4(1):015031, March 2023. ISSN 2632-2153. doi:
10.1088/2632-2153/acc0d8. URLhttps://dx.doi.org/10.1088/2632-2153/acc0d8.
[52] Nicholas E Jackson, Michael A Webb, and Juan J De Pablo. Recent advances in machine
learning towards multiscale soft materials design.Current Opinion in Chemical Engineering,
23:106–114, March 2019. ISSN 22113398. doi: 10.1016/j.coche.2019.03.005. URL https:
//linkinghub.elsevier.com/retrieve/pii/S2211339819300036.
[53] Yajie Ji, Jiuyang Liang, and Zhenli Xu. Machine-Learning Interatomic Potentials for Long-
Range Systems.Physical Review Letters, 135(17):178001, October 2025. doi: 10.1103/ssp9-7s81.
URLhttps://link.aps.org/doi/10.1103/ssp9-7s81.
19

Preprint
[54] Yajie Ji, Jiuyang Liang, and Zhenli Xu. Accurate learning of long-range interatomic potentials
by coupling Cartesian atomic cluster expansion and sum-of-Gaussians neural networks.The
Journal of Chemical Physics, 164(2):024109, January 2026. doi: 10.1063/5.0303312. URL
https://doi.org/10.1063/5.0303312.
[55] Adil Kabylda, J. Thorben Frank, Sergio Suárez-Dou, Almaz Khabibrakhmanov, Leonardo
Medrano Sandonas, Oliver T. Unke, Stefan Chmiela, Klaus-Robert Müller, and Alexandre
Tkatchenko. Molecular Simulations with a Pretrained Neural Network and Universal Pairwise
Force Fields.Journal of the American Chemical Society, 147(37):33723–33734, September
2025. doi: 10.1021/jacs.5c09558. URLhttps://doi.org/10.1021/jacs.5c09558.
[56] Yanming Kang, Giang Tran, and Hans De Sterck. Fast Multipole Attention: A Scalable
Multilevel Attention Mechanism for Text and Images, October 2023. URLhttps://arxiv.
org/abs/2310.11960. arXiv:2310.11960 [cs.CL].
[57] Ehsan Rahmatizad Khajehpasha, Jonas A. Finkler, Thomas D. Kühne, and S. Alireza
Ghasemi. CENT2: Improved charge equilibration via neural network technique.Physical
Review B, 105(14):144106, April 2022. doi: 10.1103/PhysRevB.105.144106. URL https:
//link.aps.org/doi/10.1103/PhysRevB.105.144106.
[58] Dongjin Kim and Bingqing Cheng. Long-range electrostatics for machine learning interatomic
potentials is easier than we thought.The Journal of Chemical Physics, 164(6):060901, February
2026. ISSN 0021-9606. doi: 10.1063/5.0316886. URLhttps://doi.org/10.1063/5.0316886.
[59] Dongjin Kim, Xiaoyu Wang, Santiago Vargas, Peichen Zhong, Daniel S. King, Theo Jaffrelot
Inizan, and Bingqing Cheng. A universal augmentation framework for long-range electrostatics
in machine learning interatomic potentials.Journal of Chemical Theory and Computation,
21(24):12709–12724, December 2025. ISSN 1549-9618. doi: 10.1021/acs.jctc.5c01400. URL
https://pmc.ncbi.nlm.nih.gov/articles/PMC12707604/.
[60] John G. Kirkwood. The Dielectric Polarization of Polar Liquids.The Journal of Chemical
Physics, 7(10):911–919, October 1939. ISSN 0021-9606. doi: 10.1063/1.1750343. URL
https://doi.org/10.1063/1.1750343.
[61] Tsz Wai Ko, Jonas A. Finkler, Stefan Goedecker, and Jörg Behler. A fourth-generation
high-dimensional neural network potential with accurate electrostatics including non-local
charge transfer.Nature Communications, 12(1):398, January 2021. ISSN 2041-1723. doi: 10.1
038/s41467-020-20427-2. URLhttps://www.nature.com/articles/s41467-020-20427-2.
[62] Emir Kocer, Andreas Singraber, Jonas A. Finkler, Philipp Misof, Tsz Wai Ko, Christoph
Dellago, and Jörg Behler. Iterative charge equilibration for fourth-generation high-dimensional
neural network potentials.The Journal of Chemical Physics, 162(12):124106, March 2025.
ISSN 0021-9606, 1089-7690. doi: 10.1063/5.0252566. URLhttps://pubs.aip.org/jcp/art
icle/162/12/124106/3340486/Iterative-charge-equilibration-for-fourth.
[63] Risi Kondor. N-body Networks: a Covariant Hierarchical Neural Network Architecture for
Learning Atomic Potentials, March 2018. URLhttp://arxiv.org/abs/1803.01588.
[64] Arthur Kosmala, Johannes Gasteiger, Nicholas Gao, and Stephan Günnemann. Ewald-based
Long-Range Message Passing for Molecular Graphs. InProceedings of the 40th International
Conference on Machine Learning, volume 202 ofPMLR, pp. 17544–17563, July 2023. URL
http://arxiv.org/abs/2303.04791.
20

Preprint
[65] Konstantin N Kudin and Gustavo E Scuseria. A fast multipole method for periodic systems
with arbitrary unit cell geometries.Chemical Physics Letters, 283(1–2):61–68, January 1998.
ISSN 0009-2614. doi: 10.1016/S0009-2614(97)01329-8. URLhttps://www.sciencedirect.
com/science/article/pii/S0009261497013298.
[66] Thomas D. Kühne, Marcella Iannuzzi, Mauro Del Ben, Vladimir V. Rybkin, Patrick Seewald,
Frederick Stein, Teodoro Laino, Rustam Z. Khaliullin, Ole Schütt, Florian Schiffmann, et al.
CP2K: An electronic structure and molecular dynamics software package – Quickstep: Efficient
and accurate electronic structure calculations.The Journal of Chemical Physics, 152(19):
194103, 2020. doi: 10.1063/5.0007045. URLhttps://doi.org/10.1063/5.0007045.
[67] Yunyang Li, Yusong Wang, Lin Huang, Han Yang, Xinran Wei, Jia Zhang, Tong Wang,
Zun Wang, Bin Shao, and Tie-Yan Liu. Long-Short-Range Message-Passing: A Physics-
Informed Framework to Capture Non-Local Interaction for Scalable Molecular Dynamics
Simulation. InInternational Conference on Learning Representations, May 2024. URL
http://arxiv.org/abs/2304.13542.
[68] Zongyi Li, Nikola Kovachki, Kamyar Azizzadenesheli, Burigede Liu, Kaushik Bhattacharya,
Andrew Stuart, and Anima Anandkumar. Multipole Graph Neural Operator for Paramet-
ric Partial Differential Equations. InAdvances in Neural Information Processing Systems,
volume 33, pp. 6755–6766, December 2020. URLhttps://arxiv.org/abs/2006.09535v2.
[69] Jiuyang Liang, Libin Lu, Yajie Ji, and Shidong Jiang. Prolate spheroidal wave functions
enable fast and exponent-aware long-range machine learning interatomic potentials.arXiv
preprint arXiv:2606.06617, June 2026. URLhttps://arxiv.org/abs/2606.06617.
[70] Yi-Lun Liao and Tess Smidt. Equiformer: Equivariant Graph Attention Transformer for 3D
Atomistic Graphs. InInternational Conference on Learning Representations, May 2023. URL
http://arxiv.org/abs/2206.11990.
[71] Alec J. Linot, Haotian Hang, Eva Kanso, and Kunihiko Taira. Hierarchical equivariant
graph neural networks for forecasting collective motion in vortex clusters and microswimmers.
Communications Physics, 8:515, November 2025. doi: 10.1038/s42005-025-02417-2. URL
https://www.nature.com/articles/s42005-025-02417-2.
[72] Philip Loche, Kevin K. Huguenin-Dumittan, Melika Honarmand, Qianjun Xu, Egor Rumiant-
sev, Wei Bin How, Marcel F. Langer, and Michele Ceriotti. Fast and flexible long-range models
for atomistic machine learning.The Journal of Chemical Physics, 162(14):142501, April 2025.
ISSN 0021-9606. doi: 10.1063/5.0251713. URLhttps://doi.org/10.1063/5.0251713.
[73] Moin Uddin Maruf, Sungmin Kim, and Zeeshan Ahmad. Learning Long-Range Interactions
in Equivariant Machine Learning Interatomic Potentials via Electronic Degrees of Freedom.
The Journal of Physical Chemistry Letters, 16(35):9078–9087, September 2025. doi: 10.1021/
acs.jpclett.5c02352. URLhttps://doi.org/10.1021/acs.jpclett.5c02352.
[74] Albert Musaelian, Simon Batzner, Anders Johansson, Lixin Sun, Cameron J. Owen, Mordechai
Kornbluth, and Boris Kozinsky. Learning local equivariant representations for large-scale
atomistic dynamics.Nature Communications, 14(1):579, 2023. ISSN 2041-1723. doi: 10.1038/
s41467-023-36329-y. URLhttps://doi.org/10.1038/s41467-023-36329-y.
[75] Y. Muto. Force between nonpolar molecules.Nippon Sugaku-Buturigakkwaishi, 17(10-11-12):
629–631, 1943. doi: 10.11429/subutsukaishi1927.17.10-11-12_629. In Japanese.
21

Preprint
[76] Nhat Khang Ngo, Truong Son Hy, and Risi Kondor. Multiresolution Graph Transformers
and Wavelet Positional Encoding for Learning Long-Range and Hierarchical Structures.The
Journal of Chemical Physics, 159(3):034109, July 2023. ISSN 0021-9606, 1089-7690. doi:
10.1063/5.0152833. URLhttp://arxiv.org/abs/2302.08647. arXiv:2302.08647 [cs].
[77] Samuel P. Niblett, Mirza Galib, and David T. Limmer. Learning intermolecular forces at
liquid–vapor interfaces.The Journal of Chemical Physics, 155(16):164101, October 2021.
ISSN 0021-9606. doi: 10.1063/5.0067565. URLhttps://doi.org/10.1063/5.0067565.
[78] Lars Onsager. Electric Moments of Molecules in Liquids.Journal of the American Chemical
Society, 58(8):1486–1493, August 1936. ISSN 0002-7863. doi: 10.1021/ja01299a050. URL
https://doi.org/10.1021/ja01299a050.
[79] Kenta Oono and Taiji Suzuki. Graph neural networks exponentially lose expressive power
for node classification. InInternational Conference on Learning Representations, 2020. URL
https://arxiv.org/abs/1905.10947.
[80] Yoonjae Park, Dongjin Kim, Daniel S. King, Nam H. Ðào, Roya Savoj, Sebastien Hamel,
Xiaoyu Wang, and Bingqing Cheng. Polarizable atomic multipoles for learning long-range
electrostatics, September 2026. URLhttps://arxiv.org/abs/2605.05746v2. Version 2.
[81] Isaac J. Parker, Mandy J. Hoffmann, William J. Baldwin, Shuang Han, Srishti Gupta,
Kara D. Fong, Angelos Michaelides, Christoph Schran, Sandip De, and Gábor Csányi. False
Metallization in Short-Ranged Machine Learned Interatomic Potentials, March 2026. URL
http://arxiv.org/abs/2603.04228. arXiv:2603.04228 [physics].
[82] Behnam Parsaeifard, Deb Sankar De, Jonas A. Finkler, and Stefan Goedecker. Fingerprint-
Based Detection of Non-Local Effects in the Electronic Structure of a Simple Single Component
Covalent System.Condensed Matter, 6(1):9, March 2021. ISSN 2410-3896. doi: 10.3390/cond
mat6010009. URLhttps://www.mdpi.com/2410-3896/6/1/9.
[83] Thomas Plé, Louis Lagardère, and Jean-Philip Piquemal. Force-Field-Enhanced Neural
Network Interactions: from Local Equivariant Embedding to Atom-in-Molecule properties and
long-range effects.Chemical Science, 14(44):12554–12569, 2023. ISSN 2041-6520, 2041-6539.
doi: 10.1039/D3SC02581K. URL http://arxiv.org/abs/2301.08734 . arXiv:2301.08734
[physics].
[84] Thomas Plé, Olivier Adjoua, Louis Lagardère, and Jean-Philip Piquemal. FeNNol: An efficient
and flexible library for building force-field-enhanced neural network potentials.The Journal
of Chemical Physics, 161(4):042502, July 2024. doi: 10.1063/5.0217688.
[85] Thomas Plé, Olivier Adjoua, Anouar Benali, Evgeny Posenitskiy, Corentin Villot, Louis
Lagardère, and Jean-Philip Piquemal. A Foundation Model for Accurate Atomistic Simulations
in Drug Design, May 2025. URLhttps://doi.org/10.26434/chemrxiv-2025-f1hgn-v3.
[86] Jay W. Ponder, Chuanjie Wu, Pengyu Ren, Vijay S. Pande, John D. Chodera, Michael J.
Schnieders, Imran Haque, David L. Mobley, Daniel S. Lambrecht, Robert A. Jr. DiStasio,
Martin Head-Gordon, Gary N. I. Clark, Margaret E. Johnson, and Teresa Head-Gordon.
Current Status of the AMOEBA Polarizable Force Field.The Journal of Physical Chemistry
B, 114(8):2549–2564, March 2010. ISSN 1520-6106. doi: 10.1021/jp910674d. URLhttps:
//doi.org/10.1021/jp910674d.
22

Preprint
[87] Sergey Pozdnyakov and Michele Ceriotti. Smooth, exact rotational symmetrization for deep
learning on point clouds.Advances in Neural Information Processing Systems, 36:79469–79501,
December 2023. URL https://proceedings.neurips.cc/paper_files/paper/2023/hash
/fb4a7e3522363907b26a86cc5be627ac-Abstract-Conference.html.
[88] Eric Qu, Brandon M. Wood, Aditi S. Krishnapriyan, and Zachary W. Ulissi. A recipe for
scalable attention-based MLIPs: unlocking long-range accuracy with all-to-all node attention,
March 2026. URLhttp://arxiv.org/abs/2603.06567. arXiv:2603.06567 [cs].
[89] Ladislav Rampášek and Guy Wolf. Hierarchical graph neural nets can capture long-range
interactions. In2021 IEEE 31st International Workshop on Machine Learning for Signal
Processing (MLSP), pp. 1–6, October 2021. doi: 10.1109/MLSP52302.2021.9596069. URL
http://arxiv.org/abs/2107.07432.
[90] Anthony K. Rappe and William A. III Goddard. Charge equilibration for molecular dynamics
simulations.The Journal of Physical Chemistry, 95(8):3358–3363, April 1991. ISSN 0022-3654.
doi: 10.1021/j100161a070. URLhttps://doi.org/10.1021/j100161a070.
[91] Egor Rumiantsev, Marcel F. Langer, Tulga-Erdene Sodjargal, Michele Ceriotti, and Philip
Loche. Learning Long-Range Representations with Equivariant Messages.Transactions on
Machine Learning Research, January 2026. ISSN 2835-8856. URLhttps://openreview.net
/forum?id=pZI9e4SW9P.
[92] Kristof T. Schütt, Oliver T. Unke, and Michael Gastegger. Equivariant message passing
for the prediction of tensorial properties and molecular spectra. InProceedings of the 38th
International Conference on Machine Learning, volume 139 ofProceedings of Machine Learning
Research, pp. 9377–9388. PMLR, July 2021. URLhttps://proceedings.mlr.press/v139
/schutt21a.html.
[93] Yusuf Shaidu, Franco Pellegrini, Emine Küçükbenli, Ruggero Lot, and Stefano de Gironcoli.
Incorporating long-range electrostatics in neural network potentials via variational charge
equilibration from shortsighted ingredients.npj Computational Materials, 10(1):47, March
2024. ISSN 2057-3960. doi: 10.1038/s41524-024-01225-6. URL https://www.nature.com/a
rticles/s41524-024-01225-6.
[94] J. S. Smith, O. Isayev, and A. E. Roitberg. ANI-1: an extensible neural network potential with
DFT accuracy at force field computational cost.Chemical Science, 8(4):3192–3203, March
2017. ISSN 2041-6539. doi: 10.1039/C6SC05720A. URLhttps://pubs.rsc.org/en/conten
t/articlelanding/2017/sc/c6sc05720a.
[95] Àlex Solé, Sergio Suárez-Dou, Albert Mosella-Montoro, Silvia Gómez-Coca, Eliseo Ruiz,
Alexandre Tkatchenko, and Javier Ruiz-Hidalgo. Machine learning multiscale interactions,
May 2026. URLhttps://arxiv.org/abs/2605.25710.
[96] A.J. Stone. Distributed multipole analysis, or how to describe a molecular charge distribution.
Chemical Physics Letters, 83(2):233–239, October 1981. ISSN 00092614. doi: 10.1016/0009-2
614(81)85452-8. URL https://linkinghub.elsevier.com/retrieve/pii/0009261481854
528.
[97] Anthony J. Stone.The Theory of Intermolecular Forces. Oxford University Press, Oxford,
2nd edition, 2013. ISBN 978-0-19-967239-4. doi: 10.1093/acprof:oso/9780199672394.001.0001.
URLhttps://academic.oup.com/book/9446.
23

Preprint
[98] Jens Stücker and Oskar Foldal. JZ-FMM: GPU-native differentiable N-body simulations with
the Fast Multipole Method, September 2026. URLhttps://arxiv.org/abs/2609.09307.
[99] Daria Sushnikova, Pavel Kharyuk, and Ivan Oseledets. FMM-Net: neural network architecture
based on the Fast Multipole Method, December 2022. URLhttp://arxiv.org/abs/2212.1
2899. arXiv:2212.12899 [math].
[100] K. T. Tang and J. Peter Toennies. An improved simple model for the van der Waals potential
based on universal damping functions for the dispersion coefficients.The Journal of Chemical
Physics, 80(8):3726–3741, April 1984. ISSN 0021-9606. doi: 10.1063/1.447150. URL
https://doi.org/10.1063/1.447150.
[101] Nathaniel Thomas, Tess Smidt, Steven Kearnes, Lusann Yang, Li Li, Kai Kohlhoff, and
Patrick Riley. Tensor field networks: Rotation- and translation-equivariant neural networks
for 3D point clouds, May 2018. URLhttp://arxiv.org/abs/1802.08219. arXiv:1802.08219
[cs].
[102] Aidan P. Thompson, H. Metin Aktulga, Richard Berger, Dan S. Bolintineanu, W. Michael
Brown, Paul S. Crozier, Pieter J. in ’t Veld, Axel Kohlmeyer, Stan G. Moore, Trung Dac
Nguyen, Ray Shan, Mark J. Stevens, Julien Tranchida, Christian Trott, and Steven J. Plimpton.
LAMMPS – a flexible simulation tool for particle-based materials modeling at the atomic,
meso, and continuum scales.Computer Physics Communications, 271:108171, February 2022.
doi: 10.1016/j.cpc.2021.108171. URLhttps://doi.org/10.1016/j.cpc.2021.108171.
[103] Moritz Thürlemann and Sereina Riniker. Anisotropic Message Passing: Graph Neural Networks
with Directional and Long-Range Interactions. InInternational Conference on Learning
Representations, 2023. URLhttps://openreview.net/forum?id=socffUzSIlx.
[104] Moritz Thürlemann, Lennard Böselt, and Sereina Riniker. Learning atomic multipoles:
Prediction of the electrostatic potential with equivariant graph neural networks.Journal of
Chemical Theory and Computation, 18(3):1701–1710, February 2022. doi: 10.1021/acs.jctc.1c0
1021.
[105] Alexandre Tkatchenko, Robert A. DiStasio, Roberto Car, and Matthias Scheffler. Accurate
and Efficient Method for Many-Body van der Waals Interactions.Physical Review Letters,
108(23):236402, June 2012. doi: 10.1103/PhysRevLett.108.236402. URLhttps://link.aps
.org/doi/10.1103/PhysRevLett.108.236402.
[106] Nguyen Thien Phuc Tu, Nazanin Rezajooei, Erin R. Johnson, and Christopher N. Rowley. A
neural network potential with rigorous treatment of long-range dispersion.Digital Discovery,
2(3):718–727, 2023. doi: 10.1039/D2DD00150K. URLhttps://pubs.rsc.org/en/content/
articlelanding/2023/dd/d2dd00150k.
[107] Nguyen Thien Phuc Tu, Siri Williamson, Erin R. Johnson, and Christopher N. Rowley.
Modeling Intermolecular Interactions with Exchange-Hole Dipole Moment Dispersion Cor-
rections to Neural Network Potentials.The Journal of Physical Chemistry B, 128(35):
8290–8302, September 2024. ISSN 1520-6106. doi: 10.1021/acs.jpcb.4c02882. URL
https://doi.org/10.1021/acs.jpcb.4c02882.
[108] Oliver T. Unke and Markus Meuwly. PhysNet: A neural network for predicting energies,
forces, dipole moments, and partial charges.Journal of Chemical Theory and Computation,
15(6):3678–3693, June 2019. doi: 10.1021/acs.jctc.9b00181.
24

Preprint
[109] Oliver T. Unke, Stefan Chmiela, Michael Gastegger, Kristof T. Schütt, Huziel E. Sauceda,
and Klaus-Robert Müller. SpookyNet: Learning force fields with electronic degrees of freedom
and nonlocal effects.Nature Communications, 12(1):7273, December 2021. ISSN 2041-1723.
doi: 10.1038/s41467-021-27504-0. URL https://www.nature.com/articles/s41467-021-2
7504-0.
[110] Oliver T. Unke, Stefan Chmiela, Huziel E. Sauceda, Michael Gastegger, Igor Poltavsky,
Kristof T. Schütt, Alexandre Tkatchenko, and Klaus-Robert Müller. Machine Learning
Force Fields.Chemical Reviews, 121(16):10142–10186, August 2021. ISSN 0009-2665. doi:
10.1021/acs.chemrev.0c01111. URLhttps://doi.org/10.1021/acs.chemrev.0c01111.
[111] Joost VandeVondele and Jürg Hutter. Gaussian basis sets for accurate calculations on molecular
systems in gas and condensed phases.The Journal of Chemical Physics, 127(11):114105, 2007.
doi: 10.1063/1.2770708. URLhttps://doi.org/10.1063/1.2770708.
[112] Martin Vondrák, Karsten Reuter, and Johannes T. Margraf. Pushing charge equilibration-
based machine learning potentials to their limits.npj Computational Materials, 11(1):288,
September 2025. ISSN 2057-3960. doi: 10.1038/s41524-025-01791-3. URLhttps://www.na
ture.com/articles/s41524-025-01791-3.
[113] Chu Wang, Lin Huang, Xinran Wei, Tao Qin, Arthur Jiang, Lixue Cheng, and Jia Zhang.
Scalable machine learning force fields for macromolecular systems through long-range aware
message passing, January 2026. URLhttps://arxiv.org/abs/2601.03774.
[114] Tong Wang, Xinheng He, Mingyu Li, Yatao Li, Ran Bi, Yusong Wang, Chaoran Cheng,
Xiangzhen Shen, Jiawei Meng, He Zhang, Haiguang Liu, Zun Wang, Shaoning Li, Bin Shao, and
Tie-Yan Liu. Ab initio characterization of protein molecular dynamics with AI2BMD.Nature,
635(8040):1019–1027, November 2024. ISSN 1476-4687. doi: 10.1038/s41586-024-08127-z.
URLhttps://doi.org/10.1038/s41586-024-08127-z.
[115] Yusong Wang, Chaoran Cheng, Shaoning Li, Yuxuan Ren, Bin Shao, Ge Liu, Pheng-Ann Heng,
and Nanning Zheng. Neural P3M: A Long-Range Interaction Modeling Enhancer for Geometric
GNNs. InAdvances in Neural Information Processing Systems, volume 37, pp. 120336–120365,
December 2024. doi: 10.52202/079017-3824. URLhttp://arxiv.org/abs/2409.17622.
[116] Yusong Wang, Tong Wang, Shaoning Li, Xinheng He, Mingyu Li, Zun Wang, Nanning
Zheng, Bin Shao, and Tie-Yan Liu. Enhancing geometric representations for molecules with
equivariant vector-scalar interactive message passing.Nature Communications, 15(1):313,
2024. ISSN 2041-1723. doi: 10.1038/s41467-023-43720-2. URLhttps://doi.org/10.1038/
s41467-023-43720-2.
[117] M.S. Warren and J.K. Salmon. Astrophysical N-body simulations using hierarchical tree
data structures. InSupercomputing ’92:Proceedings of the 1992 ACM/IEEE Conference on
Supercomputing, pp. 570–576, November 1992. doi: 10.1109/SUPERC.1992.236647. URL
https://ieeexplore.ieee.org/document/236647.
[118] Miriam Winkelmann, Edoardo Di Napoli, Daniel Wortmann, and Stefan Blügel. Solution to
the modified helmholtz equation for arbitrary periodic charge densities.Frontiers in Physics,
8:618142, 2021. doi: 10.3389/fphy.2020.618142.
25

Preprint
[119] Brandon M. Wood, Misko Dzamba, Xiang Fu, Meng Gao, Muhammed Shuaibi, Luis Barroso-
Luque, Kareem Abdelmaqsoud, Vahe Gharakhanyan, John R. Kitchin, Daniel S. Levine,
Kyle Michel, Anuroop Sriram, Taco Cohen, Abhishek Das, Ammar Rizvi, Sushree Jagriti
Sahoo, Zachary W. Ulissi, and C. Lawrence Zitnick. UMA: A Family of Universal Models for
Atoms. InAdvances in Neural Information Processing Systems, volume 38, pp. 129391–129427,
December 2025. doi: 10.52202/085713-4310. URLhttp://arxiv.org/abs/2506.23971.
[120] Junjie Xu, Jiahao Zhang, Mangal Prakash, Xiang Zhang, and Suhang Wang. DualEquiNet:
A Dual-Space Hierarchical Equivariant Network for Large Biomolecules, June 2025. URL
http://arxiv.org/abs/2506.19862. arXiv:2506.19862 [q-bio].
[121] Kun Yao, John E. Herr, David W. Toth, Ryker Mckintyre, and John Parkhill. The TensorMol-
0.1 model chemistry: a neural network augmented with long-range physics.Chemical Science,
9(8):2261–2269, February 2018. ISSN 2041-6539. doi: 10.1039/C7SC04934J. URLhttps:
//pubs.rsc.org/en/content/articlelanding/2018/sc/c7sc04934j.
[122] Lexing Ying, George Biros, and Denis Zorin. A kernel-independent adaptive fast multipole
algorithm in two and three dimensions.Journal of Computational Physics, 196(2):591–626,
May 2004. ISSN 0021-9991. doi: 10.1016/j.jcp.2003.11.021. URLhttps://doi.org/10.101
6/j.jcp.2003.11.021.
[123] Rex Ying, Jiaxuan You, Christopher Morris, Xiang Ren, William L. Hamilton, and Jure
Leskovec. Hierarchical Graph Representation Learning with Differentiable Pooling. In
Advances in Neural Information Processing Systems, volume 31, December 2018. URL
http://arxiv.org/abs/1806.08804.
[124] Hongyu Yu, Liangliang Hong, Shiyou Chen, Xingao Gong, and Hongjun Xiang. Capturing
long-range interaction with reciprocal space neural network, November 2022. URLhttp:
//arxiv.org/abs/2211.16684. arXiv:2211.16684 [cond-mat].
[125] Shuwen Yue, Maria Carolina Muniz, Marcos F. Calegari Andrade, Linfeng Zhang, Roberto
Car, and Athanassios Z. Panagiotopoulos. When do short-range atomistic machine-learning
models fall short?The Journal of Chemical Physics, 154(3):034111, January 2021. ISSN
0021-9606. doi: 10.1063/5.0031215. URLhttps://doi.org/10.1063/5.0031215.
[126] Linfeng Zhang, Han Wang, Maria Carolina Muniz, Athanassios Z. Panagiotopoulos, Roberto
Car, and Weinan E. A deep potential model with long-range electrostatic interactions.The
Journal of Chemical Physics, 156(12):124107, March 2022. doi: 10.1063/5.0083669. URL
https://doi.org/10.1063/5.0083669.
[127] Lingfeng Zhang, Taoyong Cui, Dongzhan Zhou, Lei Bai, Sufei Zhang, Luca Rossi, Mao
Su, Wanli Ouyang, and Pheng-Ann Heng. An SO(3)-equivariant reciprocal-space neural
potential for long-range interactions, March 2026. URLhttp://arxiv.org/abs/2603.18389.
arXiv:2603.18389 [physics].
[128] Yingkai Zhang and Weitao Yang. Comment on “Generalized gradient approximation made
simple”.Physical Review Letters, 80(4):890, 1998. doi: 10.1103/PhysRevLett.80.890. URL
https://doi.org/10.1103/PhysRevLett.80.890.
[129] Maksim Zhdanov, Max Welling, and Jan-Willem van de Meent. Erwin: A Tree-based
Hierarchical Transformer for Large-scale Physical Systems. InProceedings of the 42nd
26

Preprint
International Conference on Machine Learning, volume 267 ofPMLR, pp. 78023–78040, July
2025. URLhttp://arxiv.org/abs/2502.17019.
[130] Huan-Xiang Zhou and Xiaodong Pang. Electrostatic Interactions in Protein Structure, Folding,
Binding, and Condensation.Chemical Reviews, 118(4):1691–1741, February 2018. ISSN 0009-
2665. doi: 10.1021/acs.chemrev.7b00305. URL https://pubs.acs.org/doi/10.1021/acs.c
hemrev.7b00305.
[131] Roman Zubatyuk, Justin S. Smith, Jerzy Leszczynski, and Olexandr Isayev. Accurate and
transferable multitask prediction of chemical properties with an atoms-in-molecules neural
network.Science Advances, 5(8):eaav6490, August 2019. doi: 10.1126/sciadv.aav6490.
27

Preprint
A Scalar FMM
A.1 Kernel and expansion equivariance
LetR∈SO(3)be a rotation andr ′ i =Rr i +b. Fors̸=t,
G(r′ t,r′ s) = 1 ∥R(rt−rs)∥ =G(r t,rs), G(r t,rs) =∥r t−rs∥−1.(8)
Thus V′(r′ t) = V (rt), and reindexing the sources leaves the sum unchanged. The harmonic and
radial factors obey
Y (ℓ)(Rˆr) =D (ℓ)(R)Y (ℓ)(ˆr), R (ℓ) τ (∥Rr∥) =R (ℓ) τ (r).
In particular, with covariant centers, the scalar-source multipoles transform as
Φ′ s (ℓ) = ∑
i∈s
qi ˜R(ℓ)(R(ri−cs)) =D (ℓ)(R)Φ(ℓ) s .
Replacing ˜R(ℓ) by ˜I(ℓ) gives the same law for local coefficients. The CG identity [35] then gives
stage covariance and complete-block truncation invariance [17, 39]:
Tτ(Rr)Dτ s (R) =D τ t (R)Tτ(r), P pD(R) =D(R)P p.(9)
Here Dτ s,Dτ t act onℓτ s,ℓτ t, andPp retains complete spatial degrees0,...,p . Composition through
L2P givesV′ p(r′ t) = Vp(rt), including the direct near field. SinceY (ℓ)(−ˆr) = (−1)ℓY (ℓ)(ˆr)and
every analytical path obeys(−1)L = (−1)j+ℓ, the proof extends toR∈O (3). Throughout, centers,
memberships, interaction lists and tie handling must transform consistently with geometry and
particle reindexing. Under this condition, relative displacements ensure translation invariance and
source sums ensure permutation equivariance.
A.2 Stage operators and phase conventions
We use orthonormal complex harmonics with the Condon–Shortley phase and Racah-normalized
solid harmonics [17, 39]:
˜R(ℓ)(x) =
√
4π
2ℓ+ 1∥x∥ℓY (ℓ)(ˆx), ˜I(ℓ)(x) =
√
4π
2ℓ+ 1∥x∥−(ℓ+1)Y (ℓ)(ˆx).(10)
The source moments and target local coefficients of Section 2.2 satisfy
Φ(ℓ) s = ∑
i∈s
qi ˜R(ℓ)(ri−cs),Φ (ℓ) t = ∑
i∈far(t)
qi ˜I(ℓ)(ri−ct),
Vfar(ct +x)≈ 1 4πε0 p∑ ℓ=0 Φ(ℓ) t · ˜R(ℓ)(x),a·b= ∑ m amb⋆ m.
Here far(t)contains the transferred source particles. At the origin, ˜R(0) = 1and ˜R(ℓ>0) =0.
Transforming harmonics, coefficients and CG tensors consistently gives the real basis of the main
text, where conjugation drops.
28

Preprint
The addition theorems in this normalization are
˜R(ℓ)(a+b) =
ℓ∑
n=0
(
2ℓ
2n
)1/2[ ˜R(ℓ−n)(a)⊗ ˜R(n)(b) ](ℓ),
˜I(ℓ)(a−b) =
∞∑
ℓ′=0
(−1)ℓ+ℓ′
[
2(ℓ+ℓ ′) + 1
2ℓ+ 1
(
2(ℓ+ℓ ′)
2ℓ′
)]1/2[ ˜R(ℓ′)(a)⊗ ˜I(ℓ+ℓ′)(b) ](ℓ). (11)
The regular identity is exact; the irregular identity requires∥a∥<∥b∥ . Settinga =ri−cs and
b =ct−cs =−r gives the Laplace expansion atℓ = 0and M2L atℓ> 0, truncated to input/output
orders≤p . Regular shifts give M2M and, by transposition, L2L; L2P evaluates the local field.
Enclosures obeying(Rs +Rt)/∥ct−cs∥<1ensure convergence throughout the target region.
For input/output degreesj∈ℓ τ s,L∈ℓ τ t and channelsb,a, the weighted CG product is
[
x⊗w
⨁
ℓ
f (ℓ)
](L)
aM
=
∑
b,j,ℓ
∑
mj,m
waL,bj,ℓCLM jmj,ℓmx(j) bmjf (ℓ) m .(12)
The path sum also includes filter channels when present. Scalar-source FMM has one channel per
spatial degree. Withaℓ =
√
4π/(2ℓ+ 1), the addition theorems give
cτ Ljℓ
aℓ
=



1, τ= P2M, j= 0, ℓ=L,√(2L
2j
)
, τ= M2M, L=j+ℓ,√
2ℓ+ 1
2L+ 1
(2ℓ
2j
)
, τ= M2L, ℓ=j+L,
√ 2j+ 1
2L+ 1
(2j
2L
)
, τ= L2L, j=L+ℓ,
√2j+ 1, τ= L2P, L= 0, ℓ=j.
(13)
Other paths have zero weight. These coefficients assume Racah-normalized states, orthonormal
harmonic filters and source-minus-target displacements, including center minus particle at L2P; the
direction and CG coefficients carry the signs.
29

Preprint
B Tensor FMM
B.1 Kernel and expansion equivariance
LetQ′ s (ℓQ) =D(ℓQ)(R)Q(ℓQ) s andr′ s =Rrs +b. Invariance of pair distances gives componentwise
Coulomb equivariance directly [91]:
V (ℓQ)(rt) = 1 4πε0 ∑ s̸=t Q(ℓQ) s ∥rt−rs∥,V ′(ℓQ)(r′ t) =D (ℓQ)(R)V (ℓQ)(rt).(14)
To prove the same result for the expansions, first keep the charge and spatial indices separate. At a
centerc u, write
ˆΦ(n) u = ∑
i∈Su
Q(ℓQ) i ⊗H (n)(ri−cu),
ˆΦ′ u (n) = [ D(ℓQ)(R)⊗D (n)(R) ]ˆΦ(n) u . (15)
HereH(n) = ˜R(n) for multipoles and˜I(n) for local coefficients;Su contains the corresponding source
particles. The second line follows by transforming each factor and usingc′ u = Rcu +b. In this
equation⊗is the ordinary tensor product, before CG coupling. For the CG mapCL ℓQn [35],
Φ(L) u,n =C L ℓQnˆΦ(n) u ,Φ ′ u,n (L) =C L ℓQn(D(ℓQ)⊗D (n))ˆΦ(n) u =D (L)Φ(L) u,n,(16)
where allD matrices are evaluated atR and|ℓQ−n|≤L≤ℓ Q +n. Thus every coupled expansion
block is equivariant, with spatial ordernretained as a multiplicity label.
For a scalar stageTτ from Appendix A.2, the uncoupled tensor stage isˆTτ =IℓQ⊗T τ, with
IℓQ the identity on charge components. Equation 9 gives
ˆTτ(Rr) [ D(ℓQ)(R)⊗D τ s (R) ] = [ D(ℓQ)(R)⊗D τ t (R) ]ˆTτ(r).(17)
Unitary CG changes of basis preserve this identity. So does truncation byIℓQ⊗Pp, provided every
coupling ofℓQ with n = 0,...,p and its multiplicity is retained. L2P contracts the spatial part to
degree zero, leaving the charge degreeℓQ:
V′ p (ℓQ)(r′ t) =D (ℓQ)(R)V (ℓQ) p (rt).
For charge parityηQ, a spatial-order-n block has parityηQ(−1)n; preserving these parities extends
the proof toO(3). The hierarchy conditions of Appendix A.1 give translation and permutation
equivariance. This is tensor transport through a scalar kernel, distinct from physical multipole
interactions, which require kernel derivatives [97].
B.2 Stage operators and phase conventions
The coupled input and output degrees satisfy|ℓQ−n|≤j≤ℓ Q +n and|ℓQ−n′|≤L≤ℓ Q +n′. In
the convention of Appendix A.2, changing coupling order from((ℓQ⊗n )j⊗ℓ )L to( ℓQ⊗ (n⊗ℓ )n′)L
gives
cτ (n′,L),(n,j),ℓ =c τ n′nℓ (−1)ℓQ+n+ℓ+L
√
(2j+ 1)(2n′ + 1)
{
ℓQ n j
ℓ L n ′
}
.(18)
The braces denote a Wigner6j symbol andcτ n′nℓ is the scalar weight in Equation 13. Spatial orders
n,n′ remain multiplicity labels;ℓQ = 0recovers scalar FMM.
30

Preprint
The paired Coulomb kernel follows from two CG identities:
ℓ∑
m=−ℓ
Y⋆ ℓm(ˆa)Yℓm(ˆb) = (−1)ℓ√ 2ℓ+ 1 [ Y (ℓ)(ˆa)⊗Y (ℓ)(ˆb) ](0),(19)
and, withcℓ1 = (−1)ℓQ+ℓ1
√
(2ℓ1 + 1)/(2ℓQ + 1),
∑
ℓ1
cℓ1
[[
Q(ℓQ)⊗Y (ℓ)(ˆa) ](ℓ1)⊗Y (ℓ)(ˆb) ](ℓQ) =Q (ℓQ) ℓ∑
m=−ℓ
Y⋆ ℓm(ˆa)Yℓm(ˆb).(20)
These follow from the scalar CG coefficient and6j recoupling ofℓQ,ℓ,ℓ . The pairing weightscℓ1 are
distinct from the stage weightscτ. As for scalar FMM, a change to real harmonics must transform
the CG tensors and coefficient vectors consistently.
C Learnable NEMORA: Proofs
C.1 Learned operator equivariance
For|ℓ 1−ℓ 2|≤ℓ≤ℓ 1 +ℓ 2, the CG product of Equation 2 satisfies [35]
[
D(ℓ1)(R)f (ℓ1)⊗D (ℓ2)(R)g(ℓ2)](ℓ) =D (ℓ)(R) [ f (ℓ1)⊗g (ℓ2)](ℓ).(21)
ForO(3), output parity equals the product of input parities. In Equation 6, invariant radial weights
and channel mixing within the same degree and parity giveT′ st (ℓM) = D(ℓM)(R)T (ℓM) st for each
ungated block, ℓM ∈ ˜ℓτ t. Summation over a covariantly selected interaction list preserves this
identity. The hierarchy conditions are those of Appendix A.1. Analytical recovery setsαθ = 1,
R(ℓ) θ =1, WV =I and the weights of Appendix B.2, retaining all required blocks and M2L filters
through2p.
C.2 Invariant gates
The gated sum is
Ψ(ℓM) t = ∑
s∈Nτ (t)
α(ℓM) θ,st T (ℓM) st , α (ℓM) θ,st =ϕ θ(Gst⊕Mst⊕Ast)(ℓM).(22)
The inputs are geometric invariants, block norms, and same-irrep, same-parity alignments:
Ast =
⨁
ℓ
⟨q(ℓ) t ,k (ℓ) s ⟩,q (ℓ) t =W QΨ(ℓ) t ,k (ℓ) s =W KΨ(ℓ) s .(23)
Orthogonality ofD (ℓ)(R)gives⟨Dq,Dk⟩=⟨q,k⟩, henceα ′ θ,st =α θ,st and
Ψ′ t (ℓM) = ∑
s
α(ℓM) θ,st D(ℓM)(R)T (ℓM) st =D (ℓM)(R)Ψ(ℓM) t .
Gates are analogous to damping and polarization factors [86, 97, 100], not self-consistent polarization
equations.
31

Preprint
C.3 Invariant readout and equivariant forces
Equivariant backbone, lift, residuals, contractions, Kelvin maps and periodic correction, followed by
even-scalar atomic readouts, imply
E({Rri +b},RH) =E({r i},H),F ′ i =−R∇ riE=RF i.
The force identity holds whereverE is differentiable; omitH for nonperiodic systems. Atomic
summation preserves permutation invariance.
D Symmetric Contraction: Proofs
D.1 Kernel factorization and distributivity
On an admissible domain, assume a finite factorization and separable pair expansions:
K(ν+1)(rt,rs1,...,r sν) = ∑
a
ν∏
k=1
Kak(rt,rsk), K ak(rt,rs) =
∑
β
uβ(rt)vak,β(rs).
Here a indexes factorization rank andβ basis/channel components. Define accumulated coefficients
Aak,β =∑ svak,β(rs)and fields Fak(rt) =∑ βuβ(rt)Aak,β. For FMM,uβ is a regular solid-harmonic
component about the target center andAak,β its local coefficient. Distributivity gives
U(rt) =
∑
s1,...,sν
K(ν+1)(rt,rs1,...,r sν) = ∑
a
ν∏
k=1
Fak(rt)
=
∑
β1,...,βν
[∑
a
ν∏
k=1
Aak,βk
]
/bracehtipupleft /bracehtipdownright/bracehtipdownleft /bracehtipupright
Bβ1···βν
ν∏
k=1
uβk(rt). (24)
The basis products commute, soUB =USνB, whereSν symmetrizes theβindices. Distinct-source
terms have body orderν + 1for one-source pair factors; repeated indices contribute lower orders.
The identity is exact for the represented factorization. Exact reconstruction requires the product
basis, including radial factors, and product translation maps: harmonic fields are not closed under
multiplication. Equation 28 instead projects these products into configured equivariant feature
blocks.
D.2 Equivariance
For the coefficient-block representationD(R)and a parity-compatible generalized CG mapCℓM,
SνD(R)⊗ν =D(R)⊗νSν,C ℓMSνD(R)⊗ν =D (ℓM)(R)CℓMSν.
Thus symmetric contractions act equivariantly on expansion coefficients before evaluation [8, 25, 26].
E Global Kelvin: Proofs
E.1 Local-field construction and summation
For a support of radiusRu centered atcu, setx =rt−cu, r =∥x∥. Kelvin inversion [2] maps
irregular to regular harmonics:
(KRuf)(x) = Ru r f
(
R2 ux
r2
)
,
32

Preprint
KRu ˜I(ℓ)(x) = Ru r
(
R2 u
r
)−(ℓ+1)√ 4π
2ℓ+ 1 Y (ℓ)(ˆx) =R−(2ℓ+1) u ˜R(ℓ)(x).(25)
Write the node’s multipole and local states asΦM,u,ΦL,u. Forf (p) M =∑p ℓ=0 Φ(ℓ) M,u· ˜I(ℓ),
(KRuf (p) M )(x) =
p∑
ℓ=0
∆Φ(ℓ) L,u· ˜R(ℓ)(x),∆Φ (ℓ) L,u =R−(2ℓ+1) u Φ(ℓ) M,u.(26)
If the original sources lie within radiusa<R u, the full inverted series converges forr<R 2 u/a and
is regular at the center. For multiple supportsk, field addition means evaluation at a common
target, not coefficientwise addition across different centers:
fG(rt) =
∑
k
p∑
ℓ=0
∆Φ(ℓ) L,k· ˜R(ℓ)(rt−ck).
Each term must be evaluated within its convergence domain. The learned counterpart pools support
states by Equation 29 and broadcasts them to particles:
aG t = ∑
k
T L2P t←k (Ψk),a total t =a hier t +a G t .
The two outputs share target irreps and channel layout. This defines an additive learned response;
it does not require the feature-dependent maps to be linear or the supports to solve a common
dielectric boundary problem.
E.2 Equivariance
For an invariant support radius andR∈O(3),
R2 uRx
∥Rx∥2 =R R2 ux r2 ,K Ru(f◦R −1) = (KRuf)◦R −1.
For tensor-valued fields the component actionD(R)also commutes withKRu. In the learned map,
invariant radii, distances and gates and same-irrep channel mixing give
Ψ′ k (ℓ) =D (ℓ)(R)Ψ(ℓ) k ,a ′ t G,(ℓ) = ∑
k
D(ℓ)(R)T L2P t←k (Ψk)(ℓ) =D (ℓ)(R)aG,(ℓ) t .
Here support centers transform with the geometry, and support selection and pooling respect particle
reindexing. The L2P identity follows from Appendix C.1.
F Cluster-Local Kelvin: Proofs
F.1 Local-field addition
At hierarchy nodeu, Equation 26 supplies a regular field about the same center as the downward
expansion. In a common basis, normalization and validity domain,
Φtotal L,u =Φ L,u + ∆ΦL,u, T(Φ L,u + ∆ΦL,u) =TΦ L,u +T∆Φ L,u, T∈{L2L,L2P}.
With compatible normalized channels, the unmodulated learned self-update is
˜Ψ(ℓ) L,u =Ψ (ℓ) L,u + ˜R−(2ℓ+1) u Ψ(ℓ) M,u, ˜Ru =R u/rcut,(27)
For analytical tensor fields the Kelvin factor isR−(2n+1) u , indexed by spatial ordern, not total
coupled degree. The learned degree-diagonal map is a local-state correction, not necessarily an
exact tensor-field inversion or dielectric solution.
33

Preprint
F.2 Equivariance
Let∆Ψ (ℓ) L,u denote the learned correction. Invariant radii and gates and same-irrep channel mixing
imply
∆Ψ′ L,u (ℓ) =D (ℓ)(R)∆Ψ(ℓ) L,u, ˜Ψ′ L,u (ℓ) =D (ℓ)(R) ( Ψ(ℓ) L,u + ∆Ψ(ℓ) L,u ) .
Subsequent equivariant L2L and L2P maps preserve this identity, including when feature-dependent
gates make them nonlinear.
G Periodic Correction: Proof
G.1 Equivariance
WithH ′ =RHand consistently transformed image selection,
∥RHn∥=∥Hn∥,|det(RH)|=|detH|.
The degree-diagonal correction in Equation 30 therefore commutes withD(ℓ)(R). This establishes
equivariance, not exact periodic electrostatics.
H Linear-Time Complexity
Letnnode +nedge =O(N), leaf occupancy and interaction-list sizes be bounded, and angular degrees,
channels, radial basis size and contraction order be fixed [17]. Each node/edge operation then costs
O(1), and bounded near lists givenpair =O(N). WithKKelvin anchors,
Teval =O(n node +n edge +n pair +NK+|N lat|) =O(N), M eval =O(N),
for fixedK and image shell. The bound includes contractions and root reinjection, but not hierarchy
construction; a separation test alone does not guarantee bounded interaction lists.
34

Preprint
I Analytical Kernel Families
Forr< <r >, the Coulomb, Yukawa and outgoing Helmholtz kernels admit the separated expan-
sion [17, 44, 118]
G(∥r>−r<∥) =
∞∑
ℓ=0
Aℓuℓ(r<)vℓ(r>)
ℓ∑
m=−ℓ
Y⋆ ℓm(ˆr<)Yℓm(ˆr>).
Table 4 lists these bases and further analytical FMM families. For Yukawa,κ >0and iℓ(z) =√
π/(2z)Iℓ+1/2(z), kℓ(z) =
√
2/(πz)Kℓ+1/2(z), so k0(z) = e−z/z. The κ rescalings are a basis
convention; their product supplies the required prefactorκ. For Helmholtz,k> 0, jℓ and h(1) ℓ are
spherical Bessel and outgoing Hankel functions.
Table 4: Analytical free-space kernel families in three dimensions.The first three rows use the
separated form above; the remaining families require the indicated additional structure. Overall physical
prefactors are omitted, and tensor kernels are stated away from their singularities.
Family Kernel Analytical expansion structure
Coulomb1/r u ℓ =r ℓ,v ℓ =r−(ℓ+1),A ℓ = 4π/(2ℓ+ 1).
Yukawae −κr/r u ℓ =κ−ℓiℓ(κr),v ℓ =κ ℓ+1kℓ(κr),A ℓ = 4π.
Helmholtze ikr/r u ℓ =j ℓ(kr),v ℓ =h (1) ℓ (kr),A ℓ = 4πik[44].
Biharmonicr Regular branches rℓ,rℓ+2 and irregular branches
r−ℓ−1,r 1−ℓ, multiplied byYℓm; coupled branch trans-
lations [45].
Inverse powerr −λ,λ>0 Gegenbauer expansion with radial pairsrn <r−(n+λ) > ;
angular factors C (λ/2) n (cosγ ). Includes dispersion
powersλ= 6,8[19].
Stokes I r +rr⊤ r3 Tensor expansion obtained from harmonic and bihar- monic potentials and their derivatives; not a scalar
radial pair [40, 45].
Maxwell
(
I+ ∇∇⊤
k2
)eikr
r Dyadic expansion obtained by differentiating Helmholtz expansions, or using vector spherical
waves [40, 44].
Herecosγ= ˆr<· ˆr> and the inverse-power expansion is
∥r>−r<∥−λ =
∞∑
n=0
rn <
rn+λ > C(λ/2) n (cosγ).
Each family requires its own addition coefficients and, where applicable, radial branches or tensor
structure; replacing Coulomb radial factors alone is insufficient. These are unsmoothed free-space
expansions, not claims of implemented NEMORA variants. Only the Coulomb-based model is
benchmarked here.
35

Preprint
J Long-Range Models
Table 5:Long-range neural methods along six architectural axes.Equiv.:ℓ> 0tensorial long-range messages.
Learn.: learnable propagation parameters, excluding source construction and readout.Many-body: pairwise
(#), single-mode many-body via aggregation/path (G #), or both atom-level and coarse-level long-range coupling
( ). ℓ-mix: angular channel mixing during long-range transport.Hier.: hierarchical multi-scale structure.
Scaling: cost of the long-range component at fixed feature widths and block count; linear costs require
bounded interaction lists, leaf occupancy or graph degree. Symbols describe the long-range mechanism, not
the total body order of the complete potential.#= no,G #= partial/approximate, = yes.
Method Equiv. Learn. MBℓ-mix Hier. Scaling
Scalar long-range corrections
SpookyNet [109], TensorMol [121], AIMNet [3, 131]# # # # #O(N 2)
SO3LR [55], FENNOL [83, 84]# # # # #O(N·⟨N LR⟩)
4G–HDNNP [61], CENT/CENT2 [36, 57], CELLI [33],
FeNNix-Bio1 [85], Maruf et al. [73]
# # # # #O(NlogN) a
LES [16, 59], Neural P3M [115], Ewald MP [64], Reciprocal
Space NN [124]
# # # # #O(NlogN)
LODE [28, 42, 50]# # G # # #O(NlogN)
sGDML [18]#   # #O(N 2)
SOG-Net [53]#  # # #O(NlogN)
MLXDM [106, 107]# # # # #O(N·⟨N LR⟩)
Equivariant long-range corrections
LOREM [91] # G # # #O(NlogN)
EquiEwald [127] G # # # #O(N)
FieldMACE [6] # G # # #O(N+N env)b
MACE-POLAR-1 [11] # G # # #O(NlogN)
AMP [103] # # # #O(N 2)
LSR-MP [67]  G # # #O(N·N frag)
MFN [9]  G # G # #O(N 3)c
Hierarchical graph neural networks
DiffPool [123]#  G # #  O(N 3)d
HGNet [89]#  G # #  O(N) e
MGT [76]#  G # #  O(N 2)f
EGHN [48]  G # #  O(N) g
DualEquiNet [120]  G # #  O(N 2)h
MGVAE Hy & Kondor [51]#  G # #  O(N 3)i
Global attention
RANGE [15]#  G # # #O(N)
EFA [32]  G #  #O(N)
AllScAIP [88]G #  G # # #O(N 2)
UMA [119]G #  G # # #O(N 2)
Erwin [129]#  G # #  O(N)
FMM-inspired neural architectures
MGNO [68], FMM-Net [99]#   #  O(N)
MANO [20], FMA [56]#   #  O(N)
Neural FMM [29], CloudNFMM [30]#   #  O(N) j
NEMORA (ours)     O(N)
aAccelerated QEq [43]; dense solves areO(N 3). bGlobal embedding; per-atom embedding isO(NN env). cDense matrix-function
evaluation. dDense pooling at fixed pooling ratio.eSparse graphs. fFull attention. gSparse graphs, fixed cluster count.hDense
neighborhoods. iDense second-order variant.jLinear-size tree, sparse FMM evaluation, bounded leaf occupancy; fixed-tree
CloudNFMM local attention isO(N2).
36

Preprint
K NEMORA Operator Details
K.1 Symmetric contractions
LetΨ t =∑ s∈Ntmst be the pooled gated M2L field, withNt the M2L interaction list. ACE/MACE-
style contractions [8, 25] form degree-νproducts:
SymContractν(Ψt)∼
[(∑
s∈Nt
mst
)⊗ν]
CG
=
∑
s1,...,sν∈Nt
[
ms1t⊗···⊗m sνt
]
CG,(28)
Here[·]CG couples to the retained output irreps; learned weights and channel indices are suppressed.
At each levelL, the residual update is ˜Ψ(ℓM,L) =Ψ (ℓM,L) + [SymContractν(Ψ(L))](ℓM). Cross-
cluster terms provide features for non-additive interactions, such as dispersion and cooperative
polarization [4, 75, 105]. Disabling contractions leaves the gated M2L operator, whose inputs and
gates may still encode many-body information. Cost is linear in node count at fixed degrees, channels
and order. The factorized expansion identity and equivariance are proved in Appendix D.
K.2 Kelvin transform
For a spherical support of radiusRk centered atck, NEMORA uses a learned response inspired by
Kelvin inversion and continuum solvation [2, 14, 60, 78]:
Ψ(ℓM) k =
N∑
s=1
α(ℓM) sk · ( ˜R−(2ℓM+1) k ·R (ℓM) θ (rsk)·W V Ψ(ℓM) s ) (29)
Hereα(ℓM) sk is an invariant gate,˜Rk =Rk/rcut, andrsk =∥rs−ck∥. The radial modulationR(ℓM) θ
uses an independently parameterized polynomial encoder, andWV mixes channels within the
same irrep. Global supports pool and broadcast this response; cluster-local corrections enter the
downward local state. Field addition and equivariance are established in Appendices E and F. The
learned degree-diagonal response need not be an exact tensor Kelvin inversion. Cost isO(NK )for
Kglobal supports andO(N)for node-local updates on a linear-size hierarchy.
K.3 Periodic boundary correction
For a periodic cell of volumeV =|detH| , the learned branch pools top-level roots intoΨ(ℓM) 2
and applies a finite-shell, degree-diagonal correction motivated by periodic FMM and electrostatic
boundary terms [22, 65]:
˜Ψ(ℓM) 2 = [ (1−δ ℓM,0)S(ℓM) lat +δℓM,1 4πr3 cut 3V ] Ψ(ℓM) 2 ,S (ℓM) lat =γ pbc ∑ n∈Nlat ( rcut ∥Rn∥ )2ℓM+1 (30)
HereNlat ={n∈Z 3 :∥n∥∞≤n far}\{ 0} andRn =Hn. The deltas suppress this correction’s
monopole and add a volume-dependent dipole term, without enforcing charge neutrality. This is a
modeled root response, not an exact tinfoil lattice sum; equivariance is proved in Appendix G.1.
Cell derivatives contribute to stress. L2L reinjection isO(N)at fixed shell and truncation under
Appendix H’s hierarchy assumptions. The analytical branch instead uses the periodic operator
below.
37

Preprint
K.4 Analytical NEMORA
The analytical variant uses scalar latent charges, fixed P2M–L2P coefficients and extensive summa-
tion, without learned transport, gates, contractions or Kelvin responses. Every pair enters either
an admissible multipole interaction or direct P2P evaluation, including pairs inside the backbone
cutoff. A charge–potential contraction replaces the learned long-range update and readout; only the
short-range backbone and its energy and charge heads remain trainable.
Scalar heads on MACE features giveqi =∑ t⋆Qt⋆(h(t⋆) i ), with energy
E=E SR + 1 2 ~q⊤KBC σ ~q,(K free σ )ij =c erf(rij/(
√
2σ))
rij
(i̸=j),(31)
Here rij =∥ri−rj∥, σ = 1Å, c = 90.4756/(2π)follows LES, and the free-space diagonal is zero.
A fixed Cartesian Taylor FMM [23] evaluates the Coulomb part, with a directerfc(r/(
√
2σ))/r
subtraction. Under PBC, images with∥n∥∞≤w enter P2P/M2L; a precomputed root operator
represents the remaining lattice sum, omitting the zero reciprocal mode and matching LES’s self-
interaction convention. With identical sources, smoothing and boundary conventions, this is the LES
energy functional [16] evaluated by FMM. Reported periodic FMM runs use~qi =qi−N−1∑ jqj,
while LES controls use raw charges; exact comparisons must match this projection. Nonperiodic
runs use~qi =q i. Forces include coordinate derivatives of the charges.
Implemented tensor-source extensions predict latent dipoles (1o) and traceless quadrupoles (2e)
from equivariant features [96], using fixed kernel derivatives throughout, including P2P and periodic
terms. Zero-initialized heads recover the scalar model. Source degreeℓsource adds atomic anisotropy;
box orderp controls expansion accuracy. Translations remain analytical, unlike NEMORA’s learned
transport and many-body coupling.
38

Preprint
L Additional Experimental Results
L.1 Reporting conventions and benchmark runs
For run-level errorsx1,...,x n, we report the arithmetic mean andSEM =s/√n, wheres is the
sample standard deviation with denominatorn− 1. Energy errors are normalized per atom in each
frame before aggregation; force RMSE pools Cartesian components within each run. SEMs below
the displayed precision are written as upper bounds rather than zero.
Lowest means are bold and second-lowest underlined, retaining ties. Rankings compare means,
not statistical significance; SEMs describe between-run variability. Comparisons are within each
dataset and metric, with narrower groups identified in the captions.
All models trained here use the benchmark splits. Run counts are given in Table 7; EFA
Au2/MgO averages two runs. Per-run energy RMSE is103[ 1 M ∑M i=1((ˆEi−Ei)/Ni)2]1/2, whereM
is the number of evaluation frames,Ni the atom count and energies are in eV. These RMSEs are
averaged across runs without removing a constant energy offset.
L.2 Charge-equilibration and electrostatic references
The charge-supervised models (∗) and SpookyNet in Table 6 differ in supervision, cost and training
protocol [33, 61, 109].
Supervision.CELLI and 4G–HDNNP fit electronegativities to DFT Hirshfeld charges. SpookyNet
takes total charge and spin as inputs and fits partial charges to reference dipoles or charges, omitting
electrostatics when neither is available. Other models in the table use only energies and forces;
MACE–LES and NEMORA infer latent charges or multipoles without charge supervision. The
NaCl and Au2/MgO releases [61] include per-atom charges, but cumulene does not. For its charge-
supervised models, we computed Hirshfeld charges with ORCA 6.1.1 atωB97X-D3/def2-TZVP,
matching the dataset.
Cost and protocol.Both charge-equilibration methods use a direct constrained linear solve,
described in their papers as cubic in atom count; iterative and particle-mesh alternatives are
discussed but not benchmarked. SpookyNet uses explicit all-pairs electrostatics and standard Ewald
summation for periodic cells. Settings are in Appendix N.9. Published nonlocal charge-transfer
results (†) use splits not established to match ours, so their rankings are not controlled comparisons.
CELLI and Allegro values follow Fuchs et al.[33]; 2G–BPNN, 4G–HDNNP and SpookyNet follow
Frank et al. [32]. SpookyNet cumulene RMSEs are from Batatia et al. [9].
Results.Charge equilibration gives lower energy errors on the monopolar charge-transfer bench-
marks Na8Cl+ 8 /Na9Cl+ 8 and Au2/MgO, including with two-interaction CELLI–MACE at our back-
bone depth. Charge labels and the prescribed Coulomb functional may contribute, but differing
protocols prevent causal attribution. NEMORA has the lowest carbon-chain energy error and the
lowest or second-lowest force error on every nonlocal charge-transfer system. On all three cumulene
splits, the electrostatic reference models have higher force errors than short-range MACE (Table 6).
39

Preprint
Table 6:Charge-equilibration and explicitly electrostatic references on the cumulene and nonlocal charge-
transfer benchmarks, energy and force RMSEs, with our MACE and NEMORA runs from Table 1. Our
cumulene test and nonlocal charge-transfer validation results are means across runs.†Published nonlocal
charge-transfer results, which use study-specific splits, losses and architectures; all other values are our runs,
except the published SpookyNet cumulene values.∗Additional reference-charge supervision; SR disables
charge-equilibration electrostatics. SpookyNet also takes total charge and spin as inputs. In each row, lowest
means are bold and second-lowest underlined, separately for energy and force (ties retained), with published
results ranked together with our runs. Sources, run counts, charge-label generation and protocol details are
given in this appendix.
CELLI–
MACE
(2)†∗ Allegro†
CELLI–
Allegro†∗
CELLI–
Allegro
(JR)†∗
CELLI–
Allegro
(JR, SR)∗
2G–
BPNN†
4G–
HDNNP†∗ SpookyNet† MACE
NEMORA
(Ours)
Energy RMSE (meV/atom)
Cumulene
ID58.791— —59.431 59.588 42.815 41.892 30.800 16.898 3.203
SOD17.089— —16.853 16.798 16.733 16.768 31.400 16.709 0.744
OOD11.202— —11.133 11.116 12.070 11.317 23.400 11.9943.770
Charged
Carbon chain0.398 0.772 0.599 0.609—1.619 1.194 0.364 0.4250.175
NaCl0.0971.612 0.127 0.114 —1.692 0.481 0.135 1.600 0.412
Au2/MgO0.0692.329 0.077 0.077 —2.287 0.219 0.107 2.385 0.197
Force RMSE (meV/Å)
Cumulene
ID204.30— —208.78 212.85 221.06 210.82 162.30 85.07 26.85
SOD126.99— —135.93 145.78 174.54 161.90 116.20 102.16 47.87
OOD104.26— —115.81 123.74 126.15 127.46 87.60 72.26 57.01
Charged
Carbon chain21.45 49.18 31.00 32.31—129.50 78.00 5.80 15.001.88
NaCl3.54 47.51 6.44 5.15—57.39 32.781.0543.89 1.75
Au2/MgO7.95 123.67 12.04 12.01—153.10 66.00 5.34 110.075.26
Table 7:Numbers of runs contributing to the benchmark means and SEMs. Counts apply to energy and
force unless noted. The separate 3–64-carbon sweep uses three runs for LOREM, EFA and NEMORA and one
for the other models. NR denotes that no run count or no result is reported. Additional cumulene controls
have three-run means but no available SEM in the source summary; SpookyNet is a published reference with
no run count given there.
Model Cumulene Carbon chain NaCl Au 2/MgO
MACE 3 3 3 3
MACE–LES 3 3 3 3
MACE–RANGE 3 3 3 2
LOREM 3 3 3 3
EFA 3 3 3 2
MACE–MFN 3 3 3 NR
NEMORA 3 3 3 3
CELLI–MACE and short-range control 3 NR NR NR
CELLI–Allegro and short-range control 3 NR NR NR
4G–HDNNP and 2G–BPNN 3 NR NR NR
40

Preprint
Table 8:Additional cumulene energy and force errors. Validation and aggregate-test results are mean
± SEM. The 3–64-carbon length/angle experiment uses separately trained models; LOREM, EFA and
NEMORA have three seeds on that corpus and are quoted as mean± SEM, while MACE, MACE–LES,
MACE–RANGE and MACE–MFN have one and are point estimates. Bold and underlined entries mark the
lowest and second-lowest errors. LOREM has the lowest force error on that corpus; the lowest energy error is
the single-run MACE–MFN result.
Energy MAE (meV/atom) Force RMSE (meV/Å)
Model Validation Testn C = 3–64Validation Testn C = 3–64
MACE [8]8.915±0.153 11.833±0.432 10.373 109.71±0.75 86.41±0.30 81.19
MACE–LES [16]8.671±0.200 11.471±0.166 10.323 98.16±0.50 86.40±0.42 80.73
MACE–RANGE [15]11.445±0.822 14.184±1.013 12.977 121.53±2.90 101.66±3.18 81.97
LOREM [91]4.678±1.198 16.765±1.678 5.068±2.159 60.60±5.87 132.89±19.6823.03±0.97
EFA [32]4.890±1.789 15.912±1.267 4.083±0.734 56.61±8.80 113.03±10.81 31.07±0.87
MACE–MFN [9]1.211±0.109 0.970±0.297 0.984 22.08±1.69 14.81±0.8231.86
NEMORA1.377±0.069 1.400±0.100 1.478±0.137 57.05±7.48 48.63±1.96 36.83±3.07
L.3 Additional cumulene results
L.4 Backbone portability
Table 9 compares short-range, scalar-source and degree-two NEMORA models across backbones.
Interfaces are defined in Appendix N.8.
Table 9:Carbon-chain backbone and source-degree validation ablations. Each entry gives mean± SEM over
three runs. Energy and force RMSEs are in meV/atom and meV/Å. Bold and underlining mark the lowest
and second-lowest means across SR, scalar and degree-two NEMORA for each host and metric. Degree-two
sources are lifted for scalar and untyped hosts. See Appendix N.8 for the backbone interfaces.
Backbone Host Metric SRℓ= 0ℓ= 2
MACE [8] Native Energy0.425±0.006 0.484±0.0240.163±0.015
Force15.15±0.51 16.70±0.462.21±0.11
Scalar Energy0.623±0.006 0.889±0.0370.284±0.031
Force25.91±0.51 27.39±0.487.85±2.08
NequIP [12] Native Energy0.871±0.002 0.972±0.0090.182±0.006
Force42.38±0.15 32.16±0.12 2.85±0.18
Scalar Energy2.618±0.001 9.491±0.3200.448±0.158
Force93.43±0.13 47.21±1.23 5.97±0.92
ViSNet [116] Native Energy0.673±0.039 0.670±0.009 0.500±0.016
Force15.67±1.12 11.56±0.13 3.49±0.12
Scalar Energy2.615±0.016 7.452±0.7420.820±0.121
Force85.78±0.09 48.67±0.17 6.35±0.35
PET [87] Untyped Energy1.047±0.086 1.119±0.1280.944±0.019
Force39.58±0.46 39.82±0.5835.06±1.07
L.5 Component ablations
Tables 10 and 11 report retrained component ablations; Table 27 defines each change. Each arm is
compared with its corresponding FULL control.
Removing the hierarchy returns carbon-chain, NaCl and Au2/MgO force errors close to short-
range MACE, accounting for most of NEMORA’s improvement. On cumulene, the Kelvin branch
41

Preprint
Table 10:Complete available component-ablation validation force RMSEs (meV/Å), mean± SEM over
three runs. Each arm is retrained, and FULL is the corresponding retrained control. These controls differ
from the benchmark configurations in Table 1. A dash denotes an unavailable result. Lowest means are bold
and second-lowest underlined (ties retained).
Arm Carbon chain NaCl Cumulene Au 2/MgO
FULL2.07±0.05 1.89±0.05 57.15±6.53 8.50±0.17
NU31.93±0.08—50.31±1.22—
FMMCLASSIC1.95±0.03 2.78±0.23 68.86±3.484.86±0.10
NOKELVIN2.12±0.04 1.92±0.04 61.21±9.06 10.28±0.13
LMAX32.15±0.02— — —
M2LDECAY2.15±0.03— — —
NOLRHEAD2.18±0.06 1.86±0.02 71.15±0.98—
M2LPIN2.21±0.03 1.97±0.07 67.19±3.43 8.86±0.03
ELL32.23±0.13— — —
NU02.26±0.06 2.33±0.02 62.66±4.04 8.95±0.09
MAXLEV12.64±0.16 2.61±0.18 49.18±5.24 —
MAXLEV32.75±0.24— — —
FIXEDTREE3.21±0.09 3.56±0.22 88.37±12.24 8.58±0.06
LMAX13.52±0.33 3.36±0.40 106.03±3.31 8.71±0.27
MAXL14.27±0.54 2.51±0.09 107.21±2.56—
NOFUSE14.94±0.52 1.89±0.09 58.03±8.18—
NOHIER15.01±0.25 44.17±0.21 89.41±7.53 112.97±0.37
LAD216.86±0.50— — —
LMAX017.00±0.55 3.50±0.22 107.74±1.02—
LAD317.30±0.59— — —
MAXL017.53±0.95— — —
NOKESL2.32±0.07 2.40±0.02 64.76±5.17—
NOGATE2.39±0.18 1.88±0.0447.67±9.72—
NOVSQRT —1.83±0.05— —
TRES1 —1.99±0.06— —
NU2 —2.00±0.07— —
NOHIERPBC — — —8.65±0.13
NOKELVPBC — — —8.77±0.10
SLABMASK — — —8.83±0.36
NSHELLS2 — — —8.87±0.14
MICSPLIT — — —8.92±0.23
NOTINFOIL — — —8.92±0.25
MACE15.00±0.32 43.89±0.09 105.43±2.19 111.56±1.65
42

Preprint
Table 11:Cumulene component-ablation test force RMSEs (meV/Å), mean± SEM from the per-run
split evaluations. FULL is the three-run reference configuration. Lowest means are bold and second-lowest
underlined (ties retained).
Arm Test-ID Test-SOD Test-OOD
FIXEDTREE67.52±20.60 127.97±29.75 104.35±8.19
FMMCLASSIC39.04±2.03 151.67±15.65 106.64±2.53
FULL28.53±1.77 58.39±9.79 64.12±8.91
LMAX089.19±1.73 104.11±0.66 75.79±0.46
LMAX188.39±1.64 130.28±7.88 80.10±2.19
M2LPIN33.27±1.95 96.72±36.88 77.94±14.54
MACE86.00±0.40 102.07±0.05 71.91±0.08
MAXL189.75±2.48 107.57±1.98 81.72±1.62
MAXLEV1278.23±48.46 183.77±25.81 116.91±10.55
NOFUSE30.92±2.85 72.28±6.19 101.14±40.98
NOGATE26.45±6.1255.77±3.62 62.83±1.40
NOHIER77.23±6.64 151.20±28.10 121.50±29.02
NOKELVIN29.45±2.30 64.11±15.40 70.20±9.44
NOKESL33.18±0.3844.96±3.06 54.27±2.60
NOLRHEAD29.23±2.67 87.29±35.32 85.92±13.58
NU033.08±4.32 77.38±22.92 64.77±2.23
NU330.10±2.10 62.60±9.87 70.03±1.32
alone retains some improvement, but the hierarchy is needed for the lowest errors.
Consistent with the backbone experiments, restricting NEMORA to scalar features and operators
increases carbon-chain force error from 2.07 to 17.00 meV/Å. On NaCl, the scalar model still reaches
3.50 meV/Å, below the short-range error of 43.89 meV/Å. Cumulene is especially sensitive to
feature degree: degree-zero and degree-one variants approach the short-range error. These joint
feature/operator ablations also remove a quadrupole-dependent Kelvin head (Table 27).
Other effects are system-dependent. Removing the standalone Kelvin branch has little effect on
thetwosmallclustersystemsbutincreasesAu 2/MgOforceerrorfrom8.50to10.28meV/Å.Removing
per-box Kelvin contributions increases NaCl error from 1.89 to 2.40 meV/Å. FMMCLASSIC pins
radial functions and removes many-body contraction and alignment gates while retaining learned
source and energy readouts. It improves Au2/MgO force error to 4.86 meV/Å but worsens cumulene
test errors, suggesting that simpler transport suffices for some predominantly electrostatic systems
while cumulene benefits from more flexible operators.
Several smaller effects are comparable to between-run variation, particularly on cumulene.
MAXLEV1 also illustrates differing validation and test behavior: its validation error is lower, but
its ID test error is substantially higher.
L.6 Ionic systems
We use equimolar binary systems with truncated Lennard-Jones interactions and fixed reference
charges±0.6e: spherical clusters labeled by direct Coulomb summation and periodic cells labeled
by Ewald/PPPM [27, 49]. These are separate benchmarks from the small NaCl clusters of Table 1.
Training and validation containN = 256, 512, 1024; N = 2048, 4096test size extrapolation. Model
settings are given in Appendix N.7.6.
Scalar-source analytical NEMORA matches LES closely in energy and force accuracy and
extrapolates to larger systems under both boundary conditions (Table 12). Force errors remain
43

Preprint
Table 12:Periodic and non-periodic ionic test errors, E RMSE (meV/atom)/F RMSE (meV/Å). Training
includes systems withN = 256, 512, 1024, while OOD denotes larger systems not included in training.
(qCl,q Na)are the mean latent source charges. Within each system size and error metric, the lower mean is
bold and the higher underlined.
System MACE–LES NEMORA (ℓ Q = 0)
Non-periodic clusters
N= 2565.042/16.81 5.266/16.60
N= 5120.496/16.93 0.532/16.71
N= 10244.538/16.82 4.836/16.60
N= 2048(OOD)8.000/16.76 8.477/16.56
N= 4096(OOD)10.792/16.86 11.414/16.83
(qCl,q Na) (−0.5999,+0.5999) (−0.5999,+0.5999)
Periodic cells
N= 256 0.308 /9.80 0.284/9.64
N= 5120.203/10.01 0.211/9.83
N= 1024 0.155 /9.88 0.133/9.69
N= 2048(OOD)0.142 /9.95 0.109/9.78
N= 4096(OOD)0.120 /9.95 0.090/9.79
(qCl,q Na) (−0.6002,+0.6003) (−0.6000,+0.6000)
nearly constant across sizes; for non-periodic clusters, NEMORA has 0.2–1.3% lower force RMSE at
every size. Independently learned LES and NEMORA charges also agree with the reference charges,
±0.6in the benchmark’s reduced units. Together, these results support recovery and size transfer
of the known long-range functional and consistent learned scalar charges.
L.7 Periodic water
The revPBE-D3 corpus contains 1,366 training and 547 validation configurations with 384 or 768
atoms. Model settings are given in Appendix N.7.7.
Table 13:Periodic revPBE-D3 water test errors. Systems withN = 384and768atoms are included in the
training and testing sets. Energy error is in meV/atom and force error in meV/Å. Appendix N.7.7 gives the
numerical settings.⟨qO⟩ and⟨qH⟩ are test-set means of the latent scalar sources. Within the same system
size and error metric, lowest means are bold and second-lowest underlined (ties retained).
Model Energy RMSE Force RMSE⟨q O⟩ ⟨q H⟩
N= 384
MACE0.340 21.86— —
MACE–LES0.351 15.75 −0.1919 0.0959
NEMORA (ℓsource = 0)0.345 15.88−0.2054 0.1027
NEMORA (ℓsource = 1)0.259 13.07−0.4766 0.2383
N= 768
MACE0.499 20.09— —
MACE–LES0.459 13.31 −0.1878 0.0939
NEMORA (ℓsource = 0)0.474 13.37−0.2011 0.1006
NEMORA (ℓsource = 1)0.358 10.95−0.4755 0.2377
LES and scalar-source NEMORA both improve force accuracy over bare MACE (Table 13).
Adding atomic dipoles (ℓsource = 1) further improves energy and force errors in this single-seed
44

Preprint
experiment, at additional computational cost, and changes the mean scalar charges on O and H
reported in the table. No quadrupolar accuracy comparison is reported.
With identical source, smoothing and boundary conventions, scalar analytical NEMORA and
LES evaluate the same long-range energy functional by different numerical methods; the reported
periodic runs differ in neutrality projection (Appendix K.4). Particle-mesh LES could scale as
O(NlogN ), whereas the FMM translation chain scales asO(N)under the conditions below,
motivating larger-system applications beyond direct summation.
L.8 Numerical convergence
We hold charges fixed to separate solver error from fitting error. For an admissible pair,ρ =
(Rs +Rt)/∥ct−cs∥<θ< 1. Classical multipole estimates predict geometric decay of truncation
error withp at fixed separation; a smallerθ tightens admissibility at the expense of additional direct
work [17, 39]. Table 14 tests both controls in float64 on 96 uniformly sampled points in[−9, 9]3
with centered Gaussian charges, exercising all five translation stages. Increasingp reduces energy
and force errors, while tighteningθ reduces force error. Atθ = 0.4, every pair is routed to P2P,
recovering direct summation to roundoff. The partition audit finds no missing or multiply counted
pairs.
Table 14:Fixed-charge numerical errors. In the free-space Coulomb test, ϵE =|E−E ref|/|Eref| and
ϵF,∞ = ∥F−F ref∥∞/∥Fref∥∞ use direct summation as reference. The periodic test uses one 256-ion
configuration with charges±0.6e and a converged Ewald reference (reciprocal-grid parameterdl = 0.6Å); its
last column is the absolute force component RMS difference in meV/Å. Herew is the explicit image-shell
radius. All entries use float64 and contain no prediction error against training labels.
Free-space Coulomb,N= 96
p θM2L rowsϵ E ϵF,∞
2 0.5 43.01×10 −4 1.89×10 −4
4 0.5 41.28×10 −5 1.01×10 −5
6 0.5 45.66×10 −7 1.09×10 −6
4 0.6 108.95×10 −6 2.38×10 −5
4 0.4 02.56×10 −16 3.87×10 −16
Periodic smoothed Coulomb,N= 256
p θ w ϵ E Force RMS difference
3 0.50 18.77×10 −4 2.427
3 0.50 24.22×10 −5 2.369
3 0.35 11.09×10 −3 1.016
3 0.35 21.60×10 −4 0.531
4 0.35 28.04×10 −5 0.101
5 0.35 23.86×10 −5 0.031
For periodic ions atp = 3,w = 2, tighteningθ from 0.5 to 0.35 reduces force error by a factor of
4.46, while direct interaction rows increase from 312,989 to 915,502. Individual energy errors need
not decrease monotonically because signed contributions can cancel. The observed trends agree with
classical FMM convergence; they do not establish error bounds for NEMORA’s learned operators.
Tree geometry also affects finite-order error: on a 384-atom water configuration with fixed charges
qH = 0.2, qO =−0.4, thep = 3,θ = 0.35,w = 2evaluator with maximum leaf occupancy 32 has
relative energy error3.03× 10−6 and force error 0.057 meV/Å against converged Ewald. Occupancy
8 and the fixed-depth training tree give 0.345 and 0.168 meV/Å, respectively. High-order force-loss
45

Preprint
derivatives require float64 in the current implementation. The reference smoothing correction
enumerates all within-graph pairs, so these accuracy tests do not establish linear runtime for the
complete analytical backend.
At fixed expansion order and bounded interaction lists, the analytical FMM translation chain
hasO(N)cost. Linear scaling, higher-degree tensor sources and learnable extensions motivate its
use on larger systems.
L.9 Water NVE energy conservation
The NVE tests use the scalar NEMORA model (ℓQ = 0) of Table 3, velocity-Verlet integration
and deuterium masses for hydrogen. The 200 ps, 512-molecule trace in Figure 3(c) follows 10 ps of
NVT equilibration at 300 K and uses the same trained checkpoint at expansion order five. Relative
to the NVT simulations in that figure, changing the expansion order changes only the numerical
approximation, without retraining. The order-three timestep scan starts 128 water molecules from
the same equilibrated state and runs for 10 ps at each timestep from 0.25 to 2 fs, rebuilding the
hierarchy at every step. The RMS total-energy fluctuation about a linear fit (Figure 5) scales
approximately as∆t2 between 0.5 and 2 fs, with log–log slope 2.06, consistent with a second-order
symplectic integrator. At 0.25 fs it approaches a fitted floor of about2× 10−3 meV/atom, consistent
with single-precision round-off.
0.25 0.5 1 2 4
Δt (fs)
10−2
10−1
⟨ΔE2 tot⟩1/2 (meV/atom)
∝ Δt2
NEMORA
Figure 5:Root-mean-square total-energy fluctuation in 10 ps NVE trajectories of 128 water molecules with
scalar NEMORA (ℓQ = 0) as a function of the velocity-Verlet timestep∆t. The dashed line is proportional
to∆t 2.
L.10 Elongated-water molecular dynamics and dipole correlations
The MACE, MACE–LES and NEMORA simulations in Figure 3 use the models of Table 3 and
the shared backbone in Appendix N.7.7. Each starts from the same equilibrated configuration of
2048 water molecules (6144 atoms) in a24.84× 24.84× 99.35Å orthorhombic periodic cell. We use
NVT Langevin dynamics at 300 K, a 0.5 fs timestep, deuterium masses for hydrogen and a 50 fs
frame-saving interval.
Molecular dipolesµi are computed from Wannier-centroid positions predicted by the Deep
Wannier model of the DPLR framework, trained on maximally localized Wannier centers of revPBE-
D3 water [126], with point charges+6on O,+1on H and −8on the centroid. For wavevectors
46

Preprint
along the long axis,k=k ˆzwithk= 2πn/L z andn= 1,2,...up tok= 10Å −1, we compute
gL(k) =⟨|ˆmz(k)|2⟩ N⟨µ 2⟩ ,ˆm z(k) = N∑ i=1 µi,zeikzi,(32)
where zi is the oxygen coordinate andN the number of molecules. The elongated cell gives a
smallest wavevector of0.063Å−1. We discard the first 5 ps and average over frames separated by
100 fs, giving more than 2000 frames per model. Ask→ 0, gL(k)approaches a finite value set
by the static dielectric constant [16]; a model without long-range electrostatics instead shows a
spurious rise.
L.11 Scaling protocol and complete measurements
We benchmark fixed-density randomized particle clusters and cubic periodic boxes using the settings
in Appendix N.10, on one H200 with untrained models in full fp32 (TF32 disabled for every model).
Timing is the median wall time of one energy evaluation with coordinate differentiation for forces,
taken over 60 interleaved evaluations in a fresh process for each size. Memory is the peak device
memory of one such evaluation with a single structure resident: the XLA buffer assignment of the
compiled program (arguments, temporaries and outputs) for the JAX models, and the allocator peak
reset before the call for the PyTorch models. Dataset preparation and compilation are excluded
from timing and memory calculations.
Long-range exponents are log–log fits over the largest four sizes after subtracting the matched
short-range cost: the same program with the long-range module disabled for the JAX models,
the virtual-node blocks bypassed for RANGE, and a plain MACE of the same backbone for LES.
Time uses the device kernel-busy difference and memory the difference of peaks. This reduces
framework-specific fixed overhead in the fitted slopes but does not make absolute timings or memory
statistics directly comparable across frameworks.
Table 15:Energy-and-force wall time (ms) for non-periodic clusters on one H200.αLR is the fitted scaling
exponent of the long-range cost. A dash marks a size that exceeded the GPU memory.
NMACE LES RANGE EFA LOREM MFN NEMORA
640.716.4 21.81.0 2.2 124.7 4.3
1280.818.3 24.41.5 2.5 635.4 4.7
2561.020.5 27.42.2 2.8 4601.6 6.2
5121.320.8 27.83.9 4.0 35133.5 6.9
10241.821.0 28.3 6.75.8 – 8.7
20482.823.5 31.6 12.7 13.2 –11.9
40965.642.3 46.0 31.4 44.0 –19.3
819210.898.8 78.0 68.2 162.1 –37.5
1638421.4277.9 143.7 138.2 702.4 –75.5
3276843.1891.5 277.9 281.7 2971.6 –162.6
6553685.1– 547.2 – 13533.2 –334.5
131072172.6– 1099.6 – – –606.9
262144 345.8 – – – – – 1238.6
αLR – 1.99 0.99 1.02 2.21 2.77 0.96
47

Preprint
Table 16:Energy-and-force wall time (ms) for periodic boundaries on one H200.αLR is the fitted scaling
exponent of the long-range cost. A dash marks a size that exceeded the GPU memory.
NMACE LES RANGE EFA LOREM MFN NEMORA
640.8 17.2 26.00.72.2 120.7 5.3
1280.919.1 27.91.0 2.7 636.4 5.6
2561.021.3 29.91.3 3.4 4615.0 7.3
5121.421.6 29.31.9 6.1 35150.2 8.3
10241.921.9 28.72.6 11.1 – 9.3
20483.123.7 31.94.6 31.1 – 13.4
40966.042.5 47.68.8 110.0 – 20.5
819211.589.5 80.120.1 363.4 – 37.6
1638422.2233.9 146.140.9 – – 80.3
3276844.8– 281.588.7 – – 167.2
6553689.0– 554.3191.4 – – 340.8
131072177.0– 1106.4399.4 – – 662.1
262144352.2– –816.5 – – 1329.8
αLR – 1.88 0.98 0.98 1.92 2.78 1.00
Table 17:Peak GPU memory (MiB) for non-periodic clusters on one H200. αLR is the fitted scaling
exponent of the long-range cost. A dash marks a size that exceeded the GPU memory.
NMACE LES RANGE EFA LOREM MFN NEMORA
6443.699.3 110 62.7 57.1 178054.5
12861.2134 154 87.7 98.9 681080.2
25685.9181 215123 171 26900 127
512153303 372 221 328 107000212
1024273508 643 398 629 –369
20485111130 1220602 1300 – 738
409611302990 2390 7000 2760 –1540
819223609060 4740 14000 5720 –3470
16384462030600 9480 27700 12400 –6440
327689150111000 19100 55500 27800 –13000
6553618200– 38100 – 64600 –25400
13107238700– 77300 – – –52100
262144 78000 – – – – – 106000
αLR – 2.12 0.99 1.00 2.01 2.01 0.94
48

Preprint
Table 18:Peak GPU memory (MiB) for periodic boundaries on one H200.αLR is the fitted scaling exponent
of the long-range cost. A dash marks a size that exceeded the GPU memory.
NMACE LES RANGE EFA LOREM MFN NEMORA
6452101 11552.4 88.8 1780 64.4
12874.7 138 16173.6139 6820 90.8
256107 187 225103217 26900 154
512186 359 388168506 107000 271
1024322 688 6692731180 – 440
2048591 1820 12704714600 – 858
40961260 5670 246075217500 – 1730
81922550 19700 4910147066600 – 3580
163844700 72800 97502970– – 6830
327689610 – 196006000– – 14000
6553619500 – 3920012000– – 27200
13107238300 – 7830024000– – 51800
26214479100 – –47900– – 107000
αLR – 2.10 1.00 0.87 2.39 2.01 0.89
Table 19:Largest number of atomsN that fits on one H200 with fp32 precision for each model, in non-
periodic clusters and periodic boxes. Note that LOREM and EFA use a different short-range architecture
and therefore are not directly comparable.
Model Non-periodic Periodic
MACE 508,552 496,256
LES 37,096 23,128
RANGE 233,400 233,552
EFA 43,960 618,112
LOREM≈115,000 11,520
MFN 512 512
NEMORA 347,512 330,096
49

Preprint
M Datasets
M.1 Cumulene
The guaranteed nonlocal cumulene benchmark [9] tests the dependence of a carbon chain’s energy
on the relative angle of its terminal CH2 groups. For Table 1, 200 training and 50 validation
configurations use chain lengthsnC∈{ 3,..., 10, 13, 14}, with Gaussian perturbations of optimized
geometries and rotations of the terminal groups. The 170 test configurations comprise 50 in-
distribution (ID) frames at the training lengths, 60 semi-out-of-distribution (SOD) frames at
nC∈{ 11, 12} and 60 out-of-distribution (OOD) frames atnC∈{ 15, 16}. Reference energies and
forces were computed in ORCA at theωB97X-D3/def2-TZVP level.
The length and angle sweeps in Figure 2(a,b) and thenC∈ 3–64columns of Table 8 use separately
trained models. Their dataset combines all 420 frames above with 145 additional configurations:
length sweeps atφ = 5◦ and85◦, and an angle sweep atnC = 12. These 565 frames are randomly
split into 509 training and 56 validation frames. This expanded-data protocol is separate from the
held-out ID/SOD/OOD comparison.
M.2 Charged Carbon Chain (C10H2/C10H+ 3)
The non-periodic C10H2/C10H+ 3 benchmark [61] contains neutral decapentayne and its protonated
counterpart, testing the nonlocal response to protonation. We retain the original splits of 9,017
training and 1,002 validation configurations, with roughly equal numbers of neutral and charged
structures. Table 1 reports validation errors.
M.3 NaCl Clusters (Na 8Cl+ 8, Na9Cl+ 8)
The NaCl benchmark [61] contains non-periodic Na8Cl+ 8 and Na9Cl+ 8 clusters, both with net charge
+1. Adding a neutral sodium atom changes the binding energy of a sodium ion on the opposite
side of the cluster, approximately 21 Å away. We use a stratified split of 4,500 training and 500
validation configurations. Consistent with prior work [61, 91], Table 1 reports validation errors.
M.4 Au 2/MgO
The Au2/MgO benchmark [61] consists of an Au2 dimer adsorbed on a periodic MgO(001) slab, with
or without Al dopant atoms placed deep inside the slab. Each configuration contains 110 atoms in
a9 .05× 9.05× 26.46Å cell. Although the dopants lie far from the surface, they change the charge
distribution of the slab and, with it, the preferred adsorption geometry of the dimer. We use 4,500
training and 500 validation configurations and, as for NaCl, report validation errors in Table 1.
M.5 MD22
MD22 [18] contains non-periodicab initiomolecular dynamics trajectories of seven biomolecular
and supramolecular systems, labeled at the PBE+MBD level. Table 20 gives the atom counts, split
sizes and training batch sizes; model settings are in Appendix N.7.5.
50

Preprint
Table 20:MD22 split sizes (configurations) and batch sizes for MACE, MACE–LES and NEMORA. DHA
denotes docosahexaenoic acid.
System Atoms Training Validation Test Batch size
Ac–Ala3–NHMe 42 6000 750 6000 8
DHA 56 8000 1000 8000 6
Stachyose 87 8000 1000 8000 4
AT–AT 60 3000 375 3000 6
AT–AT–CG–CG 118 2000 250 2000 2
Buckyball catcher 148 600 75 600 2
Double-walled nanotube 370 800 100 800 2
M.6 Periodic Ionic Benchmark
The ionic benchmark contains equal numbers of cations and anions with charges±0.6e. Reference
energies and forces combine a Lennard-Jones potential (ϵ = 0.1eV, σ = 3.0Å, cutoff 6 Å) with
periodic Coulomb interactions evaluated by PPPM [49] in LAMMPS [102]. Geometries are sampled
every 400 fs from charge-blind Lennard-Jones dynamics in cubic cells at fixed density, with edge
lengths from 20.5 Å (N = 256) to 51.7 Å (N = 4096). Each trajectory receives an independent
random, charge-neutral assignment, held fixed across its frames. Because charges are assigned after
geometry sampling, the corpus does not develop equilibrium ionic screening correlations. At each
training size (N = 256, 512, 1024), independent trajectories provide 500 training (50 trajectories),
200 validation (20 trajectories) and 50 test configurations (10 trajectories);N = 2048and4096
contribute 50 test configurations each. A non-periodic counterpart uses spherical clusters of the
same sizes and interactions, labeled by direct Coulomb summation, with 400 training, 100 validation
and 50 test configurations per training size.
M.7 Periodic Water
The periodic water dataset was generated in this work. It contains liquid-water configurations
in cubic periodic cells with 128 and 256 molecules (384 and 768 atoms), labeled with CP2K [66]
using revPBE [128] with D3 dispersion [41]. The Gaussian and plane-wave calculations use TZV2P
MOLOPT basis sets [111], GTH pseudopotentials [38] and a 1200 Ry plane-wave cutoff. Table 21
gives the split sizes.
Table 21:Periodic water split sizes, in configurations.
Molecules Atoms Training Validation Test
128 384 788 328 474
256 768 578 219 346
Total — 1366 547 820
51

Preprint
N Model Settings
Shared backbone and optimization settings are given first, followed by model-specific settings and
per-system overrides. MACE-based comparisons use a common short-range architecture where
specified. For LOREM and EFA, we prioritize comparable receptive fields (Tr cut), angular resolution
and maximum irrep degree, and adjust short-range channel counts to balance parameter counts;
the explicit settings below record the remaining architectural differences. LOREM, EFA and
MACE–RANGE retain their own training implementations.
N.1 MACE
The MACE-based models use the backbone in Table 22, with per-system overrides in Appendix N.7.
MACE, MACE–LES and NEMORA follow Table 23; MACE–RANGE uses its separately listed
optimizer and schedule. The ionic and water benchmarks use smaller backbones, specified below.
Reference MACE options follow v0.3.15; explicitly listed model and system settings take precedence.
Table 22:Shared parameters for short-range MACE backbone upon which all MACE-based long-range
models are built.
Hyperparameter Value
Interactions 2
ℓmax 3
Hidden irreps 128x0e + 128x1o + 128x2e
ν 3
Polynomial cutoff exponent 5
Radial basis functions 8
Precision float32 (the Au2/MgO NEMORA run: float64)
Table 23:Default optimizer settings for MACE, MACE–LES and NEMORA; per-system overrides are listed
below.
Hyperparameter Value
Optimizer Adam
Learning rate 0.01
Energy:Force weight 10:100
SWA Energy:Force weight 1000:1000
EMA decay 0.99
MACE, MACE–LES and NEMORA minimize the weighted energy–force loss
L= wE
B
B∑
n=1
(
Epred n −E ref n
Nn
)2
+ wF
3AB
B∑
n=1
Nn∑
i=1
3∑
α=1
(
F pred n,i,α−F ref n,i,α )2,(33)
where B is the number of configurations in a batch,Nn is the atom count of configurationn, and
AB =∑ nNn. Energy errors are normalized per atom before averaging over configurations; force
52

Preprint
errors are averaged over all Cartesian components in the batch. We use the loss weights in Table 23,
with overrides in Appendix N.7. These models use no stress, virial or dipole supervision. Per-system
cutoffs, batch sizes and schedules are given below.
N.2 MACE–LES
MACE–LES [16] predicts one scalar latent charge per atom using a separate readout at each MACE
layer and sums these readouts before evaluating the long-range energy. The Gaussian smoothing
width isσ = 1Å, self-interactions are removed, and periodic calculations usedl = 2Å with reciprocal
cutoff kmax = 2π/dl and the zero mode omitted. Non-periodic calculations use the corresponding
real-space pair sum. The implementation’s energy normalization factor is 90.4756; the long-range
energy is added after backbone scaling, with the short-range atomic interaction shift fixed to zero.
Backbone and training settings follow the corresponding benchmark below.
N.3 LOREM
Table 24:LOREM hyperparameters for the cumulene and nonlocal charge-transfer benchmark systems.
Hyperparameter Cumulene Cumulene (3-64) NaCl Carbon
Cutoff radius (Å) 3.0 3.0 3.0 3.0
ℓmax,lr 2 2 2 2
ℓmax 6 6 6 6
Feature channels 128 128 128 128
Message-passing layers 1 1 1 1
Radial basis functions 8 8 8 8
Spherical features 8 8 8 8
Optimizer Adam Adam Adam Adam
Learning rate10 −3 10−3 10−3 10−3
Schedule linear decay linear decay linear decay linear decay
Minimum learning rate10 −6 10−6 10−6 10−6
Max epochs 4000 2000 1200 1200
53

Preprint
N.4 EFA
Table 25:EFA hyperparameters for the cumulene and nonlocal charge-transfer benchmark systems. The
EPE maximum frequency isπfor non-periodic systems andπ/4for periodic systems.
Hyperparameter Cumulene Cumulene (3-64) NaCl Carbon
Cutoff radius (Å) 2.0 2.0 3.0 2.0
Feature channels 144 144 256 144
Message-passing layers 3 3 2 3
MP maximum degree 3 3 3 3
MP radial basis functions 32 32 32 32
ERA maximum degree 2 2 2 2
ERA maximum length (Å) 19.0 86.777 25.0 19.0
ERA query/key channels 32 32 32 32
ERA value channels 64 64 64 64
Lebedev points 50 50 50 50
Optimizer Adam Adam Adam Adam
Learning rate10 −3 10−3 10−3 10−3
Schedule exp decay exp decay exp decay exp decay
Final learning rate10 −5 10−5 10−5 10−5
Loss weights (E/F) 0.01 / 0.99 0.01 / 0.99 0.01 / 0.99 0.01 / 0.99
Max epochs 200000 50000 10000 200000
N.5 MACE–RANGE
MACE–RANGE uses the short-range backbone of Table 22 with a 3 Å cutoff. It is trained with a
separate implementation, so its optimizer and schedule differ from the other MACE-based models
(Table 26). Instead of SWA, the loss weights are switched once during training.
Table 26:MACE–RANGE module and training hyperparameters for the cumulene and nonlocal charge-
transfer benchmark systems. Backbone settings follow Table 22.
Hyperparameter Cumulene Cumulene (3-64) NaCl Carbon
Virtual nodes 4 3 3 3
Virtual hidden channels 432 432 432 432
Virtual basis dimension 10 10 10 10
Virtual heads 8 8 8 8
Optimizer AdamW AdamW AdamW AdamW
Learning rate10 −3 10−3 10−3 10−3
Weight decay5×10 −7 5×10 −7 5×10 −7 5×10 −7
Scheduler CustomStepLR CustomStepLR CustomStepLR CustomStepLR
Scheduler steps 300, 200, 100 300, 200, 100 608, 192, 160 608, 192, 160
Scheduler gammas 0.8, 0.8, 0.8 0.8, 0.8, 0.8 0.8, 0.8, 0.8 0.8, 0.8, 0.8
Max epochs 2000 2000 600 600
Loss-weight switch epoch 400 500 300 300
Batch size 64 16 16 32
54

Preprint
N.6 NEMORA
All learnable NEMORA models attach after the first MACE product block (index−2) and use
operators up to degreeℓ = 2. They use a single Kelvin anchor and apply one Highway-gated
Neumann iteration with cumulant modulationγcum = 0.5unless stated otherwise. The tree is built
with the adaptive octree of Section 4.5. The backbone and NEMORA parameters form separate
optimizer groups; the NEMORA group uses a linear warmup of 2000 steps and a tensor-product
weight decay of10−4. Per-system irreps, contraction orders, learning rates and tree settings are
given in Appendix N.7.
N.7 Per-System Settings
Within each benchmark, MACE, MACE–LES and NEMORA share the backbone, data splits and
training schedule unless stated otherwise. Defaults follow Tables 22 and 23 and Appendix N.6; the
settings below take precedence. Loss weights are written as energy:force. Ionic-system and water
settings are given in Appendices N.7.6 and N.7.7.
N.7.1 Cumulene
Backbone and training.The backbone has two interaction layers, hidden irreps128× 0e + 128×
1o + 128× 2e, ℓmax = 3, correlation orderν = 3and a 3 Å cutoff. Training uses Adam (AMSGrad)
with an initial learning rate of10−2, a batch size of 16 and loss weights of1:100; the SWA stage uses
a learning rate of10−3 and weights of100:10. The main benchmark trains for 2000 epochs with
SWA from epoch 1000, and the 3–64 sweep model for 1000 epochs with SWA from epoch 500. The
MACE and MACE–LES baselines of the 3–64 sweep instead use weights of10:100and1000:1000.
NEMORA.Both cumulene models use the same configuration, with hidden irreps32 × 0e +
32× 1o + 32× 2e, maximum degreeℓ = 2and ν = 3. NEMORA parameters are trained with a
learning rate of10−3. The tree targets three children per node and has two levels, withθMAC = 0.5.
Aggregation is extensive throughout the hierarchy, and the energy readout adds a bilinear long-range
energy head.
N.7.2 Charged Carbon Chain
Backbone and training.The backbone matches cumulene, with a 3 Å cutoff. Models train for
600 epochs with a batch size of 32, loss weights of10:100, and SWA from epoch 300 with weights of
1000:1000.
NEMORA.NEMORA uses hidden irreps32 × 0e + 32× 1o + 32× 2e, ℓ = 2, ν = 2and the
trainer’s default NEMORA learning rate of10−3. The tree targets four children per node and has
two levels, withθMAC = 0.5. Upward moments are extensive and the fusion uses a density mean.
N.7.3 NaCl Clusters
Backbone and training.The backbone matches cumulene, with a 3 Å cutoff. Models train for
600 epochs with a batch size of 16, loss weights of10:100, and SWA from epoch 300 with weights of
1000:1000.
55

Preprint
NEMORA.NEMORA uses hidden irreps40 × 0e + 40× 1o + 40× 2e,ℓ = 2, ν = 3and a learning
rate of10−3. The tree targets eight children per node, has two levels and at most four atoms per
leaf, withθ MAC = 0.5. The downward pass uses two resolvent iterations.
N.7.4 Au 2/MgO
Backbone and training.The backbone matches cumulene, with a 3 Å cutoff. Models train for
600 epochs with a batch size of 2, loss weights of10:100, and SWA from epoch 300 with weights of
1000:1000. The MACE SWA stage uses weights of100:100.
NEMORA.NEMORA is trained in float64, with hidden irreps32× 0e + 32× 1o + 32× 2e, ℓ = 2,
ν = 2and a learning rate of10−3. The tree targets eight children per node, has three levels and at
most four atoms per leaf, withθMAC = 0.6. The periodic slab uses Madelung lattice sums in both
the hierarchy, with two image shells, and the Kelvin branch.
N.7.5 MD22
We train MACE, MACE–LES and NEMORA on all seven non-periodic MD22 systems [18]. Within
each system, the three models use the same data splits, MACE backbone, batch size and training
schedule (Table 20). Each result averages three independently trained models, evaluated on the
held-out test split at the checkpoint with the lowest validation force RMSE within the SWA stage.
Seeds are 42, 43 and 44, except for AT–AT–CG–CG: MACE–LES uses 42, 44 and 45, and NEMORA
uses 43, 44 and 45.
Additional baselines and evaluation.MACE–RANGE, LOREM and EFA are evaluated on
the same held-out splits with seeds 42, 43 and 44, using their original implementations, trained
on the 400-epoch protocol of Table 20. LOREM uses the checkpoint with the lowest validation
force RMSE, MACE–RANGE uses the final checkpoint after 400 epochs, and EFA uses its retained
validation-selected checkpoint. The LOREM nanotube seed-43 recovery uses element-wise gradient
clipping at 1.0 and is scored at its best-validation checkpoint. Energy RMSE equally weights
per-frame errors after division by atom count; force RMSE equally weights Cartesian components.
Atomic reference energies are restored without fitting a test-set offset.
EFA evaluation passes checkpoint parameters as dynamic JIT arguments, as in native training
and validation, while retaining the same energy model, automatic-differentiation force calculation
and NPZ batching. Inputs and parameters remain float32; matrix products use highest FP32
precision and GPU operations are deterministic. Each full test split is evaluated in two independent
GPU processes, with identical predictions in all 21 runs. Before scoring, CPU/GPU parity passed on
all 750 Ala3 validation frames, and independent-process validation repeats passed for Ala3 and the
nanotube. The acceptance tolerances are10−4 eV/Å for forces and eight float32 ULPs for energies.
CPU/GPU parity was not separately checked for every test checkpoint, and the compiler-internal
cause of the earlier closed-parameter discrepancy remains unverified.
Shared backbone and training.All three models use a MACE backbone with two interaction
layers, hidden irreps128× 0e + 128× 1o + 128× 2e, edge spherical harmonics up toℓmax = 3,
correlation orderν = 3and a 4 Å cutoff. Models are trained for 400 epochs with Adam (AMSGrad)
at an initial learning rate of10−2 and energy:force loss weights of10:100. Validation is evaluated
every two epochs; before SWA, the plateau scheduler is stepped each epoch using the latest validation
loss, with reduction factor 0.8 and patience 50. EMA decay is 0.99 and backbone weight decay
56

Preprint
is5 × 10−7. SWA starts at epoch 200 with a learning rate of10−3 and loss weights of1000:1000.
Atomic reference energies, force-RMS scaling and average neighbor counts are estimated from
training data; the LES interaction shift is fixed to zero.
NEMORA and the adaptive tree.NEMORA is attached after the first MACE product block,
with hidden irreps32× 0e + 32× 1o + 32× 2e, maximum operator degreeℓ = 2and contraction
order ν = 2. Its parameters are trained with a learning rate of10−3. The radial network uses eight
basis functions and one hidden layer of width 64 followed by its output layer; the invariant gate also
has width 64. The tree is built adaptively in the PCA frame, targeting four children per node, with
at most 16 atoms per leaf and up to eight children per node; its depth adapts to each geometry
rather than being fixed. Far-field interactions useθMAC = 0.5, and a single global Kelvin anchor is
used. Aggregation exponents areαup = 0andα down = 1.
N.7.6 Ionic systems
Within each corpus, analytical NEMORA and LES share the backbone, data splits, optimizer, and
trainingschedule. Theionicbackbonehastwointeractions, a4.5Åcutoff, and64 ×0e+64×1o+64×2e
hidden irreps. Training runs in float32 for 240 epochs with a batch size of 4, an initial learning rate
of10−2 and energy:force loss weights of10:100, with stochastic weight averaging (SWA) starting
at epoch 120 with weights of1000:1000. The periodic dipole arm instead uses a batch size of 2
and float64 for the long-range calculation; its backbone remains float32. The analytical controls
are single-seed runs, while the periodic MACE baseline is a three-seed mean, and checkpoints are
selected by validation force error. The analytical expansion order isp = 3, withθ = 0.35for clusters
and θ = 0.35, w = 2for periodic interaction lists. The periodic LES controls use reciprocal-grid
parameter dl = 2.0Å. The tree is occupancy-adaptive, with at most 16 atoms per leaf and up to six
levels.
N.7.7 Periodic water
MACE, MACE–LES and each analytical model share one backbone: one MACE interaction, a 6 Å
cutoff and128× 0e + 128× 1ohidden irreps, trained for 800 epochs with an initial learning rate of
10−2 and loss weights of10:100, and SWA starting at epoch 400 with weights of1000:1000. Both
source-degree arms use per-size batches of four 384-atom or two 768-atom frames. The analytical
settings arep = 3, θ = 0.35for periodic lists and image-shell radiusw = 2, with the long-range term
evaluated in float64. The tree has a fixed depth of two levels with a target of eight children per
node.
N.8 Backbone interfaces
For a native equivariant host, NEMORA receives the host’s typed scalar and tensor features. For
scalar-only hosts, a geometry-based lifting map combines scalar features with relative-position
angular information to construct tensor sources. PET has no native irreducible-representation
decomposition, so its attachment uses an explicit lift as well. The lift preserves equivariance when
its scalar inputs are invariant; it does not impose exact equivariance on the entire PET backbone.
N.9 Charge-equilibration and electrostatic reference settings
CELLI’s charge-loss weight is 50 on the carbon chain, 10 on NaCl and 200 on Au2/MgO. SpookyNet
uses six message-passing layers against our two, SpookyNet’s carbon-chain and Au2/MgO results
57

Preprint
use a larger cutoff than its original.
N.10 Scaling benchmark settings
The MACE-based scaling models use two MACE interactions, correlation order three, a 4 Å cutoff
and128×0e+128×1ohidden irreps. Models are built with untrained weights. EFA and LOREM use
their own short-range architectures (two message-passing rounds and a 4 Å cutoff); their long-range
blocks are kept as in the accuracy benchmarks.
58

Preprint
N.11 Component ablation settings
Table 27:Definitions of the component-ablation arms. All arms are retrained. Joint changes are identified
explicitly.
Arm Change relative to FULL
NOHIER Remove the hierarchy, retaining the standalone Kelvin branch. Periodic root
injection is also removed.
NOKELVIN Remove the standalone Kelvin branch.
NOKESL Remove the per-box Kelvin contribution to the downward pass.
FIXEDTREE Replace adaptive coarsening by a fixed top-down octree.
MAXLEV1/3 Set maximum hierarchy depth to one or three.
LMAX0/1/3 Set source-feature and operator degree together. On cumulene, degrees below
two also disable the quadrupole-dependent Kelvin head.
MAXL0/1 Reduce only the source-feature degree, retaining degree-two operators.
ELL3 Increase only the operator degree to three.
NU0/2/3 Change the many-body contraction order; zero removes the contraction.
M2LPIN Pin the radial shape to(1 +u 2)−(ℓ+1)/2, retaining a learned gain.
M2LDECAY Learn the radial decay exponent.
NOVSQRT Remove V-list square-root normalization.
TRES1 Reduce the resolvent truncation order from two to one.
NOFUSE Remove the additive long-range feature update.
NOLRHEAD Remove the separate long-range energy head.
NOGATE Remove the multipole alignment gate.
LAD2/3 Remove many-body contraction and use scalar degree; LAD3 also removes
the Kelvin branch.
FMMCLASSIC Remove contraction, Kelvin branch, alignment gate and three normalization
modes, and pin the radial shape. Learned source/readout maps remain.
NOHIERPBC Remove periodic root injection.
NOKELVPBC Remove the Kelvin periodic image sum.
NOTINFOIL Remove the surface-dipole correction.
NSHELLS2 Increase the periodic image-shell radius from one to two.
SLABMASK Mask replica images along the slab vacuum direction.
MICSPLIT Use a minimum-image near/far split with two image shells.
59
