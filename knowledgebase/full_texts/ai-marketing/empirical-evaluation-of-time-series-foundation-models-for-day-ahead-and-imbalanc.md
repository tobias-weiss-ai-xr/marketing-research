---
title: Empirical evaluation of Time Series Foundation Models for Day-ahead and Imbalance Electricity Price
  Forecasting in Belgium
url: https://arxiv.org/abs/2605.17045
category: ai-marketing
subcategory: measurement
date: 2026-05
venue: ''
authors:
- Chi Bui
- Maria Margarida Mascarenhas
- Arnaud Verstraeten
- Hussain Kazmi
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.17045
pages: 6
chars: 28144
fetched_at: '2026-11-08T13:26:33+00:00'
kb_version: 1
---

# Empirical evaluation of Time Series Foundation Models for Day-ahead and Imbalance Electricity Price Forecasting in Belgium

Empirical evaluation of Time Series Foundation
Models for Day-ahead and Imbalance Electricity
Price Forecasting in Belgium
Chi Bui
ELECTA-ESAT (KU Leuven)
Leuven, Belgium
thimaichi.bui@student.kuleuven.be
Maria Margarida Mascarenhas
ELECTA-ESAT (KU Leuven)
Leuven, Belgium
margarida.mascarenhas@kuleuven.be
Hussain Kazmi
ELECTA-ESAT (KU Leuven)
Leuven, Belgium
hussain.kazmi@kuleuven.be
Arnaud Verstraeten
ELECTA-ESAT(KU Leuven) and Gridual
Leuven, Belgium
arnaud.verstraeten@kuleuven.be
Abstract—Recent advances in Time Series Foundation Models
(TSFMs) promise zero-shot forecasting capabilities with minimal
task-specific training. While these models have shown strong
performance across generic benchmarks, their applicability in
volatile, complex electricity markets remains underexplored.
Addressing this gap, this study provides a systematic empirical
evaluation of several TSFMs, specifically Chronos-2 and Chronos-
Bolt (developed by Amazon), and TimesFM 2.5 (provided by
Google), for forecasting Belgian day-ahead and imbalance elec-
tricity prices. For both considered markets, Chronos-2 in ARX
mode produces the most accurate forecasts. Compared with the
best ensemble prediction from other machine learning methods,
Chronos-2’s Mean Absolute Error (MAE) is 5% lower for the
day-ahead market. In contrast, the model yields 10% higher
MAE predicting imbalance prices across all forecast horizons,
except for the two-hour-ahead horizon. Moreover, we find that
TSFMs exhibit genuine zero-shot forecasting skills but still
struggle under extreme market conditions.
Index Terms—Time Series Foundation Model, electricity price
forecasting, day-ahead markets, imbalance markets
I. INTRODUCTION
In Belgium, more than a quarter of national electricity
consumption is traded on the day-ahead market (DAM), where
prices are set for the next day’s delivery. The imbalance market
(IMB) penalizes deviations from the DAM nominations. His-
torically, imbalance prices have exhibited higher volatility than
DAM prices due to market design and trading time granularity,
which creates higher opportunities for trading and arbitrage.
These differences introduce distinct forecasting challenges for
each market.
Complex forecasting models, such as ensembles of deep
neural networks and regularized linear models, have shown
cutting-edge performance in both day-ahead and imbalance
markets [1], but they often entail high computational costs
Hussain Kazmi acknowledges support from the CELSA PREDDICT
project. Margarida Mascarenhas acknowledges support from 1S39625N.
and require substantial engineering for maintenance, especially
when faced with different bidding zones and non-stationarities.
Furthermore, while day-ahead price forecasting is a well-
established field, imbalance price forecasting is not yet at the
same stage of development.
Time Series Foundation Models (TSFMs), often developed
using transformer-based architectures, offer a universal fore-
casting framework alternative with minimal tuning require-
ments. In fact, TSFMs claim to leverage cross-domain pre-
training for zero-shot forecasting, reduce model training effort,
and improve adaptability. As such, they provide an interesting
alternative to building specialised forecast models for each
individual market and bidding zone. However, in practice,
there is still a lack of systematic evaluation of whether such
TSFMs can be used in the dynamic conditions seen in different
electricity markets, especially under extreme volatility.
This study evaluates the performance of such TSFMs for
the Belgian DAM and IMB markets, benchmarking against
state-of-the-art ensemble-based baselines.
II. FORECASTING IN ELECTRICITY MARKETS
A. Day-ahead market
The day-ahead market is the primary short-term electricity
market in Europe. In this market, participants submit bids and
offers for electricity delivery for each hour of the following
day. The market is cleared through a price auction in which
supply and demand curves are aggregated across participating
bidding zones. The resulting market-clearing price determines
the electricity price for each delivery hour of the next day.
Most European countries, including Belgium, participate in
the Single Day-Ahead Coupling (SDAC) operated through
the EPEX SPOT exchange. The gate-closure time for the
day-ahead market is 12:00 p.m. CET. Prior to this deadline,
market participants must forecast electricity prices in order
to support bidding strategies, portfolio optimization, and risk
arXiv:2605.17045v1  [eess.SY]  16 May 2026

