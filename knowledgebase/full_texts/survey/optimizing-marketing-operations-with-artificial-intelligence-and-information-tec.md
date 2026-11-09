---
title: Optimizing Marketing Operations with Artificial Intelligence and Information Technologies
url: https://doi.org/10.14445/22315381/ijett-v74i7p118
category: survey
subcategory: empirical
date: 2026-08
venue: International Journal of Engineering Trends and Technology
authors:
- Hassan Ali Al-Ababneh
- Ibrahim Alkhaldy
- Mohammed Abd-Alkarim Almomani
source: openalex-oa
pdf_url: https://ijettjournal.org/Volume-74/Issue-7/IJETT-V74I7P118.pdf
pages: 18
chars: 91447
fetched_at: '2026-11-08T19:46:24+00:00'
kb_version: 1
---

# Optimizing Marketing Operations with Artificial Intelligence and Information Technologies

International Journal of Engineering Trends and Technology                                                                   Volume 74 Issue 7, 263-280, July 2026
ISSN: 2231-5381/ https://doi.org/10.14445/22315381/IJETT-V74I7P118                                                      © 2026 Seventh Sense Research Group®

 This is an open access article under the CC BY-NC-ND license (http://creativecommons.org/licenses/by-nc-nd/4.0/)
Original Article
Optimizing Marketing Operations with Artificial
Intelligence and Information Technologies
Hassan Ali Al-Ababneh1, Ibrahim Alkhaldy2, Mohammed Abd -alkarim Almomani3, Maher Ibrahim Tawdrous4,
Noor Ahmad Alkhudierat5, Jameel Ahmad Khader6
1,2Department of Electronic Marketing and Social Media  Department, Zarqa University, Jordan.
3Department of Islamic Banking, Ajloun National University, Ajloun, Jordan.
4Department of General Education, College of Humanities, City University, Ajman, United Arab Emirates.
5Department of Business Administration, Irbid National University, Irbid, Jordan .
6King Saud University, Department of Applied Marketing, Riyadh, Kingdom of Saudi Arabia.
1Corresponding Author :  hassan_ababneh@zu.edu.jo
Received: 28 April 2026 Revised: 12 June 2026 Accepted: 18 June 2026 Published: 28 July 2026
Abstract - Digital marketing is more volatile than traditional marketing, making deterministic marketing planning to be
inadequate for allocating resources across technology -mediated channels. The existing AI -powered marketing research has
largely been focused on the accuracy of the predictions, with fewer studies focusing on the operational implications of learning
that are constrained and risk -aware. This research proposes a stochastic optimization model for marketing operations ,
considering the risk level of budget  allocation, information technology constraints and estimating the revenue using Artificial
Intelligence. The following model is proposed in which marketing operations are regarded as a stochastic resource allocation
problem, where expected revenue, revenue volatility and saturation effects, as well as budget constraints, are taken into account
simultaneously. Corporate-level marketing and financial metrics for Amazon, Walmart, Procter & Gamble, Coca-Cola and Nike
are used for empirical testing for the period 2019-2023. The nonlinear revenue response functions are estimated using gradient
boosting regression, and the stochastic optimization problem is solved using sample average approximation with 1,000 Monte
Carlo scenarios. The findings indicate that the proposed framework can improve ROIs for marketing from 1.00 to 1.23, decrease
the volatility of revenue by 26.0%, reduce the 10% VaR-based downside revenue loss from -18.2% to -10.4and enhance scenario
robustness by 55.8%. The improvement is validated throu gh statistical testing, sensitivity analysis and ablation analysis. The
study makes a contribution to engineering-oriented marketing research by offering a clear, repeatable model for decision support
in the context of uncertainty and uncertainty of marketing operations.
Keywords - Artificial intelligence, Stochastic optimization, Marketing operations, Information technologies, Risk-Aware decision
support, Digital marketing.
1. Introduction
The digital platforms, the algorithm -based customer
interactions and the real -time marketing technologies have
changed the way marketing management is being conducted
today. Marketing is not just about planning a campaign or
monitoring it following its execution. They are more and more
concentrating on continuous resource allocation, relying on an
integration of various digital channels and channels of varying
characteristics and capabilities, which are subject to
unpredictable demand, variable customer response, algorithm
changes on platforms, and budget constraints. In this case,
deterministic planning models and heuristic budgeting rules
might not capture the nonlinear and stochastic nature of the
marketing results. AI has enhanced companies' capacity to
predict customer behavior, predict campaign effectiveness and
segment the market. However, if the forecasts are correct, this
does not imply that there are better operations decisions that
can be made. There is a plethora of marketing models that are
still purely predictive in nature, but fail to provide a
framework for turning an estimate into a limited, risk -
informed approach to resource allocation. Furthermore, the
volatility of revenue and downside risk in digital markets may
be underestimated within th e traditional optimization models
and their stability of response functions and average expected
returns. This leaves a gap in methodology between predictive
analytics and stochastic decision theory, and between real
marketing operations [1]. The issue tha t this study aims to
tackle is the lack of an integrated framework that is able to
convert marketing responses estimated via AI into
operationally viable and risk -adjusted allocation decisions.
The approach suggested is derived from the stochastic
resource allocation problem explored in the literature with a

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

264
combination of the expected value of the revenue, the
volatility, the nonlinear saturation and constraints related to
information technology. This is especially true of digital -
oriented companies, where the outcomes of marketing
practices are dependent on the degree of investment, the data
infrastructure, the reactivity of the platform and the
unpredictability of customer behaviour.
1.1. Research Gap and Contribution
There are three gaps in the literature: Research on AI -
based marketing is mainly based on forecasting, classification,
personalisation or accuracy of recommendations without
introducing a formal decision rule in uncertainty for the
allocation of marketing resources. Second, in deterministic
marketing optimization models, the average expected
performance is usually maximized, thus neglecting the
volatility of the revenues, downside losses and nonlinear
response saturation. Thirdly, the role of information
technology infrastructure is taken into account, although not
often coupled in the mathematical formulation of marketing
optimisation. The novelty of this research lies in the following
three elements combined in one Decision Support System:
Artificial Intel ligence-based non -linear revenue response
estimation, the stochastic optimization of the allocation of
marketing funds and putting the operational and information
technology constraints explicitly into the model. Whereas
prediction-only models, the propose d framework is based on
estimated revenue distributions and transform these into
prescriptive allocation decisions. Unlike deterministic models
of budget allocation, it offers less volatility and risk on the
revenue side. Unlike black -box recommendation sy stems, it
assures mathematical transparency in terms of explicit
objective functions and constraints, and scenario -based
validation. The study has contributed the following elements:
• Using the constraints of budget and technology, a
stochastic optimization model of marketing operations is
developed;
• A new estimation layer is added based on the AI model to
estimate the nonlinear revenue response and the
conditional volatility, respectively;
• For the corporate level data for 2019 -2023, an empirical
protocol is provided that is reproducible;
• The proposed model is compared with deterministic
allocation, LP -based allocation and AI -prediction-only
allocation;
In addition, statistical significance testing, sensitivity
analysis and ablation analysis are added for validation of the
robustness of the results.
1.2. Motivation and Problem Statement
Digital marketing operations increasingly function as
high-dimensional, technology -mediated systems. Budget
allocation decisions are affected by real -time data flows,
heterogeneous customer responses, platform algorithm
changes, competitive pressure, and external market shocks.
These conditions make traditional deterministic planning
insufficient because fixed response assumptions cannot
adequately represent nonlinear and uncertain market behavior
[2, 3]. The principal difficulty in the study is the lack of a
single method of approach that integrates AI -based revenue
estimation into operationally oriented risk management.
While existing predictive models can be used to predict
revenue or conversion probability, they fail to automatically
allocate marketing resources to maximize profits with in
budget, volatility and technological constraints. At the same
time, deterministic optimization models are based on the
maximization of average expected return, without considering
the risks of the downside and the saturation of the levels of
response. To address this, the proposed framework is a
stochastic resource allocation problem, in which the
marketing operations are viewed as a stochastic resource
allocation problem. It is a combination of nonlinear revenue
response estimation with the aid of AI and a stochastic
optimization based on a sample. This was to enable the model
to take into account 'expected return', but also 'revenue
volatility', ‘downside exposure' and ‘allocation stability'. The
study provides a valuable and readily applicable decision -
support model in digital marketing situations.
2.1. Related Work and Theoretical Background
As markets become increasingly digital and with more
data available about customers and operations, the importance
of cost reduction in marketing is also an area that needs
attention academically , as well as on the operational side.
Earlier marketing research placed considerable emphasis on
performance measurement and marketing productivity [4],
whereas more recent studies have introduced adaptive
allocation mechanisms for digital campaigns [3]. However,
the explicit treatment of unce rtainty and dynamic ope rational
constraints remains uneven across these research streams. .
Although these initial studies contributed toward the
establishment of analytical  marketing research, they
downplayed the factor of uncertainty and dynamism in
operational decision -making. These bases (systemizing and
selecting problems from these previous “old” theories) were
expanded in later work by also importing quantitative methods
that had been developed in operations research as well as
econometrics. Linear programming and deterministic
optimization techniques have been widely used in the
literature for marketing mix decisions, channel allocation
problems [5]. Although it's been performed under the aegis of
balance models, having nothing to do with them, almost all
research using these equations seems to treat them as if they
are not truly even time -dependent, and has sought out fixed
points. Other recent works start to acknowledge that the
environment (promotion) in which marketing actions are
executed is increasingly uncertain, due to challenging demand
dynamics, changes in the platform algorithm or competitive
behavior [6]. This has led to a trend towards more probabilistic

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

265
and data -driven approaches, though the way in which
uncertainty is incorporated into operational optimization
differs between studies.
2.1.1. Artificial Intelligence and Information Technologies in
Marketing Research
The rapid development of artificial intelligence and the
intensification of information technologies have brought
significant changes to marketing analytics and decision
support systems. Customer segmentation, churn prediction,
demand prediction and personalized recommendation -based
ML algorithms are extensively  used by companies providing
Internet services [7]. These analytical methods are particularly
valuable in data -rich marketing environments because they
can represent complex, nonlinear, and high -dimensional
relationships that are difficult to capture through conventional
specifications [8].
Despite such advances, a significant portion of the
marketing literature on AI still has an emphasis on prediction
rather than  optimization. “Black -box” predictive models are
typically assessed for accuracy, without consideration of how
they translate to operational decision -making. Therefore, the
connection from AI -powered insights to resource allocation
tactics is likely implicit and heuristic. Information technology,
including cloud computing platforms and integrated
marketing information systems, has also been instrumental in
the provision of real -time data processing and cross -channel
coordination [ 9]. These environments enable scalable
analytics, but unfortunately, they do not solve the problem of
decision-making under uncertainty. Many of the mentioned
articles also concluded that operation visibility can be
increased with the use of technology and that this is not
enough to improve performance ; structured decision models
need to be implemented [10].
AI and optimization . AI is nouvelle interface for the
integration of AI and optimization. Predictive-to-prescriptive
approaches combine data -driven estimation with
mathematical optimization so that predicted market responses
can be translated into explicit operational decisions [11]. The
methods, however, are prone to treating uncertainty as
estimation error (i.e. “regret”) and are not necessarily very
good at handling environment design for optimal decision
making. This state of non -control spreads risk and
performance variance to its extremes. F rom the liter ature
search, three significant shortcomings are observed in current
AI-driven marketing research.  The literature search reveals
three key drawbacks in the current use of AI in marketing
research. Firstly, the classical OE problem criteria does not
take into account uncertainty in an explicit way. Second, there
is a lack of interpretability and analytical transparency with AI
models, because models are often black boxes.  Second,
models are a black box, which means that there is less
interpretability and ana lytical transparency . Thirdly, IT -
system-related and organizational aspects are often simplified
or neglected. These limitations  have resulted in limited
application performance of AISsMD in complex
environments.
2.1.2. Stochastic Optimization in Marketing and Decision
Sciences
Stochastic Optimization Stochastic optimization is a
general area that requires decisions to be made in an uncertain
world, and this domain has a rich tradition in the field of
operations research, decision scion empirical power demand
pattern for winter month s [12]. There were marketing
applications of some stochastic models on  inventory
management and pricing policies. The studies underpinned by
these results validate the added value of uncertainty analysis
and demonstrate that  appropriate consideration of the
uncertainty potential could effectively strengthen decision
models for a longer period.
However, I still believe the adoption of stochastic
optimization in marketing operations remains under cut. In the
literature, there were few research  works aimed at a single
aspect of marketing, such as stochastic pricing strategies [1 3]
and promotion timing models , but not to synthesize all
important factors that need to be captured in a model into one
integrated model with all layers of operations. Moreover, the
stochastic component of those models  is often ad formalized
by analytic expressions and stati onarity properties.  Recent
work highlights the potential of data -driven stochastic
optimization where probability distributions are learned from
empirical historical samples [14]. Furthermore, this strategy is
consistent with those employed by machine learning
algorithms, where complex conditional distributions can be
approximated by using artificial intelligence methods.
However, the utilization of AI -based estimation in the
stochastic optimization context of marketing  operations is
relatively less investigated. Another important issue concerns
computational scalability. As the number of decision
variables, constraints, and uncertainty scenarios increases,
stochastic optimization problems can become computationally
demanding, particularly in large-scale and multistage settings
[15]. Sample Average Approximation mitigates this difficulty
by replacing the original expectation with an empirical mean
calculated from a finite Monte Carlo sample, thereby
producing a deterministic approximation that can be solved
using established numerical optimization algorithms [20]. In
marketing, uncertainty -aware resource -allocation models
have been implemented through robust optimization for online
campaign and marketing -budget decisions [7 , 13]. These
studies provide an operational foundation for the present
research, which extends this line of analysis by integrating AI-
based nonlinear response estimation with scenario -based
stochastic optimization and explicit risk adjustment.
In more general terms, our review suggests a well-defined
methodological space  at the crossroads of stochastic
optimization, artificial intelligence and marketing operations.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

266
However, most existing works have  focused only on
prediction without minimization and optimization of decisions
in a formal decision -theoretic framework or merely employ
optimization methods without considering uncertainty
modeling and data -driven estimation. Such a gap motivates
the present study -the growing need for a systematic way to
combine stochastic optimization theory, AI -based estimation
and IT constraints in an organized and operationally
meaningful framework.
2.2. Causal Inference in AI-Based Marketing Optimization
In fact, recent advances in marketing analytics have
increasingly come to focus on the value of causal inference, as
predictive correlations are not necessarily causal. This is an
important factor in digital marketing as, in the digital space,
exposure of a campaign, customer targeting, platform
algorithms, and customer behavior all play a role in
determining this. A model can be used to precisely estimate
revenue or conversion rate, without even knowing if the
marketing intervention is responsible for the observed revenue
or conversion rate. This has led to some important
methodological developments , such as causal machine
learning, uplift modeling, heterogeneous treatment effect
estimation, and causal marketing mix modeling.
Causal inference increases the strength of marketing
optimizations by isolating from historical relationships the
effects of marketing. This is important in budget allocation,
and helps to avoid overspending on channels that may seem
successful, but are only seeing existing buyers who are likely
to purchase anyway. Causal models can also  be used to
simulate outcomes of counterfactuals - what might have
happened if the budget had been allocated differently. But
causal inference is not enough to address the o perational
optimization problem.
It can measure the treatment effects or response functions;
the additional decision models needed for allocating resources
under budget, risk and technological constraints, however, are
needed. Thus, causal inference is crucial for understanding the
marketing effects , and stochastic optimization is needed to
translate the marketing effects into operational decisions. In
this methodological zone is the present study. It doesn't
consider the estimation of AI to be a final product. Rather, an
estimated nonline ar revenue response and volatility
parameters are included in a stochastic optimization model.
This enables t he shift from interpretative and predictive to
prescriptive marketing decision support.
2.3. Reinforcement Learning and Dynamic Budget
Allocation
The sequential nature of decision -making has new
meaning and is more relevant in the context of marketing
budget allocation, with the new release of market information
sequentially, and the new reinforcement learning and
contextual bandit approaches joining them. At the channel
level, digital advertising can use reinforcement learning to
assist with the following activities: bidding, pacing, audience
targeting, and reallocating the budget.
The important advantage of the reinforcement learning
approach is that it deals with a trade -off between exploration
and exploitation. This is especially beneficial in situations
where there are dynamic elements within the platform, such as
customer respon ses or changing conditions. While these are
the advantages, there are some disadvantages of reinforcement
learning models for use in managerial and engineering
applications. The first is that they usually require a good deal
of granular-level interaction data, and sometimes this won't be
accessible in corporate studies. Second, the learning policies
of reinforcement learning are hard to interpret if a deep
learning architecture is used. Third, in many uses of
reinforcement learning, downside risk and/or rev enue
volatility and/or operational stability may not be explicitly
described, but these are optimized for. For companies that
require marketing decisions that can be audited,
interpretability and risk transparency are important. We argue
that what we prese nt in this paper is actually a stochastic
optimisation scheme, and not reinforcement learning, as we
are more explicit in the mathematical structure, are more
explicit in the representation of uncertainty in scenarios, and
give guidelines for decision maki ng based on risk. The
proposed framework is not intended to be a replacement for
reinforcement learning, but rather it can be used in addition to
it. For real -time adaptive control, reinforcement learning is
appropriate, while for transparent planning, bud get
governance and risk -sensitive allocation, stochastic
optimization is appropriate.
The literature surveyed shows that each of the four
marketing analytics methods – causal inference,
reinforcement learning, and stochastic optimization – can
address a part of the marketing decision problem. When
uncertainty is present, AI models perform w ell in predicting,
causal inference performs well in identifying incremental
effects, sequential adaptation performs well with
reinforcement learning, and resource allocation performs well
with stochastic optimization. Usually, these streams are
developed as isolated streams, however. The current
approaches, therefore, target predicting without optimizing,
optimizing without estimating uncertainty empirically, or
adaptively learning without sufficiently clear processes to be
applied to management. To fill this void, the proposed
framework includes a combination of AI -driven non -linear
revenue estimation, stochastic optimization, and explicit risk
adjustment. This integration is significant as marketing is not
only a problem of prediction, but it is also a pr oblem of
constraints. The study further contributes to the engineering
and technology-oriented marketing literature as it provides a
replicable model of the data preprocessing, AI estimation,
scenario building, optimization, statistical testing and
managerial interpretation of the model.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

267
3. Materials and Methods
The methodological design of the study follows an
engineering-oriented decision -support logic. Marketing
operations are modeled as a stochastic optimization problem
because digital advertising systems are exposed to demand
volatility, nonlinear customer re sponse, platform instability,
and budget restrictions. The proposed framework does not
treat uncertainty as external noise. Instead, uncertainty is
included as an endogenous component of the allocation
problem.
The model consists of four connected stages. First,
marketing resource allocation is formalized through decision
variables, budget constraints, cost functions, and stochastic
shocks. Second, AI -based regression models are used to
estimate nonlinear revenue  response and conditional
volatility. Third, Monte Carlo scenarios are generated to
represent alternative market states. Fourth, sample average
approximation is applied to identify the allocation strategy
that maximizes risk-adjusted marketing performance [15, 20].
Rather than the descriptive nature of traditional marketing
analytics, which measures what happened, with our approach,
we want to look forward and make use of data in a
probabilistic market that allows for optimization of decisions.
It is the treatment of uncertainty as a n endogenous
characteristic, rather than an exogenously  given noise, of the
marketing system.
Everything else is about to be a computational
approximation; formal decision -making as well requires the
coordination of formal optimization theory and analytical
reasoning. The theoretical  model comprises four intertwined
elements. The marketing operations are first formulated in an
abstract stochastic resource allocation framework and with
explicit assumptions on the decision variables, costs and
uncertainties.
Also, using data-based approximations for the conditional
expectations and variances, the stochastic revenue function is
to be estimated. iii) Sampling-based numerical approaches to
solve the stochastic optimization  problem are employed to
maintain computational feasibility. Finally, the method is
illustrated when applied to a dataset of real data collected from
multinational corporations (MNCs), in order for us to have a
quantitative assessment of performance improvements.
3.1. Data Collection, Preprocessing, and Feature Selection
The empirical aspect of this study is based on the
corporate-level data of 5 multinational firms — Amazon,
Walmart, Procter & Gamble, Coca -Cola, and Nike. The
selection of these companies was based on their being active
in markets with a high use of digital, reporting financial data
for marketing and providing conti nuous corporate reporting
for the years 2019 -2023. Data includes annual marketing
spend, % of marketing spend on digital, total revenue, revenue
growth, estimated customer acquisition cost, return on
marketing investment and lagged revenue indicators. Data
was gathered from the annual reports, investor presentations
and the corporate disclosures that were available. All
monetary amounts have been deflated to present values in
2023 USD. Consistency of observations was checked between
reporting periods. Any c ompany that did not report for the
chosen period was not included, no r interpolated. This rule
was used to ensure the data is accurate and not smoothed.
There were 4 stages in data pre-processing. The first step
was to compare all the monetary indicators to a common
currency. Secondly, percentages were converted into
decimals. Third, lagged variables were created to reflect the
lagged effects of the market ing variables. Fourth,
normalization of the input variables was done prior to model
estimation to avoid scale domination in the machine learning
training. Feature selection was done on a theoretical basis,
correlation screening and variance inflation crite ria. The final
features set consisted of marketing expenditure, digital
marketing share, lagged revenue growth, firm identifier, time-
period indicator and historical ROI. To facilitate the
reproducibility of this empirical protocol, a fixed random seed
was used for the empirical simulation, 1,000 scenarios were
used for each planning period, the same budget constraints
were applied for each of the different allocation models, and
five-fold cross -validation was applied in evaluating the
performance of the AI models. All the models (deterministic,
AI-prediction only, linear programming and stochastic
optimization models) were based on the same data and the
same metrics for evaluation.
Table 1. Dataset structure and variable description
Variable Symbol Measurement Source Role in Model
Marketing
expenditure MEXP USD billion, constant 2023 prices Annual reports and investor disclosures Main decision-related input
Digital marketing
share DSH % of total marketing expenditure Corporate disclosures and public estimates IT/digital intensity proxy
Total revenue REV USD billion, constant 2023 prices Annual reports Dependent performance variable
Revenue growth RG Annual percentage growth Annual reports Performance dynamics indicator
Lagged revenue
growth RGt-1 Previous-year revenue growth Calculated from revenue data Delayed response control

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

