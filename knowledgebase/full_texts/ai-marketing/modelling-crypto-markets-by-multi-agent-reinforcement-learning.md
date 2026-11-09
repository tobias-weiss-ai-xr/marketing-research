---
title: Modelling crypto markets by multi-agent reinforcement learning
url: https://arxiv.org/abs/2402.10803
category: ai-marketing
subcategory: empirical
date: 2024-02
venue: ''
authors:
- Johann Lussange
- Stefano Vrizzi
- Stefano Palminteri
- Boris Gutkin
source: arxiv
pdf_url: https://arxiv.org/pdf/2402.10803
pages: 33
chars: 99849
fetched_at: '2026-11-08T13:15:33+00:00'
kb_version: 1
---

# Modelling crypto markets by multi-agent reinforcement learning

Modelling crypto markets by multi-agent reinforcement
learning
Johann Lussange1 johann.lussange@ens.fr
Stefano Vrizzi1 stef ano.vrizzi@ens.fr
Stefano Palminteri1,2 stef ano.palminteri@ens.fr
Boris Gutkin1,2 boris.gutkin@ens.fr
1 Laboratoire des Neurosciences Cognitives, INSERM U960, Département des Études Cognitives
École Normale Supérieure, 29 rue d’Ulm, 75005, Paris, France.
2 Center for Cognition and Decision Making, Department of Psychology, NU University Higher School of
Economics, 8 Myasnitskaya st., 101000, Moscow, Russia.
Abstract
Building on a previous foundation work [ 1], this study introduces a multi-agent reinforcement
learning (MARL) model simulating crypto markets, which is calibrated to the Binance’s daily
closing prices of 153 cryptocurrencies that were continuously traded between 2018 and 2022. Unlike
previous agent-based models (ABM) or multi-agent systems (MAS) which relied on zero-intelligence
agents or single autonomous agent methodologies, our approach relies on endowing agents with
reinforcement learning (RL) techniques in order to model crypto markets. This integration is
designed to emulate, with a bottom-up approach to complexity inference, both individual and
collective agents, ensuring robustness in the recent volatile conditions of such markets and during
the COVID-19 era. A key feature of our model also lies in the fact that its autonomous agents
perform asset price valuation based on two sources of information: the market prices themselves,
and the approximation of the crypto assets fundamental values beyond what those market prices
are. Our MAS calibration against real market data allows for an accurate emulation of crypto
markets microstructure and probing key market behaviors, in both the bearish and bullish regimes
of that particular time period.
1. Introduction
General problem Crypto markets, characterized by their high volatility and unpredictability [2],
present a unique challenge for quantitative financial modeling. These markets are not just volatile,
they are complex ecosystems influenced by a myriad of factors that are both internal and external
to the market [3]. Some crypto assets like utility tokens provide users with access to a service such
as membership in a network (e.g. decentralized application) [4], others like cryptocurrencies and
stable coins serve to facilitate digital transactions and can also be used as a store of value or a
unit of account [5, 6], while others like security tokens represent ownership of a real-world asset,
such as stocks, bonds, artwork or real estate [7]. But also, crypto assets rely on very different
decentralized technologies [8], and each have their own specifics tokenomics [9, 10], with very diverse
individual impacts on their valuation. Building on the earlier foundational ideas of distributed
ledgers [11, 12], modern crypto assets now also rely on many various protocols [13, 14]. Thus,
contrary to more traditional equity markets and their own order book dynamics and transaction
orders, these protocols profoundly impact the nature of the crypto market microstructure. For all
these reasons, the equity concept of fundamental valuation [15, 16] is notoriously different for crypto
assets: unlike stocks, where fundamentals are often linked to tangible economic performance of the
company issuing the stocks (e.g. quarterly reports, news of companys’ deals), the nature of crypto
assets’ fundamental values can be more debated and tied to unique features that are proper to crypto
assets (e.g. white paper, evolving regulation). Factors such as applicability of the cryptocurrency
1
arXiv:2402.10803v1  [q-fin.CP]  16 Feb 2024

Lussange, Vrizzi, Palminteri, Gutkin
in real-world transactions, limited supply mechanics (e.g. Bitcoin’s fixed supply cap), robustness
of the underlying technology, user base and adoption, legal and regulatory developments impacting
the asset, etc. are parameters exogeneous to the market that can enter and impact its fundamental
value [17, 18].
Past research Past research in crypto market modeling that is grounded in traditional financial
market theories is thus at risk of being outpaced [3, 18] by the unique characteristics of crypto
markets, such as their extreme volatility, decentralization protocols, and fundamental valuation.
Fortunately, recent quantitative methods from agent-based modelling has provided useful tools [19]
with a focus on various aspects such as examining the interconnectedness of markets [20], analyzing
the effects of market regulation [21], understanding supply and demand dynamics [22], exploring
the impact of high-frequency trading [23, 24], assessing the outcomes of quantitative easing [25],
and investigating the influence of external factors [26]. This domain has seen significant success in
replicating characteristic market behaviors, known asstylised facts. Stylized facts describe consistent
statistical patterns in asset price fluctuations and volatility observed in such diverse markets and
time frames that they have been called universal [27]. Notable among these observations are those
related to the distribution of returns and the phenomenon of volatility clustering, which gained
recognition during the 1990s. Pioneering works by Kim and Markowitz [28], Levy, Levy, and
Solomon [29, 30, 31, 32, 33, 34, 35], Cont and Bouchaud [36], Solomon and Weisbuch [37], Lux and
Marchesi [38, 39], Donangelo and Sneppen [40, 41, 42, 43], and Solomon, Levy, and Huang [44]
significantly contributed to these insights. Notably, it was during this period that ABMs began to
emulate these stylized facts. The importance of the universality of these stylized facts stems from
the fact that the underlying causes of price movements in different markets can be markedly distinct,
encompassing both exogenous and endogenous factors. Consequently, these stylized facts shed light
on fundamental financial mechanisms that transcend specific markets. This understanding, in turn,
holds considerable value for shaping the architecture of ABMs. From a scientific perspective, the
faithful replication of these stylized facts has been a major area of research for approximately the
past twenty years [45, 27]. While their precise characteristics have exhibited subtle variations over
time and across scholarly works, the most widely recognized accepted stylized facts can be broadly
categorized into three intersecting domains:
• Non-Normal Returns: The distribution of returns notably deviates from the Gaussian distribu-
tion, challenging conventional models that treat asset prices as following Brownian random
walks [46, 47]. These non-Gaussian distributions exhibit distinctive characteristics, including
heavier tails that can be approximated by a power law with exponents typically falling within
the range of[2, 4]. Additionally, these distributions are characterized by negative skewness, often
displaying asymmetry in many observed markets, a platykurtic profile, resulting in events that
are less centered around the mean [48, 46, 49, 50, 51, 52, 53, 54], and multifractalk-moments,
causing the exponent to deviate from a linear relationship withk [51, 52, 53, 54].
• Volatility Clustering: The volatility of the market exhibits a tendency to cluster or form distinct
clusters [55]. Consequently, when compared to the average, the likelihood of experiencing high
(resp. low) volatility in the near future is notably higher if the recent past witnessed similar
high (resp. low) volatility [45, 56, 57]. Irrespective of whether the next return is positive or
negative, this leads to the observation that significant return fluctuations are often followed
by similar fluctuations, thus showcasing a form of long-term memory [58] and correlatively, a
clustering effect in trading volumes.
• Decaying Auto-Correlations: The auto-correlation function characterizing returns in financial
time series data is predominantly near zero for most lag values, with the exception of very short
lags. This is attributed to a mean-reverting microstructure mechanism that results in negative
auto-correlations [49, 59]. This phenomenon aligns with the Efficient Market Hypothesis [60, 61],
2

Modelling crypto markets by multi-agent reinforcement learning
positing that markets lack memory, implying that the prediction of future prices based on
past prices or information is implausible [56, 57]. Nonetheless, it has been observed that
certain nonlinear functions of returns, such as squared or absolute returns, exhibit persistent
auto-correlations over longer lags [59].
Subsequently, ABMs of financial markets have evolved to incorporate increasingly realistic features and
are capable of generating more robust scaling experiments. Notably, these simulations hold promise
for forecasting actual financial time series data through a reverse-engineering approach [62, 63].
New trends In recent times, ABM in economic studies have gained enhanced realism through
the modern breakthrough of machine learning [64, 65] and especially multi-agent learning [66, 67].
Reinforcement learning [68, 69, 70], in particular, shares similarities with decision-making processes in
the brain [71, 72, 73, 74], offering a computational framework to quantitatively analyze agent learning
in market price formation. Nonetheless, the integration of reinforcement learning models with real
financial data remains an ongoing challenge [69, 70, 68]. Although many current models do not fully
emulate markets with autonomously learning agents [68, 75], there is a growing interest in applying
reinforcement learning to financial ABM [75, 76, 77, 78], notably crypto markets [79], as well as order
book models [80, 81, 82]. Notably, recent multi-agent reinforcement learning (MARL) models, which
consider the collective behavior of multiple market participants, merit consideration [19, 1, 83]. Our
study builds upon these foundations, seeking to integrate and extend these methodologies, especially
in the context of real-world crypto market data from Binance, to provide a more comprehensive
understanding of the complexity of crypto markets.
Our contribution Since Bitcoin’s inception in2009, the cryptocurrency landscape has expanded
significantly, with over8, 000 digital currencies listed and a cumulative peak value of2.97 trillion
dollars in 2021. The rise in crypto exchange volumes reveal the importance of this new highly
sought-after alternative asset class. By 2023, over two hundred exchanges, including giants like
Binance with substantial daily trading volumes, have emerged, highlighting the profitability of
cryptocurrency trading. In a previous work [1], we have developed SYMBA (SYstème Multi-agents
Boursier Artificiel), an innovative MARL stock market simulator, leveraging reinforcement learning
for agent autonomy in stock price forecasting and transaction order execution [19]. This model
underwent meticulous calibration to align with actual stock market data. Subsequent research [83]
explored the evolutionary acquisition of trading strategies by its agents. This model simulates a
financial market’s microstructure through a bottom-up methodology, utilizing autonomous economic
entities—such as investors and institutions—and their financial activities, including trades and
holdings. In its equity version, each agent in SYMBA is characterized by two aspects: firstly, a
reinforcement learning algorithm for skill enhancement in price prediction and trading activities,
allowing them to independently evolve their forecasting and trading proficiency; secondly, their
learning orientation is gauged between chartist and fundamentalist, via a weight parameter that
is learned by the RL of each agent, depending on the market regime and general state. Agents
interact with a centralized order book, submitting individual orders that are then sorted and matched
for transactions. Through reinforcement learning, they assess past investment outcomes, adjusting
their strategies in response to evolving market conditions. SYMBA not only replicates supply-
demand dynamics and other crucial aspects of market behavior like illiquidity and bid-ask spread
evolution [84, 85] but also facilitates comparison of its simulated stock prices and volumes with real
financial data. Calibration of the MAS parameters allows for an analysis of the collective impact of
agents’ learning dynamics. Our model enables a comprehensive examination of financial markets
from a micro to macro perspective. In [1], we correlated the overall stock market returns with
real-world data, while [83] focused on evaluating the agents’ trading performance, informed by their
evolving strategic learning dynamics. We here apply SYMBA to model crypto markets, via a careful
3

