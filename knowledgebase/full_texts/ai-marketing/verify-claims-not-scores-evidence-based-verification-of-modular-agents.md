---
title: 'Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents'
url: https://arxiv.org/abs/2610.01348
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Ali Atiah Alzahrani
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.01348
pages: 32
chars: 124705
fetched_at: '2026-11-08T13:24:42+00:00'
kb_version: 1
---

# Verify Claims, Not Scores: Evidence-Based Verification of Modular Agents

Verify Claims, Not Scores:
Evidence-Based Verification of Modular Agents
Ali Atiah Alzahrani†
Abstract
When developers change one component of an agent, such as its controller, a learned
model or its verifier, they usually judge the change by an aggregate task score. That
score cannot tell whether improvement was attainable, which component lost value,
or what the agent’s own checks certify. We introduce aclaim-specific verification
auditfor modular agents that plan, act, check and refine. Instead of scoring the
agent, the audit scores theevidence: each conclusion is recorded with the evidence
behind it, one of four verdicts (supported, unsupported, unresolved or not evaluated)
and the boundary within which it holds. Three tools supply that evidence. Oracle
policies measure attainable improvement under an explicitly stated action set, so
that a low value can be traced to the evaluation rather than to the environment.
Replacing one component at a time with a perfect counterpart locates lost value,
with null results read as unresolved whenever a downstream component could mask
them. A separate test asks whether the verifier’s score identifies the quantity it is
read as bounding. Applied to a constrained portfolio-allocation agent in a synthetic
market with known hidden regimes, the audit shows that the value of perfect regime
information depends on the action set used to measure it, that the scenario generator
discards most of the regime signal while better local fidelity does not improve
decisions, and that the runtime verifier can be bypassed with no visible change
in outcomes. The contribution is the protocol and the evidential distinctions it
enforces; the empirical findings are specific to the agent and environment studied.
1 Introduction
Agent systems are usually improved by changing one component, such as the controller, a tool, a
memory, a learned model or a verifier, and then comparing an aggregate task score before and after
(5, 4). How much such a score can establish is widely questioned. Benchmark scores often stand in
for broader constructs than they measure (1, 2), agent evaluation harnesses contain errors that change
conclusions (6, 7), and small differences are often indistinguishable from seed variation (3). We ask
a narrower question: given a change to one component, what evidence wouldverifythat it helped,
locatewhere value was lost if it did not, anddelimitwhat each verification signal can support?
An aggregate comparison is uninformative in at least three situations, each documented in a separate
literature:
• The evaluation cannot express the improvement.The value of information depends on the
actions available to exploit it (21), so an evaluation with a restricted action set can report little
headroom where much exists.
• A downstream component masks an upstream one.A model can improve its own fidelity
metric without improving the decisions it feeds (41, 40), and a better upstream module changes
nothing if a downstream module ignores its output.
†Corresponding author: aliatiah100@gmail.com. The views expressed are those of the author and do not reflect the
views of any other individual or entity. This material is for research purposes only and does not constitute investment advice.
Preprint.
arXiv:2610.01348v1  [cs.AI]  1 Oct 2026

• The verifier does not measure what it certifies.A score may not identify the target quantity (29),
optimising against a proxy check can satisfy it without the intended property (9, 10), and agents
that re-sample until a check passes are selecting on the check (67, 66).
In each case the score is consistent with several incompatible explanations. Telling them apart
requires the true hidden state, the best decision attainable given that state, and the ability to replace a
component with a perfect version of itself. We therefore work in a controlled setting that provides all
three: a synthetic market with recorded hidden regimes, in which an agent allocates a portfolio under
explicit constraints. The agent contains no language model, and our claims concern modular decision
agents of this kind, although the questions the audit asks are not specific to finance.
Approach and what is new.We propose aclaim-specific verification audit. Its individual tools
(oracle policies, component replacement, factorial attribution, conformal calibration) are established.
What is new is the object being verified: not the agent’s score, but eachverification claim, recorded
as claim, evidence, verdict and boundary. Making the claim the unit of verification has three
consequences that, to our knowledge, have not been made explicit together for agent development:
1. Headroom is a property of the harness.Measuring oracle value at fixed information across a
lattice of action sets turns a null result into a testable statement about the evaluation, which we
callverifier expressiveness, rather than a statement about the environment (§4.2).
2. Null interventions are non-identifying by default.Component replacements are read as
recovery, not ablation: a positive result localises an observed bottleneck, whereas a null result is
recorded asunresolvedwhenever a downstream module could mask it (§4.3).
3. The verifier is itself a verification target.The audit separates sampling error, model misspecifi-
cation andscore identification, meaning whether a check measures what it is read as bounding,
and keeps decision quality, calibration, admissibility and provenance as distinct claims (§4.4).
This exposes a failure that neither outcome metrics nor feasibility and provenance records detect
(§6).
Case study.The system under audit, ARC-AGENT, is a reference agent that we built for this study.
It is the object of the audit rather than a proposed allocation method, and we make no performance
claim for it (§3; App. P). The audit finds that:
• perfect regime information has a small, statistically unresolved value under a two-portfolio
evaluation and a clearly positive value under regime-specific weights (§5.1);
• the scenario generator keeps less than a third of the regime signal it receives, and improving its
local fidelity does not detectably improve decisions (§5.2, §5.3);
• a joint repair of two generator outputs helps, while their interaction remains unresolved (§5.4);
• bypassing the runtime verifier voids the decision-quality claim with no visible effect on outcomes
(§6).
2 Related work
Evaluating agents versus verifying a change.Benchmarking performance, verifying that apartic-
ularchange helped, and diagnosingwhyvalue was lost are different activities; an aggregate score
mainly serves the first (5, 4). Construct-validity accounts ask what an operationalisation measures
(1, 2); we ask the same of adiagnosticprotocol. Related work repairs evaluation harnesses ( 6, 7),
measures gaps between visible and held-out checks (8), studies reward hacking (9, 10), and monitors
agents at runtime (13, 11). Because seed counts and pairing decide which conclusions survive (3),
every result here states its seeds, pairing and status (Table 14).
Uncertainty a verification signal can address.Separating uncertainty that more data can reduce
from uncertainty it cannot is standard (15, 16), and imprecise-probability and partial-identification
traditions (20, 19, 18) formalise the set-valued claims our verdicts take. Distribution-free methods
(64, 42, 32) control sampling error and theconsequencesof misspecification; we add the prior
question of whether a scoreidentifiesthe quantity it is read as bounding (§4.4).
Established tools, a new object.The value of information depends on the actions that can use it
(21), and decision-focused learning shows that fidelity and decision quality come apart (41, 40, 30).
2

Table 1:What each practice is typically designed to establish.Entries describe the usual focus
of a family of methods, not the limits of every work within it. ✓: addressed by design; “partly”:
addressed for a specific case; –: not the focus.
Practice Question it answers
Null traced
to harness
Masking-aware
localisation
Quality / admiss. /
provenance kept apart
Verifier score
identification
Aggregate benchmarking How well does the agent do? – – – –
Harness auditing Is the grader correct? partly – – –
Component ablation How much does removal hurt? – – – –
Runtime verification Does a run meet a spec? – – partly –
Decision-focused learning Does fidelity serve decisions? – partly – –
Claim-specific audit Which claims does the evidence
support?
✓ ✓ ✓ ✓
Oracles, component replacement, factorial designs and Shapley attribution (26, 27) are all established,
and our information–action lattice is elementary as mathematics. Table 1 summarises what we add: a
protocol that binds each tool to a named claim, an identification assumption, a verdict and a boundary.
3 The system and environment under audit
Before presenting the audit, we describe the concrete system it is applied to. Every component and
signal referred to later is introduced here.
Environment.We use U3, a synthetic benchmark (App. N). Ten assets, three of them defensive,
have daily returns whose distribution depends on a hidden marketregime: bull, stagnation or crisis.
The regime switches according to a Markov chain. Crises are rare (about5%of days), last about45
trading days on average, and are fat-tailed, with risky assets falling together. Because the simulator
records the true regime, three things become possible that are impossible on historical data: regime
inference can be scored directly, policies that know the regime can be computed exactly, and any
component can be replaced by an exact counterpart. U3 is verification infrastructure, not evidence
about financial markets. Each run (seed) simulates a 756-day warm-up followed by 69 monthly
decisions, with all estimation strictly walk-forward.
Decision problem and metric.At each rebalance t the agent chooses weights wt that are long-only
and fully invested (thebudget), lie in a per-assetbox [0,0.25] , and move at most 0.20 in ℓ1 norm
from wt−1 (theturnover cap), with 8 bps costs. The metric is the Sharpe ratio, mean return divided
by volatility. Because Sharpe can be bought with deeper drawdowns, we compare at matched risk
where possible, against astatic frontier: the best Sharpe of fixed equal-weight/minimum-variance
blends at the same maximum drawdown (MaxDD).
The agent under audit.ARC-AGENTmakes each decision in five steps (Fig. 1):
1. aregime detector, a hidden Markov model (HMM), outputs a posterior over regimes;
2. acontroller, a transparent rule plus a contextual bandit, sets configuration parameters such as the
tail weight and risk level, but never weights or constraints;
3. ascenario generator, a regime-conditioned diffusion model, draws N=512 scenarios of next-
period returns;
4. aruntime gate, calibrated by adaptive conformal inference on realised losses, accepts or rejects
the scenario set; a rejected set is regenerated up to B=3 times, then replaced by a block-bootstrap
fallback;
5. anallocatorsolves a convex program trading expected return against variance and conditional
value-at-risk (CVaRα, the mean loss in the worst 5% of scenarios) under the constraints; its
outputw sol is clipped and renormalised into the committed actionw t.
App. P gives the equations and the full loop (Algorithm 1).
Trust boundary and signals.Adaptive components (the controller and layer A in Fig. 1) may
be wrong or adversarial. They can degrade decision quality but cannot enlarge the feasible set,
3

A information and model layer
C action-containment layer B epistemic evidence layer
Regime HMM
1
2
3St
posteriorsπ t
Regime-conditioned diffusion
decision-relevant signal
retains29%of the true bull/crisis
mean gap (a bootstrap retains
101%) while local checks pass
ϵθ
xS x0
baseϵ b θ crisisϵ c θ
gt
Qq
Ltail: up-weight (1+η) left tail
Scenarios→risk
VaRα
CVaRα
loss−w ⊤r
ˆµt, ˆΣt
Operational evidence filter
KS/ES/VS, UC, CVaR err
CV aR allocator (convex QP)
w⋆
1⊤w=1, ℓ≤w≤u,∥∆w∥ 1≤τ
simplex
W eightswt
wt: post-hoc feasibility audited
zt {r(i) t+1}
sample
refine (≤B)
candidate evidence accepted
walk-forward
t→t+1
KKT/active-set record forw sol; residual audit and provenance forw t
Figure 1:ARC-AGENT, the agent under audit, and its three verification layers.Arrows trace one
rebalancing decision at date t.(A) Information and model layer: a regime HMM turns past returns
into regime posteriors πt (walk-forward), and a regime-conditioned diffusion generator, whose base
and crisis experts are mixed by a gate gt and trained with a tail-weighted loss Ltail, draws return
scenarios from which the risk quantities (VaRα, CVaRα) and moments (ˆµt, ˆΣt) are computed. The
red dashed box marks where the audit finds decision-relevant signal lost: the generator retains29% of
the true bull–crisis mean gap (a bootstrap retains101%) while local checks pass (§5.2).(B) Epistemic
evidence layer: the operational evidence filter scores each scenario set with calibration checks (KS,
energy and variogram scores, unconditional coverage, CVaR error) and either accepts it or requests
refinement, at most B times; it certifies no CVaRα bound (§4.4).(C) Action-containment layer:
the CVaR allocator solves a convex QP under the budget, box and turnover constraints. Its KKT and
active-set record is optimality evidence for the solver output wsol, whereas the committed weights wt
receive only a post-hoc feasibility audit, which supports admissibility for the reported runs.
because the constraint parameters (ℓ, u, τ)and the budget B belong to a trusted validator in the
action-containment layer (C). The system emits signals bearing on four distinct properties:decision
quality(is wt a good risk-adjusted choice?),calibration(do scenarios match outcomes? monitored by
the gate),admissibility(does wt satisfy the constraints? checked by a post-hoc audit) andprovenance
(can the solver output be traced to a logged optimisation? recorded by the KKT optimality conditions).
Protocol.Apairedcontrast compares two arms on identical simulated paths (common random num-
bers). Unless marked otherwise, intervals are 95% bootstrap intervals over seeds. Experiments with
10–24 paired seeds areconfirmatoryand those with 5–6 seedsexploratory(Table 14). Preregistration
is author-reported, with one disclosed amendment (App. T).
4 A claim-specific verification audit
The audit takes a proposed conclusion, such as “the generator is the bottleneck”, and asks whether the
evaluation canexpressthe improvement it concerns, whether the evidenceidentifiesthat improvement,
and where the inferencestops. For ARC-AGENTwe pose four questions (evidence and permitted
claims in Table 4, App. B):
Q1Was improvement attainable under an action set able to express it?
Q2Which component replacement recovers downstream value?
4

Q3Does improved local fidelity verify downstream improvement?
Q4Do joint repairs reveal structure that one-at-a-time checks miss?
4.1 Verification claims and verdicts
Averification claimis a conclusion recorded as Claim→Evidence→Verdict→Boundary , with
one of four verdicts:
•Supported: the evidence supports the claim, which may be relied on only inside its boundary.
• Unsupported: the evidence conflicts with the claim, or a required identification condition is unmet;
the claim must not be used for selection or certification.
• Unresolved: the experiment cannot distinguish the relevant explanations; the claim needs more
evidence, not clearance. It is not a weak form ofsupported.
•Not evaluated: no experiment was run.
Table 2 is the resulting ledger for ARC-AGENT; App. L expands each boundary.
4.2 Oracle headroom: can the evaluation express the improvement?
Anoracleis a policy with perfect knowledge of the hidden state. It obeys the system’s own constraints
and costs and differs from the system only in what it knows and which actions it may take. Indexing
oracles by an information setIand an action setAgives a lattice of attainable values,
J ⋆(I, A) = sup
π∈Π(I,A)
J(π),(1)
where Π(I, A)is the set of policies that use only information inI and act in A, and J is the metric. J ⋆
is monotone in both arguments (Prop. 1). A headroom estimate is therefore a property of an (I, A, J)
cell, not of the information alone. A low estimate in one cell cannot show that the information has
little value; if headroom rises whenAwidens at fixedI, the low estimate came from the evaluation.
For ARC-AGENTwe fix I to the true regime path and use four action sets of increasing expressiveness:
L0, the best static equal-weight/minimum-variance blend, with no regime knowledge;L1, switching
between those two portfolios with perfect regime knowledge;L2, a separate weight vector w⋆(k) for
each regimek; andL3, the ex-post optimal weight path.
4.3 Oracle-replacement interventions: where is value lost?
We replace one component at a time with an oracle counterpart and re-run the system. Every arm
receives the true regime, so regime detection is never the confound. Theperceptionreplacement
feeds the true regime to the generator; thefull generator bypasshands the allocator scenarios drawn
from clean, regime-conditional history.
The evidence is asymmetric. A replacement thatrecoversvalue identifies an observed bottleneck. A
replacement that recovers nothing leaves open whether the component matters, because a downstream
module that ignores its input masks any upstream repair. Such a null is recorded asunresolved, not
unsupported.
Some repairs act only jointly. The generator reaches the allocator through three channels: the scenario
set itself (tail shape and dependence), the conditional mean ˆµand the covariance ˆΣ. A complete 23
factorial switches each channel independently between the generator and clean history. Withv(S) the
paired Sharpe gain when the channels in S are repaired, we summarise the table with Shapley values
ϕi and Shapley–Taylor interaction indices ϕij (26, 27), and call P i<j ϕij/v(N) theinteraction
share. These summaries are descriptive and non-additive (App. U).
4.4 What can the runtime gate certify?
Scenarios come from the generator’s model pθ, not from the true outcome law P, so the error in
the allocator’s CVaR estimate has two parts: asamplingterm, which shrinks as N grows, and a
misspecificationterm ( pθ ̸=P ), which does not (App. W). A third question sits above both: does the
verification scoreidentifythe quantity it is read as bounding?
5

