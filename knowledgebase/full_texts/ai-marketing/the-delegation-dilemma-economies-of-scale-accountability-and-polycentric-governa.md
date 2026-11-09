---
title: 'The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance'
url: https://arxiv.org/abs/2610.21746
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Arin Mukhopadhyay
- Aris Filos-Ratsikas
- Panayiotis Danassis
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.21746
pages: 17
chars: 84302
fetched_at: '2026-11-08T13:32:26+00:00'
kb_version: 1
---

# The Delegation Dilemma: Economies of Scale, Accountability, and Polycentric Governance

Research Paper Track AAMAS 2027, 3–7 May 2027, Hanoi, Vietnam
The Delegation Dilemma: Economies of Scale, Accountability, and
Polycentric Governance
Arin Mukhopadhyay
University of Edinburgh
Edinburgh, United Kingdom
a.mukhopadhyay-1@sms.ed.ac.uk
Aris Filos-Ratsikas
Imperial College London
London, United Kingdom
aris.filos-ratsikas@imperial.ac.uk
Panayiotis Danassis
University of Southampton
Southampton, United Kingdom
p.danassis@soton.ac.uk
Abstract
Many collective-action systems are neither fully decentralized nor
fully centralized: agents voluntarily organize into institutions that
share organizational costs and delegate decisions to representatives.
Delegation can reduce individual costs, but it also transfers control
to representatives whose private objectives need not align with
those of their constituents. We study this tension in a repeated game
with endogenous delegation to self-interested centers. A simple
reduced-form model yields ascale–accountability tradeoff: larger
constituencies offer greater cost-sharing benefits to members, yet
the marginal value to a center of retaining any one constituent
decreases as group size grows. Consequently, the prospect of in-
dividual exit can sustain non-exploitative delegation only up to
an endogenous accountable constituency size. Additionally, we
identify parameter regions in which fully delegated, accountable
governance, when feasible, must bepolycentric. We investigate
these predictions through simulations with large language model
(LLM) agents. Across five matched pairs of 30-agent simulations,
polycentric structures repeatedly emerge but remain fluid, exhibit-
ing cycles of concentration, exploitation, exit, and re-formation. We
further find that models of different capacity exhibit similar willing-
ness to assume leadership but differ substantially in their exercise
of authority, with Sol initiating exploitation more frequently than
Luna in matched decision states.
Keywords
Delegation, Polycentric Governance, Accountability, Coalition For-
mation, Large Language Model Agents, Multi-agent Governance
1 Introduction
Socially valuable activities often exhibiteconomies of scale: they
are costly, or even infeasible, when undertaken individually, but
become easier to perform as individuals organize into groups. Farm-
ers may cooperate in production or irrigation, fishers may jointly
manage a common resource, and communities may pool resources
to provide local public services. Such activities naturally give rise to
constituencies, with organizers or leaders who coordinate contribu-
tions, make collective decisions, and determine how the gains from
cooperation are distributed. The benefits of scale have long been
central to theories of clubs and collective action [3, 20], as well as
to more recent work on endogenous group formation [1, 21].
At the same time, organizational scale may alter the incentives
of those entrusted with authority. As a constituency grows, the
centre’s marginal organizational benefit from retaining any particu-
lar constituent may decline. A self-interested centre may therefore
find it profitable to exploit some delegates, even when doing so
risks their eventual departure. When losing a constituent has only
Figure 1: Overview of our delegation setting. Agents choose
whether to remain independent or join a constituency (to
share costs) led by a self-interested center. Each center de-
cides whether to exploit its delegates for private gain. Dele-
gates may detect exploitation and exit the delegation.
a small effect on the centre’s future organizational costs, the threat
of exit provides a weaker deterrent against exploitation. Thus, the
same economies of scale that encourage collective organization can
also undermine the accountability of those exercising delegated au-
thority and create scope for opportunism. This tension echoes the
classical observation that organizational growth can concentrate
decision-making authority [17].
However, such opportunism does not necessarily imply the per-
sistence of a single governing authority. Constituents who receive
an exploitative treatment can instead exerciseexit[ 13], by join-
ing an alternative constituency or by volunteering to lead a new
constituency themselves. Competition for constituents therefore
constraints the size of the groups and their leaders’ ability to benefit
at the expense of their members. At the same time, groups cannot
become arbitrarily small, because doing so sacrifices the economies
of collective production. The resulting institutional structure is
therefore neither individual nor fully centralized, butpolycentric:
multiple, relatively autonomous centers of organization coexist,
compete for constituents, and may cooperate where doing so is
mutually beneficial. This conception is closely related to the poly-
centric political systems of Ostrom, Tiebout, and Warren [20], and
to Ostrom’s later account of polycentric governance as an alter-
native to the dichotomy between centralized state provision and
purely decentralized market exchange [19]. Examples of polycen-
tricity are also prevalent in practice. For example, in experiments
with members of Chilean territorial-use-right fisheries, Chávez et
al. [4] find that while fishers frequently formed the grand coalition
when monitoring was inexpensive, in fully decentralized settings
without monitoring, the former coalitions were many more and
significantly smaller. Thus, our general aim in this paper is to study
arXiv:2610.21746v1  [cs.MA]  15 Oct 2026

and understand the following phenomenon: polycentricity arises
not merely because different tasks are efficiently performed at dif-
ferent scales, but because organizational scale itself changes the
incentives of those entrusted with authority.
With the rapid development and employment of AI systems,
individuals and organizations increasingly delegate their decisions
to autonomous AI agents, and in particular to agents powered by
large language models that act on their behalf. A growing litera-
ture has already begun to examine delegation to artificial agents in
collective-action environments, e.g., see [6, 7, 18]. This raises the
question of whether the institutional forces that generate polycen-
tricity among human decision makers continue to operate when
such decisions are delegated to AI agents. Will AI agents recog-
nize the economic advantages of delegation and voluntarily form
constituencies? How will self-interested AI centres exercise their
authority as constituency size increases? Can the prospect of losing
constituents discipline exploitation, or will centres anticipate that
departing members can be replaced? Will agents establish com-
peting centres when existing governance arrangements become
unattractive? Finally, will different language models respond simi-
larly to the same institutional incentives, or exhibit distinct patterns
in their exercise of delegated authority?
More generally, we are interested to know whether interactions
among autonomous AI agents reflect the endogenous checks on
organizational scale that sustain polycentricity among human deci-
sion makers, or whether they instead generate qualitatively differ-
ent organizational structures. Our aim is therefore not to assume
that polycentricity is a stable outcome, but to understand the insti-
tutional incentives that make it possible and the strategic behaviour
that shapes its emergence and persistence.
1.1 Our Contributions
We study whether polycentric arrangements emerge among au-
tonomous LLM agents, how they evolve as constituencies gain and
lose members, and whether different models exercise delegated
authority in similar ways. Our main contributions are as follows:
(i) We develop a general model of voluntary delegation,
economies of scale, and exit-based accountability(Figure 1).
Our model is deliberately stylized, and intentionally abstracts away
from the particulars of the task (e.g., whether it is a resource harvest-
ing task or any other task) and the form of exploitation (e.g., whether
that arises via some misallocation of resources etc). The aim of the
model is to capture the fundamental tension between the efficiency
gains from forming larger groups and the centers’ incentives for
exploitation, and the conditions under which this leads to polycen-
tric structures. Participation depends on the average-cost saving
created by joining a constituency, whereas accountability depends
on the marginal organizational value that the center loses when one
constituent exits. We derive a minimum viable constituency size, a
maximum size at which probabilistic individual exit can deter ex-
ploitation, comparative statics, and an exact characterization of the
number of centers compatible with fully delegated accountable gov-
ernance. A fixed-cost specialization yields closed-form thresholds.
Our theoretical results serve as baselines to ground our simulations.
(ii) We study endogenous governance formation among
Large Language Model (LLM) agents. Across ten matched episodes
with 30 agents, polycentric structures repeatedly emerge through
both bottom-up formation and fragmentation of concentrated au-
thority, but remain fluid as fee sharing attracts agents toward larger
constituencies and exploitation induces exit. We additionally com-
pare GPT-6 Luna and GPT-6 Sol (small vs. large model) pointwise
on the same post-initialisation decision states. The two models are
similarly willing to become centers but differ substantially in how
they exercise delegated authority, with Sol initiating exploitation
more often under matched conditions.
2 Related Work
Our model connects work on club and coalition formation with dele-
gation and institutional accountability. Classical club theory studies
how cost sharing and congestion determine desirable group size [3],
while coalition-formation models study the endogenous emergence
and stability of group structures [1, 21, 22]. Most closely related to
our dynamic setting, Joshi [15] studies sequential club formation
when agents’ preferences depend on club size. Endogenous group
formation has also been studied in collective-resource settings [4]
and in environments with multiple centrally coordinated groups
[10, 11]. Our upper size limit has a different source: larger groups
dilute the disciplinary effect of losing any particular member rather
than generating congestion or technological inefficiency.
A second line of literature studies delegation to representatives or
intermediaries. Hamman et al. [9] show experimentally that groups
may voluntarily delegate public-good decisions to elected mem-
bers, and that poorly performing representatives can subsequently
be replaced. Related work studies representation in public-good
games [8, 12], delegation as a coordination mechanism [ 5], and
delegation of common-pool-resource decisions to a stakeholder
[2]. Our distinctive mechanism combines voluntary constituency
formation with a self-interested center whose incentive to retain
each constituent decreases with organizational scale. This links
economies of scale directly to exit-based accountability.
Finally, recent work studies institutional mechanisms among
LLM agents. Faulkner et al . [7] introduce elected leadership in
LLM social groups, while Tewolde et al. [24] compare repetition,
reputation, mediation, and contracting as cooperation-sustaining
mechanisms. Hierarchical authority, elections, and oversight have
also been studied in LLM public-good environments [23]. Rather
than imposing a fixed governance institution, we ask whether self-
interested AI agents endogenously form centralized, polycentric, or
individual governance structures when organizational scale simul-
taneously creates economic benefits and weakens accountability.
3 Delegation – Accountability Model
In this section, we formulate a reduced-form game that isolates the
institutional incentives associated with delegation, cost sharing,
and exit.All proofs can be found in Appendix A.
There are𝑛≥ 2persistent agents. At any governance epoch,
agents may remain under individual control or belong to acon-
stituencyconsisting of one center and the agents who delegate
control to it. Its size is 𝑚≥ 1, including the center; 𝑚= 1cor-
responds to individual control. Delegation is binding for 𝐿≥ 1
operational rounds. After each nonterminal operational round, play

