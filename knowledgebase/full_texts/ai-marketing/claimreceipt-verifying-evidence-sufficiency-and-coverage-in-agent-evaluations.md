---
title: 'ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations'
url: https://arxiv.org/abs/2609.01992
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Peiying Zhu
- Sidi Chang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.01992
pages: 8
chars: 34531
fetched_at: '2026-11-08T13:33:34+00:00'
kb_version: 1
---

# ClaimReceipt: Verifying Evidence Sufficiency and Coverage in Agent Evaluations

ClaimReceipt: Verifying Evidence Sufficiency and Coverage
in Agent Evaluations
Peiying Zhu * Sidi Chang *†
peiying@blossomai.co schang@blossomai.co
Blossom AI Blossom AI Labs
San Francisco, CA, USA Tokyo, Japan
Abstract
Agent evaluations face two distinct evidentiary questions: whether a reported claim is recomputable from retained evidence
(sufficiency), and whether the retained records cover the committed experiment set (coverage). Generic logs and hash-linked
transcripts answer neither reliably. We introduceClaimReceipt, a claim-relative receipt specification and selective verifier
that binds typed transaction evidence to a signed experiment manifest and returnsPass,Inv alid, orInconclusiveper claim.
We freeze the specification before implementation (SHA-25618d109...b81). On 1,392 historical buyer–seller records, a CR-2
verifier reproduces all five manually labeled audit verdicts, exactly replays 600 deterministic and 792 post-generation records,
makes every one of 13 declared field groups non-redundant under tested ablations, and returns the expected result on 11/11
semantic faults with 0/8 false positives. We then run a separate prospective CR-3 epoch: 30 assignments are committed before
inference, terminal receipts are signed and chained, and private evidence is encrypted for an auditor. Complete evidence yields
coverage and accountingPass; withholding one terminal receipt returnsINCONCLUSIVE_COVERAGE, while withholding all private
openings preserves coverage and protocol verification but makes economic claims inconclusive, exactly matching a preregistered
prediction. Receipt instrumentation adds 0.021% of model-inference time and 9.9KB per transaction. A specification-legibility
probe indicates that our own frozen specification is not yet unambiguous to an independent reader. Claim verification therefore
requires both claim-sufficient evidence and a committed universe against which omissions become visible.
Keywords:agent evaluation, agent verification, evidence sufficiency, experiment coverage, audit receipts, construct validity,
provenance, multi-agent systems
1 Introduction
When an agent benchmark reports that a prompt, scaffold,
guardrail, or model improved performance, two questions
follow.Sufficiencyasks whether the number can be re-
computed correctly from retained evidence.Coverage
asks whether those records are the complete committed
set rather than a favorable subset. Sufficiency protects
against an honest but fallible evaluator; coverage also ad-
dresses an operator that may prefer some runs to remain
unseen. A final reward, transcript, or generic signed log
may preserve bytes while omitting private state, parser
outputs, discarded attempts, or an expected terminal
record.
This gap is especially acute for interactive agent systems.
Their measured outcome is jointly produced by model
generations, hidden environment state, parsers, enforce-
ment code, retry rules, and downstream scoring. Agent
benchmarks already face large run-to-run variance and
protocol sensitivity [7, 10]. In multi-agent settings, the
environment also determines what one agent can learn and
which actions another may take. A scalar can therefore
remain numerically correct while the causal interpretation
attached to it is invalid.
Prior work audited this problem in an agent-to-agent
∗Both authors contributed equally to this research.
†Corresponding author.
(A2A) commerce simulation [17]. A manual construct-
validity contract separated four questions: whether the
seller instantiated the intended incentive (C1), whether
treatment arms differed only in the intervention (C2),
whether stochastic estimates were stable (C3), and
whether outcome accounting was complete (C4). That
audit stopped an attractive policy claim: the original ex-
periment wasInv alidbecause the arms used different
offer protocols, while a controlled rerun remainedIncon-
clusivebecause incentive validity and generation stability
did not pass. The audit also established an identifiability
boundary: if an evidence abstraction maps executions
with different claim truth to the same retained record, no
downstream metric can recover the discarded distinction.
This paper gives the constructive counterpart.Claim-
Receiptasks what a platform must retain so a bounded
claim is recomputable, and what it must commit so
missing runs are detectable. Hashing everything is not
enough. The contribution is a typed evidence schema,
an experiment-level manifest, exact accounting semantics,
and a selective decision procedure. Hashes, signatures, and
tamper-evident chains are standard transport mechanisms
[5, 9]; they cannot decide which semantic distinctions
matter or define the universe that should have produced
receipts.
Figure 1 shows the design. Before prospective ingress, a
manifest commits the population, arm definitions, protocol
1
arXiv:2609.01992v1  [cs.AI]  2 Sep 2026

