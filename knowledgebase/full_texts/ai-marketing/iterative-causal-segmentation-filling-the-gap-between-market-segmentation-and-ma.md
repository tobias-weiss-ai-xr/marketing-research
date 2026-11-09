---
title: 'Iterative Causal Segmentation: Filling the Gap between Market Segmentation and Marketing Strategy'
url: https://arxiv.org/abs/2405.14743
category: ai-marketing
subcategory: empirical
date: 2024-05
venue: ''
authors:
- Kaihua Ding
- Jingsong Cui
- Mohammad Soltani
- Jing Jin
source: arxiv
pdf_url: https://arxiv.org/pdf/2405.14743
pages: 13
chars: 29296
fetched_at: '2026-11-08T13:11:08+00:00'
kb_version: 1
---

# Iterative Causal Segmentation: Filling the Gap between Market Segmentation and Marketing Strategy

Iterative Causal Segmentation∗
Filling the Gap between Market Segmentation and Marketing Strategy
Kaihua Ding1, Jingsong Cui1, Mohammad Soltani1, and Jing Jin1
1AZ Brain, AstraZeneca PLC
Abstract
The field of causal Machine Learning (ML) has made significant strides in recent years. Notable
breakthroughs include methods such as meta learners [4] and heterogeneous doubly robust estimators [3]
introduced in the last five years. Despite these advancements, the field still faces challenges, particularly in
managing tightly coupled systems where both the causal treatment variable and a confounding covariate
must serve as key decision-making indicators. This scenario is common in applications of causal ML for
marketing, such as marketing segmentation and incremental marketing uplift. In this work, we present
our formally proven algorithm, iterative causal segmentation, to address this issue.
1 Motivation
The integration of machine learning into market segmentation has significantly transformed the development
of marketing messages and strategies. However, categorizing individuals into rigid market segments such
as ’loyalists’ or ’dabblers’ fails to account for the dynamic nature of consumer circumstances, potentially
leading to ineffective marketing and wasted resources. This underscores the limitations of relying solely on
traditional market segmentation for marketing actions, a challenge initially highlighted by Wendell R. Smith
in the 1950s [8]. Despite its innovative approach, market segmentation’s static methodology struggles to
capture evolving consumer behaviors, risking oversimplification and ineffective strategy development.
The emergence of causal inference in marketing provides a solution by identifying the causative factors
behind consumer behaviors, enabling the development of predictive and effective marketing strategies with
methods like Uplift Trees and Meta Learners [7, 4, 11]. However, these approaches often overlook the
complexity that arises when market segmentation becomes an intertwined part of the promotional market,
acting both as a significant confounder and a desired output for marketing purposes, especially in contexts
like pharmaceutical call planning and broadcasting media. Causality analysis alone cannot address it as
both a confounder and an output.
To tackle these challenges, we propose the iterative causal segmentation algorithm, which merges causal
inference with market segmentation to surmount their individual limitations. This method not only provides
a nuanced understanding of consumer behaviors but also amplifies the effectiveness of marketing efforts across
various segments. Nonetheless, in marketing scenarios where the interdependency between segmentation and
causality analysis poses a distinct challenge, leading to a cyclical problem where each influences the outcome
of the other, our proposed solution aims to harmonize these methodologies. By leveraging their strengths,
we seek to refine marketing strategies effectively.
∗Disclaimer: The opinions expressed in this presentation are those of the presenters and do not necessarily reflect the views
of AstraZeneca. The analyses presented in this presentation are based on Uber’s open-source CausalML GitHub repository
data and do not represent AstraZeneca data.
1
arXiv:2405.14743v1  [cs.LG]  23 May 2024

