---
title: 'FlowHFT: Imitation Learning via Flow Matching Policy for Optimal High-Frequency Trading under
  Diverse Market Conditions'
url: https://arxiv.org/abs/2505.05784
category: ai-marketing
subcategory: empirical
date: 2025-05
venue: ''
authors:
- Yang Li
- Zhi Chen
- Steve Yang
source: arxiv
pdf_url: https://arxiv.org/pdf/2505.05784
pages: 19
chars: 64824
fetched_at: '2026-11-08T13:15:29+00:00'
kb_version: 1
---

# FlowHFT: Imitation Learning via Flow Matching Policy for Optimal High-Frequency Trading under Diverse Market Conditions

arXiv:2505.05784v3  [q-fin.TR]  22 May 2025
FlowHFT: Imitation Learning via Flow Matching
Policy for Optimal High-Frequency Trading under
Diverse Market Conditions
Yang Li1, Zhi Chen 1, Steve Yang1,†
1Stevens Institute of Technology
{yli269, zchen100, syang14}@stevens.edu
Abstract
High-frequency trading (HFT) is an investment strategy that continuously monitors
market conditions and places bid and ask orders at nanosecond speeds. Tradi-
tional HFT approaches fit models using historical data and assume future market
states will follow similar patterns, limiting the effectiveness of any single model
to the specific conditions under which it was trained. Additionally, such mod-
els achieve optimal performance only under restrictive assumptions, including
specific stochastic processes for asset prices, stable order flows, and the absence
of sudden volatility spikes. However, real-world financial markets are dynamic,
heterogeneous, and frequently volatile. To address these challenges, we propose
FlowHFT, a novel imitation learning framework based on a flow matching
policy. FlowHFT simultaneously learns strategies from numerous expert models,
each of which is proficient in specific market scenarios. As a result, our framework
adaptively adjusts investment decisions according to prevailing market conditions.
Furthermore, FlowHFT incorporates a grid-search fine-tuning mechanism, enabling
it to refine strategies and achieve superior performance even under complex or
extreme market conditions where expert strategies may become suboptimal. We
evaluate FlowHFT across various market environments. Our study is the first to
demonstrate the successful application of flow matching policy within stochastic
market environments. Our findings show that FlowHFT can simultaneously learn
trading strategies for each market condition in a single model. Notably, our unified
framework consistently outperforms the best-performing expert strategy in each
tested market scenario.
1 Introduction
Market making (MM) is a trading strategy where participants place both buy and sell orders to profit
from difference in the bid-ask spread. By providing liquidity through these actions, market makers
also enhance market efficiency [ 26, 14]. High-frequency trading (HFT) is one type of market making
that executes orders at high speeds, often measured in milliseconds or microseconds. This rapid
execution allows traders to earn profit on very small price changes within short timeframes [ 2, 5, 1].
Traditional HFT strategies, such as the Avellaneda-Stoikov (AS) model [2] and the Guéant-Lehalle-
Fernandez-Tapia (GLFT) model [ 13], rely on historical market data to calibrate their parameters.
These calibrated models are used to place orders in subsequent market. However, the effectiveness of
traditional HFT models is constrained by two key limitations. If future market conditions diverge
substantially from the historical period used for calibration, the optimized parameters may become in-
effective and lead to suboptimal performance. Moreover, these models are often built on optimization
frameworks requiring strict assumptions about market behavior (e.g., specific stock price processes,
stable order flow, no sudden jumps) that reflect idealized rather than real-world scenarios. Conse-

quently, when actual market conditions violate these assumptions—a common occurrence—these
traditional models struggle to adapt and tend to produce suboptimal trading outcomes.
In the recent literature, Reinforcement learning (RL) has been applied to high-frequency trading,
framing the problem as an agent (the trading algorithm) interacting with an environment (the market).
The agent observes the market state, takes actions and receives rewards based on metrics like profit
and loss. Through this interaction, the RL aims to learn a policy—a strategy—that maximizes
cumulative rewards. However, RL often focuses on optimizing only single-step actions, which can
lead to compounding error [ 11, 20, 40] for instance, slightly suboptimal actions at each step might
accumulate, resulting in a large unwanted position. Effective HFT necessitates a long-term view,
because profitability typically relies on accumulating numerous small gains from individual steps.
Moreover, each action taken interacts with the market environment, thereby impacting the feasibility
and profitability of subsequent moves.
To address the challenges associated with traditional HFT methods, we propose FlowHFT, a novel
imitation learning framework based on flow matching policy [ 6, 34, 16, 35, 17, 36]. This framework
consists of two primary components. The first component utilizes imitation learning to develop a pre-
trained model for observing the market state and generate corresponding trading actions. We simulate
diverse market scenarios and evaluate various traditional models within each. For every scenario,
the model achieving the best performance is designated as the "expert". FlowHFT then learns by
imitating the actions of these designated experts across all scenarios, effectively integrating the
strongest known strategy for each market condition into one single, comprehensive model. Imitation
learning is useful because these models can in fact generate optimal solutions in certain scenarios.
Even in those scenarios where they only generate suboptimal solutions, FlowHFT can still learn their
strategies and improve on them subsequently. The second component uses a grid search mechanism to
fine-tune the action proposed by the pre-trained model. The initial action proposed by the pre-trained
model, refined by the adjustment from the fine-tuning stage, constitutes the final action.
To the best of our knowledge, this paper presents the first flow matching policy based imitation
learning approach to a financial stochastic control problem. The results show that the FlowHFT
framework integrates the knowledge of multiple expert strategies into a single adaptive model.
When market scenarios change, the framework demonstrates adaptability by generating actions
appropriate to the prevailing conditions, effectively leveraging patterns learned from relevant expert
demonstrations. Additionally, FlowHFT is designed for rapid inference, enabling the generation
of trading actions at millisecond speeds for HFT tasks. Furthermore, the grid search mechanism
refines these generated actions. The experimental results indicate that FlowHFT consistently achieves
superior performance compared to the best results obtained from the baseline models individually
optimized for each specific market scenario.
The results indicate that our model exhibits significant robustness to market conditions involving
sudden price jumps. We attribute this resilience primarily to our method’s output: it generates
sequences of actions over a planning horizon, rather than isolated single-step decisions. By producing
action sequences, the model inherently considers a near-term trajectory and allows for smoother
adjustments, effectively taking into account the broader consequences of initial moves. This sequential
planning perspective helps mitigate the compounding error, aligning actions more effectively over
time and thus enhancing strategic stability and performance during volatile events like jumps.
Figure 1: Visualization of FlowHFT’s Input Observation Sequence and Output Action Sequence
𝑶𝒕"𝟏 𝑶𝒕
Observation
Flow Matching Policy Fine-tune
FlowHFT
𝑨𝒕 𝑨𝒕$𝟏 … 𝑨𝒕$𝟖
Execution Horizon
𝑨𝒕$𝟗 …
Receding Window
Predictive Action Sequence 𝑨𝒕
𝑨𝒕"𝟏 𝑨𝒕$𝟏𝟎 𝑨𝒕$𝟏𝟓
2

