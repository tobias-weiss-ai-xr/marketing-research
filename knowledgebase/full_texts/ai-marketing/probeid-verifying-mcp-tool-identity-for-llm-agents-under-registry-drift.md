---
title: 'ProbeID: Verifying MCP Tool Identity for LLM Agents under Registry Drift'
url: https://arxiv.org/abs/2610.33633
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Guanxing Chen
- Sining Zhang
- Haohuai He
- Qiujie Lv
- Yu-An Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.33633
pages: 41
chars: 181028
fetched_at: '2026-11-08T13:35:41+00:00'
kb_version: 1
---

# ProbeID: Verifying MCP Tool Identity for LLM Agents under Registry Drift

PROBEID: VERIFYINGMCP TOOLIDENTITY FOR
LLM AGENTS UNDERREGISTRYDRIFT
PREPRINT
Guanxing Chen1,*, Sining Zhang1, Haohuai He2, Qiujie Lv3, Yu-An Huang4,*, and Zhi-An Huang1,*
1City University of Hong Kong (Dongguan), Dongguan, China
2The Hong Kong Polytechnic University, Hong Kong SAR, China
3Zhengzhou University, Zhengzhou, China
4Northwestern Polytechnical University, Xi’an, China
*Corresponding authors: Guanxing Chen (guanxing.chen@cityu-dg.edu.cn), Yu-An Huang (yuanhuang@nwpu.edu.cn)
and Zhi-An Huang (huang.za@cityu-dg.edu.cn)
October 27, 2026
ABSTRACT
Agents select tools by copyable descriptions, which cannot establish which implementation runs.
ProbeID compares canonicalized responses to schema-valid probes with a trusted admission refer-
ence and abstains on ambiguity, so a squatter must copy probe-observable behavior. With the gold
present, independent probes and a fixed margin, standard concentration arguments give a shared
probe budget logarithmic in the candidate count and bound the joint probability of a wrong decision.
On cached MCP-IdentityDrift cases, strict choice reaches0.956hit@1 while description routers fall
near chance, but simpler exact comparisons tie it, MMD better tolerates heavy value noise, and a
32B behavioral judge is similarly accurate at higher cost. Random probes from agent banks and a
prospective held-out study of38tools test theory-set thresholds. On the agent banks, equality refuses
every reachable replacement from64probes and the bounded distance from512, and sharper post
hoc gates halve both. Two tools whose drift no bank probe reaches always pass. In an MCP-Bench
agent, verification cuts tainted tasks from15to9of16at unchanged task success. Over eleven
weeks,7of59real tools changed responses despite version pins. Verification depends on reference
integrity, probe coverage, and response noise.
1 Introduction
Large language model (LLM) agents increasingly act through external tools, and the Model Context Protocol (MCP)
has turned this into a fast-growing open ecosystem of community-published tool servers (Model Context Protocol,
2025; Song et al., 2026). An agent that needs a capability searches a large registry and ranks tools by their advertised
descriptions (Qin et al., 2024; Fei et al., 2025), so unauthenticated, attacker-editable text decides which implementation
runs (Sneh et al., 2025). Audits find most tool descriptions underspecified (Hasan et al., 2026), server behavior
departing from the descriptions at registry scale (Li et al., 2026), and squatting among the main attack vectors (Maloyan
& Namiot, 2025). The protocol’s security interest group lists runtime drift and tool identity as open problems (Model
Context Protocol, 2026).
However, description routing and admission-time binding both assume that declared metadata fixes behavior, and reg-
istry drift breaks that assumption. A squatter copies the description of a trusted tool but implements different behavior
(Beurer-Kellner & Fischer, 2025a; Wang et al., 2025b), so a description router admits it and may select it. Admission
controls bind definitions or provenance (Bhatt et al., 2025; Narajala et al., 2026; Metere, 2026), but a definition bound
at admission does not expose a later change in behavior. In an adaptive-distractor setting, certified correctness of
metadata-based selection falls to about twenty percent after ten rounds (Yeon et al., 2026). No description matcher
can recover the intended tool from identical descriptions.
arXiv:2610.33633v1  [cs.CR]  24 Oct 2026

ProbeIDPREPRINT
(a)Metadata ambiguity (b)Reference admission
Which tool?
LLM agent
probe x
TA
 TB
name: toolX name: toolX
schema: S schema: S
≠
Same metadata, different responses
x1
x2
xB
Schema-valid
probes
fref
Trusted tool
admission only
c(·)
request_id
timestamp
value: [...]
Canonicalize
Attested reference bank
xj c(fref(xj))
Behavioral comparison Identify or abstain
Secret probes
Same inputs for
every candidate
Candidates
T1
T2
T3
c(·)
request_id
timestamp
value: [...]
Canonicalize
Behavioral fingerprints
...
...
...
...
x1 x2 ... xm
ref
T1
T2
T3
retained changed
Average paired distance over the same m probesref t
vs. Δm(ft, fref) = 1/m Σ dY(c(ft(xi)), c(fref(xi)))
m
i = 1
Nearest match
with a clear gap
d(1) d(2) τhi
gap
0 distance
Both conditions must pass
d(1) ≤ τhi
AND d(2) − d(1) ≥ γmin
Identify
 Abstain
both pass otherwise
(c) (d)
Secret probe subset
Stored responses
Figure 1:Behavior decides what copied metadata cannot.(a) Identical tool metadata can hide different responses.
(b) Admission stores canonicalized trusted responses to schema-valid probes (M1). (c) Selection sends secret bank
probes to candidates and compares their paired responses with the stored reference (M2 to M4). (d) Multiple candidates
pass the distance and gap gates (M5), while a sole candidate faces only the distance gate. ProbeID otherwise abstains
(M6). Glyphs, names, and distances are schematic.
To remove the dependence on declared metadata, we identify a tool by its behavior, as black-box model fingerprinting
identifies a model (Pasquini et al., 2025; Gao et al., 2025). Behavioral identity here means agreement of probe-
observable responses with a reference recorded at admission, not endpoint or cryptographic identity. Probing can-
didates at selection time and comparing what they return forces a squatter to match behavior rather than text. The
comparison observes only responses, so the probes must reach the difference and the reference must be trusted (Fig-
ure 1).
ProbeID is a post-admission behavioral verifier that generates schema-driven probes, canonicalizes the responses,
and selects the candidate nearest the reference under a bounded behavioral distance, abstaining when no candidate
matches or the decision is ambiguous. At a fixed margin, addingksquatters raises the number of shared probe inputs
only by a logarithmic factor, while a router the squatters mimic falls to chance1/(k+ 1). We validate the protocol on
MCP-IdentityDrift, built from real cached tool behavior (Guo et al., 2024) with injected schema-compatible squatters,
and test its error bounds with random probes from the attested banks of an agent study and from a prospective held-
out study. The contribution is the protocol, which does not depend on one comparison. Exact equality ties the
bounded distance on the cached cases and verifies deterministic drift with fewer probes, and a set-level maximum
mean discrepancy (MMD) tolerates heavy value noise better.
Our contributions are as follows.
• A reference-based verification protocol that separates identity selection from abstention (Algorithm 1) and
calibrates both with standard concentration arguments. For independent probes it needs a shared budget
m=O(γ −2 log((n+k)/δ))and, with the gold present, keeps the joint probability of a wrong decision below
2

ProbeIDPREPRINT
δ, with a matching lower bound on the leading term under independent candidate channels (Appendices B
to F).
• MCP-IdentityDrift and an evaluation that separates operating points (Table 1). Routers approach1/(k+ 1)
under copied-description rug pull while ProbeID reaches0.956strict-choice hit@1. Random probes from the
agent banks and from a prospective held-out study show where theory-set thresholds refuse replacements and
where their resolution ends (Result 2). An agent gate cuts tasks tainted by the rug pull from15to9of16, a
harm that task success does not register (Result 4).
• A census of16real published MCP servers re-probed eleven times over eleven weeks. Canonicalization
succeeds on every recorded response, most tools are deterministic, and7of59depart from their recorded
responses under unchanged version pins, three of them after a reinstall at unchanged versions (Appendix O).
2 Related work
Tool retrieval and selection.Tool selection is usually cast as retrieval over descriptions. ToolLLM trains a dense
retriever (Qin et al., 2024) and MCP-Zero discovers tools from server metadata (Fei et al., 2025). Bridge models
recover part of what dense retrieval loses under vague instructions (Chen et al., 2026), rerankers over tool cards add
little (Shi et al., 2025), and documentation augmentation improves descriptions (Fang et al., 2025). All select using
descriptions, so a copied description inherits its retrieval score.
Tool ecosystem security.Squatting, description tampering and rug pulls are documented in the MCP ecosystem,
whose specification treats self-declared tool annotations as untrusted (Model Context Protocol, 2025; Maloyan &
Namiot, 2025; Song et al., 2026). Disclosures, taxonomies and benchmarks report tool poisoning, rug pulls and
message history exfiltration in deployed servers (Beurer-Kellner & Fischer, 2025a; Kosman, 2025; Beurer-Kellner &
Fischer, 2025b; Song et al., 2026; Wang et al., 2025b). Admission defenses bind immutable definitions, registry trust
or provenance (Bhatt et al., 2025; Narajala et al., 2026; Metere, 2026; Mas et al., 2026), and runtime detectors screen
for deviation from declared intent or for injected content (Huang et al., 2026; Zhou et al., 2026; Xing et al., 2026),
without a trusted reference or selection among squatters. ProbeID complements these defenses at use time. It detects
an admitted rug pull when the trusted reference and the drawn probes expose the change, and it cannot see exfiltration
that leaves responses unchanged.
Certification of tool selection.LLMCert-T, the closest formal neighbor, certifies a tool selection pipeline over its
metadata and finds certified correctness collapsing under adaptive distractors (Yeon et al., 2026). ProbeID instead
gives a conditional guarantee from probe-observable behavior under an explicit margin model, and composing it with
a certificate over metadata is left open.
Identity from behavior.Examining an artifact itself rather than its declared metadata recurs across conformance and
differential testing, query learning, stateful API fuzzing, network service scanning, software birthmarks, and black-
box model fingerprinting (Chow, 1978; McKeeman, 1998; Angluin, 1987; Atlidakis et al., 2019; Lyon, 2009; Tamada
et al., 2004; Myles & Collberg, 2005; Podgurski & Pierce, 1993; Pasquini et al., 2025; Shao et al., 2026; Gao et al.,
2025; Zhu et al., 2026; Karvonen et al., 2025; Zhang et al., 2026). Model Equality Testing uses a two-sample test to
check whether an API still serves a trusted model, and LLMmap identifies which of a known set of models produced a
set of traces, so selection among candidates alone does not distinguish ProbeID. Here the candidates are adversarially
authored to share a schema and a description. ProbeID pairs the margin the probes must reach with a budget bound, a
matching lower bound on its leading term, and an abstention rule with a joint error bound (Appendix A).
Concurrent work.Concurrent work generates schema-valid probes for MCP servers to adjudicate execution risk
rather than identity (An et al., 2026) and measures how far an agent skill’s behavior departs from its declared capa-
bility (Wu et al., 2026). Other work tracks LLM endpoint stability and agent workflow regressions with behavioral
fingerprints (Leshin et al., 2026; Bhardwaj, 2026), and TrustShiftProbe audits live payloads against baselines learned
while a server was trusted (Rostamzadeh et al., 2026). Each checks one artifact against its own declaration or history,
whereas ProbeID probes all candidates on inputs with recorded trusted responses and selects among them.
3

ProbeIDPREPRINT
3 Behavioral tool identity
3.1 Problem setup
An LLM agent receives a user intentqand a registryRofntools, to which drift can add up toksquatters. A tool
thas a descriptiondesc(t), a typed schemaS t defining the valid inputsX t, and a behaviorf t :X t →Y t, a partial
and possibly stochastic map returning an output, a status code and a state delta. A description router forms candidates
C(q)⊆Rby lexical or semantic similarity.
Lett ⋆ be the gold tool whose behaviorqrequires. Registry drift introduces schema-compatible squatters that copy or
approximatedesc(t ⋆)with different behavior, description edits, and name or schema mimicry. The task is behavioral
identity recovery, which returns a singleˆc∈C(q)behaviorally equivalent tot ⋆, orABSTAINwhen no candidate is
confidently identifiable. Two tools are behaviorally equivalent on a probe distributionDover schema-valid inputs
when their canonicalized responses agree forD-almost every probe on the observed channels. A decision incurs the
0/1identity lossL id(ˆc) =1[ˆcnot equivalent tot⋆], and an abstention is counted separately as lost coverage. This
notion is weaker than endpoint identity and cannot see side effects that never reach a response, behavior outside the
probe support, or a reference recorded from a compromised tool. A tool that exfiltrates message history (Beurer-
Kellner & Fischer, 2025b) while preserving every probe-visible response ties the gold when both are candidates and
passes the single-candidate gate when it replaces the gold.
3.2 ProbeID
ProbeID is a post-admission runtime verifier. At admission each tool’s trusted reference behaviorfref is recorded as an
attested bank ofBschema-valid probes with their canonicalized responses. At selection ProbeID secretly subsamples
mbank probes and probes only the current candidates, so no live reference endpoint is needed.
Schema-driven probes (M1).ProbeID generates the bank at admission by type-aware enumeration over boundary
values, enums, and required or optional fields (Appendix L.1), and selection draws a secret subsample{x 1, . . . , xm}.
Theorem 1 models probes as i.i.d. draws fromD. The same bound holds for uniform sampling without replacement
from the attested bank withDread as the bank distribution, and a population margin transfers to the bank only if the
bank was itself sampled from that population (Appendix B). Pure deterministic enumeration is a heuristic outside the
guarantee, and heterogeneous or aliased schemas are filtered upstream.
Canonicalization and bounded distance (M2, M3).A canonicalizerc(·)drops named volatile fields such as times-
tamps and request ids and sorts mapping keys. A bounded distanced Y ∈[0,1]then scores structural disagreement
over the response tree, with status codes and state deltas as further channels combined by a probabilistic union (Ap-
pendix E). The analysis does not need this distance to dominate other paired comparisons.
Behavioral distance and identity rule (M4, M5).For the probe distributionD, the behavioral distance between
two tools is
∆(f, g) =Ex∼D

dY (c(f(x)), c(g(x)))

.(1)
∆is bounded and symmetric, and the analysis needs only these properties and the margin, not a triangle inequal-
ity. Deterministic tools have∆(f, f) = 0. Stochastic tools may have positive self distance∆(f, f) =µ t⋆ ≥0
between two independent responses to the same probe. The empirical estimate overmshared probes is b∆m(f, g) = 1
m
Pm
i=1 dY (c(f(x i)), c(g(xi))), the behavioral fingerprint oftisϕ(t) = (c(f t(x1)), . . . , c(ft(xm))), and given a trusted referencef ref the nearest-fingerprint rule selects
ˆc= arg min
t∈C(q)
b∆m(ft, fref ).(2)
Abstention and escalation (M6).ProbeID returnsABSTAINwhen the smallest distance exceedsτ hi, so no candidate
matches the reference, or when the gap to the second nearest is belowγ min, so identity is ambiguous (Algorithm 1).
The caller may then escalate to confirmation or to the description router, whose choice does not inherit the behavioral
error bound. A single registered candidate, such as an endpoint a squatter replaced, faces only the absolute gate
(Appendix C).
4 Identity guarantee under squatting
We now state when the nearest-fingerprint rule in Equation (2) is correct. The key quantity is a behavioral separation
margin.
4

ProbeIDPREPRINT
Algorithm 1ProbeID identity verification
1:Input:candidatesC(q), attested bank{(x j, c(fref (xj)))}B j=1, budgetm, thresholdsτ hi, γmin
2:secretly subsamplex 1, . . . , xm with their bank referenceϕ(ref)(M1)
3:foreacht∈C(q)do
4:ϕ(t)←(c(f t(x1)), . . . , c(ft(xm)))andd t ← b∆m(ft, fref )(M2 to M4)
5:sortd (1) ≤d (2) ≤ · · ·
6:if|C(q)|= 1then
7:returnthe sole candidate ifd (1) ≤τ hi, elseABSTAIN
8:ifd (1) > τhi ord (2) −d (1) < γmin then
9:returnABSTAIN (M6)
10:returnarg min t dt (M5)
Definition 1(Margin).Writeµ t = ∆(f t, fref )for the expected behavioral distance of candidatetto the reference,
the expectation taken over both the probesx∼Dand any tool randomness. A candidate set has marginγif every
behaviorally wrong candidatewis separated from the gold in mean,µ w −µ t⋆ ≥γonD.
The margin depends on the probe distribution. For a deterministic gold that matches the reference pointwise,γis
positive exactly when every squatter has positive distance on a set of positive probe mass (Appendix D). A squatter
at zero distance onDis equivalent to the gold under this comparison, and any harm it does lies outside the probe
support. A faithful deterministic gold has self distance0.00, as on the deterministic census tools (Appendix O), and
the varianceσ 2 covers sampled inputs and response randomness. Theorem 1 assumes observations independent across
probes, so stateful tools lie outside it and are treated empirically (Appendix M).
Theorem 1(Probe complexity).Letd Y ∈[0,1], and suppose the candidate pool contains the gold toolt ⋆ among at
mostn+ktools with marginγ >0. Drawmprobes i.i.d. fromD, with per-probe observations independent given
the probes. For anyδ∈(0,1), if
m > 2 γ2 log 2(n+k) δ ,(3)
then the nearest-fingerprint rule returns a behaviorally correct tool with probability at least1−δ.
The proof combines Hoeffding’s inequality (Hoeffding, 1963) with a finite-class union bound (Shalev-Shwartz & Ben-
David, 2014) (Appendix B), and the gap gate below is the stopping rule of action elimination (Even-Dar et al., 2006).
For a pool with the gold and at least two candidates, Algorithm 1 usesγmin = 2ϵ, whereϵ=
p
log(2(n+k)/δ)/(2m),
andτ hi at leastϵabove the gold self distance. Under the stated sampling conditions, the probability of deciding and
being wrong is at mostδ, and the rule returns a correct candidate whenγ≥4ϵand no twin of the gold is present
(Theorem 2). The bound is on the joint event, and among decided cases the error is bounded only byδ/P(decide), so
an observed error rate among decisions is not aδ-level certificate. A sole candidate faces only the absolute gate, and
withτ hi exactlyϵabove the gold self distance it refuses a replacement with probability at least1−δwhen its margin
exceeds2ϵ(Appendix C).
At a fixed margin,kschema-compatible squatters affect the shared-probe budget throughlog((n+k)/δ). Querying
every candidate still requires up tom(n+k)candidate tool calls, besides the one-time admission calls that record the
bank.
Variation and theσ 2 factor.Hoeffding gives the worst-case1/γ 2 rate. When the per-probe distance has variance
at mostσ 2, a Bernstein bound givesm >  8σ2γ−2 + 4 3 γ−1 log(2(n+k)/δ)(Appendix F.1). For fixed target error
and independent candidate channels, a two-point and Fano construction give anΩ(σ2γ−2 log(n+k))lower bound on
the leading term (Appendix F.2).
5 Experiments
The experiments ask whether behavior resolves copied descriptions, whether budgets and error rates follow the theory
under random probes, which comparison suits which noise, and how far verification reduces corrupted agent inputs.
5

