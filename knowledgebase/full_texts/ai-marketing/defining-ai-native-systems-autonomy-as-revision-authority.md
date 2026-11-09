---
title: 'Defining AI-Native Systems: Autonomy as Revision Authority'
url: https://arxiv.org/abs/2607.21659
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Cheng Tan
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.21659
pages: 10
chars: 51790
fetched_at: '2026-11-08T13:02:18+00:00'
kb_version: 1
---

# Defining AI-Native Systems: Autonomy as Revision Authority

Defining AI-Native Systems:
Autonomy as Revision Authority
Cheng Tan
Northeastern University
Abstract
AI has begun to write systems code: agents now synthesize,
verify, and deploy system components. Despite this shift, “AI-
native” remains a marketing term with no precise technical
definition. This paper gives it one. We define AI-nativeness
along a single axis—authority over the system’s own decisions—
rather than by the capability of the underlying AI models.
Building on a decision-level model of a system, we distin-
guishoccupancy(who executes a decision) fromrevision
authority(who may change it), organize revision authority
into a ladder—self-tuning, self-rewriting, self-architecting—
and define a system as AI-native when an AI autonomously
rewrites the system’s own implementations. The definition
further requires an escalation detector, a verification pro-
cedure, and a verified fallback, while leaving purpose and
correctness human-owned.
Keywords:AI-native systems, ML for systems, autonomy,
coding agents, self-adapting systems
1 Introduction
Artificial intelligence is starting to write systems software.
Beyond the now-familiar practice of replacing a heuristic
with a learned model, agentic systems have begun toauthor
systems code: recent frameworks discover novel scheduling
and load-balancing algorithms that beat expert baselines,
and coding agents synthesize, benchmark, and verify imple-
mentations against real workloads [4, 5, 17]. The question a
systems designer faces has shifted accordingly—from “can a
model beat this heuristic on a benchmark?” to “how much
of the system do we let an AI hold and change, and how do
we stay safe while it does?”
The moment is genuinely new. Machine learning for sys-
tems already ships—learned indexes, caches, allocators, and
schedulers run in production—yet only as narrow, hand-
built, hand-maintained point solutions, because a model that
resideson the hot path pays for it in inference overhead,
workload drift, weak tail guarantees, and expensive book-
keeping (§2). What changed is the mode of use: an agent that
authorscode works off the critical path, at development time,
and pays none of those costs. For the first time it is feasible
to let an AI continuously revise a system’s ownimplementa-
tion—not merely retune its knobs—under human-set goals.
That capability needs a name for the system property it
creates, and “AI-native” is the label the field already reaches
for. But the label is a marketing term—attached to databases,
operating systems, clouds, and developer tools, meaning
something different each time—and what it lacks is a rig-
orous, technical statement of what property a system must
have to earn it. This paper offers one.
Our definition rests on a single axis:authority over the
system’s own decisions—who is permitted to change what
the system does, at which level of its design, how often, and
under what guardrails. This is the property that determines
whether a system canevolve itself, safely, and we argue it
is what “AI-native” should name. It is a claim about the
system, not the AI: two recent efforts grade instead how
much intelligence a problem demands [14] or how capable
an AI is at systems research [7], whereas we grade how much
authority a system delegates to an AI and how that authority
is bounded. The questions are orthogonal, and §5 makes the
relationship explicit.
We develop the definition in three steps.
• First, adecision-level model(§3) stratifies a system’s de-
cisions by binding time—design, implementation, policy,
runtime—and separatesoccupancy(who executes a de-
cision) fromrevision authority(who may change it), the
axis on which autonomy actually lives.
• Second, arevision-authority ladder(§4) grades systems by
how high that authority reaches: self-tuning, self-rewriting,
and self-architecting.
• Third, the ladder framework yields thedefinition(§5):
a system is AI-native iff an AI autonomously rewrites
its implementations under an escalation detector, holds
authority over how deciders are allocated, runs every
revision through a verification procedure while retaining
a fallback, and leaves purpose and correctness human-
owned—a grade that must beevidencedby an auditable
certificate, not asserted.
We then draw an analogy between our definition and a prece-
dent: the SAE driving-automation levels (§6), which pin pur-
pose and own failure in the same places we do, and close
with theopen problems(§7) that separate the definition from
its practical realization.
2 AI for Systems Today, and Why Now
Machine learning for systems (ML4Sys) works, and it ships.
Learned index structures [10], learning-based memory allo-
cation in production server workloads [13], admission opti-
mization for datacenter flash caches [25], learned eviction
arXiv:2607.21659v1  [cs.AI]  22 Jul 2026

