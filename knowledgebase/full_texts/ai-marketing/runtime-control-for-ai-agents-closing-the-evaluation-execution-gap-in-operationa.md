---
title: 'Runtime Control for AI Agents: Closing the Evaluation--Execution Gap in Operational Workflows'
url: https://arxiv.org/abs/2610.27480
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Jayesh Bhadane
- Ramachandra Yerramsetti
- Rajesh Gupta
- Sumit Kumar
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.27480
pages: 8
chars: 44512
fetched_at: '2026-11-08T13:33:21+00:00'
kb_version: 1
---

# Runtime Control for AI Agents: Closing the Evaluation--Execution Gap in Operational Workflows

1
Runtime Control for AI Agents: Closing the
Evaluation–Execution Gap in Operational Workflows
Jayesh Bhadane Ramachandra Y erramsetti Rajesh Gupta Sumit Kumar
jayesh@runctrl.ai rcyerramsetti@protonmail.com rajesh@runctrl.ai sumit.mamoria@gmail.com
Abstract—Language-model agents increasingly participate in
operational workflows where approvals, binds, and payments
create commitments. An approval valid when issued may no
longer authorize execution after relevant facts, evidence, policy,
or authority change. We call this the evaluation–execution gap.
We specify a state-bound runtime assurance layer that separates
probabilistic measurement from deterministic adjudication, binds
an execution allowance to the decision-relevant basis of an
approval, invalidates that allowance after relevant logged changes,
and rechecks admissibility at dispatch. This distinguishes the
continued validity of a prior approval from a current-state
policy check. We describe eight failure modes, an assurance
model, a reference architecture, and prospective interventions
with retrospective remediation. In a scripted 42-case replay, the
state-bound configuration identifies 15 later-invalidated approvals
that a deliberately non-re-evaluating point-in-time comparator
does not revisit; it holds 14 affected actions before dispatch
and compensates one landed effect. These results illustrate
behavior under the stipulated policies and event orders, not
superiority over dispatch-time enforcement designs or production
effectiveness. Under explicit interception, ingestion, dependency,
and serialization assumptions, the model establishes dispatch-time
validity within the registered execution surface.
I. Introduction
Language-model agents plan, call tools, and act across
long interactions. τ -bench studies tool-agent-user work in real-
world domains [1]. Safety, robustness, and compliance remain
open as actions need constraint, observation, attribution, and
interruption.
In claims, underwriting, lending, payments, and benefits, an
approval, bind, release, or decision creates an obligation. It
must remain valid when it takes effect.
Consider a claims agent that may approve payouts below
$5,000 without senior review. It approves a claim at$4,800.
Before payment, a revised estimate raises the loss to$7,200
and requires senior approval. The first approval was valid, but
the case changed. If payment uses it, the decision is stale.
Agent evaluation assesses agent behavior [2]. Agent ob-
servability traces execution artifacts and decisions [3]. In this
paper, both supply measurement inputs. Runtime enforcement
can constrain a proposed action [4]. We add a controller that
decides whether an earlier approval remains valid after facts,
evidence, policy, or authority change.
We ask how an action can remain valid at execution after
case, evidence, policy, or authority change. Our stateful decision
runs before each action and after relevant change. It draws
on runtime assurance and runtime verification [5], [6] and
applies them to business commitments. The contributions are
an eight-mode taxonomy (Section IV), a five-property decision
(Section V), an architecture with adjudication, invalidation,
dispatch validity, and replay (Section VI), seven interventions
(Section VII), and a 42-case baseline comparison (Section VIII).
This specification paper positions the layer in Section II,
develops the examples in Section III, and states limits in
Section IX.
II. Background and Related Work
Measurement.Agent evaluation assesses multi-step be-
havior [2], while agent observability traces the artifacts and
decisions behind that behavior [3]. At dispatch, the controller
compares the approval record with the current case to decide
whether the approval still applies.
Runtime and process control.Runtime verification, se-
curity automata, edit automata, and runtime assurance check
or constrain execution [5]–[8]. Compliance monitoring and
commitments reason over processes and obligations [9], [10].
A conformant trace can still carry an approval the case has
outgrown.
Governance and access.Delegation can supply logged
identity, authority, and audit data [11]. Attribute-based ac-
cess control decides whether a principal may invoke an
operation [12]. UCON adds mutable conditions and ongoing
checks [13]. Y et live permission to invoke bind policy
can remain while the decision to bind this case becomes invalid.
Transactions and rules.Optimistic concurrency control
validates a read set [14]. Our business read set can span
facts, approvals, policy, and days. Policy-as-code evaluates
an arriving request, not an earlier approval. Table I shows the
missing combination: a state-bound business decision that is
re-evaluated and enforced at dispatch.
III. The Evaluation–Execution Gap
Evaluation estimates risk. It does not decide whether an
action should proceed under state, policy, authority, and
reversibility.
A. Why the gap is structural
The gap is structural because approval, case change, and
dispatch occur at different times. A point-in-time layer can
judge the case at approval, but does not retain the facts, policy,
evidence, and authority behind that decision. After a case
changes, it cannot compare the old approval with the current
case. At dispatch, an enforcement output cannot repair this
missing history. A controller must retain the decision basis,
arXiv:2610.27480v1  [cs.AI]  20 Oct 2026

