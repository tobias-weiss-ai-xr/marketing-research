---
title: Auditing Marketing Budget Allocation with Hindsight Regret
url: https://arxiv.org/abs/2604.25977
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Nilavra Pathak
- Olivier Jeunen
- Eric Lambert
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.25977
pages: 6
chars: 33934
fetched_at: '2026-11-08T13:07:18+00:00'
kb_version: 1
---

# Auditing Marketing Budget Allocation with Hindsight Regret

Auditing Marketing Budget Allocation with Hindsight Regret
Nilavra Pathak
Expedia Group
New York, USA
npathak@expediagroup.com
Olivier Jeunen
aampe
Antwerp, Belgium
olivier@aampe.com
Eric Lambert
Expedia Group
Seattle, USA
elambert@expediagroup.com
Abstract
Organizations routinely make strategic budget allocations under
operational constraints. However, they often lack a principled way to
assess those realized allocations. We present a retrospective auditing
frameworkbasedonhindsightregret,formarketingbudgetallocation.
Regret is defined as the opportunity cost of the realized allocation
relative to a constraint-faithful benchmark under the same budget
and stability guardrails. The framework estimates regime-specific
spend–response functions from historical logs, computes feasible
hindsight allocations by constrained optimization, and propagates
uncertainty through Monte Carlo evaluation to produce regret distri-
butions, expected lift, and probability-of-improvement summaries.
This separates allocation inefficiency from uncertainty in the esti-
mated response surfaces. Experiments on real marketing allocation
logs show that the framework yields interpretable post-hoc diagnos-
tics and reveals a practical trade-off between allocation flexibility
anddetectability:moderatefeasiblere-allocationsoftencapturemost
measurable gain, while larger shifts move into weak-support regions
with higher uncertainty. The result is a practical method for auditing
historical budget decisions when online experimentation is costly or
infeasible.
CCS Concepts
•Computingmethodologies →Causalreasoninganddiagnostics;
Machine learning;Uncertainty quantification; Continuous optimiza-
tion;•Information systems→Online advertising.
Keywords
Regret Analysis, Decision Theory, Marketing Portfolio Allocation,
Causal Inference , Counterfactual Evaluation, Partial Observability
1 Introduction
Strategic budget allocation is a recurring decision problem in digital
advertising. Organizations must distribute finite budget across chan-
nels, markets, and campaigns over a planning horizon while respect-
ing operational guardrails such as budget limits, pacing rules, and
stability constraints. Because these allocations are high-dimensional,
persistent, and costly to revise, poor decisions can carry substantial
economic consequences.
Acentralchallengeisretrospectiveevaluation.Observedoutcomes
such as revenue or profit reflect not only decision quality, but also
market conditions, platform dynamics, and other factors outside the
planner’scontrol.Asaresult,evenwhenhistoricallogsareavailable,
it is difficult to determine whether a realized allocation was close to
the best feasible decision that could have been made under the same
operational constraints. This raises a natural question:How much
value was left on the table due to the allocation decision itself?
Onlineadvertisingprovidesaconcreteandeconomicallyimportant
instance of this problem. Although auctions operate at the level
of individual impressions, many consequential choices occur at a
slower timescale through portfolio-style budget commitments across
heterogeneous assets such as channels, regions, and campaigns [27].
These decisions are subject to practical constraints including caps,
pacing rules, and limits on reallocation across periods [5, 6, 12, 18,
24].Inpractice,organizationsoftenhavedetailedhistoricalallocation
logs, but lack principled tools for auditing whether past allocations
were near-optimal.
Standard evaluation approaches do not directly address this need.
Randomizedexperimentsarecostlyorinfeasibleforcontinuous,high-
dimensionalallocationsandmayviolateno-interferenceassumptions
due to cross-channel effects [11, 16]. Pre–post and interrupted time-
series analyses are sensitive to non-stationarity and shocks [3, 7].
Synthetic control methods rely on stable donor units and cross-
sectional comparability assumptions that are difficult to justify for
persistent, multi-asset allocation trajectories [1,10]. More broadly,
while regret is central in online learning, those formulations focus
on sequential adaptation under partial feedback rather than post-hoc
auditing of a realized strategic allocation.
Wethereforestudyretrospectivebudget-allocationauditingthrough
hindsight regret: the opportunity cost of the realized allocation rel-
ative to the best feasible alternative in hindsight under the same
operational guardrails. Our goal is not online control or policy learn-
ing, but post-hoc measurement of whether a historical allocation left
recoverable value unrealized. To do so, we estimate regime-specific
spend–response functions from historical logs, construct constraint-
faithfulhindsight benchmarks through constrained optimization, and
propagatemodelandoutcomeuncertaintythroughMonteCarloeval-
uation to obtain regret distributions and probability-of-improvement
summaries. This yields an interpretable estimate of “value left on
the table” while separating apparent allocation inefficiency from
uncertainty in the estimated response surfaces.
In summary, our main contributions are:
(1) Ahindsight-regretformulationforretrospectiveallocation
auditing.We cast post-hoc evaluation of strategic budget
decisionsascomparisonagainstaconstraint-faithfulhindsight
benchmark, yielding an interpretable measure of opportunity
cost.
(2) Apracticalofflineauditingframework.Wecombineregime-
specific spend–response estimation, constrained hindsight op-
timization, and uncertainty propagation to evaluate historical
allocations using logged data alone.
(3) An empirical study on real strategic allocation logs.We
show how regret distributions, detectability thresholds, and
stability constraints together support systematic post-hoc
assessment of budget decisions.
arXiv:2604.25977v2  [econ.EM]  30 Apr 2026

