---
title: 'Monitor Accuracy Isn''t the Answer: A Decision-Value Framework for Evaluating AI Agent Restart
  Monitors'
url: https://arxiv.org/abs/2610.36544
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Siddharth Jain
- Venkat N. Vedam
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.36544
pages: 29
chars: 84700
fetched_at: '2026-11-08T13:35:44+00:00'
kb_version: 1
---

# Monitor Accuracy Isn't the Answer: A Decision-Value Framework for Evaluating AI Agent Restart Monitors

Monitor Accuracy Isn’t the Answer:
A Decision-Value Framework for Evaluating
AI Agent Restart Monitors
Siddharth Jain
Intuit
Venkat N Vedam
Intuit
Abstract
Failure monitors for AI agents can be judged by classification accuracy and true-positive and
false-positive rates on labeled failures. We show that these metrics alone do not determine what
actually matters: whether a restart improves success. Using an exact alarm-to-action identity
for an independent clean restart with zero monitoring overhead, we show analytically that a
monitor with fixed 90% accuracy can swing from a five-percentage-point loss to a 35-point gain
in success rate, depending solely on the replacement attempt’s residual-budget success proba-
bility, a quantity accuracy never measures. Building on this, we introduce two techniques for
evaluating monitors and progress signals directly in decision terms rather than classification
terms. First, a decision-sufficiency criterion, a binary-action specialization of Blackwell’s com-
parison of experiments, identifies exactly which progress representations or context compressions
preserve the information needed to choose optimally between the specified actions, independent
of how faithfully they reconstruct the trace. Second, a finite-sample, model-free decision audit
uses simultaneous binomial intervals over existing agent traces, without additional model calls,
to certify a preference for “restart” or “continue” under stated sampling assumptions, or return
an explicit “abstain” when evidence is insufficient, instead of reporting an unqualified point es-
timate. Applied to a study of 194 externally evaluated model executions on 19 selected SymPy
issues from SWE-bench Verified, with a retrospective audit of 130 of these traces, this approach
exposes what accuracy-based evaluation alone cannot establish: a 2.29-point apparent restart
gain traced to a single surviving failed attempt, a 42.29-point loss on a second model, no positive
replication of the initial gain on prospective task cohorts, and zero of 103 live comparisons meet-
ing the specified certification bar. Together, these results motivate evaluating agent monitors
through recovery opportunity, decision value, and statistical support, rather than classification
performance alone.
1 Introduction
An agent that is unlikely to finish may also be unlikely to succeed after a restart. This distinction
matters whenever a harness acts on a failure prediction: abandoning a trajectory removes its
remaining chance of success, and the replacement receives only the residual budget. A monitor can
therefore classify failures accurately while inducing harmful decisions. Conversely, a modest signal
may be useful when it resolves a small number of decisions with large consequences.
The problem has a substantial intellectual history. Dynamic restart policies use observations
of a solver’s activity to update runtime beliefs [1]; learned schedules address distributions of prob-
lem instances [2]; Bayesian early stopping derives policies from observed run features [3]. Re-
cent agent systems demonstrate useful termination and recovery, including EET [4] and FailFast-
RestartSmart [5]. Our contribution is not the premise that progress can inform stopping. We ask
1
arXiv:2610.36544v1  [cs.AI]  27 Oct 2026

how to make a claimed progress signal’sdecision valueand evidential supportexplicit under a finite
interaction budget.
Three questions organize the study:
RQ1
Which quantities determine whether a failure alarm improves success after a restart?
RQ2
What information must a progress representation retain, and when do available traces justify
a continuation or restart decision?
RQ3
How do these distinctions explain observed outcomes of restart, horizon extension, context
recovery, and failed-branch reuse?
We make the intervention precise. For a live attempt, continuation retains its state and spends
the remaining budget; a clean restart restores the original task state and spends the same budget on
a fresh attempt. A context reset that retains edits is a separate action, with a separate outcome law.
Under this definition, we derive an exact relation between alarm true-positive rate, false-positive
rate, continuation success, and restartability. An analytical control keeps failure classification
accuracy at90% while changing restart gain from−5 to +35 points solely by changing the success
probability of the replacement. This is a controlled mathematical example, not a performance claim
about an implemented detector.
The information question follows naturally. Progress need not be a monotone scalar. It can
be a representation that preserves distinctions relevant to the action. We give a binary-action
specialization of classical information comparison [6]: compressing a history loses decision value
when the compressed observation combines positive and negative continuation advantages. Exact
decision sufficiency is an ideal benchmark; an imperfect representation can still improve utility. We
then implement a conservative audit that exposes the statistical support for each action, including
an abstention when the evidence does not resolve the sign.
The empirical evidence consists of 194 model-driven executions of mini-swe-agent on 19 selected
SymPy issues in SWE-bench Verified [7, 8]. Each attempt begins from the benchmark-provided
repository state. The reference patch and evaluator remain outside the sandbox, and external
verification after each environment action records the first passing state. Earlier experiments com-
prise restart replay, prospective task transfer, additional horizon, conversational recovery, and two
bounded uses of failed branches. We retain the negative results and distinguish their design status:
later collection stages used prospectively frozen protocols, while the decision audit introduced here
is retrospective.
The audit sharpens the interpretation of the original results. Across 130 executions with a
30-call horizon, the 16-call Luna gain comes from a single eligible failed trajectory on one task. On
the second model, every task with a live attempt at that decision has an empirical advantage for
continuation. Across six decision times, all 103 comparisons with live data remain unresolved by
the simultaneous certificate. These findings distinguish visible effect size from evidence sufficient
for individual deployment decisions. They do not demonstrate that every alternative statistical
method must abstain.
Contributions.
1. An intervention-specific account of agent progress, including an alarm-to-action value identity
and an information-loss criterion for progress representations and context compression.
2

2. A dependency-free audit that estimates both action values, respects live eligibility and observed
horizons, and returns simultaneous sign certificates or abstention under explicit assumptions.
3. A reproducible retrospective analysis identifying the support of the restart effect, together with
analytical controls that separate detector accuracy, restartability, and sample resolution.
4. A sequence of externally verified agent experiments showing model-dependent restart effects and
the distinction between protocol recovery and verified task completion.
The classical decision identities are attributed and used as foundations. The empirical and
software contributions concern how those identities can discipline evaluation of current agent con-
trollers. The study does not train a monitor, directly compare against learned recovery systems,
or establish performance outside its selected tasks and runtime configurations.
2 Related Work
2.1 Restarts and inference-time allocation
Restart policies are well studied for randomized algorithms. Luby, Sinclair, and Zuckerman give
a logarithmic expected-runtime comparison with a distribution-specific fixed strategy under their
assumptions [9]. This is not a guarantee that a chosen finite-budget truncation improves success.
Dynamic restart policies already condition on solver observations and runtime beliefs [1]. Sched-
ule learning across instances [2] and Bayesian stopping from run features [3] directly precede our
formulation. The no-dominance and observation-ambiguity examples below are elementary special-
izations; novelty is not claimed for feature-dependent restarting or the need to calibrate runtime
distributions.
Our decision-value expression specializes Blackwell’s comparison of experiments [6] to two ac-
tions. The abstaining audit applies exact binomial intervals [10] and simultaneous comparison in
the spirit of safe policy improvement [11]. These foundations identify the scope of the contribution:
an explicit connection between alarm quality, intervention-specific restartability, and the statistical
support of agent decisions, implemented on externally verified traces.
Inference-time scaling allocates additional computation through sampling, voting, or search.
Self-consistency samples reasoning paths and aggregates answers [12]; Tree of Thoughts searches
over explicit intermediate candidates [13]; inference scaling studies compare compute-allocation
strategies under fixed budgets [14]. Mixture-of-Agents aggregates outputs across model instances
and layers [15]. These methods can exploit independent or weakly correlated trials and informative
scoring. Classical ensemble analysis shows why both accuracy and error diversity matter [16, 17].
Our setting removes a central advantage: the controller receives no reliable scalar score before
external task completion. We study whether schedule choice or failure-conditioned branching alone
can recover that missing information.
Iterative self-improvement methods use generated feedback to revise an answer or policy [18, 19].
Other work shows that intrinsic self-correction can fail when the feedback does not add external
information [20]. Our context-rejuvenation and semantic-resolver experiments test a related distinc-
tion at the harness level: changing the context or synthesizing failed branches can change behavior
without improving the externally verified outcome.
2.2 Agent progress and externally grounded evaluation
The closest contemporary system is FailFast-RestartSmart [5]. It trains a prefix monitor and com-
bines alarms with a fresh rollout that can inspect or apply previous edits. The paper reports both
3

