---
title: 'Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code
  Repair'
url: https://arxiv.org/abs/2607.24604
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Xueping Gao
- Jianwei Yang
- Qiang Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.24604
pages: 11
chars: 60686
fetched_at: '2026-11-08T13:33:28+00:00'
kb_version: 1
---

# Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair

Looping Is Not Reliability: State-Bound Evidence and Typed
Revision Contracts for Agentic Code Repair
Xueping Gao✉
xueping.gxp@alibaba-inc.com
Alibaba Cloud Computing
Hangzhou, China
Jianwei Yang
jianwei.yjw@alibaba-inc.com
Alibaba Cloud Computing
Hangzhou, China
Qiang Yang
yuanzhan.yq@taobao.com
Alibaba Cloud Computing
Hangzhou, China
Abstract
Generate–test–revise loops are common in coding agents, but rep-
etition alone provides no reliability guarantee. We study the gap
between finding a correct patch and retaining, verifying, and sub-
mitting it. A sealed five-seed study over 30 HumanEval repairs
produces 900 three-revision trajectories. Under forced revision,
current correctness with current traces falls from 0.820 after one
revision to 0.673 after two, although ever-correct rises to 0.847. Two
common-state studies use 2,430 branches from identical frozen pro-
grams to remove post-treatment risk-set bias. In a prespecified 14B
replication, stale traces harm 34/135 correct starts versus 4/135 with
current traces, a 22.2-point increase (task-cluster 95% CI[8.9, 37.0],
exact Holm𝑝= 0.0337). A prospective 540-rollout policy eliminates
observed correct-start harm but reduces wrong-start repair and
fails its joint criterion. Repository experiments over 24 bugs and
four coder stacks expose floor effects and component heterogeneity
without Holm-significant effects. We therefore separate admission,
preservation, grounded certification, competence, and liveness. We
derive an evidence-bound typed loop contract and instantiate its
mechanically enforceable subset in a reference implementation
that binds verifier evidence to exact code states, preserves verified
checkpoints, and emits auditable admission receipts. The imple-
mentation is an executable specification and conformance artifact,
not evidence of improved repair competence or calibrated verifier
dependence.
CCS Concepts
•Software and its engineering → Software testing and debug-
ging;•Computing methodologies→Artificial intelligence.
Keywords
coding agents, agent reliability, code repair, verification, stopping
policies, LLM evaluation
ACM Reference Format:
Xueping Gao, Jianwei Yang, and Qiang Yang. 2026. Looping Is Not Reliability:
State-Bound Evidence and Typed Revision Contracts for Agentic Code
Repair. InProceedings of the 1st International Workshop on Agentic AI for
Next-Generation Software Development (AgenticDev ’26), October 12–16, 2026,
Munich, Germany.ACM, New York, NY, USA, 11 pages. https://doi.org/10.
1145/3843282.3844438
This work is licensed under a Creative Commons Attribution 4.0 International License.
AgenticDev ’26, Munich, Germany
©2026 Copyright held by the owner/author(s).
ACM ISBN 979-8-4007-2985-0/2026/10
https://doi.org/10.1145/3843282.3844438
CODE TRAJECTORY
EVIDENCE
A  WRONG
shift = 12
B  VERIFIED
shift = 4
C  REGRESSED
shift = 12
repair + verify
NO STATE CHECK
 revise
TRACE FROM STATE A
failure: shift = 12
observe
stale trace reused
trace A ≠ code B
STATE-BOUND CHECK
reject mismatch; preserve B
Figure 1: Mechanism of stale-evidence resurrection. Repair
changes code state A (shift 12) to verified state B (shift 4),
but an old trace bound to A is reused for the next revision
and restores shift 12. State binding rejects the A/B mismatch
before revision. Section 5.3 reports HumanEval/89.
1 Introduction
Coding agents increasingly operate as loops: propose code, execute
tests, consume feedback, revise, and stop. Iterative refinement can
improve the probability that a correct solution is produced [5, 15,
22]. This search-centric view, however, obscures a deployment
question: after a correct patch appears, what prevents the next
revision from destroying it, a stale observation from reviving an
old bug, or a correlated verifier from confirming the same error?
We call this distinctionproposal search versus completion relia-
bility. Search asks whether any revision in a trajectory is correct.
Completion reliability asks whether the orchestrator retains a cor-
rect state, bases revisions on evidence about that state, and stops
only when its accepted evidence has sufficiently low risk. The dis-
tinction matters because an increasingever-correctrate can coexist
with a decreasing current or final correctness rate.
Prior work establishes important pieces of this problem. Intrinsic
self-correction may fail or regress without reliable external feed-
back [9, 11]; error localization and revision ability are distinct [25];
and weak verifiers limit self-correction [ 28]. FeedbackEval mea-
sures how feedback types affect code repair [5]. Work on evaluator
self-preference and correlated model errors cautions that a second
model is not automatically an independent judge [ 12, 18]. These
findings do not yet provide a joint account of state transitions, evi-
dence provenance, verifier selective risk, verifier dependence, and
stopping in one code-agent protocol.
This paper asks five research questions:
RQ1Is correctness an absorbing state under repeated revision?
arXiv:2607.24604v3  [cs.CL]  4 Oct 2026

