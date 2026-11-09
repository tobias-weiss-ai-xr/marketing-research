---
title: Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss
url: https://arxiv.org/abs/2606.03878
category: privacy-data
subcategory: measurement
date: 2026-06
venue: arXiv (Cornell University)
authors:
- Prashant Shekhar
- Caroline Howard
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.03878
pages: 26
chars: 82738
fetched_at: '2026-11-08T12:57:37+00:00'
kb_version: 1
---

# Privacy-Robust Incrementality Measurement for Advertising Systems under Signal Loss

Privacy-Robust Incrementality Measurement for
Advertising Systems under Signal Loss
Prashant Shekhar1 and Caroline Howard
Department of Mathematics
Embry-Riddle Aeronautical University
Daytona Beach, FL, USA
Abstract
Advertising platforms use randomized lift tests to measure incrementality, but privacy-preserving
reporting systems degrade the observed signal through match-rate loss, linkability loss, attribution-window
loss, aggregation-threshold suppression, randomized reporting noise, and segment-heterogeneous signal loss.
This paper formulates privacy-constrained advertising measurement as a robust causal decision problem
under the mentioned signal losses. Given a randomized experiment and an ambiguity set for privacy-induced
degradation, the framework projects the observation-compatible fiber of clean/unfiltered experimental worlds
onto the incrementality functional and returns certified, rejected, and unresolved decisions. The main result
gives a sharp decision frontier. Reports outside the frontier support uniformly valid certification or rejection,
whereas reports inside it contain too little information for any method to uniformly distinguish above-
threshold incrementality from non-incrementality. Supporting results give finite-sample certification, sample-
complexity guarantees, a minimax lower bound showing that signal loss reduces effective information, and a
reporting-granularity tradeoff. On 2.0M Criteo Uplift rows and the 64K-row Hillstrom email experiment,
clean conversion lift is positive in both datasets, with lifts 0.00112 and 0.00495, respectively. Population
certification survives mild degradation in Criteo and severe degradation in Hillstrom, while all considered
finite-sample stress settings in both datasets remain unresolved after simultaneous uncertainty and reporting
noise are included. At the segment level, Hillstrom population certification falls from 100% of coarse cells
to 36.0% of very fine cells, while aggregation-threshold suppression rises to 39.5%. Overall, the research
contributes a decision-theoretic layer for privacy-aware incrementality measurement whose output is the
strongest causal-claim justified by degraded ads signals.
1 Introduction
Incrementality measurement asks whether advertising caused outcomes that would not otherwise have occurred.
This question is central to ads ranking, advertiser reporting, campaign optimization, budget allocation, and
product experimentation. The clean statistical solution is a randomized experiment with well-defined treatment,
control, outcomes, and follow-up windows. In practice, however, advertising measurement is increasingly
shaped by privacy and identity constraints. Users may opt out of tracking, device identifiers may be missing or
unstable, conversions may be reported only in aggregate, small cells may be suppressed, and privacy-preserving
systems may add randomized reporting noise before reporting conversion counts. The result is a gap between
the causal estimand that the experiment was designed to identify and the degraded signal available to the
analyst.
This paper studies that gap. We formulate privacy-constrained advertising measurement as a robust causal deci-
sion problem under signal loss. The starting point is a randomized incrementality experiment with a treatment
indicator, outcome labels, and covariates. We assume the measurement system releases a degraded version of
this experiment through 6 signal-loss layers: (i) match-rate loss drops reportable outcomes, (ii) linkability loss
breaks identity continuity across events, (iii) attribution-window loss censors conversions outside reporting
1Corresponding author:shekharp@erau.edu 1
arXiv:2606.03878v1  [stat.ML]  2 Jun 2026

Figure 1:Privacy-robust incrementality measurement as a decision problem. A randomized advertising experiment
identifies clean lift before reporting constraints are applied (as summarized in Table 1). The proposed framework maps the
resulting privacy-degraded report to a decision/certification frontier and returns the strongest justified decision: (i) certify
positive incrementality, (ii) reject it, or (iii) mark the claim unresolved.
windows, (iv) aggregation-threshold suppression removes sparse reporting cells, (v) randomized reporting
noise perturbs released aggregates, and (vi) segment-heterogeneous signal loss makes these degradations vary
across customer or campaign groups. These layers correspond to common primitives in modern reporting
systems, including event-level attribution reports, summary reports, aggregation services, attribution windows,
contribution budgets, and interoperable private-attribution protocols [Google Privacy Sandbox, 2025a,b, Case
et al., 2023, Aksu et al., 2024, Tholoniat et al., 2024]. Figure 1 summarizes the resulting decision problem.
The analyst observes the degraded report and must decide whether the evidence is strong enough to certify
positive incrementality.
The key distinction is between estimating lift and certifying a decision. A point estimate can be optimistic
when high-value conversions are more likely to be unobserved, when low-volume segments are suppressed, or
when randomized reporting noise dominates the signal. A deployable measurement system should therefore
state what remains justified under plausible signal-loss mechanisms. We propose a framework that maps
an observed privacy-degraded experiment into three sets. The first contains campaigns or segments whose
lower-bound incremental value exceeds the business threshold. The second contains cases whose upper bound
is below the threshold. The third contains unresolved cases where the available signal cannot support a stronger
claim.
In essence, the paper is motivated by four observations from advertising measurement practice. First, random-
ized incrementality data remain the strongest empirical anchor for causal claims, while missing measurement
remains a separate obstacle. Second, privacy degradation changes which causal claims are identifiable, so it
belongs inside the decision rule. Third, public datasets rarely include both the pre-privacy identity graph and
post-privacy reports, so empirical work must be honest about what is actually observed. And fourth, business
decisions require conservative certification, beyond ranking or attribution alone.
1Corresponding author:shekharp@erau.edu 2

Overall, the research contributions are fivefold.First, we define a signal-loss model for privacy-constrained
ads measurement that covers match-rate loss, linkability loss, attribution-window loss, aggregation-threshold
suppression, randomized reporting noise, and segment-heterogeneous signal loss.Second, we introduce
a compatibility-fiber view of privacy-degraded reports and specialize sharp partial-identification bands to
privacy-constrained incrementality decisions over conversions and spend.Third, we show that the unresolved
region is information-theoretic in the sense that if the business threshold lies inside the sharp band, no
uniformly valid procedure observing the same degraded report can certify or reject the claim.Fourth, we
prove sample-complexity and minimax lower-bound results that separate sampling error, reporting-noise error,
and irreducible signal-loss width, with finite-sample certification handled as the direct simultaneous-coverage
decision rule. Andfifth, we define reporting-granularity diagnostics that trade off randomized reporting-noise
reduction against segment-heterogeneous signal loss and make segment-level unresolved claims visible.
2 Related Work
Incrementality, uplift modeling, and treatment targeting: Uplift modeling studies how to predict het-
erogeneous treatment effects and target treatment to units whose outcomes are most improved by treatment
[Gutierrez and Gérardy, 2017, Guelman et al., 2015, Ruda´s and Jaroszewicz, 2018, Olaya et al., 2020]. The
Criteo uplift benchmarks made large-scale randomized advertising data available for uplift modeling and
individual-treatment-effect prediction [Diemert et al., 2018, 2021]. Recent work studies area under the uplift
curve (AUUC) optimization and generalization guarantees for treatment targeting [Betlei et al., 2020]. Our
work asks a complementary measurement question: whether an observed randomized lift signal remains
decision-certifying after privacy and identity degradation.
Advertising measurement and attribution: Large field experiments have shown that observational and
model-based advertising measurement can differ substantially from randomized lift estimates [Gordon et al.,
2019, 2023, Johnson, 2023]. Related work studies ghost ads, geo experiments, causal impact, incremental
return on ad spend, latent stratification, counterfactual demand-side platform (DSP) measurement, Facebook
lift-study power calculations, and experiment-to-campaign prediction [Johnson et al., 2017, Lewis and Rao,
2015, Vaver and Koehler, 2011, Chen and Au, 2022, Brodersen et al., 2015, Berman and Feit, 2024, Chalasani
et al., 2017, Sun et al., 2015, Liu et al., 2018, Gordon et al., 2026]. Attribution models and multi-touch
attribution attempt to assign conversion credit across touchpoints, including causal and recurrent approaches
[Diemert et al., 2017, Du et al., 2019, Yao et al., 2022]. Our framework differs in its decision target. Attribution
distributes credit, while privacy-robust incrementality asks what causal decision remains certified when
reporting signals are degraded.
Privacy-preserving measurement and signal loss: Differential privacy provides formal protection against
individual-level disclosure [Dwork, 2008, Dwork and Roth, 2014]. Recent advertising-measurement work
studies private conversion measurement, Attribution Reporting and Private Aggregation in Privacy Sandbox,
Interoperable Private Attribution (IPA), summary-report optimization, on-device budgeting for differentially
private ad measurement, aggregated event measurement, and privacy-preserving conversion prediction [Delaney
et al., 2024, Google Privacy Sandbox, 2025a,b, Case et al., 2023, Aksu et al., 2024, Ghazi et al., 2025, Tholoniat
et al., 2024, Meta Audience Network, 2021, Xiao et al., 2025, Zhong et al., 2022, O’Brien et al., 2022]. These
papers focus on privacy protocols, query release, and reporting accuracy. We focus on the causal decision
layer downstream of such mechanisms. Given degraded or private reports from a randomized incrementality
test, when is positive incrementality still certifiable?
Partial identification, sensitivity, and robust decision rules: When data are incomplete or assumptions are
weak, causal effects may be partially identified rather than point identified [Horowitz and Manski, 2000, Imbens
and Manski, 2004, Manski and Pepper, 2000, Richardson et al., 2014, Coppock et al., 2017, Gabriel et al., 2023].
Recent work also studies causal inference with corrupted data and differentially private average treatment
effect (ATE) or conditional average treatment effect (CATE) estimation [Agarwal and Singh, 2021, Ohnishi
and Awan, 2025, Niu et al., 2022]. Robust policy and off-policy evaluation methods emphasize decision rules
that remain valid under confounding, weak support, or high-variance logged feedback [Kallus and Zhou, 2018,
Swaminathan and Joachims, 2015, Su et al., 2020]. Recent advertising-marketplace work applies a similar
1Corresponding author:shekharp@erau.edu 3

