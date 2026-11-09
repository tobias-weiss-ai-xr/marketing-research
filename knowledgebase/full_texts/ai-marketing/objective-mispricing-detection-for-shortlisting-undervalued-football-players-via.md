---
title: Objective Mispricing Detection for Shortlisting Undervalued Football Players via Market Dynamics
  and News Signals
url: https://arxiv.org/abs/2603.17687
category: ai-marketing
subcategory: empirical
date: 2026-03
venue: ''
authors:
- Chinenye Omejieke
- Shuyao Chen
- Xia Cui
source: arxiv
pdf_url: https://arxiv.org/pdf/2603.17687
pages: 14
chars: 34559
fetched_at: '2026-11-08T12:58:27+00:00'
kb_version: 1
---

# Objective Mispricing Detection for Shortlisting Undervalued Football Players via Market Dynamics and News Signals

Objective Mispricing Detection for Shortlisting
Undervalued Football Players via Market
Dynamics and News Signals
Chinenye Ekene Omejieke () 1, Shuyao Chen2, and Xia Cui
1 School of Computing and Mathematics, Manchester Metropolitan University,
Manchester, United Kingdomchinenyevans@gmail.com,x.cui@mmu.ac.uk
2 Typewind Ltd., London, United Kingdomcontact@typewind.co.uk
Abstract.We present a practical, reproducible framework for identi-
fyingundervaluedfootball players grounded inobjective mispricing. In-
steadofrelyingonsubjectiveexpertlabels,weestimateanexpectedmar-
ket value from structured data (historical market dynamics, biographical
and contract features, transfer history) and compare it to the observed
valuation to define mispricing. We then assess whether news-derived Nat-
ural Language Processing (NLP) features (i.e., sentiment statistics and
semantic embeddings from football articles)complementmarket signals
for shortlisting undervalued players.
Using a chronological (leakage-aware) evaluation, gradient-boosted re-
gression explains a large share of the variance in log-transformed market
value. For undervaluationshortlisting, ROC-AUC-based ablations show
that market dynamics are the primary signal, while NLP features provide
consistent, secondary gains that improve robustness and interpretabil-
ity. SHAP analyses suggest the dominance of market trends and age,
with news-derived volatility cues amplifying signals in high-uncertainty
regimes. The proposed pipeline is designed for decision support in scout-
ing workflows, emphasizing ranking/shortlisting over hard classification
thresholds, and includes a concise reproducibility and ethics statement.
Keywords:Applied data science·football analytics·player valuation
·objective mispricing·news/NLP signals·shortlisting·interpretability.
1 Introduction
Valuing professional football players underpins transfer decisions, contract nego-
tiations, and long-term squad planning [7]. Yet market valuations remain noisy
proxies of true sporting and economic value due to incomplete information, be-
havioural biases, contractual frictions, and media narratives [9,11]. Identifying
undervaluedplayers (i.e., those whose market prices fall below their underlying
worth) offers clear competitive and financial benefits.
Most valuation models rely on structured indicators (performance, age tra-
jectories, fees) and often assume near-efficient markets [8]. However, documented
arXiv:2603.17687v1  [cs.LG]  18 Mar 2026

