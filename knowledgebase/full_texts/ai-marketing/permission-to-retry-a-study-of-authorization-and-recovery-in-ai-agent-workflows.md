---
title: 'Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows'
url: https://arxiv.org/abs/2610.31916
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Deekshith Marla
- Kushagra Bhatnagar
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.31916
pages: 7
chars: 24416
fetched_at: '2026-11-08T13:35:48+00:00'
kb_version: 1
---

# Permission to Retry: A Study of Authorization and Recovery in AI Agent Workflows

23 October 2026
Permission to Retry:
A Study of Authorization and Recovery
in AI Agent Workflows
Deekshith Marla Kushagra Bhatnagar
Arya.ai
ABSTRACT
A durable agent can resume a consequential action while its authority changes and the action’s external outcome remains
uncertain. We study execution-time reliability of tool-using AI agents, isolating recovery decisions from language-model
behavior. Checkpoint state, permission to dispatch, evidence of an external effect and permission to reconcile are distinct
obligations. We present a finite conformance study that checks these obligations through histories scored against a provider
effect ledger hidden from the recovering application. A prospectively frozen campaign executes 336 histories on native
LangGraph and Temporal hosts, crossing 14 schedules, three provider contracts and four matched application policies. All
168 paired host cells have identical checked outcomes. Per host, retained-ledger reconciliation passes all 42 histories: 21
checked completions, 15 denials and six unknown outcomes with reservations retained. Cached retry, revalidation before
retry and stable-key retry pass 30, 36 and 31 histories respectively. A separate 16-case component study of InfinityOS,
an enterprise AI platform developed by Arya.ai, exercises exported authority, worker, recovery and settlement code over
repository fakes. The results isolate the roles of current authority, provider contracts and retained observations in recovery,
with safety, completion and unresolved obligations reported separately for the declared application profile.
Keywords:AI agent reliability; tool use; authorization; durable execution; recovery; uncertain outcomes.
1 Introduction
Consider a refund for an approved recipient and amount.
The service commits the refund, but the acknowledgement
disappears. Before a replacement worker resumes, the ini-
tiating principal loses write permission. Repeating the re-
quest can create a duplicate; treating a missing acknowl-
edgement as proof of failure can release an obligation pre-
maturely; abandoning every continuation can prevent legit-
imate recovery. Recovering evidence of an existing effect
and obtaining authority for a new dispatch are separate de-
cisions.
For a tool-using AI agent, resuming a workflow requires
deciding what actions remain permitted and what can be
concluded from earlier observations. We isolate this execu-
tion layer to examine how changing authority and uncertain
tool outcomes affect recovery.
This is a distributed execution problem with established
foundations. Fault-tolerant workflows already separate
durable state from external effects [8]. Agent research di-
rectly addresses semantic replay, consumed authority and
uncertain outcomes [1, 2, 3, 6]. These foundations moti-
vate evaluating their composition at agent recovery bound-
aries. The practical question is which obligations an appli-
cation preserves at each recovery boundary, under an ex-
plicit provider contract.
We study three questions. RQ1: Which configured recov-
ery policies preserve the declared safety conditions while
completing legitimate work? RQ2: Do paired applications
on two independently maintained execution hosts differ un-
der the same policy facts and provider schedules? RQ3:
How does the location of a confirmed observation relative
to settlement change recoverability?
Our contribution is a bounded conformance artifact and
its measured application: a history specification separat-
ing admission, effects and settlement; a prospective native-
host campaign; and a separately qualified InfinityOS com-
ponent case study. The evaluation record preserves raw ob-
servations, exact versions and data digests, with a recon-
struction checker and explicit exclusions. The policies are
authored ablations, not framework defaults or independent
implementations of published security protocols. Paired
host outcomes are reported alongside policy differences and
progress measures.
1
arXiv:2610.31916v1  [cs.AI]  22 Oct 2026

