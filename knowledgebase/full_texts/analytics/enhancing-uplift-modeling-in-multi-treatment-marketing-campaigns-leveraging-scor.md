---
title: 'Enhancing Uplift Modeling in Multi-Treatment Marketing Campaigns: Leveraging Score Ranking and
  Calibration Techniques'
url: https://arxiv.org/abs/2408.13628
category: analytics
subcategory: case-study
date: 2024-08
venue: arXiv (Cornell University)
authors:
- Yoon Tae Park
- Ting Xu
- Mohamed Anany
source: arxiv
pdf_url: https://arxiv.org/pdf/2408.13628
pages: 6
chars: 31042
fetched_at: '2026-11-08T12:58:29+00:00'
kb_version: 1
---

# Enhancing Uplift Modeling in Multi-Treatment Marketing Campaigns: Leveraging Score Ranking and Calibration Techniques

arXiv:2408.13628v2  [stat.ML]  27 Aug 2024
Enhancing Upli/f_t Modeling in Multi-Treatment Marketing
Campaigns: Leveraging Score Ranking and Calibration
Techniques
Yoon Tae Park∗
yoon.park@bestbuy.com
Best Buy Co., Inc
USA
Ting Xu∗
ting.xu@bestbuy.com
Best Buy Co., Inc
USA
Mohamed Anany
mohamed.anany@bestbuy.com
Best Buy Co., Inc
USA
ABSTRACT
Uplift modeling is essential for optimizing marketing stra tegies by
selecting individuals likely to respond positively to spec iﬁc mar-
keting campaigns. This importance escalates in multi-trea tment
marketing campaigns, where diverse treatment is available and we
may want to assign the customers to treatment that can make th e
most impact. While there are existing approaches with convenient
frameworks like Causalml, there are potential spaces to enh ance
the eﬀect of uplift modeling in multi treatment cases. This p aper
introduces a novel approach to uplift modeling in multi-tre atment
campaigns, leveraging score ranking and calibration techniques to
improve overall performance of the marketing campaign. We r e-
view existing uplift models, including Meta Learner framew orks
(S, T, X), and their application in real-world scenarios. Ad dition-
ally, we delve into insights from multi-treatment studies t o high-
light the complexities and potential advancements in the ﬁeld. Our
methodology incorporates Meta-Learner calibration and a s coring
rank-based oﬀer selection strategy. Extensive experiment results
with real-world datasets demonstrate the practical beneﬁts and su-
perior performance of our approach. The ﬁndings underscore the
critical role of integrating score ranking and calibrationtechniques
in reﬁning the performance and reliability of uplift predic tions,
thereby advancing predictive modeling in marketing analytics and
providing actionable insights for practitioners seeking t o optimize
their campaign strategies.
CCS CONCEPTS
• Computing methodologies → Machine learning.
KEYWORDS
Causal Inference, Uplift modeling, Multi-treatment, Score ranking,
Calibration
ACM Reference Format:
Yoon Tae Park, Ting Xu, and Mohamed Anany. 2024. Enhancing Uplift Mod-
eling in Multi-Treatment Marketing Campaigns: Leveraging Score Ranking
∗Both authors contributed equally to this research.
Permission to make digital or hard copies of all or part of thi s work for personal or
classroom use is granted without fee provided that copies ar e not made or distributed
for proﬁt or commercial advantage and that copies bear this n otice and the full cita-
tion on the ﬁrst page. Copyrights for components of this work owned by others than
the author(s) must be honored. Abstracting with credit is pe rmitted. To copy other-
wise, or republish, to post on servers or to redistribute to l ists, requires prior speciﬁc
permission and/or a fee. Request permissions from permissi ons@acm.org.
KDD 2024 2nd Workshop, August 26, 2024, Barcelona, Spain
© 2024 Copyright held by the owner/author(s). Publication r ights licensed to ACM.
ACM ISBN 978-1-4503-XXXX-X/18/06
https://doi.org/XXXXXXX.XXXXXXX
and Calibration Techniques. In Proceedings of Causal Inference and Machine
Learning in Practice (KDD 2024 2nd Workshop). ACM, New York, NY, USA,
6 pages. https://doi.org/XXXXXXX.XXXXXXX
1 INTRODUCTION
Marketing campaigns are continuously seeking optimization to iden-
tify the right customers who will be most impacted by speciﬁc in-
terventions. Uplift modeling[4, 5, 13] has emerged as a powe rful
tool to address this need by identifying the causal eﬀect of a cam-
paign on individual outcomes. Speciﬁcally, uplift modeling quanti-
ﬁes this causal eﬀect using the Conditional Average Treatme nt Ef-
fect (CATE), which has proven eﬀective in various scenarios. How-
ever, real-world marketing campaigns can be complex, often in-
volving multiple treatment methods within a single campaig n. In
these multi-treatment marketing campaign scenarios, moredetailed
and sophisticated approaches are required.
Several libraries, such as CausalML[2] or EconML[1], oﬀer c on-
venient ways to apply uplift modeling in multi-treatment ca ses.
However, a question arises: ’Why not use multiple single-treatment
models, applying single treatment modeling for each treatm ent
and then selecting the highest eﬀect treatment for each indi vid-
ual?’ This approach can be particularly useful when there are many
features to consider, allowing for feature selection tailo red to each
treatment. While this method can serve as an alternative to e xist-
ing multi-treatment solutions, it necessitates additional steps, such
as score ranking and calibration techniques, to enhance the relia-
bility of uplift predictions.
In this paper, we introduce a novel approach to optimizing multi-
treatment marketing campaigns based on CausalML. Instead o f
directly applying the multi-treatment logic provided by ex isting
framework, we propose using multiple single-treatment mod els,
augmented by score ranking to directly compare treatment eﬀ ects
on individuals, and calibration techniques to improve the r eliabil-
ity of uplift predictions.
Our main contributions are as follows:
• Applying multiple single-treatment models and selecting the
best treatment for each individual, rather than relying on a
single multi-treatment model
• Implementing a score ranking method to ensure that treat-
ment eﬀects are on the same scale for accurate comparison
• Utilizing calibration techniques to enhance the robustnes s
of uplift models
These contributions aim to advance the precision and reliability
of uplift predictions, thereby providing more actionable i nsights
for optimizing marketing campaign strategies. Through ext ensive

