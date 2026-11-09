---
title: Certified Task-Conditioned Active Observability
url: https://arxiv.org/abs/2609.28520
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Linzhe Zhang
- Changming Xu
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.28520
pages: 11
chars: 40730
fetched_at: '2026-11-08T13:33:36+00:00'
kb_version: 1
---

# Certified Task-Conditioned Active Observability

Certified Task-Conditioned Active Observability
Linzhe Zhang 1 Changming Xu 1
Abstract
Before an autonomous agent can act upon an
unobservable physical system, it must resolve
a fundamental operational dilemma: which la-
tent distinctions actually govern the downstream
task, how many active interventions are neces-
sary to certify them, and when must the system
abstain rather than risk catastrophic misclassifi-
cation? In classical control and physical estima-
tion, observability is posed as an unconditioned
binary predicate: either the microscopic state can
be uniquely reconstructed, or it is unobservable.
In deployed environments, however, passive ob-
servations cannot break latent degeneracies with-
out active perturbation, full microscopic inversion
is prohibitively expensive, and attempting to dis-
tinguish task-irrelevant degrees of freedom squan-
ders bounded interaction budgets. We formulate
task-conditioned active observability complexity,
determining the minimum worst-case expected in-
teraction cost required to identify the task-relevant
current state under explicit error and safe absten-
tion guarantees. We prove that task-predictive
equivalence induces the unique minimal suffi-
cient quotient H/∼ τ , leaving active observabil-
ity complexity strictly invariant while eliminating
superfluous physical distinctions. In determinis-
tic regimes, this complexity is characterized ex-
actly by an optimal adaptive distinguishing tree
and a Bellman recursion; in noisy regimes, it
obeys a stopped-transcript relative-entropy lower
bound alongside adaptive martingale certificates
that compose without independence assumptions.
We instantiate the theory in a prospective certi-
fied observer that operationalizes staged recov-
ery: a nominal verifier defers candidate compila-
tion, triggering active probing only upon evidence,
while a history-measurable score shell prunes hy-
potheses without sacrificing risk bounds. Stress
audits across high-dimensional physical systems
1Graduate School, Northeastern University. Correspondence to:
Linzhe Zhang <cfmy007@gmail.com>, Changming Xu <chang-
mingxu@neuq.edu.cn>.
Preprint. September 25, 2026.
and thousands of operational trials demonstrate
that the observer reliably recovers states while
slashing sensor reads and model steps, achiev-
ing zero false acceptances and safely abstaining
under ambiguity. The framework bridges discov-
ered physical ontologies and certified real-time
control, transforming active state recovery from
unconditioned microscopic inversion into prov-
ably minimal physical inquiry.
1. Introduction
In classical control and physical estimation, observability is
posed as an all-or-nothing predicate: either the microscopic
state can be uniquely reconstructed, or it is unobservable.
In practical deployment, however, this classical formulation
overlooks critical operational constraints. Passive observa-
tions often cannot break latent degeneracies without phys-
ical perturbation; fully inverting microscopic state spaces
is computationally and energetically prohibitive; and down-
stream tasks typically require distinguishing task-relevant
operational regimes rather than resolving superfluous phys-
ical degrees of freedom. Conversely, an observer that pre-
maturely discards candidate hypotheses risks catastrophic
misclassification. Bridging this gap demands an operational
theory of observability that explicitly balances active in-
teraction costs, hypothesis memory, and certified decision
risk.
We address this challenge by formalizingtask-conditioned
active observability: given a physical system with candi-
date hypotheses, how much active physical interaction is
necessary and sufficient to identify the task-relevant state
under certified error and safe abstention guarantees? In this
setting, an autonomous observer adaptively selects probe
actions, updates belief over candidate hypotheses, and termi-
nates either with a certified task decision or with a provably
safe abstention when ambiguity cannot be resolved within
budget.
Our first contribution formalizes task-conditioned active ob-
servability complexity, separating representation complexity
(which candidate distinctions govern downstream task out-
comes) from interaction complexity (the minimal cost of
adaptive experiments required to separate them). We prove
1
arXiv:2609.28520v1  [stat.ML]  22 Sep 2026

