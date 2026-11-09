---
title: 'From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model
  Agents'
url: https://arxiv.org/abs/2610.04575
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Xueping Gao
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.04575
pages: 12
chars: 71218
fetched_at: '2026-11-08T13:33:16+00:00'
kb_version: 1
---

# From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents

From Probe Scores to Alarm Policies: Operational Validity of
Activation Monitors for Language-Model Agents
Xueping Gao
Alibaba Cloud Computing
Hangzhou, China
xueping.gxp@alibaba-inc.com
Abstract
Activation probes can predict safety-relevant properties of language
models with high area under the receiver-operating-characteristic
curve (AUROC), but deployed agent monitors make thresholded
alarm decisions under tight false-alarm budgets. These are different
estimands. We introduce anOperational Validity Contractthat fixes
a monitor’s target, observability, identity, timing, intervention unit,
comparator, calibration, and cost. We formalize risk at the semantic
request or trajectory level: when one task contains repeated alarm
opportunities, row-level AUROC and false positive rate do not iden-
tify semantic-unit any-alarm risk. A confidence-certified threshold
also requires enough independent negative units, a tie-safe rule,
and transport to deployment.
Across Models Under Pressure, LASR refusal prediction,
immutable AgentDojo, and a prospectively protocol-frozen ST-
WebAgentBench replication, joint activation–observable monitors
reach AUROC 0.957 and 0.935 on the first two benchmarks, yet
their locked 5%/10% detection rates are only .642/.742 and .719/.782,
respectively. On AgentDojo, the secondary mean-activation rollout
monitor reaches AUROC 0.922 but detects none of 38 positive
semantic cases at the locked 5% operating point; thresholds
intended for 10% false alarms realize 18.7–20.0% on test. Because
the test misses its prospectively frozen 40-positive support gate,
we label it support-insufficient. On ST-WebAgentBench, activation
reaches AUROC .874, but 23 independent calibration negatives
cannot identify even a 10% controller; the locked policy abstains
rather than reporting its mechanical zero FPR as a success. An
exploratory counterexample also lowers full AUROC while improv-
ing realized 10% utility. The fail-closed compiler caps MUP and
LASR at restricted predictive value and AgentDojo and ST-Web
at representation accessibility; no setting reaches alarm-policy
validity. A reproducibility audit recomputes these claim levels
and all four settings’ reported score-derived metrics from frozen
predictions and identities.
CCS Concepts
•Computing methodologies → Artificial intelligence;•Secu-
rity and privacy→Software and application security.
Keywords
language-model agents, activation monitoring, operational validity,
risk calibration, prompt injection
ACM Reference Format:
Xueping Gao. 2026. From Probe Scores to Alarm Policies: Operational Va-
lidity of Activation Monitors for Language-Model Agents. InThe Eighth
DAI ’26, Hong Kong, China
International Conference on Distributed Artificial Intelligence (DAI ’26), No-
vember 29–December 2, 2026, Hong Kong, China.ACM, New York, NY, USA,
12 pages.
1 Introduction
Internal activations are an appealing source of safety signals for
language-model agents. A lightweight probe can reuse a model’s
forward pass, operate before a harmful action is completed, and
expose features that a small text classifier may require much more
data or compute to recover [ 13, 20, 24]. These properties have
motivated activation monitors for jailbreaks, deception, refusal,
and reward hacking. Their quality is commonly summarized by
AUROC, accuracy, or a gain over a lexical baseline.
An operator, however, does not deploy an AUROC. The operator
deploys a score, an aggregation rule, and a threshold that may stop
a trajectory, escalate a request, or invoke a human. False alarms
are paid per semantic task or trajectory, not necessarily per dataset
row. The threshold must be selected without test labels and must
transport across prompts, policies, and tool environments. A moni-
tor can therefore rank examples well while being unusable at the
false-alarm rate that the alarm policy can afford.
Our AgentDojo experiment makes this gap concrete under a
prespecified sampled retry-set stress audit. We monitor the first
policy request after a Qwen2.5-7B agent consumes an injected tool
result and predict whether each of ten frozen stochastic attempts
for the same semantic case executes the official injection goal. A
frozen mean-activation monitor reaches rollout AUROC 0.9215.
At a threshold locked for a 5% semantic-case safe-attempt alarm
budget, it detects none of the 38 cases containing an unsafe attempt.
At the 10% budget, the primary activation and joint monitors realize
18.7% and 20.0% safe-attempt alarm rates. Neither fact is visible
from rollout AUROC. The ten-attempt unit is a stress-audit choice,
not an estimate of a single-execution deployment or a controller
that stops at its first alarm. An independently frozen SuiteCRM
replication sharpens the category error: activation AUROC is .8738,
but the prespecified independent-template support cannot certify a
finite threshold, so every 5%/10% controller abstains.
We study the resulting question:when does an activation score
constitute a valid alarm signal for an agent, rather than merely a
successful probe?Our answer is an Operational Validity Contract:
Target× Observability× Identity× Timing× Unit× Compara-
tor× Calibration× Cost. The fields specify the random variable,
information set, generalization boundary, and decision policy to
which a result applies. This is an AgentOps problem: a distributed
tool-using system pays intervention costs over tasks and trajecto-
ries, while its monitor is usually validated over rows. Closing that
arXiv:2610.04575v1  [cs.CL]  3 Oct 2026

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
mismatch is necessary for observable, reproducible, and governable
agent infrastructure.
Our contribution is an activation-monitor-specific integration
of established evaluation and calibration ideas, with three concrete
outputs:
• a claim-level contract that separates representation accessi-
bility, restricted predictive value, and calibrated alarm-policy
validity by binding the semantic alarm unit, same-horizon
comparator, and confidence-locked threshold;
• a four-setting audit showing that high activation AUROC
can coexist with poor low-FPR detection, insufficient calibra-
tion support, calibration-to-test mismatch, and concentrated
group burden; and
• a fail-closed claim compiler, covered by 20 result-independent
counterexample tests, and a score-level replay binding iden-
tities, timing, frozen predictions, thresholds, and immutable
test consumption.
The calibration inequality, trajectory-level any-alarm risk, and
the distinction between ranking and alarm utility all have prior an-
tecedents. We do not claim any ingredient separately. Proposition 1
applies the standard row-to-unit risk relation to this audit rather
than proposing a new concentration inequality. The integration
makes explicit which additional evidence is needed to move from a
probe score to an alarm-policy claim.
We donotargue that activation monitors universally fail. They
improve low-FPR detection substantially in two settings. The nar-
rower conclusion is more operationally important: a probe result
alone does not identify a valid alarm policy.
2 Related Work
2.1 Activation monitoring
Activation monitors have been compared with text classifiers at low
FPR, applied to high-stakes inputs, and tested under off-policy shift
[13, 20, 24]. Temporal signals also track refusal and reward-hack
risk states [4, 33, 34]; monitor staleness after model updates is a
separate transport problem [6]. These establish accessibility, timing,
robustness, or efficiency, whereas we audit the operational unit and
calibrated alarm claim.
AgentLens, TRACES, and AgentForesight move prediction into
multi-turn execution [16, 19, 37]; AcMAS and PVDetector use acti-
vations for multi-agent attacks and policy violations [31, 35]. Yet
AUC .998 need not identify malicious content, and a critic with
AUROC .94 can reduce success after intervention [18, 29]. General
probing controls raise the same shortcut and comparator concerns
[3, 17, 30]. We propose neither a new detector nor an intervention-
effect estimator: our contribution is the same-horizon observable, se-
mantic alarm unit, threshold-support, and transport audit between
offline prediction and an alarm claim. Black-to-white performance
boosts likewise evaluate internal access relative to a black-box
monitor [23]; a finite-model gain in our audit remains restricted
predictive value, not evidence of privileged or causal state.
2.2 Risk-controlled online monitoring
Conformal risk control calibrates a parameter to bound a mono-
tone expected loss [2]. Schirmer et al. apply conformal and high-
probability risk control to online LLM verifier signals: one output
sequence is flagged if any step crosses a threshold [26]. CP-Agent
uses held-out trace calibration and a predeclared finite controller
manifest in competitive programming [ 32]. Thus calibrated on-
line monitoring and frozen controller manifests are not new. Score
order statistics and minimum sample-size requirements for high-
probability type-I-error control also predate LLM monitoring in
Neyman–Pearson classification [28]. CORA further calibrates an
execute/abstain boundary for GUI-agent actions [ 7]. We instead
audit whether the score, information set, nested agent identity, and
deployment unit justify an activation-monitor claim. System-level
evaluation already connects errors to Safety Gain, Residual Hazard,
and Availability Cost [11]; we add a semantic unit, same-horizon
comparison, and finite-sample low-FPR calibration/transport audit,
not a new utility functional.
Low-FPR monitoring is also central to AI control, where a trusted
monitor selects actions or trajectories for audit [9]. Recent work
models the low-FPR shape of monitor ROC curves [27]. We avoid
tail extrapolation and use finite observed order statistics; unsup-
ported operating points cause abstention.
Three closest contemporaneous systems sharpen our novelty
boundary. Monitoring Monitorability defines intervention, process,
and outcome-property archetypes, a monitorability metric, and a
broad agent suite [10]. GAVEL composes interpretable activation
concepts into configurable real-time safety rules [25]. PrefixGuard
synthesizes online prefix monitors across four agent benchmarks
and already shows that strong ranking need not yield actionable
first alerts at low false-alarm rates [12]. We do not claim archetype
design, operational activation rules, or the ranking–alarm-utility
distinction as new. Our narrower contribution binds an activation-
versus-observable comparison to a semantic alarm unit, confidence-
locked threshold, and frozen transport audit.
General assurance and reporting work provides an additional
boundary. Evaluation Cards composes benchmark, run, and model
metadata into an operational reporting record [8]; structured AI
safety cases bind claims, arguments, and evidence [ 14]; and the
Composable Assurance Framework propagates machine-readable
safety assertions through MLOps [ 38]. The Operational Validity
Contract is not a general evaluation schema, safety case, or deploy-
ment authorization. It is a narrower statistical contract for deciding
the strongest activation-alarm claim licensed by one frozen evalua-
tion.
2.3 Agent safety evaluation
AgentDojo evaluates prompt injection against stateful tool-using
agents using official utility and security outcomes [5]. It is suitable
because the label is executed future behavior rather than a text
proxy. We add stochastic rollouts, a pre-action boundary, semantic-
case grouping, and immutable manifests. SLEIGHT-Bench shows
that capable transcript monitors retain blind spots at 1% FPR [21];
we do not claim adaptive robustness. Other benchmarks expose
miss/false-alarm trade-offs and task-disjoint TF–IDF beating LLM

