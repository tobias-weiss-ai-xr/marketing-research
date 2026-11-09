---
title: 'When Prices Double in a Week: Forecasting of Agricultural Volatility in Import-Isolated Markets'
url: https://arxiv.org/abs/2606.29248
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Ranuga Weerasekara
- Heshan Nethmina
- Manuja Ranathunga
- Vinma Wettasinghe
- Dinithi Navodya
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.29248
pages: 9
chars: 26868
fetched_at: '2026-11-08T13:26:54+00:00'
kb_version: 1
---

# When Prices Double in a Week: Forecasting of Agricultural Volatility in Import-Isolated Markets

When Prices Double in a Week: Forecasting of
Agricultural V olatility in Import-Isolated Markets
Ranuga Weerasekara, Heshan Nethmina, Manuja Ranathunga, Vinma Wettasinghe, Dinithi Navodya,
Subavarshana Arumugam, Nirasha Munasinghe, Nisansa de Silva, Sandareka Wickramanayake
Dept. of Computer Science & Engineering, University of Moratuwa, Sri Lanka.
{ranugaw.23, heshann.23, vinmaw.23, dinithin.23, manujar.23,
subavarshanaa.21, nirasha.25, NisansaDds, sandarekaw}@cse.mrt.ac.lk
Abstract—Vegetable prices in Sri Lanka are highly volatile
because the market is largely import-isolated, so supply disrup-
tions quickly drive prices up. This study develops a machine
learning framework to forecast such volatility by incorporat-
ing supply-chain-aware features and explicitly modelling the
country’s two cultivation seasons, Maha (October–April) and
Yala (May–September). An integrated dataset was constructed
by combining retail and farmer-gate prices with origin-aligned
weather variables, diesel costs, and exchange rates across 12
vegetable varieties and 14 market centres from 2013 to 2019.
A gradient-boosted ensemble model (XGBoost and LightGBM)
was trained and optimised using Optuna, and unified and
season-specific configurations were compared. Results show that
season-specific models improve within-season fit, with the Yala-
specific model achieving the highestR 2 of 0.9420 (95% CI
[0.690, 1.000]), while the unified model delivers the best overall
predictive accuracy of 90.84% (95% CI [88.34%, 91.52%]) and
anR 2 of 0.9281 (95% CI [0.760, 1.000]). Notably, the unified
model maintains 85.96% accuracy on a completely unseen 2024
hyperinflationary period without retraining, successfully tracking
major price surges. These findings suggest that agricultural
price movements in import-constrained markets are meaningfully
predictable when models capture supply-chain dynamics, offering
practical value for early warning and decision making by farm-
ers, traders, and policymakers. Existing studies on Sri Lankan
vegetable prices are confined to Autoregressive Integrated Mov-
ing Average (ARIMA) and Generalized Autoregressive Condi-
tional Heteroskedasticity (GARCH) applied to single markets,
with no supply-chain features, seasonal segmentation, or cross-
regime validation.
Index Terms—agricultural price forecasting, XGBoost, Light-
GBM, import-isolated markets, seasonal modelling, supply-chain
feature engineering, cross-regime generalisation, Sri Lanka
I. INTRODUCTION
Predicting agricultural prices is a well-studied problem.
Statistical models such as ARIMA and Seasonal ARIMA
(SARIMA) [1] and Prophet [2] have been widely used,
while gradient-boosted methods like XGBoost [3] and Light-
GBM [4] have outperformed them on complex, non-linear
price data [5]. However, three problems remain unsolved
across the literature: existing models source weather data from
retail markets rather than actual growing zones; they treat a
full year of prices as one continuous series, ignoring seasonal
structure; and they rarely test whether a trained model holds
up under a completely different economic regime [6, 7].
Sri Lanka makes all three problems worse. Its vegetable
market is fully import-isolated; every flood, drought, or supply
breakdown hits retail prices directly with no buffer, causing
prices to double within a single week [8]. Its two cultivation
seasons,Maha(October–April) andYala(May–September),
governed by opposing monsoons, create structurally different
supply conditions that a single annual model cannot separate.
Production further divides intoupcountrycrops (carrots, leeks,
green beans) grown in the central highlands andlowcountry
crops (brinjals, pumpkin) grown across the wet and dry zones.
Prior work on this market has relied exclusively on ARIMA
and GARCH applied to single markets and limited varieties [1,
5, 9], with no supply-chain features, seasonal segmentation, or
cross-regime validation ever attempted.
This study addresses the gap through four sequential steps:
1) Construct the first integrated Sri Lankan vegetable price
dataset, resolving spatial weather mismatch and missing-
ness through four novel preprocessing strategies across
12 vegetable varieties and 14 market centres (2013–
2019).
2) Engineer supply-chain-aware features, including origin-
zone weather lags, diesel-driven logistics costs,
USD/LKR exchange rates, and farmer-gate spreads,
to encode structural market mechanics.
3) Train and compare unified and season-specific gradient-
boosted ensemble models (XGBoost + LightGBM, Op-
tuna tuned) across Maha and Yala seasons to quantify
the precision-versus-momentum trade-off.
4) Evaluate cross-regime generalisation on the fully unseen
2024 hyperinflationary period without retraining, to test
whether structural mechanics transfer across economic
regimes.
The study is guided by the following five research questions:
1)RQ1:Are price shocks in a fully import-isolated market
structurally predictable, or do they behave as random
walks?
2)RQ2:What forces govern the farmer-gate-to-retail
spread across seasons?
3)RQ3:Do Yala/Maha-specific models outperform a uni-
fied model, or does cross-season blindness cancel the
gains?
4)RQ4:Do macroeconomic step-changes (diesel,
USD/LKR) outweigh weather signals in predictive
importance?
arXiv:2606.29248v3  [cs.LG]  14 Aug 2026