ClaimReceipt Zhu & Chang
fingerprints, replication structure, estimator, thresholds,
and coverage policy. Each transaction receipt links that
manifest to an assignment, private-profile commitment,
ordered trace, raw and normalized offers, chooser decision,
exact economic claims, and artifact digests. The reference
verifier checks integrity and coverage, replays claims from
the appropriate boundary, and returns a per-contract
verdict. It may license descriptive reporting while blocking
a causal policy claim.
Our contributions are:
1. We formalize claim-relative evidence sufficiency over
executions, define a bounded claim class, and pro-
vide a field-to-claim dependency matrix. The schema
is sufficient by construction for that class, not for
arbitrary claims about intent or external truth.
2. The verifier performs selective verification at CR-
2 and CR-3: it recomputes transaction and batch
claims, preservesInconclusiveas a first-class
output, and adds prospective manifest, ingress,
encrypted-opening, receipt-chain, and conditional-
coverage checks.
3. On a previously audited corpus of 1,392 receipts
across six epochs, the verifier agrees with 5/5 manual
verdicts, exactly replays every declared transaction
claim, and reports the complete historical4× 6grid
plus a separate prospective row, rather than only
labeled cells.
4. Field ablations, 11 frozen faults, and eight benign
variations test schema semantics; a separate 30-
transaction prospective evaluation tests complete,
missing-terminal, and missing-private-evidence cases
with measured overhead.
2 Problem Formulation
2.1 Claim-relative sufficiency
Let τ be a complete admissible execution,c(τ )the ground-
truth value of claimc, and ϕE(τ )the evidence retained by
field set E. We callE claim-sufficientfor c exactly when
∀τ1, τ2 :ϕ E(τ1) =ϕE(τ2)⇒c(τ 1) =c(τ2).(1)
This definition is over executions and claim truth, not a
verifier’s output. A verifier that always abstains cannot
make E = ∅ sufficient. Conversely, when required evidence
is absent, a verifier must not substitute a reported scalar;
it must reject or abstain.
Sufficiency is always relative to a claim class. Version
0.3 supports eight transaction claims—completion, buyer
surplus (BS), seller profit (SP), welfare (W), first-best
fraction, matchquality, andtwotreatment-fidelityclaims—
plus four experiment claims C1–C4. It does not claim
sufficiency for latent intent, equilibrium, fairness, external
profile truth, or uncommitted transactions.
Coverage is instead a property of a set: no single receipt
can show that every committed assignment produced a
terminal record. It requires an experiment manifest and
an ingress commitment that define the expected set before
outcomes are observed.
2.2 Running transaction semantics
We instantiate the specification in configurable buyer–
seller transactions. A buyer profileθ assigns private values
to a component setS, an outside-option utilityoθ, and
hard constraints. If an offer at pricepis accepted,
BSθ(S, p) =Vθ(S)−p−o θ,(2)
SP(S, p) =p−C(S),(3)
Wθ(S) =V θ(S)−C(S)−o θ = BS + SP.(4)
Rejected or failed transactions contribute zero. First-best
welfare is W ⋆ θ = max(0,max S Wθ(S))under the commit-
ted component rule. The first-best claim is the exact
rational pair( W, W⋆)when W ⋆ > 0and a typed null oth-
erwise; it is not clamped, because negative welfare records
destruction. Match quality is also retained as an exact
numerator–denominator pair.
The experiment claims encode the prior audit contract
[17]: C1 tests whether ordered seller-objective levels pro-
duce the declared directional response; C2 tests cross-
arm protocol isolation; C3 tests stochastic stability using
profile-level pairing with replications nested inside profile–
condition cells; and C4 tests replay and complete account-
ing. Each returnsPass,Inv alid, orInconclusive.
3 ClaimReceipt Design
3.1 Four evidence layers
The specification separates four layers that generic “audit
log” language often conflates.
1. Transport integrity covers exact bytes, sequence num-
bers, chain links, and signatures. It detects mutation
of evidence already committed.
2. Semantic evidence (sufficiency) retains typed profile,
trace, offer-stage, choice, catalog, and scorer inputs
needed to recompute claims.
3. Experiment coverage binds receipts to an expected
assignment matrix and ingress commitment, making
omissions after committed ingress visible.
4. External truth remains outside the system. A plat-
form cannot prove that an unobserved interaction
occurred or that a synthetic profile describes a real
person.
2

