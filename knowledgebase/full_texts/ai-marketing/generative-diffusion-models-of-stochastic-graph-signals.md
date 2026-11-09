---
title: Generative Diffusion Models of Stochastic Graph Signals
url: https://arxiv.org/abs/2607.06833
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Yiğit Berkay Uslu
- Samar Hadou
- Sergio Rozada
- Shirin Saeedi Bidokhti
- Alejandro Ribeiro
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.06833
pages: 17
chars: 90325
fetched_at: '2026-11-08T13:28:18+00:00'
kb_version: 1
---

# Generative Diffusion Models of Stochastic Graph Signals

Generative Diffusion Models of Stochastic
Graph Signals
Yi˘git Berkay Uslu, Samar Hadou, Sergio Rozada, Shirin Saeedi BidokhtiMember, IEEE,
Alejandro Ribeiro,Fellow, IEEE
Abstract—Sampling stochastic signals supported on a graph
underlies many graph machine learning tasks, including recom-
mender systems, forecasting in financial markets, and wireless
network optimization. In these settings, the target signals are
realizations of unknown conditional distributions. However, pre-
vailing approaches rely mostly on intricate, application-tailored
designs that often regress to a conditional mean instead of
sampling from the conditional law. This paper unifies such
problems as conditional graph signal generative modeling and
tackles them with a single denoising diffusion framework. We
learn a reverse diffusion process, parametrized by graph neural
networks (GNNs), that draws graph signals conditioned directly
on the graph topology and on node-feature side information.
The reverse process is realized by a novel architecture, the U-
Graph Neural Network (U-GNN), which generalizes the image-
convolutional U-Net to graph-structured signals. The U-GNN
performs multi-resolution encoder–decoder processing in which
pooling and unpooling reduce to a learned node selection,
expressed by nested selection matrices, and a zero-padded lifting
of coarse signals back to the full node set. The graph convolutions
are carried out on the original graph, with a stride that sets their
hop reach, so the U-GNN bypasses explicit graph coarsening at
every resolution. We demonstrate our method on two generative
tasks: stock price forecasting and optimal wireless resource
allocation, with extensive numerical results in both domains.
Index Terms—diffusion models, graph signals, graph neural
networks, wireless resource allocation, financial forecasting
I. INTRODUCTION
Signals defined over irregular, graph-structured domains are
pervasive, spanning application areas such as recommender
systems [3]–[5], wireless communications [6]–[11], and fore-
casting in financial markets [12]–[14]. In many such set-
tings, these signals are realizations from unknown probability
distributions rather than deterministic quantities [15]. This
paper proposes a generative modeling framework that learns to
sample from such graph signal distributions.Generative mod-
eling has proved effective for synthesizing graph topologies
themselves [16], [17], with molecular generation serving as a
canonical example [18]. We instead take the graph structure
as given and learn to generate node-defined signals.
A wide array of generative paradigms exists for learning
to sample from unknown distributions [19]–[21], such as
Preliminary results of this work were presented in part at the ICASSP 2026
conference [1] and appear in the preprint [2]. Y . Berkay Uslu, Samar Hadou,
Shirin S. Bidokhti and Alejandro Ribeiro are with the Dept. of Electrical and
Systems Eng., University of Pennsylvania, Philadelphia, PA 19104 USA.
Sergio Rozada is with the Department of Signal Processing and Commu-
nications, King Juan Carlos University, Madrid, Spain.
The implementation code is available at https://github.com/yigit-uslu/
graph-signal-diffusion.
variational autoencoders, generative adversarial networks, and
normalizing flows. Among them, denoising diffusion models
and their score- and flow-based variants stand out for their
sample quality, training stability, and principled conditional
inference in high dimensions [22]–[25]. While these models
differ in what the parametric model approximates and in the
sampling dynamics, they share a common structure. A fixed
forward process gradually corrupts the data into a tractable
reference prior, and a learned reverse process denoises samples
from that prior back toward the data distribution. Graph signals
have recently become a target for generative, particularly dif-
fusion, modeling in domains such as the forecasting of traffic
and financial series [1], [26]–[29], and wireless optimiza-
tion [2], [30]–[35]. However, these efforts have mostly been
application-specific, with task-tailored denoiser architectures.
Their formulations also often remain deterministic, seeking
solution distributions whose mass concentrates near an optimal
deterministic solution rather than drawing diversified samples
from the conditional law.
In this paper, we propose a general methodological frame-
work for graph signal generation. At its core, this requires
designing a diffusion model whose denoising network encodes
inductive biases tailored to the data domain. For images, the
standard denoising backbone is the U-Net with a symmetric
encoder–decoder structure and multi-resolution hierarchy [36],
[37]. The U-Net is built on convolutional neural networks
(CNNs), whose layers apply translation-equivariant filters on
the regular pixel grid. The natural counterpart for graph-
structured data is the graph neural network (GNN), whose
layers apply graph-shift-equivariant filters, thereby extending
convolutional processing to irregular domains [38]. Replacing
CNNs with GNN layers does not, on its own, suffice to
adapt the U-Net design to the denoising of graph signals.
The main obstacle is the pooling stage. In the image setting,
the pixel grid provides a regular pooling lattice that persists
after each down-sampling step, thus, feature extraction and
spatial reduction compose seamlessly. Graph data lacks such
a canonical lattice. A common workaround coarsens the graph
at each resolution through a learned pooling operator, as
in differentiable cluster-assignment pooling and top-knode-
scoring schemes [39], [40]. These methods are mainly de-
signed for graph-level tasks, such as classification. Under
arbitrary coarsening, however, the pooled signal loses a clear
interpretation as a convolutional signal on the original graph.
We take a different route in this paper. We formalize down-
and up-sampling, equivalently graph or node (un)pooling, as a
1
arXiv:2607.06833v1  [cs.LG]  7 Jul 2026

learned node (de)selectionoperation, expressed through nested
selection matrices [38]. These matrices are trained end-to-end
with the denoising network, so each resolution retains the
nodes most informative for the denoising task at hand. The
selection operator and its transpose play two complementary
roles. First, the nested hierarchy of selections instantiates
the multi-resolution encoder–decoder cascade. Each encoder
selection picks a smaller active node subset that defines the
next coarser resolution, and the matching transpose in the
decoder lifts coarse signals back to the finer one. Second, at
a fixed resolution, the same operator pair keeps GNN filtering
interpretable as a convolution on the original graph. The trans-
pose zero-pads a node-reduced signal to the full vertex set, the
GNN layer filters there, and the selection returns the result to
the reduced domain. Unlike the coarsening schemes above,
filtering therefore stays convolutional on the original graph
at every resolution. We further introduce a stride parameter
that sets the hop distance of each graph shift. This mirrors
how dilated convolutions in CNNs replace fixed pooling rules,
folding down-sampling and receptive-field growth into the
convolution itself [41], [42]. On the active nodes, a larger
stride enlarges the aggregation neighborhoods and prevents the
graph filters from drawing mostly from zero-padded positions
under heavy down-sampling. This construction avoids explicit
graph coarsening and lets convolutional filtering and pooling
compose across arbitrary resolutions.
Building on this mechanism, we propose theU-Graph Neu-
ral Network (U-GNN)architecture as a graph-domain adapta-
tion of the classical U-Net. It comprises a U-shaped encoder–
decoder pipeline with skip connections, built from GNN layers
and the pooling and unpooling operators above. We then cast
graph signal generation as a conditional denoising diffusion
process and parametrize its reverse process with a U-GNN.
The generations are thereby conditioned directly on the graph
topology and on node-feature side information. Although we
focus on diffusion denoising, the U-GNN is a general-purpose
architecture for learning over graph signals. It inherits the
permutation equivariance, stability to perturbations, and cross-
topology transferability of GNNs [7], [43].
We demonstrate the framework and the U-GNN architecture
on two generative tasks. The first is stock price forecast-
ing over a correlation graph of financial indicators. Given
recent market history, we generate future price trajectories
as graph signals, capturing the market uncertainty and rare
tail events that point forecasts and statistical baselines often
miss. The second is resource allocation in wireless networks
under ergodic quality-of-service (QoS) requirements, where
optimal policies are inherently probabilistic and are realized
through time-sharing. Treating solution samples from an expert
primal–dual algorithm as graph signals on channel (interfer-
ence) graphs, we learn to sample from the expert allocation
distribution given channel and user-state information.
A brief summary of our contributions is as follows.
(C1).We develop a graph signal generative modeling ap-
proach that combines denoising diffusion models with
GNNs to sample stochastic graph signals.
(C2).We parametrize the reverse diffusion process with
a novel U-GNN architecture, whose building blocks
are GNN layers with stride and zero-padded pooling,
that generalizes image-convolutional U-Nets to graph-
structured signals.
(C3).We apply our approach to stock price forecasting and
optimal wireless resource allocation, with extensive
numerical results in both domains.
The rest of the paper is organized as follows. Section II
presents the conditional graph signal generative diffusion
framework. Section III introduces GNNs with built-in stride
and pooling. Section IV assembles the U-GNN architecture.
Section V validates the method on wireless resource allocation
and financial forecasting. Section VI concludes the paper.
II. GRAPHSIGNALGENERATIVEDIFFUSIONMODELS
Consider a weighted graphG= (V,E,W)onNnodes, with
node setV={1, . . . , N}, edge setE ⊆ V ×V, and weight map
W:E →R. A graph signal assigns features to the nodes and
is collected in a matrixX= [x 1, . . . ,xF ]∈R N×F , whose
fth columnx f ∈R N gathers thefth feature across all nodes.
We endowGwith a graph shift operator (GSO)S∈R N×N , a
sparse matrix with[S] m,n = 0wheneverm̸=nand(m, n)/∈
E. We note that this GSO definition allows the diagonal entries
to be chosen freely. The GSO encodes the graph topology, and
successive products (shifts)SXpropagate signal values along
the edges. Common GSO choices are the (weighted) adjacency
matrixAand the graph LaplacianL= diag(A1 N )−A.
We address the conditional generation of graph signals.
The target is a graph signalx 0 ∈R N on a known graph
G. The conditioning collects the topology, through the GSO
S, and auxiliary node statesu∈R N×U (side information)
into the variableξ= (S,u). Letq ξ denote the distribution of
the conditioning andq x|ξ(· |ξ)the law of the target givenξ.
These define the joint data distributionq data =q x|ξ qξ, from
which we draw pairs(x 0,ξ). We seek a parametric gener-
atorp θ⋆ (· |ξ) =p(· |ξ;θ∗)whose conditional law matches
qx|ξ(· |ξ)forqξ-almost everyξ, i.e.,
θ⋆ ∈argmin
θ
Eξ∼qξ

DKL

qx|ξ(· |ξ)
 pθ(· |ξ)  .(1)
The conditional laws are unknown in closed form. We assume
samples(x 0,ξ)∼q data are available. Therefore, we realize
the optimal generatorp θ⋆ as a conditional denoising diffusion
model, trained on a dataset{(x (i) 0 ,ξ (i))}|D| i=1 ∼q data.
A. Denoising Diffusion Models for Graph Signals
A denoising diffusion model pairs a fixed forward process
q(x1:K |x 0), which noises clean targets toward a tractable
reference prior, with a learned reverse processp θ(xk−1 |x k),
which denoises prior samples back toward the data. Condi-
tional generation requires no additional machinery. We condi-
tion the reverse process onξasp θ(xk−1 |x k;ξ), leaving the
forward process and the training objective unchanged. Fig. 1
illustrates this construction, which we detail next.
2

S u
x0 xk xk′ xK· · ·
q(x1| x0) q(xk| xk−1)
pθ(x0| x1; S, u)
· · ·
q(xk′ | xk′−1)
pθ(xk| xk+1; S, u)
· · ·
q(xK | xK−1)
pθ(xK−1| xK ; S, u)pθ(xk′ | xk′+1; S, u)
Fig. 1:A denoising diffusion model of graph signals.A forward noising processq(x k |x k−1)gradually removes structure
from the original graph signals by adding white noise, withx K ≈ N(0,I). A denoising diffusion processpθ(xk−1|xk;S,u)is
trained to reverse the forward process and generate novel graph signal samplesx 0 distributed approximately by the conditional
distributionsq data(x0 |S,u)for a given GSOSand observation values represented by another graph signalu.
Forward noising process.The forward process is a Markov
chain that adds noise to the targetx 0 overKsteps. Given
(x0,ξ)∼q 0 =q data withξheld fixed, we corruptx 0 with
white noise on an increasing schedule{β k}K k=1 (e.g., linear),
producing iterates{x k}K k=1 through the Gaussian transitions,
q(xk |x k−1) =N(x k;
p
1−β k xk−1, βkI).(2)
Since the drift is linear and the noise increments are indepen-
dent, the conditionals remain Gaussian at each stepk, i.e.,
qk(xk |x 0) =N

