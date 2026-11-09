---
title: 'Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller
  Allocation'
url: https://arxiv.org/abs/2610.31701
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Nan Wang
- Mitchell Turiel
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.31701
pages: 7
chars: 35118
fetched_at: '2026-11-08T13:35:35+00:00'
kb_version: 1
---

# Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller Allocation

Tradeoff-Aware Territory Design: A Multi-Objective Decision
System for Enterprise Customer-to-Seller Allocation
Nan (Iris) Wang
Databricks
San Francisco, CA, USA
nan.wang@databricks.com
Mitchell Turiel
Databricks
San Francisco, CA, USA
mitchell.turiel@databricks.com
Abstract
Enterprise customer journeys are shaped not only by product expe-
riences and marketing interventions, but also by recurring human-
resource allocation decisions. In B2B go-to-market (GTM) organiza-
tions, these decisions are operationalized through territory carving:
the recurring process of selecting which accounts receive seller
coverage, preserving valuable seller-account relationships, and al-
locating limited field capacity across heterogeneous opportunities.
Despite its strategic importance, territory carving often remains
manual and expertise-driven, making it difficult to compare account
opportunities consistently, quantify the value of continuity, or rea-
son transparently about tradeoffs among growth, balance, capacity,
and operational feasibility.
We present a production decision system for tradeoff-aware
customer-to-seller allocation in enterprise GTM planning. The sys-
tem combines three analytical components: a multidimensional
account-value layer that scores customer opportunity from multi-
ple predictive signals; an observational continuity-valuation layer
that estimates the expected cost of breaking existing account-seller
relationships using a synthetic-control-style counterfactual frame-
work; and a multi-objective optimization layer that prioritizes high-
value accounts for seller coverage while balancing continuity value,
opportunity balance, and operational constraints.
The framework has been deployed as a scenario-based decision-
support system for enterprise territory planning. Historical back-
testing shows that optimizer-generated scenarios can substantially
raise assignment compliance while preserving comparable seller-
level opportunity distribution. In production planning use, adopted
scenarios improved both assignment compliance and opportunity
balance relative to the prior planning baseline. Beyond these gains,
directing scarce seller coverage toward higher-value accounts rep-
resents a meaningful incremental revenue opportunity at enterprise
scale. The central contribution is less any single component than the
framework it enables: one that makes these tradeoffs explicit and
inspectable, turning territory carving into a governable decision
surface.
CCS Concepts
•Applied computing → Multi-criterion optimization and
decision-making; Marketing;•Mathematics of computing →
Mixed discrete-continuous optimization;Time series analysis;•Com-
puting methodologies→Classification and regression trees.
Keywords
territory planning, multi-objective optimization, mixed-integer pro-
gramming, account scoring, continuity valuation, synthetic control,
causal inference, go-to-market analytics
1 Introduction
In enterprise B2B go-to-market planning, customer-to-seller al-
location is a recurring mechanism through which organizations
shape the customer journey. Territory planning determines which
accounts receive seller coverage, which relationships are preserved,
and how scarce field capacity is allocated for the next planning
period. In large enterprise GTM organizations, this process can
involve many accounts, sellers, stakeholder groups, business rules,
and capacity constraints. Because these decisions must ultimately
result in concrete assignments, territory carving requires a decision
system that can produce feasible, inspectable recommendations.
Territory carving is often distributed and expertise-driven. Busi-
ness leaders make account-level decisions using domain knowledge,
local context, and planning judgment. While this captures impor-
tant business context, it also creates structural challenges. First,
the account universe may be too large for comprehensive manual
inspection. Second, account value is heterogeneous and only par-
tially observed, making it difficult to form a shared value system.
Third, account-to-seller assignment is globally coupled: assigning
one account to one seller consumes capacity, changes opportunity
distribution, affects relationship continuity, and constrains the re-
maining feasible assignment space. Fourth, scenario comparison is
difficult when each alternative plan must satisfy many interacting
business rules. As a result, planners have limited ability to compare
tradeoffs among account value, continuity, opportunity balance,
and operational feasibility.
Sales-territory design has long been studied as an alignment
and resource-allocation problem, often using integer programming,
heuristic optimization, or contribution-aware formulations to bal-
ance workload, opportunity, geography, and operational feasibil-
ity [7–9]. We extend this literature by treating continuity as an
empirically estimated, account-varying value rather than a fixed
movement penalty, and by making heterogeneous account value
directly usable in constrained optimization.
This paper presents a decision-system framework for tradeoff-
aware territory design. The system prioritizes high-value accounts
through an optimization-ready account-value measure, estimates
the value of seller-account continuity using a counterfactual hand-
off design, and integrates these signals into a constrained opti-
mization model for account-to-seller assignment. The resulting
framework supports scenario-based planning: decision makers can
start from feasible recommendations, inspect the tradeoffs they
encode, and apply business judgment to exceptions. More than a
particular model or solver, the contribution is a reframe: territory
carving becomes an inspectable decision problem in which hetero-
geneous account value is represented through a common planning
arXiv:2610.31701v1  [cs.AI]  21 Oct 2026