ClaimReceipt Zhu & Chang
prospective manifest
assignments, protocol, estimator
agent transaction
trace, offers, attempts
claim receipt
public + auditor evidence
selective verifier
P ass/Inv alid/Inconclusive
digest and assignment contract
Figure 1:ClaimReceiptbinds transaction evidence to an experiment manifest. Transport integrity protects retained
bytes; claim semantics determine what those bytes license.
Table 1: Prototype trust roles. Separation is by key and
function, not by organizational principal: one operator
controls all three local roles.
Role Trusted action Residual capability /
boundary
Manifest authority Ed25519-sign contract
before ingress
Can declare a biased
universe or false profile
(L4)
Ingress authority Ed25519-sign tickets,
checkpoint, receipts
Separate role, but may
collude with owner in
this prototype
Runner Produce terminal evi-
dence after a ticket
May mutate or omit;
chains and reconcilia-
tion expose L1/L3
Auditor Hold X25519 opening
key and replay private
evidence
Learns sensitive profiles;
governance and deletion
remain external
OTS calendars Commit manifest digest
before first ticket
External time anchor,
not an independent
ingress witness
The distinction prevents cryptography from being mis-
taken for construct validity. Certificate Transparency and
tamper-evident logs establish valuable integrity proper-
ties [9, 3]; they do not decide whether an omitted private
profile makes welfare underdetermined.
3.2 Threat model and trust boundary
Transport mechanisms address L1 byte mutation; semantic
replay and protocol fingerprints address L2 construct drift;
prospective ingress and terminal reconciliation address L3
omissions after commitment. L4 remains open: no receipt
system can detect transactions prevented from reaching
the witness or a false but internally consistent ground-
truth profile.
3.3 Experiment manifest
C2 and C3 are batch properties, so no single transac-
tion receipt can establish them. Every receipt references
an experiment manifest containing: the ordered profile
and condition sets; the complete expected assignment ma-
trix; replication and retry policies; treatment flags; an
allowlist of fields permitted to vary across arms; protocol
fingerprints for prompts, schemas, parsers, normalizers,
enforcers, choosers, scorers, model assignments, and in-
teraction horizon; and the analysis contract, including
estimand, nesting, pairing, estimator, threshold, seed,
draw count, input order, and interval convention.
When the signed manifest predates committed ingress,
it acts as a cryptographic preregistration. E1–E6 are
explicitly retrospective imports: their manifests were re-
constructed after the runs, so they support faithful mech-
anization rather than prospective confirmation. E7 is
separate and prospective: its signed assignment matrix
and OpenTimestamps proof precede all 30 ingress tickets.
3.4 Transaction receipts and privacy
The public receipt carries assignment identifiers, terminal
status, manifest and artifact digests, a private-profile com-
mitment, semantic digests for the trace, offer and outcome,
exact claim values, and coverage counts. An auditor enve-
lope opens the profile and preserves ordered raw-hidden
and visible events, all attempts, raw and parsed offers,
post-enforcement offers, chooser input/output, treatment
events, reported scalars, and artifact references.
Low-entropy values such as WTP cannot safely use a
bare hash. The specification commits a private canonical
objectxas
HMAC-SHA256n

tag∥uint64be(|x|)∥x