5)RQ5:Can a 2013–2019 model generalise to the 2024
hyperinflationary regime without retraining?
This paper is structured as follows. Section II reviews
related work in agricultural price forecasting. Section III
describes the dataset construction process. Section IV presents
the methodology and modelling framework. Section V reports
experimental results, and Section VI discusses key insights.
Finally, Section VII concludes the paper and outlines direc-
tions for future work.
 Dataand
 codefor this work
are publicly available.
II. RELATEDWORK
A. Statistical Time-Series Models
Statistical time-series models remain the dominant baseline
in agricultural price forecasting. ARIMA and its seasonal
extension, SARIMA, have been widely applied to vegetable
and commodity markets in South Asia, with Champika and
Mugera [1] demonstrating 71% forecast accuracy for carrot
retail prices in Sri Lanka using SARIMA(3,1,2)(0,0,2)[52],
where the non-seasonal orders(p=3, d=1, q=2)denote the au-
toregressive, differencing, and moving-average terms; the sea-
sonal orders(P=0, D=0, Q=2)their seasonal counterparts;
and the subscript 52 the annual weekly period. Prophet [2]
extends this with piecewise trend modelling robust to report-
ing gaps, making it attractive for developing-country data.
Hybrid approaches combining statistical and machine learn-
ing methods have also been explored for agricultural price
forecasting [10]. Gradient-boosted ensembles have consis-
tently outperformed statistical baselines: XGBoost [3] and
LightGBM [4] handle mixed feature types and non-linear
interactions natively, and Madubhashini [5] demonstrated their
superiority over ARIMA for Sri Lankan wholesale vegetable
price prediction.
B. Gradient-Boosted Ensembles
XGBoost [3] and LightGBM [4] have consistently outper-
formed statistical baselines on non-linear tabular prediction
tasks. Their threshold-splitting architecture naturally handles
mixed feature types without requiring explicit interaction
terms. Tree-based and ensemble methods, including gradient
boosting, random forest, and stacking regression, have been
applied to Sri Lankan and broader South and Southeast
Asian commodity price forecasting [5, 11], but rarely with
the supply-chain-aware feature engineering that agricultural
markets demand.
C. The Unaddressed Gap: Sri Lanka’s Import-Isolated Market
Sri Lanka’s vegetable market remains the most volatile and
least studied food market in South Asia from a machine
learning perspective [1]. Under full import isolation, every
domestic supply shock hits retail prices with no external
buffer [1]. The Maha and Yala seasons create structurally
different supply corridors, crop mixes, and rainfall regimes
that a single annual model cannot disentangle, yet no validated,
integrated dataset or supply-chain-aware seasonal forecasting
framework exists for this context. Closing this gap directly
supports food security policy, farmer incomes, and consumer
price protection, giving agricultural authorities a data-driven
foundation for early warning and price stabilisation.
To our knowledge, this is the first study to integrate origin-
zone weather alignment, dual-origin farmer-gate imputation,
supply-chain-aware feature engineering, and cross-regime val-
idation into a single forecasting framework for an import-
isolated vegetable market, in contrast to prior Sri Lankan work
that applies ARIMA or GARCH to single markets without any
supply-chain features.
III. DATASETCONSTRUCTION
A. Strategy 1: Data Reduction
The raw retail dataset [8] spanned 26 varieties, 37 markets,
2008-2024:746,304 cells, 26.30% missing. Rather than im-
puting∼200k target-variable values, the study was scoped to
the 12 most consistent vegetables and 14 most robust markets
over 2013-2019, as summarised in Table I.
TABLE I
EFFECT OF DATA SCOPING ON MISSINGNESS.
Metric Raw Reduced
Total records 746,304 61,152
Missing values 196,310 3,286
Missing % 26.30% 5.37%
The 12 retained varieties (Ash Plantains, Beetroot, Brinjals,
Cabbage, Carrot, Green Beans, Green Chillies, Ladies Fingers,
Leeks, Pumpkin, Snake Gourd, Tomatoes) cover both upcoun-
try and lowcountry systems, ensuring structural representation
of both seasons.
B. Strategy 2: Dual-Origin Farmer Price Imputation (RQ2)
Urban hubs like Colombo have extensive retail records but
zero farmer-gate prices, as large-scale cultivation does not
occur in these cities. The raw producer dataset was33.82%
missing. The supply chain was reverse-engineered: for each
missing urban location, the top two historically supplying
producer markets were identified and their arithmetic mean
imputed. This dropped missingness to7.59%. Residual gaps
(≤4 consecutive weeks) were filled via bounded linear inter-
polation.Final farmer-gate missingness: 3.85%.
Accurate farmer-gate data matters because the farmer-to-
retail spread ranks among the strongest predictors in the
model. Fig 1 illustrates price trend behaviour for Beetroot,
and Ash Plantains.
C. Strategy 3: Origin-Averaged Weather Alignment (RQ4)
Urban weather is irrelevant to crop yield; carrots sold
in Colombo, for instance, are grown in Nuwara Eliya. For
every retail market-vegetable pair, the true cultivation source
zones were mapped, daily weather (rainfall, mean apparent
temperature) was fetched exclusively for those origins from
Open-Meteo 1, and the geographic mean across all supplying
1https://open-meteo.com

