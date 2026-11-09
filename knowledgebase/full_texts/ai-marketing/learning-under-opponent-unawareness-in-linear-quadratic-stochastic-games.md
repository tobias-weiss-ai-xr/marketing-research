---
title: Learning under Opponent Unawareness in Linear-Quadratic Stochastic Games
url: https://arxiv.org/abs/2608.08268
category: ai-marketing
subcategory: measurement
date: 2026-08
venue: ''
authors:
- Dantong Chu
- Xuefeng Gao
- Yufei Zhang
source: arxiv
pdf_url: https://arxiv.org/pdf/2608.08268
pages: 49
chars: 144901
fetched_at: '2026-11-08T13:27:05+00:00'
kb_version: 1
---

# Learning under Opponent Unawareness in Linear-Quadratic Stochastic Games

Learning under Opponent Unawareness in Linear-Quadratic
Stochastic Games
Dantong Chu∗ Xuefeng Gao† Yufei Zhang‡
11th August, 2026
Abstract
As firms increasingly deploy machine learning for strategic decision-making, understanding
algorithmic interactions has become central to operations research and economics. This paper
studies learning in infinite-horizon, nonzero-sum linear-quadratic stochastic games under aradi-
cally uncoupledinformation structure, where players are either unaware of opponents or strategi-
cally oblivious, observing only a common state and their own action history. Under this minimal
information, we analyze an asynchronous decentralized learning process in which each player
independently runs a single-agentϵ-greedy iterated least-squares algorithm. We prove that, de-
spite being unable to identify the system parameters, players’ learning dynamics converge almost
surely to the complete-information Nash equilibrium and characterize the convergence rate. We
then apply the framework to a dynamic Cournot competition with sticky prices. Numerical
experiments validate the theoretical results and show that learning under limited information
reduces firm profits under both low and high price stickiness, while total surplus declines and
market concentration increases when price stickiness is high. Publicly revealing aggregate market
output substantially accelerates convergence and mitigates these welfare losses.
Keywords:Radically Uncoupled, Multi-agent Learning, Linear Quadratic Stochastic Game,
Dynamic Cournot Competition, Price Stickiness
1 Introduction
Driven by advances in machine learning and artificial intelligence, autonomous pricing and auto-
mated trading algorithms have become ubiquitous across e-commerce and financial markets. In
practice, these algorithms plausibly operate under a radically uncoupled information structure,
termed as in Foster and Young (2006). Under this paradigm, agents/algorithms either do not rec-
ognize the presence of their peers, lacking access to their actions, or remain strategically oblivious
by treating competitors’ dynamic behavior as exogenous environmental noise. Such obliviousness
arises both by necessity, when limited information (e.g., in over-the-counter markets) or substantial
market noise obscures competitors’ signals, and by design, as it enables the use of computationally
simpler single-agent learning algorithms. While this framework mirrors the informational reali-
ties of modern tech and financial markets, it could pose severe economic risks. Recent literature
on algorithmic collusion demonstrates that such uncoupled agents, despite independently employ-
ing reinforcement learning algorithms, may inadvertently converge to seemingly collusive outcomes
rather than to a competitive Nash equilibrium (see e.g. Abada and Lambin (2023)).
∗Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Hong
Kong, China. Email:dtchu@link.cuhk.edu.hk
†Department of Systems Engineering and Engineering Management, The Chinese University of Hong Kong, Hong
Kong, China. Email:xfgao@se.cuhk.edu.hk
‡Department of Mathematics, Imperial College London, UK. Email: yufei.zhang@imperial.ac.uk
1
arXiv:2608.08268v1  [math.OC]  8 Aug 2026

This gap reflects a fundamental limitation in our theoretical understanding. While radically
uncoupled learning is known to converge in simple stateless repeated games (Ba et al., 2025;
Bervoets et al., 2020; Xiong et al., 2024), convergence guarantees remain largely absent for stochas-
tic (Markov) games, where the state evolves according to the current state and the joint actions
of all players (Ozdaglar et al., 2022; Shapley, 1953). These state dynamics substantially compli-
cate learning under radically uncoupled information, as players will misjudge their impact on the
state in the absence of observations of their opponents (Zhang et al., 2021). Existing convergence
guarantees are therefore largely limited to specialized settings, such as (two-player) zero-sum games
(Chen et al., 2024; Sayin et al., 2021) and potential games (Maheshwari et al., 2025), and assume
finite state and action spaces to make the analysis tractable. Little is known about convergence for
generalN-player stochastic games with continuous state and action spaces.
In this paper, we study radically uncoupled learning in infinite-horizon, nonzero-sum linear-
quadratic (LQ) stochastic games. LQ games are a fundamental class of models for dynamic strate-
gic interactions in continuous state and action spaces and have been widely used in management
science, economics, and financial engineering; see Section 1.1 for an application to dynamic Cournot
competition and Dockner et al. 2000; Fershtman and Kamien 1987; Heston and Hu 2024; Muhle-
Karbe and Oomen 2026 for related examples. By combining linear state dynamics with quadratic
costs, LQ games admit closed-form equilibrium solutions and provide rigorous benchmarks for eval-
uating learning algorithms in dynamic games. Our central question is to understand the behavior of
radically uncoupled learning agents: When agents learn from their own experiences while remaining
unaware of or strategically oblivious to their competitors, can decentralized learning dynamics lead
to a Nash equilibrium?
1.1 A Motivating Application: Dynamic Cournot Competition
To motivate our learning framework, we consider a dynamic Cournot competition model with sticky
prices as an illustrative application. This classical model captures multi-period quantity competition
under market frictions and has been extensively studied (Fershtman and Kamien, 1987; Heston and
Hu, 2024). Consider a discrete-time, infinite-horizon market comprisingMfirms. In each period
t∈N, each firmmchooses its output quantityq m t . The market pricep t evolves according to the
following discrete-time process:
pt+1 =sp t + (1−s)

a−b
MX
m=1
qm t
!
+ω t,(1)
wheres∈(0,1) is the price stickiness coefficient,a >0 is the demand intercept,b >0 is the slope of
the inverse demand function, and the noise term{ω t}∞ t=0 is an i.i.d. random shock (e.g., consumer
mood swings, market noise) with zero mean and varianceσ 2 ω. In this model, price adjusts gradually
toward the level implied by the current demand function rather than instantaneously, with the speed
of adjustment governed by a stickiness parameters∈(0,1) (e.g., due to market inertia). The goal
of each firm is to select a sequence of output quantities{q m t }∞ t=0 to maximize its total discounted
expected profit:
E
" ∞X
t=0
ρt

pt+1 −c m − 1 2 qm t

qm t
#
,(2)
whereρ∈(0,1) is the discount factor, and the term (c m + 1 2 qm t )qm t represents the production
cost, consisting of a linear termc mqm t with private constant marginal cost parameterc m >0 and
a quadratic term 1 2 (qm t )2 reflecting increasing marginal production costs (Fershtman and Kamien,
1987). The feature of the sticky price places the model within the class of stochastic games rather
than repeated games, as the price acts as a state variable.
In new or emerging markets, firms may have limited information about their competitors or even
be unaware of their existence. In particular, at timet+ 1, each firmmobserves only the historical
2

price sequence{p k}t+1 k=0 and its own quantity decisions{q m k }t k=0. Moreover, the key structural
parameters of (1), includings,a,b, andσ ω, are also unknown to all firms. Under this information
constraint, each firm behaves as if it were the sole major participant in the market and treats the
effects of other firms’ actions as unobserved noise. Consequently, firmmforms a misspecified belief
about price dynamics:
pt+1 =s ′pt + (1−s ′)  a′ −b ′qm t  +ω ′ t,(3)
wheres ′ denotes the firm’s perceived price stickiness coefficient,a ′ andb ′ are the perceived intercept
and slope of the inverse demand function, andω ′ t represents the perceived market noise with mean
zero and varianceσ 2 m. The firm’s objective remains to choose an output sequence{q m t }∞ t=0 to
maximize its total discounted expected profit (2), but subject toits perceived and misspecified price
dynamics(3).
Since the parameters of the perceived dynamics (3) are unknown, firmmadopts an online
learning framework that balances exploration and exploitation. Specifically, each firm independently
employs anϵ-greedy learning algorithm based on least-squares estimation of the perceived model
parameters (e.g.,s ′, a′, b′,σ 2 m) over a sequence of expanding epochs. Within each epoch, firmm
uses a linear feedback strategy of the formq m t =−F mpt +f m +α mvm t , whereF m andf m are
derived from the estimated model parameters, andv m t is an independent exploration noise scaled
by the exploration coefficientα m. Linear inverse demand, quadratic costs, and linear strategies are
standard assumptions in the Cournot competition literature; see, e.g., Bonatti et al. 2017; Gal-Or
1985; Hauk and Hurkens 2001; Vives 1984.
The learning process described above provides a natural model for how firms adapt in emerging
markets with limited information. In contrast, dynamic Cournot games with complete informa-
tion are typically analyzed through feedback (closed-loop) Nash equilibria, which characterize firm
behavior in mature markets (Fershtman and Kamien, 1987; Heston and Hu, 2024). This contrast
raises two fundamental questions about market evolution. First, can the feedback Nash equilibrium
of a mature market emerge from radically uncoupled learning? That is, when firms learn solely from
their own experiences under model misspecification and without knowledge of competitors, do their
behaviors converge to the complete-information equilibrium? Second, how does the learning process
shape market outcomes, such as economic welfare and market concentration, during this transition?
This paper addresses these questions by establishing convergence guarantees and characterizing the
resulting market dynamics under different degrees of price stickiness.
1.2 Our Contributions
Motivated by the dynamic Cournot competition model with sticky prices in Section 1.1, we study
online learning under radically uncoupled information in a broad class of infinite-horizon,N-player
nonzero-sum LQ stochastic games. Each player observes only the common state and chooses her
own actions, while the system dynamics and all information regarding other players remain un-
known. Consequently, each player treats the environment as a single-agent problem and applies
a canonicalϵ-greedy online learning algorithm following (Mania et al., 2019; Simchowitz and Fos-
ter, 2020). We formalize this behavior through a radically uncoupled multi-agentϵ-greedy iterated
least-squares (ILS) algorithm with growing epochs. At each epoch, players estimate a perceived
(and generally misspecified) model, compute linear policies from the estimated dynamics, and in-
ject decaying exploration noise. The algorithm requires no information about other players and
allows for heterogeneous update schedules and exploration rates.
Our contributions are twofold:
•We establish the first convergence guarantee for radically uncoupled learning in LQ stochastic
games with a common state affected by all players’ actions.
The main challenge is that, without information about their opponents, players cannot disen-
tangle their own impact on the state dynamics from that of other players, and will misattribute
3

the effects of other players’ actions to system noise. This prevents them from identifying the
true system dynamics, unlike in the single-agent setting (Simchowitz and Foster, 2020). We
overcome this challenge through a key insight: although each player’s perceived model is mis-
specified, the learned parameters implicitly capture theaggregate strategic effectsof all other
players. Consequently, each player effectively computes anoisy best responseto the oppo-
nents’ previous strategy profile. We further quantify the bias in this estimated best response
induced by all players’ exploration noises and show that it vanishes asymptotically.
Building on this insight, we prove that the multi-agentϵ-greedy ILS algorithm converges to
the complete-information Nash equilibrium under a stability condition and characterize its
convergence rate, both in finite samples (with high probability) and asymptotically (almost
surely) (Theorem 1). The result applies to asynchronous and random update schedules. The
convergence rate reveals a fundamental interplay between the intrinsic stability of the Nash
equilibrium, quantified by a stability constantζ∈(0,1), and the players’ learning hyperpa-
rameters including the epoch growth rateλand the exploration-noise schedule. In particular,
when all players adopt the optimal exploration-noise decay schedule from the single-agent
setting, the convergence rate exhibits a bifurcation. If the equilibrium is sufficiently sta-
ble, the algorithm (more precisely, the linear strategy parameters) achieves a last-iterate rate
˜O(t−1/4), matching the rate that enables optimal regret guarantees in the single-agent LQ
learning benchmark (Simchowitz and Foster, 2020). Otherwise, the performance is limited by
the game’s stability and the convergence rate is ˜O

t
lnζ
lnλ

, reflecting the convergence behav-
ior of the underlying idealized best-response dynamics. Finally, numerical experiments show
that when the equilibrium is not globally stable, the learning dynamics may exhibit persistent
oscillations.
•We apply our framework to a dynamic Cournot competition model with sticky prices and
study the economic consequences of decentralized learning.
Numerical experiments in duopoly markets validate the theoretical convergence rates and char-
acterize transitional market outcomes under different degrees of price stickiness. We examine
firm profits, total surplus, and market concentration along the path from initial learning to
equilibrium. While firms experience profit losses relative to the equilibrium benchmark during
the transition in both low- and high-stickiness markets, welfare implications differ substantially
across regimes: total surplus declines persistently only under high price stickiness, and market
concentration increases in both cases, with larger effects under high stickiness. These findings
highlight the importance of accelerating convergence in markets with strong frictions. We fur-
ther show that publicly releasing aggregate market quantity substantially improves learning
speed and mitigates the adverse transitional effects. Finally, by considering a (weakly) non-
linear inverse demand function, we demonstrate that the multi-agentϵ-greedy ILS algorithm
remains effective beyond the LQ setting, converging to an accurate linear approximation of
the equilibrium.
1.3 Related Work
Our work relates to several broad research areas, including learning in games, multi-agent rein-
forcement learning, and Cournot competitions. Given the vast literature in each area, we focus our
discussion on the studies most closely related to our work.
Nash equilibrium computation for LQ games.A growing body of work has developed learn-
ing algorithms for computing Nash equilibria inN-player LQ games. When the system parameters
are known, existing approaches include policy-gradient methods (Hambly et al., 2023; Mazumdar
et al., 2020; Plank and Zhang, 2026) and iterative Lyapunov- or Riccati-based schemes (Nortmann
4

et al., 2024). (Hambly et al., 2023; Nortmann et al., 2024; Vamvoudakis, 2015) further analyze
settings with unknown system parameters, but require access to joint state-action data from all
players or coordinated exploration schemes that specify the behavior of all agents.
Our work differs from this literature in two fundamental aspects. Conceptually, rather than de-
signing algorithms to compute Nash equilibria, we study whether the learning dynamics of strategic
agents converge to a complete-information Nash equilibrium under radically uncoupled information,
where players are unaware of and cannot observe their opponents. Technically, this information
constraint prevents players from identifying the true game model. Each player instead learns a
misspecified single-agent model from noisy observations and applies a standard single-agent learn-
ing algorithm, treating the strategic behavior of others as part of the environment. Our analysis
therefore requires characterizing how the learned policy approximates a best response, quantifying
the bias induced by exploration, and establishing convergence through a joint analysis of estimation
error, exploration, and equilibrium stability.
Cournot games with incomplete information.Our analysis of dynamic Cournot competition
is also related to the literature on Cournot games with incomplete information in economics and
operations research. A substantial body of literature studies Cournot games where firms possess
private information and face uncertain cost and demand (Bonatti et al., 2017; Gal-Or, 1985; Hauk
and Hurkens, 2001). The primary focus of this literature is on how firms learn hidden market
information and strategically signal to maximize profits. For example, Bonatti et al. (2017) considers
a new market in which each firm has private marginal cost and observes only a common revenue
process, but not its competitors’ quantities or costs. Using filtering techniques, they show that firms
converge to the static complete-information Nash equilibrium despite learning only the average cost
of their competitors.
A key distinction from our work is that these studies assume the underlying market model, such
as the inverse demand function, is known to all firms, so learning is limited to opponents’ private
information such as their costs or demand shocks. In contrast, we allow both the market model
and even the presence of competitors to be unknown. Consequently, firms must simultaneously
learn a misspecified model of the environment and adapt their strategies, rendering filtering-based
approaches inapplicable.
Learning in Cournot games.Several studies examine how firms learn and compete in repeated
Cournot games with unknown demand or cost parameters using trial-and-error methods (Huck
et al., 2004), neural networks (Barr and Saraceno, 2005), policy-gradient methods (Shi and Zhang,
2020), and no-regret learning (Ba et al., 2025; Nadav and Piliouras, 2010). In particular, reinforce-
ment learning agents in repeated Cournot games may learn collusive behaviors (Kimbrough et al.,
2005; Waltman and Kaymak, 2008), a phenomenon further studied in recent work (Deshpande and
Jacobson, 2026; Lin et al., 2024).
These studies, however, focus on repeated games with static market environments and therefore
do not directly apply to the price-stickiness setting considered in this paper. With price stickiness,
firms’ current decisions affect future market states, transforming the problem into a stochastic
game rather than a repeated game. This dynamic state dependence substantially complicates the
convergence analysis of learning dynamics compared with static games.
Notation.We denote by∥A∥the spectral norm of a matrixA, byσ min(A) its minimum singular
value, byr(A) its spectral radius, and byA ⊤ its transpose. For vectors,∥ · ∥2 denotes the Euclidean
norm. The notation≽(resp.≻) refers to the Loewner order:X≽Y(resp.X≻Y) meansX−Yis
positive semidefinite (resp. positive definite). We writeI dm for thed m-dimensional identity matrix
and 0m×n for them×nzero matrix. Finally,O(·) denotes standard asymptotic notation, and ˜O(·)
suppresses logarithmic factors.
5

The remainder of this paper is organized as follows. Section 2 formulates the infinite-horizon,
nonzero-sum LQ stochastic games and derives the multi-agentϵ-greedy ILS algorithm in the radically
uncoupled setting. Section 3 defines the feedback Nash equilibrium under complete information.
Section 4 states the main assumptions and establishes the convergence guarantees of the algorithm.
Section 5 applies the results to analyze learning in dynamic Cournot competition with sticky prices.
Section 6 provides a proof sketch of the main theorem in Section 4. Finally, Section 7 concludes.
All technical proofs and supplementary materials are collected in the appendix.
2 Problem Formulation
This section introduces a general setup for LQ stochastic games in a radically uncoupled environment
and outlines an online learning procedure for such games.
2.1 Setup of LQ Stochastic Games
Consider anM-player LQ stochastic game. For each playerm, letu m t ∈R dm denote its control
input at timet, and letx t ∈R n denote the common state. The state evolves according to the linear
dynamics
xt+1 =A 0 +Ax t +
MX
m=1
Bmum t +ω t, x 0 =x,(4)
where{ω t}∞ t=0 is an i.i.d. sub-Gaussian noise sequence with mean zero and covariance matrix
Cov(ωt) = Σω ≻0,x∈R n is a given initial state, and the system parameters (A0, A,{Bm}1≤m≤M ,Σ ω)
are unknown to all players. Each player is unaware of the existence of other players and observes
only the historical state sequence{x k}t+1 k=0 and their own past controls{u m k }t k=0 up to timet+ 1.
Playermaims to minimize the following discounted costs:
Jm

u

=E
" ∞X
t=0
ρtYm  xt, xt+1, um 
#
,
with the cost function is given by
Ym(xt, xt+1, um t ) =x ⊤ t Qmxt + (xt+1)⊤Hmum t + (um t )⊤Rmum t +x ⊤ t qm + (um t )⊤rm,(5)
where the coefficient matricesQ m ≽0 n×n,R m ≻0 dm×dm,H m, and vectorsq m,r m are known to
playermas private information but unknown to other players.
Note that we include the cross term (x t+1)⊤Hmum t in the cost (5) to capture the dynamic
Cournot competition model in Section 1.1. Due to these cross terms, the cost function may not be
strongly convex in the state-control pair. This differs from the standard quadratic costx ⊤ t Qmxt +
(um t )⊤Rmum t in the literature, whereQ m andR m are typically assumed to be positive definite to
ensure strong convexity. The lack of strong convexity introduces additional technical challenges,
including issues in the well-posedness of the game and the analysis of learning algorithms.
Since each player is unaware of the impact of other players’ actions on the state dynamics, they
form a misspecified model of the environment. Specifically, playermbelieves that the state evolves
according to the perceived model
xt+1 = Θ⊤ mzm t +ω ′ t, x 0 =x,(6)
wherez m t = [1, x ⊤ t ,(u m t )⊤]⊤,{ω ′ t}∞ t=0 is an i.i.d. sub-Gaussian sequence with mean zero and
unknown covariance matrix Σ m, and Θ m = [A′ 0, A′, B′ m]⊤ ∈R (1+n+dm)×n is the unknown (drift)
coefficient. This model is misspecified because it omits the control inputs of all other players. Player
mwill estimate (Θ m,Σ m) from their own observations to compute their strategies.
6