XXX ’26, XXX, 2026, XXX Nilavra Pathak, Olivier Jeunen, and Eric Lambert
2 Background & Related Work
Overview of Measurement Approaches in Practice:Randomized
online experiments remain the standard for causal measurement in
digital systems [16]. However, strategic budget allocation is con-
tinuous, high-dimensional, and persistent, which makes large-scale
randomization costly and often operationally infeasible. Advertising
systemsalsoexhibitinterferenceacrossauctions,channels,andusers,
weakening standard no-interference assumptions [11]. When experi-
mentation is unavailable, practitioners often fall back on pre–post or
interrupted time-series designs [3, 7], which rely on stable untreated
dynamics and can break under demand shocks or non-stationarity.
Syntheticcontrolmethodssimilarlyrequiredonorstabilityandcross-
sectional comparability [1,10,26], assumptions that are difficult to
justifyforpersistent,policy-drivenallocationtrajectoriesinmediated
ad-delivery systems.
Regret as retrospective decision evaluation:In statistical de-
cision theory, regret formalizes anex-post opportunity cost: given
realized outcomes and a feasible action set, the chosen decision is
evaluated against the best feasible alternative that could have been
selected in hindsight under the same environment [17, 21]. This
produces a static optimality gap that measures decision inefficiency
rather than learning dynamics. By contrast, regret in bandit and
reinforcement learning settings [2, 4, 9, 15, 23] is sequential and
cumulative, reflecting the loss incurred while adaptively learning un-
der partial feedback. Our formulation adopts the former perspective.
It is also distinct from off-policy evaluation, whose objective is to
estimate the value of a target policy from logged feedback. Here the
object of evaluation is a realized allocation trajectory, and the bench-
mark is a feasible hindsight reallocation under the same operational
regime rather than a new policy to be deployed prospectively.
Structural Causal Modeling Approach:Budget allocation in
advertising systems operates through a structural data-generating
process:plannedbudgetsaffectlatentbiddinganddeliverydecisions,
which in turn determine realized spend and downstream returns [8].
We use the Structural Causal Model (SCM) framework [19] to give
semanticstothesecounterfactualcomparisonsthroughinterventional
response functions, namely expected returns under hypothetical
spendallocations.Identifiabilityofsuchstructuralresponsefunctions
requires assumptions on functional form and noise structure. Prior
work on additive and related noise models provides identifiability
results for nonlinear cause–effect pairs [13, 14, 20, 22, 25].
Need for a Custom Framework:Existing approaches do not
directly answer the question central to this paper: whether a realized
strategic allocation was close to the bestfeasibleallocation that
could have been chosen in hindsight under the same operational
guardrails. Our framework addresses this gap by estimating regime-
specific response surfaces from historical logs, constructing feasible
hindsight reallocations within the same regime, and quantifying the
resulting opportunity cost with uncertainty-aware regret summaries.
Non-stationarity is handled through epoch-wise re-estimation and
support-awareuncertaintyinflationratherthanbyassuminginvariant
untreated baselines or stationary learning dynamics.
3 Problem Formulation
We consider sequential budget allocation over a fixed planning
horizon of𝑇 operational time steps. Budgets are updated at coarser
decision epochs𝜏∈{1,...,𝑇/𝑘} and held fixed for𝑘 operational
steps. At each epoch, the planner allocates budget across𝑁assets.
Let b𝜏 =(𝑏 𝜏,1,...,𝑏 𝜏,𝑁)∈B⊆R 𝑁 + denote the epoch-𝜏 budget
vector, whereB encodes feasibility constraints such as total budget,
caps, floors, and operational guardrails.
Mediated execution.Budgets do not directly determine spend
or returns. Instead, delivery is mediated by a platform execution
mechanisminteractingwithastochasticmarketenvironment[ 8].Let
𝑥𝜏 denote observed context,𝑢𝜏 unobserved exogenous factors (e.g.,
competition, inventory), and𝑧𝜏 internal system state. The structural
relations are
𝜷𝜏 =𝜋(b 𝜏,𝑥𝜏,𝑧𝜏,𝑢𝜏),(1)
s𝜏 =𝜎(𝜷 𝜏,𝑥𝜏,𝑧𝜏,𝑢𝜏)+𝝃 𝜏,E[𝝃 𝜏|·]=0,(2)
𝝆𝜏 =𝜌(s 𝜏,𝑥𝜏,𝑢𝜏)+𝜺 𝜏,E[𝜺 𝜏|·]=0.(3)
Here s𝜏 denotesrealizedspendand 𝝆𝜏 realizedreturns.Latentbidding
and serving actions𝜷𝜏 are not observed. Our retrospective analysis
therefore operates at the realized-spend layer, treating the upstream
execution mechanism as latent.
Observability and feedback.At epoch𝜏 the planner observes
(𝑥𝜏,b𝜏,s𝜏,𝝆𝜏), but not𝜷𝜏,𝑧𝜏,𝑢𝜏, or counterfactual outcomes. Feed-
back is bandit-style, revealing returns only at the executed allocation.
Budget accounting.The planner is given a fixed total budget𝐵tot
for the horizon, with allocations satisfying
𝑇/𝑘∑︁
𝜏=1
𝑁∑︁
𝑖=1
𝑏𝜏,𝑖 =𝐵 tot,b 𝜏∈B∀𝜏.(4)
Planning policy.A policy Π maps available information to al-
locations: b𝜏←Π(F 𝜏), withF𝜏 ={𝑥 1:𝜏,b 1:𝜏−1,s 1:𝜏−1,𝝆 1:𝜏−1}. This
partiallyobservedsequentialformulationdefinesthehistoricalsetting
against which hindsight regret is evaluated.
4 Retrospective Regret Framework
We present a retrospective framework for auditing the quality of a
realized budget allocation throughhindsight regret, defined as the
opportunity cost relative to the best feasible spend trajectory that
couldhavebeenexecutedunderthesameoperationalconstraintsand
historical regime. The pipeline proceeds in three steps:
(1) Interventional spend–return modeling (Step I):Estimate un-
certainty aware interventional spend–return response functions
under a reduced-form grey-box abstraction.
(2) Constraint-faithfuloracleallocation(StepII):Computethebest
feasible benchmark spend trajectory under operational guardrails
via constrained optimization.
(3) Uncertainty-aware regret estimation (Step III):Propagate
response uncertainty by Monte Carlo simulation to obtain a
distribution over regret and associated summary metrics.
4.1 Empirical regret
In classical decision theory,regretis the loss in utility incurred by
a decision that is suboptimal relative to an alternative evaluated in
hindsightundertherealizedstateoftheworld[ 17,21].Inoursetting,
a decision corresponds to a feasible spend trajectorys={𝑠 𝜏,𝑖}𝜏,𝑖 and