(a) Beetroot
(b) Ash Plantains
Fig. 1. Retail vs. farmer-gate price trends for two representative vegetables across the study period.
districts was computed. Features were lagged at 1, 4, and
8 weeks to capture the delayed phenological impact on retail
prices.
Fig 2 shows that price variation tracks rainfall at cultivation
zones, not at retail markets. The optimal lag differs across
vegetable-market combinations, which motivates the use of 1-
, 4-, and 8-week lag features.
D. Strategy 4: Macroeconomic and Calendar Features
Three features were integrated at100% completeness:
Lanka Auto Diesel prices 2, USD/LKR exchange rate 3, and
a weekly public holiday count (Poya days and statutory
holidays). Fig 3 summarises the cumulative effect of the four
preprocessing strategies on missingness.
IV. METHODOLOGY
A. Feature Engineering
Raw temporal and spatial variables were transformed to
capture three distinct dynamics: short-term price momentum,
delayed weather effects, and macroeconomic regime context.
2https://ceypetco.gov.lk/historical-prices/
3https://www.cbsl.gov.lk/statistics/economic-indicators/monthly-bulletin
Lag features.For each market-vegetable group, lagged
values ofretail_price,mean_farmer_price,
reg_rain, andreg_tempwere computed at offsets
of 1, 2, 3, 4, and 8 weeks.Rolling statistics.Four-week
and eight-week rolling means and standard deviations of
farmer prices capture volatility regimes.Momentum and
spread.A momentum feature captures the ratio of the
1-week lag to the 4-week rolling mean; the lagged farmer-
to-retail spread encodes markup dynamics, independently
of base crop prices.Cyclical encoding.Week numbers
were encoded assin(2πw/52)andcos(2πw/52)to preserve
circular continuity.Interaction.A diesel-season interaction
term encodes the differing cost implications of fuel prices
across the Yala and Maha seasons.
B. Outlier Treatment
Interquartile Range (IQR) analysis reveals that statistical
outliers account for 1-4% of observations per vegetable type.
All outliers areretainedfor three reasons: (1) they rep-
resent genuine supply shocks the exact events this model
must predict; (2) gradient-boosted trees are natively robust to
magnitude extremes via threshold splitting; (3) anp.log1p