Cheng Tan
for a large content-delivery network [ 21], learned virtual-
machine NUMA placement [ 27], and lifetime-prediction-
driven VM scheduling have all reached real deployments.
These are genuine successes. But they are alsonarrow:
each is an expensive, component-scoped effort, hand-built
and hand-maintained by a team that understood both the
model and the subsystem. ML for systems is a collection of
point solutions, not a pervasive, self-sustaining property of
how systems are built and evolved. That gap—between real
component wins and systemic adoption—is what motivates
this paper.
2.1 Why classic ML4Sys stayed narrow
The reason is not that the models were bad. It is that aresident
learned component—for example, a neural network that exe-
cutes on the live path [11]—carries operational costs a small
heuristic does not, and those costs keep every deployment ex-
pensive and supervised. For classic ML4Sys deployment, five
challenges remain, and each is a reason an ML4Sys model
stays expensive to own.
Runtime overhead.Systems components run under punish-
ing latency budgets: a cache replacement resolves in nanosec-
onds, an allocator or scheduler fires easily thousands of times
per second. Neural inference—even a small MLP—frequently
costs more than the operation it optimizes, and the cost is not
only the forward pass but feature collection, preprocessing,
and acting on the prediction. Charged on the critical path
at decision frequency, a learned component is often a net
slowdowneven when its decisions are qualitatively better.
Distribution shift.Workloads are nonstationary—diurnal
cycles, load spikes, new query shapes, data growth, tenant
churn. A model trained on one regime degrades off it, and
learned indexes are the canonical case: excellent on static
read-only data, they force expensive retraining or lose per-
formance under insertions. Research benchmarks on fixed
traces hide this and inflate apparent gains. In production a
mediocre-but-robust heuristic often beats a policy that is
excellent on its training distribution and unpredictable off it,
and the cost of keeping the model aligned—detecting drift,
retraining, revalidating, redeploying—is a continuous tax
heuristics never incur.
Tail behavior.Engineers care about p99/p999 and worst-
case bounds, not averages, and learned approaches are dou-
bly mismatched. Tail events are rare, so they are underrepre-
sented in any collected dataset: the model has little signal
about exactly the regime that matters. And the objective
works against the tail: minimizing an aggregate loss is domi-
nated by the common case, so the optimizer will trade away
tail behavior for a small average gain. Classical heuristics
come with understood worst-case bounds; learned compo-
nents usually offer good average-case behavior with no guar-
antee where a single bad decision can cause a latency spike
or an SLA violation. Recovering guarantees for a resident net-
work is possible but demands its own apparatus—verifying
the network against systems specifications, and generating
those specifications in the first place [11, 22]—which adds to
the operational costs.
Maintainability.A 50-line heuristic becomes an ML pipeline:
training infrastructure, feature stores, model versioning, drift
monitoring, retraining triggers, and a serving path—each a
new dependency and failure mode. Debugging inverts too: a
misbehaving heuristic can be read and patched; a misbehav-
ing network offers no comparably direct account of why it
evicted a line. Systems software has long lifespans and con-
servative deployment cultures, so operators are reasonably
reluctant to adopt an opaque component whose bookkeep-
ing never ends and whose marginal gains rarely justify its
lifetime maintenance costs.
Expertise.Applying ML to a component requires deep skill
in two domains at once—expertise in machine learning and
systems—and the combination is rare. It bites hardest in the
data, labels, and reward: knowing which workloads matter,
what the “right” decision is (often a systems question, some-
times unavailable because only the counterfactual would
reveal it), and how to encode value including the tail. Get
any wrong and the model looks good on paper and fails, or
is dangerous, in production.
None of this says ML for systemsfailed. It says the resident-
model form—occupancy of the hot path—does not generalize
into a way ofbuildingsystems. Every barrier above is a cost
of making a modelexecuteon the live path; none is intrinsic
to letting a modelshapethe system off it.
2.2 What changed today
The mode of use changed. Agentic systems nowauthorsys-
tems code rather than reside inside it: they discover new
algorithms, evolve implementations directly, and vet candi-
dates through benchmarking and verification [4, 17]. The AI
moves fromoccupyinga decision—a model on the hot path,
deciding each event—toauthoring the codethat decides, in
a control plane that runs far off the critical path. Maas et al.
name the resulting shape: a slow control plane where models
reason about long-tail policy and generate code, and a fast
data plane where the generated code executes with minimal
latency [14]. Early explorations already ask whether an LLM
can stand in for hand-tuned system policies outright [ 26].
This dissolves the five barriers at a stroke, because they were
all costs ofresidency: authored code pays no inference over-
head on the hot path, is re-authorable when the workload
shifts, can be verified for tail behavior before it ships, is as
maintainable as the code a human would have written, and
shifts the expertise burden onto the agent.
This is why the moment matters. For the first time it is
feasible to let an AI continuously revise a system’s own
implementation—not just retune its knobs—under human-set

Defining AI-Native Systems:
Autonomy as Revision Authority
goals. That capability is as consequential as it is hazardous,
and the field has no rigorous account of the system property
it creates, nor of the guardrails that must bound it. Providing—
or at least sketching—such an account is the task of the rest
of this paper.
3 A Decision-Level View of a System
To say precisely what authority an AI holds, we need a vocab-
ulary for the decisions a system makes. This section builds
one. We model a system as a collection of decision points
related by a dominance order, stratify that order into levels
by binding time, and then argue that the resulting structure
isall there is: every decision that affects system behavior
lands at one level or on one of two orthogonal axes. The
definition of §5 then has somewhere to stand.
3.1 Decision points, deciders, dominance
Workloads.Let 𝑊 be the space of workloads. A workload
𝑤∈𝑊 is a stochastic process generating the inputs, requests,
and environmental conditions the system encounters. Work-
loads are nonstationary: the active workload at time𝑡 is𝑤𝑡,
and the gap between𝑤𝑡 and whatever the system was last
tuned for is the pressure every adaptation mechanism exists
to relieve.
Decision points.Adecision pointis a triple 𝑑=(𝑋,𝐼,𝐽) : an
option space𝑋 of admissible choices, the information𝐼 avail-
able when the choice is made, and an evaluation criterion
𝐽 :𝑋×𝑊→R (latency, throughput, tail-bound satisfaction).
Decision and decider.Adecisionat a decision point 𝑑 se-
lects𝑥∈𝑑.𝑋 given information𝑖∈𝑑.𝐼 . Adeciderfor 𝑑 is
any map𝛿 :𝐼→𝑋 ; deciders range over humans, static rules,
heuristics, classic ML models, neural networks, and LLM
agents. Two questions must be kept apart:who decides(the
decider𝛿 occupying𝑑) andwho may change the decider(the
authority to revise). Conflating them is the error the rest of
the paper is built to avoid.
Dominance.Decision point 𝑑 dominates𝑑′, written𝑑≻𝑑 ′,
if the outcome chosen at𝑑 determines the option space, in-
formation structure, or evaluation criterion of𝑑′. Choosing
at𝑑 does notanswer 𝑑′; it defines what𝑑′ even is. Choosing
a storage architecture fixes which algorithms are admissible;
an algorithm fixes which parameters exist; a parameter set-
ting fixes which runtime actions are possible. The levels are
the strata of this order.
Binding time.Each decision has abinding time; that is, the
point in the system’s life cycle at which its outcome becomes
fixed. Reading the dominance order by binding time is what
makes the level classification comprehensive (§3.5).
3.2 The four levels
Stratifying≻ by binding time yields four levels (L1–L4) inside
the artifact, generated by one recursion spelled out in §3.3.
• L1: Design.An L1 decision selects the decision archi-
tecture itself—the system’s design: the set of top-level
components, the interfaces between them, the objective
(e.g.,whichstatistics matter—mean vs. p999), and the cor-
rectness invariants and worst-case constraints. Fixing the
design𝐷 thereby determines𝑃𝐷, the set of implementa-
tions admissible at all. Examples: whether there is a buffer
pool with an eviction decision at all; the storage/compute
split; the SLA; which invariants may never be violated.
• L2: Implementation.An L2 decision selects a program
𝑝∈𝑃 𝐷 behind a fixed interface, thereby fixing both the
policy family Θ𝑝 that L3 can express and the represen-
tation in which those L3 objects live. Examples: a hash
index vs. a B-tree behind one lookup interface; which algo-
rithm implements the scheduler; replacing a formula with
a lookup table; whether the policy family is “threshold
rules” or “a small decision tree. ”
• L3: Policy.An L3 decision selects a policy 𝜃∈Θ 𝑝 from
the family the current implementation exposes, binding
the map𝜋𝜃 : 𝑆×𝐼→𝐴 (with𝑆 the system state,𝐼 the
observed information, and 𝐴 the action space); it gen-
erates every subsequent L4 decision. Examples: LRU vs.
LFU behind a flag; a cost model’s constants; an admission
threshold; timeout and retry parameters; and the trained
weights of a runtime ML model.
• L4: Runtime.An L4 decision is a single application of the
current policy: given runtime state𝑠 and observation𝑖,
select action𝑎∈𝐴 𝑠, consumed the moment it is made. Ex-
amples: evictthisline; schedulethistask; takethisbranch;
choosethisjoin order.
Above L1 sitsL0, thepurpose—what the system is for, which
workloads matter, what “correct” means. L0 dominates L1 in
the sense of≻ and, we will argue, must stay human-owned.
Runtime ML, classified.A learned component in the clas-
sical ML-for-systems sense decomposes exactly onto these
levels: its weights are an L3 object selected by a training
procedure (an L3 decider), and its forward pass is an L4
decider whose cost is charged per triggering event. The par-
adigm thus pays L4-frequency costs to exploit L3-frequency
learning—which is precisely the runtime-overhead barrier
of §2.
3.3 The decision-level hierarchy
The four levels are not an arbitrary list; they are generated
by one recursion:
A level-𝑘 decision selects an element of a space
that the level-(𝑘−1)decision produced.
𝐷 (L1) defines 𝑃𝐷;𝑝∈𝑃 𝐷 (L2) defines Θ𝑝;𝜃∈Θ 𝑝 (L3)
defines𝜋𝜃 ;𝜋𝜃 (L4) defines the action. Equivalently, each level
is a stratum of≻: L1≻ L2≻ L3≻ L4, and within a stratum
no decision dominates another.