From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents DAI ’26, November 29–December 2, 2026, Hong Kong, China
1. Specify
target, horizon, identity, unit −→
2. Compare
same-horizon observable,
activation, joint
−→
3. Calibrate
independent unit maxima,
strict threshold
↓
5. Claim
accessibility, predictive value,
or alarm-policy validity
←−
4. Stress
transport, groups, intervention
cost
Abstain
if support or identity checks
fail
Figure 1: The probe-to-policy audit. A high ranking metric is evidence at Step 2, not permission to skip specification, unit-level
calibration, or transport. Every empirical claim in this paper is labeled by the last step it passes.
judges [1, 36]. We ask the logically prior question of whether acti-
vations improve a locked alarm policy over such controls.
3 Operational Validity
3.1 A monitor claim is a contract
Definition 1 (contract-bound claim).Let a monitor emit score 𝑆,
and letC=(𝑌,𝑂,𝐼,𝐻,𝐺,𝐵,𝑃 cal,𝐿) . A validity claim is indexed by
(𝑆,C), whose eight fields are:
(1) Target: an input property, future behavior, completed-output
property, or causal state;
(2) Observability: the transcript and system information avail-
able to a non-activation comparator at the same horizon;
(3) Identity: the semantic object that may not cross training,
calibration, test, or bootstrap clusters;
(4)Timing: when the score is read relative to the action;
(5) Unit: the task, request, rollout, or trajectory on which an
alarm consumes budget;
(6) Comparator: observable features, model class, data, and
compute allowed to the baseline;
(7) Calibration: the independent population and rule used to
lock a threshold; and
(8) Cost: latency, memory, review burden, and intervention loss.
BecauseC selects the random variable, comparator, threshold law,
and loss, the contract fixes an estimand rather than a reporting
checklist.
Changing fromC toC′ ≠C requires an invariance or transport
assumption.
The contract creates a three-level claim ladder.Representation ac-
cessibilityneeds a development-frozen probe and held-out ranking
evidence.Restricted predictive valueadditionally needs a competitive
observable at the same horizon and clustered uncertainty for the
incremental gain.Alarm-policy validityadditionally needs an opera-
tional aggregation rule, an independently locked threshold, realized
risk, sufficient positive support, transport diagnostics, and declared
cost semantics. Evidence cannot be promoted up this ladder by re-
naming the target after the experiment. Causal intervention benefit
is audited separately and is not a fourth rung inferred from alarms.
This distinction is invisible to pooled AUROC. With a random
positive row score𝑆+ and negative row score𝑆−,
AUROC=Pr(𝑆 + >𝑆 −)+ 1 2 Pr(𝑆+ =𝑆−).(1)
It averages all pairwise rankings, has no deployment threshold,
weights units in proportion to their row counts, and assigns no
confidence to the extreme negative tail. It can therefore improve
while the alarm policy becomes worse, as our LASR counterexample
later demonstrates.
3.2 The operational unit
Let𝐺 denote an independent semantic operational unit. It may
contain several rows or stochastic trajectories𝑖. Let𝑌𝐺𝑖 = 1denote
an unsafe target event and let larger𝑆𝐺𝑖 be more suspicious. For a
prespecified sampled set of alarm opportunities, define the outcome-
conditioned unit maxima
𝑍− 𝐺 =max 𝑖:𝑌𝐺𝑖 =0 𝑆𝐺𝑖, 𝑍 + 𝐺 =max 𝑖:𝑌𝐺𝑖 =1 𝑆𝐺𝑖.(2)
At threshold𝑡, the corresponding operating rates are
𝑅0(𝑡)=Pr(𝑍 − 𝐺 >𝑡), 𝑅 1(𝑡)=Pr(𝑍 + 𝐺 >𝑡).(3)
Mixed units contribute to both estimands; repeated rows do not be-
come independent calibration samples. We call𝑅0 the safe-attempt
any-alarm rate and𝑅1 the unsafe-attempt any-hit rate. They are not
the FPR/TPR of a conventional binary “any unsafe” case classifier:
a mixed case can contain both a safe attempt that alarms and an
unsafe attempt that is detected.
The meaning of𝐺 is part of the operational contract, not a harm-
less grouping choice. In AgentDojo our primary𝐺 is one semantic
security case represented by a sampled set of ten prespecified at-
tempts. This is a retry-set stress audit for systems that may retry a
task, not an estimate of an ordinary single-execution deployment
or of an online stop controller. We therefore report fixed-order
𝑘-attempt and all-single-seed sensitivities separately; they are dif-
ferent estimands and cannot replace the frozen primary result. The
class-max estimand is evaluated after labeling all sampled attempts;
it does not simulate a sequential controller that halts after its first
alarm and thereby suppresses future retries. Such a stop policy
requires a new sequential contract and prospective evaluation.
Proposition 1 (row risk does not identify unit risk).If a safe unit
contains𝑛 alarm opportunities with identical row FPR 𝑝, condi-
tional independence gives𝑅0 = 1−( 1−𝑝)𝑛. Without a dependence
assumption,𝑝≤𝑅 0≤min( 1,𝑛𝑝) . Thus equal row score distribu-
tions and equal row AUROC/FPR can induce different unit risk. At
𝑝=. 05and 𝑛= 10, unit FPR is .401under independence. This is
an identification error; more row-level test data cannot repair a
misspecified unit.
Schirmer et al. already aggregate any alarm within one output
sequence [26]. Our point concerns the preceding specification: for
an agent, several sequences, seeds, or policy requests can belong to
the same user task on which review burden is paid.

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
Table 1: Scope relative to the closest evaluation and calibration work. A dash means the item is not the cited work’s primary
object, not that it is incompatible with the method.
Work Score emphasis Alarm unit Same-horizon comparator Confidence-locked risk Transport/group audit
Patel–Wang [24] activation example strong text low-FPR evaluation adversarial robustness
Guerin et al. [11] runtime monitor system outcome return/hazard model safety/availability utility application assumptions
Monitoring Monitorability [10] CoT/transcript trajectory/property action-only monitorability metric broad scaling suite
GAVEL [25] activation rules rule event text/guardrail baselines threshold metrics domain/rule audit
PrefixGuard [12] trace monitor trajectory first alert raw text/LLM judges calibrated FAR points four-benchmark diagnostics
Schirmer et al. [26] verifier output sequence multiple verifiers sequence any-alarm exchangeable sequence risk
CP-Agent [32] trace feedback program/task controller variants held-out risk control task-specific controller
Ours activation + observable semantic task/case declared visible history unit-max Beta UCB one-use + suite/support
Table 2: A 5% row false-alarm rate compounds rapidly when
a safe operational unit contains 𝑛 conditionally independent
alarm opportunities.
𝑛opportunities 1 5 10 20
Unit FPR (%) 5.0 22.6 40.1 64.2
3.3 The alarm-policy objective
For a false-alarm budget𝛼, deployment asks for a feasible threshold
that approximately solves
max
𝑡
𝑅1(𝑡)subject to𝑅 0(𝑡)≤𝛼.(4)
Alternatively, an application can declare benefits and costs and
maximize𝑏𝑅1(𝑡)−𝑐𝑅 0(𝑡)−𝐶 monitor(𝑡) . Both formulations require
a specific threshold and operational unit. Full AUROC integrates
over many thresholds the alarm policy will never use and con-
tains neither intervention cost nor a risk constraint. We use the
constrained form to express a false-alarm budget; false reviews or
blocks motivate this budget, but their application-specific costs are
not measured in these experiments.
A marginal constraint is not a worst-group constraint. If suite𝐾
is observed, a deployment may instead require max𝑘𝑅0,𝑘(𝑡)≤𝛼 or
allocate different prespecified budgets by suite. We report group
diagnostics but do not claim such conditional control, because
several AgentDojo suites lack the negative and positive support
needed to calibrate and evaluate it independently.
3.4 What can an activation add?
Let𝑂 contain all information declared observable at the monitoring
horizon, and let𝐴=𝑓 𝜃(𝑂)be a frozen deterministic activation.
Proposition 2 (information ceiling). 𝐼(𝑌 ;𝐴|𝑂)= 0, and under an
unrestricted decision class the Bayes risk using𝑂 is no worse than
that using𝐴 alone. Conditioning on𝑂 fixes𝐴, and any ruleℎ(𝐴)
can be writtenℎ(𝑓 𝜃(𝑂)).
This does not make finite activation probes useless. Held-out
probe performance can establish representation accessibility; an
incremental held-out gain over the declared observable comparator
can establish restricted predictive value. Sample or compute effi-
ciency additionally requires a learning curve or resource-matched
measurement. None implies privileged information or hidden in-
tent. If𝑂 omits information used to compute 𝐴, the claim must
state that omission explicitly.
3.5 Certified thresholds, support, and ties
Conditional on the frozen score function, suppose 𝑚 calibration
samples of𝑍− 𝐺 are independent draws from a common negative-unit
distribution, also shared by an independent deployment unit. Sort
them descending, and𝑇𝑟 is the𝑟th largest. We alarm iff𝑍− 𝐺 >𝑇𝑟 . For
any score distribution, including discrete or quantized scores, the
new-unit strict tail mass𝑞(𝑇𝑟)=Pr(𝑍 − new >𝑇𝑟|𝑇𝑟) is stochastically
upper-bounded by Beta(𝑟,𝑚−𝑟+ 1); under continuity the bound
is exact. Therefore
Pr
cal