AgenticDev ’26, October 12–16, 2026, Munich, Germany Gao, Yang, Yang
RQ2From the same wrong or correct program, how do evidence
content and state alignment change repair and continuation
harm?
RQ3 Can verifier quality or independence be inferred from model-
family diversity?
RQ4 Which orchestration guards directly block the observed fail-
ure classes, and what do they cost?
RQ5 How do contracts and revision allowance affect repository
completion?
Our contributions are:
(1) A trajectory-level reliability decompositionthat jointly
reports correctness discovery and retention, wrong-to-correct
and correct-to-wrong transitions, verifier risk–coverage, condi-
tional false-accept dependence, and sound completion.
(2) Controlled evidence studies.Forced revision shows correct-
ness loss; paired common-state interventions at two coder ca-
pacities estimate state-alignment contrasts from identical se-
lected states.
(3) An executable contract and reference implementation.
We derive testable obligations for state-bound evidence, typed
actions, checkpoint preservation, fresh completion certification,
and risk-aware stopping. A reference implementation instanti-
ates the mechanically enforceable subset as an admission layer
around existing coding agents and verifiers.
(4) Repository-agent factorials.Over 24 bugs, four coder stacks
test a contract; two Devstral factorials separate components and
depth. All use sealed adjudication and task-cluster inference.
2 Related Work
2.1 Self-Correction and Feedback-Driven Repair
Huang et al. find that intrinsic self-correction does not reliably
improve reasoning when no external signal is available [9]. Kamoi et
al. ’s survey similarly identifies reliable external feedback as a central
success condition [11]. Tyen et al. show that models often fail to
locate errors even when they can correct an error whose location
is supplied [25]; Zhang et al. separate refinement ability from the
strength of the verifier that decides when to refine [ 28]. In code,
FeedbackEval evaluates feedback types and reports diminishing
gains over repeated repair [5]. We do not claim the new observation
that feedback quality matters. We instead measure the bidirectional
transition process and intervene on whether evidence is attached
to the program state it describes.
Self-Refine and Reflexion exemplify inference-time refinement
with generated feedback or memory [15, 22]. Their motivating met-
ric is typically task success. Our focus is the reliability contract
required after a proposal exists: preservation, provenance, verifica-
tion, and stopping.
2.2 Agentic Software Engineering Systems
Repository-scale systems make orchestration concrete. SWE-agent
shows that the agent–computer interface changes coding perfor-
mance [27]; Agentless reports that a simpler localization–repair–
validation pipeline can outperform more elaborate open-source
agents on SWE-bench Lite [ 26]; and SWE-bench exposes long-
context, multi-file demands [ 10]. Beyond their end-task metrics,
we test whether loops preserve valid states, consume state-aligned
evidence, and gate completion: first under controlled function-level
states, then as a bundle in repository Git/search/edit/test loops.
Recent process studies characterize feedback integration [1]; the
“lucky pass” AgentLens identifies regression cycles [ 21], while a
production-assessed AgentLens studies verification and recovery
over whole trajectories [19]. Others control hint depth while mea-
suring preservation [13], or expose action bias and visible–held-out
gaps [7, 29]. Evidence guards, abstention, and transactional admis-
sion are established ideas [2, 3, 16]. Our narrower contribution is
a fixed-code-state intervention on evidence provenance, linked to
verifier risk and dependence and followed by a prospective policy
test.
Adjacent infrastructure enforces related but different bound-
aries. In-toto records and verifies software-supply-chain steps [24],
SLSA provenance describes where, when, and how an artifact was
produced [23], and OPA separates general policy decisions from
their enforcement [17]. Our reference implementation adopts prove-
nance and admission ideas but applies them inside an agent-repair
transaction: verifier evidence is bound to the candidate code state
on which it was produced, and admission preserves or recertifies
that state. It neither provides supply-chain attestation nor repairs
an inadequate oracle.
2.3 Code Correctness and Executable Evidence
HumanEval introduced execution-based functional correctness for
generated programs [ 4]. EvalPlus expands its tests and demon-
strates that a small visible suite can overestimate correctness [14].
We use disjoint visible, challenge, and hidden input sets derived
from HumanEval+, while explicitly treating challenge and hidden
tests as construction-dependent rather than independent oracles.
2.4 Verifier Risk and Dependence
LLM evaluators may recognize and favor their own generations [18].
More broadly, errors remain correlated across model architectures
and providers [12]. We therefore distinguish two quantities: selec-
tive risk at a specified coverage and conditional error dependence
among incorrect candidates. Risk–coverage follows selective pre-
diction, where abstention is part of evaluation rather than silently
discarded [6]. Our contribution is to connect these quantities to
agent completion decisions and to show that dependence changes
with the acceptance operating point.
3 Reliability Decomposition
Consider the observed transition sketched in Figure 1. After the shift
is repaired, the current program is correct, so𝑌𝑡 = 1. A failure trace
produced from the earlier wrong program is then supplied as if it
described the current state; the next revision restores the old defect,
yielding𝑌𝑡+1 = 0. This is a correct-to-wrong transition. Conversely,
changing a wrong program into a correct one is a wrong-to-correct
transition. The following decomposition measures both rather than
treating correctness as an absorbing endpoint.
Let𝑌𝑡 ∈{ 0, 1} denote the executable correctness of the code
after revision𝑡, and let𝑒𝑡 denote the evidence supplied for the next

Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair AgenticDev ’26, October 12–16, 2026, Munich, Germany
revision. For a fixed evidence condition𝑒, define
𝛼𝑒 =𝑃(𝑌 𝑡+1 =1|𝑌 𝑡 =0,𝑒),(1)
𝛽𝑒 =𝑃(𝑌 𝑡+1 =0|𝑌 𝑡 =1,𝑒).(2)
If𝑞𝑡 =𝑃(𝑌 𝑡 =1), then
𝑞𝑡+1−𝑞𝑡 =(1−𝑞 𝑡)𝛼𝑒−𝑞𝑡𝛽𝑒.(3)
Repair ability alone is therefore insufficient: when the current state
is likely correct, a nonzero regression rate can make another re-
vision harmful in expectation. If 𝛼𝑒+𝛽 𝑒 > 0, continuation has
negative expected correctness change when𝑞𝑡 >𝛼 𝑒/(𝛼𝑒+𝛽𝑒).
This transition view makes the paper’s three factors precise
without pretending that all are separately identifiable. Let 𝑒0 be
a matched nonactionable control. We operationalize theeffective
evidence responseon wrong and correct states as
𝑅𝑊(𝑒)=𝛼 𝑒−𝛼𝑒0, 𝑅 𝐶(𝑒)=𝛽 𝑒0−𝛽𝑒.(4)
These contrasts combine two latent quantities: how much task-
relevant information the evidence carries and how responsively the
coder maps that information into an edit. A single-coder evidence
intervention identifies their joint effective action, not “informative-
ness” and “responsiveness” separately. Zero response can mean un-
informative evidence or an unresponsive reviser; negative response
can mean misleading or state-misaligned evidence, overreaction, or
both. This identification limit is important: the three-factor thesis
is an interface decomposition, not a fitted multiplicative law.
Evidence also has provenance. Write𝑒=(ℎ 𝑠,ℎ𝑞,𝑥) for source-
state hash, test-suite hash, and payload. The evidence is state-
aligned only ifℎ𝑠 =ℎ(𝑆 𝑡). Payload𝑥 may contain true input/output
facts while the envelope is invalid for the current state. The
common-state study varies this alignment while holding the start-
ing code fixed.
For verifier 𝑣 with threshold chosen to attain coverage 𝑐, we
report
Cov𝑣(𝑐)=𝑃(𝐴 𝑣 =1),(5)
Risk𝑣(𝑐)=𝑃(𝑌=0|𝐴 𝑣 =1),(6)
where𝐴𝑣 denotes acceptance. To avoid conflating shared prevalence
with shared errors, dependence is computed only among incorrect
candidates. For verifiers𝑖,𝑗 we report excess joint false acceptance,
𝐷𝑖𝑗(𝑐)=𝑃(𝐴 𝑖𝐴𝑗|𝑌=0)−𝑃(𝐴 𝑖|𝑌=0)𝑃(𝐴 𝑗|𝑌=0),(7)
and the corresponding𝜙 coefficient. Both are operating-point con-
ditional: changing coverage changes which errors are accepted.
For an ensemble that accepts only when both verifiers accept,
let𝑓 𝑖 =𝑃(𝐴 𝑖 =1|𝑌=0). Its conditional false-accept rate is
𝑃(𝐴𝑖𝐴𝑗 =1|𝑌=0)=𝑓 𝑖𝑓𝑗+𝐷𝑖𝑗.(8)
Thus the familiar product-of-errors argument is valid only when
𝐷𝑖𝑗 = 0. Positive dependence is an additive reliability penalty even
if both marginal verifiers are individually strong; low dependence
is not useful when either marginal risk is poor.
Finally,sound completionis 𝑃(𝐴= 1,𝑌= 1) over all trajectories.
Unlike risk alone, it exposes a policy that obtains zero observed er-
ror by rejecting nearly everything. We report coverage, risk, sound
completion, and mean selected revision together rather than choos-
ing a universal scalar utility.
4 Study Design
4.1 Tasks and Executable Adjudication
We select 30 Python function-repair tasks from the HumanEval por-
tion of FeedbackEval [5]. Initial wrong candidates are stratified by
source (existing benchmark candidate, LLM-generated candidate,
and rule-based mutation) and frozen by hash before the confir-
matory runs. We do not redistribute the source benchmark data;
the artifact records task identifiers, candidate indices, sources, and
hashes.
Correctness requires passing visible, challenge, and hidden tests.
Challenge and hidden inputs are disjoint partitions of HumanEval+
[14]; they share the same benchmark construction process. Genera-
tion sees only visible evidence. Challenge and hidden suites remain
sealed until all trajectory and branch matrices pass structural vali-
dation. Evaluation is cached by(suite,task,code SHA-256).
4.2 Trajectory Study
The coder is Qwen2.5-7B-Instruct [20], sampled with temperature
0.3 and top-𝑝 0.9. Each trajectory performs three forced revisions.
We cross 30 tasks, six evidence conditions, and five seeds, yielding
900 trajectories and 2,700 revisions. The evidence conditions are
current binary outcome, current execution trace, stale binary out-
come, stale trace, unavailable evidence, and a flipped-binary stress
condition. Forced revision intentionally estimates what happens
when an orchestrator continues; it is not presented as the behavior
of every adaptive agent.
Every revision is judged by native self-declaration, fresh-context
Qwen2.5-7B, same-family Qwen2.5-14B, cross-family DeepSeek-
Coder-6.7B [8], and an executable challenge verifier. This produces
13,500 verdicts. Replaying four stopping rules for each verifier pro-
duces 18,000 paired outcomes: verifier-only, visible gate, challenge
gate, and a strict gate requiring challenge acceptance plus evidence
sourced from the immediately preceding state.
The three model verifiers use an order-swapped, single-token
A/B forced choice; the acceptance score is the mean ACCEPT prob-
ability under both label orders. Native thresholds are fixed at 0.5.
Retrospective coverage matching ranks scores on the frozen revi-
sion distribution and accepts the top fraction; it compares verifiers
but does not estimate deployment calibration. A stopping replay se-
lects the first revision satisfying its gate; if none does, it rejects after
revision 3. Because generation is frozen before replay, every policy
sees the same candidates and executable outcomes. “Mean rounds”
includes rejected trajectories, which consume the full three-revision
budget.
4.3 Common-State Intervention
Transition rates in a free-running trajectory have a post-treatment
risk-set problem: evidence affects whether a revision reaches a cor-
rect state, so comparing later regressions conditions on an evidence-
dependent event. We address this with common-state intervention.
For each task we freeze one wrong and one correct code state, se-
lected before assigning the new evidence branches. Twenty-seven
of 30 tasks contain both states and enter this study; the estimand
therefore concerns tasks with an observed repairable state.

