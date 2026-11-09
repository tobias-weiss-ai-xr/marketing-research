---
title: 'Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps'
url: https://arxiv.org/abs/2610.02740
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Jiaxin Zhang
- Xiangyu Peng
- Qinglin Chen
- Yu Li
- Hiroaki Hayashi
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.02740
pages: 38
chars: 124048
fetched_at: '2026-11-08T13:31:26+00:00'
kb_version: 1
---

# Prospective Hindsight: Self-Calibrating Reinforcement Learning via Prediction-Reality Gaps

Prospective Hindsight: Self-Calibrating Reinforcement
Learning via Prediction–Reality Gaps
Jiaxin Zhang∗, Xiangyu Peng, Qinglin Chen, Yu Li, Hiroaki Hayashi, Chien-Sheng Wu
Salesforce AI Research
Abstract
Reinforcement learning for long-horizon agents relies onpurely retrospectivetrain-
ing signals: credit is assigned only after observing environmental consequences,
leaving the agent’s belief at action time invisible to the gradient. We introduce
Prospective Hindsight (PH), a self-calibrating training principle that augments
any retrospective base method with a signal derived from the gap between the
agent’sprospective prediction(before feedback) and theretrospective evaluation
(after feedback). This per-rolloutsurpriseidentifies samples where the agent’s
self-model is most inaccurate and amplifies their gradient contribution through a
stop-gradient surprise-weighted advantage. Since the prospective predictor shares
parameters with the policy, the two co-evolve, progressively shifting focus to the
agent’s remaining blind spots. We connect this principle to a privileged-information
gap and show that minimizing the surprise residual provides a descent pathway
on the agent’s miscalibration rate; calibration thus emerges as a byproduct of
optimization rather than from an added objective. On single-turn verifiable tasks
and a multi-turn personal-agent task (under GRPO, on-policy distillation, and their
combination), PH improves both task performance and calibration, with consis-
tent gains across model scales. Notably, the dominant miscalibration mode shifts
structurally between regimes, overconfident failures in single-turn, underconfident
successes in multi-turn, yet the same training principle addresses both successfully.
Figure 1: Prospective Hindsight (PH) converts hindsight feedback into a self-calibrating training
signal. PH compares an agent’s action-time prediction with the realized verifier/PRM outcome,
partitions rollouts into calibrated and miscalibrated cases, and upweights surprising prediction–reality
mismatches during policy updating within GRPO, on-policy distillation and their combination.
∗Correspondence to{jiaxin.zhang, wu.jason}@salesforce.com
Preprint.
arXiv:2610.02740v1  [cs.LG]  2 Oct 2026

1 Introduction
LLMs increasingly act asagents: decomposing tasks, calling tools, writing code, conducting extended
tutoring conversations, and making intermediate commitments whose consequences unfold over
many steps [42, 3]. In these settings, the most damaging failures are often not simple mistakes, but
mistakes made with confidence [52, 46, 55, 51]. A confidently wrong agent continues down a flawed
trajectory, ignores opportunities for recovery, and triggers incorrect downstream actions; an agent
that fails while expressing uncertainty [47, 28], in contrast, invites a fallback, a retry, or a request for
human input. Reliable agentic learning therefore requires more than improving final accuracy — it
requires aligning the agent’s prospective belief about its own success with the reality of its outcomes.
The hindsight trap.Modern agentic RL has converged on increasingly richretrospectivefeedback
[45, 7]. Process reward models score each step by inspecting the next environmental state [42, 3];
on-policy distillation (OPD) methods [25, 37] construct a hindsight teacher conditioned on post-action
context unavailable to the agent at decision time [1, 44, 14, 34]. These methods differ in mechanism
but share a structural property: every learning signal is computed from quantities observedafterthe
agent has acted, and the agent’s prospective belief at action time, i.e., what it expected would happen,
never enters the gradient. Two rollouts that produced the same outcome therefore receive the same
update, regardless of whether one was a confident success and the other a lucky guess, or whether one
was a failure the agent could have anticipated and the other a failure that took the agent by surprise.
We call this structural obstruction thehindsight trap, and it is the reason why retrospective training
reliably improves task accuracy without resolving overconfidence [50, 21, 5, 16, 11].
Calibration as a training signal, not a diagnostic.A substantial literature on LLM calibration has
measured this overconfidence and proposed inference-time fixes: verbalized confidence prompts,
semantic uncertainty estimators, post-hoc temperature scaling [12, 15, 39, 18]. Recent work extends
these ideas into RL by adding explicit confidence-target losses or rewriting confidence tokens in the
teacher distribution [50, 21, 5], but in doing so introduces a separate calibration objective alongside
the task objective; the two are reported to trade against each other. We approach the problem from a
different angle. The gap between the agent’s prospective belief and the eventual outcome is not just a
diagnostic of how well-calibrated the agent is; instead, it is atraining signalthat points to exactly the
rollouts where action-time information was insufficient.
Why prediction–reality gaps are informative.The same property that makes the prospective belief
invisible to retrospective losses also makes the gap between belief and outcome informative. By
a law-of-total-variance argument, the residual variance in the eventual outcome given action-time
information decomposes into aleatoric noise (irreducible even with privileged context) plus a non-
negativeprivileged-information gap: the share of outcome variance that no action-time predictor can
resolve. This places agent RL inside Learning Under Privileged Information (LUPI) framework [40,
30, 24]. The rollouts that materialize this gap, overconfident failures and underconfident successes,
are exactly where action-time information falls short of post-action information. Standard hindsight-
only methods see these rollouts only through their outcome label and treat them indistinguishably
from calibrated ones; we ask what changes if training explicitly uses the disagreement.
We introduceProspective Hindsight (PH), a self-calibrating training principle that augments any
retrospective base method with a signal derived from the prediction–reality gap. Before each rollout
is scored by the verifier or PRM, we re-query the same policy with a different prompt to elicit
aprospective predictionof the eventual outcome; comparing this prediction to the retrospective
evaluation yields a per-rolloutsurprisethat identifies the training samples where the agent’s self-model
is most inaccurate. PH amplifies the gradient contribution of these samples through a stop-gradient
reweighting of the base loss, preserving the rollout sampling distribution and the internal structure
of GRPO, OPD, or their combination. Because the prospective predictor shares parameters with
the policy rather than being an external head bolted onto the model, the predictor co-evolves with
the policy as training progresses: the agent’s self-model improves implicitly alongside the agent’s
behavior, the surprise signal progressively shifts focus to the agent’s remaining blind spots, and the
reweighting diminishes as the prediction–reality gap closes. PH therefore reduces miscalibration
as a byproduct of optimization rather than through an added calibration loss, sidestepping the
capability–calibration trade-off [21, 5]. Our main contributions are summarized as follows:
• We identify thehindsight trapas a structural blind spot of retrospective RL and connect the
resulting prediction–reality gap to a privileged-information quantity within the LUPI framework.
2

• We proposeProspective Hindsight, a principle method that converts this gap into a self-calibrating
training signal compatible with binary RL (GRPO), On-policy distillation, and their combination.
• We define a calibration taxonomy by pairing the prospective belief with the verifier outcome
yields four rollout cells that decompose calibration along two interpretable axes during training.
• PH improves both task performance and calibration on single-turn verifiable tasks and on a multi-
turn personal-agent task, with consistent gains across model scales. The dominant miscalibration
mode shifts structurally between regimes and PH addresses both successfully.
2 The Hindsight Trap in Agent RL
2.1 Agentic Reinforcement Learning
We consider an agent represented by a policy πθ acting in environments with verifiable outcomes. At
each step t∈ {1, . . . , T}, the agent observes a state st (a query, a conversation history, or a partial
task description), produces an actiona t ∼π θ(· |st), and receives a step-level outcome
rt =R(s t, at, ct)∈ {−1,0,+1}, y t =1[r t >0]∈ {0,1},(1)
where ct denotesprivileged contextthat the evaluator R observes but the agent does not at action time.
This covers single-step tasks ( T=1 , with ct a ground-truth reference) and multi-turn tasks ( T >1,
with ct=st+1 the next environmental state). A trajectory is τ={(s t, at, rt)}T t=1; the base methods
of §2.2 differ in howr t andc t shape the policy update.
2.2 Retrospective Training Methods
Current methods construct the policy update from rt, optionally combined with ct. Scalar-advantage
methods such as GRPO [33] normalize the reward within a group of rollouts sharing the same query;
token-level distillation methods such as OPD [1, 44, 14] use ct to construct a hindsight teacher whose
action distribution is distilled into the student; combined methods sum the two signals [ 42]. Full
advantage formulations are given in App. C.1. All three families share the same hindsight-only
property: the learning signal is computed entirely from post-action quantities (rt, ct, or both), and the
agent’s prospective belief at action time is invisible to the update. We abstract any such instantiation
as a base lossℓ base whose precise form does not matter for the analysis below.
2.3 The Self-Evaluation Blind Spot
Hindsight-only feedback collapses two distinct questions about each step into a single label. The
first is observable from the retrospective evaluator:what happened, captured by rt. The second is
invisible:whether the agent could have anticipated what would happenwhen it chosea t. Formally,
let zt ∈ {−1,0,+1}denote the agent’s prospective belief aboutyt, formed from (st, at) alone before
ct is observed: zt = +1 encodes an expectation of success, zt =−1 an expectation of failure, and
zt = 0 an explicit acknowledgement of uncertainty (honest uncertainty). The base loss is a function
of post-action quantities alone,ℓ base =F(τ,{c t}T t=1), and therefore independent of any suchz t:
E

∇θℓbase

 zt, yt  =E  ∇θℓbase

 yt  ∀z t ∈ {−1,0,+1},(2)
i.e., the gradient distribution depends on the realized outcome yt alone and is invariant to the agent’s
prospective belief.
We call the absence of supervision on zt theself-evaluation blind spot: standard updates assign
the same gradient to two rollouts that produced the same outcome, regardless of whether the agent
acted with calibrated belief, miscalibrated belief, or honest uncertainty. Two consequences follow on
the calibrated subset zt ∈ {−1,+1}(the zt=0 case inherits the same invariance and is treated as a
neutral class). A confident success and a lucky success receive identical reinforcement, even though
the former reflects calibrated competence while the latter is an unrecognized capability the agent
cannot deploy with confidence; symmetrically, an overconfident failure is penalized exactly like an
aware failure, even though the former is the more dangerous mode — the agent’s own model endorses
an action the verifier rejects, so the same mistake is likely to recur. Closing this blind spot requires a
learning signal tied to the gap between zt and yt, but only if that gap is structurally meaningful rather
than noise that should be averaged out.
3

2.4 Why Prediction–Reality Gaps Are Informative
To characterize the structural quantity that the discrete prospective belief zt should approximate,
consider its Bayes-optimal continuous idealization, f ⋆(st, at) :=E[yt |s t, at] = Pr(yt=1|s t, at),
the minimum-MSE estimator ofy t available without observingc t.
Proposition 1(Privileged-information gap).For any (st, at) in the support of the rollout distribution,
Var(yt |s t, at) =E[Var(y t |s t, at, ct)|s t, at]| {z }
aleatoric noise
+I ⋆(st, at)| {z }
privileged-information gap
,(3)
whereI ⋆(st, at) := Var(E[yt |s t, at, ct]|s t, at)≥0.
The first term is the aleatoric noise irreducible even with ct; the second, I ⋆(st, at), is precisely the
contribution that no action-time predictor f(s t, at) can resolve. States with large I ⋆ identify exactly
where the agent’s epistemic horizon is most limited and where the prediction–reality gap is informative
rather than residual noise. This places our setting in the Learning Under Privileged Information
framework [40, 30]: signals available at training time but not at decision time fundamentally constrain
the achievable predictor (proof and full LUPI connection in App. B.1). The decomposition motivates
a learning rule: maintain a self-evaluator that produces a prospective belief zt from action-time
information alone, and reweightℓ base as a function of the gap betweenz t andy t.
3 The Prospective Hindsight Method
Prospective Hindsight (PH) converts this gap into a usable training signal through three components:
a self-evaluator that produces a per-rollout belief from action-time information; a four-cell taxonomy
that partitions rollouts by belief and outcome; and a one-line reweighting of the base loss driven by a
binary surprise indicator. We show that the same rule has a complementary interpretation as implicit
calibration. The end-to-end procedure is summarized in Algorithm 1(App. C).
3.1 Prospective Self-Evaluator
The agent πθ produces both the action at and a prospective self-evaluation of the same action. The
self-evaluator distribution peval θ (· |st, at) is realized by prompting πθ with a template that asks
whether the eventual outcome of at will be a success; the answer is parsed from a \boxed{·} field
as a ternary score in {−1,0,+1} (success / failure / honest uncertainty; App. C.4). Crucially, the
self-evaluator sees only (st, at) and does not observe the privileged context ct (full templates in
App. F). To reduce variance, we draw M independent samples per step and aggregate by majority
vote: zt = maj

z(1) t , . . . , z(M) t

, z(m) t i.i.d. ∼p eval θ (· |st, at). The only training-time overhead is M
extra forward passes per rollout step.
3.2 A Calibration Taxonomy of Rollouts
As shown in Table 1, the pair (zt, yt) partitions every rollout with zt ∈ {−1,+1}into one of four
calibration cellsalong two epistemic axes, the outcome axis ( yt, observable from the verifier) and the
anticipation axis (zt, the agent’s prospective self-assessment). Diagonal cells (CS, AF) are calibrated;
off-diagonal cells (OF, US) are miscalibrated and capture the asymmetry analyzed in §2.3: OF
rollouts are the most consequential failure mode (the agent’s own model endorses an action the
verifier rejects), while US rollouts identify capability the agent has but cannot yet recognize.
Table 1: Calibration cells of rollouts, indexed by the agent’s prospective beliefzt ∈ {−1,+1}and
the realized outcomey t ∈ {0,1}. Rollouts withzt=0are deferred to App. C.4.
Cellz t yt Epistemic interpretation
CS(confident success)+1 1calibrated competence
OF(overconfident failure)+1 0miscalibrated; agent trusts a wrong action
US(underconfident success)−1 1miscalibrated; agent doubts a correct action
AF(aware failure)−1 0calibrated incompetence
4

3.3 The Prospective Hindsight Update Rule
PH attaches to each rollout a binarysurprisescalar and amplifies the base loss in proportion.
Surprise.For zt ∈ {−1,+1}and yt ∈ {0,1}, the per-rollout surprise is the binary indicator of a
prediction–reality gap,
ξt =⊮

(zt, yt)∈ {OF,US}

∈ {0,1}.(4)
ξt=1 exactly when the agent’s prospective belief disagrees with the realized outcome (overconfident
or underconfident); ξt=0 when they agree (CS or AF). This is the per-rollout realization of the
privileged-information gap I ⋆ from Proposition 1: rollouts with ξt=1 are exactly those whose
existence makesI ⋆ visible from inside the agent’s own model.
Surprise-weighted update.Let ℓbase t (θ) be the per-rollout base loss (§2.2); PH is agnostic to whether
the base method is GRPO, OPD, or their combination. The PH-modified loss is
ℓPH t (θ) =  1 +α·ξ t  ·ℓ base t (θ),∇ θℓPH t (θ) =  1 +α·ξ t  · ∇θℓbase t (θ),(5)
with α≥0 the only hyperparameter and ξt a stop-gradient constant. Calibrated rollouts (ξt=0) keep
the base loss unchanged; surprising rollouts (ξt=1) are upweighted by 1+α. Setting α=0 recovers
the base method exactly; we useα=1as the default.
3.4 PH as Calibration through Reweighting
We also develop a complementary interpretation of the same rule as an implicit calibration mechanism.
As the prospective evaluator peval θ shares parameters with the policy πθ, every PH update changes
both the action distribution and the agent’s prospective belief; PH biases this joint update toward
states in which the two agree. We frame the analysis below asmotivationfor why PH would be
expected to reduce miscalibration as a side effect of optimization, rather than as a formal guarantee.
Surprise-weighted decomposition.The PH expected loss decomposes additively into the base
objective plus a non-negative surprise residual:
Eρθ