Lussange, Vrizzi, Palminteri, Gutkin
calibration process to Binance’s daily close prices of153 crypto assets, which were continuously
traded from September27, 2018, to September27, 2022, aims to address these challenges.
Structure The structure of this paper is laid out as such: Section 2 offers a primer on reinforcement
learning. Following this, Section 3 outlines the details of the architecture of our model, SYMBA,
outlying its iterative process, agent-specific reinforcement learning algorithms for crypto asset
forecasting and trading, and the mechanics of its distributed order book featuring a double auction
limit orders procedure. We have made the entire SYMBA code publicly accessible on GitHub for
community benefit [86]. The subsequent Section 3.5 show its calibration to Binance crypto data, and
the optimization procedure of the model hyperparameters, with Section 4 devoted to the results of
this calibration. The paper concludes in Section 5 with a discussion of our results, their implications
for cryptocurrency trading and analysis, and potential directions for future research.
2. Reinforcement learning
Figure 1: Classical algorithmic procedure of a reinforcement learning agent at time stept in the
context of SYMBA described in Section 3. In a given statest of its environment (i.e. the market), a
given agent i selects one of its actionsat (from its forecasting or trading algorithm) with respect
to the market order book of a given assetj, thus yielding an associated given rewardrt+1 and new
state of the environmentst+1.
This section offers a concise overview of the core principles of reinforcement learning, a distinct
paradigm within machine learning characterized by its focus on learning through so-called rewards
(or reinforcements). For an extensive exploration of this topic, interested readers are directed to key
resources such as [87, 88, 89].
States, actions, rewards : In the realm of reinforcement learning, three parameters are essential:
the set of statess ∈ S, depicting the various environments in which the agent may operates without
4

Modelling crypto markets by multi-agent reinforcement learning
exerting control; the set of actionsa ∈ A, representing the actions the agent can potentially select in
its environment or states; and the rewardr ∈ R eventually received by each agent after it selected
a given action in a state of its environments at time t. Notably, reinforcement learning assumes
Markovian state signals. A state signal is considered Markovian, or possesses the Markov property, if
and only if∀s′, r′ and prior historiesst, at, rt, st−1, at−1, rt−1, . . . , s1, a1, r1, s0, a0, it satisfies:
P r(st+1 = s′, rt+1 = r′|st, at) = P r(st+1 = s′, rt+1 = r′|st, at, rt, . . . , r1, s0, a0) (1)
Following the notation in [87], P r{X = x} signifies the likelihood of a random variableX assuming
the value x.
Policy and value functions To achieve its ultimate objective of maximizing cumulative rewards
over time, an intelligent agent must learn and acquire optimal behavior within its environment. This
optimal behavior involves determining the most advantageous actionsa, to undertake in response to
specific states of its environments. The function used by the reinforcement learning agent to learn
this behavior is called thepolicy, which essentially captures the agent’s probabilities of selecting each
action a given a particular states. Mathematically, this policy is denoted as:
π(s, a) = P r(a|s). (2)
Initially, this policy begins with equiprobable action selections. However, it evolves over time through
exploration by the agent of its environment, ultimately converging towards an optimal policy, denoted
as π∗(s, a). In order to do this, at each time stept, the agent essentially practices trial and error,
selecting a new actionat while in statest, and then subsequently estimating the associated rewards.
These rewards play a central role in updating the probabilities of each state-action pair withinπ(s, a).
Nonetheless, an important feature of reinforcement learning theory is that these rewards aren’t always
immediate; they can be delayed over time. In the realm of reinforcement learning, this temporal
delay in rewards is often addressed using a real parameter known as thediscount factor, denoted
as γ ∈ (0, 1], and introducing the notion of delayed rewards. Here, the agent’s policy updates are
driven not by the immediate rewards but by the concept ofreturns, denoted asRt. Returns represent
the cumulative sum of rewards, factoring in time-based discounting as such over an episodic task of
T ∈ N time steps:
Rt =
TX
k=0
γkrt+k+1. (3)
By setting γ <1, the agent assigns progressively less significance to rewards that are farther into the
future, thereby emphasizing the importance of immediate rewards in the learning process. Beyond
temporal considerations, it is crucial to recognize that rewards are inherently stochastic or statistical
in nature. To assess the magnitude of these returns, the reinforcement learning agent relies on a
probabilistic approach by working with theexpectations of these returns. This idea, coupled with the
discount factor, appears in the so-calledvalue functionused by the agent to evaluate the effectiveness
of its action selections. In the model-based version of reinforcement learning, this value function is
the state-value function, denoted asV (s), and calculates the expected returnRt when the agent is in
a specific statest = s:
V (s) = E[Rt|st = s]. (4)
It is itself intimately linked to two fundamental components: the transition probabilityPss′a =
P r(st+1 = s′|st = s, at = a), representing the likelihood of transitioning from states to state s′
5

Lussange, Vrizzi, Palminteri, Gutkin
given action a, and the expected valueRss′a = E(rt+1|st = s, at = a, st+1 = s′), which represents
the expected reward when transitioning from states to s′ under the influence of actiona.
In the model-free version of reinforcement learning, the value function used by the agent is the
action-value function, denoted asQ(s, a). This function quantifies the expected return, considering a
specific action at = a taken in statest = s. Formally, it can be expressed as:
Q(s, a) = E [Rt|st = s, at = a] . (5)
In summary, these three functionsπ(s, a), V (s), and Q(s, a) are instrumental in shaping the agent’s
decision-making process, enabling it to learning an optimal policy from its environment effectively,
optimize its actions, and adapt to the complex interplay of delayed rewards and stochastic outcomes
inherent to reinforcement learning.
Policy-based vs. value-based The convergence ofπ(s, a) to the optimal policyπ∗(s, a) is hence
the main goal of each reinforcement learning. In order to do this, there are two main families of
reinforcement learning approaches. Inpolicy-based reinforcement learning, the agent directly updates
the probabilities associated with each state-action pair within its policy function. The exploration of
the policy space can take place through both "gradient-based" and "gradient-free" techniques. In
value-based reinforcement learning (such as model-based and model-free reinforcement learning), the
value function is first evaluated according to the returns resulting from action selection, and then
the policy is updated. In model-based reinforcement learning, the agent first updates the transition
probability Pss′a and the expected valueRss′a, and then derives its value function so as to update
its policy. In model-free reinforcement learning, the value function (V (s) or Q(s, a)) is directly
estimated in order to update the policy function. Model-based reinforcement learning thus relies on
the agent converging to the optimal policy by first building a model of its environment (functions
Pss′a and Rss′a) and then deriving the associated value function (V (s) or Q(s, a)). The model-free
approach offers the advantage of converging to this optimal policy by exploring state-action pairs
independently of having a model, streamlining the learning process. Value-based methods rely on
the so-called Great Policy Iteration theorem, which consists in updating the value function after
the agent received its return, in order to refine the policy, which in turn is used later on at action
selection to better evaluate the value function and hence the policy, in a positive feedback loop unto
convergence to the optimal policy. Three major different algorithms are used to that end:Dynamic
Programming (DP), Monte Carlo(MC), andTemporal Difference(DP) learning.
Exploration vs. exploitation Reinforcement learning shares its foundational principles with
biology, where optimal behavior is not directly learned but rather emerges through trial and error
within the context of predefined rewards or reinforcements. This fundamental process is referred to
as the "exploration vs. exploitation" dilemma, where the agent faces a crucial decision over time:
should it persistently choose actions that yield the highest rewards (exploitation), or should it explore
new actions in the hopes of discovering even better rewards (exploration)? Several methods have
been devised to address this exploration-exploitation trade-off. These include theϵ-greedy method,
where a probabilityϵ ≪ 1 is chosen to either explore a random action or exploit the best action at
each time step (withϵ close to 0 indicating a strong preference for exploitation), thesoftmax method,
which ranks actions from best to worst according to a temperature parameter for exploration, and the
pursuit method, which continually selects the action that is currently deemed the best for exploitation.
Balancing exploration and exploitation is a challenge for the agent, as it cannot definitively know
whether more exploration will lead to a better policy or if it will yield unfavorable outcomes.
Temporal credit assignment Moreover, there are instances where a sequence of actions must be
undertaken over extended durations before the agent can attain the desired reward. Consequently,
6

Modelling crypto markets by multi-agent reinforcement learning
reinforcement learning deals with the notion of “delayed reward.” In certain applications of reinforce-
ment learning, we hence encounter the accumulation of discounted rewards over time, represented by
the return Rt as we saw in the context of state-valueV (s) and action-value Q(s, a) functions. This
comes with the latter challenge of assigning credit to state-action pairs at each time step, a problem
known astemporal credit assignment.
Curse of dimensionality A third crucial feature of reinforcement learning relates to what is
often referred to as thecurse of dimensionality. This issue stems from the fact that in practical
applications, the number of possible state-action pairs that an agent must explore rapidly becomes
computationally intractable. Consequently, with each reinforcement learning application comes the
question to define states and actions in such a way that most state-action pairs can practically be
explored by the agent.
Recent research trends These considerations regarding exploration versus exploitation, delayed
rewards, and dimensionality are central features of reinforcement learning and most active areas of
research in recent years have tackled these issues. Notably,policy gradient methodsseek to refine the
control policy iteratively by descending along the gradient of expected returns [90, 91]. Also, the
Q-learning [92], itself part of the model-free TD-learning paradigm, has been one of the first major
breakthroughs of reinforcement learning, by significantly reducing the number of states that require
exploration, focusing solely on pairs(s, a). This issue is crucial when reinforcement learning must
deal with large-scale Markov decision processes, making the exploration and convergence towards
an optimal policyπ∗(s, a) more difficult. This challenge of dimensionality underscores the problem
of function approximation, which has led to the fusion of reinforcement learning with artificial
neural networks, with theend-to-end or deep reinforcement learningparadigm [93]. Additionally,
ongoing research addresses related issues such aspartially observable MDP models[94, 95] and
adversarial reinforcement learning[96]. These aim to model the noise and uncertainties inherent
in state representation by introducing adversarial agents that apply specific perturbations to the
system.
A more recent research area ismeta-reinforcement learning[97], which strives to achieve rapid
generalization over different tasks and across varying time scales, a notion closely aligned with
zero-shot and few-shot reinforcement learningREF. Concurrently,transfer reinforcement learningREF
aims to transfer the knowledge gained from one task to improve performance on another, while
imitation reinforcement learningREF focuses on learning from observing other agents. Also,actor-
critic methodsintroduce a dual-role paradigm, where an actor shapes the agent’s behavior while a
critic evaluates the agent’s actions [98].
Parallel to these developments, multi-agent andself-play reinforcement learning[99] involve agents
learning policies by competing against or collaborating with other learning agents. In this domain,
multitask reinforcement learningREF explores the synergy among multiple tasks to enhance individual
task performance. It intersects withasynchronous reinforcement learning[100], which works through
parallel agent instances that share a model, diversifying the data collection process.
Modular reinforcement learning[101] decomposes complex tasks into manageable subtasks, crafting
individual policies for each, and then reconstructing them into a cohesive policy framework. In this
domain, Monte Carlo Tree Search(MCTS) reinforcement learning [93] adopts a different strategy by
employing tree search and random sampling of the search space to determine optimal actions.
Lifelong reinforcement learning[102] deals with the challenge of mastering a multitude of sequential
tasks over an agent’s lifetime.Hierarchical reinforcement learning[103] groups agent actions into
higher-level, more abstract tasks, thereby simplifying decision-making. Finally,hybrid reinforcement
learningREF, often referred to as “human-in-the-loop” reinforcement learning, relies on the role of
human intervention in improving the learning process, exemplified in domains like intelligent driving.
7

