---
title: 'COVER: Identifiable Evaluation of Coalition Routing'
url: https://arxiv.org/abs/2608.28475
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Raghul Sugumar
- Amrit Gopinath
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.28475
pages: 17
chars: 61938
fetched_at: '2026-11-08T13:33:21+00:00'
kb_version: 1
---

# COVER: Identifiable Evaluation of Coalition Routing

Preprint
COVER: IDENTIFIABLEEVALUATION OFCOALITION
ROUTING
Raghul Sugumar Amrit Gopinath
Sri Sivasubramaniya Nadar College of Engineering
ABSTRACT
When a multi-agent system changes its team, it also changes the messages and
final answer it produces, so an end-to-end accuracy gap does not by itself identify
a routing effect. We introduce COVER, an evaluation contract that fixes a public
information boundary, downstream stack G, and finite legal team family before
outcomes are generated. Complete coverage identifies exactfinite-benchmark
oracle regret conditional on that stack. For any finite collection of frozen policies,
executing the union of their distinct selected teams is the minimal assumption-
free support for every pairwise policy contrast, though not for absolute oracle
regret. Two controlled tables with source-ID-disjoint splits test the instrument.
On MuSiQue-12, a pre-specifiedprivileged positive controlimproves regret from
0.532 to 0.402; a later public-interface control reaches 0.424 versus 0.554 but is
retrospective. On HotpotQA-4, a pre-specified public direct scorer improves regret
from 0.313 to 0.110. In fixed-stack Llama execution, verified route regret improves
by 0.190, while the raw-answer gain is 0.010 with an interval crossing zero. A
five-family ToolSandbox variant-shift validation exhaustively evaluates 16 declared
teams on 14 untouched task variants (224/224 valid rows): the declared-family
oracle reaches 0.768 safe-evidence completion, while the prospectively frozen
router gets 0.637 (regret 0.131), failing the predeclared 0.10 criterion. A later
retrospective comparator reaches 0.655, matching all-workers with 4.57 versus
5.00 workers on average. Thus COVER exposes selection headroom without
manufacturing a routing win. A crossed-stack diagnostic shows absolute scores
depend on G but finds no detectable router-by-finalizer interaction. COVER is an
auditable measurement methodology, not a claim of stack-invariant or universal
agent-routing superiority.
1 THE PROBLEM IN ONE PICTURE
Suppose two multi-agent systems choose different workers for the same question. If one answers
correctly more often, was itsselectionbetter? Not necessarily: changing a team also changes private
messages and can change how a finalizer synthesizes them. This is the basic confound in routing
evaluation.
Public task
and capability cards
Frozen router
selects teamS
Selected workers see
private evidence
Fixed stackG
records valuey G x,S
Repeat for every legalS∈ F x;
then compare all routers on thesametable.
Figure 1: COVER changes only the selected coalition. Orange information is unavailable when the
route is chosen.
COVER makes the counterfactual explicit. For a task x, let Ax be its workers, Fx ⊆2 Ax its legal
teams, and G the frozen stack comprising public/private timing, workers, message order, prompt and
token policy, finalizer, judge, and utility. Let yG x,S ∈[0,1] be the outcome of executing exactly S
1
arXiv:2608.28475v1  [cs.AI]  28 Aug 2026

Preprint
underG. We call
V bench,G x (S) :=y G x,S,R bench,G(r) = 1 |D| X x∈D  max S∈Fx yG x,S −y G x,r(x)  (1)
the finite-benchmark value and regret of router r under G. Lower regret is better. Exactness is
within-stack: it neither asserts that team rankings are invariant to replacing G nor identifies stochastic
deployment utility. The latter, V pop,G x (S) =E ω[yG x,S,ω], requires repeated executions and is not
identified by one provider call.
If two systems change their workers or finalizer as well as their route, the selection contrast is not
identified: the same observed answers are compatible with a routing effect or with no routing effect
and a changed downstream pipeline. In contrast, when all legal teams are observed under one fixed
protocol, Equation 1 is a table lookup—no model of unseen coalitions is needed. If teams are missing,
one may report sampled-action regret, but not an exact oracle claim without additional assumptions.
The complete-table lookup is not itself the theoretical contribution. The substantive design question
is how much intervention support is necessary when full enumeration is unaffordable. COVER
gives a sharp answer for frozen-policy comparison: the route union is minimal for relative contrasts,
whereas the complete family is required for assumption-free absolute oracle regret. The experiments
instantiate both regimes and show when confusing them changes a conclusion.
What we contribute.We contribute (i) a stack-conditional evaluation contract and a minimal-
support theorem separating absolute oracle regret from relative frozen-policy comparison; (ii) two
controlled tables with source-ID-disjoint train/development/held-out splits; (iii) a fixed-stack execu-
tion decomposition; and (iv) a natural heterogeneous-tool validation that succeeds as a measurement
while rejecting its frozen routing headline. COVER is a methodology paper. The routers are validation
instruments, not a new universal architecture.
Reader’s guide.The main narrative is deliberately linear: Section 3 identifies the estimand;
Section 4 evaluates two complete controlled tables; Section 5 decomposes execution under one
fixed stack; and Section 6 tests the endpoint in ToolSandbox. All other experiments are visibly
supplemental.
2 RELATED WORK:WHATCOVERIS AND IS NOT
Model routers choose a complete model or scaffold using preference, similarity, or confidence (Ong
et al., 2024). Multi-agent systems additionally choose roles, communication paths, and workers (Wu
et al., 2023; Du et al., 2023; Wang et al., 2024). Their usual end-to-end comparison is valuable for
product evaluation, but it need not answer the narrower question of coalition-selection quality under
a common downstream protocol.
A contemporary post-audit example, Pandora’s Router, asks whether the expected benefit of pur-
chasing a more accurate specialist-value estimate justifies its inspection cost (Fisch et al., 2026).
Pandora optimizes information acquisition and specialist allocation; COVER instead asks what
coalition-selection contrast is identified once the information boundary and downstream stack are
declared. Pandora v2 postdates the audit freeze and is therefore cited here without altering the frozen
30-paper counts.
A targeted audit of what “routing” denotes.A frozen, purposive, non-systematic audit of 30
recent papers documents within this sample that “routing” spans joint-system design, communication
topology, sequential policies, and team selection. These are different estimands, not a catalogue of
invalid work. The coding rules, counts, single-coder limitation, and full paper-level table are confined
to Appendix F. COVER targets the narrower case of a declared finite coalition family under one
common downstream protocol.
Set encoders, submodular selection, DPPs, and correlation clustering provide useful mechanisms for
scoring groups (Zaheer et al., 2017; Lee et al., 2019; Kulesza & Taskar, 2012; Bansal et al., 2004).
We use them only as validation-policy ingredients. COVER does not claim a new attention primitive,
set-function class, or optimizer. Its target is instead the quantity a routing experiment has identified.
2

