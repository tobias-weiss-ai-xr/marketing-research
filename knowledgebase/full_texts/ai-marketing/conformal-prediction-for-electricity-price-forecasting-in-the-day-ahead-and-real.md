---
title: Conformal Prediction for Electricity Price Forecasting in the Day-Ahead and Real-Time Balancing
  Market
url: https://arxiv.org/abs/2502.04935
category: ai-marketing
subcategory: empirical
date: 2025-02
venue: ''
authors:
- Ciaran O'Connor
- Mohamed Bahloul
- Roberto Rossi
- Steven Prestwich
- Andrea Visentin
source: arxiv
pdf_url: https://arxiv.org/pdf/2502.04935
pages: 41
chars: 70141
fetched_at: '2026-11-08T13:19:06+00:00'
kb_version: 1
---

# Conformal Prediction for Electricity Price Forecasting in the Day-Ahead and Real-Time Balancing Market

Conformal Prediction for Electricity Price Forecasting in
the Day-Ahead and Real-Time Balancing Market
Ciaran O’Connor
SFI CRT in Artificial Intelligence, School of Computer Science & IT, University College
Cork, Ireland
Mohamed Bahloul
International Energy Research Centre, Tyndall National Institute, Cork, Ireland
Roberto Rossi
Business School, University of Edinburgh, Edinburgh, UK
Steven Prestwich, Andrea Visentin
SFI Insight Centre for Data Analytics, School of Computer Science & IT, University
College Cork, Ireland
Abstract
The integration of renewable energy into electricity markets poses significant
challenges to price stability and increases the complexity of market operations.
Accurate and reliable electricity price forecasting is crucial for effective market
participation, where price dynamics can be significantly more challenging to
predict. Probabilistic forecasting, through prediction intervals, efficiently quan-
tifies the inherent uncertainties in electricity prices, supporting better decision-
making for market participants. This study explores the enhancement of prob-
abilistic price prediction using Conformal Prediction (CP) techniques, specifi-
cally Ensemble Batch Prediction Intervals and Sequential Predictive Conformal
Inference. These methods provide precise and reliable prediction intervals, out-
performing traditional models in validity metrics. We propose an ensemble
approach that combines the efficiency of quantile regression models with the
Email addresses: 119226305@umail.ucc.ie (Ciaran O’Connor),
mohamed.bahloul@ierc.ie (Mohamed Bahloul), roberto.rossi@ed.ac.uk (Roberto Rossi),
s.prestwich@cs.ucc.ie, andrea.visentin@ucc.ie (Steven Prestwich, Andrea Visentin)
Preprint submitted to a Journal Monday 10 th February, 2025
arXiv:2502.04935v1  [cs.LG]  7 Feb 2025

robust coverage properties of time series adapted CP techniques. This ensemble
delivers both narrow prediction intervals and high coverage, leading to more re-
liable and accurate forecasts. We further evaluate the practical implications of
CP techniques through a simulated trading algorithm applied to a battery stor-
age system. The ensemble approach demonstrates improved financial returns in
energy trading in both the Day-Ahead and Balancing Markets, highlighting its
practical benefits for market participants.
Keywords: Probabilistic Electricity Price Forecasting, Conformal Prediction,
Arbitrage Trading, Machine Learning
1. Introduction
Electricity Price Forecasting (EPF) is particularly challenging due to mar-
ket volatility, sudden price fluctuations, and seasonal demand shifts. Accurate
EPF is essential for all market participants in deregulated markets, providing a
foundation for informed decision-making and financial planning. Power genera-
tion companies rely on forecasts to hedge against risks from deviations between
day-ahead and real-time markets, thereby stabilising revenue streams and oper-
ational planning. Load-serving utilities use forecasts to secure energy at lower
prices, optimising procurement strategies and ensuring cost-effective supply for
consumers. Virtual traders, lacking actual generation power or load require-
ments, depend on EPF to estimate price spreads between spot and forward
markets, exploiting arbitrage opportunities to generate profits. The increasing
integration of renewable energy sources and the advent of smart grids further
complicate EPF, exacerbating market volatility.
Spot markets such as the Day-Ahead Market (DAM), Intra-Day Market
(IDM), and Balancing Market (BM) are crucial for maintaining grid stability.
Yet, increasing market price volatility, driven by forecast errors in renewable
electricity generation, presents significant challenges Ortner & Totschnig (2019).
This underscores the critical importance of accurate forecasting in stabilising
energy production planning, optimising trading strategies, and implementing
2

risk-aware policies to ensure a reliable, cost-effective, and sustainable energy
supply. Accurate EPF supports market participants’ financial health and plays
an important role in advancing energy policy goals surrounding renewable inte-
gration, grid stability, and reducing carbon emissions.
There are two major EPF schemes: point forecasts and probabilistic fore-
casts. Point forecasts provide single price predictions that are easy to interpret
and establish parsimonious predictor-target relationships under the assumption
of homoscedasticity. However, they cannot quantify uncertainties, as they typi-
cally link predictors to target values using the conditional mean function. Thus,
a critical evolution in EPF has been the transition from traditional point fore-
casts to probabilistic forecasts which offer a range of potential outcomes, quanti-
fying uncertainty, and generating prediction intervals (PIs) that reflect the con-
fidence levels of forecasts. Probabilistic Electricity Price Forecasting (PEPF)
can capture the full range of potential future prices in dynamic, non-linear mar-
kets Nowotarski & Weron (2018); Ziel & Steinert (2018) addressing uncertainties
in smart grids, supply-demand dynamics, and price variations emphasising the
operational impact of forecasts Khajeh & Laaksonen (2022).
Key methods in probabilistic forecasting include Quantile Regression (QR),
Quantile Regression Averaging (QRA), Bayesian, Historical Simulation, and
Bootstrapped PIs. However, these methods fail to consistently provide validity,
particularly in non-stationary settings, which limits their reliability in high-
stakes applications. Conformal Prediction (CP) has gained significant attention
foritsabilitytoprovidevalidandadaptivePIsbyensuringpredefinedconfidence
levels are met, regardless of the underlying data distribution or non-stationarity
Gammerman et al. (1998); Vovk et al. (2005). Recent advancements, such as
Ensemble Batch Prediction Intervals (EnbPI) Xu & Xie (2021) and Sequen-
tial Predictive Conformal Inference (SPCI) Xu & Xie (2023), have successfully
extended CP methodologies to time series applications, addressing the unique
challenges of electricity markets. This focus on validity, combined with adapt-
ability, positions CP as a robust framework for managing uncertainty in highly
volatile and dynamic markets, making it a critical tool for risk management.
3

1.1. Contributions
Building on the existing literature in the field, this paper makes several
notable contributions to the area of PEPF in the DAM and BM. While the
IDM and BM share structural similarities, we focus primarily on the BM due
to its fundamental role in balancing real-time supply and demand. The key
contributions of our research are outlined as follows:
• Application of QRA and CP to BM: While QRA and Split Conformal
Prediction (SCP) have been applied to the DAM, their use in the BM re-
mains unexplored. Our study address this gap by applying these methods
to both markets, exploring their performance and how combining QRA
with CP impacts model accuracy and reliability.
• Introduction of Time Series Adapted CP Approaches: We employ EnbPI
and SPCI in both DAM and BM contexts. To our knowledge, these CP
approaches have not been previously applied to any PEPF context. Our
research demonstrates the potential benefits of these methods in providing
reliable PIs.
• Introduction of Q-Ens: We propose a novel ensemble method that com-
bines predictions from QR, EnbPI, and SPCI models. This approach aims
to balance the superior efficiency of QR with the superior validity of CP
methods, offering a robust solution in PEPF.
• Evaluation and Trading Impact: We assess the efficiency and validity of
forecasts using various probabilistic metrics, and investigate the impor-
tance of coverage guarantees for trading outcomes in both DAM and BM.
Our financial analysis includes both single-trade and high-frequency trad-
ing strategies, examining the impact of probabilistic forecasts on trading
decisions and outcomes.
This research advances the field by introducing innovative CP and QRA appli-
cations, proposing a new ensemble approach, and comprehensively evaluating
probabilistic forecasts in electricity markets. We provide the accompanying
4

