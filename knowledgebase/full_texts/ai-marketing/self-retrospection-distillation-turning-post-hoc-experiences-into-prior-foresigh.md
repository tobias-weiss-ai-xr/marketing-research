---
title: 'Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight'
url: https://arxiv.org/abs/2610.08077
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Haoxiang Zhang
- Qinglin Chen
- Hiroaki Hayashi
- Zhuofeng Li
- Siming Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.08077
pages: 46
chars: 150543
fetched_at: '2026-11-08T13:32:29+00:00'
kb_version: 1
---

# Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight

Preprint
 Salesforce AI Research
Self-Retrospection Distillation:
T urning Post-hoc Experiences into Prior Foresight
Haoxiang Zhang 1,2∗ Qinglin Chen 1∗ Hiroaki Hayashi 1∗ Zhuofeng Li 3∗ Siming Zhang ∗ Jiaxin
Zhang1 Jixuan Chen 1,2 Fang Wu4 Pan Lu4 Silvio Savarese 1 Julian McAuley 2 Chien-Sheng Wu1
1Salesforce AI Research 2UC San Diego 3T exas A&M University 4Stanford University
ABSTRACT
Reinforcement learning with verifiable rewards (RLVR) turns agent experience
into learning signals primarily through scalar outcome rewards after interaction.
For group-relative objectives, however, this signal vanishes when all rollouts re-
ceive the same reward, even though their trajectories may reveal useful informa-
tion about what the task requires and how the agent fails. We ask a complemen-
tary question:can hindsight teach an agent what it could have anticipated before
acting?We introduceprospective learning, which uses post-hoc experience to su-
pervise foresight predictions from the pre-interaction view, and instantiate it with
Self-Retrospection Distillation (SRD). Intuitively, a completed trajectory reveals
knowledge that would have been useful and pitfalls that should be avoided; SRD
distills this privileged hindsight into trajectory-blind foresight of the same policy.
Foresight serves only as a training target and need not be explicitly generated at in-
ference time. Across 10 tool-integrated reasoning and long-horizon agentic tasks,
SRD complements RLVR and self-distillation baselines with gains of up to24.2
pp. Its advantage is especially pronounced when reward contrast is scarce: when
37–98%of rollout groups are reward-uniform across model scales, yet SRD can
still exploit learning signal from sampled trajectories. In 2B setting, where98%
of groups are all-failure, the RLVR training ends up at0.0%success, while adding
SRD reaches60.6%under the same rollout budget. Our results suggest that post-
hoc agent experience is useful not only for evaluating or improving behavior, but
also for shaping predictive representations before available interaction.
 Code
1 INTRODUCTION
Reinforcement learning with verifiable rewards (RLVR) has emerged as a scalable post-training
paradigm for large language model (LLM) agents: by executing against automated verifiers and
optimizing policies from outcome signals, it enables agents to develop complex, multi-step behavior
without human-annotated traces (Shao et al., 2024; Guo et al., 2025; Yu et al., 2025). Applied to
tool-integrated reasoning (Jin et al., 2025a; Xue et al., 2026; Qian et al., 2025), code execution (Le
et al., 2022; Cao et al., 2026), computer use (Wang et al., 2025a), and multi-agent coordination (Li
et al., 2026; Ke et al., 2026), RLVR has proven remarkably effective in settings where agents must
act in an external environment and learn from feedback revealed only through interaction.
The supervision in RLVR, however, is inherently retrospective: outcome signals become available
only after interaction and are then assigned back to the actions that produced them. Yet a broad
line of work on predictive control, world models, and planning suggests that effective interaction
also depends on what an agent can anticipate before acting, how its interaction may fail, and what
the environment is likely to demand (Pathak et al., 2017; Hafner et al., 2020; Zhou et al., 2023).
Such pre-interaction expectations shape subsequent exploration, but in RLVR they remain an im-
plicit byproduct of optimizing behavior. More importantly, relying exclusively on post-hoc outcome
contrast creates a fundamental blind spot: when all rollouts in a group receive the same reward,
especially in long-horizon reasoning tasks where most attempts fail (Lightman et al., 2024), their
∗Core contributors. Correspondence tohaz140@ucsd.edu&wu.jason@salesforce.com.
1
arXiv:2610.08077v3  [cs.AI]  14 Oct 2026

Preprint
 Salesforce AI Research
group-relative advantages vanish (Schulman et al., 2017). The agent may have already revealed rich
interactive information about the task and environment, yet learn no signal from that experience.
A recent line of on-policy self-distillation extracts a denser signal from this experience: a single
model serves as both teacher and student, with the teacher conditioned on a privileged correct solu-
tion and the student trained to match its token-level distribution over the student’s own rollouts (Zhao
et al., 2026; H ¨ubotter et al., 2026). Follow-ups vary what the privileged context contains — run-
time feedback, skill summaries, or self-revisions — and hybrid objectives fold this signal back into
RLVR (Wang et al., 2026; Yang et al., 2026; He et al., 2026). Across these variants, however, the su-
pervision target is unchanged: hindsight conditions the teacher to sharpen what the agent should do
next. We ask instead what the agent could have known — whether the same completed experience
can teach it to anticipate, before acting, the demands and failures that only interaction reveals.
We call thisprospective learning: hindsight supervises the agent’s foresight. Given a task, the agent
predicts from pre-interaction information alone the knowledge the task may require and the failures
it may invite, and the completed trajectory then provides privileged supervision for those predictions.
Building on this principle, we propose Self-Retrospection Distillation (SRD). For each on-policy
trajectory, SRD pairs a pre-interaction prediction with a hindsight prediction conditioned on the
completed interaction, and aligns their token-level distributions on the student’s own prospective
rollout. As a result, every trajectory can contribute prospective supervision, precisely where reward
contrast leaves none: on a failed rollout, the self-teacher’s hindsight lets the agent distill the mistake
it just made into an anticipation it can carry forward, and on a saturated all-correct group, the same
pairing keeps extracting the knowledge that made those rollouts succeed. Reward thus decides which
lesson a trajectory teaches rather than whether it teaches one; learning then continues at both ends
of the difficulty range that group-relative methods discard. We make three contributions:
•A pre-interaction supervision target for agent experience.We formulate prospective learning
(§3.1), a post-training target that distills structured information revealed after interaction into
predictions constrained to the task and environment context available beforehand, complementary
to the retrospective use of experience in RLVR and self-distillation.
•A composable self-distillation instantiation.Self-Retrospection Distillation (SRD, §3.2) adds
a lightweight auxiliary objective to RLVR and self-distillation algorithms, and improves perfor-
mance across diverse tool-integrated reasoning and long-horizon agentic settings (§4.2); our anal-
ysis characterizes the regimes in which this additional signal is most useful (§RQ.1).
•Learning beyond scalar reward variance.SRD provides dense supervision from all trajectories
and remains informative for reward-uniform baselines where RL yields zero advantage (§RQ.3).
2 PRELIMINARIES
We consider an agent policyπ θ interacting with an environmentE. Given a taskx∼ D, the agent
produces a trajectoryτ= (a 1, o1, . . . , aT , oT ), wherea t ∼π θ(· |h t)is the action at stept,
ot ∼ E(· |ht, at)the resulting observation, andh t the previous interaction history.
Reinforcement Learning with Verifiable Rewards (RLVR)evaluates a completed trajectory
with a verifierV(e.g. a math checker, unit test, or task rubric), producing a scalar reward
r(τ) =V(x, τ)that is converted into an advantage estimateA(τ)and assigned back to the actions
that produced it:
LRL VR(θ) =−E x, τ∼πθ
h
A(τ)
TX
t=1
logπ θ(at |h t)
i
.(1)
For group-relative methods such as GRPO (Shao et al., 2024), givenGrollouts{τ i}G i=1 for the same
task with rewards{r i}G i=1, the advantage isA(τ i) =  ri −µ r  /σr, whereµ r andσ r are the group
mean and standard deviation. Critically, when all rollouts receive identical rewards,A(τ i) = 0
for everyi; standard practice discards such uniform-reward groups entirely and resamples until
a discriminative batch is obtained (Guo et al., 2025; Yu et al., 2025), prolonging the rollout and
wasting trajectories and whatever information they contain.
2

Preprint
 Salesforce AI Research
Figure 1:Comparison of three paradigms for converting agent experience into training sig-
nals.Reinforcement Learning with Verifiable Rewards (RLVR)scalarizes completed trajectories into
outcome rewards and assigns them back to the action policy.Retrospective Learningretains struc-
tured post-hoc hindsight to supervise behavior.Prospective Learninguses hindsight to supervise
predictions formed from information available before interaction.
Retrospective Learning from Agent Experience.Beyond scalarizing a trajectory into an out-
come, retrospective methods retain structured hindsightz hind =R(x, τ)extracted by a retrospec-
tionRafter interaction—encoding environment feedback, a selected solution, or a reusable skill.
All such methods can be unified under a single objective: find a policyπ θ that maximizes expected
utility when the agent has access to hindsight derived from its own experience,
max
θ
Ex, τ∼πθ
h
Ezhind∼R(x,τ)

U(π θ, zhind, x) i ,(2)
whereUis a method-specific utility that measures how well the policy exploits the hindsight. RLVR
is a degenerate instance in whichz hind =r(τ)is a scalar andUreduces to the advantage-weighted
log-likelihood. On-policy self-distillation (Zhao et al., 2026; H ¨ubotter et al., 2026) setsz hind to a
verified trace andUto the negative Kullback-Leibler divergence between the hindsight-conditioned
teacher and the student:
UOPSD(πθ, zhind, x) =−
TX
t=1
DKL

π¯θ(· |ht, zhind)  πθ(· |ht)  ,(3)
whereπ ¯θ denotes the stop-gradient self-teacher, instantiated as the same model conditioned on
privileged hindsight, andπ θ the student conditioned only on the interaction historyh t. Skill- and
memory-based methods (Wang et al., 2026; Lu et al., 2026; Xia et al., 2026) extract reusable ab-
stractions or reflections asz hind and optimizeUas downstream task performance.
Despite their differences, these retrospective methods share a common supervision target: post-hoc
information is ultimately used to improve the agent’s reasoning or action policy. We next shift the
supervision target fromwhat actionthe agent takes towhat the agent could have anticipatedbefore
interaction.
3 LEARNINGPROSPECTIVELY VIASELF-RETROSPECTIONDISTILLATION
3.1 PROSPECTIVELEARNING
Retrospective learning (Objective 2) uses post-hoc experiencez hind to supervise the agent’s reason-
ing or action policy. We formalize its complementary counterpart: letz∈ Zdenote a structured
prospection of what the upcoming interaction may unfold. Given a taskxand its environment con-
texte, we define theforesight distributionas
pfore =π θ(· |x, e),(4)
without access to the realized interaction. We suppress the specific prospection instruction from the
notation; different instantiations may query different aspects of the upcoming interaction.
3

Preprint
 Salesforce AI Research
Figure 2:Overview of Self-Retrospection Distillation (SRD).The student policy rolls out trajec-
tories and generates anticipated pitfalls and knowledge foresights via a differently prompted call to
the same model. Post-hoc experience from the completed trajectory conditions the stopped-gradient
self-teacher, whose token-level distributions supervise the student’s own foresight rollout.
After interaction, the realized trajectory provides structured hindsightz hind, as defined in Section 2.
Prospective learning utilizes this hindsight as privileged context to define a more informed distribu-
tion over the same output space:
phind =π ¯θ(· |x, e, zhind),(5)
whereπ ¯θ denotes a hindsight-conditioned teacher policy. Thus,p fore andp hind differ in whether
post-hoc interaction information is available. Prospective learning optimizes the foresight distribu-
tion to anticipate what hindsight reveals:
Lpro(θ) =E x∼D, τ∼πθ
h
D

phind ∥p fore
i
.(6)
Unlike retrospective objectives,L pro does not optimize the action distributionπ θ(· |ht)directly. It
trains the agent to internalize, prior to interaction, the patterns of failure and knowledge that its own
traces expose: a target remains informative as long as the agent’s anticipation lags behind what its
own execution reveals.
3.2 SELF-RETROSPECTIONDISTILLATION
We instantiate prospective learning asSelf-Retrospection Distillation (SRD)with two potential
perspectives of foresight: KNOWLEDGE, describing knowledge that may be required during inter-
action, and PITFALL, describing failures that may be encountered. Both views follow the same
distillation procedure and differ only in the prospection instruction used to query the model. Within
an on-policy rollout group, successful trajectories provide KNOWLEDGEsupervision, while failed
trajectories provide PITFALLsupervision, unifying positive and negative interaction experience as
two sources of prospective supervision under the same objective. 1
Hindsight and foresight construction.For a taskx, let{τ i}G i=1 denote its on-policy rollout
group, with verified rewards{r i}. For each rollouti, we usec i to denote its prospective view—
KNOWLEDGEwhenr i = 1and PITFALLwhenr i = 0. Letf i = (τ i, y∗, ϵi)denote its privileged
post-hoc context, wherey ∗ refers to gold solution or ground-truth answer andϵ i is the correspond-
ing error annotation when applicable. Conditioning on the same viewc i, SRD defines a foresight
distribution without access to the completed interaction and a hindsight-conditioned distribution that
additionally observesf i:
pi fore =π θ(· |x, e, ci), p i hind =π ¯θ(· |x, e, fi, ci).(7)
1Detailed hindsight, foresight, pitfall, and knowledge prompts are provided in Appendix B.1.
4

Preprint
 Salesforce AI Research
Here,c i is shorthand for the corresponding prospection instruction. Thus, reward determines the
typeof prospective supervision provided by a rollout, while foresight and hindsight within that view
differ only in whether privileged post-hoc interaction information is available.
Hindsight-foresight alignment.For each rollout, the student samples a foresight sequence
zfore,i ∼p i fore. The hindsight teacher evaluates the same student-generated prefix with access to
the post-hoc contextf i. SRD minimizes token-level distillation loss over the rollout group:
LSRD(θ) =E x,{τ i}G i=1∼πθ
"
1
G
GX
i=1
LiX
l=1
D

π¯θ

· |x, e, fi, zfore,i <l
  πθ  · |x, e, zfore,i <l # ,(8)
whereDis any distribution divergence measure. A natural and stable choice is the generalized
Jensen–Shannon divergence, defined forβ∈[0,1]as
JSDβ(pT ∥pS) =β DKL(pT ∥m) + (1−β)D KL(pS∥m), m=β p T + (1−β)p S,(9)
wherep T =π ¯θ(· |x, e, f, zfore <l )is theself-teacher, instantiated as a stopped-gradient copy of the
current policy, andp S =π θ(· |x, e, zfore <l )the student.
4 EMPIRICALSTUDY
4.1 EXPERIMENTSETUP
Tasks & Benchmarks.We evaluate SRD across four categories and ten tool-integrated reason-
ing and agentic benchmarks.i) Mathincludes AIME 2024, AIME 2026, and AMO-Bench (Art
of Problem Solving, 2026; An et al., 2025);ii) Codeincludes LiveCodeBench-v6 (LCB) and
OJBench (Jain et al., 2025; Wang et al., 2025b);iii) Searchincludes HotpotQA, 2WikiMultiHopQA,
and BrowseComp-Plus (Yang et al., 2018; Ho et al., 2020; Zhang et al., 2026a); andiv) Agenticin-
cludes ALFWorld and WebShop (Shridhar et al., 2020; Yao et al., 2022). The evaluation includes
held-out distribution, format, and interaction-horizon shifts across domains, testing whether gains
transfer beyond the interaction conditions seen during training.
Training & Data Construction.All methods and model scales are trained on identical data with
the same prompt ordering. Fori) Math, we use DAPO-Math-17K (Yu et al., 2025); forii) Code,
we train on thestdinsplit of LCB and evaluate on held-out LCB-v6’s functional-python prob-
lems; and foriii) Search, we follow the Search-R1 (Jin et al., 2025a) training recipe and retrieval
setup (Jin et al., 2025b) with a fixed toolset follows Zhang et al. (2026a). Foriv) Agentictasks, we
use the standard training split of ALFWorld and the standard WebShop training partition, evaluat-
ing ALFWorld on its OOD split. Math, Code, and Search are jointly trained in a single shuffled
mixture, while ALFWorld and WebShop form a second joint training mixture. We train Qwen3.5-
4B and Qwen3.5-9B (Team, 2026); full dataset splits, rollout budgets, scaffolds, and optimization
hyperparameters are provided in Appendix §C.
Baselines.We compare against three representative post-training objectives, together with the pre-
trainedVanillapolicy.a) RLVRuses a DAPO-style (Yu et al., 2025) group-relative policy opti-
mization objective (GRPO; (Shao et al., 2024)) over verified outcome rewards.b) Self-distillation:
on-policy self-distillation (OPSD) is a baseline following Zhao et al. (2026); H¨ubotter et al. (2026),
where a privileged self-teacher provides token-level supervision to the acting policy; RLSD (Yang
et al., 2026) reweighs GRPO with OPSD’s teacher-student divergence. For each baseline we ad-
ditionally report+SRDresults, where the privileged prefix is replaced by our structured hindsight
zhind and an auxiliaryL SRD loss is added with weightλ= 0.01. Both families are trained with
dynamic samplingunder the filter each objective requires, which we detail in Appendix §C.4.
4.2 MAINRESULTS
Table 1 reports performance across all task categories, where every+SRDrow distills thepitfall
hindsight alone; §RQ.1 disentangles the contribution of two perspectives and motivates that choice.
5

Preprint
 Salesforce AI Research
