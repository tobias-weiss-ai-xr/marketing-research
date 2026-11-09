---
title: 'SCOPE: Score-Isolated Agentic Optimization for Video World Models'
url: https://arxiv.org/abs/2608.15043
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Yuhua Jiang
- Jiaming Wang
- Qingbin Liu
- Feifei Gao
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.15043
pages: 17
chars: 58822
fetched_at: '2026-11-08T13:32:19+00:00'
kb_version: 1
---

# SCOPE: Score-Isolated Agentic Optimization for Video World Models

SCOPE: SCORE-ISOLATEDAGENTICOPTIMIZATION
FORVIDEOWORLDMODELS
Yuhua Jiang
Tsinghua University
Jiaming Wang
National University of Singapore
Qingbin Liu
Tencent
Feifei Gao
Tsinghua University
ABSTRACT
Video world models are increasingly used as simulators for planning and embod-
ied decision making, yet improving them at inference time introduces a subtle
evaluation problem: prompts, samplers, verifiers, and selectors may evolve to-
gether, making it difficult to attribute gains or prevent held-out feedback from
shaping the final policy. We introduce SCOPE(Score-Isolated Control Optimiza-
tion with Provenance-Bound Evidence), a framework for auditable inference-time
adaptation of frozen video world models. SCOPErepresents external controls
as a typed state, updates this state only through bounded changes supported by
development evidence, and freezes the resulting policy before held-out evalua-
tion. On Physics-IQ benchmark, SCOPEimproves over the exact frozen base by
+14.24 (95% CI [+8.10,+21.23] ). Controlled ablations further identify gains
from scene specification, sampling, and learned selection, while the margin over
the strongest matched agentic baseline remains unresolved. Cross-backbone and
prospective evaluations reveal a complementary result: useful inference-time up-
dates exist, but their benefits do not transfer uniformly across models and set-
tings. Together, these findings suggest that reliable inference-time adaptation
requires not only better proposals, but also a principled mechanism for deciding
which updates should become part of the deployed system. Code is available at
https://github.com/YuhuaJiang2002/SCOPE.
1 INTRODUCTION
Video world models provide a flexible interface for predicting future visual states and are increasingly
used for simulation, planning, and embodied decision making. Yet visually plausible videos are not
necessarily physically consistent, and retraining a large backbone for every new task is expensive.
This motivates inference-time adaptation: improving a frozen model through external controls such
as prompts, sampling strategies, verifiers, retrieval, and candidate selection.
The challenge is that these controls are typically coupled. An agent may rewrite a prompt, alter the
sampler, call a tool, rerank candidates, and reuse previous experience within the same workflow.
If several choices change at once, a higher final score does not identify which intervention was
responsible. More importantly, if held-out outcomes are reused to choose later controls, the system
can adapt to the evaluation itself. We refer to this as theinference-control evaluation gap: the gap
between observing an improvement and establishing that it comes from a well-defined inference-time
intervention.
We address this problem with SCOPE, short forScore-Isolated Control Optimization with Provenance-
Bound Evidence. SCOPEtreats the external inference harness as an explicit state Ωr containing
typed text, sampler, verifier, and reward controls. At each development round, an agent proposes a
bounded update. The update is accepted only using a predefined development objective; otherwise
the previous state is retained. The final route, including an exact Frozen Base fallback, is fixed before
held-out evaluation. This design separates three objects that are often conflated in agentic systems:
the proposed update, the deployed control state, and the score used to evaluate it.
1
arXiv:2608.15043v1  [cs.AI]  15 Aug 2026

We evaluate SCOPEfrom controlled components to the full inference-time system. SceneLang
conditioning, a sampler modification, and supervised best-of-N selection each improve their matched
controls. On the 40-scene Physics-IQ common-base protocol, the complete procedure reaches a P-IQ
score of 34.94 and improves over exact Base by +14.24 (CI [+8.10,+21.23] ), although the margin
over the strongest matched Qwen-Image-Agent-style baseline remains unresolved. Cross-backbone
experiments on Wan2.2 and CogVideoX, together with P-AI, OpenS2V-Eval, and prospective evalua-
tions, show a complementary result: improvements found during development do not reliably transfer
across all backbones, metrics, or unseen tasks. This distinction betweenfindinguseful updates and
reliably selectingthem is central to our analysis.
Contributions.Our contributions are threefold:
• We formulate the inference-control evaluation gap for agentic adaptation of frozen video world
models and separate proposed updates, deployed controls, and held-out evaluation.
• We introduce SCOPE, a typed inference-control framework with bounded updates, an exact Base
fallback, and a score-isolated update rule that prevents held-out scores from changing the deployed
state.
• We provide matched experiments across controls, backbones, and benchmarks. SCOPEimproves
over exact Base on the matched Physics-IQ protocol, while ablations and prospective evaluations
identify where component gains transfer and where selection remains unreliable.
2 RELATEDWORK
Physics-aware video generation.Training-time methods inject physical supervision, imagined
trajectories, latent motion priors, or geometry rewards into model parameters (Zhang et al., 2026a;
Wang et al., 2026; Jiang et al., 2026; Li et al., 2026a). Retrieval-based methods instead augment
generation with external physical knowledge (Cheng et al., 2026), while PhyGround and WorldRea-
sonBench stress-test physical reasoning and future-state prediction (Lin et al., 2026a; Wu et al., 2026).
Our setting instead keeps the video backbone fixed and studies reversible inference-time controls
under matched evaluation.
Inference-time alignment and scaling.WMREWARD, VIGOR, and VHS rank or steer generated
samples with latent-world, geometric, or hidden-state critics (Yuan et al., 2026; Yin et al., 2026;
Bucciarelli et al., 2026); iterative refinement and repeated sampling spend additional test-time
compute through different operators (Kang et al., 2026; Brown et al., 2024; Ma et al., 2025). These
methods primarily optimize a particular search or reward mechanism. SCOPEinstead places prompts,
samplers, verifiers, and rewards in a common typed control space and evaluates each change against
a matched protocol-local Base.
Agentic generation and tool orchestration.A closer comparison comes from agentic systems
that improve generation through feedback, planning, and reusable tools. Qwen-Image-Agent closes
context gaps through tool-augmented feedback, NEWTON plans physically grounded videos, and
LingBot-World structures interactive world generation (Zhang et al., 2026c; Feng et al., 2026; Gao
et al., 2026). GenEvolve and COMFYCLAW further organize tool calls and reusable workflow
experience for visual generation (Chen et al., 2026b; Li et al., 2026b). Tool-augmented systems can
change retrieval, segmentation, geometry, and proposal quality simultaneously, making attribution
difficult. SCOPEtherefore contributes a score-isolated update rule rather than a new search, segmenta-
tion, or foundation model. The selected route or Base fallback is fixed before held-out scoring, which
enables matched ablations of individual controls.
Persistent skills and self-evolving harnesses.SkillOpt, SkillCAT, and SkillDAG update or select
reusable agent skills (Yang et al., 2026; Chen et al., 2026a; Bai et al., 2026); Library Drift and
Harness Updating Is Not Harness Benefit expose failure modes in evolving skill libraries (Zhang
et al., 2026b; Lin et al., 2026b). SCOPEsimilarly maintains a persistent typed control state, but
restricts updates to development evidence while keeping validation and confirmation read-only. This
separates the mechanics of updating an inference harness from evidence that the update improves
held-out performance.
2