Certified Task-Conditioned Active Observability
that task-predictive equivalence induces the unique mini-
mal sufficient quotient H/∼ τ , eliminating task-irrelevant
distinctions while leaving active observability complexity
strictly invariant. In deterministic settings, this complexity
is characterized exactly by an optimal adaptive distinguish-
ing tree via a Bellman recursion; in stochastic regimes, it
satisfies a stopped-transcript relative-entropy lower bound
alongside adaptive martingale certificates that compose con-
structively under arbitrary filtration histories.
Our second contribution is an operational observer architec-
ture that realizes this theoretical separation in practice. The
observer decouples tracking from recovery by verifying a
lightweight nominal state first, compiling the broader fall-
back bank only when accumulated evidence warrants, and
certifying state transitions on independent forward measure-
ments. To scale recovery, a history-measurable score-shell
rule compresses the candidate bank while provably preserv-
ing conditional safety guarantees, ensuring unresolvable
ambiguities map to certified abstention rather than misclas-
sification. Furthermore, conformal calibration of the shell
rank controls marginal coverage, while an admissible lower-
bound certificate enables direct, closed-form candidate com-
pilation.
Our third contribution establishes an optimality principle
for physical resource scheduling. We prove that when can-
didate compilation produces no useful intermediate outputs
during sensing, any interleaved scheduling between sensor
reads and partial compilation is pathwise weakly dominated
by an atomic fallback policy. This result establishes that
compilation progress does not act as an intrinsic state vari-
able of the active observability problem, providing a formal
justification for executing fallback compilation atomically
upon certified trigger.
We validate the theoretical framework across high-
dimensional physical systems and extensive operational tri-
als. The experiments demonstrate that the staged observer
reliably recovers task-relevant states while substantially re-
ducing sensor queries and model computation, achieving
zero false acceptances and safely abstaining under ambigu-
ity. Together, these results provide an end-to-end framework
for certified active state recovery, transforming classical ob-
servability from unconditioned microscopic inversion into
provably minimal physical inquiry.
2. Problem formulation
2.1. Finite controlled hypothesis model
A completed operation history produces a finite candidate
set H=H(H 0). A hypothesis h∈ Hcontains a candidate
operation endpoint and its known future controlled transi-
tion and observation model. At future time t, the observer
selects At ∈ A, receives Yt ∈ Y, and updates the propa-
gated state of each candidate. The action rule, stopping time
N, and output are nonanticipating. Policies are determin-
istic measurable maps of the observed history; there is no
exogenous randomization, and all probability comes from
the observation process. The output is either a label bτ∈Θ
or abstention⊥.
A fixed task map
τ:H →Θ(1)
specifies which distinctions matter. It can request the exact
operation endpoint, an active/inactive label, or any other
fixed task-relevant quotient. When the desired report is
a current state, the operation-end label can be propagated
through the executed confirmation actions before output.
Let c(a)>0 be the physical interaction cost of action a. A
policyπis(α, β)-valid if, uniformly for allh∈ H,
π
Pr
h
(bτ /∈ {τ(h),⊥})≤α,(2)
π
Pr
h
(bτ=⊥)≤β.(3)
The worst-case task-conditioned active observability com-
plexity is
AOα,β(H, τ) = inf πvalid sup h∈H Eπ h
" NX
t=1
c(At)
#
.(4)
The value is +∞ if no valid policy exists. Computation is
recorded separately in the empirical study; it can also be
folded into a generalized cost when it is serial and action-
independent.
2.2. Task-predictive equivalence
Let E be the family of finite deterministic nonanticipating
experimental policies. For ν∈E , write P ν h for the induced
finite transcript law.
Definition 2.1(Task-predictive equivalence).Two hypothe-
ses are equivalent, writtenh≡ τ h′, when
τ(h) =τ(h ′)andP ν h =P ν h′ for everyν∈E.(5)
For standard controlled Markov kernels, equality can equiv-
alently be checked on all finite open-loop action words;
adaptive transcript equality then follows by conditioning on
the common history and induction.
Theorem 2.2(Minimal predictive quotient).Let Q=
H/≡ τ . Then:
1. every representation from which both τ(h) and all
future experimental laws can be recovered must refine
Q;
2.Qis sufficient;
2

Certified Task-Conditioned Active Observability
3. for everyα, β,
AOα,β(H, τ) =AOα,β(Q,¯τ).(6)
Thus Q is the unique minimal sufficient representation up to
relabeling.
The theorem isolates the only candidate distinctions that
can affect either the answer or any future evidence. It also
justifies quotienting before optimizing an active observer.
Corollary 2.3(Identifiability obstruction).Suppose two
hypotheses have different task labels but identical transcript
laws under every policy. If 2α+β <1 , then no (α, β)-valid
observer exists.
3. Active observability theory
3.1. Exact deterministic characterization
Assume deterministic transitions and observations. An infor-
mation configuration S is a finite set of pairs (ℓ, z), where
ℓ is the fixed task label of an initial hypothesis and z is its
current propagated state. Duplicate pairs are removed. A
configuration ispureif all pairs have the same label. For
action a and observation y, let Sa,y be the propagated subset
that producesy.
A task-separating experiment tree places actions at internal
nodes, observations on edges, and label-pure configurations
at leaves. Define its minimax cost by
D(S) = inf
T
max
ℓ∈leaves(T)
X
v∈path(ℓ)
c(av),(7)
withD(S) = +∞when no finite separating tree exists.
Theorem 3.1(Deterministic closure).For a deterministic
noiseless controlled system,
AO0,0(S) =D(S).(8)
Equivalently, D is the least extended nonnegative solution
of
D(S) = 0for pureS,(9)
and otherwise
D(S) = inf
a∈A

