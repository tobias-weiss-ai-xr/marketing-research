---
title: A Coupled Friedkin-Johnsen Model of Popularity Dynamics in Social Media
url: https://arxiv.org/abs/2503.15170
category: social-media
subcategory: empirical
date: 2025-03
venue: ''
authors:
- Gaya Cocca
- Paolo Frasca
- Chiara Ravazzi
source: arxiv
pdf_url: https://arxiv.org/pdf/2503.15170
pages: 15
chars: 31292
fetched_at: '2026-11-08T13:02:38+00:00'
kb_version: 1
---

# A Coupled Friedkin-Johnsen Model of Popularity Dynamics in Social Media

arXiv:2503.15170v2  [cs.SI]  30 Jun 2025
A Coupled Friedkin-Johnsen Model
of Popularity Dynamics in Social Media
Gaya Cocca ∗, Paolo Frasca †, Chiara Ravazzi ‡§
July 1, 2025
Abstract
Popularity dynamics in social media depend on a complex interplay of
socialinfluencebetweenusersandpopularity-basedrecommendationsthat
are provided by the platforms. In this work, we introduce a discrete-time
dynamical system to model the evolution of popularity on social media.
Our model generalizes the well-known Friedkin-Johnsen model to a set
of influencers vying for popularity. We study the asymptotic behavior of
this model and illustrate it with numerical examples. Our results highlight
the interplay of social influence, past popularity, and content quality in
determining the popularity of influencers.
1 Introduction
Social media play a prominent role in contemporary societies. Therefore, it is
important to understand how the popularity of contents, topics, and influencers
evolves therein. Over the years, various kinds of models from different scientific
fields have been proposed to describe the dynamics of popularity. These models
include epidemic models [1], self-exciting processes [2], and Bass-like diffusion
models [3]. Although building upon different basic principles, most of them
emphasize that popularity is shaped by social influence between users and by
the recommendation systems deployed by the platforms [4]. Significant schol-
arly work, including mathematical models, has been produced on these topics.
Within the large literature about social influence, which in part predates the
∗G. Cocca was a master’s student of Politecnico di Torino, Corso Duca Degli Abruzzi 24,
10129, Torino, Italy. E-mail: s316763@studenti.polito.it.
†P. Frasca is with Univ. Grenoble Alpes, CNRS, Inria, Grenoble INP, GIPSA-lab, F-38000
Grenoble, France. E-mail: paolo.frasca@gipsa-lab.fr.
‡C. Ravazzi is with the National Research Council of Italy (CNR-IEIIT), c/o Politecnico
di Torino, Corso Duca Degli Abruzzi 24, 10129, Torino, Italy. E-mail: chiara.ravazzi@cnr.it.
§This work has been supported by ANR grant FeedingBias (ANR-22-CE38-0017-01) and
by the European Union – Next Generation EU, Mission 4, Component 1, under the PRIN
project TECHIE: “A control and network-based approach for fostering the adoption of new
technologies in the ecological transition” Cod. 2022KPHA24 CUP Master: D53D23001320006,
CUP: B53D23002760006.

rise of social media, we single out the celebrated Friedkin-Johnsen model [5] and
its variations, including those that account for multiple coupled dynamics [6].
Regarding the recommendation systems, even though their specifics are not dis-
closed by the platforms, they are known to leverage past popularity and user
preferences with the goal of increasing user engagement [7–9]. The objective of
the paper is to propose and study a conceptual model, based on “first princi-
ples”, which has the goal of exploring how the interplay of social influence and
recommendations can play out during the processes of content consumption in
social media. Our contribution lies in the formulation and analysis of an original
model for the evolution of popularity on social media. Our model describes the
popularity of influencers as the aggregate of the attention that their contents
receive from a population of users. The attention of each user towards each in-
fluencer evolves through a nonlinear dynamics that takes into account three key
ingredients: (i) the social influence due to interactions between users; (ii) the
competition among influencers, mediated by the popularity-based recommen-
dations by the platform; and (iii) the intrinsic quality of the contents produced
by each influencer. The model is akin to a set of coupled Friedkin-Johnsen
dynamics: each of them describes the attention that the users give to one influ-
encer, while the nonlinear coupling accounts for the aggregate popularity of the
influencers.
Our model is able to capture two distinct scenarios. When content quality is
irrelevant, the attention levels that are given to influencers converge to consen-
sus, that is, tend to become uniform across users: popularity is only driven by
social contagion effects and by the recommendations that amplify the popular-
ity of already popular content. Instead, when quality is relevant, user attention
converges toward a more heterogeneous limit profile, and quality determines
popularity. This dichotomy highlights how sensitivity to quality can serve as a
key factor in shaping the collective dynamics of popularity on social media.
This paper is organized as follows. Section 2 describes the mathematical
model and Section 3 studies its steady-state behavior. We first concentrate
on the degenerate cases when there is no network effect or no quality effect,
then consider the generic case with all effects. Section 4 discusses the results,
their relations and limitations, and their potential implications for the study of
popularity of social media. Section 5 provides some conclusions and directions
for future work.
2 The model
We consider a setV of n users of a social media platform: each of them can
access contents from a setI of influencers at each instant of timet ∈ N ∪ {0}.
Each user v ∈ Vis endowed with a scalar valuex(i) v (t) ∈ [0, 1], which quantifies
their attention to contents posted by influenceri ∈ Iat time t. Our objective
is to develop a model to describe the evolution of this attention over time,
capturing the interplay of the following factors:

