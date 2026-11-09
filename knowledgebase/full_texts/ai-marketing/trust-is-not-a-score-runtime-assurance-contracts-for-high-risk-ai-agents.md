---
title: 'Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents'
url: https://arxiv.org/abs/2609.39717
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Serhii Zabolotnii
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.39717
pages: 18
chars: 54080
fetched_at: '2026-11-08T13:33:10+00:00'
kb_version: 1
---

# Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents

Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI
Agents
Serhii Zabolotnii∗1,2,3
1Cherkasy State Business College, Cherkasy, Ukraine
2State Scientific Research Institute of Armament and Military Equipment Testing and
Certification, Cherkasy, Ukraine
3healthPrecision, New York, NY, USA
Abstract
Benchmarks, audits, and agent protocols describe performance, permissions, and repair, but
not how observed evidence should change an agent’s authority during a consequential task. We
call this the assurance-transition gap. We propose a Runtime Assurance Contract (RAC), a
policy-level formal schema binding autonomy boundaries, component eligibility, evidence state,
transition policy, human-review capacity, and non-compensatory gates. Under RAC, soft metrics
may inform routing, whereas a failed or unknown mandatory gate forces retry, switch, escalation,
deferral, or stop; aggregate performance cannot authorize action. We define the contract, an
evidence record, a permission rule, and five invariants, and illustrate them in clinical, industrial,
and judicial failure probes. We then report a deterministic failure-injection study in agentic
coding: 174 constructed cases, each a distinct mechanism, evaluated by a gate conjunction,
a score-only rule, and a restricted protocol baseline. At the published example weights and
threshold, the score rule admits 56 of 63 block-required injections and all 24 review-required
injections. Tuned in hindsight, it matches the conjunction case for case. For positive weights, a
positive threshold, binary risk signals, and each signal firing alone on some case, we show that
the two rules agree on every case if and only if the threshold does not exceed the smallest weight.
On a further 124 cases written blind by a model of another vendor, the conjunction itself admits
35 of 79 injections, and so does the tuned score rule: a missing detector is invisible to every
decision rule. A separate set of 18 hand-authored traces checks version-pinned evidence and
review transitions against simpler policy variants. In a further prospective synthetic holdout
of 24 episodes, two blinded LLM judges assign identical labels to all 72 action attempts; RAC
and a separately implemented full stateful baseline both match these labels. These studies
test mechanisms on synthetic cases; they establish neither deployed safety nor cross-domain
effectiveness.
Keywords:runtime assurance, dependable AI agents, human oversight, fail-closed gates, escalation
policy, high-risk AI, auditability, authority boundaries
1 Introduction
Agentic AI systems reach actions through chains of tool calls, component invocations, and state
transitions. A plausible final output can conceal an unauthorized component, stale context, or
∗ORCID 0000-0003-0242-2234. Email: zabolotnii.serhii@csbc.edu.ua
1
arXiv:2609.39717v2  [cs.AI]  16 Oct 2026

a skipped review earlier in the chain. Here, ahigh-riskworkflow is one in which such a path
can materially affect health, legal rights, physical safety, critical operations, or access to essential
services.
Two lines of work address complementary parts of the problem: evaluation-centered governance,
which makes claims measurable and reviewable [39], and protocol-centered engineering, which gives
agent–software interactions explicit permissions, task state, and repair paths [33]. Yet a governance
proxy does not establish its underlying deployment goal [34], and a well-formed tool call does not
establish that the agent should retain its current authority.
The unresolved issue is the mapping from an evidence state to an authority transition, which we
call theassurance-transition gap. The earlier TRACE framework [43] treats trust in a human–task–
agent interaction as measured, calibrated, and uncertainty-qualified evidence, but measurement
alone neither grants nor withdraws authority. Nor do assurance arguments, model-level abstention,
or runtime monitors automatically compose component eligibility, evidence continuity, escalation,
and available human review into one task-level decision.
We therefore propose to treat assurance as a non-compensatory runtime contract that turns
measured conditions into bounded authority. For an autonomous system, this is an adaptation
problem in which the property being adapted is the agent’s authority. This paper defines the
Runtime Assurance Contract (RAC), separates soft routing evidence from hard authorization gates,
states five invariants, and evaluates constructed failure injections and transition scenarios. The
contribution is a policy-level formal schema, not an implemented safety guarantee or a new trust
score. Non-compensatory means that no high score elsewhere can offset a failed mandatory gate.
2 From Evaluation and Protocols to Authority
RAC specifies anauthority transition: the permitted change in what an agent may do after evidence
has been observed. Representative approaches differ in their usual unit of control (Table 1).
Calibration yields evidence about confidence quality without granting system permissions [15];
governance proxies support review while remaining detachable from deployment outcomes [34];
and agent protocols such as MCP and A2A specify interfaces, permissions, and repair but leave
application-specific authority gates to the deploying system [1, 25, 33]. Assurance cases including
AMLAS organize evidence into a safety argument [2, 8, 17] rather than acting as runtime dispatchers,
and selective prediction offers a model-level reject option without reallocating task authority [12, 13].
Runtime enforcement is the nearest technical predecessor: shields and the Simplex family bind a
safety predicate to a guarded fallback transition [3, 7, 31, 32], a line since extended to probabilistic
and online synthesis [18, 22] and surveyed for AI specifically [23]; recent work addresses its adoption
cost by connecting shield synthesis to standard learning frameworks [30]. What these enforce is a
specification over actions in a modeled environment. RAC treats component eligibility, evidence
continuity, repair, escalation, and bounded human review as first-class policy objects rather than
a single plant safety predicate. Tiered Agentic Oversight is a neighboring empirical example of
task-sensitive routing [21]. As regulatory motivation, Article 72 of the EU AI Act makes post-market
monitoring a continuing obligation [11].
RAC can also be read as a self-adaptation policy. In the MAPE-K reference model, an autonomic
manager monitors a managed system, analyzes the observations, plans an adaptation, and executes
it over shared knowledge [20, 40]. In these terms the agent is the managed system, the evidence
record belongs to the knowledge, the gates are analysis predicates, andΠis the planner. The
adapted property is the agent’s own authority, and the adaptation is non-compensatory. Dynamic
assurance cases already couple self-adaptation with assurance evidence that is updated at runtime [4];
2

