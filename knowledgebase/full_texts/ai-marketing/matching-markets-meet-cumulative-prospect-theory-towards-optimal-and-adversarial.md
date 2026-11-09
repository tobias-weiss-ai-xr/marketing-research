---
title: 'Matching Markets meet Cumulative Prospect Theory: Towards Optimal and Adversarially Robust Learning'
url: https://arxiv.org/abs/2606.19883
category: ai-marketing
subcategory: measurement
date: 2026-06
venue: ''
authors:
- Ananya Kunisetty
- Avishek Ghosh
source: arxiv
pdf_url: https://arxiv.org/pdf/2606.19883
pages: 30
chars: 73817
fetched_at: '2026-11-08T13:27:18+00:00'
kb_version: 1
---

# Matching Markets meet Cumulative Prospect Theory: Towards Optimal and Adversarially Robust Learning

Matching Markets meet Cumulative Prospect Theory:
Towards Optimal and Adversarially Robust Learning
Ananya Kunisetty Avishek Ghosh
Indian Institute of Technology Bombay, Mumbai 400076, India
ananya.kunisetty@gmail.com, avishek_ghosh@iitb.ac.in
Abstract
We study a multi-agent multi-armed bandit problem in the competitive setup with two-sided matching markets
under a human centric decision making model. To capture human preferences, we use cumulative prospect theory
(CPT) that weighs the actions of the agent in a nonlinear fashion using a (𝛼-Hölder continuous) weight function. CPT
has been widely used in behavioral economics and risk sensitive machine learning to emulate human preferences.
We analyze the state-of-the-art learning algorithm [12] with CPT weight distorted rewards and derive a regret
ofO(𝐾log𝑇  1 Δ 2/𝛼), where𝐾 denotes the number of arms,𝑇 is the learning horizon, and Δ represents (suitably
defined) players’ minimum preference gap. Obtaining a regret lower bound, we notice that the dependence on Δ
is sub-optimal. We further improve this regret by judiciously selecting the active set of arms during exploration,
which achieves the optimal regret guarantees (matching the lower bound) in the setting where the number of arms
𝐾 is significantly larger than the number of players𝑁 . In addition, we also consider adversarial markets where the
observed rewards of the agents may be corrupted. We propose and analyze algorithms for robust markets with CPT
as risk sensitive measure in both settings where the total corruption budget is known and where it is unknown, and
establish logarithmic player-optimal regret guarantees in both cases.
Keywords:Markets and Bandits·Cumulative Prospect Theory·Robust Markets.
1 Introduction
Online matching markets—such as Amazon Mechanical Turk, Upwork, ride-sharing platforms (like Uber) and
labor markets connect a demand side (agents or players) with a supply side (resources). For example, businesses
hiring workers on Mechanical Turk or Upwork, customers requesting rides on Uber form the demand side, while
freelancers, crowdworkers, drivers represent the supply side. Agents repeatedly choose among resources based on
their preferences. Since resources are typically capacity constrained, agents compete for access while simultaneously
navigating uncertainty on the quality of each resource through interactions. These interactions are often modeled as
a bipartite graph, where both agents and resources have preferences over the opposite side, though these preferences
are initially unknown. Agents must therefore learn these preferences through minimal interactions and subsequently
obtain an optimal stable matching. Once preferences are learned, algorithms such as the Deferred Acceptance
algorithm proposed by David Gale and Lloyd Shapley can be used to compute the optimal stable matching.
Learning in matching markets has received considerable interest, especially from the lens of a multi-agent MAB
(multi-armed bandit) framework [18, 17, 12, 24, 4, 22, 6, 9]. In the above works, a variation of matching markets is
studied where each player has unknown preference over arms whereas arms can be certain of their preferences over
players through some known utility like payments (in case of labor markets) or some global ranking (in finance).
Denoting𝐾 as the number of arms,𝑁 as the number of players,𝑇 as the time horizon with𝐾≥𝑁 . This is done to
ensure each player has a chance of being matched (see [17, 24, 4, 12]). Moreover, let Δ be the minimum preference
gap between the first 𝑁+ 1arms across all players. With this, the objective is to find the most suitable (player
optimal) stable matching for all the players. In previous works ([18, 12, 24, 4, 6, 22, 9]) this is ensured by defining an
1
arXiv:2606.19883v1  [cs.LG]  18 Jun 2026

appropriate regret defined as the mean reward of thebestarm in hindsight minus the mean reward obtained from a
learning algorithm in presence of competition from other agents, and showing that the regret scales sublinearly with
the learning horizon.
However, in real-world applications—ranging from labor markets to financial portfolio optimization—the mean
(average) does not satisfactorily capture the merits of certain actions, especially when humans are involved in the
decision making (see [27] for a recent survey). Also, [23] demonstrates that conventional mean-based optimization of
a Nikkei option portfolio was unable to identify hidden market crashes, which become apparent only when tail-risk
measures are considered.
In many such applications, risk is a crucial consideration, and decision-makers often prefer a risk-sensitive performance
criterion rather than relying solely on the average reward. As a result, extensive research has examined a variety of
risk measures, including mean–variance [19], Value-at-Risk (VaR), Conditional Value-at-Risk (CVaR) [3, 23], spectral
risk measures [1], and utility-based shortfall risk [8]. Although these measures satisfy desirable properties such
as coherence or convexity, they fail to capture the nuances of human decisions like loss aversion and asymmetric
preferences. Such behavioral features are more effectively modeled by the celebrated (and Nobel Prize–winning)
framework of Cumulative Prospect Theory (CPT) [29] in behavioral economics.
Consider the “Asian Disease Problem” [10], in which a decision maker aims to maximize a Public Health Score 𝑟,
representing the number of lives saved. The agent must choose between two policies: aSafeprotocol that guarantees
𝑟= 200, and aRiskyprotocol that yields 𝑟= 600with probability35%and 𝑟= 0with probability65%. Under a
risk-neutral criterion based on expected reward, the risky protocol is optimal because its expected value is higher
(𝜇Risky = 210) than that of the safe protocol ( 𝜇Safe = 200). However, empirical studies show that most human
decision-makers reject this gamble and instead choose the safe protocol [29].
Cumulative Prospect Theory (CPT) resolves this discrepancy by evaluating outcomes through a distorted value rather
than a simple expectation, using a suitably chosen non-linear weighting function. In this example, the CPT weighting
function disproportionately emphasizes the probability of the adverse event{𝑟= 0}, thereby penalizing the possibility
of saving no patients. As a result, CPT correctly identifies the safe protocol as thesubjectively optimalchoice.
The study of CPT based risk measure for multi-armed bandits (MABs) has been limited. [7] introduces the notion of
CPT based regret for simple𝐾 armed bandits and linear bandits, whereas [28] uses a generic framework to handle
monotone as well as non-monotone weight distorted rewards including CPT. The above works consider a single
player multi-armed bandit setup and this leads to an interesting open problem:
Is it possible to learn in a multi-player (competitive or collaborative) MAB with CPT risk measure?
In this paper, we answer the above question in affirmative. We consider multi-player MAB in the competitive setup
of matching markets. Using CPT as risk measure, we define an appropriate distorted regret through a non-linear
Hölder continuous function, similar to [7] albeit in the competitive market setting. The objective here is to converge
to a (player optimal) stable matching based on this weighted (distorted) reward which may be quite different from
the standard matching based on reward average (see Figure 1 for an example). We propose and analyze CPT based
state of the art learning algorithm ([12]) namely CPT-Explore-Then-Gale-Shapley (CPT-ETGS) and obtain sublinear
(logarithmic) regret bound.
By proving a lower bound on CPT based regret in the matching markets setup, we observe that the regret ofCPT-ETGS
is sub-optimal. Hence, we modify the learning algorithm by carefully choosing the set of arms during the exploration
phase of CPT-ETGS. We dub the resulting algorithm Improved CPT-ETGS. As a result, we show that in large markets,
where the number of arms𝐾 is significantly larger than𝑁 , Improved CPT-ETGS achieves the lower bound on regret
and hence optimal.
Moreover, in a practical competitive market, there might be manipulation (or corruption) of rewards received by
the players. The effect of such corruption aggravates in the presence of weight distortion. Notably, online learning
in the presence of corruption is well explored in applications like feedback contamination (click fraud) in online
advertisement [31, 21], non-stationary online learning [26, 25]. Furthermore, adversarial bandits is a well studied
2

problem in the literature albeit in a single player setup [20, 2, 16]. Recently, [30] study the matching markets problem
in the presence of (bounded) corruption and propose an explore then commit type algorithm for the same.
We study the matching markets problem where the rewards are weight distorted (via CPT) and corrupted simultane-
ously. We consider two cases where the total corruption budget is known and unknown. In both cases we modify
the CPT-ETGS algorithm and obtain sub-linear regret guarantees. In particular, we characterize the (regret) cost that
comes from simultaneous control of distorted and corrupted rewards.
1.1 Summary of Contributions
We leverage CPT based risk sensitive measure to capture human centric decision making in matching markets. We use
the state of the art learning algorithm for matching markets from [12] and incorporate CPT based weight distortion.
The resulting algorithm, CPT-ETGS is shown to achieve a (player optimal) regret upper bound ofO(𝐾log𝑇  1 Δ 2/𝛼),
where Δ is the minimum preference gap between the first𝑁+ 1arms across all players and 𝛼 is the coefficient of
Hölder continuity for the (non-linear) weight distortion function. CPT-ETGS is also an explore and commit type
algorithm, however the upper and lower confidence bounds are carefully defined to incorporate the weight distortion
of the rewards.
In Section 4, we consider a simple problem instance and obtain a regret lower bound (roughly) Ω

𝐾log𝑇  1 Δ  2 𝛼−1 ,
which implies the regret of CPT-ETGS is sub-optimal (since 1 Δ2/𝛼−1 may be much smaller than 1 Δ2/𝛼 ). We identify that the sub-optimality stems fromexcessexploration inCPT-ETGS.
In the modified algorithm namely ImprovedCPT-ETGS, players adaptively switch between exploration and exploitation
and promptly eliminate sub-optimal arm so the active set of arms on which we will be exploring will not lead to unneces-
sary regret. We prove that Improved CPT-ETGS achieves a regret upper bound ofO

𝐾log𝑇  1 Δ  2 𝛼−1+𝑁 2 log𝑇 1 Δ2/𝛼  .
In the scenario where𝐾 is much larger than𝑁 (𝐾≫𝑁 ), i.e., in large markets, the first term dominates and the regret
of ImprovedCPT-ETGSmatches to that of the lower bound. This implies optimality of ImprovedCPT-ETGS.
Furthermore, in Section 5, we consider adversarial markets, the practical setup where the rewards are distorted
as well as corrupted. In this setup, players may not be able to learn their true preferences owing to the presence
of corruption. We address such adversarial market with known as well as unknown corruption budget (denoted
by𝐶). Given the corruption budget, we may bound the changes in distorted reward using the Hölder continu-
ity property of the weight distortion function. In this case we widen the confidence interval while calculating
preferences. If the corruption budget is unknown, we use a multi-layer CPT-ETGS. In both the cases we change
the confidence intervals, and regret definitions to incorporate human preferences. If 𝐶 is known, we achieve a
regret upper bound ofO

𝐾log𝑇
Δ2/𝛼 +𝐾 𝐶 Δ 1/𝛼 . On the other hand, if𝐶 is not known, we obtain an upper bound of
O

𝐾𝐶 log2𝑇  1 Δ  2 𝛼+𝐾(log𝑇+𝐶)(log𝑇) 1+ 1 𝛼  𝑑 Δ  1 𝛼  where𝑑 is a problem dependent parameter, and the difference
between these two characterizes the difficulty of not knowing the corruption budget.
1.1.1 Technical Challenges
The main technical challenge is to integrate CPT based weight distortion in the multi-agent framework with competi-
tion. In particular, we design new confidence intervals (in such a setup) such that the estimated preference is close
to the true preference. We achieve this by an application of Dvoretzky-Kiefer-Wolfowitz (DKW) inequality which
gives finite-sample exponential concentration of the empirical distribution. Subsequently, we define agoodevent for
CPT-ETGS and Improved CPT-ETGS. Note that sample mean estimation with CPT distortion uses order statistics (see
[7]), and with multiple agents and unknown preferences, such analysis becomes quite non-trivial. Furthermore, in
the case of corrupted rewards, we leverage the Hölder continuity property of the CPT weight distortion function and
modify the upper and lower confidence bounds. This leads to a bound on the maximum deviation between distorted
reward estimates computed with corrupted and uncorrupted observations. In particular, with unknown corruption
budget, tracking the corrupted and distorted reward simultaneously turns out to be quite involved.
3

