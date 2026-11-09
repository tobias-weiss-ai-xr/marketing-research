---
title: Reinforcement Learning-Based Market Making as a Stochastic Control on Non-Stationary Limit Order
  Book Dynamics
url: https://arxiv.org/abs/2509.12456
category: ai-marketing
subcategory: empirical
date: 2025-09
venue: ''
authors:
- Rafael Zimmer
- Oswaldo Luiz do Valle Costa
source: arxiv
pdf_url: https://arxiv.org/pdf/2509.12456
pages: 9
chars: 43094
fetched_at: '2026-11-08T13:18:16+00:00'
kb_version: 1
---

# Reinforcement Learning-Based Market Making as a Stochastic Control on Non-Stationary Limit Order Book Dynamics

REINFORCEMENTLEARNING-BASEDMARKETMAKING AS A
STOCHASTICCONTROL ONNON-STATIONARYLIMITORDER
BOOKDYNAMICS
Rafael Zimmer
Institute of Mathematics and Computer Sciences
University of S˜ao Paulo
rafael.zimmer@usp.br
Oswaldo L. V . Costa
School of Polytechnic Engineering
University of S˜ao Paulo
oswaldo.costa@usp.br
ABSTRACT
Reinforcement Learning has emerged as a promising framework for developing adaptive and data-
driven strategies, enabling market makers to optimize decision-making policies based on interac-
tions with the limit order book environment. This paper explores the integration of a reinforcement
learning agent in a market-making context, where the underlying market dynamics have been ex-
plicitly modeled to capture observed stylized facts of real markets, including clustered order arrival
times, non-stationary spreads and return drifts, stochastic order quantities and price volatility. These
mechanisms aim to enhance stability of the resulting control agent, and serve to incorporate domain-
specific knowledge into the agent policy learning process. Our contributions include a practical im-
plementation of a market making agent based on the Proximal-Policy Optimization (PPO) algorithm,
alongside a comparative evaluation of the agent’s performance under varying market conditions via
a simulator-based environment. As evidenced by our analysis of the financial return and risk met-
rics when compared to a closed-form optimal solution, our results suggest that the reinforcement
learning agent can effectively be used under non-stationary market conditions, and that the proposed
simulator-based environment can serve as a valuable tool for training and pre-training reinforcement
learning agents in market-making scenarios.
KeywordsReinforcement Learning·Market Making·Limit Order Book·Stochastic Control·Market Microstructure
1 Introduction
Market making in financial markets can be defined as con-
tinuously quoting bid and ask prices to profit from thes-
pread, and is an essential part of the market microstruc-
ture, as it helps to narrow bid-ask spreads, reduce volatil-
ity, and maintain market stability [13, 18]. This is par-
ticularly important in times of high uncertainty, as mar-
ket makers provide liquidity, which helps to maintain a
fair and efficient market price. With the advent of elec-
tronic trading, placing optimal bid and ask quotes as a
market maker is becoming an almost completely automa-
tized task, but such a transition requires dealing with addi-
tional caveats, including slippage, market impact, adverse
market regimes [4, 5] and non-stationary conditions [11].
The Reinforcement Learning (RL) paradigm has shown
promising results for optimizing market making strate-
gies, where agents learn to adapt their policies through
trial and error given a numerical outcome reward score 1,
which is used to evaluate the agent’s performance in the
1Not to be confused with financial returns.
environment [26]. The RL approach is based on the Bell-
man equation for state values or state-action pair values,
which recursively define the state-value of a policy as the
expected return of discounted future rewards. State-of-
the-art RL algorithms, such as Proximal Policy Optimiza-
tion (PPO) and Soft Actor-Critic (SAC), solve the Bell-
man equation by approximating the optimal policy us-
ing neural networks to learn either the policy, the value
function [26], or both [17, 22], thus enabling the agent
to learn the optimal actions according to observed market
states [3, 16].
Using historical data to train RL agents is a common prac-
tice in the market making literature, but has some limita-
tions due to being computationally expensive and requir-
ing large amounts of data, besides not including the ef-
fects of market impact and inventory risk [9, 10] on the
agent’s decision-making policies. An additional approach
to creating realistic environments are agent-based simu-
lations, where generative agents are first trained against
observed market messages and then used to simulate or-
der arrivals. This approach has the disadvantage of trading
off fine-grained control over market dynamics for realism,
arXiv:2509.12456v2  [q-fin.TR]  14 Feb 2026

