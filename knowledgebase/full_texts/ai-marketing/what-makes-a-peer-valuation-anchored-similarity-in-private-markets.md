---
title: What Makes a Peer? Valuation-Anchored Similarity in Private Markets
url: https://arxiv.org/abs/2608.12594
category: ai-marketing
subcategory: empirical
date: 2026-08
venue: ''
authors:
- Sebastian Frank
- Jingrao Lyu
- Max Jarmey
- Preetha Saha
- Mingshu Li
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.12594
pages: 9
chars: 43103
fetched_at: '2026-11-08T13:04:07+00:00'
kb_version: 1
---

# What Makes a Peer? Valuation-Anchored Similarity in Private Markets

What Makes a Peer? Valuation-Anchored Similarity in Private
Markets
Sebastian Frank
sebastian.frank@blackrock.com
BlackRock, Inc.
New York, NY, USA
Jingrao Lyu
jingrao.lyu@blackrock.com
BlackRock, Inc.
Atlanta, GA, USA
Max Jarmey
max.jarmey@blackrock.com
BlackRock, Inc.
London, UK
Preetha Saha
preetha.saha@blackrock.com
BlackRock, Inc.
New York, NY, USA
Mingshu Li
mingshu.li@blackrock.com
BlackRock, Inc.
Atlanta, GA, USA
Sweet Kaur
sweet.kaur@blackrock.com
BlackRock, Inc.
Gurgaon, HR, India
Sola Akinola
sola.akinola@blackrock.com
BlackRock, Inc.
New York, NY, USA
Dhagash Mehta
dhagash.mehta@blackrock.com
BlackRock, Inc.
New York, NY, USA
Abstract
As more investors contemplate private markets and contend with
limited transparency, sparse disclosures, and infrequent transac-
tions, identifying economically meaningful peer companies for
comparison is a fundamental challenge for valuation, due diligence,
portfolio construction, and risk management. We propose an en-
semble tree-based supervised similarity learning framework that
defines company similarity through the lens of market valuation
rather than static feature matching or semantic descriptions. Specif-
ically, we train a CatBoost gradient-boosted decision tree model
on observed private company valuations and derive a valuation-
aware similarity metric from importance-weighted leaf-node co-
occurrences across the ensemble. The similarity metric captures
shared valuation drivers while accommodating nonlinear relation-
ships, mixed data types, and pervasive missing data common in
private markets. Using a global private-market universe of approxi-
mately 270,000 companies, including more than 53,000 firms with
observed or derivable post-money valuations spanning multiple
industries, geographies, and deal stages, we demonstrate that the
proposed similarity framework improves upon traditional distance-
based and text-embedding-based approaches in downstream k-
nearest-neighbor valuation tasks in the evaluated industry groups,
while retaining case-based explainability.
1 Introduction
Private markets have become one of the fastest-growing segments
of global financial markets spanning private equity (PE), venture
capital (VC), private credit, real estate, and other asset classes. VCs, a
subset focused on new or growing companies, invest in early-stage
private companies with high growth expectations and correspond-
ingly elevated risk profiles. Despite experiencing a5%decrease in
buyout volume in 2025, the PE market recorded the largest deals in
its history, a 40% increase in PE-backed exits (100% for IPOs), and
a 17% increase in overall deal value [1]. In spite of their growing
importance, private companies remain inherently challenging to
analyze at scale due to sparse corporate disclosures, irregular report-
ing intervals, diverse business models, and infrequent transaction
data.
As private markets expand, the availability of consistent, explain-
able analytics that standardize how practitioners benchmark and
compare private assets has become critical for workflows spanning
investment research, due diligence, and risk-oriented quality con-
trol. The identification of economically meaningful comparables
determining which companies constitute true peer assets lies at the
core of these allocation decisions [2]. Investors implicitly rely on
peer groups to contextualize valuations, assess growth trajectories,
evaluate competitive positioning and perform due diligence. Tradi-
tionally, these peer groups are constructed using coarse filters such
as industry classification, verticals, geography, deal stage or product
descriptions. While intuitive, such rule-based approaches struggle
to balance relevance and coverage where broad heuristics admit
weakly related firms and narrow filters risk excluding informative
peers altogether.
Recent advances in supervised similarity learning have moti-
vated a reassessment of how firm similarity is defined and learned
[3–6]. Rather than treating similarity as a static distance in feature
space, supervised approaches learn similarity with respect to an ex-
plicit objective. In this setting, firms are considered similar because
they jointly explain an outcome of interest.
Compared with unsupervised distance metrics, supervised sim-
ilarity learning learns feature relevance directly from the target
variable, reducing reliance on manual weighting and domain exper-
tise. The resulting similarity structure is task-specific and supports
applications such as peer identification, localized valuation, anom-
aly detection, and data quality assessment. For private markets,
where data sparsity and dispersion is pervasive, this provides a
principled and scalable framework for company comparison and
peer discovery anchored on a predetermined objective or the target
variable.
A valuation-conditioned similarity metric has direct relevance
for private-market workflows beyond valuation modeling. In
arXiv:2608.12594v1  [q-fin.ST]  12 Aug 2026