ℓPH t  =E ρθ  ℓbase t  +α· R(θ),R(θ) :=E ρθ  ξt ·ℓ base t  ≥0,(6)
where ρθ is the joint rollout distribution induced by πθ, peval θ , and the verifier (App. B.2). The
surprise residual R(θ) is the base loss restricted to the miscalibrated cells OF and US: PH minimizes
a regularized objective in which surprising rollouts contribute through both their own loss and the
surprise penalty.
Miscalibration rate.Define the agent’s miscalibration rate against the verifier:
M(θ) :=E ρθ

ξt

= Pr ρθ

(zt, yt)∈ {OF,US}

,(7)
which equals the binary Brier score of the deterministic predictor z′ t=(zt+1)/2 against yt (App. B.2).
Let c(θ) :=E ρθ

ℓbase t

 ξt = 1  denote the average base loss on surprising rollouts. By the tower
rule,
R(θ) =c(θ)· M(θ),(8)
which is anexactidentity rather than an inequality (Prop. 3 of App. B.2). Eq. 8 admits two descent
pathways for the residual: (i) reducing M(θ) by aligning the prospective belief with the verifier
outcome, or (ii) reducing c(θ) by lowering the base loss on the miscalibrated set. Each PH gradient
step is one or the other (or both), without an explicit calibration loss ever entering the optimization.
When does the residual identity bind?Eq. 8 is informative as a calibration lever in the regime
where c(θ) remains bounded away from zero. Three training phases follow naturally. Early on, both
c(θ) and M(θ) are large, and minimizing R(θ) admits both pathways simultaneously; this is the
regime where PH delivers its largest empirical gains (§4). In mid-training, both factors decrease as the
agent’s self-model improves. At convergence,c(θ)→0andM(θ)→0together, soR(θ)vanishes
and PH and the base method share the same fixed points (App. B.2). The calibration interpretation is
therefore not a uniform statement about the optimization landscape but a description of how PH’s
residualdecomposesduring the operative training window.
Reported metric.Among the two cells contributing to M(θ), OF carries the dominant practical
weight (§2.3). We therefore report theoverconfident-failure rate
OFR(θ) := Pr ρθ

yt=0

 zt= + 1  = Pr[OF] Pr[zt=+1] ,(9)
5

Table 2: Single-turn results. Validation accuracy is the average / maximum loggedmean@16 (%); OFR
=OF/(CS+OF) (failure rate among predicted successes) and Surprise =OF+US (total prediction–
reality mismatch percentage);Early/Lateare the first / last 5 training steps and∆=Late−Early.
Dataset Method Val. Acc. OFR Surprise
Avg.↑Max↑Early Late↓∆↓Early Late↓∆↓
Science Q&A
SDPO 63.0 73.4 75.3 34.2 -41.1 70.9 35.2 -35.7
+Random 65.4 74.3 74.1 33.3 -41.7 69.0 35.3 -33.7
+Failure-only 65.1 74.7 73.9 25.0 -48.9 69.0 24.4 -44.6
+PH (α= 0.5) 65.7 75.5 76.8 20.9 -56.0 71.7 21.8 -49.9
+PH (α= 1.0) 64.0 74.2 73.2 23.9 -49.3 68.6 21.1 -47.5
+PH (α= 2.0) 65.8 76.374.4 24.9 -49.5 69.9 24.8 -45.1
Tool Use
SDPO 57.7 60.2 77.7 40.7 -37.0 72.8 41.6 -31.2
+Random 58.2 61.6 77.4 36.3 -41.0 72.3 36.2 -36.1
+Failure-only 58.1 60.6 76.9 39.3 -37.6 72.7 39.2 -33.5
+PH (α= 0.5) 57.3 61.0 77.9 36.2 -41.7 73.0 36.2 -36.8
+PH (α= 1.0) 58.2 61.7 76.6 33.6 -43.0 71.9 33.5 -38.4
+PH (α= 2.0) 58.260.9 77.6 38.2 -39.4 73.0 38.3 -34.7
the OF-conditional projection of M(θ), alongside task success. This connects PH to implicit
calibration of language models [15, 39, 22], in which post-training feedback induces well-calibrated
confidence without an explicit calibration loss; PH makes such implicit calibration the explicit driver
of optimization rather than an emergent side effect. We emphasize that this connection isdiagnostic:
PH does not minimize M(θ) as an explicit objective, and the alignment between the PH update
direction and−∇ θM(θ)is a quantitative motivation rather than a pointwise guarantee (App. B.2).
0 50 100 150
Training step
0%
20%
40%
60%
80%
100%Rollout share
PH composition CS OF US AF
50 100 150
Training step
1.2
1.4
1.6Mean PH weight
PH diagnostics
mean weight
verifier pass rate
0%
20%
40%
60%
80%
Verifier pass rate
Figure 2:Self-evaluation dynamics under PH on Science Q&A ( α=1).Left: per-step composition
of the four PH cells (CS / OF / US / AF); overconfident failures shrink while confident successes
grow. Right: the mean PH weight decays as the verifier pass rate rises, indicating that PH acts as an
adaptive training signal that anneals as the prediction–reality gap closes.
4 Experiments
4.1 Experimental Setup
We evaluate PH in two complementary regimes that stress retrospective signals of different fidelity.
Single-turnuses verifiers on SCIENCEQ&A [ 9] and TOOLUSE[ 38] with SDPO [14] as the base
loss.Multi-turnuses an LLM-based PRM judge on the OpenClaw-RL [ 42] PERSONALAGENT
task (GPT-4.1 user simulator), where PH plugs into RL (GRPO [ 33]), OPD [1, 44, 14], and their
Combined variant. All main runs use OLMO-3-7B-INSTRUCT[ 29] as both policy and self-evaluator
(distinct prompts, shared parameters). The prospective predictor uses M=1 sample in single-turn
(deterministic verifier) and M=3 in multi-turn (stochastic PRM); cross-scale evidence onGPT-OSS-
20B [2] and full hyperparameters are deferred to App. D.
Baselines and ablations.The boundary case α=0 recovers the base method exactly (Baseline).
To separate PH’s surprise-basedselectionof which rollouts to upweight from the contribution of
additional gradient mass, we compare against two strong reweighting controls (single-turn, App. D.3):
RandomReweight, which assigns the same per-step total weight as PH but to a uniformly sampled
6

Table 3: Multi-turn personal-agent results (GPT-4.1 simulator). PH plugged into RL, OPD, and
the Combined recipe; performance is the teacher-side personalization-evaluator score, calibration is
computed over teacher-side rollouts within mixed training,∆ best=Best−initial.
Capability Calibration
Method Setting Avg.↑Best↑∆ best ↑OFR↓Surprise↓Prosp. Acc.↑
RL
GRPO 68.6 77.7 +8.5 5.3 16.5 83.5
+PH (α= 0.5) 72.6 77.7 +8.7 4.9 15.0 85.0
+PH (α= 1.0) 75.8 82.9 +14.8 3.1 12.2 87.8
+PH (α= 2.0) 68.6 77.3 +9.42.516.0 84.0
OPD
SDPO 54.0 65.6 +2.5 15.9 37.2 62.8
+PH (α= 0.5) 61.8 77.7 +5.6 1.5 13.7 86.3
+PH (α= 1.0) 69.3 75.2 +2.7 2.6 18.1 81.9
+PH (α= 2.0) 59.2 77.3+17.15.0 17.2 82.8
Combined
RL+OPD 61.2 73.5 +0.8 10.0 40.1 59.9
+PH (α= 0.5) 66.5 75.6 +8.1 4.3 28.4 71.6
+PH (α= 1.0) 65.1 78.5 +8.1 6.8 36.0 64.0
+PH (α= 2.0) 60.3 64.4 +6.02.529.5 70.5
subset of rollouts, andFailure-onlyReweight, which upweights all verifier failures ( yt=0). Both use
the same multiplier(1+α)as PH, so only the selection rule differs.
Metrics and Evaluations.Capability: mean@16 (single-turn) or external-judge score (multi-turn).
Calibration: OFR= Pr[yt=0|z t=+1], surprise rate M(θ)= Pr[ξt=1], and prospective accuracy
PAcc=1−M(θ). Single-turn tables reportEarly/Lateas the average over the first/last 5 training
steps; multi-turn tables reportAvgover post-initial checkpoints,Best, and ∆best=Best−initial. All
headline numbers are aggregated over 3 seeds.
30% 40% 50% 60% 70% 80%
Validation accuracy
0%
20%
40%
60%
80%OFR = OF / (CS + OF)
Overconfidence vs. capability
α=0.0
α=0.5
α=1.0
0 50 100 150
Training step
30%
40%
50%
60%
70%
80%PAcc = CS + AF
Prospective accuracy
α=0.0
α=0.5
α=1.0
α=0.0α=0.25α=0.5α=1.0α=2.0
0%
10%
20%
30%
40%
50%Mean OFR when acc ≥ 60%
Overconfidence
Figure 3: Capability and calibration dynamics on Science Q&A across α.Left:OFR vs. Validation
Accuracy;Middle:prospective accuracy over training.Right:Effect ofαon overconfidence rate.
4.2 Single-Turn Verifiable Tasks
Across both domains in Table 2, PH preserves or slightly improves SDPO while substantially
shrinking calibration error. On Science Q&A, late-training OFR drops from34.2% (SDPO) to 20.9%
at α=0.5, and the surprise rate tracks OFR closely (35.2%→21.8%). On Tool Use, α=1.0 jointly
attains the best capability and calibration ( mean@16=58.2/61.7, OFR 33.6%, surprise 33.5%).
Figure 4 replicates the SDPO vs. SDPO+PH comparison onGPT-OSS-20B. Using the same α=1.0,
PH delivers comparable or larger improvements on all three metrics, showing that it tracks a structural
property of hindsight-only training that persists across model scale.
Selection, not mass, drives the gain.A natural concern is that PH simply adds gradient mass to
a subset of rollouts; any reweighting with the same per-step total weight might do equally well.
Randomreweighting leaves calibration essentially unchanged on Science Q&A (OFR 33.3% vs.
SDPO’s 34.2%) and improves it only modestly on Tool Use; the gain over SDPO is far smaller than
PH’s.Failure-onlyreweighting recovers most of PH’s OFR reduction on Science Q&A ( 25.0% vs.
20.9%) but trails PH on the surprise rate (24.4% vs. 21.8%). The OFR gap reflects that single-turn
miscalibration is OF-dominated (Figure 5), so a 1D outcome-axis baseline already captures most of it;
the surprise-rate gap reflects the cells PH amplifies but failure-only misses underconfident successes.
7

PH is a self-extinguishing adaptive curriculum.Figure 2 shows the per-step PH-cell composition
and the corresponding PH-weight trajectory on Science Q&A. The overconfident-failure (OF) cell
shrinks monotonically across training while the confident-success (CS) cell grows; the underconfident-
success (US) and aware-failure (AF) cells stay small throughout. Crucially, the mean PH weight
(right) decays as the verifier pass rate rises: PH amplifies gradient signal early when miscalibration is
rampant and naturally anneals once the policy has learned to predict its own outcomes, matching the
asymptotic argument in App. B.2 (wt→1 as ξt→0). This means PH does not require a learning-rate
schedule for the surprise weight: the data itself controls the curriculum.
Calibration emerges as a byproduct of surprise reweighting.Figure 3 (middle) tracks prospective
accuracy PAcc(θ)=1−M(θ) across training. The pre-training self-evaluator is essentially uncali-
brated but PH lifts PAcc from ∼30% to ∼80% while the SDPO baseline plateaus near 73%. The
predictor receives no direct gradient (the reweighting is stop-gradient on ξt); the gap is therefore a
byproductof policy optimization, evidence that PH co-trains a calibrated self-model alongside the
policy at no additional parameter cost. This is the mechanism behind the simultaneous capability
and calibration improvement: the same gradient steps that reduce ℓbase on miscalibrated rollouts also
drive M(θ)→0 via the parameter-sharing channel. The full α-sweep confirms the entire window
improves both axes simultaneously, withα=0.5 attaining the lowest mean OFR at matched capability.
OLMo-3-7B GPT-OSS-20B50
55
60
65
70
75
+1.0
+1.4
Val. Acc. Avg. (%)
(  better)
OLMo-3-7B GPT-OSS-20B
20
30
40 10.3
9.1
OFR Late (%)
(  better)
OLMo-3-7B GPT-OSS-20B
20
30
40 14.1
11.5
Surprise Late (%)
(  better)
SDPO baseline SDPO + PH ( =1.0)
Figure 4: Capability and calibration gains from PH transfer across model scale using SDPO baseline
and SDPO+PH (α=1.0) on OLMo-3-7B-Instruct and gpt-oss-20B.
4.3 Multi-Turn Personal Agent
Multi-turn shifts the dominant miscalibration mode from OF to US.Before discussing capability
and calibration numbers, we characterize thekindof miscalibration the multi-turn regime produces.
Figure 5 aggregates (zt, yt) pairs across training under α=1.0 and contrasts single-turn tasks with
the three multi-turn base methods. The picture is structurally different: while single-turn rollouts are
dominated by overconfident failures (OF= 34.1%, US= 2.7%), multi-turn rollouts shift the dominant
miscalibration tounderconfident successes(US), which grow monotonically across base methods, RL
(13.8%) < OPD (27.9%) < Combined (34.5%), while OF stays uniformly small (4–5%). The two
regimes therefore expose complementary failure modes: single-turn agents over-trust wrong actions,
while multi-turn agents under-trust correct ones.
Single-turnMulti-turn
(RL)
Multi-turn
(OPD)
Multi-turn
(Combined)
0%
25%
50%
75%
100%Rollout share57.2%
79.5%
63.7% 57.3%
34.1%
4.3%
4.9%
5.3%
2.7% 13.8%
27.9% 34.5%
6.0% 2.4% 3.5% 2.8%
Cell
AF
US
OF
CS
Figure 5: PH cell composition differs structurally
between single-turn and multi-turn settings.
PH improves all three base methods, with the
largest lift on OPD.At α=1.0, PH improves the
trajectory-averaged teacher-side score over the
baseline in every block of Table 3: RL (+7.2),
OPD (+15.3), and Combined (+3.9). The OPD
block is the most striking: its baseline has the
weakest absolute performance, and PH simul-
taneously stabilizes the trajectory (+15.3 Avg)
and raises the peak. The cell-composition pic-
ture above is consistent with the OPD-vs-RL or-
dering: OPD’s privileged-context teacher leaves
the student with substantially more underconfi-
dent successes than RL (US: 27.9% vs. 13.8%), and PH amplifies precisely those rollouts. The
Combined block is a partial exception to this ordering since its US share (34.5%) is the highest of the
three, yet its PH gain is the smallest.
Calibration improves uniformly at α=1.0.At the headline α=1.0, OFR drops in every block and
prospective accuracy rises in every block, peaking at87.8% (RL+PH, α=1.0) and 86.3% (OPD+PH,
8

α=0.5). The surprise gate concentrates gradient mass on exactly the cells (OF, US) that contribute
to M(θ), and those cells empirically shrink under PH training. A per-turn breakdown (Figure 8)
shows that PH compresses overconfidence most in late-turn positions, where the agent’s self-model is
least developed. Larger α trades stability for further OFR reduction: at α=2.0, the RL block reaches
the lowest OFR in the table (2.5%) but the predictor collapses toward a near-constant zt=−1 output
(Surprise rate 16.0%, prospective accuracy 84.0%), so the calibration improvement comes at the cost
of a degraded self-model rather than from genuinely better belief–outcome agreement. Replacing the
GPT-4.1 user simulator with GPT-5.4 preserves the qualitative pattern of Table 3 (see Figure 9).
What PH is doing, across regimes.The base method’s gradient is invariant to the agent’s prospective
belief; the surprise indicator ξt is the per-rollout realization of the privileged-information gap I ⋆
that this invariance hides. Three observations across both regimes are consistent with this view: (i)
calibration improves as a byproduct of optimization, so the same gradient steps that drive the base loss
also reduce M(θ); (ii) the dominant miscalibration cell flips between regimes yet the same update
rule covers both; and (iii) the surprise weight self-extinguishes as the prediction–reality gap closes,
so PH asymptotically reduces to the base method. Together these suggest that what PH amplifies is
not a particular failure mode but the existence of a prediction–reality discrepancy itself, which is why
the same scalarαtransfers across tasks, base methods, and model scales without re-tuning.
5 Related work
Retrospective training signals in Agentic RL.Recent RL/agentic RL frameworks have steadily
enriched the post-action signal delivered to the policy [45, 4]. OpenClaw-RL [42] unifies binary RL
(GRPO [33], PPO [32]), on-policy distillation (OPD [1, 44, 14, 34, 31, 17]), and their combination
under a single asynchronous training stack [54, 6]; Buening et al. [3] further show that raw multi-turn
user interactions are themselves sufficient supervision for self-distillation without an explicit reward
model. These methods differ in mechanism but share a structural property: every learning signal is
computed entirely from quantities observedafterthe agent has acted, so the agent’s prospective belief
at action time never enters the gradient [1, 44, 41]. Prospective Hindsight is orthogonal to this axis
of progress: it leaves the base method’s rollout, advantage, and regularization structure intact, and
instead converts the gap between an action-time prospective prediction and the eventual retrospective
evaluation into a per-rollout reweighting that plugs into any of the above base methods.
Calibration of language-model agents.Most prior work treats calibration as a property of the
trained model to be measured or controlled at inference time, through diagnostic studies of confidence–
accuracy alignment [12, 15, 10], elicitation of verbalized confidence or sampling-based uncertainty
estimates [39, 22, 19], trajectory-level uncertainty quantification in agentic settings [18, 8, 53, 23, 13,
47, 51], and recent analyses linking hallucination to training procedures that reward confident guesses
over abstention [16]. A separate line moves calibration into RL by adding an explicit confidence-
target objective: CaOPD [50] attributes overconfidence in hindsight distillation to teacher–student
information asymmetry and proposes confidence-token replacement; Leng et al. [21] and Damani
et al. [5] report similar calibration-augmented RL recipes. These approaches consistently report
acapability–calibration trade-off[ 43]: improved calibration comes at the cost of a regression in
task accuracy. PH proceeds differently: rather than adding a calibration term to compete with the
task objective, we use the per-rollout disagreement between the agent’s prospective belief and the
verifier outcome toreweightwhich base-method gradients deserve more mass. Calibration improves
as a byproduct of the same gradient steps that drive task success, and the trade-off observed in
calibration-augmented baselines does not arise because calibration and capability share a single
descent direction.
6 Conclusion
Prospective Hindsight treats the gap between an agent’s prospective belief and the verifier’s retro-
spective outcome as a learning resource rather than a diagnostic, amplifying the gradient on exactly
the rollouts where retrospective signals are uninformative. The same principle should extend beyond
the binary verifiers and per-turn PRMs studied here, to longer horizons such as software engineering,
terminal-use, GUI, and research agents, and to base methods beyond GRPO and on-policy distillation.
We see PH as a first but critical step toward reliable agent-RL pipelines that optimize task performance
and self-calibration jointly, by construction rather than through a separate calibration objective.
9