,(5)
where n is a fresh secret 32-byte nonce stored with the
encrypted opening [8]. Canonical JSON follows RFC 8785
semantics [14]; schema-declared sets may reorder, while
transcript and attempt order may not. Economic amounts
are scaled integers, aggregate means are(sum,count ), and
decision-bearing interval endpoints retain a precision en-
velope. If a decision boundary intersects that envelope,
the verifier abstains.
This architecture exposes a tension: verification needs
access to the hidden WTP and profile used to score the
experiment, while the marketplace policy may be designed
to keep that information from the seller. The receipt
therefore creates an auditor-visible encrypted evidence
store, not a public transcript. CR-3 implements opening-
key separation, but authorization, retention, and deletion
remain governance obligations.
3.5 Replay boundary and verdicts
The replay claim has two tiers. For deterministic scripted
sellers, replay begins at the committed policy artifact and
continues through offer generation, normalization, buyer
choice, and welfare. For LLM sellers, replay begins at
the recorded raw output and continues through parsing,
3

ClaimReceipt Zhu & Chang
enforcement, choice, and scoring. We do not claim that
another model call will reproduce the same text.
Before C1–C4, the verifier canonicalizes and dedupli-
cates idempotent deliveries, checks receipt IDs and chain
links, opens profile commitments, resolves assignment
coverage, and retains retry order. It then recomputes all
transaction claims exactly. C2 compares declared invariant
fingerprints across arms. C1 and C3 average replications
within profile cells before profile-level contrasts; genera-
tion rows never become independent buyers. C4 requires
exact replay,BS + SP = W, and the full report bundle. A
causal policy claim is licensed only when all four criteria
pass and treatment fidelity is established. A descriptive
claim may remain licensed when C1 or C3 is inconclusive
but C2 and C4 pass.
4 Implementation and Evaluation
4.1 Frozen specification and implementa-
tion
We adversarially reviewed and froze ClaimReceipt v0.3
before implementing the verifier. Earlier v0.1 and v0.2
files and hashes remain immutable. Two non-verdict ob-
servations informed amendments: an integrality audit of
9,744 historical amount cells and inspection of the histori-
cal match-quality scorer. No C1–C4 verdict or fault result
was observed before v0.3.
SHA-256:
18d10901d7760b1ab99fbeed97b2e37d
704092ba217f38478bd37d01378a1b81
The reference implementation reaches CR-2 Batch Ver-
ification on the imported corpus and CR-3 Prospective
Coverage on E7. CR-3 adds two Ed25519 signing roles,
an X25519 auditor-opening role, pre-ingress assignment
tickets and checkpoint, encrypted evidence, signed receipt
chaining, and coverage-qualified output.
4.2 Corpus
We import 1,392 terminal records from the previously
audited A2A study without importing its manual labels.
The six retrospective epochs remain exactly those in Ta-
ble 2. The deterministic epochs contain 600 records; the
remaining 792 are LLM or fixed-menu records associated
with LLM experiments. Buyer and seller generations use
Qwen2.5-Instruct 1.5B, 3B, and 14B historically [15]. Ret-
rospective receipts use deterministic test nonces. E7 is
not added to the 1,392 count: it independently runs 15
profiles under NONE and BOTH with Qwen2.5-Instruct
3B,k= 1, and fresh random nonces.
4.3 Evaluation questions
R1 reproduces five manually labeled audit cells and re-
ports the historical4 × 6grid; post-specification controls
Table 2: Retrospective corpus. Every epoch receives a
separate manifest.
Epoch Receipts Primary audit role
E1 original scaffold 270 known C2 failure
E2 unified protocol 450 controlled treatment
E3 repeated subset 36 C3 stability
E4 incentive prompts 36 C1 manipulation
E5 scripted profit maximum 300 deterministic positive con-
trol
E6 scripted bundle stress 300 deterministic positive con-
trol
Total 1,392 six manifests
separately show C1/C3 canPass. R2 measures exact
replay. R3 compares evidence abstractions and removes
13 field groups. R4 applies frozen semantic faults and
benign controls, including held-out retry shadowing versus
a valid retained retry. R5 tests public versus authorized
observability and omission propagation; R6 measures the
prospective CR-3 path. Byte tampering remains an in-
tegrity sanity check rather than the headline.
5 Results
5.1 R1: the verifier reproduces the man-
ual audit
The verifier agrees on all five manually labeled cells (5/5).
It marks E1 C2Inv alidbecause the unguarded arm
used aroom_attributes/price bundle and whole-bundle
chooser while the guarded arm used a base-plus-add-ons
schema and subset chooser. It marks E2 C2Passafter
those invariant fingerprints are unified. It returnsIncon-
clusivefor E4 C1 and E3 C3, andPassfor joint scripted
accounting.
Table 3 gives the historical grid plus the separate E7
prospective row. No additionalInv alidcell appears be-
yond E1 C2. We distinguish contract abstention (IC: no
required contract) from evidential abstention (IE: the
contract exists but evidence does not cross its boundary).
C4 passes with authorized evidence even when another
criterion blocks the causal comparison.
Agreement alone is evidence of faithful mechanization,
not independent accuracy: a criterion-wise constant clas-
sifier could match five sparse labels. The verifier does not
read those labels; it recomputes the underlying contrasts
and intervals. Moreover, the two synthetic decision-rule
controls returnPass: C1 has a monotone+38.5contrast
with one-sided 95% lower bound 37.25, and C3 has a sta-
ble+28 .5contrast with central 95% interval[27.0, 30.1].
These post-specification controls rule out constant absten-
tion but do not enter the 1,392-record corpus or support
a behavioral claim.
The historical numerical evidence is likewise reproduced
rather than copied. In E4, mean seller profit is 25.8
4