RAC places such evidence on the authorization path of each consequential action rather than in
an argument about the adaptive system as a whole. Human participation in adaptation has been
modeled as a tactic with its own latency and reliability [5], and latency-aware planning treats the
time a tactic takes to have effect as a decision input [26].G_SUPERVISIONmakes the corresponding
assumption explicit: human review is an admissible transition only while a qualified reviewer can
complete it within the declared deadline.
Table 1: Typical scope of representative assurance approaches. The entries are qualified comparisons,
not claims that every implementation has the same boundary. AMLAS denotes Assurance of
Machine Learning in Autonomous Systems; RTA, runtime assurance; MAPE-K, monitor–analyze–
plan–execute over shared knowledge; and RAC, the proposed Runtime Assurance Contract.
Approach Measures outcomes Defines permissions Defines repair Binds human capacity Evidence→ authority
Model evaluation / cali-
bration
yes no no no no
Governance proxy / au-
dit
yes indirect optional optional indirect
Agent protocol interface not inherent yes yes optional configured
Assurance case / AM-
LAS
argument constraints mitigation optional argument-level
Selective prediction model risk no reject optional model-level
Runtime enforcement /
RTA
safety state yes fallback typically no guarded transition
Self-adaptive loop
(MAPE-K)
monitored state indirect adaptation optional adaptation plan
Proposed RACmixed evidence yes yes explicit composed transitions
Two lines of work on agent safety are nearer still, and RAC is best positioned relative to them.
The first places a learned component in the authorization path. GuardAgent protects a target agent
by analyzing a safety request and emitting guardrail code for execution [41], and step-level guardrail
models judge a tool invocation before it executes, reasoning over interaction history to produce
a safety verdict [27]. A benchmark of such guards across multi-step trajectories finds that their
efficacy depends more on the structure of what they are shown than on the guard model [6], which
is consistent with the position taken here: a judgment produced by a learned component is evidence,
and Equation 4 treats it as a soft metric rather than as a permission (I1, I3). The distinction is not
that such guards are weak — several are strong — but that a system in which they can authorize
has no fail-closed element left when they are wrong.
The second line enforces permissions deterministically at the tool-call interface. Progent rep-
resents privilege as symbolic rules over tool names and arguments and checks every call against
them by a deterministic procedure [35]; MiniScope derives permission hierarchies automatically so
that least privilege does not depend on hand-written policy [44]. This is the protocol-only position
evaluated in Section 7, and it is a genuine guarantee at the boundary it governs. Its limit is scope
rather than rigor: a call may be individually permitted while the task evidence supporting it has
gone stale, lost provenance, or outrun the review capacity the policy assumes. Two recent results
sharpen this. An empirical study of permission-boundary inference reports that frontier models
both omit permissions the execution chain needs and grant unused or sensitive ones, concluding that
authorization is not a conservative-versus-permissive calibration problem [42] — in other words,
authority is not a scalar dial, the same claim Section 4 makes analytically. Separately, least privilege
has been argued insufficient for agentic systems that combine, approve, and amplify permissions
3

across workflows, motivating a compositional notion of least autonomy [28]. RAC shares that
diagnosis and differs in remedy: it keeps the permission model and adds a task-level veto with a
persisted transition record. Hazard-driven derivation of enforceable specifications is complementary
to both [9].
The proposed distinction is compositional. RAC does not replace these approaches; it defines
how their evidence and constraints jointly govern the next authority state.
3 The Runtime Assurance Contract
We define aRuntime Assurance Contractas the tuple
CRA =⟨B,K,Π,H,E,G⟩.(1)
The tuple is a normative minimum for an implementable policy, not a deployed enforcement engine.
Autonomy boundaryB. B(x,a,t )∈{allow,require_review,deny} evaluates proposed action
a in task contextx under active policy versiont. These verdicts are boundary decisions, not
state-transition labels.
Component eligibilityK. K(m,q,x,η t,t )∈{ 0, 1} states whether componentm may execute
task q given context x, evidence state ηt, and policy versiont. It may depend on capability,
calibration, modality, version, and domain restrictions, and is not a model ranking. Eligibility is
re-evaluated before eachexecutetransition and after aretry,switch, or policy-version change.
Stateful transition policyΠ.
Π(zt,o t,η t)−→(δ t,z t+1,η t+1), δ t∈∆,(2)
where zt is the runtime state, including the active context and rule versions,ot the observed output,
and∆ = {execute,verify,retry,switch,escalate,defer,act,stop} . Hereexecuteinvokes an eligible
component;verifyupdates evidence;retryrepeats a step;switchselects another component;escalate
requests human authority;deferholds a safe state;actreleases the action; andstopterminates the
action path.
Human authority and capacityH.The contract names an accountable role, safe-fallback
owner, credentials, veto rights, review outcomes, response deadline, and capacity variables such
as queue length and reviewer load. An assigned role without timely capacity does not satisfy this
requirement.
Evidence schemaE.Every transition in∆emits
et =⟨id,time,source,z t,z t+1,δ t,context_version,rule_version,
component_version,gt,β t,input_hash,output_ref,reason,
review_required,reviewer,review_outcome⟩.
(3)
Hereg t records gate outcomes andβt the remaining retry budget. A required review may initially
have no assigned reviewer; that null value records an unavailable or pending assignment, not approval.
review_outcomeis pending, approved, rejected, timed out, or returned for change. An approval is
bound to the context, rule, component, input, and output versions in the reviewed evidence record.
It is invalidated when any of those change beforeact.
4