2 Iterative Causal Segmentation
2.1 Average Treatment Effect (ATE)
A key challenge for marketing professionals concerns generating a sales uplift from promotional campaigns,
quantified by:
Expected uplift gain from applying promotion = E(Y A=1) − E(Y A=0), (1)
where:
• A represents the treatment, i.e., the promotional campaign.
• Y is the outcome, indicating the effect of the campaign.
The difference between these two expected values represents the expected uplift per person due to the
promotion. Equation 1 represents the expected average purchase uplift if the promotion is applied. This
expected uplift is also known as the Average Treatment Effect (ATE) in causality analysis. The Average
Treatment Effect is defined as:
ATE = E(Y A=1) − E(Y A=0) (2)
This formulation allows us to quantitatively assess the overall impact of the treatment across the entire
population. Additionally, recently developed causal machine learning techniques are capable of attributing
uplift gain to individual samples [2, 4] by estimating the conditional average treatment effect.
2.2 Conditional Average Treatment Effect (CATE)
The Conditional Average Treatment Effect, which can also be understood as the expected individual treat-
ment effect (ITE) conditional on covariates X, is defined as:
CATE = E(Y A=1|X) − E(Y A=0|X) (3)
where:
• A represents the treatment, i.e., the promotional campaign.
• Y is the outcome, indicating the effect of the campaign.
• X represents the covariates or features of the individual units that might affect how the treatment
impacts the outcome.
CATE provides a more nuanced understanding of how the effect of the treatment varies across different
segments of the population based on the covariates X. It allows for the estimation of how the treatment
effect differs among individuals or specific groups within the population, enabling targeted interventions.
2.3 Causal Graph
A causal graph, often used in the context of causal inference and statistics, is a graphical representation
that models the causal relationships between variables. It is a type of directed graph where nodes represent
variables (e.g., events, conditions, or quantities), and edges represent causal effects from one variable to
another. This concept is foundational in understanding causal inference, allowing researchers to visually
represent and analyze the cause-and-effect relationships within a system.
We can express the relationship among promotion application A, marketing segmentation S, covariates
Xi, and promotion outcome Y as the following causal graph.
The causal graph provides an illustrative relationship among treatment A, covariates X, and outcome
variables Y [5]. A causal graph is a product of a hypothesis and rationalization, rather than ground truth.
Regardless, the causal graph drawn according to empirical knowledge needs to be verified through sensitivity
2

Figure 1: Potential causal graph, where promotion is A, covariates are Xi, promotion outcome is Y , and
marketing segments S is a confounder.
analysis. Rather than focusing on how to come up with the best causal graph, the goal of drafting a
causal graph should be to guide the collection of covariates and the necessary control variables for covariate
matching. In the authors’ opinion, establishing a causal graph is helpful but not the most critical aspect of
causality analysis. The causal graph should change and needs to change, especially if the causal relationship
contains human perspective or ambiguities. It’s the overall reliability in the sensitivity analysis that truly
matters as the end result.
In addition, the main usage of a causal graph is to assist users in how to control for confounders or
covariates to ensure that the causality analysis is valid, e.g., backdoor and frontdoor path criteria [6]. For
simplicity, we use the disjunctive criterion [9] in this paper and we perform sensitivity analysis to check the
reliability of our causal analysis, which also serves as an assessment for the impact of unobserved confounders
and uncertainty quantification.
2.4 The Iterative Causal Segmentation Algorithm
In this section, we illustrate our proposed algorithm, Iterative Causal Segmentation. The key challenge to
address is the tightly coupled nature between segmentation and causality analysis. Instead of shying away
from the tightly coupled nature of these two computational modules, we propose a joint convergence method
that solves for segmentation and causality analysis simultaneously, as shown in Figure 2.
Figure 2 figuratively describes the joint convergence algorithm’s workflow, explicitly considering the
tightly coupled nature and mutual influence of the two modules. For the purpose of effective uplift behavior
segmentation, the causal machine learning module will generate useful uplift incremental estimation, which
we will feed into the segmentation module to produce segmentation that closely reflects the promotion
uplift effect. Segmentation results will then serve as input in the causal machine learning, and the overall
system is considered converged if the amount of segment movement becomes less than the population size
variance determined by ATE variance estimates. This workflow can be more formally defined as follows in
Algorithm 1.
Algorithm 1 formally describes Figure 2 in a more concise and concrete pseudocode fashion. Observing
Algorithm 1, one might question whether there is any need to go to such great lengths to formulate a new
algorithm to solve the causality behavior segmentation problem in marketing. This is also the question that
the authors are interested in solving first. Are there alternatives to the simpler segmentation algorithm
that serve the same purpose without the need to solve the coupled segmentation and causality system?
We can formally prove that such an alternative segmentation method does not exist. The causality uplift
segmentation analysis is exclusively determined by the iterative causal segmentation algorithms.
We formalize the proof as the following statement of Causal Segmentation Exclusivity. If this theory
holds true, it means our iterative causal segmentation is necessary since segmentation obtained this way is
exclusive to the causality.
3

