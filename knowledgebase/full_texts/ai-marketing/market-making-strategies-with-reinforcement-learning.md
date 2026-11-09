---
title: Market Making Strategies with Reinforcement Learning
url: https://arxiv.org/abs/2507.18680
category: ai-marketing
subcategory: empirical
date: 2025-07
venue: ''
authors:
- Óscar Fernández Vicente
source: arxiv
pdf_url: https://arxiv.org/pdf/2507.18680
pages: 156
chars: 315681
fetched_at: '2026-11-08T13:19:08+00:00'
kb_version: 1
---

# Market Making Strategies with Reinforcement Learning

Market Making Strategies with
Reinforcement Learning
by
Óscar Fernández Vicente
A dissertation submitted in partial fulfillment of the
requirements for the degree of Doctor of Philosophy in
COMPUTER SCIENCE AND TECHNOLOGY
Universidad Carlos III de Madrid
Advisors:
Fernando Fernández Rebollo
Francisco Javier García Polo
Tutor:
Fernando Fernández Rebollo
<January 2025>

This thesis is distributed under license “Creative Commons Atributtion - Non
Commercial - Non Derivatives”.

ACKNOWLEDGEMENTS
Quiero dar las gracias en especial a mis directores, Fernando y Javier por guiarme en
todo este largo e intenso camino. Sin su conocimiento, dedicación y apoyo no hubiera
sido posible conseguir este gran hito. Sin duda es una suerte haber caído de su lado. De
igual forma agradecer a los miembros del Tribunal, Daniel, Inés y Juan Ramón, por su
profesionalidad y sus más que relevantes aportaciones en la mejora de la Tesis.
Mención especial, por supuesto, a mi familia por el cariño y la paciencia, especial-
mente a Lina, durante todo el desarrollo de la investigación. A veces se hace cuesta arriba
y es un lujo poder contar con personas así. Sin olvidarme tampoco de los Warriors, que
siempre están ahí cuando se les necesita.
Y por último, y como no puede ser de otra manera, a toda la gente, cercana o lejana,
apasionados por este complejo y emocionante campo que aportan cada día su granito de
arena para conseguir grandes avances.

Funding Acknowledgements
This research was funded in part by JPMorgan Chase & Co. Any views or opinions
expressed herein are solely those of the authors listed, and may differ from the views and
opinions expressed by JPMorgan Chase & Co. or its a ffiliates. This material is not a
product of the Research Department of J.P. Morgan Securities LLC. This material should
not be construed as an individual recommendation for any particular client and is not
intended as a recommendation of particular securities, financial instruments or strategies
for a particular client. This material does not constitute a solicitation or o ffer in any
jurisdiction.
iii

PUBLISHED AND SUBMITTED CONTENT
The compilation of research articles published in peer-reviewed journals and confer-
ence presentations conducted throughout this dissertation is as follows:
Journal Papers
• Vicente, O.F., Fernández, F., García, J.: Automated market maker inventory man-
agement with deep reinforcement learning. Applied Intelligence (2023) https:
//doi.org/10.1007/s10489-023-04647-9. Contributor author. Included in
Section 4.1.
International Conference Papers
• Vicente, O.F., Fernández, F., García, J. Deep q-learning market makers in a multi-
agent simulated stock market. In: Proceedings of the Second ACM International
Conference on AI in Finance. Association for Computing Machinery, New York,
NY , USA, ICAIF ’21 (2022)https://doi.org/10.1145/3490354.3494448 .Con-
tributor author. Included in Chapter 3.
Unplublished Papers
• Vicente, O.F., García, J., Fernández, F.: Optimizing market making Strategies: A
Multi-Objective Reinforcement Learning Approach with Pareto Fronts. Submitted
to Expert Systems with Applications (2023). Contributor author. (Under second
review1). Included in Section 4.2.
• Vicente, O.F., García, J., Fernández, F.: Policy Weighting via Discounted Thomp-
son Sampling for Non-Stationary market making. Submitted to Artificial Intelli-
gence Review (2024). Contributor author. (Under review1). Included in Chapter 5.
The material from all the mentioned sources included in this thesis is not singled out
with typographic means and references.
1As of October 2024

CONTENTS
1. INTRODUCTION. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1. Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.2. Hypothesis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3. Objectives. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.4. Thesis overview . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2. BACKGROUND . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.1. RL and DRL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1.1. Markov decission process . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.1.2. Value functions in RL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.1.3. RL and DRL Algorithms . . . . . . . . . . . . . . . . . . . . . . . . . . . . 14
2.1.4. Multi-objective RL. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
2.1.5. Non-stationary RL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.2. Financial markets. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.3. Dealing with the market making problem . . . . . . . . . . . . . . . . . . . . . 23
2.3.1. Market making as a classic financial problem . . . . . . . . . . . . . . . . . 24
2.3.2. New techniques to deal with the market making problem . . . . . . . . . . 25
2.4. Simulated environments in RL. ABIDES . . . . . . . . . . . . . . . . . . . . . 26
2.5. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
3. RL IN MARKER MAKING OPERATIVE . . . . . . . . . . . . . . . . . . . . . . 35
3.1. Mapping a market making task onto a RL task . . . . . . . . . . . . . . . . . . 35
3.1.1. State and action space . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
3.1.2. Deep Q-learning MM agents (DQL-MM) . . . . . . . . . . . . . . . . . . . 37
3.2. Single-agent and multi-agent scenarios . . . . . . . . . . . . . . . . . . . . . . 39
3.3. Experiments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.3.1. Experimental setting . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
3.3.2. Single-agent market maker . . . . . . . . . . . . . . . . . . . . . . . . . . . 41
3.3.3. Multi-agent RL market makers . . . . . . . . . . . . . . . . . . . . . . . . . 43
3.3.4. Direct transfer learning in multi-agent RL market makers . . . . . . . . . . 46
v

3.4. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
3.5. Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 51
4. INVENTORY MANAGEMENT. . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.1. Reward engineering: Automated market maker inventory management with
DRL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
4.1.1. New RL model for inventory management . . . . . . . . . . . . . . . . . . 53
4.1.2. Experimental setting and methods . . . . . . . . . . . . . . . . . . . . . . . 58
4.1.3. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 76
4.1.4. Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.2. MORL with Pareto fronts . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
4.2.1. Multi-objetive RL MM: M3ORL . . . . . . . . . . . . . . . . . . . . . . . . 79
4.2.2. Methodology and experimental setup . . . . . . . . . . . . . . . . . . . . . 85
4.2.3. Experimental results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86
4.2.4. Analysis: The relevance of trend information in the proposed method . . . 95
4.2.5. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 99
4.2.6. Contributions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 100
5. AUTOMATION UNDER NON-STATIONARITY. . . . . . . . . . . . . . . . . . 102
5.1. Dealing with non-stationarity: Continual learning . . . . . . . . . . . . . . . . 102
5.2. Discounted Thompson sampling . . . . . . . . . . . . . . . . . . . . . . . . . . 104
5.3. Methodology: Multi-objective policy selection in dynamic markets . . . . . . 105
5.3.1. Market Maker as a MOMDP . . . . . . . . . . . . . . . . . . . . . . . . . . 105
5.3.2. Policy Weighting through discounted Thompson sampling (POW-dTS)
Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 105
5.4. Experimental evaluation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
5.4.1. Experimental setup. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 111
5.4.2. Results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 117
5.4.3. Ablation study . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 121
5.5. Discussion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 122
5.6. Contribution . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 123
6. CONCLUSION . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 124
6.1. Limitations of the presented research. . . . . . . . . . . . . . . . . . . . . . . . 126
vi

6.2. Future work . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 127
6.2.1. Future directions in simulated and real-world market making . . . . . . . . 127
6.2.2. LLMs and their application in trading strategies . . . . . . . . . . . . . . . 128
BIBLIOGRAPHY. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 130
A.1. Appendix: Additional AIIF plots. . . . . . . . . . . . . . . . . . . . . . . . . . 142
vii

LIST OF FIGURES
1.1 Composition of a Financial Market. Example of participants. . . . . . . . 2
1.2 Example of the impact of a MM in a low liquidity asset order book . . . . 3
1.3 A detailed depiction of the research’s evolution, including the rationale
and associated scholarly articles at each developmental phase. . . . . . . 9
2.1 RL agent and environment interactions . . . . . . . . . . . . . . . . . . . 11
2.2 Overview of multi-objective artifacts and concepts . . . . . . . . . . . . 19
2.3 Running OB example. . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
2.4 Reinforcement learning framework in ABIDES-Gym vs. regular ABIDES 28
3.1 Deep NN architecture used for the DQL-MM agent. . . . . . . . . . . . . 37
3.2 Single-agent training experiment. 50-simulation rolling average window. . 41
3.3 Evolution of epsilons throughout the single-agent experiment 50-simulation
rolling average window. . . . . . . . . . . . . . . . . . . . . . . . . . . . 42
3.4 SHAP variable importance summary plot. . . . . . . . . . . . . . . . . . 43
3.5 Multi-agent experiment. 50-simulation rolling average window. . . . . . . 44
3.6 DQL-MM #1 Epsilons buy, sell and hedge ( η) -50-simulation rolling av-
erage window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.7 DQL-MM #2 Epsilons buy, sell and hedge ( η). 50-simulation rolling av-
erage window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 45
3.8 DQL-MM #3 Epsilons buy, sell and hedge ( η). 50-simulation rolling av-
erage window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.9 NN Performance evaluation. Mean rewards obtained by every NN tested. 47
3.10 Results from the direct transfer learning experiment. 50-simulation rolling
average window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 47
3.11 Last simulations transfer learning results. 50-simulation rolling average
window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
3.12 Evolution of epsilon values in a single experiment. 50-simulation rolling
average window. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
4.1 Example of a trading session performed by a RL MM that applies the
proposed reward function with both AIIF and DITF coefficients . . . . . 53
viii

4.2 Mid-prices evolution sample. . . . . . . . . . . . . . . . . . . . . . . . . 60
4.3 Histogram of returns. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 60
4.4 Single training experiment, applying an AIIF = 0 in the reward function . 62
4.5 DQN MM training results applying di fferent AIIF . . . . . . . . . . . . . 63
4.6 DQN MM testing rounds, with di fferent AIIF factors. . . . . . . . . . . . 64
4.7 DQN MM testing’s rounds inventories, applying di fferent AIIF factors . . 64
4.8 DQN MM inventory distributions along di fferent experiments. . . . . . . 65
4.9 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 66
4.10 DQN MM inventories and thresholds along the experiment with AIIF = 1. 66
4.11 DQN MM inventories and thresholds along the experiment with AIIF = 5. 66
4.12 DQN MM buy and sell strategy distributions, in terms of prices, according
to different AIIF. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68
4.13 DQN MM hedge strategy distributions according to di fferent AIIF. . . . . 69
4.14 DQN single inventory and MtM per AIIF results are obtained from every
test experiment. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
4.15 DQN inventory and MtM in average per AIIF. . . . . . . . . . . . . . . . 70
4.16 Buy and sell amount of stock traded according to di fferent AIIF . . . . . 72
4.17 Benchmark results in terms of MtM (cash + inventory value). Training
stage . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
4.18 Benchmark results in terms of MtM(cash + inventory value). Testing stage. 75
4.19 Benchmark results in terms of Inventory distribution. . . . . . . . . . . . 76
4.20 MM DQN architecture and reward function. . . . . . . . . . . . . . . . . 81
4.21 Test results - Pareto . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
4.22 MORL Undominated front. . . . . . . . . . . . . . . . . . . . . . . . . . 88
4.23 Reward-engineered undominated fronts. . . . . . . . . . . . . . . . . . . 91
4.24 Reward-engineered undominated fronts. More details . . . . . . . . . . . 92
4.25 Comparison of normalized hypervolumes among algorithms . . . . . . . 93
4.26 Combined Pareto front from undominated solutions . . . . . . . . . . . . 94
4.27 EMAs example of di fferent trading sessions: EMA-L 20 minutes+ EMA-
S 8 minutes (left) and EMA-L 10 minutes + EMA-S 2 minutes (right). . . 96
4.28 Training results of agents with and without EMA variables in the state
space. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97
ix

4.29 Testing results of agents with and without EMA variables . . . . . . . . . 97
4.30 Training results of extended simulations with EMA and standard agents. . 98
5.1 POW-dTS flow . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 109
5.2 MtM of M 3ORL MM training with 0 and with 1 MM competitors. . . . . 112
5.3 Optimal agents trained against 0, 1, 5, and 7 M 3ORL MM competitors. . 113
5.4 MtM of M 3ORL MM agent pre-trained with 0 MM competitors. . . . . . 114
5.5 MtM of M 3ORL MM agent pre-trained with 1 MM competitor. . . . . . . 114
5.6 MtM of M 3ORL MM agent pre-trained with 5 MM competitors. . . . . . 114
5.7 MtM of M 3ORL MM agent pre-trained with 7 MM competitors. . . . . . 115
5.8 Comparison of methods’ performance in terms of accumulated mean re-
wards. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 119
5.9 Performance image of one experiment using POW-dTS with αinc = 1,
βinc = 1, andγ = 0.4 in terms of MtM. . . . . . . . . . . . . . . . . . . . 120
5.10 Impact of a vanilla CL strategy of the baseline agent . . . . . . . . . . . . 120
5.11 CL-EWC-λ1 (exp) experiment. . . . . . . . . . . . . . . . . . . . . . . . 121
1 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 0.2 . . . . . . . . . . . . . . . . . . . 142
2 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 0.5 . . . . . . . . . . . . . . . . . . . 142
3 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 0.8 . . . . . . . . . . . . . . . . . . . 143
4 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 1.5 . . . . . . . . . . . . . . . . . . . 143
5 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 2 . . . . . . . . . . . . . . . . . . . . 143
6 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 10 . . . . . . . . . . . . . . . . . . . 144
7 DQN MM instant inventories held and thresholds along the testing exper-
iment every time step with AIIF = 100 . . . . . . . . . . . . . . . . . . 144
x

LIST OF TABLES
2.1 Summary of research goals and reference papers. . . . . . . . . . . . . . 34
3.1 Single-agent experiment average results (250 exp) (USDx10 3). . . . . . . 42
3.2 Multi-agent experiment average results (250 exp) (USDx10 3) . . . . . . . 44
3.3 Direct transfer learning experiment average results (250 exp) (USDx10 3) . 49
4.1 DQN cash /inventory average ratio and benchmarks. . . . . . . . . . . . . 67
4.2 DQN Mark-to-Market experiment results (x10 3) and baseline agents. . . . 71
4.3 Benchmark results. MtM, inventory, and cash /inventory ratio are presented. 75
4.4 MORL and RE-W market making test results. . . . . . . . . . . . . . . . 89
4.5 Comparison of multi-objective metrics: hypervolume, sparsity, and un-
dominated solutions. . . . . . . . . . . . . . . . . . . . . . . . . . . . . 95
5.1 Results of non-stationary M 3ORL MM strategies in terms of rewards,
MtM, and absolute inventory value. . . . . . . . . . . . . . . . . . . . . 118
xi

1. INTRODUCTION
This chapter introduces the doctoral thesis by describing the context in which the work
is situated. It presents the motivation behind exploring market making in financial mar-
kets using Reinforcement Learning (RL) and outlines the challenges and opportunities
that arise from this integration (Section 1.1). The chapter further elaborates on the cen-
tral hypothesis that RL-based market making agents can outperform traditional strategies
by autonomously adapting to dynamic market conditions (Section 1.2). Additionally, the
chapter briefly describes the objectives that the research aims to achieve, including the de-
velopment of RL agents capable of efficient market making, the evaluation of their perfor-
mance in various scenarios, and the exploration of advanced inventory management and
multi-objective optimization techniques (Section 1.3). Finally, the chapter concludes with
an overview of the thesis structure, summarizing how each subsequent chapter contributes
to the comprehensive investigation of RL applications in market making (Section 1.4).
1.1. Motivation
Financial markets are complex systems characterized by the dynamic interactions of di-
verse participants, each pursuing distinct objectives. This ecosystem comprises various
actors including retail traders, large institutions, arbitrageurs, market makers, and high-
frequency traders, all engaging in transactions across di fferent types of markets such as
stock markets, bond markets, foreign exchange (Forex), commodities markets, and cryp-
tocurrencies [1]–[3]. These interactions shape the continual flux of asset prices, as rep-
resented in Figure 1.1. Each participant in the financial markets plays a unique role,
contributing to the overall liquidity and depth of the markets. Besides these traditional
participants, the financial markets are also influenced by regulatory bodies and technol-
ogy platforms. Regulatory bodies oversee the functioning of markets, setting rules that
aim to ensure fairness and transparency while minimizing systemic risk. Technology plat-
forms, including electronic trading platforms and blockchain-based systems, facilitate the
rapid execution of trades and are pivotal in the dissemination of market information.
In this financial ecosystem, market makers (MM) play a crucial role. The primary
function of classical market making is to enhance market liquidity by issuing multiple
buy and sell orders at various price levels within the order book (OB). This activity not
only provides traders with a broader range of options for executing their trades but is also
vital for maintaining liquidity, especially in markets where it is typically low [4]2.
MMs are essential in ensuring that financial markets operate e fficiently. By contin-
uously offering to buy and sell securities, they help fill the gap between supply and de-
2All these concepts are broadly detailed at Section 2.2
1

Figure 1.1: Composition of a Financial Market. Example of participants.
mand, which can prevent large price jumps and ensure that trades can be executed quickly.
Their presence reduces transaction costs for other market participants and increases mar-
ket transparency, thereby attracting more traders and investors to the market. To gain a
better understanding of the significance of these agents, as of 2008, there were over 2,000
MMs on the US Stock Exchange [5] and more than 100 in Canada [6], numbers that have
likely increased since then.
In their routine operations, MMs typically generate income by matching trades against
other market participants. This income primarily arises from the bid-ask spread, which is
the difference between the lowest price a seller is willing to accept (ask) and the highest
price a buyer is willing to pay (bid) [7], as depicted in Figure 1.2. For MMs, a wider
bid-ask spread means higher profit margins per transaction. The spread not only reflects
the liquidity of an asset but also serves as an indicator of the general market conditions.
Typically, markets with lower liquidity exhibit wider spreads, suggesting a higher com-
pensation for MMs who provide liquidity under these conditions.
Furthermore, MMs are engaged in sophisticated inventory management control. As
they execute trades, their inventory levels fluctuate; they may increase if buying activity
outweighs selling, and decrease in the opposite scenario. The main challenge with hold-
ing inventory is the risk associated with market price fluctuations, which can significantly
affect the value of held assets. Such price volatility can lead to substantial financial gains
or losses in their Mark-to-Market (MtM) value, depending on the nature of the inventory
and market price movements at the time of liquidation. MtM is a financial accounting
technique used to value assets and liabilities at their current market prices. MtM is widely
used in the trading of securities and derivatives, where market prices can fluctuate signif-
icantly in short periods, making timely valuation crucial. By updating the valuation of
these financial instruments regularly, MtM accounting allows for a transparent view of
2

Figure 1.2: Example of the impact of a MM in a low liquidity asset order book. A MM
usually populates the order book allowing the rest of the market’s participants to have
more prices to trade with.
investment performance and risk exposure.
Managing inventory is a critical aspect that necessitates meticulous risk assessment
and management strategies. The optimization of this balance, aimed at maximizing prof-
itability while minimizing risks, revolves around strategic decisions regarding the setting
of bid and ask prices—the spread. E ffective spread management not only ensures prof-
itability but also reduces market risk exposure by maintaining an appropriate level of
inventory that aligns with current market dynamics and future market expectations.
Additionally, the non-stationary aspect of financial markets demands continuous mon-
itoring and adaptive strategies from those involved. Traders, investors, and MMs must
constantly update their models and approaches to align with the current market state,
ensuring their methods are responsive to the latest market conditions. This dynamic en-
vironment makes financial markets complex and unpredictable, requiring sophisticated
tools and analytical techniques to navigate effectively.
Due to the complexities and challenges outlined, the operation of every MM presents
a particularly challenging problem for several reasons:
1. Competitive environment: MMs operate in a highly competitive environment
where interactions are not limited to independent agents; they also face competi-
tion from other MMs and participants. This competitive landscape requires that
they continuously adapt their strategies to stay ahead or simply keep pace with oth-
ers in the market.
2. Inventory risk management: A significant part of a MM’s role involves managing
inventory risk effectively. They must balance the inventory of financial instruments
3

they hold to avoid substantial losses due to adverse price movements. Proper inven-
tory management is crucial to mitigate risks associated with holding too much of a
depreciating asset.
3. High dimensionality of information: The information that MMs must process is
typical of high dimensionality, involving continuous variables such as price, vol-
ume, and inventory levels. The complexity of this data requires sophisticated mod-
els and algorithms to make informed trading decisions quickly and accurately.
4. Dynamic and evolving environment : The trading environment is not static but
evolves continuously and unpredictably. Changes can occur without prior warning,
altering the dynamics of the market and potentially rendering previous strategies
ineffective. MMs must be agile, with the ability to quickly adapt their strategies in
response to these changes.
Each of these factors contributes to the intricate nature of a MMs’ role within financial
markets. They must navigate through a labyrinth of competitive pressures, risk manage-
ment, complex data, and an ever-changing environment, which demands a high level of
expertise, sophisticated analytical tools, and adaptive strategies. This dynamic setting not
only challenges MMs but also underscores the importance of continuous learning and
evolution in their methodologies.
1.2. Hypothesis
Market making presents a significant control challenge. Managing this complexity is
difficult, which is where RL comes into play. RL offers a robust framework for decision-
making in complex environments. RL, as described by Sutton and Barto [8], represents a
paradigm within machine learning (ML) where agents learn to determine optimal behav-
iors through trial and error, interacting with their environment. These agents are designed
to optimize their decision-making processes, aiming to maximize cumulative rewards over
time. This technique is initially well suited to address the challenges presented in market
making due to several reasons:
• High performance in complex scenarios: RL agents are capable of achieving high
performance in scenarios with single or multiple objectives, making them versatile
in handling the diverse goals inherent in financial markets. This adaptability is
crucial in market making where agents must simultaneously optimize for various
factors such as cost, speed, and risk.
• Handling of continuous and high-dimensional data : They can process contin-
uous and high-dimensional information e ffectively. Many RL algorithms, partic-
ularly those involving deep RL (DRL), employ neural networks (NN), which are
powerful universal function approximators. This capability allows them to digest
4

vast amounts of market data and extract actionable insights, which is essential in
the fast-paced and complex world of financial trading.
• Adaptability to market conditions: RL is adaptable to both stochastic and deter-
ministic environments, employing various algorithms and approaches to suit the
specific context, as detailed throughout this thesis. This flexibility enables RL
agents to perform robustly across a spectrum of market dynamics, adjusting their
strategies in real-time to deal with uncertainties and volatilities.
• Continuous learning and adaptation: Beyond their initial training, RL agents can
continuously learn from their interactions with the market, improving their deci-
sions over time based on new data and experiences. This feature is particularly
beneficial in market making, where market conditions can change rapidly and un-
predictably.
• Optimization of trade execution : RL agents can also optimize the execution of
trades by determining the optimal times and prices for order placement, thereby
minimizing the market impact and the cost of trading. This aspect of RL is critical
for maintaining competitive edges in market making, where profit margins can be
tightly bound to execution efficiency.
More precisely, RL agents develop optimal policies based solely on the feedback (re-
wards or penalties) received from their interactions with the environment. This reward-
based learning guides their actions towards the most beneficial outcomes without prede-
fined strategies for goal attainment, relying instead on discerning beneficial from detri-
mental actions. Thus, RL is particularly e ffective at uncovering novel and surprisingly
efficient strategies. A prominent example of RL’s innovative capability is the “move 37”
performed by AlphaGo agent against Go master Lee Sedol [9]. This move, unforeseen by
most human experts, was instrumental in securing a victory and is acclaimed as a display
of “creativity”.
This thesis is founded on the premise that the dynamic and complex nature of stock
markets, characterized by the interplay of a diverse range of participants, presents a unique
set of challenges and opportunities for MMs. It hypothesizes that RL, with its inherent
capability to learn optimal behaviors through trial and error by interacting with a complex
environment, is particularly suited to address these challenges. This suitability comes
from RL’s ability to adapt and optimize decision-making processes in environments that
are as unpredictable and multifaceted as financial markets.
The first layer of the hypothesis proposes that an RL-based approach can significantly
enhance the MM’s ability to inject liquidity into the market while ensuring profitability.
This assertion takes into account the critical role of MMs in providing depth and stability
to the market through the issuance of multiple buy and sell orders. It further acknowledges
the nuanced balance MMs must strike between facilitating liquidity and managing the
5

inherent risks of holding inventory, especially in markets characterized by low liquidity
and high volatility.
Expanding upon this foundation, the hypothesis delves into the more complex sce-
nario of inventory risk management. It suggests that RL can e ffectively manage the dual
objectives of liquidity provision and inventory risk control, transforming the MM problem
into a multi-objective optimization challenge.
Furthermore, the hypothesis anticipates that an RL-based MM agent can achieve au-
tonomous adaptation to the evolving dynamics of financial markets. This aspect considers
the non-stationary nature of financial markets, influenced by numerous factors including
economic events, market participant behavior, and trading volume fluctuations. It sug-
gests that through continuous learning and adaptation, an RL agent can dynamically ad-
just its strategy in response to these changes, maintaining e ffectiveness and resilience in
its market making activities. Such autonomous adaptation is expected to not only sustain
the profitability and liquidity provision e fficacy of MMs but also to potentially discover
innovative strategies that enhance market efficiency and stability.
1.3. Objectives
This dissertation aims to comprehensively explore and evaluate the application of RL
in market making strategies within competitive financial markets. The research focuses
on the profitability, adaptability, and strategic inventory management of RL-based MMs
under dynamic market conditions.
This research is driven by several key questions:
• How can RL improve the decision-making processes in market making in addition
to traditional quantitative methods?
• What are the optimal strategies for managing inventory and risks in market making
using RL techniques?
• Can these strategies effectively handle the multi-objective nature of market making,
balancing profit maximization with other critical operational goals?
• How do market making strategies adapt to and perform in non-stationary market
environments?
Exploring these questions further, the specific objectives to be pursued include:
1. Evaluate RL for profitable market making in competitive scenarios:
• Develop and test RL models that can operate effectively in competitive trading
environments, emphasizing the creation of profitable market making strate-
gies.
6

• Analyze the performance of RL-driven MMs against traditional and other al-
gorithmic MMs to assess relative profitability and efficiency.
• Conduct simulations in a simulated market to understand how RL MMs inter-
act with di fferent types of trading agents and the resultant e ffects on market
dynamics and liquidity.
2. Advanced management of inventory using RL:
• Investigate various RL approaches for inventory management, focusing on
multi-objective strategies that minimize the risk associated with holding in-
ventory while maximizing profitability.
• Explore the impact of inventory levels on the decision-making processes of
RL agents, incorporating models that dynamically adjust strategies based on
current inventory states.
• Evaluate the effectiveness of these inventory management strategies through
rigorous testing in simulated environments, measuring performance through
metrics such as cost minimization and avoidance of inventory imbalances.
3. Adaptability in market making strategies to address non-stationarity:
• Develop adaptive RL models capable of responding to non-stationary market
conditions, ensuring sustained performance and relevance despite changes in
market dynamics.
• Implement and assess mechanisms to enable RL models to shift strategies
based on evolving market conditions effectively.
• Analyze how these adaptive strategies perform in long-term simulations, fo-
cusing on their ability to maintain competitiveness and profitability over time.
• Analyze and compare different existing learning strategies performed to adapt
to this non-stationarity.
In summary, this thesis encapsulates a comprehensive exploration of the application
of RL to the domain of market making. It examines the potential of RL to surpass the
traditional approaches to market making by equipping MMs with strategies that are adap-
tive, robust, and optimized for the complexities of modern financial markets. Through
this exploration, the thesis aims to contribute to the advancement of both the theoreti-
cal understanding and practical implementation of RL in financial market applications,
ultimately promoting more resilient and efficient markets.
1.4. Thesis overview
This dissertation is organized into six chapters, each serving a distinct purpose within the
overall research narrative. The journey begins with this introductory segment, which sets
7

the stage for the comprehensive exploration to follow. The following Chapter 2 takes a
deep dive into the current state of the art and the main background in several intercon-
nected fields: market making, RL, multi-objective reinforcement learning (MORL), and
the nuanced application of RL within the context of market making. Additionally, it in-
troduces the main concepts of financial markets and describes the simulated environment
used throughout this work. This entire analysis is pivotal in understanding the research.
The heart of the dissertation resides in Chapter 3, 4, and 5, where the bulk of the
research unfolds. In Chapter 3, the narrative begins with the development of a RL market
making agent capable of operating within a simulated stock market environment. This
agent is designed to enhance profitability while providing liquidity, even in the presence
of competitors. Through rigorous policy analysis and competitive testing against other
RL-based MM agents, the chapter describes the agent’s strategic efficacy.
Chapter 4 shifts the focus to the critical aspect of inventory management, approached
from two distinct angles. The initial perspective, presented in Section 4.1, treats inven-
tory management as a problem of reward engineering. Here, a novel reward function is
proposed, leveraging dynamic factors that adjust rewards based on the cash-to-inventory
ratio in real-time. This model is shown to outperform existing strategies, marking a signif-
icant advancement in the field. However, a more robust way to solve this multi-objective
problem was sought. Reward engineering, although the main approach used in RL to
deal with these kinds of challenges, su ffers from many problems. This is why, in Sec-
tion 4.2, a more sophisticated multi-objective approach is explored, allowing the agent
to focus on both objectives independently through the use of dual NNs and Pareto front
(PF) optimization. This approach is demonstrated to not only enhance stability but also
significantly improve performance compared to the reward-engineered model.
With these achievements, this research has not yet addressed the problem of the non-
stationarity of financial markets. To this point, a policy able to perform well under some
predefined circumstances has been learned. However, the performance is not guaranteed if
the market evolves due to any of the aforementioned factors. For this reason, in Chapter 5,
a non-stationary algorithm based on Thompson sampling (TS), Policy Weighting through
Discounted Thompson sampling (POW-dTS), tailored for RL market making agents is in-
troduced. This algorithm cleverly balances a suite of pre-trained policies, derived from
the multi-objective RL agent, adjusting dynamically to the ever-changing market condi-
tions. With a set of pre-trained policies, the algorithm can adapt autonomously to the best
combination of known policies in terms of rewards.
In the concluding Chapter 6, summarizes the key findings of this study, discussing
their impact on market making and RL. It highlights the contributions to academic knowl-
edge and suggests directions for future research. This final chapter aims to encapsulate
the essence of the dissertation, o ffering both a summation of the research conducted and
a visionary outlook toward the future of market making strategies empowered by RL.
The evolution of this research is visually represented in Figure 1.3, which not only
8

chronicles the progression of the study through its main milestones but also lists the ar-
ticles published or undergoing review at each pivotal moment. This graphical timeline
reveals the dissertation’s logical and methodical advancement.
Figure 1.3: A detailed depiction of the research’s evolution, including the rationale and
associated scholarly articles at each developmental phase.
9

2. BACKGROUND
The landscape of financial markets is continuously reshaped by advancements in tech-
nology and quantitative analysis, influencing strategies in trading and particularly in mar-
ket making. This chapter provides a detailed review of the state of the art in market mak-
ing, emphasizing the evolution from traditional models to sophisticated computational
approaches that leverage RL and its derivatives. The purpose is to frame the current re-
search within the broader context of recent technological advancements and to highlight
the progress that has been made as well as the gaps that this thesis aims to address.
This chapter begins in Section 2.1 by focusing on RL and deep reinforcement learn-
ing (DRL). The foundational concepts, including Markov Decision Processes (MDP),
value functions in RL, and various RL algorithms, are introduced. The discussion then
delves into MORL, exploring both reward engineering approaches and broader MORL
frameworks. Additionally, the complexities of non-stationary RL are addressed, high-
lighting strategies for adapting to changing environments. Next, the discussion shifts to
Section 2.2. This section provides an introduction to financial markets, explaining what
they are and how they work. Some relevant concepts such as the OB are presented. To un-
derstand market making, it is crucial to first understand the nature of these environments.
Following this, the analysis of the market making problem is provided in Section 2.3.
Both classical and modern (supervised learning and RL) market making approaches are
detailed. It is important to recognize how di fferent techniques have been employed to
address this challenge. The pros and cons of each approach are also discussed. Atten-
tion is then given to simulated environments in RL, specifically focusing on the ABIDES
framework. In Section 2.4, the role of simulation in developing and testing market mak-
ing strategies is explored, illustrating how simulated environments provide a robust and
controlled setting for experimenting with and refining RL algorithms. Finally, Section 2.5
details the advantages and disadvantages of current market making algorithms and tech-
niques. The reference papers in the literature are described, along with the goals aimed to
be achieved at every stage.
By reviewing these diverse aspects, this chapter sets a solid foundation for under-
standing the innovative approaches explored in this thesis, highlighting the shift towards
more dynamic, responsive, and e fficient market making mechanisms. This comprehen-
sive overview serves to position the current research within the continuum of financial
technology development, emphasizing both the achievements and the ongoing challenges
in the field.
10

2.1. RL and DRL
In this section, the main concepts of RL and DRL are described in detail. Various ap-
proaches currently applied to address the challenges associated with multi-objective op-
timization and non-stationarity in dynamic environments are also explored. Specifically,
the foundational principles of RL and DRL, their key components, and the algorithms that
underpin these techniques are discussed. Additionally, how these methods are tailored
and enhanced to handle the complexities of managing multiple objectives simultaneously
and adapting to changes in the environment over time is examined. This comprehensive
overview provides the necessary theoretical background for understanding the advanced
methodologies employed in this dissertation.
2.1.1. Markov decission process
As introduced, RL [8] is the pivot technique used around the market making problem.
The foundational framework for RL tasks is the MDP. The MDP is formally defined by
a tupleM =⟨S, A, T, R⟩, where S represents the set of all possible states in the envi-
ronment, A denotes the set of actions available to the agent, T, the transition function,
defines the probability of transitioning from one state to another given a specific action,
and R is the reward function, providing immediate feedback based on the current state and
action taken, as depicted in Figure 2.1. This framework allows for the modeling of both
deterministic environments, where actions lead to predictable outcomes, and stochastic
environments, where outcomes may vary even with the same action in the same state.
Figure 2.1: RL Agent and environment interactions. (Sutton & Barto - Reinforcement
learning an Introduction).
The final objective in RL is to discover a policy π, a strategy that dictates the action
the agent should choose when in a given state, that maximizes the expected return J(π)
from any initial state, as in Equation 2.1.
J(π) = Eπ
⎡⎢⎢⎢⎢⎢⎣ ∞∑︂
t=0
γtRt
⎤⎥⎥⎥⎥⎥⎦ (2.1)
11

