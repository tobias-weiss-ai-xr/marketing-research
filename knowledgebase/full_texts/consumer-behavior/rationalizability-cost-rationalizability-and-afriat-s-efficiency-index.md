---
title: Rationalizability, Cost-Rationalizability, and Afriat's Efficiency Index
url: https://arxiv.org/abs/2406.10136
category: consumer-behavior
subcategory: empirical
date: 2024-06
venue: ''
authors:
- Matthew Polisson
- John K. -H. Quah
source: arxiv
pdf_url: https://arxiv.org/pdf/2406.10136
pages: 12
chars: 26497
fetched_at: '2026-11-08T13:11:18+00:00'
kb_version: 1
---

# Rationalizability, Cost-Rationalizability, and Afriat's Efficiency Index

arXiv:2406.10136v2  [econ.GN]  19 Jul 2024
Rationalizability, Cost-Rationalizability,
and Afriat’s Eﬃciency Index ∗
Matthew Polisson and John K.-H. Quah †
July 23, 2024
This note explains the equivalence between approximate rat ionalizability and ap-
proximate cost-rationalizability within the context of co nsumer demand. In connection
with these results, we interpret Afriat’s (1973) critical c ost eﬃciency index (CCEI) as
a measure of approximate rationalizability through cost in eﬃciency, in the sense that
an agent is spending more money than is required to achieve he r utility targets.
JEL Codes: D11, D12.
Keywords: rationalizability, cost-rationalizability, Afriat’s eﬃciency index, CCEI.
∗We are grateful to Roy Allen, Thomas Demuynck, Pawel Dziewulski, F ederico Echenique, Georgios
Gerasimou, Ludovic Renou, and Lanny Zrill for helpful comments.
†Emails: matt.polisson@leicester.ac.uk; ecsqkhj@nus.edu.sg.
1

1 Introduction
The notion of rationalizability by utility maximization is natural and normatively uncon-
troversial in the revealed preference literature—a utility function is said to rationalize ex-
penditure data on diﬀerent goods if, at each observation, it assign s weakly higher utility to
the chosen bundle than to any other bundle that is weakly cheaper a t the prevailing prices.
But, in fact, there is an equally natural dual notion which is just as important because it
implicitly justiﬁes many empirical studies of consumer demand and this is the notion of
cost-rationalizability—a utility function is said to cost-rationalize expenditure data on dif-
ferent goods if, at each observation, any bundle that achieves at least as much utility as the
observed bundle must be weakly more expensive.
In this note, we show that these two notions of rationalizabilty are deﬁnitionally equivalent
under mild conditions. We also show that they are observationally equivalent in the sense
that, in a data set with ﬁnitely many observations, both concepts a re characterized by
the generalized axiom of revealed preference (see Afriat (1967), Diewert (1973), and Varian
(1982)). Our results can be seen as analogous to the famous duality between Marshallian and
Hicksian demands as solutions to the (primal) utility maximization and (d ual) expenditure
minimization problems, respectively.
In a suﬃciently rich empirical setting, a data set will rarely be exactly rationalizable
(equivalently, cost-rationalizable) and some way of measuring its de parture from exact ratio-
nalizability is then required. The most common approach in the applied r evealed preference
literature is to calculate Afriat’s (1973) critical cost eﬃciency index (CCEI). While Afriat’s
measure is widely used in empirical applications, its motivation is not alwa ys well understood.
Within the context of the duality between rationalizability and cost-r ationalizability, we ar-
gue that the CCEI could be motivated as a measure of approximate cost-rationalizability.
2 Approximate Rationalizability
At observation t, the prices of ℓ goods are pt and the consumer purchases the bundle xt of
these ℓ goods. We refer to the collection of observations, O = {pt, xt}T t=1, as a data set . We
assume throughout that pt ∈ Rℓ ++ and xt ∈ Rℓ + \ {0}.
2