Lussange, Vrizzi, Palminteri, Gutkin
Thischallengeinvolvesthetaskofspecifyinganddefiningtherewardsandreturnsforanagent. Beyond
the previously mentioned approach in hierarchical reinforcement learning, research is addressing this
issue throughreward shaping[104], which includes background knowledge related to sub-rewards to
enhance convergence rates. Additionally, there is the concept ofinverse reinforcement learning[105],
which extracts the reward function from the observation of optimal behavior exhibited by another
agent. Furthermore, we can also highlighthomeostatic reinforcement learning[106, 107], which
defines the reward within a manifold of numerous sub-rewards, and a state-dependent approach for
defining the agent’s rewards [108].
3. Model and data
Figure 2: Comprehensive Schematic of the SYMBA crypto Market Simulator and Its Operational
Dynamics. This figure presents an integrated view of the SYMBA simulator, emphasizing the
dual-level interaction within the simulated financial market. At the core of the system, individual
agents (bottom-left) utilize two distinct reinforcement learning algorithms,F i for forecasting andT i
for trading, to independently formulate and execute trading strategies at each simulation step. These
strategies are then aggregated at the market level through a centralized double-auction order book
(top-right). The order book directs market dynamics by matching buy and sell orders from different
agents, effectively determining market prices and volumes (bottom-right). This figure illustrates the
iterative loop of agent decision-making and market adjustment (top-left), which collectively shapes
the emergent macroscopic market behavior. By simulating the interplay between individual agent
strategies and market-level effects, SYMBA provides insights into how individual behaviors and
collective market responses yield in a complex financial ecosystem.
8

Modelling crypto markets by multi-agent reinforcement learning
In this section, we provide a detailed exposition of the architecture of our crypto market MAS
simulator, along with an in-depth discussion of the design principles governing its autonomous agents.
3.1 General architecture
As previously said at the end of Section 1, our simulation relies on several central parameters, namely:
the total number of agents denotedI, the quantity of assets tradedJ, and the duration of the
simulation in discrete time stepsT. It is worth noting that each time step corresponds to a single
trading day, or actually a trading day and night, since contrary to stock markets, crypto markets
like Binance trade24/7. Thus a year encompassesTy = 365 trading days, a month spansTm = 30
trading days, and a week encompassesTw = 7 trading days. Our analysis typically involves the
examination of statistical properties derived from a series ofS simulations. Furthermore, our model
incorporates critical financial factors such as transaction costs, as network feesb for each crypto asset
trade (which can largely vary from exchange to exchange, and from asset to asset), an annual risk-free
interest rate R pertaining to agents’ risk-free assets, and a general APR or Annual Percentage Rate
D (e.g. linked to staking in Proof of Stake consensus protocols for example). For the purpose of
simplification and model tractability, we assume these financial parameters to be uniform across
simulated crypto assets, with network fees set atb = 0.1%, the risk-free rate atR = 1%, and the
APR at D = 3%. Each simulation cycle at timet comprises four primary steps, each outlined below:
i- Initialization of Agent Parameters: At the begining of the simulation, whent = 0, a number ofI
agents are initialized, each with their unique set of parameters. These agents, representing either
individual or institutional investors, manage portfolios consisting of both crypto assets and risk-free
assets (e.g. bank account or bonds). These parameters are elaborated upon in Section 3.2.
ii- Initialization of Market Fundamentals: Following the approach adopted by various models, we set
all initial asset prices at$100 (P j(t = 0)). Here we consider the value of the crypto assets in fiat
money (i.e. US Dollars) instead of crypto currency (e.g. BTC, i.e. Bitcoin), but this has no impact
on the microstructure of the prices and volumes that are generated to emulate crypto markets. Then,
J price time series T j(t) are generated as stochastic jump processes, mirroring the fundamental
values of stocks. The term “fundamental values” for crypto assets, as used in this context, can be
comprehended in relation to the concept of “fundamental valuation” found in stock markets. In
traditional stock markets, the fundamental value of a share is based on the economic performance and
future prospects of the company that issued it. When it comes to various types of crypto assets, such
as utility tokens, cryptocurrencies, stablecoins, or digital securities representing real-world assets,
their fundamental value is different. It is determined by factors external to their current market
price, focusing on the potential technological advancements and economic growth associated with
the asset. While there might be debates around this, it is crucial to recognize that investors often
approach crypto assets with a mindset similar to that of traditional equities. They believe these
assets have an inherent value that is not solely reflected in their market price, encompassing past,
present, and future potential. However, it is important to note that this information is not directly
accessible to theI agents. Instead, each agenti estimates the valueT j(t) for asset j using their
own cointegration rule denoted asκi,j[T j(t)] = Bi,j(t). Consequently, the seriesBi,j(t) represent the
perceived fundamental values of assetj over time t as perceived by agenti. As an example, Fig. 3
elucidates the notion of cointegration by juxtaposing the modeled fundamental valuesT j(t) with
their approximations Bi,j(t) as derived by select agents.
From a comprehensive analysis of S = 20 simulations, we determine that the average annual
number of jumps inT j(t) above or below20% is 1.30, the average jump amplitude (expressed as
(T j(t) − Tj(t − 1))/T j(t)) is 4.97% (with standard deviation of6.50), and the average disparity
between the biased and actual values (indicated as(T j(t) − Bi,j(t))/T j(t)) amounts to4.69% (with
9

Lussange, Vrizzi, Palminteri, Gutkin
Figure 3: Representation of the trajectories of fundamental values modeled byT j(t) (depicted as a
black line) and their estimated values (denoted asBi,j(t)) by three different agents (displayed as red,
blue, and green lines, resp.), over200 time steps.
standard deviation of1.38). These insights inform the agents’ crypto asset pricing strategies, which
incorporate both chartist and fundamental sources of information.
iii- Autonomous Forecasting and Trading by Agents: Within this model, each agent independently
utilizes two reinforcement learning algorithms for engaging in the market. Further details about these
algorithms can be found in Section 3.3. The initial algorithm, labeled asF i, focuses on creating
an optimal econometric forecasting function. This function takes into consideration the unique
characteristics of the market’s microstructure and the agent’s own fundamental valuationBi,j(t). The
forecast produced byF i is subsequently utilized by the second reinforcement learning algorithm,T i.
The responsibility ofT i is to generate the most suitable limit order for a double auction order book
(as explained in [109]) at that particular time step. Notice the order books of a Centralized EXchange
(CEX) like Binance are not dissimilar from those of more classical markets like stock markets. This
process incorporates the forecast as well as various indicators related to the market microstructure
and the agent’s portfolio. An essential component of this procedure is the filter functionGi, which
determines the optimal time step for the agent to execute a transaction order.
iv- Order Book Population and Processing: At each time stept, a collection ofJ order books is
populated with limit orders from agents for a specific crypto assetj. These orders are organized
such that buy orders are ranked in descending order of bid prices, and sell orders in ascending order
of ask prices, each accompanied by the quantity of crypto assets offered for trade. The clearing of
the order book takes place at the same time stept. It involves matching buy and sell orders starting
from the highest bid and lowest ask prices, progressing until bid prices no longer exceed ask prices.
The market priceP j(t + 1) for asset j in the subsequent time stept is determined by the mid-price
at this final matching point. Likewise, the trading volumeV j(t + 1) is defined as the total quantity
of crypto assetj exchanged at timet. Additionally, the spreadW j(t + 1) for asset j at time stept is
calculated as the absolute difference between the mean of all bids and asks. Notably, this spread,
W j(t), is employed in the agents’ crypto asset pricing mechanism, rather than the traditional bid-ask
spread, typically defined as the gap between the highest bid and the lowest ask. The pseudo-code of
SYMBA’s iteration procedure is found in Fig. 4.
10

Modelling crypto markets by multi-agent reinforcement learning
Initialize Market parameters at t=0: I, T, P(t=0)...
Initialize Agents parameters at t=0: w, h, B(t=0)...
for (t=1; t<T; t+=1) { // simulation starts
for (i=0; i<I; i+=1) { // loops over all agents
for (j=0; j<J j+=1) { // loops over all crypto assets
Agents[i].F() // each agent RL forecasting
Agents[i].T() // each agent RL trading
} // closes j loop
} // closes i loop
for (j=0; j<J j+=1) { // loops over all crypto assets
OrderBook[j].Sort() // sorts offers vs. bids
OrderBook[j].Clear() // clears transactions, outputs P(t)
} // closes j loop
Outputting online statistics...
} // closes t loop
Outputting offline statistics...
Figure 4: Pseudo-code of SYMBA’s iteration procedure.
3.2 Initialization procedure
Our approach incorporates a diverse set of parameters that operate at both the individual agent
and the overarching framework levels. As previously outlined in Section 3, we utilize continuous
and discrete uniform distributions denoted asU () and U, respectively. Additionally, continuous and
discrete normal distributions are denoted asN () and N, respectively. Atstep 1, each agenti receives
the following initial parameter assignments:
– A trading window, denoted as wi, is determined by a uniform distributionU Tw, τi. This
parameter significantly influences theGi function, which is responsible for determining the
optimal timing for crypto assets purchases.
– An initial value of risk-free assets denoted asAi bonds(t = 0), following a normal distribution
N (0, 104). This represents the agent’s holdings in bonds or their bank account balance, which
fluctuates in response to the agent’s decisions to short or long crypto assets.
– The quantity of crypto assetsQi,j(t = 0) for each asset j, derived from a discrete positive
half-normal distribution N +0, 100. The total value of these assets is calculated asAi equity(t =
0) = PJ j=0 Qi,j(t = 0)P j(t = 0). Agents have the option to short sell these crypto assets in
the market. Notice the agents cannot buy not sell partial amount of a given crypto asset (e.g.
0.5ET H), but only an integer amount thereof. One of our model assumptions is that this integer
feature does not change the simulated market microstructure and dynamics significantly, as
real crypto market agents often deal with standard fractional values of certain cryptocurrencies
for example (cf. millibit or mBTC equal to10−3 BTC, satoshi or sat equal to10−8 BTC,
milliether equal to10−3 ETH, gwei equal to10−9 ETH, etc.).
– An investment durationτ i, selected from a uniform distributionU Tw, 6Tm. This parameter
determines the time frame after which the agent will liquidate its position, with a range spanning
from one week to six months in trading days.
– A memory spanhi, obtained from a uniform distributionU Tw, T. This interval represents the
historical data duration considered by the agent during its learning process.
11