Cheng Tan
L1 L2 L3 L4
design impl. policy runtime
Binding time design compile config execution
Decision frequency rare low medium extreme
Per-decision stakes extreme high medium tiny
Latency to decide months days ms–hrs ns–ms
Revision cost interfaces code params –
Decider today human human + agent tuner code
Table 1.The four in-artifact levels with two opposed gradi-
ents: per-decision stakes grow upward exactly as frequency
grows downward. This opposition is the formal content of
the runtime-overhead barrier: expensive deciders are afford-
able only where decision frequency is low, and L4’s frequency
excludes expensive deciders.
Table 1 lays out the binding time, frequency, and stakes
of each level, and it explains why one cannot simply “put
the smart thing on the hot path”: the level whose decisions
matter least per event is the one that fires a billion times
a second, and it admits only the cheapest decider. Intelli-
gence has to act where it is affordable—at L2 and L3—and let
compiled code carry L4.
3.4 Adaptation, formally
Definition(Adaptation at level 𝑘).An adaptation at level 𝑘
is a revision of the level-𝑘 selection, triggered by information
observed after the original selection, holding all levels above 𝑘
fixed:
𝑥𝑘→𝑥′ 𝑘 with𝑥 <𝑘 fixed, triggered byΔ𝑤.
Under this definition, online tuning and retraining are L3
adaptation; an agent rewriting the eviction routine against
fresh traces is L2 adaptation; re-architecting interfaces is
L1 adaptation. L4 admitsnoadaptation: an L4 decision is
consumed at its binding time, so only its generators (L3 and
above) can adapt. Theadaptive rangeof a system is the set
of levels at which it can adapt without human intervention.
Classical systems have adaptive range {L3} at most, and
typically only within a small hand-designed Θ (i.e., a policy
set at L3). Everything the next two sections grade is a claim
about adaptive range and aboutwhotriggers movement
within it.
3.5 Are the four levels comprehensive?
A stratification is only worth building a definition on if it is
complete. We claim the levels are comprehensive in a precise,
bounded sense, and we are equally precise about where the
boundary lies, because the two places the vertical hierarchy
cannotsee are exactly where the AI-native definition does
its work.
Claim 1(Closure within artifact scope).Fix a representation
convention𝑅 (what counts as “code” vs. “data”). Then every
decision whose outcome affects the system’s behavior on some
workload belongs to exactly one of L1–L4.
Argument. Classify by binding time and revision cost. Either
the decision binds at execution—L4—or it binds earlier. If
earlier, either it is revisable without changing code under𝑅—
L3—or it requires changing code. If it requires changing code,
either the change respects the current interfaces, objective,
and invariants—L2—or it does not—L1. The four cases are
exhaustive and mutually exclusive by construction.□
The claim is real, but its scope is exactly the phrase “within
artifact scope. ” Three caveats bound it, and each names some-
thing the linear hierarchy cannot represent, and each turns
out to be essential for the definition of AI-native systems.
(a) The L2/L3 boundary is conventional, not intrinsic.
Whether a quantity is a “parameter” or “code” is itself a
design choice. A threshold in a config file is L3; the same
threshold as a compiled-in constant is L2; a policy encoded
as an interpreted rule table is L3 under the interpreter but
L2 if compiled. Indeed, the level structure reflects a continu-
ous binding-time spectrum, and the partition depends on𝑅,
which is decided at L1.
This is not a defect but a design choice:a designer can
move a decision between levels—widening Θ𝑝 pushes an L2
decision down to L3, where adaptation is cheaper. Much
of what “AI-native architecture” should mean is choosing
𝑅 so the decisions that drift fastest live at the levels where
revising them costs least.
(b) The hierarchy is missing its top: L0.L1 selects system
design, but choosingwhat the system is for—which work-
loads matter, what the SLA should be, what “correct” means—
dominates L1 in the sense of≻ and is a distinct decision. Call
it L0. It is cleanly separable: two teams can share L0 (same
purpose, same SLA) and diverge at L1 (different architec-
tures). Folding L0 into L1 hides precisely the level every
capability account leaves human. Making L0 explicit is what
lets a definition saywhereautonomy stops.
(c) Two whole axes escape the vertical hierarchy.The
levels classify decisionsinsidethe artifact. Two families of
decisions affect behavior fromoutsideit:
• The allocation axis 𝛼.For each decision point 𝑑, some
process selects the decider𝛿𝑑—who or what decides here,
with what fallback, revised when. These are decisions
about the decision structure, not about behavior, and they
attach orthogonally to every level (one asks “who de-
cides?” of an L3 tuning as of an L4 eviction). The allo-
cation map𝛼, which assigns a decider to each decision
point, has no home on a purely vertical axis.

