---
title: 'EvoNash-MARL: A Closed-Loop Multi-Agent Reinforcement Learning Framework for Medium-Horizon Equity
  Allocation'
url: https://arxiv.org/abs/2604.10911
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Chongliu Jia
- Yi Luo
- Sipeng Han
- Pengwei Li
- Jie Ding
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.10911
pages: 10
chars: 45561
fetched_at: '2026-11-08T13:07:44+00:00'
kb_version: 1
---

# EvoNash-MARL: A Closed-Loop Multi-Agent Reinforcement Learning Framework for Medium-Horizon Equity Allocation

1
EvoNash-MARL: A Closed-Loop Multi-Agent
Reinforcement Learning Framework for
Medium-Horizon Equity Allocation
Chongliu Jia, Yi Luo 1, Sipeng Han 2, Pengwei Li 1,
Jie Ding 4, Youshuang Hu 1, Yimiao Qian 3, and Qiya Wang 1
Chongliu Jia, chongliujia@gmail.com
1University of Connecticut, yi.luo@uconn.edu, parkwest.lee@gmail.com, youshuang.hu@uconn.edu, bll24001@uconn.edu
2Xi’an University of Technology, 1211913010@stu.xaut.edu.cn
3Fudan University, 24210740058@m.fudan.edu.cn
4Iowa State University, jieding@iastate.edu
Abstract—Medium- to long-horizon equity allocation is chal-
lenging due to weak predictive structure, non-stationary market
regimes, and the degradation of signals under realistic trading
constraints. Conventional approaches often rely on single predic-
tors or loosely coupled pipelines, which limit robustness under
distributional shift.
This paper proposes EvoNash-MARL, a closed-loop frame-
work that integrates reinforcement learning with population-
based policy optimization and execution-aware selection to im-
prove robustness in medium- to long-horizon allocation. The
framework combines multi-agent policy populations, game-
theoretic aggregation, and constraint-aware validation within a
unified walk-forward design.
Under a 120-window walk-forward protocol, the final configu-
ration achieves the highest robust score among internal baselines.
On out-of-sample data from 2014 to 2024, it delivers a 19.6%
annualized return, compared to 11.7% for SPY, and remains
stable under extended evaluation through 2026.
While the framework demonstrates consistent performance
under realistic constraints and across market settings, strong
global statistical significance is not established under white’s
Reality Check (WRC) and SPA-lite tests. The results therefore
provide evidence of improved robustness rather than definitive
proof of superior market timing performance.
Index Terms—reinforcement learning, game theory, multi-
agent systems, portfolio allocation, walk-forward evaluation, non-
stationary markets
I. INTRODUCTION
Medium- and long-horizon equity allocation remains a
difficult sequential decision problem. Unlike short-horizon
signal extraction, where evaluation is often concentrated on
immediate directional accuracy, a deployable allocation system
must remain stable across market regimes, changing factor
relations, and repeated portfolio re-estimation cycles. The
difficulty is amplified by the low signal-to-noise ratio of
daily equity returns: predictive structure is weak relative to
realized volatility, and a signal that appears useful before
trading may become unattractive once transaction costs, ca-
pacity limits, beta drift, drawdown exposure, and tail-risk
constraints are considered. These frictions are not peripheral
details in medium-horizon allocation; they directly determine
whether a learned policy can be used outside a backtest. This
concern is consistent with the broader financial ML literature,
which emphasizes validation discipline, data snooping control,
and the gap between backtest performance and deployable
strategies [1]–[4].
A large body of work has studied portfolio construction
and financial decision-making from different angles. Classical
portfolio selection begins with mean-variance analysis [5],
while reinforcement learning has been used to optimize trading
and execution objectives directly [6], [7]. With deep reinforce-
ment learning, financial applications have expanded toward
automated trading, multi-asset allocation, portfolio rebalanc-
ing, market-condition-aware control, and alpha discovery [8]–
[12]. These studies show that sequential learning is a natural
formulation for financial allocation. At the same time, they
also highlight persistent limitations: many systems optimize
a single policy, rely on static train-test separation, or treat
execution constraints and statistical validation as downstream
checks rather than as part of the training and selection loop.
This mismatch is important. In financial applications, a
policy is not useful simply because it predicts returns or
improves a raw Sharpe ratio in one evaluation slice. It must
also survive regime variation, avoid unstable exposure, re-
spect feasibility constraints, and remain interpretable enough
to diagnose when the learned behavior fails. Single-agent
RL is attractive because it can optimize sequential utility,
but it can be brittle under noisy rewards, sparse effective
feedback, and distribution shift. A static ensemble can reduce
variance, but it does not by itself provide a mechanism for
strategic replacement or best-response adaptation. Population-
based and game-theoretic RL methods provide a related set of
tools for maintaining strategic diversity and updating policy
mixtures [13]–[18]. Likewise, constrained and multi-objective
RL provide useful foundations for reasoning about reward,
risk, feasibility, and model mismatch [19], [20]. However,
a purely game-theoretic policy pool is incomplete if the
resulting mixture is selected without considering transaction
costs, benchmark-relative risk, and tail constraints.
These observations motivate the central question of this pa-
arXiv:2604.10911v2  [cs.AI]  14 Apr 2026

