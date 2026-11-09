---
title: Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity
  Markets
url: https://arxiv.org/abs/2605.17307
category: ai-marketing
subcategory: empirical
date: 2026-05
venue: ''
authors:
- Kamil Kashif
- Robert Ślepaczuk
source: arxiv
pdf_url: https://arxiv.org/pdf/2605.17307
pages: 67
chars: 151614
fetched_at: '2026-11-08T13:06:05+00:00'
kb_version: 1
---

# Deep Reinforcement Learning Framework for Diversified Portfolio Management Across Global Equity Markets

Deep Reinforcement Learning Framework for Diversified Portfolio
Management Across Global Equity Markets
, Kamil Kashifa,1, Robert Ślepaczukb,2,∗
aQuantitative Finance Research Group Faculty of Economic Sciences University of Warsaw ul. Dluga 44-50 00-241
Warsaw Poland
bQuantitative Finance Research Group Department of Quantitative Finance and Machine Learning Faculty of
Economic Sciences University of Warsaw ul. Dluga 44-50 00-241 Warsaw Poland
Abstract
This study develops and evaluates a deep reinforcement learning framework for dynamic portfolio
allocation across global equity markets. The Soft Actor–Critic algorithm is used to learn continuous
portfolio weights within a Markov Decision Process, incorporating transaction costs, turnover
penalties, and diversification constraints into the reward function. Five model configurations
are compared, varying in reward formulation, policy structure (flat versus hierarchical Dirichlet),
portfolio constraints, and temporal encoder (LSTM versus Transformer), and evaluated via walk-
forward optimization across sixteen out-of-sample folds spanning 2003–2026 on the Nasdaq-100,
Nikkei 225, and Euro Stoxx 50. Results show that RL strategies achieve competitive risk-adjusted
performance primarily in the Euro Stoxx 50, where statistically significant abnormal returns are
observed, but the central hypothesis is only partially confirmed: no strategy achieves statistically
significant excess returns relative to Buy & Hold under HAC-robust inference across all markets.
Regime analysis reveals that RL adds the most value during periods of elevated uncertainty, while
ensemble aggregation across markets improves risk-adjusted performance and confirms the benefits
of geographic diversification.
Keywords:Reinforcement Learning (RL), Deep Reinforcement Learning, Hierarchical
Reinforcement Learning (HRL), Soft Actor-Critic (SAC), Portfolio Allocation, Algorithmic Trading,
Market Timing, Walk-Forward Optimization (WFO), Rolling Retraining, Nasdaq-100, Nikkei 225,
Euro Stoxx 50, Hierarchical Policy, Dirichlet Distribution, Markov Decision Process
JEL: C4, C14, C45, C53, C58, G13
1. Introduction
Predicting and navigating financial markets remains a challenging task due to their inherent
volatility, complex structure, and constantly evolving economic environment. Over the past decades,
major events such as the 2008 global financial crisis and the COVID-19 pandemic have demonstrated
∗Corresponding author
Email address:rslepaczuk@wne.uw.edu.pl(Robert Ślepaczuk)
1ORCID: https://orcid.org/0009-0004-0666-581X
2ORCID: https://orcid.org/0000-0001-5227-2014
Preprint submitted to ... May 19, 2026
arXiv:2605.17307v1  [q-fin.PM]  17 May 2026

how rapidly market conditions can change, making it difficult for traditional models to generalize
across different regimes. As a result, researchers and practitioners have explored a wide range of
approaches, from classical statistical models to advanced machine learning techniques, in an attempt
to develop robust and profitable investment strategies. In recent years, reinforcement learning (RL)
has emerged as a promising framework for financial decision-making. Unlike traditional supervised
learning approaches that focus on predicting future prices or returns, RL directly models the portfolio
allocation problem as a sequential decision-making task. This allows the agent to learn trading
strategies by interacting with the market environment and optimizing a long-term objective.
The main objective of this study is to develop and evaluate reinforcement learning-based portfolio
allocation strategies under realistic market conditions. We formulate the portfolio allocation
problem as a Markov Decision Process and employ the Soft Actor–Critic (SAC) algorithm to learn
dynamic asset allocation policies. The framework incorporates transaction costs, turnover penalties,
and diversification constraints directly into the learning objective. In addition, a walk-forward
optimization (WFO) scheme with adaptive retraining is used to simulate a realistic deployment
setting.
A central aspect of this research is the systematic comparison of different design choices within
the RL framework. Specifically, we analyze how variations in reward formulation (absolute versus
benchmark-relative), policy structure (flat versus hierarchical allocation), portfolio constraints (fully
invested versus flexible exposure), and temporal encoding (LSTM versus Transformer) influence the
performance and robustness of the learned strategies.
The central hypothesis of this study is that reinforcement learning-based portfolio allocation
strategies can achieve robust and economically meaningful performance when trained under realistic
constraints and evaluation procedures, and that their effectiveness is strongly influenced by architec-
tural and economic design choices. Furthermore, it is hypothesised that the relative performance of
reinforcement learning strategies varies across macroeconomic regimes, with active allocation adding
greater value during periods of elevated uncertainty and lower trend persistence.
The following research questions are addressed:
•RQ1. How does the choice of reward formulation (absolute vs. benchmark-relative) affect the
performance and stability of learned strategies?
• RQ2. What is the impact of different policy structures (flat vs. hierarchical allocation) on
portfolio performance and diversification?
2

• RQ3. How do portfolio constraints (fully invested vs. flexible exposure) influence trading
behavior and risk-adjusted returns?
•RQ4. Does the inclusion of different temporal encoders (LSTM vs. Transformer) improve the
model’s ability to capture market dynamics and enhance performance?
• RQ5. Does combining strategy-specific signals across multiple markets through an ensemble
approach improve risk-adjusted performance compared to single-market strategies and the
benchmark?
• RQ6. Does the performance of reinforcement learning strategies vary systematically across
macroeconomic regimes, and in which market environments do RL strategies add the most
value relative to passive and classical benchmarks?
To evaluate the proposed reinforcement learning strategies, we consider a cross-sectional equity
universe based on three major stock indices: theNasdaq 100, theNikkei 225, and theEuro Stoxx
50, representing U.S., Asian, and European markets, respectively. This selection allows for a
comprehensive analysis across different economic regions and market conditions. The full sample
spans the period from2 January 2003to13 March 2026withdailyfrequency, covering multiple
market regimes, including periods of high volatility and structural change.
The empirical framework is evaluated using a walk-forward optimization (WFO) scheme, where
each iteration consists of a5-year trainingperiod, followed by1 year of validationand1 year of
testingset. This setup allows the model to adapt to evolving market conditions while ensuring a
robust and realistic evaluation of performance.
This study contributes to the existing literature in several ways. First, it provides a unified multi-
market evaluation framework applying identical walk-forward optimization and assessment procedures
across three economically distinct equity markets, enabling direct cross-market comparison absent
from prior single-market studies. Second, it introduces a hierarchical Dirichlet policy structure
that separates the equity-cash allocation from individual asset selection, extending flat policy
architectures used in related work. Third, it proposes an adaptive retraining criterion that selectively
updates the model based on rolling validation performance, reducing computational cost while
maintaining deployment realism. Fourth, it conducts a systematic regime decomposition across three
macroeconomic periods, providing evidence on the conditions under which reinforcement learning
allocation adds value relative to passive and classical benchmarks.
3

The remainder of this thesis is structured as follows. Section 2 reviews the relevant literature on
algorithmic trading, machine learning, and reinforcement learning in finance. Section 3 describes the
data sources and preprocessing steps. Section 4 presents the theoretical background underlying the
reinforcement learning framework. Section 5 outlines the methodology, including the state represen-
tation, action space, reward function, model architecture, and validation procedure. Section 6 reports
the empirical results of the proposed strategies. Section 7 presents the sub-period macroeconomic
regime analysis. Section 8 presents the ensemble total fund perspective. Section 9 discusses the
main findings and their implications. Finally, Section 10 concludes the thesis and outlines directions
for future research.
2. Literature Review
Historically, algorithmic trading has been known with rule-based execution, econometric modeling,
and supervised machine learning aimed at avoiding human biases in market entry and exit. However,
a significant paradigm shift is occurring as researchers move beyond static price forecasting. Recent
literature has begun to explore the robust capabilities of Reinforcement Learning (RL). Unlike
traditional statistical models that focus on time predictions, RL frameworks, specifically when
integrated with deep architectures, offer a comprehensive approach to sequential decision-making,
portfolio allocation, and risk optimization.
2.1. Portfolio Optimization
Let’s go back a couple of steps and recall ourselves how it started and was up until now.
The foundational framework for modern portfolio optimization started with the work of Markowitz
(1952), who introduced mean-variance optimization (MVO) where we balance expected returns
against risk via covariance matrices, enabling efficient frontiers for diversed allocations. While, this
is applicable in terms of mathematics, its applications in real-world showed instability. For example,
Black and Litterman (1992) in their paper critiqued that MVO often leads to highly concentrated
portfolios hypersensitive to estimation errors
Most recently, the literature has shifted toward integrating predictive modeling into the optimiza-
tion loop. Ślusarczyk and Ślepaczuk (2025) modernized MVO by forecasting returns using hybrid
time series and machine learning models such as ARIMA-GARCH and the XGBoost models. The
paper demonstrates that combining forecasting models with traditional optimization can improve
portfolio outcomes compared to purely historical approaches.
4

Chaweewanchon and Chaysiri (2022) propose a hybrid portfolio optimization framework that
integrates machine learning-based stock prediction with the classical mean-variance (MV) model.
Their approach employs a CNN-BiLSTM architecture with robust statistical preprocessing to improve
prediction accuracy of financial time-series data, followed by a stock preselection step based on
predicted returns. The selected assets are then used within the MV framework to construct optimal
portfolios. Empirical results on SET50 data demonstrate that incorporating predictive stock selection
significantly improves portfolio performance in terms of return, risk, and Sharpe ratio compared to
traditional and benchmark models.
López de Prado et al. (2025) investigate the incorporation of machine learning techniques into the
Markowitz portfolio selection framework, aiming to enhance key aspects of portfolio management such
as alpha generation, risk management, and the optimization of risk measures including conditional
value at risk. Their work highlights how machine learning enables more dynamic decision-making
by leveraging complex financial datasets, while also addressing the practical considerations and
challenges of applying these methods in real-world portfolio management.
A particularly relevant benchmark in the context of portfolio optimization is the equal-weight
(1/N) strategy, which allocates capital uniformly across all available assets without estimation
or optimization. DeMiguel et al. (2009) demonstrate that this naive diversification strategy is
remarkably difficult to outperform out-of-sample, consistently matching or exceeding the performance
of sophisticated mean-variance optimized portfolios across a wide range of datasets and evaluation
periods. Their findings highlight that estimation error in expected returns and covariances severely
limits the practical advantages of complex optimization models, establishing the equal-weight
portfolio as a natural and stringent benchmark for any active portfolio allocation strategy.
2.2. Machine and Deep Learning in Finance
The application of statistical learning to financial markets represents a shift from testing economic
hypotheses to maximizing predictive accuracy. While traditional econometrics assumes linear
relationships, financial time series are non-linear. To navigate this complexity, researchers have
increasingly turned to supervised learning frameworks.
Support Vector Machines (SVM) were among the first early-stage ML tools to gain prominence
for their ability to handle high-dimensional data by identifying optimal hyperplanes for classification.
Kim (2003) demonstrated that SVMs could outperform traditional Artificial Neural Networks (ANN)
in predicting the direction of the daily KOSPI index, largely due to their ability to minimize
structural risk rather than just empirical error. Similarly, Random Forests (RF) have been known
5

for their robustness against the outliers common in financial data. Khaidem et al. (2016) utilized
RF to capture complex market patterns, finding that the ensemble based approach of decision trees
effectively mitigates the risk faced with investing the stock market. Grudniewicz and Ślepaczuk
(2023) explored the application of ML in algorithmic trading across global stock markets, where
they concluded that Linear SVM outperforms Bayesian GLM and the benchmark.
However, still the challenge remains the noise within financial signals and the high probability of
backtest overfitting. Bailey et al. (2017) provided a rigorous mathematical framework to quantify
the probability of backtest overfitting using a model-free method by proposing a framework that
measure the probability of that an optimal strategy on the training set outpeforms the average on
the test. López de Prado (2018) also argues that most machine leanring funds often fail in finance,
proposing a among other a walk-forward backtesing and a deflated sharpe ratio to ensure that
reported performance is statistically legitimate.
While early machine learning handled cross-sectional data effectively, financial time series require
architectures capable of modeling high-dimensional features over time. The literature has evolved
from basic sequential models to sophisticated attention frameworks.
The integration of Recurrent Neural Networks (RNN) marked the first major attempt to give
financial models memory by allowing information to persist across time steps. Lin et al. (2021)
provided an early benchmark showing that RNNs could capture the noisy, non-stationary dynamics
of stock prices however data pre-processing is vital. They proposed a zero-crossing rate, which is a
ratio of changes in the sign noting that this approach outperforms the traditional appraoches for the
S&P 500 equity index. Bieganowski and Ślepaczuk (2025) utilized supervised autoencoders with
recurrent structures to enhance feature extraction, proving that even simpler recurrent architectures
can perform when combined with robust labeling techniques like the Triple Barrier Method.
In order to solve the vanishing gradient problem, the Long Short-Term Memory (LSTM) model
comes in which introduces a gating mechanism that decides which information to keep or discard.
Fischer and Krauss (2018) established the gold standard by proving LSTMs significantly outperform
traditional deep neural networks in predicting S&P 500 constituents, specifically by capturing
long range interactions between historical lags. Krynska and Ślepaczuk (2023) cconducted a
granular analysis of various LSTM architectures across daily and intraday both wiht regression and
classificaiton problem, concluding that the classificiton approach outperforms the benchmark. Kashif
and Ślepaczuk (2025) developed a hybrid LSTM-ARIMA model, illustrating that the outperformance
of an LSTM is maximized when it is paired with a classical econometric component to handle linear
6

residuals of ARIMA.
The current frontier in the literature is the Transformer architecture, which replaces recurrence
with Self-Attention, allowing the model to focus on the most important historical events regardless
of how far back they occurred. Kabir et al. (2025) argued that while LSTMs process data linearly,
Transformers’ parallelization and attention mechanisms combined allows them to significantly
outperform them individually. Stefaniuk and Ślepaczuk (2025) explored the application of the
Informer architecture specifically on high-frequency Bitcoin data, demonstrating that attention when
designed appropriately with the correct loss function can outperform the benchmark.
2.3. Reinforcement and Deep Reinforcement Learning in Finance
The integration of Reinforcement Learning (RL) into financial systems represents a transition
from static price forecasting to an active, agentic decision-making. Unlike supervised learning models
that minimize prediction error, RL frameworks optimize for an object which is typciall long-term
cumulative performance, or risk-adjusted returns.
This concept of modern financial reinforcement learning is surveyed by Hambly et al. (2023),
who contrast RL with classical stochastic control approaches that rely heavily on explicit model
assumptions. Instead, RL frameworks enable agents to learn optimal decision-making policies
directly through interaction with the environment, using observed state transitions and rewards. The
survey highlights that, particularly in model-free settings, RL can effectively handle complex and
high-dimensional financial problems without requiring a fully specified model of market dynamics.
Furthermore, RL naturally integrates prediction and decision-making, making it well suited for tasks
such as optimal execution, portfolio optimization, and smart order routing.
The Direct Reinforcement (DR) approach was introduced by Moody and Saffell (2001) as a
method for optimizing trading strategies by viewing investment decision-making as a stochastic
control problem. They propose the Recurrent Reinforcement Learning (RRL) algorithm, which
eliminates the need to construct forecasting models and instead directly learns investment policies.
Unlike traditional reinforcement learning methods such as Q-learning and TD-learning, which rely
on value function estimation, the DR approach simplifies the problem representation and avoids
Bellman’s curse of dimensionality. The method optimizes risk-adjusted returns using the differential
Sharpe ratio while accounting for transaction costs. Empirical results on financial data, including
applications to the S&P 500 and T-Bills, show that RRL-based strategies achieve better trading
performance than value-function-based approaches.
7

Deng et al. (2017) propose a recurrent deep neural network framework for real-time financial signal
representation and trading, combining deep learning and reinforcement learning components. In this
approach, the deep learning module captures dynamic market conditions and extracts informative
features, while the reinforcement learning component interacts with these representations to make
trading decisions in an unknown environment. The model is implemented as a deep and recurrent
neural network, and a task-aware backpropagation through time method is introduced to address
the vanishing gradient problem during training. The proposed system is evaluated on both stock
and commodity futures markets, where its robustness is demonstrated under a range of testing
conditions.
Buehler et al. (2019) propose a framework for hedging derivative portfolios using deep reinforce-
ment learning in the presence of market frictions such as transaction costs, liquidity constraints, and
risk limits. Their approach applies reinforcement learning to non-linear reward structures based on
convex risk measures and learns trading strategies directly without relying on specific assumptions
about market dynamics. The framework is designed to scale efficiently to high-dimensional settings
and generalizes across different hedging instruments. Empirical results, including experiments on
the S&P 500 and a synthetic market based on the Heston model, show that the method outperforms
standard complete-market hedging approaches under transaction costs.
MaringerandRamtohul(2012)proposearegime-switchingextensionoftherecurrentreinforcement
learning (RRL) model, referred to as RSRRL, to better capture the complexity of financial time
series. The framework introduces regime-dependent dynamics, where switching between regimes is
driven by a volatility-based indicator. The authors present two variants of the model—a threshold
version and a smooth transition version—and evaluate their performance in automated trading
and portfolio management tasks. Out-of-sample results generally favour the RSRRL models over
the standard RRL approach, although concerns regarding robustness remain, particularly in the
presence of transaction costs.
Liu et al. (2021) propose the FinRL-Meta framework, which provides a universe of near real-market
environments for data-driven deep reinforcement learning in finance. The framework separates
financial data processing from the design of trading strategies and offers a unified data engineering
pipeline for accessing, cleaning, and processing large-scale financial data. It includes hundreds of
market environments for various trading tasks and supports efficient training through multiprocessing
using GPU resources. By enabling diverse DRL agents to be trained across these environments, the
framework addresses challenges related to data quality, simulation complexity, and scalability in
8