2 Preliminaries
In this section, we formulate the high frequency trading task mathematically. High-frequency trading
utilizes automated algorithms for order execution at extremely high speeds, often operating within
millisecond or nanosecond timescales. The objective is to continuously place buy (bid) and sell (ask)
limit orders for a specific financial instrument, while aiming to profit from the bid-ask spread.
We can model the HFT market making task as a stochastic control process [2, 13] defined over a set of
discrete time steps T = {0, 1, . . . , T}. The observation state space O captures relevant information
at time t ∈ T. An observation state Ot ∈ Otypically includes observable market information Lt
(often derived from the Limit Order Book, LOB, including stock prices and bid-ask spread) and
the agent’s information Zt, including balance, current inventory level , along with the timet itself,
such that O ⊆ L ×Z × T, where L, Z is the space of market information and agent information,
respectively. We generally assume the state St satisfies the Markov property.
Within this framework, the market maker chooses an action At from the action space A. A common
action involves setting the agent’s bid and ask quotes, often parameterized by spreads(δb t , δa t ) relative
to a reference price pref t derived from the market state Lt. The system’s evolution is governed by
stochastic transition probabilities P (Ot+1|Ot, At), defining the likelihood of moving to the next
observation state Ot+1 = (Lt+1, It+1, t+1) given the current state and action. This transition reflects
changes in both market conditions Lt+1 and the agent’s inventory It+1 due to order executions and
market activity. The agent seeks an optimal policy π : O → A, a rule mapping states to actions
(At = π(Ot)), that maximizes a defined objective function, J(π). A standard objective is to
maximize the expected final value, often combining terminal cash wealth WT with a penalty ϕ(IT )
for inventory risk at the horizon T . The optimization problem is thus:
max
π
J(π) = max
π
Eπ [WT − ϕ(IT ) | O0] (1)
Where, Eπ[·] denotes the expectation under policy π starting from the initial observation state O0 =
(L0, I0, 0). Solving for the optimal policy π∗ = arg maxπ J(π) requires dynamically balancing
profitability against inventory and adverse selection risks in a complex, stochastic environment.
3 Architecture of FlowHFT
3.1 Backbone of FlowHFT: Flow Matching Policy
Figure 2: This figure illustrates the training of a flow matching policy. The inputs are various market
situations. For each situation, the best expert is chosen from a pool of models. These optimal
market-expert pairings are then used to train the flow matching policy, which operates as a vector field.
This field maps the distribution of market conditions to a corresponding optimal action distribution.
𝑴𝒂𝒓𝒌𝒆𝒕 𝟏: (𝑰𝟏,𝑷𝟏,𝑪𝟏,𝑺𝟏,𝑻𝟏)
𝑴𝒂𝒓𝒌𝒆𝒕 𝟐: (𝑰𝟐,𝑷𝟐,𝑪𝟐,𝑺𝟐,𝑻𝟏)
𝑴𝒂𝒓𝒌𝒆𝒕 𝟑: (𝑰𝟑,𝑷𝟑,𝑪𝟑,𝑺𝟑,𝑻𝟏)
Expert Candidates
Trained for M arket 1
Expert Candidates
Trained for M arket 2
Expert Candidates
Trained for M arket 3
Expert
for Market 1
Expert 1
for Market 2
Expert 1
for Market 3
Buy 100 XXX @ Limit $185.20
Sell 50 XXX @ Limit $185.40
Actions
for Market 1
Buy 123 XXX @ Limit $200.30
Sell 50 XXX @ Limit $200.50
Actions
for Market 2
Buy 12 XXX @ Limit $127.60
Sell 13 XXX @ Limit $127.90
Actions
for Market 3
𝑿(𝑰,𝑷,𝑪,𝑺,𝑻) Y(𝑩𝒊𝒅,𝑨𝒔𝒌)
Flow Matching Policy
The core of FlowHFT is a conditional flow matching policy [ 24], denoted πθ(At+1 | Ot), which
learns to map sequences of market observations Ot to trading actions At+1. This policy is trained via
imitation learning from expert demonstrations. We draw inspiration from recent successes of flow
matching in domains like robotics, where these models effectively learn complex, continuous control
policies from expert data by mapping high-dimensional inputs to sophisticated, sequential actions.
3

Our objective is to train a neural network vθ(a, t| Ot) to parameterize a conditional vector field.
This vector field defines a probability flow that transports samples from a simple prior distribution
pprior(a0) (e.g., Gaussian noise) to the distribution of expert trading action sequences pexpert(aE |
Ot), conditioned on the observed market state Ot. Following seminal work on flow matching, we
define a time-dependent probability path pt(a | a0, aE, Ot) that interpolates between an initial
random action sequence a0 and an expert action sequence aE. A simple linear interpolation is given
by: at = (1 − t) a0 + t aE, u t(at | a0, aE) = aE − a0. The training procedure (Algorithm 1)
minimizes the discrepancy between the network’s predicted vector field vθ(at, t| Ot) and the target
vector field ut(at | a0, aE). Specifically, given a market state Ot, the model samples a random initial
action sequence a0 ∼ pprior and a corresponding expert action sequence aE ∼ pexpert(· |Ot). It
then samples a time t ∼ U(0, 1) and forms an interpolated action sequence at using the defined path.
The network is trained by minimizing the following Flow Matching (FM) loss:
LFM(θ) = Et,Ot,a0,aE ,at∼pt(a|a0,aE ,Ot)

∥vθ(at, t| Ot) − ut(at | a0, aE)∥2 . (2)
This objective effectively teaches the network vθ to generate the flow that transforms noise into
expert-like HFT action sequences conditioned on the market state.
ak+1 = ak + 1 N vθ(ak, tk | Ot), t k = k/N, k = 0, . . . , N− 1. (3)
Algorithm 1: Flow Matching Policy Training
Parameters: Neural network vθ(a, t|Ot) with parameters θ, learning rate η
Input: Expert demonstration data Dexpert containing pairs of (Ot, aE(Ot))
1 do
2 Sample a market observation Ot and corresponding expert action sequence
aE ∼ pexpert(·|Ot) from Dexpert (or generate via simulation/expert);
3 Sample an initial action sequence a0 ∼ pprior(·) (e.g., a0 ∼ N(0, I));
4 Sample a time tsample ∼ U(0, 1);
5 atsample ← (1 − tsample)a0 + tsampleaE;
6 utsample ← aE − a0;
7 ˆvtsample ← vθ(atsample, tsample|Ot);
8 L ← ∥ˆvtsample − utsample∥2
9 θ ← θ − η∇θL;
10 until not converged;
At inference (Algorithm 2), to generate an action sequence conditioned on a live market observation
Ot, the policy starts with an action sequence a0 ∼ pprior. It then iteratively refines this sequence
by solving the ordinary differential equation: da dt = vθ(a, t| Ot), from t = 0 to t = 1 . This is typically achieved using a numerical ODE solver (e.g., Euler or Heun method) over a small
number of discretization steps N. This process transforms the initial noise sequence into a coherent,
market-aware sequence of high-frequency trading actions.
Algorithm 2: Flow Matching Policy Inference
Parameters: Trained policy network vθ(a, t|Ot), Number of discretization steps N
Input: Current market observation Ocurrent t
1 a ∼ pprior(·) (e.g., a ∼ N(0, I))
2 tcurrent ← 0;
3 ∆tstep ← 1/N;
4 for k ← 0 to N − 1 do
5 vk ← vθ(a, tcurrent|Ocurrent t )
6 a ← a + vk · ∆tstep
7 tcurrent ← tcurrent + ∆tstep;
Output: a
4