268
Customer
acquisition cost CAC Estimated cost per acquired customer Public marketing estimates Efficiency indicator
Marketing ROI MROI Revenue gain/marketing expenditure Calculated indicator Optimization performance metric
Firm identifier FIRM Categorical variable Constructed Controls for firm heterogeneity
Year indicator YEAR 2019-2023 Constructed Controls time-period effects

Table 1 spells out the empirical structure of the data and
the empirical roles of each of the variables in the proposed
framework. The model does not have any personal
information. Instead, it uses a set of corporate-level indicators
that are also aggregated to be suitable for engineering-oriented
decision-support analysis.
3.2. Model Assumptions and Formal Problem Definition
Marketing operations are considered to be a multi-period
process involving uncertain factors , such that the effect of
managerial activities on the ultimate goals is probabilistic.
This model is similar to those in  classical stochastic
programming used in operations research and decision
sciences [1 6]. Suppose the planning  horizon consists of 𝑇
disjoint periods. For each period 𝑡, the firm allocates its flow
of marketing spend over the 𝑛 channels.

𝑥𝑡 = (𝑥1𝑡,𝑥2𝑡,...,𝑥𝑛𝑡) (1)

where 𝑥𝑗𝑡 ≥ 0 represents expenditure in channel 𝑗. The
marketing environment is impacted by stochastic shocks 𝜉𝑡
due to demand fluctuation, customer diversity, competition
behavior and the  algorithmic modifications of digital
platforms. These disturbances are expected to have non -
identically distributed but independent distributions across
time periods. The revenue is represented as a random function:
Rt = R(xt, εt) (2)
Operational costs are defined as a convex function:
𝐶(𝑥𝑡) = ∑ 𝑐𝑗 𝑛 𝑗=1 𝑥𝑗𝑡 + 1 2 𝑥𝑡𝑄𝑥𝑡 (3)
where 𝑐𝑗 is the marginal cost of channel, and Q is a
positive semi -definite matrix  with the decreasing return
experience effect and cross -channel interference. The firm's
objective is to maximize the expected cumulative net
marketing value:
𝑚𝑎𝑥
𝑥1,...,𝑥𝑇
𝐸|∑ (𝑅(𝑥𝑡,𝜀𝑡) − 𝐶(𝑥𝑡))𝑇 𝑡=1 | (4)
subject to:
∑ 𝑥𝑗𝑡 ≤ 𝐵𝑡,    ∀𝑡𝑛 𝑗=1  (5)
This formulation ensures the existence of an optimal
solution under standard convexity assumptions [17].
3.3. AI Architecture, Training, and Validation
The AI estimation layer is a supervised regression system
for predicting conditional revenues. Gradient boosting
regression was chosen as the main model method as it does
not require a linear structure for the model, but instead is
capable of detecting nonl inear response, interaction effects,
and even saturation effects. Two other benchmark estimators
were also used: random forest regression and regularized
linear regression.
This comparison is required to confirm if there is any
added value to be gained from using nonlinear AI estimation
as opposed to simpler predictive models. The input layer
comprised marketing expenditure, the share of marketing
spends on digital marketing, lagged revenue growth, firm
identifier, year indicator and historical marketing ROI. The
dependent variable was the response in terms of revenue to
marketing expenditure. The estimated conditional mean was
adopted to represent the expected value of the re venue part,
and the residual dispersion was adopted to represent the
conditional volatility.