cost savings and recovery gains, providing positive evidence that richer learned signals and inter-
ventions can work. EET also demonstrates useful termination from prior execution experience [4].
Our experiments do not reproduce or compare against either system. A timeout is a different
controller, and our mandatory workspace retention differs from an optional edit overlay. Our audit
complements such systems by requiring the post-alarm action and remaining-budget success to be
evaluated jointly with failure prediction.
AgentBoard introduced a progress-rate metric to complement final success across multi-turn
environments [21]. Such metrics are valuable when an environment exposes meaningful subgoals.
Park and Choi show that an agent can report improvement while externally measured state does
not improve, and argue for evaluation grounded outside the transcript [22]. We take external
grounding as a design constraint and ask what remains identifiable when the grounded signal is
binary completion rather than a dense progress measure.
Semantic early stopping detects convergence between successive drafts and can reduce tokens
in iterative question answering at comparable measured quality [23]. Geometric analyses represent
iterative outputs as trajectories, attractors, or oscillations in an embedding space [24]. These
representations describe change in semantic space, but geometric convergence is not automatically
decision sufficient for externally verified completion. VLAA-GUI uses visual completeness checks
and loop breaking in GUI automation [25]. These systems have richer task structure than our pass-
or-fail coding controller. Their results are consistent with our boundary condition: useful stopping
and recovery require a signal calibrated to the relevant external state, not elapsed calls or semantic
movement alone.
Long-horizon software agents have also motivated active context management. Context as a
Tool lets an agent compress history into structured memory [26], while later work learns or imple-
ments agent-compatible context policies [27, 28]. Our recovery intervention is deliberately simpler.
It discards conversational history after a protocol terminal event, retains the exact workspace, and
supplies a deterministic state summary. Its null result does not evaluate learned context manage-
ment. It isolates whether stale conversation alone explains observed failure in one fixed harness.
2.3 Software engineering agents and reproducible evaluation
SWE-bench evaluates repository-level issue resolution against executable tests [7]. SWE-agent es-
tablished the effectiveness of purpose-built agent-computer interfaces for these tasks [8]. We use the
compact mini-swe-agent implementation as a versioned, open-source harness. We do not compare
agent architectures or report a leaderboard estimate. Selected SymPy tasks provide controlled,
expensive trajectories with externally testable completion.
Agent evaluation is sensitive to cost, holdout design, and reproducibility [29]. Test-suite weak-
ness can also overstate issue resolution [30]. We therefore run the benchmark evaluator outside the
agent workspace after each environment action, gate tasks by base-fail and reference-pass checks,
audit every successful diff for verifier tampering, and select cutoffs with task-level holdout rather
than attempt-level splitting.
2.4 Position of this work
Prior work includes both successful stopping systems and formal restart optimization. This study
contributes an evaluation and evidence audit for a specified action pair. The distinction is summa-
rized in table 1; the negative screens do not invalidate richer systems with different observations,
training, or recovery semantics.
4

Table 1: The object measured by adjacent lines of work. A task-grounded state can support progress
decisions; a trace-only controller must infer it.
Line of work Observed quantity Primary question
Inference-time search Candidate scores or votes Which candidate should receive
compute?
Dynamic restart theory Run features and runtime
beliefs
Which restart policy minimizes expected
runtime?
Learned termination and
recovery
Prefix alarms and retained
edits
Does a trained controller save cost or
improve resolution?
Semantic stopping Change between successive
outputs
Has an iterative answer stabilized?
Trajectory evaluation Task-specific subgoal state How much of the task is complete?
Context management Structured or compressed
history
What information should the agent
retain?
This work Action values, live
eligibility, sampling
uncertainty
Does the intervention have decision
value, and is its sign supported?
3 Black-Box Progress as a Decision Problem
3.1 Setup
Fix a task, agent, model, provider policy, prompt, and tool interface. One attempt induces latent
states X0,X 1,... and observationsO1,O 2,... . This is a partially observed control process [31].
The controller’s information after callt is the filtration
Ft =σ(O1,...,O t), (1)
where observations may include actions, tool outputs, workspace summaries, external verifier re-
sults, and explicit protocol failures. Let
T = inf{t≥ 1 :V (Xt) = 1} (2)
be the first call whose resulting state passes the external verifier, withT =∞ if no such state
is reached. The belief state bt(dx) = P(Xt∈ dx|F t) is sufficient for optimal control when the
generative process is known. A black-box harness does not know this process and must approximate
decision value from its observations. A budget policyπ maps observable histories to continuation,
restart, recovery, branch, or termination actions under total call budgetB.
We usesemantic progressfor a latent property of state that predicts future verified completion.
This term does not presume that progress is monotone or one dimensional. LetQa(ht,b ) denote
expected utility when actiona is selected after historyht with b calls remaining. For the binary
continue-or-restart problem, define the continuation advantage
∆(ht,b ) =Qcont(ht,b )−Qrestart(ht,b ). (3)
The utility may combine externally verified success, calls, money, and latency, but it must be
declared before evaluating the policy.
Definition 3.1 (Decision-sufficient progress representation)An observable representation
Gt = g(O1:t) is decision sufficient for a policy class and runtime population if the optimal action
is measurable with respect to(Gt,b ). For binary control, this requires the sign of equation(3) to be
determined by (Gt,b ) almost surely.
5

Observational aliasing makes progress a control problem
Latent state Observed trace State-informed action
State A
late but viable
ΔA > 0
State B
dead branch
ΔB < 0
g(XA 0 : t) = g(XB 0 : t) = Gt
no verified pass by t
same visible actions and edits
CONTINUE
retain accumulated work
RESTART
discard the current branch
The controller sees only Gt: the sign of continuation advantage is not identifiable.
Figure 1:Observational aliasing in black-box control. Distinct latent states can induce the same observable
history while requiring opposite actions. A useful progress sensor must separate histories according to
continuation advantage, not surface activity.
This definition describes lossless action selection relative to the richer history. A representation
can be useful without attaining exact sufficiency. Embedding displacement, code churn, test counts,
and fluent self-reports may describe a trajectory while discarding a distinction that changes the
preferred action. Two histories may be close in a semantic space yet have different continuation
advantages, or look dissimilar while implying the same action.
Proposition 3.2 (Progress error is advantage-weighted decision error)Let d(ht,b ) ∈
{cont, restart} be any stopping rule and letd∗(ht,b ) select the action with larger conditional value.
Its expected regret within the binary action class is
R(d) = E[|∆(Ht,b )|I{d(Ht,b )̸=d∗(Ht,b )}]. (4)
Proof. Conditioned on a history, choosing the inferior action loses exactly the absolute difference
between the two action values; choosing the superior action loses zero. Taking expectation gives
equation (4). □
The identity shows why label accuracy is not the right primary metric for a progress detector.
Errors matter in proportion to the value difference between continuing and restarting. A detector
can achieve high accuracy on histories where the actions are nearly tied and still lose most of the
attainable utility on the few histories where|∆| is large.
3.2 Fixed restarts depend on the completion scale
Suppose fresh attempts are independent and identically distributed, restart overhead is zero, and
a live attempt is truncated at cutoffc. Write F (t) = P(T ≤ t) and decompose the total budget
as B = qc +r, whereq =⌊B/c⌋ and 0≤ r < c. If unused budget is assigned to a final residual
episode, the success probability is
Pc(B) = 1− (1−F (c))q (1−F (r)), (5)
6

withF (0) = 0. This expression assumes that noncompletion consumes the assigned episode budget.
Anexplicitterminaleventcanendanepisodeearlierandreleaseadditionalbudget, whichishandled
by trace-level replay in the experiments. An uninterrupted attempt succeeds with probabilityF (B).
The discrete completion hazard makes the missing scale explicit. Let
λu = P(T =u|T≥u). (6)
With r calls remaining and no observation beyond survival throught, continuation succeeds with
probability
C(t,r ) = 1−
t+r∏
u=t+1
(1−λu), (7)
whereas a fresh attempt succeeds with probabilityR(r) = F (r). Under equal success utility and
zero reset cost, restart is preferred exactly whenR(r) > C(t,r ). Thus elapsed time helps only
through assumptions about the hazard. A decreasing hazard favors restarts; delayed completion
mass can favor continuation. With trace featuresGt, the relevant object is the feature-conditional
residual law, not the marginal curve alone.
Proposition 3.3 (No uniformly dominant proper cutoff)For anyB≥ 2 and any fixed cut-
off 1≤c<B , there exists a completion-time distribution for which the uninterrupted policy strictly
dominates cutoff c. There also exists a completion-time distribution for which cutoff c strictly
dominates the uninterrupted policy whenever⌊B/c⌋≥ 2.
Proof. For the first claim, place all probability mass atT = c + 1≤ B. Then F (c) = 0 and
F (B) = 1. For the second, letT = c with probabilityp∈ (0, 1) and letT =∞ otherwise. Then
F (c) =F (B) =p, F (r) = 0, and equation (5) equals1− (1−p)q >p for q =⌊B/c⌋≥ 2. □
The proposition is elementary but constraining. Any positive universal-restart claim must intro-
duce assumptions on the completion distribution, a prior over task-agent tuples, or an observation
that predicts the residual completion time. Schedule shape cannot supply this information.
Corollary 3.4 (Finite-scale sensitivity)Consider any finite restart schedule whose largest
episode has lengths<B . There is a distribution supported on completion times in(s,B ] for which
the schedule has zero success and an uninterrupted attempt succeeds with positive probability.
This corollary does not contradict the classical Luby guarantee [9]. It identifies the finite-budget
role of the base scale. A universal ordering of episode lengths is not a universal calibration of model
calls.
3.3 The continuation decision is not identified by survival
Atcall c, supposetheonlytask-groundedeventisthatnoverifiedstatehasappeared. Theremaining
budget is enough for either one more call on the current attempt or one call on a fresh attempt.
Proposition 3.5 (Observational ambiguity)There are two latent completion regimes that in-
duce the same observable no-success history through callc but require opposite optimal decisions.
In one regime continuation succeeds with probability one and restart fails. In the other, conditional
continuation fails while restart has positive success probability. Consequently, no rule measurable
with respect to that history is optimal in both regimes.
7