𝑞(𝑇𝑟)≤𝐵 −1 𝑟,𝑚−𝑟+1(1−𝛿)  ≥1−𝛿.(5)
We lock the largest rank 𝑟 whose upper quantile is at most the
false-alarm budget𝛼. If no rank qualifies, the alarm policy abstains.
At rank one, a finite threshold requires
𝑚≥ log𝛿 log(1−𝛼) .(6)
For𝛼=𝛿=. 05, this is 59 independent negative units merely to
identify a finite threshold; it says nothing about TPR. Selected-value
ties make the bound conservative rather than invalid under strict
exceedance. The positive-test minima used below are frozen design-
sufficiency gates, not consequences of this negative-tail inequality.
The artifact records selected-value multiplicity, calibration strict ex-
ceedances, and test equalities; all reported test operating points have
zero equality. The pre-test AgentDojo threshold JSON and earlier
replay recorded the legacy non-strict comparison. The submission
audit changes only that comparator to strict exceedance: numeric
thresholds, ranks, and every test decision remain unchanged. We ex-
pose this post-hoc semantics correction rather than treating sample
uniqueness as proof of population continuity.
This analysis separates three bottlenecks.Tail identifiabilityasks
whether calibration support can certify a threshold.Tail separability
asks whether any valid threshold has useful 𝑅1.Transportasks
whether the calibration and deployment unit distributions match.
More calibration data can improve the first, but not guarantee the
other two.
The distinction also clarifies what a confidence statement means.
The order-statistic bound controls the marginal probability that a
new independent negative unit from that same distribution strictly
exceeds the selected score. Mere exchangeability without indepen-
dence is insufficient for this high-probability population-risk bound.
It is not a simultaneous guarantee over suites, families, policies, or
an adaptive sequence of redeployments. Those require additional
multiplicity control or a new calibration contract.