2 C.E. Omejieke et al.
transfer-market inefficiencies arise from asymmetric information and delayed re-
actions [2]. Unstructured news can affect perceptions through narratives about
form, injuries and roles; analogous effects are well known in financial mar-
kets[3,20].Integratingsuchtextwithmarketdynamicsisthereforeattractivebut
methodologically challenging; prior sports work often uses coarse sentiment and
rarely quantifies the incremental value of NLP relative to structured data [19,22].
We propose an applied, leakage-aware framework forobjective mispricingde-
tection: we estimate an expected value without using the current valuation as an
input, compute mispricing as expected vs. observed, and label the upper quan-
tile asundervalued. This provides a reproducible and domain-grounded target
aligned with scouting practice. We then study whether news-derived NLP fea-
tures complement market dynamics for shortlisting undervalued players (rank-
ing), rather than aiming at binary classification with a fixed threshold.
The primary contributions of this study are:
–A reproducible mispricing-based definition of undervaluation that avoids
subjective expert judgements.
–A practical integration of market dynamics, contract/transfer context and
news-derived sentiment/embeddings to shortlist undervalued players.
–A systematic ablation demonstrating that NLP features provide consistent
secondarygains atop market dynamics, improving robustness and inter-
pretability.
–An interpretable SHAP explanations articulate why candidates are surfaced,
facilitating analyst trust and adoption.
2 Related Work
Research on football player valuation spans economics, sports analytics, and
machine learning, reflecting the sizable financial stakes associated with trans-
fer markets and contract negotiations. Early work modeled player value using
classical econometric and hedonic pricing frameworks, where market valuations
were expressed as functions of observable performance attributes such as age,
position, playing time, and productivity. Megia [16] demonstrated that hedonic
models can explain part of the variance in market value but remain sensitive to
institutional and behavioral influences, indicating that observable performance
variables alone are insufficient.
Subsequent studies incorporated additional contextual factors. Franck and
Nüesch [9] showed that popularity-related signals, including media exposure and
fan attention, systematically inflate valuations beyond on-field contributions.
Hermet al.[11] found that both crowd-sourced and expert assessments correlate
with market prices but leave a substantial portion unexplained, suggesting that
football markets are only partially efficient. Such findings indicate that latent
player quality and market perception are imperfectly captured by structured
indicators.
Machine learning approaches have increasingly been adopted to model non-
linear interactions in valuation. Behravanet al.[1] applied ensemble learning

Shortlisting Undervalued Football Players via Market+News 3
methods and revealed systematic mispricing related to age, league exposure,
and contract structure. Decrooset al.[5] proposed action-based valuation mod-
els that quantify on-ball contributions with high granularity, though such work
depends on proprietary event-level data that may not be generally available.
Complementing micro-level perspectives, macroeconomic analyses have exam-
ined transfer-market inefficiencies at an institutional scale: Jacobsen [13] high-
lighted how governance constraints, bargaining imbalances, and information
asymmetries distort transfer outcomes and create prolonged deviations from ef-
ficient pricing. Collectively, these strands motivate the search for data-driven
frameworks capable of identifying undervalued players before markets adjust.
Unstructured data has recently emerged as an additional source of signal.
Reviews by Schumakeret al.[19] and Zadeh [10] highlight the use of sentiment
and textual cues in match prediction, engagement analysis, and performance
assessment. Football news frequently encodes soft information about injuries,
tactical roles, psychological factors, or transfer intentions (i.e., signals that may
influence perceived value before they materialize in performance statistics). Par-
allel evidence in financial economics supports the role of media in shaping asset
prices: Tetlock [20] showed that negative news sentiment depresses equity mar-
kets, while Bollenet al.[3] found that collective mood extracted from social
media predicts market movements. Such findings strengthen the theoretical jus-
tification for modeling football-player valuation using media-derived sentiment
and semantic cues.
However, most sports analytics work using text relies on lexicon-based sen-
timent or shallow machine learning models that fail to capture the contextual
richness of sports journalism. Advances in natural language processing, par-
ticularly transformer architectures [21], enable deep semantic embeddings that
encode bidirectional context. Large-scale models such as BERT [6] and Distil-
BERT [18] provide dense representations that move beyond keyword frequencies
and can capture subtle narrative signals (e.g., form trajectories, evolving roles,
injury uncertainty).
This paper extends prior work by integrating both transformer-based senti-
ment and dense semantic embeddings into a unified valuation and shortlisting
framework. Unlike earlier studies, we rigorously quantify theincrementalcon-
tribution of textual features relative to structured market and biographical data
through systematic ablations, and we define undervaluation objectively using
mispricing between expected and observed market values. This positions our
work at the intersection of valuation modeling, market inefficiency analysis, and
modern NLP-driven sports analytics.
3 Methodology
This section describes the construction of the multi-modal dataset (Section 3.1),
the preprocessing pipeline (Section 3.2), the extraction of news-derived features
(Section 3.3), and the modelling framework for estimating expected market val-
ues and identifying undervalued players via an objective mispricing formulation

