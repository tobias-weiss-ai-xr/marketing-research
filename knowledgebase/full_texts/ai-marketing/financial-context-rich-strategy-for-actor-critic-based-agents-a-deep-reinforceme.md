---
title: 'Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach
  for Stock Trading'
url: https://arxiv.org/abs/2610.32237
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Hrishikesh Singh
- Aarti Sharma
- Millie Pant
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.32237
pages: 10
chars: 44376
fetched_at: '2026-11-08T13:35:35+00:00'
kb_version: 1
---

# Financial Context-Rich Strategy for Actor-Critic based Agents: A Deep Reinforcement Learning Approach for Stock Trading

PREPRINT
Financial Context-Rich Strategy for Actor-Critic based Agents: A
Deep Reinforcement Learning Approach for Stock Trading
Hrishikesh Singh⋆
Department of Applied Mathematics
& Scientific Computing, Indian
Institute of Technology Roorkee
Roorkee, India
Aarti Sharma⋆
Department of Applied Mathematics
& Scientific Computing, Indian
Institute of Technology Roorkee
Roorkee, India
Millie Pant
Department of Applied Mathematics
& Scientific Computing, Indian
Institute of Technology Roorkee
Roorkee, India
pant.milli@as.iitr.ac.in
ABSTRACT
In modern financial markets, more than 3/4𝑡ℎ of the large volume
trade is executed by algorithmic trading based on advanced trad-
ing strategies to attain higher precision and speed than traditional
human traders. The conventional strategies focused on price-based
indicators are inadequate in capturing the market dynamism arising
from real-world events such as social sentiments, political instabil-
ity, or sudden economic shifts. With the rise ofDeep Reinforcement
Learning(DRL) and data availability, there is a requirement for
more efficient algorithms that can incorporate these external fac-
tors in trading strategies. DRL has shown potential in simulating
real-world scenarios and in simplifying complex decision-making
since DRL agents can automate the trading processi.e.executing
trades in a manner comparable to human traders. They have shown
reliable performance since they can update their policies based on
risk and quantitative factors. In this paper, we propose a DRL ap-
proach based on partial and deep-infusion of sentimental analysis.
It features distinct policy designs ofactor-critic-basedagents: only
policy optimization (A2C&PPO) and policy optimization along
with Q-learning principles (DDPG, TD3&SAC). Our findings re-
veal, that the agents based on policy optimization combined with
Q-learning, significantly and consistently demonstrate improved
performance upon sentiment deep-infusion in profit maximization
as well as risk-averse trading.
CCS CONCEPTS
•Computing methodologies → Reinforcement learning;Nat-
ural language processing;•Applied computing→Economics.
KEYWORDS
Deep Reinforcement Learning, Algorithmic Trading, Finance, Sen-
timent Analysis
1 INTRODUCTION
In 2024, India will remain the world’s fastest-growing major econ-
omy. According to the World Bank’s GDP ranking 2024 list India is
the 5th largest economy, inevitably with rapid development, an in-
crease in social media usage, the spread of the digital economy, and
financial literacy more and more retail investors are investing their
money in stock markets. Hence, the need to develop optimal trading
⋆Both authors contributed equally to this research.
In press. This paper received the Best Paper Award at BAMS-ORSI 2024, the Interna-
tional Conference on Emerging Trends in Business Analytics & Management Sciences
and 57th Annual Convention of the Operational Research Society of India (ORSI-2024).
strategies that are profitable and minimize risk is paramount. The
stock market is a dynamic and rapidly changing environment, and
many traditional trading strategies based on stochastic calculus,
numerical analysis, and quadratic programming[9] may prove to
be suboptimal since they fall short in utilizing all the dynamically
evolving relevant factors that influence the equities such as stocks.
Deep learning-based methods show potential in this scenario
since they are capable of extracting relevant features from huge
datasets. Supervised learning-based approaches to predict stock
prices mainly follow two steps, that is, forecasting and decision-
making[17]. But such strategies may lead to suboptimal perfor-
mance due to “forecasting bottleneck”. Reinforcement Learning (RL)
solves this problem since it is based on “learn by experience” method-
ology, whereas supervised learning is based on “learn by example”. It
shows excellent performance in stochastic environments such as the
stock market due to its ability to make sequential decisions[11, 22].
However, the bottleneck of reinforcement learning approaches
is its inefficiency in scaling with the huge amount of information
processing required for real-world scenarios. In this scenario, deep
reinforcement learning fits as a solution. Deep reinforcement learn-
ing (DRL) uses agents or robots to develop trading strategies in
complex scenarios involving numerous features. The agent mainly
works by either optimizing its policy or the value function. The
agents that we have used are mainly those that optimize policy and
those that optimize policy and value function.
The stock price movement is highly volatile and is not solely
based on quantitative features such as the performance metrics of
a company and the technical indicators. Many important scenarios
that impact the country’s fate such as elections, budget, etc. have
seen significant movement in stock prices. Thus, considering quan-
titative features only in stochastic decision-making processes is
painting only half a picture, it is necessary to include qualitative
features as well such as the sentiment value.
The main aim of our research is to build and validate automated
trading strategies using actor-critic DRL agents like A2C, PPO, TD3,
SAC, DDPG by incorporating sentiment analysis and thus improve
decision-making capabilities. In our paper, we have incorporated
the sentiment value in the representational state space as well
as in the reward calculations to see their impact on influencing
the agent’s behavior in developing trading strategies. Our main
contributions are as follows:
• A comprehensive evaluation of distinct DRL agents in fi-
nancial market conditions.
arXiv:2610.32237v1  [cs.AI]  23 Oct 2026

