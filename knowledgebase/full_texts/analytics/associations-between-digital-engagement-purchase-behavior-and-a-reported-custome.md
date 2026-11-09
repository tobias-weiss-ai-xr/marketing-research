---
title: 'Associations Between Digital Engagement, Purchase Behavior, and a Reported Customer Profitability
  Variable in a Secondary E-Commerce Dataset: A Cross-Sectional Exploratory Analysis'
url: https://doi.org/10.1922/comdem.v3i3s.18687
category: analytics
subcategory: theory
date: 2026-09
venue: Computer and decision making.
authors:
- Ada Mitre
- Bogart Yail Márquez
- José Sergio Magdaleno-Palencia
source: openalex-oa
pdf_url: https://comdem.org/index.php/comdem/article/download/18687/12469
pages: 11
chars: 40694
fetched_at: '2026-11-08T18:08:28+00:00'
kb_version: 1
---

# Associations Between Digital Engagement, Purchase Behavior, and a Reported Customer Profitability Variable in a Secondary E-Commerce Dataset: A Cross-Sectional Exploratory Analysis

28

 Computer and Decision Making – An International Journal, Volume 3, Issue 3s, 2026, 28-38

Computer and Decision Making
An International Journal
www.comdem.org
eISSN: 3008-1416

Associations Between Digital Engagement, Purchase Behavior, and a
Reported Customer Profitability Variable in a Secondary E-Commerce
Dataset: A Cross-Sectional Exploratory Analysis
 Ada Mitre1, Bogart Yail Marquez2, Jose Sergio Magdaleno-Palencia3, Arnulfo Alanis4

1Universidad Autónoma de Baja California. Email: mitre.ada@uabc.edu.mx
2Tecnologico Nacional de Mexico, Campus Tijuana. Email: bogart@tectijuana.edu.mx
3Tecnologico Nacional de Mexico, Campus Tijuana. Email: jmagdaleno@tectijuana.edu.mx
4Tecnologico Nacional de Mexico, Campus Tijuana. Email: alanis@tectijuana.edu.mx

ARTICLE INFO ABSTRACT

Article history:
Received 12 June 2026
Received in revised form 08 August 2026
Accepted 16 September 2026
Available online 30 September 2026

Keywords: customer lifetime value;
customer profitability; digital engagement; e-
commerce; customer analytics; RFM; data
leakage; cross-sectional analysis
Background: Customer lifetime value (CLV) and customer profitability are central
constructs in marketing analytics because they guide customer selection, retention, and
resource allocation (Berger & Nasr, 1998; Gupta et al., 2006; Jain & Singh, 2002). Digital
engagement metrics are widely observed in e -commerce, but their relationship with
financial outcomes depends on conceptual definition, temporal ordering, and the
independence of predictors and outcomes. Objective: This study examined concurrent
associations between aggregate digital engagement indicators, purchase-related variables,
and a reported customer profitability field in a secondary e -commerce dataset. Methods:
The analysis used 50,000 customer records and 53 variables. Data auditing assessed
uniqueness, m issingness, internal arithmetic consistency, and redundancy among
monetary fields. Pearson and Spearman correlations and exploratory 70/30 random -
holdout linear models were estimated. Results: Email open rate, click -through rate, and
conversion rate had ne gligible concurrent correlations with reported profitability. The
engagement-only test model had R² = -0.00003. Purchase-related models achieved high
test R² values, but their interpretation is restricted by demonstrated overlap among total
purchases, aver age order value, total spending, CLV, and reported profitability.
Conclusions: The data do not show incremental concurrent linear value for the three
aggregate engagement variables in the specified exploratory model. They also do not
support causal or prospective claims because the dataset has no event dates and contains
highly overlapping monetary fields.

1. Introduction
Customer-level valuation is a foundational problem in marketing because firms must decide which
customers to acquire, retain, develop, or serve with scarce resources. Customer lifetime value provides
a framework for estimating the economic value that a cus tomer relationship may create over time,
considering revenues, costs, retention, and, where appropriate, the time value of money (Berger &
Nasr, 1998; Gupta et al., 2006; Jain & Singh, 2002). In noncontractual customer settings, purchase
histories are especially important because firms must infer whether customers remain active and what
they may do next from observed transactions (Schmittlein et al., 1987).
RFM analysis—recency, frequency, and monetary value—has historically offered a practical summary
of customer purchase histories. Although RFM is often used descriptively for segmentation, it can also
be connected to customer -base models and lifetime -value estimation when assumptions and time
horizons are explicit (Fader et al., 2005; Kumar & Reinartz, 2016). The predictive use of purchase -
related variables nonetheless requires careful attention to whether the target outcome is independent
* Corresponding author
E-mail address: mitre.ada@uabc.edu.mx

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

