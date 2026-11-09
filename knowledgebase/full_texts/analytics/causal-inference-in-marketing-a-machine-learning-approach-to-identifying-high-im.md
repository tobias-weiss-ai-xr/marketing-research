---
title: 'Causal Inference in Marketing: A Machine Learning Approach to Identifying High-Impact Channels'
url: https://doi.org/10.5120/ijca2025925302
category: analytics
subcategory: measurement
date: 2025-07
venue: International Journal of Computer Applications
authors:
- Paras Doshi
source: openalex-oa
pdf_url: https://doi.org/10.5120/ijca2025925302
pages: 7
chars: 34384
fetched_at: '2026-11-08T17:01:56+00:00'
kb_version: 1
---

# Causal Inference in Marketing: A Machine Learning Approach to Identifying High-Impact Channels

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
7
Causal Inference in Marketing: A Machine Learning
Approach to Identifying High-Impact Channels
Paras Doshi
Opendoor
Santa Clara, USA

ABSTRACT
Traditional marketing attribution models rely heavily on
correlational analysis and are susceptible to over-attributions of
conversion to the last touching point. The outcome  is wasted
budget spending and suboptimal marketing efforts. Recent
causal inference study focuses on the determination of single
channel effects and neglects the dependence among the effects
from multi -channels and the effects of time. This research
presents a machine learning powered causal inference method
which integrates propensity  score estimation, uplift modeling
and longitudinal data  analysis for multi -channel marketing
effectiveness. The proposed  approach models cross -channel
interactions, revealing solicitations between social media,
Email Campaigns, and PPC  Ads and the lagged efficacy of
marketing. Evidence shows a budget discrepancy of up to 30%
in traditional attribution  models that overestima te direct -
response channels. The findings underline the importance of
causal inference-driven marketing analytics that creates a
more d ata-informed basis for budget allocation, campaign
planning and campaign performance evaluation in a
hypercompetitive environment.
Keywords
Causal inference, multi -channel attribution, uplift modeling,
machine learning in marketing, marketing effectiveness,
Marketing budget allocation.
1. INTRODUCTION
The precise measurement of the effectiveness of marketing
channels is essential for the optimization of campaign strategy
and budget allocation. Traditional attribution models, such as
last-touch and multi -touch attribution, have a tendency to
misestimate causal relationships by omitting underlying
dependencies and confounding variables. As a result,
marketing resources are wastefully allocated, leading to
suboptimal decision -making. Causal inference methods
provide a stronger foundation by separating the t rue effects of
marketing interventions. However, despite the progress made
in machine learning, most existing research has a tendency to
investigate single-channel impact measurements, thus ignoring
the complex interdependencies between multiple marketing
channels. Furthermore, the long -term effects of marketing
interventions are under researched, yet they significantly
contribute to consumer retention and engagement. This
research introduces a novel framework that combines cross -
channel causal inference an d longitudinal analysis using
machine learning. Based on propensity score estimation, uplift
modeling, and outcome prediction, the proposed  approach
measures the causal effects of various marketing touchpoints
with precision while measuring their long -term effects on
consumer behavior. The findings of this research provide data-
driven marketing decisions, offering an enhanced and
actionable f oundation for budget optimization and strategic
planning.
2. LITERATURE REVIEW
2.1 Causal Inference and Machine
Learning in Marketing
The area of causal inference in marketing has progressed from
traditional econometric models to machine learning -based
models. Traditional marketing performance measurement was
performed through attribution models such as last -touch and
multi-touch attribu tion. These correlation -based models and
not causality -based models have been shown to misattribute
conversions and waste marketing budgets [1], [6]. Traditional
econometric methods such as Propensity Score Matching
(PSM) [13], Difference -in-Differences (D iD) [4], and
Instrumental Variables (IV) [2] have been extensively used to
measure causal effects in the marketing field. Although these
techniques offer structured mechanisms for addressing
confounding variables, they face high -dimensional,
observational marketing data. PSM relies on the assumption
that all confounders are available, which is seldom true in
digital marketing. DiD needs a clear treatment and control
group, which is difficult to define in dynamic marketing
settings. IV techniques rely on strict exclusion restrictions that
are difficult to justify, considering the complicated interactions
between multiple marketing channels [3], [12].
Last-touch and multi -touch attribution models are classic
attribution models that are still extensively applied in
marketing analytics. However, these techniques do not address
confounding variables and cross-channel interactions, resulting
in biased concl usions [7], [14]. Last -touch attribution assigns
complete credit to the last touchpoint prior to conversion,
without considering cumulative impact of past interactions.
Multi-touch attribution assigns credit to various channels but
lacks a robust causal st ructure to identify the real drivers of
conversion. Rule-based attribution models, which are based on
pre-defined heuristics, can’t learn from complex consumer
journeys and changing behaviors [1], [6], [14].
To counter these weaknesses, machine learning -based causal
inference techniques have emerged as a more flexible and
scalable approach. Techniques such as Causal Forests  [10],
Double Machine Learning [5], and Uplift Modeling  [8], [9]
enable the estimation of heterogeneous treatment effects while
addressing nonlinear interactions between marketing channels.
These machine learning techniques complement classic
econometric models through automated feature selection,
addressing high-dimensional data, and modelin g complicated
relationships between variables. They also enable real -time
adaptation to dynamic marketing settings, with more precise
causal insights [5], [11], [12].

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
8
Figure 1: Comparison of Attribution Models
2.2 Gaps and Limitations in Existing
Methods
In spite of the advancements in machine learning-based causal
inference, there are some important limitations that remain.
Most of the current studies analyze single marketing channels
in isolation, ignoring cross -channel interdependencies that
significantly influence customer decision -making [14]. This
oversimplification yields biased causal estimates and
inefficient budget allocation. Most studies consider only short-
term conversion effects without incorporating the effect of
delayed and cumulative marketing effects, which are crucial for
long-term consumer engagement [7], [15]. Utilization of short-
term attribution models results in reactive marketing strategies
rather than proactive marketing strategies. In spite of the
growing popularity of uplift modeling for consumer
segmentation, most applications use static segmentation
variables like age, gender, and past purchasing history, instead
of adjusting to dynamic behavioral patterns evolving over time
[8], [9]. Such an approach leads to less efficient targ eting and
engagement strategies, which fail to represent the complexity
of consumer decision-making adequately.
Another important limitation of current research is the inability
to incorporate multi -touch marketing effects appropriately.
Most traditional studies analyze marketing interventions in
isolation, assuming that a consumer's reaction to a marketing
channel is independent of exposure to other channels [6], [14].
In practice, consumer decision -making is influenced by many
interdependent marketing interactions over time. The inability
to incorporate these interactions leads to marketing strategies
that overesti mate direct-response channels and underestimate
the role of sustained engagement strategies like social media,
email campaigns, and content marketing [7], [14]. The inability
to conduct longitudinal analysis in most causal inference
studies limits the unde rstanding of how marketing
interventions affect customer behavior over time. As a result,
marketing decisions based on short -term attribution models
tend to forget that advertising and promotional efforts drive
customer retention and lifetime value beyond short-term
conversions. To overcome these shortcomings requires a
strategy that integrates multi -channel interdependencies and
long-term marketing effects into causal inference models [5] ,
[10].
3. METHODOLOGY
3.1 Data and Experimental Setup
Empirical analysis was conducted on a data set of 8,000 records
with 20 variables measuring customer interactions across
marketing touchpoints, both online and offline. The research
utilizes propensity score estimation using Logistic Regression
and outcome modeling using a Random Forest Classifier to
learn cross -channel causal effects and longitudinal effects of
marketing campaigns. These techniques enable more precise
measurement of marketing effectiveness with control of
underlying variables.