Preprint
Finally, factorial and off-policy methods estimate contrasts for actions that are not all observed (Das-
gupta et al., 2015; Rebello et al., 2023; Shimizu et al., 2024). COVER occupies the complementary
regime: a small, declared action family can be executed completely. This costs more up front, but
makes the finite benchmark oracle observable rather than estimated under a surrogate model.
ToolLLM retrieves candidate APIs before use (Qin et al., 2024), while DyLAN performs preliminary
team optimization before task solving (Liu et al., 2023). Our natural-study comparators adapt these
two selection ideas to a frozen finite coalition table. They are deliberately labeled “ToolBench-style”
and “DyLAN-style”: table lookup cannot reproduce either published system’s training, prompting, or
execution stack, and we do not present the adaptations as head-to-head replications.
3 THE EVALUATION CONTRACT
For every task, a valid COVER comparison fixes five things:
1.Action space.Declare which teams are legal before outcomes are generated.
2. Information boundary.The router receives task text and public cards; evidence, answers,
required-team labels, and outcomes stay hidden.
3. Downstream protocol.Workers, ordering, communication, utility, and finalizer are identical
across routers.
4. Coverage.Execute every legal team for absolute oracle regret, or the declared route union for
relative frozen-policy contrasts.
5. Inference.Freeze routers before held-out comparison and resample tasks, not correlated worker
pairs, for uncertainty.
This contract is complementary to off-policy evaluation and learned surrogate approaches: those
extrapolate to unobserved actions under assumptions; we instead evaluate a small declared action
space completely. It is also different from model routing, which typically chooses a single model or a
full scaffold rather than a coalition of evidence workers (Ong et al., 2024; Zaheer et al., 2017; Lee
et al., 2019).
3.1 IDENTIFICATION HIERARCHY AND MINIMAL SUPPORT
The distinction between a table and a deployment distribution matters. Let Ox ⊆ Fx be the teams
that were actually executed under G and let mG x = maxS∈Ox yG x,S. If values lie in [0,1] , then for any
router whose chosen team was observed,
mG x −y G x,r(x) ≤ Rbench,G x (r)≤1−y G x,r(x).(2)
If Ox ⊊F x, both endpoints are attainable by finite tables that agree on every observed outcome:
assign every unseen team a value at most mG x for the lower endpoint, or assign one unseen team
value one for the upper endpoint. When Ox =F x, regret is exactly mG x −y G x,r(x). Thus complete
coverage is the generic route to exact benchmark regret under the declared G; with partial coverage,
the only assumption-free exception is saturation at mG x = 1. Structural, smoothness, or generative
assumptions can support estimates with partial coverage, but should be reported as such.
Absolute regret is not always the required target. Let R={r 1, . . . , rK} be frozen policies evaluated
under the same G, and let Ax(R) ={r k(x) : 1≤k≤K} be their distinct selected teams on task x.
Theorem 1(Minimal support for frozen-policy comparison).Suppose finite outcomes are otherwise
unrestricted in[0,1]. If|A x(R)| ≥2, every pairwise contrast
∆G x (ri, rj) =y G x,ri(x) −y G x,rj (x)
is point-identified from execution support Ox if and only if Ax(R)⊆O x. Consequently, the per-task
route union is the unique inclusion-minimal assumption-free design for all pairwise contrasts and
requires exactly |Ax(R)| executions. If all policies select the same team, every contrast is identically
zero without execution. In neither case does relative identification recover absolute oracle regret
unless the oracle is otherwise identified.
3

Preprint
Table 1: Information visible at each point in a COVER evaluation.
Stage Available Deliberately unavailable
Route selection task text, public cards, declared budget private evidence, answers, outcome table,
required team
Worker execution selected worker’s private evidence other workers’ private evidence
Finalization canonical selected messages router identity and unselected messages
Offline scoring frozen table values and route files any held-out training outcome
Table 2: COVER’s compute/identification regimes. Costs are interventions per task; only the first
regime identifies absolute finite-benchmark oracle regret.
Coverage regime Interventions/task Identified quantity
Complete finite family all legal teams exact finite-benchmark oracle regret
Precommitted sampled family declared sampled teams sampled-action regret or bounds, not an oracle
Frozen route union distinct selected teams all pairwise policy contrasts; inclusion-minimal
Sufficiency is direct lookup. For necessity, omit any selected team and two bounded tables can agree
on every observed intervention while assigning different values to that team, changing at least one
contrast with a policy selecting another team. The taskwise result also identifies averages, win/tie/loss
counts, and policy rankings over a fixed evaluation set. Appendix A gives the full proof and separates
this result from moving-stack comparisons.
For genuine execution, full coverage is usually too expensive. Theorem 1 justifies executing the
deduplicated union of teams selected by the frozen policies under one protocol. This design identifies
their paired differences with no model for unexecuted teams while making no execution-oracle claim.
It is the estimand used below.
4 TWO CONTROLLED INTERVENTION TABLES
We instantiate the contract twice in multi-hop QA. The task and public cards are visible to a router;
each selected worker receives only its own private evidence; a fixed symbolic finalizer scores
whether the construction-defined required evidence is present. Source IDs are disjoint across train,
development, and held-out sets. A streaming audit confirms exactly one positive team per held-out
task in both binary tables (300/300 HotpotQA tasks and 500/500 MuSiQue tasks). Exhaustive regret
is therefore exact for these constructed tables, but the outcome is a controlled evidence-selection
measurement, not natural team utility or a claim about unrestricted agents.
4.1 POLICIES ARE VALIDATION INSTRUMENTS
UNIFIED-COVER is a permutation-invariant direct scorer. It encodes the task and public cards
with a frozen sentence encoder, forms task-conditioned card states using multiplicative and distance
features, pools both the full worker set and a proposed team, and scores the team with a small MLP.
It is trained on observed training-coalition outcomes using regression, ranking, and best-team losses.
No positional worker identifier is provided.
PARTITION-COVER is intentionally different. It ranks a triple using a fixed local compatibility
proxy and the quality of its best balanced partition completion, computed exactly by bitmask dynamic
programming. Its pre-specified MuSiQue interface is trained on train-only latent component labels.
We therefore classify it as aprivileged positive control, not a candidate deployment router: conditional
on the same privileged interface, the matched graph contrast asks only whether the table detects
structured global completion. A separate public interface learns compatibility from public text and
training intervention outcomes; that control is closer to deployment, but retrospective.
4