ClaimReceipt Zhu & Chang
Table 3: Verifier grid. P=Pass, X=Inv alid;IC lacks a
contract and IE has insufficient evidence. Cov is prospec-
tive coverage; retrospective rows are not applicable. A
dagger marks the manually audited comparisons; E5–E6
form one joint accounting label.
Epoch C1 C2 C3 C4 Cov
E1 originalI C X† IC P –
E2 unifiedI C P† IC P –
E3 repeatedI C PI † E P –
E4 incentiveI † E PI C P –
E5 scripted profitI C PI C P† –
E6 scripted stressI C PI C P† –
E7 prospectiveI C PI C P P
Table 4: Exact replay by tier. Policy replay for the LLM-
associated tier applies only to 210 deterministic fixed-menu
rows; no LLM regeneration is claimed.
Replay tier Policy Choice Metrics
Scripted end-to-end 600/600 600/600 600/600
LLM post-generation 210/210 792/792 792/792
under the compliance prompt, 57.5 under the standard
prompt, and 33.8 under profit pressure. The strongest-
minus-weakest profile contrast is+8.0; its one-sided 95%
lower bootstrap bound is −2.7(central 95% interval
[−12.0, 20.0]), and the ordered response is non-monotone.
In E3, the profile-level guardrail effect is+37.6with 95%
interval[ −34.2, 109.3]and mean within-cell generation SD
47.8. The verifier therefore abstains even though the point
estimate is positive.
5.2 R2: the replay boundary is exact
All 600 deterministic records exactly match at policy,
normalization, chooser, and metric stages. All 792 records
in the LLM-associated epochs exactly match from the
committed raw offer through choice and economic claims.
Their recorded LLM text is hashed and auditable but not
regenerated. The 210 fixed-menu rows inside those epochs
additionally replay from menu policy. Thus the claim is
strong where determinism exists and deliberately narrower
where stochastic generation begins.
5.3 R3: generic evidence is not claim-
sufficient
Table 5 asks whether evidence uniquely determines a claim
under Equation 1, not whether it stores a reported number.
Outcome scalars, transcripts, and generic signed receipts
determine none of the 12 claims because each omits re-
quired claim inputs, protocol, or batch evidence. An
opened transaction receipt recovers six economic claims
Table 5: Claims uniquely determined by each evidence
abstraction. Counts include eight transaction/treatment
claims and C1–C4.
Evidence abstraction Determined Main missing distinction
Outcome scalars 0/12 claim inputs and batch
contract
Transcript + outcome 0/12 private state, chooser,
protocol, coverage
Generic signed receipt 0/12 claim-specific semantics and
artifacts
Opened transaction receipt 6/12 treatment fidelity and batch
contract
ClaimReceipt v0.3 12/12 none within declared claim
class
but not treatment fidelity or batch criteria; full ClaimRe-
ceipt determines all 12 within its declared scope.
Table 6 brings the frozen dependency matrix into
the main paper. The ablation is an implementation-
conformance check against this declared matrix, not a
procedure that discovers dependencies from data. All 13
field-group removals make at least one claim underdeter-
mined, confirming that the verifier does not silently trust
a stored value after its declared evidence is removed. This
establishes non-redundancy only under the tested group
ablations, not global field minimality over all2n subsets.
5.4 R4: semantic faults and benign con-
trols
The verifier returns the frozen expected result on 11/11
semantic faults and raises no false positive on 0/8 be-
nign variations. Detected cases include cross-arm schema
drift, profile-opening conflict, a recorded guardrail flag
without an enforcement event, scorer/version drift, pseudo-
replication, selective reporting, missing terminal evidence,
a missing private opening, and an incomplete report bun-
dle. Most importantly, the held-out retry-shadowing fault
returns C3Inv alid, while the paired benign retained retry
remainsPass. Equivalent JSON key order, whitespace,
integral numeric spelling, Unicode NFC, set order, idem-
potent redelivery, and transport-only timestamps do not
alter scientific verdicts.
These rates are specification-conformance results on a
small frozen suite, not estimates of performance against all
possible attacks. L1 byte mutation is detected by standard
digest checks. L4 interactions outside committed ingress
remain unobservable and are reported as residual risk, not
counted as false negatives.
External specification-legibility probe.Under the frozen
single-response protocol the model exhausted its output
budget before emitting final JSON; no valid measurement
was obtained and the run is not scored. The frozen proto-
col under-provisioned output for a single-response format.
A subsequent per-item run—explicitly post-hoc and not
protocol-conformant—yielded 10/11 parseable responses,
of which 3/11 matched the verifier. We treat this as
5