Frank et al.
sourcing, investors can scan for companies that resemble high-
performing portfolio firms or recently transacted peers, surfacing
opportunities outside conventional sector boundaries. In bench-
marking and diligence, analysts can compare a target’s valuation
multiples and growth profile against its learned nearest neighbors,
providing a market-grounded reference that complements manual
comparable-company selection. In portfolio construction and risk
management, the similarity structure can help identify concentra-
tion risk among holdings that appear diversified by industry but
share similar valuation drivers, and can inform secondaries and
fund-level analytics by grouping assets according to shared pricing
dynamics.
1.1 Related Work
Private-company valuation commonly relies on discounted cash
flow analysis, transaction multiples, and comparable-company
methods, all of which depend critically on selecting economically
relevant peers [2]. Recent work has used ML to make this selec-
tion data-driven: Ref. [4] jointly addressed relative valuation and
peer-firm selection by learning nonlinear valuation functions and
expressing predicted valuation multiples as weighted averages of
peer-firm multiples. Their results demonstrate that ML can recover
economically meaningful peer weights and improve out-of-sample
valuation accuracy. In private-company settings, Ref. [7] similarly
showed that ML models can improve entrepreneurial-firm val-
uation when conventional financial information is limited. Our
work builds on this literature but differs in objective: rather than
using peer weights primarily to produce a valuation estimate,
we explicitly construct a reusable pairwise similarity structure
anchored to observed private-company valuations.
A complementary literature represents inter-company relation-
ships directly. CompanyKG [8] models firms and their heteroge-
neous relationships as a large-scale graph and evaluates learned rep-
resentations on company-similarity tasks. Ref. [9] used pretrained
and fine-tuned language models to derive company embeddings
from business descriptions in SEC filings, showing that the result-
ing representations recover industry structure and identify firms
with similar financial characteristics and return correlations. More
generally, metric learning seeks to infer task-specific notions of
proximity from supervised information rather than impose a fixed
geometric distance [10]. This distinction is particularly relevant to
private markets, where industry taxonomies are non-unique, firm
descriptions are incomplete, and the appropriate definition of a
peer depends on the downstream economic objective.
Tree ensembles provide a natural mechanism for learning such
task-conditioned similarities. Breiman[ 11] introduced random-
forest proximity1, in which observations are considered similar
when they repeatedly occupy the same terminal nodes. Subse-
quent work has formalized tree-induced proximity as a repre-
sentation of the supervised geometry learned by an ensemble
[12]. In finance, tree-based proximities have been applied to
corporate-bond similarity [ 13] and relative valuation in illiquid
municipal-bond markets [5]. Our work extends this line of research
to private-company equity and venture-capital settings by learning
a valuation-conditioned similarity structure from diverse company
1https://www.stat.berkeley.edu/~breiman/RandomForests/cc_home.htm
and transaction attributes. Unlike methods that use similarity only
for peer filtering or as an implicit component of prediction, the
proposed framework explicitly constructs an tree-importance-
weighted pairwise similarity matrix whose geometry is anchored
to observed post-money valuations.
1.2 Key Contributions
This paper introduces an ML framework for identifying valuation-
relevant peer companies in private markets. Although the frame-
work is trained using post-money valuation as the supervisory
target, its primary objective is not standalone valuation prediction
but the extraction of a valuation-conditioned similarity structure
among private companies. We formalize company similarity as a
supervised learning problem, where similarity is learned from ob-
served market valuations rather than predefined distance functions,
industry classifications, or textual descriptions. By anchoring simi-
larity to valuation outcomes, the proposed approach generates peer
relationships that are directly aligned with private market pricing
dynamics.
The key contributions of this work are threefold. First, we de-
velop a supervised similarity framework based on CatBoost models
trained on post-money valuations and derive a tree-importance-
weighted leaf-node co-occurrence metric that produces a symmetric
pairwise similarity matrix across companies. Second, we demon-
strate that the learned metric improves upon traditional unsuper-
vised and semantic similarity approaches, including Euclidean,
Gower, and embedding-based distances described in Table 1, in
downstream k-nearest-neighbor valuation tasks within the evalu-
ated industry groups. These results are consistent with the broader
distance metric learning literature, which shows that task-specific
similarity functions often outperform generic geometric distance
measures [14, 15]. Finally, we provide interpretable explanations of
both valuation predictions and peer relationships using SHAP [16],
highlighting the valuation drivers that shape the induced similarity
structure.
Table 1: Distance metrics compared in k-NN evaluation
Metric Description
Cosine1− 𝑥·𝑦 ∥𝑥∥·∥𝑦∥ over MPNet dense embeddings
Euclidean
√︁˝(𝑥 𝑗−𝑦 𝑗)2 over standardized + LOO en-
coded features
Gower( 1/𝑝) ˝ 𝑗𝑑 𝑗(𝑥 𝑗,𝑦 𝑗) with mixed-type normal-
ization
Learned (Ours) 1−˝ 𝑡𝑤𝑡·I[𝑍 1,𝑡 =𝑍 2,𝑡] (Proposed framework)
2 Private Company Data
Our dataset comprises approximately 270,000 private companies
globally, spanning more than 50 industry groups, hundreds of prod-
uct and service categories, and multiple geographic dimensions
including region, country, state, and city. Deal history in the dataset
extends from 1977 to 2025, with the median deal having an age of
five years as of calibration (2025), and 75% of deals having taken

