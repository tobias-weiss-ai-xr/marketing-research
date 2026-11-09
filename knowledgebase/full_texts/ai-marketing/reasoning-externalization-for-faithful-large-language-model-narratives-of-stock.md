---
title: Reasoning Externalization for Faithful Large Language Model Narratives of Stock Return Predictions
url: https://arxiv.org/abs/2609.38869
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Sujung Kim
- Seung Hwan Cho
- Sangjin Park
- Young-Min Kim
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.38869
pages: 15
chars: 46160
fetched_at: '2026-11-08T13:24:35+00:00'
kb_version: 1
---

# Reasoning Externalization for Faithful Large Language Model Narratives of Stock Return Predictions

Reasoning Externalization for Faithful Large Language
Model Narratives of Stock Return Predictions
Sujung Kim1,†, Seung Hwan Cho 1,†, Sangjin Park 1,2,* and Young-Min Kim 1,2
1Department of Industrial Data Engineering, Hanyang University, Republic of Korea
2School of Interdisciplinary Industrial Studies, Hanyang University, Republic of Korea
Abstract
In finance, interpreting machine learning predictions is essential, yet the numerical outputs of explainable AI
can be difficult for non-experts to understand. While large language models (LLMs) can translate these outputs
into natural language, they may produce errors when inferring numerical changes and feature relations. We
propose an LLM narrative framework for cross-sectional stock return prediction that combines temporal Shapley
additive explanations (SHAP) evidence with historical regime analogs. Temporal evidence tracks changes in
the normalized global SHAP importance of an XGBoost model over six months. Historical analogs are past
periods with similar changes in SHAP importance, their model performance and subsequent market returns are
provided as comparative context. Using this framework, we conduct a controlled study of progressive reasoning
externalization, sequentially providing raw SHAP sequences, deterministic temporal descriptors, and feature
relations. Each generated claim is verified against provenance-linked evidence. Across Qwen3, externalizing
numerical and relational reasoning improved evidence faithfulness as well as temporal and relational accuracy.
Evidence faithfulness increased from 0.696 to 0.996 for Qwen3-32B-Instruct. While historical analogs did not
improve structured automatic faithfulness, they received higher human-rated usefulness scores. These results
suggest that externalizing verifiable reasoning enhances narrative faithfulness and that historical context adds
interpretive value. The code is available at https://github.com/sugenre/reasoning-externalization-xai.
Keywords
Explainable AI, Large Language Models, Narratives, Cross-sectional Stock Prediction
1. Introduction
Machine learning based predictive models are increasingly being adopted in the financial domain;
however, their inherently black box nature makes it difficult to understand the rationale underlying
their predictions. Model interpretability is considered essential in finance for both investment decision
making and regulatory compliance [1], motivating the adoption of explainable AI (XAI) methods. Among
the most widely used XAI methods, Shapley additive explanations (SHAP) quantitatively measure the
contribution of individual features to model predictions [ 2]. However, SHAP outputs derived from
complex financial data are inherently numerical and can be difficult for non expert users to understand
[3]. Translating such quantitative explanations into insights that can support decision making therefore
remains a challenging task [4].
To address this limitation, recent studies have used large language models (LLMs) to translate
SHAP outputs into natural language explanations, improving understandability [5]. However, return-
generating processes in financial markets vary over time due to business cycles, policy changes, crises,
and other structural shifts [6]. Therefore, a SHAP explanation based on data from a single point in time
cannot fully convey how the model interprets current market conditions. Historical information on
how the model behaved under similar market conditions, and how the market subsequently evolved,
can provide valuable context for financial practitioners [7]. Such temporal and historical context has
not yet been systematically incorporated into LLM-based explanations. Providing it is itself challenging,
LLM4XAI 2026: Generative Models for Explainable AI Narratives, at CIKM 2026, November 8, 2026, Rome, Italy
*Corresponding author.
†
These authors contributed equally to this work.
/envel⌢pe-⌢pensujung2026@hanyang.ac.kr (S. Kim); shcho95@hanyang.ac.kr (S. H. Cho); psj3493@hanyang.ac.kr (S. Park);
yngmnkim@hanyang.ac.kr (Y. Kim)
/orcid0000-0002-6055-0376 (S. Park)
©2026 Copyright for this paper by its authors. Use permitted under Creative Commons License Attribution 4.0 International (CC BY 4.0).

as LLMs struggle to reason over time-series data [8]. Narratives generated from this evidence therefore
require verification of their faithfulness after generation [9]. This verification is essential in finance,
where model reliability directly affects economic outcomes and regulatory compliance [1].
In this study, we propose a framework that provides LLMs with temporal XAI evidence to generate
financial analysis narratives in a cross-sectional stock return prediction setting. An XGBoost model is
trained on preprocessed CRSP1 data, and its SHAP values are used to construct temporal trajectories
of feature attributions. Historical periods with similar attribution trajectories are then retrieved and
provided as historical context. Using this framework, we conduct a controlled study of how progressively
externalizing numerical and relational reasoning affects narrative faithfulness. The main contributions
of this study are as follows.
• Evidence-grounded narrative framework.Temporal SHAP evidence is linked to historical
regimes with similar changes in SHAP importance, and each generated claim is verified against a
provenance-linked evidence registry.
• Controlled study of reasoning externalization.Deterministic temporal descriptors and
feature relations substantially reduce temporal and relational reasoning errors and improve
evidence faithfulness across Qwen3 scales.
• Role of historical analogs.Historical analogs do not improve structured automatic faithfulness
but increase human-rated usefulness, serving as complementary interpretive context.
2. Related Work
2.1. SHAP Based Feature Analysis in Financial Prediction
SHAP is one of the most widely used XAI methods grounded in game theory [2]. By providing both
global attributions for the overall model and local attributions for individual predictions, SHAP has
been extensively studied across various domains [10], including financial return prediction. Goswami
and Uddin analyzed 166 asset-pricing characteristics and found that momentum and trading related
features exhibited high contributions, with portfolio analyses further demonstrating their substantial
economic significance [11]. Wang showed that, in neural network models, momentum- and trading-
related features contributed most strongly to the prediction of abnormal stock returns, whereas investor
sentiment features exhibited the highest contributions in predicting excess stock returns [12]. However,
these studies primarily conducted static SHAP analyses over the full sample period or at specific points
in time.
To address the limitations of static analysis, Lundberg et al. proposed a method that uses SHAP to
quantify each feature’s contribution to predictive loss and tracks these contributions over time to identify
the causes of model performance degradation [ 13]. Rather than directly comparing shifts in input
distributions, Mougan et al. introduced the concept of Explanation Shift, which detects changes in how
a model utilizes features by comparing historical and current SHAP based distributions [14]. Similarly,
Jenett et al. applied XGBoost and SHAP to the prediction of Real Estate Investment Trust returns
and volatility, showing that the importance of key variables changes across distinct market regimes,
including the global financial crisis, the low interest rate period, and the COVID-19 pandemic. They
further analyzed nonlinear relationships between explanatory variables and returns using Accumulated
Local Effects [6]. These studies examined dynamic changes in SHAP importance primarily from the
perspective of monitoring and detecting model changes, but did not exploit temporal patterns in these
changes to identify historically similar market regimes or support downstream analysis.
2.2. LLM-Based Explanation and Context-Augmented Financial Analysis
Although SHAP based outputs provide detailed model explanations, they can be difficult for non
expert users to understand and interpret. To address this issue, Zeng and Zhu proposed a pipeline that
1Center for Research in Security Prices (CRSP), accessed via Wharton Research Data Services (WRDS).

