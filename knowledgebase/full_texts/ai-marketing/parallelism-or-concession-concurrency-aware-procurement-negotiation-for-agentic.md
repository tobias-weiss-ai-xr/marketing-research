---
title: Parallelism or Concession? Concurrency-Aware Procurement Negotiation for Agentic Commerce
url: https://arxiv.org/abs/2610.06017
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Xiaolin Xu
- Donghao Zhu
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.06017
pages: 11
chars: 58122
fetched_at: '2026-11-08T13:24:50+00:00'
kb_version: 1
---

# Parallelism or Concession? Concurrency-Aware Procurement Negotiation for Agentic Commerce

Parallelism or Concession? Concurrency-Aware Procurement
Negotiation for Agentic Commerce
Xiaolin Xu
School of Business
Nanjing University
Nanjing, Jiangsu, China
xuxl@nju.edu.cn
Donghao Zhu∗
Institute of Business Sciences
University of Tsukuba
Bunkyo-ku, Tokyo, Japan
University of Tokyo Market Design Center
Bunkyo-ku, Tokyo, Japan
zhu.donghao.gt@u.tsukuba.ac.jp
Abstract
Agentic buyers can cheaply fork a procurement task into many
parallel negotiations, but concurrency is not free: every thread
consumes resources, and simultaneous agreements create cancella-
tion and commitment risk. We study a one-unit post-order sourcing
problem with a single hard-deadline negotiation window, in which a
planner jointly chooses the number of seller-facing negotiators and
a common procurement price cap. The model combines a product-
specific acceptance curve with fulfillment loss, per-thread cost, and
excess-commitment cost. We establish three structural results. First,
holding the per-thread acceptance target fixed, the marginal value
of another negotiator decays geometrically, yielding a conditional
concurrency threshold. Second, under a convex quantile curve, par-
allelism substitutes for concession: more concurrent negotiators
imply a weakly lower per-thread acceptance target and price cap.
Third, when prices are more dispersed, Agentic buyers benefit by
searching harder for bargains, but suffer when they instead try to
guarantee procurement by offering higher prices. We operational-
ize these results in theConcurrency-A ware Negotiation Optimizer
(Cano), a deterministic optimizer that jointly determines the op-
timal negotiation concurrency and procurement price cap for an
agentic procurement system. Across different analytic market con-
figurations and extensive Monte Carlo, finite-data, non-Gaussian,
and correlated-seller stress tests,Canoconsistently outperforms
common heuristic policies while validating the predicted structural
properties.
CCS Concepts
•Computing methodologies→ Multi-agent systems;•Theory
of computation→ Algorithmic game theory and mechanism design;
•Applied computing→Online shopping.
Keywords
automated negotiation, agentic commerce, concurrent negotiation,
procurement, multi-agent orchestration, reservation price
ACM Reference Format:
Xiaolin Xu and Donghao Zhu. 2026. Parallelism or Concession? Concurrency-
Aware Procurement Negotiation for Agentic Commerce. InThe Eighth Inter-
national Conference on Distributed Artificial Intelligence (DAI ’26), November
29–December 2, 2026, Hong Kong, China.ACM, New York, NY, USA, 11 pages.
∗The authors are listed alphabetically by family name. Donghao Zhu is the lead and
primary contributor to this work.
DAI ’26, Hong Kong, China
1 Introduction
Large language model (LLM) agents are beginning to search, bar-
gain, and transact on behalf of users. A distinctive capability of
such systems ischeap replication: a single procurement task can be
delegated to multiple seller-facing subagents in parallel. Replication
increases the chance of finding an acceptable seller while reducing
the concession required in any individual negotiation. However,
simply contacting every seller is rarely optimal. Each additional ne-
gotiation thread consumes tokens, time, and seller attention, while
near-simultaneous agreements may leave the buyer with multiple
commitments for a single purchase.
This trade-off has attracted attention in both classical automated
negotiation and recent language-agent systems. Prior work on
concurrent negotiation studies coordination, tentative agreements,
and decommitment [2, 4, 14], while recent benchmarks evaluate
language agents in multi-seller markets with parallel execution [13,
16]. Nevertheless, existing approaches typically treat the number of
negotiation threads or the buyer’s reservation price as fixed inputs,
or learn an end-to-end dialogue policy. They do not isolate the
fundamental orchestration decision that arises before any dialogue
begins:How many negotiation agents should be launched, and what
procurement price cap should they share?
Those controls are coupled. Holding a cap fixed while adding
threads improves fulfillment but also increases the chance of du-
plicate acceptance. Holding concurrency fixed while raising the
cap improves each thread’s success but directly reduces transac-
tion surplus. Optimizing either control in isolation can therefore
recommend a high deal rate and still destroy value. The coupling is
especially consequential for language agents because replication is
cheap enough to make large𝑚 operationally plausible, while their
seller-facing actions remain difficult to coordinate after several
conversations converge at nearly the same time.
We answer this question for one-unit post-order procurement.
After accepting a customer order, a platform observes𝑁 eligible
sellers and an estimated offer-acceptance curve𝐹. It chooses𝑚≤𝑁
concurrent negotiators and a common terminal cap𝑏. All contacted
sellers must be launched before any terminal response arrives: The
delivery service-level agreement leaves time for one negotiation
window, but not for a second serial attempt. A seller accepts with
probability 𝐹(𝑏) . Failure incurs loss 𝐿, each thread costs 𝜅, and
each acceptance beyond the one fulfilled agreement incurs resid-
ual commitment cost𝛿. The last term captures races that remain
even with a commitment manager: cancellation work, seller harm,
reputational loss, or a legally binding tentative action.
arXiv:2610.06017v1  [cs.GT]  5 Oct 2026

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xu and Zhu
Market estimator
𝑁, b𝐹
Canoplanner
𝑚★, 𝑞★, 𝑏★
Parallel negotiation agents
1,...,𝑚 ★ seller-facing agents
offers constrained by
𝑝𝑖 ≤𝑏 ★ for each 𝑖≤𝑚 ★
Commitment manager
execute at most
one transaction
cancel or record the rest
outcome log, auditing, and acceptance-curve updates
Figure 1:Canoas the economic control layer of an agentic procurement system. The market estimator supplies the eligible-seller
count𝑁 and estimated acceptance curve b𝐹 . The planner selects concurrency 𝑚★, acceptance target𝑞★, and procurement cap
𝑏★. Seller-facing agents negotiate in parallel subject to 𝑝𝑖𝑡≤𝑏 ★, and the commitment manager executes at most one binding
transaction. Logged outcomes support auditing and future acceptance-curve updates.
Our contribution is a small, auditable control problem rather
than another end-to-end bargaining policy.
• We formulate concurrency and concession jointly through
a single expected-profit objective. The objective separates
fulfillment value, language-agent operating cost, and excess-
commitment exposure.
• We characterize a fixed-target concurrency threshold, prove
that parallelism substitutes for concession under explicit
regularity conditions, and identify a sign reversal in the
value of price dispersion.
• We implementCanoand evaluate it over a complete 1944-
configuration factorial sweep. The main comparisons are
analytic rather than sample-contingent; one million simu-
lated orders validate the expectation, and additional exper-
iments study estimation error, non-Gaussian markets, and
correlated seller prices.
The results reveal two practical insights. First, as the number of
sellers increases, Agentic buyers can rely more on parallel search
and less on raising prices to secure procurement. Second, greater
price dispersion creates more opportunities to find bargains, but
also makes guaranteed procurement more expensive.
2 Background and System Framework
2.1 Related Work
Automated and concurrent negotiation.Automated negotiation
has long combined game-theoretic, heuristic, and argumentation-
based approaches [9]. Parallel protocols and commitment models
allow one agent to bargain with several counterparties while con-
trolling delay and decommitment [1, 14]. An et al. [2] coordinate
tentative agreements and concessions for multiple resources, and
Bagga et al. [ 4] learn one-to-many policies with deep reinforce-
ment learning. The recent taxonomy of Florijn et al. [6] emphasizes
that one-to-many settings differ principally in how negotiation out-
comes interact. Our setting is the unit-demand case: successes are
substitutes, and at most one can be retained. Unlike dialogue-level
strategies, we obtain a product-aware ex ante rule for both the
number of dialogues and their shared reservation cap.
Language-mediated bargaining.End-to-end negotiation dialogue
models jointly learn strategy and language [10]; modular models in-
stead decouple a strategic act from its linguistic realization [8]. This
separation has become especially relevant for LLM agents. Negoti-
ationArena, buyer-side bargaining evaluations, and self-play stud-
ies document strategic variation and irrational behavior [5, 7, 15].
Consumer-market experiments report overpayment and unfavor-
able transactions [16], while verifiable-reward training improves
budget adherence and surplus extraction [11, 12]. AgenticPay pro-
vides 111 tasks from bilateral to many-to-many negotiation and
directly contrasts sequential and parallel modes [13].Canois com-
plementary: it is an outer economic controller, not a language policy
or benchmark. In particular, its cap can be enforced after an LLM
proposes a structured price action.
2.2 Positioning
Our unit of analysis is an orchestration decision, rather than an
utterance, dialogue trajectory, or learned bargaining equilibrium.
This creates two differences from the closest systems work. First,
the policy is chosenbeforeseller-facing text is generated and is ex-
pressed in quantities that an execution layer can enforce: a thread
count and a terminal cap. Second, the objective values fulfillment,
price, computation, and duplicate commitments jointly; agreement
rate alone is not the target. The theory does not assert that one
language model persuades better than another. It specifies theeco-
nomic authoritywithin which any such model may act and supplies
comparative statics that dialogue benchmarks can test.
Figure 1 illustrates the overall workflow ofCano. The market
estimator learns the eligible seller count𝑁 and acceptance curve b𝐹
from historical offer–response data. Based on these estimates, the
planner jointly determines the optimal concurrency𝑚★, acceptance
target𝑞★, and procurement price cap𝑏★. The selected seller-facing
agents negotiate in parallel under the shared price cap, while the
commitment manager executes at most one transaction and records
the remaining commitments. The resulting outcome log is fed back
to the market estimator to improve future acceptance-curve esti-
mation.
2.3 System Architecture
At planning time, the estimator supplies a product-state snapshot,
an eligible seller set, and an estimated acceptance curve 𝐹. The
planner uses the corresponding quantile function𝐶(𝑞)=𝐹 −1(𝑞)
to translate a target per-thread acceptance probability into the
corresponding procurement price cap. It then either returns “cancel”
or a tuple(𝑚★,𝑞 ★,𝑏 ★) together with a selected set of 𝑚★ sellers.
During execution, each language agent may propose negotiation
actions, but every proposed action is validated by the execution
layer before being dispatched. In particular, the execution layer

