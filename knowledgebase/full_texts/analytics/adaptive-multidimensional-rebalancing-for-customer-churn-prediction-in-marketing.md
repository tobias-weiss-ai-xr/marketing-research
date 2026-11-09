---
title: Adaptive multidimensional rebalancing for customer churn prediction in marketing analytics
url: https://doi.org/10.12688/f1000research.188025.1
category: analytics
subcategory: empirical
date: 2026-09
venue: F1000Research
authors:
- Ahmad Cahyono Adi
- Surya Arafah
- Beatrix Ayuwandira Dabur
source: openalex-oa
pdf_url: https://f1000research.com/articles/15-1558/pdf
pages: 15
chars: 58738
fetched_at: '2026-11-08T17:57:27+00:00'
kb_version: 1
---

# Adaptive multidimensional rebalancing for customer churn prediction in marketing analytics

RESEARCH ARTICLE
Adaptive multidimensional rebalancing for customer churn
prediction in marketing analytics
[version 1; peer review: awaiting peer review]
Ahmad Cahyono Adi
 1, Surya Arafah2, Beatrix Ayuwandira Dabur2,
Eni Nur Hayati3, Nur Arifah4, Andy Dwiki Iranda3, Maria Fransiska Pabundu1,
Ranip Fahmi5, Khusnul Afifah Zharaura1, Rahmadani Mailoa4,
Romanus Hadyanto Ongan1, Putri Emilia Bloemhard1, Khosyi Tiara Anggita5,
Indah Murni1
1Universitas Gadjah Mada, Yogyakarta, Special Region of Yogyakarta, Indonesia
2Universitas Padjadjaran, Bandung, West Java, Indonesia
3Universitas Diponegoro, Semarang, Central Java, Indonesia
4Universitas Indonesia, Depok, West Java, Indonesia
5Institut Teknologi Bandung, Bandung, West Java, Indonesia
First published: 22 Sep 2026, 15:1558
https://doi.org/10.12688/f1000research.188025.1
Latest published: 22 Sep 2026, 15:1558
https://doi.org/10.12688/f1000research.188025.1
v1

Abstract
Background
Customer churn prediction is a strategic imperative for maximizing
Customer Lifetime Value (CLV) and optimizing retention return on
investment (ROI). However, real-world churn datasets suffer from
severe class imbalance and high-dimensional class overlap, causing
conventional models to ignore minority patterns. Existing resampling
techniques often generate synthetic noise in ambiguous deci-sion
boundaries, degrading both predictive accuracy and business value.
Methods
This study proposes the Adaptive Multidimensional Rebalancing (AMR)
framework that dynamically evaluates the local topological structure
of the feature space, specifically local density, class overlap, and
feature variability, to adap-tively allocate synthetic minority samples.
AMR employs a constrained interpo-lation mechanism that prevents
synthetic instances from bleeding into majority-class regions. The
framework is evaluated across four diverse business sectors
(Telecommunications, Banking, Credit Card, and Insurance) and
integrated with cost-sensitive ensemble classifiers.
Open Peer Review
Approval Status  AWAITING PEER REVIEW
Any reports and responses or comments on the
article can be found at the end of the article.
 
 Page 1 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Corresponding author: Ahmad Cahyono Adi (ahmadcahyonoadi@mail.ugm.ac.id)
Author roles: Adi AC: Conceptualization, Formal Analysis, Funding Acquisition, Investigation, Methodology, Project Administration,
Resources, Supervision, Visualization, Writing – Original Draft Preparation; Arafah S: Investigation, Methodology, Software, Validation,
Writing – Review & Editing; Dabur BA: Formal Analysis, Investigation, Methodology, Validation, Writing – Review & Editing; Hayati EN:
Formal Analysis, Investigation, Methodology, Validation, Writing – Original Draft Preparation; Arifah N: Investigation, Methodology,
Resources, Software, Visualization, Writing – Review & Editing; Iranda AD: Conceptualization, Methodology, Validation, Writing – Review
& Editing; Pabundu MF: Investigation, Methodology, Validation, Writing – Review & Editing; Fahmi R: Investigation, Validation,
Visualization, Writing – Review & Editing; Zharaura KA: Investigation, Methodology, Validation, Writing – Review & Editing; Mailoa R:
Investigation, Supervision, Validation, Writing – Review & Editing; Ongan RH: Conceptualization, Methodology, Resources, Validation,
Visualization, Writing – Review & Editing; Bloemhard PE: Data Curation, Formal Analysis, Investigation, Validation, Visualization, Writing
– Review & Editing; Anggita KT: Formal Analysis, Investigation, Validation, Visualization, Writing – Review & Editing; Murni I:
Methodology, Validation, Visualization, Writing – Review & Editing
Competing interests: No competing interests were disclosed.
Grant information: This research was supported by funding from the Indonesian Endowment Fund for Education (LPDP), Indonesia.
The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.
Copyright: © 2026 Adi AC et al. This is an open access article distributed under the terms of the Creative Commons Attribution License,
which permits unrestricted use, distribution, and reproduction in any medium, provided the original work is properly cited.
How to cite this article: Adi AC, Arafah S, Dabur BA et al. Adaptive multidimensional rebalancing for customer churn prediction in
marketing analytics [version 1; peer review: awaiting peer review] F1000Research 2026, 15:1558
https://doi.org/10.12688/f1000research.188025.1
First published: 22 Sep 2026, 15:1558 https://doi.org/10.12688/f1000research.188025.1
Results
Extensive experiments demonstrate that AMR achieves statistically
sig-nificant improvements in predictive stability (AUPRC) compared to
state-of-the-art baselines like SMOTE-ENN (p < 0.05). AMR exhibits
superior computational ef-ficiency, reducing resampling runtime by
approximately 35% compared to hybrid
methods. By maximizing the Expected Maximum Profit (EMP) and
leveraging SHAP-based Explainable AI (XAI), AMR enhances predictive
sensitivity and pro-vides actionable, interpretable insights.
Conclusions
AMR bridges the gap between complex machine learning and profit-
centric marketing objectives, offering a robust, scalable, and
interpretable solution for customer retention.
Keywords
Customer Churn Prediction, Marketing Analytics, Customer Lifetime
Value, Adaptive Multidimensional Rebalancing, Cost-Sensitive
Learning, Explainable AI, Expected Maximum Profit
  Page 2 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Introduction
