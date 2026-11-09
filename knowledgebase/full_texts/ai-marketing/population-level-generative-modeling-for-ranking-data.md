---
title: Population-Level Generative Modeling for Ranking Data
url: https://arxiv.org/abs/2608.08422
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Zhaoyang Shi
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.08422
pages: 32
chars: 59264
fetched_at: '2026-11-08T13:26:45+00:00'
kb_version: 1
---

# Population-Level Generative Modeling for Ranking Data

Population-Level Generative Modeling for
Ranking Data
Zhaoyang Shi∗
Center for Applied Mathematics, Fudan University
Shanghai, China
Abstract
Ranking data arise in scientific and machine learning applications, including
recommendation systems, information retrieval, voting, marketing, and AI prefer-
ence ranking from human feedback. Existing statistical work has primarily focused
on inference tasks such as preference estimation, rank aggregation, and ranking
prediction. However, generating realistic synthetic rankings from an observed pop-
ulation is important for privacy-preserving data sharing, benchmark construction,
simulation, and uncertainty quantification. This task is challenging because rank-
ings are high-dimensional combinatorial objects with non-Euclidean dependence
structures, while ranking populations often exhibit substantial preference hetero-
geneity. We propose a framework for population-level generative modeling through
a latent preference simplex embedding. It estimates a low-dimensional latent pref-
erence simplex through a likelihood-based ranking model, leverages flow match-
ing to learn the population distribution of latent preferences, and generates new
rankings through the fitted probabilistic ranking model. We show that ranking
generation admits an oracle reduction to latent distribution learning and derive
finite-sample generative guarantees that clarify how the number of items, ranking
length, and latent dimension affect accuracy. Experiments on synthetic and real
∗Corresponding author: zyshi10m@outlook.com
1
arXiv:2608.08422v2  [stat.ME]  11 Aug 2026

datasets demonstrate improved population-level fidelity and provide a statistically
interpretable representation of preference heterogeneity.
Keywords:Generative modeling, Ranking data, Plackett-Luce model, Preference sim-
plex embedding, Flow matching.
1 Introduction
Ranking data are ubiquitous in modern statistical learning and data science. They arise
naturally in recommendation systems (Liu et al., 2025; Chen et al., 2024), information
retrieval (Fang et al., 2024; Chowdhury et al., 2025), online advertising (Qiu et al., 2025;
Yang et al., 2024), preference elicitation (Mukherjee et al., 2024; Li et al., 2025), voting
(Hosseini et al., 2024), marketing (Yin et al.), and, more recently, AI preference ranking
from human feedback (Xiao et al., 2025; Shi et al., 2025), an increasingly important com-
ponent of large language model alignment in which human evaluators rank alternative
model outputs according to preference. Unlike scalar labels or isolated pairwise compar-
isons, ranking data encode relative preferences among multiple competing items within
a single observation and therefore provide a richer description of comparative judgment.
This structured and highly informative nature makes ranking data central to a broad
range of statistical tasks, including preference estimation, consensus analysis, hetero-
geneity modeling, and prediction. Consequently, the statistical modeling and analysis of
ranking data have attracted sustained interest over the past several decades.
Among the broad range of applications and sustained methodological development,
the statistical literature on ranking data has primarily focused on inference problems.
Existing work has largely been devoted to estimating latent preference scores (Fan et al.,
2025; Dong et al., 2026), recovering consensus or population rankings (Zhu et al., 2023;
Chen et al., 2022), modeling heterogeneous preference structures (Mao and Wu, 2022;
Pearce and Erosheva, 2025; Caron et al., 2014), learning ranking models from pairwise
or partial rankings (Chen et al., 2019; Han and Xu, 2025), predicting unobserved or
future rankings and quantifying the associated uncertainty (Dai et al., 2021; Duchi et al.,
2

2013). Classical probabilistic models, including the Plackett–Luce, Bradley–Terry, and
Mallows models together with their numerous extensions, provide the foundation for these
inference tasks.
Despite these developments, a fundamentally different statistical problem has re-
ceived comparatively little attention:population-level generative modeling for ranking
data. Rather than performing an inferential task such as estimating latent preferences
or predicting rankings, the objective is to learn the population-level mechanism underly-
ing ranking behavior and subsequently generate new synthetic rankings from the learned
distribution. Such a capability is increasingly important for privacy-preserving ranking
data synthesis, benchmark construction for evaluating ranking algorithms, uncertainty
quantification through synthetic replications, simulation of complex decision systems,
and scalable preference generation for downstream training, evaluating, and aligning AI
systems.
Formally, consider a collection ofnitems and a population ofmrankers. For each
rankerj= 1, . . . , m, we observe a complete or partial ranking of their preferences overn
items:R j = (ij1 ≻i j2 ≻ · · · ≻ijLj ),where 1≤L j ≤n,i jℓ ∈ {1, . . . , n},and the ranked
items are distinct. The caseL j =ncorresponds to a complete ranking, whileL j < ncor-
responds to a top-L j partial ranking. The observed ranking data areR={R 1, . . . , Rm}.
Throughout, the ranking lengths{L j}m j=1 are treated as design quantities. The rank-
ings are viewed as independent realizations from an unknown population. Given only
{R1, . . . , Rm},our objective is to learn this population and construct a generative model
that, for a prescribed ranking lengthL gen, generates new synthetic rankings eR1, eR2, . . .
from the learned distribution. This problem is more challenging than generative mod-
eling for ordinary Euclidean data. First, rankings are high-dimensional combinatorial
objects with strong structural dependence. A complete ranking ofnitems lies in a
permutation space of cardinalityn!, while a top-Lranking belongs to a space of size
n!/(n−L)!, making direct distributional learning statistically and computationally diffi-
cult. Second, changing the position of one item necessarily alters its ordering relative to
multiple others, meaning ranking coordinates have complex dependence and cannot be
3

modeled independently. Third, real ranking populations are also highly heterogeneous,
with individuals exhibiting distinct preference patterns. These challenges therefore leave
a central statistical question unresolved:
How can we develop accurate generative models for ranking data that preserve the
underlying ranking structure while remaining statistically interpretable?
1.1 Latent preference simplex embedding with flow matching
Our central idea (see details in Section 2) is to represent high-dimensional and het-
erogeneous ranking behavior through a low-dimensional and statistically interpretable
preference simplex. Under the Plackett-Luce model, each rankerjis associated with
a utility vectorq j that determines the distribution of the observed ranking. In many
real-world ranking settings, rankers exhibit a collection of recurring preference types but
weigh them differently when ranking the items. This observation naturally motivates
a simplex representation of the utilityq j in which the vertices stand for latent utilities
corresponding to those preference types and a ranker combines these latent utilities with
different preference weights to form their utilityq j. We embed the observed rankings into
this low-dimensional latent preference simplex by estimating latent utilities and prefer-
ence weights, use flow matching to learn the population distribution of these weights
to generate new preference weights, and decode them into rankings through the fitted
Plackett-Luce model.
The proposed framework possesses several attractive properties. First, it reduces gen-
eration from a high-dimensional ranking space to a low-dimensional preference simplex.
Second, the latent preference simplex provides a direct statistical interpretation in terms
of ranker preferences. Third, the framework separates statistical estimation from gen-
erative modeling, allowing different modern generative models to be incorporated and
thereby providing a flexible and scalable approach.
4