financial reinforcement learning.
Zhang et al. (2026) propose a deep reinforcement learning framework enhanced by cluster
embedding (CE) and zero-shot prediction for financial trading. The approach groups feature
channels with intrinsic similarities and leverages clustering information instead of individual channel
features to improve representation learning. Zero-shot prediction is achieved by assigning unseen
samples to appropriate clusters, enabling predictions without additional training. The framework
also integrates predicted and observed OHLCV data to form the reinforcement learning state space.
Experimental results on multiple real-world financial datasets show improvements in predictive
accuracy and trading performance, including a cumulative return of 137.94% on the S&P 500.
Deep hedging literature was recently extended by Bracha et al. (2025), who apply a Twin Delayed
Deep Deterministic Policy Gradient (TD3) agent to at-the-money S&P 500 options. Using a walk-
forward procedure, the model is evaluated over a long out-of-sample period and benchmarked against
Black–Scholes delta hedging. The results show that the DRL agent can outperform traditional
hedging methods, particularly in volatile or high-cost environments. The study further demonstrates
that higher risk-awareness penalties can deteriorate performance, while longer volatility estimation
windows lead to more stable results.
Du et al. (2020) introduce a deep reinforcement learning framework for option replication and
hedging under realistic market frictions, including discrete trading, round lotting, and nonlinear
transaction costs. The authors employ several DRL methods, including proximal policy optimization
(PPO), to learn hedging strategies that optimize a trade-off between replication error and trading
costs. Using simulated market environments, they show that the learned strategies achieve similar
or better performance compared to Black–Scholes delta hedging, with PPO exhibiting superior
efficiency in terms of profit and loss, training time, and data requirements.
Kabbani and Duman (2022) propose a deep reinforcement learning framework for automated stock
trading, formulating the problem as a partially observed Markov decision process (POMDP) that
integrates both portfolio allocation and price prediction. The authors employ the Twin Delayed Deep
Deterministic Policy Gradient (TD3) algorithm to learn trading strategies in a continuous action
space, incorporating technical indicators and news sentiment scores into the state representation.
Using historical market data, their approach achieves strong performance, reporting a Sharpe ratio
of 2.68 on unseen test data, and demonstrating that enriched state representations significantly
improve trading outcomes.
Rani et al. (2025) propose a deep reinforcement learning framework for optimal trade execution in
9

high-frequency trading that explicitly incorporates market impact into the decision-making process.
The model integrates market impact directly into the action space and uses high-dimensional inputs
such as limit order book states, trading volumes, and price dynamics. The agent is trained to
maximize cumulative returns while accounting for execution costs and both transient and permanent
market impact. The learned policies adapt order type and quantity based on market conditions.
Experiments using simulated and historical limit order book data show that the DRL agent achieves
a favorable balance between profitability and slippage reduction compared to traditional rule-based
and optimization-based methods.
Yang et al. (2020) propose an ensemble deep reinforcement learning strategy for automated
stock trading that combines multiple actor-critic algorithms, including PPO, A2C, and DDPG. The
ensemble integrates the strengths of these individual models to improve robustness across different
market conditions. The approach is evaluated on a portfolio of 30 Dow Jones stocks and compared
against individual DRL agents as well as traditional benchmarks such as the Dow Jones Industrial
Average and a minimum-variance portfolio strategy. The results show that the ensemble method
achieves higher risk-adjusted returns, as measured by the Sharpe ratio, than both the individual
models and the baseline strategies.
Enkhsaikhan and Jo (2025) formulate portfolio optimization as a constrained Markov decision
process (CMDP) within a risk-averse reinforcement learning framework. To enforce risk-related
constraints required by investors and regulators, the authors employ an augmented Lagrangian
multiplier (ALM) method, enabling the agent to incorporate constraint satisfaction directly into the
decision-making process. The proposed approach demonstrates no constraint violations during testing
and outperforms other risk-averse reinforcement learning methods, highlighting its effectiveness for
constrained portfolio optimization.
Tamuly et al. (2024) apply a Deep Q-Network (DQN) framework with experience replay to
portfolio optimization, where an agent interacts with financial data to dynamically allocate capital
and maximize returns while managing risk. The model learns to predict optimal portfolio weights
over time based on historical price data, refining its strategy through past experiences. Empirical
evaluation on real-world data shows that the proposed approach achieves superior performance
compared to traditional methods, as measured by Sharpe ratio and cumulative returns.
Soleymani and Paquet (2020) proposed DeepBreath, a deep reinforcement learning framework
for portfolio management that combines a restricted stacked autoencoder for feature extraction with
a convolutional neural network to learn investment policies. The model employs both offline and
10

online learning to adapt to market dynamics, while blockchain is used to mitigate settlement risk.
Empirical results show that the approach outperforms existing strategies in terms of return while
minimizing risk.
Jiang et al. (2024) proposed a model-free deep reinforcement learning framework for portfolio
selectionthatincorporatestransactioncostsandinvestorriskaversionintoanextendedmean–variance
reward function. Using a twin-delayed deep deterministic policy gradient (TD3) algorithm, the
approach constructs optimal portfolios in high-dimensional markets and demonstrates superior
performance compared to traditional and DRL-based benchmarks.
Sterling and Thorne (2026) investigate the application of deep reinforcement learning to dynamic
portfolio optimization in financial markets, emphasizing its role as an adaptive alternative to
traditional static allocation methods in environments characterized by non-linear dependencies and
stochastic regimes. The study adopts a system-level perspective, analyzing architectural design
choices, reward function construction, and state-space representation, while also addressing broader
considerations such as algorithmic governance, systemic risk, and the infrastructure required for
deploying DRL in financial systems.
Cheng and Sun (2024) propose a multi-agent deep reinforcement learning framework for multi-
asset trading and portfolio management, where individual agents operate on separate assets and their
experiences are integrated to generate trading strategies and portfolio allocations. The framework
combines a trading action module and a portfolio management module, leveraging the TD3 algorithm
to improve training stability and decision quality. Experimental results on stock market data show
that the approach outperforms single-agent reinforcement learning methods and yields more stable
returns.
Millea (2023) propose a hierarchical model-based deep reinforcement learning framework for
single-asset trading, where a high-level agent dynamically selects among specialized low-level agents
trained on clustered market regimes. By integrating predictive models into the decision process,
the framework bridges model-based and model-free reinforcement learning. Empirical results on
cryptocurrency data show improved performance and support risk-aware optimization via CVaR-
based rewards.
Hao et al. (2023) propose a fuzzy ensemble deep reinforcement learning framework for stock
portfolio management, where fuzzy logic is used to represent market trends through continuous
degrees of bullish, bearish, and oscillatory behavior. The approach combines multiple reinforcement
learning algorithms, including A2C, PPO, DDPG, ACKTR, and TRPO, by averaging their action
11

outputs to form trading decisions. Using S&P 100 constituent stocks and historical market data,
the method demonstrates improved performance compared to benchmark strategies and individual
reinforcement learning models.
Shavandi and Khedmati (2022) propose a multi-agent deep reinforcement learning framework
for algorithmic trading, where multiple agents, each specialized in a distinct trading timeframe,
collaboratively learn trading strategies. The framework employs a hierarchical feedback mechanism
that transfers information from higher- to lower-timeframe agents, enabling the integration of multi-
scale market dynamics. Evaluated on historical EUR/USD data, the approach outperforms single-
agent models and benchmark trading strategies across multiple return- and risk-based performance
metrics.
Wu et al. (2020) propose adaptive stock trading strategies based on deep reinforcement learning,
integrating Gated Recurrent Units (GRU) for feature extraction from financial time-series data. They
introduce two frameworks: a critic-only Gated Deep Q-Network (GDQN) and an actor–critic Gated
Deterministic Policy Gradient (GDPG). Evaluated on stocks from U.S., U.K., and Chinese markets
under both trending and volatile conditions, the proposed methods achieve superior returns and
improved risk-adjusted performance compared to benchmark strategies, with GDPG demonstrating
greater stability.
2.4. Reinforcement Learning Beyond Finance
The reinforcement learning techniques employed in this study originate from foundational advances
in broader decision-making domains. Mnih et al. (2015) introduced the Deep Q-Network (DQN),
establishing that deep neural networks can learn control policies directly from high-dimensional
inputs without handcrafted features. Schulman et al. (2017) subsequently introduced Proximal Policy
Optimization (PPO), addressing training instability in policy gradient methods through a clipped
surrogate objective that constrains policy updates. The Soft Actor-Critic algorithm employed in
this study builds on these foundations, extending the actor-critic framework with maximum-entropy
reinforcement learning to encourage exploration and improve stability in continuous action spaces
(Haarnoja et al., 2018).
These methodological advances are directly relevant to portfolio allocation, where agents must
operate in high-dimensional, non-stationary environments and optimize long-term risk-adjusted
objectives under realistic constraints.
12

2.5. Summary
The literature reviewed in this chapter shows a progressive transformation in quantitative
finance, moving from static optimization frameworks toward adaptive, data-driven decision-making
systems. Early approaches to portfolio construction, were in mean-variance optimization, provided
a mathematical foundation for balancing risk and return. However, their practical limitations,
particularly sensitivity to estimation error and instability in non-stationary environments motivated
the development of more robust and dynamic methodologies. Subsequent advancements incorporated
regime based optimization, and predictive modeling, makeing a shift from purely historical estimation
toward forward-looking portfolio construction.
The introduction of machine learning further accelerated this shift by enabling models to capture
non-linear relationships and complex interactions within financial data. Nevertheless, the literature
consistently highlights fundamental challenges, including the low signal to noise ratio of financial time
series, susceptibility to overfitting, and the evolving nature of market dynamics. While deep learning
architectures, such as recurrent networks and attention based models, have improved the ability
to model temporal dependencies and extract latent features, they remain inherently dependent on
forecasting future returns, which limits their robustness in highly stochastic environments.
Reinforcement learning represents a conceptual departure from these approaches by reframing
financial decision making as a sequential optimization problem rather than a prediction task. Instead
of estimating future prices, reinforcement learning agents directly learn policies that maximize
long-term, risk adjusted performance under realistic constraints such as transaction costs and market
frictions. The literature demonstrates that, when combined with deep neural networks, these
methods are capable of operating in high dimensional state spaces and adapting to changing market
conditions. At the same time, research emphasizes that their performance is highly sensitive to
reward specification, model stability, and the handling of non-stationarity, indicating that careful
design and evaluation are essential.
In summary, the literature suggests that while traditional and supervised learning approaches
provide valuable foundations, they are insufficient to fully address the dynamic and sequential nature
of financial decision making. This motivates the adoption of deep reinforcement learning as a unified
framework for portfolio allocation, capable of integrating prediction, execution, and risk management
within a single adaptive system.
13

3. Data Engineering
This study considers three major equity indices to represent different global markets and provide
diversification across regions. Specifically, theNasdaq-100 equity index, theNikkei 225 equity index,
and theEuro Stoxx 50 equity indexare included in the analysis. These indices capture the dynamics
of U.S., Asian, and European equity markets, respectively, allowing for a comprehensive assessment
of cross-market behavior.
3.1. Data Description
The empirical analysis is based on a multi-source financial dataset constructed for the purpose of
training and evaluating a reinforcement learning framework for dynamic portfolio allocation across
multiple equity indices. The dataset integrates asset-level price information, index membership
dynamics, and benchmark market series.
Daily equity price data for all constituents were obtained using theyfinanceAPI. These data
include standard market variables and form the primary input for the modeling framework. Historical
information on index composition, including constituent additions and deletions over time, was
retrieved from theBloomberg Terminal Anywheresubscription. This information was used to
reconstruct time varying index membership and to address survivorship bias by ensuring that only
assets available at each point in time are considered.
In addition to constituent-level data, benchmark index proxies were incorporated to represent
the performance of each investment universe. For the NASDAQ-100, the Invesco QQQ Trust ETF
(QQQ) was used as a tradable benchmark. For the Euro Stoxx 50, the SPDR Euro Stoxx 50 ETF
(FEZ) was employed due to its long and consistent price history. For the Nikkei 225, the iShares
MSCI Japan ETF (EWJ) is used as a tradable benchmark proxy.
The full sample spans the period from2 January 2003to13 March 2026. Following data
collection, all sources were aligned within a unified preprocessing pipeline to ensure temporal
consistency across price series, benchmark data, and index membership records.
Figures 1 present the normalized price paths of the assets included in the investment universe,
with each series scaled to one at its first available observation. Tables 1 and 2 report descriptive
statistics of the equity indices at the price level and daily log-return level, respectively.
14

Figure 1: Normalized price paths of assets in the two investment universes
Note:The figure displays the price paths of all constituent assets considered in the study. Each series is normalized to unity at
its initial observation. The red line in each panel represents the corresponding benchmark ETF in its original (non-normalized)
price scale.
15

Table 1: Descriptive statistics of the equity indices used in the study.
Index Count Mean Std Min 25% 50% 75% Max
NASDAQ 100 5836 154 154 20 38 87 226 635
Nikkei 225 5676 51 12 27 41 51 59 94
Euro Stoxx 50 5836 30 11 10 23 28 33 69
Note:The descriptive statistics for NASDAQ 100, NIKKEI 225, EUROSTOXX 50 are calculated on the closing price in the
period from 2003-01-02 until 2026-03-13
Table 2: Descriptive statistics of daily log-returns for the equity indices.
Index Mean Std Skewness Ex. Kurtosis Min Max JB p-value
NASDAQ 100 0.0005 0.0136−0.2378 7.1260−0.1276 0.1148<0.001
Nikkei 225 0.0001 0.0128−0.1225 8.6171−0.1078 0.1406<0.001
Euro Stoxx 50 0.0002 0.0159−0.3300 9.8994−0.1331 0.1616<0.001
Note:Statistics are computed on daily log-returns over the full sample period 2003-01-02 to 2026-03-13. Ex. Kurtosis denotes
excess kurtosis relative to the normal distribution. The Jarque–Bera test rejects normality at the 1% significance level for all
three series, confirming the fat-tailed and negatively skewed nature of daily equity returns.
3.2. Data Preparation
This section describes the procedures applied to transform the raw financial data into a consistent
and model ready dataset. Particular attention is given to handling time varying index membership,
ensuring alignment across data sources, and constructing a tradable universe that accurately reflects
real world investment constraints.
3.2.1. Constituents Membership and Survivorship Bias
A key challenge in empirical financial studies is the presence of survivorship bias, which arises
when only currently listed assets are considered, ignoring those that were removed from the index
over time. This leads to an upward bias in performance estimates, as poorly performing or delisted
assets are systematically excluded. To address this issue, historical index membership information
was obtained from the Bloomberg Terminal. The dataset includes all constituent additions and
deletions throughout the sample period, allowing for the reconstruction of the true, time-varying
composition of each index. Figure 2 illustrates the evolution of the number of constituents over
time, highlighting the dynamic nature of the investment universe.
16

Figure 2: Evolution of the number of constiunts over time
95
100
105
2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027
Date
Number of Tradable Stocks
NASDAQ 100 Tradable Universe
223.0
223.5
224.0
224.5
225.0
2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027
Date
Number of Tradable Stocks
Nikkei 225 Tradable Universe
46
47
48
49
50
2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020 2021 2022 2023 2024 2025 2026 2027
Date
Number of Tradable Stocks
Euro Stoxx 50 Tradable Universe
Note:This figure presents how the number of constituents change over time during the period 2003-01-2 until 2026-03-13
3.2.2. Tradable Universe Construction
Following data alignment, asset price data were merged with the historical index membership
matrix described in Section 3.2.1. This matrix was expanded to the daily frequency and combined
with the price dataset to construct a tradability mask. The resulting mask indicates whether a given
asset was both a member of the index and associated with a valid price observation at each point in
time. Formally, the tradability condition ensures that only assets satisfying both membership and
data availability constraints are considered in the investment universe. This approach guarantees that
the model operates on a realistic and time-consistent set of tradable assets, effectively eliminating
survivorship bias and preventing look-ahead errors.
Following the construction of the tradability mask, the two data sources Bloomberg membership
records and yfinance price series are synchronized onto a common daily date index. Specifically, the
Bloomberg membership matrix is expanded to daily frequency by forward-filling constituency status
between recorded addition and deletion events, ensuring that each asset’s tradability is correctly
reflected on every trading day. Price data obtained from yfinance are aligned to this index, with any
17