xk; √¯αk x0,(1−¯α k)I  ,(3)
withα k := 1−β k and¯αk := Qk m=1 αm fork= 1, . . . , K. A
standard reparametrization of (3) expressesx k as a determin-
istic map of(x 0, k)plus independent standard noise [22],
xk(x0, k,ϵ) =√¯αk x0 + √ 1−¯αk ϵ,ϵ∼ N(0,I)⊥x 0,(4)
and it permits drawing any iteratex k ∼q k(· |x0,ξ)directly,
without simulating the chain in (2). For a suitable schedule and
a large enoughK, the process drivesx 0 ∼q 0(· |ξ)toward a
Gaussian prior, withx K ∼q K ≈ N(0,I)for everyξ.
Backward (reverse) denoising process.Denoising diffusion
fixesp K(· |ξ) =qK ≈ N(0,I)and learns a reverse Markov
chain whose kernelsp θ(xk−1 |x k;ξ)approximate the time
reversal of the forward chain. Consistent with the continuous-
time limit, we model each reverse step as Gaussian transitions,
pθ(xk−1

xk;ξ) =N  xk−1;µ θ  xk, k;ξ  ,Σ θ  xk, k;ξ  .(5)
As is standard, we fix the covarianceΣ θ =σ 2 kIfor a predefined
σk tied to the scheduleβ k and learn only the meanµ θ.
Training maximizes the evidence lower bound (ELBO) on
the log-likelihoodlogp θ(·

 ξ). Under the fixed covariance
and the reparametrization (4), this is equivalent to a noise-
prediction objective. Omitting its per-step ELBO weights
matches, and often improves upon, the weighted objective in
practice [22]. We therefore minimize the following objective,
θ⋆ ∈argmin
θ
L(θ) :=E
hϵ−ϵ θ  xk(x0, k,ϵ), k;ξ 2i ,(6)
where the expectation is over(x 0,ξ)∼q data and diffusion
stepsk∼unif{1, . . . , K}.
By the reparametrization (4), the trained noise predictor
ϵθ⋆ (xk, k;ξ)yields both agraph signal denoiserand the mean
of the reverse kernel in (5),
bx0(xk, k;ξ) = xk − √1−¯αk ϵθ⋆ √¯αk ,(7)
µθ⋆ (xk, k;ξ) = 1√αk

xk − βk√1−¯αk ϵθ⋆

.(8)
Thusϵ θ⋆ and the fixedΣ θ =σ 2 kIspecify (5) completely. For
sampling, we construct a family of generally non-Markovian
reverse processes [23] that preserve the forward marginals (3),
xk−1 = √¯αk−1 bx0 + q 1−¯αk−1 −σ 2 k ϵθ⋆ +σ kw,(9)
withw∼ N(0,I). A single factorη∈[0,1]tunes the noise
scaleσ k [cf. (29)]. Each step drawsx k−1 exactly from the
reverse kernel (5) atη= 1, and smaller values yield near-
deterministic and usually faster sampling.
At inference, we initializex K ∼ N(0,I)and iterate (9) for
k=K, . . . ,1to draw samplesx0 ∼p θ⋆ (· |ξ). These samples
are distributed approximately according to the conditional data
distributionq x|ξ(· |ξ)for the given conditioningξ= (S,u),
thereby realizing the conditional generative model sought in
(1). To reduce the number of model evaluations, we run an
accelerated variant of (9) (see Appendix A).
U-Nets have been instrumental in image generative models.
Accordingly, we particularizeϵ θ to a U-Graph Neural Network
(U-GNN) that tailors U-Nets for graph signal denoising.
3

III. POOLING& STRIDE INGRAPHNEURALNETWORKS
We first review graph filters, convolutions, and a standard
GNN layer. We then propose a GNN module with built-in
pooling through selection matrices and stride, which Sec-
tion IV arranges into the U-GNN encoder–decoder pipeline.
Graph filters and convolutions.Graph filters are the building
blocks of GNNs and process input graph signals through
successive graph shifts. A single shiftSxmixes each node’s
value with those of its one-hop neighbors, andkrepeated shifts
yieldS kx, which aggregates at each node the signals within
itsk-hop neighborhood. A linear shift-invariant graph filter of
orderKis the matrix polynomialh(S) := PK k=0 hkSk with
taps (coefficients)h= [h 0, . . . , hK]. It processes an input
signalxby graph convolution,
y=h∗ S x=h(S)x=
KX
k=0
hkSkx,(10)
and produces an output graph signaly∈R N as a weighted
sum of the shifted signalsS kx.
Graph neural networks.A GNN stacks graph convolutional
layers, each composing a graph filter with a pointwise nonlin-
earity [38]. Theℓth layer of anL-layer GNN reads
Xℓ =σ ℓ Hℓ(S)X ℓ−1 =σ ℓ
 KX
k=0
Sk Xℓ−1 Θℓ,k
!
,(11)
forℓ= 1, . . . , L. Here, each scalar tap of (10) becomes a
MIMO filter bankΘ ℓ,k that maps theF ℓ−1 input features
inX ℓ−1 toF ℓ output features withinK-hop neighborhoods,
with learnable coefficientsΘ ℓ ={Θ ℓ,k}K k=0 and a pointwise
nonlinearityσ ℓ, e.g., a ReLU. Stacking these layers defines
theΘ-parametrized GNNΦ(·,S; Θ) =Φ L(·,S; ΘL)◦ · · · ◦
Φ1(·,S; Θ1), with trainable parametersΘ ={Θ ℓ}L ℓ=1. It maps
an inputX 0 :=X∈R N×F 0 to an outputX L =: Y∈R N×F L,
Y=Φ(X,S; Θ).(12)
The GNN in (12) is general-purpose but not tailored to
diffusion-based generation. Since graph convolutions already
extract features on arbitrary graphs, adapting the U-Net back-
bone additionally requires only node (un)pooling, which we
introduce next together with a stride on the graph shift.
Pooling.Consider a signalX∈R N×F onNnodes. A
sampling (selection) matrixD∈ {0,1} N ′×N withN ′ < N
retains the rows ofI N indexed by a sampling setΩ⊆ V
with|Ω|=N ′.1 We learnΩ, and henceD, end-to-end, so
it is input-dependent rather than fixed (Section IV-B). We
callρ≥1withN ′ =⌊N/ρ⌋thedown-sampling (pooling)
factorthat sets the resolution reduction. By construction,D
has orthonormal rows,DD ⊤ =I N ′, andD ⊤Dis a diagonal
mask with ones onΩ. The forward mapZ=DX∈R N ′×F
down-samplesX. Its adjointD ⊤Zup-samples back toN
nodes byzero-padding, i.e., it restores the active entries on
Ωand inserts zeros on the inactive nodesV \Ω.
1We presentDas binary for exposition. We relax it to a soft selection mask
during training and binarize it to pickN ′ nodes at inference (Appendix C).
Agraph convolutional layer with poolingprocesses a down-
sampled signalZ ℓ−1 ∈R N ′×Fℓ−1 intoZ ℓ ∈R N ′×Fℓ,
Zℓ =Dσ ℓ
 KX
k=0
Sk D⊤Zℓ−1 Θℓ,k
!
.(13)
We call (13) alift–filter–reducelayer. We liftZ ℓ−1 to the
full vertex set by zero-padding throughD ⊤, filter onS, and
reduce the result back to the active set throughD. Because
the inactive nodes are zero, each active node aggregates only
the active values in its neighborhood onS, which can be few
under heavy pooling and motivates the stride introduced next.
Stride.Modern CNNs, and U-Net variants in particular, often
replace fixed pooling rules such as max- or sum-pooling with
strided or dilated convolutions for learned down-sampling and
receptive-field growth, e.g., [37], [42]. A dilated convolution
spaces its taps by a fixed step, so each tap reads from a
point several positions away rather than from an immediate
neighbor. On a graph, the natural spacing is the hop count.
Thus, we introduce a stride (dilation) parameterγ∈Z + and
replace the unit shiftSwith theγ-hop shiftS γ. The order-K
filter then aggregates from the dilated hops{0, γ,2γ, . . . , Kγ}
rather than the consecutive hops{0,1, . . . , K}. This yields the
strided graph convolutional layer with pooling,
Zℓ =Φ ℓ(Zℓ−1,S γ; Θℓ,D) =Dσ ℓ
 KX
k=0
(Sγ)k D⊤Zℓ−1 Θℓ,k
!
,
(14)
which recovers the plain layer (11) whenD=I N (ρ= 1) and
γ= 1. The pooling factorρand strideγserve complementary
roles. ThroughD, the factorρsets how many nodes survive
and hence the sparsity of the zero-padded signal. ThroughS γ,
the strideγsets how far each tap reaches [cf. Remark 1].
The strided GNN layer (14) keeps the lift–filter–reduce form
of (13), filtering onS γ instead ofS. The computations remain
on the original vertex set, andSis reused at every resolution
without explicitly formingS γ in our implementation. Instead,
we filter throughγKsuccessive unit shifts and tap the signal
everyγhops. Thus, each layer reduces to sparse matrix–vector
products, which we realize with the sparse routines of thePyG
library. We refer to Appendix B for details.
Reduced GSOs.The strided layer (14) also admits an equiva-
lent form that operates directly on theN ′-dimensional signals.
PushingDandD ⊤ through the sum defines thek-hopreduced
graph shift operators (GSOs),
S(k) :=D(S γ)k D⊤ ∈R N ′×N ′ ,(15)
whose one-hop instanceS (1) is the support of a coarse
subgraph onΩ. The family{S (k)}K k=0 then processes the low-
dimensional signals directly,
Zℓ =σ ℓ
 KX
k=0
S(k) Zℓ−1 Θℓ,k
!
.(16)
The two forms are equal because row selection commutes
with the pointwise nonlinearity,Dσ ℓ(M) =σ ℓ(DM), and
they differ only in the domain of computation. The reduced
4

