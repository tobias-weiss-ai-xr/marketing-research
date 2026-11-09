---
title: 'Boundary-State Control for Tool-Using Language-Model Agents: Commit-Time Consistency under State
  Drift'
url: https://arxiv.org/abs/2609.37475
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Wesley Shu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.37475
pages: 16
chars: 44351
fetched_at: '2026-11-08T13:31:47+00:00'
kb_version: 1
---

# Boundary-State Control for Tool-Using Language-Model Agents: Commit-Time Consistency under State Drift

Boundary-State Control for Tool-Using Language-Model Agents:
Commit-Time Consistency under State Drift
Wesley Shu
The Institute of Energetic Paradigm
September 2026
Abstract
Tool-using language-model agents can decide that an action is permissible and execute it only
after security-relevant state has changed. We study this proposal-to-commit gap and introduce
BSC-R, a deterministic eﬀect-boundary mechanism that binds a single-use commit authoriza-
tion to the exact action and to a semantic projection of the authorization state that justiﬁed it.
On 2,847 attacked AgentDojo episodes, the boundary kernel preserves the unprotected agent’s
behavior exactly (80.576% utility; 1.616% attack success). On 10,302 frozen proposals it accepts
every unchanged commit and rejects every instance of ten prospectively speciﬁed changed or
replayed classes. In an independently generated boundary-drift experiment, full joint binding
commits 0/4,403 invalid contexts while retaining 5,899/5,899 valid contexts. A prospective exter-
nal evaluation on the 3,460-scenario CONTINUITY suite retains all 700 benign cases, prevents
1,200/1,200 represented non-replay invalid eﬀects, handles 160/160 replay lifecycles correctly,
and withholds 200/200 ambiguous no-release cases. The broader external suite also exposes the
method’s limit: across all 2,560 attacks, BSC-Rhas a 25% invalid-eﬀect commit rate versus 0%
for CONTINUITY. The result is therefore a scoped commit-time consistency mechanism, not a
universal agent-safety claim.
1 Introduction
Language models increasingly act through tools rather than merely generate text. ReAct-style
agents interleave reasoning and action ( Yao et al. , 2023), Toolformer-style models learn when to
invoke APIs ( Schick et al. , 2023), and modern agent benchmarks evaluate stateful interaction with
email, ﬁles, browsers, databases, and other external systems ( Ruan et al. , 2024; Debenedetti et al. ,
2024; Lu et al. , 2025). Once an agent can create durable eﬀects, however, a security decision is no
longer identical to a language-model output. There is a temporal boundary between deciding what
may happen and making it happen.
The gap is a security problem because authorization can be time-sensitive. A target can change,
authority can be revoked, a policy can advance, an approval can cease to denote the same request,
or a previously fresh witness can become stale. This is structurally related to complete media-
tion and reference-monitor enforcement ( Saltzer and Schroeder , 1975; Schneider, 2000), to time-
of-check/time-of-use races ( Bishop and Dilger , 1996), to mutable usage authorization ( Park and
Sandhu, 2004), and to transaction ﬁnality under changing state ( Papadimitriou, 1979; Gray and
Lamport, 2006). The agent setting adds an important complication: the proposed action and the
security context are semantic objects produced and transported across model, tool, policy, approval,
and execution components.
1
arXiv:2609.37475v1  [cs.AI]  26 Sep 2026

Prompt injection makes this boundary especially consequential. Indirect instructions can enter
through retrieved or tool-returned content ( Greshake et al. , 2023); InjecAgent, AgentDojo, Agent
Security Bench, and AgentHarm show that tool-capable agents can be driven toward adversarial
objectives in stateful environments ( Zhan et al. , 2024; Debenedetti et al. , 2024; Zhang et al. , 2025;
Andriushchenko et al. , 2025). Most such benchmarks ask whether an attack ultimately succeeds.
We ask a complementary systems question: after an action has already been qualiﬁed, what must
still agree at the instant the external eﬀect becomes durable?
We study Boundary-State Control with semantic authorization projection (BSC-R). The mech-
anism places a deterministic veriﬁer at a trusted eﬀect sink. At qualiﬁcation time it binds a
single-use witness to the exact action and to a canonical projection of the authorization state that
justiﬁed the action. At commit time it re-evaluates the current security state, compares the bound
semantics, checks explicit validity predicates, and consumes the witness only if the transition re-
mains authorized. The projection uses stable authorization semantics rather than requiring opaque
producer-local authorization-object identity.
This paper makes four contributions:
• We formalize proposal-to-commit drift for tool-using agents and specify a joint commit witness
over action, authority, policy, procedure, approval, and replay-relevant state.
• We separate deterministic boundary enforcement from learned qualiﬁcation. On the complete
native AgentDojo run, the boundary kernel preserves base behavior exactly, whereas the learned
qualiﬁcation policy collapses to deny-all behavior.
• We identify the causal role of bound ﬁelds with prospectively frozen interventions and test
selective control under independently generated post-qualiﬁcation drift, obtaining 0/4,403 invalid
commits and 5,899/5,899 valid commits for full joint binding.
• We evaluate the ﬁnal semantic projection prospectively on CONTINUITY and report both its
represented successes and its residual failure regime. This external test prevents the internal
conformance results from being mistaken for a universal safety claim.
The negative results are part of the contribution. A restrictive deterministic comparator
achieves lower native attack success than the boundary kernel but also lower utility. On the com-
plete external attack suite, CONTINUITY prevents every invalid eﬀect while BSC-Rstill commits
25%. These outcomes locate the mechanism’s operating boundary rather than being collapsed into
a single post-hoc score.
2 Problem Setting and Threat Model
2.1 Proposal-to-commit drift
Let a qualiﬁed tool proposal be q = ( a, zq), where a is the canonical external action and zq is the
security-relevant state observed when the proposal is authorized. We factor
z = (u, e, c, r, p, h),
where u is authorization state, e an authority epoch, c contract or procedure evidence, r policy
identity, p approval and request binding, and h single-use execution state. The commit-time state
zc may diﬀer from zq because the environment changes after qualiﬁcation.
An invalid commit occurs when the intended external eﬀect becomes durable even though the
current state no longer authorizes the qualiﬁed transition. This deﬁnition concerns execution valid-
2