missing price observations handled via forward-fill to propagate the most recent available closing
price. Assets with no valid price observation at a given date are excluded from the tradable universe
regardless of their membership status, as enforced by the tradability mask. Following this alignment
and filtering procedure, the effective date ranges for the three indices are 2003-01-02 to 2026-03-13
for both the NASDAQ-100 and EURO STOXX 50, and 2003-01-02 to 2026-03-13 for the Nikkei 225,
with minor differences in the number of valid trading days across markets due to differing national
holiday calendars.
3.3. Summary
To summarize the data construction process, Figure 3 presents the full pipeline from raw data
acquisition to the final model-ready dataset.
The process begins with the extraction of historical index membership information from Bloomberg
and price data from yfinance. These datasets are then aligned temporally and combined to construct
the tradable universe through a masking procedure. Finally, the processed data serve as input to
the reinforcement learning framework described in the following section.
Figure 3: Data construction pipeline for the reinforcement learning framework
NASDAQ 100, Nikkei 225, Euro Stoxx 50
Bloomberg
(Historical Membership)
yfinance
(Daily Prices)
Tradable Mask
Model Dataset
Note:The figure illustrates the process of constructing the model-ready dataset.
18

4. Theoretical Background
Financial decision-making inherently involves sequential choices under uncertainty, where actions
taken at a given point in time influence future outcomes and available opportunities. In the context
of portfolio allocation, an investor repeatedly observes market conditions, selects portfolio weights,
and realizes returns that depend on both current decisions and future market dynamics.
This sequential structure naturally aligns with the framework of reinforcement learning (RL),
where an agent interacts with an environment by observing states, taking actions, and receiving
rewards. Unlike traditional optimization approaches that rely on static assumptions or one-step
forecasts, RL provides a dynamic formulation that directly optimizes long-term performance.
This section introduces the theoretical foundations underlying the methodology adopted in this
study. First, the portfolio allocation problem is framed as a sequential decision-making process
within a Markov Decision Process (MDP). Next, the core concepts of reinforcement learning and
value-based optimization are presented. Finally, the extension to deep reinforcement learning and
the role of temporal representations in financial time series are discussed.
4.1. Markov Decision Processes
Portfolio allocation can be naturally formulated as a sequential decision problem. At each time
step t, an agent observes the current market information and selects an action, which corresponds
to a portfolio allocation. The outcome of this decision is uncertain and depends on future market
movements, making the problem inherently stochastic.
A standard framework to model such problems is the Markov Decision Process (MDP), defined
by the tuple(S,A,P,r,γ), where:
•Sis the set of states, representing the information available at timet,
•Ais the set of actions, corresponding to possible portfolio allocations,
•P(s t+1|s t,at)denotes the transition dynamics of the environment,
•r(s t,at)is the reward function,
•γ∈(0,1)is the discount factor.
At each time step, the agent observes a statest∈S , selects an actionat∈A , and receives
a rewardrt, after which the system transitions to a new statest+1. A key assumption in this
19

framework is the Markov property, which states that the future evolution of the system depends
only on the current state and action, and not on the full history:
P(st+1|s t,at,st−1,at−1,...) =P(s t+1|s t,at).(1)
In financial applications, this assumption is an approximation, as market dynamics often depend
on past information. In practice, this limitation is addressed by constructing state representations
that include recent observations, allowing the agent to incorporate relevant historical information
into its decisions.
4.2. Reinforcement Learning
Within the MDP framework, the objective of the agent is to learn a decision rule, or policy, that
maximizes long-term performance. A policy is defined as a mapping from states to actions, denoted
byπ(a|s ), which specifies the probability of taking actiona when the system is in states. The
quality of a policy is evaluated through the expected cumulative reward, referred to as the return.
Starting from timet, the return is defined as:
Gt =
∞∑
k=0
γkrt+k+1,(2)
where γ∈ (0, 1)is the discount factor, controlling the relative importance of immediate versus
future rewards.
To assess the desirability of states and actions, reinforcement learning introduces value functions.
The state-value function (Vπ) measures the expected return starting from a given state under policy
π, while the action-value function (Qπ) evaluates the expected return when taking a specific action
ain states:
Vπ(s) =E π [Gt|s t =s],(3)
Qπ(s,a) =E π [Gt|s t =s,a t =a].(4)
The goal of reinforcement learning is to find an optimal policyπ∗ that maximizes the expected
return. In practice, directly optimizing over all possible policies is infeasible in complex environments.
Instead, modern approaches rely on parameterized policies and value functions, which can be learned
from data through interaction with the environment.
20

A common class of methods is the actor–critic framework, where two components are learned
simultaneously: the actor, which represents the policy, and the critic, which estimates value functions.
This combination enables stable learning by using value estimates to guide policy updates.
4.3. Deep Reinforcement Learning
In practical applications such as portfolio allocation, the state space is typically high-dimensional
and complex, consisting of multiple assets and market indicators observed over time. In such settings,
classical reinforcement learning methods that rely on tabular representations become infeasible.
Deep reinforcement learning addresses this limitation by using neural networks as function
approximators for both the policy and value functions. Instead of explicitly storing values for each
state-action pair, the agent learns parameterized functions that generalize across similar states. This
allows the model to operate in environments with large state spaces and rich feature representations.
However, combining reinforcement learning with function approximation introduces several
challenges. First, the data used for learning is sequential and highly correlated, which can lead
to unstable updates. Second, the target values used for training evolve over time as the policy
improves, creating a moving optimization objective. To mitigate these issues, modern algorithms
employ techniques such as experience replay, target networks, and stochastic optimization.
Another important aspect in financial applications is that decisions depend not only on the
current observation but also on recent patterns in the data. To capture such dependencies, the state
representation is typically constructed to include a window of past observations, allowing the model
to incorporate relevant historical information.
4.4. Representation Learning for Sequential Data
Financial markets exhibit strong dependence on past observations, where recent price movements,
volatility patterns, and market conditions provide important context for decision-making. As a
result, using only current features may lead to a loss of relevant information. To address this, modern
approaches incorporate models that can extract meaningful representations from sequences of past
observations.
Recurrent neural networks (RNNs), and in particular Long Short-Term Memory (LSTM) networks,
are designed to capture such dependencies by maintaining an internal state that evolves as new
data becomes available. This allows the model to summarize relevant information from previous
observations and use it to inform current decisions. Compared to standard feed-forward networks,
21

LSTM architectures are more effective at handling longer dependencies and mitigating issues related
to vanishing gradients.
More recently, attention-based models such as Transformers have been proposed as an alternative
approach. Instead of processing data sequentially, these models use attention mechanisms to identify
and weight the most relevant observations within a given history window. This enables the model to
capture relationships across different time steps without relying on recurrent structures.
Figure 4 provides a schematic illustration of this interaction, highlighting the sequential loop
of state observation, action selection, reward feedback, and state transition that characterizes
reinforcement learning problems.
Figure 4: Illustration of the reinforcement learning agent
Note:The diagram illustrates the interaction between an agent and its environment in a reinforcement learning setting. At each
time step, the agent observes the current statest, selects an actionat according to its policyπθ(a|s ), and receives a reward
signal. The environment transitions to a new statest+1, forming a sequential decision-making loop.
Source: Author’s own illustration.
4.5. Portfolio Allocation as a Sequential Control Problem
The portfolio allocation problem can be naturally framed as a sequential control task within the
reinforcement learning framework. At each time stept, the agent observes the current state of the
market and selects a portfolio allocation across a set of tradable assets. The action is represented by
a vector of portfolio weights:
wt = (w1,t,w 2,t,...,w Nt,t),(5)
whereNt denotes the number of available assets at timet. The weights satisfy the budget constraint:
Nt∑
i=1
wi,t = 1,(6)
22

and, in the long-only setting,wi,t≥0for alli.
Given a portfolio allocation, the realized portfolio return over the next period is given by:
Rp,t+1 =
Nt∑
i=1
wi,tRi,t+1,(7)
whereR i,t+1 denotes the return of asseti.
In practice, portfolio rebalancing incurs transaction costs, which depend on changes in portfolio
weights. These costs introduce a trade-off between responsiveness to new information and excessive
turnover. As a result, the objective is not only to maximize returns, but to optimize performance
net of trading frictions.
Within the reinforcement learning framework, this objective is captured through the reward
function, which reflects realized portfolio performance adjusted for costs and risk considerations.
The agent therefore learns a policy that maps observed market conditions to portfolio allocations,
with the aim of maximizing long-term cumulative reward.
This formulation provides a flexible and dynamic alternative to classical portfolio optimization
approaches, allowing the model to adapt to changing market conditions and incorporate complex,
non-linear relationships between assets and market variables.
5. Methodology
The aim of this section is to present the methodological framework used to construct and evaluate
reinforcement learning based portfolio allocation strategies. Building on the theoretical foundations
introduced in the previous section, the portfolio selection problem is formulated as a sequential
decision-making task, where an agent dynamically allocates capital across a set of tradable assets
over time.
The proposed framework combines a structured state representation derived from asset-level
and market-level features with a reinforcement learning algorithm designed to optimize portfolio
performance under realistic market conditions. In particular, the model accounts for transaction
costs, portfolio rebalancing, and varying market environments through a walk-forward optimization
scheme.
The remainder of this section is organized as follows. First, the state representation, action space,
and reward function are introduced. This is followed by a description of the model architecture and
the considered configuration variants. The training and validation procedure, including walk-forward
23

optimization and adaptive retraining, is then presented. Finally, the performance metrics used in
the empirical analysis are defined.
5.1. State Representation
The reinforcement learning agent operates on a structured state representation composed of both
asset-level and global market features. The objective of the feature set is to capture cross-sectional
differences between assets as well as the prevailing market environment, enabling the agent to make
allocation decisions based on both relative and absolute signals. A set of features were constructed
for each assetiat timet. These features are grouped into four categories.
Before the state is passed to the reinforcement learning agent, a cross-sectional asset selection
step is applied whenever a top-k constraint is imposed. Specifically, the agent is restricted to thek
tradable assets with the highest 120-trading-day momentum, wherek∈{ 20, 30} depending on the
configuration. The momentum measure is defined as
m(120) i,t = Pi,t Pi,t−120 −1,(8)
where Pi,t denotes the daily closing price of asseti at timet. The ranking is computed only among
assets that are tradable and have valid price observations at timet. This selection rule is exogenous
to the reinforcement learning agent and is used to reduce the dimensionality of the action space
while focusing the model on assets with the strongest recent price performance.
5.1.1. Momentum features
These capture short and medium term price dynamics through log returns computed over multiple
horizons:
r(X) i,t = log
(
Pi,t
Pi,t−X
)
,(9)
whereX∈{1,5,20,60}trading days.
5.1.2. Volatility features
These describe recent return variability using rolling standard deviations of daily log returns:
σ(X) i,t =
/radicaltp/radicalvertex/radicalvertex√ 1
X
X∑
j=1
(ri,t−j−¯ri,t)2,(10)
whereX∈{5,20}.
24

5.1.3. Technical indicators features
These were included to capture non linear price dynamics and mean reversion effects. These consist
of the relative strength index (RSI), the moving average convergence divergence (MACD) histogram,
Bollinger Band position (%B), the distance from the rolling 20-day high, and a mean-reversion signal
based on deviations from the 20-day moving average.
5.1.4. Market-relative features
These include a rolling beta estimate computed over a 60-day window with respect to the market
proxy, for example QQQ in case of NASDAQ 100, allowing the agent to account for systematic
exposure. And an absolute performance feature was included in the form of a 20-day log return
series, treated separately from the cross-sectional signals.
5.1.5. Global features
These include the level of the volatility index (VIX) and its 5-day change. Aggregate market
conditions are captured through the cross-sectional average return of tradable assets and its 5-day
rolling volatility. Additional features include market breadth, defined as the proportion of assets
with positive medium-term returns, as well as normalized returns of the market proxy, for example
QQQ in case of NASDAQ 100, over 5-day and 20-day horizons.
5.1.6. Dynamic asset universe
In order to reduce the dimensionality of the action space and focus on the most relevant investment
opportunities, the set of tradable assets is dynamically filtered at each time step. Specifically, the
agent operates on a subset of assets selected based on cross-sectional momentum. At each timet,
only the top-k assets ranked by their 120-day momentum are included in the investable universe.
Momentum is defined as:
momentumi,t = Pi,t Pi,t−120 −1.(11)
This selection procedure ensures that the agent concentrates on assets exhibiting strong recent
performance while maintaining a manageable action space. Sincek is fixed across all time steps
and folds, the top-k selection procedure guarantees a constant state vector dimension regardless
of fluctuations in the number of tradable constituentsNt over time. This ensures that the neural
network encoder receives a fixed-size input at every step, eliminating the need for dynamic padding
or variable-length architectures to handle the time-varying index composition illustrated in Figure 2.
25

5.2. Action Space
The action of the agent at each time stept corresponds to the selection of portfolio weights across
the available assets. Formally, the action is defined as:
at =w t = (w1,t,...,w Nt,t,wc t),(12)
where wi,t denotes the allocation to asseti, wc t represents the allocation to cash, andNt is the
number of tradable assets at timet. In configurations with a top-k restriction, Nt refers to the
number of selected assets after the momentum-based pre-selection step, rather than the full set of
tradable index constituents.
The portfolio weights are constrained such that:
Nt∑
i=1
wi,t +wc t = 1.(13)
To ensure valid portfolio allocations, the policy network outputs parameters of a Dirichlet
distribution, from which the weight vector is sampled. This guarantees that all weights are non-
negative and sum to one.
Two action formulations are considered. In the first, aflatallocation is used, where a single
Dirichlet distribution directly determines the weights across all assets (and cash). In the second, a
hierarchicalstructure is employed, where the policy first determines the overall allocation to equities
relative to cash, and subsequently distributes the equity portion across individual assets using a
Dirichlet distribution.
Depending on the configuration, the environment enforces different constraints. In some setups,
the portfolio is restricted to fully invested long-only positions, while in others, allocations may
include cash and allow for more flexible exposure. These variations enable the analysis of different
portfolio construction regimes within a unified reinforcement learning framework.
5.3. Reward Function
The reward function determines the objective that the reinforcement learning agent seeks to
optimize. In this framework, it is designed to balance portfolio performance with realistic trading
considerations, including transaction costs, trading activity, and diversification.
The reward function is designed to reflect the trade-offs faced by real-world portfolio managers.
In practice, maximizing raw returns alone leads to unstable and highly concentrated strategies.
26

Therefore, the reward combines three components: (i) portfolio performance, (ii) trading frictions,
and (iii) diversification. This ensures that the agent learns economically meaningful strategies that
balance profitability, stability, and implementability.
At each time step, portfolio performance is measured using the log return of the portfolio value.
Letrnet p,t denote the portfolio return net of transaction costs. A logarithmic transformation is applied
to stabilize the learning signal:
˜rp,t = log(1 +r net p,t ).(14)
In addition to returns, two penalty terms are incorporated. First, a turnover penalty discourages
excessive trading, where turnover is defined as theL1 distance between consecutive portfolio weight
vectors. Second, a concentration penalty encourages diversification by penalizing portfolios that
are overly concentrated in a small number of assets. This is measured using the Herfindahl index.
The Herfindahl–Hirschman Index(HHI )is a standard measure of concentration commonly used in
economics and finance. In the context of portfolio allocation, it quantifies how capital is distributed
across assets. A higher HHI indicates that the portfolio is concentrated in fewer assets, while a lower
value corresponds to a more diversified allocation.HHIis defined below:
HHIt =
Nt∑
i=1
w2 i,t,(15)
with the minimum value given by HHImin t = 1/Nt, corresponding to an equal-weight allocation.
Two reward formulations are considered. In the first, the agent maximizes absolute portfolio
performance:
rt = 1000·˜rp,t−λ TO·TOt·100−λ conc·(HHIt−HHI min t )·100,(16)
where TOt denotes portfolio turnover,λTO is the turnover penalty coefficient, andλconc controls the
strength of the concentration penalty.
In the second formulation, the agent maximizes performance relative to a benchmark:
rt = 1000·(˜rp,t−˜rb,t)−λ TO·TOt·100−λ conc·(HHIt−HHI min t )·100,(17)
where˜rb,t denotes the benchmark log return.
Transaction costs are incorporated directly inrnet p,t , while the turnover penalty provides an
additional regularization mechanism to discourage excessive rebalancing beyond the direct cost of
27

trading.
The scaling factors applied to the reward components are introduced to balance their relative
magnitudes and stabilize training. In reinforcement learning, poorly scaled rewards can lead to
unstable gradients or slow convergence. The chosen scaling ensures that return, turnover, and
concentration terms contribute meaningfully to the learning signal. Figure 5 summarizes the reward
functions.
Figure 5: Decomposition of the Reinforcement Learning Reward Function
Note:The diagram illustrates the structure of the reward function used in the reinforcement learning framework.Source:
Author’s own illustration.
5.4. Model Architecture
The portfolio allocation problem is addressed using a deep reinforcement learning framework
based on the Soft Actor–Critic (SAC) algorithm. The model combines a stochastic policy with
function approximation through neural networks, enabling it to operate in a high-dimensional and
continuous action space.
5.4.1. Soft Actor–Critic
SAC is an off-policy actor–critic algorithm that learns a stochastic policy while maximizing
both expected return and policy entropy. This entropy regularization encourages exploration and
leads to more stable learning. The agent consists of a policy network (actor) and two action-value
networks (critics), which are trained using experience replay and soft target updates. Target
28