Fig. 1. Architecture of the AI-Enabled stochastic optimization framework
Figure. 1 shows the full analytical pipeline of the
proposed framework. The model begins with corporate -level
data preprocessing and feature selection, then applies AI -
based revenue estimation, generates stochastic scenarios, and
finally solves a risk -aware optimization problem. The output
is evaluated using both return -oriented and risk -oriented
indicators. The AI model is not intended to replace the
optimization procedure. Instead, it provides empirical
Data
Sources
Data
Preprocessing and
Normalization
Feature
Selection
AI Revenue
Estimation
Layer

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

269
estimates of nonlinear revenue responses and conditional
volatility, which are subsequently introduced as inputs into the
stochastic optimization model [11, 15, 20].  The model
training was done by five-fold cross-validation. The values of
the hyperparameters were determined by grid search. Tuned
parameters involved in gradient boosting were the number of
estimators, the learning rate, the maximum tree depth and the
subsample ratio. The metrics used for the evaluation were root
mean squared error, mean abso lute error and out -of-sample
stability. The best model for the most accurate yet stable
predictions over the validation folds was selected.  The AI
layer also adds to the interpretability , as the model's outputs
are not used as black box recommendations. Rather, the
parameters for the revenue response and the volatility are
passed into an explicit objective function. This design
enhances the transparency and allows the optimization result
to be audited. The validation results indicate that the gradient
boosting algorithm is the most stable estimation of the
nonlinear revenue. However, the comparison also shows that
the accuracy of the predictions is not sufficient. Combined
with stochastic optimization and risk adjustment, AI -based
revenue estimation delivers optimal operational performance.
Table 2. AI model training and validation results
Model RMSE MAE Cross-Validation Stability Interpretation
Regularized linear regression 0.184 0.137 0.71 Captures general direction but misses nonlinear saturation
Random forest regression 0.142 0.106 0.79 Improves nonlinear response estimation
Gradient boosting regression 0.118 0.091 0.86 Best predictive stability and nonlinear fit
AI-prediction-only allocation 0.121 0.094 0.82 Good prediction, but no direct risk penalty
Proposed AI + stochastic
optimization 0.118 0.091 0.89 Best combined prediction and allocation stability
3.4. Stochastic Revenue Estimation Using AI-Based Models
The revenue responses being random, we need to address
the empirical estimation of conditional expectations and
variances. These standard linear models cannot,  however,
represent the nonlinear saturation effects and interaction
structures (both kind s of effects are typical in digital
marketing [18]). Therefore, flexible nonparametric estimators
from the domain of artificial intelligence are employed. Then
the conditional expected revenue is:
𝑅𝑡̂ = 𝐸[𝑅𝑡|𝑥𝑡,𝑧𝑡] (6)
where 𝑧𝑡 is a vector containing observable covariates:
traffic volume, the historical conversion rate, and seasonality
dummies. The estimation problem can be expressed as:
𝑚𝑖𝑛
𝜃
∑ (𝑅𝑖 𝑁 𝑖=1 − 𝑓(𝑥𝑖,𝑧𝑖;  𝜃))2              (7)
where f is a non-linear regression function. This is in line
with the framework of predictive -to-prescriptive analytics. If
the uncertainty  in the model prediction is to be explicitly
considered, the conditional variance is estimated as:
𝜎̂𝑡 2 = 𝐸[(𝑅𝑡 − 𝑅̂𝑡)2] (8)
Variance estimation makes risk consideration possible,
which is not available to any of the previous AI -driven
marketing model s, optimizing  for mean outcome alone.
Results from the stochastic revenue estimation show that the
data-based approximation  appropriate in conditional higher
order moment s is substantially superior to that provided by
deterministic models when assessing marketing performance
under uncertainty. From this point of view, nonlinear AI
estimators allow for the recovery of  interaction effects, even
saturation and volatility nuances, which are systematically
removed by linear or heuristic tools [1 9]. One interesting
feature of this approach is that we explicitly estimate revenue
variance, which enables us  to treat uncertainty as a priori
endogenous in the decision problem rather than postulating it
ad hoc as residual noise. The method is firmly rooted in the
theoretical domain because it  is a risk -averse stochastic
optimization and allows empirical estimation to be consistent
with subsequent decisions, so that the inference of marketing
resource allocation decision -making may be more robust and
interpretable.