References
[1] Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos Garea,
Matthieu Geist, and Olivier Bachem. On-policy distillation of language models: Learning from
self-generated mistakes. InThe twelfth international conference on learning representations,
2024.
[2] Sandhini Agarwal, Lama Ahmad, Jason Ai, Sam Altman, Andy Applebaum, Edwin Arbus,
Rahul K Arora, Yu Bai, Bowen Baker, Haiming Bao, et al. gpt-oss-120b & gpt-oss-20b model
card.arXiv preprint arXiv:2508.10925, 2025.
[3] Thomas Kleine Buening, Jonas Hübotter, Barna Pásztor, Idan Shenfeld, Giorgia Ramponi,
and Andreas Krause. Aligning language models from user interactions.arXiv preprint
arXiv:2603.12273, 2026.
[4] Fangming Cui, Ruixiao Zhu, Cheng Fang, Sunan Li, and Jiahong Li. Rethinking agentic
reinforcement learning in large language models.arXiv preprint arXiv:2604.27859, 2026.
[5] Mehul Damani, Isha Puri, Stewart Slocum, Idan Shenfeld, Leshem Choshen, Yoon Kim, and
Jacob Andreas. Beyond binary rewards: Training lms to reason about their uncertainty.arXiv
preprint arXiv:2507.16806, 2025.
[6] Ken Ding. Hdpo: Hybrid distillation policy optimization via privileged self-distillation.arXiv
preprint arXiv:2603.23871, 2026.
[7] Guanting Dong, Hangyu Mao, Kai Ma, Licheng Bao, Yifei Chen, Zhongyuan Wang, Zhongxia
Chen, Jiazhen Du, Huiyang Wang, Fuzheng Zhang, et al. Agentic reinforced policy optimization.
arXiv preprint arXiv:2507.19849, 2025.
[8] Jinhao Duan, James Diffenderfer, Sandeep Madireddy, Tianlong Chen, Bhavya Kailkhura,
and Kaidi Xu. Uprop: Investigating the uncertainty propagation of llms in multi-step agentic
decision-making.arXiv preprint arXiv:2506.17419, 2025.
[9] Kehua Feng, Xinyi Shen, Weijie Wang, Xiang Zhuang, Yuqi Tang, Qiang Zhang, and Keyan
Ding. Sciknoweval: Evaluating multi-level scientific knowledge of large language models.
arXiv preprint arXiv:2406.09098, 2024.
[10] Jiahui Geng, Fengyu Cai, Yuxia Wang, Heinz Koeppl, Preslav Nakov, and Iryna Gurevych.
A survey of confidence estimation and calibration in large language models. InProceedings
of the 2024 Conference of the North American Chapter of the Association for Computational
Linguistics: Human Language Technologies (Volume 1: Long Papers), pages 6577–6595, 2024.
[11] Tobias Groot and Matias Valdenegro-Toro. Overconfidence is key: Verbalized uncertainty
evaluation in large language and vision-language models.arXiv preprint arXiv:2405.02917,
2024.
[12] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Weinberger. On calibration of modern neural
networks. InInternational conference on machine learning, pages 1321–1330. PMLR, 2017.
[13] Jiuzhou Han, Wray Buntine, and Ehsan Shareghi. Towards uncertainty-aware language agent.
InFindings of the Association for Computational Linguistics ACL 2024, pages 6662–6685,
2024.
[14] Jonas Hübotter, Frederike Lübeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta,
Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, et al. Reinforcement
learning via self-distillation.arXiv preprint arXiv:2601.20802, 2026.
[15] Saurav Kadavath, Tom Conerly, Amanda Askell, Tom Henighan, Dawn Drain, Ethan Perez,
Nicholas Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli Tran-Johnson, et al. Language
models (mostly) know what they know.arXiv preprint arXiv:2207.05221, 2022.
[16] Adam Tauman Kalai, Ofir Nachum, Santosh S Vempala, and Edwin Zhang. Why language
models hallucinate.arXiv preprint arXiv:2509.04664, 2025.
10

[17] Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim, Jiwon Jeon,
Dongsheng Li, and Yuqing Yang. Why does self-distillation (sometimes) degrade the reasoning
capability of llms?arXiv preprint arXiv:2603.24472, 2026.
[18] Michael Kirchhof, Gjergji Kasneci, and Enkelejda Kasneci. Position: Uncertainty quantification
needs reassessment for large language model agents. InForty-second International Conference
on Machine Learning Position Paper Track, 2025.
[19] Lorenz Kuhn, Yarin Gal, and Sebastian Farquhar. Semantic uncertainty: Linguistic invariances
for uncertainty estimation in natural language generation. InThe Eleventh International
Conference on Learning Representations, 2023.
[20] Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu,
Joseph Gonzalez, Hao Zhang, and Ion Stoica. Efficient memory management for large language
model serving with pagedattention. InProceedings of the 29th symposium on operating systems
principles, pages 611–626, 2023.
[21] Jixuan Leng, Chengsong Huang, Banghua Zhu, and Jiaxin Huang. Taming overconfidence in
LLMs: Reward calibration in RLHF.arXiv preprint arXiv:2410.09724, 2024.
[22] Stephanie Lin, Jacob Hilton, and Owain Evans. Teaching models to express their uncertainty in
words.arXiv preprint arXiv:2205.14334, 2022.
[23] Hao Liu, Zi-Yi Dou, Yixin Wang, Nanyun Peng, and Yisong Yue. Uncertainty calibration
for tool-using language agents. InFindings of the Association for Computational Linguistics:
EMNLP 2024, pages 16781–16805, 2024.
[24] David Lopez-Paz, Léon Bottou, Bernhard Schölkopf, and Vladimir Vapnik. Unifying distillation
and privileged information.arXiv preprint arXiv:1511.03643, 2015.
[25] Kevin Lu and Thinking Machines Lab. On-policy distillation.Thinking Machines Lab: Connec-
tionism, 2025. https://thinkingmachines.ai/blog/on-policy-distillation.
[26] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri
Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al. Self-refine: Iterative refinement
with self-feedback.Advances in Neural Information Processing Systems, 36:46534–46594,
2023.
[27] Potsawee Manakul, Adian Liusie, and Mark Gales. Selfcheckgpt: Zero-resource black-box
hallucination detection for generative large language models. InProceedings of the 2023
conference on empirical methods in natural language processing, pages 9004–9017, 2023.
[28] Changdae Oh, Seongheon Park, To Eun Kim, Jiatong Li, Wendi Li, Samuel Yeh, Xuefeng Du,
Hamed Hassani, Paul Bogdan, Dawn Song, et al. Uncertainty quantification in llm agents:
Foundations, emerging challenges, and opportunities.arXiv preprint arXiv:2602.05073, 2026.
[29] Team Olmo, Allyson Ettinger, Amanda Bertsch, Bailey Kuehl, David Graham, David Heineman,
Dirk Groeneveld, Faeze Brahman, Finbarr Timbers, Hamish Ivison, et al. Olmo 3.arXiv preprint
arXiv:2512.13961, 2025.
[30] Dmitry Pechyony and Vladimir Vapnik. On the theory of learnining with privileged information.
Advances in neural information processing systems, 23, 2010.
[31] Hejian Sang, Yuanda Xu, Zhengze Zhou, Ran He, Zhipeng Wang, and Jiachen Sun. On-policy
self-distillation for reasoning compression.arXiv preprint arXiv:2603.05433, 2026.
[32] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
[33] Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang,
Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathematical
reasoning in open language models.arXiv preprint arXiv:2402.03300, 2024.
[34] Idan Shenfeld, Mehul Damani, Jonas Hübotter, and Pulkit Agrawal. Self-distillation enables
continual learning.arXiv preprint arXiv:2601.19897, 2026.
11

[35] Guangming Sheng, Chi Zhang, Zilingfeng Ye, Xibin Wu, Wang Zhang, Ru Zhang, Yanghua
Peng, Haibin Lin, and Chuan Wu. Hybridflow: A flexible and efficient rlhf framework. In
Proceedings of the Twentieth European Conference on Computer Systems, pages 1279–1297,
2025.
[36] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
Reflexion: Language agents with verbal reinforcement learning.Advances in Neural Information
Processing Systems, 36:8634–8652, 2023.
[37] Mingyang Song and Mao Zheng. A survey of on-policy distillation for large language models.
arXiv preprint arXiv:2604.00626, 2026.
[38] Qiaoyu Tang, Ziliang Deng, Hongyu Lin, Xianpei Han, Qiao Liang, Boxi Cao, and Le Sun.
Toolalpaca: Generalized tool learning for language models with 3000 simulated cases.arXiv
preprint arXiv:2306.05301, 2023.
[39] Katherine Tian, Eric Mitchell, Allan Zhou, Archit Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea
Finn, and Christopher D Manning. Just ask for calibration: Strategies for eliciting calibrated
confidence scores from language models fine-tuned with human feedback. InProceedings of
the 2023 Conference on Empirical Methods in Natural Language Processing, pages 5433–5442,
2023.
[40] Vladimir Vapnik and Akshay Vashist. A new learning paradigm: Learning using privileged
information.Neural networks, 22(5-6):544–557, 2009.
[41] Jiaqi Wang, Wenhao Zhang, Weijie Shi, Yaliang Li, and James Cheng. Tcod: Exploring
temporal curriculum in on-policy distillation for multi-turn autonomous agents.arXiv preprint
arXiv:2604.24005, 2026.
[42] Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, and Ling Yang. Openclaw-rl: Train
any agent simply by talking.arXiv preprint arXiv:2603.10165, 2026.
[43] Sin-Han Yang, Cheng-Kuang Wu, Chieh-Yen Lin, Yun-Nung Chen, Hung-yi Lee, and Shao-Hua
Sun. On calibration of large language models: From response to capability.arXiv preprint
arXiv:2602.13540, 2026.
[44] Tianzhu Ye, Li Dong, Xun Wu, Shaohan Huang, and Furu Wei. On-policy context distillation
for language models.arXiv preprint arXiv:2602.12275, 2026.
[45] Guibin Zhang, Hejia Geng, Xiaohang Yu, Zhenfei Yin, Zaibin Zhang, Zelin Tan, Heng Zhou,
Zhongzhi Li, Xiangyuan Xue, Yijiang Li, et al. The landscape of agentic reinforcement learning
for llms: A survey.arXiv preprint arXiv:2509.02547, 2025.
[46] Guibin Zhang, Junhao Wang, Junjie Chen, Wangchunshu Zhou, Kun Wang, and Shuicheng
Yan. Agentracer: Who is inducing failure in the llm agentic systems?arXiv preprint
arXiv:2509.03312, 2025.
[47] Jiaxin Zhang, Prafulla Kumar Choubey, Kung-Hsiang Huang, Caiming Xiong, and Chien-Sheng
Wu. Agentic uncertainty quantification.arXiv preprint arXiv:2601.15703, 2026.
[48] Jiaxin Zhang, Wendi Cui, Zhuohang Li, Lifu Huang, Bradley A Malin, Caiming Xiong, and
Chien-Sheng Wu. From passive metric to active signal: The evolving role of uncertainty
quantification in large language models. InFindings of the Association for Computational
Linguistics: ACL 2026, pages 41525–41544, 2026.
[49] Jiaxin Zhang, Zhuohang Li, Kamalika Das, Bradley Malin, and Sricharan Kumar. Sac3:
reliable hallucination detection in black-box language models via semantic-aware cross-check
consistency. InFindings of the Association for Computational Linguistics: EMNLP 2023, pages
15445–15458, 2023.
[50] Jiaxin Zhang, Xiangyu Peng, Qinglin Chen, Qinyuan Ye, Caiming Xiong, and Chien-Sheng Wu.
The illusion of certainty: Decoupling capability and calibration in on-policy distillation.arXiv
preprint arXiv:2604.16830, 2026.
12