• the social influence between users, interconnected by a social network;
• the effect of recommendations proposed by the platform according to the
influencers’ previous popularity;
• the intrinsic quality of the contents produced by the influencers.
Modeling network effects: By network effects, we mean the phenomenon
whereby a user’s attention towards an influencer is directly or indirectly influ-
enced by the attention given by other users. The ability of users to interact and
influenceeachothercanbeformalizedusingagraph G = (V, E), whereE ⊆ V ×V
describes the potential interactions. We will use aweighted-adjacency matrix
P, associated withG, in order to encode the intensity of these interactions. The
matrix P is row stochastic, i.e., has nonnegative entries andP 1n = 1n (where
1n denotes a vector withn entries, all equal to1). A node v ∈ Vin a directed
graph is said to beaperiodic if the greatest common divisor of the lengths of all
cycles starting and ending atv is equal to 1.
Modeling recommendations:We assume that the effect of recommendations
depends on a normalized popularity indexπ(i)(t), which is an aggregate measure
of the attention given to previous influencer content. We thus choose to define
the popularity index of each influenceri ∈ Ias
π(i)(t) = X
v∈V
x(i) v (t)
X
j∈I
X
w∈V
x(j) w (t).
Using such a normalized measure of popularity accounts for constraints on the
global potential audience, which are referred to as “finite carrying capacity” of
the medium in classical works about public arenas [10] and have been success-
fully included in recent mathematical models of social media [8].
Modeling content quality:We also suppose that intrinsic factors, such as the
quality of the contents proposed by the influencers, act as persistent input in the
attention dynamics: the quality affects users by the exposure to the contents.
The quality of contents posted by influenceri will be denoted byq(i) ∈ [0, 1],
with the intuition that higher quality contents should receive more attention.
The contributions of interactions, popularity, and quality are weighted by
nonnegative coefficientsαv, βv and γv, such thatαv +βv +γv = 1. Therefore, we
assume that the dynamic of the attentionx(i) v (t) evolves for allv ∈ Vaccording
to:
x(i) v (t + 1) = αv X
w∈V
Pvwx(i) w (t) + βvπ(i)(t) + γvq(i), (1)
which can be rewritten in vector form as
x(i)(t + 1) = AP x(i)(t) + Bπ (i)(t) + Γq(i),
where A = diag(α), B = diag(β), and Γ = diag(γ).

3 Qualitative and numerical analysis
In this section, we study the asymptotic behavior of the dynamics. We will
proceed by first considering, in Section 3.1, the case ofαv = 0 for all v ∈ V,
that is, when there is no social influence. Next, Section 3.2 is devoted to the
case with γv = 0 for all v ∈ V, that is, when quality plays no role and only
network effects and recommendations influence the dynamics. Notice that in
the case βv = 0 for all v ∈ V, that is, when only the network effect and the
quality play a role in the dynamics, the system reduces to a set ofn decoupled
Friedkin-Johnsenmodels [5]. Finally, in Section 3.3, we will study what happens
in the general case when all terms give contribution to the dynamics.
3.1 Asymptotic Behavior Without Network Effects
In the dynamics described by equation (1), each future attention value is influ-
enced by user interactions in the network described by the weighted-adjacency
matrix P. Assuming αv = 0 ∀v ∈ Veliminates the contribution of interactions,
retaining only the influence from past popularity values and other factors. By
taking into account that in this caseγv = 1 − βv, we can rewrite (1) as follows:
x(i) v (t + 1) = βvπ(i)(t) + (1 − βv)q(i). (2)
The following result guarantees that for any initial condition the dynamics
in (2) converges asymptotically to a limit point.
Theorem 1 (Convergence – No network). Let αv = 0 for all v ∈ Vand denote
qtot = P i∈I q(i). If ∃ v ∈ Vs.t. βv ̸= 1 and ∃i ∈ Is.t. q(i) > 0, then, for any
initial condition π(0) = π0, the dynamics(2) is such that∀i ∈ I, ∀v ∈ V,
lim
t→∞
π(i)(t) = q(i)
qtot
, lim
t→∞
x(i) v (t) = βv q(i) qtot + (1 − βv)q(i).
Proof. By denoting β = 1 n P v∈V βv and x(i)(t) = 1 n P v∈V x(i) v (t), from (2), we
obtain
x(i) v (t + 1) = βv x(i)(t)P
j∈I x(j)(t) + (1 − βv)q(i),
from which P i∈I x(i)(t + 1) = β + (1 − β)qtot and
π(i)(t + 1) = β β + (1 − β)qtot π(i)(t) + (1 − β) β + (1 − β)qtot q(i).
Since qtot > 0 and β <1, this scalar dynamics is asymptotically stable and the
statement follows immediately.
We observe that, in this case, the steady state is fully determined by the
intrinsic quality of the influencers. Numerical simulations confirm the result,

