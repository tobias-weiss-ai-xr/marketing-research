---
title: 'StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions'
url: https://arxiv.org/abs/2610.05241
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Yongyuan Peng
- Zhou Feng
- Tongying Wu
- Jiahao Chen
- Yuan Su
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.05241
pages: 21
chars: 80873
fetched_at: '2026-11-08T13:35:11+00:00'
kb_version: 1
---

# StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions

StateWise: Diagnosing and Repairing Persistent Operational
State Before Agent Actions
YONGYUAN PENG,Xi’an Jiaotong University, China
ZHOU FENG,Zhejiang University, China
TONGYING WU,Xi’an Jiaotong University, China
JIAHAO CHEN,Zhejiang University, China
YUAN SU,Zhejiang University, China
CHUNYI ZHOU,Zhejiang University, China
TIANYU DU,Zhejiang University, China
SHOULING JI,Zhejiang University, China
LLM agents combine reasoning, tool use, and persistent memory to support work across tasks, reusing stored
operational records as premises for later actions. However, changes in environments or requirements can
invalidate these records, and existing action review, provenance tracking, and clarification mechanisms may
leave the underlying persistent state uncorrected. Our audit of coding-agent trajectories further identifies
candidate failure chains linking the continued reuse of invalid records to task failures and unsafe modifica-
tions. To address this problem, we proposeStateWise, a framework for diagnosing and repairing persistent
operational state before action execution. StateWise uses record-level counterfactual replanning to identify
decision-critical records by examining how individual record interventions change the proposed action while
holding other planning inputs fixed. A hierarchical resolver establishes their current validity through reliability
checks, read-only verification of machine-observable facts, and targeted clarification of developer-owned
intent. Typed evidence grounding binds the resulting evidence to specific records and their applicable scopes,
enabling persistent corrections that preserve repair lineage and support reuse across tasks. The agent then
replans from the repaired state, and an independent state–action check assesses the revised proposal before
execution. We then evaluate StateWise on a benchmark of 150 executable coding-agent cases across diverse
runtime environments, workspace configurations, and repository settings, complemented by cross-model
evaluations. Under corrupted persistent state, StateWise achieves 93.3% overall correctness compared with
38.7% for the baseline agent and records no unsafe actions. Furthermore, component ablations, multi-task
experiments, and transfer evaluations demonstrate the effectiveness of its recovery mechanism, the persistence
of its corrections, and its transferability across repositories and tool interfaces.
1 Introduction
Advances in the reasoning, tool-use, and planning capabilities of large language models (LLMs) have
enabled LLM-based agents to undertake complex tasks across multiple interactions [37, 39, 43, 49].
For example, coding agents use these capabilities to configure development environments, modify
repositories, investigate failures, and continue working on software projects [44, 48]. To maintain
continuity across tasks, agents retain operational records in persistent state, including environment
facts, repository policies, developer intent, task progress, and historical observations [28, 40, 46, 52].
Agents retrieve and reuse these records to build on previous work and plan subsequent actions.
When retrieved records guide tool selection, target identification, or action arguments, they serve
as premises for operational decisions. Task correctness and operational safety therefore depend on
whether the records supporting an action remain valid in its current context.
Authors’ Contact Information: Yongyuan Peng, Xi’an Jiaotong University, Xi’an, China, yongyuan16625@gmail.com;
Zhou Feng, Zhejiang University, Hangzhou, China, zhou.feng@zju.edu.cn; Tongying Wu, Xi’an Jiaotong University,
Xi’an, China, wty419591@gmail.com; Jiahao Chen, Zhejiang University, Hangzhou, China, xaddwell@zju.edu.cn; Yuan
Su, Zhejiang University, Hangzhou, China, yuansu@zju.edu.cn; Chunyi Zhou, Zhejiang University, Hangzhou, China,
zhouchunyi@zju.edu.cn; Tianyu Du, Zhejiang University, Hangzhou, China, zjradty@zju.edu.cn; Shouling Ji, Zhejiang
University, Hangzhou, China, sji@zju.edu.cn.
arXiv:2610.05241v1  [cs.SE]  4 Oct 2026

2 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
Persistent State Error in a Coding Agent
MEMORYACTIONOUTCOME
t₁ Incorrect Belief t₁ Incorrect Belief
t₂ Action t₂ Action
t₃ Failure t₃ Failure
Updated:
2:00
Remembered:
3:00
Current:
B26
Stored:
B12
Go at
2:30
Go to
B12
Missed movie Missed flight
Coding Agent
$ git push --force-with-lease
Actual branch
protection = true Coding Agent
Safe Alternative Action
The failure begins before the action.
Baseline with Corrupted
Persistent State
StateWise with Corrupted
Persistent State
Human Memory Agent Belief State
Persistent State
branch_is_protected = false
corrupted / stale
Unsafe Action
Force-push on protected branch
1
Risk check
2
State
attribution
3
Verify /
repair
4
Replan
$ open_pull_request
Persistent State
branch_is_protected = false
corrupted / stale
Verification:
branch_is_protected = true
Persistent state repaired to true
StateWise asks not only whether an action is safe,
but also whether the state that led to the action is trustworthy.
Fig. 1. Persistent-state errors and recovery across memory, action, and outcome. The first two scenarios show
how outdated movie times and airport gates cause failures in human memory and agent belief state. Given
the same outdated branch-policy record, the baseline proposes a prohibited force push, whereas StateWise
verifies and repairs the record before replanning to open a policy-compliant pull request.
However, as projects, policies, and environments change, persistent records that were correct
when stored can become outdated or inapplicable. Prior work documents stale memories, super-
seding evidence, and facts used beyond their period of validity [9, 12, 16, 31, 47]. As operational
records accumulate across extended interactions, maintaining their current applicability becomes
increasingly difficult [2, 41]. For coding agents, as illustrated in Figure 1, reusing invalid records
as operational premises can lead to task failures or unsafe modifications. Because these records
persist across tasks, blocking an erroneous operation alone leaves its underlying premise available
to influence later plans. Effective recovery therefore requires locating the records behind the action,
verifying their current validity, and preserving confirmed corrections for subsequent tasks, where
existing intervention mechanisms face three limitations in providing this form of recovery:
Limitation 1: Action Control without Persistent Repair.Action-level safeguards, including
execution-boundary controls and approval mechanisms, primarily determine whether a proposed
operation should proceed [7, 11]. Risk-evaluation frameworks also examine potentially harmful
agent operations in simulated or executable environments [23, 35]. These approaches can assess or
constrain an operation without necessarily identifying and correcting the persistent state error
that produced it. An erroneous record can therefore be reused in later tasks even after the current
operation is blocked, causing the agent to propose incorrect or unsafe operations again.
Limitation 2: Unverified Validity of Trusted Records.Provenance and information-flow
methods help identify untrusted inputs and trace their influence on agents [8, 27, 38]. However, a
trustworthy source does not establish that a record remains valid. An authentic, unmodified record
can become inapplicable to the current operation after the environment changes. Similarly, an
agent can remain confident in a plan built on an outdated record, preventing uncertainty-based
clarification from being triggered [17, 34]. Even when a conversation corrects the current decision,

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 3
later tasks can reuse the old information if the corresponding persistent record is not updated.
These failures require no attacker, so defenses against malicious input alone are insufficient [1].
Limitation 3: Incomplete Diagnosis of Action Premises.When an operation depends on
multiple historical records, reviewing the operation alone leaves the influence of individual records
unresolved. Attribution and memory-lineage methods trace how historical context and stored
records contribute to agent decisions [27, 32]. For persistent-state diagnosis, these influence links
must also be connected to the current validity and scope of the underlying records. Research on
stale memory shows that later evidence can invalidate earlier premises and require corresponding
changes in downstream behavior [9]. The same operation can be appropriate under a valid premise
but risky under an outdated or mis-scoped one. State diagnosis therefore requires locating the
records that shape action selection and verifying their applicability to the current task.
These limitations motivate examining how historical operational information continues to
shape agent decisions after becoming invalid. We audited 100 coding-agent sessions sampled
from SWE-chat, a corpus of coding-agent interactions from real users [ 5], tracing the reuse of
historical information and checking the cited turns and their chronology. The audit retained 40
candidate failure chains involving task failures, user corrections, or unsafe modifications. Across
these candidates, historical information continued to guide actions despite evidence that it no
longer applied to the current operation.
Accordingly, these observations motivate the following recovery question:How can coding agents
identify and repair invalid operational premises before execution and preserve verified corrections for
later tasks?To make this question precise, we first characterize how persistent records influence
action selection. A record isdecision-criticalwhen changing or removing it changes the proposed
action while other planning inputs remain fixed. We then define apersistent-state-induced action
failureas a failure in which an incorrect, stale, or mis-scoped record changes the proposed action
relative to its currently valid counterpart and leads to an incorrect or unsafe outcome. Recovery
therefore aims to verify the premises supporting an action, persist confirmed corrections within
their applicable scopes, and replan before external side effects occur.
To address this problem, we propose StateWise, a pre-action framework for diagnosing and
repairing persistent operational state. Given a proposed action with external side effects, StateWise
traces its supporting records, resolves their current validity, and writes confirmed corrections to
persistent storage. The agent then replans from the repaired state, and an independent state–action
check governs execution. This framework enables agents to address four challenges arising from
the recovery problem.
Q1: How can recovery distinguish decision influence from retrieval relevance?A persistent-
state-induced action failure depends on a record changing action selection. Recovery must therefore
identify decision-critical premises among the many records retrieved as relevant context. StateWise
uses constrained counterfactual replanning to isolate record-level influence. It removes or changes
one candidate record while holding other planning inputs fixed, then compares the resulting
action’s operation, target, arguments, and scope with the original proposal. Type and scope bindings
connect this influence evidence to the corresponding action slots, locating candidate decision-critical
premises for verification.
Q2: How can recovery verify current validity across different record types?Diagnosing
an incorrect, stale, or mis-scoped premise requires evidence about both its value and its current
applicability to the proposed action. The appropriate evidence depends on the record’s type and
authority. StateWise uses hierarchical state resolution, first checking type, scope, source authority,
freshness, and conflicting evidence. It then resolves remaining machine-observable facts through
read-only verification and developer-owned intent through targeted clarification. The resolver

