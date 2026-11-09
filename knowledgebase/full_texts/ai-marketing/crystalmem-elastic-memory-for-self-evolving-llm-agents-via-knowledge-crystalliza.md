---
title: 'CrystalMem: Elastic Memory for Self-Evolving LLM Agents via Knowledge Crystallization'
url: https://arxiv.org/abs/2608.00303
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Beining Wu
- Jun Huang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.00303
pages: 13
chars: 67966
fetched_at: '2026-11-08T13:34:54+00:00'
kb_version: 1
---

# CrystalMem: Elastic Memory for Self-Evolving LLM Agents via Knowledge Crystallization

PREPRINT 1
CrystalMem: Elastic Memory for Self-Evolving
LLM Agents via Knowledge Crystallization
Beining Wu,Member, IEEE,and Jun Huang,Senior Member, IEEE
Abstract—Memory for self-evolving large language model (LLM) agents is often provisioned as if its byte budget only grows. Cloud
platforms, however, adjust quotas with load and cost, and we show that capability does not follow the budget back up: after a
squeeze-and-recover cycle, the agent settles below its pre-squeeze level, a gap we callmemory hysteresis. The cause is structural.
Deletion and one-way compression discard the material needed for later rebuilding, and we prove that any policy that only keeps or
drops entries carries a residual-deficit floor. We propose CrystalMem (CrystallizedMem ory), an elastic memory sidecar that demotes
entries across four fidelity states under a crystallization-energy schedule, orders demotions by advantage-weighted influence with
dependency coupling, and recovers capability through verified recrystallization under explicit compute and byte caps. Across seven
environments, seventeen methods, and six backbones, with multi-tenant serving and a physical edge–cloud deployment, CrystalMem
achieves the highest restored capability in every setting and closes the loop left open by every baseline. From a50%byte budget,
CrystalMem matches the strongest budgeted baseline at full provision on every environment; at equal budgets, it leads by+4.6pp on
average.
Index Terms—Agent memory, self-evolving LLM agents, knowledge crystallization, elastic resource management, cloud computing,
LLM serving, memory management, energy efficiency.
✦
1 INTRODUCTION
S
ELF-evolving large language model (LLM) agents im-
prove by accumulating experience. Trajectories, distilled
skills, and facts are written to an external memory and
retrieved for later tasks [1], [2], [3], [4], [5], [6], [7]. Pro-
duction systems now treat this store as a managed memory
plane, with consolidation pipelines [8], [9], [10] and value-
based governance [11], [12], [13], [14], [15] deciding what
stays. One layer below, the cloud serving stack already
treats resources as elastic: compute is scheduled [16], [17],
[18], [19], [20], [21], [22], the key–value cache is paged
and reclaimed [23], and quotas move with load and cost.
Agent memory is the exception. Its byte budget is usually
provisioned as if it could only grow, although a shared cloud
offers no such guarantee.
Budgets move in every other tier, but prior work has not
asked what a round trip of the memory budget does to agent
capability. Our measurements show that capability does not
simply return with the bytes. When the quota falls, current
stores shed bytes by deleting entries or by compressing
them in one direction; both choices discard material that
would be needed to rebuild the entry later. When the
quota returns, nothing regenerates. The agent settles below
its pre-squeeze level even though the original provision
is fully available again (Figs. 1 and 2). We call this gap
memory hysteresis: the store’s capability depends not only
on the budget it has, but also on the path the budget took.
Retention therefore has to become reversible. Compression
ladders that demote entries into coarser representations [24]
•Beining Wu and Jun Huang are with the Department of Electrical Engi-
neering and Computer Science, South Dakota State University, Brookings,
SD 57006 USA.
E-mail: Wu.Beining@jacks.sdstate.edu; Jun.Huang@sdstate.edu
keep more information than deletion, but they only move
downward, so each squeeze leaves a permanent loss. Re-
versible compression exists [25], yet reversibility alone does
not decide which entry to demote under a falling budget
or whether a later reconstruction is faithful. Value-based
governance chooses better survivors [11], [26], [27], [28], but
a policy that keeps an entry verbatim or drops it leaves no
residue to rebuild from. Closing the loop requires fidelity
states to demote into, a schedule that moves entries in both
directions as the budget moves, and a gate that verifies what
returns.
These requirements sit across three research lines. Agent
memory and self-evolution build stores that grow, consol-
idate, and retrieve under a fixed provision [8], [9], [10],
[29], [30]. Memory compression and governance reduce or
curate the store through one-way ladders, opportunistic
reversibility, or binary selection [11], [24], [25], [31], [32],
[33]. Elastic serving and evaluation reclaim resources below
the memory plane and measure memory at fixed provi-
sions [16], [17], [23], [34], [35], [36], [37], [38], [39], [40], [41],
[42], [43], [44]. None treats fidelity as a two-way function of
the byte budget, schedules demotion and promotion against
that budget, or verifies what a promotion brings back. As a
result, no current system closes the capability loop under an
elastic memory budget.
To close this loop, we introduce CrystalMem
(CrystallizedMem ory), an elastic memory sidecar for self-
evolving agents. CrystalMem treats retention as reversible
state assignment through two coupled mechanisms. First,
knowledge crystallizationassigns every entry to one of four
fidelity states, from full form down to a minimal trace. A
budget-driven schedule prices each demotion by the utility
it forgoes now plus the compute a later promotion will
cost, then takes the cheapest moves first until the store fits
arXiv:2608.00303v1  [cs.AI]  31 Jul 2026

PREPRINT 2
the incoming budget. Entry values come from an influence
estimator that attributes task outcomes to the entries that
served them. Value also flows over a dependency graph, so
entries that anchor other entries sink last. Second,verified
recrystallizationkeeps a residue and a set of invariants
for every demoted entry. When the budget expands, the
store regenerates entries from their residues and admits
only reconstructions that pass the invariant check, under
an explicit cap on regeneration compute. Both passes run
inside the serving path with one sorted sweep per stage
and no training. Deletion becomes the last resort instead of
the default.
In summary, our main contributions are as follows. They
divide into findings and designs: the phenomenon and
its floor are findings; the crystallization mechanisms are
designs; the serving stack and benchmark environments are
adopted from prior work and are not claimed as contribu-
tions.
•We identify and measurememory hysteresisin elastic-
budget agent memory: a squeeze-and-recover cycle
leaves capability below its pre-squeeze level even
after the budget fully returns. We formalize the effect
with a loop-area metric and prove a residual-deficit
floor for keep-or-drop policies.
•We propose CrystalMem: a four-state fidelity lad-
der scheduled by crystallization energy under the
live budget, entry values estimated from advantage-
weighted influence with dependency coupling, and
verified recrystallization under explicit compute and
byte caps. We prove feasibility, near-optimality, and
loop-closure guarantees.
•We evaluate CrystalMem against seventeen methods
across seven environments and six backbones, in
multi-tenant serving, and on a physical edge–cloud
testbed. CrystalMem closes the loop left open by
every baseline, matches full-provision capability at
half the byte budget, and recovers capability at a
fraction of the energy needed to re-experience the
underlying episodes.
The rest of this paper is organized as follows. Section 2
reviews related work. Section 3 formalizes elastic mem-
ory budgets and measures memory hysteresis. Section 4
presents CrystalMem. Section 5 reports the experimental
evaluation. Section 6 concludes the paper.
2 RELATEDWORK
2.1 Agent Memory and Self-Evolution
A self-evolving large language model (LLM) agent improves
without weight updates by writing experience into external
memory and retrieving it at inference time [1], [2], [45],
[46], [47]. One line of work builds the store itself. Xuet
al.[29] proposeA-MEM, which links and grows notes for
long-horizon recall;MemGPT[8] pages entries between the
context window and external storage;Mem0[9] extracts and
consolidates long-term memory at production scale; and
MemoryOS[10] brings operating-system structure to storage,
update, and retrieval. These systems make memory larger,
better organized, and easier to retrieve.
A second line turns experience into competence.Voy-
ager[3] grows a skill library from open-ended exploration;
Agent Workflow Memory[48] andReasoningBank[4] distill tra-
jectories into reusable workflows and strategies;EvolveR[49]
andPolySkill[50] close an experience-driven lifecycle over
skills;AutoRefine[51] keeps stored expertise current; and
MEM1[30] andMemory-as-Action[52] train the agent to
curate its own context. Across both lines, the store grows
and is trimmed under a fixed provision. The byte budget
is treated as a background constraint rather than a control
variable, and neither line asks how capability changes when
the budget shrinks and then returns.
2.2 Memory Compression and Governance
When memory must shrink, one family compresses it.
MaRS[31] summarizes episodes into reflections at a sin-
gle tier;RecMem[32] consolidates recurrently for long-
running agents;Human-Inspiredmemory [24] demotes en-
tries through a ladder of representations, but only down-
ward; andR 3Mem[25] makes compression reversible, yet
promotes opportunistically, with no budget-driven schedule
and no gate that verifies what returns. A parallel theory
line frames memory compaction as a rate–distortion trade-
off over a single compression event [53], [54], [55]. In these
systems, fidelity transitions are one-way or unscheduled;
none treats them as a two-way function of a moving byte
budget.
Closest to ours, a governance family decides which
entries deserve the bytes.CURATOR[11] scores net value
per byte and governs retention under a hard footprint;A-
MAC[33] learns what to admit at write time;AgeMem[12]
learns a unified long- and short-term management policy;
Darwinianmemory [56] lets a training-free store regulate
itself; andBudgetMem[27] learns selective retention under
explicit cost. These policies identify valuable entries, and
the strongest of them is our binary baseline. However,
each policy either keeps an entry verbatim or drops it.
Selection decides which entries survive a squeeze, but not
what fidelity the survivors should occupy or how evicted
capability should return when the budget does.
2.3 Elastic Serving and Evaluation
Elasticity is routine in the serving stack below the memory
store [57], [58], [59], [60], [61], [62], [63]. vLLM [23] manages
the key–value cache as a paged, reclaimable resource; sleep-
time compute [34] spends idle cycles preparing context
before queries arrive; and governed shared memory [35]
arbitrates a store written by many agents. These systems
reclaim serving memory or schedule maintenance compute,
but they do not tie the fidelity of an experiential store to
the byte budget it receives. CrystalMem composes with this
layer rather than replacing it.
Evaluation is beginning to measure lifecycle effects.
MemoryAgentBench[36] measures accumulation and selec-
tive forgetting over incremental interaction;Reclaim Eval[37]
finds that lossy retention can leave an agent worse off
than no memory at all; andNeuromem[64] decomposes
the streaming lifecycle of an external store into stages.
Each protocol measures at a fixed provision or at a single
degradation point, so capability that fails to return with the