AgenticDev ’26, October 12–16, 2026, Munich, Germany Gao, Yang, Yang
Table 1: Evidence interventions. Current evidence is generated from the code being revised; stale evidence is generated from a
different revision or the frozen wrong state.
Condition Payload Source state Role
Current binary Visible PASS/FAIL Current code Minimal aligned signal
Current trace Outcome, pass count, up to 3 failures Current code Actionable aligned signal
Stale binary/trace Same formats Previous revision Free-running freshness stress
UnavailableUNAVAILABLENone No-evidence baseline
Flipped binary Negated visible PASS/FAIL Current code Misleading-signal stress
Matched control Neutral text, character-length matched None Report-length/attention control
Stale wrong trace Failure trace Frozen wrong code State-misalignment intervention
Table 2: Confirmatory study inventory.
Component Trajectory study Common-state study
Tasks 30 27
Seeds 5 5
Coder capacities 1 2
Evidence conditions 6 4 wrong / 5 correct
Revisions per branch 3 1
Trajectories/branches 900 2,430
Candidate revisions 2,700 2,430
Verifier verdicts 13,500 —
Policy outcomes 18,000 —
From every frozen wrong state we branch current binary, cur-
rent trace, unavailable, and length-matched nonactionable evidence.
From every correct state we branch the same conditions plus a
stale trace generated from the paired wrong state. The prompt
permits returning unchanged code. Crossing 27 tasks, nine state–
evidence branches, and five common-random-number seeds gives
1,215 single-step branches for Qwen2.5-7B. Before inspecting repli-
cation outcomes, we freeze an exact Qwen2.5-14B repeat with the
same states, evidence, prompts, sampling parameters, seeds, and ad-
judication, adding 1,215 branches. The two capacities are analyzed
separately rather than pooled.
The frozen wrong state is the original visible-failing candidate.
The frozen correct state is selected mechanically as the lexico-
graphically first v0.4.3 revision passing all three suites; no failure
case is hand-picked. The matched control contains no task, test,
PASS/FAIL, or numerical semantics and exactly matches the tar-
get report in Unicode character count. It does not exactly match
tokenizer length, so prompt-token distributions remain an audited
nuisance variable. Within each task–state–seed block, evidence
branches share the sampling seed; invalid or unchanged outputs
remain in the intention-to-treat denominator.
4.4 Inference and Audit
The task, not the revision, is the independent sampling unit. Con-
firmatory common-state contrasts average seeds within each task
and then weight tasks equally. Within each coder, we use 10,000
task-cluster bootstrap draws, 100,000 paired sign flips, and one
Holm correction over six preregistered contrasts. Because five-seed
task effects lie on a discrete grid, an exact dynamic-programming
sign-flip sensitivity removes Monte Carlo error. A secondary paired
analysis subtracts 7B task-level effects from 14B effects and applies
a separate six-test Holm family; it was specified before inspecting
14B outcomes but is not a randomized model-family comparison.
Trajectory confidence intervals also resample complete task clus-
ters, preserving all seeds, conditions, revisions, and policies. Invalid
generations remain in the intention-to-treat denominator. All pro-
tocol, data-partition, trajectory, verdict, and analysis artifacts carry
SHA-256 lineage hashes.
Generation processes can read only the visible bundle. Challenge
and hidden bundles are opened only after trajectory IDs, condition
matrices, hashes, parser outputs, and lineage fingerprints validate
exactly. Hidden adjudication then recomputes the complete verifier
and policy matrices. This ordering prevents a partial run or adaptive
policy choice from leaking hidden outcomes back into generation.
4.5 Prospective Paired Online
Commit-Admission Comparison
Replay can show whether a guard would intercept recorded outputs,
but not how enforcing it changes subsequent model behavior. We
therefore run a sealed paired online comparison on the 27 common-
state tasks: two start states, five seeds, and baseline/guarded arms
yield 540 rollouts. Both arms use Qwen2.5-7B, the same typed action
prompt, visible diagnostics, challenge executions, seed schedule,
and three-step budget. Baseline commits every parseable patch
and ignores challenge verdicts for admission. Guarded execution
binds evidence to the current state, admits a patch only after the
challenge gate, and retains a last-known-good checkpoint after
invalid or rejected proposals. Hidden outcomes are opened only
after the complete paired matrix validates. The preregistered end-
points are unsafe-completion superiority and sound-completion
non-inferiority at a−5-point margin; inference uses paired task-
cluster bootstrap intervals.
4.6 Repository-Agent Factorial
To test the contract beyond single-function repair, we freeze 24 his-
torical bugs from nine Python projects, with at most three tasks per
project. Eligibility requires direct-parent bug/fix endpoints, stable
three-repeat signatures across the frozen suites, no ignored oracle,
and a gold production patch of at most five files and 200 changed
lines. The primary-only manifest excludes pilot tasks, is frozen
before model output, and permits no outcome-driven replacement.
Each task has a sanitized agent mirror containing only the buggy
tree and a separate evaluator mirror containing sealed tests but

Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair AgenticDev ’26, October 12–16, 2026, Munich, Germany
no gold source object. A hash-locked local Qwen2.5-14B snapshot
operates through typed search, view, edit, shell, test, submit, and
escalate actions in a real Git worktree, sampled at temperature 0.3,
top-𝑝 0.9, and at most 1,024 new tokens per action. We cross current
versus one-step-stale diagnostic evidence with contract OFF versus
ON and repeat every cell over three preregistered seeds, yielding
24×2×2×3 = 288intention-to-treat rollouts. Each rollout is limited
to 15 actions, three source revisions, six visible tests, and a shared
wall-clock budget.
Contract ON bundles evidence–state binding, a private com-
mit gate, rejection with rollback, last-known-good checkpoints,
and completion certification. Contract OFF executes and records
the same private gate but does not use its verdict to block a re-
vision. Diagnostic, gate, fail-to-pass, pass-to-pass, and full-suite
assets are content-hashed; generation can access only the diagnos-
tic interface. Every proposed patch, including rejected proposals, is
preserved and later replayed in an evaluator-owned worktree. Be-
fore unsealing, a 24-task by four-suite baseline audit found residue
only from terminal full-suite runs; the frozen evaluator orders fail-
to-pass, pass-to-pass, then full, and hard-resets and cleans before
each candidate. Final resolution requires all three suites to pass.
Anorchestrator-accepted completionis either an explicit agent sub-
mission or, in the ON arm, a checkpoint accepted by the frozen
completion rule. Unsafe and sound completion are accepted-and-
incorrect and accepted-and-correct, respectively.
The task is the inferential unit: seeds are averaged within task
and all 24 tasks receive equal weight. The co-primary intersection–
union decision requires the one-sided 95% upper bound on the
Contract ON-minus-OFF unsafe-completion effect to be below zero
and the lower bound on sound completion to exceed the prereg-
istered absolute−5-point margin. This margin was frozen before
outcomes; when baseline sound completion later falls below 5%, its
non-inferiority decision is necessarily weak evidence about live-
ness. We use 200,000 task-cluster bootstrap draws; task sign flips,
project-equal estimates, and leave-one-project-out checks are sen-
sitivities.
To probe stack generality under the 14B completion floor, we
froze three separate 288-rollout replications before their outcomes:
Qwen2.5-Coder-32B-Instruct-AWQ, Qwen3-Coder-Next-FP8, and
Devstral Small 2 24B. Each preserves the task matrix, co-primary es-
timands, budgets, completion rule, and task-equal inference, and is
analyzed separately. Model, tokenizer, adapter, and runtime changes
remain bundled ecological contrasts, not identified capacity or fam-
ily effects. Outcome-blind runtime or adapter faults were repaired
before restarting empty main roots; discarded attempts remain
receipted and no scientific design changed.
With Devstral fixed, a 576-rollout2 3 factorial randomizes state
binding, proposal admission/rollback, and completion certification.
Task-equal main effects enter one six-test Holm family over unsafe
and sound completion. A separate 576-rollout equal-budget factorial
crosses Contract OFF/ON with revision limits 1, 3, 5, and 8 while
holding action, test, token, and wall budgets fixed; its six-test family
covers depth, contract, and interaction effects. Full stack, runtime,
pilot, and sensitivity specifications are in the reproduction artifact.
All reported experiments use the frozen research harness de-
scribed above. The reference implementation was developed after-
ward as an executable realization of the mechanically enforceable
contract obligations and was not used to generate the reported
empirical results.
5 Results
5.1 RQ1: Correctness Is Non-Absorbing
Figure 2b separates current correctness from cumulative discovery.
With current traces, 82.0% of trajectories are correct after revision
1. Current correctness then falls to 67.3% at revision 2 and recovers
only to 69.3% at revision 3. In contrast, ever-correct increases from
82.0% to 84.7% and 85.3%. At revision 3, 16.0% of trajectories have
produced a correct patch and subsequently lost it. Current binary
evidence has lower loss (8.0%) but still does not make correctness
absorbing.
The shape is evidence-specific rather than a generic depth
penalty. Current-binary correctness is0 .700, 0.700, 0.720across
revisions; stale-trace correctness is0.687, 0.713, 0.660; and unavail-
able evidence is0 .687, 0.687, 0.707. Consequently, neither “more
rounds help” nor “more rounds hurt” is supported as a context-free
rule. Loop depth changes the number of transition opportunities;
the transition kernel determines their sign.
This result is deliberately scoped: it establishes non-absorption
under the tested forced-revision protocol. It does not show that an
adaptive loop must regress. It shows why an adaptive loop needs a
preservation and stopping rule.
5.2 RQ2: Evidence Helps Repair but Can Harm
Retention
Table 3 and Figure 3 consolidate the assignment outcomes. For
7B, current traces produce the most repairs from wrong starts
(113/135), while stale traces produce the most harms from correct
starts (12/135). Trace minus control repair is+5.9points with task-
cluster 95% CI[−2.2, 17.0]; all six 7B contrasts have Holm-adjusted
𝑝=1.0.
The 14B replication changes the ordering: unavailable evidence
produces the most repairs (126/135), so additional task feedback
is not monotonically useful. From correct starts, stale traces harm
34/135 branches versus 4/135 under current traces, a+22.2-point
contrast with CI[8.9, 37.0] and exact Holm𝑝= 0.0337. Stale minus
control is+12.6points, CI [0.7, 25.9], but does not survive Holm
correction (𝑝= 0.3934). Thus long-context editing pressure explains
part, but not all, of the stale-current gap.
The stale-minus-current interaction across coders is+17.0points
(task-cluster 95% CI[0.7, 33.4]) but remains suggestive rather than
confirmatory after its separate Holm correction (𝑝= 0.3615); we
therefore do not claim a general capacity effect. For 14B correct
starts, stale traces change code in 81.5% of branches, versus 47.4%
for current traces and 77.8% for control; the corresponding harms
are 25.2%, 3.0%, and 12.6%. Churn is therefore neither repair nor
semantic harm. Under both coders, character matching leaves a
token-length difference (498.4 versus 451.7 mean prompt tokens
for stale and control), an audited nuisance rather than a complete
explanation.