2
per: can medium/long-horizon allocation be improved by treat-
ing prediction, policy aggregation, evolution, and execution-
aware selection as one closed loop rather than as separate
modules? The question is non-trivial because the components
can pull in different directions. PSRO-style aggregation favors
a stable mixture over policy populations; walk-forward vali-
dation favors checkpoints that generalize across time; league
best-response training encourages adaptation to the current
mixture; and execution-aware scaling may suppress high-
conviction signals when they become too costly or risky to
express. A useful system must coordinate these forces rather
than simply stacking them.
We propose EvoNash-MARL, a medium/long-horizon pre-
dictive allocation framework that couples multi-agent policy
populations, PSRO-style meta-strategy updates, league best-
response training, population evolution, and execution-aware
checkpoint selection. The deployable object is not a single
predictor. It is an adaptive population of policy candidates
whose signals are aggregated, stress-tested, and selected under
the same walk-forward protocol used for final evaluation.
The policy design separates directional information from
risk control through a direction head and a risk head. The
signal layer further applies factor neutralization, nonlinear
signal amplification, feature-quality weighting, and regime-
aware handling. The execution layer incorporates transaction
cost, impact, capacity, beta exposure, downside risk, and tail
constraints before a checkpoint is accepted.
The contribution is deliberately narrower than a new generic
RL algorithm. We do not introduce a new equilibrium solver
or a new statistical test. Instead, the paper studies how
an allocation system behaves when RL-based policy search,
game-theoretic aggregation, evolutionary replacement, and
feasibility-aware selection are coupled inside a fixed medium-
horizon walk-forward design. This positioning matters because
financial overfitting often occurs not only in the prediction
model, but also in the choice of checkpoints, baselines, and
evaluation windows. Accordingly, our empirical claims are
stated with care: strong return levels are not interpreted as
directly deployable alpha, and statistical tests are used to
separate economic evidence from global significance claims.
Empirically, the resolved v21 configuration ranks first by
robust score in the 120-window protocol. Over 2014-01-02 to
2024-01-05 OOS, its annualized return is 19.6% versus 11.7%
for SPY , and in an extended walk-forward check through
2026-02-10 it is 20.5% versus 13.5%. The same evidence
also shows the limits of the current study: global signifi-
cance under WRC/SPA-lite is not established, DQN baselines
underperform in this medium-horizon setup, and transfer is
stronger against HYG/TLT than against QQQ. We therefore
interpret the results as conditional evidence that the closed-
loop training-and-selection design improves robustness under
the stated protocol, not as proof of a universally dominant
trading rule.
II. RELATEDWORK
Portfolio selection and financial reinforcement learning.
Portfolio selection has long been studied through the risk-
return trade-off formalized by mean-variance analysis [5].
Reinforcement learning later introduced a direct sequential-
control view of trading, including risk-adjusted utility op-
timization and execution-oriented decision-making [6], [7].
With the development of deep RL, financial applications
expanded from single-instrument trading toward automated
stock trading, portfolio rebalancing, multi-asset allocation,
and alpha discovery. FinRL provides a practical deep-RL
library for automated stock trading, while FinRL-Meta further
emphasizes market environments, data processing, transaction
costs, and benchmarking for financial RL [8], [9]. AlphaStock
combines an interpretable attention mechanism with a Sharpe-
oriented RL objective for winner-loser portfolio selection [10].
DeepTrader incorporates market-condition embeddings to im-
prove risk-return balancing in portfolio management [11].
More recently, AlphaQCM frames alpha discovery as a non-
stationary and reward-sparse sequential decision problem and
applies distributional RL to search for synergistic formulaic
alphas [12].
These studies are directly relevant because they show that
financial allocation is more naturally treated as a sequential
control problem than as a pure supervised prediction task.
However, most existing financial RL systems emphasize one
primary component at a time: a trading agent, a market
environment, a reward function, or a predictive representa-
tion. They less often study a closed loop in which policy
populations, strategic aggregation, evolutionary replacement,
execution constraints, and walk-forward checkpoint selection
are optimized together. Our work focuses on this integration
problem rather than on replacing these prior financial RL
models.
Multi-agent learning, game solving, and population adap-
tation.Multi-agent reinforcement learning provides a way
to reduce dependence on a single learned policy by main-
taining multiple interacting strategies [13]. From a game-
theoretic perspective, Nash equilibrium provides a classical
steady-state concept [21], while PSRO expands a policy pool
through iterative best-response computation and meta-strategy
updates [14]. Population Based Training shows how model
parameters and hyper-parameters can be adapted jointly during
training rather than fixed in advance [15]. More recent work
has refined the theoretical motivation for such population-
based designs. Robust MARL studies equilibrium learning
when the deployed environment may differ from the training
model [16]. Self-play theory has begun to characterize the
cost of policy adaptation when updates are constrained [17].
Recent PSRO extensions further emphasize that equilibrium
selection matters, not merely equilibrium approximation [18].
Survey work on self-play also highlights the practical impor-
tance of population diversity, curriculum effects, and opponent
selection in RL systems [22].
These ideas are useful for non-stationary markets be-
cause different strategies can become effective under different
regimes. A static ensemble can average model outputs, but
it does not necessarily provide a principled mechanism for
replacement, best-response injection, or strategic reweighting.
EvoNash-MARL therefore uses PSRO-style aggregation and
league best-response training as a way to maintain a policy

