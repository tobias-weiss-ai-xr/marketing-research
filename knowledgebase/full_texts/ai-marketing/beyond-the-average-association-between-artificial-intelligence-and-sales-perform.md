---
title: Beyond the average association between artificial intelligence and sales performance
url: https://doi.org/10.1007/s44163-026-02543-y
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: Discover Artificial Intelligence
authors:
- Cüneyd İkbal SARIOĞLU
- Chané  of de Bruyn
- Rıdvan Karacan
source: openalex-oa
pdf_url: https://link.springer.com/content/pdf/10.1007/s44163-026-02543-y.pdf
pages: 18
chars: 58590
fetched_at: '2026-11-08T20:06:28+00:00'
kb_version: 1
---

# Beyond the average association between artificial intelligence and sales performance

Discover Artificial IntelligenceSarıoğlu et al. Discover Artificial Intelligence          (2026) 6:1627
https://doi.org/10.1007/s44163-026-02543-y
RESEARCH Open Access
Beyond the average association between
artificial intelligence and sales performance
Cüneyd İkbal Sarıoğlu1, Chané de Bruyn2,3* , Rıdvan Karacan4 , Eda Yalçın Kayacan5 and Sema Yılmaz6
  * C o r r e s p o n d e n c e :
Chané de Bruyn
chanedb@uj.ac.za; chane.debruyn@
alu.uhu.es
1Marketing Department, University
of Kocaeli, Kocaeli, Turkey
2Centre for Local Economic
Development, College of Business
and Economics, University of
Johannesburg, Johannesburg,
South Africa
3University of Huelva, Huelva, Spain
4Department of Economics,
Marshall Campus, University of
Kocaeli, Kocaeli, Turkey
5Department of Statistics and
Econometrics, Faculty of Science,
Pamukkale University, Denizli,
Turkey
6Department of Economics, Yildiz
Technical University, Istanbul,
Turkey
© The Author(s) 2026. Open Access  This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International
License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate
credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material.
You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party
material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material
is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted
use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit  h t t p :  / / c r e a  t i v e c  o m m o  n s . o r g / l i c e n s
e s / b y - n c - n d / 4 . 0 /     .
Abstract
The assumption that AI-driven marketing technologies uniformly improve sales
performance remains insufficiently tested. Using an exploratory synthetic firm-
level dataset (n = 50), this study estimates OLS and quantile regressions at tau =
0.10, 0.25, 0.50, 0.75, and 0.90, with 2000-replication pairs-bootstrap inference. A
data-integrity audit showed that marketing efficiency and revenue per salesperson
are deterministic functions of revenue growth and were therefore excluded from
the inferential models to prevent target leakage. In the corrected specification,
automated lead generation is negatively associated with revenue growth in OLS
and at Q75 and Q90, with 95% bootstrap confidence intervals excluding zero. AI
usage, marketing budget, sales-team size, and personalized campaigns have wide
bootstrap intervals that include zero at every reported quantile. Huber and ridge
estimates preserve the OLS coefficient signs but differ in magnitude, underscoring
the exploratory nature of the results. The study contributes a cautious, distribution-
sensitive assessment and identifies priorities for validation with larger, real-world data.
Keywords AI-driven sales, Revenue growth, Quantile regression, Bootstrap inference,
Robust regression
JEL Classification M31, O33, L86, C21
 1 Introduction
Artificial intelligence (AI), machine learning (ML), and advanced data analytics have
rapidly transformed the landscape of digital marketing and sales, triggering a substan -
tial expansion in both academic research and practical applications [ 6]. In increasingly
competitive and data-intensive business environments, firms are under growing pres -
sure to adopt AI-driven technologies to enhance decision-making, improve operational
efficiency, and sustain competitive advantage [ 1]. In this context, AI-powered market -
ing technologies have emerged as critical tools for optimizing sales force performance
by automating routine processes, generating actionable customer insights, and enabling
more precise, data-driven strategies [ 49, 50]. From predictive analytics to personalized
outreach [45], AI is fundamentally reshaping sales operations and allowing sales teams
to shift their focus toward higher-value activities such as relationship management and
strategic planning [35].

Page 2 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
Traditional sales technologies, including sales force automation (SFA) and customer
relationship management (CRM) systems, have evolved significantly with the integra -
tion of AI capabilities [ 7]. These enhanced systems facilitate more effective lead genera -
tion, improve forecasting accuracy, and streamline customer engagement processes [ 49,
50, 55]. By refining sales pipelines, prioritizing high-value prospects, and reducing inef -
ficiencies in resource allocation, AI contributes to improved productivity and organi -
zational responsiveness in dynamic market conditions [ 57]. As a result, AI adoption is
often associated with superior sales performance and increased organizational agility.
Beyond operational efficiency, AI also plays a strategic role in shaping customer rela -
tionships and long-term value creation. Through large-scale data analysis, behavioral
prediction, and personalized interaction design, AI supports customer loyalty strategies
and enhances decision-making in product and market planning [ 31, 38, 56]. AI-driven
segmentation enables firms to tailor their offerings more effectively, thereby improving
customer satisfaction, retention, and conversion rates [ 44]. Importantly, the prevailing
perspective in the literature conceptualizes AI not as a substitute for human sales agents
but as a complementary technology that augments human capabilities [ 10]. By automat-
ing data-intensive tasks, AI enables sales professionals to focus on empathy-driven com -
munication, complex negotiation, and relationship-building activities [19].
From a broader perspective, AI-driven marketing technologies can also be conceptual-
ized as data-driven decision support systems that enhance managerial decision-making
processes. This study is motivated by the need to move beyond the assumption that AI-
driven marketing technologies automatically enhance sales performance. Although AI
is widely presented as a source of efficiency, predictive accuracy, and improved decision
support, managers still face uncertainty about whether these technologies generate the
same value at different positions in the conditional revenue-growth distribution.
Despite these advancements, the assumption that AI adoption universally enhances
sales performance remains insufficiently scrutinized. While AI systems excel at process -
ing large datasets, identifying patterns, and forecasting customer behavior [ 37, 40], they
may also introduce new challenges related to over-automation, misalignment with orga -
nizational processes, and reduced flexibility in decision-making. The human element,
particularly emotional intelligence, trust-building, and contextual judgment, remains
indispensable in complex sales environments [19, 41]. Consequently, the effectiveness of
AI in sales is likely to depend not only on technological capabilities but also on how well
these technologies are integrated with human expertise. The core problem addressed in
this study is therefore not merely the limited empirical attention given to AI in sales con-
texts, but the lack of clarity about when AI enhances performance and when it may cre -
ate diminishing returns through over-automation, weak organizational integration, or
reduced reliance on human judgment.
Although research has documented AI applications in marketing, CRM, personaliza -
tion, and forecasting [9, 10, 27, 32], three issues remain underdeveloped. First, most evi -
dence is usually reported as a single average effect (aggregate) and therefore says little
about how associations differ across the conditional distribution of sales performance.
Second, studies often discuss implementation risks without testing whether the sign or
magnitude of AI-related coefficients varies between lower- and upper-performing firms.
Third, macroeconomic, industry, consumer, and organizational conditions are rarely