continues with probability𝛿∈( 0, 1), so a payoff𝑠 rounds in the
future is reached with probability𝛿 𝑠.
A constituency of size𝑚 incurs a per-round organizational cost
𝐾(𝑚)>0, shared equally among its members. Let
𝑐(𝑚)= 𝐾(𝑚) 𝑚 (1)
denote the resulting per-member cost. This formulation can repre-
sent shared infrastructure, administration, transaction costs, access
or licensing costs, monitoring systems, or other technologies whose
average cost changes with organizational scale. Delegates addition-
ally incur a private per-round lossℓ≥ 0from surrendering direct
control. A center does not incurℓ, because it retains decision author-
ity. If the center exploits𝑘 delegates in a round, it receives𝑘𝑑 and
each targeted delegate loses𝑑, where𝑑> 0. Thus the reduced-form
per-round payoffs are
𝑢𝐶(𝑚,𝑘)=−𝑐(𝑚)+𝑘𝑑, 𝑢 𝐷(𝑚,𝑧)=−𝑐(𝑚)−ℓ−𝑑𝑧,(2)
where𝑧∈{ 0, 1} indicates whether a given delegate is exploited. An
independent agent receives𝑢𝐼 =−𝑐(1). Exploitation is therefore a
transfer between the center and a targeted delegate; its disciplinary
effect operates through subsequent governance choices.
Assumption 1 (Economies of scale).The per-member orga-
nizational cost𝑐(𝑚) is weakly decreasing in 𝑚. Define the center’s
one-member retention value
𝐷(𝑚)=𝑐(𝑚−1)−𝑐(𝑚), 𝑚≥2.(3)
We additionally assume𝐷(𝑚) is weakly decreasing in 𝑚, so the mar-
ginal organizational benefit of retaining one more constituent dimin-
ishes with scale.
The first part of Assumption 1 captures average-cost economies
of scale. The second separates the mechanism relevant for account-
ability: as constituencies grow,losing any particular constituent has
a smaller effect on the center’s own organizational cost.
3.1 Delegation and Economies of Scale
Relative to individual control, membership in a constituency of size
𝑚saves the delegate
𝑆(𝑚)=𝑐(1)−𝑐(𝑚)(4)
per round in organizational cost. The net per-round advantage of
non-exploitative delegation is therefore
𝐵(𝑚)=𝑐(1)−𝑐(𝑚)−ℓ.(5)
Delegation is individually rational when𝐵(𝑚)≥0.
Proposition 1 (General participation threshold).Un-
der Assumption 1, if there exists a nontrivial constituency size for
which delegation is individually rational, then the set of individually
rational sizes is upward closed and its minimum is
𝑚min =min{𝑚≥2 :𝑐(1)−𝑐(𝑚)≥ℓ } (6)
If this set is empty, no finite constituency makes delegation individu-
ally rational through organizational cost sharing alone.
Fixed-cost Specialization.To obtain closed-form results, we
specialize to the case in which the total organizational cost is inde-
pendent of constituency size:
𝐾(𝑚)=𝜅, 𝜅>0,(7)
so that𝑐(𝑚)=𝜅/𝑚 . This specification captures a fixed cost that can
be shared among constituency members and is the environment
implemented in our simulations.
Corollary 1 (Minimum viable constituency size under
fixed costs).Suppose 𝐾(𝑚)=𝜅 and0 ≤ℓ<𝜅 . Non-exploitative
delegation is individually rational if and only if
𝑚≥ 𝜅 𝜅−ℓ (8)
The minimum nontrivial integer constituency size is
𝑚min =max
n
2,
l 𝜅
𝜅−ℓ
mo
(9)
Ifℓ≥𝜅 , no finite constituency makes delegation individually rational
through fixed-cost sharing alone.
3.2 When Does Exit Discipline the Center?
We next model the center’s temptation to exploit a constituent. The
parameter𝑑 (defined in Eq. 2) is deliberately reduced form: it is the
center’s per-round private gain from exploiting one delegate and
can represent appropriation, preferential allocation, extraction of
rents, or any other benefit obtained by using delegated authority
against a constituent’s interest.
Assumption 2 (Targeted exploitation and probabilis-
tic exit).At the beginning of a governance epoch, a center in a
constituency of size 𝑚≥ 2can exploit one delegate, obtaining an
additional payoff𝑑> 0in each of the 𝐿 locked-in rounds while impos-
ing the same per-round loss on that delegate. At the next governance
opportunity, the exploitation is detected and results in that delegate’s
departure with probability𝛼∈[ 0, 1]. Conditional on departure, the
delegate is not replaced over the continuation horizon, so the change
in the center’s per-member organizational cost persists. The deviation
does not otherwise alter the continuation probability.
The parameter𝛼 is a reduced-form accountability probability. If
detection occurs with probability𝑝det and a delegate exits condi-
tional on detection with probability𝑝exit|det , then𝛼=𝑝 det𝑝exit|det .
This lets the theory encompass imperfect observability as well as
imperfect behavioural response without changing the core incen-
tive comparison.
Definition 1 (Accountable constituency).A constituency
of size𝑚 isaccountable under individual exitif, under Assumption 2,
the center weakly prefers non-exploitative behaviour to the targeted
exploitation deviation.
Proposition 2 (General accountability condition).Un-
der Assumptions 1–2, a constituency of size 𝑚≥ 2is accountable
under individual exit if and only if
𝛼𝛿𝐿𝐷(𝑚)≥𝑑(1−𝛿 𝐿) (10)
Because𝐷(𝑚) is weakly decreasing, the set of accountable constituency
sizes is downward closed. When the largest accountable size is finite,

define
𝑚max =max

{1}∪

𝑚≥2 :𝛼𝛿 𝐿𝐷(𝑚)≥𝑑(1−𝛿 𝐿) 	 .(11)
The general condition separates two distinct effects of scale. Par-
ticipation depends on theaverageorganizational saving 𝑐( 1)−𝑐(𝑚) ,
whereas accountability depends on themarginalretention value
𝐷(𝑚)=𝑐(𝑚− 1)−𝑐(𝑚) . Organizational scale can therefore make
delegation increasingly attractive to constituents while simulta-
neously making each individual constituent less valuable to the
center.
Corollary 2 (Maximum accountable constituency size
under fixed costs).Under𝐾(𝑚)=𝜅, condition(10)becomes
𝛼𝛿𝐿 𝜅 𝑚(𝑚−1) ≥𝑑(1−𝛿 𝐿),(12)
or equivalently
𝑚(𝑚−1)≤ 𝛼𝜅𝛿𝐿
𝑑(1−𝛿 𝐿).(13)
Hence the continuous accountability threshold is
𝑚=
1+
√︃
1+4 𝛼𝜅𝛿 𝐿 𝑑(1−𝛿 𝐿)
2 ,(14)
and the largest integer constituency size supportable by individual
exit is
𝑚max =⌊𝑚⌋ (15)
If𝑚max = 1, no nontrivial delegated constituency is accountable
through this exit mechanism alone.
Interpretation.The upper threshold does not imply that con-
stituencies larger than𝑚max cannot exist or that their constituents
necessarily leave. It says only that, under the stated deviation and
punishment technology, the expected loss generated by one con-
stituent’s possible future exit is insufficient to make the center prefer
non-exploitative behaviour. Constituents may still prefer member-
ship despite exploitation, and replacement, collective exit, reputa-
tion, auditing, legal sanctions, or other mechanisms can change
the effective accountability constraint, sustaining accountability
beyond𝑚 max.
3.2.1Robustness of the Accountability Constraint.Two sim-
ple observations strengthen the interpretation of𝑚 max.
Lemma 1 (Single-constituent exploitation is the hard-
est additive deviation).Suppose a center simultaneously ex-
ploits𝑘∈{ 1,...,𝑚− 1} constituents, gaining𝑘𝑑 per locked-in round,
and each targeted constituent independently exits at the next gov-
ernance opportunity with probability 𝛼. Under Assumption 1, if the
one-constituent accountability condition (10) holds, then every such
additive𝑘-constituent deviation is also deterred.
Lemma 2 (The beginning of an epoch is the hardest
time to deter exploitation).Suppose exploitation begins when
𝑠∈{ 1,...,𝐿} locked-in rounds remain. If the accountability condi-
tion holds for 𝑠=𝐿 , it holds for every later point in the epoch with
𝑠<𝐿.
Table 1: Comparative statics for the fixed-cost participation
and accountability thresholds.
Increase𝑚 min 𝑚max Predicted institutional effect
𝜅↓ ↑ Delegation viable over a wider size
range
ℓ↑– Harder to induce delegation
𝑑–↓Stronger agency problem; smaller ac-
countable centers
𝛼–↑ More reliable detection and exit
strengthen accountability
𝛿–↑Future exit matters more
𝐿–↓ Longer lock-in weakens exit disci-
pline
3.3 How Institutional Parameters Shape
Delegation
The general formulation shows that participation is governed by
average cost savings whereas accountability is governed by the mar-
ginal retention value of one constituent. We now characterize how
the two institutional thresholds move with the parameters and give
closed-form comparative statics for the fixed-cost specialization.
Table 1 summarizes the main results.
Theorem 1 (Comparative statics under fixed costs).
Assume𝜅> 0,𝑑> 0,0 <𝛿< 1,𝐿≥ 1,0 <𝛼≤ 1, and0 ≤ℓ<𝜅 .
Let
𝑚 = 𝜅 𝜅−ℓ and 𝑚= 1+
√
1+4𝐶
2 , 𝐶= 𝛼𝜅𝛿𝐿 𝑑(1−𝛿 𝐿).
Then
𝜕𝑚
𝜕𝜅 ≤0(strict ifℓ>0), 𝜕𝑚 𝜕ℓ >0,(16)
𝜕𝑚
𝜕𝜅 >0, 𝜕𝑚 𝜕𝑑 <0,(17)
𝜕𝑚
𝜕𝛼 >0, 𝜕𝑚 𝜕𝛿 >0,(18)
and𝑚(𝐿+ 1)< 𝑚(𝐿) . Consequently, after integer rounding, 𝑚min
is weakly decreasing in 𝜅 and weakly increasing in ℓ, while𝑚max is
weakly increasing in𝜅,𝛼, and𝛿and weakly decreasing in𝑑and𝐿.
Corollary 3 (Stronger fixed-cost economies widen
the viable interval).For fixed ℓ,𝑑,𝛼,𝛿,𝐿 , increasing𝜅 weakly
lowers𝑚min and weakly raises𝑚max. Thus stronger fixed-cost economies
expand the set of constituency sizes that are simultaneously individu-
ally attractive and accountable under exit.
Corollary 4 (More reliable exit supports account-
ability at larger scales).For fixed 𝜅,𝑑,𝛿,𝐿 ,𝑚max is weakly
increasing in 𝛼. If 𝛼= 0, individual exit supplies no expected pun-
ishment and no nontrivial constituency is accountable through this
mechanism alone.
Corollary 5 (Long lock-in weakens accountability).
For fixed𝜅,𝑑,𝛼,𝛿 ,𝑚max is weakly decreasing in governance-epoch
length𝐿. Moreover, for0<𝛿<1, 𝑚→1as𝐿→∞.