In the contemporary era of the digital economy, decoding digital market power and understanding complex consumer
behavior are essential for maintaining a strategic advantage.1 Within this landscape, customer retention has ascended as a
primary strategic imperative for service-oriented organizations.2,3 Empirical evidence from the Harvard Business Review
and various marketing studies consistently demonstrates that the cost of acquiring a new customer can be five to twenty-
five times higher than the cost of retaining an existing one. 4,5 Customer churn, the phenomenon wherein customers
terminate their relationship or subscription with a company, poses a direct and substantial threat to a firm ’s long-term
profitability, market share, and Customer Lifetime Value (CLV).3,6 Consequently, predicting customer churn proactively
has become a cornerstone of Customer Relationship Management (CRM) and marketing analytics. 7,8 We draw upon
three foundational pillars that establish the economic and strategic imperative of churn prediction. Customer Retention
Theory posits that increasing customer retention rates by merely 5% can increase profits by 25% to 95%, establishing the
fundamental economic rationale for investing in predictive churn models. 4,1 This theory emphasizes that the cumulative
value of long-term customer relationships far exceeds the short-term gains from customer acquisition. Furthermore,
Relationship Marketing Theory emphasizes that long-term customer engagement is built on trust, commitment, and
mutual value creation; churn represents a breakdown in this relational bond, often preceded by subtle behavioral shifts
that can be detected through advanced analytics.9,3 This theoretical perspective suggests that churn is not a sudden event
but a gradual process of disengagement. Additionally, Customer Lifetime Value (CLV) Theory shifts the focus from
transactional metrics to the net present value of future cash flows from a customer, providing a framework for evaluating
the long-term economic impact of retention strategies. 9,4 Together, these theories establish that churn prediction is not
merely a technical classification problem but a strategic marketing imperative that requires sophisticated analytical tools
to identify at-risk customers and design targeted retention interventions.
Despite the widespread adoption of machine learning (ML) and deep learning (DL) models to forecast customer
defection, marketing analysts continually grapple with the inherent characteristics of real-world customer data. The
most pervasive of these challenges is the class imbalance problem.10,11 In typical business environments, the number of
customers who churn is significantly smaller than the number of customers who remain loyal. Standard predictive
algorithms, which are designed to maximize overall accuracy, often exhibit a severe bias towards the majority class (non-
churners). As a result, these models may achieve deceptively high overall accuracy while simultaneously producing a
high rate of false negatives, failing to identify the actual customers at risk of churning, thereby rendering the models
practically ineffective for retention campaigns. 12,13,14
Furthermore, modern marketing datasets are highly multidimensional, encompassing demographic profiles, transactional
histories, product usage logs, and customer service interactions. 15,8,5 This multidimensionality often exacerbates a
secondary issue known as class overlap, where the feature spaces of minority and majority classes are highly intertwined,
making the decision boundary ambiguous. 16 In marketing terms, this represents behavioral ambiguity, referring to
situations where at-risk customers exhibit usage patterns indistinguishable from loyal customers until the moment of
defection. While conventional data-level solutions like the Synthetic Minority Over-sampling Technique (SMOTE) or
algorithmic solutions like cost-sensitive learning have been employed to mitigate class imbalance, they frequently fall
short in high-dimensional, overlapping feature spaces, sometimes generating noisy synthetic data or overfitting the
minority class.17,18
This study proposes an Adaptive Multidimensional Rebalancing (AMR) framework for customer churn prediction.
AMR is not merely a classification framework; it is a retention-oriented analytical framework that dynamically adapts to
the data ’s topological structure. By doing so, it aligns predictive modeling with marketing analytics objectives,
maximizing both predictive sensitivity and economic profitability. 9,3 Specifically, this study addresses three core
research questions to guide our investigation:
[1] RQ1: Can topology-aware rebalancing improve churn prediction accuracy under severe class imbalance and
high-dimensional behavioral overlap?
[2] RQ2: Can the proposed AMR framework significantly improve Expected Maximum Profit (EMP) com-
pared to existing state-of-the-art resampling techniques?
[3] RQ3: Can interpretable churn drivers be effectively extracted through SHAP analysis to provide actionable
insights for targeted retention strategies?
Page 3 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

To answer these questions, this study makes three distinct contributions to the existing body of knowledge in marketing
analytics:
1. Methodological Contribution: We introduce the AMR framework, which transcends traditional static
resampling by dynamically evaluating local topological structures (density, overlap, and variability). This
fundamentally resolves the class overlap problem inherent in high-dimensional CRM data by employing a
constrained interpolation mechanism that prevents synthetic noise generation in ambiguous decision bound-
aries.
2. Theoretical Contribution: We bridge the gap between machine learning evaluation and marketing profitabil-
ity theory by integrating AMR with cost-sensitive ensemble learning. We demonstrate how topological data
analysis can operationalize CLV theory, ensuring that algorithmic optimization aligns with economic impact
rather than mere statistical accuracy.
3. Practical Marketing Contribution: By leveraging SHAP-based Explainable AI (XAI), we translate complex,
black-box predictions into actionable, interpretable customer segments. This enables marketing practitioners to
design targeted, cost-effective retention campaigns that maximize Return on Investment (ROI) by minimizing
false-positive retention costs and focusing resources on high-value at-risk customers.
Related work and theoretical foundations
The trajectory of customer churn prediction research has evolved significantly, shifting from basic statistical modeling to
sophisticated, AI-driven analytical frameworks. Churn prediction is deeply rooted in established marketing theories.
Customer Retention Theory and Relationship Marketing Theory posit that customer defection is a gradual erosion of
relational commitment rather than an abrupt event.9,3 Recent literature emphasizes that understanding the “silent signals”
of disengagement is critical. However, traditional marketing models often fail to capture these subtle, non-linear
behavioral shifts in high-dimensional data. Customer Lifetime Value (CLV) Theory further dictates that not all churners
are equal; the financial impact of losing a high-value customer far outweighs that of a low-value one.4 Despite this, many
predictive models treat all churns equally, misaligning with the profit-centric objectives of modern marketing.
Early efforts relied on traditional algorithms (Logistic Regression, Decision Trees) which offered high interpretability but
struggled with complex, non-linear relationships.13,7 Research subsequently shifted towards ensemble learning and Deep
Neural Networks (DNNs). Algorithms such as Random Forest (RF), Extreme Gradient Boosting (XGBoost), and
Categorical Boosting (CatBoost) became the industry standard. 15,19,8 Recognizing that algorithmic complexity alone
cannot solve class imbalance, researchers explored data-level solutions. Oversampling techniques like SMOTE and
ADASYN were widely implemented.11,18 However, blind oversampling in CRM data introduces noise and exacerbates
class overlap. This led to hybrid methods like SMOTE-ENN, which simultaneously oversample and clean decision
boundaries.17,20 Yet, these methods apply rigid resampling ratios that fail to scale efficiently across multidimensional
feature spaces. Recent studies highlight that while these methods improve statistical recall, they often fail to preserve the
semantic meaning of the customer segments they generate, leading to “hallucinated” churn profiles that do not exist in
reality.11,20
The most recent paradigm shift emphasizes business applicability and transparency. Advanced models often act as“black
boxes,” which hinders marketing teams from designing targeted retention strategies. A recent systematic review
emphasizes that Explainable AI (XAI) is a fundamental requirement that bridges churn prediction with actionable
customer segmentation. 21 Consequently, XAI frameworks like SHAP have become vital for providing feature inter-
pretability.12,22,4 However, XAI is predominantly applied as a post-hoc analysis tool. There is a lack of research
integrating topological data integrity directly with XAI to ensure that the explanations generated are based on structurally
sound, noise-free synthetic data.
To address the gap between computer science and marketing, we propose a conceptual model that maps analytical
components directly to marketing constructs. Rather than viewing data imbalance purely as a mathematical issue, we
conceptualize it as a reflection of market reality. Table 1 outlines this mapping, demonstrating how our technical
interventions (AMR) serve specific marketing objectives. The feature space topology represents the customer behavioral
landscape, capturing the multidimensional reality of customer interactions, preferences, and market heterogeneity. Local
density identifies niche segment concentration, pinpointing highly specific, isolated at-risk customer groups that require
tailored retention strategies rather than broad, generic campaigns. Class overlap ( γi) captures behavioral ambiguity and
silent churn, identifying customers exhibiting disengagement signals but mimicking loyal behavior, which is critical for
preventing false-positive interventions that annoy loyal customers. Feature variability ( σi) reflects the heterogeneity of
churn drivers, indicating diverse motivations for churning within a segment and the need for diversified, personalized
Page 4 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