organizes SHAP outputs into a structured format and generates natural language explanations through
prompt engineering, thereby improving the clarity and usability of model explanations [3]. Zytek et al.
introduced Explingo, which consists of a Narrator that translates ML explanations into natural language
and a Grader that evaluates the generated explanations, with the aim of producing high quality narratives
[4]. Martens et al. proposed XAIstories, which transforms SHAP and counterfactual explanations into
LLM generated narratives, and showed that these narratives helped users summarize and understand
AI decisions more accurately than raw SHAP outputs [5]. Geng et al. found that providing SHAP based
feature rankings to an LLM resulted in better performance than allowing the LLM to infer feature
importance independently, suggesting that LLMs should be used as controlled narrative interfaces
[15]. Beyond SHAP, Wang translated explanations of a temporal graph convolutional network for
stock trend prediction into natural language financial reports using LLMs, and evaluated the reports
with a factual sensitivity protocol [16]. Nevertheless, concerns remain regarding the faithfulness of
generated narratives. Lukassen et al. pointed out that prior studies have predominantly evaluated the
textual quality of generated narratives while providing limited validation of their practical usefulness
for decision making [17]. Pratama and Tseng further identified fidelity failures in LLM generated credit
risk reports, including reversals of SHAP value signs, omission of dominant features, and inclusion of
features that were not provided in the underlying evidence [9].
A growing body of research has also investigated the use of contextual information in financial
analysis and prediction. Teixeira et al. proposed Labeled Guide Prompting, which combines structured
outputs from Bayesian Networks with LLMs to automatically generate credit risk reports [18]. Kim et
al. provided GPT-4 with financial statements to predict the direction of future earnings changes and
demonstrated that LLMs can generate useful narrative insights regarding future earnings [19]. Fatouros
et al. introduced MarketSenseAI 2.0, which integrates news, financial statements, and macroeconomic
data within a multiagent LLM architecture to support stock analysis and investment decision making
[20]. These studies primarily used textual or numerical information observed at a given point in time as
contextual input to LLMs. Other studies have explored the use of historically similar cases as contextual
information. Khanna et al. proposed a framework that combines macroeconomic indicators with text
embeddings to retrieve similar historical periods and provides the retrieved cases as context for LLM
based prediction [7]. In their framework, similarity is measured based on macroeconomic variables,
while temporal patterns in feature attributions derived from an ML model are not used.
3. Methodology
3.1. Data Preparation and Stock Return Prediction
Using monthly CRSP data obtained through WRDS, we constructed 30 stock level characteristics covering
price and trend, momentum, volatility and risk, and trading volume and liquidity. Each characteristic
was defined as either a month end value or a monthly aggregate according to its economic interpretation
and the measurement convention of the underlying raw data. For delisting observations, both regular
returns and delisting returns were incorporated. Missing characteristic values were imputed using the
monthly cross sectional median, after which the remaining missing values were set to zero following
[21]. To mitigate the influence of extreme observations while maintaining consistent preprocessing
across time, each characteristic was winsorized using the 1st and 99th percentile thresholds estimated
from the training sample, and the same thresholds were subsequently applied to the validation and
test periods [22]. Preserving the temporal ordering of the data, the sample was divided into a training
period from January 1995 to December 2009, a validation period from January 2010 to December 2011,
and a test period from January 2012 to November 2023.
Using the resulting monthly stock characteristics, we formulated a cross sectional stock return
prediction task in which the feature vector x𝑖,𝑡 of stock 𝑖 observed in month 𝑡 is used to predict its
realized return 𝑟𝑖,𝑡+1 in the following month. Monthly prediction is a widely adopted setting in cross
sectional asset pricing research based on firm characteristics [21] and is also well suited to aligning
characteristics with heterogeneous update frequencies at a common time point. Because the primary

