---
title: 'Data-Driven Telecom Marketing Optimization: A Machine Learning-Based Churn Prediction and Customer
  Segmentation Framework'
url: https://arxiv.org/abs/2607.10260
category: ai-marketing
subcategory: measurement
date: 2026-07
venue: ''
authors:
- Nada Ali
- Lina Ahmed
- Tahani Abdalla Attia Gasmalla
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.10260
pages: 12
chars: 41962
fetched_at: '2026-11-08T13:26:32+00:00'
kb_version: 1
---

# Data-Driven Telecom Marketing Optimization: A Machine Learning-Based Churn Prediction and Customer Segmentation Framework

Data-Driven Telecom Marketing Optimization: A
Machine Learning-Based Churn Prediction and
Customer Segmentation Framework
Nada Ali, Lina Ahmed
Department of Electrical and Electronic Engineering
University of Khartoum
lina.alnoosh2@gmail.com
nadaali1232000@gmail.com
Dr. Tahani Abdalla Attia
Associate Professor
Department of Electrical and Electronic Engineering
University of Khartoum
tahani@uofk.edu
Abstract—Customer churn is one of the most significant
challenges facing telecommunication companies, directly erod-
ing revenue and long-term customer relationships. Traditional
retention programs typically rely on generic, non-personalized
incentives and lack the precision needed to identify high-risk
customers before they leave. This paper presents a complete,
data-driven marketing optimization framework that integrates
(i) machine-learning-based churn prediction, (ii) two-dimensional
customer segmentation combining churn risk with customer
value, and (iii) tailored, segment-specific marketing and Return-
on-Investment (ROI) strategies. Using the IBM Telco Customer
Churn dataset (7,043 customers, 21 features), three gradient-
boosting ensembles—XGBoost, LightGBM, and CatBoost—were
trained and rigorously tuned via randomized search with strati-
fied 5-fold cross-validation, explicit class-weighting, and F1-score-
driven decision-threshold optimization to counter the dataset’s
73.4%/26.6% class imbalance. CatBoost was selected as the
deployment model, achieving 77.68% accuracy, 73.53% recall,
56.12% precision, an F1-score of 0.6366, a PR-AUC of 0.6553, and
a ROC-AUC of 0.8403 on the held-out test set. Customers were
subsequently partitioned with K-Means clustering (validated via
the Elbow method and visualized with Principal Component
Analysis) into High-, Medium-, and Low-Value segments, which
were further cross-tabulated against churn-risk labels to define
four actionable customer clusters. Segment-specific retention,
upsell, and engagement strategies were designed for each cluster,
and a theoretical ROI/CLV framework is provided to quantify the
financial impact of the proposed interventions. The entire pipeline
was operationalized in an interactive Streamlit web application
that allows non-technical marketing teams to upload data, filter
by segment, visualize churn drivers via SHAP, and download
automated segment reports. The results confirm that combining
predictive churn modeling with value-aware segmentation yields
substantially more actionable, and more profitable, marketing
decisions than churn prediction alone.
Index Terms—Churn Prediction, Customer Segmentation,
Gradient Boosting, XGBoost, LightGBM, CatBoost, K-Means
Clustering, PCA, SHAP, Return on Investment, Customer Life-
time Value, Telecom Industry, Streamlit
I. INTRODUCTION
A. Background and Motivation
Telecommunication companies operate in a saturated, price-
competitive market in which acquiring a new customer is
estimated to cost several times more than retaining an existing
one. Customer churn—the voluntary or involuntary termina-
tion of a subscriber relationship—therefore represents a direct
and compounding threat to revenue. Traditional retention pro-
grams generally apply blanket incentives (discounts, bundle
offers) irrespective of a customer’s actual risk of leaving or
their financial value to the company, which wastes marketing
budget on customers who were never going to leave while
under-serving high-value customers who are quietly at risk.
This paper addresses that inefficiency by building a full
pipeline that predictswhois at risk, segmentshow valuable
each customer is, and only then decideswhatmarketing action
to take andwhether it pays off.
B. Problem Statement
Existing telecom retention systems suffer from three com-
pounding weaknesses: (1) churn prediction is frequently
treated as a stand-alone classification exercise, disconnected
from any downstream business action; (2) customer segmen-
tation, where it exists, is usually performed independently of
churn risk, using purely descriptive demographic or usage
groupings; and (3) few published systems attempt to trans-
late model outputs into an operational, deployable tool that
estimates the financial return of an intervention. This work
is designed specifically to close all three gaps simultaneously
within a single, reproducible pipeline.
C. Contributions
This paper makes the following contributions:
•An integrated ML pipeline.A four-stage framework –
churn prediction, value segmentation, tailored campaign
design, and ROI measurement – implemented end-to-end
on a real public dataset (Fig. 1).
•A rigorous churn-prediction study.Three gradient
boosting families (XGBoost, LightGBM, CatBoost) are
trained under identical randomized-search hyperparam-
eter optimization with 5-fold stratified cross-validation,
explicitscale_pos_weighttuning, and a custom F1-
maximizing threshold search (Algorithm 1), rather than
relying on the default 0.5 decision boundary.
arXiv:2607.10260v1  [cs.LG]  11 Jul 2026