0 5 10 15
Iterations
0.2
0.25
0.3
0.35
0.4
0.45
0.5
Popularity
Influencer 1
Influencer 2
Influencer 3
0 5 10 15
Iterations
0
0.2
0.4
0.6
0.8
1
Attention
Influencer 1
Influencer 2
Influencer 3
Figure 1: Evolution of dynamics (2): Popularity π(i)(t) (left) and attention
x(i) v (t) (right).
showing convergence for any initial condition. In Figure 1, we present a sim-
ple example. We consider three influencers and 20 users and we set q(i) =
(0.3, 0.7, 0.5) and the parameters βv sampled from a uniform distribution over
[0, 1]. The initial conditionsx(i) v (0) are also sampled from uniform distributions
on [0, 1].
3.2 Asymptotic behavior without quality effects
We now consider the case in which the quality gives no contribution, i.e. when
γv = 0 ∀v ∈ V. Since βv = 1 − αv, the dynamics in (1) becomes
x(i)(t + 1) = AP x(i)(t) + (I − A)π(i)(t), (3)
where A = diag( α). Let us define z(t) = P i∈I x(i)(t) and use it to rewrite
π(i)(t) in terms ofz(t) as
π(i)(t) =
P
v∈V x(i) v (t) P
w∈V
P
j∈I x(j) w (t) = 1⊤ n x(i)(t) 1⊤n z(t) . (4)
Proposition 1. Let γv = 0 for all v ∈ Vand assume that, in the graph asso-
ciated to P, there exists for allv ∈ Va path fromv to w with αw < 1. Then,
z(t) converges to z⋆ = 1n.
Proof. From equation (3), recalling thatP i∈I π(i)(t) = 1 for all t we obtain,
z(t + 1) = AP z(t) + (I − A)1n. This is a specific instance of a Friedkin-Johnsen
model [5], in which the constant input is 1n. Then, the reachability of the
deficient nodev implies, by [11, Lemma 5], thatAP is Schur stable and therefore
z⋆ = (I − AP )−1(I − A)1n = 1n, where the last equality follows immediately
from P 1n = 1n.

It is convenient to treat the evolution ofx(i)(t) and of π(i)(t) jointly. By
defining s(i)(t) := (x(i)(t)⊤, π(i)(t))⊤, the joint model becomes
s(i)(t + 1) = U (t)s(i)(t), (5)
with
U (t) =
"
AP (I − A)1n
1T n AP
1⊤n z(t)
1⊤ n (I−A)1n
1⊤n z(t)
#
. (6)
Notice that1⊤ n z(t) converges ton by Proposition 1 and thereforeU (t) converges
to the row stochastic matrix
eU =
"
AP (I − A)1n
1⊤ n AP
n
1⊤ n (I−A)1n
n
#
. (7)
We therefore have the following result, whose proof is postponed to Appendix
A.
Theorem 2 (Convergence – No quality). Let γv = 0 for all v ∈ Vand z(0) ≥ 1.
Assume that in the graph associated toP, for allv ∈ V, there exists a path from
v to an aperiodic node w with αw < 1. Then, for all i ∈ Ithe dynamics
(5) converges to s(i)⋆ = ϕ⊤s(i)(0) 1n+1 as t → ∞for some vector ϕ ∈ Rn+1.
Moreover, let λ1 = ρ(AP ) and let ˜ϕ be the stationary distribution of eU, then
there exists a constantχ >0
∥ϕ − ˜ϕ∥1 ≤ χ∥z(0) − 1∥1 λ1pn(λ1) (1 − λ1)n+1 .
where pn(λ1) is a polynomial of degreen and pn(0) = 1.
It can be seen that in this case, the dynamics for each influenceri converges
to a consensus, since the role of each user is the same: in other words, all users
converge to the same value of attention for thei-th influencer, which is equal to
its popularity. Althoughϕ is the same for alli, the consensus value is different
depending on the influenceri, since it depends on the initial conditions(i)(0).
Moreover, for fixedn, when the influence of the matrixAP is weak, λ1 will be
small and ϕ will approach the reference stationary distribution˜ϕ. On the other
hand, when λ1 approaches 1, the bound will be less informative, but we expect
that ϕ will be close to the invariant measure ofP.
Figure 2 shows an example. The network is modeled as an Erdős-Rényi
random graph withn = 20 nodes and edge probabilityp = 0.2. The parameters
βv and initial conditionsx(i) v (0)are sampled from a uniform distribution in[0, 1].
It can be observed that, for any influenceri, the attention values by all users
x(i) v (t) go to a consensus, as deduced in theory. The consensus value is the limit
popularity ofi, limt→∞ π(i)(t). Simulations also confirm thatϕ is close to˜ϕ: the
dashed lines in the left plot of Figure 2 show the consensus values that would
be produced by using˜ϕ instead of ϕ.

