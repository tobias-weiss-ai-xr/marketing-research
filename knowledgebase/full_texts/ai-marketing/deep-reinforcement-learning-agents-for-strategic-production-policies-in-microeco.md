---
title: Deep Reinforcement Learning Agents for Strategic Production Policies in Microeconomic Market Simulations
url: https://arxiv.org/abs/2410.20550
category: ai-marketing
subcategory: empirical
date: 2024-10
venue: ''
authors:
- Eduardo C. Garrido-Merchán
- Maria Coronado-Vaca
- Álvaro López-López
- Carlos Martinez de Ibarreta
source: arxiv
pdf_url: https://arxiv.org/pdf/2410.20550
pages: 19
chars: 43048
fetched_at: '2026-11-08T13:17:41+00:00'
kb_version: 1
---

# Deep Reinforcement Learning Agents for Strategic Production Policies in Microeconomic Market Simulations

Deep Reinforcement Learning Agents for
Strategic Production Policies in Microeconomic
Market Simulations
Eduardo C. Garrido-Merch´ an, Maria Coronado-Vaca,
´Alvaro L´ opez-L´ opez, Carlos Martinez de Ibarreta
Universidad Pontificia Comillas, Madrid, Spain
ecgarrido@comillas.edu, mcoronado@icade.edu
allopez@comillas.edu, charlie@comillas.edu
November 2024
Abstract
Traditional economic models often rely on fixed assumptions about
market dynamics, limiting their ability to capture the complexities and
stochastic nature of real-world scenarios. However, reality is more com-
plex and includes noise, making traditional models assumptions not met
in the market. In this paper, we explore the application of deep reinforce-
ment learning (DRL) to obtain optimal production strategies in microe-
conomic market environments to overcome the limitations of traditional
models. Concretely, we propose a DRL-based approach to obtain an effec-
tive policy in competitive markets with multiple producers, each optimiz-
ing their production decisions in response to fluctuating demand, supply,
prices, subsidies, fixed costs, total production curve, elasticities and other
effects contaminated by noise. Our framework enables agents to learn
adaptive production policies to several simulations that consistently out-
perform static and random strategies. As the deep neural networks used
by the agents are universal approximators of functions, DRL algorithms
can represent in the network complex patterns of data learnt by trial and
error that explain the market. Through extensive simulations, we demon-
strate how DRL can capture the intricate interplay between production
costs, market prices, and competitor behavior, providing insights into op-
timal decision-making in dynamic economic settings. The results show
that agents trained with DRL can strategically adjust production levels
to maximize long-term profitability, even in the face of volatile market
conditions. We believe that the study bridges the gap between theoret-
ical economic modeling and practical market simulation, illustrating the
potential of DRL to revolutionize decision-making in market strategies.
1
arXiv:2410.20550v1  [cs.LG]  27 Oct 2024

1 Introduction
The complexity of developing effective business strategies and production poli-
cies in dynamic markets has long been recognized as a significant challenge, as
highlighted by studies on business strategy and simulation in complex environ-
ments [1, 2]. In particular, in highly volatile and complex markets dealing with
lots of explanatory variables of an endogenous variable, conventional assump-
tions of stability and predictability are often invalid, leading to chaotic condi-
tions where traditional economic models struggle to provide accurate forecasts
and actionable insights [3, 4]. Given this complexity in the patterns involving
variables such as how many production should a company perform in a certain
time, it must be emphasized that neural networks, known for their capability
as universal approximators, offer a potential solution by modeling non-linear
patterns within the markets, enabling us to represent in the weights of the net-
work intricate dependencies that are typically not representable by the capacity
of simpler models like generalized linear models [5]. However, neural networks
trained by supervised learning need an annotated dataset, independent and
identically distributed data and a derivable numerical continuous loss function,
assumptions that are often not possible to satisfy in daily markets.
On the other hand, reinforcement learning, particularly in a simulated en-
vironment, provides a framework for agents to learn optimal strategies through
experience, iteratively refining their actions based on feedback [6] that can be
given at any moment in the training of the agent and can be discrete. In par-
ticular, this process mimics real-world learning by trial and error, where agents
adjust their policies to maximize cumulative rewards over time. However, in
scenarios where the simulator does not perfectly replicate real-world conditions
like the markets given their complexity, introducing controlled noise, a process
which is known as domain randomization, can help bridge this reality gap. By
perturbing certain parameters within the simulator, it is possible to generate
variations that cover a wide range of possible real-world scenarios. Within these
perturbed distributions, one instance may closely approximate actual market
conditions, improving the robustness of the agent’s learned policy [7, 8].
In our approach, we combine the virtues of the representative capacity of
deep learning networks and the way that an agent learns with reinforcement
learning to leverage deep reinforcement learning (DRL) within a corrupted sim-
ulation environment to approximate optimal production policies of an agent
in a market. In particular, DRL’s ability to handle high-dimensional spaces
and learn complex policies enables us to model nuanced production strategies
that adapt to fluctuating market dynamics, offering potential improvements in
decision-making under uncertainty [9]. By iterating through multiple instances
of a noisy simulator, our model develops robust strategies that can potentially
be used in real, unpredictable market conditions, aiming to outperform static
or traditional policy models.
The remainder of this paper is organized in the following way: First, Sec-
tion 2 provides a review of the state-of-the-art in Deep Reinforcement Learning
(DRL), including general approaches, applications in finance and economics, and
2