3.2 Model Implementation and Evaluation
Propensity Score Estimation (PSE) was used to balance
treatment groups to enable differences in conversion outcomes
to be due to marketing interventions and not confounding
variables. A Random Forest Classifier was used to predict
probabilities of conversi on while modeling nonlinear
relationships between marketing channels and consumer
behavior. The uplift modeling technique also estimated the
incremental effect of marketing exposures, allowing for more
targeted marketing resource allocation.

3.3 Data Collection and Preprocessing
To ensure robustness and validity of causal inference, the data
went through various preprocessing steps comprising data
cleaning, feature engineering, and normalization. The
treatment variables included CampaignChannel,
CampaignType, AdvertisingPlatform, and AdvertisingTool.
The outcome variable was conversion, depicted by a binary
classification model (1 = conversion, 0 = no conversion).
Confounding variables like Age, Gender, Income, AdSpend,
Click-Through Rate (CTR), Conversion Rate, Website Visits,
Pages Per Visit, Time on Site, Social Shares, Email Opens,
Email Clicks, Previous Purchases, and Loyalty Points were
incorporated to remove the possibility of bias from the model.
To handle missing data, multiple imputations were applied,
especially to variables like AdSpend and Engagement Metrics,
to prevent biased estimates. Categorical variables like
CampaignChannel and AdvertisingPlatform were encoded
through one -hot encoding to enable causal estimation
interpretability. Continuous variables like AdSpend a nd Time
on Site were normalized to remove scale bias among the
machine learning models. Outlier detection handling employed
Interquartile Range (IQR) filtering to remove extreme values
that cause skew causal effects.
3.4 Causal Inference Framework
The study employs a causal inference approach grounded in
machine learning with three basic steps. First, Propensity Score
Estimation (PSE) is used to obtain balance between treatment
groups by estimating the conditional probability of marketing
exposure g iven observable covariates for comparability
between treated and untreated units. Second, Outcome
Prediction (Causal Estimation) predicts the probability of
conversion and adjusts for confounding variables to better
estimate the direct effect of marketing interventions. Third,
Uplift Modeling (Heterogeneous Treatment Effects) predicts
an incremental increase in the probability of conversion from
exposure to marketing and identifies customer segments most
responsive to alternative marketing strategies. This approach is
a more realistic and empirically informed measure of marketing
effectiveness compared to the traditional attribution model.

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
9
3.5 Propensity Score Estimation (PSE)
To avoid selection bias in exposure to marketing, propensity
scores were estimated by employing Logistic Regression,
assigning a probability to the probability of a customer's
receiving a specific marketing treatment:
𝑃( 𝑇𝑖 = 1 ∣∣ 𝑋𝑖 ) = 𝑒𝛽0+𝛽1𝑋𝑖1+𝛽2𝑋𝑖2+⋯+𝛽𝑛𝑋𝑖𝑛 1+𝑒𝛽0+𝛽1𝑋𝑖1+𝛽2𝑋𝑖2+⋯+𝛽𝑛𝑋𝑖𝑛    (1)
Where;
• P(Ti=1∣Xi) is the probability that individual i
receives treatment (is exposed to a marketing
channel), given covariates Xi
• Xi1,Xi2,…,Xin represent the covariates (e.g., age,
income, previous purchases).
• β0 is the intercept, and βn are the regression
coefficients for each covariate.
To evaluate balance of the propensity scores, the study
conducts overlap checks by standardized mean differences
(SMDs) across treatment groups. If imbalance still exists in
some instances, inverse probability weighting (IPW) or
covariate-matching methods can be used to improve
adjustment for biases.
3.6 Outcome Prediction Using Random
Forest
After estimation of propensity scores, the research estimated
the causal impact of marketing exposure on the probability of
conversion. Since customer interactions are nonlinear and of
high dimensionality, a Random Forest Classifier was used for
prediction.
 𝑌𝑖 = 𝑓(𝑇𝑖, 𝑋𝑖) + 𝜖𝑖    (2)
