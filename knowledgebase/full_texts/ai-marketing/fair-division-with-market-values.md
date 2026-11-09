---
title: Fair Division with Market Values
url: https://arxiv.org/abs/2410.23137
category: ai-marketing
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Siddharth Barman
- Soroush Ebadian
- Mohamad Latifian
- Nisarg Shah
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.23137
pages: 19
chars: 81185
fetched_at: '2026-11-08T13:16:23+00:00'
kb_version: 1
---

# Fair Division with Market Values

arXiv:2410.23137v1  [cs.GT]  30 Oct 2024
FAIR DIVISION WITH MARKET VALUES
Siddharth Barman1, Soroush Ebadian 2, Mohamad Latiﬁan 2, Nisarg Shah 2
1Indian Institute of Science Bangalore
2University of Toronto
barman@iisc.ac.in,{soroush,latiﬁan,nisarg}@cs.toronto.edu
ABSTRACT
We introduce a model of fair division with market values, whe re indivisible goods must be parti-
tioned among agents with (additive) subjective valuations , and each good additionally has a market
value. The market valuation can be viewed as a separate addit ive valuation that holds identically
across all the agents. We seek allocations that are simultan eously fair with respect to the subjective
valuations and with respect to the market valuation.
We show that an allocation that satisﬁes stochastically-do minant envy-freeness up to one good (SD-
EF1) with respect to both the subjective valuations and the m arket valuation does not always exist,
but the weaker guarantee of EF1 with respect to the subjectiv e valuations along with SD-EF1 with
respect to the market valuation can be guaranteed. We also st udy a number of other guarantees such
as Pareto optimality, EFX, and MMS. In addition, we explore n on-additive valuations and extend
our model to cake-cutting. Along the way, we identify severa l tantalizing open questions.
1 Introduction
For centuries, human civilizations have pondered how to set tle disputes centered around division of goods. Such
resolution requirements come up often in cases such as divor ce settlement and estate division (in the absence of a
will). A common practice in the real world is not to liquidate all the goods but to assess their fair market value (FMV)
and create an “equal division” whereby the total fair market value of the goods awarded to each party is (almost) equal.
Such a division is sometimes even a legal requirement [ 25]. For instance, fair market values of land—as determined
by assessors [ 26]–are often used to settle land disputes [ 35]. However, an FMV -based approach has two limitations:
(i) parties may disagree on what the fair market value of a goo d is, and (ii) parties may have personal (i.e., subjective)
cardinal preferences (over the goods) which may be quite dif ferent from the assessed market values.
Starting with the seminal work of Steinhaus [ 36], the mathematical theory of fair division has made signiﬁc ant ad-
vances over the last century. The theory systematically add resses the issue (ii) mentioned above by developing models
wherein the participating agents (parties) can submit thei r own heterogeneous valuations over the goods. Here, the
underlying goal is to ﬁnd a division that each agent would con sider fair according to their own valuation . Hence, the
models provide a systematic way to avoid disagreements. In r ecent years, fair division literature has made impressive
strides in the context of indivisible goods, resulting in al location methods that achieve appealing fairness guarante es.
One such notion is envy-freeness up to one good (EF1), which demands that no agent prefers the allocation of another
agent over their own if we hypothetically exclude just one go od from the envied agent’s allocation [ 28, 13, 14].
Despite the mathematical and conceptual appeal of this fram ework, equal division of goods under market values still
holds unshakable importance in real-world dispute resolut ions. Hence, we study the framework of fair division with
market values, where we seek an allocation of the goods that the agents ﬁnd f air with respect to their heterogeneous
personal preferences (“subjective utilities”), and that i s also a near-equal division under the market values. Formal ly,
a setM of (indivisible) goods must be allocated among a set N of n agents. Each agent i∈N submits an additive
subjective utility function ui : 2 M→ R/greaterorequalslant0 and there is an additive market value function v : 2 M→ R/greaterorequalslant0.1 Our goal
1A set function f : 2 M→ R/greaterorequalslant0 is said to be additive if f (S) = ∑ r∈S f ({r}) for all S⊆M with f (∅) = 0 .

Fair Division with Market V alues
is to seek an allocation that is simultaneously fair (e.g., E F1) with respect to the subjective utilities {ui}i∈N and with
respect to the market values v.
The signiﬁcance of this formulation is further substantiat ed by the following observations: First, near-equal divisi on
under the market values can correspond to a feasibility cons traint, imposed due to legal or normative reasons. Hence,
one can view the requirement under market values as seeking a n allocation that is fair (with respect to the agents’
subjective utilities) as well as feasible (with respect to the market values). Indeed, with this viewp oint, the current
work contributes to the growing body of work on fair division under constraints (see, e.g., [ 37]), and some of our
results are derived using ideas from this line of work.
Second, one can adopt an epistemic perspective that the subj ective utilities provided by the agents are in fact their
(personal) noisy estimates of the market values of the goods . Further, the “market values” that we take as input may
be an expert’s estimate or algorithmic prediction. Achievi ng an equal division with respect to both agents’ personal
estimates and the external estimate can provide greater rob ustness and prevent future disputes.
Our work is closely related to two very recent papers, which a lso study fair division in the presence of market values. 2
Dall’Aglio [ 18] studies the same model, but with divisible goods and the sub jective utility of each agent, for every
good, modeled a function of the good’s market value. The focu s in [ 18] is on the behavior of prominent rules, rather
than on concrete fairness guarantees. The work of Bu et al. [ 12] is closer to ours, who consider a generalization of our
model with heterogeneous market values{vi}i∈N , motivated as an allocator’s preference over which agent sh ould get
which good. Their result for this general model establishes guarantees for proportionality, a notion weaker than the
one studied in the current paper, namely, envy-freeness. In particular, there are two results where the current paper
and the work of Bu et al. [ 12] overlap: First, we show that the fairness guarantee for goo ds obtained in [ 12] can be
viewed as a corollary of a result due to Biswas and Barman [ 9]. Second, we show that the existential result in [ 12]
can be turned into a polynomial-time algorithm in our model ( while [12] provides a polynomial-time algorithm for a
weaker notion). Our study of Pareto optimality, EFX, and MMS in this framework is entirely novel. We discuss these
technical points at length in Section 1.2.
1.1 Our Contributions
In Section 3, we begin by asking whether there always exists an allocatio n of indivisible goods that satisﬁes stochastic-
dominance envy-freeness up to one good (SD-EF1)—a strengthening of EF1—w.r.t.3 both additive subjective utilities
and additive market values. We answer the question in the neg ative, using a carefully crafted instance with 2 agents
and 7 goods. Complementing this result, we prove positive re sults for 2 agents and up to 6 goods, and for any number
of agents with identical utilities. Then, relaxing the requ irement slightly, we prove that an allocation that is EF1 w.r .t.
subjective utilities and SD-EF1 w.r.t. market values alway s exists via a reduction to an algorithm by Biswas and
Barman [9]. The complementary guarantee of SD-EF1 w.r.t. agents’ uti lities and EF1 w.r.t. market valuation stands
as an interesting open question.
Next, in Section 4, we consider other desiderata such as Pareto optimality (PO ), maximin share fairness (MMS), and
envy-freeness up to any good (EFX). In Section 4.1, our main result is that an allocation that is PO w.r.t. subje ctive
utilities and EF1 w.r.t. market values always exists, but th ere are open questions surrounding several other combi-
nations of desiderata. Section 4.2 shows that MMS or EFX cannot be attained w.r.t. one side (subj ective utilities or
market values) together with EF1, MMS, or EFX on the other sid e. Finally, in Section 4.3, we observe that the exis-
tence of an allocation that is EF1 w.r.t. even monotone subje ctive utilities and monotone market values remains open,
but prove the existence of allocations that are 1/2-EF1 w.r.t. subadditive subjective utilities and SD-EF1 w. r.t. additive
market values. These results are summarized in Table 1.
Finally, in Section 5, we extend our setup of fair division with market values to ca ke-cutting. That is, we consider
partitioning a heterogeneous divisible good (cake) among a gents with subjective utilities in the presence of a market
valuation, both subjective utilities and market valuation represented as countably additive measures over the cake.
This model is formally introduced in Section 5. We observe that the existence of an allocation that is EF w.r .t. both
subjective utilities and market values can be reduced to the known existence of a perfect cake-division [ 21]. We
prove bounds on the number of cuts (of the cake) and queries (o f the subjective utility measures and the market value
measure) required to achieve EF w.r.t. both sides. We also sh ow that there may not exist any cake-division that is
EF+PO w.r.t. the subjective utilities along with EF w.r.t. t he market values. Though, relaxing EF+PO to simply PO
w.r.t. the subjective utilities yields a positive result.
2Our work was conducted concurrently and independently of th ese works. That said, there is very little overlap between ou r
results and the ones obtained in [ 18] and [ 12], which we discuss at length in Section 1.2.
3We will, throughout, abbreviate ‘with respect to’ as w.r.t.
2