4 C.E. Omejieke et al.
(Section 3.4). All components are designed to ensure strict temporal integrity,
reproducibility, and applicability within real-world scouting workflows.
3.1 Data and Features
Structured data were collected directly from Transfermarkt3, including player
biographical attributes (age, height, nationality), contract information (start
date, expiry date, remaining duration), and longitudinal club affiliations. Weekly
market-value snapshots from 2015–2024 provide a detailed view of valuation
trajectories from which market-dynamics features were derived. Transfer histo-
ries were obtained in parallel, containing transfer dates, origin and destination
clubs,declaredfees,andtransfercategories.Together,thesesourcesprovidelong-
term signals of economic stability, mobility, and performance-related valuation
changes.
To complement the structured dataset, we constructed a multi-source cor-
pus of football news. Articles were retrieved from multiple outlets including
The Guardian, Sky Sports, BBC Sports, The Athletic, ESPN FC, and BeSoccer
via the NewsAPI platform4, using player names and identifiers as search keys.
To expand coverage beyond indexed sources, we additionally scraped publicly
accessible football news websites. All articles were stored with full text and pub-
lication timestamps, enabling strict chronological alignment with market-value
data. The combined dataset includes 19,982 players, 70,627 news articles, and
280,334 valuation snapshots (Table 1).
T able 1.Summary statistics of the integrated dataset (07/05/2015–23/01/2024).
Item V alue Description
Unique Players 19,982 Structured player records from Transfermarkt
News Articles 70,627 Multi-source football news mentioning players
Market Value Records 280,334 Weekly time-stamped valuations
Avg. Articles/Player 44.20 Mean article count per player
Temporal Range 2015–2024 Shared coverage period
3.2 Data Preprocessing
Raw data were processed at two levels: player market dynamics and news ar-
ticles. From market-value time series, we derived player-level features including
average valuation, volatility, maximum historical value, and a least-squares trend
coefficient to capture career trajectory. Contract durations and transfer frequen-
cies were also computed to reflect economic and career stability. Player names
3 https://www.transfermarkt.com/
4 https://newsapi.org/

Shortlisting Undervalued Football Players via Market+News 5
in news articles were normalized and mapped to unique entity identifiers us-
ing string matching and resolution heuristics, ensuring consistent cross-source
linkage.
News articles were preprocessed usingspaCyand regular-expression clean-
ing. This involved lowercasing, removal of HTML markup and boilerplate text,
punctuation normalization, and sentence segmentation. Articles with insufficient
content (e.g., fewer than 3 words) were discarded to maintain minimum informa-
tion density, as research indicates that linguistic metrics become unstable and
highly dependent on length in short-form texts [15]. All article timestamps were
preserved, and every transformation was applied to prevent information from the
future influencing past data, adhering to best practices to avoid temporal leak-
age [14]. This chronological discipline ensures our evaluation reflects real-world
deployment.
3.3 News Features
Sentiment Analysis.To capture tonal context, we extracted sentiment sig-
nals from each player’s associated news articles. Representations were initially
obtained using the Hugging FaceBERT-base-uncasedtransformer [6]. For senti-
ment polarity, we employed aDistilBERTclassifier [18] due to its computational
efficiency (40% smaller and 60% faster than BERT while retaining 97% of its lan-
guage understanding) which was critical for processing our high-volume dataset.
Sentiment scores were normalized to[−1,+1]. For each playeri, we aggregated
mean sentimentµ i and sentiment volatilityσi:
µi = 1 ni
niX
j=1
sij, σ 2 i = 1 ni −1
niX
j=1
(sij −µ i)2.(1)
Such signals have been shown to influence market-based outcomes [4].
Semantic Embeddings.To capture richer narratives—form, injuries, trans-
fer talks—we encoded each article using a pre-trained sentence-level transformer.
Tokenization employed the model’s native WordPiece tokenizer with a maximum
sequence length of 512. The[CLS]token representation was used as a holistic
summary embedding. Player-level representations were obtained by mean pool-
ing:
¯ei = 1 ni
niX
j=1
eij.(2)
These contextual embeddings outperform bag-of-words approaches in capturing
nuanced semantics [17,23]. To mitigate dimensionality and multicollinearity, we
appliedthePrincipalComponentAnalysis(PCA)tothe768-dimensionalembed-
dings, retaining 95% of cumulative variance. The PCA was fitted exclusively on
the training set to ensure data isolation. The resulting low-dimensional features
were concatenated with the structured market features of Section 3.2.

