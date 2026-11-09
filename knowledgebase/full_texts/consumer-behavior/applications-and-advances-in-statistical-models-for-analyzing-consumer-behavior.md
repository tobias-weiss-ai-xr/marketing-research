---
title: Applications and Advances in Statistical Models for Analyzing Consumer Behavior and the Savings
  Rate
url: https://doi.org/10.56028/aemr.17.1.184.2026
category: consumer-behavior
subcategory: review
date: 2026-07
venue: Advances in Economics and Management Research
authors:
- Qianyi Huang
source: openalex-oa
pdf_url: https://madison-proceedings.com/index.php/aemr/article/download/5198/5200
pages: 10
chars: 29463
fetched_at: '2026-11-08T18:22:07+00:00'
kb_version: 1
---

# Applications and Advances in Statistical Models for Analyzing Consumer Behavior and the Savings Rate

184
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
Applications and Advances in Statistical Models for Analyzing
Consumer Behavior and the Savings Rate
QianYi Huang
The Affiliated International School of Shenzhen University, Shenzhen, 518054, China

Abstract. This paper provides a review of the application and evolution of statistical models in
analyzing the relationship between consumer behavior and savings rates, and offers two interrelated
yet distinct topics. It adopts a dual analytical work: at the micro level, the linear and the non-linear
(log-linear, exponential, and logistic) demand curve models are employed to capture the response
mechanisms of consumption behavior of consumers; at the macro level, the Autoregressive
Integrated Moving Average (ARIMA) model is introduced to analyse the temporal dynamics and
forecasting capability of consumer saving rates. Although the linear demand model provides a
fundamental explanation for analyzing consumer consumption behaviors, it fails to capture the
flexible behavior of consumers in empirical studies. This limitation has encouraged the use of the
non-linear demand curve model to effectively reflect more complex consumer behavior by
incorporating factors such as sensitivity and saturation. On the other hand, the ARIMA model is
advantageous in forecasting and trend decomposition of savings rates. By integrating the strengths
and limitations of both model families, this study reveals the complementarity between micro-level
behavioral mechanisms and macro-level dynamic patterns, offering a more comprehensive
perspective for understanding consumer behavior and saving rates. This paper also concludes some
limitations of the models reviewed.
Keywords: Consumer behavior; Savings rate; The Linear Demand Curve model; The Non-linear
Demand Curve models; The Autoregressive Integrated Moving Average Model.
1. Introduction
Consumer behavior and savings rate are two fundamental parts of macroeconomic analysis.
Consumer behavior analysis focuses on the microeconomic level, understanding how the
consumption of consumers changes under price and income constraints. On the other hand, the
savings rate acts as a macroeconomic variable, which reflects the results of consumption and how
they are influenced by capital accumulation and economic growth. Statistical models play an
important role in both micro and macro economics, with the demand curve model capturing the
response mechanism of consumers, and the ARIMA models analysing the dynamics and trends of the
savings rate.
In the analysis of consumption behavior of consumers, the linear demand curve model offers the
basic framework (Mankiw, 1998; Samuelson & Nordhaus, 2009). To estimate more complex
behaviors, researchers developed the non-linear demand curve model, including the log-linear model
(Arrow et al., 1961), the exponential model(Hursh & Silberberg, 2008), and the logistic
model(Mansfield, 1961). These non-linear demand curve models can effectively reflect the
heterogeneity and complex patterns of consumption behavior of consumers (Browning & Lusardi,
1996; Deaton & Muellbauer, 1980). In the research on the savings rate of consumers, the ARIMA
models are widely used in the analysis and forecasting of the savings rate under different periods and
conditions. The model captures the persistence and dynamic feature of saving rates but is more
suitable for short-term forecasting than casual analysis (Deaton, 1992; Hamilton, 1994).
This paper reviews the usage of these models and examines their structure, parameter
interpretations, advantages, and limitations, providing a reference for model selection in related fields.

