---
title: Price of Anarchy of Algorithmic Monoculture
url: https://arxiv.org/abs/2604.00444
category: digital-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Robert Kleinberg
- Erald Sinanaj
- Éva Tardos
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.00444
pages: 27
chars: 67017
fetched_at: '2026-11-08T13:04:26+00:00'
kb_version: 1
---

# Price of Anarchy of Algorithmic Monoculture

Price of Anarchy of Algorithmic Monoculture
Robert Kleinberg, Erald Sinanaj, and Éva Tardos
Cornell University, Ithaca NY, USA
rdk@cs.cornell.edu, erald@cs.cornell.edu, eva.tardos@cornell.edu
Abstract. Several recent works investigate the effects ofmonoculture,
the ever increasing phenomenon of (possibly) self-interested actors in
a society relying on one common source of advice for decision making,
with an archetypal driving example being the growing adoption and
predictive power of machine learning models in matching markets, e.g. in
hiring. Kleinberg and Raghavan (PNAS, 2021) introduced a model that
captures the effects of monoculture in a one-sided matching market with
advice, demonstrating that a higher accuracy common signal (such as
an algorithmic vendor) might incentivize society as a whole to rationally
adopt it, but as a collective it would be better off if each instead adopted
less accurate, but private advice. We generalize their model and address
the open question of their work in quantifying thesocial welfare loss. We
find that monoculture and more generally decentralized optimization is
close to optimal: we show a tight constant bound of 2 on the price of
anarchy (and more general notions) for the induced game.
1 Introduction
Algorithmic monoculture describes the now prevalent pattern of collective reliance
on algorithmically curated advice. While the predictive power of algorithms and
machine learning models usually outclasses traditional means, convergence and
over-dependence can lead to detrimental effects in social welfare [14, 17, 11] and
fairness concerns over outcome homogenization [21, 6, 2].
Our work considers a one-sided matching market under limited advice and
specifically a model that is directly influenced by the one introduced by Kleinberg
and Raghavan in [14], that kick-started the study of the effects of algorithmic
monoculture. The motivation stemmed from the setting ofalgorithmic hiring: in
their model a number of firms each seek to hire one candidate out of a pool of
many, sharing a common ground truth valuation. However, they do not know
a priorithis valuation (or future performance). To the aid of their decisions,
they have access to a public algorithmic vendor, that relays a single shared noisy
ranking to any who choose to view it, and a private human advisor (employee)
that also produces a ranking for their corresponding firm, independently of any
other. They model both of them as ranking distributions of the same family,
parameterized by an accuracy term; the algorithm is more accurate than a human
advisor. Each firm chooses either the algorithm or the human for advice, and
they proceed in random order to hire the top remaining candidate in the ranking
they received.
arXiv:2604.00444v1  [cs.GT]  1 Apr 2026

2 R. Kleinberg, E. Sinanaj and É. Tardos
The theme of [14] is, as they state, a counterintuitive fact: the choice of
the algorithm might be a dominant strategy for each firm, but welfare and
thus average utility might be better if every firm instead used the less accurate
human evaluator. They show this to be the case for two firms, under some
natural assumptions, and experimentally verify that this phenomenon can arise
for multiple firms as well. However, this surprising qualitative conclusion does
not shed light to the degree of the negative effect that monoculture impacts.
Our work is devoted to providing a measure to this welfare loss, resolving their
open question with a rather reassuring answer: monoculture (and more generally
selfish behavior) is not that bad. We show that theprice of anarchyfor this game
is 2 (which is asymptotically tight), foranynumber of agents andanynumber of
“advice sources”, thus bounding the welfare loss even when there is no dominant
strategy (and we also extend this for more general notions of equilibria).
We show this to be the case for a generalization of their model, substantially
relaxing the assumptions about the structure of the advice acquisition and the
relevant ranking distributions, which allows us to apply our findings to a much
broader landscape, capturing a wealth of realistic scenarios. The properties we
seek for the advice sources are attained by a very rich class of distributions,
which we termSchur-concaverankings; as an example, any ranking produced
by additive i.i.d. noise falls under this class, whenever the noise distribution is
log-concave(with two examples being the Gaussian and Laplacian, considered in
[14]). We also show that the quite well known Mallow’s Model rankings enjoy the
same properties that lead to our bounds. As previously mentioned, our results
do not assume the existence of a dominant strategy and allow for arbitrary
asymmetry between the firms, specifically any number and combination of unique
idiosyncratic and ‘common’ signals. Furthermore, we extend our results to a
more realistic mechanism, that allows for more expressive strategic behavior
and we show that under minimal assumptions a firm does not have tostrategize
any differently from the previous model. In addition, our main results assume
a condition which roughly states that for any two candidates it is more likely
that their relative order is correct, rather than not. For environments that are
systemicallybiased, in that advice sources may violate this property, we provide
price of anarchy bounds that scale gracefully with the degree of violation of this
condition.
The paper is structured as follows. In the immediately succeeding section
we discuss related work. In Section 3 we formalize specifics of our problem. In
Section 4 we show our main result; a constant price of anarchy. In Section 5 we
discuss the generality of our assumptions and the strategic extension. In Section 6
we establish that our price of anarchy bound is tight and show that if the natural
assumption we impose on the rankings is arbitrarily violated, the price of anarchy
becomes unbounded. Finally, in Section 7 we introduce the relaxation of our
condition on rankings, and go on to provide a price of anarchy bound which
degrades in a controlled manner, as a function of the extent to which the original
assumption is violated.

Price of Anarchy of Algorithmic Monoculture 3
2 Related Work
A number of recent papers explore the theme ofalgorithmic monoculture, address-
ing various questions about the impacts of substituting algorithmically-derived
rankings and recommendations for human preferences in strategic settings. These
works typically model the algorithmically-derived preferences as more accurate
(which tends to improve social welfare) but less varied (which tends to reduce
social welfare), leading to subtle questions about which of these effects predomi-
nates. This phenomenon was explored in the setting of one-sided matching by
Kleinberg and Raghavan [14], in two-sided matching markets by Peng and Garg
[17], and in the setting of competing classifiers by Jagadeesan et al. [11]. While
each of the aforementioned papers introduces examples of settings in which algo-
rithmic monoculture leads to reduced social welfare, to the best of our knowledge
the present work is the first to bound the worst-case social welfare loss due to
algorithmic monoculture. We establish such bounds in a one-sided matching
model directly inspired by [14].
The model of one-sided matching we investigate assumes that the mechanism
used is Random Serial Dictatorship (also known as Random Priority). While
the price of anarchy of one-sided matching mechanisms, including Random
Serial Dictatorship, has been investigated in several prior works, the model we
study differs in two key respects. First, it is a common value environment: any
candidate has the same value to all agents. Consequently, the social welfare of
a matching depends only on the set of candidates matched, rendering price-of-
anarchy questions vacuous in the special case when candidates and agents are
equinumerous. Second, most importantly, the agents in our model are uncertain
of the candidates’ values. In fact, the main strategic decision they face is not
which candidate to select, but whichsignalto obtain in order to advise their
ranking of the candidates.
In the classical model of matching when firms have private values for the
candidates, for markets with an equal number of agents and candidates, under a
standard unit-sum normalization assumption on agents’ values, Christodoulou
et al. [7] obtained a tight bound ofΘ(√n)on the price of anarchy of both Random
SerialDictatorshipandanotherwidely-studiedmechanism,theProbabilisticSerial
mechanism of Bogomolnaia and Moulin [5]. Other earlier works had focused on
welfare guarantees for truthful mechanisms [1, 10] and some investigated novel
measures of welfare [4]. Jiang et al. [12] analyzed the price of anarchy of one-sided
matching mechanisms in asymmetric markets where candidates may outnumber
agents. In particular, they showed that the price of anarchy in markets withn
agents can be asymptotically greater than√n when the number of candidates is
sufficiently large compared ton.
3 Setup
Game specificationThere are n firms (agents) with a shared but unknown
cardinal preference overm candidates (items) and a unit demand over them. Any