Permission to Retry Arya.ai
2 Related work and contribution boundary
AID-Guard connects authorization to provider commitment
and conservative ambiguity handling [1]. CapLease con-
serves token-independent authorization instances and quali-
fies effect guarantees by the sink contract [2]. Both provide
foundations for studying authorization across retries and re-
covery. LIMBO uses controlled tool faults and independent
effects to evaluate recovery across harnesses [3], establish-
ing the importance of fault injection and effect-side scoring.
ACRFence identifies semantic rollback and authority res-
urrection, and distinguishes its validated attacks from a pro-
posed mitigation not yet implemented in that evaluation [6].
ZeroGate separates exact admission from full lifecycle cost
and makes freshness assumptions explicit [4]. Matoi sep-
arates reusable evidence, current authority and occurrence
history [5]. ResidualAuth studies which authorization his-
tory must remain distinguishable under revocable delegation
[7].
We study matched application controls on native persis-
tence/retry hosts, checked at declared authority and obser-
vation boundaries. We did not obtain a qualified licensed
executable implementation of the closest security protocols
from the inspected papers. Their absence is not scored as
failure, and our controls are not attributed to their authors.
LangGraph persistence [9] and Temporal retry semantics
[10] are execution mechanisms consumed by the applica-
tion, not security baselines.
3 Model and conformance contract
An authorization instance binds an organisation/principal
scope, a canonical action, a policy epoch, expiry and an
allowed effect count. It is distinct from a transport key,
worker lease and checkpoint identifier. This campaign uses
one synthetic refund and a one-effect allowance per history.
Proposals and approvals are scripted facts, not real human
attestations or model outputs.
The history contains worker claims, authority events, ad-
missions, dispatches, provider effects, participant observa-
tions, settlements, reservation snapshots and terminal dec-
larations. The scheduler owns provider truth and exposes
only declared send/lookup responses. The checker im-
ports neither application controls nor InfinityOS admis-
sion/recovery predicates. It reconstructs scope and fresh-
ness, approval consumption, worker ownership, effect mul-
tiplicity, retained uncertainty, settlement evidence and truth-
ful completion.
At the initial local admission boundary, the scope, action,
grant and approval must be current. For a repeated dispatch,
this benchmark additionally requires current write authority
and either a live stable-key deduplication contract or certi-
fied predecessor closure. This repeat-freshness rule is ex-
plicit. A protocol that permits redelivery under an already
prepared grant must be judged against its own contract, not
declared broken merely for differing from ours.
An already admitted first delivery can commit after lo-
cal revocation. Such an effect is counted separately from
an invalid local admission; no instant remote cancellation
guarantee is assumed. Read-only reconciliation has a sep-
arate synthetic capability that remains valid after write re-
vocation. It can settle an observed historical effect without
authorizing another write.
The provider profiles are P1, stable-key deduplication
within a declared horizon; P2, queryable outcomes with-
out deduplication or automatic cancellation; and P3, opaque
outcomes. An empty lookup cannot certify absence if an
earlier request may still commit. Provider truth is never
used to supply evidence that the participant did not re-
ceive. An unresolved outcome retains its unit reservation.
A passing finite supplied history is not proof that all possi-
ble effects were captured. Incomplete capture or provider-
contract contradictions cannot receive a passing score.
4 Implementation and prospective study
4.1 Matched applications
The application prepares an admission, dispatches and set-
tles. Its SQLite row is separate from the host’s persistence.
All four controls share initial authority and action binding,
reservation state and receipt-bound idempotent settlement.
Cached retry sends again with a fresh key using the exist-
ing admission. Revalidation checks current write authority
before a fresh-key retry and otherwise retains uncertainty.
Stable-key retry preserves the original transport key. Ledger
reconciliation looks up the previous delivery, settles a con-
firmed effect or retains uncertainty, and does not redispatch.
LangGraph 1.2.16 with SQLite checkpointer 3.1.2 runs
prepare, dispatch and settle nodes. A controlled excep-
tion leaves the current node pending; the process closes its
databases and exits. A second process loads the same check-
point and application row and invokes the pending graph
with its original persisted state. Completed graphs are in-
spected without invoking nodes again.
Temporal Python SDK 1.34.0 uses the same application
through activities. The isolated CLI 1.9.1 server, embed-
2

