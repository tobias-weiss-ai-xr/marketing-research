---
title: Competition and Collusion in Two-Sided Markets with an Outside Option
url: https://arxiv.org/abs/2505.06109
category: consumer-behavior
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Cristian Chica
- Yinglong Guo
- Gilad Lerman
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.06109
pages: 64
chars: 151987
fetched_at: '2026-11-08T13:10:11+00:00'
kb_version: 1
---

# Competition and Collusion in Two-Sided Markets with an Outside Option

arXiv:2505.06109v1  [econ.GN]  9 May 2025
Competition and Collusion in Two-Sided Markets with
an Outside Option*
Cristian Chica, Yinglong Guo, and Gilad Lerman†
June 12, 2025
Abstract
We introduce pricing formulas for competition and collusion models of two-sided markets
with an outside option. For the competition model, we find conditions under which prices and
consumer surplus may increase or decrease if the outside option utility increases. Therefore,
neglecting the outside option can lead to either overestimation or underestimation of these
equilibrium outputs. Comparing collusion to competition, we find that in cases of small cross-
side externalities, collusion results in decreased normalized net deterministic utilities, reduced
market participation and increased price, on both sides of the market. Additionally, we observe
that as the number of platforms increases in the competition model, market participation rises.
Profits, however, decrease when the net normalized deterministic utility is sufficiently low but
increase when it is high. Furthermore, we identify specific conditions that quantify the change
of price and consumer surplus when the competition increases.
Keywords: Competition, Collusion, Outside Option, Two-sided Markets, Externalities
1 Introduction
Platform businesses have immensely grown in the last several decades due to the widespread adop-
tion of communication technologies.1 For example, the sales of Amazon, which is a platform, have
grown from $148 millions in 1997 to $386 billions in 2020 (Wells et al., 2021). Platforms facilitate
the interaction between different types of users, such as buyers and sellers (Amazon and eBay),
drivers and riders (Uber and Lyft) and content creators and consumers (YouTube, Twitch and Spo-
tify). Their business model has become very popular, but its careful study is still in an early stage,
where the first research works are from the beginning of this century (see, e.g., Rochet and Tirole
*This work was partially supported by NSF awards DMS 2124913 and 2427955. We sincerely thank Prof. ¨Ozlem
Bedre Defolie and the anonymous reviewers for their invaluable feedback and insights, which have significantly en-
hanced the quality of our work.
†School of Mathematics, University of Minnesota. Email addresses: chica013@umn.edu, guo00413@umn.edu,
lerman@umn.edu.
1According to the United States Census Bureau, the percentage of US citizens reporting owning a computer has
grown from 8% in 1984 to 89% in 2016 (see, e.g., Ryan (2017)).
1

(2003) and Caillaud and Jullien (2003)). There are still many open questions and, in particular, a
complete model of platform competition is still far from reach.
A common yet limiting assumption in platform modeling is full market coverage, meaning that
in equilibrium all users join at least one platform. While this assumption is strong, most models
incorporate it because it leads to explicit equilibrium pricing formulas (see, e.g., Tan and Zhou
(2021)). In this work, we relax this assumption by considering a model in which N horizontally
differentiated platforms compete across two market sides—buyers and sellers (collectively referred
to as users)—who can either join one of the platforms (single-homing) or choose not to participate,
a choice referred to as the outside option.
Dating apps offer a clear example of a market with a significant outside option and platform
competition. Many users still prefer traditional, non-priced methods of meeting partners—such
as through friends or at school—underscoring the importance of the outside option. This market
also includes numerous competing platforms. While users typically multi-home across apps (see,
e.g., the last table in SSRS (2024)2), some platforms encourage behavior closer to single-homing.3
For tractability, some economic models assume single-homing in this context (see, e.g., Gal-Or
(2020); Halaburda et al. (2018)). We thus use this market to ground some of our theoretical results.
Ride-sharing services (e.g., Uber and Lyft) offer another example of a market with a strong outside
option—public transportation, scooters, or e-bikes—but with pronounced multi-homing, as users
switch between platforms depending on availability, pricing, or convenience.
We develop pricing formulas for our model and express them in terms of the equilibrium nor-
malized net deterministic utility that platforms provide to users, i.e., the difference between the
deterministic utility of users joining one platform and the deterministic utility of the outside op-
tion. This allows us to transition from a space of prices to a space of utilities in the spirit of
Armstrong and Vickers (2001).
We utilize these pricing formulas to study competition and collusion between platforms with
an outside option. We first establish sufficient conditions for the existence and uniqueness of a
symmetric Nash equilibrium and a collusive equilibrium in this setting. We further show that under
small cross-side externalities,4 the normalized net deterministic utilities and market participation
are smaller in collusion than in competition; furthermore, the prices on both sides are bigger in
collusion than in competition. We also study the effect of increasing competition on the outputs of
the competitive Nash equilibrium. In this case of increasing competition, we specify regimes for
the decrease or increase of both prices and consumer surplus (these regimes depend on the size of
the user’s heterogeneity in tastes, the number of platforms and the size of network externalities).
We demonstrate how these results can shed light on the pricing strategies observed in dating apps
and how they change depending on the heterogeneity of the population and the size of network
2The table shows the percentage of people in different age groups who have ever used specific dating sites or apps
among those who have used any dating site or app. It indicates that, on average, individuals have used about two
different apps, with this average decreasing with age. However, since people may use different apps at different times,
the number of apps used simultaneously is likely lower.
3For example, Hinge markets itself as “designed to be deleted,” while loyalty-encouraging subscription models,
like Bumble Boost, and curated apps, like The League or JDate, may encourage users to stick with a single app.
4Cross-side externalities capture the benefits that users on one side of the market derive from interaction with users
on the other sides of the market. When these externalities are positive, platforms are confronted with the “chicken &
egg” problem: to attract buyers, the platform must have a large base of sellers, who will join the platform if and only
if there are many buyers in the platform (see Caillaud and Jullien (2003)).
2

externalities.5 We further show in this case that market participation always increases, and profits
decrease if the net normalized deterministic utility is sufficiently small and increase if the net
normalized deterministic utility is sufficiently large.
The size of the outside option determines the sign of the net deterministic utility in a nonlinear
fashion. Indeed, we show that there exists a critical threshold for the deterministic outside option
utility such that above this threshold users only receive negative deterministic utility, and below this
threshold the sign of the net deterministic utility depends on the relative size of the heterogeneity
in user’s tastes versus the within-side externalities.
Moreover, we show that when the outside option increases, prices and consumer surplus may
increase or decrease, based on the relative size of the heterogeneity in user’s tastes versus the
within-side externalities. In particular, we show that a model of platform competition that omits
the outside option may overestimate or underestimate the true equilibrium price.
Our pricing formulas imply the following standard results for platforms, accounting for an
outside option (see further references and details in Section 3): (i) platforms hold market power
and charge users in a way that is directly proportional to user’s heterogeneity in tastes; (ii) if the
within-side externalities6 are positive, platforms subsidize users on one side of the market by an
amount that is proportional to the joining population on this side of the market; (iii) if the cross-
side externalities are positive, platforms subsidize users on one side of the market with an amount
proportional to the joining population on the other side of the market. The alignment of our results
with existing ones suggests that the standard platform pricing strategy can be more general than
previously understood.
Related Literature. The study of two-sided markets has emerged in the last few decades.
The earlier works of Rochet and Tirole (2003, 2006), Caillaud and Jullien (2003) and Armstrong
(2006) laid out the modeling foundations of two-sided markets with network externalities. These
works shed some light on how equilibrium outputs of platform competition and platform monopoly
depend on: (i) the size of the network externalities relative to user’s heterogeneity in tastes; (ii)
users being able to join either one or two platforms (i.e., having a single-home or multi-home
option). Weyl (2010) and White and Weyl (2016) placed an emphasis on platform competition
with insulated tariffs, which allow platforms to choose participation rates rather than prices.
Tan and Zhou (2021) modeled competition between N ≥ 2 platforms serving multiple sides of
a market. In this setting, customers are heterogeneous and modeled through random idiosyncratic
preferences. Under general conditions for the probability distribution of idiosyncratic preferences,
they characterized a symmetric subgame perfect equilibrium. Our model generalizes their ap-
proach by incorporating an outside option and conducting an extensive analysis for specific prob-
ability distributions. This generalization enables us to study the effects of the outside option on
equilibrium outputs and collusion in two-sided markets. We remark that Tan and Zhou (2021)
pricing formulas are similar to the ones in Armstrong (2006), White and Weyl (2016), Jullien and
Pavan (2019) and Chica et al. (2021) in the sense that they explicitly depend on the parameters.
Due to the challenges of the outside option in our model, our pricing formulas are implicitly deter-
5Dating markets with heterogeneous populations are dominated by general apps like Tinder and Bumble, while
more homogeneous populations tend to use niche apps like The League and JDate.
6Within-side externalities capture negative within-side competition effects and positive collaboration effects be-
tween users on the same side of the market. For example, competition between content creators in the same platform
(e.g., YouTube, Twitch and others) and collaboration between open source programmers (e.g.,C++, Python, Linux and
others).
3

mined by the equilibrium net deterministic utility and cannot be explicit like the previous formulas.
Similar to Tan and Zhou (2021), but under the assumption of an outside option, we find that increas-
ing competition can either raise or lower equilibrium prices and consumer surplus—depending on
the relative strength of network externalities versus user heterogeneity in tastes—and may also
increase or decrease platform profits, depending on a condition involving the normalized net de-
terministic utility. However, we show that market participation always increases, whereas Tan and
Zhou (2021) assumes 100% market participation. Moreover, our collusion analysis is novel and
cannot be addressed in markets with full participation.
Cohen and Zhang (2022) focused on the particular setting and idiosyncrasies of ride-sharing
services (e.g., Uber and Lyft). One of their interesting results is that under collusion riders pay
a larger price and drivers receive a lower wage than under competition. This result is similar to
one of our results (to see this one should note that the wage in their model is a negative price in
our model). Nevertheless, the modeling choice for customer demand is different in both works. In
their model, network externalities are endogenous, whereas ours are exogenous and thus follow the
traditional setting that stems from Armstrong (2006). As such, we can examine the effects of the
network externalities on the equilibrium outputs. Another major difference between these works is
the type of solution obtained. They inductively solve a sequence of problems, which approximates
the Nash equilibrium, and their final solution is a limit of the former solutions. We characterize the
best-response of a platform that deviates from the symmetric Nash equilibrium and directly study
properties of this equilibrium. The major advantage of our approach is that it allows us to study
the effects of competition on the equilibrium outputs, because we can differentiate these outputs.
Our work also pertains to the literature on platform collusion. On the theoretical side, Dewenter
et al. (2011) compared between competition, semi-collusion (i.e., collusion in only one side of the
market) and full collusion in a special model for the newspapers market, where the two sides of
the market were represented by advertisers and readers. Comparing full collusion to competition,
they found out that for the advertisers market, participation is lower and prices are higher under
full collusion. This result is similar to one of ours, as we show that for both sides of the markets,
all sizes of within-side externalities and relatively small cross-side externalities, collusion always
leads to less market participation and higher prices.7
Other relevant works that include an outside option are: Jeitschko and Tremblay (2020), which
studied how consumers and firms endogenously choose between different homing options or the
outside option; Correia-da Silva et al. (2019), which examined the welfare effects of horizon-
tal mergers between multi-sided platforms while incorporating an outside option for consumers;
Tremblay et al. (2023), which analyzed Cournot platform competition in two-sided markets with
indirect network effects, where both consumers and sellers have an outside option; Peitz and Sato
(2023) studied a model of asymmetric platform oligopoly while allowing partial user participation,
i.e., outside options; and Teh et al. (2023) study the effects of allowing multi-homing for both sides
of the market while also incorporating outside options.
Organization of the Article: Section 2 formulates our platform models of competition and
7Note that we focus on the study of full collusion, whereas Dewenter et al. (2011) and Lefouili and Pinho (2020)
also study semi-collusion in two-sided markets and show that if the cross-side externalities are positive and sufficiently
large, then semi-collusion may benefit users on the collusive side and harm users on the competitive side. Furthermore,
Dewenter et al. (2011) also show that on the readers side, the collusion price may be lower than the competitive price
if the competition in the advertising market is high and the newspaper market is large. We remark that our demand
specification is different and, in particular, we do not incorporate a parameter for the relative size of the markets.
4

collusion. Section 3 solves the models via backward induction. Section 4 compares the outputs
of colluding and competing market models. Section 5 examines the effects of increasing compe-
tition on the equilibrium quantities of the competition model. Section 6 examines the economic
implications of our main results. Section 7 concludes this work.
2 The Platform Model with an Outside Option
We formulate a platform competition model by following previous works, such as White and Weyl
(2016) and Tan and Zhou (2021). LetN ≥ 2 be the number of horizontally differentiated platforms
in the market. Each index i ∈ N := {1, . . . ,N} represents a platform competing in two different
sides of a market. We index each side by k ∈ {b,s}, where b and s represent buyers and sellers,
respectively. Each platform i sets prices for each side of the market, denoted by pi = (pi b, pi s).
The endogenous mass of users on each side of the market subscribed to platform i is denoted by
xi = (xi b,xi s) ∈ [0,1]2. For i = 0, x0 = (x0 b,x0 s ) ∈ [0,1]2 denotes the mass of users not participating
in the market.
Users on side k of the market have idiosyncratic preferences for platforms and for the outside
option. These preferences are captured by the i.i.d. random variables εi k ∼ Fk(·), where k ∈ {b,s},
i ∈ N ∪ {0} (i ∈ N for the platforms and i = 0 for the outside option) and Fk(·) is a differentiable
probability distribution.
The game consists of two stages. In stage 1, platforms strategically choose prices to maximize
profits. In this article, we study two scenarios in stage 1: (i) The competition scenario, where
firms compete and maximize individual profits; (ii) The collusion scenario, where firms collude
and jointly maximize profits. In stage 2, given the prices determined by the platforms, users on
each side of the market choose whether to participate or not and if they participate they also choose
which platform to join. The game is solved using backward induction and we thus first describe
the details of the second stage and then the first one.
(i) Stage 2 (users’ interactions):Any user on sidek ∈ {b,s} of the market who joined platform
i ∈ N receives the following utility:
ˆui k := εi k − pi k + φk(xi), (1)
where εi k represents the idiosyncratic utility the user enjoys; pi k is the price paid by the user to
access services provided by the platform (it was determined in stage 1); and φk : [0,1]2 − →R is a
Lipschitz differentiable function so that φk(xi) captures the network benefits that the user receives
from all other users who are also joining platformi. We further denote the deterministic component
of the utility by
ui k := −pi k + φk(xi).
If a user does not join any platform, it receives the utility
ˆu0 k = ε0 k + u0 k, (2)
where u0 k ∈ R is a constant representing the deterministic outside utility. 8 Note that users will
choose the platform that maximizes their utility, i.e., they will join j ∈ argmaxi∈N ∪{0}{ ˆui k}. It
8Most models of platform competition leave out the analysis of the outside utility option that users have. By doing
so, they cut out from the profit maximization process the trade-off between market participation and competition. In
this article, we study this trade-off.
5

follows that the mass of users from side k joining platform i solves the equation
xi k = P

ˆui k > max j∈N ∪{0}\{i} { ˆu j k}

∀k ∈ {b,s}, i ∈ N ∪ {0}. (3)
Proposition 3.1 below implies that (3) has at least one solution for any set of prices {(pi b, pi s)}N i=1,
and also establishes a sufficient condition for a unique solution of (3).
(ii) Stage 1 (platforms’ optimization): We consider the following two scenarios: a competi-
tive market and a collusive market.
(a) A competing market: Platform i, for each i ∈ N , sets prices {pi b, pi s} that maximize indi-
vidual profits, i.e., platform i solves
max
{pi b,pis} πi  pi b, pi s  , where πi  pi b, pi s  := xi bpi b + xi spi s, (4)
and xi k is implicitly defined by (3). We adopt the standard assumption of zero marginal cost for
serving users on sides b and s. A Nash equilibrium corresponding to (4) is referred to as a compet-
itive Nash equilibrium (CNE).
(b) A colluding market: The colluding platforms act as a single platform trying to maximize
joint profits across all sides of the market by charging one price on every side of the market; i.e.,
they solve
maxpb,ps Πtot(pb, ps), where Πtot(pb, ps) :=
N
∑
i=1

xi bpb + xi sps  . (5)
As in the competitive case, we assumed that the marginal costs of serving sellers and buyers are
zero. We refer to any maximizer of (5) as collusive equilibrium (CE).9
In order to fully quantify the equilibrium outcomes, we make two additional assumptions:
(a) Assumption I: The idiosyncratic preferences, {εi k}k∈{b,s},i∈N ∪{0}, are i.i.d. Gumbel distributed
with parameters (µk, βk). That is, for k ∈ {b,s}, βk > 0 and µk ∈ R, the distribution Fk(·) is
Fk(z) =e−e
µk−z
βk
. (6)
We claim that this assumption is natural since it gives rise to the classical Logit model (see Werden
et al. (1996), Anderson and De Palma (1992)), which describes the demand of heterogeneous
consumers for a set of differentiated goods (see Berry (1994), Conlon and Gortmaker (2020),
Besanko et al. (1998)). To support this claim, we note that the central equation in this work is (3),
which can be rewritten using (2) and the alternative variablesθ i k = εi k − ε0 k , i ∈ N ∪ {0}, k ∈ {b,s}
as follows:
xi k = P

θ i k + ui k ≥ max j=0,1,...,N, j̸=i
n
θ j k + u j k
o
, ∀k ∈ {b,s}, i ∈ N ∪ {0}.
We further note that θ i k ∼ Logistic(0, βk) for i ∈ N and thus conclude the claim.
9While, in general, collusion can be any situation where two or more platforms jointly make decisions, in this
article, we focus on the worst-case-scenario, where all platforms collude.
6

(b) Assumption II: The function φk(x) is linear, i.e., it can be represented by multiplying with
the real-valued matrix Φ ∈ R2×2
 φb(xb,xs)
φs(xb,xs)

=
 φbb φbs
φsb φss

| {z }
Φ
 xb
xs

. (7)
We remark that the following results do not require these additional assumptions: The exis-
tence and uniqueness of the solution of (3) (see Proposition 3.1 in Section 3) and the derivation
of the first- and second-order conditions for both (4) and (5) (see Lemma A.1, A.2, A.3 and A.4
in Appendix A). We note that many of the results presented in this paper can be extended to other
probability distributions of economic interest. In the Online Appendix, we demonstrate this for
the exponential distribution with two platforms. In particular, we explicitly derive the first-order
condition for (4) using Mathematica. Additionally, we present numerical simulations supporting
results similar to those shown in Propositions 4.4, 4.6, and 4.7, but using the exponential distribu-
tion. It is important to recognize that each probability distribution requires special treatment, and
the analysis of the Gumbel distribution is already quite lengthy and complex.
3 Equilibrium
We solve our model using backward induction. We first study the solution to (3) and show that
for any set of prices, {(pi b, pi s)}N i=1, there is a well-defined set of market shares, {(xi b,xi s)}N i=0, that
solve (3) and under a certain condition they are unique. Next, we characterize the symmetric CNE
of (4) (i.e., the CNE such that pi k = p∗ k for each i ∈ N ) and the CE of (5). At last, we interpret the
resulting equilibrium pricing and market share formulas.
Stage 2 Solution: Users’ Maximization
We establish sufficient conditions for the existence and uniqueness for (3). We recall that (3)
captures the users’ dynamics when prices change. Let u = (u0,u1, . . . ,uN) ∈ RN+1 and for k ∈
{b,s} and i ∈ N ∪ {0} define
T i k (u) := P(εi k > max j̸=i (ε j k + u j − ui)). (8)
In view of (8), (3) can be rewritten as
xi k = T i k (u0 k, φk(x1) − p1 k, . . . ,φk(xN) − pN k ). (9)
It follows that a vector x = (x0 b,x0 s , . . . ,xN b ,xN s ) solves (3) if and only if it is a fixed point of the map
Σ : [0,1]2(N+1) − →[0,1]2(N+1) given by
Σ(x) := (T 0 b (ub),T 0 s (us), . . . ,T N b (ub),T N s (us)), (10)
where uk = (u0 k, φk(x1) − p1 k, . . . ,φk(xN) − pN k ) and xi = (xi b,xi s). Proposition 3.1 below, shows
that (10) always has at least one fixed point and thus (3) always has a solution. This proposition
7

also provides sufficient conditions for the uniqueness of this fixed point and the solution of (3). Its
formulation requires the following Lipschitz-type constants:
MT := max k∈{b,s},i∈N ∪{0} sup u∈RN+1
N
∑
l=0

 ∂T i k (u) ∂ul

 , and
Mφ := max k∈{b,s} sup (xb,xs)∈[0,1]2 ∑ l∈{b,s}

 ∂ φk(xb,xs) ∂xl

 . (11)
We remark that ∂T i k (u)/∂ul captures the user’s sensitivity to changes in utility levels. Similarly,
∂ φk(xb,xs)/∂xl measures how externalities change when more people join one specific platform.
Proposition 3.1 (Existence and Uniqueness of Market Shares). For any prices{(pi b, pi s)}N i=1 ⊂ R2,
there exists a solution to (3),x = (x0 b,x0 s ,x1 b,x1 s , · · ·,xN b ,xN s ), such that for each k∈ {b,s}, ∑N i=0 xi k =
1. Moreover, if MT Mφ < 1, where MT and Mφ are given by (11), then the solution of (3) is unique.
This Proposition provides sufficient conditions for the mapping {(pi b, pi s)}N i=1 7→ {(xi b,xi s)}N i=0
to be well-defined. Its proof is in Appendix A.10
Stage 1 Solution: Platforms’ Optimization
We establish sufficient conditions for the existence and uniqueness of symmetric solutions of (4)
and (5). We first focus on symmetric solutions for (4). For this purpose, we use the following
transformation:
zk := uk − u0 k βk , for k ∈ {b,s}. (12)
We note that uk − u0 k ≡ −pk + φk(x) − u0 k captures the difference between the deterministic utility
of users (sellers or buyers) joining one platform and the deterministic utility of the outside option.
We remark that in the symmetric case any platform charges the price pk for k ∈ {b,s} and the
market shares are given by x = (xb,xs). The Gumbel distribution parameter βk is a measure of the
standard deviation of the idiosyncratic preference εi k and it captures the degree of heterogeneity
in users’ tastes. 11 Throughout the article, we will refer to zk as the normalized net deterministic
utility of users on side k of the market.
We can write the first-order condition (FOC) of (4) as a function of zk.12
Proposition 3.2 (FOC of (4)). Suppose there is a symmetric equilibrium (p∗ b, p∗ s ) solution of (4)
with market shares (x∗ b,x∗ s ). If one platform unilaterally deviates from this symmetric CNE, the
FOC that characterizes its best-response is given by
βz = (Φ − H(z)) Ω(z) − u0, (13)
10We remark that while Proposition 3.1 is used to identify symmetric Nash equilibria, it should not be restricted
to symmetric market shares. When proving the existence of symmetric Nash equilibria (see Proposition 3.3), it is
necessary to consider all possible deviations from the equilibrium path, including those that lie off the symmetric path.
11Note that in general, if εi k ∼ G(µk, βk), then Var[εi k] =π2 6 β 2 k and thus the standard deviation of εi k is π√ 6 βk.
12It is a known fact that attempting to solve (4) by means of an FOC with respect to prices{(pi b, pi s)}N i=1 produces a
non-tractable system of equations (see, e.g., Tan and Zhou (2021) and Chica et al. (2021)). By contrast, our proofs in
the appendix take derivatives with respect to {xi b,xi s}N i=1. By Proposition 3.1 and the implicit function theorem, there
is a well-defined locally 1-1 mapping from {(xi b,xi s)}N i=1 to {(pi b, pi s)}N i=1.
8