Auditing Marketing Budget Allocation with Hindsight Regret XXX ’26, XXX, 2026, XXX
utility is total realized return𝑅(s):= ˝ 𝜏,𝑖𝜌𝜏,𝑖(𝑠𝜏,𝑖). Given a realized
trajectorys real and a feasible benchmarks★, regret is defined as
Reg :=𝑅(s ★)−𝑅(s real).(5)
Because realized returns are stochastic and response functions are
estimatedfromdata, Regisarandomvariable.Individualrealizations
may be negative, corresponding to favorable stochastic outcomes
under the realized trajectory relative to the benchmark. We therefore
evaluateexpected regret
E[Reg]=E

𝑅(s ★)−𝑅(s real)  ,(6)
and report probability statements of the formP(Reg>0) , which
quantify the likelihood that the benchmark dominates the realized
trajectory in hindsight.
Operational regret with stability constraints (𝛿) and confidence
(𝜀).The benchmark depends on the operational realism encoded by
the feasible set. We index the feasible set by a stability parameter𝛿
and define
Reg(𝛿):=𝑅(s ★(𝛿))−𝑅(s real),s ★(𝛿)∈arg max s∈B(𝛿) 𝑅(s),(7)
whereB(𝛿) denotesthe 𝛿-constrainedfeasibleset(definedinStepII).
We call regret𝜀-certifiedat level𝛿if
P(Reg(𝛿)>0 )≥𝜀.(8)
Let Δ denote a prespecified set of plausible constraint levels. We
select
𝛿★∈arg max
𝛿∈Δ
E[Reg(𝛿)] s.t.P (Reg(𝛿)>0 )≥𝜀,(9)
and reportE[Reg(𝛿 ★)]together withP(Reg(𝛿 ★)>0).
4.2 Step I: Grey-Box Response Functions
We model epoch-specific spend–return mappings and evaluate coun-
terfactual spend trajectories under fixed operational guardrails. Up-
stream budget-to-bid dynamics are abstracted away; analysis is
conducted at the realized-spend layer.
4.2.1Structural Target and Identification.We formalize the
assumptions used to identify an epoch-specific interventional mean
response. The key modeling choice is to treat each epoch as a
locallystationaryregime:withinanepoch,observationsareanalyzed
as conditionally independent replicates given observed covariates,
while non-stationarity is handled at epoch boundaries through drift
regularization and stability constraints.
A1. Structural Response Model.For asset𝑖 in epoch𝑒, realized
outcomes satisfy
𝜌𝜏,𝑖 =𝑓 𝑖,𝑒(𝑠𝜏,𝑖,𝑥𝜏,𝑖)+𝜀 𝜏,𝑖, 𝜏∈𝑒.(10)
The function𝑓𝑖,𝑒 represents the reduced-form spend–return mecha-
nism induced by the execution regime in epoch𝑒.
A2. Within-epoch stationarity and local mean independence
(identification).Within epoch 𝑒, conditional on(𝑠𝜏,𝑖,𝑥𝜏,𝑖), the noise
process{𝜀𝜏,𝑖}𝜏∈𝑒 is treated as mean-zero and approximately indepen-
dent across𝜏:
E[𝜀𝜏,𝑖|𝑠 𝜏,𝑖,𝑥𝜏,𝑖]=0, 𝜀 𝜏,𝑖 ⊥ ⊥𝜀𝜏′,𝑖 (𝜏≠𝜏 ′;𝜏,𝜏 ′∈𝑒).(11)
Under A2, the interventional mean response
𝜇𝑖,𝑒(𝑠)=E

