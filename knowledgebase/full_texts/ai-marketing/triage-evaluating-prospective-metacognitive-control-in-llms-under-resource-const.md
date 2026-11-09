---
title: 'TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints'
url: https://arxiv.org/abs/2605.13414
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Zabir Al Nazi
- Shubhashis Roy Dipta
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.13414
pages: 22
chars: 86657
fetched_at: '2026-11-08T13:36:16+00:00'
kb_version: 1
---

# TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under Resource Constraints

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs under
Resource Constraints
Zabir Al Nazi 1 Shubhashis Roy Dipta 2
Abstract
Deploying language models as autonomous
agents requires more than per-task accuracy:
when an agent faces a queue of problems un-
der a finite token budget, it must decide which
to attempt, in what order, and how much com-
pute to commit to each, all before any execu-
tion feedback is available. This is the prospec-
tive form of metacognitive control studied for
decades in human cognition, yet whether lan-
guage models possess it remains untested. We
introduce TRIAGE, an evaluation framework in
which a model receives a task pool and a token
budget calibrated to its own baseline cost, and
commits to a single ordered plan that jointly en-
codes selection, sequencing, and per-problem al-
location. Plans are scored against an oracle with
full knowledge of the model’s solvability and cost
on each problem, yielding a triage efficiency ra-
tio on a common scale. We evaluate frontier
and open-source models, with and without rea-
soning enabled, across competition mathematics,
graduate-level science, code generation, and ex-
pert multidisciplinary knowledge, and find that
current language models exhibit substantial gaps
in prospective metacognitive control, revealing a
previously unmeasured capability dimension with
direct implications for resource-efficient agent de-
ployment.
1. Introduction
Scaling test-time compute has become a major paradigm
for improving LLM reasoning (Snell et al., 2025), but it
has also made compute allocation a central unsolved prob-
lem: current reasoning models lack reliableprospective
controlover their own compute expenditure, and adaptive
allocation per problem can yield substantial efficiency gains
over uniform budgets (Snell et al., 2025; Alomrani et al.,
2025). Reasoning models generate thousands of tokens
even for trivial problems (Chen et al., 2024) and underthink
hard ones, prematurely abandoning promising reasoning
paths (Wang et al., 2025b).Unconstrained agents, simi-
larly, can consume thousands of tokens on agentic tasks and
still fail, exhibiting analysis paralysis and wasted compute
that correlates with decreased performance (Cuadron et al.,
2025).
This creates a concrete deployment problem: agents built
on these models face real resource constraints - token bud-
gets, tool-call limits, latency windows - and must decide
which tasks to attempt before committing resources. A
resource-rational agent should allocate finite compute to the
tasks where its expected return is highest (Lieder & Griffiths,
2020). In practice, this means an LLM facing a queue of
problems under a token budget should abstain from attempt-
ing ones it cannot solve, spend less on easy ones, and safely
commit sufficient resources to each attempted problem so
that under-allocation does not expend budget on partial or
incomplete solutions that yield no return - the same strategy
a student applies on a timed exam - the capability that Nel-
son & Narens (1990) formalized asmetacognitive control:
regulating effort allocation based on judgments of one’s own
knowledge state.
Recent work suggests LLMs have some of this capability
in isolation: large language models can predict whether they
will answer a question correctly (Kadavath et al., 2022),
yet reasoning-trained models are worse - not better - at
knowing when to abstain (Kirichenko et al., 2025). Barkan
et al. (2025) found that frontier models are systematically
overconfident about their own capabilities, and that this
overconfidence does not diminish with scale or reasoning
augmentation. The critical capability for an LLM planner is
not just predicting token cost or knowing when to abstain
from a single question, but managing a portfolio: given a set
of tasks and a shared budget, selecting which to attempt, esti-
mating cost, and ordering execution to maximize value. This
is the problem that many real-world agentic deployments
face - coding agents working through backlogs of issues,
research agents decomposing queries into sub-questions of
varying difficulty, and planning agents budgeting compute
across subtasks of a larger goal - all require cross-task prior-
itization under finite compute. Existing per-task budgeting
methods estimate token cost for a single problem (Han et al.,
2025; Li et al., 2025), and external batch schedulers rank
or route requests for throughput (Jin et al., 2023; Fu et al.,
2024). However, whether LLMs can themselves perform
1
arXiv:2605.13414v1  [cs.AI]  13 May 2026

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
the joint optimization - assessing their own feasibility, cost,
and priority across a heterogeneous task set under a shared
budget - remains untested, and answering it is a prerequisite
for building agents that can plan and optimize their own
resource use rather than relying on external orchestration.
We introduce TRIAGE, an evaluation framework for
prospective metacognitive controlunder resource con-
straints. The construct has three components.Metacogni-
tive controlis the use of self-knowledge to regulate behav-
ior, graded by the consequences of the model’s plan rather
than by verbalized confidence (Ackerman, 2026).Prospec-
tivedenotes that all decisions are committed before any task
is attempted, distinguishing TRIAGE from retrospective
measures of confidence or post-hoc calibration (Kadavath
et al., 2022; Koriat, 1997).Resource constraintsrefers to
a finite shared budget - output tokens by default - that the
model’s behavior consumes (Han et al., 2025). In TRIAGE,
a model receives a set of problems, point values per problem,
and a token budget calibrated to its own baseline cost on the
set. It returns a single ordered plan specifying which prob-
lems to attempt, how many tokens to allocate to each, and in
what order. This design operationalizes three foundational
control functions from Nelson & Narens (1990) in their
prospective form: selection (which problems to attempt),
allocation (how much compute to commit per problem),
and termination (where to commit budget cutoffs ex ante).
TRIAGE evaluates the control output directly rather than
asking the model to verbalize its underlying judgments -
appropriate for LLMs, where self-reports are an unreliable
signal of internal state and metacognition is better measured
behaviorally (Ackerman, 2026). Just as human learners
plan effort allocation under time pressure (Son & Metcalfe,
2000), an autonomous agent must jointly optimize them to
maximize expected utility under finite inference limits.
We evaluate 20 model architectures - 4 standard LLMs
and 16 reasoning-augmented LLMs, evaluated both with
and without thinking enabled - across four domains: com-
petition mathematics (AIME 2024–2025), graduate-level
science (GPQA Diamond; Rein et al., 2024), code gener-
ation (LiveCodeBench; Jain et al., 2024), and multidisci-
plinary expert knowledge (Humanity’s Last Exam; Phan
et al., 2025).
We find that current language models exhibit substantial and
uneven gaps in prospective metacognitive control. Strong
self-assessment in one domain rarely transfers to another,
extended reasoning improves task-level accuracy without
improving triage quality, and reasoning-trained models are
less likely to recognize unsolvable items when they appear
in a task pool. The gap between advisory and enforced
regimes is wide across budget levels, indicating that models
can sometimes choose what to attempt but rarely commit
budgets that they themselves can honor. Together, these
experiments characterize a previously unmeasured capabil-
ity dimension with direct implications for resource-efficient
agent deployment.
2. Related Work
2.1. Metacognition in Large Language Models
Metacognition, the capacity to monitor and regulate one’s
own cognitive processes (Nelson & Narens, 1990), has be-
come a central concern in LLM evaluation. Research has
progressed through three levels of investigation: metacog-
nitiveknowledge(can the model identify what a task re-
quires?), metacognitivemonitoring(can the model judge
whether it will succeed?), and metacognitivecontrol(can
the model act on those judgments to regulate its behav-
ior?). Existing work has made progress on the first two;
the third remains untested because no current evaluation
forces a model to commit, in advance, to a portfolio of tasks
under a shared budget – a regime where control becomes
operationally distinct from monitoring.
Metacognitive knowledge and monitoring.Kadavath
et al. (2022) provided the foundational result on monitoring,
showing that LLMs can predict which questions they will
answer correctly, with calibration improving at scale. Di-
dolkar et al. (2024) demonstrated that LLMs also possess
metacognitiveknowledge: given a math problem, frontier
models can assign meaningful skill labels and use skill-
matched exemplars to improve reasoning, establishing that
models can assess task properties. Xiong et al. (2024) sys-
tematically benchmarked confidence elicitation methods
and found that LLMs are consistently overconfident when
verbalizing confidence, though both calibration and failure
prediction improve with scale. Wang et al. (2025a) formal-
ized the separation of metacognitive ability from raw cogni-
tive ability via their DMC framework, finding that stronger
LLMs exhibit stronger metacognition and that enhancing
metacognition alleviates hallucination. At the mechanistic
level, Ji-An et al. (2025) demonstrated that LLMs can moni-
tor and control a low-dimensional subspace of their internal
activations via a neurofeedback paradigm – direct evidence
of metacognitive access to internal states, though limited
to concurrent activations rather than prospective task-level
judgments.
These results are counterbalanced by evidence of system-
atic failure. Kapoor et al. (2024) showed that verbalized
confidence is poorly calibrated for open-ended generation
and that a classifier trained on internal features substantially
outperforms prompting – implying that metacognitive moni-
toring is latent in representations but not reliably accessible
through natural outputs. Griot et al. (2025) found that LLMs
provide confident answers to medical questions even when
correct options are entirely absent, revealing a disconnect
2

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
between stated confidence and actual capability.
Ackerman (2026) used behavioral paradigms where the
model must decide before answering whether to attempt
or defer (the Delegate Game) and found only rudimentary,
context-dependent metacognition that depends on training
regimen rather than scale. Steyvers & Peters (2025) orga-
nize these mixed findings by distinguishing metacognitive
sensitivity(ranking own performance across items) fromcal-
ibration(matching confidence to success rate), noting that
the two can vary independently and that neither is reliably
strong across models and domains.
From monitoring to control.The work above measures
whether models can assess their own capabilities. Real de-
ployment requiresactingon those assessments to allocate
resources. The closest prior work to ours is Barkan et al.
(2025), who explicitly distinguish in-advance from after-
the-fact confidence and test prospective self-assessment on
coding and agentic tasks (SWE-Bench Verified). They find
that frontier models are systematically overconfident, and
that neither scale nor reasoning augmentation improves pre-
diction accuracy. Their resource-acquisition experiment -
accepting or declining sequential work contracts at varying
cost - is the nearest existing analog to budget-constrained
decision-making. But this evaluation design - sequential,
independent accept/reject decisions - by construction can-
not expose the combinatorial problem of jointly selecting,
allocating, and ordering under a shared budget, where at-
tempting one problem reduces what remains for all others.
AbstentionBench (Kirichenko et al., 2025) scales the moni-
toring question to a benchmark setting, testing whether mod-
els abstain from unanswerable questions across 20 datasets
and finding that reasoning fine-tuning degrades abstention
by ∼24%. Their unanswerable variants of existing bench-
marks inform our unsolvable-injection experiment. But
abstention there is a property of thequestion- some are
answerable, others are not. In TRIAGE, the relevant prop-
erty is themodel–task–budget triple: a problem may be
answerable in principle but not by this model under this
budget.
Across this literature, a consistent picture emerges: LLMs
possess metacognitive knowledge and some monitoring abil-
ity, but both are contested in degree and fragile across do-
mains. More critically, all existing evaluations operate one
task at a time. The portfolio-level version of the problem is
harder - accurate monitoring of any one task is necessary
but not sufficient, because the model must also compare
feasibility and cost across tasks while respecting a shared
constraint. Whether current models can make this transi-
tion from single-task monitoring to portfolio-level resource
allocation is what TRIAGE is designed to test.
2.2. Compute Allocation for LLM Reasoning
The test-time compute scaling paradigm (Snell et al., 2025)
has made compute allocation a practical problem. Reason-
ing models overthink trivial problems (Chen et al., 2024),
underthink hard ones (Wang et al., 2025b), and in agen-
tic settings exhibit analysis paralysis that correlates with
decreased performance (Cuadron et al., 2025). Existing
methods address this waste, but split on who allocates and
at what granularity, and neither side covers the full problem.
On the self-assessed side, TALE (Han et al., 2025) has the
LLM estimate its own token cost before solving a problem,
and SelfBudgeter (Li et al., 2025) trains the model to emit a
budget before its chain of thought. Both are prospective and
self-assessed, but per-task: the model decides how long to
spend, never whether to attempt at all, and there is no shared
budget linking decisions across tasks. On the systems side,
external predictors schedule LLM inference for throughput
- via length-bucket classification (Jin et al., 2023), listwise
ranking (Fu et al., 2024), or interval prediction under un-
certainty (Chen et al., 2025). These operate at the portfolio
level, but the predictor is external to the LLM, the objective
is latency, and the model’s own judgment of what it can
solve plays no role.
Existing benchmarks test related but distinct capabilities.
PlanBench (Valmeekam et al., 2023) evaluates whether
LLMs can produce valid plans in classical planning domains,
with automated ground-truth validation via external solvers
- but tests planexecution, not prospective self-assessment of
which plans will succeed. τ-bench (Yao et al., 2024) intro-
duces tool-call interactions as a measurable resource axis for
agent evaluation, and GAIA (Mialon et al., 2024) provides
a heterogeneous, difficulty-leveled agent benchmark with
validated ground truth. Both motivate the agentic extension
of TRIAGE but neither tests whether the agent can plan its
own workload efficiently under finite resources.
These two literature meet at a measurement gap. Single-task
confidence benchmarks isolate monitoring; external sched-
ulers isolate allocation; neither evaluates the joint capability
that deployment actually requires. TRIAGE is designed to
close this gap as an evaluation. The model produces a plan
- selecting tasks, estimating costs, and ordering execution
- which we score by simulating its consequences against
pre-computed ground truth, yielding a single, falsifiable
measure of the joint product of metacognitive monitoring
accuracy and planning quality under a binding budget. We
design a portfolio-level test in which accurate per-task self-
assessment is necessary but not sufficient, because the model
must also compare feasibility and cost across tasks while
respecting a shared constraint.
3

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
3. TRIAGE Framework
3.1. Prospective Metacognitive Control
Effective problem-solving under constraint requires more
than the capacity to execute individual tasks; it requires
metacognitive control over how that capacity is deployed,
and for an agent operating under a finite execution budget,
that control is exercised as prospective planning: a com-
mitment, made before any problem is attempted, to which
problems will be pursued, in what order, and how much
of the budget each will receive. Cognitive psychology dis-
tinguishes anobject level, where a task is executed, from
ameta level, which monitors the object level and exerts
control over it (Nelson & Narens, 1990; Koriat & Gold-
smith, 1996). Two control functions of the meta level, what
to attempt and how long to persist on what is attempted,
are the levers behind human study-time allocation (Son &
Metcalfe, 2000; Metcalfe & Kornell, 2005) and test-taking
strategy (Ackerman & Goldsmith, 2011). We benchmark
these levers in language models.
Metacognitive judgments partition by their position in the
execution timeline (Dunlosky & Metcalfe, 2009): prospec-
tive, formed before execution; concurrent, formed during;
and retrospective, formed after. We focus on the prospective
class, Ease-of-Learning judgments in the laboratory (Under-
wood, 1966; Leonesio & Nelson, 1990), initial test plans in
applied settings, for three independent reasons.
Methodological isolation. Once feedback is allowed dur-
ing execution, observed performance reflects an
unidentifiable mixture of prospective judgment quality
and adaptive replanning; the two cannot be separated
post-hoc. Studying prospective judgments without in-
tervening feedback is the established technique for
isolating the construct in human work (Mazzoni &
Cornoldi, 1993; Son, 2004).
Deployment realism. A growing class of LLM-driven sys-
tems commits to a task-level plan over a heterogeneous
set of subtasks before any one is attempted. Deep re-
search agents decompose a query into sub-questions
and dispatch them across parallel sub-agents, each run-
ning with its own context window and token budget
that the orchestrator cannot revise once dispatched (Lin
et al., 2026). Coding agents process queues of bug
reports or pull-request issues under per-issue token
budgets, where wasted attempts on infeasible items
measurably degrade overall throughput (Jimenez et al.,
2024). In both cases the quality of the upfront plan,
what to attempt, in what order, with what allocation,
determines whether the run completes usefully or ex-
hausts its budget on the wrong items.
Construct priority. A model that revises its plan mid-
execution is only useful if its initial plan is any
good (Thiede & Dunlosky, 1999). To measure what
mid-execution adjustments add, we first need a clean
measurement of the up-front plan in isolation, and that
requires evaluating planning without any feedback dur-
ing execution.
Tokens as the control variable.Classical study-
allocation work uses time as the meta-level control variable.
In autoregressive language models, output tokens are the
natural unit of expended effort: generation time, compute,
and monetary cost are all approximately proportional to
token count, and the central paradigm of test-time compute
scaling treats per-problem token allocation as the system’s
primary lever for adapting to problem difficulty (Snell et al.,
2025; Han et al., 2025). Tokens are therefore the operational
analog of time in study-allocation theory, with the additional
property of being exactly measurable.
Distributional self-knowledge and binding plans.Com-
mon agent pipelines generally decouple planning from
execution into separate inference calls over identical
weights (Xu et al., 2023). The planner does not introspect on
an ongoing computation; it predicts the behavior of a same-
weights solver under standard execution conditions. We
treat this as the deployment-relevant form of self-modeling.
The plan is moreoveroperationally binding: at execution
time, per-problem token allocations from the plan can be
enforced as binding constraints on the solver, converting
the plan from a forecast into a self-commitment and testing
whether the model can satisfy a budget it set for itself; we
study this enforced setting alongside the unconstrained one
as a secondary regime (§3.2).
Four primitives.Prospective metacognitive control under
a finite execution budget reduces to four jointly exercised
judgments: (i)feasibility, whether the model can solve the
problem? (ii)cost, how many tokens will it take? (iii)
selection, which subset to attempt? and (iv)sequencing,
in what order, given that budget exhaustion truncates the
tail? Existing LLM benchmarks isolate slices of this set:
per-item confidence calibration covers (i) (Barkan et al.,
2025); abstention covers a hard form of (i) without a bud-
get (Kirichenko et al., 2025); per-task budget control covers
(ii) for a single item (Li et al., 2025). TRIAGE measures the
joint exercise of all four primitives under a finite budget.
3.2. Problem Formulation
We formalize TRIAGE for a singletask pool, a finite set of
problems sharing a domain and a budget, the unit of work
the agent commits to in a single planning step before any
execution feedback arrives.
4

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Setup.A task pool P={p 1, . . . , pn} contains finitely
many problems. For each problem pi and a fixed solver
model M: vi ∈R >0 is the point value, observable to M;
yi ∈ {0,1}indicates whether M solves pi under standard ex-
ecution, unobservable to M at planning time; and ci ∈R >0
is the output-token cost M incurs when attempting pi, also
unobservable at planning time. Both yi and ci are properties
of the (problem, solver) pair, determined empirically by
runningMonp i once at temperature0.
Budget.The budget is B(M, α) =⌊α·Pn i=1 ci⌋ with α∈
(0,1] ; the floor reflects that token counts are integer-valued.
The factor α <1 forces selection by setting the budget
below the solver’s full baseline cost; α= 1 supplies the full
baseline budget, in which selection pressure is reduced but
the model must still identify which items it can solve, since
omissions result in forfeiting value.
Action.The model produces an ordered plan π=
(i1, . . . , ik) with 0≤k≤n , indexing a selected subset
S={i 1, . . . , ik} ⊆ {1, . . . , n}, together with per-problem
allocations aij ∈R ≥0 satisfying P j aij ≤B . The plan thus
jointly encodes selection, sequencing, and forecast.
Execution.Plans are executed in plan order under one
of two regimes, which differ in whether the per-problem
allocationsa i are binding.
Unconstrained regime (U).The solver runs each problem to
its natural completion at the cost ci; only the global budget
B binds. Execution proceeds through π until reaching an
item whose true cost exceeds the remaining budget, at which
point execution stops. Problem ij contributes vij yij to the
achieved value if executed, and zero otherwise.
Constrained regime (E).Each problem ij is executed with
a hard token limit aij at the solver: if the solver completes
within aij , the outcome is the result under that limit; oth-
erwise the attempt scores zero. The full allocation aij is
deducted from the remaining budget regardless of outcome,
and execution proceeds through π until reaching an item
whose allocation exceeds the remaining budget, at which
point execution stops.
The two regimes isolate distinct components of the meta-
level control problem (Nelson & Narens, 1990). Regime U
probesprospective monitoring: the planner’s predictions
of (yi, ci) surface only through which items it selects and
in what order, since allocations are advisory; truncation
discipline comes entirely from ordering quality. Regime E
probesprospective controlin the strict sense: per-problem
allocations are binding, so the model is held to commitments
it makes to itself. We write VM (π) for the achieved value at
termination under whichever regime is in force, and report
results in both.
Measuring triage skill.We need a single scalar that cap-
tures how well the planner’s committed plan π acts on its
(unobserved) knowledge of (yi, ci) under the budget B. A
raw value comparison VM (π) is uninformative on its own -
its magnitude depends on pool difficulty and on B, which
vary across cells. The standard device in forecast verifi-
cation (Murphy, 1973) and in selective-prediction evalua-
tion (Geifman & El-Yaniv, 2017) is tonormalizethe sys-
tem’s achieved value between a reference that uses no privi-
leged knowledge and an oracle that uses all of it. We adopt
that construction here.
Oracle and random references.Theoracleis a planner
with full knowledge of (yi, ci) for every i. Its achievable
value is
Voracle = max x∈{0,1}n
nX
i=1
vi yi xi s.t.
nX
i=1
ci xi ≤B,
(1)
a 0–1 knapsack - each problem is either included (xi = 1) or
omitted (xi = 0), with no fractional attempts (Kellerer et al.,
2004). Therandomreference Vrandom is the expected value of
a feasible plan obtained without any self-knowledge, drawn
uniformly without replacement subject to remaining-budget
feasibility; we report the mean over10 3 such samples.
Triage efficiency ratio.The triage efficiency ratio nor-
malizes the model’s achieved value between these two refer-
ences:
ηM = VM (π)−V random Voracle −V random .(2)
On the standard interpretation, ηM = 0corresponds to no
use of self-knowledge and ηM = 1to the value attainable
with perfect self-knowledge; intermediate values report frac-
tional skill on the random-to-oracle scale. Negative values
indicate plans worse than uninformed random selection, an
anti-skill signal under tight budgets, indicating the planner’s
choices systematically picked items that didn’t fit the bud-
get or weren’t solvable. Pools with Voracle = 0(no problem
in the pool is solvable by the model) are out of scope for
triage measurement and excluded; we discuss the boundary
behaviour ofη M in Appendix D.
Uniform values: preventing difficulty leakage.The
main protocol fixes vi = 1. Any vi correlated with em-
pirical difficulty would let the planner read difficulty off
the prompt rather than estimate it from problem content,
and language models are known to exploit such surface
cues when present (Koriat, 1997; Tang et al., 2023). Under
uniform v, the oracle objective simplifies: Voracle equals the
maximum number of solvable items (yi = 1) whose costs
fit within B. Let S⋆ ={i:y i = 1}and let i(1), i(2), . . .index
5

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
S⋆ in ascending order ofc i; then
Voracle = max
n
m

 mX