dataset and Python code for forecasting and trading, facilitating the adoption
and replication of our methods. Our findings highlight the strengths of CP
methods in ensuring coverage guarantees and benefiting trading strategies.
The structure of this paper is as follows: Section 2 provides an overview of
recent advancements in PEPF within the context of the DAM and BM. Section
3, we detail our methodological framework, including our forecasting models
and probabilistic approaches. Section 4 discusses probabilistic metrics used to
evaluate the efficiency and validity of our forecasts. The effectiveness of each
forecasting approach, especially the proposed ensemble, is discussed through
case study results in Section 5. Finally, Section 6 summarises our findings.
2. Related W ork
EPF has emerged as a critical research area due to the increasing complexity
and volatility of electricity markets. Accurate forecasting is essential for market
participants to make informed decisions, mitigate financial risks, and optimise
operations. Probabilistic forecasting methods, in particular, address the inher-
ent uncertainties in these markets by providing PIs rather than single-point
estimates, allowing stakeholders to assess the range of potential outcomes. Ta-
ble 1 provides a comprehensive summary of the literature on probabilistic EPF
methods, highlighting the evolution from traditional point forecasts to advanced
probabilistic techniques, including QR and CP. This section critically examines
the role of forecasting in electricity spot markets, foundational concepts of un-
certainty in EPF, recent advancements in probabilistic methods, and the grow-
ing role of CP as an alternative framework, while evaluating their strengths,
limitations, and practical implications.
2.1. Electricity Spot Markets
The DAM is a cornerstone of electricity trading, where market participants
submit bids for electricity trades up to one day in advance, with the bidding pro-
cess closing in the afternoon to determine market-clearing prices and volumes
5

based on supply, demand, and grid constraints Newbery et al. (2016); Ilea et al.
(2018). While the DAM enhances cross-border electricity trading and grid sta-
bility, itfaceschallengesfromforecastuncertaintiesdrivenbytheincreasingpen-
etration of intermittent renewable energy sources such as wind and solar Miraki
et al. (2025). These challenges necessitate advanced forecasting models capable
of managing the variability introduced by weather-dependent renewables, such
as privacy-preserving frameworks that enhance accuracy by integrating diverse
data sources Liu & Zhang (2025). Initially dominated by traditional statistical
methods, forecasting has shifted toward advanced machine learning (ML) tech-
niques, which excel at capturing the complex, non-linear relationships inherent
in electricity markets Ugurlu et al. (2018); Lago et al. (2018); Chen et al. (2019);
Li & Becker (2021). Hybrid approaches combining ML with other techniques
have further improved precision, particularly in modelling supply-demand dy-
namics and adapting to varying market conditions Lago et al. (2021); ElRobrini
et al. (2024).
The IDM is crucial for real-time electricity trading, bridging the DAM and
BM by allowing continuous trading up to a few hours before delivery. This en-
ables participants to adjust their positions in response to unforeseen events, such
as plant outages or fluctuations in renewable energy output Shinde & Amelin
(2019). In contrast to the DAM’s hourly settlement intervals, the IDM allows
trades in 30-minute blocks, notably in markets like the Irish Single Electricity
Market.The IDM’s real-time nature necessitates advanced forecasting models
capable of accurately predicting short-term price movements. These challenges
necessitate advanced forecasting models capable of managing the variability
introduced by weather-dependent renewables Piantadosi et al. (2024), with ex-
plainable frameworks helping ensure adaptability and reliability in dynamic con-
ditions Samarajeewa et al. (2024). Traditional statistical methods Uniejewski
et al. (2019b); Narajewski & Ziel (2020) have shown success in processing large
datasets and adapting to the market’s dynamic conditions. Additionally, in
markets with a high penetration of renewable energy, the IDM optimises trad-
ing strategies by enabling participants to refine their actions in near real-time,
6

thereby mitigating risks associated with price volatility Koch & Hirth (2019);
Birkeland & AlSkaif (2024). Although the BM shares several structural similar-
ities with the IDM—particularly in their real-time nature and focus on short-
term trading—our work centres primarily on the BM due to its finer granularity
and its role in balancing supply and demand in real-time.
Despite the importance of the BM in maintaining equilibrium between sup-
ply and demand, the literature on BM forecasting is relatively underdeveloped
compared to that of the DAM and IDM. The BM plays a key role in bal-
ancing supply and demand with finer granularity than the IDM, particularly
when responding to the fluctuations associated with renewable energy Ortner
& Totschnig (2019). Accurate BM price forecasts are essential, especially where
large-scale energy storage is not viable Mazzi & Pinson (2017). Studies have
compared various forecasting models and their performance in BM settings, typ-
ically with limited horizons. Probabilistic forecasting methods for BM prices,
such as those proposed by Dumas et al. (2019), show promise but suggest fur-
ther enhancements and integration into bidding strategies. Notably, existing
research often lacks critical analysis and broader context. Recent studies, in-
cluding Narajewski (2022) and O’Connor et al. (2024a), explore diverse models
for BM price forecasting, with simpler models often outperforming the more
complex ML and DL models. These studies highlight the need for continued
research to address current limitations and explore emerging methodologies,
ensuring sharp and reliable BM price predictions. Given the challenges of re-
newable energy integration and market volatility, European electricity market
reforms increasingly prioritise resilient mechanisms Zachmann et al. (2023).
2.2. Probabilistic Methods
Probabilistic forecasting methods have evolved substantially to meet the
need for robust PIs in volatile electricity markets. Techniques such as Bayesian
approaches, bootstrap methods, distribution-based forecasts, Monte Carlo simu-
lations, andhistoricalsimulationseachbringuniquestrengthsbutalsofaceprac-
tical limitations. Bayesian methods effectively quantify uncertainty by combin-
7

Reference Point Proba-
bilistic
CP Day-
Ahead
Real-
Time
Nowotarski & Weron (2015) ✓ ✓
Hagfors et al. (2016) ✓ ✓
Maciejowska et al. (2016) ✓ ✓
Hagfors et al. (2016) ✓ ✓
Lago et al. (2018) ✓ ✓
Nowotarski & Weron (2018) ✓ ✓
Koch & Hirth (2019) ✓
Shinde & Amelin (2019) ✓
Cheng et al. (2019) ✓ ✓
Dumas et al. (2019) ✓ ✓
Uniejewski et al. (2019b) ✓ ✓
Narajewski & Ziel (2020) ✓ ✓
Lucas et al. (2020) ✓ ✓
Marcjasz et al. (2020) ✓ ✓
Lago et al. (2021) ✓ ✓
Uniejewski & Weron (2021) ✓ ✓
Kath & Ziel (2021) ✓ ✓ ✓ ✓
Narajewski (2022) ✓ ✓
Khajeh & Laaksonen (2022) ✓
Jensen et al. (2022) ✓ ✓
Hu et al. (2022) ✓ ✓
Zaffran et al. (2022) ✓ ✓
Uniejewski (2023) ✓
Marcjasz et al. (2023) ✓ ✓
Ghosh et al. (2023) ✓ ✓
Dewolf et al. (2023) ✓ ✓
Trebbien et al. (2023) ✓ ✓
Cordier et al. (2023) ✓ ✓
8

Reference Point Probab-
ilistic
CP Day-
Ahead
Real-
Time
O’Connor et al. (2024a) ✓ ✓ ✓
Monjazeb et al. (2024) ✓ ✓
De la Torre et al. (2024) ✓ ✓ ✓
Lee et al. (2024) ✓ ✓
Xu et al. (2024a) ✓ ✓
Angelopoulos et al. (2024) ✓
Our approach ✓ ✓ ✓ ✓
Table 1: Literature on PEPF. The ✓is the approach presented herein
ing prior knowledge with observed data, as seen in advancements like Bayesian
neural networks (BNNs), stochastic volatility models, and hybrid Bayesian op-
timisation Vahidinasab & Jadid (2010); Kostrzewski & Kostrzewska (2019);
Chengetal.(2019). However, theirhighcomputationaldemandsandrelianceon
strong priors limit scalability, particularly in non-stationary conditions. Boot-
strap methods, such as residual-based bootstrapping, improve empirical cov-
erage in BM settings but often produce overly wide intervals during volatile
periods Uniejewski et al. (2019a); Khosravi et al. (2013). Distribution-based
forecasts, including copula processes and generalised additive models, capture
extreme price behaviours but are constrained by their reliance on correct dis-
tributional assumptions Klein et al. (2023); Serinaldi (2011); Monteiro et al.
(2018). Monte Carlo simulations, enhanced through Bayesian networks and se-
quential Markov Chain Monte Carlo techniques, improve real-time adaptability
but remain computationally prohibitive for high-frequency trading Yuanchen
et al. (2023). Historical simulations offer simplicity and robustness but strug-
gle to address structural shifts or unprecedented events, particularly in markets
integrating renewable energy Maciejowska & Nitka (2024); Janczura (2024). Re-
cent studies have explored the use of meta-heuristic optimization techniques for
forecasting models in short-term load forecasting Bhatnagar et al. (2025).
9