c(a) + max
y:Sa,y̸=∅
D(Sa,y)

.(10)
The equality is exact, not asymptotic: every exact policy
unfolds into a separating tree, and every such tree is an exe-
cutable exact policy. Combined with theorem 2.2, it gives a
two-step characterization: first quotient the representation,
then solve the minimum distinguishing-tree problem.
3.2. Noisy information lower bound
Let Pπ h denote the stopped transcript law, including the
decision, under policyπ. Define binary relative entropy
d(p∥q) =plog p q + (1−p) log 1−p 1−q .(11)
Theorem 3.2(Pairwise stopped-transcript necessity).As-
sume 2α+β <1 . For every (α, β)-valid policy and every
pair withτ(h)̸=τ(h ′),
DKL(Pπ h∥Pπ h′)≥d(1−α−β∥α).(12)
For controlled Markov observations with kernel K(· |z, a),
the adaptive chain rule yields
DKL(Pπ h∥Pπ h′) =E π h
NX
t=1
DKL

K(· |zh t , At) 
K(· |zh′ t , At)  . (13)
Let Γh→h′ be the largest one-step directed KL per unit cost
over paired states reachable under a common action history.
Then
AOα,β(H, τ)≥max τ(h)̸=τ(h ′) max
 d(1−α−β∥α)
Γh→h′
,
d(1−α−β∥α)
Γh′→h

.
(14)
A zero information rate for any task-inequivalent pair makes
the complexity infinite.
3.3. Certified-tree upper bound
A node-level certified test may itself be sequential. At node
v with candidate configuration Sv, it has a correct branch
map bv :S v →B v and, conditional on every possible entry
history, obeys
Pr
h
(bbv /∈ {bv(h),⊥} | Fentry)≤α v,(15)
Pr
h
(bbv =⊥ | Fentry)≤β v,(16)
with conditional expected cost at most cv. A certified distin-
guishing tree has task-pure leaves and stops globally if any
node abstains.
Theorem 3.3(Adaptive certified composition).Executing
a certified distinguishing tree gives
Pr(wrong task label)≤max
ℓ
X
v∈path(ℓ)
αv,(17)
Pr(abstain)≤max
ℓ
X
v∈path(ℓ)
βv,(18)
3

Certified Task-Conditioned Active Observability
and worst-case expected cost at most
max
ℓ
X
v∈path(ℓ)
cv.(19)
No independence between node tests is required.
Corollary 3.4(Active-observability sandwich).Let Lα,β de-
note the pairwise information lower bound in equation(14),
and let Uα,β be the least path cost of a certified tree satisfy-
ing the pathwise risk budgets. Then
Lα,β ≤AO α,β ≤U α,β.(20)
In the deterministic noiseless specialization, the certified-
tree optimum reduces to the exact quantity
DTin
crefthm:deterministic.
4. Certified observer construction
4.1. Nominal-first staged confirmation
Rather than compiling the full hypothesis space H(H0) up-
front, the observer maintains a nominal candidate N={n}
for expected tracking while deferring compilation of the
generic fallback candidate bank G(H0), where the unified
candidate set is U=N∪G . The observer first interro-
gates N on a fresh observation stream under risk budget
αnom. If confirmed, n is accepted immediately at minimal
query and compute cost; otherwise, atomic fallback com-
piles and verifies U on subsequent independent measure-
ments under risk budget αfall. Partitioning the overall risk
budget as αnom +α fall ≤α guarantees conditional safety
via theorem 3.3, with candidate set instantiation statistically
decoupled from certification.
4.2. Readwise evidence-triggered fallback
In latency-sensitive deployments, waiting for exhaustive
nominal rejection can incur unnecessary physical query cost.
The observer incorporates an evidence-triggered sequen-
tial rule that monitors the running verification transcript
readwise. When intermediate observations yield strong
discordant evidence against N, the system preemptively
triggers atomic fallback without exhausting the nominal
testing budget. Because the trigger functions as an adap-
tive stopping rule while fallback certification operates on
disjoint subsequent data, this early switching modulates
interaction cost without compromising conditional safety
guarantees. The parameter λ≥0 governs the interaction-
versus-compilation tradeoff in algorithm 1, evaluated across
frozen values λ∈ {0,10,100,1000} alongside eager and
staged baselines.
Algorithm 1Certified Staged Active Observer
Require: Tracking history H0, task map τ, query budget
Tmax, thresholdλ, risk budgets(α nom, αfall).
Ensure: Certified task decision ˆℓ∈Θ or safe abstention ⊥.
1: Initialize nominal candidate N← {n}from history H0.
2:// Phase 1: Nominal sequential verification
3:fort= 1, . . . , Tmax do
4:Query actionA t and record measurementY t.
5:Update nominal evidence margin∆ t(n).
6:if∆ t(n)≥γ conf (αnom)then
7: return τ(n) {Nominal certified under risk αnom}
8:else if∆ t(n)≤ −λthen
9:break{Preemptively trigger fallback}
10:end if
11:end for
12:// Phase 2: Score-shell candidate compression
13: Instantiate generic bank G(H0) and form union U←
N∪G(H 0).
14: Evaluate lexicographic scores ρ(c) via (21) for c∈U .
15: Compress to top- J score-shells: Sshell ←
FilterShells(U, J= 8).
16: // Phase 3: Disjoint confirmation and certified deci-
sion
17: Execute verification actions on Sshell over fresh obser-
vation stream.
18: ifunique candidate c∗ ∈S shell is certified under risk
αfall then
19:returnτ(c ∗)
20:else
21:return⊥{Safe abstention satisfying theorem 3.3}
22:end if
4.3. Score-shell compression and exact compilation
Each endpoint candidate c receives the lexicographic score
ρ(c) = (mis(c),so(c) + sy(c),max{so(c),sy(c)}).(21)
Candidates with the same score form a shell. The com-
pressed representation keeps the first J distinct shells after
endpoint-wise minimization, plus the nominal endpoint.
Theorem 4.1(History-measurable sub-bank safety).Let
H0 be the completed operation history and let B(H0) be
any finite history-measurable candidate bank fixed before
a fresh confirmation stream. If the verifier has conditional
family-wise false-accept probability at most α for every
fixed bank, then
Pr(wrong acceptance|H 0)≤α.(22)
Candidate omission can reduce coverage, but it cannot in-
crease the allocated false-accept bound.
4

