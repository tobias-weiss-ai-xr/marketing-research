---
title: Lifetime-valid decisions by continually evolving AI analysts
url: https://arxiv.org/abs/2610.30562
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Xiaojing Sun
- Yuhan Zeng
- Xiao Wang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.30562
pages: 70
chars: 235747
fetched_at: '2026-11-08T13:34:38+00:00'
kb_version: 1
---

# Lifetime-valid decisions by continually evolving AI analysts

Lifetime-valid decisions by continually evolving AI analysts
Xiaojing Sun1, Yuhan Zeng1, and Xiao Wang 1
1Department of Statistics, Purdue University
Abstract
AI agents increasingly act as analysts whose decision can often be cast as hypothesis tests.
Classical tests control the Type I error rate, the probability of rejecting a true null hypothe-
sis, for fixed procedures. However, AI analysts introduce internal randomness and can evolve
continuously over time. As AI analysts evolve, the risk of approving versions with Type I error
rates above the target can accumulate, and adaptive use of evaluation feedback can lead to over-
fitting. We introduce continual validation, which evaluates each proposed AI analyst version
before deployment using simulated data under the null hypothesis, with scenarios that can be
randomized and expanded over time. We prove that, regardless of how updates are chosen or
how many are proposed, the lifetime probability of ever deploying a version whose Type I error
rate exceeds the allowed level remains bounded. This guarantees that every subsequent decision
controls the Type I error rate at the target level across these scenarios. At the same time,
updates with sufficiently low Type I error rates pass validation with high probability, allowing
the analyst to continuously improve its performance without sacrificing rigor. In two examples
involving evolving AI analysts for bioequivalence studies and product A/B tests, Type I error
rates reached 0.098 and 0.183 without continual validation, compared with at most 0.045 and
0.044 with it, while retaining 82% and 96% of the power from optimally selected valid updates.
1 Introduction
As large language models and the systems built around them advance, AI agents are increasingly
used to analyze data. They plan analyses, write and execute code, and report findings in tasks such
as developing machine learning methods, studying cellular processes, and discovering new drugs
[1, 2, 3, 4]. Recent benchmarks assess these capabilities across scientific and data science tasks
[5, 6, 7, 8]. We refer to agents performing such analyses as AI analysts.
Although these analyses may involve complex workflows, including multiple stages of data pro-
cessing, model selection, diagnostic evaluation, and iterative refinement, they often lead to decisions
such as reporting a discovery, claiming bioequivalence of a drug product, or launching a product.
Such decisions can often be formulated as hypothesis tests, which AI agents are increasingly trained
to perform [9, 10]. For example, in bioequivalence studies [11, 12], the null hypothesis states that
the test product is not bioequivalent to the reference product. A Type I error occurs when a true
null hypothesis is rejected. Similarly, when deciding whether to launch a new product feature, the
null hypothesis states that the feature provides no improvement, while the alternative states that
it does. Classical statistical methods control the probability of this error at a prespecified level
α, typically for procedures fixed before the data are observed, where randomness comes primarily
from data sampling [13, 14].
AI analysts, however, pose two additional challenges to Type I error control. First, even a fixed
version can make different decisions on the same data. A version fixes its model, prompts, and
1
arXiv:2610.30562v1  [stat.ME]  22 Oct 2026

available tools, but sampling from the underlying language model may change which analyses and
tools are selected [15, 16]. Each version therefore defines a randomized test, whose Type I error
rate accounts for both data sampling and the analyst’s internal randomness [17, 14].
Second, the analyst itself can change frequently in many ways. Developers edit prompts, add
skills, redesign workflows, and upgrade models [18]. Self-improving agents can also repeatedly
revise themselves to evolve [19, 20, 21, 22, 23, 24]. Together, these changes can produce a rapid
and potentially unlimited sequence of versions, each modifying multiple parts of the analyst. We
call each proposed change an update and the resulting configuration a new version of the analyst.
Updates are often retained when they appear to improve the analyst’s performance, but without
appropriate validation, an increase in their Type I error rate may go undetected.
This adaptive selection makes the problem different from controlling a single randomized test.
Updatescanbeselectedbasedonfeedbackfromearlieranalysesandevaluations, potentiallycausing
the analyst to overfit past results and inflate its Type I error rate [25, 26]. Even a single update
can substantially change the Type I error rate. For example, at a target Type I error level of
0.10, replacing Claude Sonnet 3.5 with Claude Haiku 3.5 in a hypothesis-testing agent increased
its estimated Type I error rate from 0.082 to 0.780 on one benchmark [9].
Existing methods provide important statistical guarantees, but they address different problems.
Prediction-powered inference enables valid statistical inference using machine learning predictions
[27], while conformal methods such as TxConformal control false discoveries when AI predictions are
used to select therapeutic candidates [28]. Agentic falsification controls Type I error for a specified
agent performing sequential hypothesis testing [9]. Other methods address adaptive analysis choices
and repeated testing. The reusable holdout allows the same dataset to be used repeatedly to
evaluate adaptively chosen analyses [29], while selective inference accounts for data-dependent
analysischoices[30]. Onlinemultipletestingcontrolsfalserejectionsacrossasequenceofhypotheses
[31], and adaptive clinical trial designs allow prespecified modifications within a trial [32].
Other work examines how learning systems can be updated safely. High-confidence safety
frameworks evaluate candidate algorithms against specified constraints [33], while approval policies
for medical software control the risk of harmful updates and gradual deterioration in performance
[34]. Recent methodsforself-improvingagentsprovidestatisticalguaranteesforacceptingbeneficial
modifications [35, 36], while Learn then Test calibrates a prespecified set of configurations to satisfy
statistical risk constraints [37].
However, these methods do not directly guarantee Type I error control for AI analysts that
continually evolve through adaptive updates to their models, tools, and decision rules. Our goal
is to provide a lifetime guarantee by controlling the risk of ever deploying a version whose Type I
error exceeds the required level. This allows the analyst to continue updating while maintaining
Type I error control in future studies. We also aim to preserve statistical power at a reasonable
computation cost.
We introduce continual validation, shown in Fig. 1A, which allows AI analysts to keep improving
while maintaining Type I error control at modest cost. Developers or the analyst itself can propose
any updates. Before deployment, each proposed version is fixed and tested on newly simulated
datasets where the null hypothesis is true. We set a validation levelα′ slightly belowα. We
prove that, regardless of how updates are proposed, the probability of ever deploying a version
whose Type I error rate exceedsα′ under the simulated null conditions is at most a prespecified
δ. This guarantees Type I error control at the prespecified levelαfor every subsequent decision.
At the same time, updates with sufficiently low Type I error rates can still be approved with
high probability. We apply it to two AI analysts, one for bioequivalence studies of test products
and another for product launching experiments. We compare it with four alternative deployment
strategies, and Fig. 2 summarizes the comparison.
2

AContinual validation tests every update before it is deployed
Proposer
developer or AI analyst
Update 1
α′
scenarios under H0
deploy v1
Update 2
scenarios under H0
do not deploy v2,
keep v1
Update 3
scenarios under H0
deploy v3
…
feedback
Type I error
above α′
v0 v1in use v3
What each level controls
α′
scenarios
α′validation level
An update is deployed only if its Type I
error bound is at most α′ in every
simulated null scenario.
lifetimes
δlifetime risk
Over any number of updates, the
chance of ever deploying a version
above α′ is at most δ.
null studies
αevery decision
In a real study where H0holds, the
chance of rejecting H0is at most
α = α′ + δ(1 − α′).
BThe two examples and the experiment
Example 1Is the test product bioequivalent to the reference product?
hypotheses data bioequivalence
AI analyst, version vr
decisionTtest productRreference product
H0 H1 H0
0.80 1.25
true ratio, test to reference
H0not bioequivalent
H1bioequivalent
Period 1 2 3 4
Subject 1T R T R
Subject 2R T R T
Subject 3T R T R
Subject nR T R T
0.80 1.25
CI of the geometric mean ratio
claim bioequivalence
no claim
defer to a human
Type I error
a false claim
calling the test product
bioequivalent when it
is not
Example 2Does a new feature of a shopping app make more users buy?
hypotheses data A/B test
AI analyst, version vr
decision(users randomized to A or B)
H0 H1
0
true change in purchase rate
H0no improvement
H1improvement
Acurrent version
Bnew feature
purchases per day
Day 1 Day 14
p value
launch
do not launch
Type I error
a false launch
launching a feature
that does not make
more users buy
ProposerAI developer
Claude Sonnet 5.5
Qwen 3.8
DeepSeek-R1
deployment method
continual validation(our method)
or one of four comparison methods
deploy the update
keep the current version
for each deployment method
10 rounds
20 runs
update
deployed version
deployed versionfeedback on each update
Figure 1:Continual validation and the two examples. (A) A human developer or the AI analyst itself
proposes updates. The validator freezes the updated version and runs it alongside a reference analysis on
datasets newly simulated under the null hypothesis. The update is deployed only when the upper confidence
bound on its Type I error rate is at most the validation levelα′ across all simulated scenarios. The bound for
update 2 exceedsα′ in one scenario so it is rejected andv1 stays in use. The proposer receives this result as
feedback. Over any number of updates the chance of ever deploying a version aboveα′ remains at most the
lifetime riskδ. In every real study where the data follow a simulated null scenario a trueH0 is rejected with
probability at mostα=α ′ +δ(1−α ′). The examples useα= 0.05andδ= 0.005which givesα ′ = 0.0452.
(B) The two examples and the experiment setup. In Example 1 the agent decides whether a test product
and a reference product are bioequivalent under the standard average bioequivalence framework. The true
ratio is the ratio of their geometric mean exposures for a measure such as the peak concentration. The null
hypothesis states that this ratio lies outside the regulatory acceptance limits of 0.80 and 1.25. The data
come from replicate crossover studies where subjects receive the formulations in successive periods and the
reference product is given at least twice. The agent claims bioequivalence and rejectsH0 when the computed
confidence interval lies entirely within these limits. The agent can also defer a study to a human. In Example
2 users of a shopping application are randomized to the current version or to a new feature over 14 days.
The true change represents the difference in the share of users who make a purchase. The agent uses the
statistics engine of the GrowthBook platform and makes launch decisions according to the rule specified by
each version. A false launch constitutes a Type I error. In the experiment Claude Sonnet 5.5 proposes one
update per round. The update either changes a setting or introduces a new decision rule. Each method is
run 20 times for 10 rounds. Example 1 also tests the open-weight models Qwen 3.8 and DeepSeek-R1 as
developers under three of the methods.
3

2 Results
2.1 Why Common Validation Strategies Can Fail to Control Type I Error for
Evolving AI Analysts
Three commonly used statistical strategies can each fail to control the Type I error rate of an
evolving AI analyst for different reasons.
First, validating each statistical tool separately does not validate an analyst that combines
them. In a bioequivalence example, two tests each control the Type I error rate near 0.05, but
applying the second whenever the first fails to show bioequivalence raises it to 0.0587, as shown in
Fig. A1Ain the Appendix. Theorem A2 in the Appendix provides a general result.
Second, evaluating every proposed update at a fixed confidence level [33] does not control
the risk over many updates. Even when each update is evaluated using new simulated data, the
probability of approving a version whose Type I error rate is too high can accumulate. If every
proposed version has a Type I error rate above the target and independently passes validation with
probabilityη, the probability that at least one such version passes withinGupdates is1−(1−η)G,
which approaches one asGgrows. Fig. A1Bin the Appendix shows this effect.
Third, repeatedly evaluating updates on the same benchmark [36] can lead to overfitting. As
updates are developed using the same test cases or their feedback, they may perform well on the
benchmark without controlling Type I error on new data. In an extreme example, an updated
version can reproduce the decisions of a valid reference analysis on every stored test case but reject
the null hypothesis on all other datasets. It would pass the benchmark evaluation while having
a Type I error rate of one on new data from a continuous distribution, as Proposition A3 in the
Appendix shows.
2.2 Continual Validation Maintains Type I Error Control at Modest Cost
Continual validation, outlined in Fig. 1Aand Algorithm 1, addresses these problems simultaneously.
Evaluating an evolving AI analyst requires controlling the Type I error rate across diverse data
distributions and operational settings. For example, in a bioequivalence study, the null hypothesis
holds when the true drug exposure ratio is at or beyond the acceptance limits of 0.80 and 1.25 for
most drugs, and the error rate can vary with sample size, within-subject variability, and dropout
rate. We therefore evaluate an analyst under different null scenarios, each specifying a data-
generating process under which the null hypothesis is true. For instance, one scenario consists of
36 volunteers, 10 percent dropout, and a true exposure ratio at the upper acceptance limit, with
volunteers resampled from a published study. For a versionvand a null scenarioθ, we denote its
Type I error rate bye(v,θ).
Given the proposed version, the validator simulatesmr datasets from each null scenario for
updater, and runs the updated version alongside a reference analyst versionv0, where the reference
analysis can be a standard statistical procedure run at levelα0, with a known upper boundbθ on
its Type I error rate in scenarioθ. Using these simulated datasets, the validator computes an exact
upper confidence boundBθ on the updated version’s Type I error rate. An update is deployed only
ifB θ is at most the validation levelα′ in every scenario. Here,αis the target Type I error rate
for each decision, whileδbounds the lifetime probability of ever deploying a version whose Type I
error rate exceedsα′. We setα′ = (α−δ)/(1−δ)so thatα ′ + (1−α ′)δ=α. For a target Type
I error level such asα= 0.05and lifetime riskδ= 0.005, this givesα ′ = 0.0452. For updater,
the validator constructs each boundBθ at confidence level1−δ r, whereδ r = 6(δ−δ 0)/(π2r2).
These error budgets sum toδ−δ0 over all updates, with the remainingδ0 reserved for the reference
4

Algorithm 1Continual validation
GivenType I error levelα, lifetime riskδ, reference riskδ 0, initial null scenariosS 0, reference
analysisv 0 with boundsbθ
1:Setα ′←(α−δ)/(1−δ)andS←S 0
2:Deployv 0, or a version that rejects only wherev0 does, ifbθ≤α′ for everyθ∈S 0. Otherwise,
start with a version that defers every study.
3:foreach proposed updater= 1,2,...do
4:Freeze the updated versionv r
5:Add scenarios toSfor any new inputs used byv r, each with a reference boundbθ
6:SetS r←S
7:Setδ r←6(δ−δ 0)/(π2r2)and fix the numbermr of datasets per scenario
8:Simulatem r new datasets from eachθ∈S r
9:Runv r andv 0 on the same datasets
10:For eachθ∈S r, count rejectionsXθ ofv r, added rejectionsN + θ , and removed rejections
N− θ
11:LetU(x;m,η)andL(x;m,η)be the exact one-sided binomial bounds forxevents inm
trials at confidence level1−η[38]
12:B pair θ ←b θ +U(N + θ ;mr,δr/4)−L(N − θ ;mr,δr/4)
13:B dir θ ←U(X θ;mr,δr/2)
14:B θ←min(B pair θ ,B dir θ )
15:IfB θ≤α′ for everyθ∈S r, deployvr. Otherwise, retain the current version.
16:Report the deployment decision to the proposer
17:end for
boundsb θ. The initial setS0 of null scenarios is specified in advance and expanded when an update
uses information not varied by the existing scenarios.
The following theorem establishes that the lifetime risk remains controlled, regardless of how
many updates are proposed or how they are selected.
Theorem 1(Lifetime risk control).Suppose Algorithm 1 is followed and the reference bounds
bθ hold simultaneously except with probability at mostδ0. Then, regardless of how updates are
proposed, we have
Pr
{
∃r:v r passes,max θ∈Sr e(vr,θ)>α ′
}
≤δ 0 +
∑
r≥1
δr =δ,
wherev r is the version proposed in updaterandSr is its set of null scenarios.
Theorem 1 guarantees that the probability of ever deploying a version whose Type I error rate
exceedsα′ in any tested null scenario is at mostδ, regardless of the number or selection of updates.
The following corollary establishes Type I error control for every subsequent decision made by the
AI analyst.
Corollary 1(Type I Error Control for Every Decision).Let the analyst follow Algorithm 1.
Consider any future studyswhose data follow a null scenario covered by the version deployed
before the study data arrive. The probability of incorrectly rejectingH0 satisfies
Pr
θ
{rejectH 0 in studys}≤α ′ + (1−α ′)δ=α.
5

Corollary 1 establishes that each decision in a validated null scenario controls Type I error at
the target levelα, even after an unlimited number of adaptive updates. We call this property
lifetime validity.
Controlling Type I error alone would be trivial if no updates were ever approved. We therefore
also show that continual validation allows updates whose Type I error rate is sufficiently belowα′
to pass with high probability.
Proposition 1(Valid updates pass).Consider updaterwithJ r =|S r|null scenarios. Suppose
the proposed versionvr has Type I error rate at mostα′−γin every scenario, where0< γ < α′
is the margin below the validation level. For any0<ζ <1, the update passes with probability at
least1−ζifm r≥ 8α′ γ2 log max{2/δr,Jr/ζ}.
This proposition shows that updates with Type I error rates sufficiently belowα′ can be ap-
proved reliably. For a fixed number of scenarios, the required number of simulated datasets grows
only logarithmically with the update number. For updates that never add rejections relative to the
reference analysis, the guarantee is even stronger. Ifbθ≤α′−γin every scenario, such updates
are guaranteed to pass validation whenevermr≥log(4/δ r)/γ.
Although continual validation requires repeated simulations, its computational cost can be
reduced in two ways. First, it can avoid expensive language model calls. When an analyst follows a
fixed set of allowed analysis paths, each ending in a decision computed by fixed code, the validator
canevaluatethesedecisionsdirectlywithoutrunningthelanguagemodel. Thefollowingproposition
justifies this approach.
Proposition 2(Allowed paths).Suppose every run of an AI analyst follows one of a fixed set of
allowed paths, each producing a decision that is a function of the data. Then its Type I error rate
in every scenario is at most that of the any-path rule, which rejects whenever any allowed path
rejects, regardless of which language model is used or how it selects among the paths.
The choice of analysis path can vary substantially across models, even for the same data and
analysisoptions, asTableA13intheAppendixshows. Theany-pathruleinProposition2makesthe
guarantee independent of which path the model selects. Thus, validating the any-path rule avoids
language model calls, and subsequent model replacements, prompt edits, or provider updates that
preserve the allowed paths require no additional simulation.
Second, forupdatesthatrequirevalidation, comparingtheirdecisionswiththereferenceanalysis
on the same simulated datasets can substantially reduce the number of simulations needed, as
Fig. A1Cin the Appendix shows.
2.3 Two Evolving AI Analysts
We studied continual validation in two AI analysts that kept changing, an agent that decides
whether a test product is bioequivalent to its reference product and an analyst that decides whether
to launch a new product feature. Fig. 1Boutlines both. In each, the language model Claude
Sonnet 5.5 acted as the developer of the analyst. In each of ten rounds, it proposed one update
after reviewing a performance report and the validation feedback from its earlier proposals.
In both experiments, while a language model plans the workflow, deterministic tools execute the
computations. This architecture allows us to bypass expensive model calls and efficiently evaluate
the agents at scale through their underlying rules, as section A7.10 of the Appendix details. Each
run started with a conservative baseline test. The developer was then tasked with safely increasing
statistical power and automation.
We compared five deployment methods.
6

