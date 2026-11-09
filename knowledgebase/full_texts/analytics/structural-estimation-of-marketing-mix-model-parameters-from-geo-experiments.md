---
title: Structural Estimation of Marketing Mix Model Parameters from Geo-Experiments
url: https://arxiv.org/abs/2608.21128
category: analytics
subcategory: empirical
date: 2026-08
venue: arXiv (Cornell University)
authors:
- Niklas Heusch
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.21128
pages: 12
chars: 54557
fetched_at: '2026-11-08T12:59:40+00:00'
kb_version: 1
---

# Structural Estimation of Marketing Mix Model Parameters from Geo-Experiments

Structural Estimation of Marketing Mix Model
Parameters from Geo-Experiments
Niklas Heusch (niklas.heusch@zalando.de)
Abstract—Marketing Mix Models (MMMs) are widely used for
marketing measurement and budget allocation, but face funda-
mental identification challenges: due to endogenous marketing
spend decisions, MMM estimation on observational time-series
data cannot recover the true causal effects of marketing. On
the other hand, geo-experiments provide causal identification
through randomization, but it is not clear how to use them
eﬀiciently to calibrate marketing mix models. We propose a novel
structural estimation approach that recovers the complete set
of MMM parameters—adstock decay ( 𝛼), saturation ( 𝜆), and
effectiveness (𝛽)—directly from geo-experimental time-series. By
differencing outcomes between treatment and control regions, our
method eliminates observed and unobserved confounding factors
while preserving the temporal variation that identifies each
parameter. We demonstrate on synthetic data that this approach
recovers the true ROAS and the response curve over the range
of spending covered by the experiments, together with credible
estimates of the underlying parameters. Our framework enables
eﬀicient pooling across multiple experiments and provides a
principled foundation for MMM calibration that fully utilizes
the information experiments contain.
Companion materials: Dataset · Illustrated walkthrough
I. INTRODUCTION
Marketing Mix Modeling has become a standard approach
for measuring marketing effectiveness and guiding decisions
on budget allocation. As privacy regulations limit user-level
tracking and third-party cookies disappear, aggregate time-
series approaches like MMM have gained renewed impor-
tance ( Jin et al. 2017 ). Several widely-used software pack-
ages, including Google’s Meridian, Meta’s Robyn, and pymc-
marketing, implement MMM estimation, making these meth-
ods accessible to practitioners across industries.
However, MMM faces a fundamental identification challenge:
marketing budgets are not randomly assigned. Companies
increase advertising during periods of expected high demand,
algorithmic bidding systems chase performance signals, and
strategic decisions coordinate marketing with promotional
calendars. This endogeneity means that standard time-series
estimation cannot distinguish whether sales increased because
of marketing or whether marketing increased because sales
were expected to be high. In other words, MMMs struggle
to estimate the effects of marketing, as - in the presence of
unobserved confounders - they cannot tell causality apart from
correlation.
Geo-experiments provide a solution through randomization.
By randomly assigning geographic regions to treatment and
control conditions, these experiments break the endogenous
relationship between marketing and demand, enabling causal
identification. Many companies routinely run geo-experiments
to measure the effect of their marketing, generating rich time-
series data on outcomes and spending in both experimental
groups.
Still, it has not been clear how to best marry geo-experiments
and MMMs and how to eﬀiciently utilize geo-experiments to
calibrate MMMs. 1 So far, standard practice reduces each ex-
periment to a single number, which is then used to calibrate the
MMM: total incremental revenue divided by total incremental
spend. This point estimate of Return on Advertising Spend
(ROAS) discards the temporal evolution of treatment effects—
precisely the variation needed to understand how marketing
effects persist over time (adstock) and how they diminish with
scale (saturation).
Our contribution: We show how to extract substantially more
information from geo-experimental time-series. Rather than
reducing experiments to point estimates, we directly use them
to estimate the structural parameters that govern marketing
dynamics in MMM specifications. Our approach recovers the
complete functional form — adstock decay rates, saturation
curves, and effectiveness coeﬀicients — from the same time
series of geo-experiments that standard analysis reduces to a
single ROAS number.
The key insight is simple: given the time series of outcomes for
both the treatment and control groups in geo-experiments, all
confounding factors cancel out when taking their difference.
This leaves a clean equation without any confounders that
relates observed outcome differences to observed marketing
spends through exactly the transformations MMM assumes.
This differenced equation can be estimated directly, yielding
causally-identified estimates of all MMM parameters govern-
ing the impact of marketing. Multiple geo-experiments can be
eﬀiciently pooled to improve precision.
The remainder of this paper proceeds as follows. Section 2 dis-
cusses related work and literature. Section 3 develops our key
insight about information in geo-experimental time-series and
presents the structural estimation approach. Section 4 presents
the Bayesian estimation framework. Section 5 demonstrates
the approach on synthetic data. Section 6 discusses integration
with full MMM estimation and limitations.
1This problem exists in particular when multiple geo-experiments are
available for the same marketing channel.
arXiv:2608.21128v2  [stat.AP]  7 Sep 2026