ClaimReceipt Zhu & Chang
Table 6: Frozen absolute field-to-claim dependencies. A dot means that removing the field group makes the claim
underdetermined. Cmp=completion; FB=first-best fraction; MQ=match quality; IG/CG=information/conduct
guardrail fidelity.
Field Cmp BS SP W FB MQ IG CG C1 C2 C3 C4
I ingress/coverage• • • • • • • • • •
A assignment• • • •
P private profile• • • • • • • • • •
K catalog/cost• • • • • • •
T ordered trace•
O offer stages• • • • • • • • • •
D chooser• • • • • • • • • •
F scoring artifacts• • • • • • • •
G guardrail events• • •
Q protocol• • • • • •
J objective contract•
R replication contract• • •
B report bundle•
exploratory diagnosis, not a confirmatory measurement.
The dominant error mode was temporal: the specifica-
tion classifies faults by layer but never declares fault timing
relative to commitment as an explicit attribute, although
every layer assignment depends on it. The probe there-
fore motivates a v0.4 amendment addingfault_timing
∈ {pre_commitment, post_commitment} to each taxon-
omy entry, with a preflight rule routing post-commitment
cases to integrity checking before layer classification. We
state the amendment but do not adopt it: applying it after
observing the probe would void the preregistration, and
re-testing against the same eleven items would evaluate a
specification written to those items.
This is one model under one protocol; we cannot sepa-
rate specification ambiguity from model-specific reading
failure, so the result bounds legibility from below rather
than measuring it.
5.5 R5–R6: prospective coverage, observ-
ability, and overhead
E7 commits 15 profiles under NONE and BOTH
before inference (internal IDs unguarded_agent and
guardrailed_agent). The signature-bound manifest
time is 08:13:17.826Z; calendar attestations are obtained
at 08:13:20.192Z; the first of 30 preassigned ingress tickets
is issued at 08:13:20.197Z. All receipts form one verified
chain and reconcile to 24 accepted and six rejected ter-
minals. The supplemental OpenTimestamps proof was
upgraded to a Bitcoin block-header attestation at height
963833. We do not claim that this host independently
validated the block: it has no configured Bitcoin Core
node. Role separation is therefore real at the key level,
not at the organizational-principal level.
Table 7 shows two selective degradations. Removing
the last terminal receipt leaves a valid 29-receipt prefix
but returns INCONCLUSIVE_COVERAGE; C4 and descriptive
licensing fall with it, while C2 remainsPass. Propagating
unresolved coverage to C4 is an implementation reading of
complete accounting, not a new frozen decision threshold.
Before the private-opening ablation, we freeze a predic-
tion (SHA-256 72c554...4c0f): public receipts should
retain coverage and C2, but all six economic and two
treatment-fidelity claims should becomeInconclusive.
The observed result matches exactly. In particular, public
SP is not trusted because its frozen dependency includes
the private profile needed to recompute the completion
branch.
The primary auditor-verification number is the 10-run
median, 734µs (range 724–828); 1,040µs is one cold read,
not a second estimator. Storage comprises a 2.64KB
public receipt, 6.21KB encrypted envelope, and 1.05KB
ingress ticket. Tickets are batch-issued after the epoch
assignment set is committed and before inference, making
their signing cost pre-ingress rather than terminal-path
latency.
6 Discussion and Limitations
The contribution is semantics, not cryptography.A hash
chain answers whether retained bytes changed; ClaimRe-
ceipt answers which retained distinctions a declared claim
depends on. The field–claim matrix is the constructive
dual of an identifiability failure: if removing a field group
allows two admissible executions with different claim truth
to share one evidence projection, no later solver or metric
can repair that loss. Other domains will need different
claim classes and dependencies, but the workflow—declare
claims, derive evidence, commit the experiment, replay or
abstain—transfers.
Selective abstention is a result.The grid contains many
Inconclusivecells because historical runs were not de-
signed for every criterion. This is intended behavior. The
verifier still licenses exact descriptive accounting where C2
and C4 pass while blocking causal claims about strategic
sellers or stable policy effects. A gate that never stops an
attractive result is not verification.
Receipts do not create external coverage.E7 demon-
strates prospective manifest, tickets, checkpoint, en-
6