3
population whose members can be reweighted or replaced as
validation evidence changes. The goal is not to model the
market as a literal two-player game, but to use game-solving
machinery as a disciplined population-management tool inside
a financial allocation pipeline.
Constraints, model mismatch, and statistical validation.
Financial deployment differs from many simulated RL bench-
marks because the training environment is only an approx-
imation of future market conditions. Recent constrained RL
work shows that a policy satisfying constraints during training
can violate them after deployment when model mismatch
exists [19]. Robust MARL makes a related point in multi-
agent settings: environmental uncertainty can alter which
equilibrium behavior is admissible or desirable [16]. Multi-
objective RL also provides a useful lens because trading poli-
cies must balance return, risk, stability, and feasibility rather
than maximize a single scalar reward without safeguards [20].
Statistical validation is equally important. Financial ML
research has repeatedly warned that raw return or Sharpe
ratios can be misleading when multiple models, windows, or
hyper-parameters are explored [1]. We therefore use Newey-
West tests [23], stationary bootstrap [24], White Reality
Check [3], SPA [4], and Deflated Sharpe Ratio [2]. This
evaluation protocol is intentionally conservative. The reported
OOS returns are treated as conditional evidence under a fixed
walk-forward design, while the lack of strong WRC/SPA-lite
significance is reported as a limitation rather than hidden.
Relative to prior work, the distinguishing feature of EvoNash-
MARL is therefore not a single new component, but the
coupling of population-based RL, game-theoretic aggregation,
execution-aware utility, and statistical validation within one
medium/long-horizon allocation pipeline.
III. METHOD
A. Problem Formulation
We consider daily panel data with universe sizeNand
horizon lengthT. Let
ri,t = Pi,t Pi,t−1 −1(1)
be asset return,b t be benchmark return (default SPY),x t ∈
Rd be features,z t ∈ {BULL,BEAR,SIDEW AYS,SHOCK}
be market regime, ands t ∈[−s max, smax]be position signal
(long-only:[s min, smax]).
The optimization target is risk-constrained excess perfor-
mance: Letπdenote a candidate allocation policy. The opti-
mization target is
max
π
ExcessSharpe(π)−λ tailTailRisk(π)−λ stabInstability(π).
(2)
B. Architecture Overview
The allocation system is organized around three interacting
objects: a policy population, a meta-strategy over that popula-
tion, and a validation/execution selector. The policy population
contains heterogeneous agents with different inductive biases,
so the system does not rely on one model to represent
Fig. 1. EvoNash-MARL allocation loop. Policy populations are aggregated
through a PSRO-style meta-strategy, updated through league/evolution steps,
and selected through execution-aware validation.
all regimes. The meta-strategy assigns mixture weights to
these agents through a PSRO-style update. The selector then
evaluates the resulting signal under benchmark-relative utility,
execution penalties, and validation-window stability.
This organization is motivated by the failure modes of
medium-horizon trading. A single policy can become fragile
when the market regime changes; a static ensemble can
average signals but cannot replace weak members; and an
unconstrained trading objective can prefer checkpoints that
look profitable before costs but become unattractive after
beta, drawdown, or capacity constraints are applied. EvoNash-
MARL addresses these issues by keeping policy aggregation,
league replacement, evolution, and execution-aware selection
inside the same training loop. Recent self-play, PSRO, robust
MARL, and multi-objective RL results support the use of
population-level adaptation and explicit objective trade-offs,
although our implementation is an applied allocation system
rather than a direct instantiation of those theoretical mod-
els [16], [18], [20], [22].
C. Feature and Regime Modeling
Features include market momentum/volatility, cross-
sectional breadth/dispersion, tail and higher-moment
descriptors, benchmark-relative features, and LS factor
streams. Regimes are identified by
BULL: ¯rt ≥θ bull,BEAR: ¯r t ≤θ bear,(3)
SHOCK:σ t > κshock ¯σt,SIDEW AYS:otherwise.(4)
D. Policy Parameterization and Risk Head
For agentk, base score is
ak,t =w ⊤ k xt +b k +c k,zt ,(5)
with regime biasc k,zt. Base signal:
˜sk,t = tanh
 ak,t
max(0.15, τk)

.(6)
If risk-head is enabled:
uk,t =σ

(w(r) k )⊤xt +b (r) k +c (r) k,zt

,(7)
ℓk,t =ℓ min k + (ℓmax k −ℓ min k )uk,t,(8)
sk,t = sign(˜sk,t)|˜sk,t|ℓk,t.(9)

4
E. Trading PnL with Execution Constraints
Letp t be executed position,u t =|p t −p t−1|be turnover.
Daily PnL is
πt =p t−1rt −c tcut −λ risk|pt−1|σt
−λ impu2 t −λ cap|pt−1|2(1 +σ t), (10)
wherec tc =bps/10000. We further apply rebalance schedul-
ing, smoothing, vol-targeting, and tail deleveraging overlays.
F . Game Layer: PSRO Meta Strategy
For policy set{1, . . . , K}, payoff matrix:
Aij = ¯πi −¯πj.(11)
Meta strategym∈∆ K is updated by multiplicative weights:
v(τ) =Am (τ) , m (τ+1) k ∝m (τ) k exp(ηv (τ) k ).(12)
Nash gap:
NashGap= max
i
(Am)i −m ⊤Am.(13)
Ensemble signal:
sens t =
KX
k=1
mksk,t.(14)
G. Utility, Fitness, and Evolution
Strategy utility:
Uk =SR(π k) +λ exSR(πk −b)
−λ downDownDev(πk)−λ dd|MDD(πk)|
−λ cvar|min(0,CVaR α(πk −b))|
−λ worst|min(0,min t (πk,t −b t))|
−λ con ·Violation k.
(15)
Constraint violation:
Violationk = max(0, c⋆ cvar −CVaR α(πk −b))
+ max(0, c⋆ worst −min t (πk,t −b t)). (16)
Fitness:
Fk = (Am)k +U k +λ divDk
+λ leagueLk −λ β|βk −β ⋆|, (17)
Dk = 1− 1 K−1 X j̸=k |Corr(s k, sj)|.(18)
The resulting objective is intentionally multi-criteria. Rather
than maximizing return alone, the system trades off
benchmark-relative reward, downside stability, constraint satis-
faction, diversity, and exposure control. This is consistent with
recent multi-objective RL viewpoints in which the quality of a
policy is not reducible to a single unconstrained reward chan-
nel [20]. In our setting, this matters because a strategy with
slightly lower raw return but materially better feasibility and
inter-window stability is often preferable for medium/long-
horizon deployment.
H. League Self-Play and Best Response
Opponent aggregate signal:
sopp t = X
k
mksk,t.(19)
Ridge BR usesh-day forward return:
R(h) t =
hY
u=1
(1 +r t+u)−1,(20)
yBR t = clip  sign(R(h) t )−s opp t  ,(21)
then ridge fitting and parameter blending.
RL-hybrid BR uses Q-learning with state(x t,pos t, sopp t )
(optionally with RFF expansion), and discrete
position/leverage actions. Reward without risk-head:
rt =π t +ω h