ity, not whether the language model’s original plan was desirable. A proposal can be semantically
well formed yet become invalid before commit.
We evaluate two endpoints jointly:
ICR = Pr[commit | zc invalid],
VR = Pr[commit | zc valid].
A useful boundary should reduce invalid-commit rate (ICR) without achieving that reduction merely
by refusing valid actions, so valid retention (VR) is reported separately.
2.2 Trust and attack surface
BSC-Rassumes a trusted eﬀect sink, trusted canonicalization code, a secret witness key, and
durable state for single-use consumption. The language model, retrieved content, tool-returned
content, and intermediate orchestration are not trusted to preserve authorization semantics. We
allow security-relevant state to change between qualiﬁcation and commit, including revocation,
authority-epoch movement, request or target substitution, policy change, procedure-context change,
and replay.
The mechanism does not protect a compromised eﬀect sink or key, and it cannot enforce a pred-
icate that its semantic projection neither observes nor validates. This last limitation is central: the
external experiment explicitly tests invariants represented by BSC-Rand additional CONTINUITY
invariants outside that projection.
3 Boundary-State Control
3.1 Joint commit witness
At qualiﬁcation time, BSC-Rissues
τ = MACk(canon(a)∥ canon(π(zq))∥n) ,
where n is a single-use nonce and π is the semantic authorization projection. The MAC only makes
the witness tamper-evident; the scientiﬁc object is the set of semantics required to remain valid at
the durability boundary.
At commit time, the sink canonicalizes the proposed eﬀect again, computes the current semantic
projection, evaluates explicit validity predicates, veriﬁes the witness, and checks that n is uncon-
sumed. If all checks pass, the sink atomically consumes n with the eﬀect; otherwise it withholds
the eﬀect. This issue–verify–consume structure follows the general systems principle that autho-
rization must be mediated at the operation actually causing the protected state transition ( Saltzer
and Schroeder , 1975; Schneider, 2000).
3.2 Semantic authorization projection
Authorization systems commonly distinguish principals, roles, delegated authority, and context
rather than equating authorization with a single opaque object identity ( Sandhu et al. , 1996; Blaze
et al. , 1996; Burrows et al. , 1990; Abadi et al. , 1993; Li et al. , 2003). BSC-Rfollows that distinc-
tion. Exact equality is retained for the canonical action and for security ﬁelds whose identity is
semantically meaningful, but not for producer-local authorization-object identiﬁers that may be
regenerated without changing eﬀective authority.
3

For the ﬁnal external adapter, π binds principal, actor, authority, delegation scope, policy iden-
tity, policy digest, policy epoch, and taint. Commit-time predicates additionally bind revocation
state, context-root presence, the actual execution subject, and external-release readiness. Non-
external data is directly eligible; external data requires the typed release expected by the adapter.
Exact action binding and durable single-use replay state remain mandatory.
This design is a form of semantic complete mediation rather than capability identity matching.
Capabilities and leases provide related ways to make authority explicit and time-sensitive ( Gray and
Cheriton, 1989; Watson et al. , 2010); usage-control models likewise emphasize that authorization
can change during use ( Park and Sandhu , 2004). BSC-Rasks which of those security semantics
must still be true at the agent’s ﬁnal eﬀect boundary.
3.3 Why semantic rather than opaque identity?
An earlier development adapter required equality of a producer-local authorization-object identi-
ﬁer. External validation showed that the producer could regenerate an equivalent authorization
object while preserving the eﬀective principal, authority, delegation, policy, and release semantics.
Treating that regenerated identiﬁer as a security change caused over-restriction.
We therefore froze the ﬁnal semantic projection before evaluating the revised mechanism. The
predecessor run and its hashes remain in the supplementary audit artifact, but the results reported
here evaluate the ﬁnal BSC-Rprojection. This distinction matters experimentally: the repaired pro-
jection changes what counts as security-relevant equality without weakening exact action binding,
revocation checks, or single-use consumption.
4 Related Work
4.1 Security enforcement under changing state
The proposal-to-commit problem has deep systems antecedents. Saltzer and Schroeder’s complete-
mediation principle requires authorization checks at each protected access ( Saltzer and Schroeder ,
1975); reference-monitor and enforceable-policy work formalizes where such checks can constrain
executions ( Harrison et al. , 1976; Schneider, 2000). Clark–Wilson integrity emphasizes well-formed
transformations over protected state ( Clark and Wilson , 1987). TOCTOU work demonstrates that
a check can become stale before use ( Bishop and Dilger , 1996), while UCON explicitly models
mutable authorization and ongoing decision factors ( Park and Sandhu , 2004).
Transaction research provides a second lineage. Serializability separates an operation’s local
execution from whether the overall history is valid ( Papadimitriou, 1979); distributed commit pro-
tocols make ﬁnality a distinct systems event ( Gray and Lamport , 2006). BSC-Rdoes not reproduce
database concurrency control. It borrows the boundary intuition: a durable eﬀect should be condi-
tioned on the state that is valid at commit, not merely on an earlier decision.
4.2 Tool-using agents and security benchmarks
ReAct and Toolformer established inﬂuential patterns for coupling language models to external
actions ( Yao et al. , 2023; Schick et al. , 2023). ToolEmu and ToolSandbox evaluate broader stateful
tool-use capabilities and risks ( Ruan et al. , 2024; Lu et al. , 2025). Security-focused benchmarks
then expose indirect prompt injection, adversarial tool use, and harmful agent behavior: InjecAgent
measures indirect injections in tool-integrated agents ( Zhan et al. , 2024); AgentDojo evaluates
attacks and defenses in dynamic environments ( Debenedetti et al. , 2024); Agent Security Bench
4