decision-object perspective to adjacent problems, including mechanism-robust online experiment design under
interference [Shekhar and Howard, 2026a] and support-aware offline reserve-policy selection from logged
auctions [Shekhar and Howard, 2026b]. This paper builds on those ideas by developing a privacy-degraded
incrementalitydecision frontier, which is a specialization of sharp partial-identification logic to advertising
reports whose signal-loss layers determine whether a lift claim is certifiable, rejectable, or impossible to
resolve, together with finite-sample and information-theoretic limits for that frontier.
3 Problem Setup
We observe a randomized marketing experiment with treatment assignment Ai ∈ {0,1}, outcome Yi, and
reported segment membership i∈s . The outcome may represent conversion, visit, spend, or advertiser value.
LetY i(1)andY i(0)denote potential outcomes. For a segments, the clean incrementality estimand is
∆s =E[Y i(1)−Y i(0)|i∈s].(1)
Randomization identifies this estimand under clean observation. The measurement problem is that the analyst
may not observe the clean arm means needed to estimate ∆s. Instead, the reporting system releases a privacy-
degraded segment report rs. In the simplest mean-reporting case, rs contains degraded treated and control arm
means eµ1,s,eµ0,s, together with cell counts, suppression indicators, and any reporting-noise metadata. The
degraded arm mean is related to the clean arm mean by a reportable-retention multiplier
eµa,s =q a,sµa,s, µ a,s =E[Y i(a)|i∈s], a∈ {0,1}.
The multiplier qa,s ∈(0,1] summarizes the share of outcome signal that remains matchable, attributable, and
linkable to arm a in segment s. Later sections allow qa,s to vary over an ambiguity set rather than assuming it
is exactly known.
Privacy-preserving reports may also suppress small cells or add randomized reporting noise. A generic released
cell total has the form
eSs =1{N s ≥m}(N s eµs +ξ s),
where Ns is the reported cell count, m is an aggregation threshold, and ξs is randomized reporting noise. This
notation is only meant to make the reporting layer concrete. The rest of the paper works directly with the
released report rs, the degraded arm means it implies, and the set of clean experimental worlds that remain
compatible with that report.
The decision problem is to determine whether the clean incrementality value ∆s remains certified after signal
loss. Let bs ≥0 denote a business threshold for meaningful incremental value. A valid measurement procedure
should certify segment s only when the degraded report supports ∆s > bs uniformly over plausible signal-loss
mechanisms.
4 Signal-Loss Ambiguity Sets
We describe privacy and identity degradation through an ambiguity setU. Each element u∈ Uspecifies a plau-
sible signal-loss mechanism. A mechanism may include treatment-specific match-rate loss, segment-specific
match-rate loss, linkability loss, attribution-window loss, aggregation-threshold suppression, randomized
reporting noise, and segment-heterogeneous signal loss. We write
u= (π a,s, κs, ρa,s, m, σξ, ηs),(2)
where πa,s is the match probability for treatment arm a in segment s, κs controls linkability loss, ρa,s is
attribution-window retention, m is the aggregation threshold, σξ is the randomized reporting-noise scale, and
ηs captures segment-heterogeneous signal loss.
The ambiguity set can be specified from product knowledge, data quality diagnostics, privacy-system doc-
umentation, or stress-test ranges. In a deployed ads setting, these ranges should be read from the reporting
1Corresponding author:shekharp@erau.edu 4

Table 1:Mapping the paper’s signal-loss layers to deployed ads-reporting primitives and model components. Here qa,s is
the reportable-retention multiplier defined in (6). The empirical stress layers are simplified, auditable instantiations of
these primitives over public randomized datasets, not proprietary production API traces.
Signal-loss layer Examples in modern systems Model component
Match-rate loss Missing outcome matches, opt-outs,
unmatched conversions
πa,s,q a,s
Linkability loss Browser, device, or identity fragmen-
tation across events
κs,q a,s
Attribution-window loss Event-level report windows, delayed
or windowed conversion attribution
ρa,s,q a,s
Aggregation-threshold suppres-
sion
Summary reports, conversion-key ag-
gregates, minimum aggregation sizes
m, unresolved cells
Randomized reporting noise Aggregation-service noise, private
summary release, noisy aggregate
measurement
ξg,σ ξ
Segment-heterogeneous signal
loss
Segment-specific reporting quality,
trigger coarsening, prioritized events
ηs, segment-specificU s
contract whenever possible. Attribution Reporting and IPA-style systems expose a small number of operational
primitives such as whether reports are event-level or aggregate, which attribution windows are active, which
keys define summary reports, which small cells are suppressed or clipped, and what randomized reporting
noise or contribution budget is applied. Table 1 gives the mapping used in this paper.
For example,
πa,s ∈[π s, πs], ρ a,s ∈[ρ s, ρs], σ ξ ∈[0, σξ],
with monotonicity or symmetry restrictions when justified. The analyst states the range of signal-loss
mechanisms under which the decision claim should remain valid, and the framework certifies only claims that
hold across that range.
This mapping is the link between the theoretical ambiguity set and real ads privacy systems. A Privacy
Sandbox summary report, for instance, naturally determines a reporting partition, an aggregation threshold or
contribution constraint, and a noise scale for ξg. Event-level reporting determines attribution windows and
coarsened trigger values, which enter through attribution-window loss and segment-heterogeneous signal loss.
IPA-style protocols similarly return aggregate, purpose-limited measurements rather than row-level conversion
labels, so their output is naturally represented as a released reportrs with an associated compatibility fiber. The
paper’s experiments use simplified, auditable stress layers as reproducible approximations to vendor-specific
implementation traces. They test whether incrementality decisions survive the signal losses that these systems
impose.
Assumption 1(Randomization and bounded outcomes).Treatment is randomized with known assignment
probabilities bounded away from zero and one. Outcomes satisfyY i(a)∈[0, B]fora∈ {0,1}.
Assumption 2(Signal-loss ambiguity).The unknown measurement mechanism belongs to a known ambiguity
set U. For each u∈ U, the mechanism specifies loss parameters (defined in (2)) that determine the distribution
of the observed report conditional on the clean randomized experiment.
Compatibility fibers: The information geometry of the problem is captured by the set of clean experimental
worlds that remain compatible with the released report. Let rs denote the privacy-degraded report for segment
s, including observed treated and control summaries, reporting thresholds, and randomized reporting-noise
metadata. For a clean world ηs, which contains the clean arm means and any latent match or attribution
quantities needed to define the estimand, write Tu(ηs) for the report that would be released under signal-loss
mechanismu. The compatibility fiber is
Fs(rs;U) ={η s :there existsu∈ Usuch thatT u(ηs)is compatible withr s}.(3)
1Corresponding author:shekharp@erau.edu 5

The word “compatible” means exact equality for deterministic degraded reports and membership in a high-
probability confidence region when randomized reporting noise is present. The sharp population question
is therefore geometric, asking to project the fiber Fs(rs;U) onto the incrementality functional ∆s(ηs). If
the projection lies entirely above the business threshold, the claim is certifiable. If it lies entirely below the
threshold, the claim is rejectable. If it crosses the threshold, the released report has not preserved enough
information to support either conclusion.
5 Certified Incrementality Bounds
5.1 From compatibility fibers to business decisions
Let ∆s(ηs) denote the clean incrementality value in segment s for a clean world ηs. The sharp population
bounds induced by a released reportr s are
ℓ⋆ s(rs;U) = inf ηs∈Fs(rs;U) ∆s(ηs), u ⋆ s(rs;U) = sup ηs∈Fs(rs;U) ∆s(ηs).(4)
These are identification limits caused by signal loss, with sampling uncertainty added later. Let LBs(α;U) and
UBs(α;U) denote finite-sample lower and upper outer bounds for the clean incrementality value in segment s,
constructed so that they contain the sharp population fiber projection with probability at least 1−α . Their
concrete plug-in form is given in Eq. (8) later. The operational decision rule is
Decision(s) =



Certify,LB s(α;U)> b s,
Reject,UB s(α;U)≤b s,
Unresolved,otherwise.
(5)
This rule deliberately treats unresolved cases as a valid output. If privacy degradation destroys too much
information relative to the business thresholdb s, the correct conclusion is a weaker decision claim.
This decision rule is the practitioner-facing version of the information geometry. The analyst asks what can be
certified for all mechanisms in U, without first selecting a single true signal-loss mechanism. The sharpness of
this logic is given by the certification-frontier in Theorem 5.1, and the general fiber-projection result in Lemma
B.1 in the appendix; the finite-sample validity of the rule is formalized afterward.
5.2 Sharp match and attribution-loss frontier
The fiber projection becomes closed form for the most common ads measurement failure mode. Suppose
outcomes are nonnegative and bounded by B. In segment s, let the observed treated and control means be
eµ1s and eµ0s. Let qa,s denote the combined reportable-retention multiplier in arm a, collecting match-rate
loss, attribution-window loss, and linkability loss when these channels are not separately identifiable. In this
subsection qa,s is an outcome-signal multiplier satisfying eµa,s =q a,sµa,s. It captures retained outcome signal
after reporting loss, while a raw user match rate captures only one possible source of that retention. In the
simplest match-attribution case,
qa,s =π a,sρa,sκs ∈[q a,s, qa,s],0< q a,s ≤ qa,s ≤1.(6)
For nonnegative outcomes, the clean arm meanµ a,s =E[Y i(a)|i∈s]must satisfy
eµa,s
qa,s
≤µ a,s ≤min
(
B, eµa,s
qa,s
)
.
The resulting population signal-loss band is
ℓs(U) = eµ1s q1,s −min
(
B, eµ0s
q0,s
)
, u s(U) = min
(
B, eµ1s
q1,s
)
− eµ0s
q0,s
.(7)
1Corresponding author:shekharp@erau.edu 6