•No validation deploys every update without any check.
•The static benchmark evaluates update on the same fixed set of simulated studies [29].
•The improvement test deploys an update when a lower confidence bound on its gain in power
over the current version is positive [35, 36].
•Learn then Test evaluates a predefined set of configurations once before the first update [37].
•Continual validation runs withα= 0.05andδ= 0.005.
Each deployment method ran twenty times from the same initial version. The Type I error
rate and power of every deployed version were estimated afterwards from independent simulations,
on the validation scenarios and on off-grid scenarios that no method simulated. Power is reported
relative to an oracle which, in its own runs with the same developer, deploys an update only if
its estimated Type I error rate is at mostα′ in every validation scenario and its estimated power
exceeds that of the current version.
Example 1, an Agent That Analyzes Bioequivalence Studies
A test product is approved on several kinds of evidence, and one of them is a bioequivalence study,
which tests whether the test product delivers the active substance to the body like the reference
product [39, 12, 40, 41]. Bioequivalence assessment spans many designs, endpoints, and acceptance
rules [42, 43, 40], and our example covers one common part of it: average bioequivalence from
pharmacokinetic endpoints in replicate crossover studies. Healthy volunteers take the test product
and the reference product in successive periods, the reference at least twice, and the exposure in
each period is summarized by the area under the concentration curve and the peak concentration.
Evaluating bioequivalence can be formulated as performing the following hypothesis test:
H0 :the two products are not bioequivalent
H1 :the two products are bioequivalent
In practice, the test is based on whether the true ratio of their geometric mean exposures lies
outside the 0.80 to 1.25 interval (H0), or within it (H1). An analyst claims bioequivalence when
the 90 percent confidence interval for the ratio lies within this range, which corresponds to the two
one-sided tests at level 0.05 [11]. For highly variable drugs, whose reference product has a within-
subject coefficient of variation above 30 percent, regulatory agencies widen these limits based on
observed variability [44, 45, 46].
A statistician performing this analysis checks the protocol, prepares the data, fits the model,
runs diagnostics, and computes the interval, with judgment at each step. Our AI analyst is an
agent (https://be.statrust.ai/) that carries out these steps with tools under the direction of
language models, writes reports, and claims bioequivalence, retains the null hypothesis, or defers
the study to a human. Our experiment uses an early, simplified configuration of this broader
agent, which continues to evolve through updates evaluated by continual validation. To evaluate
proposed updates to this workflow, we used realistic null scenarios resampled from published studies
[47, 48]. This exposed the analyst to complex clinical edge cases, including the 30 percent variability
threshold where regulatory limits shift and errors easily inflate [49, 50].
Fig. 2AtoDsummarize the results. We highlight three key findings.
First, continual validation successfully controls the Type I error rate while enabling the analyst
to safely evolve and achieve higher statistical power. Continual validation deployed no version above
α′ in any of the 20 runs, and no deployed version had an estimated Type I error rate above 0.045
on the validation scenarios as shown in Fig. 2BandC. The final version of the analyst achieved a
7

power of 0.79 while maintaining a true Type I error rate of 0.043. Across all 200 rounds, the analyst
proposed 112 distinct versions. Furthermore, 32 percent of these updates introduced entirely new
decision rules, creating the unique evolutionary trajectories shown in Fig. 2A.
Second, comparison methods fail to balance capability evolution and Type I error control, as
Fig. 2BtoDshow. Both no validation and the improvement test failed to control the Type I error
rate. They deployed versions aboveα= 0.05in every run and reached error rates up to 0.098. The
static benchmark failed to detect when the Type I error rate exceededαand deployed versions
above this level in 20 percent of runs. Learn then Test strictly controls the Type I error rate but
only evaluates predefined options. Because it cannot evaluate novel decision rules proposed by the
analyst, it achieved only 52 percent of the oracle power. Continual validation evaluates these novel
rules while controlling the Type I error rate. It never exceeded the adjusted boundα′, reached
a maximum Type I error rate of 0.045, and attained the highest power among all methods that
controlled the Type I error rate. Continual validation reached a mean final power of 82 percent of
the oracle’s and the highest among the methods that deployed no version aboveα.
Third, continual validation is robust. Although continual validation requires constructing null
scenarios, its deployed versions maintained estimated Type I error rates at or below 0.05 on at least
666 of 690 off-grid scenarios (96.5%). The few exceedances, reaching at most 0.058, occurred only
under response-dependent dropout in two datasets not used for validation. By drawing random
scenarios, continual validation drives the analyst to evolve toward population-level performance
rather than overfitting to a fixed testing grid. In an additional experiment shown in Fig. 3, this
randomization successfully rejected twelve updates that inflated the Type I error rate at off-grid
sample sizes. Under this setting, the method retained 79 percent of the oracle power. Finally, these
results hold across different language models. Substituting Qwen or DeepSeek produced identical
patterns. The comparison methods failed to control the Type I error rate, while continual validation
maintained strict control, as section A7.8 of the Appendix details.
Example 2, an Analyst of Product Experiments
Online companies evaluate new product features through controlled experiments, commonly known
as A/B tests [51, 52]. Our example focuses on a two-arm experiment over 14 days. The primary
metric is conversion, with revenue and engagement as secondary goals. Evaluating the new feature
can be formulated as performing the following hypothesis test
H0 :the new feature does not improve conversion
H1 :the new feature improves conversion
RejectingH 0 means launching the feature, and launching an ineffective feature constitutes a Type I
error. Common analytical choices, such as evaluating data every day or selectively choosing metrics
after seeing the results, severely inflate this error [53, 25]. We built the analyst on GrowthBook,
an open-source experimentation platform [54]. The initial version uses daily purchase data to
compare conversion rates and bases its launch decision on the day-14p-value. The developer was
instructed to safely launch effective features more often and earlier. To evaluate proposed updates,
we simulated null experiments featuring heavy-tailed revenue, correlated metrics, and multiple user
segments, alongside dynamic scenarios targeting complex updates like daily data evaluations and
new decision rules.
The results in Fig. 2EtoHshow that continual validation deployed no version with a Type
I error rate aboveα′ = 0.0452in any run. Of the 30 rejected updates, 28 had Type I error rates
aboveα′, while the remaining two had rates of 0.0435 and 0.0434, slightly belowα′. In one run,
the analyst proposed checking the data daily, which raised the Type I error rate to 0.17. Continual
8

validation rejected this update. In response to this feedback, the analyst autonomously developed
a new decision rule that allowed early launches only for very smallp-values and used an adjusted
threshold on day 14. The final version achieved a power of 0.21 with a true Type I error rate of
0.043. Across all runs, the analyst proposed 62 distinct versions, and 21 percent of its updates were
new decision rules.
Comparison methods failed to consistently balance statistical power and Type I error control.
No validation and the improvement test deployed versions aboveα= 0.05in 60 and 95 percent of
runs, reaching error rates up to 0.183 and 0.817. The static benchmark deployed no version above
α′ and reached 98% of the oracle’s power in Example 2. This was because all six updates that
would have exceededα= 0.05did so in scenarios covered by its fixed benchmark. In Example
1, by contrast, harmful updates exceededαin scenarios outside the fixed benchmark. Learn then
Test deployed no version aboveαbut could not deploy new decision rules, reaching only 80 percent
of the oracle power. Continual validation safely evaluated these novel rules, never exceeded the
adjusted boundα ′, and attained 96 percent of the oracle power. Furthermore, On 116 off-grid
scenarios, its deployed versions had estimated Type I error rates of at most 0.044.
3 Discussion
Type I error control need not end when a decision procedure starts to change. Continual validation
extends this guarantee from a fixed procedure to an adaptively evolving, potentially unlimited
sequence of AI analyst versions. Simulating datasets under the null hypothesis accounts for data
sampling, while evaluating each frozen version accounts for the analyst’s internal randomization.
Freezing each update before simulating its validation data and controlling the lifetime probability
of approving an invalid version prevents overfitting during the adaptive selection of the analyst.
Together, these steps ensure that the probability of ever approving an invalid version remains
bounded and that each deployed decision strictly controls the Type I error.
Several features distinguish continual validation from existing methods for evaluating and up-
dating AI systems [35, 36, 34]. First, it directly controls the Type I error of statistical decisions,
whereas methods that check only improvements in performance do not. A performance-based de-
ployment criterion can still be added without affecting the statistical guarantee. Second, simulating
new data after each update is frozen allows updates to be proposed adaptively, including by the
analyst itself. Third, comparing every update with the same fixed reference analysis reduces simu-
lation costs and avoids accumulating differences relative to successive versions. Finally, validating
the allowed analysis paths can cover model replacements and prompt changes without additional
simulation. Unlike Learn then Test, which calibrates a finite menu of configurations fixed in advance
[37], continual validation also accommodates previously unanticipated updates, including new deci-
sion rules written by the analyst. Regulators already use simulation over nuisance parameter grids
for adaptive clinical trials [55] and provide for predetermined change control plans for AI-enabled
medical software [56]. Continual validation could provide a statistical framework for evaluating
updates under such plans.
A limitation is that the theoretical guarantee strictly applies to the null scenarios covered by
validation. It does not automatically provide a mathematical bound for unobserved data generating
patterns. However, our experiments demonstrate that continual validation remains highly robust
in practice. The deployed versions successfully maintained Type I error control even on unseen
off-grid scenarios. Furthermore, developers can easily expand the validation scenarios as the AI
system gains new capabilities. Moreover, drawing randomly sampled scenarios naturally extends
the theoretical safety guarantee to the broader data population. This prevents the AI analyst
9

1 5 10
Update round
1
2
3
4
5
6
7
8
9
10
Run
0 2 4 6 8 10
Update round
0.00
0.02
0.04
0.06
0.08
0.10
Largest Type I error rate
above α
α′
α
0 50 100
Runs above α (%)
No validation
20/20
Static benchmark
4/20
Improvement test
20/20
Learn then Test
0/20
Continual validation
0/20
0 2 4 6 8 10
Update round
0.0
0.2
0.4
0.6
0.8
1.0
Power
oracle
1 5 10
Update round
1
2
3
4
5
6
7
8
9
10
Run
0 2 4 6 8 10
Update round
0.00
0.05
0.10
0.15
0.20
Largest Type I error rate
above α 0.82
α′
α
0 50 100
Runs above α (%)
No validation
12/20
Static benchmark
0/20
Improvement test
19/20
Learn then Test
0/20
Continual validation
0/20
0 2 4 6 8 10
Update round
0.0
0.1
0.2
0.3
0.4
0.5
0.6
Power
oracle
Example 1, bioequivalence agent
A B C D
Example 2, analyst of product experiments (GrowthBook)
E F G H
Updates in continual validation Type I error of deployed version Runs ever above α Power of the deployed version
Deployment methods
Updates in A and E
No validation Static benchmark Improvement test Learn then Test Continual validation
within α′ above α′ above α not deployed new decision rule malformed
Figure 2:Continual validation and four comparison methods evaluated across two evolving AI analysts.
Each method was tested in 20 independent runs of 10 rounds from the same initial version. In each round,
Claude Sonnet 5.5 acted as the developer and proposed one update based on feedback from earlier rounds.
(AtoD) Bioequivalence analyst. (EtoH) Product experiment analyst. (AandE) Updates proposed under
continual validation in the first ten runs, with one row per run. Circles denote setting changes, squares
denote new decision rules, and crosses denote malformed updates. Filled markers indicate deployed updates.
Colors indicate the true Type I error rate of the proposed version, showing rates withinα′ (grey), aboveα ′
(pink), and aboveα(dark red). (BandF) Largest true Type I error rate of the deployed version over the
full validation set after each round. Lines show the median over runs and bands extend to the worst run for
no validation (vermilion), the static benchmark (orange), the improvement test (bluish green), Learn then
Test (sky blue), and continual validation (blue). The dashed line marks the validation levelα′ = 0.0452, the
dotted line marks the target levelα= 0.05, and the shaded region lies aboveα. InF, the axis ends at 0.2
and an arrow indicates the largest rate in the worst run of the improvement test. (CandG) Share of runs
that ever deployed a version aboveα, showing Wilson 95 percent intervals and the raw count out of 20 runs.
(DandH) Mean true statistical power of the deployed version after each round. The dashed line represents
an oracle that deploys only valid updates that strictly increase power.
from overfitting to a fixed testing grid and ensures it safely evolves toward true population-level
performance. The method is applicable wherever relevant null scenarios can be simulated and the
AI system can be evaluated at sufficient scale.
Although we focus on Type I error, the framework requires only valid upper confidence bounds
on the risk being controlled. It can therefore extend to other statistical error measures, such
as the false discovery rate of a screening agent, when suitable confidence bounds are available.
Overall, continual validation provides a practical deployment framework for AI systems. It allows
AIanalyststocontinuouslyimprovetheirstatisticalpowerandadapttonewtaskswhilemaintaining
10

0 2 4 6 8 10
Update round
0.00
0.02
0.04
0.06
Largest Type I error rate
α
α′
Deployed
Refused
Inflates error off the grid
0 2 4 6 8 10
Update round
0.0
0.2
0.4
0.6
Power
100%
79%
A Type I error at off-grid sample sizes B Power in 20 runs
Continual validation with random scenarios Oracle
Figure 3:Continual validation with random scenarios in the bioequivalence analyst. (A) Largest true Type
I error rate of the deployed version at sample sizes of 30, 42, and 60, outside the original validation grid of
24, 36, and 48. Filled circles indicate deployed versions, while open circles indicate rejected updates. Orange
circles highlight four rejected updates that would increase Type I error outside the original grid while leaving
the analysis unchanged on the grid. The dashed and dotted lines mark the validation levelα′ = 0.0452and
the target levelα= 0.05, respectively. The shaded region indicates rates aboveα. (B) Mean true power of
the deployed version across 20 runs with Claude Sonnet 5.5 proposing updates. The dashed line shows the
oracle in Fig. 2, and the percentages indicate power relative to the oracle after ten rounds.
rigorous safety guarantees throughout their working lives.
4 Methods
4.1 Decisions, Versions, and Type I Error
An AI analyst maps the data of a study, including its protocol, to one of three decisions, to reject
the null hypothesis, to retain it, or to defer to a human. A deferral never counts as a rejection,
so the guarantee concerns the decisions the analyst makes on its own. A versionvis a complete
specification of everything that can change the decision, including the language model and its
sampling settings, the prompts, the allowed tools and skills, the workflow, the code, and decision
thresholds. A deployed version decides each study using that study’s data and its own internal
randomness, without updating decision-relevant memory across studies. Information from earlier
studies may inform future updates, which are validated before deployment. For a null scenario
θ, the Type I error ratee(v,θ)is the probability thatvrejects, over the data and the internal
randomness. We assume that a real study whose true state is a validation scenario produces data
with the distribution from which the validator simulates, and that a version cannot tell simulated
studies from real ones, which the Appendix states as Assumption A1.
4.2 Validation of an Update
The boundsU(x;m,η)andL(x;m,η)of Algorithm 1 are the exact one-sided Clopper and Pearson
bounds [38]. Their levelsδr/4,δ r/4, andδr/2add up toδ r, so by a union bound all three bounds
of a scenario hold together with probability at least1−δr. Because an update passes only if every
scenario passes, the intersection-union argument [57] of Theorem A6 in the Appendix shows that
no division ofδr among the scenarios is needed. Random scenarios drawn after the freeze enter a
round with the analytic bound of the reference analysis where one exists andbθ = 1otherwise, as
11

described in section A4.6 of the Appendix.
4.3 Reference Analysis and Lifetime Risk
The reference analysis is the standard analysis of the field, run at a reference levelα0 belowα′. For
the two one-sided tests on Gaussian scenarios with dropout that does not depend on the responses,
its Type I error rate is at mostα0 [11], which Theorem A10 in the Appendix confirms for every
design used here, so thatbθ =α 0 at no simulation cost. On scenarios built from real studies or with
non-Gaussian data, the reference analysis receives a one-time validation that holds simultaneously
over these scenarios, including those that later updates may add, and usesδ0 of the lifetime risk.
Each round simulates allmdatasets in every scenario before the deployment decision, because
optional stopping would invalidate the exact bounds. We useα= 0.05,δ= 0.005andδ 0 = 0.001,
withα 0 = 0.030in Example 1 andα0 = 0.040in Example 2, and section A4 of the Appendix gives
the proofs.
4.4 Conditions for Deployment
The validator must be able to run each version on simulated studies, either through its allowed
paths or in full. An analyst that learns from each study keeps its memory frozen while a version
is in force. The random seeds of a round are drawn after its freeze. Each study is decided by
one binding run, because rerunning a stochastic version until it rejects is a different procedure.
A version validated in full pins its hosted model to a fixed snapshot, whereas a version validated
through its allowed paths is protected against silent model updates by Proposition 2.
Acknowledgments
The research of Xiao Wang was supported in part by the National Science Foundation under Grant
SES-2316428, by Anthropic through its AI for Science program, and by Lilly Purdue Innovation
Institute.
References
[1] C. Lu, et al., Towards end-to-end automation of AI research.Nature651, 914–919 (2026).
[2] K. Swanson, W. Wu, N. L. Bulaong, J. E. Pak, J. Zou, The Virtual Lab of AI agents designs
new SARS-CoV-2 nanobodies.Nature646, 716–723 (2025).
[3] S. Alber, et al., CellVoyager: AI CompBio agent generates new insights by autonomously
analyzing biological data.Nature Methods23, 749–759 (2026).
[4] H. G. Zhang, P. Eckmann, J. Miao, A. B. Mahon, J. Zou, The Virtual Biotech: A multi-agent
AI framework for therapeutic discovery and development.Science(2026).https://doi.org/
10.1126/science.aeg6779(accessed 6 October 2026).
[5] Z. Chen, et al., ScienceAgentBench: Toward rigorous assessment of language agents for data-
driven scientific discovery inInternational Conference on Learning Representations. (2025).
[6] B. P. Majumder, et al., DiscoveryBench: Towards data-driven discovery with large language
models inInternational Conference on Learning Representations. (2025).
12

[7] J. S. Chan, et al., MLE-bench: Evaluating machine learning agents on machine learning
engineering inInternational Conference on Learning Representations. (2025).
[8] F. Nie, et al., DSGym: A holistic framework for evaluating and training data science agents.
arXiv [Preprint](2026).https://arxiv.org/abs/2601.16344(accessed 6 October 2026).
[9] K. Huang, et al., Automated hypothesis validation with agentic sequential falsifications inPro-
ceedings of the 42nd International Conference on Machine Learning, Proceedings of Machine
Learning Research. Vol. 267, pp. 25372–25437 (2025).
[10] J. Miao, J. Mu, G. Chen, J. Zou, Fisher-R1: Training LLM agents for reliable hypothesis
testing.arXiv [Preprint](2026).https://arxiv.org/abs/2608.07437(accessed 6 October
2026).
[11] D. J. Schuirmann, A comparison of the two one-sided tests procedure and the power approach
for assessing the equivalence of average bioavailability.Journal of Pharmacokinetics and Bio-
pharmaceutics15, 657–680 (1987).
[12] International Council for Harmonisation, ICH M13A guideline on bioequivalence for
immediate-release solid oral dosage forms, (ICH), Harmonised guideline (2024).
[13] J. Neyman, E. S. Pearson, On the problem of the most efficient tests of statistical hypotheses.
Philos. Trans. R. Soc. Lond. A231, 289–337 (1933).
[14] E. L. Lehmann, J. P. Romano,Testing Statistical Hypotheses(Springer, ed. 4, 2022).
[15] M. Bertran, R. Fogliato, Z. S. Wu, Many AI analysts, one dataset: Navigating the agentic
data science multiverse.Proc. Natl. Acad. Sci. U.S.A.123, e2606495123 (2026).
[16] J. Miao, J. K. Pritchard, J. Zou, The agentic garden of forking paths.arXiv [Preprint](2026).
https://arxiv.org/abs/2607.01507(accessed 6 October 2026).
[17] K. D. Tocher, Extension of the Neyman-Pearson theory of tests to discontinuous variates.
Biometrika37, 130–144 (1950).
[18] L. Chen, M. Zaharia, J. Zou, How is ChatGPT’s behavior changing over time?Harvard Data
Science Review6(2024).
[19] J. Schmidhuber, Gödel machines: Fully self-referential optimal universal self-improvers in
Artificial General Intelligence, B. Goertzel, C. Pennachin, Eds. (Springer, 2007), pp. 199–226.
[20] E. Zelikman, E. Lorch, L. Mackey, A. T. Kalai, Self-taught optimizer (STOP): Recursively
self-improving code generation inConference on Language Modeling. (2024).
[21] J. Zhang, S. Hu, C. Lu, R. Lange, J. Clune, Darwin Gödel Machine: Open-ended evolution of
self-improving agents inInternational Conference on Learning Representations. (2026).
[22] N. Shinn, F. Cassano, A. Gopinath, K. Narasimhan, S. Yao, Reflexion: Language agents with
verbal reinforcement learning inAdvances in Neural Information Processing Systems. Vol. 36,
pp. 8634–8652 (2023).
[23] M.Yuksekgonul, etal., OptimizinggenerativeAIbybackpropagatinglanguagemodelfeedback.
Nature639, 609–616 (2025).
13

[24] Q. Zhang, et al., Agentic context engineering: Evolving contexts for self-improving language
models inInternational Conference on Learning Representations. (2026).
[25] J. P. Simmons, L. D. Nelson, U. Simonsohn, False-positive psychology: Undisclosed flexibility
in data collection and analysis allows presenting anything as significant.Psychological Science
22, 1359–1366 (2011).
[26] R. Silberzahn, et al., Many analysts, one data set: Making transparent how variations in
analytic choices affect results.Advances in Methods and Practices in Psychological Science1,
337–356 (2018).
[27] A. N. Angelopoulos, S. Bates, C. Fannjiang, M. I. Jordan, T. Zrnic, Prediction-powered infer-
ence.Science382, 669–674 (2023).
[28] Y. Jin, et al., TxConformal: Controlling false discoveries in AI-driven therapeutic discovery.
bioRxiv [Preprint](2026).https://doi.org/10.64898/2026.04.27.721076(accessed 6 Oc-
tober 2026).
[29] C. Dwork, et al., The reusable holdout: Preserving validity in adaptive data analysis.Science
349, 636–638 (2015).
[30] Y. Benjamini, Selective inference: The silent killer of replicability.Harvard Data Science
Review2(2020).
[31] J. Tian, A. Ramdas, Online control of the familywise error rate.Statistical Methods in Medical
Research30, 976–993 (2021).
[32] P. Bauer, K. Köhne, Evaluation of experiments with adaptive interim analyses.Biometrics
50, 1029–1041 (1994).
[33] P. S. Thomas, et al., Preventing undesirable behavior of intelligent machines.Science366,
999–1004 (2019).
[34] J. Feng, S. Emerson, N. Simon, Approval policies for modifications to machine learning-based
software as a medical device: A study of bio-creep.Biometrics77, 31–44 (2021).
[35] B. Sengupta, Self-evolving agents with anytime-valid certificates.arXiv [Preprint](2026).
https://arxiv.org/abs/2607.00871(accessed 6 October 2026).
[36] X. Sun, Y. Zeng, Z. She, X. Wang, Which self-improvements should we trust? Reliable self-
improvement when agents reuse their benchmarks.arXiv [Preprint](2026).https://arxiv.
org/abs/2609.33180(accessed 6 October 2026).
[37] A. N. Angelopoulos, S. Bates, E. J. Candès, M. I. Jordan, L. Lei, Learn then test: Calibrating
predictive algorithms to achieve risk control.The Annals of Applied Statistics19(2025).
[38] C. J. Clopper, E. S. Pearson, The use of confidence or fiducial limits illustrated in the case of
the binomial.Biometrika26, 404–413 (1934).
[39] European Medicines Agency, Guideline on the investigation of bioequivalence, (Committee for
Medicinal Products for Human Use), Guideline CPMP/EWP/QWP/1401/98 Rev. 1 (2010).
[40] U.S. Food and Drug Administration, Statistical approaches to establishing bioequivalence,
(FDA), Guidance for industry (2026).
14

[41] B. M. Davit, et al., Comparing generic and innovator drugs: A review of 12 years of bioequiva-
lence data from the United States Food and Drug Administration.Annals of Pharmacotherapy
43, 1583–1597 (2009).
[42] S.-C.Chow, J.-P.Liu,Design and Analysis of Bioavailability and Bioequivalence Studies(Chap-
man & Hall/CRC, ed. 3, 2008).
[43] D. Hauschke, V. Steinijans, I. Pigeot,Bioequivalence Studies in Drug Development: Methods
and Applications(Wiley, 2007).
[44] L. Tóthfalusi, L. Endrényi, A. García-Arieta, Evaluation of bioequivalence for highly variable
drugs with scaled average bioequivalence.Clinical Pharmacokinetics48, 725–743 (2009).
[45] B. M. Davit, et al., Implementation of a reference-scaled average bioequivalence approach for
highly variable generic drug products by the US Food and Drug Administration.AAPS J.14,
915–924 (2012).
[46] V. Karalis, M. Symillides, P. Macheras, Bioequivalence of highly variable drugs: A comparison
of the newly proposed regulatory approaches by FDA and EMA.Pharmaceutical Research29,
1066–1077 (2012).
[47] H. Schütz, M. Tomashevskiy, D. Labes, replicateBE: Average bioequivalence with expanding
limits (ABEL) (R package version 1.1.3, CRAN) (2022).https://doi.org/10.32614/CRAN.
package.replicateBE(accessed 6 October 2026).
[48] H. Schütz, et al., Reference datasets for studies in a replicate design intended for average
bioequivalence with expanding limits.AAPS J.22, 44 (2020).
[49] D. Labes, H. Schütz, Inflation of type I error in the evaluation of scaled average bioequivalence,
and a method for its control.Pharmaceutical Research33, 2805–2814 (2016).
[50] J. Muñoz, D. Alcaide, J. Ocaña, Consumer’s risk in the EMA and FDA regulatory approaches
for bioequivalence in highly variable drugs.Stat. Med.35, 1933–1943 (2016).
[51] R. Kohavi, D. Tang, Y. Xu,Trustworthy Online Controlled Experiments: A Practical Guide
to A/B Testing(Cambridge University Press, 2020).
[52] N. Larsen, et al., Statistical challenges in online controlled experiments: A review of A/B
testing methodology.The American Statistician78, 135–149 (2024).
[53] R. Johari, P. Koomen, L. Pekelis, D. Walsh, Peeking at A/B tests: Why it matters, and
what to do about it inProceedings of the 23rd ACM SIGKDD International Conference on
Knowledge Discovery and Data Mining. pp. 1517–1525 (2017).
[54] GrowthBook, Inc., GrowthBook: Open source feature flags, experimentation, and product
analytics (GitHub repository, statistics engine gbstats under the MIT License) (2026).https:
//github.com/growthbook/growthbook(accessed 7 October 2026).
[55] U.S. Food and Drug Administration, Adaptive designs for clinical trials of drugs and bio-
logics: Guidance for industry (Final guidance) (2019).https://www.fda.gov/media/78495/
download(accessed 6 October 2026).
15

[56] U.S. Food and Drug Administration, Marketing submission recommendations for a predeter-
mined change control plan for artificial intelligence-enabled device software functions: Guid-
ance for industry and Food and Drug Administration staff (Final guidance, originally issued 4
December 2024) (2025).https://www.fda.gov/media/166704/download(accessed 6 October
2026).
[57] R. L. Berger, Multiparameter hypothesis testing and acceptance sampling.Technometrics24,
295–300 (1982).
16

Appendix
A1 Setting and notation
The theory concerns an AI analyst that decides one study after another while its decision procedure
keeps changing. We define the objects first, then the Type I error rate that every guarantee controls,
and finally the property of lifetime validity. Table A1 collects the symbols used here and in later
sections.
A1.1 Studies and decisions
The analyst reads the dataDof a study, which include its protocol, and returns one of three
decisions,
Y∈{reject,retain,defer}.
Rejecting the null hypothesis is the consequential action that the evidence must support. Such
actions include reporting a discovery, launching a product feature and declaring a test product
bioequivalent to its reference product. Retaining the null hypothesis declines the action, and a
deferral hands the study to a human expert. A deferral is never counted as a rejection, and the
guarantees below concern the rejections that the analyst makes on its own.
The data-generating distribution of a study depends on the true state of the world. A scenarioθ
specifies this state completely, andPrθ denotes probability when the data of a study are drawn from
scenarioθ. In a bioequivalence study a scenario fixes the true ratio of geometric mean exposures,
which the null hypothesis concerns, and the within-subject and between-subject variability, which
are nuisance parameters. For highly variable drugs the within-reference variability also sets the
limits that define the null hypothesis. The scenario also fixes the sample size, the allocation to
sequences, the dropout pattern and the protocol the analyst reads.
LetΘ 0 be the set of null scenarios, those in which the null hypothesis holds and a rejection
is wrong. The null hypothesis is composite, since it holds in many scenarios. In bioequivalence
the null scenarios are those whose true ratio lies on or outside the regulatory limits for the true
variability. These limits are 80.00 and 125.00 percent when the true within-reference coefficient
of variation is at most 30 percent. Otherwise they are the widened limitsexp(±0.760σ wR)of
the European Medicines Agency (EMA) [1], capped at 69.84 and 143.19 percent and evaluated at
the true within-reference standard deviationσwR on the log scale, whereas the EMA’s rule itself
evaluates them at the observed standard deviationswR (section A7.4). With the limits of 80.00
and 125.00 percent the null hypothesis is|µ|≥∆for the log-ratioµand∆ = log 1.25. Scenarios
may be parametric, such as Gaussian models of a crossover study. They may also be built from
real studies by resampling their subjects and moving the true effect to the boundary of the null
hypothesis or beyond it. The validator can draw studies from every scenario it uses.
A1.2 Versions
A versionvof the AI analyst is one fixed configuration of everything that turns the data of a
study into a decision. It includes the language model with its identifier and sampling settings, the
instructions, and the tools and skills with their code. It also includes the statistical analyses and
their thresholds, the rules that send a study to an analysis or to a human, and the computing
environment. The analyst decides each study by running its current version.
17

A version determines its decision as a fixed function of the data and of the analyst’s internal
randomness,
Yv =y v(D,ξ),(A1)
whereξcollects every random choice the analyst makes. The randomnessξ, which includes the
samplingofalanguagemodel, isdrawnindependentlyofDfromadistributionthattheversionfixes.
Each version is therefore a randomized test, a decision rule that may use randomness independent
of the data, and two runs of one version on one study have the same distribution of decisions.
A version carries no memory from one study to the next. An analyst whose context grows with
every study it decides becomes a new version after each study. Its memory must therefore stay
frozen while a version is in force and change only through updates. Each study is also decided by
one binding run. Rerunning a stochastic version until it rejects is a different procedure, andK
runs of a version whose Type I error rate isacan reject with probability up to1−(1−a)K (the
example after Proposition A22).
Every change to any component produces a new version, and the theory treats all such versions
alike. An edited prompt, a new skill, an upgraded tool, a swapped model, a changed threshold and
a revision written by the analyst itself are all new versions. So is a hosted model that its provider
updates behind an unchanged name.
ThevalidatorofsectionA3runsaversionexactlyasitrunsindeployment, andsimulatedstudies
reach the version through the same input as real studies. One assumption links the scenarios to
the studies the analyst decides in the field.
Assumption A1(Faithful simulation).A real study whose true state isθproduces data with the
lawPr θ from which the validator draws. A version’s decision depends on a study only through its
dataDand its internal randomnessξ. In particular, a version cannot tell a simulated study from
a real one.
Under Assumption A1 the rejection rate of a version in a simulated scenario is its Type I error
rate on real studies in that state. The guarantees below are therefore statements about decisions
in the field. The assumption asks more of scenarios resampled from real studies than of para-
metric ones, because resampling can leave traces that real studies lack, such as repeated subjects.
Section A4 shows how far the guarantee reaches beyond the laws of the validation scenarios.
A1.3 Type I error rate
For a versionvand a scenarioθ∈Θ 0 the Type I error rate is
e(v,θ) = Prθ{Yv =reject},(A2)
the probability over the data of the study and the internal randomness of the analyst. For a set
S⊆Θ 0 we writee(v,S) = sup θ∈Se(v,θ), which is the size ofvonS. We callvvalid at levelaon
Sife(v,S)≤a. Power is the probability of a rejection in a scenario where the null hypothesis is
false. Power plays no part in the guarantees, and most updates try to raise it.
Throughout, every decision is held to the levelα= 0.05, and the lifetime risk isδ= 0.005. The
lifetime risk is the largest acceptable probability that validation ever passes an update whose Type
I error rate exceeds the validation level in one of its validation scenarios. Each validation uses the
validation levelα′ = (α−δ)/(1−δ) = 0.0452, the reference analysis introduced below runs at the
reference levelα 0 of the example (0.030 in Example 1 and 0.040 in Example 2), andδ0 is the part
ofδspent on the reference bounds (section A4).
18