form avoids computation on the inactive nodes but is ill-
suited to our setting. The reduced GSOs do not compose, i.e.,
S(m+n) ̸=S (m)S(n), sinceD ⊤D̸=I N in general. Therefore,
eachS (k) must be formed separately rather than by powering
S(1). Moreover,Dis input-dependent, so the family{S (k)}
is rebuilt on every forward pass, negating any gains from pre-
computing. We therefore adopt the lift–filter–reduce form.
GNNs with pooling and stride.StackingLstrided
graph convolutional layers with pooling [cf. (14)] defines
the(Θ,D)-parametrized GNN moduleΦ(·,S; Θ,D) =
ΦL(·,S γ; ΘL,D)◦ · · · ◦Φ1(·,S γ; Θ1,D). It maps an input
Z0 :=X∈R N ′×F0 to an outputZ L =: Y∈R N ′×FL,
Y=Φ(X,S; Θ,D),(17)
with parametersΘ ={Θ ℓ}L ℓ=1 andD∈ {0,1} N ′×N . This
GNN module is the main processing unit of each block in the
U-GNN architecture, which is introduced next.
Remark 1.In both views, the strideγoffsets the sparsity
introduced by down-sampling withD. Under lift–filter–reduce,
a stride such asγ=⌊ √ρ⌋keeps nodes from aggregating pre-
dominantly zeros. Under the reduced GSO, projecting through
Dmay isolate nodes in the induced subgraph, andS γ with
γ >1restores connectivity. A suitable value depends on the
average connectivity and the uniformity ofD.
Remark 2.A variant of(16)instead learns a genuine polyno-
mial filter in the one-hop reduced GSOS (1) =D S γ D⊤, the
principal submatrix ofS γ onΩ. This is no longer equivalent
to(14), since sampling and filtering commute only at first
order. PoweringS (1) confines every hop toΩ, whereas the
familyS (k) allows walks to traverse inactive nodes.
IV. U-GRAPHNEURALNETWORKS
The GNN in (17) processes graph signals at a single node
resolution fixed by the sampling matrixD. To build the
multi-resolution encoder–decoder hierarchy of a U-Net on
top of this module, we first define the resolutions through
depth-dependent selection matrices{C b}B b=1, whereC b ∈
{0,1} Nb×Nb−1 selectsN b nodes from theN b−1 nodes active
at the preceding depth, withN 0 =NandN=N 1 ≥N 2 ≥
· · · ≥NB. We form the composite (nested) sampling matrices,
Db :=
bY
j=1
Cj =C b · · ·C1 ∈ {0,1}Nb×N ,(18)
which relate the depth-bnodes to the fullN-node domain and
induce a nested hierarchy of sampling setsΩ B ⊆ · · · ⊆Ω1 ⊆
V. We setD 1 =C 1 =I N by convention, so the first depth
operates at full resolution. Here,C b andD b carry theper-
levelandcumulativedown-sampling factorsρ b :=N b−1/Nb
(ρ1 = 1) and¯ρb := Qb i=1 ρi =N/N b, respectively.
We call the resulting architecture aU-Graph Neural Net-
work (U-GNN). It spansBresolution levelsN=N 1 ≥ · · · ≥
NB, withB−1encoder–decoder block pairs and a bottleneck
block at the coarsest resolutionN B.
We present the U-GNN in two stages. We first fix a pure
encoder–decoder cascade whose blocks are single encoding,
decoding, and bottleneck GNN modules [cf. (17)], writtenΦ E b ,
ΦD b , orΦ B B with weightsΘ E b ,Θ D b , andΘ B B, respectively, along
with the signal flow among them in (19)–(21). These equations
include the skip connections, take the selection matricesC b as
given, and omit the node-state and diffusion-step embeddings.
We then complete the blocks with projection (fusion) layers
and, on the encoder side, node-selection heads (Sections IV-A
and IV-B). These only enlarge the block interiors and parame-
ter sets, leaving the composition here unchanged. The U-GNN
overview in Fig. 2 and the complementary block interface
details in Fig. 7 (deferred to Appendix E due to limited space)
may be consulted throughout this section.
The encoder blocks form anencoding pathΦ E =Φ E B−1 ◦
· · · ◦ΦE 1, and the decoder blocks adecoding pathΦ D =
ΦD 1 ◦ · · · ◦ΦD B−1. The encoding path extracts graph convolu-
tional features at progressively coarser resolutions, while the
decoding path reverses this progression by restoring resolution
and reintroducing fine details through skip connections.
We describe each path in turn, starting from the input
featuresZ 0. Each encoder block maps its input to an encoded
signalZ b ∈R Nb×Fb,
Zb =Φ E b  CbZb−1,S; Θ E b ,D b  ,(19)
forb= 1, . . . , B−1, whereCb down-samples the depth-(b−1)
feature onto theN b nodes processed at depthb. At the top
level,C 1 =I N andΦ E 1 operates at full resolutionN 1 =N.
Each decoder block receives the coarser decoded signal
Yb+1 ∈R Nb+1×Fb+1 from depthb+ 1, up-samples it onto
theN b-node support throughC ⊤ b+1, and combines it with the
matched encoder featureZ b through a skip connection,
Yb =Φ D b  C⊤ b+1Yb+1;Z b  ,S; Θ D b ,D b  ,(20)
forb=B−1, . . . ,1, where[·;·]denotes the skip combina-
tion. The decoded signalY b then passes to the next decoder
block or to the read-out layer atb= 1.
The two paths connect at depthBthrough the bottleneck
block, which acts as aBth encoder block,
YB =Φ B B  CBZB−1,S; Θ B B,D B  .(21)
The bottleneck outputY B enters the decoding path (20) at
depthb=B−1, and the final decoder outputY 1 ∈R N×F 0 is
mapped by a read-out layer to the model target, i.e., the noise
predictionϵ θ here. We note that all blocks share the same
S, and a depth-dependent strideγ b is implicit in the notation
[cf. (14)]. Appendix B specifies howγ b is set and how each
block evaluates its strided convolutions on the sharedS.
A. Input Processing and Block-Level Conditioning
The U-GNN realizes the denoiserϵ θ(xk, k;ξ)with con-
ditioningξ= (S,u). It incorporates the conditioning along
two routes. The graph enters as the shared shift operatorSof
every GNN module [cf. Section III], while the node statesu
enter as side information, embedded and fused into each block
5

ϵθ(xk, k; S, u)
D1=I
×
D2
×
D3
×
D4
nested sampling
Db = ∏ j≤b Cj
Ψ1
TopK
Ψ2
TopK
Ψ3
TopK
ΦE 1
Π1
ΦD 1
Π1
ΦE 2
Π2
ΦD 2
Π2
ΦE 3
Π3
ΦD 3
Π3
ΦBΠ4
↓
↓
↓
↑
↑
↑
xk Π0
S
k Πstep 0
u Πcond 0
∥
Πout ϵθ
Z0
→ all Φb
Z1
C2Z1
Z2
C3Z2
Z3
C4Z3
Y4
C⊤ 4 Y4
Y3
C⊤ 3 Y3
Y2
C⊤ 2 Y2
Y1
skip Z1
skip Z2
skip Z3
C2
C⊤ 2
C3
C⊤ 3
C4
C⊤ 4
Z1
Z2
Z3
K0
U0
[U0; K0] (× Db) to every Π b, Ψb Encoder
Decoder
Encoder
Decoder
Encoder
Decoder
q(xk | x0) ˆx0 ∝ xk − √1 − ¯αk ϵθ
↓ C2 ↑ C⊤ 2
↓ C3 ↑ C⊤ 3
↓ C4 ↑ C⊤ 4
Down-sampling (encoding) path Up-sampling (decoding) path
Depth 1 Depth 1
Depth 2 Depth 2
Depth 3 Depth 3
Depth 4 Depth 4
Clean x0
= xk (Noisy)
Est. ˆx0
= ϵθ
Fig. 1b. U-GNN denoiser ( B=4 depths, incl. bottleneck) as a vertical encoder–decoder U. Each block stacks its per-block pro-
jection Πb (fuse with Db[U0; K0]) on the GNN Φb. Selectors Ψb produce Cb+1 (reused transposed by the matched decoder up-
sampling); the left pipe nests Db = ∏ j≤b Cj. The graph shift operator S enters once and parametrises every GNN block. The
module frame ϵθ leaves the raw I/O ( k, u, xk, S, ϵθ) outside. The encoder and decoder blocks (outlined) are detailed in Fig. 2.
Side insets: one fixed grid graph, drawn at each depth. The clean x0 is noised to the network input xk (depth 1, q(xk|x0)). Down
the left (encoder), pooling ( ↓ Cb, signal-adaptive TopK) keys off the clean signal while the displayed features are a low-pass of
the noisy xk (residual noise denoises with depth); up the right (decoder) the same selections up-sample the noise estimate, whose
depth-1 output ϵθ = xk − ˆx0 recovers the clean estimate ˆx0 (top, a lightly-corrupted x0). Hollow nodes are inactive (pooled-out).
Fig. 2:U-GNN denoiser architecture.A U-GNN ofB=4depths maps the noisy graph signalx k to a noise estimateϵ θ.
At each depth, a projectionΠ b (purple) fuses the global embeddings[U 0;K 0]of node statesuand diffusion stepkinto the
signal path before a GNN moduleΦ E/D b (green), and decoder blocks additionally merge the encoder skips. Learned selectors
Ψb (orange) produce selection matricesC b+1 that down-sample the signal between depths and, transposed, up-sample it in
the decoder. The shift operatorSand the global embeddings[U 0;K 0]are shared across all blocks. Side panels trace one
fixed input graph (signal) sample through all four depths, with the encoding (down-sampling) path on the left and decoding
(up-sampling) on the right. On the left, a cleanx 0 (top-left) is corrupted into the inputx k at depth1via the forward diffusion
process [cf. (3) and (4)] and then down-sampled across depths by the selectorsC b+1 (↓). Node colors show a low-pass view
ofx k whose residual noise fades with depth, and hollow markers denote inactive nodes. On the right, the transposesC ⊤ b+1
up-sample (↑) the estimate to full resolution, yieldingϵ θ at depth1, from which the clean bx0 (top-right) is estimated via (7).
together with an embedding of the diffusion stepk. Note that
the stepkis a model input and not part of the conditioning
ξ. We now detail the embedding pipeline.
A read-in layerΠ 0 maps the noisy signalx k ∈R N to
the initial node embeddingsZ 0 ∈R N×F 0 that enter the first
encoder block. The node statesu∈R N×U and the stepkare
embedded separately into global representations shared across
all blocks. A node-wise MLPΠ U 0 (a shared per-node MLP
with no cross-node mixing) mapsuto per-node embeddings
U0 =Π U 0 (u)∈R N×F 0. A diffusion-step encoderΠ k 0, a
sinusoidal positional encoding followed by a node-wise MLP,
maps the scalarkto anF 0-dimensional vector broadcast to
all nodes asK 0 =1 N Πk 0(k)⊤ ∈R N×F 0.
At each depthb, a fusion layerΠ b merges the main signal
path with these global embeddings before the GNN mod-
ule. The block inputV b and the down-sampled embeddings
Db [U0;K 0]are each projected to a common width, merged
along the feature dimension, and mapped toF b channels,
Pb =Π b

Vb,D b [U0;K 0]

.(22)
The factorD b restricts the global embeddings to theN b nodes
active at depthb, matching the support ofV b, and the per-
input projection reconciles their differing feature (channel)
widths. The block input depends on the path. Forbth encoder
block,V b =C b Zb−1 down-samples the depth-(b−1)feature
onto theN b active nodes. Forbth decoder block, the coarser
outputY b+1 ∈R Nb+1×Fb+1 is up-sampled throughC ⊤ b+1,
concatenated with the encoder skipZ b along the feature
dimension, and mapped toF b channels by a learned skip-
projectionΠ skip b :R Fb+1+Fb →R Fb,
Vb =Π skip b  C⊤ b+1Yb+1;Z b  .(23)
The fusion layerΠ b is shared between the matched encoder
and decoder blocks, so its weights appear in bothΘ E b and
6

ΘD b , while the GNN module and skip-projection remain block-
specific. The node-state and diffusion-step embeddings enter
each block by input substitution. In (19) and (21), the module
inputC b Zb−1 is replaced by the fusedP b. In (20), the
skip combination[C ⊤ b+1Yb+1;Z b]is first mapped byΠ skip b
[cf. (23)] and then fused intoP b. The GNN modules and the
block composition remain unchanged, and only the module
inputs differ. Figure 2 shows this separation, with the fusion
drawn as the purple projectionΠ b preceding each green GNN
module, and Fig. 7 (Appendix E) details the block interface.
Finally, a read-out layerΠ out, a node-wise MLP, maps the
final decoder outputY 1 ∈R N×F 0 to the predictionϵ θ ∈R N .
B. Down-sampling (Pooling) via Learned Node Selection
The selection matricesC b and their compositionsD b de-
termine the active nodes at each depth. Rather than fixing
them in advance, we learn them end-to-end by letting each
encoder block score its own GNN output and select the active
nodes propagated to the next depth. The node-selection head
of encoder blockbderivesC b+1 from the encoded featureZ b,
forb= 1, . . . , B−1, producingC2, . . . ,CB. The top level
performs no selection sinceC 1 =D 1 =I N , and the deepest
selectionC B down-samples into the bottleneck, which itself
does not further down-sample.
We describe the selection operation using two index sys-
tems.Globalindices label nodes inV, with the active setΩ b ⊆
V,|Ω b|=N b, nested as in the beginning of Section IV.Local
indices[N b] :={1, . . . , Nb}enumerate only the active nodes
in a fixed order. The composite matrixD b ∈ {0,1}Nb×N maps
a global-indexed signal to its local form, andD ⊤ b scatters a
local-indexed signal back to theN-node domain. The selection
below acts in the local space[N b].
Each encoder block is equipped with a head that scores the
active nodes and keeps the highest-scoring ones. Concretely,
a node-wise MLPΨ b, with parametersΘ sel b , takes the block
outputZ b, along with the node and step embeddings restricted
to the active nodes, and returns a per-node score vector,
vb =Ψ b

Zb,D b [U0;K 0];Θ sel b

∈R Nb .(24)
The dependence onD b [U0;K 0], as in (22), allows the
selection to adapt to the node states and the diffusion step.
Given a down-sampling factorρ b+1 >1, we keep the
Nb+1 =⌊N b/ρb+1⌋highest-scoring nodes,
Sb = TopK(vb, Nb+1)⊆[N b].(25)
The selection matrixC b+1 =