Proof. In the late regime, let the current attempt complete deterministically atc + 1 and let a
fresh attempt require more than one call. Continuation is uniquely optimal. In the fast-or-never
regime, an attempt completes on its first call with probabilityp> 0 and never completes otherwise.
Conditional on survival throughc, the current attempt is in the never component, so continuation
fails and a fresh attempt succeeds with probabilityp. Both regimes can emit the same observation
sequence before external completion. A deterministic rule chooses the wrong action in one regime.
A randomized rule cannot attain the regime-specific optimum in both. □
The result is about identification, not metaphysical opacity. A task-specific sensor may distin-
guish the regimes. Absent such a sensor or a calibrated prior, a controller that restarts because the
trace looks stagnantimports an untested mapping from appearance to residual value.
Corollary 3.6 (Regret under observational aliasing)In the construction of proposition 3.5,
suppose a fresh attempt in the fast-or-never regime succeeds with probabilityp∈ (0, 1). For any
randomized policy that observes only the aliased history, the worst-case regret over the two regimes
is at leastp/(1 +p). The bound approaches1/2 as p approaches one.
Proof. Let the policy continue with probabilityα. Its regret is1−α in the late regime andpα in
the fast-or-never regime. Minimizingmax{1−α,pα} givesα = 1/(1 +p) and regretp/(1 +p). □
The corollary gives an operational meaning to unobservability. It is not merely that a trace
classifier may be inaccurate. Without an identifying assumption, error remains even with unlimited
computation applied to the same observable history.
An additional failure-selection example and the standard correlated-ensemble variance identity
appear in Appendix G. They motivate the branch-reuse screens but are not empirical estimates of
our patch population.
4 From Failure Prediction to Restart Decisions
The useful question is whether a signal changes expected utility under a specified intervention. This
section connects the classical value of information [6] to a finite-budget audit that can be computed
without model access. The identities specialize existing decision theory; the contribution is their
operationalization for agent termination and recovery, together with an explicit account of what
the available traces can identify.
4.1 Failure prediction must be combined with restartability
Fix one task and runtime, a live decision at callt, and residual budgetb =B−t. Let YC be the
potential binary outcome of uninterrupted continuation to the deadline. Letq = P(YC = 1), and
let p be the success probability of one independent clean restart with the same residual budget.
We callp the restartability of this decision. An alarmA = 1 triggers the restart. Define its failure
true-positive rateτ = P(A = 1|YC = 0) and false-positive rateϕ = P(A = 1|YC = 1).
Proposition 4.1 (Alarm-to-action value identity)Assume the fresh outcome is independent
of (A,YC) conditional on the fixed task and runtime, the restart restores the initial state, and the
alarm consumes no budget. The success change relative to continuing every live attempt is
G(q,p,τ,ϕ ) = (1−q)τp−qϕ(1−p). (8)
If (1−q)τ +qϕ> 0, a positive gain requires
p> qϕ (1−q)τ +qϕ. (9)
8

Proof. On correctly alarmed failures, the restart changes success from zero top, contributing
(1−q)τp. On falsely alarmed successes, it changes success from one top, contributing−qϕ(1−p).
Unalarmed outcomes are unchanged. Rearrangement gives the threshold. □
Forq = 1/2,τ = 0.9, andϕ = 0.1, the detector’s classification accuracy is90% for everyp, while
G = 0.5p− 0.05. Thus identical alarm quality gives a five-point loss atp = 0, no change atp = 0.1,
and a 35-point gain atp = 0.8. Even perfect failure prediction produces no additional successes
when p = 0, although early termination can still save cost. These are analytical controls, not
measured monitor performance. They motivate joint reporting of alarm discrimination, residual-
budget restartability, and realized utility. A global accuracy or AUROC alone omits the second
quantity.
An edit-preserving restart changes the intervention and need not satisfy the independence as-
sumption. For a general alarm, the exact identity isG = E[A(YR−YC)]. Computing it requires
outcomes for the specified recovery action. Mixing task populations can also induce dependence,
even when fresh draws are independent within each task. We therefore estimate and interpret
action values within task and runtime before aggregation.
Corollary 4.2 (Opportunity ceiling for a failure alarm)Under the assumptions of proposi-
tion 4.1, any alarm satisfies
G≤ (1−q)p. (10)
Equality is attained by a perfect alarm,A = 1−YC. The additional value of this clairvoyant alarm
over the better constant action is
(1−q)p− (p−q)+ = min{(1−q)p, q(1−p)}. (11)
Proof. In equation (8), useτ≤ 1 and ϕ≥ 0. Subtract the better constant-action gain(p−q)+
and distinguishp≥q from p<q . □
The ceiling is a value-of-perfect-information benchmark for one specified action pair. It is
neither a realizable detector nor an upper bound for state-preserving recovery, multiple restarts,
or another model. A plug-in estimate of this ceiling can diagnose an evaluation set with little
measured opportunity; it does not establish that the true opportunity is small without sampling
uncertainty.
4.2 The decision value of a richer progress signal
LetZ be a richer observation and letD(Z) =QR(Z)−QC(Z) =−∆(Z) denote restart advantage.
A coarser representation isG = g(Z). Fix the residual budget and population of live decisions.
The best policy usingG has value
V (G) = E[QC(Z)] + E [(E[D(Z)|G])+], (12)
where (x)+ = max(x, 0).
Proposition 4.3 (Value lost by compressing a progress signal)The loss from replacingZ
by G =g(Z) is
V (Z)−V (G) = 1 2{E|D(Z)|− E|E[D(Z)|G]|}≥ 0. (13)
It vanishes when each coarse observation contains advantages of only one sign, up to zero-probability
events. In particular, preserving the optimal action can preserve decision value without reconstruct-
ing the original trace.
9

Proof. Using x+ = (x +|x|)/2 in both values cancels the common mean advantage. Conditional
Jensen’s inequality proves nonnegativity. Equality in the absolute-value inequality holds exactly
when positive and negative advantages do not coexist within a conditional observation class.□
This gives a task-specific criterion for context compression: preserve distinctions that change
the preferred action. Token retention, embedding fidelity, and reconstruction quality do not by
themselves measure this loss. The identity is a binary-action specialization of classical informa-
tion comparison, not a new universal information theorem. It also permits imperfect signals to
have positive value; exact decision sufficiency is an ideal reference, not a prerequisite for practical
improvement. If acquiringZ reduces expected utility byκ while otherwise preserving the action-
value model, its net benefit isV (Z)−V (G)−κ. When acquisition consumes calls or changes the
workspace, action values must instead be evaluated at the resulting budget and state.
4.3 A finite-sample decision certificate
Let E denote explicit protocol termination. At a fixedt, a trace is eligible only if it is still live:
Lt ={T >t, E >t}. (14)
For taskj, the audited comparison is uninterrupted continuation throughB versus one clean restart
with B−t calls:
qj,t = P(T≤B|Lt,j ), p j,t = P(T≤B−t|j). (15)
The first quantity is estimated from eligible attempts; the second from all fresh attempts on that
task. A later protocol terminal counts as unsuccessful continuation. An earlier terminal is outside
the live-decision population. Neither arm extrapolates beyond the observed horizon.
For a fixed family ofM task-time comparisons, form two-sided Clopper-Pearson intervals [10]
for everyqj,t and pj,t, each with error probabilityα/(2M). Write them as[LC,UC] and [LR,UR].
An empty eligible sample receives[0, 1]. The decision audit returns
Dj,t =



restart, L R >U C,
continue, U R <L C,
abstain, otherwise.
(16)
Proposition 4.4 (Simultaneous sign certification)For IID attempts within each fixed task
and runtime, complete observation through B, and a comparison family fixed independently of
the evaluated outcomes, every nonabstaining decision in equation(16) has the correct sign with
probability at least1−α.
Proof. Each binomial interval has its stated marginal coverage, including the continuation interval
conditional on the number of eligible attempts. A union bound over the2M intervals gives simul-
taneous coverage. On that event,pj,t−qj,t∈ [LR−UC,UR−LC], so either strict separation certifies
the sign. Independence between the two estimated arms is unnecessary for the union bound; the
samples may overlap. □
This certificate implements a simple form of conservative policy improvement [11]. It is a
sufficient evidence rule, not an optimal test or an impossibility bound for all estimators. Abstention
means that this procedure does not resolve the comparison. Falling back to continuation after
abstention does not certify continuation as optimal. Deployment also requires the calibration
population to match the future runtime; the guarantee does not cover arbitrary distribution shift
or uncorrected repeated checking.
10

0.0 0.2 0.4 0.6 0.8 1.0
Continuation success q
0.0
0.2
0.4
0.6
0.8
1.0Fresh residual-budget success p
Restart improves success
Restart harms
A  Same alarm quality, different decision value
1 decision 26 cells 156 cells
0
25
50
75
100
125
150
175
200Zero-success trials required
20
35 4342
73
9086
149
184
B  Resolution cost of a boundary result
p < 20%
p < 10%
p < 5%
−50
0
50
Success change (points)
Analytical sensitivity only. A: failure TPR 0.90, FPR 0.10; no monitoring cost.
B: equal-tailed binomial bounds, family error 0.05. Counts refer to independent eligible trials.
Figure 2: Analytical controls for monitor evaluation. Panel A keeps the failure detector’s true-positive and
false-positive rates fixed while varying continuation success and restartability. The black curve is the zero-
gain boundary. Panel B gives the number of zero-success observations required by the specified simultaneous
interval procedure to bound a success probability. Neither panel reports newly collected agent performance.
Evidence cost at zero success. For n observations with zero successes, the upper endpoint
under this interval allocation is
U0(n,M ) = 1−
( α
4M
)1/n
. (17)
To obtainU0≤ϵ requires
n≥
⌈log(α/(4M))
log(1−ϵ)
⌉
. (18)
These counts describe this specified binomial procedure. They quantify the evidence needed to
bound one success probability, not sufficient sample sizes to establish an intervention effect. Con-
ditional continuation additionally requires that these observations reach the decision alive.
5 Experimental Method
5.1 Design principle
We use a sequential falsification design. Each experiment was motivated by the preceding result,
but its task rule, intervention, outcome, and stopping rule were frozen before new outcomes were
observed. Earlier data are used only where stated. This structure does not make an adaptive
research program equivalent to one preregistered confirmatory study. It does prevent within-stage
changes to the tested intervention after seeing its result.
5.2 Benchmark and runtime tuple
We use 19 issues from the SymPy repository in SWE-bench Verified [7]. Restricting to one reposi-
tory removes language and build-system variation, while retaining issue-level differences in symbolic
11