𝑓𝑖,𝑒(𝑠,𝑋𝜏,𝑖)|𝜏∈𝑒

is identified over therealized spend rangein epoch𝑒, that is, the𝑠
values observed under the historical policy within that epoch.
A3.Boundeddriftacrossepochs(regularizationonly).Acrossad-
jacentepochs 𝑒 and𝑒′,thereduced-formmechanismvariessmoothly
on the overlap of their realized spend ranges:
sup
𝑠∈S𝑒,𝑒′
|𝑓𝑖,𝑒(𝑠)−𝑓 𝑖,𝑒′(𝑠)|≤𝛿,S 𝑒,𝑒′ :=range(𝑒)∩range(𝑒 ′).
(12)
This condition enables weak borrowing of strength for estimation
stabilitybutdoesnotexpandcausalidentificationbeyondtheepoch’s
realized spend range. Accordingly, the framework is intended for
within-regime retrospective auditing, with conservative uncertainty-
aware evaluation when optimization reaches weak-support regions.
4.2.2Drift-regularized grey-box model.The mean response is
decomposed as
𝜌𝜏,𝑖 =𝜇 nom,𝑖,𝑒(𝑠𝜏,𝑖 ;𝜃𝑖,𝑒)+𝑔 𝑖,𝑒(𝑠𝜏,𝑖)+𝜎 𝑖,𝑒(𝑠𝜏,𝑖)𝜀𝜏,𝑖.(13)
Nominal saturation.
𝜇nom,𝑖,𝑒(𝑠)=𝑎 𝑖,𝑒(1−𝑒 −𝑏𝑖,𝑒𝑠), 𝑎 𝑖,𝑒,𝑏𝑖,𝑒≥0.(14)
Residual mean and variance.
𝑔𝑖,𝑒(·)∼GP(0,𝑘 𝑔),log𝜎 2 𝑖,𝑒(·)∼GP(𝑚 𝜎,𝑘𝜎),
with Matérn(2.5)kernels.
The two Gaussian processes serve distinct purposes. The mean
GP𝑔𝑖,𝑒 captures systematic deviations from the nominal saturation
curve, allowing flexible local curvature while preserving the inter-
pretable global shape imposed by𝜇nom,𝑖,𝑒. The variance GP models
heteroskedastic outcome dispersion as a function of spend, enabling
uncertaintytoincreaseinweak-supportregions.Separatingmeanand
variance components yields calibrated counterfactual uncertainty,
whichisessentialforMonteCarloregretestimationanddetectability
analysis.
Auxiliary regularization.Neighboring-epoch samples are incor-
porated with exponential weights
𝑤𝑡 =𝛼 aux exp(−|𝑑𝑡|/𝜏),
whichisequivalenttotreatingauxiliarypointsasnoisierobservations.
Coreepochdatadetermineidentification;auxiliarydataprovideweak
curvature regularization under bounded drift.
Support-awareextrapolation.For 𝑠beyondtheupperboundaryof
thecoreepoch’srealizedspendrange,thefittedmeanisprojectedonto
thespaceofnon-decreasingfunctionsviaboundary-anchoredisotonic
regression.For 𝑠 beyondtheweightedrealizedrange(coreplusdown-
weighted auxiliary coverage), epistemic variance is inflated:
𝜎 2 epi(𝑠)=𝜎 2 𝑔(𝑠)+
"
𝜅right

max{0,𝑠−𝑠 all hi}
𝑠scale
!𝑝
𝜎res
# 2
.(15)
Theseregionsareusedonlyforconservativeregretevaluation.Within
the core realized range, monotonicity is not imposed; in practice,
the posterior mean is typically monotone due to the dominance of
the nominal saturation component and smooth GP regularization.