•Two-dimensional, actionable segmentation.K-Means
clustering (with PCA-based dimensionality reduction and
validation) is combined post-hoc with churn-risk labels to
produce four cross-sectional customer clusters, each with
a distinct, empirically profiled marketing strategy.
•A transparent ROI/CLV framework.A discounted
Customer Lifetime Value formulation and campaign-level
ROI equation are provided, together with worked hypo-
thetical scenarios (Table VII), so telecom operators can
substitute their own Average Revenue Per User (ARPU)
and campaign-cost figures.
•A deployable system.The complete pipeline is imple-
mented as an interactive Streamlit dashboard, including
automated SHAP-based explainability, dynamic filtering,
and downloadable per-segment text reports (Algorithm 2).
D. Paper Structure
Section II reviews related work in churn prediction, segmen-
tation, and ROI-driven telecom marketing. Section III provides
the theoretical background for the models used. Section IV
details the methodology: dataset, preprocessing, feature engi-
neering, model training, segmentation and the marketing/ROI
framework. Section V describes the system deployment. Sec-
tion VI presents experimental results. Section VII discusses
key insights, addressed research gaps, and limitations. Section
VIII concludes and outlines future work.
II. RELATEDWORK
A. Churn Prediction in the Telecom Sector
Customer churn is one of the most pressing challenges for
telecom companies because of its direct impact on revenue,
Customer Acquisition Cost (CAC), and long-term profitability
[1], [7]. Numerous studies confirm that retaining an existing
customer is substantially cheaper than acquiring a new one
[2], [7]. Traditional models such as logistic regression and
decision trees offer interpretability but degrade on complex,
high-dimensional tabular data [21]. Gradient boosting methods
– XGBoost [17], LightGBM [18], and CatBoost [19] – have
since become the standard for structured churn data due to
their ability to model non-linear interactions and handle mixed
categorical/numerical features. Ahmad et al. applied ML on
a big-data platform to forecast churn with high precision [9];
Wagh et al. benchmarked multiple ML models and highlighted
the practical value of ensembling in telecom [8]. SyriaTel’s
deployment of churn prediction combined with Social Network
Analysis achieved a 47% retention rate among predicted
churners [9], while V odafone Ghana used survival analysis
on top-up and Minutes-of-Use behavior to target at-risk high-
value customers [10]. However, most of these studies stop
at the prediction step without integrating the outputs into a
concrete marketing decision framework – the gap this paper
directly targets.
B. ML in Marketing Optimization
Telecom marketing has shifted from mass promotion to-
ward personalized, data-driven campaigns. ML enables near-
real-time segmentation, targeting, and campaign adjustment
to maximize ROI and Customer Lifetime Value (CLV) [4],
[6], [15]. Integrating ML outputs with CRM systems allows
promotions to be tailored to behavior, preference, and churn
risk [5], [16]. Sridevi et al. proposed predictive analytics for
end-to-end campaign optimization, including offer generation
and ROI tracking [6]. Despite this progress, few works propose
a full-stack implementation that unifies prediction, segmenta-
tion, and personalized marketing in a single deployable system
– a gap this study addresses directly with an operational
Streamlit application.
C. Customer Segmentation Techniques
Traditional segmentation relies on demographic or usage-
based groupings, which often lack the resolution needed to
identify nuanced behavior or profitability potential [12], [13].
Modern approaches use K-Means, hierarchical clustering, and
dimensionality-reduction methods such as PCA to generate
higher-resolution segments [11], [14], distinguishing groups
such as high-value loyalists, price-sensitive users, or dormant
subscribers. Alkhayrat et al. compared deep-learning-based
dimensionality reduction against classical PCA for telecom
clustering [11]; Sudirjo emphasized how data-driven segmen-
tation accelerates marketing decision-making [13]. Segmen-
tation efforts, however, are rarely integrated with churn-risk
labels or ROI-focused campaign planning – a limitation this
work overcomes by cross-tabulating value segments directly
with churn-risk output.
D. ROI and CLV in Telecom Marketing
ROI and CLV are the key financial metrics guiding tele-
com marketing decisions. Ramachandran defines CLV as the
present value of all future profits a customer will generate,
essential for prioritizing retention and upsell spend [4]. Sridevi
et al. proposed predictive analytics to track ROI alongside
customer behavior [6], and Pandian argued for evaluating
retention in terms of measurable financial return rather than
generic engagement metrics [3]. The operational challenge of
combining these financial metrics with real-time ML output
in a single tool remains open; Section IV-H proposes exactly
such a unified, adjustable framework.
III. THEORETICALBACKGROUND
A. Gradient Boosting Framework
Gradient boosting builds an additive ensemble of weak
learners (decision trees)h m(x), each fitted sequentially to the
residual/negative-gradient of a differentiable loss function:
ˆy=
MX
m=1
γmhm(x)(1)
whereγ m is the weight assigned to them-th learner. For
binary churn classification, the model minimizes a regularized
logistic-loss objective:
Obj(θ) =
nX
i=1
ℓ(yi,ˆyi) +
TX
t=1
Ω(ft)(2)