Where Eπ[·] represents the expectation over the distribution of states and actions by
following policyπ, Rt is the reward received at time step t, and γ∈ [0, 1) is the discount
factor, indicating the present value of future rewards.
The objective is to find the optimal policyπ∗ that maximizes J(π) as in Equation 2.2:
π∗ = arg max
π
J(π) (2.2)
2.1.2. Value functions in RL
In RL, value functions are essential for evaluating the potential outcomes of states and
actions. These functions help agents decide by estimating the expected rewards. The
two primary types of value functions are the state value function (V) and the action-value
function (Q). The state-value function, denoted as V(s), estimates the expected return
(present and future rewards) starting from a state s while following a given policyπ. It is
formally defined as in Equation 2.3:
Vπ(s) = Eπ
⎡⎢⎢⎢⎢⎢⎣ ∞∑︂
t=0
γtrt+1| st = s
⎤⎥⎥⎥⎥⎥⎦ (2.3)
In this equation, Eπ represents the expected value following policyπ,γ is the discount
factor, which discounts future rewards,rt+1 is the reward received at time stept + 1; and st
is the state at time stept. The state-value function indicates how favorable it is for an agent
to be in a specific state, assuming it follows the policy π. The main di fference between
Equation 2.1 and this function is that the former represents the expectation over the distri-
bution of states and actions encountered while following policy π, whereas Equation 2.3
focuses on the expected return when following policyπ starting from a specific state s. In
summary, J(π) provides a global view of the policy performance, whereas Vπ(s) offers a
local view from each state.
The action-value function, or Q-function, denoted as Q(s, a), estimates the expected
return for taking an action a in state s and then continuing to follow policyπ. It is defined
as in Equation 2.4:
Qπ(s, a) = Eπ
⎡⎢⎢⎢⎢⎢⎣ ∞∑︂
t=0
γtrt+1| st = s, at = a
⎤⎥⎥⎥⎥⎥⎦ (2.4)
Here, Eπ represents the expected value following policyπ,γ is the discount factor,rt+1
is the reward received at time step t + 1, and st and at are the state and action at time step
t. The Q-function indicates how favorable it is to take a specific action in a given state,
assuming the agent continues following policyπ.
The state-value function V(s) and the action-value function Q(s, a) are very related.
Indeed, the value of a stateV(s) can be derived fromQ(s, a) by averaging over all possible
12

actions, weighted by the policyπ, as shown in Equation 2.5 and Equation 2.6, depending
on whether stochastic or deterministic policies are applied:
Vπ(s) = ∑︂
a∈A
π(a| s) Qπ(s, a), ∀s∈S (when stochastic policy) (2.5)
Vπ(s) = Qπ(s,π (s)), ∀s∈S (when deterministic policy) (2.6)
This means the value of a state is the expected value of the Q-function for all actions,
considering the probability of each action under the policyπ.
In RL, the main goal is to find the optimal policy π∗ that maximizes the expected re-
turn. The optimal state-value functionV∗(s) and the optimal action-value functionQ∗(s, a)
are defined as in Equation 2.7 and Equation 2.8:
V∗(s) = max
π
Vπ(s), ∀s∈S (2.7)
Q∗(s, a) = max
π
Qπ(s, a), ∀s∈S and ∀a∈ A (2.8)
For the optimal policy, the relationship between V∗ and Q∗ is as in Equation 2.9:
V∗(s) = max
a∈A
Q∗(s, a) (2.9)
This indicates that the optimal value of a state is the highest expected return achievable
by any action in that state, followed by the optimal policy. This value function tends to
work very well when dealing with discrete and not very large state and action spaces. In
such scenarios, algorithms can be computed iteratively in tabular modes, such as Q-tables,
where each state-action pair is explicitly stored and updated. The most representative
value-function tabular algorithm is called Q-learning[10]. Q-learning uses a Q-table to
store and update the Q-values for each state-action pair. This algorithm updates the q-
values of each state-action pair according to the Equation 2.10, where max a′ Q(s′, a′)
represents the maximum estimated Q-value for the next state s’ over all possible actions
a’:
Q(s, a)← Q(s, a) +α
[︃
r +γ max
a′
Q(s′, a′)− Q(s, a) ]︃ (2.10)
However, when the state or action space becomes very large or even continuous, the
“curse of dimensionality” is encountered. This term refers to the exponential growth in
computational complexity and resource requirements as the dimensionality of the space
increases. In these situations, using a tabular approach becomes impractical due to the
immense number of entries required and the infeasibility of updating each one through
direct experience.
13

To address the curse of dimensionality, it is mandatory to employ some form of func-
tion approximator that can generalize across the vast or infinite number of states and
actions. This is where neural networks (NNs) come into play, transforming traditional
RL into deep reinforcement learning (DRL). NNs, with their ability to learn complex pat-
terns and representations, can approximate value functions e ffectively by mapping high-
dimensional input spaces (states) to output spaces (value estimates or actions). Hence,
NNs enable RL to scale to problems with continuous or very large discrete spaces by
learning a compact, parametric representation of the value function. Instead of storing a
value for every possible state-action pair, the network learns to predict these values based
on the features of the state and action. This not only makes the approach more memory
efficient but also allows the agent to generalize learned knowledge to unseen states, im-
proving its ability to make informed decisions in new or previously unexplored parts of
the state space.
However, the use of NNs in RL introduces new complexities and challenges. Training
deep NNs is computationally intensive and requires careful tuning of hyperparameters.
Additionally, NNs can be unstable and prone to divergence during training, especially in
the context of bootstrapped updates like those used in Q-learning. Techniques such as
experience replay [11], where past experiences are stored and sampled randomly to break
the correlation between consecutive updates, and target networks, which stabilize learning
by slowly updating the network parameters, are essential to mitigate these issues.
Finally, there are some other issues regarding the use of NNs in this type of problem.
The first is the loss of explainability [12], as the many parameters a NN can have may
obscure the relationship between inputs and outputs. Additionally, NNs must interpo-
late or extrapolate between continuous inputs, making it di fficult to ensure whether the
state-action space has been adequately explored, how frequently it has been visited, and
whether the interpolations are performing as expected across the entire dimensional space.
Nevertheless, DRL has proven to be an effective solution for high-dimensional problems.
The following subsection takes a deeper look into various RL and DRL algorithms.
2.1.3. RL and DRL Algorithms
There exists a rich spectrum of RL algorithms. These methodologies fall into two pri-
mary classifications: value-based or policy-based; and model-based or model-free algo-
rithms. Each one is tailored for specific scenarios and challenges inherent to RL tasks.
Value-based algorithms, as introduced in the previous section, prioritize the evaluation
of action-values within states. Central to these methods is the concept of a value function,
which predicts the cumulative rewards expected from each state or state-action combina-
tion, thereby guiding the agent towards actions that maximize future returns. Q-learning,
for example, leverages a tabular approach while, in Deep Q-Networks’ case (DQN), a NN
to approximate these values across potentially vast or continuous state spaces. These al-
gorithms are particularly effective in settings with discrete, clearly defined action spaces,
14

offering versatile solutions across a multitude of applications. The return is calculated as
the discounted sum of rewards, as in Equation 2.3 and Equation 2.4, where rk represents
the reward received at step k, γ is the discount factor determining the present value of
future rewards (where 0 ≤ γ≤ 1), and E denotes the expectation over the distribution
of paths generated by policy π. The discount factor γ plays a crucial role in balancing
the importance of immediate vs. future rewards, enabling the agent to make strategic
decisions that consider both short-term gains and long-term objectives.
Conversely, policy-based algorithms such as REINFORCE[13], Soft Actor Critic
(SAC)[14], and Proximal Policy Optimization (PPO)[15] focus on directly learning the
policy that determines the agent’s actions in various states. This class of algorithms es-
chews indirect value estimation in favor of optimizing the policy itself, often through
techniques like gradient ascent, to maximize expected returns. Their direct approach to
learning and optimizing policies renders them well-suited to environments with continu-
ous states and action spaces.
An additional classification for RL algorithms depends on whether they have a model
of the environment or not. Model-based RL strategies endeavor to understand and repli-
cate the environment’s dynamics to inform their decision-making process. Techniques in
this regard, like Dyna-Q[8] and Monte Carlo Tree Search (MCTS)[16], merge the insights
of value-based and policy-based methods, utilizing models of the environment—whether
learned or predefined—to simulate potential future states and rewards. This predictive
capability allows for enhanced strategic planning and decision-making, reducing the ne-
cessity for exhaustive interaction with the actual environment. Conversely, model-free
algorithms learn without knowledge of the transition probabilities and reward functions
that describe the dynamics of the environment.
This research primarily focuses on DQN with various adaptations. The main reason
for choosing DQN is its suitability for handling continuous state spaces while allowing
for the discretization of action spaces. DQN excels in scenarios where defining a pre-
cise model of the environment is challenging or impractical. Additionally, as a model-
free approach, DQN does not require a predefined model of the underlying environment,
making it particularly relevant for applications in financial markets. As a value function
method, it computes the optimal policy according to the Equation 2.4 detailed at Sub-
section 2.1.2. Financial markets are inherently stochastic and complex, characterized by
unpredictable fluctuations and a multitude of interacting variables. Traditional model-
based methods struggle to capture this complexity accurately. In contrast, DQN can learn
effective policies directly from interaction with the environment, making it a robust choice
for developing adaptive and resilient market making strategies in such a volatile context.
Additionally, experience replay has also been applied in every experiment. Instead of
processing all the transitions sequentially, experience replay gets random samples from
all the stored transitions. This helps achieve more stable and reliable learning, preventing
the algorithm from overfitting to recent experiences, among other benefits. Algorithm 1
details the standard DQN with experience replay algorithm, as described in [17]. All the
15

details can be found in the mentioned work.
Algorithm 1 Deep Q-learning with Experience Replay Algorithm (From [17])
1: Initialize replay memoryD to capacity N
2: Initialize action-value function Q with random weights
3: for episode = 1, M do
4: Initialize sequence s1 ={x1} and preprocessed sequenceϕ1 =ϕ(s1)
5: for t = 1, T do
6: With probabilityϵ select a random action at
7: otherwise select at = maxa Q∗(ϕ(st), a;θ)
8: Execute action at in emulator and observe reward rt and image xt+1
9: Set st+1 = st, at, xt+1 and preprocessϕt+1 =ϕ(st+1)
10: Store transition (ϕt, at, rt,ϕ t+1) inD
11: Sample random minibatch of transitions (ϕ j, a j, r j,ϕ j+1) fromD
12: Set y j =
⎧⎪⎪⎪⎨⎪⎪⎪⎩ r j for terminalϕ j+1 r j +γ maxa′ Q(ϕ j+1, a′;θ) for non-terminal ϕ j+1
13: Perform a gradient descent step on (y j− Q(ϕ j, a j;θ))2 according to equation 3
14: end for
15: end for
2.1.4. Multi-objective RL
To this point, the focus has primarily been on solving single-objective tasks. However,
many real-world problems involve addressing multiple objectives simultaneously, which
are commonly referred to as multi-objective problems, as discussed in the literature [18]–
[20]. Over time, various techniques have been developed to address this optimization
problem.
More precisely, in the domain of RL, addressing multi-objective challenges necessi-
tates strategies that differ notably from those used for single-objective optimization [21]–
[23]. With multiple, potentially competing objectives to consider, the agent must learn
to find a balance, often optimizing one aspect while compromising on another to some
degree. The common method to navigate this complexity is through the integration of all
objectives into a single reward function, which is accomplished by assigning weights or
parameters that reflect the importance of each subgoal. The result is a composite objective
that guides the agent’s behavior.
Yet, the field of multi-objective RL o ffers an array of alternative strategies that may
prove more adequate for certain applications. Multi-objective RL frameworks (MORL)
are designed to pursue multiple objectives in parallel, capturing the essence of the trade-
offs between them. Instead of forcing a compromise through a single reward signal, these
frameworks maintain a spectrum of policies, each attuned to different objective balances,
16

thus offering a suite of solutions among which decision-makers can choose based on their
preferences or changing situational demands.
To gain a better understanding of both techniques, the following subsection provides
detailed explanations of the two multi-objective approaches: reward engineering and
MORL.
Multi-objective RL via reward engineering
Reward function engineering stands as a cornerstone in the domain of multi-objective
RL, offering a methodical way to direct an agent towards achieving multiple objectives
[24], [25]. The process involves creating a reward function that includes all the goals the
agent needs to achieve. However, engineering such functions is complex. It often leads to
elaborate formulas that complicate the learning process [26]. The task becomes even more
challenging when the agent must balance many objectives within a single scalar reward
signal. This consolidation necessitates careful calibration, as the weights or parameters
involved present a challenge in their specification without prior empirical knowledge [27].
The art of reward engineering extends to more sophisticated techniques than mere
weight adjustments. These advanced methods craft complex reward functions that may
implement penalty terms. Such terms are designed to modulate one objective in the con-
text of another’s performance, thus creating a deliberate interdependence between goals
[28], [29]. The inclusion of penalty terms represents an e ffort to balance competing ob-
jectives, where success in one aspect may necessitate a controlled concession in another.
This nuanced approach allows for a more refined guidance of the agent’s behavior, allow-
ing a better alignment of the agent’s actions with the multifaceted nature of real-world
tasks.
By shaping the decision-making processes of RL agents, these engineered rewards
guide them toward achieving a balance of objectives that mirrors the complexities and
trade-offs inherent in their tasks. These approaches, therefore, have multiple weaknesses,
including the need to define one reward function per a priori goal, di fficulty in handling
nonlinear relationships between sub-goals, and a lack of explainability regarding the re-
ward, among others.
Multi-objective RL via MORL
Considering the mentioned weaknesses of reward-engineered approaches, another alter-
native for addressing multi-objective problems with RL involves using MORL frame-
works.
MORL differs from single-objective RL in that it requires optimization across mul-
tiple dimensions, effectively transforming the classic MDP into a Multi-Objective MDP
(MOMDP). This transformation leads to the simultaneous optimization of multiple goals,
17

where rewards and Q-values are treated as vectors to accommodate the complexity and
multi-dimensionality of the problem. Consequently, the Q-value function is defined to
reflect this vector nature, as in Equation 2.11:
Q⃗ (s, a) = (Q1(s, a), Q2(s, a),..., Qn(s, a)) (2.11)
Where every Qx corresponds to one sub-goal. In the same way, the reward is repre-
sented by a vector instead of a scalar, as in Equation 2.12
R⃗(s, a) = (R1(s, a), R2(s, a),..., Rn(s, a)) (2.12)
Q-functions can be managed using Q-tables when dealing with discrete state spaces
or with NNs when handling continuous space states, as in their case. Some MORL al-
gorithms use weights to balance all the goals and, in this sense, obtain the policies that
define the PF. However, these weights differ from their reward-engineered alternative, as
they do not collapse the multiple objectives into a single scalar reward . Instead, they
influence the exploration and exploitation of the solution space to find a balance between
the objectives. The main reason for not scalarizing the rewards in MORL is to preserve
the diversity of the solution set . By maintaining multiple objectives and representing
trade-offs, MORL allows for a richer and more flexible set of solutions. Scalarization can
sometimes oversimplify the problem by aggregating the objectives into a single value,
potentially losing important information about the relationships between the objectives.
Additionally, MO and MORL solutions are typically supported by Pareto fronts (PFs)
[23], [30]. PFs have been extensively utilized in solving various multi-objective problems
across different domains, such as engineering, finance, and healthcare [31]. Within the
market making domain, for instance, PFs have proven e ffective in optimizing trading
strategies to balance conflicting objectives, such as maximizing profits while minimizing
risk [32].
PFs depict the non-dominated policies, which represent the optimal solutions where
enhancing one objective would necessitate deteriorating at least one other objective (Fig-
ure 2.2). By o ffering decision-makers a spectrum of optimal solutions, PFs enable them
to navigate the trade-offs between competing objectives effectively. Decision-makers can
analyze a PF to identify the optimal trade-o ff based on their preferences and priorities.
This analytical process facilitates informed decision-making and objective exploration,
allowing stakeholders to make decisions aligned with their strategic goals and objectives.
Moreover, PFs are not limited to RL applications but are broadly applied in di fferent
fields, including engineering design, resource allocation, and portfolio optimization [33]–
[35]. Across these diverse domains, PFs serve as a valuable tool for decision-makers to
evaluate alternative solutions and make decisions that strike a balance between conflicting
objectives.
In summary, MORL frameworks supported by PFs o ffer a powerful approach to ad-
18

Figure 2.2: Overview of multi-objective artifacts and concepts.
dressing multi-objective RL problems. By providing decision-makers with a compre-
hensive view of optimal solutions, PFs enable them to navigate complex decision spaces
and identify trade-offs that align with their strategic objectives. This approach enhances
decision-making processes across various domains, leading to more e ffective and in-
formed outcomes.
2.1.5. Non-stationary RL
In the previous sections, it was assumed that the underlying MDP remains constant through-
out the tasks. However, another issue that may arise is that the MDP changes over time.
In this case, it is said that the environment is non-stationary. Non-stationary environments
present a significant challenge for RL algorithms, as the policies learned may become sub-
optimal as the environment evolves. This requires the development of adaptive methods
capable of responding to changes and maintaining optimal performance.
In the domain of RL, the quest to tackle non-stationary challenges present in many re-
search areas remains a significant focus [36]. The strategies used are customized to each
problem’s unique features, including factors like how long decisions need to be planned
for (finite or infinite), the availability of a context library, and the degree of understand-
ing regarding the MDPs and their contexts. Particularly in non-episodic tasks, such as
our approach in market making, two predominant strategies for navigating the dynamic
environment are performed. Firstly, there is the strategy of adapting the learned policy to
reflect the ongoing changes in the environment (single-policy). This adaptation involves
continuously updating the policy based on the latest observations and feedback from the
environment. By doing so, the agent can better respond to shifts in market conditions, en-
suring its actions remain effective and relevant over time. Secondly, there is the approach
of maintaining a collection of policies and selecting the optimal one at each decision point
(multi-policy). This strategy involves training multiple policies or models to cover a range
19

of possible scenarios or market conditions. Then, at runtime, the agent selects the most
suitable policy from this collection based on the current state of the environment. By
maintaining a diverse set of policies and dynamically choosing the best one, the agent can
effectively handle the variability and unpredictability inherent in non-episodic tasks like
market making.
In addition to the two primary strategies utilized to address non-stationarity in RL,
there exists a plethora of other techniques within classical ML aimed at managing this
challenge. Continual learning (CL), for instance, represents a subset of methods designed
to enable models or agents to seamlessly incorporate new incoming data while maintain-
ing or even improving their performance over time. Unlike traditional batch learning
paradigms, CL methods focus on the incremental acquisition of knowledge, allowing
models to adapt and evolve as they encounter new information. This iterative learning
process enables agents to stay relevant and e ffective in dynamic environments where the
underlying data distribution may change over time.
Regarding this, the following details various algorithms and techniques from the liter-
ature used to address the problem of non-stationarity:
Single-policy algorithms: Within this domain, strategies often revolve around a single
policy that evolves in response to environmental changes. Infinite-horizon scenarios have
seen limited focus, with RUQL (Referenced Update Q-learning) by [37] standing out.
RUQL adjusts Q-values in reaction to new experiences or changes in transition proba-
bilities, applying uniform updates based on new data. This method is based on having
a full understanding of MDP dynamics and is designed for discrete state spaces. The
Q-learning framework has seen various modifications to better suit non-stationary envi-
ronments through learning rate adjustments [38], [39]. For example, [38] enhanced Q-
learning by dynamically altering the learning rate through gradient descent, showing su-
periority over traditional methods in shifting environments. Similarly, Optimal Step Size
Algorithm [39] (OSA) fine-tunes the Q-learning rate to counteract noise in non-static
environments, focusing on minimizing estimation errors rather than directly improving
learning outcomes. OSA presupposes prior knowledge of transition and reward struc-
tures. Regarding financial market non-stationarity, studies like [40] leverage prior deep
learning models to glean insights from technical indicators for RL policy training, though
they lack adaptability to newly emerging changes.
Multi-policy algorithms: Contrarily, some solutions involve maintaining and selectively
applying multiple policies or contexts, especially in non-episodic settings. The RL-CD
model (RL with context detection) [41] exemplifies this, utilizing a series of models cho-
sen based on performance signals and generating new ones as needed. It requires meticu-
lous parameter adjustments specific to each challenge and is limited to discrete decision-
making environments. While other studies like [42] aim to simplify these aspects, they
remain largely conceptual. Alternatives such as HM-MDP [43] and ContextQL [44] ex-
plore the use of model-based and policy-variance strategies. ContextQL is also based on
20

change point detection strategies, specifically the Online Parametric Dirichlet Change-
point detector [45] (ODCP), a multivariate detector that identifies whether the dynamics
of the environment have changed.
Continual Learning (CL): Given the unique challenges of the multi-objective continu-
ous MDP, exploration into CL [46], [47], a subset of ML focused on adapting to new data
without succumbing to Catastrophic Forgetting (CF) [48], is undertaken. CF, the perfor-
mance degradation following new data integration, is mitigated through strategies such as
freezing layers (FL) [49], data rehearsal (DR) [50]–[52], and elastic weight consolidation
(EWC) [53], targeting parameter isolation, data replay, and regularization, respectively.
While FL, a tactic of adjusting weights in certain layers while preserving others, shows
efficacy in supervised learning (SL) and transfer scenarios, its RL application, especially
in non-stationary contexts, is less examined. EWC, distinguishing crucial NN weights
via a Fisher information matrix, discourages adjustments to key weights, thereby safe-
guarding vital learned information. DR, alternatively, incorporates a mix of old and new
data during training, maintaining a broad experiential spectrum for the agent, a practice
particularly valued in RL for enhancing performance and stability.
2.2. Financial markets
To this point, the context of RL in which this thesis is framed has been introduced in
detail. The following section will describe the financial context, thus completing the
general background of the thesis. Key concepts of financial markets are discussed to
provide a better understanding of their movements, dynamics, and characteristics, and
where the MM agent will have to perform.
As introduced in Section 1.1, financial markets are characterized by the interaction
of various participants, each with di fferent goals, strategies, operations, and impacts on
the market itself. For instance, retail traders, often individuals, engage in trading on
a smaller scale, primarily influenced by personal goals and risk tolerance. They add
significant volume to trades, especially in highly liquid markets like Forex and stocks.
However, the influence of individual retail traders is typically smaller compared to insti-
tutional traders. Large institutions, such as mutual funds, pension funds, and insurance
companies, trade in large volumes and can significantly impact market prices with their
large-scale transactions. Their strategies are typically more sophisticated, involving long-
term positions and hedging techniques. Arbitrageurs seek to exploit price discrepancies
between markets or securities, adding to market efficiency by ensuring that prices do not
deviate substantially from their fair values for long. Their strategies are crucial in main-
taining the interconnectedness of global markets, ensuring that anomalies between similar
financial instruments are minimized. High-frequency traders (HFTs) use advanced al-
gorithms to move in and out of positions in seconds or milliseconds. HFTs thrive in
markets where speed is a critical factor and can capitalize on very small price differences.
Their activities contribute to market liquidity and can also lead to increased volatility
21

when large volumes of trades are executed quickly. The interaction between these diverse
market participants and technologies not only drives the day-to-day movements in asset
prices but also shapes the strategic evolution of financial markets. Innovations such as
automated trading and artificial intelligence are reshaping strategies, while global eco-
nomic events and policy changes continue to test the resilience and adaptability of market
structures.
The mentioned participants take part in a perpetual auction, submitting buy and sell
orders through a centralized public limit order book (OB), which is crucial in determining
asset price movements [54]. The OB serves as an electronic catalog that lists all pend-
ing (unmatched) orders. It is continuously updated, with new limit orders being added
and executed orders being removed in a first-in-first-out (FIFO) sequence. This dynamic
process offers a real-time representation of the market’s supply and demand dynamics in
terms of price and volume, showcasing the vibrant and fluid nature of financial markets.
Each level within the OB displays the total volume of orders at specific price points,
providing valuable insights into the market depth and the potential for upcoming price
movements. Such information is vital for market participants in strategizing their entries
and exits. Additionally, the transparency of the OB allows for an understanding of market
sentiment and potential price support or resistance levels. A graphical depiction of the
OB’s key elements, illustrating its structure and function, can be found in Figure 2.3. This
visualization aids in comprehending how orders are organized and executed, influencing
overall market liquidity and price stability.
Figure 2.3: Running OB example. Source: https://www.simtrade.fr/blog_
simtrade/understanding-order-book-how-impacts-trading/ . (last accessed:
October 24, 2024)
22

Liquidity is critical because it reflects the ease with which assets can be bought or sold
at stable prices. The level of liquidity in a market is heavily influenced by the number
of active participants and the volume of transactions taking place. In conditions where
liquidity is lacking, even large orders can lead to severe price fluctuations. Such orders
quickly fill up the OB, causing significant changes in the asset’s price. These volatile
conditions can lead to substantial financial losses for investors in a short period, which
can diminish confidence in the asset or even the entire market.
MMs counteract these risks by ensuring a steady stream of orders, which helps to
stabilize the market. They act as a buffer against sharp price movements by balancing the
buying and selling pressures through their continuous order flows. The vital role of MMs
in enhancing the stability and liquidity of financial markets is illustrated in Figure 1.2,
which shows the impact of MMs on the OB and, consequently, on market liquidity.
One significant characteristic of every financial market is the non-stationarity [55]–
[58]. Financial markets are not static; they evolve continuously, influenced by a variety of
factors. Elements such as trading session schedules [59], news [60] , and economic expec-
tations [61] serve as triggers for these changes, generating non-stationarity in the market
itself. These factors collectively impact the inherent dynamism of price movements, com-
plicating the task of defining stable and robust strategies. Furthermore, the introduction
of new financial products and the entrance of new technology in trading systems, such
as algorithmic and high-frequency trading, also contribute to the non-stationary nature of
markets. These technological advancements can drastically change trading patterns and
volumes within very short periods, often leading to unexpected volatility or new market
trends.
2.3. Dealing with the market making problem
Once introduced to how the financial markets work and provided the main background
on RL and ML, it is time to dive into the market making problem. The literature presents
many types of strategies within the realm of market making. Before advanced ML tech-
niques revolutionized trading systems, more traditional mathematical and algorithmic ap-
proaches were predominant. These classical methods relied on statistical models, stochas-
tic processes, and other quantitative techniques to make trading decisions. However, with
the advent of sophisticated ML and RL techniques, the landscape of market making has
significantly evolved.
In the following section, both classical and modern approaches to market making are
explored. The traditional mathematical and algorithmic strategies that laid the ground-
work for automated trading systems are introduced first. These foundational methods
have been extensively used in the past.
The focus then shifts to the more recent advancements in ML and RL technologies.
This section provides a detailed exploration of how these cutting-edge techniques are
23

applied to market making. This includes an overview of various ML models, mainly SL
algorithms, and a deep dive into RL methods that enable agents to learn optimal trading
strategies through interaction with the market environment.
By comparing and contrasting these approaches, the strengths and limitations of both
traditional and modern strategies are highlighted. This comprehensive review sets the
stage for understanding the advanced methodologies discussed later in this dissertation.
2.3.1. Market making as a classic financial problem
From a financial point of view, the market making problem has been addressed for many
years and even decades. One of the most important contributions and a reference was
made by Avellaneda and Stoikov [62], where they combine the Ho and Stoll [63] frame-
work with the microstructure of the OB, based on the current inventory and a calculated
reservation price. In a nutshell, they try to find a symmetrical optimal spread based on a
reference price and a pre-defined inventory strategy. The reference price is conditioned by
the imbalance between buy and sell orders placed in the OB. This reservation price is cal-
culated with the following terms: (i) the current mid-price of the stock, (ii) the inventory
they want to hold under the strategy, (iii) a risk aversion coefficient, and (iv) the volatility
of the traded asset. With this reservation price, and including another additional term that
represents the liquidity (density) of the OB, they calculate an optimal spread that fits the
initial strategy.
This work by Avellaneda and Stoikov inspired other authors, such as Gueant et al. [64],
who introduced an evolution with a new change of variables based on Hamilton-Jacobi-
Bellman equations and a limited inventory to improve the model. More recently, the
same authors introduced another solution also based on Avellaneda’s framework where
they face the problem of multi-asset market making, addressing the challenge of manag-
ing correlated assets [65]. All these works at the end of the day propose an evolution of
this first work, by focusing on certain points.
Excluding Avellaneda’s approaches, other works deal with this problem. For example, re-
garding HFT and its underlying challenges, some authors [66] propose specific solutions
based on a previous liquidity analysis of these environments. The analysis of liquidity as
a predictor of future movements is not only used in market making tasks but also gives us
insights into the underlying short-term price intentions.
As presented, many different paths have been followed to address the market making
challenge. Some of them are based on the OB, while others are more focused on liquidity,
or other strategies.
24

2.3.2. New techniques to deal with the market making problem
Apart from the traditional market making strategies, which are predominantly based on
mathematical techniques, the adoption of ML-based strategies has become increasingly
common in recent years. The integration of ML techniques into the financial sector has
revolutionized many aspects of trading, including market making. This subsection ex-
amines how ML, diverging from classical and purely mathematical approaches, o ffers
new dimensions of analysis and strategy development in market making. With the advent
of sophisticated algorithms, the traditional landscape of market making has been trans-
formed, allowing for more dynamic and responsive trading mechanisms.
ML in market making can be broadly categorized into two streams: supervised learn-
ing (SL) and RL. Each stream provides a unique approach to tackling the complex chal-
lenges faced by MMs, from predicting market movements to developing autonomous
trading agents that interact and learn from the market environment in real-time.
The following subsections analyze both types of techniques applied to address the
market making challenge.
Market making as a machine learning problem
Beyond classical and pure mathematical approaches presented in Subsection 2.3.1, there
are also some interesting works in the context of ML. The application of ML in trading
is primarily categorized into two streams. The first stream focuses on SL, which aims
to model or forecast market dynamics directly. The second stream revolves around RL,
adopting a distinctly di fferent methodology by developing agents that engage with the
market based on a policy refined through learning experiences.
Within the realm of SL, and in the context of market making, researchers leverage
historical market data to predict future market trends or to generate trading signals. This
predictive capability is fundamental to the design of trading strategies, where signals serve
as indicators for executing trades. These predictive signals are typically derived from a
variety of sources, including OBs, financial news, and other alternative data sets. The
essence of SL in this context lies in its ability to provide foresight into imminent market
movements, thereby empowering MMs with the ability to devise more effective strategies.
Notably, some studies [67] have focused on utilizing SL for the generation of trading
signals, while others, like Dixon [68], have explored its utility in predicting short-term
stock price movements, o ffering valuable insights for MMs in their quest for optimal
trading positions. However, all these methods are not easily adaptable to changes in the
underlying environment.
25

Reinforcement learning in market making
In the exploration of RL within the market making domain, a variety of strategies and
focuses have emerged, each contributing uniquely to the understanding and advancement
of RL applications in financial markets. This section outlines the progression and dif-
ferentiation in research e fforts, highlighting both the evolution of RL strategies and the
specialization towards market making in both single-agent and multi-agent environments.
Development of RL strategies in market making: Early works by Chan and Shel-
ton [69] introduced the use of di fferent RL strategies, such as SARSA and actor-critic,
laying the groundwork for further exploration in this field. They use a very simple sim-
ulated market, with discrete state variables. They demonstrate that RL can be further
explored to solve MM problems in more complex scenarios. Following this, Yagna Pa-
tel [70] innovated by combining micro and macro agents, each receiving different inputs,
to craft a profitable strategy. Spooner et al. [71] then shifted focus towards creating a real-
istic simulation of an OB using Q-learning agents, advancing the realism and applicability
of RL models in market making scenarios. Continuing with Q-learning, Lokhacheva et
al. [72] developed an agent influenced by trading signals such as Exponential Moving
Average (EMA) and Relative Strength Index (RSI) to define the state space.
Multi-agent environments and market making:Research expanded to include multi-
agent environments, recognizing the complexity and dynamism of real-world markets.
Wang, Zhou, and Zeng [73] conducted multiple experiments in simulated markets with
both informed and uninformed traders, with a particular focus on inventory optimization.
More recently, Ganesh et al. [74] delved into competitive multi-agent scenarios using
ABIDES [75] as a simulation environment, where RL agents aimed to outperform other
MM agents through the discovery of profitable policies.
Consideration of inventory risk: A notable gap in many market making RL strate-
gies is the lack of attention to inventory risk, with a predominant focus on maximizing
profits and losses (PnL). Approaches that do not consider inventory management in their
solutions present a significant limitation. To bridge this gap, research has evolved to in-
corporate inventory management and associated risks within RL strategies. The methods
applied to address this vary: some works apply penalties to changes in inventory held
during trading sessions [71], [76], while others penalize the entire inventory held to dis-
courage asset accumulation [77], [78]. An alternative method penalizes the inventory
held only at the end of episodes, often utilizingConstant Absolute Risk Aversion(CARA)
utility to gauge risk aversion [79]–[81].
2.4. Simulated environments in RL. ABIDES
RL utilizes a variety of training methodologies, primarily categorized into o ffline and
online learning strategies. Depending on the learning strategy employed, they can be
26