[51] Jiaxin Zhang, Caiming Xiong, and Chien-Sheng Wu. Agentic confidence calibration.arXiv
preprint arXiv:2601.15778, 2026.
[52] Shaokun Zhang, Ming Yin, Jieyu Zhang, Jiale Liu, Zhiguang Han, Jingyang Zhang, Beibin Li,
Chi Wang, Huazheng Wang, Yiran Chen, et al. Which agent causes task failures and when?
on automated failure attribution of llm multi-agent systems.arXiv preprint arXiv:2505.00212,
2025.
[53] Qiwei Zhao, Dong Li, Yanchi Liu, Wei Cheng, Yiyou Sun, Mika Oishi, Takao Osaki, Katsushi
Matsuda, Huaxiu Yao, Chen Zhao, et al. Uncertainty propagation on llm agent. InProceedings
of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long
Papers), pages 6064–6073, 2025.
[54] Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya
Grover. Self-distilled reasoner: On-policy self-distillation for large language models.arXiv
preprint arXiv:2601.18734, 2026.
[55] Kunlun Zhu, Zijia Liu, Bingxuan Li, Muxin Tian, Yingxuan Yang, Jiaxun Zhang, Pengrui Han,
Qipeng Xie, Fuyang Cui, Weijia Zhang, et al. Where llm agents fail and how they can learn
from failures.arXiv preprint arXiv:2509.25370, 2025.
13

Contents
Contents
1 Introduction 2
2 The Hindsight Trap in Agent RL 3
2.1 Agentic Reinforcement Learning . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.2 Retrospective Training Methods . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.3 The Self-Evaluation Blind Spot . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
2.4 Why Prediction–Reality Gaps Are Informative . . . . . . . . . . . . . . . . . . . . 4
3 The Prospective Hindsight Method 4
3.1 Prospective Self-Evaluator . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.2 A Calibration Taxonomy of Rollouts . . . . . . . . . . . . . . . . . . . . . . . . . 4
3.3 The Prospective Hindsight Update Rule . . . . . . . . . . . . . . . . . . . . . . . 5
3.4 PH as Calibration through Reweighting . . . . . . . . . . . . . . . . . . . . . . . 5
4 Experiments 6
4.1 Experimental Setup . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
4.2 Single-Turn Verifiable Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
4.3 Multi-Turn Personal Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
5 Related work 9
6 Conclusion 9
A Extended Related Work and Discussion 16
B Theoretical Details and Proofs 17
B.1 Proof of Proposition 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
B.2 PH as Calibration through Reweighting: Detailed Analysis . . . . . . . . . . . . . 18
C Algorithm and Implementation Details 22
C.1 Base Method Advantage Formulations . . . . . . . . . . . . . . . . . . . . . . . . 22
C.2 PH Algorithm Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
C.3 Discrete and Continuous PH Gates . . . . . . . . . . . . . . . . . . . . . . . . . . 23
C.4 Honest Uncertainty: Thez t = 0Class . . . . . . . . . . . . . . . . . . . . . . . . 24
D Additional Experimental Setup 24
D.1 Single-Turn Verifiable Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
D.2 Multi-Turn Personal Agent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
D.3 Reweighting-Baseline Protocols . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
D.4 Compute and Reproducibility . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
14

E Additional Experiment Results and Analysis 28
E.1 Single-Turnα-Sweep: SDPO + PH on Science Q&A . . . . . . . . . . . . . . . . 28
E.2 Multi-Turnα-Sweep: Per-Round Capability and Per-Turn Calibration . . . . . . . 28
F Prompt Templates 30
F.1 Single-Step Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
F.2 Multi-Turn Tasks . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
G Limitations and Future Work 37
H Broader Impact 38
15

A Extended Related Work and Discussion
Agent RL: from outcome rewards to process supervision.Reinforcement learning for language-
model agents has progressed from sparse outcome-only rewards (e.g., GRPO [ 33] applied at the
trajectory level) to dense, step-level supervision delivered by process reward models and structured
frameworks. OpenClaw-RL [42] provides a unified asynchronous training stack that combines binary
RL, on-policy distillation, and their composition in one rollout–score–update loop, together with a per-
turn PRM that grades each turn from the next environmental state. Buening et al. [3] push this further
by showing that raw multi-turn user interactions are already sufficient supervision for self-distillation,
eliminating the need for a separately trained reward model. Across these systems, the per-turn signal
varies considerably in fidelity and modality: rule-based binary verifiers for verifiable single-turn
tasks, learned scalar PRMs for soft multi-turn signals, and hindsight-teacher token distributions for
OPD [25, 54]. What doesnotvary is the structural property that motivates this paper: every learning
signal is computed from quantities observable only after the action is committed, and the agent’s
prospective belief at action time is invisible to the gradient. Prospective Hindsight is orthogonal to
the choice of base method, leaves the post-action signal untouched, and adds a single per-rollout
reweighting on top.
Hindsight distillation and the OPD lineage.On-policy distillation [ 1] introduced the idea of
distilling a teacher’s improved actions into the student under on-policy rollouts; subsequent work
has extended this in several directions. Ye et al. [ 44] formalize on-policy context distillation, in
which the teacher conditions on a privileged context ct that the student does not see at deployment;
Hübotter et al. [14] and Shenfeld et al. [34] develop self-distillation variants in which the teacher and
student share parameters and the privileged context is constructed on-the-fly from verified-correct
rollouts. We position PH as a complementary mechanism in this lineage. Standard OPD [25] uses
privileged information to constructbetter actionsfor the teacher, and the resulting per-token signal
is the dominant training signal. PH instead uses the gap between privileged and non-privileged
evaluationsto identify which rollouts deserve more weight, and absorbs OPD’s per-token signal into
a single per-rollout multiplier. The two mechanisms can be applied jointly without interaction: in
our multi-turn experiments PH is plugged on top of GRPO, OPD, and the OpenClaw-RL Combined
recipe with no method-specific tuning.
Calibration and self-awareness in LLMs.Modern confidence calibration in LLMs draws on sev-
eral lines of work. At the diagnostic level, Guo et al. [12] pioneered the study of miscalibrated softmax
outputs in deep networks, and Kadavath et al. [15] systematically measured whether language models
“know what they know” across knowledge tasks. Methods to elicit calibrated confidence include
verbalized confidence prompts [39, 22] and sampling-based estimators of semantic uncertainty [19];
Geng et al. [10] provide a survey. At the agentic level, Kirchhof et al. [18] argue for trajectory-level
calibration diagnostics, and a series of recent papers [8, 53, 23, 48] quantify uncertainty propagation
through multi-step trajectories; Han et al. [13] use uncertainty as an inference-time control signal.
Kalai et al. [16] take a different angle and argue that hallucination itself is incentivized by training
procedures that reward confident guesses over calibrated abstention, linking training-procedure design
to overconfidence at the model-output level. This literature largely treats calibration as a diagnostic
property to measure or to control at inference, rather than as a training signal to optimize. PH inverts
that relationship: it converts the binary self-evaluation mismatch into a per-rollout training-time
weight, and the binary Brier score of the agent’s self-evaluator coincides with the miscalibration rate
that the PH residual lower-bounds. Calibration emerges as a side effect of the same gradient steps
that drive task success, rather than as a post-hoc check or a separate auxiliary loss.
Calibration-augmented RL and the capability–calibration trade-off.A line of recent work
specifically targets the overconfidence introduced by hindsight distillation. CaOPD [50] attributes this
overconfidence to the information asymmetry between the privileged-context teacher and the student
and proposesexplicit confidence-token replacementin the teacher distribution; Leng et al. [ 21] and
Damani et al. [5] study calibration-augmented RL recipes that add explicit confidence supervision
to the loss. Across these approaches, calibration improvements typically come at the cost of a
modest capability regression, and the calibration objective is a separate term added to the base RL
loss. PH is complementary along two dimensions. First, the base method is left untouched: PH
does not rewrite confidence targets, does not add a separate calibration loss, and does not require
a calibration-specific reward model. Second, the per-rollout reweighting connects calibration and
16

capability through the surprise residual decomposition: a gradient step that reduces the base loss
on miscalibrated rollouts and a gradient step that reduces the miscalibration rate are both valid
descent directions on. Empirically, this removes the capability–calibration trade-off seen in the cited
baselines: PH preserves capability while substantially cutting OFR on single-turn and lifts both the
trajectory-averaged and best-checkpoint scores across all three multi-turn base methods.
Privileged information and prediction-error signals.Our framing of the prediction–reality gap
connects directly to Vapnik’s Learning Under Privileged Information framework [40, 30]. In LUPI,
training examples are accompanied by privileged information that is not available at deployment,
and the goal is a predictor that uses standard inputs alone. Lopez-Paz et al. [ 24] unify LUPI with
knowledge distillation, showing that distillation can be viewed as a transfer of privileged information
from teacher to student. Our agent-RL setting instantiates LUPI with (st, at) as the standard input,
yt as the target, and ct as the privileged signal. Standard OPD-style methods use ct to construct
improved actions for the teacher; PH instead uses theevaluationgap that ct creates, formalized as the
non-negative privileged-information gap I ⋆(st, at) in Proposition 1. To our knowledge this is the
first explicit use of I ⋆ as a sample-level training signal in agent RL: the surprise indicator ξt is the
per-rollout realization of I ⋆ from inside the agent’s own model, and upweighting surprising rollouts
concentrates gradient budget exactly where action-time information is insufficient.
A related but distinct line is intrinsic-motivation RL, in which prediction errors between two predictors
of the next state driveexplorationof novel states. PH differs in three ways. First, the prediction error
is computed in theoutcome / evaluationspace, not the state space, and is used for training-signal
prioritization rather than for action selection. Second, the predictor is the same model as the policy,
parameterized by the same θ and queried via a different prompt, rather than a separate frozen network.
Third, the surprise scalar is stop-gradient: it modulates the magnitude of the base gradient on the
existing on-policy rollouts but does not introduce a new gradient component of its own. The two
perspectives are complementary — one amplifies novelty in state space, the other amplifies prediction
errors in evaluation space — and we view their combination as a natural avenue for future work.
Self-correction, self-refinement, and reasoning chains.A parallel line of work uses model self-
evaluation to driveinference-timebehavior: Reflexion [ 36] and Self-Refine [26] iterate on a draft
response using a self-critic. PH operates at training time rather than inference time; the prospective
prediction is consumed once, used to compute ξt, and discarded after the gradient step. This is a
deliberate design choice: PH does not change deployment behavior, does not lengthen the agent’s
effective context, and does not require the agent to reason about its own confidence at inference.
Inference-time self-correction is therefore composable with PH (it operates on the policy distribution
after PH has shaped it), but the two mechanisms target different stages of the pipeline. A second
related line is hallucination characterization (e.g., [27, 49, 54]), which studies the conditions under
which LLMs produce unsupported content; we view PH’s reduction of overconfident-failure rate as
operating in the same regime, but at the agent-RL training-loop level rather than at the per-output
classification level.
B Theoretical Details and Proofs
B.1 Proof of Proposition 1
Fix(s t, at)and apply the law of total variance toy t with conditioning random variablec t:
Var(yt |s t, at) =E

Var(yt |s t, at, ct)

 st, at 
+ Var

E[yt |s t, at, ct]

 st, at 
=E

Var(yt |s t, at, ct)

 st, at  +I ⋆(st, at),(10)
where the second equality uses the definition of I ⋆. Both terms are non-negative, and the second
vanishes if and only if E[yt |s t, at, ct] is almost surely a function of (st, at), that is, ct provides no
additional information abouty t beyond(s t, at).□
Connection to Learning Under Privileged InformationThe decomposition in Proposition 1
places the agent RL setting of §2.1 inside the Learning Under Privileged Information (LUPI) paradigm
introduced by [40]. In LUPI, training examples are accompanied by privileged information available
17

only at training time, and the goal is a predictor that uses standard inputs alone. [30] formalize the
statistical-learning theory of this setting. [24] unify LUPI with knowledge distillation, showing that
distillation can be viewed as a transfer of privileged information from teacher to student.
Our setting instantiates LUPI with (st, at) as the standard input, yt as the target, and ct as the
privileged signal. The base methods of §2.2 use ct in different ways: GRPO uses ct only through
the scalar reward rt =R(s t, at, ct); OPD-style methods condition the hindsight teacher distribution
on ct and distill to a student that drops ct at inference. Both retain the blind spot of §2.3: training
never asks the policy to predict yt from (st, at) before ct arrives, so the privileged-information gap
I ⋆(st, at)is never measured per step. Our method (§3) makes this gap an explicit training signal.
Equivalent information-theoretic statement.Equation (3) can equivalently be expressed in
entropy form. For binaryy t, letH(y| ·) :=−E[logp(y| ·)]. Then
H(y t |s t, at)−H(y t |s t, at, ct) =I

yt;c t

 st, at  ≥0,(11)
that is, the conditional mutual information between yt and ct given (st, at) measures the same
privileged-information increment as I ⋆. The equality I(y t;c t |s t, at) = 0 characterizes the degener-
ate case in which I ⋆(st, at) = 0 for almost every (st, at): no prospective predictor can be improved
by access toc t at training time.
B.2 PH as Calibration through Reweighting: Detailed Analysis
This appendix provides the formal setup, the exact residual identity and its consequences, a gradient-
flow analysis of the PH update direction, and a discussion of the assumptions’ empirical validity. We
frame the results below asmotivationfor the calibration interpretation of PH outlined in §3.4, not as
formal guarantees of monotone calibration descent.
Setup and notation
We work in a single-step task to keep notation light; the multi-turn extension is recorded in §B.2. Let
θ∈Θparameterize a shared autoregressive model that defines:
• the policyπ θ(a|s), a conditional distribution over actionsa∈ Agiven states∈ S;
• the prospective self-evaluator peval θ (z|s, a) , a conditional distribution over evaluator outputs
z∈ {−1,0,+1}.
The verifier y is sampled from a parameter-independent kernel penv(y|s, a) with y∈ {0,1}; the
state distribution isρ 0(s). The joint rollout distribution induced byθis
ρθ(s, a, z, y) =ρ0(s)π θ(a|s)p eval θ (z|s, a)p env(y|s, a).(12)
We restrict attention to z∈ {−1,+1}; the residual z= 0 class is treated separately in App. C.4 and
contributes neutrally to all expressions below since ξt = 0 there. The surprise indicator (Eq. 4 of the
main text) is
ξ(z, y) =⊮

(z, y)∈ {OF,US}

,(13)
and we write ξt when the rollout is implicit. We assume the base loss ℓbase t (θ) is non-negative; this
is satisfied by all retrospective methods of §2.2 after additive constant shifts that do not affect the
gradient.
Surprise-weighted decomposition
Proposition 2(Surprise-weighted decomposition).For anyα≥0,
Eρθ