PREPRINT 3
TABLE 1
Notation.
Symbol Meaning
m,D m environment index; its query distribution
q,g(q, M)query; graded outcome in[0,1]under storeM
e,µ(·)memory entry; byte measure
M s,W s store at stages; entries written during stages
bs,B 0 budget fraction at stages; provisioned bytes
S,∆ b number of stages; budget spanmax s bs −min s bs
π,Π b memory policy; binary-retention class
Cs m capability on environmentmat stages
Γ,H m capability–budget loop; hysteresis area
Dm residual deficit after the budget returns ¯M,Rentries evicted in the squeeze; re-observed subset
ue,p e terminal marginal utility; re-observation bound
budget remains invisible. To our knowledge, no prior sys-
tem schedules fidelity movement in both directions under a
byte budget, and no prior protocol measures what an elastic
budget does to agent capability.
3 PRELIMINARIES ANDMEMORYHYSTERESIS
ANALYSIS
This section names and formalizes the failure mode: under
an elastic budget, capability lost during a squeeze does not
automatically return when the budget recovers. We model
the memory plane and its elastic budgets (Sec. 3.1), define
and measure memory hysteresis (Sec. 3.2), and show why
deletion-based retention cannot close the loop (Sec. 3.3).
3.1 System Model and Elastic Budgets
We consider a self-evolving LLM agent hosted in the cloud.
Completed episodes append experiential entries, such as
trajectories, distilled skills, and environment facts, to a mem-
ory store. At inference time, the agent retrieves from this
store to condition its policy. The store is a metered resource,
and its provisioned budget changes with cost control, tenant
load, and pricing events. We call this regime anelastic budget,
and we call the storage side of the agent the memory plane.
Letedenote an entry andµ(e)its serialized size in
bytes. For a storeM, writeµ(M) = P e∈M µ(e). The agent
serves an environmentmwith query distributionD m. Time
is divided into stagess= 1, . . . , S. During stages, the agent
holds storeM s, answers queries, and appends new writes
W s. Amemory policyπthen maps(M s, Ws)to the next store
M s+1 under the byte budget of stages+1. Capability is
the expected graded outcomeC s m =E q∼Dm [g(q, Ms)]. The
provider-facing problem is to sustain this capability across
the full budget path:
max
π
1
S
SX
s=1
Eq∼Dm[g(q, Ms)] s.t. µ(M s)≤b sB0 ∀s.
(1)
Deployed policies fall into two classes.Binary reten-
tionΠ b keeps an entry verbatim or drops it, soM s+1 ⊆
M s ∪W s. Recency eviction, expiry, and learned value
governance [11] belong to this class.Irreversible laddersmay
replace an entry by a lossy transform, but transitions run
in only one direction: once demoted, an entry is never
rebuilt [24]. Both classes share the same structural property.
At trough (25%) Budget restored (100%)
0.5
0.6
0.7
0.8
0.9
1
Normalized capability
LRU
Mem0
Irrev. Ladder
CURATOR
CrystalMem
Fig. 1.Memory hysteresis under an elastic budget cycle.Capability
normalized to each method’s pre-squeeze level (seven environments
×five seeds). After the budget returns to 100%, every baseline stays
below its pre-squeeze capability; CrystalMem returns to the full-recovery
line (red dashed).
A squeeze step is a projection, and what it discards re-enters
the store only if the input stream supplies it again.
Definition 1(Elastic budget schedule).An elastic
cycle is the budget pathb= (b 1, . . . , bS) =
(1,0.75,0.5,0.25,0.5,0.75,1)withS= 7: asqueeze
phases∈ {1, . . . ,4}and arecoveryphases∈ {4, . . . ,7}, with
span∆ b = 0.75. All policies run under the same path and the
same byte accounting (iso-budget).
3.2 The Memory Hysteresis Phenomenon
Elastic budgets turn memory management into a round trip:
the store is squeezed to a quarter of its provision and then
restored. If the squeeze were reversible, capability would
retrace the same path during recovery. We borrowhysteresis
from magnetism for the failure of this retracing: the state
of the system depends on the path of the control variable,
not only on its current value. The cycle traces a closed
pathΓ ={(b s, Cs m)}S s=1 in the capability–budget plane,
and the enclosed area measures how much recovery lags
the squeeze.
Definition 2(Hysteresis area and residual deficit).For a
policyπon environmentmunder Definition 1, thehysteresis
areais the normalized loop integral
Hm(π) = 1 C 1m ∆b

 I Γ Cdb

 ,(2)
estimated from the staged measurements by the trapezoid sum
ˆHm = 1 C 1m ∆b

 S−1X s=1 1 2  C s+1 m +C s m   bs+1 −b s

 ,(3)
and theresidual deficitisD m(π) =C 1 m −C S m, the capability
still missing once the budget is fully restored.
Hm = 0exactly when the cycle retraces itself. Both
quantities are normalized by the pre-squeeze capabilityC 1 m,
making them comparable across environments.
We measure one representative from each policy fam-
ily under Definition 1: recency eviction (LRU), single-tier
summarization (Mem0 [9]), a four-level irreversible lad-
der [24], binary value governance (CURATOR [11]), and

PREPRINT 4
(a) hysteresis area
0
0.05
0.1
0.15
0.2
LRU
Mem0
Irrev. Ladder
CURATOR
CrystalMem
(b) residual deficit (pp)
0
5
10
15
20
Fig. 2.Two currencies of hysteresis damage: (a) normalized
hysteresis-loop area and (b) residual capability deficit after budget
restoration (mean±std across seven environments).
CrystalMem. The testbed covers seven environments: re-
trieval (SF, TTL [36]), long-context dialogue (LoCoMo [65],
LongMemEval [66]), agentic control (ALFWorld [67], We-
bArena [68]), and synthetic drift (SynDrift), with a Qwen2.5-
7B host [69], a bge-m3 retriever [70], and five seeds. Two
regularities emerge.
Observation1 (Ordered degradation at the trough).At the
squeeze trough (b 4 = 0.25), median capability retention
orders by policy family:0.585(LRU)<0.703(Mem0)
<0.755(irreversible ladder)<0.790(CURATOR)<0.841
(CrystalMem); see Fig. 1, left group.
Observation2 (Restoration does not restore).After the bud-
get returns to100%, the four baselines plateau at0.71–0.89
of their pre-squeeze capability and trace open loops with
ˆHm between0.086and0.207; CrystalMem returns to0.984
with ˆHm = 0.010. See Fig. 1, right group, and Fig. 2.
The mechanism is simple. Evicted entries are gone,
recovery-phase writes replace only what the stream supplies
again, and retrieval degrades around the missing entries.
The next subsection shows that, for deletion-based reten-
tion, this behavior follows from a bound rather than an
implementation choice.
3.3 Why Existing Memory Policies Cannot Close the
Loop
Two assumptions isolate what the argument needs.
Assumption 1(Bounded re-observation).Let ¯Mbe the set
of entries evicted during the squeeze phase. Eache∈ ¯Mis
supplied again by the input stream during the recovery phase
with probability at mostp e <1.
Episodic streams rarely repeat: conversations move on,
tasks change, and drifting environments retire facts. Thusp e
is small in practice.
Assumption 2(Additive terminal utility).There existu e ≥0
such that removing anyA⊆Mfrom a storeMat the terminal
stage lowers capability by at least P e∈A ue; redundancy is
absorbed into the definition ofu e.
Proposition 3(Deficit lower bound for binary retention).
Fix the schedule of Definition 1 and anyπ∈Π b. Let ˜Cdenote
the terminal capability of the same run withb s ≡1. Under
Assumptions 1–2,
E
h
˜C−C S m
i
≥
X
e∈ ¯M
ue (1−p e).(4)
Proof.Fix the stream and condition on the squeeze. Let
R⊆ ¯Mbe the evicted entries supplied again during the
recovery phase; Assumption 1 givesP(e∈R)≤p e. Because
πis binary, an eviction leaves no residue. The terminal store
is thereforeM S =  M 1 \ ¯M  ∪R∪W, whereWcollects
recovery-phase writes, while the un-squeezed counterfac-
tual holds ˜M=M 1 ∪W. Hence ˜M\M S ⊇ ¯M\R, and
Assumption 2 applied toA= ¯M\Ryields ˜C−C S m ≥P
e∈ ¯M\R ue. Taking expectation over re-observation gives
E
h
˜C−C S m
i
≥ P e∈ ¯M ue P(e /∈R)≥P e∈ ¯M ue (1−p e).
The bound is not vacuous: the trough expels at least
1−b 4 = 75%of resident bytes, so the sum in (4) covers most
of what the agent has learned. We report deficits against
the pre-squeeze anchorC 1 m. Value governance operates
within the bound, not beyond it. Choosing which entries
to evict reduces the sum but cannot make it vanish, and the
strongest binary baseline still forfeits6.6±1.4pp, compared
with17.5±4.6pp for recency eviction (Fig. 2(b)).
Lossy tiers relax the binary premise only partially. A sin-
gle tier fixes one exchange rate between bytes and fidelity;
a4×squeeze exceeds that rate, so the tier deletes what
it cannot hold and inherits the bound (12.4±2.9pp for
Mem0). A one-way ladder keeps residues at several rates
but never promotes them, so it serves degraded represen-
tations even after the budget returns (10.1±2.2pp). The
measurements separate the two levers: four tiers instead of
one buy2.3pp, while the reversible stack of CrystalMem
buys another9.0pp (1.1±0.4pp). The proof uses only the
absence of a residue from which an entry can be rebuilt.
Store such a residue, and promotion by compute rather than
re-observation becomes possible. Reversibility is the first-
order lever; tier count is second-order.
The analysis determines the design. The store must hold
entries at several fidelities and move them in both direc-
tions, using a reversible ladder rather than one-way demo-
tion. Because the sum in (4) is weighted byu e, demotion
must track marginal utility, and entries that anchor others
must sink last. Because re-synthesis spends tokens and
can hallucinate, promotion must be budgeted and verified
before it re-enters the store. CrystalMem is built around
exactly these requirements.
4 CRYSTALMEMDESIGN
4.1 Overview
The analysis gives three design requirements: a reversible
ladder, utility-aware demotion, and verified promotion.
CrystalMem implements them with a single control loop
around the store (Fig. 3), executed once per stage in three
phases.Monitormaintains per-entry value estimates.Crys-
tallizereassigns fidelity states to satisfy the incoming byte