classified into offline RL algorithms (data-based), and online RL algorithms (interacting
with the environment). Furthermore, online learning strategies can be implemented in
two distinct ways: one involves operating in real environments, and the other employs
simulators. Each approach addresses di fferent research needs and presents its own set of
advantages and challenges.
Online RL performed in real environments allows the agent to interact directly
with the actual system, enabling real-time learning and adaptation. This method ensures
that strategies are developed and refined in the exact environment where they will be
implemented, potentially enhancing their effectiveness. However, direct interaction with
the live environment means that errors can have immediate and significant financial con-
sequences. Additionally, the complexity and variability of real-world environments can
complicate the learning process and affect the stability of the model.
Online RL performed in simulators provides a controlled yet dynamic setting for
training and testing RL policies. Using simulators for online RL allows for extensive
testing of strategies without the risk of real-world repercussions, provides the ability to
experiment with a wide range of scenarios, and generates diverse data scenarios to enrich
learning opportunities. However, ensuring that the simulated environment accurately re-
flects real-world conditions poses significant challenges, and discrepancies in simulation
accuracy can lead to strategies that perform well in the simulator but less so in reality.
Sim2Real strategies [82], [83] have to be applied to reduce that gap. Additionally, devel-
oping and maintaining a high-fidelity simulator can be resource-intensive.
For this thesis, the decision to employ a simulator-based RL approach is driven by sev-
eral key considerations, primarily the necessity for a method that offers both adaptability
and safety. Utilizing a simulator allows for dynamic interaction and strategic exploration
across a diverse range of market conditions, without incurring the financial risks and po-
tential losses associated with real-world market engagement. This controlled environment
enables the detailed testing and iteration of RL strategies under simulated market condi-
tions that can be adjusted to reflect various levels of complexity and unpredictability.
The use of a simulator also provides the opportunity to model and analyze how these
strategies would perform under extreme market conditions that are rare in the real world
but critical for testing the robustness of financial strategies. Furthermore, simulators can
accelerate the learning process, as they allow for “faster than real-time” simulations, en-
abling the collection of vast amounts of interaction data in a relatively short period. This
capability is invaluable for deep learning approaches that require extensive data to refine
and validate their algorithms.
Additionally, the simulated environment supports a level of granularity in control and
monitoring that is often unfeasible in real markets. Researchers can easily adjust vari-
ables, introduce new elements, or isolate specific factors to observe how these changes
affect the performance of RL agents. This flexibility is crucial for dissecting the mechan-
ics of complex strategies and for understanding the nuanced behaviors of RL agents under
27

Figure 2.4: Reinforcement learning framework in ABIDES-Gym vs. regular ABIDES.
Picture from [84]. (adapted fonts)
.
different market dynamics.
Overall, the choice of a simulated environment for online RL in this thesis provides
a practical and e ffective framework for conducting rigorous academic research. In this
regard, all experiments have been conducted in a simulated event-based trading environ-
ment called ABIDES[75]. ABIDES (Agent-Based Interactive Discrete Event Simulation)
is a market simulator that enables the running of multiple setups, which increases the
variance of the data and reduces over-fitting, among other benefits. In its more recent ver-
sions, ABIDES is being integrated as an OpenAI gym environment [84]. Essentially, it is
an agent-based simulation tool where defined agents interact with each other in a trading
session, much like a real market. Each agent in the market has its strategy (non-informed
traders, MMs, momentum agents, etc.), and the natural interaction among them defines
the price movement of the negotiated assets. The main architecture of the ABIDES sys-
tem, both the standard ABIDES and the gym version, is depicted in Figure 2.4.
The ABIDES simulation framework is centered around a discrete event-based kernel,
found in the Kernel class, and is required for all simulations. All agent messages pass
through the kernel’s event queue. The kernel supports geography simulation, computation
time, and network latency while enforcing simulation ‘physics’ by maintaining the current
simulation time and ensuring no inappropriate time travel. Key features of the ABIDES
kernel, as described by authors in [75], include:
28

• Historical date simulation: Simulations occur on configurable historical dates,
allowing real historical data to be seamlessly injected.
• Nanosecond resolution: Time is simulated at nanosecond resolution using Pandas
Timestamp objects, allowing agents to operate on different time scales with minimal
overhead.
• Global virtual time (GVT): Tracks the latest simulated time for which all mes-
sages are processed. GVT typically advances faster than wall clock time.
• Current time per agent: Maintains a “current time” per agent, incremented after
Agent.receiveMessage() or Agent.wakeup(), with message delivery delayed if the
agent’s current time is in the future.
• Computation delay: Stores a computation delay per agent, added to the agent’s
current time and outbound message times, adjustable for di fferent computation
events.
• Configurable network latency: Maintains a pairwise agent latency matrix and a
latency noise model, simulating network conditions and agent location, including
co-location.
• Deterministic but random execution: Uses a single pseudo-random number gen-
eration (PRNG) seed for initialization, generating individual PRNGs per agent to
ensure identical simulations for the same seed. This setup supports A /B testing
without affecting other agents’ stochastic sources.
Additionally, ABIDES works by using an internal OB, which tracks all open orders
and the last trade price for a single stock symbol. All the activity is logged through the
exchange agent. The OB implements the following functionality:
• Order matching: Matches incoming orders against the appropriate side of the OB,
selecting the best price match. If multiple orders have the same price, the oldest
order is selected.
• Partial execution: Incoming or matched limit orders may be partially executed.
The remaining quantity is reduced, and the matching continues. Participants receive
an “order executed” message for each partial execution, noting the fill price. The
average price per share is recorded as the last trade price when the incoming order
is executed in multiple parts.
• Order acceptance: If the incoming limit order has a remaining quantity after all
possible matches, it is added to the OB for later fulfillment, and an “order accepted”
message is sent.
29

• Order cancellation: Locates the requested order by unique order id, removes any
remaining unfilled quantity and sends an “order canceled” message.
The platform also produces realistic slippage naturally due to dynamic computation
and network delays, without the need for an explicit slippage model.
This tool is used in many trading studies [85]–[87] as it can simulate very realistic
trading markets. It allows for the generation of diverse market configurations according
to the needs of a specific study.
2.5. Discussion
As stated in Section 2.3, the market making problem has been approached from many
different perspectives, ranging from more mathematical and quantitative methods to more
recent ML techniques. Some works focus solely on profitability [68], [72], while many
others also attempt to manage the inventory problem [67], [69], [71], [76]–[81]. Regard-
ing those works that include inventory in their strategies, the main strategy is to include
a static penalty term in the reward function. Some apply this penalty at the end of the
episode [79]–[81], and others along the trading session [71], [76]. However, in both al-
ternatives, the reward function is static and does not adapt to the changing market
conditions, as proposed in this dissertation. Additionally, there are di fferent approaches
to training. Some works use historical data to train the agent [71], [72], [78], while others
generate some kind of simulation based on the OB [79], fitted on historical data [71], [77],
or as the result of agent-based interactions [69], [74], [81]. In this dissertation, the use of
an agent-based market simulator is proposed because of the many advantages it has, as
broadly discussed in Section 2.4.
Additionally, unlike prior works that primarily targeted profitability and risk manage-
ment from an RL perspective, this thesis expands the focus to include the interaction
among MM agents . The analysis delves into how these interactions a ffect profitabil-
ity and explores the diversity of strategies adopted by competing MM agents in both
single-agent and multi-agent setups. Direct transfer learning is employed to assess the
performance and policies of pre-trained RL MMs in these experiments. This dissertation
focuses on applying RL to this problem, using various methods. While there exists some
ML approaches in the state of the art, we manage the problem as a non-episodic method
that does not rely on a “world model”, or just a model, of the financial market or some
of its dynamics. Attempting to model a financial market given its heavy stochasticity and
incomplete information is not an appropriate alternative, from our point of view. The
proposed MM must be able to operate continuously, adapting to the non-stationarity of a
changing market.
Last but not least, it is crucial to mention thatnone of the aforementioned strategies
consider non-stationarity in their approaches, which is a substantial weakness. There
are RL algorithms that attempt to manage the non-stationarity of the environments, as
30

stated in Subsection 2.1.5. Within the domain of single-policy algorithms, various strate-
gies revolve around a single policy that evolves in response to environmental changes.
One notable algorithm is RUQL (Referenced Update Q-learning) by [37], which adjusts
Q-values based on new experiences or changes in transition probabilities, applying uni-
form updates based on new data. Despite its innovation, RUQL faces several challenges,
such as the diminishing relevance of prior experiences amidst new explorations and a full
understanding of MDP dynamics. Additionally, RUQL’s design, aimed at discrete state
spaces, is not fully compatible with dynamic spaces. Q-learning frameworks have seen
various modifications to better suit non-stationary environments through learning rate ad-
justments. For instance, [38] enhanced Q-learning by dynamically altering the learn-
ing rate through gradient descent, demonstrating superiority over traditional methods in
shifting environments. However, this model is limited to scenarios with state dynam-
ics. Similarly, [39]’s OSA fine-tunes the Q-learning rate to counteract noise in non-static
environments, focusing on minimizing estimation errors rather than directly improving
learning outcomes. OSA, however, presupposes prior knowledge of transition and reward
structures, a premise not assumed in our work.
In contrast, multi-policy algorithms involve maintaining and selectively applying mul-
tiple policies or contexts, especially in non-episodic settings. The RL-CD model [41]
exemplifies this approach, utilizing a series of models chosen based on performance sig-
nals and generating new ones as needed. Despite its potential for adaptability, RL-CD
requires meticulous parameter adjustments specific to each challenge and is limited to
discrete decision-making environments. While other studies like [42] aim to simplify
these aspects, they remain largely conceptual. Alternatives such as HM-MDP by [43]
and ContextQL by [44] explore the use of model-based and policy-variance strategies.
However, they often assume known environmental patterns, which is a risky assumption
in trading environments. Notably, change point detection strategies, despite their inno-
vation, may suffer under gradual environmental shifts or false positives, a ffecting agent
performance. For these reasons, CL techniques have been chosen instead of directly ap-
plying the aforementioned non-stationary RL algorithms.
In this thorough pursuit, there is a clear line of works and publications that must be
considered. In the Table 2.1, the evolution of this research is shown. Every objective
presented in Section 1.3 is accompanied by a group of relevant works and techniques.
Both works that serve as a comparison with the proposed methods and/or techniques and
frameworks that are the basis of the research are clearly presented in the table.
The first objective, “Evaluate RL for profitable market making in competitive scenar-
ios”, is addressed by building on the previous work of Ganesh et al.[88], who explored the
use of RL in market making and provided a basis for further research in this area. This
first study establishes the foundations by validating RL as an appropriate technique for
addressing the market making problem.
The second objective, “Advanced management of inventory using RL”, focuses on
31

inventory management and is driven by two di fferent approaches. The first, inventory
management via reward engineering, is a common method addressed in the literature.
The main difference between the works lies in how they define the reward function and
the penalty term for inventory holding. This is evident in the works by [71] and [78],
which serve as comparison points. However, these approaches share a common limitation:
they do not consider the adapting situation of the MM in terms of liquidity. A fixed
penalty is established throughout the experiment, a ffecting it equally at all times. Such
restrictive reward functions can negatively impact total returns, as they prompt the agent
to act more cautiously. Conversely, the reward function presented in this thesis goes a step
further by considering the liquidity ratio (cash/inventory value) of the MM throughout the
experiment. This allows the agent to assume more risks dynamically if it gathers more
cash from its operations. Risk is, therefore, adapted to the changing situation of the agent
without increasing risk aversion. This enables the agent to obtain more profits when the
situation is favorable.
Following this approach, and considering the multi-objective nature of the market
making problem, a strict MORL alternative is proposed. Reward engineering has many
weaknesses and challenges, such as the trial-and-error process of debugging, the need
to balance sub-goals, and other issues presented in Subsection 2.1.4. To find a more ro-
bust approach that combines RL and multi-objective problems, the work evolves into a
MORL framework. Based on previous works by [89], a MORL MM is proposed. This
empowered agent can specialize in di fferent sub-goals separately, avoiding the complex
and sometimes biased reward engineering process. This alternative is compared to the
previous reward-engineered approach [90] to demonstrate the power of this novel appli-
cation.
Finally, the third objective “Adaptability in market making strategies to address non-
stationarity”, addresses non-stationarity in market making strategies. To the best of our
knowledge, no work addresses the market making problem in non-stationary environ-
ments using RL. All the literature revolves around training an agent in a specific market
situation. Regarding dealing with non-stationary environments, di fferent strategies have
been introduced in Subsection 2.1.5. None of the current non-stationary algorithms, in
our opinion, fits well with the current problem. Some rely on having a model of the envi-
ronment, some are adapted to discrete state and action spaces, and others use changepoint
detectors. Apart from RL, non-stationarity has also been addressed using di fferent ML
techniques. Most of them, under the concept of CL, allow the model or the agent to learn
from new data without losing past knowledge. This dissertation proposes a novel way
to deal with non-stationarity from a multi-policy perspective. Additionally, the proposed
technique is compared with existing CL techniques, such as EWC [53], DR [50], and FL
[49]. Combining a robust multi-objective RL approach with non-stationarity adaptation
based on RL is a powerful proposition that can serve as the foundation for many MMs.
There are no other works that address this problem in such a holistic way as presented
here.
32

In summary, Table 2.1 presents a comprehensive overview of the research goals and
the relevant reference papers that support each objective. This table not only illustrates
the evolution of the research but also demonstrates how each objective is grounded in and
supported by previous works and techniques.
All the experiments in this research have been conducted in Python 3.11. All the
simulations have been run on a PC Intel i7-9700 Linux (WSL2) with an ASUS 1070GTX
GPU, and 32GB RAM. Torch library has been used to train the models in GPU with
CUDA.
33

Title Objective Reference Papers.
RL in marker
making opera-
tive
Objective 1:
Evaluate RL
for Profitable
market making
in Competitive
Scenarios.
Evolution of previous work:
• S. Ganesh, N. Vadori, M. Xu, H. Zheng, P. Reddy, and M. Veloso, “Re-
inforcement learning for market making in a multi-agent dealer mar-
ket,” Nov. 2019.
Inventory man-
agement via Re-
ward Engineer-
ing
Objective 2 (a):
Advanced Man-
agement of
Inventory Using
RL:
Reward engi-
neered approach
Comparison to other similar RL solutions:
• B. Gasperov and Z. Kostanjcar, “Market making with signals through
deep reinforcement learning,” IEEE Access, vol. 9, pp. 61611–61622,
2021.
• T. Spooner, J. Fearnley, R. Savani, and A. Koukorinis, “Market making
via reinforcement learning,” AAMAS ’18, pp. 434–442, Apr. 2018.
Solution based on previous work:
• O. Fernández, F Fernández, and F. García. 2022. Deep Q-learning mar-
ket makers in a multi-agent simulated stock market. In Proceedings of
the Second ACM International Conference on AI in Finance (ICAIF
’21). Association for Computing Machinery, New York, NY , USA, Ar-
ticle 19, 1–9.
Inventory man-
agement via
MORL
Objective 2 (b):
Advanced Man-
agement of
Inventory Using
RL:
Multi-objective
RL (MORL)
Approach
MORL solution based on framework :
• P. Vamplew, R. Dazeley, A. Berry, R. Issabekov, and E. Dekker, “Em-
pirical evaluation methods for multiobjective reinforcement learning al-
gorithms,” Machine Learning, vol. 84, no. 1, pp. 51–80, Jul. 2011.
Comparison with the former reward-engineered approach:
• O. Fernández, F. Fernández, and J. García. 2023. Automated market
maker inventory management with deep reinforcement learning. Ap-
plied Intelligence 53, 19 (Oct 2023), 22249–22266
Non-
Stationarity:
POW-dTS
Objective 3:
Adaptability in
market making
Strategies to
Address Non-
Stationarity.
Comparison of the proposed method to other CL ML techniques:
• Elastic Weight Consolidation:
– J. Kirkpatrick et al., “Overcoming catastrophic forgetting in neural
networks,” Proceedings of the National Academy of Sciences, vol.
114, no. 13, pp. 3521–3526, 2017.
• Data Rehearsal:
– “Catastrophic forgetting, rehearsal, and pseudorehearsal,” Con-
nection Science, vol. 7, pp. 123–146, 1995.
• Freezing Layers:
– A. Sorrenti, G. Bellitto, F. Salanitri, M. Pennisi, C. Spampinato,
and S. Palazzo, “Selective freezing for e fficient continual learn-
ing,” IEEE Computer Society, Oct. 2023, pp. 3542–3551.
Table 2.1: Summary of research goals and reference papers.
34

3. RL IN MARKER MAKING OPERATIVE
The initial objective of this thesis is to a ffirm the e fficacy of RL in addressing the
challenges associated with market making and to deepen our knowledge and application
of RL in the realm of market making in financial markets. The first aim is to develop
an agent proficient in executing the MM task of injecting liquidity into a particular asset,
ensuring profitability. In this phase, inventory management is not considered, although is
included as part of the reward.
Bearing all these aspects in mind, the goal of this chapter is to study the behavior of
the MMs from an agent-based perspective. Here, the proposal is the application of RL for
the creation of intelligent MMs. In particular, it aims to define an environment where RL
MMs compete with other predefined MM agents, and also among themselves, to achieve
the most profitable strategy. According to this, the intention is to analyze the behavior of
MMs from a competitive and non-competitive point of view. This analysis allows for a
better understanding of the trading strategies they employ when trading alone and when
they compete against other RL MMs.
The experiments are conducted using ABIDES, introduced in Section 2.4, which sim-
ulates a regular financial market. It is inside this environment where experimental market
makers interact with investor agents that always pick up the cheapest MM in terms of
spread.
The chapter is organized as follows: Section 3.1 introduces the task of applying RL on
financial markets, defining states, actions, and rewards. It also represents the architecture
of RL agents. Section 3.2 introduces the rationale behind the experiments. Section 3.3
describes all the experiments launched, with the results obtained. Next in Section 3.4, the
main conclusions obtained from the research are discussed. At last Section 3.5 details the
main contributions of this study.
3.1. Mapping a market making task onto a RL task
This section describes the process of mapping the market making problem onto a RL
framework. Initially, it delineates the state space S , the action space A, and the reward
function R to provide a comprehensive understanding of the system. The transition func-
tion T, which models the dynamics of the environment, is assumed to be unknown to the
learning agent. Following this, the architecture of the DQN agent, including its NN, and
the algorithm that underpins the learning process are presented.
35

3.1.1. State and action space
The proposed RL MM agent is defined by a state space comprising 10 features that capture
the essence of market dynamics: (i) the count of buy transactions completed in the last
time step, (ii) the volume of stocks acquired, (iii) the count of sell transactions completed,
(iv) the volume of stocks sold, (v) the inventory level (which can be positive for a surplus
or negative for a deficit) from the last time step, (vi) the current inventory level, (vii)
the fluctuation in the stock’s mid-price ( Pvar = current mid price− last mid price), (viii)
the current reference spread, (ix) the previous time step’s spread, and (x) the total traded
stock volume, typically referred to as volume. This selection of state space variables
is deemed optimal for capturing crucial market elements, detailing not only the current
market conditions like spread and inventory but also the transition from the prior time step,
including price evolution—an essential factor for valuing inventory. While other methods,
such as employing rolling averages or relative di fferences of specific inputs, could also
be viable, they have not been considered. However, in later chapters, an experimental
analysis has been performed evaluating the impact of including trend information.
Actions: The action space for the MMs consists of three primary decision variables
at each time step: (i) the buy spread, (ii) the sell spread, and (iii) the inventory volume
to hedge. These variables have been discretized, forming an action space spanning these
three dimensions. This discretization aims to enhance the learning agent’s convergence
speed by prioritizing rapid decision-making over pinpoint accuracy in value selection. It is
worth mentioning that other approaches based on continuous actions have also been tested
previously, but the discretized version has achieved better results. Actions entail choosing
a value, referred to as epsilon (buy, sell or hedge) throughout this dissertation, from a
predefined list of values η(b,s)i ∈ {−1,−0.8,−0.6,..., 0.6, 0.8, 1} to adjust buy and sell
spreads as S preadmm = S preadmkt· (1 +η(b,s)i), where S preadmkt represents the market’s
current spread and S preadmm the spread o ffered by the MM. Hedging actions similarly
involve selecting an epsilon to proportionally reduce inventory by a percentage ranging
from 0% to 100%, asηhi∈{ 0, 0.25, 0.5, 0.75, 1}. This strategy simplifies the action space
to 605 discrete actions, derived from all possible combinations of buy, sell, and hedge
epsilons.
Rewards: The reward function is designed to optimize the MtM value, reflecting not
only the profits from individual transactions but also the valuation of the held inventory.
Although inventory value is included in the MtM calculation, no inventory control mea-
sures are applied. Consequently, a single-objective approach is pursued. The reward R at
each time step i is calculated as:
Ri = Ei + PnLi− HgCi (3.1)
Where Ei represents the earnings or profit from trading activity, calculated as the
product of the number of traded stocks and the market spread;PnLi reflects the inventory’s
36

profit or loss based on mid-price changes; and HgCi accounts for the costs incurred from
hedging inventory.
Through the delineation of state and action spaces, alongside a carefully constructed
reward function, the RL MM agent is designed to learn profitable trading strategies within
the simulated market environment.
3.1.2. Deep Q-learning MM agents (DQL-MM)
Due to the continuous and high-dimensional nature of the proposed RL task, this first
approach opts for using deep learning strategies to learn the behavior policy of the RL
MMs. Each RL MM is based on a DQN architecture [17]. These DQN MM agents
(DQL-MM) consist of a fully connected NN that predicts the expected reward of taking
an action from a specific state at each time step. The NN is retrained, with its weights
adjusted every 200 time steps. The defined architecture for the experiments includes
an input layer with 10 nodes, three hidden layers with 32 nodes each, and one output
layer with 605 nodes, representing one output node for every possible action. Figure 3.1
provides a graphical representation of the proposed DQN architecture.
Figure 3.1: Deep NN architecture used for the DQL-MM agent.
All three hidden layers use the ReLU (rectified linear unit) activation function, while
the output layer employs a linear activation function. ReLU is an activation function well-
known for mitigating the vanishing gradient problem, a common issue in neural networks.
Additionally, it allows for faster convergence. For the output layer, since this is a regres-
sion problem where expected returns are predicted for each action, the linear activation
function is a good option. The Adam optimizer has been chosen because it handles noisy
data effectively, and Mean Absolute Error (MAE) is used as the loss metric. Input data has
been previously standardized using StandardScaler from Scikit-learn library [91]. Each
output represents a combination of one buy’s epsilon, one sell’s epsilon, and one hedge’s
37

epsilon. Keras for Tensorflow has been used for the NN model. This architecture was
ultimately chosen after several trials. Additional layers (4 and 5) and more neurons (64,
128, and 512) were tested, but no performance improvement was observed. Furthermore,
smaller networks typically require fewer gradient steps to converge.
Algorithm 2 shows the learning process of DQL-MM agents, and it is based on expe-
rience replay [17]. For every simulation considered, DQL-MM imports NN from the last
simulation (line 5 in Algorithm 2). Once a simulation starts, along all-time steps DQL-
MM queries the current reference market spread (line 8) S preadmkt that comes from the
interaction of the rest of agents (Subsection 3.3.1). After that, it is time to pick an action.
According to theϵ-greedy strategy and the value of the parameterϵ, the selected action at
will be the best possible (greedy) (line 11) or a random one (line 13). The best possible
action will be returned by the NN that computes the value function of every possible ac-
tion for that state. DQL-MM calculates rewards earned the previous time step according
to taken actions, and the tuple⟨st, at, st+1, rt⟩ is stored to a bufferD (line 17). Every 200
time steps, NN is retrained with stored tuples inD (line 20).
Algorithm 2 DQL-MM algorithm
1: Initialize memoryD←∅ , t← 0
2: for each simulation do
3: Init simulation
4: if Saved agent state then
5: Get last NN weights
6: end if
7: for every time step in simulation do
8: Get S preadmkt from market data.
9: Initialise state, st
10: if rand <ϵ then
11: at=best_action(buy, sell and hedge epsilons )
12: else
13: at=random_action(buy, sell and hedge epsilons )
14: end if
15: Execute action at, observe rt and st+1
16: Applyϵ decay
17: Store transition⟨st, at, st+1, rt⟩ buffer inD
18: t← t + 1
19: if t mod 200 = 0 then
20: Retrain NN with transitions sampled fromD
21: end if
22: st← st+1
23: end for
24: end for
38

3.2. Single-agent and multi-agent scenarios
Two main cases are studied in this work. Initially, the aim is to evaluate how a single
DQL-MM agent behaves in a stationary competitive trading domain, alongside two other
non-RL MM agents (Subsection 3.3.2). This evaluation focuses on the DQL-MM agent’s
performance in terms of profitability and stability compared to non-RL MM agents, as
well as on the significance of the variables involved in the decision-making process. Once
this scenario is examined, it becomes especially relevant to assess how DQL-MM agents
behave when competing against each other in an environment perceived as non-stationary
by every agent (Subsection 3.3.3). In this more complex scenario, MMs must adapt their
strategies dynamically in response to the actions of their competitors to maximize re-
wards. Furthermore, in this multi-agent environment, the e ffectiveness of policy transfer
is evaluated to determine the performance of winning pre-trained policies in new sce-
narios (Subsection 3.3.4). This evaluation is crucial for understanding whether successful
strategies from simulated environments, such as ABIDES, can be effectively transferred to
real markets. The subsequent experiments analyze both the single-agent and multi-agent
approaches, providing valuable insights into MM behaviors, strategies, and profitability.
3.3. Experiments
Three distinct configurations are explored in this experimental segment. The first two con-
figurations aim to identify the best strategies in two different contexts: (i) a scenario fea-
turing a single DQL-MM agent in competition with two predefined non-RL MMs (Sub-
section 3.3.2), and (ii) a scenario where three DQL-MM agents compete against each
other, alongside two additional non-RL MM agents (Subsection 3.3.3). The third exper-
iment (iii) focuses on assessing the effectiveness of transferring pre-trained MM policies
into a competitive setting (Subsection 3.3.4).
The setup for these experiments is detailed in the following Subsection 3.3.1.
3.3.1. Experimental setting
Each simulation conducted in ABIDES was configured with the following lineup of
agents:
• 100 Noise agents: These agents execute orders of a fixed size in random directions.
• 10 Value agents: Equipped with fundamental time series data, these agents make
trades based on the deviation of the mid-price from their forecasted mid-price.
• 10 Momentum agents: These agents act upon the crossover of 50-step and 20-step
moving averages.
39

• 1 Adaptive POV (percentage of volume) MM agent : By placing orders at pre-
determined intervals around mid-price, this agent injects a certain level of liquidity
into the synthetic market. POV , or percentage of volume, refers to the proportion
of the market maker’s order size relative to the total transacted volume observed
during the previous lookback window.
• 1 Exchange agent : This agent facilitates the interactions among all participating
agents and manages the OB.
Each simulation represents a 2-hour market session, limited by computational con-
straints. However, the proposed strategy performs numerous operations during these ses-
sions, initially providing su fficient data to validate its potential. During these two-hour
market sessions, the agents’ interactions establish a reference spread ( S preadmkt) and
induce specific price volatility patterns based on their trading behaviors. Within this dy-
namic environment, the activities of experimental MMs are scrutinized. Each experiment
features three distinct types of MMs:
• DQL market maker (DQL-MM): The RL MM. It utilizes deep Q-learning (DQL)
to make market making decisions.
• Random Market Maker (Random-MM): Employs random spreads and hedges at
each time step.
• Persistent market maker (Persistent-MM) : Maintains a constant, randomly se-
lected spread and hedging strategy throughout the simulation. More precisely, it
randomly selects one buy, one sell, and one hedging strategy at the beginning of
every round and keeps them until that trading round is over. It repeats this process
for all rounds.
The market making agents in this study are supplemented by interactions with 50 ad-
ditional investor agents. These investor agents issue buy or sell orders in a uniformly ran-
dom manner, consistently opting to match their orders with the MM offering the narrow-
est spread—thus, the most cost-e ffective option for either buying or selling . There-
fore, as it is a zero-sum game, all existing market makers (RL, random, and persistent)
compete with each other to match the 50 investor orders. In scenarios where MMs
present identical spreads, investors select one at random to prevent any bias that could
arise from the order in which MM orders are placed. It is important to note that transac-
tion fees were not considered. This means that all the buys and sells in the simulations
were performed at 0 cost.
The DQL agents are configured with specific initial parameters: starting ϵ is set at
0.99, with anϵ decay rate tailored for 250 simulations and a minimum floor of 0.01. The
discount factor,γ, is chosen to be 0.6.
40

To ensure the robustness and reliability of the experimental findings, a total of 250
simulations were conducted for each experimental setup. Moreover, to mitigate the impact
of stochastic variability in the results, 5 rounds of these simulations were executed in
parallel using different seeds.
3.3.2. Single-agent market maker
The first experiment focuses on training a single DQL-MM agent in a competitive setting
against two non-RL MMs: a Random-MM and a Persistent-MM. Figure 3.2 illustrates
the comparative performance evolution of the three market making agents throughout the
training period. Notably, the DQL-MM agent begins to secure positive rewards from the
early stages of the experiment, outperforming the other two agents, as expected. However,
a marked performance improvement is observed around simulation 175, indicating a sig-
nificant enhancement in the agent’s market-making strategy due to increased exploitation
from that point onward.
Figure 3.2: Single-agent training experiment. 50-simulation rolling average window.
Table 3.1 presents the average rewards from 250 simulations for each experimental
MM. It is observed that both the Random-MM and Persistent-MM agents conclude the
experiment with negative rewards on average. Conversely, the DQL-MM agent success-
fully learns an effective policy that distinctly surpasses the performance of the former two
agents in terms of earnings.
41

Table 3.1: Single-agent experiment average results (250 exp) (USDx103).
MM Agent MEAN TOP BOTTOM STD
DQL-MM 159 782 -148 180
RANDOM-MM -23 13 -94 11
PERS-MM -37 0 -91 15
Figure 3.3 illustrates the progression of buy, sell, and hedge values throughout the
experiment, reflecting the actions executed by the market maker. The values represented
are the moving averages across 50 simulations for each of these metrics, showcasing the
adaptive strategy of the DQL-MM over time. Notably, both buy and sell epsilons tend
to converge around a value of−0.2, as depicted in Figure 3.3. However, the volatility of
the buy epsilon increases after the 150th simulation, with noisy and variable buy prices,
suggesting that an optimal strategy was not found. The adoption of negative values for
buy/sell epsilons implies o ffering prices lower than the S preadmkt, enhancing the likeli-
hood of matching with an investor but yielding lower rewards per trade. Meanwhile, the
hedge epsilon value converges near 0.2, indicating the DQL-MM’s strategy to liquidate
20% of its inventory at each time step, thereby incurring hedging costs at the S preadmkt.
Figure 3.3: Evolution of epsilons throughout the single-agent experiment 50-simulation
rolling average window.
Input variable analysis: A closer examination of the DQL-MM single-agent, which
exhibits superior performance despite volatility, allows for an in-depth analysis of the
input variables influencing its NN. Utilizing tools like SHAP [92], the significance of
various variables in shaping the agent’s final policy and strategy can be determined. This
analysis not only aids in optimizing variables but also enhances comprehension of the MM
policy and its inputs. Correspondingly, Figure 3.4 presents the impact of di fferent state
42

