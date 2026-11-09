---
title: 'Optimal transport meets speech: a tutorial review'
url: https://arxiv.org/abs/2609.31787
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Xugang Lu
- Yu Tsao
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.31787
pages: 27
chars: 139386
fetched_at: '2026-11-08T13:25:12+00:00'
kb_version: 1
---

# Optimal transport meets speech: a tutorial review

1
Optimal transport meets speech: a tutorial review
Xugang Lu 1, Yu Tsao 2
1. National Institute of Information and Communications Technology, Japan
2. Research Center for Information Technology Innovation, Academia Sinica, Taiwan
Abstract—Optimal Transport (OT) provides a principled
framework for comparing and transforming probability distri-
butions while preserving geometric structure. Recently, OT has
gained significant attention in machine learning due to its ability
to measure discrepancies between distributions, even when their
supports do not overlap, making it effective for tasks such as
generative modeling, domain adaptation, and transfer learning.
Despite its success in fields such as computer vision and natural
language processing, OT remains relatively underexplored in
speech research. Speech signals present unique challenges, includ-
ing temporal dynamics, speaker variability, noise, reverberation,
and heterogeneous multimodal representations involving audio,
text, and visual information. These factors often lead to dis-
tribution mismatches, where OT offers a natural framework for
alignment and interpretation. This work aims to promote broader
adoption of OT in speech processing by: (1) reviewing OT founda-
tions through intuitive physical interpretations and highlighting
connections to modern generative models; (2) presenting compu-
tational algorithms suitable for deep learning frameworks; and
(3) demonstrating OT applications in cross-domain and cross-
modal speech tasks, including speech enhancement, automatic
speech recognition, language and speaker recognition, and audio
spoof detection. We highlight OT’s strong potential for addressing
distributional variations in real-world speech applications.
Index Terms—Optimal transport, Cross-domain adaptation,
Cross-modal knowledge transfer learning, Alignment and match-
ing.
I. INTRODUCTION
Optimal transport (OT), also known as mass transport, can
be simply described as the search for the most efficient way to
transform from one mass distribution to another, considering
a specified transform cost [63], [120]. This theory which
has been extensively studied by many researchers has found
extensive applications in operational research, mathematics,
economics, and physics [63], [120]. In particular, it has
garnered widespread attention in statistical machine learning
(ML) in recent years [64], [96], [103].
A. Optimal transport in machine learning
In statistical ML, whether dealing with pattern classifica-
tion or regression problems, numerous research tasks involve
comparing or manipulating the probability distributions of the
underlying features or objects. The role of applying OT in ML
lies in its ability to furnish an effective metric measure (e.g.,
discrepancy or distance measure) between two probability
distributions, establishing correspondences between sets of
samples with a geometric-aware distance between distribu-
tions. This metric measure can then function as a learning
objective or metric when handling feature vectors within
a probability space. OT-based learning has been shown to
be effective in measuring the distribution discrepancy even
when the compared distributions have disjoint supports [101].
Furthermore, this learning can incorporate the geometric struc-
tures of datasets, demonstrating a form of geometric-aware
learning [26]. In addition to the increasing popularity of ML
in recent years, especially in computational ML theories (such
as generative model learning, domain adaptation, or transfer
learning) [26], OT theory has been extensively applied in real-
world scenarios, particularly in the fields of computational
graph, image classification [132], and computer vision [13],
[130]. It has also gained recognition for a range of natural
language processing (NLP) tasks [11], [19], [123], including
document retrieval, semantic matching [11], machine transla-
tion [141], and word embedding [70]. In contrast, the speech
science community has only recently begun to explore appli-
cations of OT. The inherently sequential and temporal nature
of speech signals poses significant challenges in integrating
OT into speech processing frameworks, which has limited its
exploration in this domain.
B. Optimal transport in speech
In speech tasks, various challenges need consideration,
including feature representation learning, feature and model
fusion, domain adaptation, knowledge transfer learning, etc.
These learning algorithms primarily manipulate probability
distributions. A crucial aspect for improving performance is
the thoughtful selection of a meaningful measurement metric,
such as discrepancy, similarity, or distance. The use of OT ex-
tends to estimating, comparing, and aligning the distributions
for feature aggregation, model fusion, cross-domain and cross-
modal adaptation, and transfer learning. Hence, the primary
goal of this review paper is to review fundamental knowledge
about OT and its computational algorithms, demonstrating
their adaptability to deep learning model frameworks with
ease. Through this review, a clear understanding emerges that
OT can offer meaningful explanations in model learning.
In real-world applications of speech technologies, the per-
formance of speech applications often experiences notable
degradation due to various factors. On the one hand, speech
signals are susceptible to external or extrinsic degradations
such as noise, reverberation, and noise suppression process-
ing, significantly impacting speech quality and intelligibility
[75], [124], [139]. On the other hand, intrinsic variations
pose challenges as speech exhibits considerable diversity in
articulation styles among speakers and co-articulation effects
influenced by different contexts and domains. A co-occurring
pattern involves representing acoustic speech in multi-views,
arXiv:2609.31787v1  [eess.AS]  24 Sep 2026

2
including text content and visual information during speak-
ing. Addressing these challenges, learning representations that
encompass all these multi-view information sources can po-
tentially mitigate uncertainty. Robust representations learned
through cross-modal feature learning have been shown to
enhance performance and adaptability in diverse speech sce-
narios. The OT serves as a powerful mathematical tool for
quantifying and manipulating distribution variations. Thus, the
second objective of this review paper is to introduce ideas
and techniques to seamlessly integrate OT to describe the
underlying distribution variations of speech, with the aim of
enhancing overall performance.
In summary, the purpose of this review is to introduce OT
in speech signal processing and to share our findings, offering
our insights to speech researchers seeking entry points into
this promising area. In this review paper, our aim is to: (1)
Provide a historical review of the OT problem, mathematical
foundations, connections in transport modeling to generative
diffusion models, and computational algorithms, particularly
focusing on those integrated into deep learning model frame-
works. (2) Introduce potential applications of OT in ML
and related fields, particularly in domain adaptation tasks;
(3) Explain how OT can be seamlessly and effectively inte-
grated into speech-related application tasks. We will present
research topics that integrate OT for speech application prob-
lems, including speech translation, spoken document retrieval,
semantic analysis in NLP, and speech acoustic modeling.
Specifically, we will address cross-domain problems related
to speech enhancement (SE) [52], [77], speaker recognition or
verification (SR/SVR) [122], [133], spoken language identifi-
cation/recognition (SLID/SLR) [87], and multi-modal or cross-
modal knowledge transfer and adaptation for automatic speech
recognition (ASR) [86], [88], [90], [91]; (4) Share our review
and perspective on the potential usage of OT in speech.
C. Notations and symbols
For a self-contained introduction of the main concepts of
OT, we begin by giving several fundamental mathematical
notations, symbols and operators that will be frequently used
throughout this paper.
1) Gradient:The gradient of a scalar functionf:R n →R
is the vector consisting of its partial derivatives with respect
to each coordinate direction. It points in the direction of the
steepest increase in the function and encodes how the function
changes in space, a vector field denoted by∇fformulated as:
grad(f) :∇f
∆
=
 ∂f
∂x1
, ∂f ∂x2 , ...,∂f ∂xn

.(1)
2) Divergence:The divergence of a vector field is the
scalar quantity obtained by summing the partial derivatives
of each vector component. It measures the net rate at which
“mass” or “flow” is expanding or contracting at a given
point. The divergence of a vector fieldF:R n →R n with
F= (F 1, F2, . . . , Fn)is a scalar field denoted by∇ ·Fand
is defined as:
div(F) :∇ ·F
∆
=
X
i
∂Fi
∂xi
.
Push-forward measure
𝑇:𝑋 → 𝑌
𝜈=𝑇 #𝜇
(𝑋,𝒜,𝜇) (𝑌,ℬ,𝜈)
Figure 1. Push-forward measure in probability spaces.
3) Laplacian:The Laplacian operator is defined as the
divergence of the gradient. Applied to a scalar function, it
produces a scalar quantity that describes how the value of the
function at a point compares to its average value in a small
neighborhood. The Laplacian plays a central role in diffusion
processes, heat equations, and many partial differential equa-
tions (PDEs) relevant to OT. The Laplacian of a scalar field
f:R n →Ris a scalar field denoted by∆for∇ 2fand is
defined as the divergence of the gradient off:
∆f=∇ 2f=∇ ·(∇f) = div(grad(f)).
Explicitly, inR n, it is given by:
∆f
∆
= ∂2f ∂x2 1 + ∂2f ∂x2 2 +· · ·+∂2f ∂x2n .
4) Probability space and Push-Forward Measures:The
notion of a probability space and the concept of a push-forward
measure [71] are fundamental in OT. A probability space (or
a measure space) is formally described as a triple(X,A, µ),
where
•Xis the sample space, representing all possible out-
comes,
•Ais aσ-algebra of measurable subsets ofX, representing
the collection of admissible events,
•µis a probability measure that assigns a probability value
to each event inA.
Although these definitions arise from abstract measure the-
ory (e.g.,Xis often assumed to be a Polish space), our purpose
here is practical. Therefore, it suffices to consider a probability
space as a structured way to assign probabilities to events.
Now consider a measurable transformationT:X→Ythat
maps elements from one probability space to another. This
map naturally induces a new measure inY, called the push-
forward measure, as shown in Fig. 1. Intuitively, the push-
forward describes how the probability mass is transported
fromXtoYthroughT. Formally, given a measure space
(X,A, µ)and a measurable space(Y,B), the push-forward
measureν=T #µin(Y,B)is defined by:
T#µ(B) =µ