KDD 2024 2nd Workshop, August 26, 2024, Barcelona, Spain Yoon Tae Park, Ting Xu, and Mohamed Anany
experiments with real-world datasets, we demonstrate the p racti-
cal beneﬁts and superior performance of our approach, under scor-
ing the critical role of integrating score ranking and calib ration
techniques in predictive modeling for marketing analytics .
2 RELATED WORK
Uplift modeling in multi-treatment contexts has been appro ached
in various ways.
2.1 Decision tree-based approach
Decision tree-based approaches provide logics in terms of splitting
criteria to eﬀectively handle multi-treatment cases. One s uch ap-
proach deﬁnes the split criteria based on arbitrary diverge nce be-
tween two distributions: (1) all treatments and the control group,
and (2) the diﬀerences between treatments themselves [8]. Another
decision tree-based approach, the Contextual Treatment Se lection
(CTS) algorithm, directly maximizes the expected response from
the decision tree by optimizing the splitting criteria [12] .
2.2 Meta-learner based approach
Extending meta-learners[5] to support multiple treatments has been
proposed by expanding the propensity score model to calculate the
Conditional Average Treatment Eﬀect (CATE) for each treatm ent
group [13]. This approach also introduces a net value optimization
framework by modifying treatment eﬀect. The lift is measure d us-
ing the observed value, the estimated response, and conside ring
the cost function for each treatment.
2.3 Multi-armed bandit approach
Another interesting work utilizes a multi-armed bandit app roach
to deﬁne customer-level treatment eﬀects by measuring the d iﬀer-
ence between receiving treatment 𝑡 and not receiving treatment 𝑡,
where 𝑡 refers to one of the multiple treatments [9]. This method
follows a logic similar to one-vs-all multi-treatment clas siﬁcation.
2.4 Optimization framework
An optimization framework has also been proposed as a direct ion
for improvement. While it primarily relies on single-treatment cases,
a dynamic calibration technique [3] has been introduced. This tech-
nique adjusts the model threshold dynamically and optimize s the
incremental treatment outcome, ensuring compliance with t he re-
quired Return on Investment (ROI) constraints.
3 METHODOLOGY
3.1 Problem Deﬁnition
Our problem focuses on recommending a group of customers who
would beneﬁt most from the marketing campaign. Given a limit ed
budget, the marketing team aims to maximize the campaign’s i m-
pact.
Our uplift modeling framework is based on Rubin’s approach
[7]. We denote 𝑌 as the response ﬂag (or revenue) for customer 𝑖
at treatment 𝑡 (𝑡 = 0 for the control group, 𝑡 = 1 for the treatment
group), 𝑋 as a vector of features, and𝑥𝑖 as the feature value per cus-
tomer [13]. Here, we rank customers by the highest lift, deﬁn ed as
having the highest Conditional Average Treatment Eﬀect (CA TE),
where:
𝜏 (𝑥𝑖 ) = E[𝑌𝑖 (1) − 𝑌𝑖 (0) | 𝑋 = 𝑥𝑖 ] (1)
For the multi-treatment case, we expand this formula as follows:
𝜏𝑡 (𝑥𝑖 ) = E[𝑌𝑖 (𝑡) − 𝑌𝑖 (0) | 𝑋 = 𝑥𝑖 ] (2)
where 𝑡 = 𝑛 (𝑛 > 0) denotes a treatment condition 𝑛, and 𝑡 = 0
denotes the control condition, assuming we have 𝑛 treatments in
the given marketing campaign.
We then compare each treatment eﬀect and select the most ef-
fective treatment for each customer as:
assign treatment
𝑡𝑖
= max
{𝑡𝑖 }
𝜏𝑡𝑖 (𝑥𝑖 ) (3)
Finally, we establish a cutoﬀ point (or threshold) to assign cus-
tomers to treatment groups based on the top percentile, wher e we
can achieve the highest lift.
3.2 Meta-Learner as a baseline
Our baseline approach is mainly focusing meta-learner, as i t has
been constantly developed and now is one of the robust approa ch.
This ranges from simple approach such as S/T learners to more
complex approach such as X learner. Note that we used those learn-
ers from CausalML[2] package for convenience.
3.2.1 S-learner. "Single" estimator learner[2, 5] would be consid-
ered as one of the simplest approach in meta-learner. S-lear ner es-
timates the treatment eﬀect using a single machine learning model
by estimating the average outcome 𝜇 (𝑥) with covariates 𝑋 and an
indicator variable for treatment 𝑇 :
𝜇 (𝑥, 𝑡) = 𝐸 [𝑌 | 𝑋 = 𝑥, 𝑇 = 𝑡] (4)
and deﬁne the CATE estimate as:
ˆ𝜏 (𝑥) = ˆ𝜇 (𝑥, 1) − ˆ𝜇 (𝑥, 0) (5)
3.2.2 T-learner. "Two" estimator learner [2, 5] is probably one of
the well-known approaches in meta-learner. This "Two Model Ap-
proach" takes two steps. First, it estimates the control res ponse
function by a base learner as:
𝜇0 (𝑥) = 𝐸 [𝑌 (0) | 𝑋 = 𝑥] (6)
Second, it estimates the treatment response function as:
𝜇1 (𝑥) = 𝐸 [𝑌 (1) | 𝑋 = 𝑥] (7)
with a potentially diﬀerent base learner.
Finally, it estimates the treatment eﬀect by the diﬀerences be-
tween treatment and control response functions as:
ˆ𝜏 (𝑥) = ˆ𝜇1 (𝑥) − ˆ𝜇0 (𝑥) (8)
3.2.3 X-learner. The X-learner builds on the T-learner but diﬀers
in that it uses the ground truth observations in the training set
in an "X"-like shape [5]. This approach is well-known for usi ng
"pseudo-eﬀects". First, it uses the same treatment and cont rol re-
sponse functions as:
𝜇0 (𝑥) = 𝐸 [𝑌 (0) | 𝑋 = 𝑥] (9)
𝜇1 (𝑥) = 𝐸 [𝑌 (1) | 𝑋 = 𝑥] (10)