These limitations have driven interest in Conformal Prediction (CP) tech-
niques, which offer a flexible, distribution-free framework for generating reli-
able PIs. CP avoids the restrictive assumptions of traditional methods while
ensuring predefined confidence levels, even in non-stationary markets Gammer-
man et al. (1998); Vovk et al. (2005). Recent advancements, such as Ensemble
Batch Prediction Intervals (EnbPI) and Sequential Predictive Conformal Infer-
ence (SPCI), extend CP’s utility to time-series applications Xu & Xie (2023).
Despite these strengths, CP’s reliance on large calibration datasets and sensi-
tivity to structural breaks can undermine performance in dynamic electricity
markets Foygel Barber et al. (2022). Further research should focus on enhanc-
ing CP’s adaptability and robustness, particularly for handling extreme price
events and evolving market complexities.
Quantile Regression & Conformal Prediction
QR and QRA are widely used in PEPF for their simplicity, efficiency, and
ability to capture uncertainty across quantiles. Recent advancements have re-
fined these techniques, such as Lasso QRA and smoothed QRA with kernel
estimation, which improve predictive performance Uniejewski & Weron (2021);
Uniejewski (2023). DL integrations have also shown promise, with methods like
QR combined with LSTNet and SHAP-based feature selection enhancing sharp-
ness through kernel density estimation Liu et al. (2023), or hybrid QR-LSTM
frameworks optimised via multi-objective algorithms improving accuracy under
diverse market conditions Xu et al. (2024b). While effective, QR and QRA
face challenges in uncertainty quantification, particularly in achieving reliable
coverage, motivating the exploration of CP as a complementary framework.
CP generates distribution-free PIs with predefined confidence levels, making
it a robust alternative for uncertain and volatile markets Gammerman et al.
(1998); Vovk et al. (2005). Extensions like Ensemble Batch Prediction Intervals
(EnbPI), which combines ensemble learning with block bootstrap methods, have
demonstrated success in addressing seasonality and trends in energy forecasting
Xu & Xie (2021); Zaffran et al. (2022). Similarly, Sequential Predictive Con-
10

formal Inference (SPCI) dynamically recalibrates PIs to improve reliability in
non-stationary settings, with Transformer-based extensions further enhancing
its adaptability Lee et al. (2024). Hybrid approaches such as Ensemble Con-
formal QR and SCP with QR, offer a balance between computational efficiency
and robust coverage, making them suitable for real-time applications Jensen
et al. (2022); Cordier et al. (2023). However, CP still faces practical limita-
tions, including sensitivity to structural breaks and reliance on large calibration
datasets Foygel Barber et al. (2022). Enhancing CP’s robustness, addressing
extreme price events, and integrating CP with DL architectures to improve its
accuracy and adaptability in dynamic electricity markets have proven beneficial
Angelopoulos et al. (2024); Xu et al. (2024a).
3. Methodology
This section outlines our study’s methodology, emphasising the key models
and forecasting approaches. It is structured as follows: Section 3.1 introduces
probabilistic forecasting models, followed by Section 3.2, which describes the
proposed uncertainty quantification approaches and our proposed ensemble, Q-
Ens.
3.1. Electricity Price Prediction Models
The probabilistic regressor models benchmarked include:
• LASSO Estimated AR (LEAR): An autoregressive model with LASSO
regularization for feature selection and handling high-dimensional data,
providing probabilistic predictions through conditional distribution esti-
mation.
• K-Nearest Neighbors(KNN): A non-parametric model predicting outputs
based on the "K" nearest neighbors, with probabilistic predictions derived
from the neighbors’ output distribution.
11

• Random Forest(RF): An ensemble model combining multiple regression
trees to reduce variance and maintain low bias, generating probabilistic
predictions by aggregating tree outputs.
• Light Gradient Boosting Method(LGBM):Anensemblemodelusingboost-
ing to reduce bias and variance, providing probabilistic forecasts by sum-
ming weighted outputs of weak learners (trees).
3.2. Uncertainty Estimation
In the domain of EPF, probabilistic forecasting methods offer a significant
advancement over traditional point forecasts by providing insights into the un-
certainty surrounding future prices. In this section, we delve into various meth-
ods for PEPF in both the DAM and BM. We outline the approaches utilised,
including QR, SCP, EnbPI, SPCI, QRA, and our proposed QR-CP Ensemble
(Q-Ens).
We frame the price prediction problem as a regression task. Given a dataset
Z = {(xt, yt)}N t=1, where xt represents the covariates andyt the response vari-
able, our objective at each time stept is to predict the next priceyt based on
previous prices and covariatesxt. The prediction is made using a modelf, such
that:
ˆyt = f (xt) (1)
where ˆyt is the model’s prediction. The models are trained on the historical
dataset Z, which consists of N input-output pairs. The conditional quantile
function Qyt (α | xt) estimates the value below which a certain percentageα of
the future price yt is expected to fall, given the covariatesxt. We denote the
lower quantile at levelα as ˆqα t and the upper quantile at level1 − α as ˆq1−α t . In
the probabilistic prediction setting, as shown in Figure 1, the modelf generates
a PI defined by these quantiles:
Γ1−2α(xt) = [ˆqα t , ˆq1−α t ] (2)
This interval indicates that the future priceyt is expected to fall within the
range [ˆqα t , ˆq1−α t ] with a confidence level of1 − 2α. For example, ifα = 0.1, the
12

0 2 4 6 8 10 12
0
10
20
30
ˆqα t
ˆq1−α t
ˆqα t+1
ˆq1−α t+1
ˆqα t+2
ˆq1−α t+2
ˆqα t+3
ˆq1−α t+3
ˆqα t+4
ˆq1−α t+4
Time
e/MWh
Real Price
Forecasted Price
Quantile Region
Figure 1: Quantile forecast of electricity prices
PI corresponds to an 80% confidence level (1 − 2α = 0.8), implying that there
is an 80% probability thatyt will lie within the interval.
3.2.1. Quantile Regression
QR, introduced in Koenker & Bassett Jr (1978), extends ordinary least
squares regression to estimate conditional quantiles of the response variable
rather than just the mean. QR provides a more comprehensive view by estimat-
ing the conditional median or other quantiles, revealing how covariates influence
the entire distribution of the response variable. Consider a linear model of the
form:
yt = x⊤ t β + ϵt (3)
where yt isthedependentvariableforthe t-thobservation, xt isa K-dimensional
vector of covariates, β is a K-dimensional vector of coefficients, andϵt is the
error term.
The goal of QR is to estimate the conditional quantile function, which rep-
resents the value below which a certain percentageα of the response variable
yt falls, given the predictor variablext. For a given α quantile level, the QR
13

estimator ˆβα is defined as the solution to the following optimisation problem:
ˆβα = arg min β
NX
t=1
ρα(yt − x⊤ t β) (4)
where ρα(u) is the check function defined by:
ρα(u) = u(α − 1{u <0}) (5)
Here, 1{u <0}isanindicatorfunctionthatequals1if u <0and0otherwise.
The check function can be rewritten as:
ρα(u) =



αu if u ≥ 0
(α − 1)u if u <0
(6)
This function penalises underestimation and overestimation asymmetrically, de-
pending on the value of α. Specifically, it assigns a weight of α to positive
residuals and 1 − α to negative residuals, allowing the estimation of different
quantiles.
The asymptotic properties of the QR estimatorˆβα are well-established un-
der suitable regularity conditions. The estimator ˆβα is consistent, meaning it
converges to the true parameter value as the sample size increases, and it is
asymptotically normally distributed, approaching a normal distribution as the
sample size grows. The asymptotic covariance matrix ofˆβα is given by:
Cov( ˆβα) = α(1 − α)  fyt|xt (ˆqα t )2 · (X ′X)−1 (7)
where α(1 − α) adjusts for the variability in estimating the quantile levelα,
fyt|xt (ˆqα t ) is the conditional density ofyt given xt at the α quantile level, re-
flecting the density around this quantile, and (X ′X)−1 is the inverse of the
product of the design matrix with its transpose. The design matrixX contains
the values of all predictor variables for each observationX = {(xt)}N t=1, and its
inverse accounts for the scaling and correlations among these predictors.
Conformal Prediction
CP is a flexible, distribution-free framework for quantifying the uncertainty
of predictions made by machine learning models. CP generates prediction sets
14