1.2 Related work
A large statistical literature on ranking data focuses on estimating preference parameters,
recovering latent rankings, aggregating rankings, predicting unobserved comparisons, and
quantifying uncertainty. Representative examples are discussed in the Introduction. How-
ever, their inferential target is different and they cannot address the joint problem of
learning the population distribution underlying observed rankings and generating new
rankings from the learned distribution.
Mixture extensions of ranking models accommodate population heterogeneity through
latent components, with each ranker generated from one of several component-specific
ranking models (Murphy and Martin, 2003; Gormley and Murphy, 2008; Mollica and
Tardella, 2017; Zhao et al., 2016; Johnson et al., 2020; Pearce and Erosheva, 2025). Most
of them represent each ranker by one underlying component while a smaller literature
allows continuous latent representation across several preference groups. However, even in
these formulations, the primary goal is inference on latent groups or ranking parameters
rather than generative modeling of the ranking population. In particular, it remains
unclear how to learn a flexible population distribution of ranker preferences from the
observed rankings and use this distribution to generate new rankers with previously
unseen preference profiles.
Low-rank ranking models provide another flexible representation of heterogeneity by
expressing ranker-specific utilityq j through shared low-dimensional latent factors (Park
et al., 2015; Negahban et al., 2018; Wu et al., 2018). These models are primarily developed
for utility estimation, preference completion, or ranking prediction. Moreover, the latent
factors are generally identifiable only up to transformations and therefore do not define
a canonical latent space on which a population distribution can be meaningfully learned
and interpreted. A related limitation appears in classical generative rank models such
as Biernacki and Jacques (2013), which restrict the ranking distribution to a specific
low-dimensional parametric family.
Recent advances in generative AI have produced a wide range of flexible models,
including autoregressive architectures (Germain et al., 2015; Huang et al., 2025), vari-
5

ational autoencoders (Jazbec et al., 2021), flows (Rezende and Mohamed, 2015; Guo
et al., 2025), and diffusion-based methods (Ho et al., 2020). While these approaches pro-
vide powerful general-purpose tools for distribution learning and data generation, their
direct application to ranking data faces several difficulties. Modeling rankings directly
requires learning a distribution over a high-dimensional combinatorial space whose com-
plexity grows rapidly with the number of items. Introducing a generic neural latent
representation can reduce this dimensionality, but the resulting latent coordinates typi-
cally lack both rigorous finite-sample theoretical guarantees and statistically identifiable
interpretation for such a generative modeling of ranking data. Consequently, they do
not directly address the joint statistical problem of estimating heterogeneous ranker pref-
erences, learning their population distribution, and generating new rankings from that
learned population.
These observations identify the gap addressed in this paper. Population-level ranking
generation requires more than either fitting a statistical ranking model or applying a
generic generative model. It requires a representation that is low-dimensional enough to
be estimated from one ranking per ranker, structured enough to admit a statistical inter-
pretation in terms of ranker preferences, and sufficiently flexible to support distribution
learning across a heterogeneous population.
1.3 Notations
LetZ + denote the set of all positive integers. Forn∈Z +, [n] stands for the set{1, . . . , n}
and1 n denotes then-dimensional vector of ones. Fork∈Z +, lete k be the Euclidean
basis vector whosek-th entry is one and the rest entries are zero. For a matrixA,
let∥A∥be its operator norm,∥A∥ F be its Frobenius norm, and∥A∥ max := max ij |Aij|.
For a vectora, use∥a∥for its Euclidean norm and∥a∥ ∞ for itsℓ ∞ norm. We write
N(µ,Σ) for the normal distribution with meanµand covariance matrix Σ. Fora∈R,
let [a] + := max{a,0}. For a vector, [·] + is applied componentwise. For a setA, let|A|
denote its cardinality. We writeA≲B(equivalentlyB≳A) if there exists a constant
C >0 such thatA≤CB. We writeA≍BifA≲BandB≲A.
6

2 Proposed method
2.1 Latent Preference Simplex Embedding (LPSE)
We first recall the Plackett-Luce (PL) ranking model. For rankerj∈[m], letq j =
(qj1, . . . , qjn)⊤ ∈R n denote the utility vector. PL model uses the following sequential
softmax law for the probability of observing a top-L j rankingR j = (ij1, . . . , ijLj ):
P(Rj |q j) =
LjY
ℓ=1
exp(qjijℓ )P
r∈Ajℓ exp(qjr ) ,(1)
whereA jℓ = [n]\ {ij1, . . . , ij,ℓ−1}is the remaining set before theℓth selection.
A fully unrestricted PL model considers unrelated utility vectors{q j}m j=1. Directly
building a generative model on these high-dimensional utility vectors is statistically chal-
lenging. More importantly, our goal is to construct a generative framework that respects
the underlying ranking mechanism while retaining a clear statistical interpretation. To
this end, the key observation is that empirical ranking data are heterogeneous in a struc-
tured way: different users may rank in substantially different ways while these rankings
often exhibit common preference types over the same collection of items. For example,
in movie rankings, some users may consistently place action movies near the top as one
preference type, whereas others may favor comedies or dramas; many users may also
combine such preference types in a single ranking. This observation motivates us to rep-
resent each ranker’s utility vectorq j as a combination of latent utility vectors associated
with some preference types so that each ranker aggregates their preference types when
forming a final ranking.
Formally, leth 1, . . . , hK ∈R n denote latent utility vectors associated withKpref-
erence types for someK∈Z +. For eachk∈[K],h k = (h k1, . . . , hkn)⊤ records latent
utilities ofnitems fork-th preference type. Rankerjaggregates these latent utilities to
form an individual utility vectorq j ∈R n:
qj =
KX
k=1
πjkhk,(2)
7

whereπ jk is the weight of rankerjon their preference typek. Letπ j = (πj1, . . . , πjK )⊤ ∈
∆K−1 := n x∈[0,1] K : PK k=1 xk = 1 o ,where ∆ K−1 is a (K−1) dimensional latent pref-
erence simplex. Each vertexh k represents a pure preference type such as action movies,
comedies, and dramas in the above movie ranking example. To see how this simplex rep-
resentation recovers the preference-type interpretation, consider two itemsa, b∈[n]. For
any two itemsaandb, letP j(a≻b) andP j(b≻a) denote the probabilities that ranker
jranksaabovebandbabovea, respectively. Under the PL model (1), the pairwise
preference probability is a logistic function of the utility differenceq ja −q jb:
log Pj(a≻b) Pj(b≻a) =q ja −q jb (2) =
KX
k=1
πjk(hka −h kb).
For preference typek, the utility differenceh ka −h kb measures how strongly that type
favorsaoverb: it is positive when the type tends to rankaaboveb, negative when it
tends to rankbabovea, and larger in magnitude when the preference is stronger. The
weightπ jk reflects how much this utility difference under preference typekcontributes
to rankerj’s tendency to rank itemaabove itemb.
LPSE is reminiscent of topic models and latent-factor models in that ranker utilities
are represented as a collection of latent utilities. Its geometry, however, is different. In
topic models, each topic is typically a nonnegative probability vector with a common
unit-sum normalization while our latent utilities are signed vectors, and only their utility
differences are relevant.
2.2 Likelihood-based estimation of the latent preference sim-
plex
LetQ= [q 1, . . . , qm],H= [h 1, . . . , hK] and Π = [π 1, . . . , πm] withQ=HΠ. We first
address the identifiability issue of the model parameters before we estimate (Π, H).
The PL probabilities depend only on utility differences: for anya∈R K, defineH (a) =
H+1 na⊤.For rankerjand itemi,q (a) ji =π ⊤ j h(a) i =π ⊤ j hi +π ⊤ j a=q ji +π ⊤ j a.All utilities
of rankerjare shifted by the same constant such thatP(R j |π j, H(a)) =P(R j |π j, H).
8

