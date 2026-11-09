---
title: 'Accuracy Is Not Service: A Decision-Aware Benchmark for Intermittent-Demand Forecasting'
url: https://arxiv.org/abs/2609.13840
category: ai-marketing
subcategory: measurement
date: 2026-09
venue: ''
authors:
- Joo Ern Chin
- Shih-Fen Cheng
- Aldy Gunawan
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13840
pages: 10
chars: 55909
fetched_at: '2026-11-08T13:29:44+00:00'
kb_version: 1
---

# Accuracy Is Not Service: A Decision-Aware Benchmark for Intermittent-Demand Forecasting

Accuracy Is Not Service: A Decision-Aware
Benchmark for Intermittent-Demand Forecasting
Joo Ern Chin 1,2, Shih-Fen Cheng 1, and Aldy Gunawan 1
1School of Computing and Information Systems, Singapore Management University
80 Stamford Road, Singapore 178902
jooern.chin.2025@engd.smu.edu.sg{sfcheng, aldygunawan}@smu.edu.sg
2ST Logistics Pte. Ltd.
5 Clementi Loop, Singapore 129816
Abstract—A contract-logistics spare-parts operator is paid on
order-level service: an order counts only ifeveryrequested
line is fulfilled, yet forecasters are selected based on line-level
forecast accuracy. This disconnect matters when demand is
intermittent and lumpy, histories are short, and lead times
span months. We benchmarked 38 forecasting methods spanning
classical, intermittent-demand, machine-learning, deep-learning,
and pretrained foundation models. A common decision-aware
protocol evaluates them on an industrial panel drawn from a
live contract and two public datasets. Forecast-accuracy rank
and order-service rank arenegativelycorrelated on the industrial
panel, at -0.555, across methods evaluated on 20,330 real multi-
item orders. Service is more closely associated with thedirection
of cumulative forecast bias, including over-prediction during
zero-demand periods, than with point accuracy. Examining bias
in Chronos-2’s instance normalization yields a training-free
correction that lifts the per-material fill proxy from 77.5%
to 92.0% (14.5 percentage points) at the 90% policy target
and raises the complete-order fill rate from 54% to 63%. For
reproducibility, we releaseRUF(Regenerate-Until-Fidelity), a
method for generating fidelity-certified synthetic panels on which
the findings reproduce. For intermittent demand, the lowest-error
forecast need not deliver the highest service. Bias direction helps
explain this gap, which can be reduced without retraining.
Index Terms—intermittent demand, spare parts, forecasting
benchmark, foundation models, decision-aware evaluation, ap-
plied machine learning
I. INTRODUCTION
Keeping fielded equipment operational requires spare parts
that may be ordered only a few times a year, making inventory
planning difficult. A contract-logistics spare-parts operator is
judged on order-level service and penalized for shortfalls; as
an operating threshold, we adopt an illustrative80-of-80target
(80% of customer orders fully filled across 80% of platforms,
the equipment fleets a contract covers). Demand histories
are sparse and replenishment lead times are measured in
months. Service requirements are strict: a multi-item order is
incomplete if any component is short. In this setting, planners
use simpler, auditable rules. Like much of the spare-parts
and maintenance, repair, and operations (MRO) industry, the
operator we study drives replenishment with moving averages
Shih-Fen Cheng would like to acknowledge the funding support from the
Singapore Ministry of Education (MOE) Academic Research Fund (AcRF)
Tier 1 Grant (Project Number: 2026-UI-002).
in a spreadsheet or enterprise resource planning (ERP) system
rather than a learned model.
The operational question is which forecaster should inform
replenishment. Accuracy-based selection assumes that the
most accurate model is also the best choice. This assumption
fails on our industrial panel: moving averages perform well
on accuracy, but their bias direction can reduce service under
the common replenishment policy.
Two gaps limit evidence-based method choice here. First,
broadcross-classcomparison on genuinely intermittent indus-
trial demand is scarce. Intermittent-demand studies typically
compare specialized estimators, and machine-learning studies
compare learners. Recent foundation-model evaluations often
emphasize structurally smoother retail or macroeconomic se-
ries [1], [2]. Second, method choice still defaults to point
accuracy. The conventional pipeline illustrates this assumption:
a forecaster is selected on accuracy (mean absolute scaled
error, MASE; symmetric mean absolute percentage error,
sMAPE), its point forecast sets the order-up-to level through
the textbook base-stock formula, and lower error is presumed
to translate into higher service [3]. Competitions rank methods
on accuracy [1], and intermittent-demand research tunes bias
corrections to accuracy targets [4]. The forecast–inventory
gap is acknowledged [5], but it is rarely measuredacross
model classesagainst an operational target. Accuracy rankings
therefore need validation against service outcomes.
We address these gaps by benchmarking 38 methods under a
common decision-aware protocol and examining how forecast
bias direction contributes to the resulting accuracy–service
inversion. We show that the associated bias can be reduced
within a foundation model without retraining and reproduce
the findings on a fidelity-certified synthetic panel.
Our contributions are as follows:
1)RUF (Regenerate-Until-Fidelity):we release a fidelity-
certified public benchmark (CC-BY-4.0, with full eval-
uation code and open data in a public reproduction
repository1), certified against the confidential data at the
level of fitted marginal distributions and cross-material
copula dependence, on which the leaderboard, inversion
1https://github.com/sfcheng-research/icdm-2026-reproduction
arXiv:2609.13840v1  [cs.LG]  12 Sep 2026