with a predefined confidence level, ensuring that the true value lies within these
sets with a specified probability. At the core of CP is the concept of nonconfor-
mity, which measures how unusual a new data point(xnew, ynew) is compared
to a set of previously observed examples. A nonconformity measureA is de-
fined to assign a nonconformity score to each data point in the training setZ.
Traditional CP methods use p-values calculated from nonconformity scores to
construct prediction sets. For a new examplexnew with a candidate labelynew,
the p-value is given by:p(ynew) =
|{(xt, yt) ∈ Z: A(xt, yt) ≥ A(xnew, ynew)}| + 1
N + 1 (8)
where N is the size of Z. The prediction set for xnew includes all candidate
labels for which the p-value exceeds a certain significance level.
3.2.2. Split Conformal Prediction
SCP, also known as inductive CP, is a simplified variation of standard confor-
mal prediction that enhances computational efficiency by dividing the data into
two separate sets: a training set and a calibration set. The training set is used
to fit a predictive model, while the calibration set is used to generate noncon-
formity scores, which measure the discrepancy between the true and predicted
values. The data is split into two subsets: a training setZtrain and a calibration
set Zcal. A predictive modelf is trained onZtrain, and the model’s performance
is assessed on the calibration set by computing nonconformity scores for each
pair (xt, yt) ∈ Zcal.
The nonconformity score for an observationt is defined as:
A(xt, yt) = |yt − f (xt)| (9)
This score measures the absolute difference between the true valueyt and the
predicted value f (xt), with larger scores indicating higher nonconformity be-
tween the model’s prediction and the observed outcome. Once nonconformity
scores are computed for all calibration examples, a quantile of the nonconfor-
mity scores is selected to construct PIs for new data points. Let λt be the
15

quantile for time periodt, corresponding to the desired confidence level1 − 2α.
This ensures that at least1−2α of the calibration examples have nonconformity
scores smaller than or equal toλt, guaranteeing that the PIs will cover the true
value with confidence level1 − 2α.
For a new examplext, the PI is constructed as:
Γ1−2α(xt) = [f (xt) − λt, f(xt) + λt] (10)
This interval represents the range of possible values for the response variableyt
that are consistent with the nonconformity scores computed from the calibra-
tion set. SCP balances computational efficiency and prediction robustness by
calculating nonconformity scores on a smaller calibration set, avoiding the need
to recompute predictions for each test example. This reduces the computational
load but assumes data exchangeability, which limits its applicability in settings
like time series data.
3.2.3. Ensemble Batch Predictive Interval (EnbPI)
EnbPI, introduced in Xu & Xie (2021), is a probabilistic method within
the CP framework, specifically designed to generate PIs with strong coverage
guarantees. EnbPI leverages ensemble learning techniques and bootstrap sam-
pling to provide reliable PIs, particularly for forecasting applications. Unlike
traditional CP methods that require a separate calibration set, EnbPI adopts
a leave-one-out approach, which enables the method to maintain valid coverage
without sacrificing data for calibration. Given a datasetZ, EnbPI constructs
PIs by first generatingB bootstrap samples from the original dataset. A pre-
dictive model f (b) is trained on each bootstrap sampleZ (b), allowing EnbPI to
account for model variability and provide more reliable PIs. For each trained
model f (b), residuals are computed for every observation(xt, yt) by calculating
the absolute difference between the observed valueyt and the predicted value
f (b)(xt). The residuals are given by:
A(b)(xt, yt) = |yt − f (b)(xt)| (11)
16

These residuals reflect the model’s prediction errors and are used to deter-
mine the width of the PIs. The quantileλ(b) t for each bootstrap model is defined
as:
λ(b) t = Quantile1−2α(A(b) 1 , A(b) 2 , . . . , A(b) N ) (12)
The PI for a new input xt is constructed as Γ1−2α(xt), for a confidence
level of 1 − 2α, by averaging the predictions from all bootstrap models and
incorporating the marginλt. The resulting PI is given by:
Γ1−2α(xt) =
"
1
B
BX
b=1
f (b)(xt) − λt, 1 B
BX
b=1
f (b)(xt) + λt
#
(13)
where λt is the average of the quantilesλ(b) t across all bootstrap models:
λt = 1 B
BX
b=1
λ(b) t (14)
By averaging across multiple models and adjusting the interval width using the
quantile of residuals, EnbPI mitigates the effects of outliers and reduces the
variance in PIs. Its flexibility allows use across various models and data types,
making it ideal for complex EPF. The use of ensemble learning also improves
the resilience of the PIs.
3.2.4. Sequential Predictive Conformal Inference (SPCI)
SPCI, introduced in Xu & Xie (2023), extends the EnbPI method to handle
non-exchangeable time series data. Recognizing the limitations of traditional
CP methods in the context of temporal dependencies, SPCI incorporates quan-
tile regression forests (QRF) to estimate conditional quantiles of residuals. This
allows SPCI to better adapt to the temporal dependencies and heteroskedastic-
ity often encountered in time series data. SPCI works by training a predictive
model f on the datasetZ. The model’s residuals are computed using Equation
(9) on a rolling calibration set and used to estimate future residuals through
QR. By applying QRF to the residuals, SPCI estimates the conditional quantile
ˆqα t , where 1 − 2α represents the desired confidence level. This approach helps
SPCI account for the serial dependence in the residuals, which is critical for
17

accurate PIs in time series forecasting. To generate PIs for a new inputxt,
SPCI constructs the interval:
Γ1−2α(xt) = [f (xt) − λt, f(xt) + λt] (15)
where λt is derived from the quantiles of past residuals, adjusted for the level
of uncertainty in the data. One of the main advantages of SPCI is its ability to
dynamically re-estimate residual quantiles as new data becomes available. This
adaptive mechanism allows the method to maintain valid coverage over time, en-
suring that the true outcome falls within the PI with a specified confidence level
(1 − 2α). Furthermore, SPCI is applicable to a wide range of predictive models
and data types, making it highly versatile for complex time series forecasting
tasks. Compared to SCP and EnbPI, SPCI often yields narrower intervals with-
out sacrificing coverage, offering a powerful tool for uncertainty quantification
in time series.
3.2.5. Quantile Regression Averaging
QRA was introduced in Nowotarski & Weron (2015). QRA applies QR
to a set of point forecasts from different models, allowing direct estimation of
electricity spot price distribution without separating the probabilistic forecast
into a point forecast and an error distribution. This method directly leverages
electricity price distribution properties for improved forecasting accuracy. It
considers M different point prediction modelsf m and feeds their output to a
probabilistic model:
Γ1−2α(xt, [f 1(xt), f2(xt), . . . , fM (xt)]) = [ˆqα t , ˆq1−α t ] (16)
In our implementation, two sets of point forecasts are generated:
• QRA-R: Includes forecasts from models trained on different data contexts
(full datasets, historical, and future datasets) to capture diverse trends
and improve reliability.
• QRA-CP: Consists of forecasts from various Conformal Prediction (CP)
18

models like SCP, EnbPI, and SPCI, each contributing unique strengths to
quantile predictions.
3.2.6. QR-CP Ensemble: A Robust Approach
Inpredictivemodeling, uncertaintyiscategorisedintoepistemicandaleatoric
types. Epistemic uncertainty arises from limited knowledge of the underly-
ing model and can be reduced with more data or model improvements, while
aleatoric uncertainty results from inherent variability in the data and cannot
be mitigated by additional data. Our Q-Ens combines QR, EnbPI, and SPCI
aims to address both uncertainties, improving the reliability and sharpness for
PEPF. QR captures a wide range of possible outcomes by estimating multiple
conditional quantiles, thus addressing both epistemic and aleatoric uncertain-
ties. EnbPI reduces epistemic uncertainty by averaging predictions from boot-
strap samples, thereby lowering variance and reflecting aleatoric uncertainty in
the constructed PIs. SPCI adapts dynamically to new data, updating PIs in
real-time to account for evolving data variability, thus capturing both types of
uncertainty as they change over time.
The ensemble combines the strengths of these methods, working from a sim-
ilar approach as EnbPI, averaging the models outputs to both reduce epistemic
uncertainty further, and improve overall forecast performance. The ensemble
prediction is obtained by averaging the quantile predictions from QR, EnbPI,
and SPCI models: Γ1−2α =
[ 1 3 (QRα +EnbPIα +SPCIα), 1 3 (QR1−α +EnbPI1−α +SPCI1−α)] (17)
with an outline of the PIs construction shown in Figure 2.
4. Evaluation Metrics
Our evaluation of probabilistic predictions hinges on two crucial dimensions:
validity and efficiency. Efficiency, gauged through metrics like sharpness and in-
terval width, enhances precision. Simultaneously, validity, including calibration
19

Figure 2: Construction of the Ensemble, Q-Ens.
and coverage, requires the generation of precise PIs to affirm the reliability of
our forecasts.
4.1. Efficiency
Efficiency in probabilistic forecasting is crucial for precision. It is evaluated
using two key metrics: the Pinball Score and Interval Width.
4.1.1. Pinball Score
In both the DAM and BM, sharpness plays an important role in accurate
anticipation, hedging, and real-time adjustments. The Pinball Score Zhao et al.
(2019), derived from the Pinball Loss function, measures the sharpness of the
forecast based on the quantile predictionˆqα t and the observed priceyt for time
period t:
P S(ˆqα t , yt, α) =