ProbeIDPREPRINT
Table 1:Operating points kept apart.Decided and wrong are fractions of all checks. With the gold present, wrong
is the joint rate Theorem 2 bounds, and with the gold absent it is the acceptance of a replacement. Cached rows use
the fixed cache-order probes of the450headline cases atk=8, which meet no sampling condition, and strict choice
scores a tie as wrong. Bank rows drawmprobes at random from the agent study’s banks,1,000draws per tool, with
theory-set thresholds atδ=0.05(Appendix Q). The two unreachable tools match the gold on every bank probe but
corrupt agent calls. A check costsmin(m, B)probe calls per candidate.
evidence probes rule decided wrong
cached cases, gold present fixed,≤12strict choice 1.000 0.044
cached cases, gold present fixed,≤12per-case radius 0.153 0.000
banks, gold present, 8 reachable tools random,m=32Algorithm 1, equality 0.784 0.000
banks, gold absent, 8 reachable tools random,m=32single gate, equality 0.006 0.006
banks, gold absent, 2 unreachable tools random, anymsingle gate, either 1.000 1.000
banks, 77 golds and 67 unaffected tools random, anymsingle gate, either 1.000 0.000
5.1 Setup
We build MCP-IdentityDrift on the StableToolBench virtual API server, whose cache returns deterministic outputs
for cached arguments (Guo et al., 2024), over the ToolBench corpus (Qin et al., 2024). A recursive loader yields
3493 tools with at least four structured cached responses. A gold tool’s cached arguments form its probe set and its
cached responses the trusted referencef ref, andkschema-compatible squatters keep its description while mutating
output values or silently dropping a field, a rug pull. Identity runs use up to 12 probes and three registry seeds with
adversarial tie-breaking, so a behavioral twin counts as a miss. A gold enters only if some squatter is separable from it,
so hit@1 is conditional on that filter (Appendix T counts the excluded golds). Verification runs on CPU, and headline
comparisons report95%paired bootstrap intervals over10 4 resamples. Baselines run on the 402 tools with a real
ToolBench description, 150 gold per seed. BM25 (Qin et al., 2024), a dense retriever in the ToolRetriever style, and an
LLM reranker serving Qwen2.5-7B over tool cards (Sun et al., 2023; Shi et al., 2025) share candidates and backend,
and a random selector and an oracle give the1/(k+ 1)floor and the ceiling.
5.2 Result 1: identity under registry drift
Copied descriptions remove the identity signal available to every description router (Table J.1), and definition hash
pinning is blind to the same behavior-only change (Vercel, 2026). These controls isolate information access without
showing superiority over other behavioral methods. On a separate clean cohort the lightweight behavioral comparisons
tie (Appendix J.2), exact equality needs fewer probes on deterministic agent tools, and MMD better tolerates heavier
value noise. The informative comparisons are therefore among behavioral methods, and their order depends on the
noise regime and the budget. Appendix K.2 extends the candidate sweep.
Figure 2(a) adds the judge cohort,300gold per seed against the headline’s150. The judges’ prompts cut each serialized
response to200characters, whereas ProbeID compares complete canonicalized responses. On complete-response
prompts that fit, the 32B judge’s accuracy changes by at most0.006, but8to17%of complete prompts exceed its
32k-token context (Appendix H). Qwen2.5-7B trails at everyk, while Qwen2.5-32B is ahead of ProbeID atk∈ {2,4},
where strict tie-breaking scores ProbeID’s ties as misses, and behind atk∈ {1,8}. The 32B judge’s decision step
takes3.40seconds on a dedicated46GB GPU against3.527milliseconds for ProbeID on one CPU core. Both timings
exclude probe calls and use different hardware, so they establish neither end-to-end acceleration nor a reproducibility
advantage (Appendix H.1). Atk=8the gap over the better router is0.844, with a95%gold-clustered bootstrap interval
of[0.807,0.880]over307distinct gold tools. The4.4%strict-choice misses atk≥2are mutations that canonicalized
back to the gold on every cached probe, realized twins that strict tie-breaking scores as misses (Appendix K.3).
ProbeID stays at0.956as a squatter’s description diverges (Appendix I.1). On two real JSON serializers the small
margin constrains the budget, with no misidentification (Appendix I.4), and among near-duplicate vendor descriptions
a dense router cannot identify the recorded sibling (Appendix I.3).
5.3 Result 2: probe budget and error control
The deterministic cache does not exercise the noisy regime that16of the59census tools show (Appendix O). In a
Bernoulli mismatch channel calibrated to cached behavior, where a squatter diverges on aγfraction of probes and tool
noise sets a positive self distance and varianceσ 2, hit@1 rises withm(Figure 2(b), Appendix K.1).
6

ProbeIDPREPRINT
1 2 4 8 16 32 64
squatters k
0.0
0.2
0.4
0.6
0.8
1.0
identity hit@1
identity under rug pull
chance 1/(k+1)
best router
7B judge
32B judge
ProbeID, judge set
ProbeID
1 4 16 64 256
probe budget m
0.0
0.2
0.4
0.6
0.8
1.0
identity hit@1
budget, controlled channel
γ = 0.05
γ = 0.1
γ = 0.2
γ = 0.4
2 4 8 16
probe budget m
0.0
0.2
0.4
0.6
0.8
1.0
budget, live server
Á = 0.15
Á = 0.3
Á = 0.5
1 − (1 − Á)m
8 32 128 512
probe budget m
0.0
0.2
0.4
0.6
0.8
1.0
replacement accepted
2 unreachable tools
random bank probes, gold absent
equality
structural dY
0 .05 .1 .2
leaf jitter ρ
0.6
0.7
0.8
0.9
1.0
identity hit@1, k = 8
comparisons under noise
structural dY
set level MMD
embedding NN
exact equality
response hash
0.2 0.4 0.6 0.8 1.0
committed coverage ρ
0.0
0.2
0.4
0.6
0.8
1.0
rate
adaptive squatter
abstention
m = 2
m = 4
m = 8
m = 16
fixed probes
misidentify
(a)
(d)
(b)
(e)
(c)
(f)
Figure 2:Identity and abstention across operating regimes.(a) Strict-choice hit@1 on the headline and judge
cohorts, with routers near chance under copied descriptions. (b) Probe budget against margin. (c) Fresh live probes
against a near twin, with the sampling prediction dashed. (d) Acceptance of a rug-pull replacement, gold absent,
under random bank probes and theory-set thresholds, averaged over the eight reachable tools. No draw refuses a gold.
(e) Comparison methods under retained value noise. (f) Identification and abstention against a committed coverage
squatter.
The smallest budgetm ⋆ reaching0.99hit@1 keepsm ⋆γ2 near constant over a fourfold range ofγon a doubling grid.
The product grows from the2.6to5.8band at a gold self distance of0.18to the5.1to10.2band at0.34, the direction
theσ 2 factor predicts (Table K.1). Against a live near twin that diverges on aϕfraction of inputs, measured hit@1
tracks1−(1−ϕ) m (Figure 2(c)). Live servers with byte-identical tool cards are identified at1.00by eight probes
where a description router sits near chance (Appendix L).
The benchmark’s fixed cache-order probes do not meet the theorem’s sampling condition, so we test the bounds on the
attested banks of the agent study (Result 4), which recorded every entry, up to512probes, against the gold twice and
its rug-pull replacement once. We drawmprobes uniformly without replacement from each of the77banks,1,000
draws per tool and budget, with every threshold fixed by the theory atδ=0.05(Table 1, Figure 2(d), Appendix Q). No
observed rate violates its bound in the1,282cells where one applies, which checks threshold implementation rather
than tool behavior, since a bank mean is an exact expectation under its own sampling (Table Q.1). The informative
quantity is refusal. With the gold absent, equality accepts a replacement of the eight reachable drifted tools at a mean
rate of0.154atm=8,0.006atm=32and0fromm=64. The structural distance needs512probes, because on the
conversion and calculator tools equality’s margin is four to five times larger. Neither comparison refuses a gold or
any of the67unaffected tools, and the two tools whose drift no bank probe reaches pass at every budget, the zero-
margin case the theorem excludes. With the gold present no draw returns the squatter, which a deterministic gold
at distance zero guarantees. A prospective held-out study repeats the test on the38read-only tools of eight census
servers with seven replacement policies, from full and partial value drift to legitimate updates, and draws fresh random
banks only after fixing its rules and policies (Appendix R). At the full bank every candidate with a bank margin above
0.2is refused and no gold is, but drift on one input in twenty passes on14of22local tools, because the worst-case
radius cannot resolve so small a margin. An exact hypergeometric test for equality and a finite-population radius for
the structural distance, added once these results were known, halve the observed refusal budgets on reachable agent
replacements, from64to32probes and from512to256. At the full bank they refuse every held-out replacement
7

ProbeIDPREPRINT
whose bank distance exceeds the admission self distance, and the structural gate also refuses every answer-changing
legitimate update tested (Appendix S). A sequential structural gate (Proposition 1) refuses full value drift on local tools
after8probes on average instead of512.
5.4 Result 3: complementarity, and drift in real registries
ProbeID is a verifier, not a replacement for routing. It abstains on a constructed twin family whose members differ
only in description, where a lexical router recovers the gold (Appendix I.2). On40identity trials over20census tools
in10schema-compatible sibling groups with distinct genuine descriptions, a dense router scores1.00and ProbeID
0.90, abstaining without misidentification on one pair at distance0, so verification follows routing.
Canonicalization zeroes the gold self distance under the volatile fields it names but can hide drift confined to them
(Appendix J.1). Under residual noise,0/1equality and hash baselines degrade most and a set-level MMD performs
best under heavier value jitter (Figure 2(e)). On the agent’s deterministic tools, however, the0/1test verifies with fewer
probes (Appendices J.2 and P). Atρ=0.2andk=8, the MMD advantage is0.063, with a pointwise95%gold-clustered
interval of[0.043,0.085](Appendix J.2). No single comparison is best in every regime.
Drift in the wild.On the16census servers, eleven byte-for-byte replays of the recorded probes over eleven weeks
show7of59tools moving beyond their ownt 0 noise, setting aside three measurement artifacts. Three weather tools
reflect legitimate content updates, and an AWS documentation recommender climbs from0.10to1.00by55days
at an unchanged recorded version while two sibling tools stay at0.00. Three further tools moved after a reinstall at
unchanged versions, because their SDK declares its validation library as a range spanning two major versions and the
validation errors changed form (Figure 3(a)). Version pins therefore do not fix responses, and none of these changes
is evidence of malice (Figure 3(b), Appendix O).
5.5 Result 4: verification in an agent
We test whether verification changes the tool values an agent receives. On MCP-Bench (Wang et al., 2025a) we run
the16tasks that touch four servers for which we hold a gold and a squatter, benign or rug pulled, with and without
the gate, at one seed under greedy decoding. Gold replay, rather than benchmark scores, defines the outcome. Every
call to a server with a gold is re-issued to it with identical arguments, so a difference is a value the agent should not
have been given. Unverified, the rug pull corrupts93of1476adjudicable calls and taints15of16tasks. With the
gate drawing each tool’s whole bank of up to512probes, it corrupts20of1159adjudicable calls and taints9tasks,
with102calls refused instead (Figure 3(c)). Both benign arms have no corrupted call, and the gated benign arm
refuses none of its269verdicts. All three end-to-end runs of each arm taint equally many tasks, but corrupted-call
counts vary by trajectory (Appendix P). The surviving corruption comes from two tools whose bank probes miss the
change, a stateful tool whose probes ask about a tensor they never created and a batch tool whose schema admits seven
distinct probes. Both sit at distance0.000and pass at any budget. An exact equality gate leaves corruption only on
these two tools with far fewer probe calls (Figure 3(d)). Task success is1.000in all four arms and mean judge-rated
completion does not fall on the corrupted ones. A metric of apparent task completion therefore misses these wrong
values (Appendix P).
Adaptive adversaries and probe secrecy.Against a committed coverage squatter that returns the gold on a fraction
ρof inputs, a fixed probe set is fooled at every budget while secret subsampling from the bank detects it toward1−ρm,
so detection depends on probe secrecy rather than probe count. Over88cells and14,080trials, including white-box
squatters written by a code model told how ProbeID works, higher coverage converts identification into abstention and
no squatter is selected, as a deterministic gold at distance zero guarantees (Figure 2(f), Appendix G).
6 Limitations
Verification needs a trusted admission reference and probes that reach the difference. A compromised reference leads
ProbeID to accept compromised behavior, and drift outside the probe distribution passes unseen, which leaves9of16
gated agent tasks tainted. Side effects that never reach a response go unobserved, so behavioral identity is not endpoint
identity. The agent gate reads its whole bank at every check, so an adversary that observes the probes and adapts is not
covered. A full-bank check costs up to512probe calls and minutes on a slow remote tool, and a refused legitimate
update requires a new reference. The held-out replacements transform genuine answers and are not independent
attackers. Stateful tools fall outside the independent-probe theorem, small margins in large outputs raise the budget
(Appendix N), and production scale is untested.
8

ProbeIDPREPRINT
0 25 50 75
days since t0
0.0
0.5
1.0
distance to t0
reinstall
drift under unchanged pins
live service data (3)
changed at reinstall (3)
AWS doc recommender
10 0 10 20 30
calls, gate at m = 512
bmi_bsa_calculator
mean
round
convert_temperature
convert_force
convert_density
convert_mass
convert_speed
determinant
convert_batch
32
23
11
11
10
5
5
5
10
10
refused, 102corrupted, 20
gate outcome per tool
104 105
probe calls, rug pull arm
0
4
8
12
16
tainted tasks of 16
no gate, 15
m=32 m=128
m=512
structural dY
exact equality
m=32
cost of the comparison(b) (c) (d)
(a) drift the probes see
♂serverfilesystem server, directory_tree tool |/thumbtackversion 2026.7.4 on both days
same probe, re-issued byte for byte:excludePatterns: "*.txt"
day 0 [{"expected": "array",
"code": "invalid_type",
"path": ["excludePatterns"], ...}]
day 22 Invalid input: expected array,
received string at excludePatterns
reinstall dY =1.00
drift seen
drift the probes miss
♂serverscientific computing server, determinant tool, in the agent study
gold squatter
512 bank probes
"i667b7yny", ...
The tensor name is not found
in the store.
dY =0.000
admitted
agent’s call
"covariance_matrix"
0.000541582 ̸= 0.000536166 corrupted value used
Figure 3:Visible and missed drift.(a) A changed validation error after reinstall is visible, while bank probes miss
a tensor value changed on an agent call. (b) Per-tool distance from admission over eleven weeks. (c) Refused and
corrupted agent calls by tool. (d) Tainted tasks and probe calls under structural distance and exact equality, one run
each.
7 Conclusion
ProbeID tests whether a candidate’s canonicalized responses agree with a trusted behavioral reference and abstains
when the evidence is inconclusive. Across the reported studies its calibrated gates refuse sufficiently separated re-
placements and reduce corrupted agent inputs without changing benchmark success, within the limits of reference
integrity, probe support and response noise.
Ethics statement
ProbeID is a defensive mechanism for agent tool use. It detects when a selected tool’s probe-visible responses no
longer match its trusted reference, which mitigates rug pull and squatting attacks on open tool registries. A failure
mode is misplaced trust in the reference itself. If reference behavior was recorded from an already compromised tool,
ProbeID will accept the wrong behavior. Abstention limits silent errors but does not remove this dependency on a
clean admission step. Behavioral probing also executes tools, so probes must be confined to read-only or sandboxed
calls. The cached studies replay saved responses, the census probes only whitelisted read-only tools, and the stateful
and write studies probe reset sandboxes.
Reproducibility statement
Every reported number is traceable to a released artifact, with two exceptions stated where they arise. The original
judge runs kept no per-case records (Appendix H), and the full raw response corpus will be released upon acceptance
(Appendix T). The identity rule and the bounded behavioral distance are stated in Equation (1) and Equation (2) and
given in full, including the canonicalizer and the three response channels, in Appendix E. Theorem 1 is stated in the
body and Theorem 2 in the appendix, with proofs in Appendices B and C. The separability condition, the variance-
aware refinement and the matching lower bound are in Appendices D, F.1 and F.2. Benchmark construction, the
9

ProbeIDPREPRINT
squatter families, the probe generator and the seeds are documented in Appendix T. The code and the result files
behind every reported number will be released upon acceptance. A README names the result file and the script
behind each table and figure, and one script recomputes the main and judge tables, the noise factorial and the agent
replay counts from those files. The in-the-wild census of Appendix O pins each server to an exact version and records
every probe argument and canonicalized response, so the drift replay re-issues identical probes and is checkable against
the released per-replay summaries. The agent study of Appendix P releases every recorded tool call with its arguments
and the response the agent received, from which its ground truth is computed. It also releases the replay verdicts for
all twelve runs, three of each arm, and the gate’s own verdict logs, so the corrupted-call counts, the spread across
repeats, and the probe cost can be recomputed. The random-probe validation, the sequential gate, the held-out study,
the sharper gates and the judge information control are recomputed from the released per-entry distances, the recorded
held-out banks and the cached benchmark, each by one script. The held-out study’s replacement policies and probe
pools are released with it.
AI use statement
Generative AI tools were used to assist with writing code, with revising and polishing the writing of this paper, and
with generating the icons in Figure 1. The authors reviewed all AI-assisted work and take full responsibility for the
content of this paper.
References
Baichao An, Pei Chen, Geng Hong, Yueyue Chen, and Mengying Wu. FlowGuard: From signals to evidence for MCP
security detection.arXiv preprint arXiv:2607.14754, 2026.
Dana Angluin. Learning regular sets from queries and counterexamples.Information and Computation, 75(2):87–106,
1987. doi: 10.1016/0890-5401(87)90052-6.
Vaggelis Atlidakis, Patrice Godefroid, and Marina Polishchuk. RESTler: Stateful REST API fuzzing. In2019
IEEE/ACM 41st International Conference on Software Engineering (ICSE), pp. 748–758, 2019. doi: 10.1109/
ICSE.2019.00083.
Rémi Bardenet and Odalric-Ambrym Maillard. Concentration inequalities for sampling without replacement.
Bernoulli, 21(3):1361–1385, 2015.
Robert E. Bechhofer. A single-sample multiple decision procedure for ranking means of normal populations with
known variances.Annals of Mathematical Statistics, 25(1):16–39, 1954.
Antonia Bertolino and Andrea Polini. The audition framework for testing web services interoperability. InEUROMI-
CRO Conference on Software Engineering and Advanced Applications (EUROMICRO-SEAA), pp. 134–142. IEEE
Computer Society, 2005.
Luca Beurer-Kellner and Marc Fischer. MCP Security Notification: Tool Poisoning Attacks. https://invariantlabs.ai/
blog/mcp-security-notification-tool-poisoning-attacks, 2025a. Blog post, Invariant Labs.
Luca Beurer-Kellner and Marc Fischer. WhatsApp MCP Exploited: Exfiltrating your message history via MCP.
https://invariantlabs.ai/blog/whatsapp-mcp-exploited, 2025b. Blog post, Invariant Labs.
Varun Pratap Bhardwaj. AgentAssay: Token-efficient regression testing for non-deterministic AI agent workflows.
arXiv preprint arXiv:2603.02601, 2026. doi: 10.48550/arXiv.2603.02601. URL https://arxiv.org/abs/2603.02601.
Gautam Bharti. Registry descriptions go stale unevenly: An 89-day measurement of Model Context Protocol drift,
and why drift-ranked re-auditing under-covers it.arXiv preprint arXiv:2608.00997, 2026.
Manish Bhatt, Vineeth Sai Narajala, and Idan Habler. ETDI: Mitigating tool squatting and rug pull attacks in Model
Context Protocol (MCP) by using OAuth-enhanced tool definitions and policy-based access control. In2025 Cyber
Awareness and Research Symposium (CARS), pp. 1–6. IEEE, 2025. doi: 10.1109/CARS67163.2025.11337310.
Kunfeng Chen, Luyao Zhuang, Fei Liao, Juhua Liu, Jian Wang, and Bo Du. Tool retrieval bridge: Aligning vague
instructions with retriever preferences via bridge model.Neural Networks, 202:109037, 2026. doi: 10.1016/j.
neunet.2026.109037.
C. K. Chow. On optimum recognition error and reject tradeoff.IEEE Transactions on Information Theory, 16(1):
41–46, 1970.
Tsun S. Chow. Testing software design modeled by finite-state machines.IEEE Transactions on Software Engineering,
SE-4(3):178–187, May 1978. doi: 10.1109/TSE.1978.231496.
10

ProbeIDPREPRINT
Ran El-Yaniv and Yair Wiener. On the foundations of noise-free selective classification.Journal of Machine Learning
Research, 11:1605–1641, 2010.
Eyal Even-Dar, Shie Mannor, and Yishay Mansour. PAC bounds for multi-armed bandit and Markov decision pro-
cesses. InComputational Learning Theory (COLT 2002), volume 2375 ofLecture Notes in Computer Science, pp.
255–270. Springer, 2002.
Eyal Even-Dar, Shie Mannor, and Yishay Mansour. Action elimination and stopping conditions for the multi-armed
bandit and reinforcement learning problems.Journal of Machine Learning Research, 7:1079–1105, 2006.
Wei Fang, Yang Zhang, Kaizhi Qian, James R. Glass, and Yada Zhu. PLAY2PROMPT: Zero-shot tool instruction
optimization for LLM agents via tool play. InFindings of the Association for Computational Linguistics: ACL
2025, pp. 26274–26290, 2025.
Xiang Fei, Xiawu Zheng, and Hao Feng. MCP-Zero: Active tool discovery for autonomous LLM agents.arXiv
preprint arXiv:2506.01056, 2025.
Irena Gao, Percy Liang, and Carlos Guestrin. Model equality testing: Which model is this API serving? InInterna-
tional Conference on Learning Representations, 2025. URL https://arxiv.org/abs/2410.20247.
Yonatan Geifman and Ran El-Yaniv. Selective classification for deep neural networks. InAdvances in Neural Infor-
mation Processing Systems 30, pp. 4878–4887, 2017.
Zhicheng Guo, Sijie Cheng, Hao Wang, Shihao Liang, Yujia Qin, Peng Li, Zhiyuan Liu, Maosong Sun, and Yang Liu.
StableToolBench: Towards stable large-scale benchmarking on tool learning of large language models. InFindings
of the Association for Computational Linguistics: ACL 2024, pp. 11143–11156, 2024.
Mohammed Mehedi Hasan, Hao Li, Gopi Krishnan Rajbahadur, Bram Adams, and Ahmed E. Hassan. Model Context
Protocol (MCP) tool descriptions are smelly! Towards improving AI agent efficiency with augmented MCP tool
descriptions.arXiv preprint arXiv:2602.14878, 2026.
Wassily Hoeffding. Probability inequalities for sums of bounded random variables.Journal of the American Statistical
Association, 58(301):13–30, 1963. doi: 10.1080/01621459.1963.10500830.
Steven R. Howard, Aaditya Ramdas, Jon McAuliffe, and Jasjeet Sekhon. Time-uniform, nonparametric, nonasymp-
totic confidence sequences.Annals of Statistics, 49(2):1055–1080, 2021.
Yiheng Huang, Zhijia Zhao, Bihuan Chen, Susheng Wu, Zhuotong Zhou, Yiheng Cao, Xin Hu, and Xin Peng. From
component manipulation to system compromise: Understanding and detecting malicious MCP servers.arXiv
preprint arXiv:2604.01905, 2026. doi: 10.48550/arXiv.2604.01905. URL https://arxiv.org/abs/2604.01905.
Shivaram Kalyanakrishnan, Ambuj Tewari, Peter Auer, and Peter Stone. PAC subset selection in stochastic multi-
armed bandits. InProceedings of the 29th International Conference on Machine Learning (ICML), pp. 655–662,
2012.
Adam Karvonen, Daniel Reuter, Roy Rinberg, Luke Marks, Adrià Garriga-Alonso, and Keri Warr. DiFR: Infer-
ence verification despite nondeterminism.arXiv preprint arXiv:2511.20621, 2025. URL https://arxiv.org/abs/2511.
20621.
Emilie Kaufmann, Olivier Cappé, and Aurélien Garivier. On the complexity of best-arm identification in multi-armed
bandit models.Journal of Machine Learning Research, 17(1):1–42, 2016.
Simcha Kosman. Poison everywhere: No output from your MCP server is safe. https://web.archive.org/web/
20250711001450/https://www.cyberark.com/resources/threat-research-blog/poison-everywhere-no-output-from-
your-mcp-server-is-safe, 2025. Threat Research Blog, CyberArk, 30 May 2025. Archived copy.
Jonah Leshin, Manish Shah, Ian Timmis, and Daniel Kang. Behavioral fingerprints for LLM endpoint stability and
identity. InProceedings of the ACM Conference on AI and Agentic Systems, pp. 1327–1331, 2026. doi: 10.1145/
3786335.3813194.
Zhihao Li, Boyang Ma, Xuelong Dai, Minghui Xu, Yue Zhang, Biwei Yan, and Kun Li. Don’t believe every-
thing you read: Understanding and measuring MCP behavior under misleading tool descriptions.arXiv preprint
arXiv:2602.03580, 2026. doi: 10.48550/arXiv.2602.03580.
Gordon Fyodor Lyon. Nmap Network Scanning, chapter 7: Service and application version detection. Online book
chapter, 2009. URL https://nmap.org/book/vscan.html. Accessed 2026-07-08.
Narek Maloyan and Dmitry Namiot. Breaking the protocol: Security analysis of the Model Context Protocol specifi-
cation and prompt injection vulnerabilities in tool-integrated LLM agents.Modern Information Technologies and
IT-Education, 21(3):420–428, 2025. doi: 10.25559/SITITO.021.202503.420-428.
11