2
TABLE I
Relationship to prior mechanisms and the proposed state-bound decision-validity model.
Established approach Existing capabilities Design emphasis in this paper
Agent evaluation and observability
[2], [3]
Behavioral evaluation, execution traces, and recorded
assessments
Treat assessments as recorded inputs, not independently
sufficient authorization for execution
Runtime enforcement and
verification [4]–[8]
Runtime policy checks, temporal monitoring, and action
constraints
Track the validity of a specific prior approval and
invalidate its allowance after relevant state changes
Access and usage control [11]–[13] Identity, delegation, contextual authorization, and
mutable permissions
Separate endpoint permission from the standing associated
with a specific recorded business approval
Process compliance and transaction
control [9], [10], [14]
Process obligations, commitment models, and read-set
validation
Bind approval history, evidence, decision dependencies,
and rule versions to a long-lived execution allowance
re-evaluate it after relevant change, and, unlike probabilistic
measurement, make a deterministic, reproducible, inspectable,
and defensible intervention.
Runtime assuranceadjudicates each consequential action
against current state before effect.Runtime controlis our
deterministic layer. It maps upstream signals, state, policy,
authority, evidence, and reversibility to one intervention.
B. Two running examples
Claim payout.The$4,800 approval is valid under the
specified$5,000 rule. The later$7,200 estimate invalidates
its use for the payment. A dispatch-time threshold check
would detect the amount increase; a state-bound allowance
also records that the earlier approval was issued under different
case conditions and must not be silently reused.
Commercial-property submission 8871.For this illustrative
workflow, the declared underwriting rules require a senior sign-
off at$8.2M total insured value and independent retention of
every materially relevant guideline exception. A parser records
three separately identified guideline exceptions. The agent
compresses them into “one material issue” without a recorded,
authorized consolidation decision and recommends binding. A
junior underwriter approves from that summary despite lacking
the standing required by the exposure rule. In the sequence
below, a senior underwriter then reviews the three separately
recorded exceptions, resolves the unsupported summary, and
issues a valid approval on that case state. Before binding, an
inspection vendor reports a fourth exception. The example
separates three questions: whether the agent’s summary is
supported, whether the reviewer had standing, and whether
even a properly issued prior approval would remain valid after
the new inspection. Table II traces the submission across these
positions, contrasting what the control layer retains with what
a point-in-time view sees.
IV . A Taxonomy of Operational Workflow Failures
The examples above show stale decisions, missing standing,
and unsupported assessments. The taxonomy names these
and related implementation-independent failures in obligations,
authority, evidence, and commitments. Later sections map each
mode to detection and response.
A. Workflows, commitments, and failure
Anoperational workflowis a finite sequence of actor-
performed steps with inputs, obligations, invariants, and suc-
cessors. Obligations require standing and createcommitments
that may be reversible, compensable, or irreversible. Cases
can change while open. Anoperational failureviolates an
invariant by action, commitment, or lack of progress, even
without malfunction.
B. Classification
Each mode has a locus, surfacing horizon, and commitment
reversibility. The locus can be evidence, authority, temporal
validity, rules, record truthfulness, or boundary. It may surface
during a step, later, or after an external trigger. Handoffs can
delay detection because the next actor receives a summary.
Reversibility sets response strictness.
C. The failure modes
F1: Unauthorized commitment.An approval lacks state-
dependent business standing, despite tool permission. On 8871,
the junior underwriter lacks senior standing. It may surface at
audit and is irreversible.
F2: Stale-decision execution.A valid decision is invalidated
by later case change before execution. Agents may execute
against it rather than re-read the file. The claims payout is F2.
F3: Incomplete-evidence discharge.A step proceeds before
policy-required facts are present. Agents need absence enforced
as a block. A bind on 8871 before a signed statement of values
is F3. It can surface at claim time and be irreversible.
F4: Ungrounded discharge.Facts and authority may
exist, while the assessment does not follow from facts. The
layer detects recorded contradiction, missing support, or a
groundedness threshold. It cannot decide whether a supported
assessment is substantively wrong (Section IX). On 8871,one
material issuecontradicts three exceptions. The layer preserves
the recorded facts and treats the assessment as a separate
assertion.
F5: Prohibited commitment.No actor may make the
commitment, so escalation cannot cure it. A bind in an unfiled
class is F5 and may surface at regulatory examination.
F6: Inconsistent-rule adjudication.The governing policy
version or its case applicability is not determinate. Effective
dates, transitions, and case conditions matter. A transition
assigning a case to neither version is F6.
F7: Narrative capture.A summary or recommendation
replaces the facts it describes, or is stored as if it were a fact.
If 8871 kept onlyone material issueand dropped the three
extracted exceptions, the controller could no longer compare the