(1 − α)(ˆqα t − yt) for yt ≤ ˆqα t
α(yt − ˆqα t ) for yt ≥ ˆqα t
(18)
20

Here, α denotes the quantile level, such as 0.1 for the 10th percentile; hence, an
80% PI ([ˆqα t , ˆq1−α t ]) corresponds to quantile levels 0.1 and 0.9.
4.1.2. Interval Width
The Interval Width is another important metric for assessing the efficiency of
probabilistic forecasts. While sharpness ensures reliability, efficiency is pivotal
in refining precision, and it is intricately linked to the width of PIs. The Interval
Width (IW t) for a given PI can be defined as follows:
IW t = ˆq1−α t − ˆqα t (19)
where ˆq1−α t and ˆqα t are the upper and lower quantiles of the PI, respectively.
Narrower intervals indicate higher efficiency, reflecting greater precision in the
forecast.
4.2. Validity
Validity in probabilistic forecasting ensures that the predicted intervals ac-
curately reflect the true distribution of the observed data. Two primary metrics
used to evaluate validity are coverage and the Winkler Score.
4.2.1. Coverage
Both reliability and accuracy of probabilistic forecasts are crucial, with a
particular focus on evaluating their validity. We examine the models’ coverage
to highlight their ability to capture the true distribution, focusing on precision
in capturing the priceyt within a predefined PIs. The empirical coverage, in-
dicating the agreement of predictions with the specified intervals, is denoted by
the binary indicatorI α t :
I α t =



1 if yt ∈ [ˆqα t , ˆq1−α t ]
0 if yt /∈ [ˆqα t , ˆq1−α t ]
(20)
The Coverage Probability (Λ) is then defined as:
Λ = 1 N
NX
t
I α t (21)
21

where N is the total number of forecasts. Ideally, the coverage probability
should be close to the nominal level (e.g., 80% ifα =0.1), indicating that the
PIs are valid.
4.2.2. Winkler Score
The Winkler Score (Wt) combines reliability and sharpness into a single
metric, offering a comprehensive assessment of probabilistic forecasts. This
score evaluates the interval width (IW t), see equation 19, of PIs based on the
observed values (yt), incorporating a penalty factor (τ) for deviations from the
interval bounds:
Wt =



IW t if yt ∈ [ˆqα t , ˆq1−α t ]
IW t + 2 τ (ˆqα t − yt) if yt < ˆqα t
IW t + 2 τ (yt − ˆq1−α t ) if yt > ˆq1−α t
The Winkler Score penalises larger deviations when observed prices fall outside
the PIs, offering insight into the model’s balance of accuracy and interval width.
5. Case Studies
We present two case studies to demonstrate the effectiveness of our QR-CP
Ensemble (Q-Ens) approach for PEPF in the DAM and BM. Utilizing datasets
from O’Connor et al. (2024a) spanning 2019 to 2022, we focus on the Irish elec-
tricity market, which is characterized by high curtailment rates due to surplus
renewable generation during low-demand periods Yasuda et al. (2022). This
section evaluates probabilistic approaches and forecasting models in both the
DAM 5.1 and the BM 5.2. We examine the effectiveness of each model, looking
at QR and CP approaches, with a focus on the performance of our proposed
QR-CP Ensemble. The analysis can be divided into two main aspects: efficiency
and validity. Efficiency evaluates the sharpness of the forecasts by examining
metrics such as the Aggregate Pinball Score (APS) and interval width. Validity
assesses the reliability of the forecasts by measuring each approach’s ability to
22

achieve coverage. These two aspects are integrated using the Winkler Score,
which ties together efficiency and validity. This culminates in a financial per-
formance evaluation of these probabilistic methods in Section 5.3. To ensure
reproducibility, the Python code and dataset used for this section are available
on GitHub1.
5.1. Day-Ahead Market
The DAM dataset includes historical data and the system operator (TSO)
predictions, revealing past market behaviors and aiding in forecasting future
conditions. In this case study, we predict DAM prices for the next 24 settlement
periods using historical DAM prices and TSO wind and demand forecasts from
the past 168 hours.
5.1.1. Efficiency in the Day-Ahead Market: Pinball Score & Interval Width
Analyzing the APS for DAM models in Table 2 highlights the strong perfor-
mance for the Q-Ens approach, producing the two lowest APS in the DAM for
theRFandLGBMmodels. ThisincludesstrongperformanceforCPapproaches
Model QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
KNN 6.65 7.79 5.71 6.09 6.20 6.01 5.96
LEAR 8.35 4.81 4.18 4.08 8.36 8.35 4.54
LGBM 3.62 3.67 3.76 3.71 3.67 3.66 3.48
RF 3.63 3.85 3.81 3.84 3.60 3.61 3.59
Avg. 5.56 5.03 4.37 4.43 5.43 5.36 4.39
Table 2: APS for the DAM. Best approach for each regressor marked in bold, worst in red.
EnbPI and SPCI, in particular improving LEAR and KNN models, taking ad-
vantage of CPs model agnostic feature. Time series adapted CP approaches
EnbPI and SPCI also demonstrate notable improvements over SCP. QR and
1https://anonymous.4open.science/r/PEPF_Conformal-C0AF/
23

QRA models struggle, but this is largely as a result of their poor performance
with LEAR, substantially dragging down the average.
Looking further into efficiency, we evaluate the interval width of the models
for the DAM in Figure 3, centered around a median of 50 for clarity. The
analysis of IW across different models reveals key insights into model efficiency
and precision. A pronounced contrasting outcome in Figure 3 between QR
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
0
10
20
30
40
50
60
70
80
90
100 QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Interval Width
Figure 3: Interval Width for each model in the DAM
and CP approaches is how CP approaches, SCP, EnbPI, and SPCI, result in a
wider interval width for less accurate models KNN and LEAR, and a narrowing
interval width for the more accurate RF and LGBM. SPCI, developed as a
successor to EnbPI to produce narrower intervals, fails to achieve this for KNN
in the DAM but succeeds slightly for LEAR, LGBM, and RF. This trend is
absent entirely for QR and QRA approaches with QR and QRA producing
intervals independently of models accuracy, with QRA-CP producing similarly
sized Interval widths compared to QRA-QR, despite the contrasting contents of
each approaches dataset. Q-Ens closely mirrors EnbPI and SPCI for LEAR and
KNN models. However, for LGBM, Q-Ens produces narrower interval widths
due to the model’s inherently narrow intervals when using QR. Conversely, Q-
Ens with RF produces wider intervals than EnbPI or SPCI due to the wider
24

interval width of QR.
5.1.2. Validity in the Day-Ahead Market: Coverage
Figure 4 summarizes coverage across the 0.1-0.9 quantile range in the DAM,
highlighting each forecasting approaches ability to achieve coverage. In the
KNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBM
0.4
0.6
0.8
1
Coverage
QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Figure 4: DAM Coverage for 0.1-0.9 quantile pair
DAM context, aiming for a coverage of 0.8 within the 0.1-0.9 quantile range,
CP models consistently outperform QR counterparts. QR produces the worst
results by a margin, failing to achieve coverage in a single model. Both QRA
approaches begin to diverge from QR, improving coverage for most models,
LGBMinparticular, andachievingthedesired0.8coverageforRFinbothQRA-
R and QRA-CP. Our Q-Ens approach yields slightly inferior results compared
to EnbPI and SPCI. However, considering the lower APS for RF and LGBM
models compared to EnbPI and SPCI, as shown in Table 2, this trade-off is
justified.
Focusing on the 0.3-0.7 quantile pair with a target of 0.4 in Figure 4, we see
a similar trend to Figure 4 with QR struggling and QRA improving QR for each
model, with the exception of RF this time. All CP approaches achieve coverage
for all models this time, highlighting the advantages of CP when it comes to
improving a models reliability. Our Q-Ens achieves coverage for all models, with
slightly lower scores than EnbPI and SPCI, but substantially better than QR,
with the exception of RF.
25

KNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBM
0
0.2
0.4
0.6
0.8
1
Coverage
QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Figure 5: DAM Coverage for 0.3-0.7 quantile pair
5.1.3. Efficiency & Validity in the Day-Ahead Market: Winkler Score
Table 3 provides a detailed overview of Winkler Scores, highlighting each
approach’s ability to tie together both efficiency and validity in our chosen fore-
casting models. Our approach Q-Ens excels producing the lowest average score,
Model QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
KNN 57.02 64.16 51.47 56.16 53.70 51.73 54.33
LEAR 61.97 36.30 37.37 35.06 61.82 61.74 39.37
LGBM 29.87 30.39 32.76 31.31 31.5 31.47 29.79
RF 33.7 30.81 32.14 31.65 33.00 32.36 29.99
Avg. 42.94 40.42 38.43 38.55 45.01 44.33 38.37
Table 3: Winkler Scores for the DAM. Best approach for each regressor marked in bold, worst
in red.
and the two lowest scores for all models with LGBM and RF. QR and QRA pay
the price of their poor performance in coverage, producing the highest average
winkler scores. CP approaches produce lower winkler scores, underscoring the
benefits of their strong performance in coverage, with EnbPI strong performance
just missing out on our Q-Ens approach.
26

5.2. Balancing Market
The BM dataset include historical data and TSO predictions, revealing past
market behaviors and aiding in forecasting future conditions. For the BM, we
forecast prices for the next 16 open settlement periods starting att + 2, uti-
lizing historical BM prices, volumes, wind discrepancies, interconnector flows,
and DAM prices from the past 24-48 hours. We also incorporate future physical
notifications, interconnector schedules, renewable forecasts, demand forecasts,
and DAM prices for the next 8 hours. Despite similar average prices with
the DAM (BM:e54.772/MWh, DAM: e53.77/MWh), the BM exhibits higher
price volatility (standard deviation: e64.60/MWh) compared to the DAM
(e37.38/MWh). More Details surrounding both the DAM and BM datasets
can be found at O’Connor et al. (2024a).
5.2.1. Efficiency in the Balancing Market: Pinball Score & Interval Width
Analyzing the APS for BM models in Table 4 follows a similar trend to
Table 2 with Q-Ens showing strong performance producing the lowest average
this time, except we see EnbPI and SPCI, two of the top approaches for the
DAM, produce the two highest average scores. SCP produces markedly better
Model QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
KNN 14.09 15.19 14.60 15.84 13.66 13.49 14.25
LEAR 15.22 12.91 13.96 13.79 15.33 15.22 13.21
LGBM 12.48 12.87 13.55 13.6 12.58 12.41 12.70
RF 12.66 13.01 13.34 13.48 12.79 12.89 12.88
Avg. 13.61 13.50 13.91 14.18 13.59 13.50 13.26
Table 4: APS for the BM. Best approach for each regressor marked in bold, worst in red.
scores, with QR and QRA approaches also performing better than EnbPI and
SPCI. The two lowest scores are achieved by LGBM with QRA-R and RF with
QR.
27

Examining efficiency in the BM, we evaluate the interval width of the models
in Figure 6. Compared to the average interval width for the DAM in Figure 3, all
models in the BM have significantly wider interval widths, reflecting the greater
inherent uncertainty in the BM. We see the same trend as the DAM with interval
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
KNNLEARLGBM
RF
0
10
20
30
40
50
60
70
80
90
100
QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Interval Width
Figure 6: Interval Width for each model in the BM
width being independent of model accuracy for QR and QRA approaches, but
again a strong correlation between interval width and model accuracy for all CP
approaches, albeit less pronounced for SPCI than in the DAM. SPCI produces
narrower interval widths than EnbPI as expected, but much more pronounced
than in the DAM. Q-Ens produces wider interval widths than SPCI and QR,
skewed by EnbPI large interval width.
5.2.2. Validity in the Balancing Market: Coverage
Figure 7 summarizes coverage across the 0.1-0.9 quantile range in the BM.
Aiming for a coverage of 0.8 within this range, all models in the BM come signif-
icantly closer to achieving the desired coverage compared to their performance
in the DAM. CP approaches similarly excel, with all models achieving coverage,
excluding LGBM for EnbPI and RF for SPCI, both just missing the coverage
target. QRA again improves all QR models noticeably, with RF for both QRA
approaches achieving coverage. Our Q-Ens fails to perform as well as any CP
28

KNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBM
0.4
0.6
0.8
1
QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Figure 7: BM Coverage for 0.1-0.9 quantile pair
approach, but outperforms all QR and QRA models bar RF for QRA.
Focusing on the 0.3-0.7 quantile pair aiming for a coverage of 0.4 in Figure
8, again all CP approaches achieve coverage, including Q-Ens. QRA fails to
KNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBMKNNLEAR
RF
LGBM
0
0.2
0.4
0.6
0.8
1
QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
Figure 8: BM Coverage for 0.3-0.7 quantile pair
demonstrate a noticeable improvement off of QR, but all models come close to
achieving coverage, with RF for QR and both QRA achieving the 0.4 target.
5.2.3. Efficiency & Validity in the Balancing Market: Winkler Score
Table 5 provides a overview for Winkler Scores in the BM, offering insights
into each approaches ability to tie efficiency and validity together. The analysis
in Table 5 highlights the strong performance of our ensemble approach again,
resulting in the second lowest winkler score, slightly underperforming QRA-
29

Model QR SCP EnbPI SPCI QRA-R QRA-CP Q-Ens
KNN 124.18 134.77 131.35 132.18 119.21 120.89 126.35
LEAR 127.79 115.02 122.63 126.16 129.03 127.75 124.09
LGBM 107.34 115.77 111.18 122.41 109.47 108.34 111.18
RF 114.37 113.88 111.84 114.32 116.15 115.07 111.39
Avg. 118.42 119.86 119.25 123.77 118.47 118.01 118.25
Table 5: Winkler Scores for the BM. Best approach for each regressor marked in bold, worst
in red.
CP. QR and QRA demonstrate considerably improved performance than they
did for winkler scores in the DAM, with QRA-CP coming first, QR third, and
QRA-R fourth. The last 3 spots are occupied by all three CP approaches with
SPCI changing from just 0.07 off the top approach in the DAM, to the worst
performer in the BM. QR achieves the lowest score of any model with LGBM,
while Q-Ens has the second lowest with RF. These results are likely due to
the closer coverage scores and narrower interval widths for the QR and QRA
approaches.
5.3. Financial Performance Analysis
For our financial evaluation, we utilise a Battery Energy Storage System
(BESS). This section outlines our BESS trading strategy, crucial for ensuring
grid stability and seamlessly integrating renewable energy into the dynamic
energy landscape. This consists of our Single trade strategy (TS1) and our
high-frequency trading strategy (TS2):
• TS1 is a rule-based heuristic trading strategy adopted from Uniejewski
& Weron (2021); Uniejewski (2023). This strategy utilizes quantile-based
forecasts to optimize trading decisions involving a hypothetical 1 MWh
battery with no discharge limit, 80% discharge efficiency, and 98% charge
efficiency. Over the specified time horizon (1 day for DAM or 8 hours for
30

BM), a single buy-sell pair trade is permitted, with the requirement that
the buy trade occurs before the sell trade.
• TS2 leverages optimization techniques to maximize profits in electricity
markets, adopted from O’Connor et al. (2024b). It incorporates flexible
buy/sell timestamps within bottleneck-constrained volumes, considering
realistic constraints such as battery capacity, charging speed, discharging
rate, minimum charge level, and energy efficiency. The dynamic adjust-
ment of charging and discharging operations, based on forecasted mini-
mum and maximum price periods, is a fundamental aspect of this adap-
tive approach. The overarching goal of TS2 is to enhance profitability
within bottleneck limitations, significantly increasing trading frequency
and contributing to overall market efficiency.
For more detailed information on the implementation of both TS1 and TS2
see O’Connor et al. (2024b). Table 6 summarizes the financial performance of
Model TS1
DAM
TS1 BM TS2
DAM
TS2 BM A vg.
DAM
A vg. BM
QR e16,376 e3,634 e21,887 e16,112 e19,131 e9,873
SCP e16,032 -e1,215 e17,610 e11,119 e16,821 e4,952
EnbPI e16,806 e3,214 e20,932 e16,237 e18,869 e9,725
SPCI e16,486 e3,280 e21,632 e16,807 e19,059 e10,044
QRA-R e13,868 e2,768 e20,938 e14,705 e17,403 e8,736
QRA-CP e13,880 e3,923 e20,805 e15,061 e17,342 e9,492
Q-Ens e16,935 e3,748 e21,926 e17,400 e19,430 e10,574
Table 6: Financial Performance Comparison of RF & LGBM Models. Best approach marked
in bold, worst in red.
various forecasting approaches in the DAM and BM for trading strategies TS1
and TS2, excluding the KNN and LEAR models to focus on top performers.
SCP consistently produces the worst results, with the lowest averages and the
31

