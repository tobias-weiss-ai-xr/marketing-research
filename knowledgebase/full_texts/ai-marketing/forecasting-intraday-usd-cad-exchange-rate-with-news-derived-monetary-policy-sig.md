---
title: Forecasting Intraday USD/CAD Exchange Rate with News-Derived Monetary-Policy Signals
url: https://arxiv.org/abs/2609.32773
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Maya Kodeih
- Aliaa Alnaggar
- Mucahit Cevik
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.32773
pages: 10
chars: 54230
fetched_at: '2026-11-08T13:24:47+00:00'
kb_version: 1
---

# Forecasting Intraday USD/CAD Exchange Rate with News-Derived Monetary-Policy Signals

Forecasting Intraday USD/CAD Exchange Rate
with News-Derived Monetary-Policy Signals
Maya Kodeih∗, Aliaa Alnaggar ∗, Mucahit Cevik ∗
∗Department of Mechanical and Industrial Engineering, Toronto Metropolitan University, Toronto, ON, Canada
Abstract—Monetary-policy announcements and central-bank
communications play a central role in foreign exchange markets,
yet their qualitative, unstructured form makes their forecasting
value difficult to quantify. While prior research has largely
focused on sentiment extracted from financial news, compara-
tively little is known about the relative contribution of different
dimensions of monetary-policy communication. Existing studies
primarily evaluate whether textual information improves overall
forecasting performance but provide limited insight into which
communication channels drive such improvements. To address
this gap, this paper introduces a statistical attribution method-
ology that decomposes monetary-policy communication into in-
terpretable channels and quantifies their incremental forecasting
contribution under false-discovery-rate control. Monetary-policy
news is transformed into structured communication signals using
large language models (LLMs) and temporal feature engineering.
These signals are evaluated using rolling-window experiments
with tree-based machine-learning models. The results show that
monetary-policy communication contains measurable predictive
information. Attribution analysis shows that predictive value is
concentrated in a small subset of signals, with communication
timing providing the strongest individual feature-level contribu-
tion, targeted communication-activity measures also contributing
positively, and LLM-derived sentiment providing complemen-
tary information at the group level. The findings indicate that
communication-based forecasting value extends beyond sentiment
alone and that attribution, rather than aggregate accuracy alone,
is central to evaluating news-derived signals.
Index Terms—Foreign exchange forecasting, financial news
analytics, feature attribution, ablation analysis, time series.
I. INTRODUCTION
Financial news and central-bank communications play an
important role in shaping expectations in foreign exchange
(FX) markets. Monetary-policy announcements, policy guid-
ance, and macroeconomic news influence exchange rates by
affecting expectations regarding future interest rates, inflation,
and economic conditions [1, 2]. Consequently, researchers
have increasingly incorporated textual information into FX
forecasting systems to complement traditional economic and
market-based predictors [3, 4, 5]. Recent advances in machine
learning and financial natural language processing have ex-
panded the methodologies available for financial forecasting.
Previous work has used tree-based ensembles to capture
nonlinear structure in financial time series and large language
models (LLMs) to interpret financial text beyond dictionary-
based sentiment [6, 7, 8, 9]. Despite these advances, existing
Corresponding author(s): M. Kodeih (email: mkodeih@torontomu.ca),
A. Alnaggar (email: aliaa.alnaggar@torontomu.ca), M. Cevik (email: mce-
vik@torontomu.ca).
studies have primarily evaluated textual information through
its effect on aggregate forecasting accuracy [3, 4, 10]. While
such studies suggest that financial news contains predictive
value, comparatively little attention has been devoted to under-
standing which dimensions of monetary-policy communication
drive forecasting improvements.
Modern forecasting systems often combine sentiment scores
with communication activity, policy classifications, news-
arrival indicators, temporal persistence measures, and other
engineered representations derived from central-bank commu-
nications [5, 7, 8, 9]. As these feature sets grow more com-
plex, it becomes increasingly difficult to determine whether
predictive gains originate from sentiment itself, communica-
tion timing, communication frequency, policy stance, or a
relatively small subset of engineered communication signals.
Although interpretable machine learning has emphasized the
importance of feature attribution and model interpretation
[11, 12, 13], systematic empirical evaluation of the relative
forecasting value of different dimensions of monetary-policy
communication remains limited in FX forecasting. We address
this gap by developing a methodology for attributing the
forecasting value of monetary-policy communication in in-
traday USD/CAD exchange-rate forecasting. Federal Reserve
and Bank of Canada news articles are transformed into struc-
tured communication signals using an LLM-based sentiment-
labeling pipeline and temporal feature engineering. The re-
sulting feature set captures several dimensions of monetary-
policy communication, including sentiment, communication
activity, communication timing, policy stance, and informa-
tion persistence. These signals are evaluated using rolling-
window forecasting experiments, benchmark comparisons,
feature-level and group-level attribution analysis, and false-
discovery-rate (FDR)-controlled statistical testing. Rather than
asking whether sentiment alone improves forecasting perfor-
mance, the proposed methodology identifies which dimensions
of monetary-policy communication provide measurable and
statistically supported forecasting value. Accordingly, the prin-
cipal methodological contribution is a statistically controlled
attribution framework for identifying which dimensions of
monetary-policy communication provide incremental forecast-
ing information beyond aggregate predictive performance.
The contributions of this paper are as follows:
•We present an end-to-end methodology for transforming
monetary-policy communications into structured forecast-
ing signals using LLM-based sentiment extraction and
arXiv:2609.32773v1  [cs.AI]  26 Sep 2026