29
of the predictors. If profitability is constructed from spending, purchase count, or order value, strong
correlations can be partly algebraic rather than evidence of a novel, generalizable relationship.
Digital engagement is also central to contemporary customer analytics. Firms routinely track email
opens, clicks, website activity, conversion rates, social -media responses, and app interactions.
However, engagement is a multidimensional marketing construc t rather than a single behavioral
counter. The customer -engagement literature describes cognitive, emotional, behavioral , and
relational manifestations of engagement and emphasizes that its antecedents and consequences
depend on the focal context (Brodie et al., 2011; Hollebeek et al., 2014; Pansari & Kumar, 2017).
Accordingly, an email open rate or click -through rate may be useful for campaign diagnostics without
being an exhaustive or direct measure of a customer’s economic value.
The relationship between engagement and customer value is theoretically plausible but empirically
conditional. Kumar et al. (2010) proposed that customers may create value through purchases as well
as referral, influence, knowledge, and feedback behaviors.  Kumar and Pansari (2016) similarly argued
that engagement can contribute to competitive advantage through multiple mechanisms. In e -
commerce, Vanderveld et al. (2016) demonstrated that engagement signals may be incorporated into
a customer lifetime value system when features and outcomes are organized in a temporal modeling
framework. These studies do not imply that every aggregate digital metric predicts  every financial
outcome; instead, they show why the contribution of engagement should be tested with transparent
definitions, appropriate time windows, and comparison against established behavioral information.
A separate methodological concern is information leakage. Predictive performance can be exaggerated
when a predictor contains information from the outcome, is derived from the outcome, uses post -
outcome information, or is processed in a way that violates t he separation between training and
evaluation data (Kapoor & Narayanan, 2023; Rosenblatt et al., 2024). In customer analytics, this
problem is especially likely when total spending, CLV, profitability, monetary scores, and customer -
value categories coexist in the same file without a documented feature-generation process.
This study therefore adopts a deliberately cautious objective. It does not attempt to demonstrate that
engagement causes profitability, nor does it label engagement indicators as universally “vanity
metrics.” Instead, it examines the observed concurrent as sociation of email open rate, click -through
rate, and conversion rate with a reported profitability variable in one secondary dataset and
documents material data-structure limitations that restrict interpretation.

2. Theoretical Background
2.1 Customer lifetime value and customer profitability
CLV has been studied as a managerial metric for identifying valuable customers, targeting retention
investments, and assessing the financial return of customer -relationship strategies (Berger & Nasr,
1998; Jain & Singh, 2002). Gupta et al. (2006) reviewed multiple CLV models and highlighted that the
appropriate approach depends on the business setting, customer contract structure, available
transaction information, and cost assumptions. Thus, the terms CLV, customer value, revenue, and
profitability should not be used interchangeably unless the underlying financial calculation is explicitly
documented.
In a noncontractual setting, purchase timing and frequency are often modeled to infer customer
activity. Schmittlein et al. (1987) provided a foundational framework for counting customers and
estimating what they may do next. Fader et al. (2005) linked RFM information to CLV through iso-value
curves, demonstrating that recency, frequency, and monetary value can be organized into a systematic
customer-base analysis. More recent work continues to explore how transaction histories, sequential
behavior, and machine -learning methods can improve future customer -value estimation (Bauer &
Jannach, 2021; Xing et al., 2021).
2.2 Engagement as a multidimensional construct
Customer engagement has developed into a major research domain in marketing and service research.
Brodie et al. (2011) conceptualized engagement as a psychological state arising from interactive
customer experiences. Hollebeek et al. (2014) operationalized consumer brand engagement in social -

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