(directionally), and correction reproduce. The procedure
could support certified benchmarks in other domains.
2)A 38-method cross-class benchmarkfordecision-
awareintermittent spare-parts forecasting, spanning
eight model classes, three sparsity regimes (industrial,
RAF, M5), and 31 demand-pattern segments, run under
anaudited, no-fallback protocol(every method regen-
erated from source, failures logged and counted, with
no silent baseline substitution), which we propose for
benchmark releases.
3)A bias-direction diagnostic (BDD): on intermittent
demand the accuracy ranking canreverseagainst the
contractual service target: across then= 38methods,
each scored on 20,330 real multi-item orders, the Spear-
man correlation isρ=−0.555(95% confidence interval
(CI)[−0.78,−0.26]), strengthening toρ=−0.88once
near-duplicate variants are collapsed to one per model
class. We examine forecast bias direction through its
effect on stock targets (Proposition 1), a scalarα-sweep,
and ahurdlemodel that forecasts demandoccurrence
andsizeseparately. Realized service also depends on
replenishment timing and order allocation.
4)A zero-training-cost correctionto Chronos-2’s in-
stance normalization that increases the per-material fill
proxy by 14.5 percentage points on the industrial panel
and 17.1 percentage points on RAF at the 90% policy
target, and raises industrial complete-order fill rate from
54% to 63%, illustrating the diagnostic’s use.
II. RELATEDWORK
Work on intermittent-demand forecasting includes Croston’s
occurrence–size decomposition [6] and its bias corrections
SBA [4] and TSB [7], temporal-aggregation heuristics [8],
and the Syntetos–Boylan demand taxonomy [9]. The M5 com-
petition evaluated feature-based gradient boosting and global
deep models [1], [10], and pretrainedfoundationtime-series
models (Chronos [11], TimesFM [12], and Moirai [13]) report
competitive zero-shot performance. Other studies forecast the
lead-time demanddistributiondirectly by resampling the em-
pirical demand history rather than estimating a point mean
(Willemain’s Markov-chain bootstrap [14] and its empirical
variants [15]). Across these forecasting branches, evaluation
is constrained by data. The public anchors (M4/M5 [1], [16])
and the general time-series benchmarks now used to rank
foundation models (the Monash archive [17] and GIFT-Eval
[18]) are dominated by smooth, regularly sampled series with
little zero-inflated spare-parts demand. Realistic intermittent
panels are also proprietary. This limits independent replication
of decision-facing findings on sparse demand. RUF addresses
this gap (Section III).
Transportation studies also connect demand prediction with
operational data and outcomes. M2–CNN combines spatiotem-
poral demand patterns with microscopic information from
vacant-taxi movements [19], while Agarwal et al. show that
surge-informed demand predictions improve taxi operations
in a driver-guidance analysis [20]. Our focus is how forecast-
TABLE I
MONTHLY DEMAND PROFILES OVER THE FULL CHARACTERIZATION
WINDOWS:INDUSTRIAL(4,558MATERIALS, 81MONTHS), RAF (5,000,
84),ANDM5 (250, 60). ADI:AVERAGE DEMAND INTERVAL; CV 2:
SQUARED COEFFICIENT OF VARIATION.
Dataset Zero frac. ADI CV 2 Interm.+Lumpy %
Industrial panel 0.70 4.04 2.46 89.7
RAF (public) 0.90 8.65 0.63 100.0
M5 (stratified) 0.33 1.81 0.22 56.8
accuracy rankings translate into complete-order service rank-
ings under heavy intermittency.
End-to-end methods train predictors against decision cost
[21] or optimize stock directly from data [22]. Their advantage
is problem-dependent [23]; we retain two stages because
operators need explainable, auditable policies that can be
retuned per platform.
The forecast–inventory interaction, though acknowledged
[2], [5], is seldom measured on one panel across many classes
against an operational target. M5-style studies primarily rank
methods on accuracy [1], and the closest prior work measures
a forecast–inventory link on smooth M5 retail data and finds
it weaklypositive[10]. We evaluate 38 methods across model
classes against a contractualcomplete-orderservice target un-
der heavy intermittency and find that the relationshipreverses.
Classical intermittent-demand work calibrates bias corrections
within the Croston family precisely toremoveover-forecast
bias and improve accuracy [4], [7], [24]. Our finding is that
under a complete-order contract, the same bias can improve
service. Removing it for accuracy can reduce service.
III. METHODOLOGY
A. Panels
The industrial panel contains 4,021 benchmark-eligible ma-
terials (the operator’s term for a stocked part, or stock-keeping
unit (SKU))2 over 81 monthly periods (69 for training, 12 for
testing), with limited covariates, long lead times, and multi-
item orders. In the full characterization panel (Table I), 70%
of monthly cells are zero, the average demand interval (ADI)
is 4.04, and 89.7% of series are intermittent or lumpy. The
panel is drawn from a contract-logistics operator’s live spare-
parts contract; material identifiers and prices are anonymized,
and the panel itself cannot be released under the operator’s
commercial terms. This constraint motivates the public RUF
surrogate of Section III-B. We replicate the benchmark on
the public RAF spare-parts panel (5,000 series, 90% zeros;
benchmarked on a stratified 500-series sample, Section IV-H)
[25] and use a 250-item monthly M5 panel, stratified toward
M5’s sparsest items but still substantially less intermittent than
spare-parts demand, as a low-intermittency anchor (Table I).
This contrast tests how rankings vary by regime.
2Panel slices: 4,021 for accuracy (rolling-origin); 3,828 of these scored for
order service (20,330 orders, 41 platforms); 4,558 for pooled accuracy and
service in the Chronos study, including the 537 materials outside the main
benchmark. RUF is a separate synthetic corpus (5,000 materials).