� �� �� �� �� �� ��
���������
���
���
���
���
���
���������
��������
�����
�������������������������������
�������������������������������������
���������������
�������������
���������
���������������������
���������������������
���������������
���� ���� ���� ���� ���� ����
����������������
�����������
������������
���������������
��������������
����������
������� ��
������������������
�����������������������
�����
����������������������������������
������������������������������������
���� ���� �����
����
�����
�����
�������
��������
���
���
���
���
���
���
������������������
�����������
������������
����������
������
�������������������������������������
����������������������������������
(a) Representational
underreach
(b) Information loss under
downstream misspecification
(c) Joint-repair
structure
ARC-A GENT
Figure 2:Three failure modes exposed by the audit(Sharpe; seeds and intervals in Table 14).(a)
Representational underreach: regime-conditional weights (L2) sit +0.38 above the static frontier
at matched drawdown, but switching between two portfolios (L1) only +0.18, a paired gain over L0
of +0.07±0.08 .(b) Interventional diagnosis: the true-regime replacement recovers nothing and
isunresolvedbecause the generator can mask it; removing the turnover cap, adding scenarios and
shrinking the mean also fail; only the full generator bypass recovers the gap (+0.68).(c) Joint-repair
structure(exploratory; Sharpe only): the mean-plus-scenario arm improves over baseline; the 55%
interaction share is a point estimate whose six-seed interval includes zero.
The gate is calibrated on realised returns, the only direct evidence about misspecification, and acts as
anoperational evidence filter. Its score compares one realised loss with a scenario CVaR. CVaR is
not elicitable (29), so this score does not identify CVaRα (condition C5); a joint VaR–CVaR score
would (28). In addition, refine-until-pass selects on the calibration statistic, which a union bound
corrects only for bounded B and only if each attempt is valid on its own (condition C6; App. W).
The gate is therefore not a decision-quality certificate: that claim isunsupported, and no empirical
result in §5 depends on the gate.
4.5 Trusted action boundary and attack surfaces
Controller-settable parameters areuntrusted: they can degrade quality but not enlarge the feasible
set. Constraint parameters and B aretrustedand validator-owned (App. O; Prop. 3). We specify
five attacks:A1randomises controller outputs within their ranges;A2poisons memory by flipping
the regime posterior;A3bypasses the runtime gate;A4is an adversarial controller that maximises
turnover;A5would compromise the validator. A1–A4 were executed; A5 was not.
5 Verification findings
All numbers are measured and scoped to U3 and the audited architecture. Each subsection answers
one question and ends with a verdict.
5.1 Q1: Restricted evaluations can hide attainable headroom
With perfect regime knowledge and identical constraints and costs, the four oracles reach Sharpe0.78
(L0), 0.84 (L1), 1.06 (L2) and 1.28 (L3), against 0.56 for ARC-AGENT(Table 10; rf=1.6% , see
App. V forrf=0).
L1 is anevaluation rulewith a restricted action set, not a weak baseline. Under it, perfect regime
information is worth a paired+0.07±0.08 Sharpe over L0, an interval that spans zero. Widening only
the action set raises the paired L2−L0 gain to +0.28±0.08 . What limited the measured headroom
was the evaluation, not the environment. ARC-AGENTdoes not capture this headroom (it sits 0.04
below the static frontier at matched drawdown), and no other scenario-based method does either
(App. G).
Verdict: supported, for U3 and the stated action sets.
6

5.2 Q2: Oracle replacements localise an observed generator bottleneck
Giving the generator the true regime instead of the HMM posterior changes nothing (16 seeds, paired:
+0.041±0.153 ), although the HMM is poor (crisis recall falls from 0.54 to 0.07 as tails fatten).
This doesnotclear perception: a generator that ignores its conditioning masks any benefit, and the
detector×generator factorial was not run. Removing the turnover cap (−0.09), shrinking ˆµ(−0.37)
and raising N from 512 to 4096 (−0.03) also recover nothing; more scenarios reduce sampling error
but not misspecification. Only the full generator bypass recovers the gap (Table 5).
The reason is visible in the generator’s output. Given perfect regime conditioning, it reproduces only
29% of the true bull–crisis difference in conditional means (90 of 313 bps), which we callmean-gap
retention. A regime-conditional bootstrap, which resamples history from the same regime, reproduces
101% and scores higher downstream (0.85 versus 0.56). The regime signal reaches the generator,
yet no end-to-end score reports its loss.
Verdict: supportedfor the generator as an observed bottleneck under this architecture;unresolvedfor
perception.
5.3 Q3: Local fidelity does not verify downstream improvement
Sweeps over diffusion steps and crisis oversampling implicate two contributors to the retention loss:
truncated reverse diffusion and under-representation of crises in training. A repair targeting both
raises retention from 47% to 186% and corrects the direction of the regime mean shift (cosine
0.59→0.97 ). Yet the paired Sharpe change is +0.075±0.174 , and the repaired generator (0.63)
still trails the bootstrap (0.85). The repair overshoots the size of the shift (208%), so the mean vector’s
relative error grows (0.82→1.18; Table 7).
Verdict: supported.Better local fidelity does not establish better decisions. The claim is one of
non-identification, not of a zero effect.
5.4 Q4: Joint repairs reveal structure missed by one-at-a-time checks
Repairing the mean and the scenarios together improves on the all-generator baseline by +0.221 (six-
seed paired 95% CI ±0.160), essentially all that the three channels recover together (v(N) = +0.218 ).
Each channel alone does less (mean +0.020±0.206 ; scenarios +0.079±0.066 ; covariance nothing).
The Shapley–Taylor estimate assigns 55% of v(N) to the mean×scenario interaction (Table 15), but
its six-seed interval (±0.18) includes zero, and the factorial records Sharpe only (App. D).
Verdict: supportedfor the joint repair improving on baseline;unresolvedfor superadditivity and the
size of the interaction.
5.5 Summary: different signals support different claims
Table 2 collects the verdicts. Evidence for one property does not transfer to another: feasibility audits
support admissibility for the reported runs only; the KKT record supports provenance for wsol, not
wt; and because the gate’s score does not identify CVaRα, the decision-quality claim isunsupported.
6 Red-teaming the verifier and its trusted boundary
If decision quality cannot be certified, what can the harness still be trusted to say? Attacks A1, A2
and A4 compromise adaptive components but leave the trusted boundary intact. Under all three, every
committed action passed the feasibility audit and kept its provenance record (Table 3). This holds
only for attacks that do not touch the validator.
A3 attacks the verifier itself, and nothing notices.Bypassing the gate removes the evidential basis
for the decision-quality claim, yet feasibility and provenance stay intact and the outcome stays benign:
under A3 the maximum drawdown, 9.9%, is thelowestin the table. No outcome metric we report
would have flagged the bypass. A verifier can lose its evidential validity without any immediately
poor outcome, and feasibility and provenance cannot substitute for it, because they never depended
on the gate.
7

Table 2:Claim ledger for ARC-AGENT(boundaries expanded in App. L).Unresolvedis not a
weaker form ofsupported; it marks a claim the evidence cannot settle either way.
Verification claim Evidence Verdict Boundary
Decision-relevant information is present
and expressible
L2 information–action hier-
archy
supported U3, specified action set
ARC-AGENTcaptures it matched-risk frontier unsupported current architecture
Generator is an observed bottleneck full generator bypass supported current trained generator
Improving perception would not improve
downstream value
true-regime replacementunresolvedmasked by generator
Joint mean+scenario repair improves on
the all-generator baseline
23 coalition table supported U3; 6 seeds, exploratory;
Sharpe only
Mean×scenario superadditivity Shapley–Taylor intervalunresolved interval includes zero at 6 seeds
Executed actions are admissible post-hoc residual checks supported reported runs only; not a univer-
sal guarantee
Solver outputs are traceable KKT and active-set records supported applies to wsol; auditability un-
measured
Implemented gate certifies decision quality
(CVaR)
implemented one-step score unsupported identification condition (C5) un-
met
Trusted-path compromise contained A5not evaluatedattack unexecuted
Table 3:Attack surfaces and what survives each executed attack.Decision quality, admissibility
and provenance are reported separately because they are different claims. Exploratory: 5 seeds,
unpaired; levels in Table 11. The feasibility audit is a post-hoc check, not a construction guarantee;
solver provenance is a record for wsol, not KKT-optimality of wt.A5 was not executed, so no claim
covers compromise of the trusted path.
Attack Claim surface Effect on decision-quality evidence Feas. audit Solver prov.
A3 gate bypass quality-verification layergate bypassed; metrics benign passed retained
A1 corrupted controller untrusted configuration degraded, within noisepassed retained
A2 poisoned memory untrusted memory degraded, within noisepassed retained
A4 adversarial controller untrusted configuration movedalongfrontierpassed retained
A5 validator compromise: specified but not executed; no robustness claim.
The preregistered containment hypothesis H3 wasnot supported: under A4, ARC-AGENT’s apparent
advantage over a rule-based control (0.83 versus 0.72 Sharpe) comes at a different risk level (16.7%
versus 19.4% MaxDD), and at matched risk the attack moved the systemalongthe frontier (App. H).
7 Lessons, limitations and conclusion
Lessons for reliable agent development(in full in App. A):
1. Check that the evaluation can express the target improvement before reading anything into a null.
2. An unchanged score fits both a useless and a masked component, so verify updates by intervention.
3. Read interventions asymmetrically: a positive replacement localises a bottleneck; a null one does
not show irrelevance.
4. Decision quality, calibration, admissibility and provenance are different claims, and none certifies
another.
5. Red-team the verifier as well as the agent: it can be bypassed while outcomes stay benign.
Limitations.Every statement is scoped to U3, one architecture and one generator family (App. L).
Perception is unresolved under masking; the interaction results rest on six seeds and Sharpe only;
conditions C5 and C6 behind any certificate reading of the gate are unproved, though no empirical
result depends on the gate; A5 was not executed; and no language-model controller, model judge or
prompt-injection attack was evaluated.
Conclusion.The unit of agent verification should be the claim, not the score. Treating it so turns
a flat score into three separate questions: could the change have helped under the evaluation used,
where was value lost, and what does each check certify. In the case studied, this exposed a restricted
evaluation, an observed generator bottleneck, a gap between local fidelity and decision value, and a
verifier that could be bypassed without any visible effect on outcomes.
8

