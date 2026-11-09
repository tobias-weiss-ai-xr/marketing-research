---
title: When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention
url: https://arxiv.org/abs/2609.25806
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Peiying Zhu
- Sidi Chang
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.25806
pages: 9
chars: 34462
fetched_at: '2026-11-08T13:24:54+00:00'
kb_version: 1
---

# When Are Aggregate Agent Traces Diagnosable? Traffic-Governed Interpretation and Calibrated Abstention

When Are Aggregate Agent Traces Diagnosable?
Traffic-Governed Interpretation and Calibrated Abstention
Peiying Zhu * Sidi Chang *†
peiying@blossomai.co schang@blossomai.co
Blossom AI Blossom AI
San Francisco, CA, USA San Francisco, CA, USA
Abstract
Runtime traces are often treated as transparent evidence about an agent, but a closed-loop policy determines which states are
visited and therefore which failures can become visible. We study a simulated hotel-pricing agent whose policy maps time,
inventory, and market state to discrete price actions under varying demand regimes. A fault may leave no aggregate trace when
the policy rarely visits its affected cells. We treat entry into aggregate-only fault interpretation as a diagnosability decision
that precedes scoring or localization. A reference-map gate requires repeated clean-policy support; a matched runtime gate
then requires joint support in clean and current streams. Stable signal analysis occurs only after both gates pass. We calibrate
false admission on a disjoint clean stream at the physical-component level and model detection by affected clean traffic rather
than nominal cell coverage.
In a frozen one-shot heldout, 55/72 (76.4%) regime-component units were reference-admitted, representing 20 physical
components; 54/55 then passed matched runtime admission, and the rejected unit abstained. Stable false admission was 0/20,
with one-sided exact 95% upper bound 0.1391, meeting the frozen 0.20 criterion. Across 540 repeated unit-arm rows nested
in those 20 clusters, affected clean traffic reduced negative log likelihood by 29.3% relative to cell coverage, a gain of 0.1264
nats per row (cluster-bootstrap 95% interval [0.0593, 0.1918]). Adding mask family and its interaction improved log loss by
only 0.0015 nats per row (one-sided upper bound 0.0066), below the frozen 0.01 practical-sufficiency margin. A development
audit also found that exact minimum hitting set and greedy selection chose identical supports in 12/12 scenarios because
singleton evidence had already resolved the conflicts. The result is a bounded rule for interpreting aggregate agent behavior:
first establish exposure, then score change, and abstain when the trace cannot support the claim.
Keywords:agent behavior, runtime traces, closed-loop systems, fault diagnosis, diagnosability, abstention, traffic exposure
1 Introduction
Agent evaluation is moving from final-task scores toward
trajectories: tool calls, intermediate states, recovery be-
havior, and long-horizon traces [18, 19, 20]. These records
are richer than an outcome, but they are not neutral win-
dows into the system. Closed-loop agents act on state,
and those actions change which states will be observed
next. A component can therefore fail without producing a
visible aggregate change when the policy rarely visits the
affected region. Demand shift can also change visitation
and action summaries without any component fault. No
diagnosis algorithm can recover information absent from
its measurements [3]; trace interpretation that ignores
exposure can turn missing evidence into reassurance or
ordinary drift into a fault.
The system is a simulated hotel-pricing agent whose
policy maps time, inventory, and market state to discrete
price actions under varying demand regimes. Its target
policy is partitioned into 24 behavioral components, and
the interpreter receives typed aggregate trajectories rather
than the planted fault identity or every internal decision.
Earlier versions treated exact, risk-calibrated minimum
∗Both authors contributed equally to this research.
†Corresponding author.
hitting set (MHS) as the main contribution. Conflict-
directed diagnosis maps conflicts to hitting-set candidates
[1, 2], but our audit changed that conclusion: exact MHS
and weighted greedy selected the same support in all
12 development scenarios. Exact-scope predicates and
one-component probes had already introduced planted-
component singletons, leaving no residual ambiguity after
propagation.
This negative result redirects the question upstream. If
a trace compiler already reveals the answer, a stronger
optimizer cannot demonstrate a localization advantage.
If policy traffic never exposes the affected region, neither
exact nor approximate optimization can recover it. The
consequential interpretive decision is whether the current
trace contains evidence about the claimed component at
all.
Our workflow uses two gates. The reference-map gate
asks whether a component is repeatedly visited in a clean
stream. The runtime gate asks whether clean and cur-
rent streams are jointly supported in matched partitions.
Only then is stable signal evaluated. Clean-versus-clean
false admission is calibrated separately, and the physical
component, not each repeated regime arm or simulator
trajectory, is the safety sampling unit.
We also measure fault severity in the coordinates that
1
arXiv:2609.25806v1  [cs.AI]  22 Sep 2026

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
generate the traces. A mask may change many unvisited
cells or a few high-traffic cells, so cell count need not
predict signal strength. We define affected clean traffic as
the fraction of clean visits falling in changed cells, compare
it with affected cell count, and test whether traffic remains
practically sufficient across uniform and flow-weighted
masks.
A frozen shift detector separately triggers map recom-
putation rather than declaring a fault or an abstention.
This keeps distribution change, support loss, and stable
fault signal as distinct events.
The paper makes four bounded contributions to inter-
preting agent behavior:
1. We operationalize trace diagnosability with reference
and matched-runtime support gates that return ex-
plicit abstentions.
2. We define affected clean traffic as a behavior-grounded
exposure variable and test it against nominal edit size.
3. We pre-register independent false-admission calibra-
tion and family-robustness criteria at the physical-
component level.
4. We report a negative optimizer result that exposes
a verifier artifact: exact MHS showed no advantage
over propagation-aware greedy selection in this bench-
mark.
The heldout confirms gates, abstention, and traffic-
indexed signal behavior. It does not confirm localization
accuracy.
2 Related work and conceptual po-
sition
Interactive-agent benchmarks increasingly retain trajecto-
ries and environment state rather than only final answers
[18, 19, 20]. Such benchmarks establish tasks and ob-
servable records; they do not automatically establish that
a particular trace statistic identifies a component-level
failure. Our contribution is complementary: it asks when
an aggregate trajectory is eligible to support a fault inter-
pretation in the first place.
Conflict-directed model-based diagnosis derives candi-
dates as hitting sets of conflicts [1], and exact methods im-
prove search efficiency [2]. These solvers are conditional on
the compiled conflict family; they do not establish whether
upstream observations distinguish the represented physi-
cal faults. Diagnosability work instead asks whether faults
can be distinguished from available measurements [3, 4, 5].
Our gates are a finite-sample operationalization for ag-
gregate closed-loop traces, not a general diagnosability
theorem.
Selective prediction trades coverage against error by re-
jecting unsupported inputs [6, 7, 8, 16]. Overlap analysis
and offline reinforcement learning similarly avoid inference
where state-action coverage is weak [9, 10, 11, 12]. We ap-
ply this support-first principle before trace interpretation,
with fault visibility rather than treatment effect or policy
value as the estimand. Dataset-shift and conformal meth-
ods motivate a separate drift-to-refresh path [13, 14, 15].
Recent work interprets runtime behavior through point-
wise temporal-logic diagnostics [21] and trajectory-level
competence and visualization tools for LLM agents [22];
complementary theory establishes limits on predicting
agents from behavior alone [23]. Our narrower question
is whether an aggregate trace is eligible to support a
component-level fault interpretation. Our contribution is
the empirical synthesis in a pre-localization pipeline: sup-
port gates, component-level false-admission calibration,
and traffic-indexed signal analysis. We do not claim to
originate diagnosability, abstention, overlap analysis, shift
detection, or behavioral diagnostics.
3 Problem setting
3.1 Components, regimes, and aggregate
traces
Let C be the set of 24 disjoint target-policy components.
Each component is indexed by a time quarter, inventory
half, and market third. The simulator is evaluated under
three separately fitted demand regimes,lambda0 in {5,
7, 9} . A regime-component pair is a unit, giving 72 units
before admission.
For each unit and evaluation partition, the system
records typed aggregate traces. The signal calculation
uses two existing summaries:
•region_d1, a regional distribution distance; and
•mean_action_gap , the mean reference-current action
difference.
The diagnostic does not observe the planted fault iden-
tity when deciding admission or signal stability.
3.2 Fault masks and directions
A formal fault changes a deterministic subset of direction-
changeable target-field cells by one action bucket. Each
selected subset is tested in outward and inward directions.
Two nested mask families are used:
•uniform , a seeded random ordering of changeable
cells; and
•flow_weighted , a seeded weighted-without-
replacement ordering in which frequently visited
clean cells tend to enter earlier.
The two families can have the same selected cell fraction
but very different affected traffic.
2

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
3.3 Affected clean traffic
For component cell c, let oc be its clean reference visit
count. For a directional fault selecting cellsSd, define
τd =
P
c∈Sd oc P
c∈component oc
.
The primary exposure is
τ= (τ outward +τ inward)/2.
For the matched cell-count model, directional coverage
is the selected fraction of direction-changeable cells, and
the bi-directional covariate is the arithmetic mean
fcell = (foutward +f inward)/2.
If component occupancy is zero, tau is zero. Zero-
exposure cases are reported separately and are not shifted
by an arbitrary constant before logging.
3.4 Diagnosability as a state, not a hidden
assumption
For a unitu, a reference streamR, and a current stream
Q, the diagnostic state is:
REFERENCE_ABSTAIN→RUNTIME_ABSTAIN
→SIGNAL_ELIGIBLE
→ {DETECTED,NOT_DETECTED}.
The arrows denote tests, not a temporal guarantee that
every unit progresses. A unit that fails the first gate never
reaches the second. A unit that fails the second never
reaches signal interpretation. This ordering distinguishes
“no usable comparison” from “usable comparison with no
stable signal.”
4 Why MHS is downstream
Given conflicts and component costs, exact MHS finds the
minimum-cost set intersecting every conflict. Its guaran-
tee remains conditional on the conflict family and does
not establish physical-fault identification. In 12 audited
development scenarios, exact MHS and propagation-aware
greedy selection chose identical supports and achieved
identical exact recovery (9/12). The instances were not
devoid of combinatorial structure: non-singleton conflicts
comprised 55.5% of the conflict collection, and conflicts
overlapped in all 12 scenarios. A follow-up audit found
planted-component singleton conflicts in 9/9 exact-anchor
and 9/9 hard-probe cases, with 0/9 nonempty residual
conflict families after propagation.
The mechanism is upstream. Classical GDE selects a
next measurement to discriminate among diagnoses by
expected entropy reduction [17]. The hard probe here
instead changed exactly one component and paired that in-
tervention with a predicate scoped to the same component,
converting the local response into a planted-component
singleton. Propagation therefore forced the choice before
exact and greedy solvers could differ. This does not show
that MHS is wrong; it shows that the evidence construc-
tion does not test optimizer advantage. We retain MHS
only as an optional downstream risk-cost optimizer and
make no formal localization claim.
5 Diagnosability method
5.1 Reference-map gate
A component has partition support when its existing sup-
port count is at least 12. A regime-component unit enters
the formal reference map when at least 14 of 15 clean ref-
erence partitions have support. All 72 units are screened;
none is excluded by identity or development eligibility.
The admitted proportion over 72 units is the primary
coverage description. The number of distinct physical
components represented is also reported. A low admission
rate is a limitation of the observable system, not a reason
to change the gate.
5.2 Runtime two-stream gate
A runtime partition is supported only when reference and
current support are both at least 12 in that same parti-
tion. Runtime admission requires at least 14 such joint
partitions out of 15. For a bi-directional fault observation,
both directions must pass.
This intersection matters because separate aggregate
counts can hide mismatched evidence: 14 well-supported
reference partitions and 14 well-supported current parti-
tions do not guarantee 14 usable comparisons if they occur
in different partitions.
5.3 Stable aggregate signal
For each matched reference-current partition pair, define
z= max
 region_d1