0 5 10 15
Iterations
0.3
0.31
0.32
0.33
0.34
0.35
0.36Popularity
Influencer 1
Influencer 2
Influencer 3
0 5 10 15
Iterations
0
0.2
0.4
0.6
0.8
1
Attention
Influencer 1
Influencer 2
Influencer 3
Figure 2: Evolution of dynamics (3): Popularity π(i)(t) (left) and attention
x(i) v (t) (right).
3.3 Asymptotic behavior with all effects
It remains to understand how the general dynamics, in which all terms ap-
pear, behave. We defines(i)(t) := ( x(i)(t)⊤, π(i)(t))⊤, and express the coupled
dynamics
s(i)(t + 1) = U (t)s(i)(t) + q(i)c(t) (8)
where
U (t) =
"
AP B 1n
1⊤ n AP
1⊤n z(t)
1⊤ n B1n
1⊤n z(t)
#
, c (t) =
"
(I − A − B)1n
1⊤ n (I−A−B)1n
1⊤n z(t)
#
. (9)
Notice that also in this case we have the convergence ofz.
Proposition 2. Assume that for allv ∈ Vthere exists a path fromv to w such
that γw > 0 in the graph associated toP. Then z(t) converges and
z⋆ := lim
t→∞
z(t) = (I − AP )−1(B + qtot(I − A − B))1n.
Proof. Notice that in this case
z(t + 1) = AP z(t) + B1n + qtot(I − A − B)1n.
As in the proof of Proposition 1, the connectivity assumption guarantees that
AP is Schur stable by Lemma 5 in [11].
Thefollowingtheoremguaranteesasymptoticconvergenceof s: itssomewhat
lengthier proof is given in Appendix B.
Theorem 3 (Convergence–Genericcase) . Assume that, in the graph associated
to P, for all v ∈ Vthere exists a path fromv to an aperiodic nodew such that
γw > 0. If qtot ≥ 1 and z(0) ≥ 1n, then the dynamics (8) is convergent for
t → ∞and for all i ∈ I, limt→∞ s(i)(t) = q(i) (I − eU )−1ec, with
eU =
" AP B 1n
1⊤ n AP
1⊤n z⋆
1⊤ n B1n
1⊤n z⋆
#
, ec =
"(I − A − B)1n
1⊤ n (I−A−B)1n
1⊤n z⋆
#
. (10)

0 5 10 15
Iterations
0.2
0.25
0.3
0.35
0.4
0.45Popularity
Influencer 1
Influencer 2
Influencer 3
0 5 10 15
Iterations
0
0.1
0.2
0.3
0.4
0.5
0.6
0.7Attention
Influencer 1
Influencer 2
Influencer 3
Figure 3: Evolution of popularity π(i)(t) (left) and attention x(i) v (t) (right) in
the general case (8), when αv ̸= 0 , βv ̸= 0 , γv ̸= 0 for all v. Notice that
condition zv(0) ≥ 1 in Theorem 3 is not satisfied in this example.
This convergence result requires thatqtot ≥ 1 and zv(0) ≥ 1 for all v ∈ V
(The latter condition also appears in Theorem 2). We argue that these condi-
tions are mild and, in fact, not necessary for convergence. Indeed, they require
both the total quality of the influencers and each user’s total attention for the
influencers to be at least 1. This assumption is not restrictive as long as the
number of competing influencers is not too small. Furthermore, simulations
show that the dynamics converge also when these conditions are not met. An
example is provided in Figure 3, where the network is the same as in Figure 2.
The parameters αv, βv, γv and x(i) v (0) are sampled from a uniform distribution
in [0, 1], then normalized to satisfyαv + βv + γv = 1 for all v ∈ V.
4 Discussion
The study of the model shows that, under mild connectivity conditions, the
dynamics converge to equilibria, which we are able to characterize explicitly.
The characterizations of the equilibria allow us to deduce important in-
sights on the relationship between social influence, recommendations, and con-
tent quality. Let us discuss the various cases of interest.
When the network has no role (α = 0 ) as in Theorem 1, popularity is
determined solely by quality. Therefore, it appears that the network is essential
for recommendations to have an effect. When recommendations (and thus past
popularity) have no role (β = 0), the system reduces to|I| decoupled Friedkin-
Johnsen’s models with constant input q(i)1n, whose equilibria read x(i)∗ =
(I − AP )−1(I − A)q(i)1n = q(i)1n and are globally asymptotically stable, as
long as the social network contains a globally reachable node. In this case,
the popularity of the influencers is trivially determined by their quality, thus
making the network irrelevant. These two cases, taken together, indicate that
recommendations enhance and enable the effects of the network. If quality has