PREPRINT 5
(a) The elastic stage loop
(b) Fidelity ladder and energy schedule (c) Verification gate
CrystalMem
Influence
& coupling
Energy
schedule
Verify &
promote
Budget path: Each stage arrives with its own byte budget: it may tighten, tighten again,
then relax. The store must survive the squeeze and recover what it gave up.
Phase I:Monitor Phase II: Crystallize Phase III: Recrystallize
snapshot (b, C)
crystallization
front
Regenerate from residue,
then verify before promotion
Water-filling descent
FULL
COMPRESSED
SKELETAL
TRACE
crystallization front
descends
cheapest to demote
to verification gate
from COMPRESSED
from SKELETAL
from TRACE
Generate × Verify
one unmet
to FULL
two unmet
COMPRESSED
three unmet
to SKELETAL
Fig. 3.CrystalMem framework.(a) Each stage runs one control loop:Monitorscores entries by advantage-weighted influence with dependency
coupling,Crystallizefits the store to the incoming byte budget, andRecrystallizebuys capability back when the budget relaxes. (b) A crystallization
front descends the four-state fidelity ladder by water-filling on energy, demoting the cheapest entries first. (c) Recrystallization regenerates promoted
entries from their residues and admits a draft only after verification confirms the invariants stored at demotion time.
budget.Recrystallizebuys back capability when the budget
expands. The stage transition factorizes as
p

M s+1 |M s, bs+1 =
" Y
e∈M s
φ

f s+1 e |f s e , ηe 
#
×
" Y
e∈U s
R(e′ |z e, Ms)V(v e |e ′, he)
#
,
(5)
where the first factor crystallizes: an assignment kernel
φmoves each entry along the fidelity ladderf e under a
crystallization energyη e. The second factor recrystallizes: a
generation operatorRrebuilds promoted entries from their
residuesz e, and a verification operatorVchecks the result
against stored invariantsh e. Deletion does not appear in
(5). It remains only as last-resort eviction of bottom-rung
residues.
4.2 Fidelity Ladder and Crystallization Energy
Observation 2 traced open loops to one-way demotion. The
ladder replaces deletion with reversible state assignment.
Every entry occupies one ofK= 4states,f 1 (FULL)
throughf 4 (TRACE), withCOMPRESSEDandSKELETALbe-
tween. At statek, an entry costsµ k(e)bytes and delivers
a fractionr k of its utility, withµ 1(e)>· · ·> µ4(e)and
1 =r 1 >· · ·> r4; regenerating from statekcostsc k tokens,
increasing ink. FromCOMPRESSEDdown, each entry keeps
a residuez e, namely its state-krepresentation, and a set of
invariantsh e: key spans, entity tuples, and outcome facts
distilled at demotion time. These invariants later anchor
verification.
A demotion decision trades utility now against compute
later. We price both terms in one score,
ηe(k) = ˜v e (1−r k) +τ c k,(6)
the utility forgone by holdingeat statekplus the antici-
pated cost of buying it back, withτconverting regeneration
tokens into capability cost. Given the incoming budget,
Crystallize solves the constrained assignment
φ⋆ = arg min
φ
X
e∈M s
ηe(φ(e))
s.t.
X
e∈M s
µφ(e)(e)≤b s+1B0. (7)
The objective is separable, so the Lagrangian P e ηe(φ(e)) +
θ( P e µφ(e)(e)−b s+1B0)is minimized rung by rung: an
entry stays at the deepest state whose marginal price
∆ηe/∆µe remains below the multiplierθset by the budget.
CrystalMem implements this step as a water-filling descent,
demoting one rung at a time in increasing order of marginal
price until the store fits. We call the moving boundary the
crystallization front (Fig. 3(b)).
4.3 Influence-Driven Assignment
The bound (4) charges a policy for every unit of deleted util-
ity, so demotion order must tracku e. CrystalMem estimates
this value online.
Each retrieval attributes the query outcome back to the
entries it surfaced, baselined against recent outcomes:
Ie ←γ I e + (1−γ)w e
g(q, M)−mean j∈Q gj
stdj∈Q gj
,(8)
wherew e is the normalized retrieval weight ofein answer-
ingq,Qis a sliding batch of recent queries, andγis the

PREPRINT 6
averaging horizon. Entries that repeatedly appear in above-
average outcomes accumulate influence; stale or decorative
entries decay toward zero. The estimator is white-box: it
uses only retrieval logs and graded outcomes, both already
produced by the serving path.
Entries are not independent: a skill cites facts, and a
trajectory can ground a distilled rule. CrystalMem maintains
a dependency graph over co-retrieval and reference edges
and lets influence flow across it,
˜ve =I e +λ
X
e′∈N(e)
x(e, e′)P
j∈N(e) x(e, j)Ie′,(9)
whereN(e)is the neighborhood ofe,x(e, e ′)counts co-
retrievals, andλsets the coupling strength. Hub entries take
value from the entries they anchor and therefore sink last,
matching the demotion order required by the analysis. As a
hard guard, an entry is not demoted belowSKELETALwhile
aFULLneighbor still cites its invariants.
4.4 Recrystallization
Proposition 3 depends on evictions leaving no residue.
Recrystallization removes that condition.
When the budget expands, Recrystallize selects a promo-
tion set
U s = arg max
U⊆M s
X
e∈U
˜ve ∆e
s.t.
X
e∈U
ce ≤ρ ns, µ(Ms) + X
e∈U
∆µe ≤b s+1B0, (10)
where∆ e is the utility regained by liftingeone rung,c e is its
regeneration cost,n s is the serving-token count of the stage,
andρis the compute cap (default10%). The two constraints
make the trade-off explicit: promotion may spend at most a
fixed share of serving compute and may never exceed the
byte budget. Greedy selection by density˜ve∆e/ce gives the
standard knapsack approximation for (10) and runs in idle
windows between queries.
A selected residue is rebuilt by conditioning the host
model onz e and its graph neighborhood,e ′ ∼ R(· |ze, Ms).
The draft is admitted only if the verification operator
confirms it against the stored invariants,V(e ′, he) = 1
(Fig. 3(c)): every key span, entity tuple, and outcome fact
recorded at demotion time must be entailed bye ′. A re-
jected draft leaves the entry at its current rung, so a failed
promotion cannot degrade the store. Hallucinated recon-
structions are filtered before they enter retrieval. Admission
therefore converts serving tokens into recovered capability,
the storage-for-compute exchange the ladder was built to
support.
Three properties locate the guarantees of the loop; only
the last one is idealized.
Proposition 4(Feasibility invariance).Under Algorithm 1,
µ(M s)≤b sB0 at every stages.
Proof.The Crystallize loop demotes, and at the bottom
rung evicts, until the constraint holds. Each step strictly
decreasesµ(M), so the loop terminates with a feasible store.
Promotions are admitted only within the byte headroom in
(10).
Proposition 5(Near-optimality of the water-filling sched-
ule).Suppose each entry’s marginal price∆η e/∆µe is nonde-
creasing along the ladder. Then the Phase II schedule is optimal
for the fractional relaxation of(7), and its energy exceeds the
integral optimum by at mostmax e [ηe(K)−η e(1)], the span of
one entry.
Proof.Under nondecreasing prices, taking rung moves
greedily by price matches the fractional optimum up to
the single boundary move where the byte constraint be-
comes tight, by the classical fractional-knapsack argument.
Rounding that move integrally charges at most one entry’s
span, and the fractional optimum lower-bounds the integral
one.
The promotion pass in (10) admits the same argument
per binding cap, losing at most one boundary entry for each
cap.
Proposition 6(Loop closure under exact regeneration).Sup-
pose no bottom-rung eviction occurs,Rrestores each promoted
residue to its full utility, andVhas no false rejections. If the
caps in(10)admit all candidates during the recovery phase, then
E[Dm]→0and the loop of Definition 2 closes.
Proof.Every squeezed entry retains its residue. Under the
stated hypotheses, each entry is lifted back tof 1 as the bud-
get returns, so the terminal store matches the counterfactual
store of Proposition 3 on the evicted mass. The deficit term
vanishes, the recovery branch retraces the squeeze branch,
and the enclosed area of Definition 2 is zero.
Both greedy passes sort once and sweep once,
O(|M|log|M|)per stage, with no training and no external
solver. The loop is cheap enough to run inside the serving
path.
4.5 System Implementation
CrystalMem runs as a sidecar beside the serving stack [23].
Monitor hooks the retrieval path and updates (8) inline;
Crystallize fires on budget events; and Recrystallize batches
its generation calls into idle windows, so foreground queries
do not wait on promotion. The store keeps, for each entry,
the current rung, the residuez e, the invariantsh e, and the
graph edges of (9). Under multi-tenancy, the same schedule
runs over the pooled budget with tenant-weighted values
and per-tenant capability floors. On edge hosts, a small
model runs Monitor and Crystallize locally and delegates
Rto the hub.
Taken together, CrystalMem turns retention into re-
versible state assignment. Advantage-weighted influence
and a dependency kernel value each entry; a crystallization-
energy schedule demotes entries along a four-state ladder
to satisfy the budget path; and a generation–verification
operator pair buys capability back under explicit compute
and byte caps, admitting only reconstructions that pass
invariant checks. Deletion becomes the last resort instead
of the default.