Certified Task-Conditioned Active Observability
Calibration is performed in exchangeable blocks that each
contain all 20 active strata. If Mi is the maximum true-shell
rank in blockiandJ m = maxi≤m Mi, then
Pr(Mm+1 ≤J m)≥ m m+ 1 .(23)
The inequality follows because failure requires the final
block to be a unique strict maximum. With m= 100 , the
frozen choice J= 8 has next-block marginal coverage at
least100/101.
Exact direct compilation.To avoid enumerating the full
bank before discarding later shells, every partial search node
u is assigned an admissible lexicographic lower bound L(u)
on the score of all of its completions. Once eight distinct
endpoint-best shells have been found with eighth threshold
θ8, the search terminates directly when
min
u∈OPEN
L(u)> lex θ8.(24)
When this certificate fails, the compiler falls back to exact
exhaustive enumeration. Hence the hybrid compiler returns
the identical endpoint-score candidate map as exhaustive
filtering on every input while bypassing unviable branches.
Theorem 4.2(Atomic fallback dominance).Assume the
compilation target is fixed before confirmation, compilation
has no usable intermediate output, compute produces no
plant observation, read and compute costs add serially, and
there is no deadline, discount, or reward for early com-
pletion. Every policy that interleaves reads and partial
compilation is pathwise weakly dominated by a policy that
performs no compilation until an observation stopping time
and then either never compiles or completes the entire fall-
back atomically.
The proof moves all useful compile microsteps to the first
point at which the completed bank is used and deletes all
unused work. The read sequence, decision, and useful com-
putation are unchanged; therefore, compilation progress
need not appear as an additional state variable in the active-
observability formulation.
5. Empirical evaluation
5.1. Experimental setup and evaluation metrics
We evaluate the certified active observability framework
across three complementary benchmark domains:
Benchmark domains.First, a prospective closed-loop
control testbed evaluates sequential tracking and fallback
policies across two 24-bit controlled Boolean models with
96 public commands. Each operational episode executes
192 commanded actions under hidden command substitu-
tions and sensor flips. The benchmark spans 72 prospective
87.5 90.0 92.5 95.0 97.5 100.0 102.5 105.0
Mean future physical reads
2
3
4
5
6
7
8Mean model computation (millions of steps)
Eager
Staged
Readwise lambda=0
Readwise lambda=10
Readwise lambda=100
Readwise lambda=1000
Figure 1.Mean physical interaction versus mean model compu-
tation for the six frozen controller policies. Eager compilation is
separated from the cluster of deferred policies. Readwise thresh-
olds trace a physical-read/computation tradeoff inside that cluster.
tasks across six families, consisting of 20 active and 52
inactive operations. To ensure strict paired comparisons
without multiplying physical risk, every policy replays iden-
tical prospective observation streams of length at most 600.
Second, a large-scale confirmatory benchmark evaluates
candidate compression and compiler exactness over 100
calibration blocks and 100 independent evaluation blocks,
comprising 2,000 total operations across the 20 active strata.
All hyperparameters are frozen prior to evaluation, with
J= 8 , a probe target of 16 shells, and an evaluation budget
of 95,000 queries. Third, a synthetic control suite evalu-
ates theoretical invariants across 600 random deterministic
Mealy automata and 5,000 adaptive stochastic policies.
Evaluation dimensions.Performance is audited across
four operational axes: (i)physical interaction cost, mea-
sured by future sensor reads and commanded actions;
(ii)computational complexity, quantified by candidate-
compilation evaluations and verifier model steps; (iii)certi-
fication reliability, tracked via correct confirmations, safe
abstentions, and empirical false acceptances; and (iv)com-
piler exactness, verified by state-by-state equality of pruned
versus full candidate maps. Candidate coverage and con-
ditional false-accept safety are audited and reported sepa-
rately.
5.2. Closed-loop interaction and computation trade-offs
All six evaluated controller policies correctly confirm all
72 prospective tasks without producing unknown outcomes.
Table 1 and Figure 1 summarize the aggregate interaction
and computational trade-offs. Eager compilation incurs
severe computational waste by executing 8.62 million model
steps to compile candidates unconditionally across all 52
inactive tasks. In contrast, nominal-first staging exploits
expected physical regularity, reducing model computation
more than five-fold to 1.65 million steps while lowering
mean future reads from 104.25 to 88.76.
5

