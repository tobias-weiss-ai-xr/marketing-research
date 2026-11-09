---
title: Can Reinforcement Learning Efficiently Discover Price Manipulation?
url: https://arxiv.org/abs/2607.06121
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Ioanna-Yvonni Tsaknaki
- Andrea Macrì
- Fabrizio Lillo
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.06121
pages: 30
chars: 63027
fetched_at: '2026-11-08T13:23:23+00:00'
kb_version: 1
---

# Can Reinforcement Learning Efficiently Discover Price Manipulation?

Can Reinforcement Learning Efficiently
Discover Price Manipulation?
Ioanna-Yvonni Tsaknaki, Andrea Macr ` ı, and Fabrizio Lillo
Scuola Normale Superiore, Piazza dei Cavalieri 7, Pisa 56126, Italy.
Abstract
In this paper, we investigate whether a model-free RL agent can identify and
exploit price manipulation opportunities more effectively than a traditional model-
based approach that assumes correct specification of the data-generating process
but relies on noisy parameter estimates. We consider a single-asset market in
which prices evolve according to an Almgren–Chriss framework with non-linear
permanent impact and linear temporary impact. We first establish the existence
of price-manipulative strategies in discrete time and compute the optimal bench-
mark strategy using Sequential Least Squares Quadratic Programming under full
information. We then compare two finite-sample learning approaches: a model-
based procedure that estimates impact parameters from simulated execution data
and an agnostic RL approach based on Deep Deterministic Policy Gradient, trained
directly on the same amount of data. For intermediate volatility, the RL agent suc-
cessfully discovers profitable manipulative strategies without explicit knowledge of
the underlying model, even when training data are quite limited. More importantly,
RL consistently outperforms the model-based approach when parameter estimates
are affected by sampling error, despite the latter benefiting from the correct model
specification. For large volatility, all methods are unable to identify manipulation
opportunities, while for small volatility, the model based approach outperforms RL.
These findings highlight both the effectiveness of RL in complex control problems
and the risks associated with deploying learning algorithms in financial markets
without appropriate safeguards.
1 Introduction
The increasing use of autonomous algorithmic trading systems has transformed mod-
ern financial markets. Reinforcement Learning (RL) methods, in particular, have at-
tracted growing attention because of their ability to learn adaptive trading policies di-
rectly from market interaction. While these techniques offer significant advantages in
high-dimensional and partially observed environments, they also raise important concerns
for regulators. Since RL agents optimize rewards without explicit economic understand-
ing or regulatory awareness, they may discover trading behaviours that are profitable
but potentially manipulative. As emphasized by Wellman and Rajan (2017) and Azzutti
et al. (2021) autonomous trading agents may create new forms of market abuse and chal-
lenge traditional regulatory frameworks designed around human intent and accountability.
1
arXiv:2607.06121v1  [q-fin.TR]  7 Jul 2026

Recent research in market manipulation and market microstructure has highlighted the
vulnerability of electronic markets to algorithmic strategies capable of distorting price for-
mation and exploiting structural weaknesses of limit order book environments Lee et al.
(2013). In modern electronic markets, even relatively simple algorithmic trading rules can
artificially influence short-term prices and induce predictable reactions from other market
participants. Such behaviours may undermine market integrity and generate misleading
signals regarding supply and demand. Moreover, recent studies suggest that reinforce-
ment learning agents may autonomously discover manipulative trading strategies purely
through reward maximization and repeated interaction with the environment Mart ´ ınez-
Miranda et al. (2016); Mizuta (2020). Specifically in Mart ´ ınez-Miranda et al. (2016) they
predefine honest and manipulative actions, such as spoofing and pinging and use RL
to determine when those already-defined actions are optimal under different transaction
costs, penalties, and liquidity conditions. The actual price-manipulation mechanism is
assumed in the model rather than learned by the agent. On the other hand, in Mizuta
(2020) a genetic algorithm discovers a pump-and-dump pattern through feedback with
trend-following agents in an artificial market. This differentiates us since we explicitly
model non-linear permanent market impact and show that a model-free DDPG agent can
recover such strategies in a continuous-action environment.
One potential source of manipulation arises from the presence of non-linear market
impact, which is the reaction of prices to trades. A large empirical literature such as
Lillo et al. (2003); Potters and Bouchaud (2003); Lillo et al. (2004) and Zhou (2012)
documents that instantaneous market impact is typically a non-linear function of volume
for individual trades, typically with an odd and concave shape. While these effects are
well established empirically, they may also create environments in which trading activity
can influence prices in exploitable ways. In particular, non-linear impact can reintroduce
the possibility of dynamic arbitrage 1, allowing round-trip trading strategies, those with
zero initial and terminal inventory, to generate positive expected cash flow purely through
their impact on prices. This phenomenon, commonly referred to as price manipulation,
was formalized by Huberman and Stanzl (2004) and further explored in continuous-time
settings by Gatheral (2010) and Gueant (2016). Understanding when and how such
manipulation arises remains a central question in market microstructure.
Although one can often find mathematically price manipulations for a given impact
model, their identification from market data poses several challenges. First, the true Data
Generating Process (DGP) of the price and trade dynamics is unknown, and models rep-
resent at most a stylized description of reality. Second, even when the DGP is known, its
parameters must be estimated from a finite sample of data. The error in their estima-
tion can severely undermine the manipulation opportunities. Thus, the mere existence of
manipulations does not imply a systematically profitable strategy.
RL offers an intriguing alternative since it is learning based and model-free.Rather
than postulating a model and estimating the parameters on a finite sample, it uses this
sample to directly identify the policy that maximizes the reward. It is therefore natural to
ask whether RL based manipulation identification outperforms in finite sample the model
based approach, even under the correct DGP specification. This is the main question we
answer in this paper.
The use of RL methods for optimal execution and trading, where actions correspond to
1Dynamic arbitrage exists if a trader can buy and sell over time, end with no inventory, and still make
positive expected profit purely from the market-impact dynamics.
2

trading rates, is widespread, both in academia and in industry. The Deterministic Policy
Gradient framework introduced by Silver et al. (2014) and its deep learning extension,
Deep Deterministic Policy Gradient (DDPG) by Lillicrap et al. (2016), enable efficient
learning in continuous action spaces. These methods have been successfully applied to
optimal execution and portfolio management tasks (see, e.g., Jiang et al. (2017); Moody
and Saffell (2001); Micheli and Monod (2024)). Early applications of RL to trading in-
clude Nevmyvaka et al. (2006), who applied Q-learning to execution problems, and more
recent work such as Hendricks and Wilcox (2014) and Ning et al. (2021), which demon-
strate the effectiveness of deep RL methods in complex market environments. Extensions
incorporating realistic features such as stochastic liquidity and partial observability have
been studied in Macr ` ı and Lillo (2025) and Macr ` ı et al. (2025), respectively.
The use of RL in financial markets presents several criticalities, since algorithmic
trading systems must operate within strict regulatory frameworks designed to prevent
manipulation and ensure market integrity. In fact, as pointed out in a recent work by
Cartea et al. (2023), the risk of unintentional market manipulation exists, especially when
learning algorithms converge to strategies that artificially influence prices in order to in-
crease profits. This phenomenon is closely related to the broader problem of reward
misspecification in machine learning, where the objective function does not fully capture
the desired behaviour of the agent. In the context of optimal execution, an RL agent
trained to maximize trading profits may inadvertently learn to exploit non-linear impact
effects, effectively engaging in dynamic arbitrage even when such behaviour is undesir-
able or unrealistic, simply following a reward maximisation logic while learning from the
environment.
Motivated by these considerations, this paper examines whether an RL agent is more
effective than a traditional model-based strategy, which assumes correct model specifica-
tion but faces parameter uncertainty arising from finite-sample estimation, in generating
positive expected cash flows through price manipulation in a market characterized by non-
linear price impact. We consider a single-asset setting, where the price evolves according
to an Almgren-Chriss (AC) type model (Almgren and Chriss, 2000) with non-linear per-
manent impact and linear temporary impact (i.e. quadratic temporary impact costs). The
agent is constrained to follow a round-trip strategy, meaning that it starts and ends with
zero inventory over a finite trading horizon. This constraint ensures that any profit must
arise purely from trading dynamics rather than directional exposure. Leveraging on this
framework, and extending Gueant (2016), by considering discrete time and non-vanishing
temporary impact costs, we first prove the existence of manipulative strategies from a the-
oretical perspective, showing that non-linear impact functions can indeed admit solutions
with positive expected cash flow even when only two trading velocities are allowed. Due
to the non-convexity of the optimization problem, we numerically find the general optimal
strategy by using Sequential Least Squares Quadratic Programming (SLSQP), assuming
full knowledge of the model parameters. The SLSQP algorithm has been used previously
for the solution of optimal execution problem for the non linear transient impact model
in Curato et al. (2017). This provides a benchmark solution against which learning-based
methods can be compared.
We then consider the problem of learning to manipulate the price from a finite sample
of data and we compare two approaches. The first is the model based one: we use a
finite sample of simulated TW AP execution to estimate the temporary and permanent
impact parameters following the approach proposed by Almgren et al. (2005). Notice
that in this approach the correct DGP is known and only the parameters are estimated.
3

We then use them to implement the optimal manipulation strategies obtained with the
SLSQP optimization on a test set of simulations. The second approach is model free and
based on RL: we train a DDPG algorithm to learn directly to manipulate the price on a
finite sample of the same size of the one of TW AP executions. Then, as before, we test
the learned strategy on a test set. For both approaches, the critical variable is volatility
since, depending on its level, it preventsan accurate estimation of impact parameters or
an effective learning of the strategy, respectively.
Our first finding is that the RL agent is capable of discovering trading strategies
that yield positive expected cash flow, effectively identifying price-manipulative behav-
iors without explicit knowledge of the model, also when the training set is relatively small
and volatility is not too large. More importantly, the numerical results show that the
performance of the RL-based strategy is superior to the one of the model based approach
when impact parameters are noisily estimated from data. The superiority of RL is ob-
served when volatility is not too low, because otherwise the parameter estimation of the
model based approach is extremely accurate and therefore the method is equivalent to an
exact optimization of a well specified DGP. It is important to stress that the central ques-
tion of the paper is therefore not whether manipulation exists theoretically, but whether
an RL algorithm can independently learn to exploit these market vulnerabilities, when
they are present, and if it can outperform a traditional model based approach.
These results highlight both the effectiveness of RL in solving complex control prob-
lems and the potential risks associated with its unsupervised deployment in financial
markets. In particular, they underscore the need for a careful design of reward func-
tions and regulatory safeguards to prevent potentiallyunintendedmarket manipulation
adopted by learning algorithms. From a broader perspective, this work extends the liter-
ature on non-linear market impact and dynamic arbitrage by demonstrating how modern
learning algorithms can exploit these features in practice. At the same time, it connects
to the growing body of research on the safety and robustness of machine learning systems,
emphasizing the importance of aligning algorithmic objectives with market stability and
regulatory requirements.
The rest of the paper is organized as follows. In Section 2, we formulate the prob-
lem and demonstrate the existence of a manipulative solution involving only two trading
velocities. In Section 3, we introduce the SLSQP numerical optimizer and present its ma-
nipulative solution under full information of the trading environment. We also illustrate
the complexity of the problem and assess its performance under partial information. In
Section 4, we introduce the DDPG algorithm. Finally, in Section 5, we compare all the
methods.
2 Framework of the Problem
In this section, we provide a general framework for the problem of dynamic arbitrage. We
define the market model with non-linear permanent impact in discrete time, the trading
cost structure, and finally we provide a solution to the case where the trader can trade
with just two velocities.
We consider the problem of a risk-neutral agent seeking an optimal trading strategy
over a finite time horizon, subject to zero initial and terminal inventory. The agent is
allowed to both buy and sell during the trading period, and therefore aims to construct
around-tripstrategy. The trading horizon is divided intoTsubintervals, each assumed,
4

for simplicity, to have length ∆t= 1.
We assume that the price dynamics follow an AC model with non-linear permanent
impact, namely:
St =S t−1 +f(v t)∆t+σ
√
∆tξt, ξ t ∼ N(0,1) (1)
˜St =S t−1 +κv t, κ >0 (2)
whereS t is the market price and ˜St is the execution price at timet.
Assuming that the trader trades at eacht∈[T], 2 we denote byq t andv t the inventory
and the trading velocity at timetrespectively. The trading velocityv t represents the
traded volume at timet. Clearly, it holds thatq 0 =q T = 0. The permanent market
impact is non-linear and it is
f(v t) =θsign(v t)|vt|δ, θ >0, δ∈(0,1) (3)
whenδ= 1, the permanent impact is linear as in the standard AC framework. The
coefficientκis the temporary impact coefficient, hence we assume a linear temporary
impact. We observe that a buy order pushes the price up, both the market and the
execution price, sincef(v t)>0 andκv t >0. Similarly, a sell order pushes both prices
down.
Now, as in other optimal execution problems, we have that:
TX
t=1
vt =q 0 = 0.
In such a problem, the final cash flow, will be:
XT =−
TX
t=1
vt ˜St
The expected cash flow is then (see Appendix A):
E[XT ] =−
h T−1X
t=1
f(v t)
TX
j=t+1
vj +κ
TX
t=1
v2 t
i
.(4)
As the main aim of the paper is to study the existence, feasibility and learnability of
dynamic arbitrages, we briefly recall its main definition used throughout the text.
Definition 2.1(Huberman and Stanzl (2004)).InT∈Ntrading steps there is a dynamic
arbitrage if there exists{v t}t∈[T] such that
• PT t=1 vt = 0and
•E[X T ]>0.
Therefore, finding an optimal solution to the trading problem defined above amounts
to finding a solution⃗ v∗ ∈R T such that the functionE[X T ] :=c(⃗ v∗) is maximized, where
byc(⃗ v∗) we denote a function of the optimal trading trajectory⃗ v∗. To this end, we first
need to make sure that there exists a solution to the problem we pose. The following
proposition guarantees that the problem is not ill-posed.
2We use the notation [T] :={1,· · ·, T}.
5

Proposition 2.1.The expected cash flow forδ <1, is a continuous function of the
strategy. Moreover searching for a strategy that maximizes the expected cash flow is a
well-posed problem since
lim
λ→±∞
c(λ⃗ v) =−∞.
Therefore, there exists a solution that maximizesE[X T ]withδ <1.
Proof.See Appendix A.
The above proposition does not guarantee that there is a round-trip strategy but that
the problem we want to solve is not ill-posed, since the best strategy might still be to not
trade.
3 Dynamic arbitrage strategies
In this section, we investigate the existence and characteristics of dynamic arbitrage strate-
gies of the previously introduced impact model. Due to the non-convexity of the problem,
the investigation is mainly numerical. However in the next subsection we show that,
by restricting to trading strategies with only two velocities, it is possible to find and
characterize price manipulation strategies.
3.1 Price-manipulation with only two trading velocities
Before considering more complex cases, we start by analysing the case where the trader
can only select two trading velocities. Leveraging on Gueant (2016), we denote byA ⊂
[−b, b]⊂Rthe set of all possible trading actions across time step and by|A|the cardinality
ofA. Notice that for a trading strategy{v t}t∈[T] there are at mostTdifferent trading
velocities thus|A| ≤T. We observe that for a round-trip strategy it must haveT≥2
(i.e. at least two time steps). In the rest of this subsection we consider that|A|= 2. In
this case it is
vt =
(
α,ift∈S⊂[T]
−β,ift∈[T]\S
whereSis any set of indexes in [T]. To be a round-trip strategy,αandβmust have the
same sign and it should be that:
TX
t=1
vt =|S|α−(T− |S|)β= 0⇔ |S|α= (T− |S|)β.(5)
In the following lemma, we compute the expected cash flow when one trading velocity
is used up to a certain time and then replaced by a different trading velocity for the
remainder of the trading horizon.
Lemma 3.1.Let|A|= 2andn∈[T−1]such thatv t =αfor every1≤t≤nand
vt =−βfor everyn < t≤T, then
E[XT ] = nα 2 [(n+ 1)f(α) +f(− n T−n α)(T−n−1)]−κ[nα 2 + n2α2 T−n ] (6)
Proof.See Appendix B.
6

Now that we have the expected cash flow for the case when there are only two trading
velocities we can compute which are the optimal ones that maximize the cash flow. The
following lemma proves this result.
Lemma 3.2.Assume the conditions of Lemma 3.1 hold andα >0, then the maximum
expected cash flow at the end of the trading period is
max
n∈[T−1]
E[XT ](α∗, n)withα ∗ =
 (δ+ 1)A(n)
2B(n)
 1
1−δ
(7)
and
A(n) = nθ 2 h (n+ 1)−(T−n−1)  n T−n δi , B(n) =κ h n+ n2 T−n i .
Proof.See Appendix A
Figure 1:The optimal long position,nα ∗, as
a function ofδfor the PnD strategy.
Notice that we do not have a closed-form
analytical solution for the optimal value ofn,
but only for the optimal value ofα, which it-
self depends onn. Therefore, when|A|= 2,
we first determine the optimal trading veloc-
ityα ∗ for each fixedn, and then choose the
value ofnthat maximizes the expected cash
flow. Finally, for a fixedn, there exists a
unique strategy that maximizes the expected
cash flow whenα >0. Throughout the re-
mainder of the paper, we refer to this strat-
egy as the pump-and-dump strategy (PnD).
It is important to stress that nonlinearity
is the main source of manipulation. Fig. (1)
shows that the long position in the optimal
PnD strategy decreases asdeltaincreases.
This relationship illustrates how stronger nonlinear price impact increases the size of
the position selected by the optimal manipulation strategy.
3.2 Numerical optimization via SLSQP
Assuming only two distinct trading velocities, as in subsection 3.1, clearly restricts the
space of possible strategies and the revenues generated from trading. A richer set of
trading volumes and strategies could emerge if|A|were allowed to include more than
just two velocities. However, in that case the problem is not convex any more and there
are no closed-form solutions. We therefore resort to numerical methods to obtain an
approximate solution to the problem. We solve the constrained optimization problem
using the Sequential Least Squares Programming (SLSQP) algorithm proposed by Kraft
(1988). Therefore, the resulting optimization problem reads as follows:
⃗ v∗ = argmax⃗ v∈RT E[XT ], s.t
TX
t=1
vt = 0,
7

(a)
Figure 2: T op-Left:The optimal trading strategy by SLSQP and the corresponding inventory
(red line).Bottom-Left:The expected cash-flow. The green (red) area indicates the region
for whichE[X t]>0 (E[X t]<0).Right:The histogram ofE[X T ] from the different starting
points.Note:The parameters used are the ones reported on Table 1.
The objective functionE[X T ] is defined in Eq.(4), and the parameter values used to
determine it are reported on Table 1. We initialize the optimization fromN= 500 different
starting points, sampling uniformly at random fromU[−b, b] T , in order to identify the
best solution. Clearly, in this first step, to use the numerical solution we assume complete
T able 1:Fixed Parameters used both for the RL environment and for the definition of the
objective for the SLSQP.
Description Symbol Value
Time Horizon T 21
Permanent Impact Exponent δ 0.1
Permanent Impact Coefficient θ 0.0001
Temporary Impact Coefficient κ 0.0003
Maximum Buy (Sell) b 15 (−15)
knowledge of the parameters governing the evolution of the trading environment.
Fig. (2) illustrates the best numerical solution obtained via SLSQP. The top-left panel
shows the optimal trading velocity together with the corresponding inventory trajectory,
depicted by the red line. The bottom-left panel reports the associated expected cash flow,
from which we observe the existence of a manipulative strategy sinceE[XT ]>0. The right
panel displays the histogram ofE[X T ] obtained from 500 different SLSQP initializations.
These results highlight the complexity of the optimization problem, which stems from the
8

non-linear form of the permanent market impact function. In Appendix C we shed light
on the landscape of the various trading strategies found by the SLSQP starting from the
Ndifferent initial points.
3.3 Effect of impact parameter estimation on profitability
The previous numerical results were based on the assumption that the parameters gov-
erning the market were fully known when optimizing with SLSQP. In practice, this corre-
sponds to an idealized setting that cannot realistically be solved under full information.
In Section 3.3.1, we study the sensitivity of SLSQP to parameter misspecification, while
in Section 3.3.2, we present a method of impact parameters estimation on a finite sample
of optimal execution strategies, based on Almgren et al. (2005).
3.3.1 Sensitivity of PnL to parameter misspecification
Usually, most of the times in real market scenarios, impact parameters values are not
available, as by definition they are latent quantities and therefore difficult to be estimated
directly. Therefore, numerical solutions obtained with estimated parameters might be
affected by estimation errors as magnitudes might be misspecified. To see this, Fig. (3)
illustrates the expected cash as a function of parameter misspecification across all three
parameters. For the computation of the cash flow, we find the optimal strategy by using ˆδ
and then we substitute this strategy to Eq.(4) where we use the parameterδ, similarly for
the other two cases when we do not have knowledge of parametersθandκ. Specifically,
panel (a) shows the impact of misspecification inδ, panel (b) inθ, and panel (c) inκ.
Two key observations emerge. First, clearly the highest expected cash is achieved in
the absence of misspecification, and performance deteriorates as the magnitude of the
misspecification increases. Second, performance improves when the true value ofδis
closer to 1 rather than to 0. A similar pattern is observed in the remaining panels, where
the highest cash is again attained under no or minimal misspecification.
(a)
 (b)
 (c)
Figure 3:Expected cash vs the true parameters;δ, θandκwhen the optimal strategy is found
using ˆδ, ˆθand ˆκ.
3.3.2 Estimation of impact parameters
Here we present a parameter estimation method based on Almgren et al. (2005). In
Almgren et al. (2005), the authors used real metaorders 3, thus here we estimate the
3Metaorders are large trading orders that are split into pieces and executed incrementally.
9

parameters bysimulatingmetaorders from a TW AP strategy in a time window [1, T]
leaving the dynamics of the market unchanged from previous numerical experiments.
Specifically, we assume that for the metaorderithe fundamental and the execution price,
respectively, are
S(i) t =S (i) t−1 +θsign(v (i))|v(i)|δ +σξ (i) t
˜S(i) t =S (i) t−1 +κv (i), t= 1,· · ·, Tandi= 1,· · ·, N.
We assume that at thei-th metaorder we want to executeq i shares4 at a constant speed
for any orderiand it isv (i) = qi T withq i ∼U[1,20].
For each metaorderithe fundamental price at timetcan be written as:
S(i) t =S 0 +tθ(v (i))δ +σ
tX
s=1
ξ(i) s
thus, at the end of metaorderi, at timeTthe fundamental price it is
S(i) T =S 0 +T θ(v(i))δ +σ
TX
s=1
ξ(i) s ⇔
S(i) T −S 0
S0| {z }
Ii
= T θ(v(i))δ
S0
+ noise
The execution price at timetcan be written as:
˜S(i) t =S 0 + (t−1)θ(v (i))δ +σ
t−1X
s=1
ξ(i) s +κv (i)
and the realised price (following the terminology in Almgren et al. (2005)) for the metaorder
i, due to the TW AP strategy, is
¯Si =
PT
t=1 v(i) ˜S(i) t PT
t=1 v(i)
=
PT
t=1
qi
T
˜S(i) t
PT
t=1
qi
T
=
1
T qi
PT
t=1
˜S(i) t
qi
¯Si = 1 T
TX
t=1
˜S(i) t
= 1 T
TX
t=1
h
S0 + (t−1)θ(v (i))δ +κv (i) +σ
t−1X
s=1
ξ(i) s
i
=S 0 +θ T−1 2 (v(i))δ +κv (i) + noise⇔
¯Si −S 0
S0| {z }
Ji
= T−1 2T Ii + κv(i) S0 + noise
4In Almgren et al. (2005) this variable is denoted byX.
10

Therefore, we end up with the following two regressions 5:
Ii = T θ(v(i))δ
S0
+ noise (8)
Ji − T−1 2T Ii = κv(i) S0 + noise (9)
To find an estimate forδwe minimize the residuals sum of squares (RSS):
ˆδ= argmin δ∈(0,1)
NX
i=1

Ii − ˆθ(δ) T S0  qi T δ2 (10)
where ˆθ(δ) = S0 T
PN
i=1( qi T )δIi PN
i=1( qi T )2δ (see Appendix D for a derivation of this formula). Then ˆθ= ˆθ(ˆδ). Similarly, for the estimation ofκit is
ˆκ=S0
PN
i=1( qi T )(Ji − T−1 2T Ii) PN
i=1( qi T )2 .
3.4 Numerical experiments
We now perform numerical experiments to show how the estimation method proposed
above works in finite sample. The parameter of the impact model are those in Table 1.
For the choice of the volatilityσ, we adopt a realistic estimate by using real data. First
we use an estimate of the daily realized volatility (R V) (see Andersen et al. (2003)) of
MSFT from April 2018 and we setσ daily = 0.026. Similarly to Almgren et al. (2005) we
assume that an average metaorder lasts 0.39 days, thus
σmetaorder :=σ=σ daily
√
0.39 = 0.0168.
Moreover for the impact parameters;θandκ, we choose them in a way such that the ratios
σ
θ and σ κ are 56 and 167 respectively. These ratios are the same with the ones reported
on Table B from Almgren et al. (2005) in which they report the summary statistics
from a sample of real metaorders. Finally, we consider the estimation on samples of size
N∈ {500,5000}.
The results are shown in Table 2. As expected, the estimation is more precise for
larger samples 6 and for smaller volatility. The interesting aspect is that the estimation
of the parameterδis very noisy and usually upward biased. As suggested by Fig. (1),
this overestimation leads to more conservative strategies (i.e. with smaller long position),
reducing the potential PnL of the dynamic arbitrage strategy when the DGP is known
but the impact parameters must be estimated from a finite sample of data.
5Notice that in Almgren et al. (2005) they use the approximation T−1 T ≈1, to simplify the second
regression equation but we observe, without this approximation, that the estimations for the temporary
impact are more robust, since forT= 21 the approximation is not sufficiently accurate.
6We conducted experiments for larger values ofN, which provide indications that the estimators are
asymptotically consistent.
11

Parameter (10−4) h ˆθSE of ˆθˆκSE of ˆκ i ˆδSE of ˆδ σ N
Estimate
0.61 3 2 17 0.99 1.88 0.0168
5001 0.48 4 3 0.79 0.94 0.0030
1 0.23 1 2 0.20 0.31 0.0020
1 0.63 9 5 0.26 0.61 0.0168
5,0001 0.12 3 0.09 0.48 0.22 0.0030
1 0.07 3 0.65 0.15 0.10 0.0020
True 1 3 0.1
T able 2:Estimate and Standard Error (SE) of the parameters whenT= 21. Note that the
values for the first 4 columns are in basis points.
4 Dynamic Arbitrage via deep RL
Having set the stage with numerical techniques, we now pass to studying the problem
with deep RL. By means of RL we aim at assessing whether a learner, who has no direct
knowledge of either the impacts structure or of the values for the impacts, would be able
tolearna dynamic arbitrage strategy, employing as little information on the market as
possible. In a spirit similar to that of Ning et al. (2021) and Macr ` ı and Lillo (2025),
we solve the round trip optimal trading problem in the context of the model reported in
Eq.(1) with DDPG.
4.1 Environment, states and reward
The deep RL experiment runs over a numberMof training episodes of trading where the
agent learns the optimal strategy. The agent, for each time stept, has access to a simple
state representation of the environment calledS t = (q t, t, St), that is the tuple made by
current inventory at time stept, time steptand permanently impacted price at time step
t, i.e.S t.
The price dynamics evolve as in Eq.(1) and the values of the parameters are the same
as the ones described on Table 1, therefore the agent has to make a trading decisionvt (i.e.
buy/sell action to adopt) based on the knowledge of the stateS t, such that the reward at
each time step is maximal. The reward, seen at each trading step is defined as:
rt =S tvt −κv 2 t (11)
Wherev t is the traded volume at timet,S t is the permanently impacted price as in Eq.
(1) andκis the temporary impact parameter. The reward and the actions are added to
the tupleS t when they are stored in the memory used by the algorithm to train its neural
networks (further details below).
4.2 The learning algorithm
The DDPG algorithm is composed by two main neural networks: acriticand anactor
network. It allows for continuous controls and combines deterministic policy gradients
with deep function approximation. Originally introduced by Lillicrap et al. (2016), DDPG
extends the deterministic policy gradient framework of Silver et al. (2014) by leveraging
neural networks to approximate both the policy (actor) and the action-value function
12