Table 2: Experimental ladder. Model attempts count actual agent or resolver executions. Patch algebra
used existing failed workspaces and no model calls.
Stage Question Attempts Frozen comparison
Initial restart Does a short cutoff beat one 30-call at-
tempt?
70 Cutoffs and universal sched-
ules
Prospective transfer Does the selected cutoff transfer to un-
seen tasks?
60 Fixed 16 versus fixed 30
Horizon extension Is completion mass hidden after call
30?
20 One 60 versus repeated 30
Context recovery Does fresh context recover protocol col-
lapse?
40 Baseline versus rejuvenation
Patch algebra Do clean unions of failed patches solve? 0 19 frozen composites
Semantic resolver Can one agent synthesize failed hy-
potheses?
4 Four bounded portfolio runs
Total 19 unique tasks, two models 194 Plus 19 verifier-only candi-
dates
mathematics, printing, assumptions, matrices, and related subsystems. It also limits external va-
lidity, which we treat explicitly in section 7.3.
An experimental runtime is identified by benchmark task, model endpoint, agent re-
lease, provider route, prompt configuration, and sampling policy. We use mini-swe-agent
2.4.6 [32]. Attempts use temperature 0.7, restore the benchmark-specified repository state
before each run, execute under WSL2 Bubblewrap isolation without network access, and expose
a workspace visible only to the attempt. The initial comparison usesopenai/gpt-5.6-luna and
deepseek/deepseek-v4-flash-0731. All subsequent model-driven experiments use the former.
The primary budget unit is a model call. Dollar cost and wall time are secondary operational
measures. A 30-call attempt need not emit 30 valid environment actions, and an explicit format
failure can end it early. We retain the distinction between nominal horizon, first verified completion,
and protocol-terminal call.
Formally, letE be the first explicit protocol-terminal call and letH be the configured horizon.
The trace records
U = min{T,E,H }, J ∈{ verified,protocol terminal,right censored}. (19)
The event labelJ matters for replay. A protocol terminal can release calls to a new episode; a
right-censored live trajectory cannot be treated as known failure beyondH.
5.3 External verification and completion time
Each selected task passes two environment gates before collection: the benchmark-provided starting
state fails the task evaluator and the reference patch passes it. The evaluator and test patch remain
outside the agent sandbox. After every environment action, the controller transfers the candidate
diff into a clean evaluator and runs the hidden fail-to-pass tests. Completion time is the first passing
state. This prevents a later destructive action or an inaccurate self-declaration from changing the
recorded time.
Every successful model attempt was audited for changes to the verifier, test runner, or hidden
tests. None modified those assets. Successful patches changed implementation files, with occasional
scratch reproductions. The analysis never exposes hidden verifier output, the reference patch, or
completion labels to the model.
12

Table 3:Runtime controls shared across model-driven experiments unless a stage states otherwise.
Component Frozen value
Benchmark SWE-bench Verified, selected sympy/sympy tasks
Agent mini-swe-agent 2.4.6
Models openai/gpt-5.6-luna;
historical comparator deepseek/deepseek-v4-flash-0731
Sampling Temperature 0.7; separate provider draws
Primary budget Model calls, with stage horizons of 12, 30, or 60
Verification External fail-to-pass evaluator after every environment action
Isolation Benchmark-specified task state, network-disabled Bubblewrap, evaluator
outside workspace
Collection dates August 31 and September 6, 2026
5.4 Restart replay
The initial cohort contains five nominally independent 30-call attempts for each of seven tasks
and two models, totaling 70 observations. We evaluate a fixed cutoffc under total budget 30
by empirical resampling of fresh attempts within task. Write30 = qc +r, withq =⌊30/c⌋ and
0≤r<c . In the absence of an earlier protocol-terminal event, the plug-in probability is
ˆPj,c(30) = 1−
(
1− ˆFj(c)
)q(
1− ˆFj(r)
)
. (20)
The exact replay additionally releases unused calls when a recorded protocol-terminal event occurs
before the assigned cutoff. Macro success averages the resulting probability across tasks. Cutoffs
range from 4 to 30 in steps of two. The full-horizon cutoff is the uninterrupted baseline. For
geometric and Luby schedules, the implementation uses Monte Carlo replay with 50,000 episode
sequences per task.
Cutoff selection is evaluated in sample and by leave-one-task-out selection. Each fold selects
the best cutoff on the other tasks, breaking ties toward the longer cutoff, then evaluates it on the
held-out task. No attempt-level split is used because attempts from one issue share task difficulty.
5.5 Prospective task cohorts
The first new cohort selects the seven highest-ID unseen SymPy tasks that pass the environment
gates. This mechanical cohort produced 35 attempts. Because all were solved early, a second
difficulty-enriched cohort targeted unseen issues labeled at least one hour, then filled rejected po-
sitions from the highest-ID unseen issues labeled 15 minutes to one hour. Five tasks passed the
gates, yielding 25 attempts. The transferred cutoff of 16 calls and the 30-call baseline were fixed
before either outcome set was observed.
The 60-call extension contains five fresh attempts on each of four stress tasks that were0/5
at horizon 30. Its primary outcome is any first completion in calls 31 through 60. A secondary
analysis separates right-censoring from explicit repeated-format termination.
5.6 Context-rejuvenation intervention
Four tasks that exhibited repeated-format termination receive five fresh baseline and five treatment
attempts each. Both conditions have a shared 60-call cap. After three consecutive invalid tool
responses, treatment preserves the exact repository state, discards the conversation, instantiates
a fresh model client, and supplies the original issue plus deterministicgit status and diff-stat
13

summaries. Itreceivesnoextracalls, hiddenfeedback, progressscore, ormodelcheckpoint. Baseline
follows the unmodified harness behavior.
The prospective expansion rule required at least a five-point success gain or two recovered
successes, with no more than a20% mean-cost increase. The rule was frozen before collection.
5.7 Failed-branch reuse
The context experiment yielded 38 externally failed, nonempty, production-code-only terminal
patches after excluding one verified patch and one empty patch. We deduplicated them by content,
enumerated unordered within-task pairs, and performed clean three-way composition against the
common benchmark starting state. Candidate generation used no model, verifier output, or gold
patch. The ranking was frozen before verification and allowed at most eight candidates per task.
Nineteen candidates were evaluated.
The semantic-resolver screen then supplied one clean 12-call Luna attempt per task with the
issue and every unique failed patch for that task, each explicitly labeled as a failed hypothesis. The
resolver could inspect and edit a clean workspace. The four contexts were frozen before execution.
The protocol allowed no retries, and a second stage would open only after at least one verified
success.
5.8 Retrospective decision-value audit
We reanalyze the 70 initial and 60 prospective 30-call attempts, without additional model calls.
These 130 observations form 26 task-model cells with five attempts each. The audit evaluates
t∈{ 4, 8, 12, 16, 20, 24} at total budgetB = 30, giving a family ofM = 156 comparisons. It uses
the live eligibility rule and binomial intervals in section 4.3, withα = 0.05. Empty live populations
are reported as not reached, not as successful abstentions. All attempt identities are deduplicated
before analysis.
The decision is a single clean restart using the residual budget, not the repeated-cutoff policy
used in the earlier replay. We report conditional action values within each task, then weight the
change by the observed fraction reaching the decision and average tasks equally. A task oracle
chooses the better estimated action separately for each task; a perfect failure alarm additionally
knowswhichlivecontinuationswillfail, asincorollary4.2. Bothareretrospectiveplug-inreferences,
not deployed policies or validated opportunity bounds. In particular, zero observed restart success
does not establish zero true restartability.
This audit was designed after inspection of the collected experiments. Its comparison family
and analysis are fully specified for reproduction, but the audit is exploratory, not preregistered or
a prospective test of the coverage guarantee. It supplies no paired state-conditioned intervention
outcomes and does not evaluate a learned prefix monitor.
5.9 Uncertainty and reporting
For policy contrasts, percentile bootstrap samples tasks with replacement and then attempts within
sampled task. Unless specified, intervals use 10,000 replicates and report the empirical2.5% and
97.5% quantiles. We report bootstrap sign probabilities as descriptive quantities, not posterior
probabilities or frequentistp values. Boundary outcomes are accompanied by an unclustered New-
combe interval as a sensitivity check where useful. All success estimates are absolute percentage-
point differences.
14