Page 3 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
integrated into the same empirical framework. These omissions motivate a distribu -
tional, explicitly contingent analysis.
This study addresses the first two gaps by estimating how the associations of AI usage,
automated lead generation, marketing budget, sales team size, and personalized cam -
paigns vary across revenue-growth quantiles. Marketing efficiency is retained only as
a descriptive diagnostic because the supplied measure is revenue growth divided by
marketing budget and would therefore introduce target leakage if used as a regressor.
The quantiles describe positions in the conditional distribution of revenue growth; they
should not be interpreted as direct measurements of organizational age, industry life-
cycle stage, or a firm's longitudinal development stage.
The study makes three bounded contributions. First, it reframes AI-driven market -
ing technologies as decision-support resources whose associations with performance
may vary across the revenue-growth distribution. Second, it links this heterogeneity to
dynamic-capability and socio-technical arguments about organizational fit and human-
AI complementarity, while avoiding claims that the present data directly test those
mechanisms. Third, it provides an exploratory simulation framework that makes omit -
ted contextual factors and replication requirements visible. The contribution is therefore
analytical and hypothesis-generating, not causal or population-representative.
The remainder of the paper is structured as follows. The next section reviews the rel -
evant literature and develops the hypotheses. The methodology section then outlines
the data and empirical approach, followed by separate Results and Discussion sections.
Managerial and policy implications are presented before the study's limitations and a
concise conclusion.
2 Literature review
Artificial intelligence (AI)-driven marketing technologies can be conceptualized as data-
driven decision support systems (DSS) that augment managerial decision making. By
processing customer and market data, AI tools may support sales and marketing deci -
sions, but their associations with performance can vary across the conditional outcome
distribution and across organizational contexts. Conditional quantiles are used here as
distributional positions, not as measures of firm age or life-cycle stage.
The integration of artificial intelligence (AI) into sales and marketing has attracted sig-
nificant scholarly attention in recent years, with a growing body of research examining
its implications for sales force performance, customer engagement, and firm-level out -
comes. Existing literature highlights multiple dimensions through which AI transforms
marketing and sales processes, ranging from automation and predictive analytics to per -
sonalization and human–AI collaboration.
One of the earliest and most influential applications of AI in sales lies in the evolu -
tion of Sales Force Automation (SFA) and Customer Relationship Management (CRM)
systems. Originally developed to streamline administrative tasks and organize customer
data, these systems have evolved into AI-enhanced platforms incorporating predictive
analytics and automated decision-making capabilities. Agnihotri [ 2] emphasizes the
fragmented nature of research in this domain and calls for a comprehensive perfor -
mance framework to evaluate returns on investments in CRM, digital media, and AI
technologies. Similarly, Kumar et al. [ 28] argue that emerging technologies such as AI,
machine learning, IoT, and blockchain significantly enhance CRM capabilities, while

Page 4 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
Vignesh and Vasantha [58] highlight the transformative role of big data and analytics in
overcoming the limitations of traditional CRM systems. Libai et al. [ 29] further suggest
that AI-driven CRM systems improve customer acquisition, development, and reten -
tion by enabling more accurate predictions of customer lifetime value. Additionally,
Liu-Thompkins et al. [ 30] introduce the concept of artificial empathy, emphasizing its
potential to create value for customers and firms while also noting that it may be unnec -
essary or even harmful in some situations.
Predictive analytics represents another critical dimension of AI adoption in sales. By
leveraging machine learning algorithms, firms can forecast demand, identify high-poten-
tial leads, and optimize resource allocation. Venkataramanan et al. [55] review AI-driven
forecasting techniques in CRM systems and report that they can improve sales forecast -
ing accuracy. At the same time, Enholm et al. [ 11] note that the value firms obtain from
AI depends on technological, organizational, and environmental enablers and inhibitors
of adoption and use. Amirkolaii et al. [ 5] show that AI-driven models outperform tradi -
tional forecasting methods in handling irregular demand patterns, particularly in service
supply chains. Ruiz-Real et al. [ 47] further underscore the strategic importance of pre -
dictive analytics in digital marketing and business decision-making.
Automated lead generation has also emerged as a central focus in AI-driven sales
research. Potla [43] identifies AI-powered lead generation systems as essential tools for
enhancing customer targeting and improving conversion rates. Jayaweera and Farooq
[23] demonstrate how AI automates labor-intensive processes and enhances customer
engagement in the real estate sector. Similarly, Haleem et al. [ 15] and Umamaheswari
[54] highlight the role of AI in enabling real-time personalization and targeted com -
munication. Davenport et al. [ 10] describe how AI sales assistants can contact large
numbers of leads and identify the most promising ones, which may accelerate lead quali-
fication and expand sales pipelines. However, while these studies emphasize efficiency
gains, they often overlook potential trade-offs related to lead quality and sales force
overload.
In the domain of customer segmentation and personalization, AI plays a crucial role
in enabling more refined and targeted marketing strategies. Kedi et al. [ 25] demonstrate
how AI-driven tools enhance customer experience and sales performance in SMEs by
delivering personalized recommendations. Huang and Rust [ 20] conceptualize “think -
ing AI” as a mechanism for enhancing segmentation and targeting strategies, thereby
improving marketing effectiveness. Hicham et al. [ 17] further highlight the integration
of predictive analytics, personalization, and conversational AI in shaping customer
engagement. Despite these advancements, the empirical evidence on the performance
impact of personalization remains mixed, suggesting the need for further investigation.
A growing stream of literature emphasizes the importance of human–AI synergy in
achieving optimal performance outcomes. Petrescu and Krishen [ 42] argue that com -
bining human creativity with AI’s analytical capabilities leads to superior marketing
performance. Sankaran et al. [ 48] highlight the importance of human oversight in algo -
rithmic decision-making to avoid suboptimal outcomes driven by purely data-centric
approaches. Hemmer et al. [ 16] conceptualize human–AI complementarity through
capability and information asymmetries, while Simón et al. [ 51] demonstrate how team-
level interactions enhance value creation in AI-integrated environments. Revilla et al.