0.0 0.2 0.4 0.6 0.8 1.0
True probability p
0.0
0.2
0.4
0.6
0.8
1.0Decision weight w(p)
overweights
small p
underweights
large p
w(p) = pγ
(pγ + (1 − p)γ)1/γ
Probability Weighting Function
w(p) = p  (no distortion)
w(p),  TK (γ = 0.61)
(a) Tversky–Kahneman probability weighting function
𝑤(𝑝) . Small probabilities areoverweighted( 𝑤(𝑝)>𝑝 )
and large probabilities areunderweighted(𝑤(𝑝)<𝑝).
a0
r = 0.80,  p = 0.10
a1
r = 0.12,  p = 0.90
a2
r = 0.50,  p = 0.50
a3
r = 0.03,  p = 0.80
0.00
0.05
0.10
0.15
0.20
0.25
0.30Preference value
#3
#2
#2
#3
#1
#1
#4 #4
rank swap
EV vs CPT Arm Values  (Bernoulli Rewards)
EV = p ⋅ r
CPT = w(p) ⋅ r
(b) EV vs. CPT arm values for a representative player. Arms
𝑎0 and 𝑎1 swap ranks: 𝑎0 (rare high reward, 𝑝=0.10) is
boosted under CPT while𝑎1 (frequent low reward,𝑝=0.90)
is demoted.
Figure 1:CPT distortion leads to different preference orders.Each arm follows a Bernoulli distribution: reward 𝑟
with probability𝑝, and0otherwise. Under expected value, a player ranks arms by 𝜇𝑗 =𝑝 𝑗𝑟𝑗. Under CPT, the same
samples yield rankings based on𝜈𝑗 =𝑤(𝑝 𝑗)𝑟𝑗. Since 𝑤(·) overweights small probabilities (a), arms with rare but
large rewards can overtake arms with frequent but modest rewards (b), producing adifferentpreference order from
the same data. Hence, ETGS andCPT-ETGSconverge to different stable matching.
2 Formulation
We formally introduce the problem setting below. For any positive integer𝑛, we use[𝑛]to denote{1,2,...,𝑛}.
2.1 Risk Neutral (Undistorted) Matching Market Model
We study a two-sided market comprising𝑁 playersP={𝑝 1,...,𝑝 𝑁} and𝐾≥𝑁 armsA={𝑎 1,...,𝑎 𝐾}. Each player
𝑝𝑖 is characterized by unknown mean rewards ¯𝜇𝑖,𝑗 over arms, while each arm𝑎𝑗 possesses a fixed, publicly known
strict ranking(𝜋 𝑗,𝑖)𝑖∈[𝑁] over the players with all values distinct.
The interaction unfolds over𝑇 rounds. In round 𝑡, every player𝑝𝑖 selects an arm𝐴𝑖(𝑡)∈A to propose to. Each
arm accepts its highest-ranked proposer under𝜋𝑗 and rejects the remaining players. Denoting by ¯𝐴𝑖(𝑡) the arm that
accepts𝑝𝑖 (with ¯𝐴𝑖(𝑡)=∅ if rejected), the accepted player observes a stochastic reward𝑋𝑖(𝑡)∼F 𝑖, ¯𝐴𝑖(𝑡) with mean
¯𝜇𝑖, ¯𝐴𝑖(𝑡) , while a rejected player receives𝑋𝑖(𝑡)=0. The global matching at round𝑡is ¯𝐴(𝑡)={(𝑖, ¯𝐴𝑖(𝑡)):𝑖∈[𝑁]}.
A matching isstableif no player–arm pair(𝑝𝑖,𝑎𝑗) would mutually benefit from deviating, i.e., there is no pair satisfying
¯𝜇𝑖,𝑗 > ¯𝜇𝑖, ¯𝐴𝑖(𝑡) and𝜋𝑗,𝑖 >𝜋 𝑗, ¯𝐴−1 𝑗 (𝑡) . Among all stable matchings𝑀, theplayer-optimal stable matching 𝑚∗ is the unique
element for which ¯𝜇𝑖,𝑚∗ 𝑖 ≥ ¯𝜇𝑖,𝑚𝑖 for every𝑚∈𝑀 and𝑖∈ [𝑁] ; its existence is guaranteed by the Gale-Shapley
deferred-acceptance procedure [5].
Assumption 1.The reward𝑋 𝑖(𝑡)is bounded almost surely, i.e.,|𝑋 𝑖(𝑡)|≤𝑀for some constant𝑀>0.
2.2 CPT based Distorted Utility Model
Instead of evaluating actions using the standard expected reward, we adopt a distorted utility model based on
cumulative prospect theory (CPT) [29]. In this framework, players evaluate stochastic outcomes through a nonlinear
transformation of probabilities.
Let𝑌𝑖,𝑗 denote the random reward obtained by player 𝑝𝑖 when matched with arm𝑎𝑗. Let 𝑤 :[0, 1]→[ 0, 1] be a
probability weighting function satisfying 𝑤( 0)= 0and 𝑤( 1)= 1. The distorted utility of arm 𝑎𝑗 for player𝑝𝑖 is
defined as
𝜇𝑖,𝑗 =
∫ ∞
0
𝑤P(𝑌𝑖,𝑗 >𝑧) 𝑑𝑧− ∫ ∞
0
𝑤P(−𝑌𝑖,𝑗 >𝑧) 𝑑𝑧.(1)
4

The above expression represents the CPT value of the reward distribution by integrating the distorted tail probabilities
of gains and losses. For analytical convenience, we decompose the distorted utility into its positive and negative
components. Let 𝜇𝑖,𝑗 =𝜇 + 𝑖,𝑗 −𝜇 − 𝑖,𝑗, where the gain component and loss component are defined respectively as
𝜇+ 𝑖,𝑗 = ∫∞ 0 𝑤P(𝑌𝑖,𝑗 >𝑧) 𝑑𝑧and𝜇 − 𝑖,𝑗 = ∫∞ 0 𝑤P(−𝑌𝑖,𝑗 >𝑧) 𝑑𝑧.
The term𝜇+ 𝑖,𝑗 captures the distorted contribution of gains, while𝜇− 𝑖,𝑗 captures the distorted contribution of losses [11,
7]. The probability weighting function𝑤(·) distorts the tail probabilities, reflecting the behavioral bias described by
cumulative prospect theory [11, 7]. In particular, small probabilities may be overweighted while moderate or large
probabilities may be underweighted depending on the shape of𝑤.
Note that when the weighting function is the identity function𝑤(𝑝)=𝑝 , the distorted utility reduces to the standard
expected reward, i.e.,𝜇𝑖,𝑗 = ¯𝜇𝑖,𝑗 =E[𝑌𝑖,𝑗]. Thus the distorted utility formulation generalizes classical expected-value
based evaluation.
Throughout the paper, we use𝜇𝑖,𝑗 to denote the CPT-distorted reward defined in equation 1, rather than the standard
expected reward ¯𝜇𝑖,𝑗 .
Assumption 2.(Hölder continuity) Let 𝑤 :[0, 1]→[ 0, 1] denote the probability weighting function. We assume
that𝑤( 0)= 0and 𝑤( 1)= 1. Furthermore,𝑤(·) satisfies a Hölder continuity condition: there exist constants𝐿> 0
and𝛼∈(0,1]such that for all𝑥,𝑦∈[0,1],
sup
𝑥≠𝑦
|𝑤(𝑥)−𝑤(𝑦)|
|𝑥−𝑦| 𝛼 ≤𝐿.(2)
Similar assumptions featured in previous works [7, 28, 11] with CPT risk.
2.3 CPT Regret
Let𝑚∗ denote the player-optimal stable matching. The goal of each player is to learn the arm assigned to it in𝑚∗.
The player-optimal stable regret of player𝑝𝑖 after𝑇 rounds is defined as CPT-Reg𝑖(𝑇)=𝑇𝜇 𝑖,𝑚∗ 𝑖− ˝ 𝑗∈[𝐾] 𝑇𝑖,𝑗(𝑇)𝜇 𝑖,𝑗,
and the expected regret can be written as
E[CPT-Reg𝑖(𝑇)]=
∑︁
𝑗∈[𝐾],𝑗≠𝑚 ∗ 𝑖
E[𝑇𝑖,𝑗(𝑇)]Δ 𝑖,𝑚∗ 𝑖,𝑗.(3)
where𝑇𝑖,𝑗(𝑇)= ˝𝑇 𝑡=1 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗} is the number of times arm 𝑗 is matched by player𝑖 up to time𝑇 and Δ𝑖,𝑚∗ 𝑖,𝑗 is
defined below.
Preference Gap[12]: Consider a player𝑝𝑖 and two distinct arms𝑎𝑗 and𝑎𝑗′. The preference gap of player𝑝𝑖 between these
two arms is defined asΔ𝑖,𝑗,𝑗 ′ =|𝜇 𝑖,𝑗−𝜇𝑖,𝑗′|. Let𝜌𝑖 denote the preference ordering of player𝑝𝑖 over the arms, and let𝜌𝑖,𝑗
represent the arm ranked at position 𝑗 in this ordering, for 𝑗∈[𝐾] . We define Δ=min 𝑖∈[𝑁];𝑗,𝑗 ′∈[𝑁+1];𝑗≠𝑗 ′ Δ𝑖,𝜌𝑖,𝑗,𝜌𝑖,𝑗′
to be the smallest preference gap taken over all players and over all pairs of arms among their first 𝑁+ 1ranked
arms. Since all preference values are assumed to be distinct, this quantity is non-negative. Finally, for each player𝑝𝑖,
define Δ𝑖,max =𝜇 𝑖,𝑚∗ 𝑖 which corresponds to the maximum player-optimal stable regret that player𝑝𝑖 may incur across
all rounds.
3 Human Centric Matching Markets with CPT Regret
3.1 Distorted Preference Estimation
To estimate player preferences under cumulative prospect theory (CPT), we use a distorted utility estimator based on
the empirical reward distribution.
Algorithm 1 computes an empirical estimate of the distorted utility using the observed rewards. The observed rewards
are first sorted so that the ordered samples correspond to empirical quantiles of the reward distribution. This quantile
5

Algorithm 1CPT Distorted Preference Estimation [11]
1:Input:rewards𝑋 𝑖,𝑗,1,...,𝑋 𝑖,𝑗,𝑙 , weight function𝑤(·)
2:Sort samples:𝑋 𝑖,𝑗,(1) ≤···≤𝑋 𝑖,𝑗,(𝑙) and let𝑙𝑏 be the number of negative samples
3: ˆ𝜇+ 𝑖,𝑗 = ˝𝑙 𝑘=𝑙𝑏+1𝑋𝑖,𝑗,(𝑘)  𝑤( 𝑙+1−𝑘 𝑙 )−𝑤( 𝑙−𝑘 𝑙 ) 
4: ˆ𝜇− 𝑖,𝑗 = ˝𝑙𝑏 𝑘=1𝑋𝑖,𝑗,(𝑘)  𝑤( 𝑘−1 𝑙 )−𝑤( 𝑘 𝑙) 
5:Return: ˆ𝜇𝑖,𝑗 = ˆ𝜇+ 𝑖,𝑗− ˆ𝜇− 𝑖,𝑗
Algorithm 2CPT-ETGS(Player𝑝 𝑖)
Require:player set𝑃, arm set𝐴, horizon𝑇
1:Initialize ˆ𝜇𝑖,𝑗 =0,𝑇 𝑖,𝑗 =0
2:Phase 1: Index discovery
3:Phase 2: Preference learning
4:forsub-phaseℓ=1,2,...do
5:for2 ℓ roundsdo
6:select arm via round-robin based on Index
7:observe reward, increment𝑇 𝑖,𝑗 and update ˆ𝜇𝑖,𝑗 using Algorithm 1
8:end for
9:compute W-UCB and W-LCB for all arms
10:iftop𝑁arms identifiedthen
11:record ranking𝜎 𝑖
12:end if
13:ifall players matchedthen
14:terminate exploration
15:end if
16:end for
17:Phase 3: Stable matchingvia decentralized GS algorithm
representation allows the distorted utility, which is defined through distorted tail probabilities, to be approximated
using order statistics of the empirical distribution.
The distortion function 𝑤(·) is then applied to the probability levels associated with these quantiles. The terms
𝑤

𝑙+1−𝑘
𝑙

−𝑤

𝑙−𝑘
𝑙

represent the distorted probability mass assigned to the𝑘-th order statistic.
Since CPT evaluates gains and losses separately, the estimator computes the contributions of positive and negative
rewards independently. The distorted gain component aggregates positive samples, while the distorted loss component
accounts for negative samples. Combining these components yields the empirical estimate ˆ𝜇𝑖,𝑗 . This quantile-based
estimator follows the CPT-value estimation scheme introduced in [14] and later adapted for bandit settings in [11].
3.2 Algorithm:CPT-ETGS
In this section, we consider the problem of finding the player-optimal stable matching in human-centric matching
markets, where players evaluate outcomes based on behavioral preferences rather than purely expected rewards. To
address this, we propose a CPT-aware algorithm that builds on the Explore Then Gale Shapley (ETGS) framework
[12, 13]. The key distinction between Algorithm 2 and the ETGS algorithm of [12] lies in the estimation of player
preferences over arms. This modification enables the algorithm to learn preference values aligned with CPT evaluations
using Algorithm 1 while preserving the ETGS framework.
CPT-ETGS proceeds in three phases. In the first phase, each player obtains a unique index that allows players to
coordinate their exploration and avoid collisions, in the second phase players estimate their preferences over arms by
exploring with the help of the index obtained in the first phase, and in the third phase using the preference order
6