Table 4:Main empirical results. Intervals resample tasks and attempts unless noted.
Comparison Observed result Interpretation
Fixed 16 versus 30, Luna
training tasks
+2.29 points [0.00, 6.86] Weak in-sample gain
Luna-selected fixed 16 on
DeepSeek
−42.29 points
[−69.14,−17.71]
Selected scale does not transfer across
models
Fixed 16 versus 30, all 19
Luna tasks
−0.21 points [−4.21, 2.53] Pooled estimate includes initial and
prospective tasks
First completion after call 30 0/20; one-sided upper
bound 13.9%
No observed useful late tail; rare mass
remains possible
Fresh context versus baseline 0/20 versus 1/20; mean
cost +56.7%
Protocol label improves, task outcome does
not
Failed-branch reuse 0/19 composites; 0/4
resolvers
Textual diversity does not supply verified
closure
For taskj and policyπ, letθj,π(B) be the probability of external verification within total budget
B. The primary estimand is the task-macro policy value
Θπ(B) = 1 J J∑ j=1 θj,π(B), (21)
and a policy contrast is∆π,π0 = Θπ(B)−Θπ0(B). Equal task weighting prevents an issue with more
retained attempts from dominating the result. The hierarchical bootstrap targets variability over
both sampled tasks and provider draws within task. With only one repository and purposefully
selected cohorts, it should not be read as a population interval over all software engineering tasks.
Unsuccessful attempts at a horizon are right-censored: they establishT > c, notT =∞ [33].
Offline replay never evaluates a cutoff beyond the observed horizon. Explicit protocol termination
is a competing event, recorded at its observed call, and may release the residual budget to a new
attempt. Treating these terminal events as ordinary censoring would overcharge the episode and
obscure the distinction between time-based truncation and fault recovery.
6 Results
Table 4 states the principal contrasts before the stage-by-stage analysis. The paper gives priority
to frozen prospective comparisons over in-sample maxima.
6.1 A restart scale does not transfer across models
The initial 70 attempts already contain two different completion-time regimes under the same tasks
and harness. Luna solves 29 of 35 attempts, mostly early. DeepSeek solves 24 of 35, but many
completions occur after call 16. Per-task outcomes appear in table 5; the empirical completion
distributions and fixed-cutoff policy values appear in figure 3.
The best Luna cutoff spans calls 16 through 20 and reaches85.14%, compared with82.86% for
one 30-call attempt. At cutoff 16, the estimated change is+2.29 points with a task-hierarchical
interval of[0.00, 6.86] and bootstrap positive fraction0.504. This is weak in-sample evidence.
Applying the same 16-call scale to DeepSeek changes success from68.57% to 26.29%, a−42.29
point effect with interval[−69.14,−17.71]. DeepSeek’s best cutoff is the full 30 calls. The direction
15

Table 5:Initial externally verified outcomes. Call statistics are conditional on successful attempts.
Luna DeepSeek
Task Pass Calls: min/mean/max Pass Calls: min/mean/max
23413 4/5 5/7.0/9 4/5 21/23.8/27
23824 5/5 4/5.2/6 5/5 11/12.8/15
23950 0/5 none 1/5 29/29.0/29
24066 5/5 5/7.0/11 3/5 20/25.0/29
24213 5/5 4/4.6/5 5/5 13/19.8/28
24443 5/5 8/12.0/16 4/5 19/23.0/30
24661 5/5 6/7.4/9 2/5 15/22.5/30
Total 29/35 24/35
4 8 12 16 20 24 28 30
Episode cutoff c (model calls)
0
20
40
60
80
100Task-macro verified success (%)
A
82.9% Luna
22.9%
DeepSeek
Completion by call cutoff
4 8 12 16 20 24 28 30
Episode cutoff c (model calls)
B
85.1%
Luna
26.3%
DeepSeek
Luna-selected cutoff
Policy value under a 30-call budget
Restart value depends on the model-specific completion scale
Initial cohort: 7 tasks, 5 attempts per task and model. Bands are pointwise 95% task-then-attempt bootstrap intervals.
Figure 3: Model-specific completion scale and restart-policy value on the initial seven tasks. Panel A
reports the task-macro probability that one attempt has verified by callc. Panel B reports the exact plug-in
success of repeated cutoffc under 30 total calls. Shading gives pointwise 95% hierarchical bootstrap intervals.
Enlarged points mark the Luna-selected cutoff of 16 calls.
of transfer in the other direction is conservative: applying 30 calls to Luna retains82.86% and gives
up only the small in-sample oracle difference.
Leave-one-task-out selection removes the apparent Luna benefit. It yields 75.54% against
82.86% for the 30-call baseline, a−7.31 point difference. The decisive held-out task is 24443:
the other six tasks select cutoff 10, while all five successful runs of task 24443 require 8 to 16 calls
and repeated cutoff 10 has only48.8% plug-in success. DeepSeek selects 30 calls in every fold and
ties its baseline.
Finite geometric schedules reach at most approximately 84.59% on Luna and 22.88% on
DeepSeek under the preregistered family. The tested Luby schedules range from45.72% to 67.40%
on Luna and have zero success on DeepSeek because none allocates an episode long enough for
an observed completion. This is the scale sensitivity of proposition 3.3, not a contradiction of
asymptotic restart theory.
Finding. The same tasks and harness do not determine a portable restart scale. Changing only the
model moves useful completion mass beyond the selected cutoff and turns a small apparent gain into a
large loss.
16

Table 6:Transfer of the Luna-selected 16-call cutoff. The interval resamples tasks and attempts.
Cohort Tasks / attempts Fixed 16 Fixed 30 Difference and 95% interval
Initial 7 / 35 85.14% 82.86% +2.29 [0.00, 6.86]
Prospective high ID 7 / 35 100.00% 100.00% 0.00 [0.00, 0.00]
Difficulty enriched 5 / 25 0.00% 4.00% −4.00 [−16.00, 0.00]
Pooled 19 / 95 68.21% 68.42% −0.21 [−4.21, 2.53]
6.2 The in-sample gain does not survive prospective transfer
The two prospective cohorts add 60 Luna attempts. All 35 attempts in the mechanically selected
high-ID cohort pass by call 15, so both policies score100%. In the difficulty-enriched cohort, only
one of 25 attempts passes, at call 23. Fixed 16 therefore scores zero while fixed 30 scores4%.
Results are summarized in table 6.
Across all 19 Luna tasks, fixed 16 scores68.21% and fixed 30 scores68.42%. The difference is
−0.21 points with interval[−4.21, 2.53] and bootstrap positive fraction0.317. The pooled in-sample
oracle is cutoff 24 at68.84%, only 0.42 points above fixed 30. Leave-one-task-out cutoff selection
scores 67.37%, a−1.05 point difference from fixed 30.
Under total budget 60, a conservative policy of 15, 15, then a reserved 30-call attempt
scores 69.43%. Two 30-call attempts score70.11%, for a difference of−0.67 points with interval
[−2.53, 0.84]. Reserving a full episode avoids catastrophic truncation, but the short probes displace
another useful long attempt.
Finding. The positive cutoff result does not replicate prospectively. Easy tasks create no headroom,
while the only stress-cohort success occurs after the selected cutoff.
6.3 Policy differences do not certify individual restart decisions
The retrospective audit separates where a decision occurs, which action has higher estimated value,
and whether the estimate resolves its sign. Of 156 task-time cells, 103 contain at least one live
attempt; the other 53 are never reached. None of the 103 live comparisons is certified by the
simultaneous interval rule. This is a finite-sample limitation of the specified conservative procedure,
not evidence that all actions have equal value.
At the previously selected cutoff of 16, only 13 task-model cells remain live. Table 7 summarizes
the decision opportunities; figure 4 displays conditional advantages and uncertainty. Five initial
Luna tasks have completed in every attempt. Task 23413 has one survivor among five. For that
survivor, estimated continuation success is zero and fresh success within the remaining 14 calls is
4/5. Its task-macro contribution is therefore
1
7· 1 5· 4 5 = 0.022857. (22)
The remaining live Luna task, 23950, has no observed success in either arm. Thus the entire2.29-
point initial gain is supplied by one surviving failed attempt and the early successes of other draws
on that same issue. The headline effect is not evidence of a broad stagnant-trajectory phenotype.
All six live DeepSeek task cells favor continuation in the plug-in estimates. The prospective
high-ID cohort supplies no live decision at all: both policies tie because completion precedes the
alarm time. The stress cohort supplies many failures, but no observed fresh completion within
14 calls. This is a failure-rich evaluation set with little measured recovery opportunity under the
17

Table 7:Decision opportunities at call 16 with total budget 30. Changes are task-macro percentage points
relative to continuation. The oracle knows future continuation failure and uses the specified independent
clean restart. Its values are plug-in diagnostics, not statistically validated upper bounds. No live cell receives
a sign certificate.
Cohort Attempts Live Restart all Perfect alarm
Initial Luna 35 6 +2.29 +2 .29
Initial DeepSeek 35 27 −42.29 0 .00
Prospective high ID 35 0 0.00 0 .00
Prospective stress 25 25 −4.00 0 .00
chosen action. A detector cannot be usefully assessed for completion gains merely by selecting
trajectories likely to fail.
The perfect-alarm calculation in corollary 4.2 adds no estimated completion gain beyond con-
tinuation in either prospective cohort or the initial DeepSeek cohort at this decision time. This
statement is narrowly conditional on the empirical distributions, call 16, and one independent clean
restart. It does not bound a richer recovery action, a different decision time, or the true opportunity
concealed by limited sampling. Even oracle diagnostics require uncertainty assessment.
The lack of individual certificates is compatible with the large cross-model policy loss. The
earlier bootstrap measures an aggregate policy contrast across sampled tasks; the audit asks for the
sign of each conditional action comparison with simultaneous protection. Five attempts per task,
sometimes reduced to one live continuation, cannot provide comparable resolution. For example,
equation (18) requires 90 zero-success observations to reduce the specified upper bound to10%
when M = 156, versus 42 for one decision. These are procedure-specific evidence costs, not lower
bounds on every possible learning method.
Finding. Failure prevalence, decision opportunity, and statistical support are different quantities. The
same audit set can contain many failures, negligible measured recovery opportunity, and insufficient
evidence to certify any individual action.
6.4 Additional horizon reveals protocol collapse, not late success
The horizon extension tests four tasks that were previously 0/5 at 30 calls. Among 20 fresh
60-call attempts, one passes at call 17. No completion first appears during calls 31 through 60.
An unclustered one-sided 95% binomial upper bound is 13.9%. This attempt-level sensitivity
calculation does not provide population coverage over heterogeneous tasks; rare late completion
and repository-level variation remain unresolved.
Seventeen attempts end after three consecutive invalid tool responses and two exhaust the
horizon. On the same four tasks at horizon 30, only one of 20 attempts had ended in repeated-
format failure. The attempt-level Fisher exact comparison of 17/20 with 1/20 givesp = 4.06×10−7;
it is descriptive because attempts are clustered within four tasks. Fourteen of the 17 format failures
occur after call 30.
At total budget 60, repeated fixed 30 scores9% by empirical replay, compared with5% for one
60-call attempt. A policy that allows the full 60 calls but immediately recycles budget after explicit
terminal failure also scores9%. Hence the apparent restart benefit comes entirely from reusing calls
after an observable protocol terminal event. Arbitrarily censoring a live trajectory adds nothing.
18

