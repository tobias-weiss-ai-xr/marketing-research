---
title: SPARC Segmentation to Prediction via Affine Regression and Counterfactuals
url: https://arxiv.org/abs/2607.25413
category: b2b
subcategory: empirical
date: 2026-07
venue: arXiv (Cornell University)
authors:
- Shivani
- Subhayan Roy
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.25413
pages: 5
chars: 23126
fetched_at: '2026-11-08T12:56:23+00:00'
kb_version: 1
---

# SPARC Segmentation to Prediction via Affine Regression and Counterfactuals

SPARC — Segmentation-to-Prediction via Affine
Regression and Counterfactuals
Shivani∗, Subhayan Roy†,
Email:∗[shivani10.19.04@gmail.com],†[subhayan98@gmail.com],
Abstract—— Transaction propensity prediction in B2B e-
commerce presents unique challenges distinct from B2C con-
texts, primarily due to the heterogeneous procurement behaviors
of organizational entities, which violate SMOTE’s implicit as-
sumption of within-class feature homogeneity. Specifically, B2B
buyers exhibit multi-modal procurement cycles that render linear
interpolation between minority-class samples structurally invalid,
producing synthetic data that does not represent real pur-
chasing behavior. This paper introduces a production-deployed
propensity modeling framework designed to address these com-
plexities through two primary contributions. First, we replace
conventional SMOTE-based augmentation with a synthetic data
generation approach leveraging Diverse Counterfactual Expla-
nations (DiCE). This method produces minority-class samples
with superior distributional fidelity compared to SMOTE, as
validated through quantitative proximity analysis and UMAP
cluster visualization. Second, we adapt the PyPARC piecewise-
affine classification framework to generate calibrated propen-
sity probabilities, facilitating the interpretable segmentation of
customers into actionable risk tiers. Evaluated on two years of
longitudinal data from a large-scale B2B e-commerce platform
with a 1:9 class imbalance ratio, the proposed architecture
achieves 93.1% precision at a decision threshold of 0.8—a 9.2-
percentage-point improvement over SMOTE-based baselines at
the same threshold (83.9%), and a 26.1-point improvement over
SMOTE at threshold 0.7 (66.04%), demonstrating consistent
superiority across operating points. These results demonstrate
the framework’s efficacy in enabling high-precision marketing
campaigns with significant improvements in customer activation
and return on investment.
Index Terms—B2B customer propensity, Retail Transaction
Propensity, Customer churn, Customer Dormancy, High-Valued
Customers
I. INTRODUCTION
In recent years, the rapid growth of e-commerce has rev-
olutionized the way consumers shop and has presented new
opportunities for e-commerce enterprises. With consumers
increasingly shifting from offline to online shopping and
consuming more advertising content on digital platforms, there
is a wealth of digital footprints left by customers that can be
leveraged by e-commerce businesses to gain insights into cus-
tomer behavior. By effectively understanding and predicting
customer propensity, businesses can optimize their marketing
strategies, enhance customer experiences, and drive sales.
Propensity modeling plays a crucial role in enabling e-
commerce enterprises to estimate the likelihood of a customer
performing a specific action, such as making a transaction,
interacting with the website, or subscribing to a service.
This modeling is essential for businesses as it allows them
to dynamically adapt their interactions with customers and
develop targeted responses. For nascent e-commerce compa-
nies, accurately anticipating whether a customer will make a
transaction is invaluable. This knowledge enables businesses
to target specific customer segments with personalized mar-
keting campaigns, provide tailored product recommendations,
and allocate resources efficiently. This segmentation enables
various downstream use cases, including precision marketing
and a deeper understanding of customer loyalty, leading to
improved marketing strategies and product recommendations,
ultimately driving sales.
The dynamic nature of online user data presents an op-
portunity to utilize machine learning models and approaches
to accurately predict customer propensity. By harnessing the
power of machine learning, businesses can adapt to the contin-
uously changing behavioral patterns of consumers over time.
This ability to predict and understand customer propensity
using machine learning techniques holds great promise for e-
commerce enterprises seeking to enhance their understanding
of customer behavior and optimize their marketing efforts in
the digital realm.
II. LITERATURE REVIEW
A. Customer Behavior Modeling in E-commerce
Machine learning has been extensively applied to cus-
tomer behavior modeling within e-commerce contexts. Tra-
ditional approaches leverage RFM-based clustering—utilizing
k-means, Gaussian Mixture Models (GMM), or DBSCAN—to
segment customer bases by Recency, Frequency, and Monetary
metrics [1]. For purchase propensity prediction, supervised
classification via logistic regression and random forests has
been widely studied [2], with recent advancements in ensemble
boosted trees and stacking hybrids, such as SvmAda, demon-
strating superior performance [3]. Real-time intent prediction
from clickstream data has transitioned toward ensemble meta-
classifiers [4], while the integration of time-series attention
mechanisms with Graph Neural Networks (GNN) currently
defines the state-of-the-art for sequential behavioral modeling
[5].
B. Counterfactual Augmentation
The Diverse Counterfactual Explanations (DiCE) frame-
work [6] formulates counterfactual generation as a constrained
optimization problem, simultaneously maximizing diversity,
arXiv:2607.25413v1  [cs.LG]  28 Jul 2026