proposal context (replaceable infrastructure)
prompt
first frame
VLM feedback
or Director card
tool calls
image search /
sam segment
frozen ledger
references, masks,
event notes
proposal set
As
Base
fallback
typed control state
Ωr: text · noise
verifier · reward
bounded edits
add / delete
/ replace
retirable cards
provenance + guards
conflicts, risk,
Base fallback
score-blind policy
qΩr , captions,
reward, task evidence
freeze before score
a⋆(s) or Base
1 2
Frozen Wan2.2 WM
pθ(y|x 0, c)
weights fixed
generate mp4
from frozen
choice
development ac-
ceptance rule
objective improves
and all guards pass
accept Ωr+1
before held-out
evaluation
reject edit
preserve Ωr
3
otherwise3 score-isolated state update: an accepted edit becomes the next typed state
4 held-out scores are read-only:validation / confirmation cannot change ΩR or the frozen route a⋆(s).4
SCOPECORE A: typed, score-blind control policy
SCOPECORE B: score-isolated state update
Figure 1:Overview of SCOPE.Proposal mechanisms in the gray band are replaceable. SCOPE
maintains(1)a typed state over text, noise, verifier, and reward controls;(2)a score-blind deployment
choice with an exact Base fallback;(3)a development-time state update that accepts or rejects
bounded edits; and(4)a score-isolation constraint that keeps held-out outcomes read-only. Only the
external inference state changes; model weights remain frozen.
Adaptive evaluation and safe updates.Reusable-holdout methods study validity under repeated
adaptive queries, while high-confidence policy evaluation asks whether a proposed policy is safe
to deploy from a conservative lower bound (Dwork et al., 2015; Thomas et al., 2015). These ideas
motivate the score-isolation principle in SCOPE. The method prevents direct adaptation to held-out
scores, while repeated development on the same ledger can still overfit; prospective evaluation on
disjoint tasks therefore remains necessary.
3 METHOD
3.1 PROBLEMFORMULATION ANDOVERVIEW
Let pθ(x1:T |x 0, c)denote a pretrained video world model, where x0 is the initial observation, c
is the conditioning signal, and x1:T is the generated trajectory. Throughout adaptation, the model
parameters θ remain frozen. Rather than modifying the world model itself, we adapt an external
inference-time control state
Ω∈ C,(1)
where C denotes the space of admissible inference controls. A control state may contain textual
directives, sampling configurations, verification or abstention rules, and reward-based selectors.
Starting from an initial state Ω0, an agent proposes a sequence of bounded edits δ0, . . . , δR−1. State
evolution is governed by a development-only update operator,
Ωr+1 =U r(Ωr, δr;D r), r= 0, . . . , R−1,(2)
where Dr is the sealed development ledger available at round r. Each edit modifies a declared
component of the current control state, while Ur determines whether the edit is committed. Crucially,
Ur has access only to admissible development evidence; held-out evaluation outcomes are never valid
inputs to the update process.
After R development rounds, the resulting state ΩR is frozen. For an evaluation instance s, the frozen
state induces the deployment policy
πΩR (s) =F(Ω R, xs,A s),(3)
3

where xs denotes the available input and As is the corresponding candidate set. The complete
routing rule, including the exact Frozen Base fallback, is fixed before the held-out evaluation score is
revealed.
This formulation separates two questions that are often conflated in inference-time adaptation:which
intervention improves development behavior, andwhich intervention is admissible for deployment.
We therefore formulate adaptation as constrained control-state optimization around a frozen world
model, rather than unconstrained search over prompts, samplers, or candidate outputs.
3.2 SCOPE: STRUCTUREDINFERENCE-TIMECONTROL
SCOPEinstantiates the above formulation with an explicit and persistent control state. At round r, we
decompose
Ωr =

Ωtext r ,Ω sample r ,Ω verify r ,Ω select r  ,(4)
where the four components respectively encode textual directives, sampling controls, verification and
abstention rules, and reward-based selection mechanisms.
The decomposition makes interventions explicit and independently editable. More importantly, it
separates four conceptually distinct operations:proposal,commitment,deployment, andevaluation.
At each round, a proposer suggests a bounded modification to one control axis; the update rule
determines whether that modification enters the persistent state; the final frozen state determines
deployment; and held-out evaluation measures the resulting policy without modifying it.
Formally, an axis-specific proposer generates
δr =P r(Ωr, Dr),(5)
where Pr may itself use VLM feedback, Director modules, retrieval, external tools, or predefined
proposal families. SCOPEdoes not constrain the internal form of Pr; instead, it specifies the interface
through which a proposal is allowed to modify persistent inference-time behavior.
Some components of Ωr may themselves be learned during development. For example, the reward
selector can be trained on disjoint Physics-IQ scenes. Once development terminates, however, its
parameters and inputs are treated as part of the frozen control state. At deployment it consumes only
label-free features and cannot be updated using held-out outcomes.
Figure 1 summarizes this separation between proposal generation, persistent control-state adaptation,
frozen deployment, and held-out evaluation.
3.3 DEVELOPMENT-ONLYCONTROL-STATEUPDATES
We restrict each proposal δr to a bounded elementaryadd,delete, orreplaceoperation on one
declared control axis. This restriction makes individual state changes attributable and prevents a
single proposal from silently modifying multiple components.
Let Jdev(Ω;D r) denote the predeclared development objective evaluated on ledgerDr. We define
the development contrast of proposalδ r as
∆dev r (Dr) =J dev  Ur(Ωr, δr);D r  −J dev  Ωr;D r  ,(6)
where Ur(Ωr, δr) denotes the state obtained by applying the proposed edit before acceptance testing.
In addition to improving the development objective, a proposal must satisfy a predefined collection
of admissibility constraints. Let
Gr,k

Ur(Ωr, δr);D r

≤0, k= 1, . . . , K,(7)
represent the individual guards, including motion, sharpness, identity preservation, and static-video
checks. We summarize their conjunction by
Gr(Dr) =
KY
k=1
1

Gr,k

Ur(Ωr, δr);D r

≤0

.(8)
4