Figure 1:Overview of the proposed framework for generating evidence-grounded LLM narratives of stock return
predictions.
focus of this study is not short term price fluctuations themselves but rather the model’s feature
dependence structure and its temporal variation, both the return prediction task and the subsequent
SHAP based temporal analysis were conducted at a monthly frequency.
3.2. Temporal XAI Evidence Construction
Tree based models can flexibly capture nonlinear relationships and interactions among features in cross
sectional return prediction [21], while TreeSHAP enables efficient computation of feature attributions
for individual predictions [13]. Let the SHAP value for stock𝑖, feature 𝑗, and month 𝑡 be denoted by 𝜑𝑖,𝑗,𝑡.
The monthly global attribution was computed by first taking the cross sectional mean of the absolute
SHAP values for each feature and then normalizing it by the sum of these mean absolute attributions
across all features to obtain 𝑃𝑗,𝑡. The resulting 𝑃𝑗,𝑡 represents the relative importance of feature 𝑗 in
the model’s global attribution for month 𝑡. Let 𝑃𝑡 denote the 30 dimensional global attribution vector
for month𝑡; the temporal evidence over the most recent six months was then constructed as𝑆 𝑡.
𝐴𝑗,𝑡 = 1 𝑁𝑡 ∑︁ 𝑖 |𝜑𝑖,𝑗,𝑡|,(1)
𝑃𝑗,𝑡 = 𝐴𝑗,𝑡∑︀
𝑘 𝐴𝑘,𝑡
,(2)
𝑆𝑡 = [𝑃𝑡−5, 𝑃𝑡−4, . . . , 𝑃𝑡]∈R 6×30.(3)
3.3. Historical SHAP Based Analog Augmentation
To augment temporal XAI evidence with historical comparative context, we retrieved past market
regimes exhibiting similar patterns of change in feature importance. While raw market variables such
as prices and returns can characterize similarity in market states, changes in global SHAP importance
reflect how the relative contribution structure of features evolves over time under a fixed predictive
model. We therefore retrieved historical regimes with similar SHAP importance dynamics and provided

the model’s predictive performance and subsequent universe returns in those periods as comparative
context.
Using 𝑃𝑡, we defined the monthly change in attribution as in Equation (4) and used it as the retrieval
representation. For a temporal window of length 𝐿, the query trajectory at month 𝑡 was constructed as
in Equation (5). Because each Δ𝑃𝑡 is a 30 dimensional vector, Δ𝑃𝑡∈R 30, the distance between query
trajectory𝑄 (𝐿) 𝑡 and historical candidate trajectory𝑄 (𝐿) 𝑠 was computed using Euclidean distance.
Δ𝑃𝑡 =𝑃 𝑡−𝑃 𝑡−1,(4)
𝑄(𝐿) 𝑡 = [Δ𝑃𝑡−𝐿+1, . . . ,Δ𝑃𝑡],(5)
𝑑(𝑡, 𝑠) =
⃦⃦⃦vec (︁ 𝑄(𝐿) 𝑡 )︁ −vec (︁ 𝑄(𝐿) 𝑠 )︁⃦⃦⃦ 2 .(6)
To ensure that the query and candidate trajectories did not overlap and that the outcome following
each candidate was observable before the query period, historical candidates were restricted to 𝑠≤
𝑡−(𝐿+ 1) . The top 𝐾 candidates with the smallest distances were selected as historical analogs. The
sensitivity to𝐿and𝐾, as well as the final retrieval configuration, was determined empirically.
Each historical analog was associated with its trajectory distance, monthly RankIC at the correspond-
ing period, and the equal weighted universe return in the subsequent month. These outcomes were
not treated as direct forecasts or causal evidence. Rather, they served as comparative historical context
indicating the model’s predictive performance and subsequent universe returns during past periods
exhibiting similar changes in feature attribution.
3.4. Structured Evidence Registry
The generated prediction, feature attribution, temporal descriptors, feature relations, and historical
analog evidence were stored in a unified structured evidence registry. Each evidence unit was assigned
a unique provenance identifier specifying the case, evidence type, and associated feature or relation.
For example, case_id#TMP:momentum12 denotes the temporal numerical evidence for momentum12
in a given case.
All experimental conditions shared the same underlying registry, while the visibility of each evidence
unit was predetermined for each condition. Thus, differences across conditions were created by
varying only the scope of information exposed to the LLM, rather than by recomputing the underlying
evidence. The prompt presented each evidence item together with its corresponding identifier, which
was subsequently used to verify generated claims against the source evidence.
3.5. Reasoning Externalization and Narrative Generation
To control the reasoning burden placed on the LLM during temporal XAI narrative generation, numerical
and relational reasoning were progressively externalized. Motivated by findings that delegating compu-
tation from the LLM to an external interpreter improves reasoning accuracy [23], these computations
were performed deterministically before generation and provided as evidence rather than derived by
the LLM. The experimental conditions were designed according to the dependency structure of the
required reasoning steps, while the system prompt and output schema were kept unchanged across
conditions.
C0 evaluates whether the model suppresses unsupported temporal inference when no temporal
evidence is available. Under C1, the LLM must infer temporal trends and feature relations directly
from the raw temporal sequence. C2 externalizes deterministic numerical computation by explicitly
providing temporal statistics. The six-month attribution change was defined as Δ6𝑃𝑗,𝑡 =𝑃 𝑗,𝑡−𝑃 𝑗,𝑡−5.
The temporal slope was estimated by OLS over the six monthly attribution values 𝑃𝑗,𝑡−5:𝑡, using month
indices0, . . . ,5. Trend direction was labeled as increasing, decreasing, or flat according to the sign of
the six month OLS slope. C3 further provides OVERTAKES relations, thereby removing the burden of
relational inference from the LLM. Feature 𝑎 was defined to overtake feature 𝑏 when 𝑃𝑎,𝑡−5 < 𝑃𝑏,𝑡−5