management. Day-ahead electricity price forecasting has been
extensively studied. Comprehensive overviews of electricity
price forecasting methods and evaluation practices are pro-
vided by Weron [2] and, more specifically, for day-ahead
markets, by Lagoet al.[3], [4].
B. Imbalance market
After the closure of day-ahead and intraday markets, balance
responsible parties (BRPs) should ensure that their portfo-
lio balance is in accordance with nominated volumes. Any
deviations from the planned schedule are registered by the
transmission system operator (TSO), and they are penalized or
remunerated based on the imbalance price. In most European
countries (including Belgium), the imbalance settlement period
is equal to 15 minutes. As the sign of the collective system
imbalance determines the need for upward or downward
regulation volumes, the imbalance price can fluctuate strongly
depending on the balancing state of the system. In addition,
the system imbalance can be difficult to predict due to the
uncertain output of variable renewables, which in turn leads
to volatile imbalance prices. In the literature, there are two
main approaches to forecasting imbalance prices. The first
approach is to use a fundamental forecasting method based on
the balancing regime, such as in [5], [6]. Another forecasting
approach is to use data-driven machine learning models such
as gradient boosting or neural networks [7]–[9].
C. TSFMs in electricity markets
According to the technical reports introducing Amazon’s
Chronos [10] and Google’s TimesFM [11], such TSFMs have
demonstrated strong zero-shot forecasting performance across
a wide range of public benchmark datasets. These evaluations
include datasets from multiple domains, such as retail demand,
financial time series, and energy-related datasets, including
Australian Electricity Demand, ETT (Electricity Transformer
Temperature), and ERCOT Load. A recent study conducted by
Timoth´ee et al. [12] investigated the forecasting performance
of TSFMs for DAM across multiple European bidding zones.
Although this work provides valuable insights into the poten-
tial of foundation models for the electricity price forecasting
task, the analysis focuses primarily on day-ahead markets. In
contrast, imbalance markets have received considerably less
attention in the forecasting literature despite their importance
for real-time system balancing and trading strategies. To our
best knowledge, no existing study has systematically evaluated
the performance of TSFMs for imbalance price forecasting.
This work aims to bridge these research gaps by providing an
empirical evaluation of TSFMs for both the Belgian DAM
and IMB market. By comparing zero-shot forecasts from
prominent TSFMs with state-of-the-art baselines, we provide
insights into the practical applicability of TSFMs in electricity
market forecasting.
III. METHODOLOGY
This section describes the forecasting framework used to
evaluate the performance of TSFMs relative to traditional
forecast approaches. For each market, the models produce
point forecasts for fixed horizons that align with the market’s
operational requirements. In the day-ahead market, the fore-
casting horizon consists of the 24 hourly prices of the next
day. In the imbalance market, forecasts are generated for the
next eight 15-minute settlement periods, corresponding to a
two-hour horizon.
A. Baseline models
For the day-ahead market, a weekly persistence model is
used. The forecasted price for each hour of the next day is
equal to the observed price from the same hour one week
earlier. For the imbalance market, two different naive models
are used. The persistence model predicts the most recent
imbalance price for the full forecast horizon. The second
naive model uses the day-ahead price as the imbalance price
forecast.
B. Baseline data-driven models
In addition to naive benchmarks, two state-of-the-art data-
driven forecasting models are considered: the Lasso-enhanced
AutoRegressive (LEAR) model and a Deep Neural Network
(DNN) model. The LEAR model is a linear autoregressive
model with Lasso regularization. Due to its linear structure, the
LEAR model is computationally efficient and offers a higher
degree of interpretability compared with the DNN model,
which is a nonlinear alternative capable of learning more
complex relationships between input variables and electricity
prices.
Both models are trained using a rolling calibration win-
dow of one year and are periodically recalibrated to account
for evolving market dynamics. Furthermore, both models
incorporate feature selection mechanisms. The LEAR model
performs feature selection implicitly through regularization,
while the DNN model includes feature selection as part of the
hyperparameter optimization process. Prior to inference, the
DNN model undergoes hyperparameter optimization over the
search space presented in Table VI. More detailed descriptions
of these models and their forecasting performance in electricity
markets can be found in [3], [13]. In addition, model forecast
ensembles are used to construct baseline results, as ensembling
is a well-established way to improve forecasting performance
[2]. Here, we simply average the forecasts from individual
models to produce the ensemble forecast.
C. TSFMs
TSFMs are large models with transformer architectures
and millions of parameters, similar to large language mod-
els (LLMs) but for the time-series domain. These models
are claimed to offer a universal forecasting framework with
minimal tuning requirements. TSFMs can be categorized into
Pre-trained and LLM-based models [14], [15]. While LLM-
based models aim to adapt existing large language model ar-
chitectures for time series forecasting tasks, pre-trained models
are trained on diverse, multi-domain time series datasets. This
study’s scope is restricted to pre-trained models.