185
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
2. Method
By integrating these models, the study can establish a link between the microfoundations of
behaviors and macroeconomic outcomes, thus offering a more comprehensive way for understanding
patterns, which effectively boosts policy making and saving rates forecasting.
2.1 Linear Demand Curve Model
In this study, the linear demand curve model is the basic way to analyse the behavior of consumers.
This model provides a straightforward way to explore how consumers make decisions to maximize
their utilities under deterministic conditions and within a given budget constraint. The most
fundamental and simplified form of a linear demand function of a certain good or service is:
𝑄ௗ = 𝛼 − 𝛽𝑃 ( 1)
The parameter in this function represents different economic meanings. 𝑄ௗ  represents the
quantity demanded by consumers of certain products, which is the most observable outcome of
consumer behaviour; P represents the price of the good or service; α ( α > 0) is the intercept
parameter, which indicates the quantity demanded by consumers when the price is zero. It can also
represent the effect on quantity demanded by factors other than price, such as preferences of
consumers and income; β ( β> 0) presents the extent of impact of price on quantity demanded.
According to the law of demand, β > 0 indicates that the quantity demanded of a good falls when
the price of the good rises (Mankiw, 1998). (The theoretical possibility of a positively sloped demand
curve (β <  0) for certain Giffen or Veblen goods is acknowledged but is not relevant to the context
of this study.) The Linear Demand Curve model is shown in Figure 1.

Figure 1 Linear Demand Curve Model.
The linear demand model is simple, transparent, and clear, thus making it serve as a foundation
for analysis. The main advantage of the model is its feasibility: Since the slope parameter β directly
measures the sensitivity, the model offers an intuitive static analysis. Therefore, a few data points are
required for estimation, and the solution can be invaluable for illustrating core economic principles
such as the law of demand and market equilibrium(Varian, Hal R. 2014). However, its simplicity and
the assumption of a constant slope constitute its primary limitation, which motivates further
introduction of more complex models discussed subsequently.
2.2 Non-linear Demand Curve Model
Among the various non-linear functions, there are three models for the illustration of demand
patterns: the Log-linear Model, the Exponential Model, and the Logistic Model. The variables 𝑃and

186
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
𝑄 carry the same economic interpretation in the non-linear demand models as in the linear demand
model. 𝑄 represents the quantity demanded; 𝑃 indicates the price of a product.
2.2.1 The Log-linear Demand Curve Model
For this analysis, we first use the log-linear demand model, which has the function in the form:
𝑄ௗ = 𝛼 ⋅ln(𝑃) + 𝛽 ( 2)
Here, the parameters α and β have separate meanings compared to the linear demand curve model.
In this model, α (𝛼 < 0) is the coefficient of ln(𝑃), which interprets the absolute change in quantity
demanded when the price changes by a unit proportion. We expected that 𝛼 < 0, as the quantity
demanded reduces when price increases, resulting from the law of demand; β is the intercept, which
indicates the base demand quantity when ln(𝑃) = 0. The Log-linear Demand curve Model is shown
in Figure 2.

Figure 2 The Log-linear Demand Curve Model.
2.2.2 The Exponential Demand Curve Model
The Exponential Demand Curve Model has the function in the form:
𝑄 = 𝛼 ⋅ 𝑒ఉ௉ (3)
For this model, the quantity demanded reduces exponentially as the price increases. α (α > 0) is a
scale parameter, which indicates the theoretical quantity demanded when price is zero; β is the
curvature parameter, which determines the direction and the rate of change in quantity demanded
when responding to changes in price. When β < 0, quantity demanded decreases exponentially as
price increases, while quantity demanded grows exponentially with the price when β > 0. The
Exponential Demand Curve Model is shown in Figure 3.

187
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)

Figure 3 The Exponential Demand Curve Model.
2.2.3 The Logistic Demand Curve Model
The Logistic Demand Curve Model has the function in the form:
𝑄ௗ = 𝐿 1 + 𝑒ି௞(௉ି௉0) (4)
In this model,  L(L > 0) is the potential of the market or the level of saturation, which represents
the maximum possible quantity demanded; 𝑃0(𝑃0> 0) is the inflection point parameter, which refers
to the opportunity cost at the critical point of the model. At 𝑃0, the quantity demanded, is half of the
saturation level of consumption, which is
௅
2. At this point, the sensitivity of consumers to the change
in price is the greatest;  k(k > 0) is the steepness parameter, which determines the rate at which the
quantity demanded adjusts to changes in price. An increasing k indicates that as the price rises, the
quantity demanded, changes from high to low at a higher rate. The Logistic Demand Curve Model is
shown in Figure 4.

Figure 4 The Logistic Demand Curve Model.