TABLE II
SYNTHETIC VERSUS REAL DATA:FIDELITY ON MATCHED SAMPLES.
Fidelity check Real Synthetic
Top marginal family (gamma-mix2) share 0.445 0.446
Winner-family mix (TVD, lower=closer) 0.038
Zero fraction (median) 0.750 0.729
Dispersion index (median) 2.06 2.29
Mean upper-tail dependenceλ U 0.107 0.116
Mean lower-tail dependenceλ L 0.029 0.018
Copula-family mix (TVD) 0.068
B. RUF: Regenerate-Until-Fidelity generation
We release a certified, 5,000-materialRUFsurrogate of the
confidential panel (seed 42; datasheet in the release; CC-BY-
4.0; see footnote 1). Its generator has three stages.(1) Tem-
plate sampling:each material draws a real SKU’s aggregate
template: its best-fit distribution family (Poisson, negative-
binomial, zero-inflated, hurdle, compound-Poisson, or gamma-
mixture), that family’s fitted parameters, a target zero fraction
and CV 2, and a platform.(2) Occurrence×size synthesis:de-
mand is modeled as an occurrence process multiplied by a con-
ditional demand size. A platform-level Gaussian factor couples
monthly draws. Well-determined fits use inverse cumulative
distribution functions (CDFs); otherwise Gaussian-threshold
occurrence draws are combined with moment-matched sizes,
including continuous gamma mixtures rounded to positive
counts. Poisson templates use a native count branch. Occur-
rence probabilities and demand sizes vary with the template’s
first-/second-half demand ratio; a per-SKU empirical per-
centile bounds the tail. This mechanism models co-occurrence
and non-stationarity rather than imposing log-normal renewal
intervals. Multi-item orders and right-skewed moving-average-
price (MAP) unit costs are synthesized, and∼20% of materials
are designated as cold-start items.(3) Regenerate-until-fidelity:
each material isredrawn until its realized Syntetos–Boylan
class and zero fraction match its real template(up to ten
draws, retaining the best match and scoring CV 2; 84% of
non-cold-start materials pass, and the release includes the
per-material audit), adding a sample-level fidelity check to
aggregate comparisons.
We assess fidelity beyond summary moments at two levels
(Table II; matched 800-SKU and∼2,900-pair stratified sam-
ples, fitted using the same code path on a shared 60-month
window).Marginals:the distribution of best-fitting families
across materials is similar (total-variation distance (TVD)
0.038, the same most common family (a gamma mixture)
on both panels; zero fraction (median) 0.750 vs. 0.729, dis-
persion index 2.06 vs. 2.29).Dependence:a bivariate-copula
screen matches upper-tail dependence within 0.01 (λ U 0.107
vs. 0.116) and copula-family mix (TVD 0.068); both panels
exhibit weak tail dependence. The panel approximates the real
data’s marginal-family distributionandcross-material depen-
dence. The leaderboard, inversion direction, and correction
reproduce on it (Section IV-G).
C. Demand segmentation
The segmented benchmark contains intermittent/lumpy ma-
terials; smooth/erratic materials in Table I’s broader character-
ization panel are excluded. The Syntetos–Boylan class (inter-
mittent or lumpy) is crossed with structural traits, including
level shifts, autocorrelation, trend (up or down), seasonality,
ultra-sparsity, and high dispersion. The31 demand-pattern
segmentswith≥10materials cover 3,914 of the 4,021
eligible materials; 107 in smaller groups are omitted from this
segment analysis. Boundaries are ADI1.32, CV 2 0.49, and
sparsity tiers at zero-fraction0.30and0.80. These segments
define the blocks for the Friedman test and identify where each
model class performs well (Section IV).
The 38-method roster.The benchmark spans38 meth-
ods across eight model classes: 7 classical (Naive, Sea-
sonalNaive, SES, Holt, ETS, ARIMA, Prophet [26]), 5 in-
termittent specialists (Croston, SBA, TSB, ADIDA, Boot-
strap), 3 simple averages (MA, WMA, EMA), 9 feature-based
machine-learning (ML) methods (LightGBM [27], LightGBM-
Ensemble, LightGBM-Quantile, XGBoost [28], RF, Gradient-
Boosting, GlobalMLP, SVR, ElasticNet), 7 deep sequence
models (DeepAR [29], DeepAR-Tweedie, N-BEATS [30],
TFT [31], Transformer, RNN, TwoStageML), 2 state-space
models (TBATS, BATS) [32], 1 hybrid (HybridHierarchical),
and 4 pretrained foundation models (Chronos-Bolt tiny/small,
TimesFM, Moirai). For this cross-class comparison, we dis-
tinguish two Chronos model families: the benchmark uses
Chronos-Bolt[11], [33], the distilled fast-inference model,
while the adaptation of Section IV-D usesChronos-2[34],
whose instance normalization is exposed for the modification
evaluated there.
Protocol, metrics, and audit.Using forecast origins [35],
each methodmturns history into a demand-rate forecastˆr i,o,m
for materiali; we evaluate the demand it predicts over a full
replenishment lead time, ˆY (H) i,o =Hˆri,o,m, against observed
demand (Eq. 1), to match the replenishment horizon.
Y (H) i,o =
HX
h=1
yi,o+h, ˆY (H) i,o =Hˆri,o,m.(1)
Table III and the industrial order-book accuracy ranks use a
single six-month lead-time window: origin 69 for industrial
and 78 for RAF. The reference predictsH¯y (3) i,o , where¯y(3) i,o is
the last three training observations’ mean; the method named
Naive instead repeats the last observation. Sete i =|Y (H) i,o −
ˆY (H) i,o,m|andd i =|Y (H) i,o −H¯y(3) i,o |. The benchmark convention
is
MASEm = 1 |Mm| X i∈Mm
(
ei/di, d i >0,
ei, d i = 0, (2)
whereM m contains valid material forecasts. This legacy score
uses unscaled absolute error when the reference is exact;
it is not conventional in-sample-scaled MASE, nor does a
value below 1 universally imply superiority to the reference.
Lower is better. Rolling-origin adaptation instead uses the
pooled ratio P i,o ei,o/ P i,o di,o, with an undefined score if

the pooled denominator is zero. We identify the aggregation
for each comparison. Rankings are stable across naive scales
(Section IV-H). We propose anaudited, no-fallback protocol
for benchmark releases. Every method’s result stream is re-
generated from source. Any failure (non-convergence, missing
forecast) islogged and counted, never silently replaced by
a baseline. Such substitution would overstate a method’s
coverage. We cite only audited streams.
Non-seasonality.A four-detector seasonality audit (classical
and locally smoothed seasonal-trend decomposition, Fourier
power-ratio, and lag-12 autocorrelation, all purpose-built for
a period-12 signal) flags at most 5.3% of the industrial panel
and 2.4% of RAF as seasonal. These low rates suggest that
seasonal misspecification is unlikely to be the main driver
of simple rate estimators’ competitiveness or the accuracy–
service comparison.
D. From forecasts to service
To translate forecasts into service outcomes, we evaluate
every method under onecommonorder-up-to policy (at each
review, replenishment is ordered toward a target levelS), so
any service difference is attributable to the forecast, not to per-
method tuning. The base-stock level uses the standard normal-
approximation form (Eq. 3), with protection periodL+R
(lead time plus review interval) and a single safety factorz=
Φ−1(τ)shared across all methods at policy targetτ:
Si,m = ˆµi,m (L+R) +zˆσ i,m
√
L+R.(3)
HereL= 6months andR= 1month unless varied;ˆµis
the mean rate of the extracted point forecasts andˆσis the
forecaster-supplied dispersion estimate, whose estimation is
method-specific. Targets are clipped at zero. Each replay starts
withSon hand and an empty replenishment pipeline. Receipts
precede demand; orders placed after demand arriveLmonths
later. Service is the complete-order fill rate (COFR): replaying
the operator’s actual multi-item orders, an order succeeds only
ifeveryrequested line is available within the window [36],
COFRm = 1 |Q| X q∈Q 1 n min j∈Iq Fqj,m = 1 o ,(4)
whereF qj,m = 1if and only if linejof orderqis filled on
time. Orders are processed in a fixed common sequence. An
order that cannot be filled in full counts as a failure, consumes
no stock, and is not backordered; successful orders consume
every requested line. After each monthly review, the replay
ordersmax(0, S−inventory position)for each material. Our
representative80-of-80target aggregates this to the platform
level (at least 80% of orders complete for at least 80% of
platforms); it tracks the order-level metric (Section IV-C,
Table IV).Optimizingthe per-platform axis (reserved allo-
cation, per-platform safety factors) is a separate inventory-
control problem. Because a single short line makes an order
incomplete, the implicit-safety-stock effect of Section IV-A
can affect complete-order service.
TABLE III
PER-MATERIAL LEAD-TIMEMASE (EQ. 2)AND RANK:INDUSTRIAL
ORDER-BOOK PANEL(3,828MATERIALS)ANDRAF (500).†:NORAF
RANK(NO-FALLBACK SUBSET).
Industrial RAF
Method Rank MASE Rank MASE
WMA 1 0.803 7 2.011
Chronos-Bolt-tiny 2 0.890 4 1.095
Chronos-Bolt-small 3 0.895 3 1.057
Holt 4 0.922 10 2.931
MA 5 0.971 12 3.155
SES 6 0.995 8 2.905
TimesFM 8 1.044 2 1.048
LightGBM-Quantile 9 1.060 1 0.943
SVR 10 1.118 5 1.143
Naive 11 1.147 6 1.169
DeepAR† 12 1.316 – 1.615
TSB 15 1.512 15 4.102
TBATS 18 1.702 18 4.662
XGBoost 23 2.154 20 5.090
Moirai 34 3.321 32 14.178
Croston 35 3.382 31 8.062
HybridHierarchical 36 3.519 29 7.681
ADIDA 37 3.548 28 7.380
IV. EXPERIMENTS
Table III summarizes industrial and RAF accuracy (18 of
38 methods shown across all eight classes; full roster in the
release). Four findings emerge.
First, classical intermittent-demand methods do not lead
the industrial accuracy ranking. On the order-book panel a
weighted moving average (WMA, MASE 0.803) ranks first,
with the two Chronos-Bolt foundation models just behind
(0.890, 0.895) and the intermittent specialists at the bottom.
A sparsity analysis helps explain this result: native-frequency
smoothing beats temporal aggregation in 70–88% of materials,
and the best moving-average window shrinks as sparsity rises
(MA(4) at 0–20% zeros, MA(1) above 80%). (Under a pooled
MASE on the full benchmark the pretrained models lead
instead, with TimesFM at 0.831; the ordering is aggregation-
dependent, so we anchor the service analysis to the order
book.)
Second, RAF preserves the cross-class picture: the Chronos-
Bolt foundation models, TimesFM, and a quantile gradient-
boosting model lead, while Moirai has much higher error (per-
material MASE 14.2). Foundation-model status alone does
not imply low error on either panel. Six out of seven deep-
sequence methods receive no RAF rank: five are scored on
no-fallback subsets, and the audit excludes DeepAR-Tweedie’s
unstable run; TwoStageML ranks.
Third, accuracy and forecastbias directioncome apart:
the low-MASE leaders have neutral-to-negative cumulative
bias, whereas the intermittent specialists over-predict demand
during zero-demand periods. This asymmetry helps explain the
service outcomes (Section IV-A).
Fourth, aggregate ranks do not establish dominance across
demand patterns. The Friedman test ranks methodswithin
each of the 31 demand-pattern segments (Section III-C) and

averages those ranks to compare methodsacrossdemand
types rather than by aggregate error. The Friedman test rejects
equality (χ 2 = 239.68,p <10 −30, 31 segments), but the
Nemenyi critical difference is wide (CD = 10.90), wider than
the entire 9.1-rank spread of the top-20 Friedman mean ranks
(11.0to20.1, Fig. 1): a single connecting bar would join all of
these leading methods. The segment-blocked TimesFM–WMA
comparison is also inconclusive (unadjustedt-testp= 0.110);
this does not establish equivalence. The Nemenyi comparison
does not separate the leading methods from a broad field in-
cluding moving averages and the Croston family. WMA leads
on order-book MASE (Table III) but does not consistently
lead across demand types. Service offers a further deployment
criterion.
The same picture holds segment by segment (Fig. 2):
ranking all 38 methodswithineach of the 31 demand-pattern
segments, no class is best everywhere. Simple averages, the
foundation models, and the lone hybrid method lead the most
segments (classes with one or two methods have high-variance
means); intermittent specialists win specific level-shift patterns
and rank poorly on others; every class performs poorly in some
segments. Deployment therefore requires method choice by
demand pattern, beyond aggregate ranks.
A. The bias-direction diagnostic (BDD): when accuracy and
service rankings diverge
We test whether forecast rankings translate into complete-
order service rankings. Replaying the operator’s real multi-
item orders across 41 platforms under the common policy
of Eq. 3, we correlate each method’s MASE rank with its
complete-order fill-rate rank (COFR, Eq. 4). Across the full
order book (20,330 orders, 3,828 forecastable materials) the
correlation at the 80% policy target isnegative:ρ=−0.555
(p= 3×10 −4,n= 38; 95% bootstrap CI[−0.78,−0.26]),
and it stays negative at every service target from 0.70 to 0.95
(ρfrom−0.61to−0.48). Across methods, greater accuracy is
associated with lower contractual service. Using the complete
order book rules out stratified subsampling as the source of
this effect. The 38 methods include near-duplicate variants
(three moving averages, two Chronos sizes, several boosting
variants). Collapsing each of the eight model classes to a single
representative provides a sensitivity check, and the inversion
strengthens(ρ=−0.88,n= 8,p= 0.004;ρ=−0.81
on class means). The association persists under equal class
weights.
Why accuracy inverts.Forecast means affect service through
the inventory targets, subject to the replay’s allocation and
replenishment rules.
Proposition 1(Forecast mean and the stock target).FixL+
R >0,z, and identical dispersion estimates for two forecasts.
Ifˆµi,a ≥ˆµi,b for every materiali, thenS i,a ≥S i,b in Eq. 3.
Before clipping, each target difference equals(L+R)(ˆµ i,a −
ˆµi,b).
Proof.Subtract the two target equations. Their safety terms
cancel; multiplication byL+R >0and clipping at zero
preserve the componentwise ordering.
This is a target ordering, not a pathwise service guarantee.
In the complete-order replay, rejecting an unfillable order
preserves stock for later orders; a larger target can instead
serve that order and deplete stock. Partial fulfillment also does
not ensure pathwise monotonicity when higher targets change
replenishment timing. The service association is empirical,
and a larger panel-average mean alone does not imply the
componentwise premise of Proposition 1.
We distinguish signed lead-time bias, the mean of ˆY (H) i,o,m −
Y (H) i,o over valid material–origin pairs, from 12-month drift,
the material-average sum P12 t=1(ˆyi,t,m −y i,t). The separate
absolute-error decomposition is
MAEm = 1 N X
t:y t=0
|ˆyt|
| {z }
zero-period
+ 1 N X
t:y t>0
|yt −ˆyt|
| {z }
non-zero-period
.(5)
HereNcounts evaluated material–month pairs; the zero-
period error share divides the first term by total MAE. In
the industrial diagnostic, 53–54% of Croston/SBA error is
the zero-period term (over-prediction when nothing was de-
manded) versus≈26% for Naive: positive errors on zero-
demand months can offset under-prediction of demand spikes.
The 12-month drift diagnostic on a separate 500-material
industrial sample makes the directional split visible. Methods
with positive cumulative drift include Croston (+8.9, 86% of
materials over-forecast), ADIDA (+8.5), Moirai (+8.8), SBA
(+7.3), LightGBM (+5.3), TSB (+4.5). The accuracy-leading
foundation models drift the other way (TimesFM−8.3, only
51% over-forecast; Chronos-Bolt-tiny−7.1), and deliver lower
service under the same policy. Accuracy and service thus favor
different bias directions here.
The public RAF and M5 panels carry no multi-item order
log, so to compare the three regimes we use the per-material
fill proxy: the fraction of positive-demand periods fully served,
averaged equally over evaluated material windows. A no-
demand window scores 1. Partial demand is consumed and
shortages are lost; replenishment toSis triggered when
inventory position is at mosts= max(0, S−ˆµR). This proxy
is available on all panels (Fig. 3). The same inversion appears
on the industrial panel (ρ=−0.582, 38 methods), weakens on
RAF (−0.173, 38 methods; this replay includes the intermit-
tent specialist iMAPA in place of Prophet), and turns positive
on M5 (+0.359, 38 methods). The industrial per-material
value is comparable in magnitude to the contractual order-level
inversion (ρ=−0.555, above), while the cross-panel pattern
provides evidence of regime dependence (Section IV-B). The
RAF correlation uses pooled rolling-origin accuracy from its
separate service-replay stream, not the per-material accuracy
column of Table III; method records are paired, but available
material coverage differs for some methods.
Robustness to policy form.We first test whether the inver-
sion depends on the Gaussian-zorder-up-to policy (Eq. 3).
Rerunning the full 38-method diagnostic on the per-material
fill proxy under adistribution-awarepolicy (ordering to the

11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33
Friedman segment-mean rank (lower = better)
CD = 10.90  (Nemenyi, =0.05)
top-20 spread = 9.1 ranks  <   CD
SES
TimesFM
MA
WMA CB-small
CB-tiny
BATS
Transformer
DeepART weedie
N-BEATS
GlobalMLP
All 38 methods on one rank line: the leading field spans less than one critical difference
Friedman 2 = 239.7 (31 segments), best is SES at 11.0; a CD-wide band from it covers the top 28 methods
Fig. 1. All 38 methods on the Friedman segment-mean-rank axis. A critical-difference-wide band anchored at the best methodon this axis(SES, which need
not match the order-book MASE leader WMA, as the two use different aggregations) covers the top 28. Lower-ranked methods fall outside the band.
Int
+AC
Int
+LS
Int
+LS
+AC
Int
+LS
+AC
+Se
Int
+LS
+AC
+US
Int
+LS
+Se
Int
+LS
+US
Int
+TD
Int
+TD
+AC
Int
+TD
+LS
Int
+TD
+LS
+AC
Int
+TD
+LS
+AC
+US
Int
+TD
+LS
+US
Int
+TU
+LS
Int
+TU
+LS
+AC
Int
+TU
+LS
+AC
+US
Int
+TU
+LS
+US
Int_baseLum
+LS
Lum
+LS
+AC
Lum
+LS
+AC
+HD
Lum
+LS
+HD
Lum
+LS
+US
Lum
+LS
+US
+HD
Lum
+TD
+LS
Lum
+TD
+LS
+AC
Lum
+TD
+LS
+AC
+HD
Lum
+TU
+LS
Lum
+TU
+LS
+AC
Lum
+TU
+LS
+AC
+HD
Lum
+TU
+LS
+HD
31 demand-pattern segments (Int/Lum × LS level-shift, AC autocorr., US ultra-sparse, HD high-disp., TD/TU trend, Se seasonal)
Simple avg.
Foundation
Intermittent
Hybrid
Feature ML
Classical
State-space
Deep seq.
27 22 20 23 8 22 31 9 5 8 2 7 10 9 6 11 21 30 26 10 12 15 10 17 6 2 3 17 5 3 15
18 15 16 8 5 22 14 15 17 7 11 9 9 28 26 22 21 22 12 3 2 4 5 8 6 17 14 20 24 22 32
15 4 10 10 20 13 14 14 19 25 36 34 34 12 27 15 13 13 6 9 23 12 19 9 33 35 32 7 14 18 15
33 14 35 2 26 10 32 18 11 21 8 31 34 4 29 6 1 35 23 18 30 13 17 21 21 24 32 1 1 9 2
14 22 19 19 24 22 17 26 21 27 22 16 19 19 18 17 15 14 18 27 20 22 22 19 23 19 17 19 20 21 16
26 24 27 24 21 19 22 17 22 15 17 18 16 19 14 22 21 23 26 21 21 24 23 25 16 14 19 26 21 18 18
26 20 26 22 14 25 6 27 30 14 30 22 16 25 18 34 28 20 24 23 8 30 20 30 22 28 19 30 32 26 27
17 25 18 29 26 19 24 23 21 24 19 25 22 27 23 24 26 20 24 28 30 26 25 26 22 21 22 23 24 25 24
No family wins everywhere: best method family shifts across demand patterns
5
10
15
20
25
30
35
Fig. 2. Mean within-segment MASE rank (1 = best of 38) per model class across the 31 demand-pattern segments. Bright (yellow) indicates a low mean
rank within a segment.
empiricalτ-quantile of each method’s lead-time-demand dis-
tribution)strengthensthe inversion at every service level. In
a matched comparison at the 80% target the per-materialρ
moves from−0.59(Gaussian) to−0.70(distribution-aware,
allp <10 −4), and the contractual order-level inversion
(ρ=−0.555) is of the same sign and magnitude. Lower
MASE is associated with worse service under both tested
policy forms, suggesting that the inversion extends beyond the
Gaussian approximation.
Scope: the common-policy regime.A further concern is that
the over-forecasters merely run at a higher effective service
level, and that giving each method its own safety factor would
erase the inversion. We tested this on the full order book by
re-deriving each method’s order-up-to level under its owncost-
optimalz, and under the more permissivezthatmaximizesits
own service. The inversion attenuates:ρmoves from−0.555
at commonzto−0.278under each method’s cost-optimalz
(no longer significant at the 5% level,p= 0.09), and with
a service-maximizingzfor each method it remains−0.384
(p= 0.02). Within the tested range ofz, methods with
negatively biased forecasts attain lower complete-order fill
rates (TimesFM and WMA reach only COFR0.57–0.63at
the largest safety factor, while the over-forecasters reach0.97–
0.98). Per-method retuning requires order-level simulation,
whereas the initial BDD screen uses forecast diagnostics. The
inversion is clearest under the common-zpolicy; cost-optimal
tuning attenuates it below statistical significance.
B. Why the inversion is regime-specific
The same diagnostic helps explain the cross-dataset pattern.
On RAF the bias populations roughly balance: foundation
models negative (−7.7to−7.2), Croston-family positive (+2

0 5 10 15 20 25 30 35
MASE rank (lower = more accurate)
0
5
10
15
20
25
30
35Per-material service rank (lower = better service)
(a) Industrial panel
ρ = −0.582, p = 0.0001, n = 38
0 5 10 15 20 25 30 35
MASE rank (lower = more accurate)
0
5
10
15
20
25
30
35
(b) RAF spare parts
ρ = −0.173, p = 0.30, n = 38
0 5 10 15 20 25 30 35
MASE rank (lower = more accurate)
0
5
10
15
20
25
30
35
(c) M5 monthly
ρ = +0.359, p = 0.027, n = 38
Classical
Intermittent
Simple avg.
Feature ML
Deep seq.
State-space
Hybrid
Foundation
Fig. 3. MASE rank vs. per-material service rank at the 80% target: (a) industrial (ρ=−0.582), (b) RAF (ρ=−0.173), (c) M5 (ρ= +0.359).
to+8), and the rank correlation weakens to−0.173. On M5,
zeros are rare in the evaluation window (≈5% of monthly
cells in the final 12 months, versus 33% over all 60 months
in Table I), so the zero-period error term appears insufficient
to overturn the accuracy ordering. The accuracy–service rela-
tionship is positive (+0.359). The inversion is consistent with
an interaction between heavy intermittency and directional
cumulative forecast bias. Matched-subset checks suggest that
sparsity alone is insufficient (Section IV-H).
C. Service efficiency and the 80-of-80 target
Within a single method, scaling the forecast trades inventory
for service (Section IV-E). Table IV shows the same trade
acrossmethods, against a representative80-of-80target: the
share of the 41 platforms reaching COFR≥0.80when the
20,330 real multi-item orders are replayed, met if≥80%of
platforms do. Three findings emerge. (i) The lowest-MASE
methods miss the target: the leading foundation models hold
theleastinventory (0.37–0.54×Naive) and rarely meet the
platform threshold (≤2%of platforms), and the order-book
leader WMA clears only 12%. (ii) Only the over-forecasting
methods clear it (Croston, SBA, ADIDA, HybridHierarchical,
TwoStageML, ETS;80–93%of platforms; Table IV shows
four of the six), at1.2–1.5×Naive’s inventory: directional
bias improves service at a measurable inventory cost. (iii) The
target reproduces the inversion: the most accurate methods
miss it most severely. The platform roll-upcorroboratesthe
order-level reading rather than adding a criterion: the same six
methods clear both (Spearman 0.93 between the COFR and
%-platform columns), indicating strong agreement between the
rankings. Wereport, not optimize, this target (Section III-D).
Operationalizing the BDD.The BDD (Fig. 4) screens fore-
casts before simulation: flag low-MASE methods with negative
cumulative drift as stockout risks and assess the inventory cost
of positive drift. Final COFR validation is required before
deployment.
TABLE IV
SERVICE–INVENTORY FRONTIER AGAINST THE80-OF-80TARGET
(INDUSTRIAL):ORDER-LEVELCOFR (EQ. 4),PER-MATERIAL INVENTORY
RELATIVE TONAIVE,AND THE SHARE OF PLATFORMS ATCOFR≥0.80.
Method COFR Inv. (×Naive) % plat.≥0.8080-of-80
TimesFM 0.544 0.37 2%×
Chronos-Bolt-small 0.567 0.54 2%×
WMA 0.558 0.96 12%×
Naive 0.627 1.00 15%×
Moirai 0.719 1.38 54%×
LightGBM 0.771 1.16 51%×
TSB 0.793 1.22 56%×
SBA 0.847 1.36 80%✓
Croston 0.858 1.42 88%✓
ADIDA 0.906 1.49 93%✓
HybridHierarchical 0.903 1.47 90%✓
Bias-Direction Diagnostic (BDD): deployment check
Input:candidate forecasts; recent demand history.
1) Compute MASE and meansignedlead-time bias.
2) Compute the zero-period over-prediction share and the sign of
cumulative drift.
3) Flag: low MASE+negativedrift⇒stockout risk;positive
drift⇒implicit safety stock; low MASE+near-zero drift⇒
deployment candidate.
4) If negatively biased, correct the forecastmean(non-zero re-
centering, or scale toward bias-neutralα ⋆), with subsequent
service and inventory validation.
5) Validate on COFR at the contractual target before deployment.
Fig. 4. A reusable forecast-side deployment check.
D. Correcting the bias inside the model
The bias-direction mechanism motivates a correctionwithin
the model. Across a 31-configuration fine-tuning sweep (low-
rank adaptation (LoRA) ranks 4/8/16, data filtering, longer
schedules), no configuration outperforms zero-shot Chronos-
2. Material-level 5-fold cross-validation gives the same result.
With about 70% of observations equal to zero, fine-tuning
may favor near-zero predictions and reinforce the bias. These
results motivate examining normalization as a possible source
of bias.