Pre-trained TSFMs utilize various techniques to transform
time points intotokensthat form input layers, which are
then trained as LLMs. Moreover, in zero-shot inference,con-
text lengthcontrols how far back into the past values that
foundation models have accessed to and perform attention
mechanism, and can be considered to be equivalent to max-
imum lag order in traditional time series analysis. We use
two inference modes: AR (univariate, using only historical
target data) and ARX (multivariate, incorporating cointegrated
time series) from two librarieschronos-forecasting
andtimesfm. The ARX mode is implemented only for the
Chronos-2 model.
a) Chronos (Amazon):Chronos was first introduced in
2024 with two main variants, i.e, Chronos (original variant)
and Chronos-bolt (fast inference variant), each having its own
derivatives based on model size. In this study, we chose to
experiment with two representative models for each variant,
Chronos-2 and Chronos-bolt (base), having 120M and 205M
parameters, respectively. Standard encoder-decoder architec-
ture is employed for building Chronos-bolt while Chronos-2
adopts encoder-only design.
A key innovation in Chronos is the transformation of con-
tinuous time series into discrete token sequences by applying
quantization to map numerical values to discrete bins defined
by learned or fixed scaling rules [10], [16]. This discretization
enables the model to treat time-series forecasting as a language
modeling problem, predicting the next token given previous
tokens. After inference, tokens are mapped back to numerical
values through inverse scaling.
b) TimesFM (Google):Google’s TimesFM is among the
pioneering models in this emerging research of TSFMs, with
TimesFM 1.0 introduced in early 2024. In this study, we
use the latest release, TimesFM 2.5 (2025), which contains
approximately 200 million parameters and offers improved
documentation and ease of implementation. Unlike Chronos,
TimesFM adopts decoder-only architecture and forms tokens
by grouping temporally adjacent time steps regardless of their
numerical magnitude.
D. Input features
Table I contains the input features used in the forecasting
models. For day-ahead price forecasting, the input covariates
include lagged electricity prices (autoregressive component)
from the previous two days and the previous week, lagged
exogenous variables from the previous day and the previous
week, as well as for the day being forecasted, and calendar
features (a holiday dummy variable and dummy variables for
the day of the week).
In the case of imbalance price forecasting, the inputs include
lagged imbalance prices and system imbalance values from the
past hour, and past and future day-ahead prices. The lookahead
for future input information is the same as the forecast horizon,
which is equal to two hours.
E. Evaluation metrics
We use Mean Absolute Error (MAE) and Root Mean
Squared Error (RMSE) to evaluate the accuracy of the fore-
TABLE I: Input features used in day-ahead and imbalance
price forecasting
Data Frequency Unit Forecast
DAM price Hourly EUR/MWh DAM, IMB
Wind generation forecast Hourly MW DAM
Day-ahead load forecast Hourly MW DAM
Solar generation forecast Hourly MW DAM
Humidity forecast Hourly % DAM
Temperature forecast Hourly °C DAM
Imbalance price 15 minutes EUR/MWh IMB
System imbalance 15 minutes MW IMB
casts, which are common metrics used in electricity price
forecasting literature. [2], [3], [4], [13].
MAE=
PT
t=1 |ˆyt −y t|
T (Unit: EUR/MWh) (1)
RMSE=
s PT
t=1 (ˆyt −y t)2
T (Unit: EUR/MWh) (2)
wherey t is the true value andˆy t is the predicted value.
Lower values of MAE and RMSE are desWe use Mean
Absolute Error (MAE) and Root Mean Squared Error (RMSE)
to evaluate the accuracy of the forecasts, which are common
metrics used in electricity price forecasting literature. [2], [3],
[4], [13].
MAE=
PT
t=1 |ˆyt −y t|
T (Unit: EUR/MWh) (3)
RMSE=
s PT
t=1 (ˆyt −y t)2
T (Unit: EUR/MWh) (4)
wherey t is the true value andˆyt is the predicted value. Lower
values of MAE and RMSE are desirable as shows better
approximate between predictions and true values. However,
these metric are prone to outliers. irable as shows better
approximate between predictions and true values. However,
these metric are prone to outliers.
IV. EXPERIMENTS ANDRESULTS
A. Case study setup
For the Belgian day-ahead market, year 2023 is used for
initial calibration and 2024 is used as the out-of-sample test
year; during testing, the one-year calibration window is rolled
forward day-by-day while keeping its length fixed. For the
Belgian imbalance market, 2022 is used for initial calibra-
tion, and 2023 is used as the out-of-sample test year, with
the same fixed-length rolling-window procedure and monthly
recalibration. The time period under consideration has been
cross-checked with the list of disclosed pretrained datasets that
all tested TSFMs were trained on to avoid the well-known
data leakage problem of TSFMs. A high-level summary of
the time series used in the analysis is included in Table I.
Different context length configurations for TSFMs have been
experimented with, and the best performance is reported, to be
specific, 8192 hours of context (almost one year) are used for