no role (γ = 0) as in Theorem 2, popularity is solely determined by the structure
of the user network and by the initial condition: influencers who initially receive
attention by prominent users will continue to be successful. In this scenario, the
success of influencers is uniform across users (all users share the same taste) and
if the alpha parameter is small, then influence becomes evenly distributed, thus
fixing initial success. On the contrary, in the generic case with all effects, as
in Theorem 3, quality plays a fundamental role. The steady-state vector of the
attention received by an influencer is the product of its quality and an influence
profile vector. Each user heeds influencers differently, but the influence profile
is the same for every influencer and depends on the parametersγv’s and on the
network structure, with no role for the initial condition.
In conclusion, our analysis offers insights into the potential relationships
between quality, network effects, and popularity. One key insight is that the
network has a significant impact despite quality being a property of the influ-
encer only, independent from the users. Indeed, the discussion on the cases with
α = 0 and β = 0 shows that popularity-based recommendations enhance the
role of the social network. Another key insight is that the dynamics displays
rather different regimes, depending on whether users are sensitive to quality. If
γ is positive, quality plays a dominant role. Ifγ is zero and the initial conditions
are random, their randomness plays a dominant role, making popularity more
unpredictable. This diversity of regimes may be useful to explain variations
across different platforms, which can display forms of virality that are more or
less predictable and more or less directly explainable by content features.
5 Conclusion
In this paper, we have formulated a nonlinear model that aims to explain how
users’ attention to influencers, and thus the popularity of the latter, evolves.
Our original model, which generalizes the well-known linear model by Friedkin
and Johnsen [5], includes three key factors: social influence through user inter-
actions, popularity-based recommendations by the platform, and the influencer
quality. As we have discussed in the previous section, the regimes captured
by our model (see Sections III.B and III.C) are consistent with qualitative ob-
servations reported in recent studies: users of platforms such as TikTok can
show a lower sensitivity to content quality and reward influencers regardless
of their experience [12], while for example on YouTube, a smaller number of
creators tend to dominate attention thanks to the production of high-quality
content [13]. Future research should seek more explicit empirical confirmations
of these insights.
Further work would also be beneficial to overcome some limitations of our
analysis (essentially, the assumption on zv(0) in Theorems 2 and 3 and the
connectivity assumptions on the social influence network) and to extend the
model to allow for distinct personal preferences of individualsq(i) v .

References
[1] C. Richier, E. Altman, R. Elazouzi, T. Jimenez, G. Linares, and Y. Por-
tilla, “Bio-inspired models for characterizing YouTube view count,” in
2014 IEEE/ACM International Conference on Advances in Social Networks
Analysis and Mining (ASONAM 2014), 2014, pp. 297–305.
[2] R. Crane and D. Sornette, “Robust dynamic classes revealed by measur-
ing the response function of a social system,”Proceedings of the National
Academy of Sciences, vol. 105, no. 41, p. 15649–15653, 2008.
[3] X. Gao, Z. Zheng, Q. Chu, S. Tang, G. Chen, and Q. Deng, “Popular-
ity prediction for single tweet based on heterogeneous Bass model,”IEEE
Transactions on Knowledge and Data Engineering, vol. 33, no. 5, pp. 2165–
2178, 2019.
[4] M. Bressan, S. Leucci, A. Panconesi, P. Raghavan, and E. Terolli, “The
limits of popularity-based recommendations, and the role of social ties,”
in Proceedings of the 22nd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining, 2016, pp. 745–754.
[5] N.FriedkinandE.Johnsen, “Socialinfluencenetworksandopinionchange,”
Advances in Group Processes, vol. 16, 1999.
[6] N. E. Friedkin, A. V. Proskurnikov, R. Tempo, and S. E. Parsegov, “Net-
work science on belief system dynamics under logic constraints,”Science,
vol. 354, no. 6310, pp. 321–326, 2016.
[7] P. Covington, J. Adams, and E. Sargin, “Deep neural networks for YouTube
recommendations,” Proceedings of the 10th ACM Conference on Recom-
mender Systems, pp. 191–198, 2016.
[8] M. Castaldo, T. Venturini, P. Frasca, and F. Gargiulo, “Junk news bubbles
modelling the rise and fall of attention in online arenas,”New Media &
Society, p. 1461444820978640, 2021.
[9] M. Castaldo, P. Frasca, and T. Venturini, “Online attention dynamics in
social media,” Cyber–Physical–Human Systems: Fundamentals and Appli-
cations, pp. 491–510, 2023.
[10] S. Hilgartner and C. L. Bosk, “The rise and fall of social problems: A
public arenas model,” American journal of Sociology, vol. 94, no. 1, pp.
53–78, 1988.
[11] P. Frasca, C. Ravazzi, R. Tempo, and H. Ishii, “Gossips and prejudices:
Ergodic randomized dynamics in social networks,”IFAC Proceedings Vol-
umes, vol. 46, no. 27, pp. 212–219, 2013.