Permission to Retry Arya.ai
ding Temporal 1.32.0, persists to a temporary SQLite file.
The scheduler kills a worker with SIGKILL before activity
acknowledgement. A different process receives the native
retry after the configured two-second activity timeout. The
workflow run identity and retry attempt are recorded. The
logical interruption positions match the graph study, while
the mechanisms differ. Neither host is killed inside an active
database transaction.
4.2 Corpus and capture
The manifest fixes two hosts, 14 schedules, three provider
contracts and four policies: 336 histories, 168 per host
and 42 per host-policy combination. Schedules cover
completed-work reopen; revocation, policy change, expiry
and payload drift before admission; pre-preparation inter-
ruption; lost acknowledgement; delayed commitment after
an empty query; interruption before settlement and after
settlement but before host acknowledgement; and expired
deduplication. Recovery cases have unchanged-authority or
revocation controls where applicable.
A pre-preparation interruption consumes no approval.
After a dispatch node/activity completes, its confirmed ob-
servation is persisted by the host before settlement. Set-
tlement stores the receipt identity with the application row
so a repeated settlement can verify the same evidence with-
out charging twice. A pending provider request commits
at the final observation boundary, after the replacement has
acted. Logical times specify ordering, not measured service
latency.
The campaign was frozen in source b746778054e4 before
collection; the artifact records its full revision. The tree was
clean before and after execution. CPython was 3.13.14, its
SQLite library 3.53.1 and Node 24.19.0. The artifact pre-
serves every history, per-process state, version and reported
result. Adapter errors abort collection rather than silently
omit cells. Verification regrades all histories and indepen-
dently reconstructs coverage, continuity and aggregates.
Earlier development work comprised 180 synthetic-
control histories and 144 native LangGraph histories. Their
purposes and denominators remain separate. This prospec-
tive campaign follows adapter development and does not
claim unseen scenarios or statistical independence. Its com-
plete research suite passes 64 tests with zero skips; in-
tended assertions were observed failing before checker, na-
tive adapter and extended-boundary implementation.
5 Native results
5.1 Safety and progress
Table I reports finite counts. Passing histories include cor-
rectly denied work and unresolved work; checked comple-
tion additionally requires a truthful successful terminal out-
come. The 15 denials per policy concern initial invalid au-
thority/action/expiry or revocation before preparation. They
are not counted as completed tasks. No history was scored
not measured in this captured corpus.
All 168 paired host cells agree on safety, progress, ef-
fect/reservation counts and finding codes. This is a null host
difference for shared authored policies, not equivalence of
all framework features. The experiment confirms that the
observed policy distinction survives each qualified native
recovery path; it does not establish that either framework
defaults to the unsafe controls.
Cached retry reports success in 27 histories per host, but
only 15 are checked completions. Its 12 repeated-delivery
histories exceed the effect allowance. Revalidation removes
post-revocation fresh sends, but six still-authorized retries
duplicate effects. It passes 36 histories while providing the
same 15 checked completions as cached retry, and retains
six unknown reservations.
Stable-key retry has 16 checked completions. Its contract
suppresses some duplicates, but nine histories exceed the
effect allowance where deduplication is unavailable or ex-
pired. Six repeat dispatches fail the benchmark’s current-
authority rule; these findings overlap effect violations and
must not be summed as independent histories. Stable trans-
port identity addresses a different obligation from current
authority.
Ledger reconciliation passes all 42 supplied histories per
host, with 21 checked completions, 15 denials and six un-
known reservations. Per host, three unknowns concern
opaque providers after acknowledgement loss or horizon
expiry, and three concern pending commitments across the
provider profiles. The exact provider/scenario cells remain
visible in Figure 2 and the raw artifact. Zero findings in this
finite set is not a universal guarantee.
5.2 Why the observation boundary matters
The provider profile alone does not determine recoverabil-
ity. When a confirmed observation is already retained by
the host or application, interruption before settlement or af-
ter settlement can complete without another provider write,
even for P3. By contrast, P3 acknowledgement loss has
no participant-visible receipt. In the pending-request cases,
3

Permission to Retry Arya.ai
Table IFinite native conformance outcomes by authored policy
Host and authored policy Passing
histories
Reported
successes
Checked
completions
Denied Unknown
LangGraph: Cached retry 30 / 42 27 15 15 0
LangGraph: Revalidate retry 36 / 42 21 15 15 6
LangGraph: Stable-key retry 31 / 42 27 16 15 0
LangGraph: Ledger reconciliation 42 / 42 21 21 15 6
Temporal: Cached retry 30 / 42 27 15 15 0
Temporal: Revalidate retry 36 / 42 21 15 15 6
Temporal: Stable-key retry 31 / 42 27 16 15 0
Temporal: Ledger reconciliation 42 / 42 21 21 15 6
Figure 1Finite policy outcomes. Each bar contains 42 histories. Checked completion, reported success with a violation, denial and unresolved work are
separate.
P1/P2 can initially return an empty lookup and still later
commit; the ledger policy retains its reservation rather than
manufacture certified absence. A post-revocation remote ef-
fect from that first admitted delivery remains separate from
admitting a new write after revocation.
5.3 Observed fixture execution cost
Table II summarizes whole replacement-worker wall times.
These include Python startup, IPC, scheduling and the con-
figured timeout. Temporal’s timeout/retry wait is part of
the tested protocol, whereas the graph exception is already
closed before replacement starts. This is neither an apples-
to-apples latency ranking nor a product throughput result.
The finite p95 is an empirical order statistic over hetero-
geneous schedules, not a population estimate or confidence
interval.
4