ℓPH t  =E ρθ  ℓbase t  +α· R(θ),R(θ) :=E ρθ  ξt ·ℓ base t  .
The surprise residual R(θ) is non-negative and vanishes if and only if ξt ·ℓ base t = 0 holds ρθ-almost
surely.
Proof. By Eq. 5 of the main text, ℓPH t = (1 +αξt)ℓ base t =ℓ base t +αξ tℓbase t . Linearity of expectation
gives the decomposition. Non-negativity of R follows from ξt ∈ {0,1}and ℓbase t ≥0 . The vanishing
condition is the standard a.s. zero condition for non-negative integrands.
18

The two pathways for residual minimization—reducing Pr[ξ= 1] (calibration) or reducing ℓbase on
miscalibrated rollouts (base-objective improvement on those rollouts)—are formalized exactly in the
next subsection.
Exact residual identity
Proposition 3(Exact residual identity).Define the agent’s miscalibration rate
M(θ) :=E ρθ

ξt

= Pr ρθ

(zt, yt)∈ {OF,US}

,(14)
and the conditional mean base loss on surprising rollouts
c(θ) :=E ρθ

ℓbase t

 ξt = 1  .(15)
Then
R(θ) =c(θ)· M(θ).(16)
Proof.By the tower rule,
R(θ) =E

ξtℓbase t  =E  ℓbase t

 ξt = 1  ·Pr  ξt = 1  =c(θ)· M(θ).
Eq. 16 is anexactidentity, not an inequality: the residual factors cleanly into a base-loss-on-
miscalibrated component c(θ) and a miscalibration-rate component M(θ). As a corollary, whenever
c(θ)≥c 0 >0 on a contiguous training window, R(θ)≥c 0 · M(θ)on that window, and minimizing
R(θ)via PH must reduceM(θ)at rate at leastc 0 relative to the rate of residual descent.
When does Eq. 16 drive calibration?The identity is most informative as a calibration lever when
both factors are non-negligible. Three regimes arise as training progresses:
• Early training. c(θ) is large (the base method has not yet learned to solve surprising rollouts)
and M(θ) is large (many rollouts are miscalibrated). Both pathways for residual minimization
are active, and PH’s surprise reweighting allocates additional gradient budget to cells where the
prediction–reality gap is widest.
• Mid training. c(θ) and M(θ) decrease together as the agent’s self-model and the base policy
co-evolve. The dual-pathway decomposition continues to hold, but the per-step weight of each
pathway shifts.
• Convergence. c(θ)→0 and M(θ)→0 jointly, R(θ)→0 , and PH and the base method share
the same fixed points (App. B.2). The identity becomes uninformative because both sides are
zero, but PH itself is no longer doing work in this regime.
The bound R(θ)≥c 0 · M(θ)is therefore not a uniform property of the optimization landscape: it
characterizes the operative training window during which PH’s calibration gains accrue.
Equivalence to the binary Brier score.For binary z′ t = (z t + 1)/2∈ {0,1} and yt ∈ {0,1},
(z′ t −y t)2 =⊮(z ′ t ̸=y t) =ξ t, so M(θ) coincides with the standard binary Brier score E[(z′ t −y t)2]
of the deterministic predictor z′ t against the verifier yt. We use the termmiscalibration ratethroughout
because it more directly conveys the operational meaning—the fraction of rollouts on which the
agent’s prospective belief disagrees with the verifier outcome—and because the experimental section
reports a one-sided projection ofMrather than the full Brier score (§B.2).
Connection to the overconfident-failure rate (OFR)
The miscalibration rate M(θ) in Eq. 14 aggregates both miscalibrated cells, OF and US, symmetri-
cally. The experimental section reports the OF-conditional projection
OFR(θ) := Pr ρθ

yt = 0

 zt = +1  = Pr[OF] Pr[CS] + Pr[OF] = Pr[OF] Pr[zt = +1] .(17)
This is a one-sided, conditional version of M focused on the OF cell, which is the dominant
miscalibration mode singled out in §2.3. The two metrics are related by
Pr[OF]≤ M(θ),OFR(θ) = Pr[OF]/Pr[z t = +1],(18)
19

so reductions in M(θ) imply reductions in Pr[OF] whenever Pr[US] does not increase, and re-
ductions in Pr[OF] imply reductions in OFR(θ) whenever Pr[zt = +1] does not collapse. Both
monotonicity assumptions hold in our experiments: the prospective predictor’s confidence rate
Pr[zt = +1] stays in a stable range across training, and the underconfident-success rate Pr[US]
remains a small fraction of M(θ) at all checkpoints. We therefore report OFR(θ) as a faithful
empirical proxy forM(θ)in §4.
Gradient-flow analysis: when is the PH update calibration-aligned?
We now characterize the direction in parameter space along which PH gradient flow moves, relative
to the negative gradient of the miscalibration rate. The result below should be read as amotivation
for why one would expect PH to reduce M(θ), not as a guarantee that it does so monotonically in
every step.
Let uPH :=−∇ θEρθ [ℓPH] and ubase :=−∇ θEρθ [ℓbase] denote the PH and base update directions.
By Prop. 2,
uPH =u base −α∇ θR(θ).(19)
Score-function decomposition of ∇θR.Applying the score-function trick to R(θ) =E ρθ [ξtℓbase t ],
∇θR(θ) =E ρθ [ξt∇θℓbase t ]| {z }
base-loss descent on{ξ=1}
+E ρθ [ξtℓbase t ∇θ logρ θ]| {z }
distributional shift inξ
,(20)
where ∇θ logρ θ =∇ θ logπ θ(a|s) +∇ θ logp eval θ (z|s, a) , since ρ0 and penv are parameter-free.
Similarly,
∇θM(θ) =E ρθ [ξt∇θ logρ θ].(21)
Theorem 4(PH gradient under uniform-loss assumptions).Let ¯ℓ(θ) :=E ρθ [ℓbase t |ξ t = 1] =c(θ)
andδ(θ) := Var ρθ, ξt=1[ℓbase t ]. SupposeE[ξ t∥∇θ logρ θ∥2]<∞. Then
uPH =u base −α·E ρθ [ξt∇θℓbase t ]−α ¯ℓ(θ)· ∇θM(θ) +r(θ),(22)
where the remainderr(θ)satisfies
∥r(θ)∥ ≤α
p
δ(θ)·
p
E[ξt∥∇θ logρ θ∥2].(23)
In the limit δ(θ)→0 (the base loss is constant on surprising rollouts), the PH update direction differs
from the base direction by exactly a −α¯ℓ· ∇θM(θ) component plus a base-loss descent component
on the miscalibrated set.
Proof.Decompose the second term of Eq. 20 via the identity
E[ξtℓbase t ∇θ logρ θ] = ¯ℓ·E[ξ t∇θ logρ θ] +E  ξt(ℓbase t − ¯ℓ)∇θ logρ θ  .
The first term equals ¯ℓ·∇ θM(θ) by Eq. 21. The second term is bounded in norm by Cauchy–Schwarz:
E[ξt(ℓbase t −¯ℓ)∇θ logρ θ]  ≤ q Varξt=1[ℓbase t ]· p E[ξt∥∇θ logρ θ∥2] = p δ(θ)· p E[ξt∥∇θ logρ θ∥2],
which gives Eq. 23 after multiplication by α. Substituting back into Eqs. 20 and 19 yields Eq. 22.
Remark1 (Empirical magnitude of the remainder).The remainder bound in Eq. 23 is not an
assumption but a quantity measurable from training logs. We define the relative remainder
ρ(θ) :=
p
δ(θ)
c(θ) =
q
Varξt=1[ℓbase t ]
Eξt=1[ℓbase t ] ,(24)
the coefficient of variation of the base loss conditional on ξt = 1. Theorem 4 is most informative
when ρ(θ) is small; the limit ρ(θ)→0 recovers the uniform-loss case in which the leading term
−α¯ℓ· ∇θMdominates the remainder.
20

Calibration alignment, qualified.Taking the inner product of Eq. 22 with−∇ θM(θ)gives

uPH,−∇ θM(θ)  =
ubase,−∇ θM(θ) 
+α ¯ℓ(θ)· ∥∇θM(θ)∥2
−α

E[ξt∇θℓbase t ],−∇ θM(θ) 
+⟨r(θ),−∇ θM(θ)⟩.(25)
Among the four terms on the right-hand side, the second is the leading calibration-aligned term and is
non-negative; the fourth is bounded by α
p
δ(θ)·
p
E[ξt∥∇θ logρ θ∥2]· ∥∇θM(θ)∥ via Eq. 23. The
third term is a base-loss descent component on the miscalibrated set; its inner product with−∇θM is
sign-indeterminate in general, but in policy-gradient base losses ∇θℓbase t is bounded by the per-batch
advantage normalization of §2.2, so its contribution scales with the magnitude of the base advantage.
The PH update direction is thereforebiased toward −∇θM(θ) rather thanexactly alignedwith
it. Whether this bias is large enough to drive monotone descent on M(θ) depends on the relative
magnitudes of the four terms in Eq. 25, which are themselves a function of the training step. We do
not claim monotone descent; we claim that the leading term provides a calibration-aligned restoring
force that is consistent with the empirical observation in §4 that OFR(θ) decreases monotonically
under PH training.
Scope and limitations of the alignment claim.We make four honest qualifications. First, The-
orem 4 is an exact identity, but the calibration-alignment interpretation that follows it requires the
leading ¯ℓ· ∇θM term to dominate the remainder—i.e., ρ(θ) to be small relative to ¯ℓ/∥∇θM∥.
Second, the E[ξt∇θℓbase t ] term has indeterminate sign relative to −∇θM(θ), and we do not claim it
contributes to calibration descent. Third, the analysis is gradient-flow, not finite-step SGD: under
standard learning-rate and smoothness assumptions, the conclusions hold approximately for finite
steps with higher-order corrections, but we have not derived sharp rates. Fourth, the analysis is
per-step: it does not compose across the trajectory of training to yield a convergence-rate result on
M(θ).
We therefore frame Theorem 4 as amotivationfor why PH’s update direction would be expected to
reduce M(θ), not as a guarantee that it does so. The empirical observation that OFR(θ) decreases
monotonically under PH training across all base methods and tasks in §4 is then evidence that the
motivation translates into practice, rather than a derivation of that fact.
Discussion
Single-step versus multi-turn.The arguments above treat each rollout as a single (s, a, z, y)tuple.
In multi-turn settings, the per-turn surprise ξt is computed from (zt, yt) at turn t, and the joint
distribution ρθ extends to a sequence over turns. Prop. 2 extends turn-by-turn (linearity of expectation
across turns), and Theorem 4 applies at each turn under the same assumptions; the per-turn alignment
is then aggregated over the trajectory. The remainder bound in Eq. 23 is typically larger in multi-turn
settings because the per-turn variance of the base loss is amplified by stochasticity in the LLM-based
PRM judge (App. D.2).
Tabular versus neural-network policies.Theorem 4 is stated as an exact gradient-flow identity
modulo the explicit remainder r(θ). For finite-step gradient descent with neural-network policies, the
conclusion holds approximately under standard learning-rate, smoothness, and Lipschitz assumptions,
with equalities replaced by inequalities up to higher-order terms in the learning rate.
Asymptotic behavior.As θ converges, both ℓbase and ξ approach zero on the support of ρθ, so
c(θ)→0 , M(θ)→0 , and R(θ)→0 . By Prop. 2, PH and the base method share the same fixed
points; PH differs only in the optimization trajectory leading up to convergence, in which additional
gradient budget is allocated to surprising rollouts via Eq. 16. The miscalibration rate also vanishes
asymptotically, consistent with calibration being achieved at convergence.
Relation to existing calibration losses.The miscalibration rate M(θ) is the binary specialization
of mean-squared-error calibration (the Brier score). Expected Calibration Error (ECE), defined for
predictors that emit confidence p∈[0,1] , coincides with M(θ) when predictions are binarized
21

via thresholding. Negative Log-Likelihood of the prospective evaluator is a different but related
calibration objective; PH does not directly minimize NLL, but does so implicitly through the
parameter-sharing channel that couples the policy and evaluator gradients. Among these losses,
M is the one most naturally connected to the PH update rule, since PH’s reweighting is itself an
indicator-weighted scheme. The OF-conditional projection OFR(θ) used in our experiments (Eq. 17)
is a one-sided form ofMtailored to the OF-focused narrative of §2.3.
C Algorithm and Implementation Details
C.1 Base Method Advantage Formulations
We give the explicit advantage formulations of the three retrospective base methods abstracted as
ℓbase in §2.2.
GRPO [33].For a group of G rollouts {(st, a(g) t , r(g) t )}G g=1 sharing the same query, the per-rollout
advantage is
AGRPO t = rt −¯r σr +ϵ ,(26)
where ¯r= 1 G P g r(g) t and σr is the group standard deviation; ϵ >0 is a small constant for numerical
stability.
OPD [1, 44, 14].The privileged context ct (in multi-turn, ct =s t+1) is used to construct a hindsight
teacher conditioned on(s t, ct), whose per-token action distribution is distilled into the student:
AOPD t,j = logπ θ(at,j |a t,<j, st, ct)−logπ θ(at,j |a t,<j, st),(27)
wherea t,j is thej-th token ofa t anda t,<j is its prefix.
Combined [42].The combined advantage sums the scalar and token-level signals:
Acomb t,j =w rlAGRPO t +w opdAOPD t,j ,(28)
withw rl =w opd = 1in our experiments.
In all three cases, the per-rollout (or per-token) base loss ℓbase t is the policy-gradient surrogate of the
corresponding advantage; the precise form does not affect any analysis in §2–§3.
How PH wraps each base method.PH’s per-rollout reweighting in Eq. 5 preserves all internal
structure of the base advantage. For GRPO, the group normalization σr is computed on the original
rewards rt, not the surprise-weighted loss. For OPD, the per-token signal AOPD t,j is aggregated as in
the base method; PH then multiplies the resulting per-rollout (single-turn) or per-turn (multi-turn)
loss by (1+αξt). The surprise scalar is broadcast across action tokens within the rollout/turn, which
is the operation that absorbs OPD’s per-token signal into the per-rollout reweighting.
C.2 PH Algorithm Details
Algorithm 1 states the end-to-end training step. Inside any base method of §2.2, PH inserts three
operations into each rollout step: (i) draw M samples from the prospective self-evaluator and
aggregate them by majority vote (§3.1); (ii) compute the surprise indicator ξt from the resulting zt
and the verifier outcome yt (§3.2, §3.3); (iii) multiply the base per-rollout loss by 1 +αξ t (§3.3).
The base optimizer then updates the parameters using the resulting PH loss; the rollout sampling
distribution, the group reward normalization, the per-token aggregation in OPD, and any auxiliary
regularizer inℓ base are all unchanged.
Cost.The only additional compute cost relative to the base method is M prospective forward passes
per rollout step (line 5 of Algorithm 1). With shared parameters between the action policy and the
self-evaluator, no extra trainable parameters are introduced, so PH does not change the memory
footprint of the base method beyond the storage of zt and ξt per step. With M= 1 , the prospective
overhead is one extra forward pass per step. The verifier and privileged-context computations on line
22

Algorithm 1Prospective Hindsight (PH) training step.
Require: parameters θ, batch of prompts {xb}B b=1, base method (GRPO, OPD, or Combined),
hyperparametersα≥0andM≥1
1:foreach promptx b,b= 1, . . . , Bdo
2:foreach step (or turn)tof the rolloutdo
3:a t ∼π θ(· |st)▷base method’s action sampling
4:form= 1, . . . , Mdo
5:z (m) t ∼p eval θ (· |st, at)▷Eq. 3.1, prospective forward pass
6:end for
7:z t ←maj