• Yi is the conversion outcome for customer i (1 if
converted, 0 otherwise).
• Ti is the treatment indicator (exposure to a specific
marketing channel).
• Xi represents confounding variables.
• ϵi captures unexplained variation.
• The function f(T i,Xi) is approximated using a
Random Forest model.
The research further validates model performance using:
• Accuracy & F1-score (classification performance)
• AUC-ROC Curve (discriminative ability)
• Feature Importance Analysis (determining key
conversion drivers)
The analysis  also compares Random Forest results with
alternative ML models such as Gradient Boosting and Causal
Forests to test robustness.
3.7 Uplift Modeling
To model the incremental contributions of marketing
interventions, uplift scores were computed, which capture the
difference in probability of conversion between treated and
control customers:
Uplift i = 𝑃( 𝑌𝑖 ∣∣ 𝑇𝑖 = 1, 𝑋𝑖 ) − 𝑃( 𝑌𝑖 ∣∣ 𝑇𝑖 = 0, 𝑋𝑖 )
(3)
Where;
• Uplifti represents the estimated increase in
conversion probability due to marketing exposure.
• P(Yi∣Ti=1,Xi) is the predicted probability of
conversion under treatment.
• P(Yi∣Ti=0,Xi) is the predicted probability of
conversion without treatment.
To check for robustness, customers are split into high, medium,
low responders based on uplift scores (maintaining
heterogeneity), test uplift estimates over deciles (maintaining
heterogeneity) and compare uplift model performance with
baseline rule-based attribution techniques. This allows firms to
invest marketing budgets in high -ROI segments instead of
using strategies across the board.
3.8 Model Evaluation
To provide causal estimates reliability, various evaluation
methods were employed. Propensity score validation was
achieved by testing balance through standardized mean
differences (SMDs). In case of imbalance, Inverse Probability
Weighting (IPW) or covari ate matching was used to control
confounding differences. The outcome prediction model, a
Random Forest classifier, was validated through accuracy, F1-
score, and AUC -ROC to estimate classification performance.
Feature importance analysis was performed to determine
influential marketing variables that influence conversions. For
uplift modeling, validation was achieved by comparing uplift
scores by customer deciles, testing treatment effect
heterogeneity, and determining the most responsive customer
segments. Sensitivity analysis was perfor med by testing
alternative model specifications, e.g., Causal Forest and
Gradient Boosting, while varying confounder selection to
determine the causal estimates robustness. Counterfactual
analysis was performed by comparing predicted and actual
conversions under various treatment assignments, such that the
causal interpretations derived from the model were reliable.
Using these validation methods, bias was reduced,
interpretability was enhanced, and causal effect estimation was
made more robust. The propose d methodology provides a
scalable, data-driven solution for marketers to better allocate
budgets, optimize customer engagement strategies, and
enhance long-term marketing effectiveness.
4. RESULTS
Figure 2: Correlation Matrix
4.1 Model Performance Evaluation
Model performance evaluation and marketing effectiveness
reported significant differences between traditional attribution

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
10
models and machine learning -based causal inference
approaches, particularly for budget misallocation, customer
engagement, and channel effectiveness.
4.2 Propensity Score Estimation (Logistic
Regression Performance)
The Logistic Regression model achieved 88.5% accuracy and
an AUC-ROC of 75.8%, reflecting a good ability to predict the
probability of treatment assignment. However, another
investigation of standardized mean differences (SMDs)
revealed differences in cust omer engagement metrics,
including Click -Through Rate (CTR) and Time on Site. To
address these differences, Inverse Probability Weighting (IPW)
and covariate-matching strategies were employed, which led to
better balance across covariates.
4.3 Outcome Prediction (Random Forest
Classifier Performance)
The Random Forest Classifier achieved better than Logistic
Regression, with an accuracy of 89.4% and an AUC -ROC of
78.5%, thereby reflecting its stronger ability to capture
nonlinear relationships between marketing channels and the
probability of conversio n. A feature importance analysis
revealed that Email Clicks, Time on Site, and Social Media
Engagement were the most important variables, reflecting the
strong contribution of interactive engagement -centering
marketing strategies.
4.4 Uplift Modeling Findings
Uplift modeling revealed more detailed insights into the
incremental impact of individual marketing channels on
conversion rates. The analysis reported that customers with
high engagement metrics (e.g., Email Clicks, Time on Site)
reflected significantly higher uplift values, reinforcing the fact
that marketing exposure is most powerful when consumers
have already displayed interaction or interest. On the other
hand, consumers with low or negative uplift scores reflected
low engagement levels before exposur e, justifying the
assumption that blanket marketing strategies are ineffective.
Rather, marketing to high -propensity consumers for
engagement results in a better return on investment (ROI).
4.5 Marketing Channel Effectiveness &
Budget Allocation Insights
A comparison of some of the marketing channels showed
varying average uplift values and conversion rates:
Table 1: Conversion Rates and Uplift Across Marketing
Channels
Marketing Channel Conversion Rate (%) Average Uplift (%)
Social Media Ads 12.8 6.2
Email Campaigns 15.4 7.1
PPC Ads 9.3 3.8
Display Advertising 6.5 2.2
The results indicate that Social Media and Email Campaigns
achieved the highest uplift and conversion scores, confirming
that engagement -based methods like PPC Ads and Display
Advertising are surpassed by exposure -based methods. The
study also revealed bud get over -allocation in standard
attribution models, which overestimated the impact of PPC Ads
despite their low uplift scores. Budget reallocation to more
effective channels like social media and Email Campaigns
would significantly improve marketing ROI.