What Makes a Peer? Valuation-Anchored Similarity in Private Markets
place since 2015. Table 2 shows the key variables available for our
experiments. The dataset contains company-level characteristics,
deal information from the most recent funding round, observed
transaction-based valuations, and the latest available financial data.
2.1 Feature description
Post-money valuation, or the post-deal equity valuation of a firm,
is available following a recent funding round. For some compa-
nies, we see a post-money valuation directly, while for others, we
compute this amount based on enterprise value, deal size divided
by the acquisition percentage, pre-money valuation (equity val-
uation prior to the deal) plus deal size, or pre-money valuation
plus the total offering amount. This enables us to recover approxi-
mately 53,000 post-money valuations (the most recent deal for each
firm in our universe). The final feature set contains 27 variables,
of which 23 are categorical, reflecting the inherently taxonomic
nature of private market data. Key attributes such as deal stage,
deal type, internal sector classification, geography, customer profile,
and product offerings are naturally categorical and often exhibit
high cardinality. For example, deal type contains approximately 80
distinct transaction categories spanning venture capital and private
equity markets, while internal sector and industry classifications
encompass hundreds of fine-grained categories. In addition, several
variables contain multi-label assignments, further increasing the
complexity of the feature space.
A defining characteristic of private-market data is the prevalence
of missing information, reflecting limited disclosure requirements
for private companies in jurisdictions such as the United States.
Of the approximately 270,000 companies in the original universe,
roughly 53,000 have an observed or derivable post-money valuation
and at least one PE or VC transaction, forming the calibration
universe for this study. Financial variables such as revenue (top-line
sales), EBITDA (earnings before interest, taxes, depreciation, and
amortization), and net income (income after all expenses) exhibit
the highest levels of missing values (75–80%), whereas categorical
attributes including country, deal stage, and customer type are
largely complete. Feature cardinality is highest among geographic
and sector-related variables and lowest among strategy, status, and
offering-type fields.
To construct the final feature set, we applied a two-stage se-
lection procedure. First, categorical features with fewer than 50%
non-missing observations were excluded. Second, features exhibit-
ing zero importance in a preliminary CatBoost model were re-
moved. This process reduced the risk of learning unstable decision
boundaries from missing feature values. Summary statistics for the
principal features are provided in Table 2.
3 Valuation-based similarity learning
framework
3.1 Valuation as a Supervised Anchor
A central challenge in private markets is that there is no universally
accepted definition of what constitutes a comparable company [17].
Traditional approaches rely on industry classifications, geography,
funding stage, or business descriptions, yet private companies fre-
quently span multiple sectors, products, and customer segments
simultaneously. As a result, peer identification is often subjective
and highly dependent on practitioner judgment.
We use observed private market valuations as the supervisory
anchor for learning company similarity. Unlike predefined tax-
onomies, valuations reflect investors’ assessment of a firm’s growth
prospects, competitive position, financial performance, and risk
profile at the time of a transaction [2]. As such, valuation provides
a market-based summary of company characteristics and future
expectations.
Conditioning similarity on valuation aligns peer identification
with the primary objective of comparable analysis. Under this frame-
work, companies are considered peers because they exhibit similar
valuation dynamics given their underlying attributes. Importantly,
the framework does not simply group firms with similar valua-
tion levels. Companies with identical valuations may be deemed
dissimilar if their valuations are driven by different factors, while
firms with different valuations may be identified as close peers if
they share similar valuation drivers. The resulting similarity met-
ric therefore captures common valuation mechanisms rather than
merely matching firms by size or market value.
3.2 Tree-Based Similarity Learning via Gradient
Boosted Decision Trees
Gradient boosted decision trees (GBDTs) are well suited to private
market data because they naturally accommodate mixed data types,
missing values, and complex nonlinear interactions [3, 5]. When
trained to predict company valuations based on multiple input
features, GBDTs partition firms into locally homogeneous regions
defined by valuation-relevant feature interactions, including ge-
ography, sector, deal stage, and financial attributes. This learned
structure provides a natural foundation for supervised similarity
learning: firms are considered similar if they are repeatedly grouped
together by the valuation model.
To construct the similarity metric based on the trained GBDT,
we leverage leaf-node co-occurrences across the ensemble. Because
GBDTs are trained sequentially to minimize prediction error [18],
different trees contribute unequally to the final model. We therefore
weight each tree according to its incremental reduction in training
loss, assigning greater influence to trees that contribute more to
predictive performance. Pairwise similarity is then computed as
the weighted frequency with which two companies are assigned to
the same terminal node across the ensemble.
The resulting similarity matrix captures shared valuation drivers
rather than simple feature proximity. By conditioning similarity
on the valuation objective, the framework learns a localized, non-
linear distance metric that identifies companies exhibiting similar
valuation behavior.
3.3 CatBoost Implementation
We implement the valuation model using Categorical Boosting
(CatBoost)2, a gradient-boosted decision tree algorithm designed
for structured datasets containing high-cardinality categorical vari-
ables and missing information [19]. This setting closely matches pri-
vate market data, where economically important attributes such as
deal type, sector classification, product offering, customer segment,
2https://catboost.ai/

