---
title: IMPLEMENTATION OF PREDICTIVE MODELLING OF PRESCRIPTION GROWTH THROUGH MARKETING MIX MODELLING
url: https://doi.org/10.17148/ijireeice.2026.14370
category: analytics
subcategory: measurement
date: 2026-03
venue: IJIREEICE
authors:
- Selvapujith T
- Mohamed Athfan D
source: openalex-oa
pdf_url: https://doi.org/10.17148/ijireeice.2026.14370
pages: 8
chars: 30662
fetched_at: '2026-11-08T17:06:05+00:00'
kb_version: 1
---

# IMPLEMENTATION OF PREDICTIVE MODELLING OF PRESCRIPTION GROWTH THROUGH MARKETING MIX MODELLING

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  408
IMPLEMENTATION OF PREDICTIVE
MODELLING OF PRESCRIPTION
GROWTH THROUGH MARKETING MIX
MODELLING

Selvapujith T1, Mohamed Athfan D2
M.Sc. Data Science and Business Analysis Rathinam College of Arts and Science Coimbatore, Tamilnadu, India 1
Department of Computer Science Rathinam College of Arts and Science Coimbatore, Tamilnadu, India 2

Abstract: The pharmaceutical assiduity is faced with a grueling question moment how can they effectively spend
their marketing budget while adding the number of prescriptions?  This exploration proposes a result to this problem
by using data - driven prognostications to identify which marketing sweats are  actually effective.  We’ve designed
a system that analyzes different marketing sweats similar as deals representatives  visiting croakers, free samples,
online advertising, medical conferences, and special juggernauts to identify their factual effectiveness  on the number
of conventions written.  Our system uses statistical analysis and intelligent features that  consider delayed goods(
since marketing doesn’t work incontinently)  and long- term goods( since moment’s advertising can impact
hereafter’s opinions).  The system analyzes the literal data of conventions and marketing spending, cleans the data,
and generates prophetic models that can actually tell marketers what works. We’ve enforced our system and created
visual interfaces that help interpret the result s. The analysis demonstrates that online marketing is a crucial factor
affecting and direct marketing to croakers are the most effective, and more intelligent budget allocation can increase
returns by 15 – 20 chance points. This system provides a foundation for pharmaceutical marketers to make informed
opinions grounded on real substantiation.

Keywords: Market Mix Modeling, Prescription Growth, Regression Analysis, Adstock, ROI Optimization, Feature
Engineering, Pharmaceutic al Marketing, Predictive Analyt ics.

I. INTRODUCTION

1.1 Industry Context and Challenges
On a global position, the pharmaceutical sector is honored as a largely influential and essential assiduity
economically important and competitive sectors, with annual marketing spending exceeding hundreds of billions
of bones worldwide. Recent assiduity analyses reveal that the current top medicinal companies allocate around 25
– 30channels to direct croaker engagement conditioning involving face - to- face educational m eetings with
healthcare professionals, complimentary product sample distribution to support trial operation and case
inauguration, sophisticated online marketing juggernauts exercising social media plat - forms and online advertising,
participation in medical conferences and continuing medical education programs, and other marketing conditioning
similar as patient mindfulness juggernauts and healthcare professional engagement activities. Notwithstanding the
massive spending commitments and marketing strategi c significance, pharmaceutical companies continue to face
challenges in precisely measuring the individual channel donation to overall tradition volume growth. This is due
to a number of introductory challenges and issues lapping time goods whereby multipl e marketing sweats
contemporaneously affect defining geste , delayed response goods whereby marketing exposure is reflected in
tradition geste weeks or months after marketing exposure,non - linear relations between multiple marketing channels
creating syner gistic or negative goods, external confounding variables similar as competitive conduct and
nonsupervisory changes, and the introductory difficulty of establishing unproductive connections in marketing data
[1].