INb

Sb,: ∈ {0,1}Nb+1×Nb
keeps the rows ofI Nb indexed byS b, and the composite matrix
updates asD b+1 =C b+1Db [cf. (18)]. The retained global
setΩ b+1 ⊆Ω b collects the nonzero columns ofD b+1, so
Sb andΩ b+1 express the same selection in local and global
coordinates, respectively.
The decoder performs no selection. At each depth, the
encoder-producedC b+1 is reused by the matched decoder for
up-sampling throughC ⊤ b+1 [cf. (23)], whileD b parametrizes
the depth-bGNN modules [cf. (19)–(21)].
TABLE I: Summary of U-GNN configuration.
Hyperparameter S&P 500 WRA
U-GNN (depthB= 4)
Pooling levels (factor)3(ρ=2,¯ρ B=8)
Channel widthsF 0 =· · ·=FB 64
GNN layersL/ hopsK ℓ 2/2
GNN strideγ b min{⌊¯ρb⌋, γmax = 2}
Embedding dim (step, cond.) 128
Dropout 0.1
Conditioning channelsU12 2
Conditioning fusion cross-attn. concat.
Diffusion
Diffusion noise stepsK500
Noise scheduleβlinear

β1 = 10−4, β500 = 2×10 −2
DDIM steps (η)100(0.2)
Optimization
Optimizer AdamW,β= (0.9,0.98)
Learning rate schedule Cosine anneal (10 −4)
Epochs 5000
Batch size 64 800
The Top-K operation in (25) is non-differentiable inv b.
Therefore, we train the headΨ b with a straight-through
estimator (STE) [44] that keeps the hard selectionS b in the
forward pass, while gradients reach the scoresv b through a
differentiable sigmoid surrogate of the binary selection mask.
Appendix C details the surrogate mask, and Appendix D
integrates classical fixed-pooling rules with the U-GNN.
V. NUMERICALRESULTS
We evaluate the proposed U-GNN denoiser on stock price
forecasting for the S&P 500 index and wireless resource
allocation (WRA) in a power control setup. Both use the same
depth-B=4U-GNN backboneϵ θ, diffusion noise schedules,
and optimizers. They differ only in the signal and condi-
tioning interface that each task dictates—a multi-step return
trajectory for forecasting versus a single power allocation for
resource allocation. Table I summarizes the model, diffusion,
and optimization hyperparameters. We detail the shared and
application-specific configurations in Appendix E.
A. Stock Price Forecasting
We cast stock price forecasting as a spatio-temporal gener-
ative task. Given recent market history for a panel of stocks,
the goal is to sample from the conditional distribution of their
short-horizon future log-return trajectories.
Setup.We use daily S&P 500 data obtained with the open-
sourceyfinancelibrary. After aligning all stocks on a
common trading day axis and dropping those with insufficient
coverage, we retainN= 468stocks across11GICS sectors
over2353trading days (2016-09-06 to 2026-02-13). Let
r(t) ∈R N collect the daily log returns on trading dayt,
where[r (t)]i is the log ratio of stocki’s consecutive closing
7

TABLE II:Forecast accuracy and distributional fidelity comparisons on the S&P 500 test split.Best values per column
are shown inbold. TheU-GNNoutperforms the GRW baseline in almost every accuracy, calibration and stylized-fact metrics.
Returns Price ($) Direction Stylized-fact gaps
Model CRPS↓MIS 90 ↓RMSE↓MAE↓CRPS↓MIS 90 ↓RMSE↓MAE↓MV-DA↑V ol↓Mom↓Kurt↓
U-GNN 1.01 9.28 1.96 1.36 2.69 25.17 10.03 3.62 0.53 0.06 0.0312.96
GRW 1.08 9.69 2.16 1.42 3.43 30.01 13.96 4.61 0.49 0.10 0.057.71
MV-DA: cumulative-horizon majority-vote direction accuracy.Vol,Mom,Kurt: absolute gap|s gen −s real|between generated and real volatility-clustering,
momentum, and excess-kurtosis statistics. Continuous ranked probability score (CRPS), mean 90% prediction interval score (MIS 90), root mean squared error
(RMSE), and mean absolute error (MAE) are reported on both the return and nominal price scales.
112.5
115.0
117.5
120.0
122.5
Price
APD
Historical
Target
Predicted (Mean)
90% CI
56
58
60
62
Price
FISV
215 219 223 227 231 235 239
Date Index
13.0
13.5
14.0
14.5
15.0
15.5
Price
HPQ
48
50
52
54
56
58
Price
C
Historical
Target
Predicted (Mean)
90% CI
115
120
125
130
135
Price
INCY
220 224 228 232 236 240 244
Date Index
58
60
62
Price
ZTS
80
82
84
86
88
Price
AVY
Historical
Target
Predicted (Mean)
90% CI
17
18
19
20
21
Price
CTRA
225 229 233 237 241 245 249
Date Index
66
67
68
69
70
71
72
Price
PCG
Fig. 3:Example S&P 500 forecasting trajectories from U-GNN. Each column is a different test window with three panels
for arbitrarily chosen stocks. In each panel, the solid black line is the observed history whereas the solid blue line is the
ground-truth future, the thin orange lines are individual trajectories sampled from the diffusion ensemble, and the solid orange
line is their mean, over the forecast horizon. The spread of the sampled trajectories reflects the forecast uncertainty.
prices. For each stock and day, we gatherU= 12market
features intou (t) ∈R N×U , comprising the open, high, low,
and standardized closing prices; the log returnr (t) and its
trailing moving averages; the log-volume; and two technical
indicators, RSI and MACD.
We build a static, undirected graphGfrom long-term
company fundamentals (e.g., market capitalization and price-
to-earnings ratios). Its adjacencyWcombines the rank corre-
lation between two stocks’ fundamental profiles with a same-
sector bonus. We threshold and spectrally normalizeWto
obtain the GSOS, which is shared across all forecast windows.
We form data samples with a sliding window of length
(Th +T p)over the panel. In each window, the first
Th days are the conditioning history, stacked intou=
[u (t−Th+1),· · ·,u(t) ]∈R N×T h×U , and the nextT p days
are the forecast target, stacked into the clean graph signal
x0 = [r (t+1),· · ·,r (t+Tp) ]∈R N×T p. We reversibly
instance-normalize (RevIN) each target window [45], using
statistics from its conditioning block alone, and we invert this
normalization on the DDIM-generated samples before scoring.
The U-GNN treats theT p horizon steps as a temporal axis. It
applies graph convolutions onSat each step, couples the steps
through interleaved temporal-convolution layers, and fuses a
per-node summary of theT h history steps into the conditioning
context by cross-attention.
We setT h = 20andT p = 5, yielding2328windows in total.
We partition them using an interleaved chronological scheme.
We split the trading-day axis into10equal chunks. Within each
chunk, we assign the earliest80%days to training, the next
10%to validation, and the final10%to testing, then pool the
matching parts across chunks. This ordering keeps each test
block later than its training block, so the model is never fitted
on days that follow its test period. Interleaving also spreads
anomalous regimes, such as COVID-19, across all three splits
rather than concentrating them in one, which mitigates the test
distribution shift that a single contiguous split would create.
Results.We assess the U-GNN forecasts qualitatively through
the sample trajectories of Fig. 3 and quantitatively through
8

1 2
Lag  l
0.10
0.05
0.00
0.05
0.10
0.15
Normalized ACF  l
Autocorrelation of r and r2
Real
GRW
U-GNN
r
r2
1 2 3 4 5
Eigenvalue rank
0
20
40
60
80
100
120
140Eigenvalue  k
Top-5 eigenvalues of C
i.i.d. ( = 1)
Real
GRW
U-GNN
(a)
1 2
Lag  l
0.10
0.05
0.00
0.05
0.10
0.15
Normalized ACF  l
Autocorrelation of r and r2
Real
GRW
U-GNN
r
r2
1 2 3 4 5
Eigenvalue rank
0
20
40
60
80
100
120
140Eigenvalue  k
Top-5 eigenvalues of C
i.i.d. ( = 1)
Real
GRW
U-GNN
(b)
1.0 1.5 2.0 2.5 3.0
GRW NLL per (stock, step)  [nats]
0
1
2
3
4
5
6Density
GRW-scored  NLL histogram
Real
GRW
U-GNN
i.i.d. Gaussian floor ( 1.42)
1.0 1.5 2.0 2.5 3.0
GRW NLL per (stock, step)  [nats]
0.0
0.2
0.4
0.6
0.8
1.0Empirical CDF
GRW-scored  Empirical CDF
Freal
FGRW
W1=0.23
FU GNN
W1=0.14
i.i.d. Gaussian floor ( 1.42)
0.25 0.30 0.35 0.40 0.45 0.50 0.55
Denoising MSE per element  (ELBO)
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Density
U-GNN-scored  NLL histogram
Real
U-GNN
GRW
0.25 0.30 0.35 0.40 0.45 0.50 0.55
Denoising MSE per element  (ELBO)
0.0
0.2
0.4
0.6
0.8
1.0Empirical CDF
U-GNN-scored  Empirical CDF
Freal
FU GNN
W1=0.04
FGRW
W1=0.14
(c)
1.0 1.5 2.0 2.5 3.0
GRW NLL per (stock, step)  [nats]
0
1
2
3
4
5
6Density
GRW-scored  NLL histogram
Real
GRW
U-GNN
i.i.d. Gaussian floor ( 1.42)
1.0 1.5 2.0 2.5 3.0
GRW NLL per (stock, step)  [nats]
0.0
0.2
0.4
0.6
0.8
1.0Empirical CDF
GRW-scored  Empirical CDF
Freal
FGRW
W1=0.23
FU GNN
W1=0.14
i.i.d. Gaussian floor ( 1.42)
0.25 0.30 0.35 0.40 0.45 0.50 0.55
Denoising MSE per element  (ELBO)
0.0
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Density
U-GNN-scored  NLL histogram
Real
U-GNN
GRW
0.25 0.30 0.35 0.40 0.45 0.50 0.55
Denoising MSE per element  (ELBO)
0.0
0.2
0.4
0.6
0.8
1.0Empirical CDF
U-GNN-scored  Empirical CDF
Freal
FU GNN
W1=0.04
FGRW
W1=0.14
(d)
Fig. 4:Distributional fidelity diagnostics on the S&P 500 test split. (a)Temporal structure: autocorrelation of returnsr
and squared returnsr 2 for real and generated series, probing linear predictability and volatility clustering.(b)Spatial (cross-
sectional) structure: the top-5 eigenvalues of the return covariance matrix ˆC, capturing how well each model reproduces inter-
stock correlation.(c)–(d)Histograms and empirical CDFs of per-window negative log-likelihood (NLL): values are computed
under the GRW model’s analytic likelihood(c)and as ELBO estimates under the trained U-GNN(d), each evaluated on the
real data and on samples drawn from both models. Close overlap between the generated and real distributions indicates higher
distributional realism; U-GNN’s samples track the real statistics more closely than the GRW baseline across all four panels.
the accuracy and distributional fidelity metrics of Table II,
both computed on the held-out test split with100sampled
trajectories per window. We benchmark U-GNN against a
geometric random walk (GRW), in which each stock’s future
log-returns are drawn i.i.d. from a fixed per-stock Gaussian. Its
drift and volatility are estimated once on the training set, with
shrinkage toward the market-wide statistics, and they are held
fixed at inference, independently of the conditioning window.
U-GNN outperforms the GRW on nearly every metric, at
both the return and price scales. It reduces price CRPS, RMSE,
and MAE by22%,28%, and21%, respectively, and recovers
directional information unavailable to a random walk, rais-
ing majority-vote direction accuracy above chance (0.53vs.
0.49). Beyond point and interval accuracy, U-GNN reproduces
stylized facts of returns. It substantially shrinks the volatility-
clustering gap (0.06vs.0.10) and reduces the momentum
gap. The one exception is excess kurtosis, where it overshoots
the empirical heavy tails. This overshoot is the artifact of a
desirable property. The GRW confines nearly all of its mass
to a band around the mean, whereas U-GNN places non-
negligible probability on the rare, far-from-mean moves that
real markets exhibit. At the reported checkpoint it allocates
somewhat more mass to these extremes than the data warrant,
and we read this gap as a fidelity–sharpness trade-off rather
than a fixed limitation. Checkpoints with a near-vanishing
kurtosis gap are attainable, but only by sacrificing sharpness.
Sharp forecasts emerge early in training and distributional
fidelity improves later, with the reported model sitting toward
the sharper end (Fig. 4(d)).
These dynamics are evident in the individual forecasts of
Fig. 3. The sampled trajectories spread out from the last
observed price, and the spread grows over the forecast days,
while their mean stays close to the realized path. Each sample
tends to track the recent behavior of its stock, picking up its
trend and volatility rather than flattening into a straight line
or spreading evenly in all directions. A few paths break from
the bundle to trace larger excursions, which is the generative
model anticipating the occasional market swings noted above.
Fig. 4 assesses the distributional fidelity of U-GNN samples
against those of GRW along four axes. Fig. 4(a) shows that
9