PREPRINT Singh, Sharma and Pant
• Integration of sentiment and analyzing its impact on the
trading performance of agents.
• Examining the impact of policy design variations on finan-
cial decision-making.
2 RELATED WORK
Stock market prediction has been of interest to researchers for an
extended time. The earlier studies utilized linear[2] and machine
learning techniques[18] to build predictive models. Over time vari-
ous evolved techniques such as artificial neural networks[21] were
employed to predict stock prices, options prices, exchange rates,
etc. Some techniques involved extracting qualitative information
using text mining to predict the stock prices[8, 16]. Several works
used natural language processing techniques to forecast financial
instrument movement[23].
In the deep learning landscape, the authors of [ 3] proposed a
modified CNN and time series analysis of financial data to build a
forecasting model for stock prices. In a similar vein, in [20] CNN is
used on stock chart images to develop a financial trading model. Re-
current neural networks show excellent performance on time series
data. They have also been employed in predictive stock trading, the
authors of [10] used a Bidirectional GRU network and compared
its performance with LSTM and GRU. Attention-based LSTM was
another method proposed for stock prediction [4].LSTM with opti-
mization algorithms is explored by the author of [6]. Reinforcement
learning has an advantage in simulating real-life trading scenarios
and faster and superior decision-making. There has been ongoing
research in this direction establishing the effectiveness of RL-based
models for stock prediction[11, 22]. Deep reinforcement learning
combines the feature extraction capabilities of deep learning with
real-world simulation and complex decision-making abilities of re-
inforcement learning. DRL-based models are capable of providing
useful insights as well as planning and developing complex trading
strategies[24].
The existing work establishes the effectiveness of deep learning-
based agents. Building upon this foundation we have further ex-
plored and compared the decision-making abilities of five distinct
DRL agents which have unique policy designs, in the same market
conditions. We further experimented with sentiment infusion, to
analyze the trading behavior of these agents upon providing more
context of the financial market.
3 DATASET
3.1 Stock Market Data
For the stock historical dataset, we selected 5 top Indian stocks by
market capitalization: Reliance, Adani, Bharti Airtel, HDFC and
ICICI, covering main financial sectors such as energy, telecommuni-
cation, banking. The main advantages of selecting stocks by market
capitalization are, stocks with larger market capitalization tend to
be more stable and less volatile compared to smaller-cap stocks.
Larger companies often have more comprehensive and accurate
financial data available. This can be advantageous for RL algorithms,
as high-quality data is crucial for training models and making
informed investment decisions. Large-cap stocks typically have a
significant influence on the overall market. By focusing on these
Company Market Capitalization Sector
(in Trillion INR)
Reliance 19.64 T Oil
Adani Ports 3.09 T Infrastructure/Ports
Bharti Airtel 9.44 T Telecommunications
HDFC Bank 12.53 T Banking
ICICI Bank 8.71 T Banking
Table 1: Market Capitalization & Domain of Selected Indian
Companies (Sept 2024)
stocks, RL models can align more closely with broader market
trends and indices.
The range of our financial dataset is 5.5 years from Jan 2019 to
June 2024. We obtained the historical data of the selected stocks
from Yahoo Finance. The features of historical stock data from
Yahoo Finance are:Date, Ticker, Open, High, Low, Close, Volume
&Day. We have also pre-processed out financial data by adding
technical indicators,CBOE Volatility Index(VIX) and turbulence.
The technical indicators are:Moving A verage Convergence Di-
vergence(MACD),Bollinger Bands, Relative Strength Index(RSI-30),
Commodity Channel Index(CCI-30),Directional Index(DX-30),30-
day Simple Moving A verage(Close 30 SMA),60-day Simple Moving
A verage(Close 60 SMA).
3.2 Financial News
We build the corresponding financial news dataset for the prior
selected stocks using Google’s RSS Feeds API. To obtain a broad
context and reporting for the stocks we collected multiple news
for the same stock at any given day among the timeline we had
decided earlier ( 5 years).
The multiple headlines for a particular day help us obtain a more
realistic average market sentiment for that day. On an average
for a particular day the number of headlines vary from 1 to 10.
The features of our financial news dataset are:Date, Ticker, News
HeadlineandSource.
3.3 Sentiment Score
After scraping the headlines, we did a sentiment analysis of these
headlines using FinBERT, (BERT for Financial Text Mining).
The authors of FinBERT[13], have used two financial corpuses to
further pre-train the BERT model. They used TRC2-financial which
consists of 46,143 documents with more than 29M words and nearly
400K sentences. The second dataset is Financial PhraseBank[ 14]
which consists of 4845 English sentences selected randomly from
financial news found on LexisNexis database.
FinBERT generates 3 normalized label scores for each headline
i.e. positive, negative and neutral where ‘positive’ label is encoded
as 1, ‘negative’ label as -1 and ‘neutral’ label as 0. We assigned the
label with the highest score to corresponding news.
For a single day we had up to 10 headlines. For each headline
we calculated the sentiment label and sentiment score. On the days
when the news headlines were not available through Google’s RSS