techniques like domain randomization. Then, Section 3 illustrates the method-
ology, detailing foundational aspects of reinforcement learning and specific tech-
niques in DRL. Afterwards, Section 4 describes the market design, including the
simulation environment and the Markov Decision Process (MDP) formulation
used to model agent interactions. Once that everything is defined, in Section
5, we present experimental results and evaluate the impact of producer actions
on the simulated market. Finally, Section 6 concludes the paper and discusses
potential avenues for future research.
2 State-of-the-art
In recent years, DRL has emerged as a powerful tool for solving complex decision-
making problems in a plethora of domains. Concretely, DRL approaches have
been successful in areas requiring sequential decision-making and adaptability
such as the one described in this work, driven by the ability of neural networks to
approximate complex functions and optimize actions through continuous feed-
back. For a complete description of DRL methodologies, far beyond the reach
of this article, there is information in books such as those by [10] and [11], that
provide comprehensive overviews of DRL techniques and their wide range of
applications.
Dealing with the application of this article, microeconomics, and with the
fact that no papers explore the production of items, it is interesting to see a
related application of DRL where it is widely used, finance, especially for tasks
such as portfolio management, asset pricing, and trading strategies. Several
surveys, including [12], [13], and [14], have reviewed the current applications of
DRL in finance, denoting how DRL can handle the stochastic nature of financial
markets and adapt strategies to maximize returns, which is something similar to
what we are going to illustrate in this paper. These studies emphasize the poten-
tial of DRL in transforming financial decision-making, where agents can learn
optimal trading strategies by simulating market environments and optimizing
based on performance feedback. However, they also highlight the challenges in
applying DRL to finance, such as handling noisy data, high-dimensional spaces,
and maintaining robustness in volatile markets. In particular, a specific inter-
esting subfield where DRL is being applied is environmental, social, and gov-
ernance (ESG) finance, which focuses on sustainable and socially responsible
investments. Recent work by [15] explores the integration of DRL with ESG
criteria, exploring how DRL models can prioritize investment strategies that
align with sustainability goals.
Dealing with economics, many current DRL models in economics address
tangent theoretical or predictive problems. According to [16], the integration
of DRL in economic applications is primarily constrained by the complexity
of modeling economic actions that involve multiple, interdependent factors, and
by the challenge of capturing realistic producer behaviors in simulation environ-
ments. Although several DRL approaches are beginning to be used in economic
problems no one deals with the actions that can be done by a producer [16].
3

Consequently, we target this research gap in this article with our proposed ap-
proach whose methodology is going to be explained in the following section.
3 Methodology
In this section we briefly describe the fundamentals of, first, reinforcement learn-
ing and, then, of deep reinforcement learning to illustrate why the use of this
methodology is adequate to estimate a policy of a production agent in a market
simulation.
3.1 Reinforcement Learning
Reinforcement learning [6] is a learning paradigm in which an agent interacts
with an environment in discrete time steps, with the purpose of learning a policy
that maximizes a given loss function, like cumulative rewards or, in our case,
cumulative profits in a time period. Formally, the interaction of the agent with
the environment is modeled as a Markov Decision Process (MDP), defined by
a tuple ( S, A, P, R, γ), where S is the set of observed states by the agent, A is
the set of actions that the agent can perform, P (s′|s, a) is the state transition
probability, representing the probability of moving to state s′ from state s af-
ter taking action a, R(s, a) is the reward function, representing the immediate
reward after taking action a in state s that the agent perceives and γ ∈ [0, 1]
is a discount factor variable, determining the importance of future rewards.
The goal in RL is to find an optimal policy π∗ that maximizes the expected
cumulative reward of the agent in its trajectory through states, or the return
Gt = P∞ k=0 γkR(st+k, at+k), where t is the timestep. This optimal policy is
typically obtained by maximizing the value function V π(s), defined as:
V π(s) = Eπ [Gt|st = s] (1)
and the action-value function Qπ(s, a):
Qπ(s, a) = Eπ [Gt|st = s, at = a] . (2)
The agent seeks to maximizeV π(s) and Qπ(s, a) through various RL algorithms.
However, reinforcement learning stores the value function and action-value func-
tion in a table that maps actions with states. In particular, if the observation
space or action space of the MDP of an agent is high-dimensional or continuous,
the table will need a huge amount of memory to store all the values mapping
states and actions by the reward and computational resources to be traversed by
the agent in training time. In order to circumvent the issue of the memory and
assuming a smoothness between similar states and actions, Deep Reinforcement
Learning will use deep neural networks to represent this mapping, as we will see
in the following section.
4