Definition 1. Let U be a collection of utility functions deﬁned on the consumption space
X ⊆ Rℓ +. The data set O = {pt, xt}T t=1 is rationalizable in U with respect to the vector of
eﬃciency coeﬃcients e = {et}T t=1 (where et ∈ (0, 1] for all t) (or simply e-rationalizable in
U) if there is a utility function U : X → R belonging to U, such that, at every observation t,
U(xt) /greaterorequalslant U(x) for all x ∈ B t(et) = {x′ ∈ X : pt · x′ ⩽ etpt · xt}.
A data set O is said to be exactly rationalizable (or simply rationalizable) in U if it is
(1, 1, . . . ,1)-rationalizable in U.
Loosely speaking, the further is e from (1 , 1, . . . ,1), the weaker is the rationalizability
displayed within the data set. Afriat (1973) proposes the critical cost eﬃciency index (CCEI)
as a measure of a data set’s distance from exact rationalizability.
Definition 2. Given a data set O and a family of utility functions U, the CCEI is given by
sup{e : O is ( e, e, . . . , e)-rationalizable in U }. (1)
To understand what the CCEI means, suppose that a data set O has a CCEI of 0.95
for the family of utility functions U. Then the agent’s observed choices are not exactly
rationalizable in the sense that for any utility function U in U, there is some observation s
and bundle x′ such that U(xs) < U (x′) and ps · x′ ⩽ ps · xs. However, this “irrationality” is
limited in the sense that for any ε > 0 suﬃciently small, there is a utility function ¯U in U
such that ¯U (xt) /greaterorequalslant ¯U (x) for any x satisfying pt · x ⩽ (0.95 − ε)pt · xt for all observations t; in
other words, xt gives weakly higher utility than any bundle that is more than 5% cheape r.
Afriat (1973) provides a way to calculate the CCEI. To be precise, le t ULN S be the
family of locally nonsatiated utility functions deﬁned on X = Rℓ +. It is shown that if O
is e-rationalizable by a member of ULN S, then O must obey a particular property that is
easy to check; furthermore, if a data set satisﬁes this property then it is e-rationalizable by
a member of UW B, the family of well-behaved utility functions, in the sense that the utility
functions are deﬁned on X = Rℓ +, strictly increasing, and continuous. Given this result, a
data set’s CCEI can be obtained via a binary search over e = (e, e, . . . , e), for e ∈ (0, 1], and
3

the CCEI for the family ULN S must coincide with that for the family UW B.
We now introduce the concepts needed to explain Afriat’s result.
Definition 3. Let O = {pt, xt}T t=1 be a data set and e = {et}T t=1 a vector of eﬃciency
coeﬃcients. For any pair of bundles ( xt, xs), the bundle xt is (strictly) directly revealed
preferred to the bundle xs, denoted xt ≽∗ 0 (≻∗ 0) xs, whenever pt · xs ⩽ (<) etpt · xt. For any
ﬁnite sequence of bundles ( xt, xi, xj, . . . ,xl, xs), the bundle xt is revealed preferred to the
bundle xs, denoted xt ≽∗ xs, whenever xt ≽∗ 0 xi, xi ≽∗ 0 xj, . . . , xl ≽∗ 0 xs.
Definition 4. Given a vector of eﬃciency coeﬃcients e = {et}T t=1, a data set O = {pt, xt}T t=1
obeys e-GARP (where GARP stands for the generalized axiom of revealed preference) so long
as xt ≽∗ xs =⇒ xs ⁄≻∗ 0 xt. O satisﬁes GARP if it satisﬁes e-GARP for e = (1, 1, . . . ,1).1
The following result is well known. For proofs, see Afriat (1973) and Halevy, Persitz, and Zrill
(2018). We provide a further proof in the Appendix for the sake of completeness.
Theorem 1. Let O = {pt, xt}T t=1 be a data set and e = {et}T t=1 a vector of eﬃciency
coeﬃcients. The following statements are equivalent:
(1) O is e-rationalizable in ULN S.
(2) O obeys e-GARP.
(3) There is a set of numbers {φt, λt}T t=1 (with φt ∈ R and λt ∈ R++), such that, at all t, s,
φs ⩽ φt + λtpt · (xs − etxt).
(4) O is e-rationalizable in UW B.2
An immediate corollary of this result is that a data set’s CCEI for the f amily of utility
functions ULN S coincides with that for the family UW B and is given by
sup{e : O satisﬁes ( e, e, . . . , e)-GARP}. (2)
1The term GARP is originally from Varian (1982); Afriat (1967) introdu ces and refers to its equivalent
as cyclical consistency, and Afriat (1973) develops a modiﬁed version of this property (wh ich is equivalent
to e-GARP with e = (e, e, . . . , e)).
2Recall that the families ULN S and UW B both contain utility functions which are deﬁned on X = Rℓ +.
Also notice that statement (4) could be strengthened to say that O is e-rationalizable in the family of
well-behaved and concave utility functions.
4