II. RELATED WORK
Our work engages three streams of literature: the identification
challenges in marketing mix modeling, experimental methods
for advertising measurement, and approaches to calibrating
MMMs with experimental data.
Identification in Marketing Mix Models. Modern MMMs
capture advertising dynamics through adstock transformations
for temporal carryover and saturation functions for diminish-
ing returns, typically estimated jointly in a Bayesian frame-
work ( Jin et al. 2017 ). A fundamental challenge, established
by Dew et al. ( 2024), is that saturation effects and time-
varying effectiveness are not separately identifiable from ob-
servational data: models incorporating either effect can ap-
proximate data generated by the other, yet imply different
optimal budget allocations. This identification failure is partic-
ularly acute when spending follows autoregressive patterns—
a common feature of marketing data exacerbated by adstock
transformations themselves. Gordon et al. ( 2019) and Gor-
don et al. ( 2023) demonstrate empirically that observational
methods—including matching, regression adjustment, and syn-
thetic controls—fail to recover causal effects from randomized
experiments even with hundreds of millions of observations
and rich behavioral covariates. The implication is clear: ex-
perimental variation, not merely richer data, is necessary for
reliable identification.
Experimental Measurement Methods. Geo-experiments en-
able randomized treatment at the market level, avoiding the
individual-level tracking challenges that complicate user-based
experiments. Vaver and Koehler ( 2011) introduce the geo-
experiment framework for measuring ad effectiveness through
randomized regional assignment. Brodersen et al. ( 2015) de-
velop Bayesian structural time-series models for counterfactual
prediction, implemented in the CausalImpact package. Chen
and Au ( 2022) introduce the Trimmed Match estimator for
robust inference on incremental return on ad spend from
paired geo-experiments. The synthetic control framework of
Abadie et al. ( 2010) provides foundations for counterfactual
construction when only aggregate data are available. These
methods yield credible estimates of total treatment effects,
but they do not recover the structural parameters—adstock
decay, saturation curvature, and channel effectiveness—that
determine how effects vary with spending levels and over time.
Calibrating MMMs with Experiments. Recognizing that
observational MMMs may produce unreliable estimates, prac-
titioners have developed calibration approaches using experi-
mental results. Zhang et al. ( 2024) reparameterize MMMs with
ROAS as a direct parameter, enabling informative Bayesian pri-
ors derived from experiments. Meta’s Robyn treats calibration
as a third objective in multi-objective optimization, penalizing
deviation from experimental lift estimates ( Runge et al. 2023 ).
The pymc-marketing package adds lift test observations to the
model likelihood, treating them as points on the saturation
curve ( Orduz 2024 ). These approaches share a common limi-
tation: they reduce each experiment to an aggregate statistic—a
point estimate of total lift or ROAS—discarding the temporal
structure of experimental outcomes. The Bayesian prior ap-
proach cannot distinguish experiments conducted at different
spending levels without ad-hoc weighting. The saturation-
curve approach identifies the shape of diminishing returns but
not adstock dynamics, since it does not use how effects evolve
over time. In all cases, information is lost.
III. STRUCTURAL ESTIMATION FROM GEO-EXPERIMENTS
A. Geo-Experiments and Standard Practice
Geo-experiments divide a market into geographic units—
typically Designated Market Areas (DMAs) or metropolitan
regions—and randomly assign these units to a treatment or
control group. During the test period, marketing spend is
modified in the treatment group (often reduced to zero, in
“go-dark” tests) while the control group maintains normal
spending.
A well-designed geo-experiment includes three phases:
• Pre-test period : Establishes that treatment and control
groups follow parallel trends before intervention
• Test period: Marketing differs between groups; outcome
differences reflect causal effects
• Cooldown period: Marketing returns to normal; residual
effects decay over time
Fig. 1. Time-series from a geo-experiment showing treatment and control
group dynamics across test and cooldown periods. (A) Sales for treatment
and control groups. (B) Marketing spend in both groups. (C) Sales difference
(control minus treatment) highlighting the causal impact of advertising, with
the true effect gap (dashed) for reference—available here because the data is
synthetic. Shaded regions indicate the test period where marketing was turned
off in the treatment group.

The raw output of geo-experiments is rich: complete time-
series of outcomes and marketing spend for both groups,
typically at daily granularity. Y et standard practice computes
a single number:
̂ROAS = ∑𝑡∈test(𝑦control𝑡 − 𝑦treatment𝑡 ) ∑𝑡∈test(𝑥control𝑡 − 𝑥treatment𝑡 )
This point estimate answers the question: “What was the
average return on this marketing spend?” But by summing over
the test period and dividing totals, it discards all information
about dynamics—how effects evolve over time and how they
respond to different spending levels.
B. Marketing Dynamics in Theory and in Geo-Test Data
Marketers have long recognized that advertising effects are
neither immediate nor constant. Effects persist: a TV ad seen
this week may influence a purchase next week. And there
are saturation effects : the hundredth impression on the same
audience yields less incremental impact than the first. 2
Marketing Mix Models formalize these dynamics by applying
two transformations to translate marketing spends into incre-
mental sales:
Adstock captures persistence and delayed effects: the impact
of marketing in week 𝑡 is determined not only by the marketing
spend of week 𝑡, but also the marketing spends in previous
weeks. The first transformation is hence to calculate the
adstock - which can be thought of as measuring how present
the ads are in the mind of consumers in week 𝑡 - as a function
of the marketing spends in the current and the 𝐿 − 1 previous
weeks.
𝑥∗𝑡 = ∑𝐿−1 ℓ=0 𝛼ℓ 𝑥𝑡−ℓ
∑𝐿−1 ℓ=0 𝛼ℓ
Here 𝑥𝑡−ℓ is marketing spending ℓ weeks ago, 𝐿 is the lookback
window (e.g., 6 weeks), and 𝛼 ∈ [0, 1) is the decay rate,
indicating how much spending from previous weeks ‘carries
over.’ When 𝛼 = 0 , only current-week spending matters; when
𝛼 = 0.7 , spending from several weeks ago still contributes
substantially.3
Saturation captures diminishing returns to adstock. Combined
with an effectiveness coeﬀicient 𝛽, the saturation function
translates the adstock in week 𝑡 into the impact of marketing
in week 𝑡:
2The notion of diminishing returns is essential to the idea of marketing
mix modeling: if returns were constant across channels, no mix would be
required—one would simply allocate the entire budget to the highest-return
channel.
3In other words, the adstock 𝑥∗𝑡 in a given week 𝑡 is determined by the
marketing spend in week 𝑡 and the 𝐿 − 1 previous weeks. As can be seen in
the equation, each past week’s spending is weighted by 𝛼ℓ, so more recent
spending counts more. The denominator normalizes the weights to sum to one,
ensuring that €1000 of spending produces €1000 of total adstock, distributed
across weeks rather than concentrated in one.
𝐼𝑛𝑐𝑟𝑒𝑚𝑒𝑛𝑡𝑎𝑙𝑆𝑎𝑙𝑒𝑠 𝑡 = 𝛽 ⋅ sat(𝑥∗𝑡 ; 𝜆)
sat(𝑥∗𝑡 ; 𝜆) is generally chosen to be an increasing, concave
function, such as the logistic saturation function, which rises
steeply at low adstock and flattens at high adstock. 4 The
parameter 𝜆 > 0 controls the curvature: higher 𝜆 means
saturation (diminishing returns) set in earlier, at lower levels of
adstock. The coeﬀicient 𝛽 then converts the saturated adstock
into euros of incremental revenue.
Three parameters thus govern how spend on a given marketing
channel translates into incremental sales: 𝛼 (persistence of
spending), 𝜆 (speed of diminishing returns), and 𝛽 (overall
effectiveness).
Fig. 2. The two key transformations in marketing mix models. (A) Adstock
decay weights for different 𝛼 values, showing how past spending contributes
to current-period impact. (B) Saturation curves for different 𝜆 values, showing
diminishing returns to adstock.
What geo-tests reveal. Returning to fig. 1, note that time-
series data from geo-experiments reveals these dynamics di-
rectly.
Adstock from the test and cooldown periods. The adstock
mechanism is visible at both ends of the experiment. When
marketing stops in the treatment group at the start of the go-
dark test period, the outcome gap doesn’t emerge instantly—
it widens gradually as treatment’s adstock depletes while
control’s is maintained. Similarly, when marketing resumes
at the start of the cooldown period, the gap doesn’t close
instantly—it narrows gradually as treatment’s adstock rebuilds.
The rate of these transitions identifies 𝛼. Fast transitions—
where the gap emerges or closes within a week or two—imply
low 𝛼: spending in previous weeks carries over very little, so
adstock depletes and rebuilds quickly. Slow transitions—where
convergence takes many weeks—imply high 𝛼: past spending
continues to influence outcomes for an extended period, so
adstock changes gradually.
Saturation from spending variation. Geo-tests at different
spending levels trace the saturation curve. If doubling spend
doubles the outcome gap, returns are proportional ( 𝜆 is small).
If doubling spend yields less than double the gap, we observe
diminishing returns ( 𝜆 is larger).
4We use the logistic saturation function, sat (𝑥∗𝑡 ; 𝜆) = 1−𝑒−𝜆𝑥∗𝑡 1+𝑒−𝜆𝑥∗𝑡