4 R. Kleinberg, E. Sinanaj and É. Tardos
candidate awards a firm some non-negative utility or value. Firms have access to
ranking technologies(advice sources). Each firm chooses one such technology, from
those available to her and receives a ranking sample, not necessarily independent
of one another firm receives (below we discuss this in further length).Random
Serial Dictatorshipdictates the order in which each firm is called: nature draws a
uniformly random ordering and each firm is called in that order. When a firm is
called, she receives the top remaining candidate from her chosen ranking and this
is public knowledge. This is the setting of [14], which we will mostly focus on; we
will call this mechanismObedience-constrainedRandom Serial Dictatorship. We
will also investigate a less strict mechanism, which is identical to the previous
but different in one important aspect: a firm can decide freely about her choice
of a candidate when it’s her turn. We will call this mechanismUnconstrained
Random Serial Dictatorship. More discussion about the unconstrained model
will follow in Section 5; unless explicitly stated, all definitions and claims will be
for the former model.
Ranking technologiesA ranking technology is a distribution on rankings of
candidates (permutations of the set[m] :={1, . . . , m}). There exists acommon
signal space A of independent ranking technologies, such that if any two firms
choose the same strategy from A they receive the same sample. Each firm
has access to some arbitrary subset Ai ⊂ Aand anidiosyncraticspace of
independent ranking technologiesHi, which is mutually disjoint between firms,
(that is Hi ∩ Hj = ∅ for i̸ = j). We note that ranking technologies are mutually
independent (for any realization of the candidate values). The action space of
the firms in line with the model of Kleinberg and Raghavan [14] corresponds to
A and Hi being singleton sets, withAi = A and each idiosyncratic technology
being identically (but independently) distributed. The pure strategy space is the
set S := ×i∈[n]Ri (with Ri := Ai ∪ Hi). Further, we will refer toR := S i∈[n] Ri
as theadvice spaceof the game.
Valuations, welfare and notationCandidates are identified with indices
i∈ [m]and their value x(i). The joint value vectorxis drawn from some
distribution X supported on a subset of[0,∞ )m. Whenever we have a ranking
technology R we will usually denote withr= ( r1, . . . , rm)the ranking (i.e.,
permutation of[ m]) sampled from the corresponding distributionFR(x). If C
is some subset of[m],r −C will denote the partial ranking induced by removing
the candidates inC from consideration. Thus, in line with the previously defined
notation, r−C i denotes the i-th ranked candidate in the corresponding ranking
(whenever it’s well defined). We will usually denote a pure profile by the letter
s ∈ S. The utility ui(s)of some firm in profilesis the expected value of the
candidate she hires and the social welfareSW (s)is the usualutilitarianone (the
utility sum). A socially optimal profile is one that maximizes the social welfare.
The Price of Anarchy [15] is the ratio of the optimal welfare to the worst-case
Nash equilibrium welfare.

Price of Anarchy of Algorithmic Monoculture 5
4 The price of anarchy
Before we state our main result we define a very natural property that we would
like a ranking technology to have.
Definition 1(Stochastically Consistent).A ranking technologyR isstochas-
tically consistentiff the following holds for all indicesi < j∈[m]and candidates
k, ℓ∈[m]. The factx(k)≥x(ℓ)implies that:
Pr∼FR(x)

(ri, rj) = (k, ℓ)

 r−{k,ℓ}  ≥P r∼FR(x)  (ri, rj) = (ℓ, k)

 r−{k,ℓ}  a.s.
That is, the ranking obeys a notion ofindependence of irrelevant alternatives:
conditioned on two candidatesk and ℓ being ranked at two specific spots (i and
j) in any order, and conditioned on the set of candidates ranked in some other
arbitrary positions, it is more probable that the ranking correctly represents the
relative order of the aforementioned pair, rather than not. In Section 5 we show
how deceivingly broad it is; demonstrating that it captures almost any natural
ranking distribution one can think of and the wealth of those studied in the
literature.
We extend this definition, declaring anadvice spacestochastically consistent
when all its ranking technologies are stochastically consistent. Our main result is
the following favorable conclusion about the social welfare loss of monoculture
and more generally of any Nash equilibrium.
Theorem 1. The Price of Anarchy of the Obedience-Constrained Random Serial
Dictatorship mechanism, in which firms obtain their rankings from a stochastically
consistent advice space, is bounded above by 2.
Before presenting the full proof of the theorem, we sketch the intuition behind
the result. An initial observation is that, since agents have shared (cardinal)
preferences in our model, the total utility of all agents is equal to the total value
of the candidates hired. The main idea of the proof is to consider two cases,
depending on the total value of the candidates that each firm gets in the socially
optimal profiles ∗, but would have been “taken” from them in the equilibrium
profilesby the firms that went before her. The value of this set of candidates
will be denoted in the proof byW (β) snatched(s∗, s), where β is the order of the firms.
If its expectation is at least half that of the optimum social welfare, then clearly
the price of anarchy is bounded above by two. Otherwise, at least half of the
expected total value of the candidates hired in the socially optimal profile must
be attributable to candidates that would not be “taken” by those before the
respective firm in the equilibrium profile.
Thus, in the second case, if a firm at random in the equilibrium had unilaterally
deviated to her strategy in the optimal profile, she would be expected to do
reasonably well by at least gaining a fraction of this “unshared” welfare, assuming
that rankings are “well behaved” enough (which we discuss immediately below).
The argument concludes by recalling the definition of the equilibrium; the social

6 R. Kleinberg, E. Sinanaj and É. Tardos
welfare of the equilibrium should upper bound the total expected utility of every
such firm unilaterally deviating to this strategy.
The next lemma establishes the “well behaved” property of the rankings
that we need for our argument to hold and shows that it is the case for our
modeling assumptions. In short, we claim thatstochastic consistencyof the
ranking strategies implies the following fact. For any two pure strategy profiless,
s∗, conditioned on the order of firms beingβ, whenever the random candidate
that firmi hires in profiles∗ is not selected by the firms before her ins, she would
have done as well or better (than her result in the optimal profiles∗), competing
in profiles, if she was usings∗ i. While this idea is intuitive, it turns out to not
be the case in general: in some cases a higher ranked candidate being available
may correlate with the value of the candidate being poor in expectation. We
show that our intuition is true however, when the advice space is stochastically
consistent. The proof of the statement below can be found in the Appendix.
Lemma 1. Consider an Obedience-Constrained Random Serial Dictatorship
mechanism with a stochastically consistent advice space. Letc(β) i (s)denote the
candidate hired by firm i in profileswhen the order of firms is β. Let also
x(β) i (s) :=x(c(β) i (s))be the value of this candidate. Further, defineC (β) i (s)to be
the set of candidates hired by the firms going beforeiin profiles.
For any two pure strategy profiless,s∗ the below holds:
E
h
x(β) i (s∗ i ,s −i)−x (β) i (s∗)

 x, β, c(β) i (s∗)/∈C (β) i (s) i ≥0
where the expectation is over the randomness of the samples drawn from the
ranking technologies andxrepresents the joint value vector of the candidates.
Now we are ready to prove our main result.
Proof (Theorem 1).Consider a pure strategy profile s = (s1, . . . , sn). The
outcome of the selected candidates depends on the rankings sampled from the
technologies adopted by the agents, but also on the orderβ that Random Serial
Dictatorship draws (and the random candidate valuesx). Let the socially optimal
profile be s∗ and define the following quantity the we previously described
informally:
W (β) snatched(s∗,s) :=E

 X
i∈[n]
x(β) i (s∗)·1  c(β) i (s∗)∈C (β) i (s) 

 RSD order=β  
(Note that whenβ(i) = 1we haveC (β) i (s) =∅ and thus these terms are zero.)
Similarly, define:
W (β) available(s∗,s) :=E

 X
i∈[n]
x(β) i (s∗)·1  c(β) i (s∗)/∈C (β) i (s) 

 RSD order=β  

Price of Anarchy of Algorithmic Monoculture 7
To illustrate this, consider the example in Figure 1. Suppose the order of the
firms is fixed, and in that order from top to bottom we have, on the left, the
candidates hired in profiles, and on the right, those hired in profiles∗. We have
colored the candidates hired ins∗ either green or red. A green-colored candidate
is one that would be still available to the corresponding firm in profiles, while a
red-colored candidate is one would have been “snatched" from the corresponding
firm, in profilesand not available to be hired.
Fig. 1.Candidates E and S are snatched, while A, B, D are available to the corresponding
firms.
Another way to defineW (β) snatched(s∗, s)and W (β) available(s∗, s)is the following.
Consider the two (random) random sequencesh(β) s , h(β) s∗ of candidates hired in
profilesands ∗, according to the order of the firms being β. The quantity
W (β) snatched(s∗, s)represents the expected welfare of the candidates ofh(β) s∗ that ap-
pear earlier inh(β) s , whileW (β) available(s∗, s)is the value of the rest of the candidates
inh (β) s . Now, we distinguish two cases.
Case 1:WhenE β
h
W (β) snatched(s∗,s) i ≥ 1/2·SW(s ∗):
In this case, we haveSW (s) ≥E β
h
W (β) snatched(s∗,s) i ≥ 1/2·SW (s∗), as claimed.
The first inequality holds becauseSW (s)represents the expected combined value
ofallcandidates hired in profiles, whereas Eβ
h
W (β) snatched(s∗,s) i represents the
expected combined value of a subset of the candidates hired in profiles.
Case 2:WhenE β
h
W (β) snatched(s∗,s) i < 1/2·SW(s ∗):
In this case, we have that equivalently:Eβ
h
W (β) available(s∗,s) i > 1/2·SW (s∗).
Now, we use a proof outline reminiscent of the classical smoothness [19] framework
for price of anarchy. Suppose a firm in the equilibrium unilaterally deviates to
the strategy she employs in the optimal profiles∗. The idea is to observe that if