poorest performance in TS2 for both markets and TS1 for the BM. In contrast,
EnbPIandSPCIdemonstratestrongperformance, withSPCIleadingamongthe
CP approaches, highlighting the benefits of time series-adapted methods. QRA
does not surpass QR, with QR achieving better average scores in both markets
and QRA-R ranking last for TS1 in the DAM. However, QRA-CP secures the
top result for TS1 in the BM and scores closer to QR in the BM. The most
notable outcome is the strong performance of our ensemble approach, which
achieves the highest average result in both the DAM and BM, only missing the
top position for TS1 in the BM.
5.4. Key Findings and Limitations
The application of CP techniques, particularly EnbPI and SPCI, improves
the accuracy of PEPF in both DAM and BM, outperforming traditional QR
models by providing more reliable PIs with consistent coverage. The ensemble
approach, combining QR with EnbPI and SPCI, improves the balance between
narrow intervals and coverage, resulting in more consistent and accurate fore-
casts. Financial analysis of these forecasting methods indicates that CP tech-
niques, particularly our ensemble, Q-Ens, can increase profitability in trading
algorithms; however, their dependence on large amounts of historical data and
higher computational requirements may limit their practicality in real-time sce-
narios. These models can also face challenges when encountering extreme price
events or sudden market shifts.
6. Conclusion
This study evaluated several probabilistic forecasting methods for electric-
ity prices in the Irish DAM and BM, focusing on QR, QRA-R, QRA-CP, SCP,
EnbPI, SPCI, and the proposed ensemble method Q-Ens. Our evaluation cov-
ered multiple dimensions—accuracy, reliability, interval width, coverage, and fi-
nancial performance. We found that QR and QRA approaches performed well in
efficiency metrics but fell short in coverage, where CP methods like SCP, EnbPI,
32

and SPCI excelled. The ensemble approach (Q-Ens) demonstrated strong re-
sults in both efficiency and validity, and it delivered superior financial outcomes
in a single trade and high-frequency trading strategy, confirming its practical
value for market participants. The integration of CP techniques into EPF offers
a promising way to improve forecast reliability and financial outcomes, espe-
cially as the energy market evolves and renewable energy integration increases.
However, the financial evaluation, based on simulated trading, may not fully
capture the complexities of real-world market conditions, including transaction
costs, market liquidity, and sudden structural shifts. Therefore, further research
should focus on testing these methods in diverse markets, including IDM, and
exploring the practical limitations of CP models, particularly in environments
with extreme price events or limited historical data. Future studies could also
delve deeper into more granular 5-minute BM datasets and incorporate proba-
bilistic forecasting frameworks that address transaction costs and market con-
ditions. Additionally, improving the robustness of CP methods, particularly
with respect to outliers and non-exchangeable time series, will be fundamental.
Exploring the application of CP models in renewable energy forecasting, smart
grid management, and real-time data streams presents a rich avenue for future
development, which will help to create more adaptable and reliable forecasting
systems in increasingly complex energy markets.
Acknowledgments
This work was conducted with the financial support of Science Foundation
Ireland under Grant Nos. 18/CRT/6223 and 12/RC/2289-P2 which are co-
funded under the European Regional Development Fund. For the purpose of
Open Access, the author has applied a CC BY public copyright licence to any
Author Accepted Manuscript version arising from this submission.
33

References
Angelopoulos, A., Candes, E., & Tibshirani, R. J. (2024). Conformal pid control
for time series prediction.Advances in neural information processing systems,
36.
Bhatnagar, M., Rozinaj, G., & Vargic, R. (2025). Using crafted features and
polar bear optimization algorithm for short-term electric load forecast system.
Energy and AI, (p. 100470).
Birkeland, D., & AlSkaif, T. (2024). Research areas and methods of interest in
european intraday electricity market research—a systematic literature review.
Sustainable Energy, Grids and Networks, (p. 101368).
Chen, Y., Wang, Y., Ma, J., & Jin, Q. (2019). Brim: An accurate electricity
spot price prediction scheme-based bidirectional recurrent neural network and
integrated market.Energies, 12, 2241.
Cheng, H., Ding, X., Zhou, W., & Ding, R. (2019). A hybrid electricity price
forecasting model with bayesian optimization for german energy exchange.
International Journal of Electrical Power & Energy Systems, 110, 653–666.
Cordier, T., Blot, V., Lacombe, L., Morzadec, T., Capitaine, A., & Brunel,
N. (2023). Flexible and systematic uncertainty estimation with conformal
prediction via the mapie library. InConformal and Probabilistic Prediction
with Applications. PMLR.
Dewolf, N., Baets, B. D., & Waegeman, W. (2023). Valid prediction intervals
for regression problems.Artificial Intelligence Review, 56, 577–613.
Dumas, J., Boukas, I., de Villena, M. M., Mathieu, S., & Cornélusse, B. (2019).
Probabilistic forecasting of imbalance prices in the belgian context. In2019
16th International Conference on the European Energy Market (EEM)(pp.
1–7). IEEE.
34

ElRobrini, F., Bukhari, S. M. S., Zafar, M. H., Al-Tawalbeh, N., Akhtar, N.,
& Sanfilippo, F. (2024). Federated learning and non-federated learning based
power forecasting of photovoltaic/wind power energy systems: A systematic
review. Energy and AI, (p. 100438).
Foygel Barber, R., Candes, E. J., Ramdas, A., & Tibshirani, R. J. (2022).
Conformal prediction beyond exchangeability. arXiv e-prints, (pp. arXiv–
2202).
Gammerman, A., Vovk, V., & Vapnik, V. (1998). Learning by transduction.
Proceedings of the 14th Conference on Uncertainty in Artificial Intelligence
(UAI), .
Ghosh, S., Shi, Y., Belkhouja, T., Yan, Y., Doppa, J., & Jones, B. (2023). Prob-
abilistically robust conformal prediction.Proceedings of the 39th Conference
on Uncertainty in Artificial Intelligence (UAI), 216, 681–690.
Hagfors, L. I., Bunn, D., Kristoffersen, E., Staver, T. T., & Westgaard, S.
(2016). Modeling the uk electricity price distributions using quantile regres-
sion. Energy, 102.
Hu, J., Luo, Q., Tang, J., Heng, J., & Deng, Y. (2022). Conformalized temporal
convolutionalquantileregressionnetworksforwindpowerintervalforecasting.
Energy, 248, 123497.
Ilea, V., Bovo, C. et al. (2018). European day-ahead electricity market coupling:
Discussion, modeling, and case study.Electric Power Systems Research, 155,
80–92.
Janczura, J. (2024). Expectile regression averaging method for probabilistic
forecasting of electricity prices.arXiv preprint arXiv:2402.07559, .
Jensen, V., Bianchi, F. M., & Anfinsen, S. N. (2022). Ensemble conformalized
quantile regression for probabilistic time series forecasting.IEEE Transac-
tions on Neural Networks and Learning Systems, .
35

Kath, C., & Ziel, F. (2021). Conformal prediction interval estimation and ap-
plications to day-ahead and intraday power markets.International Journal
of Forecasting, .
Khajeh, H., & Laaksonen, H. (2022). Applications of probabilistic forecasting
in smart grids: A review.Applied Sciences, .
Khosravi, A., Nahavandi, S., & Creighton, D. (2013). Quantifying uncertainties
of neural network-based electricity price forecasts.Applied energy, 112, 120–
129.
Klein, N., Smith, M. S., & Nott, D. J. (2023). Deep distributional time series
models and the probabilistic forecasting of intraday electricity prices.Journal
of Applied Econometrics, 38, 493–511.
Koch, C., & Hirth, L. (2019). Short-term electricity trading for system bal-
ancing: An empirical analysis of the role of intraday trading in balancing
germany’s electricity system. Renewable and Sustainable Energy Reviews,
113, 109275.
Koenker, R., & Bassett Jr, G. (1978). Regression quantiles. Econometrica:
journal of the Econometric Society, .
Kostrzewski, M., & Kostrzewska, J. (2019). Probabilistic electricity price fore-
casting with bayesian stochastic volatility models. Energy Economics, 80,
610–620.
Lago, J., De Ridder, F., & De Schutter, B. (2018). Forecasting spot electricity
prices: Deep learning approaches and empirical comparison of traditional
algorithms. Applied Energy, 221, 386–405.
Lago, J., Marcjasz, G., De Schutter, B., & Weron, R. (2021). Forecasting day-
ahead electricity prices: A review of state-of-the-art algorithms, best practices
and an open-access benchmark.Applied Energy, .
36