Fair Division with Market V alues
Market
SD-EF1 EF1
Agents
SD-EF1 ✗ (Theorem 1) ?
EF1 ✓ (Corollary 1)
PO ✗ (Theorem 4) ✓ (Corollary 2)
MMS/EFX ✗ (Theorems 6 and 7)
Table 1: Summary of our results. PO on the market side is alway s guaranteed. Positive result with PO on the agents’
side is conditioned on strictly positive utilities. MMS and EFX impossibilities hold even when swapping sides (i.e.,
EF1/SD-EF1 on the agents’ side and MMS/EFX on the market side ), or demanding MMS/EFX on both sides.
Throughout, we identify a number of interesting and fundame ntal open questions.
1.2 Related Work
As mentioned previously, the works of Dall’Aglio [ 18] and Bu et al. [ 12] are the closest to ours. None of the results
obtained in Dall’Aglio [18] imply anything in our model, since this prior work addresses homogeneous divisible goods.
Bu et al. [12] study a generalization of our model with heterogeneous market valuations{vi}i∈N . They view{vi}i∈N
as the allocator’s preferences over which agent should get w hich item. Bu et al. [ 12] provide four existential results:
1. EF1 on both sides, when there is a single market valuation ( i.e., our model).
2. EF1 on both sides for the particular case of two agents.
3. PROP- O(log n) on both sides, where PROP (proportionality) is a notion weak er than envy-freeness.
4. PROP-2 on both sides under binary valuations.
The ﬁrst result in the above-mentioned list is studied in the current work as well. However, we show that, in the case
of goods (which is what Bu et al. address), the result is already implied by [ 9]. In the list above, the second result
is strong, but it does not come with an efﬁcient construction . In fact, they show how to achieve EF2 on both sides
in polynomial time, which we are able to improve to EF1, on bot h sides, in polynomial time. Their EF1 existential
result extends to monotone subjective utilities and monoto ne market values, whereas our EF1 result extends only to
monotone subjective utilities and additive market values ( though still with polynomial value query complexity). The
last two results in the list above address the weaker notion o f proportionality, which we do not focus on. In summary,
the technical overlap between [ 12] and the current work is little. The two works together, howe ver, point to interesting
open questions, which we highlight throughout.
A bit more broadly, fairness with respect to market values ca n be viewed as placing feasibility constraints (induced by
the market values) on the allocation. Hence, fair division w ith market values can be considered as case of constrained
fair division. Notably, many recent results address fair al locations subject to various feasibility constraints, suc h
as cardinality constraints [ 9], matroid constraints [ 19], or budget constraints [ 8]. As we show in this work, EF1
with respect to an additive market valuation can be achieved by placing appropriately deﬁned cardinality constraints.
However, it is not clear if EF1 with respect to a more general ( e.g., submodular) market valuation or with respect to
heterogeneous additive market valuations can be reduced to known constraints.
Our model is also related to recent works on fair division in t wo-sided markets [ 30, 23, 24], where agents on two
sides of a market are matched to each other, with agents on eac h side having preferences over those on the other side.
Freeman et al. [ 23] also seek EF1 on both sides, but in their case the second side has its own allocation, whereas in
our case, the market side is also evaluated using the same all ocation.
2 Preliminaries
An instance of fair division with market values is a quadrupl e,⟨N ,M, v, ⃗ u= (ui)i∈N⟩, whereN is a set of n agents,
M is a set of m indivisible goods, v : 2 M→ R/greaterorequalslant0 is a monotone set function indicating the market valuation o f the
goods, and ui : 2 M→ R/greaterorequalslant0 is the (subjective) monotone utility function of agent i∈N . In particular, ui(S) and v(S)
denote agent i’s value and the market value for subset of goods S⊆M , respectively. Throughout most of the paper,
we consider market valuation v and utilities ⃗ uthat are additive: recall that a set function f : 2 M→ R/greaterorequalslant0 is additive if
f (S) = ∑ g∈S f ({g}) for all S⊆M . Section 4.3, in particular, goes beyond additive utilities and conside rs general,
monotone ones. For notational convenience, we will write ui(g) := ui({g}) and v(g) := v({g}).
3

Fair Division with Market V alues
An allocation is n-partition A = ( A1, . . . , An) ofM, where Ai⊆M denotes the bundle of goods given to agent i.
Here, Ai∩ Aj =∅ for all i⁄= j and∪i∈N Ai =M. Our goal is to ﬁnd allocations that are fair with respect to b oth
subjective utilities and market valuation. A prominent fai rness criterion for indivisible goods is envy-freeness up t o
one good.
Deﬁnition 1 (Envy-free up to one good) . For an instance ⟨N ,M, v, (ui)i∈N⟩, we say that an allocation A =
(A1, . . . , An) is envy-free up to one good (EF1) with respect to subjective u tilities if, for every pair of agents i, j∈N ,
either Aj =∅ or ui(Ai) /greaterorequalslant ui(Aj\{ g}) for some good g∈ Aj. In addition, we say that A is EF1 with respect to
market values if the above-mentioned inequalities hold wit h ui replaced by v.
Next, we deﬁne a strengthening, SD-EF1, based on the stochas tic dominance (SD) relation.
Deﬁnition 2 (SD-preference [ 10]). For X, Y ⊆M , we say that agent i SD-prefers X to Y , denoted X ≽SD i Y , if,
for each good g∈M , it holds that |{g′∈ X : ui(g′) /greaterorequalslant ui(g)}| /greaterorequalslant|{g′∈ Y : ui(g′) /greaterorequalslant ui(g)}|. That is, for each
g, the subset X has at least as many goods with utility (to agent i) at least as much as g as Y does. Also, we deﬁne
SD-preference under the market valuation, denoted X ≽SD v Y , by replacing ui with v.
Deﬁnition 3 (SD-EF1 [4]). An allocation A = ( A1, . . . , An) is said to be SD-envy-free up to one good (SD-EF1) if,
for every pair of agents i, j∈N , either Aj =∅ or Ai ≽SD i Aj\{ g} for some good g∈ Aj .
We will say that an additive function u :M→ R/greaterorequalslant0 induces a ranking (with ties) π :M→ [|M|] if π ranks the
goods in decreasing order of u, i.e., π(g) ⩽ π(g′) iff u(g) /greaterorequalslant u(g′) for all g, g′∈M . Here, a weaker notion is that of
consistency: u is said to be consistent with π if π(g) ⩽ π(g′) implies u(g) /greaterorequalslant u(g′) for all g, g′∈M .
Note that SD-EF1 is a stronger notion than EF1: if an allocati on is SD-EF1 with respect to utilities (ui)i∈N , then it
must be EF1 with respect to (ui)i∈N , as well as with respect to any other utility proﬁle (u′ i)i∈N where, for each i, the
utility u′ i is consistent with the ranking πi induced by ui.
The following lemma provides a useful observation about SD- EF1 with respect to a proﬁle with identical valuations;
recall that the market valuation can be seen as such a proﬁle.
Lemma 1. Let π :M↔ [m] be a strict ranking over M. If ui induces π for every i∈N , then A is SD-EF1
with respect to (ui)i∈N iff, for all agents i∈N and each index ℓ∈{ 1, 2, . . . ,⌈m/n⌉}, we have |Ai∩{ a∈M :
nℓ− n + 1 ⩽ π(a) ⩽ nℓ}| ⩽ 1. Further , if u′ i is consistent with π for every i∈N , then such an allocation is still
SD-EF1 with respect to (u′ i)i∈N .
Proof. For ℓ∈ [⌈m/n⌉], let Cℓ ={g∈M : nℓ− n + 1 ⩽ π(g) ⩽ nℓ}. First, we prove the if and only if condition.
(⇒) Suppose this is not true. Let k be the smallest value for which there exists an agent j with|Aj∩ Ck| > 1, and
since|Ck| ⩽ n, there must exist another agent i with|Ai∩ Ck| = 0. By the choice of k, for all ℓ < k and agent i, we
must have|Ai∩ Cℓ| ⩽ 1, and since|Cℓ| = n, this would imply|Ai∩ Cℓ| = 1 . Now, since|Aj∩ Ck| /greaterorequalslant 2, consider
any two goods g, g′∈| Aj∩ Ck| and, without loss of generality, suppose g≻π g′. Taking T ={g′′∈M : g′′≻π g′},
we see that|Ai∩ T| = k− 1 whereas|Aj∩ T| = k + 1, violating the SD-EF1 property.
(⇐) Suppose A is an allocation satisfying the given condition. Consider a ny two agents i and j, and any good g∈M .
Let T ={g′∈M : g′≻π g}. We want to prove that |Ai∩ T| /greaterorequalslant|Aj∩ T|− 1. Suppose g∈ Ck. Then, the desired
condition follows from observing, as above, that |Ai∩ Ck′| =|Aj∩ Ck′| = 1 for all k′ < k (for which|Ck′| = n)
and|Aj∩ Ck| ⩽ 1.
For the last part of the lemma, it sufﬁces to observe that when u′ i is consistent with π, for every good g∈M , there
exists a good g′∈M such that{g′′∈M : u′ i(g′′) /greaterorequalslant u′ i(g)} ={g′′∈M : g′′≻π g′}. Hence, SD-EF1 with respect
to π imposes a strictly greater set of conditions than SD-EF1 wit h respect to ⃗ u′.
3 Simultaneous Envy-Freeness
This section ﬁrst shows that the strong notion of SD-EF1 cann ot be guaranteed w.r.t. both the subjective utilities and
the market valuation simultaneously.
Theorem 1. There exists an instance with 2 agents and 7 goods in which no allocation is SD-EF1 w.r .t. both the
subjective utilities and the market valuation.
4