Certified Task-Conditioned Active Observability
Table 1.Prospective task-level controller results. All policies are correct on 72/72 tasks. Model computation includes candidate
compilation, propagation, and verifier steps.
Policy Mean reads Model steps (M) Compilations Correct
Eager 104.250 8.6213 72 72/72
Staged 88.764 1.6532 20 72/72
Readwiseλ= 086.375 1.9802 47 72/72
Readwiseλ= 1086.2221.6862 36 72/72
Readwiseλ= 10087.431 1.6527 21 72/72
Readwiseλ= 100087.7081.6505 2072/72
Table 2.Stratified performance breakdown across the 72 prospec-
tive controller tasks under formal staging and conservative read-
wise fallback.
Outcome Policy Episodes Mean reads Compilations
Active Staged 20 104.600 20
Active Readwise
λ= 1000
20 100.800 20
Inactive Staged 52 82.673 0
Inactive Readwise
λ= 1000
52 82.673 0
Readwise evidence-triggered switching further optimizes
this Pareto frontier. Rather than waiting to exhaust the
nominal testing budget, the readwise rule monitors accumu-
lated discordance and triggers fallback early. Conservative
switching with λ= 1000 compiles the exact same 20 ac-
tive tasks as formal staging while trimming mean future
reads from 88.76 to 87.71. More aggressive switching with
λ= 10 achieves the lowest physical interaction at 86.22
reads, though incurring 16 unnecessary compilations on
inactive tasks.
Table 2 reveals the mechanistic origin of these savings by
stratifying tasks across operational outcomes. The domain
naturally bifurcates into two regimes: (i)inactive opera-
tions, comprising 52 tasks or 72.2% of the domain, where
the nominal hypothesis is confirmed immediately using only
82.67 future reads and zero candidate compilations; and
(ii)active operations, comprising 20 tasks or 27.8% of
the domain, where conservative readwise triggering with
λ= 1000 reduces average reads from 104.60 to 100.80.
Crucially, the median fallback trigger shifts from 9 reads
under formal rejection down to 4 reads under readwise mon-
itoring. Evidence-triggered switching thus protects nominal-
path throughput without compromising worst-case safety
auditing.
5.3. Representation compression and exact compilation
Candidate compression and coverage calibration.Re-
stricting the fallback bank to the top-J= 8 score shells elim-
inates 85.51% of candidate states, dropping from 7,520,508
Candidate states Verifier model steps Physical reads
0.0
0.2
0.4
0.6
0.8
1.0Normalized cost
0.145 0.144
0.978Full bank
T op-8 shells
Figure 2.Cost retained after replacing the full fallback bank with
the first eight score shells. Candidate states and verifier computa-
tion fall to about 14.5% of the full-bank values; physical interaction
changes much less.
to 1,090,024, and 85.57% of verifier model steps, drop-
ping from 140,052,481 to 20,210,639, while reducing phys-
ical reads by 2.19% through earlier verification (Table 3,
Figure 2). Across 2,000 independent operations, the true
endpoint is certified in 1,999 instances, with the single omis-
sion resulting in a safe abstention, thereby achieving zero
false acceptances and zero unknown outcomes. This con-
firms theorem 4.1: representation pruning governs empirical
coverage as a calibrated availability property while strictly
preserving conditional safety.
Compiler exactness and search truncation.Direct score-
shell compilation reproduces the candidate-score map of
full exhaustive enumeration with 100% state-by-state iden-
tity across all 2,000 operations. When the lexicographic
bound in (24) certifies that unexpanded branches cannot
reach the eighth score shell, search terminates early. Direct
certificates are established in 38 operations, reducing com-
pilation evaluations by 28.19% on those instances. Over
the full 2,000-operation benchmark, total evaluations fall
from 10,033,791,134 to 9,929,092,066, representing a net
reduction of 104,699,068 evaluations (1.04%) that fully ab-
sorbs the 91,390,153 evaluations expended on uncertified
exploratory probes in the remaining 962 operations. Exact
fallback boundaries ensure that branch pruning introduces
zero approximation error into state verification.
6