where β = diag(βb, βs), z = (zb,zs), u0 = (u0 b,u0 s ), Φ is the externalities network matrix defined
in (7), Ω(z) = (ω(zb), ω(zs))T with ω : R − →(0, 1 N ) such that ω(z) := 1 e−z+N , and H(z) is a 2x2
matrix defined as
H(z) :=
LbdbKs + hb − φbb −φsb(dsLb + 1)
−φbs(dbLs + 1) LsdsKb + hs − φss

, (14)
where Lk, dk and hk for each k ∈ {b,s} are given by
Lk = (N − 1)βk Jφ (1 + Nezk),
dk = βk(1 + Nezk),
hk = βk(1 + ezk)(e−zk + N),
Kk = φkk − βk(1 + Nezk)(e−zk + N − 1),
Jφ = KbKs − φsbφbs.
(15)
Let us assume z∗ = (z∗ b,z∗ s )T is the unique solution of (13) and it satisfies a corresponding
second order condition. We discuss below (see Proposition 3.3) sufficient conditions for this as-
sumption. We use z∗ to characterize the symmetric equilibrium solution of (4), p∗ = (p∗ b, p∗ s )T ,
with market shares x∗ = (x∗ b,x∗ s )T . By applying (8) and (9) evaluated at ui k = u∗ k = −p∗ k + φk(x∗),
where i ∈ N and k ∈ {b,s}, one can show (see (76) in Appendix A) that
x∗ k = ω(z∗ k) ≡ 1 e−z∗ k + N and thus x∗ = Ω(z∗). (16)
We further note that (12) implies thatβz ∗ = −p∗ + Φx∗ − u0. Combining the latter equation, (13)
and (16), the symmetric CNE of (4) is given by
p∗ = H(z∗)Ω(z∗) and
x∗ = Ω(z∗). (17)
In order to ensure that (17) yields the symmetric CNE, we next establish a sufficient condition
for (13) to have a unique solution that satisfies a corresponding second order condition. It uses the
following function
f (N) := 2(N − 1) N2 , (18)
where we note that f approaches 0 as N → ∞. It also uses the notation Bε (0) for the ball in R2 of
radius ε > 0 around the origin.
Proposition 3.3 (Existence and uniqueness of the symmetric CNE) . Suppose that N ≥ 2 and for
each k ∈ {b,s}, (φkk, βk) satisfies
either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > f (N) φkk) . (19)
Then, there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) there is a unique solution of (13) and
this solution satisfies a second order condition. 13 Furthermore, (17) yields the unique symmetric
CNE of (4).
13We clarify that the ε in Proposition 3.3 depends on (φbb, φss, βb, βs,N,u0 b,u0 s ), but for simplicity we denote it by
ε. We use the same convention in other places in this article where a similar condition with ε appears.
9

Proposition 3.3 guarantees the existence and uniqueness of a symmetric CNE for a large family
of the parameters {φkk, βk}k∈{b,s}. In particular, if the within-side externalities (i.e., those that re-
flect interactions of the same sides of the market), φkk, are negative, then existence and uniqueness
of a solution for (13) is guaranteed for any size of heterogeneity in user’s tastes, βk. On the other
hand, if the within-side externalities are positive, then existence and uniqueness is only ensured for
relatively large sizes of heterogeneity in user’s tastes (i.e.,βk > f (N)φkk). Recall that as the number
of platforms N grows to infinity, f (N) approaches 0. Thus, even for positive within-side externali-
ties, existence and uniqueness of a solution for (13) is guaranteed for any size of βk, provided that
the number of platforms in the market is large enough. Some form of the latter condition appears
in many studies of platform competition (see, e.g., Anderson et al. (1992), Armstrong (2006),
and Tan and Zhou (2021)). This condition ensures that network effects do not always dominate
idiosyncratic preferences when users are charged non-zero prices (see, e.g., Chica et al. (2021)).
Figure 1 below shows the region described by (19) when N = 4.
Figure 1: Region of (φkk, βk) that guarantees a unique symmetric CNE when N = 4 according to
Proposition 3.3.
Next, we focus on the solution of (5). We first establish the FOC of (5) as a function of zk.
Proposition 3.4 (FOC of (5)). The FOC of (5) is given by
βz = (Φ − HC(z))Ω(z) − u0, (20)
where β, z, u0, Φ, Ω(z) were defined in Proposition 3.2, and HC(z) is a 2x2 matrix defined by
HC(z) :=
"
βb(1+Nezb )2
ezb − φbb −φsb
−φbs βs(1+Nezs )2 ezs − φss
#
. (21)
Let us assume zC = (zC b ,zC s )T is the unique solution of (20) and it satisfies a corresponding
second order condition (we provide sufficient conditions for these assumptions in Proposition 3.5
below). Following the same derivation of (17) (see the proof of Proposition 3.4 in Appendix A),
one can show that the CE solution of (5), pC = (pC b , pC s )T and the corresponding market shares,
xC = (xC b ,xC s )T , satisfy
pC = HC(zC)Ω(zC) and
xC = Ω(zC). (22)
10

In order to ensure that (22) yields the CE, we establish sufficient conditions for (20) to have a
unique solution that satisfies a corresponding second order condition.
Proposition 3.5 (Existence and uniqueness of the CE) . For any u0 b,u0 s ∈ R, Φ ∈ R2x2, βb, βs > 0
and N ≥ 2, there exists a solution for (20). Moreover, if for each k∈ {b,s}, (φkk, βk) satisfies
either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > 8φkk 27N ), (23)
then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂ R2, the solution for (20) is unique, it
satisfies a corresponding second order condition and (22) yields the unique CE of (5).
The proof of Proposition 3.5 implies thatf (N)φkk, which was used in Proposition 3.3, is strictly
bigger than 8φkk/(27N) for all φkk > 0. It follows that, if (φkk, βk) satisfies (19) for each k ∈ {b,s},
then it also satisfies (23) and consequently there exists unique solutionsz∗ and zC to (13) and (20),
respectively. Section 4 will compare these two solutions assuming (19) is satisfied.
Interpretation and Implications of the Resulting Pricing Formulas
We discuss the pricing formulas (17) and (22) for the competition and collusion models. We first
relate them to common pricing competition models. Both formulas are expressed in terms of the
equilibrium normalized net deterministic utility, zk, that platforms provide to users on both sides
of the market. They thus remind the formulation in Armstrong and Vickers (2001), where multiple
firms compete in a utility space, instead of a space of prices. When solving (4), firms internalize
competition for users in terms of the utility they can provide w.r.t. (with respect to) the outside
utility. The optimal vector utility, z∗, provided by the competing platforms is determined so that
some users are always excluded from the market. 14 A similar result is obtained for the colluding
case, while excluding a larger portion of participants, as shown below in Proposition 4.11. There-
fore, our models also imply the standard result that the output is not optimally distributed among
users when there is price competition or collusion (see, e.g., Varian (1989), Armstrong (1996) and
Rochet and Chon´e (1998)).
Our pricing formulas (17) and (22) generalize many of the standard results in the platform’s
literature for the case of an outside option. We emphasize some of these generalizations: (i) For
CE, the term βk(1 + Nezk)2/ezk, which appears in the diagonal of the matrix (21), captures the
platform’s market power (see Perloff and Salop (1985)). It implies that in equilibrium platforms
charge users on side k of the market proportionally to the platform’s differentiation parameter βk
(see Tan and Zhou (2021) and Chica et al. (2021)). (ii) For CNE and CE, assume that the within-
side externalities are positive (i.e., φkk ≥ 0). Then, from the diagonal of (14) and (21), platforms
subsidize users on side k by an amount that is proportional to the joining population on this side of
the market (i.e., they subsidize users on sidek with φkkx∗ k and φkkxC k , respectively, for the competing
and colluding models). If these externalities are negative (i.e., φkk < 0), the opposite result is true
(see Bardey et al. (2014)). (iii) For CNE and CE, assume positive cross-side externalities, that
is, φlk ≥ 0 for each l,k ∈ {b,s}, l ̸= k. Then, the off-diagonal terms of (14) and (21) imply that
platforms subsidize users on side k with an amount directly affected by the joining population on
the other side of the market (i.e., platforms subsidize an amount φlkx∗ l to users on side k).
14Note that the equilibrium market share satisfies x∗ k = ω(z∗ k) < 1/N (see (17) and the definition of ω(·) in Propo-
sition 3.2). This condition excludes the participation of some users.
11

4 Competition and Collusion in Two-sided Markets with an
Outside Option
We compare the colluding and competing market models by studying the main properties of and
differences between the pricing formulas (17) and (22). We first assume competition and character-
ize the markets in which users receive positive and negative normalized net deterministic utility,z∗ k
(see Proposition 4.1 and Corollary 4.2). We also characterize the sign of z∗ k under perfect competi-
tion (i.e., as N → ∞) and show that platforms charge a price that is equal to user’s heterogeneity in
tastes while covering the entire market (see Corollary 4.3). We then study the effects of the outside
option on the change of prices, profits and consumer surplus. In particular, we show that when
the outside option increases: (i) prices on side k may increase or decrease (see Proposition 4.4);
(ii) profits decrease (see Proposition 4.6); and (iii) consumer surplus may increase or decrease (see
Proposition 4.7). Next, we assume collusion and characterize markets in which zC k is positive or
negative (see Proposition 4.8 and Corollaries 4.9 and 4.10). Finally, we compare the equilibrium
quantities of competition and collusion (see Proposition 4.11).
The Sign of the Net Deterministic Utility Under Competition
In CNE, a positive (negative)z∗ k implies that the deterministic utility that users enjoy in equilibrium
from joining a given platform is larger (smaller) than the deterministic utility of the outside option.
For this reason, we first study the sign of z∗ k as given by the solution of (13). The following
proposition shows sufficient conditions to partition the region described by (19) into two regions:
{z∗ k < 0} and {z∗ k > 0}, which we demonstrate in Figure 2 for two different values of u0 k. The
indifference region {z∗ k = 0} is described by a curve βk = γ(N, φkk,u0 k) in the plane (φkk, βk), where
γ is defined as follows:
γ(N, φkk,u0 k) :=

2φkk − Nu0 k  + r 2φkk − Nu0 k 2 + 4φkk  u0 k − 2φkk N+1 
2 (N + 1) . (24)
We remark that the clustering of the sign ofz∗ k according to this proposition requires a local bound
on the cross-side externalities.
Figure 2: Classification of the sign of z∗ k based on (φkk, βk), k ∈ {b,s}, according to Proposition
4.1, where N = 4 and u0 k = −1 (left) or u0 k = 0.5 (right). The red and blue regions correspond to
negative and positive z∗ k, respectively.
12

Proposition 4.1 (The sign of z∗ k). Suppose that N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies
(19). Then we can further partition the domain specified in (19) into two regions, which cluster the
sign of z∗ k as long as a local condition on the cross-side externalities hold:
(i) If βk > γ(N, φkk,u0 k), then there existsε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂ R2, z∗ k < 0.
(ii) βk < γ

N, φkk,u0 k  , then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂ R2, z∗ k > 0.
We first clarify the economic meaning of this proposition. If user’s heterogeneity in tastes is
large enough (i.e., βk > γ(N, φkk,u0 k)), then it is a standard result that platforms extract consumer
surplus by charging a price that leads to a negative normalized net deterministic utility, i.e.,z∗ k < 0
(see Anderson and De Palma (1992), Tan and Wright (2021), Chica et al. (2021) and others).15 On
the other hand, if the user’s heterogeneity in tastes, βk, is small enough (i.e., βk < γ

N, φkk,u0 k  ),
then users receive positive normalized net deterministic utility, i.e.,z∗ k > 0.
We identify a critical threshold for the deterministic outside utility so that above this threshold,
(ii) in Proposition 4.1 is not feasible.
Corollary 4.2 (The sign of z∗ k for large values of u0 k). Case (ii) in Proposition 4.1 is not feasible if
u0 k ≥ ˜u0 k(N, φkk), where ˜u0 k(N, φkk) is the critical threshold for the deterministic outside utility and
it is defined in (135) in the Appendix A.
This corollary implies that if the deterministic outside utility is sufficiently large (i.e., u0 k ≥
˜u0 k(N, φkk)), the CNE leads to a negative net deterministic utility for any size of heterogeneity in
user’s tastes satisfying (19). In other words, only if the deterministic outside utility is relatively
small (i.e., u0 k < ˜u0 k(N, φkk)), users with relatively weak preferences (i.e.,βk < γ(N, φkk,u0 k)) receive
positive net deterministic utility.
Next, we show that in the case of perfect competition (i.e., the limiting case N → ∞), the sign
of z∗ k can be characterized by the sign of u0 k and the size of βk.
Corollary 4.3 (CNE under perfect competition) . For each k ∈ {b,s}, any u 0 k ∈ R, Φ ∈ R2x2 and
βk > 0, under perfect competition (i.e., when N → ∞),
lim
N→∞
z∗ k
(
> 0, if u0 k < 0 and βk < −u0 k;
< 0, if (u0 k < 0 and βk > −u0 k) or u0 k ≥ 0. (25)
Moreover, as N → ∞, p ∗ k → βk, x∗ k → 0 and Nx∗ k → 1.
Under perfect competition, platforms charge a price that is equal to the user’s heterogeneity
in tastes for that side of the market, i.e., p∗ k = βk. Moreover, the equilibrium market participation
on side k of the market is complete, i.e., Nx∗ k = 1. When the deterministic outside option utility
is positive, users receive negative normalized net deterministic utility for any size of βk under
perfect competition. When the deterministic outside option utility is strictly negative, users receive
positive normalized net deterministic utility if and only if the heterogeneity of users’ taste is small,
i.e. βk < −u0 k. We demonstrate (25) in Figure 3 for two different values (negative and positive) of
u0 k and a sufficiently large N.
15This result is due to the fact that highly heterogeneous users are less responsive to price and demand effects.
13

Figure 3: Classification of the sign of z∗ k based on (φkk, βk), k ∈ {b,s}, for large N according to
Corollary 4.3, where N = 200 and u0 k = −1 (left) or u0 k = 1 (right). The red and blue regions
correspond to negative and positive z∗ k, respectively.
The Effects of the Outside Option on the CNE
The following proposition provides sufficient conditions to characterize the sign of ∂ p∗ k/∂u0 k. It
shows that the effect of the outside option on p∗ k is nonlinear. It uses the following quantities:
gp,u(N) :=

N +
p
(N − 1) (N + 3) +1

2N and
fp,u(N) := 1 2
 r
N − 2
N + 1
!
.
(26)
Proposition 4.4. (The sign of ∂ p∗ k/∂u0 k) Suppose that N ≥ 2 and for each k ∈ {b,s}, (φkk, βk)
satisfies (19). Then we can further partition the domain specified in (19) into two regions, which
cluster the sign of ∂ p∗ k/∂u0 k as long as a local condition on the cross-side externalities hold:
(i) If either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > gp,u (N) φkk), then there exists ε > 0 such
that for any (φbs, φsb) ∈ Bε (0) ⊂ R2, ∂ p∗ k/∂u0 k < 0.
(ii) If φkk > 0, N ≥ 3 and f (N) φkk < βk < fp,u (N) φkk, then there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0) ⊂ R2, ∂ p∗ k/∂u0 k > 0.
Moreover, if(φbs, φsb) =0, then
lim
u0 k→−∞ p∗ k = N N − 1βk − φkk N − 1 =: pk,u, and
lim
u0 k→∞ p∗ k = βk =: pk,E. (27)
Consequently, p∗ k ∈ (pk,E, pk,u) in case (i), and p∗ k ∈ (pk,u, pk,E) in case (ii).
We clarify the economic meaning of this proposition. We first note it implies p∗ k → pk,u when
u0 k → −∞, which coincides with the equilibrium price in a platform competition model with no
outside option. It also implies p∗ k → pk,E = βk when u0 k → ∞, which represents the efficient price,
that is, the price, βk, under perfect competition, expressed in Corollary 4.3. In part (i), the incor-
poration of an outside option into the platform competition model decreases the equilibrium price
14

w.r.t. the no outside option model, which is an expected result. Thus, if the cross-side externalities
are sufficiently small and the within-side externalities are either negative or positive with relatively
large user’s heterogeneity in tastes, then users are compensated by an amount equal to pk,u − p∗ k.
Moreover, in this case, users always pay a price that is bigger than the efficient price, pk,E. On the
other hand, in part (ii), incorporating an outside option increases the equilibrium price w.r.t the no
outside option model, which is non-trivial. Therefore, under sufficiently small cross-side external-
ities and positive within-side externalities, users with relatively small heterogeneity in tastes pay a
premium w.r.t the model with no outside option, which is quantified by p∗ k − pk,u. Moreover, users
always pay a price that is smaller than the efficient price pk,E.
Remark 4.5 (Price overestimation vs. underestimation). If a given population can be parameterized
using the region of parameters described by either (i) or (ii) of Proposition 4.4, then a model
of platform competition that omits the outside option will either overestimate or underestimate,
respectively, the true equilibrium price.
The following proposition shows sufficient conditions to determine the sign of ∂ π∗ k /∂u0 k. It
uses the following quantity:
gπ,u(N) :=
r
N − 1
N3 + 1 N . (28)
Proposition 4.6. (The sign of ∂ π∗ k /∂u0 k) If N ≥ 2 and
either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > gπ,u (N) φkk),
then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂ R2, ∂ π∗ k /∂u0 k < 0. Moreover, if
(φbs, φsb) =0, then
lim
u0 k→−∞ π ∗ k = βk N − 1 − φkk (N − 1)N =: πk,u, and
lim
u0 k→∞ π ∗ k = 0 =: πk,E. (29)
Note that even though, by part (ii) of Proposition 4.4, prices may increase with the outside
option utility, Proposition 4.6 shows that profits are always decreasing w.r.t. u0 k. This happens
because market participation is always decreasing w.r.t. u0 k. Therefore, it is not a surprise that
profits are decreasing as a function of u0 k.
The following proposition provides sufficient conditions to determine the sign of the derivative
of the consumer surplus w.r.t. the outside option utility. More specifically, it uses the equilibrium
consumer surplus on side k of the market, CS∗ k, which is defined as follows (see Tan and Zhou
(2021) for the case without an outside option):
CS∗ k := E

max
i=0,...,N
εi k

− p∗ k + φk (x∗ b,x∗ s ) , (30)
where E

maxi=0,...,N εi k  is the expected maximum idiosyncratic utility.16 It also uses the function
fCS,u(N) given in Appendix A (see (156)).
16Note that max i=0,...,N{εi k} ∼G(µk + βk ln (N + 1) , βk) and thus E[maxi=0,...,N εi k] = [µk + βk ln (N + 1)] +βkγ,
where γ denotes the Euler-Mascheroni constant. This quantity captures the product variety of the market.
15

Proposition 4.7 (The sign of ∂ (CS∗ k)/∂u0 k). The effect of the outside option on the change of
consumer surplus can be clustered into the following two regions:
(i) If N ≥ 2 and either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > 2φkk), then there exists ε > 0
such that for any (φbs, φsb) ∈ Bε (0), ∂ (CS∗ k)/∂u0 k > 0.
(ii) If N ≥ 2, φkk > 0, f (N) φkk < βk < fCS,u (N) φkk, then there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0), ∂ (CS∗ k)/∂u0 k < 0.
Part (i) of this proposition implies that the incorporation of an outside option into the platform
competition model may increase the consumer surplus, or equivalently, the consumer welfare,
w.r.t. the no outside option model. On the other hand, Part (ii) implies that incorporating an outside
option may decrease the equilibrium consumer surplus w.r.t the no outside option model. While
part (i) is standard, part (ii) is surprising.
The Sign of the Net Deterministic Utility Under Collusion
The following proposition quantifies the sign of zC k in the collusion case of (5). In particular, it
claims that the indifference region {zC k = 0} is described by a curve βk = γC(N, φkk,u0 k) in the
plane (φkk, βk), where γC is defined as follows:
γC(N, φkk,u0 k) := 2φkk − u0 k (N + 1) (N + 1)2 . (31)
Proposition 4.8 (The sign of zC k ). Suppose that N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies
(23). Then we can further partition the domain specified in (23) into two regions, which cluster the
sign of zC k as long as a local condition on the cross-side externalities hold:
(i) If βk > γC(N, φkk,u0 k), then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂ R2,
zC k < 0.
(ii) βk < γC  N, φkk,u0 k  , then there existsε > 0 such that for any(φbs, φsb) ∈ Bε (0) ⊂ R2, zC k > 0.
The interpretation of Proposition 4.8 is very similar to that of Proposition 4.1. When the user’s
heterogeneity in tastes is small (i.e., βk < γC(N, φkk,u0 k)), then users receive zC k > 0. On the other
hand, if βk is large (i.e., βk > γC(N, φkk,u0 k)), users receive zC k < 0. Figure 4 demonstrates the
regions described in Proposition 4.8 for two different values of u0 k.
Figure 4: Classification of the sign of zC k based on (φkk, βk), k ∈ {b,s}, according to Proposition
4.8, where N = 4 and u0 k = −1 (left) or u0 k = 0.5 (right). The red and blue regions correspond to
negative and positive zC k , respectively.
16

Corollary 4.9 (γC(N, φkk,u0 k) vs γ(N, φkk,u0 k)). If N ≥ 2 and γ(N, φkk,u0 k) ≥ 0, then γ(N, φkk,u0 k) ≥
γC(N, φkk,u0 k).
By Corollary 4.9, in order to have a positive normalized net deterministic utility zk in CE, the
size of the user’s heterogeneity in tastes must be smaller than in CNE. Moreover, in CE, we also
identify a critical threshold for the outside utility such that above this threshold, the condition of
(ii) in Proposition 4.8 is not feasible.
Corollary 4.10 (The sign of zC k for large values of u0 k). Case (ii) in Proposition 4.8 is not feasible
if u0 k ≥ ˜uC k (N, φkk), where ˜uC k (N, φkk) is the critical threshold for the outside utility and it is defined
in (161) in the Appendix A.
Economic Outputs in Competitive vs. Collusive Markets
The following proposition compares the normalized net deterministic utility, market participation
and prices in competitive and collusive markets.
Proposition 4.11 (Competition vs Collusion Outputs). Suppose that N ≥ 2 and for each k∈ {b,s},
(φkk, βk) satisfies (19). Then, there exists ε > 0 such that for any ϕ1 = (φbs, φsb) ∈ Bε (0) ⊂ R2, in
equilibrium:
(i) the normalized net deterministic utility for users on side k is bigger under competition than
under collusion (i.e., z∗ k > zC k );
(ii) the market participation is bigger under competition than under collusion (i.e., Nx∗ k > NxC k );
(iii) the price charged on side k of the market is smaller under competition than under collusion
(i.e., p∗ k < pC k ).
Part (i) of the above proposition agrees with the standard collusion literature (see, e.g., Bishop
(1960), Varian (1989), Brander and Spencer (1985) among others) in which users receive the lowest
normalized net deterministic utility under collusion. Part (ii) is a direct corollary of part (i). Indeed,
Proposition 3.2 implies that ω(·) is monotonically increasing. Thus, combining (17), (22) and part
(i) of Proposition 4.11 leads to part (ii) as follows: Nx∗ k = Nω(z∗ k) > Nω(zC k ) =NxC k . To explain
part (iii), we use (12) and decompose the difference between collusion and competition prices as
follows:
pC − p∗ = Φ(xC − x∗) +β(z∗ − zC). (32)
competition. A careful combination of this formula with parts (i) and (ii) of Proposition 4.11, the
assumption (φbs, φsb) ∈ Bε (0) (or for simplicity (φbs, φsb) =0) and the observation that if φkk ≥
0 for k ∈ {b,s} then βk > f (N)φkk (see (19)) leads to part (iii). We thus note that the above
detailed analysis regarding the deterministic net utility is valuable for deriving broader economic
implications.
Our results can be compared to other ones on platform collusion. Dewenter et al. (2011) study
collusion and competition following the idiosyncrasies of a newspapers market with two firms.
They find that for small cross-side network externalities the collusive price is higher than the
competitive price. We generalize this result by incorporating the outside option utility, u0 k, the
within-side network externalities, φkk, and by having N horizontally differentiated platforms. Part
17