Preprint
Table 3: The two intervention-complete controlled instances. A task, rather than a card pair or
intervention, is the unit of inference.
Instance Held-out tasks Legal teams/task Construction purpose
MuSiQue-12 500 220 size-three teams Tests globally coherent components amid distrac-
tor components
HotpotQA-4 300 4 size-three teams Tests direct team scoring without a partition de-
coder
Table 4: Controlled findings and their evidential status. Regret is exact over each declared offline
family conditional on its frozen stack; exact scoring does not make a privileged policy deployable or
a retrospective policy confirmatory.
Study Tasks Result Interpretation
MuSiQue-12 public 500 0.424 vs 0.554 Deployment-relevant public interface; retrospective
control
MuSiQue-12 privileged 500 0.402 vs 0.532 Pre-specified positive control of instrument sensitivity
HotpotQA-4 300 0.110 vs 0.313 Direct set scoring is a useful bias in a four-way deci-
sion
4.2 PRE-SPECIFIED ANALYSIS
The original confirmatory family comprises the MuSiQue privileged positive-control contrast, the
HotpotQA public-interface comparison, and the Llama verified-evidence execution endpoint. We
use paired task bootstrap intervals, two-sided sign-flip tests, and Holm correction within that family.
“Confirmatory” here describes the frozen test, not deployment validity: the MuSiQue contrast confirms
instrument sensitivity conditional on privileged supervision. ToolSandbox is a later natural validation.
All other endpoints, controls, scale studies, comparators, provider replications, and failed or null
gates are secondary and labeled as such; most appear only in the supplement and append-only ledger,
while the retrospective public MuSiQue control and ToolSandbox comparator rows remain in the
main text to expose the deployment-relevant comparison and make the natural null interpretable.
MuSiQue-12: public control and privileged positive control.Each pool has twelve permuted
cards and 220 legal triples. The deployment-facing result is the public interface learned only from
public task/card text and training intervention outcomes: partition decoding obtains 0.424 regret
versus 0.554 for its matched graph, with no latent membership labels at training or test time. Because
this interface was designed after the primary analysis, the result is retrospective and cannot replace a
prospectively frozen public-policy validation. Separately, the pre-specified interface trained from
latent component membership obtains 0.402 versus 0.532. Those labels are privileged benchmark-
construction information. We retain that pair solely as a positive control showing that the outcome
table is sensitive to global completion when the relevant local structure is supplied; it is not evidence
for an externally useful router. Dependence, no-partition, and representation controls are reported in
Appendix D.
HotpotQA-4: a direct-comparator stress test.Each task has four workers and one must choose a
size-three team. The direct baseline family is deliberately non-degenerate: a balanced multinomial
leave-one-out classifier and an unrestricted two-hidden-layer team MLP both consume exactly the
public task/card text and training-only best-full-team labels, and both can represent every one of the
four decisions. Neither reads required roles, evidence, answers, semantic-route labels, or held-out
outcomes. The leave-one-out classifier is the stronger held-out direct baseline (regret 0.3133; the
MLP is 0.3500 at seed 29), so the reported UNIFIED-COVER contrast is conservative: 0.1100 versus
0.3133, paired gain 0.2033 (CI [0.1533, 0.2567], sign-flip p=.00001 ; 69/223/8 wins/ties/losses).
Low-order unary/pairwise baselines are degenerate under the strict proof gate because incomplete
teams have value zero; they are therefore not the main comparator. This is evidence for an inductive
bias and sample efficiency in a four-action decision—not evidence that direct set scoring already
solves large coalition routing.
5

Preprint
mean benchmark regret (lower is better)
MuSiQue graph 0.554
MuSiQue partition 0.424
Hotpot leave-one-out 0.313
Hotpot direct set 0.110
Figure 2: Controlled public-interface comparisons. The MuSiQue pair is retrospective; the HotpotQA
pair is pre-specified. Regret is exact within each declared action space; scales are not compared
across instances.
5 EXECUTION DECOMPOSITION UNDER A FIXED STACK
Offline tables isolate selection exactly, but genuine worker messages are still useful as a diagnostic.
We freeze both routes, execute their union with the same hosted workers and fixed finalizer, then
compare only the selected routes. The oracle term cancels in this paired difference, so this identifies
a relative route comparison even though it does not recover an execution oracle.
The pre-specified 300-task Llama study makes the key distinction visible: UNIFIED-COVER trans-
ports verifier-complete evidence more often, but its raw exact answer advantage over leave-one-out is
only one percentage point and its 95% interval crosses zero. A better route can therefore be hidden by
a weak finalizer; conversely, an end-to-end answer gain alone cannot prove a routing effect without
the fixed-protocol control.
Table 5: Frozen genuine execution. Executed-route regret is calculated only on the union of the
frozen selected routes, not over all possible teams.
Family Router
Verified evidence
complete
Raw answer
exact
Raw route
regret
Llama UNIFIED-COVER 81.67% 36.33% 0.050
Llama leave-one-out 62.67% 35.33% 0.060
The verified evidence-complete Llama contrast is 0.190 executed-route-regret points (95% CI
[0.140, 0.240]; Holm p=.00003 within the original family). This endpoint records successful
evidence/citation transport under the enforced verifier; it is not finalizer exact-answer success. The
untouched raw-answer contrast is 0.010 (CI [ −0.0067, 0.0267]). These numbers make the claim
hierarchy concrete: verified evidence transport is the confirmatory execution result; raw-answer gains
are conditional on the downstream configurationG.
That conditioning is substantive. The completed crossed2×2 diagnostic shows that absolute execution
values depend on the finalizer, while finding no detectable router-by-finalizer interaction in this two-
finalizer panel (Table 10; Appendix D). All four within-cell route advantages are positive, so the
experiment does not demonstrate a routing-rank reversal; that remains a theoretical possibility under
Proposition 1. The broader six-configuration panel remains incomplete. All provider replications and
later follow-ups are disclosed in Appendix D and the ledger, but do not enter the main claim.
6 NATURAL HETEROGENEOUS-TOOL VALIDATION
The controlled QA tables identify their finite estimands, but their outcomes are constructed evi-
dence coverage. We therefore ask whether the same protocol remains informative in a natural tool
environment. The final ToolSandbox study exposes five heterogeneous public families—settings,
date/utility, directory, messaging, and reminders—backed by official local tools. Its declared action
family contains the five singletons, ten pairs, and the full five-worker team: 16 coalitions per task.
A pinned Qwen2.5-14B-AWQ executor starts from fresh simulator state, and value is the fraction
6

Preprint
of official safe tool-state milestones completed. This decomposed endpoint attributes selection and
execution separately from answer synthesis.
The development matrix combines 34 earlier tasks and contains all 34×16 = 544 outcomes. We
then freeze a public capability router and evaluate an outcome-untouched 14-task within-family
variant-shift validation. It is not scenario-family-disjoint replication. Every one of the 14×16 = 224
expected held-out rows is valid, and every task exhibits at least two distinct coalition values. The
natural gate therefore passes its two prerequisite questions: the stack can use the tools, and changing
the coalition changes the measured outcome.
Table 6: Five-family ToolSandbox variant-shift validation (14 tasks, 16 declared coalitions/task).
Completion is the official safe-evidence endpoint; lower regret is better. “Style” rows are interface-
level adaptations, not exact published-system reproductions.
Policy or reference Completion Regret Mean workers
Per-task declared-family oracle .768 — —
All workers .655 .113 5.00
Development-best fixed team .655 .113 5.00
Learned value router .655 .113 4.57
ToolBench-style card retriever .655 .113 5.00
Frozen public capability router .637 .131 3.00
DyLAN-style trial selector .482 .286 2.50
The prospectively frozen capability router reaches 0.637 completion and regret 0.131 (95% task-
bootstrap CI [0.042,0.244]), failing the predeclared regret threshold of 0.10 and trailing all-workers by
0.018. The 0.10 criterion was fixed as a practical tolerance on the [0,1] endpoint: a successful router
could leave at most ten percentage points of mean safe-evidence completion below the declared-
family oracle. This is a valid negative held-out result, not a failed run: all rows are present and
the 0.113 gap between the declared-family oracle and all-workers shows genuine team-dependent
headroom.
After the held-out summary had been inspected, we ran a no-API comparator suite on the already
collected matrix. Every route is fitted using development outcomes only, serialized, and then scored
by held-out-table lookup. The strongest five-fold-selected learned value router matches all-workers
exactly at 0.655 while selecting the full team on 12 tasks and a pair on two, reducing mean team size
from 5.00 to 4.57 without improving value. The development-best fixed team and ToolBench-style
card retriever both reduce to all-workers; the DyLAN-style trial selector performs worse. None clears
regret 0.10. Because the suite itself was specified after inspection of the held-out summary, only
the comparator-suite rows in Table 6 are retrospective, even though their route fitting never reads
held-out outcomes. They cannot retroactively rescue or replace the prospectively frozen router result.
This is the natural study’s substantive finding: exhaustive evaluation reveals a 0.768 declared-family
ceiling, but the later best development-frozen comparator leaves 0.113 value on the table. COVER
succeeds here by distinguishingmeasurement headroomfromachieved routing performance. A
final-answer-only benchmark would additionally mix this gap with synthesis failures; a top-k success
metric would hide it behind ties. The decomposed finite table makes the unresolved routing problem
visible.
7 ARTIFACTS AND REPRODUCIBILITY
Every controlled study is tied to a frozen source-ID manifest, held-out route file, task-level result file,
and analysis command. The repository provides a sanitized intervention archive containing hashed
task identities, generic coalition identifiers, and deterministic values. This archive is sufficient to
re-score a supplied route file, but not to run a new public-information router by itself because source
text and public cards are omitted for licensing reasons. To develop a new router, a researcher obtains
the original datasets under their licenses, reconstructs the allowed public inputs with the released
manifest builder, emits routes keyed by the frozen task hashes, and scores them against the archive.
7