4 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
explicitly assigns each record a valid, defective, or unresolved status, grounding subsequent repair
and execution decisions in the available evidence.
Q3: How can recovery preserve corrections and their scope across tasks?A correction made
only in the current interaction leaves the persistent premise available to influence later plans.
Recovery must therefore preserve corrections together with their applicability boundaries and
supporting evidence. StateWise uses typed evidence grounding to bind each confirmed correction
to the attributed record and its applicable scope. Within that scope, the update supersedes the
defective active value and retains the original record and corrective evidence as repair lineage.
Later tasks can retrieve the corrected value together with the basis for its update.
Q4: How can recovery address action risks that remain after state repair?Repairing a
decision-critical premise can change the proposed action while leaving other planning errors
unresolved. Recovery must therefore assess the revised operation against the repaired state and
execution constraints. StateWise replans from the repaired store and applies an independent state–
action check to the new proposal. This check evaluates the action’s arguments and scope against the
verified state, safety invariants, and permission requirements. Execution proceeds only when the
required premises are resolved and the checks pass, with StateWise returning a safe stop otherwise.
In general, our contributions are as follows:
• We audit real coding-agent trajectories and identify candidate chains in which historical
operational information continues to influence actions despite conflicting evidence, exposing
a persistent-state recovery gap. We formalizepersistent-state-induced action failurethrough
record defects, decision-critical action dependence, and incorrect or unsafe outcomes, and
define pre-action recovery around verification and scoped persistent repair.
•We developStateWise, which couples constrained counterfactual replanning with hierar-
chical state resolution to connect action influence with current validity. Typed evidence
grounding binds confirmed corrections to the attributed records and scopes, producing per-
sistent repairs with lineage for replanning and cross-task reuse. An independent state–action
check governs execution of the revised proposal.
• We evaluate StateWise on a benchmark of 150 executable cases spanning runtime, workspace,
and repository state, complemented by component ablations, four-task sequences, cross-
model tests, and transfer evaluations. Further experiments demonstrate the effectiveness of
its recovery mechanisms, the persistence of its corrections, and its transferability across
repositories and tool interfaces.
• We open-source the StateWise implementation to support reproducibility and further re-
search on persistent-state recovery.
2 Background and Related Work
LLM agents combine planning, tool use, feedback, and memory to support work across interac-
tions [37, 39, 43, 49, 51]. A recent survey identifies the safety implications of reusable state and its
influence on later agent behavior [10]. Coding agents apply these capabilities to environment config-
uration, repository modification, and iterative debugging across interactions [44, 48]. Their reliance
on historical operational information connects three research concerns: maintaining applicable
records, tracing their influence on actions, and supervising the resulting operations.
Agent-memory systems support this continuity by organizing and retrieving information from
earlier experience [28, 30, 39, 40, 51, 52]. A-Mem creates links among structured memories and
updates existing representations as new information arrives [46], while Mem0 extracts and consoli-
dates salient conversational information for persistent retrieval [13]. Memory benchmarks assess
recall, reasoning across sessions, and adaptation to updated information [24, 45]. As these memories

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 5
are reused, their current validity becomes central to agent reliability. Temporal question-answering
research studies facts whose validity changes over time [12, 16, 21, 42], while agent-memory re-
search examines stale records, superseding evidence, and temporal validity in retrieval [9, 31, 47].
Knowledge-editing research likewise studies factual updates, their consequences for related knowl-
edge, and preservation of unrelated knowledge [ 14, 25, 26, 53]. For operational records, these
concerns extend to whether a correction remains applicable to the current task and scope.
Maintaining applicable records also requires tracing their influence on actions. Prompt-injection
research and benchmarks examine how untrusted external content redirects agent behavior [ 1,
15, 50]. Attribution and provenance methods trace these influences through memory lineage [27],
provenance analysis [38], information-flow tracking [8], and attribution to earlier context [ 32].
These methods help locate the sources and contextual premises behind a decision, particularly
when the underlying information may be untrusted. An authentic record can nevertheless become
outdated as its environment changes. Operational diagnosis therefore requires connecting these
influence links to evidence about a record’s current value and applicability to the proposed operation.
At the execution boundary, this diagnostic concern connects to oversight of the resulting opera-
tion and its potential consequences. Human oversight and mixed-initiative systems provide ways to
intervene in automated decisions [4, 19]. Repeated confirmations can encourage routine approval,
while poorly explained warnings may be ignored [ 6, 20, 22, 29, 36]. Clarification methods seek
missing information or user intent relevant to the current task [3, 17, 33, 34]. Action safeguards
choose whether to execute, ask, or refuse a proposed operation [11]. Execution controls constrain
resource access, while risk-evaluation frameworks assess operations in emulated or executable
environments [7, 23, 35]. For cross-task recovery, any correction established through oversight
must also be written to the persistent record within its applicable scope.
Together, these research directions address information retention, changing facts, decision prove-
nance, and action oversight. A remaining challenge lies at their intersection: when an erroneous
persistent record influences an action, recovery requires locating that record, establishing its current
validity, and preserving a correction within the appropriate scope.
3 Problem Definition
The preceding discussion identifies a gap between constraining an action and correcting the
persistent record behind it. We first examine this gap in real coding-agent trajectories, then use the
observed pattern to formulate persistent-state recovery.
Observation.We sampled 100 coding-agent sessions from SWE-chat [ 5]. A model annotator
identified 60 candidate chains linking an earlier operational fact to a later dependent action, contra-
dictory evidence, and an observable consequence. Checking the cited turns and their chronology
retained 40 candidates. Figure 2 summarizes the audit funnel, invalid-state categories, and observed
consequences.
The retained candidates exhibit a common pattern: historical operational information remains
available and is reused in a later decision, while new evidence indicates that it no longer applies
to the current operation. These observations motivate a recovery problem: identify the persistent
records that influence a proposed action, establish their current validity, and preserve scoped
corrections for replanning and later tasks. To make this problem precise, we distinguish record
influence, record defects, and action outcomes, then specify the requirements for recovery.
State–Action Dependence.To model this pattern, consider a tool-using coding agent that carries
operational records across tasks. Let𝑇𝑖 denote task𝑖,𝑀𝑖 its persistent store, and𝑡 a decision step
within the task. We use𝑔𝑖 for the task objective,𝐻𝑖 for the set of hard safety invariants, and𝑜𝑖 for