ProbeIDPREPRINT
Lluis Mas, Jordi Vilaplana, Josep Rius, Radu Spaimoc, and Jordi Mateo. The trustworthy Model Context Protocol
(MCP) registry: An architectural blueprint for cryptographic provenance and runtime integrity.Future Internet, 18
(5):243, 2026. doi: 10.3390/fi18050243. URL https://doi.org/10.3390/fi18050243.
William M. McKeeman. Differential testing for software.Digital Technical Journal, 10(1):100–107, 1998.
Alfredo Metere. Attested tool-server admission: A security extension to the Model Context Protocol.arXiv preprint
arXiv:2605.24248, 2026. doi: 10.48550/arXiv.2605.24248. URL https://arxiv.org/abs/2605.24248.
Model Context Protocol. Specification 2025-11-25: Tools. https://modelcontextprotocol.io/specification/2025-11-
25/server/tools, 2025.
Model Context Protocol. Security charter. MCP Security Interest Group charter, 2026. URL https://
modelcontextprotocol.io/community/interest-groups/security. Initial charter dated 2026-06-13.
Ginger Myles and Christian Collberg. K-gram based software birthmarks. InProceedings of the 2005 ACM Symposium
on Applied Computing (SAC), pp. 314–318, 2005. doi: 10.1145/1066677.1066753.
Vineeth Sai Narajala, Ken Huang, and Idan Habler. Securing GenAI multi-agent systems against tool squatting: A
zero trust registry-based approach. In2026 International Conference on AI x Data and Knowledge Engineering
(AIxDKE), pp. 91–93. IEEE, 2026. doi: 10.1109/AIxDKE67294.2026.00022.
Dario Pasquini, Evgenios M. Kornaropoulos, and Giuseppe Ateniese. LLMmap: Fingerprinting for large language
models. In34th USENIX Security Symposium, pp. 299–318. USENIX Association, 2025.
Andy Podgurski and Lynn Pierce. Retrieving reusable software by sampling behavior.ACM Transactions on Software
Engineering and Methodology, 2(3):286–303, 1993. doi: 10.1145/152388.152392.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru Tang, Bill
Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein, Dahai Li, Zhiyuan Liu, and
Maosong Sun. ToolLLM: Facilitating large language models to master 16000+ real-world APIs. InInternational
Conference on Learning Representations, 2024.
Mehrdad Rostamzadeh, Sidhant Narula, Mohammad Ghasemigol, and Daniel Takabi. TrustShiftProbe: Characteriz-
ing, benchmarking, and defending staged trust attacks on MCP servers.arXiv preprint arXiv:2608.23763, 2026.
R. J. Serfling. Probability inequalities for the sum in sampling without replacement.The Annals of Statistics, 2(1):
39–48, 1974.
Shai Shalev-Shwartz and Shai Ben-David.Understanding Machine Learning: From Theory to Algorithms. Cambridge
University Press, 2014.
Shuo Shao, Yiming Li, Hongwei Yao, Yifei Chen, Yuchen Yang, and Zhan Qin. Reading between the lines: To-
wards reliable black-box LLM fingerprinting via zeroth-order gradient estimation. InProceedings of the ACM Web
Conference 2026, 2026. doi: 10.1145/3774904.3792196. URL https://arxiv.org/abs/2510.06605.
Zhengliang Shi, Yuhan Wang, Lingyong Yan, Pengjie Ren, Shuaiqiang Wang, Dawei Yin, and Zhaochun Ren. Re-
trieval models aren’t tool-savvy: Benchmarking tool retrieval for large language models. InFindings of the Associ-
ation for Computational Linguistics: ACL 2025, pp. 24497–24524, 2025.
Jonathan Sneh, Ruomei Yan, Jialin Yu, Philip Torr, Yarin Gal, Sunando Sengupta, Eric Sommerlade, Alasdair Paren,
and Adel Bibi. ToolTweak: An attack on tool selection in LLM-based agents.arXiv preprint arXiv:2510.02554,
2025.
Hao Song, Yiming Shen, Wenxuan Luo, Leixin Guo, Ting Chen, Jiashui Wang, Beibei Li, Xiaosong Zhang, and Jiachi
Chen. Beyond the protocol: Unveiling attack vectors in the Model Context Protocol (MCP) ecosystem.IEEE
Transactions on Software Engineering, 52(8):2410–2426, 2026. doi: 10.1109/TSE.2026.3694876.
Weiwei Sun, Lingyong Yan, Xinyu Ma, Shuaiqiang Wang, Pengjie Ren, Zhumin Chen, Dawei Yin, and Zhaochun
Ren. Is ChatGPT good at search? Investigating large language models as re-ranking agents. InProceedings
of the 2023 Conference on Empirical Methods in Natural Language Processing, pp. 14918–14937, 2023. doi:
10.18653/v1/2023.emnlp-main.923.
Haruaki Tamada, Masahide Nakamura, Akito Monden, and Ken-ichi Matsumoto. Design and evaluation of birth-
marks for detecting theft of Java programs. InProceedings of the IASTED International Conference on Software
Engineering, pp. 569–574, 2004.
W. T. Tsai, R. Paul, Z. Cao, L. Yu, A. Saimi, and B. Xiao. Verification of web services using an enhanced UDDI server.
InIEEE International Workshop on Object-Oriented Real-Time Dependable Systems (WORDS), pp. 131–138, 2003.
Alexandre B. Tsybakov.Introduction to Nonparametric Estimation. Springer Series in Statistics. Springer, New York,
2009. ISBN 978-0-387-79052-7. doi: 10.1007/b13794.
12

ProbeIDPREPRINT
Twitter. Diffy: Testing services without writing tests. Twitter Engineering Blog and https://github.com/twitter-archive/
diffy, 2015.
Vercel. AI SDK core: Model Context Protocol (MCP) tools. https://ai-sdk.dev/docs/ai-sdk-core/mcp-tools, 2026.
DocumentsfingerprintToolsanddetectToolDrift, accessed 2026-08-06.
Zhenting Wang, Qi Chang, Hemani Patel, Shashank Biju, Cheng-En Wu, Quan Liu, Aolin Ding, Alireza Rezazadeh,
Ankit Shah, Yujia Bao, and Eugene Siow. MCP-Bench: Benchmarking tool-using LLM agents with complex real-
world tasks via MCP servers.arXiv preprint arXiv:2508.20453, 2025a. URL https://arxiv.org/abs/2508.20453.
Zhiqiang Wang, Yichao Gao, Yanting Wang, Suyuan Liu, Haifeng Sun, Haoran Cheng, Guanquan Shi, Haohua Du,
and Xiangyang Li. MCPTox: A benchmark for tool poisoning attack on real-world MCP servers.arXiv preprint
arXiv:2508.14925, 2025b.
Mengying Wu, Pei Chen, Geng Hong, Baichao An, Jinsong Chen, Binwang Wan, Xudong Pan, Jiarun Dai, and Min
Yang. MCPZoo: A large-scale dataset of runnable Model Context Protocol servers for AI agent.arXiv preprint
arXiv:2512.15144, 2025. doi: 10.48550/arXiv.2512.15144. URL https://arxiv.org/abs/2512.15144.
Yuhao Wu, Tung-Ling Li, and Hongliang Liu. Behavioral integrity verification for AI agent skills.arXiv preprint
arXiv:2605.11770, 2026.
Wenpeng Xing, Zhonghao Qi, Yupeng Qin, Yilin Li, Caini Chang, Jiahui Yu, Changting Lin, Zhenzhen Xie, and Meng
Han. MCP-Guard: A multi-stage defense-in-depth framework for securing Model Context Protocol in agentic AI.
InFindings of the Association for Computational Linguistics: ACL 2026, pp. 4877–4889, 2026. doi: 10.18653/v1/
2026.findings-acl.240.
Jehyeok Yeon, Isha Chaudhary, and Gagandeep Singh. Quantitative certification of agentic tool selection.arXiv
preprint arXiv:2510.03992, 2026. Version 2, May 2026. Version 1 (October 2025) was titled Quantifying Distribu-
tional Robustness of Agentic Tool-Selection.
Jiahao Zhang, Xiuyu Li, and Suhang Wang. Your “Pro” LLM subscription may actually be “Free”: Expos-
ing fingerprint spoofing risks in LLM inference services.arXiv preprint arXiv:2606.16100, 2026. URL https:
//arxiv.org/abs/2606.16100.
Zhenhong Zhou, Yuanhe Zhang, Hongwei Cai, Moayad Aloqaily, Ouns Bouachir, Linsey Pang, Prakhar Mehrotra,
Kun Wang, and Qingsong Wen. MCPShield: A security cognition layer for adaptive trust calibration in Model
Context Protocol agents.arXiv preprint arXiv:2602.14281, 2026.
Xiaoyuan Zhu, Yaowen Ye, Tianyi Qiu, Hanlin Zhu, Sijun Tan, Ajraf Mannan, Jonathan Michala, Raluca Ada Popa,
and Willie Neiswanger. Auditing black-box LLM APIs with a rank-based uniformity test. InInternational Confer-
ence on Learning Representations, 2026. URL https://openreview.net/forum?id=PSIe9mmF7a.
13

ProbeIDPREPRINT
Appendix
Appendix A extends the related work, and Appendices B to F prove the results of Section 4 and define the distance.
Appendices G and H support the adversary and judge comparisons of Results 1 and 2, and Appendices I to K the
routing, noise and budget studies of Results 1 to 3. Appendices L to N report the live, stateful and large-output studies,
Appendices O to Q the census, the agent study and the random-probe validation, Appendix R the prospective held-
out study and Appendix S the exact and finite-population gates. Appendix T gives implementation and reproduction
details.
Contents
A Behavioral identity in prior work
B Proof of Theorem 1
C The abstaining algorithm
D Sources of the behavioral margin
E The behavioral distanced Y
F Variance-aware budget and a matching lower bound
G Adaptive and independently authored squatters
H A behavioral LLM-judge baseline
I Description routing and natural cases
J Canonicalization and simple behavioral baselines
K Further results on the cached benchmark
L Live MCP servers
M Stateful, side-effecting and authenticated tools
N Behavioral distance under large outputs
O An in-the-wild census of real MCP servers
P The agent study and residual failures
Q Random probes from the attested banks
R A prospective held-out study
S Exact and finite-population gates
T Implementation and reproducibility
A Behavioral identity in prior work
Judging an artifact by what it does or contains, rather than by its declared metadata, is a recurring idea. Conformance
testing (Chow, 1978), query learning (Angluin, 1987), stateful API fuzzing (Atlidakis et al., 2019), and network
service scanning (Lyon, 2009) all examine implementations through probe responses. Software birthmarks identify
programs by intrinsic characteristics they cannot easily fake (Tamada et al., 2004; Myles & Collberg, 2005), input-
output examples retrieve reusable code by sampling behavior (Podgurski & Pierce, 1993), and language models are
fingerprinted from their responses (Pasquini et al., 2025; Shao et al., 2026). Closest in spirit, Model Equality Testing
uses a two-sample test over sampled outputs to ask whether a black-box API still serves a trusted reference model
(Gao et al., 2025). Related audits detect silent endpoint substitution (Zhu et al., 2026) or verify which computation
produced an output under nondeterminism (Karvonen et al., 2025), and spoofing attacks show that passively collected
fingerprints can be gamed (Zhang et al., 2026). Some methods already combine selection with rejection. LLMmap’s
closed-set variant attributes a queried endpoint among many known model templates, and its open-set variant thresh-
olds relative distances. In this line of work, an adversary, if present, attacks the verifier. Fingerprint spoofing adapts a
model until an auditor mistakes it for another (Zhang et al., 2026), and no guarantee is attached to a decision among
candidates authored to be mistaken for a trusted one. ProbeID’s setting iskcandidates that are schema compatible and
description identical by construction, under an explicit drift model, with a margin condition, a probe-budget bound
with a matching lower bound on its leading term, and an abstention rule for behaviorally ambiguous tools. It thus
differs from model version attribution (Pasquini et al., 2025) and program theft detection (Tamada et al., 2004) in the
adversarial construction of the candidate set and the joint error bound on the decision, not in the act of selecting.
The verification mechanism itself follows established software testing practice. Differential testing runs independent
implementations on the same inputs and flags disagreements (McKeeman, 1998), and Diffy compares a candidate
service with two trusted instances, using their disagreement to cancel noise much as ProbeID’s self distance does
(Twitter, 2015). Registry-side testing of web services at registration and at discovery, with test scripts attached to the
registered service, anticipates the admission reference and the use-time check (Tsai et al., 2003; Bertolino & Polini,
2005). ProbeID adds a calibrated decision and abstention rule to this practice and studies it against description-copying
squatters on MCP registries.
Three concurrent defenses for MCP servers observe behavior at run time. MCPShield generates invocations from
a tool’s metadata and checks the observed behavior against that declaration, including drift over time (Zhou et al.,
2026). TrustShiftProbe audits a single server’s responses against a baseline learned while it was trusted, without
an oracle (Rostamzadeh et al., 2026). FlowGuard sends schema-valid probes to gather evidence of vulnerabilities,
14

ProbeIDPREPRINT
and stops when a round adds no actionable signal (An et al., 2026). Each compares a tool with its own declaration
or history, which for TrustShiftProbe is a baseline recorded while the tool was trusted. None probes description-
identical candidates on shared inputs, compares their responses with a recorded trusted reference, or bounds the error
of selecting among them. The approaches are complementary, since a tool can match its own history and still differ
from the reference that was admitted.
B Proof of Theorem 1
Fix the trusted referencef ref and a candidatet. The empirical distance b∆m(ft, fref ) = 1 m Pm i=1 Zi averagesmterms Zi =d Y (c(ft(xi)), c(fref (xi)))∈[0,1]that are independent across the i.i.d. probesx i ∼D, with mean∆(f t, fref ).
By Hoeffding’s inequality, for anyϵ >0,
Pr

| b∆m(ft, fref )−∆(f t, fref )| ≥ϵ  ≤2 exp(−2mϵ 2).
The deployed protocol draws itsmprobes as a secret subsample without replacement from an attested bank of sizeB
rather than i.i.d. fromD. Hoeffding’s inequality also holds for sampling without replacement from a finite population
(Hoeffding, 1963), and Serfling (1974) sharpens it by the finite-population correction1−(m−1)/B. For the bank,
the statement holds withDread as the uniform distribution over theBrecorded probes and the margin measured
on those probes. A margin on a population distribution transfers to the bank only if the bank was itself drawn i.i.d.
from it, at the cost of a second Hoeffding radius overB. The guarantee still does not cover the choice of probe
distribution. A deterministic enumeration concentrates its support on a predictable set, which the method section
excludes and Appendix G.1 quantifies through the coverageρ. Apply a union bound over the at mostn+kcandidates
and set the total failure probability toδ, so2(n+k) exp(−2mϵ 2)≤δ, givingϵ= p log(2(n+k)/δ)/(2m). On the
complementary event, which holds with probability at least1−δ, every empirical distance is withinϵof its expectation.
Under the margin condition the gold has expected distanceµ t⋆ and every wrong candidate has expected distance at
leastµ t⋆ +γ. Ifϵ < γ/2, then the gold empirical distance is below the midpointµt⋆ +γ/2and every wrong empirical
distance is above it, so the gold is strictly nearest and Equation (2) returns a behaviorally correct tool. The condition
ϵ < γ/2is equivalent tom > 2 γ2 log 2(n+k) δ , which proves the claim. The dependence onn+kis logarithmic, sok
squatters enter the budget only through this factor.■
The argument is the finite-class uniform convergence bound of agnostic PAC learning (Shalev-Shwartz & Ben-David,
2014, Corollary 4.6) applied to then+kcandidates, and up to constants it is the budget of uniform-sampling PAC
best-arm identification (Even-Dar et al., 2002). The marginγplays the role of an indifference zone (Bechhofer, 1954).
We claim no new concentration result, only its application to behavioral verification.
C The abstaining algorithm
Theorem 1 certifies the forced nearest-fingerprint choice. We certify the deployed abstaining rule, Algorithm 1, and
relateγ min to the same confidence radius.
Theorem 2(Calibrated abstention).Assume the setting of Theorem 1 with marginγ, the gold present, and at least
two candidates. Writeϵ=
p
log(2(n+k)/δ)/(2m)and run Algorithm 1 withγ min = 2ϵandτ hi ≥µ t⋆ +ϵ.
With probability at least1−δ, the algorithm(i)does not return a behaviorally wrong candidate and(ii)returns a
behaviorally correct tool wheneverγ≥4ϵand no behavioral twin of the gold is among the candidates. Otherwise,
it returns a correct candidate orABSTAINon the same event. This bounds the joint event of a wrong decision and a
decision. It does not bound the error rate conditional on deciding byδ.
In terms of probabilities,Pr(wrong and decide)≤δunder the stated assumptions, and whenPr(decide)>0the
conditional error satisfies onlyPr(wrong|decide)≤δ/Pr(decide). An observed error rate among decisions is not a
δ-level certificate, and a rule that rarely decides can have a conditional error well aboveδ.
LetEbe the event that|d t −µ t| ≤ϵfor every candidatet, whered t = b∆m(ft, fref )andµ t = ∆(f t, fref ). The
Hoeffding union bound in the proof above givesPr[E]≥1−δfor thisϵ. Argue onE.
(i)Suppose Algorithm 1 returns a candidate, so the nearest passes both gates,d (1) ≤τ hi andd (2) −d (1) ≥γ min = 2ϵ.
If the returned candidate were a behaviorally wrongw, thend (1) =d w, while the gold hasd t⋆ ≥d (2) since the
gold distance is at least the second smallest oncewis smallest. OnE,µ w ≤d (1) +ϵandµ t⋆ ≥d (2) −ϵ, so
µw −µ t⋆ ≤(d (1) −d (2)) + 2ϵ≤2ϵ−γ min = 0, contradictingµ w −µ t⋆ ≥γ >0. Hence the returned candidate is
behaviorally correct, either the gold or a behavioral twin of it.
15