U-GNN matches the autocorrelation signature of stock returns,
which is near-zero forrand persistent forr 2, with the
latter implying strong volatility clustering. Fig. 4(b) pertains
to the cross-sectional structure, where U-GNN tracks the
leading eigenvalues of the return covariance ˆCthat capture
the dominant market directions, whereas the GRW baseline
flattens them. The remaining two plots take a score-based view.
Each assigns every evaluation window a scalar score, then
compares the resulting distribution to the real one through the
1-Wasserstein (W 1) distance between their empirical CDFs.
They differ only in which model supplies the score.
Fig. 4(c) uses the GRW score, the analytic NLL per (stock,
step) in nats, for which an i.i.d. Gaussian is lower-bounded by
its differential entropy 1 2 ln(2πe)≈1.42(dotted line). Scored
by the homoskedastic Gaussian that generated them, the GRW
samples collapse onto a near-degenerate spike essentially at
this floor, so every window is equally surprising, and the score
carries no volatility information. The real returns, instead,
spread out with a rightward skew, as calm windows fall below
the floor and heavy-tailed ones, beyond the reach of the GRW,
are pushed into the tail. U-GNN’s samples sit just left of the
floor (mean≈1.25), which the GRW scorer even rates as
more typical than an i.i.d. draw. Even under the baseline’s
own likelihood, U-GNN lands closer to the real distribution
(W1=0.14) than GRW’s own samples do (W 1=0.23).
Fig. 4(d) instead scores each window by a uniformly
weighted version of U-GNN’s training loss in (6), estimated
by a stratified Monte Carlo average over64strata of the
diffusion step (one noise draw each). This orders windows
by denoising difficulty, and hence by volatility. U-GNN’s
samples cluster lowest (mean≈0.28), while the real data
lies just to their right (mean≈0.32). GRW paths form a
distinct high-error mode (mean≈0.46), since memoryless
Gaussian increments are hard to denoise for a model that
expects temporal and cross-sectional structures. Here, U-GNN
nearly coincides with the real data (W 1=0.04), while GRW
sits farther away (W 1=0.14). Neither score is impartial on
its own, but read together, they corroborate that U-GNN
better captures the real distribution. While U-GNN’s score
isolates GRW samples as unrealistic, GRW ranks U-GNN
above the real data. That said, the temporal nature of stock data
may favor attention-based architectures suited to long-range
dependencies. We leave the integration of a graph transformer
with our U-GNN backbone to future work.
B. Wireless Resource Allocation
We study optimal power control in multi-user interference
networks. The setup closely follows our preliminary work on
diffusion policies for resource allocation [2], [32] and the
related state-augmented formulations of [11]. We summarize
it below and collect the simulation parameters in Table III.
Setup.We consider wireless networks ofN= 400
transmitter–receiver (tx–rx) pairs dropped uniformly at random
over a square service area. The pairs share a single channel of
bandwidthWwith noise PSDN 0 and per-transmitter power
budgetP max (Table III). The channel gainh ij,t ∈R + from
TABLE III: Power control (WRA) simulation setup.
Parameter Value
Network and deployment
Tx–rx pairsN400
Area side lengthR{7800,7000,6300,5800}m
User densityν{6.6,8.2,10.1,11.9}pairs/km 2
Tx–rx separationUniform[20,100]m
Min. tx–tx spacing 50 m
Networks128(32 per density)
Train/val/test (per density)20/4/8(5:1:2)
Channel and fading
BandwidthW40 MHz
Carrier frequencyf c 2.4 GHz
Noise PSDN 0 -174 dBm/Hz
Max. tx powerP max 10 dBm (10 mW)
Shadowing std. dev. 7 dB
Allocation timescale
Fading stepδt10 ms
Realizations per networkT500
Ergodic windowT 0 5 slots (50ms)
Slots per networkS100
transmitterito receiverjat steptcombines a static large-scale
component with a unit-mean Rayleigh fast-fading component.
The large-scale component follows a dual-slope path-loss law
with log-normal shadowing and fixes the long-term average
gainh ij. We collect the long-term and instantaneous gains in
H,H t ∈R N×N + , with[H] ij =h ij and[H t]ij =h ij,t.
The policy and the instantaneous gainsH t evolve on
separate timescales. The fast-fading process generatesTre-
alizations ofH t, while the policy emits one allocation per
slot and holds it constant over a window ofT 0 realizations,
givingS=T /T 0 slots per network (Table III). The network
configurationHstays fixed over the operation window and is
the only channel state available at allocation time. The policy
is conditioned onHvia the GSOSand node-stateu(defined
below), while the instantaneous gainsH t are observed only
through the rates they induce.
We model each configuration as a drawH∼q H from a
family of network geometries and large-scale fading. Sweeping
the area side lengthRover four values yields four user
densities, each contributing32networks for a dataset of128
configurations in total, which we split5:1:2into training,
validation, and testing (Table III).
Given an allocationpand a channel realization eH, the rate
of the receiverjis
ef(p, eH)  j = log2

1 + [p]j [ eH]jj
W N0 + P i̸=j[p]i [ eH]ij

.(26)
We evaluate a policy by its ergodic rate, estimated by averag-
ing the instantaneous rates over the fading realizations,
f(π,H) =E p, eH
 ef(p, eH)  ≈ 1 T TX t=1 ef  p⌈t/T0⌉,H t  .(27)
10

TABLE IV:Ergodic-rate performance on the WRA test split (32networks,12,800tx–rx pairs,f min = 0.6bits/s/Hz).
U-GNNtracks the expert (PD) policy on the cell-edge percentiles and feasibility, where FP and AP collapse. Per column, the
policy performing closest to the reference expert is shown inboldand±is one standard deviation across networks.
Ergodic rate (bits/s/Hz)↑Gap to expert (%)↓ Feasible (%)↑
Model p1 p5 p10 mean p1 p5 p10 mean
PD-Expert(ref.)0.66±0.10 0.82±0.11 0.93±0.12 2.84±0.27— — — —99.1±1.1
U-GNN0.55±0.100.77±0.090.92±0.09 2.81±0.3317.8 5.3 0.91.198.1±1.1
Full power (FP)0.08±0.04 0.28±0.09 0.53±0.14 3.14±0.3687.9 65.4 43.0−10.6 88.0±2.9
Avg. power (AP)0.19±0.08 0.52±0.13 0.74±0.152.85±0.3971.8 36.8 19.7−0.392.7±2.7
pk:k-th percentile of per-user ergodic rates (worst-served tx–rx pairs).Gap:100×(f exp −f)/f exp (>0: below expert,<0: above).Feasible: Percentage
of tx–rx pairs meetingf min. FP usesP max on every link; AP uses each network’s mean expert power.
In (27), the expectation is over the policy allocationsp∼
π(· |H)and the fast-fading channeleH∼q eH|H. The allocation
ps is drawn once per slots=⌈t/T 0⌉and held fixed across
it, whileH t is the channel realized at stept.
GivenH, an optimal policyπ ⋆(H) =π ⋆(·

 H)maximizes
the ergodic sum-rate subject to a per-user minimum-rate (QoS)
requirementf min = 0.6bits/s/Hz, i.e.,
π⋆(H)∈argmax
π
1⊤ N f(π,H)(28a)
subject tof(π,H)≥f min 1N .(28b)
The diffusion targets are produced by anexpert primal–
dual (PD) algorithmthat solves (28) via Lagrangian dual
(sub)gradient ascent. We train a separate expert per density
group, parametrized by a shallow GNN, across all networks.
We then collect200allocations per training network from its
converged primal iterates, giving16000conditional samples
that the diffusion model (U-GNN) learns to reproduce given
(S,u). Running the same expert across all splits, including the
validation and test networks held out from U-GNN, yields the
reference allocations against which we benchmark the U-GNN
policy. Since the expert solves each network directly rather
than generalizing, it is a near-ideal reference that U-GNN
can only approach, so the comparison favors the expert by
design. At inference, U-GNN thus samples directly from this
distributionof near-optimal, feasible allocations rather than
re-solving the optimization per network. We refer to [2] for
the expert’s algorithmic details.
We representHas a directed, weighted channel graph on
Nnodes, one per tx–rx pair. A self-loop carries the direct-link
gainh ii, and an edge carries the interference gainh ij,i̸=j,
which is generally asymmetric, i.e.,h ij ̸=h ji. We sparsify
this graph into the GSOSby retaining, for each receiver, its
self-loop and the incoming edges from them= 10strongest
interferers, followed by a log-normalization that compresses
the wide dynamic range of the channel gains. We also derive
a two-feature node-state vectoruthat collects each node’s
direct-link strength and its aggregate incoming interference
under full-power transmission. BothSanduare deterministic
functions ofH, so they form the conditioning inputξ= (S,u)
of Section II, andq H induces its distributionq ξ.
The diffusion variable is the rescaled allocationx 0 =
p/Pmax − 1 2 ∈[− 1 2 , 1 2 ]N , viewed as a scalar graph signal onS.
We realize the U-GNN policy, which is trained to imitate the
optimal policyπ ⋆, through the conditional diffusion generator
pθ⋆ (· |S,u)of Section II. That is, givenH, we sample a batch
ofS= 100rescaled allocationsx 0 ∼p θ⋆ (· |S,u)and map
them to power allocationsp= clip [0,Pmax]

Pmax(x0 + 1 2 )  .
We place these allocations in random order as{p s}S s=1 and
execute them sequentially, with slotstransmittingp s over its
T0-realization window.
We compare the U-GNN policy against two deterministic
baselines that forgo time-sharing. For every slotsand net-
workH, full power (FP) setsp s =P max1N , and average
power (AP) is the expert’s per-network mean allocation, i.e.,
ps(H)≈E p∼π⋆(· |H)

p

.
Results.We report in Table IV the ergodic-rate performance
of the U-GNN policy, expert (PD) policy, and baselines.
The U-GNN diffusion policy closely matches the expert
across the full distribution. Its 5th- and 10th-percentiles (p5,
p10) rates reach0.77and0.92bits/s/Hz, trailing the expert
by only5.3%and0.9%. The p5rate already exceeds the
fmin = 0.6bits/s/Hz floor, and only the bottom∼2%of users
fall slightly short. U-GNN’s gap to the expert is largest at
p1, at17.8%(0.55vs.0.66bits/s/Hz), whereas FP and AP
baselines trail by87.9%and71.8%at this percentile, making
U-GNN’s degradation minor by comparison. FP attains the
highest mean rate at3.14bits/s/Hz while collapsing its p1
rate to0.08bits/s/Hz and lowering feasibility to88.0%. U-
GNN instead sustains a mean rate of2.81bits/s/Hz, on par
with the expert (2.84) and AP (2.85). AP matches this mean
rate but still leaves7.3%of users belowf min, so collapsing
the policy to a deterministic mean allocation is not enough.
U-GNN’s value rests jointly on its stochastic formulation
and generative sampling. The stochastic formulation treats the
policy as a distribution over allocations, sustaining feasibil-
ity through randomization where the deterministic AP fails.
The expert shares this formulation but reaches it through
thousands of primal–dual iterations per network, whereas U-
GNN bypasses online optimization and attains comparable
performance in a single DDIM sampling pass.
Fig. 5 illustrates why the optimal policy must be stochastic
and how U-GNN realizes it throughtime-sharing. The optimal
(expert) policy is multi-modal, activating a different subset of
the mutually interfering tx–rx pairs in each slot. No single
allocation serves all users, yet, alternating them across slots
renders the time-averaged ratef(π ⋆,H)feasible for every
11