Preprint
The final ToolSandbox release contains the five-family development and held-out manifests, 544
development and 224 held-out task–coalition rows, the prospectively frozen capability-router decision
file, and the retrospective offline baseline suite. The latter serializes its own method parameters and
hashes before opening the held-out table. The released summary, freeze record, and 84 per-policy
held-out routes are sufficient to recompute Table 6 without another model or API call. The earlier
three-family 105-row table is retained in the study ledger as a capability pilot, not silently combined
with or substituted for the final validation.
The hosted execution traces are not claimed to be perfectly replayable: a provider can change despite
temperature-zero requests. We release compact per-task outcomes, prompts, route decisions, model
identifiers, protocol hashes, and no-API commands for every calculation that does not require the
provider. An append-only study ledger lists positive, null, failed-gate, diagnostic, incomplete, and
infrastructure-invalid studies with their stopping rules. This is why the paper separates a finite
deterministic table result from a stochastic population-utility claim.
8 DISCUSSION:WHEN SHOULD ONE USECOVER?
COVER is most useful when a researcher can afford exhaustive outcomes for a meaningful but small
team family, and wants to know whether a routing rule rather than a changed pipeline caused a
measured effect. It is particularly suitable for evaluating a new selector against an established worker
and finalizer stack. It is not the right tool for claiming exact oracle performance among hundreds of
unconstrained tools. In that setting, a researcher should precommit a public sampling design, record
inclusion probabilities, report sampled-action regret and its coverage, and test the sampler against
full enumeration on a smaller overlap cohort.
Large spaces need not make every comparison unidentifiable: Theorem 1 shows that the precommitted
route union is exactly the minimal assumption-free support for all contrasts among the frozen policies,
while leaving absolute oracle regret unidentified. Table 2 states the general distinction; the stress-test
implementation is supplemental.
The methodology also suggests a reporting norm. A paper should say whether its conclusion concerns
(a) a finite controlled selection table, (b) evidence transport under fixed generation, or (c) final task
success under stochastic execution. These are related but not interchangeable quantities. In our
own evidence ladder, the Llama experiment demonstrates precisely why the distinction changes the
conclusion.
The ToolSandbox result adds a second reporting norm: a declared-family oracle ceiling is not router
performance. Here 0.768 is obtainable only by post-hoc per-task lookup over the 16 declared teams,
whereas the prospectively frozen router scores 0.637 and a later retrospective development-only
comparator scores 0.655. Reporting the oracle without achieved performance would turn treatment
variation into a fictitious routing result; reporting only achieved performance would conceal that the
environment contains exploitable heterogeneity. COVER requires both.
9 SCOPE AND CONCLUSION
COVER answers one narrow question well: within a declared finite action space and frozen stack,
how much benchmark value does a router lose relative to the best team when only the selected
coalition changes? Complete interventions, a strict information boundary, and frozen downstream
execution make that question identifiable. The evidence spine is deliberately short: two controlled
tables establish exact selection evaluation, one execution study separates evidence transport from
synthesis, and the five-family ToolSandbox variant-shift validation establishes natural treatment
variation while rejecting the frozen router headline.
The limits are equally important. The controlled outcomes are construction-defined; the pre-specified
MuSiQue policy is only a privileged positive control, while its more deployment-relevant public-
interface result is retrospective; the natural validation has only 14 within-family task variants and
its retrospective baseline suite cannot be promoted to a prospective result; and a one-draw provider
execution is not population utility. No result establishes stack-invariant, large-pool, or general agent-
system superiority. The headline is methodological: COVER can identify a routing gain, separate
it from synthesis, and—when the data demand it—show that substantial declared-family oracle
8