Table 1: Main results on Math, Code, Search, and Agentic benchmarks, reported asavg@8pass
rates in percent.Boldand underline mark the best and second-best result per column within each
model scale.Improved Perf.rows give the absolute gain in points that+SRDcontributes over its
own base algorithm, with a deeper green marking a larger gain.
Math Code Search Agentic
MethodAIME24 AIME26 AMOAvg LCB-v6 OJBenchAvg HotpotQA 2Wiki BCPAvg ALFWorld WebShop
Qwen3.5-4B-Thinking
Vanilla 24.17 29.58 1.75 18.50 40.48 3.73 22.11 58.12 48.25 20.36 42.24 39.25 75.34
OPSD 62.50 54.17 8.75 41.81 49.40 13.96 31.68 58.00 52.38 17.47 42.62 52.88 85.90
OPSD+SRD 63.33 66.25 14.75 48.11 57.34 17.69 37.52 73.25 63.00 22.29 52.85 66.62 87.46
Improved Perf. +0.83 +12.08 +6.00 +6.30 +7.94 +3.73 +5.84 +15.25 +10.62 +4.82 +10.23 +13.74 +1.56
GRPO 69.58 54.58 14.50 46.22 55.36 18.34 36.85 71.00 60.62 13.25 48.29 67.75 77.21
GRPO+SRD76.67 70.83 21.25 56.25 63.89 26.46 45.18 74.25 72.0022.77 56.34 71.0083.13
Improved Perf. +7.09 +16.25 +6.75 +10.03 +8.53 +8.12 +8.33 +3.25 +11.38 +9.52 +8.05 +3.25 +5.92
RLSD 67.92 60.42 13.25 47.20 55.75 18.99 37.37 71.38 61.88 19.40 50.89 62.75 86.89
RLSD+SRD 68.75 66.67 17.50 50.97 57.74 18.02 37.88 71.88 61.8823.3752.38 68.50 88.14
Improved Perf. +0.83 +6.25 +4.25 +3.77 +1.99 -0.97 +0.51 +0.50 0.00 +3.97 +1.49 +5.75 +1.25
Qwen3.5-9B-Thinking
Vanilla 19.58 18.75 0.75 13.03 55.75 2.44 29.10 67.88 59.63 23.98 50.50 48.62 86.82
OPSD 54.17 52.92 12.00 39.70 53.57 20.13 36.85 62.38 55.8725.5447.93 73.8891.76
OPSD+SRD 72.92 77.08 20.75 56.92 64.29 20.62 42.46 78.6371.38 24.70 58.24 77.13 88.15
Improved Perf. +18.75 +24.16 +8.75 +17.22 +10.72 +0.49 +5.61 +16.25 +15.51 -0.84 +10.31 +3.25 -3.61
GRPO 76.25 70.42 18.50 55.06 67.26 27.60 47.43 75.3871.6317.95 54.99 77.13 78.06
GRPO+SRD84.17 81.67 28.00 64.61 67.50 31.80 49.65 75.62 71.1225.5457.43 78.2584.18
Improved Perf. +7.92 +11.25 +9.50 +9.55 +0.24 +4.20 +2.22 +0.24 -0.51 +7.59 +2.44 +1.12 +6.12
RLSD 72.08 67.50 18.75 52.78 60.71 22.24 41.48 73.25 67.88 21.81 54.31 66.25 90.95
RLSD+SRD 77.92 78.33 22.75 59.67 66.67 23.38 45.03 77.38 69.13 23.86 56.79 77.25 91.12
Improved Perf. +5.84 +10.83 +4.00 +6.89 +5.96 +1.14 +3.55 +4.13 +1.25 +2.05 +2.48 +11.00 +0.17
SRD broadly improves post-training objectives and transfers beyond training conditions.
SRD improves category-level performance across GRPO, OPSD, and RLSD at both model scales,
with only one regression—WebShop under 9B OPSD (−3.61pp). The gains are often substan-
tial. For 4B GRPO, adding SRD improves the Math, Code, and Search averages by10.03,8.33,
and8.05pp, respectively, while also improving ALFWorld by3.25pp and WebShop by5.92pp.
The effect extends to other optimization targets: at 9B, OPSD+SRD raises the Math average from
39.70%to56.92%(+17.22pp) and Search+10.31pp. The gains extend to the hybrid objective:
RLSD+SRD improves ALFWorld from66.25%to77.25%(+11.00pp). These results indicate that
SRD is not tied to a particular base objective, but complements pure RLVR, self-distillation, and
their hybrid. The gains also persist when evaluation departs from the training interaction regime.
On Code, where training uses the LCBstdinformat and evaluation uses functional-format prob-
lems, SRD improves the 4B GRPO average by8.33pp, including an8.12pp gain on OJBench. On
the ALFWorld unseen environments, SRD improves every base-objective–scale combination, with
gains ranging from1.12to13.74pp. BrowseComp-Plus further introduces a substantially longer
interaction horizon (10×or more tool calls) than the training rollouts; SRD improves five of six
settings there, by up to9.52pp.
SRD mitigates the instability of pure self-distillation.Self-distillation without an outcome-
grounded signal is the least stable baseline here, and its degradation is concentrated on several
tool-integrated benchmarks. At 9B, OPSD alone ends upbelow the untrained policy— by5.50pp
on HotpotQA,3.76pp on 2Wiki and2.18pp on LCB-v6 — i.e. the post-training run has spent its
budget degrading the very interface it was supposed to sharpen. The symptom is visible in the scal-
ing behaviour: the Math average of OPSD isinvertedacross scale, the 9B run landing2.11ppbelow
the 4B one (39.70%vs.41.81%), driven by AIME24 (54.17%vs.62.50%) and AIME26 (52.92%
vs.54.17%). Adding SRD restores the expected ordering and improves both ends: OPSD+SRD
reaches48.11%at 4B and56.92%at 9B, an8.81pp gap in the right direction, gaining6.30and
17.22pp over the corresponding baseline, and all three Math benchmarks now scale monotonically
(AIME24+9.59, AIME26+10.83, AMO+6.00pp from 4B to 9B). The same repair shows on
the three columns that had regressed belowVanilla, which now stand at10.75,11.75and8.54pp
abovethe untrained policy on HotpotQA, 2Wiki and LCB-v6, respectively. These results suggest
that prospective supervision provides a complementary learning signal when direct hindsight-to-
behavior distillation becomes unstable.
6

Preprint
 Salesforce AI Research
Prefix SRD target AIME26 AMO Wall-clock (s/step)
Qwen3.5-4B
trace — 53.75 15.50 197
trace pitfall 57.08 13.50 217
trace+knowledge 57.08 15.75 221
hindsight — 63.75 13.25 258
hindsight pitfall 67.08 16.75250
hindsight+knowledge 67.50 11.50 267
Qwen3.5-9B
trace — 65.42 17.50 195
trace pitfall 67.08 21.25 229
trace+knowledge 62.92 19.75 243
hindsight — 77.50 26.50262
hindsight pitfall 84.17 26.25 275
hindsight+knowledge 80.42 26.50279
Table 2:Left: Prefix and channel choice in self-distillation, OPSD. Prefix is what the OPSD
teacher sees; SRD target is the distilled perspective; green/red marks a gain/loss over the raw-trace
no-SRD row, and Wall-clock is the rollout time per step.Top center: the SRD divergence in each
perspective during training, on two different domain-shuffled runs on 4B with RLSD; the band is
the local interquartile range of the logged points.Top right: which epistemic tokens and the classes
they belong to the SRD policy changes.Bottom center: the GRPO+SRD displacement from the
untrained base, decomposed onto GRPO’s own direction: blue is how much of that direction is kept
and red is the orthogonal remainder, per split. The dashed line is unity.Bottom right: per-token
similarity between each objective’s own update direction and the same objective plus SRD, as a
cumulative distribution over held-out positions, each median marked where its curve crosses0.5.
The arrows give how far each policy travelled from the base before and after adding SRD.
SRD remains effective as the base policy gets stronger.The benefit of prospective supervision
does not disappear at 9B: the best +SRD result increases from 4B to 9B in every task category,
with particularly strong improvements in Math and Agentic tasks. Importantly, we observe that the
gain from SRD does not increase monotonically with scale, but continues to provide complementary
supervision even as the underlying policy becomes stronger. We examine why this signal persists
across capability levels in dual-channel SRD in §RQ.3, where reward-uniform rollout groups remain
prevalent despite a shift from predominantly all-failure to increasingly all-success groups.
5 RESEARCHQUESTIONS
RQ1: WHICHFORESIGHT IS MOREINFORMATIVE?
SRD can learn from two different perspectives,pitfallsandknowledge, as we shown the promising
results in Table 1 with only the pitfalls channel. In this section, we show this choice is more an
efficiency motivation than a performance deficit. In Table 2 (Left), we vary the two things that
define that target: what the privileged teacher has in self-distillation (OPSD), and which channel
LSRD distills alongside it. Read against the no-SRD row of each block, SRD helps underboth
prefixes: distilling pitfalls adds3.3and1.7pp of AIME26 on the raw-trace prefix at 4B and 9B
and3.3and6.7on the hindsight prefix, and lifts AMO-Bench on 4B with the hindsight prefix by
3.5pp. The gain concentrates on the hindsight prefix, which solidifies that our hindsight-foresight
structure is reliable. However, adding the knowledge channel on top of pitfalls then buys nothing
and potentially risks. It is the only setting that ever landsbelowthe baseline:4pp drops on AMO-
Bench at 4B against the baseline, and62.92%AIME26 at 9B against65.42%. Its two wins over
pitfall are incremental (67.50vs.67.08;26.50vs.26.25), and it is the more expensive of the two in
every pair, spending more time in rollout, the phase that is78–87%of one training step. The training
curves in Table 2 (top center) make the same point from the optimization side: the pitfall channel’s
divergence falls steadily by47%and30%over training on the two runs shown, while the knowledge
channel stays flat (∼0.0045and∼0.003), so the second perspective is somehow redundant and
resists being fitted. Therefore, distilling pitfalls alone is a cheaper and safer target.
7

Preprint
 Salesforce AI Research
RQ2: WHICHTOKENS DOESSRD REALLOCATE?
In this section, we measure the effect of the SRD on the policy in the context of token categories. We
compare GRPO and OPSD against+SRD in the main results (§4.2), respectively, on5K policies’
own multi-turn rollouts, scoring only the tokens the model itself emitted.
Figure 3: The same shift token by to-
ken, on one rollout per arm: rows are
the top-4 likeliest continuations un-
der the policy that owns the rollout.
For every token, we accumulate its expected number of oc-
currences per rollout under the policy that generated the roll-
out, and take the difference between the two arms (Figure 2,
top right); no checkpoint is ever asked to score another’s text.
The shift is systematic in the sense that whole lexical classes
move together, and in opposite directions. On validation sets
in code,L SRD raises connective prose by8.6expected to-
kens per rollout, explicit planning language (we,need,think)
by3.7and words that name the problem’s structure (key,in-
sight,constraint) by1.4, while lowering inline mathematical
notation by6.7, punctuation by4.3, digits by4.1and inline
variable names (x,n,numbers) by3.0; tool-call syntax re-
mains unchanged (+0.03). The gains and the losses nearly
cancel: summed over every class, the shift is+0.6tokens
per rollout, so SRD is not making the policy talk more; it
is moving where the policy spends a fixed budget: out of
carrying a calculation inline, into naming the problem and
the plan, and it leaves the syntax of calling the interpreter
untouched. The same redistribution is visible at a single pre-
fix (Figure 3), where it is concentrated: in these two roll-
outs under GRPO (top) & GRPO+SRD (bottom) the leading
continuation moves two to three times as far as the other
four (+1.9against+0.6nats above,+1.5against+0.7be-
low), soL SRD re-weights within the local distribution with-
out adding an offset to all of it. Appendix §E.2 has the full class table and two controls: the shift is
not a global sharpening, and it does not depend on whose text is scored.
RQ3: CANSRD LEARN FROMREWARD-UNINFORMATIVETRAJECTORIES?
Figure 4: Uniform-reward groups
waste most of the rollout atbothends
of the capability range: (a) usable
share of the budget, (b) overall train-
ing group composition.
In GRPO, a prompt contributes a non-zero policy-gradient
signal only when its rollout group{τ i}G i=1 contains reward
variation. To isolate this regime, we train on the code do-
main alone, disable dynamic sampling, and compare the
same objective as Yu et al. (2025) with and without SRD
across four Qwen3.5 scales (Figure Right). Reward-uniform
groups consume a substantial fraction of the sampled bud-
get across capability levels: the usable share of the budget
never exceeds63%, and the discarded share isU-shaped
in capability (98.0,39.1,37.0,41.3points), because as the
policy strengthens all-zero reward groups fall monotonically
(98.0→13.4) while all-one reward groups rise monotoni-
cally (0.0→27.9): a weak policy solves nothing, a strong
one solves a lot, and neither leaves any outcome contrast to
learn from. Appendix A.3 formalizes this pattern and shows
how heterogeneity in prompt difficulty raises the uniform-
group rate beyond the homogeneous prediction. Model scal-
ing does not eliminate the blind spot, but it shifts it from fail-
ure saturation toward success saturation. SinceL SRD scores
a trajectory against its own hindsight-conditioned prospec-
tion rather than against its peers, it needs no within-group
reward variance and applies to every group. The2B case is the limiting one: with98%of groups
uniform, the baseline’s reward is so sparse that it never gets off the ground (1.6%peak training
success,0.0%final), whereas the same budget with SRD reaches60.6%in training.
8

Preprint
 Salesforce AI Research
Table 3: Making foresight explicit at inference, on Qwen3.5-4B-Thinking. Each+test-time fore-
sightrow re-evaluates the checkpoint above it with the predicted KNOWLEDGE/PITFALLblocks
emitted before acting. Benchmarks, splits and protocol are unchanged from §C.5, andAvgis on the
same convention as Table 1. Cell shading is each value’s gain over the base of its own objective, on
the scale of Table 1; base rows are unshaded.Bold: best per base objective.
ALFWorld WebShop
Qwen3.5-4B-ThinkingPick Look Clean Heat Cool Pick2 Avg Score
Base objective: RLSD
Base 85.12 50.69 58.59 58.13 56.73 61.46 62.75 86.89
+SRD (PITFALL) 88.69 45.14 72.66 70.00 75.00 53.13 68.50 88.14
+test-time foresight 86.31 59.03 83.59 66.88 85.58 57.29 73.50 88.27
+SRD (PITFALL+KNOWLEDGE) 84.52 30.56 46.09 60.00 70.19 34.38 55.87 82.21
+test-time foresight 82.14 33.33 44.53 60.63 61.54 42.71 55.62 83.80
Base objective: GRPO
Base 88.69 53.47 64.84 57.50 58.65 83.33 67.75 77.21
+SRD (PITFALL) 92.86 54.86 64.06 60.63 62.50 92.71 71.00 83.13
+test-time foresight 94.05 45.14 68.75 61.25 62.50 86.46 69.63 83.61
+SRD (PITFALL+KNOWLEDGE) 94.05 87.50 67.19 58.13 75.00 64.58 75.38 88.42
+test-time foresight 93.45 93.75 64.84 57.50 69.23 63.54 75.00 88.37
RQ4: HOW DOESSRD SHAPE THEPROSPECTIONDISTRIBUTION?
To ask where that change points, we measure all four displacements from one common origin, the
untrained base:AandSfor what GRPO and OPSD training did (A= logp GRPO −logp base,
and likewiseS), andE,E S for the same two runs with SRD. None is a component of another, so
we can splitEinto the part alongAand the part across it,E=α ˆA+E ⊥ with ˆA=A/∥A∥,
in the Fisher metric (Table 2, bottom center). On the held-out code split (626,992positions, never
trained on),α/∥A∥= 1.30: the+SRD run travels30%furtheralong GRPO’s own direction,
not back along it, and adds an orthogonal component of comparable size (∥E ⊥∥/∥E∥= 0.49).
Neither this nor its OPSD counterpart averages over cancelling halves:cos(A, E) = +0.81and
cos(S, ES) = +0.98, positive at77%and94%of positions individually (Figure 2, bottom right).
LSRD preserves substantial alignment with the host objective while introducing a non-negligible
orthogonal displacement, though the two hosts disagree with each other (cos(A, S) =−0.78).
What it changes is scale, in opposite directions: it more than doubles the small RL displacement
(0.39→0.86) and shortens the large OPSD one (1.97→0.57) along the same ray (E S ≈0.28S).
That asymmetry follows from what the term is — a dense per-token divergence to a target the policy
derives from itself. Against a host that supplies sparse credits, it adds movement; against a host
already dense self-distillation, it’s asecondself-referential target competing for the same capacity,
and it behaves like an anchor, the run travelling less far along the direction it was already going.
With Table 1, where SRD helps under both objectives, the complementarity is measured: an axis
extended, an orthogonal component of comparable size, and a step size pulled toward the host’s
own. Appendix §E.4 and §E.5 take up the opposite rescaling and the spread across domains.
RQ5: DOESTEST-TIMEFORESIGHTHELP?
This section asks what the prospective objective is worth once training is over: whether the choice
of distilled channel changes the agentic result, and whether anything further is gained by making the
foresight explicit at inference instead of leaving it implicit. Table 3 varies both, under the evaluation
protocol of §C.5. In aggregate the answer is narrow. GRPO is the only base objective where the
direction is consistent: all four of its SRD arms land above its base, by1.88–7.63pp on ALFWorld
and5.92–11.21pp on WebShop. Under RLSD the sign flips with the channel: PITFALLis worth
+5.75pp while adding KNOWLEDGEcosts6.88pp against the same base, plausibly because RLSD
already carries a self-distillation term and the KNOWLEDGEchannel adds a second self-referential
target competing with it, though with two objectives at one scale and one seed we can only offer
that as a conjecture. The test-time axis is nearly inert: of the four checkpoints, one gains5.00pp
when it states its foresight before acting and the other three move by2,3and11rollouts out of800,
9

Preprint
 Salesforce AI Research
which we read as no change, not as a measured cost. What the aggregate hides matters more than
what it shows. Not one of the eight arms improves all six ALFWorld task types over its own base;
every arm trades, without exception. The spread between an arm’s best and worst task type runs
from10.16pp, for the flattest arm (GRPO+SRD (PITFALL)), to60.07pp, and the same task type
moves in opposite directions depending on the arm: across the eight,Lookranges from−20.13to
+40.28pp andPick2from−27.08to+9.38pp. Avg therefore hides the trade. Neither axis buys a
uniform improvement, and the test-time one carries an extra risk: a predicted foresight can be wrong,
and the one we examine is, placing a two-object task’s capacity limit on the destination instead of the
agent (§F.3). As a training target a wrong foresight can be corrected by subsequent updates; spoken
before acting, it conditions the whole episode. Generating it at inference is therefore not free.
6 RELATEDWORK
From outcome supervision to hindsight-rich distillation.RLVR learns from verifiable
trajectory-level outcomes (Shao et al., 2024; Guo et al., 2025; Yu et al., 2025), while process su-
pervision raises the temporal resolution of that feedback (Lightman et al., 2024; Setlur et al., 2025;
Feng et al., 2025). A parallel line increases the information content retained from each completed
rollout: on-policy self-distillation conditions a self-teacher on privileged solutions (Zhao et al., 2026;
H¨ubotter et al., 2026), and its successors enrich that privileged context with self-revisions (He et al.,
2026), trajectory-level skills (Wang et al., 2026; Wu et al., 2026), procedural memory (Liu et al.,
2026), or an outcome-RL term (Yang et al., 2026; Lu et al., 2026). Recent diagnostics, however,
show that enriching the teacher context is not unconditionally beneficial: privileged conditioning
can alter calibration, self-correction, epistemic suppression, and even the teacher behavior being
distilled (Zhang et al., 2026b; Kaur et al., 2026; Ichihara et al., 2026; Kim et al., 2026). These mo-
tivate separating two design choices that prior work conflates —what hindsight containsandwhat
hindsight supervises. Across all of the above, the supervision target is the same (the agent’s action
distribution); SRD changes the target, redirecting hindsight from behavior to foresight.
Prospective Learning and Foresight.Learning to anticipate the consequences of interaction has
a long history in reinforcement learning. Early predictive and model-based methods learn from re-
alized transitions to estimate future outcomes and support planning before execution (Sutton, 1988;
1990), while later world-model approaches explicitly imagine possible futures — from learned
“dreams” and latent dynamics to decision-relevant predictions used for planning (Ha & Schmidhu-
ber, 2018; Hafner et al., 2020; Schrittwieser et al., 2020). Complementary hindsight methods reuse
realized outcomes to relabel or assign credit to past experience (Andrychowicz et al., 2017; Chelu
et al., 2020). Recent language-agent work has brought these ideas closer together by learning action
consequences, prospective state rollouts, and other forms of foresight before execution (Xie et al.,
2025; Song et al., 2026; Zhang et al., 2026d;c). SRD follows this predictive lineage but couples
hindsight and foresight differently: completed interaction provides privileged training-time supervi-
sion for a trajectory-blind prediction of interaction-relevant structure. Thus, SRD does not require
reconstructing a full future trajectory or explicitly consuming foresight for planning at inference
time; hindsight teaches the shared policy what could have been anticipated before acting.
7 CONCLUSION
We introduced prospective learning, extending the use of post-hoc experience from behavioral revi-
sion to pre-interaction anticipation. Our proposed Self-Retrospection Distillation (SRD) instantiates
this principle by distilling hindsight into trajectory-blind foresight over interaction-relevant knowl-
edge and failure modes. Empirically, SRD complements reinforcement learning with verifiable
rewards and self-distillation across diverse reasoning and agentic tasks, including regimes where
objective-specific filtering leaves much of the sampled experience unused. More broadly, we view
prospective learning as a post-training design axis, and we believe that a key direction toward more
capable agents is to optimize not only how they learn from experience, but also how well they can
anticipate what an interaction will demand and where it may fail before acting.
10