System Principal boundary object Relation to BSC-R
SecureClaw (Ma and
Schmid, 2026)
Canonical request at trusted sink BSC-Rjointly binds action plus authoriza-
tion, policy/procedure, approval, and replay-
relevant state.
Commit-Time Au-
thorization ( Santos-
Grueiro, 2026)
Fresh eﬀect-bound authority BSC-Rtests several simultaneous drift dimen-
sions rather than freshness alone.
Consent Integrity
(Weng, 2026)
Approval view bound to execution Approval/request identity is one element of
the joint witness.
CapLease ( Xu et al. ,
2026)
Durable authorization consumption Single-use state is combined with action and
current semantic context.
Cordon /
Mnemosyne ( Chen
et al. , 2026; Chang
and Geng , 2026)
Transactional task/workﬂow admis-
sion
BSC-Risolates selective acceptance at the ﬁ-
nal eﬀect boundary.
CONTINUITY
(Zheng and Yang ,
2026)
Cross-component security context External evaluation tests both shared and un-
represented invariants.
Table 1: Nearest mechanisms and the speciﬁc boundary object tested here. The table describes
overlap; it is not a superiority ranking.
systematizes multiple attack and defense families ( Zhang et al. , 2025); and AgentHarm evaluates
harmful autonomous behavior ( Andriushchenko et al. , 2025).
These benchmarks motivate defenses but primarily score end-to-end behavior. BSC-Rtargets
a narrower enforcement layer: once a proposal exists, it asks whether the exact durable eﬀect
still satisﬁes the authorization contract at commit. It is therefore complementary to prompt-level
defenses, model alignment, planning constraints, and attack detection.
4.3 Nearest commit-boundary mechanisms
Recent systems move enforcement closer to execution. SecureClaw binds canonical requests at a
trusted eﬀect sink ( Ma and Schmid , 2026); commit-time authorization requires fresh eﬀect-bound
authority ( Santos-Grueiro, 2026); Consent Integrity binds trusted approval to the action that exe-
cutes ( Weng, 2026); CapLease makes authorization consumption durable against replay ( Xu et al. ,
2026); Cordon and Mnemosyne place generated work behind transactional admission boundaries
(Chen et al. , 2026; Chang and Geng , 2026); and CONTINUITY propagates authenticated security
context across component transitions ( Zheng and Yang , 2026).
Table 1 states the overlap directly. We do not claim novelty for exact-action binding, freshness,
replay state, transactional execution, or context propagation individually. The experimental ob-
ject here is their joint proposal-to-commit consistency role under a frozen semantic authorization
projection.
5 Experimental Design
We separate four questions that otherwise become confounded in agent-security evaluations:
whether the boundary itself changes native behavior, whether each bound ﬁeld has an identiﬁable
role, whether the complete veriﬁer selectively handles post-qualiﬁcation drift, and whether the
frozen semantic projection transfers to an independently authored external suite.
5