j=1
ci(j) ≤B
o
.(3)
The model receives only problem text and must form its plan
without observing (yi, ci). Differences in η between models
therefore reflect differences in their implicit predictions
of (yi, ci), not differences in optimization: the oracle, the
random reference, and the execution rule are identical across
models. Thus we measure the model’s prediction of its
own future behavior, with the oracle playing the role of an
ideal forecaster, as in selective-prediction evaluation more
broadly (Geifman & El-Yaniv, 2017).
4. Experimental Setup
Models.We evaluate 20 model architectures spanning
frontier and open-source families (Qwen 2.5/3/3.5, GPT-
OSS, Claude, DeepSeek, Gemini, GLM, GPT-5, Kimi),
with reasoning enabled and disabled where supported. Full
model identifiers, providers, parameter counts, and reason-
ing configurations are listed in Table 4 (Appendix E).
Datasets and task pools.We construct task pools from
four domains: competition mathematics (AIME 2024–
2025), graduate-level science (GPQA Diamond (Rein et al.,
2024)), code generation (LiveCodeBench (Jain et al., 2024),
filtered to contests from 2025 onward to reduce contami-
nation risk from problems that may appear in pre-training
data), and multidisciplinary expert knowledge (Humanity’s
Last Exam (Phan et al., 2025), excluding image-bearing
items and topic categories overlapping with the other three
datasets). Each dataset is partitioned into independent task
pools of nchunk = 30problems to fit within planner context
limits and avoid the long-context degradation reported in
prior work (Liu et al., 2024). Each pool has its own budget,
oracle, and random reference, andη is averaged across pools
within each(dataset, α)cell.
To probe sensitivity to infeasible items, we addi-
tionally inject unsolvable problems from Abstention-
Bench (Kirichenko et al., 2025) (GPQA-Abstain and
MMLU-Math-Abstain) into pools at varying ratios.
Phase 0: baseline measurement.We first run each model
on every problem once, in an isolated session at tempera-
ture 0, to record its baseline output-token cost ci and cor-
rectness yi. These two quantities serve two purposes: ci
calibrates the per-pool budget Blocal =⌊α P i ci⌋ given to
the planner in Phase 1, and (ci, yi) together provide the
ground truth against which the oracle andηare computed.
Phase 1: planning.The planner receives problem texts,
point values ( vi = 1 ), the per-pool budget Blocal =
⌊α P i∈pool ci⌋, and instructions to return an ordered plan
with per-problem token allocations summing to at most
Blocal. The full prompt template is given in Appendix B. A
prompt sensitivity analysis is available in C.2 and shows
robustness under prompt variations.
Phase 2: execution.Plans are executed under both
regime U and regime E (§3.2), under same configuration so
that observed differences in η reflect planning quality rather
than solver stochasticity.
Budget conditions.We sweep α∈ {0.25,0.5,0.75,1.0}
to vary selection pressure from severe to slack. Main results
reportα= 0.5, under 50% budget constraint.
Metric.We report triage efficiency ηM (§3.2) as the
primary metric and normalized regret ˜RM = (V oracle −
VM )/Voracle ∈[0,1] as a bounded alternative for robustness
(Appendix D.5); lower ˜RM is better. The random reference
Vrandom is estimated by drawing 103 uniform shuffles of the
gradeable items per pool and executing each under regime-
U rules - the same execution rule used to score model plans,
ensuring ηM measures the value added by self-knowledge
over uninformed random selection.
For the unsolvable-injection probe, we additionally report
waste rate W= P i∈S∩U ai / P i∈S ai, the fraction of allo-
cated tokens spent on unsolvable items, anddetection rate
D=|U\S|/|U| , the fraction of unsolvable items correctly
excluded from the plan, where S={i:a i >0} is the
planned set and U the injected unsolvable items in the pool.
5. Results
5.1. Triage at moderate budget
Figures 1 and 2 report triage at α= 0.5, where the budget
covers half the items’ baseline costs and selection genuinely
matters. We report both metrics: η measures how much of
the gap between an oracle planner and a random planner
the model recovers, while ˜R measures the absolute frac-
tion of oracle value the model fails to capture and remains
well-defined whenever Voracle >0 . The main findings are
described below.
Advisory triage does not transfer across benchmarks.
ηU in Figure 1 varies sharply across (model, dataset) pairs
and no configuration ranks at the top on all four benchmarks.
Configurations that achieve high advisory efficiency on one
or two datasets frequently drop near or below random on the
others, showing that the ability to identify worthwhile items
in one domain does not carry over reliably. Strong advisory
performance is also decoupled from raw solve rate: several
configurations attain high ηU and low advisory regret ˜RU
on datasets where their base accuracy is low, indicating
6

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
1.0
0.0
0.5
1.0
AIME
oracle
random
1.0
0.0
0.5
1.0
GPQA
oracle
random
1.0
0.0
0.5
1.0
LCB
oracle
random
Qwen 2.5 3BQwen 2.5 7BQwen 2.5 14BQwen 2.5 32B Qwen 3 4BQwen 3 8BQwen 3 14BQwen 3 32BQwen 3.5 4BQwen 3.5 9BQwen 3.5 27B
Qwen 3.5 35B-A3BClaude Haiku 4.5
DeepSeek V3
Gemini 2.5 Flash
GLM 5.1 GPT-5 Mini Kimi K2.5
GPT-OSS 20BGPT-OSS 120B
1.0
0.0
0.5
1.0
HLE
oracle
random
Reasoning mode
standard inference extended reasoning
Reasoning mode
standard inference extended reasoning
Metric
accuracy (dashed line) solid bar = U
 hatched bar = E