Permission to Retry Arya.ai
Figure 2Boundary coverage for the 168 LangGraph cells. C means checked completion, D denial, U unresolved reservation and F a conformance violation.
P1 is deduplicating, P2 queryable and P3 opaque. All paired Temporal cells have the same checked outcomes.
6 InfinityOS component case study
The separate case study imports InfinityOS’s exported au-
thority resolver and the existing internal Sandbox har-
ness. Ten synthetic authority cases check current grants,
trust/approval revocation, policy change, dependency re-
fusal, lease expiry, cancellation, wrong-run scope and ap-
proval expiry. All ten return the specified grant or denial.
These test dependency composition; they do not validate
real identity-provider ordering or cryptographic human con-
firmation.
Six additional cases execute the actual action coordina-
tor, worker, recovery and settlement code, crossing response
loss and rolled-back settlement with the three provider pro-
files. The substrate is the existing repository fake and
scripted engine. A separate synthetic provider records one
effect in every case, independently of the product ledger.
No case redispatches that effect. Old worker heartbeats are
refused after lease replacement, without increasing effect
count.
The opaque lost-acknowledgement case retains its un-
certain reservation. The opaque settlement- rollback case
recovers from its retained confirmed observation with-
out provider lookup. These results support the same
observation-boundary distinction as the native corpus. Sep-
arately, 17 existing action-crash and real-Weave sequential-
approval regression tests pass on the pinned source. Those
regressions exercise Sandbox approval/resume paths but are
not new independent- provider experiments and are not
pooled with either study.
5

Permission to Retry Arya.ai
Table IIWhole replacement-worker fixture wall durations
Host Observations Median ms Empirical p95 ms Maximum ms
LangGraph 168 261.4 316.7 347.3
Temporal 168 2149.5 2824.1 3048.8
Table IIISeparate InfinityOS component recovery observations
Interruption Provider profiles Cases Settled receipts Unresolved
reservations
Lost acknowledgement P1, P2, P3 3 2 1
Rolled-back settlement with retained
observation
P1, P2, P3 3 3 0
The 16 new component cases do not qualify physical
Mongo durability, the complete human-approval lifecycle or
deployed InfinityOS behavior. The six new recovery cases
use a scripted engine; the separate existing real-Weave tests
do not change that experimental tier.
7 Threats to validity
The policies, provider and checker originate in the same
project. Separate effect truth and reconstruction, hand-
authored counterexamples, corrupted-artifact tests and prior
RED assertions reduce some circularity; they do not substi-
tute for independent human review or a separately imple-
mented oracle. The common application logic also makes
matched outcomes unsurprising.
One canonical action with scripted proposals does not
establish generalization to arbitrary tools, model behavior,
concurrent agents, delegation graphs or real authority stores.
The benchmark’s repeat-freshness contract is stricter than
some prepared-redelivery contracts. Its results must not
be used to attribute violations of guarantees those systems
never offered.
The corpus is finite and deterministic. It was fixed
prospectively after development, not sampled from deploy-
ments or held out from all adapter testing. There are no
frequency estimates, statistical replications or acceptance-
probability claims. A correct refusal can pass safety;
progress metrics are reported separately to expose conser-
vative abstention.
Native worker races, abrupt failure inside transactions,
lost/corrupted databases, settlement-log capture gaps and
real IAM check/commit contention remain unmeasured.
Logical event order establishes fixture happens-before re-
lationships, not atomic serialization with a third-party per-
mission service. Python socket refusal protects the graph
fixture from accidental calls; the local Temporal server/SDK
are trusted participants, not an adversarial network sandbox.
No actual provider, billing account, model server, cus-
tomer dataset or Production environment was used. Library
and local SQLite behavior do not establish SaaS or on-
premise product readiness. No independently maintained
security-protocol implementation was executed. These lim-
its constrain the contribution to conformance and replication
evidence for the declared application profile.
8 Implications and conclusion
Within the measured profile, three questions must remain
explicit at resume: is a new dispatch currently authorized; is
a previous delivery still capable of committing; and is there
durable participant-visible evidence that permits settlement?
A checkpoint, current grant or stable key alone does not an-
swer all three. The finite results distinguish safety, legit-
imate progress and conserved uncertainty without ranking
framework defaults. The artifact supplies concrete histories
and counterexamples for evaluating other implementations
under declared contracts.
9 Availability, ethics and AI assistance
The accompanying publication package contains the
manuscript source, figures, machine-readable outcome ta-
bles and timing observations. Original captures, manifests,
implementation and detailed reproduction instructions are
retained in the authors’ research record; this version pro-
vides no public execution repository. The InfinityOS com-
ponent case study depends on proprietary product source
and repository fakes, which are excluded from the publi-
6