TABLE I: Comparison of the Three Gradient-Boosting Churn
Models
Aspect XGBoost LightGBM CatBoost
Tree growth Level-wise
(breadth-first)
Leaf-wise (best-
first)
Oblivious (sym-
metric splits)
Categorical
handling
Requires
explicit
encoding
Requires
explicit
encoding
Native
cat_features
support
Regularization L1
(reg_alpha),
L2
(reg_lambda)
L1,L 2 L2
(l2_leaf_reg)
+ ordered
boosting
Overfitting
control
gamma,
min_child
_weight,
pruning
min_data_in
_leaf,
num_leaves
depth,
permutation-
driven ordered
boosting
Parallelism Data / boosting-
round parallel
Exclusive
feature bundling
Native
CPU/GPU
optimization
whereℓ(y i,ˆyi) =−[y i log(ˆyi) + (1−y i) log(1−ˆyi)]is the
logistic loss andΩ(f t)is a regularization term penalizing tree
complexity. All three algorithms studied here minimize (2), but
differ substantially in tree-growth strategy, categorical-feature
handling and regularization, as summarized in Table I.
B. K-Means Clustering
K-Means partitions customers intoKclusters by minimiz-
ing the within-cluster sum of squares (WCSS):
WCSS=
KX
k=1
X
xi∈Ck
∥xi −µ k∥2 (3)
whereC k is thek-th cluster andµ k its centroid. Centroids are
initialized with theK-means++ scheme and updated iteratively
until convergence. The optimalKwas chosen using the Elbow
method (Fig. 5), which plots (3) againstKand identifies the
point of diminishing returns;K= 3was selected in this study.
C. Principal Component Analysis (PCA)
PCA is used both to decorrelate clustering features and to
visualize the resulting segments in two dimensions. Given the
standardized feature matrixX, the covariance matrix is
Cov(X) = 1 n−1 X ⊤X(4)
and the data is projected onto the leading eigenvectorsWof
Cov(X):
Z=XW(5)
Components were retained according to their explained-
variance ratio,
EVRj = λj PP
p=1 λp
(6)
which preserves maximal variance while eliminating redun-
dant/noisy dimensions prior to clustering and visualization
(Fig. 6).
Fig. 1: Overview of the proposed four-stage ML framework.
TABLE II: Characteristics of the IBM Telco Dataset
Total features 21
Total customers 7,043
Missing values None (initially)
Churn class 26.6% (1,869)
Non-churn class 73.4% (5,174)
Data distribution Imbalanced
Categorical features 17
Numerical features 4
D. Evaluation Metrics
Given the binary nature of churn prediction and the class
imbalance in the dataset, the following metrics were used:
Accuracy= T P+T N T P+T N+F P+F N (7)
Precision= T P T P+F P,Recall= T P T P+F N (8)
F1 = 2· Precision·Recall Precision+Recall (9)
Because accuracy is misleading under a 73.4%/26.6% class
split, ROC-AUC and, more importantly, Precision-Recall AUC
(PR-AUC) were used as the primary model-selection criteria,
since PR-AUC is far more sensitive to minority-class (churner)
performance than ROC-AUC under imbalance.
IV. METHODOLOGY
Fig. 1 shows the overall four-stage framework: churn pre-
diction→customer value segmentation→tailored marketing
campaigns→ROI measurement.
A. Dataset Description
This study uses the publicly availableIBM Telco Customer
Churn dataset[20], retrieved from Kaggle, comprising7,043
customer records and 21 featuresspanning demographics,
account information, service subscriptions, and billing. The
target variable,Churn, is binary (Yes/No). Table II summa-
rizes the dataset’s key characteristics.
Feature groups include:Usage/Financial(tenure,
MonthlyCharges,TotalCharges);Service
subscription(InternetService,OnlineSecurity,
OnlineBackup,DeviceProtection,TechSupport,
StreamingTV,StreamingMovies,PhoneService,
MultipleLines);Account(Contract,
PaperlessBilling,PaymentMethod); and
Demographic(gender,SeniorCitizen,Partner,
Dependents).

Fig. 2: Class distribution of the target variable Churn.
Fig. 3: Churn distribution across categorical features.
1) Dataset Limitations:Four limitations were identified and
explicitly accounted for during modeling: (1)class imbalance
(5,174 vs. 1,869, Fig. 2); (2)limited temporal coverage– the
dataset is a single snapshot with no time-series or seasonal
signal; (3)no external variablessuch as competitor actions or
macroeconomic conditions; and (4)potential label oversimpli-
fication, since the binary Yes/No churn label cannot capture
partial or temporary service reduction.
B. Exploratory Data Analysis
Bar-chart analysis of categorical features against churn
(Fig. 3) shows the highest churn concentrated among month-
to-month contract holders, fiber-optic internet subscribers (vs.
DSL), customers lacking online security/tech support/backup
add-ons, customers paying via electronic check, and senior
citizens without a partner or dependents. Distribution anal-
ysis of numerical features (Fig. 4) shows churn is high-
est among short-tenure, mid-to-high-paying customers, while
long-tenure, high-total-charge customers are the most loyal –
confirming tenure and contract type as leading churn predic-
tors.
Fig. 4: Distribution of numerical features by churn status.
C. Data Preprocessing
The following preprocessing pipeline was applied prior to
modeling:
•Irrelevant-column removal:customerIDwas
dropped.
•Missing values:convertingTotalChargesto numeric
revealed 11 rows with missing values, all corresponding
totenure=0 (logically inconsistent); these rows were
removed via listwise deletion.
•Duplicate removal:22 duplicated rows were identified
and dropped.
•Categorical encoding:one-hot encoding (with
drop=’first’) for XGBoost/LightGBM; CatBoost
consumed raw categorical columns natively via its
cat_featuresparameter, avoiding target leakage
from encoding.
•Target encoding:Churnmapped Yes/No→1/0.
•Stratified 80/20 train-test splitto preserve the
73.4%/26.6% class ratio in both partitions.
D. Feature Engineering
Fifteen domain-informed features were engineered to cap-
ture financial stress, service instability, and engagement signals
not directly present in the raw schema (Table III).
E. Churn Prediction: Training and Hyperparameter Optimiza-
tion
Each model was trained withRandomizedSearchCV
under stratified 5-fold cross-validation, optimizingaverage
precision(equivalent to PR-AUC) as the search objective. The
tuned hyperparameter spaces covered:
•Class weighting:scale_pos_weight
•Learning rate:learning_rate
•Regularization:reg_alpha,reg_lambda,
l2_leaf_reg
•Tree structure/complexity:max_depth,
depth,num_leaves,min_data_in_leaf,
min_child_weight,gamma
•Ensemble size:n_estimators,iterations
1) Class Imbalance Mitigation:The 1:2.76 churn/non-
churn ratio was addressed with two complementary strategies
rather than resampling alone:
1)Dynamic class weights:scale_pos_weightwas
searched using both the raw imbalance ratio (2.76) and
its square root (1.66), balancing sensitivity against over-
penalization of the majority class.