Parallelism or Concession? DAI ’26, November 29–December 2, 2026, Hong Kong, China
Table 1: Core notation and operational interpretation.
Symbol Meaning
𝑁eligible sellers (market thickness)
𝑚concurrently launched negotiators
𝑏=𝐶(𝑞)common terminal procurement cap
𝑉net value of a fulfilled order
𝐿loss from cancellation or failed fulfillment
𝜅cost per launched negotiation thread
𝛿cost per acceptance beyond the first
enforces
𝑝𝑖≤𝑏 ★ and
𝑚★∑︁
𝑖=1
𝑥𝑖≤1,
where𝑥𝑖∈{ 0, 1} is a binary commitment indicator that equals 1 if
seller𝑖 is selected for the final binding transaction, and 0 otherwise.
The parameter𝛿 represents the residual cost incurred when simul-
taneous negotiations cannot be perfectly coordinated because of
external latency, seller-side finalization, or legally binding tentative
acceptance. It models unavoidable implementation risk rather than
relaxing the execution constraints.
The outcome log records the estimator version, planned tuple,
offers, acceptances, rejected actions, final commitment, and can-
cellations. These records support off-policy recalibration of𝐹, cap-
violation audits, and human review without exposing the language
model to unilateral authority over payment. Thus Figure 1 sepa-
rates a statistical component that may be uncertain, an optimization
component that is deterministic given its inputs, and an execution
component that is safety critical. The architecture is presented to
clarify the system context rather than to optimize every component.
In particular, this paper focuses exclusively on the economic con-
trol layer, the planner that determines negotiation concurrency and
procurement price caps, while estimator design, language policy,
and execution engineering are outside the scope of this work.
3 Procurement Model
3.1 Market and Decisions
One accepted customer order yields net value𝑉> 0if fulfilled, after
non-procurement costs. There are𝑁 sellers that already satisfy qual-
ity and delivery filters. Seller𝑖’s minimum acceptable terminal price
is𝑅𝑖∼𝐹 , independently and identically distributed conditional on
the product state. The planner starts𝑚∈{ 1,...,𝑁} threads and
assigns the same terminal procurement cap 𝑏 to every thread. It
may instead cancel immediately, denoted𝑚= 0, receiving payoff
−𝐿. We remark that, if procurement is expected to be uneconomi-
cal, the platform may immediately cancel the order and refund the
customer instead of initiating negotiation. The cap is awalk-away
price, not an opening offer. The terminal-offer abstraction charges
𝑏 whenever at least one seller accepts. It is conservative when a
multi-round protocol sometimes closes below its cap [3].
A seller accepts if and only if 𝑅𝑖≤𝑏<𝑉 . We write𝑞=𝐹(𝑏)
and𝐶(𝑞)=𝐹 −1(𝑞) where𝑞 is per-thread acceptance probability
and𝐶 is the reservation-price quantile curve. “Price dispersion”
below always refers to dispersion in the latent distribution of seller
reservation prices𝑅𝑖, rather than dispersion in posted prices. For
the structural results, 𝐹 is continuous and strictly increasing on
the price interval containing the active policies, so the displayed
inverse is well defined. The implementation can instead consume a
bounded empirical quantile and uses global numerical search rather
than the derivative results.
Remark (timing and information).The customer order is already
accepted when sourcing begins. The platform first applies non-price
eligibility filters and freezes a product-state estimate of𝐹; It then
chooses𝑚,𝑏 , launches the threads simultaneously, observes termi-
nal acceptances at the end of the sourcing window, and retains at
most one transaction. There is no opportunity to launch a replace-
ment thread after observing failure without missing the fulfillment
deadline. Outcomes update future estimates but do not change𝐹
within the current order. After conditioning on observable seller
and product characteristics through eligibility filtering and market
estimation, the remaining reservation prices are assumed to be i.i.d.
Shared unobserved shocks violate it and are evaluated separately
in Section 5.3.
We restrict attention to a common cap. Exchangeability moti-
vates this parsimonious choice, and it reduces the execution in-
terface to one auditable scalar, but we do not claim it is optimal
among arbitrary asymmetric mechanisms. If seller-specific features
support distinct conditional curves𝐹𝑖, the planner should choose
seller-specific caps and a subset jointly; that heterogeneous assign-
ment problem is outside the structural claims here. Likewise, 𝐹
describes the terminal response to a cap under a fixed interaction
protocol. It is not identified by posted prices, and it may change if
the dialogue policy, seller population, or product state changes.
3.2 Expected Objective
For𝑚≥ 1, the number of acceptances is𝐾∼Binomial(𝑚,𝑞) . Hence
𝑆𝑚(𝑞)=P(𝐾≥1)=1−(1−𝑞) 𝑚
and
𝐷𝑚(𝑞)=E[(𝐾−1) +]=𝑚𝑞−𝑆 𝑚(𝑞).(1)
When𝐾= 0, payoff is−𝐿−𝜅𝑚 . When𝐾≥ 1, the buyer keeps one
agreement and receives𝑉−𝑏−𝜅𝑚−𝛿(𝐾− 1). Taking expectations
gives
Π(𝑚,𝑏)=(𝑉−𝑏)𝑆 𝑚(𝐹(𝑏))|               {z               }
Expected fulfilled-order value
−𝐿[1−𝑆 𝑚(𝐹(𝑏))]|               {z               }
Expected fulfillment loss
−𝜅𝑚|{z}
Thread cost
−𝛿{𝑚𝐹(𝑏)−𝑆 𝑚(𝐹(𝑏))}|                       {z                       }
Expected excess-commitment cost
.(2)
The objective (2) consists of four economically meaningful com-
ponents. The first term is the expected surplus generated when
procurement succeeds, namely the net order value multiplied by
the fulfillment probability. The second term is the expected loss
from procurement failure. The third term captures the operating
cost of launching negotiation threads. The final term represents the
expected cost of excess commitments caused by multiple simulta-
neous acceptances. In acceptance space this becomes the central
objective:
Π(𝑚,𝑞)=[𝑉+𝐿+𝛿−𝐶(𝑞)]𝑆 𝑚(𝑞)−𝐿−𝜅𝑚−𝛿𝑚𝑞. (3)

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xu and Zhu
In addition to profit and fulfillment, we report two complemen-
tary measures of commitment risk. The expected number of accep-
tances beyond the first is𝐷𝑚(𝑞), defined in (1). The probability that
at least two threads accept is
𝐵𝑚(𝑞)=1−(1−𝑞) 𝑚−𝑚𝑞(1−𝑞) 𝑚−1.
𝐷𝑚 prices the linear exposure in the objective, whereas𝐵𝑚 is easier
to interpret as the frequency of orders requiring decommitment
handling. Both are zero for 𝑚= 1, but neither is controlled by
fulfillment probability alone.
The planner maximizes Π over𝑚∈{ 1,...,𝑁} and𝑞∈[ 0, 1],
then compares the best procurement policy with immediate can-
cellation Π( 0)=−𝐿 . Appendix A.1 gives the full derivation and
boundary conventions.
4 Structural Results andCano
4.1 A Threshold for Concurrency
Fix𝑞. The value of adding a(𝑚+1)-st thread is
Δ𝑚(𝑞)=[𝑉+𝐿+𝛿−𝐶(𝑞)]𝑞(1−𝑞) 𝑚−𝜅−𝛿𝑞.(4)
Proposition 4.1 (Concurrency threshold).For fixed 𝑞∈
(0,1):
(1) If𝑉+𝐿+𝛿−𝐶(𝑞)> 0, then Δ𝑚+1(𝑞)<Δ 𝑚(𝑞) for all𝑚≥ 1.
(2)If𝑉+𝐿+𝛿−𝐶(𝑞)≤0, thenΔ 𝑚(𝑞)≤0for all𝑚≥1.
(3) With ties resolved in favor of fewer threads, the optimizer of
the fixed-𝑞problem is
𝑚★ 𝑞 =min{𝑚∈{1,...,𝑁}:𝑚=𝑁orΔ 𝑚(𝑞)≤0 }.
Proposition 4.1 establishes a threshold structure for concurrency.
For a fixed per-thread acceptance target, the planner continues
adding negotiators while the next thread has positive incremental
value and stops once this value becomes non-positive. The compar-
ative statics follow immediately from (4). Increasing𝑉 or𝐿 raises
the incremental value of every additional thread, whereas increas-
ing𝜅 or𝛿 lowers it. Consequently, the threshold weakly increases
with𝑉and𝐿, and weakly decreases with𝜅and𝛿. The intuition is
event-based. Thread𝑚+ 1creates new fulfillment value only when
all first𝑚 threads fail, an event with probability(1−𝑞)𝑚. Operating
and excess-commitment costs do not enjoy this geometric discount.
The complete proof is in Appendix A.2.
The threshold is directly computable without enumerating all
subsets. If𝜅+𝛿𝑞> 0, the stopping point is the smallest𝑚≥ 1such
that
(𝑉+𝐿+𝛿−𝐶(𝑞))𝑞(1−𝑞) 𝑚≤𝜅+𝛿𝑞.(5)
This expression separates ascarcity term,(𝑉+𝐿+𝛿−𝐶(𝑞))𝑞( 1−𝑞)𝑚,
from a nonvanishing launch-and-commitment cost. It also shows
why a large seller pool does not imply contacting every seller:𝑁
enlarges the feasible set, but it does not slow the geometric decay
of the next thread’s contribution. If𝜅=𝛿= 0, every finite marginal
is positive and the fixed-𝑞subproblem selects𝑁.
4.2 Parallelism Substitutes for Concession
For fixed𝑚, define
𝐴𝑚(𝑞)= 1−(1−𝑞) 𝑚 𝑚(1−𝑞) 𝑚−1 = 𝑞 𝑚 𝑚−1∑︁ 𝑗=0 (1−𝑞) −𝑗.
We state the substitution result under conditions that rule out spu-
rious nonconvex roots.
Assumption 1 (Regular qantile).Let 𝐼={𝑞∈( 0, 1) :𝐶(𝑞)≤
𝑉+𝐿+𝛿} . On𝐼 ,𝐶 is twice continuously differentiable, 𝐶′(𝑞)> 0,
and𝐶′′(𝑞)≥ 0. For every fixed 𝑚 under comparison, every global
maximizer over𝑞∈[0,1]lies in the interior of𝐼.
Assumption 1 imposes mild regularity conditions on the reservation-
price quantile curve. Monotonicity (𝐶′(𝑞)> 0) reflects the natural
requirement that achieving a higher acceptance probability requires
a weakly higher procurement cap. Convexity (𝐶′′(𝑞)≥ 0) rules
out pathological quantile shapes and ensures that progressively
higher acceptance targets become increasingly expensive. Finally,
restricting the optimizer to the interior of 𝐼 excludes degenerate
corner solutions, such as always rejecting or always accepting, and
ensures that the optimum is fully characterized by the first-order
condition, allowing the comparative-statics analysis to focus on
economically meaningful operating regimes.
Theorem 4.2 (Parallelism–concession substitution).Under
Assumption 1, the fixed-𝑚optimizer𝑞 ★ 𝑚 is unique and satisfies
𝐶(𝑞)+𝐶 ′(𝑞)𝐴𝑚(𝑞)+𝛿  (1−𝑞) −(𝑚−1) −1  =𝑉+𝐿.(6)
Moreover,
𝑞★ 𝑚+1≤𝑞 ★ 𝑚 and𝐶(𝑞 ★ 𝑚+1)≤𝐶(𝑞 ★ 𝑚).
Theorem 4.2 shows that the optimal bargaining policy depends
on the available degree of parallelism. As more negotiation agents
(larger𝑚) are launched in parallel, the planner optimally lowers
the target per-thread acceptance probability, which in turn implies
a lower procurement cap. Consequently, parallelism substitutes for
concession: additional negotiation threads allow each individual
agent to bargain more aggressively rather than relying on higher
prices to secure procurement. Therefore, an agentic buyer should
adapt its bargaining policy to the available degree of parallelism
instead of replicating one fixed strategy across different market
conditions. Conversely, when API or seller-contact cost raises𝜅, the
joint solution typically uses fewer threads and compensates with a
higher cap. The proof in Appendix A.3 shows that both𝐴𝑚(𝑞) and
the commitment term in (6) grow with𝑚, forcing the unique root
leftward.
Equation (6) is a marginal balance condition: the planner in-
creases the procurement cap until the marginal gain from higher
procurement reliability is exactly offset by the marginal procure-
ment and duplicate-commitment costs. As more negotiation agents
are launched in parallel, overall procurement becomes less depen-
dent on any single negotiation thread, reducing the need to buy
reliability through higher prices. Consequently, parallelism substi-
tutes for concession: more parallel agents imply a lower optimal
acceptance target and procurement cap for each individual negotia-
tor. The thread cost𝜅 does not appear in the first-order condition
because it is independent of the procurement cap for fixed𝑚. In-
stead, it affects the outer optimization that determines the optimal
number of negotiation threads. Managerially, the theorem suggests
that, when parallelism is inexpensive, agentic buyers should in-
vest computational resources in broader parallel search rather than
higher procurement prices.