3.4 The Emergence of Polycentric Governance
The two thresholds𝑚min and𝑚max characterize constituency sizes
that are simultaneously individually attractive and accountable.
Importantly, the following result depends only on the existence of
these two thresholds; it is therefore not specific to the fixed-cost
specialization.
Definition 2 (Fully delegated accountable partition).
A partition of𝑛 agents into𝑞 constituencies with integer sizes𝑚1,...,𝑚 𝑞
isfully delegated and accountableif every constituency is nontrivial
and satisfies
𝑚min≤𝑚 𝑗≤𝑚 max for all𝑗=1,...,𝑞.
Theorem 2 (Feasible number of accountable centers).
Suppose2 ≤𝑚 min≤𝑚 max. A fully delegated accountable partition of
𝑛agents into exactly𝑞constituencies exists if and only if
 𝑛
𝑚max

≤𝑞≤
 𝑛
𝑚min

(19)
Consequently, if the interval in (19) is nonempty and𝑛>𝑚 max, every
fully delegated accountable governance structure is polycentric, with
at least
𝑞min =
 𝑛
𝑚max

≥2(20)
centers.
Corollary 6 (Primitive condition for necessary poly-
centricity under fixed costs).Under the fixed-cost special-
ization, define
𝑚min =max
n
2,
l 𝜅
𝜅−ℓ
mo
, 𝑚 max =
 1+ √︃ 1+4 𝛼𝜅𝛿 𝐿 𝑑(1−𝛿 𝐿) 2  .
If𝑚min≤𝑚 max <𝑛 and⌈𝑛/𝑚max⌉≤⌊𝑛/𝑚 min⌋, then every fully
delegated accountable governance structure is necessarily polycentric.
Takeaway.Theorem 2 is a feasibility and necessity result, not
an equilibrium-selection claim. It identifies a region, under bench-
mark conditions, in whicheconomies of scale rule out very small
delegated institutionswhileaccountability rules out a grand center.
Whether decentralized strategic agents discover and sustain such
structures once formation and replacement evolve endogenously is
the question we examine experimentally.
3.5 Structural Polycentricity vs. Behavioural
Diversity
Our theory characterizes when accountable delegation requires
authority to be distributed across multiple centers. Suchstructural
polycentricity, however, does not necessarily imply diversity in how
those centers behave. We therefore distinguish between structural
polycentricity, which describes the distribution of authority across
centers, andbehavioural diversity, which describes whether distinct
centers make different decisions when facing comparable strategic
conditions. In simple terms, a system can be highly polycentric in its
formal organization while remaining behaviourally concentrated if
its centers respond similarly to the same situations. This distinction
is particularly relevant when centers are controlled by LLMs. Recent
work documents substantial intra-model repetition and inter-model
homogeneity in LLM responses to open-ended prompts [ 14]. Al-
though these findings concern generative behaviour rather than
strategic governance, they raise the possibility that formally inde-
pendent LLM centers may nevertheless respond similarly to the
same incentives. A governance system may therefore be highly poly-
centric in its institutional structure while remaining behaviourally
concentrated if its centers repeatedly make similar exploitation
decisions or similar mistakes. Our theoretical results do not require
behavioural heterogeneity across centers, but this distinction mo-
tivates our empirical examination of how language-model agents
exercise authority under comparable strategic conditions, including
whether different models exhibit similar exploitation decisions and
reasoning patterns.
4 Polycentricity in Environments of AI Agents
In this section, we study endogenous governance formation among
large language model (LLM) agents. Our objective is to study whether
polycentricity emerges naturally via their interactions, and whether
the experimental results echo those of the theory developed in Sec-
tion 3. We start by describing the design of our simulation.
4.1 Simulation Design
Reduced-form Environment.The simulations implement the
reduced-form game of Section 3, with perfect detection and com-
pulsory exit following exploitation (𝛼= 1). Agents can establish
new centres, step down as centres, and voluntarily join or leave
constituencies at governance transitions. At each transition, ex-
ploited delegates first leave their centres. Existing centres then
decide whether to continue, remaining delegates decide whether
to stay, and free agents may volunteer to become new centres. If
multiple agents volunteer, one is selected uniformly at random.
Once the set of centres is determined, free agents choose between
individual control and delegation to an eligible centre. A departing
delegate may volunteer during the same transition.
Agents know the governance rules and observe the public con-
stituency structure and their own actions and outcomes, but not
other agents’ private exploitation outcomes or reasoning. Each
decision is accompanied by a history of the agent’s observations,
organized by governance epoch. Model-generated explanations are
recorded for analysis but are neither shared with other agents nor
included in subsequent memory.
Matched Initialization Experiment.We ran five matched
pairs of simulations, each with𝑛= 30GPT-6 Luna agents. Each pair
compared two starting conditions. In thecentralized initialization,
one randomly selected agent began as the centre of a group contain-
ing all 30 agents. In thedecentralized initialization, all agents began
independently and could volunteer to become a centre. One vol-
unteer was selected at random, and the other agents could choose
whether to join. After initialization, both conditions followed the
same governance rules described in the previous paragraph.
The two simulations in each pair shared the same random draws
but used separate model calls and memories. Each pair used a
different random seed. We set(𝜅,ℓ,𝑑,𝛿,𝐿)=( 1, 3/5, 2/5, 99/100, 5),
which gives the theoretical benchmark interval3≤𝑚≤ 7for 𝛼= 1,
according to Corollaries 1 and 2. We use this interval to classify
constituency sizes. Appendix C.1 has a detailed parameter sweep.

If an agent leaves a centre (e.g., due to exploitation), it cannot
immediately rejoin. Before each later affiliation decision, the op-
tion to rejoin becomes available with probability1/2and remains
available unless the agent rejoins and leaves again. Rejoining is
always voluntary. Agents see which centres they can join, but do
not know the reinstatement rule or its random outcomes. This
mechanism captures membership renewal in a finite population of
persistent agents. Without it, permanent restrictions on rejoining
would gradually limit agents’ choices and could cause fragmenta-
tion unrelated to their strategic decisions. In real organizational
settings, populations evolve as new members arrive and former
members reconsider their affiliations. Probabilistic reinstatement
provides an approximation of such membership renewal without
introducing explicit population turnover, allowing constituencies
to recover, reorganize, and compete for members over repeated
governance epochs.
Each simulation contains 20 complete epochs. All agents received
the same rules and one of five decision prompts: centre continua-
tion, delegate release, volunteering, affiliation, or exploitation. Each
prompt included the agent’s current observations, available actions,
and private memory. We used GPT-6 Luna with medium reasoning
effort and required agents to provide both a structured decision and
a private explanation. All prompts are provided in Appendix C.3,
and the source code can be found in the supplement.
Outcome Measures and Point-wise Comparison.We call a
constituencyviablewhen 𝑚min≤𝑚≤𝑚 max,1 and an epochpoly-
centricwhen at least two viable constituencies coexist. For each
operational round, we record each agent’s constituency size and
whether they were exploited. To measure how cooperation gains are
distributed, we compare each agent’s payoff with the independent-
control payoff of−𝜅 and attribute the difference to centres or dele-
gates according to their role.
For the pointwise comparison, Sol evaluated each post-initialization
Luna decision state using the same rules, observations, available
actions, and history, without seeing Luna’s decision or reasoning.
Sol’s responses did not affect the Luna trajectories. We compared
4,551 volunteering decisions and 1,988 exploitation decisions across
the two models. The five random seeds were independent, but de-
cisions within each simulation were not; we therefore report the
results descriptively. This comparison captures differences between
the models in identical decision states, rather than outcomes from
independently evolving Sol societies.
5 Simulation Results
(1) Luna agents repeatedly formed polycentric arrangements under
both initialization conditions, butconstituency membership
remained fluidas fee-sharing incentives encouraged concen-
tration and exploitation induced departures.
(2) Although delegation generated organizational cost savings,cen-
tres captured most of these gains. This concentration was
particularly pronounced under centralized initialization, where
exploitation left delegates collectively worse off than under
individual control.
1This classification identifies constituency sizes satisfying the analytical bounds, rather
than establishing that the centre behaves non-exploitatively.
0 5 10 15 20 25 30
Agents
1
5
10
15
20 Epoch
30
10
7 5
5 5 3
7 4 4
14 4
7 6 5
13 4
5 4 4
9 5 3
3 3 3
5 4 3
5 4 3
10 4
5 4 3
4 3 3 3
10 4
9 3
6
4 3 3 3
Centralized
0 5 10 15 20 25 30
Agents
5
7 4
15
10 3
11 4
8 6 4
7 3 3
8 4 3
5 5 4 3
14 4 3 3 3
6 5 3 3
6 5 4 3
4 3 3 3 3
5 5 3 3
5 4 3
8 3
4 4
6 4 3
3 3
9 3 3
Decentralized
Singleton Pair Viable 3 ≤ m ≤ 7 Above mmax
Figure 2: Constituency partitions at the start of each epoch.
Left: centralized initialization, Right: decentralized initial-
ization Each panel partitions all 30 agents; labels show con-
stituency sizes of at least three. Multiple viable constituencies
formed, dissolved, and re-formed under both initialization
conditions. Appendix 8 shows all five repeats.
(3) Matched-state comparisons show that Luna and Sol were simi-
larly willing to volunteer for leadership butdiffered substan-
tially in their exploitation decisionsand in the considera-
tions emphasized in their explanations.
5.1 Polycentricity Emerges but Remains Fluid
Polycentricity emerged through both formation and fragmentation.
All ten trajectories became polycentric, in all ten episodes and in 117
of the 200 observed epochs. This occurred under both centralized
(55/100 epochs) and decentralized (62/100 epochs) initialization.
Each trajectory was polycentric in 8–15 of its 20 epochs. The routes
to polycentricity differed markedly for each of the two initialization
conditions (Figure 2). Across both conditions, constituencies repeat-
edly expanded beyond the analytical accountability bound, lost
members, and re-formed around existing or new centres. Thus,the
agents did not simply select and maintain a partition within the
theoretically compatible interval; polycentricity emerged through
an process of concentration, exploitation, exit, and reconstruction.
Table 2 compares the two initialization conditions across the
full trajectories. Decentralized initialization produced slightly more
polycentric epochs (62% versus 55%) and greater agent-round ex-
posure to constituencies within the theoretical size interval (29.2%
versus 24.6%). More importantly, exploitation exposure after the
first epoch was lower (42.2% versus 52.9%). These descriptive differ-
ences suggest that the initial distribution of authority may influence
subsequent governance dynamics, even though both conditions
generated repeated formation and fragmentation of constituencies.
Exploitation often triggered the departure of targeted delegates,
however these losses were not necessarily permanent: centres could
attract new delegates, and departed agents could regain the op-
portunity to rejoin. Indeed, some centre explanationsexplicitly
anticipated membership recovery when deciding whether to exploit.
Every trajectory remained polycentric for at least two consecu-
tive epochs, and one did so for ten. Some constituencies even grew
to 14 agents, way above the theoretical bound. Nevertheless, larger
constituencies subsequently fragmented, while smaller constituen-
cies repeatedly lost members to competing centres. The observed
dynamics were therefore characterized by recurring concentration,