3 Approximate Cost-Rationalizability
Definition 5. Let U be a collection of utility functions deﬁned on the consumption space
X ⊆ Rℓ +. The data set O = {pt, xt}T t=1 is cost-rationalizable in U with respect to the vector
of eﬃciency coeﬃcients e = {et}T t=1 (or simply e-cost-rationalizable in U) if there is a utility
function U : X → R belonging to U, such that, at every observation t,
etpt · xt ⩽ pt · x for all x ∈ P t = {x′ ∈ X : U(x′) /greaterorequalslant U(xt)}.
A data set O is said to be exactly cost-rationalizable (or simple cost-rationalizable) in U if
it is (1 , 1, . . . ,1)-cost-rationalizable in U.
Exact cost-rationalizability means that there is some utility function U in U for which
the bundle chosen by the agent at each observation t could be understood as the cheapest
way of achieving a utility target U(xt) given the prevailing prices pt.3
The next proposition relates e-rationalizability and e-cost-rationalizability.
Proposition 1. (a) If a locally nonsatiated utility function U : Rℓ + → R e-rationalizes
O, then U also e-cost-rationalizes O. (b) If a continuous utility function U : Rℓ + → R
e-cost-rationalizes O, then U also e-rationalizes O.
Proof. If (a) is false then there is an observation t and a bundle y such that U(y) /greaterorequalslant U(xt)
with etpt · xt > pt · y. Since U is locally nonsatiated, there is y′ such that U(y′) > U (y) /greaterorequalslant
U(xt), with etpt · xt > pt · y′, which contradicts the e-rationalizability of O by U.
For (b), we again prove by contradiction. Suppose that U e-cost-rationalizes O but that
there is an observation t and a bundle y such that U(y) > U (xt) with pt · y ⩽ etpt · xt. By
the continuity of U and the fact that etpt · xt > 0, there is y′ such pt · y′ < e tpt · xt and
U(y′) > U (xt), but this is impossible since U e-cost-rationalizes O.
We know (from Theorem 1) that e-GARP is suﬃcient for e-rationalizability by a utility
function U belonging to UW B, and therefore (by Proposition 1a) it is also suﬃcient for e-
3See also the related notion of cost-rationalizability within the contex t of production in Afriat (1972),
Hanoch and Rothschild (1972), and Varian (1984). One important d iﬀerence between production and con-
sumption is that output levels are observed in the former, while utility targets are unobserved in the latter.
5

cost-rationalizability by a utility function U belonging to UW B. The necessity of e-GARP is
stated formally below.
Proposition 2. O obeys e-GARP whenever any of the following conditions holds:
(i) O is e-rationalizable and e-cost-rationalizable in U, where U is a collection of utility
functions U : X → R deﬁned on the consumption space X ⊆ Rℓ +.
(ii) O is e-rationalizable by a locally nonsatiated utility function U : Rℓ + → R.
(iii) O is e-cost-rationalizable by a continuous utility function U : Rℓ + → R.
Proof. In view of Propositon 1, (ii) and (iii) follow once we prove (i). So we prov e (i).
Indeed, if pt · xs = etpt · xt, then U(xs) ⩽ U(xt) since U e-rationalizes O. Furthermore,
if pt · xs < e tpt · xt, then U(xs) < U (xt) since U is e-cost-rationalizes O. Therefore, if
xt ≽∗ xs then U(xt) /greaterorequalslant U(xs) and so xs ⁄≻∗ 0 xt, as required by e-GARP (otherwise, we obtain
U(xs) > U (xt), which is a contradiction).
Polisson and Quah (2013) studies a family of utility functions U deﬁned on a discrete
consumption space X. Part (i) of Proposition 2 guarantees that GARP holds if a data set
is rationalizable and cost-rationalizable by a utility function in U; the authors show that
GARP is also suﬃcient to guarantee the existence of a strictly increa sing utility function
deﬁned on X that rationalizes and cost-rationalizes the data set.
An implication of Proposition 2 is that, for the family of well-behaved ut ility functions
UW B, e-rationalizability and e-cost-rationalizability are observationally equivalent because
they are both equivalent to e-GARP. Similarly, the CCEI (for U = UW B) as deﬁned by (1),
which is equal to (2), is also equal to
sup{e : O is ( e, e, . . . , e)-cost-rationalizable in U }. (3)
This identity gives us a diﬀerent way of interpreting the CCEI beyond its deﬁnition.
6