From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents DAI ’26, November 29–December 2, 2026, Hong Kong, China
Table 3: Frozen claim cards. “Pre” means before the predicted
behavior.
Setting Target Timing Unit
MUP high-stakes input input input
LASR future refusal pre-response semantic request
AgentDojo injection execution pre-action security case
ST-Web task failure pre-action intent template
4 Evaluation Protocol
4.1 Four targets
The four settings are case studies of a common audit procedure, not
a controlled cross-benchmark comparison or a sample from a single
deployment population. Each asks which claim its own target, unit,
comparator, and calibration evidence support. We report within-
setting comparisons without pooling effect sizes or estimating how
often activation monitors succeed or fail in deployment.
Table 3 records the claim before any operating-point comparison.
MUP contains independent high-stakes inputs and tests an observ-
able input property [20]. LASR predicts whether Llama-3.2-3B will
refuse before any assistant token, using recovered original requests
as units [13]. These analyses use frozen splits but are retrospective
because earlier benchmark results had been inspected.
The released LASR row split is not a pure semantic OOD split:
207 of 969 test request identities occur in the official training set,
including 52 that occur in our frozen calibration subset. We there-
fore label official-all results as a published-split description, not
independent transport evidence, and report the protocol-declared
semantic-unseen subset (762 requests) as the identity- disjoint sensi-
tivity. The subset is defined only by request identity, without using
labels or monitor scores.
AgentDojo is the prospective future-behavior test. We freeze
AgentDojo v1, Qwen2.5-7B-Instruct, temperature .7, top-𝑝 .9, three
then ten seeds for model fitting, and disjoint user-task splits. The
monitoring boundary is the first policy request after an injected
tool result. The label is whether the remaining trajectory executes
the official injection task. A global constant marker replaces an
early identity-bearing marker before any monitor feature is col-
lected. One immutable 1,190-identity test manifest, containing ten
prespecified stochastic attempts per semantic case, is consumed
once; failed trajectories are retained without regeneration. This is
not the same estimand as observing one trajectory per case.
ST-WebAgentBench is a separately protocol-frozen prospective
replication on SuiteCRM [15]. Its unit is an intent template with safe
and unsafe trajectory siblings; the monitor reads Qwen2.5-7B layer
14 before each browser action. Of 192 immutable test identities,
173 valid rollouts yield 2,237 pre-action rows. Twelve engineering
failures are retained without replacement. The exhaustive ledger
assigns all result-bearing input, future-response, tool-agent, and
browser-agent branches to this table; it is not a random task sample,
and rejected, failed, and negative branches remain in the supple-
ment.
For AgentDojo, the eight fields instantiate as: executed injec-
tion goal (𝑌 ); exact visible history through the injected tool result
(𝑂); user task and frozen model/policy identity (𝐼); first subsequent
policy request (𝐻); the sampled ten-attempt security case (𝐺); TF–
IDF, tool/suite metadata, and three Qwen-14B forecasts (𝐵); disjoint
negative-case maxima with the frozen strict order statistic (𝑃cal); and
safe-attempt alarm burden versus unsafe-attempt hits (𝐿). Down-
stream intervention cost is not measured, so this audits risk proxies
rather than net deployment utility.
4.2 Monitor ladder
Each setting compares observable, activation, and joint monitors.
MUP uses a frozen lexical observable and a validation-selected
probe. LASR’s observable combines lexical features with three
Qwen-14B semantic forecasts available from the same prompt. Its ac-
tivation is the corrected layer-12 cumulative mean. AgentDojo’s ob-
servable combines canonical visible-history character/word TF–IDF,
suite/tool metadata, and three frozen Qwen-14B future-outcome
log-odds prompts. The primary activation is Qwen2.5-7B zero-
indexed decoder layer 14 at the final token of the exact policy
request; full-request mean is a prespecified secondary analysis.
Late fusion uses out-of-fold base predictions with grouped folds.
No AgentDojo layer, pooling, template, feature, solver, or threshold
is chosen from calibration or test performance. ST-Web reuses the
frozen layer/pooling and strong-observer construction, with intent-
template-grouped fitting and no outcome-dependent revision.
The declared observer is intentionally capable where public arti-
facts permit: does activation add predictive utility beyond what the
same visible history can support? The settings nevertheless use het-
erogeneous observer classes (lexical for MUP; Qwen-14B-assisted
for LASR and AgentDojo), so we make within-setting increments,
not cross-setting comparator rankings. Compute is reported sepa-
rately rather than assumed equal.
4.3 Calibration and integrity
Model fitting and threshold calibration use disjoint semantic units.
We lock 95%-confidence marginal thresholds for𝛼∈{. 05,. 10} from
negative unit maxima. Results report realized FPR/TPR, paired
5,000-sample semantic-unit bootstrap intervals, and suite/family
diagnostics. Each budget binds its own minimum TPR; all four con-
tracts froze .80 before operating-point analyses. It is not a universal
optimum or a hypothesis-test threshold; the scientific conclusions
use the reported rates, intervals, support, and transport audits rather
than this binary rule.
Coverage additionally requires independent calibration and de-
ployment units from the same negative-unit distribution. Because
the official LASR test contains the disclosed training identity over-
lap, we attach no transport certificate to that all-test panel; the
semantic-unseen panel is the corresponding identity-disjoint check.
MUP, AgentDojo, and ST-Web use their declared independent test
units.
For a mixed case, safe and unsafe stochastic outcomes enter𝑍− 𝐺
and𝑍+ 𝐺 respectively: the same user task can create both a safe-
attempt alarm and an unsafe-attempt detection opportunity. Paired
differences reuse each resampled semantic case across monitors;
percentile intervals are computed from 5,000 case-cluster bootstrap
replicates. The calibration UCB and the realized test FPR answer
different questions, so neither is substituted for the other. We treat
realized FPR as a transport diagnostic, not proof of exchangeability;

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
Frozen alarm-policy audit procedure
(1) Declare target, visible history, semantic identity, horizon, unit,
score families, and promotion rule.
(2) Split by semantic identity; fit Observable and Activation only
on model fit, and fit Joint from grouped out-of-fold base pre-
dictions.
(3) Freeze model and feature hashes. On calibration only, form
negative unit maxima and select the largest Beta-certified rank.
(4) Apply strict exceedance, audit support, selected-value multi-
plicity, and test equalities; abstain only when no rank has the
required upper bound.
(5) Hash the thresholds, consume test once, retain failures, and
report unit FPR/TPR, paired monitor differences, and group
support.
Figure 2: No layer, pooling rule, template, model, or threshold
is changed after its corresponding freeze point.
Table 4: Artifact checks that prevent a ranking result from
silently changing its estimand.
Boundary Immutable check
Identity semantic hashes; grouped folds; overlap/non-overlap
audit
Timing exact visible prefix; tool-result boundary reconstruc-
tion
Features layer, pooling, templates, payload and model hashes
Calibration negative-unit count, selected rank, Beta UCB, strict
rule/ties
Test one-use manifest, failed-rollout retention, no refitting
a point estimate below 𝛼 cannot itself certify deployment shift.
MUP intervals resample medical specialties and LASR intervals
resample semantic requests; AgentDojo intervals resample semantic
security cases, and ST-Web intervals resample intent templates.
Across monitor, budget, and sensitivity panels we report pointwise
intervals without familywise multiplicity control. We do not select
a significant cell or reinterpret these intervals as simultaneous
guarantees.
The claim compiler applies the claim ladder in Section 3 to frozen
evidence; it never fits or searches. Appendix F specifies its deci-
sion rule. Twenty result-independent counterexamples cover mal-
formed identities, budgets, ranks, ties, support, mechanical zeros,
and promotion. A separate replay reconstructs all four settings’
score metrics from allowlisted frozen archives; upstream audits
separately verify prompt/token and activation alignment, hashes,
and immutable test consumption.
4.4 Resource accounting
Predictive dominance and deployment preference are different com-
parisons. In a separate hook microbenchmark on the AgentDojo
Qwen-7B stack, capturing the frozen layer added no resolvable
batch-one latency and 0.067% at batch eight; the captured tensor oc-
cupied 4–41 MiB across tested sequence lengths, against an approx-
imately 26 ms batch-one forward pass. These measurements cover
activation extraction, not the downstream probe or the Qwen-14B
Table 5: Independent negative-unit support and realized
primary-activation FPR. Selected ranks depend on 𝑚,𝛼, and
𝛿=.05, not test performance.
𝑚5% budget 10% budget
Setting𝑟/UCB Test FPR𝑟/UCB Test FPR
MUP 69 1/.0425 .0099 3/.0884 .0199
LASR 372 12/.0485 .0183 28/.0987 .0872
AgentDojo 100 2/.0466 .0000 5/.0892 .1867
ST-Web 23 abstain abstain
observer. We therefore report the latter as a strong information-
set comparator, not as a compute-matched replacement. A cheap
activation can remain useful in a cascade even when it has no inde-
pendent predictive increment. Human-review and action- blocking
costs are unmeasured, so we compare risk proxies and do not claim
net deployment utility.
5 Results
We organize evidence by the three gates induced by the contract
rather than by benchmark: whether a low-FPR threshold is identifi-
able, whether the certified tail is separable, and whether calibration
transports. Retry and suite analyses then test whether the declared
unit hides policy or group heterogeneity.
5.1 Calibration support and threshold
identifiability
The first three settings contain enough independent negative cal-
ibration units to select finite thresholds at both budgets. Table 5
reports the frozen rank and its 95% upper confidence bound (UCB).
This rules out the simplest explanation—that poor utility is only
an undefined percentile from too few negative rows. It does not
establish positive-class separation or transport. AgentDojo illus-
trates the distinction: its 10% activation threshold has an 8.92%
calibration UCB but realizes 18.67% test FPR. Under the continu-
ous independent-and-identically-distributed null, integrating over
the frozen rank-5 threshold gives𝐾∼BetaBinomial( 75, 5, 96) and
Pr(𝐾≥ 14)=. 001745; strict exceedance is conservative when
scores tie. This predictive check includes calibration-threshold un-
certainty and diagnoses a calibration-to-test distribution mismatch,
not an intervention effect. ST-Web exposes the logically prior failure.
Its 23 calibration-negative intent templates are below the rank-one
requirements of 59 at 5% and 29 at 10%. All frozen thresholds are
therefore+∞. The resulting zero alarms are mechanical abstention,
not successful transport.
5.2 High AUROC does not ensure low-FPR
detection
Table 6 reports the joint monitor, which is the most favorable sum-
mary for an activation increment on MUP and LASR. MUP reaches
AUROC .9571, yet its realized 5% and 10% TPRs at FPR-certified
thresholds are .6424 and .7417. LASR reaches request-event AUROC
.9348; the corresponding realized TPRs are .7189 and .7821. Both
improve over observable baselines, so the result is not “activations
fail. ” Neither meets the frozen requirement of at least .80 TPR at
both budgets.