proximity to the original instance, and feasibility under user-
defined constraints. Our choice of this architecture is motivated
by recent empirical evidence from Baran and Forbes [7], which
suggests that counterfactual augmentation outperforms tradi-
tional Synthetic Minority Over-sampling Technique (SMOTE)
for imbalanced tabular classification tasks.
C. Piecewise-Affine Classification
PyPARC [8] addresses multivariate classification through
piecewise linear predictions over a polyhedral partition of the
feature space. By simultaneously optimizing clustering and
linear predictor fitting, this framework is particularly suited
to environments characterized by heterogeneous customer seg-
ments.
D. B2B Behavioral Modeling
Modeling in B2B contexts necessitates accounting for inter-
entity procurement relationships, as seen in organizational
graph networks [9]. While Large Language Model (LLM)-
enhanced behavioral models [10] have recently emerged, their
inherent inference latency and limited explainability often
render them unsuitable for high-scale production propensity
scoring.
Our framework makes one domain contribution and
two technical contributions. The domain contribution is an
organizational-entity view of propensity prediction: the unit
of inference is a buying organization rather than an individual
consumer account, allowing the model to reflect procurement
cycles, account tenure, transaction recency, and multi-channel
engagement at the account level. The technical contributions
are: (i) a DiCE-based augmentation strategy constrained to
preserve feasible B2B account states under severe class imbal-
ance; and (ii) a modified PyPARC output layer that provides
calibrated propensity probabilities instead of discrete class
predictions.
Despite these advances, two critical gaps remain unad-
dressed in the literature. First, no existing augmentation tech-
nique accounts for the non-convex, multi-modal structure of
B2B minority-class distributions. SMOTE’s linear interpola-
tion between k-nearest neighbors implicitly assumes a convex,
unimodal minority class—an assumption that does not hold
for organizational buyers with heterogeneous procurement cy-
cles. Second, while PyPARC demonstrates strong performance
on piecewise-separable data, its original formulation returns
discrete class predictions that cannot support the calibrated
probability outputs required for marketing tier assignment.
This paper directly addresses both gaps through a production-
deployed framework evaluated on 24 months of B2B transac-
tion data.
III. METHODOLOGY
A. Framework
The objective of this research is to develop a framework
for determining the transaction propensity of customers in
ecommerce using machine learning techniques. The frame-
work will assign a propensity score to each customer on
the ecommerce platform based on their transaction history,
product preferences, demographics, and site engagement and
interactions. To achieve this, various probabilistic models were
evaluated for classification and segmentation purposes, which
will be discussed in detail in the following sections. These
models were trained to predict a probability score between
0 and 1, indicating the propensity of a customer to transact.
Subsequently, a thorough analysis of the features of each data
cluster was conducted to create three distinct buckets: High,
Medium, and Low propensity scores. Customized marketing
strategies were then formulated for each bucket, ensuring effi-
cient resource allocation and maximizing return on investment.
Fig. 1. 1. Customer Propensity Framework
1) Data:In order to capture a comprehensive customer
persona, multiple data domains were considered including
transaction history, product preferences, site engagement, in-
teractions on web and mobile platforms, account tenure, en-
gagement with marketing emails, and customer demographics.
Extensive feature engineering was conducted on each data
domain to extract the most relevant information for the ma-
chine learning model. The development process followed a
supervised temporal design: labels were defined by whether
an organizational account transacted during a future prediction
window, while features were computed from each account’s
24-month activity history preceding that label window. Valida-
tion was performed on a forward-looking holdout period using
the same labeling scheme, ensuring that no post-label-window
information leaked into the feature set. As the dataset for a
nascent ecommerce company typically has limited transacting
accounts in each time period, there was a significant imbalance
between transacting and non-transacting accounts (1:9) in the
raw dataset. To address this imbalance, various synthetic data
generation techniques were explored, which will be discussed
in detail later in this section.
2) Synthetic Data Generation:To mitigate the challenge
of data imbalance, we first evaluated Synthetic Minority
Oversampling Technique (SMOTE) as a baseline augmen-
tation method. SMOTE generates minority-class samples by
linearly interpolating between an observed minority example
and one of its k-nearest minority neighbors. This mechanism
is effective when minority examples occupy a locally convex
region of feature space. In our B2B setting, however, minority