Parallelism or Concession? DAI ’26, November 29–December 2, 2026, Hong Kong, China
4.3 When Dispersion Helps
Consider a mean-preserving symmetric location-scale family, in
which the mean reservation price remains fixed while the distri-
bution becomes more or less dispersed symmetrically around the
mean:
𝐶𝜎(𝑞)=𝜇+𝜎𝑧(𝑞)and𝑧(1−𝑞)=−𝑧(𝑞),
where 𝜎 controls the degree of price dispersion and symmetry
implies that reservation prices spread equally above and below the
mean. So𝑧(𝑞) is negative below the median and positive above it.
The uniform family used for the main experiment has
𝑧(𝑞)=
√
3(2𝑞−1)and𝑅 𝑖∼𝑈
h
𝜇−
√
3𝜎,𝜇+
√
3𝜎
i
.
Theorem 4.3 (Dispersion sign reversal).Fix 𝑚. Suppose its
maximizing target is unique and interior. Let Π★ 𝑚(𝜎) denote the re-
sulting maximized profit. At differentiability points,
𝑑Π ★ 𝑚(𝜎)
𝑑𝜎 =−𝑧(𝑞 ★ 𝑚)𝑆𝑚(𝑞★ 𝑚).
Hence dispersion raises optimal value when 𝑞★ 𝑚 < 1/2, lowers it when
𝑞★ 𝑚 >1/2, and is locally neutral at𝑞 ★ 𝑚 =1/2.
Parallel search makes the lower tail usable. In a thick market,
where many eligible sellers are available, the buyer can achieve
high overall fulfillment even when each individual negotiation has
a relatively low acceptance probability (𝑞★ 𝑚 < 1/2). Consequently,
spreading reservation prices creates more opportunities to find
low-price sellers. By contrast, in a thin market, where only a few
eligible sellers are available, or when fulfillment reliability is critical,
the planner must keep the target acceptance probability above the
median. Although Theorem 4.3 is stated for a fixed concurrency
level𝑚, the same conclusion extends piecewise to the joint opti-
mization problem. Specifically, whenever the optimal concurrency
𝑚★(𝜎) remains constant over an interval of𝜎, the value function
satisfies Π★(𝜎)=Π ★ 𝑚★(𝜎) and the dispersion result applies directly.
Non-differentiability may occur only at switching points where
the optimizer changes from one concurrency level to another, i.e.,
𝑚★(𝜎−)≠𝑚 ★(𝜎+). The complete envelope argument is provided
in Appendix A.4.
The result is deliberately local to a location–scale family. It does
not say that every mean-preserving spread is beneficial below the
median, nor that an increase in observed listing-price variance has
this effect. The operative object is the estimated terminal acceptance
quantile. The sign result is useful because it converts a distributional
change into a testable policy boundary: After re-optimization, the
active target𝑞★ =. 5separates a lower-tail-search regime from a
reliability-through-concession regime.
4.4CanoOptimizer
Canoenumerates 𝑚= 1,...,𝑁 , solves the one-dimensional fixed-
𝑚 problem, evaluates (3), and compares the best result with −𝐿.
Under Assumption 1, the left side of (6) is strictly increasing, so
bisection with boundary checks returns a globally optimal policy
to tolerance𝜀 using𝑂(𝑁log( 1/𝜀)) evaluations of the quantile func-
tion and its derivative. Empirical acceptance curves and mixtures
need not satisfy the assumption. Our implementation therefore uses
a bounded global scan in𝑞, followed by golden-section refinement
around the best cell. Unlike derivative-based root-finding meth-
ods, this implementation does not rely on a favorable initialization
and therefore remains robust for empirical acceptance curves. This
version costs𝑂(𝑁𝐺+𝑁log( 1/𝜀)) where𝐺 is the number of grid
points in the initial coarse search. The first term corresponds to
the global scan, while the second is due to the subsequent golden-
section refinement. Complete implementation details, including
pseudocode, correctness, boundary handling, and numerical valida-
tion, are provided in Appendix B.
5 Computational Evaluation
5.1 Design
We ask three questions: whether the numerical optimizer repro-
duces the structural results; how costly common restricted policies
are; and how sensitive the planner is to estimating𝐹 or misspecify-
ing seller dependence.
Parameters and policies.We normalize 𝜇= 1. The complete
analytic factorial crosses
𝑁∈{1,2,5,10,20,50}, 𝜎∈{.05,.15,.30,.45},
𝑉−𝜇∈{.1,.3,.5}, 𝐿∈{0,.1,.3},
𝜅∈{.001,.01,.03}, 𝛿∈{0,.02,.1},
for1944configurations. We compare jointCanowith: (i)Single-
agentOptimal (𝑚= 1, optimize𝑞), representing the traditional one-
to-one negotiation paradigm without parallelism; (ii)All-parallel
(𝑚=𝑁 , optimize𝑞), representing the strategy of launching every
available negotiation agent; (iii)Mean-cap( 𝑏=𝜇 , optimize𝑚),
representing a simple market-heuristic pricing rule with a fixed
procurement cap at the market mean; and (iv)Fixed-𝑞 (𝑞=. 8per
thread, optimize𝑚), representing a service-level heuristic that fixes
a conventional high per-thread acceptance target while adjusting
only concurrency. Every policy may immediately cancel. Because
these baselines restrict one or both decision dimensions, they quan-
tify the value of joint optimization. For each market configuration,
we define the regret of a restricted policy as
𝑅policy =max 𝑚∈{0,...,𝑁}
𝑞∈[0,1]
ΠCano(𝑚,𝑞)−Π policy,
where policy∈{Single-agent,All-parallel,Mean-cap,Fixed-𝑞}
and ΠCano(𝑚,𝑞) denotes the expected profit achieved by the pro-
posed joint optimizer. Regret therefore measures the opportunity
cost of restricting the feasible decision space, and the informative
outcome is its magnitude and location rather than the fact that it is
nonnegative. We additionally report the ratio of aggregate surplus
above−𝐿, the share of cells within one percent of the oracle surplus
(with a0.01scale floor near zero), and cancellation frequency. No
confidence interval is attached to the factorial sweep because it
exhausts the declared design rather than sampling configurations.
Main comparisons use analytic expected values and therefore
have no sampling interval. Reference runs use 2,049𝑞-values before
refinement; The factorial and regime-map runs use 257, estimation
and dependence runs use 513, and distributional and sensitivity
runs use 1,025. These resolutions were selected through prelimi-
nary convergence checks, balancing numerical accuracy against
computational cost; denser grids produced negligible changes in the

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xu and Zhu
10 20
Concurrent threads m
0.0
0.1
0.2
0.3
0.4
0.5
Optimal acceptance q ⋆ m
(a) Concession
10 20
Concurrent threads m
0.6
0.7
0.8
0.9
1.0
Price cap b ⋆ m
(b) Cap
10 20 30 40 50
Eligible sellers N
0.1
0.2
0.3
0.4
0.5
Price dispersion σ
(c) Joint policy m ⋆
q ⋆ = . 5
 2.5