(iii) of our result also has the same conclusion as Cohen and Zhang (2022), who in the context
of ride-sharing services (e.g., Uber and Lyft), show that under collusion, riders pay a larger price
and workers receive a lower wage than under competition (note that the wage in their model is a
negative price in our model). Nevertheless, Cohen and Zhang (2022) assume a different model for
the user’s utility function, which is tailored for their specific setting of prices and wages.
5 The Effects of Increasing Competition on the CNE
We study how increasing competition (i.e., increasingN) affects four CNE quantities: price, market
participation, consumer surplus, and profit. We first establish sufficient conditions for the deriva-
tive ∂ p∗ k/∂N to be either positive or negative (see Proposition 5.1). We thus specify regions where
competition can lead to increasing or decreasing prices. We also establish sufficient conditions
for ∂ (Nx∗ k)/∂N to be positive and consequently for increasing market participation under com-
petition (see Proposition 5.2). We further formulate sufficient conditions to have increasing and
decreasing consumer surplus, i.e., to have positive and negative ∂ (CS∗ k)/∂N (see Proposition 5.3).
Finally, we establish sufficient conditions for the derivative ∂ π∗ k /∂N to be either positive or nega-
tive (see Proposition 5.4). That is, we specify regions where competition can lead to increasing or
decreasing profits on side k of the market.
The effect of competition on prices. We study the sign of ∂ p∗ k/∂N. We first clarify the
difficulty in estimating the latter derivative. In view of (17), the equilibrium vector price is p∗ =
H(z∗)Ω(z∗). As shown in (14) and (16), the matrix H and the vector Ω directly depend on N.
However, (13) and the definitions of H and Ω imply that z∗ is an implicit function of N. It is
thus hard to determine the sign of ∂ p∗ k/∂N. Nevertheless, when the cross-side externalities are
sufficiently small, the following proposition establishes sufficient conditions to determine the sign
of ∂ p∗ k/∂N. It uses the functions gp(N) and fp (N) defined in (177) and (183), respectively, of
Appendix A. We note that gp(N) and fp (N) approach 0 and 1, respectively, as N → ∞.
Proposition 5.1 (Regions where competition decreases/increases prices). The effect of competition
on the change of prices can be clustered into the following two regions:
(i) Assume that N ≥ 2 and either (φkk ≤ 0 and βk > gp(N)φkk) or (φkk > 0 and βk > φkk). Then,
there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), ∂ p∗ k/∂N < 0.
(ii) Assume that N ≥ 3, φkk > 0 and f (N) φkk < βk < fp (N) φkk. Then, there exists ε > 0 such
that for any (φbs, φsb) ∈ Bε (0), ∂ p∗ k/∂N > 0.
The first part of Proposition 5.1 agrees with traditional results, where a sufficiently large user’s
heterogeneity in tastes implies the decrease of the equilibrium prices with the increase of com-
petition, i.e., ∂ p∗ k/∂N < 0 (see Anderson and De Palma (1992)). On the other hand, the second
part of Proposition 5.1 agrees with a recent and less conventional result, where positivity of the
within-side externalities, φkk, and sufficiently small user’s heterogeneity in tastes, βk imply the
increase of prices with the increase of competition, i.e., ∂ p∗ k/∂N > 0 (see, Tan and Zhou (2021)).
The proposition carefully quantifies the thresholds on the user’s heterogeneity in tastes that yield
different signs of ∂ p∗ k/∂N. The resulting regions are demonstrated below in Figure 5 for N = 4.
The two regions are subsets of the region specified in (19) and whenN → ∞ the union of the former
two regions approaches the latter region (because gp(N) → 0 and fp(N) → 1 as N → ∞).
18

Figure 5: Classification of the sign of ∂ p∗ k/∂N based on (φkk, βk), k ∈ {b,s}, according to Propo-
sition 5.1, where N = 4. The red and blue regions correspond to negative and positive ∂ p∗ k/∂N,
respectively.
The effect of competition on market participation. The equilibrium market participation on
side k of the market is given byNx∗ k, where x∗ k is given by (16). The following proposition provides
sufficient conditions for positive ∂ (Nx∗ k)/∂N. It uses the following quantity:
gx(N) :=

2N2 − 2N + 1 
N (N2 − N + 1) . (33)
Proposition 5.2 (Competition increases market participation). If N ≥ 2 and
either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > gx(N)φkk),
then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), ∂ (Nx∗ k)/∂N > 0.
Most models of platform competition leave out the analysis of the outside utility option. By
doing so, they assume full market coverage, 17 and thus cannot study the effect of competition
on market participation. Proposition 5.2 fills this gap and its region of positive ∂ (Nx∗ k)/∂N is
demonstrated below in Figure 6 when N = 4. We note that the region described by Proposition
5.1 part (ii) intersects with the region described by Proposition 5.2. Thus, when the within-side
externalities are sufficiently large (relative to the user’s heterogeneity in tastes) then both prices
and market participation increase with competition. At last, we note that the region described by
Proposition 5.2 is a subset of the region described by (19) and they coincide as N → ∞.
17Corollary 4.3 shows that full market coverage occurs when N → ∞, however, when the number of platforms is
finite, we find this assumption unrealistic.
19

Figure 6: Demonstration of the region of positive ∂ (Nx∗ k)/∂N based on (φkk, βk), k ∈ {b,s} (in
blue), according to Proposition 5.2, where N = 4.
The effect of competition on consumer surplus. The equilibrium consumer surplus on side
k of the market, CS∗ k, is defined above in (30). The following proposition provides sufficient
conditions to determine the sign of ∂ (CS∗ k)/∂N. It uses the following quantities:
gCS (N) := 2N3 − N + 1 N2 (N2 − N + 2) (34)
and fCS (N) which is given by (205) in Appendix A.
Proposition 5.3 (Regions where competition decreases/increases consumer surplus). The effect of
competition on the change of consumer surplus can be clustered into the following two regions:
(i) If N ≥ 2 and either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > gCS (N) φkk), then there exists
ε > 0 such that for any (φbs, φsb) ∈ Bε (0), ∂ (CS∗ k)/∂N > 0.
(ii) If N ≥ 7, φkk > 0, f (N) φkk < βk < min

fCS (N) φkk, γ

N, φkk,u0 k 	 and z ∗ k < 1 5 ln2, then
there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), ∂ (CS∗ k)/∂N < 0.
Part (i) of Proposition 5.3 agrees with traditional results, where consumer surplus increases
with increased competition. For example, Hsu and Wang (2005) consider the Bertrand competition
model with substitute goods and show that competition increases consumer surplus. The region
in part (i) of Proposition 5.3 has small cross-side externalities and its within-side externalities
are either negative or positive and small with respect to the user’s taste heterogeneity. Part (ii),
on the other hand, shows sufficient conditions for decreasing consumer surplus with increased
competition. This result agrees with a result from Tan and Zhou (2021), where in markets that are
relatively concentrated with a few platforms, consumer surplus decreases as competition increases.
Moreover, in the asymptotic regime asN goes to infinity, the region in part (ii) disappears (because
gCS(N) → 0 and fCS(N) → 0 as N → ∞) and such behavior is also observed in Tan and Zhou (2021).
Note that the region in Part (ii) of Proposition 5.3 has positive within-side externalities, small user’s
heterogeneity in tastes relative to the within-side externalities, positive but small normalized net
deterministic utility relative to the number of platforms, and small cross-side externalities. Figure 7
demonstrates the resulting regions (i) and (ii) whenN = 4, while excluding the condition involving
z∗ k.
20

Figure 7: Classification of the sign of ∂ (CS∗ k)/∂N based on (φkk, βk), k ∈ {b,s}, for N = 4 and
u0 k = 0. The blue and red regions correspond to positive and negative ∂ (CS∗ k)/∂N, respectively.
For the red region we did not include the bound on z∗ k, but we still demonstrate a restricted region.
The effect of competition on profits. The equilibrium profit quantity, π ∗, is given by
π ∗ := ∑
k∈{b,s}
p∗ kx∗ k. (35)
For each k ∈ {b,s}, let π ∗ k := p∗ kx∗ k, the profits on side k of the market. The following proposition
provides sufficient conditions to determine the sign of ∂ π∗ k /∂N. It uses the following condition:
either (φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > gπ (N) φkk) , (36)
where gπ (N) > f (N), f (N) is given by (18) and gπ (N) is given by (221) in Appendix A. It
also uses the functions gπ,z(N, φkk,u0 k, βk) and fπ,z(N, φkk,u0 k, βk) defined in (218) and (219) of
Appendix A, respectively.
Proposition 5.4 (Regions where competition decreases/increases profits on side k). Assume that
N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies (19). The effect of competition on the change of
profits on side k of the market can be clustered into the following two regions of z∗ k:
(i) If z ∗ k < gπ,z(N, φkk,u0 k, βk), then there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0),
∂ π∗ k /∂N < 0.
(ii) If z ∗ k > fπ,z  N, φkk,u0 k, βk  and (36) is satisfied, then there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0), ∂ π∗ k /∂N > 0.
Part (i) of Proposition 5.4 shows that in markets where the normalized net deterministic utility
from joining the market is relatively small, the increased competition decreases profits. In other
words, when the incentive to join the market in equilibrium, z∗ k, is small enough, more platforms
joining the market reduce the pie for all of the competing platforms. A more interesting result
appears in part (ii) when the incentives to join the market are high enough (relatively large z∗ k) and
thus the increased competition increases profits. This observation aligns with traditional results in
the platform’s literature (see Tan and Zhou (2021)) where the effect of network externalities can
reverse the usual link between competition and firm profit (i.e., profits can increase with competi-
tion).
21

6 Economic and Policy discussion
We examine the economic implications of some of the results presented in Sections 4 and 5. We
first discuss how increases in outside option utility and competition influence equilibrium prices
and consumer surplus. These findings may inform policy discussions aimed at improving con-
sumer outcomes and market efficiency. We also interpret our mathematical result comparing col-
lusion and competition under small cross-side externalities. For concreteness, we focus on the
dating app market, as motivated in the introduction.
Scenarios in which an increased outside option or greater competition leads to lower
prices and higher consumer surplus: Both parts (i) of Propositions 4.4 and 4.7 suggest that,
under some conditions, such as relatively high heterogeneity, increasing the value of the outside
option decreases prices and increases consumer surplus. In the setting of popular dating apps
that attract a heterogeneous population—such as Tinder, Bumble, and Hinge—increased prefer-
ence for traditional partner-finding methods leads to the reduction of dating app prices and the
increase in consumer surplus. This suggests that apps should adjust pricing strategies, possibly by
reducing prices or enhancing sign-up services. Similarly, both parts (i) of Propositions 5.1 and 5.3
imply that, under some conditions, such as relatively high heterogeneity, increasing competition
decreases prices and increases consumer surplus. This finding is well-known in the traditional
single-sided competition literature (see, e.g., Tirole (1988) and Anderson and De Palma (1992)).
In summary, under certain conditions—particularly high heterogeneity—our findings suggest two
regulatory mechanisms to decrease prices and increase consumer surplus: enhancing the value of
outside options or incentivizing competition.
Scenarios in which an increased outside option or greater competition leads to higher
prices and lower consumer surplus: Both parts (ii) of Propositions 4.4 and 4.7 suggest that un-
der different conditions, such as relatively low heterogeneity, an increased outside option raises
prices and reduces consumer surplus. These results may be exemplified by dating apps that tar-
get specific demographics or niches where users are often homogeneous in their preferences. For
example, apps like The League and JDate target more homogeneous segments of the population,
and consequently, they can charge higher prices. Therefore, in these apps, users are less sensitive
to outside options. Moreover, if subscribers are loyal at a sufficiently high outside option utility,
there is no incentive to reduce prices even when this utility increases. Similarly, both parts (ii) of
Propositions 5.1 and 5.3 imply that, under some conditions, such as relatively low heterogeneity,
increasing competition leads to higher prices and lower consumer surplus. The intuition follows
from (30). We first note from this equation that consumer surplus is inversely related to price, so we
focus on the former. Additionally, we observe that, for a fixed price, consumer surplus increases
with (i) the expected maximum user idiosyncrasy, and (ii) the size of the network externalities.
In homogeneous populations, the expected maximum user idiosyncrasy is relatively small, which
makes network externalities more pronounced. In this scenario, fewer platforms can amplify net-
work effects more effectively (e.g., instead of having many alternatives to The League or JDate),
making them more attractive. As a result, even with increased competition or a higher outside
option, users may gravitate toward a smaller number of large platforms to maximize the benefits of
network externalities. This dynamic allows these platforms to maintain or increase prices, while
consumer surplus remain stagnant or decreases.
Population heterogeneity matters for policy: The discussion above suggests that in markets
like those described in this paper, regulators should carefully assess the level of population hetero-
22

geneity when aiming to improve consumer surplus and reduce equilibrium prices. This is because
the same policy can have varying effects depending on the degree of heterogeneity. Specifically,
when population heterogeneity is sufficiently high, policies that either promote competition (e.g.,
reducing entry barriers and enforcing antitrust laws) or improve the outside option (e.g., enhanc-
ing public spaces like parks, libraries, and cultural centers) tend to lower equilibrium prices and
increase consumer surplus. Conversely, when population heterogeneity is sufficiently low, poli-
cies that limit competition (e.g., supporting a dominant platform) or restrict the outside option
(e.g., subsidizing part of the cost for some consumers) can help maintain or reduce prices while
preserving or increasing consumer surplus.
Collusion under small cross-side externalities: Proposition 4.11 shows that in cases of small
cross-side externalities, collusion (in comparison to competition) results in decreased normalized
net deterministic utilities, reduced market participation and increased price, on both sides of the
market. This is intuitive since when the cross-side externalities are sufficiently small—meaning
users derive limited benefit from the presence of users on the opposite side—competing platforms
have strong incentives to lower prices and attract users. In contrast, colluding platforms internalize
each other’s pricing decisions and reduce competition, enabling them to raise prices on both sides.
This further results in higher net deterministic utilities and greater overall participation for the
competition case versus the colluding one. The collusive outcome resembles classic monopoly
pricing: platforms extract more surplus at the expense of user welfare, resulting in higher prices
and lower market participation compared to the competitive case. In the dating app market, cross-
side externalities capture the value one side (e.g., men) derives from a larger presence of the other
side (e.g., women) on a given platform. These externalities are typically lower in large-scale
casual apps like Tinder, Badoo, and Facebook Dating, where user pools are already extensive
and the marginal value of new users is diminished. While Proposition 4.11 is difficult to verify
empirically, we illustrate its logic with a speculative example. During the 2013-2017 period of
increasing competition among casual dating apps like Tinder, OkCupid, and Plenty of Fish (POF),
prices were lower, user utility was higher, and market participation was larger. In contrast, we
hypothesize that the dating app market has shifted in recent years toward reduced competition and
arguably increased collusion. Match Group has gained a dominant position through acquisitions of
major platforms such as Tinder, POF, OkCupid and Hinge (Gilbert, 2019). In parallel, the adoption
of AI-based pricing strategies raises questions about the potential for tacit coordination (Chica
et al., 2024). During this period, rising prices have become evident. Moreover, features that were
once free are increasingly placed behind paywalls. This results in lower utility for price-sensitive
users and may limit participation, despite overall market growth.
Lastly, we note that the impact of increasing or decreasing competition appears both in Propo-
sition 4.11, where competition is compared to collusion in an extreme case, and in Propositions 5.1
and 5.3, where competition changes by either increasing or decreasing the number of platforms in
the market.
7 Conclusions
We provided a realistic framework for platform competition and collusion with an outside option.
Among our many results, we highlight the following key findings:
1. When the cross-side externalities are sufficiently small, the normalized net deterministic
23

utilities and market participation are smaller in collusion than competition, and the prices on
both sides of the market are higher in collusion than competition.
2. Depending on the size of the user’s heterogeneity in tastes, incorporating an outside option
may increase or decrease the equilibrium price and consumer surplus w.r.t. the no outside
option model. In particular, a model of platform competition that omits the outside option
will either overestimate or underestimate the true equilibrium price.
3. Depending on the size of the user’s heterogeneity in tastes, the number of platforms and the
size of network externalities, we also demonstrated when different quantities either decrease
or increase with increased competition.18
While the paper uses lengthy mathematical derivation, a basic and fundamental idea is demon-
strated in (32). This equation decomposes the price gap between collusion and competition into
two forces: reduced network benefits from lower participation, and lower user utility under collu-
sion. Together, these explain why prices are higher in the collusive regime.
There are many open directions for future research. In particular, it would be interesting to
extend our model to incorporate the following features: (i) a multi-homing option, i.e., allowing
users to join more than one platform; and (ii) platform asymmetries, i.e., allowing for different
marginal costs of serving users. Incorporating multi-homing would require introducing an addi-
tional decision margin for users, potentially following the frameworks in Chica et al. (2021) or
Teh et al. (2023). For the case of platform asymmetries, one could modify problems (4) and (5)
by introducing a marginal cost ci > 0 for each platform i ∈ {1, . . . ,n}. Exploring these extensions
would likely require a combination of numerical methods and further simplifying assumptions.
We view these as promising directions for future work that can build on the foundation laid by
the present analysis. Another direction we are currently exploring is the use of our models as an
economic framework for analyzing how reinforcement learning algorithms for platform pricing
affect equilibrium outcomes. Our models help us assess whether network externalities mitigate or
exacerbate the degree of collusion that AI-driven platforms may achieve (Chica et al., 2024).
18In particular, when the number of platforms increases, prices decrease if the user’s heterogeneity is relatively large
compared to the within-side externalities, and increase if there are at least three platforms and the user’s heterogeneity
is relatively small compared to the within-side externalities; market participation always increases; consumer surplus
increases if the user’s heterogeneity is relatively large compared to the within-side externalities, and decreases if there
are at least three platforms, the user’s heterogeneity is relatively small compared to the within-side externalities, and
the net deterministic utility is small relative to the number of platforms; and profits decrease if the net normalized
deterministic utility is small enough and increase if the net normalized deterministic utility is large enough.
24

A Appendix
We prove all the stated results in the following order: Proposition 3.1, Proposition 3.2 (for which
we first provide various definitions and establish Lemma A.1), Proposition 3.3 (for which we first
prove Lemma A.2), Proposition 3.4 (for which we first prove Lemma A.3), Proposition 3.5 (for
which we first prove Lemma A.4), Proposition 4.1, Corollary 4.2, Corollary 4.3, Proposition 4.4,
Proposition 4.6, Proposition 4.7, Proposition 4.8, Corollary 4.9, Corollary 4.10, Proposition 4.11,
Proposition 5.1, Proposition 5.2, Proposition 5.3 and Proposition 5.4. In order to save space, we
leave some of the lengthy calculations to Mathematica and report them in the supplementary file
Gumbel N.nb.
Proof of Proposition 3.1. Let {(pi b, pi s)}N i=1 ⊂ R2 be a set of prices. For i ∈ N ∪ {0} and k ∈
{b,s}, set vi k := ˆui k − εi k. From (1) and (2), for i, j ∈ N ∪ {0}, i ̸= j, (3) can be rewritten as
xi k = P( ˆui k > max j̸=i ( ˆu j k))
= P(εi k > max j̸=i (ε j k + v j k − vi k)), k ∈ {b,s}. (37)
For i ∈ N ∪ {0} and k ∈ {b,s}, we define T i k : RN+1 − →[0,1] such that
u = (u0,u1, · · ·,uN) 7→ T i k (u) := P(εi k > max j̸=i (ε j k + u j − ui) | {z }
:=Ei k(u)
).
Note that Ei k(u) ⊂ Ω (where Ω is the domain of the random variables {εi k}i∈N ∪{0},k∈{b,s}). In two
steps, we show that for any u ∈ RN+1 and k ∈ {b,s}, ∑N i=0 T i k (u) =1.
Step (i): For any i ̸= j, the events Ei k(u) and E j k (u) are disjoint because either εi k > ε j k +u j −ui
or ε j k > εi k + ui − u j, but not both. Then, ∑N i=0 T i k (u) =P  ∪N i=0Ei k  .
Step (ii): We show that P

∩N i=0(Ei k)c = 0. First, note that the sets {Ei k ∩ (Ei k)c}i∈N ∪{0},k∈{b,s}
have P-zero probability, because P is absolutely continuous with respect to the Lebesgue measure
and each of the sets Ei k ∩ (Ei k)c is contained inside an N-dimensional set of RN+1. We claim that
∩N i=0(Ei k)c ⊆ ∪N i=0(Ei k ∩ (Ei k)c). Let ω ∈ ∩N i=0(Ei k)c. Then, for all i ∈ N ∪ {0},
εi k ≤ max j̸=i (ε j k + u j − ui). (38)
If there exists i ∈ N ∪ {0} such that (38) holds with equality, then ω ∈ Ei k ∩ (Ei k)c and the claim
holds true. Now we prove that if for alli ∈ N ∪ {0}, (38) is satisfied with strict inequality, we get a
contradiction. By (38) with strict inequality, there existsθ (0) ∈ N ∪ {0}, θ (0) ̸= 0 such that ε0 k <
ε θ (0) k + uθ (0) − u0. Similarly, there exists θ 2(0) ̸= θ (0) such that ε θ (0) k < ε θ 2(0) k + uθ 2(0) − uθ (0).
Note that θ 2(0) ̸= 0, otherwise, ε θ (0) k < ε0 k + u0 − uθ (0) which contradicts the definition of θ (0).
By induction, suppose that for n ∈ N and all 0 ≤ m ≤ n, there exists θ m(0) ∈ N ∪ {0} such that
θ m(0) /∈ {0, θ (0), · · ·, θ m−1(0)} and ε θ m−1(0) k < ε θ m(0) k + uθ m(0) − uθ m−1(0). (39)
25