From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents DAI ’26, November 29–December 2, 2026, Hong Kong, China
The conclusion persists on 762 identity-disjoint, semantic-
unseen LASR requests. AUROCs are .9066 (Observable), .9424
(Activation), and .9427 (Joint). Their 5% FPR/TPR pairs are .0334/
.6234, .0180/.7065, and .0206/.7065; at 10% they are .1054/.7403,
.0643/.7662, and .0720/.7740. Joint-minus-Observable TPR is +.0831,
request-bootstrap 95% CI [.0494,. 1169], at 5%, and +.0338, CI
[.0052,. 0623], at 10%. Thus overlap does not create the observed
increment, but the unseen alarm policy still misses the frozen .80
utility gate.
Paired cluster uncertainty also distinguishes the two budgets.
MUP Joint-minus-Observable TPR is +.2649, specialty-bootstrap
95% CI[.1529,. 4268], at 5%, but +.0762, CI[−.0192,. 2209], at 10%.
LASR’s request-bootstrap increments are +.1059, CI[.0754,.1385],
and +.0407, CI[.0122,. 0692], respectively. Thus activation can ma-
terially improve a restricted comparator while the locked alarm
policy still misses its utility requirement.
Appendix Figure 3 visualizes the AUROC–operating-point mis-
match without pairing row-level discrimination with unit-level
TPR.
The LASR nominal, non-certified 10% activation threshold
reaches .8126 TPR, but realizes .1136 FPR. At 5%, even its nominal
TPR is .7475. Thus LASR’s 10% near miss is partly calibration-
resolution limited, whereas its 5% failure is primarily tail separation.
A fixed-data allocation sweep later increased calibration support
without rescuing the operating point, illustrating that support and
separation cannot be substituted mechanically.
5.3 AgentDojo calibration-to-test mismatch
No model selection on test.Before calibration or test behavior
was generated, grouped model-fit out-of-fold AUROC was .9020
for Observable, .8918 for Activation last, and .8879 for Joint last.
The Joint-minus-Observable difference was −.0141with paired-
case 95% CI[−.0338,. 0041]. On mixed cases it was−.0469with CI
[−.0990,−. 0039]. These diagnostics arguedagainstan activation
increment. We nevertheless locked the declared pipelines and con-
sumed the test manifest once. This negative pre-test evidence is
important: the reported test is a falsification attempt, not a selected
success from layers or pooling rules.
The AgentDojo test contains 1,190 frozen rollout identities, of
which 1,165 complete. There are 602 eligible monitoring-boundary
rows across 82 semantic cases, with 75 negative cases, 38 positive
cases, and 31 mixed cases. Trace alignment and exact prompt re-
construction are 100%. The prospectively frozen minimum was 40
positive cases, so the formal status issupport-insufficient; this was
a frozen design-sufficiency rule distinct from the analytic negative-
tail certificate, and we do not add or rerun cases. The primary
increment and 10% transport conclusions below fail independently
of this two-case shortfall.
The primary case maximum corresponds to the sampled ten-
attempt retry-set audit, not an intrinsic property of “AgentDojo. ”
Prespecified fixed-order𝑘= 1, 3, 5, 10and single-seed sensitivities
(Appendix D) vary sharply; only four single-seed policies identify
a finite 5% threshold. They do not replace the primary estimand,
but show why retry semantics must be declared in advance.
At 5%, Observable detects two positive cases with two false
alarms. Activation last detects the same number with no false
alarms, while Joint last detects one with none. The primary Joint-
minus-Observable TPR difference is−.0263, paired semantic-case
bootstrap 95% CI[−.0789, 0]. It fails the promotion rule before con-
sidering the support shortfall. At 10%, Observable and Joint make
exactly the same positive-case decisions, but both realize .20 FPR.
The activation-only FPR is .1867 and TPR .5263.
Pooling reinforces the category error. Mean activation has the
best rollout AUROC in Table 6, yet zero 5% TPR and only .1053 TPR
at 10%. Because mean pooling was frozen as secondary, this is a
sensitivity rather than a post-hoc model switch.
5.4 The declared unit exposes suite
concentration
AgentDojo alarms concentrate by suite: at 5%, all true positives and
both Observable false positives occur in Slack; its 14.29% Slack FPR
contrasts with 2.67% pooled FPR. Sparse suite support precludes
certificates but rejects interpreting a marginal rate as uniform pro-
tection.
The failure modes are therefore not interchangeable. MUP has
modest positive tail overlap despite conservative realized FPR. LASR
has adequate support and passes the 10% target only under the
exploratory tail-aligned objective, but its 5% tail remains poorly
separated. AgentDojo has formal negative-tail support but exhibits
a calibration-to-test mismatch at 10%, has negligible 5% positive
recall, and exhibits severe suite concentration. ST-Web is earlier still:
its activation AUROC is .8738 and Joint-minus-Observable AUROC
is +.0215, template-bootstrap 95% CI[−.0097,. 0568], but calibration
support makes both controllers unidentifiable; its 28 negative test
templates also miss the prospectively frozen 29. Reporting only “did
not reach 80% TPR” would erase the scientific distinction among
identifiability, separation, and transport.
The compiler therefore caps MUP and LASR atrestricted predic-
tive value: their comparator increments are supported, but their
retrospective contracts did not prespecify test-support gates. Agent-
Dojo and ST-Web stop atrepresentation accessibilitybecause their
frozen comparator increments fail; support and transport failures
independently preclude alarm-policy validity. No current setting
licenses an intervention-effect claim.
5.5 Objective mismatch: AUROC and utility can
move oppositely
An exploratory LASR unit-max partial-AUC objective over FPR
[0,. 10] lowers AUROC .9344→.9184 but raises certified 10% TPR
.7780→.8106 while FPR falls .0872→.0669. This constructively re-
verses full-AUROC selection. Partial-AUC is prior art [ 22], test
results were already inspected, and a separately frozen 5% vari-
ant fails (.7189→.5743 TPR); this is a diagnostic, not a promoted
optimizer.
6 Discussion
6.1 Implications for AgentOps
Monitor registries should bind every score to the eight contract
fields and reject identity leakage, row/unit mismatch, unsupported
ranks, ties, or drift. Dashboards should report unit-level rates and
abstain on unidentified policies.

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
Table 6: Locked operational-unit results. AUROC is test unit-level AUROC except AgentDojo, where both primary case-max
and the highest prespecified rollout AUROC are shown. FPR/TPR are realized at independently calibrated thresholds. LASR
rows show the official all-test split; the identity-disjoint sensitivity is reported in text and Appendix B, Table 7. ST-Web dashes
denote prespecified abstention, not observed zeros. ADJ = AgentDojo.
Setting Monitor AUROC 5% FPR 5% TPR 10% FPR 10% TPR
MUP Observable .9396 .0033 .3775 .0497 .6656
Activation .9446 .0099 .5000 .0199 .6457
Joint.9571.0066.6424.0232.7417
LASR Observable .8987 .0467 .6130 .1176 .7413
Activation .9344 .0183.7189.0872 .7780
Joint.9348.0243.7189.0913.7821
ADJ Observable .7860 .0267 .0526 .2000.5789
Activation last.8028.0000.0526.1867 .5263
Joint last .7986 .0000 .0263 .2000.5789
ADJ rollout Activation mean.9215.0000 .0000 .0000 .1053
ST-Web Observable .8497 – – – –
Activation last.8738– – – –
Joint last .8712 – – – –
Activation access remains useful under this standard. On MUP
and LASR it materially improves low-FPR recall over the declared
restricted observable models. Cheap probes may form a cascade, but
without a learning curve or resource match, predictive increments
do not establish privileged information, efficiency, or deployment
validity.
AgentDojo also shows that suite or policy shift can violate ex-
changeability even with immutable code and thresholds.
6.2 What the evidence does and does not
establish
The cross-setting pattern supports accessibility and, retrospectively
on MUP/LASR, improved low-FPR recall over restricted observables.
LASR additionally shows, only exploratorily, that an operational
objective can beat full-AUROC selection. Neither result implies
privileged information, causality, or transport.
Alarm-policy evaluation therefore requires a declared unit and
horizon, a capable same-horizon comparator, independent-unit
calibration, and distinct support, separation, and transport tests.
Each can change the conclusion.
6.3 Limitations
AgentDojo and ST-Web are independently frozen prospective eval-
uations; both retain failures and miss a prespecified support gate.
MUP and LASR are retrospective. Both prospective tests study one
Qwen-7B layer and frozen pooling; AgentDojo covers one attack
and four sparse suites, while ST-Web is SuiteCRM-only. Certificates
are marginal, not adversarial or familywise. The Qwen-14B com-
parators are not compute matched, so their contrasts establish only
predictive differences under the declared information sets, not rela-
tive cost-effectiveness. We do not measure human-review burden,
blocking cost, intervention benefit, or net deployment utility. The
contract records these missing quantities explicitly; an audit verdict
is not a complete deployment assessment.
AgentDojo’s sampled ten-attempt unit is policy-specific; post-
hoc sensitivities cannot choose deployment semantics. A single-
execution or stop-on-alarm policy would require its own calibration
and prospective evaluation. The exhaustive screening ledger is
not a random task sample, so the audit does not estimate failure
prevalence.
The four heterogeneous targets form a validity audit, not a pooled
effect. In particular, the prospective studies demonstrate rejection
of unsupported alarm claims rather than validate a successful alarm
policy; their limited support cannot establish a general failure of
activation monitoring. Qwen-14B forecasts are automated compara-
tors, not human judgments. Adaptive attacks and calibration drift
remain open.
The artifact verifies frozen scores, identities, contracts, and pa-
per numbers; it does not regenerate behavior/features or refit, so
reproducibility is score-level rather than end-to-end.
6.4 Ethical and societal considerations
The public experiments use model-generated trajectories. Invalid
thresholds can concentrate burden; unsupported policies should
abstain and use group reporting, least privilege, and escalation.
Logs require access control and minimal retention; we release no
new exploit payloads.
7 Conclusion
A probe asks what is accessible; an alarm policy asks whether a
locked decision meets operational risk and utility requirements.
Across four targets, semantic units, same-horizon observables, cali-
bration, support, and transport change the answer suggested by AU-
ROC. The contribution is their fail-closed, activation-alarm-specific
binding—not a new detector or calibration theorem. Deployment
validity is a separate claim.