Lussange, Vrizzi, Palminteri, Gutkin
– A transaction gesture threshold gi, derived from a uniform distribution U (0.2, 0.8). This
parameter indicates the agent’s willingness to transact at prices either above or below its own
asset valuation. The range of this parameter is influenced by the model’s gesture scalarζ i, as
discussed in Table 1 below.
– A reflexivity amplitude parameterρi, assigned from a uniform distributionU (0, 100%). This
parameter impacts the agent’s approach to price valuation, striking a balance between technical
market forecasts and fundamental pricing. It directly influences the action amplitudeF within
the first reinforcement learning algorithm.
– A reinforcement learning rate parameter βi, set from a uniform distributionU (0.05, 0.20).
This rate applies to both reinforcement algorithmsF i and T i and is informed by findings in
neuroscience literature [110, 72, 73].
– A drawdown thresholdli, defined as the year-to-date peak-to-bottom loss in net asset value,
drawn from a uniform distributionU (40%, 50%). If the agent’s portfolio value falls below
this threshold at any given time stept, the agent is declared bankrupt and excluded from
further market interactions. It’s worth noting that this threshold is set higher than typical
industry standards to ensure a constant number of agents within our model, even in bankruptcy
scenarios.
In this section, we will explain further the various parameters of our model. Some of these parameters
are optimized as hyperparameters of the model, such as the drawdown thresholdli, which is adjusted
using a threshold parameterL ∈N+). Additionally, the transaction gesture parameter,gi, is modified
through ζ i ∈ N. Other parameters are derived from existing literature, such as the reinforcement
learning rate βi ∈ R+. Parameters like the reflexivity amplitude parameter, denoted asρi, are
integrated as learned variables in the reinforcement learning process of the agent. Furthermore,
certain parameters are preset, including the initial values of agents’ bond portfoliosAi bonds, equity
portfolios Ai equity, the investment horizonτ i, and the time intervalswi and hi. These components
collectively form the foundational framework of our model’s architecture.
3.3 Agent first RL algorithm
In this section, we will explore the details of "step3" mentioned earlier, with a focus on the two core
reinforcement learning algorithms:F i, responsible for accurate price prediction, andT i, dedicated to
effective trading based on those predictions. As previously discussed, each agenti independently runs
these algorithms for each crypto assetj at every time stept. These algorithms utilize a direct policy
search approach, where the probability of each action is directly determined from the policy, bypassing
the use of an action-value function as described in the Generalized Policy Iteration theorem [87].
The action-state pairs for these algorithms consist of729 for F i and 972 for T i. We define the
sets of statesS, actions A, and returnsR for both algorithms as follows. The first algorithm,F i,
enables the agent to monitor long-term asset price volatility (sF 0 ), short-term volatility (sF 1 ), and
the discrepancy between its fundamental valuation and the current market price (sF 2 ). Using this
information, the agent optimizes its price forecasting over its investment horizonτ i by evaluating
three actions through a direct policy search: adopting a basic econometric forecasting method focused
on mean-reverting, averaging, or trend-following (aF 0 ), selecting the duration of the past interval for
forecasting (aF 1 ), and determining the influence of its own fundamental asset pricing in the combined
future price estimate, which incorporates both fundamentalist and chartist perspectives (aF 2 ).
12

Modelling crypto markets by multi-agent reinforcement learning
State Space S F: The F i algorithm operates within a state space denoted asS F, which comprises27
dimensions. Each component of this state space can assume values of0, 1, or 2. The agents calculate
the variances σ2 L and σ2 S of crypto asset pricesP j(t) over specific time frames.
– σ2 L represents long-term volatility and is evaluated and stored as a time series. It is sorted in
ascending order and truncated to match the agent’s memory spanhi. The percentile ranking
of σ2 L at time t determines sF 0 , classifying it into three categories:sF 0 = 0 if it falls below25%,
sF 0 = 2 if it exceeds75%, and sF 0 = 1 otherwise.
– Similarly, σ2 S, indicating short-term volatility, is processed and categorized in the same manner
as sF 1 , providing insights into the short-term market dynamics of assetj.
– The deviation between the market price and the agent’s fundamental valuation is measured by
averaging the relative difference|P j(t) − Bi,j(t)|/P j(t) over a specific interval[t − 3τ i, t]. This
measurement sets sF 2 = 0 if it is below10%, sF 2 = 2 if it exceeds30%, and sF 2 = 1 otherwise.
Actions AF: Within the framework of the reinforcement learning algorithmF i, we contemplate an
action aF, which is a constituent of a setAF = aF 0 , aF 1 , aF 2 , encompassing 27 possible states. Each
action, specifically aF 0 , aF 1 , aF 2 , holds the capability to independently adopt one of the values0, 1, or
2. The determination of these actions is subject to a direct policy search, as elaborated subsequently,
contingent upon whether the agent finds itself in a phase of exploration or exploitation. Initially,
each agent computes two distinct mean values,⟨P j[t − 2T, t− T ](t)⟩ and ⟨P j[t − T, t](t)⟩, derived
from the historical asset prices. Here,T is explicitly defined asT = (1 + aF 1 )τ i/2. Subsequently, the
econometric mechanism calculates:
ˆP i,j(t) = P j(t) + ⟨P j[t − 2T, t− T ](t)⟩ − ⟨P j[t − T, t](t)⟩ (6)
ˆP i,j(t) = 1 2 ⟨P j[t − 2T, t− T ](t)⟩ + 1 2 ⟨P j[t − T, t](t)⟩ (7)
ˆP i,j(t) = P j(t) − ⟨P j[t − 2T, t− T ](t)⟩ + ⟨P j[t − T, t](t)⟩ (8)
These equations apply foraF 0 = 0, 1, 2, respectively. These actions correspond to strategies encom-
passing mean-reversion, utilization of moving averages, and tracking trends. Consequently, actions
aF 0 and aF 1 are intimately associated with the realm of technical analysis, withaF 0 dictating the
selection of the econometric forecasting approach andaF 1 defining the duration of these forecasts.
The third action,aF 2 , associate the chosen technical forecastˆP i,j(t) with the agent’s fundamental
valuation Bi,j(t), giving rise to the agent’s projection:
H i,j(t) = α ˆP i,j(t) + (1 − α)Bi,j(t) (9)
In this equation,α ∈ R is selected based on the agent’s reflexivityρi. If ρi ≤ 50%, then α assumes
the values 0, ρi, 2ρi for aF 2 = 0, 1, 2, respectively. Conversely, ifρi > 50%, α takes on the values
2ρi − 1, ρi, 1 for aF 2 = 0, 1, 2. Consequently, whenaF 2 = 2, the agent adapts the weight allocated to
its chartist versus fundamentalist valuation methods.
Returns RF: Subsequently, the reinforcement learning algorithm F i computes the percentage
divergence between the agent’s previous asset price predictionH i,j(t − τ i) made τ i time steps earlier,
and the present actual priceP j(t):
|H i,j(t − τ i) − P j(t)|
P j(t) (10)
13