Financial Context-Rich DRL Strategy for Trading PREPRINT
Feed API, we assigned a sentiment score of 0 and sentiment label
as neutral.
Our final data with news headlines and sentiment analysis was of
dimension: (4843, 4) with standard features: Date, Ticker, Sentiment
Label and Sentiment Score.
From the sentiment score we obtained for each date we calculated
an inclination score in the following way:
Let s be a particular stock, d be a particular date. Let𝜂(𝑠,𝑑) denote
the news headline of a particular stock s on a date d. Since we have
gathered multiple news headlines for a stock s on a particular day,
d, we define𝜂𝑖(𝑠,𝑑) be the𝑖𝑡ℎ news headline for stocks s on date d,
where𝑖 ranges from 1 to N, where N denotes the total number of
articles on a particular date for a particular stock. For each𝜂𝑖(𝑠,𝑑)
we multiplied the sentiment score with {1, -1 or 0} depending on the
sentiment label to obtain an adjusted sentiment score ranging from
-1 to 1. Then we took the mean of the adjusted sentiment score to
obtain an inclination score. More formally:
𝜃=
˝𝑁
𝑖=1𝛼(𝜂𝑖(𝑠,𝑑))
𝑁 (1)
𝜃: Inclination score for news headlineifor stocksand dated
𝛼: Adjusted Sentiment Score for news headline i for stock s and
date d
𝑁: Total number of news headlines for a stock s on date d
3.4 Fusion
After obtaining the inclination score for each date for a stock we
merged these scores with the historical stock data. We merged these
two datasets on stock’s ticker symbol and date. The missing values
of inclination score for a particular stock and date in the merged
dataset were populated with a default value of 0 , thereby indicating
a neutral sentiment.
4 MODELING
To model this research problem, we have replicated the trading
activity in market structure onto agent and environment based
framework. The trading activity is primarily aMarkov Decision
Process(MDP), where an agent is an actor, taking the action by
interacting with the dynamic environment.
Every trading activity by the DRL model is a series of Markov
decisions. The Environment consists of the states, reward and meta-
data. The sequential decisions taken by the agents over a course
of action are represented as a list of states and the associated re-
wards with each step. By continuous feedback from the dynamically
changing environment, agents learn to trade better by policy opti-
mization, which is a component of agents.
4.1 Stock Market Structure
US stock market have two major exchange i.e. New York Stock
Exchange (NYSE) and NASDAQ. Similarly, Indian stock market also
have dual-exchange market structure i.e. National Stock Exchange
(NSE) and Bombay Stock Exchange (BSE).
These exchanges handle various kinds of instruments as a part
of their day-to-day trading. We will be focusing on stock trading
among these instruments.
Figure 1: NSE Schema
In a live trading scenario, there are two components working to-
gether i.e. Trader (Human) and the Stock Trading Setup (Orderbook,
Market Datafeed, Capital, etc.). A trader will analyze the market
using the inbound data feed to strategize their action for achieving
their objective. There are various aspects to the objective such as
risk appetite, capital, desired liquidity, stakeholder preference, etc.
so here the strategy is influenced by the financial experience of the
trader or portfolio manager combined with the derived knowledge
from the analysis of the incoming feed.
Our research will be localized between Order Book & Trading
and Market Data Feeds in the architecture diagram.
To model and simulate this real world setup we have replicated
the trading activity and a component of stock market architecture
relevant to our use case in the form of four major components:
Environment, State, RewardandAgent.
For a simpler analogy, the stock market architecture and data
such as the exchange in which we are trading, rules of engagement,
market conditions will be a part of the modeled environment. The
current scenario or snapshot of our position in the market at a
specific time will be calledStatei.e. price, portfolio composition,
values of technical indicators etc. Now theAgentassumes the role
of a trader and has similar options available as to a human trader.
WhilePolicyis analogous to the intuition or technical acumen of
a trader whereasRewardcan be assumed as the feedback for the
actions taken by the model.
Now we will explain the components of our modeling in follow-
ing sections:
4.2 State
A state describes the current conditions of an environment to an
agent. Based on these conditions an RL agent takes actions. States
in reinforcement learning follow Markov property which means
that given the current state the future must be independent of the
past. We have modeled our use case as aMarkov Decision Process.
The key aspect of MDP in RL is that decisions and rewards are
assumed to be dependent on the current state only. Hence, the state

PREPRINT Singh, Sharma and Pant
Figure 2: Trading based Reinforcement Learning Architecture
must contain all the information about the current conditions of
the environment. We have defined a finite state space. In our case
we have included these features in our state space: agent’s cash
balance, the current stock prices, number of shares held for each
stock, technical indicators, and inclination score derived from the
sentiment score and sentiment label for each stock. The need to
include sentiment data in state space is to let the agent take more
sentiment aware decisions. Since we have defined a Markov state
we can define the transition dynamics of our environment at time
steptas:
𝑃(𝜁𝑡+1,𝛼𝑡+1|𝜁𝑡,𝛼𝑡)(2)
Heresandtare state and action respectively at current time
steptand the next time step.t+1. The equation 2 describes the
probability of our environment to transition from a state 𝜁𝑡 and
action𝛼𝑡 to the next state𝜁𝑡+1 and action𝛼𝑡+1 . The probability to
transition from current state and action to the next state and action
is entirely dependent upon current state and action.
4.3 Environment
In reinforcement learning an environment encompasses state, ac-
tion and reward. Essentially, it is the environment with which an
RL agent interacts. Based on the state the agent takes actions and
rewards or penalties are provided by the environment for the action
taken. The transition dynamics for the environment as in equation 2
gives the probability distribution of transitioning to the next state
given the current state and action. In our use case equation 2, 3 and
7 define various aspects of our environment.
4.4 Reward
There are two ways we have calculated reward. In the case of stock
trading without sentiment, as well as the case where sentiment
incorporation is done only in the state, the reward is calculated as
follows:
Let us assume we are at time step 𝑡. At the beginning of each
time step, we calculate the asset value as𝛽(𝑡𝑠), which is the sum of
cash balance(𝑐) and the number of stocks held(𝑛). After the agent
performs certain actions, the asset value at the end of the time step
is calculated similarly as𝛽(𝑡𝑒). The final reward(𝛾) is obtained as
the change in the asset value from the beginning of the time step
to the end of the time step as follows:
𝛾=Δ(𝛽(𝑡))=𝛽(𝑡 𝑒)−𝛽(𝑡 𝑠)(3)
In another case, where we have incorporated the inclination
score in the reward calculation so that sentiment has a better influ-
ence on the agent’s actions, we have followed this strategy:
As in equation 3 above, first the asset change is calculated. Then
we compute the average individual reward. The calculation of the
average individual reward is done as follows:
Step 1:For a particular stock, calculate the difference between
the current price𝜌𝑡𝑖 and the price at the beginning of the time step
𝜌𝑡𝑖−1 :
Δ𝜌𝑡 =𝜌 𝑡𝑖−𝜌𝑡𝑖−1 (4)
Step 2:Calculate the individual reward 𝑟𝑠 for a particular stock
(𝑠) by multiplying the price difference with the inclination score
𝜃𝑖:
𝑟𝑠 =Δ(𝜌 𝑡)×𝜃 𝑖 (5)
After calculating the individual reward for each stock, we take
the mean of all individual rewards to obtain the average individual
reward:
𝑟avg =
˝
𝑠𝑟𝑠
𝑁 ,where𝑁is the number of stocks (6)