The width of this band is a direct measure of privacy-induced information loss. It widens when retention rates
are poorly known, when treatment and control retention can differ, or when the observed outcomes are sparse.
Theorem 5.1(Sharp privacy-loss certification frontier).Under the bounded nonnegative outcome model above,
with positive retention lower bounds 0< qa,s ≤ qa,s, Eq. (7) is sharp. For every δ∈[ℓ s(U), us(U)], there
exists a clean randomized experiment and a retention mechanism in U that produce the same degraded arm
means and satisfy∆ s =δ. Consequently:
1. ifℓ s(U)> bs, positive incrementality is certifiable uniformly overU;
2. ifu s(U)≤b s, non-incrementality relative tob s is rejectable uniformly overU;
3. if ℓs(U)≤b s < us(U), the released report is intrinsically unresolved. More precisely, there exist two clean
worlds and two mechanisms in U that induce the same released-report distribution, one with ∆s ≤b s and
one with ∆s > bs. Any binary rule that must decide between certification and non-certification from the
released report has worst-case error at least 1/2, and any uniformly valid three-state rule must leave this
report unresolved.
The theorem is the paper’s main identification result. Existing missing-data bounds show that causal effects
may be partially identified when outcomes are not fully observed. Here, partial-identification logic becomes a
sharp measurement decision frontier for privacy-degraded ads reports. The frontier has both a constructive and
an impossibility side. Outside the band, every compatible clean world supports the same decision. Inside the
band, the same released report can be generated by clean worlds on opposite sides of the business threshold, so
a forced binary decision has worst-case error at least1/2. The unresolved region is therefore an information-
theoretic part of the compatibility fiber, where the degraded report has not preserved enough information to
certify or reject the claim.
5.3 Finite-sample and reporting-noise certification
Population sharpness is not enough for deployment because reports are finite and may contain randomized
reporting noise. We keep the match-attribution relation from the previous subsection, eµa,s =q a,sµa,s with
qa,s ∈[q a,s, qa,s], and replace the population degraded mean by a simultaneous confidence interval. Let
[eµa,s(α), eµa,s(α)]
be simultaneous confidence bounds for eµa,s, including bounded-outcome randomization uncertainty and
randomized reporting-noise uncertainty. Since smaller retention implies a larger compatible clean mean, the
clean arm mean lies in the outer interval
µa,s ∈
" eµa,s(α)
qa,s
,min
(
B, eµa,s(α) qa,s
)#
.
Taking the smallest compatible treated mean minus the largest compatible control mean gives the finite-sample
lower bound, and taking the largest compatible treated mean minus the smallest compatible control mean gives
the finite-sample upper bound:
LBs(α;U) =
eµ1,s(α)
q1,s
−min
(
B, eµ0,s(α) q0,s
)
,UB s(α;U) = min
(
B, eµ1,s(α) q1,s
)
−
eµ0,s(α)
q0,s
.(8)
The finite-sample guarantee follows directly from simultaneous coverage of the degraded arm means. Suppose
Assumptions 1 and 2 hold, and the degraded mean intervals used in Eq. (8) have simultaneous coverage at
least1−αover the reported segment collection. Then, with probability at least1−α,
LBs(α;U)≤∆ s ≤UB s(α;U)for all reported segmentss.
1Corresponding author:shekharp@erau.edu 7

Consequently, Eq. (5) controls false certification and false rejection simultaneously over all reported segments
and all signal-loss mechanisms inU.
This is the sampling-theory layer. It says that a certified claim has survived three filters at once: bounded-
outcome randomization uncertainty, randomized reporting noise, and worst-case signal loss in U. A rejected
claim has failed the same robust test. An unresolved claim is one whose finite-sample, privacy-degraded
compatibility interval still crosses the threshold.
5.4 Sample complexity and privacy utility
The finite-sample bound also gives a sample-complexity diagnostic. Let qmin = mina,s qa,s. If qmin is small,
every observed degraded mean must be rescaled more aggressively to recover a clean mean, so randomization
error is amplified. If the retention intervals are wide, there is also an irreducible identification width that more
samples cannot remove.
Proposition 5.2(Sample complexity under privacy signal loss).Consider a finite reported segment collection
C and balanced per-arm sample size ns ≥n in every segment. Suppose Yi(a)∈[0, B] , qa,s ∈[q a,s, qa,s],
qmin = mina,s qa,s >0 , and independent mean-zero randomized reporting noise added to each arm total is
sub-Gaussian with variance proxyσ 2 ξ. With probability at least1−α, all segment effects satisfy
∆s ∈[ℓ s(U)−Rad n, us(U) + Radn],Rad n = 2B qmin
r
log(4|C|/α)
2n + 2σξ qminn p 2 log(4|C|/α).(9)
Consequently, achieving finite-sample radiusRad n ≤εis guaranteed if
n≳max
(
B2
q2 minε2 log |C| α , σξ qminε
r
log |C| α
)
.(10)
The remaining width us(U)−ℓ s(U) is an identification cost of signal-loss uncertainty. It persists as n grows
unless the ambiguity setUitself tightens.
The rate in Eq. (10) is the coverage penalty in concrete form. If only half of outcomes are matchable and
attributable, the sampling-driven requirement scales by roughly 4. If only one fifth are reliably retained, it
scales by roughly 25. Sample size addresses sampling error, while measurement diagnostics address the
population band [ℓs(U), us(U)]. More impressions shrink Radn, and better diagnostics tighten the ambiguity
setU.
Theorem 5.3(Minimax lower bound for signal-loss measurement).Consider one segment with binary
conversion value Yi(a)∈ {0, B}for a known scale B >0. Let pa = Pr{Yi(a) =B}, a∈ {0,1},denote the
clean conversion probability in arm a, so the clean incrementality target is ∆ =B(p 1 −p 0). In each arm,
the analyst observes only eYi(a) =R i(a)Yi(a), where Ri(a)∼Bernoulli(q) is independent retention and
q∈(0,1] is known. With n observations per arm, every estimator b∆ based only on the degraded observations
satisfies
sup
p0,p1∈[1/4,3/4]
Ep0,p1
h

 b∆−B(p 1 −p 0)

 i ≥c B√qn ,
for a universal constant c >0 , whenever qn is large enough. Consequently, any estimator that attains
constant-probability error at most ε uniformly over this class requires n≥c ′ B2 qε2 for a universal constant
c′ >0 . If q is not known and only q∈[q , q] is known, then even with infinite data the minimax absolute error
is at least B 4

1−
q
q

.
The theorem explains why the sample-complexity penalty reflects a real loss of information. Retention loss
reduces the effective number of observed conversion trials, so the clean-data rate is no longer attainable from
the degraded report. In addition, uncertainty about the retention mechanism creates an identification floor
1Corresponding author:shekharp@erau.edu 8

that no estimator can remove from the released report alone. The lower bound is stated for binary conversion
outcomes, while Proposition 5.2 gives a conservative sufficient bound for bounded outcomes and noisy reports.
Together they give the same planning message. More samples can reduce finite-sample uncertainty, but
information omitted by the privacy-degraded report remains unavailable unless the ambiguity set itself is
tightened.
Aggregation-threshold suppression and randomized reporting noise affect certification through the standard
error of released cell means. If a reported cell g has treated and control counts N1g and N0g, and the report
adds independent mean-zero noise with variance σ2 ξ to each arm total, a conservative variance proxy for the
released treated-control difference is
bV priv g = bV rand g +σ 2 ξ

1
N 2 1g + 1 N 2 0g
!
.(11)
Here bV rand g is the usual randomization variance proxy for the clean difference in means, and the second term
is the reporting-noise penalty after converting noisy arm totals into noisy arm means. This penalty is small
for large cells and severe for small cells, which is why privacy-preserving reports often support aggregate
campaign conclusions before they support fine segment-level claims.
For a two-arm randomized experiment with assignment-unit variance proxy σ2 s, effective per-arm cell size Ns,
and randomized reporting-noise varianceσ 2 ξ, the corresponding conservative minimum detectable effect is
MDEpriv s =  z1−α/2 +z 1−β 
s
2σ2s
Ns
+σ 2 ξ
 1
N 2 1s + 1 N 2 0s

.(12)
The first quantile controls the two-sided type-I error rateα, and the second controls power 1−β . If the positive
population signal-loss margin ℓs(U)−b s is smaller than MDEpriv s , then certification is not expected to be
statistically powered at level (α, β). The MDE formula is therefore a planning diagnostic. It separates cases
where the campaign effect is too small from cases where randomized reporting noise, sparse cells, or retention
uncertainty make the privacy-degraded report too weak for certification. Appendix Proposition B.2 gives the
derivation.
5.5 Reporting granularity and segment geometry
Privacy reports are often released over a partitionP of users, campaigns, geographies, devices, or time windows.
Finer partitions are more interpretable and better aligned with segment safety, while smaller cells increase
aggregation-threshold suppression. Coarser partitions reduce randomized reporting noise and missing-cell
risk, while larger cells can hide segment-heterogeneous signal loss. This tradeoff can be made explicit.
To see the tradeoff mathematically, suppose the segment-level treatment effect function isH-Lipschitz over a
segment metricd seg. For any reported cellg∈ P, define
diam(g) = sup
s,s′∈g
dseg(s, s′), ¯∆g = X
s∈g
ws|g∆s,
where ¯∆g is the within-cell weighted average effect. The Lipschitz condition implies that every segment s∈g
is no more than Hdiam(g) below the cell average. Therefore, if the cell-level robust lower bound satisfies
¯∆g ≥LB g(α;U)on the simultaneous coverage event, then every segments∈gsatisfies
∆s ≥LB g(α;U)−Hdiam(g).
Thus cellgsupports segment-safe certification whenever
LBg(α;U)−Hdiam(g)> b g.(13)
This calculation gives a practical rule for choosing reporting granularity. A coarse cell has larger Nag, so
Eq. (11) is smaller and aggregation-threshold suppression is less likely. The same coarse cell can have larger
1Corresponding author:shekharp@erau.edu 9