space variables on the agent’s action selection process. The length of each bar signifies
the variable’s importance, with the bar color denoting the specific action taken, as each
color represents a distinct action. The graph underscores the special relevance of Pvar
(MidPrice_Variation) in action determination. The second most influential variable is
S preadmkt (Current_spread), while variables related to inventory inv (Last_Inventory and
Inventory) and the previous time step’s S preadmkt (Last_Spread) exhibit minimal e ffect
on the model.
Figure 3.4: SHAP variable importance summary plot.
3.3.3. Multi-agent RL market makers
In the second experiment, the competitive landscape is expanded to include two additional
RL MM agents, resulting in a total of three DQL-MM agents contending against each
other within the same trading environment. It is important to note that, to date, no transfer
learning has been applied. All the RL agents are being trained in the competitive envi-
ronment from scratch. This scenario also features the participation of one Random-MM
and one Persistent-MM agent. Figure 3.5 showcases that only the first DQL-MM agent
(#1) manages to secure notable returns, a trend that becomes particularly evident starting
from simulation number 175. Interestingly, towards the final phases of the experiment,
DQL-MM agent #3 begins to demonstrate a profitable strategy, which in turn slightly
diminishes the performance of DQL-MM #1. On the other hand, DQL-MM agent #2
struggles to identify a viable competitive strategy throughout the experiment, ultimately
concluding with negative returns.
43

Figure 3.5: Multi-agent experiment. 50-simulation rolling average window.
As depicted in Table 3.2, only the first DQL-MM agent (#1) manages to conclude
the experiment with positive average returns. Throughout the experiment, each agent
embarks on a journey to discover and adapt to the most beneficial strategy, evidenced
by their evolving tactics. This evolutionary process of strategy adaptation is detailed
in figures Figure 3.6 (DQL-MM #1), Figure 3.7 (DQL-MM #2), and Figure 3.8 (DQL-
MM #3). These figures specifically illustrate the progression of buy, sell, and hedge
epsilons for each of the RL agents, showcasing the individual strategic adjustments made
throughout the experiment.
Table 3.2: Multi-agent experiment average results (250 exp) (USDx103)
MM Agent MEAN TOP BOTTOM STD
DQL-MM #1 129 1.018 -94 179
DQL-MM #2 -45 111 -393 27
DQL-MM #3 -5 434 -343 24
RANDOM-MM -38 9 -87 7
PERSISTENT-MM -45 2 -85 6
As observed in the mentioned figures, the buy and sell epsilons among the three DQL-
MM agents vary as they dynamically adjust their strategies to respond to the evolving
environment. It is important to highlight that, in this zero-sum scenario, any strategy
adopted by one agent has a direct impact on the performance of the others; an improve-
ment in one agent’s performance typically results in a decrease for the others. Based on
this dynamic, the agents develop their strategies in distinct manners.
DQL-MM #1 (Figure 3.6) adopts a strategy for epsilons that resembles the approach
44

taken by the sole DQL-MM agent in the first experiment, exhibiting less variance through-
out the experiment. The strategy of DQL-MM #3 (Figure 3.8) closely mirrors that of
DQL-MM #1, albeit with a noticeable increase in the volatility of the buy epsilon as it
explores new policies. For both, the average buy and sell epsilons tend towards approx-
imately−0.4. Conversely, the strategy of DQL-MM #2 (Figure 3.7) deviates from the
other two agents by shifting its sell epsilons towards positive values.
Figure 3.6: DQL-MM #1 Epsilons buy, sell and hedge (η) -50-simulation rolling average
window.
Figure 3.7: DQL-MM #2 Epsilons buy, sell and hedge (η). 50-simulation rolling average
window.
45

Figure 3.8: DQL-MM #3 Epsilons buy, sell and hedge (η). 50-simulation rolling average
window.
Hedging epsilons are very similar in all three DQL-MM, converging smoothly to 0.2.
This hedging epsilon seems to be the most favorable in this environment too.
It can be concluded that when multiple RL agents participate in the same experiment, they
face greater challenges due to the competitive environment, although they strive to adapt
their policies to seek profitability.
The hedging epsilons for all three DQL-MM agents display considerable similarity,
steadily converging towards a value of 0 .2. This convergence suggests that a hedging
epsilon of 0.2 may be the most advantageous strategy within this specific environment. It
can be deduced that the presence of multiple RL agents in a singular experiment intensifies
the competitive dynamics, significantly challenging each agent. Despite these challenges,
the agents endeavor to adjust their policies in pursuit of profitability.
3.3.4. Direct transfer learning in multi-agent RL market makers
After completing the experiments in sections 3.3.2 and 3.3.3, an interesting area to ex-
plore is the performance of the top DQL-MM agents when competing against each other
in the same scenario. This exploration aims to verify whether a pre-trained policy exists
that outshines the others, thereby having the potential for direct application in subsequent
experiments. This concept has been analyzed through direct transfer learning, whereby
NNs from the “best performance” DQL-MM agents were applied. Specifically, concern-
ing the initial experiment in Subsection 3.3.2, to determine the most e ffective learned
policy, the performance of NNs from 10 distinct simulations was evaluated at intervals:
[0, 10, 20, 30, 40, 50, 100, 150, 200, 250]. The outcomes of this performance assessment
are depicted in figure Figure 3.9. According to the findings illustrated in this figure, the
NN that achieved the best performance was from simulation 200; hence, this particular
NN was chosen for transfer.
46

Figure 3.9: NN Performance evaluation. Mean rewards obtained by every NN tested.
Regarding the second experiment detailed in Sections 3.3.3, the same NN, notably
from simulation 200, was employed. This pre-trained NN was introduced into a novel
environment where it competed alongside another learning DQL-MM agent, in addition
to facing off against a Random-MM and a Persistent-MM agent. Figure 3.10, consistent
with previous experiments, illustrates the rewards achieved by each MM throughout the
experiment. It is important to note that pre-trained agents were not continuously trained.
Figure 3.10: Results from the direct transfer learning experiment. 50-simulation rolling
average window.
The findings offer several interesting observations. Firstly, the pre-trained DQL-MM
47

agent from the first experiment (depicted in blue) outperforms the other DQL-MM in
terms of average earnings (780 compared to 165 for the second one, as shown in Ta-
ble 3.3). Secondly, the pre-trained DQL agent from the multi-agent scenario of the second
experiment, shown in orange, also yields positive returns. While not as high as the first,
these returns come with reduced volatility, indicating a potentially less risky approach
than that of the single-agent policy. Both pre-trained DQL-MM agents exhibit strong per-
formance up until the 175-200 simulation mark. It is at this juncture that the learning
DQL-MM agent, illustrated in green, begins to show an improvement in results, akin to
observations from previous experiments. This enhancement in performance results in a
decrease in rewards for the pre-trained multi-agent DQL-MM (orange).
Additionally, post-simulation 200, the pre-trained DQL-MM single-agent (blue) dis-
plays a notable increase in the variance of its results, as highlighted in Figure 3.11. This
figure zooms in on the last 100 simulations of Figure 3.10, providing a detailed view
of this phenomenon. The performances of the Random-MM and Persistent-MM agents
remain negative, consistent with prior experiments.
Figure 3.11: Last simulations transfer learning results. 50-simulation rolling average
window.
It is crucial to point out that the learning DQL-MM did not achieve profitability on
par with its performance in the first experiment, where it was the sole RL MM. More-
over, the learning DQL-MM (green) exhibits significantly lower volatility compared to
the pre-trained DQL-MM agents, suggesting that learning agents, despite not reaching
the highest profitability, offer a less risky and more consistent strategy than relying solely
on fixed pre-trained policies, regardless of their initial e ffectiveness. Table 3.3 compiles
the average final rewards achieved by each agent.
48

Table 3.3: Direct transfer learning experiment average results (250 exp) (USDx103)
MM Agent MEAN TOP BOTTOM STD
DQL-MM single 780 10.447 -8.187 1.442
DQL-MM multi 165 5.268 -3.622 742
DQL-MM trained 121 877 -76 138
RANDOM-MM -37 15 -64 5
PERSISTENT-MM -50 -15 -90 5
In examining strategies and epsilon values, particularly during one of the five rounds
in the current experiment, the evolution of epsilons among the three competing agents
throughout the simulations is observed. Figure 3.12 distinctly showcases the emergence
of three divergent strategies, each unique to its respective agent. Both the DQL-MM
single-agent and DQL-MM multi-agent exhibit similar buy epsilon values, but their sell
epsilon strategies diverge significantly. Specifically, the DQL-MM single-agent repre-
sented in blue, opts for a less negative epsilon, indicating a preference for fewer but more
profitable sell trades. Conversely, the DQL-MM multi-agent (depicted in orange) aims
for a higher volume of sell trades, albeit with a lower reward per transaction. This reveals
that both pre-trained policies maintain a considerable degree of stability.
Figure 3.12: Evolution of epsilon values in a single experiment. 50-simulation rolling
average window.
On the other hand, the training DQL-MM agent illustrated in green, demonstrates a
significant shift in strategy from the outset, aiming to adapt to the competitive environ-
ment. It learns a distinctly different policy, even adopting positive sell epsilons, markedly
diverging from the strategies of the pre-trained agents.
This analysis leads to the conclusion that pre-trained policies exhibit greater volatility
49

in reward outcomes compared to those still in the training phase. Moreover, the introduc-
tion of new RL agents significantly influences the e ffectiveness of pre-trained policies.
Consequently, the pursuit of profitability should not focus solely on fixed, predefined
strategies but rather on the development of adaptable, responsive strategies capable of
adjusting to evolving market conditions and competitive dynamics.
3.4. Discussion
In exploring the realm of research, both experimental scenarios—operating as a singu-
lar DQL-MM agent and contending amongst multiple DQL-MM agents—demonstrate
commendable performance concerning rewards and consistency. RL MM agents exhibit
superior behavior compared to random agents, distinctly improving their profit margins
through strategic adaptations after a series of learning simulations. This adaptation be-
comes particularly pronounced in scenarios involving competition with other RL agents,
underscoring the dynamic nature of strategy adjustment in pursuit of maximal rewards
based on the information at hand.
The concept of direct transfer learning emerges as a noteworthy strategy, facilitating
the migration of successful policies into new competitive environments with promising
outcomes. This approach underscores the adaptability required in the ever-evolving land-
scape of RL market making, where pre-trained agents must continuously adjust to the in-
flux of new competitors, rendering the environment increasingly non-stationary. Despite
the initial success of pre-trained policies, their e ffectiveness is invariably tested against
the dynamism introduced by new entrants, regardless of the policy’s prior achievements.
From the perspective of risk management, pre-trained policies exhibit a higher de-
gree of volatility in average returns compared to those still undergoing learning. This
observation suggests a preference for agents that engage in ongoing learning from their
environment, rather than relying on static, pre-defined strategies. Such adaptability not
only mitigates risk but also enhances the agent’s responsiveness to market changes.
From a financial point of view, these experiments lay the groundwork for further ex-
ploration into profitable market making strategies within competitive scenarios leveraged
on RL. They call for deeper investigation, not just from the MM’s viewpoint but also from
broader market perspectives. This opens avenues for understanding how RL can be used
to optimize trading strategies, improve market liquidity, and navigate the complexities
of financial markets with a higher degree of sophistication and e fficiency. Additionally,
these experiments open a door to deep dive into profitable MM strategies in competi-
tive scenarios based on RL, not only from MM’s perspective but also from other market
approaches.
50

3.5. Contribution
The primary contributions of this foundational work include:
• Application of RL to market making: The study demonstrates the innovative
application of RL, specifically deep Q-learning (DQL), to create intelligent MM
agents in simulated stock markets. This approach allows for the exploration of how
RL can be utilized to develop strategies for providing liquidity.
• Analysis of competitive and non-competitive scenarios: One of the novel contri-
butions is the detailed analysis of RL MM agents’ behavior in both non-competitive
(single-agent) and competitive (multi-agent) scenarios. This di fferentiation pro-
vides insights into how these agents adapt their strategies based on the presence
or absence of competition, offering a comprehensive understanding of their perfor-
mance under varying market conditions.
• Direct transfer learning evaluation: The study contributes to the field by inves-
tigating the efficacy of direct transfer learning in market making. It examines how
strategies learned by RL agents in one scenario (either single-agent or multi-agent)
can be transferred to a new, competitive environment, assessing the performance
implications of such transfers.
• Framework for future research: Lastly, the research provides a robust framework
for future exploration in the application of RL to financial markets. By highlighting
the capabilities and adaptability of RL MM agents, the work paves the way for
further studies on the application of ML techniques to trading, investment strategies,
and beyond.
From a financial perspective, the experiments show that, when RL MMs interact
against simple agents, they are much more profitable than when other RL MMs partici-
pate simultaneously. It is remarkable how RL MMs adapt their strategies dynamically to
adapt to more challenging scenarios, where multiple RL agents take place. These insights
can be useful to define further profitable strategies based on ML, not only from MM per-
spective but also from a stock trading point of view. It is worth mentioning that all these
experiments are being performed in simulators. A necessary line of work is required for
these strategies to be applied in the real world. This involves first finding a way to accu-
rately simulate the asset of interest and then addressing the gap between the simulator and
the real asset. This point will also be discussed in further sections.
51

4. INVENTORY MANAGEMENT
Upon evaluating the profitability of a market making RL agent, the progression moves
to the subsequent challenge of managing inventory risk. As stated previously, inventory
management is crucial in market making. This evolution of the problem introduces a
multi-objective dimension to the task. In the field of RL, there are several strategies to
address such multi-objective problems, as presented in Subsection 2.1.4. These mainly
include reward engineering and the adoption of a genuine MORL framework.
In this thesis, both two multi-objective approaches are evaluated. Initially, a reward
engineering strategy that considers the changing situation of the MM along the trading
session is explored in Section 4.1, demonstrating superior performance compared to other
documented methods. Subsequently, a comprehensive MORL framework that leverages
PF optimization is delved into in Section 4.2. This framework not only addresses the in-
ventory risk management challenges more effectively but also surpasses the performance
of the reward engineering approach, o ffering a more sophisticated solution to the multi-
faceted problem of market making.
4.1. Reward engineering: Automated market maker inventory management with
DRL
Market making inventory management through RL is a topic that has been addressed by
some authors, as it is broadly described in Subsection 2.3.2. However, most of those
solutions rely on adding some sort of penalty term to the reward function, an action that
reduces the reward obtained at every time step according to the full inventory value or its
value variation. In some cases, this penalty is computed at the end of the trading sessions
by removing the full value of this inventory. Nevertheless, both kinds of approaches do
not take into consideration the changing conditions of the MM during the trading session,
penalizing linearly the accumulated inventory. In this regard, it can be acceptable to
have higher levels of inventory if the cash-inventory value ratio is very positive. Being
more flexible in this way allows the MM to adopt more aggressive strategies in terms of
profitability.
In this section, it is described how to design an intelligent RL MM agent that can
be profitable while managing inventory risk dynamically and adaptively, through a novel
reward function. This agent takes into account its changing situation, in terms of liquidity
(cash), adapting its policy through the trading sessions. Additionally, an in-depth analysis
of the underlying policies is conducted to understand the behavior of different risk-averse
agents. A comparison is also run against other existing reward functions to evaluate the
performance of the proposed solution.
52

To address this issue, two coefficients in the proposed reward function are defined to
modulate the inventory exposure: Alpha Inventory Impact Factor (AIIF) and Dynamic
Inventory Threshold Factor (DITF). These two coe fficients, widely described in Sub-
section 4.1.1, determine the behavior of the MM through the definition of a dynamic
inventory threshold, managing the inventory dynamically at every time step through its
contribution to the reward function. Figure 4.1 depicts an example of the coe fficients in
action.
Figure 4.1: Example of a trading session performed by a RL MM that applies the proposed
reward function with both AIIF and DITF coe fficients. In green it is shown the perfor-
mance in terms of MtM of the agent, while in blue dots it is shown how the inventory is
controlled with the red threshold line.
Regarding the organization of the remainder of the section, Subsection 4.1.1 details
the RL MM agent, including the proposed dynamic reward function. Subsection 4.1.2
describes the environment and all the details of the experimental setup. Subsection 4.1.3
analyses the results of the proposed MM, including a comparison with other existing ap-
proaches. Finally, Subsection 4.1.4 presents all the conclusions derived from this second
study.
4.1.1. New RL model for inventory management
In order to control the MM inventory, an RL agent has two main levers to interact with.
On one hand, it can increase buys or sells if it wants to increase or reduce inventory re-
spectively. Both actions can be achieved by populating more competitive buy over sell
prices, or vice versa, depending on the desired goal. With this ‘skewness’, the MM in-
ventory will be increased or decreased accordingly along the trading session due to that
imbalance. On the other hand, every agent has the option of selling stocks (or buying)
in the market at every moment. This action, usually known as hedging, allows the agent
to reduce almost instantly the desired level of inventory held. The main problem with
this alternative is that every hedging action is executed by matching a market-order. This
means that it has a cost, as every market-order has to pay the current market spread. Re-
strictive penalty terms or risk-averse policies usually impact negatively on final returns, as
agents must operate more cautiously. Generally, less restrictive penalty terms will trans-
53

late into higher and more volatile returns. Finding an equilibrium between both goals, to
earn profits and to manage risks, should be the main objective of every operator. Accord-
ing to this, non-adapting penalty terms as stated in previous works cannot be optimal by
definition. The idea behind the reward function is that MMs should be able to hold, and
thereby, manage varying amounts of inventory in response to changing conditions dur-
ing the trading session. Therefore, if a MM is operating throughout a trading session, its
situation in terms of MtM and cash/inventory value evolves as well. This changing situa-
tion should be considered to adapt the inventory holding strategy to improve profits. For
instance, the trading strategy should not be the same when having a 50%-50% cash /in-
ventory value ratio, 80%-20%, or 20%-80%. In the first case, with an 80% cash and 20%
inventory ratio, allowing the inventory to increase could be beneficial if it also increases
profits, resulting from a less restrictive policy. The opposite approach should be taken in
a 20%-80% scenario, where inventory risk should be managed more cautiously due to the
imbalance. These proportions may also change during the trading session, compelling
the MM to adapt its policy accordingly, aiming to find the best balance. This is why the
MM operating strategy should not only be a matter of keeping inventory always close to
zero units or consistently applying a linear penalty term, but rather finding a balance that
enhances profits while managing inventory risk.
In the following subsection, the incorporation of these concepts into the reward func-
tion is described. Additionally, the state and action spaces used in this work are detailed.
Finally, the training flow performed by the MM is outlined.
Reward function
Learning good policies in RL is usually tied to the design of appropriate reward functions.
Reward function engineering is, in fact, a matter of research by itself [93]–[96]. The
proposed reward function presented here aims to find the highest trading profitability in
terms of returns while controlling inventory dynamically using a specific penalty factor, as
stated previously. It is important to remark on again the dynamic nature of this approach,
as the penalty factor will adapt to available cash and inventory value at every moment.
To learn this adapting policy, a proper reward function must be designed that is capable
of being profitable while controlling risks. This involves adjusting the operations to the
operator’s risk aversion and also adapting to the changing situation of the MM.
To achieve that, the following key concepts are introduced:
Definition 1 (Dynamic Inventory Threshold Factor (DITF)) . factor that determines the
reference ratio between the value of cash and inventory, which must be respected by the
agent throughout the trading session. (Equation 4.6)
According to this term, established at the beginning of the training stage, if the goal
is for the MM agent to follow a 1:1 ratio between cash value and inventory value as a
reference, then DIT F = 1 should be assigned. This factor defines a dynamic threshold
54

(thr) throughout the trading session, a threshold that determines the maximum inventory
limit that the MM must adhere to at any given time.
Definition 2 (Alfa Inventory Impact Factor (AIIF)) . factor that modulates the agent’s
risk aversion by including a coe fficient in the penalty term of the reward function (as in
Equation 4.5)
Regarding this factor, the higher this coefficient is, the stronger the penalty the agent
will receive from holding inventories out of the allowed threshold, previously defined.
These two concepts will aid the agent in controlling risks while seeking profitabil-
ity and achieving it intelligently. It is recognized that the objectives of earning profits and
controlling inventory are often at odds, necessitating a strategy that optimizes both. While
a static reward function that simply ‘scalarizes’ both goals according to some fixed weight
could have been chosen, as is done in other works, it is crucial to note that as the MM op-
erates within a trading session, the proportion between cash and inventory value changes
according to the results of the strategy performed. Consequently, the MM might admit
more inventory in some cases than others, while maintaining an overall risk aversion ra-
tio. The two previously introduced factors assist in this task. The AIIF factor establishes a
general risk aversion threshold that is respected throughout the trading session; while the
DITF modulates the overall risks depending on the evolving cash /inventory value ratio.
These concepts are incorporated into the penalty term of the reward function.
The reward function is defined as follows:
Definition 3 (The Reward function for Inventory Management (RIM)). is a reward func-
tion R : E× PnL× HgC× Pny→ R, computed as defined in Equation 4.1,
Ri = Ei + PnLi− HgCi− Pnyi (4.1)
The different terms of the reward function are described as follows:
• (i) Ei: The trading profits obtained by the MM at time step ti result from buys or
sells. More precisely, as shown in Equation 4.2:
Ei =
n∑︂
x=0
(Bx· S prBi) +
n∑︂
x=0
(S x· S prS i) (4.2)
where Bx and S x refer to the number of stocks traded (buys or sells) by investors
with the MM, and S pr(b,s)i is the buy or sell spread quoted by the MM respectively
at that time step ti. Thereby, the higher the spread quoted by the MM, the higher
the profits earned, as previously mentioned.
• (ii) PnLi: The inventory held by the MM will gain or lose value according to mid-
price variation in every time step ti. Therefore, if the price rises the inventory value
55

will rise as well, and vice versa. This is what PnLi reward term refers to, computed
as shown in Equation 4.3:
PnLi = invi· ∆Pri (4.3)
where invi is the quantity of stock held by the MM (positive or negative) at ti, and
∆Pri the difference between current and previous stock prices: ∆Pri = Pri− Pri−1.
• (iii) HgCi: The MM has the option to reduce its inventory instantly by buying or
selling it at every time step. When doing this, it pays a hedging cost as a penalty, as
it is executed through a market-order. Hedging costs HgCi are equal to the amount
of inventory hedged multiplied by the market spread S preadmkt. It is computed as
shown in Equation 4.4:
HgCi = Hgi· S preadmkt (4.4)
where Hgi is the amount of inventory hedged, and S preadmkt is the current market
spread, at ti.
• (iv) Pnyi: The last term concerns the penalty for holding inventory. This term is
especially relevant in this approach as it drives the policy according to the inven-
tory risk. As introduced previously, MMs should carry the least amount of inven-
tory possible, in accordance with their liquidity situation, to mitigate risks caused
by price volatility. To achieve this, it is necessary to establish some restriction or
penalty that discourages the agent from accumulating inventory during the trading
session. Particularly, a dynamic term has been opted for, which can adapt to the
MM inventory and cash values at every moment. This term, Pnyi, impacts the re-
ward as it penalizes the inventory that the MM holds outside of a specific range.
This range, or threshold, is not a fixed value but is dynamically adjusted taking into
account the desired proportion between the MM’s cash value (liquidity) and the
average value of the inventory held in the last n steps.
Hence, the penalty term is defined as in Equation 4.5:
Pnyi = AIIF· min{|Ri|,|Ri· invi
thri
|} (4.5)
where:
thri = DIT F·
⃓⃓⃓ cashi 1
n
∑︁t
x=t−n midi
⃓⃓⃓ (4.6)
thri = 1 n
t∑︂
t−n
thrx (4.7)
invi = 1 n
t∑︂
t−n
invx (4.8)
The dynamic threshold thri (Equation 4.6) is calculated by dividing the MM cash
value at ti by the average of the last n stock mid-prices midi. The resultant value is
56

multiplied by DIT F, the Dynamic Inventory Threshold Factor. This factor defines
the proportion between cash and inventory value mentioned above. This proportion
is between the cash value at ti and the average inventory held in the last n time
steps. An average value is used instead of the spot value to reduce the impact of
price volatility and to stabilize convergence. The whole penalty is modulated using
the first coefficient AIIF , our Alpha Inventory Impact Factor.
According to Equation 4.5, it is important to remark that this penalty term behaves
as a piecewise function, where this penalty increases linearly frominvi = 0 until the
dynamic threshold thri is reached. The idea behind this is to have a smooth penalty
term that discourages proportionally the accumulation of inventory.
In the experimental Figure 4.1.2 the impact of the AIIF factor on profitability, in-
ventory management, and policies is described.
State and action spaces
As with every RL problem definition, some key elements have to be defined apart from
the reward function. On one hand, the agent must have a good understanding of the envi-
ronment. This is achieved by defining a proper state space that contains enough valuable
information to select the best possible actions at every time step. On the other hand, it
is necessary to determine the action space, hence, all the actions that can be performed
by the agent. State and action spaces have been designed based on the previous work of
Ganesh et al. [88], with some adaptations such as the action space’s discretization. All
these elements are detailed as follows.
States: The observation state of our agent consists of 8 features: (i) the number of
stocks bought in the previous time step, (ii) the number of stocks sold in the previous
time step, (iii) the current inventory size (positive or negative), (iv) the inventory size in
the previous step, (v) the stock mid-price variation between current and previous time
step ( ∆Pri = Pri− Pri−1), (vi) the current reference bid-ask spread, (vii) the bid-ask
spread in previous time step, and (viii) the total amount of stock traded ( Vi), known as
volume, by the MM in previous time step. The state space was reduced compared to the
previous section because it was observed that the agent’s performance improved with this
reduction. Other space states have been also tested, such as more reduced space states,
with worse results.
Actions: Following the approach outlined in the previous section, the proposed MM
agent has three possible actions to execute. First, it can quote a buy price and /or a sell
price. These prices, related to the current market spread, will determine how many oper-
ations are matched and how much trading profits the agent will earn. In addition, it can
decide how many inventory units are hedged through a market-order. To perform these
actions there are three variables that MMs can interact with in every time step ti: (i) buy
spread Bs i , (ii) sell spread S s i , and (iii) amount of inventory hedged Hs i . With these three
variables, a discrete action space has been defined.
57

Hence, buy and sell actions will consist of picking oneη in the following list of evenly
distributed values respectively:η(b,s)i ∈{− 1,−0.8,−0.6,..., 0.6, 0.8, 1}.
Therefore, streamed buy/sell spreads (prices) correspond to Equation 4.9:
Bi Sp, S i Sp = S preadmkt· (1 +η(b,s)i) (4.9)
where S preadmkt is the current price spread streamed by the market, and BiSp, S iSp are
the spread that MM quotes at time ti. Both buy and sell η(b,s)i can be equal or di fferent,
incurring in asymmetry in the latter case. This asymmetry, also known as skewness,
allows MM to balance between buys and sells if needed.
In addition, to buy or sell actions, hedging action will consist of picking another η
from the list ηhi ∈ {0, 0.25, 0.5, 0.75, 1}. Depending on the specific ηhi selected by the
agent, its inventory will be reduced proportionally by 0% to 100% in the following time
step ti+1. Thereby, as shown in Equation 4.10:
invi+1 = invi·ηhi (4.10)
Where invi is the inventory held by the MM at ti. Hedging action is not free, as it will
incur specific costs as described in Subsection 4.1.1.
In conclusion, the action space consists of 11 buy× 11 sell× 5 hedgeη, represented
by the tuple ai = (ηbi,η si,η hi). This solution was chosen over a continuous action space to
increase the convergence rate while sacrificing a more concrete value, which is not con-
sidered necessary for this exercise. Additionally, using relative values instead of absolute
figures helps the agent to generalize better if the domain values change. For example,
having at ti a market spread of S pit = 7, an inventory of invi = 150 units, and the fol-
lowingη returned by the agent ai = (0.8,−0.2, 0.5), the MM would stream the following
values: BSp i = 7× 0.8 = 5.6, and S Sp i = 7×− 0.2 = 1.4. Additionally, inventory would
be reduced to invi+1 = invi− 75 = 75 units, regardless of inventory increases or decreases
due to the rest of trading operations.
Market maker’s training algorithm
The training flow follows the same process as presented in Algorithm 2, in the previous
section. The only di fference is that, in this work, two neural networks are used instead
of one to enhance stability during the learning phase. In this setup, after completing
the training stage (line 20), the neural network used for training is copied to the target
network. This target network is then utilized by the algorithm to select actions.
4.1.2. Experimental setting and methods
Due to the continuous state space, and the non-episodic nature of our approach, a Deep
Q-Network for the MM agent has been used. As introduced in previous sections, the
58

Q-function Q(s,a) is approximated by a DQN, by using a fully connected network. In
fact two, instead of one, identical NNs are used: a training NN and a target NN. This
improves the stabilization in the learning stage [17]. These NNs have been defined with
a total of 8 state space variables in the input layer and 605 possible actions in the output
layer. Furthermore, and similarly to the previous section, the agent’s network has 3 hidden
layers with 32 neurons in each one. The input and the three hidden layers have ReLu as
the activation function. The output layer uses a linear activation function. For every
given state the NN approximates the reward of every action, selecting the action with the
best-expected reward. Epsilon-greedy is, again, the exploration strategy. Other network
architectures have also been tested, such as 3× 32, 3× 64, and 5× 64 (layers× neurons).
Regarding the training stage, the NN is fitted every 200 time steps. Experience
replay is used to improve the training. According to this, all the experiences tuples
ei = (si, ai, ri, si+1) are stored in a replay-bu ffer of 1M size. Every epoch, the training
NN takes mini-batches of 1.024 random experiences from this replay-bu ffer fitting the
weights using back-propagation. Adam has been chosen as the learning optimizer and
MAE as the loss metric. The learning rate is set to lr = 0.01. The discount factor has
been set toγ = 0.6. These hyperparameters have been selected after testing other alterna-
tive values.
Regarding the trading environment, there are three types of experimental MMs com-
peting with each other in every simulation, as follows:
• 1 DQN market maker(DQN MM): The deep Q-learning intelligent MM proposed
in this approach.
• 1 Random market maker (Random MM), a MM with uniform random spreads
and hedges on every time step. Same action space as DQN.
• 1 Persistent market maker (Persistent MM), a MM with fixed uniform random
spread and hedges over every simulation. The spreads and hedges are selected at
the beginning of each simulation and kept until the simulation is finished. Same
action space as DQN.
In this work, an attempt was made to generate a ‘standard’ market in ABIDES in
terms of price volatility. With this setup, the goal was to achieve credible price move-
ments, while maintaining the stochastic essence of every trading environment. According
to this, the market simulation configuration in which the experiments were conducted
included the following participants/setup: 100 noise agents, 10 value agents, 10 Momen-
tum agents, 1 adaptive POV agent, and 1 exchange agent. The market generated from the
interaction of these agents has enough liquidity to allow for di fferent spreads along the
simulations. Additionally, the returns are reasonable and the price movements are suitable
for a standard financial market. To illustrate these points, Figs.4.2 and 4.3 show different
price trajectories and returns respectively across full experiments.
59

Figure 4.2: Mid-prices evolution sample. This figure illustrates how the price changes
along a random sample of different simulations, showing the stochastic nature of ABIDES
simulator.
Figure 4.3: Histogram of returns. The plot shows the returns (price variations) distribution
at the end of all simulations. Rett = (Pricet/Price0)− 1.
All these agents interact for two hours, determining a trading session. This interaction
defines the movement of the stock price, its volatility, and also the reference market spread
S p. In addition to these agents, 50 investor agents interact solely with the MMs. These
investor agents place random buy or sell orders with a fixed size. As greedy investors,
they always choose the MM with the narrowest spread available in the OB, hence the
60

cheapest one. If there were many MM with the same cheapest BiSp or S iSp, the investor
would pick one of them randomly.
As mentioned above, every training /testing simulation is based on a 2-hour market
session (9:30h to 11:30h). One DQN MM agent, one Random MM, and one Persistent
MM are included. Full experiments have a total of 150 independent simulations (trading
sessions), with 5 total experiments per setup. No trading costs have been considered.
Asset prices evolve stochastically according to agents’ natural interaction. All simulations
begin with an opening price of $1.000,00. The experiment results are evaluated in terms
of the total MtM and cash/inventory value ratios at the end of the trading sessions.
Experimental evaluation
In this subsection, all the experiments are described, from the agent training to the com-
parison with other existing reward functions. Initially, to evaluate the impact of di fferent
penalty factors, the DQN MM is trained with 10 di fferent setups. This phase provides
an initial idea of the learning and performance of the di fferent MM setups. Once these
DQN MM are trained, they are tested in new fresh environments. The test results are then
analyzed in terms of profitability, inventory management, and cash /inventory value ratio
as the main metrics. Furthermore, the policies performed by the DQN in all the testing
environments are inspected. Finally, to compare the proposed solution against other ex-
isting approaches, additional experiments are set up in which these reward functions are
evaluated, demonstrating how the proposed solution is capable of generating better MM
policies.
Training the market maker
Our DQN MM competes against two additional MMs in the trading sessions: one ran-
dom agent, and one persistent agent. To evaluate the DQN MM performance in terms of
profitability and inventory risk management, multiple training setups have been launched
applying di fferent Alpha Inventory Impact Factors (AIIF). A total of 10 di fferent AI-
IFs have been tested. Starting from AIIF = 0, where no inventory penalty is applied
to the reward function, up to AIIF = 100 where inventory impact is severe. There-
fore, AIIF = {0, 0.2, 0.5, 0.8, 1, 1.5, 2, 5, 10, 100}. In addition, the Dynamic Inventory
Threshold Factor DITF, has been established in this experimentation with a fixed value
of DIT F = 0.5. This value was chosen because it is considered feasible to keep the
inventory value below 25% of the total MtM at any time. All MMs start with cash of
$100,000.00 and 0 units of asset inventory. A total of approximately 612K gradient steps
have been performed per single experiment.
The first training results (with AIIF = 0) show very good performance in terms of
MtM, finding a more profitable policy than random and persistent MMs (Figure 4.4).
These two non-intelligent MM, in fact, end with lower MtM even than at the starting
61

point. Regarding alpha coe fficients (AIIF), and taking a closer look at Figure 4.5 where
the different values of AIIF are represented, it is remarkable to see how the slopes of the
MtM curves moderate as long as the AIIF factor increases.
Figure 4.4: Single training experiment, applying an AIIF = 0 in the reward function. The
three competing agents are shown. It is noted how the DQN MM agent can learn along
simulations how to be profitable, compared to the other two random agents.
62

Figure 4.5: DQN MM training results applying different AIIF . It is noticeable how MtM
return reduces as long as the AIIF factor is increased. This e ffect has to do with the
control of inventory. (Random and Persistent agents are not shown).
Testing the policies
Once the agents have been trained using different AIIF factors, they are all tested on new
experiments. At first sight, they perform well in terms of profitability with almost all small
AIIFs (Figure 4.6). As long as alpha is increased, profitability is impacted. However, the
inventory is controlled as well, as expected (Figure 4.7).
63

Figure 4.6: DQN MM testing rounds, with different AIIF factors. Higher profits are linked
to lower AIIF factors, as inventory control is more relaxed.
Figure 4.7: DQN MM testing’s rounds inventories, applying di fferent AIIF factors. In
general terms, as long as the AIIF factors are increased, inventories are reduced as well,
due to the controlling effect that this factor has on them.
64

Analyzing inventory distributions (Figure 4.8), it is clear that as soon as the AIIF
penalty factor increases the inventory also shrinks. Therefore, the distributions get nar-
rower according to this coefficient as expected.
Figure 4.8: DQN MM inventory distributions along di fferent experiments. This Figure
illustrates the different inventories held by every agent during the testing stage, according
to their different AIIF factors.
But not only the AIIF factor plays a key role in managing the inventory risk. This
management is also related to Dynamic Inventory Threshold Factor (DITF). This factor,
which is established in this research to a value of 0.5, defines the proportion between cash
and inventory value along the experiments. In Figures 4.9, 4.10, and 4.11 can be noticed
how this threshold (in red) adapts dynamically along them according to the different AIIF
factors, based only on the cash held by the MM at every moment, and the inventory value.
Here three examples are shown,AIIF = 0 (no penalty), AIIF = 1, and AIIF = 5. As long
as the AIIF factor is increased, inventories are kept more strictly inside the thresholds.
Note that y-axis ranges of Figures 4.9, 4.10 and 4.11 have been adjusted independently
for the sake of legibility. Additional AIIF factors tested are shown in Appendix A.1.
65

Figure 4.9: DQN MM instant inventories held and thresholds along the testing experiment
every time step. Due to the lowest restrictive alpha factor applied ( AIIF = 0), noisy
inventory thresholds and big variances in inventories are noted.
Figure 4.10: DQN MM inventories and thresholds along the experiment with AIIF = 1.
More stable thresholds are shown compared to the lower AIIFs of the previous Figure 4.9.
In addition, the inventories are also more constrained.
Figure 4.11: DQN MM inventories and thresholds along the experiment with AIIF = 5.
Here, extremely stable and low thresholds with very constrained inventories inside these
thresholds. For the sake of legibility, y-axis ranges in Figures 4.9, 4.10 and 4.11 have
been adjusted.
Finally, it has been explained that the dynamic threshold is calculated with the value
of the inventory at every time. In this sense, the discussion revolves around cash/inventory
value ratios, as it is the main driver of the penalty term. Regarding this point, Table 4.1
presents average ratios per experiment. Once again, it can be observed how increasing
the AIIF factor directly impacts this ratio, thereby improving this value. This is very
reasonable, as the agent is constantly managing the trade-o ff between profitability and
66

inventory value. Hence, the higher the AIIF factor, the higher the cash /inventory value
ratio returned.
Table 4.1: DQN cash/inventory average ratio and benchmarks.
DQN MM Random MM Persistent MM
Experiment Avg 1 σ2 Avg1 σ2 Avg1 σ2
AIIF = 0 1 , 08 0 , 12 1 , 31 0 , 31 1 , 44 1 , 18
AIIF = 0, 2 1 , 18 0 , 06 1 0 , 3 1 , 24 0 , 96
AIIF = 0, 5 1 , 01 0 , 15 1 , 34 0 , 23 1 , 59 0 , 95
AIIF = 0, 8 1 , 32 0 , 38 1 , 33 0 , 29 2 , 22 2 , 36
AIIF = 1 1 , 48 0 , 65 1 , 22 0 , 31 1 , 29 0 , 71
AIIF = 1, 5 1 , 39 0 , 21 1 , 05 0 , 34 1 , 31 1 , 32
AIIF = 2 3 , 06 16 , 55 1 , 2 0 , 28 1 , 3 0 , 69
AIIF = 5 11 , 62 90 , 3 1 , 23 0 , 29 1 , 28 0 , 43
AIIF = 10 7 , 96 24 , 42 1 , 27 0 , 29 1 , 18 0 , 45
AIIF = 100 59 , 34 413 , 12 1, 21 0 , 28 1 , 22 0 , 44
Note: Table with the average ratio between the cash of the MM and the value of the inventory held
at every experiment. It is noticeable that as long as the AIIF factor is increased, so is the cash over the
inventory value. Every experiment corresponds to different Alpha factors (AIIF).
aAverage cash/inventory ratio per experiment.
bCash/inventory ratio standard deviation per experiment.
Qualitative analysis of the generated policies
As formerly detailed, DQN agent behavior relies on a NN that returns the best action for
each state. On many occasions, NNs are considered “black boxes”, as they su ffer from a
certain lack of interpretability. To have a better understanding of the experimental results
and the policies followed by the different MMs, the analysis delves into the different buy,
sell, and hedging spreads performed in the various experiments.
Regarding buy and sell strategies, as shown in Figure 4.12, it is noticeable how both
η(b,s) move from negative to positive values as long as the AIIF rises. This suggests that
with smaller or negative η(b,s) the MM is more aggressive in terms of prices (narrower
spread), being able to capture a higher number of trades. Furthermore, it is also remark-
able how strategies evolve not only in terms of negative or positive values but increasing
the distance between buy and sellη(b,s) (as it happens aroundAIIF = 0.5 and AIIF = 1.5).
Thus, different approaches and behaviors are found by the MM.
67

Figure 4.12: DQN MM buy and sell strategy distributions, in terms of prices, according
to different AIIF. The higherηs, the more expensive the price streamed by the MM.ηh=0
represents the same price as the last market spread. With high AIIF factors, higher spreads
are streamed by the MM.
Regarding the hedging strategies (Figure 4.13), it is noticed that as long as the inven-
tory penalty increases so does hedging ηh. This increase makes MM keep low inventory
despite losing profitability due to hedging costs. Thereby, buy/sellη(b,s) adaptive strategies
combined with different hedging actionsηh compose the unique learned policies.
68

Figure 4.13: DQN MM hedge strategy distributions according to different AIIF.ηh repre-
sents the amount of inventory the MM is reducing instantly by buying or selling at market
price in a specific time step. This ‘urgency’ has an extra cost. It is remarkable how higher
hedgesηh are performed as long as the alfa factor is increased.
Taking a look at the average status of the MMs (Figures 4.14 and 4.15), it is remark-
able how higher AIIFs can even finish with less value in terms of MtM than the starting
value. Focusing on AIIF = 5, although the inventory position ends in a very constrained
situation, it can be seen how the experiment finishes below the starting MtM reference
line. So, according to this, it is very important to be aware of the impact of increasing
AIIF factor on the overall performance. All the details regarding the MtM can be found
in Table 4.2.
69

Figure 4.14: DQN single inventory and MtM per AIIF results are obtained from every test
experiment. Each point represents the average MtM and Inventory of the MM of every
testing simulation (150 simulations x 10 alphas ). As noticed, the dispersion is higher
with lower AIIF factors.
Figure 4.15: DQN inventory and MtM in average per AIIF are obtained from every test
experiment(grouped by alpha). Here it can be noticed the inverse correlation between
MtM+inventory and AIIF factors. In addition, it clearly shows the competing nature of
both goals: to reduce the inventory while increasing the MtM.
70

Table 4.2: DQN Mark-to-Market experiment results (x103) and baseline agents.
DQN MM Random MM Persistent MM
Experiment Avg 1 σ2 Var3 Avg1 σ2 Var3 Avg1 σ2 Var3
AIIF = 0 12 .399 48 24,50% 9 .711 10 -2,98% 9 .648 13 -3,35%
AIIF = 0.2 12 .833 66 28,05% 9.559 7 -4,30% 9 .575 14 -4,45%
AIIF = 0.5 11 .688 122 15,27% 9 .957 39 -0,33% 9 .889 17 -0,71%
AIIF = 0.8 10 .358 23 3,69% 9 .823 9 -1,96% 9 .884 14 -1,26%
AIIF = 1 10176 7 1,72% 9 .889 9 -0,94% 9 .900 9 -0,88%
AIIF = 1.5 10 .501 24 5,60% 9 .775 12 -2,71% 9 .811 13 -1,76%
AIIF = 2 10 .081 12 0,85% 9 .944 13 -0,47% 9 .922 13 -0,81%
AIIF = 5 9 .984 3 -0,18% 10 .064 16 0,69% 10 .038 13 0,37%
AIIF = 10 10 .061 6 0,57% 9 .969 7 -0,36% 9 .998 9 0,15%
AIIF = 100 10 .008 1 0,11% 10 .019 15 0,04% 10 .048 11 0,41%
Note: Table with all the MtM values along different testing experiments. Every experiment corresponds
to different Alpha factors (AIIF). Starting MtM = 10.000 (x103)
aAverage MtM along the experiment.
bMtM standard deviation along the experiment.
cMtM increase/decrease at end of the experiment (return).
Finally, aiming to fully understand the policies behind actions, it is relevant to analyze
how the AIIF factor impacts the number of stocks traded by the DQN MM. Taking into
account that higher AIIFs usually rely on higher buy and sellη(b,s) as stated before, it may
be expected that the number of operations performed by the MM could decrease as long
as the AIIF factor increases. In Figure 4.16, it can be appreciated that this intuition is ac-
curate and especially relevant with higher AIIFs. In summary, and with all these insights
raised, it can be said that, as long as the AIIFs increase, the MM becomes more selective
with actions performed, preferring higher spreads and increasing the use of hedging.
71

Figure 4.16: Buy and sell amount of stock traded according to di fferent AIIF. As long as
the AIIF factor is increased, the number of executed operations is reduced. This has to do
with the increase of buy and sell η(b,s) shown in Figure 4.12, a point that makes the MM
to be less competitive in terms of price, capturing fewer orders from the investors.
Comparison with existing reward functions
To test the robustness of the approach, it is important to perform a benchmark with other
reward functions. Accordingly, different and recent works [71], [78], already introduced
in Subsection 2.3.2, have been selected. These three di fferent works represent common
MM RL approaches, as they focus on different metrics to define the reward of their agents.
To do a ‘fair’ comparison among methods, only their respective reward functions have
been used, while preserving the rest of the parameters as similar as possible. Therefore,
every agent shares the same state and action space, the same DQN architecture, and the
same hedging policy, as presented before in Subsection 4.1.2. The rest of the experimental
settings (environment agents, episode lengths, random competing agents, etc.) have been
preserved as well.
Hence, a total of 4 different reward functions have been compared:
• Full inventory penalty: Inspired in [78] 3, this reward function includes a penalty
term related to the absolute amount of inventory held by the MM at every time step,
multiplied by a risk aversion coefficient, as shown in Equation 4.11:
3Rt+1 = (Qask t - Mt+1)1Qask t exe + (Mt+1 - Qbid t )1{Qbid t exe}−λ|It+1|
72

Ri = Ei−λ∗| invi|− HgCi (4.11)
λ has been set toλ = 0.15, following the experimental setup of the mentioned work.
• Asymmetrically dampened PnL: Based on [71]4, this reward function includes a
penalty term that penalizes the incomes coming from Inventory value increases. It
is modulated by a scale factorη, as shown in Equation 4.12:
Ri = Ei + PnLi− max(0,η· PnLi)− HgCi (4.12)
η has been initially set toη = 0.1 as shown in the respective work.
• PnL: No inventory penalty term is included. This is a common approach in many
works as introduced in Subsection 2.3.2. Here, only the profits derived from trades
are considered, apart from hedging costs, as shown in Equation 4.13:
Ri = Ei− HgCi (4.13)
• RIM (Our reward function, Equation 4.1): For the sake of comparison, di fferent
AIIFs have been included: AIIF ∈{ 0.2, 0.5, 0.8, 1}.
Seven different DQN agents were trained independently, based on the described re-
ward functions. The training process is shown in Figure 4.17. Examining the results of
the testing stage in Figure 4.18 and Table 4.3, it can be seen that the reward function
with AIIF = 0.2 was the most profitable during the 150 tested trading sessions, followed
by the Asymmetrically dampened reward function and the reward function with AIIF =
0.5. These two last cases obtain almost the same profitability. With higher AIIF values
(α = 0.8 andα = 1), MtM decreases, as stated earlier, due to inventory control.
4ri =ψ(ti) - max(0,η· Inv(ti)△m(ti))
73

Figure 4.17: Benchmark results in terms of MtM(cash+ inventory value). Training stage.
Four different reward functions are compared: Full Inv 4.11, Asym Damp 4.12, PnL 4.13,
and our reward function RIM 4.1( alpha). Di fferent AIIF factors (α) have been included
for our reward function.
These agents had stable returns during the test experiments, as shown in Figure 4.18.
However, the agent with the PnL reward function performed much worse in both MtM
and inventory management, indicating that inventory metrics should be included in the
reward function to design better market making agents.
74

Figure 4.18: Benchmark results in terms of MtM(cash + inventory value). Testing stage.
Four different reward functions are compared: Full Inv 4.11, Asym Damp 4.12, PnL 4.13,
and our reward function RIM 4.1( alpha). Di fferent AIIF factors (α) have been included
for our reward function.
Table 4.3: Benchmark results. MtM, inventory, and cash/inventory ratio are presented.
Mark-To-Market Inventory Cash /Inv.Value ratio
Experiment Avg 1 σ2 Var 3 Avg1 σ2 Avg1 σ2
AsymDamp 11.672 162 17 , 27% 2 .975 288 1 , 08 0 , 25
FullInv 10.107 27 1 , 02% −32 14 1 , 15 0 , 19
PnL 8.338 1 .048 −0, 53% 16 .569 1 .882 1 , 03 0 , 14
AIIF = 0.2 12 .833 66 28 , 05% −183 35 1 , 18 0 , 06
AIIF = 0.5 11 .688 122 15 , 27% 199 31 1 , 01 0 , 15
AIIF = 0.8 10 .358 23 3 , 69% −40 9 1 , 32 0 , 38
AIIF = 1 10.176 7 1 , 72% −8 4 1 , 47 0 , 64
Note: Table with the results of the di fferent reward functions tested, in terms of MtM, inventory, and
cash/inventory value ratio.
aAverage value along the experiment.
bStandard deviation along the experiment.
cMtM increase/decrease at end of the experiment (return).
Regarding inventory management, and observing Figure 4.19, it is noted how our re-
75

ward function performed well in all cases. TheFull inventory penaltyreward function also
performed well, despite lower returns. However, the Asymmetrically dampened PnL and
PnL reward functions perform poorly in managing inventory, as shown in the distribution
dispersion.
Figure 4.19: Benchmark results in terms of Inventory distribution. This Figure illustrates
the different inventories held by every agent during the testing stage, according to their
different reward functions. Four di fferent reward functions are compared: Full Inv 4.11,
Asym Damp 4.12, PnL 4.13 and our reward function RIM 4.1 (alphas).
As an overall conclusion of this benchmark, it can be observed that our reward func-
tion allows the MM to perform better in terms of MtM, and also, in terms of inventory
management than the rest of the tested functions. The average ratio figures between the
cash and the inventory value presented in Table 4.3 also illustrate how our MMs can man-
age these proportions properly. Furthermore, from the obtained results, it can be affirmed
that including some kind of penalty term in the reward function helps to improve the prof-
itability of the agent while constraining the inventory risks. In fact, those reward functions
that are based only on PnL, ignoring inventory, can lead to the design of ine ffective and
also unstable agents.
4.1.3. Discussion
Achieving different goals in a multi-objective environment is not always easy. Market
making can be clearly considered a multi-objective task. The presented results (Table
4.3) demonstrate that the proposed agent and reward function can deal with this, adapting
properly to the changing environment while seeking the two main objectives:
• To be profitable, as shown in the results. In this sense, the MtM average results show
that our agent obtains good returns and performs better than most of the previous
ones, except for AsymDamp.
• To keep inventory controlled, as evidenced by comparing the average inventory
returns with those of PnL and AsymDamp alternatives.
76

As a limitation of this method, it can be remarked that one pre-trained agent per con-
figuration is required before going live. Defining a scalarized reward function, as done in
this work, requires prior knowledge of the future utility function. If the utility function
changes a posteriori, pre-trained agents that can adapt to it are needed.
Conversely, RL enables the definition of agents by specifying the reward function.
This means it always seeks the best policy, regardless of system complexity. This is a
noteworthy advantage in stochastic and dynamic environments such as stock markets,
where rule-based agents would require continuous calibrations and adaptations.
As the main conclusions of this first way of controlling inventory, a robust approach
for learning a market making agent based on RL has been presented, where the agent can
modulate its inventory automatically according to a desired liquidity ratio. A reward func-
tion has been introduced that, when combined with the DQN algorithm, can modulate the
inventory while seeking profitability and adapting to the evolving liquidity of the agent.
This reward function has two key factors that allow the agent to control the inventory
risk dynamically while looking for profitability. First, the AIIF factor modulates the risk
aversion related to inventory risk by serving as a penalty term. Additionally, the DITF
factor can dynamically adjust the behavior of the agent as it adapts to the cash /inventory
value held at every time. These two terms combined enable the MM to control its risks
dynamically while adhering to the initial risk aversion strategy. Therefore, the MM will
not follow a static policy driven by a standard scalarized multi-objective reward function.
Rather, it will adapt to the market based on its holdings of cash and inventory.
The MM agent has been tested with di fferent penalty factors to evaluate the perfor-
mance of these parameters in a simulated but realistic environment and has also been com-
pared to random baseline agents. Experimental results show that the presented approach
allows for the design of an RL MM that, with only two liquidity parameters, e fficiently
modulates its operations.
Additionally, not only has this intelligent agent been designed, but the underlying
strategies followed by the MM in terms of price and hedge spreads (actions) have also
been understood and evaluated. This analysis has been conducted taking into account
different penalty coe fficients, obtaining valuable insights about the trading operative in
terms of pricing, inventory hedging, and inventory dynamic thresholds. This analysis
allows delving into the reasoning behind the learned strategies, without leaving the agent
to operate as a “black box”.
Last but not least, the proposed solution has been compared with other existing re-
ward functions, concluding that our function can achieve good returns while managing
inventory risk in a more robust way than the alternative tested approaches.
Regarding future work, some aspects can also be explored and even improved. The
main aspect found relevant is related to the selection of a proper AIIF factor. With the
current proposal, this coe fficient is predetermined and does not consider the changing
market conditions over time. It is well known that market volatility evolves, even for
77

the same asset, behaving differently depending on the hour of the day, the arrival of new
economic data, or some other events. Including a volatility parameter that modulates this
AIIF coefficient according to the market ‘texture’ at every time could be a good upgrade
of the reward function.
4.1.4. Contribution
This work makes several important contributions to the field of automated market making
strategies using DRL. There is a special focus on inventory control through a dynamic
reward function.
These contributions are outlined as follows:
1. Adaptive reward function: Development of an innovative adaptive reward func-
tion that adjusts to changes in market conditions and the agent’s inventory status,
enhancing the traditional static reward functions typically used in market making.
2. Control coefficients for dynamic inventory management: Introduction of two
novel control coefficients, Alpha Inventory Impact Factor (AIIF) and Dynamic In-
ventory Threshold Factor (DITF), which enable dynamic adjustments to the MM’s
behavior based on real-time liquidity and cash-inventory ratio conditions.
3. In-depth strategy analysis: Comprehensive analysis of the strategies employed
by RL agents, focusing on their impact on profitability and inventory management
under various market conditions.
4. Comparative evaluation of reward functions: Detailed comparative study of the
new reward function against existing methodologies, demonstrating the advantages
of the proposed approach in real trading environments.
These contributions collectively advance the field of market making, providing signif-
icant theoretical and practical insights that help bridge the gap between academic research
and industry application.
4.2. MORL with Pareto fronts
Once the first multi-objective reward-engineered strategy was developed and its pros and
cons analyzed, an evolution of the method is presented. In this regard, a strict MORL
alternative is developed. Aiming to surpass the main problems of the reward-engineered
approach, such as the trial-and-error iterative design process and the need to engineer both
subgoals into a single complex function, a MORL alternative comes into play. As already
introduced, the market making problem involves addressing two main objectives: (i) in-
creasing MM profitability and (ii) maintaining low inventory levels to mitigate devalua-
tion risks. To tackle these challenges, the integration of a multi-objective framework with
78

PFs and DRL for addressing the MM problem is proposed. This approach is capable of
specializing in both subgoals without introducing design biases, keeping the process more
straightforward. To demonstrate the robustness of the MORL solution, a comparison with
other classical reward engineering market making alternatives is presented, illustrating
the strengths and weaknesses of all of them.
The following subsections describe the entire process: First, in Subsection 4.2.1, the
foundation of the agent is defined, starting with a brief review of the technique, the agent
architecture, the algorithm used by the agent, and the metrics that will be used to deter-
mine the performance of the agent. After that, the setup of the experiments is detailed in
Subsection 4.2.2. Then, the results of the experiments are presented in Subsection 4.2.3.
Subsection 4.2.4 provides an analysis of the impact of including trend information in the
presented agent. This is followed by the discussion in Subsection 4.2.5 and the contribu-
tions in Subsection 4.2.6.
4.2.1. Multi-objetive RL MM: M3ORL
The contribution of this section is twofold: i) the novel modeling of MMs as RL multi-
objective agents with two distinct goals: maximizing profitability while minimizing in-
ventory, and ii) the comparison of these agents with other MMs that utilize traditional re-
ward engineering techniques. Consequently, a MM agent based on MORL called M3ORL
is developed, leveraging the advantages of this approach. PFs have been widely employed
in solving diverse multi-objective problems [31], including those in the market making
domain [32]. The utilization of PFs o ffers numerous benefits in handling multi-objective
problems, which have been previously discussed in detail in Subsection 2.1.4.
Market maker as an MOMDP
As part of the RL framework, the main characteristics of the RL agent as an MOMDP
need to be defined. This includes specifying the state and action spaces, designing the
reward function, and determining the agent’s architecture. The design of the state and
action spaces has been based on the previous section.
Space state: The agent’s observation state comprises eight distinct features, the same
as in the previous Section 4.1 due to the good performance achieved by this configu-
ration. These include (i) the number of stocks purchased in the previous time step,
(ii) the number of stocks sold in the previous time step, (iii) the current inventory size
(which may be either positive or negative), (iv) the inventory size from the previous step,
(v) the di fference in the stock mid-price between the current and previous time steps
(∆Pricei = Pricei− Pricei−1), (vi) the current reference bid-ask spread, (vii) the bid-ask
spread from the previous time step, and (viii) the total volume of stock traded (Voli) by the
MM in the previous time step. Other state representations have also been experimented
with, including more simplified versions, but these have yielded worse results.
79

One relevant element not considered in this dissertation is trend information. Upward
and downward trends are situations where markets stabilize over certain, yet undeter-
mined, periods. Indeed, many strategies rely on this aspect [97]–[99]. Deep analysis
has been performed regarding this topic in Subsection 4.2.4, where trend information is
incorporated into the agent’s state space to evaluate the impact of including this type of
information.
Action space: As previously, the MM agent has three possible actions: quote a buy
price, quote a sell price, and decide how many inventory units to hedge through a market
order. The agent can interact with three variables in every time step ti: (i) buy spread
S prBuy i , (ii) sell spreadS prS ell i , and (iii) amount of inventory hedgedHgi, to perform these
actions. A discrete action space is defined, where buy and sell actions consist of selecting
oneη from a list of evenly distributed values η(b,s)i ∈{− 1,−0.8,−0.6,..., 0.6, 0.8, 1}, and
hedging action consists of selecting anotherη fromηhi∈{ 0, 0.25, 0.5, 0.75, 1}. Therefore,
the complete action space consists of 11 buy × 11 sell× 5 hedge η, represented by the
tuple ai = (ηbi,η si,η hi). When selecting an action, and due to the multi-objective nature
of the solution, the best action will be selected based on a utility coe fficient w. This
coefficient, presented in Figure 4.20 and detailed in the following subsection, balances the
action that aims to optimize the first objective (MtM) with the second objective (inventory
control). Its value, therefore, depends on the a priori utility function imposed by the
operator. It should be noted that no trading costs were considered in our study, and the
asset prices evolved stochastically based on agents’ natural interaction.
80

Figure 4.20: MM DQN architecture and reward function. The MM DQN architecture in-
cludes separate blocks of NNs (train+target) to handle each subgoal independently. These
networks compute the Q-function for both the MtM and Inventory subgoals. The weight
parameter, denoted as ’w’, is used to balance the importance of MtM and Inventory in the
overall reward function.
Reward functions: Considering two di fferent objectives, and following the MORL
framework introduced previously, two reward functions are taken into account. Therefore,
the agent will receive a vector as shown in Equation 4.14 at each learning step.
R⃗(s, a) = (R1(s, a), R2(s, a)) (4.14)
In this context, the reward obtained from increasing the agent’s profitability is denoted
as R1 and it represents the MtM of the agent. The MtM includes not only the profits earned
or lost by the agent but also its value based on the inventory at each time step. Therefore,
it represents the overall value of the agent at every time step. R1 (MtM) is defined as in
Equation 4.15:
R1(s, a)i = Ei + PnLi− HgCi (4.15)
Where:
• (i) Ei: The trading profits or earnings obtained by the MM at time stepti result from
buying or selling stocks. The profits are given by Equation 4.16:
81

Ei =
n∑︂
x=0
(Bx· S prBi) +
n∑︂
x=0
(S x· S prS i) (4.16)
Where Bx and S x refer to the number of stocks traded (buys or sells respectively)
by investors with the MM, and S pr(B,S )i is the buy or sell spread quoted by the MM
respectively at time step ti.
• (ii) PnLi: The inventory held by the MM gains or loses value according to mid-price
variation at every time step ti. PnLi is computed as shown in Equation 4.17:
PnLi = Ii· ∆Pricei (4.17)
where Ii is the quantity of stock held by the MM at ti, and ∆Pricei is the difference
between current and previous stock prices.
• (iii) HgCi: The MM can reduce its inventory instantly by buying or selling it at
every time step, but it incurs a hedging cost as a penalty, as it is executed through a
market-order. The hedging costs HgCi are given by Equation 4.18:
HgCi = Hgi· S preadmkt (4.18)
where Hgi is the amount of inventory hedged, and S preadmkt is the current market
spread, at ti.
On the other hand, R2 is associated with the inventory level maintained by the agent.
R2 (Inventory control) is defined as in Equation 4.19:
R2(s, a)i =−α·| Ii|− HgCi (4.19)
where,
• (i):|Ii|: is the absolute amount of stock held by the MM as inventory in time step i.
• (ii) HgCi: Same definition as described in R1(s, a).
• (iii) : α is a correction term that normalizes R2(s, a) to be in similar scales as
R1(s, a). In our case, and according to a first study of the preliminary results, it
has a value of α = 5. Other normalization techniques can be applied as well. It is
important to remark that this coefficient is only used to scale the parameter w of
the action selection between 0 and 1. This coefficient does not affect the learning
process, as both networks aim to independently optimize their sub-objectives due
to the use of a reward vector instead of a scalar. Therefore, any other value could
have been used without impacting the agent’s performance.
82

Note that hedging is an action that impacts both goals independently. It can be per-
formed at any moment, but the agent is discouraged from doing so, as it has a cost. This
is why the HgCi term is included in both goals’ rewards.
Agent’s architecture
Each independent MM objective is supported by two independent DQN blocks conformed
by 3 hidden layers with 32 neurons each, which compute the Q-value actions for each
objective, thus composing the vectorQ⃗ (s, a) = (Q1(s, a), Q2(s, a)). There are two identical
NNs per goal/block (training and target NN) for the sake of learning stability, as detailed in
Equation 4.2.1. Figure 4.20 illustrates the complete M3ORL agent architecture, including
the reward blocks. Both groups of NN are also included, one per goal.
M3ORL algorithm
The training flow of the market making agent is defined in Algorithm 3. The MORL
algorithm follows the guidelines outlined by Vamplew et al. [89], [100], incorporating
them into the training flow of the MM. First, the buffer and parameters are initialized (line
0). At each time stepti, the MM agent selects three actions: the buy spread, the sell spread,
and the hedge percentage. This selection can be either random or greedy, based on the
epsilon-greedy strategy (lines 7-13). To pick the action greedily, both value functions are
weighted according to the predefined w value. This w guides the exploration according to
the a priori utility function (i.e. to emphasize MtM over inventory control). Nevertheless,
it is important to remark that, in the MORL framework, both Q-value functions are trained
individually, as depicted in lines 22 and 23. This enriches the agent’s knowledge about
each sub-goal. Going back to the flow, and after selecting the proper actions, the MM
agent quotes the prices to the market (line 14), and the hedging is performed (line 15).
Once all the agents have spread their respective prices, the investor agents choose the
agent with the lower spreads to match buy and sell random orders (line 16). The MM
agent then computes the rewards r1i and r2i for each objective and stores the transition in
the replay buffer (lines 17 and 18). Every 200-time steps, both Q-networks are updated
using random transitions (1.024) from the replay bu fferD (line 21). Importantly, the
algorithm updates each NN separately based on the specific sub-goals (lines 22 and 23).
Finally, the Train and Target networks are synchronized on both objectives (line 24).
83

Algorithm 3 M3ORL MM training flow details
1: InitializeD←∅ , t← 0, w← x, n← 200, z← 1.024
2: for simulation do
3: Init ABIDES simulation
4: for every time step ti in the simulation do
5: get current market spread S preadmkt from market data.
6: initialize state, si
7: if rand <ϵ then ▷ pick the best action
8: Qval1i← Q1(si)
9: Qval2i← Q2(si)
10: ai← argmax(w· Qval1i + (1− w)· Qval2i) ▷ buy, sell and hedgeη
11: else
12: ai← random_action() ▷ buy, sell and hedge randomη
13: end if
14: execute action ai (place buy and sell orders)
15: execute hedging from the previous time step Hgi
16: investor agents launch buy/sell (random) operations on the cheapest MM
17: MM computes rewards ri, gathers st+1 and appliesϵ decay
18: MM stores transition⟨si, ai, si+1, (r1i, r2i)⟩ in bufferD
19: t⇐ t + 1
20: if t mod n = 0 then
21: Train NN with z transitions fromD:
22: Q1(s, a)← Q1(s, a) +α(R1(s, a) +γQ1(s′, a′)− Q1(s, a))
23: Q2(s, a)← Q2(s, a) +α(R2(s, a) +γQ2(s′, a′)− Q2(s, a))
24: Target NN⇐ Training NN
25: end if
26: si⇐ si+1
27: end for
28: end for
Multi-objective performance metrics
To evaluate the performance of the solution and to make the results comparable between
algorithms (MORL and reward-engineered algorithms), the following well-known multi-
objective metrics are used [101]–[103]:
• Hypervolume metric: It is a metric used to measure the extent of dominance in the
objective space by a set of solutions on the PF, relative to a reference point. Hyper-
volume provides a quantitative measure of the quality of a PF approximation, with
a larger hypervolume indicating a better approximation. To ensure comparability, it
is often recommended to normalize hypervolumes when they are on different scales.
84

• Sparsity: The sparsity measures the average distance among undominated solu-
tions produced by the algorithm. Specifically, the sparsity is calculated as the sum
of the Euclidean distances between each undominated point in the undominated set
and its closest point, divided by the number of points in the reference set. A smaller
sparsity value indicates better coverage of the PF.
• Number of undominated solutions : This point refers to the amount of undomi-
nated solutions in the non-dominated set. In this sense, the algorithm is better if it
has a higher number of undominated policies.
By using these metrics, di fferent algorithms, including single-objective and MORL
ones, can be objectively compared. It is important to consider all of the metrics in the
comparison, rather than relying solely on one of them, to avoid inaccurate results. This
comprehensive approach is necessary to make an informed final decision.
4.2.2. Methodology and experimental setup
In the study, all experiments were conducted within the simulated trading environment
ABIDES [75], which is an event-based market simulator. This type of environment al-
lows for testing multiple setups, thus increasing the variance of the data and reducing the
risk of overfitting, among other advantages. Moreover, having a simulator provides the
opportunity to train agents in an online manner, enabling RL algorithms such as DQN to
explore various state spaces, as discussed previously.
In the study, inspired by our previous work (Section 4.1), the aim was to generate a
‘standard’ market in terms of price volatility. The market simulation configuration in-
cluded 100 noise agents, 10 value agents, 10 momentum agents, 1 adaptive POV agent,
and 1 exchange agent. The noise agents place orders in the OB in a random direction
of fixed size, while the value agents have access to fundamental time series and operate
based on variations of the mid-price related to their mid-price forecast. The momentum
agents operate based on when 50 and 20-step moving averages are crossed. The adaptive
POV agent provides certain liquidity to the market by placing orders at fixed intervals.
Finally, the exchange agent orchestrates the interaction and integration of all the agents
and the OB.
In addition to these agents, and similar to previous sections, 50 investor agents interact
solely with the market makers. These investor agents place random buy or sell orders with
a fixed size, always choosing the MM with the narrowest spread available in the OB, hence
the cheapest one. If there were many MMs with the same cheapest bid or ask, the investor
would randomly select one of them.
All the simulations begin with an opening price of $1,000.00 and are based on a two-
hour market session from 9:30 am to 11:30 am. One DQN MM agent, one Random MM
(with random prices), and one Persistent MM (also with random prices but keeping the
85

same price stable the whole simulation) are included in each simulation, as competitors.
There were conducted a total of 150 independent simulations across five experiments per
setup.
4.2.3. Experimental results
In this section, the results of the M3ORL agent are presented, and they are compared with
other reward-engineered approaches. The objectives are three-fold: (1) to demonstrate the
effectiveness of the MORL approach in handling the market making problem managing
the two objectives, (2) to show that the M 3ORL approach outperforms standard reward-
engineered approaches in terms of metrics such as hypervolume, sparsity, and the number
of undominated solutions, and (3) to enhance risk management through the use of the
weight parameter while increasing the interpretability of the solution.
In the experiment, 10 di fferent weights, w∈{ 0, 0.1, 0.2,... 1}, are trained and tested
using Algorithm 3. In the training phase, different configurations are started based on the
presented w. Every weight represents a utility function, hence, a prioritization or balance
between both objectives. This w can also be used as an inventory risk aversion coefficient.
The higher thew, the less averse to inventory risk. A total of five independent experiments
are conducted for each w. Once all the agents are trained, one trained agent per weight is
randomly picked, and five different tests are carried out.
Examining the first results, the average outcomes for each testing weight are analyzed
in Figure 4.21, which showcases the trade-o ff between MtM and inventory control, de-
noted by R1(s, a) and R2(s, a) respectively. Each data point represents the average value of
MtM and inventory corresponding to a specificw, obtained from multiple (5) experiments.
Notably, there is a clear trend where increasing thew prioritizes the MtM objective, lead-
ing to higher levels of both MtM and inventory. Note that, for the sake of explanation, the
inventory level is presented always in negative values.
86

Figure 4.21: Test results: Each data point on the plot represents the average value of a
simulation conducted with a specific weight. Five simulations were performed for each
weight, as indicated in the plot. Notably, the plot demonstrates the relationship between
controlling the inventory (lower value of ’w’) and achieving a lower level of sparsity in
the solution, and vice versa.
To further evaluate the performance of different w, the PF for each weight is presented
in Figure 4.22. Among the 11 weights tested, 9 yielded undominated solutions (orange
points), indicating favorable outcomes. However, 2 points remained dominated by the
rest of the solutions (grey points). It is worth mentioning that as the w approaches 1, the
standard deviation of the average solutions also increases (details in Table 4.4), signifying
greater instability when focusing solely on profitability. Conversely, when incentivizing
inventory control, the sparsity of average points in Figure 4.21 is reduced.
87

Figure 4.22: MORL Undominated front. The plot displays all the solutions generated by
the MORL algorithm during the testing stage, distinguishing between dominated solutions
(grey) and non-dominated solutions (orange). Each data point represents the average of
five runs per weight.
88

Table 4.4: MORL and RE-W market making Test Results. This table provides detailed data from
the experiments, showcasing the performance in terms of average MtM and Inventory. It is evident
that the weight parameter plays a significant role in modulating both goals, as indicated in the
figures. It is also remarkable how the MORL approach manages the inventory more e fficiently
than RE-W in higher and lower weights.
MORL MtM MORL Inv RE-W MtM RE-W Inv
Weight Avg[ a] σ Var% Avg σ Avg[b] σ Var% Avg σ
W = 1 1 , 23 35 23 , 95% −106 23 1 , 23 275 27 , 62% 1860 177
W = 0.9 1 , 11 32 11 , 82% −55 10 1 , 37 265 37 , 89% −3986 565
W = 0.8 1 , 09 25 8 , 78% 146 10 1 , 10 31 10 , 72% 135 8
W = 0.7 1 , 04 12 4 , 10% 24 5 1 , 04 29 4 , 09% −17 9
W = 0.6 1 , 02 13 2 , 46% −50 7 1 , 05 25 6 , 24% −66 10
W = 0.5 1 , 01 10 2 , 01% −34 2 1 , 04 11 4 , 42% −9 7
W = 0.4 1 , 03 16 3 , 10% −9 4 0 , 99 10 −0, 44% 22 4
W = 0.3 1 , 04 21 4 , 60% −90 5 1 , 0 5 1 , 08% 14 2
W = 0.2 1 , 006 11 0 , 64% 4 3 1 , 0 2 0 , 47% −3 1
W = 0.1 1 , 001 2 0 , 13% −1 2 1 , 01 3 1 , 01% −10 2
W = 0 1 , 004 4 0 , 50% 1 1 1 , 02 3 0 , 38% 12 1
aFor the sake of legibility the MtM has been adapted to start at 1 instead of 17. Same with standard deviation.
bFor the sake of legibility the MtM has been adapted to start at 1 instead of 17. Same with standard deviation.
Overall, our approach demonstrates its ability to address the market making challenge,
providing a range of undominated solutions to choose from based on the desired utility
function. The PF analysis showcases the e ffectiveness of the MORL approach in achiev-
ing a balance between profitability and inventory control, with a high ratio of undominated
solutions.
Reward-engineered vs MORL analysis
To evaluate the robustness of the MORL approach and compare its performance against
classical RL reward engineering alternatives, a comparison with two reward-engineered
versions was conducted:
1. RE-AIIF. The first one is called Reward Engineering Alpha Inventory Impact Fac-
tor (RE-AIIF). It defines the reward function introduced in Subsection 4.1.1 of the
previous work that scalarizes both goals into a single-objective, including a dynamic
penalty term (Pny) for managing inventory risk, as shown in Equation 4.20.
R(s, a)i = Ei + PnLi− HgCi− Pnyi (4.20)
89

In that equation, Ei represents the reward from the buy and sell profits at ti, PnLi is
the value earned or lost due to inventory value change, andHgCi is the hedging cost.
The penalty term can manage the amount of inventory held dynamically according
to an impact factor (AIIF), as detailed in Equation 4.21:
Pnyi = AIIF· min{|Ri|,|Ri· invi
thri
|} (4.21)
The AIIF coefficient balances between both objectives, where a lower value indi-
cates less inventory control and higher MtM as a result, and vice versa. The fol-
lowing AIIFs were tested: AIIF = 0, 0.2, 0.5, 0.8, 1, 1.5, 2, 5, 10, 100. Ri represents
the MtM reward, defined as Ri = Ei + PnLi− HgCi. Additionally, invi represents
the average inventory value held in the last n time steps, while thri is a dynamic
threshold computed at every time step based on the cash-to-inventory value ratio.
This reward function was compared against other reward functions from di fferent
works, yielding favorable results. The experimental data obtained from the original
work can be found in Table 4.1.
2. RE-W. For the second comparison, a reward function called Reward Engineering
(Weighted) (RE-W) has been developed, which is described by Equation 4.22.
R(s, a) = w· (Ei + PnLi− HgCi) + (1− w)· (−α·| Ii|− HgCi) (4.22)
This function aims to provide a straightforward approach by scalarizing both goals
using weighted terms. It incorporates the same terms as the MORL approach, but
with the inclusion of weights ( w) to combine the subterms into a single reward
value based on a specific utility function. It is important to note that in the MORL
approach, similar weights are used, but they are utilized to guide exploration and
balance between subgoals rather than aggregating their rewards. The motivation
behind designing this weighted reward function is to compare the MORL approach
with a pure weighted reward-engineered approach, ensuring that at least the same
reward terms are considered as inputs for the comparison. As stated, both reward
subterms are similar to Equations 4.15 and 4.19.
Apart from reward functions, and to ensure a fair comparison among methods, most
of the experimental parameters were kept consistent, including the ABIDES environment
configuration, the number and type of agents, the training episode lengths (150), the num-
ber of training episodes per approach (5), the DQN NN architectures, and the state and
action spaces.
In the initial results, it is observed that MORL and RE-AIIF solutions have similar
undominated fronts, as depicted in Figure 4.23. However, the RE-W alternative returns
different undominated solutions, diverging from the MORL set (Figure 4.24). Using the
proposed metrics to compare the three alternatives, the following observations were made:
90

Figure 4.23: Reward-engineered undominated fronts. The plots display all the solutions
generated by the reward-engineered algorithm RE-AIIF during the testing stage, dis-
tinguishing between dominated solutions (grey) and non-dominated solutions (orange).
Each data point represents the average of five runs per weight.
91

Figure 4.24: Reward-engineered undominated fronts. The plots display all the solutions
generated by the reward-engineered algorithm RE-W during the testing stage, distinguish-
ing between dominated solutions (grey) and non-dominated solutions (orange). Each data
point represents the average of five runs per weight.
1. Hypervolumes: Figure 4.25 and Table 4.5 illustrate that the MORL approach
covers a larger area compared to the classical alternatives: 9.71 vs 9.56 (RE-W) and 6.8
(RE-AIIF). To calculate the hypervolumes, all the solutions are first normalized to the
range [0, 1], with a little extra margin. This is achieved by applying min-max normal-
ization to every point, independently for each axis. For this exercise, the Nadir point is
chosen as the reference point (Figure 2.2, [104]).
92

Figure 4.25: Comparison of normalized hypervolumes among algorithms: The extent of
the objective space covered by each algorithm determines its performance, with a larger
coverage indicating a better algorithm. In this sense, MORL has the larger hypervolume
(9.62), followed by RE-W (8.46) and RE-AIIF (6.71).
2. Undominated solutions: If all the solutions are aggregated into one set, as shown
in Figure 4.26, the MORL approach exhibits a higher number of undominated solutions
(7 out of 15) compared to the classical approaches: 6 (RE-W) and 2 (RE-AIIF) out of
15. A higher number of undominated solutions indicates a higher quality front, as the
algorithm provides more non-dominated solutions.
93

Figure 4.26: Combined Pareto front from undominated solutions. The plot showcases
the undominated solutions obtained from the three algorithms. In our case, MORL con-
tributes the most solutions (7 out of 15), followed by the RE-W (6 out of 15), and the pure
reward-engineered solution RE-AIIF (2 out of 15).
3. Sparsity: Finally, the average Euclidean distance between the undominated solu-
tions is calculated to assess their proximity. Once again, the MORL approach demon-
strates a lower sparsity between undominated solutions compared to the classical ap-
proaches: 299k vs 453k (RE-W) and 561k (RE-AIIF).
All the multi-objective metrics are detailed in Table 4.5. In addition to these metrics,
the MtM and Inventory values from the MORL and RE-W experiments can be reviewed
in Table 4.4. As for the RE-AIIF experiments, all the values can be reviewed in Table
4.5).
94