Certified Task-Conditioned Active Observability
Table 3.Independent 2,000-operation score-shell confirmation.
Metric Full bank Top-8 shells Change
Candidate states 7,520,508 1,090,024−85.51%
Verifier model steps 140,052,481 20,210,639−85.57%
Physical reads 203,135 198,683−2.19%
Correct confirmations 2,000 1,999−1
Safe rejections 0 1+1
Wrong acceptances 0 0 0
Theoretical invariants on synthetic systems.Across 600
random Mealy automata and 5,000 adaptive noisy policies,
the structural predictions of section 3 hold uniformly. Task-
predictive quotienting preserves exact distinguishing depth
in all 600 deterministic systems while reducing state repre-
sentations in 75. In stochastic regimes, stopped-transcript
relative entropy strictly dominates the divergence of every
induced binary decision event, and the explicit information
lower bound d(1−α−β∥α) holds across all 461 nonvacu-
ous risk-constrained instances.
6. Related work
Classical linear and nonlinear observability characterize
whether internal state can be reconstructed from input-
output behavior (Kalman, 1960; Hermann & Krener, 1977).
Active state-estimation work chooses inputs to improve es-
timation quality (Hu & Ersson, 2004). Our formulation
differs by making task equivalence, finite candidate repre-
sentations, interaction cost, error, and abstention explicit,
and by seeking an exact finite-system characterization rather
than a rank condition or estimator design.
Sequential experimental design and controlled sensing study
how actions should be chosen to discriminate hypotheses
under sample or decision-risk constraints (Chernoff, 1959;
Wald, 1947; Naghshvar & Javidi, 2013; Nitinawarat et al.,
2013). The KL lower bound in theorem 3.2 follows this
information-theoretic lineage. Our emphasis is the interface
between evolving controlled states, task-conditioned quo-
tients, certified node tests, candidate compilation, and safe
abstention.
Finite-state-machine testing studies state identification,
distinguishing sequences, and conformance experiments
(Moore, 1956; Chow, 1978; Lee & Yannakakis, 1994;
van den Bos & Vaandrager, 2019). The deterministic tree
in theorem 3.1 is closely related to adaptive distinguishing
experiments, but here it is embedded in a risk-controlled
noisy observer and coupled to history-dependent candidate
representations.
While automata learning reconstructs unknown state ma-
chines from query responses (Angluin, 1987; Vaandrager,
2017), our setting optimizes state recovery within a known
dynamical representation.
Interface with physical coordinate discovery and ontol-
ogy learning.The active observability framework devel-
oped here addresses a complementary operational challenge
to the physical representation learning program established
in Papers 1–3 of this series (Zhang & Xu, 2026a;b;c). In
physical representation learning, an autonomous agent seeks
to discover the continuous coordinate geometry, Lie group
gauge symmetries, and thermodynamic contact structures
(T, η)of an unknown physical system through experimen-
tal scaling, contact, and reservoir interventions. Once this
continuous physical ontology is discovered and frozen, prac-
tical execution in autonomous facilities, such as self-driving
synthesis laboratories or battery management platforms, re-
quires monitoring the operational regime in real time.
In such deployed environments, full continuous state decon-
volution is often unobservable or prohibitively expensive
under bounded instrumentation. Task-conditioned active
observability bridges this divide: by quotienting the state
space modulo the target control task into H/∼ τ , the agent
avoids wasting physical resources to resolve task-irrelevant
physical fluctuations, while retaining certified mathematical
guarantees against erroneous state assertions.
7. Limitations
The theoretical guarantees apply to finite controlled mod-
els with known representations under deterministic policies.
The formulation focuses on certified tracking within verified
dynamics and does not address unanchored cold-start identi-
fication or unmodeled process faults. Extending the guaran-
tees from marginal next-block coverage to distribution-free
conditional coverage across arbitrary covariates remains an
open theoretical direction.
Our atomicity analysis considers sequential evaluation; ex-
tending the framework to parallel execution, execution dead-
lines, or incremental candidate generation presents a practi-
cal direction for deployment.
7

Certified Task-Conditioned Active Observability
8. Conclusion
Task-conditioned active observability separates a system’s
minimal predictive representation from the interaction
needed to identify its current task-relevant state. The predic-
tive quotient is uniquely minimal and leaves the complexity
unchanged. Deterministic systems admit an exact adaptive-
tree characterization; noisy systems admit complementary
information lower bounds and certified-tree upper bounds.
The prospective observer demonstrates how these ideas
organize practical choices: defer expensive candidates,
trigger fallback from evidence, use fresh confirmation data
after selection, compress representations without conflating
safety and coverage, and stop expanding the controller
when partial computation has no decision value.
Within a fixed representation, tightening the gap between
the noisy information lower bound and executable certified
trees remains the primary open direction.
8