188
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
2.3 Autoregressive Integrated Moving Average Models
The Autoregressive Integrated Moving Average (ARIMA) models were developed by Box and
Jenkins (1976). It expresses current saving rates as a linear combination of past values and random
errors (Ghazo, Abdullah, 2021).
2.3.1 The Autoregressive Model
The Autoregressive Model is used to capture the persistence in the saving behavior of consumers,
which reflects how past saving rates influence current decisions through habit formation or
adjustment. This model has the form:
𝑋௧ = 𝜑1𝑋௧ି1 + 𝜑2𝑋௧ି2 + ⋯ +𝜑௣𝑋௧ି௣ + ∁ + ℇ௧ (5)
In the model, 𝑋௧ is the saving rates at time t; p is the lag order; 𝜑1 ,...,𝜑௣  represent the
Autoregressive coefficients, which indicate the extent of effect of each past data on current data.
When 𝜑௣ > 0, this indicates a stronger persistence in saving behavior, while there is a reversal in
saving behaviors when 𝜑௣ < 0; ∁ represents the constant term; ℇ௧ represents the random errors
(Voloshyn, Ihor.,2014).
2.3.2 The Moving Average Model
The Moving Average Model is defined in the form:
𝑋௧ = 𝜃1𝜀௧ି1 + 𝜃2𝜀௧ି2 + ⋯ +𝜃௤𝜀௧ି௤ + ∁ +𝜀௧ (6)
In the Moving Average Model,  𝑋௧ is the saving rates at time t, which represents when the mean
∁ plus the current random error 𝜀௧  and the weighted sum of the q previous errors ；𝜃1 ,...,𝜃௤
represents the moving average coefficients, which indicates the extend of effect of q previous data on
current values; ∁ is a constant; q is the order of the moving average; 𝜀௧ is the random error.
2.3.3 The Autoregressive Moving Average (ARMA) Model
By combining the Autoregressive model and the Moving Average model, we obtain the
Autoregressive Moving Average (ARMA) model. The model has the formula:
𝑋௧ = 𝜑1𝑋௧ି1 + 𝜑2𝑋௧ି2 + ⋯ +𝜑௧𝑋௧ି௣ + ∁
+𝜀௧ + 𝜃1𝜀௧ି1 + 𝜃2𝜀௧ି2 + ⋯ +𝜃௤𝜀௧ି௤ (7)
All parameters follow the same definitions as in equations (5) and (6).
This model combines the traits of both AR and MA models, capturing long-term dynamics through
the autoregressive component and short-term dynamics through the moving average component (Box,
Jenkins, & Reinsel, 2015). However, the ARMA model requires a stable time series, whereas
macroeconomic variables like saving rates often contain trends, leading to non-stationarity (Nelson
& Plosser, 1982).
2.3.4 The Integrated Method
By differencing, a non-stationary series is transformed into a stationary one, eliminating trends
and period-to-period changes. First-order differencing is defined as:
𝑌௧ = 𝛻𝑋௧ = 𝑋௧ − 𝑋௧ି1 (8)
For the Second-order differencing (if the series is still non-stationary after the first differencing):
Yt = 𝛻2𝑋௧ = 𝛻(𝛻𝑋௧) = (𝑋௧ − 𝑋௧ି1) − (𝑋௧ି1 − 𝑋௧ି2) ( 9)
Yt is the differenced series at time t; 𝛻 is the difference operator; 𝑋௧ is the saving rates at time t.
2.3.5 The Autoregressive Integrated Moving Average Model (ARIMA)
The ARIMA (p, d, q) model integrates differencing into the ARMA model to achieve stationarity
(Box & Jenkins, 1976). This method first transforms the original series through dth-order differencing
to obtain a stationary series of saving rates, then applies the ARMA model to the differenced data. In
this study, we first use the Augmented Dickey-Fuller (ADF) test to test the stationarity of the saving
rates series (Dickey & Fuller, 1979). If the series is non-stationary, we apply differencing of order d.
We then select the orders of p and q using the Akaike Information Criterion (AIC) and Bayesian
Information Criterion (BIC) (Box, Jenkins, & Reinsel, 2015), and estimate the ARMA model. This