Frank et al.
Table 2: Feature categories and representative variables (Metrics from Calibration)
Category Type Key Features (% Missing Values for Numerical Features, Cardinality for Categorical Features)
Financial Numerical Revenue (78%), EBITDA (80%), Net Income (78%), Avg Time Since Last Financials (75%)
Deal-level Categorical Deal Type (83), Strategy (2), Target Status (2), Offering Type (3)
Geographic Categorical Country (130), Region and City (4,816)
Sector/Product Industry Categorical Internal Industry Group (720), Internal Sector Categorization (229), Product/Service Offering (305)
Customer Categorical Customer Type (4), Customer End User (7), Customer Use (244)
and geography are predominantly categorical and often contain
hundreds or thousands of distinct values.
Unlike conventional boosting pipelines that require one-hot or
externally computed target encodings, CatBoost processes cate-
gorical variables natively through ordered target statistics. These
statistics are constructed using only observations that precede the
current instance under a random permutation, thereby reducing
target leakage and the prediction shift associated with standard
target encoding. CatBoost further employs ordered boosting, in
which residual estimates are generated without using the target
value of the observation being predicted. Together, these mech-
anisms provide a leakage-resistant treatment of high-cardinality
categorical information while avoiding the dimensional expansion
induced by one-hot encoding.
CatBoost also handles missing numerical values directly through
learned split directions, allowing missingness to contribute predic-
tive information without explicit imputation. The model is built
from symmetric, or oblivious, decision trees, in which the same
split condition is applied at each depth. This structure enables effi-
cient inference, regularization, and straightforward extraction of
terminal-node assignments across the ensemble. The latter property
is central to our framework, since company similarity is derived
from tree-importance-weighted leaf-node co-occurrences. CatBoost
therefore serves not only as the valuation estimator, but also as
the learned partitioning mechanism from which the valuation-con-
ditioned similarity structure is constructed.
3.4 Regression
Let𝑧𝑖 =log(𝑦 𝑖) denote the log-transformed post-money valuation.
The model is trained to minimize the root mean squared error in
log space:
L=
vut
1
𝑁
𝑁∑︁
𝑖=1
( ˆ𝑧𝑖−𝑧 𝑖)2.(1)
Here,𝑧𝑖 and ˆ𝑧𝑖 denote the observed and predicted log valuations,
respectively. The predictive ensemble function ˆ𝑧(𝑥) is constructed
sequentially as an additive sum of𝑇 decision trees scaled by the
learning rate𝜂:
ˆ𝑧(𝑥)=
𝑇∑︁
𝑡=1
𝜂ℎ 𝑡(𝑥),(2)
whereℎ𝑡(𝑥) denotes the output of tree 𝑡. Predictions are trans-
formed back to valuation levels as ˆ𝑦(𝑥)=exp( ˆ𝑧(𝑥)).
3.4.1 Tree Importance Weighting.Not all trees contribute equally
to predictive accuracy. Earlier trees typically capture dominant
predictive structure, while later trees refine residual errors. We
assign importance weights based on the incremental reduction in
loss. Let𝑇𝐿 𝑡 denote the training loss after the first𝑡 trees, where𝑇𝐿 0
represents the loss of the initial null model. The step-size predictive
contribution𝑆𝑡 of an individual tree𝑡 is calculated via the absolute
difference in sequential training loss:
𝑆𝑡 =|𝑇𝐿 𝑡−𝑇𝐿 𝑡−1|(3)
To establish the proportional influence of each weak learner on
the final similarity space, the normalized tree weight𝑤𝑡 is computed
as:
𝑤𝑡 = 𝑆𝑡 ˝𝑇
𝑗=1𝑆 𝑗
(4)
This ensures that trees contributing the largest improvements to
the loss have proportionally greater influence on the similarity
measure.
3.4.2 Leaf-Node Co-occurrence Similarity and Supervised Dissimi-
larity.For companies 𝑋1 and𝑋2, let𝑍1,𝑡 and𝑍2,𝑡 denote leaf nodes
to which they fall into while traversing an assigned treetin an
ensemble. The tree-weighted leaf-node co-occurrence similarity
function𝑆(𝑋 1,𝑋 2)is formulated as:
𝑆(𝑋 1,𝑋 2)=
𝑇∑︁
𝑡=1
𝑤𝑡·I[𝑍 1,𝑡 =𝑍 2,𝑡](5)
where I[·] is the indicator function equal to 1 when the two com-
panies occupy the same terminal node and 0 otherwise.
The final bounded supervised dissimilarity measure𝐷(𝑋 1,𝑋 2)
is derived directly from the complement of the similarity matrix
score:
𝐷(𝑋 1,𝑋 2)=1−𝑆(𝑋 1,𝑋 2)(6)
This operation maps the pairwise relationship into a symmetric
matrix where𝐷∈[0,1].
While we refer to the proposed measure as a distance, it is
best viewed as a supervised dissimilarity function that captures
valuation-conditioned proximity; it is not guaranteed to satisfy all
metric-space axioms such as the triangle inequality.
4 Experimental Setup
For training the CatBoost algorithm, we use the cross-sectional
company and transaction attributes as input variables shown in
Table 2. We use post-money valuation associated with the most
recent observed transaction as the target variable. Post-money
valuation is the implied equity value of a company immediately
after its most recent financing round, calculated by multiplying

