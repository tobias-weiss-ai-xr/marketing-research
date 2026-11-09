---
title: 'The Shared Discovery Paradox: How a One-Answer Rule Turns Better Information into Worse Search'
url: https://arxiv.org/abs/2607.18045
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Yohei Nakajima
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.18045
pages: 29
chars: 74900
fetched_at: '2026-11-08T13:21:41+00:00'
kb_version: 1
---

# The Shared Discovery Paradox: How a One-Answer Rule Turns Better Information into Worse Search

The Shared Discovery Paradox
How a One-Answer Rule Turns Better Information into Worse Search
Yohei Nakajima∗
Untapped Capital
July 2026
Abstract
Organizations often pool dispersed information into one ranking and then allow many agents to act on
that shared view. In a discovery problem, this can improve beliefs while reducing coverage. We develop
an exactly solvable benchmark with sixteen boxes, one target, eight searchers, and noisy private clues.
Pooling raises the accuracy of the best single recommendation from0.20 to 0.3835, but repeating that
recommendation lowers group discovery from0.8322 under decentralized clue-following to0.3835. A
coordinated eight-action portfolio using the same pooled reports reaches0.8594, and seven coordinated
actions recover the decentralized benchmark. The paradox is not an information failure. It is a protocol
failure: a one-answer rule compresses a portfolio of available actions into one repeated choice.
We then replace the planner with self-interested searchers who split a prize. The equal-split game is a
potential game. Its anonymous symmetric equilibrium obeys a water-filling rule, and discovery equals
𝑁 times the common equilibrium payoff. In the canonical instance it achieves0.5991: strictly above
consensus, but below both private search and the planner. The exact mixed price of anarchy is2−1/𝑁 ,
while uniform symmetric mixing yields the familiar𝑒/(𝑒−1) limit. A sole-rescue reward, which pays
only an agent who covers the target alone, makes every pure Nash equilibrium first-best. Finally, a latent
common-cue model shows how correlated reports collapse effective discovery channels. The centralized
planner gain rises strictly with copying, and in the canonical environment the symmetric market overtakes
decentralized report-following at copying probability𝑐=0.788462 . In a proportional large-market limit
thefive-protocolorderingsurvivesexactly: consensusdiscoveryvanisheswhileblind,market,private,and
portfolio search converge to0.500, 0.547, 0.847, and0.874. The contribution is a compact benchmark
that separates information, allocation, incentives, and dependence into exact, reusable quantities.
Keywords:collective discovery, organizational search, consensus, congestion games, price of anarchy,
information aggregation, correlated signals.
JEL codes:C72, D23, D83, O31.
1 Introduction
A group can become better informed and less likely to discover what it is looking for. The apparent
contradiction arises when an institution solves an estimation problem and then uses the answer as if it had
solved an allocation problem. Pooling information may identify the most likely target more accurately. Yet if
∗Untapped Capital. Code, data, and an interactive guide:github.com/yoheinakajima/shared-discovery-paradox. All
numerical claims in the paper are reproduced to stated precision by the accompanying verification script; see Appendix D for the
check list and claim-status taxonomy.
1
arXiv:2607.18045v1  [cs.AI]  20 Jul 2026

many available actions are all assigned to that one target, the organization converts a portfolio of attempts into
a repeated bet.
This paper isolates that mechanism in a deliberately small environment. Sixteen boxes contain one
jackpot. Eight searchers receive noisy clues, each naming the correct box with probability0.20. If searchers
independently follow their own clues, group discovery is0.8322. If they pool the clues, identify the posterior
mode, and all follow it, the selected box is more accurate than any individual clue, but discovery falls to
0.3835. If a coordinator instead assigns the same eight available actions to the eight highest-posterior boxes,
discovery rises to0.8594. Even a coordinator who ignores the clues entirely and opens eight distinct boxes
succeeds half the time: no information at all beats informed consensus. The same information supports both
failure and improvement; the action protocol determines which one is realized.
Methodologically, the paper follows a familiar benchmark tradition. Akerlof [1970] compresses quality
uncertainty into a lemons market; Schelling [1971] compresses local preferences into a checkerboard; and
Arthur [1994] compresses strategic crowding into the El Farol problem. Their power comes from making one
mechanism visible in a toy environment that later work can extend, calibrate, or reject. Our narrower object is
the separation between shared beliefs and diversified search. The comparison is methodological, not a claim
of comparable scope. The aim is to make a recurring organizational failure measurable.
The paper develops four layers of the benchmark.
First,weseparatethevalueofinformationfromthequalityoftheactionprotocol. Foraninformationset F
and action budget𝐿, the attainable frontier is the posterior mass of the best𝐿-state portfolio. Protocol loss is
the gap between that frontier and the set actually searched. In the canonical pooled-information environment,
the entire47.60 percentage-point gap between consensus and the optimal eight-action portfolio is protocol
loss. The resulting action-budget frontier yields an integer recovery budget: seven coordinated actions are
sufficient to replace eight decentralized clue-followers.
Second, we ask whether decentralized incentives can supply the missing dispersion. After reports are
pooled,𝑁 self-interested searchers choose boxes and split a unit prize equally if several select the jackpot.
This is a singleton congestion or covering game. It has an exact potential, and its anonymous symmetric
equilibrium takes a water-filling form: posterior mass is traded off against expected prize dilution. The
equilibrium improves on consensus at every posterior, but it can still collide excessively. Averaging over the
canonical report distribution gives discovery0.5991 and only2.67 distinct searches in expectation. Thus the
canonical ordering becomes
𝐺consensus<𝐺 sym market<𝐺 private<𝐺 planner.
Wesharpentheinefficiencyresultfromafactoroftwototheexactbound 2−1/𝑁 forallmixedNashequilibria.
This bound is known in the covering-game literature; the contribution here is a short search-specific proof and
its integration into the Bayesian benchmark. Under a uniform posterior on𝑁 boxes, anonymous symmetric
mixing gives the familiar ratio converging to𝑒/(𝑒−1) , even though efficient asymmetric pure equilibria
coexist.
Third, we identify a minimal incentive correction. Under a sole-rescue rule, the realized prize is paid only
if exactly one searcher chose the target. The expected payoff to an agent is then exactly the posterior mass that
the agent contributes uniquely to coverage. The resulting potential is social discovery itself. With at least as
many boxes as searchers and positive posterior mass on every box, every pure Nash equilibrium assigns one
searcher to each of the𝑁 highest-posterior boxes. This is full pure-strategy implementation of the planner
portfolio, not a dominant-strategy claim: equilibrium selection and mixed behavior remain separate issues.
Fourth, we introduce a latent common-cue copying model. Searchers may repeat the same unobserved
source rather than draw independent clues. Copying reduces the number of effective discovery channels,
2

can make raw report counts mis-rank posterior probabilities, and raises the value of reallocating duplicated
capacity. We prove that the equal-budget centralized planner gain is strictly increasing in the copying
probability. We then run the equal-split game on the herd-aware posterior. In the canonical environment,
decentralized report-following initially dominates the symmetric market because independent clues create
natural coverage. The ranking reverses at𝑐=0.788462 : beyond that point, channel collapse harms private
report-following more than posterior concentration harms the dispersing market.
The ingredients have substantial precedents. Team theory, optimal search, parallel R&D, organizational
learning, information cascades, epistemic networks, potential games, and covering games each formalize
part of the design problem [Marschak and Radner, 1972, Koopman, 1957, Nelson, 1961, March, 1991,
Banerjee, 1992, Bikhchandani et al., 1992, Zollman, 2007, Monderer and Shapley, 1996, Gairing, 2009].
We do not claim that communication-induced convergence, correlated signals, congestion-game inefficiency,
or marginal-contribution incentives are individually new. The contribution is to place them in one exactly
solvable Bayesian discovery benchmark and provide a common set of quantities: one-action value, portfolio
value, protocol loss, recovery budget, effective channel count, anonymous-market value, price of anarchy, and
rescue implementation.
2 The sixteen-box benchmark
There are𝑀=16 boxes, exactly one of which contains a jackpot. The true box is𝜃∈{1,...,16} and has a
uniform prior. There are𝑁=8searchers. Conditional on𝜃, searcher𝑖observes a clue𝑋 𝑖 satisfying
P(𝑋𝑖 =𝜃|𝜃)=𝑝=0.20,P(𝑋 𝑖 =𝑏|𝜃)=𝑞= 1−𝑝 𝑀−1 = 0.8 15 (𝑏≠𝜃).
The clues are conditionally independent in the baseline model. Each searcher can open one box, and the
group succeeds if at least one opened box is the target.
2.1 Three benchmark protocols
Privateclue-following.Eachsearcheropenstheboxnamedbythesearcher’sownclue. Thegroupsucceeds
whenever at least one clue is correct, so
𝐺private=1−(1−𝑝) 𝑁 =1−0.8 8=0.83222784.(1)
Shared consensus.All reports are pooled and every action is assigned to the posterior mode. With a
uniform prior and symmetric independent signals, posterior rank equals report-count rank, so consensus is
plurality with uniform tie-breaking. Exact enumeration gives
𝐺consensus=0.38346871.(2)
The recommendation is substantially better than one private clue, since0.3835>0.20 . But eight identical
actions cover one box, so recommendation accuracy and group discovery coincide.
Shared portfolio.A coordinator observes the same pooled reports and assigns actions to the𝐿 highest-
posterior boxes. With𝐿=8,
𝐺planner=0.85942125.(3)
3

The planner uses the information gain without compressing the action budget.
These values establish the basic paradox:
0.20<𝐺 consensus=0.3835<𝐺 private=0.8322<𝐺 planner=0.8594.
Every participant can follow a better-informed recommendation while the group becomes less likely to
discover the target.
Definition 1(Shared Discovery Paradox).A Shared Discovery Paradox occurs when a shared-information
protocol raises average action quality but lowers union success. If protocolΠ produces actions𝐴1,...,𝐴 𝐿,
define average action quality
𝑄(Π)= 1 𝐿 𝐿∑︁ ℓ=1 P(𝐴ℓ =𝜃)
and discovery𝐺(Π)=P(𝜃∈{𝐴 1,...,𝐴 𝐿}). The paradox is
𝑄(Π𝑆)>𝑄(Π 𝑃)and𝐺(Π 𝑆)<𝐺(Π 𝑃).
In the canonical comparison,𝑄(Π𝑆)=0.3835>0.20=𝑄(Π 𝑃), while𝐺(Π𝑆)=0.3835<0.8322=
𝐺(Π𝑃).
Average action quality admits an exact accounting link to discovery. Let𝐾= ˝𝐿 ℓ=1 1{𝐴ℓ =𝜃} be the
number of actions that select the target. Then𝐿𝑄(Π)=E[𝐾]and𝐺(Π)=P(𝐾≥1), so
𝐿𝑄(Π)−𝐺(Π)=E

