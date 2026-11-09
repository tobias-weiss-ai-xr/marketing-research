---
title: Forecasting Weather-Driven Price Dynamics Across Sri Lankan Tea Market Catalogues
url: https://arxiv.org/abs/2608.24894
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Hesandi Mallawarachchi
- Senilka Madurapperumage
- Nadil Kulathunge
- Thilokya Angeesa
- Nethsith Gunaweera
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.24894
pages: 8
chars: 35763
fetched_at: '2026-11-08T13:28:01+00:00'
kb_version: 1
---

# Forecasting Weather-Driven Price Dynamics Across Sri Lankan Tea Market Catalogues

Forecasting Weather-Driven Price Dynamics Across
Sri Lankan Tea Market Catalogues
Hesandi Mallawarachchi, Senilka Madurapperumage, Nadil Kulathunge, Thilokya Angeesa, Nethsith Gunaweera,
Sandeepa Weerasekara, Patalee Narasinghe, Nisansa de Silva, Sandareka Wickramanayake
Dept. of Computer Science & Engineering, University of Moratuwa, Sri Lanka.
{hesandim.23, senilkam.23, nadilk.23, thilokyaa.23, nethsithg.23,
sandeepa.25, patalee.21, NisansaDds, sandarekaw}@cse.mrt.ac.lk
Abstract—We construct and publicly release a novel structured
dataset of 12,233 records parsed from 105 weekly broker PDF
reports spanning late 2023 to 2026, a machine-readable archive
of Colombo Tea Auction (CTA) prices combined with region-
specific lagged weather variables from the Open-Meteo histor-
ical archive. Using this dataset, we investigate the relationship
between local weather conditions and price behavior across
four Sri Lankan tea catalogues: High Grown, Low Grown, Off-
Grade, and Dust. We apply Granger causality analysis alongside
four tree-based machine learning models:Random Forest,
XGBoost,LightGBM, andGradient Boosting. Our results
show that market dynamics are primary drivers, while weather
provides limited catalogue-specific predictive information. Ex-
tended Granger analysis across cumulative lag orders of 1–8
weeks identified one FDR-significant association: temperature
history through four weeks Granger-predicted Dust prices, while
other nominal weather associations were treated as exploratory.
Catalogue-specific modelling outperformed unified approaches,
withLightGBMemerging as the superior model for three out
of four catalogues, though Naive Persistence was the strongest
overall method for Low Grown. Overall, this study highlights the
importance of considering both localized weather patterns and
catalogue-level differences when forecasting tea prices, offering
a more precise and practical framework for the tea industry.
Index Terms—High Grown, Low Grown, Off-Grade, Lagged
weather effects, Catalogue-specific modeling, Granger causality,
LightGBM , Auction price forecasting.
I. INTRODUCTION
As of 2024, Sri Lanka was the world’s fifth largest tea
producer [1] and remains a leading exporter of orthodox (Cey-
lon) tea, with tea contributing roughly 10% of the country’s
agricultural export earnings and supporting more than two
million livelihoods among smallholders, estate workers, and
downstream trades [?]. The Colombo Tea Auction (CTA),
held weekly by the Tea Board of Sri Lanka, is the primary
price-discovery mechanism for Ceylon tea and sets bench-
marks that flow into forward contracts and retail shelves in
more than 90 countries. Price signals from the CTA therefore
have direct welfare consequences for a large, weather-exposed
workforce.
A. Tea Categorization in Sri Lanka
Sri Lankan tea is primarily categorized using two comple-
mentary systems1 that together provide both geographical and
1Information based on weekly market reports by Forbes & Walker Tea
Brokers (Pvt) Ltd, the leading tea broker in Sri Lanka
commercial context for auction pricing and market analysis.
1) Categorization by Elevation (Geographical/Regional):
This is the most structurally important grouping for price
modeling and supply analysis, as elevation strongly influences
tea quality, flavor profile, and growing conditions.
•High Grown Areas- Teas cultivated at higher altitudes,
typically above∼1,200 m (e.g., Nuwara Eliya, Western
High, Uda Pussellawa, Uva regions).
•Medium Grown Areas- Teas from mid-elevation estates,
roughly 600 - 1,200 m.
•Low Grown Areas- Teas grown below∼600 m, mainly
in the southern and southwestern regions (Galle, Matara,
Ratnapura).
2) Categorization by Catalogue Type:This mainly reflects
tea-leaf quality and how teas are physically sorted, processed
and presented at the Colombo Tea Auction:
•High Grown Catalogue- Primarily consists of High and
Medium Grown teas sold in bulk under individual estate
names.
•Low Grown Catalogue- The high-volume Low Grown
production, further subdivided by leaf size and style.
These teas are highly prized for their visual appeal and
brisk taste.
•Off-Grade- Teas that fall outside standard leaf grades
during processing, often containing higher proportions of
fiber, stalk, or broken leaves.
•Dust- The smallest particle size fraction, consisting of
the finest tea dust.
Importantly, both Off-Grade and Dust are mixed cate-
gories that include teas from all three growing regions: High,
Medium, and Low Grown. These four catalogues show sub-
stantial differences in average auction prices, yet most prior
computational work on Sri Lankan tea prices pools all grades
into a single target or uses annual aggregates [2], making it
impossible to recover the catalogue-level drivers that brokers
actually use for decision-making.
Another practical challenge is data. CTA price information
is distributed as weekly PDF reports issued by the eight
licensed brokers including semi-structured tables buried in
prose commentary and there is no public machine readable
archive. By contrast, weather data is abundant but must be
aligned to the correct growing region, auction week and linked
arXiv:2608.24894v2  [econ.GN]  29 Aug 2026