5.0
7.5
10.0
12.5
15.0
17.5
threads
Figure 2: Structural predictions for 𝑉= 1.4,𝜇= 1,𝐿=. 2,𝜅=
.01,𝛿=. 05. (a–b) With 𝑁= 20,𝜎=. 30, the fixed-𝑚 acceptance
target and cap fall as concurrency grows; the dashed line
marks the joint optimum. (c) The joint policy over market
thickness and dispersion. The white contour marks 𝑞★ =. 5,
the sign boundary in Theorem 4.3.
resulting objective values while requiring substantially more eval-
uations. Empirical-quantile runs also include every interpolation
knot. Sixteen unit tests cover the expectation, marginal identity,
first-order condition, monotonicity, dispersion derivative, distribu-
tion inversion, cancellation, correlated extension, and agreement
with a 100,001-point exhaustive grid. A one-million-order Monte
Carlo run uses seed 20,260,803. Further details are in Appendix C.
5.2 Structural and Policy Results
Policy adaptation across market regimes.Figure 2 (a) and (b)
sweep the candidate concurrency level𝑚= 1,...,𝑁 . At each value
of𝑚, the planner holds 𝑚 fixed and solves the one-dimensional
problem𝑞★ 𝑚∈arg max 𝑞∈[0,1] Π(𝑚,𝑞) . Panel (a) plots the resulting con-
ditional optimum 𝑞★ 𝑚, whereas panel (b) expresses the same so-
lution in price units through 𝑏★ 𝑚 =𝐶(𝑞 ★ 𝑚). Thus, panel (b) is the
price-space representation of panel (a), rather than the result of a
separate optimization over𝑏. The vertical dashed line marks the
jointly optimal concurrency𝑚★, obtained by comparing Π(𝑚,𝑞 ★ 𝑚)
across all candidate thread counts and with immediate cancella-
tion. Panel (c) instead varies the market environment. Its horizontal
axis is the number of eligible sellers 𝑁 , and its vertical axis is
reservation-price dispersion𝜎. At each point(𝑁,𝜎) ,Canojointly
re-optimizes𝑚 and 𝑞; the color reports the resulting 𝑚★, with
darker colors indicating fewer threads and brighter colors indicat-
ing more. The stepwise color bands reflect the discreteness of𝑚★.
The white contour is the set of market configurations for which
the jointly optimized target satisfies𝑞★ =. 5. The higher-dispersion
side of the contour corresponds to 𝑞★ <. 5, whereas the lower-
dispersion side corresponds to𝑞★ >. 5. The point(𝑁,𝜎)=( 20,. 30)
in panel (c) is exactly the reference market shown in panels (a)
and (b): it yields (𝑚★,𝑞 ★,𝑏 ★)=( 13, 0.161, 0.648) and expected
profit0 .465. Although the optimal per-thread acceptance target
falls from𝑞★ 1 =. 539to 𝑞★ = 0.161, aggregate fulfillment rises to
𝑆𝑚★(𝑞★)=1−(1−𝑞 ★)𝑚★ ≈.898.
Figure 2 translates the structural results into an operating map.
Panels (a) and (b) show how the optimized per-thread acceptance
target and procurement cap adjust as concurrency increases, while
panel (c) identifies the market conditions under which broader par-
allel search becomes valuable. At low dispersion, the optimizer uses
Thin
low σ
Thick
low σ
Thin
high σ
Thick
high σ
0.0
0.1
0.2
0.3
0.4
0.5
Expected profit
(a) Economic objective
Thin
low σ
Thick
low σ
Thin
high σ
Thick
high σ
0.0
0.2
0.4
0.6
0.8
1.0
Fulfillment probability
(b) Reliability
CANO Single-agent All-parallel Mean-cap Fixed-q=0.8
Figure 3: Representative markets with 𝑁∈{ 3, 20} and𝜎∈
{.08,. 35}, holding𝑉= 1.4,𝐿=. 2,𝜅=. 01,𝛿=. 05. Joint optimiza-
tion matters most in dispersed markets. Higher reliability is
not free: Mean-cap and Fixed-𝑞 can fulfill more often while
earning less.
only a few relatively reliable threads because there is little lower-
tail value to exploit. As 𝑁 and𝜎 increase, optimal concurrency
generally rises but remains well below𝑁 ; The downward-sloping
𝑞★ =. 5contour further indicates that thicker markets can enter the
lower-tail-search regime at lower levels of dispersion. Managerially,
eligible sellers should therefore be treated as an option pool rather
than as a launch target: Broader search should be paired with tighter
price authority, and the buyer should choose between reliability
through concession and reliability through parallel lower-tail search
according to market thickness and the estimated reservation-price
distribution.
Profit–reliability trade-off.Figure 3 compares expected profit
in panel (a) and system-level fulfillment probability in panel (b)
across four representative(𝑁,𝜎) regimes. Policy differences widen
substantially as price dispersion increases. In the thick dispersed
market,Canoearns0 .519at 𝑚= 14,𝑞=. 151, compared with
0.090for Single-agent and0 .269for Mean-cap, even though All-
parallel and Mean-cap attain slightly higher fulfillment. Together,
the two panels show that higher reliability may be too costly when
achieved through excessive price concession or unnecessary con-
currency.Canoinstead selects the profit-maximizing reliability
level by balancing procurement price, fulfillment loss, thread cost,
and excess-commitment exposure.
Costs of restricted orchestration.Table 2 summarizes performance
over the full factorial and reveals two distinct costs of restricted
orchestration. Single-agent, All-parallel, Mean-cap, and Fixed- 𝑞
recover61 .4%,85 .7%,72 .7%, and44 .0%, respectively, ofCano’s
recoverable surplus, defined as aggregate profit above the immediate
cancellation payoff−𝐿. All-parallel is within one percent of the joint
solution in62.8%of configurations, but cancels in10 .9%because
launching all𝑁 threads can be worse than stopping, whereas Single-
agent is within one percent in only28.8%. The underlying regret
patterns clarify why. Single-agent leaves lower-tail search unused:
its mean regret rises from0 .016at 𝜎=. 05to0 .300at 𝜎=. 45,
and from zero at 𝑁= 1to0 .252at 𝑁= 50. All-parallel accesses
the lower tail but pays for threads it does not need, with mean
regret increasing from zero at 𝑁= 1to0 .211at 𝑁= 50. The