1.2 Limitations o f Traditional Approaches
Traditional approaches to marketing effectiveness evaluation are primarily grounded on literal correlation analysis
or simple retrogression modeling approaches that aren’t sophisticated or effective enough to duly capture the
intricate temporal dynamics and accretive processes involved in pharmaceutical marketing conditioning [ 3]. These
traditional styles have a number of critical limitations that render them ineffective for strategic decision - timber.

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  409
First, traditional correlation analysis can not duly distinguish between unproductive and spurious correlations due
to the presence of confounding variables or temporal association. A detailing visit to a croaker may not affect
defining geste until several  weeks latterly when the croaker sees suitable patient cases. Digital marketing
juggernauts may take months to inclusively make mindfulness and trust before affecting tradition opinions.
Traditional models that don’t regard for these lagged goods totally u nderrate the factual effect of marketing
investments.

1.3 Research Objectives and benefactions
To effectively overcome these significant methodological and practical difficulties, this exploration work proposes
and validates a comprehensive request Mix Modeli ng frame knitter- made for pharmaceutical tradition soothsaying
and marketing optimization.

Market Mix Modeling is a quantitative logical methodology that totally assesses and forecasts the effect of
marketing channels on business issues through rigorous statistical modeling of literal data. The final thing is to give
a strong, interpretable, and practical prophetic methodology that statistically quantifies individual channel goods,
produces accurate tradition vaticinations at colorful situations of granul arity, and provides strate - gic perceptivity
to grease data - driven marketing cub - progeny allocation. This frame improves organizational decision - making
capacities while icing effective use of marketing coffers, therefore leading to increased profit gene ration and, in
turn, sustainable compet - itive advantage.

LITERATURE SURVEY AND RESEARCH GAP

1.4 Literature Survey
There have been attempts to probe the operation of Market Mix Modeling MMM and data - driven approaches to
estimate the effectiveness of marketin g. Hanssens et al. intro - duced classical retrogression - grounded MMM to
demon- strate the significance of mar - keting conditioning in shaping demand [ 3]. Lim et al. used machine literacy
algorithms like Random Forest and Grad ient Boosting to enhance the delicacy of prognostications in
pharmaceutical marketing analytics [ 8]. Google’s MMM frame emphasized the sig - nificance of adstock and
carryover goods in modeling the lagged goods of marketing [ 6]. Yang et al. examined the operation of distributed
pause and adstock models to measure the continuity of marketing goods. Other studies have emphasized the
significance of point engineering and business intelligence dashboard ing for enhanced man - agerial deci - sion
support [7]. While these studies establish the significance of analytics in marketing, utmost of the being literature
either concentrate on delicacy or interpretability, but not both to gether in an intertwined frame.

1.5 Research Gap
From the literature check over, it has been noted that there’s a gap in the being literature for an intertwined end - to-
end result that combines point engineering, adstock modeling, time pause modeling, formal ized retrogression analy-
sis, and business intelligence dash - boarding for pharmaceu - tical tradition soothsaying. The being literature does
n’t duly address multicollinearity, lagged goods, and business interpretability contemporaneously. There’s a bear -
ment for a strong, accurate, and interpretable prophetic MMM frame, which is fulfilled in this exploration work.

II. PROPOSED SYSTEM

The proposed system in this exploration work is an end - to- end prophetic request Mix Modeling MMM system
that aims to dissect, prognosticate, and optimize tradition growth in the pharmaceutical assiduity. The proposed
system com- bines data engineering, ma- chine literacy modeling, and business intelligence visualization as a single
logical process.

The main ideal of this proposed system is n’t only to prognosticate unborn tradition vol - ume but also to measure
the donation of each marketing channel, prisoner delayed and accretive marketing impacts, and give strategic
decision support for marketing budget allocation.