We focus on linear feedback strategies of the formu m t =−F mxt +f m +α mvm t , whereF m is
the feedback matrix governing the response to the current statex t,f m is an offset term capturing
state-independent actions,{v m t }∞ t=0 is an i.i.d. sub-Gaussian noise sequence with mean zero and
covariance matrixI dm, andα m ≥0 scales its magnitude. We denote a strategy for playermby the
triple (F m, fm, αm), and refer to (F m, fm) as the deterministic component (i.e., the strategy when
αm = 0). Playermchoosesα m to ensure suitable exploration, and selects (F m, fm) to minimize the
cost objective given current information.
To formulate each player’s optimization problem and facilitate the theoretical analysis, we re-
strict strategy parameters to the following boundedadmissible strategy sets:
Am ={F m ∈R dm×n :∥F m∥ ≤κm},B m ={f m ∈R dm :∥f m∥2 ≤κ ′ m}.
The constantsκ m, κ′ m >0 bound the allowable feedback and offset, respectively, reflecting physical
or economic constraints on playerm’s ability to implement control. For the Cournot model of
Section 1.1,κ m andκ ′ m directly represent production limits for price-based and active adjustments.
The admissible setsA m andB m constitute private information for playermand are unknown to
other players.
Given a perceived parameter pair (Θ m,Σ m), the initial pointx, and the exploration noise scale
αm, playermfaces the following optimization problem
inf
(Fm,fm)∈Am×Bm
J (Θm,Σm) m  (Fm, fm);x, αm  ,(7)
withJ (Θm,Σm) m  (Fm, fm);x, αm  =E
" ∞X
t=0
ρtYm  xt, xt+1,−F mxt +f m +α mvm t 
#
,
where for each (F m, fm)∈ Am × Bm, the statex t evolves according to the perceived dynamics (6)
under the parameters (Θ m,Σ m) and the control lawu m t =−F mxt +f m +α mvm t .
To ensure (7) is finite, playermrestricts the parameters to the followingfeasible parameter set
Sm:
Sm =

(Θm,Σ m) :−∞<inf (Fm,fm)∈Am×Bm J (Θm,Σm) m  (Fm, fm);x, αm  <∞,for allx∈R n, αm ≥0  .
(8)
For any (Θm,Σ m)∈ Sm andx∈R n, αm ≥0, there exists at least one optimal strategy
(Φm(Θm,Σ m, x, αm), ϕm(Θm,Σ m, x, αm))∈ Am × Bm to problem (7).
Within this setting, the next section introduces an online learning procedure in which every
player independently learns the environment and applies adaptive strategies to minimize her own
discounted cost.
2.2 Radically Uncoupled Multi-agentϵ−Greedy ILS Algorithm
We assume that each player independently follows anϵ-greedy ILS scheme over a sequence of
exponentially increasing epochs. In each epoch, a player implements a certainty-equivalent control
strategy by applying the optimal linear feedback policy corresponding to their current estimate of
the (potentially misspecified) system, together with an exploratory noise process to ensure sufficient
exploration. The main components of the learning process are summarized below.
Update schedule and exploration.Letτ (k) m denote the length (in time steps) of thek-th epoch
for playerm, e.g.τ (k) m =λ k for someλ >1.At the end of epochk, playermupdates her strategy,
which is then held fixed throughout the subsequent epoch of lengthτ (k+1) m . Playermalso specifies a
decaying sequence of exploration noise scales{α (k) m }∞ k=0. The decaying exploration schedule follows
7

the standard single-agent online learning framework (Simchowitz and Foster, 2020), reflecting the
assumption that each player behaves as if she were the sole decision-maker.
Players may employ heterogeneous update schedules and exploration noise scales, leading to
asynchronous learning. The precise conditions onτ (k) m andα (k) m (for convergence analysis) are given
in Condition 1 in Section 4.
Regularized least-squares (RLS) estimation and fallback.At the initial update, each player
independently selects a feasible initial parameter pair based on the information available at time
zero. At thek-th update point, playermestimates the parameters of the perceived model (6) by
solving a regularized least-squares problem using only data collected during the most recent epoch.
Specifically, playermconsiders the estimate
ˆΘ(k) m ∈arg min y∈R(1+n+dm)×n


βm∥y∥2 +
¯τ(k) m −1X
t=¯τ(k−1) m
∥xt+1 −y ⊤zm t ∥2 2


 ,(9)
where ¯τ(k) m = Pk i=1 τ (i) m is the cumulative number of time steps completed by playermup to the
end of thek-th update, andβ m >0 is a regularization constant. The estimate (9) admits the
closed-form expression
ˆΘ(k) m =  V (k) m −1


¯τ(k) m −1X
t=¯τ(k−1) m
zm t x⊤ t+1

 ,withV (k) m =β mI(1+n+dm) +
¯τ(k) m −1X
t=¯τ(k−1) m
zm t (zm t )⊤.(10)
Here we restrict the estimation to data from the most recent epoch. This reflects a natural behavioral
assumption: without observing the opponents, players update their perceived model using recent
observations that best represent the current environment. Similarly, the estimate of the perceived
noise covariance matrix is
ˆΣ(k) m = 1 τ (k) m


¯τ(k) m −1X
t=¯τ(k−1) m
(xt+1 −( ˆΘ(k) m )⊤zm t )(xt+1 −( ˆΘ(k) m )⊤zm t )⊤

 .(11)
Playermchecks whether the estimated parameter pair ( ˆΘ(k) m , ˆΣ(k) m ) belongs to the feasible set
Sm in (8) to ensure the solvability of the corresponding control problem. If feasible, the estimate is
accepted; otherwise, the player reuses the previous epoch’s parameter pair:
( ˜Θ(k) m , ˜Σ(k) m )←



( ˆΘ(k) m , ˆΣ(k) m ) if ( ˆΘ(k) m , ˆΣ(k) m )∈ Sm,
( ˜Θ(k−1) m , ˜Σ(k−1) m ) otherwise. (12)
ϵ-Greedy strategy execution.Using the parameter estimate ( ˜Θ(k) m , ˜Σ(k) m ), together with the
initial statex ¯τ(k) m and the current exploration scaleα (k) m , playermsolves the LQ control problem
(7) to obtain a minimizer
(F (k) m , f(k) m ) = (Φm( ˜Θ(k) m , ˜Σ(k) m , x¯τ(k) m , α(k) m ), ϕm( ˜Θ(k) m , ˜Σ(k) m , x¯τ(k) m , α(k) m )).(13)
For the next epoch, playermimplements theϵ-Greedy strategy with an additive exploratory noise:
um,(k+1) t =−F (k) m xt +f (k) m +α (k) m vm t ,(14)
8

Algorithm 1Radically Uncoupled Multi-agentϵ-Greedy ILS Algorithm
1:Require:Epoch length{τ (k) m }k≥1, exploration noise scales{α (k) m }k≥0, RLS parameterβ m,
feasible setS m, for 1≤m≤M
2:fort= 0,1,2, . . . ,do
3:form= 1,2, . . . , Mdo
4:Calculate max number of epochs up to timet:k m = sup{k: ¯τ(k) m ≤t}
5:ift= 0then
6:Initialize: select ( ˜Θ(0) m , ˜Σ(0) m )∈ Sm
7:ComputeF (0) m = Φm( ˜Θ(0) m , ˜Σ(0) m , x, α(0) m ) andf (0) m =ϕ m( ˜Θ(0) m , ˜Σ(0) m , x, α(0) m )
8:else ift= ¯τ (km) m then
9:Estimate and select ( ˜Θ(km) m , ˜Σ(km) m ) via (12)
10:ComputeF (km) m = Φm( ˜Θ(km) m , ˜Σ(km) m , xt, α(km) m ) andf (km) m =ϕ m( ˜Θ(km) m , ˜Σ(km) m , xt, α(km) m )
11:end if
12:Apply controlu m,(km+1) t as in (14)
13:end for
14:Observe statex t+1 from (4)
15:end for
where{v m t }∞ t=0 is an i.i.d. sub-Gaussian sequence with mean zero and covariance matrixI dm. The
noise scaleα (k) m is kept positive within each epoch to guarantee sufficient excitation, while gradu-
ally decaying across epochs to anneal exploration as the player gains more information about the
environment.
Algorithm 1 summarizes the procedure executed concurrently by all players and models learning
in the radically uncoupled environment described in Section 2.1. First, the algorithm satisfies the
radically uncoupled requirement of Foster and Young (2006): each player’s updates depend solely
on her own observed state trajectory and applied controls, without access to other players’ payoffs,
actions, or admissible strategy sets. Second, theϵ-greedy ILS scheme naturally captures the behavior
of a player who treats the environment as a single-agent online LQ control problem. This choice is
further justified by its optimality in the single-agent (average-reward) LQ setting: theϵ-greedy ILS
scheme achieves optimal regret with exponentially growing epochs and exploration noise decaying
as (τ (k+1) m )−1/4 (Simchowitz and Foster, 2020).
The central question we address is whether the joint learning dynamics generated by Algorithm 1
converge to the complete-information feedback Nash equilibrium. To answer this question, we first
characterize the feedback Nash equilibrium in the next section.
3 Feedback Nash Equilibrium under Complete Information
This section analyzes the LQ stochastic game introduced in Section 2.1 under complete information,
assuming that the true system dynamics (4) and all players’ strategies are known to every player.
We consider deterministic linear feedback strategies of the formum t =−F mxt+fm withF m ∈ Am
andf m ∈ Bm. Unlike the learning setting in Section 2.1, no exploration noise is introduced since
players have complete information. LetA:= QM m=1 Am andB:= QM m=1 Bm be the joint feedback
gains and offsets of all players, respectively, and letF={F m}1≤m≤M andf={f m}1≤m≤M be
generic elements inAandB, respectively. We writeA −m := Q j̸=m Aj andB −m := Q j̸=m Bj, and
denote by (F −m, f−m) = ({Fj}j̸=m,{f j}j̸=m)∈ A−m × B−m the strategies of all players other than
playerm.
Given other players’ strategies (F −m, f−m)∈ A−m × B−m and initial statex∈R n, playerm
9

considers the minimization problem
inf
(Fm,fm)∈Am×Bm
Jm

(Fm, fm); (F−m, f−m), x

,(15)
withJ m

(Fm, fm); (F−m, f−m), x

=E
" ∞X
t=0
ρtYm  xt, xt+1,−F mxt +f m 
#
,
where{x t}∞ t=0 follows the dynamic (4) with the strategy profile (F m, fm, F−m, f−m):
xt+1 =

A0 + X
j̸=m
Bjfj

 +

A− X
j̸=m
BjFj

 xt +B m(−Fmxt +f m) +ω t.(16)
Note that, under complete information, playermknows the true state dynamics (16), in contrast
to the radically uncoupled setting in Section 2.1, where playermperceives the state as evolving
according to the misspecified model (6).
Following the standard treatment of LQ games (Ba¸ sar and Olsder, 1998; Sun and Yong, 2019),
we define a feedback Nash equilibrium as a strategy profile from which no player has an incentive
to unilaterally deviate.
Definition 1.A policy profile(F ∗, f∗) = ({F ∗ m}1≤m≤M ,{f ∗ m}1≤m≤M )∈ A × Bis a feedback Nash
equilibrium if for all1≤m≤Mandx∈R n,J m  (F ∗ m, f∗ m); (F∗ −m, f∗ −m), x  is finite, and(F ∗ m, f∗ m) =
arg inf(Fm,fm)∈Am×Bm Jm

(Fm, fm); (F∗ −m, f∗ −m), x  .
To characterize best responses, we assume that given the strategy profile of other players, each
player’s optimization problem (15) admits a unique optimal strategy.
Assumption 1.(Well-posedness of best responses) For all1≤m≤M,x∈R n, and(F −m, f−m)∈
A−m × B−m, the infimum in problem(15)is attained at a unique minimizer that is independent of
the initial statex. Moreover, this minimizer is continuous in(F −m, f−m).
We denote the unique minimizer of problem (15) by (ψ m(F−m, f−m), φm(F−m, f−m)) and refer
to it as playerm’sbest responseto the strategy profile (F −m, f−m) of the other players. This defines
acollective best-response mapΨ :A × B → A × Bby
Ψ((F, f)) =

ψm(F−m, f−m)

1≤m≤M ,

φm(F−m, f−m)

1≤m≤M

.(17)
Because each component of Ψ is continuous, Ψ itself is continuous on the compact setA × B;
hence, by Brouwer’s fixed-point theorem, Ψ admits at least one fixed point. It follows directly from
Definition 1 and the definition of Ψ that a feedback Nash equilibrium corresponds to a fixed point
of this map. We state this existence and characterization in the following lemma.
Lemma 1.Under Assumption 1, there exists a fixed point(F ∗, f∗)ofΨ, i.e.,Ψ((F ∗, f∗)) =
(F ∗, f∗); moreover, a strategy profile is a feedback Nash equilibrium if and only if it is a fixed point
ofΨ.
To analyze the convergence of Algorithm 1, we further impose the following (global) stability
condition on the Nash equilibrium.
Assumption 2.(Stability of the feedback Nash equilibrium) There exist constantsµ >0and
0< ζ <1such that for all(F, f)∈ A × B,
Ψ((F, f))−Ψ((F ∗, f∗))  µ,1,2 ≤ζ (F, f)−(F ∗, f∗)  µ,1,2,
where(F ∗, f∗)is a fixed point ofΨ, and∥(F, f)∥ µ,1,2 :=µ PM m=1 ∥Fm∥  + PM m=1 ∥fm∥2  is a
weighted composite norm overA × B.
10

Assumption 2 implies that Ψ admits a unique fixed point, and hence a unique feedback Nash
equilibrium for the LQ game: any fixed point (F ′, f′) of Ψ satisfies∥(F ′, f′)−(F ∗, f∗)  µ,1,2 =Ψ((F ′, f′))−Ψ((F ∗, f∗))  µ,1,2 < (F ′, f′)−(F ∗, f∗)  µ,1,2, which forces (F ′, f′) = (F ∗, f∗). The
stability constantζalso plays a key role in establishing the convergence of the learning dynamics
and characterizing its convergence rate (see Theorem 1). Without the stability condition, learning
algorithms may fail to converge to the Nash equilibrium, even when it is unique (see Mazumdar
et al. (2020) for examples involving gradient-based algorithms). We investigate two representative
cases (that violate Assumption 2): a unique equilibrium exists but is locally unstable (i.e., the map
Ψ is not a local contraction around the equilibrium; see Section 5.4 for a formal definition), or
multiple locally stable equilibria coexist. In the former case, Section 5.4 shows that Algorithm 1
fails to converge and exhibits persistent oscillations. In the latter case, Appendix C.2 shows that
the algorithm may converge to one of the equilibria or exhibit oscillatory behavior.
4 Main Convergence Result
This section shows that, under suitable conditions, the asynchronousϵ-greedy ILS algorithm in
Algorithm 1 converges to the feedback Nash equilibrium (Definition 1) and further characterizes its
convergence rate.
We shall assume the state dynamics (4) is stable under all admissible policy profiles.
Assumption 3.It holds thatsup F∈A
A− MP
m=1
BmFm
 <1.
Assumption 3 ensures that the state process{x t}∞ t=0 in (4) remains stable under every admis-
sible strategy profile (see (16)). If this assumption is violated, numerical examples in Section 5.4
demonstrate that the state may explode. Consequently, the ridge regression in (9) may fail to yield
meaningful estimates, making theϵ-greedy ILS algorithm unimplementable.
We further assume the Lipschitz continuity of the optimal strategy map with respect to param-
eter estimates. To state the assumption formally, we define for each playermand (F −m, f−m)∈
A−m × B−m,
Θ(F−m,f−m) m =

A0 + X
j̸=m
Bjfj, A−
X
j̸=m
BjFj, Bm


⊤
,(18)
which captures the aggregate effect of other players’ linear strategies on the state dynamics from
playerm’s perspective; see (16).
Assumption 4.For all1≤m≤M, there exist constantsδ m, Lm ∈(0,∞)such that for all
( ˜Θm, ˜Σm)withmax  ∥ ˜Θm −Θ (F−m,f−m) m ∥,∥ ˜Σm −Σ ω∥ 	 ≤δ m, we have
(a)( ˜Θm, ˜Σm)∈ Sm.
(b) For all initial statexandα m ∈[0, δm], the control problem(7)admits a unique minimizer
(Φm( ˜Θm, ˜Σm, x, αm),ϕ m( ˜Θm, ˜Σm, x, αm))satisfying
Φm( ˜Θm, ˜Σm, x, αm)−Φ m(Θ(F−m,f−m) m ,Σ ω, x,0)  ≤L m∆m, ϕm( ˜Θm, ˜Σm, x, αm)−ϕ m(Θ(F−m,f−m) m ,Σ ω, x,0)  2 ≤L m∆m,
where∆ m = max

∥ ˜Θm −Θ (F−m,f−m) m ∥,∥ ˜Σm −Σ ω∥, αm 	 .
Assumption 1 ensures that (Θ (F−m,f−m) m ,Σ ω)∈ Sm for all (F −m, f−m)∈ A−m × B−m. As-
sumption 4((a)) strengthens this by requiring that parameters sufficiently close to (Θ (F−m,f−m) m ,Σ ω)
11

remain feasible. Consequently, once estimation errors become sufficiently small, (12) accepts the
new estimates and updates the parameters. Assumption 4((b)) requires the optimal strategy map
to be locally Lipschitz continuous, with a neighborhood sizeδ m and the Lipschitz constantL m
that are independent of the opponents’ strategies (F −m, f−m). This regularity is needed for our
convergence analysis, as it controls how estimation errors propagate through players’ best-response
updates (see Step 2 of the proof sketch in Section 6).
For standard LQ games without cross-product or linear terms (i.e.,Hm, qm, rm,andA 0 in (4) and
(5) are zero), Assumption 4 follows from classical sensitivity analysis (Konstantinov et al., 1993),
provided that the unconstrained minimizer of (15) lies in the interior ofA m × Bm. These results,
however, rely on positive definiteness of the quadratic objective. To the best of our knowledge,
corresponding sensitivity results for the more general class of LQ games considered here remain
unavailable. For the dynamic Cournot competition model in Section 5, we establish explicit sufficient
conditions ensuring Assumption 4; see Appendix B.3.
For convergence analysis, we impose the following condition on the epoch lengths and exploration
noise scales in Algorithm 1.
Condition 1.For all1≤m≤Mandk≥0, the epoch length and exploration noise used by player
min epochksatisfy
τ (k+1) m =  τ (k+1) + ˜τ(k+1) m  , α (k) m = ¯α(τ(k+1) m )−νm,
whereτ (k+1) =τ +τ λk+1 is the base epoch length with someλ >1,τ >0, andτ ≥0,˜τ (k+1) m is an
asynchronous shift taking values in[0,¯τ]for some¯τ >0, and¯α >0andν m ∈(0, 1 2 )are the base
exploration rate and decay rate, respectively.
Condition 1 captures the asynchronous learning of different players using a single-agent algo-
rithm, due to their unawareness of competitors. Consistent with the single-agent online LQ learning
literature (Simchowitz and Foster, 2020), we assume an exponential growth schedule for the base
epoch length{τ (k)}∞ k=1, reflecting that players deploy their policies for increasingly longer durations
as the learning proceeds. The choiceλ= 2 recovers the standard doubling trick (Besson and Kauf-
mann, 2018). Similarly, the decay rateν m ∈(0, 1 2 ) also follows the standard exploration schedule
in single-agent learning, ensuring persistent excitation for consistent parameter estimation while
allowing exploration to vanish asymptotically.
Unlike single-agent learning, we incorporate a player- and epoch-dependent shift ˜τ(k+1) m into the
learning epochs to accommodate asynchronicity across players when updating their strategies (recall
that strategy parameters are updated only at the end of each epoch). These shifts are allowed
to be random (e.g., uniformly distributed on [0,¯τ]), provided they are independent of the state
noise{ω t}∞ t=0 and the exploration noise{v m t }∞ t=0. While we assume bounded shifts for simplicity
of presentation, our convergence analysis can be readily extended to settings with polynomially
growing shifts.
We are now ready to present the main convergence theorem. To facilitate the discussion, we
introduce a few notations. Definek m(t) = sup{k: ¯τ (k) m ≤t}. Let (F (km(t)) m , f(km(t)) m ) denote the
strategy parameters used by playermat timet. We write (F (k(t)), f(k(t))) to denote the strategy
profile where playermemploys the strategy (F (km(t)) m , f(km(t)) m ) at timet.
Theorem 1.Suppose Assumptions 1-4 and Condition 1 hold. For anyδ∈(0,1), there exist
constantsc 0, c1 >0andT(δ) =O((log(1/δ)) c1)such that, with probability at least1−δ, for all
t≥T(δ),
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 =O  max{R1(t, δ), R2(t, δ), R3(t)}  ,(19)
where∥ · ∥µ,1,2 is defined in Assumption 2, and
R1(t, δ) =

(logt)
3
2 + (log 1 δ )c0  t lnζ lnλ , R 2(t, δ) = q logt+ log 1 δ t −( 1 2 −max m νm) , R 3(t) =t −min m νm .
(20)
12