5.1 Native corpus and independence unit
Our native corpus is the complete attacked AgentDojo run: 2,847 episodes producing 10,302 tool
proposals. AgentDojo evaluates user-task utility and adversarial objective success from environment
state rather than from model self-report ( Debenedetti et al. , 2024). Proposal-level analyses retain
the complete frozen corpus with no post-outcome subset removal. Statistical uncertainty is clustered
by AgentDojo task pair (suite, user task , injection task ); the three attack variants are nested within
each of 949 clusters.
5.2 RQ1: Does the boundary itself suppress useful behavior?
The learned transition-qualiﬁcation policy and the deterministic boundary are evaluated separately.
The binding_only condition removes learned qualiﬁcation while retaining the deterministic eﬀect-
sink kernel shared by BSC-R. We compare it episode-by-episode with the unprotected native base
agent on utility, attack outcome, committed-action count, proposal count, and infrastructure status.
5.3 RQ2: Which bindings close which drift classes?
Before outcomes were read, we froze ten post-qualiﬁcation perturbation classes: action substitution,
authorization revocation, authority-epoch change, contract-identity change, procedure-evidence
change, policy-identity change, approval-identity change, approval-request change, a joint ac-
tion/authority/contract change, and nonce replay. An unchanged control is evaluated on the same
10,302 proposals. Component conditions retain only action binding, only state/authority binding,
or only qualiﬁcation-time checks.
This layer is mechanism identiﬁcation. Because the perturbations are author-deﬁned to isolate
ﬁelds, success here establishes that the packaged veriﬁer responds to the ﬁelds it claims to bind; it
is not an independent naturalistic safety benchmark.
5.4 RQ3: Does joint binding selectively survive independent drift?
A separately frozen deterministic transition generator maps immutable record identities to one of
six families: authorization-lifecycle change, authority-epoch transition, contract/procedure-context
transition, action-target state transition, mixed transition, or no-drift control. The generator is
separate from every veriﬁer, executes after qualiﬁcation and before commit, and does not inspect
veriﬁer digests or outcomes.
Conditions are qualiﬁcation-time precheck, partial action binding, partial state/authority bind-
ing, and full joint boundary binding. The frozen primary test requires full joint binding to reduce
invalid commits relative to each alternative with paired 95% conﬁdence intervals excluding zero.
Valid retention must be non-inferior to native binding_only with a −2 percentage-point margin.
We use 50,000 paired task-cluster bootstrap replicates with RNG seed 20260918.
5.5 RQ4: Does the ﬁnal projection transfer externally?
We evaluate the ﬁnal BSC-Radapter on the original 3,460-scenario CONTINUITY suite at frozen
source commit 59cfe609.... Each scenario is paired with a same-domain, same-seed clean benign
canonical qualiﬁcation context. The ﬁnal semantic authorization projection and analysis rules
were frozen before the revised outcomes were evaluated, and the mechanism does not receive the
ground-truth validity label.
6

The target construct contains benign cases plus invalidations represented by BSC-R’s declared
projection. We report these construct-speciﬁc endpoints and, separately, the full CONTINUITY
attack suite, which contains additional provenance, release-validity, transformation/receipt, stage-
signer, alternate-path, and related invariants. This separation tests transfer without silently re-
deﬁning the mechanism after observing external failures.
We compare the ﬁnal method with a mechanism-matched contract-only baseline, a parity-
constrained CommitGuard-faithful reimplementation, and original CONTINUITY. Full-suite
counts are deterministic conformance results over this ﬁxed suite, not prevalence estimates for real
deployments.
6 Results
6.1 RQ1: Learned qualiﬁcation collapses; the boundary preserves native behav-
ior
Across all twelve learned-policy seeds, native utility is 35.054% and the learned controller collapses
to deny-all behavior. We retain this as a negative result rather than interpreting zero attack success
under blanket refusal as successful selective control.
By contrast, binding_only exactly matches the unprotected base agent on all 2,847 attacked
AgentDojo episodes for utility, attack outcome, committed-action count, proposal count, and infras-
tructure status. Aggregate utility is 80.576% and attack success is 1.616% in both conditions. The
deterministic eﬀect boundary therefore does not explain the learned controller’s utility collapse.
6.2 RQ2: Joint binding closes the targeted mechanism failures
The full joint-boundary veriﬁer accepts 10,302/10,302 unchanged commits. For each of the ten
frozen changed or replayed classes, it rejects 10,302/10,302 proposals. Component conditions fail
exactly where their omitted state matters: qualiﬁcation-time precheck cannot observe later changes;
action-only binding misses state/authority drift and replay; state/authority-only binding misses
action substitution and replay.
This result identiﬁes the roles of the bound ﬁelds but should not be read as independent evidence
of general security. The perturbation taxonomy and the veriﬁer are deliberately coupled by the
scientiﬁc hypothesis being tested.
6.3 RQ3: Independent boundary drift requires joint binding
The independently generated drift corpus contains 5,899 semantically valid and 4,403 invalid commit
contexts. Full joint binding executes the packaged issue–verify path on every row, commits 0/4,403
invalid contexts, and retains 5,899/5,899 valid contexts. Qualiﬁcation-time precheck commits every
invalid context; action-only binding commits 2,665/4,403 (60.527%); state/authority-only binding
commits 1,719/4,403 (39.042%).
Relative to precheck, action-only binding, and state/authority-only binding, full joint binding
reduces invalid commits by 100.000 percentage points (95% CI [100.000, 100.000]), 60.527 points
([59.072, 61.972]), and 39.042 points ([37.575, 40.493]), respectively. Its valid-retention diﬀerence
from 100% is 0.000 points (95% CI [0.000, 0.000]), satisfying the frozen −2 point non-inferiority
margin.
The veriﬁer also provides a falsiﬁcation trace. Every valid context returns PASS; invalid rows are
rejected by witness-digest or contract-digest mismatch according to the concrete state transition.
7