ProbeIDPREPRINT
(ii)Ifγ≥4ϵ, then onEthe gold satisfiesd t⋆ ≤µ t⋆ +ϵ≤τ hi, and every wrongwsatisfiesd w ≥µ t⋆ +γ−ϵ. With
no behavioral twin present the next nearest candidate is wrong, so the gold is strictly nearest and the gap is at least
(µt⋆ +γ−ϵ)−(µ t⋆ +ϵ) =γ−2ϵ≥2ϵ=γ min. Both gates pass, so ProbeID returns the gold.
(iii)In the remaining regime the gap gate may pass, returning a behaviorally correct tool by(i), or fail and return
ABSTAIN. In neither case is a wrong candidate returned.■
The gap gate is the stopping condition of action elimination and of LUCB-style best-arm algorithms (Even-Dar et al.,
2006; Kalyanakrishnan et al., 2012), and abstention is Chow’s reject option (Chow, 1970). Selective classification
calibrates the conditional risk itself (El-Yaniv & Wiener, 2010; Geifman & El-Yaniv, 2017), whereas Theorem 2
bounds it only by the coverage-dependentδ/Pr(decide)above.
The trichotomy needs the gold among the candidates and the stated sampling, margin and threshold conditions. On
its probability1−δevent a returned candidate is correct, the gold is returned once its margin exceeds4ϵwith no
behavioral twin present, and below that margin the rule returns a correct candidate or abstains. The stateful study
is empirical evidence outside the independent-probe theorem. Sinceϵshrinks as1/ √m, a larger budget lowers the
margin sufficient for acceptance at the same error bound.
A single registered candidate.A deployed gate often sees one server under a trusted name, and that server may
be a squatter that replaced the gold, as in the agent study of Appendix P. With one candidate there is no second
distance, and Algorithm 1 reduces to its absolute gate, accepting whend (1) ≤τ hi. On the eventEfor that one
candidate, withτ hi =µ t⋆ +ϵ, the gold is accepted, and a candidatewis refused wheneverµ w −µ t⋆ >2ϵ, since then
dw ≥µ w −ϵ > τhi. Below that margin the bound gives no protection. A squatter within2ϵof the reference may be
accepted, and one at distance zero onDalways is. The agent gate draws each tool’s whole bank, at most512probes,
and setsτ hi to the tool’s self distance plusϵ=
p
log(2/δ)/(2m)atδ=0.05. The threshold is0.060for a full bank at
zero self distance and0.51for a tool whose schema admits only seven distinct probes. The two tools that survive the
gate sit at distance0.000and are accepted, as this bound allows (Appendix P).
A sequential gate.A fixed budget spends the whole bank on every check, even when a few probes already settle
it. The sequential gate instead reads nested prefixes of one secret random permutation of the bank at checkpoints
m1 <· · ·< mJ and splits the error budget evenly,δ j =δ/Jandϵ j =
p
log(2/δj)/(2mj). Withd (j) the mean
distance over the firstm j probes, it refuses at the first checkpoint whered (j) > s+ϵ j, accepts at the first where
d(j) +ϵ j ≤s+γ res, and reports the check as inconclusive if the last checkpoint does neither. The resolutionγ res is
an indifference zone chosen by the deployer.
Proposition 1(Sequential gate).Letµbe a candidate’s expected distance on the bank distribution andsthe admission
self distance. With probability at least1−δ, the sequential gate does not refuse the candidate whenµ≤sand does
not accept it whenµ > s+γ res. On every draw it decides no later than the first checkpoint with2ϵ j ≤γ res, if one
exists.
LetEbe the event that|d (j) −µ| ≤ϵ j at every checkpoint. Each prefix is a uniform sample without replacement
from the bank, so Hoeffding’s inequality bounds each failure byδ j, and a union bound over theJcheckpoints gives
Pr[E]≥1−δ. OnE, ifµ≤sthend (j) ≤s+ϵ j at every checkpoint and the gate never refuses, and ifµ > s+γres
thend (j) +ϵ j ≥µ > s+γ res and it never accepts. At a checkpoint with2ϵ j ≤γ res, a gate that does not refuse has
d(j) ≤s+ϵ j, henced (j) +ϵ j ≤s+γ res, and it accepts.■
A candidate withs < µ≤s+γ res may be accepted, so the resolution plays the role that2ϵplays at a fixed
budget, now fixed in advance rather than set by the budget. The same splitting makes Algorithm 1 sequential. With
ϵj =
p
log(4/δj)/(2mj)for two candidates and a decision at the first checkpoint whose two gates pass, part(i)of
Theorem 2 holds at every checkpoint on the same kind of event, so the joint probability of a wrong decision stays
at mostδ. The even split is the simplest valid choice. Time-uniform confidence sequences (Howard et al., 2021)
and concentration bounds for sampling without replacement (Bardenet & Maillard, 2015) give tighter radii, the latter
shrinking to zero asmapproaches the bank size. On the agent banks with checkpoints8,16, . . . ,512andδ=0.05, the
sequential equality gate refuses every reachable replacement after12.5probes on average, where the fixed gate needs
64to stop accepting them, and atγ res=0.2accepts76of the77golds within128probes. It refuses none of the golds
and leaves convert_batch, whose bank holds seven probes, inconclusive. No observed rate breaks the proposition’s
bounds on these banks or in the held-out study of Appendix R.
16

ProbeIDPREPRINT
D Sources of the behavioral margin
Theorem 1 takes the marginγas given. The margin depends on the probe distribution and on each candidate’s
responses. This section gives conditions for a positive margin and a way to measure it for tested candidates.
For a deterministic gold whose canonical response matches the reference forD-almost every probe,µ t⋆ = 0. Fix a
wrong candidatewand define∆ w ={x:d Y (c(fw(x)), c(fref (x)))>0}with massp w = Pr x∼D[x∈∆ w]. The
distance is zero on∆ c w and positive on∆ w. Henceµ w = R ∆w dY dD≤p w, andµ w >0if and only ifp w >0. This distance-based definition matters because distinct canonical values can have zero implemented distance.
Proposition 2(Separability).With a deterministic pointwise faithful gold and a finite candidate pool,γ= min w µw >
0if and only if every squatter has positive distance from the reference on a set of positive probe mass,minw pw >0. A
candidate withp w = 0is indistinguishable underd Y andD. When the gold is also present, the margin gate abstains
on their tied observations.
The characterization is qualitative by necessity. If the canonical responses reachable onDtake finitely many structural
distance values, for instance bounded-size outputs, or a scalar or binary channel where the smallest positive distance is
dmin = 1, the bound sharpens to the quantitativeµ w ≥d min pw withd min the smallest positive valued Y attains. On
variable-size outputs no uniformd min exists, and the margin can be small even at large divergence mass. Appendix N
measures this dilution on a live server. A format-faithful squatter that perturbsfofNresponse fields leaves a per-
probe marginγ=f /(12N), so no schema-level constant boundsγaway from zero, and in that regime the abstention
rule, not the identity rule, carries the guarantee.
Three consequences follow. First, probe design controls the margin. Boundary and enumeration values seek differ-
ences, but schema validity does not ensure positiveD-mass on every∆ w. The agent study exhibits missing state
prerequisites and a nested schema whose probes miss the altered behavior (Appendix P). Second, if a squatter has
zero distance on a fractionρ= Pr D[x∈∆ c w]of inputs, thenp w = 1−ρ. The margin is at leastd min(1−ρ)when
a positive minimum distance exists. Third, zero margin means that at least one candidate is indistinguishable under
this distance and probe distribution. It does not imply identical behavior outside the probe support or in fields the
comparison ignores.
E The behavioral distanced Y
The canonicalizercdrops, at any depth and regardless of case, twelve volatile keys,timestamp,request_id,
requestid,id,trace_id,traceid,cursor,created_at,updated_at,nonce,etaganddate. It sorts the
remaining keys, rounds floats to six decimals, keeps lists in order and booleans as they are, and applies no whitespace
or Unicode normalization. A response delivered as JSON text is parsed first. Every response carries a status, set to
success when the server reports none, and a state delta, empty when none is observed. On canonicalized values the
distance reduces to a recursive structural distanceδ∈[0,1]. For two scalarsδ(a, b) =⊮[a̸=b], an integer and a float
of equal value count as equal, and a type mismatch givesδ= 1. For maps over the key unionK= keys(a)∪keys(b),
δ(a, b) = 1 |K| X κ∈K δ(aκ, bκ)κ∈a∩b, 1otherwise,
and for lists withL= max(|a|,|b|),δ(a, b) = 1 L P i<L δ(ai, bi)where a missing index is charged1. By convention
δ(a, b) = 0whenK=∅(two empty maps) orL= 0(two empty lists), so an empty container matches itself at
distance0andδis total on canonicalized values. A canonicalized response carries three observable channels (output,
status and state delta), combined by a probabilistic union so that any channel difference registers,
dY (a, b) = 1−
Y
c∈ {out,stat,∆}

1−δ(a c, bc)

.
Eachd Y ∈[0,1]is symmetric and is0for identical responses, and the empirical behavioral distance is the probe mean
b∆m(f, g) = 1 m Pm i=1 dY (c(f(x i)), c(g(xi))), so the[0,1]range assumed by Theorem 1 holds. The probabilistic union keeps a genuine output difference from being diluted when status and state delta are constant, the common case
for read-style tools. Without a canonicalizer, a simpler0/1equality or hash comparison of these responses collapses
under volatile fields while the boundedd Y remains effective (Appendix J.2).
17

ProbeIDPREPRINT
F Variance-aware budget and a matching lower bound
F.1 Variance-aware budget
Theorem 1 bounds the worst case overd Y ∈[0,1], which is loose when the per-probe termsZ i =
dY (c(ft(xi)), c(fref (xi)))have small variance. Suppose every candidate, including a noisy gold with meanµ t⋆, has
per-probe varianceVar(Z i)≤σ 2. By Bernstein’s inequality,Pr[| b∆m −∆| ≥ϵ]≤2 exp  − mϵ2 2σ2+2ϵ/3  . Repeating
the union bound overn+kcandidates and the midpoint margin stepϵ < γ/2gives the budget
m > 8σ2
γ2 log 2(n+k) δ + 4 3γ log 2(n+k) δ ,
whose leading term isO(σ 2γ−2 log((n+k)/δ))and recovers the noiseless rate asσ→0up to the additive1/γ
term. The variance admits a plug-in estimate from the probe sample,ˆσ 2 = 1 m Pm i=1(Zi − ¯Z) 2, which gives a run- time diagnostic, and a high-confidence certificate would add the standard empirical Bernstein variance term. Result 2
sweepsσthrough the controlled channel and reportsm ⋆γ2 growing withσ 2 as this predicts.
F.2 A lower bound matching the leading term
Theorem 1 and Appendix F.1 give an upper bound of orderσ 2/γ2 on the probe budget. Over independent candidate
channels this rate is minimax optimal. No identity rule separates a gold tool from a squatter at marginγwith fewer
than orderσ 2/γ2 probes, so the leading term of the budget cannot be reduced beyond constants. The construction
below makes the candidate channels independent, the regime in which the lower bound is tight. Correlated drift across
squatters falls outside this independent construction, so the minimax floor does not formally cover it. Result 3 observes
live that such correlation only makes the gold easier to single out, but that is an empirical observation and does not
follow from the lower bound.
Fix a single candidate (k=1) and reduce identity to a two-point test. Each probexi ∼Dyields the mismatch indicator
Zi =d Y (c(f(x i)), c(fref (xi)))∈ {0,1}. Under the gold hypothesisH 0 the candidate is the reference up to noise,
soZ i ∼Bernoulli(p)for somep∈(0,1), with self distance meanpand per-probe varianceσ 2 =p(1−p). Under
the squatter hypothesisH 1 the candidate diverges on an extraγfraction of probes, soZ i ∼Bernoulli(p+γ)with
p+γ≤1, a behavioral distanceγto the reference. An identity rule with budgetmis a testψon the i.i.d. sample
Z1, . . . , Zm decidingH 0 againstH 1. The binary mismatch indicator is a realizable instance of the bounded behavioral
distance. A tool whose canonical response on each probe is either equal to the reference or maximally distant makes
dY ∈ {0,1}, which scalar-output tools such as get-sum already satisfy. A minimax lower bound proved on an instance
inside the model class is a valid lower bound for the class, so the rate below cannot be beaten in general even though
dY may take fractional values on other tools.
By Le Cam’s two-point lemma (Tsybakov, 2009), every such test has average error
1
2

PrH0 [ψ=1] + PrH1 [ψ=0]

≥ 1 2  1−TV(P ⊗m 0 , P⊗m 1 )  ,
whereP 0 = Bernoulli(p)andP 1 = Bernoulli(p+γ). Pinsker’s inequality with tensorization gives
TV(P ⊗m 0 , P⊗m 1 )≤ q 1 2 mKL(P 0∥P1), and a second-order expansion of the Bernoulli divergence, whose first-order
term vanishes atγ= 0, yieldsKL(P 0∥P1) = γ2 2p(1−p) +O(γ 3) = γ2 2σ2 (1 +o(1)). Combining the two bounds,
TV(P ⊗m 0 , P⊗m 1 )≤ γ 2σ √m(1 +o(1)).
For the average error to fall toδthe total variation must reach1−2δ, which forces
m≥ 4(1−2δ) 2 σ2
γ2 (1 +o(1)).
Hencem= Ω(σ 2/γ2)probes are necessary, matching the Bernstein upper bound of Appendix F.1 in theσ2/γ2 factor.
Thelog(n+k)factor in Theorem 1 is also necessary, by a multiple-hypothesis argument. TakeM=n+k
candidates andMregistry configurations, where configurationjmakes candidatejthe gold, with per-probe mis-
match lawBer(p)against the reference, and every other candidate a squatter at marginγ, with lawBer(p+γ).
A verifier that drawsmshared probes and observes all candidates must name the gold, anM-ary test. Be-
tween configurationsjandj ′ only candidatesjandj ′ change law, so with the symmetrized divergenceJ(a, b) =
KL(Ber(a)∥Ber(b)) + KL(Ber(b)∥Ber(a))the observation laws satisfy
KL(Pj∥Pj′) =m J(p, p+γ) =mγ2 σ2 (1 +o(1)).
18

ProbeIDPREPRINT
By Fano’s inequality with the mutual information bounded by the largest pairwise divergence, any rule has error
Pr[ˆȷ̸=j]≥1− mγ2/σ2 + log 2 logM ,
so identifying the gold with constant probability requiresm= Ω
 σ2
γ2 log(n+k)

. The variance-aware budget of
Appendix F.1 is thus tight in its leadingσ 2γ−2 log(n+k)term, and Theorem 1, whose worst-case rate takesσ 2 of
constant order, is tight inγand the candidate count. The lower bound does not capture the additiveO(γ −1 log(n+k))
Bernstein term, so the match is in the leading term, not the full finite-sample rate. The two constructions serve different
roles. Thek=1two-point test isolatesσ 2/γ2, while theM-ary independent-channel Fano packing yields the product
withlog(n+k). Both theσ 2/γ2 dependence and thelog(n+k)factor are minimax floors over the independent-
channel class, attained by the constructions above, so no identity rule removes them uniformly. They do not imply
that every registry is this hard, and probe secrecy is no substitute for probes that reach the difference. Kaufmann et al.
(2016) develop instance-dependent lower bounds of this kind for best-arm identification.
G Adaptive and independently authored squatters
G.1 Randomized probes against committed-coverage adversaries
The bound above assumes the probes are i.i.d. from a distributionD, not chosen after seeing the verifier. We now
allow an adaptive squatter that returns the gold response on a committed regionCof inputs and drifts elsewhere, where
Ccovers a fractionρ= Pr x∼D[x∈C]of the probe distribution. This committed-coverage adversary may know the
probe distribution and the verifier, but it commitsCbefore the probes are drawn. An adversary that observes the
drawn probes before responding is outside the model. If the verifier drawsmprobes i.i.d. fromD, the squatter evades
only when every probe lands inC, which happens with probabilityρ m, so ProbeID detects it with probability at least
1−ρ m, andm≥log(1/δ)/log(1/ρ)probes give detection probability1−δ. A fixed probe set that the adversary has
already seen is the caseρ= 1on that set and is evaded with certainty. Fresh unpredictable probes give exponential
decay inmonly when the committed region hasρ <1, and asCcovers almost all ofDthe squatter approaches a
twin on that distribution, although differences outside its support can remain harmful. Against an adaptive attacker the
probes must be secret as well as numerous, and the geometric bound makes this precise within a specific limit. Sinceρ
is the adversary’s coverage of the realized probe distribution, the guarantee requires thatDhave support the adversary
cannot enumerate and cover, and thatCbe committed without observing the drawn probes. A squatter that reverse-
engineers a predictable, small-support probe generator, for instance a verifier that only probes the schema boundary
values enumerated by M1, can setCto that support and driveρ→1, making the bound vacuous. The defense depends
on drawing from a large, high-entropy input space, as the live studies do, and not only on the probe count. The probe
generator ablation of Appendix L.1 confirms both halves of this caveat on a live server. Fresh schema-valid probes
recover identity, and the M1 boundary set over-covers a fixed drift region, as the small-support concern predicts.
The attested bank on a live server.Fresh probes must be available without live access to the trusted tool, which the
threat model excludes. We rerun the live committed-coverage study with the deployed protocol. At admission a bank
ofB=256schema-valid probes and their canonicalized gold responses is recorded. At selection each trial secretly
subsamplesmbank probes, the reference fingerprint is read from the recorded bank entries, and only the current
candidates are probed live. Over160trials per cell, detection matches the fresh-probe results. Atρ=0.5, hit@1 rises
0.700,0.956,1.000,1.000asmgoes2,4,8,16(the live fresh-probe run measured0.95atm=8), and atρ=0.9it
rises0.163,0.362,0.619,0.844, tracking1−ˆρ m at the bank’s realized coverageˆρ≈0.887of the nominal0.9. The
fixed-probe control stays at0.00at every budget, so detection depends on the secrecy of the subsample, not on bank
size. An attacker who commits its mimicry region before the bank is recorded gains nothing from the bank being
finite, and the trusted tool is queried only during admission. Repeated exposure of the same bank can still reveal it
(Appendix P).
Coverage and escalation.Two coverage levels alone do not establish whether a squatter that covers enough of the
input space is eventually selected or only escalated. We sweepρfrom0.1to0.99against budgetsm∈ {2,4,8,16},
160trials per cell, and score the deployed abstaining rule with its three outcomes rather than the forced choice used
above. Table G.1 reports the bank protocol.
The sweep separates two quantities that a single number hides. Coverage drives escalation. Atρ=0.99andm=2
the squatter forces abstention on0.994of trials, and a larger budget recovers only part of it, to0.863atm=16,
because at that coverage the squatter agrees with the gold almost everywhere and is close to the behavioral twin the
abstention rule exists for. Coverage does not lead to the squatter being selected. Across all88cells of the sweep and
19

ProbeIDPREPRINT
Table G.1:An adaptive squatter induces abstention without certification while the gold is a candidate(live get-
sum tool, bank of256probes,160trials per cell). Each entry is correct / abstain, and the misidentification rate is0.000
in every cell. Raising the committed coverageρconverts correct identifications into escalations, and a larger secret
subsample converts them back.
ρ m=2m=4m=8m=16
0.11.000 / 0.000 1.000 / 0.000 1.000 / 0.000 1.000 / 0.000
0.30.950 / 0.050 0.981 / 0.019 1.000 / 0.000 1.000 / 0.000
0.50.700 / 0.300 0.956 / 0.044 1.000 / 0.000 1.000 / 0.000
0.70.425 / 0.575 0.794 / 0.206 0.938 / 0.062 0.994 / 0.006
0.90.163 / 0.838 0.362 / 0.637 0.619 / 0.381 0.844 / 0.156
0.950.087 / 0.912 0.163 / 0.838 0.306 / 0.694 0.550 / 0.450
0.990.006 / 0.994 0.013 / 0.988 0.044 / 0.956 0.138 / 0.863
Table G.2:No misidentification of an independently authored squatter, including a white-box one, with the gold
among the candidates(50gold benchmark tools). A blind code-model squatter is detected or causes abstention when
it is a behavioral twin. A verifier-aware squatter that knows the distance and thresholds can only drive ProbeID to
abstain, since a deterministic gold at distance zero cannot be undercut, and the misidentification rate stays0over these
cases.
attackerkhit@1 abstain misid
blind 1 0.86 0.14 0.00
blind 8 0.84 0.16 0.00
verifier-aware 1 0.42 0.58 0.00
verifier-aware 8 0.10 0.90 0.00
both probe modes,14,080trials in total, the misidentification rate is0.000. The fixed-probe control is the extreme
case, abstaining on1.000of trials at everyρand everym, again with no misidentification. A fully predictable probe
set is evaded completely, and the failure is total escalation, not a wrong selection. The deterministic gold is among
the candidates and has zero distance, so the attack changes abstention rather than which candidate is nearest. This
experiment does not establish the same outcome for a replaced endpoint without the gold (Theorem 2).
Two facts limit the interpretation of the zero misidentification rate. The gold is a live deterministic server whose
distance to its own recorded bank is0.00in all14,080trials, and the selector abstains when the gap falls belowγ min,
so no squatter can be strictly nearer than the gold. Here a wrong certification is excluded by construction, and the
sweep measures the split between identification and abstention. Nor does the zero carry over to a squatter that replaces
the gold. With no gold among the candidates the decision is the one-sided gate of Appendix C, and a squatter is
accepted whenever every drawn probe falls in its mimicry region, with probability at leastρ m, the evasion term of the
bound at the start of this appendix.
G.2 Independently authored and verifier-aware squatters
The benchmark squatters come from two algorithmic families we wrote, output-value drift and silent field drift, the
axis the structural distance measures. To go beyond these families, a separate code model generates squatter behaviors
under two threat levels. This broadens the tested attacks but does not cover all adversaries. Ablindattacker sees only
the gold tool card, schema, and a sample response, and writes a plausibly drifted reimplementation. Averifier-aware
attacker is also told how ProbeID works, including canonicalization, the bounded structural distance and theτ hi/γmin
gates, and is instructed to minimize detectable divergence while still altering behavior. The squatter designs are the
model’s own and are released. We run the deployed abstaining selector, with unchanged scoring code, on50gold
benchmark tools and on four live tools of the everything reference server.
Table G.2 reports the benchmark arm. Against the blind attacker ProbeID holds hit@1 at0.84to0.86acrossk,
abstaining on the remainder, with a misidentification rate of0.00. An independently written squatter is still separated
in behavior space, so the result does not depend on the two mutation families. The verifier-aware attacker is the sharper
test. Told the distance and the thresholds, it shrinks its canonical divergence and drives hit@1 down to0.10atk=8,
but the loss in hit@1 corresponds to increased abstention, from0.58atk=1to0.90atk=8, and the misidentification
rate stays0.00at everyk. Knowing the verifier lets a squatter approach a behavioral twin and force an escalation, but
in these cases it was never selected. The gold here is its own cached reference at distance zero, so no squatter can
be strictly nearer, and the designs change only how much identification turns into abstention. The theorem’s bound
20