By (38) with strict inequality, there existsθ n+1(0) ∈ N ∪ {0}, θ n+1(0) ̸= θ n(0) such that ε θ n(0) k <
ε θ n+1(0) k + uθ n+1(0) − uθ n(0). We claim that θ n+1(0) /∈ {0, θ (0), · · ·, θ n(0)}, otherwise θ n+1(0) =
θ m(0) for some 0 ≤ m ≤ n − 1. In this case, by (39)
ε θ n+1(0) k = ε θ m(0) k < ε θ m+1(0) k + uθ m+1(0) − uθ m(0)
< ε θ m+2(0) k + uθ m+2(0) − uθ m+1(0) + uθ m+1(0) − uθ m(0)
...
< ε θ n(0) k + uθ n(0) − uθ m(0).
(40)
Note that (40) contradicts the definition ofθ n+1(0). Then θ n+1(0) /∈ {0, θ (0), · · ·, θ n(0)} and (39)
is satisfied for the next indexn +1. It follows that (39) holds for anyn ∈ N. The latter is impossible
because there are onlyN +1 different indices insideN ∪ {0}. Thus, ∩N i=0(Ei k)c ⊆ ∪N i=0(Ei k ∩ (Ei k)c)
and P

∩N i=0(Ei k)c = 0.
Combining steps (i) and (ii), we get that for any u ∈ RN+1 and k ∈ {b,s}, ∑2 i=0 T i k (u) =1.
Now, for x = (x0b,x0s,x1b,x1s, . . . ,xNb,xNs) ∈ [0,1]2(N+1) and each i ∈ N ∪ {0}, we introduce the
auxiliary functions φ i k(x) defined as
φ i k(x) =
(
φ 0 k if i = 0
φk(xib,xis) if i ≥ 1 .
Similarly, we define
σ i k(x) := T i k (v0 k(x), · · ·,vN k (x)),
where v j k(x) =φ j k (x) − p j k (p0 k = 0). If Σ : [0,1]2(N+1) − →[0,1]2(N+1) is defined by
Σ(x) = (σ 0 b (x), σ 0 s (x) · · ·, σ N b (x), σ N s (x)),
then solving system (3) is equivalent to finding a fixed point ofΣ, i.e., Σ(x) =x. Existence of such
a fixed-point is guaranteed by Brouwer’s Fixed Point Theorem, as Σ is continuous on [0,1]2(N+1).
For such a fixed point: ∑N i=0 xi k = ∑N i=0 σ i k(x) =∑N i=0 T i k (v0 k(x), · · ·,vN k (x)) =1.
To show the uniqueness of the solution of (3), we use the Banach Fixed Point Theorem. Let
x, y ∈ [0,1]2(N+1), then
|σ i k(x) − σ i k(y)| = |T i k (v0 k(x), · · ·,vN k (x)) − T i k (v0 k(y), · · ·,vN k (y))|
≤ max
j
|v j k(x) − v j k(y)| ·

sup
u∈RN+1
N
∑
l=0

 ∂T i k (u) ∂ul

 !
≤ max
j
|φ j k (x) − φ j k (y)| ·MT
≤ Mφ MT |x − y|∞,
where
MT := max k∈{b,s},i∈N ∪{0} sup u∈RN+1
N
∑
l=0

 ∂T i k (u) ∂ul

 , and
Mφ := max k∈{b,s} sup (xb,xs)∈[0,1]2 ∑ l∈{b,s}

 ∂ φk(xb,xs) ∂xl

 .
26

It follows that Σ(·) is a (strict) contracting mapping whenever MT Mφ < 1, and uniqueness
follows.
Preliminary results for the proof of Proposition 3.2. We introduce notation and definitions
and establish a useful lemma. Let X =

x1 b, · · ·,xN b ,x1 s , · · ·,xN s  and P =  p1 b, · · ·, pN b , p1 s , · · ·, pN s 
be two vectors in R2N. For k ∈ {b,s}, let ˜uk := (u0 k,u1 k, . . . ,uN k ), where ui k = φk  xi b,xi s  − pi k. Using
(9), we can define a mapping from R4N to R2N as
(X, P ) 7→ T (X, P ) :=

T 1 b ( ˜ub) − x1 b, · · ·,T N b ( ˜ub) − xN b ,T 1 s ( ˜us) − x1 s , · · ·,T N s ( ˜us) − xN s  . (41)
The Jacobian of (9) w.r.t. P is defined as
det∂ T ∂ P (X, P ) := Qb (X, P )Qs (X, P ) , where
Qk (X, P ) :=

 − ∂T 1 k ∂u1 ( ˜uk) . . . − ∂T 1 k ∂uN ( ˜uk) ... ... ... − ∂T N k ∂u1 ( ˜uk) . . . − ∂T N k ∂uN ( ˜uk)

 . (42)
Under symmetry, for any i ∈ N and k ∈ {b,s}, we write pi k = pk, xi k = xk, and ui k = uk :=
φk(xb,xs) − pk. Let uk := (u0 k, φk(xb,xs) − pk, · · ·, φk(xb,xs) − pk)T ∈ RN+1. For i, j ∈ N , i ̸= j,
k ∈ {b,s}, we define the functions
Sk(uk) := ∂T i k ∂ui k (uk),
Rk(uk) := ∂T i k
∂u j k (uk),
Jk(uk) := Sk(uk) (Sk(uk) + (N − 2)Rk(uk)) − (N − 1)Rk(uk)2, and
Jφ (ub, us) :=
∂ φs
∂xs
− 1 Js(us)Ss(us)  ∂ φb ∂xb − 1 Jb(ub)Sb(ub)  − ∂ φs ∂xb ∂ φb ∂xs .
(43)
Whenever there is no room for confusion, we simplify the notations by neglecting the explicit
mention of the inputuk. For example, T i k (uk), Sk(uk), Rk(uk), Jk(uk) and Jφ (ub, us) are simplified
to T i k, Sk, Rk, Jk and Jφ respectively. The following Lemma shows the first-order condition of (4)
as a function of xk.
Lemma A.1 (FOC of CNE). If det ∂ T ∂ P (x∗, p∗) ̸= 0, then the symmetric Nash equilibrium outputs
p∗ and x∗ are solutions of (3) and of the following two equations
pk + ∂ φk ∂xk xk + ∂ φl ∂xk xl − 1 Jk (Sk + (N − 2)Rk)xk + 1 J2 k JlJφ (N − 1)R2 kSlxk
+ N − 1 JkJφ Rk
 1
Jl
Rl
∂ φl
∂xk
xl − 1 Jk Rk ∂ φl ∂xl xk

= 0, for k,l ∈ {b,s}, k ̸= l.
(44)
27

The proof of this Lemma does not require assumptions I and II of Section 2. Thus, the FOC
given by (44) is applicable to idiosyncratic preferences other than Gumbel distribution and to more
general externality functions φk(x).
Proof of Lemma A.1. Assume that all platforms follow a symmetric equilibrium where pi = p∗ =
(p∗ b, p∗ s ) and xi = x∗ = (x∗ b,x∗ s ). We show that unilateral deviations from this strategy lead to zero
gain. Without loss of generality, we assume that the first platform deviates from the symmetric
setting. This platform can deviate by either choosing prices p1 k ̸= p∗ k or market shares x1 k ̸= x∗ k.
Suppose that det ∂ T ∂ P (X ∗, P ∗) ̸= 0, where
X ∗ = (x∗ b, · · ·,x∗ b,x∗ s , · · ·,x∗ s ) and P ∗ = (p∗ b, · · ·, p∗ b, p∗ s , · · ·, p∗ s )
belong to R2N. Then, by the Implicit Function Theorem, there exists a neighborhood B of X ∗ in
R2N and a unique differentiable function P : B − →R2N such that P (X ∗) =P ∗ and
T (X, P (X)) =0 for all X ∈ B. (45)
From (4) and (45), we can compute the FOC for this platform w.r.t. x1 k as
∂ π1
∂x1 k

pi=p∗,xi=x∗, for i̸=1 = p1 k + x1 k ∂ p1 k ∂x1 k + x1 l ∂ p1 l ∂x1 k = 0, for each k,l ∈ {b,s}, k ̸= l. (46)
To solve (46), we need to compute the following derivatives
∂ p1 k
∂x1 l , for each k,l ∈ {b,s}. (47)
We determine those four partial derivatives ∂ p1 ∂ x1 in (47) using the definition of Tk in (8). By (9), for
k ∈ {b,s}, the vectors of market shares and prices, (x1 k,x∗ k, . . . ,x∗ k) and (p1 k, p∗ k, . . . ,p∗ k) satisfy all
the following
T 1 k (u0 k,u1 k,u2 k, . . . ,uN k ) =x1 k and (48)
T i k (u0 k,u1 k,u2 k, . . . ,uN k ) =xi k, for i ∈ {2,3, · · ·,N}. (49)
Taking derivatives w.r.t.x1 b and x1 s in (48) and (49), respectively, gives us
∂T 1 k (u0 k,u1 k,u2 k, . . . ,uN k )
∂x1 l = δkl and (50)
∂T i k (u0 k,u1 k,u2 k, . . . ,uN k )
∂x1 l = ∂xi k ∂x1 l , for i ∈ {2,3, · · ·,N}, k,l ∈ {b,s}, (51)
where δkl = 1 if k = l and δkl = 0 if k ̸= l. Note that the system of equations in(50) and (51) includes
4 +4(N −1) =4N equations. The unknowns are ∂ p1 k ∂x1 l and ∂xi k ∂x1 l , for k,l ∈ {b,s} and i ∈ {2,3, . . . ,N}, adding up to 4N unknowns.
28

Note that u0 k is a constant and it does not depend on x1 k. By the chain rule, the left hand side of
(50) and (51) can be rewritten as
∂T j k (u0 k,u1 k,u2 k, . . . ,uN k )
∂u1
∂u1 k
∂x1 l +
N
∑
i=2
∂T j k (u0 k,u1 k,u2 k, . . . ,uN k )
∂ui
∂ui k
∂x1 l , for k,l ∈ {b,s}, j ∈ {1,2, . . . ,N}.
(52)
Recall that u1 k = φk(x1) − p1 k, then, we can explicitly write
∂u1 k
∂x1 l = −∂ p1 k ∂x1 l + ∂ φk ∂xl , for k,l ∈ {b,s}. (53)
On the other hand, for i ∈ {2,3, · · ·,N}, ui k = φk(xi) − p∗ k. Thus,
∂ui k
∂x1 l = ∂ φk ∂xb ∂xi b ∂x1 l + ∂ φk ∂xs ∂xi s ∂x1 l , for k,l ∈ {b,s}, i ∈ {2, . . . ,N}. (54)
Plugging (52), (53) and (54) into (50) and (51), we obtain for k,l ∈ {b,s} and j ∈ {2,3, · · ·,N},
∂T 1 k
∂u1

−∂ p1 k
∂x1 l + ∂ φk ∂xl

+
N
∑
i=2
∂T 1 k
∂ui
 ∂ φk
∂xb
∂xi b
∂x1 l + ∂ φk ∂xs ∂xi s ∂x1 l  = δkl, (55)
∂T j k
∂u1

− ∂ p1 k
∂x1 l + ∂ φk ∂xl

+
N
∑
i=2
∂T j k
∂ui
 ∂ φk
∂xb
∂xi b
∂x1 l + ∂ φk ∂xs ∂xi s ∂x1 l  = ∂x j k ∂x1 l , (56)
There are 4N equations with 4N variables in the above system. Before solving the system, we
want to apply the property of symmetry at equilibrium, where we denote
∂x j k
∂x1 l =: yk,l, for j ∈ {2,3, · · ·,N} and
∂T i k
∂u j
=:
 Sk i = j
Rk i ̸= j , for i, j ∈ {1, . . . ,N}.
(57)
Incorporating (57), we can further reduce the system described by (55) and (56) into 8 equations
with unknowns: ∂ p1 k ∂x1 l and yk,l, for k,l ∈ {b,s}. The new system is, for k,l ∈ {b,s},
Sk

− ∂ p1 k
∂x1 l + ∂ φk ∂xl

+ (N − 1)Rk
 ∂ φk
∂xb
yb,l + ∂ φk ∂xs ys,l

= δkl and (58)
Rk

− ∂ p1 k
∂x1 l + ∂ φk ∂xl

+ (Sk + (N − 2)Rk)
 ∂ φk
∂xb
yb,l + ∂ φk ∂xs ys,l

= yk,l. (59)
To solve the above equations, we notice that there are two groups of equations: (A) four equa-
tions associated to derivatives w.r.t.x1 b; (B) four equations associated to derivatives w.r.t.x1 s . Thus,
we solve two linear systems, each one containing four equations and four unknowns.
29

Using (43), we conclude that when Jk ̸= 0 for any k ∈ {b,s} and Jφ ̸= 0,
yb,b = − 1 JbJφ Rb
 ∂ φs
∂xs
− Ss
Js

, (60)
ys,b = 1 JbJφ Rb ∂ φs ∂xb , (61)
yb,s = 1 JsJφ Rs ∂ φb ∂xs , and (62)
ys,s = − 1 JsJφ Rs
 ∂ φb
∂xb
− Sb
Jb

. (63)
Moreover, it follows that
∂ p1 b
∂x1 b = ∂ φb ∂xb − 1 Jb (Sb + (N − 2)Rb) +N − 1 Jb Rb

− 1 JbJφ Rb
∂ φs
∂xs
− 1 Js Ss

, (64)
∂ p1 s
∂x1 b = ∂ φs ∂xb + N − 1 Js Rs
 1
JbJφ
Rb
∂ φs
∂xb

, (65)
∂ p1 b
∂x1s = ∂ φb ∂xs + N − 1 Jb Rb
 1
JsJφ
Rs
∂ φb
∂xs

, and (66)
∂ p1 s
∂x1s = ∂ φs ∂xs − 1 Js (Ss + (N − 2)Rs) +N − 1 Js Rs

− 1 JsJφ Rs
 ∂ φb
∂xb
− 1 Jb Sb

. (67)
Finally, we can plug in (64), (66), (65) and (67) into the FOC (46) to obtain
pk + ∂ φk ∂xk xk + ∂ φl ∂xk xl − 1 Jk (Sk + (N − 2)Rk)xk + 1 J2 k JlJφ (N − 1)R2 kSlxk
+ N − 1 JkJφ Rk
 1
Jl
Rl
∂ φl
∂xk
xl − 1 Jk Rk ∂ φl ∂xl xk

= 0, for k,l ∈ {b,s}, k ̸= l.
(68)
Lemma A.1 is general enough to accommodate idiosyncratic preferences other than Gumbel
distribution and general externality functions φk(x). Next, we use Assumptions I and II from
Section 2 and Lemma A.1 to prove Proposition 3.2.
Proof of Proposition 3.2. We want to rewrite the FOC given by (44) using Assumptions I and II
from Section 2. Applying Gumbel distribution, we can derive specific forms for the functions T i k,
Sk, and Rk as defined in (43). By Assumption I, {εi k}k∈{b,s},i∈N ∪{0} are i.i.d. Gumbel distributed
with distribution
Fk(z) =e−e
µk−z
βk
. (69)
For any i ∈ N , the random variable Y i := εi k + ui k − max j=0,1,...,N, j̸=i
n
ε j k + u j k
o
has a logistic
distribution,
30

Y i ∼ Logistic(ui k − βk ln αi, βk), where αi := ∑
j=0,1,...,N, j̸=i
e
u j k
βk .
By (8), we can explicitly write T i k as follows
T i k (u0 k,u1 k, . . . ,uN k ) =P

εi k + ui k ≥ max j=0,1,...N, j̸=i
n
ε j k + u j k
o
= 1 − FY i(0) =1 − 1 1 + e(ui k−βk ln(αi))/βk . (70)
The derivatives of T i k can be calculated as
∂T i k (u0 k,u1 k, . . . ,uN k )
∂ui =
1
βk e(ui k−βk ln(αi))/βk

1 + e(ui k−βk ln(αi))/βk 2 and (71)
∂T i k (u0 k,u1 k, . . . ,uN k )
∂u j =
−e(ui k−βk ln(αi))/βk · 1 βk eu j k/βk αi

1 + e(ui k−βk ln(αi))/βk 2 , for j ̸= i. (72)
At a symmetric equilibrium, ui = u = (ub,us)T , for any i ∈ N . Then, we can further simplify
(70), (71) and (72),
T i k = euk/βk
eu0 k/βk + Neuk/βk , (73)
Sk = 1 βk euk/βk(eu0 k/βk + (N − 1)euk/βk)  eu0 k/βk + Neuk/βk 2 and (74)
Rk = − 1 βk e2uk/βk  eu0 k/βk + Neuk/βk 2 . (75)
Using (12), we derive the dependence of x and p on z under the symmetric setting as
xi k = T i k (u) = euk/βk
eu0 k/βk + Neuk/βk = 1 e(u0 k−uk)/βk + N = 1 e−zk + N =: ω(zk). (76)
Denoting Ω(z) := (ω(zb), ω(zs))T , we obtain x = Ω(z) in the symmetric equilibrium. Moreover,
we can write u − u0 = βz, u = Φx − p and
p = ΦΩ(z) − βz − u0. (77)
At this point, we want to use Lemma A.1 to rewrite (44) using Assumptions I and II. First, we
verify that det ∂ T ∂ P (X, P ) ̸= 0, see (42), for any pair of symmetric vectors
X = (xb, · · ·,xb,xs, · · ·,xs) and P = (pb, · · ·, pb, ps, · · ·, ps) .
31

Using (71), (72) and (12) into (42), we obtain
Qk (X, P ) =

 − ∂T 1 k ∂u1 . . . − ∂T 1 k ∂uN ... ... ... − ∂T N k ∂u1 . . . − ∂T N k ∂uN

= 1 β N k eNzk (1 + (N − 1)ezk)N (1 + Nezk)2N

 −1 ezk 1+(N−1)ezk . . . ezk 1+(N−1)ezk ... −1 ... ... ezk 1+(N−1)ezk ezk 1+(N−1)ezk . . . −1

= 1 β N k eNzk (−1)N (1 + Nezk)N+1 ̸= 0.
(78)
We can now apply Lemma A.1 and equations (73) to (77) into (44) to obtain
βz = (Φ − H(z)) Ω(z) − u0, (79)
where u0 = (u0 b,u0 s ), H(z) is a 2 × 2 matrix defined as
H(z) :=
LbdbKs + hb − φbb −φsb(dsLb + 1)
−φbs(dbLs + 1) LsdsKb + hs − φss

, (80)
and, for any k ∈ {b,s}, Lk, dk and hk are functions depending on zk as
Lk = (N − 1)βk Jφ (1 + Nezk),
dk = βk(1 + Nezk),
hk = βk(1 + ezk)(e−zk + N),
(81)
and Jφ is a function of zb and zs as
Kk = φkk − βk(1 + Nezk)(e−zk + N − 1), for k ∈ {b,s},
Jφ = KbKs − φsbφbs. (82)
Denoting z∗ to be the solution to (79) and using (76) and (77), we conclude the proposition by
noting that the symmetric equilibrium solution of (4) is given by x∗ = Ω(z∗) and p∗ = ΦΩ(z∗) −
βz ∗ − u0.
Preliminary results for the proof of Proposition 3.3. We introduce notation and definitions
and establish a useful lemma. Let j ∈ {1, · · ·,N}, k,l and m ∈ {b,s}, uk,l := ∂ φk ∂xb yb,l + ∂ φk ∂xs ys,l where yk,l is given by (57). Moreover,
U j k,lm := ∂ ∂x1m
"
∂T j k
∂u1
# 
−∂ p1 k
∂x1 l + ∂ φk ∂xl

+
N
∑
i=2
∂
∂x1m
"
∂T j k
∂ui
#
uk,l+
N
∑
i=2
∂T j k
∂ui
 ∂ 2φk
∂xm∂xb
∂xi b
∂x1 l + ∂ 2φk ∂xm∂xs ∂xi s ∂x1 l  , (83)
where the derivatives of T j k are evaluated at (u0 k,u1 k, · · ·,uN k ), u1 k := φk(x1) − p1 k and ui k := φk(xi) −
p∗ k for i ≥ 2. The following Lemma shows the second-order condition of (4) as a function of xk.
32

Lemma A.2 (SOC of CNE). The second-order condition of (4) is given by
D2 (x1 b,x1s )π1 =

 2 ∂ p1 b ∂x1 b + x1 b ∂ 2 p1 b ∂(x1 b) 2 + x1 s ∂ 2 p1s ∂(x1 b) 2  ∂ p1 b ∂x1s + ∂ p1s ∂x1 b  + x1 b ∂ 2 p1 b ∂x1s ∂x1 b + x1 s ∂ 2 p1s ∂x1s ∂x1 b ∂ p1s
∂x1 b + ∂ p1 b ∂x1s  + x1 b ∂ 2 p1 b ∂x1 b∂x1s + x1 s ∂ 2 p1s ∂x1 b∂x1s 2 ∂ p1s ∂x1s + x1 b ∂ 2 p1 b ∂(x1s ) 2 + x1 s ∂ 2 p1s ∂(x1s ) 2

 , (84)
where for k,m and l ∈ {b,s}, ∂ p1 k ∂x1 l is given by (64)-(67),
∂ 2p1 k
∂x1m∂x1 l = ∂ 2φk ∂xm∂xl + 1 Jk  (Sk + (N − 2)Rk)U1 k,lm +  xk,ml −Uk,lm  (N − 1)Rk  , (85)
and Rk, Sk and Jk are given by (43). Moreover,
 xb,ml
xs,ml

= 1 Jφ



∂ φs
∂xs − 1 Js Ss

− ∂ φb ∂xs
− ∂ φs ∂xb

∂ φb
∂xb − 1 Jb Sb





1
Jb

RbU1 b,lm − SbUb,lm

1
Js

RsU1 s,lm − SsUs,lm


 , (86)
where U1 k,lm and Uk,lm := U j k,lm for j ≥ 2 are given by (83).
The proof of this Lemma does not require assumptions I and II of Section 2. Thus, the SOC
given by (84) is applicable to idiosyncratic preferences other than Gumbel distribution and to more
general externality functions φk(x).
Proof of Lemma A.2. Differentiating the left-hand side of (46) w.r.t. x1 m, for m ∈ {b,s}, easily
yields (84). To obtain (85) and (86), we differentiate (55) and (56) w.r.t.x1 m. For m,k,l ∈ {b,s} and
j ∈ {2,3, · · ·,N}, we obtain
∂T 1 k
∂u1

− ∂ 2p1 k
∂x1m∂x1 l + ∂ 2φk ∂x1m∂xl  + N ∑ i=2 ∂T 1 k ∂ui  ∂ φk ∂xb ∂ 2xi b ∂x1m∂x1 l + ∂ φk ∂xs ∂ 2xi s ∂x1m∂x1 l ! +U1 k,lm = 0, (87)
∂T j k
∂u1

− ∂ 2p1 k
∂x1m∂x1 l + ∂ 2φk ∂x1m∂xl  + N ∑ i=2 ∂T j k ∂ui  ∂ φk ∂xb ∂ 2xi b ∂x1m∂x1 l + ∂ φk ∂xs ∂ 2xi s ∂x1m∂x1 l ! +U j k,lm = ∂ 2x j k ∂x1m∂x1 l ,
(88)
where U1 k,lm and U j k,lm are given by (83). Note that the derivatives of T j k in (87) and (88), are
evaluated at (u0 k,u1 k, · · ·,uN k ), u1 k := φk(x1) − p1 k, where ui k := φk(xi) − p∗ k for i ≥ 2. The unknowns
are ∂ 2 p1 k ∂x1m∂x1 l and ∂ 2xi k ∂x1m∂x1 l for k,l,m ∈ {b,s} and i ∈ {2, . . . ,N}, adding up to 8 + 8(N − 1) =8N. Similarly, the number of equations in the system of equations described in (87) and (88) is 8N.
Next, we apply the property of symmetry at equilibrium, where we denote
U j k,lm =: Uk,lm and
∂ 2x j k
∂x1m∂x1 l =: xk,ml, for j ∈ {2, . . . ,N}.
(89)
33

Incorporating (43), (57) and (89), we can reduce the system described by (87) and (88) into 16
equations with unknowns: ∂ 2 p1 k ∂x1m∂x1 l and xk,ml for k,l,m ∈ {b,s}. For k,m,l ∈ {b,s}, the 16 equations are
Skqk + (N − 1)Rktk = −U1 k,lm,
Rkqk + (Sk + (N − 2)Rk)tk = xk,ml −Uk,lm,
(90)
where qk =

− ∂ 2 p1 k ∂x1m∂x1 l + ∂ 2φk ∂x1m∂xl  and tk =  ∂ φk ∂xb xb,ml + ∂ φk ∂xs xs,ml  . Solving the 2x2 system given by (90) easily yields (85) and (86).
Lemma A.2 is general enough to accommodate idiosyncratic preferences other than Gumbel
distribution and general externality functions φk(x). Next, we use Assumptions I and II from
Section 2, Proposition 3.2 and Lemma A.2 to prove Proposition 3.3.
Proof of Proposition 3.3. The proof has two main steps: (i) Verifying sufficient conditions for
(13) to have a unique solution; (ii) Establishing that a second order condition is satisfied.
Step (i): Note that (13) is equivalent to
(2φbb − φssdbLb + hb) ω (zb) + (φsb + φbs + φsbdsLb) ω (zs) − u0 b = βbzb and
(φsb + φbs + φbsdbLs) ω (zb) + (2φss − φbbdsLs + hs) ω (zs) − u0 s = βszs, (91)
where for any k ∈ {b,s}, Lk, dk and hk are functions depending on zk given by (81). We want to
find sufficient conditions for (91) to have a unique solution. First, we write some definitions. Set
ϕ1 = (φbs, φsb) and ϕ2 = (φbb, φss). For the given parameters in ψ =

βb, βs,u0 b,u0 s ,N  , we define
M : R6 − →R2 as
M (zb,zs, ϕ1, ϕ2; ψ) :=
 Mb (zb,zs, ϕ1, ϕ2; ψ)
Ms (zb,zs, ϕ1, ϕ2; ψ)

, where for each k, j ∈ {b,s}, j ̸= k,
Mk (zb,zs, ϕ1, ϕ2; ψ) :=

2φkk − φ j jdkLk + hk

ω (zk) +

φsb + φbs + φ jkd jLk

ω

z j

− u0 k − βkzk.
(92)
We show that under (19), equation (91) has a unique solution for ϕ1 = 0. From (92), if we let
ϕ1 = 0, we obtain
Mk (zb,zs,0, ϕ2; ψ) =

2φkk − φ j jdkLk + hk

ω (zk) − u0 k − βkzk. (93)
Plugging (81) into (93) gives
Mk (zb,zs,0, ϕ2; ψ) =−β 2 k (1 + Nezk)3 + βkφkkezk ((2N − 1)ezk + 3) (1 + Nezk) − 2e2zkφ 2 kk (1 + Nezk) (βk (1 + (N − 1)ezk) (1 + Nezk) − ezkφkk)
− βkzk − u0 k.
(94)
It follows that for ϕ1 = 0, Mk does not depend on z j for j ̸= k. Under (19), we claim that if ϕ1 = 0,
then the three statements below, (i-a)-(i-c), hold true:
(i-a) Mk (zb,zs,0, ϕ2; ψ) is continuous on zk for all zk ∈ R.
34

(i-b) Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in the variable zk for all zk ∈ R.
(i-c) The following limits hold true
lim
zk→−∞
Mk (zb,zs,0, ϕ2; ψ) =∞ and
limzk→∞Mk (zb,zs,0, ϕ2; ψ) =−∞. (95)
Before proving the above claims, note that (i-a), (i-b) and (i-c) combined imply that there is a
unique (z∗ b,z∗ s ) ∈ R2 such that
M (z∗ b,z∗ s ,0, ϕ2; ψ) =
 Mb  z∗ b,z∗ s ,0, ϕ2; ψ 
Ms

z∗ b,z∗ s ,0, ϕ2; ψ 

= 0.
Thus, under (19), equation (91) has a unique solution for ϕ1 = 0. By (i-b),
det
∂ (Mb,Ms)
∂ (zb,zs)


(z∗ b,z∗s ,0,ϕ2;ψ) = ∂Mb  z∗ b,z∗ s ,0, ϕ2; ψ  ∂zb ∂Ms  z∗ b,z∗ s ,0, ϕ2; ψ  ∂zs > 0. (96)
By (96) and the Implicit Function Theorem, there exists ε > 0 and a unique continuous function
(zb (·) ,zs (·)) : Bε (0,0) − →R2
such that (zb (0,0) ,zs (0,0)) =

z∗ b,z∗ s  . Moreover, for all ϕ1 ∈ Bε (0,0),
M (zb (ϕ1) ,zs (ϕ1) , ϕ1, ϕ2; ψ) =0.
In particular, under (19), there exists ε > 0 such that for all ϕ1 ∈ Bε (0,0), equation (91) has a
unique solution. We now prove that under (19), if ϕ1 = 0, then (i-a)-(i-c) hold true.
Proof of (i-a). We prove thatMk (zb,zs,0, ϕ2; ψ) is continuous onzk for all zk ∈ R. The auxiliary
function
g (zk) := e−zk (1 + (N − 1)ezk) (1 + Nezk)
has a unique minimum at z0 k = − 1 2 ln(N (N − 1)), with g  z0 k  = 2 p N (N − 1) +2N − 1. It follows
that if
βk > φkk
(2
p
N (N − 1) +2N − 1)
, (97)
then, the denominator of the fraction in (94) is never zero. We further prove (see the Mathematica
file Gumbel N.nb) that for all φkk > 0,
f (N)φkk ≥ φkk
(2
p
N (N − 1) +2N − 1)
(98)
(recall that f (N) is stated in the proposition and given by (18)). Thus, if (φkk, βk) satisfies (19),
then (97) is satisfied and Mk (zb,zs,0, ϕ2; ψ) is continuous on zk for all zk ∈ R.
Proof of (i-b). We prove that for eachk, Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in the variable
zk for all zk ∈ R. In the supplementary file Gumbel N.nb, we show that the partial derivative of
Mk (zb,zs,0, ϕ2; ψ) w.r.t. zk can be written as
∂Mk (zb,zs,0, ϕ2; ψ)
∂zk
= − ∑6 m=0 amemzk
(1 + Nezk)2 (βk (1 + (N − 1)ezk) (1 + Nezk) − ezkφkk)2 , (99)
35

where the coefficients {am}6 m=0 are polynomials on the parameters {φkk, βk,N} and are given by
a0 = β 3 k ,
a1 = β 2 k (βk (6N − 1) − 4φkk) ,
a2 = βk

β 2 k  15N2 − 6N + 1  + 4βk (1 − 4N) φkk + 5φ 2 kk  ,
a3 = 2Nβ 3 k  10N2 − 7N + 2  + β 2 k φkk  −24N2 + 11N − 1  + βkφ 2 kk (10N − 3) − 2φ 3 kk,
a4 = βkN

Nβ 2 k  15N2 − 16N + 6  + βkφkk  −16N2 + 10N − 2  + (5N − 2) φ 2 kk  ,
a5 = βkN2  Nβ 2 k  6N2 − 9N + 4  + βkφkk  −4N2 + 3N − 1  + φ 2 kk  ,
a6 = β 3 k (N − 1)2 N4. (100)
Because (97) is satisfied, the denominator of (99) is always positive. We then show (see the Math-
ematica file Gumbel N.nb) that under (19), i.e., if N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies
either
(φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > f (N) φkk) ,
then am > 0 for all m = 0, . . . ,6, where f (N) is given by (18). From (99), it follows that
∂Mk (zb,zs,0, ϕ2; ψ)
∂zk
< 0 for all zk. (101)
It follows that Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in the variable zk for all zk ∈ R.
Proof of (i-c). This claim follows from applying L’hopital rule in (94).
Step (ii): We show that a second-order condition is satisfied. From (71), (72) and the substitu-
tion zk = uk−u0 k βk , we obtain for i,r, j ∈ {1, . . . ,N} and k ∈ {b,s},
∂ 2T i k  u0 k,uk, ...,uk 
∂ur∂u j = ezk (1 + Nezk)3 β 2 k ·



(1 + (N − 1)ezk) (1 + (N − 2)ezk) i = j = r
− (1 + (N − 2)ezk)ezk i = j,i ̸= r
− (1 + (N − 2)ezk)ezk i ̸= j, j ̸= r,i = r
2e2zk − (1 + Nezk)ezk i ̸= j = r
2e2zk i ̸= j, j ̸= r,i ̸= r
.
(102)
In the supplementary file Gumbel N.nb, we show that the matrix D2 (x1 b,x1s )π1|ϕ1=0, as given by (84), can be written as
D2 (x1 b,x1s )π1

ϕ1=0
= diag

∂ 2π1
∂

x1 b 2 , ∂ 2π1 ∂ (x1s )2
!

ϕ1=0
, (103)
where
∂ 2π1
∂

x1 k 2

ϕ1=0
= ∑7 m=0 smemzk
ezk (βk ((N − 1)ezk + 1) (Nezk + 1) − ezkφkk)3 . (104)
The coefficients {sm}7 m=0 are polynomials on the parameters {φkk, βk,N} and are given by
s0 = −β 4 k ,
s1 = β 3 k (5φkk + βk (1 − 7N)) ,
36

s2 = −3β 2 k  β 2 k N (7N − 2) +βkφkk (2 − 9N) +3φ 2 kk  ,
s3 = βk

5β 3 k N2 (3 − 7N) +4β 2 k (N (15N − 7) +1) φkk + 3βk (3 − 11N) φ 2 kk + 7φ 3 kk  ,
s4 = 5β 4 k N3 (4 − 7N) +2β 3 k N (N (35N − 26) +7) φkk + β 2 k ((26 − 45N)N − 5) φ 2 kk + βk (13N − 4) φ 3 kk − 2φ 4 kk,
s5 = βk

3β 3 k (5 − 7N)N4 + 3β 2 k (N (15N − 16) +6)N2φkk + βk ((25 − 27N)N − 10)Nφ 2 kk +  6N2 − 4N + 1  φ 3 kk  ,
s6 = βkN

β 3 k (6 − 7N)N4 + β 2 k (N(15N − 22) +10)N2φkk + βk  −6N2 + 8N − 5  Nφ 2 kk + φ 3 kk  ,
s7 = −β 3 k (N − 1)N4  βkN2 + 2 (−N + 1) φkk  . (105)
Because (97) is satisfied, the denominator of (104) is always positive. We then show (see the
Mathematica file Gumbel N.nb) that under (19), i.e., if N ≥ 2 and for each k ∈ {b,s}, (φkk, βk)
satisfies either
(φkk ≤ 0 and βk > 0) or (φkk > 0 and βk > f (N) φkk) ,
then sm < 0 for all m = 0, . . . ,6, where f (N) is given by (18). It follows that D2 (x1 b,x1s )π1|ϕ1=0 is
negative definite. By continuity there exists ˜ε > 0 such that for all ϕ1 ∈ B˜ε (0,0),
D2 (x1 b,x1s )π1 (zb (ϕ1) ,zs (ϕ1) , ϕ1, ϕ2; ψ)
is negative definite. Therefore, a second condition for (79) is satisfied.
Preliminary result for the proof of Proposition 3.4. Using the same notation we introduced
in (43), the following lemma provides the FOC of (5) as a function of xk.
Lemma A.3 (FOC of CE) . The symmetric collusive equilibrium pC and xC are solutions of (3)
and of the following two equations
pk + xk
 ∂ φk
∂xk
− 1 Sk + (N − 1)Rk

+ xl
∂ φl
∂xk
= 0, for k,l ∈ {b,s},k ̸= l. (106)
The proof of this Lemma does not require assumptions I and II in Section 2. Thus, the FOC
given by (106) is applicable to idiosyncratic preferences other than Gumbel distribution and to
more general externality functions φk(x).
Proof of Lemma A.3. The FOC of (5) w.r.t. xk is
∂ Πtot
∂xk
= N

pk + xk
∂ pk
∂xk
+ xl
∂ pl
∂xk

= 0, for k,l ∈ {b,s},k ̸= l. (107)
To solve (107), we need the expressions of
∂ pk
∂xl
, for each k,l ∈ {b,s}. (108)
We determine those four partial derivatives ∂ p1 ∂ x1 in (108) using the definition of Tk in (8). By (9), for k ∈ {b,s}, the vectors of market shares and prices, (xk, . . . ,xk) and (pk, . . . ,pk) satisfy all the
following
T i k (u0 k,uk,uk, . . . ,uk) =xk, for i ∈ {1,2, · · ·,N}. (109)
37

Using the relationship uk = φk(x) − pk, it follows that
∂uk
∂xl
= ∂ φk
∂xl
− ∂ pk
∂xl
.
Taking derivative w.r.t.xb and xs in (109) gives us

N
∑
j=1
∂T i k
∂u j
! ∂ φk
∂xl
− ∂ pk
∂xl

= δkl, for i ∈ {1, · · ·,N}, k,l ∈ {b,s}, (110)
where δkl = 1 when k = l and δkl = 0 when k ̸= l. From (43) and (110),
∂ pk
∂xl
= ∂ φk
∂xl
− δkl
Sk + (N − 1)Rk
. (111)
Plugging (110) into (107) gives us
pk + xk
 ∂ φk
∂xk
− 1 Sk + (N − 1)Rk

+ xl
∂ φl
∂xk
= 0, for k,l ∈ {b,s},k ̸= l. (112)
Lemma A.3 is general enough to accommodate idiosyncratic preferences other than Gumbel
distribution and general externality functions φk(x). Next, we use Assumptions I and II from
Section 2 and Lemma A.3 to prove Proposition 3.4.
Proof of Proposition 3.4. We want to rewrite the FOC given by (106) using Assumptions I and II
from Section 2. We plugging (74), (75), (76) and (77) from the proof of Proposition 3.2 into (106)
to obtain
βz =

Φ − HC(z)  Ω(z) − u0, (113)
where HC(z) is a 2 × 2 matrix defined as
H(z) :=
"
βb(1+Nezb )2
ezb − φbb −φsb
−φbs βs(1+Nezs )2 ezs − φss
#
. (114)
Denoting zC to be the solution to (113) and using (77), we conclude the proposition by noting
that the symmetric equilibrium solution of(5) is given byxC = Ω(zC) and pC = ΦΩ(zC) − βzC −
u0.
Preliminary results for the proof of Proposition 3.5. The following Lemma shows the
second-order condition of (5) as a function of xk.
Lemma A.4 (SOC of CNE). The second-order condition of (5) is given by
∂ 2Πtot
∂xm∂xk
= N
 ∂ pk
∂xm
+ δkm
∂ pk
∂xk
+ δml
∂ pl
∂xk
+ xk
∂ 2pk
∂xm∂xk
+ xl
∂ 2pl
∂xm∂xk

, for k,l,m ∈ {b,s},k ̸= l,
(115)
38

where ∂ pk ∂xl is given by (111),
∂ 2pk
∂xm∂xl
= ∂ 2φk
∂xm∂xl
+ δkmδkl
(Sk + (N − 1)Rk)3

N
∑
j=1
N
∑
r=1
∂ 2T i k  u0 k,uk, · · ·,uk 
∂ur∂u j
!
, for k,l,m ∈ {b,s},
(116)
and Sk, Rk are given by (43).
The proof of this Lemma does not require assumptions I and II of Section 2. Thus, the SOC
given by (115) is applicable to idiosyncratic preferences other than Gumbel distribution and to
more general externality functions φk(x).
Proof of Lemma A.4. Differentiating the left-hand side of (107) w.r.t. xm, for m ∈ {b,s}, easily
yields (115). To obtain (116), we differentiate (110) w.r.t.xm. For m,k,l ∈ {b,s}, we obtain
N
∑
j=1
N
∑
r=1
∂ 2T i k
∂ur∂u j
 ∂ φk
∂xm
− ∂ pk
∂xm
 ∂ φk
∂xl
− ∂ pk
∂xl

+

N
∑
j=1
∂T i k
∂u j
!  ∂ 2φk
∂xm∂xl
− ∂ 2pk
∂xm∂xl

= 0, (117)
where the derivatives of T i k are evaluated at  u0 k,uk, ...,uk  and uk = φk(x) − pk. Plugging (43) and
(111) into (117), yields (116).
Lemma A.4 is general enough to accommodate idiosyncratic preferences other than Gumbel
distribution and general externality functions φk(x). Next, we use Assumptions I and II from
Section 2, Proposition 3.4 and Lemma A.4 to prove Proposition 3.5
Proof of Proposition 3.5. The proof has two main steps: (i) Verifying sufficient conditions for
(20) to have a unique solution; (ii) Establishing that a second order condition is satisfied.
Step (i): Note that (20) is equivalent to
2φbb
βb(N + e−zb) + φbs + φsb βb(N + e−zs) − u0 b βb − (1 + Nezb) =zb and
φbs + φsb
βs(N + e−zb) + 2φss βs(N + e−zs) − u0 s βs − (1 + Nezs) =zs. (118)
For each k ∈ {b,s}, k ̸= l, we denote
Fk(zb,zs) := 2φkk βk(N + e−zk) + φbs + φsb βk(N + e−zl ) − u0 k βk − (1 + Nezk). (119)
We want to find sufficient conditions for (118) to have a unique solution. By bounding each term
of Fk(zb,zs) independently, we can identify an upper bound for Fk(zb,zs) in R2, indeed,
Fk(zb,zs) ≤ |2φkk| βkN + |φbs + φsb| βkN − u0 k βk − 1 := vk. (120)
Similarly, if zk ≤ vk, a lower bound for Fk(zb,zs) is
Fk(zb,zs) ≥ −|2φkk| βkN − |φbs + φsb| βkN − u0 k βk − (1 + Nevk) := wk. (121)
39

We denote a vector-valued function F (zb,zs) := (Fb(zb,zs),Fs(zb,zs))T . By combining (120) and
(121), we conclude that F (zb,zs) maps the area [wb,vb] × [ws,vs] into [wb,vb] × [ws,vs]. It is clear
that F (zb,zs) is a continuous function. By using Brouwer’s Fixed-Point Theorem, there is a fixed
point for the function F (zb,zs) in the area [wb,vb] × [ws,vs], and this concludes that there is a
solution for (20) in the area [wb,vb] × [ws,vs].
We now prove the uniqueness of the solution. We first consider φbs = φsb = 0, then (20) be-
comes two decoupled equations. In particular, for each k ∈ {b,s}, zC k is the solution to
MC k (zb,zs,0, ϕ2; ψ) := 2φkk N + e−zk − βk (1 + Nezk) − u0 k − βkzk = 0, (122)
where we are setting ϕ1 = (φbs, φsb) =0, ϕ2 = (φbb, φss) and ψ =

βb, βs,u0 b,u0 s ,N  . From (122),
the function MC k (zb,zs,0, ϕ2; ψ) is continuous for all zk ∈ R. Moreover,
lim
zk→−∞
MC k (zb,zs,0, ϕ2; ψ) =∞ and limzk→∞MC k (zb,zs,0, ϕ2; ψ) =−∞. (123)
The partial derivative of MC k (zb,zs,0, ϕ2; ψ) w.r.t. zk can be written as
∂MC k (zb,zs,0, ϕ2; ψ)
∂zk
= 2ezkφkk − βk (Nezk + 1)3
(Nezk + 1)2 . (124)
Given that βk > 0, if φkk ≤ 0, then MC k (zb,zs,0, ϕ2; ψ) is strictly decreasing w.r.t. zk for all zk ∈ R.
Now, suppose that φkk > 0. The function zk 7→ 2ezk/ (Nezk + 1)3 has a unique maximum over R
at z0 k = log 1 2N and such maximum is given by 8 27N . Therefore, the numerator of (124) is strictly
negative whenever βk > 8φkk 27N . Thus, if either φkk ≤ 0 or (φkk > 0 and βk > 8φkk 27N ), then
∂MC k (zb,zs,0, ϕ2; ψ)
∂zk
< 0 for all zk. (125)
It follows that there is a unique solution for (122). Now, notice that
det

∂ (MC b ,MC s )
∂ (zb,zs)
!

(zC b ,zCs ,0,ϕ2;ψ) = ∂MC b  zC b ,zC s ,0, ϕ2; ψ  ∂zb ∂MC s  zC b ,zC s ,0, ϕ2; ψ  ∂zs > 0. (126)
By the Implicit Function Theorem, there exists ε > 0 and a unique continuous function
(zC b (ϕ1),zC s (ϕ1)) : Bε (0,0) − →R2
such that (zC b (0,0),zC s (0,0)) = (zC b ,zC s ). Moreover, for all ϕ1 ∈ Bε (0,0),
MC(zC b (ϕ1),zC s (ϕ1), ϕ1, ϕ2; ψ) :=
 MC b (zC b (ϕ1),zC s (ϕ1), ϕ1, ϕ2; ψ)
MC s (zC b (ϕ1),zC s (ϕ1), ϕ1, ϕ2; ψ)

= 0.
Step (ii): We show that a second-order condition is satisfied. Combining (102), (115) and
(116), we show (supplementary file Gumbel N.nb) that
D2 (x1 b,x1s )Πtot =

−Ne−zb

βb (Nezb + 1)3 − 2ezbφbb

N(φbs + φsb)
N(φbs + φsb) −Ne−zs

βs (Nezs + 1)3 − 2ezsφss


 .
(127)
40

Following the same argument from the paragraph above (125), if φbs = φsb = 0, N ≥ 2 and for
each k ∈ {b,s}, (φkk, βk) satisfies either
(φkk ≤ 0 and βk > 0) or

φkk > 0 and βk > 8φkk 27N  ,
then D2 (x1 b,x1s )Πtot |ϕ1=0 is negative definite. By continuity there exists ˜ε > 0 such that for all ϕ1 ∈
B˜ε (0,0),
D2 (x1 b,x1s )Πtot (zb (ϕ1) ,zs (ϕ1) , ϕ1, ϕ2; ψ)
is negative definite. Therefore, a second condition for (113) is satisfied.
Proof of Proposition 4.1. Suppose that N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies (19).
Assume that ϕ1 = (φbs, φsb) =0. From the proof of Proposition 3.3, Mk does not depend on z j for
j ̸= k (see (94)). Moreover,
lim
zk→−∞
Mk (zb,zs,0, ϕ2; ψ) =∞, (128)
and Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in zk for all zk ∈ R. From (94), we compute
Mk (zb,zs,0, ϕ2; ψ)

zk=0
= − β 2 k (N + 1)3 − 2φkkβk (N + 1)2 + 2φ 2 kk
(N + 1) (βkN (N + 1) − φkk) − u0 k
= − Ak
(N + 1) (βkN (N + 1) − φkk),
(129)
where Ak is a polynomial of order 2 in βk given by
Ak := β 2 k (N + 1)3 + βk (N + 1)2  Nu0 k − 2φkk  − φkk  (N + 1)u0 k − 2φkk  . (130)
The largest root of Ak is
γ(N, φkk,u0 k) :=

2φkk − Nu0 k  + r 2φkk − Nu0 k 2 + 4φkk  u0 k − 2φkk N+1 
2 (N + 1) . (131)
We also denote the smallest root ofAk by γ−. Note that by (19), the denominator of (129) is always
positive.
Step (i): If βk > γ(N, φkk,u0 k), by (129), (130) and (131), then (129) is strictly negative. From
(128), the fact that Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in zk for all zk ∈ R, and that z∗ k is the
unique solution of Mk (zb,zs,0, ϕ2; ψ) =0, then z∗ k < 0.
Step (ii): If γ− < βk < γ(N, φkk,u0 k), then (129) is strictly positive. From (128), the fact that
Mk (zb,zs,0, ϕ2; ψ) is strictly decreasing in zk for all zk ∈ R, and that z∗ k is the unique solution of
Mk (zb,zs,0, ϕ2; ψ) =0, then z∗ k > 0.
Note that from the definition of γ− as the smallest root of the second degree polynomial Ak, if
φkk ≤ 0, then γ− ≤ 0. If φkk > 0, then f (N)φkk > γ− (see the supplementary file Gumbel N.nb). It
follows that (19) combined with βk < γ(N, φkk,u0 k) imply that z∗ k > 0.
41

To end the proof of this proposition, note that from the Proof of Proposition 3.3, there is ε > 0
and a unique continuous function
(z∗ b (·) ,z∗ s (·)) : Bε (0,0) − →R2
such that for allϕ1 ∈ Bε (0,0), M

z∗ b (ϕ1) ,z∗ s (ϕ1) , ϕ1, ϕ2; ψ  = 0. By continuity, forˆε = |z∗ k(0,0)|/2,
there exists δ > 0 such that for all ϕ1 ∈ Bmin(δ ,ε) (0,0),
z∗ k(0,0) −

z∗ k(0,0)

2 < z∗ k (ϕ1) < z∗ k(0,0) +

z∗ k(0,0)

2 .
Thus, when z∗ k(0,0) < 0, by step (i) we obtain z∗ k (ϕ1) < z∗ k(0,0) 2 < 0. When z∗ k > 0, by (ii) we obtain
z∗ k (ϕ1) > z∗ k(0,0) 2 > 0.
Proof of Corollary 4.2. We show that case (ii) in Proposition 4.1 is not feasible for large values
of u0 k. We first assume φkk ≤ 0 and βk > 0. From (131),
sign

γ

N, φkk,u0 k  = sign  2φkk N + 1 − u0 k  . (132)
Set u0 k,1 := 2φkk/(N + 1). It follows that if φkk ≤ 0 and u0 k ≥ u0 k,1, then γ  N, φkk,u0 k  ≤ 0. Thus, (ii)
in Proposition 4.1 is not feasible as βk > 0.
Next, we assume that φkk > 0 and βk > f (N) φkk. We verify (see Gumbel N.nb) that for all
φkk > 0 and N ≥ 2, (
γ

N, φkk,u0 k  ≤ f (N) φkk for any u0 k ≥ u0 k,2,
f (N) φkk < γ

N, φkk,u0 k  for any u0 k < u0 k,2, (133)
where
u0 k,2 := −2

N4 − 2N3 − 2N2 + 2N + 2  φkk
N3 (2N3 + N2 − 3N − 2) . (134)
In particular, if u0 k ≥ u0 k,2, then case (ii) in Proposition 4.1 is not feasible as βk > f (N) φkk.
We finish the proof with a piecewise definition for ˜u0 k,
˜u0 k :=
(
u0 k,1 if φkk ≤ 0,
u0 k,2 if φkk > 0, (135)
where u0 k,1 = 2φkk/(N + 1) and u0 k,2 is given by (134).
Proof of Corollary 4.3. For each k ∈ {b,s}, let u0 k ∈ R, Φ ∈ R2x2 and βk > 0. From (91), as
N → ∞, the FOC of (4) becomes
−u0 k − βk (zk + 1) =0, for each k ∈ {b,s}.
Thus, limN→∞ z∗ k = −  u0 k βk + 1  . Moreover, limN→∞ Nx∗ k = 1 and limN→∞ p∗ k = βk. The solution of
the equation z∗ k = 0 when N → ∞ is βk = −u0 k if u0 k < 0. If u0 k ≥ 0, then limN→∞ z∗ k < 0.
42

Proof of Proposition 4.4. Recall from (77) in the Proof of Proposition 3.2,
p∗ = ΦΩ (z∗) − βz ∗ − u0,
where Ω(z∗) = (ω(z∗ b), ω(z∗ s ))T , ω(·) and z∗ are given by (76) and (91), respectively. We want to
compute the following quantity when ϕ1 = 0,
∂ p∗ k
∂u0 k

ϕ1=0
=
"
φkkez∗ k

Nez∗ k + 1 2 − βk
#
∂z∗ k
∂u0 k − 1, k ∈ {b,s}. (136)
By (94), z∗ k is uniquely characterized by Mk  z∗ b,z∗ s ,0, ϕ2; ψ  + u0 k − u0 k = 0. It follows that
∂z∗ k
∂u0 k =
"
∂

Mk

z∗ b,z∗ s ,0, ϕ2; ψ  + u0 k 
∂zk
#−1
=
"
∂Mk

z∗ b,z∗ s ,0, ϕ2; ψ 
∂zk
#−1
, (137)
where
∂Mk(z∗ b,z∗s ,0,ϕ2;ψ)
∂zk is given by (99). After plugging (137) into (136), we show (see Gum- bel N.nb) that
∂ p∗ k
∂u0 k

ϕ1=0
= −np,u

z∗ k, βk, φkk,N 
dp,u

z∗ k, βk, φkk,N , (138)
where np,u

z∗ k, βk, φkk,N  and dp,u  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the fol-
lowing way,
np,u (z∗ k, βk, φkk,N) :=
5
∑
m=1
np,u,memz∗ k , and
dp,u (z∗ k, βk, φkk,N) :=
6
∑
m=0
dp,u,memz∗ k .
(139)
Moreover, the coefficients np,u,m are as follows:
np,u,1 = β 2 k (βk − φkk) ,
np,u,2 = 2βk

2β 2 k N − 2βkNφkk + φ 2 kk  ,
np,u,3 = 6β 3 k N2 − Nβ 2 k (6N + 1) φkk + φ 2 kkβk (4N − 1) − φ 3 kk,
np,u,4 = 2βkN2 (βk − φkk) (2βkN − φkk) , and
np,u,5 = βkN2  β 2 k N2 − φkkNβk (N + 1) +φ 2 kk  .
(140)
The coefficients dp,u,m are given by
dp,u,0 = β 3 k ,
dp,u,1 = β 2 k (βk (6N − 1) − 4φkk) ,
dp,u,2 = βk

β 2 k  15N2 − 6N + 1  + 4βk (1 − 4N) φkk + 5φ 2 kk  ,
dp,u,3 = Nβ 3 k  20N2 − 14N + 4  + β 2 k  −24N2 + 11N − 1  φkk + βk (10N − 3) φ 2 kk − 2φ 3 kk,
dp,u,4 = βkN

Nβ 2 k  15N2 − 16N + 6  + βk  −16N2 + 10N − 2  φkk + (5N − 2) φ 2 kk  ,
43

dp,u,5 = βkN2  Nβ 2 k  6N2 − 9N + 4  + βk  −4N2 + 3N − 1  φkk + φ 2 kk  , and
dp,u,6 = β 3 k (N − 1)2 N4. (141)
Because the expressions determining np,u

z∗ k, βk, φkk,N  and dp,u  z∗ k, βk, φkk,N  are complex,
we focus on finding sufficient conditions for these expressions to have a specific sign for all z∗ k.
Case (i): ∂ p∗ k
∂u0 k

ϕ1=0
< 0. We verify in the supplementary file Gumbel N.nb that np,u and dp,u
(see (139)) are positive, if either of the two conditions below, (i-a) or (i-b), hold:
(i-a) φkk ≤ 0, N ≥ 2 and βk > 0.
(i-b) φkk > 0, N ≥ 2 and βk > gp,u(N, φkk), where gp(N, φkk) is the largest real root of the third
degree polynomial np,u,5 (viewed as a polynomial in βk).
Using the quadratic formula, we verify that np,u,5 (see (140)) has three real roots and that
gp,u(N, φkk) is linear in φkk and can thus be expressed as gp,u(N, φkk) =gp,u (N) φkk where
gp,u (N) :=

N +
p
(N − 1) (N + 3) +1

2N .
Case (ii): ∂ p∗ k ∂N

 ϕ1=0 > 0. We verify in the supplementary file Gumbel N.nb that np,u and dp,u
(see (139)) are negative and positive, respectively, if the condition below, (ii), holds:
(ii) φkk > 0, N ≥ 3 and f (N)φkk < βk < fp,u (N, φkk), where fp,u (N, φkk) is the largest real root
of the third degree polynomial np,u,2 (viewed as a polynomial in βk).
Using the quadratic formula, we verify that np,u,2 (see (140)) has three real roots and that
fp,u(N, φkk) is linear in φkk and can thus be expressed as fp,u(N, φkk) =fp,u (N) φkk where
fp,u (N) := 1 2
 r
N − 2
N + 1
!
.
We now show that the limits in (27) hold. From (95) and (101), the functionMk (zb,zs,0, ϕ2; ψ)+
u0 k is strictly decreasing w.r.t. zk and it approaches ±∞ as zk approaches ∓∞. Thus, if z∗ k is the
unique solution to Mk

z∗ b,z∗ s ,0, ϕ2; ψ  + u0 k = u0 k, as u0 k → ∞, Mk  z∗ b,z∗ s ,0, ϕ2; ψ  → ∞ and there-
fore, z∗ k → −∞. It follows that limu0 k→∞ z∗ k = −∞. Similarly, limu0 k→−∞ z∗ k = ∞. From (77) and (94), it follows that
p∗ k =

βk + ez∗ k (βkN − φkk)   βk  Nez∗ k + 1 2 − ez∗ k φkk 

1 + Nez∗ k   βk  1 + (N − 1)ez∗ k   1 + Nez∗ k  − ez∗ k φkk . (142)
Taking limits in the above expression yields,
lim
u0 k→−∞ p∗ k = N N − 1βk − φkk N − 1, and
lim
u0 k→∞ p∗ k = βk.
44

Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), (i) and (ii) in
Proposition 4.4 hold. From (76), (77) and (91), ∂ p∗ k/∂u0 k is a rational function w.r.t. (φbs, φsb).
Moreover, at (φbs, φsb) = (0,0), the partial derivative ∂ p∗ k/∂u0 k is given by (136). Thus, ∂ p∗ k/∂u0 k
is continuous w.r.t. (φbs, φsb) at (0,0). We conclude that there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0) ⊂ R2, cases (i) and (ii) in Proposition 4.4 hold true.
Proof of Proposition 4.6. Using (142) from the Proof of Proposition 4.4 and (76), we can write
π ∗ k

ϕ1=0
=
ez∗ k  βk + ez∗ k (βkN − φkk)   βk  Nez∗ k + 1 2 − ez∗ k φkk 

Nez∗ k + 1 2  βk  (N − 1)ez∗ k + 1   Nez∗ k + 1  − ez∗ k φkk , k ∈ {b,s}. (143)
It follows that ∂ π∗ k
∂u0 k

ϕ1=0
= ∂ π∗ k ∂z∗ k ∂z∗ k ∂u0 k , where ∂z∗ k ∂u0 k is given by (137). We show (see Gumbel N.nb) that
∂ π∗ k
∂u0 k

ϕ1=0
= −nπ,u

z∗ k, βk, φkk,N 
dπ,u

z∗ k, βk, φkk,N , (144)
where nπ,u

z∗ k, βk, φkk,N  and dπ,u  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the fol-
lowing way:
nπ,u (z∗ k, βk, φkk,N) :=
6
∑
m=1
nπ,u,memz∗ k , and
dπ,u (z∗ k, βk, φkk,N) :=
7
∑
m=0
dπ,u,memz∗ k .
(145)
Moreover, the coefficients nπ,u,m are as follows:
nπ,u,1 = β 3 k ,
nπ,u,2 = β 2 k (5βkN − 4φkk) ,
nπ,u,3 = βk

10β 2 k N2 + 2βk (1 − 7N) φkk + 5φ 2 kk  ,
nπ,u,4 = 10β 3 k N3 + 2Nβ 2 k (2 − 9N) φkk + βk (9N − 2) φ 2 kk − 2φ 3 kk,
nπ,u,5 = βkN

5β 2 k N3 + 2Nβk (1 − 5N) φkk + (4N − 1) φ 2 kk  and
nπ,u,6 = βkN2  β 2 k N3 − 2βkN2φkk + φ 2 kk  .
(146)
The coefficients dπ,u,m are given by
dπ,u,0 = β 3 k ,
dπ,u,1 = β 2 k (βk (7N − 1) − 4φkk) ,
dπ,u,2 = βk

β 2 k  21N2 − 7N + 1  + 4βk (1 − 5N) φkk + 5φ 2 kk  ,
dπ,u,3 = Nβ 3 k  35N2 − 20N + 5  + β 2 k  −40N2 + 15N − 1  φkk + βk (15N − 3) φ 2 kk − 2φ 3 kk,
dπ,u,4 = N2β 3 k  35N2 − 30N + 10  + Nβ 2 k  −40N2 + 21N − 3  φkk + 5Nβk (3N − 1) φ 2 kk − 2Nφ 3 kk,
dπ,u,5 = βkN2  Nβ 2 k  21N2 − 25N + 10  + βk  −20N2 + 13N − 3  φkk + (5N − 1) φ 2 kk  ,
dπ,u,6 = βkN3  Nβ 2 k  7N2 − 11N + 5  + βk  −4N2 + 3N − 1  φkk + φ 2 kk  , and
45

dπ,u,7 = β 3 k (N − 1)2 N5. (147)
Because the expressions determining nπ,u

z∗ k, βk, φkk,N  and dπ,u  z∗ k, βk, φkk,N  are complex,
we focus on finding sufficient conditions for these expressions to have a specific sign for allz∗ k. We
verify in the supplementary file Gumbel N.nb that nπ,u and dπ,u (see (145)) are positive, if either
of the two conditions below, (i-a) or (i-b), hold:
(i-a) φkk ≤ 0, N ≥ 2 and βk > 0.
(i-b) φkk > 0, N ≥ 2 and βk > gπ,u(N, φkk), where gπ,u(N, φkk) is the largest real root of the third
degree polynomial nπ,u,6 (viewed as a polynomial in βk).
Using the quadratic formula, we verify that nπ,u,6 (see (146)) has three real roots and that
gπ,u(N, φkk) is linear in φkk and can thus be expressed as gπ,u(N, φkk) =gπ,u (N) φkk where
gπ,u (N) :=
r
N − 1
N3 + 1 N .
We now show that the limits in (29) hold. From the Proof of Proposition 4.6, we have that
limu0 k→∞ z∗ k = −∞ and limu0 k→−∞ z∗ k = ∞ (see the paragraph above (142)). Taking limits in (143) yields,
lim
u0 k→−∞ π ∗ k = 1 N − 1βk − φkk (N − 1)N , and
lim
u0 k→∞ π ∗ k = 0.
Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), the first part in
Proposition 4.6 holds. From (76), (77) and (91), ∂ π∗ k /∂u0 k is a rational function w.r.t. (φbs, φsb).
Moreover, at (φbs, φsb) = (0,0), the partial derivative ∂ π∗ k /∂u0 k is given by (144). Thus, ∂ π∗ k /∂u0 k
is continuous w.r.t. (φbs, φsb) at (0,0). We conclude that there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0) ⊂ R2, the first part of Proposition 4.6 holds true.
Proof of Proposition 4.7. Plugging (142) from the Proof of Proposition 4.4 and (76) into (30), we
obtain
CS∗ k