Financial Context-Rich DRL Strategy for Trading PREPRINT
The final reward is then calculated as:
𝛾=Δ(𝛽(𝑡))+𝑟 avg (7)
In both these cases, we have obtained various results, which are
documented in the experiment section.
4.5 Agent
In the case of stock trading, there are three actions available to the
agent i.e. buy, sell or hold. These actions result in creation of the
next state and based on the performance, a reward or penalty is
given to the agent.
Figure 3: Markov Decision Chain of Agent actions
Using this reward and state feedback, the agent aims to optimize
its policy to attain the objective faster and accurately. Policy can be
optimized by actor-critic methods directly or by using Q-learning
in continuous action spaces.
We have selected 5 advanced reinforcement learning agents
(Actor-Critic) to balance the exploration and exploitation in our
modeling environment. A2C and PPO are based on policy optimiza-
tion while DDPG, SAC and TD3 extend to use Q-learning too. The
characteristics and the workings are defined as follows:
Figure 4: Selected Algorithms
4.5.1 Advantage Actor-Critic (A2C).The actor-critic method is
based on policy gradient and primarily has two neural networks,
an actor and a critic. The actor determines the next action while
getting post-action feedback about their impact from the critic net-
work. This step is simplified further by employing an advantage
function which acts as an estimator by minimizing variance and
giving faster learning speed. The A2C is synchronous while A3C
is asynchronous[7]. In A3C the parallel update step reduces the
inter-dependence of actor-learner for one to finish before starting
the other process.
In our trading experiment, A2C intends to maximize profits by
improving its trading policy based on actor actions and feedback
from the critic.
Policy Gradient Update:
∇𝜔𝑈(𝜔)=𝐸 𝑥∼𝑝 𝜇
h
∇𝑏𝑅𝜇(𝑥,𝑏)

 𝑏=𝜇(𝑥)∇𝜔𝜇𝜔(𝑥) i (8)
Where∇𝜔𝑈(𝜔) represents the gradient of the expected return
𝑈 with respect to policy parameters𝜔.𝑅𝜇(𝑥,𝑏) is the action-value
function, estimating the expected return for taking action𝑏 in state
𝑥 and then following policy 𝜇.𝜇𝜔(𝑥) represents the policy[7], a
mapping from states to actions, parameterized by𝜔.
Advantage Function:
𝐴(𝑥,𝑏)=𝑅 𝜇(𝑥,𝑏)−𝑆 𝜇(𝑥)(9)
Where𝐴(𝑥,𝑏) is the advantage of taking action 𝑏 in state 𝑥.
𝑆𝜇(𝑥) is the state-value function[7], estimating the expected return
of starting in state𝑥and following policy𝜇.
4.5.2 Proximal Policy Optimization (PPO).This is an on-policy al-
gorithm which minimizes rapid policy changes to improve stability
by using clipped probability ratios in its objective function.
We have selected this agent algorithm[19] to avoid making sig-
nificant trade volume especially when market volatility is high.
The clipped surrogate probability function equips the algorithm
to evaluate the continuous action space and hence improves the
stability and mitigating the arbitrary trade risks.
Clipped Surrogate Objective:
𝜌𝑖(𝜃)= 𝜋𝜃(𝑏𝑖|𝑥𝑖) 𝜋𝜃𝑜𝑙𝑑(𝑏𝑖|𝑥𝑖) (10)
Where𝜌𝑖(𝜃) is the probability ratio of taking action𝑏𝑖 in state𝑥𝑖
under the current policy𝜋𝜃 compared to the old policy𝜋𝜃𝑜𝑙𝑑 .[19]
This ratio is then clipped:
clip(𝜌𝑖(𝜃),1−𝜖,1+𝜖)(11)
Where𝜖 is a hyperparameter limiting the policy update step
size.
4.5.3 Deep Deterministic Policy Gradient (DDPG).This is an off-
policy algorithm based on an actor-critic architecture but utilizes
deterministic policy gradient theorem[19]. Here the advantage is
generated by using a replay buffer which can store and sample
experiences requiring less data and smoother learning. Instead of
providing an action probability distribution, it simply suggests the

PREPRINT Singh, Sharma and Pant
exact action to take, hence the name “deterministic”. This algorithm
also works on continuous action space[7, 12].
Actor Update:
∇𝛼𝜈𝑈≈𝐸 𝑥∼𝜌 𝛽
h
∇𝑏𝑅(𝑥,𝑏|𝛼 𝑅)