XXX ’26, XXX, 2026, XXX Nilavra Pathak, Olivier Jeunen, and Eric Lambert
Metric Definition Interpretation
Expected regret bE[Reg(𝛿 ★)]= 1 𝐽 ˝𝐽 𝑗=1 Reg(𝑗)(𝛿★) Average achievable gain from feasible hindsight reallocation at the selected constraint level.
Standard deviationb𝜎 Reg =
√︃
1
𝐽−1
˝
𝑗(Reg(𝑗)(𝛿★)− bE[Reg(𝛿 ★)]) 2 Sensitivity of regret to outcome noise and model uncertainty; large values indicate fragile
conclusions.
Credible intervalCI 1−𝛼 =[𝑄 𝛼/2,𝑄 1−𝛼/2] Range of plausible regret values under uncertainty; intervals spanning zero indicate
ambiguous dominance.
Probability of improve-
ment
bP(Reg(𝛿 ★)>0)= 1 𝐽 ˝ 𝑗 1{Reg(𝑗)(𝛿★)>0} Likelihoodthatthe 𝛿★-constrainedbenchmarkoutperformstherealizedtrajectory;compared against𝜀in (8).
Table 1: Empirical regret metrics and uncertainty summaries. All quantities are computed from Monte Carlo draws{Reg(𝑗)(𝛿)} 𝐽 𝑗=1. Unless otherwise
stated, we evaluate at𝛿=𝛿★ selected by(9).
Spend
Return
Adjacent Periods
Current Period
Posterior Mean
95% Uncertainty
Spend
Return
Adjacent Periods
Current Period
Posterior Mean
95% Uncertainty
Figure 1: Monotone grey-box spend–response estimation under bounded
temporal drift. Current-period observations define the core realized
spendrange(blue),whileadjacentperiods(grey)provideweaklyweighted
curvature information. Posterior uncertainty widens outside the core
range to reflect increased epistemic risk.
Example of the constructed oracle functional forms are shown in
Figure 1.
4.3 Step II: Oracle allocation under operational
feasibility constraints
Giventhefittedepoch-wiseresponsefunctions { ˆ𝜇𝑖,𝑒(·)}𝐾 𝑖=1,wedefine
anoracleallocationasthesolutiontoafixedobjectiveevaluatedover
alternative feasible sets:
max
{𝑠𝜏,𝑖}𝜏,𝑖
𝐸∑︁
𝑒=1
𝐾∑︁
𝑖=1
ˆ𝜇𝑖,𝑒(𝑠𝑒,𝑖),(16)
where𝑠𝑒,𝑖 denotes the spend assigned to asset𝑖 in epoch𝑒. The
distinction between oracle variants arises solely from differences
in thefeasible set, which encodes alternative assumptions about
operational realism.
4.3.1Unconstrained oracle (idealized hindsight).The uncon-
strained oracle evaluates(16) over the largest feasible setBunc,
defined only by budget accounting and asset-level bounds:
Bunc :=
(
s

 ∑︁ 𝑒,𝑖 𝑠𝑒,𝑖 =𝐵 tot, 𝑠𝑖≤𝑠𝑒,𝑖≤𝑠𝑖 ) .
This oracle represents a theoretical upper bound corresponding to
perfect hindsight and unrestricted reallocation across epochs.
4.3.2Constrained oracle (realism-adjusted).Unconstrained
optimization may produce trajectories that are operationally im-
plausible. To restore realism, we introduce a constrained family
Bcon(𝛿) ⊂ Bunc that limits how allocations may change across
decision epochs. We impose epoch-to-epoch stability constraints:
𝑠𝑒−1,𝑖(1−𝛿)≤𝑠 𝑒,𝑖≤𝑠𝑒−1,𝑖(1+𝛿),∀𝑒>1, 𝑖,(17)
where𝛿∈(0,1)encodes allowable relative changes.
The constrained oracle is defined as
s★ con(𝛿)∈arg max s∈B con(𝛿)
𝐸∑︁
𝑒=1
𝐾∑︁
𝑖=1
ˆ𝜇𝑖,𝑒(𝑠𝑒,𝑖).
4.3.3Relationship between oracle variants under support-
aware planning.Oracle variants differ only through the feasible
setB(𝛿),wherelarger 𝛿 permitsgreaterepoch-to-epochreallocation.
For the deterministic planning objective ˜𝑅(s) in Step II, nested
feasibility implies
max
s∈B(𝛿 2)
˜𝑅(s) ≥max
s∈B(𝛿 1)
˜𝑅(s), 𝛿 2 >𝛿 1.
Thusmonotonicityholdsforthedeterministicplanningobjective,but
not necessarily for uncertainty-aware empirical regret after posterior
evaluation in Step III.
However,wereportuncertainty-awareregretfromStepIII,where
the chosen allocations★(𝛿) is evaluated under posterior predictive
uncertainty. Larger𝛿 may shift the optimizer toward weakly sup-
ported regions, increasing variance and occasionally reducing both
E[Reg(𝛿)] and the detectabilityP(Reg(𝛿)>0) . Thus operational
lift need not be monotone in𝛿, and empirical curves may exhibit
saturation or dips.
4.4 Step III: Regret distribution via Monte Carlo
Regret is random due to stochastic outcomes and uncertainty in the
Step I response surfaces. For each stability level𝛿∈Δ (and the
unconstrained case), we first compute the oracle trajectorys★(𝛿)
by optimizing the plug-in mean responses from Step I over the
feasible set from Step II. We then holds★(𝛿) fixed and propagate
uncertaintyviaMonteCarlotoobtainadistributionover Reg(𝛿).For
each scenario we perform the following sampling steps:
(1) Sample counterfactual returns.Draw independent innovations
𝜀(𝑗) 𝑒,𝑖 ∼N(0,1) andgeneratecounterfactualreturnsusingthefitted
location–scale model,
𝜌(𝑗) 𝑒,𝑖(𝑠)= ˆ𝜇𝑖,𝑒(𝑠)+𝜂 (𝑗) 𝑖,𝑒(𝑠)+ ˆ𝜎𝑖,𝑒(𝑠)𝜀 (𝑗) 𝑒,𝑖 ,
where𝜂(𝑗) 𝑖,𝑒(𝑠) is a GP-consistent mean perturbation for𝑔𝑖,𝑒, aug-
mented with the off-range inflation term in(15). This simulation
treatsdrawsasconditionallyindependentacrossassetsandepochs