PREPRINT 7
Algorithm 1CrystalMem Elastic-Stage Lifecycle ( Monitor ,
Crystallize , and Recrystallize )
Input:storeM s, incoming budgetb s+1, serving tokensn s,
compute capρ, ratesγ, λ, τ
1:Phase I: Monitor▷budget and query telemetry
2:on a budget eventb s+1 ̸=b s, snapshot the loop
point(b s, Cs m)
3:on each retrieval, update the influenceI e by (8)
4:refresh the coupled values˜v e by (9)
5:Phase II: Crystallize▷solve(7)
6:whileµ(M)> b s+1B0 do
7:pop the cheapest movee=
arg mine ∆ηe/∆µe; raise the multiplierθ
to that price
8:demoteeone rung, distilling(z e, he)at its first
demotion; if alreadyTRACE, evicte
9:end while
10:Phase III: Recrystallize▷verified promotion
11:select the promotion setUby (10)
12:for alle∈Udo
13:drawe ′ ∼ R(· |ze, M); admit one rung up iff
V(e ′, he) = 1
14:chargec e to the recrystallization ledger; stop
onceρ ns is spent
15:end for
16:returnM s+1
5 EXPERIMENTS
5.1 Experimental Setup
1) Environments and Protocol:We evaluate on seven environ-
ments in four workload families: retrieval under streaming
writes (the SF and TTL tracks of [36]), long-context dialogue
(LoCoMo [65] and LongMemEval [66], abbreviated LME),
agentic control (ALFWorld [67] and WebArena [68]), and
SynDrift, a synthetic protocol that retires facts mid-stream
(Drift). Every policy runs the elastic cycle of Definition 1
under the same byte accounting. Capability is measured at
each of the seven stages. Unless a table states otherwise,
reported numbers aggregate five seeds; the cost frontier, the
three largest backbone scales, the multi-tenant study, and
the deployment study use three.
2) Comparison Methods:We compare CrystalMem with
fifteen baselines, grouped as in Table 2.(i)Reference bounds:
keep-all, which ingests the same streams without a bud-
get and bounds capability from above; LRU; expiry; and
random drop.(ii)Single-tier summarization: Mem0 [9],
MemGPT [8], and MaRS [31].(iii)Hierarchical and ladder
policies: A-MEM [29], MemoryOS [10], the Human-Inspired
irreversible ladder [24], and R 3Mem [25], which stores
reversible residues but promotes them without a sched-
ule.(iv)Value governance: CURATOR [11], A-MAC [33],
RecMem [32], and AgeMem [12] with its learned admis-
sion policy frozen. Each baseline enforces the stage budget
through its native retention knob. CrystalMem runs in two
configurations throughout: full, with dependency coupling
on, and lite, with coupling off.
3) Evaluation Metrics:We report the three loop metrics of
Definition 2: restored capabilityC S m, hysteresis area ˆHm es-
timated by (3), and residual deficitD m. Capability is scored
on a0–100scale, so deficits read directly in points (pp).
Two meters cover serving cost: the recrystallization ratio,
defined as promotion tokens divided by stream inference
tokens, and the scheduler share of stage wall-clock time.
4) Implementation Details:All policies serve from
vLLM [23] on A100 and H100 GPUs, with a Qwen2.5-
7B-Instruct host [69] at temperature0and a bge-m3 re-
triever [70]. Five additional backbone scales are evaluated
in Sec. 5.4.
5.2 Iso-Budget Main Comparison
Table 2 gives the iso-budget comparison. CrystalMem has
the highest restored capability on all seven environments,
averaging57.4against52.8for R 3Mem, the strongest base-
line in this comparison. The margin averages+4.6pp and
never falls below+3.4pp (WebArena). The loop metrics
separate the methods more sharply than raw capability:
mean hysteresis area falls to0.013against a baseline range
of0.044–0.216, and mean residual deficit falls to0.5pp.
The remaining headroom is small, since keep-all, which
never discards entries, ends only1.3pp higher. The lite row
isolates dependency coupling:0.6pp on average, concen-
trated on ALFWorld (1.1pp) and WebArena (0.8pp), which
Sec. 5.4 revisits.
Figure 4 shows the cycles behind these aggregates. Every
method follows the squeeze downward. During recovery,
the baselines flatten, while CrystalMem rejoins the keep-all
trace, closes the budget–capability loop, and recovers most
of its trough loss one stage after the budget turns.
The deficit column shows the cost of each missing
lever. R 3Mem keeps residues at several fidelities but pro-
motes them without an energy schedule or a verification
gate; reversibility without scheduling forfeits4.7pp. The
strongest binary policy, CURATOR, chooses evictions by
learned value but leaves no residue to rebuild from. The
floor of Proposition 3 then applies, and selection without re-
versibility forfeits6.1pp. The Human-Inspired ladder keeps
several fidelities but moves entries only downward. At
10.1pp, it trails even binary governance, because demoted
entries continue serving degraded representations after the
budget returns. Closing the loop needs both levers: residues
to rebuild from and a schedule that decides when to spend
them.
Two meters bound the serving cost of these gains.
Recrystallization uses7.3%of stream inference tokens on
average and9.1%at worst, within the token cap of (10). The
scheduler adds3.4%of stage wall-clock time on average
and3.8%at most. Across the4,165-measurement grid, no
method exceeds its stage budget, and CrystalMem main-
tains the feasibility invariant of Proposition 4 at every stage.
Table 3 restates the frontier in budget terms. The me-
dianb ⋆ across environments is50%, with six environments
matched at half provision and TTL at40%. Even a40%
budget leaves at most a0.7pp shortfall, and the curve is
flat above the match point: capability at a60%budget stays
within0.3pp of full provision on every environment. Over
the eight-budget grid, CrystalMem is never below LRU,
Mem0, or CURATOR at any operating point, so the ranking
does not depend on where a provider sits on the frontier.