4 Cost-Rationalizability and the CCEI
First, we argue that when analyzing observational data , it is reasonable to require both
rationalizability and cost-rationalizability as rationality criteria. This is because, typically,
the researcher would simply have access to just a fraction of the p urchases made by the
consumer. Even if the consumer did have an exogenously given budg et, it is unlikely that
all the goods on which that budget is spent are actually part of the r esearcher’s observation.
For example, xt could be the consumer’s purchases of food products from a groce ry store.
The data set O = {pt, xt}T t=1 is cost-rationalizable if there is a utility function U deﬁned
on those ℓ goods (properly speaking, a sub-utility function, since her consumption decisions
will cover many other (unobserved) goods) so that, at each obse rvation t, the bundle xt is
the cheapest way of achieving utility level U(xt). This is a reasonable rationality criterion
to impose since we would expect the consumer to be cost eﬃcient in he r purchases of the ℓ
goods, in order to maximize the money available for purchases of the non-ℓ goods.
In the context of cost-rationalizabilty, what does it mean for a con sumer to have a CCEI
of (say) 0.9? This means that for any e′ = 0 .9 − ε with ε > 0 suﬃciently small, O is cost-
rationalizable with respect to ( e′, e′, . . . , e′). Then there is a well-behaved utility function U
deﬁned on the ℓ goods, such that there is no observation t at which the agent could have saved
more than 100(0 .1 +ε)% of her observed expenditure pt · xt while achieving utility U(xt). In
other words, there could be one (or more) observation(s) at whic h she is spending more than
is necessary given her utility target, but the cost saving is not mate rially greater than 10% at
any observation. Furthermore, given that 0.9 is the supremum amo ng all possible values of e
at which O is ( e, e, . . . , e)-cost-rationalizable, for any well-behaved utility function U, there
must be at least one observation s such that the agent could have achieved utility U(xs) and
saved more than 100(0 .1 − ε)% of her observed expenditure ps · xs.
Now consider analyzing laboratory data, and suppose that a subject’s data set is exactly
rationalizable. Then the data set is also exactly cost-rationalizable, which means there is
a utility function for which the subject will be strictly worse oﬀ should the experimenter
give the subject a smaller budget (less of the experimental curren cy) in any one round. The
CCEI is a measure of how close the subject is to exact cost-rationa lizability. A CCEI of 0.9
7