Figure 1:Triage efficiency across models and benchmarks at moderate budget ( α= 0.5 ).Solid bars show ηU
(unconstrained regime, advisory allocations), hatched bars show ηE (constrained regime, binding allocations), and red
dashed lines mark base accuracy. η= 1 is oracle triage; η= 0 is random; η <0 is worse than random. Bar color
distinguishes standard inference from extended reasoning.
accurate self-assessment over a small set of feasible items.
Binding the budget breaks triage.The gap between ηU
(solid) and ηE (hatched) in Figure 1 is the most consistent
pattern across models. At α= 0.5, ηE is negative for the
large majority of configurations, and a substantial fraction
reach ˜RE near the full-regret bound in Figure 2, meaning the
model captures essentially no value once its own per-item
allocations are enforced. The collapse is sharpest on the
reasoning-heavy benchmarks (AIME, GPQA, LCB), where
binding the budget cuts off solver outputs before they can
produce an answer. HLE is the only benchmark where any
extended-reasoning configuration attains clearly positiveηE.
A controlled re-solve experiment confirms this behaviorally:
models rarely honor the budgets they themselves declare
even when explicitly instructed to (Appendix C.1).
Plans and execution diverge under enforcement.
Across all 30 configurations evaluated, only one (Gemini
2.5 Flash in standard inference) achieves positive ηE on
every benchmark, and only two (Gemini 2.5 Flash standard
and Qwen 3.5 27B standard) achieve ˜RE <0.5 on more
than one benchmark. Both belong to the standard-inference
variant of their respective model. Within paired-mode com-
parisons, the standard variant achieves a lower enforced-
regime regret than its extended-reasoning counterpart on
the majority of datasets, indicating that extended reasoning
tends to produce longer outputs that exceed the planner’s
own allocations and so collapse under enforcement.
Extended reasoning lifts accuracy without consistently
lifting triage.Within the paired-mode models, base ac-
curacy (red dashed line) increases with extended reasoning
on most (model, dataset) pairs, and on some datasets the
lift is large. Advisory regret ˜RU , however, follows no such
pattern: extended reasoning leaves it essentially unchanged
or worsens it on roughly half of paired configurations. The
pattern that does emerge consistently is the failure mode
of the previous paragraph: extended reasoning enlarges the
gap between the advisory and enforced regimes, because
longer traces are less likely to fit within the model’s own
allocation. Object-level capability and metacognitive con-
trol thus dissociate empirically: a longer trace can solve
more problems without making the planner any better at
deciding which ones to attempt, and can substantially hurt
the planner’s ability to execute within its own budget.
Triage quality does not scale with parameter count.
Within Qwen 2.5, the largest 32B model is the worst on
GPQA in the entire family and the family shows no upward
trend with size on either GPQA or LCB. Within Qwen 3.5,
the dense 27B beats the larger mixture-of-experts variant
in standard mode on every benchmark. Among GPT-OSS,
the 120B underperforms the 20B by a wide margin on LCB.
No family in our evaluation exhibits a clean upward trend
across all four benchmarks. Triage quality, as measured
here, does not follow the standard scaling trends observed
for raw accuracy, and may require capabilities that grow
only weakly, or not at all, with parameter count.
7

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
0.0
0.5
1.0
AIME
full regret
oracle
0.0
0.5
1.0
GPQA
full regret
oracle
0.0
0.5
1.0
LCB
full regret
oracle
Qwen 2.5 3BQwen 2.5 7BQwen 2.5 14BQwen 2.5 32B Qwen 3 4BQwen 3 8BQwen 3 14BQwen 3 32BQwen 3.5 4BQwen 3.5 9BQwen 3.5 27B
Qwen 3.5 35B-A3BClaude Haiku 4.5
DeepSeek V3
Gemini 2.5 Flash
GLM 5.1 GPT-5 Mini Kimi K2.5
GPT-OSS 20BGPT-OSS 120B
0.0
0.5
1.0
HLE
full regret
oracle
Reasoning mode
standard inference extended reasoning
Reasoning mode
standard inference extended reasoning
Metric
accuracy (dashed line) solid bar = RU (advisory)
 hatched bar = RE (enforced)
Figure 2:Normalized triage regret across models and benchmarks at moderate budget ( α= 0.5).Solid bars show
˜RU = (Voracle −V U )/Voracle (unconstrained regime), hatched bars show ˜RE (constrained regime), and red dashed lines
mark base accuracy. ˜R= 0is oracle (no value lost); ˜R= 1is full regret (no value captured). Lower is better.
Behavior across budget pressure.Full per-(model, α,
dataset) breakdowns appear in the appendix: accuracy in
Figure 4, advisory-regime efficiency ηU in Figure 5, and
enforced-regime efficiency ηE in Figure 6; per-α versions
of Figures 1 and 2 are in Figure 5. The findings at α= 0.5
are broadly stable across the other budget levels we evaluate:
the same configurations retain advisory-regime leadership
on multiple benchmarks, and the ηU -ηE gap persists at ev-
ery budget, with enforced efficiency remaining negative for
most configurations on the reasoning-heavy benchmarks.
At α= 1.0 the efficiency metric saturates because the
oracle-random gap approaches zero in many configurations,
whereas the regret formulation remains numerically stable
there. Across the models and benchmarks we evaluate, no
single configuration is simultaneously a strong monitor and
a strong controller on more than one benchmark. Prospec-
tive metacognitive control, in the joint sense of §3.1, remains
an open capability gap.
5.2. Recognizing Unsolvable Problems
Effective planning requires recognizing tasks that cannot
be solved. Tokens spent on an unsolvable task produce no
reward and reduce the budget available for solvable ones,
so the ability to identify and exclude infeasible items is
itself a metacognitive skill worth measuring. We probe
sensitivity to infeasible items of selected models by injecting
unsolvable problems from AbstentionBench (Kirichenko
et al., 2025) (GPQA-Abstain, MMLU-Math-Abstain) into
the GPQA and MMLU-Math pools at substitution ratios
r∈ {0,0.25,0.50,0.75,1.00} , holding pool size constant.
We report detection rateD (fraction of unsolvables correctly
left out of the plan) and waste rate W (fraction of the plan’s
tokens spent on unsolvables); see §4. Figure 3 traces each
ablation model through (D, W)space; the main findings
are described below.
Recognition of unsolvables splits the cohort.Two mod-
els recognize unsolvables consistently across injection ra-
tios: Gemini 2.5 Flash, whose detection stays in [0.60,0.79]
across all ratios on both datasets, and Qwen 2.5 32B, whose
detection stays at or above 0.33 across all ratios. The re-
maining two models – Qwen 3 32B and GPT-OSS 20B, both
reasoning-trained – detect substantially fewer unsolvables.
Their detection lies in [0.00,0.30] on GPQA-Abstain across
all ratios. On MMLU-Math-Abstain, GPT-OSS 20B’s de-
tection remains below 0.13 at every ratio (max 0.127 at
r= 0.50 ), while Qwen 3 32B’s detection declines mono-
tonically from 0.54 at r= 0.25 to 0.07 at r= 1.0 . The
Qwen pair provides the cleanest within-family compari-
son: under standard inference, the model recognizes the
majority of unsolvables at low injection (D= 0.67 GPQA,
0.88 MMLU-Math at r= 0.25); under extended reasoning,
the same architecture detects substantially less (D= 0.08
GPQA, 0.54 MMLU-Math at the same r= 0.25 ). The
within-Qwen pattern reproduces under portfolio planning
what Kirichenko et al. (2025) report for isolated abstention –
that reasoning training can reduce sensitivity to infeasibil-
ity. We note that this is a within-family effect: Gemini 2.5
Flash, also reasoning-augmented, retains detection across
8

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
0.00 0.25 0.50 0.75 1.00
Detection rate  D   better
0.00
0.25
0.50
0.75
1.00
 better  Waste rate  W