189
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
process yields a stationary series suitable for modeling and enables short-term forecasting of savings
rate dynamics.
In summary, at the micro level, the paper uses a linear demand curve model for fundamental
analysis of consumer behavior and introduces three nonlinear demand curve models to capture more
dynamic changes in consumption. At the macro level, the paper applies ARIMA models to analyze
the dynamics of consumer savings rates.
3. Results
This section summarizes the application of both linear and non-linear demand curve models to
consumer behaviors and ARIMA models to the saving rates of consumers.
3.1 Application of Linear Demand Curve Model to Consumer Behaviors
The results of studying consumer behavior by using the Linear Demand Curve Model are
consistent with the law of demand. The linear model usually has a negative coefficient for most goods,
which indicates that the quantity demanded reduces when the price increases (Deaton & Muellbauer,
1980; Mankiw, 1998). However, when comparing the linear demand curve model to alternative
models, scholars found that the linear model can provide only an approximate description of
consumer behaviors. The report shows that the results at the extremes of prices and quantity
demanded from the linear model are sometimes inappropriate, such as negative predictions. Also,
linear models generally display larger residual variance and weaker fit, especially when some goods
or services have strong saturation or effects (Deaton & Muellbauer, 1980).
3.2 Application of Non-Linear Demand Curve Model to Consumer Behaviors
3.2.1 The Log-linear Demand Curve Model
For many goods or services categories, researchers like to apply the log-linear or log-log demand
curve to model the relationship between price and quantity demanded. Reports show that the demand
systems based on logarithmic transformations usually produce approximately constant price
elasticities over the price intervals. Compared with the linear model, the Log-linear demand curve
model can represent percentage changes rather than absolute changes (Deaton & Muellbauer, 1980).
The Log-linear model also avoids negative results or predictions, which makes it suitable for
capturing the percentage responses to policies, such as excise tax on unhealthy food and energy
products (Andreyeva et al., 2010).
3.2.2 The Exponential Demand Curve Model
The Exponential Demand Curve Model is mainly used under the circumstances that consumption
decreases rapidly when price or other cost factors increase. Scholars propose an exponential demand
function when studying behavioral economics and experimental studies of addictive consumption,
which indicates that the Exponential model is suitable not only for the insensitive demand at low
prices, but also the steep decline in consumption at a higher price (Hursh & Silberberg, 2008).
Compared with the linear model and the log-linear model, the exponential model can provide fewer
prediction errors and better reproduce the observed curvature of demand (Hursh & Silberberg,
2008).
3.2.3 The Logistic Demand Curve Model
The Logistic Demand Curve Model is primarily used to describe the diffusion of new technologies
and products among consumers. The Logistic model is suitable for the cumulative proportion of
adopters over time, which indicates a slow adoption in the beginning, accelerating in the middle stage,
and becoming saturated at the final stage, resulting from the study of industrial innovation (Mansfield,
E., 1961).
For example, early consumers are insensitive to price change, as they focus more on the product
itself, while late consumers are more easily affected by market penetration of the product or the

190
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
comment on the product  (Mansfield, 1961; Bass, 1969). As a result, the Logistic Demand Curve
Model is usually used to forecast the peak of the sales and the time when the sales reach the maximum
according to the results in early data.
In conclusion, the linear and the log-linear demand curve models are primarily used for general
consumer demand estimation and policy analysis, while the exponential and the logistic models are
applied under circumstances where strong non-linearities, saturation, or adoption dynamics are main
characteristics of consumer behaviour.
3.3 Application of the ARIMA Models to the saving rates of consumers
3.3.1 The AR and the MA components
When applying the Autoregressive model in studying saving rates of consumers and aggregate
consumption, scholars found that the model has high persistence in the series. This model provides
information about how past saving or consumption influences the current behavior of consumers
(Deaton, A., 1992). Some studies indicate that lagged consumption and lagged income can influence
the prediction of current consumption, which indicates that saving rates exhibit a serial correlation,
resulting from the fact that saving equals income subtracted by consumption (Campbell, J. Y., &
Mankiw, N. G., 1989).
Many scholars found that it is advantageous to introduce the MA model in time series studies, as
the model captures the short-term impact of temporal shocks to saving rates, including policy changes
or income changes (Box & Jenkins, 1976; Hamilton, 1994). The pure MA model is less commonly
used in studying saving rates, as the model is mainly used in the modelling of short-term shocks. As
a result, the MA model is frequently combined with the AR model to form ARMA or ARIMA models
to show the persistence and impact of shocks to the saving rates of consumers (Box & Jenkins, 1976;
Box et al., 2015).
In sum, when having stationary data of saving rates or related variables, it is appropriate to use
ARMA models, resulting from the fact that low orders of p and q are enough to capture the dynamic
structure (Deaton, 1992; Hamilton, 1994).
3.3.2 The Integrated component and the ARIMA models
By introducing the Integrated (I) component to ARMA models, series are differenced until they
are stationary, and then the model is used to model the dynamics of the series. Through the first
differences, the unit roots are removed, thus leading to ARIMA ( p, 1, q) models, which have smaller
values of p and q (Deaton, 1992; Hamilton, 1994).
ARIMA models capture key dynamic characteristics such as persistence and gradual decay of
shocks, and are well-suited for short-term forecasting (Box & Jenkins, 1976; Hamilton, 1994;
Hyndman & Athanasopoulos, 2018).
4. Discussion
4.1 Demand models
4.1.1 Examples of differences in results with the same models and study object
Empirical studies on the consumption of consumers show that different results can be obtained
even when using the same model and comparable data. For example, when Andreyev, Long, and
Brownell (2010) review the study of the elasticities of 160 types of foods among 23 works, where
most of the works use log-log models or similar models, they found that the price elasticity of demand
varies among different countries and periods, even when using similar models.
Some studies present that different implementations of the demand system will result in different
estimates of price or different interpretations of elasticities. In their comparison, the log-linear
demand curve model often provides more stationary results in elasticities than simple models like the
linear demand curve model (Deaton & Muellbauer, 1980).