through the biological lag between leaf formation and sale. No
prior study has combined a machine parse-able CTA corpus
with region specific weather and formally tested whether
weather Granger causes [3] catalogue-level prices in the sense
of [4].
This paper makes two contributions to address that gap:
•A novel structured dataset of price observations parsed
from 105 weekly Forbes and Walker broker reports
(November 2023 - March 2026) enriched with region-
specific daily weather from the Open-Meteo historical
archive and aligned at the sale week level with lagged
weather features.
•Practical guidance on catalogue specific price drivers.
This allows brokers to provide more accurate market
advice and buyers to make better sourcing and bidding
decisions.
II. RELATEDWORK
Tea Price Forecasting.Most earlier studies on Sri Lankan
tea prices have taken a macroeconomic approach [5], exam-
ining how exchange rates, oil prices and supply from other
countries affect aggregate export prices [6]. These analyses
operate at monthly or annual frequency and pool across
all grades, which makes them well suited to trade-balance
questions. However, those analyses are unable to resolve the
weekly, catalogue-level dynamics on which brokers and buyers
actually transact. More recently, researchers have started using
machine learning methods such asARIMA,SVR, andLSTMon
Indian tea auction data [7], and a few attempts have been made
to model Sri Lankan prices as well [2]. However, these studies
usually treat all teas as one large group. Most studies do
not explicitly model heterogeneity across grades and auction
catalogues, and few studies incorporate region specific weather
variables into tea price forecasting [7]. This leaves a clear
gap because it is not yet clear how weather and tea-quality
interact across the four distinct catalogues in the Colombo
Tea Auction.
Time-Series Modeling of Agricultural Commodities.
Temporal dependency is a key challenge in forecasting agricul-
tural commodity prices due to the volatile nature of price series
and sensitivity to external shocks. As a result, recent studies
incorporate temporal structures using machine learning and
deep learning approaches to improve forecasting performance
[8]. However, limited work has examined weekly tea auction
prices in Sri Lanka using time series techniques, particularly
in relation to lagged weather effects across different market
catalogues.
Weather and Price Linkages.Agronomists have long
shown that rainfall, temperature, and sunshine strongly influ-
ence tea yield [9] and leaf quality in Sri Lanka [10]. Although
prior agronomic studies in Sri Lanka have examined how
weather affects tea yield and quality, those findings have not
been directly tested against weekly, catalogue-level auction
price formation in the Colombo Tea Auction. There remains
a clear gap between agronomic evidence and catalogue-level
price behavior at auction.
1. Data Collection
(105 PDF reports + Open-Meteo
Extracted usingpdfplumber)
2. Preprocessing &
Feature Engineering
(Lags, Weather, Structural)
3. EDA & Pattern
Analysis (Cyclone Ditwah)
4. Time-Series Diagnostics
(ADF, Granger, Event Window)
5. Modeling & Evaluation
(Catalogue-Specific Model Comparison)
Fig. 1. End-to-end methodology pipeline for Colombo Tea Auction price
modeling.
III. DATASOURCES
The main dataset is constructed from weekly market reports
published by Forbes & Walker Tea Brokers (Pvt) Ltd, one of
eight licensed brokers operating at the Colombo Tea Auction
and a member of the Colombo Tea Traders’ Association
(CTTA). These reports are publicly available [?]. A total of
105 weekly reports from November 2023 to March 2026 were
collected for initial analysis 2.
Meteorological data was obtained from theOpen-Meteo
historical archive API[11], which is free and publicly acces-
sible and provides daily observations without authentication.
Weather variables, including total precipitation (mm), mean
temperature ( ◦C) and sunshine duration (seconds), were ob-
tained for tea-growing coordinates representing High Grown,
Medium, and Low Grown regions. 3 Key features extracted
from the sale reports include catalogue average price in
LKR and USD, total volume sold (kg), text-parsed weather
condition per region, and crop intake direction.
IV. METHODOLOGY
The overall methodology follows a five-stage end-to-end
pipeline as displayed in Figure 1:
A. Data Collection
Structured data was extracted from each weekly Forbes &
Walker PDF report usingpdfplumber, a Python library
specialized in table extraction from PDFs. A custom multi-
table pipeline was developed to parse the reports and generate
nine standardized CSV files per run. Table I describes the main
dataset overview.
In addition to market and price tables, weather in-
formation was collected from two sources. First, textual
weather and crop condition descriptions were parsed di-
rectly from theCROP AND WEATHERsection of
2https://www.forbestea.com/statistics-tea-market-reports
3Region centroids used for Open-Meteo API calls: Western High
Grown/Maskeliya (6.9271°N, 80.5350°E), Nuwara Eliya (6.9497°N,
80.7891°E), Uva/Uda Pussellawa (6.8700°N, 81.0600°E), Low
Grown/Matara–Galle (6.2500°N, 80.3000°E). Off-Grade and Dust catalogues
use Low Grown as primary and Western High Grown as secondary region,
reflecting their mixed-elevation sourcing.