Preprint
headroom has not yet been converted into deployable routing performance. The supplement and
append-only ledger retain all representation controls, alternative endpoints, scale studies, provider
follow-ups, null gates, and incomplete panels so that this narrower narrative does not become selective
reporting.
REFERENCES
Nikhil Bansal, Avrim Blum, and Shuchi Chawla. Correlation clustering.Machine Learning, 56:
89–113, 2004.
Tirthankar Dasgupta, Natesh S. Pillai, and Donald B. Rubin. Causal inference from 2k factorial
designs using the potential outcomes model.arXiv preprint arXiv:1211.2481, 2015. URL
https://arxiv.org/abs/1211.2481.
Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, and Igor Mordatch. Improving factual-
ity and reasoning in language models through multiagent debate.arXiv preprint arXiv:2305.14325,
2023.
Adam Fisch, Shubhendu Trivedi, Fantine Huot, William W. Cohen, Michael Kaisers, Mirella Lapata,
Kate Larson, and Jacob Eisenstein. Pandora’s AI model routing box: Efficient allocation with
costly value estimation.arXiv preprint arXiv:2608.20316, 2026. URL https://arxiv.org/
abs/2608.20316. Version 2, revised 21 August 2026.
Alex Kulesza and Ben Taskar.Determinantal Point Processes for Machine Learning, volume 5 of
Foundations and Trends in Machine Learning. Now Publishers, 2012.
Juho Lee, Yoonho Lee, Jungtaek Kim, Adam R. Kosiorek, Seungjin Choi, and Yee Whye Teh.
Set transformer: A framework for attention-based permutation-invariant neural networks. In
Proceedings of the 36th International Conference on Machine Learning, pp. 3744–3753, 2019.
Zijun Liu, Yanzhe Zhang, Peng Li, Yang Liu, and Diyi Yang. A dynamic LLM-powered agent
network for task-oriented agent collaboration.arXiv preprint arXiv:2310.02170, 2023. URL
https://arxiv.org/abs/2310.02170.
Isaac Ong, Amjad Almahairi, Vincent Wu, Wei-Lin Chiang, Tianhao Wu, Joseph E. Gonzalez,
M. Waleed Kadous, and Ion Stoica. RouteLLM: Learning to route LLMs with preference data.
arXiv preprint arXiv:2406.18665, 2024.
Yujia Qin, Shihao Liang, Yining Ye, Kunlun Zhu, Lan Yan, Yaxi Lu, Yankai Lin, Xin Cong, Xiangru
Tang, Bill Qian, Sihan Zhao, Lauren Hong, Runchu Tian, Ruobing Xie, Jie Zhou, Mark Gerstein,
Dahai Li, Zhiyuan Liu, and Maosong Sun. ToolLLM: Facilitating large language models to master
16000+ real-world APIs. InInternational Conference on Learning Representations, 2024. URL
https://arxiv.org/abs/2307.16789.
Aaman Rebello, Shengpu Tang, Jenna Wiens, and Sonali Parbhoo. Leveraging factored action spaces
for off-policy evaluation.arXiv preprint arXiv:2307.07014, 2023. URL https://arxiv.org/
abs/2307.07014.
Tatsuhiro Shimizu, Koichi Tanaka, Ren Kishimoto, Haruka Kiyohara, Masahiro Nomura, and
Yuta Saito. Effective off-policy evaluation and learning in contextual combinatorial bandits. In
Proceedings of the 18th ACM Conference on Recommender Systems, 2024. doi: 10.1145/3640457.
3688099. URLhttps://arxiv.org/abs/2408.11202.
Junlin Wang, Jue Wang, Ben Athiwaratkun, Ce Zhang, and James Zou. Mixture-of-Agents enhances
large language model capabilities.arXiv preprint arXiv:2406.04692, 2024.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu, Beibin Li, Erkang Zhu, Li Jiang, Xiaoyun
Zhang, Shaokun Zhang, Jiale Liu, et al. AutoGen: Enabling next-gen LLM applications via
multi-agent conversation.arXiv preprint arXiv:2308.08155, 2023.
Manzil Zaheer, Satwik Kottur, Siamak Ravanbakhsh, Barnab´as P´oczos, Ruslan Salakhutdinov, and
Alexander J. Smola. Deep sets. InAdvances in Neural Information Processing Systems, volume 30,
2017.
9

Preprint
A FORMAL IDENTIFICATION DETAILS
A.1 WHY MOVING-PIPELINE COMPARISONS ARE NOT SELECTION COMPARISONS
Write G for the full downstream protocol: public/private timing, worker behavior, communication,
finalizer, and utility. For frozen routersr 0, r1, the selection contrast under a common protocol is
∆G x (r1, r0) =V G x (r1(x))−V G x (r0(x)).
Theorem 2(Moving-pipeline non-identification).Observing V G0 x (r0(x)) and V G1 x (r1(x)) does not
identify ∆G0 x (r1, r0) when G0 and G1 may differ, even with arbitrarily many repeated observations
of those two systems.
Proof. Consider one task, teams A, B, r0(x) =A , r1(x) =B , and observed system outcomes 0,1 .
In one compatible world G0 =G 1 and V G0 (A) = 0, VG0 (B) = 1, giving contrast one. In another,
both teams have value zero under G0 but V G1 (B) = 1 because the downstream protocol changed,
giving contrast zero. The observations are identical.
Proposition 1(Within-stack exactness does not imply stack invariance).Even if every team in Fx is
observed under G0, neither the team ranking nor the regret of a policy under a different stackG1 is
identified without an assumption or observations linkingV G0 x andV G1 x .
Proof. For two teams A, B, a complete G0 table with V G0 x (A) = 1 and V G0 x (B) = 0 is compatible
both with a G1 table preserving that ordering and with one reversing it. Both worlds agree on every
G0 intervention. Thus exhaustive coverage identifies a table conditional on G0, not transport to
G1.
Panel summaries do not create invariance.For a predeclared finite panel of stacks G, sensitivity
can be summarized without collapsing the stack index. For example,
RG(r) =|G| −1 X
G∈G
Rbench,G(r), s 2 G(r) = (|G| −1)−1 X
G∈G

Rbench,G(r)− RG(r) 2 ,
together with pairwise policy-rank reversals acrossG. These quantities describe the observed panel
only: a mean is not a stack-free causal score, and neither its variance nor pairwise agreement identifies
transport to an unobserved finalizer. Our completed 2×2 worker-message/finalizer study is such a
conditional sensitivity diagnostic. The broader six-configuration panel is incomplete and is not used
to estimate these summaries.
Theorem 3(Exact identified set for a finite action table).Fix G. Let Ox ⊆ Fx be observed
interventions, all values lie in[0,1],r(x)∈O x, andm G x = maxS∈Ox yG x,S. IfO x =F x, then
Rbench,G x (r) =m G x −y G x,r(x).
If Ox ⊊F x, the identified set of Rbench,G x (r) over all bounded finite tables compatible with the
observations is exactly h
mG x −y G x,r(x),1−y G x,r(x)
i
.
Thus, with at least one unobserved team, exact nonparametric regret is point-identified if and only if
mG x = 1.
Proof. When all actions are observed, the displayed equality is the definition of finite-table regret
underG. Otherwise, the observed maximum supplies the lower endpoint and the range supplies the
upper endpoint. Assign every unobserved team a value at most mG x to attain the lower endpoint, or
assign one unobserved team value one to attain the upper endpoint. Both completions agree on Ox.
The endpoints coincide exactly whenm G x = 1.
10

Preprint
A.2 MINIMAL ROUTE-UNION SUPPORT
Proof of Theorem 1. Write A=A x(R). If A⊆O x, then every yG x,rk(x) is observed, so every
pairwise difference is a lookup. Now suppose |A| ≥2and some S† ∈A is absent from Ox. Choose
T∈A\ {S †}. Construct two outcome tables that agree on every observed intervention and on every
unobserved intervention except S†, but set yG x,S† = 0 in one and yG x,S† = 1 in the other. Hold yG x,T
fixed across the two tables. The contrast between a policy selecting S† and one selecting T therefore
differs across two observationally equivalent tables and is not point-identified. Hence every sufficient
support contains A, while A itself is sufficient, making it the unique inclusion-minimal support. If
|A|= 1 , all policies choose the same action and every pairwise difference is zero by definition.
For two frozen routes, define Ux(r) as the observed endpoint for r(x). Route-union regret uses only
the two executed values, and its difference cancels the route-union oracle:

max(Ux(r0), Ux(r1))−U x(r0)

−

max(Ux(r0), Ux(r1))−U x(r1)

=U x(r1)−U x(r0).
This is a relative contrast over frozen policies, not absolute regret againstmax S∈Fx yG x,S. The same
support result extends to any finite K and automatically deduplicates policies that choose the same
team.
B BENCHMARK CONSTRUCTION AND INFORMATION CONTROLS
B.1 MUSIQUE-12
Each held-out MuSiQue task provides a target multi-hop evidence component. Three non-target
components from source-disjoint donor examples are added to form a twelve-card pool, and card
order and superficial labels are permuted. A legal action is any size-three coalition, giving
12
3