T −1(B)  ,∀B∈ B,(2)
whereT −1(B) ={x∈X|T(x)∈B}.
The push-forward measure satisfies the usual change-of-
variables formula. For any measurable functionφ:Y→R,
we have: Z
Y
φ d(T#µ) =
Z
X
φ◦T dµ.(3)

3
Monge
(1746-1818)
Kantorovich
(1912-1986)
Dantzig
(1914-2005)
Wasserstein
(1944 )
Caffarelli
(1948 )
Brenier
(1957)
Otto
(1966)
Ambrosio
(1963)
McCann Villani
(1973)
Figalli
(1984)
Koopmans
(1910-1985)
Nobel Prize in 1975
Hitchcock
(1875-1957)
2010 Field prize 2018 Field prize
2012 Wolf prize
2023 Abel prize
Figure 2. Historical figures in the development of OT theory.
This identity is used extensively in OT theory, particularly
when describing how probability distributions transform under
transport maps.
II. HISTORIC REVIEW OFOPTIMAL TRANSPORT
This section provides a comprehensive and historical review
of the fundamental concept of OT and its connections to
concepts used in other disciplines.
A. Problems of OT
OT problems have been described through various intuitive
examples in different fields, for example, delivering baked
goods to coffee shops, moving sand or soil for construction, or
relocating rubble for site preparation [120]. In simple terms,
OT seeks the most efficient way to achieve a given goal,
typically by minimizing the effort or cost required to move the
mass from one distribution to another. Despite the simplicity
of its underlying idea, solving OT problems is often highly
nontrivial. The field has a history spanning more than two
centuries and has been marked by extensive and ongoing
research activities. Fig. 2 describes the important characters
related to OT along the time line.
B. Historical figures in the development of OT theory
Over the past two centuries, many influential scholars have
contributed to the development of OT theory, which continues
to thrive with vigorous research activities, especially in the
21st century. As shown in Fig. 2, OT theory traces its origins
back to 1781, when Monge first posed the problem of de-
termining the most efficient way to transport mass between
two locations. The development of this theory progressed
slowly until 1942, when Kantorovich introduced a relaxed
formulation of Monge’s problem by incorporating duality and
linear programming, thus establishing OT as a powerful tool
for resource allocation [38], [120]. In parallel, Dantzig-known
as the “father of the simplex algorithm” proposed efficient
algorithms that further advanced the solution of optimization
problems in OT. Wasserstein later formalized the Kantorovich
problem through what is now known as the Wasserstein
distance [1]. This formulation opened the door to new in-
sights and methodologies that have influenced a wide range
of disciplines, including physics, probability theory, financial
mathematics, and economics. Toward the new century, signif-
icant theoretical progress was made by mathematicians such
Monge problem
Kantorovich problem
Duality
1987
Wasserstein gradient flow
2000
2001
Wasserstein distance
2005
1781 1969 1998
1942
Brenier theorem Benamou-Brenier formulation
Dynamic OT
Otto Calculus, Geometry of OT
Gradient flow in
Wasserstein metric space
Figure 3. Landmark research activities.
as Brenier [15], who addressed the existence of OT maps, and
Otto and McCann, who investigated the geometric structure
underlying OT. In recent decades, Villani has made profound
contributions to OT theory, and his influential books on OT
are widely known [120], [121]. Figalli has also advanced the
field, particularly through applications to PDEs. The histor-
ical trajectory of these contributions highlights not only the
brilliance of the researchers involved but also the recognition
the field has received through numerous prestigious awards.
Together, these developments underscore the importance and
enduring vitality of OT as a research area.
C. Landmark research activities
During the development of OT theory, several historical
moments or landmark activities have been recorded. A rough
figure is shown in Fig. 3. The figure summarizes the major
milestones in the development of OT theory. The concept
originated in 1781, when Monge introduced what is now
known as the Monge OT problem: finding an OT map that
moves mass from one distribution to another while minimizing
a prescribed cost. This formulation is elegant but difficult to
solve, and, moreover, an optimal map does not always exist.
Substantial progress was made in 1942 when Kantorovich pro-
posed a relaxed version of Monge’s formulation by introducing
the notion of a transport plan or coupling. This relaxation
transformed the OT problem into a LP framework and allowed
solutions to exist under far more general conditions. In the late
1960s, the concept of the Wasserstein distance was articulated,
revealing that the Wasserstein metric is equivalent to the
Kantorovich formulation. This insight provided a geometric
interpretation of OT and connected it to probability theory,
analysis, and geometry. However, for many years, the exis-
tence of OT maps remained unclear. A breakthrough occurred
around 1987, when Brenier established his celebrated theorem,
proving the existence and uniqueness of OT maps under suit-
able conditions, and showing that such maps arise as gradients
of convex functions [15], [93]. This result has become founda-
tional for modern computational OT, for example, many neural
network-based OT methods such as an neural OT models and
algorithms based on the Input Convex Neural Network (ICNN)
model [3], [94], directly build on the structure revealed by
Brenier’s theorem. Further significant advances took place in
the late 1990s. Around 1998-1999, researchers demonstrated
that the evolution from one probability distribution to another
can be interpreted as a Wasserstein gradient flow, governed by
a PDE [35]. Shortly thereafter, around 2000, OT was linked to

4
Optimal transport (OT)
Fluid Dynamic
Stochastic Mean Field Game
Schrödinger Bridge
Optimal control
Wasserstein distance metric
/Gradient flow
Flow matching
Diffusion model
Monge-Ampère-type equations
Nash Equilibrium
Master Equation
Information geometry
Otto calculus
Itô process
Fokker-Planck Equation
Benamou-Brenier formulation
Transfer operator
Stochastic Differential Equation
Figure 4. Wide concept connections to OT.
fluid dynamic formulations, giving rise to a dynamic viewpoint
in which OT corresponds to minimizing kinetic energy over
time [9]. This dynamic formulation inspired numerous exten-
sions, including time-dependent OT models and applications
in continuum mechanics [9]. The study of gradient flows
in the Wasserstein space also led to the discovery of rich
geometric properties of OT, most notably the development
of Otto’s Calculus [57], [98]. These geometric insights have
had far-reaching consequences: they connected OT to the
analysis of PDEs, informed variational approaches to diffusion
equations, and motivated modern interpretations of stochastic
differential equations (SDEs) through the lens of Wasserstein
geometry [40]. Together, these theoretical developments form
the backbone of both classical and modern OT theory, laying
the foundation for its widespread influence in mathematics
[57], physics, engineering, data science, and machine learning
[120].
D. Wide concept connections to OT
Based on OT theory, many concepts and methods could be
connected to OT. Fig. 4 shows several concepts and methods
we have ever met in different research fields which have
a close relationship to OT. For example, fluid dynamics,
diffusion model, flow matching, etc., particularly their con-
nections with recent generative model based machine learning
algorithms. These concepts are original from physics and
mathematics, and there is a trend in the machine learning
society trying to apply these concepts to learning algorithms
[101]. In applications, a lot of tools have been derived from
these research fields and concepts. In the following sections,
we will introduce the mathematical formulations and proper-
ties related to OT.
III. MONGE’SOPTIMALTRANSPORTPROBLEM
Monge’s OT problem is one of the classical formulations
in OT theory. Given a probability measureµin a measurable
space(X,A), a probability measureνin a measurable space
(Y,B), and a cost functionc:X×Y→[0,∞), the goal is to
find a measurable mapT:X→Ythat minimizes the total
transportation cost. The problem is formulated as [2], [120]:
inf
T
Z
X
c(x, T(x))dµ(x),(4)
subject to the constraint that the mapTpushes the measure
µontoν:
T#µ=ν.(5)
Several key components appear in this formulation:
•Transport mapT: A measurable map that transfers the
mass from the source measureµto the target measureν.
The push-forward operation ensures thatTredistributes
µ-mass to matchν.
•Cost functionc(x, y): A nonnegative function defining
the transportation cost betweenx∈Xandy∈Y. Com-
mon choices include the Euclidean distance, its powers,
or more general Minkowski-type distances.
•Total cost of transport: The integralR
X c(x, T(x))dµ(x), representing the total cost of
transporting the mass according to the mapT.
•Infimum: The problem seeks the minimum possible
value of the total cost over all admissible transport maps
(indicated as symbol “inf” in Eq. (4) ). Informally, this
may be regarded simply as a minimization problem.
In summary, the Monge formulation asks for an OT map
Tthat moves the mass ofµto matchνwhile achieving the
smallest possible transport cost.
IV. KANTOROVICHRELAXATION OF THEOPTIMAL
TRANSPORTPROBLEM
The formulation of the OT problem in Monge’s sense suffers
from several fundamental limitations. Monge’s formulation
requires a transport mapTthat sends each point in the
source domain to exactly one point in the target domain. This
prohibits any splitting of the mass and implicitly assumes
thatµandνhave the same total mass and compatible struc-
tures. Consequently, the Monge problem may be ill-posed: a
minimizer may not exist, and even when a solution exists,
it is difficult to compute because the problem is inherently
combinatorial [101]. A major breakthrough occurred in 1942
due to Kantorovich, who proposed a relaxed formulation of
the transport problem. In Kantorovich’s version, mass may
be split and redistributed across multiple destinations, making
the transportation process stochastic rather than deterministic.
This relaxation replaces transport maps with transport plans
(also called couplings). With this modification, the existence of
minimizers is guaranteed under very mild conditions, and the
theory becomes substantially more tractable. This relaxation
marks the beginning of modern OT theory [2], [120].
A. Kantorovich OT Problem
Kantorovich’s formulation generalizes Monge’s problem
by replacing measurable maps with joint measures. Given
probability measuresµon(X,A)andνon(Y,B), and a cost
functioncas defined in Monge’s problem, the objective is to
find a transport planγthat minimizes the total transportation

5
𝑦
𝜇(𝑥𝑖 )
𝜈(𝑦𝑗 )𝑥
Figure 5. Mass splitting in discrete Kantorovich OT.
cost. A transport plan is a probability measureγinX×Y
whose marginals areµandν. The Kantorovich OT problem
is then defined as:
inf
γ∈Π(µ,ν)
Z
X×Y
c(x, y)dγ(x, y),(6)
where the admissible set of couplings is
γ(A×Y) =µ(A),∀A∈ A,
γ(X×B) =ν(B),∀B∈ B. (7)
In this formulation, a transport planγis a joint distributionQ (µ, ν)onX×Ythat describes how mass is transferred
fromXtoY. Its marginals satisfy:
Z
Y
γ(x, dy) =µ(dx),
Z
X
γ(dx, y) =ν(dy).(8)
Unlike Monge’s transport map, a transport plan allows the
mass at a single locationx∈Xto be split and sent to multiple
destinations.
B. Discrete Kantorovich OT
In the discrete setting, letX={x 1, . . . , xm}andY=
{y1, . . . , yn}with corresponding probability distributionsµ
andν. Letc(x i, yj)denote the transportation cost fromx i to
yj. A discrete transport plan is represented by a nonnegative
matrixγ= (γ ij)∈R m×n ≥0 , whereγ ij specifies the fraction
of mass moved fromx i toy j. The discrete Kantorovich OT
problem becomes [101]:
min
γ∈Π(µ,ν)
mX
i=1
nX
j=1
γij c(xi, yj),(9)
subject to:
nX
j=1
γij =µ(x i),∀i,
mX
i=1
γij =ν(y j),∀j,
γij ≥0,∀i, j.
(10)
This discrete transport process is explained in Fig. 5. As
shown in this figure, Kantorovich’s relaxation allows the mass
at eachx i to be divided among multiple target pointsy j,
making the coupling matrixγa probabilistic representation
of all permissible transport assignments. This relaxation not
only guaranties the existence of minimizers but also provides
the foundation for modern numerical OT algorithms and
theoretical advancements.
V. WASSERSTEINDISTANCEMETRIC
Based on the concepts and definitions explained in sections
III and IV, we now introduce an important notion that appears
frequently in our research, i.e., the Wasserstein distance.
This distance is defined between two probability measures
and quantifies how far one distributionµis from another
distributionν. The terminology “Wasserstein” originates from
the mathematician Leonid Vaser ˇste˘ın, whose name appeared
in the literature in this transliterated form. Thep-Wasserstein
distance is defined using the cost of transporting the mass with
respect to a ground distance metricd(x, y). This construction
leads to a mathematically well-behaved notion of distance
with strong geometric and analytic properties. In particular,
the Wasserstein distance is a metric, which allows us to study
probability measures within the framework of metric geometry
and functional analysis. Forp≥1, thep-Wasserstein distance
between probability measuresµandνon a metric space(X, d)
is defined as [101], [120]:
Wp(µ, ν)
∆
=

inf
γ∈Q(µ,ν)
Z
X×X
d(x, y)p dγ(x, y)
1/p
,(11)
where Q(µ, ν)denotes the set of all couplings ofµandν,
i.e., all joint probability measures inX×Xwhose marginals
coincide withµandν, respectively. Several properties are
related to this Wasserstein distance:
•Non-negativity:W p(µ, ν)≥0andW p(µ, ν) = 0if and
only ifµ=ν.
•Metric property:W p defines a metric in the space of
probability measures with finitep-th moment.
•Invariance:W p(µ, ν)is invariant under isometries of the
underlying metric space.
Based on this definition, several special cases could be ob-
tained:
•Whenp= 1, the Wasserstein distanceW 1 is known as the
Earth Mover’s Distance or the Kantorovich-Rubinstein
metric. It is widely used in computer vision and machine
learning, including the Wasserstein GAN framework [6].
•Whenp= 2, the Wasserstein distanceW 2 corresponds
to the quadratic Wasserstein metric, central in OT theory
and geometric interpretations of PDEs.
Because the Wasserstein distance is a genuine metric, the
induced space:
Wp(X) :
∆
= (Pp(X), Wp),(12)
which is known as the Wasserstein space. This geometric
structure enables various operations on probability distribu-
tions, including interpolation, computation of geodesics, and
analysis of distributional flows. Furthermore, the geometric
viewpoint has deep connections to PDEs. Many evolution
equations, such as the continuity equation and several SDEs,
can be interpreted as gradient flows in the Wasserstein space
[1]. This perspective has become foundational in modern
generative modeling, for example in diffusion-based generative

6
AI, where stochastic diffusion processes admit gradient-flow
formulations in Wasserstein geometry. The broader theoretical
development of Wasserstein spaces is extensive and influential,
although its details are beyond the scope of this review paper
[1], [93], [105].
VI. DUALPROBLEM OFOPTIMALTRANSPORT
OT theory, originating from Monge and later rigorously
reformulated by Kantorovich, aims to determine the most
cost-efficient way to transport the mass from one probabil-
ity distribution to another. Kantorovich’s relaxation naturally
leads to a linear programming (LP) formulation, which in turn
provides access to its dual problem through LP duality. In this
section, we introduce the primal and dual problems and explain
their connections through thec-transform and Kantorovich
potentials [101], [120].
A. Primal Problem
Given two probability measuresµandν, and a measurable
cost functionc, the Kantorovich OT problem seeks a coupling
γ∈Π(µ, ν)minimizing the total transportation cost as defined
in eqs. (6), (8) and (9), (10). Looking at their structures,
they are formulated the same as used in LP which structure
implies the existence of a corresponding dual problem. Intu-
itively, while the primal minimizes transportation cost, the dual
maximizes the “benefit” associated with assigning potential
values to the source and target points, subject to feasibility
constraints.
B. Dual Problem
The dual of the Kantorovich OT problem introduces func-
tions:
ϕ:X→R, ψ:Y→R,(13)
called the Kantorovich potentials, satisfying the inequality
constraint:
ϕ(x) +ψ(y)≤c(x, y),∀(x, y)∈X×Y.(14)
The dual objective is then
sup
ϕ,ψ
Z
X
ϕ(x)dµ(x) +
Z
Y
ψ(y)dν(y)

.(15)
c-transform andc-concavity:A key concept for understand-
ing the dual problem is thec-transform [121]. For a function
ϕ:X→R, define:
ϕc(y) : ∆ = inf
x∈X
(c(x, y)−ϕ(x)),(16)
and similarly,
ϕcc(x) : ∆ = inf
y∈Y
(c(x, y)−ϕc(y)).(17)
Whenϕ cc =ϕ, the functionϕis calledc-concave. The dual
potentials satisfy relations of the form [121]:
ψ(y) =ϕ c(y),
ϕ(x) =ψ ¯c(x) : ∆ = inf
y∈Y
(c(x, y)−ψ(y)). (18)
Thus, dual optimization may be recast as optimizing a single
c-concave function. This formulation is sometimes referred to
as the semi-dual problem.
Interpretation of Dual Variables:The dual functionsϕand
ψrepresent the marginal prices or potentials associated with
the transport of mass. The inequality constraint ensures that
no transport betweenxandycosts less than the assigned
potential difference. Geometrically, these potentials describe
the supporting hyperplanes of the cost function and play an
essential role in understanding optimal couplings [121].
C. Relationship Between Primal and Dual Problems
A fundamental result in OT is strong duality:
inf γ∈Q (µ,ν) R X×Y c(x, y)dγ(x, y)
∆
= supϕ,ψ
R
X ϕ(x)dµ(x) +
R
Y ψ(y)dν(y)

,
(19)
subject to:
ϕ(x) +ψ(y)≤c(x, y).(20)
Special cases include:
•c(x, y) =−⟨x, y⟩, in which case the dual takes a
Legendre-transform-like form:
ψ(y)
∆
= sup
x∈X
(⟨x, y⟩ −ϕ(x)).(21)
•c(x, y) =∥x−y∥ 2, important in quadratic OT and
Brenier’s theorem (will be introduced in section VII).
D. Kantorovich-Rubinstein Distance from Duality
For the special casep= 1, duality yields the classical
Kantorovich-Rubinstein formula:
W1(µ, ν)
∆
= sup
ϕ∈Lip1
Z
X
ϕ(x)dµ(x)−
Z
Y
ϕ(y)dν(y)

,
(22)
whereLip 1 is the set of 1-Lipschitz functions. This dual
form is widely used in machine learning, particularly in the
Wasserstein GAN (WGAN) framework [6].
E. Applications based on the dual properties
The dual formulation plays a central role in economics,
physics, PDE theory, and modern machine learning. Entropic
regularization, for example, modifies the primal LP to yield
smooth and computationally efficient dual objectives, forming
the basis of Sinkhorn algorithms. When the ground costc(x, y)
is metric or convex in its arguments, alternatingc- and¯c-
transforms naturally produces a pair ofc-concave potentials.
Hence, the dual problem can often be reduced to maximizing
over a singlec-concave potential, significantly simplifying
numerical optimization [94]. In summary, the dual problem
provides an elegant and powerful perspective on OT, revealing
the structure of optimal couplings through potential functions
and enabling efficient computational methods across diverse
applications.

7
VII. BRENIER’STHEOREM
Brenier’s theorem is a cornerstone of OT theory, particularly
for the quadratic cost function. It provides powerful conditions
that guaranty the existence and uniqueness of an OT map, and
further shows that this map is the gradient of a convex function
[15], [121]. Up to this point, we have introduced the basic
concepts of Monge and Kantorovich formulations and the
associated dual problems. A natural and fundamental question
in OT is whether an OT map exists. If so, is it unique, and
how is it related to the OT plan? Historically, these questions
have been highly challenging to answer. For many decades it
was unclear whether solutions to Monge’s original formulation
even existed, except in special cases. In the late 20th century,
Brenier resolved these issues in Euclidean spaces for the
quadratic cost, establishing the existence, uniqueness, and
structural form of the optimal map. This achievement is one of
the landmark results in modern OT theory [101], [120]. Later,
Gangbo and McCann extended Brenier’s result to Riemannian
manifolds, greatly broadening its applicability [40]. In this
section, we highlight the conclusions of Brenier’s theorem that
are most relevant for practical applications including machine
learning, where the convex potential is often approximated
using ICNNs [3], [94].
A. Theorem Statement
Letµandνbe two probability measures inR n. Assume
thatµis absolutely continuous with respect to the Lebesgue
measure. Consider the quadratic cost functionc(x, y) =|x−
y|2, then there exists a convex functionφ:R n →Rsuch that
the OT mapT:R n →R n is given by:
T(x) =∇φ(x).(23)
Furthermore, this map advancesµtoνwith meaningT #µ=
ν, or equivalently for every measurable setB⊆R n,ν(B) =
µ(T −1(B)).
B. OT Map
The OT mapT=∇φminimizes the cost of quadratic
transportation:
Z
Rn
|x−T(x)| 2 dµ(x).(24)
Because the cost is strictly convex, any mass at pointxis
optimally transported to a unique pointT(x).
C. Existence and Uniqueness
The convex potentialφis unique up to an additive constant.
Consequently, the OT mapT=∇φis unique almost every-
where with respect toµ. This result gives a complete solution
to Monge’s formulation under the stated conditions. Based on
the above explanations, Brenier’s theorem gives the following
implications:
•Convex Potential Representation.For quadratic cost,
the optimal map is always the gradient of a convex func-
tion. This greatly simplifies analysis and computation.
•Regularity.Ifµandνhave smooth, strictly positive
densities and satisfy the appropriate convexity conditions,
thenφis smooth, and so isT.
•Machine Learning.In modern applications, the convex
potentialφis often parameterized using ICNNs [3], [94],
making Brenier’s theorem a foundation of neural OT
methods.
The theorem answers two classical questions at once: (1)
the existence of an optimal map, and (2) its structural rela-
tionship with the optimal plan. Moreover, whenever a Monge
map exists, it always induces the corresponding Kantorovich
optimal plan.
D. Relationship Between OT Map and Plan
OT theory distinguishes between two objects:
•The OT mapT:X→Y, which gives a deterministic
assignment.
•The OT planγ∈Π(µ, ν), which is a joint probability
distribution describing how mass is transported.
The two concepts are closely related but not always identical.
Brenier’s theorem clarifies this relationship in the quadratic-
cost case. For a strictly convex cost of the form:c(x, y) =
h(x−y)withh(·)convex, the optimal map has the form:
T(x) =x− ∇h−1(∇φ(x)),(25)
whereφis a convex potential associated with the dual prob-
lem. If a unique optimal mapTexists, the map will induce a
plan that is deterministic and given by:
γ= (Id×T) #µ,(26)
whereIdis an identity matrix. In most general cases, ifµ
is not absolutely continuous, or if the cost is not strictly
convex, then an optimal map may not exist. In such cases,
the mass may split: the optimal planγencodes probabilistic
couplings rather than deterministic assignments. For example,
in the deterministic case, if bothµandνhave continuous
densities and the cost is strictly convex (e.g.,|x−y| 2), the
optimal plan is induced by a unique mapT=∇φ. For
discrete distributions, the OT plan is typically a transport
matrixγ. There is generally no single map unless the problem
reduces to a perfect matching. In summary, the OT plan
is the most general object, always guaranteed to exist. The
OT map is a special but highly valuable structure: it exists
under regularity and convexity assumptions, and when it exists,
it fully determines the plan. Brenier’s theorem provides the
precise conditions under which this powerful simplification
holds.
VIII. OPTIMALTRANSPORT INNON-COMPARABLE
SPACES
In previous sections, we discussed OT in settings where
the cost function or distance metric is defined on a shared
space, i.e., both probability measures live on the same un-
derlying domain, allowing distances between samples to be
computed directly. However, many real-world applications
involve probability distributions defined on different, and

8
(a) (b)
Figure 6. OT as graph matching on nodes (a) and edges (b) as conventional
definition of OT and GWOT, respectively.
often non-comparable feature spaces. In such situations, the
classical Wasserstein distance is no longer applicable because
the ground costd(x, y)(instead of usingc(x, y)as a dis-
tance representation) cannot be defined meaningfully. This
motivates the use of Gromov-Wasserstein optimal transport
(GWOT), which compares distributions through the intrinsic
structure of their own metric spaces [102], [119]. Rather
than comparing samples directly, GWOT aligns the pairwise
distances within each space. This concept is illustrated in
Fig. 6, where matching can be operated on either nodes
(in comparable spaces) or edges (in non-comparable spaces).
GWOT is particularly useful for comparing heterogeneous
modalities. For instance, acoustic features, text embeddings,
and video descriptors, each lies in distinct feature spaces
where cross-modal distances are undefined. Yet, intra-modal
distances (within each modality) remain meaningful. GWOT
constructs an optimal coupling by aligning these intra-modal
geometries across modalities. This is conceptually similar to
graph matching, where correspondences between nodes must
also respect the similarity between edges. Moreover, when
temporal structure is present (e.g., in speech or video), GWOT
naturally relates to directed graph matching, because temporal
order introduces directionality into the pairwise relationships.
In this section, we introduce the Gromov-Wasserstein dis-
tance (GWD) and show how it leads to a more general hybrid
formulation known as the fused Gromov-Wasserstein distance
(FGWD), which incorporates both the intrinsic geometric
discrepancy between spaces and the conventional Wasserstein
discrepancy between samples. These tools will later be used
for cross-modal graph matching and knowledge transfer in
ASR applications [90].
A. Gromov-Wasserstein OT
GWOT aligns two metric measurement spaces(X, d X , µ)
and(Y, d Y , ν)by minimizing the distortion between their
respective pairwise distances. In the discrete setting, letD X ∈
Rn×n andD Y ∈R m×m denote the intra-space distance
matrices. GWOT seeks a couplingγ∈Π(µ, ν)such that the
relational structures (i.e., the edges) of the two spaces are best
aligned. The GWOT problem is defined as [102], [119]:
min
γ∈Π(µ,ν)

D

DX ,D Y  ⊗γ, γ  ,(27)
whereD(·)is a distance function. In fully discrete form as:
min
γ∈Π(µ,ν)
X
i,j,k,l
di,j,k,l γi,kγj,l,(28)
where the distortion tensor evaluates pairwise discrepancies:
di,j,k,l :
∆
= D  DX i,j,D Y k,l  .(29)
This formulation emphasizes that GWOT compares struc-
tures (edges) rather than samples (nodes) as a graph matching
schematic point of view conceptually illustrated in Fig. 6. It is
therefore well suited for matching distributions whose supports
are not directly comparable.
B. Fused Gromov-Wasserstein OT
In many applications, both node features and edge struc-
tures provide complementary information. For example, in
multimodal learning, acoustic and text embeddings (node
features) can be compared via a learned cross-modal cost,
while their temporal or relational structures (edges) must
also be considered. To capture both aspects simultaneously,
the fused Gromov-Wasserstein OT (FGWOT) combines the
classical Wasserstein alignment of node features with GW
alignment of pairwise structures. The fused objective is defined
as:
min
γ∈Π(µ,ν)
(1−α)

DX,Y , γ  +α
D

DX ,D Y  ⊗γ, γ  ,(30)
whereD X,Y is the ground cost comparing node features
across spaces (used in classical OT asC X,Y ),α∈[0,1]
balances node-level vs. edge-level alignment, the second term
enforces relational (edge) consistency. Whenα= 0, FGWOT
reduces to classical OT; whenα= 1, FGW reduces to pure
GWOT. Based on this formulation of the fused objective in
Eq. (30), we can observe the following.
•The first term enforces point-wise similarity, aligning
samples across modalities.
•The second term enforces structural similarity, encourag-
ing pairs of points with similar relationships in one space
to correspond to pairs of similar relationships in the other.
•The FGW distance thus behaves like a graph-matching
distance that incorporates both node attributes and edge
structures.
This makes FGWOT particularly suitable for:
•Cross-modal learning (acoustic-text, text-vision, etc.),
•Temporal sequence alignment (speech frames, video
frames),
•Knowledge transfer across heterogeneous architectures,
•Graph matching and graph-based signal processing.
In a later section XIII-F6, we will show the application of
GWOT and FGWOT formulations to cross-modality knowl-
edge transfer in ASR tasks, where acoustic and text dis-
tributions lie in different feature spaces but share structural
relationships that can be exploited through OT.
IX. UNBALANCEDOPTIMALTRANSPORT
In the original definition of OT, marginal distribution con-
straints are required to be kept (Eqs. (7), (8), (10)), i.e., the
masses of source and target should be equal in transport.
These constraints can be relaxed to increase the potential
of OT applications. For example, in cross-modal alignment

9
between acoustic and linguistic distributions, alignment for
matching requires to identify meaningful and reliable corre-
spondences between acoustic and linguistic spaces, acoustic
frames with no corresponding linguistic transcriptions (e.g.,
noisy backgrounds) could be ignored or discarded in matching
to linguistic transcriptions (tokens) [91]. Also in semantic
interactions between sentences through word alignment [5], it
is natural that information inequality exists between sentences.
This requirement fits well to the mathematical theory of un-
balanced OT (UOT), i.e., controlling the marginal distributions
cross modalities during OT. The UOT has been investigated
in [23], [97], [109]. Suppose that the two discrete probability
distributions with weight coefficients are as follows:
µ= (u 1, u2, ..., um)⊤ ∈R m,
ν= (v 1, v2, ..., vn)⊤ ∈R n, (31)
with the pairwise cost matrixC∈R m×n, the UOT is defined
as:
LUOT
∆
= min
γ∈Rm×n +
m,nX
i,j
γi,jCi,j +α 1D(γ1 n||µ) +α 2D(γ ⊤1m||ν),
(32)
where1 m ∈R m and1 n ∈R n are vectors of ones,γ1 n ∈R m
andγ ⊤1m ∈R n are the marginals of row and column ofγ,
D(·∥·)is a Kullback-Leibler (KL)-divergence based distance
function,α 1, α2 ≥0control the penalty on deviation from
the two original marginals, whenα 1, α2 → ∞, equal mass
constraint is guaranteed which is the original definition of OT.
With setting a different threshold ratio to maintain the mass
transport, partial OT (POT) shares a similar function to the
partial alignment between two distributions which has also
been investigated [18].
X. DYNAMICOPTIMALTRANSPORT
In the previous sections, OT was introduced in its static
formulations, where no temporal evolution is considered.
Conceptually, the classical OT problem seeks a transport map
that moves an initial probability distributionρ 0(x)to a target
distributionρ 1(y)with minimal transportation cost. A natural
extension of this idea is to ask: how does a distribution
evolve over time along an energetically efficient path on the
space of probability measures? This perspective introduces an
additional temporal dimension and leads to the framework of
dynamic OT as illustrated in Fig. 7, i.e., the distributions are
changed along a trajectory with time-variant distributionρ t.
In this sense, OT can be regarded as a transport problem on
a manifold of probability distributions, endowed with a well-
defined geometry. The dynamic formulation of OT has a strong
connection to fluid mechanics and optimal control theory [22].
The celebrated Benamou-Brenier formulation interprets OT as
a fluid flow problem, where the goal is to determine both the
evolution of the density and the velocity field that together
transport the fluid from the initial to the final configuration
with minimal kinetic energy [9].
A. Lagrangian and Eulerian Descriptions of Fluid Dynamics
The Benamou-Brenier formulation is based directly on the
principles of fluid dynamics, incorporating both spatial and
𝜌0 𝜌1
𝑥 ∈ 𝜌 0
 𝑦 ∈ 𝜌 1(a)
𝜌0 𝑥,𝑡= 0
(b)
𝜌𝑡 𝑥,𝑡
 𝜌1 𝑥,𝑡= 1
Figure 7. (a) Static OT; (b) Dynamic OT, distribution changes along an
efficient path.
𝑍𝑡 (𝑥;𝑡 0,𝑥 0)
𝑣𝑡 (𝑍𝑡 (𝑥))
𝑥0
(a) (b)
Figure 8. Lagrangian (a) and Eularian (b) point of views for fluid dynamics.
temporal structures of mass evolution [9]. In fluid mechanics,
two complementary modeling viewpoints are widely used, as
shown in Fig. 8:
•Lagrangian description: tracks individual particles
along their trajectories, where each particle is initially
located at positionx 0 at timet 0.
•Eulerian description: studies the evolution of physical
quantities (density, velocity, etc.) at fixed spatial locations
described by a velocity fieldv t.
These two descriptions can be formally linked by a flow
mapZ t(x)that satisfies the differential equation:


dZt(x)
dt =v t (Zt(x)),
Z0(x) =x,
(33)
wherev t denotes the velocity field at timet. The flow map
induces an evolution of densities through the push-forward
operation:
ρt = (Zt)#ρ0.(34)
Hence, a time-varying velocity field generates a corresponding
temporal evolution of the density. As further illustrated in
Fig. 9, intuitively, the velocity field describes the tangent
direction along each streamline of the flow, while the set of
all streamlines describes the motion of a large population of
particles.
B. Continuity Equation in Fluid Dynamics
In fluid dynamics, mass conservation is expressed through
the continuity equation, which governs the evolution of density
ρt(x)under a velocity fieldv t(x)as [106], [120]:
∂ρt(x)
∂t +∇ ·

ρt(x)v t(x)

= 0.(35)

10
𝑍𝑡1 (𝑥)
𝑍𝑡2 (𝑥) 𝑣𝑡1 (𝑥)
𝑣𝑡2 (𝑥)
Figure 9. Velocity as tangent directions along a particle trajectory (a) and on
streamlines of population of particles (b).
Here,∂ tρt represents the rate of change in density, while
∇ ·(ρtvt)describes the divergence of the mass flux generated
by the velocity field. This equation enforces the principle of
mass conservation: mass is neither created nor destroyed, but is
only redistributed in space. In the context of OT, the continuity
equation acts as a constraint linking the density evolution and
the velocity field. It ensures that feasible density pathsρ t
correspond to physically valid mass flows. This continuity
equation forms the basis for understanding how densities
evolve under OT processes, ensuring that the fundamental
conservation laws are satisfied throughout the dynamics which
is frequently mentioned in the later sections.
C. Benamou-Brenier Formulation of Dynamic OT
Based on the above introduction, the dynamic OT problem
aims to find both the density path(ρ t)t∈[0,1] and the velocity
field(v t)t∈[0,1] that transportρ 0 toρ 1 while minimizing the
kinetic energy. The Benamou-Brenier formulation expresses
the squared Wasserstein-2 distance as the optimal value of the
following variational problem [9], [120]:
W 2 2 (ρ0, ρ1) ∆ = min ρ, v
Z 1
0
Z
X
L(v(x, t))ρ(x, t)dx dt

,(36)
subject to the constraints:
ρ(·,0) =ρ 0, ρ(·,1) =ρ 1,(37)
and the continuity equation (35). A common choice for the La-
grangian is the kinetic energyL(v) = 1 2 ∥v∥2. This formulation
reveals that, rather than computing a static coupling, OT with
a quadratic cost is equivalent to finding a time-varying flow
of probability densities that smoothly interpolates between the
two measures along a minimal-energy path. The optimal path
ρt serves as the geodesic betweenρ 0 andρ 1 in the Wasserstein
space.
D. Benamou-Brenier Formula and Gradient Flows in Wasser-
stein Space
The Benamou-Brenier formulation also provides a geo-
metric interpretation of the Wasserstein distance and plays
a fundamental role in the study of gradient flows in the
Wasserstein space. For two probability measuresµ 0 andµ 1,
the dynamic formulation expresses the Wasserstein distance as
[2], [35], [105]:
W 2 2 (µ0, µ1) ∆ = Z 1
0
Z
X
∥∇ϕt(x)∥2 dρt(x)dt,(38)
Push-forward transport:
Flow map
Snap-shot from stochastic process
Generative model
𝜌 𝑥,𝑡= 0 =𝜌 0 𝜌 𝑥,𝑡= 1 =𝜌 1𝜌𝑡
𝜌𝑡 = (𝑍𝑡 (𝑥))#𝜌0
Figure 10. Transport-based modeling with a flow map.
whereϕ t is the time-dependent OT potential and(ρ t,∇ϕ t)
satisfy the continuity equation
∂ρt
∂t +∇ ·(ρt∇ϕt) = 0.
This dynamic formulation plays a central role in modern
analysis and machine learning, enabling:
•Variational formulations of diffusion equations,
•Schr ¨odinger bridge problems,
•Score-based generative modeling and diffusion models,
•Optimal control formulations,
•Continuous-time interpolation between probability distri-
butions.
The Benamou-Brenier perspective therefore provides not
only a physically intuitive framework for OT but also a
mathematically rich foundation for dynamic modeling on the
space of probability measures which plays a crucial role in
understanding the geometry of Wasserstein spaces and pro-
vides a variational characterization of the Wasserstein distance,
connecting it directly to OT maps and gradient flows.
XI. TRANSPORT-BASEDMODELING
In the Benamou-Brenier formulation of OT, the transport
trajectory is described by a deterministic differential equa-
tion whose boundary conditions are given by the initial and
terminal distributionsρ 0 andρ 1. A natural extension of this
idea is to ask: what if the transport trajectory itself follows a
stochastic process? This question leads to the diffusion-bridge
view of OT, most notably expressed by the Schr¨odinger Bridge
Problem (SBP) [20], [22], [73]. In recent years, several gener-
ative modeling frameworks have emerged-including diffusion
models, score-based models, flow matching, and normalizing
flows that all describe transformations between probability
distributions through continuous-time dynamics. These gener-
ative modeling frameworks can be simply described as in Fig.
10. Observations or samples are regarded as snap-shots from
different distributions along time evolutionρ t. Although their
algorithmic motivations differ, these approaches share a unified
structure: each specifies a transport mechanism (deterministic

11
or stochastic) that maps a source distribution to a target distri-
bution under suitable constraints. From this perspective, they
can be collectively viewed as transport-based modeling under
a unified stochastic differential equation (SDE) framework.
In this section, we introduce the key theoretical foundations
underlying these connections, beginning with the Schr ¨odinger
Bridge and diffusion bridges, followed by SDE-based diffusion
models and flow-matching methods, and concluding with a
transfer-operator perspective that further unifies these view-
points.
A. Schr ¨odinger Bridge Problem and Diffusion Bridges
The SBP is the most classical and influential example of a
diffusion bridge. Originally studied by Schr ¨odinger in 1931-
1932, the problem asks for the most likely evolution of a
cloud of particles observed at two time points, with prescribed
initial and terminal marginals. In modern terms, the SBP
seeks a probability law on the space of stochastic paths that:
(i) matches the two marginals, and (ii) is closest in relative
entropy to a given reference process. In Schr ¨odinger’s original
setting, this reference was the standard Brownian motion.
Formally, letP 0:T be the probability law of the reference
process. The SBP seeks a path measureQ 0:T that satisfies the
marginal constraintsQ 0 =ρ 0 andQ T =ρ 1 and minimizes
the KL-divergence [22]:
Q∗ 0:T : ∆ = arg min Q0:T :Q0=ρ0, QT =ρ1 KL(Q0:T ∥P 0:T ).(39)
Intuitively, the SBP constructs a stochastic “bridge” between
the two distributions by perturbing the reference process as
little as possible while still matching the desired marginals.
Thus, SBP can be interpreted as a stochastic analog of OT,
where randomness is explicitly incorporated through diffusion.
1) Reference Process in Schr ¨odinger Bridge:Let the refer-
ence process be an It ˆo diffusion:
dXt =f(X t, t)dt+g(X t, t)dWt,(40)
wheref(X t, t)is a drift term,g(X t, t)denotes diffusion
coefficient, andW t is a Wiener process. The SBP seeks an
alternative processQ, absolutely continuous with respect to
the reference lawP, that minimizes:
inf
Q
EQ