3.2 Deep Reinforcement Learning
As we have introduced in the previous subsection, DRL generalizes traditional
RL by using neural networks as function approximators, particularly useful in
high-dimensional spaces where traditional tabular methods are infeasible [9]. In
DRL, the agent employs a deep neural network Q(s, a; θ) with parameters θ
to approximate the Q-values or directly model the policy π(a|s; θ). Roughly,
depending on whether they approximate the value function, they directly opti-
mize the policy or if they combine both approaches we find a family of methods
belonging to where they focus the learning that we summarize here. In this
work, we will use three algorithms, one belonging to each different type to test
how they adapt to this problem.
The methodology for deep reinforcement learning (DRL) encompasses sev-
eral approaches, including value-based, policy-based, and actor-critic methods,
each with unique strategies for optimizing agent behavior within a complex
environment.
In a value-based approach, a popular algorithm is Deep Q-Learning, known
as DQN [17]. DQN uses Q-learning combined with neural networks to approxi-
mate the action-value function Q(s, a), which estimates the expected reward for
taking an action a in a state s. The objective is to learn an optimal Q-function,
Q∗(s, a), that satisfies the Bellman equation:
Q∗(s, a) = E h R(s, a) + γ max
a′
Q∗(s′, a′) | s, a i , (3)
where R(s, a) is the immediate reward, γ is the discount factor, and s′ is the next
state. DQN updates its parameters by minimizing a loss function L(θ) like the
mean squared error (MSE) between a predicted Q-value and a target Q-value.
Finally, the policy is set as the actions that are selected based on a greedy
approach, that is selecting the action with the highest probability associated,
or an ϵ-greedy policy, relaxing the selection with a probability ϵ of choosing
any action, to balance exploitation of learned actions and exploration of new
possibilities.
Another family of algorithms, Policy-based methods, such as Proximal Policy
Optimization (PPO) [18], focus on directly optimizing the policy π(a|s; θ) to
maximize the expected cumulative reward. PPO uses a clipping mechanism
to maintain stable updates, keeping the policy within a trust region to avoid
unstable learning. Concretely, the PPO objective function is defined as:
LPPO(θ) = Et
h
min

rt(θ) ˆAt, clip(rt(θ), 1 − ϵ, 1 + ϵ) ˆAt
i
, (4)
where rt(θ) = π(at|st;θ) π(at|st;θold) is the probability ratio between the new and old
policies to avoid unstable learning, ϵ is a small constant, and ˆAt is the advantage
function, which indicates the relative value of an action in a state with respect
to the value function of the state. Critically, the clipping mechanism in PPO
ensures that updates remain conservative, preventing large jumps in policy space
that could destabilize learning.
5