It implies that the likelihood is consequently invariant to arbitrary row-wise shifts of
H. We then impose a condition onH: (C1)H ⊤1n =0.For the preference simplex
parameter (Π, H), we consider the conditions: (C2) For each preference typek∈[K],
there exists a pure rankerj k (i.e.,π jk =e k); (C3){h k}K k=1 are affinely independent.
Under Conditions (C1)-(C3), all parameters are identifiable (up to a permutation if not
pre-labeled and we will omit this permutation for notational convenience; see Proposition
2 in the supplementary material).
Remark1.Condition (C3) means PK k=1 αkhk =0and PK k=1 αk = 0 imply allα k’s are
zero. It ensures every utility vectorq j admits a unique convex representation in (2) by
h1, . . . , hK. This condition is weaker than rank(H) =Kin density mixture model (Fan
et al., 2026) and DCMM network model (Jin et al., 2024).
Remark2.Condition (C2) ensures that pure rankers serve as labeled anchors to identify
the latent preference simplex. This condition is analogous to the pure-node condition in
mixed-membership network models (Jin et al., 2024) and the anchor-region assumption
in density mixtures (Fan et al., 2026). It can be relaxed toϵ-pure ranker, where the
distance of someπ jk toe k is bounded byϵ=o(1). There are some other identifiability
conditions such as sufficiently scattered condition (Huang and Fu, 2019) and volume-
minimization identifiability (He, 2023). We choose Condition (C2) as it is simple and
statistically interpretable.
In LPSE, each vertex is a column of the latent utility matrixHand each column of the
utility matrixQis a convex combination of all the vertices. This geometry motivates the
use of vertex recovery on{q j}m j=1 to recover the vertices{h k}K k=1. SinceQis unknown, we
propose a constrained likelihood method to estimateQand then apply a vertex recovery
algorithm to estimateHand Π. Given the observation ranking dataR={R 1, . . . , Rm},
the log-likelihood of the PL model in (1) is
ℓ(Π, H) := logP(R |Π, H) =
mX
j=1
LjX
ℓ=1

π⊤ j hijℓ −log

 X
r∈Ajℓ
exp(π⊤ j hr)



 .
We defineS K,m =

Π = [π1, . . . , πm]∈R K×m :π j ∈∆ K−1 for everyj∈[m] 	 andH n,K =
9


H= [h 1, . . . , hK]∈R n×K :H ⊤1n =0,∥H∥ max ≤B 	 for some constantB >0, and con-
sider the constrained maximum likelihood estimator
max
Π∈SK,m,H∈H n,K
mX
j=1
LjX
ℓ=1

π⊤ j hijℓ −log



X
r∈Ajℓ
exp(π⊤ j hr)




 .(3)
Let ( eΠ, eH) be a solution to (3) and bQ= eH eΠ. We also define
Qn,m,K :={Q=HΠ :H∈ H n,K,Π∈ SK,m}.
Since the log-likelihood depends on (H,Π) only through their productQ, it is seen that bQ
is also an MLE of the utility matrixQwith likelihoodℓ(Q) over the setQ n,m,K. However,
( eH, eΠ) is not necessarily a consistent estimator of (H,Π) since the factorization ofQis
not uniquely determined by the likelihood. Indeed, letA∈R K×K be invertible with
A1K =1 K.For any feasible pair (Π, H), define Π ′ =AΠ andH ′ =HA −1.Whenever
Π′ ∈ SK,m andH ′ ∈ Hn,K, it always holds thatH ′Π′ = (HA −1)(AΠ) =HΠ and
ℓ(Π′, H′) =ℓ(Π, H).The pair ( eΠ, eH) is regarded only as a preliminary factorization to
obtain the estimator bQ.
To obtain an estimator for (H,Π), we then apply a vertex recovery algorithm to bQto
obtain an estimator bH. An estimator bΠ is subsequently obtained from the barycentric
coordinates of the columns of bQrelative to the estimated vertices as the columns of bH.
Here we treat vertex recovery as a generic plug-in step in our method. Possible candidates
could be Successive Projection (SP) (Ara´ ujo et al., 2001), Sketched Vertex Search (SVS)
and its variant SVS∗ (Jin et al., 2024). We pick SVS due to its additional denoising step.
See more details in Section D.1.2 in the supplementary material. Operationally, SVS first
applies a denoising step: given a tuning integerM S ≥K, partition the columns{ˆq j}m j=1
intoM S clusters byk-means and denote the resulting local centers by ˆm1, . . . ,ˆmMS . Then,
it selectsKdistinct centers whose convex hull best approximates allLlocal centers:
(ˆj1, . . . ,ˆjK)∈arg min
1≤j1<···<jK ≤MS
max
1≤ℓ≤L
dist( ˆmℓ,conv{ˆmj1, . . . ,ˆmjK }),
10

and sets bH= [ ˆmˆj1, . . . ,ˆmˆjK ].After using SVS to estimateH, we propose to recover Π
by barycentric coordinates. Let bD= [ ˆh1 − ˆhK, . . . ,ˆhK−1 − ˆhK].For eachj∈[m], we first
compute the barycentric coordinateseaj = ( bD⊤ bD)−1 bD⊤(bqj − bhK),and set ˜πj = (˜a⊤ j ,1−
1⊤ K−1 ˜aj)⊤.The final weight estimator is obtained by truncation and renormalization:
ˆπj = [˜πj]+
1⊤ K[˜πj]+ , bΠ = [ˆπ1, . . . ,ˆπm],
where fora∈R, [a] + := max{a,0}and for a vector, [·]+ is applied componentwise.
Remark3.One could enforce the pure ranker condition, or another identifiability con-
dition as stated in Remark 2 directly in the likelihood optimization. However, such
constraints are combinatorial or globally geometric and would substantially complicate
both theoretical analysis and computation of MLE with additional tuning and bias. Our
method separates estimation from identification.
Remark4.The latent dimensionKdetermines both the number of preference types
and the dimension of the generative model trained in the next subsection. It may be
selected using held-out PL likelihood/cross-validation (CV) (Stone, 1974; Geisser, 1975),
or information criteria (Mollica and Tardella, 2017). In the numerical studies, we select
Kusing training-based model selection with an empirical screening. Details are provided
in Section D.3 in the supplementary material.
2.3 Flow matching on the latent preference simplex
LPSE serves as the key representation on which our generative framework is built. Rather
than directly modeling the highly combinatorial ranking distribution (or through then-
dimensional utility vectors{q j}m j=1), we reduce the problem to learning and generating the
unknown population distribution of theK-dimensional barycentric coordinates{π j}m j=1.
Formally, we regard the observed preference weights{π j}m j=1 as one realization from an
underlying population lawP π supported on the latent preference simplex:{π j}m j=1 i.i.d. ∼P π,
whereP π ∈ P(∆K−1).Under this interpretation, the ranking distribution admits the
11

hierarchical representation
πj ∼P π, q j =Hπ j, R j |π j, H∼PL Lj (Hπ j),(4)
where the PL Lj (·) denotes the law given by the PL model (1). This hierarchical rep-
resentation motivates the followingLatentPreferenceSimplexEmbedding withFlow
Matching method (LPSE-FM, also see Algorithm 1):
1. Estimate the latent preference geometry ( bΠ, bH) by constrained maximum likeli-
hood in (3) and vertex recovery. Then hold bHfixed and regard{ˆπ j}m j=1 as noisy
observations from the unknown populationP π.
2. We build a generative model bPπ ≈P π and obtain generated barycentric coordinates
{˜πj}j≥1
i.i.d.
∼ bPπ.
3. Compute generated utility vectors ˜qj = bH˜πj and generate the synthetic ranking by
eRj |˜πj, bH∼PL Lgen( bH˜πj).
For step 2, we use flow matching to build a generative model bPπ. Thus, the likelihood-
based estimation in Section 2.2 is formulated conditionally on the configuration Π, whereas
Pπ provides the population-level model used to learn and generate out-of-sample prefer-
ence weights.
Flow matching (Lipman et al., 2022) has recently emerged as one of the leading
paradigms for deep generative modeling and achieved state-of-the-art performance across
a wide range of generative modeling tasks. See Lipman et al. (2024) for more details.
Since our latent distributionP π lies in the simplex ∆ K−1, we apply an additive log-
ratio transformation of the simplex and then adopt a standard flow matching framework.
Formally, define the log-ratio transformation
T: ∆ K−1 →R K−1, T(π) =

log π1
πK
, . . . ,logπK−1
πK
⊤
.(5)
Let the pushforward distribution beP Z :=T #Pπ =P π ◦T −1.We first fixP 0 =N(0, I K−1)
as a simple reference distribution. LetZ 0 ∼P 0 andP Z be our target distribution.
12