TABLE I
DATASETOVERVIEW
Property Total Rows Rows with Price Missing Target
Dust 2,205 2,171 34 (1.5%)
High Grown 2,124 2,124 0 (0.0%)
Low Grown 5,384 5,384 0 (0.0%)
Off-Grade 2,520 2,118 402 (16.0%)
each report, producing per-region crop intake direction
(text_crop_change), matched weather condition terms
(text_keywords), and a composite regional severity score
(avg_weather_severity). Second, daily weather data
was retrieved from the Open-Meteo historical archive API for
each tea-growing region and aggregated into 7-day windows;
lagged features at 1, 2, and 3 weeks prior to each auction
date were generated usingauction_date−7×lag as the
reference date, to capture delayed supply effects.
B. Data Preprocessing
A master analytical dataset is constructed by joining the
price observations from the high-grown, low-grown, and
off-grade/dust tables with sale-level context and region-
aligned weather features usingsale_idas the primary
key. The target variableprice_mid_lkris derived as
(price_lo_lkr+price_hi_lkr)/2, with a fallback
toprice_lo_lkrwhen only a lower bound is reported.
The resulting modeling-ready dataset contains 12,233 rows.
Beyond the raw auction and weather variables, two categories
of derived features were constructed.
1) Temporal lags:Lagged features were constructed for
total precipitation (mm), mean temperature ( ◦C), and sun-
shine duration (seconds) at 1, 2, and 3 weeks before each
auction date. Each lag represents a 7-day window fetched
from the Open-Meteo API usingauction_date−7×lag
as the reference date. This primary window targets short-
term harvest, supply, and auction-market disruption while
preserving observations within the 105-week study period; it
is not intended to represent the full biological crop-to-auction
pathway. To assess longer weather histories, Granger tests
were separately extended to maximum cumulative lag orders
of 4–8 weeks. Missing early-lag values were imputed using
the region-level median because precipitation distributions are
right-skewed.
2) Tea structural features:elevation,grade, and
tiercapture the physical and commercial hierarchy of each
price observation, allowing catalogue-specific models to distin-
guish price behaviour across quality levels.fx_usdprovides
the LKR/USD exchange rate consolidated from year-specific
columns extracted from the PDF reports.
C. Exploratory Data Analysis (EDA)
Table II summarizes the prices by its structural factors. Low
Grown teas consistently command the highest average prices,
followed by High Grown, Dust, and Off-Grade catalogues.
TABLE II
DESCRIPTIVESTATISTICS OFTEAAUCTIONPRICES BYMARKET
CATALOGUE
Group Category Mean(LKR) Median(LKR) SD(LKR)
By Elevation
Low Grown 1,446.8 1,290.0 734.7
High Grown 1,057.6 1,100.0 268.4
Medium Grown 859.9 900.0 189.8
By Catalogue
Low Grown 1,578.7 1,400.0 749.5
High Grown 1,135.6 1,170.0 261.5
Dust 984.4 985.0 207.3
Off-Grade 792.2 730.0 169.3
Overall1,255.8 1,120.0 623.7
Note:The Low Grown “By Elevation” aggregates all tea grown below
600m, whereas the Low Grown “By Catalogue” is a specific commercial
subdivision sorted by leaf size and style that excludes mixed categories like
Off-Grade and Dust
This clear segmentation by elevation and catalogue type high-
lights the need for catalogue-specific modeling approaches in
Sri Lanka tea auction price analysis.
Low Grown is the dominant catalogue in the dataset, both
in size and variability, with 5,436 records, substantially higher
than Dust, High Grown, and Off-Grade. Off-Grade further
shows a notable data quality concern, with a 15.95% rate
of missing price values, which introduces potential bias in
any aggregate comparisons unless handled in a catalogue-
aware manner. In addition, categorical label completeness
is uneven across catalogues. Structural categorical features
such asgrade,tier, andcatalogueare not equally
informative across catalogues, which explains why catalogue-
specific modelling is often more stable.
D. Time-Series Diagnostics
Auction prices are nota prioristationary and applying
regression based causality tests to non stationary series inflates
type-I error. Therefore, we begin the analysis with three
diagnostic steps.
1) Stationarity:The Augmented Dickey-Fuller (ADF) test
confirmed that Low Grown price series is non-stationary in
levels (p=0.1087) and required first-differencing. Conversely,
High Grown, Off-Grade and Dust prices were found to be
stationary at levels (p <0.05). Among weather variables,
precipitation, temperature, and sunshine duration were gen-
erally stationary across all catalogues, ensuring valid Granger
causality testing.
2) Structural break.:Cyclone Ditwah made landfall on 28
November 2025 and is a candidate structural break. An event
window comparison of prices before and after landfall shows a
short-lived upward shift in High Grown prices consistent with
a supply shock (section VI-A).
3) Granger causality:After ADF-guided differencing, the
primary analysis tested each catalogue×weather variable
combination at maximum cumulative lag orders of 1–3 weeks
(Figure 2). To assess longer weather histories, the same
procedure was separately extended to maximum cumulative
lag orders through 8 weeks. All weather–price conclusions
are predictive associations in the Granger sense, not structural
causal claims.