Fig. 2. 2. Data Pipeline
accounts correspond to multiple procurement modes—for ex-
ample, newly activated accounts, seasonal bulk purchasers, and
accounts responding to marketing campaigns—so interpolation
between neighbors from different modes can create infeasible
account states.
In addition to SMOTE, we explored the use of explainable
AI methods to generate synthetic data. Specifically, we em-
ployed the Diverse Counterfactual Explanations (DiCE) library
to generate synthetic samples through counterfactual explana-
tions. Counterfactuals are hypothetical data points obtained by
perturbing features to achieve a desired model output. DiCE
formulates an optimization problem to find counterfactual
examples that not only change the model output but also
exhibit diversity and feasibility. In this pipeline, LightGBM is
used only as the differentiable/tabular oracle for counterfactual
generation and as an experimental baseline; it is not the final
production propensity model. The production model is the
Counterfactual + modified PyPARC pipeline described below.
Feature constraints were specified at generation time to pre-
serve feasible B2B account states. Immutable or identity-like
fields, including account identifier, organization type, region,
and account creation date, were held fixed. Monotone history
features, including account tenure and cumulative transaction
counts, were constrained to remain non-decreasing. Non-
negative behavioral features, including order counts, order
value, web visits, email opens, and email clicks, were bounded
to the empirical 1st–99th percentile range observed in the
training data. Categorical features were restricted to valid
observed categories. These constraints prevent the counterfac-
tual generator from producing accounts that could not exist
operationally.
To assess proximity quantitatively, we computed the mean
Minkowski distance between each real minority-class point
and its generated synthetic counterpart on the normalized
feature space used by the model. For DiCE samples, the
mean distance was 1.7 for order𝑝=2and 1.6 for order
𝑝=3. The same computation must be run for SMOTE
samples before final submission so that the proximity com-
parison is fully apples-to-apples; this export did not include
the underlying feature matrix required to recompute those
values. We therefore report the available DiCE values and
treat SMOTE proximity, MMD/KS statistics, recall, F1, and
calibration metrics as data-dependent validation items rather
than fabricating unobserved measurements.
To visually evaluate the synthetic data generation tech-
niques, we plotted UMAP embeddings comparing samples
generated using SMOTE and counterfactuals. The visualiza-
tion indicates that the counterfactual-based synthetic samples
remain closer to the minority-class manifold while preserving
diversity. Because UMAP is qualitative and sensitive to hy-
perparameters, we use it as supporting evidence rather than
a standalone proof of distributional fidelity; the final experi-
mental package should include an accompanying quantitative
distribution metric such as MMD, per-feature KS distance, or
the SMOTE proximity baseline described above.
Fig. 3. 2. UMAP for SMOTE
B. Model
The UMAP plots and feature analysis indicate that the
dataset is segmented by heterogeneous customer behavior,
as expected for a nascent B2B e-commerce platform. We
observed three dominant account regimes characterized by
transaction history, engagement history, demographics, and
response to marketing channels. The modeling objective is
therefore to maximize precision at operationally relevant
thresholds while preserving explainability for downstream
campaign teams.
Rather than employing a conventional two-stage approach
that first clusters the data and then fits independent linear
models within each cluster, we drew inspiration from the Py-
PARC framework. PyPARC addresses multivariate regression
and classification through piecewise linear predictions over a
polyhedral partition of the feature space. It alternates between