networks are updated via soft updates controlled by the smoothing parameterτ∈ (0, 1), whereby
the target network parameters are shifted toward the current network parameters at each step:
θ−←τθ + (1−τ )θ−. The entropy coefficientα is held fixed at 0.2 throughout all experiments rather
than using automatic tuning, as adaptiveα introduced training instability across walk-forward folds
due to the non-stationarity of financial return series and the relatively short validation windows. A
fixed value ensures a consistent and reproducible exploration-exploitation trade-off across all markets
and configurations.
5.4.2. State encoding
To process the structured state representation, a neural encoder is employed to transform asset-
level and global features into a compact representation. Asset-level features are first encoded
individually, and their historical information is summarized using a sequence model. In the baseline
configuration, this is achieved using a Long Short-Term Memory (LSTM) network applied to each
asset. The resulting embeddings are then combined using a cross-sectional attention mechanism,
allowing the model to capture relationships across assets.
In one configuration, the LSTM encoder is replaced by a Transformer-based architecture. This
alternative uses self-attention to model dependencies across the input sequence and allows for a
more flexible representation of historical patterns.
5.4.3. Policy network
The policy network maps the encoded state representation to a portfolio allocation. To ensure
valid portfolio weights, the policy outputs parameters of a Dirichlet distribution, from which the
allocation vector is sampled.
Two policy structures are considered. In theflatformulation, a single Dirichlet distribution
directly determines the allocation across all assets and cash. In thehierarchicalformulation, the
policy first determines the overall allocation to equities relative to cash, and then distributes the
equity allocation across individual assets using a Dirichlet distribution. This structure allows the
model to separate high-level allocation decisions from asset selection.
5.4.4. Critic networks
The critic consists of two independent neural networks that estimate the action-value function.
Both critics take as input the encoded state representation together with the proposed action and
output an estimate of the expected return. The use of twin critics mitigates overestimation bias and
improves training stability.
29

5.5. Model Configurations
This study evaluates five reinforcement learning configurations, each representing a distinct
combination of model architecture, policy structure, reward specification, and portfolio constraints.
While all configurations are based on the Soft Actor–Critic framework and share a common feature
representation as mentioned in section 5.1, they differ in key design choices that affect portfolio
construction and learning dynamics.
Each row in Table 3 represents a distinct model configuration, defined by a specific combination
of encoder, policy structure, reward formulation, and portfolio constraints.
Table 3: Overview of reinforcement learning configurations.
Configuration Encoder Policy Reward Constraints Top-k
LSTM_1 LSTM Flat Dirichlet Log return Cash + flexible exposure 20 / 30
LSTM_2 LSTM Hierarchical Log return Cash + flexible exposure 20 / 30
LSTM_NC_1 LSTM Flat Dirichlet Benchmark-relative Fully invested (no cash) 10 / 20
LSTM_NC_2 LSTM Flat Dirichlet Benchmark-relative Fully invested (no cash) 20
TRANSFORMERS Transformer Flat Dirichlet Log return Cash + flexible exposure 20 / 30
Note:All configurations are based on the Soft Actor–Critic (SAC) algorithm. “Cash + flexible exposure” indicates that the
agent can dynamically allocate capital between risky assets and cash, allowing for partial investment and varying market
exposure. In contrast, “fully invested (no cash)” denotes that the portfolio is entirely allocated to risky assets at all times.
Table 4 reports the key reinforcement learning hyperparameters shared across configurations.
These parameters govern the optimization process, including learning rates, replay buffer size, and
update dynamics of the SAC algorithm.
Table 4: Reinforcement learning and optimization hyperparameters.
Parameter Value
Learning rate (actor)3×10 −4
Learning rate (critic)5×10 −4
Learning rate (entropy)3×10 −4
Discount factorγ0.99
Target smoothingτ0.005
Gradient steps 2
Batch size 128
Replay buffer size 20,000
Warm-up steps 500
Entropy coefficientα0.2 (fixed)
Note:This table reports the common reinforcement learning hyperparameters used across all configurations.
30

Table 5 summarizes the sequence encoder architectures used in the model. The configuration of
LSTM differ in hidden size, while the configuration of Transformer uses a two-layer self-attention
encoder.
Table 5: Neural network architecture parameters across configurations.
Encoder Type Hidden Size Layers
LSTM 64 / 128 1
Transformer 128 2
Note:The table summarizes the architecture of the sequence encoders used in the model.
Table 6 presents the environment and training parameters affecting portfolio dynamics and
learning. The transaction costs and penalty terms directly affect the reward function, while the
lookback window defines the length of historical input provided to the model.
Furthermore, the transaction cost assumption of 2 basis points per unit of turnover is consistent
with the lower bound of equity commissions available to institutional and high-volume traders on
Interactive Brokers (IBKR) under the tiered pricing schedule, which ranges from 0.05 to 0.35 bps
per share depending on monthly volume.
Table 6: Environment configuration parameters.
Parameter Value
Lookback window 60 days
Transaction cost 2 bps
Turnover penalty 0.003
Concentration penalty 0.0 / 0.1 / 0.5 (config-dependent)
Epochs 50
Early stopping patience 8
Note:This table reports the environment and training-related parameters.
5.6. Training and Validation Procedure
The training and validation procedure is designed to ensure a realistic and robust evaluation
of the proposed reinforcement learning strategies. Given the non-stationary nature of financial
markets, the framework combines a walk-forward optimization scheme with adaptive retraining and
systematic hyperparameter selection. This approach allows the model to be evaluated in a strictly
out-of-sample setting while dynamically adjusting to changing market conditions.
31

5.6.1. Walk Forward Optimization
Overfitting is a major concern in machine learning models, particularly in financial time-series
applications. Standard cross-validation techniques such ask-fold validation are generally not suitable
for financial data because they ignore the temporal ordering of observations. As a result, model
evaluation based on such methods may lead to overly optimistic performance estimates and poorly
generalizing strategies.
To address this issue, a walk-forward optimization (WFO) framework is employed. As noted by
Carta et al. (2021), walk-forward optimization is one of the most widely used validation techniques
in financial machine learning and algorithmic trading research. The WFO procedure simulates a
realistic trading environment by repeatedly training the model on historical data and evaluating it
on subsequent unseen observations. This approach reduces the risk of overfitting and allows the
model to adapt to evolving market conditions.
Two variants of WFO are commonly used: anchored and non-anchored. In the anchored approach,
each walk shares a common starting point and the training window expands over time. In contrast,
the non-anchored approach uses rolling windows with a fixed length, where both the starting and
ending points shift forward over time. In this study, the non-anchored variant is adopted because it
maintains a constant training horizon and better reflects a realistic portfolio management setting.
The walk-forward scheme used in this study consists of a training window of 5 trading years,
followed by validation and testing windows of one trading year each. The model is trained on
the historical training window, reinforcement learning agent approach is selected using the both
the training window and validation window as described in the subsequent sections, and final
performance is evaluated on the out-of-sample testing period. The walk-forward procedure is
illustrated in Figure 6.
It should be noted that the WFO architecture itself including the 5-year training window, 1-year
validation period, and adaptive retraining criterion (presented in Section 5.6.2) represents a set of
design choices that were not subject to systematic optimization across alternatives. These parameters
were selected based on established conventions in the financial machine learning literature (Carta
et al., 2021) and practical considerations regarding the minimum training horizon required for stable
SAC convergence. As noted by Bailey et al. (2017), ex-post selection of walk-forward parameters
can itself constitute a form of meta-overfitting, producing apparently robust out-of-sample results
that may not generalise to different time horizons.
32

Figure 6: Walk-Forward Optimization Scheme (5-Year Training, 1-Year Validation, 1-Year Test)
Full OOS
Fold 1
Fold 2
Fold 3
Fold 4
Fold 5
Fold 6
Fold 7
Fold 8
Fold 9
Fold 10
Fold 11
Fold 12
Fold 13
Fold 14
Fold 15
Fold 16
2005 2010 2015 2020 2025
Date
Fold
Train
Validation
Test
Full OOS
Note:Green bars represent the training dataset, yellow bars the validation dataset, and red bars the out-of-sample testing
dataset. Dark-red bars indicate the cumulative out-of-sample period. The plot is constructed using the final feature matrix
provided to the reinforcement learning agent. The training window corresponds to five trading years, while the validation and
testing windows correspond to one trading year each.
5.6.2. Adaptive Retraining Strategy
In addition to the walk-forward structure, an adaptive retraining mechanism is employed to
determine when the model should be re-estimated. Instead of retraining at every step, the proce-
dure selectively updates the model based on its recent validation performance, thereby reducing
computational cost while maintaining a realistic deployment setting.
At the first fold, the model is always trained. For each subsequent foldk, the current model is
evaluated on the validation window using the Sharpe ratio computed from daily net returns. Based
on this evaluation, a retraining decision is made.
Let Sk denote the validation Sharpe ratio at foldk. A performance threshold is defined using
recent validation results:
θk = median(Sk−m,...,S k−1)− 1 2 std(Sk−m,...,S k−1),(18)
where the window includes up to the lastm = 5validation observations, provided that at least three
past values are available. For the initial folds where fewer than three prior validation observations
exist (i.e.,k <3), the threshold criterion in Equation 18 cannot be computed and the model is
always retrained regardless of validation performance, ensuring a well-defined cold-start behaviour.
33

Retraining is triggered if any of the following conditions are satisfied:
•S k <0,
•S k <θ k,
• the number of consecutive folds without retraining exceeds a predefined limit (set to 3 folds).
If none of these conditions are met, the previously trained model is carried forward and applied
to the next test period.
The validation Sharpe ratio is computed as:
Sk = ¯rk σk √ A,(19)
where ¯rk and σk denote the mean and standard deviation of daily net portfolio returns on the
validation set, andAis the annualization factor (A= 252).
5.6.3. Hyperparameter-Selection
Within each walk-forward training window, model hyperparameters are selected through a
systematic evaluation of predefined candidate configurations. For each configuration, the agent is
trained on the training dataset and subsequently evaluated on the corresponding validation period.
Performance is assessed using the Sharpe ratio computed over validation returns. To obtain a
more robust estimate of performance, returns are aggregated at the monthly level, and the Sharpe
ratio is computed for each month. This aggregation reduces the influence of short-term noise and
provides a more stable measure of performance across different market conditions. These values are
then summarized to guide model selection.
The selection procedure follows a tiered approach. First, configurations that demonstrate
consistently strong performance across both training and validation data are preferred. Among
these, models with similar performance between training and validation are prioritized, as this
indicates better generalization. If no configuration satisfies these criteria, the model with the highest
validation performance is selected.
This procedure ensures that the selected hyperparameters balance performance and robustness,
thereby reducing the likelihood of overfitting. In particular, the selection process avoids configurations
that exhibit highly unstable performance, such as achieving strong results in a single period while
performing poorly over the remainder of the validation window.
34

5.7. Computational Setup
All experiments were conducted on a cloud-based environment equipped with an NVIDIA L4
GPU (24GB VRAM) using a G2-standard instance configuration with 30GB of system memory.
The computational requirements of the models differed depending on the architecture. Training
a single LSTM based reinforcement learning agent required approximately 14 hours per walk-
forward cycle, while the Transformer based model required approximately 23 hours due to its higher
computational complexity and self attention mechanisms.
5.8. Performance Metrics
To evaluate the performance and robustness of the proposed trading strategies, a set of metrics
commonly used in the financial literature is employed, following Michańków et al. (2022) and Bui
and Ślepaczuk (2022). These metrics provide a comprehensive assessment of profitability, risk,
drawdowns, and trading activity.
Annualized Return Compounded (ARC) measures overall profitability, while Annualized Standard
Deviation (ASD) captures return variability as a proxy for risk. Risk-adjusted performance is
evaluated using both the Sharpe Ratio (SR) and Information Ratio (IR1), with the Modified
Information Ratio (IR2) placing additional emphasis on drawdown control. Maximum Drawdown
(MD) and Maximum Loss Duration (MLD) quantify the severity and persistence of losses.
In addition, portfolio turnover is reported to assess trading intensity and the economic feasibility
of the strategies, particularly in the presence of transaction costs. The detailed definitions of each
metric are presented below.
5.8.0.1. Annualized Return Compounded (ARC).The Annualized Return Compounded shows the
rate of return that was annualized for the given strategy during the period of(0,...,T ). It is expressed
as a percentage.
ARC= (
N∏
t=1
(1 +Rt))
252
N −1×100%(20)
where:
Rt - the percentage rate of return
N- the sample size
Rt is calculated as follows:
Rt = Pt−Pt−1 Pt−1 (21)
35

where:
Pt - the price at the pointt
5.8.0.2. Annualized Standard Deviation (ASD).The Annualized Standard Deviation is a risk
measure.
ASD=
√
252×
/radicaltp/radicalvertex/radicalvertex√ 1
N−1
N∑
t=1
(Rt− ¯R)2×100%(22)
where:
Rt - the percentage rate of return
¯R- the mean rate of return.
N- the sample size
¯Ris calculated in the following way:
¯R= 1 N N∑ t=1 Rt (23)
5.8.0.3. Maximum Drawdown (MD).The Maximum Drawdown gives us the maximum percentage
drawdown throughout the investment and is calculated as follows:
MD(T) = max
s∈[0,T]
(
max
t∈[0,s]
(Ri,T−Ri,s)
)
×100%(24)
5.8.0.4. Maximum Loss Duration (MLD).The Maximum Loss Duration represents the longest
period, expressed in years, between two consecutive local equity curve maxima (Michańków et al.,
2022). It is calculated as follows:
MLD= max
(mj−mi
S
)
(25)
wheremi andmj denote the dates of two consecutive local maxima of the equity curve, andS = 252
is the number of trading days per year, such that MLD is expressed in years.
5.8.0.5. Sharpe Ratio (SR).The Sharpe ratio measures risk-adjusted performance by evaluating
excess return per unit of total volatility. Let(Rt)N t=1 denote the sample of simple portfolio returns,
with mean return ¯R= 1 N ∑N t=1Rt. The Sharpe ratio is defined as:
SR=
¯R
σR
√
252(26)
36

where:
σR - the standard deviation of returns
5.8.0.6. Information Ratio(IR1).The Information Ratio describes the risk-adjusted return metric
based on the relation between ARC to its ASD and is calculated as follows:
IR∗ = ARC ASD (27)
5.8.0.7. Modified Information Ratio(IR2).The Modified Information Ratio is another more complex
and comprehensive risk-adjusted return metric which we regard as themost importantmetric for
the evaluation of strategies in this research and is calculated as follows:
IR∗∗ =IR∗×ARC× sign(ARC) MD (28)
5.8.0.8. Extended Information Ratio (IR3).In addition to IR∗∗, an extended risk-adjusted per-
formance metric is proposed that simultaneously penalizes volatility, maximum drawdown, and
maximum loss duration:
IR∗∗∗ = ARC 3
ASD×MD×MLD (29)
5.8.0.9. Turnover (ADT).Portfolio turnover measures the extent of rebalancing activity over time
and reflects the trading intensity of the strategy. Letwi,t denote the portfolio weight of asseti
at timet, andwc t the corresponding cash weight. Given previous weights(w− i,t,wc,− t ), turnover is
defined as:
TOt =
Nt∑
i=1
|wi,t−w− i,t|+|w c t−wc,− t |(30)
Turnover corresponds to theL1 distance between consecutive portfolio allocations and captures
the magnitude of trading required to rebalance the portfolio. Transaction costs are modeled as
proportional to turnover, and average turnover is reported as the time-averaged percentage across
the evaluation period.
5.9. Benchmark Strategies
To evaluate the performance of the proposed reinforcement learning strategies, four benchmark
portfolios are constructed and maintained throughout the out-of-sample evaluation period.
37

5.9.0.1. Buy & Hold strategy.represents the primary benchmark against which all reinforcement
learning models are compared. It consists of a passive investment in the market index ETF the
Invesco QQQ Trust (QQQ) for the NASDAQ-100, the SPDR Euro Stoxx 50 ETF (FEZ) for the
EURO STOXX 50, and the iShares MSCI Japan ETF (EWJ) for the Nikkei 225 held continuously
without rebalancing throughout the evaluation period. This benchmark is considered the most
stringent point of comparison, as it requires no active management, incurs no transaction costs, and
captures the full market return. Outperforming a passive Buy & Hold strategy on a risk-adjusted
basis is widely regarded as a high bar in empirical portfolio management research (DeMiguel et al.,
2009), and constitutes the central performance criterion of this study.
5.9.0.2. Momentum Top-20 strategy.selects the top 20 assets by 120-day price momentum at each
rebalancing date and allocates capital equally among them. This benchmark captures the well-
documented momentum premium and serves as a comparison point for the momentum pre-selection
mechanism embedded in the RL framework, isolating whether the RL allocation policy adds value
beyond simple momentum-based selection.
5.9.0.3. Equal Weight monthly strategy.allocatescapitaluniformlyacrossthesametop- k momentum-
selected universe used by the RL agent, rebalanced at monthly frequency. Following DeMiguel et al.
(2009), this naive diversification benchmark is included to assess whether the RL policy adds value
over and above the momentum pre-filter alone. If the equal-weight portfolio achieves comparable
performance to the RL strategies, it would suggest that the momentum selection step, rather than
the learned allocation policy, is the primary driver of returns.
5.9.0.4. Markowitz Minimum Variance portfolio.is constructed within the same walk-forward
optimization framework as the reinforcement learning strategies, using a 5-year rolling training
window to estimate the covariance matrix. At each rebalancing date, portfolio weights are obtained
numerically by solving a constrained minimum-variance problem subject to long-only, fully-invested,
and maximum position size constraints, and the portfolio is rebalanced monthly (every 21 trading
days). This benchmark provides a direct comparison between the proposed RL framework and a
classical optimization-based approach under identical data constraints and evaluation conditions.
5.10. Methodology Summary
The overall research framework can be summarized as a sequential pipeline that integrates data
processing, feature construction, model training, and evaluation within a unified reinforcement
38