Since Off-Grade and Dust teas are sourced from all three
growing elevations, no single weather region can fully rep-
resent their supply conditions. Rather than selecting regions
arbitrarily, we aligned these catalogues to the growing areas
most prominently featured in the broker reports, a choice that
also sits comfortably with established agronomic findings on
how mid-to-high elevation temperature conditions shape leaf
quality in Sri Lanka [9]. Alternative region mappings were not
tested; however, this limitation has minimal impact given that
all Granger findings are treated as exploratory.
4) Multiple-comparisons Correction:Benjamini-Hochberg
correction [12] was applied across the 83 estimable tests in the
extended 1–8 week lag family. Out of 96 planned catalogue
weather lag comparisons, 13 High Grown comparisons were
not estimable because the aggregated weather predictor series
contained constant values. Full test outputs are available in the
project repository; results from the extended lag
sensitivity analysis are reported in Section V-A.
E. Models and Training Protocols
We evaluated four tree-based ensemble algorithms:Random
Forest[13],Gradient Boosting[14],XGBoost[15],
andLightGBM[16], under unified pooled and catalogue-
specific strategies. To assess value beyond short-term price
autocorrelation, we also evaluated Naive Persistence, where
ˆpt+1 =p t, and an AR(1) benchmark, whereˆp t+1 =α+βp t,
using only the current-week price within each catalogue–
grade–tier stream.
The target variable isprice_next_week, constructed
by shiftingprice_mid_lkrforward by one auction week
within each product stream. All approaches were evalu-
ated using5-fold chronologicalTimeSeriesSplitcross-
validation. For tree-based models, hyperparameters were se-
lected through grid search across eight candidate configura-
tions per algorithm. This configuration count was chosen as
a practical trade-off given the 105-week study window, and
represents a limitation on tuning depth.
Median imputation was applied usingSimpleImputer
with the median strategy. The imputer was fitted only on
training data within each fold throughscikit-learn[17]
pipeline objects, preventing test-set statistics from influencing
imputation. Rows with missing forecasting targets were ex-
cluded before training and evaluation; the effective Off-Grade
dataset therefore reflects records with valid price labels.
To quantify the incremental contribution of lagged weather,
the selected best tree-based model for each catalogue was
re-evaluated after removing the nine lagged precipitation,
sunshine-duration, and temperature features. Full and ablated
models used identical chronological folds and all remaining
features. We report combined out-of-fold metrics and fold-
wise RMSE mean and standard deviation.
V. RESULTS ANDANALYSIS
A. Granger Causality Analysis
The primary analysis evaluated maximum cumulative lag
orders of 1–3 weeks. Among 33 estimable primary tests,
Fig. 2. Primary Granger test results for maximum cumulative lag orders 1–3.
The heatmap is descriptive; inferential conclusions are based on Benjamini–
Hochberg-adjusted p-values.
10 weather-price associations were nominally significant at
p <0.05. However, none survived Benjamini-Hochberg
correction across the full extended family of 83 estimable
tests. These short-lag findings are therefore interpreted as
exploratory predictive signals rather than confirmed causal
effects.
To assess longer weather histories, the analysis was ex-
tended to maximum cumulative lag orders of 4-8 weeks.
Table III summarizes the best raw result within each lag
range. The only association that survived correction was Dust
temperature at maximum lag 4 (F= 5.843,p= 0.000310,
q= 0.0257). This is a joint test of temperature history
across weeks 1-4, rather than an isolated fourth-week effect.
No maximum cumulative lag order from 5 through 8 weeks
remained significant after correction.
B. Model Performance
1) Evaluation Metrics:Model performance is assessed
using four metrics computed from combined out-of-fold pre-
dictions across five chronologicalTimeSeriesSplitfolds.
Root Mean Squared Error (RMSE):The primary ranking
criterion, measuring prediction error in the original LKR scale.
It penalizes large errors and is sensitive to high price variance.
Mean Absolute Error (MAE):The average absolute devi-
ation per lot in LKR, providing an interpretable measure of
typical error.