Condition ICR ↓ VR ↑
Qualiﬁcation precheck 100.000% 100.000%
Action binding only 60.527% 100.000%
State/authority only 39.042% 100.000%
F ull joint binding 0.000% 100.000%
Table 2: Boundary-drift results. ICR is invalid-commit rate; VR is valid retention.
Condition Attack invalid eﬀect ↓ Benign ↑ Ambiguous ↑ Replay ↑
BSC-R 25.000% 100% 100% 100%
Contract-only 93.750% 100% 0% 0%
CommitGuard-faithful 44.531% 100% 0% 0%
CONTINUITY 0% 100% 100% 100%
Table 3: Full external-suite comparison. These columns expose diﬀerent semantics and are not
collapsed into a scalar winner.
Scope-irrelevant transitions remain valid and are retained. This distinguishes actual boundary
execution from simply returning a hidden validity label.
6.4 Native safety–utility comparison is a tradeoﬀ, not a win
A separate prospectively rerun native lane compares the deterministic boundary-kernel condition
shared by BSC-Rwith a restrictive authority/state comparator. The boundary kernel has 1.616%
attack success and 80.576% utility; the comparator has 0.105% attack success and 69.371% utility.
With lower attack success deﬁned as safer, comparator attack success minus boundary-kernel
attack success is −1.510 percentage points, paired 95% CI [−2.213, −0.878]. The boundary kernel’s
utility advantage is +11.205 points, 95% CI [8.535, 13.909]. Thus the boundary condition is not
demonstrated to dominate stronger restriction on native attack success. The comparison instead
exposes two control regimes: restriction can suppress more attacks by suppressing more benign
execution, while boundary consistency targets whether already-qualiﬁed actions remain valid at
commit.
6.5 RQ4: External validation succeeds on represented invariants and fails be-
yond them
The ﬁnal external run completes all 3,460 scenarios with zero infrastructure failures. On the
prospectively speciﬁed target construct, BSC-Rretains 300/300 target-relevant benign cases and
700/700 benign cases overall. It prevents eﬀects on 1,200/1,200 represented non-replay invalid cases,
handles 160/160 replay lifecycles with the required execute-once behavior, and withholds commit
on 200/200 ambiguous external/no-release cases. A row-only recomputation reproduces the runner
summary exactly.
The complete external suite gives a diﬀerent, deliberately broader view. Across all 2,560 CON-
TINUITY attack scenarios, BSC-Rcommits invalid eﬀects in 25.000% of cases. The contract-only
baseline commits 93.750%, the CommitGuard-faithful implementation 44.531%, and CONTINU-
ITY 0%. Benign retention is 100% for all four. Ambiguous no-commit correctness and replay
lifecycle correctness are 100% for BSC-Rand CONTINUITY and 0% for the two narrower com-
parators.
8

The residual BSC-Rfailures concentrate in provenance, release-validity, transformation/receipt,
stage-signer, alternate-path, and related invariants absent from its semantic projection. The result
therefore falsiﬁes any interpretation that the internal 0% ICR establishes complete external safety.
At the same time, the all-benign retention and perfect correctness on represented non-replay, replay,
and ambiguous-release cases show that the ﬁnal projection is not merely a deny-all rule.
7 Discussion
7.1 The projection is the security boundary
The experiments suggest that commit-time enforcement has two separable requirements: a trust-
worthy enforcement point and an adequate semantic projection. The internal architecture and drift
tests isolate the ﬁrst. Once the relevant action and state ﬁelds are represented, joint issue–verify–
consume enforcement prevents the corresponding stale or substituted commits without refusing
unchanged controls.
The external suite isolates the second requirement. A mechanically correct veriﬁer cannot
enforce semantics that its projection omits. This is why BSC-Rcan be simultaneously perfect on
its represented target construct and incomplete on the full CONTINUITY suite. The operative
design question is therefore not “does the token match?” but “does the token commit to every
security fact whose change should invalidate this eﬀect?”
7.2 Stable semantics can matter more than object identity
The semantic-projection repair exposes a second lesson. Security mechanisms often need iden-
tity, but the relevant identity is the one tied to authority semantics. Requiring equality of an
implementation-local authorization object can create false revocation when an equivalent object is
regenerated. Conversely, dropping identity too aggressively can admit privilege substitution. The
correct boundary therefore depends on which ﬁelds are constitutive of authority and which are
incidental representations.
This observation connects agent execution to older authorization work that separates principals,
roles, delegation, and contextual conditions ( Sandhu et al. , 1996; Abadi et al. , 1993; Li et al. , 2003).
BSC-Roperationalizes that distinction at a language-model agent’s eﬀect sink. The ﬁnal projection
is one concrete choice, not a universal schema.
7.3 Why not solve the problem with a stronger refusal policy?
The native comparator demonstrates why attack success alone is insuﬃcient for this question. A
restrictive policy can lower attack success by declining more actions. That may be appropriate in
some deployments, but it is a diﬀerent control objective from preserving an authorized transition
while invalidating it only when the relevant state changes.
Our evaluation therefore keeps safety and retention endpoints separate. This follows the same
systems logic that motivates least privilege and complete mediation: enforcement should constrain
unauthorized transitions, but an enforcement mechanism is not characterized solely by how often it
refuses. For agent deployments, the practical design space includes model-level ﬁltering, restrictive
deterministic policies, and commit-time consistency checks; these can be composed rather than
treated as mutually exclusive alternatives.
9