(critic). The actor network deterministically maps states to actions, while the critic
estimates the expected return. To stabilize training, DDPG employs target networks
and an experience replay buffer, borrowing key ideas from Deep Q-Network. The critic
is trained by minimizing the Bellman error using targets constructed from the reward
signal and the discounted estimate of future returns, while the actor is updated via the
deterministic policy gradient, maximizing the critic’s evaluation of the chosen actions.
4.2.1 The actor and critic networks
The critic and actor neural networks are feed-forward networks with four and three in-
put neurons, respectively, a number ofl NN layers ofd NN hidden nodes, each withSiLu
activation function, in the Actor network, the final layer hastanhactivation function.
We refer to the actor network asπ, since it is the network that parametrises the
policy directly, and to the critic network asQ, as the architecture of the critic part of the
algorithm relies fully on double deep Q-learning.
At the beginning of the training loop we initialise the networksπ, Qwith random
weightsµ π, µQ. As training unfolds, (µ π, µQ)→(µ ∗ π, µ∗ Q), where (µ ∗ π, µ∗ Q) are the optimal
weights that correspond to the optimal policy that maximises the the sum of discounted
rewards.
Therefore, during training theQnetwork, in order to avoid an overestimation of the
Q-values for the considered state-action pairs, we use aQ tgt network that is initialised at
the beginning of the training routine as a copy of theQnetwork with weightsµ Qtgt =µ Q,
thus employing double deep Q-learning for the Critic part of the algorithm, the weights
of theµ Qtgt are then periodically set equal toµ Q. In order to do so, we have adopted the
soft update technique as described in the original DDPG paper by Lillicrap et al. (2016),
with the soft update parameter set to 0.001.
During training, as the trading unfolds we chose to keep memory of the states seen
and the actions, volumes traded, at each time step into a memory of lengthm. As soon
as the memory has at least lengthB, which is the length of a batch, the algorithm starts
training the two networks via gradient descent. In any case, every time the networks are
trained, batches of past trading experiences are randomly sampled from the memory.
The critic.For each training iteration, we train a critic networkQ. To this end, we
add an additive exploration zero mean noise to the output of the actor networkπ(whose
training is described below), whose variance declines at each iteration7. The additive noise,
ε, helps the Actor neural network to explore the range of inventory holdings to be held
depending on the state. Thus, while training theQnetwork,v t+1 =π(S t|µπ) +N(0, ε),
whereπ(S t|µπ) is the output of the Actor network. Clearly, as the training unfolds andε
becomes smaller, the exploration noise diminishes and the policy chosen by the networkπ
becomes deterministic. In this way, given the weightsµ ∗ π, found at the end of the training,
the Critic network directly maps a state into an action such that:
v∗ t =π(S t|µ∗ π) (12)
7Specifically, before learning loop starts we seta= 1/Tandε min = 0.1 Then, for each train iteration
mwe setε= max(ε−a, ε min). In this way, the more we iterate in the learning routine the lower the
εvalue.εis then used as an additive noise in the Actor-Critic architecture used in both the learning
algorithms.
13