obtained in second phase players find out the stable matching and then would focus on that arm for the remaining
rounds. The details of the first and third phase are mentioned in the Appendix B.
The second phase of the algorithm is divided into multiple subphases𝑙= 1, 2, 3,... and each subphase has a length of
2𝑙+ 1consisting of an exploration stage of2 𝑙 rounds followed by a monitoring round. In the exploration rounds, the
players choose arms in a round robin fashion to avoid collision and to make estimates of their preference over arms.
In the monitoring round, all the players estimate their CPT-distorted preference values over all arms using Algorithm
1 adapted from [11], and construct confidence intervals for each arm.
The confidence bounds are defined as
W-UCB𝑖,𝑗 = ˆ𝜇𝑖,𝑗+𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
,W-LCB𝑖,𝑗 = ˆ𝜇𝑖,𝑗−𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
(4)
We set W-UCB𝑖,𝑗 to∞and W-LCB 𝑖,𝑗 to−∞when𝑇 𝑖,𝑗 =0. Once the confidence sets for two arms𝑎 𝑗,𝑎𝑗′ are disjoint,
i.e., W-LCB𝑖,𝑗 >W-UCB𝑖,𝑗′ or W-LCB𝑖,𝑗′ >W-UCB𝑖,𝑗 ,𝑝𝑖 can determine its preference over these arms. When a player
is able to identify the top𝑁 arms in its ranking, then in the monitoring round the player propose to the arm with
the unique index obtained in the first phase, and the players who have not yet determined their preferences remain
inactive. When all the players are matched with an arm, we can determine that all players have found their preference
order over arms and can proceed to the third phase. We next derive an upper bound on the player-optimal stable
pseudo-regret incurred by each player when using our algorithm. The proof is deferred to Appendix C.
Theorem 3.1.The player optimal stable regret incurred by each𝑝 𝑖∈Nunder Algorithm 2 satisfies
E[CPT-Reg𝑖(𝑇)]≤𝑐 0
 3𝐾log𝑇
Δ2/𝛼 (4𝐿𝑀)2/𝛼+𝑁 2+2𝑁𝐾

Δ𝑖,max.
where𝑐 0 is a universal positive constant.
Remark 3.2.Observe that the CPT-regret of player 𝑖 is𝑂

𝐾log𝑇 𝐿𝑀 Δ 2/𝛼 . In Section 4.1, we show that the
dependence on𝐾 and𝑇 is optimal. However the dependence on the gap Δ is sub-optimal. In the subsequent section,
we modifyCPT-ETGSto achieve such optimal regret.
Remark 3.3.When 𝛼= 1, the CPT-regret reduces to the usual risk neutral regret, matching that of ETGS [12]. Even
for a (single agent) simple bandit problem, such equivalence has been observed in [11, 7].
4 ImprovedCPT-ETGSand Optimal Regret
4.1 Regret Lower Bound
In this section, we obtain a lower bound on player-optimal stable regret. We adhere to the classical asymptotic regret
lower bound framework of Lai and Robbins [15]. These lower bounds are also studied in [24] in the context of (risk
neutral) markets and bandits.
Consider an instance where all arms share the same preference ordering over players,𝑝1≻𝑝 2≻···≻𝑝 𝑁 . This is
called the global ranking [18] or the serial dictatorship [24] model. We characterize the regret lower bound based on
this instance.
Lemma 4.1(Lower bound on player-optimal stable regret).There exists a problem instance with serial dictatorship
such that for any learning algorithm, the player-optimal stable regret of player𝑝 1 satisfies
lim inf
𝑇→∞
E[CPT-Reg1(𝑇)]
log𝑇 ≥
∑︁
𝑗∈[𝐾],𝑗≠𝑚 ∗ 1
1
4(𝐿𝑀) 2/𝛼

1
Δ1,𝑚∗ 1,𝑗
! 2
𝛼−1
.
whereΔ 1,𝑚∗ 1,𝑗 is the preference gap between the best arm𝑚 ∗ 1 and the𝑗-th arm.
7

Algorithm 3ImprovedCPT-ETGS(player𝑝 𝑖)
1:Input:number of players𝑁, number of arms𝐾, horizon𝑇
2:Initialize: ˆ𝜇𝑖,𝑗 =0,𝑇 𝑖,𝑗 =0, W-UCB𝑖,𝑗 =∞, W-LCB𝑖,𝑗 =−∞for all𝑗
3:D 𝑖←∅,A 𝑖←K,𝐸 𝑖←True
4:forround𝑡=1,2,...,𝑇do
5:Select an arm𝐴 𝑖(𝑡)fromA 𝑖 using a round-robin schedule
6:Update ˆ𝜇𝑖,𝑗 using Algorithm 1, increment𝑇𝑖,𝑗
7:Remove suboptimal arms fromA 𝑖 using the confidence bounds if|A 𝑖|>𝑁
8:ifone arm is confidently better than all othersthen
9:Commit to that arm: setA 𝑖 ={𝑗}and𝐸 𝑖 =False
10:end if
11:foreach other player𝑝 𝑖′ already committed to arm𝐴𝑖′ do
12:ifarm𝐴 𝑖′ prefers𝑝𝑖′ over𝑝𝑖 then
13:Add𝐴 𝑖′ to deletion setD𝑖 and remove it fromA𝑖
14:if𝑝 𝑖 had committed to that armthen
15:Resume exploration: set𝐸 𝑖 =True
16:end if
17:end if
18:end for
19:end for
Remark 4.1.The above result roughly implies that the (minimax) lower bound for CPT distorted matching markets
has an improved dependence on preference gap compared to the regret ofCPT-ETGS.
Intuition:It is easy to see that under serial dictatorship, the stable matching between the players and arms is unique.
Player ranked1( 𝑝1) prefers the arm𝑚∗ 1 =arg max𝑗∈[𝐾] 𝜇1𝑗 the most, where𝜇𝑖𝑗 is the CPT distorted mean of player𝑖
pulling arm 𝑗. Since player𝑝1 is the highest ranked player, it will not face any collision and the learning problem for
𝑝1 reduces to the classical multi-armed bandit problem (with CPT distorted rewards) where a player is given𝐾 actions
(arms) and must learn to choose the best action over time. Detailed proof of the lemma is provided in the Appendix E.
4.2 ImprovedCPT-ETGSAlgorithm
To improve the dependence on K in the regret obtained in Theorem 3.1 we build on the adaptive ETGS framework
of [13], modifying it to operate with CPT-distorted confidence bounds. The key idea is to interleave exploration with
arm elimination rather than exploring all𝐾 arms uniformly (as in CPT-ETGS), players progressively discard arms that
are provably suboptimal under the distorted reward estimates, thereby reducing unnecessary exploration.
Each player𝑝𝑖 maintains a candidate arm setA𝑖 (initially[𝐾] ), a rejected arm set𝐷𝑖 (initially∅), and an exploration
flag𝐸𝑖 (initially True) indicating whether the player is still exploring or has committed to a single arm.
At each round𝑡, player𝑝𝑖 updates its CPT-distorted estimate ˆ𝜇𝑖,𝑗(𝑡) via Algorithm 1 and constructs the confidence
intervals based on W-UCB and W-LCB as defined in equation 4. An arm whose W-UCB falls below the W-LCB of any
other arm is eliminated fromA𝑖. This elimination is the central difference from CPT-ETGS, it ensures that the number
of samples wasted on clearly inferior arms scales with the per-arm gap Δ𝑖,𝑚∗ 𝑖,𝑗 rather than the global minimum gap Δ,
leading to improved regret.
The Algorithm 3 operates as an online counterpart of the Gale-Shapley procedure [5]. While 𝐸𝑖 =True , player𝑝𝑖
explores arms fromA𝑖 via round-robin and eliminates suboptimal arms using the confidence bounds. Once a single
arm dominates all others inA𝑖, the player sets𝐸𝑖 =False and commits to that arm. If a committed arm is subsequently
claimed by a higher-priority player (according to the arm’s ranking𝜋𝑗), the arm is moved to𝐷𝑖, the candidate set
is reset toA𝑖 =[𝐾]\𝐷 𝑖, and 𝐸𝑖 is restored to True so that exploration resumes over the remaining arms. This
interaction process mirrors the offline Gale-Shapley algorithm, ensuring convergence to the player-optimal stable
8

matching. We refer to [13] for details on the communication protocol and collision handling (Lemma B.2 therein
guarantees that each arm is sampled at least once every2𝑁rounds despite collisions).
Theorem 4.2.The player-optimal stable regret for each player𝑝 𝑖 satisfies
E[CPT-Reg𝑖(𝑇)]≤𝑐 1 '›
«
∑︁
𝑗∈[𝐾],𝑗≠𝑚 ∗ 𝑖
log𝑇 (𝐿𝑀) 2/𝛼
Δ2/𝛼−1 𝑖,𝑚∗ 𝑖,𝑗 +𝑁 2 log𝑇 (𝐿𝑀) 2/𝛼 Δ2/𝛼 ·Δ𝑖,max “ﬁ ‹
where𝑐 1 is a universal positive constant.
The proof is deferred to Appendix D.
Remark 4.3.When 𝐾≫𝑁 , the regret for Improved CPT-ETGS matches to that of the lower bound obtained in
Lemma 4.1, implying optimality of the algorithm.
5 Corrupted Matching Markets with CPT Regret
5.1 Adversarial Corruption Model
We extend the CPT-matching framework to accommodate adversarial reward corruption, following the model of [30].
At each round𝑡, a true reward𝑟𝑆 𝑖,𝑗(𝑡)∼F 𝑖,𝑗 is generated for every player-arm pair who get matched. An adversary,
with access to the full history of rewards and matching decisions up to round 𝑡, then perturbs these values and
presents a corrupted reward𝑟𝑖,𝑗(𝑡) in their place. A matched player𝑝𝑖 therefore observes𝑋𝑖(𝑡)=𝑟 𝑖,𝐴𝑖(𝑡)(𝑡) rather
than the true stochastic reward.
Assumption 3.We assume that the total corruption experienced by player 𝑝𝑖 over the time horizon𝑇 is bounded by˝𝑇
𝑡=1 max𝑗∈[𝐾]

𝑟𝑖,𝑗(𝑡)−𝑟 𝑆 𝑖,𝑗(𝑡)

≤𝐶.
Assumption 4.The stochastic rewards are non-negative and bounded by a constant 𝑀 almost surely, i.e.,0 ≤
𝑟𝑆 𝑖,𝑗(𝑡)≤𝑀∀𝑖,𝑗,𝑡,and the possibly corrupted rewards are non-negative, i.e.,𝑟 𝑖,𝑗(𝑡)≥0∀𝑖,𝑗,𝑡.
Remark 5.1.We assume corrupted rewards are non-negative since the stochastic rewards are also non-negative. If a
negative reward were observed, the player could immediately detect that corruption has occurred. Moreover, any
negative corrupted reward can be safely replaced by0without affecting the analysis.
5.2 Algorithm with known corruption budget
We now consider the setting where the total corruption budget𝐶 is known in advance. In this case, we modify the
CPT-ETGS algorithm to make the learning process robust to adversarially corrupted rewards, as in Algorithm 1 of
[30]. We play Algorithm 2 and to account for the corruption while players estimate their preferences over arms, we
enlarge the confidence intervals as W-UCB𝑖,𝑗 = ˆ𝜇𝑖,𝑗+𝐿𝑀

3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 𝐶𝐿 𝑇𝛼 𝑖,𝑗 , W-LCB𝑖,𝑗 = ˆ𝜇𝑖,𝑗−𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 − 𝐶𝐿 𝑇𝛼 𝑖,𝑗 .
The rest of the three-phases: index discovery, preference learning via round-robin exploration, and decentralized
Gale-Shapley matching remains unchanged. This modification ensures that the true CPT-distorted preference value
stays within the confidence interval despite adversarial perturbations.
Theorem 5.2.With a (known) corruption budget of 𝐶, the CPT regret of 𝑝𝑖 ∈ Nsatisfies E[CPT-Reg𝑖(𝑇)]=
O

𝐾log𝑇
Δ2/𝛼 +𝐾 𝐶 Δ 1/𝛼 .
When𝛼= 1, the CPT regret matches to that of [30] where undistorted rewards are considered. The proof is deferred
to Appendix F.
9

Algorithm 4CPT-Multi-layer ETGS Race (player𝑝 𝑖)
1:Input:N,K,𝑇, sub-phase length𝑑
2:Initialize: ˆ𝜇ℓ 𝑖,𝑗 =0,𝑇 ℓ 𝑖,𝑗 =0for𝑗∈[𝐾],ℓ∈[log𝑇]
3:Phase 1:Estimate player index using ETGS
4:forsub-phase𝑘=1,2,...do
5:Explore arms for𝑑rounds using the layer-ℓround-robin rule and update ˆ𝜇ℓ 𝑖,𝑗,𝑇ℓ 𝑖,𝑗
6:Compute confidence bounds𝑊-UCB ℓ 𝑖,𝑗 and𝑊-LCB ℓ 𝑖,𝑗 for all𝑗∈[𝐾]
7:ApplyMonitoringto obtain ranking𝜎 ℓ 𝑖
8:if𝑁arms are identifiedthen
9:Compute the stable arm via decentralized Gale–Shapley and assign the matching to all layersℓ ′≤ℓ
10:end if
11:if𝑝 𝑖 is the leaderthen
12: Sample layerℓ with probability2−ℓ , with remaining probability sampleℓ= 1and broadcast using 𝑐𝑘 =⌊ℓ⌋
arm pulls
13:end if
14:end for
5.3 Algorithm with Unknown Corruption
We now consider the setting where the total corruption level𝐶 is unknown. The algorithm retains the three-phase
structure of CPT-ETGS (index discovery, preference learning, stable matching). The core challenge is that without
knowing𝐶, we cannot calibrate the corruption term in the confidence intervals. Following [30], we address this
by running log𝑇 parallel layers of the learning algorithm, where layer ℓ is activated with probability2−ℓ . Layers
that are selected less frequently accumulate fewer corrupted samples in expectation. Exploration within each layer
proceeds in fixed-length sub-phases of𝑑 rounds, with observations updating only the active layer’s statistics. The
CPT-distorted estimates are computed via Algorithm 1.
For layerℓ, we construct confidence intervals as
W-UCBℓ 𝑖,𝑗 = ˆ𝜇ℓ 𝑖,𝑗+𝐿𝑀