3
TABLE II
A state-bound decision across the 8871 underwriting workflow: what the control layer retains versus what a point-in-time view sees.
Step Workflow event State retained by control layer Point-in-time view Runtime-control consequence
t0 Parser extracts three guideline
exceptions
Three facts enter the record with source
provenance
Extraction completes Facts are available to future obligations
t1 Agent writes “one material issue;
recommend bind”
Narrative retained as an assertion, not a
replacement for three facts
Summary can appear plausible in
isolation
Recorded contradiction can trigger monitoring
or escalation (F4)
t2 Junior underwriter approves Approval records actor, policy version, and
current state
Review exists; user has tool access Authority fails for$8.2M exposure; route to
senior authority (F1)
t3 Senior reviews the three
exceptions, resolves the summary,
and approves
V alid approval supports an allowance bound
to that case state
Approval is now present Binding may proceed only while allowance
dependencies remain unchanged
t4 Inspection vendor reports a fourth
exception
New fact changes variable read by binding
obligations
Earlier senior approval still exists Old allowance invalidated (F2)
t5 Agent proposesbind policyCurrent state includes four exceptions and
allowance bound at t3
Tool guard sees valid call plus
approval
Re-adjudicate before dispatch; withhold
binding until conditions are met
summary with the facts. When information enters the system,
source typing keeps facts, assertions, and decisions separate.
F8: Governance bypass.A commitment uses an ungoverned
database edit, payment rail, or override. No layer can intervene
on what it never sees. F8 therefore lies outside the model’s
prevention guarantee.
D. Two tiers, exhaustiveness, and scope
F1–F6 areadjudication failures. The controller can see the
proposed action and case record, then choose a response. F7–F8
arestructural failures. In F7, the record needed for a decision
has been replaced or made unreliable. In F8, the action happens
outside the controller’s view.
The taxonomy is exhaustive only for the workflow step
described in this paper. Within that boundary, a failure concerns
missing input, an unsupported assessment, authority, an old
decision, policy, record integrity, or a bypassed boundary. It
does not cover infrastructure faults, attacks, or obligations that
policy never encoded. An attack may still appear as F1–F7 if
it changes a visible record, authority, or decision.
V . The Runtime Assurance Model
F1–F6 are adjudicated when a governed action reaches the
controller. A governed action is consequential, registered in
the manifest, and routed through the controller. F2 can arise
after a later event. The controller rebuilds the case, evaluates
the action against current records, and returns one intervention.
This section defines that protocol and its limited guarantee.
A. The assurance decision
The assurance decision, called D, answers one question: may
this action proceed in the case as it stands now? D checks the
proposed action against current case facts, applicable policy,
the actor’s authority, evidence, and reversibility. It returns one
intervention. The controller records its reasons and returns
the outcome to the agentic workflow, whose registered action
connector enforces it.
Consider the claims payout introduced earlier. The agent
approved$4,800 under a rule that permits approval below
$5,000 without senior review. Before sending payment, the
controller rebuilds the case from its initial state and ordered
event log. The log is append-only: new events are added, and
earlier events remain available. Reconstruction uses recorded
events and preserved procedures, without a new model call or
external lookup.
D needs more than the amount. It checks the approval,
the actor’s authority, required evidence, the governing policy
version, and whether payment can be reversed or compensated.
If all requirements hold, it returns allow. The controller stores
the action, case, actor, log position, outcome, and every input
used. These inputs form thedecision read set. Each entry
identifies the fact or governing artifact, its observed value, and
its applicable version. This includes thresholds, authority and
registry rules, prior decisions, deadlines, and effective dates. D
uses only the action and this complete set of recorded inputs.
Now the revised estimate of$7,200 arrives before payment.
Ingestion adds it to the log. The amount is an input to the earlier
decision, so the controller marks that decision stale and runs D
again. The new amount requires senior review. The controller
therefore returns escalate; the agentic workflow holds
payment and routes the claim for review. It records the senior
review when it arrives and checks all current requirements
again before returning an allowance.
An unrelated event leaves the decision standing. A change
to a recorded input, governing version, or version-applicability
condition requires another decision. An expiry must enter the
log before a later action that depends on it. Restoring an earlier
value cannot revive the old decision, because the intervening
change remains in the log. A digest identifies the decision
for audit. The recorded inputs and subsequent events establish
whether it remains current.
This separates anapproval, a recorded decision by a person
or an authorized agent, from anallowance, the controller’s
permission to proceed. The runtime returns its outcome and
allowance to the agentic workflow. Immediately before its
registered action connector invokes a target, it checks with the
controller that the allowance remains current. A stale decision
triggers re-evaluation and the connector holds the action. The
final check and invocation must be serialized with incoming
events, so no relevant change can enter between them.
D returns one of seven interventions. allow permits
execution. monitor permits reversible or compensable work
under observation. require evidence names missing
facts. escalate routes to a reviewer. pause waits for a