Preprint
 Salesforce AI Research
ETHICSSTATEMENT
This work studies post-training for language-model agents on mathematical reasoning, program-
ming, retrieval, and simulated interactive tasks. Improved task performance can also increase the
effectiveness of agents used for harmful purposes, including unsafe code execution or unauthorized
information access. Distilling a model’s own hindsight can reinforce errors and biases from its base
model, training data, or feedback; benchmark gains therefore do not establish safety, fairness, or
reliability in deployment. Applications beyond the evaluated settings should use task-specific safety
evaluations, sandboxed execution, restricted tool permissions, and human oversight for consequen-
tial actions, with safeguards for sensitive information in interaction traces.
ACKNOWLEDGMENTS
We sincerely appreciate all contributors to the journey that makes this research happen. Special
thanks to Becky Xiangyu Peng for infrastructure scheduling and construction, which makes exper-
iments more efficient; to Dr. Yefan Zhou, Manya Wadhwa, Kartik Narayan, and Ziyan Jiang for
valuable discussions; and to Dr. Shafiq Joty for critical advice on topic selection.
REFERENCES
Shengnan An, Xunliang Cai, Xuezhi Cao, Xiaoyu Li, Yehao Lin, Junlin Liu, Xinxuan Lv, Dan Ma,
Xuanlin Wang, Ziwen Wang, et al. Amo-bench: Large language models still struggle in high
school math competitions.arXiv preprint arXiv:2510.26768, 2025.
Marcin Andrychowicz, Filip Wolski, Alex Ray, Jonas Schneider, Rachel Fong, Peter Welinder, Bob
McGrew, Josh Tobin, Pieter Abbeel, and Wojciech Zaremba. Hindsight experience replay. In
Advances in Neural Information Processing Systems, volume 30, 2017.
Art of Problem Solving. AIME problems and solutions.https://artofproblemsolving.
com/wiki/index.php/AIME_Problems_and_Solutions, 2026. Accessed: 2026.
Ruisheng Cao, Mouxiang Chen, Jiawei Chen, Zeyu Cui, Yunlong Feng, Binyuan Hui, Yuheng Jing,
Kaixin Li, Mingze Li, Junyang Lin, et al. Qwen3-coder-next technical report.arXiv preprint
arXiv:2603.00729, 2026.
Veronica Chelu, Doina Precup, and Hado P. van Hasselt. Forethought and hindsight in credit assign-
ment. InAdvances in Neural Information Processing Systems, volume 33, 2020.
Zijian Chen, Xueguang Ma, Shengyao Zhuang, Ping Nie, Kai Zou, Andrew Liu, Joshua Green,
Kshama Patel, Ruoxi Meng, Mingyi Su, et al. Browsecomp-plus: A more fair and transparent
evaluation benchmark of deep-research agent.arXiv preprint arXiv:2508.06600, 2025.
Lang Feng, Zhenghai Xue, Tingcong Liu, and Bo An. Group-in-group policy optimization for llm
agent training.Advances in Neural Information Processing Systems, 38:46375–46408, 2025.
Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu
Zhang, Shirong Ma, Xiao Bi, et al. Deepseek-r1 incentivizes reasoning in llms through reinforce-
ment learning.Nature, 645(8081):633–638, 2025.
David Ha and J¨urgen Schmidhuber. World models.arXiv preprint arXiv:1803.10122, 2018.
Danijar Hafner, Timothy Lillicrap, Jimmy Ba, and Mohammad Norouzi. Dream to control: Learning
behaviors by latent imagination. InInternational Conference on Learning Representations, 2020.
Yinghui He, Simran Kaur, Adithya Bhaskar, Yongjin Yang, Jiarui Liu, Narutatsu Ri, Liam Fowl,
Abhishek Panigrahi, Danqi Chen, and Sanjeev Arora. Self-distillation zero: Self-revision turns
binary rewards into dense supervision.arXiv preprint arXiv:2604.12002, 2026.
Xanh Ho, Anh-Khoa Duong Nguyen, Saku Sugawara, and Akiko Aizawa. Constructing a multi-hop
qa dataset for comprehensive evaluation of reasoning steps. InProceedings of the 28th Interna-
tional Conference on Computational Linguistics, pp. 6609–6625, 2020.
11

Preprint
 Salesforce AI Research
Jonas H ¨ubotter, Frederike L ¨ubeck, Lejs Behric, Anton Baumann, Marco Bagatella, Daniel Marta,
Ido Hakimi, Idan Shenfeld, Thomas Kleine Buening, Carlos Guestrin, et al. Reinforcement learn-
ing via self-distillation.arXiv preprint arXiv:2601.20802, 2026.
Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, and Junpei Komiyama. Privileged solu-
tions or context-induced teacher behavior? dissecting on-policy self-distillation.arXiv preprint
arXiv:2608.09228, 2026.
Naman Jain, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-
Lezama, Koushik Sen, and Ion Stoica. Livecodebench: Holistic and contamination free evalua-
tion of large language models for code. InInternational Conference on Learning Representations,
volume 2025, pp. 58791–58831, 2025.
Bowen Jin, Hansi Zeng, Zhenrui Yue, Jinsung Yoon, Sercan Arik, Dong Wang, Hamed Zamani, and
Jiawei Han. Search-r1: Training llms to reason and leverage search engines with reinforcement
learning.arXiv preprint arXiv:2503.09516, 2025a.
Jiajie Jin, Yutao Zhu, Zhicheng Dou, Guanting Dong, Xinyu Yang, Chenghao Zhang, Tong Zhao,
Zhao Yang, and Ji-Rong Wen. Flashrag: A modular toolkit for efficient retrieval-augmented
generation research. InCompanion Proceedings of the ACM on Web Conference 2025, pp. 737–
740, 2025b.
Simran Kaur, Narutatsu Ri, Yinghui He, Liam Fowl, and Sanjeev Arora. Rethinking on-policy
self-distillation for thinking models.arXiv preprint arXiv:2607.05184, 2026.
Zixuan Ke, Yifei Ming, Austin Xu, Ryan Chin, Xuan-Phi Nguyen, Prathyusha Jwalapuram, Jiayu
Wang, Semih Yavuz, Caiming Xiong, and Shafiq Joty. Mas-orchestra: Understanding and im-
proving multi-agent reasoning through holistic orchestration and controlled benchmarks.arXiv
preprint arXiv:2601.14652, 2026.
Jeonghye Kim, Xufang Luo, Minbeom Kim, Sangmook Lee, Dohyung Kim, Jiwon Jeon, Dongsheng
Li, and Yuqing Yang. Why does self-distillation (sometimes) degrade the reasoning capability of
llms?arXiv preprint arXiv:2603.24472, 2026.
Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese, and Steven Chu Hong Hoi. Coderl:
Mastering code generation through pretrained models and deep reinforcement learning.Advances
in Neural Information Processing Systems, 35:21314–21328, 2022.
Zhuofeng Li, Haoxiang Zhang, Seungju Han, Sheng Liu, Jianwen Xie, Yu Zhang, Yejin Choi,
James Y Zou, and Pan Lu. In-the-flow agentic system optimization for effective planning and
tool use. InInternational Conference on Learning Representations, volume 2026, pp. 50524–
50570, 2026.
Hunter Lightman, Vineet Kosaraju, Yuri Burda, Harrison Edwards, Bowen Baker, Teddy Lee, Jan
Leike, John Schulman, Ilya Sutskever, and Karl Cobbe. Let’s verify step by step. InInternational
Conference on Learning Representations, volume 2024, pp. 39578–39601, 2024.
Ye Liu, Srijan Bansal, Bo Pang, Yang Li, Zeyu Leo Liu, Yifei Ming, Zixuan Ke, Shafiq Joty, and
Semih Yavuz. Procedural memory distillation: Online reflection for self-improving language
models.arXiv preprint arXiv:2607.01480, 2026.
Zhengxi Lu, Zhiyuan Yao, Zhuowen Han, Zi-Han Wang, Jinyang Wu, Qi Gu, Xunliang Cai, Weim-
ing Lu, Jun Xiao, Yueting Zhuang, et al. Self-distilled agentic reinforcement learning.arXiv
preprint arXiv:2605.15155, 2026.
OpenAI. GPT-5.6: Frontier intelligence that scales with your ambition.https://openai.com/
index/gpt-5-6/, July 2026. Accessed: 2026-09-11.
Deepak Pathak, Pulkit Agrawal, Alexei A Efros, and Trevor Darrell. Curiosity-driven exploration
by self-supervised prediction. InInternational conference on machine learning, pp. 2778–2787.
PMLR, 2017.
12

Preprint
 Salesforce AI Research
Cheng Qian, Emre Can Acikgoz, Qi He, Hongru Wang, Xiusi Chen, Dilek Hakkani-Tur, Gokhan
Tur, and Heng Ji. Toolrl: Reward is all tool learning needs.Advances in Neural Information
Processing Systems, 38:105523–105553, 2025.
Julian Schrittwieser, Ioannis Antonoglou, Thomas Hubert, Karen Simonyan, Laurent Sifre, Simon
Schmitt, Arthur Guez, Edward Lockhart, Demis Hassabis, Thore Graepel, Timothy Lillicrap, and
David Silver. Mastering atari, go, chess and shogi by planning with a learned model.Nature, 588
(7839):604–609, 2020. doi: 10.1038/s41586-020-03051-4.
John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal policy
optimization algorithms.arXiv preprint arXiv:1707.06347, 2017.
Amrith Setlur, Chirag Nagpal, Adam Fisch, Xinyang Geng, Jacob Eisenstein, Rishabh Agarwal,
Alekh Agarwal, Jonathan Berant, and Aviral Kumar. Rewarding progress: Scaling automated
process verifiers for llm reasoning. InInternational Conference on Learning Representations,
volume 2025, pp. 60808–60838, 2025.
Zhihong Shao, Peiyi Wang, Qihao Zhu, Runxin Xu, Junxiao Song, Xiao Bi, Haowei Zhang,
Mingchuan Zhang, YK Li, Yang Wu, et al. Deepseekmath: Pushing the limits of mathemati-
cal reasoning in open language models.arXiv preprint arXiv:2402.03300, 2024.
Mohit Shridhar, Xingdi Yuan, Marc-Alexandre C ˆot´e, Yonatan Bisk, Adam Trischler, and Matthew
Hausknecht. Alfworld: Aligning text and embodied environments for interactive learning.arXiv
preprint arXiv:2010.03768, 2020.
Yan Song, Xidong Feng, Bo Liu, Xinyu Cui, Haotian Fu, Zichen Liu, Mengyue Yang, Cheng Deng,
Jian Zhao, and Jun Wang. Learning stateful predictive knowledge from experience.arXiv preprint
arXiv:2607.28638, 2026.
Richard S. Sutton. Learning to predict by the methods of temporal differences.Machine Learning,
3(1):9–44, 1988. doi: 10.1007/BF00115009.
Richard S. Sutton. Integrated architectures for learning, planning, and reacting based on approximat-
ing dynamic programming. InProceedings of the Seventh International Conference on Machine
Learning, pp. 216–224, 1990. doi: 10.1016/B978-1-55860-141-3.50030-4.
Qwen Team. Qwen3.5: Towards native multimodal agents, February 2026. URLhttps://qwen.
ai/blog?id=qwen3.5.
Hao Wang, Guozhi Wang, Han Xiao, Yufeng Zhou, Yue Pan, Jichao Wang, Ke Xu, Yafei Wen,
Xiaohu Ruan, Xiaoxin Chen, et al. Skill-sd: Skill-conditioned self-distillation for multi-turn llm
agents.arXiv preprint arXiv:2604.10674, 2026.
Xinyuan Wang, Bowen Wang, Dunjie Lu, Junlin Yang, Tianbao Xie, Junli Wang, Jiaqi Deng, Xiaole
Guo, Yiheng Xu, Chen Wu, et al. Opencua: Open foundations for computer-use agents.Advances
in Neural Information Processing Systems, 38:139756–139806, 2025a.
Zhexu Wang, Yiping Liu, Yejie Wang, Wenyang He, Bofei Gao, Muxi Diao, Yanxu Chen, Kelin Fu,
Flood Sung, Zhilin Yang, et al. Ojbench: A competition level code benchmark for large language
models.arXiv preprint arXiv:2506.16395, 2025b.
Ronald J. Williams. Simple statistical gradient-following algorithms for connectionist reinforcement
learning.Machine Learning, 8(3):229–256, 1992. doi: 10.1007/BF00992696.
Jinyang Wu, Shuo Yang, Zhengxi Lu, Fan Zhang, Yuhao Shen, Lang Feng, Haoran Luo, Zheng
Lian, Shuai Zhang, Zhengqi Wen, et al. Seed: Self-evolving on-policy distillation for agentic
reinforcement learning.arXiv preprint arXiv:2607.14777, 2026.
Peng Xia, Jianwen Chen, Hanyang Wang, Jiaqi Liu, Kaide Zeng, Yu Wang, Siwei Han, Yiyang
Zhou, Xujiang Zhao, Haifeng Chen, et al. Skillrl: Evolving agents via recursive skill-augmented
reinforcement learning.arXiv preprint arXiv:2602.08234, 2026.
13

Preprint
 Salesforce AI Research
Kaige Xie, Ian Yang, John Gunerli, and Mark Riedl. Making large language models into world mod-
els with precondition and effect knowledge. InProceedings of the 31st International Conference
on Computational Linguistics, pp. 7532–7545. Association for Computational Linguistics, 2025.
Zhenghai Xue, Longtao Zheng, Qian Liu, Yingru Li, Xiaosen Zheng, Zejun Ma, and Bo An. Simple-
tir: End-to-end reinforcement learning for multi-turn tool-integrated reasoning. InInternational
Conference on Learning Representations, volume 2026, pp. 8424–8449, 2026.
Chenxu Yang, Chuanyu Qin, Qingyi Si, Minghui Chen, Naibin Gu, Dingyu Yao, Zheng Lin, Weip-
ing Wang, Jiaqi Wang, and Nan Duan. Self-distilled rlvr.arXiv preprint arXiv:2604.03128, 2026.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Bengio, William Cohen, Ruslan Salakhutdinov,
and Christopher D Manning. Hotpotqa: A dataset for diverse, explainable multi-hop question
answering. InProceedings of the 2018 conference on empirical methods in natural language
processing, pp. 2369–2380, 2018.
Shunyu Yao, Howard Chen, John Yang, and Karthik Narasimhan. Webshop: Towards scalable
real-world web interaction with grounded language agents.Advances in Neural Information Pro-
cessing Systems, 35:20744–20757, 2022.
Qiying Yu, Zheng Zhang, Ruofei Zhu, Yufeng Yuan, Xiaochen Zuo, Yu Yue, Weinan Dai, Tiantian
Fan, Gaohong Liu, Lingjun Liu, et al. Dapo: An open-source llm reinforcement learning system
at scale.Advances in Neural Information Processing Systems, 38:113222–113244, 2025.
Haoxiang Zhang, Qixin Xu, Zhuofeng Li, Lei Zhang, Pengcheng Jiang, Yu Zhang, and Julian
McAuley. Masking stale observations helps search agents–until it doesn’t: A regime map and
its mechanism.arXiv preprint arXiv:2606.00408, 2026a.
Jiaxin Zhang, Xiangyu Peng, Qinglin Chen, Qinyuan Ye, Caiming Xiong, and Chien-Sheng Wu.
The illusion of certainty: Decoupling capability and calibration in on-policy distillation.arXiv
preprint arXiv:2604.16830, 2026b.
Xuan Zhang, Wenxuan Zhang, See-Kiong Ng, and Yang Deng. Self-evolving world models for llm
agent planning.arXiv preprint arXiv:2606.30639, 2026c.
Xuan Zhang, Zhijian Zhou, Lingfeng Qiao, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, and
Yuan Qi. Internalizing the future: A unified agentic training paradigm for world model planning.
arXiv preprint arXiv:2606.27483, 2026d.
Siyan Zhao, Zhihui Xie, Mengchen Liu, Jing Huang, Guan Pang, Feiyu Chen, and Aditya Grover.
Self-distilled reasoner: On-policy self-distillation for large language models.arXiv preprint
arXiv:2601.18734, 2026.
Andy Zhou, Kai Yan, Michal Shlapentokh-Rothman, Haohan Wang, and Yu-Xiong Wang. Lan-
guage agent tree search unifies reasoning acting and planning in language models.arXiv preprint
arXiv:2310.04406, 2023.
14

Preprint
 Salesforce AI Research