[12] C. Ling, J. Blackburn, E. De Cristofaro, and G. Stringhini, “Slapping cats,
bopping heads, and Oreo shakes: Understanding indicators of virality in
TikTok short videos,” inProceedings of the 14th ACM Web Science Con-
ference 2022, 2022, p. 164–173.
[13] M. L. Cheung, W. K. Leung, E. C.-X. Aw, and K. Y. Koay, ““I follow
what you post!”: the role of social media influencers’ content characteris-
tics in consumers’ online brand-related activities,”Journal of Retailing and
Consumer Services, vol. 66, p. 102940, 2022.
[14] G. Stewart, “On the powers of a matrix with perturbations,”Numerische
Mathematik, vol. 96, 2003.
A Proof of Theorem 2
Lemma 1. Let M ∈ Cn×n be a matrix with spectral radiusρ ∈ (0, 1). Then
∥M k∥∞ ≤ C kn ρk for all k ∈ N, where χ >0 is a constant (independent ofk
and ρ).
Proof. Let q be the number of distinct eigenvalues of the matrixM ∈ Cn×n,
denoted by {λℓ}q ℓ=1, and consider its Jordan canonical decomposition: M =
U J U−1. Then, ∥M k∥∞ ≤ ∥U ∥∞∥J k∥∞∥U −1∥∞. The k-th power of a Jordan
block of sizes associated with eigenvalueλ has entries bounded by
 k
m

|λ|k−m,
for m = 0 , . . . , s− 1. Hence, ∥J k∥∞ ≤ maxℓ |λℓ|k Psℓ−1 m=0  k m  |λℓ|−m, where sℓ
is the size of the largest Jordan block associated withλℓ. Using the bound k
m

≤ km, we get for some constant χ > 0, independent of k, ∥J k∥∞ ≤
maxℓ |λℓ|kksℓ−1 Psℓ−1 m=0 |λℓ|−m ≤ χρkkn, Therefore, there exists a constantC =
∥U ∥∞∥U −1∥∞χ, independent ofk, such that∥M k∥∞ ≤ Cρ kkn.
Lemma 2. Let λ ∈ (0, 1) and n ∈ N. Then P∞ k=0 knλk = λpn−1(λ) (1−λ)n+1 , where
pn−1(λ) is a polynomial of degreen − 1 satisfying pn−1(0) = 1.
Proof. Proceed by induction onn ∈ N. For n = 1
∞X
k=0
kλk = λ
∞X
k=0
kλk−1 = λ d dλ ( 1 1 − λ ) = λ (1 − λ)2 ,
which is in the desired form withp0(λ) = 1 . Assume by induction that the
formula holds forn − 1,
∞X
k=0
knλk = λ d dλ
 ∞X
k=0
kn−1λk
!
= λ d dλ  λpn−2(λ) (1 − λ)n  .
By differentiating we obtain
d
dλ
 λpn−2(λ)
(1 − λ)n

= (pn−2(λ) + λp′ n−2(λ))(1 − λ) + nλpn−2(λ) (1 − λ)n+1 .
where the numerator is a polynomial of degree at mostn − 1, say pn−1, with
the property pn−1(0) = pn−2(0) = 1. Multiplying by λ, we get the result.