400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
allocation · time slot s 1
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
allocation · time slot s
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
allocation · time slot s + 1
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
mean allocation  E[p]
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
rate · time slot s 1  (56% feas)
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
rate · time slot s  (57% feas)
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
rate · time slot s + 1  (86% feas)
400 600 800 1000 1200 1400 1600
X (m)
800
1000
1200
1400
1600
1800
2000
Y (m)
TIME-SHARING rate  (100% feas)
0.01
0.022
0.046
0.1
0.22
0.46
1
Normalized tx power p/Pmax
0.00
0.20
0.40
0.60
1.7
4.7
13
Rate (bits/s/Hz)
WRA power-allocation realizations vs stochastic time-sharing  low density, network 0, r_min=0.6  (camera zoom · 19 RXs in view, cross-boundary edges trail off)
Fig. 5:U-GNN attains ergodic feasibility through time-sharing.We zoom in on an example test network, where each node
is a tx–rx pair and edges indicate interference strength. The top row shows the per-node normalized transmit powerp/P max
(logarithmic color scale) for three consecutive slots of the sequential allocation sampled by the U-GNN policy, alongside the
mean allocationE[p](rightmost). The bottom row shows the per-receiver rates for each slot (color bar centered atf min) with
the per-slot feasibility annotated above, and the time-averaged rate delivered by time-sharing (rightmost). No single slot serves
all users (56–86%feasible), yet alternating these allocations across slots mitigates interference and achieves 100% feasibility
for this network. In contrast, the mean allocation rates typically stay infeasible for interference-limited tx–rx pairs.
200 400 600 800 1200 1600
Network size (number of tx-rx pairs)
0.5
0.6
0.7
0.8
0.9
1.0Ergodic p5-rate (bits/s/Hz)
Density (tx-rx pairs/km2)
6.6
8.2
10.1
11.9
fmin
Native (training size)
Fig. 6:Size-transferability of the U-GNN policy.Ergodic
5th-percentile (p5) rate vs. network size for four interference
densities (tx–rx pairs/km2) atf min = 0.6bits/s/Hz (red dashed
line). Diamonds mark the native training size (400pairs), and
all other sizes are evaluated without retraining.
receiver. Crucially, this rate averages the per-slot rates and
must not be conflated with the rate of the single mean
allocationE[p], which activates every interferer at once and
remains infeasible. This is exactly the failure mode of the AP
baseline in Table IV.
Fig. 6 examines the size-transferability of the U-GNN
policy. The model is trained only on networks of the native
size|V|= 400tx–rx pairs (diamonds) with mixed densities.
It is then evaluated without retraining on networks ranging
from200to1600pairs at similar densities. The ergodic
5th-percentile rate stays essentially flat and above thef min
floor across this range for every density. Denser networks
(11.9vs.6.6pairs/km 2) attain lower tail rates due to stronger
interference, but their ordering and stability are preserved
across all sizes. This indicates that the permutation-equivariant
GNN backbone is also scalable. Similar observations hold for
the mean and additional tail rates, which are not shown here.
VI. CONCLUSION& FUTUREWORK
We proposed a denoising diffusion framework for generat-
ing graph signals. We cast this as a denoising process and
parametrized it with a U-GNN, a graph-domain adaptation
of the U-Net. At its core, a pooling mechanism formal-
izes down/up-sampling as learned node selection via nested
selection matrices and zero-padding. We demonstrated the
framework on wireless resource allocation and stock-price
forecasting. Future directions include designing graph-aware
and latent diffusion processes, and integrating graph trans-
formers into the U-GNN backbone for spatio-temporal tasks.
REFERENCES
[1] Yi ˘git Berkay Uslu, Samar Hadou, Sergio Rozada, Shirin Saeedi
Bidokhti, and Alejandro Ribeiro, “Graph signal generative diffusion
12

models,” inIEEE Intl. Conf. Acoust., Speech and Signal Process.
(ICASSP). IEEE, 2026, pp. 626–630.
[2] Yigit Berkay Uslu, Samar Hadou, Shirin Saeedi Bidokhti, and Alejandro
Ribeiro, “Graph signal diffusion models for wireless resource alloca-
tion,”arXiv preprint arXiv:2604.05175, 2026.
[3] Xiang Wang, Xiangnan He, Meng Wang, Fuli Feng, and Tat-Seng
Chua, “Neural graph collaborative filtering,” inIntl. ACM SIGIR Conf.
Research and Develop. Info. Retrieval, 2019, pp. 165–174.
[4] Kelong Mao, Jieming Zhu, Xi Xiao, Biao Lu, Zhaowei Wang, and
Xiuqiang He, “Ultragcn: Ultra simplification of graph convolutional
networks for recommendation,” inACM Intl. Conf. Info. and Knowledge
Management (CIKM), 2021, pp. 1253–1262.
[5] Jiahao Liu, Dongsheng Li, Hansu Gu, Tun Lu, Peng Zhang, Li Shang,
and Ning Gu, “Personalized graph signal processing for collaborative
filtering,” inACM Web Conf. (WWW), 2023, pp. 1264–1272.
[6] Mark Eisen and Alejandro Ribeiro, “Optimal wireless resource allo-
cation with random edge graph neural networks,”IEEE Trans. Signal
Process., vol. 68, pp. 2977–2991, 2020.
[7] Yifei Shen, Jun Zhang, S. H. Song, and Khaled B. Letaief, “Graph
neural networks for wireless communications: From theory to practice,”
IEEE Trans. Wireless Commun., vol. 22, no. 5, pp. 3554–3569, 2023.
[8] Zhongyuan Zhao, Gunjan Verma, Chirag Rao, Ananthram Swami, and
Santiago Segarra, “Link scheduling using graph neural networks,”IEEE
Trans. Wireless Commun., vol. 22, no. 6, pp. 3997–4012, 2023.
[9] Yunqi Wang, Yang Li, Qingjiang Shi, and Yik-Chung Wu, “ENGNN:
A general edge-update empowered GNN architecture for radio resource
management in wireless networks,”IEEE Trans. Wireless Commun.,
vol. 23, no. 6, pp. 5330–5344, 2024.
[10] Arindam Chowdhury, Gunjan Verma, Ananthram Swami, and Santiago
Segarra, “Deep graph unfolding for beamforming in mu-mimo inter-
ference networks,”IEEE Trans. Wireless Commun., vol. 23, no. 5, pp.
4889–4903, 2024.
[11] Yi ˘git Berkay Uslu, Navid NaderiAlizadeh, Mark Eisen, and Alejandro
Ribeiro, “Fast state-augmented learning for wireless resource allocation
with dual variable regression,” 2025.
[12] Yingmei Chen, Zhongyu Wei, and Xuanjing Huang, “Incorporating
corporation relationship via graph convolutional neural networks for
stock price prediction,” inACM Intl. Conf. Info. and Knowledge
Management (CIKM), 2018, pp. 1655–1658.
[13] Ramit Sawhney, Shivam Agarwal, Arnav Wadhwa, and Rajiv Ratn Shah,
“Spatiotemporal hypergraph convolution network for stock movement
forecasting,” inIEEE Intl. Conf. Data Mining, 2020, pp. 482–491.
[14] Ajim Uddin, Xinyuan Tao, and Dantong Yu, “Attention based dynamic
graph neural network for asset pricing,”Global Finance Journal, vol.
58, 2023.
[15] Nathanael Perraudin and Pierre Vandergheynst, “Stationary signal
processing on graphs,”IEEE Trans. Signal Process., vol. 65, no. 13, pp.
3462–3477, 2017.
[16] Jaehyeong Jo, Seul Lee, and Sung Ju Hwang, “Score-based generative
modeling of graphs via the system of stochastic differential equations,”
inIntl. Conf. on Machine Learning (ICML), 2022, vol. 162 ofPMLR,
pp. 10362–10383.
[17] Cl ´ement Vignac, Igor Krawczuk, Antoine Siraudin, Bohan Wang, V olkan
Cevher, and Pascal Frossard, “DiGress: Discrete denoising diffusion for
graph generation,” inIntl. Conf. on Learning Repr. (ICLR), 2023.
[18] Emiel Hoogeboom, V ´ıctor Garcia Satorras, Cl ´ement Vignac, and Max
Welling, “Equivariant diffusion for molecule generation in 3d,” inIntl.
Conf. on Machine Learning (ICML), 2022, vol. 162 ofPMLR, pp. 8867–
8887.
[19] Diederik P. Kingma and Max Welling, “Auto-encoding variational
bayes,” inIntl. Conf. on Learning Repr. (ICLR), 2014.
[20] Ian J. Goodfellow, Jean Pouget-Abadie, Mehdi Mirza, Bing Xu, David
Warde-Farley, Sherjil Ozair, Aaron Courville, and Yoshua Bengio,
“Generative adversarial nets,” inAdvances in Neural Info. Process.
Syst., 2014, vol. 27, pp. 2672–2680.
[21] Danilo Jimenez Rezende and Shakir Mohamed, “Variational inference
with normalizing flows,” inIntl. Conf. on Machine Learning (ICML),
2015, vol. 37 ofPMLR, pp. 1530–1538.
[22] Jonathan Ho, Ajay Jain, and Pieter Abbeel, “Denoising diffusion
probabilistic models,” inAdvances in Neural Info. Process. Syst., 2020,
vol. 33, pp. 6840–6851.
[23] Jiaming Song, Chenlin Meng, and Stefano Ermon, “Denoising diffusion
implicit models,” inIntl. Conf. on Learning Repr. (ICLR), 2021.
[24] Yang Song, Jascha Sohl-Dickstein, Diederik P. Kingma, Abhishek Ku-
mar, Stefano Ermon, and Ben Poole, “Score-based generative modeling
through stochastic differential equations,” inIntl. Conf. on Learning
Repr. (ICLR), 2021.
[25] Yaron Lipman, Ricky T. Q. Chen, Heli Ben-Hamu, Maximilian Nickel,
and Matt Le, “Flow matching for generative modeling,” inIntl. Conf.
on Learning Repr. (ICLR), 2023.
[26] Haomin Wen, Youfang Lin, Yutong Xia, Huaiyu Wan, Qingsong Wen,
Roger Zimmermann, and Yuxuan Liang, “DiffSTG: Probabilistic spatio-
temporal graph forecasting with denoising diffusion models,” inACM
Intl. Conf. Adv. Geo. Info. Syst. (SIGSPATIAL). 2023, pp. 1–12, ACM.
[27] Divyanshu Daiya, Monika Yadav, and Harshit Singh Rao, “DiffSTOCK:
Probabilistic relational stock market predictions using diffusion models,”
inIEEE Intl. Conf. Acoust., Speech and Signal Process. (ICASSP). 2024,
pp. 7335–7339, IEEE.
[28] Weijun Chen and Yanze Wang, “DHMoE: Diffusion generated hierar-
chical multi-granular expertise for stock prediction,”AAAI Conf. Artif.
Intell., vol. 39, no. 11, pp. 11490–11499, 2025.
[29] Sergio Rozada, Vimal K B, Andrea Cavallo, Antonio G. Marques,
Hadi Jamali-Rad, and Elvin Isufi, “Graph-aware diffusion for signal
generation,” inIEEE Intl. Conf. Acoust., Speech and Signal Process.
(ICASSP), 2026, pp. 461–465.
[30] Amirhassan Babazadeh Darabi and Sinem Coleri, “Diffusion model
based resource allocation strategy in ultra-reliable wireless networked
control systems,”IEEE Commun. Lett., 2024.
[31] Ruihuai Liang, Bo Yang, Zhiwen Yu, Bin Guo, Xuelin Cao, M ´erouane
Debbah, H. Vincent Poor, and Chau Yuen, “Diffsg: A generative solver
for network optimization with diffusion model,”IEEE Commun. Mag.,
vol. 63, no. 6, pp. 16–24, 2025.
[32] Yi ˘git Berkay Uslu, Samar Hadou, Shirin Saeedi Bidokhti, and Alejandro
Ribeiro, “Generative diffusion models for resource allocation in wireless
networks,” inIEEE Intl. Wrksp. Computat. Advances Multi-Sensor
Adaptive Process. (CAMSAP), 2025, pp. 201–205.
[33] Jia Guo, Xiaoxia Xu, Yuanwei Liu, and Arumugam Nallanathan, “Diffu-
sion model for multiple antenna communication,”IEEE Commun. Mag.,
vol. 63, no. 10, pp. 44–50, 2025.
[34] Zhizhou He, Fabien H ´eliot, and Yi Ma, “Deterministic score-based
diffusion model for channel estimation in ris-assisted mimo systems,”
inIEEE Intl. Wrkshp. Signal Process. and Artif. Intell. for Wireless
Commun. (SPAWC), 2025, pp. 1–5.
[35] Taekyun Lee, Juseong Park, Hyeji Kim, and Jeffrey G. Andrews, “Gen-
erating high dimensional user-specific wireless channels using diffusion
models,”IEEE Trans. Wireless Commun., vol. 25, pp. 2907–2921, 2026.
[36] Olaf Ronneberger, Philipp Fischer, and Thomas Brox, “U-net: Convolu-
tional networks for biomedical image segmentation,” inMedical Image
Comput. and Computer-Assisted Intervention (MICCAI). 2015, vol. 9351
ofLecture Notes in Computer Science, pp. 234–241, Springer.
[37] Fabian Isensee, Paul F. Jaeger, Simon A. A. Kohl, Jens Petersen, and
Klaus H. Maier-Hein, “nnu-net: a self-configuring method for deep
learning-based biomedical image segmentation,”Nature Methods, vol.
18, no. 2, pp. 203–211, 2021.
[38] Fernando Gama, Antonio G. Marques, Geert Leus, and Alejandro
Ribeiro, “Convolutional neural network architectures for signals sup-
ported on graphs,”IEEE Trans. Signal Process., vol. 67, no. 4, pp.
1034–1049, 2019.
[39] Rex Ying, Jiaxuan You, Christopher Morris, Xiang Ren, William L.
Hamilton, and Jure Leskovec, “Hierarchical graph representation learn-
ing with differentiable pooling,” inAdvances in Neural Info. Process.
Syst., 2018, vol. 31, pp. 4805–4815.
[40] Hongyang Gao and Shuiwang Ji, “Graph u-nets,” inIntl. Conf. on
Machine Learning (ICML), 2019, vol. 97 ofPMLR, pp. 2083–2092.
[41] Jost Tobias Springenberg, Alexey Dosovitskiy, Thomas Brox, and Martin
Riedmiller, “Striving for simplicity: The all convolutional net,” inIntl.
Conf. on Learning Repr. (ICLR), Workshop Track, 2015.
[42] Fisher Yu and Vladlen Koltun, “Multi-scale context aggregation by
dilated convolutions,” inIntl. Conf. on Learning Repr. (ICLR), 2016.
[43] Luana Ruiz, Fernando Gama, and Alejandro Ribeiro, “Graph neural
networks: Architectures, stability, and transferability,”Proc. IEEE, vol.
109, no. 5, pp. 660–682, 2021.
[44] Yoshua Bengio, Nicholas L ´eonard, and Aaron Courville, “Estimating
or propagating gradients through stochastic neurons for conditional
computation,”arXiv preprint arXiv:1308.3432, 2013.
[45] Taesung Kim, Jinhee Kim, Yunwon Tae, Cheonbok Park, Jang-Ho Choi,
and Jaegul Choo, “Reversible instance normalization for accurate time-
series forecasting against distribution shift,” inIntl. Conf. on Learning
Repr. (ICLR), 2022.
[46] Wouter Kool, Herke Van Hoof, and Max Welling, “Stochastic beams
and where to find them: The gumbel-top-k trick for sampling sequences
without replacement,” inIntl. Conf. on Machine Learning (ICML).
PMLR, 2019, pp. 3499–3508.
13