A1.4 Scenario sets
The validator tests versions on finite sets of scenarios, the validation scenarios. They begin with the
initial scenario setS 0⊆Θ 0 ofJscenarios, which the validator fixes before the analyst’s working
life begins. The initial scenario set varies the factors that the validator expects to change decisions,
such as variability, sample size and dropout. It also contains null scenarios both at the boundary
of the null hypothesis and inside it. When an updated version reads a kind of information that no
scenario in the current set varies, the validator adds scenarios that vary it (section A4.5). Scenarios
are added and never removed, so the setSr in force at updateralways containsS 0. The validator
may also draw scenarios at random in each round, after the updated version is frozen, and use them
in that round only. These extend the guarantee for each deployed version to the space between the
fixed scenarios, except a set of small probability (Proposition A18). The proposer has no say in
which scenarios validation uses.
A1.5 An analyst that keeps changing
Over its working life the analyst receives updatesr= 1,2,..., and updateroffers a new versionvr,
the updated version. An update may come from anyone, and we call its source the proposer. The
proposer may be the analyst revising itself after a failure or an engineer editing its instructions.
It may also be an optimizer that maximizes power or an adversary searching for a version that
rejects too often. Each updated version passes or fails validation. A version that passes may be
deployed, and a deployed version decides every study whose data arrive afterward. An update that
fails changes nothing but still counts, because updates are counted by attempt.
The validator holds a reference analysisv0, a fixed decision procedure with reference boundsbθ
on its Type I error rates. These bounds have simultaneous coverage,bθ≥e(v 0,θ)for every scenario
ever used, except on an event of probability at mostδ0 (section A4). Whenbθ≤α′ for everyθ∈S 0,
the analyst starts its life with the reference analysis in force, or with a version that rejects only
where the reference analysis rejects (Corollary A21). Otherwise it starts with the version that
defers every study. In bioequivalence the reference analysis is the two one-sided tests procedure at
the reference levelα0 applied to the subjects with complete data (sections A3.6 and A7.3).
Studiess= 1,2,...arrive over time, each with a true scenarioθ s and a decisionYs. We write
v(s) for the version in force when the data of studysarrive.
A1.6 Lifetime validity
Definition A1(Lifetime validity).An analyst that keeps changing is lifetime valid at levelαon
a set of scenariosS⊆Θ 0 if every studysthat it ever decides, and whose true scenarioθs lies inS
almost surely, satisfies
Pr{Ys =reject}≤α,(A3)
where the probability is taken over everything that happens up to and including the decision. This
history consists of the updates, the validations, the earlier studies, the data of studysand the
internal randomness of the analyst.
Lifetime validity is a guarantee about each decision, under whichever version is in force, after
any number of changes chosen in any way. Corollary A12 shows that continual validation delivers
it on every scenario set on which all versions in force are validated, and Assumption A1 carries it
to the real studies in those states.
19

Table A1:Notation.
symbol meaning
D,ξdata of a study, internal randomness of the analyst
Yv∈{reject,retain,defer}decision of versionv
Ys,θ s decision on studys, true scenario of studys
θ,Θ 0 scenario, set of null scenarios
e(v,θ),e(v,S)Type I error rate inθ, worst case overS
aa level of validity, the target of a single validation
µ,∆log-ratio of the geometric means, equivalence limitlog 1.25
σwR,s wR true and observed within-reference standard deviation on the log scale
βi,f(i,j)effect of sequenceiin the crossover, formulation given in periodjof se-
quencei
Tµ,T κ tstatistics of the log-ratioµand of the sequence effectκ=β 1−β 2
S0,S r initial scenario set, scenario set of updater
J,J r number of scenarios inS0, number of scenarios in roundr
S(v)scenario set on whichvpassed validation or whose validity it inherits
v0,v r,v (s) reference analysis, updated version of updater, version in force for studys
R,vR set of allowed paths, any-path rule
ϕ,ϕ λ,Λanalysis, member of a routing family, index set of the family
Irouting information that selects an analysis
α,α′,α 0 Type I error level of every decision, validation level, reference level
δ,δ 0,δ r lifetime risk, reference risk (the part ofδspent on the reference bounds),
share of updater
δ0,θ,δ′ 0,δ 0,k level of the reference bound ofθ∈S 0, their sum, level of thekth added
scenario
bθ reference bound, a bound on the Type I error rate of the reference analysis
inθ
E0,Eevent that every reference bound holds, event that in addition no update
above the validation level passes
Ar event thatvr passes validation withe(vr,Sr)>α ′
m,m r,m 0 simulated studies per scenario in one round, in roundr, in the validation
of the reference analysis
Xθ,N + θ ,N − θ rejections of the version under validation, rejections it adds to those of the
reference analysis, rejections it removes
q+ θ ,q− θ probabilities of an added and of a removed rejection
U(x;m,η),L(x;m,η)exact one-sided upper and lower binomial bounds at levelη
η,ζlevel of a bound, allowed probability that a valid update fails
Bpair θ ,B dir θ ,B θ,B r,θ paired, direct and combined bounds of scenarioθ, combined bound ofθin
roundr
γmargin below the validation level
kl(x,y),ℓ,ℓ r relative entropy between Bernoulli distributions, logarithmic terms in the
numbers of simulated studies of Theorem A9 and Proposition A14
Gr,H s information at the freeze of roundr, at the arrival of studys
Π,Q r,K r,ε Π law, set and number of the random scenarios of roundr,Π-probability left
uncovered
Vr,Γ r set wherevr exceedsα′, event thatΠ(Vr)>ε Π and no random scenario of
roundrlies inV r
Fk,Ψ k number of false rejections among the firstkstudies of Corollary A13,Fk
minus the sum of their conditional probabilities
20

A2 Why common checks fail
A
two one-
sided tests
distribution-
free test
switch if
first fails
0.040
0.045
0.050
0.055
0.060
Type I error rate
5 percent
Combining valid tests fails B
1 10 100 1000
number of updates
0.00
0.25
0.50
0.75
1.00
probability a version above
α′ has been deployed
14 updates
95% check
99.5%
check
continual
validation
Fixed checks fail over time C
1 10 100 1000
update number
1,000
10,000
100,000
simulated datasets per
scenario to pass
without reference
adds some rejections
adds no rejections
Validation stays affordable
Figure A1:Why common checks fail and what validation costs. (A) Combining individually valid tests
can inflate Type I error. Two bioequivalence tests each control Type I error near 5 percent, but using the
second whenever the first fails exceeds this level. Dots show nine designs, each evaluated using 400,000
simulated studies. (B) Repeated validation at a fixed confidence level accumulates risk. The curves show the
probability of ever deploying a version aboveα′ when every proposed version lies just above this threshold.
Fixed 95 percent and 99.5 percent checks accumulate risk, whereas continual validation keeps it below the
lifetime levelδ. (C) Simulated datasets per scenario required for an update to pass validation as the update
number increases. Without reference comparison, a version with Type I error rateα0 passes with probability
0.9 (gray). With paired comparison, a version that adds no rejections passes with certainty (solid blue),
while one that adds rejections at rate(α′−α 0)/2passes with probability 0.9 (dashed blue). PanelsBand
Cuseα= 0.05,δ= 0.005,δ 0 = 0.001, andα 0 = 0.040, givingα ′ = 0.0452.
An analyst that changes freely can reject far more often than any check of a single version
suggests. Three mechanisms are at work, and each has an exact statement below. Valid analyses
do not compose, a check that reuses stored simulations can be defeated, and a check that is valid
for each version separately still fails over a long life.
A2.1 Valid analyses do not compose
An analysis is any decision ruleϕwith values reject and retain. It is valid at levelαife(ϕ,θ)≤α
for everyθ∈Θ 0.
Theorem A2(Valid analyses do not compose).Fixα∈(0,1)and an integerK≥2.
(i) Letϕ 1,...,ϕ K be analyses valid at levelα. Letvbe any version that rejects on a study
only when at least one ofϕ 1,...,ϕ K rejects on it, howevervchooses among them. Then
e(v,θ)≤min(1,Kα)for everyθ∈Θ 0.
(ii) The bound is attained. There are analysesϕ1,...,ϕ K withe(ϕ k,θ) =αfor everykand every
θ∈Θ 0, and a versionvof the kind in (i), such thate(v,θ) = min(1,Kα)for everyθ∈Θ 0.
Proof.(i) The rejection event ofvlies in the union of the rejection events of the analyses, so
e(v,θ)≤ ∑ ke(ϕk,θ)≤Kα, and a probability is at most one.
(ii) LetWbe uniform on[0,1)and independent of the data, as part of the internal randomness
of the analyst. Setc= min(α,1/K)and letϕ k reject when(W−(k−1)c) mod 1< α. Each
(W−(k−1)c) mod 1is uniform on[0,1), soe(ϕ k,θ) =αin every scenario. The rejection event of
ϕk is the arc of lengthαthat starts at(k−1)con the circle[0,1). IfKα≤1, thenc=α, theK
arcs are disjoint and their union has lengthKα. IfKα >1, thenc= 1/K < α, consecutive arcs
21

overlap and their union is the whole circle. The version that rejects when anyϕk does therefore
hase(v,θ) = min(1,Kα).
Choosing among valid analyses after seeing the data can multiply the Type I error rate by
the number of analyses, and nothing in the individual analyses reveals it. The bound in (i) is
Boole’s inequality, and the construction in (ii) ignores the data so that the arithmetic is exact.
Real analyses behave the same way whenever they reject on different studies. In bioequivalence,
falling back to a distribution-free interval whenever the two one-sided tests fail raises the Type I
error rate at the equivalence boundary to 0.0587 (section A10.2). The reference-scaled rule of the
US Food and Drug Administration (FDA) for highly variable drugs, which switches between two
valid analyses according to the observed variability, reaches about 2.4 times its nominal level when
each criterion is judged where the switch applies it (section A10.3).
A2.2 Selection through repeated updates
A proposer that maximizes power keeps every change that adds rejections. If a versionv′ rejects on
every run on whichvrejects, thene(v′,θ)≥e(v,θ)in every null scenario. In that casev′ also has at
least the power ofvin every scenario where the null hypothesis is false. Under such changes power
and the Type I error rate rise together. Without a check, a lineage ofKchanges that each add a
valid analysis is a version of the kind in Theorem A2 and can reachmin(1,Kα). The changes that
raise power fastest are often of exactly this kind. Optional stopping, which tests at every interim
look and stops at the first rejection, launching when any of several metrics improves, and widening
the equivalence limits when the observed variability is high all add rejections.
Checking each version is not enough, because the proposer selects among checked versions. If
the check reuses the same simulated studies, the proposer can tune versions to them. If the check
draws new studies but gives every version the same confidence level, the probability that some
version above the validation level passes grows with every update. The next two results make both
failures exact, the first for reused simulations and the second for a fixed confidence level per version.
A2.3 A reused set of simulations can be defeated
Proposition A3(A reused suite can be defeated).Let the reference analysisv0 decide by a fixed
function of the data. LetDbe a stored suite of simulated studies,mper scenario, that the proposer
can read. Then there is a version˜vthat makes the decision of the reference analysis on every study
inD. A validation computed fromDtherefore gives˜vexactly the bounds it gives the reference
analysis itself, and˜vpasses whenever the reference analysis would pass in its place. Its Type I error
rate satisfiese(˜v,θ)≥1−Pr θ{D∈D}in every scenario, ande(˜v,θ) = 1in every scenario whose
data have a distribution without atoms, such as any distribution with a density.
Proof.Let˜vreturn the decision of the reference analysis on any study inDand reject on any other
study. OnDthe two procedures agree study by study, so the rejection count of˜vequals that of
the reference analysis, and˜vadds and removes no rejections. These are exactly the counts that
the reference analysis produces against itself. In scenarioθthe version˜vrejects wheneverD /∈D,
which gives the bound one(˜v,θ), and a finite suite has probability zero under a distribution without
atoms.
A suite of simulations that the proposer can see is a benchmark that it can overfit. The
constructionisextreme, anditsmilderformisselectiononnoise. Aproposerthattunesacontinuous
threshold against stored studies keeps the most permissive version whose estimate on those studies
22

stays below the validation level. The kept version is selected for a low estimate, and its true Type
I error rate can exceed that level. Conditions (a) and (b) of Theorem A11 remove both effects for
the simulated studies, because the studies of every round are drawn after the version is fixed and
independently of everything the proposer has seen. The same two effects can act on a fixed set of
scenarios, and random scenarios drawn after each freeze confine them to a set of small probability
(section A4.6).
A2.4 A fixed confidence level per version fails over a lifetime
Call an update invalid if its Type I error rate exceeds the validation level in some of its validation
scenarios.
Lemma A4(A fixed confidence level per version).Suppose that every update is validated on newly
simulated studies at the same confidence level1−η. In particular, given everything that precedes
the draws of roundr, an invalid update passes with probability at mostη. Then for every proposer
the probability that some invalid version passes among the firstGupdates is at most1−(1−η)G.
If every update is invalid and passes with conditional probability exactlyη, the probability equals
1−(1−η) G, which tends to one asGgrows.
Proof.LetA r be the event that updateris invalid and passes, and letG r be the information
available before the draws of roundr. LetN r be the event that none ofA1,...,A r occurs. The
eventN r−1 is known before the draws of roundr, so
Pr(Nr) =E
[
1Nr−1 Pr(Ac r|G r) ] ≥(1−η) Pr(N r−1),
and induction givesPr(NG)≥(1−η) G. Under the second hypothesisPr(Ac r|G r) = 1−ηonN r−1,
and every inequality becomes an equality.
Aconfidencelevelperversionisaguaranteeperversion, andoverGupdatestheriskcompounds.
In the worst case of the lemma, the familywise error rate over the updates, the probability that some
invalid update passes, exceeds one half after 14 updates at the conventional 95 percent confidence,
and after 139 updates at 99.5 percent.
Continual validation divides the lifetime riskδamong all updates, and updaterreceives a share
δr with∑ rδr≤δ. By a union bound over the updates, the familywise error rate is then at mostδ
however many updates arrive (Theorem A11).
A3 Validating one version
This section shows how a single frozen version is validated. The versionvis fixed, and the validator
drawsmnew simulated studies in each scenario of a finite setS. The question is whethere(v,θ)is
at most a targetain every scenario ofS. In continual validation the target is the validation level
a=α ′, and Section A4 chains such validations over a lifetime.
A3.1 Exact bounds in one scenario
LetXbe binomial withmtrials and success probabilityp, and writePrp for probabilities under this
distribution. The exact one-sided upper bound of Clopper and Pearson [2] at levelηisU(x;m,η) =
1forx=m, and otherwise the(1−η)quantile of theBeta(x+ 1,m−x)distribution. The lower
bound isL(x;m,η) = 0forx= 0, and otherwise theηquantile of theBeta(x,m−x+1)distribution.
23

Lemma A5(Exact binomial bounds).For everym≥1, everyη∈(0,1)and everyp∈[0,1],
Prp{U(X;m,η)< p}≤ηandPr p{L(X;m,η)> p}≤η. MoreoverPr p{U(X;m,η)≤p}≤ηfor
everyp<1, andPr p{L(X;m,η)≥p}≤ηfor everyp>0.
Proof.Forx < mthe probabilityPr q{X≤x}is continuous and strictly decreasing inq, and it
equalsPr{Beta(x+ 1,m−x)>q}. HenceU(x;m,η)is the value ofqat whichPr q{X≤x}=η,
andUincreases inx. Fixp<1. If noxhasU(x;m,η)≤p, the event{U(X;m,η)≤p}is empty.
Otherwise letxp be the largest suchx. Thenxp<mbecauseU(m;m,η) = 1, and
Prp{U(X;m,η)≤p}= Pr p{X≤x p}≤Pr U(xp;m,η){X≤x p}=η,
becausep≥U(x p;m,η)andPr q{X≤x p}decreases inq. The strict statement follows forp <1,
and it holds forp= 1because thenX=mandU(m;m,η) = 1. The statements forLfollow
fromL(x;m,η) = 1−U(m−x;m,η)applied tom−X, which is binomial with success probability
1−p.
The bounds are exact for every number of simulated studies, with no asymptotic approximation.
The second statement adds that the upper bound falls at or below the true rate with probability
at mostη. This property implies that a version whose Type I error rate equals the target cannot
be validated (Proposition A7).
A3.2 Every scenario must pass
A validation ofvonScomputes one boundB θ per scenario from the simulated studies. The version
vpasses validation ifB θ≤afor every scenarioθ∈S. The boundB θ is valid at levelηforvif
Pr{e(v,θ)>B θ}≤η.
Theorem A6(Every scenario must pass).Letvbe a fixed version andSa finite set of scenarios.
For eachθ∈S, letB θ be a bound that is valid at levelηforv. Then
Pr
{
vpasses validation ande(v,S)>a
}
≤η,
andmax θ∈SBθ is an upper confidence bound fore(v,S)at levelη. The bounds may be computed
from shared or from separate simulated studies.
Proof.Fix an enumeration ofS, and letθ ∗ be the first scenario in it at whiche(v,·)is largest.
BecausevandSare fixed,θ ∗ is fixed as well. Ifvpasses validation ande(v,S)> a, then
Bθ∗≤a<e(v,θ ∗). Ife(v,S)>max θBθ, thene(v,θ ∗)>B θ∗. Both events lie in{e(v,θ∗)>B θ∗},
whose probability is at mostη.
A version above the target exceeds it in some particular scenario, and passing requires the
bound of that scenario to come out at or below the target. That one event has probability at
mostη, so the level does not have to be divided among the scenarios ofS. The rule that every
scenario must pass is an intersection-union test, which rejects a union of null hypotheses, here the
hypothesese(v,θ)> aforθ∈S, only when it rejects each of them. This is also why the two
one-sided tests procedure needs no correction for running two tests [3]. Bounds with simultaneous
coverage, holding in all scenarios at once, would require dividing the level among the scenarios.
Such a division replaceslog(1/η)by aboutlog(|S|/η)in the simulation effort, and valid versions
then fail more often with no gain in validity.
24

A3.3 A version at the target cannot be validated
Proposition A7(Validation fails at the target).Leta<1, and letBθ =U(X θ;m,η)be the direct
bound computed from the numberXθ of rejections ofvamongmsimulated studies of scenarioθ.
Ife(v,θ)≥a, thenvpasses scenarioθwith probability at mostη, for everym.
Proof.The countX θ is binomial with success probabilityp=e(v,θ). Ifp <1, passing requires
U(Xθ;m,η)≤a≤p, which has probability at mostηby Lemma A5. Ifp= 1, thenX θ =mand
U(Xθ;m,η) = 1>a, sovnever passes.
Simulation can confirm that a Type I error rate lies below the target by some margin, and never
that it equals the target. A version whose Type I error rate equals the target is valid, yet it fails
validation with probability at least1−ηhowever many studies are simulated. The same holds for
the paired and combined bounds of the next subsection (Theorem A8).
This limit also governs the choice of the reference levelα0. The two one-sided tests procedure
at levelahas a Type I error rate within a negligible distance ofaat the equivalence boundary
when a study is precise (Theorem A10). A reference analysis run at the validation level would thus
fail validation with probability close to1−ηin scenarios where its bound comes from simulation.
The paired bound also needs a margin below the target. SinceU(0;m,η)>0, even a version that
copies every decision of the reference analysis passes the paired bound only ifbθ <a. The reference
analysis therefore runs at a reference levelα0 below the validation levelα′ = 0.0452.
The marginγ=α ′−α 0 is available to every future version and does not shrink, because every
version is compared with the same reference analysis and not with its predecessor, so increments
do not accumulate across versions.
A3.4 Paired and direct bounds
The validator runs the versionvand the reference analysisv 0 on the samemsimulated studies
of scenarioθ, with independent internal randomness for every run. It counts the studies on which
onlyvrejects,N + θ , and those on which only the reference analysis rejects,N− θ , together with the
rejections ofv,X θ. Letq + θ andq − θ be the probabilities of an added and of a removed rejection in
scenarioθ. Then
e(v,θ) =e(v 0,θ) +q + θ −q− θ (A4)
exactly. Given a reference boundbθ≥e(v 0,θ)and levelsη 1,η 2,η 3, the paired, direct and combined
bounds are
Bpair θ =b θ +U(N + θ ;m,η 1)−L(N − θ ;m,η 2),
Bdir θ =U(X θ;m,η 3), B θ = min ( Bpair θ ,B dir θ ) . (A5)
Theorem A8(Paired and direct bounds).Fix the versionv, the scenarioθand a reference bound
bθ≥e(v 0,θ), and let the counts come frommindependent simulated studies ofθ.
(i)Pr{e(v,θ)>B pair θ }≤η 1 +η 2,Pr{e(v,θ)>B dir θ }≤η 3, andPr{e(v,θ)>B θ}≤η 1 +η 2 +η 3.
(ii) Ife(v,θ)<1, then alsoPr{B θ≤e(v,θ)}≤η 1 +η 2 +η 3.
Withη 1 =η 2 =η/4andη 3 =η/2the combined bound is valid at levelη. Suppose that every
bθ bounds the Type I error rate of the reference analysis. By the intersection-union argument of
Theorem A6, a version withe(v,S)>athen hasB θ≤ain every scenario, and so passes validation,
with probability at mostη.
25

Proof.Themsimulated studies and the runs on them are independent and identically distributed,
soN + θ ,N − θ andX θ are binomial with success probabilitiesq+ θ ,q− θ ande(v,θ). Their joint law plays
no role.
(i) By Lemma A5, the eventU(N + θ ;m,η 1)< q + θ has probability at mostη 1, and the event
L(N− θ ;m,η 2)> q− θ has probability at mostη2. Outside these two events, (A4) andbθ≥e(v 0,θ)
givee(v,θ)≤b θ +q + θ −q− θ ≤B pair θ . The statement for the direct bound is Lemma A5, and the
combined statement follows by the union bound.
(ii) IfBpair θ ≤e(v,θ), thenU(N + θ ;m,η 1)−L(N− θ ;m,η 2)≤q + θ−q− θ , so eitherU(N+ θ ;m,η 1)≤q + θ
orL(N − θ ;m,η 2)>q − θ . Sinceq + θ ≤e(v,θ)<1, Lemma A5 bounds the two probabilities byη 1 and
η2. The eventBdir θ ≤e(v,θ)has probability at mostη 3 by the same lemma. The eventBθ≤e(v,θ)
lies in the union of the events for the paired and direct bounds.
The paired bound compares the version with the reference analysis on the same simulated
studies. It therefore needs to resolve only how often the version adds a rejection that the reference
analysis would not make. That rate is zero for a version that never adds rejections and small for
a modest edit, whatever the Type I error rate of the reference analysis. The direct bound ignores
the reference analysis, and it is the better bound for a version that changes many of the decisions
of the reference analysis. Taking the smaller bound in each scenario costs a quarter of the level for
each count in the paired bound and half of it for the direct bound. The validator need not know
in advance which bound will be smaller.
With Theorem A6, part (i) bounds the probability of the joint event that a version passes and
lies above the target, so no conditioning on passing is involved.
A3.5 What validation costs
Writekl(x,y)for the relative entropy between Bernoulli distributions with success probabilitiesx
andy. Letζ∈(0,1)be an acceptable probability that a valid version fails validation.
Theorem A9(Cost of the two bounds).Fix a scenarioθ, a targeta∈(0,1), a marginγ∈(0,a)
and a levelη∈(0,1/4), and writeℓ= max{log(1/η),log(1/ζ)}.
(i) A version that never adds rejections. Ifq+ θ = 0andb θ≤a−γ, thenB pair θ ≤awith probability
one as soon asm≥log(1/η)/log{1/(1−γ)}, andm≥log(1/η)/γsuffices.
(ii) A version that adds few rejections. Ifq+ θ ≤cγwith0≤c<1andb θ≤a−γ, thenB pair θ ≤a
with probability at least1−ζwheneverm≥8ℓ/{(1−c) 2γ}.
(iii) Validation from scratch. Ife(v,θ) =a−γ, thenB dir θ ≤awith probability at least1−ζ
wheneverm≥8aℓ/γ 2. Conversely, consider a rule that decides from the rejections of a
version onmsimulated studies ofθ. Suppose that it passes every version withe(v,θ)> a
with probability at mostη. Then it passes a version withe(v,θ) =a−γwith probability
below one half unlessm≥a(1−a) log{1/(4η)}/(2γ 2).
Hereηis the level of the bound in question, that is,η1 in (i) and (ii), andη3 in (iii).
Proof.The proof uses three standard facts about binomial tails and relative entropy. First, for
Xbinomial withmtrials and success probabilityy, Chernoff’s bound givesPr{X≤mx} ≤
exp{−mkl(x,y)}forx≤yandPr{X≥mx}≤exp{−mkl(x,y)}forx≥y. Second,kl(x,y)≥
(x−y) 2/{2 max(x,y)}, because the second derivative ofkl(·,y)attis1/{t(1−t)}≥1/max(x,y)
fortbetweenxandy. Third,kl(x,y)≤(x−y) 2/{y(1−y)}, the chi-square bound. By the proof
26

of Lemma A5,U(x;m,η)≤gholds forx<mexactly whenPr g{X≤x}≤η, so the first two facts
give
U(x;m,η)≤gwheneverx/m≤gand(g−x/m) 2≥2glog(1/η)/m.(A6)
(i) HereN + θ = 0almost surely,U(0;m,η) = 1−η 1/m becausePr q{X= 0}= (1−q) m, and
L≥0. HenceB pair θ ≤a−γ+ 1−η 1/m, which is at mostawhenη 1/m≥1−γ, that is when
mlog{1/(1−γ)}≥log(1/η). Finally, the inequalitylog{1/(1−γ)}≥γgives the simpler sufficient
condition in (i).
(ii) Lety= (1 +c)γ/2. On the eventN + θ ≤mywe haveγ−N + θ /m≥(1−c)γ/2, and (A6)
withg=γgivesU(N + θ ;m,η)≤γoncem≥8 log(1/η)/{(1−c) 2γ}. ThenB pair θ ≤b θ +γ≤a. The
countN + θ is binomial with success probability at mostcγ < y. The first two facts therefore give
Pr{N + θ >my}≤exp{−m(y−cγ) 2/(2y)}= exp{−m(1−c) 2γ/(4(1 +c))}, which is at mostζonce
m≥8 log(1/ζ)/{(1−c) 2γ}.
(iii) On the eventXθ≤m(a−γ/2), (A6) withg=agivesB dir θ ≤aoncem≥8alog(1/η)/γ 2.
Moreover,Pr{Xθ >m(a−γ/2)}≤exp{−m(γ/2) 2/(2a)}, whichisatmostζoncem≥8alog(1/ζ)/γ 2.
For the converse, letAbe the event that the rule passes the version. WritePrp(A)for its probability
when the rejections are independent with probabilityp. The probabilityPrp(A)is a polynomial in
p, hence continuous, soPra(A)≤η. The data-processing inequality for relative entropy gives
mkl(a−γ,a)≥kl
(
Pra−γ(A),Pra(A)
)
.
Sincekl(x,y)increases inxforx≥yand decreases inyfory≤x, the right side is at least
kl(1/2,η) = 1 2 log[1/{4η(1−η)}]≥ 1 2 log{1/(4η)}wheneverPr a−γ(A)≥1/2. The chi-square bound
giveskl(a−γ,a)≤γ 2/{a(1−a)}, and the two inequalities together give the stated lower bound
onm.
Validation against the reference analysis needs a number of simulated studies of order1/γfor
a version that never adds rejections or adds them at a rate below the margin. Validation from
scratch needs ordera/γ2 for a version whose Type I error rate liesγbelow the target, and no rule
that uses only the decisions of the version can do better. The ratio is of ordera/γ, about 9 at
the marginγ=α ′−α 0 = 0.0052of Example 2, and the constants of the exact bounds widen it.
Table A2 gives the exact numbers of simulated studies at the first update. The two numbers differ
by a factor of 19.8 at the margin of Example 2 and of 108 at a margin of0.001. The combined
bound costs no more than the better bound in every scenario.
The saving shrinks as a version changes more decisions of the reference analysis, and Table A2
gives the profile. A version whose rejections contain those of the reference analysis and add re-
jections at half the margin needs 11,928 simulated studies against 114,862 from scratch, a factor
of 9.6. A version that keeps the Type I error rate of the reference analysis but adds and removes
rejections at equal rates gains less, because the paired bound carries the uncertainty of both counts.
Its factor, a Monte Carlo approximation accurate to about 2 percent, falls from 4.8 to 1.2 as the
rate of added and of removed rejections rises from0.002to0.012each, and the combined bound
then rests on the direct bound.
A3.6 A reference analysis validated by proof
In the two-period, two-sequence crossover, subjectkof sequencei∈{1,2}receives the test formu-
lation T and the reference R in different periods, with T first in sequence 1. On the log scale its
response in periodjis
yikj =µ 0 +βi +pj +τf(i,j) +uik +εikj,(A7)
27