𝑏=𝜈(𝑥|𝛼 𝜈)∇𝛼𝜈𝜈(𝑥|𝛼 𝜈)
i
(12)
Where∇𝛼𝜈𝑈 is the gradient of the expected return𝑈 with re-
spect to the actor[5] parameters𝛼𝜈.𝑅(𝑥,𝑏|𝛼 𝑅) represents the Q-
value, the expected return of taking action 𝑏 in state 𝑥, parame-
terized by𝛼𝑅.𝜈(𝑥|𝛼 𝜈) represents the deterministic policy, directly
mapping states to actions, parameterized by𝛼 𝜈.
Critic Update:
𝑅𝜇(𝑥,𝑏)=𝐸 [𝑟(𝑥,𝑏)+𝛾𝑅 𝜇(𝑥′,𝑏′)] (13)
Where𝑥′ is the next state.𝑏′ is the action taken in the next state
following the current policy.
4.5.4 Twin Delayed DDPG (TD3).In continuous action spaces, one
of the problems is overestimation bias in Q-learning. To solve this
problem, an enhancement in the DDPG algorithm led to TD3[5].
This algorithm proposed 3 additions: target policy smoothing, de-
layed policy update and clipped double Q-learning.
In our experiment, TD3 minimizes the trading risk originating
from overestimation bias and also reduces the variance. To attain
this objective, it uses 2 Q-networks and provides a conservative
action value by adopting a minimum of all predictions hence lower-
ing the risk even if the market volatility is unusually high because
of noisy data.
Target Value Update:
𝑧=𝑟+𝛾min
𝑖=1,2
𝑅𝛼′ 𝑖(𝑥′,𝜈𝛽′(𝑥′)+𝜁)(14)
𝜁∼clip(N(0,𝜎),−𝑐,𝑐)(15)
Where𝑧 is the target value.𝑅𝛼′ 𝑖(𝑥′,𝑎) represents the target Q-
values from two separate critics ( 𝑖= 1, 2).𝜈𝛽′(𝑥′) is the target
policy.𝜁 is the clipped noise term, sampled from a clipped normal
distribution, added to the target action[5].
4.5.5 Soft Actor-Critic (SAC).SAC is an off-policy algorithm based
on the actor-critic framework but with the concept of maximum
entropy reinforcement learning[7]. The conventional RL prioritizes
maximizing the expected return while SAC tweaks the policy to
prioritize exploration as well as maximizing the returns but this
improves the learning. So in non-standard Indian stock market con-
ditions, SAC will potentially be able to balance between exploiting
the working strategies as well as exploring novel trading strategies.
Maximum Entropy Objective:
𝜇∗ =arg max
𝜇
𝐸
"∞∑︁
𝑖=0
𝛾𝑖(𝑟(𝑥𝑖,𝑏𝑖)+𝛼𝐻(𝜇(·|𝑥 𝑖)))
#
(16)
Where𝜇∗ is the optimal policy.𝐻(𝜇(·|𝑥 𝑖)) represents the entropy
of the policy at state 𝑥𝑖.𝛼 is the temperature parameter control-
ling the balance between maximizing rewards and maximizing
entropy[7].
Soft Q-function:
𝑅𝜇(𝑥𝑖,𝑏𝑖)=𝑟(𝑥 𝑖,𝑏𝑖)+𝛾𝐸 𝑥′∼𝑝[𝑆𝜇(𝑥𝑖+1)] (17)
where𝑆 𝜇(𝑥𝑖+1)is the soft value function, defined as:
𝑆𝜇(𝑥𝑖+1)=𝐸 𝑥′∼𝑝,𝑏′∼𝜇[𝑅𝜇(𝑥𝑖+1,𝑏𝑖+1)−𝛼log𝜇(𝑏 𝑖+1|𝑥𝑖+1)] (18)
The explicit working of SAC algorithm in current modelling of
Indian financial marketing is explained in following steps:
Algorithm 1SoftActor-CriticAlgorithm
1: Initialize parameters:𝜃→ actornetwork ( 𝜇𝜃 ), Φ1→ firstcritic
network (𝑄Φ1),Φ 2→secondcriticnetwork (𝑄 Φ2)
2: Initialize policy𝜇𝜃(𝑥) , Q-values networks𝑄𝜙1(𝑥,𝑏) ,𝑄𝜙2(𝑥,𝑏) ,
target𝑄-networks & temperature (𝛼)
3:Initialize the replay buffer𝐷
4:foreach iterationdo
5:foreach environment stepdo
6: Observe current state𝑥𝑡 (technical indicators, inclina-
tion score)
7:Select action𝑏 𝑡∼𝜇 𝜃(𝑏𝑡|𝑥𝑡)
8:Execute action𝑏 𝑡
9:Calculate reward𝑟 𝑡
10:Next State𝑥 𝑡+1∼𝑃(𝑥 𝑡+1|𝑥𝑡,𝑏𝑡)
11: Store in replay buffer𝐷←𝐷∪{𝑥 𝑡,𝑏𝑡,𝑟𝑡(𝑥𝑡,𝑏𝑡),𝑥𝑡+1}
12: Sample mini-batch from D & update Q-values, policy
&𝛼
13:Soft update target𝑄-networks
14:end for
15:end for
5 EXPERIMENTS & RESULTS
In this section, before conducting the experiment we have decided
upon the relevant evaluation metrics and methodologies to assess
our results and findings.
We have done it in three phases: A.Trading without sentiment,
B.Trading with partial sentiment infusionand C.Trading with senti-
ment deep infusion. It is structured this way to give a comprehensive
choice to traders and investors to have options to choose from while
defining their requirements and trading timeline. For experiment,
we have allocated an initial portfolio of 1 million INR with trade
timeline of approximately a year (June 2023toJune 2024).
5.1 Evaluation Metrics
To comprehensively evaluate the performance of our selected al-
gorithms, we have shortlisted a few qualitative and quantitative
evaluation metrics. These metrics are selected to explain the al-
gorithm selection for different kinds of investment appetite and
trading requirements i.e. aggressive return focus trading and risk
averse trading.
5.1.1 Annual Returns.This is a useful metric to evaluate long-term
growth directly since it shows the annual overall profitability of
our RL algorithms’ investment strategy.
𝐴𝑛𝑛𝑢𝑎𝑙 𝑅𝑒𝑡𝑢𝑟𝑛=( 𝑃𝐴−𝑃 0
𝑃0
−1)×100(19)