2.1System Overview
The proposed system’s overall process starts with the colle ction of literal data from col - orful enterprise sources
similar as deals databases, client relationship operation CRM systems, and marketing crusade operation soft -
earthenware. These sources of data gener - ally store information aboutproduct -wise andregi on-wise tradition
volumes,channel -wise marketing expenditures, and other external control variables similar as seasonality and
competitive activ - ities. The reused data is also fed into the machine learn - ing modeling element, where three

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  410
retrogression mod els are erected Linear Regression, Ridge Regres - sion, and Lasso Regression. Linear
Retrogression is used as a birth model, while Ridge Regression and Lasso Regression are used to handle
multicollinearity in marketing vari - ables and to stabilize and inter pret the results [ 2,4,5]. The three models com -
bined form the vaticination machine of the proposed system. This machine has the capability to produce unborn
tradition vaticinations at colorful situations of detail, including product - wise, region -wise, andtime -wise
vaticinations. likewise, the model portions are used to calculate channelposition donation and return on investment
ROI, which are essential for marketing performance evaluation. Eventually, the logical results are combined into a
visualization subcaste erected on Power BI [ 7]. The visualization subcaste displays the results in the form of
interactive dashboards, similar as trad ition trend maps, channel donation heatmaps, ROI comparison maps, and
crucial performance index KPI cards. These interactive dashboards enable business druggies to interactively dissect
the data, drill down into the data, and compare different strategic op tions without demanding any specialized
knowledge.

Figure 1: Architecture Design System

2.2 Architecture Description
The armature of the proposed system is organized in a modular and layered fashion, icing scalability, flexibility,
and maintainability. The system has the following primary factors

1) Data Ingestion Subcaste: This subcaste is assigned with ingesting data from different sources similar as deals
systems, CRM systems, and marketing databases. The data can come in different f orms and at different intervals,
and this subcaste ensures that all the data is combined into a single logical dataset.

2) Preprocessing Subcaste: In this subcaste, the raw data is gutted and regularized. Missing data is addressed
using the right insinuation styles, outliers are iden- tified and addressed, and variables are converted into formalized
units and formats. This subcaste ensures that the data is accurate and amenable to modeling.

Figure 2: Sample Dataset

3) point Engineering Layer: This subcaste ex tends the dataset by creating new ex - plicatory variables similar
as pause variables, adstock variables, and commerce terms. These variables enable the system to dissect the time -
dependent, accretive, andcross - channel goods of marketing conditioning.
4) Modeling Subcaste: The modeling subcaste trains a variety of retrogression - grounded machine literacy
models similar as Linear Regression, Ridge Regression, and Lasso Re - gression. The models are trained using literal
data, and hyperparameters are designed to be optimal for prophetic performance and conception.
5) vaticination and Analytics Layer: This subcaste employs the trained models to produce unborn tradition
fore- casts and channel- position benefactions, ROI, and perfor - mance criteria . This is the centra l logical machine

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  411
of the system.
6) Visualization and Decision Support Subcaste: The final subcaste is responsible for the donation of the
results using Power BI dashboards, which allow marketing directors and decision - makers to dissect results and
make strategic opinions.

2.3Marketing Budget Distribution
The commensurable distribution of marketing expenditure across fo ur major channels television, Digital,
Programmatic, and publish media. It’s observed that television ad - vertising dominates the total marketing budget,
account for 45.1% of the total spend, indicating that TV remains the primary medium for mass outreach and brand
visibility. Digital marketing contributes 30.9% of the total cub - progeny, pressing the adding signif- icance of online
and performance - driven platforms in targeted followership engagement and measurable crusade effectiveness.
Programmatic adver tising accounts for 17.7% of the expenditure, reflecting the association’s relinquishment of
automated and data - driven media buying strategies. publish media represents only 6.2% of the total spend,
showinga declining reliance on traditional print channel s due to lower reach and limited perfor - mance track - ing
capabilities. Overall, television and Digital channels to - gether account for further than 76% of the total marketing
budget, indicating a strong strategic focus  on high - impact and high - reach platforms.  This budget distribution
forms the base for farther analysis in the Marketing Mix Model to quantify the donation and  return on investment(
ROI) of each channel toward tradition growth.

MATHEMATICAL EXPRESSION OF MARKET MIX MODELING AND PREDICTIVE MODELS
Figure 3: Mathematical Architecture of Market Mix Modeling

2.4General Market Mix Modeling Equation
The primary ideal of Market Mix Modeling( MMM) is to represent tradition volume as a function  of multiple
marketing- related andnon-marketing-related factors. Let  Yt denote the number of prescriptions at time t; Xi,t
represent the i-th marketing channel such as detailing, digital advertising, or sampling.
Yt = β0 +
Σ
βiXi,t +
Σ
γjZj,t + ϵt (1)
i j
where β0 is the intercept( birth conventions without marketing), βi represents the in - cremental donation of the
i-th marketing channel, γj represents the impact of con - trol variables.  This equation decomposes total
conventions into birth, marketing - driven, external goods.