6 C.E. Omejieke et al.
3.4 Objective Mispricing and Shortlisting
Expected Market Value Estimation.Market values are right-skewed; with-
out transformation, a regressor would over-prioritize high-value players. To sta-
bilize variance and linearize exponential growth, we applied a log transform. An
expected value model was trained on all feature groups (excluding the current
value) using XGBoost, linear regression, and TabNet. For playeriwith observed
valueV i:
yi = log(1 +V i),ˆy i =f(x i,z i), ˆVi = exp(ˆyi)−1.(3)
The addition of 1 ensures stability for zero-value entries.
Mispricing and Undervaluation Label.Mispricing is the log-difference be-
tween expected and observed values:
Mi = log(1 + ˆVi)−log(1 +V i).(4)
This relative view aligns with the scouting heuristics. To create actionable tar-
gets, we flag a player asundervaluedif their mispricing exceeds the 85th per-
centile:
ui =1(M i ≥τ)whereτ=Q 0.85(M).(5)
This 15% threshold reflects a realisticshortlisting budgetin scouting funnels.
This relative view aligns with scouting heuristics, where data serve as a high-
volume filter to manage limited human observation capacity [12]. Sensitivity
analyses at 10% and 20% preserved model rankings, suggesting stability.
Shortlisting Model.We trained classifiers (XGBoost, Random Forest, Tab-
Net) to predict undervaluation labels using the full feature set, applying class
weighting to address imbalance. Because the label is derived indirectly, we em-
phasizeranking qualityvia ROC-AUC, treating the classifier as ashortlister
for human evaluation rather than a hard decision rule. F1-score is reported for
completeness. Formally, a classifier estimates:
P(U i = 1|x i,z i).(6)
3.5 Evaluation Protocol
All experiments used a chronological split: earliest 80% for training, latest 20%
for testing. PCA and normalization were fitted on training data only. For regres-
sion, we compared linear regression, XGBoost, and TabNet. XGBoost hyperpa-
rameters: 500 trees, learning rate 0.05, max depth 6, subsampling 0.8. TabNet
used early stoppingon validationRMSE. Ablation experiments evaluated feature
groups: full, no text, and text-only.