APPENDIXCONTENTS
A Analysis of the Reward-Silent Regime 16
A.1 Overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
A.2 Setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
A.3 Budget accounting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.4 What group normalization optimizes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
A.5 The reward-silent event . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
A.6 How many groups each direction costs to estimate . . . . . . . . . . . . . . . . . . . . . . . 18
A.7 A remark on the two channels . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
B Instruction and Prompt Templates 20
B.1 Knowledge and Pitfall Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
B.2 LLM-as-judge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
C Experimental Details 25
C.1 Training Data Construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
C.2 Training Details . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.3 Compared Baselines . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
C.4 Dynamic Sampling . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
C.5 Evaluation Benchmarks and Protocol . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28
D More Experiment Results 29
D.1 Ablation Studyλ. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
E WhatL SRD Does to the Policy 29
E.1 Probe Setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
E.2 What the Policy Emits Differently . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
E.3 Where the Update Points . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
E.4 Why SRD Lengthens the RL Step and Shortens the Self-Distillation One . . . . . . . . . . . 31
E.5 Why the Kept Fraction Varies So Much Across Domains . . . . . . . . . . . . . . . . . . . . 32
E.6 A Statistic We Retracted . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
F Case Study: a Mechanism-Level Audit 33
F.1 From Zero Reward Contrast to a Sharper Prospection . . . . . . . . . . . . . . . . . . . . . . 33
F.2 An Interaction Contract the Task Statement Cannot Reveal . . . . . . . . . . . . . . . . . . . 37
F.3 Interaction-Grounded Foresight in an Agent Environment . . . . . . . . . . . . . . . . . . . 40
F.4 All-Success Groups and the KNOWLEDGEChannel . . . . . . . . . . . . . . . . . . . . . . . 43
F.5 How Each Channel’s Foresight Changes over Training . . . . . . . . . . . . . . . . . . . . . 45
15

Preprint
 Salesforce AI Research
A ANALYSIS OF THEREWARD-SILENTREGIME
A.1 OVERVIEW
This section answers one question:which trajectories can produce a gradient, and what does it cost
to estimate the resulting direction?That is the question §RQ.3 probes empirically.
Throughout,p=p x(θ)is the per-task success probability, and
π(p) := min{p,1−p}(10)
quantifies the distance to determinism. Expressing bounds in terms ofπ(p)simultaneously captures
both extremes of the capability range, which forms the central focus of our study.
Takeaway
The reward direction can be nonzero only on mixed-outcome groups, whose probability satisfiesq G(p) =
1−p G −(1−p) G ≤Gπ(p), whereas the prospective direction has no such structural gate. This zero-
support gate forces a second-moment penalty and, asπ(p)→0, aπ(p) −1 estimation-cost penalty for the
reward direction.
(i) The reward-usable budget is gated byπ(p)andG, and its empirical floor reveals hetero-
geneity (§A.3).A group carries a non-zero group-relative advantage exactly when its outcomes
are mixed, so its usable probability isq G(p) = 1−p G −(1−p) G, while the discarded share
pG + (1−p) G is symmetric aboutp= 1/2and tends to1at both saturation limits. Equivalently,
collectingnmixed groups requires at leastn/π(p)environment rollouts in expectation. This is the
gating pattern visible in Figure 4: the reward-usable budget collapses as groups become reward-
uniform. Separately, atG= 8, any homogeneous success rate in[0.3,0.7]predicts less than6%
discarded budget, whereas the measured floor is37%. By convexity, this excess certifies task-level
heterogeneity and cannot be explained by mean accuracy alone.
(ii) On a reward-uniform group one operator is identically zero (§A.5).On an all-failed group,
UR = 0pointwise: every realization yields exactly zero reward direction, so no scalar rescaling
can recover it. The prospective operator is not structurally forced to vanish there. This establishes a
structural separation in thesupportof the two directions, independent of any assumptions on teacher
quality.
(iii) Only the reward direction pays aπ(p) −1 gating cost (§A.6).Estimating its own mean di-
rection to relative errorϵ 2 costsn R = Ω  (Gπ(p)ϵ2)−1 groups for the reward operator, because it
vanishes off the mixed-outcome event, againstn H =O