Consequently, it holds almost surely that ast→ ∞,
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 = ˜O  t−q , q := min n − lnζ lnλ , 1 2 −max m νm,min m νm o .
Theorem 1 shows that Algorithm 1 converges to the complete-information equilibrium at a
polynomial rate, both with high probability (in finite samples) and almost surely (asymptotically).
The precise convergence rate is characterized by the interplay between the game characteristics and
the hyperparameters governing each player’s learning dynamics:
(1) The exponent− lnζ lnλ ofR 1 is the idealized convergence rate that would be achieved if all players
performed exact best-response oracle updates at the end of each epoch. Indeed, each best-
response update contracts the error by a factor ofζ(the stability constant in Assumption 2).
Since the epoch lengths grow geometrically with ratioλ, the number of updates completed by
timetis approximately lnt/lnλ. Hence, the error at timetscales asζ lnt/lnλ =t lnζ/lnλ . A
smaller value ofλleads to more frequent best-response updates and hence faster asymptotic
convergence.
(2) The above idealized rate is, however, degraded in our radically uncoupled learning setting,
where players do not observe their opponents and perform estimation and exploration under
misspecified models. Consequently, the convergence rate is constrained by the minimum of
1
2 −max m νm and min m νm, which correspond to the bottleneck decay rates of least-squares
estimation errors and exploration noise, respectively. The radically uncoupled structure is
reflected in the dependence of the convergence rate onindividualexploration schedules: each
player must independently generate informative data through its own exploration, even though
all players’ exploration noises simultaneously affect the state dynamics.
If all players adoptν m = 1 4 , the optimal exploration noise decay rate for single-agent LQ learning
(Simchowitz and Foster, 2020), then the convergence rate of Algorithm 1 exhibits a bifurcation
phenomenon governed by the stability of the Nash equilibrium. Whenζ≤λ − 1 4 (i.e., the equilibrium
is sufficiently stable), the convergence rate (19) (with fixedδ) simplifies to
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 =O p logt·t − 1 4  .
which is confirmed by our numerical experiments in Section 5.1. This rate coincides with the
parameter convergence rate that enables optimal regret guarantees in single-agent LQ learning
(Simchowitz and Foster, 2020). In contrast, whenζ > λ− 1 4 (i.e., the equilibrium is less stable), the
convergence rate is dominated by the factort
lnζ
lnλ =ζ
lnt
lnλ , which depends on the effective number of
strategy updates performed up to timet.
5 Application: Dynamic Cournot Competition with Sticky Prices
In this section, we apply our LQ game framework to a dynamic Cournot competition model with
sticky prices. The dynamic Cournot competition model introduced in Section 1.1 is a special case
of the general LQ game in Section 2.1, with price serving as the state and quantities as the control
actions.
Specifically, the correspondence between the two formulations is established in the following
three aspects. First, the price dynamics (1) can be expressed in the general form (4) by taking
A0 = (1−s)a,A=s,B m =−(1−s)b, and Σ ω =σ 2 ω. Second, a firm’s misspecified statistical
model (3) coincides with (6) upon setting Θ m = [(1−s ′)a′, s′,−(1−s ′)b′]⊤,Σ m =σ 2 m. Third, for
playerm, maximizing the total expected discounted profit is equivalent to minimizing the following
discounted cost:
E
" ∞X
t=0
ρt
 1
2 qm t −p t+1 +c m

qm t
#
.(21)
13

The running cost in (21) aligns with the general form in (5) by setting the parameters asQ m =
0, Rm = 1 2 , Hm =−1, qm = 0, rm =c m. Consequently, Algorithm 1 is directly applicable to this set-
ting. Appendix B.1 provides further implementation details, including a verifiable characterization
of the feasible set (8) for implementing (12) and a procedure for computing the greedy strategy.
In the sequel, we first present numerical experiments for a duopoly Cournot game to confirm
the theoretical convergence results and examine how the price stickiness parameter affects market
outcomes along the transition path to equilibrium. We then show that publicly releasing aggregate
quantity information significantly accelerates convergence and mitigates the adverse transition ef-
fects identified above. Finally, we demonstrate that the multi-agentϵ-greedy ILS algorithm remains
effective under a weakly nonlinear inverse demand function and investigate cases violating Assump-
tions 1-4 to illustrate the role of these conditions. For simplicity, we use Gaussian noise for both
market disturbances and exploration noises.
5.1 Numerical Experiments in Duopoly Markets
Duopoly market is a common setting in the dynamic Cournot competition model with sticky prices
(Fershtman and Kamien, 1987; Heston and Hu, 2024). In this section, we investigate the perfor-
mance of Algorithm 1 under different levels of price stickiness and examine the resulting market
outcomes.
We use the following model and algorithm parameters: number of firmsM= 2, discount factor
ρ= 0.8, noise varianceσ 2 ω = 1.00, inverse demand parametersa= 60.0 andb= 0.3, cost parameters
c1 = 20.0 andc 2 = 30.0, initial pricep 0 = 40, and production capacity limitsκ m = 1.50,κ ′ m = 500
form= 1,2. We examine three price stickiness levels:s= 0.2 (low stickiness, fast price adjustment),
s= 0.5 (moderate stickiness), ands= 0.8 (high stickiness, slow price adjustment). For each selected
stickiness parameter, we perform 200 independent simulations of Algorithm 1 with hyperparameters
λ= 1.1,τ= 300,τ = 2000, ¯τ= 200,ν m = 0.25, ¯α= 2.0, andβ m = 0.01 form= 1,2. In each
simulation, every player performs 130 updates over a total ofT≈7.2×10 8 time steps. At each
update, the asynchronous shift of each player is sampled independently from a uniform distribution
on [0,¯τ]. In all simulations, no negative prices or quantities are observed, indicating that such events
occur with negligible probability.
The chosen model parameters satisfy Assumptions 1–4, and the algorithm parameters satisfy
Condition 1; see Appendix B.3 for details. Hence, Theorem 1 applies to the settings considered
here. The equilibrium strategies (F ∗, f∗) and the stability coefficientζfor each stickiness level are
reported in Table 1, where we note thatF ∗ 1 =F ∗ 2 .
5.1.1 Convergence Rates of Learning Dynamics
To estimate the convergence rate, we define for each epochkthe relative error of the updated
strategy parameters with respect to the equilibrium and take the maximum across the two players:
RE(k) F = max m=1,2
(
|F (k) m −F ∗ m|
|F ∗m|
)
,RE (k) f = max m=1,2
(
|f (k) m −f ∗ m|
|f ∗m|
)
.(22)
We regress the relative error against the elapsed time on a log-log scale. For each epochk, we record
the relative errors together with the corresponding elapsed time step (using the cumulative time of
the player attaining the maximum error). To reduce Monte Carlo variability, we average both the
relative errors and the elapsed time steps over 200 independent runs before fitting the power-law
model RE (k(t)) =θ 0t−θ1 using the final 50 epochs.
The estimated decay exponentθ 1 is remarkably close to the theoretical value of 0.25 across all
tested values ofs; see Table 1. This agreement is consistent with Theorem 1. Indeed, for every
tested value ofs, the estimated stability coefficientζsatisfiesζ < λ −1/4 = 0.9765, implying that
14

the equilibrium is sufficiently stable, and hence the convergence rate is governed by the decay of the
estimation error and exploration noise. Figures 1 and 2 further illustrate the predictedt −1/4 decay
fors= 0.2 ands= 0.8.
Table 1: Equilibrium strategies, stability coefficients, and convergence rates with different price
stickiness levels
StickinessF ∗ 1 (F ∗ 2 )f ∗ 1 f ∗ 2 Stability RE F REf
s ζ θ 0 θ1 θ0 θ1
0.2 -0.1160 16.8841 9.0615 0.5831 1.1209 0.2699 1.0407 0.2573
0.5 -0.3390 6.6769 -1.4260 0.5625 0.9550 0.2498 3.8618 0.2740
0.8 -0.6520 -7.0131 -15.6836 0.5324 1.6430 0.2486 1.0045 0.2547
104 106 108
Time
10−3
10−2
10−1
100
101
RE(k) F
Full Sample
Estimation Sample
Fitted Line
(a)s= 0.2
104 106 108
Time
10−3
10−2
10−1
100
101
RE(k) F
Full Sample
Estimation Sample
Fitted Line (b)s= 0.8
Figure 1: Convergence of feedback gainFunder different price stickiness levels
104 106 108
Time
10−3
10−2
10−1
100
101
RE(k) f
Full Sample
Estimation Sample
Fitted Line
(a)s= 0.2
104 106 108
Time
10−3
10−2
10−1
100
101
RE(k) f
Full Sample
Estimation Sample
Fitted Line (b)s= 0.8
Figure 2: Convergence of offsetfunder different price stickiness levels
5.1.2 Market Outcomes under Low and High Price Stickiness
We now compare the market outcomes generated by the learning dynamics under low (s= 0.2) and
high (s= 0.8) price stickiness. We focus on four key performance measures: average price, firm
profits, economic welfare, and market concentration.
We begin by introducing the corresponding performance measures under the complete-information
Nash equilibrium (F ∗, f∗), which serves as the benchmark for evaluating the learning dynamics. Un-
15

der the equilibrium strategy, the price process{p t}∞ t=0 defined by (1) is asymptotically stationary,
allowing the long-run market performance measures to be defined in terms of its stationary dis-
tribution. Ast→ ∞, the distribution ofp t converges to a Gaussian distribution with mean and
variance
µp = (1−s)(a−b P2 m=1 f ∗ m) 1−  s+ (1−s)b P2 m=1 F ∗m  , σ 2 p = σ2 ω 1−  s+ (1−s)b P2 m=1 F ∗m 2 .
The expected stationary profit of firmmunder the equilibrium is then given by
Π∗ m =E h pt+1 −c m − 1 2 qm t  qm t i ,(23)
whereq m t =−F ∗ mpt +f ∗ m,p t+1 follows (1), andp t ∼ N(µp, σ2 p). To measure overall social welfare,
including both producers and consumers, we use total surplus (TS), a standard welfare measure in
Cournot games (Bonatti et al., 2017; Cellini and Lambertini, 2007):
TS∗ =
2X
m=1
Π∗ m +E h 1 2 (a−p t+1) 2X
m=1
qm t
i
,
where Π∗ m is given by (23), andq m, pt+1 are defined as in (23). Finally, to measure market concen-
tration, we use the Herfindahl–Hirschman Index (HHI), the standard measure in Cournot games
(Bonatti et al., 2017):
HHI∗ =E


2X
m=1

qm tP2
m=1 qm t
!2
 ,
withq m defined as in (23). The HHI captures how market output is distributed across firms, with
higher values indicating greater concentration. Table 2 reports the values ofµ p,σ 2 p, Π ∗ 1, Π ∗ 2, TS ∗,
and HHI∗ with different price stickiness.
Table 2: Equilibrium values of market indicators
s µ p σ2 p Π∗ 1 Π∗ 2 TS∗ HHI∗
0.2 48.82 1.0213 395.62 168.71 772.63 0.5220
0.8 48.02 2.0874 386.24 160.08 784.42 0.5237
We now investigate the evolution of the above performance measures under the learning dy-
namics. For each of the 200 independent simulations of Algorithm 1, we compute at every epoch
the sample mean of each performance indicatorW(average price, firm profits, TS, HHI) from
300 time points sampled uniformly throughout the epoch, representing and approximating the true
epoch-average performance despite varying epoch lengths. LetW (k) denote this sample mean for
epochk. The deviation from the equilibrium benchmark is ∆W (k) =W (k) −W ∗. We examine the
biasE[∆W (k)] to capture systematic over-/underestimation, where the expectation is taken over
the 200 independent runs. To improve plot readability, all results reported below exclude the initial
fifteen epochs.
Figure 3 shows that the bias of the epoch-average price,E∆µ (k) p , is negative fors= 0.2 (the price
is systematically lower than the equilibrium level) but oscillates around zero fors= 0.8. Turning to
the firm level, the profits of the two firms exhibit systematic negative biases under both stickiness
levels (Figure 4). The extent of these biases depends on the model parameters. Under our parameter
choices, for firm 1, which has the lower marginal cost, the negative bias is substantially larger under
s= 0.8 than unders= 0.2. For firm 2, the magnitude of the negative bias is comparable across the
two stickiness levels, but the bias exhibits greater fluctuation across epochs unders= 0.8.
16

Epoch
20 40 60 80 100 120
Bias
-0.25
-0.2
-0.15
-0.1
-0.05
0
0.05
0.1
0.15
s=0.2
s=0.8
Figure 3: Bias in average price
Epoch
20 40 60 80 100 120
Bias
-10
-8
-6
-4
-2
0
2
s=0.2
s=0.8
(a) Firm 1
Epoch
20 40 60 80 100 120
Bias
-5
-4
-3
-2
-1
0
1
s=0.2
s=0.8 (b) Firm 2
Figure 4: Bias in firm profits
Epoch
20 40 60 80 100 120
Bias
-12
-10
-8
-6
-4
-2
0
2
4
s = 0.2
s = 0.8
Figure 5: Bias in total surplus
Epoch
20 40 60 80 100 120
-2
0
2
4
6
8
10
Bias
×10−3
s=0.2
s=0.8 Figure 6: Bias in HHI
At the society level, the bias of total surplus (TS) is shown in Figure 5. TS exhibits a slight
positive bias fors= 0.2, while fors= 0.8 it remains consistently below its equilibrium level (negative
bias). Regarding market concentration, during the transition from an emerging to a mature market,
the HHI remains above its equilibrium level and gradually declines toward it (Figure 6). This
over-concentration phenomenon is consistent with observations in the literature on Cournot games
with incomplete information (see Bonatti et al. (2017)). The extent of over-concentration is more
pronounced under higher stickiness (s= 0.8).
17

Taken together, these results reveal both common features and important differences between
the two price-stickiness regimes. From the perspective of individual firms, profits remain below
their equilibrium benchmarks throughout the transition under both regimes. At the societal level,
however, total surplus remains persistently below its equilibrium benchmark only under high price
stickiness, while market concentration is elevated in both regimes and is substantially higher when
price stickiness is high. These findings suggest that radically uncoupled learning is particularly
costly in highly sticky markets, reducing both firm profitability and overall social welfare during the
transition to equilibrium. Moreover, these qualitative patterns are robust across a range of model
and algorithm parameters we test. In particular, we obtain similar results for markets with more
than two firms and when players employ heterogeneous exploration noise decay rates.
5.2 Accelerating Convergence Through Aggregate Information
The findings of the previous section suggest that under high price stickiness, both firms and a
market regulator have strong incentives to accelerate convergence to the equilibrium. One natural
intervention is for the regulator to publicly release the aggregate market quantityQ t = PM m=1 qm t
in real time. With this additional information, the information structure no longer falls within the
radically uncoupled setting studied earlier: each firm can now observe the aggregate outputs of
its competitorsQ −m t :=Q t −q m t , and thus explicitly account for their presence. This additional
information enables firms to better infer the underlying market environment and competitors’ be-
havior, leading them to adopt more informed best-response strategies. We therefore introduce a
modified version of Algorithm 1 that exploits the publicly available aggregate market output. Al-
though the algorithm is still executed independently by each firm, it is no longer radically uncoupled
because it leverages the aggregate market quantity. As we show below, this additional information
substantially accelerates convergence to the equilibrium.
Firms continue to follow the asynchronous update schedules and exploration noise scales spec-
ified in Algorithm 1. The main modification concerns the system estimation step in Section 2.2:
instead of performing a single RLS regression, each firm now conducts two separate RLS regressions
using the additional information on aggregate market output. The first regression directly estimates
the true price dynamics (1) based on the observed aggregate output. The second regression esti-
mates the aggregate policy profile of the competitors, allowing the firm to anticipate their strategic
behavior and formulate a more accurate best-response strategy. Specifically, taking firmmas the
representative firm, it assumes that the aggregate quantity of the other firms is linear in price:
Q−m t =−F ′ −mpt +f ′ −m +v −m t ,
whereF ′ −m andf ′ −m are the aggregated feedback coefficient and offset term of all other firms, and
v−m t is a residual term with perceived varianceσ 2 v,−m. At thek-th update time ¯τ (k) m , firmmuses
the data collected during thek-th epoch to perform the two regressions, obtaining estimates of
the price dynamics parameters (ˆs(k),ˆa(k), ˆb(k),ˆσ2,(k) ω ) and the prediction of other firms’ aggregate
behavior ( ˆF (k) −m, ˆf (k) −m,ˆσ2,(k) v,−m). Based on these estimates, firmmthen forms the following belief about
the (controlled) price dynamics:
pt+1 = ˆs(k)pt + (1−ˆs(k))  ˆa(k) − ˆb(k) qm t − ˆF (k) −mpt + ˆf (k) −m +v −m,(k) t  +ω (k) t ,(24)
whereQ −m t :=− ˆF (k) −mpt + ˆf (k) −m +v −m,(k) t represents the estimated aggregate behavior of other firms,
and{ω (k) t }∞ t=1 and{v −m,(k) t }∞ t=1 are i.i.d. zero-mean sub-Gaussian sequences with variances ˆσ 2,(k) ω
and ˆσ2,(k) v,−m, respectively. Note that (24) can be rewritten in the form of (6) with Θ m = ˆΘ(k),c m and
18

Σm = ˆΣ(k),c m , where
ˆΘ(k),c m = [(1−ˆs(k))(ˆa(k) − ˆb(k) ˆf (k) −m),ˆs(k) + (1−ˆs(k))ˆb(k) ˆF (k) −m,−(1−ˆs (k))ˆb(k)]⊤,
ˆΣ(k),c m = ˆσ2,(k) ω + ((1−ˆs(k))ˆb(k))2ˆσ2,(k) v,−m.
Firmmthen applies the same fallback rule as in (12) to maintain feasibility of ( ˆΘ(k),c m , ˆΣ(k),c m ),
computes the greedy strategy using the accepted parameters, and executes the resulting strategy
with additive exploration noise in the next epoch, as in Algorithm 1.
We test this modified algorithm using the same model and algorithm settings as in Section 5.1,
focusing on the high-stickiness cases= 0.8. We perform 200 independent runs, each consisting of
100 updates per player, corresponding to a total ofT≈4.2×10 7 time steps. The results show
that the modified algorithm converges to equilibrium approximately six times faster, measured by
the number of time steps required for the relative errors RE (k) F and RE(k) f in (22) to fall below 0.01.
Moreover, Figures 7 and 8 show that during the transition phase the negative biases of both firms’
profits and total surplus are substantially smaller (cf. Figures 4 and 5). These findings suggest that
publicly revealing the aggregate quantity accelerates market maturation by improving the efficiency
of the learning dynamics and bringing them closer to the equilibrium.
Intuitively, the acceleration from publicly releasing the aggregate quantityQ t arises from the
improved information structure. In the radically uncoupled setting, each firm can only leverage
its own exploration noise to improve estimation, whereas observingQ t allows firms to exploit the
aggregate exploration signals of all market participants. Consequently, the regression estimation
benefits from richer, more informative data. This improves the accuracy of parameter estimation
and accelerates convergence to equilibrium.
Epoch
20 30 40 50 60 70 80 90
Bias
-3
-2.5
-2
-1.5
-1
-0.5
0
0.5
1
Firm 1
Firm 2
Figure 7: Bias in firm profits
Epoch
20 30 40 50 60 70 80 90
Bias
-3.5
-3
-2.5
-2
-1.5
-1
-0.5
0
0.5 Figure 8: Bias in total surplus
5.3 Robustness with Nonlinear Demand Functions
This section illustrates the robustness of Algorithm 1 when the true inverse demand function is
weakly nonlinear. We consider the dynamic Cournot competition model as in Section 1.1, but
replace the linear inverse demand with the nonlinear functiona−b
PM
m=1 qm t δ, whereδ >0 is a
curvature parameter (Bulow and Pfleiderer, 1983). The true price dynamics become
pt+1 =sp t + (1−s)

a−b
 MX
m=1
qm t
δ
!
+ω t,(25)
which reduces to the linear case studied in Section 1.1 whenδ= 1. We now focus on the nonlinear
case withδ̸= 1. Each firmmcontinues to maximize its discounted expected profit given by
19

(2). The complete-information Nash equilibria are nonlinear functions of pricep, and are computed
numerically by solving coupled Bellman equations. In the radically uncoupled learning setting, each
firm continues to employ linear feedback strategies and adopt the misspecified linear model (3), since
the true nonlinear form of the inverse demand function is unknown to the firm. Consequently, the
firms’ behaviors follow Algorithm 1, except that the price evolves according to the true nonlinear
dynamics (25).
We sets= 0.8 and consider two nonlinearity parametersδ= 0.9 andδ= 1.1, with all other
parameters fixed as in Section 5.1. For each configuration, we first compute the feedback equilibrium
numerically and conduct 50 independent simulations. In each simulation, we compare the trajectory
generated by Algorithm 1 with a benchmark trajectory in which all firms follow the equilibrium
strategy throughout. Both trajectories are driven by the same sequence of price shocks. Denote by
qm t the quantity produced by firmmunder Algorithm 1 at timet, and by ¯q m t the corresponding
equilibrium quantity. For each epochk, we uniformly sample 300 time pointsT k, measure the
trajectory error by
Err(k) = max
m=1,2
1
300
X
t∈Tk