PREPRINT 8
TABLE 2
Iso-budget comparison over one elastic cycle (Definition 1): restored capabilityC S m (mean±std, five seeds), its seven-environment average, mean
hysteresis area ¯H(3), and mean residual deficit ¯D(pp). The best value in each baseline family is underlined ; the gain of CrystalMem over each
row appears in the ∆column .Gray italicis the unconstrained keep-all bound, not ranked.
Retrieval Dialogue Agentic Synthetic
Method SF TTL LoCoMo LME ALF Web Drift Avg↑ ¯H↓ ¯D↓ ∆
Keep-all 66.8±0.5 59.1±0.6 58.3±0.2 55.5±0.7 68.9±0.8 30.3±0.7 72.5±0.8 58.8— — −1.3
LRU 45.9±0.5 41.9±0.7 43.0±0.6 39.0±0.4 48.0±0.4 19.0±0.3 46.6±0.5 40.5 0.209 17.6 ↑16.9
Expiry 49.3±0.7 44.8±0.1 43.3±0.7 40.8±0.2 51.5±0.8 19.8±0.8 51.2±0.4 43.0 0.178 15.1 ↑14.5
Random drop 46.2±0.5 41.7±0.6 40.4±0.4 38.4±0.3 48.4±0.7 17.9±0.4 47.4±0.2 40.0 0.216 17.9 ↑17.4
Mem0 [9][arXiv’25] 52.0±0.6 47.5±0.6 46.0±0.3 43.0±0.3 53.7±0.3 22.0±0.7 55.2±0.6 45.6 0.145 12.3 ↑11.8
MemGPT [8][COLM’24] 52.8±0.5 47.1±0.7 46.4±1.1 43.7±1.1 54.8±0.9 22.0±0.8 55.4±0.6 46.0 0.144 12.1 ↑11.4
MaRS [31][arXiv’25] 51.4±0.7 46.5±0.6 45.0±0.5 42.2±1.0 53.3±0.3 21.1±0.3 53.6±0.6 44.7 0.157 13.3 ↑12.7
A-MEM [29][NeurIPS’25] 54.7±0.3 48.5±0.2 47.7±0.6 44.8±0.4 56.7±0.4 22.9±0.8 57.7±0.4 47.6 0.121 10.5 ↑9.9
MemoryOS [10][EMNLP’25] 56.0±0.3 49.7±0.4 48.9±0.2 45.7±0.2 58.0±1.4 23.9±0.3 59.2±0.7 48.8 0.109 9.2 ↑8.7
Human-Inspired [24][arXiv’26] 54.6±0.4 48.7±0.5 48.0±0.8 45.0±0.4 57.1±0.5 22.6±0.5 58.1±0.4 47.7 0.122 10.1 ↑9.7
R3Mem [25][ACL’25] 60.0±0.6 53.5±0.4 53.1±0.6 49.6±0.3 62.5±0.8 26.3±0.8 64.6±0.3 52.8 0.044 5.2 ↑4.6
CURATOR [11][arXiv’26] 58.7±0.4 52.3±0.4 51.1±0.6 48.4±0.3 60.5±0.6 25.4±0.2 62.9±0.6 51.3 0.087 6.6 ↑6.1
A-MAC [33][ICLR-W’26] 58.0±0.3 51.6±0.6 51.2±0.6 47.7±0.4 60.0±0.8 25.1±0.5 62.4±0.5 50.8 0.088 7.2 ↑6.6
RecMem [32][ACL’26] 57.6±0.7 51.3±0.4 50.4±0.5 47.6±0.1 59.5±0.4 24.9±0.8 61.7±0.3 50.4 0.093 7.6 ↑7.0
AgeMem [12][arXiv’26] 56.8±1.0 50.9±0.8 50.2±0.3 46.9±0.4 58.9±0.5 24.3±0.8 60.7±0.3 49.8 0.102 8.2 ↑7.6
CrystalMem-lite 65.0±0.6 56.7±0.4 56.4±0.9 52.7±0.7 67.4±0.6 29.0±0.3 70.9±1.2 56.9 0.013 1.1 ↑0.6
CrystalMem (Ours) 65.1±0.4 57.4±0.7 56.6±0.5 53.2±1.2 68.6±0.5 29.8±0.3 71.3±1.0 57.4 0.013 0.5 –
LRU TTL Mem0 MemoryOS Irrev. Ladder R3Mem CURATOR CrystalMem Keep-all (oracle) Byte budget (%)
1 2 3 4 5 6 7
Stage
35
40
45
50
55
60Capability
0
20
40
60
80
100
(a) LoCoMo
1 2 3 4 5 6 7
Stage
40
50
60
70Capability
0
20
40
60
80
100 (b) ALFWorld
25 50 75 100
Byte budget (%)
35
40
45
50
55
60Capability (c) Loops (LoCoMo)
4 5 6 7
Stage
0
20
40
60
80
100Recovered share (%) (d) Recovered share
Fig. 4. Elasticity dynamics under the squeeze–recover schedule (seed means). (a), (b) Capability trajectories on LoCoMo and ALFWorld, with the
byte budget overlaid as gray stairs (right axis). (c) Budget–capability loops on LoCoMo: arrows give traversal direction, and shaded regions mark
the areas enclosed by LRU and by CrystalMem. (d) Share of trough loss recovered at each recovery stage, averaged over all seven environments;
the red dashed line marks full recovery.
The provisioning rule is simple: run the memory plane at
half its nominal budget and lose nothing relative to the
best fixed-provision baseline. Figure 5 draws the frontier:
CrystalMem meets the keep-all reference at half budget,
and the per-environment curves keep it above the strongest
binary baseline at every operating point.
5.3 Mechanism and Theoretical Validation
Figure 6 traces the machinery of Algorithm 1 on live cycles.
Panel (a) tracks the store’s fidelity composition. At the start,
85%of entries occupy the upper two states,FULLand
COMPRESSED. The squeeze pushes all but29%down to
SKELETALandTRACE; verified promotion raises the upper
share back to68%by the final stage. The store moves in both
directions through fidelity space.
Panel (b) checks the influence estimator (8) against leave-
one-out ground truth on200entries in each of three environ-
ments. Spearman correlation reaches0.75–0.76, and75–80%
of the true top-decile entries land in the estimated top decile.
The advantage-weighted signal is accurate enough to order
demotions.
Panel (c) splits recrystallization by origin state. The gate
rejects6.9%of reconstructions fromCOMPRESSED,16.4%
fromSKELETAL, and27.5%fromTRACE. Rejection rises
with demotion depth, as sparser residues leave more room
for invariant violations. Admitted reconstructions recover
about90%of retrieval utility regardless of origin, and
their downstream contribution remains positive (+0.9to
+1.0pp). Sec. 5.4 shows the cost of removing the gate.
Panel (d) tests Proposition 3 where it applies. Across the
seven binary policies, measured deficits track the estimated
bound with correlation0.76and exceed it on two thirds of
the245environment–seed points. CrystalMem breaks the
premise rather than the bound: it keeps residues, and its
deficit (0.5pp, Table 2) sits an order of magnitude below ev-
ery binary floor. Together with the zero budget violations of

PREPRINT 9
TABLE 3
Iso-capability budget (three seeds). Ref is CURATOR, the strongest
budgeted baseline at full provision;b ⋆ is the smallest budget at which
CrystalMem matches it. Cells at or above Ref inbold; the medianb ⋆ in
red.
CrystalMem at budget
Env. Ref@100 40% 50% 60% b⋆
SF 66.3 66.267.0 67.1 50%
TTL 58.6 58.6 59.3 59.5 40%
LoCoMo 58.0 57.558.4 58.3 50%
LME 55.3 54.955.4 55.6 50%
ALF 68.5 68.168.7 69.1 50%
Web 29.9 29.330.6 30.7 50%
Drift 72.1 72.072.5 72.8 50%
Median across environments 50%
10 20 30 40 50 60 80 100
Byte budget (%)
35
40
45
50
55
60Capability LRU
Mem0
MemoryOS
CURATOR
CrystalMem
Keep-all at 100%
(a) Frontier
10 20 30 40 50 60 80 100
Byte budget (%)
20
40
60
80Capability
CrystalMem
CURATOR (b) Per environment
Fig. 5. Cost frontier under constant provisioning (seed means).
(a) Seven-environment mean capability against the byte budget; the
dashed line is keep-all at full provision; shaded bands give seed vari-
ation. (b) Per-environment curves (thin) and their means (thick) for
CrystalMem and the strongest binary baseline.
Sec. 5.2 and the closed loops of Table 2, these measurements
ground Propositions 4 and 6 in the observed cycles.
5.4 Ablations and Sensitivity
Table 4 removes one design choice at a time; every variant
loses capability, so no component is redundant. The full
row re-runs the Table 2 configuration, and its average lands
within0.1pp. Replacing the water-filling schedule (7) with
size-greedy demotion costs1.8pp, and random demotion
costs3.0pp: which bytes are reclaimed matters as much as
how many. The demotion ordering relies on the influence
signal (8); recency costs1.3pp, and random scoring costs
3.7pp. Removing the verification gate costs2.8pp even
though every reconstruction is admitted, because unverified
regenerations pollute retrieval. This is the failure mode
rejected by the gate in Fig. 6(c). Dependency coupling is
the smallest term,0.4pp on the seven-environment average,
concentrated on the two agentic environments, matching the
lite gap in Table 2.
The recrystallization cap prices loop closure directly. At
ρ= 0, the deficit regresses to6.5pp, within noise of the
strongest binary floor (6.6pp, Table 2); a reversible ladder
without promotion compute is a slower way to forget. At
ρ= 5%, the deficit falls to2.1pp, and raisingρfrom the
default10%to20%buys only0.3pp. Ladder depth shows
the same knee: two states forfeit3.0pp, three forfeit0.8pp,
and six change nothing (0.1pp), so the four-state ladder sits
TABLE 4
Ablation over one elastic cycle (seven environments, five seeds):
seven-environment averages, with∆the drop in Avg relative to full
CrystalMem (default: water-filling schedule, advantage-weighted
influence,ρ= 10%,K=4states).
Variant Avg↑ ¯H↓ ¯D↓ ∆
CrystalMem (full) 57.3±0.3 0.015 0.7 –
Schedule→size-greedy 55.6±0.2 0.015 2.2 ↑1.8
Schedule→random 54.3±0.2 0.033 3.7 ↑3.0
Influence→recency 56.0±0.2 0.012 1.9 ↑1.3
Influence→random 53.7±0.2 0.035 4.3 ↑3.7
w/o dependency coupling 56.9±0.2 0.011 1.0 ↑0.4
w/o verification gate 54.6±0.2 0.025 3.3 ↑2.8
Recryst. cap0% 51.4±0.2 0.071 6.5 ↑5.9
Recryst. cap5% 55.9±0.2 0.010 2.1 ↑1.4
Recryst. cap20% 57.1±0.1 0.013 0.9 ↑0.3
LadderK=2 54.3±0.2 0.024 3.5 ↑3.0
LadderK=3 56.6±0.3 0.011 1.5 ↑0.8
LadderK=6 57.2±0.1 0.015 0.7 ↑0.1
TABLE 5
Backbone sweep (averages over SF , ALFWorld, and SynDrift; five
seeds up to 14B, three above): restored capability and hysteresis area
per model scale.∆is the CrystalMem gain over CURATOR at the
same backbone.
LRU CURATOR CrystalMem
Backbone Avg ¯H Avg ¯H Avg ¯H ∆
Qwen2.5-3B 39.0 0.240 52.6 0.093 60.3 0.012 ↑7.6
Qwen2.5-7B 46.9 0.213 60.7 0.080 68.4 0.014 ↑7.7
Qwen2.5-14B 50.0 0.203 63.8 0.079 71.3 0.013 ↑7.5
Qwen2.5-32B 51.7 0.196 65.9 0.076 73.2 0.010 ↑7.3
Qwen2.5-72B 53.8 0.195 67.7 0.075 75.6 0.011 ↑7.9
Llama-3.3-70B 52.9 0.197 66.8 0.076 74.1 0.012 ↑7.3
at the point of vanishing marginal return. Figure 7 plots both
sweeps per environment. The knee at the deployed cap and
the plateau past four states appear in every environment,
not only in the mean.
Table 5 repeats the cycle on six backbones spanning
Qwen2.5 [69] from 3B to 72B and Llama-3.3-70B [71], on
the SF, ALFWorld, and SynDrift subset. Hysteresis is not
a 7B artifact: LRU’s area stays between0.195and0.240at
every scale. Scale also does not close the loop by itself. The
strongest binary baseline still forfeits7.5–7.9pp on every
backbone. CrystalMem holds its area at or below0.014and
its deficit at or below0.5pp on all six scales, with a steady
+7.3to+7.9pp margin over it. The 3B row supports the
deployment premise of Sec. 5.6: the margin survives at edge
scale.
The design does not depend on the seven environments
used for tuning. With every hyper-parameter frozen, one
cycle on BabyAI [72], an agentic stream outside that set,
leaves CrystalMem with a1.5pp residual deficit and a0.011
loop area, against5.5pp and0.069for the strongest binary
baseline and17.2pp and0.199for recency eviction. The
family ordering is unchanged.