Financial Context-Rich DRL Strategy for Trading PREPRINT
𝑃𝐴 is annual value of portfolio and𝑃 0 is the initial portfolio
5.1.2 Sharpe Ratio.This is an estimate of the risk-adjusted returns
by factoring volatility. Higher values are preferred since this tells
the returns per unit of risk.
𝑆ℎ𝑎𝑟𝑝𝑒𝑅𝑎𝑡𝑖𝑜= 𝑅𝐴−𝑅𝐴𝑅𝐹
𝜎𝐴
where𝑅 𝑓 is the risk-free rate. (20)
5.1.3 Stability.This metric conveys the consistency of our algo-
rithmic strategy in generating reliable profitable returns in various
conditions of the market.
𝑆𝑡 =1− 𝜎𝑃𝐺 𝜒𝑃𝐺 (21)
𝜎𝑃𝐺 is Standard deviation of portfolio growth and𝜒𝑃𝐺 is mean
portfolio growth.
5.1.4 Annual volatility.This metric is useful to determine and man-
age the risk exposure by qualitatively measuring the price fluctua-
tions. Low values mean lower risk.
𝐴𝑛𝑛𝑢𝑎𝑙𝑉𝑜𝑙𝑎𝑡𝑖𝑙𝑖𝑡𝑦=𝜎 𝑑×
√
252
here𝜎𝑑 is daily return standard deviation.
(22)
5.1.5 Max drawdown.This is the delta between local maxima and
local minima of a price fluctuation over a defined time period or in
the equity curve. Lower max drawdown signifies lesser risk.
𝑀𝑎𝑥 𝐷𝑟𝑎𝑤𝑑𝑜𝑤𝑛= 𝑃𝐻−𝑃𝐿
𝑃𝐿
(23)
Here 𝑃𝐻 and 𝑃𝐿 is the portfolio value at highest and lowest
respectively.
5.2 Trading without Sentiment
Initially, the five selected DRL agents were traded on the proposed
timeline without incorporating sentiment information. We used
only technical indicators in our state space. The detailed agent-wise
performances are as follows:
Metric A2C DDPG TD3 PPO SAC
Annual return 0.16 0.31 0.28 0.45 0.34
Annual volatility 0.15 0.14 0.19 0.15 0.14
Sharpe ratio 1.06 2.09 1.40 2.50 2.14
Stability 0.58 0.83 0.66 0.91 0.80
Max drawdown -0.13 -0.09 -0.15 -0.06 -0.11
Table 2: Performance Metrics of DRL Agents without Senti-
ment Infusion
• A2C: It performed moderately as compared to other agents
with lower returns and stability. It also performed poorly in
drawdown (-0.1293) which is the maximum as compared to
other agents. Drawdown indicates the maximum loss from
a peak to a trough and its lower values are preferable.
• DDPG: It outperformed A2C in annual returns, and it
showed the lowest volatility indicating more stability. It
has a high Sharpe ratio which implies good risk-adjusted
returns.
• TD3: It performed moderately on returns and showed a
decent Sharpe ratio.
• PPO: Distinctively the highest annual return, stability,
Sharpe ratio, and lowest max drawdown.
• SAC: Its Sharpe ratio is nearly as good as PPO and a strong
return trailing PPO.
It was observed that PPO performed better than all other agents
with the highest annual return and Sharpe ratio. This signifies
that PPO consistently balanced risk and returns. For risk-averse
investors, lower annual volatility is preferable, PPO showed moder-
ate volatility at 0.1531, whereas DDPG has the lowest volatility at
0.1358.
Thus, if the primary focus is the maximization of profits and
risk-adjusted returns, PPO should be considered, since it showed
the highest returns as well as the maximum Sharpe ratio. PPO also
showed high stability which indicates its consistent performance
and the lowest drawdown means that PPO also managed to keep
the potential losses to a minimum.
From the point of view of risk-averse trading, DDPG can be a
better option, since it showed the least volatility and relatively low
drawdown. Moreover, high stability and Sharpe ratio indicate that
it can perform reliably by maintaining a good balance of annual
returns and risks.
From this experiment, we developed an understanding that in
the absence of sentiment infusion the agents of both paradigms
i.e. policy optimization based and Q-learning along with policy
optimization, have paved the scope for improvement in perfor-
mance if financial markets’ contextual awareness is available to
our autonomous agents. We will be validating this idea in the next
experiment.
5.3 Trading with Partial Sentiment Infusion
We incorporated the sentiment inclination in the state space using
the inclination score and observed the results. The individual agent-
wise performance analysis is as follows:
Metric A2C DDPG TD3 PPO SAC
Annual return 0.61 0.46 0.63 0.26 0.41
Annual volatility 0.21 0.19 0.21 0.19 0.18
Sharpe ratio 2.36 2.15 2.46 1.32 2.01
Stability 0.93 0.87 0.94 0.71 0.90
Max drawdown -0.13 -0.10 -0.12 -0.14 -0.08
Table 3: Performance metrics for Sentiment Aware DRL
• A2C: It achieved one of the highest returns, thus making it
the most profitable in this scenario. It also has a high Sharpe
ratio, which implies that it provides good risk-adjusted
returns.
• DDPG: It too showed improved returns and moderate
volatility. It has a good sharp ratio and better stability,

PREPRINT Singh, Sharma and Pant
(a) A2C
 (b) DDPG
 (c) TD3
(d) PPO
 (e) SAC