Defining AI-Native Systems:
Autonomy as Revision Authority
• The verification axis 𝜌.Whether a candidate revision
is valid, when it deploys, how it rolls back, what is mon-
itored, when drift triggers regeneration. These bindbe-
tweenversions of the artifact rather than within one.
Collapsing them into L2 loses the operational distinction
that matters most: an L2 decisionproducesa candidate; a
𝜌decisionadmitsit.
Verdict.The four levels are comprehensive as a stratification
of in-artifact decisions by binding time, relative to a fixed𝑅.
However, they arenota complete map of the decision land-
scape an AI-native definition must range over. The complete
picture is a vertical hierarchy of five levels crossed with two
orthogonal axes:
L0| {z }
purpose
≻L1≻L2≻L3≻L4|                  {z                  }
artifact axis
×𝛼 | {z }
allocation
×𝜌
| {z }
verification
.
The definition that follows (§5) factors cleanly along exactly
these three directions—adaptive range on the vertical axis,
authority over𝛼, constraint by𝜌, with the human residue
pinned at L0.
3.6 Occupancy versus revision authority
The pivotal move, which the allocation axis makes available,
is to separate two questions the field routinely runs together.
Occupancy:who executes the selection at a decision point—
compiled code, a lookup table, or a neural policy’s forward
pass?Revision authority:who is allowed tochangethat de-
cision when the workload demands it? A learned eviction
policyoccupiesL4—its forward pass is the decider—while
holding revision authority over nothing: it cannot re-tune
its own weights, rewrite its serving code, or alter its design.
A human installs it and a human maintains it.Occupancy
without revision authority is not autonomy; it is an expensive
resident.Autonomy is a claim about revision authority, and
that is the axis the next two sections climb. Table 2 presents
several canonical examples that illustrate these differences.
4 The Revision-Authority Ladder
We now grade systems byrevision authority: the highest
level at which an AI process can perform adaptation au-
tonomously.
Definition(Autonomy ceiling).Theautonomy ceilingof
a system is the highest level Lk in the dominance order ≻ at
which an AI process can perform adaptation autonomously—
i.e., at which Lk lies in the adaptive range with an AI as the
adapting decider. Grade Sk names a system with ceiling Lk.
Two structural facts fix the shape of the ladder. First, be-
cause a level-𝑘 selection re-parameterizes every level below
it (the generating rule of §3.3), revision authority iscumula-
tive downward: authority at Lk without authority at the level
just below it is incoherent, since selecting a new 𝑝 entails
selecting an initial 𝜃∈Θ 𝑝, and selecting a new 𝐷 entails
selecting an initial𝑝∈𝑃 𝐷. A grade-𝑘 system therefore has
adaptive range covering L3 through Lk under AI authority.
Second, L4 is excluded from the ladder by the formalism
itself: an L4 decision is consumed at binding time and admits
no adaptation (§3.4). “Autonomy at L4” is a category error,
so the ladder has exactly three grades, each indexed by the
level it governs.
Off-ladder: model-residency.A system isModel-Resident
iff some runtime decision point is occupied by a learned
model:𝛼(𝑑)=𝜋 𝜃 with𝜃 selected by training. This is an
occupancyproperty, not a grade: the weights are an L3 object
and the forward pass an L4 decider, and a Model-Resident
component may sit inside a system of any grade or none.
Crucially, it confers no autonomy by itself—a learned index
bolted into a database revises nothing; a human made the
allocation once and a human maintains it. A large body
of ML for systems optimized occupancy of the one level
where adaptation is undefined, while the ladder below stood
unclimbed.
S3: Self-Tuning.An AI process𝜏 revises the policy𝜃 within
the family the implementation exposes (𝜃→𝜃 ′, with𝑝 and
𝐷 fixed): autoscalers with fitted forecasters, knob tuners,
self-tuning database configurations. Runtime ML is the de-
generate case—𝜏 is a training loop, the L3 object a weight
vector, the L4 occupant the resulting forward pass. Its con-
stitutive failure issaturation: when Δ𝑤 outruns what Θ𝑝
can express, no 𝜃′ recovers, and the degradation is silent,
because “is Θ𝑝 still the right family?” is an L2 question, one
level above the system’s authority. An S3 system cannot even
represent its own inadequacy. This is the classical ceiling:
essentially every adaptive system built before LLM coding
agents is S3 or below.
S2: Self-Rewriting.An AI process 𝜎 synthesizes a new
implementation𝑝′∈𝑃 𝐷 behind the same interfaces (𝑝→𝑝 ′,
design fixed): swap the threshold rule for a decision tree, the
hash index for a range index, re-derive the eviction routine
against fresh traces. This is the level that was out of reach
before, because revising an implementation means writing
code against a specification—exactly what agentic synthesis
now does [4, 17].
Two clauses are constitutive at S2 that were optional at
S3.(i) Escalation.Anescalation detector 𝜀 maps evidence
of saturated L3 adaptation to an L2 regeneration trigger,
turning “my tuning has stopped working” into a signal rather
than an incident; it is the genuinely novel object at this
level—a decision procedure over the adequacy of decision
procedures.(ii) 𝜌-verification.Every candidate revision
passes a verification procedure𝜌—validation suites, invariant
checks, trace replay, adversarial probes—with a verified non-
AI fallback retained, so the deployed artifact is fallback⊕𝑝 ′
and its worst case is the fallback’s by construction. S2 without
𝜌is not a maturity grade; it is an incident generator.