1 + (Geff ϵ2)−1 for the prospective oper-
ator, whereG eff ≥1absorbs the dependence induced by group-level pitfall hindsight aggregation.
The asymmetry survives the worst caseG eff = 1, where the bound still carries noπ(p) −1.
A.2 SETTING
Fix a taskxwith contexteand writep=E τ∼Π θ(·|x,e)[r(τ)], whereΠ θ is the trajectory distri-
bution induced byπ θ andr∈ {0,1}. A group ofG≥2conditionally independent rollouts
{τ i}G i are drawn, and every group is retained. Withˆp=G −1 P i ri and the trajectory score
si := P t ∇θ logπ θ(ai t |h i t),
A(τ i) =
(
(ri −ˆp) p ˆp(1−ˆp),0<ˆp <1,
0,ˆp∈ {0,1},
UR = 1 G
GX
i=1
A(τ i)si,(11)
whereA(τ i)is the group-normalized advantage andU R is the resulting reward update direction;
the second branch is the standard convention for a reward-uniform group. LetH=G −1 P i H i
denote the prospective update direction, so thatθ + =θ+η(U R +λH). For rolloutτ i and foresight
token positionl, letz il denote the student logits,δ il :=∇ zil Dil, the gradient of the per-position
divergence, andJ il :=∂z il/∂θthe corresponding logit–parameter Jacobian. Stacking theJ il row-
wise intoBand concatenating theδ il intoδgivesH=−G −1B⊤δ. The teacher is the stopped-
gradient current policy. We writeµ R =E[U R],µ H =E[H], and reserveµ P =E[H i |r i=0],
16

Preprint
 Salesforce AI Research
µK =E[H i |r i=1]for theper-trajectoryhindsight construction in whichf i depends on the group
only throughτ i.
A.3 BUDGET ACCOUNTING
Proposition 1(gating of the reward direction).U R = 0pointwise off the mixed-outcome eventM,
and
qG(p) := Pr(M) = 1−p G −(1−p) G, Gπ(p)  1−π(p) G−1 ≤q G(p)≤Gπ(p).(12)
Consequently, obtainingnmixed groups takesn/q G(p)attempts and therefore at leastn/π(p)en-
vironment rollouts in expectation. Across a task distribution with¯p=E x[px],
Ex

pG x + (1−p x)G ≥¯p G + (1−¯p)G,(13)
with equality if and only ifp x is almost surely constant.
Proof.On a reward-uniform group the second branch of equation 11 applies, so everyA(τ i) = 0
andU R vanishes pointwise, not merely in mean. A mixed group requires at least one successandat
least one failure, so two union bounds giveq G(p)≤Gpandq G(p)≤G(1−p), hence the upper
bound in equation 12. Sinceq G is symmetric underp7→1−p, groups with exactly one minority
outcome occur with probabilityGπ(p)(1−π(p)) G−1 and form a subset of the mixed groups, giving
the lower bound. Waiting times between mixed-group occurrences are geometric with parameter
qG(p), andG/q G(p)≥1/π(p). For equation 13,u7→u G + (1−u) G is strictly convex on[0,1]for
G≥2.
Reading against Figure 4.Two separate facts are visible in that figure and equation 12 separates
them. The divergence at both ends is theπ(p) −1 rollout cost: it is one expression, symmetric in
success and failure saturation, so the all-correct regime at9B and35B is not a different phenomenon
from the all-failed regime at2B but the same one reflected. The elevatedfloorin the middle is the
Jensen gap of equation 13: it certifies heterogeneity ofp x across prompts, since no single difficulty
level predicts it. Neither fact says the problem is insensitive to capability — raising allp x from0.1
toward0.4would lower the discarded share considerably — only that improving average capability
does not by itself move the system out of the regime, which is what the non-monotone trajectory
shows.
A.4 WHAT GROUP NORMALIZATION OPTIMIZES
Proposition 2(induced objective).Define the scalar weighting functiona G(p) =
G−1 PG−1 m=1 G m p m(G−m)p m−1(1−p) G−m−1,
E[UR |x, e] =a G(p)∇ θp, 2(G−1) G ≤a G(p)≤ √ G−1on[0,1],(14)
so∇ θExΦG(px) =E[U R]withΦ G =
R ·
0 aG strictly increasing: the sampled reward direction ascends a task-reweighted success utility, not mean success.
Proof.Condition on the success countm. The score identities of Williams (1992) giveE[s|r=1] =
∇p/pandE[s|r=0] =−∇p/(1−p); substituting the two advantage values for1≤m≤G−1
givesE[U R |m] =
p
m(G−m)∇p/(Gp(1−p)), and averaging over the binomial law yields the
identity (uniform groups contribute zero, and atp∈ {0,1}both sides vanish). For the bounds, put
y=m(G−m)∈[G−1, G 2/4]on1≤m≤G−1; then2y/G≤ √y≤y/ √ G−1, and since
E[m(G−m)] =G(G−1)p(1−p)the same binomial weights satisfy P m G m  m(G−m)p m−1(1−
p)G−m−1 =G(G−1). Applying the two inequalities termwise gives equation 14.
Implication for the reward-silent regime.It removes a tempting shortcut. One might expect the
rarity ofMto appear as a factorq G(p)inE[U R]; it does not, because the conditional magnitude
onMgrows exactly enough to cancel it, anda G is bounded away from zero uniformly inp. The
reward signal therefore doesnotdegrade in expectation beyond the degradation of∇pitself. What
survives the cancellation is of two other kinds — a pointwise statement about support (§A.5) and a
second-moment statement (§A.6) — and those are the two the paper relies on.
17

Preprint
 Salesforce AI Research
A.5 THE REWARD-SILENT EVENT
LetE 0 be an all-failed group,Pr(E 0) = (1−p) G. By Proposition 1,U R = 0pointwise there, so the
update reduces toθ + =θ+ηλHat anyη, and scaling the reward direction by anyc >0leaves it
at zero.
We state the consequence at the strength it holds. The prospective loss isevaluableonE 0 — the
teacher is conditioned on the group’s failures, the student on the task alone — soHis defined there
and is not structurally forced to vanish; it is not guaranteed non-zero either, sinceδ= 0would give
H= 0. The separation is one of constraint, not existence:
UR = 0identically onE 0,whereasHis unconstrained there. (15)
The empirical counterpart is in §RQ.3: at2B, with98%of groups uniform, the GRPO training ends
at0.0%while the same budget withL SRD reaches60.6%.
A.6 HOW MANY GROUPS EACH DIRECTION COSTS TO ESTIMATE
At a frozen policy, we compare the group budget required to estimate each mean update direction to
a prescribed relative accuracy, exposing the estimation burden induced by reward gating. Averaging
ni.i.d. copies of learning signalUwithµ U ̸= 0gives relative mean-squared errortr Σ U /(n∥µU ∥2);
the non-degeneracy is needed for the criterion to be defined at all.
Lemma 3(effective row count).LetV row :=G −1 P i tr Cov(Hi)denote the average row-wise total variance. Whenevertr Cov(H)>0, define the effective row countG eff :=V row/tr Cov(H),
equivalently, the variance-reduction factor induced by averaging theGrow updates. ThenG eff ≥1
for arbitrary dependence among the rows, withG eff =Gunder independence.
Proof.WithX i =H i −EH i, Minkowski inL 2 and then Cauchy–Schwarz givetr Cov(H) =
E∥G−1 P i Xi∥2 ≤G −2 P i p E∥Xi∥22 ≤G −1 P i E∥Xi∥2 =V row. Under independence the cross terms vanish.
This is a scalar summary on traces: positive residual dependence typically pushesG eff belowG,
negative dependence can push it above, and in general no scalar reproduces the matrixCov(H).
Proposition 4(gating cost).Fix the policy and teacher withp∈(0,1),µ R ̸= 0,µ H ̸= 0. Let
nR, nH be the minimum numbers of independent groups attaining relative mean-squared errorϵ 2
forU R andH. Then
nR ≥ qG(p)−1 −1 ϵ2 ≥  Gπ(p) −1 −1 ϵ2 , n H = max  1,  Vrow Geff ϵ2∥µH ∥2  .(16)
If the per-row second moments are bounded byM v and∥µ H ∥ ≥mH >0uniformly along a
sequence of policies withπ(p)↓0, then
nR = Ω

G π(p)ϵ2−1 , n H ≤1 + Mv Geff m2 H ϵ2 ≤1 + Mv m2 H ϵ2 ,(17)
the last step by Lemma 3. Under per-trajectory hindsight the non-degeneracy hypothesis follows
from bounded view moments together with∥µ P ∥ ≥mP >0nearp= 0and∥µ K∥ ≥mK >0
nearp= 1, sinceµ H = (1−p)µ P +pµ K.
Proof.U R vanishes offM, soµ R =q G(p)E[U R | M]and conditional Jensen givesE∥U R∥2 =
qG(p)E[∥U R∥2 | M]≥ ∥µR∥2/qG(p), hencetr Σ R ≥(q G(p)−1 −1)∥µ R∥2; the second inequal-
ity in equation 16 is equation 12, andq G(p) =Gπ(p)

1 +O(π(p))

gives the asymptotic form.
The expression forn H is the relative-error criterion withtr Cov(H) =V row/Geff; the bound uses
Vrow ≤M v andmax{1,⌈a⌉} ≤1 +a.
Scope of the bound.Theπ(p) −1 penalty arises from the zero-support gate1 M, not from a partic-
ular policy-gradient estimator: any transformation that preservesU R = 0offMinherits the same
gating mechanism. On the prospective side, we do not assumeG eff =G; even in the worst case
Geff = 1,n H =O(1 +ϵ −2)remains independent ofπ(p).
18

Preprint
 Salesforce AI Research
A.7 AREMARK ON THE TWO CHANNELS
Two observations help interpret the ablation in §RQ.1. First, under per-trajectory hindsight,µ H =
(1−p)µP +pµK assigns weight1−pto PITFALL; at the prevailing training success rates, pitfall rows
therefore form the majority. Second, the prospective gradient is controlled by its own divergence.
For a nonnegativeL-smoothD il, the descent lemma gives∥δ il∥2 ≤2LD il, and hence∥H∥ ≤
G−1∥B∥op
q
2L P i,l Dil.The measured KNOWLEDGEdivergence remains similar, whereas the
PITFALLdivergence falls by30–47%(Figure 2, top center). Thus the divergence-dependent factor
in the bound tightens for PITFALLbut not visibly for KNOWLEDGE. Together with the ablation,
these observations are consistent with the observed redundancy of the KNOWLEDGEchannel and
motivate PITFALL-only SRD as a compute-efficient default. They establish nothing stronger:Land
∥B∥op are unmeasured, the bound is one-sided, and a small divergence can still carry task-relevant
signal.
19

Preprint
 Salesforce AI Research
B INSTRUCTION ANDPROMPTTEMPLATES
B.1 KNOWLEDGE ANDPITFALLCONSTRUCTION
In our SRD, foresights and hindsights turn a rollout group into two kinds oftiny skills: positive
KNOWLEDGEdistilled from a correct trace (which should at least include one usable piece of knowl-
edge), and negative PITFALLSdistilled from the failed ones (which at least bear one incorrect action
one should avoid). In hindsight (Eq 5), both come in aprivilegedform (the policy sees the trace)
used to build the teacher prefix, and in foresight (Eq 4) the student policy sees only the problem
and the pre-interaction information. PITFALLSare produced in two stages: a per-trace stage that
diagnoses one failed attempt, and an aggregation stage that merges the per-trace pitfalls of all failed
traces on thesamequery into one short shared list, so the teacher sees a tight “how this problem
tends to fail” summary rather than a long, noisy, and duplicated concatenation.
KNOWLEDGEHindsight from a Correct Trace
System.You are given a CORRECT worked solution. Distill the transferable KNOW-HOW it used into a
list of tiny, self-contained SKILLS — each a reusable knowledge/rule unit, NOT a step-by-step roadmap
of this specific problem. Use this EXACT structured format, one block per distinct skill (1–3 blocks):
[Knowledge/Rule]
<a general principle / identity / method / theorem the solution relied on — transferable, concrete, not
vague>
[Details/Examples]
<a tiny concrete worked instance of the rule (small numbers / short snippet), NOT this problem’s final
answer>
Good (specific):
[Knowledge/Rule]
Expandinga 2 +b 2 keeps the cross term:a 2 +b 2 = (a+b) 2 −2ab.
[Details/Examples]
Ifu+v= 6anduv= 4thenu 2 +v 2 = 36−8 = 28.
Bad (vague / problem-specific roadmap, do NOT do this): “First read the problem, then set up equations,
then solve” / “Be careful with algebra”.
Hard constraints:
• Use the literal[Knowledge/Rule]/[Details/Examples]headers for every block.
• Each skill must be a TRANSFERABLE unit usable on OTHER problems, not a recipe specific to this
one; the[Details/Examples]a self-contained mini instance.
• Do NOT state this problem’s final answer (no final letter/number/name, no “the answer is . . . ”).
• Output ONLY the[Knowledge/Rule]/[Details/Examples]blocks, nothing else.
User.
PROBLEM:
{problem}
WORKED SOLUTION (reference, do not echo):
{solution}
Distill the transferable know-how into 1–3[Knowledge/Rule]/[Details/Examples]tiny-skill
blocks (each reusable on OTHER problems; do not state this problem’s final answer).
KNOWLEDGEForesight
System.Given a problem (and NOTHING else — no solution, no answer), predict the general KNOWL-
EDGE/RULES a solver would need on this kind of problem. Output them as tiny, self-contained SKILLS
in this EXACT structured format, one block per distinct skill (1–3 blocks):
20

Preprint
 Salesforce AI Research
[Knowledge/Rule]
<a general principle / identity / method / theorem likely needed here — transferable, concrete, not
vague>
[Details/Examples]
<a tiny concrete worked instance of the rule (small numbers / short snippet), NOT this problem’s answer>
Hard constraints:
• Use the literal[Knowledge/Rule]/[Details/Examples]headers for every block.
• Each skill must be a TRANSFERABLE unit usable on OTHER problems, not a recipe specific to this
one.
• Do NOT solve the problem or give its full method; only the general knowledge it likely draws on.
• Never state a final answer.
• Output ONLY the[Knowledge/Rule]/[Details/Examples]blocks, nothing else.
User.
PROBLEM:
{problem}
Tools:
{toolsets}
Environment:
{environment constraint}
Predict the general knowledge/rules needed as 1–3[Knowledge/Rule]/[Details/Examples]
tiny-skill blocks (no solution, no answer).
PITFALLHindsight from One Failed Trace (per-trace stage)
System.You are given a FAILED attempt at a problem and the ground-truth answer. The attempt is
WRONG. Do NOT solve the problem or write a correct solution — you only learn from the failure.
Extract the SPECIFIC mistake(s) as concrete, reusable lessons in this EXACT structured format, one
block per distinct mistake (1–3 blocks):
[Error]
<the specific wrong step/assumption the attempt made — concrete, not vague>
[Rule]
<the general principle/identity/method that would have avoided it>
[Example]
<a tiny concrete worked instance of the rule (small numbers / short snippet), NOT this problem’s answer>
Good (specific):
[Error]
Dropped the coefficient 2 when expanding the identity.
[Rule]
a2 +b 2 = (a+b) 2 −2ab.
[Example]
Ifu+v= 6anduv= 4thenu 2 +v 2 = 36−8 = 28.
Bad (vague, do NOT do this): “Be careful with the algebra” / “Avoid mistakes in expansion”.
Hard constraints:
• Use the literal[Error]/[Rule]/[Example]headers for every block.
• Each field must be SPECIFIC and concrete; the[Rule]must be a transferable principle, the
[Example]a self-contained mini worked instance.
• Never state this problem’s final/ground-truth answer and never give its full worked solution.
• Output ONLY the[Error]/[Rule]/[Example]blocks, nothing else.
User.
PROBLEM:
{problem}
21

Preprint
 Salesforce AI Research
FAILED ATTEMPT (wrong, do not echo):
{attempt}
GROUND-TRUTH ANSWER (for locating the mistake only, do NOT put it in the output):
{ground truth}
TOOL EXECUTION FEEDBACK FROM THIS ATTEMPT:{tool trace}
{failure note}
Identify the specific mistake(s) and write them as[Error]/[Rule]/[Example]blocks (1–3 blocks,
using the literal headers; specific and concrete; no solution, no answer).
{failure note}— one of three variants, selected from how the trace failed.
•truncated.NOTE: this attempt was CUT OFF by the response-length limit before it finished. The
reasoning may have been on track; the pitfall is more likely about efficiency/length (e.g. being too
verbose, not reaching the answer in time) than a conceptual error. Judge accordingly.
•format.NOTE: this attempt produced NO parseable final answer (missing/empty answer tag). The
reasoning may be fine but the OUTPUT FORMAT is broken. The pitfall should stress following the
required answer format.
•wrong.NOTE: this attempt gave a complete but INCORRECT answer. The pitfall should target the
conceptual/computational mistake that led to the wrong answer.
PITFALLHindsight Aggregated over the Query’s Failed Traces (aggregation stage)
System.You are given several sets of PITFALL LESSONS (each a list of
[Error]/[Rule]/[Example]blocks) distilled from different failed attempts at the SAME
problem. Synthesize the COMMON, recurring mistakes into one short shared list, merging duplicates and
dropping one-off noise, KEEPING the same structured format.
Output 1–3 blocks, each EXACTLY:
[Error]
<the specific recurring mistake>
[Rule]
<the general principle/identity/method that avoids it>
[Example]
<a tiny concrete worked instance, NOT this problem’s answer>
Hard constraints:
• Use the literal[Error]/[Rule]/[Example]headers; keep each field SPECIFIC (no vague “be
careful” warnings).
• Never state the final/ground-truth answer and never give a worked solution.
• Output ONLY the[Error]/[Rule]/[Example]blocks, nothing else.
User.
PROBLEM:
{problem}
FAILED ATTEMPT 1 PITFALLS:{pitfalls1}
. . .
FAILED ATTEMPTkPITFALLS:{pitfalls k}
Synthesize the common recurring pitfalls into 1–3[Error]/[Rule]/[Example]blocks (merge du-
plicates, drop one-off noise; no solution, no answer).
PITFALLForesight from the Problem Alone
System.Given a problem (and NOTHING else — no attempt, no answer), predict the pitfalls a solver
is most likely to fall into on this kind of problem. Output them as tiny, self-contained SKILLS in this
EXACT structured format, one block per distinct pitfall (1–3 blocks):
22

Preprint
 Salesforce AI Research
[Error]
<the specific trap a solver is likely to fall into here — concrete>
[Rule]
<the general principle/method that avoids it>
[Example]
<a tiny concrete worked instance of the rule, NOT this problem’s answer>
Hard constraints:
• Use the literal[Error]/[Rule]/[Example]headers for every block; keep each field SPECIFIC
(no vague “be careful” warnings).
• Do NOT solve the problem or give its full method; only the traps + the rule that avoids each.
• Never state a final answer.
• Output ONLY the[Error]/[Rule]/[Example]blocks, nothing else.
User.
PROBLEM:
{problem}
Tools:
{toolsets}
Environment:
{environment constraint}
Predict the pitfalls to avoid as 1–3[Error]/[Rule]/[Example]tiny-skill blocks (no solution, no
answer).
Privileged-Information Splice Templates
The teacher prompt is the student prompt with exactly one privileged section inserted immediately before
the generation suffix; which label is used depends on what the teacher is privileged with. Distinct labels
keep a correct solution from ever being confused with observed mistakes.
Correct peer solution. (trace-prefix OPSD)
Correct solution:{successful previous attempt}
Peer KNOWLEDGEhindsight, in place of the raw trace above. (hindsight-prefix OPSD)
Correct solution:{KNOWLEDGEhindsight}
Group-aggregated PITFALLhindsight, appended after the above. (hindsight-prefix OPSD)
Common mistakes to avoid (seen in failed attempts):{PITFALLhindsight}
Teacher for PITFALLforesight (privileged with the group’s all trace-level real failures).
Observed failed-attempt pitfalls (privileged, do not reveal):{[per-trace
PITFALLhindsights]}
Teacher for KNOWLEDGEforesight (privileged with this trace’s self-generated correct solution).
Observed correct solution (privileged, do not reveal):{solution}
23

Preprint
 Salesforce AI Research
B.2 LLM-AS-JUDGE
Every domain is graded deterministically first, and the judge is a fallback rather than the primary
grader. For math, answers are matched symbolically against the reference, and the judge is invoked
only for problems whose reference answer is a free-form description that no matcher can verify. For
search, exact match (EM) against the golden answer list runs first; an EM hit short-circuits with
no judge call, and only an EMmiss(whose trace does contain an extracted answer) gets a second
opinion from the judge — this recovers correct answers phrased differently from the single golden
string EM happens to compare against. For BrowseComp-Plus the judge is the primary grader, since
the benchmark ships free-form long-form answers with per-item reference answers. All three use
gpt-5.6-luna(OpenAI, 2026).
LLM-as-Judge — Math Fallback
System.You are a strict grader for science exam answers. You are given the QUESTION, the REF-
ERENCE ANSWER (ground truth), the model’s FULL RESPONSE, and the model’s EXTRACTED
ANSWER. Decide whether the model’s answer is scientifically correct and equivalent to the reference
answer.
Rules:
• Judge correctness of the ANSWER’s meaning, not its wording/format. Accept mathematically or
chemically equivalent forms (e.g. same SMILES/quantity/name).
• The extracted answer must actually answer the question. A blank, missing, or placeholder answer is
INCORRECT even if the full response rambles near the topic.
• Do NOT give credit for a guess with no supporting reasoning if it does not match the reference answer.
Reply with EXACTLY one word on the final line: CORRECT or INCORRECT.
User.QUESTION:{question}
REFERENCE ANSWER:{reference}MODEL FULL RESPONSE:{response}(truncated to 8k char-
acters) MODEL EXTRACTED ANSWER:{extracted}Is the model’s answer correct? Reply CORRECT
or INCORRECT.
LLM-as-Judge — Search / Multi-hop QA Fallback
System.You are a strict grader for multi-hop question-answering. You are given the QUESTION, one
or more ACCEPTABLE REFERENCE ANSWERS, the model’s FULL RESPONSE, and the model’s
EXTRACTED ANSWER. Decide whether the extracted answer is correct.
Rules:
• Judge correctness of MEANING, not exact wording. Accept equivalent phrasings, abbreviations,
aliases, or a different but correct level of specificity (e.g. ‘USA’ for ‘United States’, a full name for a
name the reference gives partially).
• The extracted answer must actually answer the question. A blank, missing, or placeholder answer is
INCORRECT.
• Do NOT give credit for a guess with no supporting reasoning if it does not match any reference an-
swer’s meaning.
First, briefly analyze in 1–3 sentences whether the extracted answer matches any reference answer’s mean-
ing. Then reply with EXACTLY one word on the FINAL line: CORRECT or INCORRECT.
User.
QUESTION:{question}
ACCEPTABLE REFERENCE ANSWER(S):{golden answers, semicolon-joined}
MODEL FULL RESPONSE:{response}
MODEL EXTRACTED ANSWER:{extracted}
Is the model’s answer correct? Reply CORRECT or INCORRECT.
24

Preprint
 Salesforce AI Research
LLM-as-Judge — BrowseComp-Plus Grader
Judge whether the following[response]to[question]is correct or not based on the precise and
unambiguous[correct answer]below.
[question]:{question}
[response]:{response}
Your judgement must be in the format and criteria specified below:
extracted final answer: The final exact answer extracted from the[response]. Put the ex-
tracted answer as ‘None’ if there is no exact, final answer to extract from the response.
[correct answer]:{correct answer}
reasoning: Explain why theextracted final answeris correct or incorrect based
on[correct answer], focusing only on if there are meaningful differences between
[correct answer]and theextracted final answer.
Do not comment on any background to the problem, do not attempt to solve the problem, do not argue for
any answer different than[correct answer], focus only on whether the answers match.
correct: Answer ‘yes’ ifextracted final answermatches the[correct answer]given
above, or is within a small margin of error for numerical problems. Answer ‘no’ otherwise, i.e. if there is
any inconsistency, ambiguity, non-equivalency, or if the extracted answer is incorrect.
confidence: The extracted confidence score between 0% and 100% from[response]. Put 100 if
there is no confidence score available.
C EXPERIMENTALDETAILS
C.1 TRAININGDATACONSTRUCTION
All methods and model scales use the same training examples in the same order. We first construct
a source pool for each domain and then sample a fixed training mixture that is reused across all
experimental arms.
Math.We use DAPO-Math-17K (Yu et al., 2025) as the source pool and render each problem
into our native multi-turn tool-calling format. Answers are graded by the DAPO rule-based verifier.
AIME 2024, AIME 2026, and AMO-Bench are used only for evaluation and do not overlap with the
training set.
Code.The source pool consists of themediumandhardproblems from thestdinportion
of LiveCodeBench (Jain et al., 2025), yielding2,000candidate training prompts. Evaluation uses
held-out problems in the functional Python format of LCB-v6 together with OJBench (Wang et al.,
2025b). Training and evaluation therefore differ both in problem instances and submission format.
A submission is marked correct only if it passes all retained unit tests.
Search.Following Search-R1 (Jin et al., 2025a), we construct a source pool from1,500training
questions each from HotpotQA and 2WikiMultiHopQA, obtained through FlashRAG (Jin et al.,
2025b). The agent interacts with a fixed search interface backed by a local BM25 index over
Wikipedia-18. Held-out development questions from HotpotQA and 2Wiki are used for evaluation,
while BrowseComp-Plus is never used for training.
Agentic.For ALFWorld (Shridhar et al., 2020), we train on the400games from the standard
TextWorld training split and evaluate on100out-of-distribution games with unseen room layouts
and object placements, while preserving all chat histories. For WebShop (Yao et al., 2022), we
follow the standard session partition used by Xia et al. (2026), using400training and100held-out
shopping instructions. Success requires the environment to return a terminal score of1.0.
Joint training mixtures.For Math, Code, and Search, each run uses a fixed equal-ratio mixture
of all prompts per domain, shuffled once and reused in the same order for every method and model
scale. ALFWorld and WebShop are jointly trained in a second mixture with 1:1 prompts from each
environment. This controls the training data and ordering across all compared objectives.
25

Preprint
 Salesforce AI Research
C.2 TRAININGDETAILS
We train Qwen3.5-4B and Qwen3.5-9B with thinking-on on a single node with8×NVIDIA H200
GPUs. Each training step samples16prompts with8on-policy rollouts per prompt, giving128tra-
jectories before dynamic-sampling resampling. We keep the nominal step count and retained batch
size fixed across comparable arms so that methods are trained with the same number of accepted
trajectories per optimization step.
Training rollouts use temperature1.0andtop p = 1.0, with at most8interaction turns. Table 4 sum-
marizes the shared rollout and optimization hyperparameters. Self-distillation (OPSD, RLSD, and
our SRD) uses an exponential-moving-average (EMA) self-teacher rather than a separately trained
model. The EMA parameters are updated at rate0.05per optimization step. Teacher distributions
are approximated using the top-klog-probabilities, with the importance-sampling ratio clipped at
2.0.
Table 4: Rollout and optimization hyperparameters, shared by every arm.
Setting Value
Max response length per turn8,192tokens
Max response length foresight2,048tokens
Max tool-calling turns (training)8
Temperature /top p 1.0/1.0
Optimizer Adam
Learning rate1×10 −6, constant
Warmup iterations10
Weight decay0.1
(β1, β2) (0.9,0.98)
Loss normalization per-token
Table 5: Objective-specific loss terms and hyperparameters. SRD augments the corresponding base
training configuration with the prospective distillation objective.
Arm Loss terms Hyperparameters
GRPO group-relative policy gradientϵ low =ϵ low = 0.2; IS clip 2.0
OPSD on-policy self-distillation Divergence clip2.0; top-k = 100; JSDβ=
0.5; updated token position first 8K
RLSD policy gradient w/ self-distillation reweighed clipϵ= 0.2; IS clip 2.0
+SRD base objective+L SRD Divergence clip 2.0; top-k = 100; JSDβ= 0.5
C.3 COMPAREDBASELINES
All baselines are trained by us in the identical scaffold, on the identical data stream, with the identical
rollout and optimizer budget described above; they differ only in the learning target.
•Vanillais the pretrained backbone with no post-training, evaluated directly in the multi-turn agen-
tic setting. It establishes how much of the reported capability is already present in the base model
under our settings.
•RLVR (GRPO)(Shao et al., 2024; Yu et al., 2025) is a DAPO-style group-relative policy op-
timization baseline with verifiable rewards. We stress that its learning target is leftunmodified:
the original clipped group-relative policy-gradient objective on the group-normalized outcome
reward, with no distillation term of any kind. This is what makes the comparison clean — every
difference we report is attributable to the auxiliary target rather than to a reweighted or otherwise
26

Preprint
 Salesforce AI Research
altered RL objective:
JRL VR(θ) =E (q,a)∼D,
{oi}G i=1∼πθold (·|q)
"
1PG
i=1 |oi|
GX
i=1
|oi|X
t=1
min

ri,t(θ) ˆAi,t,clip  ri,t(θ),1−ϵ low,1 +ϵ high  ˆAi,t # ,(18)
ri,t(θ) = πθ(oi,t |q, oi,<t) πθold (oi,t |q, oi,<t) , ˆAi,t = Ri −mean({R j}G j=1) std({Rj}G j=1) .(19)
•Self-distillation (OPSD)(Zhao et al., 2026) is on-policy self-distillation, following (H ¨ubot-
ter et al., 2026) with full-parameter finetuning, where the student is distilled toward its own
EMA teacher conditioned on a privileged prefix built from environment feedback and skill sum-
maries (Wang et al., 2026; Liu et al., 2026):
LOPSD(θ) =E (x,y,z priv)


|y|X
t=1
D(π θ(· |x, y<t)∥stopgrad [π ¯θ(· |x, f, y<t)])

 ,(20)
where ¯θdenotes the EMA teacher parameters ,ydenotes rollout, andfdenotes the privileged
prefix.
•RLSD(Yang et al., 2026) is self-distilled RLVR, which combines the group-relative policy-
gradient objective with an on-policy self-distillation term, and therefore sits between the two
families above. Following the hybrid formulation, its token-level objective can be written as
LRLSD(θ) =E

 1
G
GX
i=1
1
|y(i)|
|y(i)|X
t=1
min

wtA(i),clip(w t,1−ϵ,1 +ϵ)A (i)


 ,(21)
wt = exp

sign(A(i)) ∆t

=
 PT (yt |f, y<t)
PS(yt |y <t)
sign(A(i))
,(22)
whereP T andP S denote the teacher with privileged informationfas in OPSD and student token
probabilities, respectively. We cancel the RLSD target decay as it finally becomes GRPO.
•+SRDis our addition, applied on top of each of the three trained baselines: the privileged prefix
is replaced by our structured hindsightz hind and an auxiliaryL SRD loss is added with weightλ.
Specifically, for any base methodB∈ {RL VR,OPSD,RLSD}, the resulting objective is simply
LB+SRD =L B +λL SRD. (23)
C.4 DYNAMICSAMPLING
Both the RLVR and the self-distillation families are trained withdynamic sampling, each under the
filter that its own objective requires, and we keep those filters in place for every arm in Table 1 so that
no method is credited for a gradient the other could not have received. A filtered group is discarded
and resampled, so a step always commits the same usable batch-size trajectories regardless of arm.
•RLVR (GRPO, RLSD)keeps a prompt group only if its rewards have non-zero standard devi-
ation. An all-correct or all-incorrect group has a vanishing group-relative advantage for every
token it contains and contributes exactly zero gradient, so retaining it would consume batch ca-
pacity without moving the policy.
•Self-distillation (OPSD)keeps a group only if it isnot all-incorrect, i.e. at least one rollout
succeeded. The distillation target is constructed from a successful trajectory, so a group with no
correct rollout has no teacher to distill from — whereas an all-correct group remains perfectly
usable, because the teacher signal is the successful trajectory itself and not a reward contrast.
The asymmetry matters for interpreting the results. The two filters accept different sets of groups, so
the two families pay different rollout costs to fill an identical batch, and the groups that RLVR must
throw away (all-correct and all-incorrect) are precisely the ones where an outcome-reward contrast
27

Preprint
 Salesforce AI Research
carries no information. This is why we also report a variant with dynamic samplingremovedin
§RQ.3, in which every sampled group is trained on regardless of its reward pattern: SRD continues
to learn from the groups the filters would have discarded, which is the most direct expression of its
sample efficiency.
C.5 EVALUATIONBENCHMARKS ANDPROTOCOL
Common evaluation protocol.Unless otherwise specified, we evaluate each checkpoint with
avg@8: for every prompt, we sample8independent trajectories at temperature1.0andtop p = 1.0,
compute the fraction of successful trajectories, and then average across evaluation prompts. All
compared methods use the same fixed evaluation sets and task interfaces. For math/code/search, we
set max output per turn as 16K; in agentic tasks, we set this as 8K. Math answers are graded by the
DAPO verifier, search answers by exact match, code by execution against retained unit tests, and the
agentic environments by their native binary success signals; for additional LLM-as-judge fallback,
please refer to §B.2.
Math.We evaluate on AIME 2024, AIME 2025, AIME 2026 (Art of Problem Solving, 2026),
and AMO-Bench (An et al., 2025). AIME 24, 25, and 26 each contain30olympiad-level problems
with automatically verifiable integer answers. AIME 2026 postdates the backbone’s pretraining
cutoff and therefore provides a more contamination-resistant evaluation. AMO-Bench contains 50
harder olympiad-style problems with verifiable short answers and serves as our most challenging
mathematical reasoning benchmark.
Code.We evaluate on the functional Python split of LiveCodeBench-v6 (Jain et al., 2025) (63
problems) and the medium-difficulty Python track of OJBench (Wang et al., 2025b). This differs
from training, which uses thestdinformat of LiveCodeBench, and therefore tests transfer across
both problem instances and submission formats. The graded candidate is the final program executed
by the agent through the interpreter rather than the last fenced code block in its response. A problem
receives credit only when the executed program passes all retained unit tests; partial credit is not
awarded. We retain at most10tests per LCB problem and15per OJBench problem, with a6-
second limit per test. After filtering problems with unavailable upstream test data or unsupported
inputs, the OJBench evaluation set contains77problems (52NOI and25ICPC).
Search.We evaluate short-horizon retrieval on HotpotQA (Yang et al., 2018) and 2WikiMulti-
HopQA (Ho et al., 2020), and long-horizon evidence gathering on BrowseComp-Plus (Chen et al.,
2025). For HotpotQA and 2Wiki, we construct fixed100-question evaluation subsets from their
held-out development splits using Qwen3-8B under the Search-R1 scaffold as a difficulty calibrator.
We retain questions whose empiricalpass@8lies above0%but below30%, avoiding examples that
are nearly always solved or nearly always failed by the reference policy or incorrect/blur ground
truth answers. The resulting subsets are fixed once and reused unchanged across all methods and
model scales.
HotpotQA and 2Wiki use the same local retrieval interface as training, with answers graded by exact
match. BrowseComp-Plus is never used for training and evaluates substantially longer-horizon evi-
dence gathering with the fixed tool setting of Zhang et al. (2026a). It is evaluated with its dedicated
benchmark harness rather than the standard short-horizon Search-R1 scaffold.
Agentic.ALFWorld (Shridhar et al., 2020) evaluates on the standard out-of-distribution split of
100games, whose room layouts and object placements are unseen during training. WebShop (Yao
et al., 2022) uses100held-out shopping sessions under the standard session partition. An episode
is counted as successful only when the environment returns its terminal success criterion; for Web-
Shop, this requires an exact match to the requested product attributes and options.
28

Preprint
 Salesforce AI Research
D MOREEXPERIMENTRESULTS
D.1 ABLATIONSTUDYλ
Table 6 sweeps the weightλon the auxiliary prospective loss of Eq. 23, with everything else held
fixed. The base objective is OPSD, the policy is Qwen3.5-4B, and training uses the single shuffled
math/code/search mixture described in §C.1 — one policy serving all three tool interfaces, not three
separately tuned models. The bottom row is the untrained policy at step0. Note that this sweep was
run against AIME25, which is not one of the evaluation sets used in the main paper.
Table 6: Effect of the auxiliary loss weightλon Qwen3.5-4B under OPSD+λL SRD, trained on the
mixed math/code/search stream. Best per column in bold.allis the unweighted mean over avg@8
on the five benchmarks.λ= 0.01is the value used throughout the main paper.
λAIME24 AIME25 LCB-v6 HotpotQA 2Wiki all
1.072.1 65.848.8 72.5 62.064.2
0.1 70.0 64.2 50.973.462.564.2
0.01 63.3 61.757.373.363.063.7
0.001 68.8 62.5 52.5 72.4 61.3 63.5
base(step0) 24.2 26.1 40.5 58.1 48.3 39.3
The aggregate column is remarkably flat: across three orders of magnitude ofλ, the mean over the
five benchmarks moves only between63.5and64.2, while every setting sits far above the untrained
policy at39.3. We therefore donotattribute the gains reported in Table 1 to a fortunate choice ofλ;
the auxiliary objective helps across the range we swept, and tuning it is not what produces the effect.
What the sweep does show is thatλtrades performancebetweendomains rather than raising or
lowering it uniformly. The per-column spread is several times the aggregate spread and the columns
move in opposite directions: atλ= 1.0the policy is strongest on mathematics (72.1and65.8)
and weakest on code (48.8), while atλ= 0.01that reverses (63.3and61.7on mathematics,57.3
on code, the best in the column). A stronger prospective pull appears to favour the domains where
anticipating the right knowledge matters most, at some cost to the domain where the interaction is
dominated by execution.
We take two things from this. First, there is real headroom here that we have not exploited: a
practitioner targeting a single domain could pickλfor that domain and do better than any row of
this table does on average. Second, and for exactly that reason, the value carried into Table 1 is
the one that is mostbalancedacross all domains rather than the one that maximises any particular
column;λ= 0.01is chosen because it is the best compromise for a single policy serving three tool
interfaces, not because it is the best setting available. Reporting a per-domain-tunedλwould raise
the headline numbers and would also make them a weaker test of the method, since the comparison
against the base objectives is only clean when one hyperparameter setting is shared by every arm.
E WHATL SRD DOES TO THEPOLICY
This appendix is the full version of §RQ.2 and §RQ.4: §E.2 backs the first, §E.3 onwards the second,
and §E.1 is the probe setting both share.
E.1 PROBESETTING
Five checkpoints are scored on the same Qwen3.5-9B backbone rollouts: the untrained base, GRPO
and GRPO+SRD, and OPSD and OPSD+SRD. Within each pair, the two runs share the base, the
data, and every hyperparameter, and differ only byL SRD. The base serves as one common origin
for all four displacements, so no displacement is a component of another.
Every rollout is produced through the real multi-turn ReAct scaffold with live
tools. Only tokens the model itself emitted are scored: the model template injects
<|im start|>user\n<tool response>...between assistant turns, and those posi-
tions are masked out. Positions with predictive entropy below0.1nats are dropped, since at
29

Preprint
 Salesforce AI Research
those positions every checkpoint is effectively deterministic and the log-probability difference is
dominated bybf16precision noise.
•Held outis LCB-v6 functional+OJBench medium,8rollouts per problem, exactly paired be-
tween arms. It iscode only: there is no math or search in it. The code the runs trained on is
the LiveCodeBenchstdinsplit at medium and hard difficulty, so the held-out split differs from
training both in test format (functional) and in benchmark (OJBench).
•Training mixis the joint math/code/search data in §C.1. It is included only because math and
search have no paired held-out dump, and its rollouts come fromintermediatecheckpoints, which
makes it the weaker evidence; it is never given equal footing with the held-out split. Dynamic
sampling also accepted different groups in the two runs, so the training split is not prompt-paired.
That is harmless for the emission shift, which never compares arms on the same text, and for the
decomposition, which scores both checkpoints ononerollout.
In total:5152rollouts,2,617,027generated positions, of which1,093,803(42%) clear the entropy
gate, and626,992of those are held out.
E.2 WHAT THEPOLICYEMITSDIFFERENTLY
For each arm, on its own rolloutsX, we accumulate the expected count of every token underX’s
own distribution,E X [w] = P t pX (w|X :t), normalise per rollout, and reportE e[w]−E a[w]where eis GRPO+SRD andais GRPO. Neither checkpoint is ever asked to score the other’s text, so this
statistic has no off-policy confound at all. Table 7 gives the top-10 classes.
Class∆tokens Largest movers
function words+8.64the,to,that
other (residual)+5.94about,each,carefully
planning prose+3.70we,need,think
problem framing+1.35key,insight,problem
tool-call syntax+0.03<,‘‘‘
whitespace−1.04space, newline
variable names−2.95x,n,q
digits−4.121,0,2
punctuation−4.28,,-
math notation−6.69$,\
Table 7: Change in expected occurrences per rollout, held-out split. Classes are lexical and are
nota partition of the shift:otheris the unclassified residual and is the second largest entry, so the
decomposition is indicative only.
Two of the ten classes were carved out of the residual because they were the only coherent groups
inside it:variable names(single letters, i,[i, and common identifiers such asnums,max,gcd)
andproblem framing(key,insight,constraint,step,structure). One classification detail matters: the
tokenIis first person, not a loop variable, and is only distinguishable fromicase-sensitively.
Behavioural counterpart.On the same held-out problems, the+SRD arm issues2888tool calls
against the baseline’s2243, with a median of four assistant turns rather than three. This is the one
behavioural quantity we report, and it is a count over the realised rollouts rather than anything read
off the conditional distributions.
It is not a global sharpening.Mean|move|per occurrence is flat across every lexical class
(0.390–0.469), and plain prose ranks second. Only thesignedshift separates the classes, which
is what Table 2 (top right) plots.
It is not an artifact of whose text we score.Scoring both checkpoints at the same prefix gives a
per-token shift; computing it along GRPO’s own rollouts and along SRD’s own rollouts gives two
independent estimates. Over held-out tokens seen at least500times on both arms’ rollouts, they
agree at Pearsonr= +0.9976with99.75%sign agreement (n= 801). The agreement is monotone
30

Preprint
 Salesforce AI Research
in the frequency threshold and is therefore not an artifact of it:n= 2990,r= +0.991at≥100;
n= 277,r= +0.999at≥2000.
E.3 WHERE THEUPDATEPOINTS
WriteA= logp GRPO −logp base,E= logp GRPO+SRD −logp base, andS,E S for the OPSD
pair, all at the same position and all from the same origin. Inner products are taken in the Fisher
metric⟨u, v⟩p = P i piuivi under the owning policy, because a Qwen-3.5’s248K entries vocabulary is mostlybf16noise under the Euclidean one. Two nuisance axes are projected out first: the
temperature axis (logp−E p[logp]) and the realised-token axis (e y −p y), the latter because the
hindsight block leaks the trace. We then decomposeE=α ˆA+E ⊥. Table 8 reports every subset.
Subset∥A∥ ∥E∥α/∥A∥ ∥E ⊥∥n
code (held out)0.387 0.857 1.304 0.335 626,992
math (train)1.077 1.258 0.996 0.291 124,054
code (train)0.363 0.789 0.106 0.410 189,046
search (train)0.710 0.813 0.536 0.388 153,711
Table 8: Displacement decomposition, per-position medians. Note that∥E ⊥∥barely moves across
subsets while∥A∥varies by3×.
Held-out medians for both families:cos(A, E) = +0.814(positive at77.4%of positions),
cos(S, ES) = +0.980(93.8%), andcos(A, S) =−0.783(positive at only28.7%);∥A∥= 0.387→
∥E∥= 0.857and∥S∥= 1.966→ ∥E S∥= 0.568.
We deliberately do not quotecos(E, S) =−0.954as evidence for anything. It is largelyimpliedby
cos(A, E) = +0.81together withcos(A, S) =−0.78, and so carries almost no information beyond
them.
E.4 WHYSRD LENGTHENS THERL STEP ANDSHORTENS THESELF-DISTILLATIONONE
The two families move in opposite directions whenL SRD is added:0.39→0.86for GRPO but
1.97→0.57for OPSD. Three measured facts make this less surprising than it first reads.
First, the two hosts are not comparable to begin with. Self-distillation supplies a dense per-token
target at every position, whereas GRPO supplies one sparse advantage per trajectory under a KL
leash to the base, so the self-distillation run ends up∥S∥/∥A∥= 5.1×further from the base. The
question is therefore not why one grew and the other shrank, but why both ended up at asimilar
distance:∥E∥= 0.86against∥E S∥= 0.57, a factor of1.5, where their hosts differed by a factor
of5.
Second, the shrinkage in the OPSD family is pure shrinkage, not redirection. ProjectingE S onto
ˆSgivesα ES /∥S∥= 0.278with only0.194ofE S off that axis, i.e.E S ≈0.28S: the same ray, a
shorter distance. That is the signature of an added regulariser or an earlier stop, not of a competing
objective. The growth in the GRPO family has the opposite signature:α/∥A∥= 1.30plusan
orthogonal component of comparable size (0.493of∥E∥), i.e. further along the same axis and also
into a direction GRPO does not travel in.
Third, this is what the term is:L SRD is a dense per-token divergence to a prospection target derived
from the policy itself. Against a host that provides no dense signal, it is the only such signal, and it
adds movement. Against a host that is already a dense self-distillation, it is asecondself-referential
target — prospection without the hindsight block — competing for the same capacity, and it behaves
like an anchor: the run travels less far along the direction it was already going.
We flag the limitation this reading rests on. These are displacements of the final checkpoint from
the base, so they conflate the size of a step with the number of effective steps; the two runs in each
pair share hyperparameters but not the total loss, and we measure only the endpoint. Repeating the
same norms at intermediate checkpoints would separate the two, and we have not done that.
31

Preprint
 Salesforce AI Research
E.5 WHY THEKEPTFRACTIONVARIESSOMUCHACROSSDOMAINS
Table 8 looks inconsistent: held-out code and training math keep essentially all of GRPO’s direction
(α/∥A∥= 1.30and1.00), while training search keeps half (0.54) and training code almost none
(0.11). Two factors account for it, and the first is visible directly in the table.
The orthogonal component is roughly constant; the RL update is not.∥E ⊥∥is0.34,0.29,
0.41,0.39across the four subsets — a1.4×spread — while∥A∥ranges from0.36to1.08, a3×
spread. The SRD-specific part of the displacement therefore has about the same size everywhere,
and itsshareis set by how large the host’s own update happened to be at those positions. Math is
the domain where GRPO moved most (∥A∥= 1.08), so the shared component dominates and only
28%ofEis orthogonal; training code is where GRPO moved least (0.36), so the same absolute
0.41of new direction becomes66%ofE. A small kept fraction in a domain is a statement about the
denominator, not evidence that SRD undid the policy gradient there.
On-distribution versus stale prefixes.That alone does not explain held-out code (1.30) against
training code (0.11) at almost the same∥A∥(0.387against0.363). The difference is whose text the
positions come from. The held-out rollouts were generated by the very checkpoints being compared,
so both displacements are measured where those policies actually operate, and they share a direction
(cos(A, E) = +0.81). The training-mix rollouts come from intermediate checkpoints, and for code
they are additionally in thestdinformat rather than the functional one, so they are text neither
final checkpoint would now produce; at such prefixes the shared component nearly vanishes while
the SRD-specific component does not. This is the same reason the training-mix rows are the weaker
evidence throughout, and it is why the main text quotes only the held-out split.
E.6 A STATISTICWERETRACTED
An earlier trial analyzed that the SRD update was anti-aligned with the RL update, fromcos(F−
A, A)withA= logp GRPO −logp base andF= logp GRPO+SRD −logp base. That statistic cannot
be positive: the two arguments share the termA, which forces
cos(F−A, A) =−
q
1−ρ
2 , ρ= cos(A, F),
for anyFof the same norm asA, regardless of content. The measured−0.36back-solves toρ=
0.74, i.e. the two updates were74%aligned— the opposite of what was claimed. We verified the
identity analytically and by Monte Carlo, and every decomposition in this appendix is taken from
the common base instead, so no vector is a component of another, and the artifact cannot recur.
32

Preprint
 Salesforce AI Research
F CASESTUDY:AMECHANISM-LEVELAUDIT
The claim this paper makes is causal and has four links: a completed trajectory exposes information,
a retrospective teacher turns that information into structured hindsight, distillation converts the hind-
sight into anticipation formedbeforethe next interaction, and that anticipation changes behaviour.
This appendix audits those links one at a time on the raw training dumps, and it is organised so that
each subsection reports something that should not occur if the mechanism were absent. §F.1 takes a
group on which group-relative RL has no gradient at all; §F.2 takes a failure mode that the task state-
ment cannot reveal; §F.3 takes an interactive environment whose action grammar is only exposed
through acting; §F.4 takes an all-success group, which is the half of the “every trajectory” claim
that the PITFALLchannel cannot carry; §F.5 asks whether the content of each channel’s prediction
changes, holding the domain fixed.
Corpus-level context.Individual cases are realizations of a population, so we state the population
first. Over the686scanned groups,47.2%are reward-uniform (24.6%all-fail,22.6%all-success):
on nearly half the sampled prompts a group-relative objective has an identically zero advantage for
every token, while SRD’s construction is defined on all of them. Over the5,216sampled prospection
records in those runs, Table 9 reports how often the hindsight refers to the interaction interface —
tool names, thestdincontract, the answer-tag contract, admissible actions, turn budgets — and
how often it does so when the blind foresight for the same prompt did not.
Table 9: Corpus-level statistics over all logged prospection records in the five runs scanned. “In-
terface mention” is an automatic lexical test for references to tool names, thestdinor answer-tag
contracts, admissible actions, or turn budgets — a proxy, not a blind human annotation. The last
column is the fraction of PITFALLrecords whose hindsight refers to the interface when the foresight
for the same prompt did not.
Channel records foresight tok. fore. mentions hind. mentions hind. only
PITFALL1,889 539.195.470.299
KNOWLEDGE3,327 382.225— —
In29.9%of PITFALLrecords the realized interaction surfaced an interface-level fact that the same
policy’s pre-interaction prediction had not mentioned. That gap is the quantity SRD is built to close,
and the cases below are concrete realizations of it. The caveat is that this is a lexical proxy: it detects
that the interface ismentioned, not that the mention is correct or useful. We did not run blind human
annotation, and we do not claim the29.9%is a rate ofcorrectactionable advice.
F.1 FROMZEROREWARDCONTRAST TO ASHARPERPROSPECTION
This is the case the paper’s central argument rests on, so it is the one we most want not to have
chosen by hand. It is what the pre-registered rule of §F returned for the stratumcode×all-fail×
early, out of109candidate groups. The run is the code-only Qwen3.5-2B configuration of §RQ.3,
with dynamic sampling disabled so that reward-uniform groups are retained rather than resampled;
at this step31of32groups are all-fail and the mean rollout reward is0.012.
Example from # LiveCodeBenchstdin— an all-fail group
Problem (abridged).You are given a stringSof lengthNover{A, B, ?}and an integerK. A stringT
over{A, B}isgoodif no contiguous substring of lengthKis a palindrome. Replacing each?indepen-
dently gives2 q strings; count how many are good, modulo998244353. Constraints:2≤K≤N≤1000,
K≤10.
Group outcome.r(τ i) = 0for alli= 1, . . . ,8. Response lengths
[6004,8192,8998,8192,4350,8192,8192,28394]— four rollouts terminate exactly on the8,192-token
per-turn cap.
33

Preprint
 Salesforce AI Research
What the two objectives see on this group
Withˆp= 1 8 P i ri = 0, the group-relative advantage of Eq. 11 takes its second branch andA(τ i) = 0 for every rollout, so∇ θLGRPO = 0pointwiseon this prompt — no rescaling recovers it, and under the
standard filter the group would simply be discarded (§C.4). SRD’s construction, by contrast, is defined
here: every rollout hasr i = 0, so every rollout takes the PITFALLview, and the teacher is privileged with
what the eight failures exposed.
What the failures were.The eight rollouts fail in two distinguishable ways rather than one. Four
exhaust the response budget without ever calling the interpreter, each terminating exactly on the
8,192-token cap; a fifth is cut off after a single failed call. The remaining three run the interpreter to
the8-turn limit and commit to a dynamic program whose state is wrong. We reproduce the longest
of them in full, because the diagnosis below is a claim about this trace and the reader should be able
to check it against the code.
Failure Case — all 8 turns (longest rollout of the group,28,394response tokens, 8 tool
calls, 6 tool errors)
Turn 1.After24,279tokens of reasoning, brute-forces Sample 1 to confirm its reading of the problem.
This part is correct.
[RESULT] String: ABAAABA, has palindrome of length 4: False
String: ABAABBA, substring of length 4: BAAB, palindrome: True
String: ABBAABA, substring of length 4: ABBA, palindrome: True
String: ABBABBA, substring of length 4: ABBA, palindrome: True
Turn 2.Attempts the DP.SyntaxError: closing parenthesis ’]’ does not match
opening parenthesis ’(’— the offending line iscurrent dp[(""]}= 1 # Wait, s
should be length K-1 or less, an unbalanced bracket written mid-thought.
Turn 3.Retries brute force.[timeout] Execution timed out after 10 seconds.
Turn 4 — the decisive turn.Writes two DP formulations, argues in the comments that each is wrong,
abandons both, and executes a third whose state is the growingprefixs + crather than the trailing
K−1window.
Reasoning Content:The brute force approach timed out. I need a more efficient DP approach. [. . . ]
The key insight is that we need to track the string content to ensure noK-length substring is a palin-
drome. But sinceKis small (K≤10) andN≤1000, we can use DP with state representing the last
Kcharacters. [. . . ] Let me redefine the DP state:dp[i][s]= number of valid strings of lengthi+ 1
wheres=T[i−K:i][. . . ]But wait[. . . ]we only track the firsti-K+1characters. We can’t check
easily because we don’t know the rest. So, this DP approach is not correct.
Tool:code interpreter
Tool Call(7,818chars in total; twocount good strings dpstubs are written, commented on
at length and abandoned withpass. We show only the function that actually runs):
def count_good_strings_final(N, K, S):
MOD = 998244353
palindromes = set()
for mask in range(1 << K):
temp = bin(mask)[2:].zfill(K)
if temp == temp[::-1]:
palindromes.add(temp)
dp = [{} for _ in range(N)]
dp[K-1] = {"": 1}
for i in range(K, N):
new_dp = defaultdict(int)
for s, count in dp[i].items():
for c in [’A’, ’B’]:
new_s = s + c
34

Preprint
 Salesforce AI Research
if new_s in palindromes:
continue
new_dp[new_s] += count
dp[i] = new_dp
return sum(dp[N-1].values()) % MOD
print("Sample 1:", count_good_strings_final(7, 4, "AB?A?BA"))
print("Sample 2:", count_good_strings_final(40, 7,
"????????????????????????????????????????"))
print("Sample 3:", count_good_strings_final(15, 5, "ABABA??????????"))
print("Sample 4:", count_good_strings_final(40, 8, "?A?B??B?B?AA?A?B??B?B
???BA??BAA"))
Result:every sample returns zero, including Sample 1 whose answer is1. Three defects are visible in
these twenty lines:new s = s + cnever truncates to the lastK−1characters, so the membership
test can only ever fire whilelen(new s) == K; the loop assignsdp[i]instead ofdp[i+1],
leavingdp[N-1]empty; and the argumentSis never read at all, so the fixed characters and the?
positions are ignored.
Sample 1: 0 | Sample 2: 0 | Sample 3: 0 | Sample 4: 0
Turns 5 – 8.Four further attempts, none of which revisits the state definition:SyntaxError:
invalid syntax(if cand s in defaultdict ifSD(o, [0, K-1]):), thenSyntaxError:
expected ’(’(def count good strings n brute(N, K, S):), then another[timeout], and
finallyKeyError: 4. The rollout ends with no submitted program.
Below we show the per-trace PITFALLhindsight that locates this error: of everything the rollout did
wrong, it names the state, not the six syntax errors and timeouts surrounding it. (Its[Example]
clause describes a variant of the same defect taken from a sibling rollout in the group; the dump does
not record which rollout each diagnosis was drawn from.)
Per-trace PITFALLhindsight, one failed rollout
[Error]The solution did not correctly implement the state transition for substrings of lengthK, likely
by only checking the prefix condition while missing the requirement to prevent forming a palindrome
when placing a new character at positionithat creates a palindrome starting ati−K+ 1and extending
toi.
[Rule]For every positioni, after deciding the characterCat positioni, one must check all previous
positionsjsuch that the new substringT[j:i+ 1]has lengthK. Specifically, if a substringT[j:j+K]
becomes a palindrome upon placingC, the new configuration must be invalid.
[Example]IfN= 4,K= 3,S=????, and we are at positioni= 2, the only substring of length 3
starts atj= 0. If we choseA,B,A, thenT[0 : 3] =ABAis a palindrome and should be excluded. The
error arises if one only checks for palindromes starting at the current position.
Group-aggregated PITFALLhindsightz hind, merged over the failures
[Error]The solution attempts to construct the full multiset of characters from?, but fails to correctly
parse the input stringSinto a list of placeholders, which causes the replacement logic to overwrite fixed
characters or produce incorrect counts.
[Rule]When inserting characters from a replacement set into fixed positions in a string, preserve the
exact indices and characters of existing non-?characters to maintain structural integrity.
[Example]IfSisA?Band we assign?, the fixedAat 0 andBat 2 must remain unchanged; incorrect
reconstruction might shift indices.
[Error]The DP state representation assumes a global invalid state upon initialization or transition
without distinguishing a state that is “fully invalid” (contains a palindrome) from a “valid pending state”
(appropriate length to check), leading to incorrect base cases.
[Rule]In the count of valid strings, the string state is always valid. The transition allows adding a new
character to any valid state, provided it doesn’t complete a palindrome of lengthK; if the string length
is less thanK, it is valid but does not need boundary checking yet; the base case should not assume all
35

Preprint
 Salesforce AI Research
strings are invalid for smalli.
[Example]ForK= 4and lengthi <4, any string of lengthiis valid; the transition to lengthi+ 1
only fails ifi+ 1 = 4and the new character completes a palindrome.
PITFALLforesightz fore, predicted from the problem alone
[Error]Confusing direct brute force of replacement enumeration with dynamic programming, due to
the modular arithmetic request and the combinatorial explosion of the input string length.
[Rule]Use dynamic programming based on substring validity, precomputing transitions for each posi-
tion and character value.
[Example]Precompute valid pairs for lengthK. Then iterate throughS, maintaining a DP state where
dp[i][mask]stores the count of ways to fill the substring starting ati, where themaskrepresents the
valid transitions from previous characters (e.g. which of the lastK−1characters were filled).
A second all-fail group, where the failure mode is the budget itself.Not every reward-silent
group fails for an algorithmic reason, and SRD’s construction does not assume one. The rule of §F
returns, for the same run one stage later, a group in which the dominant failure is that the policy
never stops reasoning. Here the attribution is unambiguous: six of the eight rollouts terminate at
exactly the8,192-token cap having madezerotool calls, so the diagnosis can only be about them.
A second all-fail group — # LiveCodeBenchstdinsplit
Problem (abridged).Nmochi in ascending size order, thei-th of sizeA i. MochiAcan be stacked
on mochiBiffa≤b/2. For each ofQquery ranges[L i, Ri], report the maximum number of disjoint
stackable pairs formable from the mochi in that range.
Group outcome.r(τ i) = 0for all eight. Response lengths
[8192,8192,8192,8192,8192,8192,14580,8192]; seven rollouts truncated, six of them after a
single turn with no interpreter call at all.
Failure Case — a truncated rollout (single turn,8,192tokens, 0 tool calls, no answer)
Reasoning Content:This is a problem about finding the maximum number of kagamimochi that can
be made from a subset of mochi. Let me break down the problem: [. . . ] This is equivalent to finding
the maximum number of edges in a matching in a DAG where vertices are the mochi and edges exist
between mochijand mochii(whereicomes beforejin the list) if mochij≤mochii. Wait, let me
thin[. . . ]
[. . . ] involves creating a flexible selection method that considers each potential pairing, tracking the
number of valid kagamimochi formed. The goal is to develop an algorithm that can quickly identify
and count compatible mochi combinations within a specified range.
I’ll implement a solution that rigorously checks each potential pair against the condition, ensuring I
capture the true maximum kagamimochi possible. The implementation will focus on efficient valida-
tion and counting of valid pairings across different interval queries.
The key optimization is to pre-process the mochi array for queries, using a solution that can efficiently
determine valid range pairings without redundant calculations.[8,192-token cap reached — end of
rollout]
The rollout is cut off while still announcing what it is about to implement. It never calls
code interpreter, never writes a program, and never emits an answer.
Per-trace PITFALLhindsight — the budget, not the algorithm
[Error]The attempted algorithm was excessively verbose and complex, explicitly iteratively trying al-
ternative approaches (like binary search intuition, greedy matching considerations) for “fixing” a problem
mechanics that appears mathematically trivial in the input constraints (sorted array).
[Rule]Identify that the permutation requirement (distinct indices) is automatically satisfied because the
array is sorted and the problem allows choosingKpairs; the “complexity” is deceptive, and a direct count
exists.
36

Preprint
 Salesforce AI Research
[Example]ForN= 4andA= [1,2,3,4]: pairs(1,2),(1,3),(1,4),(2,4)satisfyA i ≤A j/2while
(2,3)and(3,4)do not, so the maximum number of disjoint such pairs is2. The code would have to run
many iterations or complex logic to find “2” from this simple instance.
This is thetruncatedbranch of the per-trace prompt (Box B.1) doing what it is specified to do:
when a trace is cut off by the length limit, the extractor is told the reasoning may have been on
track and that the pitfall is more likely about efficiency than about a conceptual error. Concretely,
these branches are how the error annotationϵ i of the privileged post-hoc contextf i in Eq. 7 is
instantiated:ϵ i is a coarse classification ofhowthe rollout failed, taking one of three values —
TRUNCATED(cut off by the response-length limit),FORMAT(no parseable answer tag), orWRONG
(a complete but incorrect answer) — and it routes the extractor toward the corresponding class of
lesson, which recognises when a sorted-input problem admits a direct count instead of exploring
matching formulations.
F.2 ANINTERACTIONCONTRACT THETASKSTATEMENTCANNOTREVEAL
Illustrative case.This case isolates a single variable: thesubmission contract. The tool schema
states that the lastcode interpretercall is re-executed verbatim against the hidden test input,
so the submitted program must read real stdin. Both traces below pass every provided sample; only
one submits a program that can be graded at all.
Example from # LiveCodeBenchstdinsplit (domain=code)
Problem (abridged):There areNboxes; boxiinitially contains one ball of colorC i. ProcessQqueries
(a, b): move all balls from boxato boxb, then print the number of distinct colors in boxb. Constraints:
1≤N, Q≤200000.
Group:4/8rollouts correct; tool calls[2,2,0,8,3,8,2,0], tool errors[0,0,0,3,1,2,0,0].
Success Case (2 tool calls, reads real stdin)
Turn 1:
Reasoning Content:The naive solution would maintain the contents of each box and merge them, but
that could beO(N 2)in the worst case. However, there’s a pattern here — each box acts as a leaf in a
tree structure . . . Let me implement this solution and verify it with the sample input.
Tool:code interpreter
Tool Call:the program readssys.stdin; the sample is passed through the separatestdinpa-
rameter, not baked into the source.
code:
import sys
def solve():
data = sys.stdin.read().split()
if not data: return
iterator = iter(data)
n = int(next(iterator)); q = int(next(iterator))
c = [int(next(iterator)) for _ in range(n)]
boxes = [set() for _ in range(n + 1)]
for i in range(1, n + 1):
boxes[i].add(c[i-1])
for _ in range(q):
a = int(next(iterator)); b = int(next(iterator))
boxes[b].update(boxes[a])
boxes[a] = set() # box a becomes empty
print(len(boxes[b]))
37

Preprint
 Salesforce AI Research
if __name__ == "__main__":
solve()
stdin: ’6 5\n1 1 1 2 2 3\n1 2\n6 4\n5 1\n3 6\n4 6’
Result:
1
2
1
1
3
Turn 2:
Reasoning Content:The output matches Sample 1 exactly. Let me also verify with Sample 2.
Tool:code interpreter— the identical program, re-run against the second sample.
stdin: ’5 3\n2 4 2 4 2\n3 1\n2 5\n3 2’
Result:
1
2
0
Turn 3 — submission.The last call’s source is the stdin-reading program, so it can be re-run against
the hidden tests unchanged.
Failure Case (8 tool calls, 3 tool errors, hardcoded input)
Turn 1:
Reasoning Content:This is a classic set union problem . . . This is a Disjoint Set Union (DSU) problem
where each box maintains the set of colors it contains.
Tool:code interpreter
Tool Call:the sample is embedded in the source as a literal.
code:
from collections import defaultdict
def solve():
# Read input
input_data = """6 5
1 1 1 2 2 3
1 2
6 4
5 1
3 6
4 6"""
lines = input_data.strip().split(’\n’)
N, Q = map(int, lines[0].split())
...
Result:debug prints; the simulation is wrong.
Turn 2 – 7 (condensed):
What the model is doing in this stretch:Six turns are spent re-deriving the semantics of the
move operation and fixing indexing bugs in the hardcoded literal —TypeError: object
of type ’int’ has no len(), thenValueError: too many values to unpack
(expected 2)twice, becauselines[i]is offset by the colour line. Three of the eight calls return
a traceback. By turn 6 the samples finally pass. Every one of these calls still carries the sample text
insideinput data; none of them ever reads stdin.
38

Preprint
 Salesforce AI Research
Turn 8 — submission:
Reasoning Content:Both samples pass. Now I need to think about efficiency forN, Qup to 200,000.
The naive set union approach in worst case: each box could accumulateO(N)colors . . . Total:O(N·
Q)which is4×10 10 operations — too slow! However, with smaller-to-larger merging . . .
Tool:code interpreter
Tool Call:
code:
def solve_optimized():
input_data = """6 5
1 1 1 2 2 3
1 2
6 4
5 1
3 6
4 6"""
...
Result:1 / 2 / 1 / 1 / 3— the sample passes.
This final call is the submitted program. Re-run against the hidden test input it ignores stdin entirely
and re-prints the sample answer, so the submission fails regardless of whether its algorithm is correct.
The supervision SRD builds from this group.The aggregated hindsight of a neighbouring code
group in the same run states the contract directly.
Group-aggregated PITFALLhindsight, a neighbouring code group (step 4) — the submis-
sion contract
[Error]Incorrectly reading or truncating the input strings (e.g., treating a 7-character string as the
intended 8-character target), leading to mismatched lengths and logic errors before the core algorithm
even runs.
[Rule]Always read the entire input content usingsys.stdin.read()and split strictly by newlines
to extract S and T, ensuring no characters are dropped or misread during the input parsing phase.
[Example]Given sample input"afwgebrw\naoarbrenq", ensure the split yields
["afwgebrw", "oarbrenq"]. If the read process misses the final newline or splits incorrectly, the
second string might be truncated, causing a length mismatch error immediately.
[Error]Outputting the result inside a function without calling it, or hiding the code block in a snippet
that isn’t executed, resulting in no visible output matching the problem’s requirement for a list of numbers
and strings.
[Rule]The final response must explicitly print the formatted answer to stdout as plain text (the count
followed by each string on a new line) rather than returning a value from a function or providing unexe-
cuted code.
[Example]Correct output format for count 3 and strings"abc","def"is the three lines3/abc/
def. Incorrect: a block of codesolve()that returns[3, "abc", "def"], or a function definition
without invoking it.
PITFALLforesightz fore, predicted from the problem alone
[Error]Assuming propagating the full set of colors (e.g., usingstd::setor a boolean array) leads
toO(N)per move, causingO(N Q)total time complexity which exceeds the limit.
[Rule]Use Linked Lists to represent disjoint sets of colors in each box, merged inO(min(|S A|,|S B|))
time, avoiding iterating over all elements when merging.
[Example]If box A has{1,2}and box B has{10,20,30,40,50}, iterate only over{1,2}from A,
check their existence in B efficiently, and merge; do not iterate the 5 elements of B.
[Error]Failing to correctly handle the case where the destination box is empty or contains only dupli-
cates of colors already existing, resulting in counting the same color multiple times or missing the new
39

Preprint
 Salesforce AI Research
ones.
[Rule]Only count a color in the destination if it is not already present there before attempting the merge,
ensuringO(1)addition per element.
The blind foresight reasons entirely about asymptotics and data structures — correctly identifying
theO(N Q)trap, though prescribing the wrong structure for it — and says nothing about how the
program must consume its input, which is what actually decided four of the eight rollouts. This is
the asymmetry the case is meant to isolate: the algorithmic content is inferable from the problem
statement, and the policy does infer it; the execution contract is not, and the policy does not.
F.3 INTERACTION-GROUNDEDFORESIGHT IN ANAGENTENVIRONMENT
In the agentic mixture the environment observationisthe prospection context: the string below fills
thePROBLEMfield of both prospection prompts, and the only tools declared arealfworld step
andwebshop step, each returning the current state together with the list of currently admissible
actions. The task below is hard for a reason worth stating precisely: its optimal solution is exactly
eight actions against an eight-turn cap, so a single wasted move is fatal, and reaching it requires a
constraint that appears in no part of the prompt.
Example from # ALFWorld (task type=pick two obj and place)
Initial observation:
-= Welcome to TextWorld, ALFRED! =-
You are in the middle of a room. Looking quickly around you, you see a armchair 2, a armchair 1, a
cabinet 4, a cabinet 3, a cabinet 2, a cabinet 1, a coffeetable 1, a drawer 4, a drawer 3, a drawer 2, a drawer
1, a dresser 1, a garbagecan 1, a sidetable 1, and a sofa 1.
Task:put two creditcard in armchair.
Group:1/8rollouts win. All eight spend the full8-action budget; there are no tool errors, so every failure
is semantic.
drawer 1 drawer 2 drawer 3 drawer 4
cabinet 1 cabinet 2 cabinet 3 cabinet 4
dresser 1
sofa 1
START coffeetable 1 armchair 1 sidetable 1
creditcard 2 goal receptacle creditcard 1
T1–2 go, take card 2
T3–4 go,placecard 2 T5–6 go, take card 1
T7–8 go, place card 1
swept by four rollouts, all empty winning route —armchair 1twice, since card 2 must be put down before card 1 can be taken
Figure 5: Both cards sit on furniture named in the opening observation. Four of the eight rollouts
nonetheless sweepdrawer 1--4orcabinet 1--4and never reach them. The winning route
returns toarmchair 1a second time: the first card has to be deposited before the second can be
picked up, so the detour is forced, and the four legs consume the eight-action budget exactly.
40

Preprint
 Salesforce AI Research
Success Case (8 actions, episode won with zero slack)
T1 go to coffeetable 1 -> On the coffeetable 1, you see a box 1, a
creditcard 2,
a statue 1, and a watch 2.
offers: take box 1 ..., take creditcard 2 ...
T2 take creditcard 2 from coffeetable 1 -> You pick up the creditcard 2.
offers: move creditcard 2 to coffeetable 1
<- every ‘take’ has disappeared
T3 go to armchair 1 -> offers: move creditcard 2 to armchair 1
T4 move creditcard 2 to armchair 1 -> You move the creditcard 2 to the
armchair 1.
offers: take creditcard 2 from armchair 1
T5 go to sidetable 1 -> On the sidetable 1, you see a creditcard 1.
offers: take creditcard 1 from sidetable 1
T6 take creditcard 1 from sidetable 1 -> You pick up the creditcard 1.
T7 go to armchair 1 -> On the armchair 1, you see a creditcard 2.
T8 move creditcard 1 to armchair 1 -> You move the creditcard 1 to the
armchair 1.
[WIN]
Failure Case (finds both cards, then stalls on the carry limit)
Turns 1–3.Identical to the winner for two moves, then it goes looking for the second cardwhile still
holding the first.
T1 go to coffeetable 1 -> ... a creditcard 2 ...
T2 take creditcard 2 from coffeetable 1 -> You pick up the creditcard 2.
T3 go to sidetable 1 -> On the sidetable 1, you see a creditcard 1.
offers: move creditcard 2 to sidetable 1
<- NOT ‘take creditcard 1’
Turn 4.The card is visibly on the table, so the model reaches for it.
Reasoning Content:Great! I found creditcard 1 on sidetable 1. Now I need to take it. Let me take
creditcard 1 from sidetable 1.
T4 take creditcard 1 from sidetable 1 -> Nothing happens.
Turns 5–6.It reads the admissible list, sees the action missing, and cannot infer why — spending two
of its remaining four turns onexamine.
Reasoning Content (T5):Hmm, “Nothing happens” and the admissible actions still don’t include
“take creditcard 1 from sidetable 1”. This is strange. Let me check the admissible actions more
carefully.
Reasoning Content (T6):Still can’t take creditcard 1. The admissible actions still don’t show “take
creditcard 1 from sidetable 1”. But I saw it before when I arrived at sidetable 1.
The recollection is false — the offer was withdrawn the moment the first card was picked up — and
the rollout never recovers.
Turns 7–8walk back tocoffeetable 1andsidetable 1with the budget gone.
The supervision SRD builds from this group.The two substantive blocks of the aggregated
hindsight partition the group’s failures exactly: the first covers the four rollouts that sweptdrawer
1--4orcabinet 1--4, the second covers the three that found both cards and then violated the
carry limit. The first block diagnoses its failures correctly but overshoots in the remedy — “traverse
the entire state space of known furniture” is not available under an eight-action cap, and the lesson
the four sweeps actually support is the narrower one of not spending the whole budget on a single
receptacle class.
41

Preprint
 Salesforce AI Research
Group-aggregated PITFALLhindsightz hind (ALFWorld)
[Error]The agent exhaustively searches specific container types (e.g., cabinets or drawers) without ex-
ploring other available locations (e.g., tables, dressers, armchairs) before concluding an object is missing.
[Rule]In spatial reasoning tasks, one must systematically traverse the entire state space of known fur-
niture and locations rather than stopping after inspecting a few containers of the same type.
[Example]If searching all drawers yields no results for a key, the agent must proceed to check the
coffee table, desk, or bed instead of immediately claiming the object is absent.
[Error]The agent attempts to “take” objects while holding other items or fails to recognize that admis-
sible actions change from “take” to “move” based on inventory state.
[Rule]Always inspect the current inventory and the specific admissible actions list before executing a
manipulation command; if holding an item, use “move” to place it, while using “take” only for unheld
items.
[Example]If holding “item A” and standing at “Location B” containing “item C”, calling “take C from
B” fails; the correct sequence involves moving “A” first or navigating differently to acquire “C” via valid
actions.
PITFALLforesightz fore, predicted from the observation alone
[Error]Focusing on the object count (seeing “cabinet 1” vs “cabinet 2”) instead of the functional
property (identifying which furniture items can actually “hold” an item like a credit card).
[Rule]Only define an object as a valid container if the problem description explicitly uses a verb like
“in” or states the object can hold items.
[Example]If the goal is to “put” an item, ignore “garbagecan 1” because the text never says things are
“in” the garbagecan, whereas “armchair 1” is the intended target.
[Error]Repeatedly moving the agent to the same location instead of scanning the list of objects to find
multiple valid “armchair” entries or checking if the current container can hold the card.
[Rule]If the task requires placingtwoitems, verify that the destination object is either a single container
capable of holding multiple items OR that there are at least two distinct containers of that type available
in the scene.
[Example]If the instruction is “put two keys in drawer,” and the scene only lists one “drawer 1,” the
solver must check if “drawer 1” can hold more than one item; if not, they must look for a second drawer.
[Error]Assuming the task is complete after placing the first credit card because the command was
interpreted as a single action rather than a quantity requirement.
[Rule]The imperative “put X of [count] [object] in [container]” implies a sequence of [count] successful
placement actions must be verified before declaring the task done.
[Example]For the command “put two pens in box,” the solver must place pen #1, confirm it is “in box,”
and then immediately repeat for pen #2.
What the interaction supplied.The blind foresight gets the shape of the problem right and the
location of the constraint wrong, which is the most informative way it could fail. Its second block
correctly anticipates that a two-object task has a capacity problem, and then places that capacity
on thedestination: it asks whetherarmchair 1can hold two cards, and advises hunting for a
second armchair if not. The real limit is on theagent— one carried object at a time — and it is
enforced by withdrawing everytakefrom the admissible list the instant the first card is in hand.
No observation states the rule in words; it is disclosed only implicitly, as a change in the action
set between the empty-handed and holding states, and the agent has to induce the constraint from
that difference. The failing rollout registers the difference — it reads the list and notes the action is
absent — but cannot make the inference, and concludes only that the situation is “strange”.
That asymmetry is what the PITFALLchannel is being asked to close here. The hindsight states the
rule in the environment’s own terms —admissible actions change from ‘‘take’’
to ‘‘move’’ based on inventory state— and pairs it with the ordering that fol-
lows: place before you collect again. Neither the task string (put two creditcard in
armchair) nor the tool schema contains that fact. Seven of the eight rollouts fail under the zero-
slack budget, and they fail in two distinguishable ways: four spend it sweeping receptacle classes
42

Preprint
 Salesforce AI Research
that never held the cards, while three reach both cards and are stopped by the carry constraint they
could not have known.
F.4 ALL-SUCCESSGROUPS AND THEKNOWLEDGECHANNEL
A group in which every rollout succeeds is reward-uniform for the same structural reason as an
all-fail group:ˆp= 1, the advantage vanishes for every token, and a group-relative objective learns
nothing from it. It is also the half of the construction that the PITFALLchannel cannot serve, since
there is no failure to diagnose. The group below is drawn from the run in which both channels are
distilled and the KNOWLEDGEstudent is blind to the solution.
Example from # DAPO-Math — an all-success group
Problem.Suppose thatx,y,zare positive reals satisfying
x2 +xy+y 2 = 64, y 2 +yz+z 2 = 49, z 2 +zx+x 2 = 57.
Then 3√xyzcan be expressed as m n withm, ncoprime positive integers. Computem+n.
Answer:69
Group outcome.r(τ i) = 1for alli= 1, . . . ,8; tool calls per rollout[2,5,1,2,2,4,3,2].
What the student prospects.The KNOWLEDGEforesights for this group, sampled independently
from the problem alone. They agree: all read thea 2 +ab+b 2 form as a120 ◦ Law of Cosines and
propose the Fermat-point construction.
KNOWLEDGEforesightz fore — rollout A
[Knowledge/Rule]A rule for decoding cyclic systems with quadratic forms resembling the Law of
Cosines.Many equations involving three variables in cyclic quadratics (e.g.a 2 +ab+b 2 =C) correspond
to the Law of Cosines in triangles with a fixed internal angle of120 ◦ (cos 120◦ =− 1 2 ). Treatingx, y, z as side lengths from a common pointO, the system implies that they form the sides of a triangle with a
120◦ angle between each adjacent pair when arranged around a central point.
[Details/Examples]Constructing a figure whereOA=x,OB=y,OC=zmeet at120 ◦ angles
allows one to compute the sides of triangleABCfrom the given constants. The area can then be calculated
two ways — as the sum of three smaller120 ◦ triangles, and by a standard side-area formula — to relate
xyzto the constants.
KNOWLEDGEforesightz fore — rollout B
[Knowledge/Rule]Recognizing algebraic structures based on the Law of Cosines, where a system
involving three pairs of variables matching the forma 2 +ab+b 2 =krepresents the squared side lengths
of triangles with angles of120 ◦.
[Details/Examples]The equationa 2 +ab+b 2 =c 2 represents a triangle with sidesa,b,cwhere
the angle oppositecis120 ◦. If three such equations form a cycle forx, y, z, they can be visualized as
three sides of a larger triangle containing a central point where the pairwise angles are all120 ◦.
[Knowledge/Rule]Using Ptolemy’s Theorem or coordinate geometry to relate the geometry of a
cyclic quadrilateral (or the specific120 ◦ configuration) to the product of the legs of the component tri-
angles, often leading to a calculation involving the area or specific side lengths of the constructed larger
triangle.
[Details/Examples]Ifx, y, zare sides of triangles with a common120 ◦ vertex joined cyclically,
the outer triangle’s side lengths satisfyL x =
p
y2 +yz+z 2, etc. The system impliesx, y, zcorrespond
to segments forming a larger triangle with sides
√
64 = 8,
√
49 = 7,
√
57. One can use the area of this
larger triangle, or direct algebraic relations from the cosine law, to findxyz.
[Knowledge/Rule]Applying principles of symmetric systems, or algebraic identities for cyclicx 2 +
xy+y 2 sums, to extract the productxyzwithout solving for individual variables — often using the
43

Preprint
 Salesforce AI Research
relationship between the area of the outer triangle and the areas of the inner sub-triangles.
[Details/Examples]A common technique involves realizing the outer triangle is constructible and
using Heron’s formula or vector algebra to isolate the term under the cube root.
What the trajectories actually did.The anticipation is stable; the realizations are not. Across the
eight correct rollouts we find at least three distinct routes, two of which are shown below.
Trajectory A — exact symbolic elimination (1 tool call)
Reasoning Content:These equations look similar to the law of cosines [. . . ]x2 +y 2 −2xycos(120 ◦),
sincecos(120 ◦) =−1/2. So this suggests we could think of these as distances in a triangle with120 ◦
angles.
Actually, let me try a different approach.[. . . ] Let me subtract equations to find relationships between
the variables.
Tool:code interpreter
from sympy import symbols, solve, Eq
x, y, z = symbols(’x y z’, positive=True, real=True)
solution = solve((Eq(x **2 + x *y + y **2, 64),
Eq(y**2 + y *z + z **2, 49),
Eq(z**2 + z *x + x **2, 57)), (x, y, z))
Result:Solutions: [(64/13, 56/13, 49/13)] xyz: 175616/2197
Final Answer.Subtracting pairs gives(x−z)S= 15,(y−x)S=−8,(z−y)S=−7with
S=x+y+z; substituting intox+y+z=Syieldsx=S/3 + 23/(3S),y=S/3−1/(3S),
z=S/3−22/(3S), and the first equation then forcesS 2 = 169orS 2 = 1. Positivity selectsS= 13,
so 3√xyz= 56/13andm+n= 69.The geometry is never used.
Trajectory B — geometric reading, then numeric solve and rational reconstruction (2
tool calls)
Reasoning Content:x 2 +xy+y 2 =x 2 +y 2 −2xy(−1/2), so this corresponds tocosC=−1/2,
which meansC= 120 ◦. So if we imagine a pointOand three pointsA, B, Csuch thatOA=x,
OB=y,∠AOB= 120 ◦, thenAB 2 =x 2 +y 2 +xy= 64, soAB= 8; likewiseBC= 7and
CA=
√
57. The angles aroundOsum to360 ◦ [. . . ]
Tool:code interpreter— numeric solve from several initial guesses.
solutions = sympy.nsolve((eq1, eq2, eq3), (x, y, z), (5, 4, 3))
for guess in [(6, 4, 3), (5, 5, 4), (4, 6, 3), (4, 4, 5)]:
sol = sympy.nsolve((eq1, eq2, eq3), (x, y, z), guess)
Result:
Numerical solution: Matrix([[4.92307692307692],
[4.30769230769231],
[3.76923076923077]])
Then:recognises 3√xyz≈4.30769≈56/13, conjectures(x, y, z) = (64/13,56/13,49/13), and
verifies those rationals exactly against all three equations.
Final Answer. 3√xyz= 56/13, som+n= 69.
One anticipation, many realizations.A third rollout parametrises directly byS, solvesx 2 +xy+
y2 = 64forS∈ {1,13}, and rejectsS= 1on the grounds that it forcesy= 0andz=−7. So
the group contains an exact algebraic elimination, a numeric solve with rational reconstruction, and
a parametrise-then-prune argument — all reaching56/13, none of them the area double-count that
every foresight proposed.
This is the sense in which the KNOWLEDGEchannel is not a request forthemethod. The teacher
for each rollout is privileged with that rollout’s own trajectory, so the same stable anticipation is
paired with three different realizations, andL SRD pulls the prediction toward the route that rollout
44

Preprint
 Salesforce AI Research
actually had available rather than toward a canonical solution. The diversity is the asset: a group that
a group-relative objective sees as eight identical zeros of advantage is, to a prospective objective,
eight different demonstrations of what this problem admits.
F.5 HOWEACHCHANNEL’SFORESIGHTCHANGES OVERTRAINING
This section asks a different question: conditional on a channel, does thecontentof the prediction
change? To avoid confounding the answer with the shifting domain mix, we hold the domain fixed
to mathematics and compare early against late records of each channel in the dual-channel run.
KNOWLEDGE: from a single identity to a solution strategy.The two problems compared are
both algebraic-system questions from DAPO-Math.
Problems
Step 1.The numbers 1 1 , 1 2 , . . . ,1 2010 are written on a blackboard. A student chooses any two of the numbers, sayxandy, erases them, and then writes downx+y+xy. He continues this process until only
one number is left on the blackboard. What is this number?
Step 45.Supposew, x, y, zsatisfy
w+x+y+z= 25, wx+wy+wz+xy+xz+yz= 2y+ 2z+ 193.
The largest possible value ofwcan be expressed in lowest terms as w1 w2 for integersw 1, w2 >0. Find w1 +w 2.
Early KNOWLEDGEforesights tend to name one transferable fact and stop. The step-1 example
is a good one — it spots the substitution that linearises the whole problem — but it is a single
observation.
KNOWLEDGEforesight — step 1
[Knowledge/Rule]The operationx◦y=x+y+xyis associative and commutative, meaning
the final result depends only on the set of initial numbers, not the order of operations. This operation is
isomorphic to standard multiplication via the transformationf(z) =z+ 1.
[Details/Examples]Transform the operation by lettinga ′ =a+ 1. Then the new operation on
primed values becomesa ′ ◦′ b′ =a ′b′. Thus iteratingx◦yon the original numbers is equivalent to
multiplying their(value+ 1)counterparts. For example, applying the rule to{1,2}:(1◦2) + 1 = 6,
which equals(1 + 1)(2 + 1) = 6.
Late KNOWLEDGEforesights more often lay out aroute: several facts ordered so that each one
licenses the next.
KNOWLEDGEforesight — step 45
[Knowledge/Rule]Vieta’s formulas for quadratic roots.A polynomialt 2 −(sum)t+ (product) = 0
has roots whose sum is the coefficient oftwith opposite sign. This allows grouping variables into quadratic
equations when a sum and product relationship are known.
[Details/Examples]Ifa+b=Sandab=P, they are the roots oft 2 −St+P= 0. Ifa+b= 5
andab= 6, thent 2 −5t+ 6 = 0givest= 2,3.
[Knowledge/Rule]Non-existence of real roots.A quadraticat 2 +bt+c= 0with real coefficients
has no real solutions iff its discriminant∆ =b 2 −4acis negative; equal real roots occur at∆ = 0.
[Details/Examples]Fort 2 −4t+ 5 = 0,∆ = 16−20 =−4<0, so no realtsatisfies it.
[Knowledge/Rule]Optimisation of one variable under real-solvability constraints.To maximisew
wherex, y, zmust remain real, eliminate the secondary variables to form an inequality inw. The boundary
of the feasible region occurs when the auxiliary quadratic has a repeated real root, i.e. when its discriminant
is exactly zero.
45

Preprint
 Salesforce AI Research
[Details/Examples]Express the constraint as a quadratic in one variable and require∆≥0; the
extremum sits at∆ = 0.
The three blocks are not independent facts: Vieta turns the symmetric constraints into a quadratic,
the discriminant condition turns “the other variables are real” into an inequality, and the third block
says where in that inequality the optimum lies. That composition is what is absent from the step-1
example, which states its identity and stops.
PITFALL: from generic procedure to problem-structure traps.The two problems compared
are both algebraic-system questions from DAPO-Math.
Problems
Step 0.Determine the real numberasuch thatf(a) =ais a relative minimum of the functionf(x) =
x4 −x 3 −x 2 +ax+ 1.
Step 47.Find the sum of all positive integersnsuch that 2n+ 1 n(n−1) has a terminating decimal representa-
tion.
The early PITFALLforesights read like exam advice — correct, but about the method in general
rather than about this problem.
PITFALLforesight — step 0
[Error]Confusing the definition of “absolute” minimum with “relative” (local) minimum, or assuming
the critical point atx=amust be the global minimum of the function onR.
[Rule]Apply the second-derivative test to classify critical points locally, without evaluating global
behaviour unless explicitly required. Forf(x), check whetherf ′′(a)>0for a relative minimum.
[Example]Forf(x) =x 2, the critical pointx= 0is a relative minimum becausef ′′(0) = 2>0,
even though it is also the absolute minimum.
Later ones more often name a trap that exists only because of howthisexpression is built.
PITFALLforesight — step 47
[Error]Overlooking the factor ofn−1in the denominator when reducing the fraction. Since the
expression is(2n+ 1)/(n(n−1)), the denominator isn(n−1). A solver might only check the prime
factors ofnand ignore(n−1), leading to false positives.
[Rule]To ensure the reduced denominator is of the form2 a5b, both factors of the unreduced denomi-
nator,nand(n−1), must contribute only the primes2and5after cancelling any common factors with
the numerator(2n+ 1).
[Example]Forn= 4: denominator4·3 = 12, numerator9, fraction9/12 = 3/4, denominator2 2 —
valid. Forn= 3: denominator3·2 = 6, numerator7, fraction7/6, denominator has a factor3— invalid.
46