z(1) t , . . . , z(M) t 
8:Receivec t andy t from environment and verifier
9:ξ t ←⊮

(zt, yt)∈ {OF,US}

▷Eq. 4
10:Computeℓ base t (θ)following §2.2
11:ℓ PH t ←  1 +α·ξ t  ·ℓ base t (θ)▷Eq. 5
12:end for
13:end for
14:θ←optimizer_step

θ,∇ θ
P
b, tℓPH t  ▷ ξt is stop-gradient
15:returnθ
8 are inherited unchanged from the base method, since the retrospective methods of §2.2 already
require them. PH thus adds a single training-time hyperparameter α and a single inference-time
hyperparameterMon top of the base method.
Special cases.Two boundary cases are useful for sanity checks. First, α= 0 collapses Algorithm 1
into the base method exactly, since 1 +αξ t = 1 for all t. Second, M= 1 removes the majority vote
and uses a single prospective sample per rollout step, which is the configuration in all our single-turn
experiments.
C.3 Discrete and Continuous PH Gates
The PH update rule of Eq. 5 weights the base loss by wt = 1 +α ξt for a non-negative surprise
scalar ξt. We use two concrete realizations of ξt, depending on whether the retrospective signal
is deterministic or stochastic; both share the same shape wt ∈[1,1 +α] and the same asymptotic
behaviourw t →1as the prospective belief and the realized outcome agree.
Discrete gate (single-turn).With a rule-based binary verifier yt ∈ {0,1}and a single ternary
prospective sample zt ∈ {−1,0,+1}(M=1, App. D.1), the surprise indicator is the binary cell
membership of Eq. 4,
ξdisc t =⊮  (zt, yt)∈ {OF,US}  ∈ {0,1}, w t = 1 +α ξdisc t ∈ {1,1+α}.(29)
Honest-uncertainty rollouts (zt = 0) are folded into ξt = 0 to preserve the neutral-class semantics of
§C.4, sow t = 1on{z t = 0}.
Continuous gate (multi-turn).With an LLM-based per-turn PRM judge that emits an aggregated
turn score rt ∈ {−1,0,+1}and M predictor samples averaged into ¯zt ∈[−1,+1] (App. D.2), we
use the continuous relaxation
ξcont t = 1 2

¯zt −r t

 ∈[0,1], w t = 1 +α ξcont t ∈[1,1+α].(30)
The factor 1 2 rescales the maximum disagreement |¯zt −r t|= 2 (i.e., ¯zt = +1, rt =−1 or vice versa) to ξt = 1. Eq. 30 reduces to Eq. 29 on the corners of the (¯zt, rt) grid: when both ¯zt ∈ {−1,+1}
and rt ∈ {−1,+1}, ξcont t =ξ disc t . Intermediate values of ¯zt encode predictor uncertainty (averaged
over M samples) and intermediate values of rt encode PRM-judge uncertainty; the continuous gate
carries this uncertainty through tow t rather than collapsing it to{0,1}.
Self-extinguishing curriculum.Both gates share the limiting behaviour wt →1 as ξt →0 , i.e.,
as the prospective belief and the realized outcome converge. This is the mechanism behind the
23

empirical PH-weight decay reported in Figs. 2 and 7: as training closes the prediction–reality gap,
the prospective signal naturally fades and the PH loss reduces to the base loss. By Proposition 2, the
surprise residual R(θ)→0 in the same limit, so PH and the base method share the same fixed points
(App. B.2).
Implementation flag.A single training-time flag SURPRISE_MODE selects between the two gates.
Setting SURPRISE_MODE=discrete uses Eq. 29; setting SURPRISE_MODE=continuous uses Eq. 30.
The single-turn experiments of §4.2 use the discrete gate; the multi-turn experiments of §4.3 use
the continuous gate. All other PH-side hyperparameters (α, M, weight clip) are independent of this
choice.
C.4 Honest Uncertainty: Thez t = 0Class
The prospective self-evaluator of §3.1 is prompted to return a ternary score zt ∈ {−1,0,+1}; the
value zt = 0 encodeshonest uncertainty: an explicit signal that the agent’s prospective belief about
yt from(s t, at)alone is inconclusive. This appendix records our handling of this residual class.
Treatment as a neutral class.Rollouts with zt = 0 inherit the gradient invariance of Eq. 2 but
do not fit the four-cell calibration taxonomy of Table 1, because the agent has not committed to a
directional prediction. The PH update rule (§3.3) assigns weight 1.0 to all such rollouts, matching
the weight given to the calibrated cells (CS, AF) so that zt = 0 neither amplifies nor dampens the
base loss.
Tie-breaking under majority vote.When M >1 samples in Eq. 3.1 produce a strict majority for
one of {−1,+1} , we use that value. Under a tie, or when all M samples are unparseable (e.g., the
model fails to emit a valid \boxed{·} field), we default to zt = 0. This conservative rule prevents
PH from amplifying ambiguous rollouts and folds parsing failures into the neutral class.
Empirical frequency.Across our main experiments, zt = 0 accounts for a small minority of
rollouts in both single-step and multi-turn settings, with the exact rate varying by task and model.
The frequency is largely independent of the base method (GRPO, OPD, Combined) and decreases as
M increases in the majority vote, since aggregating over multiple samples collapses borderline cases
toward the dominant prediction.
D Additional Experimental Setup
This appendix expands §4.1 with all information needed to reproduce our experiments. §D.1 covers
the single-turn verifiable tasks (Science Q&A and Tool Use) built on top of the SDPO [14] backbone,
and §D.2 covers the multi-turn personal agent built on top of the OpenClaw-RL [42] framework. §D.4
summarizes compute, software environment, and code release. The two regimes differ along one
important axis —single-turn uses a rule-based binary verifier with no learned reward model, while
multi-turn uses an OLMo-3-7B-Instruct PRM judge— which explains the configuration differences
below.
D.1 Single-Turn Verifiable Tasks
Setting in one sentence.Each rollout is a single prompt x and a single model response a, with a
rule-based verifier R(x, a)∈ {0,1}that returns binary correctness and no auxiliary reward model;
this is the simplest possible instantiation of PH (single prediction, single outcome,T=1 , deterministic
retrospective signal).
Datasets and verifiers.We use the Chemistry subset of SCIKNOWEVAL[ 9] following the released
CaOPD [50] preprocessing. Each prompt asks the model to reason step-by-step and emit a single letter
ˆy∈ {A, B, C, D}; the verifier is rule-based, R(x, a)=1iff the parsed letter equals the gold answer.
We also use the Tool Use split derived from TOOLALPACA[ 38] as preprocessed in CaOPD; each
prompt provides API documentation in a ReAct-style template and the verifier checks (a) the action
name matches the gold tool and (b) the JSON arguments match the gold schema under canonical
normalization. Both training sets contain4–5k prompts; we evaluate on the corresponding test split.
24

Together they probe both knowledge-intensive reasoning (Science Q&A) and structured agentic
prediction (Tool Use), and were the two domains used in CaOPD, which lets our calibration numbers
be directly compared against theirs.
Backbone OPD method (SDPO) and privileged-context construction.We build the single-
turn experiments on top of SDPO [ 14], using the official codebase as modified in CaOPD [ 50].
SDPO is an on-policy self-distillation method: the same model serves as both student πθ(·|x) and
teacher πθ(·|x, z), where z is a privileged context not available at deployment. We use the SDPO
“correct-solution” mode of CaOPD: for each prompt, after the rollout phase, one verified-correct
rollout a⋆ is chosen on-the-fly and inserted as z, so the teacher is then asked to “Correctly solve
the original question” conditioned on (x, z). The training loss is per-token reverse KL between
student and teacher on the teacher trajectory, with rollout importance sampling correction and SDPO
defaults (top-K=100 distillation, EMA teacher update rate 0.05, IS clip 2); thinking mode is disabled
(enable_thinking=false) so that the trajectory we distill is the answer trajectory.
Models, training framework, and hardware.Backbones areOLMo-3-7B-Instruct[ 29] (primary,
both Science Q&A and Tool Use) andgpt-oss-20B[ 2] (scale ablation). Both are used as student and
EMA-teacher (the EMA teacher is the same model with the privileged context z). We deliberately
keep the verbalized-confidence template of CaOPD intact so that PH plugs in cleanly: each rollout still
ends with a parseable Confidence: {x} token, but PH ignores this string and uses only the binary
verifier outcome R(x, a)as the retrospective signal. The codebase forks CaOPD’s SDPO branch,
implemented on top ofverl[ 35] with PyTorch FSDP2 for sharded optimizer state andvLLM[ 20]
for batched rollout generation; our PH plug-in adds (i) a per-prompt prospective prediction call,
(ii) a stop-gradient weight w(ξt) on the per-rollout reverse-KL contribution, and (iii) lightweight
surprise/OFR bookkeeping in the training logger. Each run uses one node of p5en.48xlarge (8×
NVIDIA H200), which is sufficient for both 7B and 20B-MoE training under FSDP2.
Prospective Hindsight plug-in.For each rollout, after the student emits its answer a but before the
verifier evaluates R(x, a), we issue an additional generation call to the same student model with a
different prompt that strips the verbalized-confidence instruction and asks the model to predict whether
its previous answer is correct, incorrect, or uncertain. The exact predictor template is given in App. F.
Because the verifier here is rule-based and deterministic, a single ternary predictionzt ∈ {−1,0,+1}
per rollout already gives a low-variance signal, so we use M=1 predictor sample (no majority vote).
Predictor generation is capped at max_new_tokens= 128 tokens at temperature 0.6, top-p=0.95;
un-parseable outputs are treated asz t=0(uncertain). The surprise indicator and weight are
ξt =1

(zt, yt)∈ {OF,US}

, w t = 1 +αξ t,
with α=1.0 default and clip wt ∈[0.5,2.0] as a safety net (the unclipped weight is in {1,2} already,
so the clip is rarely active). The weight is a stop-gradient scalar and multiplies the SDPO per-rollout
reverse-KL loss; no gradient flows back through the predictor.
Hyperparameters.Table 5 reports the hyperparameters for all single-turn runs. All values are
taken either from the CaOPD defaults or from a one-shot tuning on a held-out validation slice; no
hyperparameter is tuned per-method (the same configuration is used for SDPO, SDPO + PH, and the
α-sweep ablation).
Evaluation protocol and metrics.Capability is reported as mean@16: for each held-out test
prompt we sample Kval=16 rollouts at temperature 0.6, top-p=0.95, evaluate the verifier on each,
and report the mean accuracy. From the same Kval=16 rollouts we compute, per prompt and then
averaged across the test set, (i) the surprise rate cM= Pr[ξ t=1], (ii) the overconfident-failure rate
Pr[yt=0|z t=+1], and (iii) the honest-uncertainty rate Pr[zt=0] (App. C.4, where we verify that the
neutral cell does not collapse under PH). All headline numbers are mean±std over 3 seeds, reported
at the end of epoch 3; the α-sweep additionally logs per-step trajectories of mean@16 and OFR
(App. E.1).
D.2 Multi-Turn Personal Agent
Setting in one sentence.A trained student model serves as an OpenAI-compatible chat agent
inside the OpenClaw runtime; an external LLM “user” (GPT-4.1) drives multi-turn math-tutoring
25

conversations grounded in GSM8K, an OLMo-3-7B-Instruct PRM judges each main-line turn, and
PH attaches a per-turn surprise signal to the OpenClaw-RL training loop.
Task and agent design.We follow the personal-agent track of OpenClaw-RL [ 42] verbatim.
At each training round we alternate between two scenarios: (i) aStudentscenario in which the
simulated user is a “lazy student” who needs the agent to solve a math problem in a non-AI-style
tone (no bold, no bullet points); the student writes the problem tohomework/i.txt, asks the agent
to solve, critiques the style, and ends with the literal sentinel DONE once satisfied; and (ii) aTeacher
scenario in which the simulated user is a strict math teacher who wants warm, specific, prose-only
grading comments. The agent has access to the OpenClaw runtime’s standard file-I/O tools but
only text generation is exercised in this benchmark. Each session is one (problem, scenario) pair
with up to Tmax=48 turns, ending whenever the simulator emits DONE; turns inside a session are
tagged turn_type=main (used for training) or turn_type=side (eval-only). We split GSM8K into
disjoint training and evaluation pools (offsets 36:∞ training; 0:36 student-eval, 0:24 teacher-eval),
withsessions_per_round=2and16training rounds.
User simulators and conversation protocol.The simulators are GPT-4.1 calls (temperature 0)
with the system prompts taken verbatim from the OpenClaw-RL evaluation script; the full strings
are reproduced in App. F. The salient content of theStudentprompt is: “You are role-playing as a
lazy student who knows nothing. . . If the AI’s answer has stuff like bold text, numbered lists,Final
answer:, or anything too AI-like, tell it to rewrite. . . After the AI shows you a satisfactory version,
say exactly:DONE.” TheTeacherprompt asks for warm, specific, prose-only grading comments and
ends similarly with DONE. The first user message in each scenario is templated from the GSM8K
problem and (for the Teacher scenario) the gold answer.
Base method: Combined (Binary RL + OPD).The default base method we plug PH into is the
Combinedrecipe of OpenClaw-RL [ 42]; we also evaluate Binary RL only and OPD only as ablations.
For each main-line turn the PRM judge produces a scalar score rt ∈ {−1,0,+1}from the next-state
signal (the simulator’s reply); GRPO advantages are computed within the trajectory with mean and
standard deviation across the same session, with disable_rewards_normalization so that the
per-turn scale of rt is preserved. The OPD component uses the same model conditioned on a textual
hint extracted from the next-state signal; the teacher’s per-token log-probability gap with the student
forms the token-level directional advantage AOPD t,j (EMA teacher tracking rate 0.05). The combined
per-turn advantage is Acomb t =w rlAGRPO t +w opdAOPD t with wrl=wopd=1; the PPO surrogate uses
asymmetric clipε lo=0.2,ε hi=0.28from GRPO [33] andkl_loss_coef= 0.
PRM judge and OPD hindsight teacher.Both the PRM and the OPD teacher share weights
with the student (full self-distillation): they all run OLMo-3-7B-Instruct, served by sepa-
rate sglang engines (separate from the rollout engine) so they do not block training. We
use prm_num_gpus=1, prm_teacher_num_gpus=1, prm_m=1 (PRM majority vote; we ablate
prm_m=3), prm_temperature=0.6, prm_max_new_tokens=2048, and the OPD teacher source
ismegatronso that the teacher distribution is on-policy with the actor.
Training framework: Slime + Megatron-LM.We use the asynchronous 4-component training
loop of OpenClaw-RL [42], implemented on slime (RL orchestrator) and Megatron-LM (training
backend), with sglang serving rollouts/PRM/teacher. The 8 GPUs of one p5en.48xlarge node
split as: 4 GPUs for the actor (TP=4, sequence-parallel, bf16); 2 GPUs for rollout (one engine per
GPU, TP=1); 1 GPU for the PRM judge; 1 GPU for the OPD teacher. PH inserts a per-turn predictor
call between the actor’s response and the PRM’s score; in the asynchronous regime the predictor
runs concurrently with PRM scoring (neither reads the next-state signal), so PH adds essentially
zero wall-clock overhead in steady state. Each session writes a JSONL record of ( session_id,
turn_index, turn_type, prm_score, prospective_score, surprise, weight_version) to
disk, allowing offline reconstruction of all calibration metrics.
Prospective Hindsight plug-in.For each main-line turn t, after the agent emits its response at
but before the PRM scores it, we issue an additional generation request to the same actor with a
prompt that asks the model to predict whether its own response in the current dialog state will be
judged correct/incorrect/uncertain by an external judge. The predictor sees (s1:t, at) but never the
26