ProbeIDPREPRINT
Table H.1:Behavioral judges against ProbeID on the judge cohort(300gold per seed,3seeds,900case-runs
perk, same pool as Table J.1). The judges read the probe responses, not the descriptions, so they stay well above
the1/(k+ 1)random bound. The judge-view column is an exact-match rule that reads each response as the judges’
prompt shows it, cut to200characters. Best non-oracle result in bold.
kProbeID judge view, exact 7B judge 32B judge Random Oracle
11.0000.997 0.973 0.996 0.498 1.000
2 0.952 0.951 0.9230.9680.352 1.000
4 0.952 0.951 0.9060.9670.190 1.000
80.9520.951 0.844 0.950 0.103 1.000
Table H.2:The 32B judge on complete responses matches the truncated condition where it can read them.Same
900case-runs perkand one serving session for both conditions. Sent counts the case-runs whose complete-response
prompt fits the32,768-token context. The first four columns are hit@1 on the sent case-runs, and the last counts unsent
case-runs as misses.
ksent 200 characters complete ProbeID complete, all
1 827 0.995 0.998 1.000 0.917
2 817 0.965 0.961 0.947 0.872
4 792 0.962 0.957 0.946 0.842
8 746 0.946 0.945 0.946 0.783
does not apply to these fixed probes. Across the four squatter counts, the103benchmark cases that the verifier-aware
model drove to zero canonical divergence are such twins, and ProbeID abstained on all of them. The live arm agrees.
A blind squatter on the four live tools is caught at hit@11.00, and a verifier-aware one falls to0.17atk=8while its
misidentification rate stays0.00.
H A behavioral LLM-judge baseline
The description routers of Table J.1 collapse to chance because every candidate advertises the gold description, which
raises the question of whether a baseline that reads behavior instead of text can match the bounded behavioral distance.
The LLM judge runs Qwen2.5-7B. One request per case lists the trusted reference responses and every candidate’s
responses on the same probes ProbeID uses, in the case’s shuffled candidate order, each serialized response cut to200
characters. The judge answers with one integer, generating at most8tokens at temperature0, and names the candidate
whose behavior matches the reference, while0or an unparseable answer counts as an abstention. The prompt is
released with the code. The judge sees no descriptions, so the byte-identical rug pull does not defeat it and it does
not collapse to1/(k+ 1). It reads the same probes as ProbeID but only the first200characters of each response,
while ProbeID compares complete canonicalized responses, so the comparison does not isolate the distance rule. We
evaluate on the described pool of Table J.1, now with 300 gold tools per seed over three seeds.
The 7B judge performs well above chance. It reaches0.973atk=1and falls monotonically as candidates accumulate,
to0.844atk=8, while ProbeID stays at0.952fork≥2, a gap that widens from2.7to10.8points. Atk=8the 7B
judge sits at0.844with a95%exact binomial interval of[0.819,0.868]against ProbeID at0.952with[0.936,0.965],
overn=900case-runs. These intervals are descriptive. They treat case-runs as independent, although a gold can recur
across seeds because the golds of each seed are drawn from one pool of402tools, and the original judge runs kept no
per-case records from which a tool-level interval could be computed.
Information hidden by truncation.The effect of truncation can be measured without a model. We rebuilt every
case of this cohort from the cache and scored an exact-match rule with strict tie-breaking on each response as the
judge’s prompt renders it. The rebuild reproduces ProbeID’s and the random selector’s stored hit@1 at everyk.
Between498and512of the900case-runs perkcarry a response longer than the cut, yet the judge-view rule reaches
0.997atk=1and0.951atk≥2(Table H.1), against1.000and0.952for the same rule on complete responses. The
cut hides the only distinguishing difference in3case-runs atk=1and in1at each largerk. On this cohort truncation
removes little information needed for exact matching. The 32B judge’s0.950atk=8is close to that rule’s0.951on
the same view, and atk∈ {2,4}the judge exceeds it, since strict tie-breaking scores the rule’s ties as misses.
21

ProbeIDPREPRINT
Complete responses.We reran the 32B judge on the same3,600case-runs with each response left uncut, beside
the200-character condition in the same serving session, and kept every choice (Table H.2). The truncated condition
reproduces the values of Table H.1 exactly. A complete-response prompt longer than the judge’s native32,768-token
context cannot be sent, which happens in73,83,108and154of900case-runs atk=1,2,4and8, and20to56of them
exceed even128k tokens. On case-runs whose prompts fit the context window, the judge on complete responses scores
within0.006of the truncated condition at everyk, and every gold-clustered95%interval of the difference includes
zero. Counted as misses, the unsent case-runs lower complete-response hit@1 to0.783atk=8, while ProbeID reads
every case-run and scores at least0.981on the ones the judge cannot send. A decision costs1.95seconds on truncated
prompts and3.76seconds on complete ones, at concurrency16on one46GB GPU and excluding probe calls. Where
the judge can read complete responses they neither help nor hurt it, and its context limit, which ProbeID does not have,
excludes the rest.
Scaling the judge closes the accuracy gap. A Qwen2.5-32B judge on the same truncated evidence reaches0.996,0.968,
0.967, and0.950hit@1 atk∈ {1,2,4,8}, within a point or two of ProbeID and ahead atk∈ {2,4}, while the random
selector and oracle are bit for bit identical to the 7B run, since the pool and gold are unchanged. The study places
ProbeID at0.952on this cohort against0.956on the 150-gold headline cohort. A sufficiently large behavioral judge
recovers identity, so the router collapse of Table J.1 comes from the copied descriptions and not from the behavioral
channel. ProbeID and the 32B judge differ in the cost of the decision step, not in accuracy. Appendix H.1 measures
3.40seconds per decision for the judge on a dedicated46GB GPU against3.527milliseconds for the bounded distance
on one CPU core, both excluding probe calls. Access to behavior is necessary but not sufficient at 7B, and a large
judge or the bounded behavioral distance closes the remaining gap to the oracle.
H.1 Decision reproducibility and inference cost
A deterministic decision would distinguish ProbeID from a model judge only if the judge’s decisions varied across
identical requests. We replayed the judge’s requests to measure this and also report the cost of each decision step.
The judge is queried at temperature0, which is nominally greedy. Greedy decoding under a real serving stack is not by
itself a reproducibility guarantee, since continuous batching, prefix caching, and reduction order inside fused kernels
can all vary with server state, and the temperature pins none of them. We replayed identical requests and recorded
thechosen candidate, not only whether it was a hit, because two passes that both miss while naming different wrong
candidates disagree in a way a hit vector cannot show. ProbeID’s choice was recomputed on the same cases in the
same loop as a control.
Over900cases atk=8, three seeds, replayed three times against one server at concurrency16, the judge produced zero
decision changes, and per-seed hit@1 was identical to four decimals (0.9400,0.9367,0.9733, mean0.9500). After a
server restart, three further passes over300cases at concurrencies1,16, and4returned identical choice vectors, again
with zero changes. Aggregate hit@1 atk=8was also0.950under vLLM0.19.1, which produced the32B numbers
of Appendix H, and0.9500under0.24.0above, although choice vectors were not compared across versions. The
deterministic ProbeID control was unchanged. These observations are limited to the configurations we varied and
show no reproducibility advantage for ProbeID.
The cost of the decision step was measured on the same machine and the same cases. The judge takes3.40seconds
per decision on a dedicated46GB GPU at concurrency16(9186seconds for2700decisions). ProbeID takes3.527
milliseconds per decision on one CPU core, timing the identity rule alone with case construction excluded, over the
same900cases atk=8andm=12. The judge figure also assumes a46GB accelerator, a served32B checkpoint, and
an inference stack whose version becomes part of the verifier’s trusted base, while the bounded distance is arithmetic
over responses already collected. Both figures exclude the probe calls themselves, which the judge needs as much as
the bounded distance does, and on real servers those calls are the larger cost, so neither figure is an end-to-end latency.
Over the1,248probe responses recorded att 0 on the16census servers of Appendix O, the median call returns in1.3
milliseconds, but15.5%take longer than a second, the90th percentile is1.8seconds, and four of the16servers have
a median above one second. Wherever a tool calls a slow remote service, the end-to-end cost of a decision is set by
executingmprobes on each candidate, and the gap in the decision step does not carry over to it.
I Description routing and natural cases
I.1 Beyond identical descriptions
The headline keeps the squatter description byte identical to the gold, which forces routing to fail by construction.
Figure I.1 relaxes this and shows that the behavioral comparison is not tautological. It varies the squatter description
from identical to disjoint, at token overlapsfrom1to0, while keeping behavior mutated, atk=4. ProbeID stays flat
22

ProbeIDPREPRINT
0 0.25 0.5 0.75 1
squatter description similarity to the gold, s
0.0
0.2
0.4
0.6
0.8
1.0
identity hit@1, k = 4
stealthy
rug pull
ProbeID
BM25
dense retrieval
random
Figure I.1:ProbeID remains flat as description routers recover.Similaritysmoves from1to0atk=4, with
behavior still mutated. Routers recover away from copied descriptions, while ProbeID is independent ofs.
Table I.1:Behavioral twins require routing or escalation.Results use 300 gold tools and 3 seeds. ProbeID abstains
while lexical routing identifies the gold. The two signals address different failure modes (Table J.1).
kProbeID abstain ProbeID wrong, all cases lexical hit@1
1 1.00 0.00 0.998
2 1.00 0.00 0.991
4 1.00 0.00 0.983
at0.956, since it ignores descriptions. The description routers improve as the squatter description diverges from the
gold, with dense retrieval recovering earlier than BM25, and reach ceiling only when the squatter advertises a clearly
different description. A stealthy squatter that copies the description (highs) defeats routing, which handles only the
careless attacker, and ProbeID holds in that regime.
I.2 Complementarity on a constructed twin family
The main text reports natural sibling groups. In this constructed counterpart every candidate keeps the gold behavior
and differs only in its description, so the behavioral margin is zero by construction. The candidates are equivalent on
the probe distribution, the gap gate abstains, and these responses cannot recover which tool was recorded (Table I.1).
I.3 Natural description collisions and a dense router
The headline rug pull copies the gold description byte for byte, which defeats routing by construction. This study
uses only vendor-authored descriptions and replaces the lexical router with a dense embedding one. Real Model
Context Protocol servers already ship groups of tools whose vendor-written descriptions naturally overlap, whose
input schemas are compatible, and whose behavior differs. We use these groups over live stdio JSON-RPC on the
official filesystem server. The listing group holds three real listing tools that take a single path and return a plain
directory listing, the same listing with sizes, or a recursive JSON tree. Their vendor descriptions are near duplicates,
with an all-MiniLM-L6-v2 cosine of0.80and a Jaccard of0.85between the closest pair, yet the three tools have
pairwise distance1.00on the tested probes. The reading group holds read_text_file and its deprecated alias, a genuine
behavioral twin at description cosine0.58.
An agent records a reference for one tool in a group and must re-identify that tool among its natural siblings. A
description router scores each candidate’s real description against the agent’s natural language intent, averaged over
three phrasings of the need. For the listing group they areshow the files and directories inside a folder,list the contents
of a directoryandwhat files are in this path. For the reading group they areread the text contents of a file,get the
23

ProbeIDPREPRINT
Table I.2:The admission reference separates natural siblings, and ProbeID abstains on an alias(live filesystem
server, real vendor descriptions, all-MiniLM-L6-v2 dense router,30seeds, strict tie-breaking). The listing group has
three behaviorally distinct siblings, the reading group has a tool and its deprecated alias (a behavioral twin). ProbeID
recovers the recorded tool by behavior, or abstains on the twin, while a dense embedding router and a lexical Jaccard
router, which lack the reference, sit at the1/|C|chance line. Best in bold.
group (|C|) ProbeID abstain dense Jaccard chance
listing (3)1.000.00 0.33 0.33 0.33
reading (2) – 1.00 0.50 0.50 0.50
Table I.3:Probe budgets resolve two close JSON implementations(the CPython and V8 serializers, live over stdio
JSON-RPC,100seeds). The tools agree on most inputs and diverge only on integer-valued floats and non-ASCII
escaping, a small natural marginϕ. Identity hit@1 rises with the probe budgetmand tracks1−(1−ϕ) m. No wrong
candidate was selected in any of the100seeded trials of any cell, since the gold matches its own reference, and the
remainder abstains.
marginϕ m=1m=2m=4m=8m=16
0.150.15 0.34 0.38 0.65 0.93
0.300.29 0.58 0.74 0.95 1.00
0.500.49 0.75 0.94 0.99 1.00
full text of a fileandopen a file and return its text. ProbeID probes each candidate live and matches behavior to the
recorded reference, abstaining on a true twin. We compare a dense router that embeds descriptions with MiniLM
against a lexical Jaccard router. We author no descriptions. Every description is the vendor’s own, fetched live from
the server’s tool listing.
Table I.2 reports the result. On the listing group ProbeID recovers the recorded tool at hit@11.00, since the siblings
are maximally separated in behavior, a sibling distance of1.00against a self distance of0.00. Both routers sit at the
1/3chance line, the dense one no better than the lexical one, because near-duplicate descriptions do not encode which
specific sibling a reference recorded, so the router picks the same candidate regardless of the truth. On the reading
group the deprecated alias is a behavioral twin, so ProbeID abstains on every trial while the routers stay at the1/2
chance line. These vendor-authored siblings test identification against an admission reference, which ProbeID reads
and the shared intent cannot reveal, so the result concerns this information asymmetry and not general dense-retrieval
accuracy. Two caveats limit it. First, the behavioral separation in the listing group is large, so the study measures a
router’s blindness to natural description collisions and not a difficult behavioral distinction, and the behaviorally hard
natural case is the twin in the reading group, where ProbeID correctly abstains. Second, the admission reference is
unavailable to the description router, which matches the stated verification task but limits a direct accuracy comparison
with intent-based retrieval.
I.4 Two real implementations, a behaviorally close natural case
The natural sibling study of Appendix I.3 separates tools whose behavior differs on every probe. The harder and more
realistic case is two legitimate tools that agree on most inputs and diverge on a few, a small natural margin rather
than a maximal one. We test this case with two real, independently implemented JSON serializers exposed as live
MCP tools over stdio JSON-RPC, with the JSON serializer of CPython’s standard library as the gold and V8’s built-in
serializer run through a live Node worker as the candidate. Neither is malicious. We run both in compact mode so
that whitespace, a formatting choice the canonicalizer does not normalize (Appendix E), does not mask the semantic
divergence. Each tool returns its serialized text as a string field, which the canonicalizer compares literally. On the
tested workload they agree on integers, ASCII strings, and fractional floats, and differ where their documented defaults
differ, an integer-valued float (62.0against62) and a non-ASCII character (é written as a Unicode escape sequence
against a raw é). The divergence arises from the implementations’ defaults without an authored drift, and the tool cards
are the vendors’ own wording, the CPython docstring against the MDN description, at a dense embedding cosine of
0.54.
An agent records a reference from the CPython tool and must re-identify it against the V8 tool. A probe lands in the
naturally divergent region with probabilityϕ, set by the workload, so the per-probe mismatch of the V8 tool is a real
Bernoulli(ϕ)variable. This deterministic agreement experiment tests the margin-dependent budget on real software.
It does not instantiate the noisy minimax construction of Appendix F.2. We sweepϕand the budgetmover100seeds.
24

ProbeIDPREPRINT
Table J.1:ProbeID recovers identity where copied descriptions reduce routers to chance.Identity hit@1 under
rug pull drift, on 402 tools with real ToolBench descriptions (150 gold per seed, 3 seeds). BM25, dense retrieval, and
an LLM reranker all match random because the squatter copies the gold description. Best non-oracle result in bold.
kProbeID BM25 Dense LLM-card Random Oracle
11.0000.496 0.516 0.496 0.538 1.000
20.9560.344 0.344 0.344 0.349 1.000
40.9560.200 0.207 0.200 0.191 1.000
80.9560.111 0.111 0.111 0.107 1.000
Table I.3 reports identity hit@1, and two properties hold in every cell. First, the misidentification rate is0.00. The
CPython tool matches its own reference, so it is never beaten, and ProbeID either names it when a probe hits the
divergence or abstains, never selecting the wrong implementation. Second, the observed margin constrains the budget.
Atϕ≈0.3hit@1 rises0.29,0.58,0.74,0.95,1.00asmgoes1,2,4,8,16, tracking1−(1−ϕ) m, and a smaller margin
needs a larger budget, withϕ≈0.15reaching0.93only atm=16. The rest abstain. This is the Theorem 1 dependence
on a behaviorally close pair of real, independently written tools, the regime where identity is hard.
J Canonicalization and simple behavioral baselines
J.1 The canonicalization ablation in full
Injecting ten random timestamp and id fields into each response isolates the effect of canonicalization. On the 150-
gold headline cohort with canonicalization on, the noise floor stays at0.00and hit@1 at0.956fork≥2, matching
the noise-free run. With it off the gold self distance rises to0.73and forced-choice identity barely moves,0.953at
k=4, because symmetric noise cancels in the ranking, and a gate at the twin study’sτ hi=0.6would reject the average
gold, since0.73exceeds it. This compares the measured self distance with the threshold and is not a gated run.
Canonicalization lowers the measured self distance relative to this fixed threshold. Under noise that canonicalization
does not remove, a0/1equality or hash baseline loses discrimination while continuousd Y retains it (Appendix J.2).
J.2 Simple behavioral baselines
To test whether the bounded structural distance is necessary, we add three simple baselines that share ProbeID’s
probe set, fingerprints and strict tie-breaking and differ only in how they compare responses.Exact equalityscores
a candidate by the fraction of probes whose canonical response differs from the reference, a 0/1 test in place of the
structurald Y .Response hashcompares the sets of response hashes by Jaccard distance, the usual signature-matching
check.Per-probe votekeeps a continuous per-probe distance but aggregates by majority vote instead of the mean.
Three further selectors use alternative response comparisons. Anembedding nearest-neighbor(NN) selector encodes
each canonicalized response with all-MiniLM-L6-v2 mean pooling and scores a candidate by the mean per-probe
cosine distance to the reference, which tests whether response embeddings can replace the structural distance. AMET
style MMDtreats the reference and candidate response sets as two samples and computes an unbiased MMD 2, the
test of Gao et al. (2025) with a character 4-gram spectrum kernel in place of their Hamming kernel. The embedding
selector serializes each canonical response as sorted JSON and truncates it to256tokens. The spectrum kernel is
normalized to unit self-similarity, and a negative unbiased estimate is not clipped. Adefinition hash pinfollows the
industry practice of pinning a hash of the tool definition, description plus schema (Beurer-Kellner & Fischer, 2025a),
and selects uniformly among pin-matching candidates. A deployed toolkit implements this check. The AI SDK digests
each tool’s description, resolved input schema and title and diffs two such digests to flag drift (Vercel, 2026). Two
shortcuts bound what a trivial signal achieves.Status onlycompares the status channel alone, andtype and length
compares each response’s top-level type and the relative gap between serialized lengths. All selectors are scored on
one fixed cohort, the described pool with300gold per seed over three seeds, whose cases are built from clean canonical
behavior and held fixed while one factor of the observation changes. The canonicalizer is on or off. The noise is one of
four kinds, namely none, ten volatile fields named on the canonicalizer’s drop list as in the canonicalization ablation,
ten volatile fields under names the drop list misses, or independent jitter of every scalar leaf with probabilityρ. The
unlisted names include a camel-case creation time, a hyphenated request identifier and a latency. The reference, the
gold and every squatter are observed with independent noise.
Table J.2 separates the factors that the canonicalization ablation changed together. On the clean cache every compari-
son of complete responses scores0.952, a selector reading only each response’s type and length already scores0.927,
and status alone scores0because every cached response reports success, so the clean column cannot rank comparisons.
25