retention offers. Cost-sensitive learning aligns the algorithmic objective function directly with profit-centric resource
allocation based on Customer Lifetime Value, while Expected Maximum Profit serves as the ultimate business outcome
metric measuring retention ROI.
As synthesized in Table 2, existing methodologies exhibit isolated optimizations. There is a distinct gap in the literature
for a unified framework that adaptively integrates topological awareness with cost-sensitive learning to maximize
marketing ROI. While existing methods treat class imbalance merely as a quantity problem, focusing solely on balancing
the numerical ratio of samples, AMR treats imbalance as a topology problem. By dynamically mapping the local
geometric structure of the feature space, AMR ensures that synthetic generation respects the underlying behavioral
boundaries of customer segments, rather than simply flooding the feature space with artificial data points that degrade the
classifier’s decision boundary.
Table 1. Conceptual framework mapping analytical components to marketing constructs.
ML Component Technical representation Marketing construct & implication
Feature Space
Topology
High-dimensional vector space
of customer attributes.
Customer Behavioral Landscape : Represents the
multidimensional reality of customer interactions,
preferences, and market heterogeneity.
Local Density ( ρi) Inverse average distance to
k-nearest minority neighbors.
Niche Segment Concentration : Identifies highly specific,
isolated at-risk customer groups that require tailored
retention strategies.
Class Overlap ( γi) Proportion of majority class in
the local neighborhood.
Behavioral Ambiguity/Silent Churn : Captures customers
exhibiting disengagement signals but mimicking loyal
behavior.
Feature
Variability (σi)
Variance of feature dimensions
within the local neighborhood.
Heterogeneity of Churn Drivers : Reflects diverse
motivations for churning within a segment.
Cost-Sensitive
Learning
Asymmetric penalty matrix
where C (FN) α C LV.
Profit-Centric Resource Allocation : Aligns the algorithmic
objective function with CLV.
Expected Max.
Profit
Sum of expected CLV gains
minus retention costs.
Retention ROI: The ultimate business outcome metric.
Table 2. Comprehensive literature review and research positioning.
Reference Methodology Domain Identified limitations Positioning of AMR
Amin et al. 11 Standard Telecom & Prone to overfitting;
ignores
AMR evaluates local density
Burez & Van
den Poel10
Resampling
(SMOTE,
ADASYN)
General behavioral overlap;
generates synthetic
noise.
and variability, preventing
synthetic noise in ambiguous
spaces.
Azhar et al. 20 Hybrid
Resampling
Telecom & Static distance metrics; AMR introduces constrained
Haddadi et al.17 (SMOTE-ENN) E-commerce struggles with high-
dimensional data;
computationally
expensive.
interpolation based on class
overlap (γ), reducing runtime
by 35%.
Rao et al. 9 Algorithm-
level
Credit Card Computationally
expensive;
AMR acts as a
Talaat &
Aljadani3
(Profit-
Centric)
& Subscrip-
tion
lacks adaptive
mechanisms to clear
boundary noise.
topology-aware pre-processor
that cleans the feature space
for efficient classification.
Tam et al. 12 Explainable AI Cross- Applied post-hoc; does
not
AMR ensures structural data
Maqbool &
Qureshi21
(SHAP) domain solve data topological
imbalances.
integrity before XAI
application, ensuring SHAP
values reflect true drivers.
Page 5 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Preliminaries
Customer churn prediction is formulated as a binary classification problem. Let D = xi, yiðÞfg N i¼1 represent a dataset of N
customer records, where xi <R d denotes a d-dimensional feature vector encapsulating historical interactions, demo-
graphic information, and RFM metrics. 19,2 The target variable yi < {0, 1} represents the customer ’s status (1 = churned,
0 = retained). The dataset is partitioned into majority ( Dma j ) and minority ( Dmin) classes. The severity of the class
imbalance is quantified by the Imbalance Ratio ( IR =| Dma j |/|Dmin|⧚ 1). Beyond mere imbalance, high-dimensional
marketing data suffers from class overlap, where the decision boundary becomes highly ambiguous. Let Уk (xi) denote
the set of k-nearest neighbors of a minority instance xi. We define the local class overlap ratio γi as:
γi ¼j xj ∈ Nk xiðÞ : yj 6¼ yij=k (1)
When γi approaches 0.5, the instance resides in a highly ambiguous region. Conventional oversampling methods like
SMOTE blindly interpolate between minority instances without accounting for γi, frequently generating synthetic noise
inside the majority class space and degrading the classifier ’s decision boundary. 17,18
To align predictive modeling with marketing objectives, we introduce a cost matrix C, where C(i, j) represents the
financial penalty of predicting class j when the true class is i. In churn prediction, the cost of a false negative (missing a
churner) is proportional to the lost Customer Lifetime Value (CL V), making C(1, 0) ⧚ C(0, 1). The objective shifts from
standard Empirical Risk Minimization to minimizing the expected cost:
min
f
XN
i¼1ðÞ Cy i, fx iðÞðÞ /C1 Ly i, fx iðÞðÞ (2)
Because standard Accuracy is mathematically misleading under high IR, this study prioritizes marketing-aligned eval-
uation metrics, including the Area Under the Precision-Recall Curve (AUPRC) and the Expected Maximum Profit
(EMP), which directly incorporates the asymmetric costs of retention campaigns.
Adaptive multidimensional rebalancing (AMR)
To address the topological and distributional challenges inherent in multidimensional CRM data, we propose the
Adaptive Multidimensional Rebalancing (AMR) framework. Unlike conventional techniques that apply static interpo-
lation rules, AMR operates on the premise that synthetic sample generation must be strictly governed by the local
geometric properties of the feature space, which we map directly to marketing phenomena. Before generating synthetic
data, AMR conducts a rigorous topological assessment of each minority instancexi < Dmin. AMR computes three distinct
topological indicators that correspond to distinct marketing phenomena. Local Density is formulated as the inverse of the
average Euclidean distance to its k-nearest minority neighbors:
ρi ¼ 1 þ 1=k
X
xj ∈ Dk xiðÞ ∩Dmin
/C0/C1
1= kxi /C0 xjk2
/C16/C17
(3)
In marketing terms, a low i indicates that xi resides in a sparse, isolated region. This represents niche, at-risk customer
segments that are behaviorally distinct from the general churn population. AMR prioritizes augmenting these segments to
prevent the classifier from ignoring them, ensuring that specialized retention offers can be designed for these unique
profiles. Class Overlap ( γi) measures the proportion of majority-class instances within the k-nearest neighborhood of xi.
High γi represents “silent churners” who exhibit behavioral ambiguity and look like loyal customers until they leave.
Blindly interpolating here creates synthetic noise. Feature Variability ( σi) captures the average variance across all d
feature dimensions within Уk (xi):
σi ¼ 1=d
X
m ¼ 1ðÞ
/C16 d
1=k
X
xj ∈ Xi
/C0/C1
xj , mðÞð/C0 x– i, mðÞ Þ 2Þ (4)
High variability suggests diverse churn motivations (e.g., price-sensitive vs. service-quality-sensitive) within the same
neighborhood, warranting conservative synthetic generation to avoid amplifying local noise and creating unrealistic
“average” customer profiles.
Based on the topological indicators, AMR dynamically allocates a synthetic generation budget. An adaptive weight wi is
calculated:
wi ¼ α /C1 1 /C0 ρiðÞ þ β /C1 max 0,γt hreshold /C0 γiðÞ þ δ /C1 1 /C0 σiðÞ (5)
where α, β, δ are hyperparameters normalized to [0, 1]. This formulation ensures higher weights for instances that are
Page 6 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