Standard ROAS analysis discards both signals entirely. Our
approach recovers them.
C. The Differencing Equation
We recover this information by estimating the structural model
directly on geo-test data. The key is recognizing that treatment
and control groups can be viewed as two parallel universes:
identical in every respect except for marketing in the tested
channel.
The parallel universes. Consider a geo-experiment testing
marketing channel 𝐴. If our specification correctly describes
how marketing spends translate into incremental sales, out-
comes in each group follow:
𝑦control𝑡 = 𝜇 𝑡 + 𝛽𝐴 ⋅ sat(𝑥∗,control 𝑡,𝐴 ; 𝜆𝐴) + 𝜀control𝑡
𝑦treatment𝑡 = 𝜇 𝑡 + 𝛽𝐴 ⋅ sat(𝑥∗,treatment 𝑡,𝐴 ; 𝜆𝐴) + 𝜀treatment𝑡
Here 𝜇𝑡 captures everything except marketing spends on chan-
nel 𝐴: baseline demand, contributions from other marketing
channels, effects of pricing and promotions, seasonality, and
any unobserved factors. 5 Crucially, 𝜇𝑡 is identical in both
groups because randomization ensures treatment and control
differ only in channel 𝐴 spending.
The differencing equation. Subtracting treatment from con-
trol eliminates 𝜇𝑡:
𝑦control𝑡 − 𝑦treatment𝑡 = 𝛽 𝐴[sat(𝑥∗,control 𝑡,𝐴 ; 𝜆𝐴)
− sat(𝑥∗,treatment 𝑡,𝐴 ; 𝜆𝐴)] + 𝜈𝑡
where 𝜈𝑡 = 𝜀 control𝑡 − 𝜀treatment𝑡 .
The intercept cancels; other channels cancel (as spends are
identical in both groups); control variables cancel (as values
are identical in both groups); unobserved confounders cancel
(as, balanced by randomization, they are identical in both
groups). What remains is a function of only the channel 𝐴
parameters—𝛼𝐴 (embedded in the adstock 𝑥∗), 𝜆𝐴, and 𝛽𝐴—
and observed spending data.
5The full MMM specification models outcomes as:
𝑦𝑡 = 𝛽 0 +
𝑀
∑
𝑚=1
𝛽𝑚 ⋅ sat(𝑥∗𝑡,𝑚; 𝜆𝑚) + ∑
𝑐
𝛾𝑐𝑧𝑡,𝑐 + ∑
𝑢
𝛿𝑢𝑤𝑡,𝑢 + 𝜀𝑡
where the sum over 𝑚 covers all 𝑀 marketing channels, 𝑧𝑡,𝑐 are observed
controls (seasonality, pricing, etc.), 𝑤𝑡,𝑢 are unobserved factors affecting
demand (competitor actions, macroeconomic sentiment, etc.), and 𝜀𝑡 is
idiosyncratic noise. When we isolate channel 𝐴, we can rewrite this as
𝑦𝑡 = 𝜇 𝑡 + 𝛽𝐴 ⋅ sat(𝑥∗ 𝑡,𝐴; 𝜆𝐴) + 𝜀𝑡, where:
𝜇𝑡 = 𝛽 0 + ∑
𝑚≠𝐴
𝛽𝑚 ⋅ sat(𝑥∗𝑡,𝑚; 𝜆𝑚) + ∑
𝑐
𝛾𝑐𝑧𝑡,𝑐 + ∑
𝑢
𝛿𝑢𝑤𝑡,𝑢
That is, 𝜇𝑡 contains everything except channel 𝐴’s contribution—including the
unobserved factors 𝑤𝑡,𝑢. Because randomization balances these unobserved
factors across treatment and control groups, they cancel when we difference,
even though we never observe them directly. See Appendix A for a formal
treatment of identification.
The key property. The differencing equation contains only
three unknown parameters and only observable quantities: the
outcome difference on the left, spending in both groups on
the right. Everything else—seasonality, other channels, unob-
served demand shocks—has vanished through differencing.
This resolves the identification problem that plagues obser-
vational MMM estimation. To estimate causal effects from
observational data in a standard MMM, we must account for all
factors that influence both marketing spending and outcomes.
For example, if high expected demand causes both higher sales
and higher marketing budgets (because firms advertise more
when they anticipate strong demand), we must observe and
control for “expected demand” perfectly—otherwise, we can-
not distinguish whether sales increased because of marketing
or because demand was high. In econometric terms, any factor
that affects both spending and outcomes but is not controlled
for ends up in the error term, violating the assumption that
errors are independent of spending.
In practice, this assumption is nearly impossible to satisfy.
Marketing budgets respond to expected demand, algorithmic
bidding systems chase performance signals, and strategic deci-
sions depend on factors that researchers cannot fully observe.
The differencing estimator sidesteps this problem entirely:
randomization ensures that all confounders—observed and
unobserved—are balanced across treatment and control groups,
so they cancel through differencing. We achieve causal iden-
tification through experimental design rather than by hoping
our controls capture every relevant factor.
IV . ESTIMATION
The differencing equation provides the foundation for esti-
mation. We observe outcome differences and spending in
both groups; we seek to recover the parameters ( 𝛼, 𝜆, 𝛽)
that govern the channel’s effect. This section describes how
to prepare data for estimation, how to pool observations
across multiple geo-experiments, and our Bayesian estimation
approach.
A. Data Preparation
1) From the Differencing Equation to Observable Data: The
differencing equation makes clear what data we need for each
observation. The left-hand side requires outcomes in both
treatment and control groups at time 𝑡, so we can compute
their difference. The right-hand side requires marketing spend
in both groups—not just at time 𝑡, but also in the preceding
𝐿 − 1 weeks, since these determine the adstock 𝑥∗𝑡 .
For each time period 𝑡, we therefore need:
• 𝑦control𝑡 and 𝑦treatment𝑡 (to compute the outcome difference)
• 𝑥control𝑡 , 𝑥control 𝑡−1 , … , 𝑥control 𝑡−𝐿+1 (to compute control adstock)
• 𝑥treatment𝑡 , 𝑥treatment 𝑡−1 , … , 𝑥treatment 𝑡−𝐿+1 (to compute treatment ad-
stock)