qm t −¯qm t 2,
and report the average the error over the 50 independent simulations.
Figure 9 shows the error in production quantities forδ= 0.9 andδ= 1.1. In both cases,
the error gradually decreases and eventually stabilizes at a positive level. The error in the final
epoch is 0.1422 forδ= 0.9 and 0.0484 forδ= 1.1, which are significantly smaller than the typical
quantity levels observed during the simulations (in the range 10–30, depending on the firm and price
level). The remaining error does not vanish because the true equilibrium strategy is nonlinear, while
Algorithm 1 restricts the learned strategy to be linear. Nevertheless, the approximation error is small
relative to the scale of production decisions. These results show that, even under weak nonlinearity,
the radically uncoupled learning algorithm converges to an accurate linear approximation of the
complete-information equilibrium.
Epoch
80 90 100 110 120 130
Err(k)
0
0.5
1
1.5
2
δ = 0.9
δ = 1.1
Figure 9: Errors in production quantities for
differentδ.
5.4 Results Beyond Theoretical Assumptions
This section presents numerical experiments that illustrate the importance of the assumptions un-
derpinning our theoretical analysis.
Assumption 3 concerns the stability of the state process{x t}∞ t=0 under all admissible strategy
profiles; it affects the consistency of the RLS estimator and can be checked directly. The other three
assumptions (Assumptions 1, 2, and 4) are about the game structure and are closely related. We
therefore treat them as a group. They can be verified via sufficient conditions expressed solely in
20

terms of the model parameters (see conditions 2-3 in Appendix B.3) for the Cournot model). Alter-
natively, we can detect violations by examining the number of equilibria and their local behavior.
When an equilibrium (F ∗, f∗) exists, we call itlocally stableif the collective best-response map Ψ
is well-defined in a neighborhood of (F ∗, f∗) (i.e., problem (15) admits a unique minimizer for all
1≤m≤M,x∈R n, and (F −m, f−m) sufficiently close to (F ∗ −m, f∗ −m)) and the spectral radius of
its Jacobian matrix at (F ∗, f∗) satisfiesr(DΨ(F ∗, f∗))<1; otherwise it is locally unstable. Note
that local stability is a weaker condition than Assumption 2. Thus, if the spectral radius ofDΨ
at the equilibrium exceeds 1, then Assumption 2 must be violated. In addition, the existence of
multiple equilibria also violates Assumption 2; we examine the behavior of Algorithm 1 in this case
in Appendix C.2, where the algorithm may converge to one of the equilibria or exhibit oscillatory
behavior.
Here we consider two parameter configurations under the Cournot setting. The common pa-
rameters across both groups area= 40.0,b= 2.0,s= 0.2, andσ 2 ω = 1.00.
Group 1 (violation of state stability).This group violates Assumption 3 while satisfying the
remaining assumptions, in particular having a globally stable equilibrium. The specific parameters
are:
ρ= 0.4, M= 2, c 1 = 10.0, c2 = 20.0, κm = 0.7, κ′ m = 5000 (m= 1,2).
Group 2 (violation of equilibrium stability).This group satisfies Assumption 3 but violates
Assumption 2. The specific parameters (for a Cournot game with four players) are:
ρ= 0.8, M= 4, c 1 =c 3 = 10.0, c2 =c 4 = 20.0, κm = 0.12, κ′ m = 500 (1≤m≤4).
Our numerical analysis suggests a unique equilibrium for this group. Computing the spectral radius
of the Jacobian matrix at this equilibrium yieldsr(DΨ) = 1.1160>1, so the equilibrium is not
locally stable and Assumption 2 is violated.
For each group, we execute 200 independent runs of Algorithm 1. Each player uses the same
algorithm parameters as in Section 5.1, and the total number of time steps is set identically. We
classify the outcome of each simulation into three categories:
•Explode: the state variable pricep t grows without bound, causing the algorithm to fail.
•Oscillatory: the strategy parameters continue to fluctuate and do not settle near any fixed
point.
•Converge to Equilibrium: the strategy parameters approach (a small neighborhood of) the
feedback Nash equilibrium.
Table 3 summarizes the percentage of simulations falling into each category for the two groups.
Table 3: Distribution of learning outcomes
Parameter Group Explode (%) Oscillatory (%) Converge to Equilibrium (%)
Group 1 52.00 0.00 48.00
Group 2 0.00 100.00 0.00
The results reveal the following patterns. A violation of Assumption 3 means that some admissi-
ble strategy profiles render the state process unstable. When the learning algorithm encounters such
a profile, the state explodes; indeed, a substantial fraction of simulations for Group 1 (52%) exhibit
explosive behavior. However, there also exist admissible strategy profiles that are stabilizing. In the
remaining 48% of simulations, the particular realized sequence of strategy profiles{(F (k), f(k))}∞ k=0
does not cause the state process to become unstable, and the algorithm runs without explosion even
though Assumption 3 fails. In these non-explosive runs, since the other assumptions are satisfied,
all paths converge to the feedback Nash equilibrium.
21

For Group 2, Assumption 3 holds, so no explosion occurs. However, because the equilibrium is
not locally stable, none of the simulation paths converge to it. Instead, all trajectories exhibit a
persistentbest-response cycle: the strategy profile alternates between two distinct non-equilibrium
points, each constituting the collective best response to the other. Similar cyclic behavior has been
observed in evolutionary games with logit dynamics (Hommes and Ochea, 2012) and policy gradient
methods for LQ games (Mazumdar et al., 2020). Figure 10 shows a representative trajectory in
the later epochs, illustrating that the strategy parameters continue to cycle without settling. This
demonstrates that a unique Nash equilibrium alone is insufficient to guarantee convergence; local
stability is also essential.
Epoch
110 120 130
F (k) 1
-0.15
-0.1
-0.05
0
0.05
0.1
Epoch
110 120 130
F (k) 2
-0.15
-0.1
-0.05
0
0.05
0.1
Epoch
110 120 130
F (k) 3
-0.15
-0.1
-0.05
0
0.05
0.1
Epoch
110 120 130
F (k) 4
-0.15
-0.1
-0.05
0
0.05
0.1
Figure 10: Oscillatory dynamics when Assumption 2 is violated (Group 2). The four subfigures
correspond to four players. In each subfigure, the solid line isF (k) m and the dashed line is the
equilibrium valueF ∗ m.
6 Sketched Proof of Theorem 1
This section outlines the main steps in proving Theorem 1. We first present the main ideas in the
synchronous setting (Steps 1–3) and then discuss the additional technical challenges involved in
extending the analysis to asynchronous updates (Step 4). Throughout this section,Cdenotes a
generic finite constant independent of the epoch indexkand the probability boundδ; its value may
change from line to line.
In the synchronous case, all players share the same update times:τ (k) m =τ (k) for everym. Let
(F (k), f(k)) denote the strategy profile after thek-th update. From playerm’s perspective, during
epochkthe true state dynamics (4) induced by all players’ strategies become
xt+1 = (Θ
(F (k−1) −m ,f (k−1) −m ) m )⊤zm t + ˜ωm t ,
where Θ
(F (k−1) −m ,f (k−1) −m ) m is defined in (18) with (F −m, f−m) = (F (k−1) −m , f(k−1) −m ), and{˜ωm t }∞ t=0 is an i.i.d.
sub-Gaussian sequence with mean zero and covariance matrix Σ ω + P
j̸=m
(α(k−1) j )2BjB⊤ j . Crucially,
in contrast to the single-player case (Simchowitz and Foster, 2020), playermfaces a misspecified
model (6), and hence cannot identify the true system parameters (A 0, A,{Bm},Σ ω). Instead, they
will asymptotically learn theeffective system parametersat thek-th epoch given by
Θ(k),∗ m = Θ (F (k−1) −m ,f (k−1) −m ) m ,Σ (k),∗ m = Σω + X
j̸=m
(α(k−1) j )2BjB⊤ j .(26)
We show that this procedure corresponds to a biased best response to (F (k−1) −m , f(k−1) −m ), and quantify
the decay rate of the resulting bias in (33).
22

Step 1: Estimation error bounds.We first quantify the estimation error of the RLS estimate
( ˆΘ(k) m , ˆΣ(k) m ) relative to the effective system parameters (Θ (k),∗ m ,Σ (k),∗ m ). Specifically, we establish the
following high-probability error bound: for anyδ∈(0,1), there existsK m(δ) =O(log log(1/δ))
such that, with probability at least 1−δ,
∀k≥K m(δ),max
n ˆΘ(k) m −Θ (k),∗ m ,  ˆΣ(k) m −Σ (k),∗ m  o ≤C η (k) m (δ),(27)
where the decay rateη (k) m (δ) is given by
η(k) m (δ) =
r
k+ log(1/δ)
λ(1−2νm)k .(28)
The proof builds upon the arguments in Simchowitz and Foster (2020), but requires substantially
more involved analysis due to the presence of constant offsets in the dynamics and policies, which in-
troduce non-excited directions, and the need to jointly estimate the drift and covariance parameters
(Θ(k),∗ m ,Σ (k),∗ m ). Extending the analysis to asynchronous updates requires further technical efforts
(see Step 4).
Step 2: F rom estimation error to strategy deviation.Bounding∥Σ (k),∗ m −Σ ω∥via (26)
and combining it with (27) yield the following high-probability bound
max{∥ ˆΘ(k) m −Θ (k),∗ m ∥,∥ ˆΣ(k) m −Σ ω∥} ≤Cmax

η(k) m (δ),max j̸=m (α(k−1) j )2

.(29)
Since bothη (k) m (δ) andα (k) m vanish askgrows, the right-hand side of (29) is smaller than the
thresholdδ m in Assumption 4 for all sufficiently largek. Assumption 4((a)) then guarantees that
playermaccepts the current estimate, so the bound (29) also holds for the accepted parameter
pair ( ˜Θ(k) m , ˜Σ(k) m ). By Assumption 4((b)), for anyδ∈(0,1), there existsK ′ m(δ)∈Nsuch that, with
probability at least 1−δ, for allk≥K ′ m(δ),
max
nF (k) m −Φ m(Θ(k),∗ m ,Σ ω, x,0)  , f (k) m −ϕ m(Θ(k),∗ m ,Σ ω, x,0)  2 o ≤Cmax  η(k) m (δ),max 1≤j≤M α(k−1) j  ,
(30)
where (F (k) m , f(k) m ) = (Φm( ˜Θ(k) m , ˜Σ(k) m , x, α(k) m ), ϕm( ˜Θ(k) m , ˜Σ(k) m , x, α(k) m )).
Now we observe the following key identity:
(Φm(Θ(k),∗ m ,Σ ω, x,0), ϕm(Θ(k),∗ m ,Σ ω, x,0)) = (ψm(F (k−1) −m , f(k−1) −m ), φm(F (k−1) −m , f(k−1) −m )),(31)
where the best response map (ψ m, φm) is given in (17). Indeed, consider the complete-information
problem (15) with other players’ strategies (F (k−1) −m , f(k−1) −m ). In this case, the dynamic (16) can be
rewritten in the form of (6) with Θ m = Θ(k),∗ m , Σm = Σω, andu m t =−F mxt +f m, which means that
the aggregate effect of the opponents’ linear strategies on the state evolution is captured by Θ (k),∗ m .
Since playermfaces the same objective in both settings, solving the complete-information problem
is equivalent to solving the control problem (7) with the parameters (Θ (k),∗ m ,Σ ω) andα m = 0. This
implies that
Jm

(Fm, fm); (F(k−1) −m , f(k−1) −m ), x  =J (Θ(k),∗ m ,Σω) m  (Fm, fm);x,0  ,(32)
and directly yields (31).
Combining (30) and (31) allows for interpreting (F (k) m , f(k) m ) as anoisy best responseto the
opponents’ previous strategy profile (F (k−1) −m , f(k−1) −m ). The error can be controlled in a high prob-
ability byη (k) m (δ) and max 1≤j≤M α(k−1) j . Specifically, we prove that, for anyδ∈(0,1), there exists
K(δ) =O(log log(1/δ)) such that, with probability at least 1−δ,
∀k≥K(δ),∥(F (k), f(k))−Ψ((F (k−1), f(k−1)))∥µ,1,2 ≤Cξ k(δ),(33)
23

where
ξk(δ) =
p
k+ log(1/δ)λ
−( 1 2 −max m {νm})k +λ −(min m {νm})k .(34)
Step 3: Convergence via the stability of the feedback Nash equilibrium.Under
Assumptions 1–2, there exists a unique stable feedback Nash equilibrium (F ∗, f∗). On the event
(33), we have
∥(F (k), f(k))−(F ∗, f∗)∥µ,1,2 ≤ ∥(F(k), f(k))−Ψ((F (k−1), f(k−1)))∥µ,1,2
+∥Ψ((F (k−1), f(k−1)))−Ψ((F ∗, f∗))∥µ,1,2
≤Cξ k(δ) +ζ∥(F (k−1), f(k−1))−(F ∗, f∗)∥µ,1,2,
whereζ∈(0,1) is given in Assumption 2. Solving this recursive inequality case-by-case, depending
on the relative sizes ofζ,λ
−( 1 2 −max m νm) , andλ −min m νm , and using the fact that the epoch lengths
grow exponentially at rateλto translate epoch counts into real timetprove Theorem 1 in the
synchronous case.
Step 4: Asynchronous updates.When players update at different times (see Condition 1),
we partition the timeline into synchronous and asynchronous phases, and analyze them separately.
Synchronous phases are intervals during which all players have completed the same number of
updates; the remaining time constitutes asynchronous phases.
Asynchronous updates introduce several additional technical complications in our convergence
analysis: (i) the estimation error decompositions contain extra terms from asynchronous phases that
must be bounded separately; (ii) the epoch indexk m(t) in the expression (F (k(t)), f(k(t))) may differ
across players; and (iii) random asynchronous shifts introduce an additional source of randomness,
making update times random as well. Condition 1 ensures the asynchronous time in epochkis
O(k) and thatk/τ (k) m is summable, which allows us to control these extra terms and to replace
individual indices by a common index when deriving rates. When the shifts are independent of the
other randomness, we first condition on theσ-algebra generated by all shifts, carry out the analysis
under this conditioning, and then remove the conditioning using the uniform boundedness of the
shifts. By carefully handling these aspects, the convergence analysis in Steps 1–3 carries over to the
asynchronous setting.
7 Conclusion
In this paper, we provide the first convergence analysis for a radically uncoupled learning procedure
in LQ stochastic games. We demonstrate that the last-iterate convergence rate is fundamentally
driven by the interplay of three factors: the decay of the estimation error, the decay of the explo-
ration noise, and the stability of the Nash equilibrium. Furthermore, we apply this framework to
a dynamic Cournot competition model with sticky prices, illustrating how varying levels of price
stickiness alter market trajectories during transitions from emerging to mature phases within a
highly restrictive informational environment.
Several directions merit further investigation. First, it is of interest to rigorously justify the
accelerated convergence induced by publicly revealing aggregate market output, as observed in
our numerical experiments. Second, extending our analysis to other stochastic games with infinite
state-action spaces would broaden its applicability and deepen the theoretical understanding of
radically uncoupled learning in complex dynamic environments. Third, studying asymmetric in-
formation settings, where players possess heterogeneous structural knowledge, may provide further
economic insights. Finally, applying uncoupled learning procedures to other dynamic economic and
operational models remains a promising direction for future research.
24

References
Abada, I. and Lambin, X. (2023). Artificial intelligence: Can seemingly collusive outcomes be
avoided?Management Science, 69(9):5042–5065.
Ba, W., Lin, T., Zhang, J., and Zhou, Z. (2025). Doubly optimal no-regret online learning in
strongly monotone games with bandit feedback.Operations Research, 73(6):3219–3244.
Barr, J. and Saraceno, F. (2005). Cournot competition, organization and learning.Journal of
Economic Dynamics and Control, 29(1-2):277–295.
Ba¸ sar, T. and Olsder, G. J. (1998).Dynamic noncooperative game theory. SIAM.
Bervoets, S., Bravo, M., and Faure, M. (2020). Learning with minimal information in continuous
games.Theoretical Economics, 15(4):1471–1508.
Besson, L. and Kaufmann, E. (2018). What doubling tricks can and can’t do for multi-armed
bandits.arXiv preprint arXiv:1803.06971.
Boggs, P. T. and Tolle, J. W. (1995). Sequential quadratic programming.Acta numerica, 4:1–51.
Bonatti, A., Cisternas, G., and Toikka, J. (2017). Dynamic oligopoly with incomplete information.
The Review of Economic Studies, 84(2):503–546.
Bulow, J. I. and Pfleiderer, P. (1983). A note on the effect of cost changes on prices.Journal of
Political Economy, 91(1):182–185.
Cellini, R. and Lambertini, L. (2007). A differential oligopoly game with differentiated goods and
sticky prices.European Journal of Operational Research, 176(2):1131–1144.
Chen, Z., Zhang, K., Mazumdar, E., Ozdaglar, A., and Wierman, A. (2024). Last-iterate con-
vergence of payoff-based independent learning in zero-sum stochastic games.arXiv preprint
arXiv:2409.01447.
De la Pe˜ na, V. H., Lai, T. L., and Shao, Q.-M. (2009).Self-normalized processes: Limit theory and
Statistical Applications. Springer.
Deshpande, S. and Jacobson, S. H. (2026). Strategic AI in cournot markets.arXiv preprint
arXiv:2601.17263.
Dockner, E. J., Jorgensen, S., Long, N. V., and Sorger, G. (2000).Differential games in economics
and management science. Cambridge university press.
Fazel, M., Ge, R., Kakade, S., and Mesbahi, M. (2018). Global convergence of policy gradient
methods for the linear quadratic regulator. InProceedings of the 35th International Conference
on Machine Learning, pages 1467–1476. PMLR.
Fershtman, C. and Kamien, M. I. (1987). Dynamic duopolistic competition with sticky prices.
Econometrica: Journal of the Econometric Society, 55(5):1151–1164.
Foster, D. P. and Young, H. P. (2006). Regret testing: Learning to play nash equilibrium without
knowing you have an opponent.Theoretical Economics, 1(3):341–367.
Gal-Or, E. (1985). Information sharing in oligopoly.Econometrica: Journal of the Econometric
Society, 53(2):329–343.
Hager, W. W. and Horowitz, L. L. (1976). Convergence and stability properties of the discrete riccati
operator equation and the associated optimal control and filtering problems.SIAM Journal on
Control and Optimization, 14(2):295–312.
Hambly, B., Xu, R., and Yang, H. (2023). Policy gradient methods find the nash equilibrium in n-
player general-sum linear-quadratic games.Journal of Machine Learning Research, 24(139):1–56.
Hauk, E. and Hurkens, S. (2001). Secret information acquisition in cournot markets.Economic
Theory, 18:661–681.
Heston, S. L. and Hu, B. (2024). Dynamic duopolistic competition with sticky prices.Operations
25

Research, 73(5):2627–2635.
Hommes, C. H. and Ochea, M. I. (2012). Multiple equilibria and limit cycles in evolutionary games
with logit dynamics.Games and Economic Behavior, 74(1):434–441.
Horn, R. A. and Johnson, C. R. (2012).Matrix analysis. Cambridge university press.
Huck, S., Normann, H.-T., and Oechssler, J. (2004). Through trial and error to collusion.Interna-
tional Economic Review, 45(1):205–224.
Kimbrough, S. O., Lu, M., and Murphy, F. (2005). Learning and tacit collusion by artificial agents
in cournot duopoly games. InFormal modelling in electronic commerce, pages 477–492. Springer.
Konstantinov, M. M., Petkov, P. H., and Christov, N. D. (1993). Perturbation analysis of the
discrete riccati equation.Kybernetika, 29(1):18–29.
Lin, R. Y., Ojha, S., Cai, K., and Chen, M. F. (2024). Strategic collusion of LLM agents: Market
division in multi-commodity competitions.arXiv preprint arXiv:2410.00031.
Maheshwari, C., Wu, M., Pai, D., and Sastry, S. (2025). Independent and decentralized learning in
markov potential games.IEEE Transactions on Automatic Control, 70(11):7538–7553.
Mania, H., Tu, S., and Recht, B. (2019). Certainty equivalence is efficient for linear quadratic
control.Advances in neural information processing systems, 32.
Mazumdar, E., Ratliff, L. J., Jordan, M. I., and Sastry, S. S. (2020). Policy-gradient algorithms
have no guarantees of convergence in linear quadratic games. InProceedings of the 19th Interna-
tional Conference on Autonomous Agents and Multiagent Systems, pages 860–868. International
Foundation for Autonomous Agents and Multiagent Systems.
Muhle-Karbe, J. and Oomen, R. (2026). Pre-hedging.Operations Research, 74(3):1221–1240.
Nadav, U. and Piliouras, G. (2010). No regret learning in oligopolies: Cournot vs. bertrand. In
International Symposium on Algorithmic Game Theory, pages 300–311. Springer.
Nocedal, J. and Wright, S. J. (2006).Numerical optimization. Springer.
Nortmann, B., Monti, A., Sassano, M., and Mylvaganam, T. (2024). Nash equilibria for linear
quadratic discrete-time dynamic games via iterative and data-driven algorithms.IEEE Transac-
tions on Automatic Control, 69(10):6561–6575.
Ozdaglar, A., Sayin, M. O., and Zhang, K. (2022). Independent learning in stochastic games. In
International Congress of Mathematicians, volume 7, pages 5340–5373.
Plank, P. and Zhang, Y. (2026). Learning distributed equilibria in linear-quadratic stochastic
differential games: Anα-potential approach.arXiv preprint arXiv:2602.16555.
Sayin, M., Zhang, K., Leslie, D., Basar, T., and Ozdaglar, A. (2021). Decentralized q-learning in
zero-sum markov games.Advances in Neural Information Processing Systems, 34:18320–18334.
Shapley, L. S. (1953). Stochastic games.Proceedings of the national academy of sciences,
39(10):1095–1100.
Shi, Y. and Zhang, B. (2020). Multi-agent reinforcement learning in cournot games. In2020 59th
ieee conference on decision and control (cdc), pages 3561–3566. IEEE.
Simchowitz, M. and Foster, D. (2020). Naive exploration is optimal for online LQR. InProceedings
of the 37th International Conference on Machine Learning, pages 8937–8948. PMLR.
Simchowitz, M., Mania, H., Tu, S., Jordan, M. I., and Recht, B. (2018). Learning without mixing:
Towards a sharp analysis of linear system identification. InProceedings of the 31st Conference
On Learning Theory, pages 439–473. PMLR.
Sun, J. and Yong, J. (2019). Linear–quadratic stochastic two-person nonzero-sum differential
games: Open-loop and closed-loop nash equilibria.Stochastic Processes and their Applications,
129(2):381–418.
Vamvoudakis, K. G. (2015). Non-zero sum nash Q-learning for unknown deterministic continuous-
26