References
[1] A. Z. Jacobs and H. Wallach. Measurement and fairness. InACM Conference on Fairness, Accountability,
and Transparency (FAccT), pp. 375–385, 2021.
[2] I. D. Raji, E. M. Bender, A. Paullada, E. Denton, and A. Hanna. AI and the everything in the whole wide
world benchmark. InNeurIPS Track on Datasets and Benchmarks, 2021.
[3] R. Agarwal, M. Schwarzer, P. S. Castro, A. C. Courville, and M. G. Bellemare. Deep reinforcement
learning at the edge of the statistical precipice. InAdvances in Neural Information Processing Systems,
volume 34, pp. 29304–29320, 2021.
[4] S. Rabanser, S. Kapoor, P. Kirgis, K. Liu, S. Utpala, and A. Narayanan. Towards a science of AI agent
reliability. InICML, 2026. arXiv:2602.16666.
[5] X. Liu, H. Yu, H. Zhang, Y . Xu, X. Lei, H. Lai, Y . Gu, H. Ding, K. Men, K. Yang, S. Zhang, X. Deng,
A. Zeng, Z. Du, C. Zhang, S. Shen, T. Zhang, Y . Su, H. Sun, M. Huang, Y . Dong, and J. Tang. AgentBench:
Evaluating LLMs as agents. InICLR, 2024.
[6] A. El hattami, M. Thakkar, N. Chapados, and C. Pal. WebArena Verified: Reliable evaluation for web
agents. InWorkshop on Scaling Environments for Agents (NeurIPS), 2025.
[7] S. Kara, F. Faisal, and S. Nath. WAREX: Web agent reliability evaluation on existing benchmarks.
arXiv:2510.03285, 2025.
[8] B. Zhao, D. Srikanth, Y . Wu, and Z. Jiang. SpecBench: Measuring reward hacking in long-horizon coding
agents. arXiv:2605.21384, 2026.
[9] J. Skalse, N. H. R. Howe, D. Krasheninnikov, and D. Krueger. Defining and characterizing reward hacking.
InNeurIPS, 2022.
[10] V . Krakovna, J. Uesato, V . Mikulik, M. Rahtz, T. Everitt, R. Kumar, Z. Kenton, J. Leike, and S. Legg.
Specification gaming: the flip side of AI ingenuity. DeepMind blog, 2020.
[11] Y . Zheng, Y . Hu, T. Yu, and A. Quinn. AgentSight: System-level observability for AI agents using eBPF.
InWorkshop on Practical Adoption Challenges of ML for Systems, pp. 110–115, 2025. arXiv:2508.02736.
[12] L. Dong, Q. Lu, and L. Zhu. AgentOps: Enabling observability of LLM agents. arXiv:2411.05285, 2024.
[13] R. Koohestani. AgentGuard: Runtime verification of AI agents. InIEEE/ACM International Conference
on Automated Software Engineering Workshops (ASEW), pp. 74–77, 2025.
[14] V . Bengs, E. Hüllermeier, and W. Waegeman. Pitfalls of epistemic uncertainty quantification through loss
minimisation. InAdvances in Neural Information Processing Systems, volume 35, pp. 29205–29216, 2022.
[15] A. Der Kiureghian and O. Ditlevsen. Aleatory or epistemic? Does it matter?Structural Safety, 31(2):105–
112, 2009.
[16] E. Hüllermeier and W. Waegeman. Aleatoric and epistemic uncertainty in machine learning: an introduction
to concepts and methods.Machine Learning, 110(3):457–506, 2021.
[17] E. Hüllermeier, S. Destercke, and M. H. Shaker. Quantification of credal uncertainty in machine learning:
a critical analysis and empirical comparison. InProceedings of the 38th Conference on Uncertainty in
Artificial Intelligence (UAI), PMLR volume 180, pp. 548–557, 2022.
[18] C. F. Manski.Partial Identification of Probability Distributions. Springer, 2003.
[19] G. Shafer.A Mathematical Theory of Evidence. Princeton University Press, 1976.
[20] P. Walley.Statistical Reasoning with Imprecise Probabilities. Chapman and Hall, London, 1991.
[21] R. A. Howard. Information value theory.IEEE Transactions on Systems Science and Cybernetics,
2(1):22–26, 1966.
[22] A. Agrawal, B. Amos, S. Barratt, S. Boyd, S. Diamond, and J. Z. Kolter. Differentiable convex optimization
layers. InNeurIPS, 2019.
[23] P. Z. Wang, J. Liang, S. Chen, F. Fioretto, and S. Zhu. Gen-DFL: Decision-focused generative learning for
robust decision making. arXiv:2502.05468, 2025.
[24] Z. Zhao, C. Yeh, L. Kong, and K. Wang. Diffusion-DFL: Decision-focused diffusion models for stochastic
optimization. InICLR, 2026.
[25] J. Xie, H. Wu, Q. Chen, X. Su, and Y . Chen. Decision-weighted flow matching for contextual stochastic
optimization. arXiv:2606.16790, 2026.
[26] L. S. Shapley. A value for n-person games. InContributions to the Theory of Games II, pp. 307–317.
Princeton, 1953.
[27] M. Sundararajan, K. Dhamdhere, and A. Agarwal. The Shapley–Taylor interaction index. InICML, 2020.
[28] T. Fissler and J. F. Ziegel. Higher order elicitability and Osband’s principle.Annals of Statistics, 44(4):1680–
1707, 2016.
[29] T. Gneiting. Making and evaluating point forecasts.JASA, 106(494):746–762, 2011.
[30] B. Amos and J. Z. Kolter. OptNet: Differentiable optimization as a layer in neural networks. InICML,
2017.
[31] A. Ang and A. Timmermann. Regime changes and financial markets.Annual Review of Financial
Economics, 4:313–337, 2012.
[32] A. N. Angelopoulos, S. Bates, A. Fisch, L. Lei, and T. Schuster. Conformal risk control.arXiv:2208.02814,
2023.
[33] N. Astorga, T. Liu, Y . Xiao, and M. van der Schaar. Autoformulation of mathematical optimization models
using LLMs. InICML, 2025.
9

[34] D. B. Brown. Large deviations bounds for estimating conditional value-at-risk.Operations Research
Letters, 35(6):722–730, 2007.
[35] A. Butler and R. H. Kwon. Integrating prediction in mean-variance portfolio optimization.Quantitative
Finance, 23(3):429–452, 2023.
[36] P. F. Christoffersen. Evaluating interval forecasts.International Economic Review, 39(4):841–862, 1998.
[37] E. Delage and Y . Ye. Distributionally robust optimization under moment uncertainty.Operations Research,
58(3):595–612, 2010.
[38] A. Desai, C. Freeman, Z. Wang, and I. Beaver. TimeV AE: A variational autoencoder for multivariate time
series generation.arXiv:2111.08095, 2021.
[39] F. X. Diebold and R. S. Mariano. Comparing predictive accuracy.Journal of Business & Economic
Statistics, 13(3):253–263, 1995.
[40] P. Donti, B. Amos, and J. Z. Kolter. Task-based end-to-end model learning in stochastic optimization. In
NeurIPS, 2017.
[41] A. N. Elmachtoub and P. Grigas. Smart “predict, then optimize”.Management Science, 68(1):9–26, 2022.
[42] I. Gibbs and E. Candès. Adaptive conformal inference under distribution shift. InNeurIPS, 2021.
[43] T. Gneiting and A. E. Raftery. Strictly proper scoring rules, prediction, and estimation.Journal of the
American Statistical Association, 102(477):359–378, 2007.
[44] P. Grünwald, R. de Heide, and W. Koolen. Safe testing.JRSS-B, 2024.
[45] J. D. Hamilton. A new approach to the economic analysis of nonstationary time series.Econometrica,
57(2):357–384, 1989.
[46] S. Holt, M. Ruiz Luyten, A. Berthon, and M. van der Schaar. G-Sim: Generative simulations with large
language models and gradient-free calibration. InICML, 2025.
[47] S. Holt, M. Ruiz Luyten, T. Pouplin, and M. van der Schaar. Fact-augmented lookahead planning for
LLM agents. InProceedings of the 29th International Conference on Artificial Intelligence and Statistics
(AISTATS), PMLR volume 300, 2026. arXiv:2506.09171.
[48] S. R. Howard, A. Ramdas, J. McAuliffe, and J. Sekhon. Time-uniform, nonparametric, nonasymptotic
confidence sequences.Annals of Statistics, 49(2):1055–1080, 2021.
[49] C.-J. Kim and C. R. Nelson. Dynamic linear models with Markov-switching.Journal of Econometrics,
60(1–2):1–22, 1994.
[50] M. Kollovieh, A. F. Ansari, M. Bohlke-Schneider, J. Zschiegner, H. Wang, and Y . Wang. Predict, refine,
synthesize: Self-guiding diffusion models for probabilistic time series forecasting (TSDiff). InAdvances
in Neural Information Processing Systems, 2023.
[51] P. H. Kupiec. Techniques for verifying the accuracy of risk measurement models.Journal of Derivatives,
3(2):73–84, 1995.
[52] M. López de Prado. Building diversified portfolios that outperform out of sample.Journal of Portfolio
Management, 42(4):59–69, 2016.
[53] M. López de Prado.Advances in Financial Machine Learning. Wiley, 2018.
[54] O. Ledoit and M. Wolf. A well-conditioned estimator for large-dimensional covariance matrices.Journal
of Multivariate Analysis, 88(2):365–411, 2004.
[55] B. Lim, S. Ö. Arik, N. Loeff, and T. Pfister. Temporal fusion transformers for interpretable multi-horizon
time series forecasting.International Journal of Forecasting, 37(4):1748–1764, 2021.
[56] R. Lowe, Y . Wu, A. Tamar, J. Harb, P. Abbeel, and I. Mordatch. Multi-agent actor-critic for mixed
cooperative-competitive environments. InNeurIPS, 2017.
[57] H. Markowitz. Portfolio selection.Journal of Finance, 7(1):77–91, 1952.
[58] A. Ramdas, P. Grünwald, V . V ovk, and G. Shafer. Game-theoretic statistics and safe anytime-valid inference.
Statistical Science, 38(4):576–601, 2023.
[59] K. Rasul, A.-S. Sheikh, I. Schuster, U. Bergmann, and R. V ollgraf. Autoregressive denoising diffusion
models for multivariate probabilistic time series forecasting. InICML, 2021.
[60] R. T. Rockafellar and S. Uryasev. Optimization of conditional value-at-risk.Journal of Risk, 2(3):21–41,
2000.
[61] D. Salinas, V . Flunkert, J. Gasthaus, and T. Januschowski. DeepAR: Probabilistic forecasting with
autoregressive recurrent networks.International Journal of Forecasting, 36(3):1181–1191, 2020.
[62] Y . Tashiro, Y . Song, J. Song, and S. Ermon. CSDI: Conditional score-based diffusion models for time
series imputation. InNeurIPS, 2021.
[63] P. S. Thomas and E. Learned-Miller. Concentration inequalities for conditional value at risk. InICML,
2019.
[64] V . V ovk, A. Gammerman, and G. Shafer.Algorithmic Learning in a Random World. Springer, 2005.
[65] Y . Wang and F. Gao. Deviation inequalities for an estimator of the conditional value-at-risk.Operations
Research Letters, 38(3):236–239, 2010.
[66] X. Wang et al. Executable code actions elicit better LLM agents. InICML, 2024.
[67] S. Yao, J. Zhao, D. Yu, N. Du, I. Shafran, K. Narasimhan, and Y . Cao. ReAct: Synergizing reasoning and
acting in language models. InICLR, 2023.
[68] J. Yoon, D. Jarrett, and M. van der Schaar. Time-series generative adversarial networks. InNeurIPS, 2019.
[69] M. Zaffran, O. Féron, Y . Goude, J. Josse, and A. Dieuleveut. Adaptive conformal predictions for time
series. InICML, 2022.
10

Appendix
The appendix is supplementary: it records specifications, full tables, derivations and boundary
statements for the claims made in the main body.
A Verification-audit principles, in full
This case study motivates five verification-audit principles, which may transfer beyond it. Verify the
opportunity before verifying the system: our L1 oracle was a representation-restricted evaluation
protocol, not a weak baseline. Verify changes by intervention, since a null after an upstream update
establishes nothing when downstream masking is possible. Treat interactions as first-class verification
objects, because component-wise checks can obscure joint-repair patterns; in the present factorial the
joint arm improves over baseline, while the interaction and conditional-contribution claims remain
unresolved. Separate quality, admissibility and provenance, because a feasible or auditable action
may still be poor. And verify the verifier: bypass, adaptive selection and invalid scoring rules are
attack surfaces in their own right, and our own gate fails two of them.
B Claim–evidence map
Each question in §5 is answered by a specific, separately reported piece of evidence; Table 2 gives
the resulting verdicts and their boundaries. Table 4 states, for each of the four questions posed in §4,
the evidence used and the claim that evidence permits.
Table 4:Verification questions posed of ARC-AGENT, the evidence used, and the claim that
evidence permits.Each row concerns adifferentconstruct. Sharpe is an operational proxy for
risk-adjusted decision value, not a general measure of agent quality. Verdicts are collected in Table 2.
Verification question Evidence Permitted claim
Q1 Was improvement attainable under
an action set able to express it?
L0–L3 oracle Sharpe at fixed information, widen-
ing the action set (§5.1, Table 10); 24 seeds,
paired, confirmatory
Measured headroom depends on the action
representation, not on the information alone
Q2 Which component replacement re-
covers downstream value?
Stage-wise oracle replacement with the true
regime given to every arm (§5.2, Table 5); 10–16
seeds, paired, confirmatory
A positive replacement identifies an ob-
served bottleneck; a null one does not iden-
tify irrelevance
Q3 Does improved local fidelity verify
downstream improvement?
Retention, directional cosine and vector error
against paired Sharpe (§5.3, Table 7); 6 seeds,
exploratory
Improved local scores do not establish
downstream improvement
Q4 Do joint repairs reveal structure that
one-at-a-time checks miss?
Complete 23 coalition table with Shapley and
Shapley–Taylor summaries (§5.4, Tables 6, 15);
6 seeds, exploratory
The joint arm improves over the all-
generator baseline; its conditional contribu-
tion and the interaction magnitude remain
unresolved
Evaluation question Evidence
Is meaningful improvement attainable? L0–L3 oracle hierarchy (§5.1)
Did the full agent capture that improvement? static risk frontier, paired contrasts (§5.1)
Which stage forfeited the improvement? stage-wise oracle replacements (§5.2)
Can a module be masked by another? complete2 3 channel coalition table (§5.4)
Does the runtime boundary preserve admissibility? per-action feasibility audits (§6)
Is the action traceable? solver records and active-set logs (App. K)
Can the verifier itself fail silently? A3 gate-bypass attack (§6)
Which claims remain unsupported? unmet score identification (§4.4); unexecuted A5
C Oracle-replacement intervention outcomes
Table 5 reports the stage-wise interventions summarised in §5.2. Every row is given the true latent
regime, so detection is never the confound, and rows are paired on common random numbers. “% of
gap recovered” is measured against the L2 reference policy, not against an upper bound: L2 optimises
mean–variance per regime, so a CVaR allocator handed the clean scenario law can exceed it, which
is why I1 exceeds 100%. The remaining interventions of Fig. 2(b) (scenario count, shrinkage) are
reported inline in §5.2.
11

Table 5: Oracle-replacement interventions (10 seeds, paired, common random numbers; true regime
given to every row). Only a full generator bypass recovers the measured gap; no other intervention
recovers a detectable share of it. The factorial of Table 6 subsequently separates that single bypass
into the conditional-mean, covariance and scenario tail/dependence channels; the two experiments
use different baselines and seed counts and their levels are not directly comparable (§5.4). “% of
gap recovered” is (Sharpe−Sharpe I0)/(SharpeL2 −Sharpe I0). ± values are across-seed standard
errors over 10 seeds under common random numbers.L2 is a reference policy, not an upper bound: it
optimises mean–variance per regime, so a CVaR allocator given the clean scenario law can exceed it.
Intervention Sharpe Turn.% % of gap recovered
I0 baseline (scenario moments, cap0.20)0.465±0.090 19.7n/a
I1 + clean regime-conditional scenarios
and moments(full generator bypass)
1.141±0.12718.8 +121%
I2+no turnover cap0.377±0.084 60.2−16%
L2 regime-weight reference policy1.023±0.111 8.8n/a
The allocator is not the bottleneck (detail for §5.2).We conjectured that the CVaR term, roughly
33× the return term at a daily horizon, dominates the objective and leaves the solution insensitive to
the conditional mean. We tested it, and it is false: swapping bull- for crisis-regime scenarios moves the
QP’s solution by118% of the oracle’s own rotation, aligned with it atcos(∆wQP,∆w oracle) = +0.75.
The optimiser would therefore have used a correct conditional mean had one reached it, which is
what makes the generator, not the allocator, the observed bottleneck of §5.2.
D Factorial over decision functionals
The allocator reads the scenario law through three separable channels, so we can swap each in-
dependently between the generator’s output and clean regime-conditional history. Table 6 reports
all eight cells of the 23 design, paired against the all-generator baseline. The two-channel rows
are the informative ones: covariance adds nothing to any other repair, so the design collapses to a
mean×scenarios interaction on a nuisance third factor. Note the asymmetry in the single-channel
intervals: the scenario-only effect is +0.079±0.066 , an interval that excludes zero, so that channel
does deliver a modest standalone repair; the mean-only effect is +0.020±0.206 , which is wide
enough not to exclude the joint effect either. Descriptively, the joint-arm point estimate is larger than
either single-arm point estimate. Because the paired contrast between the joint and scenario-only
arms is unavailable from the retained aggregate summaries, this comparison does not establish a
nonzero conditional mean contribution or superadditivity.
The contrast that bears most directly on the mean channel is v({mean,scenario})−v({scenario}) =
+0.221−0.079 = +0.142 : what the clean conditional mean addsonce the scenario channel is
already repaired. We report the point estimate only. Its seed-bootstrap interval would be a paired
contrast between two repaired cells rather than against the common baseline, and the per-seed pairs
those two cells require were not retained, so the interval cannot be recovered from the available
aggregate summaries. We therefore report this contrast descriptively and do not use it to support the
interaction claim.
Reconciling Table 5 with Table 6.These are different experiments and their levels are not directly
comparable, so we state the relationship explicitly. I1 is afull generator bypass: the allocator
is handed the clean regime-conditional empirical scenario law (its scenario set together with the
moments computed from it) in place of anything the diffusion model produces. The 23 factorial
instead decomposes that single bypass into its three separable channels and swaps them independently.
Consequently (i) I1 is the union of all three factorial repairs plus whatever the bypass changes that the
three-channel parameterisation does not capture, and (ii) the two arms are run at different seed counts
(10 vs. 6) against differently-constructed baselines (0.465 for I0, 0.635 for the all-generator factorial
cell), which are themselves trained separately, as elsewhere in this paper (§5.4). The gap between
I1’s 1.141 and the factorial’s all-three cell at 0.853 is thereforenotevidence that the channels fail
to compose; it is the combined effect of a wider intervention, a different baseline, and independent
training runs. No paired arm is available to decompose that difference: with independently trained
12