7.4 Implications for agent architecture
A language model is a useful proposer but a poor place to store ﬁnal authority. Its context may
contain stale, untrusted, or indirectly injected information, and its reasoning trace is not an atomic
transaction with the external system. A trusted eﬀect boundary can instead receive the model’s
proposal as data, re-derive security-relevant commit context from authoritative sources, and decide
whether the transition remains admissible.
This architecture does not make model behavior irrelevant. Bad proposals still waste work
and may expose other risks. It does, however, relocate one class of correctness property from
probabilistic generation to deterministic enforcement. In that sense, BSC-Ris closer to a reference
monitor for agent eﬀects than to another prompt-injection classiﬁer.
8 Conclusion
Tool-using agents create a proposal-to-commit interval in which authorization, policy, targets, ap-
provals, and replay state can change. BSC-Rtreats that interval as an explicit systems boundary:
exact actions are bound to a single-use witness over stable authorization semantics, and the current
state is checked again where the external eﬀect becomes durable.
Across the native and prospectively frozen drift experiments, the deterministic boundary pre-
serves valid execution while rejecting the state changes it represents. The external CONTINUITY
evaluation conﬁrms both sides of the claim: the ﬁnal semantic projection retains all 700 benign
cases and handles every represented non-replay, replay, and ambiguous-release case correctly, yet
still permits invalid eﬀects on 25% of the complete attack suite because additional security invari-
ants are outside its projection. Commit-time consistency is therefore useful only to the extent that
the boundary represents the semantics that matter.
9 Limitations
The native evidence is not an estimate of real-world failure prevalence. Its 10,302 proposals come
from 2,847 attacked AgentDojo episodes, and the architecture-closure perturbations are author-
designed to test mechanism-relevant ﬁelds. Even the independently generated boundary-drift fam-
ilies remain synthetic state transitions over a benchmark corpus. The 0/4,403 invalid-commit and
5,899/5,899 valid-retention counts therefore establish conformance and selective behavior on the
frozen experiment, not universal deployment safety.
The external CONTINUITY suite is independently authored and substantially broader, but
BSC-Rintentionally represents only a subset of its security invariants. This limitation is quantita-
tive rather than hypothetical: BSC-Rpermits invalid eﬀects on 25% of the 2,560 full-suite attacks
while CONTINUITY permits 0%. The residual families include provenance, release-validity, trans-
formation/receipt, stage-signer, alternate-path, and related checks absent from the declared projec-
tion. Accordingly, the 1,200/1,200 represented non-replay prevention result must not be generalized
to invariants the mechanism does not encode.
The ﬁnal semantic projection was motivated by development evidence showing that opaque
authorization-object identity could be overbound. We froze the revised projection before evaluating
its outcomes and preserve the predecessor run in the audit artifact, but this development path
still means that future adapters require independent validation of which ﬁelds constitute authority.
Replay resistance assumes durable consumption state, and all guarantees assume an uncompromised
eﬀect sink, key, canonicalizer, and authoritative commit-time data sources.
10