TABLE III
DETAILEDLONG-LAGGRANGERSENSITIVITYRESULTS.
Catalogue Weather Best max. lag 1–3; rawpBest max. lag 4–8; rawpMin. FDRq
High Grown Precip. 1; 0.1718 NE 0.3854
High Grown Temp. 1; 0.1936 5; 0.7464 0.4202
High Grown Sun. NE NE NE
Low Grown Precip. 2; 0.0147 4; 0.0716 0.1898
Low Grown Temp. 1; 0.2600 5; 0.5636 0.4877
Low Grown Sun. 1; 0.0199 4; 0.0366 0.1898
Off-Grade Precip. 1; 0.4483 8; 0.5877 0.6645
Off-Grade Temp. 1; 0.0152 8; 0.0484 0.1898
Off-Grade Sun. 1; 0.1110 8; 0.1568 0.3291
Dust Precip. 3; 0.4957 8; 0.3479 0.6278
Dust Temp. 3; 0.0167 4; 0.0003100.0257
Dust Sun. 3; 0.0527 8; 0.0499 0.2302
Lag;preports the maximum cumulative lag order with the smallest raw p-value within the stated group. Min.qis the minimum
Benjamini–Hochberg-adjusted p-value across all estimable lag orders 1–8. NE = not estimable because the aggregated predictor series contained constant
values. A maximum lag ofkjointly tests weather information from weeks 1 throughk.
Coefficient of Determination (R 2):Measures the proportion
of price variance captured relative to a mean-prediction base-
line. A positiveR 2 indicates predictive value, while values
≤0do not outperform the catalogue mean.
Mean Absolute Percentage Error (MAPE):The mean abso-
lute error expressed as a percentage of the actual price. Since a
fixed LKR error produces a larger percentage error for lower-
priced catalogues, MAPE should be interpreted alongside
RMSE rather than compared directly across catalogues.
2) Catalogue-Specific Models:Table IV compares price-
only baselines with the four tree-based models. Among the
tree-based models,LightGBMachieved the lowest RMSE
for High Grown and Off-Grade, whileXGBoostperformed
best for Dust. However, Naive Persistence was the best overall
method for Low Grown, achieving an RMSE of79.76LKR
and anR 2 of0.9896, compared withLightGBM’s RMSE of
145.43LKR andR 2 of0.9653.
For High Grown, Off-Grade, and Dust, the best tree-based
model improved on Naive Persistence by33.31%,45.78%, and
52.42%in RMSE, respectively. Thus, tree-based models add
forecasting value for these catalogues, whereas Low Grown’s
high one-week predictability is primarily explained by short-
term price persistence.
3) Weather-Feature Ablation and Fold Variability:Table V
isolates the contribution of lagged weather features. Removing
lagged weather increased out-of-fold RMSE by1.10LKR for
High Grown,5.03LKR for Low Grown,2.19LKR for Off-
Grade, and4.78LKR for Dust. These gains indicate modest
incremental value from lagged weather, with the clearest
improvements observed for Low Grown and Dust. However,
the gains are small relative to fold-level RMSE variation and
should be interpreted cautiously. Low Grown’s full machine-
learning model also remains less accurate than the Naive
Persistence baseline.
4) Unified Pooled Model:In the pooled setting,LightGBM
achieved the lowest RMSE of139.17LKR and anR 2 of
0.9516. It improved on Naive Persistence by21.36%in
RMSE, indicating that the richer pooled feature set adds
predictive value beyond short-term price persistence. However,
the pooled result is influenced by the larger Low Grown
catalogue and should be interpreted alongside the catalogue-
specific results.
VI. KEYFINDINGS
A. Short-Term Market Response to Extreme Weather: Evi-
dence from Cyclone Ditwah
Cyclone Ditwah struck Sri Lanka’s eastern coast on 28
November 2025, bringing heavy flooding and landslides that
severely affected many tea growing areas 4. Looking at the
event window around the cyclone (Figure 3), both Low Grown
and High Grown mid-prices move upward into a mid-window
peak and then soften after the window closes, suggesting a
temporary event-period price pressure rather than a permanent
level shift.
Notably, the Cyclone Ditwah impact on High Grown prices
occurs quickly and fades rapidly. Even though this event-
window analysis reveals a visible short-term price adjustment
consistent with a supply shock, a single cyclone cannot
establish a generalizable pattern. Nonetheless, the directional
finding aligns with agronomic expectations and motivates
closer monitoring of extreme weather events in future auction
series as more events accumulate
B. Clean and Reproducible Tea Auction Dataset
To support reproducible forecasting, we construct a cleaned
tea auction dataset from raw PDF reports and release it via
public repositories on
 huggingfaceand
 github.