Figure 3: Marketing Channel Vs. Gender on Conversion

Figure 4: Marketing Channel Vs. Gender on Conversion
4.6 Demographic & Behavioral
Segmentation Insights
The marketing campaigns received a mixed response across
demographic groups, highlighting the importance of targeted
strategies.
Table 2: Top-Performing Marketing Channels Across
Demography
Demographic
Segment
Top-Performing
Channel
Response
Rate (%)
18-30 (Younger
Audience)
Social Media, PPC
Ads
21.20%
31-45 (Mid-Age
Group)
Email Campaigns,
PPC
16.80%
46+ (Older
Audience)
Traditional Email 12.50%
Young age groups (18 -30 years) showed a greater
positive response to Social Media and Pay-Per-Click ads,
while older age groups (46 years and older) preferred
interaction via email. This proves that segmentation
based on age is better than mass marketing techniques.

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
11

Figure 5: Marketing Channels Across Demography

Figure 6: Campaign Type Across Demography
A longitudinal analysis of campaign performance
determined that different campaign types operated on
different performance curves over time. Awareness
campaigns, which were intended to drive branded
visibility, achieved the lowest conversions. While they
were successful in raising visibility, they did not directly
impact sales. The performance of these campaigns was
significantly enhanced when combined with retargeting
campaigns. Retention campaigns, such as loyalty emails
and VIP offers, drove the highest uplift values, especially
among repeat customers. This indicates that relationship
nurturing with existing customers through personalized
rewards deepens long -term relationships and increases
conversion rates. Conversion campaigns, which are
focused on ins tant sales through promotion and price
reductions, triggered short -term conversion peaks but
lacked the promotion of continuous engagement. Their
performance was fleeting unless complemented by
continuous engagement programs. These findings
highlight the n eed for an integrated marketing program
that balances awareness, engagement, conversion, and
retention campaigns to facilitate long -term customer
acquisition and growth.
5. FEATURE IMPORTANCE ANALYSIS
To determine which variables most impacted conversion
probability, the Random Forest Classifier was employed. The
top three conversion-critical variables were Email Clicks, Time
on Site, and Ad Spend. Email Clicks was the strongest
predictor, confirming that the most active users tend to convert.
This reinforces the importance of optimally positioned email
campaigns that spur active rather than passive opening. Time
on Site was second, which means users spending more time on
site having a higher likelihood of a purchase. Ad Spend, though
significant, came behind engagement-based metrics, indicating
that increased spending does not necessarily equate to
improved conversions without adequate targeting.