2) Wide Format: We reshape the geo-test data into wide
format, where each row contains all the information needed
for one observation: the outcome difference and the current
plus lagged spending for both groups.
This format has a crucial property: each row is now a self-
contained observation with no temporal dependencies on other
rows. All the lagged spending values needed to compute
adstock are included within the row itself.
3) Pooling Multiple Experiments: The wide format makes
pooling across multiple geo-experiments straightforward: we
simply stack the rows from different tests. Since each row con-
tains all information needed for estimation (including lagged
spends), there are no cross-row dependencies to worry about.
Observations from a geo-test run in January can be combined
with observations from a test run in June—they are simply
additional rows in the dataset, each providing independent
information about the same underlying parameters ( 𝛼, 𝜆, 𝛽).
4) Scaling: The parameters we estimate are not scale-
invariant. A geo-test run on a subset of the country will have
smaller absolute spending and outcomes than the country-
level MMM we ultimately want to calibrate. To ensure our
parameter estimates are comparable, we transform the geo-test
data to match the scale of the MMM:
1. Scale to country level. If the treatment group represents
40% of the country and the control group 60%, we
divide treatment outcomes and spending by 0.4 and
control outcomes and spending by 0.6. This transforms
the data to what we would observe if each group were
the entire country.
2. Apply MMM scaling. In case the MMM applies data
transformations for numerical stability (e.g., dividing
outcomes and/or spends by their maximum value), we
apply the same transformation to the geo-test data. This
ensures parameters estimated from geo-tests are on the
same scale as those of the MMM.
B. Bayesian Model
We estimate the differencing equation using Bayesian inference
with weakly informative priors:
TABLE I
BAYESIAN MODEL PRIORS
Parameter Prior Rationale
𝛼 Beta(1, 3) Limited carryover for digital channels
𝜆 Gamma(3, 1) Positive, mode at 2
𝛽 HalfNormal(2) Positive effectiveness
𝜎 HalfNormal(0.5) Observation noise
These are the default priors of the pymc-marketing package
(v0.19). Deliberately, the observational MMM benchmark of
Section 5 uses the same priors for its media parameters, so the
comparison between the two methods cannot be confounded
by prior choice; Appendix C examines sensitivity to these
choices for both models. The likelihood follows directly from
the differencing equation: the observed outcome difference
equals the predicted difference in saturated adstock effects plus
normally distributed noise.
Implementation details, including the full probabilistic model
in plate notation, are provided in Appendix B.
V . EMPIRICAL DEMONSTRATION
A. Synthetic Data
We demonstrate the approach using synthetic data designed
to capture realistic features of marketing measurement. The
data simulates an online retailer with three marketing channels
(paid search, social media, TV) over 156 weeks, incorporating:
• Realistic seasonality and trends
• Endogenous marketing allocation (budgets respond to
expected demand)
• Algorithmic bidding that chases performance signals
• True saturation and adstock effects with known parame-
ters
The synthetic data generation process is described in detail in
a companion paper ( Heusch 2026 ), whose notebook generates
the exact dataset used here. All data is synthetic: parameter
values, magnitudes, and business mechanisms are fictional,
chosen to lie in the range of published industry benchmarks,
and the complete data-generating process—including the true
value of every parameter—is public. The key advantage is that
we observe the true data-generating process, including ground-
truth values for all parameters.
The true parameters for the paid search (PLA) channel are:
adstock decay 𝛼 = 0.2 (20% weekly carryover); saturation
𝜆 = 0.008 per thousand euros of adstocked spend, implying
half-saturation at roughly EUR 137K of weekly adstocked
spend; effectiveness 𝛽 = 1,100 (thousands of euros per unit
of saturated adstock); and true ROAS of 4.20× . Because
estimation divides each series by its maximum (Section 4),
estimated parameters live on that scale; the scaled truths are
𝜆scaled ≈ 1.71 and 𝛽scaled ≈ 0.18 , and the parameter tables
below report this scale.
B. Simulated Geo-Tests
From the synthetic data, we generate four geo-experiments for
the PLA channel at different time periods and spending levels:
1. Test 1 (weeks 20–23): low spending (mean control-
group PLA spend of EUR 54K per week)
2. Test 2 (weeks 55–58): high spending (EUR 129K)
3. Test 3 (weeks 100–103): moderate spending (EUR 64K)
4. Test 4 (weeks 140–143): low-to-moderate spending
(EUR 57K)
Each test includes 4 weeks pre-test, 4 weeks test (with PLA
spend set to zero in treatment), and 8 weeks cooldown.
Estimation uses all 16 weeks of every test—pre-period, test,
and cooldown—with lagged spends taken from the full spend
history, so the gap-opening and gap-closing transitions enter
the likelihood. The variation in spending levels across tests