= 220
teams per task. The offline finalizer is fixed and proof based: it receives the selected worker evidence
in canonical order and scores the evidence units recovered by the team. This creates a controlled
complementarity stress test; it does not claim that natural agent pools come pre-partitioned into
balanced triples.
The train-only component membership labels used by the pre-specified Partition-COVER positive
control are deliberately treated as privileged construction supervision. They never enter held-out
routing, but they are not a naturally available deployment label. To test whether such labels are
indispensable, a secondary post-hoc control derives pair pseudo-labels only from completetraining
coalition outcomes (a pair is positive if it occurs in an optimal training triple) and learns qij from
public task/card text. It uses no component IDs, private evidence, or held-out outcomes. This public
interface obtains regret 0.4240, versus 0.4540 after removing only completion and 0.5540 for its
matched public graph; it is evidence that an interface can be learned from prior intervention feedback,
not a preregistered deployment result.
B.2 HOTPOTQA-4
Each HotpotQA task exposes four public worker cards and routes exactly three workers. Private
worker evidence is constructed so that the finalizer must combine the selected messages to recover
the answer. The four legal actions are the four possible omissions. This deliberately small action
space permits exhaustive held-out outcomes and direct full-team baselines. It should be read as a
sample-efficiency/inductive-bias test, rather than a representation-theoretic separation from a classifier
that can enumerate all four actions.
B.3 FRESHPUBLIC-MEDIUM-33PROTOCOL
The machine-readable protocol and target manifest were committed as5889e17 before the evaluator
was first run. The statistical units are 25 unused target source IDs in each split. The target IDs are fresh
relative to prior MuSiQue history; globally unused donor allocation was infeasible after the historical
source audit, so donor banks are instead target-disjoint and train/heldout-disjoint, with this limitation
recorded in the manifest. Each target receives ten donor chains, producing 33 permuted public cards.
11

Preprint
A card’s synthetic budget weight is a deterministic hash of its public description; all teams of sizes
one through four with total weight at most 12 are legal. These weights are feasibility proxies, not
measured resource costs. The router sees task text, card text, and weights only. It learns pair targets
from maximum observedtraining-team coverage and then fits a fixed public coalition regressor; the
baseline receives the same pair interface but scores only pairwise/relevance terms. Required roles
are used only to create training table targets and to score held-out teams. The run-all-25 stopping
rule, bootstrap, sign-flip test, and no-rerun condition were frozen in the protocol. The null result is
therefore not removed, reseeded, or reinterpreted as an unreported tuning failure.
Table 7: Public/private boundary used in both controlled instances.
Field Router at selection time Worker/finalizer after selec-
tion
Question and public capability cards yes yes
Private passages and evidence units no selected worker only
Gold answer, required team, component ID no no
Held-out intervention value no evaluation only
Finalizer identity and canonical message order fixed, not routed fixed
B.4 BINARY AND GRADED VALUES
The primary offline endpoint awards a complete proof. To test whether the conclusion is purely an
all-or-nothing artifact, we re-score the frozen same intervention tables by the unweighted fraction of
required evidence units recovered. No route, model, or hand-chosen evidence weight changes under
this re-scoring. The direction of the two main offline comparisons remains positive; these graded
results are secondary endpoint-sensitivity evidence, not additional primary discoveries.
C VALIDATION-POLICY IMPLEMENTATION DETAILS
C.1 UNIFIED-COVER
Unified-COVER uses a frozen MiniLM sentence encoder for task and public-card embeddings. For
a task embedding t and card embedding vi, a learned projection receives [t, vi, t⊙v i,|t−v i|].
Self-attention pools card states for the full available pool and a candidate team; invariant sums and
maxima are concatenated with these pooled states and passed to a small MLP. No worker position or
hidden role label is supplied. Training uses observed train-coalition values with regression, pairwise
ranking, and best-team listwise terms. On HotpotQA it scores all four legal teams directly.
C.2 PARTITION-COVER
Partition-COVER is a structured decoder, not a second learned set-value model. A logistic text inter-
face fitted on 120 training tasks maps public task/card pair features to a bounded compatibility score
qij. The pre-specified positive-control interface fits this map using latent component-membership
targets; the retrospective public interface instead derives targets from training coalition outcomes. At
held-out routing time both consume only public text, but only the latter has a deployment-plausible
training signal. The decoder uses a fixed monotone logit transform of clipped qij, task relevance, and
path coherence to score triples, then applies exact bitmask dynamic programming over balanced par-
titions. Each matched graph receives the same interface and relevance. Hence each within-interface
contrast is about global completion conditional on shared local information, not better edge prediction.
The task relevance/path weights (8,1) were selected on development and frozen before held-out
evaluation.
The decoder runs in O(2nn2) time and O(2n) memory. It is practical for n= 12 but intentionally
not claimed as a hundred-worker algorithm. If natural coalitions have unequal sizes, the balanced
feasible family can exclude the optimum; variable-size partitioning remains future work.
12

Preprint
Table 8: Originally specified offline comparisons. Lower regret is better. Holm correction applies to
these three tests; the MuSiQue row is a privileged positive control, not deployment evidence.
Study Comparator COVER Improvement Status
MuSiQue-12 binary calibrated graph 0.5320 0.4020 0.1300 positive control
HotpotQA-4 binary leave-one-out 0.3133 0.1100 0.2033 primary
Llama verified route regret leave-one-out 0.2900 0.1000 0.1900 primary
Table 9: Attribution and robustness checks. All rows are secondary and unadjusted.
Check Result Interpretation
Same local score, no partition 0.4660 vs 0.4020; gap 0.0640,
CI [0.0400,0.0880]
global completion contributes
beyond fixed local scores
Graded evidence coverage both offline advantages remain
positive
conclusion is not only a proof-
gate effect
Outcome-supervised public interface partition 0.4240 vs graph
0.5540; no-partition 0.4540
train outcomes and public text
suffice; retrospective, no latent
membership labels
Zero-shot Llama public router MuSiQue regret 0.4860 (500
tasks)
external practitioner compara-
tor; between public partition and
public graph
GPT-OSS strict 300-task rerun raw gain 0.0433, CI
[0.0133,0.0733]
secondary matched family sup-
port
GPT-OSS source-disjoint 1k raw gain 0.0870, CI
[0.0640,0.1110]
late prospective provider-
pipeline confirmation
D EXTENDED RESULTS AND EXECUTION PROVENANCE
D.1 DEPENDENCE,REPRESENTATION,AND STACK CONTROLS
Some composite MuSiQue targets share internal source-component IDs. Grouping the 500 tasks into
201 connected component-sharing clusters (largest 20 tasks) leaves the pre-specified positive-control
gain of 0.1300 positive under cluster bootstrap, CI [0.0968,0.1634]. This is a dependence sensitivity,
not a claim that every latent component is independent.
On HotpotQA, an unrestricted direct four-way classifier receiving the frozen MiniLM task/card
embeddings and the same seven-dimensional public role vectors has regret 0.4467. Changing only
the set scorer’s static role prior gives regret 0.1233 for original profiles, 0.1167 for one-hot identity,
0.1167 for deterministically permuted profiles, and 0.7500 when all workers share one constant profile.
Thus the hand-authored semantic coordinates do not explain the advantage, while distinguishable
worker identity is necessary in this construction. These post-hoc controls do not overwrite the frozen
primary 0.1100 result.
Table 10: Completed 300-task 2×2 worker-message/finalizer diagnostic. Values are raw exact
accuracy; gain is Unified-COVER minus leave-one-out with a task-bootstrap 95% interval.
Worker messages Finalizer Leave-one-out Unified-COVER Gain [95% CI]
Llama Llama .4833 .5000 .0167 [−.0067,.0400]
Llama GPT-OSS .5767 .6000 .0233 [−.0067,.0533]
GPT-OSS Llama .4833 .5267 .0433 [.0133,.0733]
GPT-OSS GPT-OSS .5533 .5900 .0367 [.0033,.0700]
Absolute accuracy changes across G. Switching finalizers changes the route advantage by 0.0067 for
Llama messages (CI [−0.0200,0.0333]) and −0.0067 for GPT-OSS messages (CI [−0.0333,0.0200]).
Both interactions include zero, but this two-finalizer panel cannot establish invariance. The prede-
clared six-configuration panel remains incomplete and contributes no confirmatory claim.
13