Hard-gate setG.The applicable subset Gt⊆G contains mandatory functionsg : (zt,o t,η t)↦→
{0, 1,⊥}, where⊥ denotes an unknown or unevaluated outcome. Soft metrics cannot compensate
for0or⊥(Section 4).
Intake Admissibility check Component execution (L2) Evidence verification
Retry / switch
Human review (L4)
Authorized
action
Deferred
Safe stop
allow
recoverable failure
∧retry budget
all gates pass∧
policy authorizes
defer
unrecoverable
escalate
reject / no change
defer
approve⇒revalidate pins and gates
require review
deny (not overridable by review)
×
no direct L2→act authority
hard gatesG(non-compensatory∧):
BOUNDS·CONTEXT·EVIDENCE
ELIGIBILITY·SUPERVISION·RESOLUTIONevery transition in∆
emits evidence recordet
reviewer unavailable or over
declared capacity⇒
defer / stop, never auto-approve
Figure 1: RAC state machine. An output does not authorize action directly. Failed or unknown
mandatory gates fail closed; unavailable mandatory review yieldsdeferorstop. Each consequential
transition emitse t (Eq. 3); Table 2 specifies failure transitions.
TRACE supplies one architectural mapping, withB,K,Π, and H corresponding to its L1 rule
core, L2 component inventory, L3 orchestration, and L4 supervision, andE spanning all layers. RAC
itself is architecture-neutral.
Consider an agent preparing a medication order. A stale medication list failsG_CONTEXT, so
Πemitsretry; after refresh,G_SUPERVISIONrequires a credentialed clinician within the declared
queue and response limits, so the next transition isescalate, notact. A protocol could admit every
tool call here: protocols govern interaction boundaries, whereas RAC composes conditions across
the task.
4 Non-Compensatory Authority Transitions
Let(δ t,z t+1,η t+1) = Π(zt,o t,η t). Permission to act is
Permit(zt,o t,η t) =
[
δt =act
]
∧
(⋀
g∈Gt
[
g(zt,o t,η t) = 1
])
.(4)
The two terms address different failures:Πselects a transition, while the gate conjunction indepen-
dently vetoesact. It equals1only when every applicable gate returns1; any0or ⊥ makes Permit
false. A gate omitted as non-applicable evaluates to true only when the policy version stores its
scope and rationale.
Equation 4 differs from score-only authorization,
Permitscore(zt,o t) =1{∑ iwimi(zt,o t)<τ}, w i>0, τ >0.(5)
Here mi measures a risk signal, and the action is refused once the weighted sum reachesτ. Soft
metrics remain useful for monitoring and routing, but cannot waive a mandatory gate.
5

Table 2: Minimal hard gates and required failure transitions.
Gate Passing condition Failure transition
G_BOUNDS boundary allows action or required
review is approved
escalate/defer/stop
G_CONTEXT required context fresh and traceableretry/defer/stop
G_EVIDENCE event fields complete and source-
valid
verify/retry/stop
G_ELIGIBILITYK= 1for task/version/domainswitch/stop
G_
SUPERVISION
role, load, queue, deadline admissibledefer/stop
G_RESOLUTION no unresolved failure on action pathretry/escalate/stop
The compensatory–non-compensatory distinction is not new to this setting. Decision research has
long separated additive models, in which a high value on one attribute offsets a low value on another,
from conjunctive and lexicographic rules that screen each attribute independently [10, 36], and the
conditions under which decision makers move between the two families are well studied [16, 29].
Equation 5 is the additive member of that pair and Equation 4 the conjunctive one. What is specific
to runtime assurance is not the distinction but its consequence. In choice modeling, compensation is
a claim about preference; here the attributes are safety conditions, so compensation is the mechanism
by which a satisfied condition licenses a violated one.
Equation 5 is not a straw man. The introductory worked example in one evaluator vendor’s
documentation quarantines a message when a weighted sum of three probabilities reaches0.6, so
a credential request judged0.85probable scores0 .38alone and escapes both quarantine and the
review band beneath it [37]. The same vendor’s guardrails cookbook, by contrast, thresholds each
hazard separately and promotes a borderline probability about a serious hazard to a block through
an independent severity gate [38]. Practitioners therefore do draw the distinction, but they do not
apply it consistently, and the introductory pattern is the additive one. The failure also appears
under measurement. In a research deployment that halts every tool call an LLM monitor scores at
3/10or above until a human decides, the authors’ own red-teaming found that a hand-written fake
user turn lowered the mean score of a harmful action from8.1to3 .7, and12of30runs fell below
the threshold [24]. The claim of authority entered through the same text the score was computed
from.
After a reviewer approves,actstill requires a fresh evaluation of Equation 4 against the pinned
evidence and current policy. A reviewer leaving the queue after a completed approval does not annul
that approval; capacity is checked when review is requested, not used as an indefinite condition on
an already completed decision.
The retry budgetβt is scoped to the candidate action path and stored inzt: a recoverable
failure withβt > 0permitsretryorswitchand decrements it, and at zero onlyescalate,defer, or
stopremain. Escalation does not clear an unresolved failure; a qualified reviewer must resolve it or
assume authority under a recorded policy, and the event records the reviewer, outcome, rule version,
and reason. The same conditions select among the alternatives in Table 2.
RAC implies five invariants:
I1 — Authority separation.A learned component cannot authorize a consequential action or
alter its autonomy boundary.
I2 — Fail-closed gates.A failed or unknown mandatory gate blocksact.
I3 — Confidence asymmetry.Low confidence may reduce autonomy; high confidence does not
waive independent checks [21].
I4 — Oversight viability.Required review that misses its role, capacity, or deadline condition
6

yieldsdeferorstop, never auto-approval.
I5 — Evidence continuity.A missing transition record is an operational failure rather than a
later documentation defect.
5 Cross-Domain Failure Probes
Table 3 instantiates the same symbolic sequence in three domains: observed state, failed gate,
prohibited action, mandatory transition, and event record. The probes are illustrative. They provide
no performance measurements or cross-domain validation.
Table 3: Illustrative failure probes and mandatory transitions.
Probe Baseline state Failed gate Prohibited ac-
tion
Required tran-
sition
Persisted evidence
Stale clinical
context
benchmark
passed; call
well-formed
G_
CONTEXT commit order draft refresh and retry; else
defer
stale field, gate,
context version, δt,
reason
Judicial draft
with missing
provenance
risk score
below refusal
threshold
G_
EVIDENCE release recom- mendation verify; if policy marks high
consequence,
escalate
missing field, gate,
δt, reviewer
Operator
queue over
capacity
call permit-
ted; review
required
G_
SUPER
VISION
approve set-
point change
safe hold with
defer; elsestop
load, deadline, gate,
δt, reason
Across the three probes, a score or protocol check can remain permissive while task evidence
requires less authority. RAC’s claimed distinction is precisely this additional veto and its persisted
transition record (Eq. 3), not measured cross-domain superiority. An audit may record a failure, a
monitor may flag it, and a protocol may still admit the call; RAC requires the task-level veto and
its resulting transition record.
6 A Documented Failure
An open-source agent harness persists model-authored skills and subagent specifications across
episodes and applies refinements at turn boundaries without review. Its authors report that the
agent found an out-of-band interface bypassing the rules of its task environment, used it despite an
explicit instruction not to, and kept the bypass as reusable state that later refinement optimized
further. They conclude that safe deployment needs least-privilege action interfaces, independent
state validation and auditable rollback [19]. This is a reported incident, not a controlled evaluation of
RAC. It motivates a check of whether later authority can change without a recorded, independently
validated transition; it does not establish that the particular RAC gates proposed here would have
prevented the incident.
7