What Makes a Peer? Valuation-Anchored Similarity in Private Markets
the total shares outstanding (common stock, preferred stock, and
option pool) by the conversion price per share of that round, and
may be sourced directly from press releases, computed from issued
shares in regulatory filings, or estimated from authorized shares
with a discount factor.
4.1 Feature Engineering and Preprocessing
4.1.1 Target Variable.Given the highly right-skewed nature of
private company valuations, the target variable is transformed into
log space prior to model calibration and winsorized at the 1st and
99th percentiles to mitigate the influence of extreme outliers.
The target valuation is constructed from multiple transaction-
related fields. When available, post-money valuation is used directly.
Otherwise, it is derived from enterprise value, acquisition trans-
action terms, pre-money valuation plus deal size, or pre-money
valuation plus total offering amount. The model is trained to min-
imize the root mean squared error (RMSE) of log valuations (Eq.
1), which stabilizes variance and improves predictive performance
across the wide range of company sizes observed in private markets.
4.1.2 Input Variables.Input variables (Table 2) undergo minimal
preprocessing to preserve their economic interpretation while en-
suring robustness. Multi-label deal types are concatenated into a
single categorical feature prior to training. Numerical variables are
retained in their original scale, while categorical features are passed
directly to CatBoost, which natively handles high-cardinality cate-
gorical variables through ordered target statistics. Missing values
are not explicitly imputed and are instead incorporated into the tree-
splitting process within CatBoost as potentially informative signals.
In addition, we construct anA verage Time Since Last Financials
feature to capture the staleness of reported financial information.
For each financial metric (revenue, EBITDA, and net income), we
measure the time elapsed since they were last reported, then take
the average of those time horizons. Because the dataset represents
a snapshot in time as of September 2025, this variable enables the
model to distinguish between structurally missing financials and
observations whose financial data may simply be outdated.
4.2 Modeling
4.2.1 Stratified Sampling.The dataset is divided into training and
test sets using an 80:20 split stratified by internal subindustry clas-
sification to preserve category representation across both samples.
The same stratification scheme is applied within cross-validation
folds used for hyperparameter optimization. All preprocessing de-
cisions, feature selection, model estimation, and tree-importance
weights are derived exclusively from the training data. After fitting,
the trained CatBoost ensemble is held fixed and used to compute
similarities between test companies and the training reference set.
Test-set valuations are used only for final performance evaluation
and do not influence model fitting, neighbor selection, similarity
weights, scaling-factor estimation, or conformal calibration.
4.2.2 Sample Weighting.Given that the historical transactions in
the calibration dataset span nearly fifty years (median: five years),
we apply recency-based weighting to the training samples to empha-
size more recent transactions. Specifically, sample weights increase
with transaction recency, reflecting structural changes in private
markets and the time-varying nature of valuation determinants.
Four observations with missing transaction dates were assigned the
minimum recency, putting their weights in line with the median
sample weight.
4.2.3 Hyperparameter Optimization.We optimize hyperparame-
ters using Optuna v4.7.0 [20] with tree-structured Parzen Estimator
(TPE) sampling over 50 trials using five-fold cross-validation on
the training set. The optimal configuration and search ranges are
shown in Table 3.
Table 3: Optimized CatBoost Hyperparameters via Optuna
Hyperparameter Best Value Search Range Step Size
Tree Depth 13[7,14]1
Number of Estimators 1,859[500,2000]1
Max Leaves per Tree 108[31,127]1
Min Data in Leaf 242[128,512]1
Bagging Temperature 6.96[1,8]Cont.
Random Strength 7.71[2,10]Cont.
Learning Rate (𝜂) 0.023[0.015,0.06]Cont. (log)
Max Bin 164[128,255]1
L2 Leaf Regularization 24.28[10,200]Cont. (log)
4.3 Model Outputs
4.3.1 Valuation Regression and Benchmark Models.The valuation
forecast produces a single point estimate in log-space, which can
then be exponentiated and scaled to a linear value. The model ac-
curacy is measured based on mean absolute error (MAE), RMSE,
𝑅2, mean absolute percentage error (MAPE) and median absolute
percentage error (MdAPE). We also used Ordinary Least Squares
(OLS) as a baseline before selecting the CatBoost model for valua-
tion prediction. Leave one out encoding was used on the categorical
inputs, while simple mean imputation was performed for missing
numeric data.
4.3.2 Conformal Prediction.To quantify predictive uncertainty, we
use conformal prediction, which constructs distribution-free pre-
diction intervals from calibration residuals [21, 22]. Residuals are
normalized and grouped by deal type to account for heteroskedastic-
ity across funding rounds. The resulting intervals provide calibrated
uncertainty bounds around each valuation estimate.
4.3.3 Similarity Matrix.Beyond valuation prediction, the trained
model is used to construct a pairwise similarity matrix across com-
panies. Similarity is computed as the importance-weighted fre-
quency with which two firms are assigned to the same terminal
node across the ensemble. Trees that contribute more to predictive
performance receive greater weight, ensuring that the resulting
similarity measure reflects the most influential valuation drivers
learned by the model.