Certified Task-Conditioned Active Observability
References
Angluin, D. Learning regular sets from queries and coun-
terexamples.Information and Computation, 75(2):87–
106, 1987. doi: 10.1016/0890-5401(87)90052-6.
Chernoff, H. Sequential design of experiments.The Annals
of Mathematical Statistics, 30(3):755–770, 1959. doi:
10.1214/aoms/1177706205.
Chow, T. S. Testing software design modeled by finite-state
machines.IEEE Transactions on Software Engineering,
SE-4(3):178–187, 1978. doi: 10.1109/TSE.1978.231496.
Hermann, R. and Krener, A. J. Nonlinear controllability and
observability.IEEE Transactions on Automatic Control,
22(5):728–740, 1977. doi: 10.1109/TAC.1977.1101601.
Hu, X. and Ersson, T. Active state estimation of nonlinear
systems.Automatica, 40(12):2075–2082, 2004. doi:
10.1016/j.automatica.2004.06.015.
Kalman, R. E. A new approach to linear filtering and pre-
diction problems.Journal of Basic Engineering, 82(1):
35–45, 1960. doi: 10.1115/1.3662552.
Lee, D. and Yannakakis, M. Testing finite-state machines:
State identification and verification.IEEE Transactions
on Computers, 43(3):306–320, 1994. doi: 10.1109/12.
272431.
Moore, E. F. Gedanken-experiments on sequential machines.
In Shannon, C. E. and McCarthy, J. (eds.),Automata
Studies, volume 34 ofAnnals of Mathematics Studies, pp.
129–153. Princeton University Press, 1956.
Naghshvar, M. and Javidi, T. Active sequential hypothesis
testing.The Annals of Statistics, 41(6):2703–2738, 2013.
doi: 10.1214/13-AOS1144.
Nitinawarat, S., Atia, G. K., and Veeravalli, V . V . Controlled
sensing for multihypothesis testing.IEEE Transactions
on Automatic Control, 58(10):2451–2464, 2013. doi:
10.1109/TAC.2013.2261188.
Vaandrager, F. Model learning.Communications of the
ACM, 60(2):86–95, 2017. doi: 10.1145/2967606.
van den Bos, P. and Vaandrager, F. State identification for
labeled transition systems with inputs and outputs.arXiv
preprint arXiv:1907.11034, 2019.
Wald, A.Sequential Analysis. John Wiley and Sons, New
York, 1947.
Zhang, L. and Xu, C. Discovering physical representation
languages: Metric-free axiomatics and topological ontol-
ogy identification.arXiv preprint, 2026a.
Zhang, L. and Xu, C. Blind thermodynamic ontology dis-
covery from anonymous experiments.arXiv preprint,
2026b.
Zhang, L. and Xu, C. Parasitic-free three-frequency laws
for positive relaxation ports.arXiv preprint, 2026c.
9

Certified Task-Conditioned Active Observability
A. Proofs
A.1. Proof of the minimal predictive quotient theorem
Suppose a representation r(h) is sufficient to recover both
τ(h) and the transcript law of every future experiment. If
r(h) =r(h ′), every decoded quantity agrees, henceτ(h) =
τ(h ′) and P ν h =P ν h′ for every ν. Therefore h≡ τ h′ and
every sufficient representation refinesQ.
Conversely, one task label and one family of future experi-
mental laws are well-defined on every equivalence class, so
Q is sufficient. Any policy on H induces identical transcript,
cost, error, and abstention laws for all members of a class
and therefore descends to Q. Every policy on Q lifts to H.
Taking the same infimum and supremum proves complexity
invariance.□
For theorem 2.3, let E be the event that the observer outputs
τ(h). Under h, validity requiresPrh(E)≥1−α−β . Under
h′, the same output is wrong, so Prh′(E)≤α . Identical
transcript laws imply identical output laws, contradicting
1−α−β > α.
A.2. Proof of the deterministic closure theorem
Fix any exact policy. By the policy convention in section 2,
its decisions are deterministic functions of the observation
history, so unfolding them gives an action-observation tree.
At every reachable stopping leaf, all remaining candidate
pairs must have the same task label; otherwise the common
output would be wrong for at least one candidate. Hence
the policy induces a finite task-separating tree with the same
worst-case cost and cannot beatD(S).
Conversely, execute any task-separating tree and output the
unique label at the reached leaf. The policy is exact and
has the tree’s worst-case path cost. Taking infima proves
AO0,0(S) =D(S) . Decomposing a nonterminal tree at its
root gives the Bellman lower bound in equation (10); adjoin-
ing optimal child trees gives the reverse bound. Because all
action costs are positive, the least extended solution assigns
+∞ exactly to configurations with no finite separating tree.
□
A.3. Proof of the KL lower bound
Let E={bτ=τ(h)} . Under h, Pπ h(E)≥1−α−β ; under
h′, Pπ h′(E)≤α . Data processing through the indicator 1E
gives
DKL(Pπ h∥Pπ h′)≥d(P π h(E)∥Pπ h′(E)).(25)
Since1−α−β > α, binary relative entropy is increasing
in its first argument and decreasing in its second over the
relevant rectangle. This proves equation (12).
For the cost bound, the action-selection kernels are the same
functions of the observed history under both hypotheses
and cancel in the likelihood ratio. The chain rule gives
equation (13). Each term is at mostΓ h→h′c(At), hence
Eπ h
NX
t=1
c(At)≥ d(1−α−β∥α) Γh→h′ .(26)
Repeat in the reverse direction and use the worst-case ob-
jective.□
A.4. Proof of certified adaptive composition
A wrong terminal label implies that at least one visited node
misrouted the true hypothesis. Condition on each node’s
entry sigma-field. Its misrouting probability is at most αv
for every possible entry history. The tower property and
a union bound over the realized root-to-leaf path give the
path sum. Maximizing over paths gives the first bound. The
abstention proof is identical. Conditional expected costs add
by iterated expectation, and the sum along every realized
path is bounded by the largest path sum. No cross-node
independence is used.□
A.5. Proof of history-measurable sub-bank safety
Condition on the completed operation history H0. Then
B(H0) is a fixed finite bank. By the fixed-bank verifier
guarantee,
Pr(wrong acceptance|H 0, B(H0))≤α.(27)
Because B(H0) is measurable with respect toH0, condition-
ing on both is the same as conditioning on H0. Candidate
omission does not alter this inequality; it only removes the
completeness premise needed to guarantee an acceptance.
□
For equation (23), exchangeability makes every block
equally likely to be the unique strict maximum among
m+ 1 block maxima. Failure occurs only when the last
block is that unique maximum, whose probability is at most
1/(m+ 1). Ties can only improve coverage.
A.6. Proof of atomic fallback dominance
Fix a realized read/outcome path of an arbitrary policy. If
no completed bank is used, delete every compile microstep.
If a completed bank is first used at some observation stop-
ping history, move every useful compile microstep to one
contiguous block immediately before that use. Compila-
tion emits no observation, does not change the plant, and
has a fixed target, so all read-dependent decisions and the
completed bank remain unchanged. Additive serial cost
remains the same; unused work is deleted. Applying this ex-
change pathwise yields a policy that never maintains partial
progress and is weakly cheaper on every path.□
10