diam(g), which increases the heterogeneity penalty Hdiam(g). The empirical implementation estimates this
penalty from the data by nesting the finest reporting cells inside each coarser reported cell, computing the
treatment-effect dispersion of those finest cells, and using the maximum deviation from the coarser cell’s
weighted average as the observed Hdiam(g) proxy. The best reporting partition is determined by the balance
between randomized reporting-noise reduction and the segment heterogeneity it averages over.
5.6 Segment safety under heterogeneous signal loss
Aggregate incrementality can be certified even when subgroup claims are not. LetC be a collection of segments,
such as device types, channels, customer history groups, geography, or advertiser categories. The framework
certifies segment safety by requiring
LBs(α/|C|;U)> b s for everys∈ C
or by reporting which segments remain unresolved after multiplicity correction. This step is important because
signal loss is often heterogeneous. For example, match-rate loss may differ by channel, attribution-window
loss may differ by customer history, and aggregation-threshold suppression may disproportionately affect
small segments.
This segment-safety check is substantive. Appendix B.5 gives a constructive example in which two signal-loss
mechanisms induce the same aggregate degraded lift and lead the segment-level rule to certify different
segments. The practical warning is that a campaign can appear incrementally positive in aggregate while
the evidence is insufficient for one or more segments. The proposed decision object makes this visible by
returning unresolved segment claims directly.
6 Robust Incrementality Certification Algorithm
Algorithm 1 summarizes the proposed method. The algorithm takes randomized experimental data, an
ambiguity set of signal-loss mechanisms, reporting thresholds, randomized reporting-noise parameters, and
business decision thresholds. It returns three sets indicating certified, rejected, and unresolved cases. In the
match-attribution implementation used in the experiments, the worst case overU has the closed form in Eq. (7),
so match-rate loss, attribution-window loss, and linkability loss enter through the retained-signal interval
[qa,s, qa,s].
The validity of Algorithm 1 is an immediate consequence of the finite-sample certification logic in Section 5.3.
On the simultaneous coverage event for the finite-sample bounds, the algorithm certifies only segments with
∆s > bs, rejects only segments with ∆s ≤b s, and leaves the remaining segments unresolved by construction.
The operational interpretation is simple. If the ambiguity set is wide, the algorithm returns more unresolved
decisions. If the measurement system improves, the ambiguity set tightens and certification becomes easier.
7 Empirical Results
7.1 Datasets
The empirical analysis uses two randomized datasets.
Criteo Uplift: The Criteo dataset contains anonymized covariates, treatment assignment, exposure, visits,
and conversions from a large advertising incrementality setting [Diemert et al., 2018, Criteo AI Lab, 2021].
The experiments use 2,000,000 rows, with treated share 0.850 and conversion rate 0.00293. It is the main
large-scale ads dataset. Its treatment imbalance and low conversion rates make it useful for studying sparse
conversion certification and randomized reporting-noise sensitivity.
Hillstrom email experiment: The Hillstrom dataset contains randomized email treatment arms, customer
history features, visits, conversions, and spend [Hillstrom, 2008]. The experiments use all64,000rows, with
1Corresponding author:shekharp@erau.edu 10

Algorithm 1Privacy-robust incrementality certification
Require: Randomized experiment D, segment collection C, ambiguity set U, business thresholds {bs}s∈C,
error levelα.
Ensure:Certified setC cert, rejected setC reject, and unresolved setC unres.
1:Identify the cell collectionC cell ⊆ Cinduced by the reporting partition, and set the per-arm error level to
αarm =α/max{2|C cell|,1}.
2:Initialize the suppressed setC supp ← ∅.
3:foreach segments∈ Cdo
4: Estimate treated and control degraded means and arm counts in segment s, the inputs to Eqs. (7)
and (8).
5:ifthe reporting count is below the aggregation thresholdthen
6:Marksas aggregation-suppressed by updatingC supp ← Csupp ∪ {s}.
7:else
8:ConvertUto retained-signal endpointsq a,s and qa,s as in Eq. (7).
9: Construct simultaneous degraded-mean bounds using αarm, the bounded-outcome Hoeffding
radius, and the reporting-noise radius summarized in Eq. (9).
10:ConstructLB s(α;U)andUB s(α;U)by plugging the endpoint worst cases into Eq. (8).
11:end if
12:end for
13:C cert ← {s∈ C \ Csupp : LBs(α;U)> b s}as in Eq. (5).
14:C reject ← {s∈ C \ Csupp : UBs(α;U)≤b s}as in Eq. (5).
15:C unres ← C \(Ccert ∪ Creject)as in Eq. (5).
16:returnC cert,C reject,C unres.
treated share 0.667, conversion rate 0.00903, and mean spend 1.051. It is smaller and more interpretable than
Criteo. It is useful for segment-level decision analysis because customer history, channel, and demographic-like
variables define natural reporting cells.
7.2 Signal-loss stress layers
Public datasets provide randomized treatment and outcomes without paired pre-privacy identity graphs and
post-privacy production reports, so we introduce controlled signal-loss layers over real randomized experiments.
Table 1 gives the reporting-system interpretation of these layers; this subsection describes the corresponding
implementation. The experimental implementation uses an explicit stress tuple consisting of match rate,
attribution retention, linkable-identity retention, aggregation threshold, and reporting-noise scale. Match-rate
loss is implemented by multiplying clean treated and control arm means by a match component that lowers the
share of outcomes remaining matchable to the randomized experiment; attribution-window loss is implemented
by a second retention component that lowers the matched share retained inside the reporting window; linkability
loss is implemented by a third retention component that lowers the share of outcomes still linkable to the same
experimental unit. In the aggregate certification frontier, these three components are set equal to q1/3, so their
product is the reportable-retention parameter qtrue ∈ {0.95,0.80,0.65,0.50,0.35,0.25}. The corresponding
retention half-widths are ω∈ {0.04,0.06,0.08,0.10,0.12,0.14} , so the decision rule constructs the interval
[qtrue −ω, qtrue +ω] , clipped to [0.02,1] , and applies the sharp match-loss band and finite-sample band to the
degraded arm means. Aggregation-threshold suppression is implemented by checking reported cell counts
against m∈ {50,100,150,250,400,600} for the six aggregate stress settings; suppressed cells are assigned
the unresolved state rather than a numerical certificate, and in the granularity analysis the fixed reporting-cell
threshold is m= 100 . Randomized reporting noise is implemented as Gaussian arm-total uncertainty with
scale σξ, which enters the finite-sample radius after division by the treated and control cell counts. The six
aggregate stress settings useσξ = (1.0,1.6,2.0,2.5,3.0,4.0) for Criteo and σξ = (0.4,0.64,0.8,1.0,1.2,1.6)
for Hillstrom. Segment-heterogeneous signal loss is separately implemented in the granularity diagnostic
by letting each reporting cell have its own retention interval and noise scale as a function of cell size and a
deterministic cell-level jitter, and by adding a data-driven heterogeneity penalty equal to the largest nested
1Corresponding author:shekharp@erau.edu 11

Figure 2:Population and finite-sample certification frontiers under auditable signal-loss stress layers. The purple curve
is the population lower bound, which applies signal-loss uncertainty while treating the degraded arm means as exactly
known. The green curve is the finite-sample lower bound, which adds simultaneous randomization uncertainty and
randomized reporting-noise uncertainty to the same signal-loss band. A claim can therefore be population-certifiable and
still finite-sample unresolved.
fine-cell treatment-effect deviation inside the reported cell. This keeps the empirical procedure aligned with
the theory in the sense that the implementation uses auditable reporting-primitive stress tests over public
randomized data, while production identity graphs and conversion timestamps remain unavailable.
7.3 Population and finite-sample certification
The first empirical distinction mirrors the two layers of the theory. The population signal-loss band asks
what would be certifiable with exactly known degraded arm means and a retention mechanism known
only through U. This is the object in Theorem 5.1. The finite-sample band then adds bounded-outcome
randomization uncertainty, randomized reporting-noise uncertainty, and multiplicity correction across the
reported cells within the evaluated report, as described in Section 5.3. The six stress settings are evaluated as
separate planning scenarios, with multiplicity correction applied within each report. A claim can therefore be
population-certifiable and still finite-sample unresolved.
Figure 2 shows the distinction directly. The population curve answers anidentificationquestion that if
the degraded report were known without sampling error, would the signal-loss ambiguity set still allow
certification? The finite-sample curve answers thedeploymentquestion that after adding simultaneous
confidence radii and reporting-noise uncertainty, does the lower bound still clear the business threshold? In
Criteo, the clean conversion lift is 0.001117, compared with a business threshold of 0.0005. The population
robust lower bound certifies the claim at q= 0.95 and q= 0.80 , with lower bounds 0.000905 and 0.000740.
At q= 0.65 , it reaches 0.000499, just below the threshold. The finite-sample lower bound is negative
throughout, ranging from −0.00323 at q= 0.95 to −0.02945 at q= 0.25 . In Hillstrom, the clean conversion
lift is 0.004955, compared with a threshold of0.001. Population certification survives through q= 0.50 , where
the lower bound is 0.001743, and becomes unresolved at q= 0.35 and below. As in Criteo, all finite-sample
decisions are unresolved. This is the intended output of a conservative measurement system when the released
report has limited information for a stronger deployed decision.
7.4 Sample complexity and information loss
The second diagnostic connects the finite-sample radius in Eq. (9), the sufficient sample-size condition in
Eq. (10), and the lower-bound rate in Theorem 5.3. The left panel of Figure 3 evaluates Radn from Eq. (9)
over a grid of per-arm sample sizes n and reportable-retention levels qmin, using B= 1 , |C|= 24 , and
α= 0.05 . The plotted curves set σξ = 0 to isolate the retention-driven sampling penalty; the reporting-noise
term in Eq. (9) is included in the implementation and affects finite-sample certification in Figure 2. The right
1Corresponding author:shekharp@erau.edu 12