−100 −50 0 50 100
Restart minus continuation success (percentage points)
DeepSeek / 23413  (live 5/5)
DeepSeek / 23950  (live 5/5)
DeepSeek / 24066  (live 5/5)
DeepSeek / 24213  (live 3/5)
DeepSeek / 24443  (live 5/5)
DeepSeek / 24661  (live 4/5)
Luna / 23413  (live 1/5)
Luna / 23950  (live 5/5)
Prospective stress / 16597  (live 5/5)
Prospective stress / 17630  (live 5/5)
Prospective stress / 21612  (live 5/5)
Prospective stress / 21930  (live 5/5)
Prospective stress / 22080  (live 5/5)
Decision direction is heterogeneous; every interval includes zero
One decision at call 16, total budget 30. Simultaneous 95% bounds across 156 cells.
Dots are retrospective estimates. No state-conditioned monitor or live restart was tested.
Figure 4: Conditional restart advantage in the 13 task-model cells with a live attempt at call 16. Dots
are plug-in estimates. Lines are simultaneous difference bounds formed from binomial intervals across all
156 audited comparisons. Positive values favor restarting. Every interval includes zero despite substantial
heterogeneity in point estimates.
Finding. More nominal horizon increases exposure to protocol failure but reveals no observed late
completion. Recycling budget after an explicit failure is distinct from declaring a still-running trajectory
stagnant.
6.5 Fresh context changes the terminal label, not success
The context intervention fires in 18 of 20 treated attempts. Baseline solves one of 20; treatment
solves none. The task-clustered bootstrap difference is−5 points with empirical range [−20, 0].
Since treatment has no successes, this range is boundary-degenerate and cannot represent a positive
treatment event. An unclustered Newcombe sensitivity interval is[−23.6, 15.2] points.
The treatment does eliminate the finalRepeatedFormatError label. Every triggered attempt
instead consumes its remaining calls, and all 20 treated attempts end atLimitsExceeded. Mean
dollar cost rises from $0.03786 to $0.05934, a56.7% increase. Mean wall time rises from 309.5 to
512.8 seconds, a65.7% increase. Figure 5 displays the failure-mode substitution.
Thefrozenexpansioncriterionisnotmet. Freshinferencecontextremovestheterminalinterface
symptom but preserves the workspace, including potentially wrong edits. The tested reset does not
support conversational contamination as a sufficient explanation for recoverable failure. It does not
isolate which retained edits or other mechanisms caused the remaining failures.
Finding. An intervention can improve a harness diagnostic by 90 points while leaving success no better
and making cost materially worse. Failure-mode movement is not task progress.
19

Table 8:Fresh 60-call outcomes on tasks previously unsolved in five 30-call attempts.
Task Pass First pass Format fail Limit Mean cost
16597 0/5 none 4 1 $0.05716
17630 0/5 none 5 0 $0.03577
21612 1/5 call 17 4 0 $0.03126
21930 0/5 none 4 1 $0.04996
Total 1/20 no pass after 30 17 2
Baseline Fresh context
0
20
40
60
80
100Attempts (%)
1 (5%)
18 (90%)
1 (5%)
20 (100%)
A Terminal outcome distribution
1.0 1.2 1.4 1.6 1.8
Fresh-context / baseline ratio
Mean metered cost
Mean wall time
1.57x
1.66x
B Resource use relative to baseline
Fresh context substitutes the failure mode without recovering success
Prospective intervention: 20 attempts per condition under a shared 60-call budget.
Verified Format terminal Limit terminal
Figure 5: Context rejuvenation changes the observed failure mode without improving task success. Panel
A shows terminal outcomes, with counts and within-condition percentages. Panel B shows the corresponding
increase in mean metered cost and wall time relative to baseline.
6.6 Failed branches are diverse but not compositional
The 40-run context experiment yields 38 admissible failed sources and 37 unique patch contents.
Of 162 unordered source pairs, 51 form clean, novel three-way composites. The frozen verifier-blind
ranking selects 19. None passes. Task 17630 produces no clean novel composite because branches
edit the same matrix-code region incompatibly.
One bounded semantic resolver is then run per task. It receives every unique failed patch as
an explicitly failed hypothesis and starts from a clean workspace. All four runs use the 12-call cap
and fail verification. The patches are not copies: their maximum character-level diff similarity to
any supplied parent is 0.563, 0.700, 0.645, and 0.802. The task-level relevant tests pass in counts
76/79, 21/22, 99/100, and 47/52, but the protocol forbids extending the near miss after outcome
inspection.
The historical clean-context cohort also has no completion within 12 calls on these tasks, so
the resolver screen provides no evidence of improvement and is not treated as a randomized effect
estimate. The null result has a more focused interpretation: syntactic novelty and access to multiple
failed views are insufficient evidence of independent corrective information.
Finding. Failed branches occupy different textual locations without supplying a verified closure opera-
tion. Clean union and shared-model synthesis both preserve diversity without establishing correctness.
20

Table 9:Context-rejuvenation outcomes under the shared 60-call budget.
Outcome Baseline Rejuvenation Treatment difference
Verified success 5.0% 0.0% −5.0 points
Repeated-format terminal 90.0% 0.0% −90.0 points
Limit terminal 5.0% 100.0% +95.0 points
Mean cost $0.03786 $0.05934 +$0.02148
Mean wall time 309.5 s 512.8 s +203.3 s
Table 10:Verifier-blind patch composition from failed terminal branches.
Task Sources Unique Pairs Clean novel Evaluated Pass
16597 10 9 45 35 8 0
17630 10 10 45 0 0 0
21612 9 9 36 13 8 0
21930 9 9 36 3 3 0
Total 38 37 162 51 19 0
7 Discussion
7.1 Contribution and scope
The contribution is an operational account of when progress information can improve a specified
agent-control decision. Classical restart optimization already allows informative observations, and
contemporary learned monitors demonstrate successful termination and recovery. Our results do
not overturn those findings. They connect failure discrimination to residual-budget restartability,
distinguish decision-preserving compression from trace reconstruction, and expose the sampling
support of per-task action comparisons.
Three levels of evidence must remain separate. The mathematical identities hold under stated
assumptions and specialize established decision theory. The retrospective audit diagnoses the col-
lected traces and supplies a reusable calculation, but does not demonstrate a deployed policy gain.
The prospective intervention screens establish outcomes of particular controllers on selected tasks,
not universal limits on monitoring or recovery. Combining these levels makes the paper useful only
if their inferential boundaries are preserved.
7.2 Implications for evaluation and deployment
Measure opportunity before monitor quality.A failure detector should be evaluated where
an alternative action can plausibly recover value. A ceiling cohort offers no live decisions; a hard
cohort can offer many failures but little residual-budget restartability. The perfect-alarm reference
in corollary 4.2 is a diagnostic for this distinction. A small plug-in ceiling warrants additional
evidence or a different intervention, not a conclusion that every progress signal is useless.
Match the signal to the action. A clean restart, conversational reset with mandatory
workspace retention, and optional reuse of previous edits define different potential outcomes. Their
action values cannot be interchanged. FailFast-RestartSmart [5], for example, evaluates a learned
monitor with a recovery mechanism not tested here. Its positive results and our negative timeout
screens can both hold. A meaningful comparison must fix reset semantics, residual budget, verifier,
and monitoring cost.
21

1
Restart scale
Early completion
mass
No transfer
2
Long horizon
Useful late
mass
No pass after 30
3
Fresh context
Conversation
binding
0 of 20 pass
4
Patch algebra
Partial solutions
compose
0 of 19 pass
5
Resolver
Independent views
complement
0 of 4 pass
Five bounded tests of restart and recovery
Observed outcomes distinguish protocol changes from verified completion.
Figure 6: Five bounded tests of restart and recovery. Outcomes identify limitations of the tested inter-
ventions, not impossibility results for richer controllers. The task populations and uncertainty differ across
stages.
Preserve decision distinctions, not every token.The information-value identity gives a pre-
cise connection to context compression. A representation can discard large parts of a trace without
losing control value if the discarded distinctions do not reverse the preferred action. Conversely,
faithful reconstruction can preserve many irrelevant details. This is a criterion for future evaluation,
not evidence that our study has built a superior compressor.
Make abstention explicit. The released audit returns an action only when its specified intervals
separate. Otherwise it reports insufficient evidence. This is useful as a calibration check before
enabling an automatic restart rule; it is not a claim that continuation is optimal whenever the
audit abstains. The present five-run cells are too sparse for this conservative task-specific rule.
Hierarchical pooling could improve efficiency, but would introduce assumptions that require held-
out validation.
Separate protocol repair from task recovery.Observable termination is not a live stagnation
decision. Recycling its unused calls recovers budget in our replay. Replacing its final error label
without changing verified completion is a different result. The context intervention illustrates why
dashboards should report final task outcomes and cost alongside protocol diagnostics. Likewise,
failed-patch diversity alone does not establish that a particular composition or synthesis operator
can recover a solution. We do not estimate error correlation or identify the causal source of the
unsuccessful combinations.
7.3 Limitations
All 19 tasks are selected SymPy issues. The cohort construction deliberately mixes a pilot, a
mechanical high-ID selection, and difficulty enrichment; pooled rates do not estimate performance
over SWE-bench Verified or agent workloads generally. Later interventions use one model and one
compact harness. Two models on seven shared tasks demonstrate heterogeneity, not broad model
coverage.
Five attempts per task leave substantial uncertainty, particularly after conditioning on live
22