Parallelism or Concession? DAI ’26, November 29–December 2, 2026, Hong Kong, China
Table 2: Full-factorial policy summary over 1,944 analytic configurations. Surplus ratio aggregates profit above immediate
cancellation. Regret is in normalized profit units; “Near” is the share within 1% ofCano’s recoverable surplus; “Cancel” is the
share choosing𝑚=0.
Policy Surplus ratio Mean regret 90th-pct. regret Near (%) Cancel (%) Mean𝑚
Cano1.000 0.000 0.000 100.0 0.0 7.07
Single-agent 0.614 0.160 0.425 28.8 0.0 1.00
All-parallel 0.857 0.059 0.234 62.8 10.9 10.46
Mean-cap 0.727 0.113 0.319 8.5 0.0 2.96
Fixed-𝑞=.80.440 0.232 0.575 3.6 25.9 1.23
Table 3: Finite-data planning for 𝑁= 20,𝜇= 1,𝜎=. 35,𝑉=
1.4,𝐿=. 2,𝜅=. 01,𝛿=. 05. Each row uses 100 independent his-
tories; intervals are percentile bootstrap intervals for mean
oracle regret. Calibration is mean absolute acceptance error
at the selected cap.
𝑛Mean regret 95% interval Mean𝑚Calibration
25 .0686 [.0528, .0860] 12.56 .0591
50 .0251 [.0197, .0309] 12.95 .0337
100 .0220 [.0171, .0273] 13.53 .0306
250 .0092 [.0070, .0115] 14.06 .0173
1000 .0033 [.0027, .0041] 13.99 .0095
joint policy instead expands concurrency sublinearly: Averaged
over all other factors, mean𝑚★ rises from1.00at 𝑁= 1to17 .06at
𝑁= 50, while the corresponding mean target falls from𝑞★ =. 610to
.291. Aggregate fulfillment nevertheless increases from.610to .888,
showing that lower per-thread concession and higher system-level
reliability can coexist. These comparisons quantify the opportunity
cost of restricting the orchestration decision space; They do not
claim that deterministic optimization outperforms an unconstrained
learned policy.
5.3 Estimation and Dependence Stress Tests
We next study how estimation error affects planning by replacing
the true quantile function with an empirical quantile estimated from
𝑛∈{ 25, 50, 100, 250, 1000} historical reservation samples. For each
sample size, we generate 100 independent datasets and evaluate
the resulting policy under the true distribution. Mean oracle re-
gret decreases from0.0686(95% bootstrap interval [0.0528, 0.0860])
at𝑛= 25to0 .0033([0.0027, 0.0041]) at 𝑛= 1000, while mean
acceptance-calibration error falls from.059to .010. Thus, even an
estimated acceptance curve is sufficient for good planning, although
limited data can still lead to noticeably suboptimal concurrency
decisions. This experiment intentionally represents a favorable es-
timation setting because it directly observes sellers’ latent reserva-
tion thresholds. In practice, historical negotiation logs contain only
offer–response outcomes, so reservation thresholds are interval-
censored and may also be affected by the policies that generated
the data. Estimating b𝐹 in deployment therefore requires additional
modeling assumptions. Our results isolate only the effects of finite-
sample estimation error and integer policy decisions, leaving these
identification issues aside. Table 3 summarizes the finite-data re-
sults. Because each sample size uses independently regenerated
histories rather than nested datasets, the bootstrap intervals for
𝑛= 50and 𝑛= 100overlap, so their small difference should not be
interpreted as a monotone improvement. Nevertheless, increasing
the amount of historical data substantially reduces both planning
regret and acceptance-calibration error. The reported calibration
metric is local to the selected procurement cap and therefore does
not assess the accuracy of the entire estimated acceptance curve.
Estimation error is relatively modest compared with violating the
independence assumption. We therefore introduce an exchangeable
Gaussian copula while preserving every seller’s marginal accep-
tance distribution𝐹, where𝜌 denotes the latent correlation govern-
ing shared seller shocks. Complete model details are provided in
Appendix B.3. When𝜌=. 7, representing a strongly correlated mar-
ket, the policy planned under independence sees expected profit
fall from0.519to0 .042, whereas a correlation-aware planner re-
covers profit to0 .169by reducing concurrency from 𝑚= 14to
4and increasing the acceptance target from 𝑞=. 151to .363. As
𝜌 increases from.1to .7, the planner progressively selects fewer
but more accommodating negotiation threads, showing that pos-
itive dependence weakens the diversification benefit of parallel
negotiation: although each seller’s marginal acceptance probability
remains𝑞, fulfillment is no longer1−(1−𝑞) 𝑚.
Finally, the one-million-order Monte Carlo simulation differs
from the analytic expected profit by only 0.00040, within two Monte
Carlo standard errors, confirming the numerical correctness of the
analytical model. Appendix D reports the complete robustness anal-
yses, including alternative reservation-price distributions, copula-
based dependence models, parameter sensitivity analyses, and the
full performance curves.
5.4 What the Evaluation Establishes
The evaluation establishes that the proposed economic controller
behaves consistently with its theoretical predictions across the
declared design space. The numerical optimizer reproduces the
structural comparative statics, joint optimization consistently out-
performs common restricted policies across market regimes, and
the analytical objective closely matches Monte Carlo simulation.
Additional finite-data, distributional, and dependence experiments
demonstrate robustness to estimation error while identifying seller
dependence as the principal source of model misspecification. These
results validate the economic control layer rather than a complete
agentic procurement system. They do not establish LLM instruction
following, stationary seller behavior, or buyer profit as the appropri-
ate social objective. Our contribution is an auditable optimization

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xu and Zhu
policy and execution boundary that future end-to-end agent evalu-
ations can build upon, independent of any specific language model
or API version.
6 Limitations, Responsible Use, and Conclusion
6.1 Limitations
The model deliberately isolates a one-unit, single-cap procurement
problem with conditionally i.i.d. sellers and a risk-neutral expected-
profit objective.It does not model bundles, inventory, repeated in-
teraction, endogenous seller strategies, or dynamic bargaining. .
Acceptance curves must be learned from offer–response data rather
than listing prices, and seller heterogeneity, correlation, and legal
commitment differences are treated only through reduced-form ex-
tensions. We evaluate the economic controller, not LLM persuasion
quality.
The single negotiation window is essential.If failed negotiations
could be retried immediately at negligible cost, sequential launch
would weakly dominate parallel launch. Our results therefore apply
only when all negotiations must be initiated before terminal re-
sponses arrive. Multi-window settings require dynamic batch-size
decisions.
The common-cap abstraction treats all prices below 𝑏 as opera-
tionally equivalent.Real procurement may jointly optimize price,
delivery, warranty, or other contract attributes, and multiround
bargaining may settle below the cap. Extending the decision from
one scalar to multiple attributes would require multidimensional
acceptance models.
Finally, the factorial grid is designed to cover representative
market regimes rather than reflect their empirical frequency. Its
normalization enables relative comparisons but does not calibrate
𝜅 or𝛿 to currency units. Practical deployment therefore requires
parameter estimation, periodic recalibration, and robust fallbacks
under distribution shift.
6.2 Responsible Use
Parallel agents can amplify spam, bargaining power asymmetry,
deception, accidental commitments, and seller-contact externali-
ties. Deployments should therefore rate-limit seller contact, dis-
close automation where required, distinguish tentative from bind-
ing actions, enforce price caps outside the language model, main-
tain auditable logs, and provide human oversight for high-stakes
cases. Acceptance estimation should minimize personal data, while
seller-level rate limits and cooldowns should constrain 𝑁 before
optimization, and 𝜅 should reflect seller-attention costs as well
as computation. Applicable contract, consumer, privacy, and anti-
discrimination law always take precedence over economic objec-
tives.
6.3 Conclusion.
Agentic replication changes the economics of negotiation. Its ben-
efit is not simply a higher probability of agreement: Parallelism
permits lower per-conversation concession, but only until geomet-
ric fulfillment gains are overtaken by thread and commitment costs
at a fixed target.Canojointly re-optimizes the target and turns
that tradeoff into an auditable policy, and the dispersion sign re-
versal identifies when a varied market is an opportunity rather
than a liability. These results support a design principle for agentic
commerce: delegate language, but centrally optimize and enforce
economic authority.
References
[1] Samir Aknine, Suzanne Pinson, and Melvin F. Shakun. 2004. An Extended Multi-
Agent Negotiation Protocol.Autonomous Agents and Multi-Agent Systems8, 1
(2004), 5–45. doi:10.1023/B:AGNT.0000009409.19387.f8
[2] Bo An, Victor Lesser, and Kwang Mong Sim. 2011. Strategic Agents for Multi-
Resource Negotiation.Autonomous Agents and Multi-Agent Systems23, 1 (2011),
114–153. doi:10.1007/s10458-010-9137-2
[3] Tim Baarslag, Mark JC Hendrikx, Koen V Hindriks, and Catholijn M Jonker.
2016. Learning About the Opponent in Automated Bilateral Negotiation: A
Comprehensive Survey of Opponent Modeling Techniques.Autonomous Agents
and Multi-Agent Systems30, 5 (2016), 849–898.
[4] Pallavi Bagga, Nicola Paoletti, Bedour Alrayes, and Kostas Stathis. 2020. A Deep
Reinforcement Learning Approach to Concurrent Bilateral Negotiation.arXiv
preprint arXiv:2001.11785(2020).
[5] Federico Bianchi, Patrick John Chia, Mert Yuksekgonul, Jacopo Tagliabue, Dan
Jurafsky, and James Zou. 2024. How Well Can LLMs Negotiate? Negotiationarena
Platform and Analysis.arXiv preprint arXiv:2402.05863(2024).
[6] Tamara C. P. Florijn, Pinar Yolum, and Tim Baarslag. 2025. A Survey on One-
to-Many Negotiation: A Taxonomy of Interdependency. InProceedings of the
Thirty-Fourth International Joint Conference on Artificial Intelligence. 10436–10444.
doi:10.24963/ijcai.2025/1159
[7] Yao Fu, Hao Peng, Tushar Khot, and Mirella Lapata. 2023. Improving Language
Model Negotiation with Self-play and In-context Learning from AI Feedback.
arXiv preprint arXiv:2305.10142(2023).
[8] He He, Derek Chen, Anusha Balakrishnan, and Percy Liang. 2018. Decoupling
Strategy and Generation in Negotiation Dialogues. InProceedings of the 2018
Conference on Empirical Methods in Natural Language Processing. Association for
Computational Linguistics, 2333–2343. doi:10.18653/v1/D18-1256
[9] Nicholas R Jennings, Peyman Faratin, Alessio R Lomuscio, Simon Parsons, Carles
Sierra, and Michael Wooldridge. 2001. Automated Negotiation: Prospects, Meth-
ods and Challenges.International Journal of Group Decision and Negotiation10, 2
(2001), 199–215.
[10] Mike Lewis, Denis Yarats, Yann N. Dauphin, Devi Parikh, and Dhruv Batra. 2017.
Deal or No Deal? End-to-End Learning of Negotiation Dialogues. InProceedings
of the 2017 Conference on Empirical Methods in Natural Language Processing.
Association for Computational Linguistics, 2443–2453. doi:10.18653/v1/D17-1259
[11] Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao, Xin Chen, and David Simchi-
Levi. 2026. Strategic Bargaining in Multi-Buyer Markets: Reinforcement Learning
from Verifiable Rewards for LLM Negotiations.arXiv preprint arXiv:2607.05863
(2026).
[12] Shuze Daniel Liu, Claire Chen, Jiabao Sean Xiao, Lei Lei, Yuheng Zhang, Yisong
Yue, and David Simchi-Levi. 2026. Instructing LLMs to Negotiate Using Rein-
forcement Learning with Verifiable Rewards.arXiv preprint arXiv:2604.09855
(2026).
[13] Xianyang Liu, Shangding Gu, and Dawn Song. 2026. Agenticpay: A Multi-
agent LLM Negotiation System for Buyer-Seller Transactions.arXiv preprint
arXiv:2602.06008(2026).
[14] Thuc Duong Nguyen and Nicholas R Jennings. 2005. Managing Commitments in
Multiple Concurrent Negotiations.Electronic Commerce Research and Applications
4, 4 (2005), 362–376.
[15] Tian Xia, Zhiwei He, Tong Ren, Yibo Miao, Zhuosheng Zhang, Yang Yang, and
Rui Wang. 2024. Measuring Bargaining Abilities of LLMs: A Benchmark and A
Buyer-Enhancement Method. InFindings of the Association for Computational
Linguistics: ACL 2024. 3579–3602.
[16] Shenzhe Zhu, Jiao Sun, Yi Nian, Tobin South, Alex Pentland, and Jiaxin Pei.
2025. The Automated But Risky Game: Modeling and Benchmarking Agent-
to-Agent Negotiations and Transactions in Consumer Markets.arXiv preprint
arXiv:2506.00073(2025).