time linear systems.Automatica, 61:274–281.
Vershynin, R. (2018).High-dimensional probability: An introduction with applications in data sci-
ence. Cambridge university press.
Vives, X. (1984). Duopoly information equilibrium: Cournot and bertrand.Journal of economic
theory, 34(1):71–94.
Waltman, L. and Kaymak, U. (2008). Q-learning agents in a cournot oligopoly model.Journal of
Economic Dynamics and Control, 32(10):3275–3293.
Xiong, Y., Chen, N., and Gao, X. (2024). Is thompson sampling susceptible to algorithmic collusion?
arXiv preprint arXiv:2405.17463.
Zhang, K., Yang, Z., and Ba¸ sar, T. (2021). Multi-agent reinforcement learning: A selective overview
of theories and algorithms.Handbook of reinforcement learning and control, pages 321–384.
27

Additional Notation.
We use∨and∧to denote maximum and minimum, respectively: for real numbersa, b,a∨b=
max{a, b}anda∧b= min{a, b}. The relationa k ≍b k indicates that there exist positive constants
c, Csuch thatcb k ≤a k ≤Cb k for all sufficiently largek. The unit sphere inR n is denoted byS n−1,
i.e., the set of vectorsv∈R n with∥v∥ 2 = 1. Throughout this appendix, 0≤C <∞denotes a
generic constant depending on model and algorithm parameters; its value may change from line to
line. When a constant associated with a quantityXneeds to be explicitly referenced, we use CX ,
CX , andL X to denote upper bounds, lower bounds, and Lipschitz constants, respectively. All these
constants are independent of the time indext, the epoch indexk, and the probability boundδ.
A Proof of Theorem 1
The proof is divided into several parts. Appendix A.1 bounds the error of the RLS estimator for
a representative playermin each epoch. Appendix A.2 bounds the deviation between the current
strategy profile and the collective best response to the previous profile, i.e.,∥(F (k+1), f(k+1))−
Ψ((F (k), f(k)))∥µ,1,2. Based on these results, Appendix A.3 completes the proof of Theorem 1.
Appendix A.4 presents the proofs of the auxiliary lemmas in Appendix A.1. All analysis is conducted
under Assumptions 1–4 and Condition 1.
In every run of Algorithm 1 there are three independent sources of randomness: the state noise
{ωt}∞ t=0, the exploration noise{v m t }∞ t=0, and the asynchronous shifts{˜τ (k) m }∞ k=1. We first condition
on theσ-algebraT=σ({˜τ (k) m : 1≤m≤M, k≥1}) generated by all shifts and carry out the
subsequent analysis under this conditioning. Conditioning onTturns each epoch lengthτ (k) m into a
deterministic constant satisfyingτ (k) ≤τ (k) m ≤τ (k) + ¯τfor everymandk; all remaining randomness
then comes only from the state and exploration noises. Throughout the rest of this section up
to the end of the derivation of Theorem 1, every statement is understood under the conditional
probabilityP(· | T), andEdenotes the corresponding conditional expectation. For brevity we keep
the notationPandEwithout explicit conditioning. All constants that appear in the bounds are
deterministic and depend only on the parameters of Condition 1; consequently they are uniform
over all realizations ofT. The unconditional statements of the theorem are recovered in Step 4 of
Appendix A.3 by taking expectation overTvia the law of total probability.
A.1 Estimation error of( ˆΘ(k) m , ˆΣ(k) m )
In this section we fix a representative playermand bound the errors of herk-th RLS estimates ˆΘ(k) m
and ˆΣ(k) m relative to the effective parameters (Θ (k),∗ m ,Σ (k),∗ m ) defined in (26). The analysis for other
players is identical. The main result is the following proposition.
Proposition 1.Suppose Assumptions 3 and 4 and Condition 1 hold. For anyδ∈(0,1)there exist
Km(δ) =O(log log(1/δ))and a constantC <∞such thatP(E m(δ))≥1−δ, where
Em(δ) =
n
∀k≥K m(δ) : max

∥ ˆΘ(k) m −Θ (k),∗ m ∥,∥ ˆΣ(k) m −Σ (k),∗ m ∥ 	 ≤C η(k) m (δ) o ,
withη (k) m (δ)defined in(28).
The proof of Proposition 1 requires addressing several key difficulties beyond the analysis for
the classical single-player LQ problem (Simchowitz and Foster, 2020). First, due to the presence
of constant offsets in the dynamics and linear cost terms, the regression vectorz m t contains a
non-excited direction (the constant 1), which requires extra care when establishing the growth rate
of the information matrix. Second, the asynchronous periods introduce additional terms in the
28

decomposition of ˆΘ(k) m −Θ (k),∗ m , which must be bounded separately. Third, unlike the uncontrolled
LQ setting where only the drift parameter error is estimated, here we must also bound the covariance
estimation error∥ ˆΣ(k) m −Σ (k),∗ m ∥.
We introduce several auxiliary lemmas to handle these three difficulties. To prepare for their
statements, we first allocate the failure probability and rewrite the state dynamics from playerm’s
viewpoint.
Probability allocation and dynamic characterization.For a given confidenceδ∈(0,1)
setδ k = 6δ/[π 2(k+ 1) 2]; then P∞ k=0 δk =δ. All high-probability statements that follow are first
established for asingleepochkwith failure probability proportional toδ k. Summing these bounds
overkvia a union bound will yield the “for all largek” statement in Proposition 1.
Under Algorithm 1, the state dynamics (4) can be rewritten from playerm’s viewpoint as
xt+1 = (Θ∗ m,t)⊤zm t + ˜wm t , z m t = [1, x⊤ t ,(u m,(km(t)) t )⊤]⊤,(35)
where ˜wm t is independent sub-Gaussian with mean zero and covariance matrix Σ ∗ m,t, and
Θ∗ m,t = h A0 + X
j̸=m
Bjf (kj (t)) j , A− X
j̸=m
BjF (kj (t)) j , Bm i⊤ ,Σ ∗ m,t = Σω + X
j̸=m
(α(kj (t)) j )2BjB⊤ j .
Auxiliary lemmas.Lemmas 2-4 below address the three difficulties mentioned above. They
employ two-sided bounds on sub-Gaussian matrices (Theorem 4.6.1 of Vershynin (2018)), the block
martingale small-ball (BMSB) condition (Simchowitz et al., 2018), the self-normalised martingale
inequality (Lemma E.2 of Simchowitz and Foster (2020) or Theorem 14.7 of De la Pe˜ na et al.
(2009)), and Rayleigh quotient techniques; together they lead to the polylogarithmic threshold
O(log log(1/δ)). Detailed proofs of Lemmas 2-4 are deferred to Appendix A.4. Lemma 5 is a direct
consequence of Lemma E.2 of Simchowitz and Foster (2020).
Lemma 2(Information matrix).There exist constantsC V , CV >0andK V,m(δ) =O(log log(1/δ))
such that for everyk≥K V,m(δ), it holds for some eventE V,k withP(E V,k )≥1−δ k/4that
σmin

V (k) m  ≥C V τ (k) m (α(k−1) m )2,∥V (k) m ∥ ≤CV τ (k) m ,det(V (k) m )≤( CV τ (k) m )1+n+dm.
Lemma 3(Asynchronous bias).There existsK A,m(δ) =O(log log(1/δ))such that for allk≥
KA,m(δ), it holds for some eventE A,k withP(E A,k)≥1−δ k/4that
max



 ¯τ(k) m −1X t=¯τ(k−1) m zm t (zm t )⊤(Θ∗ m,t −Θ (k),∗ m )⊤  ,  ¯τ(k) m −1X t=¯τ(k−1) m (Θ∗ m,t −Θ (k),∗ m )⊤zm t ( ˜wm t )⊤     ≤C  k2+log(1/δ)  .
Lemma 4(Noise covariance).There existsK cov,m(δ) =O(log log(1/δ))such that for everyk≥
Kcov,m(δ), it holds for some eventE cov,k withP(E cov,k)≥1−δ k/4that
 1 τ (k) m ¯τ(k) m −1X t=¯τ(k−1) m  ˜wm t ( ˜wm t )⊤ −Σ (k),∗ m   ≤Cη (k) m (δ).
29

Lemma 5(Self-normalised noise bounds).For eachk≥1, it holds for some eventE ω,k with
P(Eω,k)≥1−δ k/4that
 (V (k) m )−1 ¯τ(k) m −1X t=¯τ(k−1) m zm t ( ˜wm t )⊤  ≤C vuut log det(V (k) m ) + log(1/δk) σmin(V (k) m ) ,(36)
 1 τ (k) m ¯τ(k) m −1X t=¯τ(k−1) m zm t ( ˜wm t )⊤  ≤C vuut (log det(V (k) m ) + log(1/δk))∥V (k) m ∥ (τ (k) m )2 .(37)
For the rest of this section we setK joint,m(δ) := max{K V,m, KA,m, Kcov,m}=O(log log(1/δ))
and define, for eachk≥K joint,m(δ), the joint good eventE k =E V,k ∩E A,k ∩E ω,k ∩E cov,k.By the
union bound,P(E k)≥1−δ k. We now show that onE k both the drift parameter error∥ ˆΘ(k) m −Θ(k),∗ m ∥
and the covariance error∥ ˆΣ(k) m −Σ (k),∗ m ∥are bounded byCη (k) m (δ).
Error bound for ˆΘ(k) m .By the definitions of ˆΘ(k) m in (10), Θ (k),∗ m in (26), and (35),
ˆΘ(k) m −Θ (k),∗ m =−β m(V (k) m )−1Θ(k),∗ m| {z }
I1
+ (V (k) m )−1
¯τ(k) m −1X
t=¯τ(k−1) m
zm t (zm t )⊤(Θ∗ m,t −Θ (k),∗ m )⊤
| {z }
I2
+ (V (k) m )−1
¯τ(k) m −1X
t=¯τ(k−1) m
zm t ( ˜wm t )⊤
| {z }
I3
.(38)
We analyze each term onE k:
•By the eigenvalue lower bound in Lemma 2,∥I 1∥ ≤βm∥Θ(k),∗ m ∥ σmin(V (k) m ) ≤C/[τ (k) m (α(k−1) m )2]≤Cη (k) m (δ).
•By Lemma 3 and the eigenvalue bound,∥I 2∥ ≤ C(k 2+log(1/δ)) σmin(V (k) m ) ≤C k2+log(1/δ) τ (k) m (α(k−1) m )2 . Because
τ (k) m (α(k−1) m )2 ≍λ (1−2νm)k grows exponentially with exponent 1−2ν m > 1 2 −ν m, while the
numerator is polynomial inkand log(1/δ), there existsK Θ,m(δ) =O(log log(1/δ)) such that
for allk≥K ′ Θ,m(δ) this term is bounded byCη (k) m (δ).
•Substituting the eigenvalue bounds of Lemma 2 into (36) gives∥I 3∥ ≤Cη(k) m (δ).
Hence, for everyk≥max{K joint,m(δ), KΘ,m(δ)}, on the eventE k,
∥ ˆΘ(k) m −Θ (k),∗ m ∥ ≤Cη(k) m (δ).(39)
Error bound for ˆΣ(k) m .By the definitions of ˆΣ(k) m in (11), Σ (k),∗ m in (26), and (35),
ˆΣ(k) m −Σ (k),∗ m = Λ1 + Λ2 + Λ3 + Λ4 + Λ5 + Λ6 + (Λ4 + Λ5 + Λ6)⊤,(40)
where
Λ1 = (Θ(k),∗ m − ˆΘ(k) m )⊤

 1
τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
zm t (zm t )⊤

 (Θ(k),∗ m − ˆΘ(k) m ),Λ 2 = 1 τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
˜wm t ( ˜wm t )⊤−Σ(k),∗ m ,
30

Λ3 = 1
τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
(Θ∗ m,t −Θ (k),∗ m )⊤zm t (zm t )⊤(Θ∗ m,t −Θ (k),∗ m ),
Λ4 = 1
τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
(Θ∗ m,t −Θ (k),∗ m )⊤zm t (zm t )⊤(Θ(k),∗ m − ˆΘ(k) m ),
Λ5 = 1
τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
(Θ∗ m,t −Θ (k),∗ m )⊤zm t ( ˜wm t )⊤,Λ 6 = 1 τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
(Θ(k),∗ m − ˆΘ(k) m )⊤zm t ( ˜wm t )⊤.
We now bound the Λ i onE k.
•Λ 2 is directly controlled by Lemma 4:∥Λ 2∥ ≤Cη(k) m (δ).
•Asynchronous terms Λ 3,Λ 4,Λ 5. Using Lemma 3 and the bound∥Θ ∗ m,t −Θ (k),∗ m ∥ ≤Cand
∥ ˆΘ(k) m −Θ (k),∗ m ∥ ≤Cη(k) m (δ), we obtain
∥Λ3∥+∥Λ 5∥ ≤C(k 2 + log(1/δ))
τ (k) m ,∥Λ 4∥ ≤C(k 2 + log(1/δ)) τ (k) m η(k) m (δ).(41)
•Remaining terms Λ 1,Λ 6. OnE V,k the empirical moment satisfies
 1 τ (k) m ¯τ(k) m −1P t=¯τ(k−1) m zm t (zm t )⊤  ≤C.
Together with the cross term bound in Lemma 5 and∥ ˆΘ(k) m −Θ (k),∗ m ∥ ≤Cη(k) m (δ) gives that
∥Λ1∥ ≤C

η(k) m (δ) 2,∥Λ 6∥ ≤C
vuut log(τ (k) m ) + log(1/δ)
τ (k) m η(k) m (δ).(42)
As withI 2 in the analysis of ˆΘ(k) m , the exponential growth of the denominator guarantees the
existence ofK Σ,m(δ) =O(log log(1/δ)) such that all error bounds in (41) and (42) are bounded by
Cη (k) m (δ) for allk≥K Σ,m(δ). Thus,k≥max{K joint,m(δ), KΣ,m(δ)}, on the eventE k, we have
∥ ˆΣ(k) m −Σ (k),∗ m ∥ ≤Cη(k) m (δ).(43)
Proof of Proposition 1.TakeK m(δ) = max

Kjoint,m(δ), KΘ,m(δ), KΣ,m(δ)

=O(log log(1/δ)).
Define the eventE m(δ) = T k≥Km(δ) Ek. By the union bound,P(E m(δ)c)≤ P k≥Km(δ) P(Ec k)≤P
k≥Km(δ) δk ≤δ. OnE m(δ), for allk≥K m(δ) the estimates (39) and (43) hold simultaneously,
giving max{∥ ˆΘ(k) m −Θ (k),∗ m ∥,∥ ˆΣ(k) m −Σ (k),∗ m ∥} ≤Cη(k) m (δ).
A.2 Strategy Deviation of(F (k), f(k))
We first translate the estimation error bounds obtained in Appendix A.1 into bounds on the accepted
parameters ( ˜Θ(k) m , ˜Σ(k) m , α(k) m ) relative to (Θ (k),∗ m ,Σ ω,0).
Lemma 6.Suppose Assumptions 3 and 4 and Condition 1 hold. For anyδ∈(0,1), there exist
K′ m(δ) =O(log log(1/δ))and a constantC <∞such thatP(E ′ m(δ))≥1−δ, where
E′ m(δ) = n ∀k≥K ′ m(δ),max  ∥ ˜Θ(k) m −Θ (k),∗ m ∥,∥ ˜Σ(k) m −Σ ω∥, α(k) m 	 ≤C  η(k) m (δ)∨max 1≤j≤M {α(k−1) j } o .
31

Proof.Proof LetE m(δ) be the event from Proposition 1. OnE m(δ), for allk≥K m(δ) we have
∥ ˆΘ(k) m −Θ (k),∗ m ∥ ≤Cη(k) m (δ) and∥ ˆΣ(k) m −Σ (k),∗ m ∥ ≤Cη(k) m (δ). By definition of Σ (k),∗ m in (26),∥Σ (k),∗ m −
Σω∥ ≤Cmax j̸=m (α(k−1) j )2, so on the same event
max{∥ ˆΘ(k) m −Θ (k),∗ m ∥,∥ ˆΣ(k) m −Σ ω∥} ≤C  η(k) m (δ)∨max j̸=m (α(k−1) j )2 .(44)
From the definition ofη (k) m (δ) in (28) and the fact thatα (k) j ≍λ −νj k, there existsK ′′ m(δ) =
O(log log(1/δ)) such that for allk≥K ′′ m(δ) the right-hand side of (44) is smaller than the constant
δm from Assumption 4. TakeK ′ m(δ) = max{Km(δ), K′′ m(δ)}; thenK ′ m(δ) =O(log log(1/δ)). Part 1)
of Assumption 4 then guarantees ˜Θ(k) m = ˆΘ(k) m and ˜Σ(k) m = ˆΣ(k) m for allk≥K ′ m(δ).
Finally, the deterministic bound max{α (k) m ,max j̸=m (α(k−1) j )2} ≤Cmax 1≤j≤M {α(k−1) j }holds for allk.
LetE ′ m(δ) be the eventE m(δ), but with the statement required only fork≥K ′ m(δ). SinceK ′ m(δ)≥
Km(δ), we haveP(E ′ m(δ))≥P(E m(δ))≥1−δ.
Now we consider the strategy profile (F (k), f(k)), by which we mean that every player uses the
strategy (F (k) m , f(k) m ) obtained after herk-th update. Due to the presence of asynchronous shifts,
this profile may differ from the profile (F (k(t)), f(k(t))) that appears in Theorem 1; the two profiles
coincide only during the synchronous phases. Here we first derive the deviation of (F (k+1), f(k+1))
from the collective best response Ψ((F (k), f(k))) based on the error bound for the accepted param-
eters established above. This strategy deviation serves as an intermediate result for the proof of
Theorem 1; the actual profile (F (k(t)), f(k(t))) for arbitrarytwill be handled in the next section.
Lemma 7.Suppose Assumptions 1-4 and Condition 1 hold. For anyδ∈(0,1), there existK(δ) =
O(log log(1/δ))andL F f<∞such thatP(E(δ))≥1−δ, where
E(δ) =
n
∀k≥K(δ),∥(F (k+1), f(k+1))−Ψ((F (k), f(k)))∥µ,1,2 ≤L F fξk+1(δ) o ,
withξ k(δ)defined in(34)and the norm∥ · ∥ µ,1,2 defined in Assumption 2.
Proof.Proof SetK(δ) = max
m
K′ m(δ/M), whereK ′ m(·) is from Lemma 6; thenK(δ) =O(log log(1/δ)).
By definition,η (k) m (δ)∨max 1≤j≤M {α(k−1) j } ≤C ξk(δ) for allk≥1. Since Θ (k+1),∗ m = Θ (F (k) −m,f (k) −m) m by (26),
the equivalence in Assumption 1 gives
ψ(F (k) −m, f(k) −m) = Φm(Θ(k+1),∗ m ,Σ ω, x,0), φ(F (k) −m, f(k) −m) =ϕ m(Θ(k+1),∗ m ,Σ ω, x,0).
On the event TM m=1 E′ m(δ/M), for allk≥K(δ),
∥(F (k+1), f(k+1))−Ψ((F (k), f(k)))∥µ,1,2 =µ
MX
m=1
∥F (k+1) m −Φ m(Θ(k+1),∗ m ,Σ ω, x,0)∥
+
MX
m=1
∥f (k+1) m −ϕ m(Θ(k+1),∗ m ,Σ ω, x,0)∥2
≤C
 MX
m=1
Lm

(µ+ 1)ξ k+1(δ),
where we used Lemma 6 and Assumption 4. TakingLF f=C( P m Lm)(µ+1) gives TM m=1 E′ m(δ/M)⊂
E(δ). The probability estimate follows fromP(E(δ))≥P( TM m=1 E′ m(δ/M))≥1− PM m=1 δ/M≥
1−δ.
32