Table 6:The complete 23 factorial: all eight cells.Paired ∆Sharpe against the all-generator
baseline (6 seeds, common random numbers, 95% CI over seeds). Reading down the single-channel
rows, covariance is worth nothing; reading across the pairs,addingcovariance to any other re-
pair changes nothing (mean +0.020 versus mean+covariance +0.020; scenarios +0.079 versus
scenarios+covariance +0.079), while mean +scenarios recovers essentially the whole effect and
adding covariance on top of it does not improve matters ( +0.221 vs. +0.218). At six seeds the
design isunderpowered to distinguish superadditivity from additivity. Descriptively the joint-arm
estimate exceeds either single-arm estimate; because the paired joint-versus- scenario-only contrast
cannot be recovered from the retained summaries, neither superadditivity nor a nonzero conditional
mean contribution is established. The interaction estimate and its seed-bootstrap interval are reported
in Table 15; at six seeds that interval includes zero.These cells report Sharpe only.We did not record
MaxDD or turnover per cell, so the risk-axis check we insist on elsewhere (§5.1, §6) has not been
applied to the factorial: a channel repair that moved a cell along the risk frontier rather than off it
would not be visible here.
Channels replaced with clean regime-conditional history Sharpe∆Sharpe95%CI
none (all generator; baseline)0.635n/a n/a
covariance ˆΣonly0.634−0.001±0.001
conditional meanˆµonly0.655 +0.020±0.206
scenarios only (tail+dependence)0.713 +0.079±0.066
mean+covariance0.654 +0.020±0.212
scenarios+covariance0.714 +0.079±0.066
mean+scenarios0.856+0.221±0.160
all three0.853 +0.218±0.164
Table 7:Retention metrics. ∆µtrue is the true bull-minus-crisis conditional mean vector and ∆ˆµ
the generator’s. The first row is the headline 29%; the middle rows are the same scalar computed in
other arms; the last two rows are thedirectionalandvectordiagnostics that show why the scalar is
insufficient.
Quantity Definition Reported values Arm
Mean-gap retention∥∆ˆµ∥ 1/∥∆µtrue∥1 29%(90/313bps) deployed pipeline
same, step sweep as above19/30/76%(S=20/50/100) step-count sweep
same, repair arm as above47%→186%repair arm
Directional similaritycos(∆ˆµ,∆µ true) 0.59→0.97repair arm
Size ratio∥∆ˆµ∥ 2/∥∆µtrue∥2 208%(overshoot) repair arm
Relative vector error∥∆ˆµ−∆µ true∥2/∥∆µtrue∥2 0.82→1.18repair arm
baselines and different seed counts, the remaining discrepancy is not identifiable from the reported
runs, and the boundary is recorded as item (ii) of App. L.
Mechanisms behind the mean collapse (detail for §5.3).The collapse implicates two candidate
contributors to the observed retention loss.Truncated reverse diffusion: mean-gap retention is 19%
at S=20 steps, 30% at our preregistered S=50 and 76% at S=100.A starved conditioning class:
oversampling crisis 15× lifts retention 30%→53% . The reported η sweep does not support the
tail-weighted loss as the primary driver of the retention loss: retention is flat in η and is 29% even at
η=0. Repairing both mechanisms raises retention 47%→186% within the repair arm and moves
the paired Sharpe by +0.075±0.174 . Arms are trained separately, so unrepaired retention differs
slightly across them (29% deployed, 30% step-sweep, 47% repair); we always quote an arm against
its own baseline.
The retention quantities, defined.Three distinct quantities appear above and are easy to conflate,
so Table 7 defines each one. All are computed with the true regime given to the generator; none is a
decision metric.
13

Table 8:Does the complete system deliver genuine improvement at matched risk?(exploratory,
5 seeds; ± is the across-seed standard deviation, not a paired contrast; those are in Tables 5–6.) The
static frontier is the reference: “Excess” is Sharpe relative to the frontier at the same realised MaxDD,
the comparator being the best static blend within the restricted EW–MinVar family. ARC-AGENT
does not outperform the frontier, whereas the regime-conditional bootstrap (ten lines, no generative
model) does, which is what shows the environment contains usable regime information. The −CVaR
ablation lies beyond the frontier’s risk endpoint (off-supp.), as does mean–variance (Table 9).
Method Sharpe MaxDD% Turn.% Frontier Excess
Equal weight0.74±0.46 18.50.0 0.74+0.00
Minimum variance0.37±0.328.52.8 0.38−0.01
Gaussian→QP0.41±0.27 12.119.7 0.60−0.19
Block bootstrap→QP0.44±0.28 10.319.6 0.52−0.08
Regime-cond. bootstrap→QP0.85±0.1010.919.6 0.53+0.32
ARC-AGENT(full)0.56±0.29 10.518.1 0.60−0.04
−verifier0.41±0.29 9.718.3 0.48−0.07
−CVaR term0.84±0.50 19.918.4off-supp.n/a
Table 9: The five remaining implemented baselines (exploratory, 5 seeds; mean ± across-seed
standard deviation). None reaches the regime-conditional bootstrap’s 0.85. Mean–variance attains
the highest Sharpe of the five but at 19.2% drawdown, beyond the static frontier’s risk endpoint, the
same risk-axis confound the frontier test exists to expose, and the reason it is not evidence against our
conclusion.
Method Sharpe MaxDD% Turn.%
Risk parity0.52±0.30 11.4 1.5
Mean–variance0.71±0.50 19.2 12.0
Hierarchical risk parity0.36±0.29 8.7 3.2
Historical CVaR0.45±0.29 10.1 19.6
DRO-CVaR0.34±0.27 9.7 19.9
E End-to-end comparison at matched risk
This table supports the claim that end-to-end performance alone is insufficient. It is not a performance
result in its own right, which is why it sits here (§5.5).
F Remaining baselines
Table 9 reports the five implemented baselines not shown in Table 8 or Table 11, so that all eleven are
accounted for. They are run under the same box, turnover cap and costs as every other method, on the
same paths. Like Table 8 these areexploratoryfive-seed results and are not paired contrasts.
G Oracle hierarchy
The hierarchy of §5.1 in full. All four oracles have perfect knowledge of the latent regime and run
under identical box, turnover and cost settings; they differ only in the action set they are permitted to
express that knowledge through. Figure 3 plots them against the static EW/MinVar frontier, so the
headroom is read as averticalgap at matched drawdown.
H Red-team results
Full numbers for the fourexecutedattacks summarised at verification-surface level in Table 3 of §6.
A5 (constraint injection against the validator) is registered and was not run, so it has no row here
and no claim is made about it. The two comparison rows at the foot of the table are the rule-based
weights-emitting controls of App. Q, standing in for an agent that emits weights directly with no
14

� �� �� �� �� �� ��
���������
���
���
���
���
���
���������
�������������������������������
���������������������������
���������
������������������������
���������������������������� � ���
����������������������������
ARC-A GENT
Figure 3: Oracles versus the static EW/MinVar frontier ( 24 seeds; bars are ±1 s.e.; confirmatory,
paired under common random numbers; Sharpe at rf=1.6% ). Construct: attainable decision value
of perfect latent-state information under each action representation. The wider L2 and L3 action
representations exhibit positive matched-risk oracle headroom in U3. ARC-AGENTlies close to
the evaluated static frontier under the reported matched-risk comparison. Unresolved: whether this
headroom transfers beyond U3 or beyond the four action sets shown.
Table 10: Oracle hierarchy ( 24 seeds, paired).All Sharpe levels in this table are computed at
the preregistered rf=1.6% , not at the rf=0 used for the primary U3 metrics (App. Q); the paired
L2−L0 contrast is +0.28±0.08 here and +0.248 at rf=0 (§5.1). “Excess” is Sharpe over the
static EW/MinVar frontierat the same drawdown, a different quantity from that paired contrast.
The action set decides the answer: L1 is near-tautological, while L2, the oracle appropriate to a
regime-conditional allocator, shows positive paired headroom under the wider action representation.
Oracle over. . . Sharpe MaxDD% Excess
L0 (no regime knowledge)0.78 12.4 0.00
L1 two-point action set (EW↔MinVar)0.84 16.0 +0.18
L2regime-conditional weightsw ⋆(k)1.0617.2 +0.38
L3 ex-post optimal weight path1.28 14.7 +0.62
ARC-AGENT0.56 10.5−0.04
solver to configure; they arenotlanguage-model agents, and no LLM was executed anywhere in this
work.
I Why scalar local signals are insufficient (detail for §5.3)
Does any single upstream score verify downstream decision quality? Ours does not. Separate
step-count and crisis-oversampling sweeps implicate two candidate contributors to the observed
retention loss: truncated reverse diffusion and limited representation of the crisis conditioning
class. The combined repair targets both contributors and therefore does not isolate their individual
downstream effects; the reported η sweep does not support the tail-weighted loss as the primary
driver (App. D). Repairing both raises retention 47%→186% while the paired Sharpe moves
+0.075±0.174 , with an interval spanning zero; the repaired generator ( 0.63) still loses to the
bootstrap (0.85). The vector diagnostics show why: the repair fixes thedirectionof the regime
mean-shift (cos 0.59→0.97 ) butovershootsits size ( 208%), so the relative error of the mean vector
15

Table 11: Red-team results,measured( 5 seeds; ± is the across-seed standard deviation, not a paired
contrast). Feasibility and provenance survive everyexecutedattack (A1–A4), but so does feasibility
for an agent that merely projects, which is why the surviving claim concerns auditability.“Infeas.” is
a post-hoc audit, not a construction guarantee: every committed weight vector is checked against
the budget (10−4), box (10−6) and turnover (10−4) tolerances, and the column counts the rebalances
that fail (App. O).“Solver record”reports whether the underlying convex solve produced a complete
active-set and KKT record; it doesnotimply that the post-processed committed vector is itself
KKT-optimal.A5 (validator injection) was not executed and has no row.The two comparison
rows are rule-based weights-emitting controls; no LLM was executed.
Attack Sharpe MaxDD% Infeas. Solver record
ARC-AGENT
none (base)0.56±0.29 10.50 100%
A1 corrupted controller0.50±0.41 12.40 100%
A2 poisoned memory0.52±0.28 10.40 100%
A3 conformal-gate bypass0.55±0.29 9.90 100%
A4 adversarial controller (injection proxy)0.83±0.38 16.70 100%
weights-emitting agent (no solver)0.50±0.42 25.7345 0%
weights-emitting agent+projection0.72±0.40 19.40 0%
getsworse( 0.82→1.18 ). Distributional fidelity, conditional mean retention, verifier pass rate
and downstream utility are not interchangeable, and a module can pass a local verification metric
while failing the system-level objective. Our own measurements do not supportdecision-functional
retentionas the missing diagnostic either. This is the decision-focused-learning critique ( 41, 40) in
sharp form, and it constrains what a remedy must target: not a better distributional score — likelihood,
the verifier’s calibration tests, or even the conditional mean the optimiser literally reads — but the
decision itself (App. M).
J Preregistered verdicts in full (detail for §5.5)
Table 8 gives the comparison for the arms that isolate scenario quality, and all five preregistered
verdicts follow, each against its frozen failure condition.H1 (tail control): inconclusive, not refuted.
ARC-AGENT’s MaxDD ( 10.5) versus a block bootstrap (10.3) is a paired +0.2pp against a design
with little power at that scale; what wecansay is that the diffusion model shows no detectable benefit
even with perfect conditioning.H1b (does the CVaR term do the work?): supported, with a
twist.Removing it inflates MaxDD 10.5→19.9 andraises Sharpe to 0.84, the highest in the table:
a drawdown reduction bought with a real Sharpe cost, precisely the risk-axis trade the frontier test
exposes.H2 (union-bound correction): not exercised.The correction never binds, so nothing here
tests Prop. 2.H3 (containment of corrupted intent): not supported(§6).H4: not executed.No
LLM controller was run.
K Active-set analysis from the logged duals
Which constraints actually bind (using the logged duals).Provenance is worth more than a
100% checkbox only if the KKT record is used. We therefore report active-set frequencies from the
logged duals: in the illustrative run the turnover cap is slack in calm regimes (mean ∥∆w∥1 ≈8%
vs. the 20% cap) butbinds in ∼38% of crisis-onset rebalances, when the agent wants to de-risk
faster than the cap allows; the box binds on the volatility proxy and short-duration sleeves during
flights-to-quality. This is the one genuinely informative thing provenance yields, and it also sharpens
the case for executing A5: the feasibility guarantee is not guarding an idle door. The turnover
constraint is exactly what an attacker (or a panicked controller) would most want to relax, and it is
the one the validator refuses to expose. A5 remains registered and unexecuted (§6).
What the record does and does not give.The KKT record certifies feasibility and stationarity of
thesolver output wsol for the problem it was solved against. The subsequently committed action wt,
obtained from wsol by clipping and renormalisation (App. O),passed the specified post-hoc feasibility
audit, but we do not claim it retains the solver’s KKT optimality certificate (Prop. 3). Neither claim,
by itself, re-derives wt from scratch.Deterministic replayadditionally requires the realised scenario
16