Figure 3:Sample-complexity and minimax scaling under privacy signal loss. The left panel evaluates the finite-sample
radius Radn from Eq. (9) as the per-arm sample size and reportable-retention lower bound qmin vary. The right panel
evaluates the implemented constant-scaled minimax curve 0.08B/ √qn, corresponding to the universal-constant lower-
bound rate in Theorem 5.3. Lower retention enlarges both quantities, showing that privacy signal loss reduces effective
information rather than merely adding a removable constant error.
panel plots the constant-scaled minimax curve 0.08B/ √qn, which is the implemented visualization of the
universal-constant lower-bound rate in Theorem 5.3. Thus the figure compares the upper-bound planning
radius used by the certification rule with the information-theoretic lower-bound scale that no estimator can
uniformly beat.
Figure 3 shows the expected 1/q2 min-type sample burden from the first term of Eq. (10). To reach Radn ≤
ε= 0.02 , the sufficient per-arm sample size is 186,669 at qmin = 0.90, 604,807 at qmin = 0.50, and 6.72
million at qmin = 0.15. For a tighter radius ε= 0.005 , the corresponding qmin = 0.15 requirement is 107.5
million per arm. The minimax curve gives the complementary impossibility statement from Theorem 5.3
that when only a small share q of outcomes remains reportable, the effective information scale is qn, so no
estimator observing the same degraded report can uniformly recover clean incrementality at the clean-data rate.
The sample-complexity panel and the minimax panel therefore make the same point from opposite directions.
Eq. (10) states how many observations are sufficient for the deployed bound to shrink, while Theorem 5.3
shows why theq-dependent slowdown is unavoidable.
7.5 Granularity and segment safety
The third diagnostic tests the reporting-granularity logic in Section 5.5 and the segment-safety logic above.
The experiment forms increasingly fine reporting partitions in both datasets using binary conversion outcomes,
α= 0.05 , bounded outcome scale B= 1 , and business thresholds 0.0005 for Criteo and 0.001 for Hillstrom.
The Criteo partitions are {f0}, {f0,f1} , {f0,f1,f2} , and {f0,f1,f2,logged exposure} , where
the feature buckets are quartile buckets of the anonymized features. The Hillstrom partitions are {channel},
{channel,zip} , {channel,zip,history} , and {channel,zip,history,recency} , with re-
cency also quartile-bucketed. For each reported cellgwith row countn g, the implementation sets
bqg = clip

0.70 + clip
 log(ng/500)
20 ,−0.10,0.10

+ζ g,0.35,0.92

,
where ζg ∈[−0.05,0.05] is a deterministic cell-level jitter used only to create reproducible segment-
heterogeneous signal loss. The retention interval is
[max{0.02,bqg −ω g},min{1,bqg +ω g}], ω g = 0.08 + (250−n g)+ 2500 ,
and the reporting-noise scale is
σξ,g = 1 + (200−n g)+ 200 .
1Corresponding author:shekharp@erau.edu 13

Figure 4:Reporting granularity diagnostics. The horizontal axis is the number of reported cells in the partition. The left
panel compares the share of cells that clear the population signal-loss lower bound with the share that clear the finite-sample
lower bound after simultaneous uncertainty and reporting noise are added. The middle panel reports aggregation-threshold
suppression with fixed threshold m= 100. The right panel reports the empirical segment-heterogeneity penalty, computed
as the largest nested fine-cell treatment-effect deviation inside each reported cell and used as a proxy for Hdiam(g) in
Eq. (13). Finer reports reduce this heterogeneity penalty but create smaller cells and more suppression, so aggregate or
population-level lift should not be read as subgroup safety.
Cells with ng <100 are marked aggregation-suppressed and assigned the unresolved state. Non-suppressed
cells are evaluated by the same population and finite-sample certification rules used in Figure 2, with the
finite-sample correction applied simultaneously over the cells in the current report.
The segment-safety penalty is computed by nesting the finest partition inside every coarser reported cell.
For each valid finest cell f⊂g with at least 80 rows and both treatment arms present, the implementation
computes b∆f = ¯Y1f − ¯Y0f . It then forms the row-weighted average b¯∆g = P f⊂g wf|g b∆f and uses
bHdiam(g) = max
f⊂g

 b∆f − b¯∆g

as the empirical proxy for the heterogeneity term in Eq. (13). The reported segment-safe lower bound is
therefore the finite-sample lower bound minus this penalty.
Figure 4 shows why segment certification is difficult under privacy constraints. In Criteo, population cell
certification is about 25% for the coarse and medium partitions, 28.6% for the fine partition, and only 2.8% for
the very fine partition. In Hillstrom, population certification is 100% for coarse and medium partitions, 61.4%
for the fine partition, and 36.0% for the very fine partition. Finer reports reduce the empirically estimated
nested-cell heterogeneity penalty and create sparse cells with aggregation-threshold suppression. Aggregation-
threshold suppression reaches 8.4% in the finest Criteo partition and 39.5% in the finest Hillstrom partition. In
the current stress layers, every finite-sample cell-level decision is unresolved and every segment-safe decision
is also unresolved under the three-state rule. This agrees with the theory in the sense that the framework
should refuse a subgroup claim when the lower bound, randomized reporting noise, multiplicity correction,
and heterogeneity penalty do not jointly clear the business threshold.
8 Discussion
The proposed framework treats privacy-preserving ads measurement as a causal decision problem under
incomplete observation. This framing differs from both pure attribution and pure privacy-protocol design.
Attribution asks how to allocate credit among touchpoints. Privacy protocols ask how to report measurements
while protecting individuals. Privacy-robust incrementality asks what causal claim remains justified after the
measurement signal has been degraded.
This distinction matters for platform decisions. A privacy-preserving report can be technically valid yet
decision-insufficient. A randomized experiment can be causally valid in design while linkability loss,
attribution-window loss, or randomized reporting noise still prevent fine-grained lift certification. The frame-
work makes this insufficiency explicit by outputting unresolved claims instead of overconfident estimates.
1Corresponding author:shekharp@erau.edu 14

9 Limitations and Future Work
The framework depends on the ambiguity set U. If the analyst excludes plausible signal-loss mechanisms,
the certification rule may be too optimistic. The empirical design also uses controlled stress layers because
public datasets lack the complete pre-privacy and post-privacy measurement process. The stress layers are
semantics-faithful abstractions of modern ads reporting primitives, and their numerical bands should be
interpreted as reproducible stress-test results for the stated public-data setting. This limitation reflects the
realistic setting for reproducible research on privacy-constrained advertising measurement. Future work should
evaluate the framework against production reporting logs or browser-level API traces, richer identity graphs,
auction-level ads data, and adaptive experimentation policies that choose between additional measurement and
launch decisions. Appendix A provides additional diagnostics that isolate the fiber geometry, privacy-aware
MDE behavior, and heterogeneous signal-loss reversals.
10 Conclusion
Privacy constraints are now part of the statistical environment for advertising measurement. Randomization
remains essential, and privacy-degraded reports require an additional certification layer when match-rate loss,
linkability loss, attribution-window loss, aggregation-threshold suppression, randomized reporting noise, and
segment-heterogeneous signal loss are present. This paper proposes a privacy-robust incrementality framework
that converts randomized marketing evidence into certified, rejected, and unresolved decision claims. The
empirical results reinforce the theoretical message. Positive clean lift and favorable population lower bounds
can still fall short of deployment certification once finite-sample uncertainty and randomized reporting noise
are included. The contribution is a frontier-based certification layer for modern ads systems. It preserves the
strength of randomized experiments while making explicit when privacy-degraded data are insufficient for a
causal decision.
Code availability.The implementation is available in the GitHub repository.
References
Google Privacy Sandbox. Attribution reporting: Full system overview. https://privacysandbox.
google.com/private-advertising/attribution-reporting/system-overview ,
2025a. Accessed 2026-05-27.
Google Privacy Sandbox. Private aggregation api fundamentals. https://privacysandbox.google.
com/private-advertising/private-aggregation/fundamentals, 2025b. Accessed
2026-05-27.
Benjamin M. Case, Richa Jain, Alex Koshelev, Andy Leiserson, Daniel Masny, Thurston Sandberg, Ben
Savage, Erik Taubeneck, Martin Thomson, and Taiki Yamaguchi. Interoperable private attribution: A
distributed attribution and aggregation protocol.IACR Cryptology ePrint Archive, 2023.
Hidayet Aksu, Badih Ghazi, Pritish Kamath, Ravi Kumar, Pasin Manurangsi, Adam Sealfon, and Avinash V .
Varadarajan. Summary reports optimization in the privacy sandbox attribution reporting api.Proceedings
on Privacy Enhancing Technologies, 2024(4):605–621, 2024. doi: 10.56553/popets-2024-0132.
Pierre Tholoniat, Kelly Kostopoulou, Peter McNeely, Prabhpreet Singh Sodhi, Anirudh Varanasi, Benjamin
Case, Asaf Cidon, Roxana Geambasu, and Mathias Lécuyer. Cookie monster: Efficient on-device budgeting
for differentially-private ad-measurement systems. InProceedings of the ACM SIGOPS 30th Symposium on
Operating Systems Principles, pages 693–708, 2024. doi: 10.1145/3694715.3695965.
1Corresponding author:shekharp@erau.edu 15