as well as limiting the agent’s adaptability to unseen mar-
ket regimes, which can lead to underfitting and subopti-
mal decision-making under scenarios where market im-
pact and slippage have a more prominent effect on the
agent’s performance. On the other hand, using stochas-
tic models to simulate the limit order book environment is
computationally cheaper and faster to train, but may not
capture the full complexity of real market dynamics, due
to simplified assumptions and static [25].
In the context of this paper, we propose and discuss
a methodology for integrating a reinforcement learning
agent in a market-making context, where the underlying
market dynamics are explicitly simulated using parame-
terizable stochastic processes combined carefully to cap-
ture observed stylized facts of real markets. Our main
contribution is implementing multiple non-stationary dy-
namics into a single limit order book simulator, and how
using fine-controlled non-stationary environments can en-
hance the resulting agent’s performance under adverse
market conditions and provide a more realistic training
environment for RL agents in market-making scenarios,
while still considering market impact and inventory risk.
We then perform a comparative analysis of the agent’s
performance under changing market conditions during
the trading day and benchmark it against the Avellaneda-
Stoikov market making strategy [2] optimal solution (un-
der a simplified market model).
2 Bibliography Review
A bibliographical search was performed to determine the
current state-of-the-art in market-making research using
reinforcement learning. The analysis performed showed
a gap in the literature regarding simulations with varying
market regimes and non-stationary environments, which
we aim to address in our research. We determined the best
performing algorithms and state-action spaces used in the
literature, and the most common data types and reward
structures used in the references. The search was made
using the Web of Science repository, covering the last 5
years, with the following search key:
(
"reinforcement learning" OR
"optimal control" OR
"control theory" OR "machine learning"
)
AND
(
"market making" OR "market maker"
)
Initially, 59 references were selected and deemed relevant to the
project, with 23 of them being effectively used in our analysis,
and 5 additional references being added to the list after the initial
selection.
2.1 Data Type
The majority of the references used historical data, while the
second most common type was agent-based simulations, where
Figure 1: Data types used in the references.
generative agents are trained against observed market messages
and used to simulate the LOB environment [9, 10] trading off
control over the market dynamics for replicating observed mar-
ket flow.
The third most common were stationary processes including Ge-
ometric Brownian Motion and Poisson processes [11, 25] for
order arrival and price dynamics, while some used the Hawkes
process for simulating order arrival times. Overall, the refer-
ences shown in Figure 1 demonstrate a preference for historical
data and model-based simulators, and although being extremely
promising approaches, neither completely account for changing
market regimes and scenarios where impact and slippage have
a more prominent effect on the agent’s performance. With no
references using both simulated data and reinforcement learning
agents instead of closed-form solutions, we aim to address this
gap in the literature by implementing a reinforcement learning
agent and testing its robustness and generalization capabilities
under non-stationary environments.
2.2 State, Action, and Reward Spaces
Most analyzed references defined state spaces primarily based
on market-level observations, as shown in Figure 2c. specifically
top-of-book quotes and N-depth book levels which align well
with the real-time data available to market-making agents [3,
16]. Additionally, agent inventory was also a common fea-
ture, reflecting the importance of managing risk and liquidity
in market-making strategies [10, 20]. The tagged action spaces
was mostly made up only one pair of quotes, with some refer-
ences allowing the choice of multiple bid-ask levels. Some ref-
erences also used book levels as discrete action space variables,
displayed in Figure 2b.
Finally, almost all reward structures, shown in Figure 2a, were
based on intraday or daily profit-and-loss scores, with either run-
ning liquidation, inventory penalties, or a combination of both.
The tagged action space variables also includes a separate “In-
ventory” variable that refers to portfolio strategies that output a
target maximum inventory. For implementations that use spe-
cific quantities per order, no additional tags were used, as only
1 reference did not add quantities as part of the action space and
instead used fixed quantities.
2.3 Chosen Algorithms
Most references used Deep Q-Learning and Actor-Critic meth-
ods, leveraging neural networks for the optimal policy or state-
2

(a) Tagged reward space function variables
(b) Tagged action space variables
(c) Tagged state space variables
Algorithm References
Closed-Form Expression 8
Deep (Double) Q-Learning 6
Proximal Policy Optimization 2
Q-Learning 2
SARSA 1
Vanilla Policy Gradient 1
SAC 1
Table 1: Algorithms used in the references.
value function estimation, due to the high-dimensional nature of
limit order books [10, 20]. The most used algorithms were PPO
and DQN, as shown in Table 1, both being the best performers
in terms of convergence and generalization capabilities in the
literature [12, 25], with some references using DDQN variants.
The literature on model-free approaches overall demonstrated
strong adaptability capabilities towards changing market condi-
tions while still maintaining acceptable training times. Overall,
the performed bibliographical review underscores the growing
relevance and preference for reinforcement learning algorithms
in the market-making domain, particularly when combined with
realistic spatial and temporal state representations.
3 Methodology
The market-making problem addressed in this work involves de-
signing an optimal trading policy for an agent using reinforce-
ment learning. The policy should be able to balance profit and
risk, particularly under a market impact cost model, with non-
stationary dynamics and a complex state transition function. The
environment dynamics are modeled by an underlying limit order
book (LOB) and the details of the state transition operator and
the process of obtaining the optimal decision policy to maximize
cumulative rewards over time are described in the following sec-
tions.
3.1 A Formal Description of the Environment
In modeling the environment, we initially utilize a continuous-
time, continuous-state Markov Chain, and later transition to a
discrete implementation to address computational space con-
straints. Specifically, we model the environment as a Markov
Decision Process (MDP), defined as a 4-tuple(S,A,P, R),
where:
•Sis the set of states called the state space.
•Ais the set of actions called the action space.
•P:S × A × S →[0,1]is the transition probability function
for the MDP.
•R:S × A × S′ →Ris the reward function associated with
each state transition.
Then, the agent’s interaction with the environment is made by
chosing an actionafrom the action spaceAin response to
an observed states∈ S, according to a policyπ(s, a). The
agent’s goal is to maximize cumulative rewards over time, which
are obtained from the reward functionR. The returnG t =R T
t γk−tRkdkis used to estimate the value of a state-action pair by summing the rewards obtained from timetto the end of the
episode (usually, as well as in our case, discounted by a factor
γto favor immediate rewards), whereR t is the observed reward
at timetandTis the time of the episode’s end.
3.1.1 Chosen State Space
We choose a state space that tries to best incorporate the histor-
ical events of the limit order book into a single observable state
using market features deemed relevant and chosen through our
initial bibliography research, as well as guided by the works of
Gasparov et al. (2021) [11] and Gueant et al. (2017) [15] on
reinforcement learning for market-making. We used the agent’s
current inventory and a set of indicators for the currently ob-
served market state: the Relative Strength Index (RSI); order
imbalance (OI); and micro price (MP). Additionally, for a fixed
numberDof LOB price levels the pair(δ d, Qd), whereδ d is the
half-spread distance for the leveld≤D, andQ d the amount of
orders posted at that level is added to the state as a set of tuples,
for both the ask and bid sides of the book. The state space can
therefore be represented by the following expression:
st ∈ S=