Enhancing Upli/f_t Modeling in Multi-Treatment: Score Rankin g and Calibration KDD 2024 2nd Workshop, August 26, 2024, Barc elona, Spain
The treatment eﬀect is then estimated by imputing the user level
treatment eﬀects 𝐷1 𝑖 and 𝐷0 𝑗 for user 𝑖 in the treatment group based
on 𝜇0 (𝑥), and user 𝑗 in the control groups based on 𝜇1 (𝑥):
𝐷1 𝑖 = 𝑌 1 𝑖 − ˆ𝜇0 (𝑋 1 𝑖 ) (11)
𝐷0 𝑗 = ˆ𝜇1 (𝑋 0 𝑗 ) − 𝑌 0 𝑗 (12)
Using the user level treatment eﬀects 𝐷1 𝑖 and 𝐷0 𝑗 , it estimates
𝜏1 (𝑥) = 𝐸 [𝐷1 | 𝑋 = 𝑥] and 𝜏0 (𝑥) = 𝐸 [𝐷0 | 𝑋 = 𝑥]. Finally, CATE
estimate is deﬁned by a weighted average of 𝜏1 (𝑥) and 𝜏0 (𝑥) as:
𝜏 (𝑥) = 𝑔(𝑥)𝜏0 (𝑥) + ( 1 − 𝑔(𝑥))𝜏1 (𝑥) (13)
where 𝑔 ∈ [ 0, 1].
3.2.4 Meta-learners in Multi-Treatment Cases. As a baseline ap-
proach, we follow methodologies for multi-treatment cases pro-
posed and embedded in CausalML [2, 13]. This approach utilizes
propensity scores to estimate the CATE, and handle cost diﬀe r-
ences across treatments by updating the cost function in the treat-
ment eﬀect formula accordingly.
3.3 Calibration with Meta-Learner
A classifer is well-calibrated if the class probabilities a ccurately
represent the true probabilities. For uplift modeling, we e xtend it
to calling the model well calibrated if given diﬀerent prior s, treat-
ments or control, the predicted outcome is close to the real o ut-
come on individual level. In the context of uplift modeling, calibra-
tion ensures that the probability estimates produced by our mod-
els are accurate and reliable, thereby improving decision- making
processes in marketing campaigns. The methodologies behin d cal-
ibration involve adjusting the model outputs to correct any biases
or inaccuracies, making the predicted probabilities more r eﬂective
of true likelihoods.
3.3.1 Calibration Techniques. Isotonic regression is a non-parametric
method that ﬁts a non-decreasing function to the predicted p rob-
abilities. This approach is beneﬁcial when the predicted pr obabil-
ities do not exhibit a monotonic relationship with the true p roba-
bilities, as it ensures a more accurate alignment.
3.3.2 Implementation. Utilizing the CalibratedClassifierCVmod-
ule from sklearn[6], we applied isotonic regression to ensure that
our uplift models produce well-calibrated probability estimates. The
implementation process involves:
• Training uplift models using Meta-Learner frameworks (S-
learner, T-learner, X-learner)[5]
• Applying isotonic regression[10, 11] to the model outputs.
• Evaluating the calibrated models using Area Under the Up-
lift Curve(AUUC)[4, 8], uplift score plotting, and accurac y
on the validation dataset.
Calibration enhances the robustness and reliability of our predic-
tions, ensuring that the uplift scores reﬂect true probabil ities of
treatment eﬀects. This improves the accuracy of targeting and decision-
making in marketing campaigns.
3.3.3 Measuring Calibration. To assess the eﬀectiveness of cali-
bration, we compared uplift modeling with and without calibration
using the AUUC score. The process involved:
• AUUC Score Comparison: The metric is calculated by sort-
ing the individual on their predicted uplift score from high -
est to lowest, divided the sorted group into 100 groups, and
computing the diﬀerence between treatment and control across
these segments. We measured the AUUC for models before
and after applying calibration techniques.
• Uplift Score Distribution: Plot the uplift curve by placing
the cumulative uplift on the y-axis and the proportion of the
population on the x-axis. By observing the distribution of
uplift scores, we compared models before and after applying
calibration techniques.
• Uplift at Diﬀerent Quantiles: Sorting individual based on
their uplift score from highest to lowest. We compared the
conversion rates among the top 10%, 20%, and other quan-
tiles between the calibrated and uncalibrated models.
3.4 Scoring Rank: Oﬀer Selection Strategy
In multi-treatment marketing campaigns, selecting the mos t eﬀec-
tive treatment for each individual is a complex task. To address this,
we propose a scoring methodology which involves standardiz ing
uplift scores to identify the best oﬀer. Furthermore, we con duct a
comparative analysis between this standardization approa ch and
the direct ranking of uplift scores to evaluate the eﬀective ness in
selecting the most suitable treatment.
3.4.1 Ranking the Upli/f_t Score and Comparing Ranks. Calculate up-
lift scores for each treatment using Meta-Learner models. R ank in-
dividuals based on their uplift scores for each treatment an d com-
pare these ranks to identify the treatment with the highest u p-
lift for each individual. Ranking individuals based on thei r uplift
scores helps in identifying the most responsive candidates for each
treatment, thereby optimizing the allocation of marketingresources.
3.4.2 Z-score Standardization of Upli/f_t Scores. Compute the mean
and standard deviation of the uplift scores for each treatment. Trans-
form the uplift scores into Z-scores and compare the Z-scores across
treatments for each individual. Based on the comparison, se lect
the optimal treatment. Standardizing uplift scores using Z -scores
allows for comparisons on a common scale, it can highlight th e
most impact treatments.
After applying either the direct ranking method or Z-score s tan-
dardization, integrate the results to select the optimal treatment for
each individual. We validated the outcomes using cross-val idation
and out-of-sample testing. This approach ensured the robus tness
of the methods and allowed us to determine which technique pe r-
formed better.
4 EXPERIMENT SETUP
The experimental setup involved utilizing vehicle A, and th e cam-
paign was designed as a follow-up to a prior marketing campai gn
conducted in recent year. This section outlines the details of the
campaign, and A/B test experiment setup.
4.1 Campaign Overview
4.1.1 Initial Marketing Campaign:

KDD 2024 2nd Workshop, August 26, 2024, Barcelona, Spain Yoon Tae Park, Ting Xu, and Mohamed Anany
• Objective: The initial campaign targeted customers who
had received a catalog but had not made a purchase since
receiving it.
• Timeframe: The catalog purchase window was in short-
term period. During this observational period, a group of
customers (10% of the total targeted customers) received a
treatment at the beginning and the oﬀer would exipred at
the end of the period.
4.1.2 Follow-Up Campaign:
• Timeframe: The follow-up campaign was conducted within
a brief period following the evaluation of the initial marke t-
ing campaign’s results.
• Total Circulation: A large group of customers were tar-
geted in this campaign, divided into two creative versions:
– Version A: Treatment A was applied, targeting a subset
of the overall targeted customers. This group was equally
divided between those who had and had not received prior
treatment in the initial campaign.
– Version B: Treatment B was a more generic version, tar-
geting a subset the overall targeted customers. This group
included a mix of those who had and had not received
prior treatment.
Note that both versions contained a suﬃcient number of
customers, and balancing criteria were applied to ensure
that both groups are unbiased.
4.2 Uplift Modeling
To eﬀectively target customers for the follow-up campaign, we
leveraged these uplift modeling techniques to identify tho se most
likely to respond to speciﬁc actions. The modeling process i s de-
tailed as follows:
• Data Source: The dataset for model training was derived
from one historical Marketing campaign, which had an iden-
tical setup to the new campaign and its follow-up campaign.
• Feature Selection and Model Training: Features such as
customer demographics, past purchase behavior, and mar-
keting communication history were selected for training the
uplift models. These features were chosen based on their
predictive relevance to customer responses.
4.3 Evaluation Metrics
To measure the performance of our uplift models and the campaign
outcomes, we used several key metrics: Uplift at Diﬀerent Qu an-
tiles, AUUC, and Accuracy.
• Uplift at Diﬀerent Quantiles: Measure the eﬀectiveness
of targeting diﬀerent segments of the customer base.
• Area Under the Uplift Curve (AUUC): Evaluate the over-
all performance of the uplift model.
• Accuracy: Determine the correctness of the predictions.
4.4 Experimental Procedure
• Data Preprocessing: The historical campaign data were
cleaned and preprocessed, including handling missing val-
ues, outliers, and encoding categorical variables. Additi on-
ally, select relevant features using statistical analysis and
predictive relevance.
• Model Training: Uplift models were trained using Meta-
Learner frameworks (S-learner, T-learner, X-learner). Ca li-
bration techniques, isotonic regression was applied to reﬁne
the model outputs.
• Score Ranking and Standardization:Uplift scores for each
treatment were calculated, followed by directly ranking or
standardization using Z-scores for each treatment.
• Treatment Selection: Optimal treatments for each individ-
ual were selected based on either the direct ranking method
or Z-score standardization. Cross-validation and out-of-sample
testing were used to ensure robustness.
• Performance Evaluation: The models’ performances were
evaluated using the speciﬁed metrics (AUUC, Uplift At Quan-
tiles), comparing our approach against baseline models in
sample.
5 RESULTS
The results of our experimental setup demonstrate the eﬀect ive-
ness of the proposed uplift modeling approach, particularl y in the
context of multi-treatment marketing campaigns. Our metho dol-
ogy, which integrates score ranking and calibration techni ques,
showed signiﬁcant improvements in prediction accuracy and over-
all campaign performance.
5.1 Calibration Eﬀectiveness
Calibration techniques, particularly isotonic regression, signiﬁcantly
enhanced the reliability of the predicted probabilities. Figure shows
the calibration tables for the Meta-Learner models before and after
calibration. The calibrated model’s probabilities align more closely
with the true probabilities, demonstrating the eﬀectivene ss of the
calibration process.
5.1.1 AUUC Score Comparison. The Area Under the Uplift Curve
(AUUC) was utilized to evaluate the performance of the uplift mod-
els. We observed that our proposed approach, which includedscore
ranking and calibration, achieved higher AUUC scores compa red
to the baseline models. Table 1 summarizes the AUUC scores fo r
diﬀerent models:
Table 1: AUUC Score Comparison
Model AUUC
(Uncalibrated)
AUUC
(Calibrated)
Diﬀ
(%)
S-Learner 0.40 0.65 63.4
T-Learner 0.92 1.13 22.2
X-Learner 0.92 0.62 -32.6
Random 0.54 0.54 -
Calibration enhanced AUUC scores for the S-learner and T-learner,
ultimately identifying the highest-performing learner. H owever,