ideal
(high D, low W)
GPQA-Abstain
0.00 0.25 0.50 0.75 1.00
Detection rate  D   better
0.00
0.25
0.50
0.75
1.00
ideal
(high D, low W)
MMLU-Math-Abstain
Gemini 2.5 Flash (think) Qwen 2.5 32B Qwen 3 32B (think) GPT-OSS 20B (think) injection ratio
r = 0.25 r = 0.5 r = 0.75 r = 1.0
Gemini 2.5 Flash (think) Qwen 2.5 32B Qwen 3 32B (think) GPT-OSS 20B (think) injection ratio
r = 0.25 r = 0.5 r = 0.75 r = 1.0
Figure 3:Trajectories through (D, W)space as the unsolvable-injection ratio r increases from 0.25 to 1.00 (marker
size).The star marks the ideal corner: high detection rate, low waste rate.
the range, suggesting the relationship between reasoning
training and abstention is not uniform across models.
The dependence of detection on injection ratio.We
characterize each model by how its detection rate varies
with the injection ratio. Gemini’s detection is approxi-
mately invariant to injection: it spans 0.05 on MMLU-
Math-Abstain and 0.19 on GPQA-Abstain across the four
non-trivial ratios. Qwen 2.5 32B’s detection declines mono-
tonically with injection on MMLU-Math-Abstain (0.88→
0.67→0.58→0.40 ) but follows a non-monotonic course
on GPQA-Abstain (sharp drop after r= 0.25, then approx-
imately flat). The two reasoning-trained models hold de-
tection rate below 0.50 across every cell on GPQA-Abstain
and at every r≥0.75 on MMLU-Math-Abstain, indicating
allocations that largely fail to distinguish unsolvable items
from solvable ones.
Cross-domain consistency of detection.Three of four
models detect unsolvables more reliably on the math-derived
dataset than on the science-derived one, with mean differ-
ences of +0.19 (Qwen 2.5 32B) and +0.32 (Qwen 3 32B).
Gemini’s gap is small ( +0.04). GPT-OSS 20B is the ex-
ception: its detection is uniformly low on both datasets,
with a mean difference of −0.03, leaving no informative
comparison.
Full injection isolates detection from solving ability.At
full injection every item is infeasible and the optimal plan is
empty, so solving ability cannot contribute to detection. The
cohort split persists. Gemini continues to exclude roughly
three-quarters of items from the plan ( D= 0.73 GPQA,
0.76 MMLU-Math at r= 1.0); Qwen 2.5 32B excludes a
non-trivial fraction (D= 0.40 on both); the two reasoning-
trained models exclude almost none (D <0.08 in all four
cells), continuing to allocate budget under conditions where
any allocation is wasted by construction. Full injection also
partially removes between-domain difficulty as a source of
variance, leaving the model’s tendency to commit budget
under certain failure as the main residual axis distinguishing
the cohort.
6. Conclusion
Deploying language models as autonomous agents re-
quires a capability that single-task evaluation does not test:
prospective metacognitive control over which problems to
attempt, in what order, and with what allocation, committed
before any execution feedback. TRIAGE evaluates this ca-
pability by scoring committed plans against an oracle with
full knowledge of model-specific solvability and cost.
Across 20 models and four domains, object-level capability
and metacognitive control dissociate. Extended reasoning
improves accuracy without improving triage efficiency. Self-
assessment does not transfer reliably across domains. Mod-
els select which problems to attempt more reliably than they
commit token budgets they can honor under enforcement.
Reasoning training reduces, rather than improves, sensitivity
to infeasible items at the portfolio level. Because the failure
is prospective, execution-time monitoring cannot repair it.
Reliable upfront planning is therefore a prerequisite, not a
refinement, for agents that allocate their own compute under
finite resources.
9

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Impact Statement
This paper presents work whose goal is to advance the field
of Machine Learning. There are many potential societal
consequences of our work, none which we feel must be
specifically highlighted here.
References
Ackerman, C. Evidence for limited metacognition in LLMs. In
The Fourteenth International Conference on Learning Repre-
sentations (ICLR), 2026. arXiv:2509.21545.
Ackerman, R. and Goldsmith, M. Metacognitive regulation of
text learning: On screen versus on paper.Journal of Ex-
perimental Psychology: Applied, 17(1):18–32, 2011. doi:
10.1037/a0022086.
Alomrani, M. A., Zhang, Y ., Li, D., Sun, Q., Pal, S., Zhang, Z.,
Hu, Y ., Ajwani, R. D., Valkanas, A., Karimi, R., Cheng, P.,
Wang, Y ., Liao, P., Huang, H., Wang, B., Hao, J., and Coates, M.
Reasoning on a budget: A survey of adaptive and controllable
test-time compute in LLMs.arXiv preprint arXiv:2507.02076,
2025.
Barkan, C. O., Black, S., and Sourbut, O. Do large language
models know what they are capable of?arXiv preprint
arXiv:2512.24661, 2025. NeurIPS 2025 Workshop on Evaluat-
ing the Evolving LLM Lifecycle.
Chen, X., Xu, J., Liang, T., He, Z., Pang, J., Yu, D., Song, L., Liu,
Q., Zhou, M., Zhang, Z., Wang, R., Tu, Z., Mi, H., and Yu, D.
Do NOT think that much for 2+3=? On the overthinking of
o1-like LLMs.arXiv preprint arXiv:2412.21187, 2024.
Chen, Z., Ye, Y ., and Zhou, Z. Adaptively robust LLM infer-
ence optimization under prediction uncertainty.arXiv preprint
arXiv:2508.14544, 2025.
Cuadron, A., Li, D., Ma, W., Wang, X., Wang, Y ., Zhuang, S., Liu,
S., Schroeder, L. G., Xia, T., Mao, H., Thumiger, N., Desai,
A., Stoica, I., Klimovic, A., Neubig, G., and Gonzalez, J. E.
The danger of overthinking: Examining the reasoning-action
dilemma in agentic tasks.arXiv preprint arXiv:2502.08235,
2025.
Didolkar, A., Goyal, A., Ke, N. R., Guo, S., Valko, M., Lilli-
crap, T., Rezende, D., Bengio, Y ., Mozer, M., and Arora, S.
Metacognitive capabilities of llms: An exploration in math-
ematical problem solving.Advances in Neural Information
Processing Systems, 37:19783–19812, 2024.
Dunlosky, J. and Metcalfe, J.Metacognition. SAGE Publications,
Thousand Oaks, CA, 2009. ISBN 9781412939720.
Fu, Y ., Bailis, P., Stoica, I., and Zhang, H. Efficient LLM schedul-
ing by learning to rank. InAdvances in Neural Information
Processing Systems, volume 37, 2024. arXiv:2408.15792.
Geifman, Y . and El-Yaniv, R. Selective classification for deep
neural networks. InAdvances in Neural Information Processing
Systems, volume 30, 2017.
Griot et al. Large language models lack essential metacognition
for reliable medical reasoning.Nature Communications, 16:
642, 2025. doi: 10.1038/s41467-024-55628-6.
Han, T., Wang, Z., Fang, C., Zhao, S., Ma, S., and Chen, Z. Token-
budget-aware LLM reasoning. InFindings of the Association
for Computational Linguistics: ACL 2025, pp. 24842–24855,
2025. doi: 10.18653/v1/2025.findings-acl.1274.
Jain, N., Han, K., Gu, A., Li, W.-D., Yan, F., Zhang, T., Wang,
S., Solar-Lezama, A., Sen, K., and Stoica, I. LiveCodeBench:
Holistic and contamination free evaluation of large language
models for code.arXiv preprint arXiv:2403.07974, 2024.
Ji-An, L., Xiong, H.-D., Wilson, R. C., Mattar, M. G., and Benna,
M. K. Language models are capable of metacognitive moni-
toring and control of their internal activations.arXiv preprint
arXiv:2505.13763, 2025.
Jimenez, C. E., Yang, J., Wettig, A., Yao, S., Pei, K., Press, O., and
Narasimhan, K. R. SWE-bench: Can language models resolve
real-world GitHub issues? InThe Twelfth International Confer-
ence on Learning Representations (ICLR), 2024. URL https:
//openreview.net/forum?id=VTF8yNQM66.
Jin, Y ., Wu, C.-F., Brooks, D., and Wei, G.-Y . S3: Increasing GPU
utilization during generative inference for higher throughput. In
Advances in Neural Information Processing Systems, volume 36,
2023. arXiv:2306.06000.
Kadavath, S., Conerly, T., Askell, A., Henighan, T., Drain, D.,
Perez, E., Schiefer, N., Hatfield-Dodds, Z., DasSarma, N., Tran-
Johnson, E., Johnston, S., El-Showk, S., Jones, A., Elhage, N.,
Hume, T., Chen, A., Bai, Y ., Bowman, S., Fort, S., Ganguli, D.,
Hernandez, D., Jacobson, J., Kernion, J., Kravec, S., Lovitt, L.,
Ndousse, K., Olsson, C., Ringer, S., Amodei, D., Brown, T.,
Clark, J., Joseph, N., Mann, B., McCandlish, S., Olah, C., and
Kaplan, J. Language models (mostly) know what they know.
arXiv preprint arXiv:2207.05221, 2022.
Kapoor, S., Gruver, N., Roberts, M., Collins, K., Pal, A., Bhatt,
U., Weller, A., Dooley, S., Goldblum, M., and Wilson, A. G.
Large language models must be taught to know what they don’t
know. InAdvances in Neural Information Processing Systems,
volume 37, 2024.
Kellerer, H., Pferschy, U., and Pisinger, D.Knapsack Problems.
Springer, Berlin, Heidelberg, 2004. ISBN 978-3-540-40286-2.
doi: 10.1007/978-3-540-24777-7.
Kirichenko, P., Ibrahim, M., Chaudhuri, K., and Bell, S. J. Absten-
tionBench: Reasoning LLMs fail on unanswerable questions. In
Advances in Neural Information Processing Systems: Datasets
and Benchmarks Track, volume 38, 2025. arXiv:2506.09038.
Koriat, A. Monitoring one’s own knowledge during study: A
cue-utilization approach to judgments of learning.Journal of
experimental psychology: General, 126(4):349, 1997.
Koriat, A. and Goldsmith, M. Monitoring and control processes
in the strategic regulation of memory accuracy.Psychological
Review, 103(3):490–517, 1996. doi: 10.1037/0033-295X.103.3.
490.
Leonesio, R. J. and Nelson, T. O. Do different metamemory
judgments tap the same underlying aspects of memory?Journal
of Experimental Psychology: Learning, Memory, and Cognition,
16(3):464–470, 1990. doi: 10.1037/0278-7393.16.3.464.
Li, Z., Dong, Q., Ma, J., Zhang, D., Jia, K., and Sui, Z. SelfBud-
geter: Adaptive token allocation for efficient LLM reasoning.
arXiv preprint arXiv:2505.11274, 2025.
10

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Lieder, F. and Griffiths, T. L. Resource-rational analysis: Under-
standing human cognition as the optimal use of limited compu-
tational resources.Behavioral and Brain Sciences, 43:e1, 2020.
doi: 10.1017/S0140525X1900061X.
Lin, X., Liew, J. H., Savarese, S., and Li, J. W&D: Scaling parallel
tool calling for efficient deep research agents.arXiv preprint,
2026.
Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M.,
Petroni, F., and Liang, P. Lost in the middle: How language
models use long contexts.Transactions of the Association for
Computational Linguistics, 12:157–173, 2024.
Mazzoni, G. and Cornoldi, C. Strategies in study time alloca-
tion: Why is study time sometimes not effective?Journal of
Experimental Psychology: General, 122(1):47–60, 1993. doi:
10.1037/0096-3445.122.1.47.
Metcalfe, J. and Kornell, N. A region of proximal learning model
of study time allocation.Journal of Memory and Language, 52
(4):463–477, 2005. doi: 10.1016/j.jml.2004.12.001.
Mialon, G., Fourrier, C., Swift, C., Wolf, T., LeCun, Y ., and
Scialom, T. GAIA: A benchmark for general AI assistants. In
International Conference on Learning Representations, 2024.
Murphy, A. H. A new vector partition of the probability score.
Journal of Applied Meteorology, 12(4):595–600, 1973. doi:
10.1175/1520-0450(1973)012<0595:ANVPOT>2.0.CO;2.
Nelson, T. O. and Narens, L. Metamemory: A theoretical frame-
work and new findings. In Bower, G. H. (ed.),The Psychology of
Learning and Motivation, volume 26, pp. 125–173. Academic
Press, 1990.
Phan, L., Gatti, A., Han, Z., Li, N., Hu, J., Zhang, H., Zhang, C.
B. C., Shaaban, M., Ling, J., Shi, S., et al. Humanity’s last
exam.arXiv preprint arXiv:2501.14249, 2025.
Rein, D., Hou, B. L., Stickland, A. C., Petty, J., Pang, R. Y ., Dirani,
J., Michael, J., and Bowman, S. R. GPQA: A graduate-level
Google-proof Q&A benchmark. InConference on Language
Modeling (COLM), 2024.
Snell, C., Lee, J., Xu, K., and Kumar, A. Scaling LLM test-time
compute optimally can be more effective than scaling model pa-
rameters. InThe Thirteenth International Conference on Learn-
ing Representations (ICLR), 2025. Oral. arXiv:2408.03314.
Son, L. K. Spacing one’s study: Evidence for a metacognitive
control strategy.Journal of Experimental Psychology: Learning,
Memory, and Cognition, 30(3):601–604, 2004. doi: 10.1037/
0278-7393.30.3.601.
Son, L. K. and Metcalfe, J. Metacognitive and control strategies
in study-time allocation.Journal of Experimental Psychology:
Learning, Memory, and Cognition, 26(1):204–221, 2000. doi:
10.1037/0278-7393.26.1.204.
Steyvers, M. and Peters, M. A. K. Metacognition and uncer-
tainty communication in humans and large language mod-
els.Current Directions in Psychological Science, 2025. doi:
10.1177/09637214251391158.
Tang, R., Kong, D., Huang, L., and Xue, H. Large language
models can be lazy learners: Analyze shortcuts in in-context
learning. InFindings of the Association for Computational
Linguistics: ACL 2023, pp. 4645–4657, 2023. doi: 10.18653/
v1/2023.findings-acl.284.
Thiede, K. W. and Dunlosky, J. Toward a general model of self-
regulated study: An analysis of selection of items for study and
self-paced study time.Journal of Experimental Psychology:
Learning, Memory, and Cognition, 25(4):1024–1037, 1999. doi:
10.1037/0278-7393.25.4.1024.
Underwood, B. J.Experimental Psychology. Appleton-Century-
Crofts, New York, 2nd edition, 1966.
Valmeekam, K., Marquez, M., Olmo, A., Sreedharan, S., and
Kambhampati, S. PlanBench: An extensible benchmark for
evaluating large language models on planning and reasoning
about change. InAdvances in Neural Information Processing
Systems, volume 36, 2023. Datasets and Benchmarks Track.
Wang et al. Decoupling metacognition from cognition: A frame-
work for quantifying metacognitive ability in LLMs. InPro-
ceedings of the AAAI Conference on Artificial Intelligence, vol-
ume 39, 2025a. doi: 10.1609/aaai.v39i24.34723.
Wang, Y ., Liu, Q., Xu, J., Liang, T., Chen, X., He, Z., Song, L.,
Yu, D., Li, J., Zhang, Z., Wang, R., Tu, Z., Mi, H., and Yu, D.
Thoughts are all over the place: On the underthinking of o1-like
LLMs. InAdvances in Neural Information Processing Systems,
volume 38, 2025b. Spotlight. arXiv:2501.18585.
Xiong, M., Hu, Z., Lu, X., Li, Y ., Fu, J., He, J., and Hooi, B. Can
LLMs express their uncertainty? an empirical evaluation of
confidence elicitation in LLMs. InInternational Conference
on Learning Representations (ICLR), 2024. URL https://
arxiv.org/abs/2306.13063.
Xu, B., Peng, Z., Lei, B., Mukherjee, S., Liu, Y ., and Xu, D.
ReWOO: Decoupling reasoning from observations for efficient
augmented language models.arXiv preprint, 2023.
Yao, S., Shinn, N., Razavi, P., and Narasimhan, K. τ-bench:
A benchmark for tool-agent-user interaction in real-world do-
mains.arXiv preprint arXiv:2406.12045, 2024.
11

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
A. Limitations and Broader Impact
TRIAGE measures one specific competence - prospective, portfolio-level resource allocation under a hard shared budget -
and the design choices required to make this competence measurable bound what can be concluded from it.
Construct and design.TRIAGE operationalizes metacognitive control as a single up-front plan: the model commits to
selections, cost estimates, and an execution order before any task is attempted. This isolates prospective self-assessment
from in-the-loop revision, at the price of excluding settings where allocation is naturally interactive or streaming. We treat
this trade as deliberate - the construct is most informative when revision is unavailable - but TRIAGE scores should not be
read as a global verdict on a model’s resource-allocation ability across deployment regimes. The budget is also denominated
in a single resource per track (token cost in the reasoning track, tool calls in the agentic track); evaluations conditioned on
wall-clock latency, monetary cost, or compound resources may rank models differently.
Ground truth and measurement noise.Per-task feasibility and cost are pre-computed by running each model on each item
once, at temperature 0, prior to evaluation. This makes per-cell outcomes approximately deterministic at the provider/runtime
level, so we do not report bootstrap error bars on per-cell η. Residual noise persists from provider-side non-determinism
and from items near a model’s capability frontier, where small perturbations can flip yi. The unsolvable-injection slice
further depends on injected items being genuinely unsolvable for the evaluated models; we audit this qualitatively but cannot
exclude occasional successful completions on a small fraction.
External validity.Our model roster is a snapshot of frontier systems at submission time and will be partially superseded
within months. We have no access to closed-model training data and cannot certify that TRIAGE items were held out of any
model’s pre- or post-training. Tasks are sourced from public reasoning and agentic benchmarks, which biases the picture
toward English-language, formally-stated problems; conclusions about portfolio-level metacognition do not automatically
transfer to multilingual, multi-modal, or open-ended generation regimes. Models also lack episodic memory of their own
past performance on TRIAGE-like tasks; their “self”-assessment is therefore closer to assessment of the model class than to
grounded recollection.
Broader impacts.The intended positive impact of TRIAGE is diagnostic: surfacing systematic overconfidence and
miscalibration in resource decisions before LLMs are placed in deployments where compute, money, or human attention
are at stake. The principal risk is dual-use of the artifact itself. Used unmodified as a training signal, TRIAGE could be
optimized against, yielding models that score well without genuinely improved monitoring - a known failure mode of any
sufficiently legible benchmark. We caution that strong TRIAGE scores are not a license to delegate consequential decisions
to LLMs: passing the benchmark is necessary, not sufficient, for such delegation.
B. Planner Prompt
The planner receives the prompt template shown below. The prompt is held fixed across both regimes (U and E); regime U
treats the per-problem allocations as advisory, while regime E enforces them as hard constraint (§3.2).
Planner Prompt
You are given a set of {n} problems and a total budget of {B_local} output tokens.
Your task is to decide which problems to attempt, in what order, and how many
tokens to allocate to each.
Constraints:
- Each problem is worth 1 point. Your goal is to maximize the total points earned
within the budget.
- Each problem is attempted in an independent model session. The tokens you
allocate to a problem are spent entirely within that single session, with no
context, reasoning, or scratchpad carried over between problems.
- The sum of your per-problem token allocations must not exceed {B_local}.
- You may choose to attempt a strict subset of the problems. Problems you do not
select receive 0 tokens and 0 points.
12

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Problems:
{problems}
Return a single JSON object with the following schema:
{
"plan": [
{"id": <problem_id>, "tokens": <int>},
...
]
}
The order of items in "plan" is the order in which the problems will be attempted.
Items omitted from "plan" are not attempted. Output only the JSON object, with no
additional commentary.
Problem block format.Each problem in the{problems}field is rendered as:
[id: <problem_id>] (points: 1)
<problem_text>
Plan parsing and repair.Plan outputs are parsed as JSON. A small fraction of outputs contain recoverable formatting
issues (trailing commentary outside the JSON object, extra fields, malformed numerics); these pass through a deterministic
repair pass that strips non-JSON content, coerces token counts to non-negative integers, and discards plan items whose id
does not appear in the pool. Plans that remain unparseable after repair are excluded; pools with no parseable plan for a
model are excluded from that model’sηaverage for the affected (dataset,α) cell.
C. Additional Experiments
C.1. Budget-aware re-solving: do models honor their own allocations?
The triage protocol measureswhethera model can identify worthwhile problems given a fixed token budget; it does not test
whether the model can actually execute under its own self-declared per-problem allocation ai. We probe this directly with a
budget-aware re-solveexperiment on three models - Gemini 2.5 Flash, Kimi K2.5, and GLM 5.1, all in standard-inference
mode. For every (model, problem) where the α= 1.0 plan selected the problem with ai >0 , we re-issue the standard solver
prompt with an instruction stating the model’s owna i:
Budget-aware banner (prepended to the standard solver prompt)
You have a strict output-token budget of {a_i} tokens for solving this problem,
including any reasoning, drafts, or scratch work you produce. Plan your solution
to fit within this limit. Be concise, skip unnecessary explanation, and commit to
your final answer before exhausting the budget.
The API-level max_tokens is unchanged from the baseline run, so this imposes aself-imposedcap rather than a hard
truncation. We record two outcomes per problem:Acc baseline (the original baseline solve, no banner, full max_tokens)
andAcc budget-aware (with the banner). We also reportcompliance, defined as the fraction of problems for which the model’s
actual output length stays within its self-declared budget, i.e. compliance= 1 N PN i=1 ⊮[output_tokens i ≤a i ]. Because
no hard cap is applied, compliance measures whether the modelvoluntarilyrespects the budget statement. Finally, we
decompose the change between the baseline and budget-aware runs into four pairwise outcome counts:kept correct(correct
in both runs),lost correct(correct at baseline, wrong with the banner),newly correct(wrong at baseline, correct with the
banner), andstill wrong(incorrect in both runs). The aggregate counts are reported in Figure 7; the per-dataset breakdown is
in Figure 8.
Stating the budget improves accuracy, but compliance is poor.For all three models, Acc budget-aware exceeds Accbaseline
in aggregate (+1.9 pp for Gemini 2.5 Flash, +4.9 pp for Kimi K2.5, and +8.3 pp for GLM 5.1; Figure 7). Yet only Gemini
13

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
2.5 Flash exhibits a meaningful compliance rate (36.6%); Kimi K2.5 stays within its self-declared budget on only 6.0% of
problems and GLM 5.1 on 16.0%. The accuracy gains therefore arise even when the model overruns its stated budget - the
budget-aware instruction functions more as aconciseness priorthan as a binding constraint. This is consistent with the gap
between the advisory and enforced regimes reported in §5.1: models can plan against a budget statement but rarely execute
within it.
Per-dataset patterns.Figure 8 shows that the budget-aware lift is concentrated on the structured-reasoning datasets
(AIME, GPQA, LCB) where models also have higher baseline accuracy. On HLE, all three models remain near floor in every
column. GLM 5.1’s lift on AIME is the largest single effect in the experiment: Accbaseline = 0.10→Acc budget-aware = 0.61.
This is consistent with GLM 5.1’s leading ηU in the main results: when the model is told to be concise, it commits to its
final answer earlier and avoids the long, drifting traces that cost it correctness in the unconstrained setting.
C.2. Prompt-Sensitivity Ablation
To check whether η depends on the prompt, we re-ran the planning step under three framings of the same task: A (neutral,
used elsewhere in the paper), B (autonomous agent), and C (timed exam). The Rules block, problem text, budget, output
schema, and ordering instruction are identical across the three; only the opening paragraph differs.
Triage Prompt
Variant A — Neutral (default)
You are given a set of {domain} to attempt under a fixed output-token budget. You do not have to attempt every
problem. Deciding which problems to attempt and in what order is part of the task.
Triage Prompt
Variant B — Autonomous Agent
You are an autonomous planning agent operating under a fixed compute budget of {B} output tokens. A set of
{domain} has been assigned to you. You cannot expect to complete every assignment within budget. Your job is to
select which to execute and in what order so as to maximize total reward. Some assignments may be infeasible for
you — committing tokens to those yields no reward.
Triage Prompt
Variant C — Timed Exam
You are taking a timed exam with a fixed output-token budget of{B}across all questions. A set of{domain}is in
front of you. You do not have to attempt every question — some may be too difficult or unanswerable within the time
available. Decide which questions to attempt and in what order so as to maximize your total score.
We ran the full grid: 2 models, 2 modes, 8 datasets, 4 budget levels, 3 variants - 16 (model, mode, α) cells per variant under
each regime.
Results.For ηU , 11 of 16 cells stay within 0.1 across variants; for ηE, 14 of 16 (Tables 1, 2). The two largest spreads in
ηU are both in think-mode at extreme budgets: Kimi K2.5/think at α= 1.0(range 0.383, with Variant C alone dropping to
0.506) and Qwen 3.5 27B/think atα= 0.75(range0.188).
The α= 0.75case is not random. Variant A gives the lowest ηU in 3 of 4 think-mode cells at α≥0.5 . Variants B and C tell
the model some problems may be infeasible; A does not. Reasoning models seem to need that cue - without it they attempt
too many problems. Non-thinking modes show no such pattern (median range0.040).
Ranking stability.Table 3 reports Kendall’s τb on the four-model ranking induced by each variant pair. With n= 4, τb
can only take the values {−1,−2/3,−1/3,0,1/3,2/3,0.913,1} : a single rank swap drops τ from 1 to 0.667. We therefore
14

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Table 1: ηU under each prompt variant. Each value is the mean over 8 data splits (AIME,GPQA Diamond,LiveCodeBench,
HLE-CS/AI,HLE-Physics,HLE-Humanities,HLE-Other,HLE-Engineering) at that α.range= max−min across A, B, C;
cells with range≥0.10are bolded.
Model Modeα η A U ηB U ηC U range
Kimi K2.5
nothink
0.25 0.615 0.613 0.575 0.040
0.50 0.530 0.659 0.5540.130
0.75 0.681 0.781 0.7760.100
1.00 0.978 1.000 1.000 0.022
think
0.25 0.432 0.497 0.412 0.085
0.50 0.463 0.477 0.526 0.063
0.75 0.333 0.363 0.271 0.092
1.00 0.778 0.889 0.5060.383
Qwen 3.5 27B
nothink
0.25 0.446 0.428 0.445 0.018
0.50 0.379 0.353 0.443 0.090
0.75 0.507 0.523 0.556 0.049
1.00 0.933 0.956 0.933 0.022
think
0.25 0.414 0.361 0.391 0.053
0.50 0.333 0.448 0.3340.115
0.75 0.287 0.415 0.4750.188
1.00 0.889 0.889 0.911 0.022
Cells with range<0.10:11 / 16
Median range:0.077
report raw τ rather than apply a threshold. All 24 pairwise values are ≥2/3 , and the swapped models differ by <0.1 in η -
within the cell-level spread we already report. The rankings are stable.
Taken together - 78% of cells within 0.1 spread, all τ≥2/3 , and the largest disagreement isolated to one (model, mode, α)
corner -η U is robust to the prompt framings tested.
D. Boundary behaviour ofη
This appendix gives a formal account of the conditions under which ηM in (2) is well-defined, the convention used when the
denominator vanishes, and the filtering rule applied to the main results. All statements are with respect to the setup of §3.2:
integer token costsc i ∈Z >0, uniform valuesv i = 1, budgetB=⌊α P i ci⌋, and regime U execution.
D.1. Domain of definition
The ratio in (2) is defined whenever Voracle > Vrandom. Two structural conditions force Voracle =V random and hence leave ηM
undefined:
(D1) Empty solvable set:V oracle = 0. If yi = 0for every i in the pool, then VM = 0for any plan, and likewise Vrandom = 0.
The metric carries no signal: every planner - including one that does nothing - ties at zero.
(D2) Slack-budget collapse atα= 1. At α= 1, B= P i ci. Proposition D.1 shows that under regime U every permutation
of the gradeable items completes without truncation, soV random = P i yi =V oracle deterministically.
Proposition D.1(Truncation impossibility at full budget).Let the pool have gradeable items with costs c1, . . . , cn ∈Z >0,
budget B= Pn i=1 ci, and any permutation (i1, . . . , in) of {1, . . . , n}. Under regime U, no truncation occurs and the plan
executes every item.
Proof.After processing the firstkitems, the remaining budget is
Rk =B−
kX
j=1
cij =
nX
j=k+1
cij .
15

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Table 2: ηE under each prompt variant, same layout as Table 1. Negative values reflect systematic under-allocation in the
enforced regime - a model property, the same under all three prompts.
Model Modeα η A E ηB E ηC E range
Kimi K2.5
nothink
0.25 0.152 0.152 0.148 0.004
0.50−0.254−0.232−0.2450.022
0.75−1.421−1.352−1.4210.069
1.00 0.356 0.356 0.356 0.000
think
0.25−0.192−0.194−0.2370.045
0.50−0.712−0.692−0.7000.020
0.75−2.193−2.211−2.2820.089
1.00−0.367−0.433−0.5320.165
Qwen 3.5 27B
nothink
0.25 0.089 0.157 0.143 0.068
0.50−0.161−0.152−0.1590.008
0.75−1.180−1.113−1.1510.067
1.00 0.222 0.200 0.222 0.022
think
0.25−0.110−0.111−0.1050.005
0.50−0.479−0.552−0.5400.073
0.75−1.568−1.597−1.7820.214
1.00 0.311 0.333 0.244 0.089
Cells with range<0.10:14 / 16
Median range:0.057
Table 3: Kendall’s τb between the four-model rankings induced by each variant pair.max rangeis the largest across-variant
spread in any (model, mode) row at thatα.
Regimeα τ(A, B)τ(A, C)τ(B, C) minτmax range
ηU
0.25 0.667 1.000 0.667 0.667 0.085
0.50 0.667 1.000 0.667 0.667 0.130
0.75 0.667 0.667 1.000 0.667 0.188
1.00 0.913 1.000 0.913 0.913 0.383
ηE
0.25 0.667 1.000 0.667 0.667 0.068
0.50 1.000 1.000 1.000 1.000 0.073
0.75 1.000 1.000 1.000 1.000 0.214
1.00 1.000 1.000 1.000 1.000 0.165
For k < n, item ik+1 truncates iff cik+1 > Rk, i.e., iff Pn j=k+2 cij <0 (taking the empty sum as 0 when k=n−1 ). Since
ci >0for alli, the strict inequality is never satisfied. Hence execution proceeds through allnitems.
A corollary: at α= 1 the knapsack constraint in (1) is non-binding, so xi = 1for all i is feasible. Since the oracle objective
is non-decreasing in each xi, this is optimal and Voracle = P i yi =V random, with zero Monte-Carlo variance across the 103
random shuffles. Combining (D1) and (D2): ηM is undefined at every α for pools with Voracle = 0, and at α= 1 for all
remaining pools.
D.2. One-sided limit and implementation convention
For pools with Voracle ≥1 , consider ηM as α→1 −. The denominator Voracle(α)−V random(α) is non-negative for all α∈(0,1]
(the oracle is optimal among feasible plans, so it dominates any expectation over them) and shrinks to 0 as α→1 . Two
cases:
1. Achievement branch.If VM (α) =V oracle(α) on a left neighbourhood of α= 1 , then ηM (α) = 1identically, and
limα→1− ηM (α) = 1.
2. Failure branch.If VM (α)< V oracle(α) near α= 1 , the numerator approaches VM (1)−V oracle(1)<0 while the
denominator approaches0from above. Hencelim α→1− ηM (α) =−∞.
16

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
The released implementation extendsη M to cases withV oracle =V random by
ηM :=1[V M ≥V oracle].(4)
The achievement value in (4) coincides with the one-sided limit. The failure value is clipped to 0 rather than reported as −∞,
consistent with the interpretation of ηM = 0as “no skill”. This extension is the convention used for ηM throughout the paper,
including pools satisfying (D1).
In practice, the largest-magnitude negative efficiency values arise atα near 1, where the denominator Voracle −V random shrinks
while remaining positive, while the regret metric ˜RM (§D.5) provides a bounded alternative for these cases.
D.3. Filtering rule
The normalized regret ˜RM (§D.5) requires Voracle ≥1 to be defined, so when we report ˜RM we restrict to pools satisfying this
condition, equivalently discarding pools under (D1). These are pure capability-ceiling cases: the model fails every problem
under standard execution, so every plan achieves VM =V oracle = 0and the regret denominator vanishes. For ηM, no such
filter is applied; pools under (D1) are retained using the convention in (4), which assigns ηM = 1when VM ≥V oracle and
Voracle = 0.
D.4. Range
For pools whereη M is genuinely informative (Voracle > Vrandom):
•η M ≤1 , with equality iff VM =V oracle. This follows from VM ≤V oracle (the oracle is the maximum over feasible plans)
and a strictly positive denominator.
•η M is unbounded below. As Voracle and Vrandom approach each other (the denominator shrinks toward zero from above),
ηM can take arbitrarily large negative values for any fixedV M < Vrandom.
We therefore characterizeη M ∈(−∞,1].
D.5. Sensitivity check: regret as an alternative normalization
The asymmetric range ofη M motivates a second, bounded metric for robustness: the normalized regret
˜RM = Voracle −V M Voracle ,(5)
defined whenever Voracle ≥1 . By construction ˜RM ∈[0,1] , with ˜RM = 0at oracle and ˜RM = 1when the planner captures
none of the oracle’s value. Unlike ηM, ˜RM has no denominator singularity, is continuous at α= 1, and admits the same
interpretation across all α. We report ˜RM alongside ηM and confirm that the conclusions are robust to the choice of
normalization.
E. Model Configurations
Table 4 lists the 20 models evaluated in the main experiments, together with their providers, parameter counts where
disclosed, reasoning support, and the exact API or checkpoint identifiers used. Open-weights models were served locally
via vLLM; closed models were accessed through their respective provider APIs. All queries used temperature 0 with
provider-default sampling parameters; reasoning effort was set to the provider default for models that expose a tunable
reasoning level.
Reasoning modes.Each model is evaluated in up to two modes:standard inference(no extended reasoning) andextended
reasoning(the model’s native long chain-of-thought or thinking mode, where supported). Models without a thinking toggle
are evaluated only in standard inference. The “Reasoning” column in Table 4 indicates which modes were run for each
model.
17

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Table 4: Models evaluated in TRIAGE.Weights: O = open, C = closed.Params: parameter count where disclosed; for
mixture-of-experts models, total / active.Reasoning: S = standard inference only, S+E = both standard and extended
reasoning modes evaluated.Identifier: provider API string or HuggingFace checkpoint used.
Model Provider Weights Params Reasoning Identifier
Qwen 2.5 series (Alibaba)
Qwen 2.5 3B Alibaba O 3B SQwen/Qwen2.5-3B-Instruct
Qwen 2.5 7B Alibaba O 7B SQwen/Qwen2.5-7B-Instruct
Qwen 2.5 14B Alibaba O 14B SQwen/Qwen2.5-14B-Instruct
Qwen 2.5 32B Alibaba O 32B SQwen/Qwen2.5-32B-Instruct
Qwen 3 series (Alibaba)
Qwen 3 4B Alibaba O 4B EQwen/Qwen3-4B
Qwen 3 8B Alibaba O 8B EQwen/Qwen3-8B
Qwen 3 14B Alibaba O 14B EQwen/Qwen3-14B
Qwen 3 32B Alibaba O 32B EQwen/Qwen3-32B
Qwen 3.5 series (Alibaba)
Qwen 3.5 4B Alibaba O 4B S+EQwen/Qwen3.5-4B
Qwen 3.5 9B Alibaba O 9B S+EQwen/Qwen3.5-9B
Qwen 3.5 27B Alibaba O 27B S+EQwen/Qwen3.5-27B
Qwen 3.5 35B-A3B Alibaba O 35B / 3B S+EQwen/Qwen3.5-35B-A3B
Frontier and other open models
Claude Haiku 4.5 Anthropic C — S+Eclaude-haiku-4-5
DeepSeek V3 DeepSeek O 671B / 37B S+Edeepseek-chat
Gemini 2.5 Flash Google C — S+Egemini-2.5-flash
GLM 5.1 Zhipu O — S+Eglm-5.1
GPT-5 Mini OpenAI C — S+Egpt-5-mini
Kimi K2.5 Moonshot O — S+Ekimi-k2.5
GPT-OSS 20B OpenAI O 20B Eopenai/gpt-oss-20b
GPT-OSS 120B OpenAI O 120B Eopenai/gpt-oss-120b
Sampling and decoding.All models were queried at temperature 0. For models accessed via provider APIs, we used each
provider’s default values for top-p, top-k, frequency penalty, and presence penalty unless these parameters were unsupported
at temperature 0. For locally served models, decoding used vLLM defaults with greedy sampling. Maximum output length
was set to a value sufficient to capture the longest plan and reasoning trace observed for each model in pilot runs; exact
values per model are recorded in the released configuration files.
Reasoning effort settings.For models that expose a tunable reasoning level (e.g., reasoning effort, thinking budget),
we used the provider’s default reasoning setting (e.g., medium for GPT-OSS) in extended-reasoning mode and disabled
reasoning entirely in standard-inference mode.
18

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
AIME GPQA LCB HLE
Qwen 2.5 3B  [std]
Qwen 2.5 7B  [std]
Qwen 2.5 14B  [std]
Qwen 2.5 32B  [std]
Qwen 3 4B  [ext]
Qwen 3 8B  [ext]
Qwen 3 14B  [ext]
Qwen 3 32B  [ext]
Qwen 3.5 4B  [std]
Qwen 3.5 4B  [ext]
Qwen 3.5 9B  [std]
Qwen 3.5 9B  [ext]
Qwen 3.5 27B  [std]
Qwen 3.5 27B  [ext]
Qwen 3.5 35B-A3B  [std]
Qwen 3.5 35B-A3B  [ext]
Claude Haiku 4.5  [std]
Claude Haiku 4.5  [ext]
DeepSeek V3  [std]
DeepSeek V3  [ext]
Gemini 2.5 Flash  [std]
Gemini 2.5 Flash  [ext]
GLM 5.1  [std]
GLM 5.1  [ext]
GPT-5 Mini  [std]
GPT-5 Mini  [ext]
Kimi K2.5  [std]
Kimi K2.5  [ext]
GPT-OSS 20B  [ext]
GPT-OSS 120B  [ext]
0.03 0.29 0.06 0.03
0.10 0.32 0.20 0.03
0.13 0.47 0.21 0.04
0.20 0.47 0.28 0.03
0.50 0.46 0.27 0.04
0.50 0.51 0.30 0.04
0.57 0.52 0.33 0.04
0.59 0.62 0.32 0.04
0.25 0.59 0.27 0.04
0.23 0.64 0.20 0.03
0.42 0.65 0.28 0.03
0.30 0.68 0.22 0.03
0.50 0.71 0.39 0.05
0.57 0.77 0.30 0.04
0.38 0.54 0.35 0.04
0.54 0.78 0.32 0.05
0.45 0.61 0.41 0.03
0.67 0.70 0.52 0.02
0.57 0.71 0.38 0.04
0.72 0.73 0.39 0.08
0.28 0.41 0.34 0.03
0.62 0.70 0.33 0.05
0.10 0.31 0.18 0.01
0.55 0.61 0.19 0.05
0.52 0.69 0.47 0.05
0.77 0.79 0.41 0.06
0.13 0.21 0.20 0.03
0.42 0.62 0.28 0.07
0.67 0.56 0.42 0.03
0.78 0.73 0.49 0.03
Figure 4: Per-(model, mode) accuracy on each benchmark. Accuracy is the proportion of solvable problems and is
independent of budget α. Cells use a sequential white→teal scale; horizontal lines separate model families; the [std] / [ext]
suffix denotes standard inference versus extended reasoning.
19

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
AIME GPQA LCB HLE AIME GPQA LCB HLE AIME GPQA LCB HLE AIME GPQA LCB HLE
Qwen 2.5 3B  [std]
Qwen 2.5 7B  [std]
Qwen 2.5 14B  [std]
Qwen 2.5 32B  [std]
Qwen 3 4B  [ext]
Qwen 3 8B  [ext]
Qwen 3 14B  [ext]
Qwen 3 32B  [ext]
Qwen 3.5 4B  [std]
Qwen 3.5 4B  [ext]
Qwen 3.5 9B  [std]
Qwen 3.5 9B  [ext]
Qwen 3.5 27B  [std]
Qwen 3.5 27B  [ext]
Qwen 3.5 35B-A3B  [std]
Qwen 3.5 35B-A3B  [ext]
Claude Haiku 4.5  [std]
Claude Haiku 4.5  [ext]
DeepSeek V3  [std]
DeepSeek V3  [ext]
Gemini 2.5 Flash  [std]
Gemini 2.5 Flash  [ext]
GLM 5.1  [std]
GLM 5.1  [ext]
GPT-5 Mini  [std]
GPT-5 Mini  [ext]
Kimi K2.5  [std]
Kimi K2.5  [ext]
GPT-OSS 20B  [ext]
GPT-OSS 120B  [ext]
-0.33 -0.07 0.01 0.36 -0.95 -0.18 -0.26 0.16 -2.65* -0.67 -1.51* -0.25 0.00 0.14 0.33 0.60
-0.09 -0.13 -0.01 0.53 -0.31 -0.08 -0.28 0.32 -2.11* -0.64 -0.28 -0.27 0.50 0.86 0.33 0.60
-0.05 0.01 0.03 0.23 0.41 -0.11 -0.22 -0.10 -1.26* -0.56 -1.63* -0.25 0.00 0.86 0.00 0.67
0.27 -0.15 0.29 0.49 0.20 -0.48 -0.24 0.35 -0.40 -1.13* -1.13* -0.21 0.50 0.14 0.00 0.63
0.32 0.11 -0.18 0.33 0.33 0.18 -0.91 0.23 0.00 0.29 -2.46* -0.10 0.00 0.67 0.00 0.80
0.30 0.09 -0.27 0.24 0.36 0.06 -0.94 0.25 0.25 0.04 -2.42* 0.69 0.00 0.17 0.00 0.65
0.67 0.08 -0.25 0.29 0.39 0.07 -0.21 0.36 0.30 -0.06 -2.03* 0.05 1.00 0.67 0.25 0.88
0.50 0.14 0.25 0.38 0.36 0.15 -0.13 0.24 -0.26 -0.35 -0.58 0.17 1.00 0.50 0.00 0.71
0.01 0.05 -0.34 0.27 -0.47 -0.16 -0.96 0.06 -1.49* -0.13 -2.71* -0.13 0.00 0.86 0.00 0.73
0.33 -0.15 -0.14 0.22 -0.95 -0.09 -0.95 -0.00 0.53 -0.27 -2.83* 0.02 0.00 0.67 0.00 0.80
-0.01 0.14 0.06 0.48 -0.05 -0.09 -0.00 0.36 -0.51 0.16 -0.39 0.44 0.50 0.71 0.17 0.97
-0.36 0.11 -0.21 0.55 -0.22 -0.07 -0.63 0.36 0.06 -0.08 -0.67 0.53 1.00 1.00 0.20 0.91
0.36 0.25 0.41 0.43 0.43 0.09 0.46 0.41 0.52 -0.25 0.37 0.66 1.00 1.00 0.83 0.97
0.53 0.23 0.19 0.51 -0.05 0.20 -0.26 0.58 -1.56* 0.25 -0.90 0.91 0.50 1.00 0.50 0.91
-0.32 -0.54 0.03 0.04 -0.51 -0.94 -0.28 -0.36 -1.32* -1.98* -0.36 -1.74* 0.50 0.00 0.67 0.31
-0.65 0.26 0.43 0.24 0.02 -0.15 -0.11 0.71 0.06 0.28 0.02 0.66 0.00 0.67 0.67 0.90
-0.12 0.44 0.45 0.53 -0.20 0.21 0.33 0.37 0.48 -0.32 0.22 0.32 0.50 0.14 0.67 0.77
0.80 0.55 0.42 0.63 0.41 0.17 0.23 0.77 -1.09* -0.15 -0.24 0.24 0.50 0.43 0.50 0.97
0.46 0.25 0.21 0.32 0.21 0.20 0.37 0.55 -0.22 0.06 0.32 0.03 0.50 0.71 0.33 0.90
0.68 0.53 0.12 0.48 0.69 0.44 -0.69 0.49 -1.07* 0.21 -1.19* -0.05 1.00 0.86 0.50 0.80
0.37 0.18 0.51 0.65 0.54 0.10 0.49 0.70 0.52 -0.40 0.47 0.76 0.00 0.57 0.17 0.93
0.60 0.45 0.50 0.32 0.03 0.29 0.29 0.50 -2.24* -0.51 -0.42 0.64 0.00 0.00 0.00 0.77
0.51 0.49 0.85 0.82 0.76 0.68 0.88 0.71 0.56 0.52 0.84 0.87 1.00 1.00 1.00 1.00
0.48 0.54 0.93 0.39 0.57 0.72 0.93 0.32 0.25 0.55 1.00 0.31 0.50 0.29 1.00 0.74
0.03 0.25 -0.10 0.30 0.12 -0.19 -0.15 0.26 -0.21 -0.09 -2.24* 0.10 1.00 0.86 0.67 0.83
-0.15 0.32 -0.20 0.27 -0.02 0.21 -0.44 0.28 -0.81 0.18 -1.58* -0.31 1.00 0.86 0.33 0.73
0.74 0.33 0.81 0.60 0.23 0.22 0.77 0.54 0.63 0.44 0.92 0.69 1.00 0.71 0.83 0.87
0.67 0.39 0.67 0.35 0.58 0.40 0.63 0.37 0.63 0.01 0.37 0.39 1.00 0.14 0.50 0.77
-0.20 0.03 -0.22 0.43 0.05 -0.07 -0.23 0.30 -0.33 -0.05 -0.86 0.31 1.00 0.86 0.40 0.78
-0.15 0.02 -0.25 0.41 0.19 -0.11 -0.80 0.47 0.06 -0.09 -2.64* -0.11 0.50 0.57 0.00 0.84
= 0.25
 = 0.5
 = 0.75
 = 1.0