Cheng Tan
Decision Level Notes
Evict this cache line now L4 consumed per event
Cache policy=LRU (runtime flag) L3 parameter under𝑅
Cache policy=LRU (only policy compiled in) L2 needs a code change
Neural eviction model’s weights L3 training is an L3 decider
its forward pass L4 inference charged per event
B-tree→learned index, same API L2 interfaces preserved
Add an observable feature to eviction state L1 changes𝑆, hence𝐼below
“p999<2 ms is the goal” L0 dominates𝐽at L1
“Agent tunes; humans approve diffs”𝛼attaches to L3/L2
“Every policy must pass the trace suite”𝜌admission, not behavior
Table 2.Worked classifications. The last two rows fall on the orthogonal axes: allocation𝛼and verification procedure𝜌.
S1: Self-Architecting.An AI process revises thedesignit-
self, including the convention𝑅 that fixes what counts as a
parameter versus code, subject only to a human-owned L0.
Three properties make S1 qualitatively, not incrementally,
harder: revising design changes what 𝜌 is(self-referential
validation—who checks the checker after it is rewritten?); au-
thority over𝑅 lets the systemre-stratify, moving fast-drifting
decisions to cheaper levels; and L1 revision is interface rene-
gotiation with external stakeholders, so the practical ceiling
isS1 within a negotiated envelope, not unbounded self-design.
This tier is aspirational; §7 returns to its obstacle.
Weak and strong forms.Each grade admits aweakform,
written weak-Sk, in which the AI has the revisioncapa-
bilitybut the trigger is external—a human or a schedule
invokes regeneration—and astrongform, Sk, that adds the
autonomous trigger (for S2, the escalation detector𝜀; for S1,
an analogous detector over design adequacy). The distinction
is where the value lives: an organization running an agent
that rewrites heuristicson requesthas a weak-S2 system—
synthesis cost has collapsed, but drift detection remains a
human task. The step from weak-S2 to strong-S2 automates
thetrigger, not the synthesis, and that is where most of the
drift-robustness value sits.
Crucially, climbing this ladder doesnotmove intelligence
onto the hot path. The correct occupant of L4 is compiled
code at every grade—𝜎’s output is aprogram, and programs
are what run at L4. The AI works at development time and
between versions, at L2 and L3 frequency, where its cost is
affordable. This is the same control-plane/data-plane split
that Maas et al. argue for on capability grounds [14]: heavy
reasoning authors code off the critical path; cheap generated
code executes on it. Our contribution is not that architecture
but agovernanceaccount of it: who may revise what, and
under which guarantees, which we define in the next section.
5 AI-Native, Defined
An AI-native system is not a system that contains AI models.
It is a system whoselife cycle—the cycle that revises the sys-
tem as the world changes—has been handed, under bounds,
to an AI process. We define it by three factors, one per axis
of §3, all bound by a human-owned envelope:
Definition(AI-Native System).A system isAI-nativeif and
only if it satisfies all of the following conditions:
1. Strong-S2 autonomy.An AI autonomously revises sys-
tem implementations and, via the escalation detector 𝜀,
autonomously determines when such revisions are needed.
2. Allocation authority.An AI controls the allocation map
𝛼 across levels L2–L4. At each decision point, it determines
which decider occupies that point and may reassign the
decider as cost and workload change.
3.𝜌 -verified revision.Every AI-generated revision is subject
to the verification procedure 𝜌, and the system retains a
verified non-AI fallback implementation.
4. Human-owned envelope.Level L0, together with the ob-
jective and invariants of L1, remains under human owner-
ship and constrains all AI authority in the levels below.
Compactly:AI-native = strong-S2×𝛼 -authority×𝜌 -
verification, under a human-owned envelope.Each fac-
tor answers a distinct need.Strong-S2supplies the revision
authority a resident model lacks, and its escalation detector𝜀
is the direct remedy for silent drift: the system turns “my pol-
icy has stopped working” into a signal instead of an incident.
𝛼-authoritykeeps compiled code on the data path and lets
the AI place an expensive decider only where its frequency
can amortize it.𝜌-verificationmakes autonomous rewriting
survivable: because the deployed artifact is fallback⊕𝑝 ′, the
worst case of the composite is that of the verified fallback,
given a bounded, reversible switch with no cross-version
state corruption—the runtime-assurance pattern of the Sim-
plex architecture [20]. And thehuman-owned envelopemarks

Defining AI-Native Systems:
Autonomy as Revision Authority
Grade Certificate Auditable by
S3 Tuning log:(Δ𝑤, 𝜃→𝜃 ′,outcome)
triples
monitoring re-
view
S2 Code diff 𝑝→𝑝 ′ with passing 𝜌
record,𝜀trigger, retained fallback
ordinary code
review
S1 Re-derived𝐷′ and 𝜌′ with an argu-
ment that𝜌′ preserves the invariants
design review
(human)
Table 3.Certificates by grade. The S1 row shows why it
is hard: the certificate must include a re-derived admission
process a human can still audit, which caps the admissible
complexity of any redesign at human comprehension.
System Grade
B-tree with hand-tuned fill factor none
Learned index in production DB none (Model-Resident)
Autoscaler with fitted forecaster S3
Online-retrained learned cache S3 (Model-Resident)
Agent re-derives eviction code on request weak-S2
+ drift monitor triggers it, fallback retained S2
+ AI also (re)assigns per-point decidersAI-native
Table 4.The definition applied. Autonomy climbs by au-
tomating thetriggerand wideningauthority, not by making
the resident model smarter.
where autonomy stops: the AI may rewrite how the system
pursues its purpose, never what its purpose is.
The three factors are exactly the three axes of the extended
decision landscape of §3.5—adaptive range on the vertical
hierarchy, the allocation axis𝛼, and the verification axis𝜌—
with the human residue pinned at L0. That the definition
factors cleanly along these axes is evidence it carves the
space at its joints rather than stipulating a checklist.
Grade membership.Grade membership should be demon-
strated by an artifact, not claimed. Thecertificateof a grade
is the object whose existence and auditability establishes
the authority (Table 3). The certificate of an AI-native sys-
tem is the S2 row: an auditable, verified code diff 𝑝→𝑝 ′
carrying its passing𝜌 record, its𝜀 trigger evidence, and its
retained fallback—an artifact an ordinary code review can
check. Autonomy you cannot audit is not a grade.
The definition at work.Table 4 runs representative sys-
tems through the definition. The pattern to read off it: oc-
cupancy varies freely (models, code, agents appear at every
row) while the grade tracks only revision authority, and AI-
native is the single row where strong-S2,𝛼-authority, and𝜌
hold together.
SAE Systems analog Grade
L0–L1 Humans revise everything; at most
a tiny hand-tunedΘ
none
L2 Runtime ML bolted in: a learned
component on the hot path, a hu-
man babysits drift and rollback
Model-
Resident
(+S3)
L3 Agent-maintained heuristics: L3
re-tunes autonomously, structural
drift triggers L2 regeneration or
handoff
weak-S2 →
S2
L4 Autonomous rewriting within a
human-owned spec, verified fall-
back owning the worst case
S2 / AI-
native
L5 AI authority over the design𝐷 it-
self
S1 (aspira-
tional)
Table 5.The SAE driving-automation levels mapped onto
the revision-authority grades. The mapping is exact only
after Lesson 4 relocates the comparison from the vehicle to
the fleet loop.
Compared with recent related efforts.This definition
grades a different object than the recent capability taxonomies,
and is orthogonal to both. Maas et al. ask how muchintelli-
gencea problem demands; Feng et al. ask how capable anAI
is at systems research [7, 14]. We ask how asystemgoverns
its own evolution. The axes are independent: a system built
entirely on narrow, “low-capability” ML can be AI-native if
an agent rewrites its heuristics under𝜌-verification, while
a one-off superhuman result from an algorithm-discovery
run isnotAI-native, because it holds no standing authority
and closes no loop. The paradigm shift AI-native names is in
who holds revision authority, not in how smart the resident
model is.
6 A Precedent: Driving Automation
The definition’s shape is not unique to systems. The SAE
J3016 driving-automation levels are the best-known prece-
dent for grading autonomy not by intelligence but bywhich
decisions the machine holds, within what bounds, and who
owns failure[ 19]. A decade of automotive autonomy paid, in
engineering effort, for lessons the systems community can
now read off rather than re-learn.
6.1 The mapping
Three correspondences beneath Table 5 are structural, not
decorative.
The ODD is the human-owned envelope.An SAE L4
vehicle isfullyautonomous onlywithinan operational de-
sign domain (ODD) that humans define—geography, weather,
road class. The systems counterpart is exact: L0 purpose plus
the objective and invariants of L1 bound the region in which