TABLE III: Newly Engineered Features
Feature Purpose
Monthly
Charges_to_
Total_Ratio
Short-term vs. long-term financial
commitment
NEW_Engaged Flags 1-/2-year contracts (lower churn
propensity)
Lack_of_
Protections Missing device/tech protection (security risk)
Young_
Unengaged_
Customers
Young customers on short-term contracts
Total_Active_
Services Count of active services (engagement proxy)
NEW_FLAG_
ANY_STREAMING Any streaming subscription (modern usage)
AutoPayment_
Usage Automatic payment method (payment reliability)
Average_
Charge_Per_
Month
Mean monthly spend over tenure
NEW_Increase Current vs. average monthly charge
Average_
Service_Cost Cost per active service (value perception)
Unstable_
Payment_
Behavior
Manual payment + short contract
(instability)
HighRisk_
Low_Tenure New customers (<6 months) lacking security
Tenure_Group Lifecycle-stage segmentation by tenure
Service_
Instability Security + tech-support gap indicator
HighSpend_
LowTenure High spend + low tenure (retention priority)
2)Threshold optimization:rather than the default 0.5 cut-
off, probabilistic predictions from 3-fold cross-validation
were swept across 100 thresholds∈[0.1,0.9], selecting
the threshold that maximized F1-score subject to a
minimum precision and recall of 0.7 each (Algorithm 1).
F . Customer Value Segmentation
Independently of churn-risk labels, customers were
segmented byvalueusing K-Means clustering (K= 3,
selected via the Elbow method, Fig. 5) on standardized
tenure,MonthlyCharges,TotalCharges,
and service-adoption features (OnlineSecurity,
TechSupport,StreamingTV,StreamingMovies).
PCA was then applied for two-dimensional visualization
(Fig. 6) using (5).
The resulting clusters were mapped to value categories:
High-Value(Cluster 0: long tenure, high spend, low churn
risk);Medium-Value(Cluster 1: moderate cost, high churn
risk); andLow-Value(Cluster 2: low cost/usage, low discon-
tinuation risk). Cross-tabulating these three value tiers against
the churn-risk label from Section IV-E produces the four op-
erational clusters used for marketing design:High-Risk/High-
Value,Low-Risk/High-Value,Medium-Value(both risk levels),
andLow-Risk/Low-Value. Detailed empirical profiles for each
Algorithm 1F1-Maximizing Decision Threshold Search
Require:Cross-validated churn probabilitiesˆp i, true labelsy i
Ensure:Optimal decision thresholdt ∗
1:T← {0.10,0.109, . . . ,0.90}▷100 evenly spaced
thresholds
2:best f1← −∞,t∗ ←0.5
3:foreacht∈Tdo
4:ˆy i ←⊮[ˆpi ≥t]
5:compute Precision(t), Recall(t),F1(t)via (8), (9)
6:ifPrecision(t)≥0.7andRecall(t)≥0.7then
7:ifF1(t)>best f1then
8:best f1←F1(t),t ∗ ←t
9:end if
10:end if
11:end for
12:ifno threshold satisfied the constraintthen
13:t ∗ ←arg max t F1(t)▷unconstrained fallback
14:end if
15:returnt ∗
Fig. 5: Elbow method confirmingK= 3as the optimal cluster
count.
combination – contract mix, internet service type, payment
method distribution, and service-adoption rates – are given in
Tables IV–VI.
G. Marketing Campaign Optimization
Marketing actions were designed per cluster:high-risk,
high-valuecustomers receive high-touch, personalized reten-
tion (free service months, exclusive content, flexible payment
plans);low-risk, high-valuecustomers receive scalable, cost-
conscious loyalty reinforcement (automated communication,
loyalty discounts, contract upgrades);medium-valuecustomers
receive a mix of upselling (tiered incentives, bundled ser-
vices) and, for the high-risk sub-group, more aggressive
cost-conscious retention; andlow-valuecustomers receive
lightweight engagement tactics (small discounts, referral pro-
grams, free streaming trials, family bundles) to control cost
while maintaining activity. Strategy selection is automated
via a lookup table indexed by (churn-risk, customer-value) as
shown in Algorithm 2.