Table 1
Experimental Conditions and Evidence Provided
Condition Evidence provided
C0-Evidence Control Prediction, local SHAP, and current global attribution
C1-Raw C0 + raw 6-month global attribution sequence
C2-Numerical C1 +Δ6𝑃, slope, and trend direction
C3-Relational C2 + deterministic OVERTAKES relations
C3-Analog C3 + historical analog evidence
but 𝑃𝑎,𝑡 > 𝑃𝑏,𝑡. C3-Analog is a separate augmentation condition that combines C3 with historical
context. Each output consisted of natural language text together with structured claims. Every factual
claim was required to reference evidence IDs available under the corresponding condition, while the
model was allowed to abstain when no supporting evidence was available.
The primary model was Qwen3-32B-Instruct [24], the largest dense model that could be executed
under a consistent inference protocol in our experimental environment. Qwen3-14B and Qwen3-8B
were additionally included to assess whether the observed effects remained consistent across model
scales within the same model family, while their corresponding Base checkpoints were used to examine
sensitivity to post training. Ministral-8B-Instruct-2410 [25] and Llama-3.1-8B-Instruct [26] were further
included to evaluate whether the effects of reasoning externalization remained consistent across different
model families.
4. Experiments and Results
4.1. Evaluation Protocol
4.1.1. Prediction Performance Evaluation
Return prediction performance was evaluated using RankIC, RankICIR, RMSE, and MAE. For each
month 𝑡, RankIC was computed as the cross sectional Spearman correlation between the predicted
next-month return ̂︀𝑟𝑖,𝑡+1 and the realized next month return 𝑟𝑖,𝑡+1 across stocks. We report the average
monthly RankIC over the full test period. RankICIR was calculated as the mean monthly RankIC divided
by its standard deviation, measuring the stability of cross-sectional ranking performance over time.
RankIC𝑡 = Spearman𝑖(̂︀𝑟𝑖,𝑡+1, 𝑟𝑖,𝑡+1),(7)
RankIC = 1 𝑇 𝑇∑︁ 𝑡=1 RankIC𝑡,(8)
RankICIR = mean(RankIC𝑡) std(RankIC𝑡) .(9)
4.1.2. Deterministic Automatic Evaluation
The generated outputs were evaluated by directly matching their structured semantic fields against
the evidence registry. Our primary metric, Structured Evidence Faithfulness (EF), was defined as the
proportion of factual claims that referenced evidence permitted under the corresponding experimental
condition and matched the ground truth subject–predicate–value tuple.
Because the evaluation operates on structured fields generated alongside the natural language
narrative, EF measures the consistency between structured factual claims and their supporting evidence
rather than the overall semantic truthfulness of unrestricted free form text. Output format reliability
was additionally evaluated using the parse rate. For C0, in which no temporal evidence was provided,

we further evaluated whether the model appropriately refrained from unsupported inference using
Evidence Control Abstention Accuracy.
4.1.3. LLM-as-a-Judge
Because the deterministic evaluation verifies only the correspondence between structured claim fields
and the evidence registry, without directly assessing the narrative text itself, we conducted a comple-
mentary LLM-as-a-Judge evaluation on the C3-Relational and C3-Analog conditions. Using month
stratified sampling, we selected a common set of 400 case_ids and paired the narratives from the
two conditions at the case level. Claude Opus 5, which belongs to a different model family from the
generation models (Qwen, Llama, and Mistral), was used as the judge. Model and condition identifiers
were omitted from the evaluation prompts. Each item was evaluated once (𝑘= 1 ) through the Message
Batches API.
The evaluation comprised three criteria, with different levels of information exposure for each
criterion. First, the judge was shown only the narrative text, without any supporting evidence, and
asked to determine whether the normalized global SHAP importance ( 𝑃 ) of the focal feature had
increased, decreased, or remained unchanged over the preceding six months, or whether the direction
could not be determined from the text alone. Textual Temporal Transfer Accuracy was computed as the
exact match accuracy between the resulting judgment and trend_direction in the evidence registry.
For the second and third criteria, the judge was provided with both the narrative and the evidence
block corresponding to the relevant condition. Evidence Scope Adherence was defined as the extent
to which the narrative avoided claims beyond the scope of the provided evidence, whereas Narrative
Synthesis was defined as the extent to which multiple evidence items were coherently integrated into
an interpretation while remaining within the supported evidence scope. Both criteria were evaluated
using pre defined anchored 1–5 rating rubrics.
4.1.4. Human Evaluation
To assess the practical utility of historical analog context, we conducted a human evaluation comparing
narratives generated by Qwen3-32B-Instruct under the C3-Relational and C3-Analog conditions. Ten
evaluators each assessed two cases. For each case, the evaluator reviewed one C3-Relational narrative
and one C3-Analog narrative, resulting in four narrative evaluations per evaluator. Evaluators were non
expert users with an interest in stock investment and basic familiarity with artificial intelligence concepts.
Condition labels were hidden, and both the case order and the order of the two narratives within each
pair were randomized. Evaluators rated each narrative using five criteria: Understandability, Decision
Usefulness, Contextual Usefulness, Reliance Calibration, and Adoption Intention, on five point Likert
scales. This evaluation was designed to examine whether historical analogs provide additional value for
users’ interpretation and use of the narratives, separately from automatic faithfulness evaluation.
4.2. Experimental Setup and Prediction Model Selection
All experiments were conducted on Ubuntu 24.04 using an NVIDIA RTX PRO 6000 GPU with 96 GB of
memory. XGBoost 3.2.0 and SHAP 0.51.0 were used for prediction and XAI analysis, respectively, while
LLM inference was performed using vLLM 0.11.2. The same decoding configuration was applied across
all LLM conditions.
Because the primary objective was not to compete for state-of-the-art predictive performance, but
rather to evaluate the faithfulness of LLM-generated narratives grounded in XAI evidence derived from
a fixed prediction model, we compared two linear baselines, Linear Regression and Ridge Regression,
with two tree-based models, Random Forest and XGBoost, which can capture nonlinear relationships
and feature interactions while supporting TreeSHAP-based attribution.
The tree based models achieved higher RankIC values than the linear models, suggesting that
capturing nonlinear effects and feature interactions may be important for modeling the relationship
between financial characteristics and next month returns in this prediction setting. Compared with