Cheng Tan
the agent’s revision authority is total and outside which it
is zero. In both domains, “conditional” is not a hedge on the
definition; it is what makes the definition operable.
The minimal-risk condition is the verified fallback.
What separates SAE L3 from L4 is not driving skill butfall-
back ownership: an L4 vehicle must reach a safe state with no
human available. That is precisely the𝜌-verification clause—
deployed artifact = fallback⊕ optimized policy, so the com-
posite’s worst case is the verified fallback’s by construction.
The passenger still picks the destination.Even a hypo-
thetical L5 vehicle does not choose where you are going.
Destination selection dominates the driving task in the sense
of≻—it defines what the driveis—and stays human at every
level. This is L0, independently rediscovered: full self-driving
never meant the car chooses your errands, and AI-native
must never mean the system chooses its own SLA.
6.2 Lessons borrowed
Lesson 1: the dangerous level is the middle one.The
industry’s hardest-won finding is that SAE L2 is theworst
configuration: enough autonomy to invite trust, not enough
to own failure, with a human “monitor” whose vigilance
decays exactly as the automation’s competence grows. The
translation is uncomfortable and precise—runtime ML in
productionisthe L2 configuration. A learned scheduler han-
dles the common case well enough that the human stops
watching, degrades silently under drift, and returns control
(via an incident) at the moment of maximum difficulty.
Lesson 2: progress came from the envelope, not the
model.The jump from demos to deployed L4 was achieved
by ODD specification, validation infrastructure, scenario
coverage, and fallback engineering—not by better driving
networks alone. The capability was necessary; theenvelope
made it shippable. This is the thesis of our argument arriving
from an independent direction: the path to AI-native runs
through𝜌 and the specification, not through smarter models
on the hot path.
Lesson 3: the handoff problem is the escalation de-
tector.SAE L3’s notorious difficulty is the handback: the
vehicle must know, with lead time, that it is leaving its com-
petence. This is exactly 𝜀, converting “my L3 adaptation
has saturated” into a triggerbeforesilent degradation be-
comes an SLA violation. Self-assessment is the hard capa-
bility, harder than the competence it assesses. In practice,
L3’s human handback proved so awkward that L4—machine-
owned fallback—became the more tractable target. The ana-
log: aim for verified-fallback composition rather than human-
in-the-loop handback under time pressure.
Lesson 4: autonomy lives in the loop, not the arti-
fact.The deployed vehicle is, in our vocabulary, Model-
Resident: it executes a frozen policy and revises nothing.
What made the leading programs work is thefleet loop around
it—disengagement and telemetry (drift observation), offline
re-derivation (regeneration), simulation suites (validation),
gated over-the-air deployment (admission, i.e.𝜌). That loop
is an S2 system whose artifact happens to be a driving stack.
The lesson generalizes:autonomy is a property of the
maintenance loop, not of the artifact, and asking “is this
system AI-native?” of a binary is as confused as asking it of
a single parked car. The grade attaches to the systemplus its
loop.
7 Open Problems and a Call to Build
Strong-S2 is close, and the obstacles are guardrails, not model
quality. The capability to synthesize an implementation al-
ready exists; what stands between it and an AI-native system
is the machinery that makes standing revision authority safe.
Four problems are load-bearing.
• Escalation detection (𝜀).Knowing when you don’t know
is the hard, under-studied capability. Detecting a satu-
rated policy family before it becomes an SLA violation is
the single highest-leverage piece of an AI-native system,
and it is harder than the competence it guards: it is a
decision procedure over the adequacy of decision pro-
cedures. The automotive handback problem (§6) is the
same problem in another field, and it was the one that
gated deployment there too.
• Verification and fallback composition (𝜌).Trace-replay
suites, adversarial workload probes, invariant checks, and
provably-retained fallbacks are what make autonomous
rewriting production-ready. Systems hold a real advan-
tage here: they admit cheap, reliable verifiers and simu-
lators against which a candidate can be scored without
hallucination [14], which makes 𝜌 tractable in a way
automotive simulation never fully was.
• Re-stratification.Choosing the representation 𝑅 so the
fastest-drifting decisions live at the lowest levels—where
revision is cheapest and𝜌 is lightest—may be the deepest
sense of “AI-native architecture. ” It is design work that
pays off only once the system is expected to revise itself,
which is why it has no real precedent to borrow.
• The threat surface.An AI with standing authority to
rewrite and deploy L2 code is itself an attack surface: a
crafted workload can steer synthesis or trip𝜀 adversar-
ially, and a compromised agent holds deploy authority.
Guardrails here are a prerequisite, not a refinement.
The frontier beyond strong-S2 is S1, and its difficulty is
self-referential: revising the design changes what the lev-
els beloware, including the verification procedure 𝜌, whose
suites are written against the design’s interfaces. Who checks
the checker after the checker is rewritten? An S1 certificate
must include a re-derived𝜌′ a human can still audit, which
caps the admissible complexity of any redesign at human