191
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
4.1.2 Reasons for the difference in results
Many papers provide explanations from different angles of differences in results, even though the
linear and non-linear models have similar specifications.
Firstly, there are differences in preferences and constraints between different groups of people,
due to different backgrounds, income, and culture. Under the circumstances of having differences in
preference, consuming behaviors, and access to credit, it is understandable to have different
elasticities even using the same model to estimate. Demand curve models also assume homogeneous
preferences, using a representative consumer, which may be misleading given real-world
heterogeneity (Deaton & Muellbauer, 1980; Browning & Lusardi, 1996).
4.2 ARIMA models
4.2.1 Examples of using similar ARIMA-type methods with different conclusions
There are relatively limited direct studies that model saving rates with ARIMA models, but work
on consumption and income can illustrate how similar time-series methods can lead to different
results in estimation, prediction, and dynamics.
First, when Hall (1978) is analysing the aggregate expenditure of America, he proposes that
consumption is close to an approximate random movement, which means past data does not influence
future consumption. In this way, this is similar to the ARIMA (0,1,0) models (Hall, R. E., 1978).
However, future studies cast doubt on this research study of Hall (1978). In 1989, Campbell and
Mankiw found that lagged income has an impact on future consumption by comparing data from
different countries, which undermines the statement about the random movement of consumption.
Also, by implementing the Autoregressive model, we can discover that there exists an apparent
correlation between consumption and income, thereby indicating the ARIMA (0,1,0) model is not the
only way to describe saving rates of different countries.
In sum, although the studies are not directly related to saving rates themselves, it is clear that they
lead to different results about stationarity and persistence by using similar ARIMA time-series models.
This is basically due to different reasons, including the way scholars deal with data and samples.
4.2.2 Reasons for the difference in results
There are several reasons to explain the difference in the results of using ARIMA models. Firstly,
studies have different time spans. Therefore, some studies included financial events while others did
not. Financial events can lead to changes in the parameters of models, thus leading to different
forecasts and estimations (Nelson & Plosser, 1982; Hamilton, 1994). Also, there is a transformation
between variables, due to the fact that some papers mainly study income and consumption, while
other papers focus on saving rates, thereby affecting the stationary properties and differencing orders
(Deaton, 1992).
5. Limitation
5.1 Limitations of Demand Curve Models
First, demand curve models have a static and single focus on products. There are only equations,
thus making the focus only on the relationship between price and quantity demanded at a point in
time. They do not consider the effect of the habit of consumers and cross-price effects between goods
(Deaton & Muellbauer, 1980; Deaton, 1992).  Also, there are dynamics and expectations in
consumption, while the static demand curve models cannot capture the dynamic adjustments
(Friedman, 1957; Deaton, 1992). Therefore, studies have expanded the static demand functions into
dynamic error-correlation or habit-formation specifications, which consider consumer behaviors
based on both current price and past consumption habits (Deaton, 1992).