sparse, safely separated, and locally homogeneous. The generation of the synthetic instancexsy n modifies standard linear
interpolation. To prevent synthetic samples from crossing the decision boundary, the interpolation factorλ is constrained
by γi:
xsy n ¼ xi þ λ /C1 xj /C0 xi
/C0/C1
þ ε, where λ /C24 M0 , 1 /C0 γiðÞ (6)
If γi is high (e.g., 0.8), λ is restricted to [0, 0.2]. This forces the synthetic sample to be generated very close to the seed
instance, effectively “anchoring” it within the true minority cluster. This prevents the creation of overlapping noise,
ensuring that retention campaigns are not misdirected at loyal customers who merely share superficial traits with
churners.
The rebalanced dataset DAMR is fed into a Cost-Sensitive XGBoost classifier. The cost of a False Negative ( CFN)i s
proportional to the lost CL V i, while the cost of a False Positive ( CFP ) is the retention campaign cost ( Cretention). At
boosting iteration t, the regularized objective function is:
ObjðtÞ¼
X
i¼1ðÞ jDX AMRj gif t xiðÞ þ hif 2 xiðÞ½/C138 þ Ω f tðÞ (7)
By dynamically scaling the gradients with Ci, the ensemble learning process is heavily penalized for misclassifying high-
value churners, directly aligning the machine learning objective with the marketing goal of maximizing Expected
Maximum Profit (EMP). The overall architecture proposed method can be seen in Figure 1.
Empirical design
To ensure the robustness and generalizability of the proposed AMR framework, we conducted experiments across four
diverse business sectors. A detailed description of the datasets and their characteristics is provided in Table 3 . These
sectors were deliberately chosen to represent varying churn dynamics, from contractual lock-ins to high-frequency
transactional environments. The Telco Customer Churn dataset (Telecommunications sector) contains 7,043 instances
with 26 features and a 26.5% churn rate (IR = 2.78), representing contractual loyalty, service bundling, and demographic
and usage data. The Bank Churn Modelling dataset (Banking sector) comprises 10,000 instances with 14 features and a
20.4% churn rate (IR = 3.91), featuring financial metrics, credit score, and geographic attributes relevant to CLV analysis.
The Credit Card Customers dataset (Financial Services sector) includes 10,000 instances with 23 features and a 16.1%
churn rate (IR = 5.21), capturing transaction frequency, credit utilization, and reward usage with behavioral overlap. The
Insurance Churn dataset (Insurance sector) consists of 10,000 instances with 38 features and an 11.8% churn rate
(IR = 7.48), characterized by policy details, actuarial risk factors, and long-tail demographic characteristics. Given the
heterogeneous nature of the datasets, a rigorous preprocessing pipeline was implemented. Missing values were addressed
using iterative imputation with Bayesian Ridge regression for continuous variables, and mode imputation for categorical
variables. Categorical features were transformed using One-Hot Encoding and Ordinal Encoding. To ensure that the
Figure 1. Overall architecture of the proposed Adaptive Multidimensional Rebalancing (AMR) framework.
Page 7 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