temporal feature engineering spanning sentiment, com-
munication timing, communication activity, policy stance,
and information persistence.
•We combine rolling-window forecasting, benchmark
comparison, feature-level and group-level attribution
analysis, and FDR-controlled statistical testing to quantify
the forecasting contribution of individual communication
signals.
•We provide an empirical analysis showing that the fore-
casting value of monetary-policy communication is con-
centrated within a small subset of engineered features,
with communication timing providing the largest individ-
ual feature-level contribution, targeted communication-
activity and non-neutral policy signals also contributing
positively, and LLM-derived sentiment providing comple-
mentary predictive information at the group level.
II. LITERATUREREVIEW
Foreign exchange forecasting remains one of the most chal-
lenging problems in finance because exchange rates are influ-
enced by complex interactions among macroeconomic funda-
mentals, market expectations, and rapidly evolving information
flows. Traditional forecasting approaches rely on economic
relationships such as purchasing power parity, interest-rate
differentials, and monetary fundamentals to explain exchange-
rate movements [14]. Despite decades of research, exchange-
rate prediction remains difficult, and many economic models
have struggled to consistently outperform naive random-walk
benchmarks [14, 15].
Recent advances in machine learning have expanded the
range of forecasting approaches beyond traditional econo-
metric models. Tree-based ensemble methods, including Ran-
dom Forests, XGBoost, and LightGBM, have been used to
model nonlinear relationships among financial variables and
have been applied to exchange-rate forecasting [16, 17].
Recent USD/CAD forecasting studies have further shown
that machine-learning models combined with interpretability
techniques can extract information from macroeconomic and
financial variables such as oil prices, interest rates, equity
indices, producer prices, monetary aggregates, unemployment,
and industrial production [18]. However, these studies focus
primarily on structured macro-financial variables at daily and
weekly frequencies rather than intraday textual information or
central-bank communications.
Financial news provides an additional source of information
that may influence market expectations before it is fully
reflected in prices. Numerous studies have incorporated news
and sentiment indicators into forecasting models for equi-
ties, commodities, and foreign exchange markets [3, 4, 5].
Central-bank communications are particularly relevant because
they convey forward-looking information regarding future
monetary-policy actions and can therefore influence exchange-
rate expectations before formal policy decisions are imple-
mented [1, 2]. To incorporate textual information into quan-
titative forecasting systems, researchers commonly transform
financial text into sentiment scores, topic representations, or
policy-stance classifications. More recently, domain-specific
LLMs, including FinBERT, BloombergGPT, and FinGPT, have
expanded the ability to extract contextual information from
financial communications and have been applied to financial
sentiment analysis and market prediction tasks [7, 8, 9, 19].
As forecasting models become increasingly sophisticated,
understanding why models perform well has become an
important research objective. Interpretable machine-learning
techniques such as permutation importance, SHAP, and feature
ablation provide complementary approaches for assessing the
contribution of individual predictors and distinguishing infor-
mative variables from redundant or noisy features [11, 12, 13].
In financial forecasting applications, however, these methods
are typically used to explain model behaviour after training
rather than to systematically quantify the forecasting value
of different categories of engineered communication signals
under formal statistical inference. Consequently, an attribution
gap remains. Existing studies generally compare forecasting
systems with and without textual information, providing lim-
ited insight into whether predictive improvements arise from
sentiment itself, communication timing, communication activ-
ity, policy stance, temporal persistence, or other engineered
representations derived from central-bank communications.
In contrast to prior USD/CAD work on daily and weekly
macro-financial variables [18], we study intraday forecasting
from news- and LLM-derived central-bank communication
signals. Beyond point forecasting, we evaluate directional and
probabilistic forecasts and attribute predictive value to individ-
ual communication channels through feature- and group-level
ablation with FDR control.
III. METHODOLOGY
We develop an integrated methodology for assessing the
forecasting value of monetary-policy communication in the
USD/CAD foreign-exchange market. The objective is channel-
level attribution rather than aggregate accuracy alone. The
methodology consists of seven stages: (1) data collection
and preprocessing, (2) LLM-based monetary-policy sentiment
extraction, (3) temporal communication-signal engineering, (4)
deterministic forecasting and benchmark evaluation, (5) prob-
abilistic forecasting and uncertainty estimation, (6) feature-
level and group-level attribution analysis, and (7) statistical
significance testing. Figure 1 summarizes the overall workflow.
A. Data Collection and Processing
Financial news articles were collected from financial news
providers and real-time RSS feeds covering macroeconomic
developments, monetary-policy decisions, inflation releases,
labour-market conditions, and central-bank communications.
Because the objective is to evaluate the forecasting value of
monetary-policy information, a filtering stage was applied to
retain only articles relevant to monetary-policy expectations.
The empirical sample spans 2024-06-13 to 2026-06-12.
After filtering and duplicate removal, the final dataset con-
tains 927 monetary-policy-related articles aligned with 17,517