Lee, J., Xu, C., & Xie, Y. (2024). Transformer conformal prediction for time
series. arXiv preprint arXiv:2406.05332, .
Li, W., & Becker, D. M. (2021). Day-ahead electricity price prediction apply-
ing hybrid models of lstm-based deep learning methods and feature selection
algorithms under consideration of market coupling.Energy, 237, 121543.
Liu, H., Shen, X., Tang, X., & Liu, J. (2023). Day-ahead electricity price
probabilistic forecasting based on shap feature selection and lstnet quantile
regression. Energies, 16, 5152.
Liu, H., & Zhang, Z. (2025). Probabilistic forecasting of multiple plant day-
ahead renewable power generation sequences with data privacy preserving.
Energy and AI, 19, 100463.
Lucas, A., Pegios, K., Kotsakis, E., & Clarke, D. (2020). Price forecasting for
the balancing energy market using machine-learning regression.Energies, 13,
5420.
Maciejowska, K., & Nitka, W. (2024). Multiple split approach–
multidimensional probabilistic forecasting of electricity markets. arXiv
preprint arXiv:2407.07795, .
Maciejowska, K., Nowotarski, J., & Weron, R. (2016). Probabilistic forecasting
of electricity spot prices using factor quantile regression averaging.Interna-
tional Journal of Forecasting, 32, 957–965.
Marcjasz, G., Narajewski, M., Weron, R., & Ziel, F. (2023). Distributional
neural networks for electricity price forecasting. Energy Economics, 125,
106843.
Marcjasz, G., Uniejewski, B., & Weron, R. (2020). Probabilistic electricity price
forecasting with narx networks: Combine point or probabilistic forecasts?
International Journal of Forecasting, 36.
37

Mazzi, N., & Pinson, P. (2017). 10 - wind power in electricity markets and the
value of forecasting. In G. Kariniotakis (Ed.),Renewable Energy Forecasting.
Woodhead Publishing.
Miraki, A., Parviainen, P., & Arghandeh, R. (2025). Probabilistic forecast-
ing of renewable energy and electricity demand using graph-based denoising
diffusion probabilistic model.Energy and AI, 19, 100459.
Monjazeb, M. R., Amiri, H., & Movahedi, A. (2024). Wholesale electricity price
forecasting by quantile regression and kalman filter method.Energy, 290,
129925.
Monteiro, C., Ramirez-Rosado, I. J., Fernandez-Jimenez, L. A., & Ribeiro, M.
(2018). New probabilistic price forecasting models: Application to the iberian
electricity market. International Journal of Electrical Power & Energy Sys-
tems, 103, 483–496.
Narajewski, M. (2022). Probabilistic forecasting of german electricity imbalance
prices. Energies, 15.
Narajewski, M., & Ziel, F. (2020). Econometric modelling and forecasting of
intraday electricity prices.Journal of Commodity Markets, 19, 100107.
Newbery, D., Strbac, G., & Viehoff, I. (2016). The benefits of integrating euro-
pean electricity markets.Energy Policy, 94, 253–263.
Nowotarski, J., & Weron, R. (2015). Computing electricity spot price prediction
intervals using quantile regression and forecast averaging. Computational
Statistics, .
Nowotarski, J., & Weron, R. (2018). Recent advances in electricity price fore-
casting: A review of probabilistic forecasting. Renewable and Sustainable
Energy Reviews, .
O’Connor, C., Collins, J., Prestwich, S., & Visentin, A. (2024a). Electricity
price forecasting in the irish balancing market.Energy Strategy Reviews, 54.
38

O’Connor, C., Collins, J., Prestwich, S., & Visentin, A. (2024b). Optimizing
quantile-based trading strategies in electricity arbitrage.arXiv:2406.13851.
Ortner, A., & Totschnig, G. (2019). The future relevance of electricity balancing
markets in europe.Energy Strategy Reviews, 24, 111–120.
Piantadosi, G., Dutto, S., Galli, A., De Vito, S., Sansone, C., & Di Francia,
G. (2024). Photovoltaic power forecasting: A transformer based framework.
Energy and AI, 18, 100444.
Samarajeewa, C., De Silva, D., Manic, M., Mills, N., Moraliyage, H., Alahakoon,
D., & Jennings, A. (2024). An artificial intelligence framework for explainable
drift detection in energy forecasting.Energy and AI, 17, 100403.
Serinaldi, F. (2011). Distributional modeling and short-term forecasting of elec-
tricity prices by generalized additive models for location, scale and shape.
Energy Economics, 33, 1216–1226.
Shinde, P., & Amelin, M. (2019). A literature review of intraday electricity
markets and prices.2019 IEEE Milan PowerTech, (pp. 1–6).
De la Torre, J., Rodriguez, L. R., Monteagudo, F. E., Arredondo, L. R., &
Enriquez, J. B. (2024). Electricity price forecast in wholesale markets using
conformal prediction: Case study in mexico.Energy Science & Engineering,
.
Trebbien, J., Pütz, S., Schäfer, B., Nygård, H. S., Gorjão, L. R., & Witthaut,
D. (2023). Probabilistic forecasting of day-ahead electricity prices and their
volatility with lstms. In2023 IEEE PES Innovative Smart Grid Technologies
Europe (ISGT EUROPE)(pp. 1–5). IEEE.
Ugurlu, U., Oksuz, I., & Tas, O. (2018). Electricity price forecasting using
recurrent neural networks.Energies, 11, 1255.
Uniejewski, B. (2023). Smoothing quantile regression averaging: A new ap-
proach to probabilistic forecasting of electricity prices. arXiv:2302.00411,
.
39

Uniejewski, B., Marcjasz, G., & Weron, R. (2019a). On the importance of the
long-term seasonal component in day-ahead electricity price forecasting: Part
ii—probabilistic forecasting. Energy Economics, 79, 171–182.
Uniejewski, B., Marcjasz, G., & Weron, R. (2019b). Understanding intraday
electricity markets: Variable selection and very short-term price forecasting
using lasso. International Journal of Forecasting, 35, 1533–1547.
Uniejewski, B., & Weron, R. (2021). Regularized quantile regression averaging
for probabilistic electricity price forecasting.Energy Economics, 95.
Vahidinasab, V., & Jadid, S. (2010). Bayesian neural network model to predict
day-ahead electricity prices.European Transactions on Electrical Power, 20,
231–246.
Vovk, V., Gammerman, A., & Shafer, G. (2005). Algorithmic learning in a
random worldvolume 29. Springer.
Xu, C., Jiang, H., &Xie, Y.(2024a). Conformalpredictionformulti-dimensional
time series by ellipsoidal sets.arXiv preprint arXiv:2403.03850, .
Xu, C., & Xie, Y. (2021). Conformal prediction interval for dynamic time-series.
InInternational Conference on Machine Learning(pp. 11559–11569). PMLR.
Xu, C., & Xie, Y. (2023). Sequential predictive conformal inference for time
series. In International Conference on Machine Learning(pp. 38707–38727).
PMLR.
Xu, Y., Li, J., Wang, H., & Du, P. (2024b). A novel probabilistic forecast-
ing system based on quantile combination in electricity price.Computers &
Industrial Engineering, 187, 109834.
Yasuda, Y., Bird, L., Carlini, E. M., Eriksen, P. B., Estanqueiro, A., Flynn,
D., Fraile, D., Lázaro, E. G., Martín-Martínez, S., Hayashi, D. et al. (2022).
Ce (curtailment–energy share) map: An objective and quantitative measure
40

to evaluate wind and solar curtailment.Renewable and Sustainable Energy
Reviews, .
Yuanchen, W., Yizhi, H., Tong, G., Lei, D., Ying, W., & Wenbin, X. (2023).
Electricity price forecasting based on bayesian network and monte carlo sim-
ulation. In 2023 IEEE 6th International Conference on Automation, Elec-
tronics and Electrical Engineering (AUTEEE)(pp. 542–546). IEEE.
Zachmann, G., Hirth, L., Heussaff, C., Schlecht, I., Mühlenpfordt, J., & Eicke,
A. (2023). The design of the european electricity market–current proposals
and ways ahead.European Parliament: Luxembourg, .
Zaffran, M., Féron, O., Goude, Y., Josse, J., & Dieuleveut, A. (2022). Adaptive
conformal predictions for time series. InInternational Conference on Machine
Learning (pp. 25834–25866). PMLR.
Zhao, C., Wan, C., & Song, Y. (2019). An adaptive bilevel programming model
for nonparametric prediction intervals of wind power generation.IEEE Trans-
actions on Power Systems, 35, 424–439.
Ziel, F., & Steinert, R. (2018). Probabilistic mid-and long-term electricity price
forecasting. Renewable and Sustainable Energy Reviews, 94, 251–266.
Declaration of generative AI and AI-assisted technologies in the writ-
ing process
During the preparation of this work, the authors used ChatGPT to improve
the paper’s readability. After using this tool/service, the authors reviewed and
edited the content as needed and take full responsibility for the content of the
publication.
41