30
media settings as a multidimensional construct, while Pansari and Kumar (2017) developed a
framework that distinguishes engagement antecedents and consequences. Systematic reviews
likewise emphasize heterogeneity in engagement definitions, operationalizati ons, and outcomes
across contexts (Islam & Rahman, 2021; Srivastava et al., 2025).
This literature makes an important distinction for the present study. Email open rate, click -through
rate, and conversion rate are observable digital behaviors or performance indicators. They are not
equivalent by definition to the broader theoretical cons truct of customer engagement. An empirical
result involving these variables should therefore be described precisely as a result about aggregate
operational indicators—not as a definitive test of customer engagement theory.
2.3 Engagement, value, and temporal ordering
Engagement can be relevant to customer value through direct and indirect pathways. A customer may
buy more, recommend the firm, provide feedback, contribute knowledge, influence others, or
participate in a brand community (Kumar et al., 2010; Kumar & Pansari, 2016). Yet these pathways are
unlikely to be captured fully by contemporaneous aggregate open and click rates. A stronger empirical
design would distinguish the period in which engagement is observed from the subsequent period in
which spending, retention, or profitability is measured. This temporal separation is important both for
forecasting and for causal interpretation (Savitz & Wellenius, 2023).
Vanderveld et al. (2016) provide a relevant example in e-commerce: their engagement-based customer
lifetime value system combined customer engagement signals and behavioral information in a
framework focused on future value. This differs fundamentally from correlating aggregate engagement
rates with a concurrent monetary field in a single cross -section. The distinction does not invalidate
cross-sectional analysis, but it limits the scope of its conclusions.
2.4 Research questions
RQ1: What are the Pearson and Spearman associations between aggregate email open rate, click -
through rate, conversion rate, and the reported customer profitability variable?
RQ2: Do the three aggregate engagement variables improve exploratory random -holdout model
performance after selected controls and purchase-related variables are included?
RQ3: What internal -consistency and variable -redundancy features constrain interpretation of the
dataset’s profitability, CLV, spending, and purchase-related fields?

3. Methods
3.1 Study design and data source
This study used a secondary, cross-sectional dataset supplied as E-commerce Customer Segmentation
(Khan, 2026).  The public source describes the resource as an e -commerce customer-segmentation
dataset combining demographic characteristics, purchasing behav ior, engagement metrics, loyalty
information, RFM scores, churn risk, and customer -value indicators (Datascikhan, 2026). The CSV
contained 50,000 records and 53 variables. The dataset_year field had one observed value, 2026, and
no transaction dates, marketing-contact dates, email-event dates, web-event dates, or future outcome
dates were present. The design is therefore cross-sectional and exploratory.
3.2 Data audit and missingness

Table 1. Data-quality and internal-consistency audit.
Audit item Result
Records 50,000
Variables 53
Unique customer IDs 50,000
Complete duplicate rows 0

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

31
Observed dataset year 2026
Missing preferred_category_3 33,257 (66.51%)
Missing preferred_category_2 16,743 (33.49%)
Missing social_media_presence 12,420 (24.84%)
Missing loyalty_tier 1,272 (2.54%)
Maximum |total_spent − total_purchases × avg_order_value| 2.910e-11
Correlation: CLV with reported profitability 0.999999
Maximum |CLV − reported profitability| USD 200.00
Correlation: total spending with reported profitability 0.966451

All customer_id values were unique, and no complete duplicate rows were identified. Missingness was
concentrated in secondary preference and social-media fields rather than in the variables used for the
principal analyses. No imputation was conducted because the main ana lyses excluded the fields with
substantial missingness.
The audit revealed material redundancy among monetary fields. total_spent_usd equaled
total_purchases multiplied by avg_order_value_usd within floating -point precision.
customer_lifetime_value_usd correlated 0.999999 with customer_profitability_usd, and the maximum
absolute difference between the two fields was USD 200. total_spent_usd correlated 0.966451 with
customer_profitability_usd. These findings create a serious risk that some apparent predi ctive
relationships reflect formula overlap, shared construction, or target leakage rather than independent
explanatory information (Kapoor & Narayanan, 2023; Rosenblatt et al., 2024).
3.3 Measures
Reported profitability variable. customer_profitability_usd was treated as the outcome. Because the
available file did not provide an accounting formula or data dictionary documenting revenue, cost of
goods sold, acquisition expense, return cost, discounting, fulfillment, and service cost s, the field is
referred to as reported profitability rather than independently verified economic profit (Gupta et al.,
2006; Kumar & Reinartz, 2016).
Digital engagement variables. email_open_rate, click_through_rate, and conversion_rate  were
analyzed as continuous proportions. These fields are aggregate measures and therefore cannot identify
whether interactions occurred before or after purchases, whether customers were eligible for all
campaigns, whether the behaviors were campaign -specific, or whether observed rates differed by
message type.
Purchase-related variables. total_purchases, avg_order_value_usd, days_since_last_purchase, and
tenure_months were included as descriptive and exploratory model features. The first two require
special caution because they reproduce total spending exactly in the dataset. RFM theory supports the
relevance of recency, frequency, and monetary behavior for customer -base analysis, but it does not
justify interpreting algebraically connected predictors as independent causal drivers of a
contemporaneous monetary target (Fader et al., 2005; Schmittlein et al., 1987).
Controls. Age, customer acquisition cost, customer health score, churn risk score, customer segment,
income bracket, shopping channel, and device used were included in selected model specifications.
Categorical variables were one-hot encoded with one reference category omitted.
3.4 Statistical analysis
Descriptive statistics summarized distributions of the principal variables. Pearson correlations were
calculated with two -sided 95% confidence intervals using Fisher’s z transformation. Spearman
correlations were calculated as a nonparametric sensitivity a nalysis. Because the analysis is cross -
sectional, all correlations are interpreted as concurrent associations rather than temporal or causal
effects (Savitz & Wellenius, 2023).
For exploratory model comparison, the file was divided randomly into training (70%, n = 35,000) and
test (30%, n = 15,000) partitions using random seed 2026. Ordinary least squares models were fitted
in the training set and evaluated on the held-out test set with R², root mean squared error (RMSE), and
mean absolute error (MAE). Random splitting was used only as an internal robustness check. It does

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