ptR(h) t −Π opp t:t+h

−π opp t+1 −λ pos|pt|. (22)
Q-update:
Q(st, at)←Q(s t, at)
+η
h
rt +γmax a′ Q(st+1, a′)−Q(s t, at) i . (23)
I. Nonlinear Signal and Feature Quality Modules
Factor neutralization:
ˆβ= (F ⊤F+λI) −1F ⊤(s−¯s), s neu =s−ω(F ˆβ).(24)
Signal amplification:
mt = (|st|−τ) +,˜s t = sign(st)mγ t , s amp t =s t +(g−1)˜st.
(25)
Signal quality gate:
qt =q min + (1−q min)cν t , s gate t =q tst.(26)
Feature-quality reweighting:
Qj = (1−ω r)

0.7C (1d) j + 0.3C(h) j  +ω rC (reg) j ,(27)
wj = (1−α) +α·clip
 Qj
median(QQ>0) +ϵ ,0.4,2.5

.
(28)
J. Execution Scale Optimization
We optimize scales∈[s min, smax]by
J(s) =E[π t(s)−b t]
−λ cvar|min(0,CVaR α(π(s)−b))|
−λ downDownDev(π(s)−b)
−λ toTurnover(s),
(29)
s⋆ = arg max
s
J(s).(30)

5
K. Training Algorithm
Training begins by constructing the feature and regime
series from the panel dataD, then initializing the policy
populationPand meta strategym. The optimization is
organized into tournament rounds. Within each round, the
current population is evaluated on the training split to form
the payoff matrixA, utility vectorU, diversity termD, and
league-advantage termL. The PSRO update then revises the
meta strategy, after which the mixed policy signal is passed
through factor neutralization, nonlinear amplification, quality
weighting, and execution-scale optimization.
Checkpoint selection is performed only on the validation
split. The selected checkpoint is the one that improves the
constrained validation objective, not necessarily the one with
the largest raw return. After validation, the population is
updated through elite retention and mutation. When the league-
injection rule is active, a best-response candidate is trained
against the current policy mixture and inserted into the popu-
lation; in the v21 configuration this candidate is the RL-hybrid
BR with a risk head and regime-specific experts. Generation-
level and round-level patience rules stop the update process
when validation improvement stalls. The final output is the
best validation-selected checkpoint, or a checkpoint ensemble
when ensemble selection is enabled.
L. Selection Criterion and Statistical Testing
Constrained validation selection metric:
S=ExcessSharpe−λ 1|min(0,ExcessCVaR)|
−λ 2|min(0,ExcessWorstDay)| −λ3 ·Violation. (31)
Walk-forward robust score (window-level excess Sharpe
{sw}W w=1):
RobustScore= ¯s−λstd Std(sw)−λmin|min(0,min w sw)|.(32)
Statistical evidence includes Newey-West, stationary boot-
strap, White Reality Check, and SPA-lite:
TWRC =
√
Tmax
j
¯dj,
TSPA = max j max

0,
√
T ¯dj
ˆσj
!
.
(33)
IV. OBJECTIVEALIGNMENT ANDDESIGNCONSISTENCY
This section does not claim a new theorem for financial
predictability. Its role is narrower: to show that several design
choices in EvoNash-MARL are aligned with standard results
from no-regret learning, multi-objective selection, and con-
strained optimization. The statements below should therefore
be read as consistency checks for the training loop rather than
as a standalone theoretical contribution.
A. Setting
LetK={1, . . . , K}denote the current policy population
and letA∈R K×K be the zero-sum payoff matrix used by
the PSRO-style meta update. Signals and leverage outputs are
clipped in implementation, so we assume
1)Bounded payoffs:|A ij| ≤G,∀i, j.
2)Bounded signals:|s k,t| ≤1after clipping and leverage
control.
3)Bounded quality scaling:q t ∈[q min,1]for some0<
qmin ≤1.
These are implementation-level assumptions rather than mar-
ket assumptions.
B. Observation 1: Standard no-regret support for the meta-
strategy
Consider the multiplicative-weights update
m(τ+1) k ∝m (τ) k exp(ηv (τ) k ), v (τ) =Am (τ) ,(34)
with|v (τ) k | ≤Gandη= p 2 logK/(T G2). Then the textbook
multiplicative-weights guarantee [25] gives
RegretT ≤G
p
2TlogK, RegretT
T ≤G
r
2 logK
T .(35)
For zero-sum matrix games, the corresponding average Nash
gap decreases at rateO
p
logK/T

.
This observation is standard, but it matters here because
our meta-strategy layer uses exactly this type of update. The
implication is not that the financial environment is solved
by game theory; it is only that the policy-mixture update is
consistent with a well-understood no-regret mechanism.
C. Observation 2: the robust score favors temporal stability
by construction
Define the walk-forward robust score
R= ¯s−λ stdσs −λ min|min(0, smin)|,(36)
where¯sis mean excess Sharpe across windows,σ s is the
standard deviation of window-level excess Sharpe, ands min
is the worst-window excess Sharpe.
If two strategies have the same¯sand satisfyσ (a) s ≤σ (b) s
together with|min(0, s (a) min)| ≤ |min(0, s(b) min)|, then immedi-
ately
R(a) ≥R (b).(37)
Moreover, with
∆σ=σ (b) s −σ (a) s ≥0,
∆d=|min(0, s (b) min)| − |min(0, s(a) min)| ≥0, (38)
we have
R(a) −R (b) ≥λ std∆σ+λ min∆d.(39)
This is a simple algebraic property rather than a deep
theorem, but it clarifies what the model-selection rule actually
rewards. Modules such as the risk head, execution-scale opti-
mization, and feature-quality weighting are useful only insofar
as they improve these stability terms under the same mean-
performance level.