ϕ1=0
=−β 2 k  1 + Nez∗ k 3 + βkφkkez∗ k  (2N − 1)ez∗ k + 3   1 + Nez∗ k  − 2e2z∗ k φ 2 kk 1 + Nez∗ k   βk  1 + (N − 1)ez∗ k   1 + Nez∗ k  − ez∗ k φkk 
+ µk + βk (ln (N + 1) +γ) , k ∈ {b,s}.
(148)
It follows that ∂CS∗ k
∂u0 k

ϕ1=0
= ∂CS∗ k ∂z∗ k ∂z∗ k ∂u0 k , where ∂z∗ k ∂u0 k is given by (137). We show (see Gumbel N.nb)
that
∂CS∗ k
∂u0 k

ϕ1=0
= nCS,u

z∗ k, βk, φkk,N 
dCS,u

z∗ k, βk, φkk,N , (149)
46

where nCS,u

z∗ k, βk, φkk,N  and dCS,u  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the
following way,
nCS,u (z∗ k, βk, φkk,N) :=
5
∑
m=1
nCS,u,memz∗ k , and
dCS,u (z∗ k, βk, φkk,N) :=
6
∑
m=0
dCS,u,memz∗ k .
(150)
Moreover, the coefficients nCS,u,m are as follows:
nCS,u,1 = β 2 k (βk − 2φkk) ,
nCS,u,2 = 2βk