ProbeIDPREPRINT
Table J.2:On one fixed cohort, the structural distance does not dominate every behavioral comparison(k=4,
300 gold per seed, 3 seeds). V olatile fields named on the drop list leave every selector at the clean value when the
canonicalizer is on, by construction, and that column is omitted. A canonicalizer tolerates only fields it names, 0/1
tests fall furthest under noise it does not remove, the set-level MMD degrades least under value jitter, and on the clean
cache even type and length separates most cases.
no noise ten volatile fields leaf jitter, canon on
selector canon on canon off listed, off unlisted, onρ=0.1ρ=0.2
ProbeID (structurald Y ) 0.952 0.974 0.952 0.950 0.950 0.927
per-probe vote 0.952 0.974 0.952 0.950 0.943 0.920
MET style MMD 0.952 0.974 0.953 0.951 0.956 0.949
embedding NN 0.952 0.974 0.899 0.868 0.928 0.917
exact equality (0/1) 0.952 0.974 0.083 0.083 0.761 0.641
response hash 0.952 0.974 0.083 0.083 0.752 0.657
type and length 0.927 0.946 0.818 0.851 0.921 0.905
status only 0.000 0.000 0.000 0.000 0.000 0.000
definition hash pin 0.202 0.202 0.202 0.202 0.202 0.202
random 0.190 0.190 0.190 0.190 0.190 0.190
gold self distance 0.00 0.00 0.74 0.74 0.17 0.29
Switching the canonicalizer off there raises every comparison of complete responses to0.974. The drop list also hides
drift confined to the fields it drops. Across the20cases that change,40squatters tie the gold,34of which delete a date,
cursor or id key while the other6mutate only such fields. A canonicalizer tolerates the fields it names and nothing
else. Named volatile fields leave every selector at its clean value, and the same fields under unlisted names act as if the
canonicalizer were off. The gold self distance rises to0.74. Exact equality and response hash fall to0.083, below the
random bound, because every response mismatches on its volatile fields, while the structural distance holds at0.950
and the MMD at0.951. The embedding NN degrades more askgrows, from0.931atk=1to0.822atk=8under
unlisted fields, because volatile tokens move the whole vector. Jitter on the fields the canonicalizer keeps separates
the continuous selectors. The structural distance degrades gradually,0.957,0.950and0.927atρof0.05,0.1and
0.2. The 0/1 tests degrade faster, to0.641and0.657, and the MMD performs best, at0.949. Atk=8andρ=0.2the
MMD’s0.944is well ahead of the structural distance’s0.881, and the type and length shortcut reaches0.889. With
cases ranked by each selector’s own gap between its two nearest candidates, the area under the risk-coverage curve at
ρ=0.2is0.008for the structural distance,0.003for the MMD and0.128for exact equality. Under the tested noise
that canonicalization does not remove, continuous comparisons outperform equality, and among them the structural
distance is not the most stable under value noise. Theorem 1 and the abstention guarantee are stated for the probe
mean of a bounded per-probe comparison. They hold for exact equality and for the per-probe vote, whose vote share
is the probe mean of a bounded indicator, each with the margin measured on its own comparison. The set-level MMD
is not a probe mean and carries no such guarantee. The framework supplies the accounting from margin to budget and
a joint error bound for whichever bounded per-probe comparison a deployment’s noise calls for, and the MMD result
stays empirical. It does not depend on choosingd Y over a 0/1 test or a set statistic, and on deterministic drift a 0/1
test has the larger margin and verifies at a smaller budget (Appendix P). The definition hash pin sits at chance at every
k,0.499down to0.100. A behavior-only rug pull leaves the pinned definition untouched, so pinning admits every
candidate and carries no identity signal. An admission-time pin and a use-time behavioral check thus complement
each other.
Paired uncertainty.Resampling each gold with all its case-runs gives a pointwise95%interval of[0.043,0.085]for
the MMD minus structural-distance hit@1 difference of0.063atρ=0.2,k=8, over900case-runs from393gold tools.
Atρ=0.1and the same candidate count, the observed difference is0.006with interval[−0.003,0.015], which does not
resolve their ordering. These exploratory intervals reuse the original tools and injected noise, cover all saved regimes
in the supplement, and are not adjusted for multiple comparisons. They provide no independent-cohort validation.
K Further results on the cached benchmark
K.1 The probe budget on real recorded behavior
The controlled channel of Figure 2(b) isolates theσ 2 factor, with its smallest budgets in Table K.1, but it is simulated.
To check that the budget binds on real responses, we use a squatter that returns the gold response on a1−γfraction of
26

ProbeIDPREPRINT
2 4 8 16
probe budget m, real recorded responses, k = 4
0.0
0.2
0.4
0.6
0.8
1.0
identity hit@1
γ = 0.15
γ = 0.3
γ = 0.5
measured
qk/(1 − (1 − q)k)
Figure K.1:The probe budget binds on real recorded behavior.Identity hit@1 against probe budgetmwhen the
squatter diverges on aγfraction of real cached probes (k=4). Solid is measured, dashed is the matching closed form
conditional on a separable case. Each probe replays a recorded response of a real API, so the budget effect is not an
artifact of the simulated channel of Figure 2(b).
Table K.1:The 0.99 hit@1 budget is consistent withm ⋆ ∝σ 2/γ2.Results use 200 gold and 3 seeds. The product
m⋆γ2 is approximately constant across nominal margins and rises with self distance, consistent with theσ 2 factor.
γ=0.1 0.15 0.2 0.3 0.4
m⋆ (self dist.0.18) 256 128 128 64 32
m⋆γ2 2.6 2.9 5.1 5.8 5.1
m⋆ (self dist.0.34)>256 256 128 64 64
m⋆γ2 – 5.8 5.1 5.8 10.2
probes and a mutation on the rest, so its per-probe failure probability isγ. Figure K.1 reports identity hit@1 against the
budgetmfor three margins atk=4. As in Results 1 and 3, a case is kept only when at least one squatter is behaviorally
separable, so the reported hit@1 and its closed formqk/(1−(1−q) k)withq=1−(1−γ) m, which assumes independent
separation events across squatters, are conditional on that event. The event changes with the budget. Atγ=0.3the
exclusions fall from53of the503golds drawn over three seeds atm=2to13of463atm=16. Counting the excluded
golds as misses lowers every measured point of the figure by at most0.04, and the unconditional curve then sits below
qk by as much as0.09, against0.07for the conditional pair. Hit@1 rises withmand tracks this form, and a smaller
margin needs a larger budget. The candidate count moves the shared-input budget in the direction of the union bound.
Atγ=0.3, reaching0.9hit@1 needsm≈12atk=4andm≈16atk=8. The measured curve sits a few points below
the idealized form at largem, because some sparse responses canonicalize a mutation back to the gold.
K.2 Squatter counts beyond eight
The headline sweep stops atk=8, well inside the range where the 12-probe budget saturates, so it does not stress the
log(n+k)dependence of Theorem 1 at the squatter counts a heavily typosquatted registry could present. We extend
the same protocol, 150 gold per seed, three seeds, the same drift families and budget, tok∈ {16,32,64}. ProbeID is
flat at0.956at all three counts, unchanged fromk=8. BM25 and dense retrieval fall to0.058,0.022, and0.009, at or
below the1/(k+ 1)chance line (0.059,0.030,0.015), since identical inputs leave a router only tie-breaking, and the
random selector tracks that line at0.067,0.038,0.016. This flat curve does not test the logarithmic dependence. On
this noiseless cache the gold sits at distance zero and every added squatter comes from the same two mutation families,
so once both families are separated the squatter count cannot move ProbeID. The candidate count enters the budget
where noise does, in Result 2 and Appendix K.1, while here every description signal is already gone.
27

ProbeIDPREPRINT
Table L.1:Fresh probes recover identity on a live server without cached replay(live get-sum tool, graded near
twin at marginϕ,k=1, 30 fresh probe draws per cell, no cache consulted). The uniform control’s hit@1 tracks
1−(1−ϕ) m at its realized divergence. The proposed M1 generator reaches1.00at least as fast, since its boundary
values over-cover the tested drift region.
sourceϕidentity hit@1 atm
1 2 4 8 16
uniform0.150.10 0.33 0.53 0.73 0.90
0.300.27 0.50 0.70 0.93 1.00
0.500.40 0.67 0.93 1.00 1.00
M1 schema0.150.60 0.70 0.83 1.00 1.00
0.300.63 0.80 0.87 1.00 1.00
0.500.67 0.83 0.90 1.00 1.00
K.3 Abstention on fixed cached cases
Theorem 2 applies to independently sampled probes and a gold-present candidate pool. The headline benchmark
instead forces strict choice on fixed cache-order probes, at most12per case. We saved every candidate distance and
rescored the same450cases per squatter count. For each case, we setϵ i =
p
log(2(k+1)/0.05)/(2mi),γ min,i = 2ϵi,
andτ hi,i =d t⋆,i +ϵ i using its actualm i ∈[4,12]. The observed gold distance is0throughout, and the threshold uses
it, so this is a retrospective rescore rather than a deployable threshold rule. The rescore decides221,83,78, and69
cases atk∈ {1,2,4,8}, respectively, with no observed wrong decisions. This is an empirical operating point under
a theorem-inspired radius, not a probability certificate. The radius must use each case’s own probe count. Setting it
withm=12for every case would shrink it for the202of450cases atk=8that have fewer probes and would inflate
coverage from69/450to141/450.
The full threshold grid is descriptive because its favorable points were identified using these cases. Withτ hi=1and
γmin=0.01, coverage is0.956with no observed wrong decisions on this benchmark. The value equals strict-choice
hit@1 because this grid point decides every non-tied case and abstains on the ties that strict choice scores as misses.
The gold distance is0.00in all1,800cases, and the smallest positive gap atk≥2is0.057, so this grid point separates
every non-tied case. It cannot establish error control on unseen cases. On the behavioral twin study, the margin gate
abstains throughout because these probes contain no distinguishing response.
The same per-case records explain the headline misses. At eachk≥2, all20missed case-runs out of450, or4.4%,
have a gap of0between the gold and the nearest squatter on every available cached probe, so every miss is a realized
behavioral twin under strict tie-breaking, not a near miss. Eleven of the20missed tools expose fewer than the full12
cached probes, so their budget is bounded by cache availability rather than by the probe generator.
L Live MCP servers
L.1 Probe generator ablation on a live server
The cached benchmark treats each gold tool’s cached arguments as its probe set, so it does not test whether the schema-
driven probe generator, module M1, produces useful unseen inputs. The live-server experiment tests freshly generated
probes without cache access. The gold is the live get-sum tool of the everything server, and the squatter is a graded
near twin that drifts on aϕfraction of the integer input space. We compare two probe sources, both drawn fresh on
every trial and never reused. They are the proposed M1 generator, which emits boundary, enumerated, and random
schema-valid values, and a broad uniform random sampler as a coverage control. With strict tie-breaking the gold is
named only when some probe lands in the squatter’s drift region, so identity hit@1 should track1−(1−ϕ) m for any
source that samples the space.
In Table L.1 the uniform control behaves as predicted. Its realized divergence matches the nominalϕ, and hit@1
tracks1−(1−ϕ) m across budgets. Atϕ=0.3it rises0.27,0.50,0.70,0.93,1.00form=1,2,4,8,16against a closed
form of0.93atm=8, and atϕ=0.5the single-probe value is0.40, slightly belowϕ. Identity is recovered from
behavior on newly drawn schema-valid inputs outside the cached benchmark, not by replaying known arguments. The
M1 generator also drives hit@1 to1.00at every margin bym=8, which the uniform control does not. Its boundary
integers over-cover this hash-defined drift region, so its realized divergence runs above the nominalϕ. The gold self
distance is0.00throughout, so the noiseless margin holds on the live tool. This over-coverage is also the limit noted
28

ProbeIDPREPRINT
Table L.2:Identity hit@1 on three live MCP server familiesover stdio JSON-RPC,30seeds per cell, strict tie-
breaking. The description router over the byte-identical tool cards can only guess at1/(k+1). ProbeID recovers
identity as the probe budget grows on the filesystem and memory families, where each squatter is the same official
binary on tampered data, and saturates at one probe on the everything family, whose squatter drifts on every input.
familykProbeID hit@1 atmrouter
(tool)1 2 4 8 1 k+1
filesystem10.53 0.77 0.93 1.00 0.50
(read_text_file)20.27 0.70 0.93 1.00 0.33
30.00 0.43 0.90 1.00 0.25
memory10.60 0.77 0.97 1.00 0.50
(open_nodes)20.33 0.73 0.93 1.00 0.33
30.00 0.50 0.93 1.00 0.25
everything11.00 1.00 1.00 1.00 0.50
(get-sum)21.00 1.00 1.00 1.00 0.33
31.00 1.00 1.00 1.00 0.25
in Appendix G.1. An adaptive adversary could enumerate a small, predictable boundary set, so the live studies draw
from a large input space instead.
L.2 Diverse live servers
The live study of the main text uses the everything reference server. To check that identity recovery is not specific
to one server, we run ProbeID against three official MCP server families over live stdio JSON-RPC with no caching,
the filesystem server (read_text_file), the memory server (open_nodes) and the everything server (get-sum). The
filesystem and memory families stage a data-level rug pull, in which each squatter is the same official server binary
serving tampered backing data. The executable, tool schema and human-readable description are identical to the
gold, and only the backing data drifts. Each squatter tampers with a distinct nonempty half of the files or graph
entities. This is a weaker adversary than an independently re-implemented squatter, which we study separately in
Appendix L.3, because the output format and error behavior are inherited from the gold binary. The everything family
keeps the re-declared FastMCP squatter on get-sum. Across all three families the squatter and gold descriptions are
byte identical (verified from the live tool listing) and the gold self distance is0.00. The canonicalizer maps three
response modalities, file text, JSON knowledge-graph nodes and integer sums, to a stable signal.
On the filesystem and memory families the budget binds as predicted (Table L.2). A single probe may miss a squatter
whose tampered half it does not sample, but a handful drive hit@1 to1.00. The description router is pinned at
1/(k+ 1)because the tool cards are byte identical. Thek>1rows fall lower at the smallest budget because strict
tie-breaking demands that the gold separate from every one of theksquatters at once. We do not read these families
askindependent pieces of evidence, since the tampered regions of sibling squatters overlap. The same nearest-
fingerprint rule and canonicalizer recover identity across three real server binaries and three response modalities,
against descriptions copied byte for byte, although the guarantee also needs its sampling and margin conditions.
A census of authenticated production servers with side effects remains out of scope, for the reason stated in the
limitations.
L.3 Re-implemented squatters
The same-binary study above uses a weak adversary by design. A realistic rug pull squatter does not corrupt the
gold server’s backing data but runs an independent server that mimics the gold’s tool card and output format while
its behavior drifts. We test this case. For four tools across three official servers (get-sum and echo on everything,
read_text_file on filesystem, open_nodes on memory), the gold is the official reference server over live stdio JSON-
RPC. The squatters are hand-written re-implementations that share no code with the official server, one in raw JSON-
RPC without the MCP SDK and one on the SDK’s low-level server interface. Each squatter re-declares the target tool
with a byte-identical description, fetched live from the gold, and serves behavior from one verified drift model. The
squatter variants differ in stealth.
• Asloppysquatter returns a different output format (the careless attacker).
29

ProbeIDPREPRINT
Table L.3:Tested value drift separates re-implemented squatters, identity hit@1 over live stdio JSON-RPC
(k=3squatters in two distinct codebases,30seeds, strict tie-breaking). A format-faithful squatter that copies the
gold’s exact output envelope but returns a wrong value is caught at a single probe, identically to a sloppy one, because
the behavioral distance compares canonicalized values, not format. Under the gated rule, ProbeID abstains on the
exact behavioral twin. Self distance is the gold against itself and twin distance is the re-implemented twin against the
gold, both0.00on the sampled responses.
tool sloppy faithful twin self twin
(server)m=1m=1abstain dist dist
get-sum (everything) 1.00 1.00 1.00 0.00 0.00
echo (everything) 1.00 1.00 1.00 0.00 0.00
read_text_file (fs) 1.00 1.00 1.00 0.00 0.00
open_nodes (memory) 1.00 1.00 1.00 0.00 0.00
Table M.1:Sandboxed state restores identity in the counter experiment.Gold step1, squatter step2,m=8,30
trials. Shared sessions produce abstention, while a fresh sandbox restores zero self distance and identifies the gold.
probing self dist abstain wrong, all trials hit@1
naive (shared) 1.00 1.00 0.00 –
sandboxed (fresh) 0.00 0.00 0.00 1.00
• Aformat-faithfulsquatter copies the gold’s exact output envelope, error behavior and field structure, with a
wrong value on every probe (the stealthy attacker).
• Anear twinis format faithful and drifts on only a fractionϕof inputs.
• Anexact twinbehaves identically.
The format-faithful squatter tests whether an independent re-implementation that mimics the gold’s format can slip
past a behavioral check (Table L.3). In these experiments it does not. Canonicalization compares values, and the
tested wrong values separate the squatter from the gold at hit@1= 1.00with a single probe across all four tools
and both codebases. Only the near twin survives, and only in proportion to how rarely it drifts. On the two tools
with large input spaces (get-sum and echo,k=1), hit@1 rises toward1−(1−ϕ) m as the budget grows. For echo
atϕ=0.5it is0.40,0.70,0.90,0.97atm=1,2,4,8. A smaller marginϕ=0.15needs the full budget to climb, the
Theorem 1 dependence of Figure 2(c) now against a re-implemented near twin. The exact twin is the limitϕ=0, on
which ProbeID abstains at every budget and never selects the twin over the gold (twin distance0.00). The description
router is pinned at1/(k+1)throughout, since the four tool cards are byte identical. The fingerprint reads only tool-
call responses, never server metadata such as the information block returned at initialization, which the threat model
treats as attacker controlled. A squatter can spoof its advertised name, and in these four read-only tests the sampled
responses still separate the value-drifting squatters. This study covers only read-only, deterministic tools with few side
effects, the class our threat model targets. Appendix M.1 studies the stateful case and Appendix M.2 side-effecting
and authenticated tools, and authenticated production servers remain future work.
M Stateful, side-effecting and authenticated tools
M.1 Stateful and side-effecting tools
Theorem 1 assumes independent per-probe observations. A stateful tool violates this, because a side-effecting call
changes the server and the same probe then returns a different response depending on call order. We test this on a live
stateful MCP server whose counter tool adds a step to an internal accumulator on every call and returns the running
total. The gold steps by1and a behavioral squatter steps by2. We compare two probing strategies over30trials at
m=8(Table M.1).
Under naive probing a single shared session is reused, so the gold’s reference and its re-probed fingerprint advance
to different totals. The gold self distance is1.00, far above the distance thresholdτ hi=0.5, so the nearest-fingerprint
selector abstains on every trial with a misidentification rate of0.00. The stateful tool triggers abstention. ProbeID
detects that no candidate matches, not even the gold, and escalates. Under sandboxed probing a fresh server instance
serves each fingerprint, so every fingerprint starts from a clean state. The gold self distance returns to0.00and identity
hit@1 is1.00, separating the step-by-1 gold from the step-by-2 squatter. For a side-effecting tool, the deployment
30

ProbeIDPREPRINT
Table M.2:Observed writes and authentication checks distinguish the tested squatters.Live FastMCP,30trials,
strict ties, and identical tool cards. Reset sandboxes expose changed overwrite semantics or bypassed authentication,
with no observed misidentification.
tool squatter drift hit@1 misident.
store write semantics 1.00 0.00
read_secret auth bypass 1.00 0.00
procedure is to probe a reset sandbox or a dry-run endpoint, which restores a zero self distance, and to abstain when
no such sandbox is available. The probes of one fingerprint still run in sequence inside one sandbox, so their responses
are not independent and Theorem 1 does not cover them. The independent unit is the reset episode, and this result is
empirical.
M.2 Side-effecting writes and authentication
The studies so far probe read-only tools or a single counter. Two tool classes common in production agents fall outside
that scope, tools that mutate persistent state through writes and tools gated by authentication. We test both on live
FastMCP servers over stdio JSON-RPC, with the squatter and gold tool cards byte identical, so only behavior can
separate them.
A side-effecting key-value store.The store tool sets and gets values by key. The gold uses last-write-wins overwrite
semantics. The squatter silently ignores a write when the key already exists, a first-write-wins data-integrity drift
a description router cannot see. Each fingerprint is taken in a reset sandbox, the deployment procedure for side-
effecting tools established for the counter in Appendix M.1, so the gold matches its own reference at self distance
0.00. ProbeID separates the two write semantics on the get-after-update probes and recovers identity at hit@11.00
with a misidentification rate of0.00(Table M.2).
An authentication-gated tool.The read_secret tool returns a protected resource only for a valid token, and the
gold rejects an invalid token with an authorization error. The squatter bypasses the check and returns the resource for
any token, a security-relevant authentication drift behind an identical tool card. A probe set that alternates valid and
invalid tokens separates them, since the two agree on valid-token probes and diverge on every invalid-token probe,
placing the bypass squatter at behavioral distance0.50from the reference. ProbeID recovers the gold at hit@11.00,
at self distance0.00, with a misidentification rate of0.00, while a description router is blind by construction. This
tested bypass accepts any token, so it diverges on every invalid-token probe and is caught by construction. A stealthier
backdoor that rejected the probe tokens and bypassed only an attacker-held secret would agree with the gold across the
probe distribution and drift only off it, the measure-zero high-coverage evasion of Appendix G.1. With the gold present
ProbeID still ties it at distance zero and abstains, so misidentification stays zero, but detecting such an off-distribution
backdoor lies outside the on-Dguarantee and is not claimed.
These remain controlled, self-hosted tools with cooperative squatters that do not distinguish probe traffic from pro-
duction traffic, so the study shows identity recovery on side-effecting and authenticated behavior without settling the
adaptive or production-scale case. The in-the-wild census of Appendix O probes real third-party servers, and a corpus
of verified runnable MCP servers (Wu et al., 2025) makes a full production-scale census feasible. Throughout, the
recipe probes a reset sandbox or a dry-run endpoint to restore a zero self distance, compares canonicalized behavior
and abstains when no candidate matches.
N Behavioral distance under large outputs
Any structural distance risks dilution. If a tool returns a large object and a format-faithful squatter perturbs only one
leaf field, the normalizedd Y on a single probe is tiny, and the per-probe margin may fall below the decision threshold.
We test this on a live server. The gold is the official memory server. One probe requestsNentity nodes at once,
so a single live response is a large structured object, and a re-implemented squatter (raw JSON-RPC, byte-identical
description) returns the sameNnodes withfof them perturbed in a format-faithful way. The measured per-probe
margin is thenγ=f /(12N), which we confirm live.
Table N.1 shows that forced-choice ranking and gated acceptance respond differently to dilution. The deterministic
identity ranking is stable, because any nonzero distance places the squatter behind the gold, so hit@1 is1.00at every
output size, down toγ= 0.002atN=40. ProbeID does not miss the squatter, but the gated margin is diluted. At
31