Table 2
Out-of-Sample Prediction Performance
Model RankIC↑RankICIR↑RMSE↓MAE↓
Linear Regression 0.0170 0.2380 0.1631 0.0845
Ridge Regression 0.0209 0.2810 0.1631 0.0848
Random Forest 0.0357 0.4900 0.1627 0.0841
XGBoost0.0361 0.53800.1660 0.0859
Random Forest, XGBoost achieved 1.4% higher RankIC and 9.8% higher RankICIR. However, Random
Forest achieved lower RMSE and MAE, indicating that XGBoost did not dominate across all predictive
metrics. XGBoost was selected using validation period performance and then fixed for all test period
XAI analyses. Test results were used only for final out of sample evaluation. TreeSHAP was applied to
interpret feature contributions under this predictive model.
4.3. Historical Analog Characterization
Before incorporating historical analogs as contextual evidence, we assessed whether regimes retrieved
based on changes in SHAP importance provided useful comparative context for subsequent universe
returns. Sensitivity analyses were conducted across temporal window lengths 𝐿∈ {3,6,9} and
numbers of retrieved analogs𝐾∈{1,3,5}.
For comparison, we constructed a market state based retrieval method that retained the same retrieval
conditions but replaced the representation with changes in the cross sectional market state derived
from the raw variables. We additionally evaluated a recent return baseline and a random baseline
that selected historical regimes at random. For each method, we compared the aggregated subsequent
universe returns of the retrieved historical regimes with the realized next month universe return using
mean absolute error (MAE). Table 3 reports the results across the evaluated retrieval configurations.
Table 3
Mean Absolute Error of Subsequent Universe Returns across Retrieval Settings
Method𝐾= 1𝐾= 3𝐾= 5
𝐿= 3𝐿= 6𝐿= 9𝐿= 3𝐿= 6𝐿= 9𝐿= 3𝐿= 6𝐿= 9
SHAP-Trajectory 0.05146 0.05135 0.04845 0.041800.04260 0.040910.04012 0.039960.04121
Market-State 0.04752 0.04822 0.04899 0.04225 0.040760.04057 0.04098 0.03997 0.04147
Recent-Return0.04544 0.04128 0.039720.04544 0.04128 0.039720.04544 0.041280.04042
Random 0.04902 0.04858 0.04874 0.04236 0.04205 0.04186 0.04047 0.04040 0.04114
For SHAP-Trajectory retrieval, MAE generally decreased as the number of retrieved analogs increased.
This pattern is consistent with the possibility that aggregating multiple historical analogs reduces
sensitivity to any single retrieved period. Among the evaluated SHAP-Trajectory configurations,𝐾= 5
and 𝐿= 6 minimized validation MAE, yielding a value of 0.03996. Accordingly, we selected this
configuration for SHAP-Trajectory retrieval before evaluating C3-Analog on the test period.
However, SHAP-Trajectory retrieval was not consistently superior to the alternative methods. The
recent return baseline achieved lower MAE than SHAP-Trajectory in six of the nine evaluated config-
urations. Under the selected 𝐾= 5 and 𝐿= 6 configuration, SHAP-Trajectory achieved an MAE of
0.03996, which was nearly identical to the 0.03997 obtained by market-state retrieval. We therefore
do not interpret these results as evidence of consistent superiority of SHAP-Trajectory retrieval over
the alternative methods. Instead, the retrieved analogs are used as historical comparative context,
providing information on model performance and subsequent equal-weighted universe returns during
past periods characterized by similar changes in model feature contributions.

4.4. Reasoning Externalization and Narrative Faithfulness
Table 4 reports cross-model performance under C1–C3 in terms of evidence faithfulness, temporal
accuracy, and relational accuracy, together with output parse rates.
Table 4
Cross-Model Consistency of Reasoning Externalization
Model Parse EF C1 EF C2 EF C3 Temp. C1 Temp. C2 Temp. C3 Rel. C1 Rel. C2 Rel. C3
Qwen3-8B 0.9363 0.7219 0.7662 0.9195 0.6318 0.8784 0.8458 0.2155 0.3585 0.9295
Qwen3-8B-Instruct1.00000.8259 0.97040.9686 0.3604 0.6125 0.57500.8625 0.8875 1.0000
Qwen3-14B 0.9779 0.7570 0.8061 0.9984 0.6979 0.9916 0.99160.3375 0.2059 0.9979
Qwen3-14B-Instruct1.00000.7194 0.88440.99950.4854 0.9479 0.9521 0.4271 0.49791.0000
Qwen3-32B-Instruct 0.9988 0.6960 0.9032 0.9964 0.3396 0.9896 0.9313 0.5250 0.57291.0000
Ministral-8B-Instruct 0.54330.87330.8536 0.9204 0.5506 0.6273 0.5246 0.7341 0.8636 0.9836
Llama-3.1-8B-Instruct 0.4525 0.6555 0.5762 0.5437 0.1905 0.4020 0.4098 0.5450 0.4975 0.7639
Across all Qwen3 Instruct models, numerical externalization from C1 to C2 increased Structured
Temporal Accuracy, with improvements of 0.6500, 0.4625, and 0.2521 for the 32B, 14B, and 8B models,
respectively. When relational evidence was provided in C3, Relational Accuracy increased over C2 by
0.4271, 0.5021, and 0.1125, respectively, showing the same directional effect regardless of model scale.
Ministral and Llama exhibited relatively low parse rates of 0.5433 and 0.4525, respectively, resulting
in different numbers of valid samples across conditions; they were therefore excluded from direct
quantitative comparisons. The Qwen3 base models also showed increases in Structured Temporal
Accuracy from C1 to C2 of 0.2466 for 8B and 0.2937 for 14B, indicating that the effect of numerical
externalization was not limited to instruction-tuned models. Meanwhile, Qwen3 Base models generally
achieved higher temporal reasoning accuracy than their Instruct counterparts of the same size, but
lower relational reasoning accuracy, suggesting that the effect of instruction tuning may differ across
reasoning types.
Table 5
Structured Claim Performance by Reasoning Condition (Qwen3-32B-Instruct)
Condition EF↑Temporal Acc.↑Relational Acc.↑C0 Abstention
C0-Evidence Control 0.9104 – – 0.8386
C1-Raw 0.6960 0.3396 0.5250 –
C2-Numerical 0.90320.98960.5729 –
C3-Relational0.99640.9313 1.0000–
C3-Analog 0.9891 0.90001.0000–
For Qwen3-32B-Instruct, externalizing numerical information from C1 to C2 increased EF from 0.6960
to 0.9032, corresponding to an improvement of 0.2072, while Structured Temporal Accuracy increased
from 0.3396 to 0.9896, an improvement of 0.6500. This substantial increase indicates that explicitly
providing deterministic temporal descriptors markedly improved the model’s ability to represent
temporal changes relative to requiring such information to be inferred from raw attribution sequences.
When relational evidence was additionally structured and provided in C3, Relational Accuracy increased
from 0.5729 under C2 to 1.0000, corresponding to an improvement of 0.4271. EF also increased from
0.9032 to 0.9964, while Structured Temporal Accuracy remained high at 0.9313. Under the C0-Evidence
Control condition, abstention accuracy was 0.8386, indicating that unsupported inference was frequently,
though not perfectly, suppressed when temporal evidence was unavailable. C3-Analog maintained
perfect Relational Accuracy at 1.0000, while EF and Structured Temporal Accuracy were slightly lower
than those under C3-Relational, decreasing from 0.9964 to 0.9891 and from 0.9313 to 0.9000, respectively.
These results suggest that historical analog augmentation did not provide an additional improvement
in structured automatic faithfulness, motivating a separate evaluation of its narrative level and human
level utility.