0.20 , |mean_action_gap| 0.35  .
A partition signals when z >= 1.50 . After the unit-
level runtime gate passes, direction stability is counted
over all 15 matched pairs rather than over a support-
signal intersection; a direction is stable at 14/15 signaling
partitions, and a unit-arm is bi-directionally stable only
when both directions are stable. Signal values for an arm
that fails either support gate remain sealed validation
fields and cannot enter a power endpoint. Threshold 1.50
was selected before formal execution from the fixed grid
{1.00, 1.25, 1.50, 1.75, 2.00} . It is not tuned on
the formal null.
3

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
5.4 Three separate failure quantities
We separate:
1. reference-map invalidation:a development-
admitted reference unit fails the initial formal
reference-only rule;
2. runtime two-stream rejection:the formal refer-
ence passes but the matched current-reference com-
parison fails joint support; and
3. stable false admission:a runtime-admitted clean-
versus-clean unit produces a stable signal.
Combining them would obscure whether the problem is
a changed reference map, insufficient concurrent evidence,
or a noisy signal. Each is reported separately at unit and
physical-component-cluster levels. Reference invalidation
and runtime rejection are descriptive coverage endpoints
with no frozen population-rate threshold; each affected
unit still abstains. The only≤ 0.20population claim is
stable false admission.
5.5 Drift and refresh
A frozen split-conformal detector summarizes each clean-
null partition and raises an alarm above a precommitted
threshold. Alarms request atomic map recomputation;
they do not declare a fault or an abstention. Passing units
return toMAP_VALID, while units failing the refreshed refer-
ence rule enterREFERENCE_ABSTAIN. The formal endpoint
is only a state-machine smoke test because every refresh
reuses the same frozen reference buffer; it does not show
that future data can repair a stale map.
6 Frozen confirmatory design
6.1 Seed separation
Formal seeds 200000..202399 form 15 clean reference
partitions of 160 episodes. Disjoint seeds202400..204799
form 15 current/fault partitions. Seeds204800..204999
remain unused. Common random numbers pair conditions
within the experiment, while inference clusters repeated
observations by physical component.
An episode is one simulator trajectory used to form a
partition-level aggregate; it is not an independent statisti-
cal unit. The 3,456,000 scheduled fault-stream episodes
describe Monte Carlo workload, not an effective sample
size. The design begins with 24 physical components re-
peated across three regimes, producing 72 coverage units.
After admission, safety and bootstrap inference operate on
20 represented physical-component clusters. The primary
structural fit contains 540 unit-arm rows nested within
those clusters.
6.2 Formal mask construction
For each regime, component, direction, and family, a SHA-
256-derived seed produces a deterministic cell ordering
under master seed 2026082370. Nested prefixes target
traffic near 0.15, 0.30, 0.50, 0.75, and 0.95; achieved traffic
enters analysis. The clean stream determines occupancy
and masks before fault outcomes are opened, and selected-
cell, traffic, cell-fraction, and policy hashes are sealed.
6.3 Formal endpoints
Endpoints cover admission, component-level reference in-
validation and runtime rejection, component-level stable
false admission, stable-signal power versus achieved traffic,
traffic-versus-cell log-loss, practical family sufficiency, ag-
gregate monotonicity, and state-machine execution. MHS
output and planted localization accuracy are excluded.
6.4 Statistical analysis
Reference invalidation and runtime rejection use
component-level two-sided exact 95% Clopper-Pearson
intervals as descriptive coverage endpoints; they have no
population-rate pass threshold. Stable false admission
alone uses the component-level one-sided exact 95% upper
bound and is labeledSAFETY CONFIRMEDonly when that
bound is at most 0.20. Regime-unit rates are secondary
because regimes reuse the same physical components.
The safety rule has coarse resolution: at 20 admitted
components, 0/20 gives upper bound 0.1391 and passes,
while1/20gives 0.2161 and fails.
Power rates use Wilson 95% intervals. The primary
model fits stable signal against log(tau) on positive-
exposure units that pass both support gates. A matched
cell model uses log(cell_fraction). Traffic is supe-
rior only if the component-bootstrap two-sided 95% lower
bound on per-unit-arm-row negative-log-likelihood im-
provement, NLL(cell) - NLL(traffic) , is greater than
zero.
The family model adds mask family and its interac-
tion with log(tau). Traffic is practically sufficient across
the two frozen families only if the component-bootstrap
one-sided 95% upper bound on augmented-model log-loss
improvement is below 0.01 nats per unit-arm row. A non-
significant family coefficient is not an equivalence result.
The bootstrap samples physical components, not unit-
arm rows. A fixed generator produces 2,000 draws; finite
singular and one-class replicates are retained, and no
replicate is redrawn. Empty or nonfinite analyses return
NOT ESTIMABLErather than a favorable verdict.
The exact-binomial safety statement is conditional on
the frozen working assumption that distinct physical-
component indicators are exchangeable independent
Bernoulli trials given the policies and shared seed sched-
ule. Common random numbers can induce residual cross-
4

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
component dependence, so this is not an unconditional
new-population guarantee.
6.5 Development separation
Developmentdatamotivatedtrafficastheprimaryaxisbut
did not establish family sufficiency. They were not pooled
with the formal heldout. A pre-run projection from 20
to 15 partitions and the withdrawn cell-coverage heuristic
were development-only; neither is a formal endpoint.
7 Formal results
7.1 Sampling frame, admission, and ab-
stention
Of 72 regime-component units, 55/72 passed formal refer-
ence admission, representing 20/24 distinct components.
Relative to the development reference map, invalidation
was 0/20 at component grain and 0/55 at regime-unit
grain; the component-level descriptive two-sided exact 95%
interval was [0.0%, 16.8%]. On the clean current stream,
1/20 component clusters had a runtime two-stream rejec-
tion, with descriptive interval [0.1%, 24.9%]. These two
rates quantify coverage loss and have no population pass
threshold; every affected unit abstained.
Among the 20 runtime-admitted components, 0/20 pro-
duced a stable clean-versus-clean signal. The one-sided
exact 95% upper bound was 0.1391, satisfying the frozen
<=0.20 safety rule. The corresponding regime-unit result
was 0/54 and remains descriptive.
7.2 Traffic-indexed power
The conditional denominator is the 54 runtime-admitted
units; the operational denominator is the 55 reference-
admitted units and counts the one runtime abstention as
no actionable diagnosis. Both families were saturated at
0/54 and 54/54 at the endpoints; only the middle-target
family gaps (+4, +2, +3, uniform minus flow-weighted)
are empirically informative. Monotonicity passed but is
a weak shape check, not evidence of family equivalence.
All 44 zero-exposure scheduled observations abstained and
none was stable.
7.3 Traffic versus cell coverage and family
sufficiency
Across540repeatedunit-armrowsnestedin20represented
physical-component clusters, the traffic model achieved
negative log likelihood 164.9866 (0.3055 per row), com-
pared with 233.2453 (0.4319 per row) for the cell-count
model. The difference was 0.1264 nats per unit-arm row, a
29.3% reduction relative to the cell-model negative log like-
lihood, with component-bootstrap 95% interval [0.0593,
0.1918]. The lower bound was above zero, so traffic was
confirmed as the better primary axis.
The family-plus-interaction model improved log loss by
0.0015 nats per unit-arm row. Its one-sided component-
bootstrap 95% upper bound was 0.0066, which was below
the frozen 0.01 margin. Traffic therefore met the prac-
tical family-sufficiency criterion. The traffic-plus-family
coefficient was -0.3618 with component-bootstrap interval
[-0.8617, 0.0367] and secondary likelihood-ratio p-value
0.2019.
The largest observed family gaps occurred in the[0.30,
0.45) and [0.75, 0.90) traffic bins. They are small in
aggregate log-loss terms (0.0015 nats per row) but are not
excluded on the odds scale, consistent with the coefficient
interval above. The 0.0034-nat margin is narrow, and
the percentile cluster-bootstrap uses only 20 represented
components. The sufficiency label is therefore limited
to the two frozen mask families and the precommitted
0.01-nat criterion.
An operational sensitivity counting runtime abstention
as zero gave the same decisions: traffic-over-cell improve-
ment 0.1164 [0.0512, 0.1835] and family-plus-interaction
gain 0.0014 with upper bound 0.0060.
7.4 Drift, refresh, and decision summary
The detector was quiet in its matched lambda0=7
regime (0/15 alarms) and active under demand shifts
at lambda0=5 (15/15) and lambda0=9 (14/15). These are
descriptive state-machine inputs, not a 29/45 false-alarm
estimate. Five refresh operations reproduced the frozen
map over 120 evaluations; because they reuse the same
buffer, this does not show that refresh can repair a stale
map.
There is no combined scientific verdict. Execution,
operational safety, descriptive coverage, and the three
structural hypotheses retain separate labels and interpre-
tations.
8 Discussion
8.1 Interpretation is fixed by the endpoint
pattern
The endpoint pattern fixes a bounded interpretation: sta-
ble false admission supports only the component-cluster
0.20 upper-bound statement; reference invalidation and
runtime rejection remain descriptive coverage losses with
abstention; and a single traffic curve is practically suffi-
cient only within admitted units and the two frozen mask
families. Nondecreasing counts are a weak shape check,
not family equivalence.
5

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
Table 1: Formal admission, abstention, and false-admission endpoints.
Grain Endpoint Result Interval / bound Interpretation
regime-
component
reference admission 55/72 (76.4%) descriptive addressable units
physical
component
reference
representation
20/24 (83.3%) descriptive addressable components
physical
component
reference
invalidation
0/20 95% CI [0.0%, 16.8%] descriptive; abstain
physical
component
runtime rejection 1/20 95% CI [0.1%, 24.9%] descriptive; abstain
physical
component
stable false
admission
0/20 one-sided 95% upper 0.1391SAFETY CONFIRMED
Table 2: Conditional and operational bi-directional stable detections.
Family Traffic target 0.15 0.30 0.50 0.75 0.95
uniform, conditional 0/54 17/54 37/54 52/54 54/54
uniform, operational 0/55 17/55 37/55 52/55 54/55
flow-weighted, conditional 0/54 13/54 35/54 49/54 54/54
flow-weighted, operational 0/55 13/55 35/55 49/55 54/55
8.2 What the work changes conceptually
Optimization and observability are distinct: exact MHS
may be optimal for a compiled objective without identi-
fying the physical fault, while a simple method can look
perfect when singleton evidence already reveals the an-
swer. Neither shows whether a trace reveals failure under
a different traffic regime.
The two-gate workflow makes that dependency explicit.
Reference admission asks what the policy normally ex-
poses; runtime admission asks whether a matched compar-
ison is possible; signal admission asks whether change is
stable; and localization comes last. This is an application-
specific synthesis of diagnosability analysis [3, 4], local sup-
port characterization [9], and selective abstention [6, 7, 16].
Traffic exposure provides a mechanism for why maps
move with environment. Higher demand consumes in-
ventory more quickly, transferring visitation from high-
inventory to low-inventory regions later in the episode.
Pooled component ranks can therefore fall even when
direction-specific movement is predictable. A map may
rotate along a known inventory axis rather than become
arbitrary. The operational consequence is to refresh the
map when drift is detected, not to permanently reject the
diagnostic.
8.3 Why abstention is part of the result
Admission below 100% defines the supported portion of
the component universe, not merely lost sample size. Re-
porting conditional power alongside operational power,
with abstention counted as no action, distinguishes a nar-
row high-performing method from a broader moderate
one.
9 Limitations and claim boundaries
The formal study uses one simulator and one-bucket target-
field shifts; other magnitudes, interactions, persistence
patterns, and non-target-field faults may yield different
curves. Occupancy comes from a clean reference policy, so
systems without such a stream need another maintenance
design. Only 24 physical clusters are available. The exact-
binomial statement is coarse and remains conditional on
the exchangeable-independent component working model
despite common seeds. Percentile cluster-bootstrap inter-
vals from about 20 represented clusters may undercover in
directions favorable to both structural findings. The false-
admission bound is 0.20, not 0.05, and the study confirms
pre-localization signal behavior, not planted-fault localiza-
tion. Practical sufficiency applies only to the two frozen
mask families and the 0.01-nat margin. The intended
benefit is to prevent unsupported fault claims; the corre-
sponding risk is false assurance if simulator-specific gates
or thresholds are transferred to deployed or human-facing
agents without new calibration.
10 Conclusion
Aggregate traces should be interpreted only after estab-
lishing component exposure. The two gates admitted
55/72 reference units and 54/55 matched runtime units;
stable false admission was 0/20 (one-sided 95% upper
0.1391). Affected traffic outperformed cell coverage and
met the 0.01-nat sufficiency criterion within the two frozen
families. Exact MHS did not improve localization over
propagation-aware greedy selection; behavior under gen-
6

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
Figure 1: Bi-directional stable-signal probability versus achieved affected clean traffic. Points and pre-registered
family-interaction curves are shown separately for uniform and flow-weighted masks. Shaded bands are descriptive
95% component-cluster bootstrap intervals from 20 represented components and 2,000 resamples. Runtime admission
is shown below each curve; all 44 zero-exposure observations appear separately.
uinely ambiguous traces remains open.
References
[1] R. Reiter. A theory of diagnosis from first principles.
Artificial Intelligence, 32(1):57–95, 1987.https://
doi.org/10.1016/0004-3702(87)90062-2.
[2] P. Rodler. Memory-limited model-based diagnosis.
Artificial Intelligence, 305:103681, 2022.https://do
i.org/10.1016/j.artint.2022.103681.
[3] D. Wang, F. Fu, W. Li, Y. Tu, C. Liu, and W. Liu. A
review of the diagnosability of control systems with
applications to spacecraft.Annual Reviews in Control,
49:212–229, 2020. https://doi.org/10.1016/j.ar
control.2020.03.004.
[4] F. Fu, D. Wang, L. Li, W. Li, and Z. Wu. Data-
driven method for the quantitative fault diagnosabil-
ity analysis of dynamic systems.IET Control The-
ory & Applications, 13(8):1197–1203, 2019.https:
//doi.org/10.1049/iet-cta.2018.5378.
[5] N. Bertrand, S. Haddad, and E. Lefaucheux. A tale of
two diagnoses in probabilistic systems.Information
and Computation, 269:104441, 2019.https://doi.
org/10.1016/j.ic.2019.104441.
[6] Y. Geifman and R. El-Yaniv. SelectiveNet: A deep
neural network with an integrated reject option. In
Proceedings of the 36th International Conference on
Machine Learning, PMLR97:2151–2159, 2019.https:
//proceedings.mlr.press/v97/geifman19a.htm
l.
7

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
Table 3: Pre-registered structural tests.
Test Estimate Cluster interval / bound Criterion Result
cell minus traffic NLL,
nats/row
0.1264 95% [0.0593, 0.1918] lower > 0P ASS
family+interaction gain,
nats/row
0.0015 one-sided upper 0.0066 upper < 0.01P ASS
Table 4: Frozen decision summary.
Layer Item Formal result Label
execution frozen protocol and
validator
56 checks; 1,440 cases; 21,600 partition rows EXECUTED
safety stable false-admission upper
<=0.20
0/20; upper 0.1391 CONFIRMED
coverage reference invalidation /
runtime rejection
0/20 / 1/20 DESCRIPTIVE
structure traffic over cell coverage 0.1264 [0.0593, 0.1918] PASS
structure family practical sufficiency 0.0015; upper 0.0066 PASS
structure aggregate monotonicity
(weak shape check)
nondecreasing; endpoints saturated PASS
[7] A. Gangrade, A. Kag, and V. Saligrama. Selective
classification via one-sided prediction. InProceedings
of the 24th International Conference on Artificial In-
telligence and Statistics, PMLR 130:2179–2187, 2021.
https://proceedings.mlr.press/v130/gangrad
e21a.html.
[8] S. Bates, A. N. Angelopoulos, L. Lei, J. Malik, and
M. I. Jordan. Distribution-free, risk-controlling pre-
diction sets.Journal of the ACM, 68(6):43:1–43:34,
2021.https://doi.org/10.1145/3478535.
[9] M. Oberst, F. Johansson, D. Wei, T. Gao, G. Brat, D.
Sontag, and K. Varshney. Characterization of overlap
in observational studies. InProceedings of the 23rd
International Conference on Artificial Intelligence
and Statistics, PMLR 108:788–798, 2020.https://
proceedings.mlr.press/v108/oberst20a.html.
[10] A. D’Amour, P. Ding, A. Feller, L. Lei, and J.
Sekhon. Overlap in observational studies with high-
dimensional covariates.Journal of Econometrics,
221(2):644–654, 2021. https://doi.org/10.101
6/j.jeconom.2019.10.014.
[11] Y. Jin, Z. Yang, and Z. Wang. Is pessimism provably
efficient for offline RL? InProceedings of the 38th In-
ternational Conference on Machine Learning, PMLR
139:5084–5096, 2021. https://proceedings.mlr.
press/v139/jin21e.html.
[12] S. Levine, A. Kumar, G. Tucker, and J. Fu. Offline
reinforcement learning: Tutorial, review, and per-
spectives on open problems. arXiv:2005.01643, 2020.
https://arxiv.org/abs/2005.01643.
[13] S.Rabanser, S.Günnemann, andZ.C.Lipton.Failing
loudly: An empirical study of methods for detecting
dataset shift. InAdvances in Neural Information Pro-
cessing Systems 32, 2019.https://papers.neurips
.cc/paper/8420-failing-loudly-an-empirical
-study-of-methods-for-detecting-dataset-shi
ft.
[14] J. Lei, M. G’Sell, A. Rinaldo, R. J. Tibshirani, and
L. Wasserman. Distribution-free predictive inference
for regression.Journal of the American Statistical
Association, 113(523):1094–1111, 2018.https://do
i.org/10.1080/01621459.2017.1307116.
[15] V. Vovk, I. Petej, I. Nouretdinov, E. Ahlberg, L.
Carlsson, and A. Gammerman. Retrain or not re-
train: Conformal test martingales for change-point
detection. InProceedings of the Tenth Symposium on
Conformal and Probabilistic Prediction and Applica-
tions, PMLR 152:191–210, 2021.https://proceedi
ngs.mlr.press/v152/vovk21b.html.
[16] H. Liang, L. Peng, and J. Sun. Selective classification
under distribution shifts.Transactions on Machine
Learning Research, October 2024.https://openre
view.net/forum?id=dmxMGW6J7N.
[17] J. de Kleer and B. C. Williams. Diagnosing multiple
faults.Artificial Intelligence, 32(1):97–130, 1987. ht
tps://doi.org/10.1016/0004-3702(87)90063-4.
[18] X. Liu et al. AgentBench: Evaluating LLMs as agents.
International Conference on Learning Representa-
tions, 2024. https://openreview.net/forum?id=
zAdUB0aCTQ.
8