Table 4.5: Comparison of multi-objective metrics: hypervolume, sparsity, and undom-
inated solutions. The performance of the MORL, RE-AIIF, and RE-W experiments is
evaluated using the three key metrics. The results demonstrate that the MORL approach
outperforms the other two reward-engineered algorithms across all three metrics, indicat-
ing its superior performance and e ffectiveness in handling the multi-objective nature of
the problem.
Hypervolume1 Sparsity2 Undominated
Experiment Surface Avg σ Amount
MORL 9.62 ≈ 299k ≈ 385k 7 (46.6%)
RE-AIIF 6 .71 ≈ 561k ≈ 674k 2(13.3%)
RE-W 8 .46 ≈ 453k ≈ 515k 6(40%)
Note 1: Normalized hypervolume.
Note 2: High values due to MtM figures.
4.2.4. Analysis: The relevance of trend information in the proposed method
One relevant aspect of financial markets is related to trends, where prices typically con-
tinue moving upwards or downwards for unknown periods. In this regard, many algo-
rithms and strategies take advantage of this behavior [97]–[99]. Classical autoregressive
models, such as ARIMA, are commonly used as inputs for various strategies.
In this dissertation, this aspect has not been directly considered. Although some in-
stant variation information, such as the mid-price variation between the last timestep and
the present, is included, there is no explicit consideration of trends in the current MM
strategies. To evaluate whether this omission could represent a potential weakness in the
proposed methods, an additional experiment has been conducted using the MORL agents.
To capture short-term price trends, Exponential Moving Average (EMA) information has
been added to the initial state space of the RL MM agents. EMA is preferred over the
standard moving average because it is more sensitive to recent price changes, which is
beneficial for high-frequency strategies. This momentum metric is commonly used in
intraday strategies.
For this additional experiment, two different types of agents have been compared:
• The MORL Agent without any additional information, as used in Subsection 4.2.1,
where the standard state space of 8 variables is applied.
• Three MORL Agents that include 3 additional variables in their state space: EMA-L
(long), EMA-S (short), and EMA-L Slope, resulting in a total of 11 state variables.
The purpose of using two di fferent EMA metrics is to allow the agent to detect
when they cross each other, signaling different phases of the trend.
95