Flow matching aims to learn a time-dependent vector field, called the velocity field,
v∗ :R K−1 ×[0,1]→R K−1 through a neural network estimator and considers solving the
ODE
dZt
dt =v ∗(Zt, t), Z 0 ∼P 0,(6)
such that the solution att= 1 satisfiesZ 1 ∼P Z. There can be many such velocity fields.
Flow matching proceeds by choosing a convenient pathZt = (1−t)Z0+tZ1 ∼P t, t∈[0,1].
Along this path, the velocity field in (6) is a conditional meanv ∗(x, t) =E[Z1 −Z 0 |Z t =
x].To estimate it, given target observations{ˆz j}m j=1 with ˆzj =T(ˆπj) defined in (5), the
empirical loss becomes an MSE of regression:
bLFM(θ) = 1 m
mX
j=1
Et∼Unif[0,1],Z0

∥vθ((1−t)Z 0 +tbzj, t)−(bzj −Z 0)∥2 .(7)
We regress the neural velocity fieldv θ((1−t)Z 0 +tˆzj, t) towards ˆzj −Z 0 to obtain ˆθand
the learned velocity fieldv ˆθ. Let bΦt(z0) denote the exact solution at timetto the fitted
flow-matching ODE
dZt
dt =v ˆθ(Zt, t), Z 0 =z 0,(8)
and write bΦt :R K−1 →R K−1 for the corresponding exact flow map. To solve (8) nu-
merically, we use the explicit Euler scheme withNequally spaced time steps. Let the
step sizeh=N −1 for someN∈Z + andt k :=khfork= 0, . . . , N.For any initialization
z0 ∈R K−1, define bΦ(N) 0 (z0) :=z 0 and, recursively,
bΦ(N) tk+1(z0) = bΦ(N) tk (z0) +h vˆθ

bΦ(N) tk (z0), tk

, k= 0, . . . , N−1.(9)
Thus, bΦ(N) 1 is the numerical approximation of the exact flow map bΦ1 in practice. Then
the flow matching distribution estimator ofP Z is bP(N) Z,m :=  bΦ(N) 1  # P0.Equivalently, if
Z0 ∼P 0, then bΦ(N) 1 (Z0)∼ bP(N) Z,m.Finally, we estimate the latent preference distribution
13

Pπ and generate preference weights by{˜πj}j≥1:
bP(N) π,m := (T −1)#bP(N) Z ,˜π j =T −1

bΦ(N) 1 (Z0,j)  , j≥1,(10)
whereZ 0,1, Z0,2, . . .
i.i.d.
∼P 0 such that ˜π1,˜π2, . . .
i.i.d.
∼ bP(N) π,m and the inverse log-ratio map
T −1(z) = (ez1, . . . , ezK−1 ,1) ⊤
1 + PK−1 k=1 ezk , z= (z 1, . . . , zK−1)⊤ ∈R K−1.
Remark5.Note that the log-ratio mapTis applied to ˆπ j(k)/ˆπj(K). For stability, when
the MLE gives simplex coordinates close to zero, we can follow a common practice as in
deep neural network training (Koloskova et al., 2023) to apply a clipping mapCτ (ˆπj)(k) =
max{ˆπj(k), τ}/PK k=1 max{ˆπj(k), τ}fork∈[K] with a small thresholdτ >0.
Algorithm 1Latent Preference Simplex Embedding with Flow Matching (LPSE-FM)
1:Input:Observed rankingsR, the number of preference typesK, the length and the
number of rankings to be generatedL gen andm gen, respectively.
2:Latent preference estimation:Compute the constrained maximum likelihood
estimator ( eH, eΠ) and the utility estimator bQ= eH eΠ.
3:Preference simplex recovery:Apply vertex recovery to bQto obtain the esti-
mated latent utility matrix bH= [ ˆh1, . . . ,ˆhK],and the preference weight matrix
bΠ = [ˆπ1, . . . ,ˆπm].
4:Flow matching:Train a log-ratio-based flow matching on{ˆπ j}m j=1 and obtain an
estimated latent preference distribution bP(N) π,m.
5:Ranking generation:Generate{˜π j}mgen j=1 i.i.d. ∼ bP(N) π,m,set ˜qs = bH˜πs,and independently
sample eRs |˜πs, bH∼PL Lgen(˜qs),fors∈[m gen].
6:Output:{ eRs}mgen s=1 i.i.d. ∼ bPR and{˜πj}mgen j=1 (for interpretation).
Remark6.Our latent distributionP π lies in the simplex ∆K−1. One alternative approach
is to use recently developed manifold flow-matching methods (Chen and Lipman, 2024;
Cheng et al., 2024). When applied to the probability simplex, however, these approaches
typically endow the simplex with a non-Euclidean geometry, for example, via the square-
14

root embedding into the positive orthant of the unit sphere, and construct flows along
the corresponding geodesics, leading to additional computational complexity.
3 Theoretical properties
For any ranking lengthℓ∈[n], define the population joint distributionP (ℓ) (R,π) throughπ∼
Pπ,R|π∼PL ℓ(Hπ),and letP (ℓ) R denote its marginal ranking distribution. Generally, for
any probability measureP π′ on the simplex ∆ K−1 and latent utility matrixH ′ ∈R n×K,
defineP (ℓ) (R′,π′) throughπ ′ ∼P π′, R′ |π ′ ∼PL ℓ(H ′π′),and letP (ℓ) R′ denote the corresponding
marginal ranking distribution. In particular, takingP π′ = bP(N) π,m, H′ = bHandR ′ = eR,
gives the LPSE-FM generated ranking distributionP (ℓ) eR .
We first establish a result showing in the oracle case, our LPSE-FM reduces the
generation from high-dimensional ranking data to the preference weights in the low-
dimensional preference simplex.
Proposition 1(Oracle KL reduction).IfH=H ′, then
KL

P(ℓ) R
 P(ℓ) R′  ≤KL  P(ℓ) (R,π)  P(ℓ) (R′,π′)  = KL(Pπ ∥P π′),
whereKL(·||·)denotes the Kullback-Leibler (KL) distance.
We next present the error rates when (Π, H) is unknown. The analysis consists of
two parts: the rate for the constrained MLE and the rate for vertex recovery.
Theorem 2(Rate of the restricted PL MLE).SupposeL j ≍Lforj∈[m]. The restricted
maximum likelihood estimator bQsatisfies
1
mn ∥ bQ−Q∥ 2 F =O P
 K
L + Kn mL  log(mnL)  .
To accommodate a broad class of plug-in vertex recovery procedures, we introduce a
generic stability condition; any procedure satisfying this condition can be used for our
theoretical analysis. In particular, stability properties of this form are established in Jin
et al. (2024) for the Sketched Vertex Search (SVS) and its variant SVS ∗.
15

Condition 1.For any noisy observationQ ⋆ = [q⋆ 1, . . . , q⋆ m]∈R n×m,letH ⋆ = VR(Q⋆)∈
Rn×K be the output of the vertex recovery. We say the vertex recovery is stable in
Frobenius norm if there exists a constantC VH >0 such that
1
n ∥H ⋆ −H∥ 2 F ≤C VH 1 mn ∥Q⋆ −Q∥ 2 F .
Theorem 3(Recovery of the LPSE).Under the setting of Theorem 2, assume there exist
constants0< c H ≤C H <∞and0< c Π ≤C Π <∞such that
cHIK ⪯ 1 n H ⊤H⪯C HIK, c ΠIK ⪯ 1 m ΠΠ⊤ ⪯C ΠIK,(11)
whereA⪯BmeansB−Ais positive semidefinite. Suppose the vertex recovery satisfies
Condition 1 andK(m+n) log(mnL) =o(mL). Then bD⊤ bDin the vertex recovery step
is invertible with probability tending to one, and
1
n ∥ bH−H∥ 2 F + 1 m ∥bΠ−Π∥ 2 F =O P
 K