Table A2:Simulated studies per scenario needed at the first update.
A. Versions that add no rejection, by marginγ
Marginγ0.0052 0.002 0.001
Against the reference analysis 1,414 3,700 7,402
From scratch 28,008 197,187 796,052
Factor 19.8 53 108
B. Versions that only add rejections, at ratecγ
Fractionc0.25 0.5 0.75
Against the reference analysis 4,479 11,928 55,248
From scratch 50,407 114,862 465,016
Factor 11.3 9.6 8.4
C. Versions that add and remove rejections, each at rateq
Rateq0.002 0.006 0.012
Combined bound 5,781 14,250 22,875
From scratch 28,008 28,008 28,008
Factor 4.8 2.0 1.2
All entries are computed atα= 0.05,δ= 0.005andδ 0 = 0.001, so thatα′ = 0.0452and the first share is
δ1 = 0.0024. Validation from scratch means the direct bound at the levelδ1/2it carries inside the combined bound,
and its row gives the smallestmat whichU(Xθ;m,δ 1/2)≤α ′ with probability 0.9. In A the reference analysis and
the version both have Type I error rateα′−γ, withb θ =α′−γ, and the first row gives the smallestmwith
U(0;m,δ 1/4)≤γ, at which the version passes with certainty. In B and C the reference analysis has Type I error
rateα 0, withbθ =α 0 and the marginγ=α ′−α 0 of Example 2. In B the version rejects whenever the reference
analysis does, so its Type I error rate isα0 +cγ, and the first row gives the smallestmat which the paired bound
passes with probability 0.9. In C the version keeps the Type I error rateα0, and the first row gives the smallestm
at which the combined bound passes with probability 0.9, estimated from 4,000 simulated rounds permon a grid of
one percent. The values of C are therefore Monte Carlo approximations, accurate to about 2 percent. All numbers
grow with the update index only throughlog(1/δr).
withf(1,1) =f(2,2) = Tandf(1,2) =f(2,1) = R. Here theβ i are sequence effects, theuik are
subject effects, and the errorsεikj are independent and Gaussian with mean zero and varianceσ2 W.
The log-ratio isµ=τ T−τ R, and the sequence effect isκ=β1−β 2.
The reference analysisv 0 is the two one-sided tests procedure at levelα0 on the completers,
the subjects who complete both periods. Letn1 andn 2 be the numbers of completers in the two
sequences. When dropout leaves a sequence without completers, or fewer than three completers in
all, the reference analysis retains the null hypothesis, so we may taken1,n 2≥1andn 1 +n 2≥3
below. The within-subject differencesdik =y ik1−yik2 removeµ 0,β i andu ik. The estimateˆµ=
( ¯d1− ¯d2)/2is Gaussian with meanµand varianceσ 2 W (n−1 1 +n−1 2 )/2. With the pooled variances2 d of
the differences onν=n 1+n2−2degrees of freedom, the standard error isse = (sd/2)(n−1 1 +n−1 2 )1/2.
The reference analysis rejects the null hypothesis of nonequivalence when the intervalˆµ±t1−α0,ν se
lies inside(−∆,∆), and retains it otherwise.
Theorem A10(A reference analysis validated by proof).Under model (A7), for everyµwith
|µ|≥∆, everyσ W >0, all subject, period and sequence effects, and every dropout mechanism that
does not depend on the responses,
e(v0,θ)≤α 0.
Atµ= ∆and without dropout, the Type I error rate tends toα0 asσ W→0with the design held
28

fixed, so the bound cannot be improved.
Proof.Condition on the sets of completers, which are independent of the responses. Given them,
Tµ = (ˆµ−µ)/sehas thetdistribution withνdegrees of freedom. Forµ≥∆the rejection event
lies in
{ˆµ+t1−α0,ν se<∆}={T µ<−t 1−α0,ν + (∆−µ)/se}⊆{T µ<−t 1−α0,ν},
because∆−µ≤0, and the last event has probabilityα 0. The caseµ≤ −∆is symmetric,
and averaging over the sets of completers gives the bound. Atµ= ∆the rejection event is
{t1−α0,ν−2∆/se< T µ <−t 1−α0,ν}. Asσ W→0with the design fixed and no dropout, the ratio
ofseto the standard deviation ofˆµkeeps its distribution and2∆/se→∞in probability, so the
Type I error rate tends toPr{Tµ <−t 1−α0,ν}=α 0. With dropout the same argument gives the
limitα 0 Pr{n1,n 2≥1, n 1 +n 2≥3}.
The two one-sided tests procedure holds its level exactly, a classical fact [4]. The theorem
records this fact for every design and dropout pattern that the scenarios use. The Gaussian null
scenarios are the null scenarios of model (A7) with dropout that does not depend on the responses.
On these scenarios the reference bound isbθ =α 0 with no simulation, and no part of the lifetime
risk is spent on the reference analysis. By contrast, on scenarios built from real studies, whose
errors are not Gaussian, the reference analysis receives a one-time validation (Corollary A16).
The reference level costs some power. At a true ratio of0.95, the two one-sided tests at a
reference level of 0.040 declare between 2.3 and 4.4 percentage points fewer equivalent products
bioequivalent than at0.05, in four crossovers of 24 to 48 subjects with 74 to 90 percent power at
0.05. Updated versions that pass validation can recover part of this power, for example by running
the two one-sided tests at a level just below the validation level.
The proved bound carries over to every version whose rejections are contained in those of
the reference analysis (Corollary A21). Examples include a version that defers studies with high
variability and a version that adds a check that can only veto a rejection. The bound does not
carry over to versions that use the data to change which observations enter the analysis. A version
that excludes outlying subjects, or recovers information from subjects observed in one period only,
changes the analysis set. The pivotTµ then loses itstdistribution, so such versions are validated
on scenarios.
A4 Lifetime validity
This section proves the guarantees of the main text in general form. Two devices chain the vali-
dations of single versions over the life of the analyst. Each round is judged by simulated studies
drawn after the version of that round is fixed, and each round spends its own share of the lifetime
riskδ. Theorem A11 bounds the lifetime risk, Corollary A12 gives every decision the levelα, and
Proposition A14 shows that valid updates pass. The last three subsections obtain the reference
bounds, extend the scenario set and add random scenarios.
A4.1 Lifetime risk control
At roundrthe validator receives updater. Before any simulated study of the round exists, the
validator fixes the updated versionvr and the scenario setSr⊇S 0, together with the reference
boundsb θ forθ∈S r. It also fixes the numbermr of simulated studies per scenario and the share
δr. We call this step the freeze of roundr, and we writeGr for the information available at the
freeze. It contains everything that has happened before, including all earlier updates, deployment
29

decisions, bounds and simulated studies, as well as the validation of the reference analysis. It also
contains the real studies decided so far and the randomness the proposer used to producevr.
The validator then draws the simulated studies of the round and computes the combined bounds
(A5) withη 1 =η 2 =δ r/4andη 3 =δ r/2. WriteBr,θ for the combined bound of scenarioθin round
r. The updated versionvr passes validation ifBr,θ≤α′ for everyθ∈S r, and only a version that
passes can be deployed. LetE0 be the event thatbθ≥e(v 0,θ)for every scenario the validator ever
uses.
Theorem A11(Lifetime risk control).Suppose that
(a) ineveryroundr, theupdatedversionv r, thescenariosetS r⊇S 0 withitsreferencebounds, the
numbermr and the shareδr are fixed at the freeze, while the proposer is otherwise unrestricted
and may be adaptive, randomized or adversarial,
(b) in every roundr, givenGr, the simulated studies are independent draws from the scenarios of
Sr, and the internal randomness of the runs on them is independent ofGr, and
(c)Pr(E c 0)≤δ 0, andδ 0 +∑ r≥1δr≤δholds with probability one.
Then
Pr
{
∃r≥1 :v r passes validation ande(vr,Sr)>α ′} ≤δ.(A8)
Moreover, the probability that some reference bound fails or somev r passes validation with
e(vr,Sr)>α ′ is at mostδ.
Proof.LetA r be the event thatvr passes validation ande(vr,Sr)>α ′. Letθ∗ r be the first scenario,
in a fixed enumeration ofSr, at whiche(vr,·)is largest. Versions are finite specifications and take
values in a countable set. Hence, by (a), the updated versionvr, its Type I error ratese(vr,θ), the
scenarioθ∗ r and the evente(vr,θ∗ r)>α ′ are determined at the freeze. OnAr∩E 0 the versionvr has
passed validation, so the bound of scenarioθ∗ r satisfiesB r,θ∗r≤α′<e(v r,θ∗ r), whilebθ∗r≥e(v 0,θ∗ r).
The proof of Theorem A8(i) shows that one of the three binomial bounds of scenarioθ∗ r must then
miss its parameter, and we call this eventMr. GivenGr, the updated version, the scenarioθ∗ r, the
numberm r and the shareδr are fixed. By (b), the studies of the round inθ∗ r arem r independent
draws from that scenario, run through both procedures with internal randomness independent of
Gr. The three counts are then binomial with the parameters of Theorem A8, and Lemma A5 gives
Pr(Mr|G r)≤δ r/4 +δr/4 +δr/2 =δ r. Hence
Pr
(
Ec 0∪ ⋃
r≥1
Ar
)
≤Pr(E c 0) + ∑
r≥1
E
[
Pr(Mr|G r)
]
≤δ 0 +E
[∑
r≥1
δr
]
≤δ,
which is the second statement and contains (A8). Rounds that never take place contribute nothing.
The theorem controls a familywise error rate over all updates, the probability that validation
ever passes an update above the validation level in a scenario of its round. It covers every deployed
update and also versions that pass without being deployed, such as the any-path rule of a set of
allowed paths, from which section A5 carries validity to deployed versions. It assumes nothing about
the proposer, which may be a language model that reads every deployment decision, an optimizer
that maximizes power, or an adversary. Within a round the argument is the intersection-union
argument of Theorem A6, and across rounds it is a union bound, as in alpha spending [5, 6].
Updates are counted by attempt, so updaterspends the shareδ r whether or not it passes.
If shares were indexed by deployed versions, a proposer could resubmit after each failure at an
30

unchanged share, and the familywise error rate would grow as in Lemma A4. The shares may be
chosen adaptively, as long as each is fixed at its freeze and their total never exceedsδ−δ0. The
protocol uses
δr = (δ−δ 0) 6 π2r2, ∑ r≥1 δr =δ−δ 0,(A9)
and any other summable schedule works as well. The shrinking share costs little, because the
number of simulated studies that an update needs grows only withlog(1/δr), which is2 logrplus
a constant. A version that never adds rejections thus needs 4,050 simulated studies per scenario at
the thousandth update, against 1,414 at the first (Theorem A9(i) and Fig. A1C). The scenario set
of a round may be any set fixed at its freeze that containsS0, so every version that passes is tested
on the initial scenario set, and the set grows with the analyst (section A4.5).
A4.2 Every decision the analyst makes
Studies are decided while the analyst evolves, and we writeHs for the information available when
the data of studysarrive. It includes every round completed by then with its simulated studies,
all earlier studies with their data and decisions, and the true scenarioθs. The version in force for
studys, writtenv (s), is determined byHs.
For a versionv,S(v)denotes the scenario set on which it passed validation or whose validity
it inherits. The reference analysis hasS(v0) =S 0, and so does the version that defers every study.
A version deployed without validation inherits the scenario set named in section A5.5.
Corollary A12(Type I error control for every decision).Let the validator run the protocol of
Theorem A11 with validation levelα′ = (α−δ)/(1−δ). Let the analyst start with the reference
analysis, or with a version that rejects only where the reference analysis rejects, ifmaxθ∈S0bθ≤α′,
and otherwise with the version that defers every study. Consider a studyssuch that
(i) whatever the history of updates, its true scenario is one on which the version in force was
validated or whose validity that version inherits, that is,θs∈S(v (s))almost surely, whereθ s
may depend on everything that happened before, and
(ii) givenH s, its data are a draw from scenarioθs, as Assumption A1 provides for a real study in
that state, and the internal randomness of the analyst on it is independent ofHs, so that the
version deciding the study was fixed before the data of the study were seen.
Then
Pr{Ys =reject}≤α ′ + (1−α ′)δ=α.(A10)
Under (ii) alone,Pr{Ys =reject, θs∈S(v (s))}≤α ′ Pr{θs∈S(v (s))}+ (1−α ′)δ.
Proof.LetEbe the event that every reference bound holds and nov r passes validation with
e(vr,Sr)>α ′, the complement of the eventEc 0∪⋃ rAr of the proof of Theorem A11. The second
statement of Theorem A11 givesPr(Ec)≤δ. OnEevery version that passes validation in a roundr
is valid at levelα′ onSr by the definition ofAr, whether or not it is deployed. These versions include
deployed updates, any-path rules of allowed paths, members of validated families and updates held
back by further conditions for deployment. OnEthe starting version is valid at levelα′ onS 0 as
well. The reference analysis hase(v0,θ)≤b θ≤α′ there, a version that rejects only where it rejects
has a Type I error rate at most that of the reference analysis (Corollary A21), and the version
that defers every study never rejects. Versions deployed without validation inherit this validity
on their scenario sets (section A5.5), so onEevery version that is ever in force is valid at level
31

α′ on its scenario set. WriteCs for the eventθs∈S(v (s)), which is determined byHs. By (ii),
Pr{Ys =reject|H s}=e(v (s),θs), which is at mostα′ onE∩C s and at most one elsewhere, so
Pr{Ys =reject, Cs}=E
[
e(v(s),θs) 1Cs
]
≤α′ Pr(Cs) + (1−α′) Pr(Cs∩E c)≤α ′ Pr(Cs) + (1−α′)δ.
Under (i),Pr(Cs) = 1and this is (A10), sinceα′(1−δ) +δ=αforα ′ = (α−δ)/(1−δ).
Suppose that condition (ii) holds for every study, that a version of row 4 of Table A3 is deployed
only while every reference bound onS0 is at mostα′, and that every routing family of row 5 is
validated onS 0. ThenS(v)⊇S 0 for every version in force, and the analyst is lifetime valid at
levelαonS 0 in the sense of Definition A1. Section A5 shows that versions deployed without new
simulation keep the corollary.
The bound of Corollary A12 is a probability over the whole history of the analyst. Given the
history up to its data, a decision on a study whose true scenario lies in the scenario set of the
deciding version is a Type I error with probability at mostα′, except on the eventE c, whose
probability is at mostδby Theorem A11.
By condition (ii), an update prompted by a study applies to later studies only, and this condition
cannot be dropped. Suppose that, after seeing the dataDs of studys, a proposer submits the
version˜vthat rejects onDs and otherwise copies the reference analysis. WhenPrθ has no atoms,
e(˜v,θ) =e(v0,θ), so˜vpasses validation. Yet if˜vdecided studys, it would reject with probability
one. The protocol therefore deploys a version that passes validation only for studies whose data
arrive later.
The guarantee is continuous in total variation in the law of the data. For every version and every
lawPof the data, the probability of a rejection underPdiffers frome(v,θ)by at most the total
variation distance betweenPandPr θ, because the rejection probability given the data lies in[0,1].
A scenario whose law is close to that of real studies in total variation therefore carries the guarantee
to them up to that distance. Whole studies are rarely that close, since a small change in a variance
or a different sample size already moves the law of a study far in total variation. Between and
beyond the fixed scenarios, the guarantee rests on random scenarios (Proposition A18). Without
them, a version can exceed the validation level off the fixed scenarios (Proposition A17 and the
example of section A4.6).
Corollary A13(Long-run frequency of false rejections).Suppose the protocol of Corollary A12
runs, that its condition (ii) holds for every study, and that each decision is made before the data of
the next study arrive. Lets1<s 2<···be the studies whose true scenario lies in the scenario set
of the version in force. Whether a study is of this kind is determined before its data arrive. LetFk
be the number of rejections among the firstkof these studies. Then, for everykand everyh>0,
(a)EF k≤kα,
(b)Pr{F k >k(α′ +h)}≤δ+ exp(−2kh 2), and
(c) with probability at least1−δ,lim sup k→∞Fk/k≤α ′ whenever infinitely many such studies
occur.
Proof.The event that studysis theith study of this kind is determined byH s, so the proof of
Corollary A12 applies to eachsi and gives (a). For (b) and (c), letZi indicate a rejection on study
si, and letpi = Pr(Zi = 1|H si) =e(v (si),θsi). The decisionZi is known when the data of study
si+1 arrive, so the sumsΨk = ∑ i≤k(Zi−p i)form a martingale with increments in intervals of
length one. The Azuma-Hoeffding inequality then givesPr{Ψk >kh}≤exp(−2kh 2). On the event
Eof the proof of Corollary A12, every version ever in force is valid at levelα′ on its scenario set, so
32

pi≤α′ for everyiandF k≤kα′ + Ψk, andPr(E c)≤δby the second statement of Theorem A11.
Together these give (b). The probabilitiesPr{|Ψk|> kh}≤2 exp(−2kh 2)are summable ink, so
Ψk/k→0almost surely by the Borel-Cantelli lemma, and onEthis gives (c).
A4.3 Valid updates pass
Type I error control alone is trivial, since a validator that never passes an update achieves it. The
next result shows that valid updates pass continual validation with high probability, at a number
of simulated studies that grows only with the logarithm of the update index.
Proposition A14(Valid updates pass).Fix an updater, a marginγ∈(0,α ′)andζ∈(0,1), and
let the scenario set of roundrcontainJr scenarios. Supposee(v r,θ)≤α ′−γfor every scenarioθ
of the round.
(i) Ifm r≥8α′ℓr/γ2 withℓ r = max{log(2/δr),log(Jr/ζ)}, thenv r passes validation with proba-
bility at least1−ζ.
(ii) Ifv r never rejects where the reference analysis does not, so thatq+ θ = 0, andb θ≤α′−γin
every scenario, thenvr passes validation with probability one as soon asmr≥log(4/δ r)/γ.
Proof.(i) Apply Theorem A9(iii) in each scenario with targeta=α′, levelη 3 =δ r/2and failure
probabilityζ/J r. The theorem is stated fore(vr,θ) =a−γ. The direct bound increases with the
count of rejections, and this count is stochastically increasing ine(vr,θ), so the probability that the
direct bound is at mostα′ can only grow whene(vr,θ)< a−γ. The combined bound is at most
the direct bound, and a union bound over theJr scenarios gives (i). (ii) Apply Theorem A9(i) with
levelη 1 =δ r/4in every scenario.
Remark A15(Further conditions for deployment).A deployment method may add conditions
to validation, for example that a lower confidence bound on the gain in power is positive. Such
a method deploys a subset of the versions that pass validation. The eventsAr in the proof of
Theorem A11 concern passing and not deployment, so they are unchanged, and Theorem A11 and
Corollary A12 continue to hold. An update held back by such a condition has still passed validation,
and a version deployed later without validation can inherit its validity (section A5.5).
A4.4 The reference analysis
CorollaryA16(Lifetimeriskcontrolwithavalidatedreferenceanalysis).Letthereferencebounds
of the initial scenario set be obtained in either of two ways, or by a mixture of them across scenarios.
(i) By proof. On Gaussian null scenariosbθ =α 0, by Theorem A10.
(ii) By one validation. Before the first update the validator simulatesm0 studies in each remaining
scenario ofS0, counts the rejectionsX0 θ of the reference analysis, and setsbθ =U(X 0 θ ;m 0,δ 0,θ),
with levelsδ 0,θ fixed before the first update whose sumδ′ 0 over these scenarios is at mostδ0.
Let every scenario added later receive a bound by proof, the trivial boundbθ = 1, or a validation of
the same kind. Thekth added scenario that receives such a validation has a levelδ0,k fixed before
the first update, withδ′ 0 +∑ kδ0,k≤δ 0. Itsm 0 simulated studies are drawn after the scenario
is fixed, independently of everything before. ThenPr(Ec 0)≤δ 0, and the protocol with the shares
(A9) satisfies (A8).
33

Proof.Analytic bounds and the trivial bound hold with certainty. The reference analysis is fixed
before its bounds are computed, so each countX0 θ forθ∈S 0 is binomial with success probability
e(v0,θ). By Lemma A5, the eventbθ < e(v0,θ)then has probability at mostδ 0,θ in each of these
scenarios. An added scenarioθk may be chosen from the history. Given the information available
whenθ k is fixed, its countX0 θk is binomial with success probabilitye(v0,θk). By Lemma A5, the
eventbθk <e(v 0,θk)then has conditional probability at mostδ0,k. Taking expectations and a union
bound overkand overS 0 givesPr(E c 0)≤δ ′ 0 +∑ kδ0,k≤δ 0, and Theorem A11 applies.
The reference bounds need simultaneous coverage, holding in all scenarios at once. They enter
every later validation, and a proposer that adapts to earlier deployment decisions can steer its
updated version toward a scenario whose reference bound happens to be too low. This requirement
divides the level of the bounds among theJscenarios. The division is made once, when the
reference analysis is validated, and the updates themselves need none (Theorem A6). On Gaussian
nullscenariosneitherdivisionnorsimulationisneeded. Inthebioequivalenceanalyst, thevalidation
of the reference analysis on scenarios built from real studies spendsδ0 = 0.001, and the updates
share the remaining0.004.
In a scenario with the trivial bound, the paired bound exceeds the validation level unless
the reference analysis rejects on almost every simulated study. The direct bound therefore decides
validation there, and the scenario set can grow at any time without a new validation of the reference
analysis.
A4.5 Scenarios grow with the information a version reads
A validation concerns only the scenarios that it uses. A version may read information that the
validation scenarios hold fixed, and its Type I error rate can then depend on a factor that no
scenario varies. The following existence statement makes this precise in the crossover model.
Proposition A17(New information needs new scenarios).In model (A7) with Gaussian subject
effects, letγ=α ′−α 0, and let the scenario set of roundrconsist ofJ r null scenarios without
sequence effect,κ= 0, with the analytic reference boundbθ =α 0. There is a versionv′ with the fol-
lowingthreeproperties. First,e(v ′,θ)≤α 0+γ/2ineverynullscenariowithκ= 0. Second, itpasses
validation in roundrwith probability at least1−ζoncem r≥32 max{log(4/δ r),log(Jr/ζ)}/γ.
Third,e(v ′,θ)→1asκ→∞with the other parameters fixed. The Type I error rate of the
reference analysis does not depend onκ.
Proof.Letw ik =y ik1 +y ik2 be the subject totals. Their means in the two sequences differ in
expectation by2κ, whateverµ. Lets w be the pooled standard deviation of the totals onνdegrees
of freedom. Whenκ= 0, the statisticT κ = ( ¯w1−¯w2)/{sw(n−1 1 +n−1 2 )1/2}has thetdistribution
withνdegrees of freedom, for everyµ,σ W and subject-effect variance. Letv ′ reject when the
reference analysis rejects or whenTκ>t 1−γ/2,ν. Whenκ= 0the second event has probabilityγ/2,
soe(v ′,θ)≤α 0 +γ/2by Theorem A10, andv ′ adds rejections at rateq+ θ ≤γ/2. Theorem A9(ii)
withc= 1/2,b θ =α ′−γand levelη 1 =δ r/4shows that each of theJ r scenarios passes with
probability at least1−ζ/J r under the statedmr. Hence all of them pass with probability at least
1−ζ. Asκ→∞,T κ→∞in probability, soe(v ′,θ)≥Pr{T κ >t 1−γ/2,ν}→1. The differencesd ik
do not involve the sequence effects, so the reference analysis does not depend onκ.
The versionv ′ is the simplest example, and a practical version behaves the same way. A
version that recovers information from subjects observed in only one period uses a between-subject
contrast whose mean isµplus the sequence effect. Its Type I error rate thus moves withκ, while
34