3.2 Fine-tune Pretrained Model
In the first component, a flow matching policy learns to imitate the strategies of various experts.
So it is a general, pre-trained policy. The second component of our framework aims to fine-tune
this pre-trained policy to surpass the performance of experts. To enhance the framework’s real-time
adaptability to immediate market dynamics, we apply a linear transformation to the actions proposed
by the pre-trained model. The parameters of this transformation are rapidly calibrated using the most
current market information. This process is more computationally lightweight and efficient compared
to recalibrating the traditional HFT models. The output of this calibrated linear transformation is then
combined with the initial action from the pre-trained model to yield the final, refined trading decision.
Specifically, this fine-tuning uses a linear transformation of the form (a · output + b) to the action
sequence output by the pretrained model. Specifically, if the pretrained model outputs a sequence of
planned actions (at+1, . . . , at+Tpred) over the prediction horizon, where each action (ai) is a vector
representing the bid and ask offsets for time (t + i) (e.g., (ai = [δbid,i, δask,i])), the fine-tuned action
sequence (a′t + 1, . . . , a′t + Tpred) is computed as a′i = a · ai + b) for each step (i) from 1 to
(T pred). Here, (a) is a scalar scaling factor applied element-wise to each vector (ai), and (b) is
an additive vector offset applied to each vector (ai). Both the scalar (a) and the vector (b) (with
dimensions matching the action vector, e.g., 2 for bid/ask offsets) are calibrated using a validation set.
This adjusted action sequence (a′) is then used by the policy (typically by executing the first action
(a′ t+1)) in the environment.
Figure 3: This figure shows the action generation. The neural network of flow matching policy (left)
provides initial bid/ask outputs. A grid search (right) identifies adjustments (∆bid,∆ask) to refine
these actions. Combine the initial result and adjustment together to get the final results.
Observation
Down Conv Block
2×ResBlock
Downsample
Mid Blocks
2 ×ResBlock
×3
White Noise
Up Conv Block
2×ResBlock
Up sample
×2
Output
bid 𝒃𝒕"𝟏 𝒃𝒕 𝒃𝒕$𝟏 𝒃𝒕$𝟐 … 𝒃𝒕$𝟏𝟓
ask 𝒂𝒕"𝟏 𝒂𝒕 𝒂𝒕$𝟏 𝒂𝒕$𝟐 … 𝒂𝒕$𝟏𝟓
∆bid ∆𝒃𝒕"𝟏 ∆𝒃𝒕 ∆𝒃𝒕$𝟏 ∆𝒃𝒕$𝟐 … ∆𝒃𝒕$𝟏𝟓
∆ask ∆𝒂𝒕"𝟏 ∆𝒂𝒕 ∆𝒂𝒕$𝟏 ∆𝒂𝒕$𝟐 … ∆𝒂𝒕$𝟏𝟓
Flow Matching Policy
Grid Search
BidAdjustment
AskAdjustment
4 Data of Imitation Learning
FlowHFT is an imitation learning framework. Therefore, it is crucial to prepare high-quality learning
material. In this section, we firstly detail how to generate a set of various market scenarios. Secondly,
for each individual scenario, we evaluate a pool of candidate experts—including established traditional
algorithms and reinforcement learning agents—and designate the one exhibiting the best performance
as the "expert" for that context. We use the actions generated by the expert’s strategy to create
state-action pairs for training FlowHFT.
5

4.1 Market Simulation
We model the mid-price St as a jump-diffusion process [ 27], capturing both continuous price
movements and sudden jumps. The stochastic differential equation (SDE) governing the mid-price is
given by:
dSt = St− (µdt + σdBH (t)) + St− (eJ − 1)dNt (4)
where µ represents the drift coefficient, signifying the expected return of the asset. The asset’s
volatility is denoted by σ, which quantifies the fluctuations in its price. The term dBH (t) corresponds
to the increment of a fractional brownian motion process, capturing the continuous component of
price movement. Furthermore, J denotes the size of the jump, following a normal distribution
N (µJ , σ2 J ), which specifies the mean and variance of the jump. Lastly, dNt is a Poisson process with
intensity λJ, modeling the occurrence of jumps, thereby reflecting sudden shifts in the asset’s price.
Next we discuss simulation of order arrival. Order arrivals are modeled using mutually exciting
Hawkes processes [3, 15], effectively capturing the self-exciting and the cross-exciting nature of
financial markets. "self-exciting" effects indicate that prior buy (or sell) orders increase subsequent
arrivals of the same order type, respectively. "Cross-exciting" effects describe how buy orders
influence sell order arrivals and vice-versa.
The intensity of buy and sell orders, λb(t) and λa(t) respectively, are defined as:
λb(t) = µb +
X
ti∈Nb
αbbe−β(t−ti) + X
tj ∈Na
αbae−β(t−tj ), (5)
λa(t) = µa +
X
ti∈Na
αaae−β(t−ti) + X
tj ∈Nb
αabe−β(t−tj ), (6)
where, µb and µa are the baseline intensities for buy and sell orders, respectively. The parameters
αbb and αaa describe the self-exciting effects of buy and buy, and sell and sell orders, respectively,
while αba and αab represent the cross-exciting effects between buy and sell orders. The parameter β
denotes the decay rate, which influences how quickly the effects of past events diminish over time.
Finally, Nb and Na are the sets containing the timestamps of past buy and sell order arrivals, which
are used to model the timing of these events.
We create market scenarios with varying levels of liquidity—categorized as high, medium, and
low. Furthermore, to test the model performance under stress, we introduce scenarios featuring
sudden market changes and periods of significantly increased volatility, allowing us to examine how
effectively each model responds to dynamic and challenging environments. We simulate different
market environments by adjusting the following Simulation parameters. Combining these parameters
yields 3 × 3 × 3 × 2 × 2 × 3 × 1 = 324 parameter combinations.
Figure 4: Parameters settings of market simulation
Stock Price Movement
Brownian motion
(1) Hurst Component 𝐻
       The degree of long-term memory or persistence
       predominantly (H > 0.5), mean-reverting (H<0.5), random (H=0.5)
(2) Drift 𝜇
       Controls the deterministic
       Underlying trend around which the random fluctuations (volatility) of the process occur
(3) Volatility 𝜎
      Dictates the magnitude or scale of the random
      Unpredictable fluctuations around the process's average trend (drift)
(4) Sudden Market Jump 𝐽
       An abrupt, large, and discontinuous change in asset prices
(5) Time step 𝑑!
(1) Liquidity 𝜇",𝜇#
       Tradable volume offered at various bid and ask price levels
(2) Self-exciting 𝛼""	(buy−to−buy),𝛼## (sell-to-sell),
       How the arrival of an order temporarily increases the probability of more orders of the
       same type arriving shortly thereafter
(3) Cross-exciting 𝛼"#
       How the arrival of one type of order influences the arrival rate of orders of the other type
Order Book
Hawkes Process
Parameters Settings
[0.3, 0.5, 0.7]
[0.01, 0.05, 0.2]
[0.05, 0.1, 0.3]
[0, 0.02]
[0.01, 0.02]
[10, 20, 40]
[0.7]
[0.3]
6

4.2 Generation of State-Action Pairs
To generate diverse expert demonstrations for FlowHFT, we utilized a set of expert candidates, in-
cluding: (1) the Avellaneda-Stoikov (AS) model [2], a foundational stochastic control framework for
optimal quoting that considers inventory risk and market volatility; (2) the Guéant-Lehalle-Fernandez-
Tapia (GLFT) model [ 13], which extends such optimal control approaches, often incorporating
aspects such as order flow dynamics; (3) a modified GLFT model incorporating a price drift com-
ponent, designed to adapt strategies in markets exhibiting directional trends; and (4)a model-free
Reinforcement Learning (RL) agent trained with Proximal Policy Optimization (PPO) [33], which
learns a policy through direct interaction or simulation to maximize a specified reward function. The
detailed mathematical formulations, assumptions, and parameterization specifics for each of these
expert models are provided in Appendix A.
We generate state-action pairs for each market generated. For each parameter combination, we
simulate 100 episodes. Each episode consists of 1/dt time steps (e.g., 100 steps if dt = 0.01), each
timestamp yields a state-action pair from the expert strategy, here we collect the corresponding state-
action pairs from the dominant stochastic strategy among our candidates(AS, GLFT, GLFT-Drift,
PPO). In total, we have gathered 3.24 million state-action pairs. These generated state-action pairs
serve as the training dataset for the diffusion policy, providing a broad coverage of market conditions
and ensuring robust policy learning. This dataset serves as the training data for our diffusion policy
framework.
5 Experiments and Results Analysis
Our investigation is designed to critically evaluate FlowHFT’s advantages over existing approaches
and its capabilities to earn profit. Specifically, we address the following research questions: RQ1:
Can FlowHFT effectively generalize strategies learned from expert demonstrations to new, unseen
market conditions? RQ2: Does the fine-tuning mechanism improve the performance of actions
initially proposed by the pre-trained model? RQ3: Can the FlowHFT framework achieve greater
profitability than traditional strategies?
5.1 Out-of-sample Market Environment Settings
To evaluate FlowHFT’s performance across a spectrum of out-of-sample market environments, we
systematically configured distinct test conditions by setting key market parameters to differ from those
used during training (see appendix C ). Firstly, to simulate varied stock price trends, we controlled the
Hurst exponent, which governs the long-term memory and persistence patterns of the price series, and
the drift term, which dictates its underlying direction. Secondly, based on these trend characteristics,
we further differentiated the market microstructure by creating four specific situations based on
combinations of market volatility (V ol) and overall order arrival rate (AR): (1) High V ol/High AR
(HH), representing active, potentially news-driven volatile markets; (2) High V ol/Low AR (HL),
mimicking risky market; (3) Low V ol/High AR (LH), reflecting stable, liquid markets; and (4) Low
V ol/Low AR (LL), simulating quiet market periods. For each of these market situations, we perform
traditional strategies as well as FlowHFT to compare their performance.
5.2 Evaluation Metrics
• Profit and Loss (PnL): Measure the total change in the value over a specific period,
reflecting the aggregate percentage gain or loss.
• Sharpe Ratio (SR): It helps investors understand how much excess return an investment
generated for each unit of risk it undertook. A higher Sharpe Ratio generally indicates a
better risk-adjusted performance.
• Maximum Drawdown (MDD): Quantify the largest percentage decline in the value of a
strategy from a previous peak to a subsequent trough
The detailed calculations of these metrics are provided in Appendix B
7