Preprint
D.2 NATURALTOOLSANDBOX PROVENANCE AND OFFLINE COMPARATOR SUITE
The natural validation proceeded in stages rather than as one selectively reported run. An initial
three-family capability study completed a 42-row gate, 133-row training table, and 105-row family-
disjoint held-out table. It established that official milestone scoring varied across coalitions, but
its coarse grouping made the full three-worker team a difficult comparator to improve upon. We
retained that result and expanded the representation to five separately named public families. The final
validation action set is not all 25 −1 nonempty teams: it is the 16 predeclared singletons, pairs, and
full team. This keeps exhaustive execution manageable while testing both specialist and cross-family
collaboration.
The five-family development table contains 34 complete tasks and 544 valid rows. The pub-
lic capability router was frozen before the 14-task variant-shift validation and has freeze hash
5e15a4e28884dc6a. The held-out manifest hash is e1145424b77c8c5f; all 224 rows use
ToolSandbox commit 165848b9a78cead7. The panel consists of untouched scenario variants
from represented families, not new scenario families, and its claim boundary was recorded before
scoring: all rows must be valid and mean regret must not exceed 0.10. The threshold encodes a ten-
percentage-point practical tolerance below the declared-family oracle on the mean[0,1] safe-evidence
endpoint. Coverage passed; regret did not.
The later offline suite evaluates four development-only comparators. The fixed baseline chooses
the highest mean-value development team. The learned baseline selects between multi-output ridge
value prediction and direct team classification by five-fold development regret; ridge with α= 3
wins. The ToolBench-style adaptation retrieves public worker cards with a TF–IDF interface whose
vocabulary and inverse-document frequencies are fitted only on cards and development requests;
development selection chooses k= 5 . The DyLAN-style adaptation averages coalition values from
the nearest development trials and applies a fixed team-size penalty; development selection chooses
eight neighbors and penalty 0.05. These are COVER-compatible abstractions of retrieve-then-use
and preliminary team optimization, not executions of the published systems.
The suite writes its specification before reading held-out rows. Its freeze hash is
b48ebe8d18d96254; an independent standard-library audit resolves every selected team directly
against the raw matrix and reproduces all 84 policy–task values. This outcome isolation prevents
held-out-label leakage during fitting. It does not undo the higher-level provenance fact that we
chose the comparator suite after seeing the held-out summary, so all baseline-suite results remain
retrospective and unadjusted.
D.3 ZERO-SHOTLLM-AS-ROUTER COMPARATOR
To test whether the policies are distinguished only from bespoke baselines, we queried a zero-
shot llama-3.3-70b-versatile router once per held-out task. It received exactly the task
prompt and public capability cards, was prohibited from using private evidence, required teams, or
intervention values, and emitted one size-three team before table scoring. On MuSiQue-12 it reaches
0.4860 mean regret and a 51.4% oracle-hit rate (500 tasks): between the retrospective public graph
(0.5540) and public Partition-COVER control (0.4240). This is a fixed-prompt, post-hoc external
comparator rather than a tuned or confirmatory baseline. On HotpotQA-4 it obtains 0.7500 regret,
which is uninformative under the strict proof gate: all incomplete teams share value zero. The route
files and exact prompt are released with the supplementary artifacts.
D.4 PARTITION-FREE MEDIUM-POOL PROTOCOL
The medium-pool study freezes a deterministic 100-task development / 400-task split of the existing
500-task MuSiQue target before fitting its residual coalition scorer. It uses linear evidence coverage
and evaluates every independent size-three team in pools of 8, 10, or 12 public cards. Completion,
balanced components, and latent membership labels are absent at inference. Table 11 reports the
frozen secondary reanalysis; all values are exact benchmark regret on the declared action family, but
the target is not independent of the primary MuSiQue study. The constrained companion permits
teams of sizes 1–3 under fixed synthetic budget weights.
At 12 cards, calibrated-graph regret is 0.3283 and the local-score gain remains 0.0358 under
component-cluster resampling (190 clusters; CI [0.0143,0.0576]); the 0.3375 entry in Table 11
14

Preprint
Table 11: Frozen partition-free secondary reanalysis (400 existing-target tasks; lower linear-coverage
regret is better).
Pool / teams Graph Pairwise Local Same-18D HGB Same-18D Ridge COVER Gain/local
8 / 56 .2133 .2108 .1908 .3300 .3375.1750.0158
10 / 120 .2833 .2700 .2367 .3783 .3792.2200.0167
12 / 220 .3283 .3100 .2867 .4133 .3933.2508.0358
is the 8-card same-feature Ridge control. Gains over same-feature HGB and Ridge at 12 cards are
0.1625 and 0.1425. At proxy budgets 6, 9, and 12, respectively 55, 148, and 246 teams of sizes
1–3 are legal. COVER obtains regrets 0.1425, 0.1742, and 0.2533. The weights are not operational
cost measurements. These secondary analyses broaden the controlled action space, not the claim to
natural large-agent deployment or cost efficiency.
D.5 LARGE-SPACE ROUTE-UNION STRESS TEST
In a separately frozen 48-card stress test with all teams of sizes 1–6 (14,196,868 legal actions/task), we
execute only the union of two frozen routes plus fixed stratified background teams: 49.48 actions/task,
or 3.49×10 −6 of the declared family. The structural route recovers 0.3414 more required-evidence
mass (CI [0.2930,0.3898], sign-flip p <10−4) than the fixed public random route. This identifies
that paired effect exactly; it does not identify either route’s large-space oracle regret.
D.6 POST-LLAMA RAW-OUTPUT PROVENANCE
The GPT-OSS 1k study was not the only activity after the pre-specified Llama raw endpoint was
inconclusive. To avoid a file-drawer reading, Table 12 inventories every retained post-Llama raw route
comparison. The 1k study is source-disjoint, matched to the original Unified-COVER/leave-one-out
comparison, and frozen before its own execution, but remains late prospective and is deliberately
kept out of the main evidence spine.
Table 12: Retained post-Llama raw-output provenance. Allpvalues are unadjusted.
Activity Tasks Raw gain Status
Original-answer MuSiQue, Llama 300 0.1133 [0.0700,0.1567] secondary, different construction/comparator
Original-answer MuSiQue, GPT-OSS 140 0.0786 [0.0143,0.1500] outcome-blind quota checkpoint
Strict HotpotQA GPT-OSS rerun 300 0.0433 [0.0133,0.0733] secondary same-task replication
Source-disjoint HotpotQA GPT-OSS 1,000 0.0870 [0.0640,0.1110] late prospective confirmation
Repeated GPT-OSS subset 120×2 repeats 0.0694 [0.0139,0.1278] secondary stability check
D.7 REPEATED EXECUTION
On a subsequently frozen, evidence-pattern-stratified 120-task subset of the 1k study, two additional
executions per selected task–team yield m= 3 raw accuracy 47.22% for Unified-COVER versus
40.28% for leave-one-out. The task-clustered raw route-regret improvement is 0.0694 (CI [0.0139,
0.1278]; sign-flip p=.0232 ). Raw success changes across three draws for 10.83% of Unified-
COVER tasks and 9.17% of leave-one-out tasks. This supports repeat stability for this temperature-
zero provider pipeline; it does not identify general population utility.
E REPRODUCTION CHECKLIST
The release contains source-ID manifests, route files, compact per-task predictions, aggregate sum-
maries, paired tests, SHA-256 checksums, and scripts for each no-API computation. The following
checks reproduce the central claims:
1. verify the intervention archive checksum and route-file hashes;
2. reconstruct the MuSiQue and HotpotQA offline tables under the licensed source datasets;
3. score frozen routes and recompute task-level bootstrap and sign-flip statistics;
15