Frank et al.
5 Results
5.1 Out-of-Sample Model Performance
The CatBoost model outperforms a multivariate linear regression.
We evaluate model performance using standard regression metrics.
Table 4: Regression metrics and comparison with benchmark
model.
Metric OLS CatBoost % Relative Improvement
MAE 1.19 1.08 8%
RMSE 1.56 1.44 8%
𝑅2 0.36 0.46 28%
MAPE (%) 0.07 0.06 14%
MdAPE (%) 0.05 0.05 -%
To assess model performance across the target distribution, we
partition the test set into quintiles based on the ground-truth log
valuation. We further disaggregate performance by categorical fea-
tures to identify segments where the model exhibits systematic bias.
Prediction errors are concentrated in the lowest and highest valua-
tion deciles (the smallest and largest sized firms). Out-of-sample
RMSE rises from 0.94 in Q8 to 2.35 in Q1 and 2.05 in Q10, with
an overall RMSE of 1.44, indicating that errors are largest for the
smallest and largest firms and lowest in the middle of the valuation
distribution.
Performance also varies across geographies, industries, and trans-
action types. The ten most represented countries account for ap-
proximately 90% of the test dataset. Higher prediction errors are
observed in cybersecurity and selected software segments, reflect-
ing the greater dispersion and uncertainty of valuations within
these sectors. Across transaction types, the most prevalent cate-
gories represent approximately 83% of the out-of-sample dataset.
Prediction errors are highest for later-stage private equity trans-
actions and deals classified as unspecified, whereas early-stage
VC financings tend to exhibit lower errors and more consistent
valuation patterns.
5.2 Model Scaling
Because the model is estimated in log-valuation space, directly ex-
ponentiating predictions introduces downward retransformation
bias in linear space. We correct for this using multiplicative calibra-
tion factors estimated on the training data as the ratio of aggregate
observed valuations to aggregate exponentiated predictions. To
account for differences in valuation distributions across transaction
categories, separate factors are applied by deal type: 1.74 for Series
transactions, 5.06 for Unspecified transactions, and 2.19 for all other
transactions. These adjustments improve calibration of predicted
valuations in level terms.
5.3 Conformal Prediction
Figure 1 illustrates conformal prediction intervals across funding
stages. The intervals capture a substantial proportion of observed
valuations while providing calibrated uncertainty estimates around
each prediction. Interval widths generally increase in later funding
stages, consistent with the greater dispersion and uncertainty asso-
ciated with valuations of mature private companies. As expected,
higher confidence levels produce wider intervals, reflecting the
trade-off between coverage and interval efficiency.
Figure 1: Conformal Prediction Intervals by Deal Stage
Conformal metrics for three different confidence levels are dis-
played below. Coverage percentage represents the proportion of
observed valuations captured by the conformal interval, while in-
terval mean ratio refers to the average interval size relative to the
mean prediction.
Table 5: Prediction interval statistics
Count Confidence Level Coverage % Interval Mean Ratio
53.8k 95% 93% 3.35
53.8k 75% 74% 1.80
53.8k 60% 60% 1.60
6 Model interpretation and similarity
evaluation
We use SHapley Additive exPlanations (SHAP)3 to interpret the ML
model [23, 24]. Global feature importance is measured by the mean
absolute SHAP value across observations, capturing each feature’s
average contribution to predicted valuation.
Figure 2 shows that deal type is the dominant valuation driver,
with a mean absolute SHAP contribution of 1.31, followed by coun-
try (1.17), region and city (0.28), revenue (0.22), and average time
elapsed since most recent financials (0.20). The remaining 22 fea-
tures contribute a combined 1.62. These top five features therefore
play the largest role in shaping both valuation predictions and the
induced similarity structure.
3https://shap.readthedocs.io/