PREPRINT 10
1 2 3 4 5 6 7
Stage
0
0.25
0.5
0.75
1
Store fraction
Full
Compressed
Skeletal
Trace
(a) Fidelity composition
-2 0 2 4 6
Influence estimate
-2
0
2
4
6
Leave-one-out delta (pp)
SF
LoCoMo
ALFWorld (b) Influence estimator
SF TTL
LoCoMo
LME ALF Web Syn
0
0.1
0.2
0.3
0.4Rejection rate
Compressed
Skeletal
Trace (c) Verification gate
0 10 20 30
Predicted lower bound (pp)
0
10
20
30Measured deficit (pp)
LRU
Expiry
Random
CURATOR
A-MAC
AgeMem
RecMem (d) Deficit bound
Fig. 6. Mechanism validation on live cycles (seed means). (a) Fidelity composition of the store per stage. (b) Influence estimate against leave-one-
out ground truth, with a linear fit. (c) Verification rejection rate by origin state and environment. (d) Measured deficit against the estimated bound of
Proposition 3 for the seven binary policies; points above the gray diagonal satisfy the bound.
0 5 10 20
Compute cap (%)
-2
0
2
4
6
8
Residual deficit (pp)
SF
TTL
LoCoMo
LME
ALF
Web
Syn
Mean
(a) Compute cap
2 3 4 6
Ladder depth
0
1
2
3
4Residual deficit (pp)
SF
TTL
LoCoMo
LME
ALF
Web
Syn
Mean (b) Ladder depth
Fig. 7. Design-parameter sweeps (seed means). Thin curves: single
environments; thick: the seven-environment mean; dotted vertical: the
deployed default.
TABLE 6
Multi-tenant crystallization (three seeds): share of windows that violate
the per-tenant floor, by tenant count.∆is the reduction
CrystalMem-SLO delivers atN=8, computed on unrounded rates; ms
is the allocator decision time atN=4. Pooled Jain fairness is at least
0.999for every policy and tenant count.
SLO violations↓
Policy N=2N=4N=8 ∆ ms
LRU-fair 31% 38% 62% ↑56 3
CURATOR-fair 17% 31% 47% ↑40 4
CrystalMem-fair 8% 14% 26% ↑20 8
CrystalMem-SLO (Ours) 3% 3% 6% – 24
5.5 Fidelity-SLO Multi-Tenant Crystallization
We next share one memory pool amongNtenants with
independent streams drawn from the seven environments,
on a single vLLM instance. The pool is provisioned at
N×40%ofB 0, squeezed to half for sustained windows, and
then released, with six windows per run. A tenant’s service
level objective (SLO) holds in a window if its capability stays
within2pp of its solo capability at the same budget. Table 6
compares fair splitting of each store with the CrystalMem
allocator, which steers the pool toward tenants nearest their
floor.
Crystallization improves sharing before any allocation
intelligence is added. Fair splitting of a crystallized store
violates13.9%of windows atN=4, compared with30.6%
for CURATOR and37.5%for LRU, because a squeezed
tenant keeps residues to recover from. Every policy in this
TABLE 7
Edge deployment on the Jetson testbed (two Orin agents, ALFWorld
and SynDrift, three seeds): residual deficit (pp), recrystallization latency
p50/p95 (ms), per-stage edge–cloud synchronization (MB), foreground
blocking, and per-stage energy (J).
Policy ¯D↓ p50/p95 Sync↓ Block↓ Energy
LRU 9.1 – 16.0 0.2% 491
CURATOR 6.1 – 16.9 0.2% 463
CrystalMem (Ours) 2.0 586 / 2007 3.4 2.9% 479
experiment is byte-fair (Jain≥0.999); the violations come
from what the bytes can rebuild, not from how they are
split. The SLO-aware allocator drops violations to2.8%,
with decisions in24ms on average and42ms maximum,
well under one percent of a window. Density widens the
separation: the gap over CURATOR-fair grows from14to
28to40pp asNgoes2→8, and atN=8recency eviction
violates62%of windows. Sharing at density is survivable
only for stores that can rebuild what the pool takes away.
5.6 Real-System Deployment
The physical testbed has a Jetson AGX Thor 128 GB
hub serving Qwen2.5-7B through vLLM and two AGX
Orin 64 GB agents whose memory planes run on-device
Qwen2.5-3B, connected over real 802.11ac (Fig. 8). Each
Orin also drives a HighTorque Panthera-HT arm, whose
low-level motion runs on a shared CAN controller. The
elastic budget is the edge storage quota, cycled through
Definition 1 on ALFWorld and SynDrift with three seeds;
power is metered at10Hz through INA3221.
The capability results survive on hardware (Table 7).
Figure 9 profiles the cycle: CrystalMem dips deepest at
the trough but rejoins one stage after the turn, with flat
latency and blocking across stages. CrystalMem restores to
within2.0pp, compared with6.1pp for CURATOR and
9.1pp for LRU, preserving the cluster ordering. Its costs
remain serving-compatible: recrystallization runs at586ms
median and2.0s p95 per entry batch on the Orin, blocks
foreground inference2.9%of the time, and crystallized
synchronization moves3.4MB per stage against16–17MB
for full-fidelity shipping, a4.8–5.0×reduction over the real
link. Per-stage energy on the Orin agents is flat across poli-
cies (463–491J), so loop closure adds no energy premium
at the edge. The dedicated recovery comparison sharpens

PREPRINT 11
Panthera-HT (Arm 1) Panthera-HT (Arm 2)
AGX Orin 1 AGX Orin 2AGX Thor(hub)
Robotic Arm
Controller
Panthera-HT Arm 1
 Panthera-HT Arm 2