AgenticDev ’26, October 12–16, 2026, Munich, Germany Gao, Yang, Yang
0.60 0.65 0.70 0.75 0.80 0.85 0.90
Selective coverage
0.05
0.10
0.15
0.20
0.25Risk among accepted revisions
(a) Verifier risk-coverage
Qwen 7B
Qwen 14B
DeepSeek 6.7B
1 2 3
Forced revisions
0.60
0.65
0.70
0.75
0.80
0.85Correct at current revision
(b) Correctness is not monotone
Current binary
Current trace
Stale trace
Unavailable
Figure 2: Left: retrospective selective risk at matched coverage. Cross-family diversity does not ensure verifier quality. Right:
current correctness across forced revisions is non-monotone even while cumulative ever-correct increases.
Table 3: Common-state repair and continuation harm. Each
cell is event count/135; starts and assignments are identical
across coders.
Start Evidence 7B event 14B event
Wrong Current binary 105/135 115/135
Wrong Current trace 113/135 120/135
Wrong Unavailable 97/135 126/135
Wrong Matched control 105/135 119/135
Correct Current binary 0/135 4/135
Correct Current trace 5/135 4/135
Correct Unavailable 0/135 10/135
Correct Stale wrong trace 12/135 34/135
Correct Matched control 2/135 17/135
5.3 Stale Evidence Resurrects Fixed Bugs
Average uncertainty does not erase constructive counterexamples.
For 7B, all correct-state harms occur in 4/27 tasks (Figure 4); stale
traces regress HumanEval/10 and /89 in all five seeds. In /89, a stale
report from code using Caesar shift 12 changes the fixed shift 4 back
to 12 in every seed. The report contains valid input/expected-output
facts, but falsely asserts that they describe the current code.
For 14B, stale harm is broader: 34 branches across 12/27 task
clusters. HumanEval/10 and /46 regress in 5/5 stale seeds while
their matched controls harm 0/5 and 1/5, respectively. Conversely,
/89 no longer regresses, and /50 and /120 fail under both stale and
control prompts. This redistribution is important: stale evidence is
a reproducible failure mechanism, not a deterministic property of a
task, and responsiveness determines whether the mechanism fires.
This yields a sharper mechanism than “more information helps”:
utility depends jointly on payload, provenance, and the coder’s
response. Candidate-source diagnostics also shift across coders and
were not randomized, so they are descriptive rather than subgroup
effects. The clustering and redistribution explain why task-level,
not branch-level, uncertainty is essential.
5.4 RQ3: Verifier Quality Is Not Independence
At native thresholds, Qwen-7B covers 0.757 of revisions at risk 0.095;
Qwen-14B covers 0.711 at risk 0.040; DeepSeek covers 0.991 at risk
0.298. Coverage confounds direct comparison, so Figure 2a imposes
retrospective matched coverage. At 70%, risks are 0.050, 0.041, and
0.240, respectively. Qwen-14B minus DeepSeek is−19.9points with
task-bootstrap CI[−26.4,− 9.5] when each bootstrap draw refits the
cutoff. This compares the frozen distribution; deployment requires
held-out calibration.
This ordering is not an artifact of choosing 70% coverage: Qwen-
14B minus DeepSeek risk differences remain negative from 60%
through 90% coverage, ranging from−20.5to−4.0points, with all
five task-bootstrap intervals below zero. Repeated code states do
affect the magnitude. Collapsing 2,700 revisions to 617 unique task–
code hashes raises 70%-coverage risks to 0.400, 0.387, and 0.472;
Qwen-14B still has lower empirical AURC (0.225 versus 0.402) and
8.5 points lower risk than DeepSeek. We therefore interpret 19.9
points as the revision-distribution estimate, not an intrinsic model
constant.
Quality also does not imply independent errors. Among hidden-
incorrect revisions at 70% coverage, Qwen-7B/Qwen-14B have𝜙=
0.641with task-cluster CI [0.096, 0.935] and excess joint false ac-
ceptance0.060[0.001, 0.133]. Qwen-14B/DeepSeek have𝜙= 0.021
[−0.231, 0.272] at the same coverage, but DeepSeek’s risk is much
higher. At 75% coverage, all three scored pairs have positive excess-
joint intervals. Dependence is thus an operating-point property,
not a static label attached to a pair of model families.

Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair AgenticDev ’26, October 12–16, 2026, Munich, Germany
Binary Trace None Control
0%
20%
40%
60%
80%
100%Repair rate
78%
84%
72%
78%
85% 89% 93% 88%
(a) Frozen wrong state
Binary Trace None Stale Control
0%
5%
10%
15%
20%
25%
30%Continuation harm
0%
3.7%
0%
8.9%
1.5%
3.0% 3.0%
7.4%
25.2%
12.6%
(b) Frozen correct state
Qwen2.5-7B Qwen2.5-14B
Figure 3: Assignment outcomes from identical frozen states.
Evidence ordering changes across coder capacities; 14B stale
evidence produces the largest continuation harm. Inference
is reported in text.
Table 4: Verifier quality and conditional dependence. Risk is
at 70% coverage;𝜙is conditional on incorrect revisions.
Verifier/pair Risk Conditional𝜙
Qwen-7B 0.050 —
Qwen-14B 0.041 —
DeepSeek-6.7B 0.240 —
Qwen-7B / Qwen-14B — 0.641
Qwen-7B / DeepSeek —−0.072
Qwen-14B / DeepSeek — 0.021
5.5 RQ4: Bundled Admission Changes
Retention and Repair
Table 5 evaluates stopping and verification on the same 900 trajec-
tories. Self-only stopping accepts 99.8% but has 29.5% risk and 70.3%
sound completion. A visible gate prevents 248 false completions
and introduces none, reducing risk to 2.4% while increasing sound
completion to 77.8%. The challenge gate prevents all 265 self-only
false completions in this sample and attains 77.8% sound comple-
tion at 77.8% coverage. Its zero observed errors do not imply zero
Binary Trace None Stale Control
HumanEval/10
HumanEval/89
HumanEval/113
HumanEval/137
0 0 0 5 0
0 0 0 5 0
0 0 0 1 0
0 5 (5 invalid) 0 1 2
0
1
2
3
4
5
Harm seeds
Figure 4: 7B correct-to-incorrect outcomes are clustered, not
uniform. HumanEval/10 and /89 show stale-evidence bug
resurrection in 5/5 seeds; current-trace failures on /137 are
invalid action-schema outputs.
population risk: the conservative one-sided 95% zero-event bound
over 30 task clusters is 9.5%.
Task-cluster uncertainty is wide enough to matter. Self-only risk
has a 95% interval of [0.154, 0.445], visible-gated risk [0, 0.077],
and visible-gated sound completion[0.642,0.900]. The zero-event
task bound is1− 0.051/30 = 0.095; treating 1,877 challenge-passing
revisions as independent would instead give 0.0016 and would be
anti-conservative for cross-task generalization. The empirical result
supports executable gating in this domain, not a universal safety
guarantee.
Strict freshness is not free. Qwen-14B plus a current-evidence
challenge has no observed false completion but covers only 38.4%,
loses 311 baseline sound completions, and requires 2.27 mean re-
visions. Reliability evaluation must expose this abstention/cost
trade-off.
The prospective paired comparison estimates the bundled pol-
icy’s orchestrator-level effect. From correct starts, baseline con-
tinuation harms 13/135 branches and finishes correct on 122/135;
guarded execution has no observed harm and retains correctness
on 135/135. The−9.6-point harm contrast has a task-bootstrap 95%
CI of[−20.7, 0.0] and sign-flip𝑝= 0.25, because all baseline harms
occur in only 3/27 task clusters. From wrong starts, repair falls
from 100/135 to 93/135. Across both start states, unsafe comple-
tion changes from 1/270 to 0/270 (effect−0.4points, CI [−1.1, 0.0]),
which is too sparse to demonstrate superiority. Sound completion
changes from 219/270 to 211/270 (effect−3.0points, CI [−8.5, 1.1]),
so the preregistered−5-point non-inferiority criterion is not met.
The bundled guard therefore shifts observed errors while reducing
both revision plasticity and completion coverage; these data do not
identify any component’s individual effect.
5.6 RQ5: Repository Contracts Expose
Completion-Gate Dependence
Table 6 consolidates the four stack matrices. The original Qwen2.5-
14B study has a severe completion floor: Contract OFF produces