6
D. Observation 3: constrained checkpoint selection is
feasible-first
Validation selection uses
S=U−λ conV, V≥0,(40)
whereUis unconstrained utility andVis aggregate constraint
violation.
For two checkpointsaandb, ifU a ≥U b andV a ≤V b, then
Sa ≥S b for anyλ con ≥0.(41)
Ifλ con → ∞, maximizingSbecomes equivalent to lexico-
graphic selection: first minimizeV, then maximizeUwithin
the minimum-violation set.
Again, the point is modest but operationally important. The
constrained selector is designed to reject checkpoints that look
attractive on raw return but fail risk or feasibility requirements.
This is particularly relevant in finance, where an apparently
profitable policy may be unusable once beta drift, downside
risk, or scale-dependent frictions are accounted for.
E. Implication for the present paper
Taken together, the three observations explain the intended
logic of the training loop. The game layer uses a standard
no-regret update to maintain a diversified policy mixture; the
robust-score objective makes temporal stability explicit rather
than incidental; and the constrained selector gives feasibility
priority during checkpoint choice. These arguments do not
establish that excess return must exist in a given market.
They do show that, conditional on there being exploitable
predictive structure, the optimization loop is internally co-
herent and pushes the system toward low-regret aggregation,
stable validation behavior, and deployable rather than purely
backtest-optimal checkpoints.
This interpretation is also consistent with recent RL and
MARL theory. Adaptivity-constrained self-play [17], robust
equilibrium learning under uncertainty [16], and max-min
multi-objective RL [20] all emphasize that in non-stationary
environments one should care not only about nominal reward,
but also about admissibility, robustness, and update discipline.
That is the sense in which the present framework is theoreti-
cally motivated.
V. EXPERIMENTS ANDRESULTS
A. Experimental Setup
Data and horizon:we use a hybrid daily US-equity
panel, with the main evaluation window from 2010-01-04
to 2026-02-27.Universe and features:the resolved v21
run operates on a filtered 39-symbol liquid universe. Fea-
tures are trailing-only and include rolling market moments,
volume-derived variables, benchmark-relative quantities, and
four regime labels.Protocol:walk-forward evaluation is the
primary protocol. Core stability runs use 252 trading days for
training, 21 for testing, step size 21, over 120 windows. Inside
each training window, the in-sample segment is split 80/20
into train and validation partitions, and checkpoint choice
is frozen before the test slice is evaluated.Methods and
TABLE I
MAIN STABILITY RESULTS OVER120WALK-FORWARD WINDOWS(HIGHER
IS BETTER)
Model MeanExSharpe StdExSharpe RobustScore MeanBeta
v21 120w 0.7600 3.4254 -0.0203 0.6731
v17 120w 0.7352 3.4361 -0.0457 0.6792
v20b 120w 0.7212 3.4691 -0.0613 0.6651
Fig. 2. 120-window main metrics comparison (v17/v20b/v21).
Fig. 3. Window-level excess Sharpe distribution.
Fig. 4. Daily out-of-sample cumulative excess return curves.
baselines:EvoNash-MARL (v21) is compared with v17/v20b,
DQN baselines, panel-ridge baseline, plus cross-market and
realistic-constraint stress tests.Statistical evidence:Newey-
West, stationary bootstrap, White Reality Check (WRC), and
SPA-lite. The intended claim is economic and engineering
robustness under this protocol, not strong proof of global
statistical dominance.
Main stability, extended OOS, and statistical evidence.
Under the robust-score criterion, v21 ranks first in the
120-window evaluation. On aligned daily OOS returns from
2014-01-02 to 2024-01-05, v21 also exceeds SPY in absolute
performance: cumulative return is 499.4% versus 203.6%,
and annualized return is 19.6% versus 11.7%. We interpret
this as economically meaningful but not decisive on its own,
because the later multiple-testing results remain weak. In
particular, we do not interpret the reported return level as
directly deployable alpha; under a small filtered universe, fixed
walk-forward design, and model-selection loop, it should be
read as conditional evidence under this protocol rather than as
a live-trading claim.