Pierre Gutierrez and Jean-Yves Gérardy. Causal inference and uplift modelling: A review of the literature.
InProceedings of The 3rd International Conference on Predictive Applications and APIs, volume 67 of
Proceedings of Machine Learning Research, pages 1–13. PMLR, 2017.
Leo Guelman, Montserrat Guillén, and Ana M. Pérez-Marín. Ensemble methods for uplift modeling.Data
Mining and Knowledge Discovery, 29:1531–1559, 2015. doi: 10.1007/s10618-014-0383-9.
Krzysztof Ruda´s and Szymon Jaroszewicz. Linear regression for uplift modeling.Data Mining and Knowledge
Discovery, 32(5):1275–1305, 2018. doi: 10.1007/s10618-018-0576-8.
Diego Olaya, Kristof Coussement, and Wouter Verbeke. A survey and benchmarking study of mul-
titreatment uplift modeling.Data Mining and Knowledge Discovery, 34(2):273–308, 2020. doi:
10.1007/s10618-019-00670-y.
Eustache Diemert, Artem Betlei, Christophe Renaudin, and Massih-Reza Amini. A large scale benchmark for
uplift modeling. InProceedings of the AdKDD and TargetAd Workshop, 2018.
Eustache Diemert, Artem Betlei, Christophe Renaudin, Massih-Reza Amini, Théophane Gregoir, and Thibaud
Rahier. A large scale benchmark for individual treatment effect prediction and uplift modeling.arXiv
preprint arXiv:2111.10106, 2021.
Artem Betlei, Eustache Diemert, and Massih-Reza Amini. Treatment targeting by auuc maximization with
generalization guarantees.arXiv preprint arXiv:2012.09897, 2020.
Brett R. Gordon, Florian Zettelmeyer, Neha Bhargava, and Dan Chapsky. A comparison of approaches to
advertising measurement: Evidence from big field experiments at facebook.Marketing Science, 38(2):
193–225, 2019. doi: 10.1287/mksc.2018.1135.
Brett R. Gordon, Robert Moakler, and Florian Zettelmeyer. Close enough? a large-scale exploration of
non-experimental approaches to advertising measurement.Marketing Science, 42(4):768–793, 2023. doi:
10.1287/mksc.2022.1413.
Garrett A. Johnson. Inferno: A guide to field experiments in online display advertising.Journal of Economics
& Management Strategy, 32(3):469–490, 2023.
Garrett A. Johnson, Randall A. Lewis, and Elmar I. Nubbemeyer. Ghost ads: Improving the economics of
measuring online ad effectiveness.Journal of Marketing Research, 54(6):867–884, 2017. doi: 10.1509/jmr.
15.0297.
Randall A. Lewis and Justin M. Rao. On the near impossibility of measuring the returns to advertising.The
Quarterly Journal of Economics, 130(4):1941–1973, 2015. doi: 10.1093/qje/qjv023.
Jon Vaver and Jim Koehler. Measuring ad effectiveness using geo experiments. Technical report, Google,
2011.
Aiyou Chen and Timothy C Au. Robust causal inference for incremental return on ad spend with randomized
paired geo experiments.The Annals of Applied Statistics, 16(1):1–20, 2022.
Kay H. Brodersen, Fabian Gallusser, Jim Koehler, Nicolas Remy, and Steven L. Scott. Inferring causal impact
using bayesian structural time-series models.The Annals of Applied Statistics, 9(1):247–274, 2015. doi:
10.1214/14-AOAS788.
Ron Berman and Elea McDonnell Feit. Latent stratification for incrementality experiments.Marketing Science,
43(4):903–917, 2024. doi: 10.1287/mksc.2022.0297.
Prasad Chalasani, Ari Buchalter, Jaynth Thiagarajan, and Ezra Winston. Counterfactual-based incrementality
measurement in a digital ad-buying platform.arXiv preprint arXiv:1705.00634, 2017.
Wei Sun, Peng Wang, Dawei Yin, Jian Yang, and Yi Chang. Causal inference via sparse additive models
with application to online advertising. InProceedings of the AAAI Conference on Artificial Intelligence,
volume 29, 2015. doi: 10.1609/aaai.v29i1.9156.
1Corresponding author:shekharp@erau.edu 16

CH Liu, Elaine M Bettaney, and Benjamin Paul Chamberlain. Designing experiments to measure incrementality
on facebook.arXiv preprint arXiv:1806.02588, 2018.
Brett R Gordon, Robert Moakler, and Florian Zettelmeyer. Predicted incrementality by experimentation (pie)
for ad measurement. Technical report, National Bureau of Economic Research, 2026.
Eustache Diemert, Julien Meynet, Pierre Galland, and Damien Lefortier. Attribution modeling increases
efficiency of bidding in display advertising. InProceedings of the ADKDD’17, pages 1–6. 2017.
Ruihuan Du, Yu Zhong, Harikesh Nair, Bo Cui, and Ruyang Shou. Causally driven incremental multi touch
attribution using a recurrent neural network.arXiv preprint arXiv:1902.00215, 2019.
Di Yao, Chang Gong, Lei Zhang, Sheng Chen, and Jingping Bi. Causalmta: Eliminating the user confounding
bias for causal multi-touch attribution. InProceedings of the 28th ACM SIGKDD Conference on Knowledge
Discovery and Data Mining, pages 4342–4352, 2022.
Cynthia Dwork. Differential privacy: A survey of results. InTheory and Applications of Models of
Computation, volume 4978 ofLecture Notes in Computer Science, pages 1–19. Springer, 2008. doi:
10.1007/978-3-540-79228-4_1.
Cynthia Dwork and Aaron Roth. The algorithmic foundations of differential privacy.Foundations and Trends
in Theoretical Computer Science, 9(3–4):211–407, 2014. doi: 10.1561/0400000042.
John Delaney, Badih Ghazi, Charlie Harrison, Christina Ilvento, Ravi Kumar, Pasin Manurangsi, Martin Pál,
Karthik Prabhakar, and Mariana Raykova. Differentially private ad conversion measurement.Proceedings
on Privacy Enhancing Technologies, 2024(2):124–140, 2024. doi: 10.56553/popets-2024-0044.
Badih Ghazi, Charlie Harrison, Arpana Hosabettu, Pritish Kamath, Alexander Knop, Ravi Kumar, Mariana
Raykova, Pasin Manurangsi, Ethan Leeman, Vikas Sahu, and Phillipp Schoppmann. On the differential
privacy and interactivity of privacy sandbox reports.Proceedings on Privacy Enhancing Technologies, 2025
(3):382–397, 2025. doi: 10.56553/popets-2025-0104.
Meta Audience Network. Update: How to manage apple’s ios 14 live changes.
https://en-gb.facebook.com/audiencenetwork/resources/blog/
update-how-to-manage-apple-ios-14-live-changes , 2021. Discusses Meta’s Ag-
gregated Event Measurement and Apple’s SKAdNetwork.
Yingtai Xiao, Jian Du, Shikun Zhang, Wanrong Zhang, Qiang Yan, Danfeng Zhang, and Daniel Kifer. Click
without compromise: Online advertising measurement via per user differential privacy. InProceedings of
the 2025 IEEE Symposium on Security and Privacy, pages 2919–2937, 2025. doi: 10.1109/SP61157.2025.
00187.
Ke Zhong, Yiping Ma, and Sebastian Angel. Ibex: Privacy-preserving ad conversion tracking and bidding.
InProceedings of the 2022 ACM SIGSAC Conference on Computer and Communications Security, pages
3223–3237, 2022. doi: 10.1145/3548606.3560651.
Conor O’Brien, Arvind Thiagarajan, Sourav Das, Rafael Barreto, Chetan Verma, Tim Hsu, James Neufield,
and Jonathan J Hunt. Challenges and approaches to privacy preserving post-click conversion prediction.
arXiv preprint arXiv:2201.12666, 2022.
Joel L. Horowitz and Charles F. Manski. Nonparametric analysis of randomized experiments with missing
covariate and outcome data.Journal of the American Statistical Association, 95(449):77–84, 2000. doi:
10.1080/01621459.2000.10473902.
Guido W. Imbens and Charles F. Manski. Confidence intervals for partially identified parameters.Econometrica,
72(6):1845–1857, 2004. doi: 10.1111/j.1468-0262.2004.00555.x.
Charles F. Manski and John V . Pepper. Monotone instrumental variables: With an application to the returns to
schooling.Econometrica, 68(4):997–1010, 2000. doi: 10.1111/1468-0262.00144.
1Corresponding author:shekharp@erau.edu 17

Amy Richardson, Michael G. Hudgens, Peter B. Gilbert, and Jason P. Fine. Nonparametric bounds and
sensitivity analysis of treatment effects.Statistical Science, 29(4):596–618, 2014. doi: 10.1214/14-STS499.
Alexander Coppock, Alan S. Gerber, and Donald P. Green. Combining double sampling and bounds to address
nonignorable missing outcomes in randomized experiments.Political Analysis, 25(2):188–206, 2017. doi:
10.1017/pan.2016.6.
Erin E. Gabriel, Arvid Sjölander, and Michael C. Sachs. Nonparametric bounds for causal effects in imperfect
randomized experiments.Journal of the American Statistical Association, 118(541):684–692, 2023. doi:
10.1080/01621459.2021.1950734.
Anish Agarwal and Rahul Singh. Causal inference with corrupted data: Measurement error, missing values,
discretization, and differential privacy.arXiv preprint arXiv:2107.02780, 2021.
Yuki Ohnishi and Jordan Awan. Locally private causal inference for randomized experiments.Journal of
Machine Learning Research, 26:1–40, 2025.
Fengshi Niu, Harsha Nori, Brian Quistorff, Rich Caruana, Donald Ngwe, and Aadharsh Kannan. Differentially
private estimation of heterogeneous causal effects. InConference on Causal Learning and Reasoning, pages
618–633. PMLR, 2022.
Nathan Kallus and Angela Zhou. Confounding-robust policy improvement. InAdvances in Neural Information
Processing Systems, volume 31, pages 9289–9299, 2018.
Adith Swaminathan and Thorsten Joachims. Counterfactual risk minimization: Learning from logged bandit
feedback. InProceedings of the 32nd International Conference on Machine Learning, volume 37 of
Proceedings of Machine Learning Research, pages 814–823. PMLR, 2015.
Yi Su, Maria Dimakopoulou, Akshay Krishnamurthy, and Miroslav Dudík. Doubly robust off-policy evaluation
with shrinkage. InProceedings of the 37th International Conference on Machine Learning, volume 119 of
Proceedings of Machine Learning Research, pages 9167–9176. PMLR, 2020.
Prashant Shekhar and Caroline Howard. Choosing online experiment designs under interference in ads,
recommendations, and member-experience systems.arXiv preprint arXiv:2605.25290, 2026a.
Prashant Shekhar and Caroline Howard. Support-aware offline policy selection for advertising marketplaces.
arXiv preprint arXiv:2605.21736, 2026b.
Criteo AI Lab. Criteo uplift prediction dataset. https://ailab.criteo.com/
criteo-uplift-prediction-dataset/, 2021.
Kevin Hillstrom. Minethatdata e-mail analytics and data mining challenge dataset. https://blog.
minethatdata.com/2008/03/minethatdata-e-mail-analytics-and-data.html ,
2008. Accessed via public dataset archive.
1Corresponding author:shekharp@erau.edu 18