32
not establish out -of-time validity because all observations have the same dataset -year value and no
event timestamps are available (Hastie et al., 2009; Kapoor & Narayanan, 2023).

4. Results
4.1 Descriptive statistics

Table 2. Descriptive statistics for primary analytic variables.
Variable Mean SD Median Minimum Maximum
Reported
profitability
(USD)
57,619.615 52,437.173 42,129.690 -199.870 294,479.720
Email open
rate 0.500 0.290 0.500 0.000 1.000
Click-through
rate 0.251 0.144 0.251 0.000 0.500
Conversion
rate 0.150 0.087 0.150 0.000 0.300
Total
purchases 99.418 57.780 99.000 0.000 199.000
Average order
value (USD) 505.367 285.604 504.790 10.050 999.990
Days since last
purchase 62.971 93.281 19.000 0.000 365.000
Tenure
(months) 59.748 34.310 60.000 1.000 119.000
Customer
health score 86.674 16.107 95.000 30.000 100.000
Churn risk
score 26.841 19.207 25.000 0.000 100.000

The reported profitability field had a mean of USD 57,619.62, median of USD 42,129.69, and standard
deviation of USD 52,437.17, indicating a right-skewed distribution. Mean aggregate engagement rates
were 0.500 for email opens, 0.251 for clicks, and 0.150 for conversions. These values are descriptive
properties of the supplied dataset; they should not be generalized as external benchmarks because the
source file does not document a sampling frame or event-generation process.
4.2 Correlations

Table 3. Concurrent associations with reported profitability (N = 50,000).
Variable Pearson r 95% CI p Spearman ρ p
email open
rate -0.0021 [-0.0109, 0.0066] 0.633 -0.0020 0.651
click through
rate -0.0025 [-0.0112, 0.0063] 0.583 -0.0013 0.771
conversion
rate 0.0055 [-0.0033, 0.0143] 0.219 0.0043 0.341
total
purchases 0.6429 [0.6377, 0.6480] < .001 0.6731 < .001
avg order
value usd 0.6247 [0.6193, 0.6300] < .001 0.6422 < .001
days since last
purchase -0.0063 [-0.0151, 0.0025] 0.160 -0.0033 0.454

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

33
tenure
months 0.0029 [-0.0059, 0.0116] 0.520 0.0046 0.299

The three aggregate engagement measures showed correlations near zero. Email open rate was r = -
0.0021 (95% CI [-0.0109, 0.0066], p = .633), click-through rate was r = -0.0025 (95% CI [-0.0112, 0.0063],
p = .583), and conversion rate was r = 0.0055 (95% CI [-0.0033, 0.0143], p = .219). Spearman estimates
produced the same substantive conclusion. These results indicate no meaningful concurrent linear or
monotonic association in this dataset, but they do not assess delayed, nonlinear, causal, or subgroup -
specific relationships (Brodie et al., 2011; Savitz & Wellenius, 2023; Vanderveld et al., 2016).
Total purchases and average order value had strong positive correlations with reported profitability (r
= 0.6429 and r = 0.6247). Days since last purchase and tenure were near zero. The contrast illustrates
that different purchase -related measures are not interchangeable. It also reinforces the need to
interpret total purchases and average order value in light of their deterministic connection to total
spending and the strong correlation between total spending and the outcome.
4.3 Exploratory holdout models