Figure 2: The diagram description on how to use causal machine learning to guide segmentation efforts. The
goal is to achieve the joint convergence of the causal machine learning module as well as the convergence of
the segmentation module.
Algorithm 1 Causal Machine Learning Driven Segmentation
Require: Matched treatment / control variables A, outcome Y , initial segmentation S, and covariates X
Ensure: Causal Data Assumptions
1: Segment Movement ← initial value
2: ATE Variance ← initial value
3: while Segment Movement > (ATE Variance × Population Size) do
4: ATE ← ComputeATE(A, S, Y, X)
5: ATE Variance ← EvaluateATEV ariance(ATE)
6: CATE ← ComputeCATE(A, S, Y, X)
7: S ← Segmentation(CATE)
8: Segment Movement ← EvaluateSegmentMovement(S)
9: end while
10: return S
Theorem 1 (Causal Segmentation Exclusivity). Let us define the Conditional Average Treatment Effect
(CATE), also known as the Individual Treatment Effect (ITE), as follows:
CATE(X) = E[Y A=1 − Y A=0 | X] (4)
where Y A=1 represents the potential outcome if treated or received campaign promotion,Y A=0 represents
the potential outcome if not treated or not receiving campaign promotion, and X is a vector of individual
characteristics.
Segmentation, in the context of causal machine learning, is the process of partitioning a population
into distinct groups based on their respective CATE estimates. Here, the segmentation function S is
4

exclusively dependent on CAT E(X):
S = f (CATE(X)) (5)
We hypothesize that no other factors other than CATE influence the segmentation, that is, segmen-
tation is a function of CATE alone.
A formal proof through contradiction is detailed below,
Proof of Theorem 1. Assume for contradiction that there exists another driver D which influences the
segmentation such that:
S′ = f (CATE(X), D) (6)
where S′ represents a new segmentation outcome due to the presence of driver D.
If driver D were to affect the segmentation, we would observe a change in the segmentation outcome S
without a corresponding change in the CATE estimates. This would contravene the initial assumption that
segmentation is exclusively driven by CATE.
Since our operational framework stipulates CATE as the sole driver for segmentation, the supposition
of another influencing driver D is invalid. Therefore, changes in segmentation are directly correlated with
changes in the CATE estimates, thus affirming that the segmentation is indeed a causal behavior segmenta-
tion when CATE is the exclusive driver. ■
The Proof 2.4 formally proves that the iterative causal segmentation is a necessary system to address
when the tightly coupled nature between causality and segmentation exists. The significance of this proof
lies in its affirmation for the development of such algorithms. Now that we have justified the legitimacy of
developing this new algorithm, Algorithm 1, we will evaluate its performance in the next section.
3 Results and Discussion
3.1 Data Sources Disclaimer and Discussion
We examine the performance of Algorithm 1 by applying it to open-source data from the Uber CausalML
package [1]. We want to emphasize that all causal machine learning algorithms derive their origin from
causality analysis. As a result, all the data assumptions required for performing causality analysis need to
be true to ensure the comprehensiveness and validity of the analysis, as outlined in Table 1.
Table 1: Causal Data Assumptions. In the table below, subscript indices denote sample indices, and super-
script indicates the treatment/control variable.
Assumption Expression
SUTV A Each unit sample i’s potential outcomes Y A i are un-
affected by the treatment assignmentAj of any other
unit j, where A = 1 indicates treatment is assigned
and A = 0 indicates control.
Ignorability Y A=0 i , YA=1 i ⊥ Ai|Xi for all units i, where Ai is the
treatment assignment and Xi are covariates.
Positivity P (Ai = a|Xi = x) > 0 for all levels of treatment a
and covariates x.
Consistency If Ai = a, then the observed outcome Yi is equal to
the potential outcome Y A=a i .
The SUTV A assumption concerns the principle that the treatment received by one unit does not affect
the outcomes of any other unit. In other words, the potential outcome for any individual is assumed to be
independent of the treatment assignments of all other individuals. The ignorability assumption, also known
as the conditional independence assumption or no unmeasured confounders assumption, plays a pivotal role in
5