Figure 5:Sharp compatibility fiber for a controlled degraded-report example. This diagnostic is not dataset-specific.
It fixes degraded treated and control means eµ1 = 0.12 and eµ0 = 0.08, with retention ambiguity q∈[0.5,1.0] . The
shaded interval is the full set of clean incrementality values compatible with the same released report and ambiguity set. A
business threshold below the interval is certifiable, a threshold at or above the interval is rejectable, and a threshold inside
the interval is unresolved because compatible clean worlds exist on both sides of the decision boundary.
A Additional Empirical Diagnostics
The main paper reports three empirical diagnostics: the certification frontier, the sample-complexity and mini-
max scaling curves, and the reporting-granularity tradeoff. The appendix records the supporting diagnostics
used to validate the remaining theoretical components.
A.1 Compatibility fiber diagnostics
Figure 5 isolates the information-geometric object behind Theorem 5.1 and Lemma B.1. The degraded report
has treated mean 0.12, control mean 0.08, and retention interval [0.5,1.0] . The corresponding sharp clean
incrementality fiber is [−0.04,0.16] . A business threshold inside this interval is intrinsically unresolved from
the released report, while thresholds outside the interval are decidable at the population level. This diagnostic
is deliberately one-dimensional because it makes the core geometry visible.
A.2 Privacy-aware detectable effects
Figure 6 supports Proposition B.2. It evaluates Eq. (12) over effective per-arm cell sizes from 100 to 300,000
and reporting-noise scales σξ ∈ {0,1,3,10}, using σs = 0.5, α= 0.05 , β= 0.2 , and N1s =N 0s =N s.
At Ns = 100 , the privacy-aware MDE is 0.198 without reporting noise and 0.443 when σξ = 10 . At
Ns = 300,000, all curves are near 0.00362. Thus randomized reporting noise is most damaging for small
cells, which is the same regime where aggregation-threshold suppression and segment-level reporting are
operationally most tempting.
A.3 Heterogeneous signal-loss reversal
Figure 7 visualizes the constructive example in Appendix B.5. The construction contains two segments with
equal weights and clean control mean zero. In world u, segment 1 has clean treated mean 1 and retention 0.5,
while segment 2 has clean treated mean 0. In world u′, the segment roles are reversed. Both worlds produce
the same aggregate degraded treated mean 0.25. The appendix diagnostic then applies the same match-loss
1Corresponding author:shekharp@erau.edu 19

Figure 6: Privacy-aware minimum detectable effects. Reporting noise increases the detectable-effect floor
most strongly for small effective cell sizes, while large cells dilute the noise contribution.
Figure 7: Heterogeneous signal loss can reverse segment decisions. Two clean segment-level worlds induce
the same aggregate degraded report, while the lower-bound certification rule certifies different segments.
lower-bound rule used by the main certification implementation. At threshold b= 0.25 , world u gives segment
1 band [0.5,1.0] and segment 2 band [0,0] , so segment 1 certifies and segment 2 rejects. World u′ reverses
these bands and certifies segment 2 instead. This example explains why aggregate privacy-degraded lift should
not be interpreted as segment safety when signal loss may vary across segments.
B Supporting Results and Proofs
Lemma B.1(Fiber projection is the sharp identified set).Fix a segment s, a released reportrs, an ambiguity set
U, and the compatibility fiber Fs(rs;U) in Eq. (3). Suppose Fs(rs;U) is nonempty. The set of incrementality
values that can be induced by clean worlds compatible with the report is
{∆s(ηs) :η s ∈ Fs(rs;U)}.
Its closed convex hull is the interval
[ℓ⋆ s(rs;U), u⋆ s(rs;U)]
1Corresponding author:shekharp@erau.edu 20

defined in Eq. (4). No uniformly valid procedure that observes only rs can replace this interval by a strict
subinterval without excluding a compatible clean world.
Proof. By definition, ηs ∈ Fs(rs;U) if and only if there is at least one signal-loss mechanism u∈ Uunder
which the clean world ηs can generate the released report rs. Therefore the set of clean incrementality values
that cannot be ruled out fromr s is exactly
Ds(rs;U) ={∆ s(ηs) :η s ∈ Fs(rs;U)}.
The smallest closed interval containing this set is
"
inf
ηs∈Fs(rs;U)
∆s(ηs),sup
ηs∈Fs(rs;U)
∆s(ηs)
#
,
which is Eq. (4). This proves that the fiber projection is an outer bound on all compatible clean effects.
It remains to show sharpness. Suppose a procedure observing only rs reports a strict subinterval I of
this projection interval while claiming uniform validity over U. Because I is strict, there is some value
δ∈ Ds(rs;U) outside I, or there is a sequence of compatible values converging to a boundary point outside I.
In the first case, choose η◦ s ∈ Fs(rs;U) with ∆s(η◦ s ) =δ . The report rs is compatible with η◦ s, so excluding δ
violates validity in that clean world. In the boundary case, the same conclusion follows by taking a compatible
value sufficiently close to the excluded boundary. Hence no uniformly valid report-based procedure can
improve on the fiber projection without additional assumptions.
B.1 Proof of Theorem 5.1
Proof.Fix segmentsand arma. The degraded mean satisfies
eµa,s =q a,sµa,s, q a,s ∈[q a,s, qa,s],0≤µ a,s ≤B.
For any feasible retention rateq a,s, the clean mean must be
µa,s =eµa,s/qa,s.
Since qa,s 7→eµa,s/qa,s is decreasing on the positive interval [qa,s, qa,s], the smallest feasible clean mean is
obtained at qa,s = qa,s, and the largest feasible clean mean is obtained at qa,s =q a,s, subject to the outcome
boundB. Thus the arm-specific feasible interval is
Ia,s =
"
eµa,s
qa,s
,min
(
B, eµa,s
qa,s
)#
.
Every point in this interval is attainable, which is the step that proves sharpness rather than only validity of the
outer bound. If µ∈ Ia,s and eµa,s >0 , choose q=eµa,s/µ, which lies in the retention interval by construction.
Then construct a bounded clean outcome with mean µ, for example Y(a) =B with probability µ/B and
Y(a) = 0 otherwise. Let the outcome be reported with probability q, independently conditional on the arm and
segment. The degraded mean is then qµ=eµa,s. If eµa,s = 0, then Ia,s ={0} because retention is bounded
away from zero, and choosing any admissible q with µ= 0 attains the interval. Thus Ia,s is exactly the set of
clean arm means compatible with the degraded arm mean, not merely a conservative superset.
The treatment and control arm means can be chosen independently within I1,s and I0,s. Therefore the
identified set for∆ s =µ 1,s −µ 0,s is the Minkowski difference
I1,s − I0,s =
"
inf
µ1∈I1,s, µ0∈I0,s
(µ1 −µ 0),sup
µ1∈I1,s, µ0∈I0,s
(µ1 −µ 0)
#
,
1Corresponding author:shekharp@erau.edu 21

which is exactly [ℓs(U), us(U)] in Eq. (7). Any δ inside this interval can be written as δ=µ 1 −µ 0 for some
µ1 ∈ I1,s andµ 0 ∈ I0,s, so the interval is sharp.
The first two decision statements follow immediately from this sharpness. If ℓs(U)> bs, every compatible
clean world has ∆s > bs, so positive incrementality is certifiable uniformly over U. If us(U)≤b s, every
compatible clean world has∆ s ≤b s, so non-incrementality relative tob s is rejectable uniformly overU.
It remains to prove the lower-bound statement for the unresolved region. Suppose ℓs(U)≤b s < us(U).
By sharpness, there exists a compatible clean world η− and a mechanism u− ∈ Uwith ∆s(η−)≤b s that
produces the observed degraded arm means. Likewise, because bs < us(U), there exists a compatible clean
world η+ and a mechanism u+ ∈ Uwith ∆s(η+)> bs that produces the same degraded arm means. Let
P− and P+ denote the corresponding released-report distributions. In the deterministic degraded-report case
these distributions are identical point masses at the observed report. With randomized reporting noise, take the
same released noisy report distribution conditional on the same degraded arm means, so P− =P + as well.
Thus the released report contains no information that distinguishes the below-or-at-threshold world from the
above-threshold world.
Now consider any binary rule φ mapping released reports to {certify,not certify} . Let A={r:φ(r) =
certify}. Under P−, certification is a false positive, so the false-certification probability is P−(A). Under P+,
non-certification is a false negative, so the false-noncertification probability isP +(Ac). SinceP + =P −,
P−(A) +P +(Ac) =P −(A) +P −(Ac) = 1.
Therefore
max{P−(A), P+(Ac)} ≥1 2 .
Equivalently, every binary rule has worst-case error at least 1/2. More generally, the same argument with two
nonidentical report distributions gives the lower bound
max{P +(φ̸= certify), P−(φ= certify)} ≥1−TV(P +, P−) 2 ,
because P+(A)−P −(A)≤TV(P +, P−) for every measurable certification set A. Finally, uniform validity
rules out certification for this report because η− is compatible and has ∆s ≤b s. Uniform validity also
rules out rejection because η+ is compatible and has ∆s > bs. The only uniformly valid output is therefore
unresolved.
B.2 Proof of Proposition 5.2
Proof.Fix an armaand segments. Let
eµa,s =E[ eYi |A i =a, i∈s]
be the population degraded arm mean, and let
beµa,s = ¯eY a,s + ξa,s ns
be the released degraded arm mean after randomized reporting noise. Here ¯eY a,s is the empirical degraded
mean before reporting noise, ns ≥n is the number of randomized units in the arm-segment cell, and ξa,s is
the noise added to the released arm total.
The released mean error decomposes as
beµa,s −eµa,s =
 ¯eY a,s −eµa,s  + ξa,s ns .
1Corresponding author:shekharp@erau.edu 22

Since 0≤ eYi ≤B , Hoeffding’s lemma implies that ¯eY a,s −eµa,s is sub-Gaussian with variance proxy
B2/(4ns). The reporting-noise term ξa,s/ns is sub-Gaussian with variance proxy σ2 ξ /n2 s. Because the
randomized reporting noise is independent of the sample draw, their sum is sub-Gaussian with variance proxy
va,s = B2 4ns + σ2 ξ n2s ≤ B2 4n + σ2 ξ n2 .
LetL= log(4|C|/α). The sub-Gaussian tail bound gives
P