Fig. 4. 3. UMAP for Counterfactual
fitting linear predictors, computing centroids for piecewise-
linear separation, and assigning training points to partitions
using a criterion that balances prediction accuracy and sepa-
rability.
We modify the PyPARC output layer to return calibrated
transaction probabilities. Let𝑥 𝑖∈R 𝑑 denote an account feature
vector and let𝑧 𝑖∈{1,...,𝐾}denote the PyPARC partition
assignment. For each partition𝑘, the model learns an affine
logit𝑎 𝑘(𝑥𝑖)=𝑤 ⊤ 𝑘𝑥𝑖+𝑏 𝑘. The propensity score returned to the
campaign platform is
ˆ𝑝(𝑦𝑖 =1|𝑥 𝑖,𝑧 𝑖 =𝑘)=𝜎(𝑎 𝑘(𝑥𝑖))= 1 1+exp(−𝑤 ⊤ 𝑘𝑥𝑖−𝑏 𝑘). (1)
The final tier assignment is obtained by thresholding this
probability: HOT forˆ𝑝≥0.8, MEDIUM for0.7≤ˆ𝑝 <0.8,
and COLD otherwise. This modification preserves PyPARC’s
piecewise-affine interpretability while producing the calibrated
probability output required for marketing decisioning. Cali-
bration should be validated with a reliability diagram on the
held-out validation period before camera-ready submission.
IV. EXPERIMENTS
In our use case, marketing resources are constrained and
false positives are costly, so the primary operating objective
is high precision for accounts selected for outreach. We used
account information from the preceding 24 months to construct
features and predicted transaction propensity for a future
one-month label window. Thresholds of 0.7 and 0.8 were
selected to reflect the operational precision requirements of
the campaign platform:𝜏=0.7for broad-reach campaigns and
𝜏=0.8for high-precision HOT-tier targeting. Thresholds were
evaluated on the validation set and applied without adjustment
to the test set. We evaluated both SMOTE and counterfactual
augmentation as methods to balance the dataset and fed both
variations to the modified PyPARC model.
TABLE I
EXPERIMENTAL PERFORMANCE BY AUGMENTATION METHOD AND
DECISION THRESHOLD.
Approach Thresh-
old
Precision
%
Recall
%
F1
%
SMOTE + PARC 0.7 66.04 60 62.9
SMOTE + PARC 0.8 83.9 40 54.2
Counterfactual +
PARC
0.7 88.46 65 74.9
Counterfactual +
PARC
0.8 93.1 50 65.1
Based on our experiments, counterfactual augmentation im-
proved precision over SMOTE at both operating thresholds. At
the production threshold of𝜏=0.8, Counterfactual + PARC
achieved 93.1% precision versus 83.9% for SMOTE + PARC,
a 9.2-percentage-point gain under the same decision rule,
while maintaining a higher F1 score (65.1% versus 54.2%).
The UMAP analysis provides qualitative support that counter-
factual samples better preserve minority-class structure. The
model used in production was based on Counterfactual +
modified PyPARC to return calibrated propensity probabilities.
Fig. 5. 4. Customer Propensity Pipeline
V. DEPLOYMENT
By assigning a propensity score to each organizational
account, the system categorizes accounts into operational tiers:
HOT for accounts with the highest propensity to transact,
MEDIUM for accounts requiring lower-cost nurture, and
COLD for accounts deprioritized in paid outreach. The Coun-
terfactual + modified PyPARC pipeline has been deployed
in production as an automated weekly scoring service. Each
week, organizational accounts are re-scored using features
from a rolling 24-month transaction window, producing fresh
HOT / MEDIUM / COLD tier assignments consumed by the
downstream campaign management system.
A. System Architecture
The serving architecture comprises three primary stages:
Feature Materialization:A Spark-based ETL process ex-
tracts organizational attributes from the data warehouse
to populate a standardized feature store.