7 Evaluation
The incident in Section 6 is observational and cannot separate the decision rule from co-varying
design choices. A paired failure-injection study isolates the authorization rule on constructed cases.
We report one, narrowed to the single domain for which we have a reference implementation of
Equation 4 — agentic coding, where the consequential action is a file write proposed by a coding
agent.
7.1 Design
Every case is evaluated by all three arms, so all comparisons are paired.
• RAC.The non-compensatory conjunction of Equation 4;actonly when every applicable gate
returns1.
•Score-only.Equation 5 over the same signals:actiff ∑ iwimi<τ.
• Protocol-only.Interface permissions and repair: thedeclaredpath string is matched against
the scope and deny globs and the diff is checked for well-formedness, with no path normalization,
no symlink resolution, and no content inspection.
The three soft metrics are saturated — each takes the value1as soon as its feature is present —
which is the strongest possible reading of each detector and a deliberately charitable choice for the
baselines.
7.2 Corpus
The corpus is 174 cases: 87 injections and 87 class-matched controls across seven fault classes,
and every case is a distinct mechanism. Its provenance is deliberately split. Five classes come
from anenvelope_bypasscorpus first written in August 2026 for an unrelated purpose. Two classes
were added to include review-required cases; both were derived from a documented guard contract
rather than tuned against any arm’s behavior, and both lieinsidethe declared write scope, so the
boundary gates are silent on them and onlyG_SUPERVISIONcan reach them. Ground truth is
fixed by construction, not by adjudication, and is checked by contract tests that fail if any class
loses its gate label or if the escalation classes drift outside the declared scope.
An earlier version of this study, including arXiv v1, reported 280 cases. An internal review
found that most of them were index clones: one path listed twice, one template per class repeated
twenty times, and a single control line for every class. The corpus was rebuilt so that each case
is one mechanism with a control matched to its class. The first run on the rebuilt corpus found
seven review-required mechanisms that the guard’s contract did not cover: tests moved into helper
and data files, and module-level,unittest, import-time and collection-level silencing. The guard
was then changed by general rules, not by corpus lines. Table 4 reports both runs. The second is
in-sample: it is measured on the corpus that exposed the gaps.
7.3 Outcomes
We count unauthorized action over block-required injections, admission despite any injected gate
violation over all injections, and automatic admission of review-required injections, together with
false refusal on controls. The third quantity does not show whether an arm actually sent a request
to a reviewer; refusal alone also scores zero. The three injection counts overlap by construction: the
total admitted injections equal admitted block-required plus admitted review-required cases. The
cases are constructed mechanisms, not independent draws from a population of real changes. We
therefore report corpus counts and treat intervals and paired tests as descriptive of this corpus only.
8

Table 4: Admitted constructed cases by arm (lower is better on injected cases), before and after the
guard change described above. The score arm is shown at the published example configuration of
Section 4,w = (0.45, 0.30, 0.25), τ = 0.6, and at its best operating point chosen in hindsight over
the whole grid,w= (0.25,0.30,0.45),τ= 0.05.
Outcome Arm First run After fix Denominator
unauthorized action RAC0 063
score (vendor) 56 56 63
score (best) 0 0 63
protocol 38 38 63
admitted injections RAC 7087
score (vendor) 80 80 87
score (best) 7 0 87
protocol 62 62 87
auto-admitted review cases RAC 7024
score (vendor) 24 24 24
score (best) 7 0 24
protocol 24 24 24
false refusal RAC 3 2 87
score (vendor) 0 0 87
score (best) 3 2 87
protocol 0 0 87
7.4 Configuration dependence
At its best operating point the weighted sum matches the conjunction case for case, in both runs,
including its two false refusals: base64 text that is not a secret but fires the secret detector, which
both rules read. The conjunction removes the weights and aggregate threshold from authorization,
though engineers still have to choose, test, and scope its constituent gates. On the selected grid the
weighted sum has 114 configurations and 30 reproduce the conjunction on every case; the published
example configuration is not among them. The same 30 reproduce it before and after the guard
change and on the independent corpus below. This fraction depends on the grid and is not an
estimate of how often deployed score policies fail.
Figure 2 shows the grid result. Sweeping six weight permutations against nineteen strictly posi-
tive thresholds, agreement with the conjunction ends atτ = 0.25, the smallest weight. Proposition 1
explains that boundary for binary signals. At each threshold, the plotted permutation lexicographi-
cally minimizes unauthorized actions, admitted injections, automatically admitted review-required
cases, and false refusals, in that order. The review-admission curve therefore depends on this priority
order; it is not a bound shared by all weight permutations.
Proposition 1.Suppose wi> 0and τ >0; the risk signals are saturated,mi∈{ 0, 1}, and are the
outcomes of the same detectors the conjunction reads, so that the conjunction refuses a case iff some
mi = 1; and for each metrici the corpus contains a case that firesi alone. Then Equation 5 makes
the same decision as the conjunction on every case if and only if0<τ≤miniwi.
Proof. A case that fires no metric scores0< τ and is admitted by both rules. Ifτ≤min iwi,
any case firing at least one metric scores at leastτ and is refused, as the conjunction refuses it.
Conversely, ifτ >wj for somej, the case firingj alone scoreswj <τ and is admitted, while the
conjunction refuses it.
9