Following the diagnostic in Section IV-A, we examine how
Chronos-2 normalizes each input series:
ˆxt = xt −¯x s ,¯x= mean(x), s= std(x),(6)
Across 4,558 materials over the full 81-month descriptive win-
dow, the median overall mean is 0.47 and the median positive-
demand mean is 2.10. These are separate panel summaries: the
median within-material ratio is 5.06, and 80.3% of materials
exceed2×(Fig. 5). Equation 6 therefore centers the represen-
tation on a mean dominated by zeros, which may contribute
to the negative bias observed in the benchmark. We replace
it with the non-zero-conditional mean¯x nz =E[x|x >0]
and standard deviations nz = std(x|x >0)(Eq. 7); we
refer to this normalization change asnon-zero-conditional re-
centering.
ˆxnz t = xt −¯xnz snz .(7)
Normalization uses each origin’s training context only. With
no positive observations the center is zero; a zero conditional
scale (including a single positive observation) is replaced
by the model’sϵ. The stored center and scale also invert
the transform, after undoing any enabled arcsinh mapping.
The change increases forecast error (MASE0.831→0.948,
consistent with the pretrained weights being adapted to the
original centering) but corrects bias (−2.52→ −0.10) and lifts
the 90% per-material fill proxy from 0.775 to0.920(+14.5pp),
atzero training cost. On the complete-order service metric the
same correction lifts Chronos-2’s COFR from 0.54 to0.63
(platforms passing5%→15%). The separate hurdle run’s
mean lead-time forecast rises from 6.5 to 8.9 (Table VI), a
forecast ratio of≈1.4×, not a measured stock ratio. This
brings order service close to the Naive baseline.
The corrected model still misses the 80-of-80 target that
specialists meet with1.4–1.5×Naive’s inventory. The proxy
gain holds across targets (+14to+17pp) andreplicates on
RAF(+17.1pp,0.607→0.778; the centering discrepancy is
widespread there). Table V compares selected approaches from
the thirteen strategies (over 140 configurations) we tested (its
service column is the per-material fill proxy, not the order-
level COFR of Eq. 4): MixFT routes materials to cluster-
specific LoRA adapters and approximately matches zero-shot
accuracy. Pruning 20% increases MASE by approximately
0.0024, suggesting some parameter redundancy for this task.
Changes to normalization, forecast extraction, and downstream
calibration improve service more than fine-tuning in these
tests.
E. A continuous bias–service mechanism
We scale TimesFM’s rate forecast asˆy ′ =αˆy, holding
dispersion fixed, on 500 industrial materials at policy target
0.80. Training uses 69 months; accuracy uses the next six
months and the partial-fulfillment simulation spans 12 months
(L= 6,R= 1). This is aper-material fill-proxystudy,
distinct from Table IV’s complete-order replay. The unscaled
reference (α= 1) has MASE 0.945 and fill proxy 0.636.
TABLE V
CHRONOS-2ADAPTATION:POOLEDMASE (4,558MATERIALS;ORIGINS
69, 75),∆MASEVS ZERO-SHOT(POSITIVE=BETTER;COMPUTED
BEFORE ROUNDING),AND FILL PROXY AT TARGET0.90. SBC:
SYNTETOS–BOYLAN CLASS-BALANCED TRAINING.
Strategy MASE∆MASE Fill proxy@0.90
Zero-shot (baseline) 0.831 n/a 0.775
InstanceNorm¯xnz (no training) 0.948−0.1170.920
MixFT sub-domain (K=6) 0.832−0.0010.753
Magnitude pruning (20%) 0.834−0.0020.776
Quantile selection (90th pctl) 3.603−2.7710.946
Best LoRA (SBC-balanced r8) 0.834−0.003n/a
0 10 20 30 40 50 60
Monthly period
0
2
4
6
8
10
12
14Demand (units)
̄x = 0.9 (overall mean)
̄xnz = 4.4 (positive-demand mean)
(a) Illustrative RUF v2 series
80% zeros; within-series mean ratio 5.0×
Industrial RAF
0.0
0.2
0.4
0.6
0.8
1.0Per-material fill proxy @0.90
0.775
0.607
0.920
0.778
+14.5pp
+17.1pp
(b) Observed service improvement
(no additional training)
Zero-shot Non-zero normalization
Fig. 5. The instance-normalization correction: (a) an illustrative RUF v2 series
showing the overall mean¯xand positive-demand mean¯xnz; (b) the fill-proxy
lift from re-centering on¯x nz, both panels.
Across the testedα= 0.5–2.0 grid, proxy service increases
from 0.52 to 0.72, while mean inventory value grows from
0.3×to3.1×its value atα= 1. The most accurate setting
(α= 0.75, MASE 0.859) serves less well (proxy 0.585).
The near-bias-neutralα ⋆ ≈1.39yields proxy 0.677 at1.76×
unscaled inventory. This factor is calibrated retrospectively
from evaluation demand; prospective deployment requires a
separate calibration window. These are observed trade-offs, not
a pathwise monotonicity guarantee. Thus accuracy and service
optima diverge within one method. Like scaling towardα ⋆, re-
centering reduces negative bias, but changes the representation
without retraining.
F . A structural (hurdle) test
Because changing the forecast mean changes its stock target
(Proposition 1), we also tested astructuralalternative: a hurdle
model that estimates occurrencep t = Pr(Y t >0)from the
full history and sizeE[Y t |Y t >0]from the non-zero-
centered Chronos, then mixes them. This is not a matched-
mean experiment. The expected hurdle lowers mean LTD from
6.5 to 5.4 and increases fill proxy from 0.778 to 0.791, but
trails direct re-centering (0.924). Theτ= 0.9size quantile
achieves 0.881 while raising mean LTD to 18.2, bias to+9.5,
and MASE to 2.20. The results do not isolate mean, dispersion,
and distributional shape. Table VI uses a separate full-panel
run; its zero-shot and re-centering MASE and fill-proxy values
differ from Table V by less than 0.01.
Adistribution-awarepolicy that consumes the hurdle’s full
mixed quantile also incurs an inventory penalty. The hurdle
has lower service efficiency in the reported comparison: for