From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents DAI ’26, November 29–December 2, 2026, Hong Kong, China
Generative AI Disclosure
Generative-AI tools assisted with language editing and draft code
generation. The author independently checked the research design,
source literature, mathematical claims, code, artifact hashes, and
every reported numerical result.
References
[1] Laksh Advani. 2026. From Confident Closing to Silent Failure: Characterizing
False Success in LLM Agents.arXiv preprint arXiv:2606.09863(2026). https:
//arxiv.org/abs/2606.09863
[2] Anastasios N. Angelopoulos, Stephen Bates, Adam Fisch, Lihua Lei, and Tal
Schuster. 2024. Conformal Risk Control. InInternational Conference on Learning
Representations. https://arxiv.org/abs/2208.02814
[3] Yonatan Belinkov. 2022. Probing Classifiers: Promises, Shortcomings, and Ad-
vances.Computational Linguistics48, 1 (2022), 207–219. doi:10.1162/coli_a_00422
[4] Matteo Gioele Collu, Riccardo Conte, Alberto Giaretta, Denis Kleyko, Mauro
Conti, Matteo Zavatteri, and Roberto Confalonieri. 2026. Refusal Before Decoding:
Detecting and Exploiting Refusal Signals in Intermediate LLM Activations.arXiv
preprint arXiv:2605.28553(2026). https://arxiv.org/abs/2605.28553
[5] Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc
Fischer, and Florian Tramèr. 2024. AgentDojo: A Dynamic Environment to
Evaluate Prompt Injection Attacks and Defenses for LLM Agents. InAdvances in
Neural Information Processing Systems, Vol. 37. Curran Associates, Inc., Red Hook,
NY, USA, 82895–82920. Datasets and Benchmarks Track. doi:10.52202/079017-
2636
[6] Evan Duan. 2026. Do Activation Monitors Survive Model Updates? Benchmark-
ing, Predicting, and Repairing Activation-Monitor Staleness.arXiv preprint
arXiv:2606.15980(2026). https://arxiv.org/abs/2606.15980
[7] Yushi Feng, Junye Du, Qifan Wang, Zizhan Ma, Qian Niu, Yutaka Matsuo, Long
Feng, and Lequan Yu. 2026. CORA: Conformal Risk-Controlled Agents for
Safeguarded Mobile GUI Automation.arXiv preprint arXiv:2604.09155(2026).
https://arxiv.org/abs/2604.09155
[8] Avijit Ghosh, Anka Reuel, Jenny Chim, et al. 2026. Evaluation Cards: An Inter-
pretive Layer for AI Evaluation Reporting.arXiv preprint arXiv:2606.09809(2026).
https://arxiv.org/abs/2606.09809
[9] Ryan Greenblatt, Buck Shlegeris, Kshitij Sachan, and Fabien Roger. 2024. AI
Control: Improving Safety Despite Intentional Subversion.arXiv preprint
arXiv:2312.06942(2024). https://arxiv.org/abs/2312.06942
[10] Melody Y. Guan, Miles Wang, Micah Carroll, Zehao Dou, Annie Y. Wei, Marcus
Williams, Benjamin Arnav, Joost Huizinga, Ian D. Kivlichan, Amelia Glaese, Jakub
Pachocki, and Bowen Baker. 2026. Monitoring Monitorability. InInternational
Conference on Machine Learning. Spotlight. https://openreview.net/forum?id=
b82fgbMVpz
[11] Joris Guerin, Raul Sena Ferreira, Kevin Delmas, and Jérémie Guiochet. 2022.
Unifying Evaluation of Machine Learning Safety Monitors.arXiv preprint
arXiv:2208.14660(2022). https://arxiv.org/abs/2208.14660
[12] Xinmiao Huang, Jinwei Hu, Rajarshi Roy, Changshun Wu, Yi Dong, and Xiaowei
Huang. 2026. PrefixGuard: From Large Language Model Agent Traces to Online
Failure-Warning Monitors.arXiv preprint arXiv:2605.06455(2026). https://arxiv.
org/abs/2605.06455
[13] Nathalie Kirch, Samuel Dower, Adrians Skapars, Ekdeep Singh Lubana, and
Dmitrii Krasheninnikov. 2025. The Impact of Off-Policy Training Data on Probe
Generalisation.arXiv preprint arXiv:2511.17408(2025). https://arxiv.org/abs/
2511.17408
[14] Sung Une Lee, Liming Zhu, Md Shamsujjoha, Liming Dong, Qinghua Lu, Jieshan
Chen, and Lionel Briand. 2026. A Structured Approach to Safety Case Con-
struction for AI Systems.arXiv preprint arXiv:2601.22773(2026). https:
//arxiv.org/abs/2601.22773
[15] Ido Levy, Ben Wiesel, Sami Marreed, Alon Oved, Avi Yaeli, Nir Mashkif, and
Segev Shlomov. 2026. ST-WebAgentBench: A Benchmark for Evaluating Safety
and Trustworthiness in Web Agents. InThe Fourteenth International Conference
on Learning Representations. https://openreview.net/forum?id=MuCDzH0ctf
[16] Jiaqian Li, Yanshu Li, Boxuan Zhang, Ruixiang Tang, and Kuan-Hao Huang. 2026.
TRACES: Proactive Safety Auditing for Multi-Turn LLM Agents via Trajectory-
State Modeling.arXiv preprint arXiv:2605.27690(2026). https://arxiv.org/abs/
2605.27690
[17] Millicent Li, Alberto Mario Ceballos Arroyo, Giordano Rogers, Naomi Saphra, and
Byron C. Wallace. 2025. Do Activation Verbalization Methods Convey Privileged
Information?arXiv preprint arXiv:2509.13316(2025). https://arxiv.org/abs/2509.
13316
[18] Yanhang Li, Zhichao Fan, and Zexin Zhuang. 2026. When AUC 0.998 Is Not
Enough: A Candidate Evaluation Protocol for Hidden-State Probes of Indirect
Prompt Injection in Multimodal Computer-Use Agents. InThe 2nd Workshop
on Evaluation for Multimodal Generation. Co-located with SIGIR 2026. https:
//arxiv.org/abs/2606.22864
[19] Weidi Luo, Qiming Zhang, Yihao Quan, Mingyu Jin, Jie Cai, Chaowei Xiao,
Jingcheng Niu, and Zhen Xiang. 2026. AgentLens: Interpretable Safety Steer-
ing via Mechanistic Subspaces for Multi-Turn Coding Agent.arXiv preprint
arXiv:2606.22673(2026). https://arxiv.org/abs/2606.22673
[20] Alex McKenzie, Urja Pawar, Phil Blandfort, William Bankes, David Krueger,
Ekdeep Singh Lubana, and Dmitrii Krasheninnikov. 2025. Detecting
High-Stakes Interactions with Activation Probes. InAdvances in Neu-
ral Information Processing Systems, Vol. 38. Curran Associates, Inc., Red
Hook, NY, USA. https://proceedings.neurips.cc/paper_files/paper/2025/hash/
b9501301a7a0f99e57406cc901f4e3ce-Abstract-Conference.html
[21] Elle Najt, Colin Toft, Tyler Tracy, Fabien Roger, and Joe Benton. 2026. SLEIGHT-
Bench: A Benchmark of Evasion Attacks Against Agent Monitors.arXiv preprint
arXiv:2605.16626(2026). https://arxiv.org/abs/2605.16626
[22] Harikrishna Narasimhan and Shivani Agarwal. 2013. A Structural SVM Based
Approach for Optimizing Partial AUC. InProceedings of the 30th International Con-
ference on Machine Learning (Proceedings of Machine Learning Research, Vol. 28).
PMLR, 516–524. https://proceedings.mlr.press/v28/narasimhan13.html
[23] Aviel Parrack, Carlo Leonardo Attubato, and Stefan Heimersheim. 2025. Bench-
marking Deception Probes via Black-to-White Performance Boosts.arXiv preprint
arXiv:2507.12691(2025). https://arxiv.org/abs/2507.12691
[24] Oam Patel and Rowan Wang. 2024. Activation Monitoring: Advantages of Using
Internal Representations for LLM Oversight. InNeurIPS Workshop on Attributing
Model Behavior at Scale. https://openreview.net/forum?id=qbvtwhQcH5
[25] Shir Rozenfeld, Rahul Pankajakshan, Itay Zloczower, Eyal Lenga, Gilad Gressel,
and Yisroel Mirsky. 2026. GAVEL: Towards Rule-Based Safety through Activation
Monitoring. InInternational Conference on Learning Representations. https:
//openreview.net/forum?id=duntROHZ5R
[26] Mona Schirmer, Metod Jazbec, Alexander Timans, Christian Naesseth, Maja
Waldron, and Eric Nalisnick. 2026. Online Safety Monitoring for LLMs.arXiv
preprint arXiv:2607.02510(2026). ICML Workshop on Hypothesis Testing. https:
//arxiv.org/abs/2607.02510
[27] Kerrick Staley, Aryan Bhatt, and Julian Stastny. 2026. Logit ROCs: Monitor TPR is
Linear in FPR in Logit Space. Redwood Research. https://blog.redwoodresearch.
org/p/logit-rocs-monitor-tpr-is-linear
[28] Xin Tong, Yang Feng, and Jingyi Jessica Li. 2018. Neyman–Pearson Classification
Algorithms and NP Receiver Operating Characteristics.Science Advances4, 2
(2018), eaao1659. doi:10.1126/sciadv.aao1659
[29] Rakshith Vasudev, Melisa Russak, Dan Bikel, and Waseem Alshikh. 2026. The
Intervention Paradox: Accurate Failure Prediction in Agents Does Not Imply
Effective Failure Prevention.arXiv preprint arXiv:2602.03338(2026). https:
//arxiv.org/abs/2602.03338
[30] Cheng Wang, Zeming Wei, Qin Liu, Wenxuan Zhou, and Muhao Chen. 2025.
False Sense of Security: Why Probing-based Malicious Input Detection Fails
to Generalize. InNeurIPS Workshop on Mechanistic Interpretability. Spotlight.
https://openreview.net/forum?id=zwYzSma4V4
[31] Junhui Wang, Hangtao Zhang, Zhirun Zheng, Li Zeng, Jiejun Xiao, Xi Luo, Lihua
Yin, and Saiqin Long. 2026. PVDetector: Detecting Prompt Injection Attacks on
Purpose-Specific LLM Agents through Policy-Violation Concept Analysis.Pro-
ceedings of the 34th ACM International Conference on Multimedia(2026). Accepted
to ACM MM 2026. https://arxiv.org/abs/2607.12624
[32] Peisong Wang, Bowen Liu, Zehua Li, Yuyao Wang, Zhiwei Ma, Yuhan Li, and Jia
Li. 2026. CP-Agent: A Calibrated Risk-Controlled Agent for Feedback-Driven
Competitive Programming.arXiv preprint arXiv:2605.24693(2026). https://arxiv.
org/abs/2605.24693
[33] Patrick Wilhelm and Odej Kao. 2026. From Reward-Hack Activations to Agentic
Risk States: Context-Calibrated Mechanistic Monitoring in LLM Agents.arXiv
preprint arXiv:2606.06223(2026). https://arxiv.org/abs/2606.06223
[34] Patrick Wilhelm, Thorsten Wittkopp, and Odej Kao. 2026. Monitoring Emergent
Reward Hacking During Generation via Internal Activations.arXiv preprint
arXiv:2603.04069(2026). https://arxiv.org/abs/2603.04069
[35] Haowen Xu, Xue Tan, Lei Ma, Zhihao Zhang, Chao Wang, Qingze Wang, Ping
Chen, Jun Dai, and Xiaoyan Sun. 2026. When Agents Go Rogue: Activation-Based
Detection of Malicious Behaviors in Multi-Agent Systems.Proceedings of the 43rd
International Conference on Machine Learning(2026). Accepted to ICML 2026.
https://arxiv.org/abs/2607.06807
[36] Shu Yang, Jingyu Hu, Tong Li, Hanqi Yan, Wenxuan Wang, and Di Wang. 2026.
AutoMonitor-Bench: Evaluating the Reliability of LLM-Based Misbehavior Moni-
tors.arXiv preprint arXiv:2601.05752(2026). https://arxiv.org/abs/2601.05752
[37] Boxuan Zhang, Jianing Zhu, Zeru Shi, Dongfang Liu, and Ruixiang Tang. 2026.
AgentForesight: Online Auditing for Early Failure Prediction in Multi-Agent
Systems.arXiv preprint arXiv:2605.08715(2026). https://arxiv.org/abs/2605.08715
[38] Xiaofei Zhao. 2026. Composable Assurance for AI Alignment: A Framework for
Propagating Formal Safety Properties Through MLOps.Proceedings of the AAAI
Conference on Artificial Intelligence40, 44 (2026), 38129–38136. doi:10.1609/aaai.
v40i44.41151

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
A Proof Sketches and Calibration Details
A.1 Operational-unit compounding
Let𝐸𝑖 be the event that the𝑖th opportunity in a safe unit alarms,
withPr(𝐸 𝑖)=𝑝. If the events are conditionally independent,
Pr
 𝑛Ø