Lemma 3. If z(0) ≥ 1, then ∥U (t)∥∞ = 1, ∀t ∈ N.
Proof. Since P is row-stochastic and z(0) ≥ 1, one can show by induction on
t ∈ N that z(t) ≥ 1 for all t ∈ N. This implies that the sum of last row is not
larger than 1. Moreover, the sum of the entries in each of the remaining rows
is exactly 1. Therefore∥U (t)∥∞ = 1 for all t ∈ N.
We will use of the following known result, which holds for any submultiplica-
tive matrix norm.
Lemma 4 (Theorem 4.1 in [14]). Let the square matrixQ have a simple domi-
nant eigenvalue λ1(Q) = 1 with multiplicity 1 and let ex be the right eigenvector
associated to this eigenvalue. Let∆Q(k), for k ∈ N, be a sequence of matrices
of suitable dimension and define
R(t) :=
tY
ℓ=1
(Q + ∆Q(ℓ)). (11)
If P∞ s=1 ∥∆Q(s)∥ < ∞, then limt→∞ R(t) = exϕ⊤ for a suitable vectorϕ. The
exponential rate of convergence is not greater thanmax{ρ, σ}, where ρ is the
magnitude of the largest-in-magnitude of the subdominant eigenvalues ofeU and
σ = lim supt ∥∆Q(t)∥1/t. □
We letU (t) = eU + ∆U (t) with
∆U (t) =

1
1⊤n z(t) − 1 n
  0n 0
1⊤ n AP 1⊤ n (I − A)1n

. (12)
Notice that ∥∆U (t)∥∞ ≤

 1 1⊤n z(t) − 1 n

 n. The connectivity and aperiodicity as-
sumptions imply that AP is Schur stable with spectral radius 0 < λ1 < 1.
Then

 1 1⊤n z(t) − 1 n

 =

1⊤ n (z(t) − 1n)

 n 1⊤n z(t) ≤ ∥(AP )t∥1∥z(0) − 1n∥1 n2
≤ ∥(AP )t∥∞∥z(0) − 1n∥1
n ≤ χ ∥z(0) − 1n∥1λt 1tn n
where the last inequality follows from Lemma 1. SinceP∞ ℓ=1 ∥∆U (ℓ))∥∞ < ∞,
the convergence of the dynamics is then a direct application of Lemma 4.
Iterating the decomposition of matrix U (k) = eU + ∆U (k) and using the
triangular inequality we have
∥
tY
k=0
U (k) − eU t+1∥∞ ≤
tX
k=0
∥ eU k∥∞∥∆U (t − k)∥∞
t−k−1Y
ℓ=0
∥U (ℓ)∥∞.

Since ∥ eU ℓ∥∞ = ∥U (ℓ)∥∞ = 1 for allℓ ∈ N (see Lemma 3) and applying Lemma
2 we get
∥
tY
k=0
U (k) − eU t+1∥∞ ≤ χ∥z(0) − 1∥
tX
k=0
knλk 1
≤ χ∥z(0) − 1∥ λ1pn(λ1) (1 − λ1)n+1 ,
where pn(λ1) is a polynomial of degree equal to n with pn(0) = 1 . By Perron-
Frobenius theorem, the matrix powereU t converges to1n+1 ˜ϕ⊤ as t → ∞. Then,
using triangular inequality and Lemma 4, there exists a constantC > 0 such
that
∥ϕ − ˜ϕ∥1 ≤ ∥1n+1ϕ⊤ −
tY
k=0
U (k)∥∞
+ ∥
tY
k=0
U (k) − eU t+1∥∞ + ∥ eU t+1 − 1n+1 ˜ϕ⊤∥∞
≤ χ∥z(0) − 1∥ λ1pn(λ1) (1 − λ1)n+1 + C max{λ2( eU ), λ1}t,
where λ2( eU ) < 1 is the largest of magnitudes of the subdominant eigenvalues
of eU (see Lemma 4). The statement is then obtained by lettingt go to ∞.
B Proof of Theorem 3
Lemma 5. Assume that for all v ∈ Vthere exists, in the graph associated to
P, a path fromv to w such that γw > 0. If qtot ≥ 1 and z(0) ≥ 1, then U (t) is
Schur stable ∀t ∈ N.
Proof. First, using stochasticity of P, it can be proved thatz(t) ≥ 1n by in-
duction on t ∈ N0. Consequently, the sum of the last row (and of all other
rows) in U (t) is not larger than 1, because1⊤ n AP + 1⊤ n B1n ≤ P i αi + P i βi ≤
n ≤ 1⊤ n z(t). Finally, the connectivity assumption implies that every node is
connected to a node whose corresponding row in the matrixU (t) sums to less
than one. Applying Lemma 5 in [11], we conclude thatU (t) is Schur stable.
We consider now the joint dynamics in (8). The dynamics in (8) can be
written in the following form
s(i)(t + 1) =
 tY
k=0
U (k)
!
s(i)(0) + q(i)
tX
k=0


tY
j=k+1
U (j)

 c(k). (13)
where U (t) = eU + ∆U (t) with eU given in (10) and
∆U (t) =

1
1⊤n z(t) − 1 1⊤n z∗
  0n 0
1⊤ n AP 1⊤ n B1n

, (14)

and c(t) = ec + ∆c(t) with ec given in (10)
∆c(t) =
 0
1⊤ n (I − A − B)1n( 1 1⊤n z(t) − 1 1⊤n z∗ )