Robotic Arm
Controller
CAN CAN
Jetson AGX Orin 1 Jetson AGX Orin 2Jetson AGX Thor
802.11ac 802.11ac
high-level action / state
Fig. 8. Physical testbed: topology (top) and deployed hardware (bottom).
the energy account: recovering one point of capability by
recrystallization costs141J, compared with684J by re-
experiencing the underlying episodes, a0.21×ratio. A four-
process tenant mini-deployment across the three Jetsons ran
the same cycles concurrently with no out-of-memory events,
per-process capability within0.6pp of solo runs, and hub
p95 latency at1.5×solo.
As a closing case study, a HighTorque arm driven by an
Orin-hosted skill memory runs one squeeze–recover cycle:
the edge quota falls to25%and returns. Under CrystalMem,
the arm’s skill fragments demote to residues and recrystal-
lize on recovery; post-recovery task success is89%of the
pre-squeeze level. Under binary eviction, the demoted skills
are gone, and success plateaus at61%.
6 CONCLUSION
In cloud-served self-evolving large language model agents,
we identifiedmemory hysteresis: after an experience-store
budget is squeezed and restored, capability settles below
the pre-squeeze level. Deletion and one-way compression
cause the gap because they discard the material needed
for later rebuilding; we also prove a residual-deficit floor
for any keep/drop-only policy. CrystalMem closes the loop
by replacing binary memory management with crystallized
memory: entries move across four fidelity states under
a crystallization-energy schedule, demotions are ordered
by advantage-weighted influence with dependency cou-
pling, and verified recrystallization recovers capability un-
der explicit compute and byte caps. Across seven environ-
ments, seventeen methods, and six backbones, CrystalMem
achieves the highest restored capability everywhere, leaves
a residual deficit an order of magnitude below every bi-
nary baseline, and, from half the byte budget, matches the
strongest budgeted baseline at full provision. The advan-
tage carries into deployment: at the four-tenant operating
point, crystallized stores yield an order of magnitude fewer
service-level violations than fair splitting of binary stores,
and on a physical edge–cloud testbed, each recovered point
of capability costs about a fifth of the energy required to
re-experience the underlying episodes.
REFERENCES
[1] P . Du, “Memory for Autonomous LLM Agents: Mechanisms, Eval-
uation, and Emerging Frontiers,” arXiv preprint arXiv:2603.07670,
2026.
[2] B. Wu, Z. Ding, and J. Huang, “A Review of Continual Learning
in Edge AI,”IEEE Transactions on Network Science and Engineering,
vol. 13, pp. 6571–6588, 2026.
[3] G. Wang, Y. Xie, Y. Jianget al., “Voyager: An Open-Ended
Embodied Agent with Large Language Models,” arXiv preprint
arXiv:2305.16291, 2023.
[4] S. Ouyang, J. Yan, I.-H. Hsuet al., “ReasoningBank: Scaling Agent
Self-Evolving with Reasoning Memory,” inInternational Conference
on Learning Representations, 2026.
[5] Z. Fang, Y. Guo, Y. Zhanget al., “Shared Spatial Memory Through
Predictive Coding,” arXiv preprint arXiv:2511.04235, 2025.
[6] B. Wu and J. Huang, “Lifecycle-Aware Federated Contin-
ual Learning in Mobile Autonomous Systems,” arXiv preprint
arXiv:2604.20745, 2026.
[7] Z. Ding, J. Huang, Y. Zhao, and Z. Cai, “Combating Knowledge
Diversity and Catastrophic Forgetting in UAV-Assisted Collabo-
rative Vehicular Learning: A Game-Theoretic Approach,”ACM
Transactions on Autonomous and Adaptive Systems, 2026.
[8] C. Packer, S. Wooders, K. Linet al., “MemGPT: Towards LLMs as
Operating Systems,” inProceedings of the Conference on Language
Modeling, 2024.
[9] P . Chhikara, D. Khant, S. Aryanet al., “Mem0: Building
Production-Ready AI Agents with Scalable Long-Term Memory,”
arXiv preprint arXiv:2504.19413, 2025.
[10] J. Kang, M. Ji, Z. Zhao, and T. Bai, “Memory OS of AI Agent,” in
Proceedings of the 2025 Conference on Empirical Methods in Natural
Language Processing, 2025, pp. 25 972–25 981.
[11] B. Wu, Z. Ding, J. Huang, and Y. Zhao, “Forget to Improve:
On-Device LLM-Agent Continual Learning via Budget-Curated
Memory,” arXiv preprint arXiv:2606.25115, 2026.
[12] Y. Yu, L. Yao, Y. Xieet al., “Agentic Memory: Learning Uni-
fied Long-Term and Short-Term Memory Management for LLM
Agents,” arXiv preprint arXiv:2601.01885, 2026.
[13] Z. Ding, B. Wu, and J. Huang, “EASE: Federated Multimodal
Unlearning via Entanglement-Aware Anchor Closure,” arXiv
preprint arXiv:2605.00733, 2026.
[14] Z. Ding and J. Huang, “Toward Trustworthy Federated Unlearn-
ing for Mobile Autonomous Systems,”IEEE Network, 2026.
[15] Z. Ding, B. Wu, and J. Huang, “SCALE: Sensitivity-Aware Fed-
erated Unlearning with Information Freshness Optimization for
Mobile Edge Computing,” inProceedings of the IEEE International
Conference on Distributed Computing Systems, 2026.
[16] C. Du, Z. Yu, H. Xuet al., “Temporal-Aware GPU Resource Alloca-
tion for Distributed LLM Inference via Reinforcement Learning,”
IEEE Transactions on Cloud Computing, 2026.
[17] Q. Zhang, M. Li, Q. Liet al., “MAP: GPU Resource Planning for
Multi-Agent Systems with Stochastic and Verbose Outputs,”IEEE
Transactions on Cloud Computing, 2026.
[18] Z. Fang, S. F. Hu, Z. Changet al., “Inference-Time Budget Control
for LLM Search Agents,” arXiv preprint arXiv:2605.05701, 2026.
[19] Q. Duan, J. Huang, S. Huet al., “Combining Federated Learning
and Edge Computing Toward Ubiquitous Intelligence in 6G Net-
work: Challenges, Recent Advances, and Future Directions,”IEEE
Communications Surveys & Tutorials, vol. 25, no. 4, pp. 2892–2950,
2023.
[20] J. Huang, B. Wu, Q. Duanet al., “A Fast UAV Trajectory Plan-
ning Framework in RIS-Assisted Communication Systems With
Accelerated Learning via Multithreading and Federating,”IEEE
Transactions on Mobile Computing, vol. 24, no. 8, pp. 6870–6885,
2025.
[21] Z. Ding, B. Wu, J. Huang, and S. Mao, “Application-Aware Twin-
in-the-Loop Planning for Federated Split Learning over Wireless
Edge Networks,” arXiv preprint arXiv:2604.26105, 2026.