The only difference between EMA-L and EMA-S is the number of data points con-
sidered in each option, with EMA-L exhibiting a slower behavior compared to EMA-S.
EMA-L and EMA-S are computed as shown in Equation 4.23:
EMAt =α· xt + (1−α)· EMAt−1 (4.23)
where EMA t is the Exponential Moving Average at time t, α is the smoothing factor,
typically calculated as α = 2 1+N , with N being the number of periods. xt is the value at
time t, and EMAt−1 is the Exponential Moving Average from the previous time step.
EMA-L Slope, on the other hand, is the di fference in EMA-L between two points, as
represented in Equation 4.24. This aims to capture the smooth trend in the market.
EMA-L Slopet = EMA-Lt− EMA-Lt−n (4.24)
In the experiment, three di fferent EMA-L/EMA-S configurations have been tested:
(20,8), (15,4), and (10,2), with EMA-L Slopes of 20, 15, and 10 minutes respectively.
For instance, in the first case (20, 8) indicates the use of an EMA-L of 20 minutes and
an EMA-S of 8 minutes. Figure 4.27 shows two ABIDES trading sessions with di fferent
EMAs calculated based on the setup. 150 simulations per experiment (5 seeds) have
been run, keeping the same parameters and hyperparameters the same as in the MORL
Subsection 4.2.1.
Figure 4.27: EMAs example of different trading sessions: EMA-L 20 minutes + EMA-S
8 minutes (left) and EMA-L 10 minutes + EMA-S 2 minutes (right).
Results: Initial results from the training stage indicate that agents with additional
EMA variables in their state space perform worse, as shown in Figure 4.28.
96

Figure 4.28: Training results of agents with and without EMA variables in the state space.
Testing the final neural network from the training stage over 150 sessions confirms
that including trend information does not improve performance in our MM strategy. In
fact, it results in noisier behavior compared to the standard MORL agent, as depicted in
Figure 4.29.
Figure 4.29: Testing results of agents with and without EMA variables
97

There are several possible reasons for this degradation. One possibility is the increased
complexity of the state space, which expands from 8 to 11 variables. To rule out this
factor, an additional experiment was conducted by increasing the number of simulations
from 150 to 450 to see if performance improved compared to the standard agent. Due
to computational constraints, only one EMA agent (the best-performing one from the
previous training) was tested in this validation. As seen in Figure 4.30, this increase
proportionally affects both agents without any significant improvement in the EMA agent.
Figure 4.30: Training results of extended simulations with EMA and standard agents.
Other factors contributing to this lack of improvement could also be considered. For
instance, the nature of the strategy, which is based primarily on instantaneous spreads and
inventory management, and characterized by a high number of operations within short
timeframes (HFT style), may be less reliant on long-term or short-term price trends. High-
frequency trading strategies typically prioritize rapid execution and immediate market
conditions, making them less sensitive to the momentum and trend-following signals that
EMAs are designed to capture. It is possible that other types of strategies, particularly
those with longer holding periods or a focus on trend-following, would benefit more from
incorporating EMA variables.
Therefore, while the introduction of EMA variables did not improve the performance
of the current strategy, it does not rule out their potential utility in other trading approaches
that depend more heavily on market trends and price momentum.
98

4.2.5. Discussion
The results of the experiments demonstrate that the MORL approach consistently outper-
forms single-objective reward-engineered methods when controlling both goals simulta-
neously (Table 4.4). Specifically, it surpasses the classical approach in multi-objective
key metrics such as hypervolume, sparsity, and the number of undominated solutions,
indicating significant improvement (Table 4.5). The separate treatment of sub-objectives
within the MORL approach enables better specialization and stability in the solutions.
Additionally, compared to a fully reward-engineered approach (w/o weights), the MORL
approach offers several distinct advantages in the context of market making problems:
(1) By treating profitability and inventory management as separate objectives, the MORL
approach eliminates the need for time-consuming reward engineering and removes any
subjective influence on reward definition; (2) The separation of the two objectives within
the framework allows the agent to specialize and comprehend the nuances of both ob-
jectives, resulting in improved overall performance; (3) The separation of subobjectives
also enhances the explainability of the subsequent selection process, as it highlights the
impact of MtM improvement versus inventory management and vice versa; (4) Further-
more, the MORL approach is highly adaptable to changes in the final utility function, as it
relies on a single factor (weight, denoted as w) that can be easily adjusted over time. This
allows for dynamic risk aversion adjustments in the market making agent during trading
sessions.
While similar adaptability can be achieved in weighted reward-engineered functions
such as in RE-W, the MORL approach with its separate NNs for each objective o ffers
more flexibility in modifying the architecture, Q-Network, or state space for each objec-
tive. This flexibility is particularly valuable when dealing with assets exhibiting complex
behaviors, such as highly volatile stocks or assets with low liquidity. These advantages,
including the ability to manage the complexity of one objective without sacrificing per-
formance in the other, are not easily attainable with reward-engineered alternatives.
Overall, the MORL approach offers superior performance, increased adaptability, bet-
ter objective specialization, and enhanced explainability compared to single-objective
reward-engineered methods. It provides a robust framework for addressing multi-objective
market making problems and offers significant advantages over traditional approaches.
From a financial standpoint, these tools o ffer a more robust approach to navigating
the markets. The Pareto fronts (PFs) allow financial business users to assess how well
the agent will perform by considering the balance between maximizing profits and man-
aging inventory. By selecting the proper ‘w’ parameter based on the operator’s specific
a priori utility function, strategies can be adapted to di fferent market conditions or levels
of aggressiveness. This means they can e ffectively tailor their approach to meet specific
goals, whether it is increasing profits or minimizing risks. Ultimately, these tools pro-
vide valuable insights that help them make informed decisions and optimize their trading
strategies. It also provides them with an understanding of the algorithm’s limitations be-
99

fore deploying it in the market.
Nevertheless, this technique has its limitations. A weakness of this method is the ne-
cessity of having one agent per trained weight. This implies training one agent per w,
which increases the complexity of the final solution, and the training /adjusting time, and
reduces the generalization capabilities of the method. Other alternatives exist to address
this issue, such as Universal Value Function Approximators (UVFAs) [105], but they have
shown worse performance compared to specific MORL algorithms [23]. Another weak-
ness compared to reward-engineered versions is the increased computational time. Using
one (or two) neural networks per goal, instead of just one as in the reward-engineered al-
ternative, can increase both computational time and resource usage. Parallelization tech-
niques may be necessary to reduce the required computing time.
4.2.6. Contributions
This work makes significant contributions to the optimization of market making strategies
through a multi-objective RL framework that deals perfectly with the profitability/inven-
tory control challenge. The specific contributions are:
1. Development of a multi-objective RL framework: Introduction of a multi-objective
RL framework that outperforms previous reward engineering approaches in market
making. The advantages of this framework include:
• Elimination of the need for time-consuming reward engineering, streamlining
the development process.
• Reduction in computational time due to more efficient learning algorithms.
• Enhanced specialization in subgoals, allowing for more targeted strategy de-
velopment.
• Improved capability to balance between conflicting subgoals, optimizing over-
all strategy effectiveness.
2. In-depth analysis of multi-objective metrics : Extensive evaluation of the pro-
posed multi-objective RL framework using several key metrics, which are crucial
for validating the effectiveness and robustness of the approach:
• Hypervolume: Utilization of hypervolume measurements to assess how well
the proposed solutions cover the range of possible objective values.
• Sparsity: Analysis of sparsity to determine the distribution of solutions within
the objective space, ensuring diverse solution sets.
• Number of undominated solutions : Examination of the count of undomi-
nated solutions to evaluate the competitiveness of solutions against each other.
100

These metrics provide a comprehensive framework for validating the effectiveness
of the multi-objective RL approaches and demonstrating their superiority over tra-
ditional single-objective optimization techniques.
Additionally, the introduction of trend information has been tested by incorporating
EMA variables into the state space to assess their impact on the proposed method. The
results indicate that, in this case, the inclusion of this information does not provide any ad-
vantage. Although this was tested on MORL agents within this section, these conclusions
can be extended to the rest of the agents presented.
This work establishes a market making agent capable of robustly managing both prof-
itability and inventory control, paving the way for further enhancements. The agent’s
dual focus not only strengthens its operational e fficiency in real-time market conditions
but also sets a foundation for future advancements in market making strategies. By inte-
grating multi-objective RL, the agent effectively balances the complex trade-offs between
achieving high returns and maintaining optimal inventory levels. This balance is cru-
cial for sustaining long-term viability and competitiveness in the dynamic landscape of
financial trading.
101

5. AUTOMATION UNDER NON-STATIONARITY
Having developed an RL market making agent capable of maintaining profitability
while managing inventory, the next step is to ensure the agent’s autonomous adaptation to
environmental changes. Given the dynamic nature of financial markets, having a strategy
that can seamlessly adjust to these fluctuations is essential. As mentioned earlier, financial
markets are inherently non-stationary, making it crucial to address this property. In the
upcoming section, a modification of the previously established M 3ORL agent will be
introduced. This enhancement aims to transform the agent into an autonomous entity
capable of navigating the evolving landscapes of financial markets robustly.
5.1. Dealing with non-stationarity: Continual learning
As stated in Subsection 2.1.5, one usual technique to adapt to changes in the environment
is letting the agent, or the ML model, be fine-tuned with new incoming experiences or
data without losing previous knowledge. This is also known as continual learning (CL).
In this regard, there are ML techniques that deal with this issue. One of the goals of
the work presented in this chapter is to examine and compare three di fferent strategies
that address the challenges of CL: freezing layers (FL), data rehearsal (DR), and elastic
weight consolidation (EWC). The purpose is to understand the strengths and weaknesses
of each approach and to establish a benchmark for evaluating the algorithm proposed in
this dissertation. This section provides an overview of each of these strategies.
Freezing layers: This method strategically fixes the weights of certain layers within the
network, typically the early layers responsible for capturing basic and general features,
while allowing the weights of later, more task-specific layers to adjust and learn from new
tasks [49]. The rationale behind freezing the initial layer/s is to preserve the fundamental
knowledge they have, which is assumed to be broadly applicable across various tasks.
On the other hand, the adaptable deeper layers facilitate the learning of new, task-specific
nuances. Let Θ represent the entirety of parameters within the NN, Θ f denote the subset
of parameters located within the frozen layers, and Θt signifies the subset of parameters
residing within the trainable layers. During training on a new task, the update rules for
the parameters are:
1. For frozen layer parameters θ f∈ Θ f :
θ(new) f =θ(old) f
i.e., the parameters in frozen layers remain constant.
2. For trainable layer parameters θt∈ Θt:
θ(new) t =θ(old) t −α∂L ∂θt
102

i.e., the parameters in trainable layers are updated via gradient descent, where α is
the learning rate and ∂L ∂θt is the gradient of the loss function L.
This technique is not only applied on CL tasks, it is also indeed very common in
fine-tuning tasks [106], [107], moreover when big pre-trained models are involved.
Elastic weight consolidation : another alternative, which is “parameter’s selective” in-
stead of “layer’s selective”, is EWC [53]. This approach mirrors, in some way, the brain’s
method of synaptic consolidation, allowing for continued learning in artificial NNs by
ensuring key parameters remain close to their previously established values. To achieve
this, the Fisher information matrix is calculated once the agent is trained, using the train-
ing dataset. This way, a relative importance weight factor is obtained, which is used as
a penalty in further training. This approach prevents the deterioration of performance on
earlier tasks while new tasks are being learned. Due to the inherent over-parameterization
in deep NNs, where numerous parameter configurations can lead to similar outcomes,
EWC strategically restricts updates to a specific zone that maintains accuracy for earlier
tasks. This restriction is realized through a quadratic penalty that acts akin to a variable-
strength spring, anchoring the parameters based on their relevance to the task just com-
pleted. EWC meticulously modulates the learning trajectory to prevent significant de-
viations from the solutions of all preceding tasks, thereby harmonizing the retention of
previous knowledge with the acquisition of new information, according to the loss func-
tion of Equation 5.1.
L(θ) = LB(θ) +
∑︂
i
λ
2 Fisher i(θi−θ∗ A,i)2 (5.1)
Where LB(θ) is the loss for task B only (the new one), λ sets the importance of the
old task relative to the new one, Fisher i is the Fisher information matrix concerning the
previous task’s parameters, θ∗ A,i represents the parameters of the previous task A, and i
indexes each parameter.
Data rehearsal : The last scrutinized technique, compatible with the aforementioned
methods, leverages the reuse of previous experiences to mitigate the forgetfulness of
older information upon the introduction of new data [50]–[52]. Particularly relevant in the
context of off-policy RL algorithms, this approach involves the utilization of old replay
buffers in conjunction with new transitions during the training phase. In essence, multiple
distinct replay buffers exist, each accumulating experiences based on varied criteria. This
work explores the integration of two complementary replay buffers — one containing the
initial agent’s training data and the other housing new experiences acquired during the
testing phase — in varying proportions. Specifically, being a dataset of t experiences
D ={(s, a, s′, r)0,..., (s, a, s′, r)t}, two of them are considered: Dold with old experiences
and Dnew, containing newly gathered experiences during the testing phase. The combined
replay buffer Dcl, employed for CL, is formulated as in Equation 5.2.
103

Dcl =γ· Dold + (1−γ)· Dnew (5.2)
Here, γ∈ [0, 1] represents the proportion in which the old experiences are incorpo-
rated relative to the new experiences, effectively balancing the influence of historical and
recent data in the CL process. This approach allows the RL algorithm to balance between
both data distributions, forcing it to learn a more general policy.
5.2. Discounted Thompson sampling
As part of the proposed MM agent, it is necessary to introduce the discounted Thompson
sampling (dTS) technique. Classical TS [108] is a multi-armed Bayesian bandit strategy
employed in sequential decision-making scenarios, designed to strike a balance between
leveraging existing knowledge for immediate gains (exploitation) and gathering new data
to enhance future outcomes (exploration). This algorithm efficiently tackles a wide spec-
trum of challenges, earning it widespread adoption due to its computational effectiveness
and versatility. In the TS algorithm with Bernoulli arms, a Bernoulli sampling model
coupled with a Beta(α,β) prior distribution can be selected. Consequently, as depicted by
Equation 5.3, the posterior distribution for each round will follow a beta distribution:
Ii∼ Beta(α + S i,β + Fi), i = 1, 2, 3,..., k; (5.3)
S i denotes the cumulative number of successes and Fi denotes the cumulative number
of failures. As the number of rounds progresses, the beta distribution increasingly nar-
rows in on the empirical mean, reflecting a more precise estimation of the underlying
probability with each additional round. This default setup is good where a stationary en-
vironment is present, where coefficients grow according to the evolution of the trials. The
problem arises when the underlying dynamics change, making it di fficult to adapt these
coefficients to the new probability distributions, as it has to forget some way the last in-
puts. To mitigate this, there is one modification of the TS algorithm called discounted
Thompson sampling [109], [110]. In this alternative, two coefficients modulate theα and
β parameters in every update, according to the Equations 5.4 and 5.5:
S i = S i + rs, if ci = ai,
Fi = Fi + r f, if ci ≠ ai
(5.4)
S i =γS i, Fi =γFit,∀γ∈ [0, 1] (5.5)
At every round i, the dTS algorithm selects an arm ci based on the current α and β
coefficients. If the chosen arm is the winning arm ai, the success counter S i is incre-
mented by rs; otherwise, the failure counter Fi is incremented by r f . Additionally, both
104

coefficients are discounted byγ as described in Equation 5.5. Therefore, theγ coefficient
allows us to adjust the significance of recent experiences relative to older ones, depending
on the characteristics of the specific environment.
5.3. Methodology: Multi-objective policy selection in dynamic markets
As described, the market making challenge involves balancing two main objectives: (i)
maximizing MM profitability and (ii) minimizing inventory levels to reduce devaluation
risks. To tackle these objectives, a MORL methodology (M3ORL MM) was introduced in
Subsection 4.2.1. This approach allows for the autonomous learning of these objectives
within a specialized multi-objective framework. After learning a set of multi-objective
policies across various contexts, it is proposed to assemble a library with these policies.
The POW-dTS algorithm, outlined in Subsection 5.3.2, is then tasked with selecting the
appropriate combination of these pre-trained policies from the library based on the evolv-
ing market conditions. This technique will be an essential component of the autonomous
MM agent.
5.3.1. Market Maker as a MOMDP
In our RL framework, the RL MM agent is conceptualized as the M 3ORL MM agent
presented in Subsection 4.2.1, and in previous sections as well. In this regard, our MM
is a DQN-based agent equipped with two pairs of NNs (train and target), conformed by
3 hidden layers with 32 neurons per NN, each managing a specific goal separately. The
state and action spaces, as well as the multi-objective reward vector, remain identical to
those of the MORL agent.
5.3.2. Policy Weighting through discounted Thompson sampling (POW-dTS) Algo-
rithm
To achieve good performance with M3ORL MMs in non-stationary markets, the following
POW-dTS algorithm is proposed. In essence, it is a dynamic agent weighting mechanism
that utilizes dTS to alternate among different policies sequentially. The primary goal is to
manage effectively a set of M 3ORL MM pre-trained agents (or policies) by periodically
recalibrating their weights based on real performance, thereby optimizing the decision-
making process over time along an evolving market. The intuition behind this is that each
pre-trained agent is allocated a duration of time according to the weight that dTS assigns
to it. It is important to remark that, instead of alternating agents every time step, they
are allowed to perform actions during their corresponding time steps, and weights are
calculated accordingly. This approach is deemed more appropriate as RL is designed to
act based not only on the immediate reward but also on subsequent ones. Alternating the
agents in blocks in this manner ensures they better exploit their respective policies.
105

The algorithm is divided into two functions. Algorithm 4 provides the general flow,
while Algorithm 5 focuses on the evaluation and recalibration part of the coefficients and
weights of the dTS. Initially, as outlined in Algorithm 4, the algorithm sets up initial pa-
rameters and structures. Some parameters must be passed to the algorithm: the library
of agents/policies to be used, A, the modifiers of α and β coefficients, αinc and βinc, the
gamma discount parameter of the dTS algorithm,γ, how often the algorithm should be re-
calibrated, rounds exp , the number of testing time steps per recalibration round,rounds recal,
and how many total rounds the agents will perform their actions in the exploitation stage
(according to their weights), exp ts. Some variables also need to be initialized: the recal-
ibration flag recal, which indicates whether the algorithm is performing an update (line
1 in Algorithm 4); the initial alpha and beta coe fficients for all the agents (line 2); the
default initial weights per agent (line 3); the actuation range per agent, denoted by the
array secs (line 4); and a starting agent agt (line 5). The sections included in the vari-
able secs will be populated during the recalibration stage, according to this structure:
[(xi, xe)0,..., (xi, xe)n], where both xi and xe represent the initial and ending time steps for
each agent, respectively. Lastly, the counter tstest is initialized to 0 (line 6).
106

Algorithm 4 POW-dTS(A,αinc,βinc,γ, rounds exp , rounds recal, exp ts )
1: Set recalibration flag: recal← False,
2: Initialize alpha and beta coefficients per agent: coefs← [(1, 1)0,..., (1, 1)n]
3: Initialize agent’s weights: weights←
[︂
1
n,..., 1 n
]︂
4: Define sections array: secs← [ ]
5: Select an initial agent: agt← A[0]
6: Init tstest← 0
7:
8: for t = 0 to T do
9: rew← step(agt) ▷ Execute action by current agent agt and collect reward
10: if t mod rounds exp = 0 then ▷ Recalibration triggered
11: Set recalibration flag: recal← True
12: Reset current time steps: tsrecal← 0, tstest← 0
13: Set current agent index: curragt← 0
14: for f in range(len(A)) do
15: Init results dictionary: results [ f ]← [ ]
16: end for
17: end if
18: if recal then ▷ The agents’ performance is tested
19: results [curragt].append(rew) ▷ Append the reward
20: curragt← round(tsrecal/rounds recal) ▷ Update current agent index
21: if curragt < len(A) then
22: agt← A[curragt] ▷ Select the agent
23: else
24: recal← False ▷ End recalibration
25: agentwin← max reward agent index at results
26: secs← Recalibration(A, coefs,αinc,βinc agentwin, exp ts). ▷ Alg. 5
27: end if
28: tsrecal += 1
29: else
30: agt← Select the agent for the current time step tstest based on sections secs
31: tstest += 1
32: end if
33: end for
Once everything has been initialized, the algorithm enters a predefined loop for a
set number of iterations T (line 8), with each iteration representing a single time step.
During each time step, the selected and active agent, denoted as agt, executes a greedy
action, and the outcome, or reward rew, is recorded (line 9). Periodically, the algorithm
initiates a recalibration of the agents’ weights to adapt to environmental changes (line
10). This recalibration process begins after initializing all required variables (lines 11-
16), where each agent is allotted an equal number of time steps to act in a sequential
107

manner (line 20). Throughout these recalibration periods, agents interact with the en-
vironment, earning rewards that reflect their performance (line 19). Upon evaluating
all the agents or policies in A (lines 21-23), the algorithm determines the agent that
achieved the highest returns during the testing phase (line 25). Utilizing this data, it
proceeds to an update phase, adjusting the weights to current performance levels through
the Recalibration function (line 26). Once the recalibration phase has concluded and all
the new sections have been determined, the agent is selected according to the counter
tstest (line 30). For instance, if there are 4 policies or agents with the following sections
secs = [(0, 10)ag1, (11, 25)ag2, (26, 30)ag3, (31, 38)ag4], and the current testing time step is
14, then agent number 2 will be active. This agent continues until the tstest counter
reaches 26, at which point agent 3 will be selected.
Exploring the recalibration function further (Algorithm 5), which calculates weights
and sections, it starts by processing the initial set of reference policies/agents, A, the cur-
rentα andβ coefficients for every agent,coe f s, the agent that achieved the highest reward
in the previous testing phase,agentwin, and the total number of time steps during which all
agents will perform their policies in the exploitation stage,exp ts, as determined by the re-
cently computed weights. The initial step involves selecting a winning agent based on the
currentα andβ coefficients (line 1 in Algorithm 5). These coefficients influence the selec-
tion probabilities. If the POW-dTS’s predicted winner aligns with the actual testing stage
winner (line 8), an increase to that agent’s α coefficient is applied (line 9) to promote its
future selection; conversely, if there’s a mismatch, theβ coefficient is incremented instead
(line 11). This adjustment is designed to shift selection probabilities in favor of agents
demonstrating superior performance. Additionally, a discount factor, γ, is applied to the
coefficients of all the agents, including the rest (line 14). After recalibrating the α andβ
coefficients, the agents’ weights are recalculated (lines 20 - 24), altering the probability
distribution in line with the adjusted α andβ coefficients and ensuring the total weights
sum to 1. These revised weights then inform the determination of operational intervals for
each agent (lines 25-27), proportionate to the recalculated weights. This function finally
returns the sections for all the agents that are used in Algorithm 4 (line 30). Figure 5.1
depicts the algorithm flow.
108

Figure 5.1: This image depicts the POW-dTS flow. In the first stage of the algorithm, a
set of policies is trained to capture the di fferent dynamics in the environment. Once the
policy set is defined, the algorithm moves to the Performing phase, where it operates in the
market by assigning sequential ranges of time (secs) to the policies based on calculated
weights. The weights are recalculated every n steps during the recalibration phase, using
discounted Thompson sampling.
109

Algorithm 5 Recalibration(A, coefs,αinc,βinc agentwin, exp ts)
1: bestthp← argmax([random.beta(a, b) for (a, b) in coefs])
2: Initialize: initpos← 0
3:
4: #α andβ coefficients update
5: for ag in range(len(A)) do
6: a, b← coefs[ag] ▷ Currentα andβ coefs of this agent are gathered
7: if ag == agentwin then
8: if ag == bestthp then
9: a←γ· (a +αinc) ▷ Increaseα (success)
10: else
11: b←γ· (b +βinc) ▷ Increaseβ (fail)
12: end if
13: else ▷ For the rest a and b are discounted by gamma
14: a←γ· a, b←γ· b
15: end if
16: coefs[ag]← (a, b) ▷ Update with the new coefs
17: end for
18:
19: #Weight’s adaptation
20: weightsum← sum([a/(a + b) for (a, b) in coefs])
21: weights← []
22: for c in coefs do ▷ Weights’ recalibration according to a and b
23: weights[c]← (coefs[c][0]/(coefs[c][0] + coefs[c][1]))/weightsum
24: end for
25: for s in secs do ▷ Sections’ adjustment according to weights
26: secs[s]← (initpos, round(initpos + exp ts· weights[s]))
27: initpos← initpos + round(exp ts· weights[s])
28: end for
29:
30: return secs
It is crucial to highlight that, during the policy exploitation phase, agents are deployed
in segments as per the pre-defined intervals, operating continuously until the onset of the
next recalibration phase. This operational mode promotes the calculation of time intervals
secs. For example, and as stated previously, ifx time steps are set aside for an agent’s turn
(let’s call this a section), that agent will keep going until those x time steps are up. Once
that time is done, the next agent in line takes over. One additional and relevant point is the
algorithm’s adaptability to unseen scenarios, as it seeks the most profitable combination
of known policies in terms of rewards.
110