Once the volume is obtained, it is used to calculate the reward for each time-step using
the equation Eq.(11).
To train theQnetwork, we update the weightsµ Q such thatµ Q = argminµQ  L1(µQ;µ Qtgt),
by taking a single gradient step on the loss
 L1 = 1 b
bX
i=1
(Q(St, vt+1|µQ)−y t)2 (13)
yt =r t +γQ tgt(S ′ t, π(S′ t|µπ)|µQtgt) (14)
WhereS ′ t is the next state where the environment evolves after the agent has taken the
actionv t. The weights of the Critic networkµ Q are then updated using gradient descent.
The actor.For each training iteration we train the actor networkπ, which is the neural
network responsible for choosing the actionv t. To do this, we feed theπnetwork with a
batch ofBstatesS t. Theπnetwork returns a volume to be sold or boughtv t, which is in
turn fed to the CriticQnetwork, along with the stateS t. The output of theQnetwork is
theQvalue which is maximized during training. Specifically, the weightsµ π of the Actor
network are found by maximizing the output of the critic network with fixed weightsµ Q.
As before we perform a single gradient step to minimise the loss:
 L2 =− 1 b
bX
i=1
Q(St, π(S′ t|µπ)|µQ) (15)
whereπ(S t|µπ) is the output of the actor network with current weightsµ π. The weights
µπ are updated using the policy gradient theorem. The derivative of the loss function  L 2
with respect to the weights of the Actor network is:
∇µπ  L2 =− 1 b
bX
i=1
h
∇aQ(St, a(i)|µQ)|a(i)=π(S ′ t|µπ)∇µπ (St|µπ) i (16)
where the first part in the square brackets tells us how sensitive theQnetwork is to
changes in the action chosen by the Actorπ, this is the gradient of theQ-value with
respect to the action and evaluated at the action suggested by the Actor network, in this
context for ease of notation we usea(i) =v (i) t to denote the action for theistate among the
bconsidered in the batch. The second part inside the brackets is the gradient of the the
actor’s policy and accounts for how much the actionv t changes with respect to changes
in theπnetwork parameters. We update the weights for theπnetwork with gradient
descent. We repeat this training routine a numberlof times in order to assess how the
quality of the actions chosen by the Actor changes and, in this way, to thoroughly explore
weights combinations for theπnetwork.
The complete training algorithm for both the Critic and the Actor neural networks is
reported in Algorithm 1. Both the Actor and the Critic neural networks are feed-forward
fully connected neural networks, for the gradient descent we use the Weighted ADAM
with learning rate of 0.1. As training unfolds, we adopt a scheduler for the learning
rate, thus diminishing its value as the agent makes experience and the neural networks
are trained, once very 100 episodic iterations (i.e. time step over training episodes) the
learning rate is diminished following the rulelr←lr×0.99. The features for the DDPG
algorithm are normalised in the domain [−1,1]. Relevant parameters for the networks
and the market model are reported in Table 3.
14