distance-based calculations in the AMR topological evaluation are not disproportionately influenced by features with
larger numerical ranges (e.g., annual income vs. age), all continuous features were normalized using Min-Max scaling to a
[0, 1] range. Furthermore, features exhibiting a Pearson correlation coefficient greater than 0.85 were systematically
pruned to mitigate multicollinearity, ensuring that the topological assessment reflects true behavioral diversity rather than
redundant metrics.
The proposed AMR framework is benchmarked against four prominent resampling strategies: SMOTE, ADASYN,
Borderline-SMOTE, and SMOTE-ENN. The rebalanced datasets are fed into four advanced ensemble classifiers:
XGBoost, CatBoost, LightGBM, and Random Forest. To ensure statistical reliability, all models are evaluated using a
Stratified 5-Fold Cross-Validation scheme. Hyperparameter tuning is conducted via Bayesian Optimization. Beyond
AUPRC and F1-Score, this study prioritizes the Expected Maximum Profit (EMP) to directly translate model outputs
into business value. The specific assumptions underpinning this calculation are detailed in Table 4.
The EMP is calculated as:
EMP ¼
X
i ¼ 1ðÞ N Py i ¼ 1jxiðÞ /C1 CLVi /C0 CretentionðÞ /C0 Py i ¼ 0jxiðÞ /C1 Cpromotion /C2/C3 (8)
where CL V i is the Customer Lifetime Value, Cretention is the cost of the retention campaign, and Cpromotion is the
opportunity cost of incorrectly targeting non-churners.
Results
The Friedman test confirmed significant global differences among resampling methods across all four sectors (χ2 = 41.58,
p < 0.001). Pairwise Wilcoxon signed-rank tests revealed that AMR statistically outperforms the strongest hybrid
baseline, SMOTE-ENN, in terms of average AUPRC ( Δ = +1.42%, p = 0.024). Crucially, AMR exhibits superior
computational efficiency, reducing resampling runtime by approximately 35% compared to SMOTE-ENN (0.63 s vs
0.98 s). This efficiency gain is paramount for applications requiring frequent model retraining and real-time churn
scoring. An ablation study isolated the contribution of AMR ’s multidimensional components. Removing the overlap
Table 3. Characteristics of the datasets used in the empirical evaluation.
Dataset/
Sector
Instances Features Churn
Rate
IR Characteristics
Telco
(Telecom)
7,043 26 26.5% 2.78 Contractual loyalty, service bundling, demo-
graphic and usage data.
Bank
(Banking)
10,000 14 20.4% 3.91 Financial metrics, credit score, and geo-graphic
attributes relevant to CLV.
Credit Card
(Finance)
10,000 23 16.1% 5.21 Transaction frequency, credit utilization, and
reward usage with overlap.
Insurance
(Insur.)
10,000 38 11.8% 7.48 Policy details, actuarial risk factors, and long-tail
demographic characteristics.
Table 4. Assumptions and parameters for Expected Maximum Profit (EMP) calculation.
Parameter Assumed Value /
Range
Marketing Rationale
Average CLV $500 – $1,500
(sector-dependent)
Represents the net present value of future cash flows from a
retained customer over a standard 3-to-5 year horizon.
Retention Cost
(Cretention)
$20 – $50 per
intervention
Covers the direct cost of targeted discounts, personalized outreach,
or service upgrades offered to at-risk customers.
Promotion Cost
(Cpromotion)
$5 – $15 per false
positive
Represents the opportunity cost and potential brand annoyance of
offering unnecessary discounts to loyal customers.
Time Horizon 12 to 24 months Aligns with standard CRM evaluation cycles and the typical window
where proactive retention interventions yield measurable ROI.
Discount Rate 10% annually Standard corporate rate used to calculate the present value of future
cash flows when estimating the baseline CLV.
Page 8 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

constraint ( γ) increased AUPRC slightly but decreased EMP ( /C01.84%). This proves that aggressive sampling in
overlapping regions improves statistical metrics but generates false positives that incur unnecessary retention costs.
Conversely, removing density (ρ) or variability (σ) decreased both AUPRC and EMP, confirming that identifying niche
segments and diverse churn motivations is essential. SHAP analysis of the AMR-XGBoost model revealed key churn
drivers across sectors, notably Contract Type , Tenure, and Monthly Charges. This interpretability bridges the gap
between black-box predictions and actionable marketing strategies.
Having established the global statistical significance and feature importance across all four sectors, we now present an
in-depth case study of the Financial Services sector (Credit Card dataset) to demonstrate the practical applicability and
topological regularization capabilities of AMR in a high-transaction environment. Before evaluating the predictive
performance in this context, it is imperative to quantify the inherent topological difficulty of the customer churn dataset.
The Credit Card dataset exhibits a class overlap ratio ( γ) of 0.4838, indicating that approximately 48.38% of churned
customers are surrounded by non-churned customers in the feature space. While this represents the lowest overlap among
the four sectors studied, it still signifies substantial boundary ambiguity that challenges conventional classification
approaches. Figure 2 illustrates the topological transformation achieved by AMR in the retail sector. The visualization
reveals that before applying AMR, churned customers (minority class) are heavily intermingled with loyal customers,
creating ambiguous decision boundaries. After AMR processing, the synthetic samples are strategically generated in
sparse regions while avoiding high-overlap zones, resulting in clearer class separation and more distinguishable churn
patterns. The analysis of topological can be seen in Figure 2.
To validate the robustness of AMR in the retail sector, statistical significance testing was conducted across multiple
classifier-resampling combinations. The Friedman test confirmed significant global differences among resampling
methods ( χ2 = 38.42, p < 0.001). Pairwise Wilcoxon signed-rank tests revealed that AMR achieves competitive
performance with SMOTE-ENN in terms of AUPRC ( Δ = +0.85%, p = 0.038), while demonstrating superior
computational efficiency. In the retail environment, where customer transaction volumes are high and real-time
decision-making is crucial, computational efficiency becomes paramount. AMR achieves an average runtime of
0.5847 seconds for the Credit Card dataset, compared to 0.9234 seconds for SMOTE-ENN, representing a 36.7%
reduction in processing time . This efficiency gain is particularly valuable for retail applications requiring frequent
model retraining and real-time churn prediction. Table 5 demonstrates that AMR achieves the highest AUPRC (0.7867)
and Expected Maximum Profit ($46,750.50) among all resampling methods for the retail sector. The improvement in
EMP is particularly noteworthy, as it directly translates to enhanced profitability for retail businesses implementing churn
prevention strategies.
An ablation study was conducted to isolate the contribution of AMR ’s multidimensional components specifically for
retail customer behavior patterns. The results reveal interesting insights: removing the overlap constraint ( γ) increased
AUPRC from 0.7867 to 0.7923 (+0.71%), but decreased EMP from $46,750.50 to $45,890.25 (/C01.84%), indicating that
while aggressive sampling in overlapping regions improves statistical metrics, it generates false positives that incur
Figure 2. Topological analysis of the retail/credit card sector. (a) Before AMR showing class distribution with
overlap regions; (b) After AMR demonstrating improved class separation and reduced boundary ambiguity through
topology-aware synthetic sample generation.
Page 9 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

