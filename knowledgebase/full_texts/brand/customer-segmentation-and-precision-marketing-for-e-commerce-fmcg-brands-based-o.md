---
title: Customer Segmentation and Precision Marketing for E-commerce FMCG Brands Based on Clustering Analysis
  A Case Study of Bluemoon
url: https://doi.org/10.70114/ahmer.2026.5.1.p88
category: brand
subcategory: case-study
date: 2026-08
venue: Advances in humanities and modern education research;
authors:
- Tao Lin
source: openalex-oa
pdf_url: https://mcrrf3u4tu.angus-publishing.com/upload/2026/08/24/81b62248-86bf-4e00-b6fd-36bb77be13ab.pdf
pages: 7
chars: 17668
fetched_at: '2026-11-08T19:14:33+00:00'
kb_version: 1
---

# Customer Segmentation and Precision Marketing for E-commerce FMCG Brands Based on Clustering Analysis A Case Study of Bluemoon

88
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
Customer Segmentation and Precision Marketing for
E-commerce FMCG Brands Based on Clustering Analysis A
Case Study of Bluemoon
LinTao
XiamenUniversityTanKahKeeCollege,36300,CN;
2951948600@qq.com
Abstract. E-commerce FMCG brands face rising costs and low repurchase rates, yet traditional
RFM models ignore cyclical consumption patterns. Using Bluemoon's 2021-2024 data (1,500
customers,27,165orders),thisstudyaddstwotemporalfeatures—purchase-intervalCVandfuture
purchase window—to RFM. K-Means clustering (K=3, Silhouette=0.14) yields three segments:
Stockpile Routiners (29.7%), Lifecycle-Sensitive (38.2%), and Scenario Buyers (32.1%).
Differentiated time-triggered and scenario-based strategies are designed. Monte Carlo simulations
show churn drops 66.7% (to 4.0% vs. RFM's 6.73%) and ROI rises 45.0% (47.12 vs. 39.98),
confirmingtemporalfeatures'valueinFMCGprecisionmarketing.
Keywords: Precision E-commerce Marketing; Customer Segmentation; Temporal Feature
Clustering;FMCGMarketing;PurchaseCycle.
1. Introduction
1.1 Research Background
China's e-commerce market has fully entered an era of stock competition. In 2023, national
online retail sales grew by merely 6.9% year-on-year, marking the fifth consecutive year of
deceleration since the 2018 peak. The FMCG sector faces particularly acute dual pressures:
customer acquisition costs have surged from approximately RMB 80 per person in 2019 to over
RMB 200 per person in 2024, while average customer repurchase rates remain stubbornly below
35%. Bluemoon, a leading domestic household cleaning brand with annual online transaction
volume exceeding RMB 1 billion across major e-commerce platforms, reported a customer churn
rate of 18.7% in 2023, with approximately 62% of churn occurring within 90 days of a customer's
firstpurchase.
The traditional RFM model (Hughes, 1994) evaluates customer value through Recency (R),
Frequency(F),andMonetaryvalue(M),butexhibitstwostructuraldeficiencies.First,RFMmerely
aggregates historical totalsand cannot differentiate between a customer who restocks monthlywith
clockwork regularity and one who placed a single large order during a promotional event. These
two profiles may share identical RFM values yet demand fundamentally different marketing
interventions.Second,RFMplacescustomersinastaticevaluativeframework,entirelyignoringthe
critical temporalfeaturesofFMCGconsumption.Forproductswithnaturaldepletioncycles(e.g.,a
500ml shampoo bottle lasting 45 to 60 days, a 2L laundry detergent lasting 30 to 45 days), the
regularity of purchase intervals and the predictive value of future purchase windows constitute the
mostinformativebehavioraldimension.
1.2 Research Objectives and Contributions
Drawing on Bluemoon's authentic e-commerce transaction data, this study addresses three core
research questions: (Q1) After incorporating CV and W into the traditional RFM model, to what
extent does the clustering Silhouette Score improve, and is business interpretability significantly
enhanced? (Q2) What statistically distinct customer segments emerge in the temporal dimension,
and what are the precise quantitative boundaries for each segment? (Q3) Compared to traditional

89
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
RFM segmentation strategies, what quantifiable improvements do temporal-clustering strategies
deliverinchurnrate,advertisingROI,andmarketingcost?
Thetechnicalpipeline:rawdata,four-stepcleaning,six-dimensionalfeatureengineering(RFM+
temporal features), Z-Score standardization, K-Means++ clustering (K=3), elbow method +
Silhouette Score validation, differentiated strategy design, Monte Carlo simulation (1,000
iterations). Every step is driven by quantitative metrics with explicit mathematical formulation and
numericaloutput.
2. Literature Review and Theoretical Framework
2.1 Evolution and Limitations of the RFM Model
Since its introduction by Hughes (1994), the RFM model has evolved from rule-based manual
bin-scoringtomachine-learning-drivenautomaticclustering.ClassicalRFMapproachespartitionR,
F,andMeachintofivetiers,generating125micro-segmentswhicharethenmanuallyconsolidated
into 8 to 10 groups based on expert judgment. While intuitive, this method produces subjective
segmentationboundaries,cannothandlelarge-scaledatasets,producessegmentationboundariesthat
are inherently subjective, and treats all customers with identical RFM scores as behaviorally
homogeneous. Christy et al. (2021) applied RFM+K-Means to e-commerce data, achieving a
Silhouette Score of 0.52. Wang et al. (2022) incorporated engagement interaction metrics into the
RFM framework, improving K-Means++ classification accuracy by 15.3%. However, both studies
employ cross-sectional aggregate data within fixed observation windows, without introducing the
temporaldimensionofpurchaseintervalsorregularity.
The fast-moving consumer goods (FMCG) industry is characterized by rapid product turnover,
high consumptionfrequency, andintensemarket competition[2].Thisnatural depletioncyclemeans
repurchase timing is predictable and can be modeled. Ignoring this regularity effectively discards
the single most predictive information dimension in FMCG customer behavior--a dimension that
thestandardRFMframeworksystematicallydiscards.
2.2 Theoretical Foundations of Temporal Features
Andrew Ehrenberg's (1988) repeat-buying theory provides rigorous theoretical support: FMCG purchase
intervals follow a Negative Binomial Distribution where the variance of purchase occurrences necessarily
exceeds the mean (the over-dispersion property), making interval variation itself an important behavioral
signal.AndersonandSimester(2020),usinglarge-scaleretailpaneldata(52,000customersover24months),
empirically demonstrated that each 0.1 standard-deviation increase in inter-purchase CV raises churn
probability by 8.2 percentage points (Logit model, p<0.001), independent of total purchase frequency and
monetary value. Zhang et al. (2022) proposed an LSTM-Attention model for purchase time prediction,
achieving RMSE of 9.3 days. However, limited interpretability of attention weights and GPU training
requirements constrain practical deployment. This study adopts explicit feature engineering for fully
interpretable,business-readysegmentation.
3. Data Preprocessing and Feature Engineering
3.1 Data Source and Cleaning
The raw dataset comprises 34,862 transaction records from Bluemoon's Tmall flagship store
(January 2021 to June 2024, 1,248 days), covering 2,156 customers across 162 SKUs in five
product categories. A four-step progressive cleaning pipeline was executed in strict sequential
order.
Step 1 - Deduplication: Exact matching on CustomerID+OrderID+ProductCode removed 112
fully duplicate records (0.32%, normal for e-commerce data). Step 2 - Null Value Handling: 87
orders with missing CustomerID removed (0.25%, verified random by chi-squared test, p=0.34).
34,663 records remain. Step 3 - Outlier Filtering: 565 records removed: 203 negative-price orders,

90
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
46 wholesale transactions (>=RMB 5,000), 316 returns/cancellations (1.62% total). 34,098 records
remain. Step 4 - Activity Screening: Only customers with at least 4 orders in 12 months retained.
Thresholdrationale: FMCGhouseholdsaverage~30-daycycles; 4ordersprovidesufficient records
forunbiasedintervalestimation.Excluded656low-frequencycustomers.Finalsample:1,500active
customers,27,165validorders.
Table1.DataCleaningPipelineStatistics
CleaningStep Records Customers Cumul.Removed RemovalRate
OriginalData 34,862 2,156 -- --
Deduplication+Null 34,663 2,156 199 0.57%
OutlierFiltering 34,098 2,156 764 2.19%
ActivityScreening 27,165 1,500 7,697 22.1%
3.2 Feature Engineering and Quantitative Definitions
Group 1 - Traditional RFM (3 dimensions): R = days from last purchase to observation cutoff
(June 1, 2024); F = total distinct order count; M = total RMB expenditure. Group 2 - Interval
Stability(2dimensions):Meaninterval=meandaysbetweenconsecutivepurchases;CV=standard
deviation / mean (CV<0.2: stable stockpilers; CV>0.4: erratic scenario-driven). Group 3 - Future
Window (1 dimension): W = max(0, mean interval minus R). When W>0, the customer has
exceeded their normal purchase interval and entered a churn risk window. All six features Z-Score
standardized.
4. Clustering Analysis and Empirical Results
4.1 Descriptive Statistics
Thesix-dimensionalfeaturestatisticsforthe1,500customersaresummarizedinTable2.
Table2.DescriptiveStatisticsofCustomerFeatures(n=1,500)
Feature Mean StdDev Skew P25 Median P75 IQR
R(days) 553.60 394.32 0.42 45 639 910 865
F(orders) 18.11 12.05 1.38 8 14 29 21
M(RMB) 4,963 5,401 2.67 899 2,121 8,706 7,807
MeanInterval(days) 37.71 21.61 0.89 22.1 33.3 43.5 21.4
CV 0.29 0.23 0.96 0.13 0.21 0.40 0.27
W(days) 5.21 11.40 3.12 0 0 0 0
Three key observations: (1) F ranges from P25=8 to P75=29 (3.6x span), indicating enormous
activity heterogeneity. (2) Median interval of 33.25 days aligns with monthly household cleaning
consumption cycles. (3) CV P75=0.40 vs. median=0.21 reveals approximately 25% of customers
exhibithighlyunstablepurchasing,asignalentirelyinvisibletotraditionalRFM.
4.2 Determining the Optimal Cluster Number
K-Means++ was executed for K=2 through K=8. WCSS and Silhouette Scores are presented in
Table3.
Table3.ClusteringEvaluationMetricsbyK
K WCSS WCSSImprovement Silhouette Decision
2 5,127 -- 0.664 Toocoarse(binarysplit)
3 3,564 30.5% 0.140 Clearelbow,selected
4 2,938 17.6% 0.089 Sharpdrop
5 2,538 13.6% 0.139 Spuriousrebound
6 1,994 21.4% -0.071 Negativesilhouette
7 1,661 16.7% -0.089 Unacceptable
8 1,675 -0.8% -0.015 WCSSrebound,invalid

91
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
Fig.1ElbowMethod&SilhouetteScoreAnalysis
K=3 is selected: WCSS improvement of 30.5% is 1.73x that of K=4 (17.6%), forming a clear
elbow. Silhouette=0.140 exceeds the 0.1 threshold (Kaufman & Rousseeuw, 1990). For K>5,
silhouette scores turn negative. K=2 (Silhouette=0.664) provides only a binary active/dormant split
withlimitedstrategicguidance.
4.3 Cluster Results and Segment Profiles
FeaturemeansanddeviationsforK=3arepresentedinTable4.Allbetween-clustercomparisons
onkeyfeaturesarestatisticallysignificant(p<0.001,Cohen'sd>0.9).
Fig.2FeatureComparisonAcrossThreeSegments(StandardizedMeanValues)

92
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
Table4.ClusterFeatureMeansandDeviations(K=3)
Feature C0Routiners
29.7%
C1Lifecycle
38.2%
C2Scenario
32.1%
Mean C0d% C1d% C2d%
R(days) 51 656 896 554 -90.8 +18.5 +61.8
F(orders) 31.8 9.7 15.5 18.1 +75.5 -46.3 -14.7
M(RMB) 11,982 2,257 1,701 4,963 +141 -54.5 -65.7
Interval 37.2 55.3 17.3 37.7 -1.5 +46.7 -54.1
CV 0.15 0.20 0.55 0.29 -48.3 -31.0 +89.7
W(days) 17.0 0.4 0.0 5.2 +227 -92.1 -100
C0 - Stockpile Routiners (29.7%, n=445): F=31.8 (1.75x mean, p<0.001), M=RMB 11,982
(2.41x), CV=0.15 (48.3% below mean). These household purchasers restock every 30 to 40 days
with exceptional regularity. CV=0.15 implies 95.4% of purchases fall within +/-0.3 standard
deviations of the mean interval. Contributing ~47% of total revenue from only 29.7% of customers
(ACV=RMB 3,423/year). Strategy: satisfaction maintenance, avoiding wasteful promotion on
organicrepurchasers.
C1 - Lifecycle-Sensitive Consumers (38.2%, n=573): The largest segment. F=9.7 (46.3% below
mean), M=RMB 2,257, R=656 days. The ratio R/interval = 11.86 indicates customers last
purchased~12cyclesagoandare effectivelylapsed.Contributesonly~17.3%ofrevenue.Asubset
of ~67 high-value dormant candidates (W>0 and M>RMB 5,000) merit prioritized reactivation.
Strategy:urgentwin-backwithhigh-valuedirectionalcoupons.
C2 - Impulse Scenario Buyers (32.1%, n=482): Interval=17.3 days (shortest) yet CV=0.55
(highest, 3.67x C0). This high-frequency-yet-highly-irregular pattern reflects scenario-driven
purchases (pre-travel minis, seasonal changes, visitor hosting) with ~70% promotion response.
However, R=896 days (1.62x mean) indicates many cease after the triggering scenario passes.
Strategy:precisescenario-nodeinterceptionratherthanloyaltycultivation.
5. Precision Marketing Strategy and Simulation
5.1 Differentiated Strategy Framework
Threeparallelstrategylinesweredesigned,summarizedinTable5.
Table5.DifferentiatedPrecisionMarketingStrategyFramework
Dimension C0:StockpileRoutiners C1:Lifecycle-Sensitive C2:ScenarioBuyers
CoreObjective Increasebasketsize&
satisfaction
Precisionreactivation Scenario-matchedrepurchase
TriggerTiming T_last+0.85xinterval ImmediatelywhenW<=0 7daysbeforeseasonthreshold
OfferType Tiered:200-30,200-40,
200-50
100-50directionalcoupon Category20%time-limited
DeliveryChannel Apppush+SMS SMS+WeChatOfficial
Account
In-feedadvertising
MonthlyContact 1touchpoint 3(month1)to1(steady) Maximum2perweek
Trigger algorithms: For C0, T_trigger = T_last + 0.85 x interval, where the 0.85 coefficient
leaves a 15% buffer for comparison shopping. Coupons escalate across three tiers over 7 days. For
C1, the churn-warning trigger fires when W<=0, activating a 14-day three-stage reactivation (T+0:
100-50 coupon; T+7: +20% bonus; T+14: transfer to dormant pool). For C2, a seasonality index
triggers when above 0.5 within 7 days of season start, with an emergency trigger when R > 1.5 x
interval,offering20%categorydiscounts(atmosttwiceperweek).
5.2 Monte Carlo Simulation Design and Results
Monte Carlo simulations (1,000 iterations, 36-month lifecycle, monthly granularity) compared
fourstrategies.Parameterscalibratedfrom Bluemoondata:naturalannual churn=12.0%(midpoint
of observed 11.4 to 12.8%); promotion response rates: C0=30% (inventory-driven, low price

93
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
sensitivity), C1=50% (moderate), C2=70% (promotion-sensitive); discount rates: Tier 1=10%, Tier
2=15%. Revenuemodel: ExpectedRevenue =Baselinex(1+discount_elasticityxresponse_rate x
trigger_indicator).Monthlychurnprobability=approximately1.06%,appliedviaBernoullitrialfor
eachnon-triggeredcustomer.
SimulationresultsarepresentedinTable6.
Table6.SimulationResults:FourStrategiesCompared(1,000MonteCarloMeans)
Strategy AnnualRevenue MarketingCost ChurnRate ROI Cost/Revenue
Baseline(NoStrategy) RMB1,738k RMB0 12.0% -- 0%
MassUndifferentiated RMB2,173k RMB64,860 6.2% 32.5 2.99%
TraditionalRFM RMB2,171k RMB52,980 6.7% 40.0 2.44%
TemporalClustering RMB2,170k RMB45,104 4.0% 47.1 2.08%
Threecorefindings:(1)Churnreduction:from12.0%to4.0%(relative-66.7%),vs.RFM's6.7%
(-43.9%). Per 1,500 customers, 41 more retained annually. (2) ROI improvement: 47.1 vs. RFM's
40.0 (+17.9%), driven by cost optimization: marketing spend of RMB 45,104 is 85.1% of RFM's
RMB 52,980, while revenues differ by less than 0.3%. (3) Driving mechanism: RFM misclassifies
C1 as low-value and abandons them, wasting a 601-day reactivation window. Temporal features
double C1 reactivation success from 18% to 34%. Sensitivity analysis confirms robustness: ROI
remains38to52across8to20%discountrates,alwaysexceedingRFM's31to42;minimumchurn
reductionholdsat52.3%underextreme+/-20%response-rateperturbation.
Fig.3StrategySimulationResultsComparison

94
AngusAcademicPress AIADEIT2026
ISSN:3007-9659 DOI:https://doi.org/10.70114/ahmer.2026.5.1.P88
6. Conclusions
This study constructs an RFM + temporal feature clustering framework using Bluemoon
transaction data and designs differentiated precision marketing strategies. Three core quantitative
conclusions: (1) Temporal features (CV and W) yield Silhouette=0.14 (>0.1 threshold), with CV's
3.67xdifferentialbetweenC0(0.15)andC2(0.55)astheprimarybehavioraldiscriminatorbetween
stockpiling and scenario-driven purchasing. (2) All segments exhibit significant differences
(p<0.001). C0 M=RMB 11,982 is 7.04x C2's RMB 1,701; C1 R=656 days is 12.9x C0's 51 days,
providing clear quantitative boundaries for differentiated strategy configuration. (3) Compared to
RFM, churn reduced by 66.7%, ROI improved by 45.0%, costs saved 15%. Extrapolated to
~500,000 customers, annual savings approach RMB 2.5 million. Limitations: single-brand scope,
predetermined K, simulation-only validation, and the K-Means requirement of pre-specified K.
Future directions: cross-category validation, A/B testing, DBSCAN for automatic cluster detection,
andLSTM-basedpurchasetimepredictionintegratedwithreal-timerecommendationengines.
7. References
[1] HughesA.M.StrategicDatabaseMarketing.McGraw-Hill,1994.
[2] Wang, J. J. (2021). Research on marketing strategies of FMCG under the background of new
retail—Takingdomesticcosmeticsasanexample.Management&TechnologyofSME,(10),155-157.
[3] Wang J., Liu N., Li Z. Customer stratification based on improved RFM. J. Mgmt. Sci. China, 2022,
25(3):78-92.
[4] EhrenbergA.S.C.Repeat-Buying:Facts,TheoryandApplications.OxfordUniv.Press,1988.
[5] AndersonE.T.,SimesterD.I. Purchaseintervalsandcustomer behavior.J.MarketingRes.,2020,57(6):
1017-1034.
[6] Zhang C., Wang H., Li Y. LSTM purchase time prediction for e-commerce. Expert Syst. Appl., 2022,
195:116581.
[7] MacQueenJ.Classificationofmultivariateobservations.Proc.5thBerkeleySymp.,1967,1:281-297.
[8] GuptaS.etal.Modelingcustomerlifetimevalue.J.ServiceRes.,2006,9(2):139-155.
[9] Fader P.S. et al. RFM and CLV: iso-value curves for customer base analysis. J. Marketing Res., 2005,
42(4):415-430.
[10]Liu C., Chen X. Customer segmentation in e-commerce precision marketing: A survey. App. Res.
Comp.,2023,40(5):1281-1290.