Lussange, Vrizzi, Palminteri, Gutkin
This value is logged at each time step, organized in ascending order, and sustained for a duration
equivalent to the agent’s memory intervalhi. The percentile rank of this value at time stept is
employed to assign a discrete return valuerF from the setRF = 4, 2, 1, −1, −2, −4, corresponding
to the intervals[0%, 5%(, [5%, 25%(, [25%, 50%(, [50%, 75%(, [75%, 95%(, [95%, 100%], respectively.
Policy πF: Thereinforcementlearningmechanismundergoesregularpolicyrefinement πF t (sF t − τ i, aF t − τ i)
at each time stept. The adjustment of this policy is influenced by the learning rateβ. To enhance
the likelihood of selecting the optimal actionaF ⋆ in the statesF, a set of equations is iteratively
applied |rF | times. The goal is to increase the probability of this optimal action relative to all other
possible actions, denoted∀aF ̸= aF ⋆ as:
πF t+1(sF , aF ⋆) = πF t (sF , aF ⋆) + β  1 − πF t (sF , aF ⋆)  (11)
πF t+1(sF , aF ) = πF t (sF , aF ) − βπ F t (sF , aF ) (12)
Additionally, the algorithm incorporates an off-policy approach at intervals ofτ i/Tm + 2. This
approach calculates the action that should have ideally been taken byF i τ i steps earlier, using
current price and forecast accuracy. The policyπF is then updated using the learning rateβ and
applied |rF | = 4 times to adapt to the newly identified optimal action.
3.4 Agent second RL algorithm
This secondary approach allows the agent to dynamically assess the evolution of asset prices, as
initially determined by the primary algorithm (sT 0 ). It also evaluates market volatility (sT 1 ), the
status of risk-averse assets (sT 2 ), the current quantity of crypto assets held (sT 3 ), and the volume
of executed trades (sT 4 ). Utilizing this collected information, the agent fine-tunes its investment
strategies. It makes decisions on whether to hold, buy, or sell crypto assets in specific quantities (aT 0 )
and determines the transaction price in response to market supply and demand dynamics (aT 1 ).
States S T: The agent’s decision-making process in algorithmT i relies on a statesT within the set
S T = sT 0 , sT 1 , sT 2 , sT 3 , sT 4 . This set encompasses a108-dimensional space, wheresT 0 , sT 1 , and sT 4 can
take on values from the set0, 1, 2, and sT 2 , sT 3 from 0, 1.
– The agent calculates the ratioµ = ( H i,j(t) − P j(t))/P j(t) and records it in eitherµ− or
µ+ time series, based on its negativity or positivity, respectively. These series are sorted
in ascending order and capped to match the agent’s memory spanhi. The agent’s current
percentile value µ− in µ− at time t assigns sT 0 = 0 if it’s under 95%, and sT 0 = 1 if not.
Likewise, µ+ in µ+ determines sT 0 to be 1 if under 5%, and sT 0 = 2 otherwise. The state sT 0
thus represents the econometric predictionµ from the preceding algorithmF i, indicating a
decline, stability, or increase in assetj prices in the forthcomingτ i time steps.
– The agent records the previously computed varianceσ2 L of asset pricesP j(t) in a time series
over the interval[t − 3τ i, t]. This series undergoes sorting and truncation to align with the
agent’s memory capacityhi. At timet, the agent’s current percentile value determinessT 1 as
follows: sT 1 = 0 if the percentile is below33%, sT 1 = 2 if it’s above67%, and sT 1 = 1 otherwise.
This aids the agent in assessing long-term asset price volatility.
– The agent setssT 2 = 0 if its risk-free asset valueAi bonds(t) falls below 60% of its initial value
Ai bonds(t = 0), and sT 2 = 1 otherwise. This helps the agent monitor its risk-free asset size for
crafting appropriate investment strategies.
14

Modelling crypto markets by multi-agent reinforcement learning
– The agent assignssT 3 = 0 if the current value of its crypto asset holdingsAi equity(t) is less than
60% of the starting valueAi equity(t = 0), and sT 3 = 1 otherwise. This process assists the agent
in tracking the value of its crypto asset holdings for strategic decision-making.
– The agent logs trading volumesV j(t) at each time step in a series, which is subsequently
sorted in ascending order and truncated to match the agent’s memory periodhi. The current
percentile value at timet determines sT 4 as follows: sT 4 = 0 if V j(t) = 0, sT 4 = 1 if below 33%,
and sT 4 = 2 otherwise. This information informs the agent about market activity levels and
aids in setting appropriate bid or ask prices for transactions.
Actions AT: Within the context of the reinforcement learning modelT i, we introduce a set of
actions denoted byAT = aT 0 , aT 1 , where each actionaT belongs to this set. This set of actions is
characterized by a dimensionality of9. Both actions, aT 0 and aT 1 , can take on discrete values from
the set 0, 1, 2, and their values are determined through a process of direct policy search, which is
elaborated upon below. The representation of actionaT 0 serves a dual purpose: it signifies both the
quantity of crypto assets and the type of transaction order (sell, hold, or buy) that the agent chooses
to place in the order book. In this framework, each agent adheres to a long-only trading strategy,
involving the acquisition of crypto assets at a specific price, holding them for a predefined duration,
and eventually selling them, ideally at a higher price. The role of actionaT 1 is to express the agent’s
willingness to be flexible regarding the trading price. These actions depend on the agent’s evaluation
of asset j’s price, as determined by the initial algorithmF i. The agent’s bid price P i,jbid(t) is
formulated as follows:
P i,jbid(t) = min[H i,j(t), Pj(t)] + giW j(t − 1) (13)
P i,j bid(t) = min[H i,j(t), Pj(t)] (14)
P i,j bid(t) = min[H i,j(t), Pj(t)] − giW j(t − 1) (15)
for different values ofaT 1 (namely, 0, 1, and 2 respectively), distinct scenarios emerge. The symbolgi
signifies the trading gesture of the agent, whileW j(t − 1) represents the previous time step’s market
spread for assetj. Consequently, the term±giW j(t − 1) captures the agent’s adaptable response to
trading conditions, influenced by factors likeW j(t − 1) and the trading volumes denoted bysT 4 . The
agent’s ask price,P i,j ask(t), is formulated as follows:
P i,j ask(t) = max[H i,j(t), Pj(t)] − giW j(t − 1) (16)
P i,j ask(t) = max[H i,j(t), Pj(t)] (17)
P i,j ask(t) = max[H i,j(t), Pj(t)] + giW j(t − 1) (18)
considering the scenario where aT 1 takes on the values0, 1, and 2 respectively. In this context,
Qi,j(t) represents the quantity of assetj held by investori at time t. Specifically, when aT 0 = 0,
it signifies that investori is placing a sell order for their entire assetj holding at the asking price
P i,j ask(t). Conversely, foraT 0 = 1, investor i opts to maintain their existing position and not execute
15

Lussange, Vrizzi, Palminteri, Gutkin
any transactions. Lastly, whenaT 0 = 2, it signifies a buy order, with the investor acquiring a quantity
of crypto assetj determined by the formulaAi bonds(t)/[P i,j ask(t)J] at the bid priceP i,j bid(t).
Filter FunctionGi: The decision-making process of investori regarding sending a transaction order to
the order book at time stept is dictated by the output of the functionGi. This function is designed
to introduce a delay in order placement to optimize timing. To achieve this,Gi maintains a time
series, recording the maximum value of the action-value functionarg maxa Qt(s, a) at each time step,
which is then sorted in ascending order. The decision to execute a trade is determined by comparing
the current percentilepQ(t) of this series with the ratio of time elapsed since the last transaction
ki,j(t) to the individual trading windowwi of the investor. An order is dispatched to the order book
only if the conditionpQ(t) < ki,j(t)/wi is met. It is important to note that whileGi governs the
initiation of trades, it does not apply to exit strategies, which are executed based on the investor’s
predetermined investment horizonτ i.
Returns RT: The algorithm T i calculates the change in cash flow resulting from the current net
asset value of investori’s portfolio, compared to what it would have been if the actions takenτ i time
steps earlier had not occurred. Mathematically, this is expressed as:
Qi,j OB(t − τ i)[P j(t) − P i,j OB(t − τ i)] (19)
In this equation, Qi,j OB(t − τ i) and P i,j OB(t − τ i) represent the quantity and price of crypto assetj
cleared in the order book at timet − τ i for investor i and their trading counterpart. These values
may differ from the initial values sent by investori due to partial order fulfillment and the order
book’s pricing mechanism, which sets the transaction price at the mid-price in conjunction with
the counterparty’s order price. These values are logged in a time series at each time step, sorted
in ascending order, and truncated to maintain a length corresponding to the investor’s memory
interval hi. The percentile of this value at timet determines the discrete return valuerT in the set
RT = 4, 2, 1, −1, −2, −4, associated with the intervals[0%, 5%], [5%, 25%], [25%, 50%], [50%, 75%],
[75%, 95%], and [95%, 100%].
Policy Update MechanismπT: In the final phase, the reinforcement learning algorithm adjusts its
policy πT t (sT t−τ i , aT t−τ i ) after every τ i time steps following each transaction conducted by the agent.
This adaptation is driven by the agent’s learning rateβ. The following equations are iterated|rT |
times, with the goal of giving priority to a specific action, denoted asaT ⋆, in state sT. This is
achieved by increasing the policy probability associated withaT ⋆ over other actions, denoted as
∀aT ̸= aT ⋆:
πT t+1(sT , aT ⋆) = πT t (sT , aT ⋆) + β[1 − πT t (sT , aT ⋆)] (20)
πT t+1(sT , aT ) = πT t (sT , aT ) − βπ T t (sT , aT ) (21)
Moreover, the algorithm incorporates an off-policy mechanism everyτ i/Tm + 2 time steps. This
mechanism calculates the optimal action thatT i should have takenτ i time steps earlier, taking into
account the realized price and forecast accuracy. Subsequently, it updates the policyπT using the
agent’s learning rateβ. This update process is repeated|rT | = 4 times, as the associated action is
considered optimal.
It is essential to emphasize that both algorithmsF and T employ discretized and handcrafted
action-state spaces. This choice is motivated by the necessity to conserve computational resources,
16

Modelling crypto markets by multi-agent reinforcement learning
but also addresses a certain limitation in applying MAS to financial research, which is the substantial
computational power requirement. Additionally, the fundamental basis for defining such state and
action spaces is rooted in theFundamental Theorem of Asset Pricing[111], where present asset prices
are estimated from time-discounted future price expectations. In a similar vein, our reinforcement
learning framework for the agent comprises a forecasting componentF i and a trading component
T i, a design approach reminiscent of recent models such as [80] (see Section 3.3 for further details).
3.5 Calibration to real data
ModelAssumptions : TheSYMBAmodelisfoundedontwocoreassumptions: i-thatthebehavior
of the simulated agents accurately reflects that of real-world investors, and ii- that the transaction
limit orders simulated in the order book faithfully represent the dynamics and characteristics of actual
crypto market orders. Regarding the former, our approach simplifies the interaction of any agent,
regardless of its behavior or strategy, into three distinct possibilities: buying, selling, or holding assets
(a long-only strategy). Concerning the latter, it is worth noting that the dynamics of order books
have been extensively documented in the literature [112], including for crypto markets [113, 114],
allowing for a rigorous design.
Model limitations : Alongside our fundamental assumptions, we also acknowledge several
constraints and consistency challenges that are inherent to all financial MAS: i- Dependency on the
generation of virtual fundamentalsT j(t) (notably, wasn’t itBi,j(t) regardless?). ii- The absence
of diversification across various asset classes. iii- The lack of diverse trading strategies available
on Binance, such as short-selling, leveraging, derivatives, metaorders, market orders, and more. iv-
Neglecting intraday and seasonal market effects. v- Disregarding legal and regulatory constraints,
which furthermore have been very dynamic over the considered time period of2018 − 2022. While
some of these limitations may pose challenges, their impact and importance are intrinsic to nearly
all econometric and modeling approaches within the realm of quantitative finance. Furthermore,
modeling market activity through a market microstructure derived from a centralized order book
that processes transaction orders from multiple trading agents aligns closely with a CEX like Binance,
making it empirically relevant.
Training and testing data : Our model was calibrated to authentic crypto market data1. To
achieve this, we employed high-quality, industry-standard daily closing prices and trading volumes
from CryptoTick, for 153 crypto assets listed on Binance. This dataset covers the period from
September 27th, 2018, to September27th, 2022. As mentioned in Section 3, these records encompass
the date, opening price, highest price, lowest price, closing price, and trading volume for each day.
Notably, these figures originate directly from Binance and are not an amalgamation of data from
smaller exchanges (i.e., consolidated data). In our analysis of market microstructure, we only included
crypto assets that sustained continuous trading during the specified timeframe. Consequently, our
initial crypto asset universe was reduced to153 stocks. We tuned the MAS hyperparameters using a
random sample comprising half of these stocks as a training set. Remarkably, we observed a high
level of statistical stability within the training set when compared to the other half, as shown with
the logarithmic price returns distributions of these two sets on Fig. 5.
Finally there are three major features which are proper to crypto markets that should here be taken
into account, when considering these results: i- There are two main ways to assess the value of a
given crypto asset, namely either in fiat money (USD, EUR, GBP, etc.) or in a different crypto
currency (BTC, ETH, BNB, etc.). Given the historical central role and major influence played by
1. These computations were carried out on a Mac Pro equipped with a 3.5 GHz 6-Core Intel Xeon E5 processor and
16 GB of 1866 MHz DDR memory
17

Lussange, Vrizzi, Palminteri, Gutkin
Figure 5: Comparative Distribution of Logarithmic Price Returns: The red curve represents the
Binance training set, while the blue curve represents the Binance testing set.
Bitcoin on all the other crypto assets prices in those markets, studying the microstructure of crypto
assets in BTC as we did here, or in USD can be vastly different tasks. ii- Contrary to classical stock
markets, trading and transactions in crypto markets run24/7. iii- just as Over-The-Counter (OTC)
derivatives and other synthetic replications of stocks like Contract for Differences (CFD) proposed
by brokers, a vast amount of crypto assets are not traded via a CEX like Binance but Decentralized
EXchanges (DEX), with their own decentralized book dynamics.
Optimization and hyperparameters : The hyperparameters subjected to calibration encompass
the number of agents (I), the agent transaction gesture factor (ζ i ∈ N, which scales the gesture
parameter gi initialized for each agent att = 0), the parameterν governing the cointegration accuracy
of each agent approximating the fundamental time seriesT j, and the drawdown threshold (the
upper limit of the drawdown, initialized att = 0 for each agent). We assessed various combinations
of hyperparameters against the training dataset, and the specifics are outlined in Table 1. The
optimization procedure entailed a maximum of480 simulations, each comprisingS = 20 runs to
ensure statistical reliability.
Table 1: Model Hyperparameters and Ranges for Training: Lower Bound (Low), Upper Bound
(High), and Increment Step (Step).
Hyperparameter Low High Step
Number of Agents (I) 500 5500 1000
Gesture Scalar (ζ i) 1.0 3.0 0.5
Cointegration accuracy (ν) 9 12 1
Drawdown Threshold (L) 10 90 20
Exploring sensitivity : Throughout the optimization process, we conducted a sensitivity exam-
ination to evaluate the model’s response to diverse hyperparameter ranges. The objective was to
pinpoint regions of non-linearity concerning the alignment with actual data. Notably, we found that
18

Modelling crypto markets by multi-agent reinforcement learning
augmenting the count of agents (I) displayed a linear correlation with the reduction of short-term
price fluctuations. Additionally, increasing the values of the gesture scalar (ζ i) and the cointegration
accuracy (ν) exhibited a linear escalation in absolute daily price returns. Remarkably, large drawdown
thresholds (L > 30%) showed minimal impact on agent survivability rates.
Comparative model analysis : The existing literature, as exemplified in [115], studies the
substitution of market dynamics for individual rationality. It explores whether markets eliminate
irrational participants or whether individuals adapt and learn market rules. Figure 6 illustrates
learning curves for agents, providing a basis for model comparison, especially when compared
to contemporary order book models integrated with reinforcement learning [80], and the earlier
generation of MAS featuring zero-intelligence agents [115], which serve as baseline references.
Figure 6: Towards the end of90% of the total simulation period, our objective is to compare the
top-performing 10% of agents in our MAS crypto market simulator, represented by the blue curves,
with the top10% performers in a market simulated with randomly trading noise agents, shown by
the red curves. This comparison is based on their performance during the remaining10% of our
overall simulation duration, utilizing averaged equity curves as their year-to-date returns across20
simulations (left), and the averaged, sorted annual returns from each of these20 simulations (right).
These simulations are generated using the following parameters:I = 500, J = 1, and T = 2875.
4. Results
In this section, we present a comprehensive set of critical market microstructure indicators relevant
to the calibration of our SYMBA model. Figures 7 through 14 demonstrate the qualitative agreement
in shape between the curves generated by our model and those obtained from actual stock market
data. Unless otherwise specified, the following results stem from simulations conducted withI = 500
agents, J = 1 traded asset, T = 1453 time steps per simulation, equivalent to four years of trading
days, and a total ofS = 20 simulation runs.
To begin with, Fig. 7 illustrates the distribution of logarithmic returns of priceslog[P (t)/P (t − 1)]
for real (dashed black curve) and simulated (continuous red curve) data, displaying a close match
between the simulated and real logarithmic price returns. One should notice the limited variability
of extreme events in the tails of the distribution, as highlighted on the logarithmic y-axis. In Fig. 8,
we plot the distributions of price volatilities over different time intervals: two weeks (black), three
months (red), and one year (green), for both real (dashed curves) and simulated (continuous curves)
data. These volatilities are computed as standard deviations of prices normalized by the price itself,
σ/P (t). Although the general shapes of the simulated and real data curves are similar, we find a shift
or translation in between them. First, we observe that emulating real volatilities at longer time scales
is more challenging, likely due to our real data sample covering a unique and exceptional market
period during these years, namely the2020 − 2022 crypto market bubble and crash. Secondly, we
19

Lussange, Vrizzi, Palminteri, Gutkin
generally find lower volatility events, at all time scales, for the simulated data than for the Binance
data. This may be explained by the fact that a significant portion of cryptocurrency trading was
driven during this time period by speculative investors looking for quick returns, notably during the
pandemics. This speculative behavior, often based on market sentiment rather than fundamental
value of the crypto assets, can lead to rapid price swings.
We then want to check on the micro-tructure of the price volatility and traded volume, with the
clustering features mentioned in Section 1 in mind. In Fig. 10, we show the distributions of
correlations in the trading volumes between distinct intervals[t − ∆, t] and [t − 2∆, t− ∆] at each
time step t, considering values of∆ corresponding to two weeks (black), three months (red), and one
year (green). Again, this is for both real (dashed curves) and simulated (continuous curves) data.
One can see the great fits of the simulation to real data, highlighting the aforementioned stylized
fact of volume clustering. However, one should note the presence of numerous extra zero volume
correlations in simulated data wrt. real data, which can be explained similarly as before. Fig. 11
illustrates the simulation data (shown as the red continuous curve) emulating the actual Binance
data (represented as the black dashed curve) wrt. the distribution of price volatility correlations
between distinct time intervals[t − 2Tw, t] and [t − 4Tw, t− 2Tw] at each time stept. Although we
see a strong correspondance in fit shapes, notably in its asymmetry, there is an even larger amount
of zero autocorrelation events in simulated data. Apart from the lack of arbitrage efficiency in crypto
markets seen before in Fig. 9, this surge can be explained by the granularity of the model data,
which cannot capture all the intraday events of the real data. Simulated data might thus smooth out
certain price variations present in real data, thereby affecting the correlation structure.
Another key topic of financial quantitative research is that of market memory and efficiency. An
important issue for the model’ simulated data is hence to check on its emulation of prices autocor-
relations. Firstly, Fig. 9 presents the distributions of correlations in the price logarithmic returns
between distinct intervals[t − ∆, t] and [t − 2∆, t− ∆] at each time stept, considering values of
∆ corresponding to two weeks (black), three months (red), and one year (green). This analysis
is conducted for both real (dashed curves) and simulated (continuous curves) data. Despite the
overall good fit, especially regarding the general shape of the distributions, one should note the
presence of numerous extra zero autocorrelations in simulated data. We suggest that this difference
with real data could be attributed to a still-present lack of arbitrage efficiency in crypto markets,
especially during the early period of the2018 − 2022 interval. In Fig. 12, the distributions of the
means of the correlations in logarithmic price returns at each time stept are presented for simulated
data (continuous curves) and actual data (dashed curves), between time intervals[t − Tw, t] and
[t − Tw − ∂, t− ∂]. This is for shifts∂ ranging from one day (black), to two days (red), to five days
(green). Again, the shapes of the simulated curves fit very well the real data, but one can notice the
surplus of zero correlations for the simulated data, for reasons akin to the previous point. Fig. 13
displays the mean correlations of logarithmic returns in prices at each time stept between intervals
[t − Tw, t] and [t − Tw − ∂, t− ∂] for shifts ∂ = 1, 2, 3, 4, 5. This comparison is made between real
data (in black) and simulated data (in red). Similarly, Figure 14 presents a close fit analysis for
wider intervals of[t − 2Tw, t] and [t − 2Tw − 2∂, t− 2∂]. These statistical insights are crucial for
comprehending that our model generates a price microstructure devoid of arbitrage opportunities
while displaying the typical decay of market memory through agent learning. In simpler terms, agents
learn to exploit short-term causal structures present in historical prices, thereby rending the market
more efficient.
To summarize, the calibration process shows our MARL model ability to replicate the distribution of
logarithmic price returns (Fig. 7), the distribution of normalized price volatilities at different time
scales (Fig. 8), and the autocorrelations of trading volumes (Fig. 10) and log-price returns across
various time scales and intervals (Fig. 9, 11 to 14). The stylized facts mentioned in Section 1 of
non-gaussian price returns, clustered volatilities and volumes, and decaying autocorrelations are thus
20

Modelling crypto markets by multi-agent reinforcement learning
re-enacted by SYMBA, and fit the real data. Notably, these autocorrelation metrics play a pivotal
role in the calibration procedure as they pertain to the absence of arbitrage opportunities and the
market’s memory, both being fundamental attributes of financial markets. In simpler terms, beyond
the stylized facts, the synthetic data generated by the model should not exhibit discernible price
patterns that are more exploitable for trading than those found in real-world data. Additionally, it is
worth highlighting that our MARL simulator emulates the dynamics of real stock markets during
the very volatile and active regime of crypto markets over the period of2018 to 2022, encompassing
periods of economic downturns and growth, as well as the COVID-19 era.
That being said, there are several avenues for improving the model’s performance and characteristics.
Firstly, we should be further addressing the tail distribution fit of long-term price volatilities, as
evident in Fig. 8. These tails present a formidable challenge to capture, given their association
with jump diffusion processes inherent to volatile events affecting very diverse crypto assets (e.g.
stable coins, industrial tokens, cryptocurrencies), and as aforementioned, the specific era of COVID-
19.Secondly, we should be further investigating the peak in zero autocorrelations observed in real
price returns and volatility, showcased in Figs. 9 and 10, and especially Fig. 11 and 12. As said, this
phenomenon may be attributed to the simulator’s lack of consideration for intraday crypto market
activities. It could also potentially be explained by a remaining lack of maturity of crypto markets in
terms of market efficiency and no-arbitrage.
Figure 7: Comparative Distribution of Logarithmic Price Returns: The dashed black curve represents
real data, while the continuous red curve represents simulated data. These simulations were generated
using parameters I = 500, J = 1, T = 1453, and S = 20.
5. Discussion
In this study, we have demonstrated how our MARL model SYMBA can replicate critical aspects
of crypto market dynamics, as evidenced through its calibration with actual Binance data from
2018/09/27 to 2022/09/27. Our results offer valuable insights into the complexity and behavior of
crypto markets, highlighting the model’s ability to emulate key market characteristics such as non-
normal returns, volume clustering, and decaying price log-returns autocorrelations. These findings
underscore the importance of considering the unique attributes of crypto markets, particularly their
21

Lussange, Vrizzi, Palminteri, Gutkin
Figure 8: Volatility Distribution at Different Time Lags: This figure illustrates the distribution of
volatilities, computed at two weeks (black), three months (red), and one year (blue) intervals for
both real (dashed curves) and simulated (continuous curves) data. The simulations were generated
using parameters I = 500, J = 1, T = 1453, and S = 20.
Figure 9: Autocorrelations of Logarithmic Price Returns: This figure presents the distribution of
autocorrelations of logarithmic returns of prices at each time stept between intervals[t − ∆, t] and
[t − 2∆, t− ∆] over lags∆ of two weeks (black), three months (red), and one year (blue) intervals for
both real (dashed curves) and simulated (continuous curves) data. The simulations were generated
using parameters I = 500, J = 1, T = 1453, and S = 20.
22

Modelling crypto markets by multi-agent reinforcement learning
Figure 10: Autocorrelations of Trading Volumes: This figure presents the distribution of autocorre-
lations of trading volumes at each time stept between intervals[t − ∆, t] and [t − 2∆, t− ∆] over
lags ∆ of two weeks (black), three months (red), and one year (blue) intervals for both real (dashed
curves) and simulated (continuous curves) data. The simulations were generated using parameters
I = 500, J = 1, T = 1453, and S = 20.
Figure 11: Autocorrelations of Two Weeks-Interval Volatilities: This figure illustrates the distribution
of autocorrelations of two weeks-interval volatilities at each time stept between intervals[t − ∆, t] and
[t − 2∆, t− ∆] for ∆ = 2Tw, for both real (dashed black curve) and simulated (continuous red curve)
data. The simulations were generated using parametersI = 500, J = 1, T = 1453, and S = 20.
23

Lussange, Vrizzi, Palminteri, Gutkin
Figure 12: Means of Autocorrelations of Logarithmic Price Returns with Various Time Shifts: This
figure displays the means of autocorrelations of logarithmic returns of prices at each time stept
between intervals[t − Tw, t] and [t − Tw − ∂, t− ∂], for shifts∂ = [1, 2, 5]. The data is shown in both
real (blue) and simulated (red) scenarios. The simulations were generated using parametersI = 500,
J = 1, T = 1453, and S = 20.
Figure 13: Means of Autocorrelations of Logarithmic Price Returns with Extended Time Shifts:
This figure demonstrates the means of autocorrelations of logarithmic returns of prices at each time
step t between intervals [t − Tw, t] and [t − Tw − ∂, t− ∂], for shifts∂ = [1, 2, 3, 4, 5]. The data is
presented in both real (blue) and simulated (red) scenarios. The simulations were generated using
parameters I = 500, J = 1, T = 1453, and S = 20.
24

Modelling crypto markets by multi-agent reinforcement learning
Figure 14: Means of Autocorrelations of Logarithmic Price Returns with Extended Time Shifts:
This figure demonstrates the means of autocorrelations of logarithmic returns of prices at each time
step t between intervals[t − 2Tw, t] and [t − 2Tw − 2∂, t− 2∂], for shifts∂ = [1, 2, 3, 4, 5]. The data is
presented in both real (blue) and simulated (red) scenarios. The simulations were generated using
parameters I = 500, J = 1, T = 1453, and S = 20.
high volatility, decentralized nature, and diverse factors impacting fundamental valuation, in the
financial modeling of crypto assets. The successful calibration of SYMBA to real-world crypto data,
despite certain limitations, represents a significant step forward in the understanding and analysis
of such markets. It demonstrates the potential of agent-based models, enhanced by reinforcement
learning, to capture complex market phenomena that traditional financial models may struggle to
represent.
However, our analysis also identified areas for improvement in the model. The observed discrepancies
in the tail distribution of long-term price volatilities and the surplus of zero autocorrelations in
logarithmic price returns within the simulated data point to the need for further refinement. These
issues may stem from the model’s current limitations in capturing the very particular market regimes
that were those of the2018 − 2022 period, with its specific bubble and crash, together with the
effects of the COVID-19 era. Another issue may arise from granularity of our model, and the specific
microstructure of crypto markets stemming from the intraday activity, which is actually a24/7
trading activity. Addressing these challenges will require enhancing the decision-making processes of
market participants, an especially the impact of exogenous factors such as global economic events
akin to those aforementioned. Looking ahead, future research should focus on refining the model to
better account for the diverse and rapidly evolving nature of crypto assets and market conditions.
This includes incorporating more granular data, such as intraday trading activities, and improving
the model’s ability to simulate market responses to external shocks and policy changes. Additionally,
taking into account the ever-increasing impact of new regulations in crypto markets, could further
enhance the model’s realism.
In conclusion, our study contributes to the growing body of research on crypto markets, offering a
novel approach to understanding these complex and dynamic systems. By leveraging the power of
agent-based modeling and reinforcement learning, SYMBA provides a framework for future potential
applications in crypto markets wrt. risk management, regulatory policy development, and investment
strategy optimization. The insights gained from this research not only advance our theoretical
25

Lussange, Vrizzi, Palminteri, Gutkin
understanding of financial markets but also have practical implications for investors, policymakers,
and researchers in the field.
Acknowledgement
We graciously acknowledge this work to have been supported by the ANR (Agence nationale de la
Recherche) CogFinAIgent. Parts of this research were also carried out within the European Union’s
Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement
No 945304 - Cofund AI4theSciences hosted by PSL∗ University.
26

Modelling crypto markets by multi-agent reinforcement learning
References
[1] Johann Lussange, Ivan Lazarevich, Sacha Bourgeois-Gironde, Stefano Palminteri, and Boris
Gutkin. Modelling stock markets by multi-agent reinforcement learning. Computational
Economics, pages 1–35, 2020.
[2] Mawuli Segnon and Stelios Bekiros. Forecasting volatility in bitcoin market.Annals of Finance,
16(3):435–462, 2020.
[3] Nikolaos Antonakakis, Ioannis Chatziantoniou, and David Gabauer. Cryptocurrency mar-
ket contagion: Market uncertainty, market complexity, and dynamic portfolios.Journal of
International Financial Markets, Institutions and Money, 61:37–51, 2019.
[4] Julien Prat, Vincent Danos, and Stefania Marcassa. Fundamental pricing of utility tokens.
working paper, 2021.
[5] Marcin Wątorek, Stanisław Drożdż, Jarosław Kwapień, Ludovico Minati, Paweł Oświęcimka,
and Marek Stanuszek. Multiscale characteristics of the emerging global cryptocurrency market.
Physics Reports, 901:1–82, 2021.
[6] Richard K Lyons and Ganesh Viswanath-Natraj. What keeps stablecoins stable?Journal of
International Money and Finance, 131:102777, 2023.
[7] Hemang Subramanian. Security tokens: architecture, smart contract applications and illustra-
tions using safe.Managerial Finance, 46(6):735–748, 2020.
[8] Yang Xiao, Ning Zhang, Wenjing Lou, and Y Thomas Hou. A survey of distributed consensus
protocols for blockchain networks.IEEE Communications Surveys & Tutorials, 22(2):1432–1465,
2020.
[9] Katya Malinova and Andreas Park. Tokenomics: when tokens beat equity.Management Science,
69(11):6568–6583, 2023.
[10] Lin William Cong, Ye Li, and Neng Wang. Tokenomics: Dynamic adoption and valuation.The
Review of Financial Studies, 34(3):1105–1155, 2021.
[11] Satoshi Nakamoto et al. Bitcoin.A peer-to-peer electronic cash system, 21260, 2009.
[12] Ali Sunyaev and Ali Sunyaev. Distributed ledger technology.Internet computing: Principles of
distributed systems and emerging internet-based technologies, pages 265–299, 2020.
[13] Jie Xu, Cong Wang, and Xiaohua Jia. A survey of blockchain consensus protocols.ACM
Computing Surveys, 2023.
[14] Ankit Gangwal, Haripriya Ravali Gangavalli, and Apoorva Thirupathi. A survey of layer-two
blockchain protocols. Journal of Network and Computer Applications, 209:103539, 2023.
[15] Arman Eshraghi. Approaches to cryptocurrency valuation. In The Emerald Handbook on
Cryptoassets: Investment Opportunities and Challenges, pages 171–184. Emerald Publishing
Limited, 2023.
[16] Matteo Benetton and Giovanni Compiani. Investors’ beliefs and cryptocurrency prices.The
Review of Asset Pricing Studies, page raad015, 2024.
[17] Eyal Beigman, Gerard Brennan, Sheng-Feng Hsieh, and Alexander J Sannella. Dynamic princi-
pal market determination: Fair value measurement of cryptocurrency.Journal of Accounting,
Auditing & Finance, 38(4):731–748, 2023.
27

Lussange, Vrizzi, Palminteri, Gutkin
[18] Constantin Gurdgiev and Daniel O’Loughlin. Herding and anchoring in cryptocurrency markets:
Investor reaction to fear and uncertainty.Journal of Behavioral and Experimental Finance, 25:
100271, 2020.
[19] J. Lussange, A. Belianin, B. Gutkin, and S. Bourgeois-Gironde. Learning and cognition in
financial markets: A paradigm shift for agent-based models.Proceedings of SAI Intelligent
Systems Conference, pages 241–255, 2020.
[20] H.-C. Xu, W. Zhang, X. Xiong, and W.-X. Zhou. An agent-based computational model for
china’s stock market and stock index futures market.Mathematical Problems in Engineering,
2014:563912, 2014.
[21] R. Boero, M. Morini, M. Sonnessa, and P. Terna.Agent-based models of the economy, from
theories to applications. Palgrave Macmillan, 2015.
[22] Michael Benzaquen and Jean-Philippe Bouchaud. A fractional reaction–diffusion description of
supply and demand.The European Physical Journal B, 91(23), 2018.
[23] E. Way and M. P. Wellman. Latency arbitrage, market fragmentation, and efficiency: a
two-market model. Proceedings of the fourteenth ACM conference on Electronic commerce,
pages 855–872, 2013.
[24] M. Aloud. Agent-based simulation in finance: design and choices.Proceedings in Finance and
Risk Perspectives ‘14, 2014.
[25] F. H. Westerhoff. The use of agent-based financial market models to test the effectiveness of
regulatory policies. Jahrbucher Fur Nationalokonomie Und Statistik, 228(2):195, 2008.
[26] Stanislao Gualdi, Marco Tarzia, Francesco Zamponi, and Jean-Philippe Bouchaud. Tipping
points in macroeconomic agent-based models.Journal of Economic Dynamics and Control, 50:
29–61, 2015.
[27] S. Barde. A practical, universal, information criterion over nth order markov processes.
University of Kent, School of Economics Discussion Papers, 04, 2015.
[28] G. Kim and H. M. Markowitz. Investment rules, margin and market volatility.Journal of
Portfolio Management, 16:45–52, 1989.
[29] M. Levy and S. Solomon. Power laws are logarithmic boltzmann laws.International Journal
of Modern Physics C, 7:595–601, 1996.
[30] M. Levy, H. Levy, and S. Solomon. A microscopic model of the stock market: cycles, booms,
and crashes. Economics Letters, 45:103–111, 1994.
[31] M. Levy, H. Levy, and S. Solomon. Microscopic simulation of the stock market: the effect of
microscopic diversity.Journal de Physique I, 5:1087–1107, 1995.
[32] M. Levy and S. Solomon. Dynamical explanation for the emergence of power law in a stock
market model. International Journal of Modern Physics C, 7:65–72, 1996.
[33] M. Levy, N. Persky, and S. Solomon. The complex dynamics of a simple stock market model.
International Journal of High Speed Computing, 8:93–113, 1996.
[34] M. Levy, H. Levy, and S. Solomon. New evidence for the power-law distribution of wealth.
Physica A, 242:90–94, 1997.
28

Modelling crypto markets by multi-agent reinforcement learning
[35] M. Levy, H. Levy, and S. Solomon.Microscopic simulation of financial markets: from investor
behavior to market phenomena. Academic Press, New York, 2000.
[36] R. Cont and J. P. Bouchaud. Herd behavior and aggregate fluctuations in financial markets.
Macroeconomic Dynamics, 4:170–196, 2000.
[37] Sorin Solomon, Gerard Weisbuch, Lucilla de Arcangelis, Naeem Jan, and Dietrich Stauffer.
Social percolation models.Physica A, 277(1):239–247, 2000.
[38] T. Lux and M. Marchesi. Scaling and criticality in a stochastic multi-agent model of a financial
market. Nature, 397:498–500, 1999.
[39] T. Lux and M. Marchesi. Volatility clustering in financial markets: a microsimulation of
interacting agents.Journal of Theoretical and Applied Finance, 3:67–70, 2000.
[40] R. Donangelo, A. Hansen, K. Sneppen, and S. R. Souza. Modelling an imperfect market.
Physica A, 283:469–478, 2000.
[41] R. Donangelo and K. Sneppen. Self-organization of value and demand.Physica A, 276:572–580,
2000.
[42] P. Bak, S. Norrelykke, and M. Shubik. Dynamics of money.Physical Review E, 60:2528–2532,
1999.
[43] P. Bak, S. Norrelykke, and M. Shubik. Money and goldstone modes.Quantitative Finance, 1:
186–190, 2001.
[44] Z. F. Huang and S. Solomon. Power, lévy, exponential and gaussian-like regimes in autocatalytic
financial systems. European Physical Journal B, 20:601–607, 2000.
[45] J.A. Lipski and R. Kutner. Agent-based stock market model with endogenous agents’ impact.
arXiv:1310.0762, 2013.
[46] M. Potters and J.-P. Bouchaud. More stylized facts of financial markets: Leverage effect and
downside correlations. Physica A, 299:60–70, 2001.
[47] V. Plerou, P. Gopikrishnan, L. A. Amaral, M. Meyer, and H. E. Stanley. Scaling of the
distribution of fluctuations of financial market indices.Physical Review E, 60(6):6519, 1999.
[48] M. Cristelli. Complexity in Financial Markets. Springer, 2014.
[49] R. Cont. Empirical properties of asset returns: stylized facts and statistical issues.Quantitative
Finance, 1:223–236, 2001.
[50] J.P. Bouchaud, R. Cont, and M. Potters.Scale Invariance and Beyond, Proc. CNRS Workshop
on Scale Invariance, Les Houches. Springer, 1997.
[51] Z. Ding, R. Engle, and C. Granger. A long memory property of stock market returns and a
new model. Journal of Empirical Finance, 1:83–106, 1993.
[52] I. N. Lobato and N. E. Savin. Real and spurious long-memory properties of stock-market data.
Journal of Business and Economics Statistics, 16:261–283, 1998.
[53] N. Vandewalle and M. Ausloos. Coherent and random sequences in financial fluctuations.
Physica A, 246:454–459, 1997.
[54] B. Mandelbrot, A. Fisher, and L. Calvet. A multifractal model of asset returns. Cowles
Foundation for Research and Economics, 1997.
29

Lussange, Vrizzi, Palminteri, Gutkin
[55] Robert F. Engle. Autoregressive conditional heteroscedasticity with estimates of the variance
of united kingdom inflation.Econometrica, 50(4):987–1007, 1982.
[56] Casper de Vries and K.U. Leuven.Stylized facts of nominal exchange rate returns. Working
Papers from Purdue University, Krannert School of Management - Center for International
Business Education and Research (CIBER), 1994.
[57] A. Pagan. The econometrics of financial markets.Journal of Empirical Finance, 3:15–102,
1996.
[58] B. Mandelbrot. The variation of certain speculative prices.The Journal of Business, pages
394–419, 1963.
[59] Rama Cont. Chapter 7 - Agent-Based Models for Market Impact and Volatility. A Kirman and
G Teyssiere: Long memory in economics, Springer, 2005.
[60] E. Fama. Efficient capital markets: A review of theory and empirical work.Journal of Finance,
25:383–417, 1970.
[61] A. K. Bera, S. Ivliev, and F. Lillo.Financial Econometrics and Empirical Market Microstructure.
Springer, 2015.
[62] Judith Wiesinger, Didier Sornette, and Jeffrey Satinover. Reverse engineering financial markets
with majority and minority games using genetic algorithms.Computational Economics, 41:
475–492, 2013.
[63] Marisa Faggini, Bruna Bruno, and Anna Parziale. Toward reverse engineering to economic
analysis: An overview of tools and methodology.Journal of the Knowledge Economy, 13(2):
1414–1432, 2022.
[64] Alexander Sasha Vezhnevets, John P Agapiou, Avia Aharon, Ron Ziv, Jayd Matyas, Edgar A
Duéñez-Guzmán, William A Cunningham, Simon Osindero, Danny Karmon, and Joel Z Leibo.
Generative agent-based modeling with actions grounded in physical, social, or digital space
using concordia. arXiv preprint arXiv:2312.03664, 2023.
[65] John Jumper, Richard Evans, Alexander Pritzel, Tim Green, Michael Figurnov, Olaf Ron-
neberger, Kathryn Tunyasuvunakool, Russ Bates, Augustin Žídek, Anna Potapenko, et al.
Highly accurate protein structure prediction with alphafold.Nature, 596(7873):583–589, 2021.
[66] David Silver, Thomas Hubert, Julian Schrittwieser, Ioannis Antonoglou, Matthew Lai, Arthur
Guez, Marc Lanctot, Laurent Sifre, Dharshan Kumaran, Thore Graepel, Timothy Lillicrap,
Karen Simonyan, and Demis Hassabis. A general reinforcement learning algorithm that masters
chess, shogi and go through self-play.Science, 362(6419):1140–1144, 2018. ISSN 0036-8075.
[67] David Silver, Julian Schrittwieser, Karen Simonyan, Ioannis Antonoglou, Aja Huang, Arthur
Guez, Thomas Hubert, Lucas Baker, Matthew Lai, Adrian Bolton, Yutian Chen, Timothy
Lillicrap, Fan Hui, Laurent Sifre, George van den Driessche, Thore Graepel, and Demis Hassabis.
Mastering the game of go without human knowledge.Nature, 550:354–359, 2018.
[68] Iwao Maeda, David deGraw, Michiharu Kitano, Hiroyasu Matsushima, Hiroki Sakaji, Kiyoshi
Izumi, and Atsuo Kato. Deep reinforcement learning in agent based financial market simulation.
Journal of Risk and Financial Management, 13(4), 2020. ISSN 1911-8074. doi: 10.3390/
jrfm13040071. URL https://www.mdpi.com/1911-8074/13/4/71.
[69] Aleksander Bjerkoey and Mikael Kvalvaer.Replicating Financial Markets using Reinforcement
Learning: An Agent-Based Approach. Master Thesis, NTNU, 2019.
30

Modelling crypto markets by multi-agent reinforcement learning
[70] A. V. Rutkauskas and T. Ramanauskas. Building an artificial stock market populated by
reinforcement?learning agents.Journal of Business Economics and Management, 10(4):329–341,
2009. doi: https://doi.org/10.3846/1611-1699.2009.10.329-341.
[71] I. Momennejad, E. Russek, J. Cheong, M. Botvinick, N. D. Daw, and S. J. Gershman. The
successor representation in human reinforcement learning.Nature Human Behavior, 1:680–692,
2017.
[72] G. Lefebvre, M. Lebreton, F. Meyniel, S. Bourgeois-Gironde, and S. Palminteri. Behavioural
and neural characterization of optimistic reinforcement learning.Nature Human Behaviour,
1(4), 2017.
[73] S. Palminteri, M. Khamassi, M. Joffily, and G. Coricelli. Contextual modulation of value signals
in reward and punishment learning.Nature communications, pages 1–14, 2015.
[74] K. Duncan, B. B. Doll, N. D. Daw, and D. Shohamy. More than the sum of its parts: A role
for the hippocampus in configural reinforcement learning.Neuron, 98:645–657, 2018.
[75] Sumitra Ganesh, Nelson Vadori, Mengda Xu, Hua Zheng, Prashant Reddy, and Manuela Veloso.
Reinforcement learning for market making in a multi-agent dealer market.arXiv:1911.05892,
2019.
[76] Yuh-Jong Hu and Shang-Jen Lin. Deep reinforcement learning for optimizing portfolio man-
agement. 2019 Amity International Conference on Artificial Intelligence, 2019.
[77] R. Neuneier. Enhancing q-learning for optimal asset allocation.Proc. of the 10th International
Conference on Neural Information Processing Systems, 1997.
[78] Yue Deng, Feng Bao, Youyong Kong, Zhiquan Ren, and Qionghai Dai. Deep direct reinforcement
learning for financial signal representation and trading.IEEE Trans. on Neural Networks and
Learning Systems, 28(3), 2017.
[79] Luisanna Cocco, Giulio Concas, and Michele Marchesi. Using an artificial financial market
for studying a cryptocurrency market.Journal of Economic Interaction and Coordination, 12:
345–365, 2017.
[80] Thomas Spooner, John Fearnley, Rahul Savani, and Andreas Koukorinis. Market making via
reinforcement learning. Proceedings of the 17th AAMAS, 2018.
[81] Alessio Emanuele Biondo. Order book modeling and financial stability.Journal of Economic
Interaction and Coordination, 14(3), 2019.
[82] Justin Sirignano and Rama Cont. Universal features of price formation in financial markets:
perspectives from deep learning.Quantitative Finance, 19(9), 2019.
[83] Johann Lussange, Stefano Vrizzi, Sacha Bourgeois-Gironde, Stefano Palminteri, and Boris
Gutkin. Stock price formation: Precepts from a multi-agent reinforcement learning model.
Computational Economics, pages 1–22, 2022.
[84] A. Dodonova and Y. Khoroshilov. Private information in futures markets: An experimental
study. Manag Decis Econ, 39, 2018.
[85] P. K. Naik, R. Gupta, and P. Padhi. The relationship between stock market volatility and
trading volume: evidence from south africa.J Dev Areas, 52(1), 2018.
[86] Symba code repository, 2023. URL https://github.com/johannlussange/symba_crypto.
Accessed: 2023-12-25.
31

Lussange, Vrizzi, Palminteri, Gutkin
[87] R. Sutton and A. Barto.Reinforcement Learning, second edition: An Introduction. Bradford
Books, 2018.
[88] Marco Wiering and Martijn van Otterlo.Reinforcement Learning: State-of-the-Art. Springer,
Berlin, Heidelberg, 2012.
[89] Csaba Szepesvari.Algorithms for Reinforcement Learning. Morgan and Claypool Publishers,
2010.
[90] Richard S. Sutton, David McAllester, Satinder Singh, and Yishay Mansour. Policy gradi-
ent methods for reinforcement learning with function approximation.Advances in Neural
Information Processing Systems, 12:1057–1063, 2000.
[91] David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin Riedmiller.
Deterministic policy gradient algorithms.Proceedings of the 31st International Conference on
Machine Learning, 32, 2014.
[92] Christopher J. C. H. Watkins and Peter Dayan. Q-learning.Machine learning, 8(3-4):279–292,
1992.
[93] David Silver, Aja Huang, Chris J. Maddison, Arthur Guez, Laurent Sifre, George van den
Driessche, Julian Schrittwieser, and et al. Mastering the game of go with deep neural networks
and tree search.Nature, 529:484–489, 2016.
[94] Stephane Ross, Joelle Pineau, Brahim Chaib-draa, and Pierre Kreitmann. A bayesian approach
for learning and planning in partially observable markov decision processes.Journal of Machine
Learning Research, 12:1729–1770, 2011.
[95] Sammie Katt, Frans A. Oliehoek, and Christopher Amato. Learning in pomdps with monte
carlo tree search.Proceedings of the 34th International Conference on Machine Learning, 2017.
[96] Lerrel Pinto, James Davidson, Rahul Sukthankar, and Abhinav Gupta. Robust adversarial
reinforcement learning. arXiv:1703.02702, 2017.
[97] Jane X. Wang, Zeb Kurth-Nelson, Dharshan Kumaran, Dhruva Tirumala, Hubert Soyer, Joel Z.
Leibo, Demis Hassabis, and Matthew Botvinick. Prefrontal cortex as a meta-reinforcement
learning system. Nature Neuroscience, 21:860–868, 2018.
[98] Ivo Grondman, Lucian Busoniu, Gabriel Lopes, and Robert Babuska. A survey of actor-critic
reinforcement learning: standard and natural policy gradients.IEEE Transactions on Systems
Man and Cybernetics, 42:1291–1307, 2012.
[99] Johannes Heinrich. Deep RL from Self-Play in Imperfect-Information Games. PhD thesis,
University College London, 2017.
[100] Volodymyr Mnih, Adrià Puigdomènech Badia, Mehdi Mirza, Alex Graves, Timothy P. Lill-
icrap, Tim Harley, David Silver, and Koray Kavukcuoglu. Asynchronous methods for deep
reinforcement learning. arXiv:1602.01783, 2016.
[101] Jacob Andreas, Dan Klein, and Sergey Levine. Modular multitask reinforcement learning with
policy sketches. International Conference on Machine Learning, 2017.
[102] Chen Tessler, Shahar Givony, Tom Zahavy, Daniel J. Mankowitz, and Shie Mannor. A deep
hierarchical approach to lifelong learning in minecraft.arXiv:1604.07255, 2016.
[103] Shalabh Bhatnagara and J. Ranjan Panigrahi. Actor-critic algorithms for hierarchical decision
processes. Automatica, 42, 2006.
32

Modelling crypto markets by multi-agent reinforcement learning
[104] Andrew Y. Ng, Daishi Harada, and Stuart Russell. Theory and application to reward shaping.
International Conference on Machine Learning, 1999.
[105] Pieter Abbeel, Adam Coates, and Andrew Y. Ng. Autonomous helicopter aerobatics through
apprenticeship learning. The International Journal of Robotics Research, 2010.
[106] M. Keramati and B. Gutkin. Homeostatic reinforcement learning for integrating reward
collection and physiological stability.Elife, 3, 2014.
[107] M. Keramati and B. Gutkin. A reinforcement learning theory for homeostatic regulation.NIPS,
2011.
[108] Sophie Bavard, Mael Lebreton, Mehdi Khamassi, Giorgio Coricelli, and Stefano Palminteri.
Reference-point centering and range-adaptation enhance human reinforcement learning at the
cost of irrational preferences.Nature Communications, 4503, 2018.
[109] Roberto Mota N and Hernan Larralde. A detailed heterogeneous agent model for a single asset
financial market with trading via an order book.arXiv:1601.00229, 2016.
[110] S. Palminteri, G. Lefebvre, E. Kilford, and S. Blakemore. Confirmation bias in human
reinforcement learning: Evidence from counterfactual feedback processing.PLoS computational
biology, 13(8), 2017.
[111] Freddy Delbaen and Walter Schachermayer. What is a free lunch?Notices of the AMS, 51(5),
2011.
[112] Weibing Huang, Charles-Albert Lehalle, and Mathieu Rosenbaum. Simulating and analyzing
order book data: the queue-reactive model.Journal of the American Statistical Association,
110:509, 2015.
[113] Mate Puljiz, Stjepan Begušic, and Zvonko Kostanjcar. Market microstructure and order book
dynamics in cryptocurrency exchanges. InCrypto Valley Conference on Blockchain Technology,
2018.
[114] Eduard Silantyev. Order flow analysis of cryptocurrency markets.Digital Finance, 1(1-4):
191–218, 2019.
[115] Dhananjay Gode and Shyam Sunder. Allocative efficiency of markets with zero-intelligence
traders: Market as a partial substitute for individual rationality.Journal of Political Economy,
101(1), 1993.
33