L + Kn mL  log(mnL)  .
Remark7.In the balance condition (11), the Gram matrixn −1H ⊤Hcontrols the sepa-
ration and relative scale of theKlatent preference types, whilem −1ΠΠ⊤ controls how
broadly the rankers’ weight vectors span the corresponding preference directions. To-
gether, they exclude degenerate situations in which some preference types are nearly
indistinguishable or receive vanishingly little representation in the population.
Finally, we establish the error rate of our population-level generative modeling. Recall
thatP π denotes the probability measure from which{π j}m j=1 are sampled and that bP(N) π,m
denotes the learned distribution by flow matching defined in (10). Let eP(N) π,m denote the
oracle flow matching distribution of bP(N) π,m, obtained by{π j}m j=1 instead of{ˆπj}m j=1. We
decompose the generative modeling error measured by 1-Wasserstein metric:
W1

bP(N) π,m,P π

≤W 1

bP(N) π,m, eP(N) π,m

| {z }
estimation error
+W 1

eP(N) π,m,P π

| {z }
flow matching error
.
16

Theorem 4(Wasserstein estimation error).Under the setting of Theorem 3, we have:
W1

bP(N) π,m, eP(N) π,m

=O P
"s K
L + Kn mL  log(mnL) # .
For the flow matching error, we make the following standard assumptions (Zhou and
Liu, 2025; Fukumizu et al., 2025; Silveri et al., 2024; Tsimpos et al., 2025).
Assumption 1(Lipschitz neural velocity).For some constantsL v, Bv >0, the neural
velocity fieldv θ in (7) satisfies
∥vθ(x, t)−vθ(y, s)∥ ≤Lv(∥x−y∥+|t−s|),sup
t∈[0,1]
∥vθ(0, t)∥ ≤Bv.
Assumption 2(Oracle velocity estimation error).Letv orc ˆθ denote the oracle learned
velocity field ofv ˆθ in (7), obtained by{π j}m j=1 instead of{ˆπj}m j=1. Then
Z 1
0
EZ∼Pt
hvorc ˆθ (Z, t)−v∗(Z, t) 2i dt=O P  ε2 FM  .
Assumption 3(Moment condition on the latent preference distribution).
M2,π :=E π∼Pπ

∥logπ∥ 2 =E π∼Pπ
" KX
k=1
(logπ k)2
#
<∞,
where the logarithm is applied componentwise.
Remark8.Assumption 1 is mild by enforcing norm-constrained neural networks and
ensures stability of the learned flow. Assumption 2 assumesL 2 consistency of the oracle
learned velocity field as an estimator of the true velocity field. We will discuss the error
εFM later. For Assumption 3, flow matching requires a finite second moment of the
target distributionE Z∼PZ ∥Z∥ 2 withZ=T(π) andTas the log-ratio map. The log-
moment condition onP π provides a simple sufficient condition for this requirement and
is satisfied by common mixture distributions such as Dirichlet distribution and logistic-
normal distributions.
17

Theorem 5(Flow matching error).Suppose Assumptions 1, 2, and 3 hold. Then
W1

eP(N) π,m,P π

=O P

εFM +N −1 .
To present the final error rate of the proposed LPSE-FM method, we introduce the
1-Wasserstein distance induced by the normalized Kemeny-Snell distance commonly used
in the ranking literature. For a rankingr∈ R n and distinct itemsa, b∈[n], we regard
every ranked item as preceding every unranked item, while all unranked items are tied.
Lets r(a, b) = 1 ifais ranked abovebinr,s r(a, b) =−1 ifbis ranked abovea, and
sr(a, b) = 0 if both are unranked. The normalized Kemeny-Snell distance is
d(1/2) τ (r, r′) =
n
2
−1 1
2
X
1≤a<b≤n
|sr(a, b)−sr′(a, b)|.
For probability measuresµ, ν∈ P(Rn), define
W1,τ (µ, ν) = inf γ∈Γ(µ,ν)
Z
dτ (r, r′)dγ(r, r′).
Theorem 6(Wasserstein LPSE-FM error).Suppose the assumptions of Theorems 3, 4,
and 5 hold. Then
W1

Pπ, bP(N) π,m

+ sup
ℓ∈[n]
W1,τ

P(ℓ) R ,P (ℓ) eR

=O P
"s K
L + Kn mL  log(mnL) +ε FM +N −1 # .
Furthermore, if the step size of the numerical ODE solver(9)satisfiesN −1 =O hq K L + Kn mL  log(mnL) +ε FM i ,
then
W1

Pπ, bP(N) π,m

+ sup
ℓ∈[n]
W1,τ

P(ℓ) R ,P (ℓ) eR

=O P
"s K
L + Kn mL  log(mnL) +ε FM # .(12)
Remark9.The final error rate (12) consists of two types of errors. The estimation error
q K
L + Kn mL  log(mnL) arises from replacing{π j}m j=1 by their estimates{ˆπj}m j=1. The flow
18

matching errorε FM depends on the sample sizem, the smoothnesss >0 of the density
of the target distributionP π and the dimensionK−1. We defer its detailed analysis
to Section B in the supplementary material, where we show the flow matching error
=O P

m− s 2s+K−1  .
4 Numerical experiments
This section evaluates the proposed population-level generative framework on both syn-
thetic and real ranking datasets. We compare our LPSE-FM method with two baselines:
(i) Gaussian process variational autoencoders (GPV AE) (Jazbec et al., 2021), which
learns a Gaussian process latent model by maximizing the ELBO (evidence lower bound)
using a variational posterior over the latent variables; after training, new observations
are generated by sampling latent variables from the fitted Gaussian process model and
passing them through a decoder; (ii) Gaussian mixture variational autoencoders (GM-
V AE) (Lee et al., 2021), which learns a Gaussian mixture latent model by maximizing the
ELBO with variational posteriors over both the mixture label and the continuous latent
variable; after training, new observations are generated by sampling a latent variable
from the fitted Gaussian mixture, and passing it through a decoder. For all methods, we
evaluate the fidelity of the generated ranking data through two metrics.
1.Top-five frequency error.For a collectionAof rankings, letf i(A) denote the
proportion of rankings inAin which itemiappears among the first five positions.
We define
∆Top5 =
"
1
n
nX
i=1

fi( eR)−f i(R)
2
#1/2
,(13)
where eRdenotes the generated ranking sample.
2.Pairwise preference error.For distinct itemsa, b, letW ab(A) denote the pro-
portion of rankings inAin whichais ranked ahead ofb. We define
∆Pair =
"
1
n(n−1)
X
a̸=b

Wab( eR)−W ab(R)
2
#1/2
.(14)
19

We use the same batch size and the same number of iterations across all methods.
All methods generate the same number of synthetic rankings for evaluation. The above
metrics are reported by averaging over five independent runs. The code is available
athttps://github.com/10Mzys/LPSE-FM. Additional background and implementation
details are deferred to Section D in the supplementary material.
4.1 Synthetic data
We generate complete rankings ofnitems frommrankers. Each ranking contains all
L= 60 items. We setK= 3 so that each rankerjis represented by a preference weight
πj = (π j1, πj2, πj3)⊤.LetC j ∼Categorical(0.20,0.20,0.20,0.25,0.15).Defineg 4(t) =

(1−c t)t,(1−c t)(1−t),c t
⊤
,c t = 0.18 sin 2(πt) andg 5(t) =  0.20 + 0.55t,0.20 +
0.25 sin2(πt),0.60−0.55t−0.25 sin 2(πt) ⊤ .Forc= 1,2,3,
πj |C j =c∼Dirichlet (0.351 3 + 17.65ec),
and
πj =



g4(Tj) + 0.015ξj
1⊤(g4(Tj) + 0.015ξj) , C j = 4,
0.92 [g5(Tj)]+
1⊤[g5(Tj)]+ + 0.08ζj, C j = 5.
where
Tj |C j =c∼