RSIt,OI t, M Pt,Inventory t,
MA10,t,MA 15,t,MA 30,t,
(δd,ask t , Qd,ask t )D d=1,
(δd,bid t , Qd,bid t )D d=1
3

where0< t < T, and MAn,t is the moving average of the price
returns over the lastntime steps. The indicators for our chosen
market simulation framework are defined individually by values
directly obtained from the observed LOB, and serve as market
state summaries for the agent to use:
•Order Imbalance (OI):Measures the relative difference be-
tween buy and sell orders at a given time.
•Relative Strength Index (RSI):Momentum indicator that
compares the magnitude of recent gains to recent losses to
evaluate overbought or oversold conditions.
•Micro Price (P micro):Weighted average of the best bid and
ask prices, weighted by their respective quantities.
OIt = Qbid t −Q ask t
Qbid t +Q ask t
RSIt = 100− 100 1 + Average Gain Average Loss
Pmicro,t = P ask t Qbid t +P bid t Qask t
Qbid t +Q ask t
(1)
whereP ask t andP bid t represent the best ask and bid prices at time
t, andQ bid t andQ ask t represent the total bid and ask quantities,
respectively. TheAverage GainandAverage Lossare computed
over a rolling window (in our case, fixed 5 minute observa-
tion intervals), and are defined as the average price increases
and decreases during that window, respectively. OI t ∈[−1,1],
with OIt = 1indicating complete dominance of bid orders, and
OIt =−1indicating ask order dominance. The RSI is bounded
between 0 and 100, with values above 70 indicating overbought
conditions and values below 30 indicating oversold conditions.
Overall, the chosen state space designed to capture the most rel-
evant market features for the agent to make informed decisions
is not a novel approach per-se, containing common indicators
used in market-making literature [8, 14, 24].
3.1.2 Chosen Action Space
The control, or agent, interacts with the environment choosing
actions from the set of possible actions, such thata∈ Ain
response to observed statess∈ Saccording to a policyπ(s, a)
which we will define shortly, and the end goal is to maximize cu-
mulative rewards over time. The agent’s chosen action impacts
the evolution of the system’s dynamics by inserting orders into
the LOB that might move the observed midprice, to introduce
features of market impact into our model.
The action spaceAincludes the decisions made by the agent at
timet, specifically the desired bid and ask spreads pairδ ask, δbid
and the corresponding posted order quantitiesQ ask, Qbid:
A=
n
(δask, δbid, Qask, Qbid),∀δ∈R +,∀Q∈Z}
3.1.3 Episodic Reward Function and Returns
The episode reward functionR t ∈Rreflects the agent’s profit
and inventory risk obtained during a specific time in the episode.
It depends on the spread and executed quantities, as well as the
inventory cost and was choosen according to the best perform-
ing reward structures taken from the literature review. For our
model the utility chosen is based on a risk-aversion enforced
utility function, specifically theconstant absolute risk aversion
(CARA)[1, 21] with the virtual running Profit and Loss (PnL)
as input. It depends on the realized spreadδand the realized
quantityq 2, and is computed as follows, where the penalty for
holding large inventory positions is discounted by a factor ofη
from the final score:
Running PnLt =δ ask t qask t −δ bid t qbid t +I t ·∆M t,
Penaltyt =η(Inventory t ·∆M t)+ ,
PnLt :=Running PnL t −Penalty t
Finally, the reward function is defined as the negative of the ex-
ponential of the running PnL, a common choice for risk-averse
utility functions according to literature [8, 14, 24]. The CARA
utility function is defined as follows, whereγis the risk aversion
parameter:
Rt =U(PnL t) =−e −γ·PnLt ,
3.2 State Transition Distribution
The previously mentioned transition probability densityPis
given by a Stochastic Differential Equation expressed by the
Kolmogorov forward equation for Markov Decission Processes:
∂P(s ′, t|s, a)
∂t =
Z
S
L(x|s, a, t)P(s′|x, a, t)dx(2)
for alls, s′ ∈ Sand all timestbefore market closeT, that
is,t≤T, whereais choosen by our control agent according
to a policyπ(s).Lis the generator operator and governs the
dynamics of the state transitions given the current time.
In continuous-time and state MDPs, the state dynamics is
reflected byL, and modern approaches to optimal control
solve analytically by obtaining a closed-form expression for the
model’s evolution equations, as originally tackled by Avellaneda
et al. (2008) [2] and Gueant et al. (2017) [15]. or numerically
by approximating its transition probabilities [8, 14, 24]. Closed-
form expressions forLare obtainable for simple environment
models, by usually disconsidering market impact, which is not
the case for our proposed model, and solving for the generator
operator is therefore outside the scope of this paper. We describe
in section 4 our chosen approach to model the state transition
distribution, using the Proximal Policy Optimization (PPO) al-
gorithm to approximate the optimal policy for the agent.
3.3 Market Model Description and Environment
Dynamics
Our approach to the problem of market making leveragesonline
reinforcement learningby means of a simulator that models
the dynamics of a limit order book (LOB) according to a set of
stylized facts observed in real markets. For our model of the
limit order book the timing of events follows aHawkes process
to represent a continuous-time MDP that captures the observed
stylized fact of clustered order arrival times. The Hawkes pro-
cess is aself-exciting process, where the intensityλ(t)depends
on past events. Formally, the intensityλ(t)evolves according to
the following equation:
λ(t) =µ+
X
ti<t
ϕ(t−t i),
ϕ(t−t i) =αe −β(t−ti),
2Differs from the agent’s posted order quantityQ, asqis a
stochastic variable dependent on the underlying market dynam-
ics.
4