8 R. Kleinberg, E. Sinanaj and É. Tardos
her choice in the optimal profile would not be taken by those before her in the
equilibrium, she would hire either the candidate she would get in the optimal
profile, or someone higher up in her list. In the latter case, Lemma 1 shows that
stochastic consistency (of the advice space) guarantees that her expected utility
can only increase that way.
More formally, by definition:
X
i∈[n]
ui(s∗ i ,s −i) =E

 X
i∈[n]
x(β) i (s∗ i ,s −i)


Defining Ei :=
n
c(β) i (s∗)/∈C (β) i (s) o for brevity and recalling that valuations are
non-negative, we have:
X
i∈[n]
ui(s∗ i ,s −i)≥E

 X
i∈[n]
x(β) i (s∗ i ,s −i)·1(E i)


=E x,β
X
i∈[n]
P(E i |x, β)E
h
x(β) i (s∗ i ,s −i)

 x, β,Ei i
And now notice that by Lemma 1 this is:
≥E x,β
X
i∈[n]
P(E i |x, β)E
h
x(β) i (s∗)

 x, β,Ei i
=E β
h
W (β) available(s∗,s) i
> 1/2·SW(s ∗)
Now, assumesis a pure equilibrium; then, either case 1 holds, and we
immediately conclude thatSW (s) ≥ 1/2·SW (s∗)or not, in which case observe
that by the equilibrium property ofsit must be:
SW(s)≥
X
i∈[n]
ui(s∗ i ,s −i)≥ Case 2 1/2·SW(s ∗)
Finally, notice that nothing forbids us to extend this to mixed equilibria. We
just need to consider each case in expectation over the randomness of the mixed
strategyequilibrium,meaning,nowwedefine W (β)(σ∩s ∗) :=Es∼σ  W (β)(s∩s ∗) 
for a mixed strategy profileσ. The proof then follows the same recipe, distin-
guishing cases according to what proportion of the optimal welfare this quantity
represents.□
In fact, we can extend the previous proof in a similar fashion to other general
equilibrium concepts (e.g. correlated equilibria) or no regret sequences. One then
might wonder if our proof can be recast in the framework of “smoothness". It
turns out that the answer is yes: Stochastic Consistency implies that our game
is “(1,1)-smooth", as defined by Roughgarden [19]. The reader is referred to the
appendix for a proof of the fact.

Price of Anarchy of Algorithmic Monoculture 9
5 Generality of our assumptions
In this section we discuss and establish the generality of our assumptions.
First of all, we demonstrate that the most natural and widely considered rank-
ing distributions do indeed satisfy stochastic consistency. We show that it holds
for the well-knownMallow’s Modeldistribution (with very mild assumptions)
and for a very rich class of ranking technologies that we termSchur-concave
rankings. In Remark 1 below, we explain how the specific ranking distributions
considered by Kleinberg and Raghavan [14] fit within the two families outlined
here, as special cases.
5.1 Mallow’s model
Mallow’s model [16] has a long history in the literature of decision theory. It
dictates that the probability of observing a certain rankingπ is proportional to
ϕd(π,π 0), where d is a distance measure on permutations1, π0 is the ground-truth
ranking and ϕ∈ (0, 1]is adispersionparameter. One of the most frequently used
distance notions is the Kendall-Tau distance [13], which measures the number of
inversions (disagreements between ranked pairs) between two permutations.
Proposition 1. The Mallow’s Model of rankings with the Kendall-Tau distance
isStochastically Consistent.
Proof. That Mallow’s Model isstochastically consistentis fairly immediate: any
realization where some pair is ranked correctly can be mapped to one where
they switch positions (and obviously vice-versa). This introducesat leastone
inversion, the one between the pair (and of course, does not remove any pre-
existing inversions). Hence, the Kandall-Tau distance is strictly greater. Therefore,
witnessing this realization instead, is at mostϕ≤ 1times as likely, than the one
where the relative ordering of the pair was correct. A standard argument using
the law of total probability then implies the first claim.□
However, the claim of Proposition 1 extends to an even larger umbrella of
ranking families. We can actually characterize completely the class of Mallow’s
model ranking distributions that are stochastically consistent.
Theorem 2.A Mallow’s model ranking distribution is Stochastically Consistent
if and only if its distance function isinversion increasing.
A distance function d isincreasing with respect to inversions, if for any
permutation π and any other permutationπ′, which is a result of inverting a
pair of π that is ranked correctly (relative to each other), it holds thatd(π, π0) ≤
d(π′, π0), whereπ 0 is the ground truth ranking.
1 A distance function on the space of permutationsSn of[ n]is a non-negative and
symmetric functiond:S n ×S n →[0,∞).

10 R. Kleinberg, E. Sinanaj and É. Tardos
Proof. The “if" direction can be proved by tracing the proof of Proposition 1. We
show the “only if" direction. Suppose we have a stochastically consistent ranking
distribution that follows Mallow’s model with dispersion parameterϕ∈ (0, 1]and
some distance functiond :S m × Sm → [0,∞ ). Stochastic consistency states that
conditional on the candidate value vectorx(which implies a ground truth ranking
π0) the following holds for any two candidatesk, ℓ. Ifi < jandx(k) ≥x (ℓ), then
P

ri =k, rj =ℓ

 r−{k,ℓ}  ≥P  ri =ℓ, rj =k

 r−{k,ℓ} 
Thus, by Bayes, for any permutation2 π (with πi = k, πj = ℓ), we have that
i < jandx(k)≥x(ℓ)implies that:
P(r=π)≥P(r=π ′),whereπ ′ hasi, jswapped
But, since P(r=π) = ϕd(π,π 0) and ϕ∈ (0, 1], we must have d(π, π0) ≥
d(π′, π0).□
Other examples besides the Kendall-Tau distance discussed just previously,
include the Spearman-Rho and Spearman-Footrule (see e.g. [8]), the former of
which measures the squaredL2-distance of a ranking from the ground truth (i.e.
if π is the permutation thendSR(π) = P i  πi −π 0 i 2 ), and the latter theL1-
distance (dSF (π) =P i

πi −π 0 i

). Both of these owe their name to Spearman’s
work on correlation coefficients [20] and are also ubiquitously used, along with the
Kendall-Tau distance. Distance functions that do not fall in this category usually
arise from settings of combinatorial interest and not that of decision theory, such
as the Cayley distance, which counts the minimum number of transpositions to
make two permutations the same, or the Hamming distance, which measures how
many positions in the ranking are incorrect.
The following statement outlines a very general sufficient condition for the
distance function, which also substantiates the previous claims.
Proposition 2. Let g : [0,∞ ) → [0,∞ )be a non-decreasing, convex function.
The distance function(π, π′)7→ Pm i=1 g(|πi −π ′ i|)isinversion monotone.
The proof can be found in the appendix.
5.2 Schur-concave rankings
Before we define Schur-concave rankings we need the notion of anAdditive noise
ranking, which ranks candidates by noisy score estimation. In such a ranking
distribution, first, a joint noise vectorε is sampled and then, candidates are
ranked in decreasing order of their scores:xi + εi. The below definitions serve for
definingSchur-concave rankings:
2 Technically speaking, for all but a measure 0 set of them. But, this has to be the empty
set, as by definition, Mallow’s model has full support on the set of permutations,
which is finite.