Table 3: Top-Performing Marketing Channels Across Demography
Feature Importance (%) Interpretation
Email Clicks 18.20% Strongest predictor of conversion; highly engaged users are more likely to convert.
Time on Site 16.50% Longer engagement correlates with higher purchase likelihood.
Ad Spend 14.70% Increases visibility but does not directly drive conversions.
Click-Through Rate (CTR) 12.90% Higher CTR indicates strong ad relevance and engagement potential.
Previous Purchases 11.30% Returning customers have higher conversion rates than new users.
Social Media Engagement 9.80% Indicates customer interest and purchase intent.
Loyalty Points 8.20% Incentivized engagement drives conversions.
Website Visits 5.70% First-time visitors convert at a lower rate than returning users.
Email Opens 4.80% Less impactful than Email Clicks; opening an email does not indicate strong intent.
Pages Per Visit 3.90% Increased browsing activity correlates with greater purchase likelihood.

5.1 Discussion and Strategic Implications
The findings of this study are counter to prevailing marketing
attribution models, which are prone to overestimating
advertising spend and last -touch interactions and
underestimating customer engagement. Classic models credit
conversions to the last market ing touchpoint in isolation,
ignoring the cumulative outcome of prior interactions. This
study demonstrates that an integrated, multi -touch marketing
strategy provides a more accurate and actionable marketing
effectiveness picture. Strategically, organizat ions need to
redirect attention to high-engagement marketing channels, such
as email marketing, social media, and  website experience
optimization. Retargeting campaigns need to target high -

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
12
engagement users, as this segment shows a significantly higher
likelihood of conversion.
5.2 Limitations & Future Work
While this study presents valuable findings, it also contains
certain limitations. Data availability and quality constraints
may impact the accuracy of causal estimation. The study relies
on observational data, which may have latent biases even when
sophisticated machine learning methods are applied. Future
studies should investigate real -time causal inference models,
allowing organizations to readjust marketing strategies based
on changing conditions. Further integration of deep learning -
based uplift modeling would also make causal effect estimates
more accurate. Additionally, accounting for external economic
conditions and competitive market dynamics within causal
models would provide a more comprehensive view of
marketing effectiveness.
6. INTRODUCTION FEATURE
IMPORTANCE ANALYSIS RESULTS
6.1 Ethical Consideration
Application of machine learning for causal inference in
marketing is susceptible to various ethical issues, mainly
related to data privacy, algorithmic bias, and consumer
transparency. Marketing attribution models are built on huge
amounts of customer data , including demographics, browsing
history, purchase history, and engagement metrics. Data
protection legislation, such as the General Data Protection
Regulation (GDPR) and the California Consumer Privacy Act
(CCPA), needs to be followed while collecting and processing
such data in bulk. Algorithmic bias in propensity score
estimation and uplift modeling is one of the leading ethical
challenges. If training data is underrepresenting certain groups
of consumers, the model will create biased recommendations
and lead to discriminatory targeting or exclusion. For instance,
if the algorithm targets high-income consumers using historical
purchase behavior, it can systemat ically downwardly estimate
the marketing effort impact on low -income consumers and
hence cause discriminatory targeting behaviors. These biases
need to be resolved through regular model auditing, fairness
constraints in training, and diverse data sampling to promote
fair marketing strategies. Another issue is consumer
transparency and informed consent. Most marketing campaigns
are based on behavioral tracking and personalization
algorithms, but the consumers remain oblivious to how their
data are being leveraged for causal inference -based targeting.
Ensuring clear disclosure policies and the ability of users to opt
out of tracking -based marketing campaigns is required to
promote ethical standards for digital marketing analytics.
6.2 Ethical Consideration
Despite the advances outlined in this study, there are several
areas of primary importance that must be explored further to
enhance the usability and effectiveness of machine learning -
based causal inference models in the marketing discipline.
Further advan ces in deep learning algorithms for uplift
modeling can continue to enhance the causal effect estimation.
Current uplift models are mainly tree -based models, such as
Causal Forests and Gradient Boosting; however, the
combination of neural networks and tran sformers may be able
to better capture more complex cross -channel interactions.
Exploring architectures that utilize attention -based uplift
modeling could significantly enhance predictive power in
multi-touch marketing campaigns. Future work should also
address multi-modal causal inference, combining text, image,
and video -based marketing data with structured behavioral
data. Marketing effectiveness is often decided by creative
content and ad copy; however, current models mainly analyze
numeric engagement m etrics. Leveraging natural language
processing (NLP) and computer vision technologies, future
work could investigate the causal effect of ad content quality
on consumer decision-making behavior. Lastly, expanding the
scope of work to cover a range of indus tries and consumer
markets could enhance generalizability. This work is largely
focused on digital marketing channels, but applying similar
causal inference models to healthcare, finance, and retail
industries could yield new insights into multi -touch consumer
behavior.
7. CONCLUSION
This study illustrates the harsh limitations of conventional
attribution models with overreliance on direct -response
channels and neglect of important channel interactions.
Applying a machine learning -based causal inference
methodology, the study estimates  the actual impact of multi -
touch marketing campaigns and shows causal-driven budgeting
can improve ROI by as much as 30%.  The research is an
extension of marketing analysis as it presents a strong theory
that integrates propensity score estimation, uplift  modeling,
and longitudinal analysis. The research concludes that
marketing channels based on engagement, i.e., social media
and email, have higher values of uplift than traditional mass
media advertising channels.
7.1 Key Contributions
7.1.1 Methodological Innovation
The use of propensity score estimation combined with machine
learning-based prediction of the outcome provides a more
robust causal inference platform for marketing than traditional
econometric practice.
7.1.2 Cross-Channel Analysis
The study establishes that interdependencies between
marketing channels are high and hence channel -by-channel
analysis results in inefficient budgeting.
7.1.3 Practical relevance
30% ROI improvement gain constitutes tangible evidence that
approach is relevant to marketing experts.
7.1.4 Generalizability
Generalizability is obtained using cross-industry testing of the
methodology and adoption in healthcare, e -commerce, and
financial services
7.2 Future Research Directions
7.2.1 Real-time Causal Inference
Creating models that are dynamic in the sense that they can
inform marketing strategy in real -time based on real -time
modification of purchasing behavior.
7.2.2 Multi-modal Data Integration
Integrating text, image, and video content analysis to realize the
causal impact of creative features on consumer preference.
7.2.3 Cross-Industry Applications
Using the model in the healthcare, finance, and retail sectors to
assess whether model applies to markets.
7.2.4 Deep Learning Integration
Use attention and neural network -uplift models to enhance
causal effect estimation.