Nan (Iris) Wang and Mitchell Turiel
Figure 1: Overall framework for data-driven territory carving.
currency and seller continuity is treated as an empirically measured
tradeoff rather than an intuitive preference.
2 Problem Formulation
Territory carving is not simply an account-ranking problem or a
standalone assignment problem. Each account-to-seller decision
has several coupled consequences: it determines whether an ac-
count receives seller coverage, consumes seller capacity, changes
the distribution of opportunity across sellers, and may preserve
or break an existing seller-account relationship. A useful decision
system must therefore produce feasible assignments while making
the underlying tradeoffs inspectable to planners.
Figure 1 summarizes the end-to-end framework and provides
the roadmap for the rest of the paper. We formulate territory carv-
ing as a constrained account-to-seller assignment problem whose
output is a feasible assignment plan. The optimization is driven by
two upstream decision inputs: an account-value input𝑄𝑖, produced
by the scoring layer to make heterogeneous accounts comparable
for planning, and a continuity input 𝐶𝑖, interpreted as the value
of preserving an incumbent seller-account relationship or, equiv-
alently, the avoided cost of a handoff. Section 3 describes how𝑄𝑖
is constructed; Section 4 describes how𝐶𝑖 is estimated; Section 5
combines these inputs in a multi-objective optimization model that
generates feasible plans while navigating a tradeoff surface across
opportunity capture, continuity preservation, balance, and reas-
signment cost [4, 6, 7]; and Section 6 evaluates the resulting plans
using plan-quality metrics rather than solver objective value alone.
Let𝐼 denote the set of customer accounts and𝐽 denote the set of
sellers. Territory carving assigns accounts to sellers for a planning
period, typically the next fiscal year. We define a binary decision
variable𝑥 𝑖 𝑗 indicating whether account𝑖is assigned to seller𝑗:
𝑥𝑖 𝑗 =
(
1,if account𝑖is assigned to seller𝑗,
0,otherwise. (1)
Each account𝑖∈I is characterized by account value𝑄𝑖, work-
load weight𝑎𝑖, eligibility conditions, and, when applicable, incum-
bent ownership. Each seller 𝑗∈J has capacity bounds and cover-
age eligibility.
We model territory design as a multi-objective optimization
problem in which account value rewards opportunity capture, con-
tinuity value rewards relationship preservation, and balance and
movement penalties discourage uneven opportunity distribution
and unnecessary reassignment.
3 Account Value Quantification
A central challenge in territory planning is that account value is
multi-dimensional and not directly observable. Current revenue
may favor mature customers while understating emerging growth
opportunities. Product usage may reflect realized engagement but
not necessarily long-term commercial potential. Firmographic and
technographic signals may indicate strategic fit, but require cali-
bration before they can support account-level planning decisions.
To create a shared planning currency, we use a scoring frame-
work that decomposes account value into performance, potential,
and propensity. For each account𝑖, we define the account value as
𝑄𝑖 =𝑓

𝑃 perf 𝑖 , 𝑃pot 𝑖 , 𝑃prop 𝑖 , 𝑃fit 𝑖 , 𝑃eng 𝑖 , ...  .(2)
where𝑃 perf 𝑖 captures realized business trajectory;𝑃 pot 𝑖 captures
long-term account opportunity, including total addressable market
and other structural indicators; 𝑃 prop 𝑖 captures the likelihood of
near-term growth or expansion within the planning horizon;𝑃 fit 𝑖
captures strategic and firmographic fit; and𝑃 eng 𝑖 captures account
engagement, among other signals used in the composite. Predictive

Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller Allocation
account scoring and customer-value modeling are widely used to
prioritize scarce sales and marketing resources [3, 5]. In our setting,
the score is designed not only for ranking accounts, but also as an
optimization input for comparing heterogeneous account types.
In implementation,𝑓(·) is a weighted composite of model-based
scores, calibrated with planning heuristics and business priorities
for the specific planning use case. The goal is not only prediction
accuracy, but decision usefulness: the score must be comparable
across accounts, interpretable to stakeholders, and stable enough to
support territory design. By translating heterogeneous signals into
a common account-value measure, the scoring framework reduces
reliance on subjective prioritization and enables more consistent
organizational planning decisions.
4 Continuity Valuation Using a
Synthetic-Control-Style Counterfactual
Seller-account continuity is an important but historically under-
quantified dimension of territory design. Territory carving may
reassign an account from an incumbent seller to a new seller be-
cause of capacity rebalancing, seller movement, or GTM redesign.
While such handoffs may be operationally necessary, they can also
disrupt accumulated account context and slow post-carve consump-
tion growth. In many planning processes, continuity is treated as an
intuitive preference rather than an empirically calibrated tradeoff.
We frame a seller-account handoff as a treatment event and
estimate its effect on post-carve consumption using a synthetic-
control-style counterfactual framework [1, 2]. Let𝐷𝑖 = 1indicate
that account 𝑖 experienced a seller handoff during the territory
carve, and let 𝑌𝑖,𝑡 denote weekly consumption for account 𝑖 at
time𝑡. The causal estimate is the post-carve consumption impact
for handed-off accounts relative to the counterfactual condition
of continued seller coverage. In other words, the counterfactual
represents what consumption would have been for treated accounts
had the seller handoff not occurred.
Because this counterfactual is not observed, we construct an
estimated no-handoff trajectory from comparable accounts that
retained seller continuity. Donor accounts are selected based on
pre-carve similarity in account characteristics and consumption
trajectory, including spend tier, trailing consumption, and tenure.
The synthetic trajectory is calibrated on the pre-carve period and
then projected into the post-carve period. Let𝑌 obs 𝑡 denote observed
post-carve consumption for the treated cohort, and let ˆ𝑌 0 𝑡 denote
the estimated counterfactual consumption under continued seller
coverage. The estimated handoff effect at time𝑡is
𝜏 handoff 𝑖,𝑡 =𝑌 𝑖,𝑡− b𝑌 0 𝑖,𝑡.(3)
Aggregating over the post-planning horizonT𝑝𝑜𝑠𝑡 gives an account-
level estimate of the handoff impact:
b𝜏handoff 𝑖 = 1 |T𝑝𝑜𝑠𝑡| ∑︁ 𝑡∈T𝑝𝑜𝑠𝑡 𝜏 handoff 𝑖,𝑡 .(4)
If handoffs reduce account performance, b𝜏handoff 𝑖 is negative. We
can therefore define the estimated value of preserving continuity
as the avoided disruption from a handoff:
𝐶𝑖 =−b𝜏handoff 𝑖 .(5)
Figure 2: Continuity valuation using a synthetic-control-
style counterfactual.
Figure 2 illustrates the counterfactual design: the observed post-
carve trajectory is compared against a synthetic no-handoff trajec-
tory estimated from comparable continuity-preserved accounts. To
reduce the risk of attributing residual counterfactual error or com-
mon time-period effects to seller handoff, we adjust the estimated
handoff effect using placebo effects from continuity-preserved ac-
counts.
An empirical continuity study of a recent carve shows that seller
handoffs are associated with lower post-carve consumption. Across
more than thousands of treated accounts, handed-off accounts con-
sistently underperformed their synthetic no-handoff counterfactual
over the following year. The estimated average treatment effect
on the treated (ATT) is negative and statistically significant, and
remains so after placebo adjustment, with the confidence interval
excluding zero. The effect varies materially across account groups:
faster-growing accounts show a roughly threefold larger estimated
decline than more established ones, and disruption is clearer in
some business units and account segments than others. This het-
erogeneity is the central planning insight: continuity should be
modeled as a differentiated business tradeoff rather than a flat re-
assignment penalty, preserving seller-account relationships where
disruption is expected to be costly while allowing reassignment
where planning benefits outweigh the estimated continuity cost.
These estimates are observational. Seller handoffs are not ran-
domly assigned: they arise from capacity rebalancing, seller move-
ment, and GTM redesign, any of which may correlate with an
account’s trajectory. The estimate is therefore causal only under
the assumption that the synthetic trajectory—built from continuity-
preserved donors matched on spend tier, trailing consumption,
and tenure—approximates what a handed-off account would have
done absent the handoff. The placebo adjustment removes com-
mon time-period effects and residual counterfactual error estimated
on untreated accounts, but it does not correct for selection into
handoff on unobservables that differ between handed-off and re-
tained accounts, nor for spillovers if reassigning one account shifts
a seller’s attention to others (a SUTVA violation). We therefore

Nan (Iris) Wang and Mitchell Turiel
read the ATT as a directional, assumption-conditional estimate of
handoff disruption rather than a randomized identification.
5 Multi-Objective Territory Optimization
The optimization layer converts account value and continuity valu-
ation into feasible account-to-seller recommendations under the
constraints and tradeoffs. A key design challenge is calibration
across objectives: account value, continuity, balance, and opera-
tional feasibility are not naturally expressed in the same unit. Rather
than converting all terms into short-term dollars, we use account
value as the optimization currency, allowing the objective to reflect
both near-term commercial opportunity and long-term strategic
potential. Continuity enters as an empirically estimated adjustment
to the account value, so the penalty for reassignment can vary
between account types.
The weighted objective can be interpreted as an inspectable
scalarization of competing planning goals, a common approach in
multi-objective optimization when decision makers need to com-
pare feasible tradeoffs across objectives [6]. LetI denote the set of
accounts andJ denote the set of sellers. LetP denote the set of fea-
sible account-seller assignment candidates, where each candidate
𝑝∈P corresponds to assigning account 𝑖(𝑝) to seller 𝑗(𝑝) . The
decision variable𝑥𝑝 equals 1 if assignment candidate𝑝 is selected
and 0 otherwise.
The purpose of the optimizer is not to claim that there is a single
universally correct territory plan. Instead, the weighted objective
generates inspectable points on a planning tradeoff surface. By
varying the weights on account value, continuity, balance, and
operational feasibility, planners can compare feasible scenarios
and select an operating point that reflects current business pri-
orities. This is especially important in territory carving because
improvements along one dimension often require concessions along
another: a plan may improve opportunity balance by reassigning
more accounts, or preserve continuity by accepting less balance
improvement. We use the following compact objective to expose
the main territory-design tradeoffs:
max
𝑥
∑︁
𝑝∈P
𝛼𝑞𝑝𝑥𝑝
|      {z      }
Account value
+
∑︁
𝑝∈P
𝛽𝑐𝑝𝑥𝑝
|      {z      }
Continuity
−𝜆Bal(𝑥)
|   {z   }
Opportunity balance
+
∑︁
𝑝∈P
𝛾𝑘 𝑝𝑥𝑝
|      {z      }
Intent-to-Keep
−𝛿
∑︁
𝑗∈J
𝑟 𝑗
|  {z  }
Shortfall
−𝜇Φ op(𝑥) |    {z    }
operational feasibility
.
(6)
Here,𝑞𝑝 =𝑄 𝑖(𝑝) is the account-value value from the scoring
framework for the account in candidate assignment𝑝. The conti-
nuity term𝑐𝑝 is estimated separately from account value and trans-
lated into the same account-value currency used by the optimizer. It
captures the avoided value loss from preserving seller-account con-
tinuity, with the magnitude varying by account segment, spend tier,
or business unit based on the estimated handoff disruption. Thus,
continuity enters the objective as an empirically calibrated, hetero-
geneous adjustment rather than as a flat reassignment penalty.
The balance penalty measures deviation from seller-level oppor-
tunity targets:
Bal(𝑥)=
∑︁
𝑗∈J

 ∑︁ 𝑝∈P 𝑗(𝑝)=𝑗 𝑞𝑝𝑥𝑝−𝑇 𝑗

 .(7)
The objective is optimized subject to hard GTM feasibility con-
straints. Each account can be assigned to at most one seller:
∑︁
𝑝∈P
𝑖(𝑝)=𝑖
𝑥𝑝≤1,∀𝑖∈I.(8)
The intent-to-keep value𝑘𝑝 is used in production re-optimization
to preserve explicit planning edits made during the current plan-
ning cycle. When field leaders adjust an assignment after review-
ing an optimized scenario, the next optimization run treats that
edit as planning intent rather than as noise to be reverted. This
term is distinct from continuity: continuity preserves pre-existing
seller-account relationships, while intent-to-keep preserves expert-
reviewed assignment decisions made during the iterative planning
process. The weight𝛾 controls how strongly the optimizer respects
these edits relative to account value, continuity, balance, and other
operational objectives.
Minimum workload or coverage requirements are modeled with
a nonnegative shortfall variable:
∑︁
𝑝∈P
𝑗(𝑝)=𝑗
𝑎𝑖(𝑝)𝑥𝑝+𝑟 𝑗≥𝐿 𝑗, 𝑟 𝑗≥0,∀𝑗∈J.(9)
Locked assignments are preserved when required by business
rules. LetPlock denote the set of locked assignment candidates.
Then:
𝑥𝑝 =1,∀𝑝∈P lock.(10)
This formulation separates strategic objectives from feasibility
requirements. The objective defines the tradeoff surface across ac-
count value, continuity, balance of opportunities, and coverage,
while the constraints enforce the operating rules under which the
territory plan must be valid. This structure makes each recommen-
dation inspectable: a proposed territory plan can be decomposed
into the account value it captures, the continuity it preserves, the
balance impact it creates, and the feasibility constraints it satisfies.
Table 1 illustrates this tradeoff surface. The selected production
scenario captures most of the observed imbalance reduction rela-
tive to the deployed baseline plan. Moving to more balance-heavy
scenarios adds less than one percentage point of additional imbal-
ance reduction, but requires 10–19% more account reassignment.
Conversely, more continuity-heavy scenarios reduce reassignment
but leave substantially more imbalance unresolved. We therefore
operate near the knee of the tradeoff surface: preserving most of the
balance gain while avoiding unnecessary movement and continuity
disruption.

Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller Allocation
Table 1: Scenario frontier on the backtest. Imbalance reduc-
tion is measured against the deployed baseline plan; account
reassignment is measured against the selected production
scenario.
Balance gain Continuity break
vs deployed plan vs production
Continuity heavier 34% -46%
Continuity heavy 71%−10%
Production (selected) 94% 0% (ref.)
Balance heavy 95% +10%
Balance heavier 95% +19%
6 Evaluation
We evaluate the framework using two complementary views: his-
torical backtesting and production plan-quality outcomes. The his-
torical backtest assesses whether the core optimization engine can
improve territory-plan quality under comparable planning con-
straints. The production comparison assesses whether adopted
plans improved after the decision system was embedded into the
latest planning workflow. Across both views, we focus on plan-
quality metrics rather than solver objective value alone, because a
useful territory plan must be feasible, balanced, interpretable, and
operationally usable.
For the historical backtest, we use the previously deployed plan-
ning snapshot as the expert-carved baseline and rerun the opti-
mizer using only planning-time information, including the same
assignment universe, eligibility rules, locked-account constraints,
and capacity bounds available during the original planning cy-
cle. This isolates the plan-quality impact of optimizer-generated
scenarios under comparable operating conditions. The adaptive
re-optimization workflow described in Section 7 is not simulated
in this backtest; it is assessed through the observed production
planning outcome.
We assess optimizer output using a plan-quality scorecard rather
than solver objective value alone. The scorecard captures the ex-
ternal business properties required for a useful territory design:
compliance with planning rules, capture of high-value accounts, op-
portunity balance across sellers, preservation of valuable continuity,
limited account movement, and solver stability within planning
runtime constraints. Table 2 summarizes these evaluation dimen-
sions.
The optimizer improves assignment compliance by 78% (Figure 3)
and produces a modestly more balanced opportunity distribution
while preserving comparable seller attainment, with mean attain-
ment essentially unchanged (Figure 4). These results indicate that
the optimizer improves the feasibility and balance of opportunities
without materially distorting the expected seller opportunity under
a four-hour solver runtime.
The backtest also estimates the opportunity-value channel from
account prioritization. Using the same historical planning snapshot,
we compare the account value captured by the optimized plan
against the deployed expert-carved plan under comparable coverage
capacity. By directing scarce seller coverage toward accounts with
higher account values, the optimized plan captures a measurably
Table 2: Optimizer output evaluation dimensions.
Evaluation area What it assesses
Compliance Adherence to eligibility, locked assign-
ments, capacity limits, and business rules.
Account value Capture of higher-quality accounts in rec-
ommended territories.
Balance Distribution of opportunity across sellers.
Continuity Preservation of valuable account-seller re-
lationships.
Movement Level of account reassignment and opera-
tional disruption.
Solver stability Reliability of solutions within planning
runtime constraints.
Figure 3: Backtest comparison of optimizer-generated and
historical territory plans on compliance rate.
Figure 4: Comparison of seller attainment distribution under
optimizer-generated and historical territory plans.
higher share of total account value than the deployed expert-carved
plan under comparable coverage capacity. We interpret this as
a directional backtest-based opportunity estimate rather than as
realized revenue lift or a randomized causal effect.
We complement the quantitative evaluation with targeted human-
in-the-loop review. For selected patches and districts, planning
stakeholders inspect recommended assignments, territory distri-
butions and continuity breaks. This review is not a substitute for

Nan (Iris) Wang and Mitchell Turiel
quantitative evaluation, but a validation step: it helps confirm that
the optimizer output is interpretable, actionable, and consistent
with planning context that may not be fully captured in the data.
Beyond the historical backtest, the most recent production carve
provides an observed deployment outcome from the adopted plan-
ning cycle. Relative to the prior deployed plan, the adopted plan
improved assignment compliance by 17% and opportunity balance
by 7%. This production gain is smaller than the backtest improve-
ment by design: the backtest reruns the optimizer cleanly under
fixed planning constraints, whereas the production figure reflects
the adopted plan after field review, in which expert edits trade some
measured compliance for local business judgment not captured in
the optimizer. This comparison reflects before-versus-after plan-
quality changes in the deployed planning process, not a randomized
causal estimate and not a simulated backtest. We use it as evidence
that the decision system was operationally adopted and associated
with improved plan-quality metrics in production.
7 Deployment
The framework is operationalized within territory planning as an
adaptive, human-in-the-loop decision-support system rather than
an automated assignment engine (Figure 5). At the start of a plan-
ning cycle, the account-value and continuity-valuation layers pro-
duce their inputs, which are combined with assignment eligibility
and capacity constraints to generate an initial feasible territory
scenario.
As planning progresses, field stakeholders review the recom-
mended scenario and apply expert adjustments that reflect local
context and business priorities not fully captured in the data. The
optimizer is periodically re-run against the latest reviewed plan, so
that algorithmic recommendations and accumulated human edits
continuously inform one another; the intent-to-keep term (Sec-
tion 5) prevents these refreshes from reverting deliberate expert
changes.
Optimizer outputs are surfaced as inspectable planning scenarios
rather than written directly as final assignments, allowing stake-
holders to compare a recommendation against the current plan
and decide whether to adopt, adjust, or use it as reference. The
account-scoring layer is additionally used on its own for account-
value inspection and territory review. Together, this shifts terri-
tory carving from account-by-account manual assignment toward
scenario-based governance that embeds predictive scoring, conti-
nuity valuation, and constrained optimization into a governable
decision system—improving consistency and scale while preserving
human control.
8 Lessons Learned
First, objective-function design is the core challenge. Invoking an
optimizer is not sufficient; the difficult work is translating business
priorities into measurable objective terms and constraints. Account
value, continuity, balance, and capacity are not naturally expressed
in the same units, so the objective must be carefully calibrated to
avoid over-weighting one dimension.
Second, not every business rule should be a hard constraint. Some
requirements, such as segment eligibility or locked assignments,
may need to be enforced strictly. Others, such as balance targets or
continuity preferences, may be better represented as soft penalties
that allow the optimizer to make tradeoffs when necessary.
Third, continuity should be empirically calibrated where possible.
Planning teams often know that relationship disruption matters, but
the magnitude is difficult to reason about. Synthetic-control-based
valuation helps convert this intuition into a measurable tradeoff
that can be used in optimization.
Fourth, common currency matters for adoption. When account
scores, continuity values, and balance penalties are expressed only
in abstract optimization units, stakeholders may find it difficult to
understand why the optimizer prefers one assignment over another.
Finally, human-in-the-loop design is essential because territory
carving involves strategic context that may not be fully captured in
data. The optimizer should therefore serve as a consistent baseline
for expert review, not as an automatic final decision.
9 Limitations
Several limitations bound the claims in this paper.
Account value is treated as assignment-invariant.The optimizer
maximizes captured account value under the assumption that an
account’s value is independent of which seller is assigned to it. In
practice, seller fit, capacity, and continuity all plausibly affect real-
ized outcomes; relaxing this assumption—jointly modeling account
value and assignment—is an open problem.
Continuity is estimated, not identified.As discussed in Section 4,
the handoff effect is observational. The placebo adjustment guards
against common time-period effects but not against selection into
handoff on unobservables or cross-account spillovers. The reported
ATT should be read as directional.
Evidence type.Our evidence combines historical backtesting
and production before-versus-after comparisons. The backtest re-
sults are backtest-based comparisons to the deployed expert plan,
while the production compliance and balance gains are observed
outcomes from adopted production plans. The production results
demonstrate operational improvement but should not be read as
randomized causal estimates, since planning rules, account mix,
and field behavior may differ across cycles. The account-value op-
portunity estimate is also directional rather than measured realized
lift.
Operational scope.The current formulation does not encode
patch-level rules such as geography or language coverage, can
produce weaker plans in low density districts where few feasible
sellers exist, and may surface infeasibility when a district mixes
segments or sales motions. These cases presently fall back to human
review.
Toward causal validation.The natural next step is to move from
observational backtesting to staged or randomized rollout—varying
assignment policy across comparable districts—so that compliance,
balance, and continuity effects can be estimated causally rather
than inferred from a single planning snapshot.
10 Conclusion
We present a production-oriented decision system for territory
carving that combines account value quantification, continuity

Tradeoff-Aware Territory Design: A Multi-Objective Decision System for Enterprise Customer-to-Seller Allocation
Figure 5: Adaptive human-in-the-loop deployment workflow. Planning inputs drive an initial scenario generation; planners
review and govern the recommendation, and re-optimization incorporates their edits, iterating between human review and the
optimizer until a final territory plan is adopted.
valuation, and multi-objective optimization. The system has been
operationalized in planning workflows as a scenario-based decision-
support tool: optimizer outputs serve as recommended planning
scenarios that stakeholders can adopt, adjust, or use as references,
while account scores also support independent account-value re-
view. The broader contribution is less any single component than
the reframe they enable: by expressing account value as a com-
mon currency and continuity as a measured cost, territory carving
becomes a transparent, governable decision surface rather than a
distributed act of expert judgment.
Future work will focus on further improving the multi-objective
formulation, including additional realistic planning constraints,
more interpretable objective terms, and stronger explanation of
optimizer recommendations. We also plan to extend optimization
from account-to-seller assignment toward higher-level district and
regional planning, where larger planning scopes make manual
tradeoff management increasingly difficult.
Acknowledgments
We are especially grateful to the Strategic Planning (SPACE) team
for their close partnership throughout this work. Their domain
expertise, planning-design guidance, and support in driving stake-
holder adoption were central to translating the decision framework
into a usable territory-planning system. We thank Megan Luu, An-
drew Liu, Hannah Wilenskey-Ho, Marcus Trott, Stephen Huang,
Sid Kumar, Sahana Sarma, and the broader SPACE team for their
sustained collaboration.
We also thank Jake Brutlag, Jason Huang, Feng Pan, Divy Meng-
hani and our internal data science reviewers for valuable feedback
on the framing, methodology, and evaluation. We thank Vinson
Wei for analytical and implementation support. We are grateful to
the GTM Analytics team, including Petar Zoric and David Gojo, for
related input on the account-signal foundation. Finally, we thank
the territory-planning stakeholders whose domain review helped
validate the system and shape its production use.
References
[1] Alberto Abadie. 2021. Using Synthetic Controls: Feasibility, Data Requirements,
and Methodological Aspects.Journal of Economic Literature59, 2 (2021), 391–425.
[2] Alberto Abadie, Alexis Diamond, and Jens Hainmueller. 2010. Synthetic Control
Methods for Comparative Case Studies: Estimating the Effect of California’s
Tobacco Control Program.J. Amer. Statist. Assoc.105, 490 (2010), 493–505.
[3] Sunil Gupta, Dominique Hanssens, Bruce Hardie, William Kahn, V. Kumar,
Nathaniel Lin, Nalini Ravishanker, and S. Sriram. 2006. Modeling Customer
Lifetime Value.Journal of Service Research9, 2 (2006), 139–155.
[4] Laura Hervert-Escobar and Vassil Alexandrov. 2018. Territorial Design Optimiza-
tion for Business Sales Plan.J. Comput. Appl. Math.340 (2018), 501–507.
[5] Suvendu Jena, Jilei Yang, and Fangfang Tan. 2023. Unlocking Sales Growth:
Account Prioritization Engine with Explainable AI.arXiv preprint arXiv:2306.07464
(2023).
[6] Kaisa Miettinen. 1999.Nonlinear Multiobjective Optimization. Kluwer Academic
Publishers.
[7] Roger Z. Ríos-Mercado and J. Fabián López-Pérez. 2013. Commercial Territory De-
sign Planning with Realignment and Disjoint Assignment Requirements.Omega
41, 3 (2013), 525–535.
[8] Bernd Skiera and Sönke Albers. 1998. COSTA: Contribution Optimizing Sales
Territory Alignment.Marketing Science17, 3 (1998), 196–213.
[9] Andris A. Zoltners and Prabhakant Sinha. 1980. Integer Programming Models for
Sales Resource Allocation.Management Science26, 3 (1980), 242–260.