The dataset integrates sale-level, price-level, and weather
variables usingsale_idas the primary key, with rule-based
mapping between tea categories and weather regions.
The final dataset contains 12,233 records with 26 features
across 105 sales from November 2023 to March 2026. This
4https://www.aljazeera.com/news/2025/12/10/
like-wastelands-sri-lanka-tea-plantations-suffer-cyclone-ditwahs-wrath

Fig. 3. Event-window analysis of mean tea auction prices around Cyclone Ditwah (November 2025-January 2026). The shaded region denotes the primary
cyclone impact window. High-grown teas display the strongest short-term price spike.
dataset serves as a reusable research artifact, enabling repro-
ducibility and standardized analysis of Sri Lankan tea auction
data. Our
 codeis also publicly available.
VII. DISCUSSION
A. Weather Impact on Tea Prices
Weather signals were limited and catalogue-specific. Al-
though several short-lag weather–price associations were nom-
inally significant, none survived Benjamini–Hochberg correc-
tion across the extended lag family. The only robust result
emerged in the 1–8 week sensitivity analysis: Dust prices were
Granger-predicted by cumulative temperature history through
maximum lag 4 (F= 5.843,p= 0.000310,q= 0.0257;
Section V-A). This is a joint test of temperature information
across weeks 1–4, rather than an isolated fourth-week effect.
No maximum cumulative lag orders from 5 through 8 weeks
remained significant after correction.
The event-window around Cyclone Ditwah suggests a tem-
porary High Grown price adjustment. However, this single-
event pattern does not establish a generalizable weather effect
and should be interpreted as descriptive evidence for continued
monitoring of extreme-weather shocks.
The lagged-weather ablation provides modest evidence of
incremental forecasting value beyond the remaining model fea-
tures. Removing lagged weather increased out-of-fold RMSE
by5.03LKR for Low Grown,2.19LKR for Off-Grade,
and4.78LKR for Dust, while the High Grown change was
only1.10LKR. These differences are small relative to fold-
level variation and should therefore be treated as exploratory
predictive gains rather than decisive weather effects.
For Low Grown, lagged weather improved the machine-
learning model modestly, but Naive Persistence remained sub-
stantially more accurate. Thus, short-term price autocorrelation
dominates one-week-ahead Low Grown forecasting despite the
small incremental contribution of lagged weather variables.
B. Rationale for Catalogue-Specific Modeling
The tea market comprises High Grown, Low Grown, Off-
Grade, and Dust catalogues with distinct price levels and short-
term dynamics. Although the pooled model performs strongly
overall, its accuracy is influenced by the larger Low Grown
catalogue and can mask catalogue-specific behaviour.
No single method was optimal across all catalogues.
LightGBMachieved the lowest RMSE for High Grown and
Off-Grade, whileXGBoostperformed best for Dust. In con-
trast, Naive Persistence was the best method for Low Grown,
indicating that its one-week-ahead predictability is dominated
by short-term price continuity. Catalogue-specific evaluation is
therefore necessary to identify where richer machine-learning
models add value and where a simple operational baseline is
more appropriate.
The pooledLightGBMmodel remains useful for market-
level forecasting; however, it should be interpreted alongside