survival. The zero-success treatment and reuse screens do not exclude modest benefits in other
populations. The unclustered late-tail calculation is a sensitivity result, not a task-population
confidence statement. The retrospective decision family was chosen after the original experiments
and is not a prospective validation of the certification rule.
The analysis assumes exchangeable independent provider draws within each fixed task and
runtime. Shared routing, temporal drift, or correlated restarts can invalidate that approximation.
The binomial certificate does not transfer across arbitrary changes in the task distribution, prompt,
harness, provider, or recovery action. It also provides no protection for uncorrected adaptive
monitoring.
The binary verifier measures a finite fail-to-pass specification, not every aspect of issue correct-
ness. Base-fail/reference-pass gating and successful-patch audits reduce implementation threats
but cannot eliminate specification gaps. Per-action external evaluation supplies completion la-
bels unavailable to a typical production controller. Its computational overhead is not part of the
model-call budget; reported model costs are not end-to-end deployment costs.
Finally, we have no matched prefix-conditioned continuation and restart trials for a learned
signal. The empirical audit uses task identity and elapsed calls, not rich trace features. It cannot
measure the decision value of embeddings, learned monitors, or semantic summaries. The infor-
mation and opportunity identities describe what such experiments should estimate; they do not
substitute for them.
7.4 A focused next test
The next decisive experiment should evaluate one existing monitor under the same recovery seman-
tics as a simple baseline, rather than add another timeout family. First, use independent calibration
data to identify tasks with both live failures and nontrivial residual-budget recovery. Freeze the
monitor, threshold, budget, and clean-reset or edit-reuse rule. On held-out tasks, compare contin-
uation, a calibrated fixed-time rule, and the monitor-triggered intervention, charging monitoring
and recovery overhead to the same budget. Report opportunity, calibration, action-value regret,
success, and cost separately.
A second model or repository is necessary to test transfer; more draws on the existing four hard
tasks cannot establish it. Such a study would convert the current measurement contribution into
evidence for a deployable control method. It is deliberately distinct from the present offline audit
and should not be described as completed.
8 Conclusion
Failure prediction is useful for agent control only through the value of the action it triggers. For
an independent clean restart, that value depends jointly on alarm errors and success within the
residual budget. Classical information comparison yields a decision-oriented criterion for retaining
or compressing progress observations, while exact binomial intervals expose when a per-task action
preference lacks statistical support.
Across 194 model executions and 19 verifier-only composites, simple restart and recovery in-
terventions show strong runtime dependence and no prospective replication of the initial cutoff
gain. A new audit of 130 existing traces finds 103 live task-time comparisons but no sign certificate
under its simultaneous rule. These findings motivate an evaluation standard: declare the inter-
vention, measure recovery opportunity, account for monitoring cost, and report uncertainty at the
level where decisions are made.RestartLabprovides the accompanying trace analysis and audit
implementation; broader prospective validation remains necessary.
23

References
[1] Henry Kautz, Eric Horvitz, Yongshao Ruan, Carla Gomes, and Bart Selman. Dynamic restart
policies. InProceedings of the AAAI Conference on Artificial Intelligence, pages 674-681, 2002.
URL https://www.cs.cornell.edu/gomes/pdf/2002_kautz_aaai_iaai_dynamic.pdf.
[2] Matthew Streeter, Daniel Golovin, and Stephen F. Smith. Restart schedules for ensembles of
problem instances. In Proceedings of the AAAI Conference on Artificial Intelligence, pages
1204-1210, 2007. URL https://cdn.aaai.org/AAAI/2007/AAAI07-191.pdf.
[3] Matthew Streeter. Bayes optimal early stopping policies for black-box optimization.arXiv
preprint arXiv:1902.08285, 2019. URL https://arxiv.org/abs/1902.08285.
[4] Yaoqi Guo, Ying Xiao, Jie M. Zhang, Mark Harman, Yiling Lou, Yang Liu, and Zhenpeng
Chen. EET: Experience-driven early termination for cost-efficient software engineering agents.
arXiv preprint arXiv:2601.05777, 2026. URL https://arxiv.org/abs/2601.05777.
[5] Chenyu Wang, Yunbo Lyu, Junda He, Zhou Yang, Chenxing Zhong, Yaniv Harel, and David
Lo. Fail-fast, restart-smart: Early failure prediction and restart for SWE agentic tasks.arXiv
preprint arXiv:2608.03222, 2026. URL https://arxiv.org/abs/2608.03222.
[6] David Blackwell. Equivalent comparisons of experiments.The Annals of Mathematical Statis-
tics, 24(2):265-272, 1953. doi: 10.1214/aoms/1177729032.
[7] Carlos E. Jimenez, John Yang, Alexander Wettig, Shunyu Yao, Kexin Pei, Ofir Press, and
Karthik Narasimhan. SWE-bench: Can language models resolve real-world GitHub issues? In
International Conference on Learning Representations, 2024. URLhttps://arxiv.org/abs/
2310.06770.
[8] John Yang, Carlos E. Jimenez, Alexander Wettig, Kilian Lieret, Shunyu Yao, Karthik
Narasimhan, and Ofir Press. SWE-agent: Agent-computer interfaces enable automated
software engineering. In Advances in Neural Information Processing Systems, 2024. URL
https://arxiv.org/abs/2405.15793.
[9] Michael Luby, Alistair Sinclair, and David Zuckerman. Optimal speedup of Las Vegas al-
gorithms. Information Processing Letters, 47(4):173-180, 1993. doi: 10.1016/0020-0190(93)
90029-9.
[10] C. J. Clopper and E. S. Pearson. The use of confidence or fiducial limits illustrated in the case
of the binomial.Biometrika, 26(4):404-413, 1934. doi: 10.1093/biomet/26.4.404.
[11] Romain Laroche, Paul Trichelair, and Remi Tachet des Combes. Safe policy improvement with
baseline bootstrapping. InProceedings of the International Conference on Machine Learning,
pages 3652-3661, 2019. URLhttps://proceedings.mlr.press/v97/laroche19a.html.
[12] Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc V. Le, Ed H. Chi, Sharan Narang,
Aakanksha Chowdhery, and Denny Zhou. Self-consistency improves chain of thought rea-
soning in language models. In International Conference on Learning Representations, 2023.
URL https://arxiv.org/abs/2203.11171.
[13] Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, and
KarthikNarasimhan. Treeofthoughts: Deliberateproblemsolvingwithlargelanguagemodels.
24

In Advances in Neural Information Processing Systems, 2023. URLhttps://arxiv.org/abs/
2305.10601.
[14] Yangzhen Wu, Zhiqing Sun, Shanda Li, Sean Welleck, and Yiming Yang. Inference scaling
laws: An empirical analysis of compute-optimal inference for problem-solving with language
models. arXiv preprint arXiv:2408.00724, 2024. URLhttps://arxiv.org/abs/2408.00724.
[15] Junlin Wang, Jue Wang, Ben Athiwaratkun, Ce Zhang, and James Zou. Mixture-of-agents
enhances large language model capabilities. arXiv preprint arXiv:2406.04692, 2024. URL
https://arxiv.org/abs/2406.04692.
[16] Thomas G. Dietterich. Ensemble methods in machine learning. InMultiple Classifier Systems,
pages 1-15. Springer, 2000. doi: 10.1007/3-540-45014-9_1.
[17] Gavin Brown, Jeremy Wyatt, Rachel Harris, and Xin Yao. Diversity creation methods: A
survey and categorisation.Information Fusion, 6(1):5-20, 2005. doi: 10.1016/j.inffus.2004.04.
004.
[18] Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe,
Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Sean Welleck, Bodhisattwa Prasad
Majumder, Shashank Gupta, Amir Yazdanbakhsh, and Peter Clark. Self-refine: Iterative
refinement with self-feedback. InAdvances in Neural Information Processing Systems, 2023.
URL https://arxiv.org/abs/2303.17651.
[19] Noah Shinn, Federico Cassano, Ashwin Gopinath, Karthik Narasimhan, and Shunyu Yao.
Reflexion: Language agents with verbal reinforcement learning. InAdvances in Neural Infor-
mation Processing Systems, 2023. URL https://arxiv.org/abs/2303.11366.
[20] Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying
Song, and Denny Zhou. Large language models cannot self-correct reasoning yet. InInterna-
tional Conference on Learning Representations, 2024. URL https://arxiv.org/abs/2310.
01798.
[21] Chang Ma, Junlei Zhang, Zhihao Zhu, Cheng Yang, Yujiu Yang, Yaohui Jin, Zhenzhong Lan,
Lingpeng Kong, and Junxian He. AgentBoard: An analytical evaluation board of multi-turn
LLM agents. In Advances in Neural Information Processing Systems, 2024. URL https:
//arxiv.org/abs/2401.13178.
[22] Hyundoo Park and Byungho Choi. When do agent loops mistake stagnation for progress? self-
evaluation bias and externally grounded verification in long-running autonomous LLM agent
loops. arXiv preprint arXiv:2607.25152, 2026. URL https://arxiv.org/abs/2607.25152.
[23] Sahil Shrivastava. Semantic early-stopping for iterative LLM agent loops. arXiv preprint
arXiv:2606.27009, 2026. URL https://arxiv.org/abs/2606.27009.
[24] Nicolas Tacheny. Geometric dynamics of agentic loops in large language models.arXiv preprint
arXiv:2512.10350, 2026. URL https://arxiv.org/abs/2512.10350.
[25] Qijun Han, Haoqin Tu, Zijun Wang, Haoyue Dai, Yiyang Zhou, Nancy Lau, Alvaro A. Carde-
nas, Yuhui Xu, Ran Xu, Caiming Xiong, Zeyu Zheng, Huaxiu Yao, Yuyin Zhou, and Cihang
Xie. VLAA-GUI: Knowing when to stop, recover, and search, a modular framework for GUI
automation. arXiv preprint arXiv:2604.21375, 2026. URL https://arxiv.org/abs/2604.
21375.
25