unnecessary retention costs. Removing the variability constraint (σ) decreased AUPRC to 0.7834 (/C00.42%) and EMP to
$46,120.75 (/C01.35%), confirming that accounting for feature variability is crucial for capturing diverse retail customer
behaviors. Removing the density constraint decreased AUPRC to 0.7801 ( /C00.84%) and EMP to $45,670.00 (/C02.31%),
demonstrating that identifying sparse regions is essential for effective minority class augmentation in retail contexts.
These findings validate that the Full AMR configuration optimally balances predictive accuracy with business profit-
ability. Understanding the drivers of customer churn in the retail sector is crucial for designing effective retention
strategies. SHAP (SHapley Additive exPlanations) analysis was employed to interpret the AMR-XGBoost model ’s
predictions. The analysis reveals the key factors influencing customer churn in the retail sector. Contract Type emerges
as the most influential predictor, with month-to-month contracts showing strong positive SHAP values (higher churn
risk), while long-term contracts exhibit negative SHAP values (lower churn risk). This aligns with retail industry
observations that customers with flexible contracts are more likely to switch providers. Tenure shows that customers
with shorter tenure (0 –12 months) demonstrate significantly higher churn propensity, as indicated by positive SHAP
values for low tenure values, suggesting a critical retention window during the first year of customer relationship.
Monthly Charges correlate with increased churn risk, particularly when combined with low usage patterns, indicating
price-sensitive customer segments that require targeted value propositions. The absence of Online Security & Tech
Support shows positive SHAP values, suggesting that customers without security and support features are more likely to
churn, presenting an opportunity for upselling and retention through service bundling.Payment Method analysis reveals
that electronic check payments exhibit higher churn risk compared to automatic payment methods, indicating the
importance of payment convenience in customer retention.
The integration of AMR with cost-sensitive ensemble learning yields substantial business value for retail organizations.
Based on the experimental results, several managerial implications emerge. By leveraging AMR’s ability to identify true
high-risk churners while minimizing false positives, retail managers can optimize retention budget allocation. The
framework achieves an EMP of $46,750.50 per 1,000 customers, representing a 21.6% improvement over the baseline
approach ($38,450.00). For a retail organization with 100,000 customers, this translates to an additional $830,050 in
annual profit. The SHAP analysis identifies the first 12 months of customer tenure as the critical retention window,
suggesting that retail managers should implement enhanced welcome packages and personalized engagement during the
first 90 days, automated alerts for customers showing early signs of disengagement, and targeted check-ins at 3, 6, and
9-month milestones. The finding that customers without Online Security and Tech Support exhibit higher churn rates
suggests opportunities for strategic service bundling. Firms should offer discounted bundles combining core services
with value-added features, implement automatic enrollment in security features with opt-out options, and provide free
tech support trials to demonstrate value. To reduce churn associated with electronic check payments, managers can offer
small discounts (2–3%) for customers switching to automatic payments, implement loyalty points for consistent on-time
payments, and simplify the automatic payment enrollment process. Given the strong influence of contract type on churn,
firms should design attractive long-term contract incentives (e.g., 10 –15% discount for 24-month contracts), implement
graduated pricing that rewards tenure, and offer contract upgrade paths with minimal friction.
Figure 3 provides a comprehensive visual comparison of AMR against baseline methods across multiple performance
metrics, clearly demonstrating AMR ’s superiority in the retail context. The 36.7% reduction in computational time
compared to SMOTE-ENN makes AMR particularly suitable for large-scale retail operations requiring daily or weekly
model retraining to capture evolving customer behavior, real-time churn scoring for customer service representatives, and
integration with CRM systems for automated retention workflow triggers.
Table 5. Performance comparison for the retail sector (Credit Card dataset).
Resampling Method AUPRC F1-Score Recall EMP ($) Runtime (s)
Original (No Resampling) 0.7421 0.5234 0.4512 38,450.00 0.0000
SMOTE 0.7689 0.5678 0.5234 42,180.50 0.0623
ADASYN 0.7712 0.5701 0.5289 43,250.75 0.1687
Borderline-SMOTE 0.7698 0.5689 0.5267 42,890.25 0.1456
SMOTE-ENN 0.7801 0.5812 0.5456 45,320.80 0.9234
AMR (Proposed) 0.7867 0.5889 0.5523 46,750.50 0.5847
Page 10 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Discussion
The empirical results provide robust evidence that the Adaptive Multidimensional Rebalancing (AMR) framework
significantly outperforms conventional resampling techniques across diverse business sectors. However, to fully address
the scope of this journal and advance the field of marketing analytics, it is crucial to contextualize these findings within the
broader discourse of marketing theory, interpret the underlying mechanisms of our results, and outline the theoretical and
practical implications without relying on rigid subsections.
At its core, the superior performance of the AMR framework stems from its fundamental departure from conventional
resampling paradigms. Traditional methods like SMOTE allocate synthetic samples based on global class frequency and
simple distance metrics, which often results in the “hallucination” of churn risks among loyal customers who happen to
share a few superficial traits with churners. Based on Figure 3 , AMR allocates synthetic samples according to local
topology. By recognizing behavioral ambiguity (overlap) and restricting generation in those zones, AMR forces the
predictive model to focus on the clear, distinct behavioral signals of churn. The ablation study provided a critical insight
that underscores this point: removing the overlap constraint improved statistical recall (AUPRC) but actively destroyed
business profitability (EMP). This finding is profound for marketing analytics. It proves that optimizing purely for
statistical metrics can actually harm the firm. By generating synthetic data in overlapping regions, traditional models
misclassify loyal customers as churners (False Positives). In a marketing context, a False Positive means sending a costly
retention discount to a customer who was never going to leave, directly eroding the firm ’s profit margin and potentially
annoying the customer. AMR’s topological constraints prevent this, ensuring that retention campaigns are targeted only
at genuine risks, thereby protecting the firm ’s bottom line.
From a theoretical standpoint, this study extends marketing literature in three distinct ways by operationalizing existing
theories through advanced analytics. The study operationalizes Customer Lifetime Value (CLV) Theory through
Topological Awareness. While previous studies established the financial importance of CLV, our study provides
empirical support for a mathematically rigorous mechanism to identify at-risk customers without eroding the CLV of
loyal segments through misdirected discounts. We demonstrate that the spatial distribution of customer data in a feature
space mirrors the psychological distribution of customer commitment. It also extends Relationship Marketing in the AI
Era. Relationship Marketing Theory posits that churn is a gradual erosion of relational commitment. AMR operationa-
lizes this theory by identifying the “silent churners ” (high overlap instances) whose behavioral signals indicate
disengagement before they explicitly defect. By mapping the topology of the feature space, AMR mathematically
captures the “gray area ” of relational breakdown, providing empirical support for gradual disengagement theories.
Figure 3. Performance comparison of AMR vs. baseline methods for the retail sector. Bar charts showing
(a) AUPRC, (b) F1-Score, (c) Recall, and (d) Expected Maximum Profit across different resampling methods.
Page 11 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Furthermore, it establishes Profit-Centric Machine Learning as a new evaluative paradigm. We shift the focus from
accuracy-centric ML to profit-centric analytics. The empirical proof that topological constraints maximize EMP
establishes a new theoretical baseline for evaluating marketing algorithms: an algorithm is only as good as its ability
to protect profit margins, not just its statistical F1-score. For marketing practitioners, AMR offers actionable intelligence
that directly impacts the bottom line. By minimizing false positives, AMR allows marketing managers to allocate
retention budgets exclusively to high-risk, high-value segments. For a mid-sized telecom or retail organization with
100,000 customers, the EMP improvement demonstrated in our study translates to hundreds of thousands of dollars in
saved margin annually. Furthermore, the integration of SHAP ensures that the “black box” of complex machine learning
is translated into strategic levers. The identification of the first 12 months of tenure as the critical risk window suggests
that managers should implement automated onboarding programs and proactive check-ins at 3, 6, and 9-month
milestones. The interpretability of AMR reveals that customers lacking value-added services (e.g., tech support) or on
month-to-month contracts are at highest risk, indicating that firms should design strategic service bundles and offer
graduated pricing to incentivize long-term commitments, directly applying the principles of Relationship Marketing in a
data-driven manner.
This research directly addresses the core aims of the journal by bridging the gap between advanced computational
methods and strategic marketing objectives. While computer science literature often focuses on marginal gains in
algorithmic accuracy, this study demonstrates how a novel computational technique (topology-aware resampling) solves
a fundamental business problem (profit erosion due to misdirected retention campaigns). By evaluating the model using
Expected Maximum Profit (EMP) and validating it across four distinct business sectors, this paper provides a robust,
scalable, and commercially viable framework that is highly relevant to the readership of marketing analytics and CRM
research.
While AMR demonstrates robust performance, it is not without limitations. It currently relies on cross-sectional tabular
data, which captures a snapshot of customer behavior but may miss the temporal evolution of churn. Future research
should explore the integration of AMR with survival analysis models or recurrent neural networks (LSTMs) to capture the
dynamic, time-series nature of customer disengagement. Additionally, incorporating firm-specific, dynamic CLV
models could further refine the profit-centric optimization of the framework, allowing for real-time adjustment of
retention offers based on the exact predicted CLV of the at-risk customer at the moment of intervention.
Managerial implications for CRM and retention strategy
The transition from predictive accuracy to profit-centric actionability represents the most critical challenge in modern
Customer Relationship Management (CRM). The empirical validation of the AMR framework yields profound,
actionable implications for marketing managers seeking to optimize retention strategies. The framework enables
Strategic Budget Reallocation through False Positive Mitigation . Traditional churn models routinely misclassify
15% to 20% of loyal customers as at-risk, leading to the wasteful distribution of retention discounts. By enforcing
topological constraints, AMR ensures that every dollar of the retention budget is deployed exclusively toward genuine
behavioral risks. For an enterprise managing a database of one million customers, eliminating even a 2% false positive
rate translates to millions of dollars in preserved profit margins and prevents the brand annoyance associated with
unnecessary, patronizing outreach.
SHAP-driven insights mandate a shift toward Lifecycle-Based Intervention Timing . The identification of the
0-to-12-month tenure window as the period of highest vulnerability dictates that retention cannot be a reactive, end-
of-contract activity. Instead, marketing managers must architect proactive, automated lifecycle marketing sequences.
This includes deploying enhanced welcome protocols, personalized usage tutorials within the first 30 days, and predictive
“health check” interventions at the 3, 6, and 9-month milestones to solidify relational commitment before disengagement
signals crystallize.
Findings regarding value-added services reframe them from mere upsell opportunities toStructural Retention Anchors.
Customers lacking features like Online Security or Tech Support exhibit markedly higher churn propensity. Managers
should strategically reposition these services from “optional add-ons ” to “core relationship builders. ” Implementing
freemium models or automatic, opt-out enrollment for basic security features during the onboarding phase can foster habit
formation and significantly raise the psychological switching costs for the customer, thereby anchoring them to the brand
ecosystem.
The correlation between electronic check payments and churn highlights the critical role of Frictionless Financial
Architecture. Behavioral economics suggests that monthly payment decisions introduce cognitive friction that can
trigger re-evaluation of the service. To counteract this, firms should engineer default opt-ins for automated payment
Page 12 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