Parallelism or Concession? DAI ’26, November 29–December 2, 2026, Hong Kong, China
A Derivations and Complete Proofs
A.1 Expected Objective
For𝑚≥ 1, let𝐾= ˝𝑚 𝑖=1 1{𝑅𝑖≤𝑏} . Conditional on the product state,
𝐾∼Binomial(𝑚,𝑞), where𝑞=𝐹(𝑏). The realized payoff is
𝑈(𝐾)=
(
−𝐿−𝜅𝑚, 𝐾=0,
𝑉−𝑏−𝜅𝑚−𝛿(𝐾−1), 𝐾≥1.
The excess-commitment identity follows pointwise from(𝐾− 1)+ =
𝐾−1{𝐾≥1}:
E[(𝐾−1) +]=E[𝐾]−P(𝐾≥1)=𝑚𝑞−𝑆 𝑚(𝑞).
Therefore
E[𝑈(𝐾)]=(𝑉−𝑏)𝑆 𝑚(𝑞)−𝐿[1−𝑆 𝑚(𝑞)]−𝜅𝑚
−𝛿[𝑚𝑞−𝑆 𝑚(𝑞)]
=[𝑉+𝐿+𝛿−𝑏]𝑆 𝑚(𝑞)−𝐿−𝜅𝑚−𝛿𝑚𝑞.
Substituting𝑏=𝐶(𝑞)yields (3).
The convention𝑚= 0represents immediate cancellation after
the customer order has been accepted, soΠ( 0)=−𝐿 . For𝑚≥ 1,𝑞=
0, procurement fails surely andΠ(𝑚,0)=−𝐿−𝜅𝑚, weakly worse
than cancellation. For𝑞= 1when 𝐶( 1)<∞ , every launched thread
accepts and Π(𝑚, 1)=𝑉−𝐶( 1)−𝜅𝑚−𝛿(𝑚− 1); hence𝑚= 1
dominates larger concurrency at this boundary. For unbounded
support, no finite cap attains𝑞= 1; optimization is over𝑞∈[ 0, 1),
with the upper boundary interpreted by a limit.■
A.2 Proof of Proposition 4.1
Since
𝑆𝑚+1(𝑞)−𝑆 𝑚(𝑞)=𝑞(1−𝑞) 𝑚
and the expected acceptance count rises by𝑞, subtracting Π(𝑚,𝑞)
from Π(𝑚+ 1,𝑞) gives (4). Write𝐺(𝑞)=𝑉+𝐿+𝛿−𝐶(𝑞) . If𝐺(𝑞)> 0,
then
Δ𝑚+1(𝑞)−Δ 𝑚(𝑞)=−𝐺(𝑞)𝑞 2(1−𝑞) 𝑚 <0.
If𝐺(𝑞)≤ 0, the first term of(4) is nonpositive, soΔ𝑚(𝑞)≤−𝜅−𝛿𝑞≤
0. Thus, over positive integers, profit rises while Δ𝑚(𝑞)> 0, is flat
when Δ𝑚(𝑞)= 0, and falls after the marginal becomes negative.
Resolving a zero marginal toward the smaller thread count gives
the smallest𝑚 with Δ𝑚(𝑞)≤ 0; when no such𝑚<𝑁 exists, the
solution is𝑁.
For comparative statics, when𝐺(𝑞)>0,
𝜕Δ𝑚
𝜕𝑉 = 𝜕Δ𝑚 𝜕𝐿 =𝑞(1−𝑞) 𝑚 >0, 𝜕Δ𝑚 𝜕𝜅 =−1,
and
𝜕Δ𝑚
𝜕𝛿 =𝑞(1−𝑞) 𝑚−𝑞=−𝑞[1−(1−𝑞) 𝑚]≤0.
Moving every marginal in one direction moves its crossing thresh-
old weakly in the same direction. 𝑁 only truncates the resulting
threshold.■
A.3 Proof of Theorem 4.2
For compactness, set
𝐵(𝑞)=𝑉+𝐿+𝛿−𝐶(𝑞).
The first two derivatives of the fixed-𝑚objective are
Π′ 𝑚(𝑞)=−𝐶 ′(𝑞)𝑆𝑚(𝑞)+𝐵(𝑞)𝑆 ′ 𝑚(𝑞)−𝛿𝑚,
Π′′ 𝑚(𝑞)=−𝐶 ′′(𝑞)𝑆𝑚(𝑞)−2𝐶 ′(𝑞)𝑆′ 𝑚(𝑞)+𝐵(𝑞)𝑆 ′′ 𝑚(𝑞).
On the interval in Assumption 1,𝑆′ 𝑚(𝑞)=𝑚( 1−𝑞)𝑚−1 > 0,𝑆′′ 𝑚(𝑞)≤
0,𝐵(𝑞)≥ 0,𝐶′(𝑞)> 0, and𝐶′′(𝑞)≥ 0. Hence Π′′ 𝑚(𝑞)< 0, proving
strict concavity and uniqueness.
At an interior optimum, Π′ 𝑚(𝑞)= 0. Dividing by𝑆′ 𝑚(𝑞)=𝑚( 1−
𝑞)𝑚−1 gives
𝑉+𝐿+𝛿−𝐶(𝑞)=𝐶 ′(𝑞)𝐴𝑚(𝑞)+𝛿(1−𝑞) −(𝑚−1) .
Rearrangement yields (6).
It remains to compare roots. Let
𝐻𝑚(𝑞)=𝐶(𝑞)+𝐶 ′(𝑞)𝐴𝑚(𝑞)+𝛿[(1−𝑞) −(𝑚−1) −1].
For fixed𝑞∈(0,1), write𝑟=1−𝑞. Then
𝐴𝑚(𝑞)= 𝑞 𝑚 𝑚−1∑︁ 𝑗=0 𝑟−𝑗.
The sequence1 ,𝑟−1,𝑟−2,... is strictly increasing, so appending
its next term raises its running average: 𝐴𝑚+1(𝑞)>𝐴 𝑚(𝑞). The
commitment term is also nondecreasing in 𝑚. Thus 𝐻𝑚+1(𝑞) ≥
𝐻𝑚(𝑞).
For fixed𝑚,𝐴𝑚(𝑞) is strictly increasing because both𝑞 and every
𝑟−𝑗 are nondecreasing and the 𝑗= 0term makes the product strict.
Together with𝐶′ > 0,𝐶′′≥ 0, this makes𝐻𝑚(𝑞) strictly increasing.
Since both optima solve𝐻𝑚(𝑞)=𝑉+𝐿,
𝑞★ 𝑚+1≤𝑞 ★ 𝑚.
Finally𝐶 is increasing, so the same inequality holds for the caps. ■
A.4 Proof of Theorem 4.3
For fixed𝑚, only the quantile curve in(3) depends on𝜎. At a unique
optimum, the envelope theorem gives
𝑑Π ★ 𝑚(𝜎)
𝑑𝜎 =− 𝜕𝐶𝜎(𝑞★ 𝑚) 𝜕𝜎 𝑆𝑚(𝑞★ 𝑚)=−𝑧(𝑞 ★ 𝑚)𝑆𝑚(𝑞★ 𝑚).
Because𝑆𝑚(𝑞)> 0for 𝑞> 0and symmetry implies 𝑧(𝑞)< 0below
1/2,𝑧( 1/2)= 0, and𝑧(𝑞)> 0above1/2, the three sign cases follow.
If a positive joint optimizer over𝑚 is unique in a neighborhood of
𝜎 and its fixed-𝑚 solution remains unique and interior, the same
envelope derivative applies to the active𝑚. At an integer switch,
the upper envelope of the fixed-𝑚 value functions is continuous
but need not be differentiable.■
BCanoAlgorithm and Extensions
B.1 Planner Output and Failure Behavior
The planner receives a market instance containing(𝑁,𝑉,𝐿,𝜅,𝛿)
together with the estimated quantile function𝐶(𝑞) . It returns either
a cancellation decision or an optimal policy tuple
(𝑚★,𝑞 ★,𝑏 ★),
while fulfillment and commitment metrics are evaluated separately
by a deterministic evaluator.
The implementation first performs a bounded global search over
𝑞∈[ 10−6, 1− 10−6], followed by golden-section refinement around
the best candidate. For finite-support distributions, the boundary

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xu and Zhu
point𝑞= 1is additionally checked. The resulting policy is finally
compared with immediate cancellation, and cancellation is selected
whenever every positive-concurrency policy yields a lower ex-
pected value than−𝐿.
On a reference uniform instance, the implementation matches
an exhaustive 100,001-point grid search to within10−8. This serves
as a regression check rather than a universal optimality guaran-
tee. Theoretical global optimality remains guaranteed only under
Assumption 1. Implementation details are provided in the following.
B.2 Algorithm
For each𝑚∈{1,...,𝑁},Canoperforms:
(1) Construct𝑞 𝑔 =𝑞+𝑔(𝑞−𝑞)/(𝐺−1)for𝑔=0,...,𝐺−1.
(2) Evaluate Π(𝑚,𝑞𝑔) and retain the best cell and both neighbors.
(3) Refine that bracket by golden-section maximization to toler-
ance𝜀, also checking global endpoints.
(4) Convert the best𝑞 𝑚 to𝑏𝑚 =𝐶(𝑞 𝑚)and record its value.
It returns the best recorded positive-𝑚 policy unless cancellation
−𝐿 is larger. Under Assumption 1, Step 1 may be replaced by bound-
ary derivative checks and bisection of (6). Strict concavity proves
global correctness, while bisection needs𝑂(log( 1/𝜀)) evaluations
for each𝑚. The global-scan implementation is intentionally more
conservative for empirical curves.
B.3 Correlated Sellers
The i.i.d. theory does not apply when seller reservation prices share
shocks. For the stress test, let latent acceptance variables follow an
exchangeable Gaussian copula:
𝑍𝑖 =√𝜌𝑍 0+ √︁ 1−𝜌𝜖 𝑖,
where all normal factors are independent and a seller accepts when
𝑍𝑖≤Φ−1(𝑞). Conditional on𝑍 0 =𝑧, acceptance probability is
𝑝𝑞(𝑧)=Φ

Φ−1(𝑞)− √𝜌𝑧
√1−𝜌
!
.
Consequently,
𝑆𝜌 𝑚(𝑞)=1−E 𝑍0[(1−𝑝 𝑞(𝑍0))𝑚].
Marginal acceptance remains𝑞, so E[𝐾]=𝑚𝑞 and the objective
retains the form
Π𝜌(𝑚,𝑞)=[𝑉+𝐿+𝛿−𝐶(𝑞)]𝑆 𝜌 𝑚(𝑞)−𝐿−𝜅𝑚−𝛿𝑚𝑞.
We evaluate the one-dimensional expectation with 32-node Gauss–
Hermite quadrature, enumerate𝑚, and maximize over a 513-point
𝑞-grid. Positive dependence lowers the diversification benefit of con-
currency, explaining the shift toward fewer, more accommodating
threads.
C Additional Experimental Detail
C.1 Full Protocol
All results are generated by one Python script using NumPy and
Matplotlib. The main seed is 20,260,803. Analytic rows, figures, and
LaTeX result macros are written from the same run. The imple-
mentation contains separate modules for distributions, the profit
model, optimization, correlation, and simulation. No proprietary
data, model API, or human-subject data are used.
102 103
Observed threshold samples
0.00
0.02
0.04
0.06
0.08
Mean oracle regret
(a) Estimation
0.0 0.2 0.4 0.6
Latent Gaussian correlation ρ
0.1
0.2
0.3
0.4
0.5
Expected profit
(b) Dependence
Independence-planned
Correlation-aware
Unif. Trunc. Logn. Mix.
0.0
0.1
0.2
0.3
0.4
0.5
Expected profit
(c) Shape
CANO Single-agent All-parallel Mean-cap Fixed-q=0.8
Figure 4: Stress tests. (a) Mean regret and 95% bootstrap in-
terval over 100 finite-data replicates. (b) Correlation-aware
planning partially recovers profit lost under shared seller
shocks. (c) Policy profit under uniform, truncated-normal,
lognormal, and two-component reservation-price distribu-
tions.
Table 4: Factorial design for the1944analytic markets.
Parameter Values
𝑁1,2,5,10,20,50
𝜎/𝜇 .05,.15,.30,.45
𝑉−𝜇 .10,.30,.50
𝐿0,.10,.30
𝜅 .001,.01,.03
𝛿0,.02,.10
The primary metrics are expected profit, fulfillment probabil-
ity, cap, concurrency, expected excess commitments𝑚𝑞−𝑆 𝑚(𝑞),
duplicate probability
P(𝐾≥2)=1−(1−𝑞) 𝑚−𝑚𝑞(1−𝑞) 𝑚−1,
and absolute regret. Fixed-𝑞=. 7and .9sensitivities, as well as
one-factor sweeps in𝑉,𝐿,𝜅,𝛿, are included in the raw output.
C.2 Monte Carlo Validation
For 𝑁= 20,𝜇= 1,𝜎=. 35,𝑉= 1.4,𝐿=. 2,𝜅=. 01,𝛿=. 05,
Canoselects 𝑚= 14,𝑞=. 15097,𝑏=. 57682. Analytic expected
profit is0.518956. Across one million independent orders, simulated
mean profit is0.519354with standard error0 .000293; absolute error
is0.000397. Simulated fulfillment and duplicate probabilities are
0.89924and0.64661.
D Robustness Results
D.1 Distribution Shape
Table 5 reports the policies underlying Figure 4(c). All four distri-
butions have mean one and standard deviation approximately0.30.
The truncated normal is symmetric at three underlying standard
deviations. The two-component market contains a low-price seg-
ment and a smaller high-price segment; its quantile is represented
by 100,000 fixed-seed draws and captures unobserved seller-type
heterogeneity. Because some shapes violate the convex-quantile
condition globally, the bounded grid scan followed by local refine-
ment is used throughout.

Parallelism or Concession? DAI ’26, November 29–December 2, 2026, Hong Kong, China
Table 5: Distribution robustness:𝑚,𝑞, and expected profit.
Uniform Trunc. normal
Policy𝑚,𝑞Profit𝑚,𝑞Profit
Cano13,.161.46515,.134.421
Single1,.539.0921,.627.105
All20,.117.44420,.106.412
Mean-cap4,.500.2694,.500.269
Fixed-.82,.800.0252,.800.079
Lognormal Mixture
Policy𝑚,𝑞Profit𝑚,𝑞Profit
Cano11,.187.4065,.429.477
Single1,.641.1331,.540.215
All20,.115.37720,.133.360
Mean-cap3,.558.2803,.550.278
Fixed-.82,.800.1072,.800.003
D.2 Parameter Comparative Statics
The numerical one-factor sweeps agree with Proposition 4.1. In the
reference uniform market, raising𝜅 from .001 to .06 reduces 𝑚★
from 20 to 4 and raises𝑞★ from .117 to .325. Raising𝛿 from 0 to .20
reduces𝑚★ from 15 to 9 and expected excess commitments from
1.659 to .637. Raising𝐿 from 0 to .60 increases concurrency from
12 to 14 and fulfillment from .869 to .929. Because𝐿 also appears
in the failure payoff, reported profit need not increase with𝐿; the
policy nevertheless becomes more reliable as predicted.
D.3 Scope of the Agentic Evaluation
The experiment targets the economic control layer shown in Fig-
ure 1. It samples seller acceptance and commitment outcomes but
does not call an LLM, measure rhetoric, or compare prompts. Ac-
cordingly, no claim in the paper attributes profit improvements to
language generation. A future controlled LLM evaluation should
pair identical market seeds, seller messages, and model snapshots;
distinguish attempted from executed cap violations; and report
token use, latency, and prevented duplicate commitments. The cur-
rent results establish the policy that such a language layer should
be constrained to execute.