Figure 4: T op:Heatmap of the executed actions chosen by DDPG during the training phase of
500 episodes.Bottom:The actions chosen from DDPG along with the corresponding inventory
during the final training episode.
15

T able 3:Symbol and value used for each parameter in the DDPG algorithm.
Description Symbol Value
Training Episodes M 500
Memory Length m 10e5
Batch Size B 128
Learning Rate actor/critic ηπ =η Q 0.1
Nodes actor/critic Nπ =N Q 64
Layers actor/critic Lπ =L Q 3
Discount Factor γ 0.99
Figure 5:The 25-episode moving averagesLeft:of the action aggressiveness andRight:of
signed action directionality during training.
Training results.We train the agent using the procedure described above and termi-
nate training after episode 500, since no noticeable improvement in the learned policy is
observed beyond this point. The top panel of Fig. (4) shows a heatmap of the actions se-
lected at each time step and in each episode during one run of training. At the beginning
of the training phase, the agent alternates between exploratory buy and sell actions. As
training progresses, however, the policy converges toward a directional buying strategy
over the first 20 time steps, followed by a sell execution at the final step to satisfy the
round-trip constraint. The bottom panel shows the final learned strategy.
To characterize how the strategies learned by DDPG evolve across episodes, we define
the action aggressiveness in episodeeas:
Ae = 1 20
20X
t=1
|ve,t|(17)
and the signed directionality in episodeeas:
De =
P20
t=1 ve,t P20
t=1 |ve,t|
,with−1< D e <1 (18)
wherev e,t is the action chosen (i.e. the volume traded) in episodeeat timet. The quantity
Ae measures how aggressive in absolute terms is the pump phase of the manipulative
strategy, whileD e tells us how consistently the strategy buys or sells in the pump phase.
16