What Makes a Peer? Valuation-Anchored Similarity in Private Markets
Figure 2: Bar Plot of Absolute Mean SHAP values
6.1 Neighborhood Analysis
The objective of the similarity evaluation is to determine whether
the learned metric produces economically coherent peer groups and
captures meaningful relationships between private companies. We
assess this both qualitatively, through neighborhood consistency,
and quantitatively, through comparisons with established distance
and embedding based baselines. A successful similarity framework
should identify peers that are more similar across economically
relevant characteristics than those obtained from conventional
proximity measures.
To evaluate neighborhood consistency, we identify the 20 nearest
neighbors of each company under the learned similarity metric. For
numerical attributes, we compute the average absolute deviation be-
tween a company and its neighbors, while for categorical attributes
we calculate the proportion of mismatched categories. These mea-
sures are aggregated across all companies within an industry group
and compared against baseline similarity methods. Lower numer-
ical deviations and categorical mismatch rates indicate that the
learned similarity metric produces more coherent peer groups with
respect to economically meaningful company characteristics.
The comparison with other distance metrics (Figure 3) shows
that for the top three numeric features as measured by SHAP (rev-
enue, average time elapsed since last financials, and net income),
the learned metric consistently shows a lower deviation than co-
sine distance (between embeddings derived from internal company
descriptions) and mixed performance against Gower and Euclidean
distances on Financial Services companies. For the top three cate-
gorical features (deal type, country, and region and city), the learned
metric shows a lower mismatch rate than other metrics.
6.2 k-NN Benchmarking
To evaluate the learned similarity metric further, we compare its
ability to recover company valuations against several benchmark
distance measures, including Euclidean, Gower, and embedding-
based similarity. For each metric, we construct a weighted k-nearest-
neighbor (k-NN) estimator and assess valuation prediction accuracy
across multiple neighborhood sizes. Superior performance indicates
that the corresponding similarity measure identifies firms with
more comparable valuation characteristics.
While the proposed similarity metric is learned from valuation
data, this evaluation does not reuse CatBoost valuation predictions:
the CatBoost model is used only to construct the similarity structure,
whereas valuation estimates are generated independently through
a non-parametric k-NN procedure operating on the resulting neigh-
borhood graph. The experiment therefore evaluates whether the
learned similarity metric produces neighborhoods that are more
valuation-consistent than those obtained from conventional dis-
tance measures. If the similarity structure is economically meaning-
ful, firms identified as neighbors should exhibit similar valuations,
leading to improved k-NN performance. The results demonstrate
that the learned metric outperforms traditional distance-based and
semantic baselines in the evaluated settings, suggesting that it cap-
tures valuation-relevant relationships more effectively than generic
notions of proximity in those settings.
In Financial Services (Figure 4), the MAE and RMSE of the post-
money valuation resulting from the learned metric are consistently
lower than the other metrics across all neighborhood sizes.
7 Conclusion and Outlook
We introduce a valuation-conditioned similarity framework for
private markets that learns peer relationships from observed trans-
action valuations. The method combines CatBoost-based valuation
modeling with importance-weighted leaf-node co-occurrences to
construct an interpretable similarity structure. In the evaluated in-
dustry groups, the learned measure produces economically coherent
peer sets and generally outperforms conventional distance-based
and embedding-based baselines in downstream valuation tasks.
The framework offers a data-driven alternative to comparable-
company analysis based on fixed industry, geographic, or deal-stage
filters. Rather than matching firms by surface characteristics, it
identifies peers that share common valuation drivers.
Future work may extend the approach to scalable cross-industry
similarity, softer tree-based proximity measures, and richer textual
or graph-based representations of private companies. These exten-
sions could further improve peer identification while preserving
the valuation-centered objective of the framework.
8 Acknowledgement
The views expressed here are those of the authors alone and not of
BlackRock, Inc.
References
[1] Alexander Edlich, Chris Llewellyn, Christopher Croke, Rahel Schneider, and
Warren Teichner. Private equity — global private markets report, February 2026.
URL https://www.mckinsey.com/industries/private-capital/our-insights/global-
private-markets-report/private-equity. Accessed: May 2026.
[2] Aswath Damodaran.Damodaran on valuation: security analysis for investment
and corporate finance. John Wiley & Sons, 2011.
[3] Jerinsh Jeyapaulraj, Dhruv Desai, Peter Chu, Dhagash Mehta, Stefano Pasquali,
and Philip Sommer. Supervised similarity learning for corporate bonds using
random forest proximities. InProceedings of the 3rd ACM International Conference
on AI in Finance (ICAIF ’22), pages 411–419. ACM, 2022.
[4] Paul Geertsema and Helen Lu. Relative valuation with machine learning.Journal
of Accounting Research, 61(1):329–376, 2023. doi: 10.1111/1475-679X.12464.
[5] Preetha Saha, Jasmine Lyu, Dhruv Desai, Rishab Chauhan, Jerinsh Jeyapaulraj,
Peter Chu, Philip Sommer, and Dhagash Mehta. Machine learning-based rela-
tive valuation of municipal bonds. InProceedings of the 5th ACM International
Conference on AI in Finance, pages 634–642, 2024.
[6] Joshua Rosaler, Luca Candelori, Vahagn Kirakosyan, Kharen Musaelian, Ryan
Samson, Martin T Wells, Dhagash Mehta, and Stefano Pasquali. Supervised
similarity for high-yield corporate bonds with quantum cognition machine
learning.arXiv preprint arXiv:2502.01495, 2025.