Table 4. Exploratory 70/30 random-holdout performance (random seed = 2026).
Model Test R² Test RMSE Test MAE
Engagement only -0.00003 USD 52,211.00 USD 42,037.85
Purchase-related only 0.80120 USD 23,279.06 USD 18,002.54
Controls only 0.03665 USD 51,244.60 USD 40,945.16
Controls + purchase -
related 0.80162 USD 23,254.60 USD 17,989.97
Controls + purchase -
related + engagement 0.80156 USD 23,257.95 USD 17,992.88

The engagement-only model had a negative test R² ( -0.00003), meaning that it did not improve upon
a mean-based prediction in the holdout set. The controls-only model produced test R² = 0.03665. The
purchase-related-only model produced test R² = 0.80120, an d the controls -plus-purchase-related
model produced test R² = 0.80162. Adding email open rate, click -through rate, and conversion rate
resulted in test R² = 0.80156, a difference of -0.00006 relative to the model without engagement.
This comparison suggests that the three aggregate engagement variables did not provide incremental
linear predictive signal in the specified random-holdout model. It must not be interpreted as evidence
that engagement is economically irrelevant. The model is not temporally validated, and the high
performance of purchase -related variables may be partly driven by overlapping construction among
purchases, spending, CLV, and reported profitability. Leakage and related forms of information
contamination can create deceptively strong apparent predictive results even when a model will not
generalize to a true future-use setting (Kapoor & Narayanan, 2023; Rosenblatt et al., 2024).

5. Discussion
5.1 Main findings
This analysis yields two complementary findings. First, the three aggregate digital indicators —email
open rate, click -through rate, and conversion rate —had negligible concurrent associations with the
reported profitability field and did not improve the specified exploratory model after selected controls
and purchase-related variables were entered. This is a limited empirical result about this dataset and
these operationalizations.
Second, the monetary structure of the file makes a broad behavioral -versus-engagement conclusion
untenable. Total spending was exactly reproduced by total purchases and average order value. CLV
was almost indistinguishable from reported profitability. Ther efore, purchase -related model
performance cannot be interpreted as a fair contest between independently measured behavioral
predictors and an independently measured future profitability outcome. It may instead partly reflect

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

34
shared formulas or overlapping data-generating processes.
5.2 Relation to prior research
The limited result for aggregate engagement metrics should be situated within, rather than opposed
to, the engagement literature. Customer engagement theory does not claim that any single operational
metric will have a strong direct association with a cont emporaneous financial outcome. Instead, it
conceptualizes engagement as multidimensional, relational, and context sensitive (Brodie et al., 2011;
Hollebeek et al., 2014; Pansari  & Kumar, 2017). Similarly, customer engagement value can include
direct and indirect behaviors beyond transactions (Kumar et al., 2010).
The result also does not conflict with work showing that engagement features can contribute to CLV
systems under appropriate conditions. Vanderveld  et al. (2016) used engagement information within
an e -commerce CLV architecture designed around future value. Such research highlights the
importance of time -oriented feature construction. Future value models based on RFM, probabilistic
approaches, and mo dern sequence -based learning similarly depend on transaction histories that
precede the outcome period (Bauer & Jannach, 2021; Fader et al., 2005; Schmittlein et al., 1987; Xing
et al., 2021).
5.3 Implications for managers
Managers should avoid two symmetric errors. The first is to treat an increase in an engagement
dashboard metric as automatic evidence of economic value. The second is to remove engagement
measures solely because a cross-sectional correlation is near zero. A more useful practice is to connect
each metric to a decision, an intervention, a defined outcome, and a time horizon. Open rates may be
useful for diagnosing delivery or attention; clicks may help evaluate message relevance; conversion
rates may help evaluate funnel friction; and profitability may guide economic allocation. The value of
each metric should be evaluated against the decision it is intended to support.
Organizations should also maintain data lineage for customer analytics. Each variable should have a
documented definition, source system, calculation date, and permissible use in modeling . Monetary
scores, CLV fields, profitability categories, and RFM scores should not be incorporated blindly into
models before analysts determine whether they are derived from the target or from future
information. Such governance is central to credible ana lytics and to valid evaluation of model
performance (Kapoor & Narayanan, 2023).
5.4 Implications for research
A Q1 -level empirical contribution would require data that can distinguish engagement exposure,
subsequent behavior, and independently calculated profitability. At minimum, future research should
define a pre-outcome observation period, use only features available during that period, and calculate
a later outcome window. It should compare a baseline purchase -history mo del with an expanded
engagement model using out-of-time validation. Segment analyses should be prespecified and should
assess whether effects differ by customer type, channel, product category, or campaign purpose.
If the substantive question is causal —whether raising engagement through a marketing intervention
changes profitability —the design should include randomization, a credible quasi -experiment, or
another causal -identification strategy. Cross -sectional associa tion alone cannot settle this question
because it cannot establish temporal precedence or rule out confounding (Savitz & Wellenius, 2023).