Fig. 6: Customer clusters visualized on the first two principal
components.
TABLE IV: Characteristics of High-Value Customers
Characteristic High-Risk Low-Risk
Total customers 428 (6.1%) 1,656 (23.5%)
Monthly charges $42,712.20
(9.4%)
$151,310.65
(33.2%)
Contract mix 92.1% month-to-
month, 7.9% one-
year
51.3% two-year,
37.3% one-year,
11.4% month-to-
month
Internet service 97.4% fiber, 2.6%
DSL
59.2% fiber,
40.8% DSL
Payment method 65.7% electronic
check
33.6% bank trans-
fer, 33.5% credit
card
Streaming TV/Movies 94.9% / 93.7% 81.3% / 82.3%
Tech support / Sec. 33.4% / 24.5% 65.4% / 61.1%
H. Return on Investment (ROI) Analysis Framework
Because proprietary financial data was unavailable, a trans-
parent, substitutable theoretical framework was developed in-
stead of reporting a single unverifiable ROI figure. Estimated
customer lifetime (in months) is derived from the predicted
annual churn rate:
Lifetime= 12 Predicted Annual Churn Rate (10)
A retention intervention with efficacy ratee∈[0.15,0.30](a
conservative literature-informed range) extends this baseline
lifetime multiplicatively:
Lifetimeext =Lifetime base ×(1 +e)(11)
The discounted Customer Lifetime Value over horizonTis
CLV=
TX
t=1
Rt ·(1−Churn t)
(1 +d) t (12)
whereR t is revenue at montht, Churn t the predicted monthly
churn probability, anddthe discount rate. Campaign-level
financial return is then
ROI= (ARPU×Lifetime ext)−Campaign Cost Campaign Cost (13)
TABLE V: Characteristics of Medium-Value Customers
Characteristic Low-Risk High-Risk
Total customers 450 (6.4%) 1,871 (26.6%)
Avg. monthly charge $60.42 $74.05
Contract mix 60.4% month-
to-month, 34.9%
one-year
99.8% month-to-
month
Internet service 69.3% DSL,
30.7% fiber
22.9% DSL,
77.1% fiber
Payment method Balanced across
all
63.6% electronic
check
Streaming adoption 27% 33.5%
TABLE VI: Characteristics of Low-Value Customers
Characteristic Low-Risk High-Risk
Total customers 2,289 (32.6%) 338 (4.8%)
Contract mix 35.6% M2M,
35.6% two-year
100% month-to-
month
Internet service 60.9% none,
36.0% DSL
37.3% none,
48.8% DSL
Payment method 39.1% mailed
check
46.2% mailed
check, 34.0%
electronic check
Streaming adoption 7–8% 9–10%
Table VII presents hypothetical scenarios illustrating how tar-
geting efficiency scales with segment value; operators should
substitute their own ARPU and campaign-cost figures per
Section VII-C.
The framework’s key insight is that targeting efficiency
should be prioritized by marginal value per unit cost,
∆CLV
Cost →max(14)
which explains why the low-risk/high-value segment shows
the highest ROI multiple despite a smaller absolute churn
reduction: the low intervention cost of loyalty-reinforcement
campaigns dominates the ratio.
V. SYSTEMDEPLOYMENT
To move beyond an offline notebook study, the complete
pipeline was operationalized as an interactive web applica-
tion using theStreamlitframework, so that a non-technical
marketing analyst – not just the model’s authors – can act
on its output. The system follows a Model-View-Controller
pattern adapted for data-science applications: theModelhan-
dles preprocessing and inference (Pandas for data wrangling,
Scikit-learn for encoding, the tuned CatBoost classifier for
scoring), theViewis the Streamlit front end rendered with
Plotly, and theControllermanages file upload, filter state,
and session state across reruns. Internally, the application
executes a five-stage data pipeline – ingestion, preprocessing,
analysis, visualization, and report generation – summarized
architecturally in Fig. 7 and traced end-to-end as a sequence
diagram in Fig. 8.
A. Landing Page and Data-Control Sidebar
Fig. 9 shows the application’s landing page, which orients a
first-time user with a short “Getting Started” checklist (upload
a CSV , select target customer segments, explore insights) and