7
Fig. 5. Calendar-year return comparison between v21 and SPY (full years
only).
Fig. 6. Extended OOS cumulative return comparison (v21 vs SPY , through
2026-02-10).
TABLE II
PAIRWISE TESTS VERSUS V17 120W
Candidate MeanDiff(1d) NW p(1-side) SB p(1-side) FDR-q
v21 120w 2.54e-06 0.3691 0.3170 0.6785
v18 120w -3.45e-06 0.5572 0.5655 0.6785
v20b 120w -4.73e-06 0.6739 0.6785 0.6785
TABLE III
GLOBAL MULTI-MODEL SIGNIFICANCE TESTS
Test Statistic p-value (1-side)
White Reality Check 1.2755e-04 0.6765
SPA-lite 0.3475 0.5040
Using the same walk-forward protocol (252/21/21, non-
overlap) with the maximum feasible number of windows
on available data, we obtain 145 windows and daily OOS
coverage from 2014-01-02 to 2026-02-10. In this extended
evaluation, v21 remains ahead of SPY: cumulative return is
848.4% versus 360.1%, and annualized return is 20.5% versus
13.5%.
These tests indicate directional improvement, but they do
not establish strong global statistical significance. Accordingly,
the paper does not argue that the reported return spread
is sufficient by itself to prove a persistent universal alpha
source. The narrower empirical conclusion is that, under
a fixed medium/long-horizon walk-forward design, the v21
training-and-selection loop produces more stable deployable
checkpoints than the internal controls considered here.
Baselines, transfer, and stress tests.
Under this setup, DQN does not outperform the proposed
method; the panel baseline is stronger but with substantially
higher beta exposure.
Generalization is stronger against defensive/credit-like
benchmarks (HYG, TLT) and approximately neutral on QQQ.
Fig. 7. Pairwise effect-size confidence intervals with global WRC/SPA
context.
TABLE IV
24-WINDOW BASELINE COMPARISON
Model MeanExSharpe MedianExSharpe PosRatio MeanBeta
panel 24w 2.2570 1.5169 0.7917 1.1212
v21 first24 from 120w 0.3911 0.4244 0.5833 0.6024
dqn 24w episodes40 -0.6031 -0.1439 0.5000 0.5527
dqn 24w episodes12 -1.0444 0.0883 0.5417 0.3881
Fig. 8. Baseline comparison on risk-return plane (beta vs excess Sharpe).
TABLE V
SAME STRATEGY,DIFFERENT BENCHMARKS(2520DAYS)
Benchmark ExcessSharpe ExcessCumReturn MeanExcess(1d)
HYG 1.6803 3.2583 5.9069e-04
TLT 0.7724 2.8636 6.1728e-04
IWM 0.5815 1.2739 3.7973e-04
SPY 0.5435 0.6987 2.3351e-04
QQQ 0.0195 -0.0691 1.0905e-05
Fig. 9. Cross-market generalization by benchmark.
TABLE VI
COST/IMPACT/CAPACITY STRESS SCENARIOS(BENCHMARK: SPY)
Scenario ExcessSharpe DeltaExSharpe ExcessCumRet DeltaExCumRet
base 0.5435 0.0000 0.6987 0.0000
tc x3 0.5088 -0.0347 0.6362 -0.0625
capacity x3 0.2833 -0.2602 0.2818 -0.4169
all x2 0.3901 -0.1535 0.4388 -0.2599
all x3 0.2366 -0.3069 0.2186 -0.4801
Performance degrades under stronger frictions, while excess
Sharpe remains positive in all x3.
Window-level diagnostics and ablations.

8
Fig. 10. Constraint stress sensitivity (base/tc/impact/capacity).
Figures 11 and 12 complement the tabular results by show-
ing window-level stability, risk exposure variation, directional-
hit behavior, and ablation diagnostics.
Empirical interpretation.Taken together, the experiments
show a consistent but bounded pattern. The v21 configuration
has the best robust score in the 120-window comparison, and
the extended OOS check remains ahead of SPY through 2026-
02-10. At the same time, the global WRC/SPA-lite tests do
not establish strong statistical dominance. For this reason, the
reported returns should be interpreted as conditional evidence
under the fixed walk-forward protocol, not as a direct live-
trading alpha estimate.
The baseline comparison clarifies where the method helps.
The DQN baselines underperform in this medium-horizon
setting, which is plausible because the reward signal is noisy,
delayed, and benchmark-relative. A coarse value-based con-
troller must learn from weak daily feedback while also align-
ing its actions with multi-week allocation utility. The panel-
ridge baseline is stronger in the 24-window comparison, but
it also carries materially higher beta exposure. This makes the
comparison informative rather than decisive: part of the panel
baseline’s advantage appears to come from taking more market
exposure, whereas EvoNash-MARL explicitly penalizes beta
drift and selects checkpoints using constrained excess metrics.
The cross-market results suggest that the learned behavior is
not a universal benchmark-independent alpha source. Perfor-
mance is stronger relative to HYG and TLT, weaker relative to
QQQ, and intermediate relative to SPY and IWM. This pattern
is consistent with a risk-managed equity allocation system
whose usefulness depends on the factor overlap between the
strategy and the comparison benchmark. It also reinforces the
need to report transfer behavior rather than only the main SPY-
relative result.
The stress tests show that capacity-related penalties are more
damaging than a pure transaction-cost shock. This is expected
for medium-horizon signals: moderate linear trading costs
can be absorbed when turnover is controlled, but nonlinear
capacity penalties compress the strongest signals exactly when
the policy wants to express them. This observation supports
including execution-scale optimization and feasibility-aware
selection inside the training loop rather than applying them
as final post-processing.
Overall, the results support the design under the present
protocol, but stronger claims would require larger universes,
stricter multiple-testing control, and additional independent
OOS periods.
VI. IMPLEMENTATION ANDEVALUATIONPROTOCOL
A. Data and Universe
TABLE VII
RAW DATA SNAPSHOT USED IN THIS STUDY
Item Value
Data source Hybrid daily US-equity panel
Daily observations (approx.) 24.7 million
Distinct symbols (raw panel) 6,537
Raw coverage 1962-01-02 to 2026-02-27
Evaluation coverage (v21) 2010-01-04 to 2026-02-27
Working universe (v21) 39 liquid symbols
The starting panel is a merged daily-bar dataset assembled
from long-history US-equity records and recent liquid-market
coverage. The v21 experiments do not train on the full raw
universe. Each walk-forward run applies fixed coverage and
tradability filters: symbols must satisfy a minimum history
threshold, pass a minimum median-price screen, and survive
complete-case alignment inside the active window. The re-
solved configuration caps the working universe at 39 symbols,
including the main benchmark and transfer assets (SPY , QQQ,
IWM, TLT, HYG, VOO, and TQQQ). This reduced universe
is intentional. The experiment is not designed as broad cross-
sectional alpha mining over thousands of names; it studies
medium-horizon allocation under liquidity and execution con-
straints. Daily returns are clipped at 20% in absolute value
before model training to suppress obvious bad ticks and split-
adjustment artifacts.
B. Walk-Forward Design
TABLE VIII
PRIMARY OUT-OF-SAMPLE PROTOCOL
Item Value
Train days per window 252
Test days per window 21
Step days 21
Maximum windows 120
Total OOS daily points 2,520
Benchmark for excess metrics SPY
Model selection metric constrained excess Sharpe
Within each training window, features are computed only
from information available up to each date. The feature stack
uses rolling market moments, volume statistics, benchmark-
relative quantities, and a four-state regime label (bull, bear,
sideways, shock) built from 20-day market-return and volatil-
ity summaries. There is no future return in feature con-
struction. After feature construction, the in-window sample
is split 80/20 into train and validation segments. Checkpoint
selection uses the constrained excess-Sharpe validation metric,
and the held-out 21-day test slice is untouched until selection
is complete.
C. Resolved v21 Configuration
Several implementation choices are important for inter-
preting the results. The system is long-only in the resolved