ClaimReceipt Zhu & Chang
Table 7: CR-3 results. P=Pass, I=Inconclusive, D=determined. Percentages use 2,000.14ms model inference per
transaction.
(a) Missing-terminal propagation
Output 30/30 29/30
Coverage P I
C2 protocol P P
C4 accounting P I
Descriptive licensed blocked
(b) Public versus auditor view
Claim group Public Opened
Coverage + C2 P P
Six economic I 6/6 D
Two fidelity I 2/2 D
C4 / descriptive I / blocked P / licensed
(c) Per-transaction cost
Path Cost Inference
Terminal write 361µs 0.018%
Including ticket 428µs 0.021%
Public verify 297µs 0.015%
Auditor verify 734µs 0.037%
Cold auditor read 1,040µs 0.052%
Storage 9.90KB –
Epoch verdict 31.74ms –
crypted openings, chaining, and coverage-qualifiedPass.
The missing-terminal arm shows why this layer is not
implied by replay. Yet CR-3 proves completeness only
relative to committed ingress: a platform that prevents
a transaction from reaching the witness remains out-
side observability (L4). EveryPasstherefore carries
verified_only_within_committed_ingress.
Privacy remains an engineering and governance burden.
Auditable welfare requires the evaluator’s hidden profile,
including sensitive low-entropy values. E7 encrypts each
opening to a separate X25519 role, but one operator still
holds every role key. A deployment needs independent
custody, authorization, retention, and deletion; otherwise
verifiability can undermine the information protection
being evaluated. Zero-knowledge metrics remain future
work.
Evaluation scope.The evidence comes from one config-
urable hotel testbed and one principal model family; E7
uses only Qwen2.5-Instruct 3B andk = 1. The 11 faults
are designed rather than organic, and the abstraction
analysis is scoped to the frozen claim class. We have
not tested a second domain, an independent implementa-
tion, or separately operated trust roles. The next systems
question is governance: independent ingress witnessing,
key custody, and admission rules that reduce L4. The
legibility probe also suggests a check others can apply
cheaply: before treating a frozen contract as binding on
third parties, measure whether an independent reader can
predict its verdicts.
7 Related Work
Agent evaluation and observability.Agent evaluations
emphasize interactive completion and scenario-aware mea-
surement [11, 7, 10], while trace audits show that ag-
gregate success can conceal failures and misrank repairs
[18, 16]. ClaimReceipt specifies evidence needed to recom-
pute bounded claims and validity verdicts.
Provenance and tamper evidence.Timestamping, authenti-
cated logs, and Certificate Transparency establish append-
only integrity [5, 3, 9]; provenance tracks artifact depen-
dencies [13, 1]. We add claim semantics and conditional
coverage using standard primitives unchanged.
Evaluation contracts and construct validity.Construct
validity asks whether an operationalization measures its
named object [2, 6]; datasheets and model cards expose
assumptions [4, 12]. ClaimReceipt turns a subset into
machine-checkable contracts that stop missing evidence
from silently becoming a positive conclusion.
8 Conclusion
Agent verification needs both a sufficient record for each
claim and a committed set against which omissions are
visible. On 1,392 historical records, CR-2 reproduces a
manual audit, replays deterministic and post-generation
claims, and separates semantic faults from benign varia-
tion. On 30 prospective transactions, CR-3 distinguishes
complete evidence, a missing terminal, and unavailable
private openings at negligible runtime cost. The result is
not a universal receipt, but a demonstrated method for de-
ciding what agent-evaluation evidence licenses—including
when it licenses only abstention.
References
[1] C. Boettiger. An introduction to docker for repro-
ducible research.ACM SIGOPS Operating Systems
Review, 49(1):71–79, 2015.
[2] L. J. Cronbach and P. E. Meehl. Construct validity in
psychological tests.Psychological Bulletin, 52(4):281–
302, 1955.
[3] S. A. Crosby and D. S. Wallach. Efficient data struc-
tures for tamper-evident logging. In18th USENIX
Security Symposium, pages 317–334, 2009.
[4] T. Gebru, J. Morgenstern, B. Vecchione, et al.
Datasheets for datasets.Communications of the
ACM, 64(12):86–92, 2021.
[5] S. Haber and W. S. Stornetta. How to time-stamp a
digital document.Journal of Cryptology, 3(2):99–111,
1991.
[6] A. Z. Jacobs and H. Wallach. Measurement and
fairness. InProceedings of the 2021 ACM Conference
7