TABLE VI
HURDLE TEST:POOLEDMASEAND SERVICE OVER ALL4,558
INDUSTRIAL MATERIALS AT ORIGINS69, 72, 75 (SIX-MONTH HORIZONS).
LTD:LEAD-TIME DEMAND;SERVICE IS THE PER-MATERIAL FILL PROXY.
Method MASE Bias Mean LTD
Fill proxy
@0.90
Zero-shot (standard norm) 0.834−2.276.5 0.778
Non-zero re-centering 0.955+0.148.90.924
Hurdle, expected 0.926−3.315.4 0.791
Hurdle,τ=0.7size 1.054−1.257.5 0.771
Hurdle,τ=0.9size 2.198+9.5218.2 0.881
low-occurrence materials, its service quantile often falls inside
the zero mass, setting an order-up-to level of zero (60.8% of
materials atτ=0.70) and limiting their service. At matched
fill proxy0.85, it needs about1.6×the inventory of plain re-
centering. Using the full forecast distribution raisesachievable
service at an inventory cost; mean-correcting re-centering is
the most inventory-efficient correction tested at the reported
service targets.
G. The findings reproduce on the RUF panel
On the released RUF panel (Section III-B) the main findings
extend to the full 38-method roster. The accuracy leaders again
include foundation models and the weighted moving average
(WMA, TimesFM, and Chronos-Bolt occupy MASE ranks 1–
4). The decision-facing inversion reproduces across the 5,000-
material panel: MASE rank and per-material service rank
correlate atρ=−0.47at the 80% target, negative at every
service level (run on the released RUF v2 panel; significance,
bootstrap, and regeneration-seed checks are in Table VII).
This is the same sign as the real panel and comparable to
the industrial per-material−0.58. The training-free instance-
normalization correction (Section IV-D) reproduces too: re-
centering Chronos-2 on non-zero-conditional statistics lifts the
per-material fill proxy by+17.6to+21.4pp across service
targets (79.1%of materials show the>2×centering artifact),
with an increase in MASE (0.765→0.807), the same trade-off
as on the industrial panel. The public panel corroborates the
leaderboard, correction, and inversion direction; contractual
magnitude remains a private-panel result.
H. Robustness
We assess the sensitivity of the main results to the checks in
Table VII, including the attenuation under per-method policy
tuning.
All cited streams areaudited(method failures are logged
and counted, never silently replaced), and the panels are kept
distinct (the industrial slices are enumerated in the Section III
footnote). RAF uses a seed-fixed, Syntetos–Boylan-stratified
500-series sample, sized by the cost of running 38 methods
over rolling origins. Table III ranks full-coverage audited
methods; failure-subset scores are unranked. Its BATS/TBATS
scores use 500 series, whereas the separate rolling-origin
service stream uses 100 for their state-space refits. Thus RAF’s
38-method correlation is an available-case replication, not
TABLE VII
THREATS TO VALIDITY AND CORRESPONDING ROBUSTNESS CHECKS. THE
POLICY-FORM CHECK IS SUMMARIZED INSECTIONIV-A.
Threat Check Result Reading
Metric
artifact
MASE lag-1/3/12 rankings stable,
ρ≥0.99
stable across
tested scales
Lucky
sample
caps×seeds (12
cfg)
top cluster identical,
ρ≥0.988
stable across
tested samples
Sparsity
alone
RAF-matched
industrial subsets
inversion persists,
ρ≈ −0.42to−0.47
sparsity alone
insufficient
Gaussian-
policy
artifact
distribution-
aware quantile
policy (§IV-A)
inversionstrengthens,
−0.59→ −0.70
holds under both
forms
Lead-time
artifact
order-levelρat
H∈{1,3,6,12}
sign stable,strengthens
withH,−0.47to
−0.61
stable across
tested horizons
Per-method
z-tuning
cost-optimal /
service-maxz
per method
sign remains negative;
cost-optimalz:
ρ=−0.28,p= 0.09;
service-maxz:−0.38,
p= 0.02
attenuated under
per-method
tuning
“Just over-
stocking”
bias ladder
(§IV-E)
service costs inventory;
bias-neutral operating
point
a controlled
trade
Adaptation
overfit
material-level
5-fold CV
zero-shot 0.905 vs.
LoRA≥0.918
holds
out-of-sample
Reliance on
private data
synthetic 38/38
replay (5,000
mat.)
reproduces,ρ=−0.47
(p <0.05at every
target;p <0.005for
0.70–0.90,n= 38); CI
[−0.76,−0.10]
excludes 0; seeds
43–47:−0.41to
−0.61; gate PASS
publicly
checkable
a uniformly matched-material comparison. The caps×seeds
check (Table VII) leaves the top cluster identical (ρ≥0.988).
No tested protocol variation reverses the sign of the industrial
inversion, although its magnitude and statistical significance
depend on the evaluation choices.
V. CONCLUSION
We benchmarked 38 forecasting methods across eight model
classes on an industrial spare-parts panel and public panels.
The accuracy rankinginvertsagainst the contractual complete-
order service target on the industrial panel. The corresponding
relationship with per-material service weakens on the public
RAF panel and is positive on low-intermittency M5: a regime-
dependent forecast–inventory relationship whose sign tracks
forecast bias direction. Examining that bias in a foundation
model’s instance normalization yielded a zero-training-cost
correction that recovers lost service on both panels, including
order-level COFR on the industrial panel.
For deployment, accuracy and service can favor different
model choices: WMA tops the order-relevant industrial accu-
racy ranking, while bias direction helps explain service differ-
ences. Correcting this bias improves service despite increasing
forecast error. For Chronos-2, modifying normalization is
effective, while the tested fine-tuning configurations do not
improve on zero-shot accuracy.