2.5Matrix Form of Regression Model

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  412
2
ridge
For computational convenience, the model is written in matrix form

Y = Xβ + ϵ (1)

2.6Ordinary Least Squares Linear Regression
The objective of linear regression is to find coefficients that minimize the residual error

min
β
 Y − Xβ
2 (2)
Or in matrix form, the closed-form solution is
βˆ = (XT X)−1XT Y (2)

Interpretation in MMM Context:  Each βi tells how many prescriptions increase for one unit increase in that
channel spend.  However, when marketing channels are correlated, XT X becomes ill-conditioned (unstable
coefficients). This leads to the need for regular ization.
2.7Ridge Regression L2 Regularization
To control multicollinearity  and overfitting, Ridge Regression adds a penalty term

min Y − Xβ  2 + λ  β  2 (3)
β 2 2
The solution becomes
βˆ = (XT X + λI)−1XT Y (4)
Meaning in MMM: Shrinks coefficients of less important channels. Stabilizes the model when channels are
highly correlated. Keeps all channels but reduces their magnitudes.
2.8Lasso Regression L1 Regularization
Lasso introduces absolute value penalty

min
β  Y − Xβ  2 + λ  β  1 (4)

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  413
n
q Σ
n
Interpretation: α = 0.7 means 70% of last week’s effect carries forward. Captures memory effect of advertising.
2.10Time-Lag Variables
Sometimes effect appears after a fixed delay

Yt = β0 + β1Xt−1 + β2Xt−2 + . . . (6)

This models short-term, medium-term, and long-term effects independently.
2.11Final Combined MMM Equation
Yt = β0 +
Σ
βiAi,t +
Σ
γjLj,t + ϵt (7)
i j
Where Ai,t = Adstocked and Lj,t = lagged marketing variables.\
2.12Loss Functions
1. Mean Squared Error MSE:  1 Σ(yi − yˆi)2
n

2. Root Mean Squared Error RMSE: 1 (yi − yˆi)2
3. Mean Absolute Error MAE: 1 Σ |yi − yˆi|
2.13Goodness of Fit R2 Score
R2 measures how much variation is explained by the model.  R2 = 0.85 means 85% of prescription variation is
explained.
2.14Example Numerical Interpretation
If βdetail = 0.45, then 1 unit increase in detailing →  0.45 prescriptions; 1 unit increase in digital → 0.35
prescriptions.
2.15Non-Linear Machine Learning Models
To capture complex non -linear relationships and interactions between marketing channels, advanced machine
learning models such as Random Forest and XGBoost are employed [ 9, 10]. These models are capable of learning
high-dimensional, non-linear decision functions and automatically modeling interaction effects among variables.
The general form of a non-linear predictive model can be expressed as
Yˆt = f (Xt) (6)
where Yˆt  denotes the predicted number of prescriptions at time t, Xt represents the vector of input features
including marketing and control variables, and f (·) is a non- linear function learned from the training data.

III. FINAL RESULTS AND INSIGHTS

The experimental results clearly show that the proposed Predictive Market Mix Modeling approach is successful in
predicting the prescription trend and measuring the effect of var - ious marketing channels.  Compared to the baseline
Linear Regression model, the Ridge and  Lasso regression models perform better in terms of stability and
interpretability,  especially when there are correlations among the marketing variables [4,5]. The addition of adstock
and time lag variables has a substantial effect on improving the accuracy of the predictions,  which proves that the
delayed and cumulative effects of marketing activities are important factors to be considered.

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  414

The analysis of the coefficients and contrib ution scores of the models offers important insights into the effectiveness of
marketing channels. It is noticed that some channels, such as doctor detailing and digital marketing, are more effective
and have a strong positive effect on the growth of prescriptions, while others have a short-term effect. The Power
BI dashboard also assists in understanding the prescription trend, seasonality, and ROI of marketing channels,
which makes it easier to interpret the results of the analysis [7]. In summary, the proposed system not only provides
accurate predictions but also offers important insights that help in making data-driven marketing decisions.