2β 2 k N + βk (1 − 4N) φkk + 2φ 2 kk  ,
nCS,u,3 = 6β 3 k N2 + β 2 k  −12N2 + 5N − 1  φkk + βk (8N − 3) φ 2 kk − 2φ 3 kk,
nCS,u,4 = 2βkN

2β 2 k N2 + βk  −4N2 + 2N − 1  φkk + (2N − 1) φ 2 kk  and
nCS,u,5 = βkN2  β 2 k N2 + βk  −2N2 + N − 1  φkk + φ 2 kk  .
(151)
The coefficients dCS,u,m = dp,u,m for all m ∈ {0, . . . ,6} where dp,u,m is given by (141). Because
the expressions determining nCS,u

z∗ k, βk, φkk,N  and dCS,u  z∗ k, βk, φkk,N  are complex, we focus
on finding sufficient conditions for these expressions to have a specific sign for all z∗ k.
Case (i): ∂CS∗ k
∂u0 k

ϕ1=0
> 0. We verify in the supplementary file Gumbel N.nb that nCS,u and dCS,u
(see (150)) are positive, if either of the two conditions below, (i-a) or (i-b), hold:
(i-a) φkk ≤ 0, N ≥ 2 and βk > 0.
(i-b) φkk > 0, N ≥ 2 and βk > 2φkk.
Case (ii): ∂CS∗ k
∂u0 k

ϕ1=0
< 0. We verify in the supplementary fileGumbel N.nb that nCS,u and dCS,u
(see (150)) are negative and positive, respectively, if the condition below, (ii-a), holds:
(ii-a) φkk > 0, N ≥ 2 and f (N) φkk < βk < fCS,u (N, φkk), where fCS,u (N, φkk) is the unique real
root of the third degree polynomial nCS,u,3 (viewed as a polynomial in βk).
We next verify that nCS,u,3 indeed has a unique real root and that fCS,u (N, φkk) is linear in φkk
and can thus be expressed as fCS,u (N, φkk) = fCS,u (N) φkk. We note that nCS,u,3/(6N2) has the
standard form nCS,u,3
6N2 = β 3 k + b2β 2 k + b1βk + b0, (152)
where b0, b1 and b2 depend on N and φkk. We first clarify why this polynomial has a unique real
root using Cardano’s condition. We define tk := 1 3(3b1 − b2 2), sk := 1 27 (2b3 2 − 9b2b1 + 27b0) and
∆k := (sk/2)2 + (tk/3)3. Equivalently,
tk = −

144N4 − 264N3 + 103N2 − 10N + 1  φ 2 kk
108N4 ,
sk = −

1728N6 − 4752N5 + 4356N4 − 1106N3 + 192N2 − 15N + 1  φ 3 kk
2916N6 , and
∆k :=

4608N6 − 11136N5 + 6944N4 + 408N3 − 97N2 + 18N − 1  φ 6 kk
139968N8 .
(153)
47

For each k ∈ {b,s}, if φkk > 0 and N ≥ 2, then ∆k > 0. It thus follows that nCS,u,3 has a unique real
root given by
α := Car(sk, ∆k) − b2 3 , (154)
where b2 =

−12N2 + 5N − 1  φkk/(6N2) and Car(·, ·) is given
Car(sk, ∆k) :=

−sk
2 +
p
∆k
1/3
+

−sk
2 −
p
∆k
1/3
. (155)
For φkk > 0, it is not difficult to see that α is linear in φkk, so we can write
fCS,u (N) =α/φkk, (156)
where α is given by (154).
Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), (i) and (ii) in
Proposition 4.7 hold. From (76), (77) and (91), ∂CS∗ k/∂u0 k is a rational function w.r.t. (φbs, φsb).
Moreover, at(φbs, φsb) = (0,0), the partial derivative∂CS∗ k/∂u0 k is given by (149). Thus,∂CS∗ k/∂u0 k
is continuous w.r.t. (φbs, φsb) at (0,0). We conclude that there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0) ⊂ R2, cases (i) and (ii) in Proposition 4.7 hold true.
Proof of Proposition 4.8. Suppose that N ≥ 2 and for each k ∈ {b,s}, (φkk, βk) satisfies (23).
Assume that ϕ1 = (φbs, φsb) =0. From the proof of Proposition 3.5, MC k does not depend on z j for
j ̸= k (see (122)). Moreover,
lim
zk→−∞
MC k (zb,zs,0, ϕ2; ψ) =∞, (157)
and MC k (zb,zs,0, ϕ2; ψ) is strictly decreasing in zk for all zk ∈ R. From (122), we compute
MC k (zb,zs,0, ϕ2; ψ)

 zk=0 = 2φkk N + 1 − βk (1 + N) − u0 k. (158)
The only root of (158) as a polynomial in βk is given by
γC(N, φkk,u0 k) := 2φkk − u0 k (N + 1) (N + 1)2 . (159)
Observation (i): The condition βk > γC(N, φkk,u0 k) implies that (158) is strictly negative. We
combine this fact with (157) and the facts that MC k (zb,zs,0, ϕ2; ψ) is strictly decreasing in zk ∀zk ∈
R and zC k is the unique solution of MC k (zb,zs,0, ϕ2; ψ) =0 to conclude that zC k < 0.
Observation (ii): If βk < γC(N, φkk,u0 k), then (158) is strictly positive and thus zC k > 0.
The Proof of Proposition 3.5 implies that there is ε > 0 and a unique continuous function

zC b (·) ,zC s (·)  : Bε (0,0) − →R2
such that for all ϕ1 ∈ Bε (0,0), M C  zC b (ϕ1) ,zC s (ϕ1) , ϕ1, ϕ2; ψ  = 0. By this continuity, for ˆε =
|zC k (0,0)|/2, there exists δ > 0 such that for all ϕ1 ∈ Bmin(δ ,ε) (0,0),
zC k (0,0) −