RUFaddresses the reproducibility barrier posed by confi-
dential industrial data. We rerun the findings on a regenerate-
until-fidelity surrogate certified against the real panel. The
leaderboard, correction, and inversion direction reproduce.
Adapted to other count or continuous series, the generate-
then-certify loop could provide open certified surrogates for
confidential corpora and decision-aware benchmarks in other
domains.
Limitations and future work.The industrial evidence
comes from one domain at monthly granularity, and the 80-
of-80 target is illustrative. The M5 comparison suggests that
the inversion depends on heavy intermittency with directional
forecast bias; we do not claim the negative correlation trans-
fers to fast-moving demand. The diagnostic holds a com-
mon inventory policy fixed to isolate forecast effects; future
work should jointly optimize forecast choice and cost-aware
inventory policy, including distribution-aware decisions and
copula dependence. The service gains from distribution-aware
decisions carry an inventory cost (Section IV-F). A second
direction is directive-conditioned forecasting, which incor-
porates forward-looking operational information unavailable
from demand history alone. Finally, the reported service gains
carry inventory trade-offs; Proposition 1 orders stock targets,
not realized service. Jointly optimizing complete-order service
and inventory cost is therefore a multi-objective next step.
Practitioners should measure forecast bias direction along-
side accuracy before deployment. Under an asymmetric ser-
vice contract, the lowest-error forecast need not deliver the
highest service.
Availability.The RUF benchmark (v1 structural and v2
parametric, panel of Section IV-G), its generators, evalua-
tion code, full public-panel leaderboard, and a per-artifact
reproduction guide are at https://github.com/sfcheng-research/
icdm-2026-reproduction. The industrial panel is confidential.
REFERENCES
[1] S. Makridakis, E. Spiliotis, and V . Assimakopoulos, “The M5 accu-
racy competition: Results, findings, and conclusions,”Int. J. Forecast.,
vol. 38, no. 4, pp. 1346–1364, 2022.
[2] F. Petropouloset al., “Forecasting: theory and practice,”Int. J. Forecast.,
vol. 38, no. 3, pp. 705–871, 2022.
[3] J. E. Boylan and A. A. Syntetos,Intermittent Demand Forecasting:
Context, Methods and Applications. Wiley, 2021.
[4] A. A. Syntetos and J. E. Boylan, “The accuracy of intermittent demand
estimates,”Int. J. Forecast., vol. 21, no. 2, pp. 303–314, 2005.
[5] T. E. Goltsos, A. A. Syntetos, C. H. Glock, and G. Ioannou, “Inventory
– forecasting: Mind the gap,”Eur. J. Oper. Res., vol. 299, no. 2, pp.
397–419, 2022.
[6] J. D. Croston, “Forecasting and Stock Control for Intermittent De-
mands,”Oper. Res. Q., vol. 23, no. 3, pp. 289–303, Sep. 1972.
[7] R. H. Teunter, A. A. Syntetos, and M. Zied Babai, “Intermittent demand:
Linking forecasting to inventory obsolescence,”Eur. J. Oper. Res., vol.
214, no. 3, pp. 606–615, Nov. 2011.
[8] K. Nikolopoulos, A. A. Syntetos, J. E. Boylan, F. Petropoulos, and
V . Assimakopoulos, “An aggregate–disaggregate intermittent demand
approach (ADIDA) to forecasting: an empirical proposition and anal-
ysis,”J. Oper. Res. Soc., vol. 62, no. 3, pp. 544–554, Mar. 2011.
[9] J. E. Boylan, A. A. Syntetos, and G. C. Karakostas, “Classification for
forecasting and stock control: a case study,”J. Oper. Res. Soc., vol. 59,
no. 4, pp. 473–481, 2008.
[10] E. Theodorou, E. Spiliotis, and V . Assimakopoulos, “Forecast accuracy
and inventory performance: Insights on their relationship from the M5
competition data,”Eur. J. Oper. Res., vol. 322, no. 2, pp. 414–426, 2025.
[11] A. F. Ansari, L. Stella, C. Turkmenet al., “Chronos: Learning
the language of time series,”Trans. Mach. Learn. Res., 2024,
arXiv:2403.07815.
[12] A. Das, W. Kong, R. Sen, and Y . Zhou, “A decoder-only foundation
model for time-series forecasting,” inProc. 41st Int. Conf. Mach. Learn.
(ICML), ser. Proceedings of Machine Learning Research, vol. 235.
Vienna, Austria: PMLR, 2024, pp. 10 148–10 167.
[13] G. Woo, C. Liu, A. Kumar, C. Xiong, S. Savarese, and D. Sahoo,
“Unified training of universal time series forecasting transformers,” in
Proc. 41st Int. Conf. Mach. Learn. (ICML), ser. Proceedings of Machine
Learning Research, vol. 235. Vienna, Austria: PMLR, 2024, pp. 53 140–
53 164.
[14] T. R. Willemain, C. N. Smart, and H. F. Schwarz, “A new approach
to forecasting intermittent demand for service parts inventories,”Int. J.
Forecast., vol. 20, no. 3, pp. 375–387, Jul. 2004.
[15] E. Porras and R. Dekker, “An inventory control system for spare parts at
a refinery: An empirical comparison of different re-order point methods,”
Eur. J. Oper. Res., vol. 184, no. 1, pp. 101–132, 2008.
[16] S. Makridakis, E. Spiliotis, and V . Assimakopoulos, “The M4 Compe-
tition: Results, findings, conclusion and way forward,”Int. J. Forecast.,
vol. 34, no. 4, pp. 802–808, 2018.
[17] R. Godahewa, C. Bergmeir, G. I. Webb, R. J. Hyndman, and P. Montero-
Manso, “Monash time series forecasting archive,” inAdv. Neural Inf.
Process. Syst. (NeurIPS) Datasets and Benchmarks Track, 2021.
[18] T. Aksuet al., “GIFT-Eval: A benchmark for general time series
forecasting model evaluation,”arXiv preprint arXiv:2410.10393, 2024.
[19] S.-F. Cheng and P. Rathnayaka, “M 2–CNN: A macro-micro model for
taxi demand prediction,” in2023 IEEE International Conference on Big
Data (BigData). IEEE, 2023, pp. 1395–1402.
[20] S. Agarwal, B. Charoenwong, S.-F. Cheng, and J. Keppo, “The impact
of ride-hail surge factors on taxi bookings,”Transportation Research
Part C, vol. 136, p. 103508, 2022.
[21] A. N. Elmachtoub and P. Grigas, “Smart “predict, then optimize”,”
Manage. Sci., vol. 68, no. 1, pp. 9–26, 2022.
[22] M. Qiet al., “A practical end-to-end inventory management model with
deep learning,”Manage. Sci., vol. 69, no. 2, pp. 759–773, 2023.
[23] C. Cameron, J. Hartford, T. Lundy, and K. Leyton-Brown, “The perils of
learning before optimizing,” inProc. AAAI Conf. Artif. Intell., vol. 36,
no. 4, 2022, pp. 3708–3715.
[24] A. Syntetos and J. Boylan, “On the bias of intermittent demand esti-
mates,”Int. J. Prod. Econ., vol. 71, no. 1-3, pp. 457–466, May 2001.
[25] A. H. C. Eaves and B. G. Kingsman, “Forecasting for the ordering and
stock-holding of spare parts,”J. Oper. Res. Soc., vol. 55, no. 4, pp.
431–437, 2004.
[26] S. J. Taylor and B. Letham, “Forecasting at scale,”Amer. Statist., vol. 72,
no. 1, pp. 37–45, 2018.
[27] G. Keet al., “LightGBM: A highly efficient gradient boosting decision
tree,” inAdv. Neural Inf. Process. Syst. 30 (NeurIPS), 2017, pp. 3146–
3154.
[28] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,” in
Proc. 22nd ACM SIGKDD Int. Conf. Knowl. Discov. Data Min. (KDD),
2016, pp. 785–794.
[29] D. Salinas, V . Flunkert, J. Gasthaus, and T. Januschowski, “DeepAR:
Probabilistic forecasting with autoregressive recurrent networks,”Int. J.
Forecast., vol. 36, no. 3, pp. 1181–1191, 2020.
[30] B. N. Oreshkin, D. Carpov, N. Chapados, and Y . Bengio, “N-
BEATS: Neural basis expansion analysis for interpretable time series
forecasting,” inProc. Int. Conf. Learn. Represent. (ICLR), 2020.
[Online]. Available: https://openreview.net/forum?id=r1ecqn4YwB
[31] B. Lim, S. O. Arik, N. Loeff, and T. Pfister, “Temporal fusion trans-
formers for interpretable multi-horizon time series forecasting,”Int. J.
Forecast., vol. 37, no. 4, pp. 1748–1764, 2021.
[32] A. M. De Livera, R. J. Hyndman, and R. D. Snyder, “Forecasting time
series with complex seasonal patterns using exponential smoothing,”J.
Amer. Statist. Assoc., vol. 106, no. 496, pp. 1513–1527, 2011.
[33] Amazon Web Services, “Chronos-bolt: Fast and accurate zero-shot
forecasting,” Model card and repository, 2024. [Online]. Available:
https://github.com/amazon-science/chronos-forecasting
[34] A. F. Ansariet al., “Chronos-2: From univariate to universal forecasting,”
2025, arXiv:2510.15821.
[35] C. Bergmeir and J. M. Benitez, “On the use of cross-validation for time
series predictor evaluation,”Inf. Sci., vol. 191, pp. 192–213, 2012.
[36] J.-S. Song, “On the Order Fill Rate in a Multi-Item, Base-Stock
Inventory System,”Oper. Res., vol. 46, no. 6, pp. 831–845, Dec. 1998.