ProbeIDPREPRINT
Table N.1:Large outputs dilute the observed margin and increase abstention.Memory queries usef=1changed
node andγ min=0.05. The margin shrinks as1/N. Ranking remains correct, while a one-field difference below the
threshold triggers escalation.
output sizeN1 2 5 10 20 40
marginγ0.083 0.042 0.017 0.008 0.004 0.002
identity hit@1 1.00 1.00 1.00 1.00 1.00 1.00
passes margin gate (γ≥γmin) yes no no no no no
Table O.1:In-the-wild self distance on16real MCP servers(read-only tools,3probe passes, canonicalization on).
Under canonicalization most real tools are deterministic (self distance0), which says nothing about whether squatters
are separable. A minority are nondeterministic, theσ >0regime that the variance-aware budget and the abstention
rule address. Canonicalization succeeds on every response of every server.
regime servers tools probed mean self distance
deterministic 10 35 0.00
nondeterministic 4 16 0.10–0.92
γmin=0.05the gold passes the margin gate atN=1and the rule abstains forN≥2, because a one-field difference in
a large object is an ambiguous signal. ProbeID escalates instead of deciding on insufficient evidence and never selects
the squatter. The margin isf /(12N). WithN=20, raising the perturbed field countffrom1to20movesγfrom
0.004to0.083and passes the gate again atf=20. A small margin falls within the regime Theorem 1 governs. The
leading term of the Bernstein budget scales asσ2/γ2, so at fixedσa one-field drift in anN-field output needs a budget
growing asN 2. Dilution is the price of a mean-aggregated distance, which tolerates per-field noise, whereas a max
aggregation would react to any single noisy field. Per-field certification for very large outputs is left to future work.
O An in-the-wild census of real MCP servers
The benchmark injects squatters into a cached corpus, and the live studies above use a handful of servers we config-
ured. Neither measures the noise of independently published tools, which sets the self distance and per-probe variance
a deployed verifier faces, so we measure it on real servers. We screened community servers from public registries by
publisher reputation, download count and keyless, read-only access, and pinned exact versions. We ran18distinct
servers over stdio JSON-RPC on an isolated host,7from the official reference collection (one of them since archived)
and11community servers. They span filesystem, version control, memory, SQL, time, web fetch and search, docu-
mentation lookup, literature search, weather, and format conversion. A read-only whitelist restricted probing, so no
state-mutating or destructive tool was called. Each whitelisted tool received schema-valid probes from the M1 genera-
tor, each executed three times to estimate a self distance, and every raw and canonicalized response, latency and status
was recorded for later drift replays.
Two servers failed to start without keys and were dropped, leaving16with probe data. Canonicalization succeeded
on every recorded response of all16servers, error and exception responses included, a success rate of1.00, so the
canonicalizer handles servers we did not author without curation. Parsing alone does not establish identity separation,
and the servers differ in self distance.
Table O.1 reports the split. Ten servers are deterministic under canonicalization, at a self distance of0.00over all three
passes. They are the filesystem, git, memory, SQLite, time, fetch and DuckDuckGo servers, two AWS documentation
and pricing servers, and the corrected reference server. Zero self distance over three passes is the deterministic special
case of the theorem’s setting, although it does not by itself establish independent observations or a positive margin.
Four servers are nondeterministic. A weather server’s air quality reading changes between calls (per-tool self distance
up to1.00, mean0.18over its six tools), the context7 documentation server’s search ranking varies (0.83to1.00), and
the arXiv server (0.13) and an AWS CDK construct search (0.20on one pass) also vary. These observations describe
theσ >0regime of Appendix F.1 and are not calibrated gate evaluations, since Theorem 2 applies only when its
sampling, candidate-set and threshold assumptions hold. Two further servers, a CLI echo harness with fault-injection
tools and a mindmap converter whose calls errored, produced only exceptions and are excluded from the split. Their
raw dumps are released. Their eight tools complete the59probed, beside35deterministic and16nondeterministic
ones. Of the35, ten answer every probe with an error, so for them determinism means a stable error response, which
does not by itself separate identities. We then replay the stored probes, re-issuing every recorded argument byte for
byte under canonical JSON, after24hours and again after22days. Canonicalization holds at1.00on both replays
32

ProbeIDPREPRINT
with all16servers reachable, and the probe arguments are verified identical tot 0 by hash. Drift is counted against
each tool’s ownt 0 noise. A tool that was deterministic att 0 has drifted if it moved at all, and a nondeterministic one
only if it moved beyond its own pass-to-pass distance. Counting any movement would flag12tools at24hours, of
which4drifted beyond their own noise and two more are measurement artifacts of the probe harness, set aside below.
At24hours,4of the59probed tools show genuine drift. Three belong to a legitimately time-varying weather server.
Its current conditions and detailed forecast move to distances1.00and0.53, and its air quality reading to0.25against
a0.07noise floor. The fourth, an AWS documentation recommender at0.10, was deterministic att 0, so its movement
is not pass-to-pass noise. From the logs we attribute it to the documentation service it queries, without an identified
cause. Two tools of the fault-injection harness excluded from Table O.1 also register0.50from this replay on, and we
set both aside because neither ever returned a response. Att 0 every call to them failed on a closed session, as at every
replay, so the0.50reflects which exception the dead session raised and says nothing about the tools. At22days the
service-side count is unchanged at the same4tools, but their magnitudes have grown, the AWS recommender moving
from0.10to0.54and the weather forecast from0.53to0.71. A registry-scale study of description drift over89days
reaches the complementary conclusion and names tool behavior as the surface its data cannot observe (Bharti, 2026).
The22-day replay also separates a second mechanism. Between the two replays four npm-installed servers had to
be reinstalled, and reinstalling them at their recorded version pins changed the behavior of three further tools, two
filesystem tools and one reference server tool, which moved to distances1.00,1.00and0.80. No top-level version
changed, and the recorded version of every one of the16servers is identical at the two replays. Every changed
response is a validation error string, rendered by a library that is not pinned. The SDK these servers build on declares
its schema validation library as a version range spanning two major versions, and the reinstall resolved it to4.4.3
(released lockfile). We did not snapshot the installed tree att 0, so which version it replaced is not recorded, and we
claim only that the same servers, reinstalled at the same recorded versions, answer differently. This is the failure
the threat model describes, arriving through the supply chain instead of the service. A pinned version does not pin
behavior, and a use-time behavioral check sees what the pin misses.
Nine further snapshots at25,27,34,41,48,55,62,69and77days, each taken with the same replay script, separate
the mechanisms by how they evolve over time. Across the ten replays from22days onward the same seven tools drift
once the harness artifacts are set aside, with canonicalization succeeding on every recorded response, all16servers
reachable, probe arguments verified identical tot 0 by hash, and every recorded server version identical tot 0 at every
snapshot. The three supply-chain tools stay at1.00,1.00and0.80in all ten, because nothing was reinstalled again.
The service side splits three ways rather than two. One tool holds a constant value throughout, the current-conditions
reading at the ceiling of1.00. Two oscillate inside a band without a trend, the weather forecast between0.48and0.71
and the air quality reading between0.23and0.29. The AWS recommender diverges progressively. It climbs from
0.10at one day through0.54,0.60,0.60,0.62,0.62and0.67to the ceiling of1.00at55days and holds that ceiling
at62,69and77days, a Spearman rank correlation with elapsed time of0.954over the ten replays from22days. The
correlation describes these ten points and is not a test, since they are one tool observed repeatedly rather than a sample.
The version pin showed no change. Its recorded version is the one fromt 0, its probe arguments are byte identical,
the server was reachable and canonicalized at1.00on every pass, and the two sibling tools on that server remain at
0.00. A supply-chain change is a step that happens once and then holds, while service-side behavior remains constant,
fluctuates within a band or diverges, and divergence is a reason to revalidate a tool against its admission reference,
although a refusal still depends on the chosen gate and its calibration.
At69days one more tool, the filesystem server’s listing of the directories it may access, moved to1.00because of
a change on the measurement host, not in the server. Between the62- and69-day replays a rename on the host left
a symbolic link on the path the server was configured with. The recorded launch command, working directory and
environment are identical tot 0, and the server now lists the resolved target of that link as a second allowed directory
beside the configured one, where it previously listed one. The seven tools of that server that read files and directories
stay at0.00, and the new listing persists at77days. We exclude this tool and the two harness tools above from every
drift count reported in this paper, so the census reports7drifting tools where its raw count at both69and77days is
10. A more sensitive use-time gate could escalate on this environmental change, while the fixed equality setting below
accepts it because its single probe leaves a vacuous threshold.
A fixed gate on the census.We retrospectively apply the agent study’s equality rule at a probe cap of32and
δ=0.05to the saved final replay. Each tool’s first two admission passes set its reference and self distance, and the
current endpoint is the sole candidate. The gate accepts55/59tools and refuses4/59across416probe calls. It
refuses three of the seven registry-side changes. Of the four accepted changes, three have just one recorded probe,
which makes the radius larger than the maximum possible equality distance. The fourth has a noisy self distance that
also makes its threshold vacuous. One overall refusal is a documented CLI timeout artifact. The remaining changes
33

ProbeIDPREPRINT
Table P.1:Verification cuts corrupted calls in four arms over16MCP-Bench tasks, ground truth by gold-server
replay. Corrupted calls are values the agent was given that the gold server would not have returned. With the verifier
they fall from93to20, and102calls are refused instead, at zero refusals in the benign arm. Each arm was run three
times, and the table reports the first, with the spread below.
arm agent calls replayed corrupted rate tainted refused
benign, no gate 1453 1388 0 0.000 0/16 0
benign, gate 1417 1347 0 0.000 0/16 0
rug pull, no gate 1575 1476 93 0.063 15/16 0
rug pull, gate 1323 1159 20 0.017 9/16 102
are not adjudicated attacks or independently labeled benign updates, so these decisions measure neither malicious-
replacement risk nor a false-alarm rate for legitimate updates.
P The agent study and residual failures
Setup.MCP-Bench (Wang et al., 2025a) runs an LLM agent over live MCP servers. We keep the16of its104tasks
that touch the four servers for which we hold a gold and a squatter, Math MCP, Unit Converter, Medical Calculator
and Scientific Computing. Four further tasks also touch BioMCP, which needs an API key we do not have, and a
task whose server cannot connect measures the broken connection instead of the arm, so we drop them and record the
omission. Agent and judge are both Qwen2.5-32B-Instruct-AWQ served at a65,536token context, decoding greedily
at temperature0with a fixed seed, which removes sampling as a source of difference between the arms without making
them identical. The two benign arms recorded1453and1417calls, neither with a corruption, since the serving stack is
not reproducible across runs even at temperature0, so the arms are paired by task and not by trajectory. Each squatter
replaces the gold binary behind an unchanged registry name, so the agent sees byte-identical tool cards, and the arms
differ in two environment variables.
Ground truth by gold replay.Every tool call is recorded with its arguments and re-issued against the gold server,
task by task on freshly started servers because several of these tools are stateful. A field the gold server does not
reproduce against itself cannot witness a corruption, so each task is replayed twice and any leaf that differs between
the two passes is excluded and logged. Image responses, which the harness renders as empty text and our parser as
a content descriptor, are counted as unadjudicable. The benign arms serve as the known-answer test. After volatile
leaves are masked and image responses excluded, every adjudicable benign call reproduces against the gold servers.
Table P.1 reports the arms. Taint is counted against the16tasks run, the denominator that makes the gated and ungated
arms comparable. The released replay for the gated rug pull carries adjudicable calls for only15of them, because on
the unit converter server the gate refused all seven calls the agent made to a server with a gold, so that task has nothing
left to adjudicate. Counting taint against those15would report0.60instead of9/16and would drop a task the gate
protected completely, so the released replay carries both denominators. The calls a row does not replay are calls to
Wikipedia, for which no gold is held, image responses that cannot be adjudicated, and the gate’s refusals,65 = 57 + 8
and70 = 62 + 8in the benign arms,99 = 89 + 10without the gate and164 = 52 + 10 + 102with it under the
rug pull. Replay masked a volatile request identifier in2,1,1and4of the1396,1355,1486and1169calls sent to
it, and the arms ran one after another, not in randomized order. All102refusals fall on the eight tools whose drift the
probes reach, with bmi_bsa_calculator32, mean23, convert_temperature11, round11, convert_force10, and5each
on convert_density, convert_speed and convert_mass. Verification cost135,111probe calls over the benign run across
269verdicts,502per verdict, and produced no false alarm. Four more verdicts fell on Wikipedia tools, which have no
attested bank and pass through the gate at zero probes, so an average over all logged verdicts gives495.
One coverage failure in two tools.Ten determinant calls and ten convert_batch calls remain corrupted under the
gate. Both tools sit at a measured distance of0.000, not just under a threshold. The determinant tool addresses a named
tensor, and a schema-driven probe invents a name that was never created, so gold and squatter both answer that it does
not exist. The convert_batch tool takes a nested array of request objects and the generator can draw only seven distinct
probes for it, none of which happens to exercise a drifted conversion category. In both cases the probe distribution
does not reach the drifted behavior, so the margin is zero and Theorem 1 gives no detection guarantee at any budget,
as the separability condition of Appendix D states. The budget matters for the other tools. In a run atm=32, Unit
Converter (realized margin0.13to0.18, requiring415to774probes) and Medical Calculator (0.093, requiring1576)
were also allowed. Raisingmto the full bank of512recovered both, including the two tools whose budget exceeds
512, because the budget is sufficient rather than necessary.
34

ProbeIDPREPRINT
Table P.2:Exact equality verifies deterministic drift at a fraction of the probe calls, end to end.Rug pull arm
over the same16tasks, one run each, them=512row being run 1 of Table P.1. Corrupted calls and tainted tasks
come from the gold replay, refusals from the call log and probe calls from the gate’s own log. Every gated row retains
the corruption of the stateful tensor tool and of the batch converter, whose probes never reach the drift, and the lower
structural budgets retain more.
per-probe comparisonmcorrupted tainted refused probe calls
no gate093 15/16 0 0
structurald Y 3235 13/16 31 8,398
structurald Y 12835 13/16 68 33,891
structurald Y 51220 9/16 102 126,428
exact equality3222 8/16 84 8,412
Full-bank use and adaptive exposure.The gate draws the entire attested bank at each verification. Against an
adversary that commits its mimicry region before observing the bank, testing every entry is at least as strong as testing
a subset. Full-bank use alone does not invalidate the committed-coverage argument. Reuse creates a different concern,
because an adversary that observes the queried inputs can learn the bank and adapt before later checks. That timing is
outside the guarantee. A larger bank with withheld probes can delay exposure, but does not establish security against
an adversary that learns and adapts to the deployed probes.
Reproducibility of the arms.Every arm was run three times end to end on freshly launched servers, and Table P.1
reports the first. The agent’s trajectory is not identical across runs even under greedy decoding, because tool responses
carry timestamps and the harness retries differently, so the number of adjudicable calls moves,1388/1372/1343be-
nign ungated,1476/1456/1471rug pulled ungated,1347/1361/1365benign gated, and1159/1154/1104rug pulled
gated. Task-taint counts do not move. Both benign arms are clean in all six of their runs, with zero corrupted calls and
zero refusals every time. The rug pull taints15of the16tasks in all three ungated runs and9in all three gated runs.
Corrupted calls track the trajectory rather than the verdict,93/90/92ungated against20/16/17gated, a reduction of
78to82%in the count of corrupted calls, with102/84/77calls refused. This records observed run-to-run variation,
not a population variance bound, with the agent model, judge and task subset held fixed. The gate’s budget and scorer
are varied below.
Paired task uncertainty.In each repeated run,6of the same16tasks change from observed taint to no observed taint
and0change in the reverse direction. The paired task-risk reduction is0.375, with a95%task-resampling interval
of[0.125,0.625]in each run. Repeats are not additional independent tasks. The interval conditions on the studied
servers, and absence of observed corruption does not establish correct final answers. The single-run comparison of
equality atm=32with structural distance atm=512differs by0.0625, with interval[0.0000,0.1875]. It supports the
observed lower probe cost without establishing superior task protection.
Budget and scorer.Apart from the server’s answers, the gate’s verdict is a function of the bank, the budget and the
subsample seed, so issuing each full bank once to the squatter and twice to the gold determines the verdict at every
budget and seed without running the agent. Derived this way, the verdict reproduces the distance, threshold and probe
count the gate logged for every tool in the gated arms, atm=512over three seeds and atm=32. Averaged over
200subsample seeds, the structural distance refuses2.00of the eight drifted tools the probes reach atm=32,3.49at
m=64,6.94atm=128and7.98atm=256, and all eight only at the full bank. Exact equality, calibrated the same
way from the two passes over the gold, refuses7.98atm=32and all eight fromm=64. Neither refuses a gold tool
at any budget. A drifted conversion changes one field of a multi-field response, so equality’s margin is0.65to0.88
on the unit conversions and0.37on bmi_bsa_calculator, four to five times the structural distance’s0.13to0.18and
0.093, and the budget of Theorem 1 falls with the square of that ratio. On deterministic tools the structural distance
has a smaller margin because it assigns partial credit, which keeps it continuous under noise (Appendix J.2).
Table P.2 runs the comparison end to end over the same tasks. The structural distance leaves35corrupted calls and
13/16tainted tasks atm=32and again atm=128, and only the full bank reaches20and9/16. Exact equality at
m=32leaves22and8/16for8,412probe calls against126,428, and what survives it in that run is the two tools the
probes cannot reach, ten determinant calls and twelve convert_batch calls. The benign arm of each configuration is
clean, no corrupted call and no refusal, so the lower-cost comparison detects drift without a false alarm here.
One fixed replacement setting.Atm=32with exact equality, the benign arm allows278/278probed verdicts
and makes10,300runtime tool calls, including8,846probes. The replacement arm allows237/266probed verdicts
35

ProbeIDPREPRINT
Table Q.1:Every observed rate respects its bound on the bank distribution.A cell is one tool, comparison and
budget, scored over1,000random draws. Premise cells are those where the stated condition holds for the bank means.
A violation is an observed rate on the wrong side of the bound.
structurald Y exact equality
bound premise cells violations cells violations
replacement refused, rate≥1−δ µ s −s >2ϵ 1 16 0 43 0
gold accepted, rate≥1−δ s≥µ g 539 0 539 0
joint wrong decision, rate≤δgold present,µ s > µg 56 0 56 0
gold returned, rate≥1−δ µ s −µ g ≥4ϵ 2,s≥µ g 6 0 27 0
and makes9,592runtime tool calls, including8,412probes and1,180business calls, while22/1,138adjudicable
calls remain corrupted. Recording the four trusted banks cost76,174calls. The later equality calibration issued
another76,174trusted calls, so the observed one-time setup cost was152,348calls. The benchmark spans11,402and
10,372seconds, respectively, excluding setup, model startup, and gold replay. These arms reused a scorer and budget
examined after earlier outcomes, and their agent trajectories differed, so they give a retrospective operating point, not
held-out replacement risk.
Limits of this study.Sixteen tasks are evaluated. Task success is1.000in all four arms, and mean judge-rated
completion is7.750and7.888in the benign ungated and gated arms against7.894and7.969in the rug-pull arms.
Agent and judge share a model, because an independent judge from another model family did not follow the rubric’s
0to10scale and returned per-task completion scores from7.9to93.5. Greedy decoding and a swapped judge mean
none of these scores is comparable to the published MCP-Bench leaderboard, and every comparison here is paired
within the study. The benchmark’s own judge is reported only to show what it misses, not as a claim about its quality
on the task it was built for.
Q Random probes from the attested banks
The benchmark’s cached probes are fixed, so they cannot test the probability statements of Section 4. The banks of
the agent study make such a test possible. Its gate recorded every entry of the attested bank of each of77tools on
four servers, twice from the gold server and once from the rug-pull server (Appendix P). The tools are stateless on
these entries, which Appendix P checks by reproducing every distance the live gate logged, so the recorded per-entry
distances determine the empirical distance of any probe subsample and the draws need no further tool calls. For
every tool and budgetm∈ {8,16,32,64,128,256,512}, withmcapped at the bank size, we draw1,000subsamples
uniformly without replacement and score each draw with both comparisons. The single-candidate gate accepts when
the mean distance is at mosts+ϵ 1, withϵ 1 =
p
log(2/δ)/(2m)and, as in the deployed gate,sthe admission self
distance for the structural distance and the mismatch between the two gold passes for equality. The two-candidate rule
of Algorithm 1 usesϵ 2 =
p
log(4/δ)/(2m),γ min = 2ϵ 2 andτ hi =s+ϵ 2. Every threshold follows fromδ=0.05,
and the rules, draw seeds and endpoints were fixed before the first draw. A tool counts as wrong when its squatter
corrupted at least one adjudicable agent call in an ungated run. Ten tools qualify. The bank reaches the drift of eight
of them, and the other two, determinant and convert_batch, agree with the gold on every bank entry.
The bank is the sampling population, so the bank meansµ g andµ s of the gold and squatter distances are exact
expectations under the bank distribution, and each bound’s premise can be checked per tool, comparison and budget.
Table Q.1 counts the cells where a premise holds and the observed rate falls on the wrong side of its bound. There are
none, raw or beyond three Monte Carlo standard errors.
Table Q.2 gives the replacement setting tool by tool. Equality’s margin on the conversions and on bmi_bsa_calculator
is four to five times the structural distance’s, because a drifted conversion changes one field of a multi-field response,
and the refusal budget falls accordingly. Averaged over the eight reachable tools, equality accepts a replacement at
0.154atm=8and0.006atm=32and never fromm=64. The structural distance accepts at0.750atm=32and
0.135atm=128, still accepts bmi_bsa_calculator at0.060atm=256, and accepts none atm=512. Under either
comparison, no draw at any budget refuses a gold or any of the67unaffected tools, whose rug-pull server matches
the gold on every bank entry and corrupted no agent call, so no benign check is lost at these thresholds. The two
unreachable tools pass at every budget. Their margin on the bank distribution is zero, so the theorem makes no claim
about them, and their harm lies on the agent’s inputs outside the bank.
36