Defining AI-Native Systems:
Autonomy as Revision Authority
comprehension. So the practical ceiling is S1 within a nego-
tiated envelope, not unbounded self-design.
None of these is a reason to wait. Each is a concrete, build-
able artifact—a detector, a verifier, a representation, a threat
model—and the capability they would govern is already in
the field. The definition names what we are building toward;
these are the guardrails that make building it safe.
8 Related Work
Taxonomies of ML for systems.Prior efforts to organize
the AI-for-systems space classifytechniques and their fit
to problems. Maas’s taxonomy [12] provides the canonical
vocabulary for deciding whether and how ML applies to a
systems problem, and comprehensive surveys organize the
resulting literature by domain and learning paradigm [8, 24].
In our vocabulary, these works catalogoccupancy: which
decision points a learned model may reside at, and with
which method.
Capability ladders for AI.A second lineage grades theAI
rather than the system. Morris et al. [16] import the spirit
of the SAE driving-automation levels [19]. Further, Maas et
al. [14] bring this ladder to systems, introducing a human-
machine baseline and arguing that fully solving classic sys-
tem policies is “AGI-complete. ” Mitchell et al. [ 15] grade
agent autonomy by escalating authority over program flow,
topping out at agents that rewrite their own code—precisely
what our S2 grade regulates, with escalation detection and
𝜌-verification. These ladders grade what an AIcan do; ours
grades what a deployed system-plus-loopis permitted to
revise, and evidences the claim with certificates.
Autonomy in specific system domains.Domain commu-
nities have independently built autonomy ladders foroper-
atingsystems without granting them authority over their
own implementation. Autonomic computing introduced the
MAPE-K loop and the self-∗ properties under human-supplied
high-level objectives [9], a lineage the self-adaptive-systems
community has since systematized [23]. Self-driving databases [2,
18] and self-driving networks [6] pursue closed-loop opera-
tional autonomy, while the 3GPP/TM Forum autonomous-
network levels [1] grade autonomy per task category—execution,
analysis, decision, intent—with intent held human longest.
These frameworks reach at most our S3 (parameter-level
adaptation within a fixed implementation); their per-category
grading and human-held intent prefigure, respectively, our
decision-level stratification and the human-owned L0.
AI-driven systems research.Most recently, coding agents
have been applied to systems research itself. ADRS [ 3, 4]
and AlphaEvolve [17] demonstrate LLM-driven discovery
of algorithms that outperform expert baselines, treating sys-
tems as white boxes whose code the AI may rewrite offline;
Feng et al. [7] propose the SOAR dimensions and five levels
of “system intelligence” keyed to PhD-student personas, and
argue benchmarks are the binding constraint. These efforts
grade theresearch agent’scapability; the revision authority
they exercise lives in an offline loop with a human trigger—
our weak-S2. Our framework is complementary: it attaches
the grade to the deployed artifact and its maintenance loop,
makes the escalation detector (𝜀) and the verification proce-
dure (𝜌) constitutive, and pins purpose at a human-owned
L0—turning their demonstrated capability into a checkable
property of a system.
9 Conclusion
“AI-native” has been a slogan in search of a referent; we
have given it one. AI is already writing systems code and
moving into the control plane, and what has been missing
is a definition of thesystem propertythis enables: bounded
authority—verified before each change takes effect—for an AI
to revise the system’s own decisions under a human-owned
purpose. We named it, graded it, and located the guardrails
that make its building safe. The capability arrived ahead of
the discipline; the definition is the first step.
References
[1] 3GPP. 2024.Management and Orchestration; Levels of Autonomous
Network (TS 28.100, Release 18). Technical Report. 3rd Generation
Partnership Project. Mirrored as ETSI TS 128 100 V18.0.0.
[2] Dana Van Aken, Andrew Pavlo, Geoffrey J. Gordon, and Bohan Zhang.
2017. Automatic Database Management System Tuning Through
Large-scale Machine Learning. InProceedings of the 2017 ACM Inter-
national Conference on Management of Data (SIGMOD). 1009–1024.
doi:10.1145/3035918.3064029
[3] Audrey Cheng, Shu Liu, Melissa Pan, Zhifei Li, Shubham Agarwal,
Mert Cemri, Bowen Wang, Alexander Krentsel, Tian Xia, Jongseok
Park, Shuo Yang, Jeff Chen, Lakshya Agrawal, Ashwin Naren, Shulu Li,
Ruiying Ma, Aditya Desai, Jiarong Xing, Koushik Sen, Matei Zaharia,
and Ion Stoica. 2025. Let the Barbarians In: How AI Can Acceler-
ate Systems Performance Research. arXiv preprint arXiv:2512.14806.
https://arxiv.org/abs/2512.14806
[4] Audrey Cheng, Shu Liu, Melissa Pan, Zhifei Li, Bowen Wang, Alex
Krentsel, Tian Xia, Mert Cemri, Jongseok Park, Shuo Yang, Jeff Chen,
Lakshya Agrawal, Aditya Desai, Jiarong Xing, Koushik Sen, Matei
Zaharia, and Ion Stoica. 2025. Barbarians at the Gate: How AI is
Upending Systems Research.arXiv preprint arXiv:2510.06189(2025).
[5] Rohit Dwivedula, Divyanshu Saxena, Sujay Yadalam, Daehyeok Kim,
and Aditya Akella. 2025. Vulcan: Instance-Optimal Systems Heuristics
Through LLM-Driven Search.arXiv preprint arXiv:2512.25065(2025).
[6] Nick Feamster and Jennifer Rexford. 2018. Why (and How) Networks
Should Run Themselves. InProceedings of the Applied Networking
Research Workshop (ANRW). doi:10.1145/3232755.3234555
[7] Xuan Feng, Peng Cheng, Qi Chen, Shan Lu, Chieh-Jan Mike Liang,
Bogdan Alexandru Stoica, Zhongxin Guo, Jiahang Xu, Tianyin Xu,
and Lidong Zhou. 2025. Defining System Intelligence. ACM SIGOPS
Blog.https://www.sigops.org/2025/defining-system-intelligence/.
[8] Marios Evangelos Kanakis, Ramin Khalili, and Lin Wang. 2022. Ma-
chine Learning for Computer Systems and Networking: A Survey.
Comput. Surveys55, 4 (2022), 71:1–71:36. doi:10.1145/3523057
[9] Jeffrey O. Kephart and David M. Chess. 2003. The Vision of Autonomic
Computing.IEEE Computer36, 1 (2003), 41–50. doi:10.1109/MC.2003.
1160055
[10] Tim Kraska, Alex Beutel, Ed H. Chi, Jeffrey Dean, and Neoklis Polyzotis.
2018. The Case for Learned Index Structures. InProceedings of the 2018