Frank et al.
Figure 3: Financial Services (3.2k firms)
Figure 4: k-NN Valuation by Neighborhood Size and Distance Metric
[7] Ruling Zhang, Zengrui Tian, Killian J. McCarthy, Xiao Wang, and Kun Zhang.
Application of machine learning techniques to predict entrepreneurial firm
valuation.Journal of Forecasting, 42(2):402–417, 2023. doi: 10.1002/for.2913.
[8] Lele Cao, Vilhelm von Ehrenheim, Mark Granroth-Wilding, Richard
Anselmo Stahl, Andrew McCornack, Armin Catovic, and Dhiana Deva
Cavalcanti Rocha. Companykg: A large-scale heterogeneous graph for company
similarity quantification. InProceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, pages 4816–4827, 2024.
[9] Dimitrios Vamvourellis, Máté Tóth, Snigdha Bhagat, Dhruv Desai, Dhagash
Mehta, and Stefano Pasquali. Company similarity using large language models.
In2024 IEEE Symposium on Computational Intelligence for Financial Engineering
and Economics (CIFEr), pages 1–9. IEEE, 2024.
[10] Aurélien Bellet, Amaury Habrard, and Marc Sebban. A survey on metric learning
for feature vectors and structured data.arXiv preprint arXiv:1306.6709, 2014.
[11] Leo Breiman. Random forests.Machine Learning, 45(1):5–32, 2001.
[12] Jake S Rhodes, Adele Cutler, and Kevin R Moon. Geometry-and accuracy-
preserving random forest proximities.IEEE Transactions on Pattern Analysis and
Machine Intelligence, 45(9):10947–10959, 2023.
[13] Jerinsh Jeyapaulraj, Dhruv Desai, Dhagash Mehta, Peter Chu, Stefano Pasquali,
and Philip Sommer. Supervised similarity learning for corporate bonds using ran-
dom forest proximities. InProceedings of the Third ACM International Conference
on AI in Finance, pages 411–419, 2022.
[14] Eric W Xing, Michael I Jordan, Stuart J Russell, and Andrew Y Ng. Distance
metric learning with application to clustering with side-information. InAdvances
in Neural Information Processing Systems (NeurIPS), volume 15, pages 521–528,
2002.
[15] Kilian Q Weinberger and Lawrence K Saul. Distance metric learning for large
margin nearest neighbor classification.Journal of Machine Learning Research
(JMLR), 10(2):207–244, 2009.
[16] Scott M. Lundberg, Gabriel G. Erion, Hugh Chen, et al. From local explanations
to global understanding with explainable ai for trees.Nature Machine Intelligence,
2:56–67, 2020.
[17] Dhagash Mehta, John RJ Thompson, Hoyoung Lee, and Yongjae Lee. Clustering
and similarity learning in financial markets: A tutorial for the practitioners.
A vailable at SSRN 5587353, 2025.

What Makes a Peer? Valuation-Anchored Similarity in Private Markets
[18] Jerome H. Friedman. Greedy function approximation: A gradient boosting
machine.Annals of Statistics, 29(5):1189–1232, 2001.
[19] Liudmila Prokhorenkova, Gleb Gusev, Aleksandr Vorobev, Anna Veronika Doro-
gush, and Andrey Gulin. Catboost: unbiased boosting with categorical features.
Advances in neural information processing systems, 31, 2018.
[20] Takuya Akiba, Shotaro Sano, Toshihiko Yanase, Takeru Ohta, and Masanori
Koyama. Optuna: A next-generation hyperparameter optimization framework.
InProceedings of the 25th ACM SIGKDD international conference on knowledge
discovery & data mining, pages 2623–2631, 2019.
[21] Glenn Shafer and Vladimir Vovk. A tutorial on conformal prediction.Journal of
machine learning research, 9(3), 2008.
[22] Mingshu Li, Dhruv Desai, Bhaskarjit Sarmah, Snigdha Bhagat, and Dhagash
Mehta. Similarity-based conformal prediciton using random forest proximities.
InProceedings of the 6th ACM International Conference on AI in Finance, pages
387–395, 2025.
[23] Scott M Lundberg and Su-In Lee. A unified approach to interpreting model
predictions. In I. Guyon, U. V. Luxburg, S. Bengio, H. Wallach, R. Fergus, S. Vish-
wanathan, and R. Garnett, editors,Advances in Neural Information Processing Sys-
tems 30, pages 4765–4774. Curran Associates, Inc., 2017. URL http://papers.nips.
cc/paper/7062-a-unified-approach-to-interpreting-model-predictions.pdf.
[24] Jilei Yang. Fast treeshap: Accelerating shap value computation for trees.arXiv
preprint arXiv:2109.09847, 2021.