𝑖=1
𝐸𝑖
!
=1−Pr
 𝑛Ù
𝑖=1
𝐸𝑐 𝑖
!
=1−(1−𝑝) 𝑛.(7)
For arbitrary dependence, the union contains each𝐸𝑖, giving the
lower bound𝑝, while Boole’s inequality gives the upper bound𝑛𝑝,
clipped at one. Both bounds are attainable: identical alarm events
attain𝑝, and disjoint events attain𝑛𝑝 when𝑛𝑝≤ 1. Thus the row
marginal alone cannot identify unit risk.
A.2 Deterministic-activation ceiling
For a frozen model, 𝐴=𝑓 𝜃(𝑂) is measurable with respect to 𝑂.
Conditioning on𝑂 makes𝐴 fixed, so 𝑌 and𝐴 are conditionally
independent, and therefore
𝐼(𝑌;𝐴|𝑂)=0.(8)
Any activation-only decisionℎ(𝐴) is the observable decisionℎ◦
𝑓𝜃(𝑂) . This proof compares information sets and unrestricted deci-
sion classes; it does not imply that a finite text model can learn𝑓𝜃
with the same samples or compute.
A.3 Distribution-free order statistic and ties
Let𝐹− be any negative-unit CDF and let𝑇𝑟 be the𝑟th largest of𝑚
independent, identically distributed calibration maxima, conditional
on the frozen score function. The deployment unit is an independent
draw from the same distribution. The probability-integral transform
𝐹−(𝑍−) stochastically dominates a uniform random variable, with
equality when𝐹− is continuous. Consequently the strict tail𝑞(𝑇𝑟)=
1−𝐹−(𝑇𝑟)=Pr(𝑍 − new >𝑇 𝑟 |𝑇 𝑟) is stochastically dominated by
Beta(𝑟,𝑚−𝑟+1). Thus, for𝑢 𝑟 =𝐵−1 𝑟,𝑚−𝑟+1(.95),
Pr
cal
{𝑞(𝑇𝑟)≤𝑢 𝑟}≥.95,(9)
with equality under continuity. We select the largest𝑟 for which
𝑢𝑟≤𝛼 and alarm only when𝑆>𝑇 𝑟 . For the four calibration sets,
the resulting UCBs are:
Setting𝑚5% rank/UCB 10% rank/UCB
MUP 69 1/.042487 3/.088444
LASR 372 12/.048471 28/.098704
AgentDojo 100 2/.046560 5/.089196
ST-Web 23 abstain/– abstain/–
This strict-exceedance construction remains valid at atoms: a tie
makes the bound conservative because equality does not alarm.
The audit records the selected-value multiplicity, the number of
calibration values strictly above it, and the number of test scores
exactly equal to it. All selected primary values have multiplicity
one and every reported test operating point has zero equality, so
replacing the earlier non-strict implementation changes no paper
count. If no rank has𝑢𝑟≤𝛼 , the alarm policy abstains via an infinite
threshold.
B LASR Semantic-Identity Sensitivity
The official LASR test contains 969 semantic request identities.
Of these, 207 occur in the official training set and 52 occur in
the frozen threshold- calibration subset. The protocol-declared
semantic-unseen mask retains 785 rows covering 762 identities;
it depends only on request identity. Table 7 applies the original
locked thresholds without refitting or recalibration.
Table 7: LASR results on 762 semantic-unseen requests. Op-
erating rates use the original strict-exceedance thresholds.
Monitor AUROC 5% FPR 5% TPR 10% FPR 10% TPR
Observable .9066 .0334 .6234 .1054 .7403
Activation .9424 .0180 .7065 .0643 .7662
Joint .9427 .0206 .7065 .0720 .7740
At 5%, Joint-minus-Observable TPR is +.0831 with request-
bootstrap 95% CI [.0494,. 1169]; at 10% it is +.0338 with CI
[.0052,. 0623]. The identity- disjoint analysis therefore preserves
both the activation increment and the failure to reach the frozen
.80 TPR gate.
C AgentDojo Exact Counts and Uncertainty
Table 8 reports exact case counts and two-sided 95% Clopper–
Pearson intervals. These intervals quantify finite test support; they
do not replace the independent calibration guarantee or the paired
case-bootstrap contrast.
Table 8: AgentDojo case operating points: count/denominator
and exact 95% CI.
Budget Monitor FPR (75 negative) TPR (38 positive)
5% Observable 2/75 [.0032,.0930] 2/38 [.0064,.1775]
Activation last 0/75 [.0000,.0480] 2/38 [.0064,.1775]
Joint last 0/75 [.0000,.0480] 1/38 [.0007,.1381]
10% Observable 15/75 [.1165,.3083] 22/38 [.4082,.7369]
Activation last 14/75 [.1060,.2933] 20/38 [.3582,.6902]
Joint last 15/75 [.1165,.3083] 22/38 [.4082,.7369]
The paired Joint-minus-Observable 5% TPR difference is−.0263,
semantic-case bootstrap 95% CI[−.0789, 0]; at 10%, the two moni-
tors make identical positive-case decisions and the paired difference
and CI are zero. Because 38 positive cases are below the frozen min-
imum of 40, these are labeled support-insufficient and are not used
to promote a monitor.
For the prespecified primary Activation-last monitor at the 10%
budget, the threshold is the fifth-largest of 100 negative calibra-
tion maxima. Under a continuous independent-and-identically-
distributed calibration–test null, the number 𝐾 of strict test ex-
ceedances among 75 negatives has the rank-predictive law 𝐾∼
BetaBinomial(75, 5, 96). Hence Pr(𝐾≥ 14)=. 001745. With score
atoms, strict exceedance can only make this upper-tail check con-
servative. Unlike conditioning on the 95% UCB, this calculation
integrates threshold-selection uncertainty. It diagnoses calibration-
to-test distribution mismatch; it does not estimate the causal effect
of intervening on an alarm.