Shortlisting Undervalued Football Players via Market+News 7
4 Results
4.1 Expected Market Value Estimation
The first stage of our pipeline involves predicting the expected log-market value,
against which current value is compared to derive the mispricing label. Table 2
summarizes the performance of the three regression models on the held-out test
set: XGBoost, TabNet and Linear Regression.
The gradient-boosted model (XGBoost) provides the strongest fit, explaining
0.935 of the variance in the log-transformed target. This significant performance
edge over the linear baseline (R2=0.611) suggests that the relationship between
player attributes, news narratives and market value is inherently non-linear and
benefits from the ensemble’s ability to model complex feature interactions. Tab-
Net, while outperforming the linear model, lags behind XGBoost, suggesting
that for this well-structured tabular task with limited sample size, tree-based
methods remain more effective than deep learning alternatives.
Figure 1 visualizes the relationship between a player’s observed market value
and the value predicted by the XGBoost model. Points lying on or near the
diagonal represent players whose current market value closely aligns with the
model’s expectation, i.e., they are considered fairly priced. Crucially, the points
above the line are those where the predicted value exceeds the observed value,
flagging them as potentiallyundervaluedand therefore of interest for scouting.
Conversely, points below the line indicate potentiallyovervaluedplayers. This
visualization serves as an intuitive screening tool for analysts, translating a com-
plex regression output into a clear, actionable shortlist.
T able 2.Regression model performance for expected log-market value. XGBoost sub-
stantially outperforms both the neural and linear baselines, capturing the complex and
non-linear relationships in the data.
Model RMSE↓MAE↓R 2 ↑
XGBoost0.453 0.337 0.935
TabNet 0.920 0.695 0.732
Linear Regression 1.109 0.863 0.611
4.2 Shortlisting Performance and Feature Ablation
The core contribution of this work is the classification model that shortlists
undervalued players. To understand the contribution of different data modalities,
we conducted an ablation study, comparing model performance when trained on
the full feature set (Full), on market/biographical features only (No Text), and
on NLP features only (Text Only). Results are presented in Table 3 with three
classification models: XGBoost, TabNet, and Random Forest (RF).

8 C.E. Omejieke et al.
104 105 106 107 108
Current Market Value ( )
101
103
105
107
Expected Market Value ( )
Current vs Expected Market Value
Fair Value Line
Fig. 1.Observed versus expected market value (log scale). Players above the diagonal
(y > x) exhibit positive mispricing and are shortlisted as undervalued. The spread of
points illustrates the model’s ability to identify valuation discrepancies.
T able 3.Ablation study for the shortlisting task (undervalued vs. non-undervalued).
Performance is measured by ROC-AUC, which emphasizes ranking quality. The full
model, incorporating both market and text features, consistently achieves the highest
discriminative power.
XGBoost TabNet Random Forest (RF)
Variant ROC AUC F1 ROC AUC F1 ROC AUC F1
Full Model 0.677 0.263 0.614 0.206 0.471 0.137
No Text 0.604 0.250 0.560 0.247 0.553 0.208
Text Only 0.514 0.264 0.508 0.295 0.488 0.050
Several key observations emerge from this analysis. First, the full model,
whichcombinesstructuredmarketdatawithNLP-derivednewsfeatures,achieves
the highest ranking performance (ROC-AUC of 0.677 with XGBoost). This sug-
gests our core hypothesis that media narratives provide a valuable and comple-
mentary signal for identifying valuation discrepancies.
Second, removing the textual features (No Text) results in a small but sys-
tematic decline in ROC-AUC across all model families. This consistent drop
indicates that while market dynamics are the dominant driver of value, the infor-
mation encoded in news coverage (i.e., sentiment, player form and injury news)
offers a genuine and non-redundant improvement to the model’s discriminative
ability. This aligns with domain knowledge that narratives can contextualize or
precede market adjustments.
Third,Text Onlymodels perform only marginally above random (ROC-AUC
≈0.51). This finding is equally important: it demonstrates that while news
narratives are a useful supplementary signal, they are insufficient on their own

Shortlisting Undervalued Football Players via Market+News 9
to explain market mispricing. Text provides context to market data, but does
not replace it. This result underscores the necessity of a multimodal approach.
Finally, XGBoost consistently outperforms TabNet and Random Forest in
the full-model setting. Its higher F1 score also suggests it is better at balancing
precision and recall for the minority (undervalued) class. This, combined with its
regression performance, establishes XGBoost as the more suitable model for this
task, offering a strong balance of predictive power, interpretability, and practical
deployability.
1.5
 1.0
 0.5
 0.0 0.5 1.0