Enhancing Upli/f_t Modeling in Multi-Treatment: Score Rankin g and Calibration KDD 2024 2nd Workshop, August 26, 2024, Barc elona, Spain
while the decision to select the calibrated learner remainsunchanged,
the X-learner exhibited a decrease in AUUC score, highlighting the
need to not solely rely on calibration steps and remain open t o fur-
ther studies
5.1.2 Upli/f_t at Diﬀerent /Q_uantiles. We also assessed the eﬀective-
ness of targeting diﬀerent customer segments based on uplift scores.
Table 2 illustrates the lift at diﬀerent quantiles for both c alibrated
and uncalibrated models. The calibrated models consistent ly out-
performed the uncalibrated models across all quantiles, wi th the
most signiﬁcant improvements observed in the top 10% and 20%
segments. Also, note that X Learners underperformed aligning the
performance on AUUC scores. The conversion rate of the rando m
target group was used as the baseline for comparison.
Table 2: Lift Comparison on Top 10% and 20% quantile
Uncalibrated Calibrated Diﬀ(%)
S Learner - Top 10% 0.9 1.3 48.2
S Learner - Top 20% 0.9 1.1 18.6
T Learner - Top 10% 2.0 2.2 6.5
T Learner - Top 20% 1.5 1.6 5.2
X Learner - Top 10% 2.1 2.0 -3.7
X Learner - Top 20% 1.6 1.5 -4.8
Random 1.0 1.0 -
5.2 Scoring Rank and Oﬀer Selection Strategy
Our score ranking strategy, involving both direct ranking a nd Z-
score standardization, was pivotal in selecting the optima l treat-
ment for each individual. Tables 3 and 4 show the distributio n of
selected treatments for a subset of the population, demonst rating
the diversity and precision of our approach.
5.2.1 Direct Ranking. Table 3 presents the baseline approach, where
we rank customers from each treatment by it’s uplift score an d as-
sign customers how has higher ranking between both treatmen ts.
This method shows a 7.5% lift for treatment A. However, for tr eat-
ment B, there is a -0.8% lift, raising questions about the val idity of
comparing treatments directly by uplift score ranking. It i s possi-
ble that the assignment strategy favored treatment A for customers
who showed positive uplift scores for both treatments A and B. We
used the conversion rate of random target group and received no
treatment as baseline.
Table 3: Direct Rank Comparison
Actual A Actual B Actual Ctrl Lift(%)
Oﬀer A 2.06 1.93 1.91 7.5
Oﬀer B 2.90 2.77 2.79 -0.8
Oﬀer Ctrl 1.03 1.01 1.00 -
5.2.2 Z-Score normalization. Table 4 illustrates the results after
applying the Z-score normalization. Here, both treatments show a
positive lift, with treatment A achieving an 8.2% lift and tr eatment
B achieving a 3.2% lift. This approach outperforms the basel ine
method, indicating that Z-score normalization allows for a more
balanced and eﬀective comparison between treatments.
Table 4: Proposed Approach: Z-score Normalization
Actual A Actual B Actual Ctrl Lift(%)
Oﬀer A 2.78 2.56 2.57 8.2
Oﬀer B 2.47 2.43 2.39 3.2
Oﬀer Ctrl 1.04 1.01 1.00 -
The results indicate that our method eﬀectively identiﬁes t he
most responsive individuals for each treatment, leading to more
targeted and eﬃcient marketing interventions. This demons trates
the beneﬁt of using Z-score standardization over direct ranking for
treatment assignment, as it provides a clearer understanding of the
relative performance of each treatment.
Table 5: Online experiment result
Treatment A Control Lift(%)
Oﬀer A Persuadable 1.12 1.00 12.0
In addition to modeling and evaluating the oﬄine experiment
results, we also leveraged uplift modeling techniques to sc ore cus-
tomers and select the optimal oﬀer for them in an online exper i-
ment. We collected the online experiment results by running an
A/B test. For customers predicted to be more responsive to Oﬀ er
A, we provided Treatment A to 2/3 of them, while 1/3 received n o
treatment. We observed a 12% lift in the online experiment, w hich
outperformed the 8.2% lift observed in the oﬄine experiment data
modeling results, as shown in Table 5.
6 CONCLUSION
In this paper, we have presented a novel approach to uplift mo d-
eling in multi-treatment marketing campaigns, discussed t he inte-
gration of score ranking and calibration techniques to enhance pre-
diction accuracy. By using Meta-Learner frameworks with ca libra-
tion and implementing a scoring rank-based oﬀer selection s trat-
egy, we aimed to address the complexities and improve the inc re-
mental eﬀect and reliability of uplift predictions.
Our extensive experiments with real-world datasets showedthat
the proposed methodology had a robust model performance. Th e
ﬁndings underscore the eﬀectiveness of score ranking and ca libra-
tion in reﬁning reliability of uplift predictions. This adv ancement
provides more actionable insights for practitioners seeki ng to op-
timize their campaign strategies.
The key contributions and ﬁndings of our work include:
• The implementation of multiple single-treatment models and
the selection of the best treatment for each individual, en-
hancing the granularity and eﬀectiveness of targeting.