means that, for a subject with any well-behaved utility function, there will be one round
(and possibly more) in which the subject could have achieved the sam e utility in that round
with a budget that is 100(0 .1 − ε)% smaller. However, for any withdrawal of 100(0 .1 + ε)%
of the budget, there is a well-behaved utility function such that a su bject with such a utility
function is strictly worse oﬀ in some round.
We should emphasize that in the deﬁnition of approximate cost-ratio nalizability, the
target utility is contingent on the observation t (or, if we interpret t as time, contingent on
time t). The deﬁnition does not require that there is not a cheaper way of achieving the same
set of utility levels, possibly after altering the observation at which a par ticular utility level is
obtained. For example, consider a data set where p1 = (1, 1) and x1 = (1, 1) at observation
1 and p2 = (2, 2) and x2 = (2, 2) at observation 2. This data set is rationalizable and cost-
rationalizable (because it obeys GARP), but clearly the agent could s ave money if he had
bought the bundle x2 = (2, 2) at the prices p1 = (1, 1) and the bundle x1 = (1, 1) at the prices
p2 = (2 , 2). This does not contradict cost-rationalizability because cost-r ationalizability
allows the agent to choose the timing of the utility targets. This grea ter permissiveness
makes sense: observation 1 could be on food spending in normal time s and observation 2 on
food spending during a festive period; cost-rationalizability does no t preclude the possibility
of the agent choosing to derive higher utility from food during a fest ive period (even when
food prices are higher) and lower utility from food in normal times (ev en when food prices are
lower). In essence, cost-rationalizability respects the price-bun dle pairs within observations,
leaving open the possibility that prices/expenditures are in fact endogenous.
5 Discussion
Approximate rationalizability through cost ineﬃciency was ﬁrst intro duced within the con-
text of production (Afriat, 1972) and then consumption (Afriat, 1973).4 The intuition be-
hind cost ineﬃciency in production is strong, 5 and our objective in this note is to provide an
equally strong intuition for cost ineﬃciency within the context of con sumer demand. This
in turn furnishes an intuitive interpretation for Afriat’s (1973) crit ical cost eﬃciency index
4Debreu (1951) also expresses a similar idea within the context of an e xchange economy.
5A cost ineﬃcient combination of inputs means that the same level of o utput can be achieved through a
diﬀerent combination of inputs which costs strictly less at the preva iling factor prices.
8