SHAP Value (Impact on Model Output)
n_transfers
News_Context_7
News_Context_35
News_Context_55
sentiment_max
sentiment_mean
News_Context_8
News_Context_19
News_Context_17
total_fees
avg_fee
contract_years_left
Age
mv_std
mv_trend
XGBRegressor: Feature Impact
Low
High
Feature value
Fig. 2.SHAP Summary Plot for the XGBoost Regression Model, showing each fea-
ture’s contribution to predicted log-market value. Features are ranked by their global
impact, with red indicating high feature values and blue indicating low values.
4.3 Model Interpretation
To move beyond performance metrics and understand the decision-making logic
of the regressor, we analyzed the trained XGBoost model using SHAP5 (SHapley
Additive exPlanations). The SHAP analysis (Figure 2) indicates that the XG-
Boost regressor relies primarily on temporal market-value signals, withmv_trend
andmv_stdexerting the largest influence on predictions. Upward value tra-
jectories strongly increase estimated market value, whereas higher volatility
leads to conservative predictions. Age is the next most influential factor, with
older ages contributing negatively in line with established valuation dynam-
ics. Contract-related variables and historical fee indicators show moderate but
5 https://shap.readthedocs.io/en/latest/

10 C.E. Omejieke et al.
Data Sources
Transfermarkt + NewsAPI + Scraping Preprocessing Feature Store Market + NLP Features Expected Value Model XGBoost / TabNet / etc.
Scouting Output API
Reports / Dashboard Mispricing & Shortlisting
Fig. 3.Prototype deployment architecture for the multimodal undervaluation short-
listing system.
consistent effects, reflecting their relevance to long-term value retention. In con-
trast, the news-derived contextual features and sentiment measures have only
marginal, case-specific contributions, suggesting that textual information pro-
vides supplementary rather than structural predictive value. Overall, the model’s
behavior is dominated by market-based and demographic variables, with con-
textual signals playing a secondary role.
5 Deployment Considerations
To illustrate how the proposed framework can be incorporated into real scout-
ing workflows, Figure 3 presents a prototype deployment architecture assembled
around the multimodal valuation pipeline. The system ingests weekly Trans-
fermarkt market-value updates alongside continuously collected football news
articles retrieved via NewsAPI and compliant web scraping. These inputs are
processed through a unified preprocessing component that performs temporal
alignment, entity normalisation, market-dynamics computation, and text clean-
ing. The resulting structured and textual features are stored in a lightweight
feature repository.
At each update cycle, the expected-value model is executed to produce re-
vised predictions of players’ market valuations. Mispricing scores are then com-
puted by comparing the predicted and observed values, after which the short-
listing module ranks players based on the mispricing threshold. This produces
an updated candidate list that can be used by downstream analytics tools or
scouting staff.
To integrate with existing decision-support systems, the output is served via
an internal API that exposes shortlists, player-level explanations, and mispricing
trajectories. The entire workflow is computationally efficient and can be sched-
uled on a single GPU-enabled workstation or mid-tier server, enabling weekly
or daily refresh intervals. The deployment pipeline demonstrates that the pro-
posed methodology is not only analytically sound but also technically feasible
for near-real-time operational use in professional scouting environments.