The left panel of Fig. (5) displays the evolution ofA e during 4 training runs. We observe
that, as training progresses, DDPG converges toward less aggressive strategies. The right
panel of Fig. (5) showsD e across the same runs. During the first episodes, this quantity
is close to zero, indicating no clear directional preference in the first 20 time steps. As
training proceeds, however, the strategy converges toward a positive direction over the
first 20 time steps. Notice that this symmetry breaking is consistent with the form of the
reward function in Eq. (11). At each time stept, DDPG seeks an actionv t that maximizes
the instantaneous reward. Therefore, by differentiating the reward with respect tov t and
setting the derivative equal to zero, we obtain the action that maximizes the reward at
timet:
v∗ t = St 2κ >0.(19)
If on the other hand, one defines the reward as:
rt =−S tvt −κv 2 t
then we will observe a negative direction at the final episodes (see Fig. (11) in Appendix
E).
5 Discovering price manipulation strategies in finite
data samples
We now consider the problem of a trader who tries to find a price manipulation strategy
in a market where dynamic arbitrage is allowed by the nonlinearity of permanent impact.
Critically, we assume that the trader has a finite amount of data to identify the strategy,
and we compare two approaches.
In the first one, the agent hasNTW AP metaorders to estimate the parameters of the
AC nonlinear model with the regression method presented above. Then the agent uses
the estimated parameters in an SLSQP optimizer to find the optimal price manipulation
and it tests it on 1000 out of sample simulations of manipulative strategies. We consider
N= 500 andN= 5000 and we term these strategies regSLSQP 500 and regSLSQP 5000,
respectively. In the second approach, the agent is agnostic about the underlying impact
model and uses the RL approach described above to learn the manipulation strategy on
N= 500 episodes. As before, the agent tests it on 1000 out of sample simulations of
manipulative strategies. We term this strategy DDPG.
As benchmarks we use the PnL obtained (i) with the optimal strategy with only two
trading velocities and (ii) with the optimal strategy obtained with SLSQP. Clearly, in
both cases we use the correct DGP and the true parameters. The two strategies are
termed PnD and SLSQP, respectively. As above, we consider three levels of volatility.
Table 4 summarizes, for each method, the average terminal cashXT , the corresponding
standard error, and the results of the t-test together with the associated p-values over
1000 out of sample implementations of the learned strategies. For the regSLSQP methods,
we follow a different approach. Since there is a large variability in the estimated impact
parameters from a finite number of TW AP executions, the PnL in the out of sample set
depends strongly on the specific realization of 500 or 5000 TW APs used in the estimation.
To mitigate this effect, we replicate the whole procedure 100 times and we report the mean
and the average standard deviation in these 100 experiments. Moreover, the t-test column
17