Finally, the learned qualiﬁcation model remains a deny-all negative result, and the determin-
istic boundary kernel does not dominate a restrictive native comparator on attack success. The
comparator reaches 0.105% attack success versus 1.616% for the boundary kernel while sacriﬁcing
11.205 percentage points of utility. We therefore do not claim that BSC-Ris the safest general-
purpose agent controller or that commit-time consistency substitutes for model-level or policy-level
defenses.
10 Ethical Considerations
This work studies defensive enforcement for tool-using agents and includes adversarial benchmark
scenarios involving potentially harmful actions. The experiments use benchmark environments
and ﬁxed external evaluation suites rather than deployment against third-party systems. The
supplementary artifact contains code and traces necessary to reproduce the reported controls; it
does not provide credentials or access to real protected services.
The main deployment risk is overclaiming the scope of a deterministic boundary. A veriﬁer can
appear reliable while omitting a security predicate that matters in the target environment. We
therefore report the complete external failure regime, retain negative results, and avoid a scalar
“safety” score that could hide refusal-based utility loss or unrepresented invariants.
References
Martín Abadi, Michael Burrows, Butler Lampson, and Gordon Plotkin. A calculus for access
control in distributed systems. ACM Transactions on Programming Languages and Systems , 15
(4):706–734, 1993. doi: 10.1145/155183.155225.
Maksym Andriushchenko, Alexandra Souly, Mateusz Dziemian, Derek Duenas, Maxwell Lin, Justin
Wang, Dan Hendrycks, Andy Zou, J. Zico Kolter, Matt Fredrikson, Yarin Gal, and Xander Davies.
Agentharm: A benchmark for measuring harmfulness of llm agents. In International Conference
on Learning Representations , 2025.
Matt Bishop and Michael Dilger. Checking for race conditions in ﬁle accesses. Computing Systems ,
9(2):131–152, 1996.
Matt Blaze, Joan Feigenbaum, and Jack Lacy. Decentralized trust management. In IEEE Sympo-
sium on Security and Privacy , pages 164–173, 1996. doi: 10.1109/SECPRI.1996.502679.
Michael Burrows, Martín Abadi, and Roger M. Needham. A logic of authentication. ACM Trans-
actions on Computer Systems , 8(1):18–36, 1990. doi: 10.1145/77648.77649.
Edward Y. Chang and Longling Geng. Mnemosyne: Agentic transaction processing for validating
and repairing ai-generated workﬂows, 2026.
Zheng Chen, Hanqing Liu, Duling Xu, Dong Dong, Jialin Li, Bangzheng Pu, and Jidong Zhai.
Cordon: Semantic transactions for tool-using llm agents, 2026.
David D. Clark and David R. Wilson. A comparison of commercial and military computer security
policies. In IEEE Symposium on Security and Privacy , pages 184–195, 1987. doi: 10.1109/SP.
1987.10001.
11

Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, and Florian
Tramèr. Agentdojo: A dynamic environment to evaluate prompt injection attacks and defenses
for llm agents. In Advances in Neural Information Processing Systems , 2024. doi: 10.52202/
079017-2636.
Cary G. Gray and David R. Cheriton. Leases: An eﬃcient fault-tolerant mechanism for distributed
ﬁle cache consistency. In Proceedings of the 12th ACM Symposium on Operating Systems Prin-
ciples, pages 202–210, 1989. doi: 10.1145/74850.74870.
Jim Gray and Leslie Lamport. Consensus on transaction commit. ACM Transactions on Database
Systems, 31(1):133–160, 2006. doi: 10.1145/1132863.1132867.
Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, and Mario
Fritz. Not what you’ve signed up for: Compromising real-world llm-integrated applications with
indirect prompt injection, 2023.
Michael A. Harrison, Walter L. Ruzzo, and Jeﬀrey D. Ullman. Protection in operating systems.
Communications of the ACM , 19(8):461–471, 1976. doi: 10.1145/360303.360333.
Ninghui Li, Benjamin N. Grosof, and Joan Feigenbaum. Delegation logic: A logic-based approach to
distributed authorization. ACM Transactions on Information and System Security , 6(1):128–171,
2003. doi: 10.1145/605434.605438.
Jiarui Lu, Thomas Holleis, Yizhe Zhang, Bernhard Aumayer, Feng Nan, Haoping Bai, Shuang Ma,
Shen Ma, Mengyu Li, Guoli Yin, Zirui Wang, and Ruoming Pang. Toolsandbox: A stateful,
conversational, interactive evaluation benchmark for llm tool use capabilities. In Findings of the
Association for Computational Linguistics: NAACL 2025 , 2025.
Yuhan Ma and Stefan Schmid. Secureclaw: Clawing back control of llm agents, 2026.
Christos H. Papadimitriou. The serializability of concurrent database updates. Journal of the ACM ,
26(4):631–653, 1979. doi: 10.1145/322154.322158.
Jaehong Park and Ravi Sandhu. The uconabc usage control model. ACM Transactions on Infor-
mation and System Security , 7(1):128–174, 2004. doi: 10.1145/984334.984339.
Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann
Dubois, Chris J. Maddison, and Tatsunori Hashimoto. Identifying the risks of lm agents with an
lm-emulated sandbox. In International Conference on Learning Representations , 2024.
Jerome H. Saltzer and Michael D. Schroeder. The protection of information in computer systems.
Proceedings of the IEEE , 63(9):1278–1308, 1975. doi: 10.1109/PROC.1975.9939.
Ravi S. Sandhu, Edward J. Coyne, Hal L. Feinstein, and Charles E. Youman. Role-based access
control models. Computer, 29(2):38–47, 1996. doi: 10.1109/2.485845.
Igor Santos-Grueiro. Temporary authority, permanent eﬀects: Commit-time authorization for llm
agents, 2026.
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Eric Hambro,
Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom. Toolformer: Language models can
teach themselves to use tools. In Advances in Neural Information Processing Systems , 2023.
12

Fred B. Schneider. Enforceable security policies. ACM Transactions on Information and System
Security, 3(1):30–50, 2000. doi: 10.1145/353323.353382.
Robert N. M. Watson, Jonathan Anderson, Ben Laurie, and Kris Kennaway. Capsicum: Practical
capabilities for unix. In 19th USENIX Security Symposium , 2010.
Xiaoqi Weng. What you approve is what executes: Consent integrity for black-box llm agents,
2026.
Jinghan Xu, Longze Fan, Zeyuan Wang, Xinjin Li, and Hankai Liu. Beyond single-use tokens:
Durable authorization state for replay-resistant llm agent actions, 2026.
Shunyu Yao, Jeﬀrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik R. Narasimhan, and Yuan
Cao. React: Synergizing reasoning and acting in language models. In International Conference
on Learning Representations , 2023.
Qiusi Zhan, Zhixiang Liang, Zifan Ying, and Daniel Kang. Injecagent: Benchmarking indirect
prompt injections in tool-integrated large language model agents. In Findings of the Association
for Computational Linguistics: ACL 2024 , pages 10471–10506, 2024. doi: 10.18653/v1/2024.
ﬁndings-acl.624.
Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu Zhan, Hongwei
Wang, and Yongfeng Zhang. Agent security bench (asb): Formalizing and benchmarking attacks
and defenses in llm-based agents. In International Conference on Learning Representations, 2025.
Chris Zheng and Geng Yang. Continuity: Security-context contracts for composable llm agent
controls, 2026.
13