Fair Division with Market V alues
Proof. Let π = ( g1≻ g2≻ g3≻ g4≻ g5≻ g6≻ g7) be the ranking induced by the market values, and those
induced by the subjective utilities of the two agents be
σ1 = (g1≻ g3≻ g2≻ g5≻ g4≻ g7≻ g6),
σ2 = (g1≻ g5≻ g2≻ g3≻ g6≻ g7≻ g4).
The impossibility result stated in the theorem will hold for any subjective utilities and market valuation that induce t he
above-mentioned rankings.
By Lemma 1, SD-EF1 w.r.t. the market valuation demands that each agent receive exactly one good from each of the
sets C1 ={g1, g2}, C2 ={g3, g4}, and C3 ={g5, g6}.
Suppose agent 1 receives good g1. Then, agent 2 must receive both good g5 (for SD-EF1 w.r.t. the subjective utilities)
and good g2 (for SD-EF1 w.r.t. the market values). Then, considering th e top four goods in σ1, agent 1 must receive
g3 to satisfy SD-EF1 w.r.t. its subjective utility. Next, reca lling the constraints imposed by SD-EF1 w.r.t. market
values through sets C2 and C3 above, we conclude that agent 2 must get g4 and agent 1 must get g6. So far, we have
{g1, g3, g6}⊆ A1 and{g2, g4, g5}⊆ A2. Since both agents have only two of their top six goods, both a gents would
need to have g7 in order to satisfy SD-EF1 w.r.t. their subjective utilitie s, which is a contradiction.
The case of agent 2 receiving good g1 leads to a similar argument, where we can deduce {g2, g3, g6} ⊆A1 and
{g1, g4, g5} ⊆A2. Hence, in this case as well, both agents would require g7 for SD-EF1 w.r.t. their subjective
utilities, which is a contradiction.
We complete the picture by providing positive results for ac hieving SD-EF1 w.r.t. both the subjective utilities and the
market values in two special cases.
Theorem 2. In instances with two agents and at most six goods, there alwa ys exists an allocation that is SD-EF1 w.r .t.
both the subjective utilities and the market valuation.
Proof. We propose a cut-and-choose style algorithm. By invoking Theorem 3 for v as the market valuation and u1
as the identical utilities, we ﬁnd a two-bundle partition of goods (A1, A2) that satisﬁes SD-EF1 w.r.t. both u1 and v.
Agent 1 accepts both bundles A1 and A2 with no SD-EF1 violation.
We will show that agent 2 accepts at least one of the two bundles towards SD-EF1 w.r.t. utility u2. Write π2 to denote
the ranking induced by utility u2 and, for each index ℓ∈ [m], letM2,ℓ :={g∈M| π2(g) ⩽ ℓ}. That is,M2,ℓ is the
set of the top ℓ goods under agent 2’s utility u2.
Also, write eℓ :=|A1∩M 2,ℓ|−| A2∩M 2,ℓ| to capture the split of the top- ℓ goods between the two subsets A1 and
A2. Note that, if, for all indices ℓ∈ [m], we have eℓ /greaterorequalslant−1, then allocating A1 to agent 2 satisﬁes SD-EF1 for her. This
follows from the fact that, in such a case, agent 2 receives at most one item less than agent 1 in eachM2,ℓ. Similarly,
if eℓ ⩽ 1 for all ℓ∈ [m], allocating A2 to agent 2 satisﬁes SD-EF1 for her. Next, we show that at least one of the
two conditions must hold. Suppose by contradiction that the re exists an ℓ1, ℓ2∈ [m] such that eℓ1 /greaterorequalslant 2 and eℓ2 ⩽−2.
Since|eℓ1− eℓ2| /greaterorequalslant 4, either|A1| /greaterorequalslant 4 or|A2| /greaterorequalslant 4, which contradicts the fact that the bundle sizes are balanc ed, i.e.,
max{|A1|,|A2|} ⩽⌈m/2⌉ ⩽ 3, where the last inequality follows from the assumption that m ⩽ 6. The theorem
stands proved.
Theorem 3. When the subjective utilities of the agents induce the same r anking over the goods, an allocation that is
SD-EF1 w.r .t. the subjective utilities and the market valuation always exists, and can be computed in polynomial time.
Proof. If m is not divisible by n, add dummy goods such that the number of items becomes divisi ble by n. For each
dummy good both market value and subjective utility for all t he agents is equal to 0. Now, by construction, we have
setM′ of m′ = nk items. Considering this integer k, construct a bipartite graph G with vertices{w1, . . . , wk} on the
left side and{z1, . . . , zk} on the right side.
Let πv be the ranking induced the market valuation v. Also, let πu be a ranking consistent with all the subjective
utilities ui. By the theorem assumption, such a ranking πu exists.
For any good a∈M ′, let ra, r′ a∈ [m′] be the ranks of a w.r.t. the two orderings, respectively, i.e.,πv(ra) = πu(r′ a) =
a. Then, in the bipartite graph G, include an edge from w⌈ra/n⌉ to z⌈r′a/n⌉ with label a. Note that, each vertex in G is of degree n. The n-regular bipartite graph G can be decomposed into n perfect matchings, by Hall’s theorem. Let the
bundle allocated to agent i be the set of goods labeled on the edges of the i-th matching. Note that each item is used as a
label of a single edge, so the bundles are disjoint. In additi on, for every index ℓ∈ [k], each bundle has exactly one item
5

Fair Division with Market V alues
a, with ra∈{ nℓ− n + 1, . . . , nℓ} and exactly one item b, with r′ b∈{ nℓ− n + 1, . . . , nℓ}. After removing the dummy
items we have|Ai∩{a∈M : nℓ−n+1 ⩽ ra ⩽ nℓ}| ⩽ 1, and similarly|Ai∩{a∈M : nℓ−n+1 ⩽ r′ a ⩽ nℓ}| ⩽ 1
for ℓ∈ [k]. Therefore, by Lemma 1, allocation A is SD-EF1 w.r.t. both market values and subjective utilitie s.
Next, let us consider relaxing the goal of SD-EF1 to (the regu lar) EF1, at least on one side. Doing so on the market
side leads to the following open problem, which seems to requ ire considerably novel ideas towards a resolution.
Open Question 1: Does there always exists an allocation that is SD-EF1 w.r.t. the subjective utilities and
EF1 w.r.t. the market valuation?
When we relax SD-EF1 to EF1 on the agents’ side, a positive res ult emerges, even in the general case. We remark that
Bu et al. [ 12] prove the existence of an allocation that is EF1 w.r.t. both the subjective utilities and the market values.
Upon careful observation, however, one ﬁnds that not only do they actually achieve SD-EF1 w.r.t. the market values,
but in fact, their algorithm is precisely an instantiation o f a more general algorithm designed previously by Biswas
and Barman [ 9]. In other words, this problem can be reduced to the result of Biswas and Barman [ 9]; we lay out the
simple reduction here, highlighting that there is no need to derive this result from scratch.
Biswas and Barman [ 9] consider a setting in which there are no market values, but w e are given a partition
{M1, . . . ,Mℓ} of the goods along with cardinality bounds h1, . . . , hℓ∈ Z+. The goal here is to ﬁnd a fair allo-
cation A that satisﬁes cardinality constraints: |Ai∩M k| ⩽ hk for each k∈ [ℓ] and agent i∈N . Note that, we
need the bound hk /greaterorequalslant⌈|Mk|/n⌉, for each k∈ [ℓ], to even ensure the existence of an allocation which satisﬁe s the
cardinality constraints. Biswas and Barman [ 9] show that, in such a case, an EF1 allocation satisfying the c ardinality
constraints is guaranteed to exist.
For our reduction, we consider πv the ranking induced by the market valuation v. Then, we set ℓ :=⌈m/n⌉, and, for
each k∈ [ℓ], deﬁneMk :={g∈M : ( k− 1)n < π v(g) ⩽ kn}. That is, M1 is the set of top n goods according
to the market values,M2 is the set of next n goods according to the market values, and so on. Finally, we i mpose the
cardinality constraints|Ai∩M k| ⩽ 1 for all i∈N and k∈ [ℓ]. From Lemma 1, we see that this implies SD-EF1 w.r.t.
the market values. The polynomial-time algorithm of Biswas and Barman [ 9] then immediately yields an allocation
that is EF1 w.r.t. the subjective utilities while satisfyin g the cardinality constraints (and, hence, SD-EF1 w.r.t. th e
market values).
Corollary 1. An allocation that is EF1 w.r .t. the subjective utilities an d SD-EF1 w.r .t. the market valuation always
exists, and can be computed in polynomial time.
4 Extensions to Other Criteria
Let us now extend our setup of fair division with market value s to (i) consider other desiderata such as Pareto optimal-
ity, MMS, and EFX, and (ii) go beyond additive utilities.
4.1 Pareto Optimality
Deﬁnition 4 (Pareto Optimality) . An allocation A is said to be Pareto optimal (PO) w.r.t. the subjective utilities if
there is no allocation A′ with the property that ui(A′ i) /greaterorequalslant ui(Ai), for all i∈N , with at least one inequality being
strict.
Appendix A addresses a strengthening called fractional Pareto optimality (fPO), which demands that not even a frac-
tional allocation (where the goods may be fractionally assi gned to agents) Pareto dominates the given integral one.
First, we note that every allocation is trivially PO w.r.t. t he market values. Hence, the only interesting consideratio n
is to demand PO w.r.t. the subjective utilities. Here, we sho w that PO cannot be achieved with SD-EF1 (Theorem
4). Interestingly, SD-EF1 implies both EF1 and balancedness (|Ai|∈{⌊ m/n⌋,⌈m/n⌉} for all i), and both these
relaxations can individually be attained together with PO [ 14, 17].
Theorem 4. There exists an instance with 2 agents and 6 goods in which the re is no allocation that is PO w.r .t. the
subjective utilities and SD-EF1 w.r .t. the market valuation.
Proof. Consider an instance with two agents with the following subj ective utilities for goods g1, . . . , g6:
In addition, let the additive market valuation be identical to the utility of the ﬁrst agent, i.e., v = u1. Note that both
agents must receive three goods, respectively, to ensure SD -EF1 (across the six goods) w.r.t. the market valuation.
6

Fair Division with Market V alues
g1 g2 g3 g4 g5 g6
Agent 1 19 7 4 3 2 1
Agent 2 8 7 6 5 4 3
Since agent 1 would be happy to give up any three goods to receive g1 and agent 2 would be happy to accept any three
goods in exchange for g1, PO demands that g1 must be given to agent 1. Then, for SD-EF1, g2 must be given to agent
2.
Among the remaining four goods{g3, g4, g5, g6}, each agent must receive two goods in such a way that no agent g ets
both g3 and g4 (or equivalently, both g5 and g6). However, it is easy to see that agent 1 would be happy to give up
A1∩{ g3, g4, g5, g6} to receive{g2}, and agent 2 would also be happy to give up{g2} to receive A1∩{ g3, g4, g5, g6},
violating PO.
This leads us, in the PO context, to the following possibilit y: EF1+PO w.r.t. the subjective utilities and EF1 w.r.t. the
market values. We leave this as an open question.
Open Question 2: Does there always exists an allocation that is EF1+PO w.r.t. the subjective utilities and
EF1 w.r.t. the market values (or even balanced)?
Finally, relaxing SD-EF1 to EF1 w.r.t. the market values, we show that PO w.r.t. the subjective utilities can be attained
together with EF1 w.r.t. the market values. Note that if the m arket values of all goods are set to be equal, then EF1 is
equivalent to balancedness; thus, our result strictly stre ngthens the known result that a balanced PO allocation alway s
exists Conitzer et al. [ 17].
In fact, we prove a slightly more general result, whereby we a llow the market values to heterogeneous (where each
agent i has an additive market valuation vi) and achieve equitability up to one good (EQ1) [22] with respect to it.
Deﬁnition 5 (EQ1). An allocation A is called equitable up to one good (EQ1) w.r.t. a valuation pr oﬁle ⃗ v= ( vi)i∈N
if, for every pair of agents i, j∈N , either Aj =∅ or vi(Ai) /greaterorequalslant vj(Aj\{ g}) for some good g∈ Aj.
Freeman et al. [ 22] prove that an allocation satisfying EQ1+PO does not always exist, but it does (and even EQ1+fPO
can be guaranteed) when all values are nonzero (i.e., strict ly positive). To obtain EQ1 and PO w.r.t. two different
valuation proﬁles, respectively, it is clear that the proﬁl e w.r.t. which we want PO must have nonzero values. 4 We
show that PO (even fPO) w.r.t. a nonzero valuation proﬁle and EQ1 w.r.t. a different valuation proﬁle can be attained,
strictly strengthening the result of Freeman et al. [ 22].
Theorem 5. An allocation that is fPO w.r .t. nonzero subjective utiliti es (ui)i∈N and EQ1 w.r .t. (heterogeneous)
market valuations (vi)i∈N always exists, and can be computed in time polynomial in n, m, and V , where V =
maxi∈N|{vi(S) : S⊆M}| is the maximum number of distinct value levels for any i.
Since both proﬁles are heterogeneous, one can swap them to ac hieve EQ1 w.r.t. subjective utilities and fPO w.r.t.
heterogeneous nonzero market values as well. Since EQ1 and E F1 coincide when the market valuations are identical,
vi = v for i, which is the case we consider throughout the paper, we obtai n the following corollary.
Corollary 2. There always exist an allocation that is fPO w.r .t. nonzero s ubjective utilities and EF1 w.r .t. the market
valuation.
4.2 MMS and EFX
In addition to EF1, two fairness criteria that have received signiﬁcant attention in the discrete fair division are max-
imin share fairness (MMS) and envy-freeness up to any good (EFX). Here, we show that these notions lead to stark
impossibilities in our setup of fair division with market va lues.
Deﬁnition 6 (α-MMS). Under utilities (ui)i∈N , the maximin share of agent i is deﬁned as µi :=
max(B1,...,Bn) mink∈[n] ui(Bk); here the max is considered over all n-partitions of M. For α∈ [0, 1], an allo-
cation A is said to be α-MMS, w.r.t. subjective utilities, if ui(Ai) /greaterorequalslant α· µi for all agents i∈N .
4Otherwise, consider an example in which three goods are posi tively valued only by agent 1, and a fourth good is positively
valued only by agent 2. The only PO allocation is to give the ﬁrst three goods to agen t 1 and the fourth good to agent 2. However,
this is not EQ1 w.r.t. a different valuation proﬁle where all agents value all goods at 1.
7