Price of Anarchy of Algorithmic Monoculture 11
Definition 2(Majorization).A vectorx ∈R n majorizes another vectory ∈
Rm (and we symbolizex≻y) whenever we have that:
mX
i=1
xi =
mX
i=1
yi, and for allk∈[m] :
kX
i=1
x↓ i ≥
kX
i=1
y↓ i
where abovex ↓ i is thei-th largest entry ofx.
Definition 3(Schur-Concavity).A function f : Rm →R is said to beSchur-
Concavewhenever for all pairsx,y∈R m such thatx≻y:
f(x)≤f(y)
A vector that is majorized by another is more "spread out" than the latter
and so a first intuition for Schur-concave distributions is that they assign less
probability mass to more ‘extreme’ points. With this information we are now
ready to state our definition.
Definition 4(Schur-Concave Ranking).We call a ranking technologySchur-
Concaveif the distribution of the ranking can be modeled by an additive noise
ranking, such that the joint density of the noise vector is Schur-Concave.
The below claim describes a quite well-known fact in majorization theory (in
the language of our setting).3
Proposition 3. Additive noise rankings with identically and independently dis-
tributed log-concave noise (in each candidate) form aSchur-concaveranking.
Some examples of log-concave distributions are possibly the most well known:
the Gaussian, the Laplacian, the uniform, beta, logistic and many more. The
below theorem establishes the breadth of the class of distributions that our notion
of “well-behavedness” (stochastic consistency) encompasses. We state its proof in
the Appendix.
Theorem 3.Schur-concave rankingsareStochastically Consistent.
Remark 1.Kleinberg and Raghavan [14] proved the following.4
Consider any two-firm game with the advice space consisting of a private
technology (human evaluator) for each firm (with identical distribution) and one
common ranking technology (algorithm). Suppose also that the private evaluators
and the algorithm produce rankings from the same (parameterized) family of
distributions, where the parameter can be thought of as an accuracy. Under
sufficient conditions, it can be the case that the more accurate algorithm is a
dominant strategy, but the social welfare is higher when both firms choose their
evaluator.
3 See e.g. [9] and observe that it can be obtained as a corollary ofFact13.24 andFact
13.29.
4 Informal restatement of their Theorem 1, adapted to our terminology.

12 R. Kleinberg, E. Sinanaj and É. Tardos
In Theorem 3, they show that when this family corresponds to the Mallow’s
model ranking distributions with the Kendall-tau distance, then for any accuracy
of the evaluator (dispersion parameterϕH), there exists an algorithm with higher
accuracy (lower dispersion parameterϕA) such that the described phenomenon
is true, regardless of the candidates’ distribution. In Theorem 2, they establish
an analogous result for a setting in which there are three candidates, and the
family is Additive noise rankings with iid Gaussian (or Laplacian) noise, and
where accuracy would correspond to the inverse of the standard deviation.
These ranking distributions they analyzed are special cases of the two families
introduced in this section.
5.3 Trusting a ranking blindly
In the rest of this section we investigate the constraint that the mechanism
imposes on the firms (and its relaxation). Specifically, it is assumed that when
it’s her turn, each firm follows her ranking sample, in choosing the top ranked
available candidate, no matter what she knows about the state of the world.
However, this is not generally true for rational actors, if we (naturally) assume
that they have the choice of selecting from the remaining candidates however
they wish. This persists even if they don’t have a Bayesian belief about the rest
of the firms (for example they might have known that all firms have access only
to well-behaved algorithmic vendors), depending on the candidate distribution
and thus one might question the assumption that a firm will trust her ranking
“blindly”.
This behavior is also a problem in that it complicates a firm’s decision making:
it would be simpler if one was reassured that the best she could do in expectation,
at any point, is to follow the ranking she sampled. The statement below shows
that a very simple assumption about the world makes this desideratum (which
we will callincentive compatibility) true. Under this assumption, even if a firm
knew exactly what technology the ones before her used, not just what candidate
they received, she is better off choosing her top ranked choice that is available in
the sample she received. Below we define the assumption in question.
Definition 5(Permutation Invariant Candidate Distribution).A can-
didate distribution X ispermutation invariantiff for any permutation π of the
set[ m]and any candidate value vectorx ∈ [0,∞ )m the following holds for the
probability density function concerning the joint values:
fX (x) =fX (π◦x)
whereπ◦xdenotes the permutation of the components ofxaccording toπ.
One can readily verify that this is satisfied by any product distribution with
identical univariates (case of i.i.d. values). More generally, the condition does
not require mutual independence of the candidate values, merely a notion of
unidentifiability or symmetry in thelikelihoodof the realizations of the world: ie,
a name, tag, or other irrelevant attribute should not predict one’s potential.

Price of Anarchy of Algorithmic Monoculture 13
We claim the following, which asserts that under this assumption, firms in
the Unconstrained Random Serial Dictatorship mechanism have no incentive to
behave differently than they would have in the Obedience-Constrained Random
Serial Dictatorship. The proof can be found in the Appendix:
Proposition 4. Unconstrained Random Serial Dictatorship, equipped with a
stochastically consistentadvice space isincentive compatibleif the candidate
distribution ispermutation invariant, even if a firm knows which technologies
each firm before her selected.
The main argument is that even conditioned on some specific subset of candi-
dates being available, the firm cannot “distinguish” any one of them as having
lesser expected value from any other and thus will not gain in expectation by
strategically permuting a sample of a stochastically consistent ranking (even
adaptively to which candidate is recommended by her chosen ranking).
Proposition 4 implies that the same price of anarchy bound holds for theUn-
constrainedRandom Serial Dictatorship, assuming that firms follow the (weakly)
dominant strategy of trusting their ranking. Moreover, under some additional
mild assumptions about the candidate distribution (assuming the distribution is
atomless) and the advice space (assumingstrictconsistency: a strict inequality
for candidates with different values) trusting one’s ranking isstrictlydominant.
6 Lower bounds and violation of assumptions
In this section we show that the bound on the price of anarchy we presented
under the considered model assumptions is asymptotically tight, up toO(1/n)
terms. We continue by illustrating the importance of stipulating that ranking
technologies in our setting are stochastically consistent. We show that when one
or more ranking strategies can be arbitrary there can be pathological scenarios
where even a dominant strategy equilibrium can be vastly worse than the optimal
social welfare, by a factor linear in the number of firms. Finally, we conclude
this section by revisiting the definition of stochastic consistency, introducing a
relaxation of the definition that pertains to general advice spaces and quantifies
the extent to which they violate stochastic consistency. We provide bounds that
scale gracefully as stochastic consistency “degrades”.
6.1 A tight lower bound construction
Theorem 4.The Price of Anarchy bound of 2 is asymptotically tight.
Proof. Consider a symmetric game withn firms and two ranking technologies
for each one: common ranking technologiesA and A′. Further, consider the
following permutation invariant distribution on the candidate values; there are
2n candidates, a random pair of them have values1and v(n) ∈ (0, 1)(to be
determined below), while all other candidates have value0.
The ranking technologyA produces rankings that always put the candidate
with value1on the first position; the rest of the ranking constitutes a uniform

14 R. Kleinberg, E. Sinanaj and É. Tardos
permutation on the remaining candidates. On the other hand,A′ always puts
the two non-zero value candidates in the firstn positions, uniformly at random
and the rest of the ranking also constitutes a uniformly random permutation on
the remaining candidates.
Notice that this game instance satisfies the assumptions that lead to our
bound; the ranking technologies are stochastically consistent. Also the candidate
distribution is permutation invariant which implies incentive compatibility for
the relaxed model.
The optimum profile is for all firms to chooseA′, resulting in the maximum
welfare of1 +v(n). Observe that the utility of a firm choosingA, while everyone
else also choosesAis:
u(A, An−1) = 1/n+v(n)·Θ(2 −n)
Now, consider a deviation of one such firm to strategyA′. With probability
1/n the firm chooses first and her conditional expected utility is1/n(1 +v(n)).
With the remaining1 − 1/n probability the firm is not choosing first and cannot
hire the candidate with value 1, but still hopes to get the candidate with value
v(n). This either happens because the candidate with valuev(n)ranks above all
candidates with value 0 (probability 1 n−1) and none of the earlier firms using
strategy A picked that candidate (probability1 −O (n· 2−n)) or because the
candidate with valuev(n)is ranked below at least one candidate with value 0,
but all higher-ranked candidates were chosen by earlier firms using strategyA
(probability O(n· 2−n)). In total, then, the expected utility of using strategyA′
against profileA n−1 is
u(A′, An−1) = 1 n · 1 n (1 +v(n)) +  1− 1 n h 1 n−1 (1−O(n2 −n)) +O(n2 −n) i v(n)
≤ v(n) n + 1 n2 +v(n)( 1 n2 +O(n2 −n))
We can choosev(n)so that An is an equilibrium, to that end we wantu(A, An−1)
> u(A′, An−1)to hold and our goal is to maximize1 +v(n), the asymptotic ratio
ofSW(A ′n)/SW(A n).
If we ignore the asymptotics, we ask to maximizev(n)subject to the constraint
1/n > v(n)(1/n + 1/n2) + 1/n2. Thus, for somev(n) = 1− 2/(n + 1)−o (1/n)
we have thatAn is indeed an equilibrium. We can estimate the social welfare of
the strategy profilesAn andA ′n as follows:
SW(A n) = 1 +n·v(n)·Θ(2 −n)
SW(A ′n ) = 1 +v(n) = 2−2/(n+ 1)−o(1/n).
From these estimates we conclude that the price of anarchy is2−O(1/n).□
6.2 Arbitrary advice spaces lead to arbitrarily bad results
The next example, while unrealistic, shows that in the setting of [14] even a
dominant strategy equilibrium can be arbitrarily bad, when ranking technologies
are not stochastically consistent.