5.3 Results Analysis
Looking at the results presented from Table 7 to Table 6, a consistent pattern emerges across the
various market scenarios. Firstly, the GLFT model typically yields superior results compared to the
AS model. Critically, our pre-trained flow matching policy model demonstrates performance levels
comparable to the GLFT instructor. This finding is significant to address the RQ1. It indicates that
the pre-trained model successfully learned and internalized effective strategies from its instructors,
even within these challenging stochastic environments.
In response to RQ2, we examine the results corresponding to the fine-tuned Flow Matching policy.
This adapted model typically and significantly outperforms both the traditional benchmark models
and the initial pre-trained model across the tested environments. This finding validates the second
core objective of our framework: we not only demonstrate the ability to effectively learn from expert
instructors but also showcase the capacity to surpass their performance. This success is attributed to
the fine-tuning process, which empowers the model to "sense" the prevailing market conditions via
the validation set calibration and subsequently adjust its behavior, specializing its strategy for the
specific market environment encountered.
Note that our experimental design includes highly volatile market environments, which are char-
acterized by the potential for sudden and significant price movements. We show that FlowHFT
exhibits robustness in these challenging conditions, particularly when compared with traditional RL
methods. This indicates that generating sequences of actions rather than purely single-step decisions
can effectively incorporate a longer-term planning perspective. This approach allows the model to
better anticipate downstream consequences, make more considered adjustments over multiple steps,
and mitigate the risk of compounding errors.
In response to RQ3, we take analyses of the performance metrics to obtain significant insights into
the profit-generating capabilities across different market conditions. The Finetuned Flow Policy
consistently demonstrates strong PnL (Profit and Loss) figures, notably achieving the highest PnL of
26.79 in the "Low V olatility & High Demand" scenario and 25.82 in the "High V olatility & High
Demand" scenario. This indicates its robust ability to capitalize on profit opportunities in both highly
active and more stable, liquid markets. Compared to the traditional models, the Finetuned Flow
Policy generally matches or surpasses the PnL of AS, GLFT, and GLFT-drift in most scenarios,
particularly excelling in high demand situations. The RL-PPO model, while adaptive, consistently
shows lower PnL figures across all tested environments, underscoring the superior profit extraction of
the FlowHFT framework.
Table 1: Parameters for Market Conditions: Hurst Exponent H = 0.5, Drift Rate µ = 0, volatility
(σ: {0.02, 0.25}) and arrival rate ( µ: {25, 50}). The linear finetuning (ax+b) are the following:
HH: action+[0.15,0.24], HL: action+[0.1,0.2], LH: action+[-0.1,0.1], LL: action+[-0.3,0.3], these
parameters can be chosen from an interval, just pick a point as representation The evaluation metrics
are tested out of sample, with each methods are tested 1 million trails to obtain significance and
convergence.
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
AS 24.22 0.09 241.65 13.54 0.09 125.78 25.20 1.05 7.66 13.67 0.72 6.61
GLFT 25.10 0.37 60.57 13.56 0.24 52.55 25.87 1.17 6.95 13.91 0.78 6.14
GLFT-drift 25.10 0.37 60.57 13.56 0.24 52.55 25.87 1.17 6.95 13.91 0.78 6.14
RL-PPO 14.76 0.10 133.61 9.29 0.08 103.85 26.74 0.81 10.13 19.80 0.46 14.56
Pretrained Flow Policy 21.99 0.34 56.94 13.28 0.23 53.43 22.29 1.5 4.07 12.10 0.91 4.2
Finetuned Flow Policy 25.82 0.38 58.38 14.43 0.26 49.64 26.79 1.62 3.62 22.31 0.96 5.17
The FlowHFT framework, with its flow matching policy, is designed to synthesize knowledge from
numerous expert instructors. While our extensive experiments confirm its learning capabilities
across many experts, we conduct a analysis to demonstrate its scaling law: that is, how performance
improves as the model learns from an increasing number of distinct expert strategies. The results of
this scaling analysis are presented in Figure 5.
Figure 5 illustrates the scaling properties of our FlowHFT framework, supporting the hypothesis that
the model benefits from exposure to an increasing number of expert strategies. Two key observations
underscore this scaling law. First, with an increase in the number of expert instructors used during
training, the framework’s performance consistently improves over configurations with fewer experts.
8

Table 2: Performance Comparison Under Different Conditions (Hurst Exponent H = 0 .2, Drift
Rate µ = 0.02).Same measures as the above table. Diffusion Policy select GLFT-drift strategy as
the expert to learn from. The linear finetuning (ax+b) for each action is HH: action+[-0.1,0.1], HL:
action+[-0.1,0.1], LH: action+[-0.2,0.2], LL: action+[-0.3,0.3], these parameters can be chosen from
multiple choices, just pick one as representation
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
GLFT 29.14 0.35 136.07 15.77 0.23 116.71 29.27 0.86 42.06 16.1 0.57 35.81
GLFT-drift 29.96 0.36 136.4 16.53 0.24 117.15 35.23 0.96 44.55 21.2 0.69 38.11
Pretrained Flow Policy 26.67 0.35 121.2 14.9 0.21 114.29 26.5 1.11 27.2 14.52 0.67 27.05
Finetuned Flow Policy 31.3 0.36 140.71 18.41 0.24 127.55 38.6 1.14 42.58 28.07 0.75 49.98
Figure 5: Scaling analysis showing the relationship between the Number of Instructors (expert
models) used in training FlowHFT and its resulting performance, as measured by Sharpe Ratio (blue
bars, left y-axis) and Maximum Drawdown (red line, right y-axis).
This progressive improvement indicates that FlowHFT effectively learns and integrates new, valuable
strategic information from additional experts. Second, this enhanced learning translates into more
robust risk-adjusted returns; not only does the Sharpe Ratio increase, but the Maximum Drawdown
(red line) simultaneously shows a general decline. This continuous improvement in both return and
risk metrics as more expert knowledge is incorporated suggests that FlowHFT is adept at leveraging a
broader set of specialized strategies to find more consistently superior actions across diverse market
conditions.
6 Conclusion
In conclusion, we propose a novel imitation learning framework FlowHFT, the first flow matching
policy-based approach in a financial stochastic control task. Our findings confirm that it has ability
to learn effective trading strategies in various stochastic environments in one model, thus enabling
prompt adaptation to prevailing market conditions. Furthermore, the incorporated grid search mech-
anism successfully refines actions, especially in situations where these experts were suboptimal.
In terms of profit generation, FlowHFT’s advantage over traditional models is evident through its
achievement of greater cumulative returns, a superior Sharpe ratio indicating better risk-adjusted per-
formance, and a reduced maximum drawdown signifying lower downside risk. Therefore, FlowHFT
represents a promising advancement in the development of adaptive and high-performance HFT
strategies.
9