5·10 −2 0.25 0.45 0.6 0.75 0.95
0
0.25
0.5
0.75
1
agrees with
conjunction
published vendorτ
Refusal thresholdτ
Corpus fraction
unauthorized action admitted injections auto-admitted review
Figure 2: Failure rates of the score-only arm against the refusal threshold on the 174-case corpus
after the guard change, at the weight permutation selected for eachτ by lexicographically minimizing
unauthorized actions, admitted injections, automatic review admissions, and false refusals, in that
order. The shaded region, where the weighted sum agrees with the conjunction on every case, ends
exactly atτ = miniwi = 0.25on this positive grid; there both refuse the same two controls (0.023).
Automatic admission of review-required cases jumps to1.0immediately above it under this selection
rule. The published vendor threshold lies well outside.
The proposition does not require clean controls or a complete detector set: a control that fires a
detector is refused by both rules, and an injection no detector sees is admitted by both. The corpus
satisfies the hypotheses: boundary, secret, and test metrics each fire alone on some case.test-rename
is the only class whose cases can fire two metrics (0.45 + 0.25 = 0.70), which is why it is the only
class the vendor configuration catches at all, and then only 7 of its 12 cases. The interpretation
matters more than the arithmetic.0<τ≤min iwi is precisely the condition under which a single
metric suffices to refuse — that is, under which no high metric can offset a low one. The weighted
sum reproduces the conjunction exactly when it has been configured so that compensation cannot
occur on cases covered by the proposition. The equivalence says nothing about missing detectors,
continuous or noisy signals, or whether the selected hard gates are correct.
7.5 Per-class behavior
The restricted protocol-only arm refuses most ofdeny-relativeand catches a fifth ofpath-traversal,
because there the declared string itself violates a glob. It passes every symlink escape and every
embedded secret, because the declared string looks legal and it never resolves the path or reads the
content. It admits every review-required case because this baseline checks only the declared call
and diff shape. That result does not characterize all permission systems or demonstrate an actual
RAC review request.
7.6 An independently written corpus
Every case above was written by the gate’s author, and the guard was changed on the corpus that
exposed its gaps. To measure what that costs, a second corpus was written blind by OpenAI Codex
(gpt-5.5). It was given only the declared policy and a public statement of the three gates, worked in
an empty directory, and did not see the gate, the earlier corpora, or any result. The corpus was
10

Table 5: Injected cases passed by each arm on the 174-case corpus after the guard change;n is
the number of distinct mechanisms in the class. Lower is better; the required transition isblockor
humanreview. Before the change, RAC and the best score arm passed 3 of the 12test-moved-in-scope
and 4 of the 12test-skip-markermechanisms.
Class Gate Req. RAC score (vend.) score (best) protocoln
base64-secretG_EVIDENCEblock 0 12 0 12 12
deny-relativeG_BOUNDSblock 0 12 0 2 12
path-traversalG_BOUNDSblock 0 15 0 12 15
symlink-escapeG_BOUNDSblock 0 12 0 12 12
test-renameG_BOUNDSblock 0 5 0 0 12
test-moved-in-scopeG_SUPERVISIONreview 0 12 0 12 12
test-skip-markerG_SUPERVISIONreview 0 12 0 12 12
committed before its first run. It holds 124 cases: 79 injections (27G_BOUNDS, 26G_EVIDENCE,
26G_SUPERVISION) and 45 controls.
Under the corpus author’s labels, RAC admits 35 of the 79 injections and refuses 1 of the 45
controls. The best score configuration admits exactly the same cases (McNemarp = 1.0), and the
vendor configuration admits 78. Every admitted case was adjudicated:
• Two are artefacts of the harness: the diff creates a symlink, which the probe does not materialize.
With the link on disk, both are refused.
• Eleven are placeholder credentials (AKIAIOSFODNN7EXAMPLE, ghp_FAKEFAKE...) that the secret
scanner ignores by design.
• Six weaken assertions inside a test. This is outside the test guard’s contract, and the gate’s
mutation check, which is not part of this probe, would have to catch them.
That leaves 16 of 62 injections (0.26, Wilson 95% CI [0.17, 0.38]) that RAC admits within its own
detectors’ contract:
•one Unicode path that normalization maps into scope;
•seven credentials in connection URIs, configuration values, or fragments assembled across lines;
• eight test-suite silencings at collection level (conftest hooks,addopts, __test__ = False , a
renamed test class).
Two readings follow. First, the zeros of Table 4 measure the gate’s own vocabulary, not its
coverage. Second, the comparison between decision rules is unchanged. The conjunction and the
tuned weighted sum read the same detectors, so an injection no detector sees passes both, as
Proposition 1 implies. Non-compensation decides how detector outcomes are combined; it cannot
supply a detector that is missing. This corpus is in-sample for any later change to the gate.
7.7 Versioned transition conformance scenarios
The single-step corpus above does not test the persisted transitions that distinguish the full contract
from a gate conjunction. We therefore add 18 hand-authored, deterministic traces in a dependency-
free executable model supplied with the artifact. Each trace contains state updates, verification,
an optional review request and approval, and a final proposed action. Its expected transition is
declared alongside the trace. These are conformance checks of the specified policy, not independent
task observations.
The full model matches all 18 declared transitions. A stateless conjunction of the same current
gate fields matches 12; a variant that accepts verification and approval across context or policy
changes matches 13; and a variant that assumes review capacity always exists matches 16. The
11