192
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
5.2 Limitation of the ARIMA models
ARIMA models are sometimes weak due to their lack of structural interpretation, as the model is
a simple form of time-series models, which only summarize the autocorrelation structure of saving
rates but do not describe the life-cycle of motivation, policy incentives, and precautionary saving of
consumers (Deaton, 1992; Hamilton, 1994). As a result, the ARIMA models are more suitable for
forecasting than for causal analysis. Also, the ARIMA models are suitable for short-run analysis from
the results above, thus indicating the limited long-run forecasting ability of the ARIMA models. The
accuracy of the ARIMA models declines over a long time range (Hamilton, 1994; Hyndman &
Athanasopoulos, 2018).
There are some suggestions to mitigate some limitations. The first way is to include exogenous
variables, such as interest rate, income, and demographic indicators, in the ARIMA models. In this
way, the model can capture more complex dynamics of the environment and saving rates, which
improves the ability of interpretation and forecasting of the model (Box et al., 2015; Hyndman &
Athanasopoulos, 2018).
6. Conclusion
In conclusion, this paper reviews two types of statistical models: the Demand Curve Models for
consumer behavior analysis, and the Autoregressive Integrated Moving Average models for
estimating the savings rate.
In the analysis of consumer behaviors, the linear demand curve model provides a basic framework.
In this way, the non-linear demand curve model addresses this issue, with the log-linear model to
reflect proportional responses, the exponential model to capture the changes in demand under extreme
conditions, and the logistic model to describe the saturation level of the market.
In savings rate research, the ARIMA model analyzes the dynamics of savings rates in the short
run, which indicates its ability in short-term forecasting and trend estimation. However, its
atheoretical nature makes it more suitable for forecasting rather than causal analysis.
Both models have their limitations. The demand curve models focus on static changes in consumer
behavior and sometimes ignore the heterogeneity and complex patterns of consumption behavior of
consumers. On the other hand, the ARIMA models are sensitive to structural changes and cannot
accurately forecast savings rate changes in the long run.
In the future, research can incorporate exogenous variables to boost the power of ARIMA, or
combine micro-level behavioral parameters with macro-level time series models to develop more
comprehensive analytical frameworks.
References
[1] Andreyeva, T., Long, M. W., & Brownell, K. D. (2010). The impact of food prices on consumption: a
systematic review of research on the price elasticity of demand for food. American journal of public
health, 100(2), 216-222.
[2] Arrow, Kenneth J., et al. "Capital-labor substitution and economic efficiency." The review of Economics
and Statistics (1961): 225-250.
[3] [3]Bass, Frank M. "A new product growth for model consumer durables." Management science 15.5
(1969): 215-227.
[4] Boskin, Michael J. "Taxation, saving, and the rate of interest." Journal of political Economy 86.2, Part 2
(1978): S3-S27.
[5] Box, George EP, et al. Time series analysis: forecasting and control. John Wiley & Sons, 2015.
[6] Browning, M., & Lusardi, A. (1996). Household saving: Micro theories and micro facts. Journal of
Economic literature, 34(4), 1797-1855.
[7] Campbell, John Y., and N. Gregory Mankiw. "Consumption, income, and interest rates: Reinterpreting
the time series evidence." NBER macroeconomics annual 4 (1989): 185-216.

193
Advances in Economics and Management Research IACBES 2026
ISSN:2790-1661 Volume-17-(2026)
[8] Deaton, Angus. Understanding consumption. Oxford University Press, 1992.
[9] Deaton, Angus, and John Muellbauer. Economics and consumer behavior. Cambridge university press,
1980.
[10] Dickey, David A., and Wayne A. Fuller. "Distribution of the estimators for autoregressive time series
with a unit root." Journal of the American statistical association 74.366a (1979): 427-431.
[11] Friedman, Milton. "Theory of the consumption function." (2018): 1-296.
[12] Ghazo, Abdullah. "Applying the ARIMA Model to the Process of Forecasting GDP and CPI in the
Jordanian Economy." International Journal of Financial Research 12.3 (2021): 70.
[13] Hall, Robert E. "Stochastic implications of the life cycle-permanent income hypothesis: theory and
evidence." Journal of political economy 86.6 (1978): 971-987.
[14] Hamilton, James D. Time series analysis. Princeton university press, 2020.
[15] Hursh, Steven R., and Alan Silberberg. "Economic demand and essential value." Psychological
review 115.1 (2008): 186.
[16] Hyndman, Rob J., and George Athanasopoulos. Forecasting: principles and practice. OTexts, 2018.
[17] Mankiw, N. Gregory. "Teaching the principles of economics." Eastern Economic Journal 24.4 (1998):
519-524.
[18] Mankiw, N. Gregory. Principles of microeconomics. Vol. 1. Elsevier, 1998.
[19] Nelson, Charles R., and Charles R. Plosser. "Trends and random walks in macroeconmic time series:
some evidence and implications." Journal of monetary economics 10.2 (1982): 139-162.
[20] Samuelson, Paul, and William Nordhaus. EBook: Economics. McGraw Hill, 2009.
[21] Varian, Hal R. Intermediate microeconomics with calculus: a modern approach. WW norton & company,
2014.
[22] Voloshyn, Ihor. "Munich Personal RePEc Archive." (2014).