the field of causal inference, particularly in observational studies where random assignment to treatment and
control groups is not feasible. This assumption is crucial for estimating causal effects from observational data,
where the potential for confounding variables is a significant concern. The ignorability assumption allows
researchers to control for confounding variables through statistical methods such as regression, matching,
stratification, or weighting. By adjusting for a comprehensive set of observed covariates X, one can estimate
the average treatment effect (ATE) or the average treatment effect on the treated (ATT) as if the treatment
assignment were random, mimicking a randomized controlled trial. The positivity assumption, also known as
the overlap or support condition, states that every unit (e.g., individual in a study) has a non-zero probability
of receiving each treatment level, given the covariates. The consistency assumption states that the potential
outcome of an individual under a specific treatment is equal to the observed outcome if the individual
receives that treatment. For marketing campaign application, we provide data processing guidelines on how
to achieve these assumptions to ensure the validity of causality analysis.
Table 2: Causal Data Assumptions: How to satisfy these requirements through data processing.
Assumption How to achieve through data processing
SUTV A Ensure the campaign measurement timeline is short
enough before noticeable interferences among units
are realized.
Ignorability Control for covariates to achieve independent treat-
ment assignment.
Positivity Trimming, weighting, or synthetic control group gen-
eration to ensure the population data restricts the
causality analysis to the overlap region where con-
trol and treatment can both be observed.
Consistency Ensure the consistency of treatment or note if there
are different versions of treatment. For new cam-
paigns, a new causality analysis needs to be per-
formed. This is important for assessing multiple
treatment effects.
Once data is pre-processed to avoid yielding biased estimates, we can then apply Algorithm 1. The
sample result is provided in Section 3.2.
3.2 Numerical Results
Before we study the numerical results produced by Algorithm 1, we need to ensure the convergence of the
algorithm. Below is a sample of the convergence result in Table 3.
Table 3: Converged Result
ATE SE SE-ATE Ratio (%) Movement Precision Segment Movement
0.507 0.005 1.053 1264.063 1235
In Table 3, the convergence of the causality module produces metrics on ATE, SE, P-Value, SE-ATE
Ratio (%), and Movement Precision. The convergence of the overall movement produces the ”Segment
Movement” that is lower than ”Movement Precision” for the overall system to be considered converged.
Additionally, we can visualize the converged segmentation results and sensitivity study of the converged
results.
Figure 3a shows that the causality is segmented into three segments. For the sensitivity study, we apply
the Qini curve measurement [7]. The Qini curve is a performance measurement for uplift modeling, which
evaluates the effectiveness of a treatment in a causal inference context. The concept of the Qini curve is
6

(a) Segmentation Result
 (b) Sensitivity Analysis
Figure 3: Segmentation results and sensitivity study result for the converged system described in Table 3
analogous to the Gini coefficient used in economics and the ROC curve used in binary classification models,
but it is specifically designed for quantifying the incremental impact of a treatment or intervention. Figure 3b,
measured with a Qini curve, shows that the 90% confidence range (CI) is shaded. Overall, it appears that
even the bottom envelope of our sensitivity study still shows positive improvement over a random assignment
Qini curve.
3.2.1 Simulation Studies and Discussions on KMeans, Propensity Score, and Causal Effect
Based Promotion Selection
After causal segmentation converges, we can perform a simulation study following the convergence of Al-
gorithm 1. This simulation study compares causality-based population selection, propensity score-based
selection, KMeans-based selection, and a random selection strategy. The relative performance of these four
selection strategies is graphed in Figure 4.
Figure 4 is plotted with the population selection percentage on the horizontal axis and the respective
cumulative uplift gain on the y-axis. Thus, when 0% of the population is selected, the overall expected
promotion gain is 0; when 100%, the selection strategy of any kind no longer matters. Interestingly, the
figure shows that the population selected with the causal effect criterion demonstrates the highest overall
gain regardless of what percentage of the population is selected for promotions. The KMeans and Random
selection curves nearly coincide with each other. Most notably, the promotion target population selected
using the propensity score performs even worse than random selection.
Causal Effect For more detail on the causal effect selection strategy, this strategy prioritizes individuals
based on their ranked uplift effects. We can intuitively understand the convex curve of the causal effect
through Figure 5.
Intuitively, selecting a promotion population based on ”Causal Effect” (CATE) in descending order is
akin to choosing users with the highest uplift first, represented in the lower right corner of Figure 5. The
initial slope of the ”Causal Effect” is the steepest because it involves selecting users from a small portion of
the population. The ”Causal Effect” curve will gradually level to match the slope of the ”Random” curve,
indicating a transition towards random population selection. Eventually, the ”Causal Effect” curve may
adopt a negative slope, signaling that users with negative uplift are being selected.
7