. (15)
From now on, we will denote the infinity norm by∥ · ∥.
Remark 1. By Proposition 2, there exist χ1, χ2 > 0 such that ∥∆c(k)∥ ≤
χ1∥(AP )k∥ and ∥∆U (k)∥ ≤χ2∥(AP )k∥.
Lemma 6. The matrices defined in(9) satisfy
tX
k=0
tY
s=k+1
U (s)c(k) =
tX
k=0
eU t−kec +
tX
k=0
eU t−k∆c(k)
+
tX
k=0
t−k−1X
ℓ=0
eU ℓ∆U (t − ℓ)
t−ℓ−1Y
s=k+1
U (s)c(k).
Proof. By repeated application ofU (t) = U + ∆U (t),
tY
s=k+1
U (s) = ( eU + ∆U (t))
t−1Y
s=k+1
U (s)
= eU t−k +
t−k−1X
ℓ=0
eU ℓ∆U (t − ℓ)
t−ℓ−1Y
s=k+1
U (s).
Weconcludebymultiplyingtheexpressionby c(k), summingover k ∈ {0, . . . , t},
and applying c(k) = ec + ∆c(k).
Starting from (13) and the definition ofes(t + 1), we can apply Lemma 6 to
show that
∥s(i)(t + 1) − es(i)⋆∥
≤ ∥
tY
k=0
U (k)∥|∥s(i)(0)∥ + q(i)
tX
k=0
∥ eU t−k∥∥∆c(k)∥
+ q(i)
tX
k=0
t−k−1X
ℓ=0
∥ eU ℓ∥ ∥∆U (t − ℓ)∥
t−ℓ−1Y
s=k+1
∥U (s)∥ ∥c(k)∥
≤ ∥eU t+1∥∥s(i)(0)∥ +
tX
k=0
t−k−1X
ℓ=0
∥ eU ℓ∥ ∥∆U (t − ℓ)∥ si(0) 
+ q(i)
tX
k=0
∥ eU t−k∥∥∆c(k)∥
+ q(i)
tX
k=0
t−k−1X
ℓ=0
∥ eU ℓ∥ ∥∆U (t − ℓ)∥ ∥c(k)∥
where the last inequality is obtained from Lemma 6, by triangular inequality
and observingQt−ℓ−1 s=k+1 ∥U (s)∥ ≤1. The connectivity and aperiodicity assump-
tions imply that both AP andeU have spectral radius in (0,1). By Remark 1,

Lemma 1 and using the boundness ofc(k), there exist positive constantsκ1, κ2,
and κ3 such that
∥s(i)(t + 1) − es(i)⋆∥
≤ κ1tnρ( eU )t+1 + κ2
tX
k=0
(k(t − k))nρ( eU )t−kρ(AP )k (16)
+ κ3
tX
k=0
t−k−1X
ℓ=0
(ℓ(t − ℓ))nρ( eU )ℓρ(AP )t−ℓ
We now distinguish two cases. (i) Caseρ(AP ) < ρ( eU ):
∥s(i)(t + 1) − es(i)⋆∥ ≤κ1tnρ( eU )t+1 + κ2tnρ( eU )t
tX
k=0
kn
 ρ(AP )
ρ( eU )
k
+ κ3tn
tX
k=0
t−k−1X
ℓ=0
ρ( eU )t−k−1−ℓρ(AP )ℓ+k+1
≤ κ1ρ( eU )t+1 + eκ2tnρ( eU )t
+ fκ3tnρ( eU )t
tX
k=0
(k + 1)n ρ(AP )k+1
ρ( eU )k+1
t−k−1X
ℓ=0
ℓn ρ(AP )ℓ
ρ( eU )ℓ
≤ κ1ρ( eU )t+1 + κ4tnρ( eU )t,
where the last inequality, with κ4 > 0, follows from Lemma 2. The claim
follows by renaming the constant terms.
(ii) Case ρ(AP ) > ρ( eU ): Fix nowϵ ∈ (1 − ρ(AP ), 1 − ρ( eU )) then ρ(AP )s <
ρ(AP )t/(1 − ϵ)t−s for anys < t. From (16), there exist constantsκ1 > 0, κ2 > 0
∥s(i)(t + 1) − es(i)⋆∥ ≤κ1tnρ( eU )t+1
+ κ2tnρ(AP )t
tX
k=0
kn ρ( eU )k
(1 − ϵ)k
+ κ3tn
tX
k=0
ρ(AP )t
t−k−1X
ℓ=0
ℓn ρ( eU )ℓ
(1 − ϵ)ℓ
≤ κ1tnρ( eU )t+1 + κ4ρ(AP )ttn+1.
Theorem 3 follows because∥s(i)(t) − es(i)⋆∥ converges to 0.