Page 5 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
[46] and Peng et al. [41] further emphasize that human intervention remains essential in
contexts requiring empathy, trust, and relational depth.
Dynamic capabilities theory provides one explanation for why the value of AI may
be contingent. AI can support sensing, seizing, and transforming activities, but per -
formance gains depend on complementary routines, managerial coordination, and the
capacity to reconfigure resources [ 51, 52, 59]. From this view, AI adoption alone is not
a capability,value arises when technology is integrated into an adaptive organizational
system.
Socio-technical and human-AI complementarity perspectives similarly emphasize
joint optimization of technical tools, work design, and human judgment. Human over -
sight can be especially important when customer interactions require empathy, trust,
or contextual knowledge [ 16, 41, 42]. These perspectives support organizational-fit
interpretations of heterogeneous coefficients, but the current variables do not directly
observe integration quality, automation intensity, or human override behavior.
Sales performance is also shaped by context outside the focal marketing technologies.
Economic policy uncertainty can alter investment, demand, financing conditions, and
firm performance [8], while geopolitical and business uncertainty may change customer
acquisition costs and purchase timing. At the market level, consumer perceptions and
buying attitudes, as emphasized by the theory of planned behavior [ 4], interact with
industry maturity, competition, and product involvement. Because these factors are not
represented in the simulation, they remain plausible omitted variables rather than con -
trolled influences.
Taken together, the literature supports a narrower research question: do the estimated
associations between AI-related marketing variables and revenue growth differ across
conditional quantiles, after accounting for the included firm-level variables? The study
does not test a universal technology effect, a causal growth-stage transition, or the pro -
posed organizational mechanisms directly.
3 Hypotheses development
Building on the theoretical foundations and empirical insights discussed above, this
study develops the following hypotheses:
H1: Marketing budget positively influences revenue growth across all firm growth levels.
H2: An independently measured marketing-efficiency construct is positively associated
with revenue growth.
H3: Sales team size positively affects revenue growth, particularly in low-to-medium
growth quantiles.
H4: Automated lead generation is negatively associated with revenue growth in higher-
growth quantiles, a pattern that may be consistent with diminishing returns or lead-qual-
ity constraints.
H5: The association between AI usage and revenue growth varies across quantiles and
may be negative in upper quantiles; organizational misalignment and over-automation
are possible, unmeasured interpretations.

Page 6 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
H6: Personalized campaigns have no significant impact on revenue growth, implying
market saturation or limited differentiation effects.
4 Data and methodology
4.1 Data
The analysis uses a stylized, country-neutral and cross-industry simulation of 50 firms.
The observations were not drawn from a specific country, sector, platform, customer
segment, or historical period. Accordingly, the data represent a controlled analytical set-
ting rather than a statistically representative business population. Revenue growth is the
dependent variable; the inferential predictors are sales team size, AI-based predictive-
analytics usage, personalized campaigns, marketing budget, and automated lead genera -
tion (Table 1).
Synthetic data are useful when access to confidential firm-level records is restricted,
but their value depends on a fully documented data-generating process [ 13, 24, 53]. The
supplied workbook contains 50 complete row-level observations with no duplicate rows.
It does not include the original generation seed, distribution families and parameters,
target dependence structure, truncation rules, or generator code, those elements of the
simulation cannot be independently verified.
The verifiable transformation sequence is as follows. Revenue growth, AI usage, and
automated lead generation remain in percentage units. Natural logarithms are applied
to sales team size, personalized campaign count, and marketing budget. The workbook
also contains revenue per salesperson (Revenue Growth/Sales Team Size) and market -
ing efficiency (Revenue Growth/Marketing Budget). Because both measures contain the
dependent variable by construction, they are reported only as data-audit diagnostics and
excluded from every inferential regression.
Figures 1, 2, 3, 4, 5, 6, 7, 8 and 9 and Table  2 document the realized marginal distri -
butions and pairwise relationships. The bounded sample does not reproduce the heavy
tails, structural breaks, measurement error, sector clustering, or rare shocks that may
occur in real firm data. Correlations involving marketing efficiency or revenue per sales -
person are partly mechanical because those ratios contain revenue growth; they are not
interpreted as independent empirical relationships.
The row-level dataset and the analysis code are sufficient to reproduce the transfor -
mations, corrected regressions, bootstrap estimates, robustness checks, tables, and new
figures reported here. Exact regeneration of the original synthetic observations still
requires the original random seed, per-variable distributions and parameters, target
Table 1 Variables and measurement units
Variable Description Unit
Rev_Growth Growth rate of revenue over a period % (Percentage)
Sales_Team Number of sales team members Count
AI_Usage AI-driven predictive analytics usage % (Percentage)
Mkt_Budget Total marketing budget allocated $ (USD)
Lead_Gen Percentage of automated lead generation % (Percentage)
Mkt_Eff Revenue growth divided by marketing budget (diagnostic only; excluded
from regressions)
Ratio
Pers_Camp Number of personalized marketing campaigns Count
Rev_Per_Sales Revenue growth divided by sales-team size (diagnostic only; excluded
from regressions)
Percentage
points per
salesperson

Page 7 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
Fig. 4 Distribution of Mkt_Budget

Fig. 3 Distribution of AI_Usage

Fig. 2 Distribution of Sales_Team

Fig. 1 Distribution of Rev_Growth

Page 8 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
correlation matrix, dependence algorithm, redraw or truncation rules, and software
environment, which were not supplied.
Synthetic data provide analytical control but do not substitute for external validation.
The results are therefore treated as an exploratory demonstration of model- and quan -
tile-sensitive associations and should be tested in larger longitudinal, multi-industry,
and country-specific datasets.
The definitions and measurement units of the variables used in the analysis are pre -
sented in Table 1.
Fig. 8 Distribution of Rev_Per_Sales

Fig. 7 Distribution of Pers_Camp

Fig. 6 Distribution of Mkt_Eff

Fig. 5 Distribution of Lead_Gen

Page 9 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
4.2 Method
To capture the heterogeneous effects of AI-driven marketing technologies across firms
with different performance levels, this study employs quantile regression. Unlike ordi -
nary least squares (OLS), which estimates the conditional mean of the dependent
variable, quantile regression enables the estimation of conditional quantiles, thereby
providing a more comprehensive understanding of the distributional dynamics of rev -
enue growth. This approach is particularly appropriate in the presence of non-normal
error distributions, heteroskedasticity, and potential outliers [26].
Formally, the quantile regression model is defined as:
 𝑄𝑄𝑌𝑌𝑖𝑖 (𝜏𝜏𝜏𝜏𝜏𝑖𝑖 ) =𝜏𝜏 𝑖𝑖 ′𝛽𝛽 (𝜏𝜏) (1)
where 𝑄𝑄𝑌𝑌𝑖𝑖 (𝜏𝜏𝜏𝜏𝜏𝑖𝑖 ) denotes the conditional τ-th quantile of the dependent variable given
the covariates Xi, and β(τ)represents the vector of quantile-specific coefficients. When
τ=0.5, the model corresponds to the conditional median.
The parameter estimates are obtained by minimizing the following objective function:
Table 2 Descriptive statistics
Variable Mean Std. Dev Minimum Maximum
Rev_Growth 9.480 5.485 1.400 19.400
Sales_Team 3.808 0.689 2.303 4.585
AI_Usage 66.120 21.590 30.000 98.000
Mkt_Budget 12.298 0.586 10.943 13.104
Lead_Gen 47.434 16.556 20.900 78.600
Mkt_Eff − 10.261 0.873 − 12.476 − 8.188
Pers_Camp 2.428 0.383 1.609 2.944
Rev_Per_Sales − 1.771 1.031 − 4.217 0.495
Fig. 9 Correlation matrix