Auditing Marketing Budget Allocation with Hindsight Regret XXX ’26, XXX, 2026, XXX
(a)𝛿=30%
 (b)𝛿=50%
 (c) Unconstrained
Figure 2: Monte Carlo regret (lift) distributions under alternative stability constraints. Each violin summarizes posterior lift relative to the realized allocation across
portfolio–horizon pairs. Increasing flexibility expands the feasible set but does not guarantee monotone improvements in uncertainty-aware lift.
given the fitted responses. We treat this as a first-order approxi-
mation for retrospective auditing rather than a full joint model of
cross-asset dependence.
(2) Compute regret at each constraint level.Using the fixed oracle
trajectorys ★(𝛿), compute
Reg(𝑗)(𝛿)=𝑅 (𝑗) s★(𝛿)−𝑅(𝑗)(sreal),∀𝛿∈Δ,
and analogouslyReg(𝑗) unc for the unconstrained oracle.
We then select𝛿★ via (9) using these Monte Carlo estimates,
including the𝜀-certificate, and report the regret distribution at𝛿★
together with the summary metrics in Table 1.
5 Results
Weevaluatetheproposedretrospectiveregretframeworkusinghistor-
ical strategic allocation logs under operationally realistic feasibility
constraints. All outcomes are reported asrelative liftwith respect
to the realized allocation. For confidentiality, we omit portfolio
composition, asset identities, absolute magnitudes, and the semantic
meaning of evaluation horizons. Our goal is not to recover a ground-
truth global optimum, but to assess whether the framework yields
stable and decision-relevant retrospective diagnostics under realistic
feasibility constraints. We address four questions:
• RQ1:Do logged allocations support stable and interpretable
regret diagnostics?
•RQ2:How does uncertainty shape regret?
•RQ3:What is the effect of operational stability constraints?
•RQ4:When are larger reallocations justified?
5.1 Retrospective Regret, Uncertainty, and
Feasibility
Weevaluate𝑃=8 portfoliosacross𝐻=8 decisionhorizons.Foreach
portfolio–horizon pair, epoch-specific spend–return functions are
estimatedusingtheweightedmonotonegrey-boxmodel(Section4.2).
Oracle allocations are computed once per feasibility specification
andthenheldfixed.Uncertaintyisintroducedonlyatevaluationtime
via Monte Carlo propagation of outcome noise and model uncer-
tainty. Figure 2 shows lift distributions for representative portfolios
across horizons under multiple feasibility settings. The distributions
illustratethatregretisinherentlydistributionalandthatitsdispersion
varies across constraint levels.
RQ1–RQ3 findings.Across all portfolio–horizon pairs we ob-
serve:
(1) Logged allocations support interpretable regret diagnostics
(RQ1).The framework produces well-defined lift distributions
and certification rates from historical logs without requiring new
experimentation, provided evaluation remains within or near
empirically supported regions.
(2) Uncertainty is first-order (RQ2).Many cases exhibit wide lift
dispersion even when posterior mean lift is positive. Negative
realizations arise naturally under Monte Carlo evaluation due to
stochastic outcomes and epistemic uncertainty.
(3) Operationalconstraintsaffectbothmagnitudeanddetectabil-
ity (RQ3).Relaxing the stability constraint𝛿 typically increases
plug-in lift, but can widen regret distributions as optimization
moves spend toward regions with weaker empirical support,
reducing high-confidence detectability.
Aggregate detectability.Table 2 summarizes certification results
across feasibility levels. For each𝛿 and confidence threshold𝜖, we
report the fraction of portfolio–horizon pairs satisfying𝑃(Reg>
0)≥𝜖and the mean lift among detectable pairs.
Three consistent patterns emerge. First, moderate thresholds
(𝜖∈{0.5,0.6} ) frequently certify improvement. Second, stringent
thresholds (𝜖≥0.8 ) substantially reduce detectability, reflecting
broad regret distributions even when mean lift is positive. Third,
increasing flexibility generally raises mean lift among detectable
cases but does not guarantee monotone gains in detectability, con-
sistent with uncertainty inflation beyond core empirical support.
Taken together, these results suggest that the framework is most
useful as an auditing tool for detecting recoverable opportunity cost
under plausible reallocation limits, rather than for certifying large
aggressive reallocations.
Constraint𝛿 𝜖=0.6𝜖=0.7𝜖=0.8𝜖=0.9
±20% 0.59 (8.2±5.6) 0.33 (8.3±5.0) 0.20 (8.2±2.9) 0.08 (9.6±1.5)
±30% 0.75 (9.4±6.7) 0.53 (10.6±6.6) 0.28 (10.3±5.3) 0.09 (11.4±4.1)
±40% 0.88 (9.9±7.6) 0.61 (11.4±7.6) 0.38 (11.3±7.0) 0.09 (12.2±4.4)
±50% 0.89 (10.5±8.0) 0.66 (11.9±8.2) 0.42 (12.8±8.4) 0.12 (12.7±4.9)
Unconstrained 0.89 (12.5±9.7) 0.67 (14.4±10.0) 0.47 (14.0±9.5) 0.22 (14.7±6.8)
Table 2: Fraction of portfolio–horizon pairs with𝑃(Reg>0)≥𝜖 . Parentheses
show mean±std lift (%) across detectable pairs.
5.2 When Are Large Re-Allocations Justified?
RQ4 evaluates the marginal benefit of relaxing the inter-epoch
stability constraint𝛿. For each𝛿, we recompute the oracle allocation
and estimate regret under the same Monte Carlo protocol, isolating
the effect of flexibility alone.