matrix (or the seed and generator state that produced it), the model checkpoint hash, the solver name,
version and tolerances, and the tie-breaking rule used when the active set is degenerate. Our log
records these alongside the certificate, but the guarantee we state and prove is the verification claim
above; replay is an implementation property of the release, not a theorem.
L Boundaries of established knowledge
This appendix is organised byclaimrather than by experiments that “should” be run. Each entry
states the exact limit of the existing evidence, and none is a promise to fix it for this paper. With the
claim–evidence ledger (Table 2), these entries record what the audit did not establish.
1. Domain boundary.Every empirical statement is scoped to U3 and to one decision architecture.
We do not claim “generative modelling is a bottleneck in modular decision systems” in general; we
claim thatthisconditional diffusion model, trained this way, forfeits the conditional mean onthis
benchmark, that the repair arm targets two plausible contributors to the collapse, and that repairing
them does not repair the decision. The regime-conditional bootstrap’s advantage is partly favoured by
U3’s stationary within-regime conditionals: a resampler inherits the conditional law by construction,
so it is close to a near-oracle generator here. Establishing where conditionalgenerationcould pay
requires sweeping within-regime nonstationarity, regime overlap and duration heterogeneity, which
we have not done.
2. Masking boundary.Perception cannot be judged independently while the generator ignores its
conditioning. Perfect detection does not helpthrough the current generator; that does not establish
perception is unimportant, and perception may matter once the generator is fixed. The factorial
detector × generator matrix that would separate the two was not run, so the verdict in Table 2 is
unresolved: neither supported nor refuted.
3. Intervention boundary.The stage interventions (Table 5) and the channel factorial (Table 6)
use different baselines and seed counts and were trained separately, so the difference between the full
generator bypass and the all-three-channel repaircannot be decomposed(§5.4, App. D). Rerunning
both against one baseline under common random numbers at a single seed count would identify
whether the three channels exhaust the bypass.
4. Risk-axis boundary.Table 6 reports ∆Sharpe alone: the factorial lacks MaxDD and turnover
per cell, so we cannot show that a channel repair moves a portfoliooffthe risk frontier rather than
along it, the confound our own frontier test exists to expose and which we apply everywhere else.
The risk-axis position of each factorial cell is therefore not identified by the reported runs.
5. Architecture boundary.One conditional generator family is evaluated. Without conditional
V AE, normalising-flow, plain conditional diffusion and moment-regularised variants, the localisation
result remains single-architecture.
6. Auditability boundary.The surviving governance claim is anargument from the available
records, not a measurement: we have not scored whether an auditor can recover the binding constraint
and the reason-for-trade from the log alone. This is the paper’s weakest link, since it is the one claim
asserted without evidence.
7. Controller boundary.No LLM controller was executed. All measured runs use arule-plus-
contextual-bandit controller; the system under test is a planning loop over typed tool configurations,
and A4 is an adversarial-controllerproxy, not a live prompt injection. Nothing here bears on
language-model reasoning or prompt-injection robustness.
8. Statistical boundary.Seed counts are 5–24 and inconsistent across tables. The factorial is the
binding case: at six paired seeds the mean-only interval is very wide and the interaction interval
includes zero, so themagnitudeof the mean–scenario interaction is unresolved and the headline 55%
is a point estimate. Twenty to thirty paired seeds under common random numbers would settle it, and
App. R records that compute is not what is stopping us.
17

9. Certificate boundary.The implemented one-step score does not identify CVaRα (§4.4, App. W),
so the executed gate is an operational filter and not a validated decision-quality certificate. H2 was
never exercised, so nothing in this paper tests the refinement correction either.
10. Threat-model boundary.Trusted-path compromise was not executed. A5 targets the validator,
and the solver, post-solve cleanup and audit code are equally inside the trusted path; robustness to
compromise of any of them is unevaluated, so the feasibility result of Table 3 is evidence about
attacks that leave those components alone.
Future work.Decision-focused training of the scenario generator; a disaggregated retention
analysis over the mean, covariance and scenario tail/dependence channels; a second decision domain
(inventory, energy dispatch) to test whether the localisation protocol transfers; and conformalrisk
controlon a monotone loss in place of coverage of a CVaR difference.
M Extended related work
Agentic systems and tool use.ReAct-style interleaving of reasoning and acting ( 67) and code-as-
action agents (66) motivate our typed configuration interface. Recent work couples language models
with formal optimisation: autoformulation of optimisation models (33) and generative simulation with
gradient-free calibration (46) show that LLMs are most reliable when theyconfigurea solver rather
than replace it. Lightweight online memory without finetuning ( 47) informs our regime-indexed
episodic store. We adopt this “LLM plans, solver acts, verifier gates” pattern as a governance principle
rather than a convenience. A systems literature instruments running systems at stable boundaries
rather than inside volatile application code ( 11, 12, 13); our validator, feasibility audit and KKT
records are instances of that discipline, and the distinction we insist on is thatobservability provides
evidence; verification specifies what property that evidence supports.
Regimes and structured generative time series.HMMs capture structural breaks and state
dependence (45, 49, 31); we reuse their posteriors as conditioning signals. GAN/V AE and diffusion
generators improve realism (68, 38, 59, 62), but are typically unconditioned and loosely coupled to
decisions; ARC-AGENTinstead couples a regime-conditioned, tail-weighted diffusion generator to
the allocator as a callable, verifiable tool.
Decision-focused learning.A parallel literature learns predictive modelsthroughthe optimiser
rather than upstream of it: smart “predict-then-optimize” (41), task-based end-to-end learning (40),
and differentiable optimisation layers (30, 22), with portfolio applications (35) and, more recently,
decision-focusedgenerativemodels ( 23, 24, 25), which target exactly the generator-to-decision
coupling that our §5.3 measurement finds broken. ARC-AGENTis deliberatelynotend-to-end:
it keeps the solver a fixed, certified, non-differentiated component so that its guarantees survive a
compromised upstream, and treats decision-aware training as future work. The trade-off this involves
is easy to overstate. It isnotoptimality versus auditability: an upstream model can be trained through
a differentiable convex layer (30, 22) and still be deployed against the same fixed solver, which still
emits the same KKT record, so auditability survives decision-focused training. What decision-focused
training actually costs ismodularity: the generator becomes coupled to a particular downstream
program and to its training pipeline, and can no longer be swapped, certified, or attacked in isolation
in the way §4.5 relies on. That coupling is the central design choice we are making, and this literature
is the alternative branch. Our own measurement (§5.3) is an argument for paying that cost.
Distribution-free uncertainty quantification.The verifier is implemented as a conformal-style
operational evidence filter. Conformal prediction ( 64) and conformal risk control ( 32) provide
finite-sample, distribution-free coverage guarantees and are the right foundation for a valid act-time
certificate, but the implemented score does not satisfy the identification conditions required for that
interpretation (§4.4).
Robust allocation and governance.Distributionally robust and CVaR formulations address fat
tails (60, 37) but hinge on scenario quality; we feed a regime-conditioned scenario set through an
operational evidence filter into a convex allocator with Ledoit–Wolf shrinkage ( 54). Multi-agent
coordination (56) inspires our role-based tools, but our emphasis is onauditability: the allocator’s
18

KKT system provides solver-side audit trails that align with the reliability/governance goals of
structured-data agents.
N The U3 benchmark
U3 is a controllable synthetic regime-shift generator over d correlated instruments. A latent Markov
chain with K=3 states (bull,stagnation,crisis) drives a state-dependent return law: per-state mean
and covariance, with crisis drawn from a fat-tailed, left-skewed law whose lower-tail dependence
exceeds its average correlation, so diversification degrades exactly when it is needed (Fig. 4b,c). There
are d=10 instruments, three of them defensive. Returns follow a regime-dependent factor model
driven by a skew-tmarket factor with shared mixing, so no regime is Gaussian: degrees of freedom
fall from 12 (bull) through 7 (stagnation) to 3.5 (crisis) and skew steepens from 0 to −0.80 (App. O).
Crisis is rare and persistent: the stationary crisis share is 4.79% and the mean crisis episode is about
45 trading days, longer than the 21-day rebalance interval; the evaluated 1,500-day development
sequence realises 66 crisis days (4.4%). Four knobs are exposed: crisisfrequency(the chain’s entry
probability),severity(the crisis mean and tail index),duration(its self-transition probability), and
detectability( regime_separation, which interpolates the per-state means toward a common
value). At regime_separation= 0 the states are indistinguishable from returns alone and HMM
balanced accuracy equals chance, 1/3, by construction; this is the calibration check in Fig. 4(d).
Because the latent state is recorded, regime inference can be scored directly and the oracle hierarchy
of §5.1 can be computed exactly, neither of which is possible on historical data.
Horizon and splits.Each seed draws a single 2,200-day path. The first 756 days (≈3 years) are a
warm-upused only to initialise the HMM and to fit the first generator; no trade is placed inside it.
The remaining 1,444 days are evaluated walk-forward with a rebalance every 21 trading days, giving
69 evaluated rebalances per seed. Estimation is strictly causal: at each rebalance the generator
and detector see only data up to that date, and the generator is refit every 1,000 trading days (2 refits
per run), the cadence behind every reported number (Table 12, App. O). The generator, its default
parameter values, and the seed registry are specified in Table 12, Table 14 and App. O; code and
configuration files will be released upon acceptance.
Reproducibility summary.Table 12 collects every setting needed to reproduce the measured
results in one place; App. O gives the full specification.
O Full experimental specification
Regime chain.The latent chain over {bull, stagnation, crisis} is built from per-regime persistences
(0.992,0.980,0.978) , with the exit mass split 0.93/0.07 from bull into stagnation/crisis, 0.88/0.12
from stagnation into bull/crisis, and0.35/0.65from crisis into bull/stagnation. This yields
P=
 0.99200 0.00744 0.00056
0.01760 0.98000 0.00240
0.00770 0.01430 0.97800
!
,(2)
whose stationary distribution is (0.669,0.283,0.048) . Crisis self-transition 0.978 gives a mean
crisis episode of about 45 trading days, deliberately longer than the 21-day rebalance interval, since
an episode shorter than the decision interval could not be rotated into by a monthly agent and the
benchmark could not test the paper’s claim. The stationary crisis share of 4.79% implies 71.9 crisis
days in a 1,500-day window; the evaluated path realises 66 (4.4%), an ordinary finite-path deviation.
Realised and stationary prevalence need not coincide, and it is the realised figure that determines how
much crisis data the generator actually saw.
Return law.Returns follow a regime-dependent factor model, ri =µ i(k) +βi(k)F(k) +ϵ i, where
F(k) is a skew-t market factor with asharedchi-square mixing variable, which is what produces
lower-taildependencerather than merely high correlation: assets co-crash. The factor has annualised
drift (0.20,0.01,−0.55) , daily volatility (0.0060,0.0095,0.0210) , degrees of freedom (12,7,3.5)
and skew (0,−0.25,−0.80) across bull, stagnation and crisis; residual cross-correlation among risky
names is (0.10,0.15,0.30) and idiosyncratic volatility is 0.0035 daily. No regime is Gaussian: the
19

Table 12:Reproducibility summaryfor the measured (U3) experiments. All values are taken from
the frozen preregistration and the implementation; the data-generating process, architecture and
verifier are given in full in App. O.
Setting Value
Benchmark
RegimesK3(bull, stagnation, crisis);K∈ {2,3,4}searched
Instrumentsd10, of which3defensive (negative crisis beta)
Transition matrix Eq. (2); stationary(0.669,0.283,0.048)
Regime persistence(0.992,0.980,0.978); mean crisis episode≈45days
Factor drift (annualised)(0.20,0.01,−0.55)
Factor daily volatility(0.0060,0.0095,0.0210)
Skew-tdegrees of freedom(12,7,3.5); skew(0,−0.25,−0.80)
Residual correlation(0.10,0.15,0.30); idiosyncratic vol0.0035
Crisis prevalence4.79%stationary (71.9crisis days per1,500)
Simulated horizon2,200days per seed:756-day warm-up,1,444evaluated
Rebalances69(monthly, every21trading days); embargo21days
Generator and denoiser
Formulation variance-preserving diffusion; predictsε
Denoiser two experts, each45→128→128→10with SiLU
Gateg t =σ(MLP(π t)),3→32→1with SiLU
Input dimension45 =d(10)+time embedding(32) +K(3)
Parameter counts23,690per expert+ 161gate= 47,541total
Diffusion stepsS50; swept over{20,50,100}
Noise schedule linearβfrom10 −4 to0.06overSsteps
ScenariosN{256,512}searched,512default;4,096in the sampling intervention
Return winsorisation|r| ≤0.10(boundsMin the concentration bound)
Training
Schedule12epochs per refit; batch128; Adam; lr2×10 −3
Refit cadence every1,000trading days (2refits per run)
Selection deflated Sharpe, computed within the walk-forward
Verifier
Method adaptive conformal inference (42, 69)
Target miscoverageδ= 0.10(90% long-run act-time coverage)
BudgetB= 3; per-attempt levelδ/B≈0.033
Scores t Definition 1;|realised tail loss−scenarioCVaR α|
Calibration window60scores (rolling); ACI step size0.01
Fallback stationary block bootstrap into the same CVaR-QP
Decision and evaluation
Constraints long-only, fully invested; box[0,0.25]; turnover≤0.20per rebalance
Costs8bps proportional
CVaR levelα0.95default;α∈ {0.90,0.95,0.99}searched
Risk-free raterf=0primary on U3; oracle hierarchy atrf=1.6%(App. Q)
Solver CLARABEL via CVXPY (≥1.4), SCS fallback; no overrides set
Solver tolerances CLARABEL gap/feas. tol.10 −8,max_iter= 200;
SCSε abs=εrel=10−4,max_iters= 10 5
Hyperparameter grid2,916configurations×5seeds= 14,580(App. T)
Ablation arms−verifier,−memory,−MoE,−CVaR term,B=1
Seed registry Table 14
20