Price of Anarchy of Algorithmic Monoculture 15
Proposition 5.The price of anarchy isΩ(n)(linear in the number of firms),
for an arbitrary advice space, in the Obedience-Constrained Random Serial Dic-
tatorship. Further, there exist game instances where there is a (strict) dominant
strategy, the socially optimal profile has no firm using the dominant strategy and
the optimal welfare is a factor ofΘ(n)larger than that of the dominant strategy
equilibrium.
Proof. We considernfirms as usual and2ncandidates. The candidate distribution
is such that uniformly at random, a set ofn− 1of them have value0, one of
them has valuen and the n rest have unique values from the increasing sequence
{ai}i∈[n] with aj = 1 +j(j−1) n−j+1 − (j−1)(j−2) n−j+2 −ε/n 2 for some smallε >0. Notice
that this distribution is permutation invariant.
Firms have access to two ranking technologies, a commonA and a private
H (of the same distribution for any firm). Rankings fromA always rank the
candidate with value n at the first position, then− 1candidates with value
0in the next positions and then everyone else arbitrarily. On the other hand,
rankings from H rank the candidates with values from the sequence in the firstn
positions in increasing order and everyone else arbitrarily in the next positions.
For brevity, letAkH n−k denote the profile wherek firms have chosenA and
n−k chose their privateH. Clearly,u(A, An−k−1H k) = 1 +k n−k by construction
of A: a firm choosingA gets non-zero value (n) if it is the first to make a selection
among the n−k firms choosing A. Now, also observe thatu(H, An−k−1H k) =
1
k+1
Pk+1
i=1 ai = 1 + k n−k −ε/n 2. Thus,Ais indeed a dominant strategy.
It’s clear that the socially optimal profile isH n: changing any firm to employ
A results in the candidate with valuen getting hired, but consequently, society
loses out on the candidate with valuean = Ω(n2). Further, any profile with
two or more firms employingA is dominated by the profile where only one out
of them employs A, and all others useH. The optimal social welfare then is
SW (H n) = n(n+1) 2 −ε/n, while the dominant strategy equilibrium welfare is just
n. □
7 On stochastic inconsistency
We have argued in previous sections that stochastic consistency is a broadly
encompassing condition. It not only provides guarantees that bound the social
welfare loss due to monoculture in the setting of [14], but also extends these
guarantees to an extremely wide range of ranking distributions (including the
standard ones used in models of stochastic choice) and to the more general setting
of advice spaces and the model detailed in Section 3. Further, its definition is
not merely a technical measure of “well-behavedness”, but corresponds to an
important desideratum for ranking: the relative ranking of two candidates should
not depend on that of other people, or on characteristics that do not relate to
their ability.
In an ideal world people and any advice they use to make decisions would
follow this principle. However, obviously, the world is far from ideal: implicit

16 R. Kleinberg, E. Sinanaj and É. Tardos
and systemic bias is prevalent. This becomes ever more relevant with the rise
of machine learning models and LLMs and, crucially, their use for advice in
decision making. The biases of large language models have been documented, for
example, in [3, 22] and, most relevantly to our application, in [18]). The question
then becomes: what happens when stochastic consistency is violated, but not
arbitrarily (that is, inconsistency can be measured by some factor)? We give an
answer to this question as well. We begin by defining exactly this notion of the
measure of stochastic “inconsistency".
Definition 6((1 −δ )- Stochastically Consistent).A ranking technology
R is(1 −δ )- Stochastically Consistent if the following holds for alli < j∈[m],
k, ℓ∈[m]. Ifx(k)≥x(ℓ)then almost surely:
Pr∼FR(x)

(ri, rj) = (k, ℓ)

 r−{k,ℓ}  ≥(1−δ)P r∼FR(x)  (ri, rj) = (ℓ, k)

 r−{k,ℓ} 
Fortunately, this measure of inconsistency allows us to state the following
result.
Theorem 5. The Price of Anarchy of the Obedience-Constrained Random Serial
Dictatorship mechanism, in which firms obtain their rankings from a(1−δ )-
Stochastically Consistent advice space, whereδ∈ [0, 1), is bounded above by
1 + 1 (1−δ)2.
We prove the theorem in the appendix using a similar technique as our main
result (the “key” lemma here, analogous to Lemma 1, is the main obstacle and
needs more careful consideration).
8 Conclusion
Our work offers a tight bound on the social welfare loss in a hiring market with
advice (something that can arise due to algorithmic monoculture or general
selfish behavior) and identifies conditions and assumptions one should impose for
such settings to be well behaved. The phenomenon of algorithmic monoculture in
markets that can be modeled by the setting we investigate seems to not pose a
grave risk to the overall welfare. Arguing about how detrimental monoculture is
in regards to the price of anarchy or social welfare loss in the models of [11, 17],
as well as other models of algorithmic monoculture, remains an enticing question
for future work.
Acknowledgments.Erald Sinanaj was supported in part by AFOSR grant
FA9550-23-1-0410. Éva Tardos was supported in part by AFOSR grants FA9550-
23-1-0410 and FA9550-231-0068, and ONR MURI grant N000142412742.

Price of Anarchy of Algorithmic Monoculture 17
References
[1] Marek Adamczyk, Piotr Sankowski, and Qiang Zhang. “Efficiency of Truth-
ful and Symmetric Mechanisms in One-Sided Matching”. In:SAGT. DOI:
10.1007/978-3-662-44803-8_2. 2014, pp. 13–24.
[2] Jackie Baek and Ali Makhdoumi. “The Feedback Loop of Statistical Dis-
crimination”. In:SSRN(2023). DOI: 10.2139/ssrn.4658797.
[3] Xuechunzi Bai et al. “Explicitly unbiased large language models still form
biased associations”. In:Proceedings of the National Academy of Sciences
122.8 (2025), e2416228122.doi:10.1073/pnas.2416228122. eprint:https:
/ / www . pnas . org / doi / pdf / 10 . 1073 / pnas . 2416228122.url: https :
//www.pnas.org/doi/abs/10.1073/pnas.2416228122.
[4] Anand Bhalgat, Deeparnab Chakrabarty, and Sanjeev Khanna. “Social wel-
fareinone-sidedmatchingmarketswithoutmoney”.In:APPROX’11/RANDOM’11
(2011). DOI: 10.1007/978-3-642-22935-0_8, pp. 87–98.
[5] Anna Bogomolnaia and Hervé Moulin. “A New Solution to the Random
Assignment Problem”. In:Journal of Economic Theory100.2 (2001). DOI:
10.1006/jeth.2000.2710, pp. 295–328.
[6] Rishi Bommasani et al. “Picking on the Same Person: Does Algorithmic
Monoculture lead to Outcome Homogenization?” In:NeurIPS. Vol. 35.
2022, pp. 3663–3678.
[7] George Christodoulou et al. “Social Welfare in One-Sided Matching Mecha-
nisms”. In:AAMAS. DOI: 10.1007/978-3-319-46882-2_3. May 2016, pp. 30–
50.isbn: 978-3-319-46881-5.
[8] Persi Diaconis and R. L. Graham. “Spearman’s Footrule as a Measure of
Disarray”. In:Journal of the Royal Statistical Society. Series B (Method-
ological)39.2 (1977), pp. 262–268.issn: 00359246.url: http://www.jstor.
org/stable/2984804(visited on 02/24/2026).
[9] Y. E. Pečarić Josip; L. Tong.Convex Functions, Partial Orderings, and
Statistical Applications. Academic Press, June 1992.isbn: 9780080925226.
[10] ArisFilos-Ratsikas,SørenKristofferStiilFrederiksen,andJieZhang.“Social
Welfare in One-Sided Matchings: Random Priority and Beyond”. In:SAGT.
DOI: 10.1007/978-3-662-44803-8_1. 2014, pp. 1–12.
[11] Meena Jagadeesan et al. “Improved Bayes Risk Can Yield Reduced Social
Welfare Under Competition”. In:NeurIPS. Vol. 36. 2023, pp. 66940–66952.
[12] Sissi Jiang et al. “The Price of Anarchy of Probabilistic Serial in One-Sided
AllocationProblems”.In:WINE.DOI:10.1007/978-3-031-48974-7_24.2024,
pp. 420–437.
[13] M. G. Kendall. “A New Measure of Rank Correlation”. In:Biometrika
30.1/2 (1938). DOI: 10.2307/2332226, pp. 81–93.issn: 00063444. (Visited
on 06/30/2025).
[14] Jon Kleinberg and Manish Raghavan. “Algorithmic monoculture and social
welfare”. In:Proceedings of the National Academy of Sciences118.22 (2021).
DOI: 1073/pnas.2018340118.