A.3 Proof of Theorem 1
Let (F ∗, f∗) denote the unique feedback Nash equilibrium guaranteed by Assumptions 1-2, and let
(µ, ζ) be the corresponding constants.
Step 1.We first show that with high probability (F (k), f(k)) converges to (F ∗, f∗). Seta k =
∥(F (k), f(k))−(F ∗, f∗)∥µ,1,2. By Lemma 7 and Assumption 2, for anyδ∈(0,1) there existsK(δ) =
O(log log(1/δ)) such that, with probability at least 1−δ, for allk≥K(δ),
ak+1 ≤ζa k +L F fξk+1(δ).
Define the constants
r1 = λ
−( 1 2 −max m {νm})
ζ , r 2 = λ
−min
m
{νm}
ζ .
Letc K(δ) = 2 PM m=1(κm +κ ′ m) andc k+1 =ζc k +L F fξk+1(δ). Unfolding the recursion gives
ck =ζ k−K(δ) cK(δ)
| {z }
Term I (transient)
+LF fζ k
kX
j=K(δ)+1
p
j+ log(1/δ)r j 1| {z }
Term II (estimation error)
+LF fζ k
kX
j=K(δ)+1
r j 2|{z}
Term III (exploration noise)
.
Term I: sinceK(δ) =O(log log(1/δ)) andζ <1,ζ −K(δ) ≤(log(1/δ)) c0 for somec 0 >0, hence
Term I =O

(log(1/δ))c0 ζ k .
Term II: write
p
j+ log(1/δ)≤
p
k+ log(1/δ) for allj≤k. Ifr 1 <1 the series P j r j 1 converges,
giving Term II =O(
p
k+ log(1/δ)ζ k); ifr 1 = 1 then Term II =O(k p k+ log(1/δ)ζ k); ifr 1 >1 the
last term dominates and Term II =O(
p
k+ log(1/δ)λ
−( 1 2 −max m {νm})k ). In all cases the dependence
onδis at mostO(
p
log(1/δ)).
Term III: this term does not involveδ. Ifr 2 <1 it isO(ζ k); ifr 2 = 1 it isO(kζ k); ifr 2 >1 it is
O(λ
−min
m
{νm}k ).
Sincea k ≤c k by induction,a k enjoys the same bounds. Consequentlya k →0 with probability
at least 1−δ, and fork≥K(δ) and each playerm,
µ∥F (k) m −F ∗ m∥+∥f (k) m −f ∗ m∥2 ≤a k.(45)
Step 2.We now translate the rates to calendar timet. By Condition 1, we haveτ (k) ≤τ (k) m ≤
τ (k) + ¯τ. Summing over epochs gives constants 0< c≤C <∞such thatcλ k ≤¯τ(k) m ≤Cλ k and
km(t) = logλ t+O(1) for allmand all largek. ChooseT(δ) so thatk m(t)≥K(δ) for allt≥T(δ)
and everym; the threshold satisfiesT(δ) =O

(log(1/δ))c1

for somec 1 >0.
By (45), fort≥T(δ),
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 ≤Mmax 1≤m≤M {akm(t)}.
Substituting the three bounds from Step 1 and converting epoch indices to time viaζkm(t) ≍t lnζ/lnλ ,
λ
−( 1 2 −max m {νm})km(t) ≍t −( 1 2 −max m {νm}) ,λ −min m {νm}km(t) ≍t −min m {νm} , we obtain
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 =O  max{R1(t, δ), R2(t, δ), R3(t)}  ,
whereR 1, R2, R3 are defined in (20).
Step 3.The estimates in Steps 1-2 are derived under the conditional probabilityP(· | T) and
show that for anyδ∈(0,1) there existsT(δ) such that the claimed bounds hold for allt≥T(δ)
withP(· | T)-probability at least 1−δ. To lift this to an unconditional statement, observe that
all constants appearing in the bounds depend only on model parameters and the parameters in
33

Condition 1, hence are uniform over all realizations of the shifts. The thresholds in the auxiliary
lemmas are chosen by making certain tail probabilities smaller than a prescribed fraction ofδ;
because the tail conditions involve only the deterministic lower boundτ (k) ≤τ (k) m , the resulting
thresholds work simultaneously for all realizations ofT. Taking expectation overTyields the same
bounds under the unconditional probabilityP.
Step 4 (Almost-sure convergence with rate).From Steps 1-3, for anyδ∈(0,1) there exist
constantsC <∞andT(δ)∈Nsuch that, with probability at least 1−δ, for allt≥T(δ),
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 ≤Cmax{R 1(t, δ), R2(t, δ), R3(t)},(46)
whereR 1, R2, R3 are defined in Step 2.
For eachj∈Nsetδ j = 2 −j and letE j be the event on which the bound in (46) holds with
δ=δ j for allt≥T(δ j). By constructionP(E j)≥1−2 −j. Since P∞ j=1 P(E c j )≤ P∞ j=1 2−j <∞, the
Borel–Cantelli lemma implies thatP
T∞
J=1
S∞
j=J E c j  = 0. Equivalently, lettingE= S∞ J=1 T∞ j=J Ej,
we haveP(E) = 1. On the almost-sure eventE, there exists a (random) indexj 0 such thatE j occurs
for everyj≥j 0.
Setq= min
n
− lnζ lnλ , 1 2 −max m {νm},min m {νm} o >0.Now observe that, for any fixedj,
tq
(logt)
3
2 log logt
max{R1(t, δj), R2(t, δj), R3(t)} →0 ast→ ∞.
Consequently, on the almost-sure eventE, for anyε >0 we can first choosejlarge enough so that
j≥j 0 and then choosetlarge enough so that the right-hand side of (46) multiplied by tq
(logt)
3
2 log logt
is smaller thanε. Hence
lim
t→∞
tq
(logt)
3
2 log logt
∥(F (k(t)), f(k(t)))−(F ∗, f∗)∥µ,1,2 = 0 almost surely.
This shows that the strategy profile converges almost surely to the feedback Nash equilibrium
(F ∗, f∗) at the rateO  t−q(logt) 3 2 log logt  .
A.4 Proofs of Auxiliary Lemmas in Appendix A.1
A.4.1 Proof of Lemma 2
We first recall a purely algebraic estimate that will be used repeatedly.
Lemma 8.LetHbe ad×dsymmetric positive semidefinite matrix. Suppose there exist matrices
Γ1 ∈R d×p andΓ 2 ∈R d×q withp+q=dsuch that[Γ 1 Γ2]∈R d×d is invertible and
[Γ1 Γ2]⊤H[Γ 1 Γ2] =
 H0 0p×q
0q×p H1

,
whereH 0 = Γ⊤ 1 HΓ 1 ∈R p×p andH 1 = Γ⊤ 2 HΓ 2 ∈R q×q are symmetric positive definite. Then
σmin(H)≥ σmin(H0)∧σ min(H1) 4  ∥Γ1∥2 ∨ ∥Γ2∥2 .
Proof.Proof For any nonzeroy∈R d, writey= Γ 1u+ Γ 2vuniquely withu∈R p andv∈R q.
Theny ⊤Hy=u ⊤H0u+v ⊤H1v≥σ min(H0)∥u∥2 2 +σ min(H1)∥v∥2 2, while∥y∥ 2 2 =∥Γ 1u+ Γ 2v∥2 2 ≤
4(∥Γ1∥2 ∨ ∥Γ2∥2)(∥u∥2 2 ∨ ∥v∥2 2). If∥u∥ 2 2 ≥ ∥v∥2 2, theny ⊤Hy/∥y∥ 2 2 ≥σ min(H0)/[4(∥Γ1∥2 ∨ ∥Γ2∥2)];
the other case is analogous. Taking the infimum overy̸= 0 gives the result.
34

Upper bound on∥V (k) m ∥and the determinant.From the definitionz m t = [1, x⊤ t ,(u m t )⊤]⊤ and
the feedbacku m t =−F (k−1) m xt +f (k−1) m +α (k−1) m vm t , we have
∥zm t ∥2 2 ≤C  1 +∥x t∥2 2 +∥v m t ∥2 2  .(47)
For the exploration noise, since{v m t }are i.i.d. sub-Gaussian, Bernstein’s inequality implies that
for everyk≥K v2,m =O(log log(1/δ)), it holds for some eventE v2,k withP(E v2,k)≥1−δ k/40 that P¯τ(k) m −1
t=¯τ(k−1) m ∥vm t ∥2 2 ≤2d mτ (k) m .
For the state, we rewrite (35) as
xt+1 =A 0 t +A cl t xt + ˜wt,(48)
whereA 0 t =A 0+PM m=1 Bmf (km(t)) m ,A cl t =A− PM m=1 BmF (km(t)) m , and ˜wt =ω t+PM m=1 Bmα(km(t)) m vm t .
Assumption 3 implies∥A cl t ∥ ≤1−γand∥A 0 t ∥2 ≤ CA,0 uniformly. Since the state process{x t}∞ t=0
is driven by sub-Gaussian innovations and the dynamics are uniformly stable, it is uniformly sub-
Gaussian; hence∥x t∥2 2 is uniformly sub-exponential for allt. By Young’s inequality,∥x t+1∥2 2 ≤
(1− γ 2 )∥xt∥2 2 +C A +C w∥˜wt∥2 2. Iterating and summing overt= ¯τ (k−1) m , . . . ,¯τ(k) m −1 gives
¯τ(k) m −1X
t=¯τ(k−1) m
∥xt∥2 2 ≤ 2∥x¯τ(k−1) m ∥2 2 γ + 2CAτ (k) m γ + 2Cw γ ¯τ(k) m −2X
j=¯τ(k−1) m
bj,k ∥˜wj∥2 2,
where 0≤b j,k = 1−(1−γ) ¯τ(k) m −1−j ≤1. The variable∥x ¯τ(k−1) m ∥2 2 is uniformly sub-exponential
and independent of the future noises{˜w j}j≥¯τ(k−1) m ; moreover,{∥˜wj∥2 2}is an independent sequence
of uniformly sub-exponential random variables. Hence, Bernstein’s inequality for weighted sums
yields
P


¯τ(k) m −1X
t=¯τ(k−1) m
∥xt∥2 2 > Cxτ (k) m

 ≤exp  −Cτ (k) m  .(49)
Hence, for everyk≥K x2,m =O(log log(1/δ)), it holds for some eventE x2,k withP(E x2,k)≥
1−δ k/40 that P¯τ(k) m −1 t=¯τ(k−1) m ∥xt∥2 2 ≤C xτ (k) m .SetE z,k =E v2,k ∩E x2,k; thenP(E z,k)≥1−δ k/20. For
allk≥K z,m = max{Kv2,m, Kx2,m}, onE z,k, by (47), we have
∥V (k) m ∥ ≤βm +
¯τ(k) m −1X
t=¯τ(k−1) m
∥zm t ∥2 2 ≤ CV τ (k) m ,det(V (k) m )≤ ∥V(k) m ∥1+n+dm ≤  CV τ (k) m 1+n+dm .
Lower bound onσ min(V (k) m ).During the whole epochkplayermuses the fixed feedback
(F (k−1) m , f(k−1) m ), therefore the regression vector can be written as
zm t =G m,k ¯xt +α (k−1) m Jmvm t ,¯x t =  1x t ⊤ ,
whereG m,k =


1 0 1×n
0n×1 In
f (k−1) m −F (k−1) m

 andJ m =
0(1+n)×dm
Idm

.Both∥G m,k∥and∥J m∥are bounded by
1 +κ m +κ ′ m. Inserting this into the definition ofV (k) m and normalising byτ (k) m (α(k−1) m )2 yields
V (k) m
τ (k) m (α(k−1) m )2 =(α(k−1) m )−2Gm,kXkG⊤ m,k +J mWkJ ⊤ m
+ (α(k−1) m )−1 Gm,kCkJ ⊤ m +J mC⊤ k G⊤ m,k  + βmI τ (k) m (α(k−1) m )2 ,(50)
35

with the empirical matrices
Xk = 1
τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
¯xt ¯x⊤ t , W k = 1 τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
vm t (vm t )⊤, C k = 1 τ (k) m
¯τ(k) m −1X
t=¯τ(k−1) m
¯xt(vm t )⊤.
We will bound each of these three blocks on a suitable high-probability event.
Step 1: State covarianceX k.Set ˆµ k = 1 τ (k) m P¯τ(k) m −1 t=¯τ(k−1) m xt and ˆΓk = 1 τ (k) m P¯τ(k) m −1 t=¯τ(k−1) m (xt −ˆµk)(xt −
ˆµk)⊤.The augmented covariance decomposes as
Xk =
 1 ˆµ ⊤ k
ˆµk ˆΓk + ˆµk ˆµ⊤ k

.(51)
Thus it suffices to lower-boundσ min(ˆΓk) and to upper-bound∥ˆµk∥2.
Recall (48), the matricesA 0 t , Acl t areF t-measurable, whereF t denotes the information available
at timetbefore the noisesω t,{v j t }1≤j≤M are drawn; by Assumption 3 they satisfy∥A cl t ∥ ≤1−γ
uniformly. The effective noise ˜wt is independent ofF t, conditionally sub-Gaussian, and its covariance
matrix is uniformly bounded below by Σ ω ≻0.
For any fixed directionq∈S n−1 the scalar processd t =q ⊤(xt+1 −x t) can be written as
dt =q ⊤(A0 t + (Acl t −I)x t) +q ⊤ ˜wt. The first term isF t-measurable, while the second is a con-
ditionally centred sub-Gaussian random variable whose conditional variance satisfiesE[(q ⊤ ˜wt)2 |
Ft]≥σ min(Σω)>0. By a standard Paley–Zygmund argument (Proposition 3.1 of Simchowitz et al.
(2018)), this implies that the process{d t}satisfies the (1, ν, p)-block martingale small-ball condition
of Simchowitz et al. (2018) with constantsν, p >0 that depend only on the sub-Gaussian norm of
˜wt and onσ min(Σω).
Applying Proposition 2.5 of Simchowitz et al. (2018) to{d t}¯τ(k) m −2 t=¯τ(k−1) m and using a net argument
(Corollary 4.2.11 of Vershynin (2018)) shows that for everyk≥K Γ,m =O(log log(1/δ)), it holds
for some eventE Γ,k withP(E Γ,k)≥1−δ k/20 that
σmin

 1
τ (k) m
¯τ(k) m −2X
t=¯τ(k−1) m
(xt+1 −x t)(xt+1 −x t)⊤

 ≥C Γ >0.
Now for anyq∈S n−1 seta t =q ⊤(xt −ˆµk); thenq ⊤(xt+1 −x t) =a t+1 −a t and (a t+1 −
at)2 ≤2a 2 t+1 + 2a2 t . Summing this inequality fromt= ¯τ (k−1) m to ¯τ(k) m −2 and using that eacha t
appears at most twice gives P¯τ(k) m −1
t=¯τ(k−1) m (q⊤(xt −ˆµk))2 ≥ 1 4 P¯τ(k) m −2 t=¯τ(k−1) m (at+1 −a t)2.Hence onE Γ,k,
σmin(ˆΓk)≥ CΓ 4 >0.
Now we derive the uniform bound for∥ˆµk∥2. Similar to the argument leading to (49), for every
k≥K µ,m =O(log log(1/δ)), it holds for some eventE µ,k withP(E µ,k)≥1−δ k/20 that∥ˆµk∥2 ≤C µ.
Now apply Lemma 8 to the matrix in (51) with Γ 1 =
 1
−ˆµk

and Γ 2 =
01×n
In

.On the event
E0,k :=E Γ,k ∩E µ,k, we obtain
σmin(Xk)≥C ¯x>0,
whereC ¯xdepends only onC Γ andC µ.
Step 2: Exploration covarianceW k.The vectors{v m t }¯τ(k) m −1 t=¯τ(k−1) m are i.i.d. sub-Gaussian with co-
variance matrixI dm. Stack them into anτ (k) m ×d m matrix and apply Theorem 4.6.1 of Vershynin
(2018). For anys >0, with probability at least 1−2e −s2 ,
 1 τ (k) m ¯τ(k) m −1X t=¯τ(k−1) m vm t (vm t )⊤ −I dm  ≤C  s dm +s 2 τ (k) m + dm +s 2 τ (k) m ! .
36

Chooses=
p
log(40/δk) and supposeτ (k) m ≥C(d m + log(1/δk)), so that the right-hand side is
at most 1/2. Hence, for everyk≥K W,m =O(log log(1/δ)), it holds for some eventE W,k with
P(EW,k)≥1−δ k/20 that
1
2 Idm ⪯W k ⪯ 3 2 Idm.
Step 3: Assembly.Consider the leading block
fMk = (α(k−1) m )−2Gm,kXkG⊤ m,k +J mWkJ ⊤ m.
On the eventE 0,k ∩E W,k we haveσ min(Xk)≥C ¯xandσ min(Wk)≥1/2. Using Lemma 8 with
Γ1 =
I1+n
0

and Γ2 =
h
−f (k−1) m F (k−1) m Idm
i⊤
,a short calculation gives
σmin( fMk)≥C fM := (C ¯x/¯α2)∧(1/2) 8(1 +κ m +κ ′m)2 >0.
It remains to control the cross term and the regularisation in (50). On the eventE z,k, we have
∥V (k) m ∥ ≤CV τ (k) m log(τ (k) m /δk), det(V (k) m )≤( CV τ (k) m log(τ (k) m /δk))1+n+dm. Similar to the argument
leading to (37) in Lemma 5, for everyk≥K 3,m =O(log log(1/δ)), it holds for some eventE 3,k with
P(E3,k)≥1−δ k/20 that onE 3,k ∩E z,k,
(α(k−1) m )−1 Gm,kCkJ ⊤ m +J mC⊤ k G⊤ m,k  + βmI τ (k) m (α(k−1) m )2  ≤C  k2 + log2(1/δ)  q τ (k) m α(k−1) m .
Sinceτ (k) m ≍λ k andα (k−1) m ≍λ −νmk withν m < 1 2 , the denominatorτ (k) m (α(k−1) m )2 ≍λ (1−2νm)k
grows exponentially with exponent 1 2 −ν m >0, while the numerator contains only polynomial terms
inkand log(1/δ). Hence there existsK 3,m =O(log log(1/δ)) such that for allk≥K 3,m ≥K z,m
the right-hand side is at mostC fM /4, which completes the control of the perturbation term.
Conclusion.Define the eventE V,k =E z,k ∩EΓ,k ∩Eµ,k ∩EW,k ∩E3,k.By the union boundP(E V,k )≥
1−δk/4. OnE V,k , for allkexceeding the maximumK V,m := max{Kz,m, KΓ,m, Kµ,m, KW,m, K3,m}=
O(log log(1/δ)), we have
σmin(V (k) m )≥C V τ (k) m (α(k−1) m )2
withC V =C fM /2. Together with the upper bound obtained at the beginning, this completes the
proof of Lemma 2.
A.4.2 Proof of Lemma 3
We first give a formal description of the asynchronous tail. For each epochk≥1 define the
synchronous phase
S(k) = [τ (k),¯τ(k)], τ (k) = max
1≤j≤M
¯τ(k−1) j ,¯τ(k) = min 1≤j≤M ¯τ(k) j −1.
DuringS (k) every player employs the policy obtained after her (k−1)-st update, so that the effective
parameter Θ∗ m,t equals the constant Θ (k),∗ m throughoutS (k). The complementary set
T (k) m = [¯τ(k−1) m ,¯τ(k) m −1]\S (k)
is called the asynchronous tail; by Condition 1 its length satisfies|T (k) m | ≤Cτ kfor all largek. On
T (k) m we only have the deterministic bound∥Θ∗ m,t−Θ(k),∗ m ∥ ≤CΘ, which follows from the compactness
of the admissible strategy setsA m,B m.
37

Now we construct the required event. As established in the proof of Lemma 2, the state pro-
cess{x t}∞ t=0 is uniformly sub-Gaussian, which implies that the regression vectors{z m t }∞ t=0 are also
uniformly sub-Gaussian. It is obvious from its definition that{˜w m t }∞ t=1 is a uniformly sub-Gaussian
sequence. Applying the standard sub-Gaussian maximal inequality over the interval [¯τ(k−1) m ,¯τ(k) m −1]
shows that for everyk≥K A,m =O(log log(1/δ)), it holds for some eventsE A1,k, EA2,k with
P(EA1,k)≥1−δ k/8 andP(E A2,k)≥1−δ k/8 that
max
¯τ(k−1) m ≤t≤¯τ(k) m −1 ∥zm t ∥2 ≤C z
q
log(τ (k) m /δk),max
¯τ(k−1) m ≤t≤¯τ(k) m −1 ∥˜wm t ∥2 ≤C w
q
log(τ (k) m /δk).
SetE A,k =E A1,k ∩E A2,k; thenP(E A,k)≥1−δ k/4. On this event we bound the two quantities
appearing in the lemma.
For the first term, using that the summand is non-zero only onT (k) m and that|T (k) m | ≤Cτ k,
 ¯τ(k) m −1X t=¯τ(k−1) m zm t (zm t )⊤(Θ∗ m,t −Θ (k),∗ m )⊤  ≤ X t∈T (k) m ∥zm t ∥2 2 ∥Θ∗ m,t −Θ (k),∗ m ∥ ≤C klog(τ(k) m /δk).