tails thicken and the skew steepens monotonically from bull to crisis. Of the d=10 instruments, 3 are
defensive, with near-zero normal beta andnegativecrisis beta (a flight-to-quality corner), and a lower
unconditional carry (0.8% annual) than the risky names. Both properties are load-bearing: without a
defensive corner the allocator is always fully invested in statistically identical assets, equal weight
is optimal by construction, and regime-conditioning has nothing to earn; without the carry penalty,
holding the defensive assets always would dominate and regime-timing would again be worthless.
Denoiser.Each of the two experts is a three-layer MLP 45→128→128→10 with SiLU
activations, where the 45-dimensional input concatenates the noisy return vector ( d=10), a 32-
dimensional sinusoidal time embedding, and the K=3 regime posterior. The gate is 3→32→1
with a sigmoid output, combining the experts as ˆεθ = (1−g t)ˆεbase θ +g t ˆεcrisis θ so the weights sum to
one by construction. Exact parameter counts are 23,690 per expert and 161 for the gate, 47,541 in
total; the −MoE ablation drops the crisis expert, leaving 23,851. Diffusion uses S=50 steps with
β linear from 10−4 to 0.06. For the reported baseline and ablation table the generator is trained for
12 epochs per refit, batch 128, Adam at lr 2×10 −3, and refit every 1,000 trading days, givingtwo
refits per run.Two other scripts in the released code, the smoke test and an early ablation sweep,
use a different generator budget (25 epochs, refit every 504 trading days) and are not the source of
any reported number; the values here are those behind Table 8, and they are the values used by every
measured arm (diff_epochs=12,retrain_every=1000).
Verifier, operationally.The score of Definition 1 is computed exactly as Definition 1 states. The
verifier keeps a rolling window of the 60 most recent scores, takes the empirical (1−β t)-quantile of
that window as the certificate width qt, targets miscoverage δ=0.10, and updates the running level
online by βt+1 =β t +γ ACI (δ−1{s t > qt}) with step size γACI = 0.01 and β0 =δ/B . Attempts
are capped at B=3 and each is evaluated at δ/B≈0.033 ; the first passing attempt is accepted. If
no attempt passes, or if the solve fails, the system falls back to a stationary block bootstrap whose
scenarios are solved by thesameCVaR-QP.
Why (C5) is not a technicality, and what would discharge it.The gap in (C5) is structural rather
than a missing lemma. Our score is a single-realisation residual |ℓt+1 − \CVaRα|, and CVaRα is
not elicitable: no scoring function has CVaRα as its unique minimiser ( 29), so no one-sample
residual can identify it, and no amount of conformal calibration on such a score can be made to bound
|CVaRpθ α −CVaR P α|. This is why we mark (C5) unproved rather than deferred: as specified, it is not
provable.
There is, however, a constructive route, and we state it because it prescribes a concrete change to
the verifier; no reported run is reinterpreted by it. Thepair (VaRα,CVaR α) isjointly elicitable,
via the Fissler–Ziegel class of strictly consistent scoring functions (28). A verifier that scored the
model’s (VaR,CVaR) pair under an FZ-consistent loss would inherit strict consistency, and under
the accompanying strong-identifiability condition an excess-score bound converts into a bound on the
population discrepancy, supplying exactly the bridge (C5) assumes. We did not run this variant, so
we register it as the repair our own diagnosis implies, in the same spirit as §4.3: the protocol convicts
the paper’s theory as well as its generator.
What st is and is not. st is anobservableabsolute one-step discrepancy between a scenario CVaR
estimate and a single realised loss. It is not an estimate of the population quantity|CVaRpθ α −CVaRP α|,
and a single realised return cannot reveal that quantity. The link between the calibrated quantiles
of {sτ } and the population discrepancy is exactly the identification condition that the conditional
certificate statement 1 assumes and that we do not prove (App. W).
Allocator and solver.The convex program (5) is solved through CVXPY withCLARABELas the
primary interior-point solver andSCSas the fallback, invoked only if the primary solve raises. No
tolerance, iteration or polish setting is overridden anywhere in the code, so each solver’s compiled-in
defaults apply. We state them here so the PDF is self-contained: CLARABEL uses absolute and
relative duality-gap tolerances and a feasibility tolerance of 10−8 with a 200-iteration limit; SCS uses
εabs =ε rel = 10−4 with a 105-iteration limit. The released dependency specification pins CVXPY
≥1.4 , the first release in which CLARABEL is the default conic solver, and CLARABEL and SCS
enter as transitive dependencies of that pin. The solver reports one of three outcomes per rebalance: a
normal solve, a fallback solve, or, if no weight vector is returned, status FAILED, in which case the
21

committed action is the previous feasible portfolio wt−1. FAILED did not occur in any reported run.
Returns are winsorised at|r| ≤0.10, which also boundsMin the concentration term of Lemma 2.
Post-solve cleanup: what it does and does not guarantee.The solver’s solution wsol is clipped to
the box and renormalised to sum to one before it is committed. This is numerical cleanup and ano-op
at an exact solution, but it is post-processing, and we state its guarantee precisely because an earlier
draft overstated it. Clipping alone gives ℓ≤w i ≤u . The subsequent division by P i wi restores the budget exactly and, with ℓ=0 as here, preserves non-negativity, but it isnotfeasibility-preserving
in general. If the clipped vector sums to s <1 every coordinate is scaled up by 1/s, which can
lift one above u; for ℓ >0 and s >1 the symmetric violation is possible at the lower bound; and
rescaling changes ∥wt −w t−1∥1, so the turnover cap can be breached too. Nor do we claim a general
perturbation bound. Renormalisation rescaleseverycoordinate by 1/s, so the displacement it induces
grows with the dimension and with how close the active coordinates sit to their bounds; bounding
it would need assumptions we have not stated. What we rely on is that the solver residuals are
numerically small, so the post-processing perturbation was small in the reported runs, and, decisively,
on the explicit audit. No theoretical guarantee is doing any work here. The paper’s feasibility claim
is therefore checked, not constructed: the “Infeas.” column of Table 11 is a post-hoc audit of every
committed weight vector against the budget (10−4), box (10−6) and turnover (10−4) tolerances, and
it is zero for every executed arm and seed. That is evidence, not a guarantee. “Verifiable provenance”
likewise means the solve is reconstructible from the log, not that a certificate has been re-derived for
a post-processed vector: the logged KKT duals certifyw sol, not the clipped iterate.
The variant that would restore the guarantee (registered, not run).The clean design does
not post-process at all. The trusted validator should check the budget, box and turnover residuals
of wsol against fixed tolerances and commit wsol only if all three pass, invoking the predefined
block-bootstrap fallback otherwise. That variant is better on two counts: every committed action is
feasible to a stated tolerance by a check thevalidatorowns rather than by a numerical convenience,
and the committed vector is the solver’s own iterate, so the logged KKT record certifies the action
actually taken and the wsol-versus-wt distinction of Prop. 3 disappears. A Euclidean projection onto
the full constraint set would also restore feasibility, but it is a second optimisation whose output
carries no KKT record from the first, so it reintroduces the gap it closes. We ran neither: every
number in this paper comes from the clip-and-renormalise pipeline described above, and we register
the change rather than retrofit it, exactly as we do for the (C5) scoring change above.
Action-space partition (detail for §4.5).Theuntrusted, controller-settable parameters are the
objective and generator parameters (K, N, η, q, λ, γ, λµ, α); none of them can enlarge the feasible
set, so a corrupted controller can degrade decisionqualitybut not admissibility. Thetrusted, validator-
owned parameters are the constraint parameters (ℓ, u, τ)and the refinement budget B. The validator
clips any untrusted value to its preregistered range and rejects any attempt to name a constraint
parameter.
Controller.The controller is atransparent rule plus a contextual bandit(LinUCB-lite) over the
preregistered grid; no LLM is involved. The rule keys off the crisis posterior πt,crisis: above 0.35
it sets η=3.0, α=0.99, γ=1.5, q=0.10 and λµ=4 (risk-off); between 0.15 and 0.35 it sets η=2.0,
α=0.95, λµ=12; below 0.15 it sets λµ=24 (risk-on). The bandit then refines {η, γ, λ, λµ} within
the grid, keeping per-(regime,knob,value) reward means and exploring uniformly with probability
ε= 0.15 . Every value it can emit is inside the preregistered ranges, and the validator clips anything
outside them.
Regime detector.A Gaussian HMM ( hmmlearn) with K states on z-scored features,
covariance_type="diag", n_iter= 200 , tol= 10 −4, and4 random restartsscored
by log-likelihood with the best retained; restart seeds are seed+ 13r . The offline regime-scoring
used for the detectability calibration of Fig. 4(d) instead uses covariance_type="full" with
tol= 10−3 and the same restart count.
Baseline tuning.The scenario-fed baselines (historical CVaR, DRO-CVaR, Gaussian, stationary
block bootstrap) areuntuned by construction: they feed the same CVaR-QP at the same α, box,
turnover cap and costs, so only scenario quality differs. The classical baselines take their standard
22

0 1000 2000 3000 4000
day
100
2×100
NAV (equal weight)
(a) ground-truth regimes
crisis
stagnation
8
 6
 4
 2
 0 2 4 6
daily return (%)
10 3
10 2
10 1
density (log)
(b) fat left tail in crisis
bull
stagnation
crisis
bull stag. crisis0.0
0.2
0.4
0.6
0.8coefficient
(c) diversification fails in the tail
mean corr.
tail dep.
0.0 0.2 0.4 0.6 0.8 1.0
regime_separation
0.3
0.4
0.5
0.6
0.7HMM balanced accuracy
chance
(d) detectability dial
balanced acc.
Figure 4: The U3 benchmark, drawn on anillustrative 4,536-day pathfrom the same generator
(panel (d) uses 2,600-day paths per seed); this is for visualising the data-generating process and isnot
the evaluated horizon, which is 2,200 days per seed (756 warm-up, 1,444 evaluated).(a)ground-truth
regimes;(b)crisis returns are fat-tailed and left-skewed;(c)correlationsandlower-tail dependence
both spike in crisis, so diversification fails exactly when it is needed;(d)the detectability dial: at
regime_separation= 0balanced accuracy equals chance (1/3) by construction.
forms with no free parameters beyond the shared constraints, except HRP, which uses the standard
single-linkage correlation-distance clustering, and the block bootstrap, whose block length is 21 days
(one rebalance interval).
Attacks, operationally.A1 randomises λµ and γ within [0,30] ; A2 flips the HMM regime posterior;
A3 bypasses the conformal gate (it does not touch the validator); A4 maximises turnover. None of the
four modifies the trusted validator, which is why the feasibility result they support excludes validator
compromise (A5, not executed).
P Problem setup, tools, and the agent loop
At rebalance date t, let Rt ∈R d be observed returns and wt ∈R d portfolio weights satisfying the
budget, box, and turnover constraints
1⊤wt = 1, ℓ≤w t ≤u,∥w t −w t−1∥1 ≤τ.(3)
Regimes follow a K-state Gaussian HMM with latent state St and posterior πt,k =P(S t=k|R 1:t).
All estimation is strict walk-forward. ARC-AGENTorchestrates three specialist tools, treated as
fixed, trusted backbones; the controller and evidence-filter layer (§3) sits around them.
Tool A: Regime detector.Fit/update the HMM on {Rs}s≤t and emit πt and a context vector zt
encodingarg max k πt,k and recent statistics.
Tool B: Scenario generator.A variance-preserving, regime-conditioned diffusion model with a
tail-weighted objective. With ˜ℓ=−min j rj a portfolio-free adverse proxy,
Ltail =E
h
1 +η1{ ˜ℓ≥Q 1−q(˜ℓ)}  ∥ε−ε θ(·)∥2 2 i , q∈[0.05,0.10], η∈[1,3],(4)
The denoiser is a two-expert (mixture-of-experts) network, ˆεθ = (1−g t)ˆεbase θ +g t ˆεcrisis θ whose gate
gt =σ(MLP(z t)) increases with the crisis posterior. At deployment it draws N scenarios {r(i) t+1}
conditioned onz t.
23

Algorithm 1ARC-AGENT: one rebalance at datet
1:input:historyR 1:t, previous weightsw t−1, refinement budgetB
2:π t, zt ←REGIMEDETECTOR(R 1:t)▷Tool A; strict walk-forward
3:a t ←CONTROLLER(z t,memory)▷config only; validator clips to preregistered ranges
4:b←0
5:repeat
6:{r (i) t+1}N i=1 ←GENERATOR(z t;a t)▷Tool B
7:pass←VERIFIER({r (i) t+1},{s τ }τ <t, δ/B)▷conformal gate, Prop. 2
8:b←b+ 1;if¬passthena t ←REFINE(a t)
9:untilpassorb=B
10:if¬passthen
11:{r (i) t+1} ←STATIONARYBLOCKBOOTSTRAP(R 1:t)▷fallback
12:end if
13:(ˆµt, ˆΣt)←blended, shrunk moments of{r (i) t+1}
14:w t ←arg minof the convex QP (5) subject to (3)▷Tool C
15:s t ←realized calibration score oncer t+1 is observed
16:log(π t, at,verifier outcome,active set,KKT duals)
17:returnw t ▷feasible by Prop. 3; KKT record is forw sol
Note on the indicator (corrected).An earlier draft printed Eq. (4) with 1{˜ℓ≤Q q(˜ℓ)}, which
up-weights theleastadverse samples, the opposite of the intent. Theimplementationwas always
correct; the equation was not. We verified this rather than asserting it: the up-weighted set has
mean return −107 bps and is 2.9× enriched in crisis days, whereas the erroneous indicator would
have selected samples averaging +106 bps. The audit script will be released upon acceptance. The
29% mean-collapse result is therefore not an artefact of an inverted indicator, and η is ruled out
independently (§5.3).
Tool C: CVaR allocator.With per-scenario loss ℓi =−w ⊤r(i) t+1 and blended, shrunk moments
(ˆµt, ˆΣt), solve the convex epigraph QP
min
w,ζ,{s i}
−λ µ ˆµ⊤ t w+γ w ⊤ ˆΣtw+ζ+ 1 (1−α)N
NX
i=1
si (5)
s.t.s i ≥0, s i ≥ℓ i −ζ, i= 1, . . . , N,
1⊤w= 1, ℓ≤w≤u,∥w−w t−1∥1 ≤τ.
The objective is a convex QP (quadraticw⊤ ˆΣtw plus a CVaR epigraph withO(N) affine constraints);
interior-point solves scale as O(d3 +N d2). We use the Rockafellar–Uryasev CVaR at levelα=0.95
and shrink ˆΣt toward the identity (54). The KKT system logs active constraints, tail weights, and
duals at each rebalance, the substrate for governance in §4.5.
The agent loop.Algorithm 1 states the plan–act–verify–refine loop of §3 in full. Configurations
are code-as-action: the controller may set objective and generator parameters, never weights and
never constraint parameters, which the trusted validator owns (§4.5).
Q Full evaluation protocol and metric registry
We evaluate ARC-AGENTunder a deliberately broad protocol built to stress nonstationarity across
universes and windows; the protocol and synthetic benchmark will be released as a reusable testbed
upon acceptance.
What we run, and what we only register.We report measured results onU3 only. U3 is a
controllable synthetic regime-shift benchmark withground-truth latent regimesand tunable crisis
frequency, severity, duration, and detectability. Among the testbeds available to us it is the only
contamination-free one: no pretrained model can have memorised its regimes, and the true state is
24