simulator’s reply st+1.Because the per-turn PRM signal is itself an LLM-based score and therefore
stochastic, we use M=3 predictor samples, parsed to {−1,0,+1} and averaged into a continuous
¯zt ∈[−1,+1].We then use the continuous PH gate (App. C.3):
ξt = 1 2

¯zt −r t

 ∈[0,1], w t = 1 +αξ t,
where rt ∈ {−1,0,+1} is the PRM-aggregated turn score. The implementation flag is
SURPRISE_MODE=continuous; setting SURPRISE_MODE=discrete recovers the binary ξt ∈
{0,1} used in single-turn experiments. The weight applies to the per-turn combined ad-
vantage Acomb t before the PPO surrogate (equivalently, broadcast across all tokens of at
since the surprise is a turn-level scalar) and is a stop-gradient constant. PH-specific knobs:
PROSPECTIVE_M=3, PROSPECTIVE_MAX_TOKENS=256, SURPRISE_ALPHA=1.0 default, no weight
clip (SURPRISE_WEIGHT_MAXunset; the gate already givesw t ∈[1,1+α]).
Hyperparameters.Table 4 reports the hyperparameters for all multi-turn runs. The same con-
figuration is used for the Combined baseline, Combined + PH, and the α-sweep ablation; only the
PH-specific rows differ across rows of Table 3.
Evaluation protocol and metrics.We use the personalization evaluator of OpenClaw-RL [ 42]
(script personalization_evaluator.py). For each held-out evaluation prompt we collect a single
first response (turn 1, no follow-up) at temperature0.3, and score it with GPT-4.1 against a fixed prefer-
ence template that requests a boxed score from {0,0.25,0.5,0.75,1} at temperature 0 with Nvotes=3
parallel votes whose successful boxed scores are averaged. The user-side preference text is one of
PREFERENCE_STUDENT (no AI-style formatting; full reasoning shown) or PREFERENCE_TEACHER
(warm, specific, prose-only grading comments); the full strings are in App. F. Capability is the mean
evaluator score across the eval pool, reported separately for Student (N=36) and Teacher (N=24)
plus the macro-average. We define multi-turn OFR as the per-turn analogue Pr[rt ≤0|z t=+1],
computed from the per-turn JSONL bookkeeping over the held-out eval pool, and additionally report
surprise rate cM= Pr[ξ t >0] and prospective accuracy. Headline numbers are reported at the final
checkpoint of round 16; dynamics plots evaluate every 4 weight updates.
D.3 Reweighting-Baseline Protocols
To isolate the contribution of PH’s surprise-based selection from the contribution of additional gradient
mass, we compare PH against two reweighting controls in the single-turn setting (Table 2). Both use
the same multiplier (1+α) as PH and are detached from the computation graph (stop-gradient); only
the rule forwhichrollouts receive the multiplier differs.
Random reweighting.At each training step, we compute the empirical fraction pt of surprising
rollouts the PH protocol produces on the same data. We then sample uniformly at random a subset
of size ⌊pt ·N⌋ from the current batch and assign these rollouts weight (1+α); the remaining
rollouts retain weight 1. By construction this matches PH’s per-step total weight P i(1 +α·ξ (i) t ), so the only difference between Random and PH is thelocationof the upweighted mass: uniform vs.
surprise-targeted. Selection seeds are derived from hash(rollout_id, step) so that within an
epoch each rollout receives a deterministic weight; we use α=1.0 throughout, matching the headline
PH configuration.
Failure-only reweighting.For every rollout with verifier outcome yt=0, we set the weight to
(1+α); rollouts with yt=1 retain weight 1. This corresponds to upweighting cells OF∪AF in the
calibration taxonomy (Table 1), as opposed to PH’s OF∪US . We again use α=1.0. Failure-only
therefore differs from PH in exactly two cells: it includes AF (calibrated incompetence, which PH
leaves unweighted) and excludes US (underconfident successes, which PH amplifies).
What each baseline controls for.Random isolates the effect ofselection: any gain of PH over
Random must come fromwhichrollouts are upweighted, not from how much weight is added.
Failure-only matches PH on the dominant single-turn cell (OF; see Figure 5) but differs on the
smaller cells, isolating whether the prospective signal zt contributes information beyond the verifier
outcome yt alone. The empirical comparison is reported in Table 2 and discussed in §4.2; the PH-cell
composition over training is shown in Figure 2.
27

D.4 Compute and Reproducibility
Hardware and software.Both single-turn and multi-turn experiments run on a single node of
p5en.48xlarge (8× NVIDIA H200). Multi-node is supported by the underlying frameworks (verl /
Slime) but not used in our reported runs. Software: CUDA 12.x , PyTorch 2.5+ , vLLM for single-
turn rollouts, sglang for multi-turn rollouts/PRM/teacher, Megatron-LM (multi-turn actor backend),
slime(multi-turn async orchestrator),verl(single-turn orchestrator).
Wall-clock and overhead from PH.Single-turn(3 epochs, 32 prompt batch, K=8 rollouts): ∼8
hours per run on Science Q&A, ∼6 hours on Tool Use; the PH plug-in adds ∼6% wall-clock
overhead from the predictor calls (amortized into the same vLLM batch).Multi-turn( 16 rounds,
2 sessions/round, Tmax=48): ∼4 hours per run; the PH plug-in adds essentially zero wall-clock
overhead because the predictor runs concurrently with the PRM in the asynchronous loop.
E Additional Experiment Results and Analysis
This appendix expands the experiments of §4.2 (single-turn SDPO + PH on Science Q&A and Tool
Use) and §4.3 (multi-turn RL / OPD / Combined + PH) with the fullα-sweeps that the main tables
abridge, finer-grained training-time dynamics, and per-turn breakdowns. All configurations match
App. D unless stated otherwise.
E.1 Single-Turnα-Sweep: SDPO + PH on Science Q&A
PH cell composition is qualitatively robust across α.Figure 6 repeats the per-step cell-
composition plot of Figure 2 (which fixes α=1.0) for the additional weights α∈ {0.1,0.25,0.5,2.0}
on Science Q&A. The four panels share a common pattern: the overconfident-failure (OF) cell shrinks
throughout training while the confident-success (CS) cell grows, and the underconfident-success (US)
and aware-failure (AF) cells stay small. The fact that this dynamics holds essentially unchanged
across two orders of magnitude of α tells us that PH is not a delicate optimization-noise instrument:
it is a structural reweighting whose direction (compress OF, grow CS) is set by the data, with α
controlling only the speed of that compression.
OFR decreases monotonically and the PH weight self-extinguishes.Figure 7 (left) plots OFR
over training for each α on Science Q&A. All five trajectories descend monotonically;α=0.5 reaches
one of the lowest late-stage OFR values, consistent with the main-text observation in §4.2. Figure 7
(right) plots the corresponding mean PH weight E[wt]: it starts above 1 (because ξt >0 on many
rollouts initially), decays toward 1 as ξt →0 on the bulk of rollouts, and the larger theα the higher the
initial weight but also the steeper the relaxation. The weight curriculum is therefore self-extinguishing
— exactly the behaviour predicted by the continuous-relaxation analysis of App. C.3.
Why α=0.5 is the Science Q&A sweet spot.Table 6 numerically compares the five α values
along three axes: late-training OFR, the early-to-late OFR drop, and the verifier pass rate at the
final checkpoint. α=0.5 is best on all three: largest absolute OFR drop ( 0.560), largest relative
drop (72.9%), and highest final verifier pass rate (73.2%). The weight column shows why: α=0.5’s
mean weight starts at 1.35 (large enough to materially reweight miscalibrated samples) and anneals
to 1.09 (small enough to not perturb late-stage learning), giving the cleanest curriculum. α=1.0
and α=2.0 start the curriculum from much higher initial weights (1.67,1.68 ) and do not anneal as
cleanly, trading a fraction of the calibration improvement for slightly noisier capability. Conversely,
α∈ {0.1,0.25}are nearly identity reweightings throughout training (initial weight 1.07,1.17 ) and
so leave the OFR drop close to the small-αfloor of≈0.49.
E.2 Multi-Turnα-Sweep: Per-Round Capability and Per-Turn Calibration
α sweep across capability and per-turn calibration.Figure 8 plots the multi-turn α-sweep on
the Combined base method under the GPT-4.1 simulator: teacher-side score across training rounds
(left), per-turn surprise rate across conversation turns (middle), and per-turn OFR across conversation
turns (right). The capability trajectory (left) reproduces the headline of Table 3: α=1.0 rises fastest
and plateaus highest, α=0.5 tracks closely, and α=2.0 exhibits the highest round-to-round variance.
28

0 20 40 60 80 100 120 140 160
Training step
0%
20%
40%
60%
80%
100%Rollout share
PH composition (alpha=0.1) CS OF US AF
0 20 40 60 80 100 120 140 160
Training step
0%
20%
40%
60%
80%
100%Rollout share
PH composition (alpha=0.25) CS OF US AF
0 20 40 60 80 100 120 140 160
Training step
0%
20%
40%
60%
80%
100%Rollout share
PH composition (alpha=0.5) CS OF US AF
0 20 40 60 80 100 120 140 160
Training step
0%
20%
40%
60%
80%
100%Rollout share
PH composition (alpha=2.0) CS OF US AF
Figure 6:PH cell composition across α on Chemistry.Per-step decomposition of training rollouts
into CS / OF / US / AF for α∈ {0.1,0.25,0.5,2.0} (the α=1.0 panel is in Figure 2). The compress-
OF / grow-CS pattern is qualitatively unchanged across two orders of magnitude ofα.
0 30 60 90 120 150 180
RL step
0%
20%
40%
60%
80%OFR = OF / (CS + OF)
5-step bins + EMA smoothing=0.75
Overconfident failure rate
0 30 60 90 120 150 180
RL step
1.0
1.2
1.4
1.6
1.8Mean PH weight
dashed line: no reweighting
Mean PH weight
α=0.1
α=0.25
α=0.5
α=1.0
α=2.0
Figure 7:OFR and PH-weight dynamics across α on Science Q&A.Left: OFR over training for
each α; all five trajectories descend monotonically. Right: the mean PH weight starts above 1 and
anneals toward1asξ t →0(App. C.3). Faint lines: 5-step bins; solid lines: EMAs.
The per-turn surprise (middle) and per-turn OFR (right) reveal a structural pattern that the trajectory-
averaged metrics in the main text do not surface:later turns have higher initial overconfidence,
consistent with the long-horizon credit-assignment intuition that the agent’s self-model is least
developed for late, context-saturated turns; and PH compresses exactly this region most. At α=1.0,
late-turn OFR drops to levels comparable to the early-turn OFR of the baseline, effectively flattening
the per-turn calibration profile.
When α=2.0 overshoots in long horizons.Figure 8 also concretizes the α=2.0 caveat from
§4.3: the right panel shows that α=2.0 achieves the lowest per-turn OFR overall, but the left panel
shows that its capability oscillates round-to-round and ends below α=1.0. The mechanism is the
variance-amplification effect quantified in App. B.2: very large α multiplies the per-rollout combined-
advantage by up to 1 +α= 3 on miscalibrated rollouts, and in long-horizon training those rollouts
also tend to be the longest token sequences (overconfident failures are correlated with more aggressive
generation), so the per-batch gradient norm spikes relative to the baseline distribution. We did not
observe this regime in single-turn (Table 2) because the per-rollout token count there is bounded and
similar across all rollouts; the multi-turn regime, with its variable-length sessions of up to Tmax=48
turns (App. D.2), exposes it.
Practitioner recommendation.For both regimes, a single α=1.0 default works well across
methods, datasets, and simulators. The per-domain optimum may shift to α=0.5 (Science Q&A,
Combined) or remain at α=1.0 (Tool Use, RL), but no α outside the {0.5,1.0} band ever beats the
29

in-band defaults onbothcapability and calibration simultaneously. We therefore recommend α=1.0
as the practitioner default and α=0.5 as a slightly more conservative alternative whenever capability
stability is paramount.
0 20 40
Round
0.6
0.7
0.8Eval score
Capability
1 2 3 4 5 6 7
Conversation turn
0.0
0.2
0.4
0.6
0.8Surprise
Surprise
1 2 3 4 5 6 7
Conversation turn
0.00
0.05
0.10
0.15
0.20OFR
OFR
alpha=0.1
alpha=0.5
alpha=1.0
alpha=2.0
Figure 8:Multi-turn α-sweep (Combined, GPT-4.1 simulator).Left: teacher-side evaluation
score across training rounds. Middle: teacher-side surprise rate across conversation turns. Right:
teacher-side OFR across conversation turns. Curves: α∈ {0.1,0.5,1.0,2.0}. Later turns start more
overconfident than early turns, and PH compresses this region most.
RL OPD Combined
0.0
0.2
0.4
0.6
0.8Eval score
Capability Performance
0.69
0.54
0.61
0.76
0.69
0.65
0.30
0.30
0.31
0.31
0.32
0.33
RL OPD Combined
0%
5%
10%
15%
20%OFR
Calibration Gap
5.3%
15.9%
10.0%
3.1%
2.6%
6.8%
19.0%
13.5%
13.1%
11.6%
10.8%
12.1%
GPT-4.1 Baseline GPT-4.1 PH GPT-5.4 Baseline GPT-5.4 PH
Figure 9:Capability and calibration across user simulators.OLMo-3-7B-Instruct trained on the
multi-turn personal-agent task with 8k response-length budget and mixed Student/Teacher rounds,
under two simulators (GPT-4.1 and GPT-5.4). Left: teacher-side personalization-evaluator score
(higher is better). Right: teacher-side OFR (lower is better).
F Prompt Templates
This appendix lists the prompt templates used by PH’s prospective self-evaluator (§3.1) and, in
multi-turn settings, the retrospective process reward model (PRM) used as the verifier R in Eq. 1. All
prompts elicit a ternary score parsed from a \boxed{·} field as zt or rt ∈ {−1,0,+1}; ties under
majority voting are broken toward0.
F.1 Single-Step Tasks
For single-step tasks (Science Q&A, Tool-Use, etc.), the prospective self-evaluator uses a task-
type-specific template that wraps a common ternary scoring instruction. The task type is routed
automatically from the dataset identifier: math (GSM8K, MATH, AIME, etc.) →math ; multiple-
choice (SciKnowEval, GPQA, MMLU) →mcq ; tool-use →tool_use ; code (LiveCodeBench,
HumanEval+, etc.) →code ; otherwise →default . Placeholders {problem} and {solution} are
filled with the task instance and the agent’s just-emitted actiona t.
The common ternary scoring instruction below is appended verbatim to every single-step template
(Listing 1); each task type then wraps it with its own header (Listings 2–6).
1Return exactly one score and no explanation:
2+1 if you are confident it is correct
30