Fig. 2. Origin-averaged rainfall (4-week lag) vs. retail price for Pumpkin. Rainfall at cultivation zones precedes retail price movements by≈4 weeks.
Fig. 3. Missingness reduction pipeline: retail from 26.30% to 5.37% (Strat-
egy 1); farmer-gate from 33.82% to 3.85% (Strategies 2-3).
transformation on the target variable compresses violent spikes
without discarding the signal. Fig. 4 shows the outlier distri-
bution.
C. Predictive Modelling Framework
Three parallel configurationsUnified,Yala-only, and
Maha-onlyare trained and compared (RQ3). The pipeline
operates in three stages.
Stage 1: Baseline.A SARIMA time-series model provides
the statistical baseline, attaining 71.20% accuracy, consistent
with the SARIMA performance reported for Sri Lankan veg-
etable prices by Champika and Mugera [1]. This baseline
shows that temporal structure alone is insufficient for a market
shaped by weather, diesel changes, and supply-chain momen-
tum.
Stage 2: Gradient-boosted ensemble.The main model
combines XGBoost [3] and LightGBM [4]. Both were tuned
with Optuna [12]. The final prediction is a weighted average,
as shown in Eq. (1):
ˆy=wxgb ·ˆyxgb +w lgb ·ˆylgb (1)
The ensemble weights were chosen by Bayesian search to min-
imise validation MAPE, givingw xgb = 0.52andw lgb = 0.48.
Stage 3: Interpretability.Feature importance was assessed
through ablation testing, removing one variable group at a time
and measuring the change in MAPE (Section VI).
D. Cross-Validation and Confidence Interval Estimation
To confirm that results do not depend on a single split, a
5-fold time-series cross-validation was applied. Each market-
vegetable pair was kept in chronological order and split with an
expanding window, so no future information entered training.
For each fold, XGBoost and LightGBM were retrained with
the same tuned hyperparameters, and predictions were blended
with fixed ensemble weights. Reported R 2 and MAPE values
are fold means.
To express statistical reliability, 95% confidence intervals
were constructed using thet-distribution, as given in Eq. (2):
¯x±tα/2, k−1· σ√ k (2)
wherek= 5andσis the sample standard deviation. Since R 2
is bounded above by 1, any upper confidence limit exceeding
1.0 was clipped to 1.0 when reported.
V. RESULTS ANDANALYSIS
All results use the final 20% of each market vegetable
group’s time-ordered records as the held-out test set (≈2018-
2019), ensuring no temporal leakage.