Chronos-2 and Chronos-bolt in DAM, and 2048 quarter-hours
(approximately 1 month) for IMB forecast, while TimesFM
uses a context length of 1024 hours in both markets.
B. F orecast accuracy
TABLE II: Forecast MAE for naive persistent model, data -
driven models, TSFMs and their ensembles in DAM and three
horizons in IMB market
Market DAM IMB
QH1 QH4 QH8
Persistent model 28.22 76.8 104.68 124.57
Chronos-bolt 16.03 75.42 92.44 97.8
Chronos 2 - AR 15.61 72.91 90.3 95.43
Chronos 2 - ARX 12.43 70.1 87.73 93.72
TimesFM 2.5 16.95 74.39 92.15 97.78
TSFMs Ensemble 14.43 72.12 89.58 95.13
LEAR 13.74 68.74 88.01 94.71
DNN 14.39 68.69 87.87 95.13
ML Ensemble 13.22 67.19 87.3 93.96
Chronos 2 & ML 12.3 67.09 86.45 92.83
TABLE III: Forecast RMSE for naive persistent model, data -
driven models, TSFMs and their ensembles in DAM and three
horizons IMB market
Model DAM IMB
QH1 QH4 QH8
Persistent model 40.99 130.81 162.45 183.96
Chronos-bolt 24 114.21 132.48 138.27
Chronos 2 - AR 23.27 115.08 132.3 137.52
Chronos 2 - ARX 19.36 110.77 130.35 136.61
TimesFM 2.5 25.07 113.86 133.55 139.68
TSFMs Ensemble 21.74 111.17 130.2 136.18
LEAR 20.38 105.58 126.26 133.36
DNN 20.98 108.32 128.87 136.61
ML Ensemble 19.72 104.15 126.19 133.52
Chronos 2 & ML 18.91 104.3 126.05 132.98
The MAE and RMSE for day-ahead price forecasts and
selected quarter-hour imbalance price forecasts are summa-
rized in Tables II and III. These two metrics are expressed
in EUR/MWh, enabling direct comparison to the average
DAM price (73.38 EUR/MWh in 2024) and IMB price (96.72
EUR/MWh in 2023). Overall, among TSFMs, Chronos-2 in
ARX mode produced the most accurate forecasts for both
DAM and IMB prices. It is also worth noting that combining
forecasts from all TSFMs yields worse results than individual
Chronos-2 (ARX mode) forecasts for both markets, due to
high correlation among TSFMs forecasts seen in Figures 1
and 2.
Regarding DAM, when using Chronos-2 with covariates,
errors are reduced significantly, in particular, 20% smaller than
AR mode, and even slightly improved in relative to trained and
calibrated LEAR and DNN models with exactly the same set
of features, indicating the acclaimed outstanding capabilities
Fig. 1: DAM: TSFMs forecasts vs. Actual prices
of the model on leveraging covariates inputs. When combining
forecasts from Chronos-2 and baseline data-driven models
(LEAR and DNN) were we able to achieve negligibly lower
MAE and RMSE of 12.29 EUR/MWh and 18.91 EUR/MWh,
respectively. However, conducting the Diebold-Mariano test
between the Chronos-2 & ML ensemble, and the ML ensemble
reveals that the improvement is not significant.
Fig. 2: IMB: TSFMs forecasts vs. Actual prices
Regarding IMB, as shown in Figure 3, TSFMs outperformed
the naive persistent model across all quarter hours. Except
for Chronos-bolt and TimesFM for horizons from 5 to 8
quarter-hour, other TSFMs setups also surpass naive model
of predicting Day-ahead price across all forecast horizon.
However, when being benchmarked against trained data-driven
models, only Chronos-2 in ARX mode outperformed at longer
forecast horizons, i.e., the eighth quarter hour (as per Table
II and III). It is also clear that when combining forecasts