Certified Task-Conditioned Active Observability
B. Additional protocol details
B.1. Staged risk accounting
The eager verifier uses false-accept budget 1/2,000,000.
The staged method uses α1 =α 2 = 1/4,000,000. Let A1
be a wrong nominal acceptance and A2 a wrong fallback
acceptance. Conditional on the entire stage-1 history and
on entering stage 2, the propagated bank is fixed before the
fresh stage-2 stream. Therefore
Pr(A1 ∪A 2)≤Pr(A 1) +E[Pr(A2 | Fstage1)]≤α 1 +α 2.
(28)
This argument does not assume that the full or compressed
bank contains truth.
B.2. Why stage-1 reads are not rescored
The decision to materialize the generic bank is a function of
stage-1 data. Rescoring the newly selected bank on those
same observations would use the data both for model se-
lection and confirmation, invalidating the fixed-bank condi-
tional guarantee unless a selective-inference correction were
supplied. The protocol instead propagates the bank through
the executed actions and starts a new verifier on fresh data.
B.3. Exact direct-shell certificate
At a partial compiler node, let the current score components
be (m, so, sy), and let ro, ry be the remaining opportunities
to reduce the two window scores. The lower bound
L(u) =

m,[s o −r o]+ + [sy −r y]+,
max{[so −r o]+,[s y −r y]+}
 (29)
is admissible and lexicographically nondecreasing along
every search path. If the current endpoint-best map con-
tains eight distinct shells and every open node has lower
bound strictly larger than the eighth shell, no unseen com-
pletion can change any retained endpoint score. An arbitrary
probe may propose an achievable threshold, but only the
exhaustive bounded search below that threshold supplies the
certificate. Failure invokes exact full enumeration.
C. Additional empirical results
C.1. Parallel speculation sensitivity
A separate-worker sensitivity study compares deferred com-
pilation, full background compilation, evidence-gated back-
ground compilation, and actual readwise switching on 72
new prospective streams. Evidence-gated background com-
pilation uses the same trigger as readwise switching but
continues the nominal verifier, spending 85 additional reads
in aggregate. Full speculation provides a 0.258% wall-clock
advantage at 1 ms/read and 0.085% at 10 ms/read while
using 1.95 and 5.36 times as much compilation CPU, re-
spectively; at 100 ms/read, readwise switching is faster. The
measured aggregate crossing is 12.78 ms/read. This is a
deployment sensitivity for the frozen compiler and traces,
not a hardware-independent theorem.
C.2. Development replay
Before the independent 2,000-operation shell confirmation,
the same J= 8 representation is replayed on the inherited
72 controller tasks. It remains correct on 72/72, reduces fall-
back candidates by 62.20%, reduces model steps by 62.02%,
and saves 98 physical reads. This replay is developmental;
the frozen independent split is the primary evidence.
11