learning setting. sThe process begins with the collection and preprocessing of financial data, followed
by the construction of asset-level and global features as described in Section 5.1. These features
form the input state representation for the reinforcement learning agent. The agent interacts with
the environment by iteratively observing the state, selecting portfolio allocations, and receiving
rewards based on portfolio performance. The model is trained using the Soft Actor–Critic algorithm
under a walk-forward optimization framework, combined with adaptive retraining and systematic
hyperparameter selection.
For each evaluation period, the trained model generates portfolio allocations, from which per-
formance metrics are computed. This pipeline ensures that all results are obtained in a strictly
out-of-sample setting and reflect realistic trading conditions. A schematic overview of the full
methodology is presented in Figure 7.
From an economic perspective, the proposed framework can be viewed as a dynamic portfolio
allocation mechanism that adapts to changing market conditions. The reinforcement learning agent
learns to balance expected returns, risk, and transaction costs through repeated interaction with the
market environment. The incorporation of turnover and concentration penalties further aligns the
learned strategies with realistic portfolio management objectives, such as diversification and cost
efficiency.
Figure 7: Overview of the reinforcement learning portfolio allocation research methodology
Note:The figure illustrates the end-to-end workflow, from data preprocessing and feature construction to reinforcement learning
training and out-of-sample evaluation.Source:Authors’ own illustration.
39

6. Empirical results
This section presents the empirical evaluation of the proposed reinforcement learning-based
portfolio allocation strategies across different equity markets. For each market, the results are
reported for three reinforcement learning configurations: LSTM with cash allowed, LSTM without
cash, and a Transformer-based model. These approaches are benchmarked against four strategies
described in Section 5.9: a passive Buy & Hold strategy, a Momentum Top-20 portfolio, an Equal-
Weight Monthly portfolio, and a Markowitz Minimum Variance portfolio.
The primary criterion for model selection in this study is the Modified Information Ratio (IR2),
which captures risk-adjusted performance while explicitly penalizing drawdowns. This metric is
considered the most comprehensive measure of strategy quality and is therefore used to identify
the best-performing model within each setting. The Buy & Hold strategy remains the primary
benchmark for comparison, as it represents the most competitive passive alternative requiring no
active management or transaction costs. Results are presented sequentially for each market to assess
both within-market performance and cross-market consistency.
6.1. NASDAQ 100
Figure 8 presents the equity curves for all strategies across the three configurations for the
NASDAQ-100 equity index. Across all panels, the Buy & Hold benchmark and the Equal-Weight
Monthly portfolio exhibit the strongest long-term growth, with RL strategies consistently tracking
below the passive benchmarks throughout the evaluation period. In Panel B, LSTM_NC_1 achieves
the highest absolute return among RL strategies but at the cost of substantially higher volatility and
drawdowns. The Transformer model in Panel C follows a similar trajectory to the LSTM models
without a clear performance advantage.
Table 7 reports the corresponding performance metrics. Based on the IR2 criterion, the Buy
& Hold benchmark achieves the highest value across all panels (IR2 = 0.52), followed closely by
the Equal-Weight Monthly portfolio (IR2 = 0.49). Among the RL strategies, LSTM_2 in Panel
A achieves the strongest risk-adjusted performance (IR2 = 0.46) with the lowest volatility and
drawdown across RL configurations (ASD = 18.67%, MD = 28.77%), reflecting the benefit of the
hierarchical policy in managing downside risk. The Momentum Top-20 strategy underperforms all
other strategies on IR2 despite its high turnover.
Overall, no RL strategy consistently outperforms the passive benchmarks on the NASDAQ-100
in terms of risk-adjusted performance. The strong and persistent upward trend of this index over
40

the evaluation period systematically favors passive allocation strategies, limiting the value of active
reinforcement learning allocation.
Figure 8: Empirical results for the NASDAQ-100 across the three reinforcement learning configurations.
Panel A: RL with LSTM and Cash Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Equity
Panel A: RL with LSTM and Cash Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_1
LSTM_2
Panel B: RL with LSTM and Cash Not-Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Equity
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_NC_1
LSTM_NC_2
Panel C: RL with Transformers
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
2.5
5.0
7.5
10.0
12.5
15.0
17.5
20.0Equity
Panel C: RL with Transformers
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
TRANSFORMERS
Note:The figure presents the empirical results for the NASDAQ-100 under the three model configurations considered in the study.
Panel A corresponds to the LSTM-based model with cash allowed (LSTM_1: flat Dirichlet policy; LSTM_2: hierarchical policy),
Panel B to the LSTM-based model without cash and benchmark-relative reward (LSTM_NC_1: flat Dirichlet, top-k=10/20;
LSTM_NC_2: flat Dirichlet, top-k=20), and Panel C to the Transformer-based model with flat Dirichlet policy and cash
allowed (TRANSFORMERS). Trading begins on 2009-04-01 for the NASDAQ-100.
41

Table 7: Performance Metrics for NASDAQ-100 Strategies
Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe ADT
Panel A: RL with LSTM and Cash Allowed
Buy & Hold1581.9 19.2720.41 35.12 1.9600.9441 0.5180 5.0956 0.96890.000
Momentum Top-20 540.5 12.27 21.65 39.55 2.242 0.5667 0.1758 0.9626 0.6461 36.159
Equal-Weight Monthly 1338.2 18.13 20.47 32.55 2.071 0.8857 0.4933 4.3184 0.9187 0.326
Markowitz Min Variance 1235.2 16.65 19.18 31.001.6670.8681 0.4662 4.6550 0.89780.214
LSTM_1 1234.8 17.61 21.63 32.34 2.258 0.8141 0.4433 3.4589 0.8622 13.782
LSTM_2 919.9 15.6418.67 28.772.262 0.8377 0.4554 3.1500 0.8759 13.951
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold 1581.9 19.27 20.41 35.12 1.9600.9441 0.5180 5.0956 0.96890.000
Momentum Top-20 540.5 12.27 21.65 39.55 2.242 0.5667 0.1758 0.9626 0.6461 36.159
Equal-Weight Monthly 1338.2 18.13 20.47 32.55 2.071 0.8857 0.4933 4.3184 0.9187 0.326
Markowitz Min Variance 1235.2 16.6519.18 31.00 1.6670.8681 0.4662 4.6550 0.89780.214
LSTM_NC_11666.4 19.7024.20 41.23 2.595 0.8140 0.3890 2.9512 0.8678 16.326
LSTM_NC_2 1407.9 18.51 22.63 33.95 2.262 0.8179 0.4460 3.6509 0.8676 14.782
Panel C: RL with Transformers
Buy & Hold1581.9 19.2720.41 35.12 1.9600.9441 0.5180 5.0956 0.96890.000
Momentum Top-20 540.5 12.27 21.65 39.55 2.242 0.5667 0.1758 0.9626 0.6461 36.159
Equal-Weight Monthly 1338.2 18.13 20.47 32.55 2.071 0.8857 0.4933 4.3184 0.9187 0.326
Markowitz Min Variance 1235.2 16.6519.18 31.00 1.6670.8681 0.4662 4.6550 0.89780.214
TRANSFORMERS 1206.9 17.46 21.43 32.27 2.262 0.8147 0.4408 3.4014 0.8619 14.248
Note:All strategies are evaluated on the NASDAQ-100, with trading commencing on 2009-04-06. All reported results are
rounded to four significant figures. Strategy labels refer to the following configurations — LSTM_1: LSTM encoder, flat
Dirichlet policy, log-return reward, cash allowed; LSTM_2: LSTM encoder, hierarchical policy, log-return reward, cash allowed;
LSTM_NC_1: LSTM encoder, flat Dirichlet policy, benchmark-relative reward, fully invested; LSTM_NC_2: LSTM encoder,
flat Dirichlet policy, benchmark-relative reward, fully invested; TRANSFORMERS: Transformer encoder, flat Dirichlet policy,
log-return reward, cash allowed. AR denotes the total cumulative return over the full evaluation period; ARC denotes the
annualized compounded return and is the primary return criterion used throughout this study. IR2 is the primary evaluation
metric for risk-adjusted performance.
6.2. NIKKEI 225
Figure 9 presents the equity curves for all strategies across the three configurations for the Nikkei
225 equity index. Across all panels, the Markowitz Minimum Variance and Equal-Weight Monthly
portfolios exhibit the strongest long-term growth, substantially outperforming both the Buy & Hold
benchmark and all RL strategies. The Buy & Hold benchmark delivers the weakest performance,
reflecting the challenging nature of the Japanese equity market over the evaluation period. In
Panel A, LSTM_1 tracks closest to the leading benchmarks among RL strategies. In Panel B, the
fully invested configurations trail substantially behind the passive benchmarks. Panel C shows the
Transformer model achieving intermediate performance between the two LSTM configurations.
Table 8 reports the corresponding performance metrics. The Markowitz Minimum Variance
portfolio achieves the highest ARC (13.17%) and IR1 (0.61), while the Equal-Weight Monthly
portfolio leads on IR2 (0.19). Among the RL strategies, LSTM_1 in Panel A achieves the strongest
risk-adjusted performance (IR2 = 0.15) and the highest IR3 (2.50), with the lowest MLD (0.690)
reflecting effective drawdown recovery. The Buy & Hold benchmark substantially underperforms all
other strategies, driven by its extremely high MLD of 11.345 indicating a recovery period of over
42

eleven years following the 2008 financial crisis.
Overall, the Nikkei 225 results reveal that simple diversification strategies such as Equal-Weight
Monthly and Markowitz Minimum Variance add substantial value over passive index exposure in
this market. While RL strategies outperform the Buy & Hold benchmark, they do not consistently
match the performance of the classical benchmarks.
43

Figure 9: Empirical results for the NIKKEI 225 across the three reinforcement learning configurations.
Panel A: RL with LSTM and Cash Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1
2
3
4
5Equity
Panel A: RL with LSTM and Cash Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_1
LSTM_2
Panel B: RL with LSTM and Cash Not-Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1
2
3
4
5Equity
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_NC_1
LSTM_NC_2
Panel C: RL with Transformers
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1
2
3
4
5Equity
Panel C: RL with Transformers
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
TRANSFORMERS
Note:The figure presents the empirical results for the Nikkei 225 under the three model configurations considered in the study.
Panel A corresponds to the LSTM-based model with cash allowed (LSTM_1: flat Dirichlet policy; LSTM_2: hierarchical policy),
Panel B to the LSTM-based model without cash and benchmark-relative reward (LSTM_NC_1: flat Dirichlet, top-k=10/20;
LSTM_NC_2: flat Dirichlet, top-k=20), and Panel C to the Transformer-based model with flat Dirichlet policy and cash
allowed (TRANSFORMERS). Trading begins on 2009-04-06 for the Nikkei 225.
44

Table 8: Performance Metrics for Nikkei 225 Strategies
Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe ADT
Panel A: RL with LSTM and Cash Allowed
Buy & Hold 171.0 4.57 20.41 55.80 11.345 0.2239 0.0183 0.0074 0.3189 0.000
Momentum Top-20 196.5 7.29 21.02 45.06 3.567 0.3468 0.0561 0.1145 0.4370 35.191
Equal-Weight Monthly 514.6 12.40 20.86 39.33 3.060 0.59440.18740.7603 0.6630 0.261
Markowitz Min Variance665.4 13.1721.76 46.23 1.0480.60520.1724 2.16960.6772 0.239
LSTM_1 418.2 11.22 20.96 39.09 0.690 0.5353 0.15362.49790.6105 23.497
LSTM_2 285.8 9.1218.37 38.27 0.5710.4965 0.1183 1.8876 0.5652 18.858
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold 171.0 4.5720.4155.80 11.345 0.2239 0.0183 0.0074 0.3189 0.000
Momentum Top-20 196.5 7.29 21.02 45.06 3.567 0.3468 0.0561 0.1145 0.4370 35.191
Equal-Weight Monthly 514.6 12.40 20.8639.333.060 0.59440.18740.7603 0.6630 0.261
Markowitz Min Variance665.4 13.1721.76 46.23 1.0480.60520.17242.1696 0.6772 0.239
LSTM_NC_1 285.7 9.11 24.15 53.070.6900.3772 0.0648 0.8546 0.4813 20.789
LSTM_NC_2 291.8 9.22 23.72 49.980.6900.3887 0.0717 0.9570 0.4897 20.036
Panel C: RL with Transformers
Buy & Hold 171.0 4.5720.4155.80 11.345 0.2239 0.0183 0.0074 0.3189 0.000
Momentum Top-20 196.5 7.29 21.02 45.06 3.567 0.3468 0.0561 0.1145 0.4370 35.191
Equal-Weight Monthly 514.6 12.40 20.86 39.33 3.060 0.59440.18740.7603 0.6630 0.261
Markowitz Min Variance665.4 13.1721.76 46.23 1.0480.60520.17242.1696 0.6772 0.239
TRANSFORMERS 283.8 9.09 21.4738.83 0.6900.4234 0.0991 1.3062 0.5110 20.650
Note:All strategies are evaluated on the Nikkei 225, with trading commencing on 2009-04-01. All reported results are rounded
to four significant figures. Strategy labels refer to the following configurations — LSTM_1: LSTM encoder, flat Dirichlet policy,
log-return reward, cash allowed; LSTM_2: LSTM encoder, hierarchical policy, log-return reward, cash allowed; LSTM_NC_1:
LSTM encoder, flat Dirichlet policy, benchmark-relative reward, fully invested; LSTM_NC_2: LSTM encoder, flat Dirichlet
policy, benchmark-relative reward, fully invested; TRANSFORMERS: Transformer encoder, flat Dirichlet policy, log-return
reward, cash allowed. AR denotes the total cumulative return over the full evaluation period; ARC denotes the annualized
compounded return and is the primary return criterion used throughout this study. IR2 is the primary evaluation metric for
risk-adjusted performance.
6.3. EURO STOXX 50
Figure 10 presents the equity curves for all strategies across the three configurations for the
EURO STOXX 50 equity index. Across all panels, the Equal-Weight Monthly portfolio exhibits
the strongest long-term growth, followed by the Markowitz Minimum Variance portfolio. In Panel
A, LSTM_2 tracks closest to the leading benchmarks among RL strategies, exhibiting notably
smoother growth than the Buy & Hold benchmark. In Panel B, the fully invested configurations
underperform relative to Panel A but remain above the Buy & Hold benchmark. Panel C shows the
Transformer model achieving competitive performance, closely tracking LSTM_1.
Table 9 reports the corresponding performance metrics. The Equal-Weight Monthly portfolio
achieves the highest ARC (10.24%) and AR (384.8%) across all strategies. Among the RL strategies,
LSTM_2 in Panel A achieves the strongest risk-adjusted performance, with the highest IR2 (0.15)
and IR1 (0.52) across all RL configurations, and the lowest volatility and drawdown (ASD = 15.97%,
MD = 29.94%). Notably, all RL strategies outperform the Buy & Hold benchmark on IR2, in
contrast to the results observed for the NASDAQ-100 and Nikkei 225. The Markowitz Minimum
Variance portfolio achieves the lowest MLD (0.413) and ADT (0.172), reflecting its focus on variance
minimization.
45

Overall, the EURO STOXX 50 results present the most favorable environment for reinforcement
learning allocation among the three markets studied. All RL strategies outperform the Buy &
Hold benchmark on risk-adjusted metrics, with LSTM_2 delivering the strongest performance. The
relatively lower trend persistence and higher structural uncertainty of the European equity market
appear to provide conditions more conducive to active RL-based allocation.
46

Figure 10: Empirical results for the EURO STOXX 50 across the three reinforcement learning configurations.
Panel A: RL with LSTM and Cash Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1.5
2.0
2.5
3.0
3.5
4.0
4.5Equity
Panel A: RL with LSTM and Cash Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_1
LSTM_2
Panel B: RL with LSTM and Cash Not-Allowed
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1.5
2.0
2.5
3.0
3.5
4.0
4.5Equity
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
LSTM_NC_1
LSTM_NC_2
Panel C: RL with Transformers
2010 2012 2014 2016 2018 2020 2022 2024 2026
Date
1.5
2.0
2.5
3.0
3.5
4.0
4.5Equity
Panel C: RL with Transformers
Buy & Hold
Momentum T op-20
Equal-Weight Monthly
Markowitz Min Variance
TRANSFORMERS
Note:The figure presents the empirical results for the EURO STOXX 50 under the three model configurations considered
in the study. Panel A corresponds to the LSTM-based model with cash allowed (LSTM_1: flat Dirichlet policy; LSTM_2:
hierarchical policy), Panel B to the LSTM-based model without cash and benchmark-relative reward (LSTM_NC_1: flat Dirichlet,
top-k=10/20; LSTM_NC_2: flat Dirichlet, top-k=20), and Panel C to the Transformer-based model with flat Dirichlet policy
and cash allowed (TRANSFORMERS). Trading begins on 2009-04-01 for the EURO STOXX 50.
47