whereµ >0is the baseline intensity, andϕ(t−t i)is thekernel
functionthat governs the decay of influence from past eventst i.
A common choice forϕis the exponential decay function, where
αcontrols the magnitude of the self-excitation andβcontrols the
rate of decay.
The bid and ask prices for each new order are modeled by two
separateGeometric Brownian Motionprocesses to capture the
normally distributed returns observed in real markets. The un-
derlying partial differential equation governing the ask and bid
prices are given by:
dX ask t = (µt +s t)X mid t dt+σdW t,
dX bid t = (µt −s t)X mid t dt+σdW t,
whereµis the price drift,s t is the mean spread, andσthe
price volatility. The drift rate process follows a mean-reverting
Ornstein-Uhlenbeckprocess [19], while the spread rate similarly
follows aCox-Ingersoll-Rossprocess [6], which, given that the
Feller condition2κ sσ2 s >1is satisfied, ensures the spread re-
mains positive:
dµt =κ(µ−µ t)dt+ηdW t,
dst =κ s(s−s t)dt+σ s
√stdWt,
These two processes serve to model a market where return and
spread regimes can vary over time, forcing the agent to choose
prices accordingly. Whenever a new limit order that narrows the
bid-ask spread or a market order arrive the midprice is updated
to reflect the top-of-book orders. The midpriceX mid t is there-
fore obtained by averaging the current top-of-book bid and ask
prices:
X mid t = X ask t +X bid t 2
and while there are no orders on both sides of the book, the mid-
price is either the last traded price, observed or an initial value
set for the simulation, in the given order of priority. By ana-
lyzing the midprice process, we can make sure the returns are
normally distributed, with meanµ t and volatility σ2 2 , assuring the model reflects a stylized fact of LOBs commonly observed
in markets [14].
To model the underlying price volatility, we use a simple
GARCH(1,1)process, where the volatility process evolves ac-
cording to Equation 3. This choice is motivated by the fact
that the GARCH(1,1) process is able to capture the clustering of
volatility observed in real markets, and can be easily calibrated
to match the observed volatility of the desired underlying asset
to be modeled.
σ2 t =ω+αϵ 2 t−1 +βσ 2 t−1, (3)
Finally, the order quantitiesq ask t , qbid t ∼Poisson(λ q)are mod-
eled as Poisson random variables, where the arrival rateλ q is
a constant parameter. Our simulator was implemented using a
Red-black tree structure for the limit order book, while new or-
ders follow the event dynamics described by the stochastic pro-
cesses above. The individual market regime variables, specifi-
cally the spread, order arrival density and return drift, are sam-
pled from the aforementioned set of pre-defined distributions,
and inserted into the simulator at each event time step.
3.4 Decision Process
In reinforcement learning, the Bellman equation is a fundamen-
tal recursive relationship that expresses the value of a state in
terms of the immediate reward and the expected value of subse-
quent states. For a given policyπ, the Bellman equation for the
value functionV(s)with respect to the chosen reward function
is:
V π(s) = X
a∈A
π(a|s)
X
s′∈S
P(s ′ t+1 |s t, a)  Rt +γV π(s′ t+1) 
V π(s) =E π [Rt +γV π(st+1)|s t =s]
whereV(s)is the value function, representing the expected re-
turn (cumulative discounted rewards) starting from states, go-
ing to states ′ by taking actionaand continuing the episode,
Rt is the reward obtained from the action taken, andγis the
discount factor, used to weigh the value favorably towards im-
mediate rather than future rewards. The Bellman equation un-
derpins the process of optimal policy derivation, where the goal
is to find the optimal policyπ ∗, that is, the control for our action
spaceAthat maximizes the expected return, and can solved by
maximizing for the value function:
V ∗(s) = max
a
E[R t +γV ∗(st+1)|s t =s, at =a]
π∗(s) = arg max
a∈A
E[R t +γV ∗(st+1)|s t =s, at =a]
The Bellman equation is used to recursively define state val-
ues in terms of immediate rewards and expected value of subse-
quent states, and for simpler environments, the equation can be
solved directly by dynamic programming methods. Such meth-
ods, like value iteration or policy iteration, although effective,
become computationally expensive and sometimes unfeasible
for large state spaces, or require a model of the environment,
which is not always available in practice. Neural networks have
been successfully used to approximate both the value function
or the optimal actions directly, demonstrating state-of-the-art re-
sults in various domains, including games, robotics, and finance
[3, 10, 12, 16, 20, 25]. Our simulation environment is complex
enough that the state space is too large to store all possible state-
action pairs, and since we assume no knowledge of the under-
lying dynamics of the environment when training the agent, a
model-free approach is necessary.
3.4.1 Generalized Policy Iteration and Policy
Gradient
Generalized Policy Iteration algorithms are a family of algo-
rithms that combines policy evaluation and policy improvement
steps iteratively, so that the policy is updated based on the value
function, and the value function is updated based on the pol-
icy. While simpler methods directly estimate state values or
state-action values, such as Q-learning, more complex methods
such as Actor-Critic algorithms, estimate both the policy and the
value function. The critic estimates the value functionV π, or
Aπ =Q π −V π, if using the advantage function, while the
actor learns the policyπ. We use apolicy gradientapproach,
where the agent optimizes the policy directly by maximizing the
expected return, through consecutive gradient ascent steps on
the policy parameters given episodes of experience. For policy
gradient methods, the following equations express the gradient
ascent step for the policy parametersθand the value function
parametersϕ, using aαlearning rate and the gradient operator
5