4
TABLE III
Operational failure modes and their runtime images.
Mode Locus Surfacing Commitment Intervention
F1 Unauthorized
commitment
authority audit irreversibleescalate
F2 Stale-decision execution temporal validity downstream / never irreversiblerollback
F3 Incomplete-evidence
discharge
evidence claim time irreversiblerequire evidence
F4 Ungrounded discharge assessment downstream / audit variesmonitor/escalate
F5 Prohibited commitment governing rules regulatory exam irreversibledeny
F6 Inconsistent-rule
adjudication
rule identity audit variespause
F7 Narrative capture veracity of record pervasive varies structural (Sec. VI)
F8 Governance bypass process boundary never irreversible excluded (Sec. VI)
TABLE IV
Evidence properties the layer can establish.
Property Runtime layer
Completeness establishes presence against declared requirements
(F3)
Provenance establishes source attribution from ingestion typing
Consistency establishes agreement against recorded facts (F4)
Substantive correctness cannot establish. Escalates
condition to be resolved. deny refuses the action. After an
earlier reversible or compensable effect has landed, rollback
directs recovery. It does not authorize the original action.
Table V maps deficiencies and reversibility to these outcomes.
B. The inputs
Case state and action.Case state contains the recorded
facts, documents, decisions, and signals. In the payout example,
it includes both estimates and the approval history. The
action registry identifies the proposed operation and target
as consequential.
Policy and authority.V ersioned policy contains conditions,
authority, evidence, and permitted actions. The controller selects
a version only when its date, transition rule, case scope, and
action scope fit. Otherwise the case is F6. An API right is
not business standing. The authority check asks whether this
actor may make this action for this case. It can depend on
exposure, jurisdiction, product, delegation, and duty separation.
Thus 8871’s junior underwriter has access but not standing.
Evidence.Completeness checks required facts and detects F3.
Provenance records source. Consistency compares assertions
with recorded facts and detects F4 by contradiction or missing
support. The layer cannot decide substantive correctness, so it
routes that question.
Reversibilityis declared in the action registry as reversible,
compensable, or irreversible. It detects no mode. It sets
strictness, so doubt that permits monitoring for a reversible
action can require escalation for an irreversible one.
C. Properties
Determinism.The same log prefix, action, decision-read-set
values, and pinned governance-artifact versions give the same
state and intervention. Signals enter only as logged values and
thresholds.
Separation of adjudication from extraction.Parsers,
evaluators, and people resolve unstructured material first. The
decision makes no hidden model call.
Risk-to-intervention translation.Groundedness concern
maps to monitor for reversible work and escalate for
irreversible work.
Reversibility-conditioned strictness.Residual uncertainty
needs stronger control before an irreversible commitment.
Temporal re-evaluation.A change to a recorded input,
pinned version, or version-applicability condition triggers a
new decision. This is why the$7,200 revision stops payment
under the earlier allowance.
VI. Reference Architecture
The architecture comprises a manifest, interception boundary,
typed log, reconstruction, engine, and controller. Figure 1 shows
the agentic layer receiving claim documents and running the
agent workflow. The agent sends evidence references and a
proposed action to runtime Ingest; the runtime records and
adjudicates them, then returns an outcome to the agentic layer.
In submission 8871, the inspection vendor’s fourth exception
arrives through the case workflow and is forwarded to Ingest.
Because it changes a dependency of the pending binding
decision, the runtime invalidates the old allowance and returns
a hold or escalation. If an action is allowed, the registered
action connector invokes it only after a current-allowance check.
The runtime returns authorization to the agentic layer; it does
not directly send the action to the enterprise target. Execution
results return to the agentic layer and are forwarded to Ingest
as logged events.
A. Interception
The manifest registers each record mutation, its reversibility,
and external binding. Running clearance is internal and
reversible. Binding is external and irreversible. An engineer,
not the agent, owns the manifest.