(𝐾−1) + .(4)
The right side is the expected number of redundant successful actions. Under consensus𝐾∈{0,8} , so
8𝑄−𝐺=7𝐺=2.684281 : a correct recommendation produces eight identical hits. Under any collision-free
portfolio at most one selected box can be the target, so the gap is zero. Private clue-following lies between the
extremes, with8𝑄−𝐺=1.6−0.832228=0.767772 , because several clues can be simultaneously correct.
The paradox is therefore a statement about duplication: a shared-information protocol can raise𝑄 precisely
by concentrating𝐾.
Blind-portfolio control.A blind control calibrates how expensive that duplication is. With a uniform
prior and no clues at all, a coordinator who assigns the eight actions to eight distinct boxes succeeds with
probability
𝐺blind= 𝑁 𝑀 = 8 16 =0.50.
A completely uninformed but diversified portfolio therefore already outperforms informed consensus at
0.383469. This is not a value-of-information comparison—the two protocols observe different things—but
it makes the action-compression loss transparent: eight coordinated searches that ignore the clues entirely
outperformeightinformedsearchesthatallrepeatthepooledrecommendation. 1 Wetreat 0.50 asacalibration
lineratherthanamemberoftheinstitutionalordering,becauseblindsearchdiscardstheavailableinformation.
1Even eightuncoordinatedblind guesses, drawn independently and uniformly, succeed with probability1−(1−1/16) 8 =
0.403281>0.383469.
4

1 2 3 4 5 6 7 8
Coordinated action budget L
0.4
0.5
0.6
0.7
0.8
0.9Discovery probability
recovery budget L * = 7
Discovery is a budget-indexed frontier
Pooled portfolio frontier
Private clue-following
Figure 1:The exact pooled-information frontier for the canonical benchmark. The one-action consensus value is only
the left endpoint. Seven coordinated actions recover the performance of eight decentralized clue-followers.
2.2 The full action-budget frontier
Consensusevaluatespooledinformationataone-actionbudget. Discoveryisinsteadabudget-indexedfrontier.
Exact enumeration gives
Actions𝐿Pooled discovery Actions𝐿Pooled discovery
1 0.383469 5 0.735604
2 0.527532 6 0.794435
3 0.604528 7 0.836010
4 0.670581 8 0.859421
The smallest coordinated budget that matches private clue-following is therefore
𝐿∗=7, 𝐺 portfolio(7)=0.836010>0.832228=𝐺 private.
A second measure is the expected number of distinct actions. Private clue-following generates
𝐷private=

1−(1−𝑝) 𝑁 +(𝑀−1)  1−(1−𝑞) 𝑁 =6.156850.(5)
Consensusgeneratesexactlyonedistinctaction;theplannergenerateseight. Thesecountsmakethemechanism
visible: pooling improves the ranking, while the protocol determines how much of the nominal action budget
survives as coverage.
5

3 Information value and protocol loss
Let the target be𝜃∈Ω with prior𝜇. A decision architecture observes an information sigma-fieldF. A
protocolΠ maps its information into an action profile(𝐴 1,...,𝐴 𝐿), where repeated actions are allowed. Let
𝑆Π ={𝐴 1,...,𝐴 𝐿}be the set of distinct searched states. Discovery is
𝐺𝐿(Π)=P(𝜃∈𝑆 Π).
For informationFand budget𝐿, define the attainable frontier
𝑉𝐿(F)=E

max
𝑆⊆Ω,|𝑆|≤𝐿
P(𝜃∈𝑆|F)

.(6)
Inanatomicstatespace,themaximizingsetcontainsthe 𝐿 largestposteriorprobabilities. Defineprotocolloss
L𝐿(Π;F)=𝑉 𝐿(F)−𝐺 𝐿(Π).(7)
Thus
𝐺𝐿(Π)=𝑉 𝐿(F)−L 𝐿(Π;F).
This accounting identity separates the quality of available information from the efficiency with which an
institution converts information and action capacity into coverage.
Proposition 1(Value of information).IfF1⊆F 2, then𝑉1(F2)≥𝑉 1(F1).
Proof. Every one-action rule measurable with respect toF1 remains feasible underF2. The optimal rule
under the richer information cannot perform worse.□
Proposition 2(Fixed-budget optimality).For every realization ofF, the posterior top-𝐿 portfolio weakly
dominates every protocol using at most𝐿distinct actions and the same realized information. Consequently,
𝑉𝐿(F)≥𝐺 𝐿(Π).
Proof. The set generated byΠ is one feasible set in the maximization defining𝑉𝐿(F) . The posterior top-𝐿
set maximizes conditional target mass. Take expectations.□
In the canonical pooled-information regime,
𝑉8(F𝑆)=0.859421,L 8(Πconsensus;F 𝑆)=0.859421−0.383469=0.475952.
Conditional on the same pooled reports and the same nominal budget, the full gap between consensus and
the planner is protocol loss. The comparison with private clue-following changes both the information
architecture and the assignment authority, so it is a combined organizational benchmark rather than a unique
causal decomposition.
3.1 Independent symmetric signals
Let𝐶𝑏= ˝ 𝑖 1{𝑋𝑖 =𝑏}be the report count for box𝑏. Under the uniform prior,
P(𝜃=𝑏|𝐶)∝𝑝 𝐶𝑏𝑞𝑁−𝐶 𝑏 =𝑞 𝑁
𝑝
𝑞
𝐶𝑏
.(8)
6

Because𝑝 >𝑞, posterior rank equals count rank. Consensus is plurality; the optimal pooled portfolio is the
set of boxes with the largest counts, with randomization at cutoff ties.
Proposition 3(Private coverage dominates one-action consensus).In the symmetric independent atomic
model,
𝐺consensus≤𝐺 private=1−(1−𝑝) 𝑁.
Proof. The plurality winner has at least one report. Therefore the event that consensus selects the target is a
subset of the event that at least one private report names the target.□
The inequality holds throughout the model, but the strict Shared Discovery Paradox additionally requires
the pooled one-action value to exceed𝑝. With two searchers and uniform tie-breaking, pooled plurality
accuracy is exactly𝑝, so𝑁=2is a coverage-compression boundary case rather than a strict paradox.
Remark1 (Partial conformity is monotonically harmful).A natural intermediate institution lets only𝑎 of
the 𝑁 searchers defer to the pooled recommendation while the remaining𝑁−𝑎 follow their own clues.
This dial only goes down. The plurality winner always carries at least one report, so it already belongs
to the privately proposed set; an adopter therefore adds nothing to coverage and merely deletes their own
proposal. Formally, for nested adopter sets the searched set satisfies𝑆𝑎⊆𝑆 𝑎−1 realization by realization, so
𝐺(𝑎) is weakly decreasing from𝐺(0)=𝐺 private to𝐺(𝑁)=𝐺 consensus; which searchers adopt is immaterial
by exchangeability. The decline is strict whenever the displaced clue is uniquely held, correct, and differs
from the realized winner, an event of positive probability at every step. Exact enumeration at the canonical
parameters gives
𝐺(𝑎)=0.8322,0.7913,0.7461,0.6967,0.6429,0.5848,0.5222,0.4551,0.3835(𝑎=0,1,...,8):
even the first adopter costs4.1 percentage points. Dispersion must be informed (private clues), priced (the
market of section 4), or assigned (the planner); it cannot be obtained by dosing conformity.
3.2 The proportional sparse-evidence limit
Thesixteen-boxenvironmentisdeliberatelysmall,soitisnaturaltoaskwhethertheorderingisasmall-number
artifact. Scale the environment proportionally: let the number of searchers grow with the number of boxes,
𝑁𝑀/𝑀→𝛼∈(0,1), and hold the clue likelihood ratio𝑟=𝑝 𝑀/𝑞𝑀 >1fixed, so that
𝑝𝑀 = 𝑟 𝑀−1+𝑟 , 𝑞 𝑀 = 1 𝑀−1+𝑟 .
The canonical benchmark corresponds to𝛼=1/2 and𝑟=3.75 . Fixing𝑟 is one natural invariant among
several—one could instead preserve mutual information—but it keeps the report-count occupancy problem
nondegenerate: the target receives an asymptoticallyPoisson(𝛼𝑟) number of reports, while a typical false box
receives approximatelyPoisson(𝛼).
Proposition4(Proportionalsparse-evidencelimit).Intheindependentsymmetricmodelwith 𝑁𝑀/𝑀→𝛼∈
(0,1) and fixed likelihood ratio𝑟 >1, consider the blind coordinated portfolio (𝑁𝑀 distinct boxes chosen
without clues), pooled one-action consensus, private clue-following, and the pooled top-𝑁𝑀 portfolio. As
𝑀→∞,
𝐺blind−→𝛼, 𝐺 consensus−→0, 𝐺 private−→1−𝑒 −𝛼𝑟, 𝐺 portfolio−→1−(1−𝛼)𝑒 −𝛼(𝑟−1) .
7