4.5. LLM-as-a-Judge Evaluation
To assess narrative-level faithfulness, we compare C3-Relational and C3-Analog in terms of temporal
information transfer, evidence-scope adherence, and narrative synthesis. Table 6 summarizes the results.
Table 6
LLM-as-a-Judge Evaluation of Narrative Level Faithfulness (Mean±SD)
Metric C3-Relational C3-Analog
Textual Temporal Transfer Accuracy0.9975 0.9975
Deterministic Temporal Accuracy0.86250.7425
Evidence Scope Adherence4.9300±0.2555 4.8900 ±0.3212
Narrative Synthesis2.0275±0.1637 1.9975 ±0.0867
Textual Temporal Transfer Accuracy was 0.9975 (399/400) for both conditions, indicating that the
addition of historical analogs did not materially impair the communication of temporal change infor-
mation for the focal feature. In contrast, Deterministic Temporal Accuracy was lower, at 0.8625 for
C3-Relational and 0.7425 for C3-Analog. Further analysis showed that all 158 cases classified as failures
by the deterministic metric lacked atemporal_trend claim but contained atemporal_change claim.
This discrepancy therefore reflects a difference in claim-type-specific aggregation rather than an actual
loss of temporal information in the narrative.
Evidence Scope Adherence remained high in both conditions, at approximately 4.9 out of 5, suggesting
that the inclusion of historical analogs did not increase the generation of claims beyond the scope of
the provided evidence. By contrast, Narrative Synthesis scores were low, at approximately 2 out of
5. This suggests that evidence constrained generation is effective in maintaining faithfulness to the
provided evidence, but may limit the flexibility with which multiple evidence items are integrated into
a narrative.
4.6. Human Evaluation of Historical Analog Context
To assess whether historical analogs improve the perceived usefulness of generated narratives, we
compare C3-Relational and C3-Analog across five human-evaluation criteria covering understandabil-
ity, decision usefulness, contextual usefulness, reliance calibration, and adoption intention. Table 7
summarizes the mean ratings and between-condition differences.
Table 7
Human Evaluation of Historical Analog Context (Mean±SD)
Item C3-Relational C3-AnalogΔ
Q1 Understandability3.2000 ±1.23973.6000±1.2732 +0.4000
Q2 Decision Usefulness3.3500 ±1.22583.8000±1.1517 +0.4500
Q3 Contextual Usefulness3.2000 ±1.50793.7000±1.2607 +0.5000
Q4 Reliance Calibration3.2500 ±1.16423.6500±1.1367 +0.4000
Q5 Adoption Intention2.8000 ±1.36113.3500±1.3870 +0.5500
Overall3.1600 3.6200+0.4600
The human evaluation results showed that C3-Analog achieved higher mean scores than C3-Relational
across all evaluation criteria. The overall mean increased from 3.1600 to 3.6200, corresponding to a
mean difference of +0.4600. Adoption Intention exhibited the largest difference (+0.5500), followed
by Contextual Usefulness (+0.5000). These higher mean ratings were observed even though EF and
Structured Temporal Accuracy under C3-Analog were slightly lower than those under C3-Relational in
the preceding automatic evaluation. This suggests that historical analog information may provide users
with useful comparative context for interpreting and potentially using current predictions, even when
it does not further improve structured accuracy. Historical analogs should therefore be interpreted

primarily as complementary information that enhances human-level contextual usefulness rather than
as a mechanism for improving automatic faithfulness.
5. Conclusion
This study examined whether the reliability of financial XAI narratives can deteriorate when LLMs
are required to directly derive numerical changes and feature relations from raw XAI evidence, and
evaluated an approach that externalizes such reasoning burdens into verifiable evidence. SHAP based
temporal evidence was structured into numerical and relational information, while factual claims were
linked to Evidence IDs, enabling deterministic evaluation of faithfulness and reasoning accuracy without
relying on LLM-as-a-Judge.
The results showed that explicitly providing attribution changes and trend information improved
faithfulness and temporal reasoning relative to providing only raw temporal sequences, while externaliz-
ing feature relations further improved relational reasoning. These findings suggest that structuring error
prone reasoning steps into verifiable evidence can improve the reliability of financial XAI narratives.
Future work should examine whether these findings generalize to other predictive models and financial
decision making tasks.
Acknowledgments
This work was supported by the National Research Foundation of Korea (NRF) grant funded by the
Korea government (MSIT) (No. RS 2025-00554384), and the Technology Development Program (No. RS
2024-00513926) funded by the Ministry of SMEs and Startups (MSS, Korea).
References
[1] S. Baviskar, Conditional adversarial fragility in financial machine learning under macroeconomic
stress, 2025. doi:10.48550/arXiv.2512.19935.arXiv:2512.19935.
[2] S. M. Lundberg, S.-I. Lee, A unified approach to interpreting model predictions, Advances in
neural information processing systems 30 (2017).
[3] X. Zeng, K. Zhu, Enhancing the interpretability of shap values using large language models, arXiv
preprint arXiv:2409.00079 (2024).
[4] A. Zytek, S. Pido, S. Alnegheimish, L. Berti-Equille, K. Veeramachaneni, Explingo: Explaining
ai predictions using large language models, 2024 IEEE International Conference on Big Data
(BigData) (2024) 1197–1208.
[5] D. Martens, J. Hinns, C. Dams, M. Vergouwen, T. Evgeniou, Tell me a story! narrative-driven
xai with large language models, Decision Support Systems 191 (2025) 114402. URL: https://www.
sciencedirect.com/science/article/pii/S016792362500003X. doi:https://doi.org/10.1016/j.
dss.2025.114402.
[6] H. Jenett, C. Nagl, M. Nagl, S. M. Price, W. Schaefers, Dynamics of reit returns and volatility:
Analyzing time-varying drivers through an explainable machine learning approach, The Journal
of Real Estate Finance and Economics 72 (2026) 1–40.
[7] S. Khanna, A. Berger, M. Chopra, D. Berghaus, R. Sifa, History rhymes: Macro-contextual retrieval
for robust financial forecasting, 2025 IEEE International Conference on Big Data (BigData) (2025)
7196–7203.
[8] M. Strong, A. Vlachos, TSVer: A benchmark for fact verification against time-series evidence, in:
C. Christodoulopoulos, T. Chakraborty, C. Rose, V. Peng (Eds.), Proceedings of the 2025 Conference
on Empirical Methods in Natural Language Processing, Association for Computational Linguistics,
Suzhou, China, 2025, pp. 29906–29926. URL: https://aclanthology.org/2025.emnlp-main.1519/.
doi:10.18653/v1/2025.emnlp-main.1519.