Table 9: Performance Metrics for EURO STOXX 50 Strategies
Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe ADT
Panel A: RL with LSTM and Cash Allowed
Buy & Hold 238.2 7.81 23.92 39.69 1.643 0.3265 0.0642 0.3051 0.4333 0.000
Momentum Top-20 209.0 7.22 21.07 33.37 1.548 0.3427 0.0741 0.3465 0.4348 39.184
Equal-Weight Monthly384.8 10.2420.63 39.40 1.139 0.4964 0.1290 1.1582 0.5738 0.859
Markowitz Min Variance 343.3 9.11 18.31 36.240.4130.4975 0.12512.76400.56530.172
LSTM_1 275.5 8.55 18.71 33.52 1.048 0.4570 0.1166 0.9508 0.5301 10.613
LSTM_2 265.4 8.3615.97 29.941.0600.5235 0.14621.15250.580711.416
Panel B: RL with LSTM and Cash Not-Allowed
Buy & Hold 238.2 7.81 23.92 39.69 1.643 0.3265 0.0642 0.3051 0.4333 0.000
Momentum Top-20 209.0 7.22 21.0733.371.548 0.3427 0.0741 0.3465 0.4348 39.184
Equal-Weight Monthly384.8 10.2420.63 39.40 1.139 0.49640.12901.15820.57380.859
Markowitz Min Variance 343.3 9.1118.3136.240.413 0.49750.12512.76400.56530.172
LSTM_NC_1 208.3 7.23 19.87 34.49 1.131 0.3639 0.0763 0.4885 0.4492 15.661
LSTM_NC_2 280.6 8.64 19.52 34.50 1.091 0.4426 0.1108 0.8765 0.5202 12.697
Panel C: RL with Transformers
Buy & Hold 238.2 7.81 23.92 39.69 1.643 0.3265 0.0642 0.3051 0.4333 0.000
Momentum Top-20 209.0 7.22 21.07 33.37 1.548 0.3427 0.0741 0.3465 0.4348 39.184
Equal-Weight Monthly384.8 10.2420.63 39.40 1.139 0.49640.12901.15820.57380.859
Markowitz Min Variance 343.3 9.1118.3136.240.413 0.49750.12512.76400.56530.172
TRANSFORMERS 284.7 8.71 18.7833.161.048 0.4638 0.1218 1.0126 0.5367 8.418
Note:All strategies are evaluated on the EURO STOXX 50, with trading commencing on 2009-04-01. All reported results
are rounded to four significant figures. Strategy labels refer to the following configurations — LSTM_1: LSTM encoder, flat
Dirichlet policy, log-return reward, cash allowed; LSTM_2: LSTM encoder, hierarchical policy, log-return reward, cash allowed;
LSTM_NC_1: LSTM encoder, flat Dirichlet policy, benchmark-relative reward, fully invested; LSTM_NC_2: LSTM encoder,
flat Dirichlet policy, benchmark-relative reward, fully invested; TRANSFORMERS: Transformer encoder, flat Dirichlet policy,
log-return reward, cash allowed. AR denotes the total cumulative return over the full evaluation period; ARC denotes the
annualized compounded return and is the primary return criterion used throughout this study. IR2 is the primary evaluation
metric for risk-adjusted performance.
6.4. Statistical Significance
While several reinforcement learning strategies exhibit competitive performance in terms of
risk-adjusted metrics, formal statistical inference is required to determine whether these differences
are statistically meaningful. A key challenge in this context is that financial return series typically
violate the assumptions underlying standard parametric tests. In particular, daily returns are known
to exhibit autocorrelation, heteroskedasticity, and non-normality (e.g., volatility clustering and
heavy tails). As a result, conventional paired sample t-tests may lead to biased inference due to
underestimated standard errors.
To address these issues, statistical significance is evaluated using two complementary approaches.
First, we employ Newey–West heteroskedasticity and autocorrelation consistent (HAC) estimators
(Newey and West (1987)) to obtain robust standard errors for the mean return differences between
each strategy and the benchmark. Second, we apply a stationary block bootstrap procedure (Politis
and Romano (1994)) to construct empirical distributions of performance measures and assess
significance without relying on parametric assumptions.
In addition to mean return differences, statistical significance is also evaluated for risk-adjusted
48

performance metrics, namely the Sharpe ratio and IR2, using bootstrap-based inference.
The null hypothesis in this setting is defined as:



H0 :µ d =µ strategy−µ benchmark = 0
H1 :µ d>0
(31)
where µstrategy and µbenchmark denote the expected returns of the evaluated strategy and the Buy &
Hold benchmark, respectively. The significance level is set at 10%. In all tests, the Buy & Hold
strategy serves as the primary benchmark, consistent with the evaluation framework described in
Section 5.9.
The results of the HAC-adjusted tests and stationary bootstrap inference are reported in Table 10.
Across all considered markets, none of the reinforcement learning strategies achieve statistical
significance in terms of mean return differences relative to the benchmark. This holds consistently
for both HAC-adjusted p-values and bootstrap based inference for Sharpe and IR2 differences. These
findings indicate that, despite observable differences in performance metrics, the null hypothesis of
equal expected returns cannot be rejected. Consequently, the apparent outperformance of certain
strategies should be interpreted with caution, as it may reflect random variation rather than
systematic excess returns.
49

Table 10: HAC-adjusted and bootstrap-based statistical significance results
Model Mean Diff. HAC p-val∆Sharpe p-val∆IR2 p-val
Panel A: NASDAQ-100
LSTM-1 -0.0000 0.6654 -0.0972 0.8322 -0.0443 0.7872
LSTM-2 -0.0001 0.9489 -0.0838 0.7762 -0.0326 0.7502
LSTM-NC-1 0.0001 0.3129 -0.0915 0.7832 -0.0986 0.7313
LSTM-NC-2 0.0000 0.4914 -0.0917 0.8062 -0.0417 0.7672
Transformer -0.0000 0.6968 -0.0975 0.8282 -0.0470 0.7882
Panel B: Nikkei 225
LSTM-1 0.0000 0.3381 0.0566 0.3556 0.0060 0.3636
LSTM-2 -0.0001 0.6949 0.0131 0.5005 -0.0288 0.4725
LSTM-NC-1 -0.0000 0.5006 -0.0705 0.7403 -0.0828 0.7612
LSTM-NC-2 -0.0000 0.5025 -0.0624 0.7213 -0.0759 0.7273
Transformer -0.0000 0.6034 -0.0427 0.6913 -0.0488 0.6903
Panel C: EURO STOXX 50
LSTM-1 0.0000 0.4992 0.1144 0.1538 0.0597 0.1349
LSTM-2 -0.0000 0.5840 0.16450.07190.08860.0619
LSTM-NC-1 -0.0000 0.6263 0.0335 0.4086 0.0205 0.3786
LSTM-NC-2 0.0000 0.4665 0.1045 0.1928 0.0540 0.1608
Transformer 0.0000 0.4758 0.1209 0.1399 0.0648 0.1229
Note:HAC p-values are based on Newey–West standard errors for mean return differences. Bootstrap p-values are based on the
stationary bootstrap for Sharpe and IR2 differences. Statistical significance at the 10% level is indicated in bold.
To further investigate the presence of abnormal performance, we estimate a regression model of
strategy returns on benchmark returns, following a standard approach in empirical finance:
Rstrategy t =α+βR benchmark t +ϵt (32)
where the interceptα represents abnormal returns relative to the benchmark. To ensure robustness,
Newey–West HAC-adjusted standard errors are used to account for autocorrelation and heteroskedas-
ticity in the residuals. Statistical significance is evaluated based on the following hypotheses:
50




H0 :α= 0
H1 :α>0
(33)
The regression results are presented in Table 11. For the NASDAQ-100 and Nikkei 225 indices,
none of the strategies exhibit statistically significant abnormal returns after applying HAC corrections.
In contrast, for the EURO STOXX 50 index, several strategies particularly LSTM-based models
and the Transformer model achieve positive and statistically significant intercepts at the 10% level.
This suggests the presence of abnormal returns in this market, even after accounting for time-series
dependencies in the data.
Table 11: Regression-based statistical significance results (HAC-adjusted)
ModelαSE(α)t α pα
Panel A: NASDAQ-100
LSTM-1 -0.0000 0.0001 -0.06 0.5220
LSTM-2 -0.0000 0.0001 -0.01 0.5053
LSTM-NC-1 0.0000 0.0001 0.29 0.3860
LSTM-NC-2 0.0000 0.0001 0.04 0.4836
Transformer -0.0000 0.0001 -0.06 0.5246
Panel B: Nikkei 225
LSTM-1 0.0001 0.0001 1.08 0.1399
LSTM-2 0.0001 0.0001 0.70 0.2427
LSTM-NC-1 0.0000 0.0001 0.11 0.4564
LSTM-NC-2 0.0000 0.0001 0.12 0.4506
Transformer 0.0000 0.0001 0.28 0.3899
Panel C: EURO STOXX 50
LSTM-1 0.0002 0.0001 1.830.0333
LSTM-2 0.0002 0.0001 2.260.0120
LSTM-NC-1 0.0001 0.0001 1.15 0.1243
LSTM-NC-2 0.0002 0.0001 1.730.0417
Transformer 0.0002 0.0001 1.890.0291
Note:The table reports abnormal returns (α) estimated from the regression model with Newey–West HAC-adjusted standard
errors. Statistical significance at the 10% level is indicated in bold.
51

Taken together, the results provide only partial support for the main hypothesis. While no statis-
tically significant outperformance is observed in terms of raw return differences across any market,
there is evidence of abnormal performance in the EURO STOXX 50 based on regression analysis.
Overall, these findings should be interpreted as exploratory, indicating that reinforcement learning
strategies may capture certain market-specific inefficiencies, but do not consistently outperform
benchmark strategies in a statistically robust manner across different markets.
6.5. Summary
Based on the results presented in Tables 7, 8, and 9, the performance of the proposed reinforcement
learning strategies differs substantially across the considered equity indices. Using the Modified
Information Ratio (IR2) as the primary evaluation criterion, the best-performing reinforcement
learning strategy for the NASDAQ-100 is LSTM_2 with cash allowed (IR2 = 0.46), however the
Equal-Weight Monthly portfolio (IR2 = 0.49) and the Buy & Hold benchmark (IR2 = 0.52) remain
superior in this market. For the Nikkei 225, LSTM_1 with cash allowed achieves the strongest
RL performance (IR2 = 0.15), but is outperformed by the Equal-Weight Monthly portfolio (IR2
= 0.19) and the Markowitz Minimum Variance portfolio (IR1 = 0.61). In contrast, for the EURO
STOXX 50, all reinforcement learning strategies outperform the Buy & Hold benchmark on IR2.
The strongest result is obtained by LSTM_2 with cash allowed (IR2 = 0.15), followed by the
Equal-Weight Monthly portfolio (IR2 = 0.13) and the Transformer model (IR2 = 0.12).
It is also important to note that the fully invested configurations generally produce higher absolute
returns, but at the cost of larger drawdowns and lower risk-adjusted performance. This pattern is
particularly visible for the NASDAQ-100, where LSTM_NC_1 attains the highest absolute return
of 1666.4%, yet its IR2 falls to 0.39, below that of the cash-allowed LSTM_2 model. These results
suggest that allowing the agent to hold cash improves the balance between return generation and
drawdown control.
Furthermore, the HAC-adjusted tests and stationary bootstrap inference reported in Table 10
indicate that none of the evaluated reinforcement learning strategies achieve statistically significant
outperformance relative to the Buy & Hold benchmark in terms of mean return differences or
risk-adjusted performance measures. However, the regression analysis reported in Table 11 reveals
that several strategies exhibit statistically significant abnormal returns in the EURO STOXX 50,
while no such significance is observed for the NASDAQ-100 or Nikkei 225. These findings suggest
that while reinforcement learning strategies do not exhibit statistically robust outperformance in
52

terms of raw returns, there is evidence of market-specific abnormal performance in the EURO
STOXX 50.
7. Regime Analysis
To assess whether aggregate results mask heterogeneous performance across market environments,
the evaluation period is decomposed into three macroeconomic regimes: the post-GFC recovery
(2009–2013), the secular bull market (2014–2019), and the COVID-19 shock combined with the rate
hike cycle (2020–2026). Tables 12, 13, and 14 report the corresponding results.
For theNASDAQ-100, the Markowitz Minimum Variance portfolio dominates the post-GFC
recovery period across all metrics, followed by RL strategies which outperform Buy & Hold during
this regime. However, in both subsequent periods passive benchmarks dominate, with Buy & Hold
and Equal-Weight Monthly leading on IR2. The persistent upward trend of the NASDAQ-100
systematically favors passive allocation and limits the value of active management across both
classical and RL-based approaches.
For theNikkei 225, the Equal-Weight Monthly and Markowitz portfolios dominate during the
post-GFC recovery, while Buy & Hold delivers the weakest performance across all strategies in this
period. The pattern reverses in 2014–2019, where LSTM_2 achieves the strongest performance
across all strategies including the classical benchmarks. In 2020–2026, Markowitz Minimum Variance
leads, followed by LSTM-based RL strategies, while Buy & Hold again delivers the weakest result.
This consistent underperformance of passive index exposure on the Japanese market highlights the
structural challenges of the Nikkei 225 as a buy-and-hold investment over this period.
For theEURO STOXX 50, the Momentum Top-20 and Markowitz portfolios lead in the first
two regimes respectively, with all RL strategies consistently outperforming Buy & Hold on IR2
across all three periods. In 2020–2026, LSTM_2 achieves the highest IR2 among all strategies, while
Momentum Top-20 collapses to near-zero performance, suggesting that momentum-based selection
is particularly fragile in the post-COVID European equity environment.
Overall, the sub-period decomposition reveals that no single strategy type dominates consistently
across all markets and regimes. RL strategies add meaningful value relative to Buy & Hold in several
settings, particularly on the Nikkei 225 and EURO STOXX 50, but do not consistently outperform
classical benchmarks such as Equal-Weight Monthly and Markowitz Minimum Variance. These
findings underscore the importance of evaluating active strategies against a broad set of benchmarks
and highlight the regime-dependence of RL portfolio allocation performance.
53

Table 12: Sub-Period Performance Metrics – NASDAQ-100
Period Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe
2009–2013: Post-GFC Recovery
Buy & Hold 178.04 23.98 18.33 16.10 0.480 1.3082 1.9485 9736.71 1.2735
Equal-Weight Monthly 204.06 26.41 20.04 21.29 0.766 1.3179 1.6348 5637.73 1.2761
Markowitz Min Var245.84 29.9618.3417.03 0.310 1.6336 2.8739 27826.48 1.5276
Momentum Top-20 184.26 24.54 21.41 22.40 0.972 1.1462 1.2557 3168.66 1.1409
LSTM_1 222.91 27.93 20.68 17.51 0.909 1.3506 2.1543 6622.14 1.3035
LSTM_2 175.93 23.8117.4016.24 0.742 1.3684 2.0062 6438.49 1.3221
TRANSFORMERS 212.99 27.09 20.16 17.31 0.913 1.3437 2.1030 6244.44 1.2993
2014–2019: Secular Bull Market
Buy & Hold164.14 17.6216.63 22.80 0.619 1.0595 0.8188 2332.981.0625
Equal-Weight Monthly 154.54 16.89 16.30 20.510.5521.0362 0.8533 2613.22 1.0427
Markowitz Min Var 103.42 12.6016.3124.460.5520.7725 0.3980 909.05 0.8139
Momentum Top-20 57.94 7.90 17.23 27.77 1.433 0.4585 0.1304 71.92 0.5309
LSTM_1 122.42 14.26 17.20 23.51 1.214 0.8291 0.5029 590.75 0.8654
LSTM_2 115.02 13.63 14.7420.370.579 0.92470.6187 1455.260.9446
TRANSFORMERS 122.58 14.27 17.26 23.57 1.214 0.8268 0.5006 588.84 0.8635
2020–2026: COVID + Rate Hike Cycle
Buy & Hold118.58 15.9925.50 36.43 1.9640.6271 0.2752 224.02 0.7164
Equal-Weight Monthly 81.62 12.00 24.73 33.68 2.075 0.4852 0.1729 99.98 0.5870
Markowitz Min Var 80.84 11.9922.66 31.00 0.7220.5291 0.2047 340.06 0.6173
Momentum Top-20 34.53 5.67 25.96 40.74 2.254 0.2184 0.0304 7.64 0.3495
LSTM_1 85.86 12.39 26.46 32.34 2.258 0.4683 0.1794 98.50 0.5825
LSTM_2 71.89 10.73 23.25 28.77 2.262 0.4615 0.1721 81.74 0.5640
TRANSFORMERS 87.60 12.60 26.29 32.27 2.262 0.4793 0.1871 104.21 0.5914
Note:Sub-period performance metrics for NASDAQ-100. Buy & Hold is the Invesco QQQ Trust ETF (QQQ).
Table 13: Sub-Period Performance Metrics – Nikkei 225
Period Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe
2009–2013: Post-GFC Recovery
Buy & Hold 52.43 9.35 19.21 25.29 2.131 0.4867 0.1799 78.95 0.5724
Equal-Weight Monthly113.82 17.6823.05 28.100.520 0.7670 0.4826 1642.69 0.8319
Markowitz Min Var 92.67 15.08 23.4127.840.607 0.6442 0.3489 866.20 0.7271
Momentum Top-20 51.88 9.39 24.12 44.75 3.560 0.3893 0.0817 21.58 0.4973
LSTM_1 64.43 11.32 22.39 35.80 2.925 0.5056 0.1599 61.88 0.5942
LSTM_2 28.95 5.5820.5938.27 3.583 0.2710 0.0395 6.16 0.3712
TRANSFORMERS 40.32 7.56 23.28 38.82 2.925 0.3247 0.0632 16.34 0.4327
2014–2019: Secular Bull Market
Buy & Hold 16.78 2.83 15.02 25.69 1.909 0.1884 0.0208 3.08 0.2509
Equal-Weight Monthly 49.00 7.16 19.64 27.91 1.921 0.3646 0.0935 34.84 0.4437
Markowitz Min Var 8.41 1.50 19.58 38.84 1.952 0.0766 0.0030 0.23 0.1684
Momentum Top-20 20.80 3.39 19.43 35.20 2.175 0.1745 0.0168 2.63 0.2628
LSTM_1 62.98 8.71 19.77 24.39 1.214 0.4406 0.1573 113.03 0.5192
LSTM_263.55 8.76 16.62 17.41 1.214 0.5271 0.2652 191.49 0.5864
TRANSFORMERS 48.28 6.98 19.32 30.61 1.901 0.3613 0.0824 30.29 0.4435
2020–2026: COVID + Rate Hike Cycle
Buy & Hold 13.77 2.998 19.03 35.92 3.417 0.1575 0.0131 1.15 0.2298
Equal-Weight Monthly 79.70 12.48 20.20 33.59 0.675 0.6178 0.2295 424.52 0.6759
Markowitz Min Var113.38 16.4321.2828.75 0.683 0.7721 0.4412 1063.07 0.8148
Momentum Top-20 51.16 8.74 19.80 30.45 0.687 0.4414 0.1267 161.54 0.5125
LSTM_1 93.36 14.1220.9431.38 0.691 0.6743 0.3034 620.58 0.7292
LSTM_2 82.93 12.84 18.15 27.88 0.571 0.7074 0.3258 731.43 0.7502
TRANSFORMERS 84.45 13.06 22.12 31.32 0.691 0.5904 0.2462 465.71 0.6597
Note:Sub-period performance metrics for Nikkei 225. Buy & Hold is the iShares MSCI Japan ETF (EWJ).
54