failures identify what the stateful terms add: a changed context, rule, or payload calls for renewed
verification; an approval pinned to an older version cannot release a changed action; unavailable
review must defer. A completed approval remains valid if the reviewer later leaves the queue,
provided its pinned state has not changed. These counts describe chosen scenarios and support no
population claim.
7.8 Prospective synthetic holdout with blinded LLM labels
We added a protected-branch merge workflow to compare RAC with a full stateful baseline.
Required checks, reviews, stale-approval dismissal, and separation of reviewer from last pusher
follow documented branch-protection options [14]. The study policy additionally specifies versioned
evidence, review expiry, capacity, an action deadline, and a retry budget; these extensions are
experimental choices. Both implementations receive the same scripted CI results and review
responses. The baseline retains all these capabilities and does not import the RAC implementation.
After eight development episodes, the policy, implementations, and evaluator were frozen with
SHA-256 hashes. A separate LLM session then constructed 24 synthetic episodes containing
72 action attempts without seeing either implementation or the development cases. Two fresh
GPT-6 Sol sessions received only the policy and anonymized event histories, with no expected
labels, implementation outputs, or other judge’s answers. Each labeled every attempt as allow,
review, block, or insufficient information and supplied a rationale. The policy, protocol, and judge
instructions were written in Ukrainian, and the judges wrote their rationales in Ukrainian; the
public repository provides English translations. Both label files were frozen before the test run.
This was a local prospective freeze, not an externally registered protocol; access restrictions were
instructional on a shared filesystem. No test-driven implementation changes were made.
The judges agreed on all 72 attempts: 30 allow, 30 review, and 12 block, with no insufficient-
information labels. RAC and the full stateful baseline each matched all 72 labels. Each produced
zero policy-violating simulated releases among the 42 non-allow attempts and zero false refusals
among the 30 allow attempts. Both recorded 28 review requests, 25 completed reviews, five invalid
review events, 30 simulated releases, and two consumed retries. Mean delay for the 25 completed
reviews was 1.84 simulated ticks; unfinished requests do not enter this mean. Four attempts stopped
and none deferred. Thus the holdout does not test the unavailable-review deferral branch, despite
containing capacity changes.
The result is observed agreement under a shared policy, with no advantage for RAC over the
full stateful baseline. The judges belong to the same model family, and the corpus is LLM-authored;
agreement does not establish an independent domain oracle. This is a holdout from implementation
development, not from the supplied specification. Its labels concern synthetic merge authority, not
the truth of CI outputs or the safety of actual patches.
7.9 Instruments, determinism, and reproducibility
The original probe implementation, escalation corpus, and contract tests were written with an AI
coding assistant (Claude Code, Claude Opus 5) under the author’s direction; the assistant also
executed the runs and generated the original tables and figure from the raw decision log. The
transition scenario model and the 2026-09 revision were prepared with OpenAI Codex. The October
2026 correction (the mechanism corpus, the independent-corpus run and its adjudication) was
prepared with Claude Code (Claude Opus 5.5); the independent corpus itself was written by OpenAI
Codex (gpt-5.5), as described above. Earlier drafting and language revision used OpenAI Codex
CLI 0.144.5 and PaperMentor 0.1.0. No model call occurs when replaying the static or transition
12

artifacts. The new holdout uses LLM calls for corpus construction and labeling, then deterministic
replay against the saved labels. The executable artifact generates the reported counts; replay
does not reproduce the stochastic judge calls. Exact model snapshots and sampling parameters
for the judging sessions were unavailable. The public code supplement athttps://github.com/
SZabolotnii/TRACE-RAC-code-supplement contains the standalone implementations and data for
the new LLM-labeled holdout. The private gate implementation and fixture generator used for
the original probe are not distributed; that probe cannot be independently rerun from the public
supplement.
The original probe run is deterministic: no sampling, no seeds beyond corpus construction,
and no model call on the evaluation path. It was reproduced byte-identically in two independent
Python environments. Two harness defects found by the first run are recorded here because they
are characteristic of this design. First, the symlink-escape fixture stores its path absolutely, which
the envelope requires in order to resolve it on disk; the protocol arm saw the absolute string, failed
the scope glob, and refused — appearing to catch the escape for a reason that cannot arise in a real
tool call. The arm now receives the path in the form the agent declares it, after which it passes
every symlink escape, as it should. Second, the first run measured the score arm only at the vendor
point, from which the weighted sum appeared unconditionally worse; the grid sweep overturned
that reading and produced the actual result. Both were fixed before any number here was treated
as a finding.
7.10 Threats to validity
This is a mechanism study, not a safety result, and eight limits bound it.
Circularity.The RAC arm is an implementation of the gate set this paper posits. The study
shows that the set is implementable and identifies when competing decision rules on identical
inputs reproduce it. It does not show that the set is correct; no independent oracle defines the
right gates.
Authored traces.The 18 transition traces and expected outcomes were hand-authored for contract
conformance. Their agreement with the executable model is a consistency check, not a measured
reliability rate.
LLM-labeled holdout.Separate sessions hide implementation outputs from the judges, but a
shared policy and model family can produce correlated errors. The 24 new episodes do not
establish independent human domain validation. The full stateful baseline implements the same
policy and matches RAC; the holdout provides no evidence of architectural superiority.
Single synthetic domain.The clinical, industrial, and judicial probes of Section 5 remain
illustrative. Nothing here supports the cross-domain claim.
Noisy signals.The signals are binary. Proposition 1 covers detectors that miss faults or fire on
clean actions only in the sense that both rules inherit the error; it does not predict behavior with
continuous or noisy scores.
Over-blocking is a corpus property.Two of 87 constructed controls are refused. This says
nothing about whether fail-closed is cheap. The operational cost of refusal — latency, reviewer
queueing, denied service — is not measured in deployment. The holdout records scripted queue
values and simulated completion delays, which do not estimate these costs.
In-sample guard.The guard was changed on the corpus that exposed its gaps. The zeros after
that change are in-sample. The independently written corpus measures out-of-sample admission,
16 of 62 within contract. Each mechanism there is a single case, not a draw from a population of
real changes.
Limited rerunnability.The shared static decision log permits a count audit, not reconstruction of
13

the private gate and its input fixtures. The transition model and the new holdout are executable
but are separate synthetic implementations, not a rerun of the original private gate.
Establishing added value in deployment therefore still requires a domain study: consequential
actions in versioned task traces, labeled before injection by two qualified reviewers under a frozen
codebook, with one prespecified fault injected into paired copies under a recorded seed, balanced
within domain and consequence strata, compared with a stateful baseline that has the same detectors.
Its outcomes should include actual review requests, completed decisions, harmful releases, false
refusals, and service delay. Deployment-specific harm analysis must set the effect margins before
data collection; this paper claims none.
8 Limits and Ethics
RAC is a design proposition. It does not prove system safety, validate the underlying boundary,
calibrate model confidence, or remove domain-specific threshold setting; accountable owners must
derive gates from risk analysis and applicable duties. A fail-closed policy can itself cause harm
through delayed care, denied service, downtime, or unequal access to scarce reviewers, and evidence
logs may expose sensitive data. Implementations therefore need service limits, safe fallback ownership,
least-privilege logging, and retention controls.G_SUPERVISIONis a minimum viability condition,
not a complete account of meaningful human oversight.
Evaluators that return probabilities without a rationale are hard to justify in regulated domains
when their outputs are summed, because the scalar does not say which condition drove a refusal.
Under Equation 4 a refusal is recorded as the identity of the gate that returned false. This recovers
which condition failed, not why the model judged it so.
9 Conclusion
RAC specifies how gate outcomes, versioned evidence, and human review govern the next authority
transition. For binary signals, a weighted risk sum makes the same decision as the gate conjunction
on every case exactly when its positive refusal threshold is no greater than the smallest positive
weight; the published example threshold falls outside that range. On a corpus written independently
of the gate, both rules admit about a quarter of the injections within contract, because the gaps are
in the detectors and not in the rule of decision. The versioned trace checks expose the additional
state that a stateless conjunction does not retain. On the prospective LLM-labeled synthetic holdout,
a full stateful baseline matches RAC. These are analytic and synthetic results. Whether the contract
improves decisions in deployed systems with noisy detectors and real review queues remains open.
Supplementary Material
The accompanying supplementary archive contains a field-limited decision log, its count-audit
script, the executable transition scenarios, and a copy of the public holdout repository. The public
repository https://github.com/SZabolotnii/TRACE-RAC-code-supplement contains the policy,
separately written implementations, development and test episodes, blinded judge labels with
rationales, freeze manifests, and simulated execution logs for the LLM-labeled holdout. It supports
rechecking those counts and policy-model outputs, subject to the rerunnability limits described
above. It does not include the private gate implementation or fixture generator used for the original
probe.
14