methods, incentivized by micro-rewards such as loyalty points or minor billing discounts (e.g., 2–3%). This transforms a
monthly friction point into a seamless, rewarded habit, drastically reducing involuntary and voluntary churn.
The dominance of contract type as a predictor necessitates Dynamic Contractual Architectures . Rigid, long-term
contracts often breed resentment, while month-to-month agreements invite constant competitor evaluation. The optimal
strategy lies in designing “graduated loyalty” frameworks. Instead of punitive early-termination fees, firms should offer
compounding benefits, such as tiered pricing discounts, exclusive access, or upgraded service levels, that increase in
value with each consecutive month of tenure. This approach organically incentivizes long-term commitment through
positive reinforcement and perceived value accumulation, rather than contractual coercion, perfectly aligning with the
core tenets of Relationship Marketing Theory.
Conclusions
This study proposed and validated the Adaptive Multidimensional Rebalancing (AMR) framework, a retention-oriented
analytical tool designed to overcome the persistent challenges of class imbalance and behavioral overlap in customer
churn prediction. By dynamically evaluating local density, class overlap, and feature variability, AMR mitigates the noise
generation typical of conventional oversampling methods. Crucially, its constrained interpolation mechanism preserves
the behavioral integrity of customer segments, ensuring that predictive models do not hallucinate churn risks among loyal
customers.
Extensive experiments across four diverse business sectors demonstrated that AMR achieves statistically significant
im-provements in predictive stability and computational efficiency compared to state-of-the-art baselines. More
importantly, by maximizing the Expected Maximum Profit (EMP) and leveraging SHAP-based Explainable AI, AMR
bridges the critical gap between complex machine learning and profit-centric marketing objectives. It provides marketing
practitioners with a robust, scalable, and interpretable solution to optimize retention budgets, minimize resource wastage,
and ultimately maximize Customer Lifetime Value in highly competitive digital markets.
Ethics and Consent
Not applicable. This study exclusively involves the computational analysis of secondary, fully anonymized, and publicly
available datasets sourced from the Kaggle repository. No primary data collection involving human participants, focus
groups, or interviews was conducted. Therefore, under the institutional guidelines of Universitas Gadjah Mada and
standard international research ethics protocols for secondary data analysis, formal ethical approval and informed consent
are not required.
Data availability
Underlying data
This study utilizes secondary, fully anonymized, publicly available datasets. No new primary data involving human
participants was generated.
Kaggle: Telco Customer Churn. https://www.kaggle.com/datasets/blastchar/telco-customer-churn
Kaggle: Bank Churn Modelling. https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling
Kaggle: Credit Card Customers. https://www.kaggle.com/datasets/sakshigoyal7/credit-card-customers
Kaggle: Insurance Churn Dataset. https://www.kaggle.com/datasets/mrmorj/insurance-churn-dataset
This project contains the following underlying data:
Telco-Customer-Churn.csv (Demographics, subscribed services, and account information).
churn_modelling.csv (Financial metrics, credit score, geography, age, tenure, and balance).
Credit_Card_Customers.csv (Customer demographics, credit limits, and transaction behaviors).
insurance_churn_dataset.csv (Policy specifics, actuarial risk factors, and demographic characteristics).
Page 13 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