Fig. 4. IQR-based outlier distribution across 12 vegetable types. Outliers represent genuine supply shocks and are retained.
A. Ensemble Performance (RQ1)
Table II reports the ensemble model’s overall performance
on the held-out test set.
TABLE II
ENSEMBLE MODEL PERFORMANCE ON THE2018-2019HELD-OUT TEST
SET WITH95%CONFIDENCE INTERVALS FROM CROSS-VALIDATION.
ACCURACY IS REPORTED AS1−MEANABSOLUTEPERCENTAGEERROR
(MAPE)
Metric Score 95% CI
R2 Score 0.9281 [0.7596, 1.0000]
Accuracy (1−MAPE) 90.84% [88.34%, 91.52%]
XGBoost individual accuracy 90.76% [88.16%, 91.54%]
LightGBM individual accuracy 90.72% [88.34%, 91.32%]
BecauseR 2 is bounded above by 1, its upper confidence
limit is truncated at this theoretical maximum. With onlyk= 5
cross-validation folds, the reported intervals are correspond-
ingly wide and should be read as indicative rather than precise.
The 90.84% accuracy achieved on a zero-import-buffer
market confirms that isolated, volatile price dynamics are
structurally predictable when the model encodes supply-chain
mechanics. Figs. 5 and 6 confirm tight alignment and correct
spike tracking.
B. Seasonal Segmentation Results (RQ3)
Analysis of seasonal segmentation reveals that the Yala-only
model achieves the highestR 2 of 0.9420 (95% CI [0.690,
1.00]), a +0.0139 improvement over the unified model. How-
ever, the wide and overlapping confidence intervals suggest
that this improvement should be interpreted with caution, as
the observed difference may reflect variability across folds
rather than a consistent performance advantage. The unified
model, however, leads in overall accuracy at 90.84% (95%
CI [88.34%, 91.52%]) compared to the Yala-only (90.39%;
95% CI [88.31%, 91.01%]) and Maha-only (90.47%; 95%
CI [87.97%, 91.61%]) configurations. This demonstrates that
cross-season price momentum provides a compensating advan-
tage in overall prediction. The Maha-only model’s lowerR 2
of 0.9210 (95% CI [0.776, 0.996]) likely reflects the greater
volatility and unpredictable supply disruptions characteristic
of the northeast monsoon season. Fig. 7 shows this trade-off.
Fig. 8 confirms the weighted ensemble consistently outper-
forms either individual base learner.
VI. DISCUSSION
A. Farmer-Gate-to-Retail Spread Dynamics (RQ2)
The dual-origin imputation strategy (Strategy 2) enabled
direct examination of the farmer-gate-to-retail markup across
seasons. Analysis of the spread feature reveals three consistent
patterns across seasons. First, the spread is systematically

Fig. 5. Predicted vs. actual on the held-out test set. Tight diagonal clustering confirms low bias (R 2 = 0.9281).
Fig. 6. Validation time-series: the ensemble correctly follows seasonal peaks, troughs, and supply-shock spikes across the test period.
larger during Yala (mean markup 38.4%) than Maha (mean
markup 29.7%), reflecting higher transport costs when high-
land production contracts and lowland supply routes lengthen.
Second, upcountry vegetables (Carrot, Leeks, Green Beans)
exhibit wider and more volatile spreads than lowcountry vari-
eties, consistent with longer supply corridors from the central
highlands to urban markets. Third, the lagged spread is the
single strongest predictor of retail price in the following week
across all model configurations, outranking both weather lags
and diesel price in ablation importance. Farmer-gate dynamics