18 R. Kleinberg, E. Sinanaj and É. Tardos
[15] Elias Koutsoupias and Christos Papadimitriou. “Worst-case equilibria”. In:
STACS’99. DOI :10.1007/3-540-49116-3_38. Trier, Germany, 1999, pp. 404–
413.isbn: 354065691X.
[16] C. L. Mallows. “Non-Null Ranking Models. I”. In:Biometrika44.1/2
(1957). DOI: 10.2307/2333244, pp. 114–130.issn: 00063444. (Visited on
06/30/2025).
[17] Kenny Peng and Nikhil Garg. “Monoculture in Matching Markets”. In:
NeurIPS. Vol. 37. 2024, pp. 81959–81991.
[18] P. S. B. Rao et al. “Invisible Filters: Cultural Bias in Hiring Evaluations
Using Large Language Models.” In:Proceedings of the AAAI/ACM Con-
ference on AI, Ethics, and Society8 (2025), pp. 2164–2176.doi:https:
//doi.org/10.1609/aies.v8i3.36703.
[19] Tim Roughgarden. “Intrinsic Robustness of the Price of Anarchy”. In:J.
ACM62.5 (Nov. 2015). DOI: 10.1145/2806883.issn: 0004-5411.
[20] Charles Spearman. “The proof and measurement of association between
two things”. In:The American Journal of Psychology15 (1904), pp. 72–101.
doi:https://doi.org/10.2307/1412159.
[21] Connor Toups et al. “Ecosystem-level Analysis of Deployed Machine Learn-
ing Reveals Homogeneous Outcomes”. In:NeurIPS. Vol. 36. 2023, pp. 51178–
51201.
[22] Anling Xiang. “Diagnosing the bias iceberg in large language models: A
three-level framework of explicit, evaluative, and implicit gender bias”. In:
Information Processing and Management63.3 (2026), p. 104554.issn: 0306-
4573.doi: https://doi.org/10.1016/j.ipm.2025.104554.url: https:
//www.sciencedirect.com/science/article/pii/S0306457325004959.
A Missing proofs
Lemma 1. Consider an Obedience-Constrained Random Serial Dictatorship
mechanism with a stochastically consistent advice space. Letc(β) i (s)denote the
candidate hired by firm i in profileswhen the order of firms is β. Let also
x(β) i (s) :=x(c(β) i (s))be the value of this candidate. Further, defineC (β) i (s)to be
the set of candidates hired by the firms going beforeiin profiles.
For any two pure strategy profiless,s∗ the below holds:
E
h
x(β) i (s∗ i ,s −i)−x (β) i (s∗)

 x, β, c(β) i (s∗)/∈C (β) i (s) i ≥0
where the expectation is over the randomness of the samples drawn from the
ranking technologies andxrepresents the joint value vector of the candidates.
Proof. Consider an ordering of firmsβ and a realizationxof the values. We will
show that this inequality is true for any choice of these. This is obviously true
when β(i) = 1, i.e. when firmi chooses first. Thus we assumeβ(i) > 1, so theni
in both profiles has some non-zero number of firms going before her.

Price of Anarchy of Algorithmic Monoculture 19
Let’s start by assumings∗ i is a private ranking. When deviating to choosing
s∗ i in profilesthe firm will get the same candidate as in profiles∗ or someone
ranked higher (as per the conditioned event), so intuition says she should not do
worse in expectation. However, this is not true in general ifi is up against firms
that use arbitrary (not stochastically consistent) technologies, as the event thati
has a higher ranked candidate available can be non-trivially correlated with the
value of that candidate, see Proposition 6 for example.
Condition on the set of candidates that were hired by the firms going before
i in profiles, e.g. say C (β) i (s) =C for some arbitraryC. Consider the ranking
sample that i draws using s∗ i, let it ber. When deviating to this strategy in
profiles, then, i will select some candidater−C 1 . Let EC denote the event that the
vector of candidate values isx, the ordering of firms isβ, the setC (β) i (s)is equal
to C, and c(β) i (s∗) ̸∈C . The eventEC can be partitioned into mutually exclusive
events Ej,C, where j ranges from 1 tom− |C|and Ej,C represents the subset of
sample points inEC that satisfy c(β) i (s∗) =r−C j . Conditional on eventE1,C we
have c(β) i (s∗ i , s−i) =c(β) i (s∗) =r−C 1 , so x(β) i (s∗ i , s−i) −x (β) i (s∗) = 0. Accordingly,
for the remainder of the proof we focus on the casej >1.
Now, notice that conditioning onC (β) i (s) =C does not imply anything about
i’s ranking r, by independence of rankings. However, assumingj >1we know
that r−C 1 was not available in profiles∗, which could correlate with its value.
Consider then whoever got that candidate in profiles∗ and let their ranking
sample be f. The idea is that since she is also using a stochastically consistent
technology, she will be “making the right choice” most of the time.
Now, we condition on an arbitrary pair of candidatesk, ℓ, so that either
(r−C 1 , r−C j ) = (k, ℓ)or( r−C 1 , r−C j ) = (ℓ, k). If we can show that for any such pair
withx(k)≥x(ℓ)the first event is the most likely, then we are done, since:
E

x(β) i (s∗ i ,s −i)−x (β) i (s∗)

 x, β, c(β) i (s∗)/∈C (β) i (s)  =
1/2·E C∼C (β) i (s)
X
j>1
X
k,ℓ∈[m]
k̸=ℓ
(x(k)−x(ℓ))P(E j,C)

P

(r−C 1 , r−C j ) = (k, ℓ)| Ej,C 
−P

(r−C 1 , r−C j ) = (ℓ, k)| Ej,C  
Fix (condition) the arbitrary positions thatk, ℓ could be ranked in rankings
r and f, say u and u + v in r and z, z + w in f (note that they both have to
“agree” on their relative positions by the conditioned event) and condition on
everyone else’s ranking (including the other positions ofr and f) for simplicity
of the argument.
To complete the proof we make use of the following inequality, for any
u < u+ v, z < z+ w∈ [m]and for any k̸ = ℓ∈ [m]with x(k) ≥x (ℓ), when
E ′ is an arbitrary event (consistent with the eventEj,C) that may depend on
the rankings of any other technology besidesr and f, and on all positions of all

20 R. Kleinberg, E. Sinanaj and É. Tardos
candidatesc /∈ {k, ℓ}in rankingsrandf.
P

ru
ru+v

=

k
ℓ

=

fz
fz+w


 E ′  ≥P  ru ru+v  =  ℓ k  =  fz fz+w 

 E ′  (1)
The inequality is valid since distinct technologies are mutually independent and
stochastically consistent. The independence implies that the left side factorizes as
P

ru
ru+v

=

k
ℓ


 E ′  ·P  fz fz+w  = k ℓ 

 E ′  andthattherightsidefactorizes
similarly. Stochastic consistency then implies that each factor on the left side is
greater than or equal to the corresponding factor on the right side.
To see that inequality(1) suffices to complete the proof of the lemma, define
E kℓ uvzw to be the event that{k, ℓ}= {fz, fz+w} = {ru, ru+v} = {r−C 1 , r−C j } (as
unorderedsets) and observe thatE kℓ uvzw can be decomposed as a disjoint union
of events E ′ of the type defined above. Hence, by taking a weighted average of
inequalities (1) for all the constituent setsE′ that composeE kℓ uvzw, we obtain
P
 ru
ru+v

=
k
ℓ

=
 fz
fz+w


 E kℓ uvzw  ≥P  ru ru+v  = ℓ k  =  fz fz+w 

 E kℓ uvzw  .
Now we calculate
P

(r−C 1 , r−C j ) = (k, ℓ)| Ej,C  −P  (r−C 1 , r−C j ) = (ℓ, k)| Ej,C 
=
X
u,v,z,w∈[m]
u+v>u
w+z>w
P

E kℓ uvzw | Ej,C 
(
P
 ru
ru+v

=
k
ℓ

=
 fz
fz+w


 E kℓ uvzw 
−P
 ru
ru+v

=
ℓ
k

=
 fz
fz+w


 E kℓ uvzw  )