known, so regime inference can be scored directly and anoracle boundcan be computed exactly
(§5.1). Neither property is available on historical data.
Two historical universes arepreregistered as protocol and deliberately not run:(U1)a point-
in-time cross-asset ETF panel respecting inception dates (TIP 2003, EEM 2003, commodity ETFs
2006+, VXX 2009; a ∼40-instrument diversified panel does not exist before the mid-2000s), and
(U2)a large-cap equity panel from point-in-time index membershipincluding delisted names. We did
not execute U1 or U2 in this study, preserving them for a separately preregistered evaluation with
independently frozen universe-construction and data-cleaning rules, and no empirical claim in this
paper is based on either. App. S records the frozen U1/U2 protocol for transparency.
Horizon and walk-forward (U3, measured).Daily simulated returns over 2,200-day paths, a
756-day warm-up, monthly rebalancing, and 69 evaluated rebalances per run. Estimation is strict,
purged, and embargoed walk-forward (53); the expanding walk-forward yieldsmultipleOOS sub-
periods. Per-instrument transaction costs of 8 bps and an ℓ1 turnover cap ∥wt −w t−1∥1 ≤0.20
per rebalanceare applied identically to all methods. Because U3 is synthetic there is no risk-free
series and no calendar: Sharpe is reported on excess return with rf=0 , and the rf sensitivity of the
headline contrast is reported in App. V.
Horizon and walk-forward (U1/U2, registered, not run).Were the historical universes executed,
they would use daily total returns over2007–2025(the earliest date at which U1 exists as a diversified
panel), the same purged and embargoed expanding walk-forward, monthly rebalancing, and three
predeclared crisis windows (2008–09, the 2020 COVID crash, and the 2022 inflation shock) as stress
slices, with Sharpe taken net of the 3-month T-bill (rf≈1.6% over that span).None of these settings
bears on any number reported in this paper; they are recorded so that a future execution is bound by
them.
Baselines (eleven, all implemented and reported).Classical(five): equal weight, risk parity,
minimum variance, mean–variance (57), hierarchical risk parity (52).Robust / scenario(four) → the
sameCVaR-QP, so only scenario quality differs: historical CVaR, DRO-CVaR, a Gaussian scenario
model, and a stationary block bootstrap.Agentic controls(two): a rule-based weights-emitting
agent with no symbolic solve, and the same agent with a projection onto the feasible set. Neither
is a language-model agent; no LLM was executed in this work. All allocator-fed methods share
ARC-AGENT’s box, turnover cap and costs. Results appear in Table 8 (four), Table 11 (two) and
Table 9 (five).
We do not report TimeGAN (68), TimeV AE (38), TSDiff (50), DeepAR (61), or TFT (55). Each is a
substantial model, and a half-trained instance would not be a fair comparator. Reporting numbers
that were not measured would violate the reporting discipline of this paper; we state the omission
rather than fill the row.
Method registry.Table 13 listseverymethod, ablation, oracle and control that appears anywhere in
this paper, with the single place each is reported. It exists so that the counts in the text can be audited
against the tables:eleven baselines(five classical, four scenario-fed, two rule-based controls), one
diagnostic comparator, three ARC-AGENTarms, and the oracle and intervention rows. The two
control arms are counted once, as baselines; they reappear as comparison rows in Table 11 rather
than as additional methods.
Seed and uncertainty registry.Seed counts differ across tables because the experiments were run
at different stages of the project, and we report that rather than harmonise it retrospectively. Table 14
states, for every table and figure, the number of seeds, whether the comparison is paired under
common random numbers, and what the reported ± means. We label every experimentconfirmatory
(paired, common random numbers, 10–24 seeds) orexploratory( 5–6 seeds), and we do not claim
that every headline result is confirmatory: the oracle hierarchy and the stage interventions are, while
the main baseline table, the red-team table and the 23 factorial, including the interaction estimate, are
exploratory and should be read as such.
Significance.We assess Sharpe and CVaR differences with a stationary block bootstrap ( R=104
replications; we reserve B for the refinement budget), Diebold–Mariano tests ( 39) on per-period
loss differentials, and thedeflated Sharpe ratio( 53) to correct for selection bias.Trial counting:
25

Table 13:Method registry.Every method in the study, its family, whether it is fed by the shared
CVaR-QP, and where it is reported. “Not reported” means implemented butnot executedfor this
version, so no outcome has been observed; nothing here was run and then withheld.
Method Family CVaR-QP Reported in
Equal weight baseline (classical) n/a Tab. 8
Minimum variance baseline (classical) n/a Tab. 8
Risk parity baseline (classical) n/a Tab. 9
Mean–variance baseline (classical) n/a Tab. 9
Hierarchical risk parity baseline (classical) n/a Tab. 9
Historical CVaR baseline (scenario)✓Tab. 9
DRO-CVaR baseline (scenario)✓Tab. 9
Gaussian scenario model baseline (scenario)✓Tab. 8
Stationary block bootstrap baseline (scenario)✓Tab. 8
Weights-emitting control baseline (rule-based control) n/a Tab. 11
+projection baseline (rule-based control) n/a Tab. 11
Regime-cond. bootstrap diagnostic comparator✓Tab. 8
ARC-AGENT(full) proposed✓Tab. 8, 11
−verifier ablation✓Tab. 8
−CVaR term ablation✓Tab. 8
−memory ablation✓not reported
−MoE (single expert) ablation✓not reported
B=1(no refinement) ablation✓not reported
L0–L3 oracle hierarchy oracle (4 rows)✓Tab. 10
I0–I2 interventions intervention (3 rows)✓Tab. 5
23 factorial arms intervention (8 cells)✓Tab. 6
Table 14:Seed and uncertainty registry.“Paired” means the arms share return paths under common
random numbers, so the reported interval is on the contrast rather than on the level. Confidence
intervals on paired contrasts are 95% percentile intervals from a bootstrap overseeds( R= 10,000
replications); because time is paired under common random numbers, resampling is over seeds, not
over time. The stationary block bootstrap (block length 21 days) is a separate procedure applied to
time-seriesSharpe and CVaR differences (App. Q), and the two should not be conflated. The last
column of the table states which experiments are confirmatory and which are exploratory.
Where Quantity Seeds Paired±denotes Status
Tab. 8 Sharpe by method 5 no across-seed s.d. exploratory
Tab. 5 Sharpe by intervention 10 yes standard error confirmatory
Tab. 6∆Sharpe, channels 6 yes95%CI exploratory
Tab. 10 oracle Sharpe 24 yes point estimates confirmatory
Tab. 11 Sharpe under attack 5 no across-seed s.d. exploratory
Tab. 9 remaining baselines 5 no across-seed s.d. exploratory
Fig. 2(a) oracle frontier 24 yes±1s.e. confirmatory
Fig. 2(b) stage interventions 10–16 yes95%CI confirmatory
Fig. 2(c) factorial 6 yes95%CI exploratory
Fig. 3 oracle frontier 24 yes±1s.e. confirmatory
§5.2 perception intervention 16 yes95%CI confirmatory
§5.1 L1, L2 paired headroom 24 yes95%CI confirmatory
§5.1, App. V L2 headroom,rfsweep 12 yes95%CI confirmatory
§5.3 repaired-generator Sharpe 6 yes95%CI exploratory
26

the effective number of trials is not the handful of rows we report but the full preregistered search:
the configuration grid (K, N, η, q, λ, γ, α, λµ) crossed with seeds, giving the 14,580 enumerated
in App. T. Ablations and baselines areexcludedfrom that count because they do not search the
grid. Deflating against the reported rows would understate the multiplicity; we deflate against the
enumerated count and report that a substantial part of our nominal advantage does not survive it.
Metrics.Portfolio: CAGR, volatility,Sharpe net of the risk-free rate(on U1/U2 the 3-month
T-bill; on U3, rf=0 ; reporting excess-return Sharpe matters because a positiverf deflates all Sharpes
and differentially flatters low-volatility strategies, i.e. ours, which is why App. V reports the headline
contrast at rf=0 , rf=1.6% and rf=3% ), Sortino (downside deviation below zero excess return),
MaxDD, Calmar, tail ratio, andturnover reported as mean per-rebalance ∥∆w∥1 (not annualised),
so it is directly comparable to the 0.20 cap.Scenario calibration: KS, energy score (ES), variogram
score (VS), CRPS ( 43), VaR unconditional and conditional coverage ( 51, 36), and CVaR error
(bps), all reported asconfidence bounds at the corrected levelof Prop. 2, not as p-values (§4.4).
Agentic-value, defined precisely:
•Rejection rate: fraction of rebalances where the first scenario set fails the certificate.
• Catch rate: fraction where refinement was triggeredandsubsequently improved calibration.
These are distinct quantities and we report both; conflating them (reporting the rejection rate
under the name “catch rate”) would overstate the verifier’s usefulness.
• Re-planning regret: 1 T P t[F t(wagent t )−F t(woracle-config t ) ], the mean QP-objective gap between the configuration the controller chose and the best configuration in the grid in hindsight, in
objective units. Negative means the controller beat the bestfixedconfiguration by adapting.
•Tool-call budget: mean tool invocations per rebalance.
Wedo notreportsolver-record availability(elsewhere loosely “provenance completeness”) as a
headline metric. It records whether the convex solve emitted a complete active-set and KKT record for
wsol, not that the committed wt is KKT-optimal, and it is100% by construction for any solver-backed
agent and 0% for any that is not, so it carries no information about quality (indeed the −verifier
ablation attains100%; see §6). We report it once, as a property, not as a result.
ARC-AGENTvariants and ablations.All executed variants use therule-plus-contextual-bandit
controller;no LLM controller variant was run, so no rule-versus-LLM comparison appears anywhere
in this paper. The preregistered ablation family has five arms, and we state the status of each once,
here: −verifier(accept the first scenario set) and −CVaR termareexecuted and reportedin Table 8;
−memory, −MoE(single expert) and B=1 (no refinement) are implemented and runnable but were
not executed for this version, so no outcome for them has been observed by us or withheld. We record
this as a disclosed deviation from the analysis plan: it registered five ablation arms and we report two.
No outcome is claimed for the three unexecuted arms anywhere in the paper. This list supersedes any
partial enumeration elsewhere.
R Cost, latency, and failure modes
A recurring objection to modular generative pipelines is compute. We quantify it rather than concede
it.
Measured cost.The pipeline records wall-clock time per rebalance. Each rebalance performs an
HMM posterior update, N=512 diffusion samples, verification, and one convex solve; diffusion
sampling dominates. The generator is refit every 1,000 trading days, so a run performs 2 refits
of 12 epochs each rather than one per rebalance (Table 12; App. O notes that other scripts in the
released code use different generator budgets). The entire measured protocol (allexecutedbaselines
and ablations at five seeds, the red-team suite, the oracle sweep and the figures) reproduces in
approximately 25 minutes on a single CPU core, which is the measured compute cost of this study;
no GPU is required. A monthly rebalancing interval is≈2.6×10 6 s, so the solve occupies
0.55 s
2.6×10 6 s ≈2×10 −7
27

of the decision interval, aboutone part in five million, not the ∼10−5 an earlier draft reported.
Inference is therefore not compute-bound for the cadence it targets; training, which is excluded from
this figure, is the real cost.
Evaluation length.Each U3 run uses a 756-day warm-up followed by 1,444 evaluated trading
days, rebalanced monthly (21 trading days), giving 69 rebalances per run. The 2007–2025 calendar,
the historical risk-free rate, and the 2008–09/2020/2022 crisis windows belong to theregistered,
unexecutedU1/U2 protocol (App. Q) and bear on no number in this paper.
Inference is negligible; refitting is the dominant computational cost.Within a run, the per-
rebalance work (sampling, verification, solve) is small relative to the two generator refits. The 14,580
figure of App. T is an enumerated multiplicity count used to deflate Sharpe; it is not a count of
executed runs, and we do not claim to have trained 14,580 generators. What we actually executed
is the set recorded in Table 14: twelve method arms at five seeds for Table 8, seven arms at five
seeds for the red-team suite, and the oracle and intervention sweeps, which require no generator at
all. Deflating against the full preregistered grid is deliberately conservative, and is preferred here to
deflating against a count of runs that happened to finish. We report no LLM latency or token figures,
because no LLM was executed (App. L). The seed counts we report are a choice we should have
made differently; compute was never the constraint. As Table 14 records, they still range from 5 to
24: the oracle hierarchy is paired over 24 seeds and the stage interventions over 10–16, but the main
baseline table (Table 8), the red-team table (Table 11) and the factorial (Table 6) rest on5, 5 and 6
seeds respectively. We treat the 24- and 10–16-seed paired contrasts as confirmatory and the 5- and
6-seed tables as exploratory, and every claim drawn from the latter is labelled accordingly rather than
argued around.
S Universe construction (registered, not run)
U1 would be built point-in-time: an instrument enters only after its inception date and only if it meets
a liquidity floor at t, so the panelgrowsfrom ∼14 instruments (2007) to ∼40 (2015 onward), and
d is time-varying. U2 would use point-in-time index membership including subsequently delisted
names.Neither was run.We register the construction so that a future execution is bound by it, and
so that our own claims cannot quietly expand to cover data we never touched.
T Enumerated trial count
Deflating a Sharpe ratio requires the number oftrials, not the number of reported rows. Our frozen
preregistration enumerates the grid K∈ {2,3,4}, N∈ {256,512}, η∈ {1,2,3}, q∈ {0.05,0.10},
λ∈ {0.3,0.5,0.7}, γ∈ {0.5,1.0,1.5}, α∈ {0.90,0.95,0.99} and λµ ∈ {4,12,24}. The Cartesian
product is 3·2·3·2·3·3·3·3 =2,916 configurations, and with the five registered seeds this is
14,580 grid-by-seed combinations, the count passed to the deflated-Sharpe calculation. This is an
enumerated multiplicity count, not a tally of executed runs, and it is used in that sense everywhere in
the paper. No configuration is pruned. The preregistration also records an upper bound that treats
eachcombinationof ablation arm and controller arm as a separate search: five ablation arms ×
two controller arms = 10 families, giving 10×14,580 = 145,800 . We deflate against the core
14,580, not against that bound, because ablations and baselines do not search this grid; the upper
bound is recorded only so that a reader can see the most adverse reading. Deflating against the eight
rows of Table 8 would understate selection bias by three orders of magnitude, and is a common and
consequential error. At this trial count none of the performance margins in Table 8 survive deflation,
which is consistent with, and reinforces, our headline negative result.
Preregistration amendment (disclosed).One amendment (PR1) was recorded after freezing and
before any hypothesis outcome was inspected: the range of λµ was widened from [0,2] to [0,30] .
Reason: at a daily horizon the CVaR term ( ∼10−2) is ∼33× the return term (∼3×10 −4), so the
original bound made the return/risk trade-offinexpressible: the objective degenerated to pure CVaR
minimisation and the agent performed no regime rotation at all. This is a specification bug; the
preregistration was re-frozen with a new hash. The amendment, the hashes and the audit scripts will
be released upon acceptance.
28