aids identification of the saturation parameter: jointly, the four
tests probe adstocked spending from roughly EUR 43K to EUR
194K per week, nearly the full range observed over the three
years. Both experimental groups are simulated directly at coun-
try scale (as if each covered the entire market), which spares
the rescaling step of Section 4 without changing anything else.
fig. 1 shows the time-series for Test 1. During the test period,
treatment group sales fall relative to control, reflecting the
causal effect of PLA advertising. The gap closes almost
immediately in the cooldown weeks—consistent with the low
adstock effect ( 𝛼 = 0.2).
C. Main Results: ROAS Recovery
We now evaluate whether our structural estimation approach
can recover the true ROAS—the ground truth parameter known
only in simulation—from the experimentally observed treat-
ment effects.
TABLE II
ROAS ESTIMATES COMPARISON.
Method ROAS 90% CI In CI?
True ROAS 4.20× — —
MMM (realistic) 10.66× [6.99, 14.42] No
MMM (oracle ctrl.) 8.45× [6.97, 9.82] No
Structural (2 tests) 4.31× [3.87, 4.74] Y es
Structural (4 tests) 4.14× [3.77, 4.51] Y es
Note: “MMM (realistic)” is the observational specification a practitioner would
run: observed promotion dummy, observed promotional price level, and three
annual Fourier harmonics for seasonality—the standard seasonal controls in
Robyn, Meridian, and pymc-marketing. “MMM (oracle ctrl.)” replaces these
with the true confounders from the data-generating process (true promotion
state, true price level, seasonal component, product-quality drift, market
sentiment)—covariates no practitioner possesses, providing an upper bound
on what better controls could achieve. The ‘In CI?’ column indicates whether
the true ROAS (4.20×) falls within the 90% credible interval.
Fig. 3. PLA ROAS estimates with 90% credible intervals. Ground truth
(green), observational MMM with realistic and with oracle controls (pink,
gray), and structural estimation with 2 and 4 geo-tests (blue, orange). Both
MMM specifications overestimate ROAS due to endogenous spend—the
oracle showing that even perfect controls cannot repair it; structural estimation
recovers the true value.
As observational benchmarks, we estimate the MMM of Sec-
tion 3 on the full three years of data in two specifications
that differ only in their information set. MMM (realistic) con-
ditions on what a practitioner actually observes: the observed
promotion dummy, the observed promotional price level, and
three annual Fourier harmonics for seasonality—the standard
seasonal device in Robyn, Meridian, and pymc-marketing.
MMM (oracle controls) conditions instead on the true con-
founders of the data-generating process—the true promotion
state and price level, and the latent seasonal, product-quality,
and market-sentiment components—covariates no practitioner
could possess. The oracle is not a feasible model but a
diagnostic: it bounds what any improvement in controls could
achieve, so any bias that survives it cannot be an omitted-
variables problem.
The realistic MMM produces a severely biased ROAS esti-
mate (10.66× vs. true 4.20×)—overestimating effectiveness
by a factor of roughly 2.5—despite carrying the seasonal
and promotional controls of standard practice. The cause is
endogeneity in the synthetic data: marketing spend correlates
with demand through strategic planning and algorithmic opti-
mization, and the model attributes the correlation to causation.
The oracle specification shows that this cannot be repaired
by better controls. Handed the true confounders themselves,
the model still estimates 8.45×—about double the true return,
with an interval that excludes it. T wo mechanisms survive even
perfect controls: the bidding algorithm responds to realized
weekly performance, including its random component, which
no covariate an analyst could hold constant can absorb; and the
true baseline combines its components multiplicatively while
the controls enter linearly, leaving residual variation that the
endogenous spend tracks. The structural estimation approach
recovers ROAS close to the true value (4.31× with 2 tests,
4.14× with 4 tests), with the true ROAS falling within the
90% credible interval in both cases. Precision improves as
more geo-tests are pooled, but even two experiments provide
accurate point estimates.
D. Parameter Estimates
Beyond ROAS, the structural approach recovers the underlying
MMM parameters:
TABLE III
PARAMETER ESTIMATES COMPARISON
Method 𝛼 (adstock) 𝜆 (saturation) 𝛽 (effectiveness)
True 0.20 1.71 0.18
Structural (2 tests) 0.18 [0.08, 0.29] 2.28 [0.91, 3.48] 0.17 [0.11, 0.32]
Structural (4 tests) 0.19 [0.09, 0.28] 1.94 [0.65, 3.10] 0.20 [0.11, 0.44]
MMM (realistic) 0.50 [0.37, 0.62] 1.27 [0.38, 2.62] 0.86 [0.30, 2.03]
Note: Values in brackets are 90% credible intervals. Parameters are reported
on the estimation scale (Section 4): 𝛼 is scale-free; 𝜆 is multiplied by the
maximum weekly PLA spend (EUR 214K); 𝛽 is divided by the maximum
weekly sales (EUR 6.03M).
The structural estimation recovers all three parameters: the true
values fall inside every 90% credible interval, and the adstock
posterior centres almost exactly on the truth ( 𝛼 = 0.19 against
0.20)—the information lives in the pre-period and transition

Fig. 4. Posterior distributions for 𝛼, 𝜆, and 𝛽 (on the estimation scale). True
values indicated by vertical lines. Structural estimation (blue, orange) produces
posteriors covering the ground truth; the observational MMM (pink) shows
substantial bias, particularly for the adstock and effectiveness parameters.
weeks of each test, which enter the likelihood in full. The
saturation and effectiveness posteriors are individually wider,
for a structural reason: 𝜆 and 𝛽 trade off along a ridge (fig. 6,
right panel; posterior correlation -0.68), because a flatter curve
with a larger coeﬀicient produces nearly the same response as
a steeper curve with a smaller one over the range of spending
the experiments cover. What the data pin down tightly is the
ridge’s joint implication—the response curve over the tested
range, and the ROAS it implies—which is why the ROAS
intervals of Section 5.3 are far narrower than the marginal
parameter intervals. fig. 5 shows this directly: over the tested
range, the posterior response curves lie on top of the truth,
and they fan out only beyond it.
Fig. 5. Response curve identified by the experiments. Posterior draws and
posterior mean (orange) from the 4-test structural estimation against the true
curve (green, dashed). Tick marks show the adstocked spending levels the
experiments probed. Over that range the curve is tightly identified; beyond it,
the draws fan out—an honest statement of what the experiments do and do
not pin down.
In contrast, the realistic MMM produces substantially biased
estimates, particularly for the adstock parameter (0.50 vs. true
0.20) and the effectiveness coeﬀicient (several times the truth).
These parameter biases combine to produce the inflated ROAS
estimate.
VI. DISCUSSION
Our simulation results demonstrate that the structural estima-
tion approach recovers all three parameters governing market-
ing dynamics—adstock decay, saturation, and effectiveness—
from geo-experimental time-series data. This section situates
Fig. 6. Pairwise joint posteriors from the 4-test structural estimation, with
the true parameter values marked (×). The 𝛼 panels are compact: the adstock
rate is identified separately, by the gap-opening and gap-closing transitions.
The 𝜆–𝛽 panel shows the identification ridge: flat-but-large and steep-but-
small parameter combinations imply nearly the same response over the tested
spending range, so the data constrain the pair jointly rather than each alone—
the ridge’s invariant is the response curve of fig. 5, and the ROAS it implies.
our contribution within the broader literature, discusses inte-
gration with full MMM workflows, and acknowledges limita-
tions.
A. Relationship to the Experimental Measurement Literature
Our empirical results corroborate the finding of Gordon et
al. ( 2019) that observational methods fail to recover causal
advertising effects. Section 5.3 demonstrates this directly:
the observational MMM produces a severely biased ROAS
estimate despite carrying the standard seasonal and promo-
tional controls, and the oracle specification—handed the true
confounders themselves—reduces the bias only from 10.66×
to 8.45× against a true 4.20×. When even perfect controls
cannot restore identification, the failure is not a matter of data
quality. As we formalize in Appendix A.2, the conditional
independence assumption required for causal identification—
that error terms be independent of marketing spending con-
ditional on controls—is virtually impossible to satisfy when
budgets respond to anticipated demand, algorithmic systems
chase performance signals, and strategic decisions depend on
unobservable factors.
Our contribution builds on this foundation. We do not merely
accept that experiments are necessary; we demonstrate why
observational MMM fails and then show how to extract
substantially more information from experimental data than
current practice allows. Rather than reducing geo-experiments
to aggregate ROAS estimates, we use the full time-series to
identify all structural parameters governing marketing dynam-
ics. This represents a shift from “experiments for measure-
ment” to “experiments for structural estimation.”
The practical implication is considerable. Many firms already
run geo-experiments but discard most of the information
they generate. Our approach enables these firms to calibrate
complete MMM functional forms—adstock decay, saturation
curvature, and effectiveness—from the same experimental in-
vestments they already make.
B. Comparison to Existing Calibration Methods
Current MMM software packages offer various approaches to
incorporating experimental results, but all share a fundamental