the reference analysis, which uses within-subject differences, is exactly invariant to it. A scenario
set that suffices for the reference analysis therefore does not suffice for such a version.
The validator extends the scenario set whenever an updated version reads a kind of information
that no current scenario varies, here by adding scenarios with a sequence effect. The validator
decides the extension and fixes it at the freeze, and the added scenarios stay in the set from then
on. The reference bound on them comes from proved invariance as here, from a validation at a level
set aside withinδ0, or from the trivial bound (Corollary A16). The guarantee for a decision covers
every scenario on which the version in force is validated whatever the history (Corollary A12), such
as every scenario of the initial set, and the scenario sets of later versions grow whenever the analyst
gains a new capability. The extension can be audited when every update declares the inputs its
decision reads and the software enforces the declaration, because the validator then sees which
factors need scenarios.
A4.6 Random scenarios extend the guarantee between fixed scenarios
A fixed scenario set is known to the proposer, who learns every deployment decision and the scenario
that decided it. A version can then copy the reference analysis on every validation scenario and
behave differently elsewhere. Consider a version that copies the reference analysis whenever the
planned sample size is one of those the scenarios use and rejects at every other sample size. It adds
no rejection in any validation scenario, so its paired bound passes whenever that of the reference
analysis would, yet its Type I error rate is one at every other sample size. This is the analogue of
Proposition A3 for scenarios. Newly simulated studies defeat versions that overfit a stored suite of
studies, and newly drawn scenarios do the same for versions that overfit a fixed set of scenarios, up
to a set of small probability.
Proposition A18(Random scenarios).LetΠbe a probability distribution onΘ 0, fixed before the
first update, under which every Type I error ratee(v,·)is measurable. In roundr, after the freeze,
let the validator draw a setQr ofK r scenarios independently fromΠand independently ofG r,
where the numbersKr are fixed before the first update. It adds them to the scenarios of the round
with the analytic reference bound where one exists and the trivial boundbθ = 1otherwise, and
only then draws the simulated studies of the round. LetVr ={θ∈Θ 0 :e(v r,θ)>α ′}be the set on
which the updated versionvr exceeds the validation level. Under the conditions of Theorem A11,
for everyε Π∈(0,1),
Pr
{
∃r≥1 :v r passes validation, ande(vr,Sr)>α ′ orΠ(V r)>ε Π } ≤δ+ ∑
r≥1
(1−ε Π)Kr.(A11)
Proof.LetG ′ r be the information at the freeze together with the drawn setQr. GivenG ′ r, the
updated version, the scenario setSr∪Qr with its reference bounds, the numbermr and the share
δr are fixed, and the simulated studies are drawn afterward. Conditions (a) and (b) of Theorem A11
therefore hold withG′ r in place ofGr. Analytic and trivial bounds hold with certainty, so the event
E0 is unchanged. The theorem givesPr{∃r:v r passes validation ande(vr,Sr∪Q r)> α′}≤δ.
LetΓ r be the event thatΠ(Vr)>ε Π and no scenario ofQr lies inVr. The setVr is determined byvr
and hence byGr, whileQr is drawn independently ofGr, soPr(Γr|G r) ={1−Π(V r)}Kr 1{Π(Vr)>
εΠ}≤(1−ε Π)Kr. Ifv r passes validation andΠ(Vr)> εΠ, then eitherΓr occurs or a scenario of
Qr lies inVr, and in the second casee(vr,Sr∪Qr)>α ′. A union bound over these events and over
rgives (A11).
The random scenarios cost no share of the lifetime risk, because within a round the intersection-
union argument needs no division across scenarios. They cost only the probability that no draw
35

falls in a set ofΠ-probability aboveε Π on which a version exceeds the validation level. Since
(1−ε Π)Kr≤exp(−ε ΠKr), the choiceKr =⌈ε−1 Π log{π2r2/(6ω)}⌉holds the added term atω. With
εΠ = 0.01andω= 0.005, the first update draws 580 scenarios and the thousandth draws 1,962.
With probability at least1−δ−ω, every update that passes validation, and so every deployed
update, is then within the validation level on every fixed scenario of its round and on all of the
null space except a set ofΠ-probability at mostεΠ. OnceΠgives sample sizes outside the fixed
scenarios a probability aboveε Π, the version of the example above fails validation except with
probability at most(1−ε Π)Kr +δr.
All random scenarios of a round must pass together. For the 580 scenarios of the first update to
pass jointly with probability 0.9 by the direct bound, a version at the reference level needs 64,845
simulated studies in each, against 28,008 for a single scenario (Table A2). On Gaussian scenarios the
analytic bound of the reference analysis holds everywhere (Theorem A10), and random scenarios
keep the paired bound and its lower cost. The draws also make the identity of a deciding scenario
uninformative for the proposer, since the next round draws new ones.
A5 Updates that need no new validation
Every update produces a new version, and Theorem A11 never asks what the update is or who
made it. Many updates need no new simulation, because an argument bounds their Type I error
rate by that of a version already known to be valid. The subsections below give these arguments,
and Table A3 collects them.
A5.1 Allowed paths
An AI analyst is usually a language model inside software that limits what the model can do. An
allowed path is one complete sequence of steps, from the start of a study to a decision, that the
software lets the model take. For example, one path might check the data against the protocol,
analyze the completers with the two one-sided tests procedure at levelα0, and decide. Another
path might defer the study to a human expert. LetRbe the set of allowed paths, where each
pathρ∈Rends in a decisiony ρ(D)that is a fixed function of the data. The language model
chooses which path to follow, and its choice may depend on the data, on its own randomness, on
its instructions and on the model itself.
Proposition A19(Allowed paths).Letvbe a version whose software mechanically confines every
run to a path inR. Each path ends in a decisionyρ(D)that is a fixed function of the data, so that
the model selects paths and computes nothing that enters a decision. Let the any-path rulevR be
the procedure that rejects whenever some allowed path rejects,
{YvR =reject}=
⋃
ρ∈R
{yρ(D) =reject}.
Thene(v,θ)≤e(v R,θ)in every scenario, whatever rule selects the path. In particular, suppose
every path that can reject applies one analysis to data prepared by one fixed rule. Then the Type
I error rate ofvis at most that of this analysis.
Proof.Whatever path is followed, the decision is a rejection only if that path rejects, so
{Yv =reject}⊆
⋃
ρ∈R
{ρis followed andy ρ(D) =reject}⊆{Y vR =reject}.
The last event depends neither on the rule that selects the path nor on the internal randomness of
the model.
36

A version is validated through its allowed paths when the any-path rulevR passes validation. A
later update that keeps the paths and their decision functions leaves this bound in force and needs
no new validation. A swapped model, an edited prompt, a changed sampling temperature and a
provider update are updates of this kind. The model may be stochastic, may drift, may become
more or less cautious, and may act adversarially within the allowed paths. None of this can enlarge
the rejection region beyond that ofvR.
The software must deliver both hypotheses, enforcing the set of allowed paths mechanically and
never letting the model compute a number that enters a decision. The model then chooses among
paths, and the paths compute. A validation of the version itself, by contrast, depends on how the
model chooses, and a model swap changes the object it validates. The bound is tightest when one
analysis carries every rejection, as in an analyst whose model can only choose between running the
sanctioned analysis and deferring.
A5.2 Deferral
Proposition A20(Deferral never raises the Type I error rate).Letv′ be a version, and letvrun
exactly asv′ except that it defers on an eventE. The eventEmay depend on anything, including
the data and the internal randomness of the analyst. Thene(v,θ)≤e(v′,θ)in every scenario.
Proof.On a common run,{Yv =reject}={Y v′ =reject}∩E c⊆{Y v′ =reject}.
Handing a study to a human never raises the Type I error rate of the decisions the analyst
makes on its own. A stricter deferral rule, a new reason to ask for review and a human who can
stop a rejection therefore need no validation. A human who can also turn a deferral into a rejection
forms a new decision procedure together with the analyst. That procedure can be validated as a
version in its own right.
A5.3 Containment in the rejection region of the reference analysis
Corollary A21(Containment).Supposevrejects only on runs on which the reference analysis
rejects, that is{Yv =reject}⊆{Y v0 =reject}for every data set and every value of the internal
randomness. Thene(v,θ)≤e(v 0,θ)in every scenario. For the reference analysis of Theorem A10,
e(v,θ)≤α 0 in every Gaussian null scenario, with no simulation and no share of the lifetime risk.
Proof.Probability is monotone under inclusion, and Theorem A10 gives the second statement.
Consider a version that keeps the reference analysis as the last step before every rejection and
adds only reasons to defer or to retain the null hypothesis. Such a version is valid on the whole
Gaussian null family by construction. Containment is proved from the definition of the version,
and it then holds exactly in every scenario, whether validation uses it or not. When containment
holds but has not been proved, such a version passes the paired bound with few simulated studies
on the validation scenarios, because it adds no rejections (Theorem A9(i)).
A5.4 Choosing among validated analyses
Proposition A22(Routing among validated analyses).Let{ϕ λ :λ∈Λ}be a countable family
of analyses withe(ϕλ,θ)≤afor everyλand everyθin a setS⊆Θ 0. Letvcompute an index
ˆλ=λ(I)from routing informationIand reject whenϕ ˆλ rejects. Suppose that in every scenario
θ∈Sthe routing informationIis independent of the statistics from which the analyses decide,
together with all internal randomness that they use. Thene(v,θ)≤afor everyθ∈S.
37

Proof.Eachϕ λ is a function of these statistics and of the internal randomness of the analyses,
which are independent ofIand hence of ˆλ, so
e(v,θ) =
∑
λ∈Λ
Prθ{ˆλ=λ}Pr θ{ϕλ =reject}≤a.
Independence of the routing information from the data alone is not enough. LetW1,...,W K
be independent uniform variables, independent of the data, and letϕk reject whenWk < α. The
informationI= (W 1,...,W K)is independent of the data, yet the rule that picks the firstkwith
Wk <αrejects with probability1−(1−α) K.
Routing on information fixed before the data, such as the design declared in the protocol,
satisfies the condition. So does routing on an ancillary statistic, one whose distribution is free of
the unknown parameters, provided the analyses are functions of a complete sufficient statistic. By
Basu’s theorem, the routing statistic and the complete sufficient statistic are then independent.
In the Gaussian crossover model, for example, consider level-α0 analyses that use the data only
through( ¯d1, ¯d2,sd). A diagnostic computed from the standardized residuals of the within-subject
differences may choose among them, and the Type I error rate stays at mostα0.
A routing family, the family of analyses of Proposition A22, is validated onSwhen each member
is valid at levelα′ onS, by proof or by passing validation on the eventEof Corollary A12.
A5.5 What each kind of change owes
Table A3 sorts changes into six kinds by the evidence they owe. Versions deployed through rows 1
to 5 inherit validity on the eventEof Corollary A12. This holds because each row bounds the Type
I error rate of the new version by that of a version already known to be valid on the same scenarios.
That version is the one being changed, the any-path rule of the allowed paths, the reference analysis
when its bounds are at mostα′, or a validated family of analyses. The new versionvinherits a
scenario setS(v), which enters condition (i) of Corollary A12. This set isS(v′)for a change ofv′ in
row 1 or row 3, andS(vR)for a change in row 2. For a version in row 4 it consists of the scenarios
in force at its deployment withbθ≤α′. For a version in row 5 it is the set on which every member
of the family is validated. Corollaries A12 and A13 therefore cover every version the analyst ever
runs. A change in row 6 is validated as an update in the sense of section A4.
38

Table A3:Kinds of change and the evidence each owes before deployment. Changes in rows 1 to 5 need
no new simulation and spend no share of the lifetime risk.
kind of change examples evidence owed result
1 cannot change any decision report formatting, logging,
an equivalent implementa-
tion
a proof that every
path to a decision
runs identical code on
identical inputs. An
identity that is only
tested goes through
row 6, where its vali-
dation needs few sim-
ulated studies
same Type I er-
ror rate
2 keeps the allowed paths
and their decision func-
tions
model swap, prompt edit,
sampling temperature,
provider update
none beyond the val-
idation of the any-
path rule
Prop. A19
3 can only replace a rejection
by a deferral
stricter deferral rule, a new
reason for review, a human
veto
none Prop. A20
4 rejects only where the
reference analysis rejects,
proved from its definition
a deferral path placed be-
fore the reference analysis,
a check that can only veto
none, valid on the
whole Gaussian null
family atα 0
Cor. A21,
Thm. A10
5 chooses among validated
analyses by information in-
dependent of the statistics
they use and of their ran-
domness
the analysis chosen by the
design declared in the pro-
tocol
validation of the fam-
ily
Prop. A22
6 anything else a new exclusion rule, a
switch between analyses af-
ter seeing data, a second
stageofsampling, anewin-
put
validation with the
combined bounds
on newly simulated
studies at the share
of the update, with
scenarios added for
new inputs
Thm. A11
A6 The procedure
Algorithm A1 collects the pieces of the preceding sections in one procedure. It repeats Algorithm 1
of the main text line by line and adds two details, the random scenarios of section A4.6 in line
8 and the report of the deciding scenario in line 16. Each of its lines delivers a condition of the
results above.
All inputs, including the levels of the reference bounds (Corollary A16) and the law and numbers
of the random scenarios (Proposition A18), are fixed before the working life of the analyst begins.
Line 2 puts the reference analysis, or a version that rejects only where it rejects (Corollary A21),
into service only if the reference bounds are at mostα′ on the initial scenario set, as Corollary A12
requires. Otherwise the analyst defers every study until its first update passes validation. Any other
first version is proposed as update 1 and validated like every later update, so it needs no share
outsideδ 0 +∑ rδr. The reference bounds come from Theorem A10 on Gaussian null scenarios
and from the one-time validation of the reference analysis on scenarios built from real studies
(Corollary A16).
39

Algorithm A1Continual validation
GivenType I error levelα, lifetime riskδ, reference riskδ 0 with the levelsδ′ 0 andδ 0,k of the
reference bounds, initial null scenariosS0, reference analysisv0 with boundsbθ, the lawΠand
the numbersKr≥0of random scenarios
1:Setα ′←(α−δ)/(1−δ)andS←S 0
2:Deployv 0, or a version that rejects only wherev0 does, ifbθ≤α′ for everyθ∈S 0. Otherwise,
start with a version that defers every study.
3:foreach proposed updater= 1,2,...do
4:Freeze the updated versionv r
5:Add scenarios toSfor any new inputs used byv r, each with a reference boundbθ that is
analytic, validated at its levelδ0,k, or1
6:SetS r←S
7:Setδ r←6(δ−δ 0)/(π2r2)and fix the numbermr of datasets per scenario
8:DrawK r scenarios fromΠwith analytic or trivial bounds and add them toSr for this round
only
9:Simulatem r new datasets from eachθ∈S r
10:Runv r andv 0 on the same datasets
11:For eachθ∈S r, count rejectionsXθ ofv r, added rejectionsN + θ , and removed rejections
N− θ
12:B pair θ ←b θ +U(N + θ ;mr,δr/4)−L(N − θ ;mr,δr/4)
13:B dir θ ←U(X θ;mr,δr/2)
14:B θ←min(B pair θ ,B dir θ )
15:IfB θ ≤α ′ for everyθ∈S r, deployv r for every study whose data arrive from now on.
Otherwise, retain the current version.
16:Report the deployment decision and the scenario with the largestB θ to the proposer
17:end for
Lines 4 to 7 are the freeze of section A4. Line 4 fixes the updated version as a complete
specification, including model, instructions, tools, code and thresholds. Line 5 is the extension
of section A4.5, which the validator decides, and line 6 fixes the scenarios of the round. Line 7
fixes the share and the number of simulated datasets. Line 8 draws the random scenarios after
the freeze, independently of everything before, and they serve this round only (Proposition A18).
Only then does line 9 draw the simulated datasets, with randomness that is new and independent
of everything the proposer has seen. These lines deliver conditions (a) and (b) of Theorem A11.
The share is indexed by the attemptr, so an update that fails validation spends its share as well,
and the shares sum toδ−δ 0, which is condition (c).
Lines 12 to 15 compute the bounds of Theorem A8 and decide by the intersection-union rule
of Theorem A6, with no correction across scenarios. The numbermr may grow withrto keep
the probability that a valid update passes high (Proposition A14). A round never stops early,
because the exact binomial bounds assume a fixed number of datasets, and optional stopping
would invalidate them.
Line 15 deploys a version that passes validation for the studies whose data arrive after the
deployment decision, which is condition (ii) of Corollary A12. Line 16 returns the deployment
decision and the scenario with the largest bound. Because the next round draws new datasets, the
proposer may learn from the deployment decision, from the bounds and even from the simulated
datasets of the round.
Changes in rows 1 to 5 of Table A3 may be deployed without lines 7 to 15 and spend no share,
40

whereas every other change goes through validation.
A7 Example 1, a bioequivalence analysis agent
Both examples ask one question. While a language model keeps updating an AI analyst to make
it more useful, which deployment methods keep the Type I error rate of the analyst at the chosen
level, and which of them still deploy useful updates? This section presents the first example, an
agent that analyzes bioequivalence studies. It states the hypothesis test that the agent decides,
how the agent reaches its decision, what an update can change and how studies are simulated. It
then gives the design that both examples share, the metrics and the results. The second example,
an analyst of product experiments, follows in section A8.
A7.1 The hypothesis test
A bioequivalence study is one part of the evidence on which a generic drug is approved. It tests
whether the generic, the test product, delivers the same exposure as the reference product. Healthy
volunteers receive both formulations in a crossover study, in which each subject receives both in
different periods. In a replicate study the reference, or both formulations, are given twice. Exposure
is summarized by the area under the concentration curve (AUC) and by the peak concentration
(Cmax). Withµthe log-ratio of the geometric mean exposures of test and reference, as in sec-
tion A1, the null hypothesisH0 is that|µ|≥∆with∆ = log 1.25, so that the true ratio lies at
or beyond 80.00 or 125.00 percent and the products are not equivalent. The alternativeH1 is that
|µ|<∆. The products are declared equivalent, andH0 is rejected, when the 90 percent confidence
interval of the ratio lies within 80.00 to 125.00 percent [1, 7]. This is the two one-sided tests at
level 0.05. A Type I error is a false conclusion of equivalence, and its probability is known in
bioequivalence as the consumer risk.
A drug is highly variable when the within-subject coefficient of variation of its reference formula-
tion exceeds 30 percent. For such a drug the EMA widens the limits for Cmax toexp(±0.760swR),
wheres wR is the observed within-reference standard deviation on the log scale. The widening stops
at 69.84 and 143.19 percent, which are reached at a coefficient of variation of 50 percent, and the
point estimate of the ratio must still lie within 80.00 to 125.00 percent [1]. For a highly variable
drug the null hypothesis uses the limits that the true within-reference standard deviation implies,
as section A7.4 states. The EMA’s average bioequivalence with expanding limits (ABEL) and the
FDA’s reference-scaled average bioequivalence (RSABE) switch to scaled limits when the observed
coefficient of variation exceeds 30 percent. This switch is known to inflate the Type I error rate
when the true variability lies near 30 percent [8, 9, 10].
A7.2 How the agent decides
We built the agent as a statistical-agent harness for planning and analyzing bioequivalence studies.
Claude Code skills read written playbooks, whose decision tables name the next command, and
deterministic Python and R tools compute and record every number. The software that computes
the results calls no language model. Its standard analysis is unscaled average bioequivalence for
a2×2crossover. A set of extended methods, still under development, also covers parallel and
replicate designs, with the FDA’s RSABE and its switch to unscaled average bioequivalence, the
EMA’s ABEL by Method A, the FDA’s criteria for narrow-therapeutic-index drugs and the EMA’s
narrowed limits. These methods are checked against the EMA’s two published replicate datasets
and against independent results computed in base R. The bioequivalence agent is available at
41

https://be.statrust.ai/. The simplified version used in our experiments will be released with
the study code athttps://github.com/xiaojing777/lifetime-valid-ai-analysts.
For each study the agent takes the same steps. It prepares the data with a prespecified analysis-
set rule, complete case or available case, and records every omitted record with its reason. It flags
outlying subjects with a prespecified rule, by default the rule of replicateBE [11], which flags a
subject when one of its externally studentized residuals in the outlier model of the method lies
beyond Tukey’s hinges by more than twice the distance between the hinges. A flagged subject is
never removed, and the result without the flagged subjects is reported beside the primary result.
The agent then applies the method of its configuration. It decides on the bounds of the confidence
interval in percent, rounded half up to two decimals, and reports the unrounded result of every
criterion beside the rounded one. In this experiment every version decides on the unrounded results,
so that the reference analysis is exactly the two one-sided tests.
The analyst of this example is the analysis part of the agent, run with a configuration that
the experiment adds. The configuration fixes every setting that can change a decision, and the
deterministictoolsapplyittothedataofeachstudy. ArejectionofH 0 isaconclusionofequivalence.
The language model that drives the analysis chooses the next command from the decision tables,
and every path that the playbooks allow ends either in the decision that the tools compute under the
configuration or in a deferral to a human. The only allowed path that can reject is therefore the one
that applies the configured decision rule, and the any-path rule of the version is this decision rule
(Proposition A19). The validator runs it directly, so validation needs no calls to a language model.
The analyst defers to a human any study for which the agent does not compute the configured
combination of settings. Section A7.10 checks on simulated studies that the agent reaches these
decisions.
A7.3 Reference analysis, settings and new decision rules
The reference analysisv0 is the agent’s standard unscaled average bioequivalence, the two one-sided
tests atα 0 = 0.030on the complete-case set, with outliers flagged but not removed and no deferral
rule. On the full replicate it uses the intra-subject contrast of each subject, the mean test minus
the mean reference log response, fitted on sequence. Equivalently, it checks there whether the 94
percent confidence interval lies within 80.00 to 125.00 percent. The agent refuses it on the partial
replicate, wherev 0 therefore defers and never rejects. The reference level is lower than in Example
2 because the subject contrasts of real studies can be skewed. At 0.040 the two one-sided tests
reach a Type I error rate of about 0.052 on resampled studies of dataset 5 with 24 subjects, above
α′, while at 0.030 they stay at or below 0.042 in every scenario of the base set.
On the Gaussian scenarios of section A7.4, the reference bound isbθ =α 0 in the full replicate
andb θ = 0in the partial replicate. These scenarios have equal within-subject variances for test
and reference, a subject effect common to both formulations and dropout that does not depend
on the responses. In the full replicate the contrast analysis is then an exactttest, and the proof
of Theorem A10 carries over. In the partial replicate every rejection of an update is an added
rejection, so the combined bound of Algorithm A1 equals the direct bound.
On scenarios built from real studies,bθ = 0in the partial replicate for the same reason. In the
full replicate their reference bounds come from a one-time validation atδ0 = 0.001(Corollary A16).
Before the first update of each run, the validator simulates106 datasets in every such scenario of
the base set, 252 in all, and dividesδ0 equally among them. The extension adds only Gaussian
scenarios, whose bounds are known. The experiment then confirms that every reference bound of
that run on the base set is at mostα′, so that the starting version is valid there (Corollary A12). A
run whose check fails starts from the version that defers every study (Algorithm A1, line 2). Once,
42

on the evaluation stream, the experiment also confirms that the reference analysis counts as within
α′ on the full validation set, by the rule of section A7.6.
An update may change one of six settings.
•Method. Unscaled average bioequivalence, or the EMA’s ABEL by Method A, which widens
the limits when the observed within-reference coefficient of variation exceeds 30 percent.
•Analysis set. Complete case or available case.
•Role of the outlier analysis. Reported beside the primary result, as in the agent, or reported
instead of the primary result when it concludes equivalence and the primary result does not.
•Level of the two one-sided tests. 0.030, 0.035, 0.040, 0.045 or 0.050, applied to every interval
that the method uses.
•Deferral by variability. None, or deferral when the observed within-reference coefficient of
variation exceeds 0.30, 0.40 or 0.50.
•Deferral of flagged files. On or off.
The menu of settings holds 320 configurations, and the reference analysis and the starting version
are two of them. The starting version is the reference analysis with two deferral rules. It sends
to a human every study whose observed within-reference coefficient of variation exceeds 0.30 and
every file with a data-quality flag. Every study is treated as a Cmax study, so the widening applies
whenever the method calls for it.
An update may instead add a new decision rule, which the developer writes as a Python function
against a fixed interface (section A7.5). A new decision rule acts on top of the settings, for example
as a new outlier criterion or as a choice of model that depends on the data. It receives a batch
of simulated studies as arrays of subjects, sequences, periods, formulations, log responses and
data-quality flags, together with the flags of the agent’s prespecified outlier rule. It may call
the estimators of the agent, through the reimplementation described below, on any subset of the
subjects of each study, with any method, analysis set and level of the menu, and it may compute
its own intervals from quantiles of thetdistribution. It returns one of three decisions for every
study, equivalence shown, equivalence not shown, or deferral to a human.
A7.4 Scenarios, workload and simulation sizes
Validation scenarios are built from ten reference datasets of the R package replicateBE [11, 12].
These are its reference datasets 1, 2, 4, 5, 10, 11, 16, 23, 24 and 26, the ten that come from real
studies. They come in several replicate designs. Every scenario is simulated in one of two replicate
designs that the agent analyzes, the four-period full replicate TRTR/RTRT and the three-period
partial replicate TRR/RTR/RRT. The agent refuses some configurations in these designs, standard
average bioequivalence on the partial replicate and the available-case set for standard average
bioequivalence on the full replicate, and the analyst then defers the study to a human. A simulated
subject is a real subject drawn with replacement, whose centered responses are placed in the periods
of its simulated sequence. Each published dataset is simulated in one design, the full replicate when
its subjects have two test and two reference responses and the partial replicate otherwise. Thekth
test andkth reference response of a resampled subject fill itskth test andkth reference period, and
the partial replicate uses the first test response. A subject is eligible for resampling when it has
the observations that the design of its dataset needs, two test and two reference responses for the
full replicate, and one test and two reference responses for the partial replicate. The design of each
43

dataset and its number of eligible subjects were fixed before the experiment. Before resampling,
the log responses are centered within each sequence and period. This removes the period, sequence
and formulation effects and keeps the spread between and within subjects.
The resampling is a smoothed bootstrap. It adds independent Gaussian noise to every log
response, withstandarddeviationonetenthoftheresidualstandarddeviationoftheEMA’sMethod
A model fitted to the original dataset. The noise removes exact ties between resampled subjects.
The test responses are then shifted by the true log-ratio of the scenario.
A scenario hasn∈{24,36,48}subjects, split evenly over the sequences, and dropout of 0, 10
or 20 percent. A subject drops out with this probability, independently of its responses, after a
period drawn uniformly from all periods but the last, and its later periods are missing. In every
simulated study, null or not, the file carries a data-quality flag with probability 0.15, independently
of the responses.
The true within-reference varianceσ2 wR of a scenario is that of its resampling distribution. It
equals half the mean squared difference between the two centered reference responses of a subject,
averaged over the subjects who receive the reference twice, plus the variance of the added noise.
The true coefficient of variation is{exp(σ2 wR)−1} 1/2. The true geometric mean ratio lies at the
regulatory limit for this variability, on either side, or 0.05 beyond it on the log scale. The limit is
80.00 or 125.00 percent when the true coefficient of variation is at most 30 percent. Otherwise it is
the EMA’s widened limitexp(±0.760σwR), which stays at 69.84 or 143.19 percent from a coefficient
of variation of 50 percent upward. Every scenario therefore belongs to the null hypothesis that the
true ratio lies at or beyond the regulatory limit for the true variability. Validation holds every
version to this null hypothesis. The base set, which is the initial scenario setS0 of Algorithm A1,
crosses every dataset, in its design, with three sample sizes, three dropout rates and these four
ratios. It holds 36 scenarios per dataset, 360 in all.
Validation adds scenarios when an update reads information that the base set does not vary
finely enough (section A4.5). An update reads the observed variability when it uses reference-scaled
limits or deferral by the coefficient of variation. Validation then adds Gaussian scenarios with true
within-reference coefficients of variation of 0.25, 0.28, 0.30, 0.32, 0.35, 0.40 and 0.50. They use the
four-period full replicate TRTR/RTRT and the three-period partial replicate TRR/RTR/RRT,
with the sample sizes, dropout rates and four placements of the true ratio of the base set. Their
errors have equal variances for test and reference. Their subject effects are common to both
formulations, with standard deviation 0.5 on the log scale, and they have no period or sequence
effects. These are 504 scenarios. Because the starting version defers by the observed coefficient of
variation, every update that keeps this deferral is validated on these scenarios.
The available-case set reads incomplete records, whose dropout the base set already varies, so
it adds no scenarios. A new decision rule reads the data and can compute the observed variability,
so every new decision rule is validated on the Gaussian scenarios above. Such a rule also sees the
allocation of subjects to sequences and the periods, which the scenarios above keep balanced and
free of period effects. Every new decision rule is therefore also validated on 72 Gaussian scenarios
that cross the two designs, the three sample sizes with two thirds of the subjects in the first sequence
and the rest split evenly over the others, the three dropout rates and the four placements of the
true ratio, at a true within-reference coefficient of variation of 0.30, with log responses that rise by
0.05 from each period to the next. Once added, a scenario stays in the set. The full validation set,
the base set together with both kinds of added scenarios, holds 936 scenarios.
Off-grid scenarios, which no deployment method ever simulates, are built in the same way and
form five families. The first uses five further reference datasets of replicateBE, numbers 7, 8, 22,
25 and 28, which validation never uses. It keeps the sample sizes and dropout rates of the base set
and places the true ratio at either limit. The authors of the package simulated these five, since its
44