KDD 2024 2nd Workshop, August 26, 2024, Barcelona, Spain Yoon Tae Park, Ting Xu, and Mohamed Anany
• The development of a score ranking method to ensure com-
parability of treatment eﬀects across individuals.
• The application of calibration techniques to improve the ro -
bustness of uplift models, ensuring that predicted probabi l-
ities are accurate and reliable.
While our results are promising, the study does have some lim -
itations, such as comparison of other approaches other than meta-
learners or potential calibration issues.
Future research should explore additional calibration techniques,
applying our methodologies into diﬀerent algorithms, and a ppli-
cations in diﬀerent domains to further validate and enhance our
approach. Addressing these limitations will help in improv ing the
model’s accuracy and applicability.
In conclusion, our work advances the state-of-the-art in pr edic-
tive modeling for marketing analytics, providing a robust f rame-
work for practitioners to optimize multi-treatment campai gns ef-
fectively. We believe these contributions will serve as valuable guide-
lines for further innovations in uplift modeling and its app lica-
tions.
REFERENCES
[1] Keith Battocchi, Eleanor Dillon, Maggie Hei, Greg Lewis , Paul Oka, Miruna
Oprescu, and Vasilis Syrgkanis. 2019. EconML: A Python Pack age for ML-
Based Heterogeneous Treatment Eﬀects Estimation. https:/ /github.com/py-
why/EconML. Version 0.x.
[2] Huigang Chen, Totte Harinen, Jeong-Yoon Lee, Mike Yung, and Zhenyu
Zhao. 2020. CausalML: Python Package for Causal Machine Lea rning.
arXiv:2002.11631 [cs.CY]
[3] Dmitri Goldenberg, Javier Albert, Lucas Bernardi, and P ablo Estevez. 2020. Free
Lunch! Retrospective Uplift Modeling for Dynamic Promotio ns Recommenda-
tion within ROI Constraints. In Fourteenth ACM Conference on Recommender
Systems (RecSys ’20) . ACM. https://doi.org/10.1145/3383313.3412215
[4] Pierre Gutierrez and Jean-Yves Gérardy. 2017. Causal In ference and
Uplift Modelling: A Review of the Literature. In Proceedings of The
3rd International Conference on Predictive Applications an d APIs (Proceed-
ings of Machine Learning Research, Vol. 67) , Claire Hardgrove, Louis
Dorard, Keiran Thompson, and Florian Douetteau (Eds.). PML R, 1–13.
https://proceedings.mlr.press/v67/gutierrez17a.html
[5] Sören R. Künzel, Jasjeet S. Sekhon, Peter J. Bickel, and B in Yu. 2019. Metalearners
for estimating heterogeneous treatment eﬀects using machi ne learning. Pro-
ceedings of the National Academy of Sciences 116, 10 (Feb. 2019), 4156–4165.
https://doi.org/10.1073/pnas.1804597116
[6] F. Pedregosa, G. Varoquaux, A. Gramfort, V. Michel, B. Th irion, O. Grisel, M.
Blondel, P. Prettenhofer, R. Weiss, V. Dubourg, J. Vanderplas, A. Passos, D. Cour-
napeau, M. Brucher, M. Perrot, and E. Duchesnay. 2011. Sciki t-learn: Machine
Learning in Python. Journal of Machine Learning Research 12 (2011), 2825–2830.
[7] D.B. Rubin. 1974. Estimating causal eﬀects of treatment s in randomized and
nonrandomized studies. Journal of Educational Psychology 66, 5 (1974), 688–701.
[8] Piotr Rzepakowski and Szymon Jaroszewicz. 2012. Decisi on trees for uplift mod-
eling with single and multiple treatments. Knowledge and Information Systems
32, 2 (2012), 303–327. https://doi.org/10.1007/s10115-0 11-0434-0
[9] Neela Sawant, Chitti Babu Namballa, Narayanan Sadagopa n, and Hous-
sam Nassif. 2018. Contextual Multi-Armed Bandits for Causa l Marketing.
arXiv:1810.01859
[10] Bianca Zadrozny and Charles Elkan. 2001. Obtaining cal ibrated probability esti-
mates from decision trees and naive Bayesian classiﬁers. In Proceedings of the
Eighteenth International Conference on Machine Learning ( ICML ’01) . Morgan
Kaufmann Publishers Inc., San Francisco, CA, USA, 609–616.
[11] Bianca Zadrozny and Charles Elkan. 2002. Transforming classiﬁer scores into
accurate multiclass probability estimates. In Proceedings of the Eighth ACM
SIGKDD International Conference on Knowledge Discovery an d Data Mining (Ed-
monton, Alberta, Canada) (KDD ’02) . Association for Computing Machinery,
New York, NY, USA, 694–699. https://doi.org/10.1145/7750 47.775151
[12] Yan Zhao, Xiao Fang, and David Simchi-Levi. 2017. Uplif t Modeling with Multi-
ple Treatments and General Response Types. arXiv:1705.084 92
[13] Zhenyu Zhao and Totte Harinen. 2020. Uplift Modeling fo r Multiple Treatments
with Cost Optimization. https://doi.org/10.48550/arXiv .1908.05372