reports the percentage of the replications (among the 100) that reject the null-hypothesis
of zero expected cash.
The results show that when volatility is high (σ= 0.0168), none of the methods among
PnD, SLSQP and DDPG produces a statistically significant positive terminal cash. This
is due to the finiteness of the test set and the large volatility. The regSLSQPs produce
a statistically significant negative expected terminal cash in 46% and 33% of the cases
when 500 and 5000 metaorders are used, respectively, for the estimation of the impact
parameters. Thus in these conditions, even if manipulation is possible, large volatility
prevents its exploitation.
For intermediate volatility values (σ= 0.003) PnD, regSLSQP5000, and DDPG
achieve statistically significant positive cash flows. PnD is the best-performing method
followed by DDPG and then by regSLSQP5000. Moreover, SLSQP even though it has
complete knowledge of both the functional form of the market-impact model and of the
parameters does not produce statistically significant positive cash. On the contrary, the
model based approach regSLSQP500 estimated on a smaller sample provides negative
expected cash flow. Importantly, notice that the same sample size is sufficient for the RL
based approach DDPG to learn a systematically profitable strategy.
Finally, when volatility is low (σ= 0.002), all methods except regSLSQP 500 generate
statistically significant positive terminal cash. However, among the two sample based
methods, regSLSQP500 outperforms DDPG. This is somewhat expected because with low
volatility and relatively large estimation set (N= 5000), the parameters of the impact
model are accurately estimated, while the DDPG is still trained onN= 500 episodes.
Method Mean (10−4) Std t-test p-value σ
PnD 32 0.1442 0.70 0.480
0.0168
SLSQP 48 0.2805 0.54 0.580
regSLSQP500 −5942 1.5924 46% <0.05
regSLSQP5000 −4082 1.24 33% <0.05
DDPG 11 0.0434 0.83 0.400
PnD 14 0.0257 1.75 0.070
0.0030
SLSQP 25 0.0501 1.58 0.110
regSLSQP500 −2562 0.1978 34% <0.05
regSLSQP5000 1 0.0561 5% <0.05
DDPG 5 0.0077 2.34 0.010
PnD 13 0.0171 2.39 0.010
0.0020
SLSQP 23 0.0334 2.22 0.020
regSLSQP500 −1071 0.0852 54% <0.05
regSLSQP5000 13 0.0349 36% <0.05
DDPG 5 0.0051 3.26 0.001
T able 4:Comparison among the methods after 1000 simulations of the price evolution as in
Eq.(1)-(2).
As expected, volatility is the key parameter for the effective profitability of dynamic
arbitrage strategies. When the model and the parameters are known (SLSQP and PnD),
large volatility prevents the exploitation of the arbitrage, at least in a finite testing sam-
ple. When the model and/or the parameters are unknown, the volatility also enters in
18

the estimation (regSLSQP) and learning (DDPG). The surprising result is that for in-
termediate volatility and small sample a model agnostic method is more effective of one
knowing the model but not the parameter in identifying profitable strategies. Even more
surprising is that in this volatility regime a ten-fold larger training set of the regSLSQP is
not sufficient to beat the performance of DDPG. Finally, even for small volatility, DDPG
outperforms regSLSQP when the training tests are equally small.
In conclusion, the DDPG algorithm generates positive cash flows while relying on only
minimal information: the current time step, the remaining inventory, and the permanently
impacted asset price. Despite this simple state representation, the agent achieves perfor-
mance comparable to numerical optimization methods, with relatively low variability in
terminal cashX T . This suggests that reinforcement learning algorithms can discover
round-trip trading strategies that create dynamic arbitrage opportunities.
6 Conclusion
This paper studied whether a model-free reinforcement learning algorithm can learn to
exploit price-manipulation opportunities more effectively than a traditional model-based
approach when both methods are trained on finite samples of market data. We considered
a single-asset optimal execution problem with concave permanent market impact, a setting
in which dynamic arbitrage may arise through round-trip trading strategies.
We first established, both analytically and numerically, the existence of profitable
manipulative strategies in discrete time. While these strategies can be derived under full
knowledge of the market-impact model, implementing them in practice requires estimating
latent impact parameters from data, introducing an additional source of uncertainty. This
observation motivates the central comparison of the paper: a model-based optimization
procedure with correctly specified dynamics but estimated parameters versus a model-free
reinforcement learning agent that learns trading policies directly from interaction with the
environment.
Our numerical experiments show that the DDPG agent is capable of learning profitable
round-trip strategies without explicit knowledge of the underlying market-impact model.
More importantly, when both approaches are constrained by the same amount of training
data, reinforcement learning frequently outperforms the model-based procedure because
it avoids the intermediate and error-prone parameter-estimation step. The advantage is
most pronounced in regimes where parameter uncertainty materially affects optimization,
whereas the model-based approach naturally regains superiority when estimation becomes
sufficiently accurate.
The broader implication of these findings is methodological as much as financial. The
paper does not argue that reinforcement learning creates manipulation where none exists;
rather, it shows that, whenever the market environment admits exploitable dynamic arbi-
trage, a model-free learning algorithm can identify such opportunities directly from data
and may do so more efficiently than a correctly specified parametric model estimated on
finite samples. This highlights an important distinction between the theoretical existence
of manipulation and its practical discoverability.
From a market-design perspective, the results also carry regulatory implications. Re-
inforcement learning agents optimize the objective they are given, without distinguishing
between economically desirable profits and profits generated through behaviour that may
undermine market integrity. Consequently, environments that inadvertently admit ma-
19

nipulative incentives may be particularly vulnerable to increasingly sophisticated learning
algorithms. As reinforcement learning becomes more widely adopted in automated trad-
ing systems, ensuring that reward functions, market design, and regulatory constraints
are aligned with no-manipulation principles will become increasingly important.
Several directions for future research naturally follow from this work. Extending the
analysis to more realistic market-impact models, including transient or stochastic impact,
would help assess the robustness of the results beyond the Almgren-Chriss framework.
Likewise, studying richer market environments with limit-order-book dynamics, multiple
strategic agents, or cross-asset interactions would provide a more comprehensive under-
standing of how learning algorithms exploit market structure. Finally, integrating explicit
no-manipulation constraints or safe reinforcement learning techniques into optimal execu-
tion algorithms represents a promising avenue for developing trading systems that remain
both profitable and market compliant.
20