and deduce that the sum is non-negative because each summand is non-negative.
Finally, to conclude the proof we have to argue about “common” strategies,
but observe that this proof can also be directly extended for that case too. There’s
only a few small changes, specifically in this case conditioning onC (β) i (s) =C
might affectsomeof i’s ranking, but crucially, stochastic consistency implies that
it won’t affect that it’s more likely a pair specific pair of candidates inr−C will
be ranked correctly rather than not. Additionally, we won’t be conditioning on
everyone else’s ranking, but only on those beforei in both profiles, except the
positions as defined previously. This again might affect some ofi’s ranking, but
not the positions we care about (by the event), and so the arguments flow in the
following fashion. If the firm who took candidater−C 1 (in profiles) is using another
independent technology, the proof follows the same blueprint as previously. If
the firm that took the candidate is using the same common technology, then
the proof is simpler, as we just have to argue about the common technology’s
stochastic consistency.□
Proposition 6. Lemma 1 does not necessarily hold if firmi is using a stochas-
tically consistent technology, but not her competitors.

Price of Anarchy of Algorithmic Monoculture 21
Proof. Assume the following for simplicity of the argument:m = n + 3,xis such
that x(i), i∈[m]is a decreasing sequence andβ is such thati is last to choose
(β(i) =n). Now, consider the following about the profiless−i ands ∗ −i: the former
is such, that they always choose the best candidates, but never identify1to be
such, meaning they will always hire the candidates of[m] \ {1, m−1, m}, leaving
the rest fori. The latter, profiles∗ −i, is not very well informed: they always choose
theworstcandidates, leaving {1, 2, 3} for i to choose. Now, supposei is employing
a stochastically consistent ranking technology ins∗, such as the Mallow’s model
with the Kendall-Tau distance. Her utility in profiles∗ conditioned on the event
of Lemma 1 is justx(1). This is because the event is only true when she hires
candidate1, as candidates2and3are never available ins. What is her conditional
utility in profilesif she were to deviate tos∗ i? It must be less thanx(1), because
there is a non zero probability she rankedm or m− 1above1(even though in
profiles ∗ she would hire candidate1).□
Theorem 6. The Obedience-Constrained mechanism with a stochastically con-
sistent advice space is(1,1)-smooth.
Proof.Consider any two profiless,t. We have the following inequalities:
X
i∈[n]
ui(ti,s −i)≥E β
h
W (β) available(t, s) i (by Lemma 1)
=SW(t)−E β
h
W (β) snatched(t, s) i
≥SW(t)−SW(s)
Thesecondlinefollowsfromthedefinitionof W (β) snatched(t, s)and W (β) available(t, s),
as:
Eβ
h
W (β) snatched(t, s) i +E β h W (β) available(t, s) i =SW(t)
Similarly, the third line follows from observing thatSW (s) ≥E β
h
W (β) snatched(t, s) i .
□
Proposition 2. Let g : [0,∞ ) → [0,∞ )be a non-decreasing, convex function.
The distance function(π, π′)7→ Pm i=1 g(|πi −π ′ i|)isinversion monotone.
Proof. Let d be the distance function in question. Without loss of generality,
it suffices to prove that for any arbitraryk < ℓ, any permutation π with i =
π−1(k) < j= π−1(ℓ)and the permutation π′ which arises fromπ by swapping
the position ofkandℓ, the following holds:
d(π,(1, . . . , m))≤d(π′,(1, . . . , m))
Observe that by the form of the distance functiond and how π and π′ relate:
d(π,(1, . . . , m))−d(π′,(1, . . . , m)) =g(|π−1(k)−k|) +g(|π −1(ℓ)−ℓ|)
−