(CCEI) which may be useful for researchers in revealed preferen ce. The CCEI is by far the
most widely used index for measuring the degree of rationality in a dat a set and as such
has received considerable attention, including some criticism (see, f or example, Echenique
(2022)). Whatever arguments there might be for and against, we do not see any interpretive
diﬃculties with this index. Besides our interpretation, another (mor e “psychological”) inter-
pretation of the index based on a consumer’s innate inability to disting uish among similar
bundles is found in Dziewulski (2020).
Our interpretation of the CCEI in terms of approximate cost-ratio nalizability remains
valid when the index is applied to other classes of utility functions which are narrower than
UW B. Note that one of the strengths of this index is the ease with which it could be calculated
for other classes of utility functions. For example, in Polisson, Quah , and Renou (2020),
CCEIs are calculated for a wide range of models of decision making with in the context
of choice under risk (e.g., expected utility ( UEU T ), disappointment aversion ( UDA), rank
dependent utility ( URDU ), and stochastically monotone utility ( UF OSD)) with and without
concavity of the Bernoulli function. 6 It could also be estimated when U is a fully parametric
class of utility functions, e.g., expected utility with constant relative risk aversion (CRRA).
We note that one could interpret the CCEI as just one way of aggregating the eﬃ-
ciency coeﬃcients e into a rationality index or score. Other prominent aggregators of
e include the Varian (1990) and Houtman and Maks (1985) indices; see the discussions
in Halevy, Persitz, and Zrill (2018) and Polisson, Quah, and Renou (2 020). The CCEI is
the one most commonly used in empirical work, 7 primarily because it is easy to calculate
in a practical sense. 8 There are also other ways of measuring departures from rational-
ity that could not be thought of as simply diﬀerent ways of aggregat ing e; this includes
Echenique, Imai, and Saito (2020, 2023) and de Clippel and Rozen (2 023) (which are based
on ﬁrst-order conditions), Echenique, Lee, and Shum (2011) (wh ich leverages the idea of a
6The approach could also be applied straightforwardly to many promin ent models of decision making
under uncertainty and over time, which are formally very similar to mo dels of decision making under risk
(see Polisson, Quah, and Renou (2020)).
7See, for just a few examples, Harbaugh, Krause, and Berry (200 1), Andreoni and Miller (2002),
Choi et al. (2007, 2014), Fisman, Kariv, and Markovits (2007), and Carvalho , Meier, and Wang (2016).
8The Afriat (1973) index can be calculated eﬃciently using a binary sea rch algorithm for a wide class of
utility models (see Polisson, Quah, and Renou (2020) and Dembo et al. (2024)), whereas the Varian (1990)
and Houtman and Maks (1985) indices are known to be more computa tionally demanding, and especially
when U is not simply UW B.
9

“money pump”), and Hu et al. (2021) (which is based on the size of perturbations of observed
demand bundles).
Appendix
Proof of Theorem 1. (1) = ⇒ (2): The e-rationalizability of O by U in ULN S guarantees
that pt · xs ⩽ etpt · xt =⇒ U(xt) /greaterorequalslant U(xs) and pt · xs < e tpt · xt =⇒ U(xt) > U (xs). The
ﬁrst implication follows directly from the deﬁnition of e-rationalizability of O by U, and the
second from the deﬁnition of e-rationalizability plus the local nonsatiation of U.9 Therefore,
for any pt · xi ⩽ etpt · xt, pi · xj ⩽ eipi · xi, . . . , pl · xt ⩽ elpl · xl, we obtain
U(xt) /greaterorequalslant U(xi) /greaterorequalslant U(xj) /greaterorequalslant · · · /greaterorequalslant U(xl) /greaterorequalslant U(xt),
which of course implies that U(xt) = U(xi) = U(xj) = · · · = U(xl) = U(xt). This equality
then equires that pt · xi = etpt · xt, pi · xj = eipi · xi, . . . , pl · xt = elpl · xl. In other words,
for any revealed preference cycle xt ≽∗ 0 xi, xi ≽∗ 0 xj, . . . , xl ≽∗ 0 xt, the weak relation ≽∗ 0
cannot be replaced with the strict relation ≻∗ 0 anywhere in the cycle.
(2) = ⇒ (3): Deﬁne at,s = pt · (xs − etxt) for all t, s, and let A be a T × T square matrix
with at,s the (t, s)-th entry. Since O satisﬁes e-GARP, A satisﬁes cyclical consistency in the
sense deﬁned in Forges and Minelli (2009), which guarantees that t here is a set of numbers
{φt, λt}T t=1 (with φt ∈ R and λt ∈ R++), such that, at all t, s, φs ⩽ φt + λtat,s.
(3) = ⇒ (4): The construction argument used here follows Afriat (1973). For any x
deﬁne U(x) = min t{φt +λtpt ·(x−etxt)}, and notice that U is strictly increasing, continuous,
and concave. First, we must have U(xt) /greaterorequalslant φt. To see this, suppose that U(xt) < φ t; then
U(xt) = φm + λmpm · (xt − emxm) < φ t, contradicting (3). Second, for any x satisfying
pt·x ⩽ etpt ·xt, we have φt /greaterorequalslant φt+λtpt·(x−etxt) since λt > 0, and U(x) ⩽ φt+λtpt ·(x−etxt)
by the deﬁnition of U. Taken altogether,
U(xt) /greaterorequalslant φt /greaterorequalslant φt + λtpt · (x − etxt) /greaterorequalslant U(x).
9To see the latter, suppose that pt · xs < e tpt · xt =⇒ U (xt) = U (xs). (From the e-rationalizability of
O by U , pt · xs < e tpt · xt =⇒ U (xt) /greaterorequalslant U (xs).) Then by the local nonsatiation of U , there must be some
bundle y such that pt · y < e tpt · xt and U (y) > U (xs) = U (xt), contradicting e-rationalizability.
10