zC k (0,0)

2 < zC k (ϕ1) < zC k (0,0) +

zC k (0,0)

2 .
48

Thus, when zC k (0,0) < 0, by observation (i) we obtain zC k (ϕ1) < zC k (0,0) 2 < 0. When zC k > 0, by
observation (ii) we obtain zC k (ϕ1) > zC k (0,0) 2 > 0. Concluding the proof of the Proposition.
Proof of Corollary 4.9. Note that from (131) and (159),
γ

N, φkk,u0 k  − γC  N, φkk,u0 k 
=
2(N−1)φkk+(−N2+N+2)u0 k+
q
N2(N+1)2(u0 k) 2+4(N2−1)φ 2 kk−4(N−1)(N+1)2u0 kφkk
2(N+1)2
. (160)
From (132) and the Proof of Corollary 4.2, if γ

N, φkk,u0 k  ≥ 0 then,
either (φkk < 0 and u0 k ≤ 2φkk N + 1) or φkk ≥ 0.
Suppose that (φkk < 0 and u0 k ≤ 2φkk N+1 ) . By (160), γ  N, φkk,u0 k  ≥ γC  N, φkk,u0 k  . On the other
hand, if φkk ≥ 0 then (160) implies that γ

N, φkk,u0 k  ≥ γC  N, φkk,u0 k  .
Proof of Corollary 4.10. First assume φkk ≤ 0 and βk > 0. From the definition of γC(N, φkk,u0 k)
in (159), if u0 k ≥ 2φkk/(N + 1), then γC(N, φkk,u0 k) ≤ 0. In this case, statement (ii) of Proposition
4.8 is not feasible as βk > 0.
Now assume that φkk > 0 and βk > 8φkk 27N . The unique ˜uC k such that γC(N, φkk, ˜uC k ) =8φkk 27N is given
by
˜u0 k = −2 (N (4N − 19) +4) φkk 27N (N + 1) .
If u0 k ≥ ˜uC k , then γC(N, φkk, ˜u0 k) ≤ 8φkk 27N . Thus, statement (ii) in Proposition 4.8 is not feasible as
βk > 8φkk 27N .
We finish the proof with a piecewise definition for ˜uC k ,
˜uC k :=
( 2φkk
N+1 if φkk ≤ 0,
− 2(N(4N−19)+4)φkk 27N(N+1) if φkk > 0. (161)
Proof of Proposition 4.11. First, we set ϕ1 = (φbs, φsb) =0. From (94) and (122), we obtain
Mk (zb,zs,0, ϕ2; ψ) − MC k (zb,zs,0, ϕ2; ψ) = βk (N − 1)ezk

βk (Nezk + 1)2 − ezkφkk

βk ((N − 1)ezk + 1) (Nezk + 1) − ezkφkk (162)
Step (i): If φkk ≤ 0 or (φkk > 0 and βk > f (N) φkk), then (162) is strictly positive for all
zk ∈ R. The proofs of Propositions 3.3 and 3.5 imply that the functions Mk (zb,zs,0, ϕ2; ψ) and
MC k (zb,zs,0, ϕ2; ψ) are independent of zl for l ̸= k and are strictly decreasing on zk. It follows that
z∗ k > zC k .
49

Again, from the Proofs of Proposition 3.3 and 3.5, there is ε > 0 and unique continuous
functions

z∗ b (·) ,z∗ s (·)  : Bε (0,0) − →R2 and  zC b (·) ,zC s (·)  : Bε (0,0) − →R2 such that for all
ϕ1 ∈ Bε (0,0),
M (z∗ b (ϕ1) ,z∗ s (ϕ1) , ϕ1, ϕ2; ψ) =0 = MC

zC b (ϕ1) ,zC s (ϕ1) , ϕ1, ϕ2; ψ  . (163)
By continuity, there is ˆε > 0 such that z∗ k (ϕ1) > zC k (ϕ1) for all ϕ1 ∈ Bˆε (0,0).
Step (ii): By (17) and (22), x∗ k = ω  z∗ k  and xC k = ω  zC k  where ω (z) = 1 e−z+N . Note that
ω ′ (z) > 0 for all z ∈ R. Then, x∗ k = ω  z∗ k  > ω  zC k  = xC k for all ϕ1 ∈ Bˆε (0,0).
Step (iii): From (12), the function p (z) =ΦΩ (z) − βz − u0 determines the equilibrium prices
p∗ k and pC k . Note that
∂ pk
∂zk
= φkkω ′ (zk) − βk = φkkezk − βk (Nezk + 1)2
(Nezk + 1)2 . (164)
The function zk 7→ ezk (Nezk +1)2 has a unique maximum over R at z0 k = log  1 N  and such maximum
is given by 1 4N . Then, (164) is strictly negative for all zk ∈ R when either φkk ≤ 0 or (φkk > 0
and βk > φkk 4N ). Moreover, from (18), f (N) φkk > φkk 4N for all N ≥ 2 and φkk > 0. Then, for ϕ1 = 0,
p∗ k = pk  z∗ k  < pk  zC k  = pC k . By step (i) and continuity, there is ˆε > 0 such that p∗ k  z∗ k(ϕ1)  <
pC k  zC k (ϕ1)  for all ϕ1 ∈ Bˆε (0,0).
Proof of Proposition 5.1. Recall from (77) in the Proof of Proposition 3.2,
p∗ = ΦΩ (z∗) − βz ∗ − u0,
where Ω(z∗) = (ω(z∗ b), ω(z∗ s ))T , ω(·) and z∗ are given by (76) and (91), respectively. We want to
compute the following quantity when ϕ1 = 0,
∂ p∗ k
∂N =

φkkω ′ (z∗ k) − βk  ∂z∗ k ∂N + φkk ∂ ω  z∗ k  ∂N + φk j  ω ′(z∗ j) ∂z∗ j ∂N + ∂ ω(z∗ j) ∂N  , k, j ∈ {b,s} k ̸= j.
(165)
By (76), ω(z∗ k) =1/(e−z∗ k + N), then
ω ′ (z∗ k) = e−z∗ k  e−z∗ k + N 2 and
∂ ω

z∗ k 
∂N = −1  e−z∗ k + N 2 .
(166)
After differentiating both sides of the two equations in (91) w.r.t. N, we can write ∂z∗ k/∂N at
ϕ1 = (φbs, φsb) =0,
" ∂z∗s
∂N∂z∗ b
∂N
#
ϕ1=0
= 1 JN
 −d b
c −a
 " ∂ [hb−φssdbLb]
∂N ω

z∗ b  + (2φbb − φssdbLb + hb) ∂ ω(z∗ b) ∂N∂ [hs−φbbdsLs]
∂N ω (z∗ s ) + (2φss − φbbdsLs + hs) ∂ ω(z∗s ) ∂N
#
, (167)
50

where JN := ad − bc and
a = ω (z∗ b)
 ∂hb
∂zs
− φss
∂ [dbLb]
∂zs

,
b = ω (z∗ b)
∂hb
∂zb
− φss
∂ [dbLb]
∂zb

+ (2φbb − φssdbLb + hb) ω ′ (z∗ b) − βb,
c = ω (z∗ s ) ∂ [hs − φbbdsLs] ∂zs + (2φss − φbbdsLs + hs) ω ′ (z∗ s ) − βs, and
d = ω (z∗ s ) ∂ [hs − φbbdsLs] ∂zb .
(168)
Moreover, recall that Lk, dk and hk for k ∈ {b,s} are given by (15). After plugging (168) into (167)
and then plugging the resulting expression into (165), we show (see Gumbel N.nb) that
∂ p∗ k
∂N

ϕ1=0
= np

z∗ k, βk, φkk,N 
d

z∗ k, βk, φkk,N  , (169)
where np

z∗ k, βk, φkk,N  and d  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the following
way,
np (z∗ k, βk, φkk,N) :=
6
∑
m=2
nm,pemz∗ k , and
d (z∗ k, βk, φkk,N) :=
6
∑
m=0
dmemz∗ k .
(170)
Moreover, the coefficients nm,p are as follows:
n2,p = β 3 k (φkk − βk) ,
n3,p = −β 2 k  4β 2 k N + βkφkk (1 − 4N) +2φ 2 kk  ,
n4,p = βk

−6β 3 k N2 + 2β 2 k φkkN (3N − 1) +βkφ 2 kk (3 − 4N) +φ 3 kk  ,
n5,p = −βk

4β 3 k N3 + β 2 k φkkN2 (1 − 4N) +βkφ 2 kkN (2N − 3) +φ 3 kk  , and
n6,p = β 3 k N4 (φkk − βk) .
(171)
The coefficients dm are given by
d0 = β 3 k ,
d1 = β 2 k (βk (6N − 1) − 4φkk) ,
d2 = βk

β 2 k  15N2 − 6N + 1  + 4βk (1 − 4N) φkk + 5φ 2 kk  ,
d3 = β 3 k N  20N2 − 14N + 4  + β 2 k φkk  −24N2 + 11N − 1  + βkφ 2 kk (10N − 3) − 2φ 3 kk,
d4 = βkN

β 2 k N  15N2 − 16N + 6  + βkφkk  −16N2 + 10N − 2  + (5N − 2) φ 2 kk  ,
d5 = βkN2  β 2 k N  6N2 − 9N + 4  + βkφkk  −4N2 + 3N − 1  + φ 2 kk  , and
d6 = β 3 k (N − 1)2 N4. (172)
51

Because the expressions determining np

z∗ k, βk, φkk,N  and d  z∗ k, βk, φkk,N  are complex, we
focus on finding sufficient conditions for these expressions to have a specific sign for all z∗ k. Note
that not all the coefficients in {dm}6 m=0 can be simultaneously negative because d0 > 0. Thus, we
focus on finding the regions for which dm > 0 for each m = 0, . . . ,6.
Case (i): ∂ p∗ k ∂N

 ϕ1=0 < 0. We verify in the supplementary file Gumbel N.nb that np and d (see
(170)) are negative and positive, respectively, if either of the two conditions below, (i-a) or (i-b),
hold:
(i-a) φkk > 0, N ≥ 2 and βk > φkk.
(i-b) φkk ≤ 0, N ≥ 2 and βk > gp(N, φkk), where gp(N, φkk) is the largest real root of the third
degree polynomial n5,p/βk (viewed as a polynomial in βk).
We next verify thatn5,p/βk has three real roots and that gp(N, φkk) is linear in φkk and can thus
be expressed as gp(N, φkk) =gp (N) φkk. We note that n5,p/(βk(4N3)) has the standard form
n5,p
βk(4N3) = β 3 k + c2β 2 k + c1βk + c0, (173)
where c0, c1 and c2 depend on N and φkk. Following the proof of Proposition 3.3, we use Cardano’s
formula to define
tk := 1 3(3c1 − c2 2) =−

16N2 − 32N + 37  φ 2 kk
48N2 ,
sk := 1 27 (2c3 2 − 9c2c1 + 27c0) =−

64N3 − 192N2 + 264N − 271  φ 3 kk
864N3 , and
∆k := (sk/2)2 + (tk/3)3 = −

64N4 − 96N3 + 52N2 + 108N − 211  φ 6 kk
27648N6 .
(174)
For each k ∈ {b,s}, if φkk ̸= 0 and N ≥ 2, then ∆k < 0. It thus follows that n5,p/βk has three simple
real roots given by
α j := 2
r
−tk
3 cos
 θ + 2 jπ
3

− c2
3 , for j = 0,1,2,
0 < θ < π, and cos (θ ) = −sk/2p
−(tk/3)3 .
(175)
From (174) and (175), θ = θ (N) is a function of N and is independent of φkk. Moreover, for
φkk < 0,
p
−tk/3 and c2 = − (4N−1)φkk 4N are linear functions of φkk. Thus, for φkk < 0, the three
simple real roots of n5,p/βk can be written as
α j = w j(N)φkk. (176)
We can thus write gp(N, φkk) =gp (N) φkk, where
gp(N) = max j=0,1,2 {w j(N)}. (177)
52

From (171) and (173),
lim
N→∞
n5,p
βk(4N3) = β 3 k − φkkβ 2 k .
Thus, for φkk < 0, the quantity gp (N) φkk approaches 0 as N → ∞.
Case (ii): ∂ p∗ k ∂N

 ϕ1=0 > 0. We verify in the supplementary file Gumbel N.nb that np and d (see
(170)) are positive if either of the two conditions below, (ii-a) or (ii-b), hold:
(ii-a) φkk > 0, N ≥ 3 and f (3)φkk < βk < 2 3 φkk, where f (3) is given by (18).
(ii-b) φkk > 0, N ≥ 4 and f (N) φkk < βk < fp (N, φkk), where fp (N, φkk) is the unique real root of
the third degree polynomial n4,p/βk (viewed as a polynomial in βk).
We next verify thatn4,p/βk indeed has a unique real root and that fp (N, φkk) is linear in φkk and
can thus be expressed as fp (N, φkk) =fp (N) φkk. We note that n4,p/(βk(−6N2)) has the standard
form n4,p
βk(−6N2) = β 3 k + b2β 2 k + b1βk + b0, (178)
where b0, b1 and b2 depend on N and φkk. We first clarify why this polynomial has a unique real
root using Cardano’s condition. We define
˜tk := −

18N2 − 48N + 29  φ 2 kk
54N2 ,
˜sk := −

108N3 − 432N2 + 630N − 85  φ 3 kk
1458N3 , and
˜∆k :=

72N4 − 168N3 − 88N2 + 556N − 171  φ 6 kk
34992N6 .
(179)
For each k ∈ {b,s}, if φkk > 0 and N ≥ 4, then ˜∆k > 0. It thus follows that n4,p/βk has a unique
real root given by
˜α j := Car( ˜sk, ˜∆k) − b2 3 , (180)
where b2 = (1 − 3N)φkk/(3N) and Car(·, ·) is given
Car(sk, ∆k) :=

−sk
2 +
p
∆k
1/3
+

−sk
2 −
p
∆k
1/3
. (181)
For φkk > 0, it is not difficult to see that ˜α j is linear in φkk, so we can write
fp (N) =˜α j/φkk, (182)
where ˜α j is given by (180). Finally, for any φkk > 0, by (178)
lim
N→∞
n4,p
βk(−6N2) = β 2 k (βk − φkk).
It thus follows that fp (N) φkk converges to φkk as N → ∞.
53

From (ii-a) and (ii-b), it follows that ∂ p∗ k ∂N |ϕ1=0 > 0 whenever N ≥ 3, φkk > 0 and f (N) φkk <
βk < fp (N) φkk, where the definition of fp(N) is extended to include the case N = 3 as follows,
fp (N) :=
(
2
3 N = 3,
˜α j/φkk N ≥ 4, (183)
where ˜α j is given by (180).
Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), (i) and (ii) in
Proposition 5.1 hold. From (165), (167) and (168), ∂ p∗ k/∂N is a rational function w.r.t. (φbs, φsb).
Moreover, at (φbs, φsb) = (0,0), the partial derivative ∂ p∗ k/∂N is given by (169). Thus, ∂ p∗ k/∂N
is continuous w.r.t. (φbs, φsb) at (0,0). We conclude that there exists ε > 0 such that for any
(φbs, φsb) ∈ Bε (0) ⊂ R2, cases (i) and (ii) in Proposition 5.1 hold true.
Proof of Proposition 5.2. Using the same ideas from the Proof of Proposition 5.1, we want to
compute the following quantity when ϕ1 = 0,
∂

Nx∗ k 
∂N = x∗ k + N ∂x∗ k ∂N . (184)
By (76), x∗ k = 1 e−z∗ k +N . Then,
∂x∗ k
∂N = −1  e−z∗ k + N 2

1 − e−z∗ k ∂z∗ k
∂N

. (185)
Using (167) and (185), we show (see Gumbel N.nb) that
∂

Nx∗ k 
∂N

ϕ1=0
= nNx

z∗ k, βk, φkk,N 
dNx

z∗ k, βk, φkk,N , (186)
where
nNx (z∗ k, βk, φkk,N) :=
6
∑
m=1
nm,Nxemz∗ k and
dNx (z∗ k, βk, φkk,N) :=
7
∑
m=0
dm,Nxemz∗ k .
(187)
Moreover, the coefficients nm,Nx are as follows:
n1,Nx = β 3 k ,
n2,Nx = β 2 k (βk (5N − 1) − 4φkk) ,
n3,Nx = βk

β 2 k  10N2 − 4N + 1  + 2βk (2 − 7N) φkk + 5φ 2 kk  ,
n4,Nx = β 3 k N  10N2 − 6N + 3  + β 2 k φkk  −18N2 + 10N − 1  + 3βkφ 2 kk (3N − 1) − 2φ 3 kk,
n5,Nx = βkN

β 2 k N  5N2 − 4N + 3  + 2βkφkk  −5N2 + 4N − 1  + (4N − 3) φ 2 kk  ,
n6,Nx = β 2 k N2  βkN  N2 − N + 1  −  2N2 − 2N + 1  φkk  . (188)
54

The coefficients dm,Nx are given by
d0,Nx = β 3 k ,
d1,Nx = β 2 k (βk (7N − 1) − 4φkk) ,
d2,Nx = βk

β 2 k  21N2 − 7N + 1  + 4βk (1 − 5N) φkk + 5φ 2 kk  ,
d3,Nx = 5β 3 k N  7N2 − 4N + 1  + β 2 k φkk  −40N2 + 15N − 1  + 3βk (5N − 1) φ 2 kk − 2φ 3 kk,
d4,Nx = N

5β 3 k N  7N2 − 6N + 2  + β 2 k φkk  −40N2 + 21N − 3  + 5βk (3N − 1) φ 2 kk − 2φ 3 kk  ,
d5,Nx = βkN2  β 2 k N  21N2 − 25N + 10  + βk  −20N2 + 13N − 3  φkk + (5N − 1) φ 2 kk  ,
d6,Nx = βkN3  β 2 k N  7N2 − 11N + 5  + βk  −4N2 + 3N − 1  φkk + φ 2 kk  ,
d7,Nx = β 3 k (N − 1)2 N5. (189)
Because the expressions determining nNx

z∗ k, βk, φkk,N  and dNx  z∗ k, βk, φkk,N  are complex,
we focus instead on finding sufficient conditions for these expressions to have a specific sign for
all z∗ k. Note that not all coefficients in {dm,Nx}7 m=0 can be simultaneously negative, as d0,Nx > 0.
Thus, we focus on finding the regions for which dm,Nx > 0 for each m = 0, . . . ,7. By the previous
argument, we also focus on finding regions where the coefficients nm,Nx > 0 for all m = 1, . . . ,6.
We verify in the supplementary fileGumbel N.nb that the coefficients nm,Nx and dm,Nx in (188) and
(189), respectively, are positive if either of the two conditions below, (a) or (b), hold:
(a) φkk ≤ 0, N ≥ 2 and βk > 0.
(b) φkk > 0, N ≥ 2 and βk > gx(N)φkk, where gx(N)φkk is the unique non-zero real root of n6,Nx
(viewed as a polynomial in βk) and gx(N) is given by
gx(N) :=

2N2 − 2N + 1 
N (N2 − N + 1) . (190)
We remark that finding the non-zero root ofn6,Nx leads to a solution of a linear equation (see (188)),
so the uniqueness of the root and its linearity in φkk are obvious. We also show (see Gumbel N.nb)
that if N ≥ 2, βk > 0 and φkk > 0, then gx(N)φkk ≥ f (N) φkk.
Finally, we show that there exists ε such that for any (φbs, φsb) ∈ Bε (0), Proposition 5.2 holds.
Note that from (167) and (168), ∂ (Nx∗ k)/∂N is a rational function w.r.t. (φbs, φsb). Moreover, at
(φbs, φsb) = (0,0), ∂ (Nx∗ k)/∂N is given by (186). Thus,∂ (Nx∗ k)/∂N is continuous w.r.t.(φbs, φsb) at
(0,0). We conclude that there existsε > 0 such that for any(φbs, φsb) ∈ Bε (0) ⊂ R2, ∂ (Nx∗ k)/∂N >
0 provided that either (a) or (b) above hold.
Proof of Proposition 5.3. Using the same ideas from the Proof of Proposition 5.1, we want to
compute the following quantity when ϕ1 = 0,
∂CS∗ k
∂N

ϕ1=0
= βk
 1
N + 1 + ∂z∗ k ∂N

 ϕ1=0  . (191)
Using equations (165), (167) and (185), we show (see Gumbel N.nb) that
∂CS∗ k
∂N

ϕ1=0
= nCSk

z∗ k, βk, φkk,N 
dCSk

z∗ k, βk, φkk,N , (192)
55

where nCSk

z∗ k, βk, φkk,N  and dCSk  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the fol-
lowing way,
nCSk (z∗ k, βk, φkk,N) :=
6
∑
m=0
nm,CSkemz∗ k , and
dCSk (z∗ k, βk, φkk,N) :=
6
∑
m=0
dm,CSkemz∗ k .
(193)
Moreover, the coefficients nm,CSk and dm,CSk are polynomials on {φkk, βk,N} and are defined, re-
spectively, as
n0,CSk = β 4 k ,
n1,CSk = β 3 k (βk (6N − 1) − 4φkk) ,
n2,CSk = β 2 k  β 2 k  15N2 − 5N + 2  + 2βk (1 − 9N) φkk + 5φ 2 kk  ,
n3,CSk = βk

β 3 k N  20N2 − 10N + 8  + β 2 k φkk  −32N2 + 6N + 2  + βkφ 2 kk (14N + 1) − 2φ 3 kk  ,
n4,CSk = βk

β 3 k N2  15N2 − 10N + 12  + β 2 k φkk  −28N3 + 6N2 + 5N − 1  + βkφ 2 kk  13N2 + 2N − 4  − 2 (N + 1) φ 3 kk  ,
n5,CSk = β 2 k N  β 2 k N2  6N2 − 5N + 8  + βkφkk  −12N3 + 2N2 + 4N − 2  + φ 2 kk  4N2 + N − 4  ,
n6,CSk = β 3 k N2  βkN2  N2 − N + 2  +  N − 1 − 2N3 φkk  . (194)
The coefficients dm,CSk are given by
d0,CSk = β 3 k (N + 1) ,
d1,CSk = β 2 k (N + 1) (βk (6N − 1) − 4φkk) ,
d2,CSk = βk (N + 1)

β 2 k  15N2 − 6N + 1  + 4βk (1 − 4N) φkk + 5φ 2 kk  ,
d3,CSk = (N + 1)

β 3 k N  20N2 − 14N + 4  + β 2 k φkk  −24N2 + 11N − 1  + βkφ 2 kk (10N − 3) − 2φ 3 kk  ,
d4,CSk = βkN (N + 1)

β 2 k N  15N2 − 16N + 6  + βkφkk  −16N2 + 10N − 2  + (5N − 2) φ 2 kk  ,
d5,CSk = βkN2 (N + 1)  β 2 k N  6N2 − 9N + 4  + βkφkk  −4N2 + 3N − 1  + φ 2 kk  ,
d6,CSk = β 3 k (N − 1)2 N4 (N + 1). (195)
Because the expressions determining nCSk

z∗ k, βk, φkk,N  and dCSk  z∗ k, βk, φkk,N  are complex,
we focus instead on finding sufficient conditions for these expressions to have a specific sign for
all z∗ k. Note that not all coefficients in  dm,CSk 	6 m=0 can be simultaneously negative, as d0,CSk > 0.
Thus, we focus on finding the regions for which dm,CSk > 0 for each m = 0, . . . ,6.
Case (i): ∂CS∗ k ∂N

 ϕ1=0 > 0. We verify in the supplementary file Gumbel N.nb that nm,CSk > 0 and
dm,CSk > 0 for all m = 0, . . . ,6 (see (194) and (195)), if either of the two conditions below, (a-i) or
(b-i), hold:
(a-i) φkk ≤ 0, N ≥ 2 and βk > 0.
(b-i) φkk > 0, N ≥ 2 and βk > gCS(N)φkk, where gCS(N)φkk is the unique non-zero real root of
n6,CSk (viewed as a polynomial in βk) and gCS(N) is given by
gCS(N) := 2N3 − N + 1 N2 (N2 − N + 2). (196)
56

We remark that finding the non-zero root of n6,CSk leads to a solution of a linear equation (see
(194)), so the uniqueness of the root and its linearity in φkk are obvious.
Case (ii): ∂CS∗ k ∂N

 ϕ1=0 < 0. First, we want to show that for all φkk > 0,
nCSk (z∗ k, βk, φkk,N) =
6
∑
m=0
nm,CSkemz∗ k < 0.
Using (18) and (196), we show (see Gumbel N.nb) that for all N ≥ 2 and φkk > 0,
f (N) φkk < gCS(N)φkk. (197)
For N ≥ 7, φkk > 0 and βk ∈ ( f (N) φkk,gCS(N)φkk), we show (see Gumbel N.nb) that
n0,CSk > 0 for all k = 0, · · ·5, and
nm,CS6 < 0. (198)
From (198), if N ≥ 7, φkk > 0 and βk ∈ ( f (N) φkk,gCS(N)φkk), then
6
∑
m=0
nm,CSkemz∗ k
= n0,CSk + n1,CSkez∗ k + n2,CSke2z∗ k + n3,CSke3z∗ k + n4,CSke4z∗ k + n5,CSke5z∗ k
| {z }
>0
+n6,CSke6z∗ k
| {z }
<0
.
(199)
From Proposition 4.1, if βk < γ

N, φkk,u0 k  , then z∗ k > 0. Moreover, by hypothesis, z∗ k < 1 5 ln2, then
e5z∗ k < 2. It follows from (199) that
6
∑
m=0
nm,CSkemz∗ k < n0,CSk + 2  n1,CSk + n2,CSk + n3,CSk + n4,CSk + n5,CSk  + n6,CSk
= βk
3
∑
m=0
ym,kβ m k ,
(200)
where yk,0 = −4 (N + 2) φ 3 kk,
yk,1 = 4

2N3 + 7N2 + 6N + 1  φ 2 kk,
yk,2 = −

2N5 + 24N4 + 51N3 + 45N2 + 18N + 2  φkk,
yk,3 =

N6 + 11N5 + 22N4 + 36N3 + 34N2 + 18N + 3  . (201)
We show (see Gumbel N.nb) that for any N ≥ 7, φkk > 0, z∗ k < 1 5 ln2 and
f (N) φkk < βk < min{ fCS(N, φkk), γ(N, φkk,u0 k)},
the right-hand side of (200) is negative and dCSk

z∗ k, βk, φkk,N  > 0 for all z∗ k, where fCS(N, φkk) is
the largest real root of the third degree polynomial ∑3 m=0 ym,kβ m k . Thus, ∂CS∗ k ∂N

 ϕ1=0 < 0.
57

We next verify that ∑3 m=0 ym,kβ m k has three real roots and the largest real root, fCS(N, φkk), is
linear in φkk and can thus be expressed as fCS(N, φkk) =fCS(N)φkk. We define
˘tk := − (N + 1)t (N) φ 2 kk
3 (N6 + 11N5 + 22N4 + 36N3 + 34N2 + 18N + 3)2 ,
˘sk := − 2s (N) φ 3 kk
27 (N6 + 11N5 + 22N4 + 36N3 + 34N2 + 18N + 3)3 , and
˘∆k := − 4δ (N) φ 6 kk
27 (N6 + 11N5 + 22N4 + 36N3 + 34N2 + 18N + 3)4 ,
(202)
where t (N) =∑9 j=0 a jN j, s (N) =∑15 j=0 b jN j, δ (N) =∑16 j=0 c jN j and
{a0, . . . ,a9} = {−32, −328, −1124, −1516, −671,577,740,364,68,4} ,
{b0, . . . ,b15} = {872,10098,45378,102078,118692,39084, −73701, −98271, −22581,50841,61656,34542,11412,2214,216,8} ,
{c0, . . . ,c16} = {−816, −9464, −42275, −92522, −97149, −4202,113985,130285,40882, −40699, −51820, −24692, −4259,1118,729,136,8} .
From (202), it follows that for any N ≥ 7, φkk > 0, then ˘∆k < 0. It thus follows that ∑3 m=0 ym,kβ m k
has three simple real roots given by
˘α j := 2
r
− ˘tk
3 cos
θ + 2 jπ
3

− y2,k
3y3,k
, for j = 0,1,2,
0 < θ < π, and cos (θ ) = − ˘sk/2p
−(˘tk/3)3 .
(203)
From (201) and (203), for φkk < 0, θ = θ (N) is a function of N and is independent of φkk. More-
over,
q
− ˘tk 3 and y2,k 3y3,k are linear in φkk. Thus, for φkk < 0, the three simple real roots of∑3 m=0 ym,kβ m k
can be written as
˘α j = w j(N)φkk. (204)
We can thus write fCS(N, φkk) =fCS (N) φkk, where
fCS(N) = max j=0,1,2 {w j(N)}. (205)
Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), (i) and (ii) in
Proposition 5.3 hold. From (167) and (168), ∂ (CS∗ k)/∂N is a rational function w.r.t. (φbs, φsb).
Moreover, at (φbs, φsb) = (0,0), ∂ (CS∗ k)/∂N is given by (192). Thus, ∂ (CS∗ k)/∂N is continuous
w.r.t. (φbs, φsb) at (0,0). We conclude that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0) ⊂
R2, (i) and (ii) in Proposition 5.3 hold true.
Proof of Proposition 5.4. We want to compute the following quantity when ϕ1 = 0,
∂ π∗ k
∂N = ∂ p∗ k ∂N x∗ k + p∗ k ∂x∗ k ∂N . (206)
58