Figure 4: Simulation study comparing the performance among the cumulative return gain of four different
promotion population selection strategies. Causal Effect selection is based on the treatment effect. Propen-
sity score selection is based on the propensity, which is regressed from the given X to the propensity of
obtaining outcome Y . KMeans is based on clustering results using X. Random selection is a random pro-
motion assignment, whose expected slope is the same as the expected gain, i.e., ATE.
Figure 5: Simulation study comparing the performance in terms of cumulative return gain among four
different promotion population selection strategies. Specifically, the causal effect curve is labeled.
K-Means Why Does Pure K-Means Without Causality Segmentation Perform Poorly? As depicted in
Figures 4 and 5, the performance of K-Means aligns closely with that of random assignment strategies for
promotion allocation. K-Means is an unsupervised learning algorithm that focuses on partitioning datasets
into k groups based on feature similarity. It aims to divide the n observations into k clusters, where each
observation is assigned to the cluster with the nearest mean, serving as the prototype for that cluster.
8

The clusters formed by K-Means are based on the mathematical criterion of minimizing the variance
within clusters, as measured by the Euclidean distance. This objective does not necessarily align with
human intuition or domain-specific, meaningful groupings. Therefore, while not ”artificial” in the sense of
being random or arbitrary, the clusters may not always correspond to explainable or expected patterns in
the data. K-Means does not ensure that the results of clustering will be inherently understandable or match
known categories within the data. The algorithm identifies structures based on its mathematical objective,
which may or may not coincide with meaningful or recognizable categories to humans.
K-Means is a powerful tool for exploratory data analysis and can uncover intriguing patterns within
the data. However, its simplicity and the nature of its objective function mean that it is most effective
under specific conditions—namely, when supplemented by domain knowledge, additional context, or other
clustering methods for interpreting the results.
Figure 6 showcases a sample of behavior segmentation results commonly utilized by marketing strategists.
The characterization of each K-Means segmented segment is based on a posteriori interpretation rather
than predictive outcomes. For instance, Segment A in Figure 6 is identified as representing loyal, highly
interested customers, while Segment E is categorized as comprising highly critical and cautious customers.
This segmentation information is relevant for businesses. However, these interpretations are not directly
derived from K-Means; the computation steps of K-Means were not informed by these specific objectives or
personas. Thus, the explanation of the segments is somewhat artificial, as illustrated in Figure 6.
Figure 6: When K-Means segmentation is performed for marketing purposes, the segmentation initially relies
on input covariates that represent behavior traits. After segmentation is completed, each segment is then
characterized by distinct behaviors. +
Propensity Score The most interesting curve in the simulation studies depicted in Figures 4 and 5 relates
to the propensity score, which actually performed worse than both the causal effect-based and K-Means-
based promotion selection strategies. Propensity models, which assess the relationship between covariates
+Disclaimer: Medicorin is a fictional drug name used for illustrative purpose only.
9

X and the purchase outcome Y , do not inherently aim to answer how to select a population for promotion
activities to maximize uplift gain. Essentially, a propensity model only addresses the likelihood of a purchase
occurring given X, not how to select individuals for promotional activities to achieve the greatest uplift.
Figure 7: An illustration of quadrants [10]
Figure 7 illustrates that even if someone has a high propensity to purchase, this should not serve as
the sole criterion for deciding whether to allocate marketing resources to specific customers. For example,
customers identified as ’Sure things’, despite their high propensity, are not ideal candidates for spending
marketing dollars on. Conversely, just because customers have a low propensity to purchase does not mean
they should automatically be excluded from marketing efforts, especially if they fall into the ”Lost Causes”
quadrant.
Table 4 clearly defines the propensity score as P (Purchase |No Intervention), which is distinct from the
objectives addressed by causal effect analysis in Equations 2 and 3.
Table 4: Machine Learning Model Comparison
ML model Model tries to answer Business problem we hope to solve
Propensity model P (Purchase |No Intervention) Find audiences with:
High P (Purchase |Intervention)
Low P (Purchase |Intervention)
Churn model P (Churn |No Intervention) Find audiences with:
High P (Churn |Intervention)
Low P (Churn |Intervention)
Response model P (Purchase |Intervention) Find audiences with:
High P (Purchase |Intervention)
Low P (Purchase |Intervention)
Therefore, neither the churn modelP (Churn |No Intervention) nor the response modelP (Purchase |Intervention)
10