9
Fig. 11. Window-level trajectories for v17/v20b/v21 in excess Sharpe, beta
exposure, and directional-hit ratio.
Fig. 12. Ablation diagnostics on validation excess Sharpe, beta, and Nash
gap.
TABLE IX
MAIN TRAINING KNOBS FROM V21RESOLVED CONFIGURATION
Parameter Value
Population size 16
Generations per round 4
Tournament rounds 5
PSRO iterations / eta 50 / 0.25
League self-play enabled
BR method RL-hybrid
BR RL episodes 24
Transaction cost 3 bps
Impact / capacity penalty 0.0002 / 0.0001
Signal amplification enabled (τ= 0.1, γ= 1.6)
Feature-quality reweighting enabled
Factor neutralization enabled (strength 0.3)
Execution-scale optimization enabled ([0.5,1.6], 12 steps)
Beta target / penalty 0.55 / 0.25
specification, uses a 14-day rebalance interval, and optimizes
against SPY as the benchmark for excess metrics. League best-
response training uses the RL-hybrid variant with 24 episodes,
21-day horizon reward shaping, regime-specific experts, and
an active risk head. Signal processing includes factor neutral-
ization, nonlinear amplification, and feature-quality weighting.
Transaction cost, impact, capacity, beta, drawdown, and tail
penalties enter either utility computation or execution-scale
selection rather than being applied only after training.
D. Reproduction Details
All reported tables and figures are produced by a fixed
pipeline covering statistical testing, window-stability aggrega-
tion, cross-market evaluation, stress testing, and final report
assembly. For manuscript generation, we use one frozen evi-
dence bundle. The manuscript numbers are therefore not hand-
picked from multiple runs after the fact; once the evidence
bundle is fixed, all tables and figures are generated from that
bundle. The replication package contains the statistical-test
outputs, window-stability diagnostics, cross-market results,
realistic-constraint stress tests, and the summary report used
to build the manuscript.
VII. CONCLUSION, LIMITATIONS,ANDFUTUREWORK
This paper studied EvoNash-MARL, a closed-loop frame-
work for medium/long-horizon equity allocation. The central
design choice is to treat allocation as a population-based
sequential decision problem rather than as a single-predictor
forecasting task. Within this framework, PSRO-style aggrega-
tion, league best-response training, evolutionary replacement,