Fig. 7. Unified vs. seasonal model performance comparison. The Yala model
leads on R 2; the unified model leads on accuracy.
Fig. 8. Individual learner vs. ensemble accuracy across all model configura-
tions, validating the blending strategy.
therefore serve as a primary signal encoding the logistics
cost structure of the Sri Lankan supply chain, rather than a
secondary variable introduced solely to address missing data.
B. Macroeconomic Feature Effects (RQ4)
Ablation results (Table III) show that removing macro
features like diesel actually increases R 2 slightly and changes
accuracy by only∼0.05 pp. This answers RQ4 with a clear
no: macro features do not outweigh weather data. Weather
lags and farmer-gate spreads are the true dominant predictors
in our model.
However, the diesel price is still useful for extreme events.
Because fuel prices jump in sudden steps, they do not help
with everyday smooth trends, but they capture sudden trans-
portation cost shifts during supply shocks. Therefore, R 2 alone
undervalues diesel because its signal is concentrated only in
extreme spikes rather than everyday price movements.
TABLE III
FEATURE ABLATION:IMPACT OF REMOVING MACROECONOMIC
VARIABLES.
Configuration R 2 Acc. MAPE
Full model 0.928190.84% 9.16%
Without Diesel 0.9308 90.79% 9.21%
Without USD/LKR 0.9309 90.78% 9.22%
C. Cross-Regime Generalisation (RQ5)
The 85.96% accuracy retained on the completely unseen
2024 hyperinflationary regime without any retraining is the
most significant empirical finding of this study, as summarised
in Table IV. Fig. 9 contrasts predicted versus actual scatter
across both regimes. The∼5 percentage point degradation
from the in-sample result is attributable to the known tree
extrapolation problem: gradient-boosted models cannot predict
beyond the value range seen in training. However, the fact
that relative supply-chain dynamics transfer across a fivefold
inflation regime confirms that the model encodes structural
market mechanics, rather than memorising absolute price
levels. The 0.95% error at the Week 29 surge point (Table V)
is especially important because this is when an early warning
system would be most useful. Per-vegetable and per-market
results for all 12 varieties and 14 markets, across both the
2013–2019 and 2024 evaluations, are provided in full in the
accompanying data and code repository.
TABLE IV
OUT-OF-TIME VALIDATION:IN-SAMPLE VS.UNSEEN2024REGIME.
Metric 2013-2019 2024 (Unseen)
R2 0.9281 0.7336
Accuracy (1−MAPE) 90.84% 85.96%
Micro-analysis: 274 LKR supply shock.Green Chillies at
Kaluthara in 2024 provide the hardest stress test.
TABLE V
GREENCHILLIES ATKALUTHARA:TRACKING A274 LKRSURGE.
Wk∆prev. Actual Predicted Error
28 +146 470.00 424.45 9.69%
29 +114 584.00 589.560.95%
30 +160 744.00 712.61 4.22%
31−23 720.86 700.08 2.88%
32−23 697.71 683.65 2.01%
At Week 29 (surge inflection), the prediction error is0.95%.
At Week 30, prices reach 744 LKR entirely outside the training
distribution yet the model tracks to 712.61 with 4.22% error.
The 5-week average error is3.95%(Fig. 10).

Fig. 9. Cross-regime performance: stable economy (2013-2019) vs. unseen hyperinflationary regime (2024).
Fig. 10. Micro-analysis of the 2024 Green Chillies supply shock at Kaluthara.
Sub-1% error at Week 29 confirms structural mechanics transfer across
regimes.
D. Interpreting the 2024 R 2 Decline: Concept Drift vs. Struc-
tural Integrity
The drop in R 2 from 0.9281 to 0.7336 on the 2024 test
data reflects concept drift during Sri Lanka’s economic crisis;
however, the model maintained 85.96% accuracy and correctly
identified the timing and location of price spikes, confirming
that supply-chain structural mechanics held across economic
regimes.
E. Limitations
Two limitations qualify these results. First, the dataset was
scoped to the 12 lowest-missingness varieties and the 14
most robust markets (Strategy 1); while this improves data
quality, it may bias accuracy upward relative to the full, sparser
national market, and the reported figures should be read with
this selection in mind. Second, the confidence intervals are
estimated from only five cross-validation folds and are conse-
quently wide and overlapping, so small differences between
model configurations are indicative rather than statistically
significant.
VII. CONCLUSION
This research demonstrates that agricultural price volatility
in an import-isolated economy exhibits structural governance
and can be predicted mathematically.This research demon-
strates that agricultural price volatility in an import-isolated
economy exhibits structural governance and can be predicted
mathematically. The Yala model leads on R², the unified model
on accuracy and it suggests seasonal segmentation may better
capture within-season dynamics, though within overlapping
confidence intervals.