3 log𝑇
2𝑇ℓ 𝑖,𝑗(𝑡)
!𝛼/2
+ 2𝑑𝐿log𝑇 (𝑇ℓ 𝑖,𝑗(𝑡))𝛼,
W-LCBℓ 𝑖,𝑗 = ˆ𝜇ℓ 𝑖,𝑗−𝐿𝑀

3 log𝑇
2𝑇ℓ 𝑖,𝑗(𝑡)
!𝛼/2
− 2𝑑𝐿log𝑇 (𝑇ℓ 𝑖,𝑗(𝑡))𝛼.
The first correction term handles stochastic estimation error (as inCPT-ETGS), while the second accounts for corruption.
Layer synchronization across players is achieved through a leader-based protocol (see [30] for details): the leader
selects a layer at the end of each sub-phase. Once a layerℓ with sampling probability below1/𝐶 confidently determines
the preference ordering, it computes the stable matching 𝜎ℓ via decentralized Gale-Shapley. By Lemma G.1, this
layer’s estimates are reliable, so its matching is propagated to all faster layersℓ′≤ℓ.
Theorem 5.3.The CPT-Multi-layer ETGS race algorithm achieves the player-optimal stable regret upper bound of each
player𝑝𝑖 ,E[CPT-Reg 𝑖(𝑇)]as
O
 "
𝐾𝐶 log2𝑇 𝐿𝑀 Δ  2 𝛼 +𝐾(log𝑇+𝐶)(log𝑇) 1+ 1 𝛼 𝑑𝐿 Δ  1 𝛼 # Δ𝑖,max ! .
Observe that although worse compared to Theorem 5.2, we still obtain logarithmic regret. The proof is deferred to
Appendix G.
10

0 1 2 3 4 5
round t 1e5
0
20000
40000
60000
80000
100000
120000max cumulative CPT-regret
base ETGS vs CPT-ETGS  (valid κ, N=2, K=4)
base ETGS (risk-neutral)
CPT-ETGS
(a) Rank-swap market (𝑁=2,𝐾=4). Base
ETGS never settles⇒ linearCPT-regret;
CPT-ETGSsaturates (Thm 3.1).
0.0 0.2 0.4 0.6 0.8 1.0
round t 1e6
0
20000
40000
60000
80000
100000max cumulative CPT-regret
CPT-ETGS vs Improved, random markets  (valid κ, N=2, K=10)
CPT-ETGS
Improved CPT-ETGS
(b) Many-arm random market ( 𝑁=2,
𝐾=10; good-arm CPT values drawn at ran-
dom each run). Improved CPT-ETGS elim-
inates fillers early and commits at a lower
regret (Thm 4.2).
0.00 0.25 0.50 0.75 1.00 1.25 1.50 1.75 2.00
round t 1e7
0
1
2
3
4
5
6
7
8max cumulative CPT-regret
1e6Corruption, fixed example market  (N=3, K=3, C=60000)
CPT-ETGS (non-robust)
Robust CPT-ETGS (known C)
Multi-layer CPT-ETGS (unknown C)
(c) Adversarial corruption (𝑁=𝐾=3,𝐶=6×
104; fixed example market, CPT values ro-
tating{0.9, 0.5, 0.1}). Non-robust is lin-
ear; robust (known𝐶) and Multi-layer (un-
known𝐶) saturate (Thms 5.2–5.3).
Figure 2:Player-optimal stable CPT-regret(max over players, averaged over100runs; error bars are ± one
standard error) (a) Ignoring the CPT distortion is harmful. (b) Adaptive elimination lowers the regret. (c) Under
corruption, both robust variants stay sub-linear while the non-robust regret diverges.
6 Experiments
We validate our theory on synthetic matching markets. We study three questions: (i) whether ignoring CPT distortion
might lead to incorrect stable matchings and whether CPT-ETGS achieves sub-linear (logarithmic) regret as predicted
by Theorem 3.1 (ii) whether adaptive elimination in Improved CPT-ETGS improves performance when many arms are
clearly sub-optimal (Theorem 4.2); and (iii) whether the robust algorithms of Section 5 peform better than CPT-ETGS
and remain sub-linear under adversarial corruption with known and unknown budgets (Theorems 5.2–5.3).
Weight function and setup.We use the Lipschitz CPT weight
𝑤(𝑝)=𝑝+𝑐𝑝(1−𝑝)(1−2𝑝), 𝑐=1.5,
an inverse-𝑆 distortion satisfying𝑤( 0)= 0and 𝑤( 1)= 1. It is 𝛼= 1Hölder with constant 𝐿=sup 𝑝|𝑤′(𝑝)|= 2.5.
Since rewards lie in[0,1],𝑀=1.
Rewards are Bernoulli that is arm 𝑎𝑗 yields𝑣𝑖,𝑗 with probability𝑞𝑖,𝑗 and0otherwise. Thus 𝜇𝑖,𝑗 =𝑤(𝑞 𝑖,𝑗)𝑣𝑖,𝑗 and
¯𝜇𝑖,𝑗 =𝑞𝑖,𝑗𝑣𝑖,𝑗 . We report the maximum player-optimal stable CPT-regret over players, averaged over100runs with ±1
standard error bars.
Ignoring CPT is harmful (Fig. 2a).We construct a rank-swap market ( 𝑁= 2,𝐾= 4) where CPT and risk-neutral
preferences induce different player-optimal stable matchings. Base ETGS, which estimates risk-neutral means, fails
to identify the CPT-optimal matching and incurs linear CPT-regret . In contrast, CPT-ETGS commits to the correct
matching and its regret saturates , consistent with Theorem 3.1.
Adaptive elimination helps (Fig. 2b).For 𝑁= 2,𝐾= 10, each player has two good arms and eight filler arms
with𝜇𝑖,𝑗 ≈ 0.005. In every run, good-arm 𝜇𝑖,𝑗 values are redrawn (top value in[0.45, 0.65], second-best0.15–0.30
lower), and arm rankings are sampled independently. Both algorithms eventually commit, but Improved CPT-ETGS
quickly eliminates fillers, commits earlier, and achieves a lower regret matching Theorem 4.2.
Adversarial corruption (Fig. 2c).We consider a fixed 𝑁=𝐾= 3market whose 𝜇𝑖,𝑗 are cyclic permutations
of{0.9, 0.5, 0.1}. An adversary with per-player budget 𝐶= 6× 104 suppresses rewards on the optimal arms. The
non-robust CPT-ETGS is misled into a wrong matching and suffers linear regret . The robust algorithm with known
11

corruption budget commits correctly and saturates , while the multi-layer algorithm for unknown𝐶 also remains
sub-linear and attains an even lower regret , in agreement with Theorems 5.2–5.3.
7 Conclusion
We consider human centric risk sensitive measure, CPT for matching markets and analyze learning algorithms.
Exploring other human aligned setups in a fair matching market is kept as future endeavor.
Use of Generative AI:AI tools were used only to improve the clarity and presentation of the paper, including
shortening, rephrasing, and editing text. They were not used for research ideas, theoretical developments, or
conclusions.
References
[1] Carlo Acerbi. “Spectral measures of risk: A coherent representation of subjective risk aversion”. In:Journal of
Banking & Finance26.7 (2002), pp. 1505–1518.doi: https://doi.org/10.1016/S0378-4266(02)00281-9.
url:https://www.sciencedirect.com/science/article/pii/S0378426602002819.
[2] Raman Arora, Ofer Dekel, and Ambuj Tewari. “Online bandit learning against an adaptive adversary: from
regret to policy regret”. In:arXiv preprint arXiv:1206.6400(2012).
[3] Philippe Artzner et al. “Coherent Measures of Risk”. In:Mathematical Finance9.3 (1999), pp. 203–228.doi:
https://doi.org/10.1111/1467- 9965.00068 . eprint: https://onlinelibrary.wiley.com/doi/
pdf/10.1111/1467-9965.00068 .url: https://onlinelibrary.wiley.com/doi/abs/10.1111/1467-
9965.00068.
[4] Soumya Basu, Karthik Abinav Sankararaman, and Abishek Sankararaman. “Beyond log2(𝑇) regret for decen-
tralized bandits in matching markets”. In:International Conference on Machine Learning. PMLR. 2021, pp. 705–
715.
[5] David Gale and Lloyd S Shapley. “College admissions and the stability of marriage”. In:The American mathe-
matical monthly69.1 (1962), pp. 9–15.
[6] Avishek Ghosh et al. “Competing Bandits in Non-Stationary Matching Markets”. In:IEEE Transactions on
Information Theory70.4 (2024), pp. 2831–2850.doi:10.1109/TIT.2024.3352228.
[7] Aditya Gopalan et al. “Weighted bandits or: How bandits learn distorted values that are not expected”. In:CoRR
abs/1611.10283 (2016). arXiv:1611.10283.url:http://arxiv.org/abs/1611.10283.
[8] Zhaolin Hu and Dali Zhang. “Utility-based shortfall risk: Efficient computations via Monte Carlo”. In:Naval
Research Logistics (NRL)65 (2018), pp. 378–392.url: https : / / api . semanticscholar . org / CorpusID :
126005263.
[9] Meena Jagadeesan et al. “Learning Equilibria in Matching Markets with Bandit Feedback”. In:J. ACM70.3 (May
2023).doi:10.1145/3583681.url:https://doi.org/10.1145/3583681.
[10] Daniel Kahneman.Thinking, Fast and Slow. New York: New York: Farrar, Straus and Giroux, 2011.
[11] Ravi Kumar Kolla et al. “Bandit algorithms to emulate human decision making using probabilistic distortions”.
In:arXiv preprint arXiv:1611.10283(2016).
[12] Fang Kong and Shuai Li. “Player-optimal stable regret for bandit learning in matching markets”. In:Proceedings
of the 2023 Annual ACM-SIAM Symposium on Discrete Algorithms (SODA). SIAM. 2023, pp. 1512–1522.
[13] Fang Kong, Zilong Wang, and Shuai Li. “Improved analysis for bandit learning in matching markets”. In:
Advances in Neural Information Processing Systems37 (2024), pp. 91904–91929.
12

[14] Prashanth L.A. et al. “Cumulative Prospect Theory Meets Reinforcement Learning: Prediction and Control”.
In:Proceedings of The 33rd International Conference on Machine Learning. Ed. by Maria Florina Balcan and
Kilian Q. Weinberger. Vol. 48. Proceedings of Machine Learning Research. New York, New York, USA: PMLR,
20–22 Jun 2016, pp. 1406–1415.url:https://proceedings.mlr.press/v48/la16.html.
[15] T.L Lai and Herbert Robbins. “Asymptotically efficient adaptive allocation rules”. In:Advances in Applied
Mathematics6.1 (1985), pp. 4–22.doi: https : / / doi . org / 10 . 1016 / 0196 - 8858(85 ) 90002 - 8.url:
https://www.sciencedirect.com/science/article/pii/0196885885900028.
[16] lin yang lin et al. “Adversarial Bandits with Corruptions: Regret Lower Bound and No-regret Algorithm”. In:
Advances in Neural Information Processing Systems. Ed. by H. Larochelle et al. Vol. 33. Curran Associates, Inc.,
2020, pp. 19943–19952.
[17] Lydia T Liu, Horia Mania, and Michael Jordan. “Competing bandits in matching markets”. In:International
Conference on Artificial Intelligence and Statistics. PMLR. 2020, pp. 1618–1628.
[18] Lydia T Liu et al. “Bandit learning in decentralized matching markets”. In:Journal of Machine Learning Research
22.211 (2021), pp. 1–34.
[19] Harry Markowitz. “Portfolio Selection”. In:The Journal of Finance7.1 (1952), pp. 77–91.url: http://www.
jstor.org/stable/2975974(visited on 01/25/2026).
[20] Laura Niss and Ambuj Tewari. “What You See May Not Be What You Get: UCB Bandit Algorithms Robust to
epsilon Contamination”. In:Conference on Uncertainty in Artificial Intelligence. PMLR. 2020, pp. 450–459.
[21] Richard Oentaryo et al. “Detecting click fraud in online advertising: a data mining approach”. In:J. Mach. Learn.
Res.15.1 (Jan. 2014), pp. 99–140.
[22] Tejas Pagare and Avishek Ghosh. “Explore-then-commit algorithms for decentralized two-sided matching
markets”. In:2024 IEEE International Symposium on Information Theory (ISIT). IEEE. 2024, pp. 2092–2097.
[23] R. Tyrrell Rockafellar and Stanislav Uryasev. “Optimization of conditional value-at risk”. In:Journal of Risk3
(2000), pp. 21–41.url:https://api.semanticscholar.org/CorpusID:854622.
[24] Abishek Sankararaman, Soumya Basu, and Karthik Abinav Sankararaman. “Dominate or Delete: Decentralized
Competing Bandits in Serial Dictatorship”. In:Proceedings of The 24th International Conference on Artificial
Intelligence and Statistics. Ed. by Arindam Banerjee and Kenji Fukumizu. Vol. 130. Proceedings of Machine
Learning Research. PMLR, 13–15 Apr 2021, pp. 1252–1260.url: https://proceedings.mlr.press/v130/
sankararaman21a.html.
[25] Abishek Sankararaman and Balakrishnan (Murali) Narayanaswamy. “Online robust non-stationary estimation”.
In:Proceedings of the 37th International Conference on Neural Information Processing Systems. NIPS ’23. New
Orleans, LA, USA: Curran Associates Inc., 2023.
[26] Abishek Sankararaman et al. “FITNESS: (Fine Tune on New and Similar Samples) to detect anomalies in streams
with drift and outliers”. In:Proceedings of the 39th International Conference on Machine Learning. Ed. by Kamalika
Chaudhuri et al. Vol. 162. Proceedings of Machine Learning Research. PMLR, 17–23 Jul 2022, pp. 19153–19177.
url:https://proceedings.mlr.press/v162/sankararaman22a.html.
[27] Vincent Y. F. Tan, Prashanth L. A., and Krishna Jagannathan.A Survey of Risk-A ware Multi-Armed Bandits. 2022.
arXiv:2205.05843 [stat.ML].url:https://arxiv.org/abs/2205.05843.
[28] Meltem Tatlı et al. “Risk-sensitive Bandits: Arm Mixture Optimality and Regret-efficient Algorithms”. In:
Proceedings of The 28th International Conference on Artificial Intelligence and Statistics. Ed. by Yingzhen Li
et al. Vol. 258. Proceedings of Machine Learning Research. PMLR, Mar. 2025, pp. 3871–3879.url: https :
//proceedings.mlr.press/v258/tatli25a.html.
[29] Amos Tversky and Daniel Kahneman. “Advances in prospect theory: Cumulative representation of uncertainty”.
In:Journal of Risk and uncertainty5.4 (1992), pp. 297–323.
[30] Zheshun Wu et al. “Bandit Learning in Matching Markets Robust to Adversarial Corruptions”. In:The Fourteenth
International Conference on Learning Representations. 2026.url: https://openreview.net/forum?id=
CoWJc5ofDO.
13