from Chronos-2 in ARX mode with ML baseline models,
the ensemble yields slightly more accurate forecasts than the
ML ensemble alone, as evidenced by lower MAE and RMSE
across all forecast horizons.
Fig. 3: IMB: MAE of different models across all forecast
horizons
C. Errors Analysis
a) DAM:To analyze how each model performs across
different market conditions, we report its accuracy for 1, 5,
and 10 DAM price deciles in Table IV. Alhough Chronos-
2 in ARX mode outperformed ensemble forecasts of data-
driven models in terms of accuracy evaluated for the test year,
the model struggles in unfavorable occasions - 1st and 10th
decile. The Chronos-2 & ML combination consistently yields
lower MAE and RMSE across all price deciles compared to
individual models, indicating their potential use of Chronos-2
in combination with currently operating models in predicting
DAM prices under extreme market conditions, eventually
benefiting risk-aware strategic planning.
TABLE IV: Accuracy across price deciles in DAM
Metrics MAE RMSE
Model/ Decile 1 5 10 1 5 10
Chronos-bolt 24.16 12.34 26.51 32.36 16.59 44.07
Chronos 2 - AR 23.42 12.03 26.11 31.43 16.23 42.87
Chronos 2 - ARX 19.36 9.08 21.28 25.29 12.01 39.06
TimesFM 2.5 24.27 12.96 28.24 31.34 18.01 45.41
TSFMs Ensemble 21.93 10.97 24.60 28.97 14.72 41.31
LEAR 19.78 10.78 22.25 25.71 14.13 39.42
DNN 20.01 10.87 23.15 25.99 14.58 39.19
ML Ensemble 19.17 10.03 21.8 24.81 13.37 38.24
Chronos-2 & ML 18.84 9.15 20.86 24.4 12 38
b) IMB:Similar to what has been done with IMB, we
also segregate imbalance price into deciles and analyze the
MAE of each model’s forecasts for the price’s 10th and 90th
percentiles with forecast horizons of 1, 4, and 8 quarter hours
(Table V). TSFMs clearly struggle under extreme conditions,
among which only Chronos-2 outperformed all models for the
8th quarter-hour forecast.
TABLE V: MAE for IMB forecasts under extreme conditions
Model 1st Decile 10th Decile
QH1 QH4 QH8 QH1 QH4 QH8
Chronos-bolt 173.8 228.9 250.5 108.9 161.1 176.9
Chronos 2 - AR 162.5 220.9 240.5 100.6 153.6 174.2
Chronos 2 - ARX 164.8 213.9 235.3 101.7 155.4 177.5
TimesFM 2.5 171.1 229.5 250.5 106.4 160.5 178.4
TSFMs Ensemble 167.1 222.7 244.04 103.6 157.2 176.5
LEAR 155.1 205.9 232.9 81.0 152.4 181.8
DNN 167.5 211.5 237.4 78.7 146.4 173.9
ML Ensemble 160.8 208.6 234.0 81.2 152.1 179.5
Chronos-2 & ML 161.9 210.7 234.3 88.5 153 178.1
V. CONCLUSION
This study presents an empirical evaluation of the zero-
shot forecasting capabilities of Time Series Foundation Models
(TSFMs) in the Belgian day-ahead (DAM) and imbalance
(IMB) electricity markets. The results show that, by operating
in ARX mode, Chronos-2 was able to utilize covariates and
even outperformed both naive and data-driven baselines, as
well as their ensemble forecasts, for DAM. Moving forward,
the underlying reasons for this impressive improvement in
predictive accuracy pose an intriguing question, where an in-
depth dive into model architecture and pre-trained datasets is
necessary to inspect how covariate information is used and
to avoid any data leakage problems. Furthermore, combining
TSFMs’ forecasts with data-driven models improves predictive
power for both DAM and IMB prices over a one-year test
period, suggesting that TSFMs can serve as a valuable comple-
mentary component in ensemble forecasting frameworks, even
though further consideration is needed for handling extreme
price markets. In addition to forecasting accuracy, TSFMs of-
fer practical advantages in terms of scalability and operational
efficiency, as they require minimal feature engineering and no
model retraining. These characteristics make them promising
tools for rapid deployment across multiple electricity markets
and bidding zones.
REFERENCES
[1] J. Lago, G. Marcjasz, B. D. Schutter, and R. Weron, “Forecasting
day-ahead electricity prices: A review of state-of-the-art algorithms,
best practices and an open-access benchmark,”Applied Energy, vol.
293, p. 116983, 7 2021. [Online]. Available: https://www.sciencedirect.
com/science/article/pii/S0306261921004529
[2] R. Weron, “Electricity price forecasting: A review of the state-
of-the-art with a look into the future,”International Journal of
F orecasting, vol. 30, no. 4, pp. 1030–1081, 2014. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S0169207014001083
[3] J. Lago, G. Marcjasz, B. De Schutter, and R. Weron, “Forecasting
day-ahead electricity prices: A review of state-of-the-art algorithms,
best practices and an open-access benchmark,”Applied Energy, vol.
293, p. 116983, 2021. [Online]. Available: https://www.sciencedirect.
com/science/article/pii/S0306261921004529
[4] J. Lago, F. De Ridder, and B. De Schutter, “Forecasting spot
electricity prices: Deep learning approaches and empirical comparison
of traditional algorithms,”Applied Energy, vol. 221, pp. 386–405, 2018.
[Online]. Available: https://www.sciencedirect.com/science/article/pii/
S030626191830196X