should be used as strategies for selecting customers for promotions.
However, this does not fully explain why the propensity score selection strategy is the least effective
among all promotional target selection strategies depicted in Figures 4 and 5. To clarify, we examine the
relationship between propensity scores and CATE, as illustrated in Figure 8.
Figure 8: Not only are they not correlated, they are mildly negatively correlated.
Figure 8 shows that propensity scores and CATE are not strongly correlated; in fact, they are weakly
negatively correlated. Therefore, propensity scores cannot serve as a substitute for causality analysis in
uplift modeling.
3.3 Explainability
Given the exclusivity between causality analysis and segmentation results as outlined in Theorem 1, the
explainability of the overall iterative causal segmentation algorithm merits discussion. Although the seg-
mentation algorithm is unsupervised and ordered by thresholding, Algorithm 1 can be elucidated through its
causality module. This module records the converged state when all three modules—causality, segmentation,
and segment movement—have converged. Techniques like SHAP values can be adopted to provide granular
explanations.
Since SHAP values can offer individualized explanations regarding features, as demonstrated in Figure 9,
they can be utilized for the causality module of the iterative causal segmentation algorithm (Algorithm 1).
Moreover, due to the exclusivity detailed in Theorem 1, the SHAP value explainability for the causality
module also extends to the overall explainability of the iterative causal segmentation algorithm.
4 Conclusion
In this paper, we have introduced the iterative causal segmentation algorithm, Algorithm 1, designed specif-
ically for marketing contexts where segmentation strategies play a crucial role in influencing purchase out-
comes. This necessitates addressing the tightly coupled system between promotion and segmentation.
We demonstrated the value of this segmentation algorithm by comparing it with other common machine
learning models used in marketing settings in Section 3.2.1. Furthermore, we established the exclusivity of
11

Figure 9: Example of SHAP value explainability for the converged results of Table 3 with a subpopulation
of 100 data points. Note: SHAP value computation can be computationally expensive.
the proposed segmentation method, showing that it cannot be easily replaced by other methods, as evidenced
in Section 2.4.
References
[1] Huigang Chen, Totte Harinen, Jeong-Yoon Lee, Mike Yung, and Zhenyu Zhao. Causalml: Python
package for causal machine learning, 2020.
[2] Behram Hansotia and Brad Rukstales. Incremental value modeling. Journal of Interactive Marketing ,
16.3, 2002.
[3] Edward H. Kennedy. Towards optimal doubly robust estimation of heterogeneous causal effects, 2023.
[4] et al K¨ unzel, S¨ oren R. Metalearners for estimating heterogeneous treatment effects using machine
learning. Proceedings of the national academy of sciences , 116.10, 2019.
[5] Judea Pearl. Causality: Models, Reasoning, and Inference . Cambridge University Press, 2009.
[6] Judea Pearl. The do-calculus revisited. arXiv:1210.4852 [cs.AI] , 2012.
[7] Nicholas J. Radcliffe and Patrick D. Surry. Real-world uplift modelling with significance-based uplift
trees. White Paper TR-2011-1, Stochastic Solutions, 2011.
[8] Wendell R. Smith. Product differentiation and market segmentation as alternative marketing strategies.
Journal Name Here , Vol. Number Here(Issue Number Here):Page Range Here, 1956.
[9] Tyler J. VanderWeele. Principles of confounder selection. European Journal of Epidemiology, 34(3):211–
219, 2019.
[10] Robert Yi. Pylift: A Fast Python Package for Uplift Modeling, 2018. Accessed: date.
12

[11] Yan Zhao, Xiao Fang, and David Simchi-Levi. Uplift modeling with multiple treatments and general
response types. In Proceedings of the 2017 SIAM International Conference on Data Mining . Society for
Industrial and Applied Mathematics, 2017.
13