When Are Aggregate Agent Traces Diagnosable? Zhu & Chang
[19] S. Zhou et al. WebArena: A realistic web envi-
ronment for building autonomous agents.Interna-
tional Conference on Learning Representations, 2024.
https://openreview.net/forum?id=oKn9c6ytLx.
[20] S. Yao, N. Shinn, P. Razavi, and K. Narasimhan. Tau-
bench: A benchmark for tool-agent-user interaction
in real-world domains.International Conference on
Learning Representations, 2025.https://openrevi
ew.net/forum?id=roNSXZpUDN.
[21] N. Brindise, A. Posada Moreno, C. Langbort, and S.
Trimpe. Pointwise-in-time diagnostics for reinforce-
ment learning during training and runtime. InPro-
ceedings of the 6th Annual Learning for Dynamics
& Control Conference, PMLR 242:694–706, 2024.
https://proceedings.mlr.press/v242/brind
ise24a.html.
[22] T. Ou, W. Guo, A. Gandhi, G. Neubig, and X. Yue.
AgentDiagnose: An open toolkit for diagnosing LLM
agent trajectories. InProceedings of the 2025 Con-
ference on Empirical Methods in Natural Language
Processing: System Demonstrations, pages 207–215,
2025. https://doi.org/10.18653/v1/2025.emnlp
-demos.15.
[23] A. Bellot, J. Richens, and T. Everitt. The limits
of predicting agents from behaviour. InProceedings
of the 42nd International Conference on Machine
Learning, PMLR 267:3623–3658, 2025.https://pr
oceedings.mlr.press/v267/bellot25a.html.
9