5
Runtime control layer
1. Ingest
Type and record
evidence, proposals,
updates
2. Reconstruct
Replay ordered log
Build current
case state
3. Adjudicate
Apply policy, evidence,
authority and
dependencies
4. Control
Return outcome
to agentic layer
Validate allowance
at tool call
Typed log
Documents, assertions,
proposals, decisions,
updates
Governance inputs
Claim rules, evidence needs,
agent authority,
action registry
Temporal validity
Track allowance dependencies
Relevant change invalidates it
replay
append
relevant logged update
validity check
re-adjudicate
record decision / outcome
Agentic layer
Receives portal documents and claim updates; agent proposes actions with evidence references.
Workflow executes consequential actions only with current runtime authorization.
evidence + proposal + updates
allow / hold / escalate / deny
Human reviewer
Receives escalated case
Returns recorded decision
review request / decision
Enterprise systems
Payment / binding / issuance targets
agentic tool call
requires current allowance
execution result
Fig. 1. Reference architecture for a runtime-controlled agentic workflow. Solid arrows show case inputs, proposals, processing, and agentic tool execution.
Dashed arrows show runtime outcomes, review, decision recording, and invalidation. The runtime returns authorization to the agentic layer; its action connector
invokes a target only with a current allowance.
Every consequential tool invocation crosses the runtime
authorization gate. The model agent cannot call a target directly;
the registered action connector holds execution credentials
and must obtain a current allowance from the runtime before
invoking a consequential action. The agentic layer owns the
workflow and initiates the invocation after authorization; the
runtime returns allow, hold, escalation, or denial rather than
sending the action itself. Alternate clients and APIs cannot
bypass this topology. It treats F8.
Deployment enumerates mutations. Action-connector retries
re-adjudicate with idempotency keys. Workers are governed
or declared ungoverned. Privileged access is break-glass and
logged. Consoles and legacy clients call the layer or fall outside
the manifest. Third parties require notification. Non-layer writes
are detectable. The guarantee covers the registered surface.
B. The ledgers
The append-only ordered log records results, decisions,
outputs, signals, notifications, and policy changes. Typing
records source, not truth. Facts are accountable observations,
assertions are agent characterizations, and signals are evaluator
judgements. Parser errors remain attributable. On 8871, three
extracted exceptions are facts andone material issue, recom-
mend bindis an assertion. They coexist. Typing prevents F7
and separates extraction.
Human decisions record actor, claimed authority, policy
version, and a rendered fingerprint of the decision record. The
junior 8871 approval has a decision read set containing the
three exceptions. A fourth exception changes that read set,
making freshness and retrospective checks mechanical.
C. State reconstruction
State is rebuilt from the initial case state and ordered
event log, without model or external reads. Correct replicas
reconstruct the same state. Assertions do not change facts. Each
adjudication records one log position for exact replay.
D. The assurance engine
The rules engine takes applicable obligations, thresholded
signals, the business-authority result, and evidence absence.
Policy, thresholds, and authority are immutable. On 8871,
access passes but standing fails.
Each applicable obligation votes. The engine records all
votes but returns the most restrictive one (Section VII-A). A
new obligation can raise, not lower, an outcome. Its record
pins the action, decision read set, versions, votes, outcome,
and log position for audit replay.
E. The controller and temporal re-evaluation
The controller records its outcome and returns it to the agen-
tic layer. Escalation cites facts, contrary assertions, mismatched
approvals, and obligations; the agentic workflow routes the case
to a reviewer and returns the review decision as a logged event.
The registered action connector checks the allowance again
immediately before a consequential invocation. Irreversible
actions are synchronous, so no approval is terminal.
A pending decision record is current only while none of its
decision dependencies changes. Restoring a value cannot repair
a stale record. The controller re-adjudicates affected actions
and returns the updated outcome to the agentic layer. On 8871,
a fourth exception stales the pending binding allowance before
the action connector can invoke binding.