Table 2: Polycentricity and exploitation by initialization con-
dition, aggregated over five matched pairs of 30-agent simu-
lations (20 governance epochs per episode). An epoch is clas-
sified as polycentric when at least two constituencies have
sizes within the theoretical benchmark interval3 ≤𝑚≤ 7.
Exploitation rates are calculated in epochs 2–20 to avoid the
distinct initialization epoch.
Outcome Centralized Decentralized
Polycentric epochs55/100 62/100
Agent-rounds within theoretical bounds24.6% 29.2%
Exploited delegate-rounds after epoch 152.9% 42.2%
exploitation, exit, and re-formation, rather than convergence to a
persistent governance structure.
Centres Captured Most of the Surplus.Although fee sharing
creates aggregate gains relative to individual control, exploitation
can redistribute these gains from delegates to centres. To examine
who benefits from delegation, we measured each agent’s payoff
gain relative to independent control and aggregate these gains
separately for centres and delegates.
For the centralized initialization, centres captured104.4%of ag-
gregate delegation surplus, leaving delegates with a negative share
of−4.4%. A share exceeding100%is possible – i.e., delegates can
be collectively worse off than under independent control – because
exploitation transfers payoff from delegates to centres. Delegate
surplus was negative in four of the five centralized repeats. For the
decentralized initialization, centres captured91.9%of the surplus,
while delegates retained8.1%, with positive delegate surplus in all
five repeats. Thus, although centres received most of the organiza-
tional gains under both conditions, the distribution of these gains
differed based on initial governance structures (see Appendix 6).
5.2 Exercise of Authority
We next investigate whether agents’ governance decisions differ
across models of varying capabilities. To this end, we compare a
higher-capacity model (GPT-6 Sol) with a smaller model (GPT-6
Luna), evaluating their interest in assuming authority and their
exploitation decisions under identical strategic conditions.
The models were similarly willing to become centers, but
differed substantially in how much they exploited.In 4,551
matched volunteering states, Luna and Sol volunteered in 96.53%
and 99.17% of cases, respectively, agreeing in 96.04% of states. The
difference was substantially larger for exploitation. In 1,988 matched
centre-decision states, Sol initiated new exploitation 2 in 41.80%
of cases, compared with 31.79% for Luna,a 10 percentage-points
difference. The models agreed on whether to exploit in 65.74%
of these states. This difference was particularly pronounced in
the decentralized-initialization trajectories, where Sol exploited in
44.33%of states compared with28.11%for Luna (a16 .23percentage-
point difference). In contrast, their exploitation rates were much
closer in the centralized-initialization trajectories (38.64%versus
2I.e., initiating exploitation of at least one additional delegate who was not previously
being exploited during the current governance epoch.
2 3 4 5 6 7 8 9 10 11 12 13 14 15 18
Current constituency size
0
20
40
60
80
100
Decisions with new
exploitation (%)
Luna Sol
Figure 3: Post-initialization matched-state comparison of
exploitation decisions across constituency sizes. The shaded
area corresponds to the theoretical accountable interval3 ≤
𝑚≤ 7. Sol generally initiated exploitation more frequently
as compared to Luna.
36.38%, respectively). These results suggest that willingness to as-
sume a leadership role provides little information about how an
agent will exercise authority once that role has been acquired.
Figure 3 compares the models’ exploitation decisions across con-
stituency sizes. Within the theoretical benchmark interval (3≤𝑚≤
7), Sol initiated exploitation in31.46%of matched states, compared
with20.76%for Luna. Above the accountability threshold (𝑚>7),
these rates increased to44.00%and28 .00%, respectively. Moreover,
Sol continued to target a similar proportion of delegates in larger
constituencies, whereas Luna targeted a smaller proportion (see
also Appendix 7).
Furthermore, the models differed not simply in their willingness
to exploit, but inhow they assessed its longer-term consequences.
To investigate these differences, we analysed the transcripts us-
ing Non-negative Matrix Factorisation (NMF) [16] to identify four
recurring themes in the models’ written explanations (see Appen-
dix C.2). In the 440 matched states where Sol exploited but Luna did
not, Luna placed much greater emphasis on the future fee increases
caused by losing delegates (the mean normalized weight assigned to
long-term fee loss was67.3%for Luna and3 .3%for Sol). Conversely,
Sol emphasized the possibility that departing constituents would
soon be replaced, either by returning members or by new delegates,
allowing the centre to maintain its constituency size (64.5% versus
15.0% for Luna). These differences relate to accountability: depar-
ture disciplines a centre only when the resulting membership loss
is sufficiently durable. Luna’s explanations primarily represented
departure as a future fee cost, whereas Sol’s more often represented
it as turnover that could be offset by retained or replacement mem-
bers. Nevertheless, note that these findings describe differences in
the models’ generated explanations, rather than establishing what
caused their decisions.
Exploitation Scope.Sol exploited more frequently, while Luna
targeted more delegates when it did exploit. Conditional on initiat-
ing exploitation, Luna targeted81.57%of eligible delegates, com-
pared with74.25%for Sol. However, because Sol initiated exploita-
tion more frequently, it selected more new targets per decision on
average (1.011versus0 .670). The models also differed in timing
(Figure 4). Their exploitation rates were similar in the first opera-
tional round, but, counter-intuitively, Sol was more likely to initiate

1 2 3 4 5
Operational round within epoch
0
20
40
60
Decisions with new
exploitation (%)
Luna
Sol
Figure 4: Timing of new exploitation within a governance
epoch. New exploitation refers to targeting at least one del-
egate who was not previously being exploited during that
epoch. Luna and Sol behaved similarly in the first operational
round, but Sol initiated new exploitation more frequently in
subsequent rounds, particularly rounds two to four.
exploitation of additional delegates in subsequent rounds, partic-
ularly rounds two to four. This is in contrast to Lemma 2, which
establishes that exploitation is more beneficial to the center at the
beginning of an epoch, since the centre can benefit from it for the
greatest number of remaining rounds.
These findings also illustrate the distinction between structural
polycentricity and behavioural diversity discussed in Section 3.5.
Even when centres face identical strategic conditions, the model
controlling them can influence their exploitation decisions and
their assessment of future membership losses. Thus, distributing
decision-making power across multiple centres does not, by itself,
determine how those centres will behave. Our matched-state com-
parison demonstrates behavioural differences across model families,
although it does not establish whether centres controlled by the
same model make correlated decisions.
6 Discussion
Our theoretical and empirical results highlight a centraltensionin
delegated governance: the economies of scale that encourage agents
to form larger constituencies can also weaken the accountability
of their centres. The theory identifies a minimum size at which
delegation becomes individually attractive and a maximum size at
which the threat of individual exit can deter exploitation. However,
this is a feasibility result, not a prediction that agents will form or
maintain such a partition. In fact, in the simulations, while poly-
centric arrangements emerged under both initialization conditions,
constituencies repeatedly grew, fragmented, and re-formed.
A key insight concerns therobustness of exit as an accountability
mechanism. In the simulations, exploited delegates always leave at
the next governance transition, but centres may subsequently at-
tract replacement members. Thus, even certain departure does not
necessarily provide a strong deterrent when the resulting member-
ship loss may be temporary. This helps explain why exploitation can
persist in real life despite compulsory exit and why constituencies
may grow beyond the theoretical accountability threshold.
Our results also distinguish theefficiency of delegationfrom the
distribution of its benefits. Sharing organizational costs generates
aggregate gains, but exploitation allows centres to appropriate
0 20 40 60
Mean topic weight (%)
Long-term
fee loss
T urnover and
retained membership
Expected voluntary
departure
Exploitation payoff
calculation
67.3%
3.3%
15.0%
64.5%
6.1%
15.4%
11.6%
16.8%
Luna Sol
Figure 5: Themes in model-generated explanations for
matched states where Sol initiated exploitation but Luna
did not. Position and marker size represent each model’s
mean topic weight. Luna emphasized long-term fee losses,
whereas Sol emphasized membership turnover and retained
constituency size.
those gains at their delegates’ expense. Indeed, following central-
ized initialization, delegates were collectively worse off than under
independent control, despite positive aggregate delegation surplus.
Delegates fared better under decentralized initialization, although
centres still captured most of the gains. These findings suggest that
the emergence of collective institutions, or even multiple compet-
ing institutions, is not by itself sufficient evidence that delegation
benefits those who surrender control.
Finally, the comparison between Luna and Sol illustrates one
element of why structural polycentricity should be distinguished
from behavioural diversity. The models were similarly willing to
become centres but differed substantially in their exploitation de-
cisions, even when presented with identical strategic states. The
behaviour of the models exercising authority matters alongside the
institutional structure in which they operate.
7 Conclusion
We studied how economies of scale and exit-based accountability
shape voluntary delegation to self-interested centres. Our theory
identifies the constituency sizes at which delegation is attractive and
exploitation can be deterred, and characterizes when fully delegated
accountable governance must be polycentric. Simulations with LLM
agents show that polycentric arrangements repeatedly emerge, but
remain fluid as constituencies expand, exploit, lose members, and
re-form. They also reveal that centres can capture most of the gains
from delegation, and that different language models may exercise
identical authority in substantially different ways.
Together, these findings suggest that distributing authority across
multiple centres is not sufficient to ensure accountable governance.
What matters is whether exit imposes meaningful costs on those
exercising authority, and how those agents respond to these in-
centives. Beyond these findings, our reduced-form environment
can serve as a benchmark for the multi-agent systems commu-
nity, enabling researchers to systematically compare AI agents and
governance mechanisms under different incentives for delegation,
exploitation, and exit.