Table 14: Sub-Period Performance Metrics – EURO STOXX 50
Period Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe
2009–2013: Post-GFC Recovery
Buy & Hold 85.86 13.65 30.42 37.80 2.488 0.4487 0.1620 88.89 0.5750
Equal-Weight Monthly101.17 15.5024.28 34.71 2.262 0.6384 0.2851 195.16 0.7184
Markowitz Min Var 77.71 12.6520.24 24.28 1.3650.6250 0.3256 301.90 0.6914
Momentum Top-20 114.98 17.13 25.31 29.02 1.5910.6768 0.3995 430.22 0.7541
LSTM_1 67.48 11.23 21.56 27.45 1.944 0.5209 0.2131 123.06 0.6037
LSTM_2 69.61 11.52 18.61 23.74 1.917 0.6190 0.3004 180.71 0.6815
TRANSFORMERS 71.77 11.81 21.68 27.40 1.917 0.5447 0.2348 144.63 0.6257
2014–2019: Secular Bull Market
Buy & Hold 11.22 1.68 17.13 30.84 3.298 0.0981 0.0053 0.27 0.1887
Equal-Weight Monthly 51.66 7.12 17.12 25.11 1.972 0.4159 0.1179 42.59 0.4866
Markowitz Min Var77.28 9.92 16.4823.59 2.0830.6019 0.2531 120.50 0.6569
Momentum Top-20 29.84 4.42 17.67 31.38 3.286 0.2501 0.0352 4.75 0.3319
LSTM_1 53.47 7.32 16.22 22.50 2.135 0.4513 0.1468 50.26 0.5163
LSTM_2 52.15 7.16 13.8218.38 1.8970.5181 0.2018 76.31 0.5696
TRANSFORMERS 52.76 7.23 16.34 22.95 2.135 0.4425 0.1394 47.29 0.5090
2020–2026: COVID + Rate Hike Cycle
Buy & Hold 47.37 7.66 23.91 38.95 2.175 0.3204 0.0630 22.18 0.4256
Equal-Weight Monthly 45.36 7.43 20.68 39.40 1.163 0.3593 0.0678 43.26 0.4443
Markowitz Min Var 39.08 6.6018.5936.240.7260.3550 0.0647 58.82 0.4286
Momentum Top-20 0.61 0.24 20.38 35.27 1.663 0.0118 0.0001 0.00 0.1080
LSTM_1 46.08 7.53 18.56 33.52 1.048 0.4057 0.0911 65.40 0.4775
LSTM_2 41.60 6.87 15.6629.941.060 0.43870.1007 65.37 0.4967
TRANSFORMERS46.60 7.6018.55 33.16 1.0480.40970.0939 68.05 0.4813
Note:Sub-period performance metrics for EURO STOXX 50 strategies across three macroeconomic regimes. Buy & Hold is
the SPDR Euro Stoxx 50 ETF (FEZ). Strategy labels refer to the following configurations — LSTM_1: LSTM encoder, flat
Dirichlet policy, log-return reward, cash allowed; LSTM_2: LSTM encoder, hierarchical policy, log-return reward, cash allowed;
TRANSFORMERS: Transformer encoder, flat Dirichlet policy, log-return reward, cash allowed. AR denotes total cumulative
return over the sub-period; ARC denotes annualized compounded return. IR2 is the primary risk-adjusted evaluation metric.
Bold denotes the best value per metric within each period.
55

8. Ensemble Total Fund
The ensemble framework evaluates whether combining strategy signals across multiple equity
markets leads to improved portfolio performance. Cross-asset portfolios are constructed by aggre-
gating out-of-sample daily returns from the NASDAQ-100, Nikkei 225, and EURO STOXX 50 for
each reinforcement learning configuration using equal weights. All return series are aligned on a
common date index and evaluated over the same out-of-sample period commencing 2009-04-06. The
benchmark corresponds to the cross-sectional average of the Buy & Hold strategies across the three
markets.
Figure 11 presents the corresponding equity curves, expressed as the growth of one unit of
capital. All reinforcement learning strategies exhibit broadly similar long-term trajectories, with
LSTM_1 delivering the strongest absolute growth. Table 15 reports the corresponding performance
metrics. Based on the IR2 criterion, LSTM_1 achieves the highest risk-adjusted performance (IR2 =
0.41), outperforming both the benchmark (IR2 = 0.34) and all alternative configurations. LSTM_2
achieves the lowest volatility and maximum drawdown among all strategies, reflecting superior risk
control, though its lower absolute return results in a slightly lower IR2. The Transformer model
delivers competitive risk-adjusted performance with low volatility, while the NC configurations
closely track the benchmark.
Figure 11: Equity curves for cross-asset ensemble portfolios across reinforcement learning strategies.
1
2
3
4
5
6
2010 2015 2020 2025
Date
Equity
Buy&Hold
LSTM_1
LSTM_2
LSTM_NC_1
LSTM_NC_2
TRANSFORMERS
Note:The figure presents the out-of-sample equity curves of cross-asset portfolios constructed as equal-weight combinations of
strategy-specific returns across the NASDAQ-100, Nikkei 225, and EURO STOXX 50. Strategy labels refer to the following
configurations — LSTM_1: LSTM encoder, flat Dirichlet policy, log-return reward, cash allowed; LSTM_2: LSTM encoder, hi-
erarchical policy, log-return reward, cash allowed; LSTM_NC_1: LSTM encoder, flat Dirichlet policy, benchmark-relative reward,
fully invested; LSTM_NC_2: LSTM encoder, flat Dirichlet policy, benchmark-relative reward, fully invested; TRANSFORMERS:
Transformer encoder, flat Dirichlet policy, log-return reward, cash allowed. The benchmark represents the cross-sectional average
of the Buy & Hold strategies across the three markets. All series are aligned on a common date index and expressed as the
growth of one unit of capital.
56

Table 15: Performance Metrics for Ensemble Strategies
Strategy AR (%) ARC (%) ASD (%) MD (%) MLD IR1 IR2 IR3 Sharpe
Common Benchmark 486.79 12.68 16.53 28.631.700.7671 0.3397 2.53 0.8055
LSTM_1514.60 13.0314.72 28.16 1.79 0.88520.4096 2.98 0.9062
LSTM_2 390.49 11.3312.75 25.461.750.88860.3954 2.55 0.9054
LSTM_NC_1 487.84 12.69 16.14 28.76 1.98 0.7862 0.3469 2.23 0.8218
LSTM_NC_2 483.44 12.64 15.76 28.77 1.79 0.8020 0.3524 2.49 0.8342
TRANSFORMERS 451.32 12.21 14.77 27.92 1.77 0.8267 0.3615 2.49 0.8541
Note:The table reports out-of-sample performance metrics for cross-asset ensemble portfolios constructed as equal-weight
combinations of strategy-specific returns across the NASDAQ-100, Nikkei 225, and EURO STOXX 50. Strategy labels refer
to the following configurations — LSTM_1: LSTM encoder, flat Dirichlet policy, log-return reward, cash allowed; LSTM_2:
LSTM encoder, hierarchical policy, log-return reward, cash allowed; LSTM_NC_1: LSTM encoder, flat Dirichlet policy,
benchmark-relative reward, fully invested; LSTM_NC_2: LSTM encoder, flat Dirichlet policy, benchmark-relative reward, fully
invested; TRANSFORMERS: Transformer encoder, flat Dirichlet policy, log-return reward, cash allowed. The benchmark
corresponds to the cross-sectional average of the Buy & Hold strategies across the three markets. AR denotes total cumulative
return over the full evaluation period; ARC denotes annualized compounded return and is the primary return criterion. IR2 is
the primary risk-adjusted evaluation metric. All reported results are rounded to four significant figures.
To assess statistical significance, we apply the same HAC-adjusted tests and stationary bootstrap
inference as described in Section 6.4. The results indicate that none of the ensemble strategies
achieve statistically significant outperformance relative to the benchmark in terms of mean returns
or risk-adjusted measures.
Regression-based analysis, however, provides partial evidence of abnormal performance. In
particular, theLSTM_1andLSTM_2ensemble strategies exhibit positive and statistically
significant intercepts at the 10% level, with HAC-adjusted p-values of0.0496and0.0481, respectively,
while no significance is observed for the remaining strategies.
Overall, while the ensemble framework improves performance metrics in economic terms, the
statistical evidence for outperformance remains limited. The results should therefore be interpreted as
indicative rather than conclusive. The corresponding statistical results are summarized in Table 16.
57

Table 16: Statistical significance results for ensemble strategies
Model Mean Diff. HAC p-val∆Sharpe p-val∆IR2 p-val
Panel A: HAC and Bootstrap Tests
LSTM_1 0.0000 0.4933 0.1007 0.1898 0.0705 0.2537
LSTM_2 -0.0001 0.8320 0.0999 0.1788 0.0553 0.2458
LSTM_NC_DAILY -0.0000 0.5098 0.0163 0.4665 0.0069 0.4925
LSTM_NC_DAILY_2 -0.0000 0.5341 0.0287 0.4156 0.0119 0.4605
TRANSFORMERS -0.0000 0.6531 0.0486 0.3407 0.0217 0.4026
Panel B: Regression (HAC-adjusted)
ModelαSE(α)t α pα
LSTM_1 0.0001 0.0001 1.650.0496
LSTM_2 0.0001 0.0001 1.660.0481
LSTM_NC_DAILY 0.0001 0.0001 0.99 0.1605
LSTM_NC_DAILY_2 0.0001 0.0001 1.06 0.1451
TRANSFORMERS 0.0001 0.0001 1.21 0.1125
Note:Panel A reports Newey–West HAC-adjusted p-values for mean return differences and stationary bootstrap p-values
for Sharpe and IR2 differences. Panel B reports regression-based abnormal returns (α) with HAC-adjusted standard errors.
Statistical significance at the 10% level is indicated in bold.
9. Discussion
The objective of this study was to evaluate whether reinforcement learning based portfolio
allocation strategies can improve risk-adjusted performance under realistic market conditions.
The proposed framework combines SAC-based agents with different architectural and economic
configurations, evaluated through a walk-forward optimization procedure against four benchmarks
mentioned in Section 5.9: Buy & Hold, Equal-Weight Monthly, Markowitz Minimum Variance, and
Momentum Top-20.
The empirical results, reported in Tables 7, 8, and 9, indicate that reinforcement learning strategy
effectiveness varies significantly across markets. The strongest results are observed for the EURO
STOXX 50, where all RL strategies outperform the Buy & Hold benchmark in terms of IR2. In
contrast, for the NASDAQ-100 and Nikkei 225, passive and classical benchmarks remain competitive
or dominant. Notably, the Equal-Weight Monthly and Markowitz Minimum Variance portfolios
prove difficult to outperform across multiple markets and regimes, consistent with the findings of
58

DeMiguel et al. (2009).
At the aggregate level, the ensemble results in Table 15 demonstrate that combining strategies
across markets leads to improved stability and superior risk-adjusted performance relative to the
benchmark. The LSTM_1 ensemble achieves the highest IR2 (0.41), outperforming the common
benchmark (0.34), highlighting the benefits of cross-market diversification.
The results provide partial support for the central hypothesis. While reinforcement learning
strategies achieve meaningful performance in certain settings, particularly in the EURO STOXX 50
and in the ensemble framework, they do not consistently outperform passive or classical benchmarks
across all markets. The regime analysis presented in Section 7 further reveals that RL strategies
tend to add the most value during periods of elevated uncertainty and lower trend persistence, while
passive benchmarks dominate in strongly trending markets such as the NASDAQ-100.
Statistical inference further limits the strength of these conclusions. As shown in Table 10, none
of the strategies achieve statistically significant excess returns relative to the Buy & Hold benchmark
based on HAC-adjusted tests and stationary bootstrap inference. However, the regression results
in Table 11 indicate that LSTM_1, LSTM_2, and the Transformer model exhibit statistically
significant positive intercepts in the EURO STOXX 50, suggesting the presence of abnormal returns
in this specific market.
RQ1. How does the choice of reward formulation (absolute vs. benchmark-relative)
affect the performance and stability of learned strategies?
The results indicate that reward formulation has a limited impact on performance. Benchmark-
relative models (LSTM_NC) do not consistently outperform absolute-return models across markets.
In the NASDAQ-100, LSTM_2 achieves a higher IR2 than LSTM_NC_2 despite using an absolute
reward, and a similar pattern holds in the EURO STOXX 50. The experimental configurations were
not designed as ceteris paribus experiments, however, as reward formulation co-varies with portfolio
constraints across configurations. Consequently, this finding should be interpreted as exploratory
rather than causal.
RQ2. What is the impact of different policy structures (flat vs. hierarchical allocation)
on portfolio performance and diversification?
The hierarchical policy structure consistently improves risk-adjusted performance. LSTM_2, which
employs a hierarchical Dirichlet policy separating the equity-cash allocation decision from individual
asset selection, achieves lower volatility and lower maximum drawdown than LSTM_1 across all
three markets. This suggests that decomposing the allocation decision into sequential stages improves
59

portfolio stability, though the same confounding caveat noted for RQ1 applies here.
RQ3. How do portfolio constraints (fully invested vs. flexible exposure) influence
trading behavior and risk-adjusted returns?
Portfolio constraints substantially affect risk-adjusted performance. Cash-allowed configurations
consistently achieve lower drawdowns and higher IR2 than their fully invested counterparts, at the
cost of somewhat lower absolute returns. This pattern is most visible in the NASDAQ-100, where
LSTM_NC_1 attains the highest absolute return among all RL strategies yet its IR2 falls well
below that of the cash-allowed LSTM_2. These results suggest that the ability to hold cash provides
meaningful downside protection, particularly during volatile market conditions.
RQ4. Does the inclusion of different temporal encoders (LSTM vs. Transformer)
improve the model’s ability to capture market dynamics and enhance performance?
LSTM-based models outperform the Transformer in risk-adjusted terms across all three markets.
While the Transformer delivers competitive absolute returns and achieves the highest AR on the
EURO STOXX 50, it does not consistently improve stability relative to LSTM-based configurations.
RQ5. Does combining strategy-specific signals across multiple markets through an
ensemble approach improve risk-adjusted performance compared to single-market
strategies and the benchmark?
The ensemble approach consistently improves risk-adjusted performance relative to individual market
strategies. All ensemble configurations outperform the common benchmark on IR2, with LSTM_1
achieving the strongest result. Volatility and maximum drawdown are also reduced relative to
single-market deployments, confirming that geographic diversification across the NASDAQ-100,
Nikkei 225, and EURO STOXX 50 provides meaningful risk reduction benefits.
RQ6. Does the performance of reinforcement learning strategies vary systematically
across macroeconomic regimes, and in which market environments do RL strategies
add the most value?
The regime analysis presented in Section 7 reveals substantial heterogeneity in strategy performance
across macroeconomic periods. On the NASDAQ-100, RL strategies outperform Buy & Hold only
during the post-GFC recovery (2009–2013), with passive benchmarks dominating in the subsequent
bull market and COVID-era periods. On the Nikkei 225, RL strategies and classical benchmarks
consistently outperform the weak Buy & Hold index exposure, with LSTM_2 leading across all
strategies in 2014–2019. On the EURO STOXX 50, RL strategies deliver consistent risk-adjusted
outperformance over Buy & Hold across all three regimes, though classical benchmarks remain
60