Figure 5: Triage skill in the advisory-budget regime, ηU , per (model, α, dataset). ηU = 1matches oracle planning, ηU = 0
matches a random baseline, ηU <0 is worse than random. Cells use a diverging coral →navy palette capped at [−1,1] ;
values outside this range are marked with∗. Bold vertical rules separateαblocks.
20

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
AIME GPQA LCB HLE AIME GPQA LCB HLE AIME GPQA LCB HLE AIME GPQA LCB HLE
Qwen 2.5 3B  [std]
Qwen 2.5 7B  [std]
Qwen 2.5 14B  [std]
Qwen 2.5 32B  [std]
Qwen 3 4B  [ext]
Qwen 3 8B  [ext]
Qwen 3 14B  [ext]
Qwen 3 32B  [ext]
Qwen 3.5 4B  [std]
Qwen 3.5 4B  [ext]
Qwen 3.5 9B  [std]
Qwen 3.5 9B  [ext]
Qwen 3.5 27B  [std]
Qwen 3.5 27B  [ext]
Qwen 3.5 35B-A3B  [std]
Qwen 3.5 35B-A3B  [ext]
Claude Haiku 4.5  [std]
Claude Haiku 4.5  [ext]
DeepSeek V3  [std]
DeepSeek V3  [ext]
Gemini 2.5 Flash  [std]
Gemini 2.5 Flash  [ext]
GLM 5.1  [std]
GLM 5.1  [ext]
GPT-5 Mini  [std]
GPT-5 Mini  [ext]
Kimi K2.5  [std]
Kimi K2.5  [ext]
GPT-OSS 20B  [ext]
GPT-OSS 120B  [ext]
-0.33 -0.07 0.12 0.19 -0.95 -0.26 -0.49 -0.03 -2.65* -1.20* -1.51* -0.82 0.00 0.00 0.33 0.33
-0.31 0.00 -0.06 0.44 -0.63 -0.03 -0.44 0.21 -2.74* -1.04* -0.66 -0.61 0.00 0.00 0.17 0.57
-0.32 -0.14 -0.04 0.08 -0.75 -0.54 -0.35 -0.27 -1.63* -1.79* -2.16* -1.24* 0.00 0.00 0.00 0.37
-0.18 -0.49 -0.03 0.18 -0.55 -1.02* -0.51 -0.16 -2.35* -2.38* -1.20* -1.08* 0.00 0.00 0.00 0.43
-0.49 -0.39 -0.33 0.03 -1.00* -0.97 -0.96 -0.13 -2.73* -2.72* -2.68* -1.14* 0.00 0.00 0.00 0.20
-0.46 -0.31 -0.33 -0.01 -1.01* -0.84 -0.94 -0.21 -2.75* -1.67* -2.67* -0.79 0.00 0.00 0.00 0.31
-0.63 -0.45 -0.34 0.12 -0.95 -0.97 -0.95 -0.34 -2.75* -2.64* -2.77* -1.22* 0.00 0.00 0.00 0.32
-0.56 -0.47 -0.32 0.22 -1.06* -0.84 -0.95 -0.37 -2.79* -2.60* -2.75* -1.17* 0.00 0.00 0.00 0.29
-0.32 -0.32 -0.34 0.09 -0.96 -0.80 -0.96 -0.35 -2.78* -2.40* -2.71* -1.53* 0.00 0.00 0.00 0.30
-0.34 -0.59 -0.31 0.07 -0.95 -1.14* -0.95 -0.10 -2.78* -2.71* -2.83* -0.78 0.00 0.00 0.00 0.47
-0.41 -0.41 0.10 0.30 -0.83 -0.81 -0.51 -0.02 -2.76* -2.29* -2.00* -0.94 0.00 0.00 0.00 0.47
-0.36 -0.68 -0.32 0.29 -0.95 -1.21* -0.80 -0.22 -1.51* -2.47* -2.85* -1.13* 0.00 0.00 0.00 0.52
-0.21 0.21 0.15 0.07 -0.22 0.01 0.15 -0.25 -0.64 -0.83 -0.48 -1.37* 0.00 0.00 0.00 0.33
-0.64 -0.75 -0.39 0.08 -0.88 -1.18* -0.95 -0.36 -2.09* -1.92* -2.58* -1.15* 0.00 0.00 0.00 0.32
-0.38 -0.63 -0.03 -0.01 -0.96 -0.94 -0.47 -0.46 -2.76* -1.98* -1.21* -1.74* 0.00 0.00 0.00 0.24
-0.65 -0.73 -0.36 -0.07 -0.83 -1.21* -0.95 -0.29 -1.59* -2.29* -2.30* -1.58* 0.00 0.00 0.00 0.45
-0.59 -0.66 -0.35 0.32 -0.73 -0.44 -0.62 0.23 -1.17* -0.89 -1.46* 0.10 0.00 0.00 0.00 0.63
-0.68 -0.71 -0.54 0.41 -0.83 -0.94 -0.92 0.16 -2.75* -2.42* -2.51* -0.55 0.00 0.00 0.00 0.53
-0.22 -0.42 -0.12 0.27 -0.38 -0.63 -0.18 -0.10 -0.97 -1.47* -0.74 -0.76 0.00 0.00 0.00 0.47
-0.56 -0.51 -0.32 -0.11 -1.11* -1.06* -0.94 -0.61 -2.73* -2.54* -2.76* -2.10* 0.00 0.00 0.00 0.17
-0.02 0.23 0.39 0.42 0.07 0.07 0.36 0.28 -1.06* -0.69 0.05 -0.32 0.00 0.00 0.17 0.57
-1.14* -0.81 -0.14 0.03 -2.04* -1.37* -0.42 -0.38 -3.30* -2.92* -1.56* -1.42* 0.00 0.00 0.00 0.33
-0.30 -0.32 -0.26 0.60 -0.71 -0.82 -0.62 0.42 -1.78* -2.17* -1.93* -0.11 0.00 0.00 0.00 0.70
-0.44 -0.41 0.02 -0.17 -1.01* -1.02* -0.29 -0.78 -2.73* -2.53* -1.72* -2.20* 0.00 0.00 0.00 0.13
-0.39 -0.25 -0.21 -0.00 -0.72 -0.12 -0.31 -0.45 -1.28* -0.80 -2.50* -1.58* 0.00 0.00 0.00 0.23
-0.57 -0.17 -0.26 -0.09 -0.53 -0.56 -0.64 -0.62 -2.87* -2.31* -2.21* -2.07* 0.00 0.00 0.00 0.17
-0.31 -0.28 -0.34 0.38 -0.96 -0.90 -0.94 0.09 -2.75* -2.71* -2.79* -0.74 0.00 0.00 0.00 0.53
-0.43 -0.48 -0.33 -0.08 -0.88 -0.97 -0.97 -0.64 -2.58* -2.68* -2.54* -2.04* -14.21* 0.00 0.00 0.17
-0.46 -0.33 -0.30 0.28 -0.69 -0.90 -0.82 -0.07 -2.30* -2.43* -2.07* -1.00* 0.00 0.00 0.00 0.37
-0.59 -0.26 -0.29 0.30 -0.36 -0.69 -0.93 0.27 -1.35* -1.57* -2.64* -0.81 0.00 0.00 0.00 0.52
= 0.25
 = 0.5
 = 0.75
 = 1.0