5.4. Experimental evaluation
In this section, extensive experiments are performed to validate the e ffectiveness of the
proposed POW-dTS algorithm. Specifically, Subsection 5.4.1 introduces the trading en-
vironment and the baseline models used for comparison. Subsection 5.4.2 presents the
results and subsequent discussion. Finally, in Subsection 5.4.3, several ablation studies
are conducted to analyze the contribution of each proposed module to the trading perfor-
mance.
5.4.1. Experimental setup
The experimental setup for the market simulation in ABIDES consisted of the following
agents: 100 noise agents, 10 value agents, 10 momentum agents, 1 adaptive POV agent,
and 1 exchange agent. Regarding MMs, the simulation incorporated 1 random MM, and
1 persistent MM agent, in addition to specific M 3ORL MM competitors, to gauge per-
formance across different independent runs. Both perform random actions, but persistent
MM keeps one random price all over a simulation. The experiments involve varying the
number of M3ORL MM competitors to introduce non-stationarity: 0, 1, 5, and 7, creating
different contexts. Additionally, to define a set of pre-trained policies in various contexts
and thus construct the library A utilized as input by Algorithm 4, there were trained four
M3ORL MM agents within each of these contextual settings: one in the absence of any
RL competitors, another in the presence of a single competitor, a third in the presence
of five competitors, and a fourth in the presence of seven competitors. These agents un-
derwent training over 150 trading sessions each in the cases of 0, 1, and 5 competitors,
and over 300 sessions in the case of 7 competitors due to increased complexity. All the
agents were trained using anϵ-greedy strategy with epsilon decay. More details about this
training stage can be found at Figure 5.2 and Figure 5.3.
111

(a) MtM of M3ORL MM training with 0 MM competitors
(b) MtM of M3ORL MM training with 1 MM competitors
Figure 5.2: MtM of M3ORL MM training with 0 and with 1 MM competitors.
112

(a) MtM of M3ORL MM training with 5 MM competitors.
(b) MtM of M3ORL MM training with 7 MM competitors.
Figure 5.3: Optimal agents trained against 0, 1, 5, and 7 M 3ORL MM competitors. The
plot distinctly illustrates two phases: an initial training phase against n additional com-
petitors, followed by a testing phase where the agent acts greedily.
Each complete experiment follows the sequence seq of context changes with:
seq = 0→ 5→ 1→ 7→ 1→ 7→ 5→ 0,
where a different number of MM competitors are considered. Figures 5.4-5.7 depict the
evolution of each agent in library A across each of the contexts in this sequence seq.
Each context is evaluated over 50 or 80 trading sessions of 2 hours trading session each,
based on the approach being tested. All the simulations started with an opening cash of
$100.000, 00, spanning a two-hour session. The multi-goal reward is defined as 90% of
R1 (MtM) with 10% of R2 (inv. control).
113

Figure 5.4: MtM of M3ORL MM agent pre-trained with 0 MM competitors.
Figure 5.5: MtM of M3ORL MM agent pre-trained with 1 MM competitor.
Figure 5.6: MtM of M3ORL MM agent pre-trained with 5 MM competitors.
114

Figure 5.7: MtM of M3ORL MM agent pre-trained with 7 MM competitors.
The M3ORL MMs trained without competitors and with one competitor yield similar
results across the contexts as shown in Figures 5.4 and 5.5. Conversely, in Figure 5.6 the
M3ORL MM trained against five competitors produces slightly better results than the oth-
ers in competitive contexts. Finally, in Figure 5.7 the M 3ORL MM agent trained against
seven competitors faced an exceedingly hostile environment during learning, making it
challenging to learn an appropriate behavioral policy, and thus exhibits the poorest evolu-
tion across contexts.
The experiments can be categorized into two distinct types: single-policy and multiple-
policy methodologies. In single-policy approaches, an initial behavior policy is estab-
lished, aiming to refine its effectiveness as the market dynamics evolve through contextual
changes. In particular, the same M3ORL MM agent is used, pre-trained with no competi-
tors, and tries to adapt it to each new context. Each context runs for 50 rounds, or trading
sessions, totaling 400 rounds. The comparison includes the following single-policy tech-
niques:
• Single-policy: The agent is not retrained during the experiments and acts greedily
in all contexts, applying only the pre-trained policy. The agent trained with no
competitors is used as the baseline for the rest of the experiments. There are 3
additional single-policy versions according to the number of competitors the agent
was trained with 1, 5, and 7. Figures 5.4-5.7 represents one run of every di fferent
mentioned policy. The baseline agent corresponds to Figure 5.4.
• CL-SingleP: The agent mentioned as the baseline (single-policy with 0 competi-
tors) is continuously retrained across the different contexts using only incoming ex-
periences. This setup was tested with two different learning rates: lr∈{ 0.1, 0.05}.
• CL-FreezingL: The technique of FL is used in this setup. The baseline agent has
all the NN layers frozen (the parameters) except for the last one, which is updated
with incoming experiences.
• CL-Rehearsal: DR is applied here. The baseline agent is retrained across different
contexts using both incoming and old experience replay buffers, maintaining a 50%
115

(old) / 50% (new) replay-buffer ratio.
• CL-EWC: EWC is applied in this setup with the baseline agent. The baseline
agent’s NNs’ parameter updates are penalized based on the Fisher information ma-
trix computed during the training stage. Three di fferentλ coefficients were tested:
λ∈{ 0.5, 1, 10}. A higher value of λ makes the network’s parameters more resis-
tant to change, thereby prioritizing the retention of what the network has previously
learned, and vice-versa.
These single-policy techniques use only experiences gathered during greedy behav-
ior, without any additional exploration. For comparison, adding 30 specific exploration
rounds after every context change was also tested. This applies to CL-SingleP, CL-
FreezingL, CL-Rehearsal, and CL-EWC setups. The motivation behind this was to eval-
uate if exploring other states could improve the agent’s policy by applying the mentioned
techniques. These experiments are denoted with an “exp” suffix in figures and tables. In
these alternative approaches, the total rounds per context are 80, comprising 30 rounds
for additional exploration plus the 50 default exploitation rounds. Essentially, these ex-
ploration rounds consist of increasing the DQN epsilon to 1 for these 30 rounds, allowing
the agent to explore di fferent states and actions. It is significant to mention that these
exploratory alternatives require some form of context change detection, which is not im-
plemented in this work. Instead, for comparison, an ‘automatic context change detection
is applied at the start of each new context.
Conversely, the multiple policy method involves the availability of a library containing
diverse policies at the outset. Here, the objective shifts to the dynamic selection of the
most suitable policy at any given moment, tailored to the prevailing market conditions.
The following multi-policy techniques are included:
• Multi-policy (Benchmark) : This setup serves as a comparison benchmark and
consists of including the best agent for each context from the beginning. This rep-
resents the best possible configuration, as all the pre-trained agents have the optimal
policy for their context. It assumes the presence of a perfect change point detector
and a precise agent’s designator for each context.
• POW-dTS (ours): The algorithm was tested with various γ and α/β modifiers:
γ∈ 0.4, 0.85 andαinc,β inc∈ 1, 5. Lower γ values reduce the influence of older ex-
periences, increasing forgiveness, whereas higher alpha and beta modifiers facilitate
faster adaptation by the algorithm. Depending on the environment, it is important
to select an appropriate γ value. As previously noted, the algorithm employs four
distinct pre-trained policies: for 0, 1, 5, and 7 M 3ORL MM competitors. POW-
dTS was initialized with rounds exp = 3, indicating to launch a recalibration every 3
rounds, rounds recal = 150 setting the time steps per recalibration round, andexp ts =
750 that established the max time steps per exploitation round.
116

• Random agents: More detailed in the ablation study Subsection 5.4.3, and simi-
lar to the POW-dTS setup, two alternative configurations were explored: Random
Agent (Blocks), which assigns random weights to each block for the four agents;
and Random Agent (Timesteps), where the concept of blocks is discarded in favor
of random agent selection at every time step. Neither alternative incorporates dTS,
only random sampling.
5.4.2. Results
Table 5.1 presents the outcomes of all conducted experiments. The column labeled asStr.
indicates whether the algorithm uses only the baseline policy, which evolves according to
different single-policy techniques (SP), or if the technique is based on utilizing all the pre-
trained policies (MP). Two additional columns indicate whether the techniques require
a change point detection mechanism (column labeled as CHDP) and if the algorithm
performs some kind of additional exploration when running ( Expl.). The table includes
all the techniques used (Methods), along with specific variants in learning rates,γ values,
or other parameters, showcasing the results. The results represent the mean values from
five seeds per experiment, in terms of mean reward ( Reward), mean MtM ( MtM), and
mean absolute inventory value held (|Inv|). Conversely, Figure 5.8 depicts the evolution of
all the different methods throughout the experiments in terms of CUMSUM mean reward
for five different seeds. This figure also illustrates how each technique performs when a
new context is introduced. The best algorithms are less sensitive to very different contexts
than the initial one (such as 5 and 7), while those with the worst performance suffer when
transitioning to these situations.
117

Str. CHDP a Expl. b Methods Reward c MtMc |Inv|c
SP
Single-Policy
0 compets (Baseline) 3240 ± 114 1.14 ± 0.01 323 ± 6
1 compets 3132 ± 831 1.14 ± 0.02 502 ± 337
5 compets 3267 ± 335 1.14 ± 0.02 531 ± 148
7 compets 1531 ± 583 1.07 ± 0.02 884 ± 641
CL-SingleP
lr = 0.1 1923 ± 617 1.09 ± 0.03 466 ± 86
lr = 0.05 3432 ± 1007 1.15 ± 0.04 428 ± 109
CL-FreezingL 3098± 714 1.13 ± 0.03 346 ± 63
CL-Rehearsal 2884± 156 1.15 ± 0.01 723 ± 80
CL-EWC
λ = 0.5 3297 ± 266 1.14 ± 0.01 381 ± 63
λ = 1 3823 ± 292 1.17 ± 0.01 414 ± 24
λ = 10 3120 ± 260 1.14 ± 0.01 371 ± 42
✓ ✓ CL-SingleP (Exp) 156± 229 1.01 ± 0.01 268 ± 274
✓ ✓ CL-FreezingL (Exp) 1405± 381 1.06 ± 0.02 240 ± 37
✓ ✓ CL-Rehearsal (Exp) 2011± 282 1.08 ± 0.01 313 ± 67
✓ ✓ CL-EWC (Exp) 1421± 240 1.06 ± 0.01 222 ± 33
MP
POW-dTS (ours)
αinc=5βinc=5γ=0.4 4354 ± 391 1.19 ± 0.02 483 ± 62
αinc=1βinc=1γ=0.85 4527 ± 135 1.2 ± 0.01 428 ± 19
αinc=1βinc=1γ=0.4 4747 ± 441 1.21 ± 0.02 448 ± 55
αinc=5βinc=5γ=0.85 4360 ± 305 1.19 ± 0.02 479 ± 29
Rand. Agents (abla-
tion)
blocks 4170 ± 166 1.18 ± 0.01 453 ± 9
time steps 3374 ± 41 1.15 ± 0.0 459 ± 8
✓ Benchmark: Optimal-
MP
5254± 100 1.22 ± 0.01 450 ± 8
a
Change point detection needed, b It perform some exploration rounds. c Average values.
Table 5.1: Results of non-stationary M 3ORL MM strategies in terms of rewards, MtM,
and absolute inventory value. POW-dTS obtain the best results in reward and MtM (bold)
after optimal benchmark (italic).
Based on the results presented in Table 5.1 and Figure 5.8, it is evident that POW-dTS
outperforms the other options by a significant margin. It nearly matches the ideal bench-
mark, which represents the best possible outcome aimed to achieve. This observation is
crucial because the benchmark alternative relies on the following assumptions: firstly, a
flawless change point detector that identifies context changes perfectly from the begin-
ning; secondly, an impeccable policy mapping algorithm that assigns the best policy to
each new context starting from the first time step. Our POW-dTS experiments involved
four different setups, varying parameters such as γ in the range{0.4, 0.85} and αinc,β inc
within{1, 5}. These setups exhibited robust behavior, as indicated by the results. As men-
tioned earlier, lower values of γ result in a more forgiving approach to older data, while
118

higher values of αinc and βinc amplify the reinforcement of successes and failures, re-
spectively. The most successful outcomes were associated with αinc,β inc = 1, suggesting
that smoother adjustments of the beta distribution parameters are preferable in the current
environment.
Figure 5.8: Comparison of methods’ performance in terms of accumulated mean rewards
(5 seeds), along all the consecutive di fferent contexts. The POW-dTS algorithm demon-
strates relevant performance across each of the four configurations: αinc and βinc coeffi-
cients, andγ.
Figure 5.9 depicts one round performed by POW-dTS in terms of MtM, using αinc,
βinc = 1, and γ = 0.4. It is worth noting that while these parameters worked well in our
case, they might need adaptation for situations with different levels of volatility.
119

Figure 5.9: The picture illustrates the strong performance of the POW-dTS algorithm in
terms of MtM across various scenarios. The average value (mean (all): 1.22) is close to
the average obtained by optimal-MP. Parameters used:αinc = 1,βinc = 1, andγ = 0.4.
Regarding the CL-SingleP strategy, it is observed that using the default learning rate of
lr = 0.1 leads to inferior results, primarily due to significant catastrophic forgetting, as de-
picted in Figure 5.10. The e ffect of new data on the agent’s NNs, significantly degrading
its performance, is evident. However, employing a lower learning rate, as in CL-SingleP
(lr=0.05), mitigates this adverse e ffect, allowing the policy to surpass the baseline. This
strategy, previously discussed in Section 5.1, presents an interesting approach to circum-
vent this issue.
Figure 5.10: The picture clearly illustrates the impact of a vanilla CL strategy of the
baseline agent with a learning rate of lr =0.1, in terms of MtM (CL-SingleP experiment).
This effect, clearly noticeable in the sequence of contexts 7-1-7-5, is commonly referred
to as catastrophic forgetting. This is due to the loss of previously acquired information in
the NN.
Another well-performing technique, according to the results, is EWC, moreover when
applying aλ = 1. However, this method’s effectiveness is sensitive to the precise selection
of this lambda parameter, as shown by the lower performance under other values.
It is also crucial to highlight the noticeable impact of exploration rounds on the overall
reward for methods that include this action, attributed partially to the decreased returns
during these exploration phases. This effect is depicted in Figure 5.11, demonstrating the
120

anticipated impact of exploration rounds on performance. These additional rounds did
not substantially improve the policy to warrant their inclusion.
Figure 5.11: The CL-EWC-λ1 (exp) experiment’s figure shows the progression of MtM
when employing an EWC strategy with λ = 1. The exploration rounds per context,
marked in yellow, indicate a decline in returns due to this exploration phase. No substan-
tial improvement is observed after these rounds. Additionally, the plot below displays the
ϵ value of the epsilon-greedy strategy executed by the MM.
Next, the pros and cons observed with the POW-dTS algorithm are outlined: Among
its notable strengths, the algorithm demonstrates robust adaptability to unseen contexts
by leveraging knowledge from familiar ones, securing significantly high and optimal re-
turns when compared to other methods. Moreover, it stands out as a computationally
affordable method, offering quick adjustments through TS. Importantly, it operates inde-
pendently of change points or known context transition probabilities/patterns, which pos-
itively affects computational resources while minimizing additional errors. Conversely,
on the downside , it necessitates the periodic evaluation of each agent’s performance,
which could affect overall returns if executed too frequently. Finding a balance between
exploitation and updating phases is critical, varying by the specific environment. Addi-
tionally, precise calibration of αinc and βinc values, along with the γ factor, is essential,
as incorrect parameter settings may negatively impact returns. Another critical point is
POW-dTS’s reliance on pre-trained policies, necessitating prior access to these contexts
for effective agent pre-training. This last aspect makes the method less suitable for sce-
narios encompassing a wide array of contexts.
5.4.3. Ablation study
To analyze the impact of the different components within POW-dTS, two additional exper-
iments were conducted: one retaining the blocks but omitting the dTS part, termed Rand.
Agents (blocks), and another performing random selection of agents at every time step,
named Rand. Agents (timesteps). It is immediately evident that both variants outperform
121

the baseline, suggesting that policy weighting alone is a potent approach in such types of
environments. Moreover, the exceptionally good performance of random agents operating
in blocks is particularly noteworthy. Alternating between different policies while allowing
them to work sequentially significantly enhances performance. This is coherent with the
intrinsic characteristics of RL algorithms, which consider not only immediate rewards but
also future ones. This configuration allows them to exploit certain trajectories, an advan-
tage that the time-step-based alternative lacks. Nonetheless, dTS algorithm shines when
it comes to adjusting the weights according to the agent’s performance, providing a sub-
stantial boost to the solution. The four distinct parameter configurations tested, with αinc
andβinc each set to either 1 or 5, and γ set to either 0.4 or 0.85, have yielded significant
results.
5.5. Discussion
Dealing with non-stationarity is not a trivial task. Financial markets are complex environ-
ments where stationarity is not usually present. In this work, a novel approach to address
this challenge, specifically within the multi-objective market making problem, has been
proposed. Based on experimental results, POW-dTS has proven to be very robust in these
types of tasks. Starting with a set of policies trained di fferently, POW-dTS can assign
weights to them to create composite policies that approximate the optimal scenario. A
key advantage of this method is its independence from identifying change points or map-
ping transition probabilities. This is particularly beneficial as it avoids potential errors
introduced by these techniques and proves advantageous when environmental shifts are
subtle—scenarios where change point detectors may fail. Not to mention the savings in
computational resources typically required by these methods. Additionally, since POW-
dTS relies on a composite policy, it adapts to unknown contexts by selecting the most
effective combination of known policies. This aspect is crucial because known and sta-
ble environments that remain unchanged over time are seldom encountered. It is more
realistic to expect a dynamic environment that evolves. This constant change challenges
the common assumption of context stability required by many algorithms that depend on
change point detection or transition probabilities.
For future work, it is confident that this method can be applied in other domains where
non-stationarity is a significant factor. Notably, heating, ventilation, and air conditioning
systems (HV AC), which require dynamic adjustment to environmental changes and oc-
cupancy patterns, present a promising area for applying our approach. Similarly, energy
trading strategies, where market conditions fluctuate rapidly, could greatly benefit from
the adaptability our method o ffers. Beyond these examples, sectors such as autonomous
vehicles, where conditions change moment-to-moment and adaptive web systems, which
must adjust to user behavior in real time, could also see substantial improvements in effi-
ciency and effectiveness. Investigating these applications further could not only validate
the versatility of this method but also contribute to advancements in these fields.
122

5.6. Contribution
The main contribution of this chapter is addressing the non-stationarity problem in finan-
cial markets faced by MMs through the development of a new algorithm, Policy Weight-
ing through discounted Thompson sampling (POW-dTS). The key aspects of this contri-
bution are enumerated as follows:
1. Innovative algorithm design: Development of POW-dTS, which combines a dy-
namic form of classical TS with policy weighting. This adaptation allows the al-
gorithm to adjust dynamically to the evolving conditions of the markets without
requiring artifacts like change point detectors or prior knowledge of the environ-
ment’s dynamics, such as transition probabilities or reward functions.
2. Comparative analysis with classical techniques: exploration and comparison of
classical training techniques for non-stationary environments. This involves assess-
ing the performance of methods such as EWC, FL, and DR, and comparing these
with the proposed method.
3. Ablation study: Inclusion of an ablation study to evaluate the crucial components
of the proposed algorithm, helping to highlight the contributions of individual ele-
ments to the overall effectiveness of the approach.
4. Evaluation of catastrophic forgetting: Examination of the impact of CF within
these environments, providing insights into how significantly this phenomenon af-
fects the stability and reliability of learning algorithms in non-stationary settings.
5. Broader applicability: While the primary objective is to present a solution for
multi-objective market making within non-stationary markets, the developed method-
ology also has potential applicability to a broader spectrum of tasks requiring flex-
ible and adaptive strategies in environments where non-stationarity is prevalent.
These points collectively underscore the novel approach taken to solve the non-stationarity
problem in financial markets. While the primary objective is to present a solution for
multi-objective market making within non-stationary markets, the methodology devel-
oped has potential applicability to a broader spectrum of tasks that need flexible and
adaptive strategies, where non-stationarity is present.
123

6. CONCLUSION
The dissertation comprehensively addresses the multifaceted challenges of market
making through the innovative application of RL, exploring the evolution from a single-
agent model focused on profitability to a fully autonomous multi-policy system capable
of adapting dynamically to complex and non-stationary financial environments.
Starting with establishing RL in market making: The journey begins with the
foundational exploration of applying deep Q-learning to simulate market making scenar-
ios. This initial approach establishes the viability of RL to inject liquidity and ensure
profitability in simulated stock markets. The focus here is to demonstrate the capacity of
RL agents to learn and adapt strategies, even with additional competitors, without human
intervention, setting a precedent for the subsequent, more complex investigations. And
not only this but also to understand the learned strategies and how these agents perform
when competing against other RL and non-RL MMs.
Advancing to sophisticated inventory management: With the foundation estab-
lished, the journey progresses to address one of the most significant challenges in market
making: inventory management. At this stage, the dissertation introduces two di fferent
approaches. The first strategy, based on reward engineering, represents a major leap from
traditional static models, o ffering enhanced flexibility and risk mitigation. This first de-
velopment implements two dynamic factors in the reward function: the Alpha Inventory
Impact Factor (AIIF) and the Dynamic Inventory Threshold Factor (DITF). These fac-
tors allow the MM to adapt to the evolving situation of its assets, enabling it to manage
inventory risk more dynamically by adjusting the ratio based on the cash-to-inventory
value ratio. This approach is compared to other published alternatives, showcasing better
performance in terms of inventory control, profitability, and risk management.
The second and more advanced approach to dealing with inventory control was based
on the use of a MORL framework. Instead of aggregating both goals (profitability and
inventory control) into one complex reward function, an RL MM with two pairs of NNs
is designed. In this stage, the use of PFs comes into play, o ffering a sophisticated tool
to navigate these trade-offs. This stage of the journey not only highlights the robustness
of multi-objective RL frameworks but also enhances the decision-making process by pro-
viding clear, quantifiable multi-objective metrics for evaluating di fferent strategies. It is
demonstrated how this strategy is more robust and stable, due mainly to the specialization
of the agent on both tasks simultaneously. This phase strengthens the agent’s ability to
operate in a complex decision environment, preparing it for full autonomy.
Culminating in autonomous adaptation:The final leg of the journey brings the most
ambitious and innovative contribution: developing an algorithm capable of autonomously
adapting to non-stationary market conditions. This stage introduces the POW-dTS algo-
rithm, which integrates the TS algorithm with policy weighting. This advancement allows
124

the market making agent to continuously adjust to changing market dynamics with only a
set of different pre-trained policies, demonstrating exceptional adaptability and learning.
Regarding the objectives presented in Section 1.3, it can be asserted that they have
been successfully accomplished. Throughout this dissertation, it has been demonstrated
that RL is a suitable tool for creating market making agents capable of operating in com-
petitive scenarios. Market making agents have been trained not only to evaluate per-
formance in non-competitive scenarios but also to explore the impact of competitors in
terms of MtM and inventory control. Even when applying transfer learning with pre-
trained policies in different environments, their effectiveness has been validated and rele-
vant insights on policy performance have been extracted. This clearly validates the first
objective, evaluate RL for profitable market making in competitive scenarios.
For the second objective, which involves managing inventory while remaining prof-
itable, two different techniques were proposed. First, a reward-engineered agent capable
of dynamically managing inventory based on the cash /inventory value ratio. This ap-
proach was compared to other reward functions from relevant works, achieving better
results in both profitability and inventory management. The dynamic nature of the reward
function, which adapts to the ongoing situation of the MM, allows it to be more aggres-
sive at certain moments without increasing risk. The second approach turned the agent
into a M3ORL MM by separating the reward function into a vector of sub-goals instead of
a single scalar. This approach enabled the agent to learn faster while avoiding the issues
associated with reward engineering. Furthermore, it outperformed the reward-engineered
option in various multi-objective metrics, demonstrating the power of this alternative so-
lution.
Finally, regarding the third objective of dealing with non-stationarity, a novel algo-
rithm called POW-dTS is proposed. This algorithm enables the previous MORL agent
to handle changes in market patterns. By pre-training a set of policies for di fferent sit-
uations, the algorithm modulates each one to best fit the current market. This algorithm
was also compared to di fferent CL techniques, achieving better performance than those.
Additionally, this algorithm can be applied to other use cases where non-stationarity is
present.
To sum up, each stage of the dissertation not only addresses increasingly complex
aspects of market making but also contributes to a holistic understanding of how RL can
be e ffectively applied in financial markets. The journey—from establishing basic RL
applications in market making to developing autonomous agents capable of adapting to
dynamic environments—illustrates a significant evolution in computational finance. This
academic research not only paves the way for future studies but also promises substantial
implications for practical applications in finance.
125

6.1. Limitations of the presented research
In this work, a method for addressing the market making problem from a reinforcement
learning perspective has been presented. However, it is crucial to highlight the limitations
of this approach when considering its application to real markets. Several challenges
must be addressed before these techniques can be effectively implemented in a real-world
trading environment.
All the research has been conducted using ABIDES, a financial market simulator
based on agents’ interaction. It o ffers numerous advantages, such as controlled envi-
ronments and the ability to test multiple scenarios without financial risk. However, the
policies trained in simulators often face significant challenges when transferred to the real
world. Firstly, before applying an agent to a specific financial asset, it is necessary to de-
velop a simulator that closely mirrors the real asset in terms of spreads, volatility, returns,
and other technical indicators. The closer the simulator is to reality, the more accurate the
policies learned by the agent will be. However, despite e fforts to emulate these dynam-
ics, the stochastic nature of financial markets makes them di fficult to replicate with high
fidelity. In other fields, the dynamics can often be derived from known e ffects, such as
physical equations or other well-defined processes, leading to highly accurate simulations.
In contrast, in finance, we face the dual challenge of replicating a stochastic environment
and validating this simulation against real market data. Moreover, markets evolve, with
their dynamics changing in response to various factors, including economic conditions,
geopolitical events, and investor sentiment. This necessitates continuous monitoring of
the simulator’s performance and regular fine-tuning to adapt to these changes, adding
another layer of complexity to the process.
Therefore, the use of simulators to learn trading strategies should be complemented
with other techniques, such as combining real and simulated experiences, using domain
randomization techniques [111] to encourage generalization, or conducting online train-
ing directly in the market. Even when a simulator is validated against a specific asset,
there will always be some discrepancy between simulation and reality. This is where
the concept of Sim2Real [82], [83], short for “simulation to reality” becomes relevant.
Sim2Real focuses on the transfer of skills and models trained in simulation to the real
world. It addresses the challenge of bridging the gap between simulated environments
and real-world conditions with different techniques, which is an essential step for deploy-
ing effective trading strategies.
An alternative approach to overcoming the limitations of simulation-based training is
to train RL agents directly in the market using online learning. While this method circum-
vents some of the issues associated with simulators, it introduces new challenges. Online
training has two main disadvantages compared to simulation: the speed of training and
the associated costs. In simulators, training times can be significantly reduced, as they
are limited only by computational power and the e fficiency of the simulation environ-
ment. In contrast, real-world training relies on the availability of data in real-time, which
126

imposes a clear constraint on training speed. Regarding costs, training agents directly in
the market incurs various expenses, such as transaction fees, slippage, and the cost of op-
erational errors. Depending on the strategy being developed, these costs can range from
manageable to prohibitive. For high-frequency or complex strategies, the financial impact
of errors or suboptimal decisions during training can be substantial.
To summarize, while RL-based methods hold promise for market making and other
financial applications, their deployment in real markets requires careful consideration of
the limitations of simulation, the need for robust validation techniques, and the practi-
cal challenges of online learning. A combination of simulation, real-world testing, and
advanced adaptation strategies is essential for developing e ffective and resilient trading
systems.
6.2. Future work
This section highlights several key areas that are worth further exploration as part of
future work. The first Subsection 6.2.1 delves into strategies for addressing the limitations
of the current method, o ffering potential alternatives and improvements to enhance its
performance. Next, Subsection 6.2.2 explores the role of large language models (LLMs)
in solving the MM problem, showcasing their potential not only in this specific context
but also in broader applications within trading.
6.2.1. Future directions in simulated and real-world market making
The foundation of a robust approach to market making through the use of RL has been es-
tablished. Although all research thus far has utilized a market simulator, significant work
remains before these methods can be applied in the real world. If the goal is to pre-train a
MM agent in a simulated stock market before transferring the learning to the real world,
it is crucial to replicate a similar simulated environment. Therefore, developing methods
that assist in the creation and validation of these simulators is a critical line of research.
Ensuring that the simulator closely resembles the asset intended for operation is essential.
Designing agents and similarity metrics that align with real price movements is a complex
task, but it is necessary for effective MM training in a simulated environment. Addition-
ally, bridging the gap between simulated and real environments (Sim2Real) is a key
requirement. Exploring different techniques to address this challenge is an important step
before deploying the agent in the real world [112], [113].
Conversely, if the option is to bypass simulators and directly learn policies in the
real environment, this approach typically incurs higher costs, in addition to increased
training times. For online training, a more cautious learning policy must be designed to
minimize potential financial losses while still enabling effective learning. Therefore, safe
RL learning techniques [114] should be explored or proposed to allow the agent to learn
127

directly in real markets in a safe manner. This could undoubtedly be an additional line of
research.
Regarding other algorithms, other lines of work can also be pursued. In the area of
dealing with non-stationarity, some interesting algorithms can be tested and compared to
our solution. One similar approach presented in this thesis is called Probabilistic Policy
Reuse in a RL Agent [115], where the authors select the current policy of the agent ac-
cording to a probabilistic method. This method shares some common points with our ap-
proach, and it would be interesting to compare it with POW-dTS in terms of performance.
Additionally, there are other methods not tested, which rely on changepoint detectors,
such as [44]. Changepoint detectors, such as ODCP5 or ECP6, which have to be correctly
tuned, introduce uncertainty into the algorithm, as they need to be robustly trained to
avoid false positives and false negatives, especially when changes in the environment are
not abrupt. However, this could be an interesting line of work, not only related to testing
these types of algorithms but also to designing robust changepoint detectors, which is a
matter of research itself.
6.2.2. LLMs and their application in trading strategies
Large Language Models (LLMs) [116] have undoubtedly opened a new universe of pos-
sibilities in machine learning. Their ability to process vast amounts of information and
extract relationships from data has enabled new capabilities across various domains. De-
signing trading and, therefore, market making strategies that benefit from these capabil-
ities is an important area of research and deserves a brief analysis. In this regard, two
main groups of applications can be explored: LLMs integrated with RL and LLMs apart
from RL. Regarding LLMs integrated with RL, the combination of RL and LLMs can
enhance agents in many ways. For instance, LLMs can improve the state space by incor-
porating new information directly from their outputs. The order book can be tokenized
as a sequence of text, allowing the LLM to extract relevant information, or other types
of unstructured data—such as news, events, tweets, and sentiment—can be incorporated.
Furthermore, multimodal LLMs [117] (models that accept not only text but also images
or other types of inputs) can be used to include visual elements like order book snap-
shots, candlestick patterns, or other technical information, enriching the state information
gathered from the environment. Another potential application of LLMs in RL is using
transformer layers (the main component of LLMs) in value or policy neural networks
to infer complex patterns. By integrating transformer architectures, the RL agent may
capture long-range dependencies and complex temporal patterns in market data, thereby
enhancing its decision-making capabilities. In addition, incorporating risk assessments
generated by LLMs into the RL framework can lead to more robust trading strategies. For
example, LLMs can analyze textual data to estimate market volatility or detect potential
5Online Parametric Dirichlet Changepoint
6E-Divisive Change Point detection
128

black swan events[118], which the RL agent can use to adjust its policy accordingly.
Additionally, LLMs can also be used as standalone agents, apart from RL. These
agents could operate based on various inputs, including the unstructured data mentioned
earlier, and can be tested or fine-tuned according to specific requirements. They can act
as ‘intelligent’ competitors in simulations, increasing the complexity of simulated mar-
kets and resulting in more robust policies. Finally, LLMs can also be used more broadly,
such as to predict market trends or generate trading signals based on textual data. For in-
stance, LLMs can process earnings call transcripts to predict stock movements or potential
impacts, which can then inform trading decisions or be used as input for other models.
Additionally, LLMs can be used to generate synthetic financial data to augment training
datasets, improving the robustness of trading algorithms, especially when historical data
is limited. They could even generate plausible market scenarios or price movements.
All of these are examples of potential applications where LLMs can positively impact
trading and market making strategies, making them worth exploring.
129

BIBLIOGRAPHY
[1] T. Hendershott, “Electronic trading in financial markets,” IT Professional Maga-
zine, vol. 5, no. 4, p. 10, 2003.
[2] G. Huberman, “A simple approach to arbitrage pricing theory,” in Theory of Val-
uation, World Scientific, 2005, pp. 289–308. doi: 10.1142/9789812701022_
0009.
[3] T. Chordia, A. Goyal, B. N. Lehmann, and G. Saar, “High-frequency trading,”
SSRN Electronic Journal, 2013. doi: 10.2139/ssrn.2278347.
[4] T. Chakraborty and M. Kearns, “Market making and mean reversion,” 2011, pp. 307–
313. doi: 10.1145/1993574.1993622.
[5] AlphaTrade, List of u.s. market makers , https : / / web . archive . org / web /
20090122074413/http://www.alphatrade.com/techSupport/marketMakers.
html, Archived from the original on 2009-01-22. Retrieved 2008-10-31.
[6] AlphaTrade, List of market makers in canada , https://web.archive.org/
web / 20070109084732 / http : / / www . alphatrade . com / techSupport /
canadianIDs.html, Archived from the original on 2007-01-09. Retrieved 2008-
10-31.
[7] T. E. Copeland and D. Galai, “Information e ffects on the bid-ask spread,” The
Journal of Finance, vol. 38, no. 5, pp. 1457–1469, 1983. doi: 10.1111/j.1540-
6261.1983.tb03834.x.
[8] R. S. Sutton and A. G. Barto, Reinforcement Learning: An Introduction, Second.
Cambridge: The MIT Press, 2018.
[9] M. Hussain, “Can alphago be apt subjects for praise /blame for "move 37"?” In
Proceedings of the 2023 AAAI/ACM Conference on AI, Ethics, and Society, ser. AIES
’23, Montreal, Canada: Association for Computing Machinery, 2023, pp. 977–
979. doi: 10 . 1145 / 3600211 . 3604730. [Online]. Available: https : / / doi .
org/10.1145/3600211.3604730.
[10] C. Watkins, “Learning from delayed rewards,” Ph.D. dissertation, King’s College,
Cambridge, UK, 1989.
[11] W. Fedus et al., “Revisiting fundamentals of experience replay,” inProceedings of
the 37th International Conference on Machine Learning, H. D. III and A. Singh,
Eds., ser. Proceedings of Machine Learning Research, vol. 119, PMLR, 2020,
pp. 3061–3071. [Online]. Available: https : / / proceedings . mlr . press /
v119/fedus20a.html.
130