beµa,s −eµa,s

 > p 2va,sL  ≤2e −L = α 2|C| .
There are 2|C| arm-segment means, so a union bound implies simultaneous control over both arms and all
segments with probability at least1−α. Moreover,
p
2va,sL≤B
r
L
2n + σξ n √ 2L≡r n,
where the last inequality usesn s ≥nand √x+y≤ √x+ √y. Therefore, on the simultaneous event,

beµa,s −eµa,s

 ≤r n
for every arm and segment.
The clean arm mean is obtained from a degraded mean by division by an admissible retention rate. Because
every admissible retention rate is at least qmin, an arm-level degraded-mean error of size rn changes any
compatible clean arm mean by at most rn/qmin. The treatment effect is a difference of two arm means, so the
finite-sample expansion of the population signal-loss band has radius
Radn = 2rn qmin = 2B qmin
r
log(4|C|/α)
2n + 2σξ qminn p 2 log(4|C|/α).
This proves Eq. (9).
To obtain the displayed sufficient sample size, require each term in Radn to be at most ε/2. The sampling
term is at mostε/2when
n≥ 8B2
q2 minε2 log 4|C| α .
The reporting-noise term is at mostε/2when
n≥ 4σξ
qminε
r
2 log 4|C| α .
Combining these two sufficient inequalities gives Eq. (10) up to universal constants. Finally, [ℓs(U), us(U)]
is the population compatibility band from signal-loss uncertainty. The proof above only adds and removes
finite-sample radius around this band; the identification width itself remains. Thus us(U)−ℓ s(U) persists
even asn→ ∞unless the retention ambiguity set tightens.
B.3 Proof of Theorem 5.3
Proof. We first prove the sampling lower bound when the retention probability q is known. A lower bound for
a restricted subproblem is also a lower bound for the full model, so it is enough to hold the control arm fixed
and vary only the treated arm. Setp 0 = 1/2. The target becomes
∆ =B(p 1 −p 0) =B

p1 − 1 2  .
1Corresponding author:shekharp@erau.edu 23

For treated units, Yi(1)/B∼Bernoulli(p 1) and Ri(1)∼Bernoulli(q) independently. Therefore the normal-
ized degraded observation
eYi(1)
B = Ri(1)Yi(1) B
is Bernoulli with success probability qp1. Signal loss has therefore reduced the effective Bernoulli success
probability by a factorq, which is where the information loss enters.
Choose two treated-arm conversion probabilities
p− 1 = 1 2 , p + 1 = 1 2 +h,
where0< h≤1/4. Both probabilities lie in[1/4,3/4]. The corresponding clean incrementality values are
∆− = 0,∆ + =Bh,
so their separation is Bh. Let P− and P+ denote the laws of the n degraded treated-arm observations under
these two worlds. Then
P− = Bernoulli(q/2)⊗n, P + = Bernoulli

q
 1
2 +h
⊗n
.
We next choose h so these two clean effects are separated, while the degraded experiments remain hard to
distinguish. For Bernoulli probabilitiesrandr+δ, with0< r < r+δ <1,
KL(Bernoulli(r)∥Bernoulli(r+δ))≤ δ2
(r+δ)(1−r−δ) .
Herer=q/2andδ=qh. Becauseh≤1/4,
r+δ=q
 1
2 +h

≥ q 2 ,1−r−δ= 1−q  1 2 +h  ≥ 1 4 ,
where the second inequality uses q≤1 . Hence (r+δ)(1−r−δ)≥q/8 , and the one-observation KL
divergence is at most8qh 2. Tensorization of KL divergence overnindependent observations gives
KL(P− ∥P +)≤8nqh 2.
Choose
h= c0 √qn
with c0 >0 sufficiently small and qn sufficiently large so that h≤1/4 and KL(P− ∥P +)≤1/8 . Pinsker’s
inequality then gives
TV(P−, P+)≤
r
KL(P− ∥P +)
2 ≤ 1 4 .
Let b∆ be any estimator based on the degraded observations. The expectation form of Le Cam’s two-point
argument follows from the identity
Z
min{dP−, dP+}= 1−TV(P −, P+).
For every possible estimator valuet,
|t−∆ −|+|t−∆ +| ≥ |∆+ −∆ −|=Bh.
Integrating this inequality with respect to the common partmin{dP −, dP+}yields
E−| b∆−∆ −|+E +| b∆−∆ +| ≥Bh{1−TV(P−, P+)}.
1Corresponding author:shekharp@erau.edu 24

Therefore
sup
θ∈{−,+}
Eθ| b∆−∆ θ| ≥Bh 2 {1−TV(P −, P+)} ≥3Bh 8 .
Substitutingh=c 0/√qngives
sup
p0,p1∈[1/4,3/4]
Ep0,p1 | b∆−B(p 1 −p 0)| ≥c B√qn
for a universal constantc >0. This proves the stated minimax estimation-rate lower bound.
The sample-size form follows from the same construction. If an estimator had absolute error at most ε with
high constant probability uniformly over the class, then, whenever ε < Bh/2, the intervals [∆− −ε,∆ − +ε]
and [∆+ −ε,∆ + +ε] would be disjoint. Thresholding b∆ at (∆− + ∆+)/2 would then produce a test
that distinguishes P− from P+ with the same high constant success probability. The best possible success
probability for testing two simple hypotheses with equal prior is (1 + TV(P−, P+))/2, which is at most
5/8 under the construction above. Thus constant-probability estimation error ε requires ε≳Bh . Since
h=c 0/√qn, this implies
n≳ B2
qε2 ,
which gives the displayed lower bound up to a universal constant.
We now prove the non-vanishing ambiguity lower bound when the retention probability is not known exactly.
This part is an identification argument rather than a sampling argument, so it remains even with infinite data.
Consider a one-arm subproblem with the control mean fixed at zero. Let the observed degraded treated mean
be
eµ=qB 2 .
This single degraded mean is compatible with two different clean worlds. In the first world, the retention
probability isq=q , so the compatible clean treated mean is
µ+ = eµ q = B 2 .
In the second world, the retention probability isq= q, so the compatible clean treated mean is
µ− = eµ q = B 2 q q .
Both clean means lie in [0, B], both retention probabilities lie in the ambiguity set [q, q], and both worlds
induce exactly the same degraded report because qµ=eµ in both cases. Their clean incrementality values
differ by
µ+ −µ − = B 2  1− q q  .
Any estimator that observes only the degraded report must return the same numerical value in these two worlds.
For any numbert,
max{|t−µ +|,|t−µ −|} ≥µ+ −µ −
2 .
Consequently the worst-case absolute error over these two compatible clean worlds is at least
B
4

1− q q  .
This proves the non-vanishing identification lower bound.
Proposition B.2(Privacy-aware MDE derivation).For a two-arm randomized experiment with assignment-unit
variance proxy σ2 s, effective per-arm cell size Ns, and independent reporting-noise variance σ2 ξ added to each
arm total, the normal-approximation minimum detectable effect is Eq.(12).
1Corresponding author:shekharp@erau.edu 25

B.4 Proof of Proposition B.2
Proof. Let b∆priv s denote the reported treated-control difference in segment s. Under a balanced effective
per-arm sample sizeN s, the randomization variance proxy for a difference in means is
Varrand( b∆s)≈ σ2 s Ns + σ2 s Ns = 2σ2 s Ns .
If the reported treated and control totals include independent mean-zero randomized reporting noises ξ1s and
ξ0s with variance σ2 ξ, then the reported means contain additional noise terms ξ1s/N1s and ξ0s/N0s. Because
these noises are independent and enter the difference with opposite signs, their variance contribution is
σ2 ξ
 1
N 2 1s + 1 N 2 0s

.
Adding the randomization and reporting-noise contributions gives the variance inside Eq. (12). For a normal-
approximation power calculation, a two-sided level-α test rejects when the estimated effect exceeds z1−α/2
standard errors under the null. To have power 1−β against an alternative effect size d, the mean shift d must
exceed this rejection threshold by anotherz 1−β standard errors. Thus, withSEdenoting standard error,
d=

z1−α/2 +z 1−β

SE.
Substituting the privacy-aware standard error gives Eq. (12). The sample-size statement follows because
certification requires the statistically detectable effect to be no larger than the robust population margin
ℓs(U)−b s; solving that inequality over feasible allocations gives the required sample size.
B.5 Heterogeneous signal-loss reversal example
This example shows that aggregate privacy-degraded lift can be compatible with opposite segment-level
certification decisions. Let outcomes be bounded by B= 1 , let the two segments have equal population
weight, and let the clean control mean be zero in both segments. Let the ambiguity set allow segment-specific
treated-arm retention rates in [1/2,1] ; control retention is irrelevant because the clean control means are zero.
Under mechanismu, set the clean treated means to
µ1,1 = 1, µ 1,2 = 0,
and choose treated retention rates
q1,1 = 1/2, q 1,2 = 1.
The degraded treated means are eµ1,1 = 1/2 and eµ1,2 = 0, so the aggregate degraded treated mean is 1/4. The
aggregate degraded control mean is zero.
Under mechanismu ′, reverse the segment roles:
µ′ 1,1 = 0, µ ′ 1,2 = 1,
with treated retention rates
q′ 1,1 = 1, q ′ 1,2 = 1/2.
The degraded treated means are eµ′ 1,1 = 0 and eµ′ 1,2 = 1/2, so the aggregate degraded treated mean is again
1/4, and the aggregate degraded control mean is again zero. Thus the two worlds have the same aggregate
degraded lift.
The segment-level lower-bound decisions are opposite. Under u, the segment 1 degraded treated mean is 1/2,
its control mean is zero, and the largest admissible retention rate is 1, so the segment-level lower bound is at
least 1/2. Segment 2 has degraded treated and control means equal to zero, so both its lower and upper bounds
are zero. Thus for any b∈(0,1/2) , the lower-bound rule certifies segment 1 and rejects segment 2. Under u′,
the same argument certifies segment 2 and rejects segment 1. The aggregate degraded report is unchanged
across the two constructions. The example shows that aggregate certification cannot imply segment-level
certification unlessUrestricts how signal loss can vary across segments.
1Corresponding author:shekharp@erau.edu 26