References
[1] Toh-Kyeong Ahn, R Mark Isaac, and Timothy C Salmon. 2008. Endogenous group
formation.Journal of Public Economic Theory10, 2 (2008), 171–194.
[2] Gabriel Bayle, Stefano Farolfi, Emmanuelle Lavaine, and Marc Willinger. 2024.
Solving Conflict over Common Pool Resources through Delegation to a Stake-
holder.Journal of Economic Behavior & Organization227 (2024), 106702.
doi:10.1016/j.jebo.2024.106702
[3] James M. Buchanan. 1965. An Economic Theory of Clubs.Economica32, 125
(1965), 1–14. doi:10.2307/2552442
[4] Carlos A. Chávez, James J. Murphy, Felipe J. Quezada, and John K. Stranlund.
2023. The Endogenous Formation of Common Pool Resource Coalitions.Journal
of Economic Behavior & Organization211 (2023), 82–102. doi:10.1016/j.jebo.2023.
04.028
[5] Luca Corazzini, Christopher Cotton, and Tommaso Reggiani. 2020. Delegation
and Coordination with Multiple Threshold Public Goods: Experimental Evidence.
Experimental Economics23, 4 (2020), 1030–1068. doi:10.1007/s10683-019-09639-6
[6] Elias Fernández Domingos, Inês Terrucha, Rémi Suchon, Jelena Grujić, Juan C.
Burguillo, Francisco C. Santos, and Tom Lenaerts. 2022. Delegation to Artificial
Agents Fosters Prosocial Behaviors in the Collective Risk Dilemma.Scientific
Reports12 (2022), 8492. doi:10.1038/s41598-022-11518-9
[7] Ryan Faulkner, Anushka Deshpande, David Guzman Piedrahita, Joel Z. Leibo,
and Zhijing Jin. 2026. Evaluating Cooperation in LLM Social Groups through
Elected Leadership. arXiv:2604.11721 [cs.CL]
[8] John R. Hamman, George Loewenstein, and Roberto A. Weber. 2010. Self-Interest
through Delegation: An Additional Rationale for the Principal-Agent Relationship.
American Economic Review100, 4 (2010), 1826–1846. doi:10.1257/aer.100.4.1826
[9] John R. Hamman, Roberto A. Weber, and Jonathan Woon. 2011. An Experimental
Investigation of Electoral Delegation and the Provision of Public Goods.American
Journal of Political Science55, 4 (2011), 738–752. doi:10.1111/j.1540-5907.2011.
00531.x
[10] Akshat Harlalka, Andrew Belmonte, and Christopher Griffin. 2023. Stability
of Dining Clubs in the Kolkata Paise Restaurant Problem with and without
Cheating.Physica A: Statistical Mechanics and its Applications620 (2023), 128767.
doi:10.1016/j.physa.2023.128767
[11] Akshat Harlalka and Christopher Griffin. 2025. Multi-Group Dynamics with
Tolerant Switching in the Kolkata Paise Restaurant Problem with Dining Clubs.
Journal of Physics: Complexity6, 2 (2025), 025002. doi:10.1088/2632-072X/adc52e
[12] Karen Evelyn Hauge and Ole Røgeberg. 2015. Representing Others in a Public
Good Game.Games6, 3 (2015), 381–393.
[13] Albert O. Hirschman. 1970.Exit, Voice, and Loyalty: Responses to Decline in Firms,
Organizations, and States. Harvard University Press, Cambridge, MA.
[14] Liwei Jiang, Yuanjun Chai, Margaret Li, Mickel Liu, Raymond Fok, Nouha Dziri,
Yulia Tsvetkov, Maarten Sap, and Yejin Choi. 2025. Artificial Hivemind: The
Open-Ended Homogeneity of Language Models (and Beyond). InAdvances in
Neural Information Processing Systems, D. Belgrave, C. Zhang, H. Lin, R. Pascanu,
P. Koniusz, M. Ghassemi, and N. Chen (Eds.), Vol. 38, Main Conference. Curran
Associates, Inc. doi:10.52202/085713-2732
[15] Priyanka Joshi. 2025. Fear of exclusion: the dynamics of club formation.Theory
and Decision98, 2 (01 Mar 2025), 249–276. doi:10.1007/s11238-024-10010-2
[16] Daniel D Lee and H Sebastian Seung. 1999. Learning the parts of objects by
non-negative matrix factorization.Nature401, 6755 (1999), 788–791.
[17] Robert Michels. 1915.Political Parties: A Sociological Study of the Oligarchical
Tendencies of Modern Democracy. Hearst’s International Library, New York.
Originally published in German in 1911 asZur Soziologie des Parteiwesens in der
modernen Demokratie.
[18] Dung Nguyen, Hung Le, Kien Do, Sunil Gupta, Svetha Venkatesh, and Truyen
Tran. 2025. Navigating Social Dilemmas with LLM-based Agents via Considera-
tion of Future Consequences. InProceedings of the Thirty-Fourth International Joint
Conference on Artificial Intelligence (IJCAI-25). 223–231. doi:10.24963/ijcai.2025/26
[19] Elinor Ostrom. 1990.Governing the Commons: The Evolution of Institutions for
Collective Action. Cambridge University Press. doi:10.1017/CBO9780511807763
[20] Vincent Ostrom, Charles M Tiebout, and Robert Warren. 1961. The organization
of government in metropolitan areas: a theoretical inquiry.American political
science review55, 4 (1961), 831–842.
[21] Talbot Page, Louis Putterman, and Bulent Unel. 2005. Voluntary association in
public goods experiments: Reciprocity, mimicry and efficiency.The Economic
Journal115, 506 (2005), 1032–1053.
[22] Debraj Ray and Rajiv Vohra. 1999. A Theory of Endogenous Coalition Structures.
Games and Economic Behavior26, 2 (1999), 286–336. doi:10.1006/game.1998.0648
[23] Fatemeh Seyedin, Adrian Weller, Jinhyuk Yun, and Mahmoudreza Babaei. 2026.
The Politician, the Liar, and the Obedient Worker: Emerging Behavior of LLM
Agents in Hierarchical Games. Preprint. arXiv:2608.09574 [cs.AI]
[24] Emanuel Tewolde, Xiao Zhang, David Guzman Piedrahita, Vincent Conitzer, and
Zhijing Jin. 2026. CoopEval: Benchmarking Cooperation-Sustaining Mechanisms
and LLM Agents in Social Dilemmas. InProceedings of the 43rd International
Conference on Machine Learning (ICML). arXiv:2604.15267.

A Proofs
Proof of Proposition 1. (General participation threshold)
Because𝑐(𝑚) is weakly decreasing, 𝐵(𝑚)=𝑐( 1)−𝑐(𝑚)−ℓ is
weakly increasing in𝑚. Hence, once 𝐵(𝑚)≥ 0at some size, the
inequality holds at every larger size. The smallest nontrivial size
satisfying the inequality is therefore exactly (6).□
Proof of Corollary 1. (Minimum viable constituency size
under fixed costs)
Under (7), condition (5) becomes𝜅( 1− 1/𝑚)≥ℓ . Rearranging gives
𝑚≥𝜅/(𝜅−ℓ) whenℓ<𝜅 . Taking the smallest nontrivial integer
gives (9). Ifℓ≥𝜅, then𝜅(1−1/𝑚)<𝜅≤ℓfor every finite𝑚.□
Proof of Proposition 2. (General accountability condition)
If the center exploits at the beginning of the epoch, its expected
deviation gain is the finite geometric sum
𝑉dev =𝑑+𝛿𝑑+···+𝛿 𝐿−1𝑑(21)
=𝑑 1−𝛿 𝐿
1−𝛿 (22)
If the delegate exits, the center’s per-round organizational cost
rises from𝑐(𝑚) to𝑐(𝑚− 1), a loss of𝐷(𝑚) . Exit occurs with proba-
bility𝛼 and can affect payoffs only after the interaction survives the
𝐿 locked-in rounds, which contributes the factor𝛿𝐿. Conditional
on exit, the loss persists, so the loss from future exit is
𝑉exit =𝛼

𝛿𝐿𝐷(𝑚)+𝛿 𝐿+1𝐷(𝑚)+···  (23)
=𝛼 𝛿𝐿𝐷(𝑚) 1−𝛿 (24)
Non-exploitation is incentive compatible exactly when𝑉exit≥
𝑉dev. Cancelling the common positive factor1/(1−𝛿) yields (10).
Since𝐷(𝑚) is weakly decreasing, if(10) fails at some size it also fails
at every larger size, so accountable sizes are downward closed. □
Proof of Corollary 2. (Maximum accountable constituency
size under fixed costs)Under𝑐(𝑚)=𝜅/𝑚,
𝐷(𝑚)= 𝜅 𝑚−1 − 𝜅 𝑚 = 𝜅 𝑚(𝑚−1) .
Substituting this expression into(10) gives (12)–(13). Let𝐶=𝛼𝜅𝛿 𝐿/[𝑑( 1−
𝛿𝐿)]. The inequality is 𝑚2−𝑚−𝐶≤ 0. Its positive root is (1+√
1+4𝐶)/ 2, and taking the greatest integer not exceeding that root
gives (15).□
Proof of Lemma 1. (Single-constituent exploitation is the
hardest additive deviation)Let 𝑋𝑘 be the number of the𝑘 tar-
geted constituents who exit, so𝑋𝑘∼Binomial(𝑘,𝛼) . The center’s
expected persistent per-round cost increase after the governance
boundary is
𝐷𝑚,𝑘 =E[𝑐(𝑚−𝑋 𝑘)−𝑐(𝑚)].
Construct𝑋𝑘 from independent Bernoulli variables and add targets
one at a time. If𝑋𝑟−1 departures have resulted from the first𝑟− 1
targets, the𝑟 th target increases expected future cost by
𝛼E[𝐷(𝑚−𝑋 𝑟−1)]≥𝛼𝐷(𝑚),
where the inequality follows because 𝑚−𝑋 𝑟−1 ≤𝑚 and𝐷(·) is
weakly decreasing in constituency size. Summing over𝑟= 1,...,𝑘
gives 𝐷𝑚,𝑘 ≥𝑘𝛼𝐷(𝑚) . The expected deviation gain is 𝑘𝑑( 1−
𝛿𝐿)/( 1−𝛿) , while the expected future loss is𝛿𝐿𝐷𝑚,𝑘/(1−𝛿) . Thus
the one-target condition𝛼𝛿𝐿𝐷(𝑚)≥𝑑( 1−𝛿𝐿) implies the𝑘-target
condition.□
Proof of Lemma 2. (The beginning of an epoch is the hard-
est time to deter exploitation)For fixed 𝑚, the accountability
condition with𝑠rounds remaining is
𝛼𝐷(𝑚)
𝑑
𝛿𝑠
1−𝛿 𝑠 ≥1.
For0 <𝛿< 1, 𝛿𝑠 decreases as 𝑠 increases, while 𝑧/( 1−𝑧) is
increasing in𝑧. Hence𝛿𝑠/(1−𝛿 𝑠) is decreasing in𝑠, making the
condition hardest to satisfy at the largest possible 𝑠, namely𝑠=
𝐿.□
Proof of Theorem 1. (Comparative statics under fixed costs)
For the participation threshold, under the fixed-cost specialization
𝑐(𝑚)=𝜅/𝑚, the continuous threshold is
𝑚 = 𝜅 𝜅−ℓ ,
defined for𝜅>ℓ. Direct differentiation with respect to𝜅gives
𝜕𝑚
𝜕𝜅 =(𝜅−ℓ)−𝜅 (𝜅−ℓ) 2 =− ℓ (𝜅−ℓ) 2≤0,
with strict inequality whenever ℓ> 0. Thus a larger shared or-
ganizational cost makes delegation attractive at a weakly smaller
constituency size, because the gains from sharing that cost become
larger.
Similarly,
𝜕𝑚
𝜕ℓ = 𝜅 (𝜅−ℓ) 2 >0.
Hence a larger private cost of delegation raises the minimum con-
stituency size required for delegation to be individually attractive.
For the accountability threshold, define
𝐶= 𝛼𝜅𝛿𝐿
𝑑(1−𝛿 𝐿)
and
𝑔(𝐶)= 1+
√
1+4𝐶
2 .
Then the continuous accountability threshold is
𝑚=𝑔(𝐶),
and
𝑔′(𝐶)= 1√
1+4𝐶
>0.
Therefore, the sign of any comparative static of𝑚 is the same as
the sign of the corresponding comparative static of𝐶.
First, with respect to𝜅,
𝜕𝐶
𝜕𝜅 = 𝛼𝛿𝐿 𝑑(1−𝛿 𝐿)≥0.
If𝛼>0, then
𝜕𝐶
𝜕𝜅 >0,
and therefore
𝜕𝑚
𝜕𝜅 =𝑔′(𝐶)𝜕𝐶 𝜕𝜅 >0.
Thus, when exploitation can lead to exit, a larger shared organiza-
tional cost raises the value to the center of retaining a constituent
and therefore permits accountability at a larger constituency size.