Fair Division with Market V alues
We know that EF1 implies (1/n)-MMS [14]. Hence, in the guarantee of Corollary 1 (EF1 w.r.t. the subjective utilities
and SD-EF1 w.r.t. the market values), the fairness property on one or both sides can be replaced by (1/n)-MMS.
However, the following result shows that this is the best one can hope for, despite the fact that in the traditional fair
division setup, even
( 3
4 + 1 12n ) -MMS is known to be exist [ 1].
Theorem 6. F or anyα > 1/n, there exists an instance with two identical valuation proﬁ les (either one can be viewed
as consisting of identical subjective utilities and the oth er as consisting of market values) in which no allocation is
simultaneously α-MMS w.r .t. the ﬁrst proﬁle and either EF1 or α-MMS w.r .t. the second,
Proof. Consider an instance with n agents and 2n− 1 goods, where the goods are partitioned into two sets, M1 with
n goods andM2 with n− 1 goods. Consider two identical valuation proﬁles with funct ions u and v as follows:
u(g) =
{1 g∈M 1
n g ∈M 2
, v (g) =
{1 g∈M 1
0 g∈M 2
.
Note that EF1 or α-MMS (for any α > 0) w.r.t. v requires that each agent receive exactly one good from M1. Since
|M2| < n, there exists an agent i∈N who does not receive any good fromM2. For this agent, ui(Ai) = 1 whereas,
under u, the maximin share µi = n, causing a violation of α-MMS w.r.t. u, for any α > 1/n.
Deﬁnition 7 (α-EFX). For α∈ [0, 1], allocation A is said to be α-envy-free up to any good ( α-EFX), w.r.t. the
subjective utilities, if, for every pair of agents i, j∈N , either Aj =∅ or ui(Ai) /greaterorequalslant α· ui(Aj\{ g}) for every g∈ Aj.
Theorem 7. F or anyα∈ (0, 1], there exists an instance with two identical valuation proﬁles (either one can be viewed
as consisting of identical subjective utilities and the oth er as market values) in which no allocation is simultaneousl y
EF1 w.r .t. the ﬁrst proﬁle and α-EFX w.r .t. the second.
Proof. Consider an instance with 2 agents, 4 goods{g1, g2, g3, g4}, and two identical valuation proﬁles with valuation
functions u and v as follows: u(gt) = 1 for all t∈ [4], v(g1) = 2 /α + 1, and v(gt) = 1 for t∈{ 2, 3, 4}.
Note that EF1 w.r.t. u requires that each agent receive two goods. Consider any all ocation A. Without loss of
generality, assume that agent 1 receives g1 and g2. Then, v(A2) = 2 whereas α v (A1\{ g2}) = 2 + α > 2,
demonstrating a violation of α-EFX.
Remark 1. Since EFX implies EF1, we can replace EF1 with EFX in Theorem 6 to deduce that EFX w.r.t. one proﬁle
and α-MMS (for any α > 1 n ) w.r.t. to the other cannot be guaranteed.
4.3 Monotone V aluations
This section addresses whether one can extend the positive r esult of Corollary 1 to hold beyond additive valuations.
That is, we consider whether EF1 can be achieved simultaneou sly for monotone (but not necessarily additive) subjec-
tive utilities and market valuation. 5
We are interested in the broad classes of monotone, subaddit ive valuations. A valuation function f : 2 M→ R/greaterorequalslant0 is
said to be monotone if f (X) ⩽ f (Y ), for all X⊆ Y ⊆M , and subadditive if f (X∪ Y ) ⩽ f (X) + f (Y ) for all
X, Y⊆M .
An allocation that is EF1 w.r.t. monotone subjective utilit ies is guaranteed to exist [ 28]. Notably, with market values,
the question remains open.
Open Question 3: Does there always exist an allocation that is EF1 w.r.t. two h eterogeneous monotone
valuation proﬁles simultaneously (i.e., w.r.t. monotone subjective utilities and heterogeneous monotone market
values)? What if one of the proﬁles consisted of additive val uations?
In fact, consider the special case of (homogeneous) additiv e market values where every good has the same market
value. Then, EF1 w.r.t. such market values is simply balance dness, yielding the following tantalizing open question
for the usual fair division setup without market values.
Open Question 4: Does there always exist a balanced EF1 allocation w.r.t. a (h eterogeneous) monotone
valuation proﬁle?
5SD-EF1 is not well-deﬁned beyond additive valuations: ther e is no natural ordering over individual goods induced by a mo no-
tone valuation, and even if one were to induce it somehow, it w ould not sufﬁce to guarantee EF1 w.r.t. every monotone valua tion
inducing it. Hence, we limit our attention to EF1.
8

Fair Division with Market V alues
While these questions remain open, we prove the existence of an allocation that is 1/2-EF1 w.r.t. subadditive subjective
utilities and SD-EF1 w.r.t. additive market values. Formal ly, for α∈ [0, 1], an allocation A is said to be α-EF1 w.r.t.
subjective utilities (ui)i∈N if, for each pair of agents i, j∈N (with Aj⁄=∅), we have ui(Ai) /greaterorequalslant α u i(Aj\{ g}) for some good g∈ Aj. Here, we use the idea of minimally envied subsets from [ 15].
Minimal Envied Swap (MES) Algorithm. As we did for establishing Corollary 1, we consider πv the ranking
induced by the (additive) market valuation v. Then, we partition the items into (M1, . . . ,M⌈m/n⌉) such thatMk :=
{g ∈ M: ( k− 1)n < π v(g) ⩽ kn}. As noted previously, for any allocation A, if |Ai∩M k| ⩽ 1 for each
k∈ [⌈m/n⌉] and all agents i, then A is SD-EF1 w.r.t. v. We now provide an algorithm that ﬁnds such an allocation
that is 1/2-EF1 w.r.t. monotone, subadditive subjective utilities.
We start with an allocation A with empty bundles, Ai =∅, for all agents i∈N . Also, initialize ‘charity’ C =M as
the set of all the unallocated goods. A subset T⊆ C is said to be an envied feasible subset of the charity if (1) there
exists an agent i∈N envying it, i.e., ui(Ai) < u i(T ), and (2)|T∩M k| ⩽ 1 for each k∈ [⌈m/n⌉]. Further, we say
that an envied feasible subset T⊆ P is minimal if no agent envies any strict subset of T . It is easy to verify that while
there exists an envied feasible subset of the charity, there also exists a minimal envied feasible subset of the charity.
The algorithm now works in two phases.
Phase 1: While there exists a minimal envied feasible subset T of the charity C, select an agent i who envies T , and
update Ai = T and charity (unallocated good) C =M\ (∪i∈N Ai).
Phase 2: Once Phase 1 has terminated, allocate goods in C arbitrarily subject to maintaining |Ai∩M k| ⩽ 1 for all
agents i∈N and each k∈ [⌈m/n⌉].
Theorem 8. Every fair division instance with (monotone) subadditive s ubjective utilities and additive market values
admits an allocation that is 1/2-EF1 w.r .t. subjective utilities and SD-EF1 w.r .t. market v aluation. Further , such an
allocation is returned by the MES algorithm detailed above.
Proof. First, we argue that the algorithm terminates and returns an allocation that is SD-EF1 w.r.t. the market values.
Note that each iteration of Phase 1 strictly increases the ut ility of the selected agent, and the utilities of the remaini ng
agents remain unchanged. Hence, Phase 1 must terminate. Fur ther, throughout the execution of Phase 1, the selected
subset of goods T is feasible, i.e., throughout, we maintain |Ai∩M k| ⩽ 1 for each i∈ Nand k ∈ [⌈m/n⌉].
Therefore, at the end of Phase 1 and for each k, the number of agents with exactly one good from Mk is equal to
|Mk\ C|. This observation implies that there remain n−|M k\ C| agents who can each still receive a good from
Mk, while maintaining the cardinality constraint. Since |Mk| ⩽ n, we obtain the following bound for the unassigned
goods|Mk∩C| ⩽ n−|M k\ C|. Hence, we can allocate the unassigned goods inMk∩C, one each, to the remaining
agents while maintaining the feasibility constraints. As n oted above, this ensures SD-EF1 w.r.t. the market values.
To show that the returned allocation is 1/2-EF1 w.r.t. the utilities, we note that the initial allocati on (with empty
bundles) is EF1. Further, during Phase 1, when we assign Ai = T , no agent envies any strict subset of Ai. Therefore,
the allocation remains EF1 even after the swap and, hence, th e EF1 property is maintained till the end of Phase 1.
During Phase 2, each agent i receives a subset of goods Bi⊆ C that is feasible (|Bi∩M k| ⩽ 1 for all k) and, hence,
is not envied by any other agent j. This follows from the fact that there are no envied feasible subsets of the charity
C left after Phase 1. Finally, the subadditivity of the utilit ies ensures that the ﬁnal allocation is 1/2-EF1. The theorem
stands proved.
Next, we provide an exact version of Theorem 8 for the special case of two agents. The proof of this theorem c losely
follows from a result of Kyropoulou et al. [ 27]. Speciﬁcally, in Corollary 5.3, they show that for two agen ts with
(arbitrary) monotone subjective utilities, there always e xists a balanced EF1 allocation. In particular, their algor ithm
arbitrarily pairs up the goods and ensures that in the ﬁnal EF 1 allocation the two goods in each pair are given to
different agents. We utilize this result to obtain the corol lary below. Write πv to denote the ranking induced by the
additive market valuation v and pair the goods as (πv(1), πv(2)), (πv(3), πv(4)), . . . ,(πv(m− 1), πv(m)).6 Note that
if the two agents, respectively, receive exactly one good from every pair, then we get SD-EF1 w.r.t. market values. This
reduction yields the result below. One can also verify that t he algorithm of Kyropoulou et al. [ 27] can be simulated
with polynomially many value queries to the subjective util ities (where, in a single query, one asks for the utility of an
agent for a bundle of goods).
6If m is odd, we can add a dummy good at the end, and let both agents ha ve zero marginal subjective utility for it. Removing
this good in the end preserves both our desired properties. T his is how Kyropoulou et al. [ 27] handle an odd number of goods as
well.
9

Fair Division with Market V alues
Theorem 9. F or the case of two agents, there always exists an allocation that is EF1 w.r .t. monotone subjective
utilities and SD-EF1 w.r .t. additive market values, and it c an be computed using polynomially many value queries.
5 Cake Division
This section extends our fair division with market valuatio n setup to heterogeneous divisible goods, i.e., to the canon -
ical setting of cake cutting. First, we brieﬂy introduce the cake-cutting model. The cake is represented by the interval
[0, 1]. A piece of the cake is a Borel subset of [0, 1]. V aluations over the cake are deﬁned via density functions. Specif-
ically, under an integrable density function f : [0, 1]→ R/greaterorequalslant0, the value assigned to any piece X of the cake is denoted
(with a slight abuse of notation) as f (X) := ∫ X f (x) dx; this induces a (countably additive) measure over the cake
that is absolutely continuous with respect to the Lebesgue m easure and, hence, non-atomic. 7
LetN denote a set of n agents participating in the cake division. An allocation A = ( A1, . . . , An) is a partition of
the cake [0, 1] into n pairwise-disjoint8 pieces. Each agent i∈N has a subjective density function ui; her utility in
allocation A = ( A1, . . . , An) is ui(Ai). Also, there is a market density function v that captures the market values of
the pieces, i.e., v(X) denotes the market value of piece X.
An allocation A = (A1, . . . , An) is envy-free (EF) w.r.t. subjective utilities if ui(Ai) /greaterorequalslant ui(Aj) for all agents i, j∈N ,
and envy-free with respect to the market valuation if v(Ai) = v(Aj ) for all i, j∈N .
5.1 Envy-Free Cake Division
In this section, we study the existence and properties of cak e allocations that are envy-free both w.r.t. subjective
utilities and market valuation. The existence of such an all ocation is rather easy to establish (as we note below), hence ,
we focus on two questions: (a) how many cuts are required in su ch an allocation, and (b) how many queries must be
made in the Robertson-Webb model to ﬁnd such an allocation.
5.1.1 Number of Cuts
This subsection obtains upper and lower bounds on the number of cuts (i.e., the total number of intervals across all
the pieces) required for the desired envy-free allocations . First, we provide a lower bound: There exist cake division
instances wherein at least 2n− 2 cuts are required to achieve simultaneous envy-freeness.
Theorem 10. There exists cake division instances wherein any allocatio n that is envy-free—both w.r .t. the subjective
utilities and the market valuation—has at least 2n− 2 cuts. This lower bound holds even when the agents’ utilities are
identical.
Proof. Consider an instance in which the agents’ (identical) densi ty function u is 2 over [0, 1/2] and 0 over [1/2, 1].
Also, the market density function v is 1 over the entire cake [0, 1].
Consider any allocation A = ( A1, . . . , An) that is EF with respect to both u and v. For A to be EF with respect to
u (for the n agents), it must be the case that [0, 1/2] is divided equally, by length, between the n pieces A1, . . . , An.
Such a division requires at least n− 1 cuts in [0, 1/2].
Analogously, for EF under v, the entire cake [0, 1] must also be divided equally—by length—between the n pieces.
Now, given that [0, 1/2] is already divided equally, the same also holds for [1/2, 1]. This requires at least n− 1 cuts
in [1/2, 1] as well. Hence, in total, at least 2n− 2 cuts are necessary to obtain EF allocation A. The theorem stands
proved.
Complementing the lower bound in Theorem 10, we next show that envy-freeness for n subjective utilities and a
market valuation can be achieved simultaneously with n(n− 1) cuts. We obtain this upper bound by invoking the
following (necklace splitting) result of Alon [ 2] that guarantees existence of perfect cake divisions.
Theorem 11 ([2]). Given any t density functions µ1, . . . , µt, there exists an n-division A = (A1, . . . , An) of the cake
with at most t(n− 1) cuts and the property that µi(Ak) = 1/n, for all i∈ [t] and each k∈ [n]. That is, A provides an
equal division under all the t densities.
Note that Theorem 11 holds for any number of densities t. The theorem leads to the following fairness guarantee.
7Integrating a density function is equivalent to assuming th e measure to be absolutely continuous with respect to the Leb esgue
measure, while non-atomicity of the measure is a weaker cond ition; see [ 33, 34].
8The pieces are allowed to have an overlap of Lebesgue measure zero.
10

Fair Division with Market V alues
Theorem 12. In any cake division instance with n agents, there always exists a cake division that has at most n(n− 1)
cuts and is envy-free, under both the subjective utilities a nd the market valuation. Further , if the agents have identic al
utilities, then 2n− 2 cuts sufﬁce for inducing simultaneous envy-freeness.
Proof. For a cake division instance wherein the n agents have subjective utilities u1, . . . , un, we invoke Theorem 11
with t = n. In particular, we set the ﬁrst t− 1 (= n− 1) densities as follows: µi = ui, for 1 ⩽ i ⩽ t− 1, and set
the last density µt = v. The resulting allocation A will have t(n− 1) = n(n− 1) cuts. Then, we let the nth agent
select her most preferred piece in A, and assign the remaining pieces arbitrarily among the ﬁrst n− 1 agents. Index
the pieces of A such that An denotes the piece selected by agent n and Ai is the piece assigned to agent i∈ [n− 1].
The allocation is envy-free for agent n, since she selects her most preferred piece. Further, the eq ual-divisions property
from Theorem 11 ensures that, for each agent i∈ [n− 1] and all j ∈ [n], we have ui(Ai) = µi(Ai) = 1/n =
µi(Aj) = ui(Aj ). That is, allocation A is envy-free for the agents. The equal-divisions property f or v = µn gives us
envy-freeness under the market valuation. This establishe s the ﬁrst part of the theorem.
For the second part, we apply Theorem 11 with t = 2 densities. In particular, we set µ1 = u, where u is the identical
utility across the agents, and µ2 = v. Here, the number of cuts is at most t(n− 1) = 2 n− 2. Note that equal division
under µ1 = u ensures EF for the agents. Also, equal division under µ2 = v ensures EF with respect to the market
values. This completes the proof.
The gap between Theorem 10 and Theorem 12 leaves open the following tantalizing question.
Open Question 5: Does there always exists an allocation of the cake with O(n) cuts that is envy-free w.r.t.
the subjective utilities and the market valuation?
We believe that the ﬂexibility of only having to achieve EF wi th respect to the subjective utilities (rather than an equal
division) should permit using o(n2) cuts, perhaps even just Θ(n) cuts.
5.1.2 Number of Queries
Recall that, in the standard Robertson-Webb query model for cake division, the work of Aziz and Mackenzie [ 3]
provides a protocol that ﬁnds envy-free division—under sub jective utilities—with a ﬁnite (albeit hyper-exponential )
number of queries. We note that, by contrast, a protocol with ﬁnite query complexity does not exist when envy-freeness
is additionally required w.r.t. market valuation.
We obtain this impossibility result by invoking the lower bo und of Procaccia and Wang [ 31] which shows that an
equitable cake division, even among two agents, cannot be computed usi ng ﬁnitely many queries. Speciﬁcally, a cake
division (X1, . . . , Xn) is said to be equitable w.r.t. densities µ1, . . . , µn if µi(Xi) = µj(Xj) for all i and j.
One can reduce equitable cake division—under two densities µ1 and µ2—to fair division with market valuation as
follows. Consider a cake-division instance with two agents whose identical subjective utilities are µ1. Also, let the
market valuation be µ2. Here, any division A = ( A1, A2) that is EF w.r.t. the subjective utilities µ1 and the market
valuation µ2 is equitable, µ1(A1) = µ1(A2) = 1 /2 and µ2(A2) = µ2(A1) = 1 /2. Hence, using the lower bound from
[31], we obtain that, with ﬁnitely many queries, one cannot ﬁnd a division that is EF simultaneously w.r.t. subjective
utilities and market valuation.
5.2 Pareto Optimality
This section addresses the inclusion of Pareto Efﬁciency as an additional desideratum in cake division. It is known that,
under agents’ subjective utilities, there always exists an cake allocation that is envy-free and Pareto optimal (PO) [ 38].
In particular, an allocation that maximizes the Nash social welfare (i.e., the product of agents’ utilities) is one such
fair and efﬁcient allocation [34]. Now, when considering the market valuation, note that any allocation will be trivially
PO.
Hence, an interesting question is whether there always exis ts a cake division that is EF and PO on the subjective side
as well as EF on the market side. It is easy to observe that, as i n the case of indivisible goods ( Section 4.1), such a
guarantee cannot be achieved if the agents’ densities are ze ro for parts of the cake. For example, consider an instance
with two agents such that agent 1 has positive density over [0, 2/3], but zero density over [2/3, 1]. By contrast, agent 2
has zero density in [0, 2/3], but positive value density over [2/3, 1]. Note that the only allocation A = (A1, A2) that is
PO with respect to these agents’ utilities entails A1 = [0 , 2/3] and A2 = [2/3, 1]. However, if the market density v is
uniform over the entire cake [0, 1], then EF for v would demand that the pieces assigned to the two agents have e qual
11

Fair Division with Market V alues
length. Since this does not hold for the PO allocation A, we get that the instance at hand does not admit an allocation
that is EF and PO on the subjective side, and EF on the market si de.
In fact, even if we assume that the agents’ subjective densit ies are strictly positive over the entire cake, the existenc e of
the desired allocation is not guaranteed. To establish this negative result, we adapt a construction of Brams et al. [ 11],
who used it to show that an allocation of the cake that is EF, PO , and equitable (EQ) under agents’ utilities does not
always exist. Recall that an allocation A = (A1, . . . , An) is said to be equitable if ui(Ai) = uj(Aj) for all agents i, j.
Brams et al. [ 11] proved the impossibility for n /greaterorequalslant 3 agents and we do the same. In particular, this negative negat ive
result even rules out a balanced EF and PO cake allocation; ba lancedness, the requirement that the piece allocated
to each agent has the same length, is equivalent to EF w.r.t. t he uniform market valuation, and is therefore a weaker
requirement than EF w.r.t. an arbitrary market valuation.
Notably, the requirements in [5] (i.e., EF, PO, and EQ) can be achieved together for two agent s. We leave it as an open
question whether, in the current context, a positive result can be obtained speciﬁcally for two agents.
Open Question 6: Does there always exist an allocation of the cake between n = 2 agents that is EF and PO
w.r.t. the subjective values and EF w.r.t. the market value?
0 0.5 1
0
1/3
1/2
1
3/2
5/3
u1(x)
u2(x)
u3(x)
Figure 1: An instance in which no balanced EF+PO allocation e xists.
Theorem 13. There exists a cake-division instance, with 3 agents, wherein no allocation is simultaneously balanced,
EF , and PO. Consequently, EF and PO w.r .t. the subjective uti lities and EF w.r .t. the market valuation cannot be
guaranteed in general.
Proof. Consider an instance with three agents and subjective densi ty functions, u1, u2, u3, deﬁned as follows (see also
Figure 1):
u1(x) =
{ 5
3− 8 3 x for x∈ [0, 0.5],
5
3− 8 3 (1− x) for x∈ [0.5, 1].
u2(x) =
{ 3
2− 2x for x∈ [0, 0.5],
3
2− 2(1− x) for x∈ [0.5, 1].
u3(x) = 1 for x∈ [0, 1]
The market density function v is uniform over the whole cake. Hence, EF w.r.t. the market va lues corresponds to
balancedness (i.e., the pieces of the three agents must have equal Lebesgue measure).
First, we narrow down the space of candidate allocations using a result of Barbanel and Zwicker [6] that an allocation A
of the cake is PO iff it maximizes some weighted welfare, i.e., A∈ arg maxB
∑3
i=1 wi·ui(Bi) for some w1, w2, w3 > 0. Further, note that a weighted welfare is maximized iff each portion of the cake is allocated to an agent with the
highest weighted density for it.
This observation and the symmetry (around 1/2) in the agents’ utilities imply that, in any PO allocation, a gent 3 must
be assigned the piece [x∗, 1− x∗] for some x∗∈ [0, 1/2]. Since the desired allocation has to be balanced, we obtain
that agent 3 must receive the piece [1/3, 2/3]. Further, the weighted densities of agents 1 and 2 must intersect at 1/6
and 5/6, so that one of those two agents receives [0, 1/6]∪ [5/6, 1] while the other receives [1/6, 1/3]∪ [2/3, 5/6].
Since both agents have higher utility for [0, 1/6]∪ [5/6, 1], the agent receiving [1/6, 1/3]∪ [2/3, 5/6] envies the
other.9
9Further inspection tells us that the only balanced PO allocation is where A1 = [0, 1/6]∪[5/6, 1], A2 = [1/6, 1/3]∪[2/3, 5/6],
and A3 = [1/3, 2/3], and this maximizes weighted welfare where w1 : w2 : w3 = 126/110 : 6 /5 : 1 .
12

Fair Division with Market V alues
If one wishes to forgo EF w.r.t. the subjective utilities, we show that there exists an allocation that is ǫ-PO w.r.t. the
subjective utilities and EF w.r.t. the market valuations, w hen the subjective density functions are strictly positive . This
is an analogue of Theorem 5 in the cake-cutting model. In fact, we prove a more general result and allow heterogeneous
market valuations, whereby each agent i has a (possibly different) market density function vi.
Theorem 14. F or a cake-division instance with strictly positive subjec tive utility functions that are Lipschitz contin-
uous and heterogeneous market values, there always exists a n allocation of the cake that is ǫ-PO w.r .t. the subjective
utilities and EQ w.r .t. the market values.
An allocation A is equitable (EQ) with respect to market valuations if vi(Ai) = vi′ (Ai′ ) for all agents i, i′∈N . A
function f : [0 , 1]→ R/greaterorequalslant0 is K-Lipschitz if|f (x)− f (y)| ⩽ K|x− y| for all x, y∈ [0, 1]. Next, we deﬁne ǫ-Pareto
optimality.
Deﬁnition 8 (ǫ-Pareto optimality) . For a given ǫ > 0, an allocation A is ǫ-Pareto optimal w.r.t. density functions
{ui}i∈N if there does not exist another allocation A′ for which ui(A′ i) /greaterorequalslant ui(Ai) + ǫ for all i∈N .
We use the Lipschitz continuity assumption in Theorem 14 to approximate the subjective utilities with piecewise
constant density function as closely as needed, as is simila rly done in Cohler et al. [ 16] and Reijnierse and Potters
[32]. A piecewise constant function h can be expressed with a union of ﬁnitely many intervals such t hat h is a constant
function over each interval.
Lemma 2 (Cohler et al. [ 16], Reijnierse and Potters [ 32]). Given a real number ǫ > 0 and a K-Lipschitz density
function v : [0 , 1]→ R/greaterorequalslant0, there exists a piecewise constant function h such that v(x) ⩽ h(x) < v (x) + ǫ/2 for all
x∈ [0, 1].
Proof. Partition the cake [0, 1] into⌈4K/ǫ⌉ many intervalsI of length at most ǫ/4K. For each interval I∈I , let
h(x) = sup x∈[l,r] v(x) for x∈ I. This way, f (x) ⩽ h(x) and by the Lipschitz continuity and that the intervals are of
length at most ǫ/4K we have f (x) ⩽ v(x) + ǫ/4 < v (x) + ǫ/2.
To proveTheorem 14, we round the subjective density functions as in Lemma 2, and use the following result to achieve
(exact) Pareto optimality w.r.t. the rounded subjective ut ilities and EQ w.r.t. market values. This is the crux of the
whole result, and its detailed proof is presented in Appendix C.
Theorem 15. F or a cake division instance with strictly positive piecewise constant subjective density functions
{ui}i∈N and heterogeneous market valuations{vi}i∈N , there always exist an allocation of the cake that is PO w.r .t .
the subjective utilities and EQ w.r .t. the market values.
The proof of Theorem 14 is simply a corollary of Theorem 15 and Lemma 2.
Proof of Theorem 14. We approximate the subjective utilities as in Lemma 2 and obtain ⃗ u′ ={u′ i}i∈N . By invoking
Theorem 15 with ⃗ u← ⃗ u′ and vi← v, we get an allocation A which is PO w.r.t. ⃗ u′ and EQ w.r.t. v. Since EQ and
EF coincide when the market valuations are identical, A is EF w.r.t. v. Further, from the approximation guarantee of
Lemma 2 and that A is PO w.r.t. ⃗ u′, we have A is ǫ-PO w.r.t. ⃗ u.
Similar to the discussion of Cohler et al. [ 16], our results can be easily extended to cases where the utili ty functions
have ﬁnitely many discontinuity points and are Lipschitz co ntinuous on each interval induced by the discontinuities.
6 Conclusion and Future Work
The current work identiﬁes a conceptually important frontier of fair division that requires fairness under market values,
along with the standard desiderata under subjective utilit ies. This framework raises many interesting questions and
admits technically rich connections with settings, such as fair division with constraints. Several of the raised quest ions
are, in fact, fundamental even in the standard fair division setting (i.e., without an explicit invocation of the market
values), e.g., the open question regarding the existence of balanced EF1 allocations under monotone utilities.
For multiple criteria—including SD-EF1, EF1, PO, MMS, and E FX—we obtain positive and negative results on
simultaneous fairness under subjective utilities and the m arket valuation. With this groundwork, interesting direct ions
for future work in the current framework include the allocat ion of chores, division of homogeneous goods, and price
of fairness. The open questions explicitly identiﬁed throu ghout the paper are also relevant avenues for exploration.
13

Fair Division with Market V alues
References
[1] H. Akrami and J. Garg. Breaking the 3/4 barrier for approx imate maximin share. In Proceedings of the 35th
Annual ACM-SIAM Symposium on Discrete Algorithms (SODA) , pages 74–91, 2024.
[2] N. Alon. Splitting necklaces. Advances in Mathematics , 63(3):247–253, 1987.
[3] H. Aziz and S. Mackenzie. A discrete and bounded envy-fre e cake cutting protocol for any number of agents. In
2016 IEEE 57th Annual Symposium on F oundations of Computer S cience (FOCS), pages 416–427. IEEE, 2016.
[4] H. Aziz, R. Freeman, N. Shah, and R. V aish. Best of both wor lds: Ex ante and ex post fairness in resource
allocation. Operations Research, 72(4):1674–1688, 2024.
[5] J. B. Barbanel and S. J. Brams. Two-person cake cutting: T he optimal number of cuts. The Mathematical
Intelligencer, 36(3):23–35, 2014.
[6] J. B. Barbanel and W . S. Zwicker. Two applications of a the orem of Dvoretsky, Wald, and Wolfovitz to cake
division. Theory and Decision , 43:203–207, 1997.
[7] S. Barman, S. K. Krishnamurthy, and R. V aish. Finding fai r and efﬁcient allocations. In Proceedings of the 19th
ACM Conference on Economics and Computation (EC) , pages 557–574, 2018.
[8] S. Barman, A. Khan, S. Shyam, and K. Sreenivas. Finding fa ir allocations under budget constraints. In Proceed-
ings of the 37th AAAI Conference on Artiﬁcial Intelligence ( AAAI), pages 5481–5489, 2023.
[9] A. Biswas and S. Barman. Fair division under cardinality constraints. In Proceedings of the 37th International
Joint Conference on Artiﬁcial Intelligence (IJCAI) , pages 91–97, 2018.
[10] A. Bogomolnaia and H. Moulin. A new solution to the rando m assignment problem. Journal of Economic theory,
100(2):295–328, 2001.
[11] S. J. Brams, M. A. Jones, and C. Klamler. N -person cake-cutting: There may be no perfect division. American
Mathematical Monthly, 120(1):35–47, 2013.
[12] X. Bu, Z. Li, S. Liu, J. Song, and B. Tao. Fair division wit h allocator’s preference. In Proceedings of the 19th
Conference on W eb and Internet Economics (WINE), pages 77–94, 2023.
[13] E. Budish. The combinatorial assignment problem: Appr oximate competitive equilibrium from equal incomes.
Journal of Political Economy, 119(6):1061–1103, 2011.
[14] I. Caragiannis, D. Kurokawa, H. Moulin, A. D. Procaccia , N. Shah, and J. Wang. The unreasonable fairness of
maximum Nash welfare. ACM Transactions on Economics and Computation , 7(3): Article 12, 2019.
[15] B. R. Chaudhury, T. Kavitha, K. Mehlhorn, and A. Sgourit sa. A little charity guarantees almost envy-freeness.
SIAM Journal on Computing , 50(4):1336–1358, 2021.
[16] Y . J. Cohler, J. K. Lai, D. C. Parkes, and A. D. Procaccia. Optimal envy-free cake cutting. In Proceedings of the
25th AAAI Conference on Artiﬁcial Intelligence (AAAI) , pages 626–631, 2011.
[17] V . Conitzer, R. Freeman, and N. Shah. Fair public decisi on making. In Proceedings of the 18th ACM Conference
on Economics and Computation (EC) , pages 629–646, 2017.
[18] M. Dall’Aglio. Fair division of goods in the shadow of ma rket values. European Journal of Operational Re-
search, 307(2):785–801, 2023.
[19] A. Dror, M. Feldman, and E. Segal-Halevi. On fair divisi on under heterogeneous matroid constraints. Journal of
Artiﬁcial Intelligence Research, 76:567–611, 2023.
[20] L. Dubins and E. Spanier. How to cut a cake fairly. The American Mathematical Monthly , 68(1):1–17, 1961.
[21] L. E. Dubins and E. H. Spanier. How to cut a cake fairly. American Mathematical Monthly , 68(1):1–17, 1961.
[22] R. Freeman, S. Sikdar, R. V aish, and L. Xia. Equitable al locations of indivisible goods. In Proceedings of the
28th International Joint Conference on Artiﬁcial Intellig ence (IJCAI), page 280–286, 2019.
[23] R. Freeman, E. Micha, and N. Shah. Two-sided matching me ets fair division. In Proceedings of the 30th
International Joint Conference on Artiﬁcial Intelligence (IJCAI), pages 203–209, 2021.
[24] A. Igarashi, Y . Kawase, W . Suksompong, and H. Sumita. Fa ir division with two-sided preferences. In Proceed-
ings of the 32nd International Joint Conference on Artiﬁcia l Intelligence (IJCAI), pages 2756–2764, 2023.
[25] J. Kagan. Equitable Distribution: Deﬁnition, State La ws, Exempt Property.
https://www.investopedia.com/terms/e/equitable-divi sion.asp, 2021.
[26] J. Kagan. Assessor: Meaning, Certiﬁcation, Why They Ma tter.
https://www.investopedia.com/terms/a/assessor.asp, 2021.
14

Fair Division with Market V alues
[27] M. Kyropoulou, W . Suksompong, and A. A. V oudouris. Almo st envy-freeness in group resource allocation.
Theoretical Computer Science, 841:110–123, 2020.
[28] R. J. Lipton, E. Markakis, E. Mossel, and A. Saberi. On ap proximately fair allocations of indivisible goods. In
Proceedings of the 6th ACM Conference on Economics and Compu tation (EC), pages 125–131, 2004.
[29] A. Murhekar and J. Garg. On fair and efﬁcient allocation s of indivisible goods. In Proceedings of the 35th AAAI
Conference on Artiﬁcial Intelligence (AAAI) , pages 5595–5602, 2021.
[30] G. K. Patro, A. Biswas, N. Ganguly, K. P . Gummadi, and A. C hakraborty. Fairrec: Two-sided fairness for
personalized recommendations in two-sided platforms. In Proceedings of the 29th International W orld Wide
W eb Conference (TheW ebConf), pages 1194–1204, 2020.
[31] A. D. Procaccia and J. Wang. A lower bound for equitable c ake cutting. In Proceedings of the 18th ACM
Conference on Economics and Computation (EC) , pages 479–495, 2017.
[32] J. Reijnierse and J. A. M. Potters. On ﬁnding an envy-fre e Pareto-optimal division. Mathematical Programming,
83:291–311, 1998.
[33] R. L. Schilling and D. Stoyan. Continuity assumptions i n cake-cutting. arXiv:1611.04988, 2016.
[34] E. Segal-Halevi and B. R. Sziklai. Monotonicity and com petitive equilibrium in cake-cutting. Economic Theory,
68(2):363–401, 2019.
[35] I. Shtechman, R. Gonen, and E. Segal-Halevi. Fair cake- cutting algorithms with real land-value data. Autonomous
Agents and Multi-Agent Systems , 35:1–28, 2021.
[36] H. Steinhaus. The problem of fair division. Econometrica, 16:101–104, 1948.
[37] W . Suksompong. Constraints in fair division. ACM SIGecom Exchanges, 19(2):46–61, 2021.
[38] D. Weller. Fair division of a measurable space. Journal of Mathematical Economics , 14(1):5–17, 1985.
15

Fair Division with Market V alues
Appendix
A Fractional Pareto Optimality
A fractional allocation A∈ [0, 1]N ×M is a complete division of goods such that ∑ i∈N Ai,g = 1 for each g∈M . Next, we deﬁne fractional Pareto optimality which implies Deﬁnition 4.
Deﬁnition 9 (Fractional Pareto Optimality) . An allocation A is fractionally Pareto optimal (fPO) if there does not
exist a fractional allocation A′∈ [0, 1]N ×M such that ui(A′ i) /greaterorequalslant ui(Ai) with one inequality being strict.
Similar to the discussion in Section 4.1, every allocation is PO w.r.t. the market values and the inte resting case is to
consider PO w.r.t. subjective utilities. The impossibilit y of Theorem 4 extends to the stricter requirement of fPO w.r.t.
the subjective utilities. However, we answer a stronger ver sion of Open Question 2 in negative.
Proposition 1. There exists an instance with 4 goods and 2 agents where no allocation is EF1 and fPO w.r .t. subjective
utilities and EF1 w.r .t. market values.
Proof. Consider an instance with two agents, four goods, and the fol lowing valuations.
• Market valuation: v(g) = 1 ,∀g∈M .
• The ﬁrst agent: u1 :{g1 : 4, g2 : 4, g3 : 1, g4 : 1}.
• The second agent: u2 :{g1 : 3, g2 : 3, g3 : 1, g4 : 1}.
The unique EF1 and fPO allocation w.r.t. subjective utiliti es is A1 ={1} and A2 ={2, 3, 4}. However, this is not
EF1 w.r.t. the market values as agent 1 envies agent 2.
B PO w.r .t. Subjective Utilities and EF1 w.r .t. Market Value s
In this section, we prove Theorem 5. Our algorithm and analysis builds on the work of Freeman et a l. [ 22] and
Murhekar and Garg [29] who show EQ1 and fPO allocations exist when all agents have s trictly positive utilities. They
build on the work of Barman et al. [7] who designed a pseudo-polynomial time algorithm to ﬁnd an a llocation of goods
that is EF1 and PO using Fisher markets. At a high-level, the a lgorithm performs a local search over Pareto optimal
allocations that eventually reaches an EF1 (and PO) allocat ion.
We ﬁrst recall Fisher markets and make the necessary deﬁniti ons to describe the algorithm, and then outline the algo-
rithm and how the proof of Murhekar and Garg [ 29] and Freeman et al. [ 22] can be adapted to prove our Theorem 5.
B.1 Fisher Markets
In a Fisher market, in addition to the utilities, we have a price vector p = ( p1, . . . , pm) where pg is the price of good
g. The bang-per-buck ratio of good g for agent i is deﬁned as bbi(g) = ui(g)/pg. We refer to the maximum of such
ratios as the maximum bang per buck (MBB) ratio of agent i denoted by mbbi = max g∈M bbi(g). Next, we deﬁne
the Fisher market equilibrium.
Deﬁnition 10 (Fisher Market Equilibrium) . An allocation A and price vector p is a Fisher market equilibrium if all
goods are allocated and each agent receives goods that have t he maximum bang-per-buck ratio, i.e., bbi(g) = mbbi
for all agents i and item g∈ Ai.
Every Fisher market equilibrium is Pareto optimal due to the ﬁrst welfare theorem.
Proposition 2. Every allocation of a Fisher market equilibrium is Pareto op timal.
The following structures are useful for describing the algo rithm.
Deﬁnition 11 (MBB Alternating Path) . For a Fisher market equilibrium (A, p), we write i1
g
← i2 if agent i2 is
allocated good g, i.e., g∈ Ai2 , and good g is an MBB good for agent i2, i.e., bbi1 (g) = mbbi1 . An MBB alternating
path of length ℓ from iℓ to i0 is a sequence i0
g1
← i1
g2
← i2
g3
←···
gℓ
← iℓ.
Deﬁnition 12 (MBB Hierarchy) . For a set of agents N ′ ⊆N , the MBB hierarchy of N ′ is the set of agents i∈
reachable fromN ′ through an MBB alternating path.
16

Fair Division with Market V alues
ALGORITHM 1: EQ1 w.r.t. Heterogeneous Market V alues and PO w.r.t. Subjective Utilities
Input: A fair division instance I = (N ,M, ⃗ v, ⃗ u) with strictly positive agent utilities and non-negative he terogeneous market
values
Output: An allocation A that is EQ1 w.r.t. Heterogeneous Market V alues and PO w.r.t. Subjective Utilities
Phase 1 Initialize by an equilibrium allocation w.r .t. subjective utilities, e.g., a social welfare maximizing allocation
(A, p)← initial welfare maximizing allocation (w.r.t. subjective utilities) where pg = ui,g for g∈ Ai
Phase 2 Reallocate goods towards a more equitable allocation w.r .t. market values
L←{ i∈N| i∈ arg minh∈N vh(Ah)}
if∃i∈ L,∃ MBB alternating path i0
g1
← i1
g2
←···
gℓ
← iℓ with viℓ (Aiℓ\{ gℓ}) > v i(Ai) then
Choose one such path with minimum ℓ
Transfer gℓ from iℓ to iℓ−1
Repeat from Phase 2
if A is EQ1 w.r .t. market valuations then return A
Phase 3 Increase prices
β← min{mbbi/bbi(g)| i∈ HL, g∈ ⋃ i∈N \HL Ai} // Note that mbb and bb’s are based on subjective
utilities ⃗ u
for g∈ ⋃ i∈HL Ai do pg← β· pg
Repeat from Phase 2 (i.e., go to line 4)
B.2 The Algorithm and Analysis
The Algorithm. We provide a constructive proof for Theorem 5 using Algorithm 1. Similar to prior Fisher market
based algorithms [ 7, 22, 29], the algorithm consists of three phases. The algorithm beg ins with an equilibrium al-
location, which is Pareto optimal, and performs a local sear ch by transferring goods locally (Phase 2) and changing
the prices of the goods (Phase 3) in a way that the intermediat e allocation A and prices p are always a Fisher mar-
ket equilibrium. Eventually, the algorithm converges to an allocation that is EQ1 and fPO (as A is an equilibrium
allocation).
In phase 1, the algorithm begins with a utilitarian welfare m aximizing allocation A and sets the prices of goods equal
to the utilities for which the allocated agents have.
In phase 2, the algorithm takes the set of agents who have the l owest utility level L ={i| vi(Ai) = min h∈N vh(Ah)},
and searches through MBB paths for agents who “violate” the E Q1 condition. More formally, the algorithm searches
for an agent iℓ via an MBB alternating path i0
g1
← i1
g2
←···
gℓ
← iℓ such that viℓ (Aiℓ\{ gℓ}) > v i(Ai). If such a path
exists, the algorithm takes one of the shortest ones and tran sfers the good at the end of the path. Since the receiver of
the good gℓ considers it MBB, the new allocation is still an equilibrium .
If no such EQ1-violating MBB paths exist, in Phase 3, the algo rithm ﬁnds the hierarchy HL of the agents with the
lowest level of utility L, who are reachable from L via MBB alternating paths; and, it increases the prices of al l
goods allocated to HL minimally such that a new MBB edge appears between HL andN\ HL the agents outside the
hierarchy. Then, the algorithm continues with Phase 2 by sea rching for EQ1 violating MBB paths. This process will
terminate in an allocation that is EQ1 w.r.t. market values a nd fPO w.r.t. subjective utilities allocation.
Sketch of the Analysis. The analysis of the algorithm closely follows the analysis o f Murhekar and Garg [ 29], who
show the existence of EQ1 and fPO allocations in the standard setting with heterogeneous subjective utilities. By
invoking Algorithm 1 with v← ⃗ u, we get the algorithm of Murhekar and Garg [ 29] for the standard setting.
Our key observation is that in Algorithm 1, one can set the prices and deﬁne MBB goods for agents accordi ng to one
valuation and ensure Pareto optimaly w.r.t. to this valuati on while achieving EQ1 w.r.t. another valuation. We remark
that the subjective utilities must be strictly positive, wh ile the market valuations may have zero or positive values. T he
requirement of nonzero subjective utilities ensures that i n Phase 3, the price increase factor β is bounded and no good
has an unbounded bang-per-buck ratio. Recall that in the sta ndard setting, which is a special case of our algorithm
where ⃗ u= ⃗ v, EQ1+PO is infeasible if there are zero utilities [ 22].
We now provide a sketch of the proof of Theorem 5 by giving pointers to the analysis of Freeman et al. [ 22], Murhekar
and Garg [29].
Theorem 5. An allocation that is fPO w.r .t. nonzero subjective utiliti es (ui)i∈N and EQ1 w.r .t. (heterogeneous)
market valuations (vi)i∈N always exists, and can be computed in time polynomial in n, m, and V , where V =
maxi∈N|{vi(S) : S⊆M}| is the maximum number of distinct value levels for any i.
17

Fair Division with Market V alues
Proof. The allocation A and price vector p are always in an equilibrium, as shown in Lemma 2 of Murhekar a nd Garg
[29].
The only way Algorithm 1 terminates is by ﬁnding an EQ1 allocation. Thus, proving termination is the main challenge.
A helpful observation is that the minimum market value never decreases, i.e., mini vi(A) is always non-decreasing, the
proof of which follows similar to Lemma 6 of Freeman et al. [ 22]. This observation is used in deriving the following
key arguments for the termination of the algorithm.
• After poly(n, m) steps of Phase 2 and Phase 3, the set L of agents with the lowest market value must change.
This follows from arguments similar to Lemma 4 of Murhekar an d Garg [ 29] (for a more detailed proof see
Lemma 13 of Barman et al. [ 7]).
• Further, if an agent i ceases to be in the set L at time-step t0 with allocation At0 and again becomes a part
of L at a later time-step t1 with allocation At1 , it must hold that vi(At1 i ) > v i(At0 i ). This closely follows
Lemma 8 of Murhekar and Garg [ 29].
From the two arguments above combined, we have that the set L changes after at most every poly(n, m) time-steps
and it changes for at most poly(n, V ) times. Phase 1 can simply be computed in poly(n, m) time. Therefore, the
algorithm terminates in O(poly(n, m, V )).
C Proof of Theorem 15
Proof of Theorem 15. When the subjective density functions are piecewise consta nt, we can partition the cake into a
set of m intervalsI ={I1, . . . , Im} such that for all agents i∈N , ui is a constant function over Ij for all i∈N and
j∈ [m]. In other words, we treat each such interval as a “divisible g ood”. We refer to the measure (length) of a piece
of the cake z by µ(z).
Fisher Market T erminology. We follow the Fisher market terminology deﬁned in Appendix B.1. For a ﬁxed price
vector p over the intervals, the bang-per-buck ratio of agent i for interval Ij is deﬁned as bbi(Ij ) = ui(Ij )/µ(Ij ) pIj , where
the numerator is the i’s density (total value for Ij normalized by its length). Further, we call an interval Ij a maximum
bang-per-buck (MBB) interval for agent i if bbi(Ij ) = max j∈[m] bbi(Ij). For a price vector p, the MBB graph of p
is the bipartite graph with agents on one side and intervals o n the other side with an edge (i, Ij ) existing iff Ij is an
MBB interval for i.
Attaining max egalitarian welfare w.r.t. market values sub ject to PO w.r.t. subjective utilities. There are at
most 2nm MBB graphs (counting by ﬁxing the subset of existing edges). Fix an MBB graph G induced by a price
vector p, where all intervals have at least one MBB edge (i.e., all int ervals can be allocated). For each MBB graph G,
we argue that we can ﬁnd an allocation that maximizes the mini mum value with respect to the heterogeneous market
values among all allocations that respect the MBB graph. Spe ciﬁcally, this allocation must assign each interval Ij only
to agents for whom Ij is MBB.
This allocation can be achieved by a straightforward applic ation of the Dubins–Spanier theorem [ 20]. According to
this theorem, for each interval Ij , the space of valuation matrices (with respect to market values) restricted to the agents
for whom Ij is MBB is compact and convex. Summing the utility spaces over all intervals (padding the matrices with
zeros for agents where the interval is not MBB) preserves com pactness and convexity. Consequently, the space of
valuation matrices over allocations that respect the MBB ed ges of G remains compact and convex. Therefore, an
allocation that maximizes the minimum utility for all agent s is attainable.
Finally, by taking the maximum (egalitarian welfare) over a ll ﬁnitely many MBB graphs, we can achieve an allocation
that maximizes the egalitarian welfare with respect to market values among all PO allocations w.r.t. subjective utilities.
Existence of EQ w.r.t. market values and PO w.r.t. subjectiv e utilities. Similar to arguments for the max egali-
tarian welfare allocation, we can ﬁnd an allocation x satisfying the following.
1. x maximizes the egalitarian welfare among all PO allocations w.r.t. subjective utilities, i.e.,
x∈ arg max{min
i∈N
vi(y)| y is PO w.r.t. ⃗ u}.
18

Fair Division with Market V alues
2. Subject to 1, x minimizes the maximum utility. That is
x∈ arg min{max
i∈N
vi(y)| y satisﬁes condition 1}.
Let vmin = min i vi(x) and vmax = max i vi(x).
3. Subject to 1 and 2, x minimizes the number of agents with the speciﬁed maximum uti lity of vmax.
We show that x is EQ w.r.t. ⃗ v. Suppose, by contradiction, that x is not EQ. Let Nmax be the set of agents with the
maximum market value. LetImax ={Ij|∃ i∈N max, µ(xi∩ Ij) > 0} be the set of intervals that a nonzero measure
of which is allocated toNmax. We come to a contradiction by a case analysis.
• Case 1. Suppose there exists an agent i′∈N\N max that has an MBB edge to one of the intervals Ij inImax
that is partially allocated to i∈N max. Then, we can transfer an inﬁnitesimal fraction δ∈ (0, µ(xi′∩ Ij )) of
Ij from i to i′ such that vi′ (xi′∪{ δ· Ij}) < v max and vi(xi\{ δ· Ij}) > v min — which is possible by the
boundedness of the density function. This contradicts the c ondition 3 or 2 above.
• Case 2. Otherwise, we have that all of Imax are only MBB to agents in Nmax. Since there are no MBB
edges fromN\N max, we can increase the prices of all other intervals I\I max, which are all allocated to
agents inN\N max until an MBB edge from some agent in N\N max appears to an interval inImax. More
speciﬁcally, we increase the prices by a factor of min{mbbi/bbi(Ij )| i∈N\N max, Ij∈I max}. After
such a price increase, the allocation is still an equilibriu m since (i) the bang-per-buck ratio for other intervals
only decreases for agents in Nmax, and (ii) increasing the prices of all intervals in I\I max keeps the MBB
edges fromN\N max towardsI\I max and the minimal increase in the prices ensures that the prior MBB
edges remain MBB. Now, the condition of Case 1 is met, and we ag ain come to a contradiction.
The requirement that subjective utilities be strictly posi tive is necessary for the price rise argument in Case 2.
The proof can be slightly adjusted to work with market valuat ions that have zero densities. In Case 1, if the owner
agent i has a positive density over interval Ij, regardless of i′, the transfer is still valid and the fact that the market
value of i decreases is enough to get a contradiction. However, if vi has density 0 over Ij, vi might remain the same.
To address this, we add one more tie-breaking condition to th e three conditions of x. The fourth condition is that x,
subject to 1-3, minimizes the total measure of the cake alloc ated toNmax for which its owner has zero market value.
That is
x∈ arg min
{∑
i∈N
∫
x∈yi
I[vi(x) = 0] dx | y satisﬁes conditions 1-3
}
.
This way, in the transfer of Case 1, if the market value of i′ is 0, then the nonzero δ transfer that keeps vi′ (xi′∪{ δ·
Ij}) < v max will strictly reduce the measure of the cake allocated to Nmax with zero market value. This contradicts
the fourth condition. Hence, x is EQ w.r.t. heterogeneous market values and PO w.r.t. subjective density functions.
19