AgenticDev ’26, October 12–16, 2026, Munich, Germany Gao, Yang, Yang
−10.0 −7.5 −5.0 −2.5 0.0 2.5 5.0
Contract effect (ON minus OFF), percentage points
Unsafe completion
Sound completion
-2.78 pp  [-8.33, +0.00]
-0.69 pp  [-2.08, +0.00]
sound NI margin (-5 pp)
Co-primary repository-agent effects
Figure 5: Prespecified repository-agent contract effects (ON minus OFF). Bars are task-cluster bootstrap 95% intervals over 24
task-level effects; the three seeds per cell are averaged before inference. Unsafe-completion superiority requires its one-sided
upper bound below zero; sound-completion non-inferiority requires its lower bound above −5points. Only the latter, floor-
limited criterion is met, so the joint IUT fails.
Table 5: Stopping-policy replay over 900 fixed trajectories.
CIs are task-clustered; paired changes are reported in text.
Policy Cov. Risk Sound Rounds
Self only 0.998 0.295 0.703 1.03
Self + visible 0.797 0.024 0.778 1.55
Self + challenge 0.778 0.000 0.778 1.56
Qwen-14B only 0.794 0.046 0.758 1.52
Qwen-14B + challenge 0.769 0.000 0.769 1.55
Challenge executable 0.788 0.000 0.788 1.52
Qwen-14B + fresh challenge 0.384 0.000 0.384 2.27
five accepted completions, whereas Contract ON produces none.
It removes all four observed unsafe completions but also the only
sound one; 276/288 rollouts exhaust the action budget. Figure 5 gives
the task-equal effects. Unsafe completion changes by−2.78points
(task-cluster 95% CI[−8.33, 0.00]), missing strict superiority, while
sound completion changes by−0.69points ([−2.08, 0.00]), passing
the−5-point margin. With only one OFF-arm sound completion,
that pass is weak liveness evidence and the joint decision is negative.
The 32B stack is the only replication with observed unsafe com-
pletion under Contract ON: six unsafe completions are concentrated
in two tasks, and the gate false-passes incorrect proposals and
submissions. Qwen3-Coder-Next and Devstral show no observed
unsafe completion, but they produce only six and four accepted
completions, respectively; 282/288 and 284/288 rollouts exhaust
their action budgets. These are stack-level ecological contrasts,
not identified capacity or model-family effects. Full gate, cost, and
sensitivity breakdowns remain in the artifact.
Table 7 moves the two Devstral factorials into one inferential
summary. No component, depth, contract, or interaction effect
survives its preregistered six-test Holm family. Certification has
the largest descriptive sound-completion effect, but only four tasks
support it and𝐶= 0removes the checkpoint-completion path; the
contrast therefore partly reflects endpoint mechanics rather than an
isolated semantic verification benefit. The depth factorial contains
0/576 unsafe and 25/576 sound completions. Revision caps rarely
bind, so its null depth result concerns this sparse-proposal process,
not loop depth in general.
Across the four stack matrices, accepted-completion totals are
only 5, 12, 6, and 4, and OFF-arm sound-completion rates are 0–
2.1%. Thus the tables expose the common floor directly: the contract
changes completion control but does not establish competence or
liveness.
6 Evidence-Bound Typed Loop Contract
The observed failures motivate an auditable orchestration specifica-
tion, not a universally validated remedy or a new prompting recipe.
Its four interfaces separate obligations that the negative policy and
factorial decisions show must be evaluated rather than assumed.
State-bound evidence.Every observation is carried in an envelope
𝐸=(ℎ 𝑐𝑜𝑑𝑒,ℎ𝑠𝑢𝑖𝑡𝑒,𝑒𝑥𝑒𝑐𝑢𝑡𝑖𝑜𝑛_𝑖𝑑,𝑝𝑎𝑦𝑙𝑜𝑎𝑑).
The orchestrator may use𝐸 to revise only whenℎ𝑐𝑜𝑑𝑒 equals the
current state hash. A mismatch triggers refresh,Keep, orEscalate;
it never directly triggers a patch.
Typed revision actions.Free-form text conflates “no edit is needed”
with “the attempted patch was unparsable. ” We use
𝑅𝑒𝑣𝑖𝑠𝑖𝑜𝑛𝐴𝑐𝑡𝑖𝑜𝑛=Keep|Patch(𝑐𝑜𝑑𝑒)|Escalate(𝑟𝑒𝑎𝑠𝑜𝑛).
Only a parsed, executablePatchmay replace the current state. In
the 7B common-state study, all five current-trace harms on Hu-
manEval/137 are responses containing onlySTATUS: DONE without
code. A fail-closed parser that maps this action toKeep, rather than
treating it as an invalid patch, would retain the correct checkpoint
in these recorded branches.
Last-known-good checkpoint.The ledger records code and ev-
idence hashes for the last state that passed the configured gate.
Invalid actions never overwrite it. This makes correctness absorb-
ing with respect to parser and protocol failures even when model
behavior is not.
Risk- and dependence-aware stopping.Verifier selection uses risk
at the intended coverage and conditional dependence, not model
diversity as a proxy. Our matched-coverage estimates are retro-
spective; deployment additionally requires held-out calibration and

Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair AgenticDev ’26, October 12–16, 2026, Munich, Germany
Table 6: Repository-agent stack matrices. Each arm has 72 rollouts and reports accepted/unsafe/sound counts; effects are
task-equal Contract ON minus OFF percentage points with task-cluster 95% CIs. Every joint IUT fails; sound non-inferiority
passes only under severe completion floors.
Stack Current/OFF Current/ON Stale/OFF Stale/ONΔunsafe [95% CI]Δsound [95% CI]
Qwen2.5-14B 3/2/1 0/0/0 2/2/0 0/0/0−2.78[−8.33,0.00] −0.69[−2.08,0.00]
Qwen2.5-Coder-32B 2/0/2 5/3/2 1/0/1 4/3/1+4.17[0.00,11.11]0.00[−2.08,2.08]
Qwen3-Coder-Next 0/0/0 2/0/2 0/0/0 4/0/40.00[0.00,0.00] +4.17[0.00,11.11]
Devstral Small 2 24B 0/0/0 2/0/2 0/0/0 2/0/20.00[0.00,0.00] +2.78[0.00,7.64]
Table 7: Devstral factorial effects (percentage points; 𝑛= 576each). CIs are task-cluster 95%; 𝑝𝐻 is Holm-adjusted within each
six-test family. B, A, and C denote state binding, admission/rollback, and completion certification.
Design (𝑛=576) ContrastΔunsafe [95% CI];𝑝 𝐻 Δsound [95% CI];𝑝 𝐻
23 components B: state binding−0.69[−2.08,0.00]; 1.000+0.69[0.00,1.74]; 1.000
A: admission/rollback0.00[0.00,0.00]; 1.000+0.69[−0.69,2.43]; 1.000
C: certification+0.69[0.00,2.08]; 1.000+6.25[0.69,13.19]; 0.753
4×2depth–contract Cap 1 to cap 80.00[0.00,0.00]; 1.000−0.23[−1.77,1.09]; 1.000
Contract ON minus OFF0.00[0.00,0.00]; 1.000+3.13[0.00,9.03]; 1.000
Depth×contract0.00[0.00,0.00]; 1.000−0.45[−7.63,6.27]; 1.000
drift monitoring. A completion decision records its operating point
so residual risk remains auditable.
6.1 Operational Semantics
The contract turns a permissive text loop into a small state machine.
At step𝑡, the orchestrator stores current state𝑆𝑡 , last-known-good
state𝐿𝑡 (possibly empty), and an append-only evidence ledger. It
executes the following transaction:
(1) run a named suite on𝑆𝑡 ; append evidence bound to the state
and suite;
(2) reject or refresh𝐸𝑡 if either hash does not match the requested
state and suite;
(3) request one typed action;Keepleaves state unchanged,Esca-
lateabstains, and only a parseablePatchcreates candidate
𝑆′ 𝑡 ;
(4) evaluate𝑆′ 𝑡 with the configured commit gate; on failure retain
𝑆𝑡 or roll back to𝐿𝑡 , never overwrite𝐿𝑡 ;
(5) stop only if the completion policy accepts the committed state at
its declared risk–coverage operating point; otherwise continue
within budget.
Two safety properties follow mechanically. First, a state-hash mis-
match cannot trigger a commit. Second, parser or action-schema
failure cannot erase a checkpoint. Neither property claims that
a hash-matched patch is semantically correct; that residual risk
belongs to the executable and learned verifiers.
6.2 StateSeal Reference Implementation and
Conformance
StateSeal wraps existing agents and project-defined verifiers. Its
admission broker recomputes state identity, verifies an isolated
proposal outside the agent process, preserves a checkpoint, and
recertifies it before issuing a digest-bearing receipt. It records cov-
erage and delivery impact but does not learn risk or dependence.
At the frozen snapshot, all 35 deterministic failure-injection cases
and three managed-language fixtures pass. This is conformance
evidence, not effectiveness, competence, verifier independence, or
study validation. The public v0.1.1 release provides source, com-
mands, and the case catalog.
In deterministic replay, state binding intercepts all 12 and 34
stale-condition harms for 7B and 14B; adding typed action reduces
total harm from19 → 2and69 → 33. A challenge checkpoint
blocks all 19 7B harms but misses two 14B hidden-test regressions.
Because stale evidence is assigned only to correct starts, replay
diagnoses mechanisms rather than end-to-end utility.
7 Discussion
Controlled counterexamples.Search does not ensure retention;
valid reports become harmful under state mismatch; and model-
family diversity ensures neither low verifier risk nor independent
errors. Iteration cannot substitute for evidence, state management,
or verification.
What they do not refute.Loops remain useful when expected
repair exceeds continuation harm. We critique unconditional con-
tinuation and unqualified completion, not adaptive search: depth
samples transitions; orchestration determines whether value accu-
mulates.
Why the three factors are not interchangeable.Better feedback
cannot help an unresponsive coder; responsiveness can amplify
stale evidence; and proposal quality cannot offset correlated false
acceptance. Equation 8 requires both low marginal false acceptance
and low dependence.
Safety, plasticity, liveness, and interface fit are separate.The
prospective policy prevents observed regression but rejects useful
repairs; repository contracts similarly trade unsupported against