[5] D. W. Bunn, J. N. Inekwe, and D. MacGeehan, “Analysis of the
Fundamental Predictability of Prices in the British Balancing Market,”
IEEE Transactions on Power Systems, vol. 36, no. 2, pp. 1309–1316,
Mar. 2021.
[6] J. Dumas, I. Boukas, M. M. de Villena, S. Mathieu, and B. Corn ´elusse,
“Probabilistic Forecasting of Imbalance Prices in the Belgian Context,”
in2019 16th International Conference on the European Energy Market
(EEM), Sep. 2019, pp. 1–7.
[7] V . N. Ganesh and D. W. Bunn, “Forecasting Imbalance Price Densities
With Statistical Methods and Neural Networks,”Policy and Regulation
IEEE Transactions on Energy Markets, vol. 2, no. 1, pp. 30–39, Mar.
2024.
[8] J. Bottieau, Y . Wang, Z. De Greve, F. Vallee, and J.-F. Toubeau,
“Interpretable transformer model for capturing regime switching effects
of real-time electricity prices,”IEEE Transactions on Power Systems,
vol. 38, no. 3, pp. 2162–2176, 2022.
[9] S. Deng, J. Inekwe, V . Smirnov, A. Wait, and C. Wang, “Seasonality
in deep learning forecasts of electricity imbalance prices,”Energy
Economics, vol. 137, p. 107770, Sep. 2024.
[10] A. F. Ansari, L. Stella, A. C. Turkmen, X. Zhang, P. Mercado, H. Shen,
O. Shchur, S. S. Rangapuram, S. P. Arango, S. Kapoor, J. Zschiegner,
D. C. Maddix, H. Wang, M. W. Mahoney, K. Torkkola, A. G. Wilson,
M. Bohlke-Schneider, and B. Wang, “Chronos: Learning the language
of time series,”Transactions on Machine Learning Research, 2024.
[Online]. Available: https://openreview.net/forum?id=gerNCVqqtR
[11] A. Das, W. Kong, R. Sen, and Y . Zhou, “A decoder-only foundation
model for time-series forecasting,” inProceedings of the 41st Interna-
tional Conference on Machine Learning, ser. ICML’24. JMLR.org,
2024.
[12] T. Hornek, A. Sartipi, I. Tchappi, and G. Fridgen, “Benchmarking pre-
trained time series models for electricity price forecasting,” in2025 21st
International Conference on the European Energy Market (EEM), 2025,
pp. 1–7.
[13] M. M. Mascarenhas, J. De Blauwe, M. Amelin, and H. Kazmi,
“Leveraging asynchronous cross-border market data for improved
day-ahead electricity price forecasting in european markets,”Applied
Energy, vol. 404, p. 127077, 2026. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S0306261925018070
[14] Y . Liang, H. Wen, Y . Nie, Y . Jiang, M. Jin, D. Song, S. Pan, and
Q. Wen, “Foundation models for time series analysis: A tutorial and
survey,” inProceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, ser. KDD ’24. New York,
NY , USA: Association for Computing Machinery, 2024, p. 6555–6565.
[Online]. Available: https://doi.org/10.1145/3637528.3671451
[15] Z. Li, X. Qiu, P. Chen, Y . Wang, H. Cheng, Y . Shu, J. Hu, C. Guo,
A. Zhou, C. S. Jensen, and B. Yang, “Tsfm-bench: A comprehensive and
unified benchmark of foundation models for time series forecasting,”
inProceedings of the 31st ACM SIGKDD Conference on Knowledge
Discovery and Data Mining V .2, ser. KDD ’25. New York, NY , USA:
Association for Computing Machinery, 2025, p. 5595–5606. [Online].
Available: https://doi.org/10.1145/3711896.3737442
[16] A. F. Ansari, O. Shchur, J. K ¨uken, A. Auer, B. Han, P. Mercado, S. S.
Rangapuram, H. Shen, L. Stella, X. Zhang, M. Goswami, S. Kapoor,
D. C. Maddix, P. Guerron, T. Hu, J. Yin, N. Erickson, P. M. Desai,
H. Wang, H. Rangwala, G. Karypis, Y . Wang, and M. Bohlke-Schneider,
“Chronos-2: From univariate to universal forecasting,” 2025. [Online].
Available: https://arxiv.org/abs/2510.15821
APPENDIX
TABLE VI: Hyperparameter search space for the DNN model.
Parameter Search space
Neurons (layer 1)[50,500]
Neurons (layer 2)[25,400]
Dropout[0,1](uniform)
Batch normalization{True, False}
Regularization{None, L1}
L1 penaltyλ[10 −5,1](log-uniform)
Learning rate[5×10 −4,0.1](log-uniform)
Random seed[1,1000]
Activation function{ReLU, Softplus, Tanh, SELU,
LeakyReLU, PReLU, Sigmoid}
Weight initialization{Orthogonal, Lecun-uniform,
Glorot-uniform, Glorot-normal,
He-uniform, He-normal}
ScaleX{None, Norm, Norm1}
ScaleY{None, Norm, Norm1}
Day-of-week dummy{True, False}
Holiday dummy{True, False}
Price lagD−1{True, False}
Price lagD−2{True, False}
Price lagD−3{True, False}
Price lagD−7{True, False}
Exogenous variablei(D){True, False}
Exogenous variablei(D−1){True, False}
Exogenous variablei(D−7){True, False}