APPENDIXA
ACCELERATEDDDIM SAMPLING
The base DDIM sampler (9) deferred the specification of
its noise scaleσ k. We provide it here, where it also governs
the accelerated sampler used in our experiments. A factorη∈
[0,1]controls the per-step stochasticity through
σk(η) =η
r
1−¯αk−1
1−¯αk
r
1− ¯αk
¯αk−1
,(29)
which interpolates between the ancestral DDPM update atη=
1and the deterministic DDIM map atη= 0.
Because the DDIM updates in (9) preserve the marginals of
the forward process, we can subsample the denoising steps to
accelerate inference without retraining. Concretely, we train
ϵθ⋆ on the full grid ofKsteps but sample along only an
increasing subset{τ 1, . . . , τK′} ⊂ {1, . . . , K}withτK′ =K
andK ′ ≪K, and we setτ 0 := 0. We drawx τK′ =x K ∼
N(0,I)and iterate the update (9) over this sub-grid,
xτk−1 = p¯ατk−1 bx0 + q 1−¯ατk−1 −σ 2τk ϵθ⋆ +στk w,(30)
fork=K ′, . . . ,1, andw∼ N(0,I). We note that both
bx0 = bx0(xτk , τk;ξ)[cf. (7)] andϵ θ⋆ =ϵ θ⋆ (xτk , τk;ξ)are
evaluated at the current stepτ k. The noise scaleσ τk follows
from (29) under the substitution(k, k−1)7→(τ k, τk−1).
APPENDIXB
IMPLEMENTATION OFSTRIDEDGRAPHCONVOLUTIONS
A literal evaluation of the strided graph convolution in (14)
would form the operatorS γ and accumulate its powers(S γ)k,
k= 0, . . . , K. Forγ >1, this densifiesSand forfeits its
sparsity, much like the reduced GSOsS (k) of (15) do. We
instead exploit(S γ)k =S γk and evaluate the layer through
γKsuccessive sparse products with the unit shiftS, tapping
the signal everyγshifts.
Starting from the lifted signal eZ0 =D ⊤Zℓ−1, we form
eZj =S eZj−1 forj= 1, . . . , γKand accumulate the tapped
terms eZγk Θℓ,k,k= 0, . . . , K. We then apply the pointwise
nonlinearityσ ℓ and the poolingD. The untapped shifts,j /∈
{0, γ, . . . , γK}, only advance the walk to the next tapped hop.
Algorithm 1 summarizes the procedure.
Notably, we never materialize the reduced GSOs. The shift
Sis a sparse weighted aggregation, while the unpoolingD ⊤
and poolingDare index scatter and gather operations. Only
the running buffer eZj and one accumulator are kept, each
of sizeN×F, so each layer runs in roughlyO(γK|E|F)
aggregation time andO(N F)memory, where|E|is the
number of edges ofG. Forming the denseS γ explicitly would
instead costO(N 2)memory. The filter keepsK+ 1taps for
anyγ, so the stride adds shifts but no parameters.
The stride enters only as a multiplier on the shift count and
is tied to the pooling ratio. When the GNN module sits in a
depth-bblock of the U-GNN, it instantiates (14) withD=D b,
and all of its layers share the strideγ b = min{⌊√¯ρb ⌋, γmax},
where¯ρ b = Qb i=1 ρi =N/N b is the cumulative down-
sampling factor [cf. (18)]. This is the ruleγ=⌊ √ρ⌋of
Algorithm 1Strided graph convolutions via iterated unit shifts
Require:Input signalZ ℓ−1 ∈R N ′×Fℓ−1; shiftS; selection
D; taps{Θ ℓ,k}K k=0; strideγ; pointwise nonlinearityσ ℓ
Ensure:Output signalZ ℓ ∈R N ′×Fℓ
1: eZ0 ←D ⊤Zℓ−1 ▷lift to the full vertex set
2:A← eZ0 Θℓ,0 ▷tapk= 0
3:forj= 1, . . . , γKdo
4: eZj ←S eZj−1 ▷one sparse shift; a singleN×F
buffer suffices
5:ifγ|jthen
6:A←A+ eZj Θℓ, j/γ ▷tap everyγshifts
7:end if
8:end for
9:Z ℓ ←Dσ ℓ(A)▷nonlinearity, then reduce toΩ
10:returnZ ℓ
Remark 1 applied at depthbwithρ= ¯ρ b and capped atγ max,
so the total reachγ bKdoes not span the whole graph and we
avoid oversmoothing.
APPENDIXC
STRAIGHT-THROUGHESTIMATION ANDSTOCHASTIC
TOP-K SELECTION
To train the score headΨ b by backpropagation, we apply a
straight-through estimator (STE) [44] to the binary selection
mask. That is, the forward pass selects a hard mask, while
gradients reachv b through a differentiable sigmoid surrogate.
Moreover, we employ a Gumbel-perturbed Top-K rule to
encourage exploration during training.
Stochastic selection.Leth b ∈ {0,1}Nb be the Top-K indica-
tor, with[h b]n =1{n∈ S b}. At inference,S b is the determin-
istic Top-K of (25). During training, we drawS b stochastically
to encourage exploration of the discrete selection. Given i.i.d.
standard Gumbel variates[g b]n =−log(−logu n),u n ∼
Uniform(0,1), and an exploration scaleε∈R +, we perturb
the scores before ranking,
Sb = TopK(vb +εg b, Nb+1).(31)
Note that Top-K is invariant to positive scaling, i.e.,
TopK(vb +εg b, Nb+1) = TopK(v b/ε+g b, Nb+1). By the
Gumbel-Top-K trick [46], (31) therefore drawsS b without
replacement with probabilities proportional toe [vb]n/ε. The
scaleεacts as a sampling temperature, and asε→0, the
sample concentrates on the deterministic Top-K, which we
recover at inference when the perturbation vanishes atε= 0.
Straight-through gradient.For the backward pass, we form
a surrogate from theunperturbedscores. Given a temperature
τ∈R + and the logistic sigmoidς(·), we set ehb =ς(v b/τ)∈
(0,1) Nb. The training mask is
mb =h b + ehb −sg( ehb),(32)
wheresg(·)is the stop-gradient operator. The soft terms
cancel in value, thusm b =h b in the forward pass. In the
backward pass,sg( ˜hb)is constant, so the gradient reachesv b
14

only through ˜hb. We note that because the surrogate uses the
unperturbed scores, the Gumbel noise affects only which nodes
enterS b, not the surrogate gradient at any node.
Gated down-sampling.We insert this mask into the en-
coder down-sampling. During training, the depth-(b+1)input
Vb+1 =C b+1 Zb of (22) becomes
Vb+1 =C b+1

mb ⊙Z b

, b= 1, . . . , B−1,(33)
where⊙scales each row ofZ b by the corresponding entry of
mb. Sincem b =h b in the forward pass, the selected rows pass
through unchanged, andC b+1 discards the rest. At inference,
the STE branch is dropped (m b =h b), and (33) reverts to the
plain down-sampling viaC b+1 Zb.
Schedules.We anneal bothτandεlinearly over training. Lett
andTdenote the current and total number of training epochs,
withT= 5000as reported in Table I. The schedule uses a
warm-up ofT w epochs followed by an anneal ofT a epochs,
τ(t) =τ 0 +r(t) (τ min −τ 0),
ε(t) =ε 0 +r(t) (ε min −ε 0), (34)
wherer(t) = min{max{(t−T w)/Ta,0},1}. We setT w =
0.02T,T a = 0.73T,(τ 0, τmin) = (1,0.5), and(ε 0, εmin) =
(1,0). This way, bothεandτreach their floors at epoch
Tw +T a = 0.75T, after which selection is (approximately)
deterministic, and the surrogate sharpness is fixed. These
values worked well in our experiments, but we found the
results to be robust, as any choice that explores broadly early
and becomes deterministic well before training ends gave
comparable performance.
We remark that the STE in (32) supplies a surrogate gradient
for the binary mask, and not a differentiable relaxation of
the hard Top-K rule. In the forward pass,C b+1 removes the
unselected rows, so each training iteration passes diffusion-
loss gradients only to the score entries of the nodes inS b. The
head nonetheless learns a global ranking for two reasons. First,
whileε >0, the stochastic selection variesS b across iterations,
so the gradient reaches a broader set of nodes over training.
Second, the head shares its parameters across all candidate
nodes, so each update reshapes the scoring function at every
node in subsequent passes.
APPENDIXD
CLASSICALSUM/MAX-POOLING OVERGRAPH
NEIGHBORHOODS
CNNs with pooling couple neighborhood aggregation and
spatial down-sampling into a single operation that summarizes
each pixel window, e.g., by its average or maximum, at a re-
duced resolution. This coupling exploits the intrinsic geometry
of the regular grid. For a general graph, the GSOSsupplies
the analogous structural information, which we use to define
pooling neighborhoods.
Our design decouples these two operations. The strided
graph convolution in (14) already returns a nonlinear summary
of each node’s neighborhood. In reduced indices, this is theK-
hop reach of{S (k)}K k=0, and in the lifted domain, it is theγK-
hop reach ofSafterD ⊤ b lifts the signal and beforeD b reduces
it back [cf. (15)]. The learned selectorsC b in turn perform
the node-space down-sampling [cf. (25)]. An explicit sum- or
max-pooling over graph neighborhoods is therefore optional
rather than essential. We describe it next for completeness.
Pooling over the full graph.For a givenSand pooling range
κ∈Z +, we define the binaryreachability matrix