While neither approach is universally superior, the selection
of the unified versus seasonal model should be guided by
whether transition-week accuracy or within-season precision
is the primary operational requirement.
A gradient-boosted ensemble achieves90.84%accuracy
on held-out test data and85.96%on a fully unseen 2024
hyperinflationary regime without retraining. This cross-regime
transfer is possible because the model focuses on structural
mechanics. It encodes origin-zone weather lags, diesel-driven
logistics costs, and farmer-gate momentum, rather than mem-
orising absolute price levels. Critically, prediction error is
lowest during the sharp supply-shock events that pose the
greatest risk to food security.
Future work will address the tree extrapolation limitation
through three strategies: (1) inflation-adjusted targets nor-
malised by a diesel index; (2) time-decay sample weighting to
emphasise recent cost structures; and (3) shock-detection com-
posite features that dynamically rebalance ensemble weights
during extreme events.
ACKNOWLEDGEMENTS
The authors thank the Hector Kobbekaduwa Agrarian Re-
search and Training Institute (HARTI) for providing access to
the vegetable price dataset that made this research possible.
REFERENCES
[1] J. A. Champika and A. Mugera, “Analysis of price behavior in Sri
Lankan vegetable market,”J. Agribus. Market., vol. 10, no. 1, pp. 4–29,
2023.
[2] S. J. Taylor and B. Letham, “Forecasting at scale,”Amer. Statist., vol. 72,
no. 1, pp. 37–45, 2018.
[3] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,”
inProc. 22nd ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining,
2016, pp. 785–794.
[4] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-
Y . Liu, “LightGBM: A highly efficient gradient boosting decision tree,”
Adv. Neural Inf. Process. Syst., vol. 30, 2017.
[5] E. L. N. D. Madubhashini, “Predicting vegetable prices in Sri Lanka
using machine learning techniques,” Master’s thesis, Univ. Colombo
School Comput., Sri Lanka, 2023.
[6] R. J. A. Little and D. B. Rubin,Statistical Analysis with Missing Data.
Wiley, 2019.
[7] A. M. Komarek, A. De Pinto, and V . H. Smith, “A review of types
of risks in agriculture: What we know and what we need to know,”
Agricult. Syst., vol. 178, p. 102738, 2020.
[8] Hector Kobbekaduwa Agrarian Res. Training Inst., “Weekly
Average Retail Prices of All Vegetable Varieties,” 2024, [Online].
Available: https://www.harti.gov.lk/index.php/en/market-information/
data-food-commodities-bulletin.
[9] R. Engle, “GARCH 101: The use of ARCH/GARCH models in applied
econometrics,”J. Econ. Perspect., vol. 15, no. 4, pp. 157–168, 2001.
[10] S. K. Purohit, S. Panigrahi, P. K. Sethy, and S. K. Behera, “Time series
forecasting of price of agricultural products using hybrid methods,”Appl.
Artif. Intell., vol. 35, no. 15, pp. 1388–1406, 2021.
[11] I. M. G. L. Illankoon and B. T. G. S. Kumara, “Analyzing the influence
of various factors for vegetable price using data mining,” inProc. 13th
Int. Res. Conf. KDU, 2020.
[12] T. Akiba, S. Sano, T. Yanase, T. Ohta, and M. Koyama, “Optuna: A
next-generation hyperparameter optimization framework,” inProc. 25th
ACM SIGKDD Int. Conf. Knowl. Discovery Data Mining, 2019, pp.
2623–2631.