Initialize Policy Trajectory Gathering Policy Evaluation
Policy Improvement
(Backpropagation)
No
Reset environments and 
use updated networks
Converged or
max_iter?Yes
End
Training
Figure 3: Diagram of the Generalized Policy Iteration
loop for the implemented agent.
∇:
∇θJ(θ) =E τ∼π θ
" TX
t=0
∇θ logπ θ(at |s t)Aπ(st, at)
#
∇ϕJ(ϕ) =E τ∼π θ
" TX
t=0
∇ϕ (V π(st)−R t)2
#
πθ ←π θ +α∇ θJ(θ), ϕ←ϕ+α∇ ϕJ(ϕ)
In the context ofProximal Policy Optimization (PPO)the
model is trained to improve its policy and value function by
maximizing the expected return, according to a clipped surro-
gate objective function, which ensures that the policy does not
deviate excessively from the previous policy, promoting stability
during training. ForPPO, the loss function used for the policy
gradient ascent is defined as:
Lactor(θ) =E t
h
min

rt(θ) ˆAt,clip(r t(θ),1−ϵ,1 +ϵ) ˆAt
i
,
ˆAt =
∞X
l=0
(γλ)lδt+l.
wherer t(θ)is the probability ratio between the new and old
policies and ˆAt is the advantage function. The critic loss is the
mean square error between the predicted valueV(s t)and the
actual returnR t, defined as:
Lcritic =E t  (V(s t)−R t)2 ,
Algorithmically, this is implemented by gathering trajectories
from the environment and estimating the expression above using
finite differences as shown in Algorithm 1.
Each pass updates both the policy parametersθand the value
function parametersϕby applying the usual backward propa-
gation pass for neural networks to minimize the loss function
according to a chosen optimizer. A more detailed explanation of
the PPO algorithm can be found in the original paper by Schul-
man et al. (2017) [23]. Our implementation of the algorithm is
a distributed-parallel version of the original version, where mul-
tiple learners interact with the environment in parallel and share
the experience to update the policy and value function. Short of
the V-trace algorithm, this approach is similar to the IMPALA
algorithm [7]. Besides the proposed approach for simulating dy-
namic limit order book environments, we also implement a hy-
brid neural network for the agent’s policy and value functions,
composed of a sequence of self-attention layers to capture the
spatial dependencies between the different levels of the LOB,
concatenated with dense layers to process the market features,
as discussed in section 4.
Algorithm 1Actor-Critic with PPO Updates
Require:Policyπ θ, value functionV ϕ, trajectoriesτ,
epochsK, batch sizeB
1:Compute Advantage Estimation:
2: ˆAt = P∞ l=0(γλ)lδt+l
3:Compute Returns:R t = ˆAt +V(s t)
4:Construct datasetD=
(st, at, ˆAt, Rt,logπ θ(at|st))
5:forepochk= 1toKdo
6:forminibatch(s, a, ˆA, R,logπθold(a|s))inDdo
7:Policy Update:
8:Compute probability ratio:r t(θ) = πθ(a|s) πθold (a|s)
9:Compute loss separately for actor and critic:
Lactor =E h min(rt(θ) ˆAt,clip(r t(θ),1−ϵ,1 +ϵ) ˆAt) i
Lcritic =E  (Rt −V(s t))2
10:Perform backpropagation and gradient up-
date:
θ←θ+α∇ θLactor, ϕ←ϕ+α∇ ϕLcritic
11:end for
12:end for
3.4.2 Benchmark Closed-Form Expression for
Simplified Model
To ensure the agent’s performance is able to capture the com-
plexity of the environment, we use a benchmark closed-form ex-
pression to compare the agent’s performance against. We chose
the closed-form expression for the optimal bid-ask spread pair
as proposed by Avellaneda et al. (2008) [2], which is given by
the following expression:
δ∗ = σ√
2
erf−1
 1