Figure 6: Triage skill in the enforced-budget regime, ηE, per (model, α, dataset). Color encoding identical to Figure 5. The
α= 1.0column block mostly saturates near zero becauseV oracle ≈V random at full budget.
21

TRIAGE: Evaluating Prospective Metacognitive Control in LLMs
Model N Accbaseline Accbudget-aware compliance newly correct lost correct kept correct still wrong
Gemini 2.5 Flash 1192 0.143 0.162 0.366 57 34 136 965
Kimi K2.5 1243 0.084 0.133 0.060 74 13 91 1065
GLM 5.1 1266 0.088 0.171 0.160 114 10 102 1040
Figure 7:Budget-aware re-solve, aggregate per model.Cells colored by intensity within each metric. N is the number of
(problem, allocation) pairs re-issued.Complianceis the fraction of problems for which the model’s actual output length
stays within its self-declared budget ai. The four right-hand counts (newly correct, lost correct, kept correct, still wrong)
sum to N and decompose the change between Accbaseline (original baseline solve) and Accbudget-aware (baseline solver prompt
augmented with an instruction to answer within the model’s owna i).
AIME GPQA LCB HLE
Gemini 2.5 Flash
Accbaseline 0.304 0.405 0.384 0.030
Accbudget-aware 0.261 0.508 0.384 0.036
compliance 0.587 0.636 0.580 0.252
Kimi K2.5
Accbaseline 0.119 0.211 0.199 0.026
Accbudget-aware 0.237 0.412 0.267 0.029
compliance 0.153 0.041 0.080 0.053
GLM 5.1
Accbaseline 0.102 0.313 0.185 0.013
Accbudget-aware 0.610 0.510 0.225 0.047
compliance 0.458 0.232 0.354 0.081
Figure 8:Budget-aware re-solve, per (model × dataset).HLE sub-domains are aggregated by problem-count weighted
mean. Rows within each model block: original baseline accuracy, accuracy with the budget banner, and compliance rate.
Color encoding follows Figure 7.
22