[9] G. R. Pratama, K.-K. Tseng, Accurate ensembles, fragile narratives: Multi-scale stacking and a
fidelity audit of llm-generated explanations for credit risk, arXiv preprint arXiv:2608.08126 (2026).
[10] J. Kim, S. Park, Groupsegment-shap: Shapley value explanations with group-segment players for
multivariate time series, arXiv preprint arXiv:2601.06114 (2026).
[11] B. Goswami, A. Uddin, Significance of predictors: revisiting stock return predictions using
explainable ai, Annals of Operations Research 357 (2026) 223–257.
[12] C. Wang, Stock return prediction with multiple measures using neural network models, Financial
Innovation 10 (2024) 72.
[13] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin, B. Nair, R. Katz, J. Himmelfarb,
N. Bansal, S.-I. Lee, From local explanations to global understanding with explainable ai for trees,
Nature machine intelligence 2 (2020) 56–67.
[14] C. Mougan, K. Broelemann, D. Masip, G. Kasneci, T. Thiropanis, S. Staab, Explanation shift: How
did the distribution shift impact the model?, arXiv preprint arXiv:2303.08081 (2023).
[15] W. Geng, D. Liu, L. Li, Y. Wang, Evaluating large language models as post hoc explainability
interfaces for credit risk models, Expert Systems 43 (2026) e70351.
[16] T. Wang, Enhancing stock market prediction with temporal graph neural networks and large
language model-based explainability, Procedia Computer Science 274 (2025) 147–160. URL:
https://www.sciencedirect.com/science/article/pii/S1877050925037366. doi:https://doi.org/
10.1016/j.procs.2025.12.015.
[17] F. Lukassen, J. Herrmann, C. Weisser, A. Silbersdorff, B. Saefken, T. Kneib, Quality without
usefulness: Llm-generated xai narratives as trust heuristics rather than decision aids, arXiv
preprint arXiv:2605.26770 (2026).
[18] A. C. Teixeira, V. Marar, H. Yazdanpanah, A. Pezente, M. Ghassemi, Enhancing credit risk reports
generation using llms: An integration of bayesian networks and labeled guide prompting, 2023,
pp. 340–348.
[19] A. Kim, M. Muhn, V. Nikolaev, Financial statement analysis with large language models, arXiv
preprint arXiv:2407.17866 (2024).
[20] G. Fatouros, K. Metaxas, J. Soldatos, M. Karathanassis, Marketsenseai 2.0: Enhancing stock analysis
through llm agents, 2025 IEEE International Conference on Data Mining Workshops (ICDMW)
(2025) 883–892.
[21] S. Gu, B. Kelly, D. Xiu, Empirical asset pricing via machine learning, The Review of Financial
Studies 33 (2020) 2223–2273. doi:10.1093/rfs/hhaa009.
[22] P. Gray, M. Limkriangkrai, W. Xu, An examination of the characteristics versus covariance debate
for contemporary asset-pricing models: Australian evidence, Accounting & Finance 64 (2024)
3781–3802. doi:10.1111/acfi.13279.
[23] L. Gao, A. Madaan, S. Zhou, U. Alon, P. Liu, Y. Yang, J. Callan, G. Neubig, PAL: Program-aided
language models, in: A. Krause, E. Brunskill, K. Cho, B. Engelhardt, S. Sabato, J. Scarlett (Eds.),
Proceedings of the 40th International Conference on Machine Learning, volume 202 ofProceedings
of Machine Learning Research, PMLR, 2023, pp. 10764–10799. URL: https://proceedings.mlr.press/
v202/gao23f.html.
[24] A. Yang, et al., Qwen3 technical report, arXiv preprint arXiv:2505.09388 (2025). doi: 10.48550/
arXiv.2505.09388.arXiv:2505.09388.
[25] Mistral AI, Ministral 8b, Model Card, 2024. URL: https://huggingface.co/mistralai/
Ministral-8B-Instruct-2410.
[26] A. Grattafiori, et al., The llama 3 herd of models, arXiv preprint arXiv:2407.21783 (2024). doi: 10.
48550/arXiv.2407.21783.arXiv:2407.21783.