[31] Linfeng Zhang and Yong Guan. “Detecting Click Fraud in Pay-Per-Click Streams of Online Advertising
Networks”. In:Proceedings of the 2008 The 28th International Conference on Distributed Computing Systems.
ICDCS ’08. USA: IEEE Computer Society, 2008, pp. 77–84.doi: 10 . 1109 / ICDCS . 2008 . 98.url: https :
//doi.org/10.1109/ICDCS.2008.98.
14

A Additional Related Work
Markets and Bandits:A rich line of work studies bandit learning in two-sided matching markets in recent years [17,
18, 12, 13, 4, 24, 6, 9, 22] using various assumptions like serial dictatorship,𝛼-condition etc. All of these works adopt
expected reward as the performance criterion and none incorporate behavioral risk measures such as cumulative
prospect theory (CPT).
Risk Sensitive ML:Risk-sensitive objectives in bandits have been studied through mean- variance [19], spectral risk
measures [1], and utility-based shortfall risk [8]. CPT-based regret for single-player bandits was introduced in [7, 11],
while [28] studied arm mixture optimality under risk-sensitive objectives.
Adversarial Learning:On the adversarial side, corrupted bandits have been widely studied in single-player settings [2,
16], and [30] recently extended corruption robustness to matching markets. Our work bridges these two directions by
jointly addressing CPT-based risk preferences and adversarial corruption in competitive matching markets.
B Details of Algorithmic procedures
In this section, we provide the details of first and third phase mentioned in Algorithm 2.
B.1 Phase 1
In the first phase, each player obtains a unique index that determines the order in which players explore arms during
the exploration phase. All players initially propose to the first arm 𝑎1. Since each arm accepts only the player it
prefers most, the accepted player receives index1. In subsequent rounds, the players who already were assigned an
index propose to arm𝑎2, and the remaining players continue proposing to𝑎1, the accepted player for arm𝑎1 receives
the next available index. After𝑁rounds, every player obtains a distinct index.
B.2 Phase 3
In the final phase, players execute a decentralized Gale-Shapley procedure using their estimated preference rankings
obtained in Phase 2. Each player sequentially proposes to arms according to its estimated ranking until no rejection
occurs. When the rankings of the top𝑁 arms are estimated correctly, this process converges to the player-optimal
stable matching.
C Proof of Theorem 3.1
Proof. Let ˆ𝜇𝑖,𝑗(𝑡) denote the estimated preference value and𝑇𝑖,𝑗(𝑡) the number of observations of arm𝑎𝑗 for player𝑝𝑖
at the end of round𝑡, andℓ max the largest sub-phase index in Phase 2.
Define the bad eventFas follows:
F=
n
∃𝑡∈[𝑇], 𝑖∈[𝑁], 𝑗∈[𝐾]:

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 o .
15

The player optimal stable CPT-regret of𝑝𝑖 under Algorithm 2 satisfies
CPT-Reg𝑖(𝑇)=
∑︁
𝑗∈[𝐾],𝑗≠𝑚 ∗ 𝑖
E

𝑇𝑖,𝑗(𝑇)

Δ𝑖,𝑚∗ 𝑖,𝑗
≤𝑁Δ 𝑖,max+E
" 𝑇∑︁
𝑡=𝑁+1
1{ ¯𝐴𝑖(𝑡)≠𝑚 ∗ 𝑖}

¬F # Δ𝑖,max+P(F)𝑇Δ 𝑖,max.
≤𝑁Δ 𝑖,max+E
"ℓmax∑︁
ℓ=1
(2ℓ+1)+𝑁 2

¬F # Δ𝑖,max+2𝑁𝐾Δ 𝑖,max.
≤𝑁Δ 𝑖,max+

3𝐾log𝑇
Δ2/𝛼 (4𝐿𝑀) 2/𝛼+log
 3𝐾log𝑇
Δ2/𝛼 (4𝐿𝑀) 2/𝛼
 !
Δ𝑖,max
+𝑁 2Δ𝑖,max+2𝑁𝐾Δ 𝑖,max.
The last inequality follows from the bound onℓmax in Lemma C.4. The first, second, and third terms correspond to the
regret incurred in the first, second, and third phases respectively, while the fourth term captures the regret resulting
from the occurrence of the bad eventF.□
Lemma C.1([11, Theorem 1]).(Sample complexity of estimating weight-distorted reward). Assume Assumption 1 and
Assumption 2. Then for any 𝜀> 0and any 𝑗∈{ 1,...,𝐾} , we have P

 ˆ𝜇𝑖,𝑗,𝑚−𝜇𝑖,𝑗

 >𝜀 ≤ 2 exp  −2𝑚  𝜀 𝐿𝑀 2/𝛼 , where
m is the number of samples of arm j observed by player i.
Lemma C.2.
P(F)≤ 2𝑁𝐾 𝑇
Proof.Fix𝑡∈[𝑇],𝑖∈[𝑁], and𝑗∈[𝐾]. Applying Lemma C.1 with𝑚=𝑇 𝑖,𝑗(𝑡)and𝜀=𝐿𝑀

3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
,we obtain
P

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2! ≤2 exp '›››
«
−2𝑇𝑖,𝑗(𝑡)
'››
«
𝐿𝑀

3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
𝐿𝑀
“ﬁﬁ
‹
2/𝛼
“ﬁﬁﬁ
‹
.
P

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2! ≤2𝑒−3 log𝑇 = 2 𝑇 3.
P(F)≤
𝑇∑︁
𝑡=1
𝑁∑︁
𝑖=1
𝐾∑︁
𝑗=1
𝑡∑︁
𝑠=1
P

𝑇𝑖,𝑗(𝑡)=𝑠,

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑠 𝛼/2!
≤
𝑇∑︁
𝑡=1
𝑁∑︁
𝑖=1
𝐾∑︁
𝑗=1
𝑡· 2 𝑇 3 = 2𝑁𝐾 𝑇 3 ·𝑇(𝑇+1) 2 ≤ 2𝑁𝐾 𝑇 .
□
Lemma C.3([12, Lemma3]).In the offline GS algorithm, at most 𝑁 arms are proposed to by players before the algorithm
stops. Thus, the player-optimal stable arm of each player must be among its first 𝑁 -ranked arms. Moreover, the GS
algorithm reaches player-optimal stability in at most𝑁 2 steps.
16

Lemma C.4.Conditional on¬F, Phase 2 proceeds in at mostℓ max sub-phases where
ℓmax =min
(
ℓ:
ℓ∑︁
𝑟=1
2𝑟≥𝐾· 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼) .(5)
This implies ˝ℓmax 𝑟=1 2𝑟 ≤ 3𝐾log𝑇  4𝐿𝑀 Δ 2/𝛼 , and ℓmax =log  3𝐾log𝑇  4𝐿𝑀 Δ 2/𝛼 , since the sub-phase length grows
exponentially. All players enter Phase 3 simultaneously at the end of sub-phaseℓ max.
Proof. We know that in the exploration part of Phase 2 all players propose to arms in a round robin order due to
which there are no collisions. Consequently, by the end of sub-phase ℓmax defined in (5), the number of samples
satisfies
𝑇𝑖,𝑗≥ 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 ∀𝑖∈[𝑁], 𝑗∈[𝐾].
According to Lemma C.6, once this sampling threshold is reached, player𝑝𝑖 is able to determine a permutation𝜎𝑖
such that
𝑊-LCB𝑖,𝜎𝑖,𝑗(𝑡)>𝑊-UCB 𝑖,𝜎𝑖,𝑗+1(𝑡) ∀𝑗∈[𝑁],
and
𝑊-LCB𝑖,𝜎𝑖,𝑁(𝑡)>𝑊-UCB 𝑖,𝜎𝑖,𝑗(𝑡) ∀𝑗=𝑁+1,...,𝐾.
During the monitoring round of sub-phaseℓmax, each player proposes to the arm corresponding to its assigned index
and observes that|𝑂ℓmax|=𝑁 . This confirms that all players are accepted, after which they proceed simultaneously to
Phase 3. □
Lemma C.5.Conditional on¬F,𝑊-UCB 𝑖,𝑗(𝑡)<𝑊-LCB 𝑖,𝑗′(𝑡)implies𝜇 𝑖,𝑗 <𝜇 𝑖,𝑗′.
Proof.Following the definition of𝑊-LCB and𝑊-UCB in eq 4 and the condition that¬Fholds, we have
𝑊-LCB𝑖,𝑗(𝑡)= ˆ𝜇𝑖,𝑗(𝑡)−𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
≤𝜇 𝑖,𝑗,
𝜇𝑖,𝑗≤ ˆ𝜇𝑖,𝑗(𝑡)+𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
=𝑊-UCB 𝑖,𝑗(𝑡).
then
𝜇𝑖,𝑗≤𝑊-UCB 𝑖,𝑗(𝑡)<𝑊-LCB 𝑖,𝑗′(𝑡)≤𝜇 𝑖,𝑗′,
which completes the proof. □
Lemma C.6.In round 𝑡, let 𝑇𝑖(𝑡)=min 𝑗∈[𝐾] 𝑇𝑖,𝑗(𝑡), ¯𝑇𝑖 = 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 . Conditional on¬F , if 𝑇𝑖(𝑡)> ¯𝑇𝑖 , then
𝑊-LCB𝑖,𝜌𝑖,𝑗(𝑡)>𝑊-UCB 𝑖,𝜌𝑖,𝑗+1(𝑡) ∀𝑗∈[𝑁],and𝑊-LCB 𝑖,𝜌𝑖,𝑁(𝑡)>𝑊-UCB 𝑖,𝜌𝑖,𝑗(𝑡) ∀𝑗=𝑁+1,...,𝐾.
Proof.We prove the claim by contradiction. Suppose that there exists𝑘∈[𝑁]such that
𝑊-LCB𝑖,𝜌𝑖,𝑘(𝑡)≤𝑊-UCB 𝑖,𝜌𝑖,𝑘+1(𝑡),
or there exists𝑘=𝑁+1,...,𝐾for which
𝑊-LCB𝑖,𝜌𝑖,𝑁(𝑡)≤𝑊-UCB 𝑖,𝜌𝑖,𝑘(𝑡).
Let𝑗denote the arm appearing on the right-hand side of the inequality and𝑗 ′ the arm on the left-hand side.
17

Conditioned on the event¬Fand using the definitions of the confidence bounds in equation 4, we have
𝜇𝑖,𝑗′−2𝐿𝑀
 3 log𝑇
2𝑇𝑖(𝑡)
𝛼/2
≤𝑊-LCB 𝑖,𝑗′(𝑡)≤𝑊-UCB 𝑖,𝑗(𝑡)≤𝜇 𝑖,𝑗+2𝐿𝑀
 3 log𝑇
2𝑇𝑖(𝑡)
𝛼/2
.
This implies
Δ𝑖,𝑗,𝑗 ′≤4𝐿𝑀
 3 log𝑇
2𝑇𝑖(𝑡)
𝛼/2
.
SinceΔ𝑖,𝑗,𝑗 ′≥Δ, it follows that
𝑇𝑖(𝑡)≤ 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 = ¯𝑇𝑖,
which contradicts the assumption that𝑇𝑖(𝑡)> ¯𝑇𝑖. The proof is therefore complete.□
D Proof of Theorem 4.2
We begin by introducing the concentration failure event. Let
F=
(
∃1≤𝑡≤𝑇, 𝑖∈[𝑁], 𝑗∈[𝐾]:

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2)
denote the event in which the empirical reward estimate deviates from the true mean beyond the prescribed confidence
width, for at least one time step and one player-arm pair. We now proceed to establish an upper bound on the
cumulative regret.
CPT-Reg𝑖(𝑇)=E
" 𝑇∑︁
𝑡=1
(𝜇𝑖,𝑚∗ 𝑖−𝜇𝑖, ¯𝐴𝑖(𝑡))
#
≤E
" 𝑇∑︁
𝑡=1
(𝜇𝑖,𝑚∗ 𝑖−𝜇𝑖, ¯𝐴𝑖(𝑡))|¬F
#
+P(F)·𝑇·𝜇 𝑖,𝑚∗ 𝑖
≤E
 𝑇∑︁ 𝑡=1 ∑︁ 𝑎𝑗 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