Algorithm 1Training of DDPG agent for optimal trading
Require:
Initialise with random weightsQand make a copyQ tgt;
Initialise with random weightsπ
Initialise the memory with max lengthm. Setε= 1,Bbatch size,Mtrain episodes;
Set market dynamics parameters;
fori in Mdo
SetS i 0 =S 0;
fort in Tdo
St ←(q t, t, Si t);
vt =π(S t|µπ);
rt ←S i t−1vt −κv 2 t ;
Si t−1 →S i t;▷GenerateS i t fromS i t−1
S ′ t ←(q t+1, t+ 1, St+1) ;
Memory←(S t, rt, vt,S ′ t);▷Memory storing
ifLength of memory≥Bthen
forj inBdo
Sample a batch of (S j t , rj t , vj t ,S ′,j t ) from memory;
trainπ;
trainQ
end for
ifLength of memory =Lthenhalve the length of memory
end if
end if
Aftermiterations decayϵ=ϵ−a;
Aftermiterationsθ tgt ←θ main;
end for
end for
21

References
R. Almgren and N. Chriss. Optimal execution of portfolio transactions. Journal of Risk,
3:5–39, 2000.
Robert Almgren, Chee Thum, Emmanuel Hauptmann, and Hong Li. Direct estimation
of equity market impact. Risk, 18:58–62, 2005.
T.G. Andersen, T. Bollerslev, F.X. Diebold, and P. Labys. Modelling and forecasting
realized volatility. Econometrica, 71:579–625, 2003.
Alessio Azzutti, Wolf-Georg Ringe, and H. Siegfried Stiehl. Machine learning, market ma-
nipulation, and collusion on capital markets: Why the “black box” matters. University
of Pennsylvania Journal of International Law, 43:79–136, 2021.
Alvaro Cartea, Patrick Chang, and Gabriel Garcıa-Arenas. Spoofing and
manipulating order books with learning algorithms. Available at SSRN:
https://ssrn.com/abstract=4639959, 2023.
Gianbiagio Curato, Jim Gatheral, and Fabrizio Lillo. Optimal execution with non-linear
transient market impact. Quantitative Finance, 17:41–54, 2017.
J. Gatheral. No-dynamic-arbitrage and market impact. Quantitative Finance, 10:749–759,
2010.
Olivier Gueant. The Financial Mathematics of Market Liquidity. Chapman & Hall/CRC
Financial Mathematics Series, 2016.
Dieter Hendricks and Diane Wilcox. A reinforcement learning extension to the almgren-
chriss framework for optimal trade execution. In 2014 IEEE Conference on Compu-
tational Intelligence for Financial Engineering & Economics (CIFEr), pages 457–464.
IEEE, 2014.
G. Huberman and W. Stanzl. Price manipulation and quasi-arbitrage. Econometrica, 72:
1247–1275, 2004.
Zhengyao Jiang, Dixing Xu, and Jinjun Liang. A deep reinforcement learning framework
for the financial portfolio management problem. arXiv preprint arXiv:1706.10059, 2017.
Dieter Kraft. A software package for sequential quadratic programming. Technical Report
DFVLR-FB 88-28, Institut f¨ ur Dynamik der Flugsysteme, Deutsche Forschungs- und
Versuchsanstalt f¨ ur Luft- und Raumfahrt, 1988.
Eun Jung Lee, Kyoung-Soo Eom, and Kyung Suh Park. Microstructure-based manipu-
lation: Strategic behavior and performance of spoofing traders. Journal of Financial
Markets, 16:227–252, 2013.
T. P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom Erez, Yuval
Tassa, David Silver, and Daan Wierstra. Continuous control with deep reinforcement
learning. In Proceedings of the 4th International Conference on Learning Representa-
tions, Proceedings of Machine Learning Research. PMLR, 2016.
22

Fabrizio Lillo, J.D. Farmer, and Rosario N. Mantegna. Master curve for price-impact
function. Nature, 421:129–130, 2003.
Fabrizio Lillo, J. Doyne Farmer, and Rosario N. Mantegna. Price impact function of a
single transaction. In The Complex Dynamics of Economic Interaction, pages 153–160,
Berlin, Heidelberg, 2004. Springer Berlin Heidelberg.
Andrea Macr ` ı and Fabrizio Lillo. Reinforcement learning for optimal execution when
liquidity is time-varying. Applied Mathematical Finance, 31:312–342, 2025.
Andrea Macr ` ı, Sebastian Jaimungal, and Fabrizio Lillo. Deep reinforcement learning for
optimal trading with partial information. arXiv:2511.00190, 2025.
Enrique Mart ´ ınez-Miranda, Frank McGroarty, and Edward Tsang. Learning unfair trad-
ing: A market manipulation analysis from the reinforcement learning perspective. In
IEEE Conference on Evolving and Adaptive Intelligent Systems, pages 103–108, 2016.
Alessandro Micheli and M´ elodie Monod. Deep reinforcement learning for online optimal
execution strategies. arXiv preprint arXiv:2410.13493, 2024.
Takanobu Mizuta. Can an ai perform market manipulation at its own discretion? – a
genetic algorithm learns in an artificial market simulation. In IEEE Symposium Series
on Computational Intelligence, pages 407–414, 2020.
John Moody and Matthew Saffell. Learning to trade via direct reinforcement. IEEE
Transactions on Neural Networks, 12:875–889, 2001.
Yuriy Nevmyvaka, Yi Feng, and Michael Kearns. Reinforcement learning for optimized
trade execution. In Proceedings of the 23rd International Conference on Machine Learn-
ing (ICML), pages 673–680, 2006.
Brian Ning, Franco Ho Ting Lin, and Sebastian Jaimungal. Double deep q-learning for
optimal execution. Applied Mathematical Finance, 28:361–380, 2021.
M. Potters and J.P. Bouchaud. More statistical properties of order books and price impact.
Physica A: Statistical Mechanics and its Applications, 324:133–140, 2003.
David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and Martin
Riedmiller. Deterministic policy gradient algorithms. In Eric P. Xing and Tony Jebara,
editors, Proceedings of the 31st International Conference on Machine Learning, vol-
ume 32 of Proceedings of Machine Learning Research, pages 387–395, Bejing, China,
22-24 Jun 2014. PMLR.
Pang-Ning Tan, Michael Steinbach, and Vipin Kumar. Introduction to Data Mining.
Pearson Education Limited, 2013.
Michael P. Wellman and Uday Rajan. Ethical issues for autonomous trading agents.
Minds and Machines, 27:609–624, 2017.
Vitalii Zhelezniak, Aleksandar Savkov, April Shen, and Nils Hammerla. Correlation co-
efficients and semantic textual similarity. In Proceedings of the 2019 Conference of the
North American Chapter of the Association for Computational Linguistics: Human
Language Technologies, Volume 1 (Long and Short Papers), pages 951–962. Associa-
tion for Computational Linguistics, 2019.
23

Wei-Xing Zhou. Universal price impact functions of individual trades in an order-driven
market. Quantitative Finance, 12(8):1253–1263, 2012.
A Derivations for section 2
In this appendix we first derive the expected cash flow and then we give the proof of
Proposition (2.1).
We derive Eq.(4) by substituting the execution price into the expression for the ter-
minal cash flow and expanding the result:
XT =−
TX
t=1
vt ˜St
=−
TX
t=1
vt(St−1 +κv t)
=−
h TX
t=1
vtSt−1 +
TX
t=1
κv2 t
i
The recursive Eq.(1) is written as
St−1 =S 0 +
t−1X
j=1
f(v j) +σ
t−1X
j=1
ξj
hence the terminal cash-flow can be written as:
XT =−
TX
t=1
vt
h t−1X
j=1
f(v j) +σ
t−1X
j=1
ξj
i
−κ
TX
t=1
v2 t .
We observe that
TX
t=1
vt
t−1X
j=1
f(v j) =
T−1X
j=1
f(v j)
TX
t=j+1
vt, v 0 = 0
thus it is
E[XT ] =−
h T−1X
t=1
f(v t)
TX
j=t+1
vj +κ
TX
t=1
v2 t
i
.(20)
The following proof establishes Proposition (2.1).
Proof.Let the vectorλv∈R T then the cost function is written as:
c(λv) =−
h T−1X
t=1
f(λv t)
TX
j=t+1
λvj
| {z }
F(λv)
+κ
TX
t=1
λ2v2 t
| {z }
S(λv)
i
(21)
24