TABLE IV
ONE-WEEK-AHEADFORECASTPERFORMANCE: BASELINES AND
TREE-BASEDMODELS.
Catalogue Method RMSE MAE MAPE (%)R 2
High Grown
Naive Persistence 250.44 169.93 14.48−0.241
AR(1) 209.11 148.83 12.79 0.135
XGBoost 170.14 100.51 8.37 0.427
LightGBM 167.02101.64 8.490.448
Gradient Boosting 171.51 102.60 8.52 0.418
Random Forest 177.23 103.12 8.57 0.378
Low Grown
Naive Persistence 79.7634.80 1.910.990
AR(1) 80.91 38.89 2.21 0.989
XGBoost 152.31 77.52 4.15 0.962
LightGBM 145.43 74.87 4.11 0.965
Gradient Boosting 149.22 76.50 4.20 0.964
Random Forest 151.97 77.30 4.21 0.962
Off-Grade
Naive Persistence 188.39 140.64 16.76−0.664
AR(1) 145.06 121.44 14.90 0.014
XGBoost 103.83 80.60 10.00 0.495
LightGBM 102.1577.37 9.540.511
Gradient Boosting 107.33 82.17 10.18 0.460
Random Forest 104.74 81.22 10.12 0.486
Dust
Naive Persistence 241.29 187.78 18.90−0.621
AR(1) 189.31 145.17 14.76 0.002
XGBoost 114.8276.36 7.460.633
LightGBM 117.48 78.12 7.64 0.616
Gradient Boosting 119.87 85.08 8.38 0.600
Random Forest 116.18 75.37 7.36 0.624
Pooled (Unified)
Naive Persistence 176.98 106.44 9.98 0.922
AR(1) 175.33 108.68 10.17 0.923
XGBoost 142.18 83.05 6.74 0.950
LightGBM 139.1783.52 6.880.952
Gradient Boosting 141.27 89.69 7.51 0.950
Random Forest 144.97 83.09 6.74 0.948
Bold= lowest RMSE within each catalogue. Naive Persistence:ˆy t+1 =y t.
AR(1): first-order price autoregression. All metrics are computed from
combined OOF predictions across5chronological folds.
catalogue-specific results rather than as a replacement for
them.
C. Limits of One-Week-Ahead Forecasting
High Grown and Dust prices exhibit substantial week-ahead
variation driven by auction-day factors such as buyer partici-
pation, bidding behaviour, and blend-maker decisions that are
not captured in pre-auction data. Low Grown prices show
stronger week-to-week continuity; however, Naive Persistence
outperformed the machine-learning models, indicating that its
high predictability largely reflects price autocorrelation.
Future work should incorporate auction-day signals, such as
buyer activity or real-time bidding data, to improve forecasts
for High Grown and Dust catalogues.
TABLE V
LAGGEDWEATHERFEATUREABLATION ANDFOLD-LEVELRMSE
VARIABILITY.
Catalogue Full No Lag∆Fold RMSE
High Grown 167.02 168.12 +1.10160.97±49.78
Low Grown 145.43 150.47 +5.03142.48±32.58
Off-Grade 102.15 104.33 +2.19100.87±17.97
Dust 114.82 119.60 +4.78108.13±43.16
Note:Full and No Lag are combined OOF RMSE values. Positive∆
indicates lower error when lagged weather features are retained. Fold RMSE
is reported as mean±standard deviation across5chronological folds.
VIII. CONCLUSION
This study establishes that Colombo Tea Auction prices are
not a monolithic series but rather a collection of distinct mar-
ket catalogues with different price dynamics and forecasting
behaviour. Extended Granger analysis across cumulative lag
orders of 1–8 weeks identified one association that remained
significant after Benjamini–Hochberg correction: temperature
history across weeks 1–4 Granger-predicted Dust prices (F=
5.843,p= 0.000310,q= 0.0257). Other nominal weather–
price associations across Low Grown, Off-Grade, and Dust
catalogues did not survive correction and should be interpreted
as exploratory predictive signals rather than confirmed weather
effects. The Cyclone Ditwah event-window analysis further
suggests a short-lived High Grown price response, although
this single-event observation is not sufficient to establish a
generalizable extreme-weather effect.
From a forecasting perspective, performance differed across
catalogues.LightGBMachieved the lowest RMSE for High
Grown and Off-Grade, whileXGBoostperformed best for
Dust. However, Low Grown prices were forecast most accu-
rately by Naive Persistence, with an RMSE of79.76LKR
and anR 2 of0.9896. This indicates that strong short-term
price autocorrelation, rather than the current richer feature set,
dominates one-week-ahead Low Grown forecasting.
Lagged-weather ablation showed modest incremental fore-
casting gains for Low Grown, Off-Grade, and Dust, but little
benefit for High Grown; these gains should be interpreted
cautiously given fold-level variability.
In the pooled setting,LightGBMranked first with an
RMSE of139.17LKR and anR 2 of0.9516, improving on
Naive Persistence by21.36%in RMSE. These results support
catalogue-specific evaluation and the practical use of simple
baselines alongside machine-learning models.
REFERENCES
[1] Sri Lanka Tea Board,Annual Report 2024. Colombo, Sri Lanka: Sri
Lanka Tea Board, 2024, accessed: 2026-06-27.
[2] K. B. A. Pasandul, R. V . Pathirana, S. S. Chandrasinghe, H. A. B. S.
Mahanama, and G. Pereraa, “Tea price trend analysis and forecasting in
Sri Lanka: A time series approach,” inTransformative Applied Research.
CRC Press, 2026, pp. 228–233.
[3] C. W. J. Granger, “Investigating causal relations by econometric models
and cross-spectral methods,”Econometrica, vol. 37, no. 3, pp. 424–438,
1969.