6 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
1 Historical Record
(persistent state)
Agent retains operational records
across tasks and reuses them
as premises for decisions.
repository.records
key: protected
type: Boolean
scope: repo A / main
value: false
tool.config
key: python_version
type: String
scope: workspace
value: 3.8
user.prefs
key: test_command
type: String
scope: global
value: pytest
...
2 Agent Decision
(uses the record)
The agent retrieves the record,
builds a plan, and proposes
a tool operation.
Retrieved Context (excerpt)
repository.records.protected
= false  (repo A / main)
“push the changes”
Proposed Action
$ git push -- force
3 Conflict and Consequence (new evidence vs. record)
New evidence indicates the record
no longer applies, but the agent
still follows the outdated record,
leading to erroneous or unsafe outcomes.
New Evidence (current environment)
branch protection = true
(repo A / main)
≠
Persistent Record (outdated)
branch protection = false
(repo A / main)
Task Failure
e.g., push rejected,
test failed
User Correction
e.g., user intervenes
to fix the action
Unsafe Mutation
e.g., unintended
modification
Failure Types in Retained Chains (n = 40)
Reasons why persistent records become invalid.
(Each chain may involve multiple reasons.)
Count Share
Stale
Record is outdated. 17 43.3%
Conflict
Conflicts with
new evidence.
30 75.0%
Scope Mismatch
Applied in the wrong
repository, branch, or context.
25 63.3%
Unverified History
Lacks verification from
the current environment.
25 63.3%
Audit Funnel
100
Sampled
Sessions
60
Possible
Chains
40
Verified
Cases
Real Coding-agent
Trajectories
Model-positive
Candidates
Structurally Verified
Failure Chains
Observed Outcomes in Retained Chains (n = 40)
Count ShareTask Failure
Task does not complete
successfully. 17 43.3%
User Correction
User intervenes to
correct the agent. 15 38.3%
Unsafe Mutation
Potentially unsafe
modification is performed.
6 15.0%
Agent Sources and Confidence (n = 40)
Agent Source Annotation Confidence
Count Share Count Share
C
Claude Code
28 70.0%
OpenCode
12 30.0%
High 24 60.0%
Medium 13 32.5%
Low 3 7.5%
user request:
..
Fig. 2. Observed failure patterns from coding-agent trajectories. Historical operational records may be reused
as premises for later decisions even after conflicting evidence appears. The audit retained 40 candidate chains
from 100 sampled sessions after checking cited turns and chronology. Failure-type categories may overlap.
the observed task outcome. A persistent operational record is
𝑟=(𝑘,𝑣,𝜏,𝜎,𝜋),
where𝑘 is a typed key,𝑣 its semantic value,𝜏 its time and freshness metadata,𝜎 its scope, and𝜋
its provenance and authority metadata. These attributes describe the record and its applicability
conditions. Storage alone does not establish that its content is correct or currently valid.
Let𝑛 be the number of records in the store and𝑅 the retrieval function. The store and retrieved
context are
𝑀𝑖 ={𝑟 1,...,𝑟 𝑛}, 𝑆 𝑖,𝑡 =𝑅(𝑀 𝑖,𝑇𝑖,𝑡).
Let 𝑃 denote the base planner with its output normalized to an action representation. The
proposed action is
𝑎𝑖,𝑡 =𝑃(𝑇 𝑖,𝑆𝑖,𝑡).
A normalized action specifies its tool, operation, target, arguments, and scope. A stopping decision
is represented explicitly when no operation is proposed. Other planning inputs are suppressed in
the notation and held fixed when comparing the effects of different records.
The first recovery challenge is to identify which retrieved records influence the proposal. For
a retrieved record𝑟, let𝐼𝑟(𝑆) remove or change only that record while preserving the rest of the
context. We call𝑟decision-criticalfor the proposal if
𝑃(𝑇𝑖,𝐼𝑟(𝑆𝑖,𝑡))≠𝑎 𝑖,𝑡.
This action-based definition distinguishes decision influence from retrieval relevance. Influence
and validity are assessed separately, so a decision-critical record can be valid or defective. For a
stochastic planner, counterfactual comparisons must account for sampling variation. Bounded
probes provide evidence of record dependence under matched planning conditions.
Failure Conditions.Decision-criticality establishes a record’s influence on action selection. To
characterize the observed failure pattern, we additionally define whether the record is defective and
whether the resulting action produces an incorrect or unsafe outcome. Let ˆ𝑟 be the retrieved record

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 7
and𝑟 ★ its authoritative, currently valid counterpart for the same fact in the current environment
and scope. Write𝑣(𝑟) for the semantic value of a record and𝐴(𝑟,𝑇𝑖)∈{ 0, 1} for whether its scope
and authority apply to task𝑇𝑖. Define the defect indicator
𝐷( ˆ𝑟,𝑇𝑖)=
(
1, 𝑣( ˆ𝑟)≠𝑣(𝑟 ★) ∨𝐴(ˆ𝑟,𝑇𝑖)=0,
0, 𝑣( ˆ𝑟)=𝑣(𝑟 ★) ∧𝐴(ˆ𝑟,𝑇𝑖)=1.
Defectiveness is determined by semantic mismatch or current inapplicability, with temporal and
provenance metadata informing this assessment.
To isolate the effect of the defective record, let𝑆𝑖,𝑡[𝑟] denote the same retrieved context with
the record under consideration set to𝑟, leaving all other records unchanged. The corresponding
actions are
ˆ𝑎=𝑃(𝑇 𝑖,𝑆𝑖,𝑡[ˆ𝑟]), 𝑎 ★ =𝑃(𝑇 𝑖,𝑆𝑖,𝑡[𝑟★]).
To express their consequences, let𝑜(𝑎) denote the outcome resulting from action𝑎 under the
task’s environment. The outcome includes an explicit stopping decision when no side effect is
performed. Let𝑔𝑖(𝑜)∈0,1 indicate whether outcome𝑜 satisfies the task objective, and letℎ(𝑜)∈0,1
indicate whether invariantℎ∈𝐻 𝑖 holds. We define
𝐽(𝑜;𝑔 𝑖,𝐻𝑖)=𝑔 𝑖(𝑜)
Ö
ℎ∈𝐻𝑖
ℎ(𝑜), 𝑉(𝑜;𝐻 𝑖)=1−
Ö
ℎ∈𝐻𝑖
ℎ(𝑜).
Here𝐽= 1denotes a correct and safe outcome, while 𝑉= 1denotes a safety violation. The product
over an empty invariant set is defined as one.
Apersistent-state-induced action failureoccurs when
𝐷( ˆ𝑟,𝑇𝑖)=1∧ ˆ𝑎≠𝑎 ★ ∧𝐽(𝑜( ˆ𝑎);𝑔𝑖,𝐻𝑖)=0.
These conditions combine a defective record, a record-dependent action difference, and an incorrect
or unsafe outcome. The comparison with𝑎★ establishes record dependence, while other planning
errors can still affect the reference action.
The defect condition covers records that were incorrect when stored, became stale, conflict with
newer evidence, or apply only to another scope. Such defects can arise during ordinary project and
environment changes. An operation may therefore follow the retrieved record while conflicting
with current task requirements. The counterpart𝑟 ★ defines the reference condition. A recovery
procedure establishes corrections through evidence available in the current task.
Recovery Requirements.Recovery addresses this failure by resolving the records supporting a
proposed action and replanning from corrected persistent state. Its objective is a correct and safe
task outcome together with preservation of unrelated persistent records. For ashould-acttask,
satisfying𝑔𝑖 requires the specified mutation. For ashould-stoptask, it requires a safe refusal.
Correctness under𝐽requires both the task objective and all hard safety invariants to hold.
Given a proposed action with external side effects, recovery identifies its decision-critical records,
obtains admissible evidence, and corrects confirmed defects within their established scope. Let
𝑈𝑖 denote the resulting update andU𝑖 the set of updates supported by admissible evidence. Such
evidence must come from an authority appropriate to the fact, such as a current environment
observation or a developer’s statement of intent. The updated store and replanned action are
𝑀′ 𝑖 =𝑈𝑖(𝑀𝑖), 𝑎 ′ 𝑖,𝑡 =𝑃(𝑇 𝑖,𝑅(𝑀′ 𝑖,𝑇𝑖,𝑡)).
To constrain the extent of repair, let Σ𝑖 contain the established repair scopes, and let ¯Σ𝑖 denote all
scopes outside that set. For a set of scopesΩ, the restriction𝑀|Ωdenotes the active records of𝑀
within those scopes. DefineA𝑖 as the set of actions and stopping decisions that satisfy the task’s
hard safety constraints and permission requirements.

8 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
Admissible recovery requires
𝑈𝑖∈U𝑖,
𝑎′ 𝑖,𝑡∈A 𝑖,
𝑀′ 𝑖| ¯Σ𝑖 =𝑀𝑖| ¯Σ𝑖.
The first condition grounds updates in admissible evidence. The second constrains the revised
action independently of state repair, and the third preserves active records outside the repair scope.
Successful recovery additionally requires
𝐽(𝑜(𝑎′ 𝑖,𝑡);𝑔𝑖,𝐻𝑖)=1.
Admissibility thus constrains how records and actions may change, while𝐽 evaluates the resulting
task outcome. A decision-critical premise required for safe execution must be resolved before the
dependent side effect is permitted.
Persistence and Transfer.Persistent repair extends recovery beyond the current proposal. To
define cross-task reuse, consider a sequence𝑄=(𝑇 1,𝑇2,...,𝑇 𝐿), with𝐿≥ 2, in which𝑇1 may trigger
a repair. Between tasks, the conversation and workspace are reset to their prescribed starting
conditions, while the persistent store is carried forward:
𝑀𝑖+1 =𝑀′ 𝑖.
Under this reset boundary, later tasks obtain corrections through retrieval from persistent state.
Define
𝑌𝑖 =𝐽(𝑜 𝑖;𝑔𝑖,𝐻𝑖), 𝐽 +(𝑄)=
𝐿Ö
𝑖=2
𝑌𝑖.
The indicator𝐽+ equals one only when every task after𝑇1 completes correctly and safely. It evaluates
downstream outcomes over the specified sequence. Attributing those outcomes to repair reuse
additionally requires evidence that later tasks retrieve and use the corrected record.
Beyond cross-task reuse, interface-conditioned transfer concerns the application of the recovery
procedure across repositories and tools. A fixed recovery core receives a declarative interface𝐶
specifying tool operations, typed state and action slots, scope semantics, and available verifier
adapters. The objective is to preserve recovery behavior across supported interfaces without
modifying the core. Authoritative reference values and outcome-scoring oracles are external to
the planner and resolver. The resolver obtains evidence through the declared verification and
clarification channels.
4 Method
The definition of persistent-state-induced action failure in Section 3 links a defective persistent
record to a change in action selection and an incorrect or unsafe outcome. Recovery therefore
requires resolving both the operational premises and the resulting action. Building on the re-
quirements in Section 3, StateWise introduces a recovery procedure between the base planner’s
side-effecting proposal and execution.
4.1 Overview of StateWise
StateWise operates alongside a tool-using base planner [37, 43, 49]. It receives the proposed action
𝑎𝑖,𝑡 =𝑃(𝑇 𝑖,𝑆𝑖,𝑡), the retrieved context𝑆𝑖,𝑡 , and the persistent store𝑀𝑖. The declarative interface𝐶
introduced in Section 3 supplies the tool operations, typed state and action slots, scope semantics,
and verifier adapters. For the current proposal,𝐶𝑎 denotes the interface’s binding to that action.
It specifies which action slots may depend on persistent state, their types and scopes, and the

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 9
repository.records
id: repo_3
type: repository
scope: acme/app
Persistent Store ℳ𝒊Proposal 𝒂𝒊,𝒕Task 𝑻𝒊
Investigate push failure
and enable code change
Operation: push
Target: origin/main
Arguments: --force
Retrieved
Context
𝑺𝒊,𝒕 = 𝓡 𝑴𝒊, 𝑻𝒊, 𝒕
Inputs
for Recovery
user.prefs
id: u_3
type: user
scope: global
workflow.rules
id: w_2
type: workflow
scope: acme/app
repository.records
key: protected
type: Boolean
scope: repo A / main
value: false
Candidate Retrieval
Find relevant candidate records for investigation
Retrieved Records (from 𝑺𝒊,𝒕)
Remove
𝑰𝒓 𝑺𝒊,𝒕
(drop record)
Uncertain
𝑰𝒓 𝑺𝒊,𝒕
(mask/unknown)
Alternative
𝑰𝒓 𝑺𝒊,𝒕
(plausible value)
Planner 𝑷
 Planner 𝑷
 Planner 𝑷
Compare Effects
+ type/scope binding
 Influential 𝑫𝒅𝒆𝒑 Uncertain 𝑼𝒂𝒕𝒕𝒓
𝑫+ = 𝑫𝒅𝒆𝒑 ∪ 𝑼𝒂𝒕𝒕𝒓
Temporary Probes (from 𝑺𝒊,𝒕)
Live Repository Policy
Developer-owned Intent
key: protected
type: Boolean
scope: repo A / main
value: true
> Confirm intended
change and acceptable
approach
Read-only Verifier
(live environment)
Target Clarification
(from developer)
Same record
+ type + scope
Evidence Routing (in parallel)
Valid
Value Preserved +
Applicability
Supported
Defective
𝑭
Confirmed Error +
Correction
Unresolved
𝑸
Missing /
Unusable /
Unbound Evidence
Resolution Outcomes
repository.records
key: protected
type: Boolean
scope: repo A / main
value: true
repository.records
key: protected
type: Boolean
scope: repo A / main
value: false repository.records
key: protected
type: Boolean
scope: repo A / main
value: true
Old Record (defective)
(superseded)
Lineage
New Record (active) Persistent Store 𝓜𝒊 ′ Reuse after conversation
+ workspace
reset
Later Tasks
Valid Records: No semantic write
(preserve value)
State-action Agreement
Hard Invariants
Permission Satisfied
Rebuild
Context
𝑺𝒊,𝒕 ′ = 𝓡 𝑴𝒊 ′, 𝑻𝒊, 𝒕
Independent
Action Check
Approved first, if required
Pass →
Execute
Unresolved or
Failed Check
→ Safe Stop
(perform action)
(block side effects)
𝑸𝒖𝒏𝒓𝒆𝒔 = ∅ and 𝜞 𝒂𝒊,𝒕 ′ , 𝑺𝒊,𝒕 ′ , 𝑯𝒊 = 𝟏
Replan
𝒂𝒊,𝒕 ′
Scoped Write-back of 𝑭
Resolution Repair & Action ControlAttribution
Action Contract 𝑪𝒂
Types: repository | file | setting | …
Scopes: workspace | repository | …
Verifiers: read-only | policy | …
Resolved
records
+ corrections
Fig. 3. The StateWise pipeline.Attributionuses counterfactual replanning and type/scope binding to identify
influential and uncertain records.Resolutionchecks their current validity using available evidence, read-only
verification, or targeted developer clarification. Confirmed defects receive scoped repairs that preserve lineage,
while valid records remain semantically unchanged. The planner retrieves the updated context and replans.
Execution requires resolved premises and an independent state–action, invariant, and permission check.
Persistent corrections remain available to later tasks.
read-only observations available for checking their values. These declarations adapt the recovery
procedure to supported repositories and tools while preserving the same recovery core.
Figure 3 organizes recovery into three stages.Attributionlocates records that influence the
proposal and retains consequential candidates whose dependence remains inconclusive.Resolution
assesses their current validity and obtains additional evidence through read-only verification or
targeted clarification.Repair and Action Controlwrites confirmed corrections to persistent storage,
replans from the updated context, and checks the revised action before execution. The procedure
returns a checked action or a safe stop, with confirmed corrections available for subsequent tasks.
The central technical contribution is a record-level connection between decision influence,
current validity, and persistent repair. StateWise couples constrained counterfactual replanning
with hierarchical state resolution and typed evidence grounding. Counterfactual probes identify
action-sensitive records, resolution obtains evidence from the appropriate authority, and evidence
grounding binds each correction to the attributed record and its established scope. Maintaining these
bindings across stages connects the premise that influenced an action to the evidence authorizing
its update. The resulting correction supports both current replanning and later retrieval, while an
independent state–action check addresses remaining execution risks.
4.2 Attribution: Decision-Critical Premises
The first challenge is to locate decision-critical premises among the many records retrieved for a task.
Attributionconnects retrieval to action selection through constrained record-level interventions
and typed state–action bindings.
Given𝑎𝑖,𝑡 ,𝑆𝑖,𝑡 =𝑅(𝑀 𝑖,𝑇𝑖,𝑡) , and𝐶𝑎,Attributionforms a candidate set from records linked to
the action’s arguments, target, policy, environment, or scope. Records with conflicting values are
retained together for subsequent verification. Candidate construction draws on agent-attribution
and memory-lineage methods [27, 32]. Let𝐶(𝑎 𝑖,𝑡,𝑆𝑖,𝑡)denote the resulting set.

10 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
For each𝑟∈𝐶(𝑎 𝑖,𝑡,𝑆𝑖,𝑡),Attributionapplies the intervention 𝐼𝑟 defined in Section 3. The inter-
vention removes or changes only𝑟, holding the remaining context and other planning inputs fixed.
These probes temporarily modify the planning context, leaving the persistent store unchanged. The
resulting proposal is compared with𝑎𝑖,𝑡 on properties specified by the action contract, including its
operation, target, arguments, scope, and risk class. Let𝑑A compare these properties. The bounded
dependence test is
Δcf(𝑟)=𝑑 A
𝑎𝑖,𝑡,𝑃(𝑇𝑖,𝐼𝑟(𝑆𝑖,𝑡)).
Holding other inputs fixed makes the comparison specific to the intervention on 𝑟. Comparing
normalized action properties focuses the test on operational changes. A positive value provides
evidence that𝑟is decision-critical under the bounded test described in Section 3.
Attributionthen checks whether the record has a compatible type and scope binding to the action.
Write𝐵(𝑟,𝑎 𝑖,𝑡,𝐶𝑎)= 1when 𝑟 can support the relevant action slot under the contract’s type and
scope rules. The records with counterfactual dependence evidence and compatible bindings form
𝐷dep =

𝑟∈𝐶(𝑎 𝑖,𝑡,𝑆𝑖,𝑡):Δ cf(𝑟)>0∧𝐵(𝑟,𝑎 𝑖,𝑡,𝐶𝑎)=1

.
The binding connects influence evidence to the specific operation and scope supported by the record.
This keeps similarly named paths, branches, and environments attached to their corresponding
action slots.Resolutionsubsequently assesses the record’s current validity for that operation.
A bounded probe can also leave dependence inconclusive. For a consequential proposal,Attribu-
tionplaces candidates with a strong provenance link to the action and inconclusive dependence
in𝑈attr. This retains potentially consequential premises for verification when the probe budget
provides insufficient evidence.Attributionoutputs 𝐷+ =𝐷 dep∪𝑈 attr, together with the bindings
and dependence evidence for the selected records.
4.3 Resolution: Current Validity
The second challenge is to establish whether an attributed premise remains valid for the current
operation. Validity depends on both the record’s semantic value and its applicability, and the
appropriate evidence varies with its type and authority.Resolutionaddresses this challenge through
a hierarchy of evidence checks, read-only verification, and targeted clarification.
For each record in𝐷+,Resolutionfirst examines its type, scope, source authority, freshness, and
newer or conflicting evidence. These checks assess whether the available evidence establishes
the record’s value and applicability for the present task. They address temporal and contextual
validity issues identified in agent memory [ 9, 31, 47]. When the available evidence is sufficient,
Resolutioncan classify the record directly. Additional verification is directed to premises whose
validity remains unsettled.
For a machine-observable fact,Resolutioninvokes the registered read-only verifier. The verifier
observes the current repository or environment and returns evidence bound to the record’s type
and scope. For developer intent, preference, or another user-owned choice that observation cannot
establish,Resolutionasks a targeted clarification question naming the disputed fact and its scope.
This route follows mixed-initiative clarification work [ 3, 17, 33]. Clarification is triggered by a
specific gap in authoritative evidence for an action premise. The resulting observation or response
must establish evidence for the same record and scope identified byAttribution.
Resolutionassigns each record one of three states:
𝜌(𝑟)∈{valid,defective,unresolved}.
A valid status indicates that the record’s value and current applicability are supported. A defective
status carries admissible evidence for correction. An unresolved status records the outstanding

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 11
evidence requirement. Let
𝐹={𝑟∈𝐷 + :𝜌(𝑟)=defective}, 𝑄 unres ={𝑟∈𝐷 + :𝜌(𝑟)=unresolved}.
Valid records retain their semantic values. Records in𝐹 proceed to Repair with corrective evidence,
while𝑄unres identifies premises that prevent execution. These explicit states connect the available
evidence to the subsequent repair and action-control decisions.
4.4 Persistent Repair and Action Control
The remaining challenges concern preserving corrections across tasks and checking action risks
after state repair. Persistent repair updates the premises available to future plans, and independent
action control assesses the operation produced from the repaired state.
Scoped Persistent Repair.Repair receives𝐹 and its corrective evidence. Typed evidence grounding
binds each confirmed correction to the attributed record, its semantic type, and the scope established
by the evidence. These bindings determine which active value the correction supersedes and where
the update applies. Repair then forms the admissible update 𝑈𝑖 ∈U 𝑖 defined in Section 3 and
produces𝑀′ 𝑖 =𝑈𝑖(𝑀𝑖).
Within each established repair scope, the update supersedes the defective active value and retains
the original record and corrective evidence as repair lineage. Active records outside those scopes
remain unchanged. This localized update draws on knowledge revision and memory lineage [14, 25–
27]. Scope binding preserves the correction’s applicability boundaries, while lineage retains the
basis for its update. When𝐹=∅, Repair makes no semantic update.
Replanning and Cross-Task Reuse.With the required premises resolved, the planner retrieves
context from𝑀′ 𝑖 and produces the revised proposal:
𝑎′ 𝑖,𝑡 =𝑃(𝑇 𝑖,𝑅(𝑀′ 𝑖,𝑇𝑖,𝑡)).
Replanning allows the corrected premise to change the operation, target, arguments, or stopping
decision. Writing the correction to persistent storage also makes it available to later tasks through
retrieval. Under the reset boundary in Section 3, this reuse survives the reset of conversation and
workspace because the corrected record is carried forward in the store.
Independent Action Control.A repaired premise can change action selection while other plan-
ning errors remain. The revised proposal therefore passes an independent state–action check. This
stage compares its arguments and scope with the resolved state, checks the hard invariants𝐻𝑖, and
applies ordinary permission requirements [11, 23, 35].
Let𝑆′𝑖,𝑡=𝑅(𝑀 ′ 𝑖,𝑇𝑖,𝑡) . Write Γ(𝑎′𝑖,𝑡,𝑆 ′𝑖,𝑡,𝐻 𝑖)= 1when the state–action, invariant, and permis-
sion checks pass. Execution requires
𝑄unres =∅ ∧Γ(𝑎 ′ 𝑖,𝑡,𝑆′ 𝑖,𝑡,𝐻𝑖)=1.
Any approval required by the permission policy must be obtained before execution. If a premise
remains unresolved or a check fails, StateWise returns an explicit safe stop. This final gate addresses
residual action risks and implements the action-admissibility requirement in Section 3.
5 Evaluation
Building on the pre-action recovery procedure, we evaluate whether StateWise improves task
correctness and action safety through verification and persistent repair of decision-critical records.
We examine the impact of erroneous persistent state, compare recovery with baseline interventions,
and assess the contribution of individual components. Beyond the current task, we evaluate whether
scoped corrections continue to support subsequent tasks and whether recovery remains effective

12 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
across state conditions and planner models. We further assess transfer across repository and tool
interfaces under supplied contracts. These objectives guide six research questions:
• RQ1: Impact of Erroneous State.How does changing one persistent record affect cor-
rectness and action safety under otherwise matched conditions?
• RQ2: Comparison with Baselines.How does StateWise compare with baseline interven-
tions that do not repair persistent state in terms of task correctness and action safety?
• RQ3: Effectiveness across State Conditions and Models.How effectively does StateWise
restore correct and safe task execution across different persistent-state conditions and
planner models?
• RQ4: Component Contributions.How do the individual components of StateWise con-
tribute to task recovery under erroneous persistent state?
• RQ5: Cross-Task Repair Reuse.To what extent can a persistent record repaired once by
StateWise support correct and safe execution across subsequent tasks?
• RQ6: Transfer across Interfaces.How well does StateWise generalize to unseen reposito-
ries, tool operations, state types, and their combinations under supplied interface contracts?
0 10 20 30 40
Cases
SW / Env. Dep.
SW / Filesystem
SW / Git Policy
SW / Config-Build
MemLineage
STALE
Ask-or-Assume
ClarEval
OpenAgentSafety
AgentDojo
Dialogue-SWEBench
OSGuard
MCP-SafetyBench
Persistent
State
Action
Link
Conflict
0
20
40
60
80
100Percent (%)
0 10 20 30 40 50
Cases
Stale
Wrong
Over-Gen.
Implicit
Scope
Joint
Runtime
Env.
Other
Env.
Git
Repo.
User
Settings
0
20
40
60
80Cases
0 10 20 30 40 50
Cases
Wrong Value
Stale Value
Over-Gen.
Conflict
Scope
0 25 50 75 100
Exact Agreement (%)
Behavior
Support Set
State Value
Behavior Support
Set
State
Value
0
25
50
75
100Exact Agreement (%)
Behavior Support
Set
State
Value
0.0
0.2
0.4
0.6
0.8
1.0Cohen’s κ
Fig. 4. Composition and annotation quality of the evaluation set. The top row summarizes case categories,
coverage of persistent state, action links and conflicts, state-issue types, and execution settings. The bottom
row shows defect types and annotator agreement on behavior, supporting evidence, and state values.
5.1 Experimental Setup and Metrics
Experimental Setup.As shown in Figure 4, we evaluate StateWise through executable coding
tasks, with the figure summarizing case sources, persistent-state types, and annotation results.
We use GPT-5.6-sol as the primary planner and additionally evaluate DeepSeek v4 Pro, Qwen 3.7
Max, and Claude Fable 5. We develop the StateWise pipeline on 40 cases and evaluate the finalized
pipeline on 150 primary cases, comprising 125 tasks that require an operation and 25 that require
a safe stop. The 150-case benchmark combines our designed coding cases with cases informed
by existing research on agent memory, clarification, and tool safety,covering runtime and other
environment state, Git repositories,and user settings, as shown in Figure 4. The agent plans from
the task and retrieved persistent records, and the intervention checks its proposal before execution.
Predefined outcome checks and safety constraints determine task correctness and action safety.
We use this set to compare correct, erroneous, and removed target records, assess component
contributions, and examine transfer to configurations not encountered during development. Within
each comparison, methods use the same cases, with task conditions and evaluation rules held fixed.

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 13
To extend baseline comparisons and examine different state defects, we construct two additional
150-case sets, each containing 105 operation tasks and 45 safe-stop tasks. One uses erroneous target
values, while the other retains correct values with defective supporting context. We also test all
four planners on the same cross-model case set and assess correction reuse through 32 four-task
sequences. Between tasks, conversation and workspace state are cleared, with only persistent
memory retained.
Metrics.To examine how recovery is achieved and sustained, we measure record-level attribution,
retrieval of repaired records, and safe completion of subsequent tasks. Finally, we quantify the
model, token, and interaction costs incurred during recovery. Table 1 summarizes these measures
and their preferred directions.
LetE be the set of valid episodes, partitioned intoE𝐴 for tasks that require an operation andE𝑆
for tasks that require a safe stop. Following Section 3,𝑦𝑒 =𝐽(𝑜 𝑒;𝑔𝑒,𝐻𝑒)∈{ 0, 1} indicates whether
episode𝑒 achieves the required outcome safely, and 𝑣𝑒 =𝑉(𝑜 𝑒;𝐻𝑒) ∈{0, 1} indicates a safety
violation. For subsequent retrieval contextsL,𝑧ℓ∈{ 0, 1} indicates whether the repaired record is
retrieved. For four-task sequencesQ,𝑦𝑞,𝑗∈{ 0, 1} indicates correct and safe completion of task𝑗
in sequence𝑞. Attribution counts true positives𝑇𝑃 , false positives𝐹𝑃 , and false negatives𝐹𝑁 at
the record level. For each episode,𝑚𝑒,𝑡𝑒, and𝑢𝑒 count model calls, tokens, and user interactions,
respectively. Cost totals include unsuccessful episodes and are normalized either per episode, with
𝑏=|E|, or per correct and safe outcome, with𝑏= ˝ 𝑒∈E 𝑦𝑒.
Table 1. Evaluation metrics for task outcomes, attribution, cross-task reuse, and cost.
Metric Definition Goal
OC(Overall correctness) Correct and safe outcomes across all episodes:
˝
𝑒∈E 𝑦𝑒
|E| .↑
AC(Act completion) Correct and safe completion of tasks requiring an operation:
˝
𝑒∈E𝐴 𝑦𝑒
|E𝐴| .↑
CS(Correct stop) Correct and safe stopping for tasks requiring a stop:
˝
𝑒∈E𝑆 𝑦𝑒
|E𝑆| .↑
UAR(Unsafe action rate) Episodes with at least one safety violation:
˝
𝑒∈E 𝑣𝑒
|E| .↓
AP,AR,AF1(Attribution
precision, recall, and F1)
Record-level precision, recall, and their harmonic mean:AP= 𝑇𝑃 𝑇𝑃+𝐹𝑃 ,
AR= 𝑇𝑃 𝑇𝑃+𝐹𝑁 ,AF1= 2AP AR AP+AR .
↑
RR(Repair retrieval) Subsequent contexts retrieving the repaired record:
˝
ℓ∈L 𝑧ℓ
|L| .↑
AFS(All-future safe) Sequences with all subsequent tasks correct and safe:
˝
𝑞∈Q
˛4
𝑗=2𝑦𝑞,𝑗
|Q| .↑
MC,TC,IC(Model, token,
and interaction cost)
Model calls, thousands of tokens, and user interactions: MC=
˝
𝑒∈E 𝑚𝑒
𝑏 ,
TC=
˝
𝑒∈E 𝑡𝑒
1000𝑏 ,IC=
˝
𝑒∈E 𝑢𝑒
𝑏 .
↓
5.2 RQ1: Impact of Erroneous State
We first examine whether an error in a single target memory record can change the agent’s
execution outcome. On the primary 150-case evaluation, we compare correct, corrupted, and
removed target memory. The correct and corrupted conditions differ only in the target memory
record. All other records, task requirements, initial workspace state, outcome checks, and safety
constraints remain fixed to isolate the effect of that error. Removing the target memory tests
whether eliminating misleading information restores performance or also removes information
needed for task completion. We compare these conditions using OC, AC, and UAR. The three panels
in Figure 5 report these metrics in order. This question focuses on conditions 1–3: correct target
memory, corrupted target memory, and removed target memory. Comparing 1 with 2 reveals the
effect of the error, while comparing 2 with 3 tests whether removal is sufficient for recovery.

14 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩
0
20
40
60
80
100OC (%)
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩
0
20
40
60
80
100AC (%)
① ② ③ ④ ⑤ ⑥ ⑦ ⑧ ⑨ ⑩
0
20
40
60
80
100UAR (%)
① Correct Memory
② Corrupted Memory
③ No Memory
④ Bare Approval
⑤ Rationale Approval
⑥ Clarification
⑦ MemLineage
⑧ Safety Sentry
⑨ Ask-or-Assume
⑩ StateWise
Fig. 5. OC, AC, and UAR under three memory conditions, three common intervention strategies, baselines
from prior work, and our method. Memory conditions include correct, corrupted, and removed target memory.
Simple interventions include bare approval, approval with an action rationale, and clarification. Baselines
include MemLineage [27], Safety Sentry [11], and Ask-or-Assume [17].
Under matched conditions, corrupting only the target memory reduces OC from 80.7% to 38.7%
and AC from 76.8% to 27.2%. UAR rises from 0.0% to 42.7%. These changes show that a single
erroneous target memory record can substantially impair task performance and induce unsafe
actions, even when the remaining memory and execution conditions are unchanged. The results
provide controlled evidence consistent with the failure chain described in Section 3: an erroneous
persistent premise can affect action selection and the resulting outcome.
Removing the target memory yields only a modest improvement, with OC reaching 45.3% and
AC reaching 35.2%. Both remain much closer to the corrupted-memory condition than to correct
memory, where OC is 80.7% and AC is 76.8%. Although UAR falls to 9.3%, avoiding misleading
information does little to restore task completion when the relevant historical information is also
lost. This contrast highlights the value of recovering a valid planning premise: StateWise achieves
93.3% OC and 92.8% AC from erroneous memory, with no observed unsafe action.
Answer to RQ1.Errors in target memory undermine both task completion and action safety. Removing
that memory reduces harm but leaves the agent without information needed to complete the task. These
findings motivate recovery at the level of persistent planning premises, where erroneous information is
replaced with verified evidence to support correct and safe execution.
5.3 RQ2: Comparison with Baselines
We next examine whether existing interventions can close this gap, comparing their OC, AC,
and UAR with StateWise. Common engineering strategies include Bare Approval, which requests
approval for the proposed action, Rationale Approval, which also explains the action’s rationale,
and Clarification, which asks for additional information before proceeding. Baselines from existing
approaches include MemLineage [27], which screens memory using provenance and lineage, Safety
Sentry [11], which intervenes based on action risk, and Ask-or-Assume [17], which uses uncertainty
to decide whether to ask or proceed. We also compare CRITIC [18], which uses external tool feedback
to evaluate and correct outputs, to examine whether tool-supported self-correction can recover
from erroneous target memory. Finally, we include Live Refresh as a simple approach to obtaining
current information. The agent is explicitly prompted to inspect the current workspace and refresh
relevant information, while choosing when and what to inspect. Figure 6 compares the OC and
UAR of these interventions with those of StateWise under erroneous target memory.

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 15
0 25 50 75 100
OC (%)
Base
Ask-or-Assume
CRITIC
MemLineage
Safety Sentry
Live Refresh
StateWise
0 25 50 75 100
UAR (%)
Base
Ask-or-Assume
CRITIC
MemLineage
Safety Sentry
Live Refresh
StateWise
Fig. 6. OC and UAR for StateWise and baseline interventions
under erroneous target memory.
Bare Approval and Rationale Ap-
proval produce no observed unsafe
action, but their AC is only 23.2% and
29.6%, with OC of 36.0% and 40.7%, re-
spectively. These common engineer-
ing strategies protect the workspace
by withholding operations, yet leave
substantial task-completion gaps.
Figure 6 compares these strategies
with the baselines. CRITIC achieves 48.0% OC with 28.0% UAR, indicating limited recovery through
tool feedback. Safety Sentry reduces UAR to 4.7%, but AC remains at 3.9%. StateWise achieves
88.7% OC, 84.8% AC, and 0.0% UAR. Within the shared experimental setting, these results support
verifying and repairing planning premises to improve both task completion and action safety.
Live Refresh performs a refresh in 105 of 150 episodes, achieving 42.0% OC and 15.3% UAR.
Even with an explicit reminder, refresh remains selective and recovery is limited, suggesting that
obtaining current information must be accompanied by identifying and revising the relevant
planning premises. StateWise makes this verification and repair explicit, while retaining corrections
for subsequent tasks.
Answer to RQ2.Common interventions and baselines from related work reduce some risks but leave
substantial task-completion gaps. StateWise achieves the highest OC and AC in the shared comparison,
with no observed unsafe action.
5.4 RQ3: Recovery Across Settings
We evaluate how effectively StateWise restores correct and safe task execution under different
persistent-state conditions and with different planning models. Figure 7 presents the cross-model
results in terms of OC and AC.
① ② ③ ④0
25
50
75
100OC (%)
① = GPT-5.6-sol
② = DeepSeek v4
③ = Qwen 3.7
④ = Claude Fable 5
① ② ③ ④0
25
50
75
100AC (%)
① = GPT-5.6-sol
② = DeepSeek v4
③ = Qwen 3.7
④ = Claude Fable 5
Fig. 7. OC and AC across four planning models on a separate
20-case evaluation set.
Under erroneous target memory,
StateWise achieves 93.3% OC and
92.8% AC on the primary 150-case
evaluation. When the target value is
correct but its freshness, provenance,
or supporting context is defective, it
achieves 88.0% OC and 82.9% AC. Nei-
ther setting produces an observed un-
safe action. These results support re-
covery from both incorrect values
and defects in the evidence support-
ing their current use.
For cross-model validation, figure 7 shows OC ranging from 80.0% to 94.4% and AC from 69.2% to
90.9%, with no observed unsafe action under any model. Task completion varies with the planner,
but the same procedure supports correct and safe recovery across all four tested models.
Answer to RQ3.StateWise supports correct and safe task execution under both erroneous target values
and defective supporting context. The unchanged recovery procedure also operates across four planning
models, achieving 80.0%–94.4% OC with no safety violations across the episodes.

16 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
5.5 RQ4: Component Contributions
To understand how StateWise achieves recovery, we remove one component at a time on the same
150 primary cases. Figure 8 compares the resulting OC and AC with those of the full pipeline.
0 25 50 75 100
OC (%)
Full StateWise
w/o Attribution
w/o Resolution
w/o Persistent Repair
w/o Typed Grounding
w/o Replanning
w/o Residual Gate
0 25 50 75 100
AC (%)
Full StateWise
w/o Attribution
w/o Resolution
w/o Persistent Repair
w/o Typed Grounding
w/o Replanning
w/o Residual Gate
Fig. 8. OC and AC of the full StateWise pipeline and six ablation vari-
ants on the same 150 cases.
RemovingResolutionorPer-
sistent Repairlowers OC by
78.7 and 76.7 percentage points,
respectively, and reduces AC
to zero. These losses highlight
the importance of establishing
evidence-supported corrections
and making them available to
planning, as described in Sec-
tions 4.3. Avoiding unsafe execution alone does not restore task completion.
RemovingAttributionlowers OC by 53.3 percentage points. Because this variant also disables
downstream state intervention, the loss reflects the combined contribution of that path. Removing
Typed Groundinglowers OC by 27.3 percentage points, showing the importance of binding evidence
to the appropriate record type and action scope. The losses from these four ablations remain
significant after Holm correction across the six comparisons.
RemovingReplanningor theResidual Gatelowers OC by 2.7 percentage points each. These stages
complete the recovery process by translating repaired state into a revised action and checking that
action before execution. Their smaller effects complement the larger gains from premise verification
and repair, indicating that the main recovery benefit comes from correcting the state on which the
agent plans.
Answer to RQ4.The ablations support StateWise’s integrated recovery pipeline:Attributionlocates
influential premises,ResolutionandTyped Groundingestablish applicable evidence,Persistent Repair
preserves corrections, andReplanningand theResidual Gateturn repaired state into a checked action.
5.6 RQ5: Cross-Task Persistence
We examine whether a correction made by StateWise continues to support subsequent tasks using
32 four-task sequences. T1 can trigger repair, while T2–T4 test correction reuse. Between tasks,
conversation and workspace state are reset under the boundary in Section 3, with only the persistent
store retained. Table 2 reports task outcomes and AFS.
Table 2. Correct and safe task outcomes and AFS across
four-task sequences (%).
Method T1 T2–T4 AFS
Correct Memory 93.8 91.7 87.5
Corrupted Memory 0.0 1.0 0.0
No Memory 0.0 0.0 0.0
MemLineage 0.0 1.0 0.0
Safety Sentry 0.0 2.1 0.0
Ask-or-Assume 9.4 6.2 3.1
StateWise 90.6 92.7 90.6
Starting from erroneous memory, StateWise
achieves 92.7% correct and safe completion
across subsequent tasks and 90.6% AFS, reach-
ing the level of the correct-memory refer-
ence, which achieves 91.7% and 87.5%, respec-
tively. RR reaches 97.9%, showing that repaired
records remain available to later planning even
after transient context is cleared.
The tested baselines do not explicitly pre-
serve verified corrections for subsequent reuse.
Their later-task completion rates remain at
1.0%–6.2%, with AFS no higher than 3.1%, of-
fering little sustained improvement over cor-
rupted memory.

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 17
Answer to RQ5.Starting from erroneous memory, StateWise achieves90.6% AFSand 92.7% correct and
safe completion across subsequent tasks, reaching the performance level of the correct-memory reference.
Persistent repair allows the benefit of an initial correction to carry forward across the evaluated task
sequence.
5.7 RQ6: Transfer Across Interfaces
We examine whether StateWise maintains its recovery performance on repositories, tool opera-
tions, and state types not encountered during development. After finalizing the recovery method
on 40 development cases, we identify both seen and unseen configurations within the 150-case
evaluation set and compare their respective recovery outcomes using consistent evaluation criteria.
Seen
Any UnseenFully UnseenNew ReposNew ToolsNew States
0
25
50
75
100OC (%)
(a) OC
Seen
Any UnseenFully UnseenNew ReposNew ToolsNew States
0
25
50
75
100AC (%) (b) AC
Repositories
Tool Operations
State TypesState–Action
0
10
20
30
40
50
60
Distinct Interface
Units
Seen Unseen
(c) Interface Coverage
Seen
Any UnseenFully UnseenNew ReposNew ToolsNew States
0
20
40
60
80
100Rate (%)
Supported (d) Support and Safety
Fig. 9. Recovery across seen and unseen configurations
with an unchanged StateWise core and supplied inter-
face contracts. Panels report OC, AC, distinct interface
units, contract support, and UAR.
Figure 9 summarizes the configuration differ-
ences and transfer results.
The evaluation introduces 8 repositories, 2
tool operations, 6 semantic state types, and
54 state–action combinations not encountered
during development. Each combination com-
prises a state key, tool operation, scope, and
verifier source. Of the 150 cases, 106 contain
unseen configurations, including new individ-
ual units.
On these 106 cases, StateWise achieves 93.4%
OC and 92.6% AC, with zero UAR, compared
with 93.2% OC on seen configurations. It also
achieves 95.1% OC on cases involving new state
types and 98.4% on those involving new repos-
itories. These results indicate that recovery
remains effective across the tested interface
changes, allowing the same procedure to be
reused through the corresponding interface
contracts.
Answer to RQ6.StateWise achieves 93.4% OC and 92.6% AC on unseen configurations, with zero UAR
and OC comparable to that on seen configurations. These results support reuse across the tested
repositories, tool operations, and state types through supplied interface contracts, without modifying the
core recovery procedure.
6 Discussion
The evaluation results motivate treating persistent-state recovery as part of reliable agent execution.
We discuss how its benefits extend across successive tasks, how StateWise connects record-level
action dependence with evidence-supported persistent updates, and how verification and scope
requirements shape its practical applicability.
State Validity and Task Continuity.The paired tests show that a single erroneous record can
impair both task correctness and action safety. The baseline comparisons distinguish suppressing
unsafe operations from restoring task capability, while ablations identify validity resolution, typed
grounding, and persistent repair as major contributors to recovery. The four-task sequences further
show that confirmed corrections remain useful after conversation and workspace resets. This

18 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
reset boundary makes persistent memory the channel through which corrections reach subsequent
planning contexts. These findings motivate treating operational-state maintenance as part of reliable
execution: applicable premises support the current task, and persistent corrections preserve their
usefulness for subsequent decisions.
Connecting Actions, Evidence, and Persistent Updates.StateWise’s technical contribution is
the correspondence it maintains among an action’s supporting records, evidence of their current
validity, and scoped persistent corrections. Constrained counterfactual replanning provides evidence
of decision dependence, making the proposed action a focused target for state diagnosis. The record’s
type and authority then determine how its validity is resolved, and typed evidence grounding
binds the resulting correction to the same record and its established scope. This binding specifies
which active value is superseded and which unrelated records must remain unchanged. Persistent
writeback retains this correction and its lineage for current replanning and later retrieval. This
connection turns action-triggered verification into reusable state maintenance. An independent
state–action check assesses the revised operation against the verified state and execution constraints.
Evidence and Scope Boundaries.Applicability depends on explicit record–action bindings,
accessible authoritative evidence, and established repair scopes for persistent updates. These
requirements fit recurring coding workflows involving inspectable runtime and workspace state,
verifiable repository policies, and developer-owned choices that can be resolved through targeted
clarification. For example, environment changes and repository policy updates can invalidate stored
records that guide repeated coding tasks. The transfer results support extending this structure
through supplied interface contracts and corresponding verifier adapters.
The audit relies on model annotation and mainly covers one agent family. Executable evaluations
use controlled single-record defects, simulated developer responses, a limited cross-model set, and
four-task sequences. Longer deployed studies with independent human annotation should examine
interacting records, conflicting corrections, and partial evidence. Extension to external services and
collaborative agents additionally requires broader verifier coverage and mechanisms for resolving
changing authority and overlapping scopes.
7 Conclusion
In this work, we studied how invalid persistent operational records influence coding-agent decisions
and proposed StateWise for pre-action diagnosis and recovery. The framework connects action attri-
bution, current-validity verification, and scoped persistent repair with replanning and independent
action checks, preserving confirmed corrections for later tasks. On the primary 150-case benchmark,
StateWise achieves 93.3% overall correctness under corrupted persistent state, compared with 38.7%
for the baseline, with no unsafe actions observed. This work addresses a gap between intervening
in the current action and correcting the persistent premise that guides subsequent decisions. An
invalid record can survive a blocked operation or a locally corrected decision and continue to influ-
ence later plans. StateWise makes the corresponding record and its applicable scope explicit targets
of evidence-supported recovery. These findings connect agent-memory research with planning and
action safety through the validity of operational premises. They motivate evaluating operational
memory through its current applicability, influence on actions, and reuse of verified corrections,
and integrating state maintenance into the execution architecture of agents operating across tasks
and changing environments.
Data Availability
Workbooks, run manifests, case definitions, per-episode audit bundles, and source code are available
in the artifact repository.

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 19
References
[1] Sahar Abdelnabi, Kai Greshake, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario Fritz. 2023. Not What
You’ve Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection. In
Proceedings of the 16th ACM Workshop on Artificial Intelligence and Security (AISec). 79–90. doi:10.1145/3605764.3623985
[2] Ahmad Al-Tawaha, Shangding Gu, Peizhi Niu, Ruoxi Jia, and Ming Jin. 2026. Remembering More, Risking More:
Longitudinal Safety Risks in Memory-Equipped LLM Agents. arXiv:2605.17830
[3] Mohammad Aliannejadi, Hamed Zamani, Fabio Crestani, and W. Bruce Croft. 2019. Asking Clarifying Questions in
Open-Domain Information-Seeking Conversations. InProceedings of the 42nd International ACM SIGIR Conference on
Research and Development in Information Retrieval (SIGIR).
[4] Saleema Amershi, Dan S. Weld, Mihaela Vorvoreanu, Adam Fourney, Besmira Nushi, Penny Collisson, Jina Suh,
Shamsi T. Iqbal, Paul N. Bennett, Kori Inkpen, Jaime Teevan, Ruth Kikin-Gil, and Eric Horvitz. 2019. Guidelines for
Human-AI Interaction. InProceedings of the SIGCHI Conference on Human Factors in Computing Systems (CHI). ACM.
[5] Joachim Baumann, Vishakh Padmakumar, Xiang Li, John Yang, Diyi Yang, and Sanmi Koyejo. 2026. SWE-chat: Coding
Agent Interactions From Real Users in the Wild. arXiv:2604.20779
[6] Zana Buçinca, Maja Barbara Malaya, and Krzysztof Z. Gajos. 2021. To Trust or to Think: Cognitive Forcing Functions
Can Reduce Overreliance on AI in AI-Assisted Decision-Making.Proceedings of the ACM on Human-Computer
Interaction (CSCW)5 (2021).
[7] Christoph Bühler, Matteo Biagiola, Luca Di Grazia, and Guido Salvaneschi. 2026. AgentBound: Securing Execution
Boundaries of AI Agents.Proceedings of the ACM on Software Engineering3, FSE (2026), 2141–2164. doi:10.1145/3808103
[8] Yuandao Cai, Wensheng Tang, Cheng Wen, and Shengchao Qin. 2026. Ghost in the Agent: Redefining Information
Flow Tracking for LLM Agents. arXiv:2604.23374
[9] Hanxiang Chao, Yihan Bai, Rui Sheng, Tianle Li, and Yushi Sun. 2026. STALE: Can LLM Agents Know When Their
Memories Are No Longer Valid? arXiv:2605.06527
[10] Jiahao Chen, Zhou Feng, Oubo Ma, Yichen Yan, Ruixiao Lin, Hangtao Zhang, Linkang Du, Hengyu An, Yong Yang,
Jun Liu, et al. 2026. Safety in Self-Evolving Agents: A Survey. (2026). Preprint.
[11] Tianyu Chen, Chujia Hu, and Wenjie Wang. 2026. Safety Sentry: Context-Aware Human Intervention via EXECUTE-
ASK-REFUSE Routing. arXiv:2607.13594
[12] Wenhu Chen, Xinyi Wang, and William Yang Wang. 2021. A Dataset for Answering Time-Sensitive Questions. In
Advances in Neural Information Processing Systems (NeurIPS) Datasets and Benchmarks Track.
[13] Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, and Deshraj Yadav. 2025. Mem0: Building Production-
Ready AI Agents with Scalable Long-Term Memory. InECAI 2025. doi:10.3233/FAIA251160
[14] Nicola De Cao, Wilker Aziz, and Ivan Titov. 2021. Editing Factual Knowledge in Language Models. InProceedings of
the 2021 Conference on Empirical Methods in Natural Language Processing (EMNLP).
[15] Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, and Florian Tramèr. 2024.
AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents. InAdvances
in Neural Information Processing Systems (NeurIPS).
[16] Bhuwan Dhingra, Jeremy R. Cole, Julian Martin Eisenschlos, Daniel Gillick, Jacob Eisenstein, and William W. Cohen.
2022. Time-Aware Language Models as Temporal Knowledge Bases.Transactions of the Association for Computational
Linguistics (TACL)10 (2022).
[17] Nicholas Edwards and Sebastian Schuster. 2026. Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding
Agents. arXiv:2603.26233
[18] Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, and Weizhu Chen. 2024. CRITIC:
Large Language Models Can Self-Correct with Tool-Interactive Critiquing. InInternational Conference on Learning
Representations (ICLR).
[19] Eric Horvitz. 1999. Principles of Mixed-Initiative User Interfaces. InProceedings of the SIGCHI Conference on Human
Factors in Computing Systems (CHI). ACM.
[20] Brittany Johnson, Yoonki Song, Emerson R. Murphy-Hill, and Robert W. Bowdidge. 2013. Why Don’t Software
Developers Use Static Analysis Tools to Find Bugs?. InProceedings of the 35th International Conference on Software
Engineering (ICSE).
[21] Jungo Kasai, Keisuke Sakaguchi, Yoichi Takahashi, Ronan Le Bras, Akari Asai, Xinyan Yu, Dragomir Radev, Noah A.
Smith, Yejin Choi, and Kentaro Inui. 2023. RealTime QA: What’s the Answer Right Now?. InAdvances in Neural
Information Processing Systems (NeurIPS).
[22] John D. Lee and Katrina A. See. 2004. Trust in Automation: Designing for Appropriate Reliance.Human Factors46, 1
(2004).
[23] Peiyang Li, Songping Wang, Yi Huang, Yanhua Shi, Chenhao Zhang, Qi Li, Yueming Lyu, Caifeng Shan, Fengting Li,
Chao Feng, Chuanqun Zhu, and Liang Chen. 2026. AgentCanary: A Security Evaluation Framework for Autonomous
AI Agents in Real Executable Environments. arXiv:2606.10484

20 Yongyuan Peng, Zhou Feng, Tongying Wu, Jiahao Chen, Yuan Su, Chunyi Zhou, Tianyu Du, and Shouling Ji
[24] Adyasha Maharana, Dong-Ho Lee, Sergey Tulyakov, Mohit Bansal, Francesco Barbieri, and Yuwei Fang. 2024. Evaluating
Very Long-Term Conversational Memory of LLM Agents. InProceedings of the 62nd Annual Meeting of the Association
for Computational Linguistics (ACL).
[25] Kevin Meng, David Bau, Alex Andonian, and Yonatan Belinkov. 2022. Locating and Editing Factual Associations in
GPT. InAdvances in Neural Information Processing Systems (NeurIPS).
[26] Eric Mitchell, Charles Lin, Antoine Bosselut, Chelsea Finn, and Christopher D. Manning. 2022. Fast Model Editing at
Scale. InInternational Conference on Learning Representations (ICLR).
[27] Ciyan Ouyang and Rui Hou. 2026. MemLineage: Lineage-Guided Enforcement for LLM Agent Memory.
arXiv:2605.14421
[28] Charles Packer, Vivian Fang, Shishir G. Patil, Kevin Lin, Sarah Wooders, and Joseph E. Gonzalez. 2023. MemGPT:
Towards LLMs as Operating Systems. arXiv:2310.08560
[29] Raja Parasuraman and Victor Riley. 1997. Humans and Automation: Use, Misuse, Disuse, Abuse.Human Factors39, 2
(1997).
[30] Joon Sung Park, Joseph C. O’Brien, Carrie J. Cai, Meredith Ringel Morris, Percy Liang, and Michael S. Bernstein. 2023.
Generative Agents: Interactive Simulacra of Human Behavior. InProceedings of the 36th Annual ACM Symposium on
User Interface Software and Technology (UIST). ACM.
[31] Vedant Patel. 2026. Supersede: Diagnosing and Training the Memory-Update Gap in LLM Agents. arXiv:2606.27472
[32] Chen Qian, Peng Wang, Dongrui Liu, Junyao Yang, Dadi Guo, Ling Tang, Jilin Mei, Qihan Ren, Shuai Shao, Yong Liu,
Jie Fu, Jing Shao, and Xia Hu. 2026. The Why Behind the Action: Unveiling Internal Drivers via Agentic Attribution.
arXiv:2601.15075
[33] Sudha Rao and Hal Daumé III. 2018. Learning to Ask Good Questions: Ranking Clarification Questions Using Neural
Expected Value of Perfect Information. InProceedings of the 56th Annual Meeting of the Association for Computational
Linguistics (ACL).
[34] Allen Z. Ren, Anushri Dixit, Alexandra Bodrova, Sumeet Singh, Stephen Tu, Noah Brown, Peng Xu, Leila Takayama,
Fei Xia, Jake Varley, Zhenjia Xu, Dorsa Sadigh, Andy Zeng, and Anirudha Majumdar. 2023. Robots That Ask For Help:
Uncertainty Alignment for Large Language Model Planners. InProceedings of The 7th Conference on Robot Learning
(Proceedings of Machine Learning Research, Vol. 229). 661–682.
[35] Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison,
and Tatsunori Hashimoto. 2024. Identifying the Risks of LM Agents with an LM-Emulated Sandbox. InInternational
Conference on Learning Representations (ICLR).
[36] Caitlin Sadowski, Edward Aftandilian, Alex Eagle, Liam Miller-Cushon, and Ciera Jaspan. 2018. Lessons from Building
Static Analysis Tools at Google.Commun. ACM61, 4 (2018).
[37] Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro, Luke Zettlemoyer, Nicola
Cancedda, and Thomas Scialom. 2023. Toolformer: Language Models Can Teach Themselves to Use Tools. InAdvances
in Neural Information Processing Systems (NeurIPS).
[38] Yining She, Yiliang Liang, and Eunsuk Kang. 2026. Safeguarding LLM Agents from Misalignment through Provenance
Analysis. arXiv:2607.01236
[39] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao. 2023. Reflexion: Language
Agents with Verbal Reinforcement Learning. InAdvances in Neural Information Processing Systems (NeurIPS).
[40] Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, and Thomas L. Griffiths. 2024. Cognitive Architectures for
Language Agents.Transactions on Machine Learning Research (TMLR)(2024).
[41] Md Nayem Uddin, Kumar Shubham, Eduardo Blanco, Chitta Baral, and Gengyu Wang. 2026. From Recall to Forgetting:
Benchmarking Long-Term Memory for Personalized Agents. InFindings of the Association for Computational Linguistics
(ACL). Association for Computational Linguistics, 26814–26841. doi:10.18653/v1/2026.findings-acl.1337
[42] Tu Vu, Mohit Iyyer, Xuezhi Wang, Noah Constant, Jerry W. Wei, Jason Wei, Chris Tar, Yun-Hsuan Sung, Denny Zhou,
Quoc Le, and Thang Luong. 2024. FreshLLMs: Refreshing Large Language Models with Search Engine Augmentation.
InFindings of the Association for Computational Linguistics (ACL).
[43] Xingyao Wang, Yangyi Chen, Lifan Yuan, Yizhe Zhang, Yunzhu Li, Hao Peng, and Heng Ji. 2024. Executable Code
Actions Elicit Better LLM Agents. InProceedings of the 41st International Conference on Machine Learning (ICML).
[44] Xingyao Wang, Boxuan Li, Yufan Song, Frank F. Xu, Xiangru Tang, Mingchen Zhuge, Jiayi Pan, Yueqi Song, Bowen Li,
Jaskirat Singh, Hoang H. Tran, Fuqiang Li, Ren Ma, Mingzhang Zheng, Bill Qian, Yanjun Shao, Niklas Muennighoff,
Yizhe Zhang, Binyuan Hui, Junyang Lin, Robert Brennan, Hao Peng, Heng Ji, and Graham Neubig. 2025. OpenHands: An
Open Platform for AI Software Developers as Generalist Agents. InInternational Conference on Learning Representations
(ICLR).
[45] Di Wu, Hongwei Wang, Wenhao Yu, Yuwei Zhang, Kai-Wei Chang, and Dong Yu. 2025. LongMemEval: Benchmarking
Chat Assistants on Long-Term Interactive Memory. InInternational Conference on Learning Representations (ICLR).

StateWise: Diagnosing and Repairing Persistent Operational State Before Agent Actions 21
[46] Wujiang Xu, Zujie Liang, Kai Mei, Hang Gao, Juntao Tan, and Yongfeng Zhang. 2025. A-Mem: Agentic Memory for
LLM Agents. InAdvances in Neural Information Processing Systems (NeurIPS).
[47] Neeraj Yadav. 2026. Temporal Validity in Retrieval Memory: Eliminating Stale-Fact Errors for AI Agents over Evolving
Knowledge. arXiv:2606.26511
[48] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik Narasimhan, and Ofir Press. 2024.
SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. InAdvances in Neural Information
Processing Systems (NeurIPS).
[49] Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, and Yuan Cao. 2023. ReAct: Synergizing
Reasoning and Acting in Language Models. InInternational Conference on Learning Representations (ICLR).
[50] Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang. 2024. InjecAgent: Benchmarking Indirect Prompt Injections
in Tool-Integrated Large Language Model Agents. InFindings of the Association for Computational Linguistics (ACL).
Association for Computational Linguistics, 10471–10506. doi:10.18653/V1/2024.FINDINGS-ACL.624
[51] Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, and Gao Huang. 2024. ExpeL: LLM Agents Are
Experiential Learners. InProceedings of the AAAI Conference on Artificial Intelligence.
[52] Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, and Yanlin Wang. 2024. MemoryBank: Enhancing Large Language
Models with Long-Term Memory. InProceedings of the AAAI Conference on Artificial Intelligence.
[53] Zexuan Zhong, Zhengxuan Wu, Christopher D. Manning, Christopher Potts, and Danqi Chen. 2023. MQuAKE:
Assessing Knowledge Editing in Language Models via Multi-Hop Questions. InProceedings of the 2023 Conference on
Empirical Methods in Natural Language Processing (EMNLP).