+E
" 𝑇∑︁
𝑡=1
1{ ¯𝐴𝑖(𝑡)=∅}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
+P(F)·𝑇·𝜇 𝑖,𝑚∗ 𝑖
≤ 3𝑁 2 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 ·Δ𝑖,𝑚𝑎𝑥+ ∑︁ 𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 } 3 log𝑇 2 '› « (4𝐿𝑀) 2/𝛼 Δ2/𝛼−1 𝑖,𝑚∗ 𝑖,𝑗 “ﬁ ‹
+3𝑁 2 log𝑇
 4𝐿𝑀
Δ
2/𝛼
·Δ𝑖,𝑚𝑎𝑥+2𝑁𝐾·Δ 𝑖,𝑚𝑎𝑥
=𝑂

𝑁 2 log𝑇
𝐿𝑀
Δ
2/𝛼
·Δ𝑖,𝑚𝑎𝑥+𝐾log𝑇
(𝐿𝑀) 2/𝛼
Δ2/𝛼−1
!
where the final inequality follows by combining Lemma D.1, Lemma D.2, and Lemma D.4.
18

Lemma D.1.The expected regret due to playing sub-optimal arms, conditioned on the good event, satisfies
E
 𝑇∑︁ 𝑡=1 ∑︁ 𝑎𝑗∈[𝐾] 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗

 ¬F  ≤ 3𝑁 2 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 ·Δ𝑖,max
+
∑︁
𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 }
3 log𝑇
2
'›
«
(4𝐿𝑀) 2/𝛼
Δ2/𝛼−1 𝑖,𝑚∗ 𝑖,𝑗
“ﬁ
‹
.
Proof. Observe that player 𝑝𝑖 revises its available setA𝑖 each time another player 𝑝𝑖′ switches𝐸𝑖′ =False while
𝜋𝐴𝑖′,𝑖′ >𝜋 𝐴𝑖,𝑖′, as prescribed by Lines 12–13 of Algorithm 3. We write𝑡𝑠 for the round at which this revision occurs
for the𝑠-th time, and set𝑡 0 =1by convention.
Intuitively, whenever a player𝑝𝑖′ transitions𝐸𝑖′ to False, this indicates that𝑝𝑖′ has successfully identified its most
preferred arm among the currently available options. In conjunction with the good event¬F and Lemma D.6, the
arm committed to by each player during exploration is guaranteed to be their true top choice among remaining arms.
This observation reveals that the Improved CPT-ETGS algorithm operates as an online realization of the Gale-Shapley
procedure, the 𝑠-th transition of 𝐸𝑖′ to False by player 𝑝𝑖′ mirrors the event where 𝑝𝑖′ proposes to its 𝑠-th most
preferred arm in the classical offline GS. It then follows from Lemma D.3 that the total number of proposals across all
players before stability is reached cannot exceed𝑁− 1. Hence, the revision at Lines 12–13 is triggered no more than
𝑁−1times for player𝑝 𝑖.
Within each interval indexed by𝑠, spanning rounds𝑡𝑠 through𝑡𝑠+1, player𝑝𝑖 iterates over all available arms using a
round-robin scheme, progressively discarding inferior arms until𝑁 candidates remain, and subsequently locks in the
best arm among the surviving𝑁 once its identity becomes clear. To streamline the presentation, we define𝑅𝑠 as the
collection of the final𝑁 arms that𝑝𝑖 sampled withinA𝑖 via round-robin before until the condition at Line 8 satisfies,
𝐷𝑠 as the subset of arms that𝑝𝑖 discards by virtue of the condition at Line 7, and𝑗𝑠 as the arm that𝑝𝑖 locks onto from
the moment it switches𝐸𝑖 to False until round𝑡𝑠+1−1. With these definitions in hand, we can write
E
 𝑇∑︁ 𝑡=1 ∑︁ 𝑎𝑗 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
≤E
 𝑁−1∑︁ 𝑠=0 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 ∑︁ 𝑎𝑗 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
≤E
 𝑁−1∑︁ 𝑠=0 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 '› « ∑︁ 𝑎𝑗∈𝑅𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗
+
∑︁
𝑎𝑗∈𝐷𝑠
1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗+1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗𝑠}·Δ 𝑖,𝑚∗ 𝑖,𝑗𝑠 “ﬁ
‹
|¬F
 .
≤E
 𝑁−1∑︁ 𝑠=0 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 '› « ∑︁ 𝑎𝑗∈𝑅𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗+ ∑︁ 𝑎𝑗∈𝐷𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗 “ﬁ ‹ |¬F  ,
where the simplification above is justified by Lemma D.6 together with the offline GS structure before termination of
the GS procedure, arm 𝑗𝑠 is ranked above𝑚∗ 𝑖 in player𝑝𝑖’s preference, which means that the regret from playing
these arms is non-positive.
We first handle the contribution from the retained arms in the expression above. By interchanging the order of
summation, we get
19

E
 𝑁−1∑︁ 𝑠=0 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 ∑︁ 𝑎𝑗∈𝑅𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
=E
 𝑁−1∑︁ 𝑠=0 ∑︁ 𝑎𝑗∈𝑅𝑠 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
≤E
 𝑁−1∑︁ 𝑠=0 ∑︁ 𝑎𝑗∈𝑅𝑠 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠,𝑗𝑠+1 2/𝛼 ·Δ𝑖,𝑚∗ 𝑖,𝑗|¬F 
≤ 3𝑁 2 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 ·Δ𝑖,𝑚𝑎𝑥
where the penultimate step applies Lemma D.5, and the last step uses the observation that𝑅𝑠 has cardinality at most
𝑁, a direct consequence of the elimination rule (Line 7).
We now address the contribution from the eliminated arms. Given an arm𝑎𝑗 and𝑠∈{ 0,...,𝑁− 1}, we write𝑇𝑖,𝑗,𝑠 for
the value of𝑇𝑖,𝑗 upon completion of round𝑡𝑠+1− 1. When𝑠≥ 1and 𝑎𝑗∈𝐷 𝑠, provided that𝑇𝑖,𝑗,𝑠−1 ≤ 3 log𝑇 2

4𝐿𝑀
Δ𝑖,𝑗𝑠−1,𝑗
2/𝛼
,
we must have
𝑇𝑖,𝑗,𝑠 :=
∑︁
𝑠′≤𝑠
(𝑇𝑖,𝑗,𝑠′−𝑇𝑖,𝑗,𝑠′−1)≤ 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠,𝑗 2/𝛼
for arm𝑎 𝑗 to be removed fromA𝑖 at step𝑠, which follows from Lemma D.5.
In the complementary case where𝑇𝑖,𝑗,𝑠−1 > 3 log𝑇 2

4𝐿𝑀
Δ𝑖,𝑗𝑠−1,𝑗
2/𝛼
, an application of Lemma D.5 yields
𝑇𝑖,𝑗,𝑠−𝑇𝑖,𝑗,𝑠−1 ≤ 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠,𝑗 2/𝛼 − 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠−1,𝑗 2/𝛼
at the moment when𝑎 𝑗 gets eliminated.
For a given arm𝑎 𝑗, we introduce
𝑠𝑗,1 :=max 0≤𝑠≤𝑁−1 {𝑠:𝑇 𝑖,𝑗,𝑠≤ 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠,𝑗 2/𝛼 }
which identifies the latest step at which the observation count for𝑎 𝑗 has not yet surpassed the required threshold.
Using this definition, the eliminated-arm contribution can be bounded as follows:
20

E
 𝑁−1∑︁ 𝑠=0 𝑡𝑠+1−1∑︁ 𝑡=𝑡𝑠 ∑︁ 𝑎𝑗∈𝐷𝑠 1{ ¯𝐴𝑖(𝑡)=𝑎 𝑗}·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
=E
 𝑁−1∑︁ 𝑠=0 ∑︁ 𝑎𝑗∈𝐷𝑠 (𝑇𝑖,𝑗,𝑠−𝑇𝑖,𝑗,𝑠−1)·Δ 𝑖,𝑚∗ 𝑖,𝑗|¬F 
=E
 ∑︁ 𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 } '› « ∑︁ 𝑠:𝑎𝑗∈𝐷𝑠,𝑠≤𝑠 𝑗,1 (𝑇𝑖,𝑗,𝑠−𝑇𝑖,𝑗,𝑠−1)
+
∑︁
𝑠:𝑎𝑗∈𝐷𝑠,𝑠>𝑠 𝑗,1
(𝑇𝑖,𝑗,𝑠−𝑇𝑖,𝑗,𝑠−1)“ﬁ
‹
Δ𝑖,𝑚∗ 𝑖,𝑗|¬F

≤E
 ∑︁ 𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 } '› « 𝑇𝑖,𝑗,𝑠𝑗,1+ ∑︁ 𝑠:𝑎𝑗∈𝐷𝑠,𝑠>𝑠 𝑗,1 (𝑇𝑖,𝑗,𝑠−𝑇𝑖,𝑗,𝑠−1)“ﬁ ‹ Δ𝑖,𝑚∗ 𝑖,𝑗|¬F 
≤
∑︁
𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 }
'›
«
3 log𝑇
2

4𝐿𝑀
Δ𝑖,𝑗𝑠𝑗,1,𝑗
!2/𝛼
+
∑︁
𝑠:𝑎𝑗∈𝐷𝑠,𝑠>𝑠 𝑗,1

3 log𝑇
2
 4𝐿𝑀
Δ𝑖,𝑗𝑠,𝑗
2/𝛼
− 3 log𝑇 2  4𝐿𝑀 Δ𝑖,𝑗𝑠−1,𝑗 2/𝛼! “ﬁ ‹ Δ𝑖,𝑚∗ 𝑖,𝑗
≤
∑︁
𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 }
3 log𝑇
2

4𝐿𝑀
Δ𝑖,𝑚∗ 𝑖,𝑗
!2/𝛼
·Δ𝑖,𝑚∗ 𝑖,𝑗
≤
∑︁
𝑎𝑗∈K\{𝑎𝑚∗ 𝑖 }
3 log𝑇
2
'›
«
(4𝐿𝑀) 2/𝛼
Δ2/𝛼−1 𝑖,𝑚∗ 𝑖,𝑗
“ﬁ
‹
where the penultimate inequality relies on the definition of𝑠𝑗,1 combined with the telescoping argument developed
above.
□
Lemma D.2.The expected regret arising from collisions, conditioned on the good event, satisfies
E
" 𝑇∑︁
𝑡=1
1{ ¯𝐴𝑖(𝑡)=∅}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
≤3𝑁 2 log𝑇
 4𝐿𝑀
Δ
2/𝛼
·Δ𝑖,𝑚𝑎𝑥.
Proof. Under the Improved CPT-ETGS protocol, whenever𝐸𝑖 =True , the central coordinator distributes arms from
A𝑖 to player𝑝𝑖 according to a round-robin schedule. Because the pool of arms

∪𝑖:𝐸𝑖 =TrueA𝑖

 available for exploration
strictly exceeds the count ˝ 𝑖 1{𝐸𝑖 =True} of active explorers a consequence of the elimination rule at Line 7 we
may safely assume that no collisions arise during the exploration phase, as elaborated in [13]. It follows that
collision-induced regret is confined to rounds where𝐸𝑖 =False.
We write𝑡𝑠 and ¯𝑡𝑠 for the round indices at which𝑝𝑖 transitions𝐸𝑖 to False for the𝑠-th occasion and back to True for
the(𝑠+ 1)-th occasion, respectively. During any period with𝐸𝑖 =False ,𝑝𝑖 consistently proposes to its committed
arm𝐴𝑖. Let𝑗 𝑠 denote the specific arm that𝑝 𝑖 selects throughout the interval[𝑡 𝑠, ¯𝑡𝑠].
21

An important feature of the Improved CPT-ETGS algorithm is that each time an arm enters𝐷𝑖 (Line 13), previously
confidence-based eliminated arms may be restored toA𝑖. This restoration is triggered exclusively when another
player commits to its current top-ranked arm. By Lemma D.3, such restorations occur at most𝑁 times in total. For an
arbitrary player𝑝𝑖′, let𝑡′ 𝑖′,𝑟 mark the round at which𝑝𝑖′ augments𝐷𝑖′ (Line 13) for the𝑟-th time. The time points
{𝑡′ 𝑖′,𝑟}𝑟∈[𝑁] further subdivide the intervals{[𝑡𝑠, ¯𝑡𝑠]}𝑠∈[𝑁] into at most2𝑁 segments. We denote the boundaries of the
𝑠-th segment by𝑡′ 𝑠 and ¯𝑡′ 𝑠, for𝑠∈[ 2𝑁] . An application of Lemma D.5 shows that𝑝𝑖′ and𝑝𝑖 propose to the same arm
no more than 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 .times within any individual segment.
Assembling these observations, the collision regret can be controlled as follows:
E
" 𝑇∑︁
𝑡=1
1{ ¯𝐴𝑖(𝑡)=∅}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
≤E
" 𝑁∑︁
𝑠=1
¯𝑡𝑠∑︁
𝑡=𝑡𝑠
1{ ¯𝐴𝑖(𝑡)=∅}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
=E
" 𝑁∑︁
𝑠=1
¯𝑡𝑠∑︁
𝑡=𝑡𝑠
1{ ¯𝐴𝑖(𝑡)=∅,𝐴 𝑖(𝑡)=𝑗 𝑠}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
≤E
"∑︁
𝑖′≠𝑖
𝑁∑︁
𝑠=1
¯𝑡𝑠∑︁
𝑡=𝑡𝑠
1{𝐴𝑖(𝑡)=𝐴 𝑖′(𝑡)=𝑗 𝑠}·𝜇 𝑖,𝑚∗ 𝑖|¬F
#
≤E
 ∑︁ 𝑖′≠𝑖 2𝑁∑︁ 𝑠=1 ¯𝑡′ 𝑠∑︁ 𝑡=𝑡′𝑠 1{𝐴𝑖(𝑡)=𝐴 𝑖′(𝑡)}·𝜇 𝑖,𝑚∗ 𝑖|¬F 