References
[1] Yacine Ait-Sahalia and Mehmet Saglam. High frequency market making: Implications for
liquidity. Available at SSRN 2908438, 2017.
[2] Marco Avellaneda and Sasha Stoikov. High-frequency trading in a limit order book.Quantitative
Finance, 8(3):217–224, 2008.
[3] Emmanuel Bacry, Ignazio Mastromatteo, and Jean-François Muzy. Hawkes processes in finance.
Market Microstructure and Liquidity, 1(1):1550005, 2015.
[4] Antonio Briola, Jeremy Turiel, Riccardo Marcaccioli, Alvaro Cauderan, and Tomaso Aste. Deep
reinforcement learning for active high frequency trading. arXiv preprint arXiv:2101.07107,
2021.
[5] Álvaro Cartea, Sebastian Jaimungal, and Jason Ricci. Buy low, sell high: A high frequency
trading perspective. SIAM Journal on Financial Mathematics, 5(1):415–444, 2014.
[6] Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ
Tedrake, and Shuran Song. Diffusion policy: Visuomotor policy learning via action diffusion.
The International Journal of Robotics Research, 2024.
[7] Quan Dao, Hao Phung, Binh Nguyen, and Anh Tran. Flow matching in latent space. arXiv
preprint arXiv:2307.08698, 2023.
[8] Zihan Ding, Yanhua Huang, Hang Yuan, and Hao Dong. Introduction to reinforcement learning.
Deep reinforcement learning: fundamentals, research and applications, pages 47–123, 2020.
[9] Pietro Fodra and Mauricio Labadie. High-frequency market-making with inventory constraints
and directional bets. arXiv preprint arXiv:1206.4810, 2012.
[10] Kevin Frans, Danijar Hafner, Sergey Levine, and Pieter Abbeel. One step diffusion via shortcut
models. arXiv preprint arXiv:2410.12557, 2024.
[11] Prakhar Ganesh and Puneet Rakheja. Deep reinforcement learning in high frequency trading.
arXiv preprint arXiv:1809.01506, 2018.
[12] Olivier Guéant. The Financial Mathematics of Market Liquidity: From optimal execution to
market making. CRC Press, 2016.
[13] Olivier Guéant, Charles-Albert Lehalle, and Joaquin Fernandez-Tapia. Dealing with the in-
ventory risk: a solution to the market making problem. Mathematics and financial economics,
7:477–507, 2013.
[14] Larry Harris. Trading and exchanges: Market microstructure for practitioners. Oxford university
press, 2002.
[15] Alan G Hawkes. Point spectra of some mutually exciting point processes. Journal of the Royal
Statistical Society: Series B (Methodological), 33(3):438–443, 1971.
[16] Jonathan Ho, Ajay Jain, and Pieter Abbeel. Denoising diffusion probabilistic models. Advances
in neural information processing systems, 33:6840–6851, 2020.
[17] Michael Janner, Yilun Du, Joshua B Tenenbaum, and Sergey Levine. Planning with diffusion
for flexible behavior synthesis. arXiv preprint arXiv:2205.09991, 2022.
[18] Jihyeong Jeon, Jiwon Park, Chanhee Park, and U Kang. Frequant: A reinforcement-learning
based adaptive portfolio optimization with multi-frequency decomposition. In Proceedings
of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining , pages
1211–1221, 2024.
[19] Leslie Pack Kaelbling, Michael L Littman, and Andrew W Moore. Reinforcement learning: A
survey. Journal of artificial intelligence research, 4:237–285, 1996.
[20] Jens Kober, J Andrew Bagnell, and Jan Peters. Reinforcement learning in robotics: A survey.
The International Journal of Robotics Research, 32(11):1238–1274, 2013.
10

[21] Robert A Korajczyk and Dermot Murphy. High-frequency market making to large institutional
trades. The Review of Financial Studies, 32(3):1034–1067, 2019.
[22] Günter Last and Mathew Penrose. Lectures on the Poisson process, volume 7. Cambridge
University Press, 2017.
[23] Baron Law and Frederi Viens. Market making under a weakly consistent limit order book
model. High Frequency, 2(3-4):215–238, 2019.
[24] Yaron Lipman, Ricky Hagaj, and Daniel Cohen-Or. Flow matching for generative modeling.
arXiv preprint arXiv:2210.02747, 2022.
[25] Yaron Lipman, Marton Havasi, Peter Holderrieth, Neta Shaul, Matt Le, Brian Karrer, Ricky TQ
Chen, David Lopez-Paz, Heli Ben-Hamu, and Itai Gat. Flow matching guide and code. arXiv
preprint arXiv:2412.06264, 2024.
[26] Ananth Madhavan. Market microstructure: A survey. Journal of financial markets, 3(3):205–
258, 2000.
[27] Robert C Merton. Option pricing when underlying stock returns are discontinuous. Journal of
Financial Economics, 3(1-2):125–144, 1976.
[28] Peter Mörters and Yuval Peres. Brownian motion, volume 30. Cambridge University Press,
2010.
[29] Rishi K Narang. Inside the black box: A simple guide to quantitative and high-frequency
trading. John Wiley & Sons, 2013.
[30] Donovan Platt and Tim Gebbie. The problem of calibrating an agent-based model of high-
frequency trading. arXiv preprint arXiv:1606.01495, 2016.
[31] Martin L Puterman. Markov decision processes. Handbooks in operations research and
management science, 2:331–434, 1990.
[32] Molei Qin, Shuo Sun, Wentao Zhang, Haochong Xia, Xinrun Wang, and Bo An. Earnhft:
Efficient hierarchical reinforcement learning for high frequency trading. In Proceedings of the
AAAI Conference on Artificial Intelligence, volume 38, pages 14669–14676, 2024.
[33] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov. Proximal
policy optimization algorithms, 2017. arXiv preprint arXiv:1707.06347.
[34] Jascha Sohl-Dickstein, Eric Weiss, Niru Maheswaranathan, and Surya Ganguli. Deep unsuper-
vised learning using nonequilibrium thermodynamics. In International conference on machine
learning, pages 2256–2265. pmlr, 2015.
[35] Yang Song, Jascha Sohl-Dickstein, Diederik P Kingma, Abhishek Kumar, Stefano Ermon, and
Ben Poole. Score-based generative modeling through stochastic differential equations. arXiv
preprint arXiv:2011.13456, 2020.
[36] Zhendong Wang, Jonathan J Hunt, and Mingyuan Zhou. Diffusion policies as an expressive
policy class for offline reinforcement learning. arXiv preprint arXiv:2208.06193, 2022.
[37] Qinglun Zhang, Zhen Liu, Haoqiang Fan, Guanghui Liu, Bing Zeng, and Shuaicheng Liu.
Flowpolicy: Enabling fast and robust 3d flow-based policy via consistency flow matching
for robot manipulation. In Proceedings of the AAAI Conference on Artificial Intelligence ,
volume 39, pages 14754–14762, 2025.
[38] Weipeng Zhang, Tao Yin, Yunan Zhao, Bing Han, and Huanxi Liu. Reinforcement learning for
stock prediction and high-frequency trading with t+ 1 rules. IEEE Access, 11:14115–14127,
2022.
[39] Zihao Zhang, Stefan Zohren, and Stephen Roberts. Deep reinforcement learning for trading.
arXiv preprint arXiv:1911.10107, 2019.
11