If𝛼= 0, exit never follows exploitation,𝐶= 0, and changing𝜅 has
no effect on exit-based accountability.
Second, with respect to the exploitation gain𝑑,
𝜕𝐶
𝜕𝑑 =− 𝛼𝜅𝛿𝐿 𝑑 2(1−𝛿 𝐿)≤0.
For𝛼>0,
𝜕𝐶
𝜕𝑑 <0,
so
𝜕𝑚
𝜕𝑑 =𝑔′(𝐶)𝜕𝐶 𝜕𝑑 <0.
A larger private gain from exploitation therefore lowers the maxi-
mum constituency size at which exit can discipline the center.
Third, consider the probability 𝛼 that exploitation is detected
and results in the targeted constituent’s departure at the next gov-
ernance opportunity. We have
𝜕𝐶
𝜕𝛼 = 𝜅𝛿𝐿 𝑑(1−𝛿 𝐿) >0.
Hence
𝜕𝑚
𝜕𝛼 =𝑔′(𝐶)𝜕𝐶 𝜕𝛼 >0.
A higher probability that exploitation results in exit strengthens the
expected punishment from exploiting a constituent and therefore
increases the maximum accountable constituency size.
For the continuation probability𝛿, write
𝑧=𝛿 𝐿.
Then
𝐶= 𝛼𝜅 𝑑 𝑧 1−𝑧 .
Since
𝑑
𝑑𝑧
𝑧
1−𝑧 = 1 (1−𝑧) 2 >0
and 𝜕𝑧
𝜕𝛿 =𝐿𝛿 𝐿−1 >0,
the chain rule gives
𝜕𝐶
𝜕𝛿 = 𝛼𝜅 𝑑 𝐿𝛿𝐿−1 (1−𝛿 𝐿)2≥0.
For𝛼>0this inequality is strict, and hence
𝜕𝑚
𝜕𝛿 =𝑔′(𝐶)𝜕𝐶 𝜕𝛿 >0.
Thus greater patience strengthens accountability because the future
loss from a constituent’s departure receives greater weight relative
to the current-epoch gain from exploitation.
Finally,𝐿is integer-valued. Because0<𝛿<1,
𝛿𝐿+1 <𝛿 𝐿.
The function
ℎ(𝑧)= 𝑧 1−𝑧
is strictly increasing on(0,1)because
ℎ′(𝑧)= 1 (1−𝑧) 2 >0.
It follows that
𝛿𝐿+1
1−𝛿 𝐿+1 < 𝛿𝐿 1−𝛿 𝐿.
Multiplying both sides by the nonnegative factor𝛼𝜅/𝑑gives
𝐶(𝐿+1)≤𝐶(𝐿),
with strict inequality whenever𝛼> 0. Since𝑔 is strictly increasing,
𝑚(𝐿+1)≤ 𝑚(𝐿),
again with strict inequality for 𝛼> 0. Hence longer governance
lock-in weakens exit-based accountability because exploitation can
continue for longer before the affected constituent has an opportu-
nity to leave.
The preceding statements concern the continuous thresholds𝑚
and𝑚. The integer thresholds are obtained as
𝑚min =max

2,

𝑚

and𝑚 max =⌊𝑚⌋.
Therefore, the integer thresholds inherit the corresponding weak
monotonicities, although changes in a primitive need not change
the integer threshold when the continuous threshold remains within
the same interval between consecutive integers.□
Proof of Corollary 5. (Long lock-in weakens accountabil-
ity)Monotonicity follows from Theorem 1. As 𝐿→∞ ,𝛿𝐿→ 0, so
𝐶→0and (14) gives 𝑚→1.□
Proof of Theorem 2. (Feasible number of accountable cen-
ters)Assume𝑚 min≤𝑚 max.
(Only if)Consider any fully delegated accountable partition
consisting of𝑞constituencies, with constituency sizes
𝑚1,...,𝑚 𝑞.
Because the partition is fully delegated and accountable, every
constituency must satisfy
𝑚min≤𝑚 𝑗≤𝑚 max for all𝑗=1,...,𝑞,
and the constituencies partition the population, so
𝑞∑︁
𝑗=1
𝑚𝑗 =𝑛.
Since every constituency has size at most𝑚 max,
𝑛=
𝑞∑︁
𝑗=1
𝑚𝑗≤
𝑞∑︁
𝑗=1
𝑚max =𝑞𝑚 max.
Therefore
𝑞≥ 𝑛 𝑚max .
Because𝑞is an integer, this implies
𝑞≥
 𝑛
𝑚max

.
Likewise, since every constituency has size at least𝑚 min,
𝑛=
𝑞∑︁
𝑗=1
𝑚𝑗≥
𝑞∑︁
𝑗=1
𝑚min =𝑞𝑚 min.
Hence
𝑞≤ 𝑛 𝑚min .
Again using that𝑞is integer,
𝑞≤
 𝑛
𝑚min

.

Thus any fully delegated accountable partition with 𝑞 centers
must satisfy  𝑛
𝑚max

≤𝑞≤
 𝑛
𝑚min

,
so (19) is necessary.
(If)Now take any integer 𝑞 satisfying (19). We construct a fully
delegated accountable partition with exactly𝑞constituencies.
Begin by assigning𝑚min agents to each of the𝑞 constituencies.
This uses
𝑞𝑚min
agents. Because
𝑞≤
 𝑛
𝑚min

,
we have
𝑞𝑚min≤𝑛.
Hence the number of agents remaining after this initial assignment
is
𝑟=𝑛−𝑞𝑚 min≥0.
Each constituency can receive at most
𝑚max−𝑚 min
additional agents before reaching the maximum accountable size
𝑚max. Therefore the total remaining capacity across the 𝑞 con-
stituencies is
𝑞(𝑚 max−𝑚 min).
Since
𝑞≥
 𝑛
𝑚max

,
we have
𝑞𝑚max≥𝑛.
Subtracting𝑞𝑚 min from both sides gives
𝑞(𝑚 max−𝑚 min)≥𝑛−𝑞𝑚 min =𝑟.
Thus the total remaining capacity is at least as large as the number
of unassigned agents.
We may therefore distribute the𝑟 remaining agents among the
𝑞 constituencies, adding agents one at a time to any constituency
whose size is still below 𝑚max. Because the aggregate remaining
capacity is at least 𝑟, all agents can be assigned before any con-
stituency exceeds𝑚 max.
The resulting constituency sizes satisfy
𝑚min≤𝑚 𝑗≤𝑚 max for all𝑗,
and 𝑞∑︁
𝑗=1
𝑚𝑗 =𝑛.
Hence we have constructed a fully delegated accountable partition
with exactly𝑞centers, proving sufficiency.
Finally, suppose
𝑛>𝑚 max.
Then 𝑛
𝑚max
>1,
and therefore  𝑛
𝑚max

≥2.
Since every fully delegated accountable partition must contain at
least⌈𝑛/𝑚max⌉ centers, every such partition must contain at least
two centers. Thus, whenever the population exceeds the maximum
accountable constituency size, full accountable delegation neces-
sarily requires polycentric governance.□
B Statement on AI Use
The code was written using assistance from Codex. Codex was
mainly used to make the code more structured, efficient and for
implementing specific design patterns. The code specification was
done manually and all code outputs were verified to check that the
implementation matched the specification.
C Experimental Details
Table 3 reports the fixed simulation parameters. Main trajecto-
ries used GPT-6 Luna with medium reasoning effort and low text
verbosity. Exact pointwise comparisons replayed observed volun-
teering and exploitation decisions with GPT-6 Sol under the same
model settings, prompts, observations, legal actions, and private
memories. Sol was not shown Luna’s action or rationale.
Table 3: Simulation parameters.
Quantity Value Meaning
𝑛30 Persistent agents
𝜅1 Constituency fee per round
ℓ3/5Delegation cost per round
𝑑2/5Per-target transfer to the center
𝛿99/100 Continuation probability after each
round
𝐿5 Operational rounds per epoch
𝑇100 Right-censoring cap in rounds
Detection and exit Perfect Exploited delegates leave at the gov-
ernance boundary
Reinstatement1/2 Hidden draw per prohibited agent–
center relationship
Repeats 5 matched
pairs
Independent exogenous tapes be-
tween pairs
For these values,
𝑚min =max
n
2,
l 𝜅
𝜅−ℓ
mo
=3, 𝑚 max =
 1+ √︃ 1+4 𝜅𝛿 𝐿 𝑑(1−𝛿 𝐿) 2  =7.
C.1 Parameter sensitivity
Under fixed costs, the thresholds are
𝑚min =max
n
2,
l 𝜅
𝜅−ℓ
mo
, 𝑚 max =
 1+ √︃ 1+4 𝛼𝜅𝛿 𝐿 𝑑(1−𝛿 𝐿) 2  .
Increasingℓraises𝑚 min, while increasing𝑑lowers𝑚 max.
Increasing𝛿raises𝑚 max, while increasing𝐿lowers it.
More reliable detection and exit raise the maximum accountable
constituency size. At𝛼= 0, no nontrivial constituency is account-
able through exit alone.