limitation: they reduce geo-experiments to aggregate statistics,
discarding the temporal structure that identifies dynamic pa-
rameters.
Google Meridian (Zhang et al. 2024 ) reparameterizes the
model to include ROAS as a direct parameter, enabling ex-
perimental point estimates to serve as informative priors. This
elegantly incorporates aggregate experimental evidence into
Bayesian estimation, but cannot distinguish between experi-
ments conducted at different spending levels or time horizons
without ad-hoc weighting. The approach identifies the level
of channel effectiveness but not how that effectiveness varies
with spending (saturation) or persists over time (adstock).
Meta Robyn (Runge et al. 2023 ) treats calibration as a third
objective in multi-objective optimization, penalizing deviation
from experimental lift estimates alongside fit and budget
allocation criteria. This provides a mechanism for steering
model selection toward experimentally-consistent regions of
the parameter space. However, without modeling the temporal
structure of experimental outcomes, the method cannot sepa-
rately identify adstock and saturation parameters—it constrains
the aggregate effect without informing its decomposition.
pymc-marketing (Orduz 2024 ) adds adds lift test observations
directly to the model likelihood, treating experimental ROAS
estimates as points on the saturation curve. This principled
Bayesian approach can inform saturation parameters when ex-
periments at different spending levels are available. However,
because it uses aggregate lift rather than time-series outcomes,
it cannot identify adstock dynamics—how long marketing
effects persist after spending stops.
Our structural estimation approach addresses these limitations
directly. By estimating the differencing equation on weekly
time-series data, we use: - The rate of outcome gap emer-
gence (when spending stops in treatment) and closure (when
spending resumes) to identify adstock decay - The relationship
between spending differences and outcome differences to
identify saturation curvature
- The level of outcome differences to identify effectiveness
All three parameters emerge from a single, theoretically-
grounded estimation rather than from separate heuristics or
aggregate constraints.
C. Integration with Full MMM Estimation
This paper focuses on structural estimation as a standalone
approach for a single channel. Several strategies exist for
integrating these estimates into a full Marketing Mix Model
covering multiple channels:
Informative priors. Use the posterior from structural esti-
mation as the prior for the corresponding channel in MMM
estimation. This requires specifying a joint prior that captures
correlations between parameters.
Joint likelihood. Incorporate the geo-test differencing equa-
tion directly into the MMM likelihood, treating both obser-
vational time-series and geo-test observations as arising from
the same underlying parameters. This approach mirrors how
pymc-marketing incorporates lift test observations into their
Bayesian model—but extended to use the full differencing
equation rather than aggregate ROAS estimates. The existing
pymc-marketing codebase provides a natural foundation for
implementing this integration.
T wo-stage estimation. Estimate channel parameters from
structural estimation, compute that channel’s contribution to
outcomes, subtract from total sales, and estimate the remaining
MMM on residualized outcomes. This sequential approach is
computationally simpler but does not propagate uncertainty
from the first stage.
D. Limitations
Several limitations merit discussion, though most are shared
with MMM estimation more broadly rather than specific to
our approach.
Functional form assumptions. Our approach assumes the
MMM specification—specifically, geometric adstock and lo-
gistic saturation—correctly describes the true data-generating
process. This is not a limitation unique to our method; any
MMM estimation requires such assumptions. Indeed, our ap-
proach offers an advantage: because the differencing equation
contains only the parameters of interest after differencing
eliminates confounders, we can compare functional forms (ge-
ometric vs. delayed adstock, logistic vs. Hill saturation) using
standard model selection criteria. This principled approach to
specification testing is not available in observational MMM
estimation, where confounding makes it diﬀicult to distinguish
model misspecification from omitted variable bias.
Geographic spillovers. The method assumes no spillovers
between treatment and control areas. If advertising in control
areas reaches treatment consumers (e.g., as consumers travel
between treatment and control areas), the outcome difference
will understate the true treatment effect. This limitation is
common to all geo-experiments, not specific to our estimation
approach.
Parameter stability. We assume parameters remain constant
across experimental periods. If marketing effectiveness varies
substantially over time—due to creative fatigue, competitive
dynamics, or changing consumer preferences—estimates re-
flect some form of average effect across the experimental
windows. This assumption is standard in MMM more broadly;
methods for accommodating time-varying parameters (see
Dew et al. ( 2024)) remain an area for future extension of our
approach.
Experimental requirements. The method requires geo-
experiments with suﬀicient temporal variation to identify
dynamic parameters. Short experiments (e.g., two-week tests)
may not generate enough adstock variation to precisely identify
decay rates. Similarly, experiments must span different spend-
ing levels to identify saturation curvature. These requirements