ten datasets from real studies all serve validation. The second uses the ten datasets with 30, 42 or
60 subjects, split as evenly as the sequences allow. The third uses them with dropout of 5, 15 or 25
percent. The fourth places the true ratio 0.025 beyond either limit on the log scale, between the
two placements of the base set. The fifth applies to these five datasets dropout that depends on the
first-period response. Only subjects whose first-period log response lies below the 20th or above the
80th percentile of their sequence drop out, each with probability equal to the dropout rate divided
by the share of its sequence in these tails, so that the overall rates are 10 and 20 percent. Factors
that a family does not change keep the values of the base set, and the true ratio lies at either limit
unless the family sets it. These families hold 690 scenarios, and each of them differs from every
validation scenario in at least one factor.
Power is measured on a workload of truly equivalent studies. It crosses the ten datasets, the
three sample sizes and the three dropout rates of the base set with true ratios of 0.95 and 1.00,
which gives 180 cells of equal weight. Power is the probability that the deployed version concludes
equivalence without deferral, averaged over the cells. The usefulness metric of the performance
report is the share of workload studies that the agent decides without a human, together with its
power. It is estimated each round from 10,000 new workload studies, and the experiment reports it
alongside the five metrics. The performance report and the improvement test draw each workload
study from a cell chosen uniformly at random.
Continual validation draws 500,000 datasets per scenario per update. The static benchmark
stores 500,000 datasets per scenario of the base set, and the improvement test draws 500,000 new
workload studies per round. Learn then Test tests the 320 configurations once on 500,000 datasets
per scenario, after a pilot of one tenth that size.
A7.5 Design shared by both examples
A language model acts as the developer of the analyst. It is Claude Sonnet 5.5 (claude-sonnet-5-
5), with its default sampling and the medium setting of its reasoning effort. Before every round
the developer receives four inputs. These are the description of the analyst’s settings, the current
configuration, a performance report and feedback on its earlier updates. The performance report
gives the usefulness metric of the example and the power of the deployed version on simulated
alternatives. The feedback states for every earlier update whether it was deployed, together with
the bound or estimate on which the deployment method decided.
The developer proposes one update per round. An update either changes one setting or adds
a new decision rule, a Python function written against a fixed, typed interface. Such a rule is
deterministic, makes no network calls and runs in a sandbox. The instructions to the developer are
identical under every deployment method and never name the method. They describe the analyst,
its settings and the interface, give the usefulness metric of the example as the goal, and ask for
exactly one update in a fixed machine-readable format. Each round is one call to the model with the
full history of the run. For every deployment method and in each example, the experiment performs
twenty independent runs of ten rounds. Every run starts from a version that needs no validation
of its own. In Example 2 it is the reference analysis. In Example 1 it is the reference analysis with
two deferral rules (section A7.3). This version rejects only where the reference analysis rejects, so
its Type I error rate is at most that of the reference analysis in every scenario (Corollary A21).
A version consists of a configuration of the settings and at most one new decision rule. Without
such a rule the configured analysis decides, and with one the rule decides. A rule may call the
configured analysis and any other analysis of the menu. A new rule replaces the earlier one, and an
update may also remove the rule. The interface is vectorized, so a rule receives a batch of simulated
datasets and returns one decision for each. A rule must decide a batch of 10,000 datasets within ten
45

seconds on one processor core, including the analyses it requests. An update is malformed when
it cannot be parsed, misses this time limit, or returns different decisions when it is run twice on
the same batch. A malformed update is not deployed under any method, the feedback names the
reason, and its round still counts.
The same five deployment methods run in both examples, and all of them receive the same
developer.
•No validation. Every well-formed update is deployed without a check.
•Static benchmark. Before the first update, the experiment simulates one set of null datasets,
of the size that validation uses, and reuses it for every update. An update is deployed when
the one-sided 95 percent Clopper and Pearson upper bound on its Type I error rate is at
mostα′ in every scenario of this set. This is today’s practice of re-checking each version on
a stored benchmark at a fixed confidence level.
•Improvement test. An update is deployed when a one-sided lower confidence bound on its
gain in power over the current version is positive. The error budget is spread over updates,
as in recent checks for self-improving agents [13, 14]. Power is estimated on new simulated
alternatives, and the Type I error rate is not checked.
•Learn then Test [15]. Before the first update, every configuration in the menu of settings
is tested once, on null datasets simulated once, with familywise error control atδby fixed-
sequence testing. A proposed update is deployed only if its configuration lies in the validated
set. Updates outside the menu, such as new decision rules, are never deployed.
•Continual validation. Algorithm A1 runs with the lifetime riskδ= 0.005, the validation level
α′ = 0.0452, the reference levelα0 of the example (0.030 in Example 1 and 0.040 in Example
2) and the sharesδr = 6(δ−δ 0)/(π2r2). In both examples the reference analysis receives
δ0 = 0.001.
The static benchmark covers the base set, which holds the validation scenarios in force before
the first update. It does not grow with later updates, because a stored benchmark is fixed before
the updates it will judge are known.
In roundrthe improvement test runs the update and the current version on the samemnew
alternatives. It counts the alternatives on which only the update rejects the null hypothesis without
deferral,G +, and those on which only the current version does,G−. The update is deployed when
L(G+;m,ϵ r/2)−U(G −;m,ϵ r/2)>0. HereUandLare the exact one-sided Clopper and Pearson
bounds, andϵr = 6δ/(π2r2). The probability that a run ever deploys an update that does not raise
power is then at mostδ.
Learn then Test tests every configuration on the base set and on the added scenarios that its own
settings call for, with as many null datasets per scenario as validation draws. The null hypothesis of
a configuration is that its Type I error rate exceedsα′ in some of these scenarios. In each scenario,
the exactpvalue is the probability that a binomial count with rateα ′ is at most the observed
number of rejections, and thepvalue of the configuration is the largest of these over its scenarios.
The tests run in the order of the largest Type I error rate of each configuration over its scenarios,
from the smallest upward, estimated on a separate pilot simulation with one tenth as many datasets
per scenario, so the order does not depend on the datasets of the test. Fixed-sequence testing then
validates the configurations in this order at levelδand stops at the first configuration that fails.
Continual validation freezes each update, draws new null datasets in every scenario in force, and
runs the update next to the reference analysis on the same datasets. It deploys the update only if
46

every combined bound is at mostα′, and every update goes through this check. The validator adds
scenarios when an update reads information that the scenarios in force do not vary (section A4.5).
The runs below draw no random scenarios (Proposition A18), so the off-grid scenarios measure how
far validation on fixed scenarios reaches, and section A7.9 adds random scenarios. By Theorem A11,
the probability that a run ever deploys an update aboveα′ in a scenario on which it was validated
is at mostδ. An update whose Type I error rate lies far enough belowα′ passes validation with
high probability (Proposition A14).
The feedback reports what each method computes. Under the static benchmark and under
continual validation, it gives the largest upper bound of the update and the scenario that attains
it. Under the improvement test it gives the lower bound on the gain in power. Under Learn then
Test it gives the largest upper bound at levelδthat the configuration reached in the one-time test,
or notes that the update lies outside the menu. When every update is deployed, the feedback states
only that the update was deployed.
The full validation set of an example holds every validation scenario, including every scenario
that the extension can add. The oracle serves only as a reference line, because it needs the true
Type I error rate and the true power of every update, which the evaluation stream of section A7.6
estimates. It deploys an update when all the estimated rates of the update on the full validation
set are at mostα′ and its estimated power exceeds that of the current version. It does not deploy
an update that counts as indeterminate (section A7.6). The oracle runs with the same developer,
also for twenty runs of ten rounds, and its feedback reports the estimates on which it judged each
update.
Every run draws its own random streams for each simulation it uses. These include the stored
set of the static benchmark, the one-time test of Learn then Test and the one-time validation of the
reference analysis. They also include the new datasets of every round, so the runs are independent.
A7.6 Metrics and analysis plan
Five metrics are fixed in advance and are identical in both examples. Metric (a) is the largest true
Type I error rate of the deployed version over the full validation set, after each round. Metric (b)
is the share of runs that ever deployed a version aboveα= 0.05, the level that every decision must
hold, with a Wilson 95 percent interval, together with the same share forα′. Metric (c) is the true
power of the deployed version after each round, together with the ratio of its mean over runs to
the mean of the oracle after the same round. Metric (d) is the largest true Type I error rate of the
version that continual validation deployed, on off-grid null scenarios that no deployment method
ever simulates, after each round. Metric (e) is the number of simulated datasets and the computing
time of each validation.
True rates are estimated in two stages on an evaluation stream that no deployment method
uses, with common random numbers across versions. The first stage draws 100,000 datasets per
scenario for every version. The scenario with the largest first-stage estimate, and every scenario
whose first-stage interval containsα′, are then estimated again from106 datasets on an independent
stream. The second stage removes the upward bias of a maximum taken over many scenarios. Off-
grid scenarios go through the same two stages, with their own largest first-stage estimate. The rate
of a scenario is its second estimate where it has one and its first otherwise, and metrics (a) and
(d) take the largest of these rates. Versions that recur across runs, such as configurations of the
menu, are evaluated once. True power is estimated from 100,000 datasets in each cell of the power
workload of each example (sections A7.4 and A8).
A version counts as aboveα′ when, in some scenario of the full validation set, its interval lies
aboveα′. It counts as withinα′ when its intervals lie belowα′ in every scenario of that set, and as
47

indeterminate otherwise. The same rule withαin place ofα′ decides whether a version counts as
aboveα. The intervals of both stages are exact two-sided Clopper and Pearson intervals at level
0.01/(2K). HereKis fixed in advance as the number of scenarios, off-grid scenarios included, times
the largest possible number of evaluated versions, so that all intervals hold together with probability
at least 0.99. The first stage selects scenarios with these intervals, and a scenario estimated twice
is judged by its second interval. Indeterminate versions are reported separately in metric (b) and
are never counted as withinα′.
The main comparison, fixed in advance, reads metric (b) together with metric (c). With twenty
runs, a method without any failure has a Wilson upper limit of about 16 percent, so metric (b)
separates methods that fail often from methods that rarely fail. The main text reports metric
(b) atαas a percentage of runs and power as the ratio of means after the last round. For no
validation and for continual validation it reports the largest value of metric (a) over all rounds and
runs, which is the largest Type I error rate of any deployed version over the full validation set.
For continual validation it also reports the largest value of metric (d) over all rounds and runs.
Theorem A11 gives the lifetime risk of continual validation, at mostδ, so the experiment does
not estimate it. Metric (b) counts every scenario of the full validation set, including scenarios on
which a deployed version was never validated. For continual validation the experiment therefore
also reports metric (b) on the scenarios on which each deployed version was validated, the event
that Theorem A11 bounds byδ. For each method the experiment also reports how many of the
updates it received were truly aboveα′, and by how much each of them exceededα′. It reports
the number of indeterminate updates beside them. For every deployed version aboveα′, it names
the scenarios in which the version is above, and whether the method simulated them, so that each
failure is traced to a scenario the method checked or to one it never simulated. Metrics (a) and
(d) are summarized round by round by the median and the range over runs, and metric (c) by
the mean. The run with the highest metric (a) after the last round is shown separately for each
method.
A7.7 Implementation requirements
Validation of one update analyzes 500,000 simulated studies in each of up to 936 scenarios. The
validator therefore calls the estimators through a vectorized reimplementation that runs on GPUs,
and every simulation of the experiment, the evaluation stream included, uses it. The reimplemen-
tation decides on unrounded bounds, as every version of the experiment does. It reproduces the
published Method A results for the two EMA reference datasets, the point estimate, the 90 percent
interval and the coefficient of variation to two decimals in percent and the two outlying subjects of
data set I, and the results for all 30 reference datasets of replicateBE. On simulated studies of both
designs and both analysis sets it agrees with a direct least-squares computation for each study to
within10−9, and every configuration of the menu reaches the same decision for every study.
A7.8 Results
Table A4 summarizes the five deployment methods and the oracle. Under every method the devel-
oper followed a similar path. In its first rounds it raised the level of the two one-sided tests toward
the regulatory 0.05, switched to ABEL, or removed a deferral rule, and in later rounds it wrote
new decision rules. The twenty runs of each method followed twenty different sequences of updates.
Under continual validation the developer proposed 112 distinct versions, 32 percent of its updates
were new decision rules, and 18 of the twenty runs ended with such a rule. Under Learn then Test
it proposed 37 new decision rules, none of which that method could deploy.
48

Table A4:Example 1. For each method, the runs that ever deployed a version aboveα= 0.05and above
α′, with Wilson 95 percent intervals in percent, the largest true Type I error rate of any deployed version,
the mean true power after the last round and its share of the oracle’s, the updates received and how many
of them created a version aboveα, and for the methods that simulate null datasets the datasets of one
validation in millions and its median time in seconds on one GPU.
Method Runs aboveαRuns aboveα ′ Largest rate Power % of oracle Updates AboveαDatasets (millions) Seconds
No validation 20/20 (84 to 100) 20/20 (84 to 100) 0.098 0.86 129 200 188
Static benchmark 4/20 (8 to 42) 6/20 (15 to 52) 0.060 0.60 90 200 68 180 569
Improvement test 20/20 (84 to 100) 20/20 (84 to 100) 0.098 0.90 134 200 188
Learn then Test 0/20 (0 to 16) 0/20 (0 to 16) 0.045 0.35 52 197 36
Continual validation 0/20 (0 to 16) 0/20 (0 to 16) 0.045 0.55 82 198 32 447 1101
Oracle 0/20 (0 to 16) 0/20 (0 to 16) 0.044 0.67 196 40
One run of continual validation shows how the developer used the feedback. Its first update
raised the threshold of the deferral by variability to 0.5, which passed. Validation then refused
ABEL with an upper bound of 0.0600 in resampled studies of dataset 11. The developer wrote that
the inflation of ABEL comes from the switch between the standard and the widened limits near a
coefficient of variation of 30 to 40 percent, and its third update was a rule that applies ABEL but
defers the studies whose observed coefficient of variation lies between 0.25 and 0.45, which passed
with a bound of 0.0375. Two later increases of the level, to 0.04 and 0.035, were refused at 0.0558
and 0.0504. The developer then narrowed the deferral zone of its rule to 0.28 to 0.40, which passed
with a bound of 0.0452, and its last update kept the current settings, with the comment that it saw
no safe change left that would add decisions. Its final version reached a true power of 0.79 with a
largest true Type I error rate of 0.043.
No validation and the improvement test deployed a version above 0.05 in every run, in most
runs within the first two rounds, when the developer switched to ABEL or raised the level. These
versions exceeded 0.05 in the Gaussian scenarios with a coefficient of variation from 0.28 to 0.40,
where the switch of ABEL inflates the error, in the scenarios added for new decision rules, and in
resampled studies of datasets 10 and 11. The static benchmark refused the updates that exceeded
0.05 in datasets 10 and 11, because its stored set contains these datasets. It still deployed a version
above 0.05 in 20 percent of runs and aboveα′ in 30 percent. Every scenario in which such a version
exceeded 0.05 was a Gaussian scenario at a coefficient of variation of 0.30, with or without unequal
allocation and period effects, and the stored base set contains none of them. Continual validation
adds exactly these scenarios when an update reads the observed variability or adds a new decision
rule.
Continual validation deployed no version aboveα′ in any run, neither over the full validation
set nor on the scenarios on which each version was validated, which is the event that Theorem A11
bounds. It judged 198 updates and deployed 117. Of the 81 it refused, the evaluation stream
placed 62 aboveα′ and 19 within the Monte Carlo resolution ofα′, so validation refused no update
that was clearly valid. The versions with the highest power, such as ABEL at a lowered level
for highly variable studies, have rates within a few thousandths ofα′, and certifying them takes
more simulated datasets in later rounds, where the sharesδr are small. With 100,000 datasets
per scenario, continual validation refused 17 valid updates and attained 74 percent of the oracle’s
power, and with 500,000 it attained 82 percent. On the 690 off-grid scenarios its deployed versions
stayed at or below 0.058. Every off-grid rate above 0.05 came from dropout that depends on the
first-period response in datasets 22 and 28, which validation never uses, a mechanism that the
validation scenarios of this example do not contain. Each validation simulated about 447 million
studies and took a median of 1101 seconds on one GPU, and the one-time validation of the reference
analysis took a median of 668 seconds per run.
49

Two open-weight models, Qwen 3.8 with 27 billion parameters and the 32-billion-parameter
distilled version of DeepSeek-R1, served as developers through Purdue’s GenAI Studio under three
of the methods, with the same instructions and 100,000 datasets per scenario. Their replies were
malformed in 7 and 21 percent of rounds, and none of the methods deployed a malformed update.
Table A5 shows that no validation and the improvement test again deployed versions above 0.05
in every run, while continual validation kept every deployed version within the level.
Table A5:Example 1 with open-weight developer models and 100,000 datasets per scenario. Columns as
in Table A4, for the methods run with each model.
Developer Method Runs aboveαRuns aboveα ′ Largest rate Power Updates Aboveα
Qwen 3.8 27B No validation 20/20 (84 to 100) 20/20 (84 to 100) 0.236 0.96 183 152
Improvement test 20/20 (84 to 100) 20/20 (84 to 100) 0.301 0.96 181 143
Continual validation 0/20 (0 to 16) 0/20 (0 to 16) 0.043 0.57 192 32
DeepSeek-R1 32B No validation 20/20 (84 to 100) 20/20 (84 to 100) 0.098 0.74 147 104
Improvement test 20/20 (84 to 100) 20/20 (84 to 100) 0.098 0.74 150 104
Continual validation 0/20 (0 to 16) 0/20 (0 to 16) 0.043 0.26 175 49
In a further experiment, every method received the same fixed list of ten updates, written in
advance, in the same order, and Fig. A2 shows which updates each method deployed and the true
rate of the version each update would have created. In Example 1 continual validation refused the
switch to ABEL, the level of 0.05 and the rule with scaled limits above a coefficient of variation
of 0.35, which would all have exceeded 0.05, and it deployed the rule for the partial replicate and
the rule with scaled limits above 0.40, whose rates stay within the level. The static benchmark
deployed the switch to ABEL, whose rate exceeds 0.05 only near a coefficient of variation of 0.30,
outside its stored set. Learn then Test refused all three new decision rules. In Example 2 continual
validation refused daily looks without sequential testing and the Bayesian threshold of 0.95, and it
deployed sequential testing, post-stratification and the rule with two planned looks.
50

No validation
Static benchmark
Improvement test
Learn then Test
Continual validation
Oracle
1. Analyze flagged files
2. Defer above CV 0.40
3. Expanding limits (ABEL)
4. Level 0.05
5. Substitute outlier analysis
6. New rule, contrast for partial replicate
7. New rule, scaled above CV 0.35
8. New rule, scaled above CV 0.40
9. Available-case set
10. No deferral by CV
No validation
Static benchmark
Improvement test
Learn then Test
Continual validation
Oracle
1. Regression adjustment
2. Daily looks
3. Sequential testing
4. Post-stratification
5. Any goal metric
6. Bayesian, chance to win 0.95
7. Segment analyses
8. New rule, two planned looks
9. Level 0.045
10. Remove the new rule
Bioequivalence agentA Analyst of product experimentsB
Within the validation level Above the validation level Above 0.05 Open: not deployed
Figure A2:Updates written in advance. The same ten updates, in the same order, judged by every method
in (A) Example 1 and (B) Example 2. A filled circle marks an update the method deployed and an open
circle one it did not. The color gives the true Type I error rate of the version the update would create,
withinα ′ or too close toα′ to resolve (blue), aboveα′ (orange), or also aboveα(vermilion).
A7.9 Random scenarios cover the space between the grid values
The runs above validated every update on fixed scenarios and added scenario kinds when an update
read new information (section A4.5). The third layer of continual validation draws new scenarios at
random after every freeze (section A4.6), so that no version can overfit the scenarios that validation
uses. We ran this layer in Example 1.
The distributionΠwas fixed before the first run, and its draws are independent. With probabil-
ity one half a draw resamples one of the ten validation datasets, chosen uniformly, with the design
and coefficient of variation of that dataset. Otherwise it is a Gaussian model whose coefficient
of variation is uniform on 0.20 to 0.55 and whose design is the full or the partial replicate with
probability one half each. The number of volunteers is uniform on 24, 30, 36, 42, 48, 54 and 60,
volunteers drop out independently of their responses at a rate uniform on 0 to 25 percent, and the
true ratio lies at the lower or the upper acceptance limit implied by the true variability or beyond
it by up to 0.05 on the log scale. The grid holds three of these sample sizes, three dropout rates
and two placements of the ratio, so most draws fall between or beyond its values. The five datasets
that validation never uses stay outsideΠ, and the off-grid scenarios remain an independent test.
Dropout that depends on the response also stays outsideΠ, because it moves the starting version
of every run, the reference analysis with its two deferral rules, aboveα, to a true Type I error rate
of 0.059 on dataset 5 with 48 volunteers and 20 percent dropout.
In roundr, after the freeze, continual validation with random scenarios addsKr scenarios drawn
fromΠon a random stream that the developer never sees. A drawn scenario takes the reference
bound where it is known without simulation, zero on the partial replicate andα0 on a Gaussian full
replicate, and the trivial bound 1 otherwise, so that the direct bound decides it. All scenarios of
the round, fixed and drawn, must pass together. WithεΠ = 0.05andω= 0.005,K r is the smallest
integer with(1−ε Π)Kr≤6ω/(π 2r2), which gives 113 scenarios in the first round and 203 in the
51

tenth. By Proposition A18, with probability at least1−δ−ω= 0.99every deployed update is
then withinα′ on every fixed scenario of its round and on all ofΠexcept a set of probability at
most 0.05. Every drawn scenario uses 500,000 simulated studies, as the fixed scenarios do.
In a second experiment with updates written in advance, continual validation on the fixed
scenarios and continual validation with random scenarios received the same ten updates in the
same order, each method in three runs with different validation streams (Fig. A3A). Six updates
come from the runs above, a deferral threshold of 0.50, two new decision rules that defer studies
near the switch to widened limits, the analysis of flagged files, the level 0.035 and the removal of
the deferral threshold. The other four, the off-grid updates, copy the current analysis at the sample
sizes of the grid and switch to widened limits at level 0.05 without deferral at every other size,
at sizes above 48 volunteers, or at 30 and 42 volunteers, the version that section A4.6 describes.
Twenty further runs used continual validation with random scenarios and Claude Sonnet 5.5 as
developer, with the instructions and simulation sizes of the runs above. The coverage ofΠby a
deployed version was measured on 300 scenarios drawn fromΠon a separate evaluation stream,
each with 100,000 simulated studies, as the share of scenarios in which its true Type I error rate
exceedsα′.
Continual validation on the fixed scenarios deployed all four off-grid updates in each of the three
runs, because on the grid they decide exactly like the version in use. With random scenarios it
refused all twelve (Table A6), each time on a drawn scenario whose sample size lies outside the grid,
with upper bounds from 0.055 to 0.088. The versions these updates create exceedα′ on at most 4
percent ofΠ, and the draws of every round found that region. Both methods deployed the same five
realistic updates in every run, with nearly equal bounds, and both refused the level 0.035, whose
excess the grid itself detects. The versions that passed on the fixed scenarios reached a true Type
I error rate of 0.098 at sample sizes outside the grid, about twiceα, while every version deployed
with random scenarios stayed at or below 0.042 there (Figs. 3Aand A3B). The last versions of both
methods had the same power, 0.78, and the same largest rate on the validation scenarios, 0.043,
so the random scenarios removed only the behavior that the grid cannot see. Under dropout that
depends on the response, which lies outsideΠ, the last versions of both methods reached 0.065, as
in the runs above.
The random scenarios cost nothing when the updates did not target the grid. None of the 69
versions that continual validation deployed on the fixed scenarios in the runs above exceededα′ in
any of the 300 scenarios drawn fromΠfor the evaluation, and their largest rate there was 0.041.
In the 20 runs with random scenarios, no run deployed a version aboveα, the largest rate on the
validation scenarios was 0.045, and the deployed versions reached 79 percent of the oracle’s power,
against 82 percent on the fixed scenarios, a difference in final power of 0.021 with a Welch testp
value of 0.67 (Figs. 3Band A3C). The fixed scenarios decided every one of the 85 updates that
this method refused, and none of its 62 deployed versions exceededα′ in a scenario drawn fromΠ
for the evaluation.
52