The anonymous symmetric equal-split market on the pooled posterior also converges:
𝐺sym market−→𝛼Λ,whereΛuniquely solves ∑︁
𝑗:𝜓 𝑗>Λ
𝑓𝑗ℎ−1Λ/𝜓𝑗  =𝛼,(9)
with 𝑓𝑗 =𝑒−𝛼𝛼𝑗/𝑗!,𝜓𝑗 =𝑟 𝑗𝑒−𝛼(𝑟−1) , andℎ(𝑥)=(1−𝑒 −𝑥)/𝑥 strictly decreasing fromℎ(0)=1 . Writing
𝑥𝑗 =ℎ −1(Λ/𝜓𝑗) on active count classes and𝑔𝑗 =𝑓 𝑗𝜓𝑗 =𝑒 −𝛼𝑟(𝛼𝑟) 𝑗/𝑗!, the equivalent tilted form is
𝐺sym market→ ˝ 𝑗𝑔𝑗 1−𝑒 −𝑥 𝑗 .
The proof is in section D. For the canonical scaling𝛼=1/2 ,𝑟=3.75 , the solution of equation (9) is
Λ=1.094021, and the complete limit ordering is
𝐺consensus→0< 𝐺 blind→0.50< 𝐺 sym market→0.547011< 𝐺 private→0.846645< 𝐺 portfolio→0.873580.
Because(1−𝛼)𝑒 𝛼 <1 on(0,1) , the portfolio limit strictly exceeds the private limit at every𝛼. The market’s
position strictly above consensus and weakly below the portfolio also holds at every(𝛼,𝑟) , since the finite
inequalitiespasstothelimit. Thepositionsoftheblindbenchmarkrelativetoprivatesearchandtothemarket,
by contrast, depend on(𝛼,𝑟), and the displayed ordering is a property of the canonical scaling.
The market limit is water-filling against a Poisson count profile: in the limit the equilibrium abandons
every box with fewer than two reports (canonically𝜓1 =0.948<Λ< 𝜓 2 =3.555 ) and spreads over the
high-count classes in which the target, whose own count isPoisson(𝛼𝑟), is hidden. The finite canonical value
0.599099 sitsabove itslimit 0.547011, andthe seededMonte Carlodiagnosticin theverificationscriptshows
a monotone decline through𝑀∈{16,64,256,1024} (0.5991, 0.5740, 0.5582, 0.5494): as the posterior
spreads over more comparably ranked boxes, symmetric mixing wastes more of its budget on collisions inside
the leading count classes.
Two readings of the canonical limit deserve note. First, information without assignment and assignment
without information deliver nearly the same discovery: the market reaches0.547 holding the full pooled
posterior but no coordination device, the blind portfolio reaches0.500 holding a coordination device but no
information, and only their combination reaches0.874. Second, the market–private gap at scale admits an
exact accounting. Since𝐺private→P Poisson(𝛼𝑟)≥1  and the canonical limit market abandons the zero-
and one-report classes,
𝐺private−𝐺 sym market −→𝑔 1+ ∑︁
𝑗≥2
𝑔𝑗𝑒−𝑥 𝑗 =0.287541+0.012094 :
essentiallytheentiregapistheprobabilitythatthetargetreceivesexactlyonereport. Thesingletondiscoveries
that private clue-followers keep for free are precisely what an anonymous market rationally abandons;
collisions inside the classes the market does cover cost only0.012.
Remark2(Abundant-evidenceregime).Theparadoxisasparse-evidencephenomenon. Hold 𝑝∈(0,1) fixed
with𝑁𝑀/𝑀→𝛼∈(0,1) ,sothatthelikelihoodratio 𝑟𝑀 =𝑝/𝑞 𝑀→∞ . Then𝐺consensus→1 ,andafortiori
every clue-using protocol converges to one: the paradox vanishes in levels, and distinctions among diversified
protocols persist only in convergence rates. The clean dial is𝜆𝑀 =𝑁 𝑀𝑝𝑀, the target’s expected report
count: proposition 4 is the bounded-𝜆 regime, while whenever𝜆𝑀/log𝑀→∞ the union bound in section D
gives consistency. The intermediate window𝜆𝑀≍log𝑀 is a multiple-comparisons threshold problem we
leave open. The benchmark is aimed accordingly: consensus institutions are adequate where evidence about
the leading candidate is abundant; the compression loss binds in sparse-evidence search—frontier science,
early-stage investing, novel-hypothesis generation—where the target’s support never separates from the noise.
8

The limit sharpens the finite benchmark in two ways. First, the paradox is not a small-number artifact:
consensus discovery vanishes while every diversified protocol retains a strictly positive limit. Second,
large-scale consensus fails through an additional channel. The target’s report count remains stochastically
bounded, but the maximum count among linearly many false boxes diverges, so the plurality winner is
eventually an extreme false positive: top-one selection loses a multiple-comparisons contest that the portfolio,
which retains every named box, never enters. The pooled ranking still contains substantial information;
converting it into one repeated action is what discards it. The portfolio formula is the asymptotic form of the
finite reallocation identity that reappears under copying in section 6: the planner’s entire limiting gain over
private search,𝑒−𝛼𝑟  1−(1−𝛼)𝑒 𝛼 , comes from redirecting duplicated capacity to unnamed states on the
event that every clue misses.
4 Selfish search and the price of coordination
The planner benchmark assumes authority to assign distinct actions. We now retain the common pooled
posterior but remove the assignment rule. Fix a posterior
𝜋=(𝜋 1,...,𝜋 𝑀),
∑︁
𝑏
𝜋𝑏=1.
There are𝑁 risk-neutral searchers. Each simultaneously chooses one box. If the jackpot is in box𝑏 and𝑘
searchers chose𝑏, each occupant receives1/𝑘; all other payoffs are zero. The unit prize is therefore split
equally among successful searchers.
4.1 Payoffs, potential, and total welfare
Suppose every other searcher uses the same mixed strategy𝑠=(𝑠 1,...,𝑠 𝑀). If a searcher chooses box𝑏, the
number of other occupants is𝐾∼Binomial(𝑁−1,𝑠 𝑏). The reciprocal-share identity is
E
 1
𝐾+1

=
𝑁−1∑︁
𝑗=0
𝑁−1
𝑗

𝑠𝑗 𝑏(1−𝑠 𝑏)𝑁−1−𝑗 1 𝑗+1 = 1−(1−𝑠 𝑏)𝑁 𝑁𝑠𝑏 .(10)
Define
𝜙(𝑠)= 1−(1−𝑠) 𝑁
𝑁𝑠 , 𝜙(0)=1.(11)
The expected payoff from choosing𝑏is
𝑢𝑏(𝑠)=𝜋 𝑏𝜙(𝑠𝑏).(12)
The function𝜙 is strictly decreasing from1to 1/𝑁. Posterior value attracts searchers; congestion dilutes the
prize.
For a pure action profile𝑎, let𝑛𝑏(𝑎) be the number of searchers on box𝑏, and let𝐻𝑘 = ˝𝑘 𝑗=1 1/𝑗 with
𝐻0=0.
Proposition 5(Potential and payout identity).The equal-split game is an exact potential game with potential
Φ(𝑎)=
𝑀∑︁
𝑏=1
𝜋𝑏𝐻𝑛𝑏(𝑎).(13)
9