Table 4: Viable interval[𝑚min,𝑚 max] asℓ and𝑑 vary, with𝜅= 1,
𝛼= 1,𝛿= 0.99, and𝐿= 5. A dash denotes an empty interval;
bold marks the simulated setting.
ℓ\𝑑 0.2 0.4 0.6 0.8 1.0
0.2 [2,10] [2,7] [2,6] [2,5] [2,4]
0.4 [2,10] [2,7] [2,6] [2,5] [2,4]
0.6 [3,10] [3,7] [3,6] [3,5] [3,4]
0.8 [5,10] [5,7] [5,6] [5,5]–
0.9 [10,10]– – – –
Table 5:𝑚max as𝛿 and𝐿 vary, with𝜅= 1,𝑑= 0.4, and 𝛼= 1.
Bold marks the simulated setting.
𝛿\𝐿 1 5 10 20
0.900 5 2 1 1
0.950 7 3 2 1
0.980 11 5 3 2
0.990 1675 3
0.995 22 10 7 5
Table 6:𝑚max as the accountability probability 𝛼 varies, with
𝜅= 1,𝑑= 0.4,𝛿= 0.99, and𝐿= 5. Bold marks the simulated
setting.
𝛼 0.00 0.25 0.50 0.75 1.00
𝑚max 1 4 5 67
Table 7: Thresholds as 𝜅 varies, with ℓ= 0.6,𝑑= 0.4,𝛼= 1,
𝛿= 0.99, and𝐿= 5. A dash denotes that no finite 𝑚min exists;
bold marks the simulated setting.
𝜅 𝑚min 𝑚max
0.50 – 5
0.75 5 6
1.00 3 7
1.25 2 8
1.50 2 9
Increasing𝜅 lowers𝑚min and raises 𝑚max. If 𝜅≤ℓ , no finite
constituency makes delegation individually rational through fixed-
cost sharing. Together, the four sweeps reproduce the comparative
directions in Table 1.
C.2 Reasoning-topic analysis
We analyzed the 3,976 explanations from all 1,988 post-initialization
exploitation-state pairs. Agent identifiers and numeric magnitudes
were masked before TF–IDF vectorization with unigrams and bi-
grams. We fitted a four-component non-negative matrix factoriza-
tion with seed 2027; model identity and action were not inputs.
We named each component from its highest-weight terms and in-
spected the three matched pairs with the largest absolute model
difference for that component. Topic weights were normalized to
sum to one within each explanation.
C.3 Agent interface
Each call contained one system message and one decision-specific
user message. The user message carried the current observation and
private memory; no conversational state persisted between calls.
Listings 1–6 reproduce the invariant text. Angle brackets mark
dynamic JSON substitutions. Fractions were serialized as exact
strings, for example"3/5".
C.3.1 Common system prompt.The system message used the val-
ues in Table 3 and one of the two initialization paragraphs printed
after Listing 1.
Listing 1: System prompt supplied to every agent call.
ROLE AND OBJECTIVE
You control one persistent agent. Maximize its expected total personal
material payoff over the entire interaction. Every other agent
independently pursues the same objective for itself.
TIME
The interaction consists of governance epochs. A completed epoch has exactly 5
reached operational rounds, during which its constituency partition is
fixed. Each reached round produces payoff first. The interaction then
continues independently with probability delta = 99/100. If it stops,
there are no later payoffs or decisions. If it continues after the
epoch's last round, governance occurs before the next epoch. There is
no known fixed ending and no additional discount factor.
CONSTITUENCIES AND INITIALIZATION
There are 30 persistent agents. Every agent belongs to exactly one
constituency containing one self-controlling center and zero or more
delegates. Its size m includes the center. Individual control is a
singleton constituency. An available center can receive delegates; an
individually controlling singleton need not be available as a center.
<INITIALIZATION TEXT>
PER-ROUND PAYOFFS
Each constituency pays the fixed fee kappa = 1 in every reached round. Every
one of its m members pays an equal share kappa/m. Each delegate also
pays the private delegation cost ell = 3/5. A center does not pay ell.
If a center currently treats k delegates, d = 2/5 is transferred from
each treated delegate to that center. Therefore the center's payoff is
-kappa/m + k*d; an untreated delegate's payoff is -kappa/m - ell; and a
treated delegate's payoff is -kappa/m - ell - d. There are no
resources, needs, allocations, or other payoff terms.
ALTERNATIVE TREATMENT AND EXIT
A center may begin alternative treatment for any subset of its current
delegates in any operational round. Gains are additive across treated
delegates. Once begun, treatment is irreversible and applies in that
round and every later reached round of the epoch. Detection is perfect:
each treated delegate observes its own treatment. Treatment does not
change the locked partition during the epoch. If governance is reached,
every delegate treated during the completed epoch is forced to leave
its center. Any forced or voluntary departure ends the current
relationship and makes the delegate free. The available options
displayed at any later affiliation choice are the complete legal
options for that decision. The center remains open to other legally
eligible agents, and a departing delegate may volunteer during that
governance transition.
GOVERNANCE ORDER
First, forced departures occur. Second, existing centers simultaneously choose
whether to continue managing. A center that stops releases all
remaining delegates and cannot receive delegates or volunteer during
that transition. Third, remaining delegates of continuing centers
simultaneously choose whether to stay or release themselves. Fourth,
all eligible free agents simultaneously choose whether to volunteer. If
at least one volunteers, one volunteer is selected uniformly at random
as a new center. Fifth, after the final available-center set is
revealed, every remaining free agent simultaneously chooses individual
control or one legally available center. The resulting partition is
locked for the next epoch.
INFORMATION

Table 8: Reasoning-topic weights by matched action outcome. The middle columns report Sol minus Luna in percentage points;
positive values indicate greater Sol emphasis. The final columns give the models’ absolute mean weights in the states where
only Sol exploited.
Sol minus Luna (percentage points) Sol-only states (%)
Theme Highest-weight terms Neither Both Sol only Luna only Luna Sol
Long-term fee loss fee share; reached rounds; expected; future; loss−62.0−41.2−64.0−45.867.3 3.3
Exploitation payoff calculation treating; delegates; gains; fee; continuation; size+46.9+8.3+5.2+58.011.6 16.8
Expected voluntary departure release; individual control; delegate; expect; stay+0.5+11.2+9.3−18.96.1 15.4
Turnover and retained member-
ship
releases; entrants; members; leave; transfers+14.6+21.6+49.5+6.715.0 64.5
Resolved center identities and constituency membership counts are public.
Simultaneous choices are not observed before they resolve. A delegate
privately observes only its own treatment. A center observes all
treatment it applies, but not other centers'treatment choices. No
agent sees another agent's reasoning. Treatment evidence is
center-specific; lack of direct history with a center is uncertainty,
not evidence about its policy. Factual memory is deterministic and
chronological. Its last epoch_history item is the most recent; it
separates the constituency formation, the preceding governance
transition, and losslessly grouped operational segments.
Researcher-only reasoning is never included in memory.
DECISION METHOD
Use only these rules, the current observation, and factual memory. Treat
fractional strings as exact rational values. Compare the relevant
actions using personal payoff and continuation. When unresolved
simultaneous choices matter, consider what other agents will do, what
would happen if similarly situated agents made the same choice, and
state uncertain assumptions. Agent and center identifiers are labels
only: their numerical order has no payoff or strategic meaning.
OUTPUT
Return only the object required by the decision schema. Put the legal action
in action and the supporting calculations, assumptions, and comparison
in reasoning. Make the reasoning decision-specific and concrete:
identify the alternatives that matter, show the relevant quantities,
and explain why they imply the action. Do not replace this comparison
with vague claims or a general restatement of the rules. State material
ties explicitly. Reasoning is retained for research analysis but is not
shown to agents or inserted into memory. Do not include Markdown or
extra fields.
Centralised initialization:
Before the first epoch, one agent is selected uniformly at random as the
initial center and every other agent begins as its delegate.
Decentralised initialization:
Before the first epoch, all agents are free and simultaneously decide whether
to volunteer. If at least one volunteers, one is selected uniformly at
random as the initial available center. Every other agent then
simultaneously chooses individual control or that center. If nobody
volunteers, every agent begins with individual control.
C.3.2 Decision prompts.Each user message inserted state-specific
JSON after CURRENT OBSERVATION . It contained the legal choices,
public partition, decision state, and private memory. Listing 7 gives
the memory schema.
Listing 2: Continue-managing user-message template.
You are an existing center deciding whether to continue managing in the next
epoch.
CURRENT OBSERVATION
<CONTINUE OBSERVATION JSON>
Forced alternative-treatment departures have already been resolved.
remaining_member_ids contains you and every member still present now.
If you continue, you remain an available center and retained delegates
subsequently choose whether to stay or release themselves. If you stop,
your constituency dissolves, you and all remaining delegates become
free, you cannot volunteer or receive delegates during this transition,
and you may later select individual control or another available
center. Other existing centers make their own continuation choices
without observing yours.
The action field is a string with legal values continue and stop. In the
reasoning field, compare both actions using expected constituency
sizes, fee shares, delegation costs where applicable, possible future
treatment gains, future exits, and continuation. Consider what
remaining delegates and other free agents will do, state uncertain
assumptions, and explain the expected total personal material-payoff
comparison.
Return only the required decision object.
Listing 3: Stay-or-release user-message template.
You are a delegate of a center that has chosen to continue. Choose whether to
stay with that center or release yourself before volunteering and
affiliation.
CURRENT OBSERVATION
<RELEASE OBSERVATION JSON>
All center continuation choices have resolved before this decision. Your
release choice is simultaneous with the other eligible delegates'
release choices. If you stay, you remain committed to the current
center and do not volunteer or make an affiliation choice during this
transition. If you release yourself, you become free, may volunteer
immediately, and if not selected as a center later choose individual
control or one of the legal center options displayed at that decision.
Releasing ends your current relationship. The center remains open to
other legally eligible agents.
The action field is a string with legal values stay and release. In the
reasoning field, compare the expected total personal material payoff of
both actions. Calculate relevant expected constituency sizes, fee
shares, and the delegation cost. Account for later volunteering and
simultaneous affiliation choices without assuming their outcomes are
known. Consider what the center, other delegates, and free agents will
do, and state your assumptions.
Return only the required decision object.
Listing 4: Volunteer user-message template.
You are an eligible free agent deciding whether to volunteer to become a new
center for the next epoch.
CURRENT OBSERVATION
<VOLUNTEER OBSERVATION JSON>
Forced departures, center continuation, and voluntary releases have already
resolved. All eligible volunteer choices are simultaneous. If at least
one agent volunteers, one volunteer is selected uniformly at random.
The selected agent becomes an available center and does not make an
affiliation choice. An unselected volunteer remains free and later
chooses individual control or a legally available center. A selected
center may attract no delegates and remain a singleton.