ClaimReceipt Zhu & Chang
on Fairness, Accountability, and Transparency, pages
375–385, 2021.
[7] S. Kapoor, B. Stroebl, Z. S. Siegel, N. Nadgir, and
A. Narayanan. AI agents that matter.Transactions
on Machine Learning Research, 2025.
[8] H. Krawczyk, M. Bellare, and R. Canetti. HMAC:
Keyed-hashing for message authentication. RFC 2104,
Internet Engineering Task Force, 1997.
[9] B. Laurie, A. Langley, and E. Kasper. Certificate
transparency. RFC 6962, Internet Engineering Task
Force, 2013.
[10] P. Liang, R. Bommasani, T. Lee, et al. Holis-
tic evaluation of language models.arXiv preprint
arXiv:2211.09110, 2022.
[11] X. Liu, H. Yu, H. Zhang, et al. Agentbench: Evalu-
ating LLMs as agents. InInternational Conference
on Learning Representations, 2024.
[12] M. Mitchell, S. Wu, A. Zaldivar, et al. Model cards
for model reporting. InProceedings of the Conference
on Fairness, Accountability, and Transparency, pages
220–229, 2019.
[13] L. Moreau and P. Missier. PROV-DM: The PROV
data model.W3C Recommendation, 2013.
[14] A. Rundgren, B. Jordan, and S. Erdtman. Json
canonicalization scheme (JCS). RFC 8785, Internet
Engineering Task Force, 2020.
[15] A. Yang, B. Yang, B. Zhang, et al. Qwen2.5 technical
report.arXiv preprint arXiv:2412.15115, 2024.
[16] P. Zhu and S. Chang. When aggregate alignment mis-
leads: Auditing policy repair without per-state expert
actions.arXiv preprint arXiv:2607.03386, 2026.
[17] P. Zhu and S. Chang. When guardrails look effective:
Construct validity failures in LLM agent commerce
evaluation, 2026. Preprint.
[18] P. Zhu and S. Chang. When outcome looks right but
discipline fails: Trace-based evaluation under hidden
competitor state.arXiv preprint arXiv:2605.18580,
2026.
8