g(|π −1(ℓ)−k|) +g(|π −1(k)−ℓ|) 
=g(|i−k|)−g(|i−ℓ|)−(g(|j−ℓ| −g(|j−k|))

22 R. Kleinberg, E. Sinanaj and É. Tardos
We definef : x7→g (|x−k| ) −g (|x−ℓ| ), with our goal being to show thatf is
non-decreasing. For ease of argument we assumeg is differentiable, but the same
follows for a general non-differentiableg. Suppose x≥ℓ > k, we have then that
f (x) =g(x−k ) −g (x−ℓ )and so f ′(x) ≥ 0, as g is convex. Similarly, forx≤k
we havef (x) =g(k−x ) −g (ℓ−x )and so f ′(x) =g′(ℓ−x ) −g ′(k−x ) ≥ 0, again
by convexity ofg. Now, letx∈ (k, ℓ), we have nowf (x) =g(x−k ) −g (ℓ−x )
and f ′(x) =g′(x−k ) +g′(ℓ−x ) ≥ 0, since g is non-decreasing. Further, sinceg
is convex it must also be continuous (which implies continuity off) and thusf
must be non-decreasing in its entire domain.
The claim follows from observing thatd(π, (1, . . . , m)) −d (π′, (1, . . . , m)) =
f (i) −f (j)and since i < jand f is non-decreasing, it is d(π, (1, . . . , m)) −
d(π′,(1, . . . , m))≤0, as needed.□
Theorem 3.Schur-concave rankingsareStochastically Consistent.
Proof. Let f : Rm →R be the pdf of the additive noise vector. We fix arbitrary
i < jand k, ℓ∈ [m]and condition on the candidate value vector, where without
loss of generality we assumex(k)≥x(ℓ).
Let r be the random ranking of the candidates induced by the additive noise
scoring procedure and letEij(k, ℓ,c)denote the event that {(r−C i , r−C j ) = (k, ℓ)}
and r−{k,ℓ} =c. Further, let Mij be the set of joint noise vectorsε that realize
event Eij(k, ℓ,c). Define Eij(k, ℓ,c)and Mji accordingly. If we show that for all
cthe following difference is non-negative we are done:
P(E ij(k, ℓ,c))−P(E ji(k, ℓ,c)) =
Z
Mij
f(ε)dε−
Z
Mji
f(ε)dε
Letδ kℓ =x(k)−x(ℓ)≥0and define the below bijection:
ξ:R m ∋y7→y+δ kℓ(ek −e ℓ)∈R m
Further letB be the matrix that swaps coordinatesk, ℓand define the bijection
t = ξ◦B . Observe thatt maps elements ofMij to Mji and vice-versa: rankings
remain the same, except itemsk and ℓ are swapped. To see this, letε∈M ij(c),
with ε(m)the additive noise to candidatem. After the transformation the noise
vector remains identical, except thek-th and ℓ-th component that would now be
ε(ℓ) −δ kℓ and ε(k) +δkℓ, resulting in scoresx(ℓ) +ε(ℓ)and x(k) +ε(k)for items
k and ℓ respectively (the scores of the rest of the candidates remain unchanged).
Thus, the only difference in this new ranking is thatk and ℓ are swapped. Now,
clearly t is Lebesgue measure preserving and since it is a bijection betweenMij
andM ji it’s the case that:t−1(Mji) =Mij.
We have then, that:
P(E ij(k, ℓ,c))−P(E ji(k, ℓ,c)) =
Z
Mij
f(ε)dε−
Z
t−1(Mji )
f(t(ε))dε
=
Z
Mij

f(ε)−f(t(ε))

dε(2)

Price of Anarchy of Algorithmic Monoculture 23
Now, observe that ifz = t(ε), then z(r) = ε(r)for all r∈ [m] \ {i, j}, but
z(k) = ε(ℓ) −δ kℓ and z(ℓ) = ε(k) +δkℓ, as we noted before. Recall then that,
sinceε∈M ij we must have thatkis ranked aboveℓ:
x(k) +ε(k)≥x(ℓ) +ε(ℓ)
Which implies:
ε(ℓ)−δ kℓ ≤min{ε(k), ε(ℓ)}.
By the same observation we also conclude that:
ε(k) +δkℓ ≥max{ε(k), ε(ℓ)}
Thus, t(ε)majorizes ε and by Schur-concavity off we have that the in-
tergrands in Equation (2) are always non-negative, leading toP(E ij(k, ℓ,c))−
P(E ji(k, ℓ,c))≥0, which implies what’s desired.□
Here, we present an equivalent definition for Stochastic Consistency, which
will be useful in some of our proofs.
Proposition 7. A ranking technologyR isstochastically consistentiff for any
two subsets M and C of[ m]with cardinality q and any enumeration{mi}i∈[q],
{ci}i∈[q] of them, for any realizationxof the joint value vector, the following
holds for alli, j /∈M,k, ℓ /∈Cwith(i−j)(x(k)−x(ℓ))≤0:
Pr∼FR(x)

(ri, rj) = (k, ℓ)|(rm1 , . . . , rmq ) = (c1, . . . , cq)

≥
Pr∼FR(x)

(ri, rj) = (ℓ, k)

 (rm1 , . . . , rmq ) = (c1, . . . , cq)  ,
(whenever the conditioning event has non-zero probability).
Proof. It’s clear that this definition implies the original. The same is true for
the inverse implication: we get the inequality for any relevant subset and their
enumeration, using the law of total probability.□
Proposition 4. Unconstrained Random Serial Dictatorship, equipped with a
stochastically consistentadvice space isincentive compatibleif the candidate
distribution ispermutation invariant, even if a firm knows which technologies
each firm before her selected.
Proof. We will show that no firm has any incentive to strategize and ask for a
candidate other than the highest ranked that is available from her sample, even if
she knew not just the candidates hired before her, but also the technologies used.
Suppose then she has a strategy to permute her sampled ranking, based on what
she witnessed (technologies used and candidates hired) and her ranking sample.
Lets:= ( s1, . . . , sk)for some k≥ 0denote the arbitrary strategies of the
firms going before her in order and letD(s)denote the (vector of) candidates

24 R. Kleinberg, E. Sinanaj and É. Tardos
that each hired. First, consider the event where the firms hire some arbitrary
candidates in that order, i.e. sayD(s) = (c1, . . . , ck). We claim that the joint
distribution of the value of candidatesC ′ = [m] \ {c1, . . . , ck} conditioned on
D(s) = (c1, . . . , ck)remains permutation invariant. This is because the event
D(s) = (c1, . . . , ck)is (trivially)symmetricwith respect to these candidates
and so permutation invariance of the original joint value vector, shall imply
permutation invariance for the joint value vector of the candidates inC ′ too,
conditioned on this event.
This shows that when a firm witnesses the eventD(s) = (c1, . . . , ck)she
doesn’t have any incentive to strategize with respect to the identities of the
candidates she sees in the partial rankingr−D. Thus, her strategy can as well
depend only on the eventD(s) = (c1, . . . , ck)by possibly choosing some later
positionin r−D than the first (and shall not depend on the sampler she sees).
Say then, whenever she witnessesD(s) = (c1, . . . , ck)she chooses the q-th ranked
candidate from her list of available candidates for someq >1, ie she seeks to hire
r−D q instead of r−D 1 . The eventD(s) = (c1, . . . , ck)implies that for some m≥ 0
and some suitable indicesℓi we have that(r1, . . . , rm) = (cℓ1 , . . . , cℓm)( m >0
implies that this ranking is sampled from an algorithmic vendor andshas some
firms employing the same advice). But now notice the following, because of the
independence of distinct technologies:
E

x(r−D 1 )−x(r −D q )|D(s) =D  =E  x(r−D 1 )−x(r −D q )|(r 1, . . . , rm) = (cℓ1 , . . . , cℓm) 
And now it’s not hard to see that stochastic consistency ensures that:
E

x(r−D 1 )−x(r −D q )|(r 1, . . . , rm) = (cℓ1 , . . . , cℓm )  ≥0
This is because:
E

x(r−D 1 )−x(r −D q )|(r 1, . . . , rm) = (cℓ1 , . . . , cℓm) 
= 1 2 ·E X
k,ℓ∈C ′
k̸=ℓ
X
i,j∈[m]
i<j
(x(k)−x(ℓ))·
n
P((r i, rj) = (k, ℓ)| ED ∧ E)
−P((r i, rj) = (ℓ, k)| ED ∧ E)
o
Where ED represents the (random) rankings of the candidates inD, that are
consistent with {r−D 1 , r−D q } = {k, ℓ} = {ri, rj} and E, which is the event
(r1, . . . , rm) = (cℓ1 , . . . , cℓm ). Since the statement of stochastic consistency implies
that for any arbitrary conditioning on the ranking of a set of candidates (disjoint
from those of interest), the above quantity must be non-negative.
This concludes the proof (as the conditioningD(S) =Dwas arbitrary).□
Lemma 2. Consider an Obedience-Constrained Random Serial Dictatorship
mechanism with a(1 −δ )- Stochastically Consistent advice space, forδ∈ [0, 1).
Let c(β) i (s)denote the candidate hired by firmi in profileswhen the order of firms

Price of Anarchy of Algorithmic Monoculture 25
is β. Let alsox(β) i (s) := x(c(β) i (s))be the value of this candidate. Further, de-
fine C (β) i (s)to be the set of candidates hired by the firms going beforei in profiles.
For any two pure strategy profiless,s∗ the below holds:
E

x(β) i (s∗ i ,s −i)−(1−δ) 2x(β) i (s∗)

 x, β, c(β) i (s∗)/∈C (β) i (s)  ≥0
where the expectation is over the randomness of the samples drawn from the
ranking technologies andxrepresents the joint value vector of the candidates.
Proof. Let E be the event that the joint value vector isx, the order isβ and
c(β) i (s∗)/∈C (β) i (s).
Now, similar to the proof of Lemma 4.3, define the eventEj,C (where j ranges
from 1 tom− |C|) to be such thatC (β) i (s) = C and c(β) i (s∗) = r−C j . Observe
that we can write:
E

x(β) i (s∗ i ,s −i)−x (β) i (s∗)

 E 
=E C∼C (β) i (s)
X
j>1
X
k,ℓ∈[m]
x(k)>x(ℓ)
(x(k)−x(ℓ))P(E j,C)

P

(r−C 1 , r−C j ) = (k, ℓ)| Ej,C 
−P

(r−C 1 , r−C j ) = (ℓ, k)| Ej,C   (3)
It’s not hard to see that for a(1−δ )-Stochastically Consistent advice space
we have for any two sample rankingsr, f(possibly the same, as in the proof of
Lemma 4.3) and valid indices:
P
 ru
ru+v

=
k
ℓ

=
 fz
fz+w


 E ′  ≥(1−δ) 2 P  ru ru+v  = ℓ k  =  fz fz+w 

 E ′ 
(4)

26 R. Kleinberg, E. Sinanaj and É. Tardos
Butthenwecanseefrom(3)that(define P j,C k,ℓ := P(E j,C)P  (r−C 1 , r−C j ) = (k, ℓ)| Ej,C 
for brevity):
E

x(β) i (s∗ i ,s −i)−x (β) i (s∗)

 E 
≥((1−δ) 2 −1)·E C∼C (β) i (s) X j>1 X k,ℓ∈[m]
x(k)>x(ℓ)
(x(k)−x(ℓ))P j,C ℓ,k (5)
= ((1−δ) 2 −1)·E C∼C (β) i (s) X j>1 X k,ℓ∈[m]
x(k)>x(ℓ)
n
x(k)P j,C ℓ,k +x(ℓ)P j,C k,ℓ
o
+ (1−(1−δ) 2)·E C∼C (β) i (s) X j>1 X k,ℓ∈[m]
x(k)>x(ℓ)
x(ℓ)

P j,C k,ℓ +P j,C ℓ,k

(6)
≥((1−δ) 2 −1)·E

x(β) i (s∗)·1  x(β) i (s∗ i ,s −i)̸=x (β) i (s∗) 

 E  (7)
≥((1−δ) 2 −1)E

x(β) i (s∗)

 E  (8)
To see line (7), note first that1− (1 −δ )2 ≥ 0for δ∈ [0, 1]and thus, the
second term is non-negative. Then, observe that the term we lower bound in line
(7) exactly represents the first term in the preceding line: it “counts" the expected
value of the candidate hired by firmi in profiles, only when this candidate is
different than the one hired ins(if she were to deviate tos∗ i). The final inequality
follows from the fact that the factor is non-positive and candidate values are
non-negative.
□
Theorem 7. The Price of Anarchy of the Obedience-Constrained Random Serial
Dictatorship mechanism, in which firms obtain their rankings from a(1−δ )-
Stochastically Consistent advice space, whereδ∈ [0, 1), is bounded above by
1 + 1 (1−δ)2.
Proof. The proof is similar to that for Stochastically Consistent advice spaces.
Using the same notation we have two cases.
Case 1:WhenE β
h
W (β) snatched(s∗,s) i ≥  1− 1 1+(1−δ)2  ·SW(s ∗):
Trivially then, we have thatSW(s ∗) SW(s) ≤  1− 1 1+(1−δ)2 −1 = 1 + 1 (1−δ)2.
Case 2:WhenE β
h
W (β) snatched(s∗,s) i <  1− 1 1+(1−δ)2  ·SW(s ∗):
By Lemma 2 we have that:
SW(s)≥(1−δ) 2 ·E β
h
W (β) available(s∗,s) i

Price of Anarchy of Algorithmic Monoculture 27
By the case assumption we knowEβ
h
W (β) available(s∗,s) i ≥ 1 1+(1−δ)2 SW (s∗)
and so sincesis an equilibrium:
SW(s)≥(1−δ) 2 1 1 + (1−δ)2 ·SW(s ∗)
Which gives
SW(s ∗)
SW(s) ≤1 + 1 (1−δ) 2
. □