6. Limitations
This study has several limitations. First, all observations are associated with a single stated year, 2026,
and the file contains no event -level dates. It cannot evaluate future profitability prediction, lags,
customer trajectories, retention, or causal me chanisms. Second, no complete data dictionary or
profitability formula accompanied the file. Third, the strong redundancy among CLV, reported
profitability, total spending, purchase count, and order value creates a substantial target-leakage risk.
Fourth, aggregate engagement variables may obscure message -level, campaign-level, and sequence-
level variation. Fifth, the random holdout procedure is an internal model comparison, not an out -of-
time test. Sixth, the provenance of the data —operational, synthetic, simulated, or hybrid—cannot be
determined solely from the CSV. These limitations should be treated as central conditions of

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

35
interpretation, not as peripheral caveats.

7. Conclusion
This study examined the concurrent relationships between three aggregate digital -engagement
indicators—email open rate, click -through rate, and conversion rate —and a reported customer
profitability variable in a secondary e -commerce dataset containing 50,0 00 customer records. The
analysis was deliberately framed as exploratory and cross-sectional because the file included only one
stated dataset year, did not contain event -level timestamps, and did not provide a technical data
dictionary documenting how the  principal monetary fields were constructed. These design features
define the appropriate scope of inference: the results describe associations and exploratory holdout -
model performance within the supplied file; they do not establish temporal prediction, e conomic
causality, or universal claims about the strategic value of digital engagement.

The first substantive result was that the three aggregate engagement measures had negligible
concurrent associations with reported profitability. Pearson correlations were -0.0021 for email open
rate, -0.0025 for click -through rate, and 0.0055 for conversi on rate. Their 95% confidence intervals
included zero, and the corresponding Spearman coefficients were similarly close to zero. In the
specified random 70/30 holdout analysis, the engagement -only model did not improve on a mean -
based benchmark, yielding a  test-set R² of -0.00003. Further, adding the three engagement variables
to the controls -plus-purchase-related specification did not increase model performance: test R² was
0.80162 without engagement and 0.80156 after engagement was added. Within this dataset and
model specification, therefore, aggregate email open rate, click-through rate, and conversion rate did
not contribute incremental concurrent linear predictive inform ation beyond the other selected
variables.

This finding should be interpreted precisely. It does not imply that customer engagement is
theoretically unimportant, that digital engagement cannot create value, or that email and digital -
marketing programs should be abandoned. Customer -engagement resear ch conceptualizes
engagement as a multidimensional and context -dependent phenomenon that can encompass
cognitive, emotional, behavioral, relational, and indirect value -creation mechanisms (Brodie et al.,
2011; Hollebeek et al., 2014; Pansari & Kumar, 2017). A single aggregate open rate, click-through rate,
or conversion rate is only one operational indicator and may not capture message relevance, campaign
timing, exposure frequency, product category, channel migration, customer intent, or del ayed
response. Prior e-commerce research also shows that engagement features can be incorporated into
customer-lifetime-value systems when they are measured before an explicitly defined future outcome
and evaluated together with behavioral history ( Vanderveld et al., 2016). The present results are
consequently best understood as evidence about the limited incremental value of these three
aggregate, concurrent indicators in this particular file —not as evidence against the broader
engagement construct.

The second and equally important result concerns the internal structure of the dataset. The apparent
predictive strength of purchase -related variables must be interpreted with substantial caution. The
audit showed that total_spent_usd was exactly reconstructible from total_purchases multiplied by
avg_order_value_usd, within floating-point precision. It also showed that total_spent_usd correlated
0.966451 with reported profitability and that customer_lifetime_value_usd correlated 0.999999 with
reported profitability. These results indicate extremely strong overlap among spending, purchase
components, CLV, and the monetary outcome. Consequently, the high test  R² achieved by purchase -
related models cannot be interpreted as a clean demonstration that independent behavioral features
predict a separately measured future profitability outcome. At least part of the performance may arise
from common formulas, shared inputs, or target-adjacent information.

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