may exceed what standard geo-test designs provide, though the
informational gains justify enhanced experimental protocols.
Relatedly, the experiments identify the response curve only
over the range of spending they probe (fig. 5); recommen-
dations far outside that range—for example, a large budget
expansion—lean on the parametric form of the saturation
function rather than on experimental variation, and should be
treated accordingly.
VII. CONCLUSION
We have presented a structural estimation approach for recover-
ing Marketing Mix Model parameters from geo-experimental
time-series. By estimating the differencing equation directly—
rather than reducing experiments to point ROAS estimates—
our method extracts substantially more information from ex-
perimental investments than current practice allows.
The approach contributes along several dimensions:
1. Causal identification of structural parameters. While
the observational MMM produces biased estimates
due to endogenous budget-setting—even under oracle
controls—our method recovers the true ROAS and re-
sponse curve, together with credible estimates of adstock
decay, saturation, and effectiveness, through experimen-
tal randomization.
2. Full utilization of experimental data. Existing cali-
bration approaches reduce geo-experiments to aggregate
statistics, discarding the temporal dynamics that identify
how effects persist and diminish. Our method uses the
full time-series, jointly identifying all three structural
parameters from the same data.
3. Eﬀicient pooling across experiments. Multiple geo-
experiments for a single channel can be naturally com-
bined by stacking observations of the same differencing
equation, with precision improving as more experimental
evidence accumulates.
4. Principled functional form selection. Because con-
founders are eliminated through differencing, alternative
specifications (different adstock and saturation func-
tions) can be compared using standard model selection
criteria—an approach unavailable in observational esti-
mation.
For practitioners, this framework offers a method to extract
greater value from geo-experimental investments. Rather than
obtaining only point estimates of channel ROAS, the same
experimental data can calibrate the complete functional form
needed for optimal budget allocation across spending levels
and time horizons.
The notebooks and other companion materials are available in
the mmm-materials GitHub repository .
REFERENCES
Abadie, Alberto, Alexis Diamond, and Jens Hainmueller. 2010.
“Synthetic Control Methods for Comparative Case Studies:
Estimating the Effect of California’s Tobacco Control
Program.” Journal of the American Statistical Association
105 (490): 493–505.
Brodersen, Kay H., Fabian Gallusser, Jim Koehler, Nicolas
Remy, and Steven L. Scott. 2015. “Inferring Causal Im-
pact Using Bayesian Structural Time-Series Models.” The
Annals of Applied Statistics 9 (1): 247–74. https://doi.org/
10.1214/14-AOAS788.
Chen, Aiyou, and Timothy C. Au. 2022. “Robust Causal
Inference for Incremental Return on Ad Spend with Ran-
domized Paired Geo Experiments.” The Annals of Applied
Statistics 16 (1): 1–20.
Dew, Ryan, Nicolas Padilla, and Anya Shchetkina. 2024. “Y our
MMM Is Broken: Identification of Nonlinear and Time-
Varying Effects in Marketing Mix Models.” Unpublished
manuscript.
Gordon, Brett R., Robert Moakler, and Florian Zettelmeyer.
2023. “Close Enough? A Large-Scale Exploration of Non-
Experimental Approaches to Advertising Measurement.”
Marketing Science 42 (4): 768–93.
Gordon, Brett R., Florian Zettelmeyer, Neha Bhargava, and
Dan Chapsky. 2019. “A Comparison of Approaches to
Advertising Measurement: Evidence from Big Field Exper-
iments at Facebook.” Marketing Science 38 (2): 193–225.
https://doi.org/10.1287/mksc.2018.1135.
Heusch, Niklas. 2026. “A Synthetic Benchmark Dataset with
Endogenous Marketing Spend for Validating Marketing
Mix Models.” arXiv Preprint . https://arxiv.org/abs/2608.2
1130.
Jin, Yuxue, Yueqing Wang, Yunting Sun, David Chan, and
Jim Koehler. 2017. Bayesian Methods for Media Mix
Modeling with Carryover and Shape Effects . Technical
Report. Google Inc.
Orduz, Juan Camilo. 2024. Lift Test Calibration . https://www.
pymc-marketing.io/en/stable/notebooks/mmm/mmm_lift_
test.html.
Runge, Julian, Y oshi Patter, and Igor Skokan. 2023. Robyn:
Semi-Automated Marketing Mix Modeling . https://github.c
om/facebookexperimental/Robyn.
Vaver, Jon, and Jim Koehler. 2011. Measuring Ad Effectiveness
Using Geo Experiments . Google Inc.
Zhang, Yingxiang, Mike Wurm, Eddie Li, et al. 2024. Media
Mix Model Calibration with Bayesian Priors . Technical
Report. Google Research.

APPENDIX A
THE MMM IDENTIFICATION PROBLEM
This appendix provides a formal treatment of the identification
problem in Marketing Mix Models and how the differencing
estimator resolves it.
A. The Full MMM Specification
The standard Marketing Mix Model specifies outcomes as a
function of marketing spending across 𝑀 channels plus control
variables:
𝑦𝑡 = 𝛽 0 +
𝑀
∑
𝑚=1
𝛽𝑚 ⋅ sat(𝑥∗𝑡,𝑚; 𝜆𝑚) +
𝐶
∑
𝑐=1
𝛾𝑐 𝑧𝑡,𝑐 +
𝑈
∑
𝑢=1
𝛿𝑢 𝑤𝑡,𝑢 + 𝜀𝑡
where:
• 𝑦𝑡 is the outcome (e.g. revenue) in period 𝑡
• 𝑥∗𝑡,𝑚 is the adstock-transformed spend for channel 𝑚, with
decay parameter 𝛼𝑚
• sat(⋅; 𝜆𝑚) is the saturation function for channel 𝑚
• 𝑧𝑡,𝑐 are observed control variables (seasonality indicators,
pricing, economic conditions)
• 𝑤𝑡,𝑢 are unobserved factors affecting demand (competitor
actions, macroeconomic sentiment, etc.)
• 𝜀𝑡 is idiosyncratic noise
• Each channel has three parameters: 𝛼𝑚 (adstock decay),
𝜆𝑚 (saturation), 𝛽𝑚 (effectiveness)
B. The Identification Problem
For the MMM to yield causal estimates of marketing effec-
tiveness, the following conditional independence assumption
must hold:
𝜀𝑡 ⟂ 𝑥 𝑡,𝑚 ∣ 𝑧 𝑡 for all 𝑚
That is, the error term must be independent of marketing
spending conditional on the observed controls. This requires
that 𝑧𝑡 captures all factors that simultaneously affect both
marketing decisions and outcomes.
In practice, this assumption is virtually impossible to satisfy:
Strategic timing. Marketing teams plan campaigns around
anticipated demand. A retailer increases TV spending before
Black Friday because sales will be high—not because the
ads will cause the sales. Without controlling for “anticipated
holiday demand,” the model conflates seasonal effects with
advertising effects.
Algorithmic optimization. Automated bidding systems (e.g.,
Google Smart Bidding) increase spending when conversion
rates are high. But high conversion rates may reflect strong
underlying demand rather than marketing effectiveness. The
algorithm’s response to demand signals creates correlation
between 𝑥𝑡 and 𝜀𝑡.
Budget responses. When sales exceed expectations in one
quarter, marketing budgets often increase in the next. This
creates correlation between past outcomes (which include past
𝜀) and current spending decisions.
Unobservable factors. Even with extensive controls, fac-
tors like competitor actions, word-of-mouth momentum, or
macroeconomic sentiment affect both outcomes and marketing
decisions in ways that cannot be fully captured.
The consequence is bias: MMM estimates reflect some un-
known mixture of true causal effects and spurious correlation
from endogenous budget-setting.
C. How Differencing Resolves Identification
The differencing estimator achieves identification through a
fundamentally different mechanism: experimental randomiza-
tion rather than conditional independence.
In a geo-experiment testing channel 𝐴, we can write outcomes
for treatment and control groups as:
𝑦control𝑡 = 𝜇 𝑡 + 𝛽𝐴 ⋅ sat(𝑥∗,control 𝑡,𝐴 ; 𝜆𝐴) + 𝜀control𝑡
𝑦treatment𝑡 = 𝜇 𝑡 + 𝛽𝐴 ⋅ sat(𝑥∗,treatment 𝑡,𝐴 ; 𝜆𝐴) + 𝜀treatment𝑡
where 𝜇𝑡 = 𝛽 0 + ∑ 𝑚≠𝐴 𝛽𝑚 ⋅ sat(𝑥∗𝑡,𝑚; 𝜆𝑚) + ∑ 𝑐 𝛾𝑐𝑧𝑡,𝑐 +
∑𝑢 𝛿𝑢𝑤𝑡,𝑢 contains all common factors.
The crucial observation is that 𝜇𝑡 is identical across treatment
and control by construction: - Random assignment ensures
the groups are statistically equivalent at baseline - Non-tested
channels have identical spending in both groups - Observed
controls (seasonality, pricing) take the same values - Unob-
served factors 𝑤𝑡,𝑢 are balanced by randomization
Taking differences:
𝑦control𝑡 − 𝑦treatment𝑡 = 𝛽 𝐴[sat(𝑥∗,control 𝑡,𝐴 ; 𝜆𝐴)
− sat(𝑥∗,treatment 𝑡,𝐴 ; 𝜆𝐴)] + 𝜈𝑡
The term 𝜇𝑡 vanishes. The remaining error 𝜈𝑡 = 𝜀 control𝑡 −
𝜀treatment𝑡 is the difference in idiosyncratic shocks, which is
uncorrelated with the spending difference by randomization.
No conditional independence required. We do not need
to assume that controls capture all confounders. We do not
need to model how budgets are set. Randomization handles
all confounding—observed and unobserved—automatically.
Complete parameter identification. The differencing equa-
tion identifies all three structural parameters ( 𝛼𝐴, 𝜆𝐴, 𝛽𝐴)
from observable quantities: outcome differences and spending
in both groups.