The persistent state evolves through the commit-or-retain rule
Ωr+1 =
(
Ur(Ωr, δr),∆ dev r (Dr)>0∧G r(Dr) = 1,
Ωr,otherwise.
(9)
Equation 9 gives every persistent intervention an explicit acceptance criterion: an edit is committed
only when it improves its predeclared development contrast and satisfies every guard. Otherwise, the
incumbent is retained exactly.
Importantly, this rule does not assume that development improvement transfers monotonically to
unseen tasks, environments, or model backbones. Its purpose is narrower: to specify which evidence is
permitted to modify the deployed system and to prevent held-out evaluation feedback from becoming
an implicit optimization signal.
3.4 FROZENDEPLOYMENT ANDSCOREISOLATION
After the final development round, adaptation terminates and the state ΩR is frozen. For each
evaluation instances, the inference procedure constructs an admissible candidate set
As =
n
a(1) s , . . . , a(M) s , aBase s
o
,(10)
wherea Base s is the exact output of the Frozen Base system and is always retained as a fallback.
The deployed route is then fixed as
a⋆ s =π ΩR (s) =F(Ω R, xs,A s),(11)
before the official evaluation scorey s is revealed. Equivalently, the complete deployment mapping
ΦΩR : (s,A s)7− →a⋆ s (12)
is precommitted before held-out evaluation.
Optional MAGE-lite memory may supply capability, task, experience, or environment records toF .
Such records are treated as part of the frozen inference state: they may be constructed or updated
during development, but cannot be modified using held-out outcomes.
This ordering yields a simple score-isolation property.
Proposition 1(Score-isolation invariant).Fix the proposal randomness, sealed development ledgers,
candidate construction procedure, world model, evaluation inputs, and fallback rule. Replacing the
complete validation, confirmation, held-out, or official-score ledger by arbitrary alternative values
leaves both the final control state ΩR and every frozen deployment route a⋆ s unchanged prior to score
release.
Proof. By Equation 5, proposal δr is determined only by the incumbent Ωr, sealed development
ledger Dr, and fixed proposal randomness. Equation 9 likewise depends only on development
quantities associated with the current round. Therefore, by induction over r, the complete state
trajectory Ω0, . . . ,ΩR is invariant to any modification of held-out scores. Equation 11 subsequently
depends only on the frozen state ΩR, evaluation input xs, candidate set As, and the fixed fallback
rule. Hence every routea ⋆ s inherits the same invariance.
The proposition establishes a deliberately narrow guarantee: held-out scores cannot influence either
control-state adaptation or deployment routing. It does not imply that the proposal mechanism is
optimal, that development selection is unbiased, that development gains generalize to unseen settings,
or that SCOPEnecessarily outperforms a matched alternative. These are empirical questions addressed
separately in Section 4.
3.5 PROVENANCE-BOUNDUPDATERECORDS
Score isolation specifies which information may influence adaptation; provenance binding makes the
resulting state evolution auditable. We bind each attempted transition to the exact incumbent state,
proposal, and development evidence from which it was produced.
5

Let h(·) denote the SHA-256 hash of a canonical serialization of its argument, let br ∈ {0,1}denote
the commit decision, and let Rr contain the frozen outcomes and reasons of all admissibility guards.
Each attempted transition emits the record
Tr =

h(Ωr), h(δr), h(Dr), br,R r, h(Ωr+1)

.(13)
A proposal is admissible only if its recorded parent agrees with the current incumbent,
h(Ωparent r ) =h(Ω r).(14)
A committed proposal modifies exactly one declared control axis and advances the corresponding
revision. A rejected or retired proposal instead restores the incumbent exactly, which implies
br = 0 =⇒Ω r+1 = Ωr =⇒h(Ω r+1) =h(Ω r).(15)
Consequently, Tr distinguishes an edit that was merely proposed from one that actually modified the
persistent state, while binding every committed change to its parent state, development evidence, and
gate decision.
Evidence roles.Only evidence explicitly designated for development and sealed before evaluation
is admissible to Equations 5– 9. Validation, confirmation, official-score, held-out, and test fields are
excluded from the executable update interface. Each admissible transition records the development-
ledger hash, guard outcomes, commit decision, and resulting state hash.
This distinction has a direct operational consequence. Altering any held-out score leaves the ad-
missible inputs to Equation 9 unchanged and therefore cannot alter the deployed state. Altering
development evidence, in contrast, changes h(Dr) and defines a distinct provenance-bound transition
that must be evaluated independently. The resulting procedure therefore provides bothscore isola-
tion—held-out outcomes cannot drive adaptation—andtransition traceability—every persistent state
change can be replayed from its recorded parent, proposal, evidence, and decision.
4 EXPERIMENTS
4.1 EXPERIMENTALSETUP
We evaluate SCOPEwith two frozen video backbones, Wan2.2 and CogVideoX, across Physics-IQ,
P-AI (PAI-Bench-G), and OpenS2V-Eval. The main Physics-IQ comparison uses 40 scenes and
reports scene-level composite scores. P-AI evaluates the matched methods on the robot split6 tasks
with the official Qwen2.5-VL-72B judge and an eight-dimensional quality score. OpenS2V-Eval
contains 180 items per backbone and is used as a broader open-domain test. We additionally use
fresh Physics-IQ and PhyGround tasks for prospective evaluation.
All comparisons are performed within the same backbone and evaluation protocol. Unless noted
otherwise, deltas are paired against the corresponding Frozen Base and uncertainty is estimated using
a paired bootstrap over the protocol’s independent unit. The generator, candidate pool, deployment
route, and analysis unit are fixed before held-out outcomes are read. Secondary and post-hoc analyses
are reported descriptively rather than pooled with the primary comparison. Full protocol and statistical
details are provided in Appendix Table 8.
4.2 MAINRESULTS ONPHYSICS-IQ
Our primary experiment asks two questions under the same 40-scene protocol: whether SCOPE
improves over the exact Frozen Base and whether it improves over the strongest matched alternative.
Table 1 compares eleven methods under a matched evaluation protocol: all methods share the same
40 scenes, official scorer, candidate pool, and Base reference within each backbone. The retrospective
LingBot Director→Pilot baseline follows the same generation and evaluation protocol. Following a
post-score materialization failure, its score evidence was recovered by deterministic replay of the
original hash-bound videos, without additional selection or tuning.
On Wan2.2, SCOPEachieves the highest point estimate at 34.94, compared with32.87 for the strongest
non-SCOPEmethod, Qwen-Image-Agent-style feedback. The resulting +2.07 difference remains
6

Table 1:Common-base Physics-IQ comparison across two frozen video backbones.All rows
report the mean over 40 scene-level Physics-IQ composites. Within each backbone, methods share
the same Base and evaluation protocol. The SCOPE–Qwen differences are +2.07 on Wan (CI
[−0.27,+6.14] ) and +0.52 on CogVideoX (CI [−0.39,+1.65] ), and remain unresolved on both
backbones. Absolute scores are not compared across backbones. The dagger denotes the separately
generated fixed Director baseline; green indicates Base-relative intervals with positive lower bounds.
Method Wan P-IQ Wan∆(95% CI) CogVideoX P-IQ CogVideoX∆(95% CI)
Frozen Base20.70–22.91–
WMReward reward-only (Yuan et al., 2026)21.81 +1.11 [−0.40,+3.17] 26.10 +3.19 [+0.85,+6.04]
V AE-θreward22.33 +1.63 [−0.67,+4.46] 25.14 +2.23 [+0.02,+4.83]
VIGOR reward-only (Yin et al., 2026)25.15 +4.44 [+1.49,+7.96] 27.75 +4.83 [+1.71,+8.44]
uniform random 3-candidate selector (Brown et al., 2024; Ma et al., 2025)27.41 +6.71 [+1.93,+11.45] 30.57 +7.65 [+4.51,+10.97]
LingBot-style Director→Pilot proxy† (Gao et al., 2026)29.98 +9.27 [+2.37,+16.12] 34.91 +12.00 [+6.76,+17.62]
fixed GPT-5.4 physics card30.04 +9.33 [+2.50,+15.93] 34.89 +11.98 [+7.05,+17.13]
fixed rule refinement31.50 +10.80 [+2.67,+19.14] 33.89 +10.98 [+6.27,+15.93]
joint self-score ablation32.07 +11.37 [+3.38,+19.69] 34.63 +11.71 [+6.83,+16.66]
Qwen-Image-Agent-style feedback (Zhang et al., 2026c)32.87 +12.16 [+4.48,+20.06] 34.99 +12.08 [+7.36,+16.98]
SCOPE (ours)34.94+14.24[+8.10,+21.23]35.51+12.60[+7.73,+17.60]
unresolved (CI [−0.27,+6.14] ). LingBot obtains 29.98, corresponding to a +9.27 improvement over
Base (CI [+2.37,+16.12] ). Its nonlinear full-set aggregate (23.57) is reported separately and is not
included in the scene-mean ranking.
The clearest matched result is the comparison with Base: SCOPEimproves Physics-IQ by +14.24 (CI
[+8.10,+21.23] ). A descriptive analysis that holds the three generated candidates fixed also yields a
+7.53 improvement over uniform selection (CI [+4.04,+11.52] ). This latter comparison controls for
candidate generation, but was not designated as the primary contrast.
The result is clear relative to Frozen Base but less conclusive relative to the strongest matched
alternative. The direct SCOPE–Qwen comparison changes only 8/40 scenes (3/32/5 wins/ties/harms),
which explains the wider uncertainty in that contrast. Table 1 therefore reports the scene-equal
estimand. Because the official Physics-IQ composite is nonlinear, absolute rankings across alternative
aggregation schemes are not inferred from scene composites alone.
Figure 2:Evolution of the matched Physics-IQ policy across two frozen backbones.R0–R3
correspond to Base, the physics-card update, the rule-refinement update, and the final selected SCOPE
state. Curves show the mean Physics-IQ score over 40 scenes, with shaded 95% scene-bootstrap
confidence intervals. Scores are compared only within each backbone.
Figure 2 shows how the matched policy evolves through the four states used to construct the final
SCOPEpolicy. On Wan2.2, Physics-IQ increases from 20.70 at Base to 30.04, 31.50, and 34.94
7

Figure 3:Example of retrieval-assisted generation on Newton’s cradle.Retrieval provides a
textual concept card but no reference pixels or visual embeddings. Both Wan2.2 variants use the
same temporal anchoring operation. The visualization for OURS additionally includes the disclosed
endpoint-motion intervention and display-only hand replacements. This example is qualitative and is
not used as evidence for the aggregate tool-use effect.
Table 2:Cross-backbone results on P-AI (PAI-Bench-G).Deltas and paired 95% CIs are relative
to the Frozen Base of the same backbone. SceneLang is the strongest fixed-policy comparator. The
diagnostic SCOPErows report the better of two variants per backbone and therefore do not represent
a single transferable policy.
Matched method Wan Overall Wan∆(95% CI) CogVideoX Overall CogVideoX∆(95% CI)
Ranking-eligible matched methods
Frozen Base76.67–74.10–
+shared global76.86 +0.19CI[−2.13,+2.66] 74.41 +0.30CI[−2.15,+2.77]
LingBot-style Director→Pilot+shared global † 76.77 +0.10CI[−2.25,+2.54] 74.29 +0.18CI[−2.30,+2.69]
Qwen-Image-Agent-style (SceneLang)77.02 +0.35CI[−1.50,+2.32]74.72+0.62CI[−1.37,+2.68]
SceneLang+shared global77.01 +0.34CI[−1.86,+2.63] 71.57−2.53CI[−5.25,+0.12]
Post-hoc upper envelope; no ranking or promotion credit
SCOPEpost-hoc upper envelope ∗ 77.47+0.80CI[−1.38,+3.12] 74.48 +0.38CI[−1.56,+2.37]
across R1–R3. On CogVideoX, the corresponding trajectory is 22.91→34.89→33.89→35.51 .
Despite the intermediate decrease at R2 on CogVideoX, the final state improves substantially over
the exact Base on both backbones. This figure illustrates the evolution relative to Base rather than a
comparison with the strongest matched alternative. Additional Wan candidates evaluated in R4–R11
did not replace the R3 state and are omitted for clarity.
4.3 CROSS-BACKBONEGENERALIZATION
We next study whether the observed behavior transfers when both the video backbone and task
distribution change. Table 2 evaluates all methods on the same robot split6 tasks using the official
Qwen2.5-VL-72B judge and the same eight-dimensional QS evaluation contract.
Among the fixed policies, SceneLang achieves the highest point estimate on both backbones (77.02
on Wan and 74.72 on CogVideoX), although its Base-relative confidence intervals include zero. The
8

Table 3:Cross-backbone results on OpenS2V-Eval ( n=180 per backbone).Scores are multiplied
by 100 and compared only within each backbone. Mean† and Weighted† use the disclosed GPT-5.4
judge with a Qwen fallback proxy. ‡ denotes a prompt-only LingBot-style proxy.
Method Wan Mean † Wan Weighted† CogVideoX Mean† CogVideoX Weighted†
Frozen Base (Team Wan et al., 2025; Yang et al., 2025)37.46 36.60 48.30 48.29
Qwen-Image-Agent-style (Zhang et al., 2026c)38.72 37.92 46.73 46.16
LingBot-style Director→Pilot prompt proxy‡ (Gao et al., 2026)41.27 42.84 47.3949.62
GPT-5.4 first-frame skill (internal)38.31 39.33 46.67 47.99
SCOPE(ours)41.75 43.17 47.7649.22
diagnostic SCOPEupper envelope gives77.47on Wan using the shared-global variant and74.48on
CogVideoX using the no-global variant. Because these values are obtained by different variants, they
should not be interpreted as the performance of a single transferable policy.
The shared-global variant further illustrates this backbone dependence. It changes Overall per-
formance by +0.80 (CI [−1.38,+3.12] ) relative to Frozen Base on Wan2.2, but by −2.41 (CI
[−5.04,+0.13] ) on CogVideoX. Although neither interval is conclusive, the reversal in point es-
timates suggests that the effectiveness of this component depends on the underlying backbone.
Complete Wan profiles are provided in Appendix Table 9.
4.4 OPEN-DOMAINGENERALIZATION ONOPENS2V-EVAL
We next evaluate cross-backbone generalization in the broader open-domain setting of OpenS2V-Eval.
Within each backbone, all methods share the same frozen sampler configuration, and routing decisions
are fixed before evaluation.
For a matched agentic baseline, we construct a LingBot-style prompt proxy that injects a Qwen3.5-9B
caption of the first frame into a fixed Director→Pilot template, while keeping the video backbone and
sampler unchanged. This baseline isolates the contribution of structured agentic prompting within
our evaluation protocol; it is not intended to reproduce the trained LingBot-World system.
On Wan, SCOPEimproves over this proxy by +0.47 in Mean (CI [−0.45,+1.43] ) and +0.33 in
Weighted score (CI [−0.93,+1.62] ). On CogVideoX, the corresponding differences are +0.37 (CI
[−0.48,+0.98] ) and −0.40 (CI [−1.39,+0.51] ), respectively. All four confidence intervals include
zero, so these contrasts remain statistically unresolved. Notably, Frozen Base achieves the highest
Mean score on CogVideoX, whereas the LingBot-style proxy slightly exceeds SCOPEon the Weighted
metric. Taken together, these results indicate that the gains from learned inference-time control are
backbone- and metric-dependent, rather than uniformly transferable across configurations.
More broadly, the direction of the effect is not fully stable across backbones. The Mean difference
relative to the strongest comparator is slightly positive on both Wan (+0.47) and CogVideoX (+0.37),
whereas the Weighted difference changes from +0.33 to −0.40. P-AI exhibits an even larger
directional change, from +0.80 to −2.41 relative to the same-backbone Base. These results suggest
a backbone–metric interaction rather than a backbone-independent improvement.
Taken together, Physics-IQ, P-AI, and OpenS2V-Eval show that SCOPEis compatible with multiple
backbones and evaluation settings, but the effect of a particular control is not invariant to backbone
or metric. We therefore report cross-backbone results separately rather than pooling scores across
heterogeneous protocols.
4.5 PROSPECTIVEEVALUATION ONUNSEENTASKS
The previous experiments evaluate matched controls and cross-backbone behavior. We next test
whether development-time improvements persist when the selection policy is frozen and applied to
unseen tasks.
Table 4 summarizes four prospective tests. On fresh Physics-IQ tasks, neither the comparison with
Base nor that with the frozen router establishes a clear improvement. The typed updater likewise does
not outperform a matched random update and degrades 15% of scenes, exceeding the predeclared
10% tolerance. The grounded tool router improves over always-on tool use, whereas its contrasts
9

Table 4:Prospective evaluations.Positive effects favor the proposed method; PhyGround reports
proposal coverage against its predeclared minimum.
Evaluation Reference / Criterion Outcome
Fresh Physics-IQ Base+0.096 [−0.887,+1.077]
Frozen router−1.019 [−2.159,+0.146]
Typed update Random update−0.316 [−5.984,+5.145]
Tool router Always-on+0.660[+0.016,+1.315]
No tool+0.083 [−0.191,+0.381]
Random routing+0.002 [−0.281,+0.299]
PhyGround Min. proposal coverage:8/32 4/32
Table 5:Ablation studies of SCOPE.Each row reports a matched comparison and its 95% CI.
Component effects are protocol-specific and should not be added across rows.
Category Variant Comparison∆(95% CI)
Control
Text (SceneLang) vs. Base+5.62 [+0.55,+10.55]
Noise vs. fixed sampler+1.26 [+0.52,+2.01]
Reward vs. matched random+3.33 [+1.49,+5.30]
Reward vs. self-score+0.66 [−1.52,+2.92]
Region-state prior identity metric−7.28 [−13.33,−2.53]
Update
Random update vs.Ω 0 +4.53 [+1.14,+9.17]
Typed update vs.Ω 0 +4.22 [+0.81,+8.30]
Typed update vs. random update−0.32 [−5.98,+5.15]
No fallback vs. Base fallback−0.773 [−1.471,−0.203]
Tool
Retrieval vs. no tool+0.562 [−0.700,+1.967]
Retrieval + SAM vs. no tool+0.013 [−2.936,+3.263]
Incremental SAM vs. retrieval−0.548 [−3.390,+2.631]
with no-tool and same-budget random routing remain unresolved. PhyGround exposes a different
failure mode: only 4/32 tasks produce a valid proposal, below the predeclared minimum coverage
of 8/32. The proposal stage therefore fails its coverage gate before downstream tool quality can be
meaningfully assessed. Together, these results show that development-time component gains do not
yet yield robust improvement under prospective evaluation.
4.6 ABLATIONSTUDIES
We analyze three complementary aspects of SCOPE: individual control axes, control-state updates,
and external tool use. Table 5 summarizes all matched ablations. Because these experiments use
different controls and evaluation units, their effects are interpreted independently rather than combined
additively.
Component controls.The text and noise controls both improve their matched baselines, and
the learned reward selector outperforms matched random selection. Its advantage over self-score,
however, remains unresolved. The SceneLang interval is conditional on three fixed seeds. The reward
selector is trained with scene-grouped out-of-fold supervision and uses only label-free features at
inference. In contrast, the region-state prior degrades the primary identity metric and is therefore
excluded from the final control state.
Control-state updates.Both the random and typed updates improve over the frozen incumbent
Ω0, indicating that updating the control state can be beneficial. The typed update, however, does not
outperform an equal-budget random update and degrades 15% of scenes, so the current experiment
does not establish an advantage for typed transfer itself. Removing the Base fallback produces a clear
degradation, supporting fallback as a conservative mechanism when an update is unreliable. The full
10

+14.24 Physics-IQ improvement is an integrated system result and should not be interpreted as the
sum of these local ablations.
Tool use.Retrieval supplies frozen textual evidence rather than reference pixels or visual embed-
dings, while SAM contributes first-frame geometric information without semantic labels. None of
the three tool-use contrasts is statistically resolved. Because the evaluation contains multiple views
nested within each scene, we use the scene-paired analysis as the primary estimand. These results
indicate that the overall Physics-IQ gain cannot be attributed to tool use alone.
5 LIMITATIONS
Our experiments expose three main limitations of the current approach.
First, strong candidate proposals do not necessarily imply reliable deployment decisions. Several
individual controls improve under matched evaluation, and the complete SCOPEpolicy substantially
improves over Frozen Base on Physics-IQ. However, prospective experiments show that selecting
when to apply these controls remains substantially harder than generating useful candidates. In
particular, selection errors and insufficient proposal coverage limit performance on unseen tasks.
Second, the effectiveness of inference-time controls is not fully invariant across backbones or metrics.
Updates that improve one configuration can have smaller effects, or even reverse direction, under
another backbone. This limits the extent to which a control learned in one setting can currently be
treated as a transferable adaptation rule.
Third, SCOPErelies on development-time evidence to decide which updates may enter the deployed
control state. Although held-out scores cannot directly modify the policy, the quality of the resulting
policy still depends on the diversity and representativeness of the development tasks. More reliable
adaptation will therefore require stronger task-disjoint proposal generation, calibrated uncertainty
estimates, and selectors that generalize under distribution shift.
The Frozen Base fallback partially mitigates these limitations by allowing the system to abstain from
uncertain updates rather than forcing every proposal to be deployed. Nevertheless, improving the
reliability of this decision remains a central direction for future work.
6 CONCLUSION
We introduce SCOPE, a framework for inference-time adaptation of frozen video world models
that explicitly separates proposal, update, deployment, and evaluation. SCOPErepresents prompts,
sampler configurations, verifiers, and reward selectors within a structured control state, updates
this state using development evidence, and freezes the resulting deployment policy before held-out
evaluation.
On the Physics-IQ benchmark, SCOPEsubstantially improves over the exact Frozen Base on both
evaluated backbones. Controlled ablations further identify useful contributions from scene speci-
fication, sampling, and learned selection, while the advantage over the strongest matched agentic
alternative remains unresolved. Cross-backbone and prospective evaluations show that these gains
are not uniformly transferable, highlighting reliable selection under distribution shift as the main
remaining challenge.
More broadly, our results suggest that improving an agentic inference system requires more than
generating better candidate interventions. It also requires a principled mechanism for deciding which
interventions should become part of the deployed policy. By making this distinction explicit, SCOPE
provides a foundation for studying inference-time adaptation as a controlled optimization problem
rather than an unstructured sequence of post-hoc improvements.
11

REFERENCES
Tong Bai, Zhenglin Wan, Pengfei Zhou, Xingrui Yu, Yang You, and Ivor W. Tsang. SkillDAG:
Self-evolving typed skill graphs for LLM skill selection at scale.arXiv preprint arXiv:2606.03056,
2026.
Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V . Le, Christopher R ´e, and
Azalia Mirhoseini. Large language monkeys: Scaling inference compute with repeated sampling.
arXiv preprint arXiv:2407.21787, 2024.
Davide Bucciarelli, Evelyn Turri, Lorenzo Baraldi, Marcella Cornia, and Rita Cucchiara. Tiny
inference-time scaling with latent verifiers.arXiv preprint arXiv:2603.22492, 2026.
Kunfeng Chen, Qihuang Zhong, Juhua Liu, and Bo Du. SkillCAT: Contrastive assessment and
topology-aware skill self-evolution for LLM agents.arXiv preprint arXiv:2606.13317, 2026a.
Sixiang Chen, Zhaohu Xing, Tian Ye, Xinyu Geng, Yunlong Lin, Jianyu Lai, Xuanhua He, Fuxiang
Zhai, Jialin Gao, and Lei Zhu. GenEvolve: Self-evolving image generation agents via tool-
orchestrated visual experience distillation.arXiv preprint arXiv:2605.21605, 2026b.
Kexu Cheng, Zicheng Liu, Mingju Gao, Chunhe Song, and Hao Tang. PhysRAG: Enhancing physics-
awareness in video generation via retrieval-augmented generation. InEuropean Conference on
Computer Vision, 2026.
Cynthia Dwork, Vitaly Feldman, Moritz Hardt, Toniann Pitassi, Omer Reingold, and Aaron Roth.
The reusable holdout: Preserving validity in adaptive data analysis.Science, 349(6248):636–638,
2015.
Yuxiang Feng, Juncheng Wang, Chao Xu, Yijie Qian, Huihan Wang, Wenlong Hou, Yang Liu, Baigui
Sun, Yong Liu, and Shujun Wang. NEWTON: Agentic planning for physically grounded video
generation.arXiv preprint arXiv:2605.18396, 2026.
Zelin Gao, Qiuyu Wang, Jiapeng Zhu, Jingye Chen, Zichen Liu, Qingyan Bai, Jiahao Wang, Yufeng
Yuan, Hanlin Wang, Yichong Lu, Ka Leong Cheng, Haojie Zhang, Jian Gao, Tianrui Feng, Yuzheng
Liu, Yao Yao, Yinghao Xu, Xing Zhu, Yujun Shen, and Hao Ouyang. Infinite worlds with versatile
interactions.arXiv preprint arXiv:2607.07534, 2026.
Bo Jiang, Depu Meng, Yihan Hu, Yichen Xie, Tianshuo Xu, and Wei Zhan. LaMo: Self-supervised
latent motion priors for physical realism in video generation.arXiv preprint arXiv:2605.23878,
2026.
Taegu Kang, Jaesik Yoon, and Sungjin Ahn. Inference-time scaling in diffusion models through
iterative partial refinement.arXiv preprint arXiv:2605.19317, 2026.
Zizun Li, Haoyu Guo, Runzhe Teng, Chunhua Shen, and Tong He. Geo-Align: Video generation
alignment via metric geometry reward.arXiv preprint arXiv:2605.23903, 2026a.
Zongxia Li, Dawei Liu, Fuxiao Liu, Yuhang Zhou, Xiyang Wu, Jingxi Chen, Jing Xie, Xiaomin Wu,
and Lichao Sun. COMFYCLAW: Self-evolving skill harnesses for image generation workflows.
arXiv preprint arXiv:2607.01709, 2026b.
Juyi Lin, Arash Akbari, Yumei He, Lin Zhao, Haichao Zhang, Arman Akbari, Xingchen Xu, Zoe Y .
Lu, Enfu Nan, Hokin Deng, Edmund Yeh, Sarah Ostadabbas, Yun Fu, Jennifer Dy, Pu Zhao, and
Yanzhi Wang. PhyGround: Benchmarking physical reasoning in generative world models.arXiv
preprint arXiv:2605.10806, 2026a.
Minhua Lin, Juncheng Wu, Zijun Wang, Zhan Shi, Yisi Sang, Bing He, Zewen Liu, Tianxin Wei,
Zongyu Wu, Zhiwei Zhang, Dakuo Wang, Xiang Zhang, Benoit Dumoulin, Cihang Xie, Yuyin
Zhou, Suhang Wang, and Hanqing Lu. Harness updating is not harness benefit: Disentangling
evolution capabilities in self-evolving LLM agents.arXiv preprint arXiv:2605.30621, 2026b.
Nanye Ma, Shangyuan Tong, Haolin Jia, Hexiang Hu, Yu-Chuan Su, Mingda Zhang, Xuan Yang,
Yandong Li, Tommi Jaakkola, Xuhui Jia, and Saining Xie. Inference-time scaling for diffusion
models beyond scaling denoising steps.arXiv preprint arXiv:2501.09732, 2025.
12

Team Wan, Ang Wang, Baole Ai, Bin Wen, Chaojie Mao, Chen-Wei Xie, Di Chen, Feiwu Yu,
Haiming Zhao, Jianxiao Yang, Jianyuan Zeng, Jiayu Wang, Jingfeng Zhang, Jingren Zhou, Jinkai
Wang, Jixuan Chen, Kai Zhu, Kang Zhao, Keyu Yan, Lianghua Huang, Mengyang Feng, Ningyi
Zhang, Pandeng Li, Pingyu Wu, Ruihang Chu, Ruili Feng, Shiwei Zhang, Siyang Sun, Tao Fang,
Tianxing Wang, Tianyi Gui, Tingyu Weng, Tong Shen, Wei Lin, Wei Wang, Wei Wang, Wenmeng
Zhou, Wente Wang, Wenting Shen, Wenyuan Yu, Xianzhong Shi, Xiaoming Huang, Xin Xu, Yan
Kou, Yangyu Lv, Yifei Li, Yijing Liu, Yiming Wang, Yingya Zhang, Yitong Huang, Yong Li, You
Wu, Yu Liu, Yulin Pan, Yun Zheng, Yuntao Hong, Yupeng Shi, Yutong Feng, Zeyinzi Jiang, Zhen
Han, Zhi-Fan Wu, and Ziyu Liu. Wan: Open and advanced large-scale video generative models.
arXiv preprint arXiv:2503.20314, 2025.
Philip S. Thomas, Georgios Theocharous, and Mohammad Ghavamzadeh. High-confidence off-policy
evaluation. InProceedings of the AAAI Conference on Artificial Intelligence, pp. 3000–3006, 2015.
doi: 10.1609/aaai.v29i1.9541.
Ruoyu Wang, Jialun Liu, Huayang Huang, Haibin Huang, Jiepeng Wang, Chi Zhang, Xuelong Li,
and Yu Wu. SIFT: Self-imagination fine-tuning for physically plausible motion in video diffusion
models. InEuropean Conference on Computer Vision, 2026.
Keming Wu, Yijing Cui, Wenhan Xue, Qijie Wang, Xuan Luo, Zhiyuan Feng, Zuhao Yang, Sudong
Wang, Sicong Jiang, Haowei Zhu, Zihan Wang, Ping Nie, Wenhu Chen, and Bin Wang. WorldRea-
sonBench: Human-aligned stress testing of video generators as future world-state predictors.arXiv
preprint arXiv:2605.10434, 2026.
Yifan Yang, Ziyang Gong, Weiquan Huang, Qihao Yang, Ziwei Zhou, Zisu Huang, Yan Li, Xuemei
Gao, Qi Dai, Bei Liu, Kai Qiu, Yuqing Yang, Dongdong Chen, Xue Yang, and Chong Luo.
SkillOpt: Executive strategy for self-evolving agent skills.arXiv preprint arXiv:2605.23904, 2026.
Zhuoyi Yang, Jiayan Teng, Wendi Zheng, Ming Ding, Shiyu Huang, Jiazheng Xu, Yuanming Yang,
Wenyi Hong, Xiaohan Zhang, Guanyu Feng, Da Yin, Yuxuan Zhang, Weihan Wang, Yean Cheng,
Bin Xu, Xiaotao Gu, Yuxiao Dong, and Jie Tang. CogVideoX: Text-to-video diffusion models
with an expert transformer. InInternational Conference on Learning Representations, 2025. URL
https://arxiv.org/abs/2408.06072.
Tengjiao Yin, Jinglei Shi, Heng Guo, and Xi Wang. VIGOR: Video geometry-oriented reward for
temporal generative alignment.arXiv preprint arXiv:2603.16271, 2026.
Jianhao Yuan, Xiaofeng Zhang, Felix Friedrich, Nicolas Beltran-Velez, Melissa Hall, Reyhane
Askari-Hemmat, Xiaochuang Han, Nicolas Ballas, Michal Drozdzal, and Adriana Romero-Soriano.
Inference-time physics alignment of video generative models with latent world models.arXiv
preprint arXiv:2601.10553, 2026.
Peiwen Zhang, Yufan Deng, Shangkun Sun, Juncheng Ma, Duomin Wang, Jonas Du, Zilin Pan,
Ye Huang, Hao Liang, Songyan Huang, Ruihua Zhang, Enze Xie, Ming-Yu Liu, and Daquan
Zhou. PhysisForcing: Physics reinforced world simulator for robotic manipulation.arXiv preprint
arXiv:2606.28128, 2026a.
Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, and Peiyang He. Library
drift: Diagnosing and fixing a silent failure mode in self-evolving LLM skill libraries.arXiv
preprint arXiv:2605.19576, 2026b.
Zekai Zhang, Jiahao Li, Jie Zhang, Kaiyuan Gao, Kun Yan, Lihan Jiang, Ningyuan Tang, Shengming
Yin, Tianhe Wu, Xiaoyue Chen, Xiao Xu, Yan Shu, Yanran Zhang, Yixian Xu, Yuxiang Chen,
Zhendong Wang, Zihao Liu, Zikai Zhou, Huishuai Zhang, Dongyan Zhao, and Chenfei Wu.
Qwen-Image-Agent: Bridging the context gap in real-world image generation.arXiv preprint
arXiv:2606.26907, 2026c.
13

A EXTENDEDGENERALIZATION ANDPROSPECTIVEEVALUATIONS
A.1 PROSPECTIVEPAI EVALUATION
By contrast, the conformal-risk-control stop test asks whether SceneLang should be replaced on new
tasks under a fully frozen gate. It fixes 96 development tasks and a disjoint 48-task confirmation set
before scoring. The procedure uses strict task-LOO proposals, eight-fold inner calibration, exact
SceneLang fallback, and three fixed CRC thresholds. The merged development panel contains 288
official score units. At every threshold, the protocol commits the same two tasks (2/96), and both are
harmful. The mean gain over the exact SceneLang anchor is −0.173; the threshold-0 simultaneous
interval is [−0.835,0.000] , and the conditional harm upper bound is 1.0. All five CRC feasibility
checks and all three downstream development requirements fail. The procedure therefore retains
SceneLang. No videos, VQA outputs, or scores are released for the 48-task confirmation set.
A.2 COMPLETIONGUARDSUCCESSOREVALUATION
A related successor test considers whether a task-disjoint replacement for CompletionGuard and
ContinuityGuard should replace the incumbent over exact SceneLang. It freezes both guards before
generating three arms on 96 fresh development tasks, while a separate 28-task confirmation set
remains sealed. The 58-dimensional strict task-LOO router makes only two non-fallback proposals
(2/96), one per candidate arm. Both are non-harmful but improve only QS, with zero RO gain.
At every frozen threshold, the minimum 24 commits fails, the conditional harm upper bound is
0.935>0.25 , and the simultaneous gain lower bound is exactly zero; the matched-random lower
bound is also non-positive. Thus no CRC threshold is selected and the secondary RO/QS gates are
not entered. The procedure retains exact SceneLang. We did not generate videos or release VQA for
the 28-task confirmation set, and we did not read its scores; the split6 evolution figure is unchanged.
A.3 PHYT2V EVALUATION
As a complementary deployment check, we ask whether candidate expansion adds value beyond
retaining the incumbent on a 40-scene PhyT2V evaluation set. Base scores 23.57, original-random
29.45, fixed-round2 31.71, the GPT-5.4 incumbent 33.08, and selected P-IQ 33.08. Although five
scenes were eligible for round3, no round3 proposal was promoted. Selected-minus-incumbent is
therefore exactly 0.00 (CI [0,0] ), whereas selected-minus-fixed-round2 is +1.37 (CI [−4.04,+7.05] ).
The larger +9.51 contrast with Base is attributable to the retained GPT-5.4 proposal, not to SCOPE
candidate expansion. Moreover, only 15/40 scene IDs are new relative to the preceding evaluation
set. We therefore interpret this result as guarded incumbent retention, not as a positive method effect.
A.4 PROSPECTIVEINTEGRATED-SYSTEMEVALUATION
Turning from deployment diagnostics to fresh-task tests, we ask whether the full harness improves on
32 fresh, task-disjoint Physics-IQ tasks and passes its deployment criteria. Full SCOPEis +0.096
over Base (CI [−0.887,+1.077] ) and −1.019 versus a simple frozen router (CI [−2.159,+0.146] ).
Retirement is significantly harmful relative to commit-plus-fallback: −0.773 (CI [−1.471,−0.203] ).
A separate 40-scene skill-optimization confirmation asks whether the typed update beats matched
random. It does not: the contrast is −0.32 (CI [−5.98,+5.15] ), and the 15% harm rate exceeds the
frozen10%ceiling. Both deployment criteria fail.
A.5 SELECTIVEGROUNDEDROUTER
Against that backdrop, the grounded-router experiment asks whether selective tool use can avoid the
harm of always-on assistance while still outperforming no-tool and random routing. The prospective
CausalVerse test uses task-disjoint fit, conformal, applicability, target, and confirmation roles. Every
target or confirmation task has the same two candidate videos (no-tool and profiled-card), three
frozen seeds, and official CRONOS DisMo scoring; the four policies only choose among those shared
videos. The fit-only group policy applies 48 cards, versus 180 for always-on and exactly 48 for a
profile/source-stratified random route.
14

Table 6:Selective grounded-router final result.Absolute DisMo cosine similarities reuse the
same two candidate arms and three seeds for all four policies. Cards count profiled prompt-card
applications across192target and96confirmation tasks; they are not additional generated videos.
Policy Cards Target Confirmation Pooled
Exact no-tool0 0.4071 0.4425 0.4189
Always-on profiled card180 0.4021 0.4352 0.4132
Fit-only group policy48 0.4096 0.4401 0.4197
Same-budget stratified random48 0.4084 0.4424 0.4197
The result is mixed. The selective router avoids the harm of always-on use but does not establish
an absolute generation gain or routing skill beyond random. In DisMo points, the preregistered
pooled contrasts are +0.083 for fit-group minus no-tool (CI [−0.191,+0.381] ), +0.660 for fit-group
minus always-on (CI [+0.016,+1.315] ), and +0.002 for fit-group minus same-budget random (CI
[−0.281,+0.299] ). The target result is positive: +0.243 points overall and +1.460 over the 32
switched tasks. Independent confirmation, however, reverses sign to −0.237 overall and −1.420 over
16 switched tasks, with negative means for all three confirmation seeds. Motion/sharpness ratios are
1.001/1.008, and all1,728scores are present.
We therefore conclude that selective fallback significantly avoids the strong harm of always-on use,
especially for the geometry group, while leaving the no-tool and same-budget-random contrasts
unresolved. Because the evidence calls were acquired before policy selection and shared across all
four policies, the experiment cannot identify fewer tool calls as the cause of the quality change.
A.6 PHYGROUNDAPPLICABILITYANALYSIS
Finally, the PhyGround chain asks whether the preregistered selector can clear applicability before
any target score is read. It stops at the pre-score gate on a 32-task target set. The pipeline completes
all 288 frozen target videos and score-blind features, but the frozen proxy produces only 4/32 raw
non-incumbent proposals, below the required minimum of 8. It produced 0 proposals at confidence
≥ −0.25(minimum 8) and 0 at confidence ≥0 (minimum 4), while law coverage passed for eight
families. The protocol therefore stops before any target PhyGround score is read and leaves the
21-task confirmation set untouched. This is an applicability failure, not a negative target-score
estimate.
A score-free audit then explains why the gate fails. The main driver is the global task-max conformal
deduction (58.47, or 0.731 after gain normalization) combined with worst-head selection; motion and
sharpness bind on no selected task. The frozen held-out calibration split likewise produces only 3/64
raw switches. At that observed rate, an eight-of-32 gate has probability 8.9×10 −5. This post-failure
replay diagnoses the frozen design but cannot justify replacing the policy on the consumed pool.
B ADDITIONALDISCUSSION
The component experiments clarify which parts of the current inference-control space are useful. Text
conditioning and the sampler modification improve their matched comparisons, and the supervised
reward selector outperforms matched random under scene-grouped OOF evaluation. In contrast, the
region-state prior and the matched web/SAM tool variants do not show reliable gains. These results
are important because they prevent the integrated Physics-IQ improvement from being attributed
uniformly to every component.
The prospective experiments expose a different limitation: reliable deployment requires both sufficient
proposal coverage and a selector that transfers beyond its development distribution. The selective
router avoids the degradation of always-on tool use while remaining unresolved against no-tool and
same-budget random routing, and its confirmation result reverses direction. PhyGround fails even
earlier because the frozen selector proposes too few non-incumbent actions. These cases motivate
future work on task-disjoint calibration and selectors that can abstain when uncertainty is high, rather
than relaxing thresholds after observing target outcomes.
15

Table 7:Result-to-artifact index.Each row links a reported experimental result to its smallest
authoritative machine-readable source.
Result Evaluation role Authoritative artifact(s)
Matched 40-scene Physics-IQ proce-
dure vs exact Base
same-universe system resultphysiq_common_base_result.json ; matched publication
in the release manifest
Retrospective LingBot harness proxy same-protocol retrospective
addition
matched score evidence and result in the release manifest
SceneLang text edit component; three fixed seeds scenelang_skill_table.json
Fixed sampler edit component; four fixed seedssampler_axis_joint_fourseed_result.json
Supervised reward selector scene-grouped OOFreward_gain_ci.json
Integrated and new-task prospective
failures
prospective negative / stoppai_scope_lifecycle_staircase_result.json ;
scope_v6_fit_group_final_result.json; pai_
wide_crc_human096_development_completion_r7.
json; pai_wide_completion_guard_development_
completion.json
Table 8:Protocol and statistical status matrix.Views are nested within scenes for Physics-IQ;
secondary, same-split, and post-hoc rows never receive promotion credit.
Setting Independent unit Evaluation role Primary comparison
GPT-5.4 SceneLang scene; 3 fixed seeds aver-
aged
component evidence SceneLang vs Base; CI conditional on these
seeds
Learned reward 64 scenes; 179 nested
views
component evidence scene-grouped OOF reward vs matched random
Physics-IQ tool axis scene; 3 nested views preregistered negative ablation web-only and web+SAM vs no-tool; incremen-
tal SAM vs web-only
PAI split6 task same-split deployment diagnos-
tic
all matched controls shown; post-hoc SCOPE
separated
OpenS2V category-stratified item prospective deployment case SCOPEvs LingBot; unresolved
Fresh PhyT2V evaluation scene deployment diagnostic selected vs incumbent/fixed proposal; no expan-
sion credit
Fresh 32-task Physics-IQ
transfer
task prospective integrated test full harness vs Base/router; frozen guard gate
Typed-update confirmation scene prospective integrated test typed update vs matched random plus harm ceil-
ing
Grounded selective router task; role/profile/family
bootstrap
prospective tar-
get+confirmation; STOP
fit-group vs no-tool, always-on, and same-
budget random
C REPRODUCIBILITYDETAILS
All reported results are linked to the scripts and machine-readable outputs used to generate the
corresponding tables and figures. The release preserves the exact protocol-local inputs for each
experiment and does not aggregate statistics across incompatible evaluation units.
D EVALUATIONPROTOCOLS ANDSTATISTICALDETAILS
Table 8 summarizes the independent unit, evaluation role, and primary comparison used for each
experimental setting. It is provided to make the statistical units and protocol boundaries explicit.
E FULLPAI METRICBREAKDOWN
Table 9 exposes the quality components aggregated by QS in the main PAI panel. Frozen Base is
shown in absolute score units; every other row is a signed difference from that same Base. These
component-wise values are descriptive diagnostics, not separately tested deployment criteria.
F ADDITIONALQUALITATIVEANALYSIS
The following visualization illustrates a disclosed post-hoc paper-submersion intervention. It is
included only as qualitative analysis and is not a native generation result or benchmark comparison.
16

Table 9:Complete official-72B PAI quality profiles.SC/BC are subject/background consistency;
MS is motion smoothness; AQ/IQ are aesthetic/imaging quality; OC is overall text–video consistency;
IS/IB are I2V subject/background fidelity. Frozen Base is absolute and all other rows are ∆ vs Base.
All 12 main-panel rows are included.
Method SC BC MS AQ IQ OC IS IB
Frozen base (absolute) 89.51 91.71 98.49 44.21 62.83 19.50 92.44 95.75
Shared global (Base parent) -0.45 -0.18 -0.73 +0.61 +1.60 -0.12 -0.09 -0.02
Qwen-Image-Agent-style (SceneLang) (Zhang et al., 2026c) +0.89 +0.37 +0.13 +0.42 +0.50 -0.06 +0.66 +0.49
SceneLang + shared global -0.03 +0.19 -0.65 +0.79 +2.25 -0.04 +0.10 +0.03
LingBot-style + safe fallback† (Gao et al., 2026) +0.24 +0.10 +0.03 0.00 +0.28 -0.02 +0.13 +0.12
LingBot-style Director→Pilot + shared global† (Gao et al., 2026) -0.16 +0.02 -0.70 +0.70 +2.17 -0.22 +0.06 +0.07
LingBot-style Director→Pilot (raw) (Gao et al., 2026) +1.33 +0.49 +0.26 -0.24 +0.94 +0.12 +0.58 +0.64
LingBot-style + shared global +0.15 +0.22 -0.55 +0.60 +1.73 -0.26 -0.08 +0.15
GPT-5.4-SKILL (raw) -1.02 -1.61 +0.07 -1.41 -0.09 +0.09 +0.14 +0.72
GPT-5.4-SKILL + shared global -2.67 -2.27 -0.66 -1.64 -1.14 -0.24 -0.54 +0.07
SCOPEw/o shared global ‡ +0.81 +0.36 +0.13 +0.41 +0.57 -0.01 +0.61 +0.44
SCOPE+ shared global (ours) ‡ -0.06 +0.20 -0.68 +0.69 +2.33 -0.03 0.00 +0.02
Figure 4:Web-grounded complete paper submersion intervention.Both rows use the same straw-
free seed-20260785 Wan2.2 baseline. The unexplained overhead straw is inpainted once in their
shared conditioning frame.WITHOUT OURSshows the complete baseline frame, in which only
the lower paper edge contacts the water.OURSapplies a disclosed post-hoc full-frame intervention:
the complete paper mask is compressed onto the dish bottom; every final paper pixel lies within the
audited water ellipse; and water tint, caustics, refraction, and a ripple band are rendered after the
paper. Both published A/B MP4s and the displayed frames are complete 832×480 images, with dish
cropping disabled in the manifest. The post-absorption Wikimedia image is display-only and never
enters either video. Retrieved pixels likewise never enter the video. The native four-seed prompt
grid failed the qualitative gate and is not shown. This visualization is a qualitative post-hoc state
intervention, not native Wan dynamics, an unbiased generation result, or benchmark evidence.
17