[4] S. Aslan and H. Ombao, “A practical approach for exploring Granger
connectivity in high-dimensional networks of time series,”arXiv preprint
arXiv:2406.02360, 2024.
[5] M. W. A. De Silva and N. S. Cooray, “The export performance of the Sri
Lankan tea: An econometric analysis,”International Journal of Research
and Innovation in Social Science, vol. 6, no. 4, pp. 224–227, 2022.
[6] B. A. T. K. Rupasinghe and S. H. P. Malkanthi, “An investigation of the
relationship between exchange rate volatility and volume of tea export in
Sri Lanka,” Faculty of Social Sciences and Languages, Sabaragamuwa
University of Sri Lanka, Tech. Rep., 2023.
[7] S. Chaundry, Y . Negi, and R. K. Shukla, “A time series analysis of
auction prices of Indian tea,”International Journal of Research in
Economics and Social Sciences, vol. 7, no. 6, pp. 100–111, 2017.
[8] M. R. L. Manogna and A. K. Mishra, “Forecasting spot prices of
agricultural commodities in India: Application of deep-learning models,”
Intelligent Systems in Accounting, Finance and Management, vol. 28,
no. 1, pp. 72–83, 2021.
[9] M. A. Wijeratne, “Vulnerability of Sri Lanka tea production to global
climate change,”Water, Air, and Soil Pollution, vol. 92, no. 1, pp. 87–94,
1996.
[10] S. Ahmed, T. Griffin, S. B. Cash, W.-Y . Han, C. Matyas, C. Long, C. M.
Orians, J. R. Stepp, A. Robbat, and D. Xue, “Global climate change,
ecological stress, and tea production,” inStress Physiology of Tea in the
Face of Climate Change. Cham, Switzerland: Springer, 2018, pp. 1–23.
[11] P. Zippenfenig, “Open-Meteo.com weather API,” Zenodo. https://doi.
org/10.5281/zenodo.14582479, Dec. 2024.
[12] V . Verma, “A review of the Benjamini–Hochberg method for multiple
hypothesis testing,”International Journal of Research, vol. 1, no. 6, pp.
775–784, 2014.
[13] L. Breiman, “Random forests,”Machine Learning, vol. 45, no. 1, pp.
5–32, 2001.
[14] J. H. Friedman, “Greedy function approximation: A gradient boosting
machine,”Annals of Statistics, vol. 29, no. 5, pp. 1189–1232, 2001.
[15] T. Chen and C. Guestrin, “XGBoost: A scalable tree boosting system,”
inProc. 22nd ACM SIGKDD Int. Conf. Knowledge Discovery and Data
Mining, 2016, pp. 785–794.
[16] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye, and T.-Y .
Liu, “LightGBM: A highly efficient gradient boosting decision tree,” in
Advances in Neural Information Processing Systems, vol. 30, 2017.
[17] F. Pedregosa, G. Varoquaux, A. Gramfort, V . Michel, B. Thirion,
O. Grisel, M. Blondel, P. Prettenhofer, R. Weiss, V . Dubourget al.,
“Scikit-learn: Machine learning in Python,”Journal of Machine Learn-
ing Research, vol. 12, pp. 2825–2830, 2011.