2

1 + µ σ  ,
erf(x) = 2√π Z x 0 e−t2 dt. (4)
whereσis the volatility,µis the mean spread, and erf −1 is the
inverse error function. The error function erf(x)serves simply
as a measure of the spread of the normal distribution.
The closed-form expression is derived from a simple market
model which assumes normally distributed non-mean revert-
ing spreads, constant executed order size and exponentially dis-
tributed event time dynamics. As it depends on a simpler model
for the market to be implemented, our expectations are that the
agent will under-perform in a more complex environment. The
optimal bid-ask spread pair according to Equation 4 is then given
byp bid =µ−δ ∗ andp ask =µ+δ ∗. A fixed quantity of1quoted
share as originally proposed is used.
4 Implementation and Model Description
As previously stated in section 3, the chosen model follows the
Actor-Critic architecture, with the Actor network learning the
policy and the Critic network learning the value function. For
the actor network input, we separate the state space into two
6

8x1152
(Features)
40x1152
(LOB)
1152x480
dim=480
dim=480
Feed 
Forward
Add & Norm
Multi-Head
Attention
Add & Norm
8x
Linear Layer
Batch Normalization
Dropout
Softmax
(2x480)x192
192x4
6x
Figure 4: Actor Network Architecture
tensors: the market features and the LOB data. The market fea-
tures contain general high-level information, including the mi-
croprice, 10, 15 and 30-period moving averages, agent inven-
tory, and the Relative Strength Index (RSI) and Order Imbal-
ance (OI) indicators. The LOB data contains the orderedNth
best bid-ask price and volume pairs.
We use a sequence of self-attention layers to capture the spatial
dependencies between the different levels of the LOB, while the
market features are passed through a dense layer and concate-
nated with the output of the self-attention layers, before being
passed through the final dense layers as shown in Figure 4. We
implement the Critic network as a simple feed-forward neural
network with two hidden layers, of 128 and 64 units, respec-
tively, with the same input tensors as the Actor network.
To train our policy and value networks, we use the aforemen-
tioned PPO algorithm[23], which is a model-free, on-policy ap-
proach to optimize the policy directly, as discussed in Subsec-
tion 3.4.1. Our training loop shown in Algorithm 2 consists
of collecting trajectories, computing the Generalized Advantage
Estimation (GAE), which is used instead of the usual returnsGt.
The chosen approach can be classified asonline reinforcement
learning, where the agent learns from interactions with the envi-
ronment, without the need for a pre-existing dataset, as opposed
to offline reinforcement learning, where the agent learns from a
static dataset. Additionally, we use a replay buffer to store the
trajectories and sample mini-batches for training the policy and
value networks. Since the replay buffer is discarded immediately
after a small fixed number of epochs, the approach is closer to
on-policy learning, as the data collected by the policy is the
same as the data used for gradient updates.
5 Experiments and Results
5.1 Experimental Setup
We trained the agent for a total of 10,000 episodes, with an av-
erage of 390 observations per episode — or 1 event per market
minute. For training, we used a single NVIDIA GeForce RTX
3090 GPU with 24GB of memory, and an AMD Ryzen 9 5950X
CPU with 16 cores and 32 threads, and 32GB of DDR4 RAM.
Algorithm 2Training Loop
Require:Environment, PPO model, optimizer, number
of episodesnum episodes
1:foreach episode in rangenum episodesdo
2:Reset environment and observe initial states
3:foreach timestep until episode endsdo
4:Select actiona∼π θ(s)
5:Observe rewardR t and next states ′
6:Store transition(s, a, r)in the trajectory
buffer
7:Sets←s ′
8:end for
9:Compute GAE and Returns// Policy evaluation
10:Update parametersθandϕ// Policy improve-
ment
11:end for
We used the Adam optimizer with a learning rate of3×10 −4
for both the policy and value networks, with 64 epochs per tra-
jectory. The discount factorγwas set to 0.9, the GAE param-
eterλwas set to 0.85, and the PPO clipping parameterϵwas
set to 0.25. The entropy coefficient was set to1.2×10 −3, and
the batch size set to 256 samples per episode/update. The hy-
perparameters were obtained through a grid search optimization
process.
For our market model, we chose the following parameters for
each process, generating 390 samples before each episode to
heat up the book:
• The order arrival rate was set toλ= 1, with clustering param-
etersα= 0.1andβ= 0.1(yearly volume of about100.000
orders).
• Mean spread was set tos= 0.1(10 market price ticks, in
our case, 10 cents) and annualized price drift toµ=−0.02
(−2%), respectively.
• The price volatility parameters were set toω= 0.5,α= 0.1,
andβ= 0.1, whereωis the constant term,αthe autoregres-
sive term, andβthe moving average term.
• The initial midprice was arbitrarily set to100.
5.2 Results Obtained
To evaluate the financial performance of the trained reinforce-
ment learning agent, we analyzed the agent’s financial return,
return volatility, and the Sortino ratio. The results were aver-
aged over10 2 trajectories using the same hyperparameters used
for training.
As shown in Table 2, the reinforcement learning agent exhib-
ited a mean financial return of5.203×10 −5 (annualized re-
turn of about+1.31%.), an almost neutral performance under
adverse market conditions, while the benchmark agent had a
mean financial return of3.037×10 −5 (annualized return of
about+0.76%), underperforming under the same conditions,
but closely matching the expected performance. For the simple
long-only strategy, the mean financial return was−2.206×10−5
(annualized return of about−0.56%), demonstrating how the
agent’s learned policies allowed the RL paradigm to outperform
a simple long-only strategy under adverse market conditions.
The Sortino ratio for the RL-agent was0.7497, outperform-
ing both benchmark agents. Observing the reward curve during
7