For the second term,
 ¯τ(k) m −1X t=¯τ(k−1) m (Θ∗ m,t −Θ (k),∗ m )⊤zm t ( ˜wm t )⊤  ≤ X t∈T (k) m ∥Θ∗ m,t −Θ (k),∗ m ∥ ∥zm t ∥2 ∥˜wm t ∥2 ≤C klog(τ (k) m /δk).
Sinceklog(τ (k) m /δk) =k  O(k) + log(1/δ) + 2 log(k+ 1)  ≤C  k2 + log(1/δ)  , both quantities are
bounded byC(k 2 + log(1/δ)) onE A,k, as required.
A.4.3 Proof of Lemma 4
We treat the synchronous phaseS (k) and the asynchronous tailT (k) m separately. Recall that|T (k) m | ≤
Cτ kand|S (k)| ≥τ(k) m −C τ k.
We first deal with the synchronous phaseS (k). OnS (k) all players use fixed strategies, hence
the effective noise vectors ˜w m t are i.i.d. with zero mean and covariance matrix Σ (k),∗ m . Lety t =
(Σ(k),∗ m )−1/2 ˜wm t fort∈S (k). Then{y t}t∈S(k) are i.i.d. sub-Gaussian withE[y t] = 0 andE[y ty⊤ t ] =I n.
Applying Theorem 4.6.1 of Vershynin (2018) exactly as in Step 2 of the proof of Lemma 2 shows
that for everyk≥K c1,m =O(log log(1/δ)), it holds for some eventE c1,k withP(E c1,k)≥1−δ k/8
that  1 |S(k)| X t∈S(k) yty⊤ t −I n  ≤C s n+ log(1/δ k) |S(k)| .
Multiplying by (Σ (k),∗ m )1/2 on both sides, using∥Σ (k),∗ m ∥ ≤Cand|S (k)| ≍τ(k) m , we obtain
 1 τ (k) m X t∈S(k)  ˜wm t ( ˜wm t )⊤ −Σ (k),∗ m   ≤C s n+ log(1/δ k) τ (k) m .
For the asynchronous tailT (k) m , we use the sub-Gaussian maximal inequality as in the proof of
Lemma 3. This shows that for everyk≥K c2,m =O(log log(1/δ)), it holds for some eventE c2,k
withP(E c2,k)≥1−δ k/8 that
max
¯τ(k−1) m ≤t≤¯τ(k) m −1 ∥˜wm t ∥2 2 ≤Clog(τ (k) m /δk).
38

OnE c2,k,  1 τ (k) m X t∈T (k) m  ˜wm t ( ˜wm t )⊤ −Σ (k),∗ m   ≤ |T (k) m | τ (k) m  max ¯τ(k−1) m ≤t≤¯τ(k) m −1 ∥˜wm t ∥2 2 +C  ≤C klog(τ (k) m /δk) τ (k) m .
Now setE cov,k =E c1,k ∩E c2,k andK cov,m = max{K c1,m, Kc2,m}=O(log log(1/δ)). Then
P(Ecov,k)≥1−δ k/4 and for allk≥K cov,m, onE cov,k,
 1 τ (k) m ¯τ(k) m −1X t=¯τ(k−1) m  ˜wm t ( ˜wm t )⊤ −Σ (k),∗ m   ≤C s n+ log(1/δ k) τ (k) m +C klog(τ (k) m /δk) τ (k) m .
Sinceτ (k) m ≍λ k andν m < 1 2 , both terms on the right-hand side are of smaller order thanη (k) m (δ)
in (28). Hence, after possibly increasingK cov,m by an absolute constant, the total error is bounded
byCη (k) m (δ) for allk≥K cov,m.
B Algorithm Implementation and Sufficient Conditions in Section
5
This section provides the implementation details of Algorithm 1 for the dynamic Cournot compe-
tition model, followed by the theoretical analysis that establishes sufficient conditions for Assump-
tions 1, 2, and 4. Appendix B.1 derives a directly verifiable characterization of the feasible setS m
and a practical method for computing the greedy strategy (Algorithm 2). Appendix B.2 identify
conditions under which the optimal strategy of (21) is unique, independent of the initial price, and
Lipschitz continuous with respect to the perceived parameters. Using these conditions together with
the equivalence relationship (32), Appendix B.3 establishes a set of sufficient conditions that guar-
antee Assumptions 1, 2, and 4. The proofs of the lemmas in Appendices B.1 and B.3 are collected
in Appendix B.4. In the first two subsections, we focus on a representative firmmand consider its
problem (21) under a perceived parameter pair (Θ m = [(1−s ′)a′, s′,−(1−s ′)b′]⊤,Σ m =σ 2 m).
B.1 Algorithm Implementation
To derive an implementable way to check feasibility and calculate the greedy strategy in Algorithm 1,
we first derive an explicit representation of the cost function (21) under the perceived model (3).
For a given linear strategy (F m, fm, αm) with (F m, fm)∈ Am × Bm andα m ≥0, the price process
implied by (3) becomes
pt+1 =

s′ + (1−s ′)b′Fm  pt + (1−s ′)a′ −(1−s ′)b′fm −(1−s ′)b′αmvm t +ω ′ t,(52)
with initial pricep 0 =p. The exploration noise{v m t }∞ t=0 and the perceived market noise{ω ′ t}∞ t=0
are mutually independent i.i.d. sub-Gaussian sequences with mean zero and variances 1 andσ 2 m,
respectively. Substituting (52) into the cost function (21) yields
J Θm,Σm m  (Fm, fm);p, αm  = ∞X
t=0
ρt

Qm(Fm)E[p2 t ] +R m(Fm, fm)E[pt] +O m(Fm, fm)  ,(53)
where{p t}evolves according to (52), and
Qm(Fm) = ( 1 2 + (1−s ′)b′)F 2 m +s ′Fm,
Rm(Fm, fm) =−(1 + 2(1−s ′)b′)Fmfm −s ′fm + ((1−s ′)a′ −c m)Fm,
Om(Fm, fm) = ( 1 2 + (1−s ′)b′)f 2 m + (cm −(1−s ′)a′)fm + (1 2 + (1−s ′)b′)α2 m.
The expressions (53) provide the foundation for a directly verifiable characterization of the feasible
setS m in (8) and a practical greedy strategy calculation method developed below.
39

B.1.1 Explicit Characterization ofS m
We first provide a more explicit characterization of the feasible parameter setS m defined in (8) for
playerm.
For allF m ∈ Am, writeA m cl (Fm) =s ′ + (1−s ′)b′Fm. This quantity characterizes the asymptotic
stationarity and growth rate of{p t}: if|A m cl (Fm)|<1, the process is asymptotically stationary;
otherwise,|E[p t]|andE[p 2 t ] grow exponentially at the rates|A m cl (Fm)|t and (A m cl (Fm))2t, respec-
tively. The cost (53) can be−∞(i.e., infinite profit) if and only if either (i)Q m(Fm)<0 and√ρ|A m cl (Fm)| ≥1, or (ii)Q m(Fm) = 0 and P∞ t=0 ρtRm(Fm, fm)E[pt] =−∞. To exclude these
pathological cases, we define the following set ˆSm
ˆSm =
(
(Θm,Σ m) :∀F m ∈ Am,
ifQ m(Fm)<0 then|A m cl (Fm)|< 1√ρ ,
ifQ m(Fm) = 0 then|A m cl (Fm)|< 1 ρ .
)
.(54)
The conditions in (54) rule out any possibility of unbounded negative cost. The following lemma,
whose proof can be found in Appendix B.4, establishes that this auxiliary set coincides with the
feasible setS m required by Algorithm 1.
Lemma 9.For the dynamic Cournot competition model, the feasible setS m defined in(8)is
identical to the set ˆSm given by(54).
BecauseQ m(Fm) andA m cl (Fm) are respectively quadratic and linear functions ofF m, checking
the conditions in (54) is straightforward. When implementing Algorithm 1 (line 8), we decide
whether to accept an estimate candidate or fall back by verifying these conditions.
B.1.2 Greedy Strategy Calculation
This subsection describes how to compute the greedy strategy in (13) for Step 9 of Algorithm 1.
Directly searching over the grid (F m, fm)∈ Am × Bm to solve (13) is computationally costly. To
circumvent this issue, we exploit the problem structure, specifically the cost function (53), to develop
a more efficient solution.
At thek-th update epoch, for a given accepted parameter set ( ˜Θ(k) m , ˜Σ(k) m )∈ ˆSm, an admissible
strategy (F m, fm)∈ Am × Bm yields either a finite cost or an infinite positive cost. To determine
when the cost is finite, we use the following lemma, which follows by applying the standard LQ
formulas (or, equivalently, solving the Bellman equation) to the linear perceived dynamics (52) with
the quadratic cost structure (53).
Lemma 10.For any given(Θ m,Σ m)∈ ˆSm,p >0, andα m ≥0, the cost(53)is finite if and only
if one of the following holds:
1. √ρ|A m cl (Fm)|<1;
2.ρ|A m cl (Fm)|<1andQ m(Fm) = 0;
3.Q m(Fm) = 0andR m(Fm, fm) = 0.
In the first two cases, for a fixedF m the cost is a quadratic function off m.
Thus, to minimize (21), firmmsearches over strategies satisfying the conditions of Lemma 10
(otherwise the cost would be infinite). BecauseA m is one-dimensional, we first perform a grid
search overF m ∈ Am. For a fixedF m, when the first two conditions of the lemma hold, the optimal
fm can be found analytically: sinceB m = [−κ′ m, κ′ m] is a closed interval and the cost is quadratic
inf m, the minimizer is either the unconstrained quadratic minimizer clipped to the interval, or
one of the endpoints. In the third condition, the values off m that satisfyR m(Fm, fm) = 0 are
directly computable becauseR m is linear inf m. This procedure yields an efficient greedy strategy
computation method, summarized in Algorithm 2. For other types of LQ games, particularly
multi-dimensional ones, we provide Algorithm 3 for greedy strategy calculation in Appendix C.
40

Algorithm 2Cournot Competition: Greedy Strategy Calculation for Firmmat Time ¯τ (k) m
1:Require:Accepted parameter pair ( ˜Θ(k) m , ˜Σ(k) m ), exploration noise scaleα (k) m , initial pricep ¯τ(k) m
2:Initialize candidate setC=∅
3:foreachF m ∈ Am do
4:if √ρ|A m cl (Fm)|<1 or (ρ|A m cl (Fm)|<1 andQ m(Fm) = 0)then
5:Computef min = arg min fm∈Bm J
˜Θ(k) m , ˜Σ(k) m
m

(Fm, fm);p ¯τ(k) m , α(k) m 
6:EvaluateJ min =J
˜Θ(k) m , ˜Σ(k) m
m

(Fm, fmin);p ¯τ(k) m , α(k) m 
7:Add (F m, fmin, Jmin) toC
8:end if
9:ifQ m(Fm) = 0then
10:foreachf m ∈ Bm such thatR m(Fm, fm) = 0do
11:ComputeJ=J
˜Θ(k) m , ˜Σ(k) m
m

(Fm, fm);p ¯τ(k) m , α(k) m 
12:Add (F m, fm, J) toC
13:end for
14:end if
15:end for
16:Select the triple (F ∗ m, f∗ m, J∗) inCwith the smallest costJ ∗
17:return(F ∗ m, f∗ m)
B.2 An explicit characterization of the optimal strategy of(53)
In this section, we study the setting in which the optimal strategy of the problem (53) over the ad-
missible setA m×Bm coincides with that of the corresponding unconstrained problem (the minimizer
of (53) overR×R). When this coincidence occurs, the optimal strategy overA m × Bm is unique
and admits a closed-form solution that is independent of the initial pricepand Lipschitz continuous
with respect to the parameters (Θ m,Σ m, αm). Leveraging the equivalence relationship (32), these
favorable properties allow us to establish Assumptions 1, 2, and 4 under some sufficient conditions
in Appendix B.3. The following lemma provides an explicit characterization of the optimal strategy
for the unconstrained problem and states when it also solves the constrained problem.
Lemma 11.If
(1−s ′)b′ >0, √ρ|s′|<1,(55)
then for anyp∈R,α m ≥0, the following hold.
(1) The unconstrained probleminf
(Fm,fm)∈R×R
J Θm,Σm m ((Fm, fm);p, αm)has a finite optimal value, and
the unique minimizer is given by
F Θm m = −s′(2ρP Θm m (1−s ′)b′ + 1) 1 + 2(1−s ′)b′ + 2ρP Θm m ((1−s ′)b′)2 ,(56)
f Θm m = (1−ρs ′)((1−s ′)a′ −c m) + 2ρPΘm m (1−s ′)b′(1−s ′)a′  1 + 2(1−s ′)b′ + 2ρP Θm m ((1−s ′)b′)2 (1−ρ(s ′ + (1−s ′)b′F Θm m )) ,(57)
where
P Θm m =
ρ
2 (s′)2 −( 1 2 + (1−s ′)b′) +
q
( 1 2 + (1−s ′)b′)− ρ 2 (s′)22 −ρ((1−s ′)b′)2(s′)2
2ρ((1−s ′)b′)2 .(58)
(2) If additionally(F Θm m , fΘm m )∈ Am×Bm, then this pair is also the unique minimizer of the problem
(53)overA m × Bm. In particular, the optimal value is finite, so(Θ m,Σ m)∈ Sm.
41

Proof.Proof We proceed in three steps.
Step 1: Riccati equation and closed-loop stability .Consider the Riccati equation
h(Pm) = 4ρ((1−s ′)b′)2P 2 m + 4  ( 1 2 + (1−s ′)b′)− ρ 2 (s′)2 Pm + (s′)2 = 0.(59)
Under condition (55), the discriminant of the quadratic (59) satisfies ∆>0, and evaluatingh(P m) at
Pm = 0 and atP m =−
1
2 +(1−s′)b′
ρ((1−s′)b′)2 showsh(P m)>0 at both endpoints. Hence Vieta’s formulas yield
two negative roots−
1
2 +(1−s′)b′
ρ((1−s′)b′)2 < P(2) m < P(1) m <0. SettingX (i) = 1 + 2(1−s′)b′ + 2ρP(i) m ((1−s ′)b′)2
and substituting the relation into (59) to obtain the quadratic equation satisfied byX (i), Vieta’s
formulas giveX (1)X (2) =ρ(s ′(1 + (1−s ′)b′))2, henceX (1) > √ρ|s′(1 + (1−s ′)b′)|> X (2) >0.
ThereforeP m in (58) (i.e.P (1) m ) is the unique root satisfying the required closed-loop stability
condition √ρ|s′ + (1−s ′)b′F Θm m |<1.
Step 2: Identifying the minimizer.We distinguish two cases according toF m.
First, by the characterization (53), for anyFm outside the interval

−
s′+ 1√ρ
(1−s′)b′ ,
1√ρ −s′
(1−s′)b′

,we have
Qm(Fm)>0, henceJ Θm,Σm m ((Fm, fm);p, αm) =∞for allf m. Such strategies cannot be optimal.
Second, restrict attention toF m in this interval and admissiblef m. To identify the optimal
strategy, introduce the auxiliary controlled dynamics
pt+1 = (1−s ′)a′ +s ′pt −(1−s ′)b′ ˜qm t −(1−s ′)b′αmvm t +ω ′ t (60)
for{˜qm t }t≥0 ∈ UΘm m , where
U Θm m =
(
˜qm t , t≥0

 ˜qm t isF t-measurable,E " ∞X t=0 ρt(p2 t + (˜qm t )2) # <∞ ) .
For anyF m in this interval and any admissiblef m, the sequence{˜qm t }t≥0 given by ˜qm t =−F mpt +f m
lies inU Θm m , and (60) coincides with (52) under this{˜q m t }t≥0. Standard dynamic programming
applied to the auxiliary problem
inf
(˜qm t )t≥0∈U Θmm
E
" ∞X
t=0
ρt  1 2 ˜qm t −p t+1 +c m  ˜qm t
#
,
subject to (60), shows that the unique minimizer is the linear feedback strategy ˜q m,∗ t =−F Θm m pt +
f Θm m .
Combining the two cases, (F Θm m , fΘm m ) is the unique minimizer ofJ Θm,Σm m ((Fm, fm);p, αm) over
R×R, completing the proof of part (1).
Step 3: Constrained optimality .Finally, if (F Θm m , fΘm m )∈ Am × Bm, then it is admissible for
the constrained problem. Since it is the unique minimizer over the larger unconstrained domain, it
must also be the unique minimizer over the subsetA m × Bm.
B.3 Sufficient Conditions for Assumptions 1, 2, and 4
In this section, we provide directly verifiable sufficient conditions under which Assumptions 1,
2, and 4 hold for the Cournot competition model. We state two main conditions. Condition 2
ensures that each player’s best response is well-defined, thereby establishing Assumption 1 and
guaranteeing the existence of a feedback Nash equilibrium; through a perturbation analysis, it also
implies Assumption 4. Building on Condition 2, Condition 3 additionally guarantees the stability
42

of this equilibrium, i.e., Assumption 2. Together, the two conditions imply all three required
assumptions. To facilitate the statement of the conditions, we first introduce the following constants:
CA,m :=s−(1−s)b
X
j̸=m
κj, CA,m :=s+ (1−s)b
X
j̸=m
κj,(61)
CG := 1 2 + (1−s)b−ρ((1−s)b) 2CP ,(62)
CP :=
1
2 (1−ρ C
2
A,m) + (1−s)b−
q 1
2 (1−ρ C
2
A,m) + (1−s)b
2 −ρ((1−s)b) 2C 2 A,m
2ρ((1−s)b) 2 ,(63)
Cf,m :=

(1−ρC A,m)∨(2ρ(1−s)b CP +ρ CA,m −1)

(1−s)(a+b P
j̸=m
κ′ j) + (1−ρC A,m)cm
2CG −ρ CA,m(1 + (1−s)b) .
(64)
With these constants in place, we state the first condition.
Condition 2.For all1≤m≤M, the following hold:
1) √ρCA,m <1,
2) CA,m
1 + 2(1−s)b−2ρ((1−s)b) 2CP < κm,
3)C f,m < κ′ m.
Part 1) of Condition 2 ensures that for each player, condition (55) holds under any admissible
strategy profile of others, so that the unconstrained problem is well-posed and the unconstrained
optimum exists. Parts 2) and 3) then guarantees this unconstrained optimal strategy falls strictly
inside the admissible setsA m × Bm. Consequently, Condition 2 implies Assumption 1, as stated in
Lemma 12; the same lemma also establishes the existence of a feedback Nash equilibrium, charac-
terized by the system therein. Its proof is deferred to Appendix B.4. For notational convenience,
for any admissible strategy profile (F −m, f−m) of the other players, define
A(F−m) =s+ (1−s)b X
j̸=m
Fj, A (f−m) 0 = (1−s)a−(1−s)b X
j̸=m
fj.
Lemma 12.Under Condition 2, the following hold:
1) Assumption 1 holds with(ψ m(F−m, f−m), φm(F−m, f−m))given explicitly in(75)for all1≤
m≤Mand(F −m, f−m)∈ A−m × B−m.
2) There exists a feedback Nash equilibrium, characterized by the solution to the coupled system



Fm =− A(F−m)(2ρPm(1−s)b+ 1) 2( 1 2 + (1−s)b) + 2ρP m((1−s)b) 2 ,
fm = (1−ρA (F−m))(A(f−m) 0 −c m) + 2ρPm(1−s)bA (f−m) 0
2

( 1 2 + (1−s)b) +ρP m((1−s)b) 2 1−ρ(A (F−m) + (1−s)bF m)  ,
Pm =
ρ
2 (A(F−m))2 −( 1 2 + (1−s)b) +
q
( 1 2 + (1−s)b)− ρ 2 (A(F−m))22 −ρ((1−s)b) 2(A(F−m))2
2ρ((1−s)b) 2 ,
(65)
for1≤m≤M.
Via a perturbation argument, Condition 2 also establishes Assumption 4, as stated in Lemma 13
below; its proof is deferred to Appendix B.4.
43

Lemma 13.Under Condition 2, Assumption 4 holds.
To find a condition that guarantees the stability of the equilibrium characterized in Lemma 12,
we introduce the following constants:
LP,m :=

|A(F ∗ −m)|+ CA,m  (1 + 2ρCP )
2 + 4(1−s)b−2ρ

A(F ∗ −m)2 + 4ρ((1−s)b) 2 P ∗m − CP  ,(66)
LF,m = |A(F ∗ −m)|ρ(1−s)b(1 + (1−s)b)L P,m
2CG

 1
2 + (1−s)b+ρP ∗m((1−s)b) 2

 + 1 2CG ,(67)
Lf,m :=

1−ρA (F ∗ −m) + 2ρP ∗ m(1−s)b

2

 1
2 + (1−s)b+ρP ∗m((1−s)b) 2