Finally, both policy-based and value-based methods can be combined, some-
thing that is known as actor-critic methods. For example, the A2C method,
Advantage Actor-Critic [19], maintains two models: an actor which is policy-
based and directly learns the policy. On the other hand a critic (value-based)
estimates the value function, that is, the expected future reward of each ac-
tion. Combining both neural networks, the actor is responsible for deciding the
actions based on the feedback provided by the critic modeling an advantage
function, which accelerates and stabilizes the training and balances exploration
and exploitation.
Having briefly covered the fundamental concepts of DRL, we now provide
details in the following section of the market design of our experiment where the
agent is trained using the DRL algorithms that we have shown in this section.
4 Market Design
In this section, we will provide all the details of the market simulation that
we have coded in a Gym environment. We will first describe the dynamics
of the market and the parameters of the environment and then provide infor-
mation about the observation space, action space and reward of the producer
agent. The code of all the simulation and the experiments is available at Github
(https://github.com/EduardoGarrido90/micro agents).
4.1 Market Simulation
We first describe the Market simulation where we have trained several agents.
It basically contains code that simulates the dynamics of a market involving one
particular asset. We assume that this item is unique in the market, in the sense
that no substitute or complementary products exist. However, we simulate the
behaviour of competitors producing the same item as the agent’s producer.
The simulator extends the environment class of the gymnasium library,
which includes a constructor, reset, step and render method. In the construc-
tor, we initialize the production limit per producer, the minimum production,
the number of competitors and their initial produced quantities sample from a
discrete uniform distribution in the ranges of production, we also initialize the
discrete action space of our agent, which are the units produced and the obser-
vation space of our agent, that is a Box space involving the variables detailed
in the following subsection. We also initialize the market price of the asset,
total supply and demand, fixed costs of the company sampled from a normal
distribution, the coefficients of the cubic total production curve, the timestep
of the simulation equal to 0 and some variables that the agent will use to track
the production of the competitors in previous timesteps. The value of the pa-
rameters that we have used as a sample to configure the environment are the
ones illustrated in Table 1.
However, we emphasize that these values are only initial point estimates
and that they are all a sample of different random variable whose joint random
6

Parameter Name V alue Description
Minimum production 0 Minimum production per producer in the simulation
Production limit per producer 14 Maximum production limit per producer
# competitors 3 Number of competing producers in the market
Initial price 15.0 Starting price of goods in the market
Max fixed costs 10.0 Maximum fixed production costs per producer
Min fixed costs 1.0 Minimum fixed production costs per producer
Total prod. constant coef. 0.0 Coefficients of the cubic production curve
Total prod. linear coef. 4.0 Coefficients of the cubic production curve
Total prod. quadratic coef. -0.6 Coefficients of the cubic production curve
Total prod. cubic coef. 0.03 Coefficients of the cubic production curve
Elasticity 1.02 Elasticity factor affecting demand responsiveness
Base demand 43.4 Base demand calculated as production limit × 3.1
Production noise 0.05 Noise factor added to production values
Storage factor 2 Factor affecting storage penalty due to excess production
Max brand effect 0.3 Maximum profit increase (30%) from brand influence
Max subsidy 10.0 Maximum subsidy level at high production levels
Table 1: Parameter values for a sample of the Market Simulator Experiment
variable is the distribution of valid market environments where the DRL agents
can be trained successfully to obtain competitive policies with respect to baseline
strategies.
Once the simulator has been initialized, the step method emulates a timestep
in the simulation, obtaining the action performed by the agent as the result of
its previous observed state and giving as a result the new state of the market,
the reward obtained by the agent which is going to be the profit and several
traces for log purposes.
The step method first simulates a random walk of the units produced by the
competitors as a result of the action of the agent, if the agent produces more,
the supply grows and the price will go down for the same fixed costs, so the
competitors try to produce less and the contrary happens if the agent produces
less. All quantities are clipped from zero to the maximum number of units that
can be produced and the total supply of the item in the market is computed
as the sum of the units produced by the agent and the competitors. Then
a base demand is simulated as 3 times the production limit per the producer,
summed by Gaussian random noise. This base demand is substracted a quantity
which is based in the price of an item, more expensive less demand and a
elasticity, representing that if the price rises a lot the demand is going to decrease
quadratically up to certain elasticity. We also simulate a sinusoidal variation in
the demand every 200 steps approximately representing stationary changes in
the demand of the asset that the agent may learn having the timestep as one of
the variables observed.
The total production cost curve is modelled as a cubic equation whose beta
coefficients are set in the constructor as a function of the ranges of price of the
7

asset. The cubic equation models a decrease in the price as a result of economies
of scale when we produce more units of the item and finally a dramatic rise in
the price if lots of items are produced as raw materials would be scarce and
imported from abroad. The cost is also perturbed by random noise, modeling
operational risk events as in fixed costs and other variables of the simulator. The
supply variation of the company of the agent is also sinusoidal and changes the
production cost. Moreover, if the producer quantity surpasses the total demand,
storage factor penalizations are sum to the production cost exponentially.
The price of the asset changes with respect to a demand and supply curve,
if more units are produced than demanded the price of the asset becomes lower
and the contrary thing happens if demand is lower than supply.
The revenue, which is the reward of the agent, is computed as the price of
the items times the quantity produced, the income, substracted by the fixed
costs of the company, perturbed by random noise representing operational risk
and the production cost. Moreover, a brand effect as a result of market cap is
introduced, so producing more items increases the revenue as a result of image
brand, also perturbed by random noise representing the volatility of the market.
Finally, a subsidy of the public administration is given to companies based on
a production level. The final profit is set as the reward of the agent and the
observation includes all the variables that in reality could be seen by a company,
as it is detailed in the following subsection.
4.2 Markov Decision Process Design
In this section we describe the variables that the agent deals with in order to
estimate a production policy in this market as the ones that are contained in a
Markov Decision Process [20], that is, the variables belonging to the observation
space, the action space and the reward.
We have summarized the variables perceived by the agent in the mentioned
simulation in Table 2. Concretely, the table presents the components of the
agent’s observation space, action space, and reward function of the described
market simulation in the previous subsection. Each element is categorized by
its name, role, variable type, and description, detailing how it contributes to
the agent’s policy. In particular, the observation space includes variables that
allow the agent to perceive the market environment, such as Total Supply, To-
tal Demand, and Price, all of which are real values providing essential data on
current market conditions. The Progress action, represented as an ordinal vari-
able, informs the agent of market trends and how the competitors are going to
react, indicating whether production levels are rising, stable, or declining, while
Timestep%100 tracks the current timestep within a cycle, enabling temporal
awareness of the sinusoidal movements of supply and demand. Additionally,
Competitors Quantities provides an array of production levels from competing
agents seen in the previous timestep, allowing the agent to strategize based on
competitor actions.
On the other hand, the action space is defined by the variable Units Pro-
duced, an integer variable where the agent selects the number of units to produce
8

within the range [0 , 14], directly influencing supply levels, potential profit and
other variables of the simulation. Finally, the reward function, represented by
Producer profit, quantifies the performance of the agent based on the profit
generated, which acts as feedback for optimizing future actions, we could also
extract more complicated reward functions but we leave that for further work.
Name Role V ariable Type Description
Total Supply Observation Real Total supply available in the market
Total Demand Observation Real Total demand in the market at the cur-
rent timestep
Progress action Observation Ordinal Indicates market trend based on pro-
duction (up, equal, or down)
Timestep%100 Observation Integer Current timestep within a 100-timestep
cycle
Competitors Quantities Observation Real array Production levels of each competitor
Price Observation Real Current market price of the goods
Units Produced Action Integer Number of units chosen for production
by the agent
Producer profit Reward Real The profit earned by the producer, used
as the reward for the agent
Table 2: Observation Space, Action Space, and Reward Function of the Agent.
In the following section, we will explain how we can train agents using the
deep reinforcement learning methods described in previous section to estimate
a successful policy in this complex market.
5 Experiments and results
We now detail the format of our experiments and interpret all the results of
them. We begin by formalizing our research hypothesis, that is, the DRL agents
are able to estimate a policy that is competitive in a complex market. More
formally, we can validate this hypothesis through statistical hypothesis testing
in the following way:
H0: µDRL ≤ µrandom
H1: µDRL > µrandom
where µDRL is the mean performance of the policy estimated by the DRL
agents and µrandom is the mean performance of a policy whose action is chosen
at random at every timestep. Consequently, we would like to obtain empirical
evidence that is not compatible with the null hypothesis, H0, that states that
the mean performance of both methods is equal. Similarly, we want to validate
an analogous hypothesis that can be formalized as:
H0: µDRL ≤ µdef ault
H1: µDRL > µdef ault
9

where µdef aultis the mean performance of a policy that always chooses to
produce the same number of assets in every timestep independently on the
market state represented in every observation. In both cases, we would like
to reject the null hypothesis to accept the alternative hypothesis that jointly
states that the performance of the DRL trained estimated policy performance
is significantly superior to a random or fixed policy, and hence, it is effective in
complex markets. We finally want to test that:
H0: µDRL ≤ 0
H1: µDRL > 0
that is, the agents obtain profits after a certain test period in the market. It
is possible that the policy is better than a random or fixed policy but ending in
red numbers, consequently, we also need to validate that the agents have profits
at the end of the test simulation.
In order to obtain empirical evidence to support these claims and reject the
null hypothesis, we design the following experiment using the environment de-
scribed in the previous section. We implement a dummy vectorized environment
of the market simulation where we trained 10 agents using the PPO DRL algo-
rithm from [0, 14] items that can be produced in each timestep. We also launch
15 agents with a default policy that always produce an asset between [0 , 14],
each one corresponding to an asset number. In order to obtain evidence, we also
initialize 5 random agents that simply choose in every timestep their action at
random. Finally, for completeness, we also test value based and combined value
and policy based DRL with a DQN and a A2C agent. We train each DRL agents
for 1.5M timesteps using a learning rate of 10 −4 and default hyperparameters.
We represent the policy in the DRL agents with a multilayer perceptron neural
network with the default StableBaselines3 configuration. For all the agents and
configurations, we save different information that can be interpreted once the
training period is finished. For evaluation purposes we launch all the agents
1000 timesteps and record the cumulated profits that are the reward of every
timestep to compare their performances.
First, we want to ensure that the DRL agents are effectively learning from
the environment about the endogeneous variable of the experiment, the profits.
We can see in Figure 1 the explained variance in the Y axis and the training
timesteps in the X axis of every PPO agent.
We can see how the variability of the profits is starting to be explained from
approximately 700K training timesteps and how the agents are able to explain
a [60, 80]% of the profits, which is an amazing result given that the action of the
agent does not condition the profits alone and lots of variables that condition
the profits are contaminated by noise. In prediction terms, we also see the same
trend in Figure 2, where we can see how the agents are able to better predict
as the training process is done.
It is also interesting to check whether the changes in the policy distribution
being learnt with respect to the previous policy in training time are lower as
the training process goes on. This means that the training is more stable,
converging into a stationary trajectory distribution. We can see in Figure 3
how this phenomenon happens as the KL divergence is lower as the training
10

0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Timesteps 1e6
0.0
0.2
0.4
0.6
0.8Explained Variance
Explained Variance over Time
Explained variance Agent 0
Explained variance Agent 1
Explained variance Agent 2
Explained variance Agent 3
Explained variance Agent 4
Explained variance Agent 5
Explained variance Agent 6
Explained variance Agent 7
Explained variance Agent 8
Explained variance Agent 9
Figure 1: Explained Variance: This plot shows the explained variance over time,
indicating how well the model captures the variance in the data.
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Timesteps 1e6
1000
800
600
400
200
0
Value Loss
Value Losses over Time
Value Loss Agent 0
Value Loss Agent 1
Value Loss Agent 2
Value Loss Agent 3
Value Loss Agent 4
Value Loss Agent 5
Value Loss Agent 6
Value Loss Agent 7
Value Loss Agent 8
Value Loss Agent 9
Figure 2: Value Loss: This plot shows the value loss over time, which helps
monitor the training stability of the model.
process continues until it is almost zero, meaning that changes in the policy
distribution are not existent as the new states and actions performed to not add
11

more information about the profits.
0.0 0.2 0.4 0.6 0.8 1.0 1.2 1.4 1.6
Timesteps 1e6
0
200
400
600
800
1000Approx KL Divergence
Approximate KL Divergence over Time
Approx KL Agent 0
Approx KL Agent 1
Approx KL Agent 2
Approx KL Agent 3
Approx KL Agent 4
Approx KL Agent 5
Approx KL Agent 6
Approx KL Agent 7
Approx KL Agent 8
Approx KL Agent 9
Figure 3: Approximate KL Divergence: This plot shows the approximate KL
divergence values over time or iterations.
Having analyzed the training process and successfully seen that the agents
are learning and their policy is stable, we are now going to analyze the market
dynamics. For example, it is interesting to analyze the demand in testing time,
shown in Figure 4.
We can see how at the beggining of the simulation the demand goes from
0 to a value of 25 and how it oscillates as a function of the timesteps but it is
also contaminated with noise, as the changes of the demand are not smooth,
representing the complexities in the market. The same thing happens with the
total supply for our agent shown in Figure 5.
We can see that both figures are not necessarily equal, though variations are
somewhat correlated, meaning that when the demand increases the supply of
the provider of the agent also increases as it is aware that the demand of the
agent product has grown, however it is not a direct correlation and it is also
contaminated by noise although it has some stationary oscillations. Finally, we
consider also interesting to study the price of the asset, shown in Figure 6.
We can see how the market dynamics influences the price and how it is
also noisy, representing the complex behaviour of demand and supply. It also
oscillates and it is somewhat negatively correlated with the supply, meaning
that more amounts of the asset being available in the market makes the price
of the asset lower, however it is not a strong correlation, representing complex
dynamics in the market.
Having studied the learning process of the DRL agents and the market dy-
namics, we are now able to illustrate the results of the profits accumulated by
12

0 200 400 600 800 1000
Timesteps
0
5
10
15
20
25
30
35Demand
Demand over Time
Figure 4: Demand over Timesteps: This plot shows the variation in demand
across timesteps in the simulation.
0 200 400 600 800 1000
Timesteps
5
10
15
20
25
30
35
40Supply
Supply over Time
Figure 5: Supply over Timesteps: This plot shows the variation in supply across
timesteps in the simulation.
all the agents in test time to see whether we have obtained enough empirical
evidence to reject the three null hypotheses associated with the research ques-
13

0 200 400 600 800 1000
Timesteps
2
4
6
8
10
12
14Price
Price over Time
Figure 6: Price over Timesteps: This plot shows the variation in price across
timesteps in the simulation.
tion of this manuscript, that is, that the agents are able to effectively learn a
policy in a complex market.
In Figure 7 we show a mean profit comparison of all the agents trained in
the experiment, the 10 PPO agents, the A2C agent, the DQN agent, the 15
default agents and the random agents with exciting results.
Concretely, we can see how the DRL agents are the only agents that consis-
tently obtain positive cumulative profits in all the experiments. Concretely, the
minimum accumulated profits in the 1000 timesteps of the experiment is 898 .65
but the maximum is 5129 .20. The PPO mean performance is 1942 .89 and the
standard deviation is 1476. As all the quantities fall in that range, we can safely
assume that the DRL agents, in this training configuration, are going to have
a mean positive profit, obtaining enough evidence to reject the null hypothesis
that the profit is equal to zero and negative. It is interesting that the DQN
agent has surprisingly obtained a good performance with respect to the PPO
agent, our default chosen algorithm due to its popularity as we can see in the
boxplot and lines of Figure 8.
Having retrieved this evidence, we leave for further work, then, the hyper-
parameter tuning problem of the DRL algorithms and model selection as it is
promising. We now focus on the first two hypothesis and provide evidence about
them. We illustrate all the results of the random and default agents in Figure
9.
More concretely, the mean default performance is −61217.42 and the ran-
dom performance is −22333.67, representing that our market simulation is hard
and no easy policy can guarantee you a good result. Only the exception of
14

PPO Default Random A2C DQN
60000
50000
40000
30000
20000
10000
0
Mean Profit
Mean Profit Comparison Across Agents
Figure 7: Mean Bar Plot: This bar plot shows the mean values of key metrics
or variables.
consistently producing 1 quantity of the asset generates a small 102 .32 profit
after all the simulation, being consistently lower than the minimum of the DRL
agents that is 898 .65. To see the evolution of the profit in testing time we also
track the profits in Figure 10.
We can see how all the agents in gray that are the default and random
agents are uniformly incurring in red numbers, some of then considerable losses,
whereas the DRL agents are profitable.
Finally to formalize the empirical evidence obtain we run a t-test that com-
pares the performance of DRL with respect to random obtaining a t-statistic
of 33 .13 and an associated p-value of almost zero. Analogously, we obtained
a t-statistic of 6 .47 in the case of default comparison also with an associated
p-value lower than 10 −5. Consequently, with a significance level α = 0.001 we
reject the null hypotheses and accept the alternative hypotheses that establish
that DRL agents performance is better than a naive policy consisting on random
or default actions. Moreover we have shown how the variability of the profits
is very well explained by the agents, how the training process is stable accord-
ing to the KL divergence and has good performance behaviour according to
the value loss and the cumulated profits. Given all this accumulated empirical
evidence, we consider satisfied our research question whose claim is that DRL
15

PPO Default Random
160000
140000
120000
100000
80000
60000
40000
20000
0
Profit
Combined Boxplot of Agent Performances
Figure 8: Combined Boxplot: This boxplot presents a combined summary of
multiple data distributions or metrics.
agents successfully estimate competitive policies in a complex market.
6 Conclusions and Further Work
This paper demonstrates how DRL agents can be effectively trained to estimate
optimal production policies for a specific item, enabling competitiveness in a
highly complex market environment. In particular, our approach is the first
DRL attempt that illustrates the way for more sophisticated actions within the
agent’s strategy, accommodating various complementary and substitute prod-
ucts that influence market dynamics. By broadening the scope of available
actions or simulating a multi agent system, the agents will gain flexibility to
adapt its production policy in response to the evolving landscape of intercon-
nected goods.
We have seen that we have used point estimations for the hyperparameters
of the DRL agents, whose probability of being the optimum in a continous
hyperparameter space is 0. Consequently, we believe that this approach will
significantly benefit for performing DRL hyperparameter tuning using Bayesian
optimization (BO) [21, 22], as only a few BO evaluations may be reasonable to
do due to computational resources.
16

1
160000
140000
120000
100000
80000
60000
40000
20000
0
Default Agent Performance Boxplot
Figure 9: Default Boxplot: This boxplot illustrates the distribution of the de-
fault configuration or baseline.
Finally, in order to satisfy the investors, an essential aspect of our methodol-
ogy is making the resulting policies explainable. Using recent advancements in
DRL explainable AI [23], we can interpret the agent’s decision-making processes,
allowing stakeholders to understand the rationale behind each production ad-
justment. This interpretability is crucial for building trust and transparency,
especially in complex systems where black-box decisions can be challenging to
justify.
References
[1] David Campbell, George Stonehouse, and Bill Houston. Business strategy:
an introduction. Routledge, 2002.
[2] Mohsen Jahangirian, Tillal Eldabi, Aisha Naseer, Lampros K Stergioulas,
and Terry Young. Simulation in manufacturing and business: A review.
European journal of operational research, 203(1):1–13, 2010.
[3] Robert Trippi and Dimitris N Chorafas. Chaos theory in the financial
markets. McGraw-Hill, Inc., 1994.
17

0 200 400 600 800 1000
Step
160000
140000
120000
100000
80000
60000
40000
20000
0
Accumulated Profit
Accumulated Profit of each Agent Over T est Steps
Agent 1 Accumulated Profit
Agent 2 Accumulated Profit
Agent 3 Accumulated Profit
Agent 4 Accumulated Profit
Agent 5 Accumulated Profit
Agent 6 Accumulated Profit
Agent 7 Accumulated Profit
Agent 8 Accumulated Profit
Agent 9 Accumulated Profit
Agent 10 Accumulated Profit
Default Agent 0 Accumulated Profit
Default Agent 1 Accumulated Profit
Default Agent 2 Accumulated Profit
Default Agent 3 Accumulated Profit
Default Agent 4 Accumulated Profit
Default Agent 5 Accumulated Profit
Default Agent 6 Accumulated Profit
Default Agent 7 Accumulated Profit
Default Agent 8 Accumulated Profit
Default Agent 9 Accumulated Profit
Default Agent 10 Accumulated Profit
Default Agent 11 Accumulated Profit
Default Agent 12 Accumulated Profit
Default Agent 13 Accumulated Profit
Random Agent 0 Accumulated Profit
Random Agent 1 Accumulated Profit
Random Agent 2 Accumulated Profit
Random Agent 3 Accumulated Profit
Random Agent 4 Accumulated Profit
A2C Agent Accumulated Profit
DQN Agent Accumulated Profit
Figure 10: Profit Evolution: This plot depicts how the profit changes over time
or iterations in the simulation.
[4] Robert S Pindyck et al. Microeconomics. 2018.
[5] Yann LeCun, Yoshua Bengio, and Geoffrey Hinton. Deep learning. nature,
521(7553):436–444, 2015.
[6] Richard S Sutton. Reinforcement learning: An introduction. A Bradford
Book, 2018.
[7] Josh Tobin, Rachel Fong, Alex Ray, Jonas Schneider, Wojciech Zaremba,
and Pieter Abbeel. Domain randomization for transferring deep neural net-
works from simulation to the real world. In 2017 IEEE/RSJ international
conference on intelligent robots and systems (IROS) , pages 23–30. IEEE,
2017.
[8] Luc ´ ıa G¨ uitta-L´ opez, Jaime Boal, and´Alvaro J L´ opez-L´ opez. Learn-
ing more with the same effort: how randomization improves the robust-
ness of a robotic deep reinforcement learning agent. Applied Intelligence ,
53(12):14903–14917, 2023.
[9] Vincent Fran¸ cois-Lavet, Peter Henderson, Riashat Islam, Marc G Belle-
mare, Joelle Pineau, et al. An introduction to deep reinforcement learning.
Foundations and Trends® in Machine Learning , 11(3-4):219–354, 2018.
[10] Mohit Sewak. Deep reinforcement learning. Springer, 2019.
[11] Hao Dong, Hao Dong, Zihan Ding, Shanghang Zhang, and T Chang. Deep
Reinforcement Learning. Springer, 2020.
18

[12] Thomas G Fischer. Reinforcement learning in financial markets-a survey.
Technical report, F AU discussion papers in economics, 2018.
[13] Santosh Kumar Sahu, Anil Mokhade, and Neeraj Dhanraj Bokde. An
overview of machine learning, deep learning, and reinforcement learning-
based techniques in quantitative finance: recent progress and challenges.
Applied Sciences, 13(3):1956, 2023.
[14] Ben Hambly, Renyuan Xu, and Huining Yang. Recent advances in rein-
forcement learning in finance. Mathematical Finance, 33(3):437–503, 2023.
[15] Eduardo C Garrido-Merch´ an, Sol Mora-Figueroa-Cruz-Guzm´ an, and Mar ´ ıa
Coronado-Vaca. Deep reinforcement learning for ESG financial portfolio
management. arXiv preprint arXiv:2307.09631 , 2023.
[16] Amirhosein Mosavi, Yaser Faghan, Pedram Ghamisi, Puhong Duan,
Sina Faizollahzadeh Ardabili, Ely Salwana, and Shahab S Band. Com-
prehensive review of deep reinforcement learning methods and applications
in economics. Mathematics, 8(10):1640, 2020.
[17] Volodymyr Mnih. Playing atari with deep reinforcement learning. arXiv
preprint arXiv:1312.5602, 2013.
[18] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and
Oleg Klimov. Proximal policy optimization algorithms. arXiv preprint
arXiv:1707.06347, 2017.
[19] Volodymyr Mnih. Asynchronous methods for deep reinforcement learning.
arXiv preprint arXiv:1602.01783 , 2016.
[20] Martin L Puterman. Markov decision processes. Handbooks in operations
research and management science , 2:331–434, 1990.
[21] Peter I Frazier. Bayesian optimization. In Recent advances in optimization
and modeling of contemporary problems , pages 255–278. Informs, 2018.
[22] Reza Refaei Afshar, Yingqian Zhang, Joaquin Vanschoren, and Uzay Kay-
mak. Automated reinforcement learning: An overview. arXiv preprint
arXiv:2201.05000, 2022.
[23] Alejandra de la Rica Escudero, Eduardo C Garrido-Merchan, and Maria
Coronado-Vaca. Explainable post hoc portfolio management financial pol-
icy of a deep reinforcement learning agent. Technical report, 2024.
19