[40] Yuheng Zheng and Zihan Ding. Reinforcement learning in high-frequency market making.
arXiv preprint arXiv:2407.21025, 2024.
[41] Chuqiao Zong, Chaojie Wang, Molei Qin, Lei Feng, Xinrun Wang, and Bo An. Macrohft:
Memory augmented context-aware reinforcement learning on high frequency trading. In
Proceedings of the 30th ACM SIGKDD Conference on Knowledge Discovery and Data Mining,
pages 4712–4721, 2024.
A Expert Market-Making Models
A.1 Avellaneda-Stoikov (AS) Model
The Avellaneda-Stoikov (AS) model [2] optimizes bid and ask spreads by maximizing the expected
utility of terminal wealth. Taking the coefficients of drift, jump intensity, self-excitation and mutual-
excitation to be zero in above settings , The value function u(s, x, q, t) is governed by the Hamilton-
Jacobi-Bellman (HJB) equation (details in Appendix):
∂u
∂t + 1 2 σ2 ∂2u ∂s2 + max δb λb (δb) [u (s, x− s + δb, q+ 1, t) − u(s, x, q, t)]
+ max
δa
λa (δa) [u (s, x+ s + δa, q− 1, t) − u(s, x, q, t)] = 0, (7)
with terminal condition u(s, x, q, T) = −e−γ(x+qST ).
The optimal bid and ask spreads are:
δAS bid = γσ 2τ 2 + 1 γ ln  1 + γ k  − qγσ 2τ, (8)
δAS ask = γσ 2τ 2 + 1 γ ln  1 + γ k  + qγσ 2τ, (9)
In the model, γ is defined as the risk aversion parameter, which quantifies the trader’s preference for
avoiding risk relative to seeking returns. The variable σ represents the asset’s volatility, indicating
the degree of price fluctuation over time. The term τ = T − t denotes the remaining time horizon,
calculating the time left until the end of the trading period. The parameter k measures the sensitivity
of order arrivals to price spreads, demonstrating how spread changes influence trading activity. Lastly,
q is the current inventory level, reflecting the amount of the asset held by the trader.
A.2 Guéant-Lehalle-Fernandez-Tapia (GLFT) Model
The Guéant-Lehalle-Fernandez-Tapia (GLFT) model [13] offers an approximate solution for optimal
spreads by incorporating additional terms into the HJB equation. The assumptions are keeping the
same as AS model expect. There is no limitation to the terminal time T. The optimal spreads are:
c1 = 1 γ ln  1 + γ k  , (10)
c2 =
s
γ
2Ak

1 + γ k ( k γ +1) , (11)
δGLFT bid = c1 + σc2 2 + σc2q, (12)
δGLFT ask = c1 + σc2 2 − σc2q, (13)
(14)
12

In the model, A denotes the base arrival rate of orders. The coefficients c1 and c2 are used to adjust
the bid and ask spreads based on factors such as risk aversion, volatility, and time horizon. Lastly, q
represents the current inventory level, indicating the amount of the asset that is held.
A.3 Modified Guéant-Lehalle-Fernandez-Tapia (GLFT) Model with Drift
Keeping everything unchanged except for the drift part, the new modified GLFT solution which
hasn’t been shown in the original paper[13].
|q| = Qmax
dSt = µdt + σdWt
(δb ∞)∗ = 1 γ ln(1 + γ k ) +  − µ γσ 2 + 2q + 1 2  r σ2 2kA (1 + γ k )1+ k γ
(δa ∞)∗ = 1 γ ln(1 + γ k ) +  µ γσ 2 − 2q − 1 2  r σ2 2kA (1 + γ k )1+ k γ
A.4 Proximal Policy Optimization (PPO) for High-Frequency Market Making
To apply Proximal Policy Optimization (PPO) in a high-frequency trading (HFT) environment, we
formulate the trading process as a Markov Decision Process (MDP). The input to the policy model
consists of high-dimensional market state features, such as limit order book snapshots, recent trade
volumes, price trends, and microstructure indicators sampled at millisecond intervals. The action
space can include discrete actions like placing a buy/sell/cancel order at a specific price level. The
reward function is designed to capture profit-and-loss (PnL) adjusted for market impact and inventory
risk, including components like realized spread, execution cost, and inventory penalties. The objective
is to train a policy that maximizes expected cumulative rewards.
In the context of market making, the RL framework can be formalized as a Markov Decision Process
(MDP) defined by the tuple (S, A, P, R, γ), where, S represents the state space, and A denotes the
action space. The state transition probabilities are symbolized by P , which dictates the likelihood
of transitioning from one state to another given a particular action. R is the reward function, which
assigns a reward based on the state and action taken. Finally, γ ∈ [0, 1] is the discount factor, used
to determine the present value of future rewards, allowing for the evaluation of long-term versus
immediate benefits.
For the space state, at each discrete time stept, the state st encapsulates essential information required
for decision-making:
st = (t, xt, qt, St, Bt−1 − At−1),
In the model, t is the timestamp indicating the specific point in time under consideration. The variable
xt denotes the current cash position, while qt represents the current inventory, which refers to the
number of shares held. The term St is the current underlying stock price, providing a snapshot of the
stock’s market value at time t. At−1 − Bt−1 is the difference between the ask and bid quotes from
the previous time step, reflecting the spread.
For the action space, the agent’s action at consists of setting new ask and bid quotes relative to the
mid-price Mt. Specifically:
at = (δask t , δbid t ),
In the model, δaskt represents the offset of the ask quote from the mid-price, which sets the ask price
to Mt + δaskt. Conversely, δbidt is the offset of the bid quote from the mid-price, setting the bid
price to Mt − δbidt.
For the reward function, it is designed to balance profitability from the bid-ask spread against the risk
associated with inventory holding. The formulation is:
rt = PnLt − λq2 t ,
13

P nLt represents the profit and loss at time t, derived from executed trades. The parameter λ is a risk
aversion parameter that penalizes large inventory positions.
After defining the MDP, policy gradient methods is used to optimize the policyπθ(a|s) parameterized
by θ to maximize the expected cumulative reward:
J(θ) = Eτ ∼πθ
" TX
t=0
γtrt
#
,
where τ = (s0, a0, s1, a1, . . . , sT ) denotes a trajectory sampled from the policy. The output of the
policy network is a parameterized probability distribution over actions, from which the actual trading
action is sampled. The derivation related to policy gradient is in Appendix.
B Calculation of Evaluation Metrics
1. Cumulative Return (CR)
The Cumulative Return measures the total percentage change in the value of an investment over a
specific period.
If ri is the return for period i, and there are n periods:
CR =
 nY
i=1
(1 + ri) − 1
!
× 100%
where:
• ri: Return for period i.
• n: Total number of periods.
2. Sharpe Ratio (SR)
The Sharpe Ratio measures the risk-adjusted return of an investment or strategy. It quantifies the
average return earned in excess of the risk-free rate per unit of volatility or total risk.
SR = E[Rp − Rf ] σp
where:
• E[Rp − Rf ]: The expected value of the excess return of the portfolio over the risk-free rate.
• ¯Rp: The average (sample mean) return of the portfolio or investment over a period.
• ¯Rf : The average (sample mean) risk-free rate of return over the same period (e.g., yield on
short-term government bonds).
• σp: The standard deviation of the portfolio’s excess returns ( Rp − Rf ). (Sometimes, the
standard deviation of the portfolio’s returns, σ(Rp), is used as an approximation, especially
if Rf is constant or has very low volatility).
3. Maximum Drawdown (MDD)
The Maximum Drawdown is the largest percentage drop in the value of an investment or portfolio
from a previous peak to a subsequent trough over a specific period. Let V (t) be the value of the
portfolio at time t over the period [0, T].
First, define the running peak value up to time t as M (t):
M (t) = max
0≤τ ≤t
V (τ )
14

Then, the drawdown D(t) at any time t is:
D(t) = M (t) − V (t) M (t)
The Maximum Drawdown (MDD) is the maximum value of D(t) over the entire period:
MDD = max
0≤t≤T
D(t)
This MDD is usually expressed as a positive percentage (e.g., an MDD of 0.25 means a 25% maximum
loss from a peak).
where:
• V (t): Value of the investment at time t.
• T : The end of the observation period.
• τ: A time index variable ranging from 0 to t.
C Parameters for Test Environemnt
Figure 6: Parameters settings of testing market environement
Stock Price Movement
Brownian motion
(1) Hurst Component !
       The degree of long-term memory or persistence
       predominantly (H > 0.5), mean-reverting (H<0.5), random (H=0.5)
(2) Drift "
       Controls the deterministic
       Underlying trend around which the random fluctuations (volatility) of the process occur