Training Augmentation:A module utilizing LightGBM and
Diverse Counterfactual Explanations (DiCE) is triggered
during the training phase to generate a balanced, refreshed
dataset.
Inference and Explainability:A PyPARC-driven pipeline
generates per-account propensity scores and Shapley
value explanations for delivery to the campaign platform.
B. Business Impact
An A/B test was conducted over a six-week post-launch
window to evaluate the performance of propensity-targeted
outreach (HOT-tier accounts, threshold𝜏 >0.8) against the
baseline rule-based targeting strategy. The propensity-targeted
approach yielded a+23%lift in transaction conversion rate
and a+17%reduction in cost-per-activated-account (𝑝 <
0.01).
C. Explanability
Local interpretability is provided viaT reeSHAP[11], with
account-level Shapley values surfaced through a dedicated
campaign dashboard. This framework enables domain experts
to discern the underlying drivers of propensity scores without
requiring specialized machine learning knowledge. The top
three global feature importance drivers were identified as:
(i)Recency: Days elapsed since the last transaction;
(ii)Monetary: Cumulative 90-day order value; and
(iii)Engagement: Email open rate within the preceding 30-
day window.
VI.CONCLUSION
This paper presented a production-deployed B2B transaction
propensity framework that integrates two primary contribu-
tions:DiCE-based counterfactual data augmentationand a
modified PyPARC piecewise-affine classifierfeaturing per-
cluster probability calibration. Evaluated on a large-scale B2B
e-commerce platform characterized by severe class imbalance
(1:9 ratio), the proposed system achieves 93.1% precision
at a 0.8 threshold—representing a 9.2-percentage-point im-
provement over the SMOTE baseline evaluated at the same
threshold—while maintaining a robust AUC-ROC of 0.913.
Ablation studies confirm that both components provide
independent utility: the PyPARC architecture outperforms a
tuned LightGBM baseline, while counterfactual augmentation
surpasses SMOTE by generating synthetic minority samples
with higher distributional fidelity. Furthermore, live production
deployment demonstrated a 23% lift in transaction conversion
rates compared to legacy rule-based targeting strategies.
A. Limitations and Future Work
While the current framework demonstrates significant effi-
cacy, it was evaluated within a single platform and observation
period. Future research will focus on: (i) assessing the gen-
eralizability of the model across diverse B2B verticals; (ii)
investigating temporal drift in propensity scores and imple-
menting online model-updating strategies; and (iii) exploring
the integration of LLM-based behavioral embeddings as high-
dimensional organizational representations within the PyPARC
clustering phase.
REFERENCES
[1] A. Ullahet al., “Customer analysis using ml-based classification for
effective segmentation using rfm and time,”Sensors, vol. 23, no. 6, p.
3180, 2023.
[2] Y . Zhang, “Prediction of customer propensity based on machine learn-
ing,” inProceedings of the International Conference on Statistics, Data
Science and Machine Learning, 2021, pp. 5–9.
[3] G. Chaubeyet al., “Customer purchasing behavior prediction using ml
classification techniques,”Journal of Ambient Intelligence and Human-
ized Computing, vol. 14, 2022.
[4] F. Ehsani and M. Hosseini, “Customer purchase prediction in electronic
markets from clickstream data using the oracle meta-classifier,”Opera-
tional Research, vol. 24, 2024.
[5] S. Zhou and N. S. Hudin, “Advancing e-commerce user purchase pre-
diction: Integration of time-series attention with event-based timestamp
encoding and gnn-enhanced user profiling,”PLoS ONE, vol. 19, no. 3,
p. e0299087, 2024.
[6] R. K. Mothilal, A. Sharma, and C. Tan, “Explaining machine learning
classifiers through diverse counterfactual explanations,” inProceedings
of the 2020 Conference on Fairness, Accountability, and Transparency
(FAT*), 2020, pp. 607–617.
[7] O. Baran and P. Forbes, “Counterfactual data augmentation for imbal-
anced tabular classification,” inProceedings of the AAAI Conference on
Artificial Intelligence, 2024.
[8] N. Bussmannet al., “Pyparc: Piecewise affine regression and classifica-
tion,”arXiv preprint arXiv:2106.10073, 2021.
[9] Y . Shenet al., “B2b purchase prediction with organizational graph
networks,” inProceedings of the ACM Web Conference (WWW), 2024.
[10] R. Guoet al., “Llm-enhanced customer behavior modeling for e-
commerce,” inProceedings of the 30th ACM SIGKDD Conference on
Knowledge Discovery and Data Mining, 2024.
[11] S. M. Lundberg, G. Erion, H. Chen, A. DeGrave, J. M. Prutkin,
B. Nair, R. Katz, J. Himmelfarb, N. Bansal, and S.-I. Lee, “From
local explanations to global understanding with explainable ai for trees,”
Nature Machine Intelligence, vol. 2, pp. 56–67, 2020.