Algorithm 2Marketing Strategy Retrieval
Require:Selected filters:churn_risk,
customer_value
Ensure:List of recommended marketing strategies
1:DefineMARKETING_STRATEGIESas a dictionary map-
ping
(churn risk,customer value)→list of strategies
2:key←(churn_risk,customer_value)
3:ifkey∈MARKETING_STRATEGIESthen
4:returnMARKETING_STRATEGIES[key]
5:else
6:return“No specific strategy defined for this segment. ”
7:end if
TABLE VII: Hypothetical ROI Improvement Scenarios
Segment Churn Reduction CLV Increase ROI Multiple
High-Risk,
High-Value
25% +35% 3.5×
High-Risk,
Medium-
Value
20% +22% 2.8×
Low-Risk,
High-Value
10% +15% 4.1×
a summary of the four headline features: interactive data
visualization, targeted marketing recommendations, churn-risk
analysis, and customer-value segmentation. Once a file is
uploaded, the sidebar (Fig. 10) becomes the system’s primary
control surface: a drag-and-drop CSV uploader; two dropdown
filters forChurn Risk Level(All / Low / Medium / High)
andCustomer Value Segment(All / Low / Medium / High); a
checkbox to reveal a live preview of the preprocessed, encoded
dataframe; and one-click buttons to download the filtered,
preprocessed data. Selecting a filter combination immediately
reruns the Streamlit script and refreshes every downstream
metric, chart, and recommendation without a page reload.
B. Interactive Dashboards per Segment
After filtering, the main content area renders three headline
metrics (total customers, total monthly charges, average tenure
in months) followed by a bank of interactive Plotly visualiza-
tions – pie charts for churn-risk and customer-value distri-
bution, contract/internet-service/payment-method breakdowns,
and service-adoption bar charts – all scoped to the currently
selected segment. Fig. 11 contrasts these dashboards across
four segment views: High-Risk/High-Value, Low-Risk/High-
Value, Low-Risk/Low-Value, and the unfiltered “All Cus-
tomers” overview, illustrating how the same layout automat-
ically re-renders around whatever slice of the customer base
the analyst selects.
C. Automated Marketing Recommendations
Below the dashboards, the interface surfaces the rule-based
recommendations produced by Algorithm 2: a short “General
Marketing Approach” headline for the selected segment (e.g.,
Cost-Conscious Retentionfor low-risk customers,Personal-
ized Retentionfor high-risk, high-value customers), followed
Fig. 7: Three-tier system architecture: frontend (Streamlit wid-
gets), backend (Pandas/Plotly/Scikit-learn), and data pipeline.
Fig. 8: Customer data processing sequence, from CSV inges-
tion through filtering, preprocessing, metric computation, and
visualization refresh.
by a bulleted list of concrete, segment-specific tactics – auto-
mated communication and low-cost incentives for stable seg-
ments; free service months, exclusive content, and proactive
outreach for high-risk, high-value customers; tiered incentives
and service bundling for medium-value customers. Fig. 12
shows this panel rendered for four representative segments,
demonstrating that the tactics visibly change with both the
churn-risk and value axes rather than defaulting to a single
generic playbook.
D. Data Preview, Downloads, and Segment Reports
Two further capabilities close the loop between analysis
and offline use. First, toggling “Show Preprocessed Data”
in the sidebar expands a scrollable table preview of the
encoded dataframe actually consumed by the model (Fig. 13),
letting analysts sanity-check the transformation before trust-
ing the recommendations built on top of it; the same data
can be downloaded as CSV for use in Excel or a sepa-
rate BI tool. Second, a dedicated “Download Segment Re-
port” button (Fig. 14) generates a templated, human-readable
.txtreport for the currently selected segment via the
generate_segment_reportroutine described in Algo-
rithm 2 of the accompanying thesis – reporting the segment’s
customer count and percentage of the base, its share of total
monthly charges, its contract/internet-service/payment-method
distribution, and its adoption rate for each add-on service.
Fig. 15 shows a representative report for the High-Risk/High-
Value segment: 428 customers (6.1% of the base), $42,712.20

Fig. 9: Landing page of the Telecom Marketing Campaign Op-
timizer, with onboarding instructions and a feature summary.
TABLE VIII: Positive-Class (Churn) Metrics on the Test Set
Model Acc. Prec. Rec. F1 PR-AUC ROC-AUC
XGBoost 0.7633 0.5386 0.7647 0.6320 0.6481 0.8408
LightGBM 0.7612 0.5351 0.7754 0.6332 0.6478 0.8397
CatBoost 0.7768 0.5612 0.7353 0.6366 0.6553 0.8403
in monthly charges (9.4% of total revenue), 92.1% on month-
to-month contracts, and 97.4% on fiber-optic internet – the
exact figures underlying Table IV, now packaged as a stand-
alone artifact a marketing team can attach to a campaign brief
without touching the underlying notebook.
E. Interactive Features Summary
In sum, the deployed dashboard provides: (1) CSV upload
and dynamic filtering by churn-risk level and value segment;
(2) real-time key-metric computation (customer counts, total
monthly charges, average tenure); (3) interactive Plotly visu-
alizations (pie charts for churn/value/service distributions, bar
charts for service adoption, line charts for revenue trends); (4)
automated, rule-based marketing-strategy recommendations
per Algorithm 2; and (5) one-click download of preprocessed
data (CSV) and detailed per-segment text reports. Every el-
ement above is generated directly from the CatBoost model
and K-Means segmentation of Section IV – there is no manual
hand-off between the ML pipeline and what the marketing
team ultimately sees.
VI. EXPERIMENTALRESULTS
A. Churn Prediction Model Performance
Table VIII reports positive-class (churner) metrics and Ta-
ble IX reports weighted-average metrics for all three tuned
models on the held-out test set, after threshold optimization
(Algorithm 1).
CatBoost was selected as the deployment model, bal-
ancing precision (56.12%) against recall (73.53%) with the
Fig. 10: Sidebar data controls: CSV upload, churn-risk and
value-segment filters, preprocessed-data preview toggle, and
download buttons.
TABLE IX: Weighted-Average Performance Metrics on the
Test Set
Model Acc. Prec. Rec. F1 PR-AUC ROC-AUC
XGBoost 0.7633 0.8036 0.7633 0.7741 0.6481 0.8408
LightGBM 0.7612 0.8051 0.7612 0.7725 0.6478 0.8397
CatBoost 0.7768 0.8041 0.7768 0.7852 0.6553 0.8403
highest F1-score (0.6366) and PR-AUC (0.6553) – the met-
ric most relevant under class imbalance – while also bene-
fiting operationally from native categorical-feature handling
and 77.68% overall accuracy. LightGBM achieved marginally
higher recall (77.54%) but at a precision cost (53.51%),
making it less suitable where false-positive retention spend
must be controlled.
As shown in Fig. 16, the optimized threshold yields 275