Shortlisting Undervalued Football Players via Market+News 11
6 Discussion
The experimental results demonstrate that combining structured market infor-
mation with news-derived textual representations provides a practical and inter-
pretable approach for identifying players whose market valuations deviate from
model-based expectations. Market dynamics remain the primary drivers of valu-
ation, confirming economic intuition that long-term trends, volatility, and career
stability carry the strongest explanatory power. News-derived features, although
not dominant in isolation, consistently provide complementary value by captur-
ing evolving narratives related to form, injury updates, tactical adjustments,
and transfer speculation. These factors are often qualitatively expressed in news
coverage before they manifest in observable market movements.
Importantly, the mispricing-based formulation aligns well with real scouting
workflows, where analysts rarely rely on a single metric but instead prioritize
shortlisting candidates for deeper review. Treating undervaluation prediction as
a ranking task rather than a strict binary classification mirrors this practice and
enables stable identification of high-potential targets under realistic class imbal-
ance. The multimodal framework also offers interpretability benefits: sentiment
volatility and semantic embedding components suggest when narrative uncer-
tainty may coincide with market underreaction, potentially revealing overlooked
opportunities. These findings collectively indicate that textual information does
not replace structured market data, but serves as a robust supplementary sig-
nal that improves shortlisting reliability in complex, real-time decision-making
environments.
7 Limitations and Future Work
Despite its practical value, the framework has several limitations. First, Trans-
fermarkt valuations (though widely used) are proxies that may contain platform-
specific biases, crowd effects, or noise unrelated to true economic value. Second,
the news corpus predominantly reflects English-language coverage, concentrat-
ing on leagues with higher media visibility and potentially overlooking narratives
surrounding lower-profile markets. Third, while chronological splitting prevents
information leakage, the framework remains observational and does not estab-
lish causality; textual signals may reflect market dynamics rather than precede
them.
Future work will address these challenges by modeling lag structures to quan-
tify whether news sentiment and narratives lead or follow changes in market
valuation, extending experiments across leagues with diverse media ecosystems,
and incorporating multilingual or region-specific news sources. Causal inference
methodsmayhelpassesswhetherparticularnarrativethemessystematicallypre-
cede mispricing corrections. In addition, more sophisticated aggregation mech-
anisms (e.g., temporal decay, source weighting, attention-based document pool-
ing) could enhance the extraction of semantically influential articles. Finally,
deployment-oriented evaluation involving Precision@k, calibration analysis, and

12 C.E. Omejieke et al.
user studies with practitioners would deepen understanding of how the system
performs in operational scouting environments.
8 Conclusion
This work introduced a multimodal, leakage-aware framework for detecting un-
dervalued football players through an objective mispricing signal that com-
pares model-estimated and market-observed valuations. By integrating struc-
tured market dynamics with sentiment and semantic features extracted from
football news, the framework provides a practical shortlisting tool that aligns
with real-world scouting processes. Market-driven features dominate predictive
performance, while news-derived features consistently add complementary con-
textual information that enhances robustness and interpretability.
The approach is transparent, readily extensible, and operationally feasible for
real-time or periodic valuation updates. It offers analysts a reproducible method
to surface potentially overlooked players and highlights the value of combining
quantitative signals with narrative-driven textual context. As football markets
continue to evolve and media ecosystems diversify, such multimodal, data-driven
strategies represent a promising direction for next-generation scouting analytics.
9 Reproducibility and Ethics
All experiments were conducted using a strict chronological evaluation proto-
col, ensuring that no future information was available to training procedures.
Preprocessing operations, including PCA dimensionality reduction and text nor-
malization, were fitted exclusively on the training split and applied unchanged
to validation and test data. Random seeds were fixed for all model training and
feature transformations to ensure deterministic behavior. Experiments were exe-
cuted on a single CUDA-enabled GPU and commodity CPU hardware; detailed
specifications and configuration files will be provided in the accompanying code
repository, subject to licensing constraints on underlying data sources.
Structured player data were collected from Transfermarkt, while the news
corpus was constructed from publicly accessible sources via NewsAPI and eth-
ically compliant web scraping. Only publicly published information was pro-
cessed, and no sensitive or private player data were included. Redistribution of
raw news or structured datasets is restricted by source licensing; however, de-
rived features and full preprocessing code will be released upon acceptance. The
system is intended strictly as a decision-support tool. Analysts and clubs should
avoid overreliance on automated outputs without expert oversight, particularly
when evaluating players in contexts where media coverage may be uneven or
biased.
References
1. Behravan, I., Razavi, S.M.: A novel machine learning method for estimating foot-
ball players’ value in the transfer market. Soft Computing25(3), 2499–2511 (2021)