≤
∑︁
𝑖′≠𝑖
2𝑁∑︁
𝑠=1
3 log𝑇
2
 4𝐿𝑀
Δ
2/𝛼
·𝜇 𝑖,𝑚∗ 𝑖
≤3𝑁 2 log𝑇
 4𝐿𝑀
Δ
2/𝛼
·Δ𝑖,𝑚𝑎𝑥
□
Lemma D.3([13, Lemma A.3]).Under the offline GS algorithm, the total number of proposals issued by all players prior
to termination is bounded above by𝑁−1.
Lemma D.4.The probability of the concentration failure event is bounded by
P(F)≤ 2𝑁𝐾 𝑇 .
Proof. The proof is identical to that of the corresponding lemma in Appendix C, using Lemma C.1 and a union bound
over all𝑡∈[𝑇],𝑖∈[𝑁],𝑗∈[𝐾], and𝑠∈[𝑡].□
Lemma D.5.Consider a player 𝑝𝑖 and set ¯𝑇𝑖 = 3 log𝑇 2  4𝐿𝑀 Δ 2/𝛼 . For any pair of arms 𝑗,𝑗 ′ satisfying𝜇𝑖,𝑗 >𝜇 𝑖,𝑗′ with
𝜎𝑖(𝑎𝑗)∈[1,𝜎 𝑖(𝑚∗ 𝑖)], whenever
𝑇𝑖(𝑡):=min{𝑇 𝑖,𝑗(𝑡),𝑇𝑖,𝑗′(𝑡)}> ¯𝑇𝑖,
it follows that
W-UCB𝑖,𝑗′(𝑡)<W-LCB 𝑖,𝑗(𝑡).
Proof.Proof is identical to Lemma C.6□
22

Lemma D.6.Under the event¬F, at every round𝑡,
W-UCB𝑖,𝑗(𝑡)<W-LCB 𝑖,𝑗′(𝑡)implies𝜇 𝑖,𝑗 <𝜇 𝑖,𝑗′.
Proof. Under¬F , the true value satisfiesW-LCB𝑖,𝑗(𝑡)≤𝜇 𝑖,𝑗≤W-UCB𝑖,𝑗(𝑡) for all𝑖,𝑗,𝑡 . Therefore𝜇𝑖,𝑗≤W-UCB𝑖,𝑗(𝑡)<
W-LCB𝑖,𝑗′(𝑡)≤𝜇 𝑖,𝑗′. □
E Proof of Lemma 4.1
Proof. We prove the result by reduction to the single-player distorted reward multi-armed bandit problem. Consider
an instance where all arms share the same preference ordering over players,𝑝1≻𝑝 2≻···≻𝑝 𝑁. Thus, whenever
multiple players propose to the same arm, the arm accepts the player with the highest priority.
Under this configuration, player𝑝1 always has priority over all other players and therefore interacts with the arms
without competition. Consequently, the learning problem faced by𝑝1 reduces to a classical stochastic multi-armed
bandit problem with𝐾arms and distorted rewards.
For such CPT distorted bandits, Theorem 3 of [11] establishes that any uniformly efficient algorithm must satisfy
lim inf
𝑇→∞
E[CPT-Reg1(𝑇)]
log𝑇 ≥
∑︁
𝑗∈[𝐾],𝑗≠𝑚 ∗ 1
(𝐿𝑀) 2/𝛼
4Δ2/𝛼−1 1,𝑚∗ 1,𝑗 ,
which completes the proof. □
F Proof of Theorem 5.2
Lemma F.1.Let ˜𝜇𝑖,𝑗 denote the oracle empirical weight-distorted reward computed using the stochastic (uncorrupted)
rewards𝑌 𝑠 𝑖,𝑗 , and let ˆ𝜇𝑖,𝑗 denote the empirical weight-distorted reward computed using the corrupted rewards𝑌 𝑖,𝑗 .
Assuming rewards are non-negative by Assumption 4. Then only the positive distortion terms contribute to the estimator.
Under this setting, the difference between the oracle and corrupted empirical estimators satisfies

 ˆ𝜇𝑖,𝑗− ˜𝜇𝑖,𝑗

≤ 𝐶𝐿 𝑇𝛼 𝑖,𝑗 .
Proof.The oracle empirical weight-distorted estimator is
˜𝜇𝑖,𝑗 =
𝑇𝑖,𝑗∑︁
𝑘=1
𝑌𝑠 [𝑖,𝑗,𝑘]

𝑤
𝑇𝑖,𝑗−𝑘+1
𝑇𝑖,𝑗

−𝑤
𝑇𝑖,𝑗−𝑘
𝑇𝑖,𝑗

,
while the estimator computed from corrupted rewards is
ˆ𝜇𝑖,𝑗 =
𝑇𝑖,𝑗∑︁
𝑘=1
𝑌[𝑖,𝑗,𝑘]

𝑤
𝑇𝑖,𝑗−𝑘+1
𝑇𝑖,𝑗

−𝑤
𝑇𝑖,𝑗−𝑘
𝑇𝑖,𝑗

Taking the absolute difference and applying the triangle inequality gives

 ˆ𝜇𝑖,𝑗− ˜𝜇𝑖,𝑗

≤ 𝑇𝑖,𝑗∑︁
𝑘=1

𝑌[𝑖,𝑗,𝑘] −𝑌 𝑠 [𝑖,𝑗,𝑘]

𝑤 𝑇𝑖,𝑗−𝑘+1 𝑇𝑖,𝑗  −𝑤 𝑇𝑖,𝑗−𝑘 𝑇𝑖,𝑗 

.
23

Using the Hölder continuity of the distortion function𝑤(·), each weight difference satisfies

𝑤  𝑘 𝑇𝑖,𝑗  −𝑤 𝑘−1 𝑇𝑖,𝑗 

≤ 𝐿 𝑇𝛼 𝑖,𝑗 .
Since sorting does not increase the total absolute deviation between sequences ˝𝑇𝑖,𝑗 𝑘=1|𝑌[𝑖,𝑗,𝑘] −𝑌 𝑠 [𝑖,𝑗,𝑘]|≤ ˝𝑇𝑖,𝑗 𝑘=1|𝑌𝑖,𝑗,𝑘−
𝑌𝑠 𝑖,𝑗,𝑘|≤𝐶, where the last inequality follows from the corruption budget. Combining these bounds:

 ˆ𝜇𝑖,𝑗− ˜𝜇𝑖,𝑗

≤ 𝐿 𝑇𝛼 𝑖,𝑗 ·𝐶= 𝐶𝐿 𝑇𝛼 𝑖,𝑗 .
□
Lemma F.2.The upper bound for the probability of inaccurately estimating preferences is
P(F)≤ 2𝑁𝐾 𝑇 .
Proof.
P(F)≤P

∃𝑡,𝑖,𝑗:

 ˆ𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 + 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡) !
≤P

∃𝑡,𝑖,𝑗:

 ˜𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

+

 ˆ𝜇𝑖,𝑗(𝑡)− ˜𝜇𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 + 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡) !
≤P

∃𝑡,𝑖,𝑗:

 ˜𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2!
+P

∃𝑡,𝑖,𝑗:

 ˆ𝜇𝑖,𝑗(𝑡)− ˜𝜇𝑖,𝑗

 > 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡)
!
=P

∃𝑡,𝑖,𝑗:

 ˜𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2!
≤
∑︁
𝑡
∑︁
𝑖
∑︁
𝑗
𝑡∑︁
𝑠=1
P

𝑇𝑖,𝑗(𝑡)=𝑠,

 ˜𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2!
≤
∑︁
𝑡∈[𝑇]
∑︁
𝑖∈[𝑁]
∑︁
𝑗∈[𝐾]
𝑡·2 exp(−3 ln𝑇)
≤ 2𝑁𝐾 𝑇 ,
The equality follows from the definition of the corruption budget 𝐶, which ensures that

 ˆ𝜇𝑖,𝑗(𝑡)− ˜𝜇𝑖,𝑗

≤ 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡) by
Lemma F.1. The exponential bound is obtained by using Lemma C.1
□
Lemma F.3.Conditional on¬F,
W-UCB𝑖,𝑗(𝑡)<W-LCB 𝑖,𝑗′(𝑡) ⇒𝜇 𝑖,𝑗 <𝜇 𝑖,𝑗′.
24

Proof.Condition on the event¬F. Then for every𝑡∈[𝑇],𝑖∈[𝑁], and𝑗∈[𝐾], the estimator ˜𝜇𝑖,𝑗(𝑡)satisfies

 ˜𝜇𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

≤𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 .
We first derive a lower bound on the confidence interval. Using the definition of LCB𝑖,𝑗(𝑡) and Lemma F.1, we obtain
LCB𝑖,𝑗(𝑡)= ˆ𝜇𝑖,𝑗(𝑡)−𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
− 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡)
≤ ˜𝜇𝑖,𝑗(𝑡)−𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
≤𝜇 𝑖,𝑗.
Similarly, for the upper confidence bound we have
𝜇𝑖,𝑗≤ ˜𝜇𝑖,𝑗(𝑡)+𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
≤ ˆ𝜇𝑖,𝑗(𝑡)+𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 𝐶𝐿 𝑇𝛼 𝑖,𝑗(𝑡) =UCB𝑖,𝑗(𝑡).
Therefore, under¬F, the true value𝜇 𝑖,𝑗 lies inside the confidence interval[LCB 𝑖,𝑗(𝑡),UCB 𝑖,𝑗(𝑡)]. Consequently,
𝜇𝑖,𝑗≤UCB 𝑖,𝑗(𝑡)<LCB 𝑖,𝑗′(𝑡)≤𝜇 𝑖,𝑗′.
This completes the proof. □
Lemma F.4.In round𝑡, let𝑇 𝑖(𝑡)=min 𝑗∈[𝐾] 𝑇𝑖,𝑗(𝑡)and
¯𝑇𝑖 = 3 log𝑇 2Δ 2/𝛼(8𝐿𝑀) 2 𝛼+  8𝐶𝐿 Δ  1 𝛼
Conditional on¬F, if𝑇 𝑖(𝑡)> ¯𝑇𝑖 , we have
W-LCB𝑖,𝜌𝑖,𝑘(𝑡)>W-UCB 𝑖,𝜌𝑖,𝑘+1(𝑡),∀𝑘∈[𝑁],
and
W-LCB𝑖,𝜌𝑖,𝑁(𝑡)>W-UCB 𝑖,𝜌𝑖,𝑘(𝑡),∀𝑘=𝑁+1,𝑁+2,...,𝐾.
Proof. Assume for contradiction that the ordering induced by the confidence bounds is violated. That is, there exists
𝑘∈[𝑁]such that
W-LCB𝑖,𝜌𝑖,𝑘(𝑡)≤W-UCB 𝑖,𝜌𝑖,𝑘+1(𝑡),
or there exists𝑘∈{𝑁+1,...,𝐾}for which
W-LCB𝑖,𝜌𝑖,𝑁(𝑡)≤W-UCB 𝑖,𝜌𝑖,𝑘(𝑡).
Let𝑗 ′ denote the arm corresponding to the left-hand side of the inequality and𝑗the arm on the right-hand side.
Condition on the event¬F. By the definition of the weighted confidence bounds, the true means satisfy
W-LCB𝑖,𝑗′(𝑡)≥𝜇 𝑖,𝑗′−2𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
− 2𝐶𝐿 𝑇𝛼 𝑖 (𝑡),
W-UCB𝑖,𝑗(𝑡)≤𝜇 𝑖,𝑗+2𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 2𝐶𝐿 𝑇𝛼 𝑖 (𝑡).
25

Combining these inequalities with the assumed violation of the ordering yields
𝜇𝑖,𝑗′−𝜇𝑖,𝑗≤4𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 4𝐶𝐿 𝑇𝛼 𝑖 (𝑡).
Recall thatΔ 𝑖,𝑗,𝑗 ′ =𝜇 𝑖,𝑗′−𝜇𝑖,𝑗 . Hence
Δ𝑖,𝑗,𝑗 ′≤4𝐿𝑀
 3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 4𝐶𝐿 𝑇𝛼 𝑖 (𝑡).
Now consider the case where
𝑇𝑖(𝑡)> 3 log𝑇 2Δ 2/𝛼(8𝐿𝑀) 2/𝛼+  8𝐶𝐿 Δ 1/𝛼 .
Substituting this lower bound into the right-hand side above gives
Δ𝑖,𝑗,𝑗 ′ < Δ 2+ Δ 2 =Δ.
However, by definition the gap satisfies Δ𝑖,𝑗,𝑗 ′≥Δ , which leads to a contradiction. Therefore the assumed violation
cannot occur, and the ordering induced by the confidence bounds must hold whenever𝑇𝑖(𝑡)> ¯𝑇𝑖.□
Proof. (of Theorem 5.2)In Algorithm 2, players propose to arms in a round-robin manner during Phase 2. As a result,
no collisions occur, and every player is successfully matched in each exploration round. Consequently, all players
transition to Phase 3 simultaneously. Letℓmax denote the largest sub-phase index of Phase 2, after which the players’
preference rankings are estimated accurately. The optimal stable regret for player i can be bounded as follows,
CPT-Reg𝑖(𝑇)=E
"∑︁
𝑡
(𝜇𝑖,𝑚∗ 𝑖−𝜇𝑖, ¯𝐴𝑖(𝑡))
#
≤E
"∑︁
𝑡
I{ ¯𝐴(𝑡)≠𝑚 ∗}·Δ 𝑖,max
#
≤𝑁Δ 𝑖,max+E
" 𝑇∑︁
𝑡=𝑁+1
I{ ¯𝐴(𝑡)≠𝑚 ∗}