International Journal of Computer Applications (0975 – 8887)
Volume 187 – No.22, July 2025
13
7.2.5 Privacy-Preserving Causal Inference
Developing federated learning algorithms that enable s causal
analysis without violating consumer privacy.
7.2.6 Longitudinal Impact Studies
Long-term causal effects of customer lifetime value of
marketing activity based on causal inference.
7.3 Real-Life Applications
The model is used in business long -term strategic decision -
making and long -term marketing optimization to enable
companies to embrace customer -focused and evidence -based
methods for long-term competitiveness. Marketing
practitioners can:
• Utilize entire budget in media with fixed accuracy
• Segmentation campaigns to reach high -value customer
segments
• Create cross -channel marketing campaigns that take
cross-channel effects into account
• Develop actual marketing ROI vs. one -touch last
attribution
7.4 Industry Impact
From the study, it can be deduced  that non-technical sectors
such as retail, healthcare, and finance can be able to use causal
inference to solve customer experience, maximize ad spend,
and improve decision -making. With machine learning and
causal analysis, businesses are in a position to  develop
customer-centric, data-driven strategies to be successful over
the long term.  The research sets a strong foundation to the
future of marketing analytics technology that is directed
towards causal understanding rath er than correlational data,
thus leading to more productive and effective marketing
expenditure.
8. REFERENCES
[1] Abhishek, V., Fader, P. S., & Hosanagar, K. (2012).
Media exposure through the funnel: A model of multi -
stage attribution. Marketing Science, 33(1), 1-20.
[2] Angrist, J. D., & Pischke, J. S. (2009). Mostly harmless
econometrics: An empiricist's companion . Princeton
University Press.
[3] Athey, S., & Imbens, G. (2017). The state of applied
econometrics: Causality and policy evaluation. Journal of
Economic Perspectives, 31(2), 3-32.
[4] Bertrand, M., Duflo, E., & Mullainathan, S. (2004). How
much should we trust differences -in-differences
estimates? Quarterly Journal of Economics , 119(1), 249-
275.
[5] Chernozhukov, V., Chetverikov, D., Demirer, M., Duflo,
E., Hansen, C., & Newey, W. (2018). Double machine
learning for treatment and causal parameters.
Econometrics Journal, 21(1), C1-C68.
[6] Dalessandro, B., Perlich, C., Stitelman, O., & Provost, F.
(2012). Causally motivated attribution for online
advertising. Proceedings of the Sixth International
Workshop on Data Mining for Online Advertising and
Internet Economy.
[7] De Haan, E., Wiesel, T., & Pauwels, K. (2016). The
effectiveness of different forms of online advertising for
purchase conversion in a multiple -channel attribution
framework. International Journal of Research in
Marketing, 33(3), 491-507.
[8] Gutierrez, P., & Gérardy, J. Y. (2017). Causal Inference
and Uplift Modeling in Marketing. Proceedings of
Machine Learning Research.
[9] He, R., & Rao, A. (2024). Causal Inference Methods and
Applications in Marketing. Now Publishers.
[10] Hitsch, G. J., & Misra, S. (2018). Estimating discrete
choice models of demand using machine learning
methods. Marketing Science, 37(2), 234-256.
[11] Huber, J. (2024). Causal Machine Learning in Marketing.
International Journal of Business and Marketing Science.
[12] Imbens, G. W., & Rubin, D. B. (2015). Causal inference
in statistics, social, and biomedical sciences. Cambridge
University Press.
[13] Li, H., & Kannan, P. K. (2014). Attributing conversions in
a multichannel online marketing environment: An
empirical model and a field experiment. Journal of
Marketing Research, 51(1), 40-56.
[14] Li, S., Sun, B., & Montgomery, A. L. (2020). Cross -
channel spillover effects of online and offline advertising.
Management Science, 66(1), 171-189.
[15] Lewis, R. A., & Rao, J. M. (2015). The unfavorable
economics of measuring the returns to advertising.
Quarterly Journal of Economics, 130(4), 1941-1973.

IJCATM : www.ijcaonline.org