IV. BUSINESS IMPACT FOR PHARMACEUTICAL COMPANIES

The proposed framework provides substantial business value for pharmaceutical compa nies by enabling the use of
historical marketing data for strategic decision -making. The framework enables pharmaceutical companies to make
informed decisions on high-impact and low-impact marketing channels, thereby allowing them to optimize their budget
allocation and maximize ROI. The proposed framework provides pharmaceutical companies  with accurate prescription
predictions, thereby enabling them to optimize their demand planning, inventory management, and field force
management. In addition, the proposed framework provides decision-makers with the capability to perform scenario
analysis, such as analyzing the potential impact of increasing or decreasing spending on a give n marketing channel.
Likewise, the proposed framework provides decision -makers with the capability to interpret the results of regression -
based models, which is particularly im portant in the pharmaceutical industry, which is highly regulated.  In conclusion,
the proposed framework provides substantial business value to pharmaceutical companies by enabling them to optimize
their cost, performance, and strategy.

a. Strategic Scenario Planning
The proposed framework provides decision -makers with the capability to perform strate gic scenario planning, which
enables them to analyze different marketing strategies and their potential impact before allocating resources. For instance,
what if the dig ital marketing budget is increased by 30%?  The framework can extend the strategic scenario
planning capabilities by incorporating parameter uncertainty, which would provide prob- ability distributions of
outcomes rather than point estimates. Marketing managers would be able to analyze not only the potential impact
but also the best -case and worst -case scenarios.

The pharmaceutical sector is subject to strict regulatory scrutiny, with a need for trans parency and justification of
marketing strategies.  Statistical models grounded in historical experience can offer sound justification for marketing
strategies, showing that resource allocation is made through objective analytical processes rather than subjective choices.
The interpretability of models is especially useful in a regulatory setting. The coefficients of ridge regression are
easily interpretable in business terms as incremental prescription effects, which can be easily explained to regulatory
bodies, auditors, or attorneys. This is not possible in black -box machine learning models, which, while potentially
better at prediction, cannot explain why specific recommendations are made. In addition to di- rect decision-making,
the model framework also provides for systematic organizational learning  about the effectiveness of marketing.
Through periodic model updates using new data, changes over time in the effectiveness of marketing channels can be
captured, enabling adaptive strategies that take into account changes in the market environment. Performance monitoring
dashboards enable quick identification of anomalies in patterns of performance, enabling investigation and corrective
action. If actual prescriptions do not match predictions despite the execution of marketing plans, the organization can
quickly identify problems —perhaps competitor activity, regulatory changes.  The docu mentation of assumptions,
methods, and findings of models provides for organizational knowledge that is not dependent on workforce.  New
marketing managers can refer to previous  analyses for what worked and why, enabling them to quickly become
effective and avoiding repetition of previous mistakes.

V. CONCLUSION  AND FUTURE SCOPE

a. Conclusion
This study has provided a complete predictive Marketing Mix Modeling (MMM) frame - work for the analysis and
forecasting of prescription growth in the pharmaceutical  industry. The proposed system combines data
preprocessing, feature extraction, regression - based machine learning models, and interactive visualization into a
single analytical process. By incorporating adstock and time -lag consideration s, as well as Ridge and Lasso
regularization, the system efficiently addresses multicollinearity  and enhances both pre- diction accuracy and model
robustness. The experimental outcomes indicate that the proposed system provides accurate predictions and
valuable insights into channel -level contributions and ROI. The integration with Power BI dashboards further
improves the practical usability of the system by enabling business users to explore trends, compare strategies, and

ISSN (O) 2321-2004, ISSN (P) 2321-5526

IJIREEICE
International Journal of Innovative Research in Electrical, Electronics, Instrumentation and Control Engineering
Impact Factor 8.414Peer-reviewed & Refereed journalVol. 14, Issue 3, March 2026
DOI:  10.17148/IJIREEICE.2026.14370
© IJIREEICE              This work is licensed under a Creative Commons Attribution 4.0 International License                  415
make data -driven decisions.  In summary, the proposed system clearly indicates that a properly designed MMM
framework can be used as a highly effective decision -support system for pharmaceutical marketing optimization.