A. Stock Level Characteristic Definitions
For the price-based characteristics, we define the adjusted price variables as
𝑐𝑡 =
{︃
1,CFACPR 𝑡 = 0or missing,
CFACPR𝑡,otherwise.
adjp𝑡 =|PRC𝑡| 𝑐𝑡 ,adjhi 𝑡 =|ASKHI𝑡| 𝑐𝑡 ,adjlo 𝑡 =|BIDLO𝑡| 𝑐𝑡 .
Table 8: Definition and Construction of Stock-Level Characteristics
Feature Definition / Formula Measurement & Source
Price Level
lowest_bid|BIDLO 𝑡|Month𝑡
CRSP: BIDLO
highest_ask|ASKHI 𝑡|Month𝑡
CRSP: ASKHI
close_price|𝑃 𝑅𝐶 𝑡|Month𝑡
CRSP: PRC
ma3mean(𝑎𝑑 𝑗𝑝 𝑡−2:𝑡), minimum 2 observations Trailing 3 months
CRSP: PRC, CFACPR
ma12mean(𝑎𝑑 𝑗𝑝 𝑡−11:𝑡), minimum 6 observations Trailing 12 months
CRSP: PRC, CFACPR
Trend & Momentum
price_distance_ma12 𝑎𝑑 𝑗𝑝𝑡−𝑚𝑎12 𝑡
𝑚𝑎12𝑡
Month𝑡, relative to 12M MA
CRSP: PRC, CFACPR
high_12m_ratio 𝑎𝑑 𝑗𝑝𝑡
max(𝑎𝑑 𝑗𝑝𝑡−11:𝑡) Trailing 12 months CRSP: PRC, CFACPR
ma_cross+1if𝑚𝑎3 𝑡 > 𝑚𝑎12𝑡; otherwise−13M vs. 12M MA
CRSP: PRC, CFACPR
momentum12 𝑎𝑑 𝑗𝑝𝑡
𝑎𝑑 𝑗𝑝𝑡−12
−112-month lag
CRSP: PRC, CFACPR
mom1m𝑅𝐸𝑇 𝑡−1 Previous month
CRSP: RET
mom6mexp
(︃ 6∑︁
𝑘=1
log(1 +𝑅𝐸𝑇 𝑡−𝑘)
)︃
−1Previous 6 months
CRSP: RET
macd𝐸𝑀 𝐴 12(𝑎𝑑 𝑗𝑝)−𝐸𝑀 𝐴26(𝑎𝑑 𝑗𝑝)12M / 26M EMA
CRSP: PRC, CFACPR
signal_line𝐸𝑀 𝐴 9(𝑚𝑎𝑐𝑑)9M EMA
CRSP: PRC, CFACPR
Oscillator
Continued on next page

Table 8 (continued)
Feature Definition / Formula Measurement & Source
stochastic100× adjp𝑡−min 𝜏=𝑡−13,...,𝑡 adjp𝜏
max𝜏=𝑡−13,...,𝑡 adjp𝜏−min 𝜏=𝑡−13,...,𝑡 adjp𝜏
Trailing 14 months; minimum 6
valid observations
CRSP: PRC, CFACPR
rsi
𝑑𝑡 = adjp 𝑡−adjp 𝑡−1,
𝑔𝑡 = max(𝑑 𝑡,0), ℓ 𝑡 = max(−𝑑 𝑡,0),
𝐺𝑡 = 1 14
13∑︁
𝑘=0
𝑔𝑡−𝑘,
𝐿𝑡 = 1 14
13∑︁
𝑘=0
ℓ𝑡−𝑘,
𝑅𝑆𝐼𝑡 = 100− 100 1 +𝐺 𝑡/𝐿𝑡 .
Trailing 14 months
CRSP: PRC, CFACPR
Volatility & Risk
volatility_12std(𝑅𝐸𝑇 𝑡−11:𝑡)Trailing 12 months
CRSP: RET
parkinson_vol
√︃
1
4 ln 2 mean𝜏=𝑡−11,...,𝑡
[︂
ln2
(︂ adjhi𝜏
adjlo𝜏
)︂]︂
Trailing 12 months
CRSP: ASKHI, BIDLO, CFACPR
bb_width 4 std(𝑎𝑑 𝑗𝑝𝑡−11:𝑡) 𝑚𝑎12𝑡 Trailing 12 months CRSP: PRC, CFACPR
atr
TR𝑡 = max{adjhi 𝑡−adjlo 𝑡,
|adjhi𝑡−adjp 𝑡−1|,
|adjlo𝑡−adjp 𝑡−1|},
ATR𝑡 = EMA 14(TR𝑡)
14-month EMA
CRSP: ASKHI, BIDLO,
PRC, CFACPR
beta60m𝛽 𝑖,𝑡 = Cov𝜏=𝑡−60,...,𝑡−1 (𝑅𝐸𝑇𝑖,𝜏 , 𝑉 𝑊 𝑅𝐸𝑇 𝐷𝜏 ) Var𝜏=𝑡−60,...,𝑡−1 (𝑉 𝑊 𝑅𝐸𝑇 𝐷𝜏 ) Trailing 60 months CRSP: RET, VWRETD
retskew12mskew(𝑅𝐸𝑇 𝑡−12:𝑡−1)Previous 12 months
CRSP: RET
maxret12mmax(𝑅𝐸𝑇 𝑡−12:𝑡−1)Previous 12 months
CRSP: RET
Volume & Liquidity
volume𝑉 𝑂𝐿 𝑡 Month𝑡
CRSP: VOL
volume_ma12mean(𝑉 𝑂𝐿 𝑡−11:𝑡)Trailing 12 months
CRSP: VOL
volume_ratio 𝑉 𝑂𝐿𝑡
𝑣𝑜𝑙𝑢𝑚𝑒_𝑚𝑎12𝑡
Month𝑡, relative to 12M mean
CRSP: VOL
obv_normalized
𝑂𝐵𝑉 𝑡 =
∑︁
𝜏≤𝑡
sign(𝑅𝐸𝑇 𝜏 )𝑉 𝑂𝐿𝜏 ,
𝑂𝐵𝑉 𝑛𝑜𝑟𝑚 𝑡 = 𝑂𝐵𝑉 𝑡−ExpMean(𝑂𝐵𝑉) 𝑡 ExpStd(𝑂𝐵𝑉) 𝑡 + 10−12 . Expanding window CRSP: RET, VOL
turnover_ratio 𝑉 𝑂𝐿𝑡
𝑆𝐻𝑅𝑂𝑈 𝑇𝑡
Month𝑡
CRSP: VOL, SHROUT
dolvol|𝑃 𝑅𝐶 𝑡|×𝑉 𝑂𝐿𝑡 Month𝑡
CRSP: PRC, VOL
Continued on next page

Table 8 (continued)
Feature Definition / Formula Measurement & Source
amihud |𝑅𝐸𝑇𝑡| 𝑑𝑜𝑙𝑣𝑜𝑙𝑡 Month𝑡 CRSP: RET, PRC, VOL
bidask 𝐴𝑆𝐾𝑡−𝐵𝐼𝐷 𝑡
(𝐴𝑆𝐾𝑡 +𝐵𝐼𝐷 𝑡)/2 Month-end𝑡 CRSP: BID, ASK