ProbeIDPREPRINT
Table Q.2:Acceptance of a replacement with the gold absent, the fraction of1,000random bank draws on which
the single-candidate gate accepts the rug-pull squatter, for the ten tools whose squatter corrupted agent calls. Margins
are the squatter’s bank mean distance. The last two tools match the gold on every bank entry.
margin structurald Y atmexact equality atm
toold Y equality 32 128 256 512 8 16 32 64
mean 0.941 0.941 0.000 0.000 0.000 0.000 0.000 0.000 0.000 0.000
round 0.465 0.465 0.003 0.000 0.000 0.000 0.460 0.184 0.003 0.000
bmi_bsa_calculator 0.093 0.371 1.000 0.997 0.060 0.000 0.651 0.435 0.046 0.000
convert_density 0.177 0.883 1.000 0.000 0.000 0.000 0.001 0.000 0.000 0.000
convert_force 0.163 0.814 1.000 0.000 0.000 0.000 0.008 0.000 0.000 0.000
convert_mass 0.129 0.646 1.000 0.085 0.000 0.000 0.103 0.009 0.000 0.000
convert_speed 0.162 0.809 1.000 0.000 0.000 0.000 0.005 0.000 0.000 0.000
convert_temperature 0.168 0.838 1.000 0.000 0.000 0.000 0.005 0.000 0.000 0.000
determinant 0.000 0.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000
convert_batch 0.000 0.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000 1.000
With the gold present, no draw returns the squatter for any of the ten tools, and on the two unreachable tools every
draw abstains because gold and squatter tie. The fraction of draws that return the gold for the eight reachable tools
is0.606,0.784and0.934for equality atm=16,32and64and reaches1.000bym=256. For the structural distance
it is0.250fromm=128to256and0.750atm=512, because four conversions’ margins clear2ϵ 2 only at the full
bank, while convert_mass at0.129and bmi_bsa_calculator at0.093never do. These tools are deterministic, so a
gold at distance zero cannot be undercut, and the zero wrong-return rate with the gold present follows from that. The
informative quantities are the observed replacement acceptance, whose refusal the theory guarantees only where the
margin exceeds2ϵ 1, and the absence of false refusals.
A rule that accepts every server is right on the67unaffected tools and wrong on all ten replacements, a tool-level
accuracy of0.870. In expectation over draws, equality is right on0.958of tools atm=8and0.973atm=32, and
the structural distance on0.890and0.896, reaching0.974only atm=512. No gate that accepts every server whose
answers match the reference can exceed that value on these banks, because the two unreachable replacements match
the gold on every entry. A single-candidate check issuesmin(m, B)probe calls and a two-candidate check twice
that. Recording the four banks took76,174tool calls, and the equality self-distance calibration another76,174(Ap-
pendix P). The banks were recorded for the agent study, so this is a validation on the bank distributions of four servers
rather than on held-out servers, and it says nothing about inputs outside the banks, which is where the two unreachable
tools do their harm.
R A prospective held-out study
The draws of Appendix Q reuse banks that the agent study recorded on servers it had already used, so we also ran
a prospective study. Its rules, its endpoints and the code of seven replacement policies, including the salt of their
triggers, were fixed before any bank was drawn, and the sharper gates of Appendix S were added only afterwards. The
study covers the38read-only tools of eight census servers (Appendix O), the MCP reference server, an echo server
and the time, memory, SQLite, git, filesystem and weather servers, and leaves out one tool that sleeps by design and
one that returns base64 media. Each tool’s bank holdsBindependent draws from the agent study’s schema-driven
generator, with repeats kept so that the bank is an i.i.d. sample of the input distribution. Paths, time zones, cities, entity
and table names and branch types come from typed pools of which10to30%of draws are invalid or unknown. File
paths are drawn from the seven workspace files and four directories, with15%missing paths and10%paths outside
the workspace. Time zones come from30IANA names and cities from30names, each with10%invalid or invented
values. Memory queries and entity names come from the fixture graph with30%and20%random words, table names
from the two tables with30%random names, repository paths with10%subdirectories and10%missing paths, and
branch types from local, remote and all with10%random strings. Other fields take the generator’s typed values. The
bank holdsB=512calls for the local servers and96for weather, which queries a public weather service at one call
per second, and its seed was read from the operating system only after the design was fixed. Every bank was answered
three times on freshly started servers, first as the reference, then as the admission pass that fixes the self distances,
and last as the later check of the unchanged server, which plays the gold.
Each replacement is one of the fixed policies applied to the gold’s answers. Value drift perturbs every scalar leaf of
an answer, adding1to4to an integer and0.5to2to a real, appending a suffix to a string and flipping a boolean,
37

ProbeIDPREPRINT
Table R.1:No observed rate breaks its bound in the held-out study.Cells are tool, candidate, comparison and
budget for the fixed rules, and tool, candidate, comparison and resolution for the sequential rules, over all38tools, the
gold and the seven policies. Premises are checked on the bank means. A violation is an observed rate on the wrong
side of the bound.
structurald Y exact equality
rule bound premise cells violations cells violations
fixed accept, rate≥1−δ µ≤s879 0 936 0
fixed refuse, rate≥1−δ µ−s >2ϵ 1 586 0 615 0
fixed joint wrong decision, rate≤δ µ > µ g 1153 0 1096 0
fixed gold returned, rate≥1−δ µ−µ g ≥4ϵ 2,s≥µ g 272 0 313 0
sequential refuse, rate≤δ µ≤s262 0 280 0
sequential accept, rate≤δ µ > s+γ res 256 0 242 0
sequential joint wrong decision, rate≤δ µ > µ g 173 0 164 0
on the inputs that a salted hash of the call selects with probabilityϕ∈ {1,0.25,0.05}. Field drift removes the first
field of every mapping answer and falls back to value drift on other answers. Three legitimate updates add a field to
every mapping answer, reword error messages, or write integers as floats in reversed key order, which canonicalization
removes. The rules and thresholds are those of Appendix Q and Proposition 1 atδ=0.05, scored over1,000draws
per tool. Eight tools have fewer than16distinct inputs in their banks, input-free tools among them, and are reported
separately because every draw repeats the same few calls. Of the other30,22are local and8belong to the time and
weather servers, whose answers depend on the clock or on live weather data. The local tools are deterministic across
restarts except for an echo tool whose response carries a timestamp the canonicalizer does not name, which sets its
self distance to0.25underd Y and to1under equality.
No observed rate breaks its bound in any of the7,227premise cells, and the two-candidate rules never return a
replacement with the gold present (Table R.1). The remaining outcomes depend on the margin. Every candidate
whose bank marginµ−sexceeds0.2,117tool and candidate cells on37tools underd Y and113on33under equality,
is refused on every draw by the fixed gate at the full bank and by the sequential gate at both resolutions. No gold is
refused at the full bank, and at smaller budgets at most0.1%of gold draws are. On the local tools, full value drift and
field drift are refused on all22tools underd Y , and the sequential gate reaches that verdict after8and14probe calls on
average, where the fixed gate spends512(Table R.2). Equality accepts every drift policy on the echo tool whose self
distance is1, because its threshold then admits any candidate, whiled Y refuses them. Drift on one input in twenty is
refused on8of the22local tools and accepted on the other14, whosed Y margins lie between0.004and0.053, inside
the resolution that Proposition 1 leaves open.
The time and weather tools show the cost of noise. Five of the six weather tools answer differently on most repeated
calls, at self distances up to0.91underd Y , and the remaining margin of a replacement shrinks accordingly. On the
noisiest, full value drift changes every answer, yets+ϵ 1 exceeds the largest possible distance atB=96, so the fixed
gate accepts it on every draw. The sequential gate reports those checks as inconclusive instead, because neither of its
tests can pass. A call to the weather service takes a median of1.6to1.7seconds, so a full-bank check of such a tool
takes about4.2minutes, while local calls return in about a millisecond and a full-bank check takes0.66seconds.
The legitimate updates measure revalidation cost. The format change leaves every per-entry distance equal to the
gold’s and is accepted wherever the gold is. Reworded error messages are refused on all16tools whose answers they
change. An added field is refused on5of the7local tools it touches underd Y , and passes on two file readers where
it alters about one answer in a hundred. Such refusals are the intended behavior of a behavioral reference, which a
deployer answers by recording a new one.
The replacements are fixed transformations of genuine answers rather than independent attackers, and the servers are
open reference implementations. For the local servers the check followed admission by22to23seconds, so the study
does not measure slow drift of an unchanged local server. It tests the stated rules on banks and replacement policies
that were fixed in advance, and it does not estimate how often replacements in the wild fall inside the resolution.
S Exact and finite-population gates
The Hoeffding radius behind every gate above is conservative in two ways. It ignores that probes are drawn without
replacement from a finite bank, so it stays positive when the whole bank is read, and on the equality channel it ignores
that the per-probe score is a Bernoulli indicator. We also score two sharper rules on the same draws and permutations
38

ProbeIDPREPRINT
Table R.2:Held-out outcomes by candidate, averaged over tools with at least16distinct inputs. Changed counts the
tools on which the policy alters at least one answer. Fixed is the acceptance rate of the single-candidate gate at the full
bank, sequential its acceptance rate atγ res=0.2with the mean number of probe calls per check.
structurald Y exact equality
candidate changed fixed sequential calls fixed sequential calls
22local tools
gold (unchanged server) – 1.000 1.000 128 1.000 1.000 128
value drift,ϕ=122 0.000 0.000 8 0.045 0.045 14
value drift,ϕ=0.2522 0.000 0.011 82 0.045 0.056 80
value drift,ϕ=0.0522 0.636 0.744 163 0.636 0.744 163
field drift 22 0.000 0.000 14 0.045 0.045 14
added field 7 0.773 0.773 115 0.818 0.818 106
reworded errors 12 0.455 0.500 90 0.455 0.500 90
format only 0 1.000 1.000 128 1.000 1.000 128
8time and weather tools
gold (unchanged server) – 1.000 1.000 95 1.000 1.000 90
value drift,ϕ=18 0.125 0.000 23 0.250 0.125 82
value drift,ϕ=0.258 0.500 0.126 86 0.750 0.509 99
value drift,ϕ=0.058 0.875 0.750 124 0.875 0.875 107
field drift 8 0.250 0.080 91 0.250 0.125 82
added field 6 0.375 0.250 112 0.750 0.502 69
reworded errors 4 0.500 0.580 118 0.500 0.625 110
format only 0 1.000 1.000 95 1.000 1.000 90
as Appendices Q and R, at the sameδ=0.05without parameter tuning. They were chosen once the results of those
appendices were known, so they are reported alongside, without replacing, the original rules. The exact equality gate
refuses whenPr(X≥x)≤δ, wherexcounts the mismatching entries among themdrawn andXis hypergeometric
with populationB,⌊sB⌋successes andmdraws. The finite-population radius isr(m, q) =
p
ρm log(q/δ)/(2m)
withρ m = 1−(m−1)/Bform≤B/2andρ m = (1−m/B)(1 + 1/m)otherwise (Bardenet & Maillard, 2015,
Corollary 2.5), which is zero atm=B. It usesq=1for the fixed single-candidate gate,q=4for Algorithm 1 with two
candidates,q=2Jfor the single-candidate sequential gate andq=4Jfor the sequential two-candidate rule.
Proposition 3(Sharper gates).Condition on a fixed bank of per-entry scores and the admission values. If a can-
didate’s bank mean is at mosts, the exact equality gate refuses it with probability at mostδ. With these radii, each
single-candidate error statement of Appendix C holds separately, Proposition 1 holds, and part(i)of Theorem 2 holds
for two candidates.
For a fixed observed countx, the hypergeometric upper tail is nondecreasing in the number of mismatching entries,
so⌊sB⌋is least favorable under a bank mean of at mosts, and the rejection probability is at mostδ, often strictly
smaller. The proofs of the other statements use only a one-sided deviation bound for each sample mean and a union
bound, and Corollary 2.5 of Bardenet & Maillard (2015) provides that bound for sampling without replacement, for
the sample mean and, applied to the negated scores, for its lower deviation.■
No observed rate breaks its checked bound in any of the3,848premise cells on the agent banks or the8,547on the
held-out study, again an implementation check rather than evidence about the tools. Table S.1 gives the agent banks.
The exact equality gate accepts a reachable replacement at0.004atm=8against0.154for the Hoeffding gate, with
no recorded acceptance fromm=32rather thanm=64. It refuses golds and unaffected tools in at most3.2%of draws,
withinδ, whereas the Hoeffding gate refuses none. The finite-population radius barely changes the structural distance
at small budgets, whereρ m is close to one, but no recorded draw accepts a reachable replacement fromm=256rather
thanm=512. With the gold present, the finite-population pair rule, which abstains on equal distances as the radius
reaches zero, returns the gold on0.798of draws atm=256and on every draw atm=512, against0.250and0.750for
the Hoeffding rule.
On the held-out study the full bank is read, so the finite-population radius is zero and the gate refuses any candidate
whose bank mean exceedss. This removes sampling error within the bank but says nothing about inputs outside it.
Every tested malicious replacement with a positive bank margin is then refused, including drift on one input in twenty,
which the Hoeffding gate accepted on14of the22local tools, and full value drift on the noisiest weather tool. No gold
is refused at the full bank under either sharper rule, and at smaller budgets at most4.7%of gold draws are refused by
the exact gate and0.8%under the finite-population radius. The cost is refusal of legitimate updates. At the full bank
39

ProbeIDPREPRINT
Table S.1:Sharper gates halve the observed refusal budget on the agent banks.Acceptance of a reachable rug-pull
replacement with the gold absent, averaged over the eight reachable tools, and the rate at which the pair rule returns
the gold with it present, over1,000paired draws per budget. Values are rounded, so a printed zero need not mean zero
acceptances. The sharper rules were added after the Hoeffding results were known.
equality, gold absent structurald Y , gold absentd Y , gold returned
mHoeffding exact Hoeffding finite pop. Hoeffding finite pop.
8 0.154 0.004 0.807 0.807 0.000 0.000
16 0.079 0.000 0.773 0.760 0.128 0.128
32 0.006 0.000 0.750 0.750 0.158 0.158
64 0.000 0.000 0.552 0.238 0.244 0.247
128 0.000 0.000 0.135 0.075 0.250 0.250
256 0.000 0.000 0.007 0.000 0.250 0.798
512 0.000 0.000 0.000 0.000 0.750 1.000
Table T.1:Study conclusions depend on the decision rule.Forced choice treats a gold tie as a miss. Gated selection
uses Algorithm 1. The single-candidate gate accepts distance at mostτ hi (Appendix C). The gated thresholds0.5
and0.05are fixed defaults of the released configuration, not derived from the theory, and the twin family uses0.6.
Appendix K.3 scores the theory-calibrated radius on the cached cases. The sequential gate also accepts onced(j) +ϵj ≤
s+γ res, and its paired form uses the gap2ϵ j.
study ruleτ hi γmin
Tables J.1, H.1 and H.2 (ProbeID and judge view; the judges ab-
stain on 0), J.2, L.1, L.2, L.3 (sloppy and faithful); Figures 2(c),
I.1, K.1; Appendices J.1, K.2
forced choice – –
Tables G.1, G.2, I.2, I.3, L.3 (twin), M.1, M.2; sibling groups gated0.5 0.05
Table I.1 gated0.6 0.05
Table N.1 margin≥γ min –0.05
Appendix K.3 calibrated, swept – –
Tables P.1, P.2; census gate (Appendix O) one-sided gate self dist.+ϵ–
Table 1 (bank rows, gold absent or alone), Q.2, Q.1, R.1, R.2
(fixed); Figure 2(d)
one-sided gates+ϵ 1 –
Table 1 (bank row, gold present), Q.1, R.1 Algorithm 1s+ϵ 2 2ϵ2
Tables R.1, R.2 (sequential); Proposition 1 sequential gates+ϵ j –
Table S.1 (equality, gold absent); Appendix S exact test hypergeometric –
Table S.1 (dY , gold absent) one-sided gates+r–
Table S.1 (dY , gold present) pair rules+r2r
the finite-population structural gate refuses every answer-changing legitimate update tested, including an added field
on all7local tools it touches rather than5. The sharper rules also make the admission estimatesbinding. Reading
the whole bank, the gate refuses a gold whose bank mean exceeds that estimate by any amount, which none of the
held-out golds did, but their checks followed admission by minutes at most.
T Implementation and reproducibility
On the cached benchmark, identity verification is inference only and deterministic given the saved responses and the
probe seed. The benchmark backend is the StableToolBench response cache. The recursive loader admits a tool when
it exposes at least four structured cached responses, parsing argument keys with a safe literal evaluator and skipping
binary or empty payloads, and the pool of Table J.1 contains every admitted tool matched to a ToolBench description,
402tools. For each registry seed,41,42and43, the pool is shuffled and golds are taken in that order until150are kept,
300for Appendices H and J.2. A case is kept only when at least one of its squatters is behaviorally separable from the
gold, so hit@1 is conditional on that event. Reaching150golds per seed drew462golds over the three seeds atk=1
and451at everykfrom2to64, so12and1were excluded. Every gold excluded atk=1returns canonical responses
holding no value a mutation changes, and every gold kept holds one. On this 150-gold cohort, counting the excluded
golds as misses lowers ProbeID from1.000to0.974atk=1and from0.956to0.953fork≥2. The300-gold studies
drew929golds atk=1and903fork≥2. A gold’s probes are its first12cached argument and response pairs in cache
order, fewer when the cache holds fewer. Squatterjtakes the family at positionjof the ordered pair (output value
drift, silent field drift). Output value drift perturbs every scalar leaf, negating a boolean, adding a uniform integer from
40

ProbeIDPREPRINT
1to4or a uniform real from0.5to2.0, and appending a suffix to a string. Silent field drift deletes the first key of a
mapping response in sorted order, and falls back to output value drift when the response is not a nonempty mapping.
Mutations, probe order and seeds are fixed in code, the gated studies use the code’s default thresholds, no development
split was held out, and Table T.1 lists the decision rule behind each study. The cached identity results average three
registry seeds, and a gold can recur across them. Atk=8the450case-runs of Table J.1 are307distinct golds,99of
them in two seeds and22in all three. Resampling golds, each with all its case-runs, instead of case-runs leaves the
gap over BM25 at0.844and moves its95%interval from[0.809,0.878]to[0.807,0.880]. The bounded behavioral
distance, the identity rule, and the guarantee check are released with the benchmark, together with the per-case hit
vectors and the paired bootstrap output behind the headline confidence intervals. The live study uses a stdio MCP
client backend that implements the same interface as the cached backend, with the official everything server as gold
and a small squatter server, both released. The ProbeID code is released under the MIT license, and the benchmark
builds on StableToolBench and ToolBench, both under the Apache-2.0 license. Code, derived data and the full raw
response corpus will be released upon acceptance.
Cost.The protocol reads the reference from its attested bank. With the full budgetm=12and one gold plusk
squatters,m(k+1)is a cap of24,60, and108candidate calls atk∈ {1,4,8}. Fewer cached probes lower the observed
number of candidate-response comparisons. The savedk=8cases average87.64comparisons, which are not measured
live calls. A variant that also queried the trusted reference live would add anothermcalls. The behavioral judge
receives the same probes with each response cut to200characters and makes one LLM request per selection, while
description routers issue no selection-time tool calls. The cached benchmark sweep, covering 150 gold,k∈ {1,4,8},
three seeds, and four selectors, takes18.8seconds on one CPU core. That wall time excludes live tool latency and
cannot establish end-to-end speed. Per-case distances and threshold sweeps are retained alongside the benchmark.
The deterministic dilution cells have no trial denominator.
41