AI Use Statement
Generative AI tools were used substantially in research ideation, literature triage, experiment or-
chestration and code generation, manuscript drafting and editing, and artifact and format quality
assurance. Scientiﬁc endpoints, comparators, thresholds, and failure rules for the conﬁrmatory ex-
periments reported as prospective were frozen before their outcomes were inspected. AI-assisted
code and claims were checked against raw artifacts, hashes, and cited primary sources. The au-
thors reviewed the AI-assisted work and take responsibility for the ﬁnal content, claims, code, and
artifacts.
Reproducibility Statement
The supplementary reviewer artifact contains frozen protocols, row-level outputs, experiment
runners, correction ledgers, native episode outputs, and SHA-256 manifests for the mechanism,
boundary-drift, native-comparator, and ﬁnal external BSC-Rresults. It also preserves the prede-
cessor external run that motivated the semantic authorization projection, the pre-outcome repair
freeze, supersession record, comparator-conformance correction, evaluator-independence audit,
exact ﬁnal rows, and row-only recomputation.
A Frozen Protocols and Provenance
Architecture closure. The prospective architecture-closure freeze has SHA-256 a2b4e07a
ae61...; the corrected row artifact has SHA-256 0d223453ecb7.... Two harness corrections were
recorded before a valid closure result: unique single-use approval/request identities per proposal
and use of the already-canonical issuance approval at veriﬁcation. Neither correction changed the
source corpus, perturbation classes, thresholds, BSC runtime, or subset policy.
Boundary drift. Boundary-drift v1.0 is explicitly invalidated for circular validation and is not
evidence. The corrected v1.1 prospective freeze SHA-256 is ac00335e5ab1...; runner SHA-256 is
85a4a420d1f7...; result-row SHA-256 is 386f7112792d...; and authoritative summary SHA-256
is b14fd1b20f92.... There are 10,302 proposal rows and 949 task-pair clusters; bootstrap seed is
20260918. The original frozen runner completed all 50,000 paired cluster-bootstrap replicates used
in the main text.
Native comparator. The correctly directed native-comparator freeze SHA-256 is ec5b6fe3
b3d6.... A forensic audit found that the ﬁrst analysis artifact accidentally used bootstrap RNG
seed 20260916 instead of the frozen 20260917. Raw native outcomes, endpoints, cluster unit, thresh-
olds, and conditions were unchanged. The authoritative corrected analysis is v1.0.1, SHA-256
d103847d062a...; correction-ledger SHA-256 is c1cefecbd963.... The corrected intervals are
numerically unchanged at the displayed precision.
External validation. The artifact preserves the predecessor external-closure result as de-
velopment provenance, including summary SHA-256 4681f3869961... and rows SHA-256
967531558f8b.... Before evaluating the revised mechanism, the semantic-projection freeze was
ﬁnalized at SHA-256 b484735275d0.... The ﬁnal runner SHA-256 is 141d832072db..., repaired
14

rows SHA-256 52818bf021f0..., and summary SHA-256 3c2ac415b136.... The ﬁnal run com-
pleted all 3,460 scenarios with zero infrastructure failures, and row-only recomputation matches
the runner summary.
B Architecture-Closure Counts
Condition Accept Reject
Unchanged control 10,302 0
Action substitution 0 10,302
Authorization revocation 0 10,302
Authority-epoch change 0 10,302
Contract-identity change 0 10,302
Procedure-evidence change 0 10,302
Policy-identity change 0 10,302
Approval-identity change 0 10,302
Approval-request change 0 10,302
Joint action/authority/contract 0 10,302
Nonce replay 0 10,302
C Boundary-Drift Family Counts
The frozen deterministic mapping produced 1,778 authorization-lifecycle changes, 1,737 authority-
epoch transitions, 1,684 contract/procedure-context transitions, 1,745 action-target state transi-
tions, 1,727 mixed transitions, and 1,631 no-drift controls. The generator does not inspect veriﬁer
digests or outcomes.
D Negative Learned-Policy Result
The learned qualiﬁcation policy was evaluated for seeds
{101, 151, 211, 271, 331, 401,
461, 521, 601, 661, 751, 811}.
Every seed reports utility 0.3505444327 and attack success 0 under the native run, consistent with
deny-all collapse. This result is not averaged with the deterministic boundary and is not used as
evidence that learned representation improves control.
E Latency
The isolated full-BSC issue+verify mechanism previously measured median 87.0 µs, p95 101.4 µs,
and p99 115.0 µs on unchanged controls. A later architecture-closure harness that deliberately
exercises the persistent authorization-consumption store measured median 21.1 ms, p95 39.6 ms,
and p99 62.2 ms. These are diﬀerent execution paths and are not conﬂated.
F Artifact Policy
The reviewer package includes prospective freezes, row-level outputs, runners, correction ledgers,
native parity evidence, corrected comparator analyses, preserved predecessor external evidence,
15

ﬁnal BSC-Rexternal evidence, evaluator-independence audit, and a SHA-256 manifest. Historical
or invalidated artifacts remain explicitly labeled. No post-outcome endpoint, subset, comparator,
or threshold change is promoted as frozen evidence; implementation-conformance corrections are
preserved with their superseded artifacts.
16