(4) = ⇒ (1): This is obvious since every well-behaved utility function is (by deﬁ nition)
strictly increasing and thus locally nonsatiated.
References
Afriat, S. N. 1967. “The Construction of Utility Functions f rom Expenditure Data.” International
Economic Review 8(1): 67–77.
———. 1972. “Eﬃciency Estimation of Production Functions.” International Economic Review
13(3): 568–598.
———. 1973. “On a System of Inequalities in Demand Analysis: A n Extension of the Classical
Method.” International Economic Review 14(2): 460–472.
Andreoni, J. and J. Miller. 2002. “Giving According to GARP: An Experimental Test of the
Consistency of Preferences for Altruism.” Econometrica 70(2): 737–753.
Carvalho, L. S., S. Meier, and S. W. Wang. 2016. “Poverty and E conomic Decision-Making: Evi-
dence from Changes in Financial Resources at Payday.” American Economic Review 106(2): 260–
284.
Choi, S., R. Fisman, D. Gale, and S. Kariv. 2007. “Consistenc y and Heterogeneity of Individual
Behavior under Uncertainty.” American Economic Review 97(5): 1921–1938.
Choi, S., S. Kariv, W. M¨ uller, and D. Silverman. 2014. “Who I s (More) Rational?” American
Economic Review 104(6): 1518–1550.
de Clippel, G. and K. Rozen. 2023. “Relaxed Optimization: Ho w Close Is a Consumer to Satisfying
First-Order Conditions?” Review of Economics and Statistics 105(4): 883–898.
Debreu, G. 1951. “The Coeﬃcient of Resource Utilization.” Econometrica 19(3): 273–292.
Dembo, A., S. Kariv, M. Polisson, and J. K.-H. Quah. 2024. “Ev er Since Allais.” Unpublished
paper.
Diewert, W. E. 1973. “Afriat and Revealed Preference Theory .” Review of Economic Studies
40(3): 419–425.
Dziewulski, P. 2020. “Just-Noticeable Diﬀerence as a Behavi oural Foundation of the Critical Cost-
Eﬃciency Index.” Journal of Economic Theory 188: 105071.
Echenique, F. 2022. “On the Meaning of the Critical Cost Eﬃci ency Index.” Unpublished paper.
Echenique, F., T. Imai, and K. Saito. 2020. “Testable Implic ations of Models of Intertemporal
Choice: Exponential Discounting and Its Generalizations. ” American Economic Journal: Mi-
croeconomics 12(4): 114–43.
———. 2023. “Approximate Expected Utility Rationalization .” Journal of the European Economic
Association 21(5): 1821–1864.
Echenique, F., S. Lee, and M. Shum. 2011. “The Money Pump as a M easure of Revealed Preference
Violations.” Journal of Political Economy 119(6): 1201–1223.
11

Fisman, R., S. Kariv, and D. Markovits. 2007. “Individual Pr eferences for Giving.” American
Economic Review 97(5): 1858–1876.
Forges, F. and E. Minelli. 2009. “Afriat’s Theorem for Gener al Budget Sets.” Journal of Economic
Theory 144(1): 135–145.
Halevy, Y., D. Persitz, and L. Zrill. 2018. “Parametric Reco verability of Preferences.” Journal of
Political Economy 126(4): 1558–1593.
Hanoch, G. and M. Rothschild. 1972. “Testing the Assumption s of Production Theory: A Non-
parametric Approach.” Journal of Political Economy 80(2): 256–275.
Harbaugh, W. T., K. Krause, and T. R. Berry. 2001. “GARP for Ki ds: On the Development of
Rational Choice Behavior.” American Economic Review 91(5): 1539–1545.
Houtman, M. and J. A. H. Maks. 1985. “Determining All Maximal Data Subsets Consistent with
Revealed Preference.” Kwantitatieve Methoden 6(19): 89–104.
Hu, G., J. Li, J. K.-H. Quah, and R. Tang. 2021. “A Theory of Rev ealed Indirect Preference.”
Unpublished paper.
Polisson, M. and J. K.-H. Quah. 2013. “Revealed Preference i n a Discrete Consumption Space.”
American Economic Journal: Microeconomics 5(1): 28–34.
Polisson, M., J. K.-H. Quah, and L. Renou. 2020. “Revealed Pr eferences over Risk and Uncertainty.”
American Economic Review 110(6): 1782–1820.
Varian, H. R. 1982. “The Nonparametric Approach to Demand An alysis.” Econometrica 50(4): 945–
973.
———. 1984. “The Nonparametric Approach to Production Analy sis.” Econometrica 52(3): 579–
597.
———. 1990. “Goodness-of-Fit in Optimizing Models.” Journal of Econometrics 46(1-2): 125–140.
12