36
This distinction is central to customer analytics. RFM and customer -base modeling provide well -
established reasons to study recency, frequency, and monetary behavior  when estimating customer
value (Fader et al., 2005; Gupta et al., 2006; Schmittlein et al., 1987). Nevertheless, valid prospective
modeling requires that customer-history features be computed before the target period and that the
target be measured independently afterward. It is not sufficient to exclude only an obvious outcome
duplicate, such as CLV, if remaining features are mathematical components of spending and spending
itself is tightly embedded in the profitability calculation. Without transparent data lineage and a
documented financial formula, it is impossible to determine the extent to which estimated model
performance represents genuine forward-looking signal rather than structural overlap. This concern is
consistent with the broader machine -learning literature, which shows that data leakage can produce
misleadingly optimistic estimates of model accuracy and impede reproducibility an d real -world
generalization (Kapoor & Narayanan, 2023; Rosenblatt et al., 2024).

The findings therefore support a measurement-governance recommendation rather than a categorical
ranking of engagement and behavior metrics. Organizations should define each metric in relation to a
specific managerial decision. Engagement indicators may be  appropriate for diagnosing delivery,
audience reach, content relevance, channel performance, or short-term campaign response. Purchase-
history measures may be appropriate for customer -base monitoring and segmentation. Profitability
measures should guide economic resource allocation only when their financial components are
documented and auditable. The analytical question should not be whether one category of metrics is
universally “good” or “bad,” but whether a measure adds decision -relevant information for a clearly
specified outcome, population, time horizon, and intervention.

For future research, the most important improvement is temporal design. A stronger study would
define a historical observation period, such as January through June, in which engagement and
purchase-history predictors are calculated. It would then define a nonoverlapping future period, such
as July through December, during which independently calculated customer profitability, retention, or
future net revenue is measured. The analysis should ensure that no predictor incorporates revenue,
transactions, or classifications from the outcome window. An appropriate empirical comparison would
include: (a) a baseline model with customer characteristics and historical purchase behavior; (b) an
expanded model that adds message -, campaign-, or channel -level engagement variables; and (c) an
out-of-time validation cohort. Such a design could estimate whether engagement adds incremental
predictive value beyond established behavioral information and could identify whether its utility differs
by customer segment, product category, channel, or stage of the relationship.

If the purpose is to determine whether increasing engagement causes financial value, an even stronger
design is required. Researchers would need randomized campaign interventions, credible natural
experiments, quasi -experimental variation, or other causal -identification strategies. Cross -sectional
data cannot establish whether engagement preceded the outcome, whether high -value customers
were more likely to receive or respond to marketing, or whether unobserved characteristics influenced
both engagement and  profitability (Savitz & Wellenius, 2023). Thus, the present study should be
viewed as a diagnostic analysis that identifies data limitations and generates more rigorous future
research questions, not as a final causal test.

In conclusion, the supplied dataset provides no evidence that its three aggregate engagement rates
have meaningful concurrent linear associations with the reported profitability variable or that they
improve the specified exploratory holdout model. At the same time, the dataset’s severe redundancy
among total spending, purchase components, CLV, and reported profitability prevents a strong claim
that purchase-related variables independently and prospectively outperform engagement metrics. The
most defensible conclusion is methodological: valid comparison of digital engagement and behavioral
predictors requires transparent variable definitions, audited data lineage, temporally ordered

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

37
observation and outcome windows, and evaluation on genuinely future data. Under those conditions,
future research can move beyond simple dashboard metrics and determine which customer signals
genuinely improve financial decision making.