1−ρ  A(F ∗ −m) + (1−s)bF ∗m 

 .(68)
With these constants in place, we state the contraction condition.
Condition 3.Let(F ∗, f∗,{P ∗ m}1≤m≤M )be a solution of(65). For all1≤m≤M, assume
1)4
 1
2 + (1−s)b

−2ρ

A(F ∗ −m)2 + 4ρ((1−s)b) 2 P ∗ m − CP  >0,
2)(1−s)b P
j̸=m
LF,j <1,
3)(1−s)b P
j̸=m
Lf,j <1,
where CP ,L F,m, andL f,m are given by(63),(67), and(68), respectively.
Condition 3 is expressed solely in terms of the model parameters and the equilibrium quantities
themselves. Part 1) ensures a non-degenerate denominator in the Lipschitz estimates, while parts 2)
and 3) impose that the cumulative influence of other players through their feedback gains and offsets
remains contracting. Lemma 14 below formalizes this implication, giving the stability coefficient
ζexplicitly; we omit the explicit expression forµ, which does not affect the convergence rate, for
brevity. Its proof is deferred to Appendix B.4.
Lemma 14.Under Conditions 2 and 3, there exists a constantµ >0(depending on the model
parameters) such that Assumption 2 holds withζgiven by
ζ= max



1
2 + 1 2 max 1≤j≤M n (1−s)b X m̸=j LF,m o ,max 1≤j≤M n (1−s)b X m̸=j Lf,m o


 .(69)
B.4 Proofs of Auxiliary Lemmas in Appendix B
B.4.1 Proof of Lemma 9
Proof.Proof We prove the two inclusions separately.
Part 1: ˆSm ⊆ Sm.Take any (Θ m,Σ m)∈ ˆSm. For allpandα m ≥0, the cost at (0,0) is finite,
so the infimum is<∞. For any admissible (F m, fm), the moments satisfyE[p t]≍(A m cl (Fm))t and
E[p2 t ]≍(A m cl (Fm))2t. Consequently, in (53), the term withQ m(Fm) converges ifQ m(Fm) = 0 or
ρ(Am cl )2 <1; the term withR m(Fm, fm) converges ifR m(Fm, fm) = 0 orρ|A m cl |<1.
Now we examine each sign ofQ m(Fm). IfQ m(Fm)≤0, the definition of ˆSm ensures that the
cost is finite. IfQ m(Fm)>0, then when √ρ|Am cl |<1 the cost is finite; otherwise it diverges to +∞
because the positiveQ m-term dominates. Thus the cost is never−∞. Lower semicontinuity on the
compact setA m × Bm implies the infimum is attained and finite. Therefore (Θ m,Σ m)∈ Sm.
Part 2:S m ⊆ ˆSm.We prove the contrapositive. Suppose (Θ m,Σ m)/∈ ˆSm. Then there exists
Fm ∈ Am violating the condition.
44

1)Q m(Fm)<0 but √ρ|Am cl | ≥1: then P t ρtQm(Fm)E[p2 t ] diverges to−∞, so the infimum is
−∞.
2)Q m(Fm) = 0 butρ|A m cl | ≥1: choose an admissiblefm withR m(Fm, fm)̸= 0 (possible because
Rm is affine inf m); then the linear term diverges to−∞for a suitable initial pricep, making
the infimum−∞.
In either case (Θ m,Σ m)/∈ Sm. HenceS m ⊆ ˆSm.
Both inclusions yieldS m = ˆSm.
B.4.2 Proof of Lemma 12
Proof.Proof We first prove part 1). For each player, under any admissible strategy profile of others,
condition (55) holds, so that Lemma 11 applies, and the unconstrained optimum exists. We then
track how bounds propagate along the chain (58)→(56)→(57), showing at each step that the output
remains strictly inside the admissible set. Part 2) then follows from Brouwer’s fixed-point theorem,
using the continuity of the best-response map established in part 1).
We take playermas a representative player. For any admissible strategy profile (F −m, f−m)
of the other players, let Θ (F−m,f−m) m = [A (f−m) 0 , A(F−m),−(1−s)b] ⊤ as in (18). By replacing
(F (k−1) −m , f(k−1) −m ) in (32) with an arbitrary (F−m, f−m)∈ A−m×B−m (and Θ(k),∗ m with the correspond-
ing Θ (F−m,f−m) m ), the minimizer of the complete-information problemJ m((Fm, fm); (F−m, f−m), p)
coincides with that of the control problem (53) with the perceived parameter pair (Θ (F−m,f−m) m ,Σ ω).
Thus, it suffices to analyze the latter, which is the focus of the rest of this subsection. By definition,
CA,m ≤A (F−m) ≤ CA,m, so Part 1) of Condition 2 gives
√ρ|A(F−m)|<1,(1−s)b >0,(70)
which means condition (55) holds. Lemma 11 therefore applies and (F Θ
(F−m,f−m)
m
m , fΘ
(F−m,f−m)
m
m )
attains the minimum overR×R.
Step 1: Bound onP m.Since|A (F−m)| ≤CA,m, one verifies by rationalizing the numerator of (58)
that the expression is monotone increasing in|A (F−m)|. HenceP Θ
(F−m,f−m)
m
m is negative and bounded
below by CP in (63). WithC G as defined in (62), we obtain
−CP ≤P Θ
(F−m,f−m)
m
m <0, 1 2 + (1−s)b+ρP Θ (F−m,f−m) m m ((1−s)b) 2 ≥C G >0.(71)
Step 2: Bound onF m.Since 0>2ρP Θ
(F−m,f−m)
m
m (1−s)b≥ −2ρ(1−s)b CP >−1, from (56) we
obtain the estimate

F Θ (F−m,f−m) m m

 < CA,m 2CG . Part 2) of Condition 2 then yields
−κm < FΘ
(F−m,f−m)
m
m < κm.(72)
Step 3: Bound onf m.Using (56), we have
A(F−m) + (1−s)bF Θ
(F−m,f−m)
m
m = A(F−m)(1 + (1−s)b)
2

( 1 2 + (1−s)b) +ρP Θ
(F−m,f−m)
m
m ((1−s)b) 2 .
Together with|A (F−m)| ≤CA,m and (71), the denominator of (57) satisfies
2

( 1 2 +(1−s)b)+ρP Θ (F−m ,f−m ) m m ((1−s)b) 2 (1−ρ(A (F−m) +(1−s)bF Θ (F−m ,f−m ) m m ))≥2C G −ρC A,m(1+(1−s)b),
(73)
45

where the positivity of the lower bound follows directly from the definitions of CP andC G. Com-
bining this with the bounds onA (f−m) 0 ,|A (f−m) 0 | ≤(1−s)(a+b P
j̸=m
κ′ j), and (71), we obtain from
(57) the estimate|f Θ
(F−m,f−m)
m
m | ≤Cf,m, whereC f,m is given by (64). Part 3) of Condition 2 then
guarantees
−κ′ m < fΘ(F−m,f−m) m < κ′ m.(74)
By part (2) of Lemma 11, the pair (F Θ
(F−m,f−m)
m
m , fΘ
(F−m,f−m)
m
m ) is the unique minimizer, indepen-
dent of the initial pricep, and continuous in (F −m, f−m), so Assumption 1 holds with
ψm(F−m, f−m) =F Θ
(F−m,f−m)
m
m , φ m(F−m, f−m) =f Θ
(F−m,f−m)
m
m .(75)
The continuity of Ψ follows from (75) and the continuity of the closed-form expressions in the
parameters (F−m, f−m). SinceA × Bis compact, Brouwer’s fixed-point theorem guarantees a fixed
point (F ∗, f∗) of Ψ, which by definition satisfies the coupled system (65). Lemma 1 then implies
that (F ∗, f∗) is a feedback Nash equilibrium. This proves part 2). The proof is complete.
B.4.3 Proof of Lemma 13
Proof.Proof Fix any (F −m, f−m)∈ A−m × B−m and let Θ (F−m,f−m) m be as defined in (18).
Part 1.Lemma 12 shows that Θ (F−m,f−m) m satisfies the conditions of Lemma 11 with strict inequal-
ities (see (70), (72), (74)). Since these inequalities involve only the components of Θ (F−m,f−m) m and
are strict, and since the bounds used in the estimates are uniform over the compact setA −m × B−m,
there existsδ m >0 independent of (F −m, f−m) such that for any ˜Θm with∥ ˜Θm −Θ (F−m,f−m) m ∥ ≤δm,
the same strict inequalities hold. Consequently, Lemma 11(2) applies and yields ( ˜Θm, ˜Σm)∈ Sm
for any ˜Σm with∥ ˜Σm −Σ ω∥ ≤δm. This establishes part 1) of Assumption 4.
Part 2.The explicit formulas (56)-(57) are smooth functions of the components of Θ (F−m,f−m) m
over the compact parameter range induced byA −m × B−m. The uniform lower bounds (71)
and (73) ensure that the denominators in these formulas stay bounded away from zero uniformly
over (F−m, f−m). By continuity and compactness, there exists a constantL m <∞such that for all
(F−m, f−m)∈ A−m × B−m and all ( ˜Θm, ˜Σm, αm) with max{∥ ˜Θm −Θ (F−m,f−m) m ∥,∥ ˜Σm −Σ ω∥, αm} ≤
δm,the Lipschitz bounds required by part 2) of Assumption 4 hold. The independence of the
minimizer from the initial statexfollows from Lemma 11(2).
B.4.4 Proof of Lemma 14
Proof.Proof By Lemma 12, (F ∗, f∗) is a fixed point of Ψ. We consider any ( ˆF ,ˆf)∈ A × Band let
(F, f) = Ψ((ˆF ,ˆf)). Under Condition 2, Lemma 12 provides the explicit formulas (75) for (F m, fm).
Step 1: Lipschitz estimate forP m.Applying a differencing argument to formula (58) and using
the uniform bound|P m| ≤CP from (71), we obtain|P m −P ∗ m| ≤LP,m|A( ˆF−m) −A (F ∗ −m)|, where
LP,m is defined in (66) and its denominator is positive by Part 1) of Condition 3.
Step 2: Lipschitz estimate forF m.Applying a differencing argument to formula (56) and
substituting the bound from Step 1 and the uniform lower bound on the denominator from (71), we
obtain|F m −F ∗ m| ≤LF,m|A( ˆF−m) −A (F ∗ −m)|, whereL F,m is given by (67). Since|A ( ˆF−m) −A (F ∗ −m)|=
(1−s)b P
j̸=m
| ˆFj −F ∗ j |, summing overmand rearranging yields
MX
m=1
|Fm −F ∗ m| ≤max 1≤j≤M
n
(1−s)b
X
m̸=j
LF,m
o MX
j=1
| ˆFj −F ∗ j |.
46

Step 3: Lipschitz estimate forf m.Applying a differencing argument to formula (57) and
substituting the bounds from Steps 1-2 together with (73), we obtain|f m −f ∗ m| ≤Lf,m|A( ˆf−m) 0 −
A
(f ∗ −m)
0 |+L f F,m|A( ˆF−m) −A (F ∗ −m)|, whereL f,m is given by (68) andL f F,m <∞depends only
on the model parameters and the bounds already established. Summing overmand rearranging
analogously to Step 2 then gives
MX
m=1
|fm −f ∗ m| ≤max 1≤j≤M
n
(1−s)b
X
m̸=j
Lf F,m
o MX
j=1
| ˆFj −F ∗ j |+ max 1≤j≤M
n
(1−s)b
X
m̸=j
Lf,m
o MX
j=1
| ˆfj −f ∗ j |.
Step 4.Letζbe defined as in (69), and chooseµ=
2 max
1≤j≤M

(1−s)b P
m̸=j
Lf F,m

1−max
1≤j≤M

(1−s)b P
m̸=j
LF,m
	 . Substituting the
estimates from Steps 2-3 into the definition of∥ · ∥µ,1,2 in Assumption 2, a direct calculation yields
Ψ(( ˆF ,ˆf)−Ψ((F ∗, f∗))  µ,1,2 ≤ζ ( ˆF ,ˆf)−(F ∗, f∗)  µ,1,2.
Parts 2) and 3) of Condition 3 ensure thatζ <1, so Assumption 2 is satisfied.
C A Numerical Example with Multiple Equilibria
In this section, we consider a linear-quadratic games with no cross term (H m = 0) andQ m ≻0,
which allow for multi-dimensional state and action spaces. This setting is standard in the LQ game
literature (Hambly et al., 2023; Mazumdar et al., 2020). We first describe the implementation of
Algorithm 1 in this setting, and then present a numerical example with two distinct Nash equilibria,
for which the learning dynamics may converge to different equilibria or oscillate across runs.
C.1 Algorithm Implementation
We first analyze the unconstrained control problem and characterize its solution. Using this result,
we then provide a verifiable characterization of the feasible setS m and describe a practical method
for computing the greedy strategy. Throughout this subsection, playermserves as the representative
agent, and we denote its parameter estimate by (Θ m,Σ m). For convenience, we partition Θ m as
Θm = [A′ 0, A′, B′ m]⊤, whereA ′ 0 ∈R n×1 is the coefficient vector for the constant term,A ′ ∈R n×n
for the statex t, andB ′ m ∈R n×dm for playerm’s controlu m t in the perceived dynamics (6).
C.1.1 The Unconstrained Optimal Strategy
We begin by studying the LQ control problem without the compact constraintsA m × Bm. The
following lemma can be derived using standard results from linear quadratic control theory (see,
e.g., Hager and Horowitz (1976)).
Lemma 15.Assume that the pair( √ρA′, √ρB′ m)is stabilizable and that( √ρA′, Qm)is detectable
(e.g.,Q m ≻0guarantees detectability). Then the following hold.
1) For every initial statex∈R n and exploration scaleα m ≥0, the infimum
inf
(Fm,fm)∈Rdm×n×Rdm
J Θm,Σm m  (Fm, fm);x, αm 
is finite and uniquely attained at the pair(F Θm m , fΘm m )given by
F Θm m =ρ  Rm +ρB ′⊤ m P Θm m B′ m −1 B′⊤ m P Θm m A′,(76)
f Θm m =  Rm +ρB ′⊤ m P Θm m B′ m −1 ρB′⊤ m  I−ρ(A ′ −B ′ mF Θm m )⊤−1 1 2 ((F Θm m )⊤rm −q m)−P Θm m A′ 0  − rm 2  ,
(77)
47

whereP Θm m is the unique positive semidefinite solution of the following equation
P Θm m =Q m +ρA ′⊤P Θm m A′ −ρ 2A′⊤P Θm m B′ m  Rm +ρB ′⊤ m P Θm m B′ m −1B′⊤ m P Θm m A′.
2) If in addition(F Θm m , fΘm m )∈ Am×Bm, then this pair is the unique minimizer of the constrained
problem(7)for everyxandα m.
C.1.2 Characterization of the F easible SetS m
For LQ games withH m = 0 andQ m ≻0, the feasible setS m defined in (8) admits a spectral char-
acterization stated in Lemma 16. We omit its proof, which follows by applying (Horn and Johnson,
2012, Theorem 5.6.12) to the dynamics under linear feedback, together with the observation that
the positive definiteness ofQ m rules out unbounded negative cost.
Lemma 16.For LQ games withH m = 0andQ m ≻0, the feasible setS m defined in(8)coincides
with
˜Sm =  (Θm,Σ m) :∃F m ∈ Am such thatr( √ρ(A′ −B ′ mFm))<1 	 .(78)
Note that ˜Sm imposes no restriction on Σ m because the well-posedness of problem (7) is de-
termined solely by the drift parameters. When implementing Algorithm 1, we decide whether to
accept a given (Θ m,Σ m) or fall back by checking whether it lies in ˜Sm; specifically, this requires
determining if there exists anF m ∈ Am such thatr( √ρ(A′ −B ′ mFm))<1. For low-dimensional
problems, a simple grid search overA m can be used. In general, we treat the problem as a feasibility
optimization: minimizer( √ρ(A′ −B ′ mFm)) subject toF m ∈ Am; if the minimal value is less than 1,
then (Θm,Σ m) is feasible. This is a non-convex constrained problem. A Sequential Quadratic Pro-
gramming (SQP) solver (or its variants adapted to non-smooth objectives) with multiple random
initializations (Boggs and Tolle, 1995; Nocedal and Wright, 2006) can be employed. This numer-
ical verification is practical for moderate dimensions. In the next subsection, we assume that the
accepted parameter set already lies in ˜Sm and focus on computing the greedy strategy.
C.1.3 Greedy Strategy Calculation
We now provide a practical method for computing the greedy strategy in Algorithm 1. For any
accepted parameter set (˜Θ(k) m , ˜Σ(k) m )∈ ˜Sm, the unconstrained optimum is well defined (Lemma 15). If
this unconstrained optimum lies inside the admissible setA m × Bm, it is optimal for the constrained
problem (7). Otherwise, we must solve a constrained optimization problem. Because the problem is
generally non-convex in (Fm, fm) (Fazel et al., 2018), we adopt the SQP approach described above,
combined with a multi-start heuristic to mitigate the risk of converging to a poor local minimum.
The cost function for the SQP solver is given by the standard LQ representation. The following
algorithm summarizes the procedure.
C.2 Numerical Example with Multiple Equilibria
This section presents a numerical experiment illustrating the behavior of Algorithm 1 in a two-player
LQ game with at least two distinct complete-information Nash equilibria. Gaussian noise is used
for both the state and exploration noises throughout. The system parameters areA= 1.0700,
B1 = 0.10254,B 2 = 0.085934,A 0 = 0, Σ ω = 0.1 2,Q 1 = 0.11112,R 1 = 0.30872,Q 2 = 0.25806,
R2 = 0.4949, andH m =q m =r m = 0 form= 1,2. The discount factor isρ= 0.9999, and
the admissible bounds areκ m = 2.0 andκ ′ m = 1.0 form= 1,2. The algorithm parameters are
τ= 300,λ= 1.1,τ = 2000, ¯τ= 200,ν= 0.25, andβ m = 0.01 for each player. At each update, the
asynchronous shift for each player is sampled independently from a uniform distribution on [0,¯τ].
The total number of time steps isT≈2.8×10 8, ensuring that every player completes 120 updates
per run. We find two feedback Nash equilibria:
48

Algorithm 3LQ Game without Cross Terms: Greedy Strategy Calculation for Playerm
1:Require:Accepted parameter set ( ˜Θ(k) m , ˜Σ(k) m ), exploration noise scaleα (k) m , initial statex ¯τ(k) m
2:Compute the unconstrained optimal strategy (F ˜Θ(k) m m , f˜Θ(k) m m ) via (76)-(77).
3:if(F ˜Θ(k) m m , f˜Θ(k) m m )∈ Am × Bm then
4:return(F ˜Θ(k) m m , f˜Θ(k) m m ).
5:else
6:GenerateN start random initial points uniformly inA m × Bm.
7:fori= 1 toN start do
8:Run an SQP solver from thei-th initial point for a local minimizer (F (i) m , f(i) m ) and its cost
J (i).
9:end for
10:Return the pair with the smallest cost: (F ∗ m, f∗ m) = arg mini J (i).
11:end if
•Equilibrium 1:F 1 = 0.8908, f1 = 0.0000, F2 = 0.4980, f2 = 0.0000. The spectral radius of
DΨ at this equilibrium is 0.9709.
•Equilibrium 2:F 1 = 0.3718, f1 = 0.0000, F2 = 1.1423, f2 = 0.0000. The spectral radius of
DΨ at this equilibrium is 0.9203.
Both equilibria are locally stable, but the existence of multiple fixed points violates Assump-
tion 2. Additionally, Assumption 3 is violated since|A|>1.
We run 100 independent simulations of Algorithm 1, where each simulation independently selects
an initial guess uniformly at random from the admissible strategy setsA m × Bm. Outcomes are
classified into four categories following the same criteria as in Section 5.4: explode (the state grows
without bound, or the algorithm diverges), oscillatory (persistent fluctuations without settling),
converge to Equilibrium 1, and converge to Equilibrium 2. Table 4 summarizes the results.
Table 4: Distribution of experimental outcomes for the multiple-equilibria example
Explode (%) Oscillatory (%) Converge to Equilibrium 1 (%) Converge to Equilibrium 2 (%)
35.00 36.00 5.00 24.00
Because Assumption 3 is violated, some simulations explode, causing the algorithm to fail. In
the remaining runs, we observe three types of behavior: convergence to Equilibrium 1, convergence
to Equilibrium 2, or persistent best-response cycles. This phenomenon is consistent with the syn-
chronous Riccati iteration results reported in Nortmann et al. (2024) (see Figure 3(c) there). Unlike
the deterministic best-response iteration studied there, Algorithm 1 is subject to estimation errors
and exploration noises; hence there is no sharp deterministic partition of the region of initial guesses
that determines convergence to a specific equilibrium. However, because both equilibria are locally
stable, each possesses a neighborhood such that once the algorithm stays within that neighborhood,
it tends to converge to the corresponding equilibrium. This explains why the behavior in this ex-
ample differs from that of Section 5.4 (Group 2), where all simulations exhibited oscillations and
none converged, whereas here some simulations do converge to equilibria.
49