D. Relationship to Standard Econometric Approaches
The differencing estimator can be viewed through several
econometric lenses:
Difference-in-differences. Like DiD, we compare treatment
and control over time. Unlike standard DiD, we estimate
structural parameters rather than average treatment effects, and
we use the full time-series rather than pre/post comparisons.
Instrumental variables. Randomization provides an instru-
ment (treatment assignment) for spending. However, our ap-
proach estimates the structural form directly rather than using
2SLS.
Potential outcomes. The parallel universes framing connects
to the Rubin causal model. Treatment and control represent
draws from the same potential outcome distribution, differing
only in the realized treatment.
APPENDIX B
IMPLEMENTATION DETAILS
This appendix summarizes the probabilistic model and key
implementation details. Complete Python code implementing
all methods is available in the companion Jupyter notebook.
A. Probabilistic Model in Plate Notation
We estimate the differencing equation using Bayesian inference
in PyMC. The model structure is shown in plate notation
below, generated directly from PyMC’s model_to_graphviz
function:
Reading the plate notation:
The diagram shows the complete data flow for both treatment
and control groups:
1. Observed inputs (rectangular nodes): Marketing spends
for control ( 𝑥ctrl) and treatment ( 𝑥treat) groups, each
containing 𝐿 weeks of data (current + lagged spends).
2. Shared parameters (elliptical nodes at top): The key
structural parameters—𝛼 (adstock decay), 𝜆 (saturation),
and 𝛽 (effectiveness)—are shared between both groups.
This encodes the assumption that the marketing channel
works the same way regardless of experimental group
assignment.
3. Parallel transformations (deterministic nodes): For
each group:
• Adstock: 𝑥∗𝑡 = ∑ 𝐿−1 ℓ=0 𝛼ℓ𝑥𝑡−ℓ/ ∑𝐿−1 ℓ=0 𝛼ℓ
• Saturation: sat (𝑥∗𝑡 ; 𝜆)
• Impact: 𝛽 ⋅ sat(𝑥∗𝑡 ; 𝜆)
4. Differencing (𝜇): The predicted outcome difference
equals impact ctrl − impacttreat.
5. Likelihood (Δ𝑦, shaded): Observed outcome differences
follow 𝒩(𝜇, 𝜎).
The plate (rectangle around observation-level nodes) indicates
that transformations are computed for each of the 𝑇 time
periods. Crucially, the parameters sit outside the plate—they
week (16) x lag (6)
week (16)
sigma
~
Halfnormal
y_obs
~
Normal
lam
~
Gamma
sat_control
~
Deterministic
sat_treatment
~
Deterministic
beta
~
Halfnormal
impact_control
~
Deterministic
impact_treatment
~
Deterministic
alpha
~
Beta
adstock_treatment
~
Deterministic
adstock_control
~
Deterministic
spend_treatment
~
Data
spend_control
~
Data
mu
~
Deterministic
Fig. 7. Structural Estimation Model: Plate Notation
are estimated once and applied identically to both groups
across all observations.
B. Computational Notes
We use PyMC’s No-U-T urn Sampler (NUTS) with 4 chains,
1000 tuning and 2000 sampling iterations each, and target
acceptance rate 0.95 (1000 sampling iterations for the observa-
tional MMM benchmarks). Convergence is assessed via R-hat
< 1.01 and ESS > 400; all runs pass. Estimation completes
in under 30 seconds on a modern laptop. The observational
MMM uses the same media-parameter priors as the structural
model (the priors table of Section 4); its remaining priors
are Normal(0, 0.3) on control coeﬀicients, Normal(0, 0.2) on
Fourier coeﬀicients, Normal(0.5, 0.2) on the intercept, and
HalfNormal(0.1) on the noise scale, with Normal(0, 2) on the
oracle specification’s control coeﬀicients so that priors cannot
be accused of holding perfect covariates back.
APPENDIX C
ADDITIONAL RESULTS
A. Sensitivity to Prior Specification
We examined sensitivity to prior choices by re-running the
structural estimation with alternative priors:

TABLE IV
SENSITIVITY TO PRIOR SPECIFICATION
Prior Set 𝛼 𝜆 ROAS (4 tests)
Baseline Beta(1,3) Gamma(3,1) 4.14 [3.77, 4.51]
Diffuse Beta(1,1) Gamma(1,0.5) 4.07 [3.69, 4.44]
Informative Beta(2,8) Gamma(5,2) 4.14 [3.82, 4.45]
Note: Prior distributions for 𝛼 (adstock) and 𝜆 (saturation). ROAS estimates
with 90% credible intervals.
Results are robust to reasonable prior variations: point es-
timates shift by less than 2%, and all credible intervals
contain the true ROAS. The same holds on the other side
of the comparison: re-estimating the realistic MMM under the
alternative prior set used in the companion blog series (Beta(2,
1) on carryover, Gamma(2, 1) on saturation, Normal(0, 0.5) on
the media coeﬀicients) leaves its bias intact (11.67× vs. 10.66×
under the baseline priors)—the endogeneity bias is likelihood-
driven, not prior-driven.