training, we can see a steady increase in the reward over time,
as shown in Figure 5, indicating that the agent was learning to
maximize its cumulative rewards over time, as expected.
The agent’s processing time was also measured, as latency is
a critical metric for real-world applications, with the actor net-
work taking on average2.90ms per episode, and the critic net-
work taking0.21×10 −4 seconds per episode, well within the
acceptable range for medium- and low-frequency trading. Fur-
ther training could be performed if necessary to improve the
agent’s performance, but the results obtained were already con-
sidered satisfactory considering the fabricated adverse market
conditions.
Overall, the training process maintained an increasing reward
curve and finished in about 3 hours and 8 minutes. The finan-
cial return of the RL-agent, as shown in Figure 6, was stable
around zero, and even though we expected a slightly negative
return due to the highly volatile market conditions and some-
what low drift, the positive but close to neutral performance was
still considered a favorable outcome, especially when compared
to the benchmark agent’s performance. The calculated Sortino
ratio of0.7497further supports the agent’s performance under
adverse market conditions, when compared to the benchmark
agent scores of0.4271and−0.0079for the Stoikov and Long-
Only strategies, respectively.
The agent demonstrated being capable of adapting to changing
market dynamics and outperform simpler strategies, where the
proposed simulator provided a realistic environment for train-
ing under non-stationary market conditions. We confirmed our
initial hypothesis that stochastic dynamic environments can ef-
fectively be used to simulate a market environment with chang-
ing regimes, and that reinforcement learning agents can learn to
adapt to these conditions, instead of using historical data with no
market impact or sample-biased generative models for training.
6 Conclusion
We have presented the design and implementation of a rein-
forcement learning agent aiming to show the effects of adverse
market conditions and non-stationary environments on control
agents for market-making. As discussed in subsection 3.3, our
approach for a environment models the dynamics of a limit or-
der book (LOB) according to a set of parameterizable stochas-
tic processes configured to mimic observed stylized facts in real
markets The resulting market model replicates stylized facts for
the midprice, spread, price volatility, and order arrival rate, as
well as the impact of market orders on the agent’s inventory, re-
turn standard deviation and end-of-day Profit and Loss score.
The fine-controlled dynamics where the agent interacts with the
environment allows us to model the effects of market impact and
inventory risk on the agent’s performance, and use it to evaluate
the agent’s performance under adverse market conditions, pro-
viding a more realistic training environment for RL agents in
market-making scenarios. The proposed methodology was able
to capture the effects of market impact and inventory risk on the
trading agent’s performance, and affected the resulting agent’s
decision-making policies, as shown in subsection 5.2, which we
verified by comparing the agent’s performance against simpler
benchmark agents that do not account for these effects in their
decision-making policies.
Prospective extensions of the presented work and future research
on existing market model simulators include developing hybrid
Figure 5: Exponential moving average of the training re-
ward per episode, with a linear trend line.
Figure 6: Financial return, averaged over 100 trajectories
with a 1 standard deviation confidence interval.
world models to combine both model-based and model-free ap-
proaches and leverage the capability of RL agents to learn from
non-stationary environments and historical observations of real
markets. Hybrid world models could further improve the ca-
pability of RL agents in adapting to changing market condi-
tions and could provide a more realistic training environment
for market-making agents.
Acknowledgments
The author(s) gratefully acknowledge support from the S ˜ao
Paulo Research Foundation (FAPESP grant no. 2023/16028-3).
References
[1] Kenneth J. Arrow.Aspects of the Theory of Risk-Bearing.
Yrj¨o Jahnsson Foundation, Helsinki, 1965. Reprinted in
Essays in the Theory of Risk-Bearing, Markham Publish-
ing Co., 1971.
[2] Marco Avellaneda and Sasha Stoikov. High-frequency
trading in a limit order book.Quantitative Finance,
8(3):217–224, apr 2008.
[3] Alexey Bakshaev. Market-making with reinforcement-
learning (sac).Quantitative Finance, 2020.
[4] Jean-Philippe Bouchaud, Julius Bonart, Jonathan Donier,
and Martin Gould.Trades, Quotes and Prices: Finan-
cial Markets Under the Microscope. Cambridge University
Press, 2018.
8