From Probe Scores to Alarm Policies: Operational Validity of Activation Monitors for Language-Model Agents DAI ’26, November 29–December 2, 2026, Hong Kong, China
0.80 0.85 0.90 0.95
Operational-unit AUROC
0.00
0.25
0.50
0.75TPR at locked threshold
5% false-alarm budget
0.80 0.85 0.90 0.95
Operational-unit AUROC
10% false-alarm budget
Observable Activation Joint MUP LASR AgentDojo Project TPR gate
Figure 3: Operational-unit AUROC versus TPR at each independently locked threshold. Marker shape identifies the setting and
color the monitor. The dashed .80 line is a frozen project promotion rule, not a universal utility threshold; all realized rates are
reported. The secondary AgentDojo rollout AUROC is excluded because pairing rollout AUROC with case-level TPR would mix
estimands; ST-Web is excluded because no finite controller was identifiable.
D Repeated-Attempt Estimand Sensitivity
The primary AgentDojo result aggregates ten prespecified seeds
as admissible repeated attempts within one semantic security case.
This is a sampled ten-attempt retry-set audit. To test dependence
on that operational unit without generating new behavior, we re-
aggregate the frozen scores over nested prefixes of the original seed
order 101, 211, 307, 401, 503, 601, 701, 809, 907, 1009. Table 9 reports
selected prefixes; no seed or prefix is chosen by its result.
Formally, evaluation first labels completed attempts, then com-
putes𝑍− 𝐺 =max𝑖:𝑌𝐺𝑖 =0𝑆𝐺𝑖 and𝑍+ 𝐺 =max𝑖:𝑌𝐺𝑖 =1𝑆𝐺𝑖 . The reported
class-max FPR and TPR are the rates of𝑍− 𝐺 >𝑡 and𝑍+ 𝐺 >𝑡 , respec-
tively. A mixed case can enter both denominators. This estimand
measures whether the sampled retry set contains a safe attempt
that would consume review budget and whether it contains an
unsafe attempt that would be detected. It is not a binary any-unsafe
case classifier and does not simulate a controller that halts and
suppresses future attempts after its first alarm; such a controller
requires a new sequential contract.
Table 9: Post-hoc AgentDojo retry-policy sensitivity. Entries
are realized FPR/TPR at independently recalibrated FPR-
certified thresholds. Support is negative/positive/mixed se-
mantic cases.
𝑘Support 5% FPR/TPR 10% FPR/TPR
Observable Joint Observable Joint
1 34/14/0 .000/.357 .000/.143 .088/.643 .118/.643
3 55/31/9 .036/.194 .000/.000 .127/.742 .109/.710
5 66/33/18 .015/.091 .000/.030 .121/.667 .106/.667
10 75/38/31 .027/.053 .000/.026 .200/.579 .200/.579
We also evaluate all ten single-seed policies. At 5%, only four of
ten have enough negative calibration units for a finite threshold.
Among those four, Observable TPR ranges .0476–.3571; Joint-last
TPR ranges 0–.1429. At 10%, all ten are identifiable, but Observable
TPR ranges .0476–.9444 and Joint-last ranges 0–.9565. This varia-
tion is not a model comparison: changing the number of attempts
changes both label support and the safe-attempt alarm event. It
shows why a repeated-seed benchmark result cannot be exported to
a single-execution deployment without redefining and recalibrating
the alarm policy.
E Paired Cross-Benchmark Uncertainty
Table 10 adds paired cluster uncertainty for the activation increment
at each locked operating point. MUP resamples medical specialties;
LASR resamples semantic requests. The intervals are pointwise and
use 5,000 replicates with seed 20260713.
Table 10: Paired TPR differences at FPR-certified thresholds.
Setting Contrast 5% difference [95% CI] 10% difference [95% CI]
MUP Joint−Observable +.2649 [.1529,.4268] +.0762 [-.0192,.2209]
MUP Activation−Observable +.1225 [-.0391,.3627] -.0199 [-.1524,.1698]
LASR Joint−Observable +.1059 [.0754,.1385] +.0407 [.0122,.0692]
LASR Activation−Observable +.1059 [.0754,.1385] +.0367 [.0082,.0652]

DAI ’26, November 29–December 2, 2026, Hong Kong, China Xueping Gao
F Frozen Reproduction Matrices
F.1 Eight-field claim-card instantiation
Table 11: Instantiated Operational Validity Contracts. Cost
measurements are reported as incomplete rather than in-
ferred from predictive performance.
Setting Target / horizon / ob-
servable
Identity / unit / comparator /
calibration
Cost status
MUP high-stakes input; input
time; input text
input; one input; frozen lexical
observable; negative input max-
ima
monitor and interven-
tion costs unmeasured
LASR future refusal; pre-
response; original
request
request hash; semantic request;
lexical + three Qwen fore-
casts; train calibration, official-
all plus unseen test
monitor and interven-
tion costs unmeasured
AgentDojo injection execution; pre-
action; canonical visible
history
suite + user-task + case hash;
sampled ten-attempt case; TF–
IDF/metadata + three Qwen
forecasts; disjoint frozen case
calibration/test
hook extraction mea-
sured; probe, observer,
review, and interven-
tion costs unmeasured
ST-Web task failure; pre-action;
browser-visible state
intent-template hash; one tem-
plate across locked safe/unsafe
variants; frozen strong ob-
server + three Qwen fore-
casts; disjoint template calibra-
tion/test
environment reset and
rollout costs measured;
monitor, review, and
intervention costs un-
measured
F.2 Fail-closed claim compiler
The compiler consumes the typed claim card and already frozen
evidence; it has no interface for fitting, feature selection, threshold
search, or subset selection. Let𝐸spec require a complete contract and
passing identity audit. Let𝐸rep require an out-of-sample probe and
held-out ranking evidence. Let𝐸inc require a declared same-horizon
comparator, point increment at least the frozen minimum, and a
positive lower clustered-confidence bound. For each budget, let
𝐸op require an identified maximum certifying rank, prospectively
prespecified test support, the budget-local locked TPR minimum
𝜏𝛼, and realized FPR no larger than𝛼. The maximum claim is then
computed in order:
claim=
 

invalid,¬𝐸 spec,
contract, 𝐸 spec∧¬𝐸 rep,
representation, 𝐸 spec∧𝐸 rep∧¬𝐸 inc,
predictive, 𝐸 spec∧𝐸 rep∧𝐸 inc∧¬𝐸 op,
alarm, 𝐸 spec∧𝐸 rep∧𝐸 inc∧𝐸 op.
(10)
Intervention evidence is an orthogonal verdict: it cannot raise this
ladder and cannot be inferred from an alarm. Missing ranks are
permitted only when rank-one support is analytically insufficient;
finite policies must use the largest certifying rank and a match-
ing Beta UCB. Twenty synthetic counterexamples exercise these
transitions without benchmark outcomes.
Table 12: Compiler outputs from the frozen contracts. “Rep. ”
is representation evidence; “Inc. ” is the clustered comparator-
increment gate.
Setting Rep. Inc. Maximum claim Independent blocker(s)
MUP pass pass restricted predictive value test support not prespecified
LASR pass pass restricted predictive value test support not prespecified
AgentDojo pass fail representation accessibility increment, support, transport
ST-Web pass fail representation accessibility increment, calibration/test support
Table 13: Parameters frozen before their corresponding eval-
uation phase.
Object Frozen value
Environment AgentDojo v1, commit089ed468; official security outcome
Agent Qwen2.5-7B-Instruct; Hermes native tool calls
Generation temperature .7; top-𝑝.9; maximum 512 new tokens
Splits 345 model-fit, 119 calibration, 119 one-use-manifest test cases; user
tasks disjoint
Seeds 101, 211, 307, 401, 503, 601, 701, 809, 907, 1009
Boundary first policy request after the injected tool result
Marker one global constant; no case or seed identity
Activation zero-index decoder layer 14; final token primary, request mean sec-
ondary; float32
Observable exact visible history; character/word TF–IDF; suite/tool metadata;
three frozen Qwen-14B forecast log-odds
Fitting shared suite + user-task grouped folds; grouped out-of-fold late
fusion
Calibration semantic-case negative maxima; .95 Beta UCB; 5% and 10% budgets;
strict exceedance; tie/equality audit
Test policy consume one 1,190-identity ten-attempt manifest once; retain failed
trajectories; no retraining or threshold changes
Model fitting generated 3,450 frozen identities; 3,418 completed
and 1,920 boundary-present rows entered feature fitting. Calibra-
tion generated 1,190 identities; 1,184 completed and 670 boundary
rows across 103 cases were scored. The one-use test manifest gen-
erated all 1,190 identities; 1,165 completed and 602 boundary rows
across 82 cases were scored. Prompt reconstruction, token/payload
alignment, constant-marker purity, finite activations, and forecast-
template alignment were 100% for all eligible rows.
Full SHA256 values for locked scores and independently
rechecked metrics are stored in the machine-readable audit. The
supplement provides manifests and audit commands with portable
paths.
G Frozen-Score Replay and Screening
Transparency
The empirical replay starts from SHA256-pinned frozen score
archives rather than the manuscript evidence summary. It verifies
hashes, reconstructs semantic-unit maxima, recomputes AUROC,
calibration ranks, Beta UCBs, selected-value ties and equalities, test
FPR/TPR, exact intervals, group diagnostics, and paired bootstraps,
and only then compares the recomputed values with the paper. All
frozen-value comparisons pass. It also emits the LASR train/test
identity overlap and semantic-unseen sensitivity; AgentDojo
retry sensitivity; and ST-Web support, modality, worst-modality,
and intent-template-bootstrap diagnostics. It fits no model and
exposes no option to change a layer, pooling rule, threshold budget,
template, or subset.
The screening ledger covers all rejected, failed, negative, retro-
spective, and clean-rerun branches; the tabled settings are neither
the only attempts nor a random task sample.