Figure 5: Annual Return of DRL Agents with Partial Sentiment Infusion
though less than A2C. It is also less risky owing to a
relatively low drawdown.
• TD3: In terms of return, volatility, and max-drawdown it
performed close to A2C. In terms of stability, it exhibited to
be the most stable of all agents which is also demonstrated
by its Sharpe ratio. With the high Sharpe ratio, it gives the
best returns per unit of risk taken.
• PPO: Its returns dropped significantly, and it has a much
lower Sharpe ratio, thus giving weaker risk-adjusted re-
turns.
• SAC: It showed good returns, and a moderate volatility i.e.
it’s less risky in terms of fluctuations while maintaining a
strong Sharpe ratio and lowest drawdown.
We observed that the performance of A2C, DDPG, TD3, and SAC
improved in terms of annual returns. PPO suffered a decline in its
performance which can be attributed to its policy design. PPO tries
to prevent large shifts in policy by penalizing large updates. The
sentiment scores of real-time data may fluctuate which could cause
PPO to be more conservative in updating its policy. Thus, in this
scenario, PPO should be avoided.
For maximizing profits TD3 is more suitable as it showed the
highest performance in most of the metrics, indicating stability and
consistency in terms of risk-adjusted returns. On the other hand, for
risk-averse strategies, SAC is preferable since it provides a balance
of low volatility, minimal drawdown, and consistent returns. The
inclusion of sentiment-based contextual awareness of the market
has upgraded the performance of agents based on the technique of
Q-learning with policy optimization.
This infusion-based improvement highlights the importance of
further deeper infusion of contextual awareness into our model’s
most dynamic components such as reward and state space com-
bined. We will explore this in phase 3 of our experiment.
5.4 Trading with Sentiment Deep Infusion
For qualitative as well as quantitative infusion of financial contex-
tual awareness, we will be using the proposed method in section 4.4
for reward-based infusion. We will be following the prior method-
ology of state-based infusion. Detailed agent-wise performance is
as follows:
Metric A2C DDPG TD3 PPO SAC
Annual return 0.26 0.70 0.33 0.25 0.46
Annual volatility 0.21 0.20 0.17 0.19 0.20
Sharpe ratio 1.23 2.75 1.78 1.24 2.02
Stability 0.68 0.95 0.81 0.66 0.86
Max drawdown -0.15 -0.07 -0.10 -0.15 -0.10
Table 4: Performance metrics of DRL Agents with Deep Sen-
timent Infusion
• A2C: Showed moderate profitability at an annual return
of about 26%. Its Sharpe ratio of 1.23 implies acceptable
risk-adjusted returns.
• DDPG: Showed the highest annual return and highest
Sharpe ratio. High stability and low max drawdown make
it more consistent and profitable.
• TD3: Its annual return dropped and the Sharpe ratio de-
clined, although its max drawdown improved slightly.
• PPO: PPO struggled to generate significant profit as com-
pared to prior, in other metrics it performed closely to A2C.

Financial Context-Rich DRL Strategy for Trading PREPRINT
(a) A2C
 (b) DDPG
 (c) TD3
(d) PPO
 (e) SAC
Figure 6: Annual Return of DRL Agents with Deep Sentiment Infusion
• SAC: Showed a decent level of returns. A Sharpe ratio
of 2.02 and high stability imply it is capable of good risk-
adjusted returns.
We observed that the performance of A2C and PPO in this case
remained consistent with partial sentiment infusion. SAC showed
improvement in annual returns and the Sharpe ratio. Whereas, the
performance of DDPG showed significant improvement with higher
returns, better risk-adjusted performance, and smaller drawdown.
TD3 experienced a decrease in performance by becoming less prof-
itable, indicating that it could be more sensitive to how the infusion
of sentiment impacted the reward structure.
The agents that optimize the policy as well as the Q-value (DDPG,
SAC), become more stable upon deeper sentiment infusion except
for TD3. Although TD3 is an improved version of DDPG but DDPG
consistently showed improved performance upon deeper sentiment
infusion whereas TD3 produced poor returns. This behavior arises
from the more complex nature of TD3 to handle updates. TD3
uses double Q-learning to ensure conservative value updates. The
infusion of sentiment might cause increased variability in the re-
ward signal which caused TD3 to become overly conservative and
under explore leading to suboptimal policies and hence drop in
performance.
6 CONCLUSIONS
In this paper, we simulated the real-world trading of curated stocks
via reinforcement learning agents that interacted with the dynami-
cally changing market condition modeled as a reinforcement learn-
ing framework. We selected theactor-critic-basedagents with dis-
tinct policy design specifically,A2CandPPOare based only on
policy optimization, whereasDDPG, TD3&SACare based on pol-
icy optimization combined with Q-learning principles.
We initially performed the trading operation without any quali-
tative features using only technical indicators. Introducing partial
sentiment infusion improved the performance of all agents except
PPO. Deeper sentiment infusion led to consistently improved perfor-
mance of policy optimization and Q-learning-based agents (DDPG
and SAC) while TD3 due to a more conservative approach to value
estimation demonstrated decreased performance. Notably, DDPG
consistently exhibited performance improvement with SAC also
showing significant improvement and ranking just below DDPG.
For further research,Explainable Reinforcement Learning(XRL)
techniques[1, 15] are recommended to demonstrate the impact of
various features such as sentiment score and various technical
indicators on the agent’s decision-making process.
DISCLOSURE OF INTERESTS
The authors have no competing interests to declare that are relevant
to the content of this research.
REFERENCES
[1] Yotam Amitai, Ofra Amir, and Guy Avni. 2024. ASQ-IT: Interactive explanations
for reinforcement-learning agents.Artificial Intelligence335 (2024). https:
//doi.org/10.1016/j.artint.2024.104182
[2] Yahya Eru Cakra and Bayu Distiawan Trisedya. 2015. Stock price prediction using
linear regression based on sentiment analysis.2015 International Conference on
Advanced Computer Science and Information Systems (ICACSIS)(2015), 147–154.
https://api.semanticscholar.org/CorpusID:18389759
[3] Jiasheng Cao and Jinghan Wang. 2019. Stock price forecasting model based
on modified convolution neural network and financial time series analysis.
International Journal of Communication Systems32, 12 (2019), e3987. https:
//doi.org/10.1002/dac.3987 e3987 IJCS-18-0961.R2.
[4] Li Chen Cheng, Yu-Hsiang Huang, and Mu-En Wu. 2018. Applied attention-
based LSTM neural networks in stock prediction. 4716–4718. https://doi.org/10.
1109/BigData.2018.8622541
[5] Scott Fujimoto, Herke van Hoof, and David Meger. 2018. Addressing Function
Approximation Error in Actor-Critic Methods. arXiv:1802.09477 [cs.AI] https:

PREPRINT Singh, Sharma and Pant
//arxiv.org/abs/1802.09477
[6] Burak Gülmez. 2023. Stock price prediction with optimized deep LSTM network
with artificial rabbits optimization algorithm.Expert Systems with Applications
227 (2023), 120346. https://doi.org/10.1016/j.eswa.2023.120346
[7] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft
Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with
a Stochastic Actor. arXiv:1801.01290 [cs.LG] https://arxiv.org/abs/1801.01290
[8] Michael Hagenau, Michael Liebmann, and Dirk Neumann. 2013. Automated
news reading: Stock price prediction based on financial news using context-
capturing features.Decision Support Systems55, 3 (2013), 685 – 697. https:
//doi.org/10.1016/j.dss.2013.02.006 Cited by: 269.
[9] J.Michael Harrison and Stanley R. Pliska. 1983. A stochastic calculus model of
continuous trading: Complete markets.Stochastic Processes and their Applications
15, 3 (1983), 313–316. https://doi.org/10.1016/0304-4149(83)90038-8
[10] Huy D. Huynh, L. Minh Dang, and Duc Duong. 2017. A New Model for Stock
Price Movements Prediction Using Deep Neural Network. InProceedings of the
8th International Symposium on Information and Communication Technology(Nha
Trang City, Viet Nam)(SoICT ’17). Association for Computing Machinery, New
York, NY, USA, 57–62. https://doi.org/10.1145/3155133.3155202
[11] Jae Won Lee. 2001. Stock price prediction using reinforcement learning. InISIE
2001. 2001 IEEE International Symposium on Industrial Electronics Proceedings (Cat.
No.01TH8570), Vol. 1. 690–695 vol.1. https://doi.org/10.1109/ISIE.2001.931880
[12] Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom
Erez, Yuval Tassa, David Silver, and Daan Wierstra. 2019. Continuous control
with deep reinforcement learning. arXiv:1509.02971 [cs.LG] https://arxiv.org/
abs/1509.02971
[13] Zhuang Liu, Degen Huang, Kaiyu Huang, Zhuang Li, and Jun Zhao. 2021. Fin-
BERT: a pre-trained financial language representation model for financial text
mining. InProceedings of the Twenty-Ninth International Joint Conference on Arti-
ficial Intelligence(Yokohama, Yokohama, Japan)(IJCAI’20). Article 622, 7 pages.
[14] Pekka Malo, Ankur Sinha, Pyry Takala, Pekka Korhonen, and Jyrki Wallenius.
2013. Good Debt or Bad Debt: Detecting Semantic Orientations in Economic
Texts. arXiv:1307.5336 [cs.CL] https://arxiv.org/abs/1307.5336
[15] Stephanie Milani, Nicholay Topin, Manuela Veloso, and Fei Fang. 2024. Ex-
plainable Reinforcement Learning: A Survey and Comparative Review.Comput.
Surveys56, 7 (2024), 1 – 36. https://doi.org/10.1145/3616864
[16] Nuno Oliveira, Paulo Cortez, and Nelson Areal. 2017. The impact of microblog-
ging data for stock market prediction: Using Twitter to predict returns, volatility,
trading volume and survey sentiment indices.Expert Systems with Applications
73 (2017), 125 – 144. https://doi.org/10.1016/j.eswa.2016.12.036 Cited by: 277;
All Open Access, Green Open Access.
[17] Kunal Pahwa and Neha Agarwal. 2019. Stock Market Analysis using Supervised
Machine Learning. In2019 International Conference on Machine Learning, Big
Data, Cloud and Parallel Computing (COMITCon). 197–200. https://doi.org/10.
1109/COMITCon.2019.8862225
[18] Ping-Feng Pai and Chih-Sheng Lin. 2005. A hybrid ARIMA and support vector
machines model in stock price forecasting.Omega33, 6 (2005), 497 – 505.
https://doi.org/10.1016/j.omega.2004.07.024 Cited by: 722.
[19] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347 [cs.LG]
https://arxiv.org/abs/1707.06347
[20] Omer Berat Sezer and Ahmet Murat Ozbayoglu. 2018. Algorithmic finan-
cial trading with deep convolutional neural networks: Time series to image
conversion approach.Applied Soft Computing70 (2018), 525–538. https:
//doi.org/10.1016/j.asoc.2018.04.024
[21] Jonathan L. Ticknor. 2013. A Bayesian regularized artificial neural network
for stock market forecasting.Expert Systems with Applications40, 14 (2013),
5501–5506. https://doi.org/10.1016/j.eswa.2013.04.013
[22] Yongming Wu, Zijun Fu, Xiaoxuan Liu, and Yuan Bing. 2023. A hybrid stock
market prediction model based on GNG and reinforcement learning.Expert
Systems with Applications228 (2023), 120474. https://doi.org/10.1016/j.eswa.
2023.120474
[23] Savas Yildirim, Dhanya Jothimani, Can Kavaklioglu, and Ayşe Başar. 2018. Clas-
sification of hot News for Financial Forecast Using NLP Techniques.Proceedings
- 2018 IEEE International Conference on Big Data, Big Data 2018(2018), 4719 –
4722. https://doi.org/10.1109/BigData.2018.8621903 Cited by: 14.
[24] Jie Zou, Jiashu Lou, Baohua Wang, and Sixue Liu. 2024. A novel Deep Re-
inforcement Learning based automated stock trading system using cascaded
LSTM networks.Expert Systems with Applications242 (2024), 122801. https:
//doi.org/10.1016/j.eswa.2023.122801