References
1. Bauer, J., & Jannach , D. (2021). Improved customer lifetime value prediction with sequence -
to-sequence learning and feature -based models. ACM Transactions on Knowledge Discovery
from Data, 15(5), Article 79. https://doi.org/10.1145/3441444
2. Berger, P. D., & Nasr, N. I. (1998). Customer lifetime value: Marketing models and applications.
Journal of Interactive Marketing, 12(1), 17 –30. https://doi.org/10.1002/(SICI)1520 -
6653(199824)12:1<17::AID-DIR3>3.0.CO;2-K
3. Brodie, R. J., Hollebeek , L. D., Jurić, B., & Ilić, A. (2011). Customer engagement: Conceptual
domain, fundamental propositions, and implications for research. Journal of Service Research,
14(3), 252–271. https://doi.org/10.1177/1094670511411703
4. Datascikhan. (2026). E -commerce customer segmentation dataset 2026 [Data set]. Kaggle.
https://www.kaggle.com/datasets/datascikhan/e-commerce-customer-segmentation-2026
5. Fader, P. S., Hardie, B. G. S., & Lee, K. L. (2005). RFM and CLV: Using iso -value curves for
customer base analysis. Journal of Marketing Research, 42(4), 415 –430.
https://doi.org/10.1509/jmkr.2005.42.4.415
6. Gupta, S., Hanssens, D., Hardie, B., Kahn, W., Kumar, V., Lin, N., Ravishanker, N., & Sriram, S.
(2006). Modeling customer lifetime value. Journal of Service Research, 9(2), 139 –155.
https://doi.org/10.1177/1094670506293810
7. Hastie, T., Tibshirani, R., & Friedman, J. (2009). The elements of statistical learning: Data
mining, inference, and prediction (2nd ed.). Springer. https://doi.org/10.1007/978 -0-387-
84858-7
8. Hollebeek, L. D., Glynn, M. S., & Brodie, R. J. (2014). Consumer brand engagement in social
media: Conceptualization, scale development and validation. Journal of Interactive Marketing,
28(2), 149–165. https://doi.org/10.1016/j.intmar.2013.12.002
9. Islam, J. U., & Rahman, Z. (2021). Customer engagement: A systematic review and future
research priorities. Australasian Marketing Journal, 29(2), 93 –117.
https://doi.org/10.1016/j.ausmj.2020.05.004
10. Jain, D., & Singh, S. S. (2002). Customer lifetime value research in marketing: A review and
future directions. Journal of Interactive Marketing, 16(2), 34 –46.
https://doi.org/10.1002/dir.10032
11. Khan, S. (2026). E -commerce customer segmentation 2026 [Dataset]. Kaggle.
https://www.kaggle.com/datasets/datascikhan/e-commerce-customer-segmentation-
2026/data
12. Kapoor, S., & Narayanan, A. (2023). Leakage and the reproducibility crisis in machine-learning-
based science. Patterns, 4(9), Article 100804. https://doi.org/10.1016/j.patter.2023.100804
13. Kumar, V., Aksoy, L., Donkers, B., Venkatesan, R., Wiesel, T., & Tillmanns, S. (2010).
Undervalued or overvalued customers: Capturing total customer engagement value. Journal
of Service Research, 13(3), 297–310. https://doi.org/10.1177/1094670510375602
14. Kumar, V., & Pansari, A. (2016). Competitive advantage through engagement. Journal of
Marketing Research, 53(4), 497–514. https://doi.org/10.1509/jmr.15.0044
15. Kumar, V., & Reinartz, W. (2016). Creating enduring customer value. Journal of Marketing,
80(6), 36–68. https://doi.org/10.1509/jm.15.0414
16. Pansari, A., & Kumar, V. (2017). Customer engagement: The construct, antecedents, and
consequences. Journal of the Academy of Marketing Science, 45(3), 294 –311.
https://doi.org/10.1007/s11747-016-0485-6
17. Rosenblatt, J. D., et al. (2024). The effects of data leakage on connectome -based machine
learning models. Nature Communications, 15, Article 1574. https://doi.org/10.1038/s41467 -

Computer and Decision Making – An International Journal
Volume 3 Issue 3s, (2026) 28-38

38
024-46150-w
18. Savitz, D. A., & Wellenius, G. A. (2023). Can cross -sectional studies contribute to causal
inference? American Journal of Epidemiology, 192(4), 514 –516.
https://doi.org/10.1093/aje/kwac247
19. Schmittlein, D. C., Morrison, D. G., & Colombo, R. (1987). Counting your customers: Who are
they and what will they do next? Management Science, 33(1), 1 –24.
https://doi.org/10.1287/mnsc.33.1.1
20. Srivastava, R., Gupta, P., Kumar, H., & Tuli, N. (2025). Digital customer engagement: A
systematic literature review and research agenda. Journal of Retailing and Consumer Services,
82, Article 104086. https://doi.org/10.1177/03128962231177096
21. Venderveld, A., Pandey, A., Han, A., & Parekh, R. (2016). An engagement -based customer
lifetime value system for e-commerce. In Proceedings of the 22nd ACM SIGKDD International
Conference on Knowledge Discovery and Data Mining (pp. 293 –302). Association for
Computing Machinery. https://doi.org/10.1145/2939672.2939693
22. Xing, M., Bian, S., Zhao, W. X., Xiao, Z., Luo, X., Yin, C., Cai, J., & He, Y. (2021). Learning reliable
user representations from volatile and sparse data to accurately predict customer lifetime
value. In Proceedings of the 27th ACM SIGKDD Conference on K nowledge Discovery & Data
Mining (pp. 3806 –3816). Association for Computing Machinery.
https://doi.org/10.1145/3447548.3467222