6
F . Formal properties
The following are architectural arguments for governed
actions. They use the controller protocol in Section V-A
and the assumptions below. They do not establish input
truth, endpoint exactly-once effect, or behavior outside the
governance boundary.
Assumption 1(Complete interception).Every registered
system-of-record mutation and externally binding action passes
through the governance layer by credential topology, not
convention.
Assumption 2(Authoritative event ingestion).Every decision-
relevant event, including expiry, enters the log with its affected
dependency or version-applicability identity before a later
action using it dispatches.
Assumption 3(Immutable governance artifacts).The log
is append-only and ordered. Its existing entries, initial case
state, decision records, stored values, and policy, threshold,
authority, registry, replay, and rule versions remain unchanged
and available.
Assumption 4(Defined dispatch semantics).For one action,
the final validity check, outcome selection, and dispatch are
serialized with additions to the log.
Theorem 1(Dispatch invariant).Under Assumptions 1–4,
every governed irreversible or externally binding action has
a current decision record that permits its dispatch. The claim
concerns governance-boundary dispatch. It does not establish
execution, exactly-once effect, or atomic external logging.
Proof:The registered action connector sends each pro-
posed consequential action to the controller and waits for its
outcome. Ingestion records every prior relevant event. Under
the rule in Section V-A, a relevant change makes the earlier
record stale even if values later return. The connector invokes
the target only after the controller returns permission and the
final validity check confirms a current record. Serialization
excludes a relevant event between that check and invocation.
Thus each governed dispatch satisfies the invariant.
Theorem 2(Deterministic adjudication).For a fixed log
prefix, action, decision-read-set values, and pinned governance-
artifact versions, the engine returns the same intervention.
Proof:Replay reconstructs the same state. Assumption 3
preserves the recorded inputs and procedures used by D. D
reads those inputs without a new model or external call. Its
fixed rules therefore return the same intervention.
Theorem 3(Temporal invalidation).A relevant event after
a decision makes its record stale permanently, even if values
return. Without such an event, the record remains current.
Proof:The validity rule examines all relevant events
since the decision. Append-only history retains a change after
reversal, so the old record cannot become current again. Without
a relevant event, the rule leaves it current.
Proposition 1(Audit replay).Under Assumption 3, any past
adjudication can be reconstructed without the agent or model.
TABLE V
Typical prospective response by deficiency and reversibility.
Deficiency Reversible or compensable Irreversible
None allow allow
Residual doubt (F4) monitor or escalate escalate
Missing evidence (F3) require evidence require evidence
Insufficient standing
(F1)
escalate escalate
Rule unclear (F6) pause pause
Action prohibited (F5) deny deny
Invalid prior allowance
(F2)
pause; re-adjudicate pause; re-adjudicate
Proof:The retained record supplies the log position, action,
read set, stored values, versions, votes, and outcome. Replay
reconstructs the state, and Theorem 2 reproduces the result.
Authorization validity is not exactly-once execution. A lost
acknowledgement can permit a valid retry to commit twice.
The controller records it as pending with an idempotency
key. Transactional endpoints append and effect atomically.
Conditional writes reject old tokens. Weaker endpoints expose
duplicates at reconciliation. Optimistic concurrency supplies
compare-and-swap [14]. The first two grades preserve the
governed-dispatch guarantee. Input truth remains outside the
guarantee.
G. Component necessity
Removing interception readmits F8. Removing typing read-
mits F7. Removing reconstruction or re-evaluation readmits F2.
Removing authority, evidence, or policy versioning readmits
F1/F5, F3, or F6. Admitting raw signals loses F4 detection or
determinism. These components provide the stated coverage
in this architecture.
VII. From Failures to Intervention
A. Prospective intervention versus remediation
Table V maps deficiency and reversibility to the typical
prospective response. Six prospective outcomes address action
proposals: allow, monitor, require evidence, escalate, pause,
and deny. Rollback or compensation is a separate post-
effect remediation operation. This removes the misleading
implication that undoing an effect is merely a more restrictive
form of denying a proposed action. In the accompanying
implementation, rollback appears as a seventh entry in the
same intervention list; the paper separates it because undoing
a landed effect is not a stronger form of refusing a proposal.
Where multiple deficiencies coexist, the engine logs each
one and applies the declared resolution policy—in the evaluated
instance, a total restrictiveness order over the prospective
outcomes. A landed effect may be reversed or compensated
under a separate, authorized recovery policy. An irreversible
effect cannot be rolled back; it can only be surfaced, reconciled,
or remedied by another permissible process.
VIII. Illustrative Evaluation
A. Setup and scope
We evaluate the specification with a deterministic replay
harness. Acaseis a hand-written, ordered event log for one