AgenticDev ’26, October 12–16, 2026, Munich, Germany Gao, Yang, Yang
Table 8: Contract obligations, reference mechanisms, conformance cases, and residual risks.
Obligation Reference mechanism Conformance evidence Residual risk
State-bound evidence Bind candidate, tree, policy, verifier, and con-
text identities
Reject replay, mutation, and wrong-
tree evidence (SB001–SB007)
Aligned evidence may be wrong; host and verifier
remain trusted
Independent admission Broker alone advances verified state and is-
sues decisions
Self-report cannot authorize admis-
sion (SB021, SB027)
Process separation does not imply error indepen-
dence
Checkpoint preservation Retain and exactly restore the last verified
candidate
Regressions and malformed actions
cannot overwrite it (SB008–SB010,
SB014, SB016)
Only oracle-covered properties are preserved
Fresh certification Re-execute checks on the selected completion
state
Failed recertification cannot com-
plete (SB012, SB020, SB031)
Flakiness, drift, and suite incompleteness remain
Auditable stopping Typed outcomes, hash-linked events, digest-
bearing receipt, coverage and liveness fields
False pass/rejection, abstention,
and coverage collapse are explicit
(SB028–SB035)
Auditability is not calibration, liveness, or attes-
tation
sparse sound completion. Neither randomized factorial is Holm-
significant. Admission, preservation, certification, interface fit, and
depth remain distinct.
Implications for agent evaluation.Pass@1 or best-of- 𝑘 misses
state loss, incorrect acceptance, and low risk from abstention. Evalu-
ations should also report current versus ever-correct, common-state
transitions, coverage–risk, sound completion, cost, and conditional
verifier overlap. Our 24 repository bugs test mechanisms, not preva-
lence.
Mechanism, policy, and calibration.State binding, transition
guards, checkpoints, and recertification are mechanical. Verifier ad-
equacy, error dependence, residual risk, and safety–liveness remain
empirical. The implementation makes failure modes falsifiable; it
does not improve agent or oracle competence.
8 Threats to Validity
External validity.The trajectory and common-state studies use
public HumanEval tasks that may occur in model training data, and
27 tasks are selected for 7B-observed repairability. Pairing strength-
ens assignment contrasts but not absolute-rate generalization. The
repository study covers 24 bugs from nine Python projects, four
coder stacks, and one scaffold. Stack factors vary jointly, interface
friction is material, and tasks within projects may be correlated;
these are mechanism tests, not random samples of agents, lan-
guages, projects, or bugs. The controlled function-level studies stop
at 14B parameters and do not establish that frontier-scale hosted
models have the same transition kernel.
Construct validity.Challenge and hidden inputs are disjoint but
share HumanEval+ construction, and no finite repository suite is a
complete specification. One-step staleness is an intervention, not
its natural prevalence; exact-code change is not semantic churn.
Verifier family and capacity are confounded. Self acceptance is
declarative, whereas repository acceptance also includes the ON
arm’s frozen checkpoint rule.
Internal and statistical validity.Forced revision is not a natural
adaptive policy. Common states address post-treatment risk-set bias,
but all six 7B and five of six 14B contrasts are nonsignificant after
Holm correction; no secondary cross-coder interaction survives
correction. The original repository contract identifies only a joint
effect; component randomization remains event-sparse, and the
depth caps rarely bind. The four stack matrices have only 5, 12,
6, and 4 accepted completions; under this floor, the absolute −5-
point non-inferiority margin weakly constrains liveness. Task-equal
inference has project-equal and leave-one-project-out checks, but
only nine projects support project-level generalization.
Reproducibility.Prompts, private suites, full lineage, and the nu-
merical reconstruction package are retained internally. The public
materials provide the StateSeal v0.1.1 source, commands, and case
catalog; licensing and evaluator privacy prevent redistribution of
the full raw trajectories and private suites. The post-study artifact
tests mechanism conformance, not effectiveness, verifier adequacy
or independence, or trust in the host, runner, Git, and OS. Strict
admission can reject useful repairs; its UI is outside the trusted
boundary.
9 Conclusion
Iteration supplies proposals, not reliability. The typed contract
separates state alignment, admission, preservation, grounded com-
pletion, competence, liveness, and interface fit; its implementation
enforces state binding, checkpoints, recertification, and auditable
decisions. Verifier quality, dependence, and general reliability re-
main empirical.
Availability and disclosures.The numerical reconstruction pack-
age is retained internally; private suites and licensed source are
not redistributed. StateSeal v0.1.1 is at https://github.com/hellogxp/
stateseal. AI-assisted code and prose were author-verified.
References
[1] Islem Bouzenia and Michael Pradel. 2025. Understanding Software Engineer-
ing Agents: A Study of Thought-Action-Result Trajectories. In40th IEEE/ACM
International Conference on Automated Software Engineering. IEEE, 2846–2857.
doi:10.1109/ASE63991.2025.00234
[2] José Pablo Cambronero, Michele Tufano, Sherry Shi, Renyao Wei, Grant Uy, Runx-
iang Cheng, Chin-Jung Liu, Shiying Pan, Satish Chandra, and Patrick Rondon.
2026. Abstain and Validate: A Dual-LLM Policy for Reducing Noise in Agentic
Program Repair. InProceedings of the IEEE/ACM 48th International Conference on
Software Engineering: Software Engineering in Practice. Association for Computing
Machinery, 118–129. doi:10.1145/3786583.3786858
[3] Edward Y. Chang, Longling Geng, and Emily J. Chang. 2026. Mnemosyne: Agentic
Transaction Processing for Validating and Repairing AI-Generated Workflows.
arXiv preprint arXiv:2607.00269(2026). doi:10.48550/arXiv.2607.00269
[4] Mark Chen, Jerry Tworek, Heewoo Jun, Qiming Yuan, Henrique Ponde de Oliveira
Pinto, Jared Kaplan, Harri Edwards, Yuri Burda, et al . 2021. Evaluating Large
Language Models Trained on Code.arXiv preprint arXiv:2107.03374(2021). doi:10.
48550/arXiv.2107.03374
[5] Dekun Dai, MingWei Liu, Anji Li, Jialun Cao, Yanlin Wang, Chong Wang, Xin
Peng, and Zibin Zheng. 2025. FeedbackEval: A Benchmark for Evaluating
Large Language Models in Feedback-Driven Code Repair Tasks.arXiv preprint
arXiv:2504.06939(2025). doi:10.48550/arXiv.2504.06939

Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts for Agentic Code Repair AgenticDev ’26, October 12–16, 2026, Munich, Germany
[6] Yonatan Geifman and Ran El-Yaniv. 2019. SelectiveNet: A Deep Neural Network
with an Integrated Reject Option. InProceedings of the 36th International Con-
ference on Machine Learning (Proceedings of Machine Learning Research, Vol. 97).
PMLR, 2151–2159. https://proceedings.mlr.press/v97/geifman19a.html
[7] Thibaud Gloaguen, Niels Mündler, Mark Niklas Mueller, Veselin Raychev, and
Martin Vechev. 2026. Coding Agents Don’t Know When to Act. InSecond Work-
shop on Agents in the Wild: Safety, Security, and Beyond. https://openreview.net/
forum?id=CVg4Honh4Y
[8] Daya Guo, Qihao Zhu, Dejian Yang, Zhenda Xie, Kai Dong, Wentao Zhang,
Guanting Chen, Xiao Bi, Y. Wu, Y. K. Li, et al . 2024. DeepSeek-Coder: When
the Large Language Model Meets Programming—The Rise of Code Intelligence.
arXiv preprint arXiv:2401.14196(2024). doi:10.48550/arXiv.2401.14196
[9] Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei
Yu, Xinying Song, and Denny Zhou. 2024. Large Language Models Cannot Self-
Correct Reasoning Yet. InInternational Conference on Learning Representations.
https://openreview.net/forum?id=IkmD3fKBPQ
[10] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir
Press, and Karthik R. Narasimhan. 2024. SWE-bench: Can Language Models
Resolve Real-World GitHub Issues?. InInternational Conference on Learning Rep-
resentations. https://openreview.net/forum?id=VTF8yNQM66
[11] Ryo Kamoi, Yusen Zhang, Nan Zhang, Jiawei Han, and Rui Zhang. 2024. When
Can LLMs Actually Correct Their Own Mistakes? A Critical Survey of Self-
Correction of LLMs.Transactions of the Association for Computational Linguistics
12 (2024), 1417–1440. doi:10.1162/tacl_a_00713
[12] Elliot Myunghoon Kim, Avi Garg, Kenny Peng, and Nikhil Garg. 2025. Correlated
Errors in Large Language Models. InProceedings of the 42nd International Confer-
ence on Machine Learning (Proceedings of Machine Learning Research, Vol. 267).
PMLR, 30038–30066. https://proceedings.mlr.press/v267/kim25e.html
[13] Cuong Chi Le, Aashish Yadavally, Minh Le-Anh, and Tien N. Nguyen. 2026.
Benchmarking Code Improvement with Progressive, Adaptive, and Interactive
Feedback.arXiv preprint arXiv:2607.01360(2026). doi:10.48550/arXiv.2607.01360
[14] Jiawei Liu, Chunqiu Steven Xia, Yuyao Wang, and Lingming Zhang. 2023. Is
Your Code Generated by ChatGPT Really Correct? Rigorous Evaluation of Large
Language Models for Code Generation. InAdvances in Neural Information Pro-
cessing Systems, Vol. 36. Neural Information Processing Systems Foundation, Inc.,
21558–21572. doi:10.52202/075280-0943
[15] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah
Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, et al .
2023. Self-Refine: Iterative Refinement with Self-Feedback. InAdvances in Neural
Information Processing Systems, Vol. 36. Neural Information Processing Systems
Foundation, Inc., 46534–46594. doi:10.52202/075280-2019
[16] Qianru Meng, Xiao Zhang, Zhaochun Ren, and Joost Visser. 2026. EviACT:
An Evidence-to-Action Framework for Agentic Program Repair.arXiv preprint
arXiv:2605.27238(2026). doi:10.48550/arXiv.2605.27238
[17] Open Policy Agent Contributors. 2026. Open Policy Agent Documentation.
Accessed 2026-07-24. https://www.openpolicyagent.org/docs
[18] Arjun Panickssery, Samuel R. Bowman, and Shi Feng. 2024. LLM Evaluators
Recognize and Favor Their Own Generations. InAdvances in Neural Information
Processing Systems, Vol. 37. Neural Information Processing Systems Foundation,
Inc., 68772–68802. doi:10.52202/079017-2197
[19] Andrey Podivilov, Vadim Lomshakov, Sergey Savin, Matvei Startsev, Roman
Pozharskiy, Maksim Parshin, and Sergey Nikolenko. 2026. AgentLens: Production-
Assessed Trajectory Reviews for Coding Agent Evaluation.arXiv preprint
arXiv:2607.06624(2026). doi:10.48550/arXiv.2607.06624
[20] Qwen, An Yang, Baosong Yang, Beichen Zhang, Binyuan Hui, Bo Zheng, Bowen
Yu, Chengyuan Li, Dayiheng Liu, Fei Huang, Haoran Wei, Huan Lin, Jian Yang,
Jianhong Tu, Jianwei Zhang, Jianxin Yang, Jiaxi Yang, Jingren Zhou, Junyang
Lin, Kai Dang, Keming Lu, Keqin Bao, Kexin Yang, Le Yu, Mei Li, Mingfeng Xue,
Pei Zhang, Qin Zhu, Rui Men, Runji Lin, Tianhao Li, Tianyi Tang, Tingyu Xia,
Xingzhang Ren, Xuancheng Ren, Yang Fan, Yang Su, Yichang Zhang, Yu Wan,
Yuqiong Liu, Zeyu Cui, Zhenru Zhang, and Zihan Qiu. 2024. Qwen2.5 Technical
Report.arXiv preprint arXiv:2412.15115(2024). doi:10.48550/arXiv.2412.15115
[21] Priyam Sahoo, Gaurav Mittal, Xiaomin Li, Shengjie Ma, Benjamin Steenhoek,
Pingping Lin, and Yu Hu. 2026. AgentLens: Revealing the Lucky Pass Problem
in SWE-Agent Evaluation.arXiv preprint arXiv:2605.12925(2026). doi:10.48550/
arXiv.2605.12925
[22] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and
Shunyu Yao. 2023. Reflexion: Language Agents with Verbal Reinforcement Learn-
ing. InAdvances in Neural Information Processing Systems, Vol. 36. Neural Informa-
tion Processing Systems Foundation, Inc., 8634–8652. doi:10.52202/075280-0377
[23] Supply-chain Levels for Software Artifacts. 2026. SLSA v1.2 Provenance. Accessed
2026-07-24. https://slsa.dev/spec/v1.2/provenance
[24] Santiago Torres-Arias, Hammad Afzali, Trishank Karthik Kuppusamy, Reza Curt-
mola, and Justin Cappos. 2019. in-toto: Providing Farm-to-Table Guarantees for
Bits and Bytes. In28th USENIX Security Symposium. USENIX Association, 1393–
1410. https://www.usenix.org/conference/usenixsecurity19/presentation/torres-
arias
[25] Gladys Tyen, Hassan Mansoor, Victor Carbune, Peter Chen, and Tony Mak. 2024.
LLMs Cannot Find Reasoning Errors, but Can Correct Them Given the Error
Location. InFindings of the Association for Computational Linguistics: ACL 2024.
Association for Computational Linguistics, 13894–13908. doi:10.18653/v1/2024.
findings-acl.826
[26] Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, and Lingming Zhang. 2025. De-
mystifying LLM-Based Software Engineering Agents.Proceedings of the ACM on
Software Engineering2, FSE (2025), 801–824. doi:10.1145/3715754
[27] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao,
Karthik Narasimhan, and Ofir Press. 2024. SWE-agent: Agent-Computer Inter-
faces Enable Automated Software Engineering. InAdvances in Neural Information
Processing Systems, Vol. 37. Neural Information Processing Systems Foundation,
Inc., 50528–50652. doi:10.52202/079017-1601
[28] Yunxiang Zhang, Muhammad Khalifa, Lajanugen Logeswaran, Jaekyeom Kim,
Moontae Lee, Honglak Lee, and Lu Wang. 2024. Small Language Models Need
Strong Verifiers to Self-Correct Reasoning. InFindings of the Association for
Computational Linguistics: ACL 2024. Association for Computational Linguistics,
15637–15653. doi:10.18653/v1/2024.findings-acl.924
[29] Bingchen Zhao, Dhruv Srikanth, Yuxiang Wu, and Zhengyao Jiang. 2026.
SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents.arXiv
preprint arXiv:2605.21384(2026). doi:10.48550/arXiv.2605.21384
Received 2026-07-23; accepted 2026-08-20