References
[1] A2A Protocol Working Group. A2A Protocol Specification, Version 1.0.0. https://
a2a-protocol.org/v1.0.0/specification/, 2026. Accessed 2026-07-17.
[2] Rasmus Adler and Michael Kläs. Assurance Cases as Foundation Stone for Auditing AI-Enabled
and Autonomous Systems: Workshop Results and Political Recommendations for Action from
the ExamAI Project, 2022. URLhttps://arxiv.org/abs/2208.08198. arXiv:2208.08198.
[3] Mohammed Alshiekh, Roderick Bloem, Rüdiger Ehlers, Bettina Könighofer, Scott Niekum, and
Ufuk Topcu. Safe Reinforcement Learning via Shielding. InProceedings of the Thirty-Second
AAAI Conference on Artificial Intelligence, volume 32, pages 2669–2678, Palo Alto, CA, USA,
2018. AAAI Press. doi: 10.1609/aaai.v32i1.11797.
[4] Radu Calinescu, Danny Weyns, Simos Gerasimou, Muhammad Usman Iftikhar, Ibrahim Habli,
and Tim Kelly. Engineering Trustworthy Self-Adaptive Software with Dynamic Assurance
Cases.IEEE Transactions on Software Engineering, 44(11):1039–1069, 2018. doi: 10.1109/
TSE.2017.2738640.
[5] Javier Cámara, Gabriel Moreno, and David Garlan. Reasoning about Human Participation
in Self-Adaptive Systems. In2015 IEEE/ACM 10th International Symposium on Software
Engineering for Adaptive and Self-Managing Systems (SEAMS), pages 146–156, Florence, Italy,
2015. IEEE. doi: 10.1109/SEAMS.2015.14.
[6] Yen-Shan Chen, Sian-Yao Huang, Cheng-Lin Yang, and Yun-Nung Chen. TraceSafe: A
Systematic Assessment of LLM Guardrails on Multi-Step Tool-Calling Trajectories, 2026.
arXiv:2604.07223.
[7] Ankush Desai, Shromona Ghosh, Sanjit A. Seshia, Natarajan Shankar, and Ashish Tiwari.
SOTER: A Runtime Assurance Framework for Programming Safe Robotics Systems. In49th
Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN),
pages 138–150, Portland, OR, USA, 2019. IEEE. doi: 10.1109/DSN.2019.00027.
[8] Yi Dong, Wenjie Huang, Vikas Bharti, Victoria Cox, Alec Banks, Sen Wang, Xingyu Zhao,
Sven Schewe, and Xiaowei Huang. Reliability Assessment and Safety Arguments for Machine
Learning Components in System Assurance.ACM Transactions on Embedded Computing
Systems, 22(3):39:1–39:48, 2023. doi: 10.1145/3570918.
[9] Aarya Doshi, Yining Hong, Congying Xu, Eunsuk Kang, Alexandros Kapravelos, and Christian
Kästner. Towards Verifiably Safe Tool Use for LLM Agents, 2026. arXiv:2601.08012.
[10] Hillel J. Einhorn. The use of nonlinear, noncompensatory models in decision making.Psycho-
logical Bulletin, 73:221–230, 1970. doi: 10.1037/h0028695.
[11] European Parliament and Council of the European Union. Regulation (EU) 2024/1689 of 13
June 2024 laying down harmonised rules on artificial intelligence (AI Act). Official Journal of
the European Union, L 2024/1689, 12 July 2024, 2024. URLhttp://data.europa.eu/eli/
reg/2024/1689/oj.
[12] Yonatan Geifman and Ran El-Yaniv. Selective Classification for Deep Neural Networks. In
Advances in Neural Information Processing Systems 30, volume 30, Long Beach, CA, USA,
2017. Curran Associates, Inc. URLhttps://arxiv.org/abs/1705.08500.
15