Table 15:Interventional attribution, measured.Shapley values and Shapley–Taylor interaction
indices computed from the complete 23 coalition table (Table 6; 6 seeds, paired, 95% CI by seed
bootstrap).The two blocks are alternative attribution summaries, not additive pieces of one
decomposition: block A already sums to v(N) = +0.218 exactly, as efficiency requires, and block
B is a further diagnostic of non-additivity that must not be added on top of it. Covariance is inert with
tight intervals throughout. The mean×scenario interaction is 55% of v(N) as a point estimate and
thetotalpairwise interaction share is 54%; both are underpowered at six seeds. These are descriptive
attribution summaries: neither the interaction magnitude nor the conditional contribution of the mean
channel is established by them.
ϕ95%CI share ofv(N)
A. Component credit(Shapley values; sum tov(N))
conditional meanˆµ+0.080±0.178 36.8%
scenario tail/dependence+0.139±0.086 63.8%
covariance ˆΣ−0.001±0.002−0.6%
B. Interaction diagnostics(Shapley–Taylor indices;notadded to A)
mean×scenarios+0.120±0.184 55.3%
mean×covariance−0.002±0.002−0.9%
covariance×scenarios−0.001±0.003−0.3%
higher-order (three-way)−0.003n/a−1.5%
total pairwise interaction share54.1%ofv(N)
U Attribution: full coalition table
Efficiency (P i ϕi =v(N) ) holds without approximation here because the coalition table is com- plete: no Monte-Carlo sampling over permutations is needed for three modules. That exactness is
combinatorial rather than statistical: each v(S) is a six-seed paired estimate, so the ϕi inherit six-seed
uncertainty, which is what the intervals in Table 15 report. The same computation on an incomplete
table would additionally require estimating v(S) for unrun coalitions, which is exactly the step at
which attribution studies usually become assumption-driven.
Two summaries, not one decomposition.Block A of Table 15 partitions v(N) among the three
channels. Block B measures how much of v(N) is attributable tonon-additivitybetween them. A
channel’s Shapley value already absorbs its share of the interactions it participates in, so the two
blocks describe the same coalition table from two directions and cannot be concatenated into a single
bar chart of additive shares. Figure 2(c) plots both, and its caption says so.
V Representation of information and action
§5.1 varies the action set at fixed information. The general object is a lattice indexed by an information
set I and an action set A, with J ⋆(I, A) = supπ∈Π(I,A) J(π) . Our L0–L3 hierarchy is the column
I={true regime path}of that lattice.
Proposition 1(Lattice monotonicity).IfI 1 ⊆I 2 andA 1 ⊆A 2 thenJ ⋆(I1, A1)≤J ⋆(I2, A2).
Proof. Any π∈Π(I 1, A1) is measurable with respect to I1, hence with respect to I2 ⊇I 1, and takes
values in A1 ⊆A 2; so Π(I1, A1)⊆Π(I 2, A2) and the supremum over the larger set is at least as
large. The argument requires only that additional information and additional actions may beignored,
which holds becauseΠis defined by measurability and range constraints alone.
The proposition itself is immediate; the content is its experimental implication. A low headroom
estimate in one information–action cell cannot establish that the information has little value, and a
rise in headroom when the action set is widened at fixed information shows that the earlier negative
conclusion came from representational restriction. §5.1 is exactly that situation: L1 gave+0.07±0.08
and L2 gave +0.28±0.08 on identical information. Reporting a single oracle number reports one
cell of this lattice without saying which.
29

The three headroom numbers, side by side.Three quantities describe the L2 headroom and
are easy to read as inconsistent, so we state each with its provenance.(a)Thepaired same-path
Sharpe differenceL2 −L0 is +0.28±0.08 (24 seeds, common random numbers, 95% CI over seeds),
computed, like every level in Table 10, at the preregisteredrf=1.6% .(b)The same contrast in the
twelve-seed rf sweep (seed registry, Table 14) is+0.248 at rf=0 , +0.263 at rf=1.6% and +0.275
at rf=3% ; §5.1 quotes the first of these as +0.248, while the abstract and Table 10 quote (a). (a) and
(b) differ in seed count and in rf , not in what they measure, and neither is a correction of the other.
(c) +0.38 is not a paired difference against L0 at all: it is theverticalexcess of L2 over the static
EW–MinVar frontierat matched drawdown, the “Excess” column of Table 10 and the gap drawn
in Fig. 2(a). (a) and (b) compare two policies on the same paths; (c) compares one policy against
a frontier at its own realised risk. A reader who subtracts (c) from (a) is subtracting two different
comparisons.
W Conditional validity and unidentified steps
We label this appendixjustificationrather thanproofs: it composes three standard results under
Assumption 1 and states explicitly, at the end, the one step we have not proved.
Assumption 1(Conditions for the conditional certificate statement 1).(C1) Bounded loss.The
portfolio loss −w⊤r is bounded by M uniformly over the feasible set of (3), and the N scenarios
are drawn i.i.d. from pθ(· |zt) given zt.(C2) Strong convexity.The objective (5) is Γ-strongly
convex in w on the feasible set, with moment sensitivities (λµ, κΣ) and moment errors (δµ, δΣ) as in
Lemma 1.(C3) Score construction and approximate local exchangeability.The calibration score
st is the absolute realised-versus-scenario CVaR discrepancy of Definition 1, computed fromrt+1
after wt is committed, so it is not used to select wt; the score sequence is approximately locally
exchangeable in the sense adaptive conformal inference is designed to tolerate ( 42, 69). We do
not verify this empirically.(C4) Selection correction.At most B refinement attempts occur per
rebalance and each attempt is evaluated at level δ/B (Prop. 2).(C5) Score-to-CVaR identification.
There exists a monotone link between the calibrated quantiles of {sτ } and the population discrepancy
|CVaRpθ α −CVaR P α|, so that coverage of the former bounds the latter.We do not prove this, and
everything below is conditional on it.(C6) Per-attempt marginal validity.Each candidate attempt
satisfies the stated marginal validity conditionbeforeadaptive selection, so that the union bound of
(C4) applies.We do not establish thisfor the implemented proposal mechanism.
Under (C1)–(C6), which include the unproved score-to-CVaR identification (C5) and per-attempt
validity (C6), the certificate below is along-runstatement: the guarantee is over the empirical
frequency of covered rebalances, never over a nominated one. We use “per-rebalance” only to
describe theformof the bound, never its validity.
Three properties follow. (i) The verifier is load-bearing: qt is computedfrom the verifier’s realized
scores, so the bound cannot even be evaluated without running it. (ii) It bounds model error, by
calibrating against P-outcomes rather than pθ-samples. (iii) The refinement correction does real work.
The body summarises the conditional certificate statement 1 and Prop. 2 without proof; the full
development follows.
The allocator’s stability under objective perturbation is standard; the substantive question is what the
verifier can certify about the gap between the optimised objective and the objective under thetrue
distribution. We first isolate that gap, then show why a Monte Carlo bound cannot close it, then close
it with a conformal certificate calibrated on realized outcomes.
The two error terms.Scenarios are drawn from the generator pθ(· |zt), not from the true law P,
so the CVaR error that the allocator’s regret depends on decomposes into a sampling term (S) and a
model term (M). Term (S) shrinks with more scenarios; term (M) is the generator’smiscalibration
and does not shrink with N at all. Term (M) is the entire reason the verifier exists, and it is the one
a concentration inequality on pθ-samples cannot touch: such a bound certifies only that we have
sampled our own generator faithfully.
Lemma 1(Allocator stability).If (5) is Γ-strongly convex in w and its moment and CVaR terms
differ from truth by (δµ, δΣ, δCVaR), then F( ˆw)−F(w⋆)≤ 1 2Γ (λµδµ +κ ΣδΣ +δ CVaR)2. This is standard; the content is what boundsδ CVaR, below.
30

Lemma 2(Sampling error, term (S)).For the bounded linear loss class {−w⊤r:∥w∥ 1 ≤C} with
|L| ≤M, a Rademacher bound for the empirical tail average (34, 65, 63) gives, with probability
≥1−δ, uniformly over feasiblew,sup w | \CVaR
pθ
α −CVaR pθ α | ≤cM 1−α
q
logd+log(2/δ)
N .
The √logdrate (not √dlogN) is the correct one for a linear class under anℓ 1 budget. This term is
real but secondary; the interesting term is (M), and it requiresrealizeddata.
Model error requires realized outcomes.Within the implemented gate and the available data,
the only direct empirical evidence about CVaRP is the sequence of realized returns rt+1 actually
observed after each decision. We therefore build the verifier as aconformal-style risk controller:
at each rebalance it scores the realized outcome against the scenario predictive distribution and
calibrates the certificate width from the empirical distribution of past scores, rather than asserting a
bound analytically.
Definition 1(Realised calibration score).Fix α= 0.95 . Let ℓt+1 =−w ⊤ t rt+1 be the realised
portfolio loss and let \CVaRα be the CVaR of theacceptedscenario set, computed as the mean of
those scenario losses at or above their own empirical α-quantile. The score is theabsoluteone-step
discrepancy
st =

 ℓt+1 − \CVaRα

 ,
in units of daily return. It is anonnegative absolute discrepancyby construction, is computedafter
wt is committed, and is the only formula used anywhere in this paper: the verifier maintains the
rolling window{s τ }τ <tof the most recent60scores and takes its empirical quantile.
Conditional certificate statement 1(Act-time decision bound, conditional on the unproved (C5)
score-to-CVaR identification and (C6) per-attempt validity).Assume the score-to-CVaR identification
condition and the per-attempt validity condition of Assumption 1, neither of which is proved here. Run
adaptive conformal inference (42, 69) on {sτ } with target level βt updated online, and gate scenarios
on the resulting interval. Then the model-error term satisfies, with long-run frequency 1−δ ′ under
the approximate local exchangeability of Assumption 1(C3), |CVaRpθ α −CVaR P α| ≤qt(δ′), where
qt(δ′) is the adaptively calibrated width at the per-attempt level δ′ =δ/B . Combining with Lemma 2
and the allocator stability lemma, the committed decision obeys, on the covered rebalances and with
long-run frequency1−δ,
F( ˆwt)−F(w ⋆ t )≤ 1 2Γ  λµδµ +κ ΣδΣ +q t( δ B )| {z }
model, conformal
+ε N ( δ B )| {z }
sampling, Lem. 2
2
.(6)
Correction (supersedes an earlier draft).A previous version asserted that an unbounded refine-
ment loop “admits no nontrivial certificate at any level.”That is false, and we withdraw it.What
the union bound shows is thatBonferroniover B attempts degrades to zero as B→ ∞, a statement
about that proof technique, not about certifiability. Anytime-valid inference (e-processes, Ville’s
inequality, always-valid p-values) is designed precisely to license optional stopping anddoescertify
unbounded refine-until-pass loops. The correct claim is therefore: naive refinement invalidates the
certificate; a union bound repairs it for bounded B assuming the per-attempt validity condition (C6);
anytime-valid inference is the principled route to unboundedB, and we do not take it.
Proposition 2(Refinement is selection; Bonferroni restores validity for bounded B, assuming (C6)).
Assuming each candidate attempt satisfies the stated marginal validity condition before adaptive
selection(a condition we do not establish for the implemented proposal mechanism), then under ≤B
refinement attempts, evaluating the conformal interval at level δ/B per attempt yields a certificate
valid for the accepted attempt despite selection on st. As B→ ∞the Bonferroni-corrected level
degrades to zero, sothis proof techniqueyields no nontrivial certificate in the limit; anytime-valid
constructions certify unbounded refine-until-pass loops, and we do not take that route here.
Nonstationarity is why it must beadaptiveconformal.Standard conformal assumes exchange-
ability, which fails precisely at regime change, exactly when the certificate is most needed. Adaptive
conformal inference (42) targets long-run coverage by updating βt from realized miscoverage, which
is why we adopt it rather than a fixed split-conformal bound. We say “targets” rather than “guarantees
under arbitrary shift”: the guarantee we invoke holds under the approximate local exchangeability
assumed in Assumption 1(C3), which we do not verify empirically.
31

Proposition 3(Audited action admissibility and solver-output provenance).Provided (ℓ, u, τ)come
from the trusted validator, the convex program enforces the budget, box and turnover constraints
on its solver output wsol, so an erroneous controller cannot enlarge the feasible set. Inall reported
executionsthe post-processed committed vector wt passed the specified post-hoc feasibility audit
at the tolerances of App. O, which also gives the validate-and-reject variant that would make this a
guarantee rather than an audit. The logged active set and KKT duals constituteoptimality evidence
forw sol; forw t we claim onlyempirically audited admissibility.
Corollary 1(Empirically audited feasibility and solver provenance).Independently of controller
quality, generator quality, or whether the certificate holds, every committed action in the reported
experiments passed the budget, box and turnover checks at the tolerances of App. O. Separately, the
solve behind each action carries a reproducible KKT record for the solver output wsol (Prop. 3).
These areempiricalproperties of the reported executions and of the logged solver outputs; they
are not unconditional guarantees for arbitrary future executions, nor optimality certificates for
the post-processed committed vector. Decision-quality certification, feasibility auditing and solver
provenance are distinct properties and we report them separately.
Remark1 (What the certificate assumes).The act-time bound rests on (a) bounded losses and i.i.d.
sampling from pθ (term S), and (b) approximate local exchangeability of calibration scores, which
adaptive conformal is designed to tolerate under shift (term M). It doesnotassume pθ ≈P ; that
gap is measured, not assumed. This is the substantive difference from a goodness-of-fit gate, which
asserts calibration it cannot observe.
What we have not proved.One step in the chain is asserted rather than demonstrated, and we flag
it here. Adaptive conformal inference gives long-run coverage for afuture calibration score st. It
does not, without further argument, yield a bound on the distance between twopopulationfunctionals,
|CVaRpθ α −CVaR P α| ≤qt(δ′). Closing that gap requires (i) a precise statement of how the score of
Definition 1 identifies the population CVaR difference, in particular a monotone link between score
quantiles and that difference, and (ii) an argument that each adaptively proposed refinement attempt
is individually valid at level δ/B beforethe union bound is applied over attempts. We have neither,
and statement 1 should be read as conditional on that link, which is why it is not labelled a theorem.
Two further limits follow from the construction rather than from any gap in it. The coverage is
long-run and marginal, so no individual rebalance is certified. And (C3) is an assumption about the
score sequence that we do not verify empirically here. H2 was never exercised in our runs (§5.5), so
nothing in this paper tests the refinement correction. Accordingly, the honest reading of the verifier
in this paper is as an empirically motivated safeguard with a stated but incomplete theoretical basis,
and a reader who prefers to discount the certificate entirely loses none of the empirical results: every
measured claim in §5 is independent of it, and feasibility and provenance rest on Prop. 3 alone.
32