Table A6:Random scenarios in Example 1. Updates written in advance, three runs per method with the
ten updates of Fig. A3A. Live runs, 20 runs per method with Claude Sonnet 5.5 as developer, the runs on
fixed scenarios being those of Table A4. Rates are true Type I error rates of the deployed versions, on the
validation scenarios and at the sample sizes outside the grid of the off-grid scenarios. The share ofΠis the
largest, over the deployed versions, share of 300 scenarios drawn fromΠon an evaluation stream in which
the true rate exceedsα′. Power is that of the last version after the updates written in advance and the share
of the oracle’s power in the live runs.
Updates written in advance Live runs
Fixed scenarios Random scenarios Fixed scenarios Random scenarios
Off-grid updates deployed 12/12 0/12
Updates deployed 27/30 15/30 117/200 113/200
Runs aboveα, validation scenarios 0/3 0/3 0/20 0/20
Largest rate, validation scenarios 0.043 0.043 0.045 0.045
Largest rate, sizes off the grid 0.098 0.042 0.042 0.043
Largest share ofΠaboveα ′ 0.04 0 0 0
Power 0.78 0.78 82% 79%
Fixed
scenarios
With random
scenarios
Defer above CV 0.50
Relax at sizes off the grid
New rule, defer CV 0.25 to 0.45
Relax above 48 volunteers
Analyze flagged files
Relax at 30 or 42 volunteers
Level 0.035
New rule, defer CV 0.28 to 0.40
Narrow rule, relax off the grid
No deferral by CV
0 2 4 6 8 10
Update round
0.04
0.05
0.06
0.07
0.08
0.09
0.10
Type I error, sizes off the grid
α
α′
0 2 4 6 8 10
Update round
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
Power
oracle
A Ten updates written in advance B Deployed version, sizes off the grid C Power in 20 runs with Claude
Continual validation, fixed scenarios With random scenarios
within α′
above α′
above α
deployed
not deployed
Figure A3:Random scenarios in Example 1. (A) Updates written in advance. The same ten updates, in
the same order, judged by continual validation on the fixed scenarios and with random scenarios, in the first
of three runs, and the other runs made the same decisions. Bold labels mark the four updates that relax the
analysis only at sample sizes outside the grid. A filled circle marks a deployed update and an open circle a
refused one. The color gives the largest true Type I error rate of the version the update would create, on
the validation scenarios or at the sample sizes outside the grid, withinα′ (blue), aboveα ′ (orange) or above
α(vermilion). (B) Largest true Type I error rate of the deployed version at 30, 42 and 60 volunteers, the
sample sizes of the off-grid scenarios outside the grid, after each round of these updates. (C) Mean true
power of the deployed version over 20 runs with Claude Sonnet 5.5 as developer, on the fixed scenarios (the
runs of Fig. 2D) and with random scenarios, and of the oracle (dashed).
A7.10 The agent reaches the decisions of the validated rule
The agent is a broader tool than the analyst of this example. Besides the analysis, it plans studies,
proposing a design and a sample size and checking their robustness, assesses the protocol before the
data arrive, and writes the report of each run. The analyst is its analysis part, from the data file to
the decision on bioequivalence. It changes only through the updates of section A7.5, new settings
and new decision rules in code that the developer proposes and the validator runs. Validation runs
the decision rule of each version through the vectorized reimplementation, and by Proposition A19
the measured rate bounds that of the analyst because every run of the agent ends in the decision of
this rule or in a deferral. We checked on simulated studies that the agent reaches these decisions,
53

first with its deterministic tools alone and then with the full agent driven by its language model.
The studies came from the validation scenarios of section A7.4. One null study was simulated in
each of 150 scenarios with the true ratio at a limit, and one alternative study in each of 150 workload
cells with a true ratio of 0.95 or 1.00. Each study was written as a data file in the format that the
agent reads and analyzed under three configurations at level 0.030, unscaled average bioequivalence
on the complete case, which is the reference analysisv0, and ABEL on the complete and on the
available case. The tools ran the computing steps of the analysis in the order of the playbooks,
opening the study, inspecting and preparing the data, fitting the model, running the diagnostics
and computing the interval. In all 900 cases the tools reached the decision of the rule (Table A7).
They refused the 88 cases of unscaled average bioequivalence on the partial replicate, which are
exactly the cases in whichv0 defers. In the other 812 cases the bounds of the interval agreed within
3.2×10 −15 on the log scale, and under ABEL the within-reference coefficient of variation agreed
within2.4×10 −15 and the degrees of freedom agreed exactly.
The agent decides on the bounds in percent rounded half up to two decimals, while every version
of the experiment decides on unrounded bounds. Rounding changed none of the 900 decisions. Its
effect on the true Type I error rate was computed in all 936 validation scenarios with 500,000
simulated studies each, by applying unscaled average bioequivalence and ABEL on the complete
case at level 0.030 to the same studies with and without rounding. Rounding changed the rate by
at most 0.0003 in any scenario. Validation applies to whatever decision code the analyst runs, so
a deployment that decides on rounded bounds validates the rounded rule.
The full agent then ran each study as it runs for a user. Claude Sonnet 4.6 in Claude Code drove
the analysis through the skills and playbooks of the agent, from the check of the protocol to the
review of the evidence, one session per case, and each session received only the entry command of
the agent with the case. Most of the 14 cases lay where a slip would change the decision. They were
the three null cases of each configuration whose interval lay closest to a claim without a claim by the
rule and the alternative case of each configuration closest to the boundary with a claim, together
with one alternative case far from the boundary and one case in whichv0 defers. In the closest null
case the lower bound of the interval was 79.985 percent, just below the limit of 80.00 percent. The
agent reached the decision of the rule in all 14 cases (Table A7). It claimed bioequivalence in the
four alternative cases and in none of the nine null cases, and its intervals agreed with those of the
reimplementation within4×10 −16 on the log scale. In the case in whichv0 defers, it stopped at
the check of the protocol and handed the study to a human, because the protocol paired unscaled
average bioequivalence with the partial replicate. A session that completed the analysis took about
five minutes and cost about 1.5 dollars at the list price of the model, so running the full agent on
the 500,000 studies of a single scenario would cost about 750,000 dollars. Validation therefore runs
the decision rule, and these checks found no case in which the agent departed from it.
Table A7:Agreement of the bioequivalence agent with the decision rule that validation runs, on simulated
studies of Example 1. The tools are the deterministic tools of the agent run without the language model,
and the full agent is driven by Claude Sonnet 4.6 in Claude Code. A case is a study analyzed under one
configuration.
Tools Full agent
Cases 900 14
Same decision as the rule 900 14
Deferred where the rule decides 0 0
Claims where the rule makes none 0 0
Refused where the rule defers 88 of 88 1 of 1
Largest difference of the bounds, log scale3.2×10 −15 3.9×10 −16
54

A8 Example 2, an analyst of product experiments built on an
open-source platform
The second example asks the question of section A7 for an analyst in another field. It uses the
same developer, deployment methods, oracle and metrics (sections A7.5 and A7.6), and this section
gives what is specific to it.
A8.1 The hypothesis test
Companies test a new feature of an online product in an experiment, often called an A/B test.
Users are randomly assigned to the current product or to the new feature, and a primary metric,
here conversion, the share of users who buy, is compared between the two groups. The true relative
lift is the conversion rate with the new feature divided by the rate with the current product, minus
one. The null hypothesisH0 is that the lift is at most zero, so that the feature does not improve
conversion, and the alternativeH1 is that the lift is positive. A launch rejectsH0, and a Type I
error is a launch of a feature that does not improve conversion. Analysts have freedoms that can
inflate this rate. They may look at the results every day and stop at the first look that favors a
launch, a practice known as optional stopping. They may choose among metrics or user segments
post hoc, after seeing the results. They may also switch between frequentist and Bayesian decision
rules.
A8.2 GrowthBook and the analyst
GrowthBook is an open-source platform for feature flags, experimentation and product analytics
[16]. Its statistics engine is the Python package gbstats, released under the MIT License. The
package provides frequentist two-sided and one-sidedttests, sequential testing with a tuning pa-
rameter, and a Bayesian engine that reports the chance to win, the posterior probability that the
new feature is better. It also provides regression adjustment for pre-experiment data in the style of
CUPED [17], post-stratification, and analyses by dimension, which split the users into segments.
It handles several goal metrics with an option to correctpvalues, and its levelαcan be set.
In this example a language model analyzes product experiments with GrowthBook. It runs
the gbstats analyses that the configuration of the version fixes and decides whether to launch,
and gbstats computes every number. The configuration fixes the analyses that gbstats runs and
the launch rule, which states the results that lead to a launch. The model may decline a launch
that the launch rule allows, but it cannot launch when the rule does not. The allowed paths
are therefore the gbstats analyses of the configuration, and the any-path rule is the launch rule
itself (Proposition A19). Validation runs gbstats on simulated experiments and needs no calls to a
language model.
A8.3 Reference analysis, settings and new decision rules
The reference analysisv 0 is the one-sided frequentistttest of gbstats on conversion at the end
of the experiment, at the reference levelα0 = 0.040. It tests the relative lift in conversion and
launches when the test rejects. Metric distributions in product experiments are not Gaussian, so no
analytic bound covers this test. Its reference bounds come from a one-time validation atδ0 = 0.001
(Corollary A16). Before the first update of each run, the validator simulates106 experiments in
every scenario of the full validation set, including the scenarios that the extension may add, and
dividesδ 0 equally among these scenarios. The two checks of section A7.3 follow, on the base set of
55

32 scenarios below and on the full validation set, and a run whose first check fails starts from the
version that defers every experiment.
An update may change one of eight settings.
•Engine. Frequentist, or Bayesian with a launch when the chance to win is at least 0.95, 0.975
or 0.99.
•Regression adjustment. On or off. When it is on, the primary metric is adjusted for its
pre-experiment value.
•Sequential testing. On, with tuning parameter 5,000, or off.
•When to decide. Only at day 14, or once a day from day 1 to day 14, with a launch at the
first look at which the configured rule says launch.
•Goal metrics. The primary metric only, or a launch if any of three goal metrics wins, with or
without a correction of thepvalues.
•Segments. The overall analysis only, or a launch if the overall analysis or the analysis of any
of three segments wins.
•Post-stratification. On or off, with the segments as strata.
•Level of the frequentist test. 0.040, 0.045 or 0.050.
A metric wins when its one-sided test rejects at the configured level, or when its chance to win
reaches the threshold. The correction ofpvalues applies Holm’s step-down procedure across the
three goal metrics. Sequential testing, the correction and the level apply only to the frequentist
engine, and the Bayesian engine keeps its default prior. The menu therefore holds 384 distinct
configurations, and the reference analysis is one of them. An experiment that its rule has not
launched by day 14 ends at day 14 without a launch.
An update may instead add a new decision rule, a Python function that acts on the outputs of
gbstats and states when to launch. The interface calls the rule once a day, from day 1 to day 14,
with the results up to that day for a batch of simulated experiments. The rule may request the
results that gbstats reports for any metric, segment and setting. These results are the estimated
lift with its interval, thepvalue, the chance to win and the numbers of users. For every experiment
the rule returns launch or wait, and the first launch fixes the day of the decision.
A8.4 Scenarios, workload and simulation sizes
In every validation scenarioH 0 holds, because the new feature does not raise conversion. Each
arm has 20,000 or 100,000 users, who arrive over 14 days. The users of an arm fall into the
42 combinations of day and segment by a multinomial law with equal probabilities, so the three
segments have equal expected size. Every user has three metrics and a covariate. Conversion, the
primary metric, is binary. Its average rate is 2 or 10 percent, and the three segments convert at
one half, one and one and a half times this rate. Revenue is zero for users who do not convert
and heavy-tailed for users who do, equal toexp(3 + 1.5W), whereWis the standard normal latent
variable of revenue in the copula below. Engagement counts the actions, out of seven possible, that
a user takes on the day of arrival, and follows a binomial distribution with 7 trials and success
probability 0.3. The covariate is the conversion of the user before the experiment, at the rate of
the user’s segment. All outcomes of a user are observed on the day of arrival, so a look on dayd
sees every user who arrived up to dayd.
56

A Gaussian copula links the four outcomes of a user. The latent variables of conversion, revenue
and engagement share the correlationρ∈{0,0.5}. The latent variable of the covariate depends on
the others only through that of conversion. Its correlation with that variable is set, within every
segment, so that the covariate and conversion have correlationc∈{0,0.5}. The null scenarios are
of two kinds. In the first the new feature changes nothing. In the second it lowers conversion by
2 percent in relative terms, a lift of−0.02that lies beyond the boundary ofH 0. The base set,
the initial scenario set of this example, crosses two sample sizes, two conversion rates, two metric
correlations, two covariate correlations and the two kinds, which gives 32 scenarios.
The validator generates the sufficient statistics that gbstats consumes and never simulates the
users who do not convert one at a time. For each arm, day and segment, it draws the number of
converting users. It draws the counts of the other users over the combinations of covariate and
engagement from a multinomial law whose probabilities come from the copula. It simulates the
converting users one at a time, which gives their revenue, engagement and covariate jointly. From
these draws it forms the counts, sums, sums of squares and the cross products that regression
adjustment needs, cumulated over days for every daily look. Simulating only the converting users
keeps the simulation of 500,000 experiments per scenario inexpensive.
Every setting except the daily looks and the segments depends on the data only through quan-
tities that the base set varies. A decision at daily looks also depends on how users arrive over the
days, and segment analyses and post-stratification depend on the shares of the segments. A new
decision rule can read the numbers of users by arm, day and segment. The base set holds all of
these fixed or uniform. Every update that decides at daily looks or uses segments, through segment
analyses or post-stratification, and every new decision rule, is therefore also validated on 32 added
scenarios (section A4.5). They repeat the base set with users assigned to the arms by a fair coin,
arrivals on days 6, 7, 13 and 14 at half the rate of the other days, and expected segment shares of
one half, three tenths and one fifth, in the order of the segments above, with the segment conversion
rates unchanged. The full validation set therefore holds 64 scenarios.
Off-grid scenarios, which no deployment method ever simulates, move the nuisance parameters
of the base set between or beyond its grid values. The off-grid values are 50,000 users per arm,
an average conversion rate of 5 percent, heavier revenue tails withexp(3 + 2.0W)in place of
exp(3 + 1.5W), metric correlations of 0.25 and 0.75, and a covariate correlation of 0.25. Five
families each change one of these parameters to its off-grid values and keep the grid values of the
others. One more family changes all of them together. Every family crosses its values with the two
kinds of null scenario, which gives 116 scenarios.
Power is measured on experiments in which the new feature raises conversion by 1, 2 or 3 percent
in relative terms and changes nothing else. The workload crosses these lifts with the sample sizes,
conversion rates, metric correlations and covariate correlations of the base set, which gives 48 cells
of equal weight. As in the second kind of null scenario, the new feature multiplies the conversion
rate of every segment by the same factor and leaves the copula unchanged. Power is the probability
of a launch, averaged over the cells. The usefulness metric of the performance report is the share of
workload experiments launched and the median number of days to the decision. An experiment that
is not launched counts at day 14. The metric is estimated each round from 10,000 new workload
experiments, and the experiment reports it alongside the five metrics. The performance report and
the improvement test draw each workload experiment from a cell chosen uniformly at random.
Continual validation draws 500,000 experiments per scenario per update. The static benchmark
stores 500,000 experiments per scenario of the base set, and the improvement test draws 500,000
new workload experiments per round. Learn then Test tests the 384 configurations once on 500,000
experiments per scenario, after a pilot of one tenth that size.
57

A8.5 Implementation requirements
Validation needs an analysis for every metric, segment and daily look of every simulated experiment.
The validator therefore calls the computations of gbstats through a vectorized reimplementation,
and every simulation of the experiment, the evaluation stream included, uses it. It matches gbstats
itself, taken from its repository at commit b71bbbc, on 300 random sets of statistics across the three
metric types, with and without post-stratification. Lifts, interval bounds,pvalues and chances to
win agree to within10 −12, and the launch decision and day of 75 random pairs of simulated
experiment and configuration equal those that gbstats computes. On GPUs and on processors it
gives the same decision for every configuration of the menu.
A8.6 Results
Table A8 summarizes the five deployment methods and the oracle. Every run began with regression
adjustment. The developer went on to post-stratification, the level of the test, Holm’s correction or
any goal metric, sequential testing, daily looks, Bayesian launch rules and segment analyses, and it
wrote new decision rules. The twenty runs of each method followed twenty different sequences of
updates. Under continual validation the developer proposed 62 distinct versions, 21 percent of its
updates were new decision rules, and 15 of the twenty runs ended with such a rule. Under Learn
then Test it proposed 18 new decision rules, none of which that method could deploy.
Table A8:Example 2. Columns as in Table A4.
Method Runs aboveαRuns aboveα ′ Largest rate Power % of oracle Updates AboveαDatasets (millions) Seconds
No validation 12/20 (39 to 78) 20/20 (84 to 100) 0.183 0.22 107 200 33
Static benchmark 0/20 (0 to 16) 0/20 (0 to 16) 0.044 0.20 98 200 6 16 1080
Improvement test 19/20 (76 to 99) 20/20 (84 to 100) 0.817 0.53 255 200 80
Learn then Test 0/20 (0 to 16) 0/20 (0 to 16) 0.043 0.17 80 200 8
Continual validation 0/20 (0 to 16) 0/20 (0 to 16) 0.044 0.20 96 200 4 29 329
Oracle 0/20 (0 to 16) 0/20 (0 to 16) 0.044 0.21 199 9
The developer used the reported bounds to guess the limit. In one run validation refused the
level of 0.05 with an upper bound of 0.0498, and the developer wrote that the limit appeared to be
about 0.04 and kept its later updates below it. Several runs wrote rules that spend the level over
the daily looks, with a strict threshold before day 14 and a larger one at day 14, and then raised
the threshold at day 14 in small steps toward the bound that validation had reported. This is the
tuning against reported results that section A2.3 describes, and because continual validation draws
new datasets for every update, it cannot exploit the noise of earlier draws.
In another run, validation refused daily looks with an upper bound of 0.170. The developer
turned on sequential testing, switched it off again after its performance report showed far fewer
launches, and wrote a rule that spends the level over the daily looks, withpbelow 0.0004 from day
4 to day 13 and below 0.0414 at day 14. The rule passed with a bound of 0.0416, a larger threshold
at day 14 passed in the next round, and the final version had a largest true Type I error rate of
0.043 and a true power of 0.21.
No validation produced a version above 0.05 in 12 of the 20 runs, and the improvement test
did so in 19. These versions exceeded 0.05 after daily looks without sequential testing, sequential
testing switched off while daily looks stayed on, segment analyses, any goal metric, or new decision
rules, and they did so in the base scenarios as well as in the added ones. The largest rate, 0.82,
came from a version deployed under the improvement test. It combined a Bayesian threshold of
0.95 with daily looks, any goal metric and segment analyses. The static benchmark refused the
six updates that would have created a version above 0.05, and it deployed no version aboveα′.
These six were daily looks without sequential testing, sequential testing switched off with daily
58

looks on, and segment analyses, and each of them exceeded 0.05 in base scenarios, which the stored
set contains.
Continual validation deployed no version aboveα′ in any run. It judged 200 updates and
deployed 170. Of the 30 it refused, the evaluation stream placed 28 aboveα′, and the other 2 had
true rates of 0.0435 and 0.0434 and validation bounds that exceededα′ by less than 0.0002. Learn
then Test reached 80 percent of the oracle’s power and continual validation 96 percent. On the
116 off-grid scenarios the deployed versions of continual validation stayed at or below 0.044. Each
validation simulated about 29 million experiments and took a median of 329 seconds on one GPU,
and the one-time validation of the reference analysis took a median of 296 seconds per run.
A9 Other decisions
The validator asks two things of a domain, a simulator for the scenarios in which a rejection is wrong
and a decision rule written out in full. Two supplementary studies used it outside bioequivalence,
for approving a therapy from a survival trial and for launching a feature from an online experiment.
In each study the authors wrote down the shortcuts that an analyst under pressure to find an effect
might take. They also wrote down adaptive rules that pay for their adaptivity, and the validator
judged each rule against a fixed reference analysis. In both decisions, at the one-shot level of0.05,
every shortcut fails validation and every rule that pays for its adaptivity passes. In the online
experiment, the best rule that passes keeps nearly all of the power of the reference analysis while
using a smaller sample on average. In the survival trial, the best rule that passes raises power well
above that of the reference analysis.
Both studies follow the conventions of confirmatory trials, in which a rule rejects when it finds
a significant two-sided difference. The therapy is approved or the feature launched when that
difference favors it, so the Type I error rate bounds the rate of false approvals and of false launches.
The rules of each study were fixed in advance and judged once, on simulated studies they
shared, by a one-shot form of validation. The reference analysis was validated from scratch with
exact Clopper and Pearson bounds [2]. Each rule was then compared with the reference analysis on
the same simulated studies. The comparison used an upper confidence bound on the rule’s added
rejections and a lower confidence bound on its removed rejections (Theorem A8). A rule’s bound
is the bound of the reference analysis plus the rule’s largest paired increment, and a rule passes
when this bound is at most0.05. The bounds of the reference analysis and of each rule held at
confidence 0.975, simultaneously over the scenarios.
This one-shot validation differs from continual validation (Algorithm A1) in four respects. Its
target is0.05, where Algorithm A1 validates at the validation levelα′ = 0.0452. Its error level is
split across the scenarios, where Algorithm A1 gives every scenario the whole shareδr. Its bound
adds the largest increment over the scenarios to the largest reference bound, where Algorithm A1
combines the bounds within each scenario and also uses the direct bound. In the online experiment
its reference analysis runs at0.045, where Example 2 uses the reference levelα0 = 0.040. The
bounds of the survival rules that pass lie belowα′. In the online experiment the bounds of the
rules that pass and of the reference analysis lie betweenα′ and0.05. These bounds would fail at
α′, henceα 0 = 0.040in Example 2.
A9.1 Approving a therapy from a survival trial
A two-arm trial compares survival under a new therapy with survival under control. In every null
scenario the two arms share one Weibull survival distribution. The scenarios cross its shape (0.75,
1 or 1.25), the fraction of patients censored (0.2 or 0.4) and the number of patients per arm (100
59

or 200). The crossing gives 12 scenarios with 50,000 simulated trials each, all with independent
uniform censoring. Power is measured under a delayed effect, with no difference before a fixed time
and a hazard ratio of 0.40 after it. Delayed effects are common in immunotherapy trials, and under
them the log-rank test loses power and analysts look for alternatives.
The individually valid analyses are the log-rank test, the difference in restricted mean survival
time (RMST) at a prespecified horizon, and the Fleming-Harrington test FH(0,1). FH(0,1) is a log-
rank test that gives late events more weight. A prespecified diagnostic compares log-rank statistics
computed before and after the median survival time of the control group and flags hazards that
are not proportional. The reference analysis, the log-rank test at level 0.040, was validated from
scratch with bound 0.0448, and its power under the delayed effect is 0.432.
Table A9:Decision rules for approving a therapy from a survival trial
Rule Type I error rate Bound Validation Power
Log-rank test at level 0.040 (reference anal-
ysis)
0.0448 reference 0.432
RMST when the log-rank test misses and
the diagnostic flags
0.0684 0.0735 fails 0.475
RMST at the best of three horizons 0.0843 0.0924 fails
Prespecified router, RMST when the diag-
nostic flags
0.0554 0.0603 fails 0.220
Log-rank test or FH(0,1), each at half the
level of the reference analysis
0.0343 0.0411 passes 0.627
Router to FH(0,1) when the diagnostic
flags, inner level 0.034
0.0393 0.0450 passes 0.600
The Type I error rate is the largest estimated rate over the 12 null scenarios, each with 50,000 simulated trials. The
bound is the bound of the reference analysis plus the rule’s largest paired increment, and a rule passes validation
when its bound is at most 0.05. Power is the mean over the scenarios under the delayed effect. Blank cells are not
reported.
Table A9 lists six rules, and all three shortcuts among them fail validation. The first two
shortcuts test at the nominal level 0.05. Reporting RMST when the log-rank test misses and
the diagnostic flags gives the trial a second chance, and it raises the Type I error rate to 0.0684.
Reporting RMST at whichever of three horizons gives the largest statistic raises it to 0.0843.
The third shortcut, a router fixed before any data were seen, sends the trial to RMST when the
diagnostic flags and to the log-rank test otherwise. Both tests run at level 0.040, and the router’s
Type I error rate is 0.0554.
Fixing a routing rule in advance does not protect it, because the diagnostic is computed from
the trial’s own data and is correlated with both test statistics. Routing between valid tests preserves
their level when the routing information is independent of the statistics and the internal randomness
that the tests use (Proposition A22), which this diagnostic is not. It is also weak, with power 0.220
against 0.432 for the reference analysis.
Two adaptive rules that pay for their adaptivity pass validation. The first rejects when the log-
rank test or FH(0,1) rejects at half the level of the reference analysis, a Bonferroni split. Its bound
is 0.0411, and its power of 0.627 exceeds both the power of the reference analysis and the 0.475 of
the second-chance rule that failed. The second sends the trial to FH(0,1) when the diagnostic flags
and to the log-rank test otherwise, both at an inner level of 0.034. The inner level was chosen on
separate tuning simulations, and the rule was then validated on new ones, with bound 0.0450 and
60

power 0.600. A rule that adapts to the data passes once its adaptivity is paid for.
The union rule also shows the allowed-paths result at work (Proposition A19). Its two paths
are the log-rank test and FH(0,1), each at half the level of the reference analysis. The union is
their any-path rule, and it passed validation. Any rule for choosing between the two paths rejects
only where one of them does. Three such routers were run, a diagnostic router, a coin router and
an adversarial router. The diagnostic router took FH(0,1) whenever the diagnostic flagged, which
happened in 10% of null trials and in 54% of delayed-effect trials. The coin router chose at random,
and the adversarial router took whichever path rejected. Their worst Type I error rates, 0.0239,
0.0220 and 0.0343, all lie below the union’s bound of 0.0411. Their power ranges from 0.484 for
the coin router through 0.542 for the diagnostic router to 0.627 for the adversarial router. The
validation covers every way of choosing among the allowed paths, so it never needs to know how a
model makes that choice.
A9.2 Launching a feature from an online experiment
An online experiment compares a new feature with the current product on 3 correlated metrics and
analyzes the accumulating data at 5 equally spaced looks. In every null scenario the feature has
no effect on any metric. The scenarios set the correlation between metrics to 0, 0.5 or 0.9, with
200,000 simulated experiments each. The reference analysis tests the primary metric once, at the
final look, at level 0.045. It was validated from scratch with bound 0.0466, and its power is 0.785
when the final z-statistic of the primary metric has mean 2.8 and the correlation is 0.5.
Table A10:Decision rules for launching a feature from an online experiment
Rule Type I error rate Bound Validation Power
Primary metric at the final look, level 0.045
(reference analysis)
0.0466 reference 0.785
Stop at the first nominally significant look 0.142 0.1449 fails 0.848
Report the best metric at the final look 0.144 0.1466 fails 0.827
Both shortcuts together 0.370 0.3737 fails 0.897
O’Brien-Fleming stopping at level 0.045 0.046 0.0481 passes 0.776
Bonferroni over the metrics at level 0.045 0.045 0.0482 passes 0.654
The Type I error rate is the largest estimated rate over the correlation scenarios 0, 0.5 and 0.9, each with 200,000
simulated experiments. Nominal significance means a two-sided test at 0.05. Power is the probability of a rejection
when the final z-statistic of the primary metric has mean 2.8, at correlation 0.5.
Three shortcuts that an analyst chasing significance might take fail validation (Table A10).
Stopping at the first look at which the primary metric is nominally significant raises the Type I
error rate to 0.142. Reporting whichever metric is most significant at the final look raises it to
0.144, and doing both raises it to 0.370. The shortcuts buy power, up to 0.897, by exceeding the
level0.05several times over.
Tworulesthatpayfortheirextralooksormetricspassvalidation. AnO’Brien-Flemingstopping
rule [18] compares the z-statistic of the primary metric at lookkwith the boundaryc
√
5/k, where
c= 2.077gives the level 0.045. Its bound is 0.0481, and its power of 0.776 is close to the 0.785
of the reference analysis. Under the same alternative it stops on average after 81% of the planned
sample. A Bonferroni rule that splits the level equally across the 3 metrics passes too, with bound
0.0482, at a power of 0.654. Validation charges for every look at the data, and how much power a
rule keeps after paying depends on how it spends the level.
61