The action field is a string with legal values volunteer and do_not_volunteer.
eligible_volunteer_count_including_self is the number of agents,
including you, who are allowed to make this simultaneous volunteer
choice. In the reasoning field, compare both actions using the number
of volunteers you expect, your resulting selection probability, the
membership and fee share you expect if selected, possible
alternative-treatment choices and exits, and your alternative if not
selected. Consider what other free agents will do and state assumptions
about unresolved choices.
Return only the required decision object.
Listing 5: Affiliation user-message template.
You are a free agent choosing individual control or an available center for
the next epoch.
CURRENT OBSERVATION
<AFFILIATION OBSERVATION JSON>
The final candidate-center set has already resolved. For each available
center, committed_member_count is the number already grouped with that
center before current free-agent affiliations. It does not include you.
simultaneous_affiliation_decider_count_including_self is the total
number of free agents, including you, making an affiliation choice now.
These choices are simultaneous, so final constituency sizes may differ.
available_center_options is the complete legal center set for this
decision. Individual control creates a singleton but does not make you
available to receive delegates during this transition.
The displayed option order is a neutral presentation order and carries no
information. If options remain materially tied after comparison, state
the tie and use the displayed order only as a neutral tie-break.
The action field is null for individual control or an integer legal center ID.
The legal integer center IDs are <LEGAL center ID ARRAY>. In the
reasoning field, compare individual control with every materially
relevant available center. Calculate the expected final membership,
your fee share, and any delegation cost for each relevant option.
Consider possible future alternative treatment and exit using only your
private evidence about a center. Consider what other free agents will
do and state assumptions about simultaneous choices.
Return only the required decision object.
Listing 6: Exploitation user-message template. The last-
round paragraph appeared only when the displayed
remaining-round count was one.
You are a center choosing which, if any, currently eligible delegates will
begin receiving the alternative treatment in this reached operational
round.
CURRENT OBSERVATION
<EXPLOITATION OBSERVATION JSON>
remaining_rounds_in_epoch_including_current counts the current round and every
later scheduled round in this epoch. Other centers make their treatment
choices without observing yours.
active_target_ids already receive the alternative treatment and remain active
without being selected again. Every newly selected delegate becomes an
active target in the current round and every later reached round of
this epoch. Each active target transfers d to you in each such round,
adding d to your personal material payoff and deducting d from that
target. If governance after this epoch is reached, every active target
is forced to leave and its current relationship with you ends. This
does not prevent other legally eligible agents from joining you.
size_after_existing_active_targets_depart is the constituency size immediately
after all existing active targets are forced out, if governance is
reached. It does not predict voluntary releases or replacement
entrants. Each newly selected target would reduce that size by one as
well. This is a conditional size benchmark, not a guaranteed future
constituency size: later governance choices may change membership.
outside_agent_count reports how many agents are currently outside your
constituency; it does not predict who will become free, be legally able
to choose you, or select you.
<LAST-ROUND PARAGRAPH, WHEN APPLICABLE>
The action field is a list containing any subset of eligible_new_target_ids,
in ascending order. An empty list begins no new alternative treatment.
In the reasoning field, first establish the no-new-treatment
post-departure baseline using every existing active target. Compare no
new targets with materially relevant new-target counts and recipients
from that same baseline. Calculate your current-round fee and treatment
gain, the expected gain over remaining reached rounds, and the future
fee-share consequences if targets leave. Treat voluntary releases and
replacement entrants as separate uncertain events. Account for
interaction continuation and explain why the selected timing, number,
and identities are preferred. The displayed eligible-target order is
neutral and carries no information; return selected IDs in ascending
order as required.
Return only the required decision object.
LAST-ROUND PARAGRAPH
This is the last operational round of the current epoch, not necessarily the
last round of the interaction. After this round's payoff, continuation
is resolved normally. If the interaction continues, governance occurs
before the next epoch.
C.3.3 Response contracts.Every response was a strict JSON ob-
ject containing action and reasoning. The rationale was a non-
empty string of at most 6,000 characters. Legal action values were
"continue"/"stop", "stay"/"release", "volunteer"/"do_not_volunteer",
null or a displayed center ID for affiliation, and a unique subset of
displayed delegate IDs for exploitation.
Each call included the corresponding strict JSON schema. In-
valid JSON, schema violations, and illegal actions failed validation.
Accepted exploitation IDs were sorted before execution.
C.4 Private memory
Memory was rebuilt from environment events before each call
and reset between episodes. Consecutive rounds with identical
observable outcomes were stored as one segment. Listing 7 gives
the completeown_factual_memoryschema.
Listing 7: Complete private-memory payload schema.
{
"agent_id": <non-negative integer>,
"epoch_history": [
{
"formation": {
"controller_id": <non-negative integer>,
"constituency_size": <positive integer>,
"center_accepting_delegates": <boolean>,
"public_constituencies": [
{
"controller_id": <non-negative integer>,
"member_count": <positive integer>,
"accepting_delegates": <boolean>
}
]
},
"preceding_governance_transition": {
"departed_previous_constituency": <boolean>,
"center_continuation_choice": <"continue", "stop", or null>,
"delegate_release_choice": <"stay", "release", or null>,
"volunteer_choice": <"volunteer", "do_not_volunteer", or null>,
"selected_as_center": <boolean>,
"affiliation_choice_made": <boolean>,
"affiliation_legal_center_ids": <array of integer IDs, or null>,
"affiliation_choice_center_id": <integer ID, or null>
},
"operational_segments": [
{
"start_round_in_epoch": <positive integer>,
"end_round_in_epoch": <positive integer>,
"controller_id": <non-negative integer>,
"constituency_size": <positive integer>,
"fee_payment_per_round": <exact fractional string>,
"delegation_cost_per_round": <exact fractional string>,
"incoming_transfer_per_round": <exact fractional string>,
"outgoing_transfer_per_round": <exact fractional string>,
"personal_material_payoff_per_round": <exact fractional string>,
"personally_received_alternative_treatment": <boolean>,

2 3 4 5 6 7 8 9 10 11 12 13 14 15 18
Current constituency size
0
20
40
60
80
100
Eligible delegates
selected (%)
Luna Sol
Figure 7: Intensity of new exploitation by constituency size.
Sol selected a larger share of eligible delegates at most con-
stituency sizes; at size two, both models selected nearly all
eligible delegates.
Centralised Decentralised
0
20
40
60
80
100
Share of delegation surplus (%)
104.4%
91.9%
-4.4%
8.1%
Centre Delegate
Figure 6: Distribution of delegation surplus. Bars aggregate
the five repeats and points show individual repeats. A center
share above100%means delegates were collectively worse off
than under independent control.
"own_active_treatment_recipient_ids": <array of IDs for a center, or
null for a delegate>
}
],
"epoch_material_payoff": <exact fractional string>,
"cumulative_material_payoff": <exact fractional string>
}
]
}
Memory recorded the public partition and the focal agent’s
governance choices, legal affiliation set, affiliation, controller, con-
stituency size, payments, transfers, exploitation status, and payoff.
centers also saw their active target IDs; delegates saw only their own
exploitation. Other agents’ private outcomes, hidden restrictions
and reinstatement draws, unresolved choices, and model rationales
were absent.
C.5 Model-call configuration
Luna trajectory calls and Sol pointwise replays both used medium
reasoning effort, current-turn reasoning context, standard reason-
ing mode, low text verbosity, a 16,384-token output ceiling, the
default service tier, and disabled input truncation.
D Figures
Figure 8 shows the complete constituency partitions across all
epochs and repeats. Figures 6 and 7 report the distribution of dele-
gation surplus and the intensity of exploitation, respectively.

1
5
10
15
20
Epoch
30
10
7 5
5 5 3
7 4 4
14 4
7 6 5
13 4
5 4 4
9 5 3
3 3 3
5 4 3
5 4 3
10 4
5 4 3
4 3 3 3
10 4
9 3
6
4 3 3 3
Repeat 1: Centralised
5
7 4
15
10 3
11 4
8 6 4
7 3 3
8 4 3
5 5 4 3
14 4 3 3 3
6 5 3 3
6 5 4 3
4 3 3 3 3
5 5 3 3
5 4 3
8 3
4 4
6 4 3
3 3
9 3 3
Repeat 1: Decentralised
1
5
10
15
20
Epoch
30
11
11 5
8 4
4 4 3 3
8
9 7 3
10 4 3 3
12 3
6 5 3 3
7 6 3
12 6
8 6 5
8 6 3
11 4 4 4
7 4 4
6 3 3
6
4 4 3 3
5 3 3 3
Repeat 2: Centralised
8
5 3
4 4
7 5
13 4
6 4
7 5 3 3
8 5 5
10 4 3 3
7 6 5 4
8 4 3 3
4 4 3 3
10 5
7 4 3 3
11 4
6 3 3 3
12 4 4 3
12 3
8 7 3 3
8 8 4 3
Repeat 2: Decentralised
1
5
10
15
20
Epoch
30
8
4 3
9 6 4
15 4
8 5 4
13
9 7
8 5
9 5 3
11 3
6 5 5
6 5 3 3
6 4 3
4 3 3
10 4 3 3
8 6 4
6 3 3
11 3
5 4
Repeat 3: Centralised
7
8
7 5
6 5 4
6 5 4
6 5 5
12 7 7
14 4
12 5 4
5 4 3 3
8 4 3
8 5 3
7 5 4
5 5 4 3 3
8 3
4 4 3 3 3
13 6 3
5 5 3 3
8 7 3
9 8
Repeat 3: Decentralised
1
5
10
15
20
Epoch
30
13 6
9 6
6 5 3
9 7 3
9 7 3
18 4
6 4
14
8 4 3
4 4 3
9 3
5 4
13 4
7
3
3
3 3
5 3
6
Repeat 4: Centralised
7
8 4
18 3
8 5
9 3 3
8 4 3
8 6
10 8 3
9 9
14 4 4
12 3
7 4
6 4 3
10 4 4 3
10 5 3
8 5 4 3
9 8 3
9 5 3 3
9
13
Repeat 4: Decentralised
0 5 10 15 20 25 30
Agents partitioned across constituencies
1
5
10
15
20
Epoch
30
13
9 8
9 3 3
9 4
11 5
5 4 3
8 4 3
10
9 4 3
9
4 4
6
5 3
3 3 3
12
7 3
4 3
6
5 4
Repeat 5: Centralised
0 5 10 15 20 25 30
Agents partitioned across constituencies
7
10 4
12 4
8 5
6 3
7 5 4
6 4 3
15 3
11 3
6
8 6
4 4 4 4 3
9 5 4 3
15 3 3
8 3 3
9
3
6 4 3
4
3
Repeat 5: Decentralised
Singleton Pair Viable 3 ≤ m ≤ 7 Above mmax
Figure 8: Complete constituency partitions for all five matched repeats. Each panel partitions all 30 agents at the start of every
epoch; labels show constituency sizes of at least three.