Using equations (165), (167) and (185), we show (see Gumbel N.nb) that
∂ π∗ k
∂N

ϕ1=0
= nπk

z∗ k, βk, φkk,N,u0 k 
dπk

z∗ k, βk, φkk,N  , (207)
where nπk

z∗ k, βk, φkk,N,u0 k  and dπk  z∗ k, βk, φkk,N  can be written as polynomials in ez∗ k in the
following way,
nπk

z∗ k, βk, φkk,N,u0 k  := 7 ∑
m=2
nm,πkemz∗ k , and
dπk (z∗ k, βk, φkk,N) :=
7
∑
m=0
dm,πkemz∗ k .
(208)
Moreover, the coefficients nm,πk are as follows:
n2,πk = β 3 k  u0 k + βkz∗ k  ,
n3,πk = β 2 k  β 2 k  (5N − 2)z∗ k − 1  + βk  (5N − 2)u0 k − 2z∗ kφkk  − 2u0 kφkk  ,
n4,πk = βk

β 3 k  10N2z∗ k − 2N  4z∗ k + 2  + z∗ k  + β 2 k  10N2 − 8N + 1  u0 k +  z∗ k + 1 − 6Nz∗ k  φkk 
+βk

βk

u0 k (1 − 6N) φkk + z∗ kφ 2 kk  + u0 kφ 2 kk  ,
n5,πk = βk

β 3 k N  10N2z∗ k − 12Nz∗ k − 6N + 3z∗ k  + β 2 k  N  10N2 − 12N + 3  u0 k +  2Nz∗ k + 4N − 1  φkk − 6N2z∗ kφkk  ,
+βk

βkφkk

N (2 − 6N)u0 k +  Nz∗ k + z∗ k + 2  φkk  + (N + 1)u0 kφ 2 kk  ,
n6,πk = βk

β 3 k N2  5N2z∗ k − 2N  4z∗ k + 2  + 3z∗ k  + β 2 k  N2  5N2 − 8N + 3  u0 k +  N2z∗ k − 2N3z∗ k + 5N2 − 2N  φkk  ,
+βk

βkφkkN

−2N2u0 k + Nu0 k +  z∗ k + 2  φkk  +  Nu0 k − 2φkk  φ 2 kk  ,
n7,πk = β 3 k N2  βkN  N2z∗ k − 2Nz∗ k + z∗ k − N  + Nu0 k + 2Nφkk − φkk + N3u0 k − 2N2u0 k  . (209)
The coefficients dm,πk are given by
d0,πk = β 3 k ,
d1,πk = β 2 k (βk (7N − 1) − 4φkk) ,
d2,πk = βk

β 2 k  21N2 − 7N + 1  + 4βk (1 − 5N) φkk + 5φ 2 kk  ,
d3,πk = β 3 k N  35N2 − 20N + 5  + β 2 k  −40N2 + 15N − 1  φkk + βk (15N − 3) φ 2 kk − 2φ 3 kk,
d4,πk = N

β 3 k N  35N2 − 30N + 10  + β 2 k  −40N2 + 21N − 3  φkk + βk (15N − 5) φ 2 kk − 2φ 3 kk  ,
d5,πk = βkN2  β 2 k N  21N2 − 25N + 10  + βk  −20N2 + 13N − 3  φkk + (5N − 1) φ 2 kk  ,
d6,πk = βkN3  β 2 k N  7N2 − 11N + 5  + βk  −4N2 + 3N − 1  φkk + φ 2 kk  ,
d7,πk = β 3 k (N − 1)2 N5. (210)
Because the expressions determining nπk

z∗ k, βk, φkk,N,u0 k  and dπk  z∗ k, βk, φkk,N  are complex,
we focus on finding sufficient conditions for these expressions to have a specific sign for all z∗ k.
(i) Case ∂ π∗ k ∂N

 ϕ1=0 < 0 : We verify in the supplementary fileGumbel N.nb that nπk and dπk (see
(208)) are negative and positive, respectively, if either of the five conditions below, (a-i)-(a-v),
hold:
59

(a-i) φkk < 0, N ≥ 2, 0 < βk < fπ (N, φkk) and z∗ k < rπ,z,1  N, φkk,u0 k, βk  where
rπ,z,1

N, φkk,u0 k, βk  := ∑3 l=0 nπz,lβ l k β 2 k (N2 − 2N3) φkk + β 3 k (5N4 − 8N3 + 3N2) +βkNφ 2 kk (211)
with coefficients given by
nπz,0 = φ 2 kk  −Nu0 k + 2φkk  ,
nπz,1 = Nφkk

2N2u0 k − Nu0 k − 2φkk  ,
nπz,2 = N

−5N3u0 k + 8N2u0 k − 3Nu0 k − 5Nφkk + 2φkk  ,
nπz,3 = 4N3.
(212)
Moreover, fπ (N, φkk) is the largest real root of the third degree polynomial
4β 3 k N3 + β 2 k (2 − 5N)Nφkk − 2βkNφ 2 kk + 2φ 3 kk = 0. (213)
We clarify below that the above polynomial has three real roots and that fπ (N, φkk) is linear
in φkk and can thus be expressed as fπ (N, φkk) =fπ (N) φkk.
(a-ii) φkk < 0, N ≥ 2, βk ≥ fπ (N) φkk and z∗ k < − u0 k βk .
(a-iii) φkk = 0, N ≥ 2, βk > 0 and z∗ k < − u0 k βk .
(a-iv) φkk > 0, N ≥ 2, f (N) φkk < βk ≤ hπ (N) φkk and z∗ k < rπ,z,2  N, φkk,u0 k, βk  where
hπ (N) := (2N − 1) N2 , and (214)
rπ,z,2

N, φkk,u0 k, βk  := −N3u0 k + βkN2 + 2N2u0 k − Nu0 k − 2Nφkk + φkk βk (N3 − 2N2 + N) . (215)
(a-v) φkk > 0, N ≥ 2, and βk > hπ (N) φkk and z∗ k < − u0 k βk .
For completeness, we quickly verify that as stated in (a-i), (213) has three real roots and that
fπ (N, φkk) is linear in φkk. We use Cardano’s condition, for φkk < 0, ˆ∆k := (ˆsk/2)2 + (ˆtk/3)3 < 0,
where
ˆtk := −

49N2 − 20N + 4  φ 2 kk
48N4 , and
ˆsk := (N + 2)

127N2 − 32N + 4  φ 3 kk
864N6 .
(216)
We note that for φkk < 0, fπ (N) satisfies
fπ (N) := max j=0,1,2
 ˆα j
φkk

, (217)
where ˆα j is given by (175), after replacing (tk,sk) by (ˆtk, ˆsk).
60

The five conditions (a-i)-(a-v) can be aggregated into the following single condition: nπk and
dπk are negative and positive, respectively, if(βk, φkk,N) satisfy (19) and z∗ k < gπ,z  N, φkk,u0 k, βk  ,
where
gπ,z

N, φkk,u0 k, βk  :=



rπ,z,1

N, φkk,u0 k, βk  if φkk < 0 and 0 < βk < fπ (N) φkk,
rπ,z,2

N, φkk,u0 k, βk  if φkk > 0 and f (N) φkk < βk ≤ hπ (N) φkk,
−u0 k/βk if φkk = 0 or (φkk < 0 and βk ≥ fπ (N) φkk),
−u0 k/βk if (φkk > 0 and βk > hπ (N) φkk)
(218)
and the quantities rπ,z,1

N, φkk,u0 k, βk  , fπ (N), hπ (N) and rπ,z,2  N, φkk,u0 k, βk  are given by (211),
(217), (214) and (215), respectively.
(ii) Case ∂ π∗ k ∂N |ϕ1=0 > 0. We verify in the supplementary fileGumbel N.nb that nπk and dπk (see
(208)) are positive if either of the two conditions below, (b-i) or (b-ii), hold:
(b-i) φkk ≤ 0, N ≥ 2, βk > 0 and z∗ k > fπ,z  N, φkk,u0 k, βk  , where
fπ,z

N, φkk,u0 k, βk  := rπ,z,2  N, φkk,u0 k, βk  , (219)
and rπ,z,2

N, φkk,u0 k, βk  is given by (215).
(b-ii) φkk > 0, N ≥ 2, βk > gπ (N, φkk) and z∗ k > fπ,z  N, φkk,u0 k, βk  , where gπ (N, φkk) is the unique
real root of the third degree polynomial
β 3 k N3  N2 − 1  + β 2 k N  −7N3 + 10N2 − 5N + 1  φkk + βkN  6N2 − 7N + 3  φ 2 kk − (2N2 − 2N + 1)φ 3 kk.
(220)
We next verify that the above polynomial indeed has a unique real root and that gπ (N, φkk) is
linear in φkk and can thus be expressed as gπ (N, φkk) =gπ (N) φkk. We use Cardano’s condition,
∆k := (sk/2)2 + (tk/3)3 > 0, where
tk := − (31N6−119N5+179N4−135N3+54N2−10N+1)φ 2 kk 3(N−1)2N4(N+1)2 , and
sk := − (362N9−2013N8+4878N7−6728N6+5781N5−3186N4+1117N3−237N2+30N−2)φ 3 kk 27(N−1)3N6(N+1)3 .
Next, we express this solution. For φkk > 0, gπ (N) satisfies
gπ (N) := Car(sk, ∆k) − b2 3 φkk , (221)
where b2 = − (7N3−10N2+5N−1)φkk (N−1)N2(N+1) and Car(·, ·) is given by (181).
Finally, we show that there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), (i) and (ii) in
Proposition 5.4 hold. From (167) and (168), ∂ π∗ k /∂N is a rational function w.r.t. (φbs, φsb). More-
over, at (φbs, φsb) = (0,0), the derivative ∂ π∗ k /∂N is given by (207). Thus, ∂ π∗ k /∂N is continuous
w.r.t. (φbs, φsb) at (0,0). Therefore, there exists ε > 0 such that for any (φbs, φsb) ∈ Bε (0), cases (i)
and (ii) in Proposition 5.4 hold true.
61

References
Anderson, S. P. and De Palma, A. (1992). The logit as a model of product differentiation. Oxford
Economic Papers, 44(1):51–67. (Cited in page 6, 13, 18, 22)
Anderson, S. P., De Palma, A., and Thisse, J.-F. (1992). Discrete choice theory of product differ-
entiation. MIT press. (Cited in page 10)
Armstrong, M. (1996). Multiproduct nonlinear pricing.Econometrica: Journal of the Econometric
Society, pages 51–75. (Cited in page 11)
Armstrong, M. (2006). Competition in two-sided markets. The RAND Journal of Economics ,
37(3):668–691. (Cited in page 3, 4, 10)
Armstrong, M. and Vickers, J. (2001). Competitive price discrimination. The RAND Journal of
Economics, pages 579–605. (Cited in page 2, 11)
Bardey, D., Cremer, H., and Lozachmeur, J.-M. (2014). Competition in two-sided markets with
common network externalities. Review of Industrial Organization , 44:327–345. (Cited in
page 11)
Berry, S. T. (1994). Estimating discrete-choice models of product differentiation. The RAND
Journal of Economics, pages 242–262. (Cited in page 6)
Besanko, D., Gupta, S., and Jain, D. (1998). Logit demand estimation under competitive pricing
behavior: An equilibrium framework. Management Science, 44(11-part-1):1533–1547. (Cited
in page 6)
Bishop, R. L. (1960). Duopoly: Collusion or warfare? The American Economic Review ,
50(5):933–961. (Cited in page 17)
Brander, J. A. and Spencer, B. J. (1985). Tacit collusion, free entry and welfare. The Journal of
Industrial Economics, pages 277–294. (Cited in page 17)
Caillaud, B. and Jullien, B. (2003). Chicken & egg: Competition among intermediation service
providers. The RAND journal of Economics, pages 309–328. (Cited in page 2, 3)
Chica, C., Chuk, K., and Tamayo, J. A. (2021). Exclusive Dealing and Entry by Competing Two-
sided Platforms. Harvard Business School. (Cited in page 3, 8, 10, 11, 13, 24)
Chica, C., Guo, Y ., and Lerman, G. (2024). Artificial intelligence and algorithmic price collusion
in two-sided markets. arXiv preprint arXiv:2407.04088. (Cited in page 23, 24)
Cohen, M. C. and Zhang, R. (2022). Competition and coopetition for two-sided platforms. Pro-
duction and Operations Management, 31(5):1997–2014. (Cited in page 4, 18)
Conlon, C. and Gortmaker, J. (2020). Best practices for differentiated products demand estimation
with pyblp. The RAND Journal of Economics, 51(4):1108–1161. (Cited in page 6)
62

Correia-da Silva, J., Jullien, B., Lefouili, Y ., and Pinho, J. (2019). Horizontal mergers between
multisided platforms: Insights from cournot competition. Journal of Economics & Management
Strategy, 28(1):109–124. (Cited in page 4)
Dewenter, R., Haucap, J., and Wenzel, T. (2011). Semi-collusion in media markets. International
Review of Law and Economics, 31(2):92–98. (Cited in page 4, 17)
Gal-Or, E. (2020). Market segmentation on dating platforms. International Journal of Industrial
Organization, 68:102558. (Cited in page 2)
Gilbert, E. M. (2019). Antitrust and commitment issues: Monopolization of the dating app indus-
try. NYUL Rev., 94:862. (Cited in page 23)
Halaburda, H., Jan Piskorski, M., and Yıldırım, P. (2018). Competing by restricting choice: The
case of matching platforms. Management Science, 64(8):3574–3594. (Cited in page 2)
Hsu, J. and Wang, X. H. (2005). On welfare under cournot and bertrand competition in differenti-
ated oligopolies. Review of Industrial Organization, 27:185–191. (Cited in page 20)
Jeitschko, T. D. and Tremblay, M. J. (2020). Platform competition with endogenous homing.
International Economic Review, 61(3):1281–1305. (Cited in page 4)
Jullien, B. and Pavan, A. (2019). Information management and pricing in platform markets. The
Review of Economic Studies, 86(4):1666–1703. (Cited in page 3)
Lefouili, Y . and Pinho, J. (2020). Collusion between two-sided platforms. International Journal
of Industrial Organization, 72:102656. (Cited in page 4)
Peitz, M. and Sato, S. (2023). Asymmetric platform oligopoly. Technical report, University of
Bonn and University of Mannheim, Germany. (Cited in page 4)
Perloff, J. M. and Salop, S. C. (1985). Equilibrium with product differentiation. The Review of
Economic Studies, 52(1):107–120. (Cited in page 11)
Rochet, J.-C. and Chon ´e, P. (1998). Ironing, sweeping, and multidimensional screening. Econo-
metrica, pages 783–826. (Cited in page 11)
Rochet, J.-C. and Tirole, J. (2003). Platform competition in two-sided markets. Journal of the
European Economic Association, 1(4):990–1029. (Cited in page 1, 3)
Rochet, J.-C. and Tirole, J. (2006). Two-sided markets: a progress report. The RAND Journal of
Economics, 37(3):645–667. (Cited in page 3)
Ryan, C. (2017). Computer and internet use in the United States: 2016. American Community
Survey Reports, ACS-39, U.S. Census Bureau, Washington, DC. (Cited in page 1)
SSRS (2024). The public and online dating in 2024. (Cited in page 2)
Tan, G. and Zhou, J. (2021). The effects of competition and entry in multi-sided markets. The
Review of Economic Studies, 88(2):1002–1030. (Cited in page 2, 3, 4, 5, 8, 10, 11, 15, 18, 20,
21)
63

Tan, H. and Wright, J. (2021). Pricing distortions in multi-sided platforms. International Journal
of Industrial Organization, 79:102732. (Cited in page 13)
Teh, T.-H., Liu, C., Wright, J., and Zhou, J. (2023). Multihoming and oligopolistic platform
competition. American Economic Journal: Microeconomics , 15(4):68–113. (Cited in page 4,
24)
Tirole, J. (1988). The theory of industrial organization. MIT Press. (Cited in page 22)
Tremblay, M. J., Adachi, T., and Sato, S. (2023). Cournot platform competition with mixed-
homing. International Journal of Industrial Organization, 91:103002. (Cited in page 4)
Varian, H. R. (1989). Price discrimination. Handbook of industrial organization , 1:597–654.
(Cited in page 11, 17)
Wells, J. R., Danskin, G., and Ellsworth, G. (2015; revised in 2021). Amazon.com, 2021.Harvard
Business School Case Study 716-402. (Cited in page 1)
Werden, G. J., Froeb, L. M., and Tardiff, T. J. (1996). The use of the logit model in applied
industrial organization. International Journal of the Economics of Business, 3(1):83–105. (Cited
in page 6)
Weyl, E. G. (2010). A price theory of multi-sided platforms. American Economic Review ,
100(4):1642–1672. (Cited in page 3)
White, A. and Weyl, E. G. (2016). Insulated platform competition. Available at SSRN 1694317.
(Cited in page 3, 5)
64