3-1 if you believe it is wrong
40 if you are unsure
5Your entire response must be exactly one of: +1, 0, -1
Listing 1: Common ternary scoring instruction (single-step).
1Review your solution to the following problem.
2
3Problem:
4{problem}
5
6Your solution:
7{solution}
8
9Do you believe your final answer is correct?
10[common scoring instruction]
Listing 2: Single-step prospective self-evaluator: Math template.
1Review the question and your chosen answer below.
2
3Question:
4{problem}
5
6Your response:
7{solution}
8
9Do you believe you selected the correct answer?
10[common scoring instruction]
Listing 3: Single-step prospective self-evaluator: Multiple-choice template.
1Review the task and your proposed solution below.
2
3Task:
4{problem}
5
6Your solution:
7{solution}
8
9Do you believe you selected the correct actions and inputs to
10complete this task?
11[common scoring instruction]
Listing 4: Single-step prospective self-evaluator: Tool-use template.
1Review the problem and your code solution below.
2
3Problem:
4{problem}
5
6Your solution:
7{solution}
8
9Do you believe your code produces the correct output for all
10test cases?
11[common scoring instruction]
Listing 5: Single-step prospective self-evaluator: Code template.
1Review your solution to the following problem.
31

2
3Problem:
4{problem}
5
6Your solution:
7{solution}
8
9Do you believe your solution is correct?
10[common scoring instruction]
Listing 6: Single-step prospective self-evaluator: Default template (fallback).
F.2 Multi-Turn Tasks
In multi-turn settings, two distinct prompts are used: aprospectiveprompt that the agent’s policy
answers immediately after emittingat (without observing the next statect =s t+1), and aretrospective
PRM prompt that scores the same response after st+1 is revealed. The retrospective PRM serves
as the verifier R in Eq. 1; the prospective prompt produces zt as in Eq. 3.1. Placeholders are filled
at runtime: {response_text} is the agent’s action at, {last_user_message} is the most recent
user turn from the conversation history, {next_state_text} is st+1, and {next_state_role}
indicates whether the next state is a user reply or a tool return.
Prospective self-evaluator (general multi-turn).This is the default prospective prompt used by
PH at every turn t. It receives only (st, at) via {last_user_message} and {response_text}; the
next states t+1 is not exposed.
1User request:
2{last_user_message}
3
4Assistant response:
5{response_text}
6
7Does this response correctly and completely address the user’s
8request?
9Answer \boxed{1} for yes, \boxed{-1} for no, \boxed{0} for unsure.
10Be brief. End your answer with \boxed{SCORE}.
Listing 7: Multi-turn prospective self-evaluator (general).
Prospective self-evaluator (Personal Agent, style-aware).This variant is used in the Personal
Agent setting where user satisfaction depends on stylistic conformance (natural prose, no AI-style
formatting) in addition to factual correctness. The prompt is split into a system message that defines
the user’s style preferences and a user message that asks for the prediction.
1[SYSTEM]
2You are predicting whether a user will be SATISFIED or
3DISSATISFIED with an AI assistant’s response, based on the
4user’s strong style preferences.
5
6The user HATES AI-style formatting. Specifically, the user
7will ask for a rewrite if the response contains ANY of these:
8- Markdown bold (**text**), headers (## or ###), or horizontal
9rules
10- Numbered lists (1. 2. 3.) or bullet points (- or *)
11- Overly structured step-by-step layouts
12- Phrases like "Here is", "Sure!", "Great question!", "Let me",
13"Certainly"
14- Emojis or excessive exclamation marks
15
16The user WANTS natural, human-like prose, as if a real person
17(student or teacher) wrote it casually. Flowing sentences, no
32

18formatting artifacts.
19
20Scoring:
21- \boxed{-1}: response has formatting issues or sounds AI-
22generated; user will request a rewrite
23- \boxed{1}: response is natural, human-like prose with no
24formatting artifacts; user will be satisfied
25- \boxed{0}: borderline / unsure
26
27Be strict. Even one instance of bold text or a numbered list
28means \boxed{-1}.
29
30[USER]
31User message:
32{last_user_message}
33
34Assistant response:
35{response_text}
36
37Check the response for AI-style formatting (bold, headers,
38numbered lists, bullet points, AI phrases). Does it read like
39natural human writing?
40Answer with \boxed{SCORE}.
Listing 8: Multi-turn prospective self-evaluator (Personal Agent, style-aware).
Retrospective PRM (verifier).The PRM observes the next state st+1 as evidence and assigns the
outcomer t ∈ {−1,0,+1}.
1[SYSTEM]
2You are a process reward model (PRM) evaluating an AI
3assistant. You will see the assistant’s output and the
4subsequent next state. Your task: decide whether the
5assistant’s output successfully fulfilled the user’s intent
6at that step, using the next state as evidence.
7
8Understanding the next state’s role:
9- role=’user’: a reply from the user.
10- role=’tool’: the return value of a tool the assistant
11invoked. This content was NOT available before the
12assistant’s action; it exists BECAUSE the assistant called
13the tool. A successful, non-error tool output means the
14assistant’s action worked correctly and should be scored
15positively.
16
17Scoring rules:
18- \boxed{1} (good): next state shows the task progressed
19as expected (user moves on, says
20thanks, environment confirms success,
21tool returns successful non-error
22result).
23- \boxed{-1} (bad): next state signals the assistant’s
24output was wrong, incomplete, or
25unwanted. Key negative signals:
26* user asks the assistant to redo,
27retry, or repeat the same action
28* user requests a correction or
29modification
30* user rephrases or restates the same
31request
32* environment returns an error,
33failure, or unexpected result.
34- \boxed{0} (neutral): next state is ambiguous.
35
33

36A change request is negative feedback: it means the previous
37output did not meet the user’s need; do not treat it as a
38neutral new instruction. Think step-by-step, then give your
39final score inside \boxed{}.
40
41[USER]
42Assistant output:
43{response_text}
44
45Next state [role: {next_state_role}]:
46{next_state_text}
47
48First, classify the next state: is it (a) positive
49progression, (b) a correction / redo / change request, or
50(c) ambiguous? Then assign \boxed{1}, \boxed{-1}, or \boxed{0}.
Listing 9: Multi-turn retrospective PRM verifier (next-state grounded).
34

Table 4: Hyperparameters for multi-turn personal agent: Combined (Binary RL + OPD) and Com-
bined + PH on OpenClaw-RL.
Parameter Value
Models, GPU layout
Backbone (student / PRM / teacher) OLMo-3-7B-Instruct (shared)
Total GPUs 8 (1 node)
Actor 4 GPUs, TP=4, sequence-parallel
Rollout (sglang) 2 GPUs, TP=1 each
PRM judge (sglang) 1 GPU
OPD teacher (sglang+Megatron) 1 GPU
Rollout / context
Rollout batch size16
Samples per prompt1(multi-turn rollout = full session)
Rollout temperature0.6
Max response length / turn8192tokens
Max context length32768tokens
Max tokens per GPU32768
Conversation
Sessions per round2
Training rounds16
Max turns per sessionT max 48
Scenario schedule alternate Student / Teacher each round
Training problems (offsets) GSM8K36:∞
Eval problems (offsets)0:36student,0:24teacher
PRM judge / OPD teacher
PRM majority voteM prm 1
PRM temperature0.6
PRM max new tokens2048
EMA teacher update rate0.05
OPD teacher source Megatron actor checkpoints
Combined advantage / PPO surrogate
Advantage estimator GRPO
wrl,w opd 1.0,1.0
PPO clipε lo/εhi 0.2/0.28
KL loss coefficient0.0
Entropy coefficient0.0
Prospective Hindsight
Surprise mode continuous
Predictor sample sizeM3(averaged into¯z t; PRM noise)
Predictor max new tokens256
Surprise amplificationα1.0default; sweep{0.5,1.0,2.0}
Surprise weight clip off (gate already in[1,1+α])
Predictor gradient stop-gradient
Optimization
Optimizer Adam (Megatron)
Learning rate1×10 −6
LR decay style constant
Weight decay0.1
Adamβ 1, β2 0.9,0.98
Save interval (in weight-update steps)25
Train epochs (data passes)1
35

Table 5: Hyperparameters for single-turn SDPO and SDPO + PH on Science Q&A and Tool Use.
Parameter Value
Models, data, and inference
Backbone models OLMo-3-7B-Instruct; gpt-oss-20B (ablation)
Thinking mode disabled (enable_thinking=false)
Max prompt length2048tokens
Max response length8192tokens
Inference engine vLLM
Rollout (training)
Question batch size32
Rollouts per questionK train 8
Rollout temperature1.0
Validation
Rollouts per questionK val 16(val_kwargs.n, “mean@16”)
Validation temperature0.6
Validation top-p0.95
SDPO loss (CaOPD defaults)
Distillation top-K100
Distillation divergence token-level reverse KL
EMA teacher update rate0.05
Rollout IS clip2
Prospective Hindsight (this work)
Predictor max new tokens128
Predictor temperature / top-p0.6/0.95
Predictor sample sizeM1(deterministic verifier; no majority vote)
Surprise amplificationα1.0default; sweep{0.0,0.25,0.5,1.0,2.0,5.0}
Weight clip[w min, wmax] [0.5,2.0]
Predictor gradient stop-gradient
Optimization
Optimizer AdamW
Learning rate1×10 −5
LR warmup steps10
Weight decay0.1
Gradient clip norm1.0
PPO mini-batch size32
Total epochs3
Hardware
Hardware1×p5en.48xlarge(8×H200)
Sharding FSDP2, bf16
Table 6:PH weight strength on Science Q&A: numerical summary across the full α-sweep.OFR
=OF/(CS+OF); Early/Late are first/last 5 training steps; Mean Weight and Verifier Pass Rate are
reported as early→late.Bold: best per column.
α Early OFR Late OFR OFR Drop Rel. Drop Mean Weight Verifier Pass Rate
0.1 0.741 0.253 0.487 65.8% 1.07→1.02 24.8%→71.4%
0.25 0.739 0.250 0.489 66.2% 1.17→1.06 25.6%→71.2%
0.5 0.768 0.209 0.560 72.9% 1.35→1.09 22.9%→73.2%
1.0 0.732 0.239 0.423 57.8% 1.67→1.29 26.0%→67.5%
2.0 0.744 0.249 0.495 66.5% 1.68→1.22 24.9%→71.7%
36

G Limitations and Future Work
While Prospective Hindsight (PH) provides a robust and simple mechanism for self-calibration in
agent reinforcement learning, we identify several limitations that offer avenues for future work:
• Variance-Amplification at High α:High values of the surprise amplification hyperparameter
(α≥2.0) can lead to gradient norm spikes, particularly in multi-turn, long-horizon tasks where
overconfident failures are correlated with longer token sequences . While α= 1.0 is a stable
default, extreme upweighting may destabilize training.
• Theoretical Assumptions:Our gradient-flow analysis, which shows the PH update is strictly
calibration-aligned, relies on a “uniform-base-loss” assumption—specifically, that the base loss
is approximately constant on surprising rollouts. In practice, this alignment is quantitative rather
than absolute, as the per-rollout loss varies with specific log-probabilities.
• Training-Time Compute Overhead:PH requires M additional forward passes per rollout
step to elicit the prospective belief. While this adds negligible wall-clock time in asynchronous
multi-turn settings (approx. 0%), it introduces a small overhead (approx. 6%) in single-turn
synchronous training.
• Dependence on Self-Model Quality:The effectiveness of the surprise signal depends on the
policy’s ability to produce meaningful ternary predictions. Although PH facilitates the co-
evolution of the self-model and policy, the initial training phase may provide noisier signals if the
base model is extremely poorly calibrated.
• Scope of Empirical Evaluation:Our experiments focused on verifiable tasks (Science Q&A,
Tool Use) and a math-tutoring personal agent. While we demonstrated cross-scale transfer from
7B to 20B models, the performance of PH in purely creative or subjective generation tasks where
retrospective rewards are inherently ambiguous remains to be fully explored.
The limitations above suggest several directions where the Prospective Hindsight principle can be
extended or its current evidence base strengthened.
• Independent characterization of the prospective evaluator.Decoupling the evaluator’s quality
from the training trajectory is important both for methodological cleanliness and for understanding
when PH should be expected to work. Promising directions include: (i) measuring evaluator
accuracy on held-out prompts at fixed checkpoints, (ii) comparing evaluator outputs against a
stronger external judge, (iii) calibrating the evaluator’s token-level confidence against its boxed
score, and (iv) studying the regime in which evaluator and policy share systematic blind spots
and how PH behaves under such failure.
• Scaling to longer-horizon agentic tasks.Our multi-turn experiments cap conversations at
Tmax = 48 turns. Genuinely long-horizon agents—software engineering trajectories spanning
hundreds of tool calls, multi-stage research assistants, or extended pair-programming sessions—
raise two questions PH does not yet answer: how does the surprise signal interact with sparse,
delayed verifier feedback at long horizons, and does the per-turn calibration cell composition
(Fig. 5) shift further as horizons grow? Combining PH with hierarchical credit-assignment
schemes that already address sparse-reward long-horizon RL is a natural follow-up.
• Continuous-valued PRM scores and richer surprise signals.The current surprise indicator
is binary (discrete gate) or a half-distance in [0,1] (continuous gate). Recent process reward
models emit graded scores, confidence intervals, or per-criterion breakdowns [42]. Extending
PH to exploit these richer retrospective signals—for example, by defining ξt as a function of the
PRM’s confidence interval on rt rather than its point estimate—may further reduce the variance
amplification at largeαthat we observe in long horizons.
• Composition with inference-time self-correction.PH operates entirely at training time and
leaves the agent’s deployment behavior unchanged. Inference-time self-correction methods
such as Reflexion [36] and Self-Refine [26] act on the policy distributionafterPH has shaped
it. Whether the two mechanisms compose constructively—PH producing a better-calibrated
self-model, then inference-time self-correction exploiting that calibration to drive re-tries—is an
open question with practical implications for deployed agentic systems.
37

H Broader Impact
The development of Prospective Hindsight (PH) aims to bridge the gap between capability and
calibration in language model agents. As LLMs are increasingly deployed in autonomous agentic
roles—such as personal assistants, tool-use interfaces, and tutoring systems—the societal implications
of their reliability become paramount.
Positive Societal Impacts:
• Enhanced Safety and Reliability:By explicitly penalizing overconfident failures, PH encour-
ages agents to recognize their own limitations. This reduction in "confidently wrong" behavior is
critical in high-stakes domains where an agent should ideally invite human intervention rather
than proceeding with a flawed trajectory.
• Improved Human-AI Trust:Calibration is a cornerstone of effective human-AI collaboration.
Agents that can accurately communicate their uncertainty (through honest uncertainty markers)
allow users to set appropriate expectations and intervene when necessary.
• Resource Efficiency:PH is a self-extinguishing curriculum that reduces the need for manually
designed reward schedules or expensive, separate calibration-specific training phases. This can
lower the computational and human-labor barriers to developing reliable AI systems.
Potential Negative Impacts and Mitigations:
• Risk of Deceptive Calibration:While PH aligns the agent’s prospective belief with verifier
outcomes, there is a theoretical risk that an agent could learn to "appear" calibrated by avoiding
difficult but necessary tasks to minimize surprise. We mitigate this by using PH as a plug-in on
top of task-success objectives, ensuring capability is not sacrificed for calibration.
• Over-reliance on Automated Feedback:The method relies on the quality of retrospective
verifiers or PRMs. If these evaluators contain biases or incorrect logic, PH may amplify these
errors by aggressively upweighting rollouts that "surprise" the model based on flawed ground
truth. Developers should ensure that the underlying verifiers are robust and subject to human
auditing.
• Dual-Use Concerns:Improved agentic autonomy and tool-use capabilities, while beneficial
for productivity, could be misused to automate malicious activities. However, PH’s primary
contribution is thealignmentof internal belief with reality, which is a fundamentally defensive
property aimed at reducing unintended failures rather than increasing raw harmful capabilities.
38