Preprint
4. recompute graded coverage from the same tables without changing routes;
5. evaluate a supplied new route file against the sanitized table; and
6. verify the five-family ToolSandbox development and confirmation hashes, the
544/224 matrix counts, the frozen capability-router hash, and all 84 routes in
outputs/toolsandbox public baseline suite v1 routes.csv;
7. rerun scripts/evaluate toolsandbox public baseline suite.py without
model access and verify freeze hashb48ebe8d18d96254;
8. inspect manifests/public medium pool protocol v1.json at
commit 5889e17, then reproduce its one permitted evaluation with
scripts/evaluate public medium pool v1.py; and
9. compile this manuscript with the included portable Tectonic configuration.
Source-bearing questions, passages, model transcripts, provider metadata, and credentials are ex-
cluded from the public archive. A researcher who wishes to run a new public-information policy
must obtain the original datasets under their licenses, reconstruct public inputs locally, and emit
hash-keyed routes. This is a licensing constraint, not a claim that the sanitized archive alone can
execute arbitrary new routers.
F FROZEN TARGETED ROUTING-ESTIMAND AUDIT
The audit in Section 2 is a targeted, non-systematic snapshot, frozen on 2026-08-19. The corpus was
assembled purposively to cover 2023–2026 work around multi-agent routing, team/role selection,
communication topology, dynamic orchestration, architecture search, context routing, and learned
collaboration. It was not produced by screening a complete database export. We included papers
whose declared primary method selects, learns, adapts, or searches a multi-agent team, role assign-
ment, communication/context route, topology, workflow, or architecture; surveys, general frameworks
without such an intervention, and static ensembles outside that scope were excluded.
The unit of coding is the paper’s declared primary intervention:Idenotes a relatively component-
aligned communication/topology intervention;T, direct team or role selection;S, a sequential routing
policy whose decision changes future interaction state; andJ, joint-system design over multiple
dimensions such as roles, models, prompts, tools, topology, or workflow. The coding order was S
for state-changing sequential routing, T for direct team/role assignment, I for a relatively isolated
communication/context/topology object, and J for a coupled multi-dimensional design object. These
mutually exclusive labels describe estimands, not methodological quality. In particular, a J result can
be exactly the right end-to-end quantity for a broad system-design objective, and an I result can be a
carefully controlled component analysis.
The frozen, machine-readable corpus and annotations are released as
routing estimand audit 30.json. It records the canonical paper titles, optimized
object, code, and audit note below; a deterministic validator checks record count, allowed codes,
unique IDs, and consistency of the reported totals. The corpus was coded by one author, without
independent second coding, inter-rater reliability, a retained complete candidate-screening count, or a
database-by-database query log. The counts are therefore descriptive only and are not an estimate of
field-wide prevalence. The corpus contains no paper that materializes an exhaustive held-out value
table over a declared finite coalition family under one common downstream protocol and reports
finite coalition-selection oracle regret. This is a scoped absence claim about these 30 papers, not a
literature-wide nonexistence claim or a claim that other routing objectives are invalid.
Code J I S T
Papers 16 8 4 2
Share 53.3% 26.7% 13.3% 6.7%
16

Preprint
Table 13: Frozen 30-paper targeted audit. “Object” names the main selected or
optimized object used for coding.
# Paper Code Object
1 DyLAN T Task-conditioned agent team followed by dynamic col-
laboration
2 GPTSwarm /Language Agents as
Optimizable Graphs
I Graph connectivity, with separate node/prompt opti-
mization
3 MacNet I Communication topology and agent scale
4 AgentPrune I Spatial/temporal communication-message graph
5 AgentDropout J Agents and communication edges jointly
6 MasRouter J Collaboration mode, agent roles, and LLM choice
7 ARG-Designer J Number of agents, roles, and communication links
8 AMAS I Environment-conditioned communication topology
9 DynaSwarm I Query-specific graph structure
10 Guided Topology Diffusion I Generated communication topology
11 EIB-LEARNER /Information
Propagation Effects
I Communication topology and sparsity
12 CARD I Environment-conditioned communication graph
13 Agent Q-Mix S Round-wise inter-agent communication actions
14 STRMAC /Optimal-Agent-
Selection
S Next acting agent conditioned on interaction history
15 Dynamic Role Assignment for
Multi-Agent Debate
T Model-to-role assignment before debate
16 RCR-Router S Memory/context subsets routed to roles over rounds
17 MaAS J Query-dependent agentic architecture sampled from a
supernet
18 MAS-Zero J Entire sub-MAS programs and workflows
19 OWL / Optimized Workforce
Learning
J Planner, coordinator, and specialized workforce behav-
ior
20 Learning to Deliberate / MPDF S Per-agent high-level deliberation actions
21 Multi-Agent Deep Research / M-
GRPO
J Planner/sub-agent policies and invocation behavior
22 WideSeek-R1 J Lead-agent orchestration and parallel subagent execu-
tion
23 MATPO J Planner and worker policies plus tool interaction
24 MAPoRL J Collaborative multi-turn behavior of interacting LLMs
25 ReMA J Hierarchical meta-thinking and reasoning agents
26 CoMAS J Agent policies trained from inter-agent interaction re-
wards
27 SiriuS J Agent behavior via an evolving trajectory/experience
library
28 AFlow J Full code-represented agentic workflow
29 ADAS / Meta Agent Search J Prompts, tools, control flow, and agent-system code
30 LGC-MARL J LLM-generated subtask/dependency graph and graph-
collaboration policy
17