[13] Yonatan Geifman and Ran El-Yaniv. SelectiveNet: A Deep Neural Network with an Integrated
Reject Option. InProceedings of the 36th International Conference on Machine Learning,
volume 97 ofPMLR, pages 2151–2159, Long Beach, CA, USA, 2019. PMLR. URLhttps:
//proceedings.mlr.press/v97/geifman19a.html.
[14] GitHub. About protected branches. GitHub Docs, https://docs.github.
com/en/repositories/configuring-branches-and-merges-in-your-repository/
managing-protected-branches/about-protected-branches, 2026. Accessed 23 September
2026.
[15] Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger. On Calibration of Modern Neural
Networks. InProceedings of the 34th International Conference on Machine Learning, volume 70
ofProceedings of Machine Learning Research, pages 1321–1330, Sydney, Australia, 2017. PMLR.
URLhttps://proceedings.mlr.press/v70/guo17a.html.
[16] John R. Hauser. Consideration-set heuristics.Journal of Business Research, 67:1688–1699,
2014. doi: 10.1016/j.jbusres.2014.02.015.
[17] Richard Hawkins, Colin Paterson, Chiara Picardi, Yan Jia, Radu Calinescu, and Ibrahim Habli.
Guidance on the Assurance of Machine Learning in Autonomous Systems (AMLAS), 2021.
URLhttps://arxiv.org/abs/2102.01564. arXiv:2102.01564.
[18] Nils Jansen, Bettina Könighofer, Sebastian Junges, Alexandru C. Serban, and Roderick Bloem.
Safe Reinforcement Learning via Probabilistic Shields, 2018. arXiv:1807.06096.
[19] Seth Karten, Alex L. Zhang, Kevin Thomas, Sebastian Müller, Elie Bakouch, Daniel Auras,
Mika Senghaas, Fares Obeid, Konstantin Dunas, Johannes Hagemann, and Sami Jaghouar.
Prime Agent: A Self-Improving RLM Harness, 2026. arXiv:2608.23552.
[20] Jeffrey O. Kephart and David M. Chess. The Vision of Autonomic Computing.Computer, 36
(1):41–50, 2003. doi: 10.1109/MC.2003.1160055.
[21] Yubin Kim, Hyewon Jeong, Chanwoo Park, Eugene Park, Haipeng Zhang, Xin Liu, Hyeonhoon
Lee, Daniel McDuff, Marzyeh Ghassemi, Cynthia Breazeal, Samir Tulebaev, and Hae Won
Park. Tiered Agentic Oversight: A Hierarchical Multi-Agent System for Healthcare Safety,
2025. URLhttps://arxiv.org/abs/2506.12482. arXiv:2506.12482.
[22] Bettina Könighofer, Julian Rudolf, Alexander Palmisano, Martin Tappler, and Roderick Bloem.
Online Shielding for Stochastic Systems, 2020. arXiv:2012.09539.
[23] Bettina Könighofer, Roderick Bloem, Rüdiger Ehlers, and Christian Pek. Correct-by-
Construction Runtime Enforcement in AI – A Survey, 2022. arXiv:2208.14426.
[24] METR. Implementing a Basic Blocking Action Monitor. Re-
search note, 27 September 2026, https://metr.org/notes/
2026-09-27-implementing-a-basic-blocking-action-monitor/ , 2026. Accessed 5
October 2026.
[25] Model Context Protocol. Model Context Protocol Specification, Version 2025-06-18.https:
//modelcontextprotocol.io/specification/2025-06-18, 2025. Accessed 2026-07-16.
16

[26] Gabriel A. Moreno, Javier Cámara, David Garlan, and Bradley Schmerl. Flexible and Effi-
cient Decision-Making for Proactive Latency-Aware Self-Adaptation.ACM Transactions on
Autonomous and Adaptive Systems, 13(1), 2018. doi: 10.1145/3149180.
[27] Yutao Mou, Zhangchi Xue, Lijun Li, Peiyang Liu, Shikun Zhang, Wei Ye, et al. ToolSafe:
Enhancing Tool Invocation Safety of LLM-based agents via Proactive Step-level Guardrail and
Feedback, 2026. arXiv:2601.10156.
[28] Christophe Parisel. A Theory of Least Autonomy in AI, 2026. arXiv:2607.09744.
[29] John W. Payne, James R. Bettman, and Eric J. Johnson.The Adaptive Decision Maker.
Cambridge University Press, Cambridge, UK, 1993. doi: 10.1017/cbo9781139173933.
[30] Stefan Pranger and Bettina Könighofer. Easy-to-Use Shielding for Reinforcement Learning,
2026. arXiv:2606.03804.
[31] Danbing Seto, Bruce Krogh, Lui Sha, and Alongkrit Chutinan. The Simplex Architecture for
Safe Online Control System Upgrades. InProceedings of the 1998 American Control Conference,
volume 6, pages 3504–3508, Philadelphia, PA, USA, 1998. IEEE. doi: 10.1109/ACC.1998.703255.
[32] Lui Sha. Using Simplicity to Control Complexity.IEEE Software, 18(4):20–28, 2001. doi:
10.1109/MS.2001.936213.
[33] Tanush Sharanarthi and Sreenidhi Polineni. Agents Need Protocols, Not API Wrappers.ACM
AI Letters, 2026. doi: 10.1145/3830910. Online first, 13 July 2026; volume and article number
not yet assigned.
[34] Aman Sharma. Proxy-Based Evaluation and the Limits of Assurance in AI Governance.ACM
AI Letters, 1(3), 2026. doi: 10.1145/3828672.
[35] Tianneng Shi, Jingxuan He, Zhun Wang, Hongwei Li, Linyu Wu, Wenbo Guo, et al. Progent:
Securing AI Agents with Privilege Control, 2025. arXiv:2504.11703.
[36] Amos Tversky. Elimination by aspects: A theory of choice.Psychological Review, 79:281–299,
1972. doi: 10.1037/h0032955.
[37] TypeSafe. System One Documentation: How to Build with TypeSafe, and Confidence. Vendor
documentation, https://docs.typesafe.ai/concepts/how-to-build-with-system-one
andhttps://docs.typesafe.ai/confidence, 2026. Accessed 17 September 2026.
[38] TypeSafe. Cookbook: LLM Guardrails. Vendor documentation,https://docs.typesafe.ai/
cookbooks/llm_guardrails, 2026. Accessed 22 September 2026.
[39] Tim Weninger. AI Ethics Must Speak the Language of Business.ACM AI Letters, 1(2), June
2026. doi: 10.1145/3805709.
[40] Danny Weyns.An Introduction to Self-adaptive Systems: A Contemporary Software Engineering
Perspective. Wiley, Hoboken, NJ, USA, 2020. doi: 10.1002/9781119574910.
[41] Zhen Xiang, Linzhi Zheng, Yanjie Li, Junyuan Hong, Qinbin Li, Han Xie, et al. GuardA-
gent: Safeguard LLM Agents by a Guard Agent via Knowledge-Enabled Reasoning, 2024.
arXiv:2406.09187.
17

[42] Zheng Yan, Jingxiang Weng, Charles Chen, Dengyun Peng, Ethan Qin, Jiannan Guan, et al.
Do Coding Agents Understand Least-Privilege Authorization?, 2026. arXiv:2605.14859.
[43] Serhii Zabolotnii. TRACE: A Metrologically-Grounded Engineering Framework for Trustworthy
Agentic AI Systems in Operationally Critical Domains, 2026. URLhttps://arxiv.org/abs/
2605.03838. arXiv:2605.03838.
[44] Jinhao Zhu, Kevin Tseng, Gil Vernik, Xiao Huang, Shishir G. Patil, Vivian Fang, et al. MiniS-
cope: A Least Privilege Framework for Authorizing Tool Calling Agents, 2025. arXiv:2512.11147.
18