Training Metric
Training Time 112 740 000 ms
Time per Episode 845.8±104.4 ms
Processing Time Actor 2.90±1.0 ms
Processing Time Critic 0.21±0.03 ms
Table 2: Test Results
Test RL-Agent Stoikov Long-Only
Mean Return 5.203×10 −5 3.038×10 −5 −2.207×10 −5
V olatility 1.178×10 −4 1.714×10 −4 2.396×10 −3
Sortino Ratio 0.7497 0.4271 -0.0079
Table 3: Training Results
[5] Rama Cont, Amal Moussa, and Edson Bastos e Santos.
Network structure and systemic risk in banking systems.
SSRN Electronic Journal, December 1 2010.
[6] John C. Cox, Jonathan E. Ingersoll, and Stephen A. Ross.
A theory of the term structure of interest rates.Economet-
rica, 53(2):385–407, 1985.
[7] Lasse Espeholt, Hubert Soyer, Remi Munos, Karen Si-
monyan, V olodymir Mnih, Tom Ward, Yotam Doron, Vlad
Firoiu, Tim Harley, Iain Dunning, Shane Legg, and Koray
Kavukcuoglu. Impala: Scalable distributed deep-rl with
importance weighted actor-learner architectures. 2018.
[8] Javier Falces Marin, David Diaz Pardo de Vera, and Ed-
uardo Lopez Gonzalo. A reinforcement learning approach
to improve the performance of the avellaneda-stoikov
market-making algorithm.PLOS ONE, 17(12), DEC 20
2022.
[9] Sascha Frey, Kang Li, Peer Nagy, Silvia Sapora, Chris
Lu, Stefan Zohren, Jakob Foerster, and Anisoara Cali-
nescu. Jax-lob: A gpu-accelerated limit order book simula-
tor to unlock large scale reinforcement learning for trading.
2023.
[10] Sumitra Ganesh, Nelson Vadori, Mengda Xu, Hua Zheng,
Prashant Reddy, and Manuela Veloso. Reinforcement
learning for market making in a multi-agent dealer market,
November 2019.
[11] Bruno Gasperov, Stjepan Begusic, Petra Posedel Simovic,
and Zvonko Kostanjcar. Reinforcement learning ap-
proaches to optimal market making.MATHEMATICS,
9(21), NOV 2021.
[12] Bruno Gasperov and Zvonko Kostanjcar. Market making
with signals through deep reinforcement learning.IEEE
ACCESS, 9:61611–61622, 2021.
[13] Lawrence R. Glosten and Paul R. Milgrom. Bid, ask,
and transaction prices in a specialist market with heteroge-
neously informed traders.Journal of Financial Economics,
14(1):71–100, 1985.
[14] Olivier Gueant. Computational methods for market mak-
ing algorithms. Mathematics in Industry-Cham, 2022. 21st
European Conference on Mathematics for Industry, 2021.
[15] Olivier Gu ´eant. Optimal market making, May 2017.
[16] Jiafa He, Cong Zheng, and Can Yang. Integrating tick-
level data and periodical signal for high-frequency market
making, 2023.
[17] V olodymyr Mnih, Koray Kavukcuoglu, David Silver, An-
drei A. Rusu, Joel Veness, Marc G. Bellemare, Alex
Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg
Ostrovski, Stig Petersen, Charles Beattie, Amir Sadik,
Ioannis Antonoglou, Helen King, Dharshan Kumaran,
Daan Wierstra, Shane Legg, and Demis Hassabis. Human-
level control through deep reinforcement learning.Nature,
518(7540):529–533, 2015.
[18] Maureen O’Hara.Market Microstructure Theory. Black-
well Publishers, 1995.
[19] Leonard S. Ornstein and George E. Uhlenbeck. On the the-
ory of the brownian motion.Physical Review, 36(5):823–
841, 1930.
[20] Yagna Patel. Optimizing market making using multi-agent
reinforcement learning, 2018.
[21] John W. Pratt. Risk aversion in the small and in the large.
Econometrica, 32(1-2):122–136, 1964.
[22] John Schulman, Philipp Moritz, Sergey Levine, Michael
Jordan, and Pieter Abbeel. High-dimensional continuous
control using generalized advantage estimation. 2015.
[23] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec
Radford, and Oleg Klimov. Proximal policy optimization
algorithms. 2017.
[24] Matias Selser, Javier Kreiner, and Manuel Maurette. Opti-
mal market making by reinforcement learning.Quantita-
tive Finance, 2021.
[25] Tianyuan Sun, Dechun Huang, and Jie Yu. Market mak-
ing strategy optimization via deep reinforcement learning.
IEEE ACCESS, 10:9085–9093, 2022.
[26] Richard S. Sutton and Andrew G. Barto.Reinforcement
Learning: An Introduction. The MIT Press, 2018.
9