(3) Volatility #
      Dictates the magnitude or scale of the random
      Unpredictable fluctuations around the process's average trend (drift)
(4) Sudden Market Jump $
       An abrupt, large, and discontinuous change in asset prices
(5) Time step %!
(1) Liquidity "","#
       Tradable volume offered at various bid and ask price levels
(2) Self-exciting '""	(buy−to−buy),'## (sell-to-sell),
       How the arrival of an order temporarily increases the probability of more orders of the
       same type arriving shortly thereafter
(3) Cross-exciting '"#
       How the arrival of one type of order influences the arrival rate of orders of the other type
Order Book
Hawkes Process
Parameters Settings
[0.2, 0.5, 0.8]
[0, 0.2]
[0.02, 0.25]
[0.02]
[0.01, 0.02]
[25, 50]
[0.7]
[0.3]
D Results for Different Market Conditions
15

Table 3: Performance Comparison Under Different Conditions (Hurst Exponent H = 0 .5, Drift
Rate µ = 0.02).Same measures as the above table. Flow Policy select GLFT-drift strategy as the
expert to learn from. The linear finetuning (ax+b) for each action is HH: action+[0.1,0.25], HL:
action+[0.1,0.2], LH: action+[-0.3,0.3], LL: action+[-0.4,0.7], these parameters can be chosen from
multiple choices, just pick one as representation
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
AS 24.16 0.08 245.49 13.51 0.09 127.70 25.18 0.92 8.02 13.61 0.63 6.98
GLFT 25.11 0.36 61.39 13.55 0.23 53.26 25.21 0.99 7.45 13.62 0.66 6.59
GLFT-drift 25.87 0.37 61.26 14.15 0.24 53.21 40.82 1.10 7.69 26.44 0.87 6.97
RL-PPO 30.74 0.16 186.1 20.47 0.14 138.88 24.79 0.72 10.58 32.49 0.65 15.28
Pretrained Flow Policy 22.72 0.35 57.09 13.28 0.23 53.43 21.90 1.64 3.97 11.96 0.98 4.05
Finetuned Flow Policy 27.45 0.39 61.31 15.15 0.26 50.95 42.81 1.17 8.44 27.12 0.93 7.42
Tables 4 to 6 expand the volatility and arrival rate options to investigate a broader spectrum of unseen
scenarios. (V olatility,σ: {0.05, 0.2}) and arrival rates, µ: {30, 60})
Table 4: Performance Comparison Under Different Conditions (Hurst Exponent H = 0 .2, Drift
Rate µ = 0.0). Same measures as the above table. Diffusion Policy select GLFT-drift strategy as
the expert to learn from. The linear finetuning (ax+b) for each action is HH: action+[0.02,0.2], HL:
action+[0.05,0.15], LH: action+[-0.15,0.15], LL: action+[-0.1,0.1], these parameters can be chosen
from multiple choices, just pick one as representation
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
AS 28.82 0.14 346.8 16.23 0.13 216.69 29.28 0.78 48.86 16.16 0.54 40.22
GLFT 29.16 0.36 134.33 15.78 0.23 115.22 29.29 0.92 41.34 16.1 0.61 35.2
GLFT-drift 29.16 0.36 134.33 15.78 0.23 115.22 29.29 0.92 41.34 16.1 0.61 35.2
Pretrained Flow Policy 26.61 0.35 119.73 14.76 0.22 112.78 26.56 1.16 26.76 14.61 0.71 26.58
Finetuned Flow Policy 29.72 0.36 136.52 15.80 0.23 114.62 31.43 1.06 36.25 16.82 0.75 29.33
16

Table 5: Performance Comparison Under Different Conditions (Hurst Exponent H = 0 .8, Drift
Rate µ = 0.0).Same measures as the above table. Diffusion Policy select GLFT-drift strategy as the
expert to learn from. The linear finetuning (ax+b) for each action is HH: action+[-0.02, 0.1], HL:
action+[0.1, 0.1], LH: action+[-0.1, 0.1], LL: action+[-0.1, 0.1], these parameters can be chosen from
multiple choices, just pick one as representation
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
GLFT 29.00 0.57 21.05 15.77 0.36 19.88 29.21 1.10 6.63 16.07 0.73 6.38
GLFT-drift 29.00 0.57 21.05 15.77 0.36 19.88 29.21 1.10 6.63 16.07 0.73 6.38
Pretrained Flow Policy 26.33 0.67 17.37 14.53 0.36 19.26 26.61 1.66 3.80 14.45 0.93 4.57
Finetuned Flow Policy 30.31 0.67 17.77 17.61 0.39 19.66 29.59 1.50 3.42 16.65 0.96 4.22
Table 6: Performance Comparison Under Different Conditions (Hurst Exponent H = 0.8, Drift Rate
µ = 0.02).Same measures as the above table. Diffusion Policy select GLFT-drift strategy as the
expert to learn from. The linear finetuning (ax+b) for each action is HH: action+[-0.1, 0.1], HL:
action+[-0.1, 0.1], LH: action+[-0.1, 0.1], LL: action+[-0.1, 0.1], these parameters can be chosen
from multiple choices, just pick one as representation
High V olatility & High Demand High V olatility & Low Demand Low V olatility & High Demand Low V olatility & Low Demand
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
GLFT 28.98 0.56 21.46 15.76 0.35 20.23 29.19 1.00 6.95 16.07 0.67 6.68
GLFT-drift 30.05 0.57 21.08 16.74 0.37 19.94 35.22 1.11 5.71 21.24 0.80 5.60
Pretrained Flow Policy 26.64 0.66 17.57 14.52 0.34 19.47 26.74 1.61 3.79 14.50 0.87 4.68
Finetuned Flow Policy 33.17 0.62 19.64 19.20 0.38 20.61 32.57 1.61 3.01 19.02 1.01 3.80
E Limitations
While FlowHFT demonstrates promising capabilities, certain limitations in the current study should be
acknowledged. One limitation of the current study is its focused scope, with the FlowHFT framework
being developed and evaluated exclusively for a single financial asset trading on a single exchange.
While this controlled setting allows for a detailed analysis of the framework’s core mechanics and
learning capabilities, we can further address the broader complexities and rich dynamics present in
multi-asset or multi-exchange HFT operations. For instance, this study can explore how FlowHFT
would manage inter-asset correlations, portfolio-level risk diversification, or the strategic allocation
of capital across different instruments. Similarly, the challenges and opportunities arising from
operating across multiple exchanges—such as navigating varying fee structures, latency differences,
diverse order book microstructures, and potential inter-exchange arbitrage—remain outside the
current investigation. Therefore, a significant and crucial avenue for future research is the extension
and evaluation of the FlowHFT framework to multi-asset and multi-exchange environments. This
would involve adapting the state and action representations, potentially incorporating mechanisms to
learn cross-asset dependencies, and developing policies capable of sophisticated order routing and
execution across different trading venues. Successfully addressing these aspects would substantially
broaden FlowHFT’s applicability and provide a more comprehensive validation of its potential as a
robust solution for real-world high-frequency trading.
F Related Work
F.1 Traditional Models for High Frequency Trading
High-Frequency Trading (HFT) is a subset of algorithmic trading characterized by exceptionally high
speeds of order execution and substantial turnover rates. Market making involves the continuous
placement of limit orders—both bids (buy orders) and asks (sell orders)—aimed at capturing the
bid-ask spread, which is the difference between the highest price a buyer is willing to pay and the
lowest price a seller is willing to accept [23, 21]. Traditional models typically formulate the market
maker’s decision-making process as a stochastic optimal control problem, aiming to devise quoting
strategies that maximize predefined objectives (e.g., expected utility of profits) while managing
associated risks (e.g., inventory risk) [9].
17