[12] A. Adadi and M. Berrada, “Peeking inside the black-box: A survey on explainable
artificial intelligence (xai),” IEEE Access, vol. 6, pp. 52 138–52 160, 2018. doi:
10.1109/ACCESS.2018.2870052.
[13] R. J. Williams, “Simple statistical gradient-following algorithms for connectionist
reinforcement learning,” Machine Learning, vol. 8, pp. 229–256, 1992.
[14] T. Haarnoja, A. Zhou, P. Abbeel, and S. Levine, “Soft actor-critic: O ff-policy
maximum entropy deep reinforcement learning with a stochastic actor,” in In-
ternational conference on machine learning, PMLR, 2018, pp. 1861–1870.
[15] J. Schulman, F. Wolski, P. Dhariwal, A. Radford, and O. Klimov, “Proximal policy
optimization algorithms,” CoRR, vol. abs/1707.06347, 2017. arXiv:1707.06347.
[Online]. Available: http://arxiv.org/abs/1707.06347.
[16] C. B. Browne et al., “A survey of monte carlo tree search methods,” IEEE Trans-
actions on Computational Intelligence and AI in games , vol. 4, no. 1, pp. 1–43,
2012.
[17] V . Mnih et al., “Human-level control through deep reinforcement learning,” Na-
ture, vol. 518, pp. 529–533, 7540 Feb. 2015. doi: 10.1038/nature14236.
[18] D. M. Roijers, P. Vamplew, S. Whiteson, and R. Dazeley, “A survey of multi-
objective sequential decision-making,”Journal of Artificial Intelligence Research,
vol. 48, pp. 67–113, 2013.
[19] Y . Jin, Multi-objective machine learning . Springer Science & Business Media,
2006, vol. 16.
[20] K. Deb, K. Sindhya, and J. Hakanen, “Multi-objective optimization,” in Decision
sciences, CRC Press, 2016, pp. 161–200.
[21] T. T. Nguyen, N. D. Nguyen, P. Vamplew, S. Nahavandi, R. Dazeley, and C. P.
Lim, “A multi-objective deep reinforcement learning framework,” Engineering
Applications of Artificial Intelligence, vol. 96, p. 103 915, 2020.
[22] K. Van Mo ffaert and A. Nowé, “Multi-objective reinforcement learning using
sets of pareto dominating policies,” The Journal of Machine Learning Research,
vol. 15, no. 1, pp. 3483–3512, 2014.
[23] C. F. Hayes et al., “A practical guide to multi-objective reinforcement learning
and planning,” Autonomous Agents and Multi-Agent Systems, vol. 36, no. 1, p. 26,
Apr. 2022. doi: 10.1007/s10458-022-09552-y . [Online]. Available: https:
//doi.org/10.1007/s10458-022-09552-y.
[24] D. Dewey, “Reinforcement learning and the reward engineering principle,” in
2014 AAAI Spring Symposium Series, 2014. [Online]. Available:https://aaai.
org/papers/07704-7704-reinforcement-learning-and-the-reward-
engineering-principle/.
131

[25] J. Eschmann, “Reward function design in reinforcement learning,” in Reinforce-
ment Learning Algorithms: Analysis and Applications . Cham: Springer Interna-
tional Publishing, 2021, pp. 25–33. doi: 10.1007/978- 3- 030- 41188- 6_3 .
[Online]. Available: https://doi.org/10.1007/978-3-030-41188-6_3 .
[26] P. Vamplew et al., “Scalar reward is not enough: A response to silver, singh, pre-
cup and sutton (2021),” Autonomous Agents and Multi-Agent Systems , vol. 36,
no. 2, p. 41, 2022.
[27] J. García, R. Iglesias, M. A. Rodríguez, and C. V . Regueiro, “Incremental rein-
forcement learning for multi-objective robotic tasks,”Knowledge and Information
Systems, vol. 51, pp. 911–940, 2017.
[28] H. Yoo, V . M. Zavala, and J. H. Lee, “A dynamic penalty function approach
for constraint-handling in reinforcement learning,” IFAC-PapersOnLine, vol. 54,
no. 3, pp. 487–491, 2021, 16th IFAC Symposium on Advanced Control of Chem-
ical Processes ADCHEM 2021. doi: https://doi.org/10.1016/j.ifacol.
2021 . 08 . 289. [Online]. Available: https : / / www . sciencedirect . com /
science/article/pii/S2405896321010624.
[29] N. J. Zakaria, M. I. Shapiai, and N. Wahid, “A study of multiple reward function
performances for vehicle collision avoidance systems applying the dqn algorithm
in reinforcement learning,” IOP Conference Series: Materials Science and Engi-
neering, vol. 1176, no. 1, p. 012 033, Aug. 2021. doi: 10.1088/1757- 899X/
1176/1/012033. [Online]. Available: https://dx.doi.org/10.1088/1757-
899X/1176/1/012033.
[30] J. García, R. Majadas, and F. Fernández, “Learning adversarial attack policies
through multi-objective reinforcement learning,”Engineering Applications of Ar-
tificial Intelligence, vol. 96, p. 104 021, 2020.doi: 10.1016/j.engappai.2020.
104021. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S0952197620303043.
[31] P. Ngatchou, A. Zarei, and A. El-Sharkawi, “Pareto multi objective optimization,”
in Proceedings of the 13th international conference on, intelligent systems appli-
cation to power systems , IEEE, 2005, pp. 84–91. doi: 10 . 1109 / ISAP . 2005 .
1599231.
[32] X. Li and A. Krause, “An evolutionary multi-objective optimization of market
structures using pbil,” in Intelligent Data Engineering and Automated Learning
– IDEAL 2010, C. Fyfe, P. Tino, D. Charles, C. Garcia-Osorio, and H. Yin, Eds.,
Berlin, Heidelberg: Springer Berlin Heidelberg, 2010, pp. 78–85.
[33] P. Ngatchou, A. Zarei, and A. El-Sharkawi, “Pareto multi objective optimization,”
in Proceedings of the 13th International Conference on, Intelligent Systems Appli-
cation to Power Systems, 2005, pp. 84–91. doi: 10.1109/ISAP.2005.1599245.
132

[34] Y . Tian, X. Xiang, X. Zhang, R. Cheng, and Y . Jin, “Sampling reference points on
the pareto fronts of benchmark multi-objective optimization problems,” in 2018
IEEE Congress on Evolutionary Computation (CEC) , 2018, pp. 1–6. doi: 10 .
1109/CEC.2018.8477730.
[35] R. Tanabe and H. Ishibuchi, “An easy-to-use real-world multi-objective opti-
mization problem suite,” Applied Soft Computing, vol. 89, p. 106 078, 2020. doi:
https : / / doi . org / 10 . 1016 / j . asoc . 2020 . 106078. [Online]. Available:
https://www.sciencedirect.com/science/article/pii/S1568494620300181.
[36] S. Padakandla, “A survey of reinforcement learning algorithms for dynamically
varying environments,” ACM Comput. Surv., vol. 54, no. 6, Jul. 2021. doi: 10.
1145/3459991. [Online]. Available: https://doi.org/10.1145/3459991.
[37] S. Abdallah and M. Kaisers, “Addressing environment non-stationarity by repeat-
ing q-learning updates,” Journal of Machine Learning Research, vol. 17, no. 46,
pp. 1–31, 2016. [Online]. Available: http : / / jmlr . org / papers / v17 / 14 -
037.html.
[38] I. Noda, “Recursive adaptation of stepsize parameter for non-stationary environ-
ments,” in Principles of Practice in Multi-Agent Systems , J.-J. Yang, M. Yokoo,
T. Ito, Z. Jin, and P. Scerri, Eds., Berlin, Heidelberg: Springer Berlin Heidelberg,
2009, pp. 525–533. doi: https://doi.org/10.1007/978- 3- 642- 11814-
2_5.
[39] A. P. George and W. B. Powell, “Adaptive stepsizes for recursive estimation with
applications in approximate dynamic programming,” Machine learning, vol. 65,
pp. 167–198, 2006. doi: https://doi.org/10.1007/s10994-006-8365-9.
[40] X. Wu, H. Chen, J. Wang, L. Troiano, V . Loia, and H. Fujita, “Adaptive stock trad-
ing strategies with deep reinforcement learning methods,” Information Sciences,
vol. 538, pp. 142–158, 2020. doi: https://doi.org/10.1016/j.ins.2020.
05.066. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S0020025520304692.
[41] B. C. da Silva, E. W. Basso, F. S. Perotto, A. L. C. Bazzan, and P. M. Engel,
“Improving reinforcement learning with context detection,” inProceedings of the
Fifth International Joint Conference on Autonomous Agents and Multiagent Sys-
tems, ser. AAMAS ’06, Hakodate, Japan: Association for Computing Machinery,
2006, pp. 810–812. doi: 10.1145/1160633.1160779.
[42] E. Hadoux, A. Beynier, and P. Weng, “Sequential decision-making under non-
stationary environments via sequential change-point detection,” in Learning over
Multiple Contexts (LMCE), Nancy, France, Sep. 2014. [Online]. Available:https:
//hal.science/hal-01200817.
133

[43] S. P. M. Choi, D.-Y . Yeung, and N. L. Zhang, “Hidden-mode markov decision
processes for nonstationary sequential decision making,” in Sequence Learning:
Paradigms, Algorithms, and Applications , R. Sun and C. L. Giles, Eds. Berlin,
Heidelberg: Springer Berlin Heidelberg, 2001, pp. 264–287. doi: 10.1007/3-
540-44565-X\_12.
[44] S. Padakandla, P. K. J, and S. Bhatnagar, “Reinforcement learning in non-stationary
environments,” May 2019. doi: 10 . 1007 / s10489 - 020 - 01758 - 5. [Online].
Available: http://arxiv.org/abs/1905.03970%20http://dx.doi.org/
10.1007/s10489-020-01758-5.
[45] P. K. J., N. Singh, P. Dayama, A. Agarwal, and V . Pandit, “Change point de-
tection for compositional multivariate data,” Applied Intelligence, vol. 52, no. 2,
pp. 1930–1955, Jan. 2022. doi: 10 . 1007 / s10489 - 021 - 02321 - 6. [Online].
Available: https://doi.org/10.1007/s10489-021-02321-6.
[46] M. D. Lange et al., “A continual learning survey: Defying forgetting in classifica-
tion tasks,” IEEE Transactions on Pattern Analysis; Machine Intelligence, vol. 44,
pp. 3366–3385, 07 Jul. 2022. doi: 10.1109/TPAMI.2021.3057446.
[47] Z. Chen and B. Liu, “Continual learning and catastrophic forgetting,” in Lifelong
Machine Learning. Cham: Springer International Publishing, 2018, pp. 55–75.
doi: 10.1007/978-3-031-01581-6\_4 .
[48] R. M. French, “Catastrophic forgetting in connectionist networks,” Trends in Cog-
nitive Sciences , vol. 3, no. 4, pp. 128–135, 1999. doi: https : / / doi . org /
10 . 1016 / S1364 - 6613(99 ) 01294 - 2. [Online]. Available: https : / / www .
sciencedirect.com/science/article/pii/S1364661399012942.
[49] A. Sorrenti, G. Bellitto, F. Salanitri, M. Pennisi, C. Spampinato, and S. Palazzo,
“Selective freezing for efficient continual learning,” IEEE Computer Society, Oct.
2023, pp. 3542–3551. doi: 10 . 1109 / ICCVW60793 . 2023 . 00381. [Online].
Available:https://doi.ieeecomputersociety.org/10.1109/ICCVW60793.
2023.00381.
[50] A. Robins, “Catastrophic forgetting, rehearsal and pseudorehearsal,” Connection
Science, vol. 7, pp. 123–146, 2 1995. doi: 10.1080/09540099550039318. [On-
line]. Available: https://doi.org/10.1080/09540099550039318.
[51] P. Buzzega, M. Boschini, A. Porrello, and S. Calderara, “Rethinking experience
replay: A bag of tricks for continual learning,” in2020 25th International Confer-
ence on Pattern Recognition (ICPR) , Los Alamitos, CA, USA: IEEE Computer
Society, Jan. 2021, pp. 2180–2187. doi: 10.1109/ICPR48806.2021.9412614.
[52] C. Atkinson, B. McCane, L. Szymanski, and A. Robins, “Pseudo-rehearsal: Achiev-
ing deep reinforcement learning without catastrophic forgetting,” Neurocomput-
ing, vol. 428, pp. 291–307, 2021.doi: https://doi.org/10.1016/j.neucom.
2020 . 11 . 050. [Online]. Available: https : / / www . sciencedirect . com /
science/article/pii/S0925231220318439.
134

[53] J. Kirkpatrick et al., “Overcoming catastrophic forgetting in neural networks,”
Proceedings of the National Academy of Sciences , vol. 114, no. 13, pp. 3521–
3526, 2017. doi: 10.1073/pnas.1611835114 . eprint: https://www.pnas.
org / doi / pdf / 10 . 1073 / pnas . 1611835114. [Online]. Available: https :
//www.pnas.org/doi/abs/10.1073/pnas.1611835114.
[54] X. Lu and F. Abergel, “Order-book modelling and market making strategies,” Jun.
2018. [Online]. Available: http://arxiv.org/abs/1806.05101.
[55] R. Manuca and R. Savit, “Stationarity and nonstationarity in time series analysis,”
Physica D: Nonlinear Phenomena, vol. 99, no. 2, pp. 134–161, 1996.doi: https:
//doi.org/10.1016/S0167-2789(96)00139-X. [Online]. Available: https:
//www.sciencedirect.com/science/article/pii/S016727899600139X.
[56] J. L. McCauley, “Nonstationarity of e fficient finance markets: Fx market evolution
from stability to instability,” International Review of Financial Analysis, vol. 17,
no. 5, pp. 820–837, 2008. doi: https://doi.org/10.1016/j.irfa.2008.
02.004. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S1057521908000045.
[57] P. F. Procacci, “Non stationarity and market structure dynamics in financial time
series,” Ph.D. dissertation, UCL (University College London), 2023.
[58] T. A. Schmitt, D. Chetalova, R. Schäfer, and T. Guhr, “Non-stationarity in finan-
cial time series: Generic features and tail behavior,”Europhysics Letters, vol. 103,
no. 5, p. 58 003, Sep. 2013. doi: 10.1209/0295- 5075/103/58003 . [Online].
Available: https://dx.doi.org/10.1209/0295-5075/103/58003.
[59] T. H. McInish, B. F. Van Ness, and R. A. Van Ness, “After-hours trading of nyse
stocks on the regional stock exchanges,” Review of Financial Economics, vol. 11,
no. 4, pp. 287–297, 2002. doi: https://doi.org/10.1016/S1058-3300(02)
00060-5. [Online]. Available: https://www.sciencedirect.com/science/
article/pii/S1058330002000605.
[60] T. Oberlechner and S. Hocking, “Information sources, news, and rumors in fi-
nancial markets: Insights into the foreign exchange market,” Journal of Eco-
nomic Psychology, vol. 25, no. 3, pp. 407–424, 2004. doi: https://doi.org/
10 . 1016 / S0167 - 4870(02 ) 00189 - 7. [Online]. Available: https : / / www .
sciencedirect.com/science/article/pii/S0167487002001897.
[61] N. Strauß, R. Vliegenthart, and P. Verhoeven, “Intraday news trading: The recipro-
cal relationships between the stock market and economic news,” Communication
Research, vol. 45, no. 7, pp. 1054–1077, 2018, PMID: 30443092. doi: 10.1177/
0093650217705528. eprint: https://doi.org/10.1177/0093650217705528.
[Online]. Available: https://doi.org/10.1177/0093650217705528.
[62] M. Avellaneda and S. Stoikov, “High-frequency trading in a limit order book,”
Quantitative Finance, vol. 8, pp. 217–224, 3 Apr. 2008.doi: 10.1080/14697680701381228.
135

[63] T. Ho and H. R. Stoll, “Optimal dealer pricing under transactions and return un-
certainty,” Journal of Financial Economics , vol. 9, no. 1, pp. 47–73, 1981. doi:
10.1016/0304-405X(81)90020-9.
[64] O. Guéant, C.-A. Lehalle, and J. F. Tapia, “Dealing with the inventory risk. a
solution to the market making problem,” Mathematics and Financial Economics,
May 2011. doi: 10.1007/s11579-012-0087-0.
[65] O. Guéant, “Optimal market making,” Applied Mathematical Finance , vol. 24,
no. 2, pp. 112–154, Aug. 2017. doi: 10.1080/1350486X.2017.1342552 . [On-
line]. Available: https://hal.archives-ouvertes.fr/hal-02862554.
[66] Y . Ait-Sahalia and M. Saalam, “High frequency market making: Implications for
liquidity,” SSRN Electronic Journal, 2017. doi: 10.2139/ssrn.2908438.
[67] X. Li, X. Deng, S. Zhu, F. Wang, and H. Xie, “An intelligent market making
strategy in algorithmic trading,” Front. Comput. Sci., vol. 8, no. 4, pp. 596–608,
Aug. 2014. doi: 10.1007/s11704-014-3312-6.
[68] M. F. Dixon, “High frequency market making with machine learning,” SSRN
Electronic Journal, 2017. doi: 10.2139/ssrn.2868473.
[69] N. T. Chan and C. Shelton, “An electronic market-maker,” 2001.
[70] Y . Patel, “Optimizing market making using multi-agent reinforcement learning,”
Dec. 2018. [Online]. Available: http://arxiv.org/abs/1812.10252.
[71] T. Spooner, J. Fearnley, R. Savani, and A. Koukorinis, “Market making via rein-
forcement learning,” AAMAS ’18, pp. 434–442, Apr. 2018. [Online]. Available:
http://arxiv.org/abs/1804.04216.
[72] K. Lokhacheva, D. Parfenov, and I. Bolodurina, “Reinforcement learning ap-
proach for market-maker problem solution,” in Proceedings of the International
Session on Factors of Regional Extensive Development (FRED 2019) , Atlantis
Press, 2020, pp. 256–260. doi: 10.2991/fred-19.2020.52.
[73] Y . Wang, H. Zhou, and W. Zeng, “The agent-based simulation of inventory-based
model’s impact on market maker trading mechanism,” 2011, pp. 601–604. doi:
10.1109/IWACI.2011.6160079.
[74] S. Ganesh, N. Vadori, M. Xu, H. Zheng, P. Reddy, and M. Veloso, “Reinforcement
learning for market making in a multi-agent dealer market,” Nov. 2019. [Online].
Available: http://arxiv.org/abs/1911.05892.
[75] D. Byrd, M. Hybinette, and T. H. Balch, “Abides: Towards high-fidelity market
simulation for ai research,” SIGSIM-PADS ’20, pp. 11–22, Apr. 2019. doi: 10.
1145 / 3384441 . 3395986. [Online]. Available: http : / / arxiv . org / abs /
1904.12066.
136

[76] Y . Zhong, Y . Bergstrom, and A. Ward, “Data-driven market-making via model-
free learning,” in Proceedings of the Twenty-Ninth International Joint Conference
on Artificial Intelligence, IJCAI-20, C. Bessiere, Ed., Special Track on AI in Fin-
Tech, International Joint Conferences on Artificial Intelligence Organization, Jul.
2020, pp. 4461–4468. doi: 10.24963/ijcai.2020/615.
[77] M. Selser, J. Kreiner, and M. Maurette, “Optimal market making by reinforcement
learning,” SSRN Electronic Journal, 2021. doi: 10.2139/ssrn.3829984.
[78] B. Gasperov and Z. Kostanjcar, “Market making with signals through deep re-
inforcement learning,” IEEE Access, vol. 9, pp. 61 611–61 622, 2021. doi: 10 .
1109/ACCESS.2021.3074782.
[79] Y .-S. Lim and D. Gorse, Reinforcement learning for high-frequency market mak-
ing. 26th European Symposium on Artificial Neural Networks, Computational
Intelligence and Machine Learning ESANN 2018 : Bruges, Belgium, April 25,
26, 27, 2018 : proceedings, 2018. [Online]. Available: https://www.esann.
org/sites/default/files/proceedings/legacy/es2018-50.pdf.
[80] G. Zhang and Y . Chen, “Reinforcement learning for optimal market making with
the presence of rebate,” SSRN Electronic Journal, 2020. doi: 10.2139/ssrn.
3646753.
[81] M. A. Mani and S. Phelps, “Applications of reinforcement learning in automated
market-making,” in GAIW, May 2019, Montreal, Canada, 2019. [Online]. Avail-
able: https://nms.kcl.ac.uk/simon.parsons/publications/conferences/
gaiw19.pdf.
[82] X. B. Peng, M. Andrychowicz, W. Zaremba, and P. Abbeel, “Sim-to-real trans-
fer of robotic control with dynamics randomization,” in 2018 IEEE International
Conference on Robotics and Automation (ICRA), Brisbane, Australia: IEEE Press,
2018, pp. 1–8. doi: 10.1109/ICRA.2018.8460528. [Online]. Available:https:
//doi.org/10.1109/ICRA.2018.8460528.
[83] S. Hofer et al. , “Sim2real in robotics and automation: Applications and chal-
lenges,” IEEE transactions on automation science and engineering, vol. 18, no. 2,
pp. 398–400, 2021.
[84] S. Amrouni, A. Moulin, J. Vann, S. Vyetrenko, T. Balch, and M. Veloso, “Abides-
gym: Gym environments for multi-agent discrete event simulation and application
to financial markets,” in Proceedings of the Second ACM International Confer-
ence on AI in Finance, ser. ICAIF ’21, Virtual Event: Association for Computing
Machinery, 2022. doi: 10.1145/3490354.3494433.
[85] S. A. Assefa, D. Dervovic, M. Mahfouz, R. E. Tillman, P. Reddy, and M. Veloso,
“Generating synthetic data in finance: Opportunities, challenges and pitfalls,” in
Generating Synthetic Data in Finance: Opportunities, Challenges and Pitfalls ,
ser. ICAIF ’20, New York, New York: Association for Computing Machinery,
2021. doi: 10.1145/3383455.3422554.
137

[86] C.-H. Kuo, C.-T. Chen, S.-J. Lin, and S.-H. Huang, “Improving generalization
in reinforcement learning–based trading by using a generative adversarial market
model,” IEEE Access, vol. 9, pp. 50 738–50 754, 2021. doi: 10.1109/ACCESS.
2021.3068269.
[87] Z. Zhang, B. Lim, and S. Zohren, “Deep learning for market by order data,” Ap-
plied Mathematical Finance , vol. 28, no. 1, pp. 79–95, 2021. doi: 10 . 1080 /
1350486X.2021.1967767.
[88] S. Ganesh, N. Vadori, M. Xu, H. Zheng, P. P. Reddy, and M. M. Veloso, “Re-
inforcement learning for market making in a multi-agent dealer market,” ArXiv,
vol. abs/1911.05892, 2019.
[89] P. Vamplew, R. Dazeley, A. Berry, R. Issabekov, and E. Dekker, “Empirical eval-
uation methods for multiobjective reinforcement learning algorithms,” Machine
Learning, vol. 84, no. 1, pp. 51–80, Jul. 2011. doi: 10 . 1007 / s10994 - 010 -
5232 - 5. [Online]. Available: https : / / doi . org / 10 . 1007 / s10994 - 010 -
5232-5.
[90] Ó. F. Vicente, F. Fernández, and J. García, “Automated market maker inventory
management with deep reinforcement learning,” Applied Intelligence, 2023. doi:
10.1007/s10489-023-04647-9. [Online]. Available: https://doi.org/10.
1007/s10489-023-04647-9.
[91] D. Cournapeau, Scikit-learn (machine learning in python), https://scikit-learn.org/stable/,
2007.
[92] S. Lundberg, Shap (shapley additive explanations), https://shap.readthedocs.io/en/latest/index.html,
2018.
[93] P. Mallozzi, R. Pardo, V . Duplessis, P. Pelliccione, and G. Schneider, “Movemo:
A structured approach for engineering reward functions,” in 2018 Second IEEE
International Conference on Robotic Computing (IRC) , 2018, pp. 250–257. doi:
10.1109/IRC.2018.00053.
[94] A. Hussein, E. Elyan, M. M. Gaber, and C. Jayne, “Deep reward shaping from
demonstrations,” in 2017 International Joint Conference on Neural Networks
(IJCNN), 2017, pp. 510–517. doi: 10.1109/IJCNN.2017.7965896.
[95] S. Adams, T. Cody, and P. A. Beling, “A survey of inverse reinforcement learn-
ing,” Artificial Intelligence Review , Aug. 2022. doi: 10 . 1007 / s10462 - 021 -
10108-x.
[96] P. Behboudian, Y . Satsangi, M. E. Taylor, A. Harutyunyan, and M. Bowling, “Pol-
icy invariant explicit shaping: An e fficient alternative to reward shaping,” Neu-
ral Computing and Applications , vol. 34, no. 3, pp. 1673–1686, Feb. 2022. doi:
10.1007/s00521-021-06259-1.
138

[97] A. C. Szakmary, Q. Shen, and S. C. Sharma, “Trend-following trading strategies
in commodity futures: A re-examination,”Journal of Banking& Finance, vol. 34,
no. 2, pp. 409–426, 2010. doi: https://doi.org/10.1016/j.jbankfin.
2009 . 08 . 004. [Online]. Available: https : / / www . sciencedirect . com /
science/article/pii/S037842660900199X.
[98] J. Rohrbach, S. Suremann, and J. Osterrieder, “Momentum and trend follow-
ing trading strategies for currencies revisited-combining academia and industry,”
Available at SSRN 2949379, 2017.
[99] S. Fong and J. Tai, “The application of trend following strategies in stock market
trading,” in 2009 Fifth International Joint Conference on INC, IMS and IDC ,
2009, pp. 1971–1976. doi: 10.1109/NCM.2009.402.
[100] P. Vamplew, J. Yearwood, R. Dazeley, and A. Berry, “On the limitations of scalar-
isation for multi-objective reinforcement learning of pareto fronts,” in AI 2008:
Advances in Artificial Intelligence, W. Wobcke and M. Zhang, Eds., Berlin, Hei-
delberg: Springer Berlin Heidelberg, 2008, pp. 372–378. doi: https : / / doi .
org/10.1007/978-3-540-89378-3 .
[101] N. Riquelme, C. V on Lücken, and B. Baran, “Performance metrics in multi-objective
optimization,” in 2015 Latin American Computing Conference (CLEI), 2015, pp. 1–
11. doi: 10.1109/CLEI.2015.7360024.
[102] J. García, R. Iglesias, M. A. Rodríguez, and C. V . Regueiro, “Directed exploration
in black-box optimization for multi-objective reinforcement learning,” Interna-
tional Journal of Information Technology & Decision Making, vol. 18, no. 03,
pp. 1045–1082, 2019. doi: 10 . 1142 / S0219622019500093. eprint: https :
/ / doi . org / 10 . 1142 / S0219622019500093. [Online]. Available: https :
//doi.org/10.1142/S0219622019500093.
[103] I. Demir, F. C. Ergin, and B. Kiraz, “A new model for the multi-objective mul-
tiple allocation hub network design and routing problem,” IEEE Access, vol. 7,
pp. 90 678–90 689, 2019.doi: 10.1109/ACCESS.2019.2927418.
[104] K. Deb and K. Deb, “Multi-objective optimization,” in Search Methodologies:
Introductory Tutorials in Optimization and Decision Support Techniques. Boston,
MA: Springer US, 2014, pp. 403–449. doi: 10.1007/978-1-4614-6940-7_15 .
[Online]. Available: https://doi.org/10.1007/978-1-4614-6940-7_15 .
[105] T. Schaul, D. Horgan, K. Gregor, and D. Silver, “Universal value function ap-
proximators,” in Proceedings of the 32nd International Conference on Machine
Learning, F. Bach and D. Blei, Eds., ser. Proceedings of Machine Learning Re-
search, vol. 37, Lille, France: PMLR, Jul. 2015, pp. 1312–1320. [Online]. Avail-
able: https://proceedings.mlr.press/v37/schaul15.html.
139

[106] Z. Shen, Z. Liu, J. Qin, M. Savvides, and K.-T. Cheng, “Partial is better than all:
Revisiting fine-tuning strategy for few-shot learning,” Proceedings of the AAAI
Conference on Artificial Intelligence, vol. 35, no. 11, pp. 9594–9602, May 2021.
doi: 10.1609/aaai.v35i11.17155. [Online]. Available:https://ojs.aaai.
org/index.php/AAAI/article/view/17155.
[107] K. Goutam, S. Balasubramanian, D. Gera, and R. R. Sarma, “Layerout: Freezing
layers in deep neural networks,” SN Computer Science, vol. 1, no. 5, p. 295, Sep.
2020. doi: 10 . 1007 / s42979 - 020 - 00312 - x. [Online]. Available: https :
//doi.org/10.1007/s42979-020-00312-x.
[108] W. R. Thompson, “On the likelihood that one unknown probability exceeds an-
other in view of the evidence of two samples,” Biometrika, vol. 25, no. 3 /4,
pp. 285–294, 1933. doi: 10.1093/biomet/25.3- 4.285 . [Online]. Available:
http://www.jstor.org/stable/2332286.
[109] M. Zhou, T. Wang, and S. Wang, “Spectrum sensing across multiple service
providers: A discounted thompson sampling method,” IEEE Communications
Letters, vol. 23, no. 12, pp. 2402–2406, 2019. doi: 10 . 1109 / LCOMM . 2019 .
2941717.
[110] F. C. Asyuraa, S. Abdullah, and T. E. Sutanto, “Empirical evaluation on dis-
counted thompson sampling for multi-armed bandit problem with piecewise-stationary
bernoulli arms,” Journal of Physics: Conference Series, vol. 1722, no. 1, p. 012 096,
Jan. 2021. doi: 10. 1088/ 1742- 6596 /1722 /1/ 012096. [Online]. Available:
https://dx.doi.org/10.1088/1742-6596/1722/1/012096.
[111] J. Tobin, R. Fong, A. Ray, J. Schneider, W. Zaremba, and P. Abbeel, “Domain
randomization for transferring deep neural networks from simulation to the real
world,” in 2017 IEEE/RSJ international conference on intelligent robots and sys-
tems (IROS), IEEE, 2017, pp. 23–30.
[112] Y . Bai, H. Lam, T. Balch, and S. Vyetrenko, “E fficient calibration of multi-agent
simulation models from output series with bayesian optimization,” inProceedings
of the Third ACM International Conference on AI in Finance, ser. ICAIF ’22, New
York, NY , USA: Association for Computing Machinery, 2022, pp. 437–445.doi:
10.1145/3533271.3561755 . [Online]. Available: https://doi.org/ 10.
1145/3533271.3561755.
[113] S. Vyetrenko et al., “Get real: Realism metrics for robust limit order book mar-
ket simulations,” in Proceedings of the First ACM International Conference on
AI in Finance , ser. ICAIF ’20, New York, New York: Association for Comput-
ing Machinery, 2021. doi: 10 . 1145 / 3383455 . 3422561. [Online]. Available:
https://doi.org/10.1145/3383455.3422561.
[114] J. García, Fern, and o Fernández, “A comprehensive survey on safe reinforcement
learning,” Journal of Machine Learning Research, vol. 16, no. 42, pp. 1437–1480,
2015. [Online]. Available:http://jmlr.org/papers/v16/garcia15a.html.
140

[115] F. Fernández and M. Veloso, “Probabilistic policy reuse in a reinforcement learn-
ing agent,” in Proceedings of the Fifth International Joint Conference on Au-
tonomous Agents and Multiagent Systems, ser. AAMAS ’06, Hakodate, Japan: As-
sociation for Computing Machinery, 2006, pp. 720–727.doi: 10.1145/1160633.
1160762. [Online]. Available: https : / / doi . org / 10 . 1145 / 1160633 .
1160762.
[116] A. Vaswani et al., “Attention is all you need,” in Advances in Neural Information
Processing Systems, I. Guyon et al., Eds., vol. 30, Curran Associates, Inc., 2017.
[Online]. Available: https : / / proceedings . neurips . cc / paper _ files /
paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf.
[117] J. Wu, W. Gan, Z. Chen, S. Wan, and P. S. Yu, “Multimodal large language mod-
els: A survey,” in 2023 IEEE International Conference on Big Data (BigData) ,
2023, pp. 2247–2256. doi: 10.1109/BigData59044.2023.10386743.
[118] N. N. Taleb, The Black Swan:: The Impact of the Highly Improbable: With a new
section:" On Robustness and Fragility" . Random house trade paperbacks, 2010,
vol. 2.
141

APPENDIX
A.1. Appendix: Additional AIIF plots
Additional experiments were performed changing the AIIF factors. The results are shown
as follows:
Figure 1: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 0.2.
Figure 2: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 0.5.
142

Figure 3: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 0.8.
Figure 4: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 1.5.
Figure 5: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 2.
143

Figure 6: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 10.
Figure 7: DQN MM instant inventories held and thresholds along the testing experiment
every time step with alpha factor applied AIIF = 1005.
144