R(S)

n,m :=1
n
Sk n,m ̸= 0for some0≤k≤κ o .(35)
Note that each node reaches itself. FromR=R(S)we read
off, for each noden∈ V, the index set
n(n) :=
n
m∈ V:

R

n,m = 1
o
(36)
of nodes aggregated atn. Letφ:R ·×F →R F be a pooling
map that is invariant to permutations of its rows (the pooled
nodes) and acts per feature, e.g.,[φ sum(X)]f = P i[X]i,f for
sum-pooling and[φ max(X)]f = maxi[X]i,f for max-pooling.
In analogy with the graph-filter notationH(S)X, we write
R(S)Xfor the pooled signal,

R(S)X

n =φ

X

n(n)

, n∈ V.(37)
Note that for sum-pooling, this operator form coincides with
the matrix productR(S)X.
Pooling at reduced resolutions.Pooling at the resolutions of
the U-GNN follows the reduced-GSO construction. We define
the node-reduced counterpart ofR,
Rb(S) =D b R(S)D ⊤ b ∈ {0,1}Nb×Nb ,(38)
which intersects theκ b-reach ofSwith the active setΩ b. Like
the reduced GSOs in (15),R b is indexed by the local labels
[Nb]. Also, the rangeκ b is left implicit at depthb, just as the
strideγ b is in (14). We define the set
nb(n) :=
n
m∈[N b] :

Rb

n,m = 1
o
,(39)
which collects the active nodes withinκ b hops ofnonS,
includingnitself. We then pool a down-sampled signalZ∈
RNb×F as

Rb(S)Z

n =φ

Z

nb(n)

, n∈[N b].(40)
In (40),R b(S)Zadmits a lift–pool–reduce form mirroring that
of the strided convolutions. One liftsZto the full vertex set,
pools over theκ b-hop neighborhoods ofS, and reduces back to
Ωb throughD b. The lift assigns each inactive node the identity
element ofφ, so that it leaves the pooled output unchanged.
This element is0for sum-pooling, for which the plainD ⊤ b
suffices, and−∞(a large negative constant in practice) for
max-pooling, supplied by a modified lift eD⊤ b .
Optional placement in the U-GNN.At each encoder depth
b= 1, . . . , B−1, the encoder outputZb is first pooled asR bZb
and then down-sampled byC b+1RbZb, which feeds the block
at depthb+ 1[cf. (19)]. The node selectors use the pooled
features as well, so we replaceZ b withR bZb in (24). Both
stages fold into the definition of the encoding GNN module.
Note that the bottleneck at depthBperforms no node-space
down-sampling or pooling.
15

Encoder block (depth b)
Πb ΦE b (Pb, S; Db, ΘE b )
Ψb(Zb, Db[U0; K0]; Θsel b )
TopK
Vb=CbZb−1
(from depth b−1)
Pb Zb
Zb
vb
[U0; K0] Db
S
×
global embeddings
Db[U0; K0]
↓ Cb+1
Cb+1
↑ C⊤ b+1
Cb+1Zb Yb+1
the rest of the U-GNN
(depths b+1. . .B)
Decoder block (depth b)
Πskip b Πb ΦD b (Pb, S; Db, ΘD b )
C⊤ b+1Yb+1
Vb Pb
[U0; K0] Db
S
×
global embeddings
Db[U0; K0]
Yb
(to depth b−1)
skip Zb
Fig. 2. Block interface (wide), oriented as Fig. 1’s U. Encoder (left): Vb enters at the top
left, the chain Π b → ΦE b → split runs along the top, and Zb exits at the bottom right into
the down-sampler; the learned selector Ψb → TopK is stacked under the split and emits
Cb+1. Junction (centre): the down-sampled Cb+1Zb descends into the elided deep levels
(depths b+1, . . . , B, a small U) and Yb+1 rises back into the up-sampler. Decoder (right):
Πskip b → Πb → ΦD b , with the up-sampled input rising into Π skip b and Yb exiting at the top
right. The skip Zb feeds straight across into Π skip b ; the samplers reuse Cb+1 (transposed). In-
side each block the global embeddings [ U0; K0] and the nested down-sampling Db multiply
(×) to Db[U0; K0] for Π b and Ψb; Db also parametrises Φb, which the graph shift S feeds.
Fig. 7:Block interface of a U-GNN encoder–decoder pair.Encoder (left):The block inputV b=Cb Zb−1 passes through
the fusion layerΠ b and the GNN moduleΦ E b to produceZ b. This feature continues along the skip and also feeds the learned
selectorΨ b. A Top-K readout of the selector scores then yields the selectionsC b+1.Junction (centre):The down-sampled
Cb+1Zb descends into the elided deeper levelsb+1, . . . , B. The returningYb+1 is up-sampled byC ⊤ b+1.Decoder (right):The
skip-projectionΠ skip b combines the up-sampled signal with the encoder skipZ b. The result passes throughΠ b and the GNN
moduleΦ D b , producingY b for depthb−1. In every block, the global embeddings[U 0;K 0], which are restricted to the depth-b
active nodes asD b[U0;K 0], enterΠ b andΨ b. The compositeD b also parametrizes the GNN modulesΦ E b andΦ D b , which
define graph convolutions over the GSOS.
The case for explicit pooling is weak in our design since
the graph convolutional layers in (14) and selector heads
in (24) already provide nonlinear neighborhood aggregation
and learned down-sampling, respectively. In our experiments,
max-pooling added computational overhead without a notice-
able gain. Hence, we adopt (14) as the default GNN operation.
Remark 3.Max-pooling admits a compositional shortcut. By
associativity and the telescoping of iterated neighborhoods,
theκ-reach maximum equalsκapplications of the unit-reach
maximum. This avoids formingR(S)explicitly and reduces
the cost toκsparsescatter_maxcalls. The same property
holds in the reduced domain.
Remark 4.For a regular graph with uniform down-sampling,
a natural CNN analog sets the pooling rangeκ b =κ⌈N/N b⌉,
proportional to the effective down-sampling at depthb, so that
pooling regions cover comparable numbers of active nodes
across resolutions. For an arbitrary graph, the tension that
governs the strideγreappears [cf. Remark 1]. Namely, a too
smallκ b collapsesn b(n)to{n}and reduces pooling to the
identity, whereas a too largeκ b pools broadly overΩ b and
may oversmooth the representation.
APPENDIXE
U-GNN DENOISER ANDDIFFUSIONCONFIGURATION
This appendix expands Table I. In particular, Appendix E.1
details the denoiser, diffusion process, and training shared
across the two tasks, and Appendix E.2 specifies the signal
and conditioning interface particular to each.
A. Shared Denoiser, Diffusion, and Training
Backbone.The denoiserϵ θ is a U-GNN spanningB=4
node resolutions. Each of its3down-sampling levels reduces
the active node set by a factor2, for an2 3=8×reduction
overall and four resolutions ofN,N/2,N/4, andN/8nodes.
Each reduction is realized by a learned node-selection pooling
operator, made differentiable with a straight-through estimator
(Appendix C). To counteract the increasing sparsity of the
coarsened graphs, the graph convolutions are strided, capped at
γmax=2(Appendix B). The feature (channel) width is uniform
at64channels across all levels.
Each encoding and decoding level applies2GNN layers
of orderK=2over powers of the augmented adjacency
I+ ˆA, with channel-wise layer normalization (LayerNorm),
a rectified linear unit (ReLU) nonlinearity, and dropout0.1;
these layers are strided variants of the topology-adaptive graph
convolution (TAGConv), following itsPyGimplementation.
A2-layer bottleneck processes the coarsest summary, and the
decoder path restores full resolution while concatenating the
encoder skip features at each level. The output head applies
LayerNorm, a sigmoid linear unit (SiLU) nonlinearity, and a
linear map. Fig. 7 complements Fig. 2 and shows a detailed
schematic of one encoder–decoder block pair at depthb.
Conditioning and fusion.The diffusion stepkis mapped
to a128-dimensional sinusoidal embedding followed by a
multilayer perceptron (MLP), and the node conditioning to a
128-dimensional representation. Both are projected to the level
width64at every level, where the signal path and the projected
step embedding are concatenated and linearly mapped back to
64channels (128→64). The conditioning is then merged in a
task-specific way: by concatenation into the same projection
for WRA, so that it maps192channels down to64over the
signal, step, and conditioning; and by two-head cross-attention
for S&P 500—queries from the signal path, keys and values
from the conditioning context—which leaves the projection
from128channels down to64.
16

Diffusion.The forward process applies a linearβschedule
from10 −4 to2×10 −2 over500steps. At inference, we sam-
ple using5×-accelerated denoising diffusion implicit models
(DDIM) with100steps and stochasticity parameterη=0.2
(Appendix A). We draw100samples per conditioning input
to form the predictive ensemble.
Optimization.We train for5000epochs with AdamW (learn-
ing rate10 −4,(β 1, β2)=(0.9,0.98), weight decay10 −4),
gradient-norm clipping at1.0, and automatic mixed precision
(AMP). The learning rate follows a per-step cosine schedule
with a linear warm-up over the first1%of training, then a
cosine decay to a floor of5%of the peak over0.8of training,
after which it is held constant. The node-selector temperature
and exploration noise are annealed over roughly the first75%
of training, moving the selector from soft selection toward
nearly hard selection (Appendix C). We retain the best check-
point under a task-specific composite validation criterion. Both
models were trained on a single NVIDIA RTX 3090. The
S&P 500 model completed training in≈58.5GPU hours, and
the WRA model did so in≈33GPU hours.
B. Application-Specific Knobs
Stock-price forecasting (S&P 500).The diffused signal
is the future log-return trajectoryx 0 ∈R N×T p over the
N=468stocks. The pooling cascade coarsens the node set as
468→234→117→58across the four levels. Because returns
are unbounded, the predicted clean signal is left unclipped.
The conditioning comprises12market features over the past
Th-day window. A per-node temporal encoder summarizes
this window and projects theT h history steps onto theT p
horizon steps, forming the per-level context that the cross-
attention fusion above consumes. This encoder interleaves di-
lated 1-D convolutions with two-head temporal self-attention.
A lightweight in-block temporal mixer further couples theT p
horizon steps. The target channel is additionally normalized by
reversible instance normalization (RevIN) [45], using statistics
from the conditioning window. RevIN uses a blend weight of
0.7and a scale correction of1.107.
The model has1.44Mtrainable parameters and is trained
on batches of64sliding windows. We retain the checkpoint
that minimizes a composite of the validation noise loss, its
train–validation gap, and continuous ranked probability score
(CRPS). This checkpoint is reached near epoch4500.
Wireless resource allocation (WRA).The diffused signal is
the centered allocationx 0 =p/P max − 1 2 ∈[− 1 2 , 1 2 ]N over
theN=400transmitter–receiver (tx–rx) pairs. The pooling
cascade coarsens the node set as400→200→100→50. The
powers are recovered asp= clip [0,Pmax]

Pmax(x0 + 1 2 )  . In
contrast to the stock model, the allocation is a single snapshot
with no time axis, soT=1. Thus, the temporal encoder and
in-block mixer are therefore disabled, and RevIN is not used.
The2per-node conditioning features are concatenated into
the level fusion described above. These features are the direct-
link gain and the aggregate cross-link interference. Because the
support is bounded, the predicted clean signal is clipped to the
valid power range at each reverse step.
Target allocations are supplied by a primal–dual expert. The
expert is a shallow GNN with3layers, hidden width64, and
K=2hops, trained per density group with dual-ascent step
0.2. As supervision for the U-GNN, we collect200allocations
per training network from its converged primal iterates. This
yields16000samples in total. Running the same expert on
the held-out networks yields the reference allocations used for
evaluation. Theoretical and algorithmic details appear in [2].
The model has0.63Mtrainable parameters and is trained on
batches of800network graph and resource allocation signal
pairs. We retain the checkpoint that minimizes a composite
of the mean rate-feasibility gap and the1%and5%rate
gaps, averaged over the four density groups. This checkpoint
is reached at epoch1600.
17