competitive. Overall, RL strategies appear to add the most value in markets characterized by lower
trend persistence and greater structural uncertainty, while their advantage diminishes in strongly
trending environments where passive strategies are most effective.
The difficulty of outperforming passive and classical benchmarks across all markets and regimes
is consistent with the findings of DeMiguel et al. (2009), who demonstrate that even sophisticated
optimization models struggle to systematically beat naive equal-weight allocation out-of-sample.
The ensemble results further reinforce the importance of diversification as a primary mechanism for
improving risk-adjusted performance within the proposed framework.
10. Conclusions
This study develops and evaluates a unified deep reinforcement learning framework for dynamic
portfolio allocation across three major global equity markets: the NASDAQ-100, Nikkei 225, and
EURO STOXX 50. The framework combines the Soft Actor–Critic algorithm with a structured
walk-forward optimization procedure, realistic market frictions, and a systematic comparison of
architectural and economic design choices. The empirical analysis covers the period from 2009
to 2026 and benchmarks the proposed strategies against four reference portfolios: Buy & Hold,
Equal-Weight Monthly, Markowitz Minimum Variance, and Momentum Top-20.
The empirical results demonstrate that reinforcement learning strategies achieve competitive
risk-adjusted performance in several settings, most notably in the EURO STOXX 50, where all RL
configurations outperform the Buy & Hold benchmark on IR2, and in the ensemble framework,
where LSTM_1 achieves an IR2 of 0.41 against the common benchmark of 0.34. However, the
hypothesis is only partially confirmed: RL strategies do not consistently outperform passive or
classical benchmarks across all markets, and none of the strategies achieve statistically significant
excess returns relative to Buy & Hold based on HAC-adjusted inference. The regime analysis further
reveals that RL strategies add the most value during periods of elevated uncertainty and lower
trend persistence, while passive benchmarks dominate in strongly trending environments such as the
NASDAQ-100 during 2014–2019.
This study makes several contributions to the existing literature on deep reinforcement learning
for portfolio management. First, it provides a unified multi-market evaluation framework that applies
identical walk-forward optimization, adaptive retraining, and performance assessment procedures
across three economically distinct equity markets, enabling direct cross-market comparison an aspect
largely absent from prior work focused on single-market settings (Yang et al., 2020, Jiang et al.,
61

2024). Second, it introduces a hierarchical Dirichlet policy structure that separates the equity-cash
allocation decision from individual asset selection, providing a principled mechanism for dynamic cash
management within the SAC framework that extends flat policy architectures used in related studies
(Hambly et al., 2023). Third, it proposes an adaptive retraining criterion based on rolling validation
Sharpe ratios that selectively updates the model only when performance deteriorates, reducing
computational cost while maintaining deployment realism a mechanism not present in standard WFO
implementations in the literature. Fourth, it conducts a systematic regime decomposition across three
macroeconomic periods, providing empirical evidence on the conditions under which reinforcement
learning allocation adds value relative to passive and classical benchmarks, contributing to the
broader debate on the regime-dependence of active portfolio management (DeMiguel et al., 2009).
Despite these contributions, several limitations must be acknowledged. First, none of the
reinforcement learning strategies achieve statistically significant outperformance relative to the Buy
& Hold benchmark in two out of three markets, indicating that the observed performance differences
may reflect random variation rather than systematic excess returns. Second, the experimental
configurations were not designed as ceteris paribus ablation studies, as each configuration varies
simultaneously across multiple dimensions including encoder type, reward formulation, and portfolio
constraints. Consequently, the answers to RQ1–RQ4 should be interpreted as exploratory rather than
causal. Third, the transaction cost assumption of 2 basis points was held fixed throughout training
and evaluation; strategies were not retrained under higher cost assumptions, and their robustness
to more realistic cost levels remains an open question. Fourth, the walk-forward architecture itself
including the choice of training window, validation period, and retraining threshold was not subject
to systematic sensitivity analysis, introducing the risk of meta-overfitting as noted by Bailey et al.
(2017). Fifth, the ensemble aggregation employs fixed equal weights across markets, which may
not reflect optimal cross-market allocation and limits the adaptability of the ensemble to changing
market conditions.
Several directions emerge naturally from this work. The most immediate extension concerns
the application of the framework to higher-frequency data and alternative asset classes, including
cryptocurrency markets, where microstructure dynamics, liquidity constraints, and volatility regimes
differ substantially from traditional equities. High-frequency environments also introduce the oppor-
tunity to evaluate intraday allocation policies under more granular transaction cost models. A second
direction concerns the enrichment of the state representation through the integration of macroe-
conomic variables such as yield curve dynamics, credit spreads, and purchasing managers indices
62

alongside sentiment signals derived from financial news using large language model embeddings. Such
representations could provide the agent with a richer characterization of the macroeconomic regime,
potentially improving performance during structural breaks and crisis periods where price-based fea-
tures alone may be insufficient. A third direction involves replacing the fixed equal-weight ensemble
with a meta-level adaptive aggregation mechanism, where cross-market portfolio weights are learned
dynamically based on recent strategy performance and prevailing market conditions. Finally, future
work could address the ablation limitation noted above by designing a dedicated ceteris paribus
experimental framework in which a single architectural or economic dimension is varied at a time,
enabling cleaner attribution of performance differences to individual model components.
References
D. H. Bailey, J. M. Borwein, M. López de Prado, and Q. J. Zhu. The probability of backtest
overfitting.The Journal of Computational Finance, 20(4):39–69, 2017. ISSN 1460-1559. doi:
10.21314/JCF.2016.322.
B. Bieganowski and R. Ślepaczuk. Supervised autoencoder MLP for financial time series forecasting.
Journal of Big Data, 12(1):207, 2025. ISSN 2196-1115. doi: 10.1186/s40537-025-01267-7.
F. Black and R. Litterman. Global portfolio optimization.Financial Analysts Journal, 48(5):28–43,
1992. ISSN 0015-198X. doi: 10.2469/faj.v48.n5.28.
Z. Bracha, P. Sakowski, and J. Michańków. Application of deep reinforcement learning to at-the-
money S&P 500 options hedging.arXiv preprint arXiv:2510.09247, 2025. doi: 10.48550/arXiv.2
510.09247.
H. Buehler, L. Gonon, J. Teichmann, and B. Wood. Deep hedging.Quantitative Finance, 19(8):
1271–1291, 2019. ISSN 1469-7688. doi: 10.1080/14697688.2019.1571683.
Q. Bui and R. Ślepaczuk. Applying Hurst exponent in pair trading strategies on Nasdaq 100 index.
Physica A: Statistical Mechanics and its Applications, 592:126784, 2022. ISSN 0378-4371. doi:
10.1016/j.physa.2021.126784.
S. M. Carta, S. Consoli, L. Piras, A. S. Podda, and D. R. Recupero. Explainable machine learning
exploiting news and domain-specific lexicon for stock market forecasting.IEEE Access, 9:30193–
30205, 2021. ISSN 2169-3536. doi: 10.1109/ACCESS.2021.3059960.
A. Chaweewanchon and R. Chaysiri. Markowitz mean-variance portfolio optimization with predictive
63

stock selection using machine learning.International Journal of Financial Studies, 10(3):64, 2022.
ISSN 2227-7072. doi: 10.3390/ijfs10030064.
L.-C. Cheng and J.-S. Sun. Multiagent-based deep reinforcement learning framework for multi-asset
adaptive trading and portfolio management.Neurocomputing, 594:127800, 2024. ISSN 0925-2312.
doi: 10.1016/j.neucom.2024.127800.
V. DeMiguel, L. Garlappi, and R. Uppal. Optimal versus naive diversification: How inefficient is the
1/N portfolio strategy?The Review of Financial Studies, 22(5):1915–1953, 2009. ISSN 0893-9454.
doi: 10.1093/rfs/hhm075.
Y. Deng, F. Bao, Y. Kong, Z. Ren, and Q. Dai. Deep direct reinforcement learning for financial
signal representation and trading.IEEE Transactions on Neural Networks and Learning Systems,
28(3):653–664, 2017. ISSN 2162-237X. doi: 10.1109/TNNLS.2016.2522401.
J. Du, M. Jin, P. N. Kolm, G. Ritter, Y. Wang, and B. Zhang. Deep reinforcement learning for
option replication and hedging.The Journal of Financial Data Science, 2(4):44–57, 2020. ISSN
2640-3943. doi: 10.3905/jfds.2020.1.045.
B. Enkhsaikhan and O. Jo. Risk-constrained reinforcement learning with augmented Lagrangian
multiplier for portfolio optimization.IEEE Transactions on Big Data, 11(5):2489–2502, 2025.
ISSN 2332-7790. doi: 10.1109/TBDATA.2025.3533905.
T. Fischer and C. Krauss. Deep learning with long short-term memory networks for financial market
predictions.European Journal of Operational Research, 270(2):654–669, 2018. ISSN 0377-2217.
doi: 10.1016/j.ejor.2017.11.054.
J. Grudniewicz and R. Ślepaczuk. Application of machine learning in algorithmic investment
strategies on global stock markets.Research in International Business and Finance, 66:102052,
2023. ISSN 0275-5319. doi: 10.1016/j.ribaf.2023.102052.
T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine. Soft actor-critic: Off-policy maximum entropy deep
reinforcement learning with a stochastic actor. InProceedings of the 35th International Conference
on Machine Learning, volume 80 ofProceedings of Machine Learning Research, pages 1861–1870.
PMLR, 2018.
B. Hambly, R. Xu, and H. Yang. Recent advances in reinforcement learning in finance.Mathematical
Finance, 33(3):437–503, 2023. ISSN 0960-1627. doi: 10.1111/mafi.12382.
Z. Hao, H. Zhang, and Y. Zhang. Stock portfolio management by using fuzzy ensemble deep
reinforcement learning algorithm.Journal of Risk and Financial Management, 16(3):201, 2023.
64

ISSN 1911-8074. doi: 10.3390/jrfm16030201.
Y. Jiang, J. Olmo, and M. Atwi. Deep reinforcement learning for portfolio selection.Global Finance
Journal, 62:101016, 2024. ISSN 1044-0283. doi: 10.1016/j.gfj.2024.101016.
T. Kabbani and E. Duman. Deep reinforcement learning approach for trading automation in the stock
market.IEEE Access, 10:93564–93574, 2022. ISSN 2169-3536. doi: 10.1109/ACCESS.2022.3203697.
M. R. Kabir, D. Bhadra, M. Ridoy, and M. Milanova. LSTM–Transformer-based robust hybrid
deep learning model for financial time series forecasting.Sci, 7(1):7, 2025. ISSN 2413-4155. doi:
10.3390/sci7010007.
K.Kashif andR.Ślepaczuk. LSTM-ARIMAas ahybridapproachinalgorithmicinvestment strategies.
Knowledge-Based Systems, 320:113563, 2025. ISSN 0950-7051. doi: 10.1016/j.knosys.2025.113563.
L. Khaidem, S. Saha, and S. R. Dey. Predicting the direction of stock market prices using random
forest.arXiv preprint arXiv:1605.00003, 2016. doi: 10.48550/arXiv.1605.00003.
K.-j. Kim. Financial time series forecasting using support vector machines.Neurocomputing, 55
(1–2):307–319, 2003. ISSN 0925-2312. doi: 10.1016/S0925-2312(03)00372-2.
K. Krynska and R. Ślepaczuk. Daily and intraday application of various architectures of the LSTM
model in algorithmic investment strategies on Bitcoin and the S&P 500 index.SSRN Electronic
Journal, 2023. doi: 10.2139/ssrn.4628806. Available at SSRN: 4628806.
Y.-F. Lin, T.-M. Huang, W.-H. Chung, and Y.-L. Ueng. Forecasting fluctuations in the financial
index using a recurrent neural network based on price features.IEEE Transactions on Emerging
Topics in Computational Intelligence, 5(5):780–791, 2021. ISSN 2471-285X. doi: 10.1109/TETCI.
2020.2971218.
X.-Y. Liu, J. Rui, J. Gao, L. Yang, H. Yang, Z. Wang, C. D. Wang, and J. Guo. FinRL-Meta:
A universe of near-real market environments for data-driven deep reinforcement learning in
quantitative finance.arXiv preprint arXiv:2112.06753, 2021. doi: 10.48550/arXiv.2112.06753.
M. López de Prado. The 10 reasons most machine learning funds fail.The Journal of Portfolio
Management, 44(6):120–133, 2018. ISSN 0095-4918. doi: 10.3905/jpm.2018.44.6.120.
M. López de Prado, J. Simonian, F. A. Fabozzi, and F. J. Fabozzi. Enhancing Markowitz’s portfolio
selection paradigm with machine learning.Annals of Operations Research, 346(1):319–340, 2025.
ISSN 0254-5330. doi: 10.1007/s10479-024-06257-1.
D. Maringer and T. Ramtohul. Regime-switching recurrent reinforcement learning for investment
decision making.Computational Management Science, 9(1):89–107, 2012. ISSN 1619-697X. doi:
65

10.1007/s10287-011-0131-1.
H. Markowitz. Portfolio selection.The Journal of Finance, 7(1):77–91, 1952. ISSN 0022-1082. doi:
10.1111/j.1540-6261.1952.tb01525.x.
J. Michańków, P. Sakowski, and R. Ślepaczuk. LSTM in algorithmic investment strategies on BTC
and S&P500 index.Sensors, 22(3):917, 2022. ISSN 1424-8220. doi: 10.3390/s22030917.
A. Millea. Hierarchical model-based deep reinforcement learning for single-asset trading.Analytics,
2(3):560–576, 2023. ISSN 2813-2203. doi: 10.3390/analytics2030031.
V. Mnih, K. Kavukcuoglu, D. Silver, A. A. Rusu, J. Veness, M. G. Bellemare, A. Graves, M. Ried-
miller, A. K. Fidjeland, G. Ostrovski, et al. Human-level control through deep reinforcement
learning.Nature, 518(7540):529–533, 2015. ISSN 0028-0836. doi: 10.1038/nature14236.
J. Moody and M. Saffell. Learning to trade via direct reinforcement.IEEE Transactions on Neural
Networks, 12(4):875–889, 2001. ISSN 1045-9227. doi: 10.1109/72.935097.
W. K. Newey and K. D. West. A simple, positive semi-definite, heteroskedasticity and autocorrelation
consistent covariance matrix.Econometrica, 55(3):703–708, 1987. ISSN 0012-9682. doi: 10.2307/
1913610.
D. N. Politis and J. P. Romano. The stationary bootstrap.Journal of the American Statistical
Association, 89(428):1303–1313, 1994. ISSN 0162-1459. doi: 10.1080/01621459.1994.10476870.
I. Rani, H. Gandhi, R. Kumar, N. Marannan, N. K. Kim, and T. Kumar. Deep reinforcement learning
for high-frequency trading with market impact modeling. In2025 International Conference on
Sustainability, Innovation & Technology (ICSIT), pages 1–6. IEEE, 2025. doi: 10.1109/ICSIT653
36.2025.11293906.
J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov. Proximal policy optimization
algorithms.arXiv preprint arXiv:1707.06347, 2017. doi: 10.48550/arXiv.1707.06347.
A. Shavandi and M. Khedmati. A multi-agent deep reinforcement learning framework for algorithmic
trading in financial markets.Expert Systems with Applications, 208:118124, 2022. ISSN 0957-4174.
doi: 10.1016/j.eswa.2022.118124.
D. Ślusarczyk and R. Ślepaczuk. Optimal Markowitz portfolio using returns forecasted with time
series and machine learning models.Journal of Big Data, 12(1):127, 2025. ISSN 2196-1115. doi:
10.1186/s40537-025-01164-z.
F. Soleymani and E. Paquet. Financial portfolio optimization with online deep reinforcement learning
and restricted stacked autoencoder—DeepBreath.Expert Systems with Applications, 156:113456,
66

2020. ISSN 0957-4174. doi: 10.1016/j.eswa.2020.113456.
F. Stefaniuk and R. Ślepaczuk. Informer in algorithmic investment strategies on high frequency
bitcoin data.arXiv preprint arXiv:2503.18096, 2025. doi: 10.48550/arXiv.2503.18096.
H. J. Sterling and M. V. Thorne. Deep reinforcement learning for dynamic portfolio optimization in
financial markets.International Journal of Artificial Intelligence Research, 1(1), 2026.
A. Tamuly, G. Bhutani, and Sukriti. Portfolio optimization using deep reinforcement learning. In
2024 IEEE 5th India Council International Subsections Conference (INDISCON), pages 1–6,
Piscataway, NJ, USA, 2024. IEEE. doi: 10.1109/INDISCON62179.2024.10744403.
X. Wu, H. Chen, J. Wang, L. Troiano, V. Loia, and H. Fujita. Adaptive stock trading strategies with
deep reinforcement learning methods.Information Sciences, 538:142–158, 2020. ISSN 0020-0255.
doi: 10.1016/j.ins.2020.05.066.
H. Yang, X.-Y. Liu, S. Zhong, and A. Walid. Deep reinforcement learning for automated stock
trading: An ensemble strategy. InProceedings of the First ACM International Conference on
AI in Finance (ICAIF ’20), pages 1–8, New York, NY, USA, 2020. Association for Computing
Machinery. doi: 10.1145/3383455.3422540.
H. Zhang, X. Li, T. Wan, and J. Du. Deep reinforcement learning for financial trading: Enhanced
by cluster embedding and zero-shot prediction.Symmetry, 18(1):112, 2026. ISSN 2073-8994. doi:
10.3390/sym18010112.
67