¬F # ·Δ𝑖,max+P(F)·𝑇·Δ 𝑖,max
≤𝑁Δ 𝑖,max+E
"𝐿max∑︁
𝑘=1
(2𝑘+1)+𝑁 2

¬F # ·Δ𝑖,max+P(F)·𝑇·Δ 𝑖,max
≤𝑁Δ 𝑖,max+E
"𝐿max∑︁
𝑘=1
(2𝑘+1)+𝑁 2

¬F # ·Δ𝑖,max+2𝑁𝐾·Δ 𝑖,max.
The last inequality follows from Lemma F.2.
From Lemma F.4, Phase 2 terminates after at most𝐿 max sub-phases, where
𝐿max =min
(
𝑘:
𝑘∑︁
𝑘′=1
𝑑𝑘′≥ 3𝐾log𝑇 2Δ 2/𝛼 (8𝐿𝑀) 2 𝛼+𝐾  8𝐶𝐿 Δ  1 𝛼 ) .
26

Recall that in Algorithm 2 the exploration length of the𝑘-th sub-phase grows geometrically, i.e.,𝑑𝑘 = 2𝑘. Using this
definition, the cumulative exploration length up to sub-phase𝐿 max satisfies
𝐿max∑︁
𝑘′=1
2𝑘′ ≤ 3𝐾log𝑇 Δ2/𝛼 (8𝐿𝑀) 2 𝛼+2𝐾  8𝐶𝐿 Δ  1 𝛼 .
Consequently, the number of sub-phases can be bounded by
𝐿max =log

3𝐾log𝑇
Δ2/𝛼 (8𝐿𝑀)
2
𝛼+2𝐾
 8𝐶𝐿
Δ
 1
𝛼
!
.
Using this bound on𝐿 max, the regret of player𝑖can be bounded as
CPT-Reg𝑖(𝑇)≤

(8𝐿𝑀) 2/𝛼 3𝐾log𝑇
Δ2/𝛼 +2𝐾
 8𝐶𝐿
Δ
1/𝛼
+log

(8𝐿𝑀) 2/𝛼 3𝐾log𝑇
Δ2/𝛼 +2𝐾
 8𝐶𝐿
Δ
1/𝛼 !!
Δ𝑖,max
+𝑁Δ 𝑖,max+𝑁 2Δ𝑖,max+2𝑁𝐾Δ 𝑖,max.
□
G Proof of Theorem 5.3
For every layerℓ∈[log𝑇] , we use the notation ˆ𝜇ℓ 𝑖,𝑗(𝑡) ,𝑇ℓ 𝑖,𝑗(𝑡) , UCBℓ 𝑖,𝑗(𝑡) , LCBℓ 𝑖,𝑗(𝑡) to represent the values of ˆ𝜇ℓ 𝑖,𝑗 ,𝑇ℓ 𝑖,𝑗 ,
UCBℓ 𝑖,𝑗 andLCBℓ 𝑖,𝑗 upon completion of round𝑡, respectively. We introduce the following event:
Fℓ 𝑆 =
(
∃𝑡∈[𝑇],𝑖∈[𝑁],𝑗∈[𝐾]:

 ˆ𝜇ℓ 𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 + 2𝑑𝐿log𝑇 (𝑇ℓ 𝑖,𝑗(𝑡))𝛼 )
which captures the scenario where some preference estimate deviates significantly from its true value over the
time horizon for layer ℓ. Additionally, letF𝐶 denote the event that there exists an ETGS instance across layers ℓ,
ℓ′∈[log𝑇] with sampling probability satisfying2−ℓ′ ≤ 1/𝐶, such that the cumulative corruption actually incurred
by some player within this instance exceeds𝑑log𝑇+2. We then define the overall failure event as
F= '›
«
Ø
ℓ∈[log𝑇]
Fℓ 𝑆 “ﬁ
‹
∪F𝐶.
We now proceed to derive an upper bound on the probability of the failure eventF.
Lemma G.1([30, Lemma3.3]).In Algorithm 4, the ETGS instance with sampling probability less than1 /𝐶 experiences,
w.p. at least1−1/𝑇, cumulative corruption bounded by𝑑log(𝑇)+2during the exploration phase.
Lemma G.2.The probability of the failure eventFsatisfies the following upper bound:
P(F)≤ 2𝑁𝐾log𝑇 𝑇 + 𝑁log𝑇 𝑇 .
27

Proof. We begin by introducing the notation𝐶ℓ 𝑖(𝑇) to denote the total corruption experienced by player𝑖 in theℓ-th
ETGS instance. Since the constant𝑑 is chosen so that𝑑log𝑇+ 2≤ 2𝑑log𝑇 , the probability of the failure eventF can
be bounded as follows:
P(F)≤
∑︁
ℓ∈[log𝑇]
P(F ℓ 𝑆)+P(F 𝐶)
≤
∑︁
ℓ∈[log𝑇]
P

∃𝑡,𝑖,𝑗:

 ˆ𝜇ℓ 𝑖,𝑗(𝑡)−𝜇 𝑖,𝑗

 >𝐿𝑀  3 log𝑇 2𝑇𝑖,𝑗(𝑡) 𝛼/2 + 2𝑑𝐿log𝑇 (𝑇ℓ 𝑖,𝑗(𝑡))𝛼 !
+
∑︁
ℓ:2−ℓ≤1/𝐶
P∃𝑖:𝐶 ℓ 𝑖(𝑇)>2𝑑log(𝑇) 
≤
∑︁
ℓ∈[log𝑇]
∑︁
𝑡∈[𝑇]
∑︁
𝑖∈[𝑁]
∑︁
𝑗∈[𝐾]
𝑡·2 exp(−3 ln𝑇)+
∑︁
𝑖∈[𝑁]
log𝑇
𝑇
≤ 2𝑁𝐾log𝑇 𝑇 + 𝑁log𝑇 𝑇 .
By virtue of Lemma G.1, we can conclude that the actual corruption sustained by layersℓ for which2ℓ≥𝐶 ,ℓ∈[log𝑇] ,
does not exceed𝑑log𝑇+ 2. Given that the constant𝑑 is selected to ensure𝑑log𝑇+ 2≤ 2𝑑log𝑇 , and the confidence
interval is set to𝐿𝑀

3 log𝑇
2𝑇𝑖,𝑗(𝑡)
𝛼/2
+ 2𝑑𝐿log𝑇 (𝑇ℓ 𝑖,𝑗(𝑡)) 𝛼 the following results are an immediate consequence.□
Lemma G.3.At round𝑡, define
𝑇ℓ 𝑖(𝑡)=min 𝑗∈[𝐾] 𝑇ℓ 𝑖,𝑗(𝑡)
together with
¯𝑇ℓ 𝑖 = 3 log𝑇 2  8𝐿𝑀 Δ  2 𝛼 +  16𝑑𝐿log𝑇 Δ  1 𝛼
Under the event¬F, whenever𝑇 ℓ 𝑖(𝑡)> ¯𝑇ℓ 𝑖 , the following separation holds:
LCBℓ 𝑖,𝜌𝑖,𝑗(𝑡)>UCB ℓ 𝑖,𝜌𝑖,𝑗+1(𝑡)for any𝑗∈[𝑁],
and moreover,
LCBℓ 𝑖,𝜌𝑖,𝑁(𝑡)>UCB ℓ 𝑖,𝜌𝑖,𝑗(𝑡)for any𝑗=𝑁+1,𝑁+2,...,𝐾.
Proof. The argument follows the same structure as the proof of Lemma F.4. Assume for contradiction that the ordering
is violated. Under¬F, expanding the confidence bounds gives
Δ𝑖,𝑗,𝑗 ′≤4𝐿𝑀
 3 log𝑇
2𝑇ℓ 𝑖(𝑡)
𝛼/2
+ 8𝑑𝐿log𝑇 (𝑇ℓ 𝑖(𝑡))𝛼 .
Substituting𝑇ℓ 𝑖(𝑡)> ¯𝑇ℓ 𝑖 = 3 log𝑇 2  8𝐿𝑀 Δ 2/𝛼 +  16𝑑𝐿log𝑇 Δ 1/𝛼 into each term yields Δ𝑖,𝑗,𝑗 ′ <Δ/ 2+Δ/ 2 =Δ , contradicting
Δ𝑖,𝑗,𝑗 ′≥Δ. □
28

Proof. (of Theorem 5.3)The stable regret for player 𝑖 under the optimal matching admits the following decomposition:
CPT-Reg𝑖(𝑇)=E
"∑︁
𝑡
(𝜇𝑖,𝑚∗ 𝑖−𝜇𝑖, ¯𝐴𝑖(𝑡))
#
≤E
"∑︁
𝑡
1{ ¯𝐴(𝑡)≠𝑚 ∗}·Δ 𝑖,max
#
≤𝑁Δ 𝑖,max+E
" 𝑇∑︁
𝑡=𝑁+1
1{ ¯𝐴(𝑡)≠𝑚 ∗}|F 𝑐
#
Δ𝑖,max+P(F)𝑇Δ 𝑖,max
≤(𝑁+2𝑁𝐾log𝑇+𝑁log𝑇)Δ 𝑖,max
+E
" 𝑇∑︁
𝑡=𝑁+1
1{ ¯𝐴(𝑡)≠𝑚 ∗}|F 𝑐
#
Δ𝑖,max,
where the final inequality is obtained by applying Lemma G.2.
We now analyze separately the regret arising from layers whose actual corruption remains below𝐶, and the regret
from layers that lack sufficient robustness to handle corruption level𝐶. To this end, we introduce the smallest layer
index that provides robustness against corruption:
ℓ∗ :=arg min
ℓ
{2ℓ >𝐶}.
For the robust layersℓ′≥ℓ∗, combining Lemma G.1 with Lemma G.2 yields a regret upper bound of

3𝐾log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+𝐾
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max.
As the total number of layers is bounded bylog𝑇, the aggregate regret from all robust layers satisfies
𝐾log𝑇

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max.
Turning to the layersℓ<ℓ ∗ that cannot tolerate corruption level𝐶 (i.e., those with2ℓ <𝐶 ), we observe that the stable
matchings computed by these faster layers are eventually overridden to coincide with that of layerℓ∗, once the latter
has accurately estimated its preference rankings.
In expectation, this synchronization cost is at most𝐶·𝑇 ℓ∗ 𝑖,𝑗 , since each action taken by layerℓ∗ occurs with probability
1/𝐶among the moves that constitute arm𝑗matchings under the optimal stable matching for the faster algorithms.
More precisely, let𝑇ℓ∗ 𝑖,𝑗 denote the number of rounds in which the optimal layer is active. In expectation, the layers
ℓ<ℓ ∗ complete their preference rank estimation before layerℓ∗ does. Consequently, we obtain
E[ ˜𝑇𝑖,𝑗]= 1 𝑃ℓ∗ 𝑇ℓ∗ 𝑖,𝑗−𝑇 ℓ∗ 𝑖,𝑗 =𝐶𝑇 ℓ∗ 𝑖,𝑗−𝑇 ℓ∗ 𝑖,𝑗 ≤𝐶𝑇 ℓ∗ 𝑖,𝑗.
where ˜𝑇𝑖,𝑗 represents the total number of rounds in which layersℓ<ℓ ∗ are selected.
Combining the above, the total regret attributable to the faster layers is bounded by
𝐾𝐶

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max.
29

Following the structure of our algorithm, the number of sub-phases within Phase 2 is at most
'››››››
«
𝐾
𝑑 log𝑇

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
+ 𝐾𝐶 𝑑

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
“ﬁﬁﬁﬁﬁﬁ
‹
which leads to an overall communication cost of
'››››››
«
𝐾log 2𝑇
𝑑

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
+ 𝐾𝐶log𝑇 𝑑

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
“ﬁﬁﬁﬁﬁﬁ
‹
Collecting all terms, the regret upper bound for the Multi-layer ETGS algorithm is given by
CPT-Reg𝑖(𝑇)≤(𝑁+𝑁 2 log𝑇+2𝑁𝐾log𝑇+𝑁log𝑇)Δ 𝑖,max
+𝐾log𝑇

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
+𝐾𝐶

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
+ 𝐾log 2𝑇 𝑑  3 log𝑇 2  8𝐿𝑀 Δ  2 𝛼 +  16𝑑𝐿log𝑇 Δ  1 𝛼 ! Δ𝑖,max
+ 𝐾𝐶log𝑇 𝑑

3 log𝑇
2
 8𝐿𝑀
Δ
 2
𝛼
+
 16𝑑𝐿log𝑇
Δ
 1
𝛼
!
Δ𝑖,max
=𝑂

𝐾𝐶

log𝑇+ log2𝑇 𝑑  𝐿𝑀 Δ  2 𝛼
+𝐾(log𝑇+𝐶)

1+ log𝑇 𝑑  (log𝑇) 1 𝛼 𝑑𝐿 Δ  1 𝛼  Δ𝑖,max  .
□
30