PREPRINT 12
1 2 3 4 5 6 7
Stage
40
50
60
70CapabilityLRU
CURATOR
CrystalMem
(a) On-device trajectories
1 2 3 4 5 6 7
Stage
0
0.5
1
1.5
2
2.5Latency (s)
0
2
4
6
8
10
12
p50
p95 (b) Recrystallization latency
1 2 3 4 5 6 7
Stage
0
5
10
15
20Sync per stage (MB)
LRU CURATOR CrystalMem (c) Synchronization traffic
Recrystallize Re-experience
0
200
400
600
800Joules per recovered pp
LRU
CURATOR
CrystalMem (d) Recovery energy
Fig. 9. Edge deployment profile (seed means). (a) Capability on the Orin agents: solid ALFWorld, dashed SynDrift. (b) CrystalMem recrystallization
latency per stage (p50 and p95 boxes over devices, environments, and seeds) with the foreground-blocking share on the right axis (dotted). (c) Per-
stage synchronization traffic; the darker segment is uplink. (d) Energy per recovered capability point: recrystallization against re-experience; dots
are environment–seed observations.
[22] B. Wu, J. Huang, Q. Duanet al., “Enhancing Vehicular Platooning
With Wireless Federated Learning: A Resource-Aware Control
Framework,”IEEE Transactions on Networking, vol. 34, pp. 1479–
1494, 2026.
[23] W. Kwon, Z. Li, S. Zhuanget al., “Efficient Memory Management
for Large Language Model Serving with PagedAttention,” in
Proceedings of the ACM Symposium on Operating Systems Principles,
2023, pp. 611–626.
[24] D. Kerestecioglu, A. Robsky, C. Vasterset al., “Human-
Inspired Memory Architecture for LLM Agents,” arXiv preprint
arXiv:2605.08538, 2026.
[25] X. Wang, S. Wang, Y. Zhu, and B. Liu, “R 3Mem: Bridging Memory
Retention and Retrieval via Reversible Compression,” inFindings
of the Association for Computational Linguistics: ACL 2025, 2025, pp.
4541–4557.
[26] B. Wu, J. Huang, and Y. Zhao, “From Alpha to Omega: Lifecycle-
Aware Forgetting Defense in Federated Continual Learning for
Planetary Exploration,” inProceedings of the IEEE International
Conference on Distributed Computing Systems, 2026.
[27] C. V . K. Alla, H. N. Gaddam, and M. Kommi, “BudgetMem: Learn-
ing Selective Memory Policies for Cost-Efficient Long-Context
Processing in Language Models,” arXiv preprint arXiv:2511.04919,
2025.
[28] U. Pudasaini, Z. Ding, and J. Huang, “Securing Smart Agri-
culture with Communication-Efficient Federated Unlearning,” in
Proceedings of the IEEE International Conference on High Performance
Switching and Routing, 2026, pp. 1–8.
[29] W. Xu, Z. Liang, K. Meiet al., “A-MEM: Agentic Memory for LLM
Agents,” inAdvances in Neural Information Processing Systems, 2025.
[30] Z. Zhou, A. Qu, Z. Wuet al., “MEM1: Learning to Synergize
Memory and Reasoning for Efficient Long-Horizon Agents,” in
International Conference on Learning Representations, 2026.
[31] S. Alqithami, “Forgetful but Faithful: A Cognitive Memory Ar-
chitecture and Benchmark for Privacy-Aware Generative Agents,”
arXiv preprint arXiv:2512.12856, 2025.
[32] Z. Dai, S. Deng, S. Guanet al., “RecMem: Recurrence-based Mem-
ory Consolidation for Efficient and Effective Long-Running LLM
Agents,” inFindings of the Association for Computational Linguistics:
ACL 2026, 2026, pp. 32 353–32 376.
[33] G. Zhang, W. Jiang, X. Wanget al., “Adaptive Memory Admission
Control for LLM Agents,” inInternational Conference on Learning
Representations Workshop on Memory for LLM-Based Agentic Systems,
2026.
[34] K. Lin, C. Snell, Y. Wanget al., “Sleep-time Compute: Beyond
Inference Scaling at Test-time,” arXiv preprint arXiv:2504.13171,
2025.
[35] Y. Margalit, N. Cohen-Inger, E. Avramet al., “Governed
Shared Memory for Multi-Agent LLM Systems,” arXiv preprint
arXiv:2606.24535, 2026.
[36] Y. Hu, Y. Wang, and J. McAuley, “Evaluating Memory in LLM
Agents via Incremental Multi-Turn Interactions,” inInternational
Conference on Learning Representations, 2026.
[37] A. Kwon, “Reclaim Evaluation: A Lossy Memory Is Worse Than
an Empty One,” arXiv preprint arXiv:2606.25449, 2026.
[38] B. Wu, J. Huang, and S. Yu, “‘X of Information’ Continuum: A Sur-
vey on AI-Driven Multi-Dimensional Metrics for Next-Generation
Networked Systems,”IEEE Communications Surveys & Tutorials,
vol. 28, pp. 5307–5344, 2026.
[39] B. Wu, Z. Cai, W. Wu, and X. Yin, “AoI-Aware Resource Manage-
ment for Smart Health via Deep Reinforcement Learning,”IEEE
Access, vol. 11, pp. 81 180–81 195, 2023.
[40] B. Wu, J. Huang, and Q. Duan, “Real-Time Intelligent Healthcare
Enabled by Federated Digital Twins With AoI Optimization,”IEEE
Network, vol. 40, no. 2, pp. 184–191, 2026.
[41] Z. Fang, S. Hu, J. Wanget al., “Prioritized Information Bottleneck
Theoretic Framework With Distributed Online Learning for Edge
Video Analytics,”IEEE Transactions on Networking, vol. 33, no. 3,
pp. 1203–1219, 2025.
[42] L. Dong, J. Huang, and R. W. Heath, “Transformer-Based Dynamic
Resource Allocation for Multi-Carrier NOMA Systems,”IEEE
Transactions on Cognitive Communications and Networking, vol. 12,
pp. 4926–4941, 2026.
[43] C.-C. Xing, Z. Ding, and J. Huang, “A Stochastic Geometry-Based
Analysis of SWIPT-Assisted Underlaid Device-to-Device Energy
Harvesting,”ACM SIGAPP Applied Computing Review, vol. 25,
no. 4, pp. 18–34, 2025.
[44] D. Pan, B.-N. Wu, Y.-L. Sun, and Y.-P . Xu, “A Fault-Tolerant
and Energy-Efficient Design of a Network Switch Based on
a Quantum-Based Nano-Communication Technique,”Sustainable
Computing: Informatics and Systems, vol. 37, p. 100827, 2023.
[45] B. Wu, Z. Ding, and J. Huang, “PRISM: Exposing and Resolving
Spurious Isolation in Federated Multimodal Continual Learning,”
arXiv preprint arXiv:2605.01061, 2026.
[46] ——, “RELIEF: Turning Missing Modalities into Training Acceler-
ation for Federated Learning on Heterogeneous IoT Edge,” arXiv
preprint arXiv:2604.04243, 2026.
[47] Y. Zhang, H. Zhang, F. Gaoet al., “Harness VLA: Steering Frozen
VLAs into Reliable Manipulation Primitives via Memory-Guided
Agents,” arXiv preprint arXiv:2607.08448, 2026.
[48] Z. Z. Wang, J. Mao, D. Fried, and G. Neubig, “Agent Workflow
Memory,” arXiv preprint arXiv:2409.07429, 2024.
[49] R. Wu, X. Wang, J. Meiet al., “EvolveR: Self-Evolving LLM Agents
through an Experience-Driven Lifecycle,” inProceedings of the
International Conference on Machine Learning, 2026.
[50] S. Yu, G. Li, W. Shi, and P . Qi, “PolySkill: Learning Generalizable
Skills Through Polymorphic Abstraction,” inInternational Confer-
ence on Learning Representations, 2026.
[51] L. Qiu, Z. Gao, J. Chenet al., “AutoRefine: From Trajectories to
Reusable Expertise for Continual LLM Agent Refinement,” arXiv
preprint arXiv:2601.22758, 2026.
[52] Y. Zhang, J. Shu, Y. Maet al., “Memory as Action: Autonomous
Context Curation for Long-Horizon Agentic Tasks,” inFindings of
the Association for Computational Linguistics: ACL 2026, 2026, pp.
19 149–19 164.
[53] M. Zou, Z. Guo, L. Lianget al., “Remember the Decision, Not the
Description: A Rate-Distortion Framework for Agent Memory,”
arXiv preprint arXiv:2605.10870, 2026.
[54] A. G. Colaco and N. Lahjouji, “What to Keep, What to Forget:
A Rate-Distortion View of Memory Compaction in LLMs and
Agents,” arXiv preprint arXiv:2607.08032, 2026.
[55] X. Zhang, G. Wang, Y. Cuiet al., “Experience Compression Spec-
trum: Unifying Memory, Skills, and Rules in LLM Agents,” arXiv
preprint arXiv:2604.15877, 2026.

PREPRINT 13
[56] H. Mi, Y. Feng, W. Luet al., “Darwinian Memory: A Training-
Free Self-Regulating Memory System for GUI Agent Evolution,”
inProceedings of the International Conference on Machine Learning,
2026.
[57] Z. Fang, J. Wang, Y. Maet al., “R-ACP: Real-Time Adaptive
Collaborative Perception Leveraging Robust Task-Oriented Com-
munications,”IEEE Journal on Selected Areas in Communications,
vol. 43, no. 12, pp. 4215–4230, 2025.
[58] Z. Fang, Z. Liu, J. Wanget al., “Task-Oriented Communications
for Visual Navigation with Edge-Aerial Collaboration in Low Al-
titude Economy,” inProceedings of the IEEE Global Communications
Conference, 2026.
[59] B. Wu, J. Huang, and Q. Duan, “FedTD3: An Accelerated Learning
Approach for UAV Trajectory Planning,” inProceedings of the
International Conference on Wireless Artificial Intelligent Computing
Systems and Applications, 2025, pp. 13–24.
[60] B. Wu, Z. Ding, L. Ostigaard, and J. Huang, “Reinforcement
Learning-Based Energy-Aware Coverage Path Planning for Pre-
cision Agriculture,” inProceedings of the ACM Research on Adaptive
and Convergent Systems, 2025, pp. 1–8.
[61] Z. Ding, J. Huang, Q. Duanet al., “A Dual-Level Game-Theoretic
Approach for Collaborative Learning in UAV-Assisted Heteroge-
neous Vehicle Networks,” inProceedings of the IEEE International
Performance, Computing, and Communications Conference, 2025, pp.
1–8.
[62] Z. Ding, J. Huang, and J. Qi, “Learning to Defend: A Multi-
Agent Reinforcement Learning Framework for Stackelberg Secu-
rity Game in Mobile Edge Computing,” inProceedings of the Inter-
national Conference on Computing, Networking and Communications,
2026.
[63] B. Wu and W. Wu, “Model-Free Cooperative Optimal Output
Regulation for Linear Discrete-Time Multi-Agent Systems Using
Reinforcement Learning,”Mathematical Problems in Engineering,
vol. 2023, no. 1, p. 6350647, 2023.
[64] R. Zhang, X. Li, T. Xuet al., “Neuromem: A Granular Decompo-
sition of the Streaming Lifecycle in External Memory for LLMs,”
arXiv preprint arXiv:2602.13967, 2026.
[65] A. Maharana, D.-H. Lee, S. Tulyakovet al., “Evaluating Very Long-
Term Conversational Memory of LLM Agents,” inProceedings
of the 62nd Annual Meeting of the Association for Computational
Linguistics (Volume 1: Long Papers), 2024, pp. 13 851–13 870.
[66] D. Wu, H. Wang, W. Yuet al., “LongMemEval: Benchmarking Chat
Assistants on Long-Term Interactive Memory,” inInternational
Conference on Learning Representations, 2025.
[67] M. Shridhar, X. Yuan, M.-A. C ˆot´eet al., “ALFWorld: Aligning
Text and Embodied Environments for Interactive Learning,” in
International Conference on Learning Representations, 2021.
[68] S. Zhou, F. F. Xu, H. Zhuet al., “WebArena: A Realistic Web
Environment for Building Autonomous Agents,” inInternational
Conference on Learning Representations, 2024.
[69] A. Yang, B. Yang, B. Zhanget al., “Qwen2.5 Technical Report,”
arXiv preprint arXiv:2412.15115, 2024.
[70] J. Chen, S. Xiao, P . Zhanget al., “M3-Embedding: Multi-Linguality,
Multi-Functionality, Multi-Granularity Text Embeddings Through
Self-Knowledge Distillation,” inFindings of the Association for Com-
putational Linguistics: ACL 2024, 2024, pp. 2318–2335.
[71] A. Grattafiori, A. Dubey, A. Jauhriet al., “The Llama 3 Herd of
Models,” arXiv preprint arXiv:2407.21783, 2024.
[72] M. Chevalier-Boisvert, D. Bahdanau, S. Lahlouet al., “BabyAI: A
Platform to Study the Sample Efficiency of Grounded Language
Learning,” inInternational Conference on Learning Representations,
2019.