Fig. 11: Key metrics and visualizations for four segment
views: High-Risk/High-Value, Low-Risk/High-Value, Low-
Risk/Low-Value, and All Customers.
Fig. 12: Automated marketing-strategy panel for four seg-
ments, each showing a distinct general approach and tactic
list.
true positives (73.53% recall) and only 99 false negatives,
confirming effective class-imbalance mitigation while limiting
unnecessary retention spend to 215 false positives (56.12%
precision).
SHAP analysis (Fig. 17) confirms thatContract
type,MonthlyCharges, andtenureare the
strongest churn predictors, while the engineered
featuresMonthlyCharges_to_Total_Ratio,
Service_Instability, and
Unstable_Payment_Behaviorrank among the top
ten drivers – empirically validating the domain-specific
feature-engineering effort of Section IV-D. Customers with
disproportionately high short-term spend relative to total
charges show markedly higher churn propensity.
The ROC curve (Fig. 18, AUC = 0.8403) confirms strong
class separability, while the higher PR baseline (Fig. 19, PR-
AUC = 0.6553) demonstrates robustness specifically under
class imbalance. The steep precision rise at moderate recall
Fig. 13: Expandable preview of the preprocessed, encoded
dataframe, alongside the churn-risk and value-segment filter
controls.
Fig. 14: One-click segment-report generation and download
from the sidebar.
indicates the model’s ability to prioritize high-confidence
churn predictions – precisely the behavior required for cost-
efficient targeted marketing.
B. Customer Segmentation Results
K-Means segmentation (Section IV-F) partitioned the cus-
tomer base into High-Value (29.6% of customers, 18.04%
churn rate), Medium-Value (33.0%, 51.7% churn rate), and
Low-Value (37.4%, 11.2% churn rate) segments (Fig. 20).
Notably, the Medium-Value segment exhibits by far the
highest churn rate (51.7%), despite contributing a moderate
revenue share – identifying it as the segment where retention
spend has the greatest volume impact, while the smaller
High-Risk/High-Value segment (6.1% of customers, Table IV)
represents the highestper-customerfinancial exposure.
C. Marketing Strategy Optimization and ROI Outcomes
Applying the segment-specific strategies of Section IV-
F, retention campaigns targeted at high-risk, high-value cus-
tomers produced the highest marginal ROI by preserving
substantial future revenue, while upsell campaigns toward low-
risk, high-value customers produced consistent revenue growth
at low campaign cost (Table VII). Generalized, non-segmented
retention campaigns applied uniformly to low-value customers
showed diminishing returns, confirming that segmentation-

Fig. 15: Sample auto-generated segment report (High-
Risk/High-Value), showing customer count, revenue share, and
contract/service distributions
Fig. 16: CatBoost confusion matrix after threshold optimiza-
tion: 275 true positives, 215 false positives, 99 false negatives,
818 true negatives.
based prioritization – not churn prediction alone – is what
drives ROI efficiency.
VII. DISCUSSION
A. Key Insights
Combining churn prediction with value segmentation and
financial evaluation produces substantially more actionable
insight than any component alone. A key empirical finding
is that high-value customers with onlymoderatechurn risk
can generate greater long-term financial losses than low-
value customers withhighchurn probability – reinforcing the
importance of probability-based, value-aware decision-making
Fig. 17: SHAP feature importance for the deployed CatBoost
model.
Fig. 18: ROC curve for the deployed CatBoost model (AUC
= 0.8403).
rather than binary churn labels. The superior performance of
CatBoost further confirms the practical advantage of native
categorical handling on telecom-style tabular data with nu-
merous nominal fields (contract type, internet service, payment
method).
B. Addressing Research Gaps
This work addresses the three gaps identified in Sec-
tion II: (1) churn prediction is embedded directly within a
segmentation-and-marketing pipeline rather than treated as a
stand-alone classifier; (2) segmentation explicitly incorporates
churn-risk probability alongside value metrics, rather than
being computed independently; and (3) the framework is
operationalized as a deployed, interactive system (Section V)
rather than remaining a purely offline analysis.
C. Limitations
Several limitations should be considered when interpreting
these results. The IBM Telco dataset is a single static snapshot