[26] Shukai Liu, Jian Yang, Bo Jiang, Yizhi Li, Jinyang Guo, Xianglong Liu, and Bryan Dai.
Context as a tool: Context management for long-horizon SWE-agents. arXiv preprint
arXiv:2512.22087, 2025. URL https://arxiv.org/abs/2512.22087.
[27] Lu Yi, Runlin Lei, Liuyi Yao, Yuexiang Xie, Yuyang Li, Wenhao Zhang, Zhewei Wei, Yaliang
Li, and Jian-Yun Nie. Learning agent-compatible context management for long-horizon tasks.
arXiv preprint arXiv:2605.30785, 2026. URL https://arxiv.org/abs/2605.30785.
[28] Xiaochuan Li, Ryan Ming, Meng Chu, Shuai Shao, Rong Jin, and Chenyan Xiong. ACM:
Agentic context management for long horizon tasks.arXiv preprint arXiv:2607.23809, 2026.
URL https://arxiv.org/abs/2607.23809.
[29] Sayash Kapoor, Benedikt Stroebl, Zachary S. Siegel, Nitya Nadgir, and Arvind Narayanan. AI
agents that matter.arXiv preprint arXiv:2407.01502, 2024. URL https://arxiv.org/abs/
2407.01502.
[30] You Wang, Michael Pradel, and Zhongxin Liu. Are “solved issues” in SWE-bench really
solved correctly? an empirical study. arXiv preprint arXiv:2503.15223, 2025. URL https:
//arxiv.org/abs/2503.15223.
[31] Leslie Pack Kaelbling, Michael L. Littman, and Anthony R. Cassandra. Planning and acting
in partially observable stochastic domains.Artificial Intelligence, 101(1-2):99-134, 1998. doi:
10.1016/S0004-3702(98)00023-X.
[32] SWE-agent contributors. mini-swe-agent: The 100-line AI agent that solves GitHub is-
sues. GitHub repository, version 2.4.6, 2026. URL https://github.com/SWE-agent/
mini-swe-agent.
[33] John D. Kalbfleisch and Ross L. Prentice. The Statistical Analysis of Failure Time Data.
Wiley, second edition, 2002. doi: 10.1002/9781118032985.
A Notation
Table 11:Principal notation.
Symbol Meaning
Xt Latent agent and environment state after callt
Ot,Ft Observation at callt and the observable history filtration
T First call whose resulting state passes the external verifier
E, H Explicit protocol-terminal time and configured attempt horizon
B, b Total policy budget and residual budget
F (t), λt Completion-time CDF and discrete completion hazard
Qa(h,b ) Conditional utility of actiona after historyh with residual budgetb
∆(h,b ) Continuation advantage over restart
Gt Observable candidate progress representation
meff Effective number of independent views in a correlated ensemble
26

Table 12:Task IDs by cohort. IDs omit the commonsympy__sympy- prefix.
Cohort Task IDs
Initial 23413, 23824, 23950, 24066, 24213, 24443, 24661
Prospective high ID 22456, 22714, 22914, 23262, 23534, 24539, 24562
Difficulty enriched 16597, 17630, 21612, 21930, 22080
Horizon 60 16597, 17630, 21612, 21930
Context A/B 16597, 17630, 21612, 21930
Patch and resolver 16597, 17630, 21612, 21930
B Task Cohorts and Frozen Decisions
The task sets overlap across stages by design. Counts of 19 unique tasks and 194 model attempts
deduplicate task identity but not fresh executions. The total consists of 70 initial attempts, 60
prospective attempts, 20 horizon-extension attempts, 40 context A/B attempts, and four semantic-
resolver attempts. The patch-algebra stage adds 19 external verifier calls on composed candidates
but no model attempt.
C Policy Definitions
Single. Run one attempt up to budgetB, stopping at first external pass or explicit terminal
failure.
Fixed c. Run independent attempts with per-episode capc until the total budget is spent. An
explicit terminal failure releases unused episode budget.
Geometric. Allocate episode caps in a frozen geometric sequence, truncated by the remaining
total budget.
Luby. Allocate episode caps according to a scaled prefix of the universal sequence in Luby et al.
[9], truncated by the remaining total budget.
Horizon insurance. At budget 60, allocate two 15-call probes followed by one reserved 30-call
episode. Compare with two 30-call episodes.
The fixed-policy plug-in estimate treats the five empirical attempts for each task as an IID
distribution. For a sequence of episode caps(c1,...,c k) and empirical CDF ˆFj, the task success
probability under independent resampling is
1−
k∏
i=1
(
1− ˆFj(ci)
)
. (23)
Monte Carlo replay is used in the implementation when terminal failures create episode-dependent
residual budgets.
D Additional Operational Results
Costs are provider-metered values recorded in the traces. They are not estimates of deployment
expense. The large cost and latency change in context rejuvenation arises because treatment
consumes all 60 calls after replacing an early terminal format failure with a fresh episode.
27

Table 13: Collection cost and accumulated wall time. Wall time sums parallelizable attempts and is not
elapsed study duration.
Stage Attempts Metered cost Wall hours
Initial Luna 35 $0.38327 0.771
Initial DeepSeek 35 $0.38023 3.644
Prospective Luna 60 $1.14379 2.596
Horizon 60 20 $0.87077 2.207
Context A/B 40 $1.94403 4.568
Semantic resolver 4 $0.05132 0.145
Total 194 $4.77341 13.931
E Artifact Manifest
The accompanying analysis package contains the following sanitized artifacts. They exclude
prompts, trajectories, local paths, hidden verifier output, reference patches, and credentials.
Table 14:Accompanying analysis artifacts and their role in the study.
Artifact cohort Scope Primary use
Initial paired-model cohort 70 attempts, 7 tasks Completion curves and restart replay
Prospective transfer cohorts 60 attempts, 12 tasks Out-of-sample cutoff transfer
Horizon extension 20 attempts, 4 tasks Late completion and protocol termination
Context intervention trial 40 attempts, 4 tasks Terminal outcomes, cost, and latency
Patch-composition screen 19 verifier-only candidates Failed-branch compositionality
Semantic resolver screen 4 attempts, 4 tasks Semantic aggregation
Decision audit 156 derived cells from 130
existing attempts
Actionvalues, eligibility, andsimultaneous
bounds
The package also contains stage protocols, the frozen composition plan, agent adapters, replay
policies, analysis code, command-line tools, and tests. The sanitized artifacts reproduce the re-
ported trace analyses and figures offline; new agent collection requires a model credential. Derived
audit cells reuse earlier attempts and do not increase the count of model executions.
F Threats to Interpretation
Task selection. The first seven tasks were an operational pilot, the prospective high-ID cohort
used a mechanical order, and the stress cohort deliberately enriched difficulty. Pooled rates are
descriptive for these tasks, not prevalence estimates for SWE-bench Verified.
Verifier granularity. Verification after every environment action yields precise first-pass timing,
but the fail-to-pass suite is still a finite specification. We report verifier success rather than semantic
issue resolution and retain the standard benchmark terminology only when naming the dataset.
Adaptive sequence. Later stages were chosen after earlier results. Each stage has its own frozen
protocol, but cross-stage narratives can still invite hindsight. The ladder table therefore states the
question and comparison at each stage, and null follow-ups are retained rather than omitted.
Multiplicity. The study evaluates several policies and mechanisms. The stage-level bootstrap
intervals are not adjusted for simultaneous coverage. Only the decision-audit intervals use the
28

explicit family allocation in section 4.3. We avoid claiming significance for exploratory maxima,
identify in-sample oracles as nondeployable, and give priority to prospective contrasts.
Model identity. Hosted behavior can change under a stable model identifier. Requested model
ID and collection date therefore define, but do not fully identify, the runtime used for calibration.
G Failure-Conditioned Branches: Supporting Examples
Branching is often proposed when continuation is uncertain. Its benefit depends on the epistemic
relation among branches, not their textual distance. Conditioning all inputs to an ensemble on
terminal failure can also reverse component reliability.
Lemma G.1 (Failure-conditioned component inversion)LetY ∼ Bernoulli(q) indicate that
one component of a patch is correct, withq >1/2. LetZ∼ Bernoulli(r) indicate that the remaining
requirements are correct, independent ofY, and let full success beS =YZ . Then
P(Y = 1|S = 0) = q(1−r) 1−qr < 1 2 (24)
whenever r> (2q− 1)/q.
Proof. Bayes’ rule gives the displayed conditional probability. Comparing it with 1/2 yields
2q(1−r)< 1−qr, which is equivalent tor> (2q− 1)/q. □
Thus a component that is reliable in the unconditional branch population can become minority-
reliable after selecting only failed full patches. The lemma is an existence result, not an estimate
of our patch population.
Correlation supplies a second limit. LetY1,...,Y m be exchangeable correctness indicators with
mean q and common pairwise correlationρ. Then
Var
(
1
m
m∑
i=1
Yi
)
= q(1−q) m [1 + (m− 1)ρ]. (25)
The variance is that of only
meff = m 1 + (m− 1)ρ (26)
independent views. If ρ = 1, increasing the number of branches does not reduce uncertainty at
all. This standard ensemble effect [16, 17] motivates our distinction betweenbehavioral diversity,
such as different files or diffs, andepistemic independence, meaning error diversity sufficient for
aggregation. Branches from one model and harness can satisfy the former while failing the latter.
29