Data Collection
and Preprocessing
LLM-Based Sentiment
Extraction
Communication-Signal
Engineering
Forecasting Tasks
Deterministic and Benchmark
Directional
Probabilistic and Uncertainty
Feature- and Group-Level
Attribution
Bootstrap Con-
fidence Intervals
and FDR Testing
Statistically Supported
Communication-
Signal Attribution
Fig. 1: Overview of the proposed monetary-policy communication forecasting and attribution workflow.
hourly USD/CAD observations. Exchange-rate data were ob-
tained from Yahoo Finance, while news articles were col-
lected through TheNewsAPI with RSS-feed aggregation. The
USD/CAD series was aligned to a continuous hourly grid;
missing observations, including those during weekend market
closures, were forward-filled using the most recent available
exchange rate, while any observations provided by Yahoo
Finance were retained. Rolling-window evaluation employs
an 85/15 train–test split within each window, corresponding
to approximately 4,324 training observations and 764 out-
of-sample observations, with slightly smaller windows at the
beginning of the sample.
Articles were filtered using a monetary-policy vocabulary
covering the Federal Reserve, the Bank of Canada, interest
rates, inflation, forward guidance, quantitative easing and
tightening, and related macroeconomic concepts. Duplicate
and near-duplicate articles were removed, and retained articles
were timestamped and aggregated to an hourly frequency to
align news-derived features with intraday USD/CAD observa-
tions.
B. Monetary-Policy Sentiment Extraction
Each filtered article was processed using an LLM to extract
monetary-policy sentiment. Sentiment labeling was performed
using OpenAI GPT-4o-mini, which classified the implied
monetary-policy stance of each article ashawkish,dovish,neu-
tral, ormixed. Federal Reserve-related and Bank of Canada-
related communications were labeled separately, enabling the
construction of institution-specific sentiment measures and
policy-divergence signals.
To assess labeling reliability, a random sample of 100
monetary-policy-related articles was manually reviewed and
compared with the corresponding LLM classifications. The
manual assessment indicated that the generated labels were
generally consistent with the monetary-policy stance expressed
in the underlying articles within this validation sample. As
an additional qualitative validation, periods containing non-
neutral central-bank communications were examined using an
exploratory event-study analysis. Exchange-rate movements
observed around these events were often directionally con-
sistent with the direction implied by the extracted communi-
cation signals, providing diagnostic evidence that the labeling
pipeline captured economically meaningful information. The
article-level sentiment labels were subsequently aggregated to
an hourly frequency and transformed into forecasting features,
including sentiment differentials, non-neutral communication
indicators, sentiment-persistence measures, and rolling senti-
ment summaries over multiple lookback windows.
C. Feature Engineering
Article-level sentiment observations were transformed into
hourly communication signals representing multiple dimen-
sions of monetary-policy information. The engineered fea-
ture set includes sentiment-derived variables, communication
timing and activity measures, temporal persistence indicators,
and conventional market variables, which are summarized in
Table I.
TABLE I: Feature categories used in the forecasting methodology.
Category Examples
Sentiment Fed sentiment, BoC sentiment, sentiment dif-
ferential
News Activity News-hour indicators, non-neutral communi-
cation events
Communication V olume Fed article counts, BoC article counts, total
article volume
Temporal Impulse variables, decay features, rolling sen-
timent measures
Market USD/CAD lags, technical indicators, volatility
measures
Representative engineered variables include rolling com-
munication counts (e.g.,fed_articles_24h), news-arrival
indicators (e.g.,is_news_hour), sentiment-differential
measures, impulse and decay features, and rolling sentiment
summaries computed over multiple lookback windows. Ad-
ditional market variables comprise USD/CAD lags, intraday
volatility, the normalized U.S.–Canada interest-rate spread,
macroeconomic momentum measures, and WTI crude oil
prices.
A central feature used throughout the analysis is the
monetary-policy sentiment differential between the Federal
Reserve and the Bank of Canada:
SDt =S F ed t −S BoC t ,(1)
whereS F ed t andS BoC t denote the corresponding central-
bank sentiment measures at timet. To capture immediate