Beta(0.7,0.7), c= 4,
Unif(0,1), c= 5,
ξj ∼Dirichlet(1 3), ζ j ∼Dirichlet(21 3).
To constructH∈R K×n, partition{1, . . . , n}intoKdisjoint blocksB1, . . . , BK of ap-
proximately equal size. Letε ki
i.i.d.
∼N(0,0.25 2) and define
H (0) ki =ε ki + 2.51(i∈B k)− 2.5 K−1 1(i /∈Bk), H ki =H (0) ki − 1 n
nX
r=1
H (0) kr .
Finally, a rankingR j = (ij1, . . . , ijL) is generated from the PL model (4).
20

Table 1: Generative performance under different values ofmandnmeasured by ∆ Top5
and ∆Pair.
m= 600 m= 1200
Method n= 60 n= 120 n= 60 n= 120
∆T op5 ∆Pair ∆T op5 ∆Pair ∆T op5 ∆Pair ∆T op5 ∆Pair
LPSE-FM 0.0155 0.0232 0.0119 0.0458 0.0111 0.0195 0.0080 0.0388
GPV AE 0.0186 0.0402 0.0162 0.0595 0.0113 0.0217 0.0143 0.0568
GMV AE 0.0160 0.0314 0.0157 0.0614 0.0120 0.0227 0.0138 0.0561
We consider a settingm∈ {600,1200},n∈ {60,120}and generatemrankings. The
performance metrics are reported in Table 1. Overall, LPSE-FM consistently achieves
the smallest ∆ Top5 error across all simulation settings, although the improvement over
GPV AE and GMV AE is relatively modest. However, LPSE-FM exhibits a substantially
larger advantage in ∆ Pair error. This indicates that it more accurately captures the
dependence structure among items rather than merely their marginal frequencies. Since
pairwise preference probabilities summarize the relative ordering between every pair of
items, this metric provides a much more stringent assessment of the underlying ranking
distribution. Additional experiments under other settings of (m, n, K) are provided in
Section E.1 in the supplementary material.
To show the interpretability of our LPSE-FM method, the generated preference weight
˜πj ∈∆ 2 can be visualized on a 2D estimated preference simplex. Each point corresponds
to one generated preference weight, while the three vertices represent the pure prefer-
ence types. To assign semantic meanings to the vertices, for vertexk, we rank the items
according to bHki and label the vertex using the two items with the largest estimated utili-
ties. In Figure 1, the three vertices are labeled by{Item 17,Item 24},{Item 71,Item 44},
and{Item 108,Item 81}under (m, n) = (1200,120). Points close to a vertex represent
rankers dominated by one preference type, and other points reflect contributions from
mixed preference types. A complete list of the leading items and their estimated utility
scores are in Table 2.
21

Vertex 1
Item 17 / Item 24
Vertex 2
Item 71 / Item 44
Vertex 3
Item 108 / Item 81
Figure 1: Generated preference weights on the estimated preference simplex by LPSE-
FM under (m, n) = (1200,120).
Table 2: Interpretation of the generated preference weights under (m, n) = (1200,120).
For each estimated vertex, the table reports its semantic label (defined by the two highest-
utility items) and the six items having the largest estimated utilities and their utility
scores.
Vertex Semantic label Top item indices Top utility scores
1 (17, 24) 17, 24, 9, 7, 6, 12 2.818, 2.807, 2.747, 2.736, 2.616, 2.582
2 (71, 44) 71, 44, 46, 64, 65, 74 2.875, 2.781, 2.763, 2.736, 2.640, 2.599
3 (108, 81) 108, 81, 86, 93, 119, 99 3.515, 3.260, 3.191, 3.073, 2.975, 2.898
4.2 Sushi preference dataset
We evaluate LPSE-FM on the Sushi Preference Dataset (Kamishima, 2003), available at
https://www.kamishima.net/sushi/. The dataset contains complete preference rank-
ings collected from 5000 individuals over a common set of ten sushi types, using both
five-point ratings and ranking responses.
We randomly split the data into 4000 training rankings and 1000 testing rankings. For
all methods, we generatem gen ∈ {500,1000}rankings.K= 4 is selected by minimizing
the model-selection criterion using the training data. Additional experiments under other
settings ofm gen are included in Section E.2 in the supplementary material.
Table 3 shows the performance metrics. Overall, LPSE-FM consistently achieves the
smallest ∆Top5 error and ∆Pair error under both settings. While GMV AE performs better
than GPV AE and closer to LPSE-FM, our method achieves a substantially smaller ∆Pair
error, indicating that LPSE-FM more faithfully preserves the underlying dependence
22

Table 3: Generative performance on the Sushi preference dataset for different numbers
of generated rankingsm gen measured by ∆ Top5 and ∆Pair.
mgen = 500 mgen = 1000
Method ∆Top5 ∆Pair ∆Top5 ∆Pair
LPSE-FM 0.03368 0.04057 0.03520 0.04414
GPV AE 0.12767 0.13683 0.12296 0.13277
GMV AE 0.05955 0.06169 0.05641 0.05943
Table 4: Interpretation of the generated preference weights for the Sushi preference
dataset underm gen = 1000. For each vertex, the table reports its semantic label, the
five sushi types with the largest estimated utilities, and the corresponding utility scores.
Vertex Semantic label Top sushi Top utility scores
1 (ebi, uni) ebi, uni, anago, ika, ikura 1.093, 0.913, 0.904, 0.564, 0.454
2 (maguro, tamago) maguro, tamago, toro, ebi, ika 2.817, 2.659, 1.199, 1.034, 0.784
3 (tamago, tako) tamago, tako, maguro, anago, toro 3.028, 2.602, 1.464, 0.672, 0.305
4 (uni, tamago) uni, tamago, tako, maguro, ebi 4.137, 3.666, 1.509, 0.686, -0.563
structure among rankings rather than only marginal item frequencies. Also, the perfor-
mance of all three methods changes only slightly asm gen increases, suggesting that the
evaluation is stable with respect to the number of generated rankings. For interpretabil-
ity, Figure 2(a) gives a substantive interpretation of the generated preference weights
among the four preference types of sushi underm gen = 1000. Vertex 1 is characterized
byebi(shrimp) anduni(sea urchin), suggesting a preference type towards distinctive
seafood flavors. Vertex 2 is characterized bymaguro(tuna) andtamago(egg), repre-
senting a more conventional type that combines a widely preferred fish item with a mild,
non-fish alternative. Vertex 3 emphasizestamagoandtako(octopus), corresponding to
a type that favors comparatively mild or firm-textured items rather than rich fish vari-
eties. Vertex 4 is characterized byuniandtamago, reflecting a contrasting combination
of the rich, distinctive flavor of sea urchin and the mild sweetness of egg. Interestingly,
tamagoappears among top two flavors in three of the four types. This indicates that the
preference simplex separates consumers primarily through their secondary preferences
while identifyingtamagoas a commonly favored item. Also, the broad interior disper-
sion in the simplex suggests that sushi preferences are better represented by mixtures of
interpretable tastes than by four separated clusters. More details are provided in Table
4.
23