Cheng Tan
International Conference on Management of Data (SIGMOD). 489–504.
[11] Shuyi Lin, Haoyu He, Tianhao Wei, Kaidi Xu, Huan Zhang, Gagandeep
Singh, Changliu Liu, and Cheng Tan. 2024. NN4SysBench: Character-
izing Neural Network Verification for Computer Systems. InAdvances
in Neural Information Processing Systems 37 (NeurIPS), Datasets and
Benchmarks Track.https://openreview.net/forum?id=mhjRudcHcB
[12] Martin Maas. 2020. A Taxonomy of ML for Systems Problems.IEEE
Micro40, 5 (2020), 8–16. doi:10.1109/MM.2020.3012883
[13] Martin Maas, David G. Andersen, Michael Isard, Mohammad Mahdi Ja-
vanmard, Kathryn S. McKinley, and Colin Raffel. 2020. Learning-based
Memory Allocation for C++ Server Workloads. InProceedings of the
25th International Conference on Architectural Support for Programming
Languages and Operating Systems (ASPLOS).
[14] Martin Maas, Milad Hashemi, Kathryn McKinley, and Parthasarathy
Ranganathan. 2026. AI for Systems is “AGI-Complete”.ACM SIGOPS
Operating Systems Review60, 1 (2026), 21–29.
[15] Margaret Mitchell, Avijit Ghosh, Alexandra Sasha Luccioni, and Giada
Pistilli. 2025. Fully Autonomous AI Agents Should Not be Developed.
arXiv preprint arXiv:2502.02649.https://arxiv.org/abs/2502.02649
[16] Meredith Ringel Morris, Jascha Sohl-Dickstein, Noah Fiedel, Tris
Warkentin, Allan Dafoe, Aleksandra Faust, Clement Farabet, and
Shane Legg. 2024. Position: Levels of AGI for Operationalizing
Progress on the Path to AGI. InProceedings of the 41st International
Conference on Machine Learning (ICML) (Proceedings of Machine Learn-
ing Research, Vol. 235). PMLR, 36308–36321.https://proceedings.mlr.
press/v235/morris24b.html
[17] Alexander Novikov, Ngân V ˜u, Marvin Eisenberger, et al . 2025. Al-
phaEvolve: A Coding Agent for Scientific and Algorithmic Discovery.
arXiv preprint arXiv:2506.13131(2025).
[18] Andrew Pavlo, Gustavo Angulo, Joy Arulraj, Haibin Lin, Jiexi Lin, Lin
Ma, Prashanth Menon, Todd C. Mowry, Matthew Perron, Ian Quah,
Siddharth Santurkar, Anthony Tomasic, Skye Toor, Dana Van Aken,
Ziqi Wang, Yingjun Wu, Ran Xian, and Tieying Zhang. 2017. Self-
Driving Database Management Systems. In8th Biennial Conference on
Innovative Data Systems Research (CIDR).
[19] SAE International. 2021.Taxonomy and Definitions for Terms Related
to Driving Automation Systems for On-Road Motor Vehicles. Technical
Report J3016_202104. SAE International.
[20] Lui Sha. 2001. Using Simplicity to Control Complexity.IEEE Software
18, 4 (2001), 20–28.
[21] Zhenyu Song, Kevin Chen, Nikhil Sarda, Deniz Altınbüken, Eugene
Brevdo, Jimmy Coleman, Xiao Ju, Pawel Jurczyk, Richard Schooler,
and Ramki Gummadi. 2023. HALP: Heuristic Aided Learned Prefer-
ence Eviction Policy for YouTube Content Delivery Network. In20th
USENIX Symposium on Networked Systems Design and Implementation
(NSDI). 1149–1163.
[22] Cheng Tan, Changliu Liu, Zhihao Jia, and Tianhao Wei. 2023. Building
Verified Neural Networks for Computer Systems with Ouroboros. In
Proceedings of Machine Learning and Systems (MLSys), Vol. 5.
[23] Danny Weyns. 2020.An Introduction to Self-Adaptive Systems: A Con-
temporary Software Engineering Perspective. Wiley-IEEE Press.
[24] Nan Wu and Yuan Xie. 2023. A Survey of Machine Learning for
Computer Architecture and Systems.Comput. Surveys55, 3 (2023),
54:1–54:39. doi:10.1145/3494523
[25] Tzu-Wei Yang, Seth Pollen, Mustafa Uysal, Arif Merchant, and Homer
Wolfmeister. 2022. CacheSack: Admission Optimization for Google
Datacenter Flash Caches. In2022 USENIX Annual Technical Conference
(USENIX ATC). 1021–1036.
[26] Yibo Zhao and Cheng Tan. 2025. Can LLMs Replace Time-Tested
System Policies? Perhaps. InProceedings of the 16th ACM SIGOPS Asia-
Pacific Workshop on Systems (APSys). 168–175. doi:10.1145/3725783.
3764405
[27] Yibo Zhao, Tianyuan Wu, Hui Xue, Qi Chen, Zhenhua Han, Zikai
Xu, Yuntai Chang, Rui Gao, Steve Deng, Jui-Hao Chiang, Mingxia Li,
Yuqing Yang, Cheng Tan, Fan Yang, Peng Cheng, Yongqiang Xiong,
Lili Qiu, and Lidong Zhou. 2026. Virtual Machine NUMA Placement at
Scale: Learning the Norm, Shielding the Tail. InProceedings of Machine
Learning and Systems (MLSys).