At every realized action profile, total searcher payoff equals the discovery indicator. Conditional on𝜋,
expected total payoff therefore equals discovery probability.
Proof. If one player moves from a box with occupancy𝑘 to a box with occupancyℓ, the player’s payoff
changes by𝜋𝑐/(ℓ+1)−𝜋 𝑏/𝑘. The potential changes by exactly the same amount. For the payout identity,
when the target box is occupied, its occupants split a unit prize and total payoff is one; otherwise total payoff
is zero. □
PureNashequilibriaexistbythepotentialargument[Rosenthal,1973,MondererandShapley,1996]. They
need not be unique or symmetric. The benchmark below focuses on the anonymous symmetric equilibrium
selected when ex ante identical searchers use the same mixed rule. This selection is not a convenience:
efficient asymmetric equilibria require role labels, conventions, or sequencing—exactly the coordination
devices whose presence or absence the paper treats as the institutional variable. Anonymity is the absence of
coordination devices, so the anonymous equilibrium measures what dispersion prices alone can supply; the
planner and sole-rescue benchmarks then measure what restoring those devices adds.
4.2 The water-filling equilibrium
Order posterior masses as𝜋(1)≥𝜋 (2)≥··· . The endpoint𝜋(1)/𝑁 matters because it is the payoff when
everyone chooses the top box.
Proposition6(Anonymoussymmetricequilibrium).Thegamehasauniqueanonymoussymmetricequilibrium
strategy𝑠.
(i) If𝜋(1)/𝑁≥𝜋 (2), every searcher chooses the top box and the common payoff is𝜆=𝜋(1)/𝑁.
(ii) Otherwise there is a unique𝜆∈(𝜋(1)/𝑁,𝜋 (1))such that
𝑠𝑏=
(
𝜙−1(𝜆/𝜋𝑏), 𝜋 𝑏 >𝜆,
0, 𝜋 𝑏≤𝜆,
∑︁
𝑏
𝑠𝑏=1.(14)
Every box in the support yields expected payoff𝜆; every excluded box yields at most𝜆.
Proof. In a symmetric equilibrium, used boxes must yield the same payoff. Since𝜙 is continuous and
strictly decreasing, an active box with𝜋𝑏 >𝜆 has the unique probability in equation (14); a box with𝜋𝑏≤𝜆
cannot attain payoff𝜆 even when approached alone. In the non-pure case, the sum of implied probabilities
is continuous and strictly decreasing in𝜆, exceeds one at𝜋(1)/𝑁, and equals zero at𝜋(1). The pure-corner
condition is exactly the no-deviation condition from the top box to the second-best box.□
The rule is water-filling on the posterior. Searchers flood boxes above a common value threshold, but they
do not impose a top-𝑁 count cutoff and they still collide. This is the invisible hand’s partial substitute for
portfolio assignment.
Proposition 7(Welfare identity).At the anonymous symmetric equilibrium,
𝐺sym market= ∑︁
𝑏
𝜋𝑏

1−(1−𝑠 𝑏)𝑁 =𝑁𝜆.(15)
Moreover,𝐺 sym market≥max 𝑏𝜋𝑏, with strict inequality unless the equilibrium is pure.
10

Proof. For an active box,𝜋𝑏[1−(1−𝑠 𝑏)𝑁]=𝑁𝑠 𝑏𝜋𝑏𝜙(𝑠𝑏)=𝑁𝑠 𝑏𝜆. Summing and using˝ 𝑏𝑠𝑏=1 gives
𝑁𝜆. If𝑏∗ is a posterior mode, then
𝑁𝜆=𝜋 𝑏∗
1−(1−𝑠 𝑏∗)𝑁
𝑠𝑏∗
≥𝜋 𝑏∗,
because1−(1−𝑠) 𝑁≥𝑠. Equality requires𝑠𝑏∗ =1.□
Thus equal sharing fixes the most extreme consensus pathology posterior by posterior: congestion makes
repetition costly. But the game can still under-cover the posterior tail.
4.3 The exact price of anarchy
The planner assigns one searcher to each of the𝑁highest-posterior boxes, giving
𝐺opt=
min{𝑁,𝑀}∑︁
𝑏=1
𝜋(𝑏).
Following Koutsoupias and Papadimitriou [1999], definePoA=𝐺 opt/𝐺eq for the worst equilibrium. The
following sharp bound is a specialization of the uniform-sharing covering-game result in Gairing [2009]; a
direct proof is short enough to include.
Theorem 1(Exact mixed price of anarchy).For every posterior𝜋and every𝑁-searcher equal-split game,
PoA≤2− 1 𝑁.(16)
The bound applies to mixed Nash equilibria and is tight.
Proof. Let𝑂={𝑜 1,...,𝑜 𝑁} be an optimal set, assigning one optimal box𝑜𝑖 to each searcher𝑖 (ignore
zero-mass padding if𝑀 <𝑁). For any realized action profile𝑎, write𝑊(𝑎) for covered posterior mass. For
each𝑜 𝑖,
𝜋𝑜𝑖≤

1− 1 𝑁  𝜋𝑜𝑖 1{𝑜𝑖 is occupied in𝑎}+𝑢 𝑖(𝑜𝑖,𝑎−𝑖).(17)
If𝑜𝑖 is empty, deviating to it gives𝜋𝑜𝑖. If it is occupied, deviating gives at least𝜋𝑜𝑖/𝑁, which completes the
right-hand side. Summing equation (17) over𝑖gives
𝐺opt≤

1− 1 𝑁  𝑊(𝑎)+ ∑︁ 𝑖 𝑢𝑖(𝑜𝑖,𝑎−𝑖),
because the occupied optimal boxes contribute at most𝑊(𝑎) . At a mixed Nash equilibrium, each player’s
expected current payoff is at least the payoff from the fixed deviation to𝑜𝑖. Total expected current payoff
equalsE[𝑊(𝑎)]. Hence
𝐺opt≤

2− 1 𝑁  E[𝑊(𝑎)].
For tightness, let one “decoy” box have posterior mass1/2 and let𝑁 tail boxes each have mass1/(2𝑁) .
The profile in which all searchers choose the decoy is a Nash equilibrium: each receives1/(2𝑁) and is
indifferent to deviating to an empty tail box. Equilibrium discovery is1/2, while the planner covers the decoy
and𝑁−1tail boxes, giving1−1/(2𝑁). The ratio is2−1/𝑁.□
11

Table 1:Canonical protocol comparison:𝑀=16,𝑁=8,𝑝=0.20.
Protocol Information Allocation rule Quality𝑄Discovery𝐺E[distinct]
Consensus pooled repeat posterior mode 0.383469 0.383469 1.000
Symmetric market pooled equal-split water-filling 0.344136 0.599099 2.673
Private clues local follow own report 0.200000 0.832228 6.157
Planner portfolio pooled top eight, one each 0.107428 0.859421 8.000
𝑄 is the average standalone probability that a selected box contains the jackpot, as in equation (4). The symmetric-market row is
an equilibrium-selection benchmark, not a claim that every Nash equilibrium has the same value.
The theorem distinguishes two questions. A posterior may possess an efficient pure equilibrium and an
inefficient anonymous mixed equilibrium at the same time. The price of anarchy controls the worst strategic
outcome; the symmetric benchmark measures what happens under anonymous, uncoordinated mixing.
The proof is a smoothness argument in the sense of Roughgarden [2015]: inequality equation (17)
establishes that the game is(1,1−1/𝑁) -smooth, so the extension theorems for robust price-of-anarchy
bounds apply verbatim. The bound2−1/𝑁 therefore holds not only for mixed Nash equilibria but for all
coarse correlated equilibria and for the average play of any no-regret learning dynamics—agents need not
compute an equilibrium for the guarantee to bind.
Uniform posterior.If posterior mass is uniform on𝑇 boxes, the anonymous symmetric equilibrium is
𝑠𝑏=1/𝑇and
𝐺sym market=1−

1− 1 𝑇 𝑁 , 𝐺 opt= min{𝑁,𝑇} 𝑇 .(18)
When𝑇=𝑁,
𝐺opt
𝐺sym market = 1 1−(1−1/𝑁) 𝑁 −→ 𝑒 𝑒−1 ≈1.582.(19)
For𝑁=8 , the ratio is1.523482. An efficient pure equilibrium placing one searcher on each box also exists.
The𝑒/(𝑒−1) constant is therefore the collision cost of symmetric mixing, not a universal impossibility result.
4.4 The canonical four-protocol ordering
For every realized pooled posterior in the sixteen-box benchmark, we solve equation (14) and then average
over the exact distribution of report-count classes. The resulting anonymous market discovery is
𝐺sym market=0.59909925.(20)
Itgenerates 2.673494 distinctactionsinexpectation. Thecompletecanonicalcomparisonisshowninfigure2
and table 1.
12

Consensus Symmetric market Private clues Planner portfolio
0.0
0.2
0.4
0.6
0.8Discovery probability
blind coordinated portfolio = 8/16 = 0.50
0.383
E[D] = 1.00
0.599
E[D] = 2.67
0.832
E[D] = 6.16
0.859
E[D] = 8.00
Same search problem, different action protocols
Figure 2:Exact ex-ante discovery under four protocols in the independent sixteen-box benchmark. The labels inside
the bars report the expected number of distinct boxes searched. The dashed line marks the blind coordinated portfolio at
8/16=0.50 : informed consensus falls below a protocol that ignores the clues entirely. Equal sharing supplies partial
dispersion, but not enough to match natural coverage from independent private clues.
The table records an exact inversion:
𝑄consensus>𝑄 sym market>𝑄 private>𝑄 planner while𝐺 consensus<𝐺 sym market<𝐺 private<𝐺 planner.
Moving toward the group-optimal allocation requires assigning actions that are individually less likely to
be correct in isolation: the planner raises group discovery to0.8594 while reducing the average standalone
probability that an assigned box contains the jackpot to0.1074. Average quality should not be confused with
equilibriumpayoff. Byequation(15),thesymmetricmarketpayoffpersearcheris 𝜆=𝐺 sym market/𝑁=0.074887 .
The quality number says the market concentrates on individually attractive boxes; the payoff number says
crowding sharply dilutes the private return from doing so.
Congestion pricing cures unanimity but not concentration. Private clue-followers condition on different
signals and therefore obtain substantial natural coverage. Symmetric market participants condition on the
same posterior and rationally overweight its peak. The invisible hand disperses, but toward the wrong
distribution.
5 Reward the rescue, not the win
The equal-split rule rewards an agent for being on the jackpot box. The group values an agent for being on a
jackpot box that no one else covered. The difference is marginal contribution.
Consider thesole-rescue rule: if exactly one searcher chose the realized target, that searcher receives the
unit prize; if two or more chose the target, no one is paid. Conditional on posterior𝜋, a searcher choosing box
𝑏receives expected payoff𝜋𝑏 if alone on𝑏and zero otherwise.
13

Proposition 8(Pure-strategy implementation).Suppose 𝑀≥𝑁 and every posterior mass is positive. Under
the sole-rescue rule:
(i) the game is an exact potential game with potential equal to covered posterior mass;
(ii) every pure Nash equilibrium is collision-free; and
(iii) the occupied boxes in every pure Nash equilibrium are exactly an𝑁-box posterior-optimal portfolio.
Thus every pure Nash equilibrium attains𝐺opt.
Proof. If a player leaves a box, covered mass falls by𝜋𝑏 exactly when the player was its sole occupant. If the
player enters another box, covered mass rises by𝜋𝑐 exactly when that box was empty. The player’s payoff
change therefore equals the change in covered mass.
If a pure profile contains a collision, at least one box is empty because𝑀≥𝑁 . A colliding player earns
zero and can move to an empty positive-mass box for a strictly positive payoff, so no collision can persist. In a
collision-free profile, a player on box𝑏 earns𝜋𝑏. Moving to an occupied box yields zero; moving to an empty
box𝑐 yields𝜋𝑐. The profile is a Nash equilibrium if and only if every occupied box has posterior mass at
least as large as every empty box. Its occupied set is therefore a top-𝑁set.□
The result is full implementation in pure Nash equilibrium, not dominant-strategy implementation. A
searcher’s best action still depends on which boxes others occupy. Nor does the result eliminate all mixed-
equilibrium or equilibrium-selection concerns. A public role-assignment or sequential convention may still
be useful for selecting among efficient top-𝑁matchings.
The rule is weakly budget-balanced ex post: it never pays more than the unit prize. On the efficient
equilibrium path it pays the full prize exactly when discovery occurs. Off equilibrium it burns the prize on a
duplicateddiscovery. Inricherapplications, attribution, sidepayments, riskaversion, andcollusionmaymake
literal sole-rescue contracting difficult. The benchmark point is narrower: compensating unique coverage
aligns the potential with the organization’s discovery objective, whereas equal sharing aligns total payout with
discovery but not the allocation of effort.
6 Common-source dependence
Real searchers rarely receive conditionally independent signals. They read the same reports, use the same
models, attend the same meetings, and inherit the same narratives. We introduce one latent common source
to make this dependence explicit.
6.1 Copying and channel collapse
Let𝑋0 be a common cue with the same accuracy law as a private clue. Each searcher independently copies
𝑋0 with probability𝑐and otherwise draws an independent clue:
𝑋𝑖 =
(
𝑋0,with probability𝑐,
e𝑋𝑖,with probability1−𝑐.
14

The copying probability𝑐 is a scalar parameter—distinct from the report-count vector𝐶=(𝐶 1,...,𝐶 𝑀) of
section 3.1—and it is not the pairwise correlation coefficient. For correctness indicators𝑌𝑖 =1{𝑋 𝑖 =𝜃},
Corr(𝑌𝑖,𝑌𝑗|𝜃)=𝑐 2.
Let𝐾∼Binomial(𝑁,𝑐) be the number of copiers. Conditional on𝐾, the copiers contribute one common
discovery channel if𝐾≥1, while the𝑁−𝐾noncopiers contribute independent channels.
Proposition 9(Channel collapse).The effective channel count is
𝑁eff =𝑁−𝐾+1{𝐾≥1}.(21)
Private report-following discovery is
𝐺private(𝑐)=1−𝑝

(1−𝑐)(1−𝑝)
𝑁
−(1−𝑝)

1−𝑝(1−𝑐)
𝑁
.(22)
Proof. If at least one searcher copies, private search misses only if the common cue misses and every
noncopier’s independent clue misses. If no searcher copies, all𝑁 independent clues must miss. Averaging
over𝐾and collecting terms yields equation (22).□
At𝑐=0 , equation (22) is1−(1−𝑝) 𝑁. At𝑐=1 , it is𝑝: eight nominal searchers have become one
effective clue. In the canonical model, expected distinct proposals fall from6.157 at 𝑐=0 to 1.362 at
𝑐=0.95.
6.2 Agreement need not mean posterior rank
Under independence, report count is a sufficient ranking statistic. Under copying, a large count can be
generated by one incorrect source repeated many times. Exact marginalization over the latent cue and copier
count can reverse the ranking.
At𝑐=0.4 ,considercounts (6,2,0,...,0) . Let𝑎 bethesix-countboxand 𝑏 thetwo-countbox. Theexact
count likelihoods are
P(𝐶|𝜃=𝑎)=1.1427×10 −4,P(𝐶|𝜃=𝑏)=1.3977×10 −4.
With a uniform prior, the two-count box has the larger posterior. This does not claim that count ranking
generally fails dramatically; it establishes that dependence-aware ranking is conceptually distinct from raw
agreement. In the canonical calculations, the Bayes-versus-count discovery discount is concentrated at one-
and two-action budgets and vanishes for𝐿≥3on the tested grid.
6.3 The centralized planner gain
Let 𝐷 be the number of distinct privately proposed boxes and let𝑉𝑁(𝑐) be the Bayes-optimal𝑁-action
portfolio value after observing reports generated at copying probability𝑐. Define the equal-budget planner
gain
Δplanner(𝑐)=𝑉 𝑁(𝑐)−𝐺 private(𝑐).(23)
Theorem 2(Monotone planner gain).In the atomic𝑀-state model with2≤𝑁≤𝑀 and 𝑝 >1/𝑀, the
15

0.0 0.2 0.4 0.6 0.8
Common-cue copying probability c
0.00
0.05
0.10
0.15
0.20
0.25
0.30
0.35Planner gain over private search
Duplicated capacity becomes more valuable to reallocate
Figure 3:Exact canonical planner gain𝑉8(𝑐)−𝐺 private(𝑐). As common-source copying creates more duplicated
capacity, identifying and reallocating it becomes more valuable.
planner gainΔplanner(𝑐)is strictly increasing for𝑐∈(0,1). At full copying,
Δplanner(1)=(𝑁−1)𝑞.(24)
The proof is in section C. Its key identity is
Δplanner(𝑐)=E

1{private search misses}𝑁−𝐷 𝑀−𝐷  .(25)
All named boxes precede unnamed boxes in the posterior ranking, so the planner preserves every distinct
proposal and fills unused slots with otherwise unsearched states. Conditional on a miss, unnamed states are
symmetric. Increasing the number of copiers weakly shrinks𝐷 and can convert a success into a miss; both
changes raise the value of the planner’s fill slots. The binomial copier count shifts upward with𝑐.
For the canonical parameters, the gain rises from0.027193 at𝑐=0 to 0.335927 at𝑐=0.95 , with limit
0.373333. Therecoverybudgetfallsfromsevencoordinatedactionsat 𝑐=0 totwoat 𝑐=0.95 . Thetheorem
concerns a frictionless centralized benchmark: it combines pooled observation with assignment authority and
therefore upper-bounds what a decentralized institution may realize.
6.4 Selfish search under copying
Now let searchers pool their reports, form the herd-aware posterior by marginalizing over the latent cue
and copier count, and play the equal-split game on that posterior. For each report-count class, we solve the
anonymous equilibrium and average conditional discovery over its exact probability.
At low copying, private report-following wins because different reports supply natural coverage. As
copying rises, that advantage collapses. The market continues to disperse over the support of the common
16

Table 2:Canonical outcomes under common-cue copying.
𝑐Consensus Symmetric market Private reports Planner
0.00 0.383 0.599 0.832 0.859
0.50 0.271 0.552 0.655 0.768
0.70 0.240 0.477 0.512 0.702
0.80 0.221 0.428 0.423 0.664
0.90 0.206 0.388 0.319 0.621
0.95 0.202 0.380 0.262 0.598
posterior and therefore degrades more slowly. High-precision enumeration gives the canonical crossover
𝑐∗=0.7884616565, 𝐺 sym market(𝑐∗)=𝐺 private(𝑐∗)=0.4338934643.(26)
Atfullcopying,privatereport-followingandconsensusbothequal 𝑝=0.20 ,theplannerreaches 𝑝+(𝑁−1)𝑞=
0.573333, and the anonymous equal-split market reaches approximately0.382006.
The crossover is not knife-edge in the parameters. A comparative-statics scan over72 combinations—
𝑀∈{8,12,16,24,32} ,𝑁∈{4,6,8} ,𝑝∈{0.10,...,0.30} with𝑝 >1/𝑀, and𝑐 scanned in steps of0.02
up to0.98—finds that the market–private gap is negative at𝑐=0 in every combination and changes sign at
most once:52 combinations cross exactly once, at crossovers ranging from𝑐≈0.29 to𝑐≈0.98 , while in
the remaining20, concentrated at large𝑀, small𝑁, and strong signals, private report-following stays ahead
throughout the scanned range. On this grid the qualitative pattern is uniform—natural coverage first, forced
dispersion after enough channel collapse—though single crossing remains a computational pattern rather
than a theorem.
The institutional implication is conditional. When information sources are genuinely independent,
decentralized local action can dominate a common-posterior market. When sources are highly correlated,
some mechanism that forces dispersion can outperform nominal decentralization. Correlation raises the value
not only of a perfect planner but also of imperfect coordination.
17

0.0 0.2 0.4 0.6 0.8
Common-cue copying probability c
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9Discovery probability
 market/private crossover
c * = 0.788
Correlation changes which decentralized protocol performs better
Consensus
Symmetric equal-split market
Private report-following
Bayes-optimal portfolio
Figure 4:Exact canonical comparison under common-source copying. The symmetric equal-split market initially trails
decentralized report-following, then overtakes it when channel collapse becomes sufficiently severe. The crossover is a
canonical computational result, not a general theorem.
7 Why this is a benchmark
A useful benchmark is not a universal law. It is a small model that isolates a mechanism, supplies stable
vocabulary,andproducesquantitiesthatrichermodelscanpreserveoroverturn. Thesixteen-boxenvironment
is designed for that role.
The benchmark separates four mechanisms that richer environments often confound:
1.Information improvement.Pooling raises the quality of the posterior ranking.
2.Action compression.A one-answer protocol makes nominally separate actions perfectly correlated.
3. Action synthesis.A coordinator can redirect duplicated capacity to candidates no private clue proposed.
4. Channel merging.Shared sources reduce effective diversity before any explicit consensus rule is applied.
7.1 Formal lineage
Teamtheoryandoptimalsearch.Thecommon-objectivemodelisateamprobleminthesenseofMarschak
and Radner [1972]: agents possess dispersed information and choose a joint action profile. Blackwell’s
comparison of experiments underlies the value-of-information result [Blackwell, 1953]. The operational
parent is optimal search: Koopman [1957] studies how finite search effort should be allocated over uncertain
target locations. The atomic model is a discrete, all-or-nothing corner in which the posterior top-𝐿 rule is
exact.
18

Table 3:The benchmark dictionary.
Object Interpretation
One-action value𝑉1(F)How accurately the information architecture identifies its best single target.
Portfolio frontier𝑉𝐿(F)The discovery attainable from𝐿actions under the same posterior.
Protocol lossL𝐿 Attainable posterior mass destroyed by the action rule.
Recovery budget𝐿∗ Smallest coordinated budget that replaces decentralized search.
Effective channels Number of independent chances encoded by nominal reports.
Symmetric market value Dispersion supplied by equal sharing without role assignment.
Price of anarchy Worst equilibrium loss relative to the top-𝑁portfolio.
Sole-rescue
implementation
Alignment obtained by rewarding unique coverage.
Correlation crossover𝑐∗ Point at which forced dispersion overtakes natural private coverage.
ParallelR&Dandorganizationallearning.Parallelprojectshedgeuncertaintyininnovation[Nelson,1961].
Organizational-learning and division-of-cognitive-labor models show how imitation and communication
can reduce exploration [March, 1991, Kitcher, 1990]. Network epistemology makes the same tension
endogenoustocommunicationstructure[Zollman,2007,Mayo-Wilsonetal.,2011]. Inthepresentaccounting,
limited communication is a second-best instrument: sparse networks preserve diversity only by withholding
information value, whereas the planner and rescue benchmarks keep the shared posterior intact and repair the
action allocation directly, separating the two effects that communication limits bundle. Duede and Evans
[2024] independently describe the belief-side half of this trade-off—collaboration inflates collective certainty
while the likelihood of genuine replication falls—which is the accuracy–coverage reversal stated in belief
space rather than action space. Rzhetsky et al. [2015] study a much richer dynamic problem of experiment
choiceonanevolvingscientificnetwork. Thepresentbenchmarkstripsawaydynamicsandcareerstoexposea
finite-action accounting identity: a community can improve its shared ranking and still waste its experimental
portfolio.
Herding and correlated judgment.Information-cascade models explain how rational observation can
generate convergent beliefs or actions [Banerjee, 1992, Bikhchandani et al., 1992, Smith and Sørensen, 2000].
Correlated-jury work shows that dependence weakens voting aggregation [Ladha, 1992]. Our copying model
does not claim the first failure of raw agreement. It places dependence inside a multi-alternative discovery
problem and measures three distinct consequences: channel collapse, posterior-versus-count ranking loss,
and the value of reallocating duplicated actions.
Congestion, covering, and potential games.The equal-split extension is a singleton congestion game with
a harmonic potential [Rosenthal, 1973, Monderer and Shapley, 1996]. Its welfare is a coverage function,
linking it to valid-utility and covering games [Vetta, 2002, Gairing, 2009]. This lineage is important for
claim calibration: the exact2−1/𝑁 bound is not presented as a new general result in algorithmic game
theory. What is new in the benchmark is the way the covering game is generated endogenously by a Bayesian
posterior and compared ex ante with private signals, consensus, a planner, and common-source copying. A
complementary line studies how information itself interacts with congestion: Acemoglu et al. [2018] show
that giving drivers additional route information can raise equilibrium travel times—an informational Braess’
paradox—and characterize the network class immune to it, with a subsequent information-design literature
choosing what to disclose [Das et al., 2017]. The mechanism is instructively different. There, information
19

expands strategy sets in a delay-minimization routing game and harms through re-routing externalities in
equilibrium; here, the information architecture is held fixed, richer information weakly raises the attainable
frontier (the argument of proposition 1 applies at every budget), and the loss arises entirely from the protocol
that converts the posterior into actions. Whether a sharper shared posterior can lower equilibrium coverage
through the water-filling pure corner—an informational Braess’ paradox in discovery rather than delay—is a
disclosure-stage question we leave open.
Submodular extensions.With one atomic target, the value of a set of distinct boxes is modular. If actions
cover overlapping state sets, the objective becomes monotone submodular; if actions reveal information
sequentially, adaptive submodularity becomes relevant [Nemhauser et al., 1978, Golovin and Krause, 2011].
The exact top-𝐿 portfolio would then be replaced by approximation guarantees, but protocol loss and recovery
budgets would remain well-defined.
8 Organizational implications
Research and development.A firm may combine analyst reports, technical reviews, and shared models to
improve its ranking of projects, then route too much laboratory capacity toward the same leading candidate.
Thebenchmarksuggeststreatinginformationaggregationandprojectassignmentasseparatedesignproblems.
A portfolio manager, explicit capacity reservation for minority hypotheses, or marginal-contribution credit
can preserve the value of shared information without preserving disagreement for its own sake.
Venture capital and innovation portfolios.Shared diligence can improve judgment about the modal
opportunity while concentrating capital and sourcing effort in the same companies or categories. The model
is not a literal theory of venture returns: it omits prices, ownership, multiple winners, heavy tails, and
endogenous entry. It does yield a testable comparative static. As sourcing and diligence become more
correlated, the marginal value of portfolio-level differentiation should rise.
Science.Open communication can improve beliefs about promising hypotheses while narrowing the set
of experiments performed. Restricting communication can preserve diversity, but only by withholding
information. The planner and sole-rescue benchmarks point to a different design: preserve the shared
posterior and diversify the actions. Provenance data could help distinguish many nominal reports from many
independent channels.
Multi-agent artificial intelligence.Agents connected to the same model, memory, retrieval context, or
evaluation rubric may produce individually stronger but highly correlated recommendations. Multi-agent
systems should therefore distinguish ensemble size from effective channel count. Posterior sampling, explicit
role differentiation, diverse retrieval sources, and marginal-coverage rewards are natural analogues of the
benchmark’sportfoliomechanisms. Thesmoothnessformoftheorem1isdirectlyrelevanthere: ensemblesof
adaptiveagentsrunninganyregret-minimizingupdateinheritthe 2−1/𝑁 coverageguaranteeunderequal-split
credit,withoutevercomputinganequilibrium. Theblind-sentinelnegativeresultisequallyactionable: adding
uninformed explorer agents to an informed ensemble is dominated in the canonical environment, so useful
diversity must be signal-contingent—sampled from the posterior or assigned to distinct evidence—rather than
signal-free.
20

The empirical program is straightforward in principle. Estimate posterior or score distributions, measure
repeated-action patterns and source overlap, compare observed coverage with the top-𝐿 frontier, and report
protocol loss and the recovery budget. The copying parameter is a model, not an observable primitive, but
source provenance and correlated failure data can discipline it. So can duplication itself: the expected number
ofdistinctproposalsisstrictlydecreasingin 𝑐 onthecomputedgrid(from 6.157 at𝑐=0 to 1.362 at𝑐=0.95
in the canonical environment), so matching an observed duplication level to the benchmark’s exact curve pins
down a latent copying rate, which in turn implies a recovery budget and a planner gain. This is the sense in
which the benchmark’s quantities serve as reference points for richer models: comparison and inversion, not
structural estimation.
9 Limitations and extensions
The benchmark is intentionally narrow. Exactly one atomic state is valuable; each action tests one state;
actions are simultaneous and costless; private clues are ex ante symmetric; the planner can observe and assign
reports; equal-split players share a common posterior; and dependence is generated by one latent cue whose
provenance is hidden. These assumptions make both inference and assignment unusually clean.
Several qualifications matter for interpretation. First, the canonical market value uses the anonymous
symmetric equilibrium. Equal-split games can also have efficient asymmetric pure equilibria, so role
labels, conventions, or sequential play may materially change outcomes. Second, sole-rescue gives full
pure-equilibrium implementation but not dominant strategies or a guarantee for every mixed equilibrium.
Third,themonotoneplanner-gaintheoremisexactforthestatedcopyingprocess;themarket/privatecrossover
is a canonical computational result. Fourth, the planner benchmark changes both information access and
decision rights relative to decentralized clue-following.
One intermediate cell deserves explicit mention. A decentralized-team benchmark would allow the agents
to commit ex ante to role-dependent policies𝑓1,..., 𝑓 𝑁 while retaining private, noncommunicated clues,
with team valuemax𝑓1,...,𝑓 𝑁 P𝜃∈{𝑓 1(𝑋 1),..., 𝑓 𝑁(𝑋𝑁)}. Characterizing that private-information team
optimum would separate assignment authority from information pooling, which the planner benchmark
changes jointly. We leave it open rather than insert a hand-selected policy: the simple hybrid that replaces
clue-followers with blind sentinels is maximized at zero sentinels in the canonical environment, so the
interesting policies are signal-contingent.
Natural extensions include heterogeneous searchers, multiple common sources or cliques, endogenous
informationacquisition,multipletargets,costlyorcapacity-constrainedactions,heavy-tailedprizes,sequential
experimentation, overlapping coverage, collusion under rescue rewards, and mechanism design when the
posterior itself is privately held. In these environments the numerical yardsticks may change, but the
benchmark’s separation between information, allocation, incentives, and dependence remains available.
10 Conclusion
Collective discovery is not collective estimation with more participants. Estimation asks for one answer.
Discovery allocates a portfolio of attempts.
Thesixteen-boxbenchmarkmakesthedistinctionexact. Poolingeightimperfectcluesraisesthebestsingle
recommendation from20.0% to 38.35%. Repeating that recommendation lowers discovery from83.22% to
38.35%. A planner using the same pooled reports reaches85.94%, and seven coordinated actions recover
the private benchmark. Equal sharing supplies partial dispersion and raises discovery to59.91%, but its
21

worst equilibrium can lose a factor2−1/𝑁 . Rewarding unique rescue aligns every pure equilibrium with the
first-best portfolio. Common-source copying collapses natural coverage, increases the value of reallocation,
and eventually makes even an imperfect dispersing market outperform private report-following.
The central design lesson is therefore not “share less information.” It is: treat information sharing and
action allocation as distinct institutional choices. Share the evidence. Diversify the actions.
A Exact independent enumeration
By symmetry, condition on box1being the target. The report-count vector
𝐶=(𝐶 1,...,𝐶 𝑀)∼Multinomial(𝑁;𝑝,𝑞,...,𝑞).
For a count vector𝑥, let
𝑟(𝑥)=|{𝑏:𝑥 𝑏 >𝑥 1}|, 𝑡(𝑥)=|{𝑏:𝑥 𝑏=𝑥 1}|.
With uniform randomization at cutoff ties, the conditional probability that the true box belongs to a top-𝐿
count set is
𝜏𝐿(𝑥)=
 

0, 𝑟(𝑥)≥𝐿,
1, 𝑟(𝑥)+𝑡(𝑥)≤𝐿,
𝐿−𝑟(𝑥)
𝑡(𝑥) , 𝑟(𝑥)< 𝐿 <𝑟(𝑥)+𝑡(𝑥).
(27)
Hence the exact pooled frontier is
𝐺𝑀,𝑁,𝐿(𝑝)=
∑︁
𝑥1+···+𝑥 𝑀=𝑁
𝑁!
˛𝑀
𝑏=1𝑥𝑏!
𝑝𝑥1𝑞𝑁−𝑥 1𝜏𝐿(𝑥).(28)
For𝑀=16and𝑁=8, the sum contains
𝑁+𝑀−1
𝑀−1

=
23
15

=490,314
count vectors. Grouping by permutations of the fifteen non-target boxes reduces both the independent and
common-cue calculations to67count classes.
At𝐿=7, the difference between the pooled portfolio and private clue-following can be decomposed as
P(𝜃∈𝑆 ∗ 7\𝑆 private)−P(𝜃∈𝑆 private\𝑆∗ 7).
Exact enumeration gives a synthesis gain of0.011744 and a compression loss of0.007962. At𝐿=8 , no box
named by a private clue is discarded; the improvement0.027193 comes entirely from reallocating duplicated
capacity.
22

B Common-cue likelihood and Bayes ranking
For a candidate target𝑡, define the report probability vector
𝜌(𝑡) 𝑟 =
(
𝑝, 𝑟=𝑡,
𝑞, 𝑟≠𝑡.
Let𝑧be the common cue and𝑘the copier count. For observed counts𝑥,
P(𝐶=𝑥|𝜃=𝑡,𝑋 0=𝑧,𝐾=𝑘)(29)
=1{𝑥 𝑧≥𝑘} (𝑁−𝑘)! (𝑥𝑧−𝑘)! ˛ 𝑟≠𝑧 𝑥𝑟! 𝑀Ö 𝑟=1  𝜌(𝑡) 𝑟 𝑥𝑟−𝑘1{𝑟=𝑧} .(30)
Marginalizing gives
P(𝐶=𝑥|𝜃=𝑡,𝑐)=
𝑀∑︁
𝑧=1
𝜌(𝑡) 𝑧
𝑁∑︁
𝑘=0
𝑁
𝑘

𝑐𝑘(1−𝑐) 𝑁−𝑘 P(𝐶=𝑥|𝜃=𝑡,𝑋 0=𝑧,𝐾=𝑘).(31)
With a uniform prior, normalize these𝑀 likelihoods to obtain the herd-aware posterior. The verification
script precomputes the coefficient of every basis term𝑐𝑘(1−𝑐) 𝑁−𝑘 for each count class and candidate target.
C Proof of the monotone planner-gain theorem
We give the omitted details for equation (25) and monotonicity.
Lemma 1(Named states precede unnamed states).For every realizable report vector under the common-cue
model, every state with a positive report count has posterior probability at least as large as every state with
zero reports.
Proof. Fix a named state𝑏 and an unnamed state𝑑. Compare the mixture likelihood under hypotheses𝜃=𝑏
and𝜃=𝑑 term by term in equation (31). If the common cue is neither𝑏 nor𝑑, the cue prefactor is identical
while the residual multinomial likelihood differs by a nonnegative power of𝑝/𝑞 in favor of𝑏. If the cue is𝑏,
its prefactor is𝑝 under𝜃=𝑏 and𝑞 under𝜃=𝑑 , and the residual likelihood contributes another nonnegative
power of𝑝/𝑞. If the cue is𝑑, feasibility requires𝑘=0 because𝑑 is unnamed; the combined likelihood ratio
is(𝑝/𝑞) 𝑥𝑏−1≥1 . Every matched nonzero term weakly favors the named state. Summing over cues and
copier counts preserves the inequality.□
Theoptimal 𝑁-actionportfoliothereforeincludesall 𝐷 distinctnamedstatesandfills 𝑁−𝐷 positionswith
unnamed states. On the event that private report-following misses, the target lies among the𝑀−𝐷 unnamed
states. Symmetry assigns equal conditional posterior mass to those states, so the planner’s conditional rescue
probability is(𝑁−𝐷)/(𝑀−𝐷). This proves equation (25).
Condition on copier count𝐾=𝑘 . Given𝑘, the joint law of the common cue and the𝑁−𝑘 independent
clues does not otherwise depend on𝑐. Define
ℎ(𝑘)=E

1{miss} 𝑁−𝐷 𝑀−𝐷

𝐾=𝑘  .
23

ThenΔ planner(𝑐)=E[ℎ(𝐾)]for𝐾∼Binomial(𝑁,𝑐). We haveℎ(0)=ℎ(1)because one copy of𝑋 0 has the
same joint distribution as one independent clue. For𝑘≥1 , couple the𝑘-copier system and the(𝑘+1) -copier
system by converting one independent searcher into an additional copier while holding the common cue and
all other reports fixed. Because the common cue is already represented, the conversion can only weakly
reduce𝐷. It can only weakly increase the miss indicator. The fraction(𝑁−𝐷)/(𝑀−𝐷) is nondecreasing
as𝐷 falls when𝑁≤𝑀 . Thusℎ(𝑘+1)≥ℎ(𝑘) . The inequality is strict for at least one𝑘: with positive
probability, the converted independent clue is the only report naming the target while the common cue and all
remaining clues miss.
If𝐾′∼Binomial(𝑁−1,𝑐), the standard binomial derivative identity yields
𝑑
𝑑𝑐 E[ℎ(𝐾)]=𝑁E[ℎ(𝐾 ′+1)−ℎ(𝐾 ′)]>0(𝑐∈(0,1)).
The hypothesis𝑁≥2 is necessary: with a single searcher the named box is the posterior mode, the planner
replicates private search, the gain is identically zero, and the derivative vanishes throughout(0,1) because
ℎ(0)=ℎ(1) . At𝑐=1 , one box is named. The planner adds𝑁−1 of the𝑀−1 unnamed boxes, each with
posterior mass𝑞, while private search covers only the named box. HenceΔplanner(1)=(𝑁−1)𝑞.
D Proof of the proportional sparse-evidence limit
Throughout,𝑁=𝑁 𝑀 with𝑁𝑀/𝑀→𝛼∈(0,1) , and𝑝𝑀 =𝑟/(𝑀−1+𝑟) ,𝑞𝑀 =1/(𝑀−1+𝑟) for fixed
𝑟 >1, so that𝑁𝑀𝑝𝑀→𝛼𝑟 and𝑁𝑀𝑞𝑀→𝛼 : the target receives an asymptoticallyPoisson(𝛼𝑟) number of
reports, while each false box receives approximatelyPoisson(𝛼). All limits are as𝑀→∞ and all clues are
independent.
Blind portfolio.The coordinator selects𝑁𝑀 distinct boxes without observing clues. Under the uniform
prior,𝐺 blind=𝑁 𝑀/𝑀→𝛼.
Privateclue-following.Byequation(1), 𝐺private=1−(1−𝑝 𝑀)𝑁𝑀,and 𝑁𝑀 log(1−𝑝 𝑀)=−𝑁 𝑀𝑝𝑀 1+
𝑂(𝑝 𝑀)→−𝛼𝑟, so𝐺 private→1−𝑒 −𝛼𝑟.
Consensus.Condition on 𝜃. The target count𝐶𝜃∼Binomial(𝑁 𝑀,𝑝 𝑀) converges in distribution to
Poisson(𝛼𝑟) and is therefore bounded in probability. Conditional on the number of off-target reports
𝐹=𝑁 𝑀−𝐶𝜃, the false counts are multinomial with𝐹 trials over𝑀−1 equally likely boxes, and𝐹/𝑀→𝛼
in probability. Fix an integer𝑗 and let𝑊𝑗 =|{𝑏≠𝜃:𝐶 𝑏≥𝑗}| . Standard occupancy asymptotics give
E[𝑊𝑗]/𝑀→P(Poisson(𝛼)≥𝑗)>0 , and the variance of𝑊𝑗 is𝑂(𝑀) because the occupancy indicators
are negatively correlated, so𝑊𝑗→∞ in probability. Hencemax𝑏≠𝜃 𝐶𝑏≥𝑗 with probability tending to one
for every fixed𝑗: the largest false count diverges in probability while𝐶𝜃 remains tight. Consensus success
requires𝐶𝜃≥max 𝑏≠𝜃 𝐶𝑏 (aneventwhoseprobabilitytendstozero), so 𝐺consensus→0 ; uniformtie-breaking
only lowers the success probability further.
Portfolio.By equation (8), every named box has strictly larger posterior mass than every unnamed box,
and at most𝑁𝑀 boxes are named, so the top-𝑁𝑀 rule retains every named box and fills its remaining slots
uniformly at random among the posterior-tied unnamed boxes. Let𝐷 be the number of distinct named
boxes. On{𝐶𝜃≥1} the portfolio contains𝜃. On the miss event{𝐶𝜃 =0} , the target is one of the𝑀−𝐷
unnamed boxes, which carry equal conditional posterior mass, so the conditional rescue probability is
(𝑁𝑀−𝐷)/(𝑀−𝐷). This is the𝑐=0case of equation (25):
𝐺portfolio=𝐺 private+E

1{𝐶𝜃 =0} 𝑁𝑀−𝐷 𝑀−𝐷  .
24

Conditional on the miss event,𝐷 is the number of occupied boxes when𝑁𝑀 balls are placed uniformly over
𝑀−1 boxes. Occupancy concentration (E[𝐷]=(𝑀−1)[1−(1− 1 𝑀−1)𝑁𝑀] with variance𝑂(𝑀) ) gives
𝐷/𝑀→1−𝑒 −𝛼 in probability, hence
𝑁𝑀−𝐷
𝑀−𝐷 −→𝜏 𝛼= 𝛼−(1−𝑒 −𝛼) 𝑒−𝛼 =1−(1−𝛼)𝑒 𝛼 in probability,
where𝜏𝛼∈(0,1) because𝑒−𝛼 >1−𝛼 for𝛼 >0: duplicated reports leave free slots asymptotically. The
ratio is bounded by one, so bounded convergence together withP(𝐶𝜃 =0)→𝑒 −𝛼𝑟 yields
𝐺portfolio−→ 1−𝑒 −𝛼𝑟 +𝑒−𝛼𝑟  1−(1−𝛼)𝑒 𝛼 =1−(1−𝛼)𝑒 −𝛼(𝑟−1) .
Finally,(1−𝛼)𝑒 𝛼 is strictly decreasing on(0,1) from the value one at𝛼=0 , so(1−𝛼)𝑒 𝛼 <1 and the
portfolio limit strictly exceeds the private limit for every𝛼∈(0,1).□
Symmetric equal-split market.Write the scaled posterior weight of box𝑏 as𝑊𝑏=𝑀𝜋 𝑏=𝑟 𝐶𝑏/(𝑍𝑀/𝑀)
with 𝑍𝑀 = ˝ 𝑏𝑟𝐶𝑏, and recall from proposition 4 the notation𝑓𝑗 =𝑒 −𝛼𝛼𝑗/𝑗!, 𝜓𝑗 =𝑟 𝑗𝑒−𝛼(𝑟−1) , 𝑔𝑗 =
𝑓𝑗𝜓𝑗 =𝑒−𝛼𝑟(𝛼𝑟) 𝑗/𝑗!, andℎ(𝑥)=(1−𝑒 −𝑥)/𝑥.
Step1: weightedoccupancylawoflargenumbers.Forafalsebox, E

𝑟𝐶𝑏

= 1+(𝑟−1)𝑞 𝑀 𝑁𝑀→𝑒 𝛼(𝑟−1)
and E

𝑟2𝐶𝑏

= 1+(𝑟 2−1)𝑞 𝑀 𝑁𝑀→𝑒 𝛼(𝑟 2−1) <∞ . For two false boxes𝑎≠𝑏 , each clue lands on at
most one of them, soE

𝑟𝐶𝑎𝑟𝐶𝑏

= 1+2(𝑟−1)𝑞 𝑀 𝑁𝑀, and a direct expansion shows the covariance is
𝑂(1/𝑀) times a bounded factor. Chebyshev’s inequality then gives𝑍𝑀/𝑀→𝑒 𝛼(𝑟−1) in probability, so
𝑊𝑏→𝜓 𝑗 in probability for a box with𝐶𝑏=𝑗 ; the same second moments give, for the truncated weighted
sums,𝑀−1 ˝ 𝑏𝑟𝐶𝑏 1{𝐶𝑏≥𝐽}→𝑒 𝛼(𝑟−1) ˝ 𝑗≥𝐽 𝑔𝑗 in probability, with the tail uniformly small in𝐽 because˝
𝑗𝑔𝑗 =1(the identity𝑓 𝑗𝜓𝑗 =𝑔 𝑗 is the exponential tilting of a Poisson law).
Step2: convergenceofthebudgetequation.Atthefiniteanonymousequilibriumofproposition6,anactive
box satisfies𝑊𝑏𝜙(𝑠𝑏)= Λ𝑀 :=𝑀𝜆 𝑀, and the budget constraint˝ 𝑏𝑠𝑏 =1 reads 𝑀−1 ˝ 𝑏𝑥𝑏 =𝑁 𝑀/𝑀
with𝑥𝑏 =𝑁 𝑀𝑠𝑏. Since(1−𝑥/𝑁) 𝑁→𝑒 −𝑥 uniformly on compact𝑥-sets,𝜙(𝑥/𝑁)→ℎ(𝑥) uniformly on
compacts, withℎcontinuous and strictly decreasing fromℎ(0)=1. Define the limit budget function
𝐵(Λ)=
∑︁
𝑗:𝜓 𝑗>Λ
𝑓𝑗ℎ−1Λ/𝜓𝑗 .
Because ℎ(𝑥)≤1/𝑥 , every active class obeys𝑥𝑗≤𝜓 𝑗/Λ, so𝐵(Λ)≤Λ −1 ˝ 𝑗𝑔𝑗 =1/Λ and the series
converges locally uniformly;𝐵 is therefore continuous, strictly decreasing where positive, with𝐵(0+)=∞
and𝐵(∞)=0 , and equation (9) has a unique rootΛ. The same bound𝑥𝑏≤𝑊𝑏/Λcontrols the high-count
contribution to the finite budget uniformly in𝑀 by Step 1, so the finite (random) budget functions converge
to 𝐵 in probability at every fixedΛ. Strict monotonicity then squeezes the equilibrium value: for any
Λ′ <Λ<Λ ′′, eventually𝐵𝑀(Λ′)> 𝑁𝑀/𝑀 > 𝐵𝑀(Λ′′) with probability tending to one, soΛ𝑀→Λ in
probability.
Step 3: from values to discovery.The welfare identity of proposition 7 gives conditional discovery
𝑁𝑀𝜆𝑀 =(𝑁 𝑀/𝑀)Λ𝑀≤1 , soΛ𝑀≤𝑀/𝑁 𝑀 is uniformly bounded, and bounded convergence yields
𝐺sym market=E[𝑁 𝑀𝜆𝑀]→𝛼Λ.
Step 4: the tilted form.Multiplying the budget equation byΛand usingΛ=𝜓𝑗ℎ(𝑥𝑗)on active classes,
𝛼Λ=
∑︁
𝑗
𝑓𝑗𝑥𝑗𝜓𝑗ℎ(𝑥𝑗)=
∑︁
𝑗
𝑓𝑗𝜓𝑗
1−𝑒 −𝑥 𝑗  = ∑︁
𝑗
𝑔𝑗
1−𝑒 −𝑥 𝑗  :
25

in the limit the market covers the target’s own count class𝑗 with probability1−𝑒 −𝑥 𝑗, where the target’s count
is Poisson(𝛼𝑟) and the number of occupants of any fixed box is asymptoticallyPoisson(𝑥𝑗). Canonically
Λ=1.094021 lies strictly between𝜓1=0.948 and𝜓2=3.555 , so the limit market abandons every box with
fewer than two reports. □
Abundant evidence (remark 2).Hold𝑝 fixed. By the multiplicative Chernoff bound,P(𝐶𝜃≤𝑁 𝑀𝑝/2)≤
𝑒−𝑁 𝑀𝑝/8→0 . Each false count isBinomial(𝑁𝑀,𝑞 𝑀) with mean𝑁𝑀𝑞𝑀→𝛼(1−𝑝) , so the standard
upper-tail bound givesP(𝐶𝑏≥𝑁 𝑀𝑝/2)≤ 2𝑒𝑞𝑀/𝑝𝑁𝑀𝑝/2, whose base is𝑂(1/𝑀) while the exponent
grows linearly in𝑀; the union bound over the𝑀−1 false boxes therefore vanishes. With probability
tending to one the target is the unique plurality winner, so𝐺consensus→1 . The same argument applies
whenever 𝜆𝑀 =𝑁 𝑀𝑝𝑀 satisfies 𝜆𝑀/log𝑀→ ∞ : the target count concentrates above𝜆𝑀/2 while
𝑀exp

−(𝜆𝑀/2)log(𝜆 𝑀/2𝑒𝛼)

→0.□
E Computational verification and status of claims
The accompanying scriptverify_shared_discovery_v8_6.py, available with all data tables and figures
atgithub.com/yoheinakajima/shared-discovery-paradox, performs the following checks.
1. It verifies the reciprocal-share identity and the water-filling equilibrium on200 random posteriors,
including dominant-posterior pure corners.
2. It verifies the welfare identity𝐺sym market=𝑁𝜆posterior by posterior.
3. It reproduces the uniform-posterior formula and the𝑒/(𝑒−1)limit.
4. It verifies the tight2−1/𝑁family and the sole-rescue pure-equilibrium characterization.
5. It exactly enumerates the67 canonical report-count classes for every copying value, verifies that class
probabilities sum to one, and reproduces the private-search closed form.
6. It reproduces the independent pooled frontier, the canonical market value0.599099252439, the full
copying table, and the crossover𝑐∗=0.788461656521.
7. Itverifiestheblind-controlvalues 8/16=0.50 and 1−(1−1/16) 8=0.403281 ,andthattheblind-sentinel
hybrid family is maximized at zero sentinels.
8. It computes the average-quality column exactly (𝑄sym market=0.344136160273 ) and verifies the redundancy
identity𝑁𝑄−𝐺=E[(𝐾−1) +] class by class for the market and in closed form for the other protocols.
9. It evaluates the proportional sparse-evidence limits at𝛼=1/2 ,𝑟=3.75 , checks the fill-identity form of
the portfolio limit, and runs a seeded Monte Carlo convergence diagnostic at𝑀∈{16,64,256}.
10. It cross-checks a closed-form expression for the common-cue likelihood coefficients against the direct
enumeration on three(𝑀,𝑁,𝑝) configurations, and validates a batched equilibrium solver against the
scalar solver on random posteriors.
11. It solves the market limit equation equation (9) to high precision (Λ =1.094021073740 , 𝐺=
0.547010536870), verifies the tilted-form identity to10−11, confirms that the active support starts
at two reports, and runs a seeded Monte Carlo convergence diagnostic for the finite market at
𝑀∈{16,64,256,1024}.
12. It computes the partial-conformity curve of remark 1 exactly for𝑎=0,...,8 , verifies the endpoints
𝐺(0)=𝐺 private and𝐺(8)=𝐺 consensus, and confirms the strict monotone decline.
26

13. It verifies the limit gap decomposition𝐺private−𝐺 sym market→𝑔 1+ ˝ 𝑗≥2 𝑔𝑗𝑒−𝑥 𝑗 =0.287541+0.012094
to 10−11, and runs a seeded fixed-𝑝 Monte Carlo confirming the abundant-evidence remark (consensus
0.385→0.947→1.000at𝑀∈{16,64,256}).
14. It scans the72-combination comparative-statics grid, verifies that the market–private gap changes sign at
most once in every combination, and writes the crossover locations togrid_crossings.csv.
15. It generates every figure and the underlying CSV tables.
Analytically established.The value-of-information and fixed-budget dominance results; posterior-count
ranking under independent symmetric signals; private coverage dominance over one-action consensus; the
weak monotone harm of partial conformity by set inclusion; the blind-control values; the redundancy identity
𝑁𝑄−𝐺=E[(𝐾−1) +]; the proportional sparse-evidence limits, including the market cell of equation (9)
and the abundant-evidence consistency remark; the reciprocal-share identity; the exact-potential and payout
identities for equal sharing; the anonymous water-filling equilibrium including its pure corner;𝐺sym market=𝑁𝜆 ;
the exact mixedPoA=2−1/𝑁 upper bound and tight family; full pure-strategy implementation under
sole-rescue; channel collapse and the closed-form private discovery function; failure of count ranking under
dependence by explicit counterexample; the fill identity; and strict monotonicity of the centralized planner
gain.
Exactly enumerated or numerically solved for the canonical model.Consensus, private, planner, and
action-budget frontier values; the partial-conformity curve𝐺(𝑎) ; recovery budget; expected distinct-action
counts; the anonymous market value and its average-quality column; the common-cue table; and the
market/private crossover. Enumeration over report classes is exact up to floating-point evaluation of finite
formulas; one-dimensional equilibrium and crossover equations are solved to high numerical precision.
Computational patterns, not general theorems.The canonical herding discount vanishes for action
budgets𝐿≥3 on the tested copying grid; the canonical recovery budget is nonincreasing over that grid; and
the market/private gap changes sign at most once on the tested72-combination grid—exactly once in52
combinations and never in the remaining20, where private report-following stays ahead through𝑐=0.98 .
These patterns should not be generalized without additional analysis.
References
Daron Acemoglu, Ali Makhdoumi, Azarakhsh Malekian, and Asuman Ozdaglar. Informational Braess’
paradox: The effect of information on traffic congestion.Operations Research, 66(4):893–917, 2018. doi:
10.1287/opre.2017.1712.
George A. Akerlof. The market for “lemons”: Quality uncertainty and the market mechanism.Quarterly
Journal of Economics, 84(3):488–500, 1970. doi: 10.2307/1879431.
W. Brian Arthur. Inductive reasoning and bounded rationality.American Economic Review, 84(2):406–411,
1994.
Abhijit V. Banerjee. A simple model of herd behavior.Quarterly Journal of Economics, 107(3):797–817,
1992. doi: 10.2307/2118364.
27

SushilBikhchandani,DavidHirshleifer,andIvoWelch. Atheoryoffads,fashion,custom,andculturalchange
as informational cascades.Journal of Political Economy, 100(5):992–1026, 1992. doi: 10.1086/261849.
David Blackwell. Equivalent comparisons of experiments.Annals of Mathematical Statistics, 24(2):265–272,
1953. doi: 10.1214/aoms/1177729032.
Sanmay Das, Emir Kamenica, and Renee Mirka. Reducing congestion through information design. In
Proceedings of the 55th Annual Allerton Conference on Communication, Control, and Computing, pages
1279–1284, 2017. doi: 10.1109/ALLERTON.2017.8262884.
Eamon Duede and James Evans. The paradox of collective certainty in science. arXiv:2406.05809
[physics.soc-ph], 2024.
Martin Gairing. Covering games: Approximation through non-cooperation. In Stefano Leonardi, editor,
Internet and Network Economics: 5th International Workshop, WINE 2009, volume 5929 ofLecture Notes
in Computer Science, pages 184–195. Springer, 2009. doi: 10.1007/978-3-642-10841-9_18.
Daniel Golovin and Andreas Krause. Adaptive submodularity: Theory and applications in active learning
and stochastic optimization.Journal of Artificial Intelligence Research, 42:427–486, 2011. doi: 10.1613/
jair.3278.
Philip Kitcher. The division of cognitive labor.Journal of Philosophy, 87(1):5–22, 1990. doi: 10.2307/
2026796.
Bernard O. Koopman. The theory of search. III. the optimum distribution of searching effort.Operations
Research, 5(5):613–626, 1957. doi: 10.1287/opre.5.5.613.
Elias Koutsoupias and Christos Papadimitriou. Worst-case equilibria. InProceedings of the 16th Annual
Symposium on Theoretical Aspects of Computer Science, volume 1563 ofLecture Notes in Computer
Science, pages 404–413. Springer, 1999. doi: 10.1007/3-540-49116-3_38.
Krishna K. Ladha. The condorcet jury theorem, free speech, and correlated votes.American Journal of
Political Science, 36(3):617–634, 1992. doi: 10.2307/2111584.
James G. March. Exploration and exploitation in organizational learning.Organization Science, 2(1):71–87,
1991. doi: 10.1287/orsc.2.1.71.
Jacob Marschak and Roy Radner.Economic Theory of Teams. Yale University Press, New Haven, 1972.
Conor Mayo-Wilson, Kevin J. S. Zollman, and David Danks. The independence thesis: When individual and
social epistemology diverge.Philosophy of Science, 78(4):653–677, 2011. doi: 10.1086/661777.
Dov Monderer and Lloyd S. Shapley. Potential games.Games and Economic Behavior, 14(1):124–143, 1996.
doi: 10.1006/game.1996.0044.
Richard R. Nelson. Uncertainty, learning, and the economics of parallel research and development efforts.
Review of Economics and Statistics, 43(4):351–364, 1961. doi: 10.2307/1927475.
George L. Nemhauser, Laurence A. Wolsey, and Marshall L. Fisher. An analysis of approximations for
maximizing submodular set functions—I.Mathematical Programming, 14(1):265–294, 1978. doi:
10.1007/BF01588971.
28

Robert W. Rosenthal. A class of games possessing pure-strategy Nash equilibria.International Journal of
Game Theory, 2:65–67, 1973. doi: 10.1007/BF01737559.
Tim Roughgarden. Intrinsic robustness of the price of anarchy.Journal of the ACM, 62(5):32:1–32:42, 2015.
doi: 10.1145/2806883.
Andrey Rzhetsky, Jacob G. Foster, Ian T. Foster, and James A. Evans. Choosing experiments to accelerate
collective discovery.Proceedings of the National Academy of Sciences, 112(47):14569–14574, 2015. doi:
10.1073/pnas.1509757112.
Thomas C. Schelling. Dynamic models of segregation.Journal of Mathematical Sociology, 1(2):143–186,
1971. doi: 10.1080/0022250X.1971.9989794.
Lones Smith and Peter Sørensen. Pathological outcomes of observational learning.Econometrica, 68(2):
371–398, 2000. doi: 10.1111/1468-0262.00113.
Adrian Vetta. Nash equilibria in competitive societies, with applications to facility location, traffic routing
and auctions. InProceedings of the 43rd Annual IEEE Symposium on Foundations of Computer Science,
pages 416–425. IEEE, 2002. doi: 10.1109/SFCS.2002.1181966.
Kevin J. S. Zollman. The communication structure of epistemic communities.Philosophy of Science, 74(5):
574–587, 2007. doi: 10.1086/525605.
29