information-arrival effects, sentiment impulse variables were
constructed as
It =
(
SDt,if a policy-related article arrives at timet,
0,otherwise.
(2)
The persistence of monetary-policy information was modeled
using exponentially decaying sentiment variables:
Dt =SD t exp(−λ∆t),(3)
where∆tdenotes elapsed time since publication andλcon-
trols the decay rate.
Rolling sentiment indicators were constructed using multi-
ple lookback windows:
RS(k) t = 1 k
k−1X
i=0
SDt−i,(4)
wherekdenotes the rolling-window length.
D. Forecasting Models
Tree-based ensemble models were employed throughout
the forecasting framework because of their ability to capture
nonlinear relationships, higher-order feature interactions, and
complex dependencies without requiring strong distributional
assumptions. The evaluated models were Extra Trees (ETR),
XGBoost, and LightGBM.
For deterministic forecasting, separate regression models
were trained independently for each forecasting horizon. This
direct forecasting strategy avoids recursive error propagation
by estimating an individual model for each prediction horizon.
For a forecasting horizon ofhhours, the models predict
the future USD/CAD exchange-rate level,ˆy t+h, using only
information available at timet. The same model families were
also used for directional classification, where the objective is
to estimate the probability of upward or downward USD/CAD
movements over each forecasting horizon. Probabilistic fore-
casting extends the deterministic models through quantile
regression, with conformal calibration evaluated separately
as a post-processing procedure. Details of the probabilistic
evaluation are provided in Section III-F.
Forecasting performance is evaluated relative to two bench-
mark strategies. The first is a naive moving-average predictor
computed from the three most recent observations within each
rolling training window. The second is the no-change random-
walk forecast,ˆy t+h =y t, which serves as the principal
benchmark because of the strong persistence exhibited by
exchange-rate levels. These benchmarks contextualize level-
forecast accuracy; the paper’s main objective remains attribu-
tion rather than benchmark dominance.
E. Directional Forecast Evaluation
We also evaluate whether monetary-policy communication
helps predict the direction of future USD/CAD movements.
For a forecast horizon ofhhours, the directional target is
defined as
dt+h =
(
1,ify t+h −y t >0,
0,otherwise. (5)
wherey t denotes the USD/CAD exchange-rate level at time
t. Classification models estimate the probability of an upward
movement, which is converted into a binary prediction using
a decision threshold.
Performance is evaluated using directional accuracy (DA),
balanced accuracy, macro F1-score, and the area under the
receiver operating characteristic curve (AUC). Because the di-
rectional target exhibits class imbalance, results are compared
with two benchmark strategies:
•Majority-class baseline: always predicts the most fre-
quently observed directional class.
•Persistence baseline: predicts that the future direction will
equal the most recently observed direction.
Reporting benchmark-relative performance together with bal-
anced accuracy helps distinguish whether directional improve-
ments reflect predictive signal rather than class imbalance or
simple persistence.
F . Probabilistic Forecast Evaluation
Deterministic forecasting produces a single estimate of the
future USD/CAD exchange-rate level but does not quantify
the uncertainty associated with that prediction. To characterize
predictive uncertainty, the deterministic forecasting framework
was extended to estimate conditional prediction intervals using
probabilistic forecasting.
Three probabilistic forecasting approaches were evaluated.
LightGBM and XGBoost employ native quantile-regression
objectives to estimate conditional quantiles directly, while
Extra Trees estimates empirical conditional quantiles from the
distribution of predictions across ensemble members. Multiple
quantile levels were estimated to construct prediction intervals
across all forecasting horizons.
To distinguish probabilistic forecasting quality from interval
calibration, the primary comparison is performed using the
uncalibrated quantile forecasts. Probabilistic performance is
evaluated using pinball loss, weighted interval score (WIS),
and empirical prediction-interval coverage, which assess quan-
tile accuracy, overall probabilistic forecast quality, and inter-
val calibration, respectively. Conformal calibration is evalu-
ated separately as a post-processing procedure using held-
out calibration residuals and is not included in the feature-
specification comparison reported in Table III.
G. Feature Attribution Analysis
To quantify the contribution of individual communica-
tion signals, forecasting performance was evaluated using a
sequential feature-ablation procedure. Unlike model-specific
feature-importance measures, which describe how a fitted
model uses available predictors, feature ablation measures the
change in out-of-sample forecasting performance after system-
atically removing information from the forecasting system.

This approach estimates the incremental predictive value of
each feature under the full forecasting pipeline. Consequently,
variables that appear highly important within a fitted model
may contribute little incremental forecasting information once
correlated communication signals are available, whereas vari-
ables with modest model importance may provide unique
predictive value. This distinction motivates the cumulative
ablation approach adopted in this study.
Beginning with the full feature set, features were removed
sequentially according to a predefined ordering. After each
removal, the forecasting models were retrained and evaluated
using the same rolling-window experimental design. The per-
formance difference between consecutive ablation steps esti-
mates the marginal contribution of the removed feature while
allowing downstream feature interactions to adjust following
retraining.
To complement the feature-level analysis, related variables
were grouped into broader feature groups, including commu-
nication timing, communication activity, sentiment, temporal
persistence, policy stance, and conventional market variables.
Group-level ablation evaluates the collective contribution of
each feature group by jointly removing all features within
the corresponding category and comparing forecasting perfor-
mance with the baseline model.
The primary attribution metric is the degradation in out-
of-sample forecasting performance relative to the preceding
ablation step. Positive degradation indicates that the removed
feature or feature group contributed useful predictive informa-
tion, whereas negligible changes suggest redundancy. Negative
degradation indicates that removing the feature improves fore-
casting performance, implying that the corresponding infor-
mation is redundant or detrimental within the forecasting sys-
tem. Feature-level attribution provides fine-grained estimates
of the contribution of individual engineered variables, while
group-level attribution characterizes the relative importance of
broader feature groups.
H. Statistical Significance Testing
We test each ablation effect with bootstrap confidence
intervals and Benjamini–Hochberg false-discovery-rate (FDR)
correction. For each feature-level and group-level ablation
experiment, rolling-window performance differences were re-
sampled using nonparametric bootstrap procedures to estimate
the sampling distribution of the attribution metric. Bootstrap
confidence intervals were then computed for each feature and
feature group.
Because multiple hypothesis tests were performed simul-
taneously, statistical significance was evaluated using the
Benjamini–Hochberg false-discovery-rate procedure [20]. For
feature-level attribution, the global FDR adjustment applies
the Benjamini–Hochberg procedure across the two-sided p-
values of all individual feature-ablation hypotheses, where
each feature-level p-value is computed from its pooled step-
wise∆R 2 observations across the evaluated model-horizon
combinations. This approach controls the expected proportion
of false discoveries while providing greater statistical power
than traditional family-wise error-rate corrections.
Features were considered statistically supported only when
both conditions were satisfied:
•the bootstrap confidence interval excluded zero; and
•the corresponding FDR-adjustedq-value satisfied the
predefined significance threshold.
Applying these criteria makes the reported attribution effects
more conservative after accounting for multiple comparisons.
Consequently, the analysis identifies communication signals
that show consistent predictive contributions across rolling
forecasting windows while reducing the likelihood of false-
positive discoveries.
I. Experimental Design
Experiments were conducted using a benchmark-aware
rolling-window evaluation designed to simulate realistic fore-
casting conditions. For each evaluation window, models were
trained using historical observations and evaluated on subse-
quent out-of-sample data, so every prediction was generated
using only information available at the forecasting time, avoid-
ing look-ahead bias.
The experimental design comprises three complementary
prediction tasks. The primary task forecasts future USD/CAD
exchange-rate levels using deterministic regression models and
forms the basis of the feature-level and group-level attribution
analyses. The second task evaluates predictive uncertainty
through probabilistic forecasting by estimating conditional
prediction intervals. The third task investigates directional
predictability using a binary-classification framework.
Forecast horizons of 1, 3, 8, and 24 hours were evalu-
ated to capture both immediate and persistent communication
effects. Deterministic forecasting was assessed using Root
Mean Squared Error (RMSE), Mean Absolute Percentage
Error (MAPE), and the coefficient of determination (R2), prob-
abilistic forecasting using quantile and interval-based scoring
metrics, and directional forecasting using standard classifi-
cation metrics together with majority-class and persistence
benchmarks.
Feature-level and group-level attribution analyses are per-
formed using deterministic point forecasts to quantify the
incremental contribution of individual communication signals.
Probabilistic forecasting is evaluated separately to determine
whether the communication hierarchy identified through deter-
ministic attribution remains consistent under uncertainty-aware
forecasting.
All experiments were implemented in Python using pub-
licly available machine-learning libraries. Data preprocessing
employedpandasandNumPy, while model development
usedscikit-learn,LightGBM, andXGBoost. LLM
sentiment extraction was performed using the OpenAI GPT-
4o-mini API.
To support reproducibility, a fixed random seed was used
for all experiments. Model hyperparameters remained constant
across rolling-window evaluations, with only the training and
testing data changing as the evaluation window advanced.

All forecasting experiments followed the same pre-
processing pipeline, feature-engineering procedure, rolling-
window evaluation protocol, benchmark comparisons, attribu-
tion methodology, and statistical testing framework. Perfor-
mance metrics were computed using identical evaluation pro-
cedures across all forecasting horizons and model configura-
tions to allow a fair comparison of deterministic, probabilistic,
and directional forecasting results.
IV. RESULTS
This section reports deterministic, probabilistic, and direc-
tional forecasting results as well as the attribution outcomes.
A. Forecasting Performance Across Horizons
We first use level forecasts to contextualize model fit and
support the subsequent attribution analysis. Across various
forecast horizons, the models achieve high out-of-sampleR 2
(0.844–0.915; Table II), highest at the 1-hour horizon (Light-
GBM Direct) and declining at longer horizons (Extra Trees
Direct). Although these results show high predictive power,
they should be interpreted relative to the no-change random-
walk benchmark, which has long served as the principal
reference model in foreign-exchange forecasting. Table II
compares the best-performing machine-learning model at each
horizon with the corresponding random-walk forecast using
normalized RMSE, andR 2.
TABLE II: Benchmark comparison for level forecasting.
Horizon Best ML Model RW
R2 NRMSER 2 NRMSE
1h 0.9150 0.00549 0.9988 0.00065
3h 0.9039 0.00584 0.9967 0.00109
8h 0.8886 0.00628 0.9916 0.00173
24h 0.8442 0.00742 0.9764 0.00289
Consistent with the longstanding foreign-exchange forecast-
ing literature, none of the evaluated machine-learning models
outperforms the no-change random walk on level-based fore-
casting metrics. Across all horizons, NRMSE remains higher
than the corresponding random-walk error, and the benchmark
achieves higherR 2 values. Benchmark-relative performance
nonetheless improves with horizon and the relative perfor-
mance gap narrows as exchange-rate persistence weakens over
longer horizons. While this benchmark result limits claims
about level-forecast dominance, it does not preclude attribution
within the fitted models.
Figure 2 summarizes the evolution of level-forecasting error
throughout the cumulative feature-ablation sequence across the
four forecasting horizons. The largest changes occur during
the early ablation steps, where several weak or redundant
sentiment and directional representations are removed. For
the tree-based forecasting models, RMSE generally decreases
after these removals, particularly at the 1-hour and 3-hour
horizons, indicating that the full feature set contains variables
that reduce forecasting efficiency when combined with the
more informative communication-timing and communication-
activity signals.
At longer horizons, model responses are more heteroge-
neous. Extra Trees remains comparatively stable throughout
the ablation sequence, whereas the boosting models become
increasingly sensitive to cumulative feature removal. These re-
sults suggest that the contribution of individual communication
signals depends not only on the forecasting horizon but also
on the interaction among the remaining engineered features.
B. Probabilistic Forecasting Results
To evaluate whether the communication hierarchy identified
through deterministic attribution also improves uncertainty-
aware forecasting, Table III compares the full feature set with
the Step 7 communication-aware specification using uncal-
ibrated quantile forecasts. The comparison uses LightGBM
quantile regression for the Step 7 models and the strongest
full-feature probabilistic model at each forecasting horizon.
Conformal calibration is evaluated separately and is therefore
not reflected in the coverage values reported in Table III.
Across all forecasting horizons, the empirical prediction
intervals are under-covered relative to their nominal confidence
levels. Coverage of the nominal 50% intervals ranges from
30.85% to 44.01%, while coverage of the nominal 90%
intervals ranges from 53.72% to 63.23%. These results indicate
that the uncalibrated prediction intervals are systematically
too narrow, motivating the separate evaluation of conformal
calibration as a post-processing procedure.
TABLE III: Full-feature versus Step 7 probabilistic forecasting per-
formance using uncalibrated quantile forecasts. Lower pinball loss
and WIS indicate better probabilistic performance; Cov90 reports
empirical coverage of the nominal 90% interval before conformal
calibration.
H Pinball Loss WIS Cov90 (%)
Full Step 7 Full Step 7 Full Step 7
1h 0.003329 0.001479 0.002394 0.001062 53.72 68.92
3h 0.003731 0.001989 0.002682 0.001429 63.23 58.47
8h 0.004001 0.002829 0.002877 0.002032 61.85 50.88
24h 0.004600 0.004102 0.003308 0.002946 57.85 46.29
The Step 7 specification consistently improves the proba-
bilistic scoring rules across all forecasting horizons. Relative
to the full feature set, pinball loss decreases by approximately
55.6% at the 1-hour horizon, 46.7% at the 3-hour horizon,
29.3% at the 8-hour horizon, and 10.8% at the 24-hour
horizon. Weighted interval score exhibits a similar pattern,
indicating that the feature-removal sequence identified through
deterministic attribution also improves probabilistic forecast-
ing performance. Thus, the ablation hierarchy is informative
for probabilistic scoring as well as point forecasting.
The interpretation, however, requires an important qualifi-
cation. Although Step 7 reduces pinball loss and WIS, it does
not uniformly improve empirical interval coverage. Coverage
of the nominal 90% interval increases from 53.72% to 68.92%
at the 1-hour horizon but decreases at the longer forecasting
horizons. Consequently, the Step 7 models produce sharper
and better-scoring probabilistic forecasts under proper scoring

Fig. 2: Mean RMSE across the cumulative ablation sequence at the 1-, 3-, 8-, and 24-hour horizons. Lower values indicate better forecasting
performance. Step 0 is the full feature set; each subsequent step removes one feature.
rules, but they also become less conservative as the forecasting
horizon increases.
Figure 3 illustrates these differences across forecast hori-
zons. At the 1-hour horizon, the median forecast closely fol-
lows the observed USD/CAD exchange rate, and the prediction
intervals capture much of the short-term variation. By the 24-
hour horizon, the median forecast responds less effectively
to rapid market movements, and observed values fall outside
the prediction intervals more frequently. This behaviour is
consistent with the reduced empirical coverage reported in
Table III and reflects the increasing uncertainty associated with
longer forecasting horizons.
C. Directional Forecasting Performance
Directional forecasting tests whether communication fea-
tures are more informative for market direction than for precise
price levels. Table IV summarizes the strongest directional-
classification results across the four forecasting horizons.
In addition to directional accuracy (DA), the evaluation in-
cludes majority-class and persistence benchmarks together
with balanced accuracy, macro F1-score, and the area un-
der the receiver operating characteristic curve (AUC). These
complementary metrics provide a more balanced assessment
because the directional target exhibits varying degrees of class
imbalance across forecasting horizons.
TABLE IV: Directional forecasting performance relative to bench-
mark strategies.
Horizon DA (%) Majority (%) Persistence (%) Balanced Acc. Macro F1 AUC
1 hour 66.08 63.05 62.61 0.721 0.660 0.744
3 hours 65.12 61.54 61.57 0.698 0.651 0.729
8 hours 66.55 57.80 61.51 0.705 0.658 0.707
24 hours 63.22 51.14 57.70 0.626 0.604 0.634
The directional target is moderately imbalanced at the
shorter forecasting horizons. At the 1-hour horizon, the out-
of-sample test set contains 939 upward movements and
1,602 downward movements, corresponding to a majority-
class benchmark accuracy of 63.05%. The corresponding
class distributions at the 3-, 8-, and 24-hour horizons are
38.46%/61.54%, 42.20%/57.80%, and 51.14%/48.86%, re-
spectively. Consequently, directional accuracy is interpreted
relative to both the majority-class and persistence benchmarks.
Across all horizons, the directional models exceed both
benchmark strategies. Directional accuracy ranges from
63.22% to 66.55%, outperforming the majority-class bench-
mark by approximately 3.0 percentage points at the 1-hour
horizon, 3.6 percentage points at the 3-hour horizon, 8.7
percentage points at the 8-hour horizon, and 12.1 percentage
points at the 24-hour horizon. Although absolute directional
accuracy changes only modestly across horizons, benchmark-
relative improvements become progressively larger, indicating
that monetary-policy communication retains predictive infor-
mation even as exchange-rate persistence weakens.
Figure 4 shows the evolution of directional accuracy
throughout the cumulative feature-ablation sequence. The
largest changes occur during the early ablation steps, after
which performance remains comparatively stable. These re-
sults indicate that the removal of a small number of engi-
neered communication features has a much greater influence
on directional performance than subsequent feature removals.
The magnitude and direction of these changes vary across
forecasting models and horizons, indicating that cumulative
ablation effects depend on both the remaining feature set and
the forecasting model rather than representing fixed measures
of feature importance.
Balanced accuracy ranges from 0.626 to 0.721, above the
0.50 value expected from random directional classification.
The strongest balanced-accuracy performance is observed at
the 1-hour horizon, while meaningful class discrimination is
maintained even at the 24-hour horizon. Similarly, macro F1-
scores between 0.604 and 0.660 indicate balanced precision
and recall across both directional classes, and AUC values
ranging from 0.634 to 0.744 indicate consistent discriminatory
ability across alternative decision thresholds. These comple-
mentary metrics indicate that the observed improvements are
not attributable to class imbalance alone but reflect directional
signal from the engineered monetary-policy communication
features. Taken together with the level-forecast benchmark
results, these findings suggest that the engineered monetary-
policy communication features may be more useful for predict-
ing market direction than for improving precise exchange-rate
level forecasts in this setting.
D. Feature-Level Attribution Results
We next examine which engineered communication fea-
tures drive forecasting performance. Feature-level cumulative
ablation quantifies the incremental contribution of each fea-

20-05-26 22-05-26 24-05-26 26-05-26 28-05-26 30-05-26 01-06-26
Time
1.374
1.376
1.378
1.380
1.382
1.384
1.386
1.388USD/CAD exchange rate
Probabilistic Forecast Intervals - LGBM_Quantile - h=1
90% interval (q05-q95)
50% interval (q25-q75)
Actual USD/CAD
Median forecast (q50)
(a) 1-hour forecast horizon
20-05-26 22-05-26 24-05-26 26-05-26 28-05-26 30-05-26 01-06-26
Time
1.3700
1.3725
1.3750
1.3775
1.3800
1.3825
1.3850
1.3875USD/CAD exchange rate
Probabilistic Forecast Intervals - LGBM_Quantile - h=24
90% interval (q05-q95)
50% interval (q25-q75)
Actual USD/CAD
Median forecast (q50) (b) 24-hour forecast horizon
Fig. 3: Step 7 LightGBM quantile forecasts at the 1- and 24-hour horizons. Black shows the observed USD/CAD exchange rate, red the
median forecast, and shaded regions the 50% and 90% prediction intervals. Responsiveness and empirical coverage decline at longer horizons.
Fig. 4: Mean directional accuracy across the cumulative ablation sequence at the 1-, 3-, 8-, and 24-hour horizons. Higher values indicate
better directional classification. Step 0 denotes the full feature set; each subsequent step removes one additional feature.
ture by measuring the change in out-of-sample explanatory
power after its removal. Changes inR 2 (∆R2) serve as
the primary attribution metric, while changes in directional
accuracy (∆DA) provide complementary evidence for direc-
tional forecasting. Statistical significance is evaluated using
the global false-discovery-rate (FDR) correction described in
Section III-H, so that only statistically supported attribution
effects are interpreted.
Table V reports the statistically supported feature-level
attribution effects. The attribution results show that forecasting
value is concentrated within a small subset of communication
features. The strongest contributor is the indicator identifying
hours containing monetary-policy news (is_news_hour),
whose removal reduces out-of-sample explanatory power by
approximately 1.2 percentage points. Although this change
appears modest in absolute terms, it should be interpreted
relative to the already high baseline forecasting performance
of the evaluated models, whoseR 2 values exceed 0.86 across
the forecasting horizons.
Beyond communication timing, the remaining statistically
significant contributors primarily capture communication ac-
tivity rather than raw sentiment. Measures of recent Federal
Reserve non-neutral communication, Federal Reserve article
counts, and Bank of Canada communication activity all con-
tribute positively after global FDR correction. These results
indicate that the timing and intensity of central-bank commu-
nication provide more reliable forecasting information than
broad sentiment measures alone.
The same analysis identifies adverse or redundant vari-
ables whose removal improves accuracy. The adverse con-
tributors exhibit a markedly different pattern. Whereas
the strongest positive contributors describe communication
timing and communication activity, the adverse features
are dominated by aggregate news-volume measures and
long-horizon recency variables. In particular, the aggre-
gate article-count variables (news_articles_24hand
news_articles_6h) consistently exhibit negative∆R 2
values, indicating that they become redundant once more
targeted Federal Reserve and Bank of Canada communi-
cation variables are included. Similarly, long-horizon re-
cency measures such ashours_since_boc_news_168h
andhours_since_news_168happear to duplicate in-
formation already captured by explicit news-arrival and
communication-activity indicators.
A clear separation emerges between communication-
specific variables, which improve performance, and aggre-
gate news measures, which are often redundant. Improving
communication-based forecasting is thus as much about se-
lecting informative features as about adding new ones.
E. Group-Level Attribution Results
While the feature-level analysis identifies the individual
communication signals responsible for forecasting improve-
ments, group-level attribution evaluates whether broader cat-
egories of related features contribute predictive value when
considered collectively. This perspective helps characterize
how forecasting information is distributed across the principal

TABLE V: FDR-supported feature-level attribution results. Positive∆R 2 indicates that feature removal reduces forecasting performance,
whereas negative∆R 2 indicates improved performance after feature removal.
Feature Mean∆R 2 Mean∆DA 95% CI Global FDRq-value
Positive contributors
is_news_hour+0.012 +0.04 pp [+0.006,+0.018] 0.003
fed_non_neutral_last_24h+0.005 -0.01 pp [+0.003,+0.008] 0.003
fed_articles_24h+0.005 -0.10 pp [+0.002,+0.008] 0.008
boc_news_last_24h+0.005 -0.09 pp [+0.001,+0.009] 0.041
boc_articles_24h+0.003 +0.08 pp [+0.001,+0.004] 0.026
Adverse or redundant contributors
news_articles_24h-0.010 -0.07 pp [-0.014,-0.006] 0.001
intraday_volatility-0.010 +0.03 pp [-0.016,-0.004] 0.008
hours_since_boc_news_168h-0.009 +0.02 pp [-0.015,-0.004] 0.008
fed_news_last_6h-0.007 +0.08 pp [-0.012,-0.004] 0.008
news_articles_6h-0.005 -0.01 pp [-0.007,-0.002] 0.008
hours_since_news_168h-0.005 +0.03 pp [-0.007,-0.002] 0.007
feature groups, including communication timing, communica-
tion activity, and LLM-derived sentiment.
TABLE VI: Group-level attribution results and representative LLM-
derived sentiment features.
Feature Group / Representative Feature Mean∆R 2 Mean∆DA
Feature groups
News timing only +0.0005 -0.01 pp
News volume only -0.0018 -0.01 pp
LLM-derived sentiment only +0.0020 +0.02 pp
Combined +0.0001 -0.00 pp
Representative LLM-derived sentiment features
sent_diff_impulse+0.001 -0.05 pp
sent_diff_decay_24h+0.002 -0.00 pp
usd_cad_confidence+0.003 +0.06 pp
usd_cad_direction-0.000 +0.02 pp
sent_diff_decay_6h-0.001 +0.07 pp
The grouped attribution results reinforce the feature-level
findings while providing a higher-level interpretation of the
communication signals. Communication timing exhibits a pos-
itive average contribution, consistent with the feature-level
result in whichis_news_houremerged as the strongest
individual contributor. Thus, the timing of policy-relevant in-
formation is one of the most informative short-horizon signals.
In contrast, the news-volume group exhibits a negative
average contribution. This result is consistent with the adverse
feature-level attribution findings, where aggregate article-
count variables became redundant once more targeted central-
bank communication indicators were included. Measuring the
source and timing of policy communication therefore provides
more useful information in these experiments than broad
measures of overall news volume.
At the group level, LLM-derived sentiment exhibits a pos-
itive average contribution, indicating that contextual informa-
tion extracted from monetary-policy communications provides
complementary predictive information beyond communication
timing and activity alone.
The lower panel of Table VI reports the principal
LLM-derived sentiment variables included in the forecast-
ing methodology. The individual sentiment variables are
generally modest in magnitude, with positive contribu-
tions for several representative measures. Features such
assent_diff_decay_24handusd_cad_confidence
increase average∆R 2, indicating that contextual information
extracted from monetary-policy communications complements
communication-frequency and timing variables.
The contribution of the LLM pipeline extends beyond
conventional sentiment scoring. It enables the construction
of higher-level representations describing policy confidence,
directional implications, non-neutral communication, persis-
tence, and sentiment dynamics. Consequently, some activ-
ity measures, especially non-neutral communication counts,
depend on information extracted during the language-model
interpretation stage. Communication timing identifieswhen
policy-relevant information becomes available, whereas the
LLM-derived features help characterizewhatthat information
implies for future monetary-policy expectations. The small
contribution of the combined group indicates substantial over-
lap among the engineered variables.
Taken together, the feature- and group-level attribution
results show that predictive information is distributed across
multiple communication dimensions. At the feature level,
communication timing provides the strongest individual contri-
bution throughis_news_hour, while targeted central-bank
activity measures also contribute positively. At the group level,
LLM-derived sentiment provides additional complementary
predictive information, whereas broad aggregate news-volume
measures are largely redundant.
Finally, cumulative ablation differs sharply from
conventional model-based feature importance. Oil price
(DCOILWTICO), the rate spread (_Spread_pct),
and sentiment-decay features rank highest by model
importance yet add little under ablation—some even improve
performance when removed—whereasis_news_hourhas
low importance but the largest ablation effect.

V. CONCLUSION ANDDISCUSSION
This paper evaluated news-derived monetary-policy signals
for intraday USD/CAD exchange-rate forecasting. The study
makes two contributions. First, within the tested framework,
predictive value concentrates in a small subset of signals: com-
munication timing provides the strongest individual feature-
level contribution, targeted measures of recent central-bank
activity also contribute positively, and LLM-derived senti-
ment provides complementary information at the group level,
whereas broad news-volume measures are largely redundant.
Second, the study shows that cumulative ablation and con-
ventional feature-importance measures provide fundamentally
different perspectives on model behaviour. Feature-importance
measures describe how forecasting models utilize available
information, whereas cumulative ablation quantifies the incre-
mental forecasting value contributed by each communication
signal. This distinction provides a more informative basis
for evaluating engineered communication features and for
understanding how monetary-policy information contributes
to forecasting performance. The reduced feature set also
improves probabilistic scores, though sharpness and interval
calibration must be judged separately.
Several limitations should be acknowledged. The empirical
evaluation is restricted to the USD/CAD exchange rate and
communications from the Federal Reserve and the Bank of
Canada, limiting direct generalization to other currencies and
monetary-policy regimes. In addition, cumulative ablation is
inherently path dependent, so measured marginal contributions
may vary with the feature-removal sequence. Finally, the
study evaluates statistical forecasting performance rather than
economic value and therefore does not consider transaction
costs, market frictions, or trading profitability. The LLM-
derived communication features are also influenced by prompt
design, model selection, and classification uncertainty.
Future research can extend this methodology to additional
currency pairs, central banks, and multilingual communication
sources to evaluate the stability of the observed communi-
cation hierarchy. Alternative attribution approaches, including
permutation-based attribution and SHAP-based group explana-
tions, would provide useful comparisons with cumulative abla-
tion. Future work should also incorporate formal benchmark-
comparison procedures, such as the Diebold–Mariano and
Clark–West tests, together with realistic trading evaluations
and more advanced probabilistic calibration techniques. More
broadly, better communication-aware forecasting depends less
on adding textual features than on identifying the few that
carry unique predictive value.
REFERENCES
[1] A. S. Blinder, M. Ehrmann, M. Fratzscher, J. De Haan, and D.-J.
Jansen, “Central bank communication and monetary policy: A
survey of theory and evidence,”Journal of Economic Literature,
vol. 46, no. 4, pp. 910–945, 2008.
[2] M. Ehrmann and M. Fratzscher, “Communication by central
bank committee members: Different strategies, same effective-
ness?”Journal of Money, Credit and Banking, vol. 39, no. 2–3,
pp. 509–541, 2007.
[3] P. C. Tetlock, “Giving content to investor sentiment: The role
of media in the stock market,”The Journal of Finance, vol. 62,
no. 3, pp. 1139–1168, 2007.
[4] J. Bollen, H. Mao, and X. Zeng, “Twitter mood predicts the
stock market,”Journal of Computational Science, vol. 2, no. 1,
pp. 1–8, 2011.
[5] T. Loughran and B. McDonald, “When is a liability not a
liability? textual analysis, dictionaries, and 10-Ks,”The Journal
of Finance, vol. 66, no. 1, pp. 35–65, 2011.
[6] G. Ke, Q. Meng, T. Finley, T. Wang, W. Chen, W. Ma, Q. Ye,
and T.-Y . Liu, “LightGBM: A highly efficient gradient boosting
decision tree,” inAdvances in Neural Information Processing
Systems, vol. 30, 2017, pp. 3146–3154.
[7] D. Araci, “FinBERT: Financial sentiment analysis with pre-
trained language models,”arXiv preprint arXiv:1908.10063,
2019.
[8] S. Wu, O. Irsoy, S. Lu, V . Dabravolski, M. Dredze,
S. Gehrmann, P. Kambadur, D. Rosenberg, and G. Mann,
“BloombergGPT: A large language model for finance,”arXiv
preprint arXiv:2303.17564, 2023.
[9] H. Yang, X.-Y . Liu, and C. D. Wang, “FinGPT: Open-
source financial large language models,”arXiv preprint
arXiv:2306.06031, 2023.
[10] K. B. K ¨uc ¸¨uklerli and V . Ulusoy, “Sentiment-driven exchange
rate forecasting: Integrating twitter analysis with economic
indicators,”Journal of Applied Finance & Banking, vol. 14,
no. 3, pp. 4–17, 2024.
[11] S. M. Lundberg and S.-I. Lee, “A unified approach to inter-
preting model predictions,” inAdvances in Neural Information
Processing Systems, vol. 30, 2017, pp. 4765–4774.
[12] C. Molnar, “Interpretable machine learning,” https://christophm.
github.io/interpretable-ml-book/, 2022, 2nd edition.
[13] A. Fisher, C. Rudin, and F. Dominici, “All models are wrong,
but many are useful: Learning a variable’s importance by
studying an entire class of prediction models simultaneously,”
Journal of Machine Learning Research, vol. 20, no. 177, pp.
1–81, 2019.
[14] B. Rossi, “Exchange rate predictability,”Journal of Economic
Literature, vol. 51, no. 4, pp. 1063–1119, 2013.
[15] Y .-W. Cheung, M. D. Chinn, and A. G. Pascual, “Empirical
exchange rate models of the nineties: Are any fit to survive?”
Journal of International Money and Finance, vol. 24, no. 7, pp.
1150–1175, 2005.
[16] V . Plakandaras, T. Papadimitriou, and P. Gogas, “Forecasting
daily and monthly exchange rates with machine learning tech-
niques,”Journal of Forecasting, vol. 34, no. 7, pp. 560–573,
2015.
[17] D. C. Yildirim, I. H. Toroslu, and U. Fiore, “Forecasting
directional movement of forex data using LSTM with technical
and macroeconomic indicators,”Financial Innovation, vol. 7,
no. 1, pp. 1–36, 2021.
[18] D. P. Neghab, M. Cevik, M. Wahab, and A. Basar, “Explaining
exchange rate forecasts with macroeconomic fundamentals us-
ing interpretive machine learning,”Computational Economics,
vol. 65, no. 4, pp. 1857–1899, 2025.
[19] Z. Liu, D. Huang, K. Huang, Z. Li, and J. Zhao, “FinBERT: A
pre-trained financial language representation model for financial
text mining,” inProceedings of the Twenty-Ninth International
Joint Conference on Artificial Intelligence, 2021, pp. 4513–
4519.
[20] Y . Benjamini and Y . Hochberg, “Controlling the false discovery
rate: A practical and powerful approach to multiple testing,”
Journal of the Royal Statistical Society: Series B (Methodolog-
ical), vol. 57, no. 1, pp. 289–300, 1995.