Permission to Retry Arya.ai
cation package. The accompanying tables permit inspection
of the reported aggregates; they do not independently repro-
duce the experiments.
All identities, approvals and business actions are syn-
thetic. Experiments used local fixtures; no customer data,
live provider or model service was involved. Dependency
and documentation retrieval occurred separately from test-
ing. AI tools assisted with research-code development, cap-
ture analysis and manuscript preparation. The same-project
origin of the controls, fixtures and checker is addressed in
the threats to validity.
References
[1] Y . Tong, L. Dai and S. Guo, “AID-Guard: State-
ful Authorization for Delegated Agent Effects,”
arXiv:2608.21159v1, 2026.
[2] J. Xu, L. Fan, Z. Wang, X. Li and H. Liu, “Be-
yond Single-Use Tokens: Durable Authorization
State for Replay-Resistant LLM Agent Actions,”
arXiv:2608.01710v1, 2026.
[3] J. Li, “Where Does Exactly-Once Live? Model, Har-
ness, and Tool-Contract Effects on Duplicate Side Ef-
fects in LLM Agents,” arXiv:2609.29095v1, 2026.
[4] Z. Wang, “ZeroGate: Trust-Preserving Fast Paths for
Governed AI Agent Runtimes,” arXiv:2609.25443v1,
2026.
[5] Z. Wang, “Matoi: Selective Revalidation of Con-
sequence Evidence for Agent Authorization,”
arXiv:2610.21394v1, 2026.
[6] Y . Zheng, Y . Yang, W. Zhang and A. Quinn,
“ACRFence: Preventing Semantic Rollback Attacks
in Agent Checkpoint-Restore,” arXiv:2603.20625v1,
2026.
[7] M. Choi, S. Jeong, S. Choi and S. Lee, “Resid-
ualAuth: What Authorization State Must Lan-
guage Agents Preserve under Revocable Delegation?,”
arXiv:2609.08062v2, 2026.
[8] H. Zhang, A. Cardoza, P. B. Chen, S. Angel and V .
Liu, “Fault-tolerant and transactional stateful server-
less workflows,” inProc. 14th USENIX Symp. Operat-
ing Systems Design and Implementation (OSDI), 2020,
pp. 1187-1204. Publisher record.
[9] LangChain, “Persistence,” LangGraph documentation,
accessed 21 October 2026.
[10] Temporal Technologies, “Error handling,” Temporal
Python SDK documentation, accessed 21 October
2026.
A Reproducibility
The manifest, original histories, host records, InfinityOS
component observations, report and data digests are pre-
served in the authors’ experiment archive. The checker in-
dependently regrades all 336 histories; the verifier checks
Cartesian coverage, versions, persistence continuity and ag-
gregate counts. The 16 component cases and 17 existing
regressions have separate records. A reproduction may gen-
erate different checkpoint UUIDs and wall times while pre-
serving its scenario definitions and checked outcomes; exact
source and dependency versions must remain visible.
The archived reproduction guide contains isolated depen-
dency setup and test, collection, verification, analysis and
offline IEEE-PDF commands. Native storage is temporary
and deleted after each experiment. The publication pack-
age includes derived per-history outcomes and replacement-
worker timings, aggregate counts, figures and exact soft-
ware versions. Full reruns require the archived implemen-
tation and dependencies; the InfinityOS component cases
additionally require proprietary source. Full public repro-
duction is therefore not claimed for this version.
7