Vertex 1
ebi / uni
Vertex 2
maguro / tamago Vertex 3
tamago / tako
Vertex 4
uni / tamago
(a) Sushi
Vertex 1
Candidate 2 / Candidate 5
Vertex 2
Candidate 1 / Candidate 5
Vertex 3
Candidate 3 / Candidate 1 (b) APA election
Figure 2: Generated preference weights on the estimated preference simplices for (a) the
Sushi preference dataset and (b) the APA presidential election dataset, withmgen = 1000.
4.3 PrefLib APA election data
We also consider the APA presidential election dataset from the PrefLib preference reposi-
tory (Mattei and Walsh, 2013), available athttps://preflib.github.io/PrefLib-Jekyll/
dataset/00028. It contains the results of the elections of the American Psychological
Association (APA) between 1998-2009. Voters submitted ordinal preferences over five
candidates, allowing the electorate to be represented through rank-order ballots. The
APA election data have consequently been used to study whether an organization exhibits
a coherent collective preference or instead displays the kinds of aggregation difficulties
highlighted in social-choice theory.
We use theAPA 2000profile distributed through PrefLib. The original profile con-
tains 20239 voters and five alternatives. Ballots are stored in weighted form, with each
distinct ranking accompanied by the number of voters who submitted it; we expand these
multiplicities to obtain individual ranking observations. We retain the complete strict
rankings so that each observation is a permutation of the same five candidates. For
this common-alternative candidate structure, a generative model must respect both the
marginal tendency of candidates to appear near the top of the ballot and the pairwise
ordering frequencies across the electorate. We randomly partition the expanded rankings
into 4000 training observations and 1000 testing observations. LPSE-FM and both base-
line methods are fitted using only the training rankings and generatem gen ∈ {500,1000}
24

Table 5: Generative performance on the APA presidential election dataset for different
numbers of generated rankingsm gen measured by ∆ Top2 and ∆Pair.
mgen = 500 mgen = 1000
Method ∆Top2 ∆Pair ∆Top2 ∆Pair
LPSE-FM 0.05602 0.05200 0.042880.03974
GPV AE 0.05798 0.05641 0.041470.04886
GMV AE 0.07245 0.06476 0.07169 0.05959
Table 6: Interpretation of the generated preference weights for the APA presidential
election dataset underm gen = 1000. For each vertex, the table reports its semantic label,
the five candidates with the largest estimated utilities, and the corresponding utility
scores.
Vertex Semantic label Top candidate indices Top utility scores
1 (2, 5) 2, 5, 3, 4, 1 2.469, 2.034, 1.920, -1.515, -4.909
2 (1, 5) 1, 5, 2, 4, 3 2.952, 2.374, 1.164, -1.865, -4.626
3 (3, 1) 3, 1, 4, 5, 2 5.897, 3.552, 1.735, -5.450, -5.733
rankings.K= 3 is selected by minimizing the model-selection criterion using the training
data. Since the dataset contains only five candidates, we replace ∆ Top5 error with ∆ Top2
error. Additional experiments under other settings ofm gen are included in Section E.3 in
the supplementary material.
Table 5 reports the generative performance. Interestingly, all methods achieve rela-
tively similar ∆ Top2 errors, indicating that reproducing the marginal popularity of the
most preferred candidates is considerably less challenging. Nevertheless, LPSE-FM con-
sistently achieves the smallest ∆Pair error, more faithfully capturing the common-alternative
candidate structure. Although GPV AE presents a slightly smaller ∆ Top2 error under
mgen = 1000, its ∆ Pair error remains relatively larger than that of LPSE-FM, suggesting
that matching marginal frequencies alone does not guarantee an accurate representation
of the underlying preference distribution. Figure 2(b) shows the simplex interpretation
with vertices labeled by the pairs Candidates{2,5}, Candidates{1,5}, and Candidates
{3,1}, respectively. It reveals a clear asymmetry that the generated preference weights
concentrate toward the pair Candidates{1,5}, indicating that this preference type is
more prevalent than the other two. The relatively sparse mass near Candidates{2,5}
and Candidates{3,1}vertices suggests a more specialized voting pattern. More details
are provided in Table 6.
25

Overall, the Sushi and APA experiments show that LPSE-FM can generate realistic
synthetic rankings while preserving interpretable population structure. In the Sushi ap-
plication, the generated rankings can facilitate consumer-preference and recommendation
studies; in the APA application, they can support the analysis and simulation of collective
choice and voting procedures.
5 Discussion
This paper develops a population-level generative framework for ranking data. The pro-
posed LPSE-FM framework combines an interpretable low-dimensional latent preference
simplex with flexible generative modeling, while retaining a probabilistic ranking mecha-
nism for decoding latent preferences into rankings. The theoretical results show that rank-
ing generation can be reduced to latent distribution learning and provide finite-sample
guarantees that explicitly characterize the effects of the number of rankers, number of
items, ranking length, and latent dimension. The numerical results further suggest that
this structure is useful in practice: LPSE-FM consistently preserves population-level fi-
delity, while the latent preference simplex provides a direct interpretation of population
preference heterogeneity.
Data availability
All datasets used in this paper are publicly available from the sources described in Sec-
tion 4.
References
M. C. U. Ara´ ujo, T. C. B. Saldanha, R. K. H. Galvao, T. Yoneyama, H. C. Chame, and
V. Visani. The successive projections algorithm for variable selection in spectroscopic
multicomponent analysis.Chemometrics and intelligent laboratory systems, 57(2):65–
73, 2001.
26

C. Biernacki and J. Jacques. A generative model for rank data based on insertion sort
algorithm.Computational Statistics & Data Analysis, 58:162–176, 2013.
F. Caron, Y. W. Teh, and T. B. Murphy. Bayesian nonparametric plackett–luce models
for the analysis of preferences for college degree programmes. 2014.
P. Chen, C. Gao, and A. Y. Zhang. Optimal full ranking from pairwise comparisons.The
Annals of Statistics, 50(3):1775–1805, 2022.
R. T. Chen and Y. Lipman. Flow matching on general geometries. InInternational
Conference on Learning Representations, volume 2024, pages 47922–47945, 2024.
Y. Chen, J. Fan, C. Ma, and K. Wang. Spectral method and regularized mle are both
optimal for top-k ranking.Annals of statistics, 47(4):2204, 2019.
Y. Chen, J. Tan, A. Zhang, Z. Yang, L. Sheng, E. Zhang, X. Wang, and T.-S. Chua.
On softmax direct preference optimization for recommendation.Advances in Neural
Information Processing Systems, 37:27463–27489, 2024.
C. Cheng, J. Li, J. Peng, and G. Liu. Categorical flow matching on statistical manifolds.
Advances in Neural Information Processing Systems, 37:54787–54819, 2024.
T. Chowdhury, Y. Zick, and J. Allan. Rankshap: Shapley value based feature attributions
for learning to rank. InInternational Conference on Learning Representations, volume
2025, pages 36765–36794, 2025.
B. Dai, X. Shen, J. Wang, and A. Qu. Scalable collaborative ranking for personalized
prediction.Journal of the American Statistical Association, 116(535):1215–1223, 2021.
P. Dong, R. Han, B. Jiang, and Y. Xu. Statistical ranking with dynamic covariates.
Journal of the Royal Statistical Society Series B: Statistical Methodology, 88(1):221–
238, 2026.
J. C. Duchi, L. Mackey, and M. I. Jordan. The asymptotics of ranking algorithms.The
Annals of Statistics, pages 2292–2323, 2013.
27

J. Fan, Z. Lou, W. Wang, and M. Yu. Ranking inferences based on the top choice
of multiway comparisons.Journal of the American Statistical Association, 120(549):
237–250, 2025.
J. Fan, Z. T. Ke, and Z. Shi. Optimal demixing of nonparametric densities.arXiv preprint
arXiv:2603.27457, 2026.
Y. Fang, J. Zhan, Q. Ai, J. Mao, W. Su, J. Chen, and Y. Liu. Scaling laws for dense
retrieval. InProceedings of the 47th International ACM SIGIR Conference on Research
and Development in Information Retrieval, pages 1339–1349, 2024.
K. Fukumizu, T. Suzuki, N. Isobe, K. Oko, and M. Koyama. Flow matching achieves
almost minimax optimal convergence. InInternational Conference on Learning Rep-
resentations, volume 2025, pages 27608–27640, 2025.
S. Geisser. The predictive sample reuse method with applications.Journal of the Amer-
ican statistical Association, 70(350):320–328, 1975.
M. Germain, K. Gregor, I. Murray, and H. Larochelle. Made: Masked autoencoder for
distribution estimation. InInternational conference on machine learning, pages 881–
889. Pmlr, 2015.
I. C. Gormley and T. B. Murphy. A mixture of experts model for rank data with appli-
cations in election studies. 2008.
H. Guo, E. Xue, L. Huang, S. Wang, X. Wang, L. Wang, J. Wang, and S. Chen. Action is
all you need: Dual-flow generative ranking network for recommendation.arXiv preprint
arXiv:2505.16752, 2025.
R. Han and Y. Xu. A unified analysis of likelihood-based estimators in the plackett–luce
model.The Annals of Statistics, 53(5):2077–2102, 2025.
S. He.Identifiability and estimation of mixed membership stochastic blockmodels. PhD
thesis, University of Illinois at Urbana-Champaign, 2023.
28