b. Future Scope
Although the proposed system provides promising results, several possible extensions can be considered for future work.
More advanced machine learning models, such as Gradient Boosting, Random Forests, and deep learning models, can be
explored to better model complex non -linear relationships. The proposed framework can also be extended to pro - vide
near real-time data integration and dynamic model updates. In addition, future research can be conducted to incorporate
external considerations, such as competitor ac tivity, policy c hanges, and epidemiological trends, to further enhance
prediction accuracy. Scenario simulation and budget optimization modules can also be incorporated to further enhance
the system from a predictive tool to a prescriptive decision-support platform.
Apart from the internal marketing factors, the future developments of the system can also include external impacting
factors such as competitor promotional activities, regula tory and policy changes, seasonal patterns, and epidemiological
trends to further enhance the accuracy and robustness of the prediction models. The integration of the scenario simulation
and the automatic budget optimization modules can therefore enable the sys tem to transform from a predictive tool
into a prescriptive decision-support platform. A major and highly influential extension of this research work is
the development of an AI-driven interactive chatbot interface built on top of the trained Marketing Mix Model.  This
intelligent decision-support tool would enable the decision-makers to interact with the system using natural language
statements such as ”What will be the prescriptions if television  spend is reduced by 10%?”, ”What is the channel
with the highest ROI?”, or ”How should the next quarter’s budget be allocated?”

The chatbot would also interpret the user inputs, convert them to model inputs, per - form simulations using the trained
model, and provide data -driven, actionable answers to the user queries based on the predicted outcomes and past
performance. This interactive decision-support system would therefore enable the non-technical stakeholders such
as the marketing managers and business directors to access the advanced analytics without having  to directly interact
with the dashboards and code. Further, the chatbot can also be developed with explanation modules to explain the
recommendations made by the chatbot by providing channel-wise contributions, response curves, and confidence levels.
This development would therefore enable the proposed system to transform into a completely intelligent, interactive, and
explainable marketing analytics platform for strategic planning and policy formulation.

REFERENCES
[1]. O. I. Kostyuk,  A. S. Krasnikova,  and M. A. Poltavskaya,  ”Marketing Mix Modeling  for Pharmaceutical
Companies on the Basis of Data Science Technologies,” in Pro- ceedings of the International Scientific
Conference on Innovations in Data Science , 2021.
[2]. D. C. Montgomery, E. A. Peck, and G. G. Vining, Introduction to Linear Regression Analysis , 5th ed.
Hoboken, NJ, USA: Wiley, 2012.
[3]. D. Hanssens, L. Parsons, and R. Schultz, Market Response Models Econometric and Time  Series Analysis.
Boston, MA, USA: Kluwer Academic Publishers, 2001.
[4]. R. J. Tibshirani, ”Regression shrinkage and selection via the Lasso,” Journal of the Royal Statistical Society,
Series B, vol. 58, no. 1, pp. 267 –288, 1996.
[5]. A. E. Hoerl and R. W. Kennard, ”Ridge regression Biased estimation for nonorthog - onal problems,”
Technometrics, vol. 12, no. 1, pp. 55 –67, 1970.
[6]. Google, ”Lightweight MMM A scalable approach to marketing mix modeling,” Google Research
Whitepaper, 2020.
[7]. Microsoft, ”Power BI documentation,”  Microsoft Corporation, 2022.
[8]. T. Lim, A. Kannan, and A. Sinha, ”Predictive analytics in pharmaceutical mar - keting,” International Journal
of Pharmaceutical Management , vol. 10, no. 2, pp. 45 –56, 2018.
[9]. L. Breiman, ”Random forests,” Machine Learning, vol. 45, no. 1, pp. 5–32, 2001.
[10]. T. Chen and C. Guestrin, ”XGBoost: A scalable tree boosting system,” in Proc. 22nd ACM SIGKDD
Int. Conf. Knowledge Discovery and Data Mining , 2016, pp. 785–794.