The Avellaneda-Stoikov (AS) model [2] is a prominent example within HFT literature. This opti-
mization approach is formulated as maximizing the expected utility of the market maker’s terminal
wealth at a predetermined finite terminal time. Several key assumptions underpin the AS model:
the mid-price of the asset follows an arithmetic Brownian motion without drift [28]; the arrival of
market buy and sell orders is modeled as independent Poisson processes [22]; and the market maker
continuously adjusts bid and ask quotes based on changes in the mid-price and inventory levels,
without incurring explicit updating or cancellation costs. Moreover, the AS model often assumes
liquidation of inventory (achieving a zero inventory position) by a specified terminal time T, typically
the end of the trading day—an assumption potentially unsuitable for assets traded continuously, such
as foreign exchange or cryptocurrencies.
The Guéant-Lehalle-Fernandez-Tapia (GLFT) model [13] represents another widely adopted tradi-
tional approach. A central motivation behind its development was to address certain practical and
theoretical limitations of the AS model. Notably, the GLFT model does not depend explicitly on a
predetermined finite terminal time, making it more suitable for continuously traded assets or markets
operating over extended periods. However, a fundamental challenge shared with the AS model is the
reliance on historical market data for calibrating key parameters, such as trading intensity coefficients
and volatility [12]. Such calibration processes are practically challenging. Empirical evidence also
suggests that the exponential form of the trading intensity function may inadequately capture complex
relationships between quote depth and execution probability across varying market conditions or
price levels. Even if parameters initially derived from the GLFT model are optimal, they tend to
become suboptimal quickly as market conditions evolve, necessitating frequent recalibrations—an
approach both computationally intensive and susceptible to estimation errors [30].
F.2 Reinforcement Learning Techniques in High Frequency Trading
Reinforcement learning (RL) enables an agent to learn rapid, sequential trading decisions by continu-
ously interacting with the market environment [19]. The appeal of RL in HFT stems from its inherent
capability to learn adaptive strategies within dynamic, complex financial environments [4].
The application of RL to HFT typically involves formulating the trading problem as a Markov
Decision Process (MDP) [31]. Under this formulation, the HFT environment (e.g., financial market
or order book) evolves through a series of states. The RL agent, representing the trading algorithm,
observes the current market state and selects an action (such as placing buy orders, canceling existing
orders, or holding positions). Subsequently, the environment transitions to a new state, providing the
agent with a numerical reward or penalty reflecting the immediate outcome of its action (e.g., profit
or loss). The ultimate objective of the RL agent is to derive an optimal policy that specifies the best
action to take in any given state, maximizing the expected cumulative discounted reward over time
[8].
A variety of RL algorithms have been explored for HFT. Q-learning and its deep learning extension,
Deep Q-Networks (DQN), along with variants such as Double DQN (DDQN), are widely employed
for optimal execution and adaptive trading strategies, as they help reduce overestimation bias [32,
4, 38]. Actor-Critic methods—which combine policy-based and value-based learning—are also
extensively used. Examples include Advantage Actor-Critic (A2C/A3C), enabling parallel learning
[39]; Deep Deterministic Policy Gradient (DDPG), well-suited to continuous action spaces like setting
order prices or sizes [18]; and Soft Actor-Critic (SAC), which enhances exploration through entropy
regularization [29]. Proximal Policy Optimization (PPO) is preferred for its stability and sample
efficiency, particularly valuable in dynamic market-making scenarios [ 41]. To capture temporal
dependencies inherent in financial time series, Recurrent Reinforcement Learning (RRL) is used,
while Nash Q-learning addresses multi-agent interactions common in competitive market-making
environments [40].
Despite the advantages, RL strategies in finance are prone to instability. Financial markets are
inherently non-stationary; their statistical properties—including mean, variance, and correlations
among assets or indicators—change over time. Patterns and relationships valid in one period may
fail to generalize subsequently. Consequently, an RL agent trained on historical data representing
a particular market regime (e.g., low-volatility trending market) may perform poorly or fail when
conditions shift to a new regime (e.g., high-volatility range-bound market).
18

F.3 Flow Matching Model in Control
Flow Matching (FM) has recently emerged as a compelling paradigm in generative modeling, provid-
ing an innovative approach to learning complex data distributions [24, 7]. FM learns transformations
that map samples from a simple, well-defined prior distribution (typically an isotropic Gaussian, often
termed "noise") to emulate complex target distributions.
Flow matching has been widely adopted in robotics, particularly for generating smooth, continuous
control actions for complex tasks [25, 37]. Its primary benefit is the ability to learn velocity fields
that directly correspond to how robot actions should evolve over time. For example, tasks involving
manipulation or humanoid locomotion benefit from FM’s capability to produce sequences of joint
movements that are inherently smooth and temporally consistent. This results in predictable and
reliable robotic behaviors, facilitating effective interactions with physical environments. Additionally,
conditioning flows on inputs like sensor data or task objectives allows robots to develop versatile
policies adaptable to changing circumstances while preserving smooth trajectories.
The motivation to adapt flow matching from robotic control to financial markets, specifically HFT,
stems from shared challenges: both domains require sophisticated and continuous sequences of
actions responsive to high-dimensional, rapidly changing environments. In robotics, FM excels at
generating smooth, multi-modal trajectories by learning velocity fields to guide robot actions over
time. In HFT, analogous "actions" are buy/sell orders, and the "environment" is the continuously
evolving market data.
However, applying flow matching to real-world HFT introduces a critical challenge: transaction speed.
Solving the underlying ordinary differential equations (ODEs) usually requires numerous iterative
steps, resulting in significant computational costs. To address this, shortcut policies [ 10] provide
an effective solution by enabling the inference process to execute within a small, fixed number of
steps—greatly reducing latency.
G Ablation Study
To validate that our FlowHFT framework indeed learns from the provided expert strategies, we
conducted an ablation study. We train FlowHFT model to imitate different sources: (1) purely random
actions, (2) only the Avellaneda-Stoikov (AS) model, and (3) only the Guéant-Lehalle-Fernandez-
Tapia (GLFT) model. The performance of each resulting imitation learning model was subsequently
benchmarked against its corresponding source expert—namely, the original traditional AS and GLFT
models.
Our results provide clear evidence that FlowHFT successfully learns strategies from expert demon-
strations. The model trained on random actions demonstrated the poorest performance, yielding
significantly lower PnL and Sharpe Ratios, thus confirming that it failed to learn any meaningful
trading strategy. In contrast, the FlowHFT model trained on the AS expert exhibited significantly
improved performance compared to the random baseline, achieving metrics comparable to those of
the original AS model under identical market conditions. This finding strongly suggests successful
imitation of the AS trading strategy. Furthermore, the FlowHFT model trained using the GLFT
demonstrations outperformed the AS-imitating model, closely approaching the performance of the
original GLFT expert. Considering that the GLFT model is explicitly designed to address certain
limitations inherent in the AS model and typically yields superior performance, this outcome provides
compelling evidence that FlowHFT effectively captures and replicates the sophisticated strategies of
advanced expert models.
Table 7: Parameters for Market Conditions: Hurst Exponent H = 0.5, Drift Rate µ = 0, volatility (σ:
{0.02, 0.25}) and arrival rate (µ: {25, 50}).
High V ol. & High Demand (HH) High V ol. & Low Demand (HL) Low V ol. & High Demand (LH) Low V ol. & Low Demand (LL)
PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓ PnL ↑ SR ↑ MDD ↓
Random Action 2.13 0.07 28.45 1.09 0.05 19.25 2.13 0.31 2.7 1.1 0.22 1.86
AS Expert 24.22 0.09 241.65 13.54 0.09 125.78 25.20 1.05 7.66 13.67 0.72 6.61
GLFT-drift Expert 25.10 0.37 60.57 13.56 0.24 52.55 25.87 1.17 6.95 13.91 0.78 6.14
Learning Random Action -1.06 -0.02 52.25 -1.01 -0.02 37.77 -0.76 -0.06 6.00 -0.50 -0.06 4.24
Learning AS Only 22.09 0.12 157.54 11.95 0.10 107.11 22.88 0.62 13.25 12.55 0.51 9.06
Learning GLFT-Drift Only 22.62 0.36 58.57 12.45 0.20 57.15 23.02 1.63 4.19 12.39 0.98 4.47
19