J. Ho, A. Jain, and P. Abbeel. Denoising diffusion probabilistic models.Advances in
neural information processing systems, 33:6840–6851, 2020.
H. Hosseini, D. Mandal, and A. Puhan. The surprising effectiveness of sp voting with
partial preferences.Advances in Neural Information Processing Systems, 37:2787–2829,
2024.
K. Huang and X. Fu. Detecting overlapping and correlated communities without pure
nodes: Identifiability and algorithm. InInternational Conference on Machine Learning,
pages 2859–2868. PMLR, 2019.
Y. Huang, Y. Chen, X. Cao, R. Yang, M. Qi, Y. Zhu, Q. Han, Y. Liu, Z. Liu, X. Yao,
et al. Towards large-scale generative ranking.arXiv preprint arXiv:2505.04180, 2025.
M. Jazbec, M. Ashman, V. Fortuin, M. Pearce, S. Mandt, and G. R¨ atsch. Scalable
gaussian process variational autoencoders. InInternational conference on artificial
intelligence and statistics, pages 3511–3519. PMLR, 2021.
J. Jin, Z. T. Ke, and S. Luo. Mixed membership estimation for social networks.Journal
of Econometrics, 239(2):105369, 2024.
S. R. Johnson, D. A. Henderson, and R. J. Boys. Revealing subgroup structure in ranked
data using a bayesian wand.Journal of the American Statistical Association, 115(532):
1888–1901, 2020.
T. Kamishima. Nantonac collaborative filtering: recommendation based on order re-
sponses. InProceedings of the ninth ACM SIGKDD international conference on Knowl-
edge discovery and data mining, pages 583–588, 2003.
A. Koloskova, H. Hendrikx, and S. U. Stich. Revisiting gradient clipping: Stochastic bias
and tight convergence guarantees. InInternational Conference on Machine Learning,
pages 17343–17363. PMLR, 2023.
D. B. Lee, D. Min, S. Lee, and S. J. Hwang. Meta-gmvae: Mixture of gaussian vae for
unsupervised meta-learning.ICLR, 2:6, 2021.
29

B. Li, A. Tamkin, N. Goodman, and J. Andreas. Eliciting human preferences with
language models. InInternational Conference on Learning Representations, volume
2025, pages 80984–81013, 2025.
Y. Lipman, R. T. Chen, H. Ben-Hamu, M. Nickel, and M. Le. Flow matching for gener-
ative modeling.arXiv preprint arXiv:2210.02747, 2022.
Y. Lipman, M. Havasi, P. Holderrieth, N. Shaul, M. Le, B. Karrer, R. T. Chen, D. Lopez-
Paz, H. Ben-Hamu, and I. Gat. Flow matching guide and code.arXiv preprint
arXiv:2412.06264, 2024.
S. Liu, A. Zhang, G. Hu, H. Qian, and T.-s. Chua. Preference diffusion for recommen-
dation. InInternational Conference on Learning Representations, volume 2025, pages
79844–79881, 2025.
C. Mao and Y. Wu. Learning mixtures of permutations: Groups of pairwise comparisons
and combinatorial method of moments.The Annals of Statistics, 50(4):2231–2255,
2022.
N. Mattei and T. Walsh. Preflib: A library for preferences http://www. preflib. org. In
International conference on algorithmic decision theory, pages 259–270. Springer, 2013.
C. Mollica and L. Tardella. Bayesian plackett–luce mixture models for partially ranked
data.Psychometrika, 82(2):442–458, 2017.
S. Mukherjee, A. Lalitha, K. Kalantari, A. Deshmukh, G. Liu, Y. Ma, and B. Kve-
ton. Optimal design for human preference elicitation.Advances in Neural Information
Processing Systems, 37:90132–90159, 2024.
T. B. Murphy and D. Martin. Mixtures of distance-based models for ranking data.
Computational statistics & data analysis, 41(3-4):645–655, 2003.
S. Negahban, S. Oh, K. K. Thekumparampil, and J. Xu. Learning from comparisons and
choices.Journal of Machine Learning Research, 19(40):1–95, 2018.
30

D. Park, J. Neeman, J. Zhang, S. Sanghavi, and I. Dhillon. Preference completion: Large-
scale collaborative ranking from pairwise comparisons. InInternational Conference on
Machine Learning, pages 1907–1916. PMLR, 2015.
M. Pearce and E. A. Erosheva. Modeling preferences: A bayesian mixture of finite
mixtures for rankings and ratings.Journal of the American Statistical Association,
120(551):1621–1632, 2025.
J. Qiu, Z. Wang, F. Zhang, Z. Zheng, J. Zhu, J. Fan, T. Zhang, H. Wang, and X. Wang.
Unirom: Unifying online advertising ranking as one model. InProceedings of the 34th
ACM International Conference on Information and Knowledge Management, pages
2440–2449, 2025.
D. Rezende and S. Mohamed. Variational inference with normalizing flows. InInterna-
tional conference on machine learning, pages 1530–1538. PMLR, 2015.
Z. Shi, K. Liu, Q. Long, W. J. Su, and J. Xiao. Fundamental limits of game-
theoretic llm alignment: Smith consistency and preference matching.arXiv preprint
arXiv:2505.20627, 2025.
M. G. Silveri, G. Conforti, and A. Durmus. Theoretical guarantees in kl for diffusion flow
matching.Advances in Neural Information Processing Systems, 37:138432–138473,
2024.
M. Stone. Cross-validatory choice and assessment of statistical predictions.Journal of
the royal statistical society: Series B (Methodological), 36(2):111–133, 1974.
P. Tsimpos, Z. Ren, J. Zech, and Y. Marzouk. Optimal scheduling of dynamic transport.
arXiv preprint arXiv:2504.14425, 2025.
L. Wu, C.-J. Hsieh, and J. Sharpnack. Sql-rank: A listwise approach to collaborative
ranking. InInternational Conference on Machine Learning, pages 5315–5324. PMLR,
2018.
31

J. Xiao, Z. Li, X. Xie, E. Getzen, C. Fang, Q. Long, and W. J. Su. On the algorithmic
bias of aligning large language models with rlhf: Preference collapse and matching
regularization.Journal of the American Statistical Association, 120(552):2154–2164,
2025.
Z. Yang, L. Sang, H. Wang, W. Chen, L. Wang, J. He, C. Peng, Z. Lin, C. Gan, and
J. Shao. Parallel ranking of ads and creatives in real-time advertising systems. In
Proceedings of the AAAI Conference on Artificial Intelligence, volume 38, pages 9278–
9286, 2024.
M. Yin, K. Boughanmi, and A. Mukherjee. Express: Modeling dynamic consumer prefer-
ences from few-shot data: A meta-learning approach.Journal of Marketing Research,
page 00222437261458290.
Z. Zhao, P. Piech, and L. Xia. Learning mixtures of plackett-luce models. InInternational
Conference on Machine Learning, pages 2906–2914. PMLR, 2016.
Z. Zhou and W. Liu. An error analysis of flow matching for deep generative modeling.
InForty-second International Conference on Machine Learning, 2025.
W. Zhu, Y. Jiang, J. S. Liu, and K. Deng. Partition–mallows model and its inference for
rank aggregation.Journal of the American Statistical Association, 118(541):343–359,
2023.
32