Fig. 19: Precision-Recall curve for CatBoost (AP = 0.655).
Fig. 20: Proportion of customers and churn rate per value
segment.
lacking temporal/seasonal dynamics or external market signals
(competitor pricing, macroeconomic shifts). CLV estimates
rely on simplified linear-churn and uniform-ARPU assump-
tions (Section IV-H); real deployments should recalibrate (10)–
(13) with actual ARPU and campaign-cost data. ROI outcomes
reported here are theoretical, simulated scenarios rather than
live A/B-tested campaign results. Finally, the Streamlit in-
terface currently supports only fixed visualization types and
single-user sessions, and does not yet integrate multi-user role-
based access or external CRM/network data streams.
VIII. CONCLUSION ANDFUTUREWORK
This paper presented a complete, reproducible ML-
based marketing optimization framework for telecom churn
management, integrating gradient-boosting churn prediction,
two-dimensional value/risk customer segmentation, tailored
marketing-strategy design, and a transparent ROI/CLV frame-
work, all operationalized in an interactive Streamlit applica-
tion. Among three tuned gradient-boosting models,CatBoost
achieved the best balanced performance (77.68% accuracy, F1
= 0.6366, PR-AUC = 0.6553), and SHAP analysis confirmed
that both raw features (contract type, monthly charges, tenure)
and engineered features (payment stability, service instabil-
ity ratios) meaningfully drive predictions. Cross-tabulating
churn risk with K-Means-derived value segments revealed
that Medium-Value customers carry disproportionate churn
risk (51.7%) while High-Risk/High-Value customers, though
only 6.1% of the base, represent the highest per-customer
financial exposure – distinct problems requiring distinct, and
now automated, marketing responses.
Future work will (1) incorporate real-time behavioral
streams (support logs, network-quality metrics, social signals)
for temporal/survival-based churn modeling; (2) explore rein-
forcement learning for continuously self-optimizing campaign
allocation; (3) extend the framework to other subscription-
based industries (streaming, SaaS, utilities) where churn dy-
namics are structurally similar; and (4) add multi-user, role-
based access to the Streamlit deployment to support collabo-
rative use by larger marketing organizations.
CODE ANDDATAAVAILABILITY
The complete implementation – churn-model notebooks, the
integrated segmentation/marketing pipeline, and the Streamlit
deployment package – is available at the authors’ GitHub
repository (contact us if you need any clarification). The IBM
Telco Customer Churn dataset is publicly available on Kaggle
[20].
REFERENCES
[1] Corporate Finance Institute, “Customer Acquisition Cost (CAC),”
[Online]. Available: https://corporatefinanceinstitute.com/resources/
accounting/customer-acquisition-cost-cac/, Accessed: Oct. 15, 2023.
[2] B. Artha, I. Zahara, B. Bahri, and N. Sari, “Customer Retention: A
Literature Review,”Social Science Studies, vol. 2, pp. 030–045, Jan.
2022. doi: 10.47153/sss21.2952022.
[3] M. P. Pandian, “5 - RFID Issues,” inRFID for Libraries, Chandos
Publishing, 2010, pp. 133–149.
[4] R. Ramachandran, “Customer Lifetime Value,” presented at an industry
conference, Feb. 2006. doi: 10.13140/2.1.1787.1049.
[5] Project Management Institute (PMI), “CRM Program Planning,”
[Online]. Available: https://www.pmi.org/learning/library/
crm-program-planning-7978, Accessed: Oct. 15, 2023.
[6] D. Sridevi, R. Ramki, R. Saini, A. S. Mohideen, S. Natarajan, and M.
Rajalakshmi, “Predictive Analytics for Marketing Campaign Optimiza-
tion,” 2024.
[7] R. Mattison,The Telco Churn Management Handbook, 2001.
[8] S. K. Wagh et al., “Customer Churn Prediction in Telecom Sector Using
Machine Learning Techniques,”Results in Control and Optimization,
2024.
[9] A. K. Ahmad, A. Jafar, and K. Aljoumaa, “Customer Churn Prediction
in Telecom Using Machine Learning in Big Data Platform,” 2019.
[10] G. R. Normeshie, “Churn Model in the Mobile Telecommunications
Industry in Ghana: A Case Study of V odafone Ghana,” 2013.
[11] M. Alkhayrat, M. Aljnidi, and K. Aljoumaa, “A Comparative Dimen-
sionality Reduction Study in Telecom Customer Segmentation Using
Deep Learning and PCA,”Journal of Big Data, 2020.
[12] P. Kotler and K. L. Keller,Marketing Management(14th ed.), Shanghai
People’s Publishing House, 2016.
[13] F. Sudirjo, “The Importance of Market Segmentation for Business
Entrepreneurs Affects Marketing Performance,”International Journal
of Management (IJM), vol. 14, no. 1, 2023.
[14] W. Zeng, “Telecommunications Industry: Analysis on Customer At-
trition Prediction and Segmentation,”BCP Business & Management
EMFRM, vol. 38, 2023.
[15] D. Chaffey and F. Ellis-Chadwick,Digital Marketing: Strategy and
Implementation, Pearson Education, 2019.
[16] K. Lemon and P. Verhoef, “Understanding Customer Experience
Throughout the Customer Journey,”Journal of Marketing, 2016.
[17] T. Chen and C. Guestrin, “XGBoost: A Scalable Tree Boosting System,”
inProc. 22nd ACM SIGKDD Int. Conf. on Knowledge Discovery and
Data Mining, 2016.

[18] G. Ke et al., “LightGBM: A Highly Efficient Gradient Boosting Decision
Tree,” inAdvances in Neural Information Processing Systems, 2017.
[19] L. Prokhorenkova et al., “CatBoost: Unbiased Boosting with Categorical
Features,” inAdvances in Neural Information Processing Systems, 2018.
[20] IBM, “Telco Customer Churn,” Kaggle. [Online]. Available:
https://www.kaggle.com/datasets/blastchar/telco-customer-churn,
Accessed: Dec. 29, 2024.
[21] W. Verbeke, D. Martens, C. Mues, and B. Baesens, “Building Com-
prehensible Customer Churn Prediction Models with Advanced Rule
Induction Techniques,”Expert Systems with Applications, vol. 38, no.
3, pp. 2354–2364, 2012.