the first term inside the parenthesis is written as
F(λv) =


f(λv 1)
f(λv 2)
...
f(λv T−1 )


⊺ 

PT
t=2 λvt 0 0 0· · ·0
0 PT t=3 λvt 0 0· · ·0 ... ... ... ...· · · ...
0 0 0 0· · ·λv T




1
1
...
1

 (22)
=|λ| δ+1F(v) (23)
while for the second term it is clearly true that
S(λv) =λ 2S(v).
hence
c(λv) =−[|λ| δ+1F(v) +λ 2S(v)]
sinceδ <1 the second term will dominate the convergence, thus the result in Eq.(21)
follows. For the continuity we simply observe thatc(v) is a sum of continuous functions.
B Derivations for section 3.1
We first prove lemma 3.1
Proof.
T−1X
t=1
f(v t)
TX
j=t+1
vj =f(α)(−β)(T−n)n+f(α)α
n−1X
k=1
(n−k) +f(−β)(−β)
T−n−1X
k=1
(T−n−k)
=f(α)(−β)(T−n)n+f(α)α[n(n−1)− n(n−1) 2 ]
+f(−β)(−β)[(T−n)(T−n−1)− (T−n)(T−n−1) 2 ]
=nf(α)(T−n)(−β) +f(α)α n(n−1) 2 +f(−β)(−β) (T−n)(T−n−1) 2
=− nα 2 [(n+ 1)f(α) +f(−β)(T−n−1)]
For the temporary impact term
κ
TX
t=1
v2 t =κ[nα 2 + (T−n)β 2]
thus
E[XT ] =−

− nα 2 [(n+ 1)f(α) +f(−β)(T−n−1)] +κ[nα 2 + (T−n)β 2]  .
We then prove lemma 3.2
25

Proof.From Lemma 3.1, for anyn∈[T−1] the expected cash flow is written as
E[XT ] = nα 2 h (n+ 1)θα δ −(T−n−1)  nα T−n δi −κ h nα2 + n2α2 T−n i
=α δ+1 nθ 2 h (n+ 1)−(T−n−1)  n T−n δi | {z }
A(n)
−α2 κ h n+ n2
T−n
i
| {z }
B(n)
(24)
We observe thatE[X T ]>0 if and only if
A(n)>0⇔n+ 1>(T−n−1)
 n
T−n
δ
and in that caseE[X T ] is a concave function ofα, thus to find the optimalαwe compute
the derivative with respect toαin Eq.(24):
∂E[XT ]
∂α = (δ+ 1)α δA(n)−2αB(n)⇔
α∗ =
 (δ+ 1)A(n)
2B(n)
 1
1−δ
.
Hence the cash flow of the optimal strategy is then
max
n∈[T−1]
E[XT ](α∗, n).(25)
C Properties of the local maxima of the optimization
problem
We analyze the trading strategies obtained by SLSQP fromNdifferent initializations,
focusing on how similar the resulting strategies are in terms of their final cash flow. To
compare two strategies⃗ vi, ⃗ vj ∈R T , we use the cosine similarity 8 (Tan et al., 2013)
c(i, j) = ⟨⃗ vi, ⃗ vj⟩ ∥⃗ vi∥∥⃗ vj∥,
which measures the angle between the two vectors and lies in [−1,1]. Since a strategy
and its sign-reversed counterpart produce the same final cash position, we use the sign-
invariant distance
d(i, j) = 1− |c(i, j)|.
This distance treats aligned and anti-aligned strategies as equivalent. We then exam-
ine the pairwise distance matrices for all SLSQP terminal strategies. As expected (see
Fig. (6)), nearby strategies in the ordering tend to have smaller distances. However, the
plots alone do not reveal whether similar strategies necessarily yield similar expected cash.
Therefore, for all pairs satisfyingd(i, j)≤ηwithη= 0.1, we compute|E i[XT ]−E j[XT ]|
(see Fig. (7)). The resulting scatter plot shows that strategies can be close under the
sign-invariant distance while still producing different expected cash, indicating structural
differences despite high similarity. Finally in Fig. (8) are illustrated two strategies with
small sign-invariant distance but relatively large cash discrepancy.
8The cosine similarity between two round-trip strategies corresponds to their Pearson correlation (see
also Zhelezniak et al. (2019)).
26

Figure 6:The heatmap of the sign-invariant distance on the left for all the strategies and on
the right with precision of two colors for all the strategies in Fig. (2).
Figure 7:Each point represents a pair of strategies whose sign-invariant distance is less than
or equal to the thresholdη.
(a)
 (b)
Figure 8:The two strategies with the largest discrepancy in expected cash for whichd(i, j) =
0.0855.
D Estimating the Parameters in SLSQP
In this Appendix we justify the derivation for the estimation of the permanent impact
parameterθas a function of the exponent impact parameterδ. Since
ˆδ= argmin δ∈(0,1)
NX
i=1

Ii − ˆθ(δ) T S0  qi T δ2
| {z }
RSS(ˆθ)
(26)
27

for the simplification in the notation we use: ˆθ(δ) := ˆθ. The RSS is a concave function in
ˆθthus there exist unique minimizer, it is then enough to consider the first derivative:
∂RSS
∂ ˆθ = 0⇔
−2 T S0
NX
i=1
 qi
T
δ
Ii − ˆθ T S0  qi T δ = 0⇔
ˆθ(δ) = S0
T
PN
i=1( qi T )δIi PN
i=1( qi T )2δ .
Fig. (9) depicts the estimated impact parameters as a function of the number of metaorders
Nfor all three values ofσ. We observe that the estimators are consistent since the stan-
dard errors get decrease asNincreases and approach the true value of the parameters.
Fig. (10) illustrates the strategy obtained with the regSLSQPN forN= 500 andN= 5000
metaorders when the volatility is 0.0168 in panels (a) and (d), when the volatility is 0.003
in panels (b) and (e) and when the volatility is 0.002 in panels (c) and (f). Clearly the
expected cash-flow is positive since we use the complete information of the price dynamics
for its computation.
E The training phase of DDPG
Here we plot the actions’ aggressiveness (see Eq.(17)) on the left plot of Fig. (11) and
the actions’ directionality (see Eq.(18)) on the right plot of Fig. (11) during the training
phase of DDPG when the reward is
rt =−S tvt −κv 2 t (27)
We observe that, although the level of aggressiveness remains approximately the same
throughout the training episodes with that of Fig. (5), the directionality of the actions
is reversed due to the negative sign in the reward function, relative to the directionality
obtained when the reward is defined as in Eq.(11).
28

(a)
(b)
(c)
Figure 9:Estimation of the impact parameters along with their standard errors as a function of
the number of metaordersN(a) whenσ= 0.0168, (b) whenσ= 0.003 and (c) whenσ= 0.002.
29

(a)
 (b)
 (c)
(d)
 (e)
 (f)
Figure 10:Plots(a-c)whenN= 500 and(d-f )whenN= 5000 metaorders. In each panel,
T op-Left:The optimal trading strategy by regSLSQPN and the corresponding inventory (red
line).Bottom-Left:The expected cash-flow. The green (red) area indicates the region for
whichE[X t]>0 (E[X t]<0).Right:The histogram ofE[X T ] from the different starting
points.
Figure 11:The 25-episode moving averagesLeft:of the action aggressiveness andRight:of
signed action directionality during training and the reward is defined as in Eq. (27).
30