3.5. Risk -Aware Stochastic Optimization and Numerical
Solution
After the stochastic sales functions and uncertainty
measures are estimated empirically, the methodological
attention has to be paid to the implementation of the structure
of optimization equations, which is induced by the contrivance
of modelling the stochastic sales functions in the same easier
counterpart. This is very important, since it ensures the
validity of the analytic features of the stochastic model and
makes them available for a numerical solution. The overall
goal is to achieve stable and smooth solutions with very strong
restrictions o n operational space over such a large decision
space. For this, we make use of the classical numerical
optimization algorithms to approximate the expected values
and apply feasibility constraints and convergence conditions.
The policies outlined here offer the practica l linkage of
probability modelling and generating viable marketing
options. We trade  off the expected performance against risk

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

270
exposure so that we can use and expand our objective function
into:

𝑚𝑎𝑥
𝑥𝑡
(𝑅̂𝑡 − 𝐶 (𝑥𝑡) − 𝜆𝜎̂𝑡 2  (9)
where 𝜆 ≥ 0 represents managerial risk aversion [20]. The
resulting stochastic optimization problem does not admit a
closed-form solution and is therefore solved using Sample
Average Approximation (SAA) [2 0]. Let 𝜉t (k), 𝑘=1,…, K,
denote simulated scenarios generated from the estimated
distributions. The deterministic equivalent becomes:
𝑚𝑎𝑥
𝑥
1
𝐾 ∑ ∑ (𝑅(𝑥𝑡,𝜉𝑡 (𝑘)𝑇 𝑡=1 𝐾 𝑘=1 ) − 𝐶(𝑥𝑡)) (10)
The presented numerical procedure makes the stochastic
marketing allocation problem computationally tractable while
preserving the probabilistic structure of market responses.
Sample average approximation transforms the original
stochastic model into a dete rministic equivalent based on
simulated scenarios. This allows the optimization procedure
to compare expected return, cost, volatility, and feasibility
constraints within one decision rule. The economic
interpretation of the model is very simple. Marketing
resources are committed to channels that have a good return
on risk , and overexposure to high -volatility channels is
sanctioned. The design ensures that the model does not select
allocations that seem like good profits on average, but become
unstable in bad markets. Thus , it seems that the proposed
optimization procedure can make a more solid marketing
decision than deterministic and purely heuristic allocation
rules. The number of firms, marketing channels, planning
periods and Monte Carlo scenarios has a n impact on the
computational complexity of the proposed framework. In the
empirical setting, for each planning period, 1,000 scenarios
were created. This number was chosen due to its reliable
optimization results, while being kept manageable in terms of
CPU usage. The framework can be parallelized as the
generation of scenarios, and the prediction of revenues can be
done in parallel computing.  Generation of scenarios and
prediction of revenue can be parallelized, making the
framework suitable for medium -scale corporate decision -
support systems. The number of scenarios and firms can have
a linear increase in the computational cost (when the number
of constraints is fixed). When extra channel level constraints,
nonlinear saturation effects, or even firm -specific restrictions
are added to the problem, however, the solver time may grow
in a nonlinear manner. The model can be recalibrated on a
periodic basis instead of continuously, thus alleviating the
computational load and facilitating management usability.
Table 3. Computational scalability assessment
Number of Scenarios Relative Runtime ROI Stability Volatility Stability Recommended Use
250 Low Moderate Moderate Preliminary testing
500 Moderate Good Good Small empirical samples
1,000 Moderate-high High High Main empirical configuration
2,000 High Very high Very high Robustness validation

The study uses aggregated corporate -level data and does
not process personally identifiable customer information. No
individual-level behavioral tracking, user profiling, or
experimental manipulation was conducted. Therefore, the
empirical analysis does not  create direct privacy risks for
individual users. If the proposed framework is later applied to
customer-level marketing data, ethical approval,
anonymization, informed consent procedures, and compliance
with applicable data protection regulations should be required.
The model is intended to support transparent managerial
decision-making rather than manipulative targeting practices.
3.6. Empirical Application
In the fourth section of the methodological framework,
we provide empirical evidence  for the introduction of the
auction stochastic optimization model. Theoretical points are
self-consistent and should be tested in practice by applying on
the (real) market. Building upon this section, we generalize the
approach and apply it to the data of online active players with
multinational status. The purpose here is to see if the model
works (performs in the expected direction , note it is not hard-
coded) with respect  to enhancing performance  (lowering
variance) as incorporated in expected return, where versioned
allocation strategies could be developed. Linking the
simulation prototype with observed data on financial
satisfaction and marketing evolution, this study provides a set
of quantitative results concerning the effectiveness and
"lifetime" of the model.  The proposed research area in this
paper is an experimental investigation of the proposed
stochastic optimization process and its possible applications to
make marketing more efficient.
The foregoing discussion provides a theoretical and
numerical background for this concept; however, empirical
research would be required to show the practical importance
and robustness of this concept [21]. There were three baseline
models used to assess th e contribution of the proposed
framework. The first baseline was of a deterministic historical
allocation. It allocates the marketing budget based on the
proportions of the marketing budget spent in the past and the
average performance observed. This is a common practice,
and hence the baseline is realistic. The second baseline was a
linear programming allocation without a variance penalty.
This model will be best for maximizing the expected
marketing return for a given budget, but it will not explicitly
include consideration of revenue volatility or downside risk. It

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

271
was added to evaluate the value of the stochastic risk
adjustment. The third baseline was for allocation only using
the artificial intelligence prediction. In this model, the budget
allocation is determined by the best forecast increase in
revenues that the AI estimator makes. This baseline was added
to determine if there is a need beyond prediction for
operational decision -making. The model proposed in this
document is different from all the baselines as it includes two
different steps: Nonlinear AI -based revenue estimation and
stochastic scenario generation, along with a risk -adjusted
objective function. Hence, when comparing the predictive
performance, robustness, stability and downside protection
must be looked into. Table 4 shows Marketing & Performance
data (line base for up to 01.01.2019 to 01.01.2023.
Table 4. Baseline marketing and performance indicators
Company Avg. Marketing Spend (USD bn) Digital Share (%) Avg. Revenue (USD bn) Revenue Growth (%)
Amazon 42.0 68 514.0 11.8
Walmart 11.5 54 611.0 6.4
Procter & Gamble 9.2 51 82.0 5.9
Coca-Cola 4.3 48 43.0 7.2
Nike 3.9 62 51.0 9.1

These findings  create a ground -truth baseline against
which we compare results from our stochastic optimization
framework. Company -specific revenue is a function of
marketing costs  and digital intensity, while the conditional
mean and variance of revenue are obtained through historical
observations.
Table 5. Baseline models and evaluation logic
Model Decision Logic Uses AI Estimation Includes Risk Penalty Main Limitation
Historical
deterministic
allocation
Uses historical spending
shares No No Ignores uncertainty and nonlinear response
Linear programming
allocation
Maximizes expected return
under constraints No No Assumes stable response and average returns
AI-prediction-only
allocation
Allocates budget to the
highest predicted return Yes No Ignores volatility and downside risk
Proposed stochastic
optimization
Maximizes risk-adjusted
expected return Yes Yes Requires scenario generation and parameter calibration

The approximation provides "hard"  nonlinear response
functions with decreasing marginal returns. In a stronger
speciation, revenue variance grows in a non-linear fashion
with expenditure levels - capturing the increasing exposure to
demand risk and platform uncertainty. For example, Table  6
presents a summary of these estimates for the expected
marginal return and revenue variability associated with
additional marketing budget.
Table 6. Estimated stochastic revenue response parameters and risk characteristics
Company
Avg. Marginal
Revenue
Elasticity
Saturation
Threshold
(USD bn)
Expected
Revenue Gain
per USD 1M
Revenue
Variance
(σ²)
Coefficient of
Variation (CV)
Downside
Risk Index
Amazon 0.41 38.5 1.32 0.087 0.29 High
Walmart 0.36 10.8 1.18 0.064 0.24 Medium
Procter &
Gamble 0.33 8.9 1.12 0.058 0.22 Medium
Coca-Cola 0.29 4.1 1.15 0.041 0.19 Low
Nike 0.38 3.6 1.26 0.071 0.27 Medium - High
(based on empirical estimation of conditional revenue functions, 2019  - 2023)
Table 6 is a multivariate summary of the estimated
stochastic revenue response parameters for  the firms studied.
In contrast to composite first-order indicators, these quantities
measure explicitly both the responsiveness and risk
dimensions of marketing investments, which are at the core of
the stochastic optimization model. The estimated average

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

272
marginal revenue elasticity shows a significant degree of
heterogeneity across firms, with firms showing the same
proportional increase in ME having very different responses
to revenue.
The higher elasticity estimates in Amazon and Nike
suggest that their revenue is more responsive to additional
marketing investments in the short -run driven by the
scalability of their digital platforms and greater marginal
effectiveness of performance -based advertising. Lower
elasticity values in Coca -Cola and Procter & Gamble , as
compared to Amazon , indicate more mature brands where
brand structure is relatively stable, but less responsive to
demand patterns. The saturation threshold parameter deliver s
important information about nonlinear effects and the law  of
diminishing returns. The greater the saturation threshold, the
more marketing a firm can digest before it runs out of positive
marginal returns; screen slopes of firms with lower thresholds
fall more steeply due to accelerating saturating effects. 1 This
is crucial to optimization, as it blocks global optimality
properties where resources are systematically allocated to
other channels or firms operating close to saturation. Measures
related to risk f urther enhance the analysis. The variance of
revenue (σ²) and the coefficient of variation (CV) measure the
spread of the revenue outcomes given marketing investment.
Higher CV values for Amazon and Nike suggest higher
relative uncertainty, thus more vulnerability to demand
variation and platform -related variations. In contrast, smaller
CV ratios for Coca -Cola indicate more stable cash flows
driven by demand for a well-entrenched brand. The downside
risk index aggregates the tail -risk properties in  negative
markets. In general, firms categorized as having high or
medium - high downside risk are more  sensitive to negative
shocks, suggesting that variance penalties need to be included
in the objective function [22]. Results in Table 2 show that not
only do marketing investments vary with respect to their
expected effectiveness, but they also have different overall
risk levels and varying nonlinear responses. These results
empirically support the use of a  stochastic optimization
approach versus deterministic all ocation rules. Through the
explicit inclusion of elasticity, saturation and variability
parameters, the methodology provides a risk -sensitive
differentiation in resource allocation decisions that reflects
firm-specific operational settings. As such, Table 3 provides
essential empirical input for the later optimization phase and
points to a potential way of bridging purely data -driven
estimation with analytical decision making. The stochastic
optimization model is solved individually by the firm through
a Monte Carlo simulation technique with 1,000 scenarios for
each planning period. In each case, stochastically realized
demand and platform  effects are generated according to
estimated distributions. Optimization  of this problem
computes the allocation vector to maximize the expected risk-
adjusted performance. The threshold comparison model is the
baseline deterministic allocation model based on historical
spending shares. This standard represents good management
practice and may be used as a basis for  an asses sment of
achievement in improving performance. Results from
Deterministic Vs Stochastic Allocation: Table 7.
Table 7. Comparison of deterministic and stochastic allocation outcomes
Metric Deterministic Allocation Stochastic Optimization Relative Change (%) Statistical Stability
Expected Marketing ROI 1.00 1.23 +23.0 High
Median ROI 0.94 1.18 +25.5 High
Revenue Volatility (σ) 1.00 0.74 -26.0 Improved
Downside Revenue Loss
(VaR, 10%) -18.2% -10.4% -42.9 Substantial
Allocation Concentration
Index 0.61 0.44 -27.9 Improved
Budget Reallocation
Frequency High Low - Stable
Scenario Robustness Score 0.52 0.81 +55.8 High

The performance comparisons in Table 7 reveal that the
stochastic optimization approach has several empirical
advantages compared to deterministic marketing allocation
methods. The stochastic model shows consistently better
expected values and marketing system robustness to variations
in sales levels across all measures of performance. The fact
that the forecasted and median ROI is higher t han what one
would expect  in perfect information indicates that
consideration for uncertainty not only decrease s risk but also
increases the efficiency of resource consumption. One of t he
most significant results is how much both revenue volatility
and lowest outcome losses are reduced. These measures
reflect the capacity of the model to avoid large losses by
embedding adverse market  conditions in its internal
optimization. In turn, deterministic active - allocation
constructs are much more sensitive to variations in returns on
the downside (thus higher performance dispersion) and then a
larger negative tilt. Furthermore, the decrease in allocation
concentration index tends to indicate tha t the stochastic
framework facilitates a fairer sharing of marketing resources
among channels, along with lower dependence on individual
high-risk allocations. The robustness score of the improved

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

273
scenario is the reliable performance in simulated markets, so
it shows that this model can be used to generate consistent and
repetitive decisions. Overall, the improved performance of
stochastic optimization in Table 3 provides not only support
for better expected returns, but  also that structurally more
robust marketing strategies can be observed. This enhanced
efficiency and robustness, released as an important feature of
the proposed method, enables operating  this model and
motivate for marketing operat ions over fluctuating digital
markets. Robustness: It uses sensitivity analysis with respect
to the level of risk -aversion 𝜆 and budget constraints as a
robustness check. As 𝜆 increases, the model progresses to
overlapped rows in portfolio allocation with larger variances
and smaller expected returns. Nevertheless, we do see that the
stochastic model is still generally able to perform even better,
and generate stability, than its deterministic scale -invariant
reference for most values of parameters that one may
reasonably expect. Their results demonstrate that stochastic
optimization provides benefits not just due to hyperparameter
tuning, but because it enables decision -making based on
uncertainty.
The methodological model of this  article establishes a
firm base for the regulation of marketing efficacy in the
structurally unstable and technically complex environment.
This approach surpasses deterministic and heuristic models of
marketing problem solving and appears to be advanced
compared to the optimization technique for the decision -
making problem in marketing, formulated by means of
stochastic programming , providing a joint account of both
uncertainties, risk and practical restrictions. The aim of this
specification is to maintain  an internal coherence between
empirical estimation, optimizing logic and management
interpretation. The main methodological innovation is to mix
stochastic programming theory with data -based estimation in
both revenue response functions and volatility parameters.
In contrast to prevailing methods, which are average -
impact-based or separate the forecasting from the decision
making (prediction and decision are made independently), our
approach injects added measurement uncertainty information
into this optimization criterion. This , in turn , will allocate
marketing budget, not just  based on estimated response over
improvement, but also explicitly with the Variance, Downside
risk and nonlinear saturation effect. Thus, marketing is
represented as a controlled stochastic system and not as a static
search for design [23]. In terms of scientific contribution, this
study illustrates how OR and decision science theory can be
adapted to a complex context in marketing and hence
contributes to the engineering -oriented marketing literature.
Sample-based approximation and risk -adjusted objective
functions provide a saleable and analytically tractable method
to address high -dimensional investment  problems under
uncertainty. The practically, the framework has an implication
to marketer s that  it may be a vital market structure to limit
marketing capability both with respect to efficiency and
stability of outcomes by applying on digital threaded markets
exposed to frequent external disruptions. Yet despite these
merits, there are several methodological limitations that must
be taken into consideration. The implementation is empirical,
since firm-level aggregated data would be used to describe the
(estimated) level stationarity of response distributions over
time. Moreover, the current mode l is unable to account for
competition-based strategic encounters among rival firms and
does not capture the reverse influences of advertising activities
on long-term brand equity.
Also, the computational overhead may be notably
increased as the decision variables and scenarios increase. The
methodology proposed here is the first of its kind , so that
marketing quantitative stud ies can be implemented in the big
data environment , which contains a lot of uncertain
information. This model can be extended with more dynamic
learning mechanisms, game -theoretic rhetoric competition
and perhaps even to adaptive learning in real -time. Other
incorporation of pricing, supply chain and custo mer lifetime
value models also promise to further develop stochastic
optimization as the bridging tool for strategic marketing
management.
4. Results
Our intention with the following section is to try to
analyse and discuss the outcomes of our application of a real -
world marketing operation using the proposed stochastic
optimization framework. In terms of methodology, on one
side its theoretical consist ency and computational skills,
emphasizing the empirical, that is , maximum sample
predictivity of performance and realistic model/ explanatory
interpretative fit. To do this, the quantitative results are
emphasized, and claims backed up by strong evidence and
comparative performance are stressed instead of descriptive
claims, as is frequently the case in engineering empirical
research. The evidence is gained by empirically applying a
stochastic investment optimization approach to a sample of
MNEs in digital-intensive industries [22, 23].
Companies have different market organizations, budget
amounts and risk preferences for which the generalization of
the method can be a good proving ground. The results of the
study are presented in standardized performance measures for
comparison. I n order to be transparent in the analysis, the
results are presented as representative with deterministic
benchmark strategies, which represent an approximation of
the most popular managerial practice. This correspondence
divides up the value added from the explic it modelling of
uncertainty in optimization. It is not only that, but they also
provide an understanding of how and why these changes are
happening based on the logic of marketing operations and
stochastic optimization theory. It is aimed at clarifying the link
between the design choice and the empirical evidence
observed (the implicit value  of this section) and at
strengthening the internal validity of the analysis.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

274
4.1. Quantitative Performance Outcomes of Stochastic
Optimization
Our stance regarding the quantity evaluations is to create
a first baseline benchmark that can be compared with the
performance of our Stochastic Optimization Model.
This baseline is  a deterministic rule of marketing
allocation, which ensures that the proportionate shares for
historical spending allocations are times -corrected by period
average performance indicators. That’s how big corporations
operate, and this is the pragmatic model that will be used to
evaluate you. Let 𝑅𝑂I𝐷 and 𝑅𝑆I be the return on investment
of D and S, respectively, while 𝜎𝐷 and ⁡ 𝜎S are the standard
Deviation of revenue. The performance metrics are
normalized to the results using the deterministic baseline; thus,
we can compare performance across companies.
The use of the stochastic optimization model  results in
equivalent and statistically significant enhancement in
expected marketing outcomes for all firms studied here.  This
kind of behavior shows up in both the mean  performance and
on the median; a bet against bad realizations. In Table 8, the
aggregate performance indicators for  Deterministic and
Stochastic models are presented.
Table 8. Aggregate performance metrics: deterministic, stochastic models
Metric Deterministic Model Stochastic Model Relative Change (%)
Expected Marketing ROI 1.00 1.23 +23.0
Median Marketing ROI 0.94 1.18 +25.5
Revenue Volatility (σ) 1.00 0.74 -26.0
Downside Revenue Loss (VaR, 10%) -18.2% -10.4% -42.9
Allocation Stability Index 0.58 0.79 +36.2
Table 9. Statistical significance of model improvements
Performance Indicator Mean Difference Statistical Test p-value Result
Expected marketing ROI +0.23 Paired t-test 0.018 Significant
Median marketing ROI +0.24 Wilcoxon signed-rank test 0.021 Significant
Revenue volatility -0.26 Paired t-test 0.026 Significant
Downside Revenue Loss (VaR, 10%) +7.8 Bootstrap confidence interval 0.031 Significant
Scenario robustness score +0.29 Paired t-test 0.014 Significant
Allocation stability index +0.21 Wilcoxon signed-rank test 0.024 Significant
The observed improvements are statistically significant as
shown in table 9. The definition of downside protection used
in this study is a decrease in the Value-at-Risk at 10% level of
the lower tail loss of revenue.
The difference between the deterministic allocation (VaR
= -18.2%) and the stochastic optimization (VaR = -10.4%) is
instead a measure of the downside loss of revenue (not of the
worst-case outcome) from an allocation problem.
The worst case is detailed as a separate part of the
downside risk analysis. At the 5% significance level, the
results are very strong for marketing ROI, revenue volatility,
downside protection, robustness and stability of allocation . A
paired t -test was used for normally distributed differences,
while the Wilcoxon signed -rank test was used as a
nonparametric robustness check.
Bootstrap confidence intervals were applied to downside
risk indicators. The results reveal that stochastic optimization
remarkably improves the expected returns at the same time of
decreasing downside risk. What’s most crucial is that the ROI
gain is excellent also  at the median level, meaning it’s not a
few super positive examples that make this result, but it holds
across all ranges.
While cross-sectional evidence contributes to optimizing
around model performance , firm-level analysis reveals
significant dispersion in performance, which outlines differing
market structure, digital preparedness and demand
fluctuations. The improvement in performance might be due
to several architectural features of the stochastic optimization
toolkit. The variance -penalty term provides a direct
punishment for heavy allocation in the channels with high
volatility marginal return.
Table 10. Firm-level expected ROI improvements
Company ROI (Deterministic) ROI (Stochastic) Improvement (%)
Amazon 1.00 1.27 +27.0
Walmart 1.00 1.19 +19.0
Procter & Gamble 1.00 1.17 +17.0
Coca-Cola 1.00 1.15 +15.0
Nike 1.00 1.24 +24.0

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

275
This in turn leads to even more  diversified marketing
investment portfolios, in a similar way as has been described
in the financial portfolio theory of diversification. Second, the
non-linear response estimate tells us that there are saturation
points where even  additional spending results in diminishing
returns. Determinate methods miss such nonlinearities ,
enabling continual over -investment in channels that have
performed well  historically. On the other hand, stochastic
optimization modifies facilit y allocation at different
timestamps on the basis of estimated returns and risk-adjusted
marginal gains. Lastly, scenario-based evaluation is employed
in the model to include  bad market realizations into the
optimization. Specifically, the best strategies are anyways
more robust to downward shocks by their very nature: this can
be in large part the reason why the reduction of negative losses
can be quite dramatic , as we observe in Table 11. In addition
to the performance measures, stochastic optimization yields
structural changes in terms of how marketing resources are
allocated between channels and across time. Analysis of the
pattern of allocation  reveals lower convergence and higher
temporal. Such changes in the level of the firm reduce
operations volatility and also protect managerial effort from
costly adjustments to ongoing short -term perturbations. This
stability also enables the marketing function to share
information and coordin ate the gentilities in marketing areas
[23]. The experimental studies reported in this section
empirically confirm the underlying assumptions of the
proposed method. Our approach leverages the empirically
estimated uncertainty for the optimization objective, which
outperforms state -of-the-art methods in interpretability and
operation validity. The evidence for the match between
theoretical predictions and possible reality provides further
support for the internal structure of the proposed framework
and its practical value in marketing.
Table 11. Allocation structure indicators
Indicator Deterministic Stochastic Change
Channel Concentration Index 0.61 0.44 -27.9
Avg. Reallocation Frequency High Low ↓
Inter-Period Variance High Moderate ↓
4.2. Risk, Stability, and Robustness Analysis
And in marketing operations, the risk appears not only as
variance in results but  also as structural fragility to the bad
realization of markets. On the other hand, marking risk never
consists of pure variance but also show s asymmetric loss
distribution and the  nonlinear response effect, the
impossibility of forecasting or conditional on the Change in
means of financial market factors for performance.
A good risk analysis standard will thus have to be not only
more refined than vulgar historic volatility, but it will also pin
down downside exposure, as well  as allocation and inter -
temporal consistency. Explicit risk models are included in the
stochastic optimization approach, with variance penalization
and marketing outcome scenario analysis.
This procedure implies that uncertainty is relegated from
an ex-post concern to an ex-ante one. The performance of the
method we propose will be evaluated in this subsection on
volatility reduction, downside risk management and
robustness for portfolio optimization across markets.   The
ambiguity in revenues, the mutability of sales , is a major
indicative of operational risk , as too  high fluctuations will
destroy forecast planning and bloated performance
measurement, and they lend to non-optimal outcomes. The SD,
as well as the IQR of revenue differences between scenarios ,
are considered to capture its variability  (i.e. volatility)
captured over simulated alternative scenarios . Such a distinct
reduction in the revenue spread can be seen in our results for
the experiment with stochastic optimization. This reduction in
volatility can be attributed not to prudent underinvestment, but
rather to a better risk -adjusted allocation [24, 25]. The model
is punishing high-variance revenues and redirecting resources
toward more stable channels with marginal returns. And also,
'theoretically', you can put it under the category of Stochastic
Programming in that all these maximizing a risk -adjusted
expected value type solution s should provide portfolios with
return and risk. For marketers, this balance promises linear
revenue growth and a reduced risk that performance will go
wild. There are several volatilit y measures available as
representations of the general dispersion, but having a
measure reflect the extent of extreme negative events is more
difficult to obtain  [26]. As well, risk -downside-type-analysis
is considering the tail of revenue-distribution and, in particular,
those cases where (the few remaining) revenues are worse
than everybody else, which again causes a severe problem for
the firm. We have already assessed the downside risk by
estimating the Value-at-Risk (VaR) and Conditional Value-at-
Risk (CVaR) statistics of both allocation mechanisms.
Table 12. Revenue Volatility Metrics Across Models
Metric Deterministic Allocation Stochastic Optimization Relative Change (%)
Standard Deviation (σ) 1.00 0.74 -26.0
Interquartile Range 1.00 0.78 -22.0
Coefficient of Variation 0.31 0.22 -29.0

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

276
Table 13. Downside risk indicators
Indicator Deterministic Stochastic Improvement (%)
VaR (10%) -18.2% -10.4% -42.9
CVaR (10%) -23.7% -13.8% -41.8
Worst-Case Outcome -31.5% -18.9% -40.0

The low tail risk losses also to the evidence  that indeed
our stochastic optimization further suppresses (means
arbitrary shifts) its harmful effects toward the other tails. This
is especially relevant to an in-house marketing team where the
impact of poor performance can be felt long -term on both
brand and budget.
When the CVaR decreases, a small amount of damage
results if it comes to the worst. This result illustrates the
benefit of scenario-based optimization when it can be used  to
consider low-derived but high-impact scenarios that occur in
a structured manner.
Operational stability is  a critical, if overlooked, urn
component of market effectiveness. The increased likelihood
of erratic budget allocations can upset implementation, raise
the costs of coordination and dissuade organizational learning.
Hence, stability is measured by observing  the inter -period
variation of the assignment vectors . Let x t be the allocation
vector at  period t. It is intuitively plausible that a stable
allocation should not include any discontinuity over time, and
we measure it by the average one-period distance between two
consecutive allocations:
∆=
1
𝑇−1 ∑ ‖𝑥𝑡+1 − 𝑥𝑡‖𝑇−1 𝑡=1   (11)
As shown in Table 13, the degree of persistence of the
foreign investment shares is far higher when stochastic
optimization is used. This perseverance is derived from the
model memorizing uncertainty and anticipating future
variability to prevent reactionary changes in response to recent
swings in performance.
Table 14. Allocation stability metrics
Metric Deterministic Stochastic Change
Avg. Inter-Period Distance High Moderate ↓
Reallocation Frequency High Low ↓
Allocation Persistence Index 0.62 0.81 +30.6

Managerially, the correlation between marketing teams
and long-term strategic programs becomes clearer with higher
stability. And importantly, stability does not need rigidity: the
model can still be set to change its prices in response to
adjustments that are made along  with changes in market
structure.
Robustness and plausible parameters robustness is the
ability of a strategy to remain valid for plausible parameters
(and even beyond), where ‘plausible’ refers to the relation of
robustness with respect to the parameter. Regarding the
soundness and performance of allocation methods in multiple
equilibrium games capturing fluctuating levels of demand,
rivalrous pressure and platform dynamics.
One can try  to do this in the aforementioned approach,
and you will find that , comparing them, the stochastic model
is far more resilient , having a positive ROI for most of the
cases, even [27]. The robustness score, which is the ratio of
mean performance to dispersion of performances , shows that
our model maintains favorable behaviors even in unfavorable
conditions. Such a strength is due  to propagating uncertainty
in the optimization process itself, provided by the scenario -
based setting. Unlike determinis tic optimization , which
mentally averages things out, stochastic optimization “gets
ready” for  variability, improving resilience. To examine  the
sensitivity of value to managerial risk preference, we vary the
degree of risk -aversion parameter 𝜆 within a broad scope , as
one would expect, larger λ result s in the more modest
allocations that reduce variance and consequently have a
slightly lower mean return. Conversely, over a wide range of
parameters, the stochastic optimization remains the superior
strategy both in terms  of stability and of downside protection
when compared to deterministic benchmarks [28].
This suggests that the use of stochastic optimization is
invariant to reasonably high levels of variation in risk attitudes
and could serve as a performance -improving device even if
accurate parameter calibration is not available. This can add
robustness to the  methodology and enable it to be applied
more uniformly in different organizations with distinct
strategies.
This sub -section analysis later indicates that using
stochastic optimization offers a significant change in the risk
of exposure of marketing  operations. New approach features
lower revenue volatility and  downside risk, more allocation
stability, and robustness across scenarios. Taking into account
these properties, we are able to satisfy  the impact needs and
still remain slightly below the SOPT target . U ncertainty-
informed optimization, however, is thus a better approach to
the marketing of operations in uncertain online marketplaces.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

277
Table 15. Sensitivity analysis by risk-aversion parameter
λ
value
Expected
ROI
Revenue
Volatility
Downside Loss (VaR,
10%)
Robustness
Score Interpretation
0.00 1.29 0.91 -15.7% 0.67 Higher return, weaker risk control
0.10 1.26 0.82 -12.9% 0.74 Balanced improvement
0.25 1.23 0.74 -10.4% 0.81 Best risk-return balance
0.50 1.17 0.68 -9.2% 0.83 Stronger stability
0.75 1.11 0.63 -8.7% 0.84 Conservative allocation

Sensitivity analysis was conducted to verify whether the
model’s results depend on a narrow parameter setting. The
risk-aversion coefficient λ was varied from 0.00 to 0.75. The
results show that the proposed stochastic optimization model
remains superior to deterministic allocation across all tested
values. Lower λ values increase expected ROI but reduce
downside protection, while higher λ values improve stability
but reduce expected return.
Table 16. Ablation analysis of model components
Model Variant Expected ROI Revenue Volatility CVaR 10% Allocation Stability Interpretation
Full proposed model 1.23 0.74 -13.8% 0.79 Best overall balance
Without AI, nonlinear
estimation 1.12 0.83 -17.4% 0.68 Lower ability to capture saturation
Without a variance
penalty 1.28 0.96 -21.6% 0.61 Higher return but excessive risk
Without scenario
simulation 1.15 0.88 -19.2% 0.65 Weak downside protection
Deterministic allocation 1.00 1.00 -23.7% 0.58 Baseline

Ablation analysis was conducted to identify the
contribution of each model component. The full model was
compared with three reduced variants: without AI -based
nonlinear estimation, without variance penalty, and without
scenario simulation. The results sho w that the strongest
performance is achieved only when all three components are
combined.
4.3. Comparative and Managerial Interpretation of Results
The empirical results indicate that the proposed stochastic
optimization framework achieves better performance than
deterministic allocation because it changes the logic of
marketing decision-making. Deterministic modelling relies on
the assumed average return that has been achieved in the past,
and is based on the assumption that the market will react to the
return as it did in the past. The assumption is incorrect in
digital markets where changes in algorithms, demand and
competition levels, as well as cu stomers' behavior, are rapid.
The proposed model does not have this drawback – instead,
the element of uncertainty is embedded into the objective
function. The proposed framework does better than using only
AI predictions for allocation since it is not restricted to using
the predicted revenue as the only allocation criterion. This can
apply to a channel that has a high predicted revenue, but high
volatility and high downside risk. Variance penalty is
introduced, and scenario -based evaluation is introduced to
avoid the concentration of excessive resources in such
channels. This is why this model is good for ROI, as well as
minimizing the volatility of revenue and worst -case loss. The
proposed model is more understandable than reinforcement
learning models [29] and is more easily audited. But there may
be benefits to using reinforcement learning for real -time
adaptive advertising, even if this can be a difficult problem to
solve with user-level data, and the policies may be difficult to
interpret. This study h as an optimization model with risk
parameters, explicit equations and explicit constraints. For an
enterprise decision support system that requires explainability,
governance and budget accountability, it's a suitable choice.
Compared with causal marketing mix models, the proposed
framework is more directly prescriptive. Causal models
estimate incremental effects, but they do not automatically
determine how resources should be allocated under risk and
budget constraints. The p roposed approach can use causal  or
predictive estimates as inputs, but its main contribution is the
transformation of estimated response functions into
operational allocation decisions  [30]. The results therefore
show that the improvement is not caused by predictive
complexity alone. Better outcomes are achieved because the
model integrates nonlinear AI estimation, stochastic
uncertainty representation, risk -aware optimization, and
explicit budget constraints. This combination provides a
stronger engineering basis for marketing opera tions
management in volatile digital markets.
5. Discussion
The results of the empirical study also serve as more
evidence that a random optimization is an effective analytical
tool to optimize marketing under uncertainty in the digital age.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

278
The first important observation is that expected and median
marketing performer s continue to rise for all the analyzed
firms. Stochastic versus Deterministic Reallocation: The
stochastic approach characterizes the allocation by risk -
corrected marginal rather than mean average historical effects,
like deterministic models. This distinction is crucial because
RF also serves as a dynamic way to endow nonlinearity
response shapes on the optimizing process, protects against
systematic over - investment in channels near or at saturation.
The magnitude and frequency of such improvements are
remarkable as well, suggesting that any stochastic search will
yield structural to very emergent benefits. They’re not some
artifact of a handful of lucky realizations, but occur anywhere
and everywhere in the space of outcomes. The higher median
result also corroborates that which was observed  in the
previous experiments , namely, that the stochastic approach
enhances typical overall performance, rather than just the best-
case. T his finding challenges the intuition of classical
managers that decision models built under uncertainty should,
by definition , trade off between expected performance and
risk management. On the contrary, we obtain that explicitly
citing uncertainty, it is possible to remove biases related with
deterministic approaches and organize resources more smartly
even in an ordinary market situation. The paper's second major
finding is a dramatic reduction of  revenue volatility and
downside risk. The history of sales  volatility. There’s a dirty
little secret in the marketing/sales world that everyone kind of
knows, but really doesn’t talk about.
But the data studied in this study suggest that volatility is
also endogenous to a large  degree, caused by the
organizational context. Sensitivity to deterministic allocation
policies is that they tend to amplify volatility through priority
of the most successful channels and lack of attention to
dispersion & tail nature of channel performance. As a  result,
these approaches are very sensitive to extrapolations. In
contrast, the SO framework reshapes a distribution of
advertising response in its entirety. Th rough the inclusion of
variance penalties and this kind of scenario dependence in the
objective function, our model will optimally hedge away risks
from a high-variance revenue stream. This feature explains the
highly significant reduction in extreme weighted downside
risk standard Deviation and interquartile range loss (in fact,
our results indicate  a lower impairment in Value -at-Risk -
VaR – as well as in Conditional Value At-Risk - CVaR)
achieved by this approach. Most importantly, these efficiency
gains are delivered with no sacrifice in expected return, further
emphasizing the efficiency of risk-adjusted choices. This type
of downside risk reduction is extremely important,
particularly for digital marketing activity, and reflects the fact
that the impact on what comes out of the “negative side” can
be much bigger at a strategy level as opposed to those coming
from the positive s ide. Take, for instance, the most severe
level of underperformance in any given period  that results in
cuts to the budget by destroying long-term plans or, even more
drastically, destroys confidence in marketing actions. The
results demonstrate  that stochastic optimization has a
favorable worst-case loss, which is due to confining the worst-
case losses in an efficient manner , as it forces negative
examples inside rather than outside of the margin. There is a
principle in the front and proactive risk control, which is much
different from in the past to fabricate marketing plans.
Collectively, increasing expected performance and decreasing
volatilities suggest an important conceptual implication of the
study: efficiency is not all or nothing in the activity. This
balance is not available in traditional deterministic models,
which could justify why managers  are forced to abandon risk
control for growth. A stochastic model shows that the two
targets are possible because “the  decisions are based on
uncertain scena rios, and uncertainty is included in their
decision-making reasoning”. From a theoretical point of view,
this feature is closely related to the classical models in
stochastic control and portfolio optimization (compare also
with the notion used in them of objectives for the firm on its
search for a trade-off between one -way return and other way
risk). Therefore, the primary essence of stochastic
optimization lies in repairing the fundamental deficiencies of
average-tracking decision protocols. With the abandonment of
ordinary averages and an examination of the distributional
properties of marketing responses, better performance, as well
as more robustness , can be generated in such a firm. Thus,
what we show in this paper is a solid argument to turn back
the clock or conventional planning adaptation and take on
uncertainty-aware optimization as an essential asset of our
modern market action.
6. Conclusion
This paper proposes and tests a stochastic optimization
model of marketing operations assisted by artificial
intelligence and information technologies. The issue that was
tackled foremost was the inability of deterministic and
prediction-driven marketing a pproaches in dynamic digital
contexts. The proposed framework is based on a stochastic
decision problem framework that incorporates the risks of
marketing budget allocation, expected revenues, risk
variability, and nonlinear saturation, as well as budgetary
constraints. The empirical results validate the effectiveness of
the proposed approach.
The stochastic optimization model enhanced expected
marketing ROI from 1.00 to 1.23, median ROI from 0.94 to
1.18, reduced the volatility of marketing revenue by 26.0%,
reduced the 10% VaR -based downside revenue loss from -
18.2% to -10.4% and increased the robustness of the scenarios
from 0.52 to 0.81. . These differences were proved to be
significant by statistical analysis and not merely descriptive.
Results from sensitivity analysis indicated that the model was
robust to various values of the risk -aversion parameter, and
ablation analysis indicated that the model yielded the best
results when all three components were combined: AI -based
nonlinear estimation, variance penalty, and scenario
simulation.

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

279
The theoretical contribution of this study involves linking
the AI -based revenue estimation to stochastic optimization
and logic for decision support using IT. The value of this
practical one is to give marketing managers a clear structure
for allocating r esources in the face of uncertainty, and for
regulating volatility and downside risk. The model can be
applied in a planning and governance framework in digital -
intensive companies where marketing performance is reliant
on the expected return and operation al stability. There are
some limitations in the study. The empirical validation is
based on corporate -level data and not individual customer
behaviour. The impact of competitive reactions and long-term
brand equity effects is not fully captured either. The model
could be expanded in future studies to include causal treatment
effect estimation, reinforcement learning, real -time campaign
data and game-theoretic competition models. Despite all these
limitations, the results show that marketing operations can b e
made more efficient, stable, and resilient by applying risk -
aware stochastic optimization in complex digital contexts.
Acknowledgement
The authors thank the reviewers and editorial office for
their constructive comments, which helped improve the
quality and clarity of the manuscript.
Funding Information
The authors received no specific funding for this study.
References
[1] Zakaria Yahia, and Mostafa ElBolok, “A Stochastic Nonlinear Programming Model for Budget Mix of Digital Marketing Campaigns
Under Practical Constraints,” Future Business Journal, vol. 11, no. 1, pp. 1-28, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[2] Bingkun Wang, and Pourya Zareeihemat, “Multi-Channel Advertising Budget Allocation: A Novel Method using Q-Learning and Mutual
Learning-based Artificial Bee Colony,” Expert Systems with Applications, vol. 271, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[3] Marco Gigli, and Fabio Stella, “Multi-Armed Bandits for Performance Marketing,” International Journal of Data Science and Analytics,
vol. 20, no. 1, pp. 151-165, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[4] Roland T. Rust et al., “Measuring Marketing Productivity: Current Knowledge and Future Directions,” Journal of Marketing, vol. 68, no.
4, pp. 76-89, 2004. [CrossRef] [Google Scholar] [Publisher Link]
[5] Yossi Luzon, Rotem Pinchover, and Eugene Khmelnitsky “Dynamic Budget Allocation for Social Media Advertising Campaigns:
Optimization and Learning,” European Journal of Operational Research, vol. 299, no. 1, pp. 223-234, 2022. [CrossRef] [Google Scholar]
[Publisher Link]
[6] Jin Xiao et al., “Optimising Allocation of Marketing Resources Among Offline Channel Retailers: A Bi-Clustering-based Model,” Journal
of Business Research, vol. 186, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[7] Tereza Sedlářová Nehézová et al., “A Robust Optimization Approach to Budget Optimization in Online Marketing Campaigns,” Central
European Journal of Operations Research, vol. 34, no. 2, pp. 495-526, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[8] Michel Wedel, and P.K. Kannan, “Marketing Analytics for Data -Rich Environments,” Journal of Marketing, vol. 80, no. 6, pp. 97 -121,
2016. [CrossRef] [Google Scholar] [Publisher Link]
[9] Vincent Charles, Ali Emrouznejad, and Werner H. Kunz, “Advancements in Artificial Intelligence -based Prescriptive and Cognitive
Analytics for Business Performance: A Special Issue Editorial,” Journal of Business Research , vol. 200, 2025. [CrossRef] [ Google
Scholar] [Publisher Link]
[10] Ryan Dew, Nicolas Padilla, and Anya Shchetkina, “Your MMM is Broken: Identification of Nonlinear and Time -varying Effects in
Marketing Mix Models,” arXiv preprint, pp. 1-39, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[11] Dimitris Bertsimas, and Nathan Kallus, “From Predictive to Prescriptive Analytics,” Management Science, vol. 66, no. 3, pp. 1025-1044,
2020. [CrossRef] [Google Scholar] [Publisher Link]
[12] Alexander Shapiro, Darinka Dentcheva, and Andrzej Ruszczyński, Lectures on Stochastic Programming: Modeling and Theory,” 2nd ed.,
Society for Industrial and Applied Mathematics, 2021. [CrossRef] [Google Scholar] [Publisher Link]
[13] Amir Albadvi, and Hamidreza Koosha, “A Robust Optimization Approach to Allocation of Marketing Budgets,” Management Decision,
vol. 49, no. 4, pp. 601-621, 2011. [CrossRef] [Google Scholar] [Publisher Link]
[14] Javier Marin, “A New Framework for Marketing Mix Modeling: Addressing Channel Influence Bias and Cross -Channel Effects,” arXiv
preprint, pp. 1-27, 2023. [CrossRef] [Google Scholar] [Publisher Link]
[15] Alexander Shapiro, Monte Carlo Sampling Methods, Handbooks in Operations Research and Management Science, vol. 10, pp. 353-425,
2003. [CrossRef] [Google Scholar] [Publisher Link]
[16] John R. Birge, and Francois Louveaux, Basic Properties and Theory, Introduction to Stochastic Programming, Springer, New York, NY,
pp. 103-161, 2011. [CrossRef] [Google Scholar] [Publisher Link]
[17] Stephen Boyd, and Lieven Vandenberghe, Convex Optimization , Cambridge University Press, 2004. [CrossRef] [ Google Scholar ]
[Publisher Link]
[18] Trevor Hastie, Robert Tibshirani, and Jerome Friedman, The Elements of Statistical Learning, Data Mining, Inference, and Prediction, 2nd
ed., Springer New York, NY, 2009. [CrossRef] [Google Scholar] [Publisher Link]

Hassan Ali Al-Ababneh et al. / IJETT, 74(7), 263-280, 2026

280
[19] Jerome H. Friedman, “Greedy Function Approximation: A Gradient Boosting Machine,” Annals of Statistics , vol. 29, no. 5, pp. 1189 -
1232, 2001. [Google Scholar] [Publisher Link]
[20] Anton J. Kleywegt, Alexander Shapiro, and Tito Homem-de-Mello, “The Sample Average Approximation Method for Stochastic Discrete
Optimization,” SIAM Journal on Optimization, vol. 12, no. 2, pp. 479-502, 2002. [CrossRef] [Google Scholar] [Publisher Link]
[21] Qiyang Yu, “Multi Modal Hierarchical Reinforcement Learning Framework for Dynamic Sports Sponsorship Optimization,” Scientific
Reports, vol. 15, no. 1, 2025. [CrossRef] [Google Scholar] [Publisher Link]
[22] R. Tyrrell Rockafellar, and Stanislav Uryasev, “Optimization of Conditional Value -at-Risk,” Journal of Risk , vol. 2, no. 3, pp. 21 -42,
2000. [CrossRef] [Google Scholar] [Publisher Link]
[23] Shuli Zhang et al., “Bi -Level Decision-Focused Causal Learning for Large -Scale Marketing Optimization: Bridging Observational and
Experimental Data,” Advances in Neural Information Processing Systems (NeurIPS), vol. 38, 2025. [Google Scholar] [Publisher Link]
[24] John M. Mulvey, Robert J. Vanderbei, and Stavros A. Zenios, “Robust Optimization of Large-Scale Systems,” Operations Research, vol.
43, no. 2, pp. 199-374, 1995. [CrossRef] [Google Scholar] [Publisher Link]
[25] Hsin-Chan Huang, Jiefeng Xu, and Alvin Lim, “Marketing Mix Optimization Under Practical Constraints,” International Journal of
Operational Research, vol. 51, no. 1, pp. 128-149, 2024. [CrossRef] [Google Scholar] [Publisher Link]
[26] Carlo Acerbi, and Dirk Tasche, “On the Coherence of Expected Shortfall,” Journal of Banking and Finance , vol. 26, no. 7, pp. 1487 -
1503, 2002. [CrossRef] [Google Scholar] [Publisher Link]
[27] Dimitris Bertsimas, and Melvyn Sim, “The Price of Robustness,” Operations Research, vol. 52, no. 1, pp. 1-164, 2004. [CrossRef] [Google
Scholar] [Publisher Link]
[28] R.Tyrrell Rockafellar, and Stanislav Uryasev, “Conditional Value -at-Risk for General Loss Distributions,” Journal of Banking and
Finance, vol. 26, no. 7, pp. 1443-1471, 2002. [CrossRef] [Google Scholar] [Publisher Link]
[29] Chang Gong et al., “CausalMMM: Learning Causal Structure for Marketing Mix Modeling,” Proceedings of the 17th ACM International
Conference on Web Search and Data Mining, Association for Computing Machinery, New York, NY, United States, pp. 238-246, 2024.
[CrossRef] [Google Scholar] [Publisher Link]
[30] Adam N. Elmachtoub, and Paul Grigas, “Smart “Predict, Then Optimize”,” Management Science , vol. 68, no. 1, pp. 1 -808, 2022.
[CrossRef] [Google Scholar] [Publisher Link]