7
workflow, containing recorded facts, documents, approvals,
evaluator signals, and agent proposals, together with the
governing policy and threshold versions and a declared
expected outcome. The harness replays each log through a
controller configuration event by event and records every
adjudication and dispatch decision. The library contains 42
such author-written cases: 27 include specified failures and
15 are designated clean, so that the prevented-violation rate
is measured rather than trivially perfect. Scripted proposals
and assertions replace a live agent; the harness makes no
model, external-system, or wall-clock read. Its purpose is to
check whether the specified adjudication, invalidation, and
replay paths produce the intended outcomes under the stipulated
policies and event sequences.
We compare (i) a point-in-time evaluation configuration that
adjudicates a proposal once and carries its allowance forward
without a later validity check, (ii) the proposed state-bound
configuration using the same recorded policy, authority, and
signal inputs, and (iii) a whole-state fingerprinting ablation that
treats all case-state changes as relevant. The comparison isolates
state-bound temporal invalidation relative to a deliberately non-
re-evaluating configuration. It does not compare against a
dispatch-time policy engine with independently maintained
approval provenance, or establish advantage over all agent
guardrails and runtime enforcement architectures.
B. Results and interpretation
Table VI reports the aggregate counts. All 15 later-invalidated
approvals are identified by the state-bound configuration and
not revisited by the point-in-time configuration. The state-
bound configuration holds 14 affected actions before dispatch
and addresses one compensable effect after it had landed. In
the compensable case, a relevant state change occurred after
valid dispatch but before the external effect completed; the
resulting effect required compensation rather than prospective
prevention. These outcomes should not be collapsed into a
single prevention statistic.
Eight failures already present at proposal time are caught by
both configurations; two of these are attempts to circumvent
in-path controls— an agent re-requesting dispatch of a denied
action, and an agent asserting over a disqualifying fact—refused
by both.
The 15 temporal invalidations and the five cases primarily
labeled F2 describe different categorizations: temporal invalida-
tion can expose an authority, evidence, grounding, prohibition,
or rule problem; Table VII lists each affected case’s primary
deficiency.
Two rates summarize the trade-off, with denominators fixed
by the harness. The adverse-effect rate is the share of the 23
governed actions with a non-dispatch outcome under the final
stipulated case state that nonetheless produce an external effect:
65.2% (15/23) point-in-time versus 4.3% (1/23) state-bound.
The one state-bound effect was dispatched while valid and
became adverse after a later state change but before external
completion.
The escalation rate is the share of all 43 proposed actions
routed to a human: 11.6% (5/43) versus 32.6% (14/43).
TABLE VI
Reported counts from the 42-case replay. Denominators are stated where they
differ from the number of cases; adverse-effect interpretation requires
verification against the replay sequence.
Measure Point-in-time State-bound
Later-invalidated approvals identified (15) 0 15
Affected actions held before dispatch 0 14
Affected landed effects compensated 0 1
Proposal-time failures caught by both 8 8
Clean cases unnecessarily held (15) 0 1
Adverse external effects(of 23 governed actions with
non-dispatch final outcome)
15 1
Escalations to a human (of 43 proposed actions) 5 14
Byte-identical adjudication on repetition yes yes
TABLE VII
Primary deficiency assigned to the 15 affected cases. An approval can
additionally be temporally invalidated; F2 is not exclusive.
Primary case label Cases
F1 Authority/standing 3
F2 Staleness without a more specific primary label 5
F3 Evidence 2
F4 Recorded grounding 1
F5 Prohibition 1
F6 Rule identity 3
Total affected cases 15
The reduction in adverse external effects is accompanied by
additional human attention; both rates describe the scripted
replay, not production incidence. The 27 failure cases contain
28 governed actions; five are legitimately dispatched by both
configurations because their deficiency is remedied in the event
log before dispatch, leaving the 23 whose adjudicated outcome
is non-dispatch.
One of the 15 clean cases requires an additional hold even
though fresh adjudication permits the action: its amount changes
within the same authority limit, invalidating the old allowance
without rendering the new amount inadmissible. This is an
unnecessary repeat decision, not an assertion that the final state
violates policy. It motivates calibration of safe dependency
scope while preserving soundness.
Table VIII reports the fingerprinting ablation. The five-
case stress set places 10–20 irrelevant events after pending
allowances and contains no stale approvals. Whole-state
fingerprinting produces 74 re-adjudications and five unnec-
essary invalidations; the declared decision-relevant projection
produces none. The two configurations detect the same 15
stale approvals in the 42-case library. These results illustrate
the selectivity mechanism for the dependencies encoded by
the authors, not the reliability of automatically discovering all
real-world dependencies.
Each case was replayed three times under each configuration,
with byte-identical decision records and votes. This checks
reproducibility of the harness’s deterministic path; it is not a
latency, scalability, or live operational reliability result.
C. What the replay cannot establish
The authors defined the rules and cases, and the point-in-time
comparator is intentionally unable to re-evaluate. Hence the