Page 10 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627

̂𝛽𝛽 (𝜏𝜏) = arg 𝑚𝑚𝑚𝑚𝑚𝑚𝛽𝛽
𝑛𝑛
∑
𝑖𝑖𝑖𝑖
𝜌𝜌𝜏𝜏 (𝑌𝑌 𝑖𝑖 −𝑋𝑋 𝑖𝑖 ′𝛽𝛽) (2)
where ρτ(u) is the quantile loss function defined as:

𝑝𝑝𝜏𝜏 (𝑢𝑢) =𝑢𝑢 (𝜏𝜏𝜏 ∥ { 𝑢𝑢𝑢𝑢 } ) = { 𝜏𝜏𝑢𝑢𝜏𝜏𝜏𝜏𝑢𝑢 ≥ 𝑢 (𝜏𝜏𝜏𝜏 ) 𝑢𝑢𝜏𝜏𝜏𝜏𝑢𝑢 𝑢 𝑢  (3)
This asymmetric loss function assigns different weights to positive and negative residu -
als, allowing the estimation of different points across the conditional distribution. T o
examine distributional heterogeneity, the model is estimated at tau = 0.10, 0.25, 0.50,
0.75, and 0.90. These estimates describe lower, middle, and upper positions in the condi-
tional revenue-growth distribution; they do not identify longitudinal firm-growth stages.
The empirical specification of the model is given by:

QRevGrowthit (𝜏𝜏𝜏Xit) =𝛼𝛼 0 (𝜏𝜏) +𝛼𝛼 1 (𝜏𝜏) SalesTeamit +𝛼𝛼 2 (𝜏𝜏) AIUsageit
+𝛼𝛼 3 (𝜏𝜏) PersCampit +𝛼𝛼 4 (𝜏𝜏) MktBudgetit +𝛼𝛼 5 (𝜏𝜏) LeadGenit  (4)
In this specification, the coefficients αj(τ)vary across quantiles, capturing how the mar -
ginal effects of explanatory variables differ across the distribution of revenue growth.
With five regressors and n = 50, Q10 and Q90 are informed by few tail observations.
Inference therefore uses a nonparametric pairs bootstrap with 2000 replications and
fixed seed 20, 260, 723; percentile 95% confidence intervals are reported for OLS and
every quantile. Model specificity is assessed with Huber robust regression [ 21] and ridge
regression [18]. Predictors are standardized for the cross-estimator comparison, and the
ridge penalty is selected by generalized cross-validation over alpha values from 10 –4 to
104.
5 Results
Revenue growth, AI usage, and automated lead generation are expressed in percentage
points; sales team size, marketing budget, and personalized campaign count enter in nat-
ural logarithms. The resulting log-level coefficients are semi-elasticities: a 1% increase in
a logged predictor corresponds approximately to beta/100 percentage points of revenue
growth, holding the other predictors constant. Table 2 reports descriptive statistics for
the transformed variables, including the two diagnostic ratios that are excluded from
inferential models.
Figures 1, 2, 3, 4, 5, 6, 7 and 8 illustrate the empirical distributions of the supplied vari-
ables. The figures describe the realized synthetic sample only. Revenue growth (Fig.  1)
shows an even spread without a dominant peak, indicating that firms at both the lower
and upper ends differ significantly, justifying the use of quantile regression.
In terms of predictors, AI usage (Fig.  3) and automated lead generation (Fig. 5) exhibit
broad variation with few firms at the extremes, suggesting that the lack of a bootstrap-
supported association for AI usage isn't due to limited adoption variability. However,
sales team size (Fig.  2) and marketing budget (Fig.  4) are left-skewed. Personalised cam -
paigns (Fig.  7) have a narrow range, leading to fewer informative observations, which
may explain the wide bootstrap confidence intervals and the sign changes noted in
Table 3, aligning with the unsupported hypotheses H1, H3, and H6.

Page 11 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
Lastly, marketing efficiency (Fig. 6) and revenue per salesperson (Fig. 8) are more sym-
metric but should not be considered well-behaved independent measures since their dis-
tributions are partly influenced by revenue growth in Fig.  1. They are included solely for
data documentation and are excluded from further inferential models.
Figure  9 presents the correlation matrix as a data-audit display. The apparent rela -
tionships of revenue per salesperson and marketing efficiency with revenue growth
are mechanically induced by their formulas. Consequently, neither derived measure is
included in the corrected OLS, quantile, Huber, or ridge models.
Table 3 reports the corrected OLS and quantile-regression estimates with revenue
growth as the dependent variable. The supplied workbook reproduces the manuscript's
previous coefficients exactly when marketing efficiency is included, but that specifica -
tion attains R-squared = 0.935 largely because log(Marketing Efficiency) = log(Revenue
Growth)—log(Marketing Budget). The corrected model excludes both dependent-vari -
able-derived ratios. Its OLS R-squared is 0.137 (adjusted R-squared = 0.039), which is a
more credible representation of the limited explanatory content of this small synthetic
sample.
For the corrected OLS model, the Breusch-Pagan statistic is 10.799 ( p = 0.056), the
Durbin-Watson statistic is 2.435, and the Jarque–Bera statistic is 1.136 (p = 0.567). Vari-
ance inflation factors range from 1.042 to 1.176, well below the commonly used thresh -
old of 10 [ 14]. These diagnostics do not reject homoskedasticity or normality at the 5%
level and show no material multicollinearity, although the near-threshold Breusch-Pagan
result and small sample further motivate bootstrap inference.
Table 3 shows that automated lead generation is the only predictor whose bootstrap
confidence intervals exclude zero. Its coefficient is negative in OLS (− 0.123) and at
every quantile. The 95% percentile interval excludes zero in OLS [− 0.211, −0.022], at
Q75 [− 0.301, −0.024] and at Q90 [− 0.320, −0.002]. The coefficient grows in absolute size
from Q10 (− 0.024) to Q90 (− 0.244), so the negative association appears stronger in the
upper part of the conditional revenue growth distribution (Fig. 10).
The analysis shows that AI usage has small coefficients that vary in sign across dif -
ferent parts of the distribution. Specifically, the coefficients are negative in OLS, Q25,
Table 3 Model estimation results
Dependent variable: Rev_Growth
Variables Model: OLS Model: quantile regression
Quantiles
0.10 0.25 0.50 0.75 0.90
Intercept 6.424
(17.425)
2.424
(13.875)
2.582
(18.715)
13.824
(23.376)
2.877
(28.920)
26.251
(29.403)
Sales_Team 0.545
(1.109)
− 1.920
(1.130)
− 1.477
(1.845)
3.813
(1.797)
2.160
(2.028)
− 2.519
(2.524)
AI_Usage − 0.028
(0.037)
0.001
(0.040)
− 0.015
(0.045)
− 0.040
(0.053)
0.003
(0.061)
− 0.058
(0.064)
Mkt_Budget 0.835
(1.345)
0.371
(1.159)
0.734
(1.460)
0.087
(1.733)
1.258
(2.292)
0.964
(2.266)
Lead_Gen − 0.123*
(0.049)
− 0.024
(0.055)
− 0.064
(0.070)
− 0.166
(0.071)
− 0.183*
(0.067)
− 0.244*
(0.081)
Pers_Camp − 0.662
(2.127)
2.058
(2.762)
1.105
(3.918)
− 3.794
(2.841)
− 2.274
(2.563)
1.561
(2.702)
Coefficients are followed by pairs-bootstrap standard errors in parentheses (2,000 replications; seed = 20,260,723). *
indicates that the percentile 95% bootstrap confidence interval excludes zero. OLS R-squared = 0.137; adjusted R-squared
= 0.039. Breusch-Pagan LM = 10.799 ( p = 0.056); Durbin-Watson = 2.435; Jarque–Bera = 1.136 ( p = 0.567)

Page 12 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
Q50, and Q90, while they are slightly positive in Q10 and Q75. Importantly, all intervals,
including Q90, encompass zero [− 0.218, 0.049]. In contrast, the marketing budget yields
positive point estimates in OLS and across all five quantiles, although all confidence
intervals still include zero. The sizes of sales teams and personalised campaigns exhibit
sign changes across quantiles, and their intervals remain wide, consistently including
zero in every model.
In Table 4 and Fig. 11, a comparison is made between the standardised estimates from
OLS and those from Huber and ridge regression. Each of the five predictors retains the
same sign across all three estimation methods: both sales team size and marketing bud -
get have positive coefficients, while AI usage, automated lead generation, and personal -
ized campaigns are negative. However, the magnitude of these coefficients differs. Ridge
regression (with an alpha of 89.074) significantly decreases all coefficients, while Huber
estimates are generally larger in absolute terms than OLS for four out of the five pre -
dictors. Notably, automated lead generation consistently shows the largest standardized
coefficient across all three estimation techniques.
Table 5 summarises how each hypothesis is assessed against these aforementioned
results.
Table 4 Alternative-estimator comparison (standardized coefficients)
Variable OLS Huber Ridge
Sales_Team 0.068 0.265 0.017
AI_Usage − 0.108 − 0.130 − 0.013
Mkt_Budget 0.089 0.057 0.031
Lead_Gen − 0.372 − 0.474 − 0.120
Pers_Camp − 0.046 − 0.215 − 0.029
Predictors and the dependent variable are standardized for this comparison. Huber uses epsilon = 1.35. Ridge alpha =
89.074, selected by generalized cross-validation. All predictor signs are identical across OLS, Huber, and ridge; magnitudes
are estimator-sensitive
Fig. 10 Quantile coefficients with 95% pairs-bootstrap confidence intervals

Page 13 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
6 Discussion
Looking at the results, it seems that neither the marketing budget nor the sales team
size (H1 and H3) received sufficient support. While the marketing budget shows positive
point estimates across all quantiles, which aligns with expectations, none of the confi -
dence intervals exclude zero. This may indicate that the relationship between market -
ing expenditure and sales isn’t linear. Agrahari et al. [ 3], in their study of publicly listed
manufacturing companies in Nepal, highlight a non-linear relationship wherein a spe -
cific level of marketing investment optimises sales. A single logged budget term may
not effectively capture such a pattern. Additionally, the budget variable reflects a lim -
ited number of firms on the lower end (Fig.  4), which restricts the available data. The
sales team size exhibits varying signs across quantiles, suggesting that the data does not
consistently support the hypothesis (H3) that larger sales teams correlate with greater
growth in the low to mid quantiles.
On the other hand, H4 is supported at the 75th and 90th percentiles. Much of the
existing literature suggests that automated lead generation enhances efficiency by
streamlining lead qualification and expanding sales pipelines [ 10, 23]. However, the
current findings do not align with this expectation. Instead, they resonate more with
studies focusing on lead quality and the follow-up processes post-lead generation. Hut -
telmaier and Heigl [22] note that companies employing marketing and sales automation
Table 5 Hypothesis assessment
Hypothesis Evidence from the reported models Assessment
H1 Mkt_Budget is positive in OLS and all quantiles, but every 95% bootstrap
CI includes zero
Not supported
H2 Mkt_Eff equals Rev_Growth / Mkt_Budget and was excluded to prevent
target leakage
Not testable with
available measure
H3 Sales_Team changes sign across quantiles and every 95% bootstrap CI
includes zero
Not supported
H4 Lead_Gen is negative throughout; 95% bootstrap CIs exclude zero in
OLS, Q75, and Q90
Supported at Q75
and Q90; also
supported in OLS
H5 AI_Usage is negative at Q90 but slightly positive at Q75; all bootstrap CIs
include zero
Not supported
H6 Pers_Camp is imprecisely estimated and all bootstrap CIs include zero;
this does not prove a zero effect
Consistent with
no detected
effect
Fig. 11 Standardized OLS, Huber, and ridge coefficients

Page 14 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
frequently overwhelm sales staff with low-quality leads, which diverts their time from
leads that could convert. Furthermore, Ohiomah et al. [ 36] found that lead management
systems influence inside sales performance through various factors such as lead follow-
up intensity, adaptive selling, and salesperson skills. This implies that the effectiveness
of such systems is contingent upon lead handling rather than sheer lead volume. Con -
sequently, a higher proportion of automated leads may merely increase volume without
contributing to revenue. However, the data do not assess lead quality or sales workload,
leaving this as a tentative interpretation. There remains a gap in understanding why the
correlation is more pronounced in the upper quantiles,one explanation worth exploring
is that faster-growing companies may have less capacity to handle additional low-quality
leads.
Regarding AI usage (H5), there is no support for this hypothesis. The coefficients for
AI usage are relatively small, show varying signs across quantiles, and all confidence
intervals include zero. There is considerable variability in AI usage among firms (Fig.  3),
so this outcome cannot be attributed solely to insufficient variation. Existing studies on
AI transformation projects indicate that AI can enhance process and organisational per -
formance [59]. Yet, reviews suggest that firms continue to struggle to extract value from
AI, with adoption often influenced by various organisational factors [ 11]. Evidence from
case studies indicates that the success of AI is largely dependent on the synergy between
people and systems. Simón et al. [ 51] connect value creation to factors such as interop -
erability and mutual trust between humans and AI. Moreover, Revilla et al. [ 46] found
that human involvement significantly enhances AI forecasts, particularly under condi -
tions of low uncertainty and extended time horizons. Conversely, Papagiannidis et al.
[39] documented the unintended consequences of AI adoption regarding work dynam -
ics, conflicts, and accountability. Taken together, these insights suggest that the lack of a
consistent association indicates that the proportion of AI activities may not be a reliable
measure of AI’s integration into sales processes. The current data do not clarify whether
issues stem from over-automation or inadequate integration. As for personalised cam -
paigns (H6), the results only align loosely with this hypothesis, as no significant relation -
ship was observed. The literature on personalisation presents mixed evidence, with some
studies indicating advantages for customer experience and sales within SMEs [25].
These findings provide contributions in three key areas. First, most existing research
on AI in marketing and sales derives from reviews, conceptual analyses, and studies
reporting average effects [ 9, 32, 34]. Quantile regression studies on firm performance
reveal that the drivers of success can differ markedly between firms with lower and
higher sales. For instance, Matekenya and Moyo [ 33] discovered that R&D investments
bolster performance in South African SMMEs with higher sales, while product and ser -
vice innovation is more critical for those with lower sales. Similarly, Ghardallou [ 12]
reports that the adverse effect of leverage on performance is stronger among more prof -
itable listed firms in Saudi Arabia. This study applies a similar approach to explore AI
marketing variables and finds that, in this sample, significant differences appear only for
automated lead generation. Second, the data audit demonstrates that efficiency ratios
constructed from dependent variables can lead to misleadingly high model fits, a con -
sideration pertinent to studies relying on ratio-based performance indicators. Finally,
the results provide indirect backing for the perspective within the dynamic capabilities

Page 15 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
and human-AI complementarity literature that mere AI adoption does not guarantee
enhanced performance [51, 52].
7 Managerial and policy implications
Managers should not infer a universal numerical 'optimal AI level' from these cross-sec -
tional synthetic coefficients. Instead, the optimal adoption level should be treated as a
firm-specific decision threshold established through staged pilots. Before deployment,
managers should define a baseline and pre-specified success criteria for incremental
revenue, conversion, forecast error, lead-acceptance rate, sales-cycle time, salesperson
workload, customer complaints, and human override frequency.
A practical scale-or-stop rule is to expand AI only when the pilot's incremental con -
tribution remains positive after total technology, integration, training, and monitoring
costs and when lead quality and customer-experience indicators do not deteriorate.
Managers should pause or redesign deployment when marginal revenue falls, lead rejec -
tion or override rates rise, sales-cycle time lengthens, or adverse customer indicators
persist for two review periods. Controlled holdout groups and confidence intervals are
preferable to selecting a cutoff from the present quantile coefficients.
Governance should also be contingent on organizational readiness. Lower-performing
firms may first strengthen data quality, measurement, and core sales routines; firms with
more developed systems should emphasize integration, decision rights, human escala -
tion paths, and continuous monitoring. Lead-generation automation should be governed
by downstream conversion and capacity metrics rather than lead volume alone.
For policy makers, the findings support capability-building and responsible-AI frame -
works rather than uniform adoption targets. Transparency, auditability, data protection,
worker training, and access to testing resources can help firms evaluate AI under sector-
specific market, consumer, and uncertainty conditions.
8 Limitations and future research
As is the case with any study, this study has several limitations. First, it utilizes a small,
cross-sectional synthetic sample with n = 50 and five regressors, making Q10 and Q90
sensitive to individual observations despite 2000 bootstrap replications. Second, market-
ing efficiency and revenue-per-salesperson measures, being deterministic functions of
revenue growth, were excluded from inferential models, preventing the testing of H2.
Third, while Huber and ridge estimates maintain coefficient directions, the ridge solu -
tion is heavily shrunk, and the design does not support causal inference or generaliza -
tion. Additionally, the simulation lacks industry, country, customer segment, or time
frame specificity, limiting its ability to capture sector dynamics, market maturity, or
anomalies. To ensure reproducibility, all relevant details such as the generator and seed
must be archived.
Moreover, the model overlooks external factors like economic uncertainty, inflation,
and competitive intensity, leading to potential omitted-variable bias in relation to AI
investment and sales performance. Future studies should incorporate macroeconomic
and industry controls and examine interactions with AI adoption [ 8]. Consumer per -
ceptions, attitudes, trust, and privacy concerns are also not addressed, even though
they can impact responses to personalization and automation [ 49, 50]. A multi-source

Page 16 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
approach that integrates data from firms, salespeople, and customers would strengthen
the findings.
Lastly, the study fails to measure crucial concepts like over-automation, integra -
tion failures, and digital maturity. These interpretations of coefficient patterns remain
unobserved mechanisms. Future research should employ longitudinal or experimental
designs and formal mediation tests to explore these factors.
9 Conclusion
This corrected exploratory analysis finds a negative association between automated lead
generation and revenue growth in OLS and at Q75 and Q90, with percentile 95% boot -
strap intervals excluding zero. For AI usage, marketing budget, sales-team size, and per -
sonalized campaigns, the bootstrap intervals include zero at all reported quantiles.
The results do not establish that over-automation, integration failure, lead quality, or
any other mechanism caused lower performance. They identify one lead-generation
pattern that requires direct measurement and external validation. Managers should
therefore use staged pilots, marginal-return and quality metrics, and human-oversight
indicators rather than a universal AI adoption threshold.
The principal next step is validation in larger, longitudinal, industry-specific data that
include macroeconomic, consumer, organizational, lead-quality, and implementation-
context measures. The original simulation generator and seed should also be deposited
so that the synthetic sample itself, not only the reported analysis, can be regenerated.
Author contributions
Author 1 (C.S): Conceptualization, Methodology, Formal analysis, Writing—original draft. Author 2 (CdB): Data curation,
Validation, Writing—review & editing. Author 3 (R.K): Supervision, Conceptualization, Writing—review & editing. Author 4
(E.K): Investigation, Resources, Visualization. Author 5 (S.Y): Writing—review & editing, Validation.
Funding
This research received institutional support. No external funding was received.
Data availability
The row-level synthetic dataset and executable analysis code accompany this revision and reproduce the
transformations, corrected regressions, 2,000-replication bootstrap, robustness checks, tables, and figures. The original
data-generation seed, distribution parameters, dependence algorithm, and generator code were not supplied; exact
regeneration of the synthetic observations is therefore not possible from the available materials.
Declarations
Ethics approval and consent to participate
Not applicable. This study does not involve human participants, human data, or human tissue.
Consent for publication
Not applicable.
Clinical trial number
Not applicable.
Competing interests
The authors declare that they have no known competing financial interests or personal relationships that could have
appeared to influence the work reported in this paper.
Received: 22 June 2026 / Accepted: 12 October 2026
References
1. Achumie GO, Oyegbade IK, Igwe AN, Ofodile OC, Azubuike C. AI-driven predictive analytics model for strategic business
development and market growth in competitive industries. Int J Soc Sci Except Res. 2022.  h t t p s  : / / d o i  . o r g /  1 0 . 5  4 6 6 0 / i j s s e r . 2
0 2 2 . 1 . 1 . 1 3 - 2 5     .
2. Agnihotri R. From sales force automation to digital transformation: how social media, social CRM, and artificial intelligence
technologies are influencing the sales process. Res Agenda Sales. 2021;21–47.

Page 17 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
3. Agrahari K, Karki D, Rai R. Impact of marketing expenditure on sales and profitability of listed manufacturing companies in
Nepal. Koshi Pravah Multidiscip Peer Rev J. 2023;2(1):61–76. https://doi .org/10.312 6/koshiprav ah.v2i1. 67127.
4. Ajzen I. The theory of planned behavior. Organ Behav Hum Decis Process. 1991;50(2):179–211.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / 0 7 4
9 - 5 9 7 8 ( 9 1 ) 9 0 0 2 0 - T     .
5. Amirkolaii KN, Baboli A, Shahzad MK, Tonadre R. Demand forecasting for irregular demands in business aircraft spare parts
supply chains by using artificial intelligence (AI). IFAC-PapersOnLine. 2017;50(1):15221–6.  h t t p s  : / / d o i  . o r g /  1 0 . 1  0 1 6 / j . i f a c o l . 2
0 1 7 . 0 8 . 2 3 2 6     .
6. Basu R, Aktar MN, Kumar S. The interplay of artificial intelligence, machine learning, and data analytics in digital marketing
and promotions: a review and research agenda. J Market Anal. 2024. https://doi.org/10.1007/s43069-024-00098-1.
7. Carlos M, Sofía G. AI-powered CRM solutions: Salesforce’s Data Cloud as a blueprint for future customer interactions. Int J
Trend Sci Res Dev. 2022;6(6):2331–46.
8. Chakradhar J, Gupta R. Heterogeneous effect of economic policy uncertainty and firm financial performance: empirical
evidence from India. Manag Decis Econ. 2024;45(7):4930–51.
9. Chintalapati S, Pandey SK. Artificial intelligence in marketing: a systematic literature review. Int J Mark Res.
2022;64(1):38–68.
10. Davenport TH, Guha A, Grewal D, Bressgott T. How artificial intelligence will change the future of marketing. J Acad Mark
Sci. 2020;48:24–42. https://doi.org/10.1007/s11747-019-00696-0.
11. Enholm IM, Papagiannidis E, Mikalef P , Krogstie J. Artificial intelligence and business value: a literature review. Inf Syst Front.
2022;24(5):1709–34. https://doi.org/10.1007/s10796-021-10186-w.
12. Ghardallou W. The heterogeneous effect of leverage on firm performance: a quantile regression analysis. Int J Islam Middle
East Finance Manag. 2023;16(1):210–25. https://doi.org/10.1108/IMEFM-12-2021-0490.
13. Goncalves A, Ray P , Soper B, Stevens J, Coyle L, Sales AP . Generation and evaluation of synthetic patient data. BMC Med Res
Methodol. 2020;20(1):108. https://doi.org/10.1186/s12874-020-00977-1.
14. Hair JF, Anderson RE, Tatham RL, Black WC. Multivariate data analysis with readings. 4th ed. Prentice Hall; 1995.
15. Haleem A, Javaid M, Qadri MA, Singh RP , Suman R. Artificial intelligence (AI) applications for marketing: a literature-based
study. Int J Int Netw. 2022;3:119–32. https://doi.org/10.1016/j.ijin.2022.07.001.
16. Hemmer P , Schemmer M, Kühl N, Vössing M, & Satzger G. Complementarity in human-AI collaboration: concept, sources,
and evidence. arXiv preprint arXiv:2404.00029, 2024.
17. Hicham N, Nassera H, Karim S. Strategic framework for leveraging artificial intelligence in future marketing decision-mak-
ing. J Int Manag Decis. 2023;2(3):139–50.
18. Hoerl AE, Kennard RW. Ridge regression: biased estimation for nonorthogonal problems. Technometrics. 1970;12(1):55–67.
19. Huang MH, Rust RT. Artificial intelligence in service. J Serv Res. 2018;21(2):155–72.  h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 / 1 0 9 4 6 7 0 5 1 7 7 5 2
4 5 9     .
20. Huang MH, Rust RT. A strategic framework for artificial intelligence in marketing. J Acad Mark Sci. 2021;49:30–50.  h t t p s : / / d
o i . o r g / 1 0 . 1 0 0 7 / s 1 1 7 4 7 - 0 2 0 - 0 0 7 4 9 - 9     .
21. Huber PJ. Robust estimation of a location parameter. Ann Math Stat. 1964;35(1):73–101.
22. Huttelmaier H, Heigl J. Boosting marketing and sales automation’s effectiveness: strategies to increase lead quality. In:
Hannig U, Seebacher U, editors. Marketing and sales automation. Springer; 2023. p. 345–62.  h t t p s : / / d o i . o r g / 1 0 . 1 0 0 7 / 9 7 8 - 3 -
0 3 1 - 2 0 0 4 0 - 3 _ 1 9     .
23. Jayaweera A, & Farooq MU. Leveraging AI-driven digital marketing strategies to automate the lead generation mechanism
of the real estate industry in the United States. 2023 GBATA Readings Book Theme: Embracing the Positive Impact of
Disruption in the Field of Futurism, 2023;263.
24. Jordon J, Yoon J, & van der Schaar M. PATE-GAN: generating synthetic data with differential privacy guarantees. Interna-
tional Conference on Learning Representations (ICLR). 2022.
25. Kedi WE, Ejimuda C, Idemudia C, Ijomah TI. AI software for personalized marketing automation in SMEs: enhancing cus-
tomer experience and sales. World J Adv Res Rev. 2024;23(1):1981–90.
26. Koenker R, Bassett G Jr. Regression quantiles. Econometrica. 1978;46(1):33–50.
27. Kumar V, Ashraf AR, Nadeem W. AI-powered marketing: what, where, and how? Int J Inf Manage. 2024;77:102783.  h t t p s  : / / d
o i  . o r g /  1 0 . 1  0 1 6 / j . i j i n f o m g t . 2 0 2 3 . 1 0 2 7 1 6     .
28. Kumar V, Ramachandran D, Kumar B. Influence of new-age technologies on marketing: a research agenda. J Bus Res.
2021;125:864–77. https://doi .org/10.101 6/j.jbusres .2020.12 .049.
29. Libai B, Bart Y, Gensler S, Hofacker CF, Kaplan A, Kötterheinrich K, et al. Brave new world? On AI and the management of
customer relationships. J Interact Mark. 2020;51(1):44–56. https://doi.org/10.1016/j.intmar.2020.04.003.
30. Liu-Thompkins Y, Okazaki S, Li H. Artificial empathy in marketing interactions: bridging the human-AI gap in affective and
social customer experience. J Acad Mark Sci. 2022;50(6):1198–218. https://doi.org/10.1007/s11747-022-00892-5.
31. Lopez S, Arjunan G. Optimizing marketing ROI with predictive analytics: harnessing big data and AI for data-driven deci-
sion making. J Art Int Res. 2023;3(2):9–36.
32. Mariani MM, Perez-Vega R, Wirtz J. AI in marketing, consumer research and psychology: a systematic literature review and
research agenda. Psychol Mark. 2022;39(4):755–76.
33. Matekenya W, Moyo C. Innovation as a driver of SMME performance in South Africa: a quantile regression approach. Afr J
Econ Manag Stud. 2022;13(3):452–67.
34. Mustak M, Salminen J, Plé L, Wirtz J. Artificial intelligence in marketing: topic modeling, scientometric analysis, and
research agenda. J Bus Res. 2021;124:389–404. https://doi .org/10.101 6/j.jbusres .2020.11 .045.
35. Nishat A. The role of artificial intelligence in sales force automation: a paradigm shift in CRM systems. Pioneer Res J Com-
put Sci. 2024;1(1):68–74. https://doi.org/10.1108/APJBA-06-2021-0243.
36. Ohiomah A, Andreev P , Benyoucef M, Hood D. The role of lead management systems in inside sales performance. J Bus
Res. 2019;102:163–77. https://doi .org/10.101 6/j.jbusres .2019.05 .019.
37. Okeleke PA, Ajiga D, Folorunsho SO, & Ezeigweneme C. Predictive analytics for market trends using AI: a study in consumer
behavior. 2024.
38. Oladele OK. Data-driven product roadmap prioritization: using AI-powered predictive analytics to optimize feature
sequencing. 2024.

Page 18 of 18
Sarıoğlu et al. Discover Artificial Intelligence           (2026) 6:1627
39. Papagiannidis E, Mikalef P , Conboy K, Van de Wetering R. Uncovering the dark side of AI-based decision-making: a case
study in a B2B context. Ind Mark Manage. 2023;115:253–65. https://doi.org/10.1016/j.indmarman.2023.07.  012.
40. Paramesha M, Rane NL, Rane J. Big data analytics, artificial intelligence, machine learning, internet of things, and block-
chain for enhanced business intelligence. Partn Univ Multidiscip Res J. 2024;1(2):110–33.
41. Peng C, van Doorn J, Eggers F, Wieringa JE. The effect of required warmth on consumer acceptance of artificial intelligence
in service: the moderating role of AI-human collaboration. Int J Inf Manage. 2022;66:102533.  h t t p s : / / d o i . o r g / 1 0 . 1  0  1 6 / j . i j i n f
o m g t . 2 0 2 2 . 1 0 2 5 3 3     .
42. Petrescu M, Krishen AS. Hybrid intelligence: Human–AI collaboration in marketing analytics. J Market Anal. 2023;11(3):263–
74. https://doi.org/10.1057/s41270-023-00210-0.
43. Potla RT. Enhancing customer relationship management (CRM) through AI-powered chatbots and machine learning.
Distrib Learn Broad Appl Sci Res. 2023;9:364–83.
44. Potla RT, & Pottla VK. AI-powered personalization in Salesforce: enhancing customer engagement through machine learn-
ing models. Val Int J Digit Library, 2024;1388–1420.
45. Ramya J, Yerraguravagari SS, Gaikwad S, & Gupta RK. AI and machine learning in predictive analytics: revolutionizing busi-
ness strategies through big data ınsights. Libr Prog Libr Sci Inf Technol Comput, 2024;44(3).
46. Revilla E, Saenz MJ, Seifert M, Ma Y. Human–artificial intelligence collaboration in prediction: a field experiment in the retail
industry. J Manag Inf Syst. 2023;40(4):1071–98. https://doi .org/10.108 0/07421222. 2023.222 9074.
47. Ruiz-Real JL, Uribe-Toril J, Torres JA, De Pablo J. Artificial intelligence in business and economics research: trends and
future. J Bus Econ Manag. 2021;22(1):98–117. https://doi.org/10.3846/jbem.2021.14212.
48. Sankaran G, Palomino MA, Knahl M, Siestrup G. A modeling approach for measuring the performance of a human-AI col-
laborative process. Appl Sci. 2022;12(22):11642. https://doi.org/10.3390/app122211642.
49. Sharma KK, Tomar M, Tadimarri A. Unlocking sales potential: how AI revolutionizes marketing strategies. J Knowl Learn Sci
Technol. 2023;2(2):231–50.
50. Sharma P , Ueno A, Dennis C, Turan CP . Emerging digital technologies and consumer decision-making in retail sector:
towards an integrative conceptual framework. Comput Hum Behav. 2023;148:107913.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . c h b . 2 0 2 3 . 1
0 7 9 1 3     .
51. Simón C, Revilla E, Sáenz MJ. Integrating AI in organizations for value creation through human-AI teaming: a dynamic-
capabilities approach. J Bus Res. 2024;182:114783. https:   //d oi. or g/10 . 1016/j. jbus res. 2024.114783.
52. Teece DJ. Business models and dynamic capabilities. Long Range Plann. 2018;51(1):40–9.  h t t p s : / / d o i . o r g / 1 0 . 1 0 1 6 / j . l r p . 2 0 1 7
. 0 6 . 0 0 7     .
53. Tucker A, Wang Z, Rotalinti Y, Myles P . Generating high-fidelity synthetic patient data for assessing machine learning
healthcare software. npj Digit Med. 2020;3(1):147. https://doi.org/10.1038/s41746-020-00353-9.
54. Umamaheswari DD. Role of artificial intelligence in marketing strategies and performance. Migr Lett. 2024;21(S4):1589–99.
55. Venkataramanan S, Sadhu AKR, Gudala L, Reddy AK. Leveraging artificial intelligence for enhanced sales forecasting
accuracy: a review of AI-driven techniques and practical applications in customer relationship management systems.
Australian J Mach Learn Res Appl. 2024;4(1):267–87.
56. Venkateswaran PS, Dominic ML, Agarwal S, Oberai H, Anand I, Rajest SS. The role of artificial intelligence (AI) in enhancing
marketing and customer loyalty. In: Data-driven intelligent business sustainability. IGI Global; 2024. p. 32–47.
57. Victor-Mgbachi TOYIN. Leveraging artificial intelligence (AI) effectively: managing risks and boosting productivity. IRE J.
2024;7(7):54–69.
58. Vignesh R, Vasantha S. Significant developments of artificial intelligence in Indian ecommerce industry in 2019. Int J Sci
Technol Res. 2019;8(12):2746–8.
59. Wamba-Taguimdje SL, Wamba SF, Kamdjoug JRK, Wanko CET. Influence of artificial intelligence (AI) on firm performance:
the business value of AI-based transformation projects. Bus Process Manag J. 2020;26(7):1893–924.  h t t p s : / / d o i . o r g / 1 0 . 1 1 0 8
/ B P M J - 1 0 - 2 0 1 9 - 0 4 1 1     .
Publisher's Note
Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations.