10
and execution-aware checkpoint selection are coupled under
the same walk-forward protocol.
The empirical results suggest that this coupling is useful
under the evaluation design considered here. The resolved
v21 configuration obtains the best robust score in the 120-
window setting, remains ahead of SPY in the extended OOS
check through 2026-02-10, and degrades in a plausible direc-
tion under transaction-cost, impact, and capacity stress tests.
The cross-market results are also informative: performance is
stronger relative to HYG and TLT, but much weaker relative
to QQQ, suggesting that the learned behavior is not a generic
source of transferable alpha across all benchmarks.
The results should be interpreted with caution. The study
uses a relatively small filtered universe, and the reported
return levels should not be read as directly deployable live-
trading alpha. Global strong significance is not established
under the WRC/SPA-lite tests, and residual data-snooping or
model-selection bias cannot be ruled out. Execution costs,
market impact, and capacity are modeled through reduced-
form penalties rather than order-book simulation or broker-
level execution data. Baseline comparability is also imperfect
when models carry materially different beta exposure.
Future work should therefore focus less on adding architec-
tural components and more on stress-testing the existing loop.
Useful extensions include larger and more diverse universes,
stricter multiple-testing control, causal-safe online adaptation,
cross-asset evaluation, and more realistic execution modeling.
A further direction is to improve interpret-ability by decom-
posing strategy contributions across regimes, risk exposures,
and policy subpopulations.
REFERENCES
[1] M. Lopez de Prado,Advances in Financial Machine Learning. Wiley,
2018.
[2] D. H. Bailey and M. L ´opez de Prado, “The deflated sharpe ratio:
Correcting for selection bias, backtest overfitting, and non-normality,”
Journal of Portfolio Management, vol. 40, no. 5, pp. 94–107, 2014.
[3] H. White, “A reality check for data snooping,”Econometrica, vol. 68,
no. 5, pp. 1097–1126, 2000.
[4] P. R. Hansen, “A test for superior predictive ability,”Journal of Business
& Economic Statistics, vol. 23, no. 4, pp. 365–380, 2005.
[5] H. Markowitz, “Portfolio selection,”The Journal of Finance, vol. 7,
no. 1, pp. 77–91, 1952.
[6] J. Moody and M. Saffell, “Learning to trade via direct reinforcement,”
IEEE Transactions on Neural Networks, vol. 12, no. 4, pp. 875–889,
2001.
[7] Y . Nevmyvaka, Y . Feng, and M. Kearns, “Reinforcement learning for
optimized trade execution,” inProceedings of the 23rd International
Conference on Machine Learning, 2006, pp. 673–680.
[8] X.-Y . Liu, H. Yang, Q. Chen, R. Zhang, L. Yang, B. Xiao, and C. D.
Wang, “FinRL: A deep reinforcement learning library for automated
stock trading in quantitative finance,”arXiv preprint arXiv:2011.09607,
2020.
[9] X.-Y . Liu, Z. Xia, J. Rui, J. Gao, H. Yang, M. Zhu, C. D.
Wang, Z. Wang, and J. Guo, “FinRL-Meta: Market environments
and benchmarks for data-driven financial reinforcement learning,”
inAdvances in Neural Information Processing Systems, vol. 35,
2022. [Online]. Available: https://papers.neurips.cc/paper files/paper/
2022/hash/0bf54b80686d2c4dc0808c2e98d430f7-Abstract-Datasets
and Benchmarks.html
[10] J. Wang, Y . Zhang, K. Tang, J. Wu, and Z. Xiong, “AlphaStock:
A buying-winners-and-selling-losers investment strategy using inter-
pretable deep reinforcement attention networks,” inProceedings of the
25th ACM SIGKDD International Conference on Knowledge Discovery
& Data Mining, 2019, pp. 1900–1908.
[11] Z. Wang, B. Huang, S. Tu, K. Zhang, and L. Xu, “DeepTrader: A
deep reinforcement learning approach for risk-return balanced portfolio
management with market conditions embedding,”Proceedings of the
AAAI Conference on Artificial Intelligence, vol. 35, no. 1, pp. 643–650,
2021.
[12] Z. Zhu and K. Zhu, “AlphaQCM: Alpha discovery in finance with
distributional reinforcement learning,” inProceedings of the 42nd
International Conference on Machine Learning, ser. Proceedings of
Machine Learning Research, vol. 267. PMLR, 2025, pp. 80 463–80 479.
[Online]. Available: https://proceedings.mlr.press/v267/zhu25ag.html
[13] R. Lowe, Y . Wu, A. Tamar, J. Harb, P. Abbeel, and I. Mordatch, “Multi-
agent actor-critic for mixed cooperative-competitive environments,” in
Advances in Neural Information Processing Systems, 2017.
[14] M. Lanctot, V . Zambaldi, A. Gruslys, A. Lazaridou, K. Tuyls, J. Perolat,
D. Silver, and T. Graepel, “A unified game-theoretic approach to
multiagent reinforcement learning,” inAdvances in Neural Information
Processing Systems, 2017.
[15] M. Jaderberg, V . Dalibard, S. Osinderoet al., “Population based training
of neural networks,”arXiv preprint arXiv:1711.09846, 2017.
[16] L. Shi, E. Mazumdar, Y . Chi, and A. Wierman, “Sample-efficient
robust multi-agent reinforcement learning in the face of environmental
uncertainty,” inProceedings of the 41st International Conference on
Machine Learning, ser. Proceedings of Machine Learning Research,
vol. 235. PMLR, 2024, pp. 44 909–44 959. [Online]. Available:
https://proceedings.mlr.press/v235/shi24d.html
[17] D. Qiao and Y .-X. Wang, “Near-optimal reinforcement learning with
self-play under adaptivity constraints,” inProceedings of the 41st
International Conference on Machine Learning, ser. Proceedings of
Machine Learning Research, vol. 235. PMLR, 2024, pp. 41 430–41 455.
[Online]. Available: https://proceedings.mlr.press/v235/qiao24b.html
[18] A. A. Nguyen, A. Gu, and M. P. Wellman, “Explicit exploration
for high-welfare equilibria in game-theoretic multiagent reinforcement
learning,” inProceedings of the 42nd International Conference on
Machine Learning, ser. Proceedings of Machine Learning Research,
vol. 267. PMLR, 2025, pp. 45 988–46 007. [Online]. Available:
https://proceedings.mlr.press/v267/nguyen25b.html
[19] Z. Sun, S. He, F. Miao, and S. Zou, “Constrained reinforcement
learning under model mismatch,” inProceedings of the 41st
International Conference on Machine Learning, ser. Proceedings of
Machine Learning Research, vol. 235. PMLR, 2024, pp. 47 017–47 032.
[Online]. Available: https://proceedings.mlr.press/v235/sun24d.html
[20] G. Park, W. Byeon, S. Kim, E. Havakuk, A. Leshem, and Y . Sung,
“The max-min formulation of multi-objective reinforcement learning:
From theory to a model-free algorithm,” inProceedings of the 41st
International Conference on Machine Learning, ser. Proceedings of
Machine Learning Research, vol. 235. PMLR, 2024, pp. 39 616–39 642.
[Online]. Available: https://proceedings.mlr.press/v235/park24b.html
[21] J. F. Nash, “Equilibrium points in n-person games,”Proceedings of the
National Academy of Sciences, vol. 36, no. 1, pp. 48–49, 1950.
[22] R. Zhang, Z. Xu, C. Ma, C. Yu, W.-W. Tu, S. Huang, D. Ye, W. Ding,
Y . Yang, and Y . Wang, “A survey on self-play methods in reinforcement
learning,”arXiv preprint arXiv:2408.01072, 2024. [Online]. Available:
https://arxiv.org/abs/2408.01072
[23] W. K. Newey and K. D. West, “A simple, positive semi-definite,
heteroskedasticity and autocorrelation consistent covariance matrix,”
Econometrica, vol. 55, no. 3, pp. 703–708, 1987.
[24] D. N. Politis and J. P. Romano, “The stationary bootstrap,”Journal of
the American Statistical Association, vol. 89, no. 428, pp. 1303–1313,
1994.
[25] Y . Freund and R. E. Schapire, “A decision-theoretic generalization of
on-line learning and an application to boosting,”Journal of Computer
and System Sciences, vol. 55, no. 1, pp. 119–139, 1997.