A10 Supplementary studies
TheclosedloopofsectionA10.1showscontinualvalidationatworkwithalanguage-modelproposer,
under the parameters stated there. The other studies measure quantities that the theory leaves
open. They ask how far composition raises the Type I error rate, how a regulatory switching
rule behaves, how large a validity reserve must be, and how differently language models behave as
analysts. The last study checks the analysis code against published results.
A10.1 A closed loop with a language-model proposer
In this study a language model, claude-sonnet-5, proposed updates to a bioequivalence analyst over
8 rounds. Only the validator stood between an update and its deployment. A version was a config-
uration with five fields, the first of which set how studies with dropouts are handled. Such studies
could be deferred to a human, analyzed on completers, or analyzed with the first-period data of the
subjects who dropped out. The other fields set the observed within-subject variability above which
the version defers and whether data-quality problems of a declared kind are repaired automatically.
They also set the role of a prespecified sensitivity analysis that drops the most outlying subject
and an optional threshold for excluding outlying subjects from the primary analysis. The starting
version deferred any study with dropouts, an observed within-subject coefficient of variation above
0.40 or a data-quality flag.
Each update changed a single field of the current configuration. The fields allow updates that
guidancedoesnotaccept, suchasexcludingsubjectsfromtheprimaryanalysisforstatisticalreasons
[7, 1]. They were kept as tempting updates, and the validator judged each update by its Type I error
rate alone. The proposer saw the current configuration, the documentation of the interface, the
deferral rate of the current version with its causes, its power, and all earlier deployment decisions
with their bounds and worst scenarios. It never saw the simulated studies that the validator used.
Each update was frozen before the validator drew its simulated studies, and each round drew
new randomness, independent of everything the proposer had seen. The validator ran the updated
version and a validated reference analysis on the same 50,000 simulated studies in each of 432
null scenarios at the equivalence boundaries. The scenarios crossed within-subject coefficients of
variation from 20 to 50%, 24 to 48 subjects, balanced or 60/40 allocation, dropout up to 20% and
a sequence effect up to 0.2. The reference analysis applied the two one-sided tests at level 0.0452,
the level found in section A10.4, to the completers and never deferred. Its validation from scratch,
on 400,000 simulated studies per scenario, gave the bound 0.04749.
The parameters of this implementation differ from those of the main text, starting with a
lifetime risk of 0.05. With a validation level of 0.05, the formula of Corollary A12 bounds the Type
I error rate of each decision by0.05 + 0.95·0.05 = 0.0975. Half of the lifetime risk went to the
one-time validation of the reference analysis. The other half was spread over the rounds in shares
0.025·6/(π 2r2)for roundr, from 0.0152 in the first round to 0.00024 in the last. An update passed
validation when its bound, the bound of the reference analysis plus the largest paired increment
over the scenarios, was at most 0.05. Each round’s share was split across the 432 scenarios and
between the two paired bounds of each scenario, and one worst-case reference bound entered every
increment. The bounds of this validator are therefore larger than those of Algorithm A1 at the
same lifetime risk.
As Table A11 shows, the proposer opened with two valid updates, and both passed validation.
It then tried the two classical ways to a higher Type I error rate. In round 3 it proposed promoting
the sensitivity analysis whenever that analysis supports equivalence, and in round 4 it proposed
recovering information from the subjects who dropped out. Both failed validation, and an inde-
62

Table A11:The archived closed loop, round by round
Round Update Bound Validation Evaluated rate
1 dropout_route→completers 0.0474 passes 0.0392
2 qc_remediation→declared_mapping 0.0477 passes 0.0427
3 sensitivity_role→promote_if_supports 0.0626 fails 0.0564
4 dropout_route→information_recovery 0.0618 fails 0.0548
5 high_cv_escalate_above→0.5 0.0477 passes 0.0427
6 exclusion_threshold→3.0 0.0501 fails 0.0450
7 exclusion_threshold→3.5 0.0478 passes 0.0429
8 sensitivity_role→escalate_on_disagreement 0.0477 passes 0.0417
Each round changed one field of the configuration. The bound is the bound 0.04749 of the reference analysis plus
the largest paired increment over the 432 scenarios at the round’s share of the lifetime risk. An update passed
validation when its bound was at most 0.05. The evaluated rate is the largest Type I error rate over the same
scenarios in an independent simulation with 400,000 studies per scenario.
pendent evaluation on 400,000 newly simulated studies per scenario puts their worst Type I error
rates at 0.0564 and 0.0548. In round 6 the proposer asked to exclude outlying subjects from the
primary analysis. That update has an evaluated rate of 0.0450, below 0.05, but its bound came out
at 0.0501 and it failed validation. Failing a valid update is the error a conservative validator makes,
and it costs power, never validity. The proposer then moved to a milder exclusion cut, which passed
in round 7. It closed by adding a rule that defers when the sensitivity analysis disagrees with the
primary analysis (round 8).
Through the 5 updates that passed, the deferral rate fell from 0.643 for the starting version
to 0.119, and autonomous power rose from 0.255 to 0.566. Both were measured on a workload
of 90 scenarios with bioequivalent products, in which 15% of studies carry a data-quality flag.
Autonomous power is the share of these studies that the version itself declares bioequivalent. All
bounds of the updates that passed were at most 0.0478, and all deployed versions have evaluated
rates of at most 0.0429. The proposer’s deliberation over all rounds cost about $0.20, and the 8
validations took 25 seconds of computation.
Had the same sequence of updates been deployed with no validation, the evaluated rate of the
deployed version would have peaked at 0.0658. It would have stayed above 0.05 for 5 consecutive
versions, until the proposer happened to replace the harmful sensitivity rule in round 8.
The protocol was then rerun for 25 further trajectories that differed only in the proposer’s
own sampling randomness. Of 200 planned rounds, 191 produced an update that reached the
validator, and 0 updates failed the typed interface. In 7 rounds the proposer declared that no
further change would help, which closed its trajectory and canceled any rounds left in it. The
independent evaluation places 47 of the 191 updates above 0.05, about one in four, and every one
of them failed validation. A further 14 updates whose evaluated rate lies below 0.05 also failed.
The 33 distinct versions that passed have evaluated rates of at most 0.0450.
Per trajectory, the median number of updates that passed was 5 (range 3 to 6). The median
final deferral rate was 0.115 (range 0.076 to 0.223), and the median final autonomous power was
0.569 (range 0.541 to 0.580). The original trajectory, run before the replication, is typical of them.
A greedy optimizer then played the adversary that Theorem A11 allows. In each round it
simulated all single-field changes on its own pilot studies and submitted the one with the highest
estimatedpower, comingbacktofaileddirectionslater. Over12roundsittriedinformationrecovery
and sensitivity promotion twice each. It also tried exclusion cuts, which it relaxed after each failure
63

until one passed. It collected 8 failures, and its 4 versions that passed have bounds of at most
0.0478. Its final version, with power 0.579 and deferral rate 0.076, matches the benign trajectories.
Searching for the edge of validation bought the adversary nothing.
A10.2 Valid analyses do not compose
By Theorem A2, an analyst who reports whichever ofKexact level-αanalyses rejects can reach a
Type I error rate ofmin(1,Kα), and this constant is attained. Table A12 checks both parts with
2,000,000 simulated replicates per row. Independent analyses give1−(1−α)K, and analyses built
to have disjoint rejection regions attainKα. Each simulated value lies within Monte Carlo error of
its theoretical value, with a largest deviation of5.4×10−4.
Table A12:Selecting amongKexact analyses after seeing the data
Independent analyses Disjoint rejection regions
KSimulated1−(1−α) K Simulatedmin(1,Kα)
2 0.09757 0.09750 0.09999 0.10000
3 0.14253 0.14263 0.14992 0.15000
4 0.18523 0.18549 0.19985 0.20000
5 0.22659 0.22622 0.25054 0.25000
8 0.33657 0.33658 0.39973 0.40000
10 0.40141 0.40126 0.50029 0.50000
Type I error rate of an analyst who reports whichever ofKexact level-0.05analyses rejects, with 2,000,000
simulated replicates per row.
The construction with disjoint rejection regions is extreme, so the same question was put to two
analyses that a bioequivalence statistician would defend. The two one-sided tests [4] are exactly
levelαat the equivalence boundary. The distribution-free procedure of Hauschke and colleagues
[19] builds on the Hodges-Lehmann interval for the shift between the period differences of the two
sequences. This procedure is conservative because its rank statistic is discrete. Nine scenarios at
the boundary cross 24, 36 or 48 subjects with within-subject coefficients of variation of 20, 25 or
30%. With 400,000 simulated studies per scenario, the largest estimated rates of the two analyses
are 0.0504 and 0.0486, and the first lies within Monte Carlo error ofα.
An analyst who reports the parametric result and falls back on the distribution-free one when
the parametric analysis fails reaches 0.0587, about 17% above the nominal level. The two analyses
are strongly dependent, which keeps the inflation moderate. A moderate inflation is exactly what
a check of each analysis on its own misses. A fallback analysis is also the kind of update an analyst
making itself more robust would propose, which is why every version is validated as a whole.
A10.3 A regulatory switching rule
For highly variable drugs the FDA scales the equivalence limits with the reference product’s within-
subject standard deviationσwR [20]. Its mixed procedure chooses its criterion from the observed
swR, and the switching value 0.2936 corresponds to a within-subject coefficient of variation of 30%.
At or above the switching value, the procedure applies the scaled criterionµ2−k 2σ2 wR≤0, with
the regulatory constantk= log(1.25)/0.25 = 0.8926. This criterion is tested through the upper
confidence bound of Hyslop and colleagues [21], together with a constraint on the point estimate.
Below the switching value the procedure applies the usual criterion|µ|<log 1.25. The switch
64

chooses between two analyses after the data are seen. It is the situation of Theorem A2, built into
a rule in regulatory use.
The size of a switching rule depends on which configurations count as not bioequivalent, and
this study uses the convention that the switch itself defines. A product whose trueσwR is at most
0.2936 is not bioequivalent when|µ|≥log 1.25, and a product whose trueσ wR exceeds 0.2936 is
not bioequivalent when|µ|≥kσ wR. Each criterion is thus judged where the rule intends to apply
it. The Type I error rate is computed on the boundary of this null set, atµ= log 1.25below the
switching value and atµ=kσwR above it. The computation assumes equal within-subject standard
deviations for test and reference. All numbers reported in this section refer to this convention.
Under this convention the rule rejects far more often than the nominal 0.05 just below the
switching value. The design is a balanced four-period full replicate (TRTR/RTRT) with 24, 36 or
48 subjects. The Type I error rate was computed at the 23 valuesσwR = 0.16,0.18,...,0.60, with
200,000 simulated studies per value. The largest rates on this grid are 0.1036 for 24 subjects, 0.1141
for 36 and 0.1204 for 48, each atσwR = 0.28, the last grid value below the switching value. At 48
subjects the rule rejects 2.4 times as often as the nominal 0.05. The rate climbs steeply asσwR
approaches the switching value from below and falls under 0.05 just above it. These grid maxima
are therefore lower bounds, up to Monte Carlo error, on the largest rate over the null boundary.
The mechanism is a selection effect just below the switching value, where the product lies in the
null of the fixed criterion. Its observedswR nevertheless crosses the switching value often enough
that the wider scaled limits are applied to a product that the fixed limits would not approve.
Under this convention the inflation grows with the number of subjects, because more subjects raise
the power of the scaled test whenever the switch is taken. Studies of reference-scaled rules have
reported inflation of the same kind [9, 8, 10]. A rule in regulatory use thus shows the failure that
continual validation prevents, with no language model involved. Each branch is valid on its own,
and the composed procedure is not.
A10.4 The validity reserve
A simulation can show that a Type I error rate lies below the target, never that it equals the
target. A procedure that is exactly levelαon the null boundary therefore cannot be validated at
α(Proposition A7). This study measured the reserve that validation needs, on a null grid of 252
scenarios with 100,000 simulated studies each. The scenarios cross both equivalence boundaries,
seven within-subject coefficients of variation from 15 to 50% and 24, 36 or 48 subjects. They
also cross balanced or 60/40 allocation with dropout of 0, 10 or 20%. The two one-sided tests
atα= 0.05have a largest estimated rate of 0.05159. Their largest Clopper and Pearson bound,
simultaneous over the scenarios at confidence 0.95 through a Sidak split [2, 22], is 0.05411, so the
test fails validation. Run at level 0.0452, a reserve of 0.0048, the same test has a largest bound of
0.04933 and passes.
The reserve is the smallest value, in steps of 0.0002, at which a test would pass the simultaneous
validation with probability 0.90 if every scenario had the Type I error rate0.05−γ. It shrinks
roughly likem −1/2 as the numbermof simulated studies per scenario grows, from 0.0066 at
m= 50,000to 0.0016 atm= 10 6. Its cost in power is modest, 1.27 percentage points on average
and 2.88 at most. The mean and the maximum are taken over 18 scenarios with true ratios from
0.90 to 1.00, coefficients of variation of 20 or 30% and 24 to 48 subjects. For the same confidence,
the intersection-union test of Theorem A6 needs no division of the level among the scenarios, which
shrinks each bound and the needed reserve with it.
65

A10.5 Language models as analysts
An earlier experiment asked how language models use analytic freedom when they act as the
analyst. Each model received completed bioequivalence studies whose true formulation difference
lay at the equivalence boundary, so that declaring bioequivalence is a false rejection. Each study
came with the results of two individually valid analyses, a primary and a backup. Charters, the
written instructions that define the analyst’s role, differed only in the freedom they granted. They
ranged from a locked charter that fixes the primary analysis to one that names no primary analysis,
with a variant that adds pressure from the sponsor. The same studies were presented under each
charter, and studies in which the two analyses disagree, the decisive studies, were oversampled.
The mid-tier model, claude-sonnet-5, analyzed 550 studies per charter, 300 of them decisive. In a
later wave the smallest and the largest model, claude-haiku-4-5 and claude-opus-5, analyzed 250
studies under each charter of Table A13, 200 of them decisive.
Table A13:Deferrals to a human on decisive studies, by model and charter
Charter claude-haiku-4-5 claude-sonnet-5 claude-opus-5
Locked 5/200 0/300 1/200
Expert discretion 78/200 65/300 0/200
Sponsor pressure 99/200 42/300 2/200
No primary named 35/200 241/300 198/200
A decisive study is one in which the primary and the backup analysis disagree. The advisory charter was run at full
size for claude-sonnet-5 only and is omitted. Pooled over all charters, a failed primary analysis was replaced by its
passing backup in 1 of 402 presentations for claude-haiku-4-5. The corresponding counts are 0 of 750 for
claude-sonnet-5 and 0 of 402 for claude-opus-5. Each denominator counts the presentations in which the primary
failed and the backup passed.
Deferral to a human depended strongly on the model (Table A13). No model deferred on a
study in which the two analyses agreed. All three models rarely or never replaced a failed primary
analysis by its passing backup (table notes). On the decisive studies, however, the three models
parted ways. Under the charter that names no primary analysis, the smallest model deferred on 35
of 200 decisive studies. The mid-tier model deferred on 241 of 300, and the largest model on 198
of 200. Under sponsor pressure the order reversed, and the smallest model deferred most often.
Deferral never raises the Type I error rate (Proposition A20), so all three models erred toward
safety, each in its own way and to its own degree under identical instructions. A guarantee that
rested on such behavior would have to be established again for every model and every update. Con-
tinual validation checks what the deployed version is able to do, so the guarantee holds whichever
model chooses among the allowed paths (Proposition A19). A model swap that keeps those paths
therefore needs no new validation (Table A3).
A10.6 Checks of the analysis code
The analysis code was checked against published reference results for two-period and replicate
designs. Schütz and colleagues published reference datasets for 8 two-period bioequivalence studies
together with the results of EquivTest/PK, SAS, WinNonlin and R [23]. Our implementation
reproduces every point estimate and 90% confidence limit on all of them to the two decimals
reported, with no discrepancy (Table A14). The datasets include an imbalanced one (C) and a
large imbalanced one with outliers (H), on which a further package in that study disagreed.
For replicate designs, a fixed-effects implementation of the EMA’s Method A [24] reproduces
66

the published point estimate and 90% interval of the EMA reference dataset. It gives a within-
reference coefficient of variation of 46.96% against the published 47.0%. On a second replicate
reference dataset [12, 11] it gives a point estimate of 151.29% against the published 151.3%.
Table A14:The analysis code on published two-period reference datasets
Dataset Subjects This implementation Published
A 18 95.09 (90.76, 99.62) 95.09 (90.76, 99.62)
B 18 71.10 (51.45, 98.26) 71.10 (51.45, 98.26)
C 13 58.56 (39.41, 87.03) 58.56 (39.41, 87.03)
D 18 71.10 (51.45, 98.26) 71.10 (51.45, 98.26)
E 18 91.83 (55.71, 151.37) 91.83 (55.71, 151.37)
F 100 99.89 (93.37, 106.86) 99.89 (93.37, 106.86)
G 1000 92.15 (88.46, 95.99) 92.15 (88.46, 95.99)
H 717 93.42 (86.81, 100.55) 93.42 (86.81, 100.55)
Point estimate and 90% confidence interval of the ratio of test to reference, in percent. Published values are those
reported by Schütz and colleagues [23].
A11 Reproducibility and software
The code and the construction of the null scenarios built from real studies will be deposited in a
public repository upon publication [25]. The repository will also hold the validation results and
the outputs behind every number. Every figure is drawn by code from the outputs of the same
programs.
Software
The computations of Fig. A1 use Python 3.9 with NumPy 2.0 and SciPy 1.13. The supplementary
studies of sections A9 and A10 were run with Python 3.12 and NumPy 2.5. Rerun with Python 3.9
and NumPy 2.0, the study of section A10.2 reproduces its archived outputs exactly. The examples
of sections A7 and A8 run on vectorized reimplementations of the experimental bioequivalence
agent and of gbstats at commitb71bbbcunder Python 3.11 with NumPy 1.26, SciPy 1.13 and
CuPy 13.6. Fig. 1 is an editable PowerPoint slide written by a Python script with python-pptx
and exported to PDF by Microsoft PowerPoint, and Figs. 2 and 3, like the data panels of Fig. A1,
are drawn with matplotlib 3.9 in the Helvetica typeface of the captions. Exact one-sided Clopper
and Pearson bounds are computed from quantiles of the beta distribution.
Randomness
Every simulation is reproducible from recorded random seeds, and the simulated studies of a vali-
dation round are drawn after its version is frozen.
Data
The ten bioequivalence studies are distributed with the R package replicateBE [11] under the GNU
General Public License, version 3, and were first published in the sources it lists [24, 26, 27, 28, 29,
30, 31]. The EMA datasets may be reproduced with acknowledgment of the source, and the FDA
67

files are works of the United States Government. The five datasets of section A7.4 that validation
never uses, numbers 7, 8, 22, 25 and 28, ship with the same package and were simulated by its
authors. Section A10.6 uses the reference datasets for 8 two-period bioequivalence studies published
by Schütz and colleagues [23] and the replicateBE datasets 1 and 26.
Language models
Both examples use Claude Sonnet 5.5 (claude-sonnet-5-5) as proposer, sampled at temperature 1.
The supplementary studies used claude-sonnet-5, claude-haiku-4-5 and claude-opus-5 with fixed
instructions. All raw responses of the models are kept with the code, so every analysis of them
reruns without access to the models.
Appendix References
[1] European Medicines Agency, Guideline on the investigation of bioequivalence, (Committee for
Medicinal Products for Human Use), Guideline CPMP/EWP/QWP/1401/98 Rev. 1 (2010).
[2] C. J. Clopper, E. S. Pearson, The use of confidence or fiducial limits illustrated in the case of
the binomial.Biometrika26, 404–413 (1934).
[3] R. L. Berger, Multiparameter hypothesis testing and acceptance sampling.Technometrics24,
295–300 (1982).
[4] D. J. Schuirmann, A comparison of the two one-sided tests procedure and the power approach
for assessing the equivalence of average bioavailability.Journal of Pharmacokinetics and Bio-
pharmaceutics15, 657–680 (1987).
[5] D. P. Foster, R. A. Stine,α-investing: A procedure for sequential control of expected false
discoveries.J. R. Stat. Soc. Series B Stat. Methodol.70, 429–444 (2008).
[6] J. Tian, A. Ramdas, Online control of the familywise error rate.Statistical Methods in Medical
Research30, 976–993 (2021).
[7] International Council for Harmonisation, ICH M13A guideline on bioequivalence for
immediate-release solid oral dosage forms, (ICH), Harmonised guideline (2024).
[8] D. Labes, H. Schütz, Inflation of type I error in the evaluation of scaled average bioequivalence,
and a method for its control.Pharmaceutical Research33, 2805–2814 (2016).
[9] M. Wonnemann, C. Frömke, A. Koch, Inflation of the type I error: Investigations on regulatory
recommendations for bioequivalence of highly variable drugs.Pharmaceutical Research32,
135–143 (2015).
[10] J. Muñoz, D. Alcaide, J. Ocaña, Consumer’s risk in the EMA and FDA regulatory approaches
for bioequivalence in highly variable drugs.Stat. Med.35, 1933–1943 (2016).
[11] H. Schütz, M. Tomashevskiy, D. Labes, replicateBE: Average bioequivalence with expanding
limits (ABEL) (R package version 1.1.3, CRAN) (2022).https://doi.org/10.32614/CRAN.
package.replicateBE(accessed 6 October 2026).
[12] H. Schütz, et al., Reference datasets for studies in a replicate design intended for average
bioequivalence with expanding limits.AAPS J.22, 44 (2020).
68

[13] B. Sengupta, Self-evolving agents with anytime-valid certificates.arXiv [Preprint](2026).
https://arxiv.org/abs/2607.00871(accessed 6 October 2026).
[14] X. Sun, Y. Zeng, Z. She, X. Wang, Which self-improvements should we trust? Reliable self-
improvement when agents reuse their benchmarks.arXiv [Preprint](2026).https://arxiv.
org/abs/2609.33180(accessed 6 October 2026).
[15] A. N. Angelopoulos, S. Bates, E. J. Candès, M. I. Jordan, L. Lei, Learn then test: Calibrating
predictive algorithms to achieve risk control.The Annals of Applied Statistics19(2025).
[16] GrowthBook, Inc., GrowthBook: Open source feature flags, experimentation, and product
analytics (GitHub repository, statistics engine gbstats under the MIT License) (2026).https:
//github.com/growthbook/growthbook(accessed 7 October 2026).
[17] A. Deng, Y. Xu, R. Kohavi, T. Walker, Improving the sensitivity of online controlled ex-
periments by utilizing pre-experiment data inProceedings of the Sixth ACM International
Conference on Web Search and Data Mining. pp. 123–132 (2013).
[18] P. C. O’Brien, T. R. Fleming, A multiple testing procedure for clinical trials.Biometrics35,
549–556 (1979).
[19] D. Hauschke, V. W. Steinijans, E. Diletti, A distribution-free procedure for the statistical
analysis of bioequivalence studies.International Journal of Clinical Pharmacology, Therapy
and Toxicology28, 72–78 (1990).
[20] U.S. Food and Drug Administration, Statistical approaches to establishing bioequivalence:
Guidance for industry, (Center for Drug Evaluation and Research), Final guidance (2026).
[21] T. Hyslop, F. Hsuan, D. J. Holder, A small sample confidence interval approach to assess
individual bioequivalence.Stat. Med.19, 2885–2897 (2000).
[22] Z. Šidák, Rectangular confidence regions for the means of multivariate normal distributions.
Journal of the American Statistical Association62, 626–633 (1967).
[23] H. Schütz, D. Labes, A. Fuglsang, Reference datasets for 2-treatment, 2-sequence, 2-period
bioequivalence studies.AAPS J.16, 1292–1297 (2014).
[24] European Medicines Agency, Questions & answers: Positions on specific questions ad-
dressed to the Pharmacokinetics Working Party (PKWP) (EMA/618604/2008 Rev. 13,
Committee for Medicinal Products for Human Use) (2015).https://www.ema.europa.
eu/en/documents/scientific-guideline/questions-answers-positions-specific-
questions-addressed-pharmacokinetics-working-party_en.pdf(accessed 6 October
2026).
[25] X. Sun, Y. Zeng, X. Wang, Reproducibility code and results for lifetime-valid decisions by con-
tinually evolving AI analysts (GitHub, 2026).https://github.com/xiaojing777/lifetime-
valid-ai-analysts(to be made public upon publication).
[26] U.S. Food and Drug Administration, Bioequivalence studies (Archived web page)
(2017).https://wayback.archive-it.org/7993/20171115165246/https://www.fda.gov/
Drugs/ScienceResearch/ucm301277.htm(archived 15 November 2017, accessed 6 October
2026).
69

[27] S. D. Patterson, B. Jones, Viewpoint: Observations on scaled average bioequivalence.Phar-
maceutical Statistics11, 1–7 (2012).
[28] R. C. Shumaker, C. M. Metzler, The phenytoin trial is a case study of “individual” bioequiv-
alence.Drug Information Journal32, 1063–1072 (1998).
[29] S.-C. Chow, J.-p. Liu,Design and Analysis of Bioavailability and Bioequivalence Studies.
(Chapman and Hall/CRC, Boca Raton, FL), Third edition, (2008).
[30] D. Hauschke, V. Steinijans, I. Pigeot,Bioequivalence Studies in Drug Development. (Wiley,
Chichester, UK), (2007).
[31] S. D. Patterson, B. Jones,Bioequivalence and Statistics in Clinical Pharmacology. (Chapman
and Hall/CRC, Boca Raton, FL), Second edition, (2017).
70