8
TABLE VIII
Whole-state versus decision-relevant fingerprinting ablation. “False inv.”
denotes invalidation caused by events not requiring a changed substantive
authorization; a relevant change can still require an unnecessary repeat approval
when readjudication permits the action.
Configuration Re-adj. False inv. Stale det.
Whole-state, library 23 1 15/15
Decision-relevant, library 19 0 15/15
Whole-state, stress set 74 5 n/a
Decision-relevant, stress set 0 0 n/a
counts demonstrate specification behavior under constructed
conditions. A dispatch-time policy re-evaluator could detect
many of the same changes. The additional semantics proposed
here are the bound history of which prior approval is being
used, what evidence and authority supported it, and whether
that approval has been superseded. No head-to-head experiment
against such a stronger comparator is claimed.
The scripted counts are not estimates of production incident
prevalence or review capacity. In particular, the system may
increase the number of repeat approvals or escalations; the
practical burden requires measurement in a live deployment.
The current paper does not report production latency or claim an
empirical advantage over alternative implemented architectures.
IX. Discussion and Limitations
Interception.An unfronted payment rail or database edit is
F8. The controller cannot prevent an effect outside its registered
path. The dispatch-time property is conditional on credential
and integration topology.
Ingestion and external effects.A relevant update that has
not yet reached the log can invalidate the real-world business
basis without violating the stated theorem. State may also
change after a valid dispatch but before an external provider
commits. The architecture guarantees neither provider-side
atomicity nor exactly-once external effect; compensation and
reconciliation remain necessary.
Dependency completeness.Selective invalidation is sound
only if the declared read set includes derived, cross-step,
and policy-applicability dependencies. A missing dependency
permits a falsely retained approval. Unknown dependencies call
for conservative widening or review, at the cost of additional
intervention.
Extraction and evidence fidelity.A parser can misrecord
a loss amount and yield a reproducibly wrong decision.
Typing preserves the origin of assertions but does not prove
factual truth. Completeness checks cannot establish substantive
professional correctness.
Policy and workflow scope.The controller enforces encoded
obligations; an unencoded rule is unenforceable. It does not
solve general planning failure, deadlock, business desirability,
or professional judgment that cannot be represented as an
obligation. A human reviewer may still make a poor decision
even with accurate recorded context.
Next steps.Production incident libraries, stronger dispatch-
time comparators, integration measurements, and review-load
studies would establish how well this specification transfers
outside the hand-written cases. These are future work, not
unperformed experiments implied by the current results.
X. Conclusion
A business decision can be valid when issued and unusable
when an agent later acts. This paper specifies an explicit state-
bound allowance that records the decision basis, distinguishes
human approval from current execution permission, invalidates
associated allowances after relevant logged changes, and
requires a new admissibility check at the registered dispatch
boundary. It draws on established runtime enforcement, mutable
authorization, process compliance, and transaction-control
mechanisms, with a particular focus on long-lived business
decisions. The 42-case scripted replay illustrates its temporal
invalidation and selective fingerprinting behavior. Within the
specified assumptions and registered surface, the resulting
guarantee concerns validity at dispatch, not universal business
correctness or the timing and uniqueness of external effects.
References
[1] S. Y ao, N. Shinn, P . Razavi, and K. Narasimhan, “ τ -bench: A benchmark
for tool-agent-user interaction in real-world domains,”arXiv preprint
arXiv:2406.12045, 2024.
[2] A. Y ehudai, L. Eden, A. Li, G. Uziel, Y . Zhao, R. Bar-Haim, A. Cohan,
and M. Shmueli-Scheuer, “Survey on evaluation of LLM-based agents,”
arXiv preprint arXiv:2503.16416, 2025.
[3] L. Dong, Q. Lu, and L. Zhu, “AgentOps: Enabling observability of LLM
agents,”arXiv preprint arXiv:2411.05285, 2024.
[4] H. Wang, C. M. Poskitt, and J. Sun, “AgentSpec: Customizable
runtime enforcement for safe and reliable LLM agents,”arXiv preprint
arXiv:2503.18666, 2025.
[5] U. Mehmood, S. Sheikhi, S. Bak, S. A. Smolka, and S. D. Stoller, “The
black-box simplex architecture for runtime assurance of autonomous
CPS,” inNASA Formal Methods (NFM), ser. Lecture Notes in Computer
Science, vol. 13260. Springer, 2022, pp. 231–250.
[6] M. Leucker and C. Schallhart, “A brief account of runtime verification,”
Journal of Logic and Algebraic Programming, vol. 78, no. 5, pp. 293–303,
2009.
[7] F. B. Schneider, “Enforceable security policies,”ACM Transactions on
Information and System Security, vol. 3, no. 1, pp. 30–50, 2000.
[8] J. Ligatti, L. Bauer, and D. Walker, “Edit automata: Enforcement
mechanisms for run-time security policies,”International Journal of
Information Security, vol. 4, no. 1–2, pp. 2–16, 2005.
[9] L. T. Ly, F. M. Maggi, M. Montali, S. Rinderle-Ma, and W. M. P . van der
Aalst, “Compliance monitoring in business processes: Functionalities,
application, and tool-support,”Information Systems, vol. 54, pp. 209–234,
2015.
[10] M. P . Singh, “An ontology for commitments in multiagent systems:
Toward a unification of normative concepts,”Artificial Intelligence and
Law, vol. 7, no. 1, pp. 97–113, 1999.
[11] T. South, S. Marro, T. Hardjono, R. Mahari, C. D. Whitney, D. Green-
wood, A. Chan, and A. Pentland, “Authenticated delegation and autho-
rized AI agents,”arXiv preprint arXiv:2501.09674, 2025.
[12] V . C. Hu, D. Ferraiolo, R. Kuhn, A. Schnitzer, K. Sandlin, R. Miller, and
K. Scarfone, “Guide to attribute based access control (ABAC) definition
and considerations,” National Institute of Standards and Technology,
Tech. Rep. NIST Special Publication 800-162, 2014.
[13] J. Park and R. Sandhu, “The UCON ABC usage control model,”ACM
Transactions on Information and System Security, vol. 7, no. 1, pp.
128–174, 2004.
[14] H. T. Kung and J. T. Robinson, “On optimistic methods for concurrency
control,”ACM Transactions on Database Systems, vol. 6, no. 2, pp.
213–226, 1981.