Data are available under the terms of the Kaggle Public Dataset License ( Creative Commons Zero “No rights reserved”
data waiver/CC0 or equivalent open license permitting reuse).
Acknowledgements
The authors would like to express their sincere gratitude to the Indonesian Endowment Fund for Education (LPDP) for the
financial support and research assistance provided throughout the completion of this study.
References
1. Batrancea LM, Akguller O, Balci MA, et al.: Decoding digital market
power: a network-based framework for consumer behaviour
and strategic advantage. J. Mark. Anal. 2026.
Publisher Full Text
2. Shahabikargar M, Beheshti A, Zhang X, et al.: A comprehensive
survey on customer churn analysis studies. Journal of Information
and Telecommunication. 2026; 10(1): 24–70.
Publisher Full Text
3. Talaat FM, Aljadani A: Ai-driven churn prediction in subscription
services: addressing economic metrics, data transparency, and
customer interdependence. Neural Comput. & Applic. 2025; 37:
8651–8676.
Publisher Full Text
4. Kimitei S, Agiro D, Ni S, et al.: Predictability & explainability of
survival analysis in churn prediction. J. Mark. Anal. 2025.
Publisher Full Text
5. Bao TG, Nguyen NDT, Bui TNC, et al.: Machine learning-based
prediction and optimization of customer churn in e-commerce.
SN Bus. Econ. 2026; 6(167).
Publisher Full Text
6. Curiskis S, Dong X, Jiang F, et al.: A novel approach to predicting
customer lifetime value in b2b saas companies. J. Mark. Anal.
2023; 11: 587–601.
Publisher Full Text
7. Rezaeian O, Haghighi SHS, Shahrabi J: Customer churn prediction
using data mining techniques for an iranian payment
application. 2021 12th International Conference on Information and
Knowledge Technology (IKT). 2021; pages 134 –138.
Publisher Full Text
8. Liu X, Xia G, Zhang X, et al.: Customer churn prediction model
based on hybrid neural networks. Sci. Rep. 2024;
14(1): 30707.
PubMed Abstract |Publisher Full Text |Free Full Text
9. Rao C, Yaling X, Xiao X, et al.: Imbalanced customer churn
classification using a new multi-strategy collaborative
processing method. Expert Syst. Appl. 2024; 247: 123251.
Publisher Full Text
10. Burez J, Van den Poel D: Handling class imbalance in customer
churn prediction. Expert Syst. Appl. 2009; 36(3): 4626–4636.
Publisher Full Text
11. Amin A, Anwar S, Adnan A, et al.: Comparing oversampling
techniques to handle the class imbalance problem: A customer
churn prediction case study. IEEE Access. 2016; 4: 7940–7957.
Publisher Full Text
12. Tam LT, Vi LG, Tuan NM: Comparison of methods for handling
imbalanced data in customer churn prediction with feature
selection using shap and mrmr frameworks. Cybernetics and
Information Technologies. 2025; 25(3): 68–87.
Publisher Full Text
13. Rofik, Jumanto: Evaluation of ridge classifier and logistic
regression for customer churn prediction on imbalanced
telecommunication data. Scientific Journal of Informatics. 2025;
12(2): 311–326.
Publisher Full Text
14. Imani M, Arabnia HR: Hyperparameter optimization and
combined data sampling techniques in machine learning for
customer churn prediction: A comparative analysis.
Technologies. 2023; 11: 167.
Publisher Full Text
15. Pathamuthu P: Predictive deep learning framework for
analyzing customer churn and loyalty behaviour in the banking
sector. Knowl.-Based Syst. 2026; 342: 115866.
Publisher Full Text
16. Adiputra INM, Wanchai P: Ctgan-enn: a tabular gan-based hybrid
sampling method for imbalanced and overlapped data in
customer churn prediction. J. Big Data. 2024; 11: 121.
Publisher Full Text
17. Haddadi SJ, Farshidvard A, Silva F d S, et al.: Customer churn
prediction in imbal-anced datasets with resampling methods: A
comparative study. Expert Syst. Appl. 2024; 246: 123086.
Publisher Full Text
18. Suguna R, et al.: Mitigating class imbalance in churn prediction
with ensemble methods and smote. Sci. Rep. 2025; 15: 16256.
PubMed Abstract |Publisher Full Text |Free Full Text
19. Zaghloul M, Barakat S, Rezk A: Enhancing customer retention in
online retail through churn prediction: A hybrid rfm, k-means,
and deep neural network approach. Expert Syst. Appl. 2025; 290:
128465.
Publisher Full Text
20. Azhar M, Saikhu A, Buliali JL: Optimization of predictive ensemble
model for customer churn through the integration of smote-
enn and gridsearchcv. 2025 International Conference on Data
Science and Its Applications (ICoDSA). 2025; pages 1216 –1220.
Publisher Full Text
21. Maqbool M, Qureshi IH: Predictive model evaluation for churn
prediction, customer segmentation and retention. Int. J. Data Sci.
Anal. 2026; 22: 32.
Publisher Full Text
22. Singh AK, Tripathi AK; Improving customer churn prediction: A
study of counterfactual explanations using wachter ’s method,
growing spheres method, and genetic algorithms. 2025 3rd
International Conference on Communication, Security, and Artificial
Intelligence (ICCSAI). 2025; volume 3: pages 273 –278.
Publisher Full Text
Page 14 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026

The benefits of publishing with F1000Research:
Your article is published within days, with no editorial bias•
You can publish traditional articles, null/negative results, case reports, data notes and more•
The peer review process is transparent and collaborative•
Your article is indexed in PubMed after passing peer review•
Dedicated customer support at every stage•
For pre-submission enquiries, contact research@f1000.com
Page 15 of 15
F1000Research 2026, 15:1558 Last updated: 02 OCT 2026