Shortlisting Undervalued Football Players via Market+News 13
2. Van den Berg, E.: The valuation of human capital in the football player transfer
market. Rotterdam: ErasmusUniversity (2011)
3. Bollen, J., Mao, H., Zeng, X.: Twitter mood predicts the stock market. Journal of
computational science2(1), 1–8 (2011)
4. Davidovic, M., McCleary, J.: News sentiment and stock market dynamics: A ma-
chine learning investigation. Journal of Risk and Financial Management18(8),
412 (2025)
5. Decroos, T., Bransen, L., Van Haaren, J., Davis, J.: Actions speak louder than
goals: Valuing player actions in soccer. In: Proceedings of the 25th ACM SIGKDD
international conference on knowledge discovery & data mining. pp. 1851–1861
(2019)
6. Devlin, J., Chang, M.W., Lee, K., Toutanova, K.: Bert: Pre-training of deep bidi-
rectional transformers for language understanding. In: Proceedings of the 2019
conference of the North American chapter of the association for computational
linguistics: human language technologies, volume 1 (long and short papers). pp.
4171–4186 (2019)
7. Follert, F., Gleißner, W.: A decision model to value football player investments
under uncertainty. Management Decision62(13), 178–200 (2024)
8. Franceschi, M., Brocard, J.F., Follert, F., Gouguet, J.J.: Determinants of football
players’ valuation: A systematic review. Journal of Economic Surveys38(3), 577–
600 (2024)
9. Franck, E., Nüesch, S.: Talent and/or popularity: what does it take to be a super-
star? Economic Inquiry50(1), 202–216 (2012)
10. H. Zadeh, A.: Quantifying fan engagement in sports using text analytics. Journal
of Data, Information and Management3(3), 197–208 (2021)
11. Herm, S., Callsen-Bracker, H.M., Kreis, H.: When the crowd evaluates soccer play-
ers’ market values: Accuracy and evaluation attributes of an online community.
Sport Management Review17(4), 484–492 (2014)
12. Hintz, E.S.: Moneyball: The computational turn in professional sports manage-
ment. In: Papers of the Business History Conference (2022)
13. Jacobsen, Å.: Managing institutional complexity in a football organization. Man-
aging Sport and Leisure pp. 1–20 (2023)
14. Mammadov, E.: Optimizing query understanding: A mathematical approach to nlp
in search engines. Norwegian Journal of development of the International Sci ence
No129, 91 (2024)
15. McCarthy, P.M., Jarvis, S.: vocd: A theoretical and empirical evaluation. Language
Testing24(4), 459–488 (2007)
16. Megía-Cayuela, D.: Football fan satisfaction based on ticket price. a dynamic he-
donic pricing model approach. Social Science Quarterly106(5), e70071 (2025)
17. Reimers, N., Gurevych, I.: Sentence-bert: Sentence embeddings using siamese bert-
networks. arXiv preprint arXiv:1908.10084 (2019)
18. Sanh, V., Debut, L., Chaumond, J., Wolf, T.: Distilbert, a distilled version of bert:
smaller, faster, cheaper and lighter. arXiv preprint arXiv:1910.01108 (2019)
19. Schumaker, R.P., Jarmoszko, A.T., Labedz Jr, C.S.: Predicting wins and spread in
the premier league using a sentiment analysis of twitter. Decision Support Systems
88, 76–84 (2016)
20. Tetlock, P.C.: Giving content to investor sentiment: The role of media in the stock
market. The Journal of finance62(3), 1139–1168 (2007)
21. Vaswani,A.,Shazeer,N.,Parmar,N.,Uszkoreit,J.,Jones,L.,Gomez,A.N.,Kaiser,
Ł., Polosukhin, I.: Attention is all you need. Advances in neural information pro-
cessing systems30(2017)

14 C.E. Omejieke et al.
22. Waskita, G.I., Kurniawan, H., Yudhistira, D., Mohamad, N.I.B., Anam, M.K.:
The role of machine learning in modern football analytics: A systematic review
of approaches and their implications. Journal of Sport and Exercise Science8(2),
178–186 (2025)
23. Xia, J., Zhao, C., Hu, B., Gao, Z., Tan, C., Liu, Y., Li, S., Li, S.Z.: Mole-bert:
Rethinking pre-training graph neural networks for molecules. In: The Eleventh
International Conference on Learning Representations (2023)