XXX ’26, XXX, 2026, XXX Nilavra Pathak, Olivier Jeunen, and Eric Lambert
Figure 3: Ablation of stability for three portfolios and horizons. Mean lift (dashed line) and lift distributions are shown as a function of allowable
inter-epoch change𝛿. Checkmarks denote𝑃(Lift>0)≥0.8. Gains typically concentrate at moderate flexibility and saturate thereafter.
Figure 3 shows two regimes. Allowing moderate flexibility (±20%
–±40%) yields large gains by correcting obvious misallocations and
shifting spend toward well-supported, high-return regions. Beyond
this, lift often saturates: once allocations approach local optima,
additional movement mainly explores flatter or weakly supported
regions where marginal returns are small and uncertainty is higher.
In some portfolios, lift continues to rise with𝛿 when profitable
regions remain farther from the realized allocation, so larger moves
are still beneficial. However, greater flexibility typically increases
variance, so detectability improves only selectively and can weaken
at stringent confidence thresholds, as reflected in Table 2. Overall,
most gains are captured at moderate𝛿, while extreme reallocations
trade reliability for limited additional return.
6 Conclusion and Future Work
We introduced a hindsight-regret framework for retrospective audit-
ing of strategic budget allocation under operational constraints. The
framework evaluates realized allocations against constraint-feasible
hindsight benchmarks built from regime-specific response surfaces
estimated from historical logs. Empirically, most recoverable gains
are attained through moderate feasible reallocations, while more ag-
gressive flexibility yields diminishing returns and higher uncertainty.
Future work will develop formal guarantees for response estima-
tion, regret perturbation, and finite-sample Monte Carlo summaries.
An important next step is a semi-synthetic benchmark with known
response structure and oracle regret, which would enable direct
recovery-based validation of the framework. We also plan to ex-
tend the same setup to policy-level retrospective scoreboarding of
alternative allocation strategies within the same logged regime.
References
[1] Alberto Abadie. 2021. Using Synthetic Controls: Feasibility, Data Requirements,
and Methodological Aspects.Journal of Economic Literature59, 2 (2021),
391–425.
[2] Yasin Abbasi-Yadkori, Csaba Szepesvári, and Peter Bartlett. 2011. Regret Bounds
for the Adaptive Control of Linear Quadratic Systems. InCOLT.
[3] JoshuaD.AngristandJörn-SteffenPischke.2009.MostlyHarmlessEconometrics:
An Empiricist’s Companion. Princeton University Press.
[4] Peter Auer. 2002. Using confidence bounds for exploitation-exploration trade-offs.
Journal of machine learning research3, Nov (2002), 397–422.
[5] Lennart Baardman, Elaheh Fata, Abhishek Pani, and Georgia Perakis. 2019.
Learning optimal online advertising portfolios with periodic budgets.Available at
SSRN 3346642(2019).
[6] Santiago R. Balseiro, Kshipra Bhawalkar, Zhe Feng, Haihao Lu, Vahab Mirrokni,
BalasubramanianSivan,andDiWang.2024. AFieldGuideforPacingBudgetand
ROS Constraints. InProceedings of the 41st International Conference on Machine
Learning (Proceedings of Machine Learning Research, Vol. 235). 2607–2638.
[7] JamesLopezBernal,StevenCummins,andAntonioGasparrini.2017. Interrupted
time series regression for the evaluation of public health interventions: a tutorial.
International Journal of Epidemiology46, 1 (2017), 348–355.
[8] LéonBottou,JonasPeters,JoaquinQuiñonero-Candela,DenisX.Charles,D.Max
Chickering, Elon Portugaly, Dipankar Ray, Patrice Simard, and Ed Snelson. 2013.
Counterfactual reasoning and learning systems: The example of computational
advertising.TheJournalofMachineLearningResearch14,1(2013),3207–3260.
[9] Sarah Dean, Horia Mania, Nikolai Matni, Benjamin Recht, and Stephen Tu. 2018.
Regret Bounds for Robust Adaptive Control of Linear Quadratic Systems. In
Advances in Neural Information Processing Systems.
[10] Arindrajit Dubé and Ben Zipperer. 2014.Pooled Synthetic Control Estimates for
ContinuousTreatments:AnApplicationtoMinimumWageCaseStudies. Technical
Report. IZA.
[11] Dean Eckles, Brian Karrer, and Johan Ugander. 2017. Design and analysis of
experiments in networks: Reducing bias from interference.Journal of Causal
Inference5, 1 (2017), 20150021.
[12] Duncan M. Holthausen and Gert Assmus. 1982. Advertising Budget Allocation
under Uncertainty.Management Science28, 5 (1982), 487–499.
[13] Patrik O. Hoyer, Dominik Janzing, Joris M. Mooij, Jonas Peters, and Bernhard
Schölkopf. 2009. Nonlinear Causal Discovery with Additive Noise Models. In
Advances in Neural Information Processing Systems, Vol. 21.
[14] Alexander Immer, Christoph Schultheiss, Julia E. Vogt, Bernhard Schölkopf, Peter
Bühlmann, and Alexander Marx. 2023. On the Identifiability and Estimation of
Causal Location-Scale Noise Models. InInternational Conference on Machine
Learning. 14316–14332.
[15] ThomasJaksch,RonaldOrtner,andPeterAuer.2010. Near-optimalRegretBounds
for Reinforcement Learning.Journal of Machine Learning Research11 (2010),
1563–1600.
[16] Ron Kohavi, Diane Tang, and Ya Xu. 2020.Trustworthy Online Controlled
Experiments: A Practical Guide to A/B Testing. Cambridge University Press.
[17] GrahamLoomesandRobertSugden.1982. Regrettheory:Analternativetheoryof
rationalchoiceunderuncertainty.TheEconomicJournal92,368(1982),805–824.
[18] Ha Nguyen, Djordje Gligorijevic, Arnab Borah, Gajanan Adalinge, and Abraham
Bagherjeiran.2023. PracticalBudgetPacingAlgorithmsAndSimulationTestBed
For eBay Marketplace Sponsored Search. InAdKDD Workshop 2023 at the 29th
ACM SIGKDD Conference on Knowledge Discovery and Data Mining.
[19] JudeaPearl.2009.Causality:Models,Reasoning,andInference(2ed.). Cambridge
University Press.
[20] JonasPeters,DominikJanzing,andBernhardSchölkopf.2017.ElementsofCausal
Inference: Foundations and Learning Algorithms. MIT Press.
[21] Leonard J. Savage. 1954.The Foundations of Statistics. Wiley.
[22] Shohei Shimizu, Patrik O. Hoyer, Aapo Hyvärinen, and Antti Kerminen. 2006. A
Linear Non-Gaussian Acyclic Model for Causal Discovery.Journal of Machine
Learning Research7 (2006), 2003–2030.
[23] Niranjan Srinivas, Andreas Krause, Sham Kakade, and Matthias Seeger. 2010.
Gaussian Process Optimization in the Bandit Setting: No Regret and Experimental
Design.InProceedingsofthe27thInternationalConferenceonMachineLearning.
[24] Efthymia Symitsi, Raphael N. Markellos, and Murali K. Mantrala. 2022. Key-
word Portfolio Optimization in Paid Search Advertising.European Journal of
Operational Research303, 2 (2022), 767–778.
[25] Naiyu Yin, Tian Gao, Yue Yu, and Qiang Ji. 2024. Effective Causal Discovery
under Identifiable Heteroscedastic Noise Model. InProceedings of the AAAI
Conference on Artificial Intelligence, Vol. 38. 16486–16494.
[26] ZiyanZhang.2019. InferenceforSyntheticControlMethodswithMultipleTreated
Units.arXiv preprint arXiv:1912.00568(2019).
[27] Kui Zhao, Junhao Hua, Ling Yan, Qi Zhang, Huan Xu, and Cheng Yang. 2019. A
Unified Framework for Marketing Budget Allocation. InProceedings of the 25th
ACM SIGKDD International Conference on Knowledge Discovery & Data Mining
(KDD ’19). 3305–3313.