log dQ dP  ,(41)
subject to
Q(X0) =P 0,Q(X T ) =P T .
From the viewpoint of stochastic optimal control, this
minimization induces a controlled SDE:
dXt =f(X t, t)dt+g(X t, t)dWt +u(X t, t)dt,(42)
where the controluis the drift adjustment required to satisfy
the marginal constraints and minimize the relative entropy.
This structure yields a dynamic programming equation closely
related to the Monge-Amp `ere equation in deterministic OT
[17].
2) Connection Between Static OT and SBP via KL-
Divergence:Consider the entropy-regularized OT (entropic
OT) problem defined as (this will be further discussed in
section XII-A for fast computational algorithms):
min
γ∈Π(µ,ν)
Z
c(x, y)dγ(x, y)−λ H(γ)

,(43)
whereH(γ) =−
R
γlogγis Shannon entropy of transport
plans. With re-arrangements, the entropic OT becomes:
min
γ∈Π(µ,ν)
λKL

γ∥e − 1 λ C .(44)
Thus, entropic OT is also a KL projection onto couplings,
with the Gibbs kernele − 1 λ C playing the role of a reference
measure. Comparing this with the SBP’s KL projection onto
a path measureQ 0:T in Eq. (39) reveals a deep equivalence:
SBP is the dynamic version of entropy-regularized OT [73].
This analogy forms the basis of many modern computational
algorithms that unify SBP and entropic OT, enabling tractable
approximations of OT in high-dimensional spaces.
3) Connection Between Dynamic OT and SBP via SDEs:
A general stochastic process is given by the It ˆo SDE as in Eq.
(40), ifg= 0, the dynamics reduce to a deterministic ODE
and correspond to the Benamou-Brenier formulation of OT. If
only the diffusion term is present (as in Brownian motion), the
dynamics describe the original SBP. In the general controlled-
SDE form, SBP can also be expressed as the minimization of
drift energy [20], [22]:
min
f∈U
E
"Z T
0
1
2 ∥f(X t, t)∥2 dt
#
,(45)
subject to the marginal constraints
X0 ∼P 0, X T ∼P T .
Through the Fokker-Planck equation, these Lagrangian
(path-space) formulations have Eulerian (density-space) coun-
terparts. This connection places OT, SBP, and SDEs within a
unified framework of stochastic optimal control [22].
B. Stochastic Differential Equations and Diffusion Models
In physics and applied mathematics, a fundamental question
is how to model interacting particles and describe their tem-
poral evolution. Such systems often exhibit both deterministic
trends and random fluctuations, motivating a probabilistic
formulation of dynamics. SDEs provide a natural and expres-
sive framework for modeling these behaviors, where particle
ensembles evolve as probability distributions that change con-
tinuously over time. The SDEs describe the evolution of a
stochastic processX t with dynamics of the form formulated
in Eq. (40) with two termsfis the drift field,gis the diffusion
coefficient, wheredW t denotes a Wiener process. These
two terms correspond respectively to deterministic flow and
random perturbations. The associated evolution of probability
densities is governed by the Fokker-Planck equation (FPE)
[106]:
∂ρt(x)
∂t =−∇·(f t(x)ρt(x))+ 1 2 ∇·∇(D ij(x, t)ρt(x)),(46)

12
whereD ij(x, t) = [gt(x)g⊤ t (x)]ij. When the diffusion term is
spatially independentg t(x) =σ(t), the equation reduces to:
∂ρt(x)
∂t +∇ ·(ft(x)ρt(x)) = σ2(t) 2 ∆ρt(x).(47)
This equation describes how the probability density func-
tion evolves over time as a result of the combined effects
of drift and diffusion in the stochastic process. The term
∇ ·(ft(x)ρt(x))represents the drift-induced transport of
probability density, while σ2(t) 2 ∆ρt(x)accounts for the spread
of the diffusion of the density. In the stochastic process, if
the drift term is zero, i.e., no drift field, the FPE follows
the diffusion process only. If the drift term is not zero, the
probability density will shift from their original positions as
well with diffusion. Therefore, in a SDE, it can manipulate
complex probability density changes with controlling the drift
and diffusion terms. That is why it is convenient to use SDEs
for generative modeling in machine learning.
The FPE, also known as the Kolmogorov forward equation,
in the context of OT theory, plays a crucial role in describing
the evolution of probability densities associated with stochastic
processes underlying OT problems. OT theory provides a natu-
ral framework to study how probability distributionsµ t evolve
under SDEs. The Wasserstein distanceW p(µt, νt)between
two distributionsµ t andν t quantifies the minimum cost of
transformingµ t intoν t. This connection is essential because
OT seeks to find the most efficient way to transport one
probability distribution to another, and stochastic processes
described by such equations naturally arise in this context. The
FPE thus provides a mathematical framework for analyzing the
evolution of probability distributions and their relation to OT
problems.
Modern diffusion-based generative models leverage SDEs to
construct a forward noising process and a learned reverse pro-
cess. The forward SDE gradually perturbs the datax 0 ∼p(x)
(usually the original data distribution) into a simple Gaussian
distribution over timeT. The reverse-time SDE reconstructs
the data by denoising [4], [115]:
dxt =

f(x t, t)−g(t)2∇xt logp t(xt)  dt+g(t) dw t.(48)
Here,p t(xt)is the marginal distribution ofx t at timet,
∇x logp(x)is a score function, the gradient of the log-density
of data distribution. The training objective is often formulated
as a variational bound on the negative log-likelihood, which
can be optimized using stochastic gradient descent [114],
[115]. However, these methods can be computationally ex-
pensive and may struggle with high-dimensional data. Neural
score matching addresses these challenges by directly learning
the score function using a neural network [50], [54], [55], [80],
[115]. This approach leverages the expressive power of neural
networks to model the score function across various noise
levels, allowing more accurate and efficient data generation.
The core idea behind neural score matching is to train a
neural networks θ(x, t)to approximate the score function
∇x logp t(x)at each time stept. Given a data set{x i}N i=1,
the training objective is to minimize the score matching loss
defined as:
L(θ) =E t∼U(0,T)
x0∼p0(x0)
xt∼pt(xt|x0)

w(t)|sθ(xt, t)− ∇xt logp t(xt|x0)|2 ,
(49)
wherew(t)is a weighting function that can be tuned to empha-
size different levels of noise during training, andp t(xt |x 0)
denotes the distribution of noisy data at timetconditioned
on the original datax 0,tbelongs to a uniform distribution
in the interval ast∼ U(0, T). In practice, the true score
function∇ xt logp t(xt |x 0)is intractable. Instead, it can
be estimated by adding Gaussian noise to the data and using
the score matching objective to learn a close approximation.
Once trained, this network can be used to perform denoising
at each time step, effectively reversing the diffusion process
[49], [115].
C. Normalizing Flow and Flow Matching
Flow matching provides a simulation-free alternative to
SDE-based generative models developed from the idea of
simplified normalizing flow. When the diffusion term in the
FPE (Eq.47) is zero, the density evolution reduces to the
continuity equation corresponding to an ordinary differential
equation (ODE):
dZt (x)
dt =v t (Zt (x)),(50)
whereZ t is a transport field or flow map generated by the ODE
withv t(·)as its velocity field. The evolution of the associated
density is given by the change-of-variables formula as in a
normalizing flow [50], [79], [80]:
ρt(x) =ρ 0

Z −1 t (x)  det  ∂Z −1 t ∂x  .(51)
In flow matching and normalizing flow models, the goal is to
learn a parameterized velocity field:
vt(Zt(x))→v t(Zt(x);θ),
such that pushing forward a simple base distribution (e.g., a
Gaussian) along the learned flow produces a complex target
distributionρ t(x), and learning model parameters with maxi-
mizing negative log-likelihood of parameterizedρ t(x;θ). This
viewpoint unifies several key concepts as shown in Fig. 11. As
shown in this figure, the velocity field governs the evolution of
particles through an ODE, the flow map-solution of the ODE,
pushing forward probability mass, continuity equation links
density evolution and the velocity field. The push-forward
operator maps the initial densities to the future densities.
Other transport-based methods can be understood as instances
of ODE/SDE-driven probabilistic transport [21], for example,
Diffusion Probabilistic Model (DPM), Denoising Diffusion
Probabilistic Model (DDPM) [49], Continuous Normalizing
Flow (CNF) [62], Conditional Flow Matching (CFM) [79],
Rectified Flow Matching (RFM) [82], etc., all share common
tasks or purposes, and can be explicitly unified as in Fig.
12. From this figure, we could figure out the relationship
between different generative model frameworks proposed in

13
Flow map
Probability paths Velocity field
Continuity equation
Flow mapVelocity field
Solving ODEPush-forward
𝜌𝑡 =(𝑍𝑡(𝑥))#𝜌0
𝜕𝜌𝑡 (𝑥)
𝜕𝑡 +∇. (𝜌 𝑡 (𝑥)𝑣𝑡 (𝑥)) = 0
Figure 11. Unified concepts in flow mapping via ODEs.
SDE�Stochastic diffusion model
(DPM, DDPM, etc.)
ODE�Flow matching
(CNF, CFM, RFM, etc.)
Removing stochastic dynamics
Fokker-Planck
equation
Continuity equation
Figure 12. Unified concepts with diffusion and flow matching models via
SDEs/ODEs.
recent years, as well as their relationship with OT [33], [65],
[82], [118].
D. Transfer Operator Perspective
In the previous subsections, dynamics was described via
SDEs or ODEs, which require knowledge of drift and diffusion
terms. An alternative viewpoint uses transfer operators with
the mathematical insight that a dynamic system intrinsically
determined by a differential equation even with complex
nonlinearity might correspond to a linear operator, i.e., the
Koopman operator, which characterizes system evolution with-
out explicitly referencing the underlying governing equations.
The idea is illustrated in Fig. 13. The evolution of the state
Xt ∈R n under nonlinear dynamicsΨ :R n →R n is
formulated as:
Xt+1 = Ψ (Xt).(52)
For a space of measurement or observable functions defined
asG:={F:R n →R}, where the element of the real-valued
Observable functions (lifting)
Linear dynamicNonlinear dynamic
𝐾𝜓 𝐹 ≔ 𝐹 ∘ 𝜓
𝑌=𝐹(𝑋)
𝐹 ∘ 𝜓 𝑋𝑡 =𝐹 𝑋𝑡+1 =𝐾 𝜓 𝐹(𝑋𝑡 )
𝑌𝑡+1 =𝐾 𝜓 𝑌𝑡
𝑋𝑡+1 =𝜓(𝑋 𝑡 )
𝑋0 𝑋1 𝑋2
𝑋𝑇
𝑌0
𝑌1
𝑌2
𝑌𝑇Composition operator
Figure 13. Transfer operator point of view for state dynamics.
measurement function isY=F(X)taking values in the state
space, the Koopman operator (composition operator)K Ψ :
G → Gis defined as [16]:
KΨF:=F◦Ψ.(53)
By this Koopman operator, the evolution of dynamics in
the whole lifting space (an infinite-dimensional space of the
collection of observable functions) is linearly represented as:
Yt+1 =K ΨYt.(54)
That is to say, the Koopman operator captures the evolution of
observables under nonlinear dynamics through a linear infinite-
dimensional operator, and it is defined as the composition of
observable with the flow induced by the dynamic system (in
practice, Koopman operator can be approximated by a finite-
dimensional matrix with data-driven based algorithms, e.g.,
Extended Dynamic Mode Decomposition (EDMD) algorithm
[129]). A much more clear explanation is shown in the bottom
panel of Fig. 13 where the nonlinear dynamics could be
analyzed in a linear space with the Koopman operator acting
on scalar-valued functions driven based on the dynamics rather
than on the original states. The adjoint of the Koopeman oper-
ator, the Perron-Frobenius operator, describes the evolution of
probability densities with uncertainty of the initial condition
through the propagation of a dynamic system [71]. It induces
a measure-preserving transform of a probability density as
a push-forward map. This viewpoint connects naturally to
OT and SDE dynamics: the Perron-Frobenius operator cor-
responds to density evolution (Eulerian point of view), the
Koopman operator corresponds to observable evolution (La-
grangian point of view), the FPE is a PDE representation of the
same evolution, and SBP and entropic OT correspond to KL
projections of path or density evolution. Thus, OT, SBP, SDE-
based generative models, and transfer-operator approaches
fit within a common theoretical framework for modeling
the transport and evolution of probability distributions. In
summary, optimal transport, diffusion processes, and transfer-
operator analysis form a coherent theoretical framework that
connects probability flows, stochastic control, and generative
modeling via analysis of SDEs which is an exciting field for
further exploration.
XII. COMPUTATIONALALGORITHMS FOROPTIMAL
TRANSPORT
The practical applications of OT in engineering, machine
learning, and data science require efficient numerical algo-
rithms. Classical OT formulations lead to large-scale linear
programs, whose computational cost can be prohibitive for
modern datasets. We first recall that the discrete Kantorovich
OT problem is a linear program. Thus, many classical LP
solvers can be directly applied, for example:
•Network Simplex Method:A variant of the simplex
algorithm tailored for network flow, effective for medium-
scale OT problems.
•Interior Point Methods:Algorithms that traverse the
interior of the feasible polytope, providing strong theo-
retical guaranties for solving large-scale LP problems.

14
•Classical Simplex Solvers:Applicable but often pro-
hibitively slow for dense OT matrices of large size.
Although theoretically sound, these methods scale poorly: the
cost of solving an×nOT problem is typicallyO(n 3)[101],
which historically limited the use of OT in large-scale machine
learning. During the past decade, significant progress has been
made in designing fast, scalable OT solvers, which has greatly
accelerated the adoption of OT in machine learning, graphics,
geometry processing, domain adaptation, scalable OT, Wasser-
stein GANs, and statistical modeling. Many researchers and
studies have contributed foundational algorithms and open-
source tools that made OT widely usable in practice [58],
[101]. Among them, a major breakthrough came in 2013 when
Cuturi introduced entropy-regularized OT and the Sinkhorn
algorithm [28], [56], [112]. This approach dramatically re-
duces computational cost and is often referred to as “optimal
transport at light speed” [28]. Since then, entropic OT has
become one of the most widely used computational algorithms.
First, let us introduce the concept of entropy-regularized OT.
A. Sinkhorn Algorithm for Entropy-Regularized OT
Given probability measuresµandνin spacesXandY,
with transport plansγ∈Π(µ, ν), the OT plan based on the
entropy-regularized OT problem (EOT) is defined as follows:
γ∗ ∆ = arg min
γ∈Π(µ,ν)
Z
c(x, y)dγ(x, y)−λ H(γ)

.(55)
HereH(γ)is the Shannon entropy defined as:
H(γ) =−
Z
γ(x, y) logγ(x, y)dx dy.(56)
Equivalently, it can be expressed using the KL-divergence:
γ∗ ∆ = arg min
γ∈Π(µ,ν)
{⟨γ, C⟩+λKL(γ|µ⊗ν)},(57)
where the KL-divergenceKL(γ|µ⊗ν)is defined as:
KL(γ|µ⊗ν)
∆
=
Z
X×Y
γ(x, y) log
 γ(x, y)
µ(x)ν(y)

dx dy.(58)
The Sinkhorn algorithm is a powerful method for efficiently
computing approximate solutions to the entropy-regularized
OT problem. This formulation introduces an entropy term
to the traditional OT cost function, promoting sparsity and
numerical stability in large-scale applications [28]. For the
discrete case in real implementation, the formulation is given:
•Two discrete measuresµ= Pm i=1 aiδxi andν=Pn
j=1 bjδyj with positive massesa i andb j, and locations
xi andy j.
•Cost matrixCwhereC ij =c(x i, yj), representing
pairwise transportation costs.
•Regularization parameterλ >0to control the regulariza-
tion strength of the entropy.
The EOT problem becomes:
EOTλ(µ, ν)
∆
= min
γ∈Π(µ,ν)
(⟨γ, C⟩ −λH(γ)),(59)
whereH(γ) =− P ij γij(logγ ij −1). With defining the Gibbs
kernel as:
K=e −C/λ,
the Sinkhorn algorithm alternates between row and column
scaling/normalization:
u(k+1) = a Kv(k) ,v (k+1) = b K⊤u(k+1) ,(60)
wherea= [a 1, a1, . . . am]andb= [b 1, b1, . . . bn]are the
marginal weight coefficients defined on sample locations in
XandY. The transport plan is then obtained as:
γ∗ = diag(u)Kdiag(v),(61)
whereuandvare two scaling (or re-normalization) vectors.
This procedure is equivalent to performing iterated Bregman
projections onto the marginal constraints. Sinkhorn’s original
scaling algorithm dates back to 1964, but its use for OT was
popularized only recently due to its remarkable efficiency,
stability, and compatibility with GPU acceleration [28], [101].
The advantages of this Entropy regularization are summarized
as follows:
•Smoothness:Entropy spreads the mass across the sup-
port, avoiding degeneracy.
•Strict convexity:Providing a unique solution.
•Stability:Prevents numerical collapse of the transport
plan.
•Scalability:Transforming an OT into a diagonal matrix-
scaling problem allows fast GPU parallelization.
Many computational OT algorithms are inspired by this
Entropy-regularized OT algorithm with algorithmic variants
and improvements, including Iterative Bregman Projections
(IBP) [10], Bregman ADMM [127], IPOT(Inexact Proximal
Point OT) [131], etc. IPOT is particularly useful when no
entropic smoothing is desired, since it approximates the exact
OT solution via proximal iterations without requiring ex-
tremely smallλ. Moreover, a more general regularization of
OT beyond entropy can be formulated as:
γ∗ ∆ = arg min
γ∈Π(µ,ν)
{⟨C, γ⟩+λReg(γ)}.(62)
Depending on the prior structure, different regularizersReg(γ)
may be used, for example, Low-rank OT [107], Sparse OT
[12], [83], Laplacian-regularized OT [36], Group-Lasso regu-
larized OT [12], etc. Regularization lets practitioners embed
structural priors (smoothness, sparsity, geometry) into the
transport plan, enabling OT to be adapted to specific appli-
cation domains. In real applications, we need to deal with the
numerical instability problem. As Sinkhorn iterations involve
exponentials and divisions, making numerical underflow or
overflow common. Stability is often improved through log-
domain Sinkhorn iterations, cost scaling, stabilization through
absorbing constants (as in log-sum-exp), GPU-friendly nor-
malization [101].
B. Neural Optimal Transport
Neural Optimal Transport (Neural OT) integrates deep
learning with OT by parameterizing potentials or transport
maps using neural networks [66], [67], [94], particularly
with neural solver algorithms by connecting deep network

15
architecture with ODE [21]. This makes OT feasible in high-
dimensional spaces where classical solvers struggle. A com-
mon approach parameterizes the Kantorovich potentialϕ(x;θ)
via a neural network. Based onc-transform, the dual OT
problem becomes:
max
ϕ
Z
ϕ(x;θ)dµ(x) +
Z
ϕc(y;θ)dν(y)

,(63)
where thec-transform is defined as (refer to the dual property
of OT in section VI):
ϕc(y;θ) ∆ = sup
x∈X
(c(x, y)−ϕ(x;θ)).(64)
Neural networks allow flexible, high-capacity approxima-
tions of optimal potentials. For the quadratic costc(x, y) =
1
2 ∥x−y∥ 2, based on Brenier’s theorem: the optimal Kan-
torovich potential is convex, the optimal OT map is the
gradient of this potential. Thus, neural OT often parameterizes
f(x;θ)as an ICNN [3], [94]:
inf
f∈cvx(X)
Z
f(x;θ)dµ(x) +
Z
f ∗(y;θ)dν(y)

,(65)
where the convex conjugatef ∗(y;θ)is defined as:
f ∗(y;θ) ∆ = sup
x
(⟨x, y⟩ −f(x;θ)).(66)
The primal OT formulation is the following.
inf
γ∈Π(µ,ν)
Z 1
2 ∥x−y∥ 2 dγ(x, y),(67)
and the dual formulation connects directly to the neural
parameterization above. Neural OT methods therefore provide
scalable tools for Wasserstein distance estimation, generative
modeling, domain adaptation, barycenter computation, and
gradient-based optimization in OT geometry.
XIII. APPLICATIONS OF OPTIMAL TRANSPORT IN SPEECH
This section provides a comprehensive review of how OT
has been applied in modern speech-processing tasks. We
first explain the use of OT in speech signal processing with
reference to its applications in machine learning, where the
applications can be broadly categorized into two paradigms:
(i) employing OT as a loss function to guide model train-
ing and (ii) using OT for domain adaptation or distribution
alignment. Following this, we present a series of successful
applications that illustrate the effectiveness of OT in real-world
scenarios. These include cross-domain and multi-modal speech
enhancement [52], [77], cross-domain speaker and language
recognition [87], [122], [133], [136], cross-corpus or cross-
language emotion recognition [135], domain-adaptive audio
spoof detection [134], [138], and cross-modal knowledge
transfer for ASR [86], [88]–[90]. Finally, we discuss emerging
research trends and potential future directions, highlighting
how OT may continue to advance speech processing in increas-
ingly complex, multi-domain, and multi-modal environments.
𝜌0 𝜌1
Figure 14. Distance measure and transform between distributions.
A. Recall of OT for Machine Learning
In machine learning, many problems can be viewed through
the lens of three fundamental operations: (i) estimating distri-
butions from observed data, (ii) sampling from these distribu-
tions, and (iii) transforming or manipulating one distribution
into another. OT is particularly relevant to the third operation.
For example, as illustrated in Fig. 14, given observations from
two distributionsρ 0 andρ 1, how can we evaluate their simi-
larity either for classification or generation tasks. It provides
both a principled geometric measure of discrepancy between
probability distributions and a framework for constructing
transport maps or interpolation paths between them. Because
of this, OT shares conceptual similarity with a wide class of
generative modeling techniques whose goal is to transform
one distribution into another. Examples include Generative
Adversarial Networks (GANs) [41], Variational Autoencoders
(V AEs) [60], [61], normalizing flows [62], [100], diffusion
models [49], diffusion Schr ¨odinger bridges [14], [110], and
flow matching approaches [79]. OT provides a geometrically
grounded alternative or complement to these methods.
In speech signal processing, the use of OT typically falls
into two major categories: OT as a loss function within
the learning objective and OT as a discrepancy metric for
cross-domain or modality knowledge transfer and adaptation.
Traditional loss functions, such as sample-wise metrics (e.g.,
Mean Square Error (MSE), Mean Absolute Error (MAE), or
task-specific measures, like Signal-to-Noise Ratio (SNR) and
Signal-to-Distortion Ratio (SDR), do not explicitly consider
the geometry of the underlying data distributions. In the
following subsection, we highlight the advantages of incor-
porating OT into learning objectives.
B. Conventional Loss Functions vs. OT-Based Losses
A central objective in machine learning is to quantify the de-
gree to which the predicted distribution deviates from the true
data distribution. Conventional losses such as Cross-Entropy
(CE), KL-divergence, and Jensen–Shannon (JS)-divergence are
widely used, but they often fail to account for geometric
relationships between target outcomes. For example, misclassi-
fying a car as a truck incurs the same penalty as misclassifying
a car as a dog (as illustrated in Fig. 15), although the former
error is semantically and geometrically much closer. A key
advantage of OT is that it incorporates the geometry of the
sample space directly into the loss function as illustrated
in Fig. 16. Wasserstein distances, for example, compute the
minimal cost of transporting mass from one distribution to
another along geodesic paths in Wasserstein space. Unlike KL-
divergence or JS-divergence, which are not true metrics and

16
1
0
0
0
0
1
0
0
0
0
1
0
0
0
0
1
Figure 15. Equal distance between different categories (no information of
category geometric relationship).
Figure 16. Geodesic distance in Wasserstein space.
require overlapping supports, OT defines a proper distance
even when the two distributions have disjoint supports. The
well-known OT distances used in ML include the Earth
Mover’s Distance (EMD) and the Wasserstein distance. A
notable example demonstrating the value of OT in represen-
tation learning is the Word Mover’s Distance (WMD) [70],
which computes the similarity of the document by measuring
the minimum amount of “work” required to move embedded
words from one document to another in the word2vec space.
This approach effectively aligns semantically related words
before measuring their distance, illustrating the geometric
insight that OT introduces. In speech processing, OT can also
be used as an auxiliary alignment loss. For example, instead
of relying solely on the Connectionist Temporal Classification
(CTC) loss in speech translation, OT has been added to en-
force alignment between speech and text embeddings, yielding
significant improvements [72].
C. Cross-Domain Adaptation and Transfer Learning
The second major application of OT in machine learning
is domain adaptation. Domain mismatch is a widespread
challenge in many learning problems. In computer vision,
for example, images collected under different lighting or
camera conditions often lead to severe degradation when
models trained in one domain are applied directly to another.
Similar issues arise in speech processing tasks. In speech en-
hancement, mismatches between training and testing acoustic
conditions frequently occur; in spoken language or speaker
recognition, channel, language, and environmental variations
all contribute to domain shift.
1) Cross-domain adaptation:In domain adaptation, we
assume that labeled data are available only in the source
domain, whereas in the target domain only unlabeled data are
observed. The model trained solely on the source domain is
then expected to generalize to the target domain. Classical
learning theory implicitly assumes that training (source) and
Source domain Target domain
Classification boundary
(a) (b)
Figure 17. Domain adaptation: solid vertical line denotes the classification
boundary trained on source domain data (a), while the dot vertical line
represents the classification boundary on target domain data (b).
test (target) samples are drawn from the same underlying
distribution. However, as conceptually illustrated in Fig. 17,
the source and target distributions can differ significantly.
Using a classifier trained on the source domain directly on the
target domain inevitably leads to performance degradation. To
mitigate this issue, unsupervised domain adaptation (UDA)
seeks to reduce the discrepancy between source and target
distributions. Let the joint distribution of featuresxand labels
ybe denoted asp(x,y). For a joint distribution:
p(x,y) =p(x)p(y|x) =p(y)p(x|y).
Depending on which part of the joint distribution changes
across domains, several types of domain shift can arise (with
ps(·)andp s(·)representing distributions in the source and
target domains, respectively) [68]:
Label/target shift:
ps(y)̸=p t(y), p s(x|y) =p t(x|y).
Covariate/feature shift:
ps(x)̸=p t(x), p s(y|x) =p t(y|x).
Concept shift:
ps(y|x)̸=p t(y|x), p s(x) =p t(x).
Conditional shift:
ps(x|y)̸=p t(x|y), p s(y) =p t(y).
Conditional-target shift:
ps(x|y)̸=p t(x|y), p s(y)̸=p t(y).
OT provides a rigorous foundation for mitigating these types
of shifts. Let the source and target domains be associated with
probability measuresµ s andµ t, respectively, and for samples
from the source and target domainsx s ∈X s,x t ∈X t, let
c(xs, xt)be a cost function measuring sample dissimilarity.
OT seeks a transport planγminimizing the total transportation
cost:
inf
γ∈Π(µs,µt)
Z
Xs×Xt
c(xs, xt)dγ(x s, xt),(68)
whereΠ(µ s, µt)is the set of couplings with the prescribed
marginals. The resulting transport plan or map can be used
for:
•Feature alignment: mapping features from the source to
the target domain.

17
•Instance reweighting: assigning importance weights to
source samples to match target distribution.
•Model adaptation: transformation of decision boundaries
according to the aligned feature space.
OT offers several advantages for domain adaptation: (1) it
provides a mathematically principled discrepancy measure;
(2) it incorporates geometric structure of distributions; (3) it
accommodates distributions with partially overlapping support.
However, challenges remain, including computational cost,
sensitivity to outliers, and the need to select an appropriate cost
function. Among the most influential works is the OT-based
domain adaptation pipeline proposed in [26]. The method
consists of three steps: (i) estimate the OT planT(·)between
the source and target distributions; (ii) transport the labeled
source samples to the target domain; (iii) train a classifier in
the transformed space with labels preserved as:
ps(y|xs) =p t(y|T(x s)).(69)
2) Domain adaptation in the deep learning framework:In
deep learning, a model can be viewed as the composition of
a feature extractor and a classifier formulated as:
y(x) =f(x;θ fc , θffea ) =f c ◦f fea (x),(70)
wheref fea :X → Zextracts latent featuresz=f fea(x),
andf c :Z → Ymaps the features to the label probabilities,
whereθ fc andθ ffea are their corresponding model parameters.
Domain adaptation typically aims to find a latent space where
the joint distributions align:
ps(z,y)≈p t(z,y),(71)
where
pm(z,y) =p m(y|z)p m(z),(72)
withm∈ {s, t}belongs to the source or target domains. The
expected risk in the target domain satisfies [25], [68], [81]:
Rt(f)≤R s(f) +L ffea (ps z, pt z) +R y,(73)
whereL ffea measures the distribution discrepancy in the latent
space, andR y reflects the mismatch of labeling functions.
Most studies aim to reduce this upper bound by minimizing
both the source-domain classification error and the distribution
discrepancy.
D. Domain-Invariant Representation Learning
The goal of domain-invariant representation learning is to
discover a latent space where feature distributions of source
and target domains become similar. There are two families
of approaches: discrepancy-based methods and adversarial
learning-based methods.
1) Minimizing distribution discrepancy:In this framework,
the model parameters are obtained by minimizing:
L(θffea , θfc )
∆
=
X
i
Ls CE(ys i , ˆys i ) +λ feaLffea (ps z, pt z),(74)
where the second term aligns the feature distributions with a
weighting coefficientλ fea. The methods based on Maximum
Mean Discrepancy (MMD)-based and Central Moment Dis-
crepancy (CMD) belong to this category [84], [99], [108].
2) Domain adversarial learning:Another approach uses
adversarial training, where a domain discriminatorf d(·)(with
model parametersθ fd) attempts to distinguish between the
source and target features, while the feature extractor attempts
to make them indistinguishable [39]. The objective is as
follows.
L(θffea , θfc , θfd)
∆
=
X
i
Ls CE(ys i , ˆys i )
−λ d
X
zi∈{Ds∪Dt}
Lfd(fd(zi), di),
(75)
with the standard min–max optimization:
(θ∗ ffea , θ∗ fc ) ∆ = arg min θffea ,θfc L, θ ∗ fd ∆ = arg max θfd L.(76)
3) OT-guided learning in deep neural networks:Al-
though moment-matching and adversarial approaches can align
marginal feature distributions, they typically ignore the geo-
metric structure of multimodal distributions, potentially de-
grading class discriminability. OT-based approaches explicitly
model geometric relationships and have shown a strong per-
formance in domain adaptation [26]. Using the Kantorovich-
Rubinstein duality, the Wasserstein distance becomes [111]:
Lh(ps z, pt z) ∆ = sup
h∈Llip
Ez∼psz [h(z)]−E z∼ptz [h(z)],(77)
whereh∈ L lip meanshbelongs to the set of 1-Lipschitz
functions. In practice, a neural network approximatesh, and
the empirical loss is:
Lwd(zs,z t) ∆ = 1 |Ds| X zi∈Ds h(zi)− 1 |Dt| X zi∈Dt h(zi),(78)
with a gradient penalty enforcing the Lipschitz constraint:
Lgrad(˜z)
∆
=(∥∇˜zh(˜z)∥2 −1) 2.
The resulting min–max optimization is:
Lh
∆
= min
θffea
max
θh
Lwd(zs,z t)−α lipLgrad(˜z),(79)
whereα lip is the weighting coefficient,|D s|and|D t|denote
the number of samples from source and target domains. To
additionally incorporate label information, Joint Distribution
OT (JDOT) framework has been proposed which aligns both
features and labels [27], [29]. Inspired by JDOT, an OT-based
domain adaptation model has been proposed for cross-domain
speaker/language recognition, building upon pre-trained x-
vectors, achieving strong performance [87] (will be introduced
in more details in section XIII-G).
A summary of the overall computational pipeline is illus-
trated in Fig. 18. As shown in this figure, there are two loss
objectives to be estimated, one is the source classification loss,
and the other is domain feature distribution discrepancy loss.
The OT part is a layer in the forward estimation. The Sinkhorn
layer is used to estimate the optimal coupling or plan, and then
multiply with Cost matrix to obtain the domain discrepancy
loss. In the back propagation step, there is no parameter
updated in this OT layer, that is, the back propagation jump
to the front layers for feature representation learning.

18
OT
Cost matrix
Source
Target
Source classification loss
Optimal coupling
Figure 18. General computational framework with an OT embedding layer.
E. OT for Speech enhancement
Speech enhancement (SE) aims to transform distorted or
noisy speech to clean ones. Deep learning-based model frame-
works for SE try to estimate the transform function with a
large quantity of noisy-clean speech pairs, and use the learned
transform function for SE in various test conditions. In real
application, there is a mismatch between training and testing
conditions which results in degraded performance. Cross-
domain adaptation techniques are usually applied to mitigate
domain-gaps. Moreover, conventional learning frameworks
only try to learn the SE transform function from acoustic
signal aspect, while linguistic or semantic information, another
modality of speech besides acoustic aspect, should play an
important role in speech intelligibility or understanding in
adversarial environments. Therefore, cross-modal knowledge
transfer during the SE transform function learning should
be considered, particularly when many pretrained large lan-
guage models encoding linguistic or semantic knowledge have
already been available. In both cases, OT takes a suitable
position in designing loss function or as a measure of do-
main/modal discrepancy measurement.
1) Wasserstein distance-based Phone-Fortified Perceptual
Loss for SE:Traditionally, deep learning-based SE is for-
mulated as a sample-to-sample mapping regression task, i.e.,
transforming a noisy sample into a clean instance. On the other
hand, OT formulates the SE as a distribution mapping task,
i.e., transforming the distribution of noisy speech signal to
a clean one. We may combine these two types of mapping
process to achieve better enhancement performance. Based on
this consideration, a learning framework has been proposed
and explained in Fig. 19 [52]. In this figure, ‘wav2vec’ is
a pretrained model block [7]. This block is used to explore
latent space which is supposed to encode rich phonetic and
semantic information for speech intelligibility. A loss function
shown in this figure ‘WD’, Kantorovich-Rubinstein dual form
of W-distance is specially designed as:
LWD
∆
= sup
∥h∥L≤1
Ez∼µ [h(z)]−E ˆz∼ν[h(ˆz)],(80)
wherez=ϕ wav2vec(y),ˆz=ϕ wav2vec(ˆy), andϕ wav2vec(·)
is a transform function of the wav2vec block, functionh(·)
belongs to a set of all 1-Lipschitz functions. The conventional
MAE loss is defined as:
LMAE
∆
= ||y−ˆy||1.(81)
SE Model Wav2Vec
Wav2Vec
WD
𝑦
𝑦
Clean
Noisy
MAE
Figure 19. SE model framework enhanced with Phone-Fortified Perceptual
Loss (PFPL) in a transformed latent space, WD: Wasserstein distance, MAE:
mean absolute error.
The proposed Phone-Fortified Perceptual Loss (PFPL) for
SE is defined as:
LPFPL(y,ˆy)
∆
= LMAE +L WD.(82)
In this definition, the OT loss (distribution-based mapping)
and MAE loss (sample-based mapping) are composed in the
estimation of the SE model. The OT-based loss defined on
wav2vec explored latent feature could help to capture rich
discriminative power of different phones for improving speech
intelligibility. By implementing the SE model with U-net, SE
experiments were carried out and showed that the proposed
PFPL loss could enhance the SE performance, and has high
correlations with the evaluation metrics PESQ and STOI
scores [52].
2) Discriminator-constrained OT network for cross-domain
SE:For mitigating domain mismatch, adversarial training
is widely applied in machine learning field. In adversarial
training, adaptive distance objective functions based on OT
could be designed in adaptation. However, most studies based
on OT for domain adaptation are for classification tasks,
while adaptation in SE is a regression which is a difficult
task since we need to maintain accurate speech structures. In
the study [77], an OT-based learning framework for SE with
an discriminative training was designed, i.e., discriminator-
constrained optimal transport network (DOTN), for improving
the speech quality. The proposed model framework is showed
in Fig. 20. As shown in this figure, the model framework
consists of an OT-based domain adaptation module and a
discriminator. The adaptation module is designed based on the
following minimization process, where an OT-based alignment
objective function is involved in:
min
γ,f
(LRec +L Align),(83)
where target estimation loss and alignment losses are designed
as:
LRec
∆
= 1 N s X i ||ys i −f(x s i )||2,(84)
and
LAlign
∆
=
X
i,j
γi,j(αx||xs i −x t j||2 +β y||ys i −f(x t j)||2),(85)
wheref(·)is a target estimator,γ i,j is OT coupling,α x and
βy are the weighting coefficient for feature and label. Mini-
mization ofL Rec tries to remind the source domain knowledge

19
Target domain
Source domain
Input
(𝑥𝑠 ,𝑦 𝑠 ),𝑥 𝑡 Output 𝑓(𝑥𝑡 )
𝑦𝑠
Target estimator𝑓(. ) Discriminatorℎ(. )
Figure 20. Discriminator-constrained OT network for SE.
to avoid the catastrophic-forgetting issue, whileL Align is used
for domain alignment. The domain discriminator is designed
by following the algorithm of WGAN as [6]:
min
f
max
h∈Llip

Ey∼PY s (h(y))−E x∼PXt (h(f(x))

,(86)
whereh∈ L lip meanshbelongs to the set of 1-Lipschitz
functions. This proposed DOTN model combines OT and
GAN is the first work that performs purely unsupervised SE
domain adaptation, and obtained better performance than ex-
isting weakly-supervised domain adaptation approaches [77].
3) Cross-modal knowledge transfer for SE:During speech
communications, besides acoustic speech, visual cues, body
gestures, and linguistic knowledge are also involved to remove
confusion in real communications, particularly in adversarial
environments or communication scenarios. Therefore, SE with
multi-modality information, i.e., visual, acoustic speech, and
text for designing SE algorithms have been intensively in-
vestigated in recent years. Conventional SE methods try to
estimate the mapping function based on speech signal only, it
is possible to encode the linguistic information in estimating
the mapping function for SE, particularly a lot of pretrained
large language models (LLMs) have been available. Here
shows a multi-modal knowledge transfer learning framework
for SE [78] in Fig. 21. In this multi-modal SE framework,
besides integrating video information and audio from a camera
and microphone, linguistic information is provided during
enhancement model training stage. And the linguistic informa-
tion, audio and video information are integrated via a cross-
model matching process where cross-modal matching could
be adopted [78]. Since the enhancement model has already
encoded the linguistic knowledge, text information is not re-
quired in inference stage [53]. With this cross-modal learning
paradigm, the performance of SE has improved significantly
[53], [78].
F . Cross-modal knowledge transfer for ASR
Linguistic knowledge information is one of the most im-
portant information in ASR. Fig. 22 shows a conventional
two-stage pipeline for ASR where a language model (LM)
encoding linguistic knowledge is involved. In this pipeline,
LM is usually used as a rescoring process after acoustic
Visual
encoder
Predictive
NeuralNet
Generative
NeuralNet
Linguistic
encoder
Cross-modal
Matching
Lip movement Noisy Clean
Text
TextScore-Based Generative Modeling
Figure 21. Multi-modal knowledge transfer learning for SE.
Acoustic
encoder
AM
(Mapping)
Token sequence
or lattice
LM
Rescoring
Text sequence
Pretrained LM
Figure 22. Conventional pipeline for ASR.
decoding as the first stage. This two-stage processing slows
recognition, and acoustic encoding could not take linguistic
information in feature exploration learning in the first stage.
With rapid advance and development of pretrained LLMs and
end to end ASR models [76], it is necessary to integrate or
transfer knowledge of LLMs into ASR while not increasing
the complexity of decoding either with knowledge distillation
[48] or attention co-training [51], [59], particularly the way
with transferring the linguistic knowledge from LLMs during
acoustic encoding [8], [24], [30], [31], [37], [45]–[47], [69],
[85], [125], [128]. In this way, when performing speech
recognition, we do not need any later usage of language model
since the linguistic knowledge has been distilled to acoustic
encoding. This could be helpful for fast and parallel decoding
in ASR since there is no need for a second-pass rescoring

20
Alignment
Mapping
Acoustic encoder
Tasks in acoustic space
Acoustic modality
Text encoder
Text modality
Tasks in linguistic space
𝜇
𝜈𝛾 ∈ (𝜇,𝜈)
Figure 23. Cross-modal alignment and mapping for knowledge transfer
learning based on OT coupling (acoustic-linguistic modalities).
process.
1) Cross-modal linguistic knowledge transfer for ASR:
During speech communication or perception, usually multi-
modalities are involved in sensing and decision making, for
example, in speech communication, modalities corresponding
to audio, video and text are integrated. For knowledge transfer
learning, multi-modal information could be transferred among
different modalities for improving performance on tasks in
a specific uni-modality. An example of acoustic-linguistic
knowledge transfer learning is shown in Fig. 23. In this figure,
there are two modalities, one is the acoustic modality, the
other is text modality, and they have shared or co-occurred
information since audio speech always has corresponding tran-
scriptions. In this sense, these two modalities can be regarded
as two sides of a coin during speech communication. However,
the distributions of the feature in these two modalities are
different (or heterogeneous). For efficient knowledge transfer
learning, feature alignment and mapping between acoustic and
text modalities are required. If we regard the two modalities
follow two different probability distributionsµandν, the
alignment between the two modalities is naturally recast to
finding OT couplingγ∈Π(µ, ν)as illustrated in Fig. 23.
Based on this idea, an OT-based knowledge transfer framework
(conformer-based acoustic model [42] and pretrained BERT
model [32]) has been proposed as detailed in Fig. 24 [88].
In this framework, two uni-modal encoders, i.e., acoustic and
linguistic encoders, are used for exploring acoustic and linguis-
tic feature representations. Between these encoders, there is
an ‘Adapter’ module for feature transforms during knowledge
transfer learning. In Fig. 24, an ‘OT matching’ module is
designed which serves as the key in cross-modal knowledge
transfer learning. The function of this OT matching module is
to align and match acoustic and linguistic representations for
efficient transfer learning. Further details are provided in the
following sections.
2) Acoustic and linguistic feature representations:As il-
lustrated in Fig. 24, the acoustic and linguistic representations
HA andZ L are extracted by:
HA = EncoderA(X);Z L = EncoderL(y),(87)
CTC loss
FC&Softmax
X
Token sequence
Acoustic modality
Acoustic
Encoder
Textual modality
y
Linguistic
Encoder
OT
Matching Distance
Token sequence
FC𝐴→𝐿
LNFC𝐿→𝐴LN
Adapter
𝜸
y
𝐇𝐴
𝐇𝐴
𝐙𝑳
𝒁𝑳
𝒁𝑳
𝐇𝐴
Figure 24. Cross-modal knowledge transfer for ASR based on OT-matching.
whereXandyare acoustic and linguistic inputs,Encoder A(·)
andEncoder L(·)denote the transforms of the two encoders,
respectively. For paired speech-text sequences, they are rep-
resented asH A = [h 1, . . . ,hla ]∈R la×da andZ L =
[z1, . . . ,zlt ]∈R lt×dt, whered a andd l are dimensions of
acoustic and linguistic features,l a andl t are sequence lengths
of acoustic and linguistic features. In Fig. 24, the dimen-
sion matching transform from acoustic to linguistic spaces
FCA→L(·)is obtained as ¯HA = ¯h1, ...,¯hla  ∈R la×dt with
element estimated from ¯hi = FCA→L (hi).
3) Sinkhorn-based OT for cross-modal alignment:Given
acoustic and linguistic feature sequences ¯HA andZ L (ob-
tained from text encoder if no further process is required),
respectively, as:
¯HA = ¯h1, ¯h2, ...,¯hi, ...,¯hla  ,
ZL = [z1,z 2, ...,zj, ...,zlt ]. (88)
Suppose that the two sequences in Eq. (88) are sampled
from two probability distributions with weight vectorsa=
[a1, a2, ..., ai, ..., ala ]andb= [b 1, b2, ..., bj, ..., blt ]. (if no
prior information is available, seta i = 1/l a andb j = 1/l t
as uniform distributions). The OT distance between the two
sequences is defined as:
LOT
∆
= min
γ∈Q ( ¯HA,ZL) ⟨γ,C⟩,(89)
whereγis a transport coupling set defined as:
Y  ¯HA,Z L  ∆ = n γ∈R la×lt +

γ1lt =a, γT 1la =b o .(90)
In Eq. (90),1 la and1 lt are vectors of ones with dimensions
la andl t, respectively. In Eq. (89),Cis a distance matrix
(or ground cost metric) with elementc i,j defined as pairwise
cosine distance:
ci,j =C
¯hi,z j  ∆ = 1−cos ¯hi,z j  .(91)
A fast estimation of OT has been introduced through the
celebrated EOT [28] (See Section XII-A), where the EOT loss
is defined as:
LEOT
 ¯HA,Z L  ∆ = min
γ∈Q ( ¯HA,ZL) ⟨γ,C⟩ −λ1H(γ),(92)

21
whereλ 1 is a regularization coefficient, andH(γ) =
− P
i,j
γi,j logγ i,j is the entropy of coupling matrix. The so-
lution of Eq. (92) can be implemented with the Sinkhorn
algorithm as [28]:
γλ1 =diag(u)∗K∗diag(v),(93)
whereK= exp

− C λ1

,uandvare two scaling (or re-
normalization) vectors.
4) Temporal order preserved OT:In the original estimation
of OT in Eq. (92), the two sequences in Eq. (88) are treated as
two sets without considering their temporal order relationship.
In speech, temporal order information is crucial in OT cou-
pling during cross-modal alignment, meaning that neighboring
frames in an acoustic sequence should be progressively cou-
pled with neighboring tokens in a linguistic sequence which
has been investigated in [89]. For the sake of clarity, the two
sequences in Eq. (88) can be further represented with temporal
order information as:
¯HA = ¯h1,1  , ¯h2,2  , ..., ¯hi, i  , ..., ¯hla , la  ,
ZL = [(z1,1),(z 2,2), ...,(zj, j), ...,(zlt , lt)]. (94)
During the alignment of the two sequences for knowledge
transfer, it is crucial to consider that elements with significant
cross temporal distances might not be likely to be coupled.
In other words, the coupling pairs with high probabilities
between the two sequences should be distributed along the
diagonal line of the temporal coherence positions. Based
on this consideration, the temporal coupling prior could be
defined as a two dimensional Gaussian distribution [116].
The fundamental concept is that the coupled pairs should
not deviate significantly from the diagonal line of temporal
coherence positions between the two sequences, which can be
defined as:
pi,j
∆
= 1
σ
√
2π exp

− d2 i,j
2σ2
!
,(95)
whereσis a variation variable controlling the impact of the
cross-temporal distanced i,j as defined in Eq. (96).
di,j = |i/la − j/lt|p 1/l2 a + 1/l2 t .(96)
In Eq. (96), the cross-temporal distance is defined on the
normalized sequence lengths in acoustic and linguistic spaces.
In this definition, it is evident that the farther the distance
between a paired position and the temporal diagonal line,
the lower the possibility of their correspondence in transport
coupling. By incorporating this temporal coherence prior as
regularization, the new OT is defined as:
LTOT( ¯HA,Z L) ∆ = min
γ∈Q ( ¯HA,ZL) < γ,C>−λ 1H(γ) +λ 2KL(γ||P),
(97)
whereλ 1 andλ 2 are two trade off parameters. In Eq. (97),
KL(γ||P)is the KL-divergence between the transport coupling
matrixγand the temporal prior correspondence matrixPwith
elements defined in Eq. (95). Building upon the definitions of
KL-divergence and entropy, Eq. (97) can be further expressed
to:
LTOT( ¯HA,Z L) ∆ = min
γ∈Q ( ¯HA,ZL) < γ,˜C>− ˜λH(γ),(98)
where ˜λ=λ 1 +λ 2, and combined ground cost matrix as
˜C=C−λ 2 logP,(99)
where elements inPare defined in Eq. (95). Following the
procedures outlined in [28], the solution of Eq. (98) is obtained
using the Sinkhorn algorithm as:
γ˜λ =diag(u)∗ ˜K∗diag(v),(100)
where ˜K= exp

−
˜C
˜λ

. Substituting variables in Eq. (99) into
˜K, we can obtain the following:
˜K=P
λ2
λ1 +λ2 exp(− C λ1 +λ 2 ).(101)
From this equation, we can see that the transport coupling
between the two sequences is further constrained by their
temporal order correspondence. Temporal order preserved OT
involves several hyper-parameters that can be challenging to
control. For the sake of simplification, their effects can be
consolidated into a reduced number of hyper-parameters. For
example, considering Eq. (99), the impact of variationσin
Eq. (95) andλ 2 in Eq. (97) can be combined into a single
control parameterβ dist, defined as:
˜C=C+β distd2 i,j,(102)
and the Sinkhorn algorithm is applied to this consolidated cost
function ˜Cfor OT in real implementations.
5) Loss function:In the transfer learning model as illus-
trated in Fig. 24, two loss functions are involved: the cross-
modal alignment and matching loss (in the right branch of Fig.
24) and the recognition loss (either CTC-based loss [43], [44]
or CE-based classification loss). For cross-modal alignment,
the acoustic feature is first projected to the linguistic space
using OT transform as:
˜ZL ∆ = OT  ¯HA →Z L  ,
= (γ∗)T × ¯HA ∈R lt×dt , (103)
where(γ ∗)T is the transpose of the OT coupling obtained
from the solution of Sinkhorn-based OT. Subsequently, the
alignment loss is directly defined on the projected space as
Lalign =
ltX
j=1
1−cos

˜ zj L,z j L

,(104)
where˜ zj L andz j L are row vectors of feature matrices ˜ZL
andZ L (according in temporal dimensions), respectively. For
efficient transfer of linguistic knowledge to acoustic encoding,
the following transforms are designed as indicated in Fig. 24:
˜HA =H A + LN(FCL→A(LN( ¯HA)))∈R la×da .(105)
Based on this new representation ˜HA, the probability predic-
tion for ASR is formulated as ˜P= Softmax(FC( ˜HA)), where
‘FC’ is a fully connected linear transform with output size the

22
t
t
(c)
(b)(a)
Acoustic space Linguistic space
𝐡𝑖 𝐡𝑖
𝐡𝑗
𝐳𝑘
𝐳𝑙
𝑑A (𝐡𝑖 ,𝐡𝑗 ) 𝑑L (𝐳𝒌,𝐳 𝑙 )𝐳𝑘
𝐳𝑙
𝐳𝑘
𝐳𝑙
𝐡𝑗
𝐡𝑗
𝐡𝑖
Figure 25. Graph matching OT in Cross-modal knowledge transfer learning
for ASR.
same as that of vocabulary tokens. Finally, the total loss in
model training is defined as
L
∆
= ηLC( ˜P,y) + (1−η)L align,(106)
whereL C( ˜P,y)is a classification loss, either CE or CTC loss
(as shown in Fig. 24). After training the model, only the branch
of the acoustic modality of Fig. (24) is retained for the infer-
ence of ASR. The alignment and matching are performed on
the final representations from encoders of the two modalities
[88], [89], as an extension, the alignment and matching also
has been designed on different layers of acoustic encoders in
order to explore rich acoustic information with consideration
of linguistic knowledge [86]. Moreover, the study in [86] also
indicated the connection between conventional transformer-
based cross-attention and OT where OT-based transport can
be regarded as a double-side (row and column) normalization
process; therefore, the matching and alignment are also named
as Sinkhorn attention [95], [104], [117].
6) Adding structure to OT in Cross-modal linguistic knowl-
edge transfer for ASR:The original concept of OT is defined
on sample points between two sets as illustrated in Fig. 25-(a),
either acoustic or linguistic space,[h 1,h 2, ...,hi, ...,hj, ...]or
[z1,z 2, ...,zl, ...,zk, ...], can be regarded as samples and can
be independently associated or coupled during transportation
between the two spaces, if we add structure (e.g., topological
structure) on points in a space, for example, by defining the
distance metric between two points in each space as illustrated
in Fig. 25-(b),d A (hi,h j)andd L (zl,z k)in acoustic and
linguistic spaces, the association or coupling can be designed
on their distance relationship between two points. Moreover,
as it is known, information in acoustic speech and text are
sequentially encoded, that is the temporal order information
of points should be considered during matching between the
two sets. For example, as shown in Fig. 25-(c), temporal order
information is attached to each node. From these explanations,
we can see that during OT, we could add these kinds of struc-
tured information. This idea has been addressed and named
as graph matching OT in cross-modal knowledge transfer for
ASR in [90].
The behavior of adding different structures in OT for
acoustic and linguistic matching and alignment has been
well analyzed with different hyper-parameters. For example,
𝛼= 1.0
𝛼= 0.1
Figure 26. Segmental structure of speech in matching between acoustic and
linguistic features based on OT.
𝛽dist = 0.5
𝛽dist = 0.1
Figure 27. Temporal order structure of speech in matching between acoustic
and linguistic features based on OT.
as shown in Fig. 26, with adjusting weighting importance
between matching on nodes and edges (the trade-off weighting
coefficientαin Eq. (30) to control the importance between
WD and GWD). In this figure, horizontal and vertical are
indexes of acoustic embedding and its corresponding linguistic
token embedding sequences. With smallα, we can see that
there are many small segments of the matching or coupling,
but whenαincreases, we can see a clear structure of the
matching or coupling segments between the embedding of
acoustic and linguistic feature embeddings. Changing the
coefficientβ dist in Eq. (102), the importance of the temporal
order information can be controlled in alignment and matching
based on OT. The behavior is shown in Fig. 27. we can see
that the alignment between acoustic and linguistic representa-
tions follows a strong monotonic corresponding relationship.
Moreover, in the solution of the OT based on the Sinkhorn
algorithm, the regularization of the OT coupling is adopted.
In the definition Eq. (98), with controlling of the regularization
coefficient ˆλ, the expansion and smooth behavior can be
observed as shown in Fig. 28. With properly setting these
hyper-parameters, state of the art ASR performance could
be obtained which showed the advantages of cross-modal
alignment and matching [88], [89].
7) Unbalanced OT in Cross-modal linguistic knowledge
transfer for ASR:With different setting ofα 1 andα 2 of
UOT in Eq. (32), the alignment behaviors between acoustic
and linguistic features can be well controlled: (a)Acoustic-to-
Linguistic (A2L) alignment: To ensure that every linguistic
token is aligned, we setα 2 > α1. This forces mass coverage
over linguistic units while permitting selective skipping or
discarding of noisy and outlier acoustic frames, including

23
𝜆 = 0.1
𝜆 = 5.0
Figure 28. Entropy regularization of coupling in matching between acoustic
and linguistic features based on OT.
(a)
(b)
(c)
Figure 29. Alignment between acoustic and linguistic tokens (indexes of
acoustic (Horizontal) and linguistic (Vertical) embedding sequences): (a)
cosine similarity matrix; (b)α 1 = 1.0,α 2 = 1.0; (c)α 1 = 0.01,α 2 = 1.0.
NULL acoustic matching; (b)Linguistic-to-Acoustic (L2A)
alignment: To account for as much of the acoustic input
as possible, we setα 1 > α2, ensuring that the acoustic
frames are matched even if some linguistic tokens are less
activated. This matching strategy in model training tries to
encourage bidirectional consistency, and the resulting optimal
transport planγ ∗ represents a soft alignment matrix that
assigns probabilistic mass between acoustic and linguistic
elements, effectively grounding linguistic tokens in observed
speech while avoiding overfitting to background noisy frames
in transfer learning [91]. The effect is shown in Fig. 29.
From this figure, we can see that the alignment between
the acoustic and linguistic embeddings is well controlled by
properly setting the regularization parametersα 1 andα 2 to
meet the requirement of unbalanced matching between them.
G. Cross-domain adaptation in various identification and de-
tection tasks
In various speech tasks, for example LID and SR, the
domain mismatch problem is very common and challenging.
Reducing domain mismatch for improving domain general-
ization performance is necessary where the distance metric
between domain distributions is involved [34]. OT is quite
suitable for these tasks, as OT naturally defines the distance
metric between probability distributions. For the cross-domain
LID task, an OT-based adaptation neural model framework has
been proposed [87]. The model framework is illustrated in
Fig. 30 where both training and test networks share the same
set of weight parameters in a Siamese network architecture.
Dense layer
Dense layer
L-Norm
softmax
Encoder
𝐱𝑡𝐱𝑠
Latent feature
Classifier
Dense layer
Dense layer
L-Norm
softmax
Encoder
𝑝𝑠 (𝐳𝑠 )𝑝 𝑡 (𝐳𝑡 )
𝑝𝑠 (𝐲𝑠 |𝐳𝑠 )𝑝 𝑡 (𝐲𝑡 |𝐳𝑡 ) Class labelsClass labels
(a) (b)
Figure 30. Cross-domain adaptation for LID based on a Siamese neural
network architecture for source (left) and target (right) domain samples.
(a) (b)
Figure 31. Visualization of feature representations via t-SNE in cross-domain
LID before (a) and after (b) adaptation, lang{1,7} tr, lang{1,7} tt denote
language IDs 1 and 7 for training and test.
And the x-vector is adopted as input feature [113] with fixed
pretrained model parameters. The adaptation is designed at
both the feature and the classifier levels to reduce the mismatch
between the distributions of training and testing sets. A similar
idea has been proposed for SR [122], [136]. The effect of
adaptation for LID and SR is shown in Figs. 31 and 32. In
these figures, the t-SNE visualizations [92] of the features
of the language and speaker clusters are plotted. From these
figures, we can see that there exist obvious gaps between the
training/source and test/target domains (two given language
IDs marked lang1 {tr, tt}and lang7 {tr, tt}in Fig. 31-a;
Speaker IDs marked with{Source, Target}speaker{1, 2, 3}in
Fig. 32-a). After adaptation, distributions of features in training
(source) and test (target) domains are pushed to neighboring
regions while keeping their class discrimination structure. OT-
based domain alignment and adaptation have also been applied
in speech emotion recognition tasks [134], [135], where speech
emotion samples come from different languages and recording
environments.
In recent years, due to the requirement of trust-worthy
speech communications, audio spoof detection (ASD) has
been increasing its importance in various applications. ASD,
also known as anti-spoofing refers to techniques designed to
distinguish between bona fide speech (genuine/real human
speech) and artificially generated or manipulated speech. Most

24
(a) (b)
Figure 32. Feature representation in cross-domain speaker recognition before
(a) and after (b) adaptation.
ASD models are designed and trained with a large number of
training data samples. It is difficult to use the same models to
deal with all spoof speech generated with various algorithms
and from versatile domains [74]. Cross-domain ASD and
OT-based adaptation techniques have been developed under
the same line of cross-domain tasks in LID and SVR, and
significant performance gains were obtained [137], [138].
XIV. FUTURE DIRECTIONS
The application of OT to speech processing has shown
promising results across various tasks and applications, either
for multi-modal representation transfer learning, or cross-
modal domain adaptation and integration. However, several
important directions remain open for further exploration.
First, scalability and efficiency remain critical challenges.
Classical OT formulations often incur high computational
cost, especially when applied to long speech sequences or
high-dimensional feature spaces. Developing more efficient
computational algorithms is essential in engineering imple-
mentations, such as stochastic OT, mini-batch OT, and low-
rank or sparsity-constrained transport plans, to enable real-
time and large-scale deployment in speech applications sys-
tems. A particularly promising direction is the integration of
OT with SDE-based generative modeling frameworks. Recent
advances in diffusion models and flow matching methods have
demonstrated strong capabilities in modeling complex data
distributions. OT provides a natural perspective for describing
the evolution of probability distributions over time, which
aligns closely with the dynamics defined by SDEs. Moreover,
with lifting the states of the dynamics in a functional space,
composition operator theory (e.g., Koopman operator) may be
applied to investigate the nonlinear dynamic properties with
linear operator analysis. Future work may explore the theoret-
ical connections between OT and diffusion bridges/processes,
transfer operator learning, as well as their practical implica-
tions for domain or modality alignment and matching.
Multi-modal learning also remains a fertile area for OT-
based methods. Speech is often accompanied by comple-
mentary modalities, such as visual information (e.g., lip
movements), articulatory signals, and textual context. Speech
processing requires methods and algorithms for multimodal
feature learning or multimodal information fusion [126], [140].
OT offers a natural framework for aligning heterogeneous
feature distributions across these modalities. In particular,
domain adaptation and modality gap minimization should
receive increased attention, especially in scenarios involving
mismatched distributions across audio, visual, and textual
streams. Future research may focus on conditional and dy-
namic transport formulations that explicitly reduce cross-
modal discrepancies, handle temporal asynchrony, and im-
prove robustness under missing or noisy modalities. In ad-
dition, theoretical advances are needed to better understand
the role of OT in speech modeling. This includes studying
the properties of transport-based alignments in sequential data,
their relationship to probabilistic formulations such as SDEs
and diffusion models, and their implications for representation
learning and generalization. Such insights could guide the
design of more principled and effective OT-based loss or
objective functions.
In summary, future research on OT for speech lies at the
intersection of efficiency, generative modeling, multi-modality,
and robustness. In particular, a deeper exploration of OT
in conjunction with SDE-based generative frameworks and
transfer operator theory (as well as composition operator
theory), along with a stronger focus on domain adaptation and
modality gap minimization, will be crucial for advancing next-
generation speech technologies.
REFERENCES
[1] Luigi Ambrosio, Nicola Gigli, Giuseppe Savar ´e, Gradient Flows In Metric
Spaces and in the Space of Probability Measures, Springer, 2008.
[2] L. Ambrosio, E. Bru ´e and D. Semola, “Lectures on Optimal Transport,”
Springer, 2021.
[3] B. Amos, L. Xu, and J. Kolter, “Input convex neural networks,” the
Proceedings of the 34th International Conference on Machine Learning,
V ol. 70, pp. 146-155, 2017.
[4] B. Anderson, “Reverse-time diffusion equation models,” Stochastic Pro-
cesses and their Applications, 12(3):313-326, 1982.
[5] Yuki Arase, Han Bao, and Sho Yokoi, “Unbalanced Optimal Transport
for Unbalanced Word Alignment,” In Proceedings of the 61st Annual
Meeting of the Association for Computational Linguistics (V olume 1:
Long Papers), pp. 3966-3986, 2023.
[6] M. Arjovsky, S. Chintala, L. Bottou, “Wasserstein Generative Adversar-
ial Networks,” International Conference on Machine Learning, PMLR:
214–223, 2017.
[7] A. Baevski, Y . Zhou, A. Mohamed, and M. Auli, “Wav2vec 2.0: A
framework for self-supervised learning of speech representations,” in
Proc. of NeurIPS, 2020.
[8] Y . Bai, J. Yi, J. Tao, Z. Tian, Z. Wen and S. Zhang, ”Fast End-to-End
Speech Recognition Via Non-Autoregressive Models and Cross-Modal
Knowledge Transferring From BERT,”IEEE/ACM Transactions on Audio,
Speech, and Language Processing, vol. 29, pp. 1897-1911, 2021.
[9] J. Benamou, Y . Brenier, “A computational fluid mechanics solution to
the Monge-Kantorovich mass transfer problem,” Numerische Mathematik,
vol. 84, pp. 375-393, 2000.
[10] J. Benamou, G. Carlier, M. Cuturi, Marco, L. Nenna, Luca, G. Peyr ´e,
“Iterative Bregman Projections for Regularized Transportation Problems,”
SIAM Journal on Scientific Computing, V ol.37, No.2, pp. A1111-
AA1138, 2015.
[11] R. Bhardwaj,T. Vaidya, S. Poria, “Towards solving NLP tasks with
optimal transport loss,” Journal of King Saud University-Computer and
Information Sciences, V ol. 34, No. 10, pp. 9441-9452, 2022.
[12] M. Blondel, V . Seguy, A. Rolet, “Smooth and Sparse Optimal Transport,”
Proceedings of the Twenty-First International Conference on Artificial
Intelligence and Statistics, pp. 880-889, 2018.
[13] N. Bonneel, J. Digne, “A survey of optimal transport for computer
graphics and computer vision,” Computer Graphics Forum (Eurographics
STAR 2023), V ol. 42, No. 2, pp. 439-460, 2023.
[14] V . De Bortoli, J. Thornton, J. Heng, A. Doucet, “Diffusion schr ¨odinger
bridge with applications to score-based generative modeling,” Interna-
tional Conference on Neural Information Processing Systems, 2021.
[15] Yann Brenier, “Polar Factorization and Monotone Rearrangement of
Vector-Valued Functions,” Communications on Pure and Applied Math-
ematics,vol. 44, pp. 375-417,1991.

25
[16] S. Brunton, M. Budi ˇsi´c, E. Kaiser, J. Kutz, “Modern Koopman Theory
for Dynamical Systems,” SIAM Review, V ol. 64, No. 2, pp. 229-340,
2022.
[17] C. Bunne, “Neural Optimal Transport for Dynamical Systems: Methods
and Applications in Biomedicine,” ETH Zurich thesis, Z ¨urich, Switzer-
land, 2023.
[18] L. Chapel, M. Alaya, G. Gasso, “Partial optimal transport with appli-
cations on positive-unlabeled learning,” Advances in Neural Information
Processing Systems, V ol. 33, pp. 2903-2913, 2020.
[19] Liqun Chen, Yizhe Zhang, Ruiyi Zhang, Chenyang Tao, Zhe Gan,
Haichao Zhang, Bai Li, Dinghan Shen, Changyou Chen, and Lawrence
Carin, “Improving sequence-to-sequence learning via optimal transport,”
arXiv preprint arXiv:1901.06283, 2019.
[20] Y . Chen, T. Georgiou and M. Pavon, “On the Relation Between Optimal
Transport and Schr ¨odinger Bridges: A Stochastic Control Viewpoint,”
Journal of Optimization Theory and Applications, V ol. 169, pp. 671-691,
2014.
[21] R. Chen, Y . Rubanova, J. Bettencourt, D. Duvenaud, “Neural ordinary
differential equations,” arXiv preprint arXiv:1806.07366, 2018.
[22] Y . Chen, T. Georgiou and M. Pavon, “Stochastic Control Liaisons:
Richard Sinkhorn Meets Gaspard Monge on a Schr¨odinger Bridge,” SIAM
Review, V ol. 2, pp. 249-313, 2021.
[23] L. Chizat, G. Peyr ´e, B. Schmitzer, F. Vialard, “Scaling algorithms for
unbalanced transport problems,” arXiv preprin arXiv:1607.05816, 2016.
[24] K. Choi, H. Park, “Distilling a Pretrained Language Model to a Multi-
lingual ASR Model,” inProc. of INTERSPEECH, pp. 2203-2207, 2022.
[25] C. Chuang, A. Torralba, and S. Jegelka,“Estimating generalization
under distribution shifts via domain-invariant representations,” inProc. of
International Conference on Machine Learning (ICML), pp. 1984-1994,
2020.
[26] N. Courty, R. Flamary, D. Tuia and A. Rakotomamonjy, “Optimal
Transport for Domain Adaptation,” In IEEE Transactions on Pattern
Analysis and Machine Intelligence, V ol. 39 (9), pp. 1853–1865, 2014.
[27] N. Courty, R. Flamary, A. Habrard, A. Rakotomamonjy, “Joint distri-
bution optimal transportation for domain adaptation,” Neural Information
Processing Systems, 2017.
[28] Marco Cuturi, “Sinkhorn Distances: Lightspeed Computation of Optimal
Transport,” In Advances in Neural Information Processing Systems, pp.
2292-2300, 2013.
[29] B. Damodaran, B. Kellenberger, R Flamary, D Tuia, N Courty, Deep-
JDOT:Deep Joint Distribution Optimal Transport for Unsupervised Do-
main Adaptation, ECCV , 2018.
[30] K. Deng, S. Cao, Y . Zhang, L. Ma, G. Cheng, J. Xu, P. Zhang,
“Improving CTC-Based Speech Recognition Via Knowledge Transferring
from Pre-Trained Language Models,” inProc. of ICASSP, pp. 8517-8521,
2022.
[31] K. Deng, Z. Yang, S. Watanabe, Y . Higuchi, G. Cheng, P. Zhang,
“Improving Non-Autoregressive End-to-End Speech Recognition with
Pre-Trained Acoustic and Language Models,” inProc. of ICASSP, pp.
8522-8526, 2022.
[32] J. Devlin, M. Chang, K. Lee, and K. Toutanova, “Bert: Pretraining
of deep bidirectional transformers for language understanding,”arXiv
preprint, arXiv:1810.04805, 2018.
[33] K. Do, D. Coeurjolly, P. Memari, N. Bonneel, “Linear-Time Transport
with Rectified Flows,” ACM Transactions on Graphics (TOG), V ol. 44
(4), No. 118, pp. 1-13, 2025.
[34] M. Farr ´us, “V oice Disguise in Automatic Speaker Recognition,” ACM
Computing Surveys (CSUR), V ol. 51 (4), No. 68, pp. 1-22, 2018.
[35] Alessio Figalli, Federico Glaudo, An Invitation to Optimal Transport,
Wasserstein Distances, and Gradient Flows, EMS society, 2023.
[36] R. Flamary, N. Courty, D. Tuia, A. Rakotomamonjy, “Optimal transport
with Laplacian regularization: Applications to domain adaptation and
shape matching,” NIPS Workshop on Optimal Transport and Machine
Learning, 2014.
[37] H. Futami, H. Inaguma, M. Mimura, S. Sakai, T. Kawahara, “Distilling
the Knowledge of BERT for CTC-based ASR,” CoRR abs/2209.02030,
2022.
[38] A. Galichon, Optimal Transport Methods in Economics. Princeton
University Press, 2016.
[39] Y . Ganin, E. Ustinova, H. Ajakan, P. Germain, H. Larochelle, F.
Laviolette, M. Marchand, and V . Lempitsky, “Domain-adversarial training
of neural networks,”Journal of Machine Learning Research, vol. 17, no.
1, pp. 1-35, 2016.
[40] Wilfrid Gangbo, Robert J. McCann, “The geometry of optimal trans-
portation,” Acta Math., 177(2), pp. 113-161, 1996.
[41] I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, D. Warde-Farley, S.
Ozair, A. Courville, Y . Bengio, “Generative Adversarial Nets,” Proceed-
ings of the International Conference on Neural Information Processing
Systems, pp. 2672-2680, 2014.
[42] A. Gulati, J. Qin, C. Chiu, N. Parmar, Y . Zhang, J. Yu, W. Han, S.
Wang, Z. Zhang, Y . Wu, R. Pang, “Conformer: Convolution augmented
transformer for speech recognition,”arXiv preprint, arXiv:2005.08100,
2020.
[43] A. Graves, “Sequence transduction with recurrent neural networks,”
arXiv preprint, arXiv:1211.3711, 2012.
[44] A. Graves, and N. Jaitly, “Towards end to-end speech recognition with
recurrent neural networks,” inProc. ICML, pp. 1764–1772, 2014.
[45] M. Han, F. Chen, J. Shi, S. Xu, B. Xu, “Knowledge Transfer from
Pre-trained Language Models to Cif-based Speech Recognizers via Hier-
archical Distillation,”arXiv preprint, arXiv:2301.13003, 2023.
[46] M. Han, L. Dong, Z. Liang, M. Cai, S. Zhou, Z. Ma, B. Xu, “Improving
End-to-End Contextual Speech Recognition with Fine-Grained Contextual
Knowledge Selection,” inProc. of ICASSP, pp. 8532-8536, 2022.
[47] Y . Higuchi, T. Ogawa, T. Kobayashi, S. Watanabe, “BECTRA:
Transducer-Based End-To-End ASR with Bert-Enhanced Encoder,” in
Proc. of ICASSP, pp. 1-5, 2023.
[48] G. Hinton, O. Vinyals, and J. Dean, “Distilling the knowledge in a neural
network,”arXiv preprint, arXiv:1503.02531, 2015.
[49] J. Ho, A. Jain, and P. Abbeel, “Denoising diffusion probabilistic models,”
Advances in neural information processing systems, V ol 33, pp. 6840-
6851, 2020.
[50] P. Holderrieth, Peter, E. Erives, “An Introduction to Flow Matching and
Diffusion Models,” arXiv: 2506.02070, 2026.
[51] T. Hori, S. Watanabe, and J. R. Hershey, “Joint ctc/attention decoding
for end-to-end speech recognition,” inProc. of ACL, vol. 1, pp. 518–529,
2017.
[52] T. A. Hsieh, C. Yu, S. W. Fu, X. Lu, and Y . Tsao, “Improving Perceptual
Quality by Phone-Fortified Perceptual Loss using Wasserstein Distance
for Speech Enhancement,” ISCA-Interspeech, 2021.
[53] K. Hung, X. Lu, S. Fu, H. Tseng, H. Lin, C. Lin, and Y . Tsao, “Linguistic
knowledge transfer learning for speech enhancement,” arXiv preprint
arXiv:2503.07078, 2025.
[54] A. Hyv ¨arinen, “Estimation of non-normalized statistical models by score
matching,” Journal of Machine Learning Research, V ol.6, pp. 695-709,
2005.
[55] A. Hyv ¨arinen, “Some extensions of score matching.,” Computational
statistics & data analysis, 51(5), pp.2499-2512, 2007.
[56] M. Idel, “A review of matrix scaling and Sinkhorn’s normal form for
matrices and positive maps,” arXiv: Rings and Algebras, 2016.
[57] R. Jordan, D. Kinderlehrer, F. Otto, “The Variational Formulation of the
Fokker-Planck Equation,” SIAM Journal on Mathematical Analysis V ol.
29, Iss. 1, 1998.
[58] A. Khamis, R. Tsuchida, M. Tarek, V . Rolland, L. Petersson, “Scalable
Optimal Transport Methods in Machine Learning: A Contemporary
Survey,” IEEE Transactions on Pattern Analysis and Machine Intelligence,
doi:10.1109/TPAMI.2024.3379571, 2024.
[59] S. Kim, T. Hori, and S. Watanabe, “Joint CTC-attention based end-to-
end speech recognition using multi-task learning,” inProc. of ICASSP,
pp. 4835–4839, 2017.
[60] D. Kingma, M. Welling, “Auto-Encoding Variational Bayes,” arXiv
preprint arXiv:1312.6114, 2013.
[61] D. Kingma,M. Welling, “An Introduction to Variational Autoencoders,”
Foundations and Trends in Machine Learning, V ol. 12, No. 4, pp. 307-
392, 2019.
[62] I. Kobyzev, S. Prince, and M. Brubaker, “Normalizing flows: An intro-
duction and review of current methods,” IEEE Transactions on Pattern
Analysis and Machine Intelligence, 2021.
[63] S. Kolouri, S. Park, M. Thorpe, D. Slep ˇcev, and G. Rohde, “Transport-
based analysis, modeling, and learning from signal and data distributions,”
arXiv preprint arXiv:1609.04767, 2016.
[64] S. Kolouri, S. Park, M. Thorpe, D. Slepcev, G. K. Rohde, “Optimal
Mass Transport: Signal Processing and Machine-learning Applications,”
IEEE Signal Processing Magazine, V ol. 34 (4), pp. 43-59, 2017.
[65] N. Kornilov, P. Mokrov, A. Gasnikov, and A. Korotin, “Optimal Flow
Matching: Learning Straight Trajectories in Just One Step,” The Thirty-
eighth Annual Conference on Neural Information Processing Systems,
2024.
[66] A. Korotin, L. Li, A. Genevay, J. Solomon, A. Filippov, E. Burnaev,
“Do Neural Optimal Transport Solvers Work? A Continuous Wasserstein-
2 Benchmark,” Advances in Neural Information Processing Systems, V ol.
34, pp. 14593-14605, 2021.

26
[67] A. Korotin, V . Egiazarian, A. Asadulaev, R. Safin, Ruslan, E. Burnaev,
“Neural Optimal Transport,” arXiv preprint arXiv:2201.12220, 2022.
[68] W. M. Kouw and M. Loog, “A Review of Domain Adaptation without
Target Labels,”IEEE transactions on pattern analysis and machine
intelligence, 43(3), pp. 766-785, 2019.
[69] Y . Kubo, S. Karita, M. Bacchiani, “Knowledge Transfer from Large-
Scale Pretrained Language Models to End-To-End Speech Recognizers,”
inProc. of ICASSP, pp. 8512-8516, 2022.
[70] M. Kusner, Y . Sun, N. Kolkin, K. Weinberge, “From Word Embeddings
To Document Distances,” Proceedings of the 32nd International Confer-
ence on Machine Learning (ICML), V ol. 37, pp. 957-965, 2015.
[71] A. Lasota, and M. Mackey, Chaos, Fractals and Noise. Stochastic
Aspects of Dynamics, Applied Mathematical Sciences vol. 97, New York
Springer, 1994.
[72] P. Le, H. Gong, C. Wang, J. Pino, B. Lecouteux, D. Schwab, “Pre-
training for Speech Translation: CTC Meets Optimal Transport,”arXiv
preprint, CoRR abs/2301.11716, 2023.
[73] C. L ´eonard, “A survey of the Schr ¨odinger problem and some of its
connections with optimal transport,” Discrete & Continuous Dynamical
Systems-A, V ol. 34, No. 4, pp. 1533-1574, 2014.
[74] M. Li, A. Yasaman, X. Zhang, “A Survey on Speech Deepfake Detec-
tion,” ACM Computing Surveys, V ol. 57 (7), No. 165, pp. 1-38, 2025.
[75] J. Li, L. Deng, R. Haeb-Umbach, Y . Gong, Robust Automatic Speech
Recognition: A Bridge to Practical Applications, Academic Press, 2015.
[76] J. Li, “Recent advances in end-to-end automatic speech recogni-
tion,”APSIPA Transactions on Signal and Information Processing, DOI
10.1561/116.00000050, 2022.
[77] H. Lin, H. Tseng, X. Lu, Y . Tsao, “Unsupervised Noise Adaptive Speech
Enhancement by Discriminator-Constrained Optimal Transport,” inProc.
of NeurIPS, pp. 19935-19946, 2021.
[78] M. Lin, J. Hou, C. Chen, S. Chien, J. Chen, X. Lu, and Y . Tsao,
“Bridging the multi-modality gaps of audio, visual and linguistic for
speech enhancement,” arXiv preprint arXiv:2501.13375, 2025.
[79] Y . Lipman, Y ., R. Chen, H. Ben-Hamu, M. Nickel, and M. Le, “Flow
matching for generative modeling,” arXiv preprint arXiv:2210.02747,
2022.
[80] Y . Lipman, M. Havasi, P. Holderrieth, N. Shaul, M. Le, B. Karrer, R.
Chen, D. Lopez-Paz, H. Ben-Hamu, I. Gat, “Flow Matching Guide and
Code,” arXiv:2412.06264, 2024.
[81] X. Liu, Z. Guo, S. Li, F. Xing, J. You, C. Kuo, G. Fakhri, J. Woo,
“Adversarial Unsupervised Domain Adaptation with Conditional and
Label Shift: Infer, Align and Iterate,” inProc. of IEEE/CVF International
Conference on Computer Vision (ICCV), pp. 10347-10356, 2021.
[82] X. Liu, C. Gong, and Q. Liu, “Flow straight and fast: Learning to
generate and transfer data with rectified flow,” International Conference
on Learning Representations, 2023.
[83] T. Liu, J. Puigcerver, M. Blondel, “Sparsity-constrained optimal trans-
port,” Proceedings of the Eleventh International Conference on Learning
Representations (ICLR), 2023.
[84] M. Long, J. Wang, G. Ding, J. Sun, and P. S. Yu, “Transfer feature learn-
ing with joint distribution adaptation,” inProc. of the IEEE International
Conference on Computer Vision, pp. 2200-2207, 2013.
[85] K. Lu and K. Chen, “A Context-aware Knowledge Transferring Strategy
for CTC-based ASR,” inProc. of SLT, pp. 60-67, 2022.
[86] X. Lu, S. Shen, Y . Tsao, H. Kawai, “Hierarchical Cross-Modality
Knowledge Transfer with Sinkhorn Attention for CTC-based ASR,”
IEEE-ICASSP, 2024.
[87] X. Lu, P. Shen, Y . Tsao, H. Kawai, “Unsupervised Neural Adaptation
Model Based on Optimal Transport for Spoken Language Identification,”
inProc. of ICASSP, pp. 7213-7217, 2021.
[88] X. Lu, S. Shen, Y . Tsao, H. Kawai, “Cross-modal Alignment with
Optimal Transport for CTC-based ASR,” IEEE-ASRU, 2023.
[89] X. Lu, P. Shen, Y . Tsao, H. Kawai, “Temporal Order Preserved Optimal
Transport-based Cross-modal Knowledge Transfer Learning for ASR,”
IEEE-SLT, 2024.
[90] X. Lu, P. Shen, Y . Tsao, H. Kawai, “Cross-modal Knowledge Transfer
Learning as Graph Matching Based on Optimal Transport for ASR,”
ISCA-Interspeech, 2025.
[91] X. Lu, P. Shen, Y . Tsao, H. Kawai, “Learning to Align with Unbalanced
Optimal Transport in Linguistic Knowledge Transfer for ASR,” IEEE-
ICASSP, 2026.
[92] L. Maaten and G. Hinton, “Visualizing data using t-sne,” Journal of
machine learning research, pp. 2579-2605, 2008.
[93] Francesco Maggi, Optimal Mass Transport on Euclidean Spaces, Cam-
bridge University Press, 2023.
[94] A. Makkuva, A. Taghvaei, S. Oh, J. Lee, “Optimal Transport Mapping
via Input Convex Neural Networks,” Proceedings of the 37th International
Conference on Machine Learning, V ol. 119, pp. 6672-6681, 2020.
[95] G. Mialon, D. Chen, A. Aspremont, J. Mairal, “A Trainable Optimal
Transport Embedding for Feature Aggregation and its Relationship to
Attention,” ICLR 2021.
[96] E. Montesuma, F. Mboula and A. Souloumiac, “Recent Advances in
Optimal Transport for Machine Learning,” IEEE Trans. Pattern Anal.
Mach. Intell., vol.47, no. 22, pp. 1161–1180, 2025.
[97] Q. Nguyen, H. Nguyen,Y . Zhou, L. Nguyen, “On unbalanced optimal
transport: gradient methods, sparsity and approximation error,” J. Mach.
Learn. Res., V ol. 24, No.1, 2023.
[98] F. Otto, “The geometry of dissipative evolution equations: the porous
medium equation,” Communications in Partial Differential Equations,
26(1–2), pp. 101–174, 2001.
[99] S. Pan, I. Tsang, J. Kwok and Q. Yang, “Domain Adaptation via Transfer
Component Analysis,” inIEEE Transactions on Neural Networks, vol. 22,
no. 2, pp. 199-210, Feb. 2011.
[100] G. Papamakarios, E. Nalisnick, D. Rezende, S. Mohamed, B. Lakshmi-
narayanan, “Normalizing flows for probabilistic modeling and inference,”
JMLR, V ol. 22, No. 1, pp. 1532-4435, 2021.
[101] G. Peyr ´e and M. Cuturi, “Computational Optimal Transport: With
Applications to Data Science,” Foundations and Trends® in Machine
Learning, V ol. 11 (5-6), pp 355-607, 2019.
[102] G. Peyr ´e, M. Cuturi, J. Solomon, “Gromov-Wasserstein Averaging of
Kernel and Distance Matrices,”Proc. of ICML, vol. 48, pp. 2664-2672,
2016.
[103] G. Peyr ´e, “Optimal Transport for Machine Learners,”
arXiv:2505.06589, 2025.
[104] M. Sander, P. Ablin, M. Blondel, G. Peyre, “Sinkformers: Transformers
with Doubly Stochastic Attention,” inProc. of AISTATS, pp. 3515-3530,
2022.
[105] Filippo Santambrogio, Optimal Transport for Applied Mathematicians:
Calculus of Variations, PDEs and Modeling, Springer, 2015.
[106] S. S ¨arkk¨a, and A. Solin, Applied Stochastic Differential Equations,
Cambridge University Press, IMS Textbooks series, 2019.
[107] M. Scetbon, M. Cuturi, and G. Peyr ´e, “Low-Rank Sinkhorn Factoriza-
tion,” In International Conference on Machine Learning, 2021.
[108] B. Scholkopf, J. Platt, T. Thomas, “A Kernel Method for the Two-
Sample-Problem,” inProc. of the International Conference on Neural
Information Processing Systems (NIPS), vol. 19, pp. 513-520, 2006.
[109] T. S ´ejourn´e, G. Peyr´e, F. Vialard, “Unbalanced Optimal Transport, from
theory to numerics,” in Handbook of Numerical Analysis,V ol. 24, pp.
407-471, 2023.
[110] Y . Shi, V . De Bortoli, A. Campbell, A. Doucet, “Diffusion schr ¨odinger
bridge matching,” International Conference on Neural Information Pro-
cessing Systems, 2023.
[111] J. Shen, Y . Qu, W. Zhang, Y Yu, “Wasserstein Distance Guided
Representation Learning for Domain Adaptation,” AAAI Conference on
Artificial Intelligence, 2017.
[112] R. Sinkhorn and P. Knopp, “Concerning nonnegative matrices and dou-
bly stochastic matrices,” Pacific Journal of Mathematics, 21(2):343–348,
1967.
[113] D. Snyder, D. Garcia-Romero, G. Sell, D. Povey and S. Khudanpur,
“X-Vectors: Robust DNN Embeddings for Speaker Recognition,” IEEE
International Conference on Acoustics, Speech and Signal Processing
(ICASSP), pp. 5329-5333, 2018.
[114] Y . Song, S. Ermon, “Generative Modeling by Estimating Gradients of
the Data Distribution,” CoRR abs/1907.05600, 2019.
[115] Y . Song, J. Sohl-Dickstein, D. Kingma, A. Kumar, S. Ermon, B.
Poole, “Score-Based Generative Modeling through Stochastic Differential
Equations,” ICLR 2021.
[116] B. Su, G. Hua, “Order-Preserving Wasserstein Distance for Sequence
Matching,” Proceedings of the IEEE Conference on Computer Vision and
Pattern Recognition (CVPR), 2017.
[117] Y . Tay, D. Bahri, L. Yang, D. Metzler, D. Juan, “Sparse Sinkhorn
Attention,” inProc. of ICML, pp. 9438-9447, 2020.
[118] A. Tong, K. Fatras, N. Malkin, G. Huguet, Y . Zhang, J. Brooks,
G. Wolf, Y . Bengio, “Improving and generalizing flow-based generative
models with minibatch optimal transport,” Transactions on Machine
Learning Research, pp. 1-34, Mar., 2024.
[119] T. Vayer, L. Chapel, R. Flamary, R. Tavenard, N. Courty, “Fused
Gromov-Wasserstein Distance for Structured Objects,”Algorithms, vol.
13, no. 9, 212, https://doi.org/10.3390/a13090212, 2020.
[120] C ´edric Villani, Topics on optimal transportation, AMS society, 2003.
[121] C ´edric Villani, Optimal Transport: Old and New, Springer, 2008.

27
[122] W. Yang, J. Wei, W. Lu, L. Li, X. Lu, “Domain Adaptation for
Speaker Verification Using Optimal Transport with Pseudo Label,” IEEE
Transactions on Information Forensics & Security, 2026.
[123] Sho Yokoi, Ryo Takahashi, Reina Akama, Jun Suzuki, and Kentaro
Inui, “Word rotator’s distance,” In Proceedings of the 2020 Conference
on Empirical Methods in Natural Language Processing (EMNLP), pp.
2944–2960, 2020.
[124] D. Yu, L. Deng, Automatic Speech Recognition: A Deep Learning
Approach, Springer Publishing Company, 2014.
[125] F. Yu, K. Chen, and K. Lu, “Non-autoregressive ASR Modeling
using Pre-trained Language Models for Chinese Speech Recognition,”
IEEE/ACM Transactions on Audio, Speech, and Language Processing,
vol. 30, pp. 1474-1482, 2022
[126] Y . Yuan, Z. Li, B. Zhao, “A Survey of Multimodal Learning: Methods,
Applications, and Future,” ACM Computing Surveys, V ol. 57 (7), No.
167, pp. 1-34, 2025.
[127] H. Wang, A. Banerjee, Arindam, “Bregman alternating direction
method of multipliers,” Proceedings of the 28th International Conference
on Neural Information Processing Systems, pp. 2816-2824, 2014.
[128] W. Wang, S. Ren, Y . Qian, S. Liu, Y . Shi, Y . Qian, M. Zeng,
“Optimizing Alignment of Speech and Language Latent Spaces for End-
To-End Speech Recognition and Understanding,” inProc. of ICASSP, pp.
7802-7806, 2021.
[129] M. O. Williams, I.G. Kevrekidis, C.W. Rowley, “A Data–Driven
Approximation of the Koopman Operator: Extending Dynamic Mode
Decomposition, ” Journal of Nonlinear Science 25, pp. 1307-1346, 2015.
[130] Jiankai Xing, Fujun Luan, Ling-Qi Yan, Xuejun Hu, Houde Qian, and
Kun Xu. Differentiable rendering using rgbxy derivatives and optimal
transport. ACM Transactions on Graphics (TOG), 41(6):1–13, 2022.
[131] Yujia Xie, Xiangfeng Wang, Ruijia Wang, and Hongyuan Zha, “A
fast proximal point method for computing exact wasserstein distance”
In Uncertainty in artificial intelligence, pp. 433–453, PMLR, 2020.
[132] Chi Zhang, Yujun Cai, Guosheng Lin, and Chunhua Shen, “Deepemd:
Few-shot image classification with differentiable earth mover’s distance
and structured classifiers,” In Proceedings of the IEEE/CVF Conference
on Computer Vision and Pattern Recognition (CVPR), June 2020.
[133] R. Zhang, J. Wei, X. Lu, W. Lu, D. Jin, L. Zhang, J. Xu, “Optimal
Transport with a Diversified Memory Bank for Cross-Domain Speaker
Verification,” IEEE-ICASSP, 2023.
[134] R. Zhang, J. Wei, X. Lu, Y . Li, J. Xu, D. Jin, J. Tao, “SOT:
Self-supervised Learning-Assisted Optimal Transport for Unsupervised
Adaptive Speech Emotion Recognition,” ISCA-Interspeech, 2023.
[135] R. Zhang, J. Wei, X. Lu, Y . Li, W. Lu, D. Jin, J. Xu, “Self-supervised
Domain Exploration with an Optimal Transport Regularization for Open
Set Cross-domain Speech Emotion Recognition,” IEEE-ICASSP, 2024.
[136] R. Zhang, J. Wei, X. Lu, W. Lu, D. Jin, L. Zhang, J. Xu., “Unsuper-
vised Adaptive Speaker Recognition by Coupling-Regularized Optimal
Transport,” IEEE-TASLP, 2024
[137] R. Zhang, J. Wei, X. Lu, L. Zhang, D. Jin, J. Xu, W. Lu, “SHDA:
Sinkhorn Domain Attention for Cross-Domain Audio Anti-Spoofing,”
IEEE Transactions on Information Forensics & Security, 2025.
[138] R. Zhang, J. Wei, X. Lu, L. Zhang, D. Jin, W. Lu, J. Xu, “Multi-
Sinkhorn Teacher Knowledge Aggregation Framework for Adaptive Au-
dio Anti-Spoofing,” IEEE Transactions on Audio, Speech, and Language
Processing, 2025.
[139] Z. Zhang, J. Geiger, J. Pohjalainen, A. Mousa, W. Jin, B. Schuller,
“Deep Learning for Environmentally Robust Speech Recognition: An
Overview of Recent Developments,” ACM Transactions on Intelligent
Systems and Technology (TIST), V ol. 9, no. 5, pp. 1-28, 2018.
[140] F. Zhao, C. Zhang, B. Geng, “Deep Multimodal Data Fusion,” ACM
Computing Surveys, V ol. 56 (9), No. 216, pp. 1-36, 2024.
[141] Y . Zhou, Q. Fang, Y . Feng, “CMOT: Cross-modal Mixup via Optimal
Transport for Speech Translation,”arXiv preprint, arXiv:2305.14635,
2023.
