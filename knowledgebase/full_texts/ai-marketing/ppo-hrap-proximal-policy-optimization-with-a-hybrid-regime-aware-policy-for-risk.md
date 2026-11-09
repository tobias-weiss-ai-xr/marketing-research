---
title: 'PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading'
url: https://arxiv.org/abs/2610.01325
category: ai-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors:
- Duong Hien Chi Kien
- Thanh Trung Huynh
source: arxiv
pdf_url: https://arxiv.org/pdf/2610.01325
pages: 8
chars: 35565
fetched_at: '2026-11-08T13:24:51+00:00'
kb_version: 1
---

# PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading

PPO-HRAP: Proximal Policy Optimization with a Hybrid
Regime-Aware Policy for Risk-Controlled Trading
Duong Hien Chi Kien
24kien.dhc@vinuni.edu.vn
College of Engineering and Computer Science,
VinUniversity
Ha Noi, Viet Nam
Huynh Thanh Trung
trung.ht@vinuni.edu.vn
College of Engineering and Computer Science,
VinUniversity
Ha Noi, Viet Nam
Abstract
Reinforcement learning for trading often struggles to balance up-
side participation with drawdown control. Profit-only policies can
collapse toward passive long exposure on upward-drifting assets,
while aggressively risk-penalized rewards can become too defen-
sive during volatile periods. This paper proposes PPO-HRAP, a
hybrid regime-aware policy that combines Proximal Policy Opti-
mization with an interpretable regime prior. The agent observes
both market features and portfolio-state variables, receives a re-
ward combining portfolio log return, VIX-conditioned drawdown-
increase penalty, target-exposure deviation, and turnover cost, and
executes a blended action between the PPO actor output and a
regime-derived target exposure. On the held-out 2020–2022 SPY
test window, PPO-HRAP achieves 27.62% total return, 8.48% annu-
alized return, 0.6447 Sharpe ratio, 0.8588 Sortino ratio, and 0.4592
Calmar ratio, while reducing maximum drawdown from 34.10% for
Buy and Hold to 18.47%. Across five SPY seeds, PPO-HRAP remains
stable with mean total return0 .2725± 0.0109and mean Sharpe
ratio0.6219± 0.0565. Single-run cross-asset tests on QQQ and DIA
further show that the proposed method ranks first on total return
and Sharpe ratio for all three reported assets. These results suggest
that blending learned actions with a volatility-aware regime prior
is a practical way to improve risk-adjusted trading behavior, al-
though the current policy still incurs high turnover and cross-asset
robustness beyond SPY remains limited to single-run evidence.
Keywords
reinforcement learning trading, portfolio management, PPO, market
regime, risk control, drawdown control
1 Introduction
Reinforcement learning (RL) has become a practical tool for port-
folio management because it can optimize sequential allocation
decisions directly from market interaction rather than from a fixed
predictive model [13, 17]. In trading, however, the reward function
is often misaligned with the real objective. A policy trained only to
maximize return can converge to behavior that is close to remain-
ing fully long on an upward-drifting equity index. Conversely, a
policy penalized too aggressively for risk can become excessively
defensive and sacrifice most upside.
This tension is not merely an implementation detail. Daily al-
location is a closed-loop control problem: the action changes the
portfolio state, the new portfolio state changes future risk exposure,
and the reward observed by the agent mixes market movement
with the consequences of prior trades. A useful trading agent there-
fore needs both market information, such as trend and volatility,
and portfolio information, such as current weight, cash ratio, and
drawdown. If the state omits these portfolio variables, the agent
receives an incomplete description of the system it is controlling.
If the reward ignores drawdown or turnover, the agent can learn
policies that look profitable in average return but are unattractive
as trading systems.
This problem becomes sharper when risk control depends on
volatility signals such as the CBOE Volatility Index (VIX), a widely
used indicator of market stress [40]. VIX can indicate how aggres-
sively a portfolio should be sized, but it does not by itself provide
a strong directional prior. In a single-asset SPY plus cash setting,
this creates an unstable design space: mild penalties fail to move
the policy far enough away from passive exposure, whereas strong
penalties may push it toward near-flat or short-biased behavior.
We address this gap with PPO-HRAP, short for PPO-Hybrid
Regime-Aware Policy. The method uses a PPO backbone [34] but
augments it with an explicit regime-aware action prior. The core de-
sign separates two questions: which direction the portfolio should
lean, and how much risk should be taken under the current market
regime. Trend signals define a desired directional exposure, while
the VIX z-score controls drawdown sensitivity and exposure reduc-
tion under stress. Empirically, we evaluate the method with a main
SPY benchmark, a five-seed SPY reliability study, and single-run
transfers to QQQ and DIA.
The method is intentionally simple. Rather than asking a neural
policy to discover all regime structure only from delayed rewards,
PPO-HRAP computes an interpretable target exposure from trend
and stress indicators and then blends that target with the PPO action.
This keeps the learned policy in the loop but anchors execution
to a prior that is easy to inspect. The design is therefore closer to
a hybrid control system than to a fully unconstrained black-box
trader.
The contribution is practical rather than purely theoretical. PPO-
HRAP is designed as a hybrid control-plus-RL trading policy rather
than as a purely learned reward innovation. Its main contributions
are:
• a hybrid reward formulation that combines portfolio log
return, dynamic drawdown control, target-exposure regu-
larization, and turnover control;
• an explicit regime-classification rule that separates direc-
tional guidance from volatility-aware risk sizing;
• an action-blending mechanism that treats the PPO policy
as a correction around an interpretable prior instead of as
an unconstrained controller; and
arXiv:2610.01325v1  [cs.AI]  1 Oct 2026

Duong Hien Chi Kien and Huynh Thanh Trung
• a benchmarked evaluation pipeline spanning financial base-
lines, RL reward baselines, validation-based action-prior se-
lection, SPY multi-seed reliability analysis, and cross-asset
transfer to QQQ and DIA.
On the 2020–2022 test window, PPO-HRAP achieves the highest
total return and the highest Sharpe, Sortino, and Calmar ratios
among all compared methods in the main SPY run, while also
transferring favorably to QQQ and DIA. The multi-seed analysis
adds nuance to this picture: averaged over seeds, SAC with a profit-
only reward attains better risk ratios at a lower total return. The rest
of the paper presents the related literature, the hybrid policy design,
the experimental protocol, and the resulting empirical trade-offs.
2 Related Work
Deep RL for trading and portfolio allocation has evolved from
early direct reinforcement formulations into policy-based systems
that operate on historical market features [ 1, 10, 16, 17, 19, 21–
24, 28, 30–32, 42, 43]. More recent frameworks extend this direction
with richer temporal structure, broader action spaces, or short-
selling support [13]. At the optimization level, PPO [34] and SAC
[14] remain strong continuous-control baselines and are therefore
natural comparators in our setting.
This work also sits alongside classical portfolio allocation and on-
line portfolio selection. Mean-variance allocation [26], continuous-
time portfolio control [27], Kelly-style growth criteria [6, 18], and
universal portfolios [9] all highlight the long-standing trade-off be-
tween return, risk, and adaptive capital allocation. Online multiplicative-
update methods further show that portfolio rules can be updated
sequentially as new prices arrive [15]. PPO-HRAP differs from these
approaches because it learns a policy from simulated trading in-
teraction, but the same trade-off between upside participation and
drawdown control motivates the design.
Among these optimizers, PPO is particularly relevant because
it combines policy-gradient learning with a clipped surrogate ob-
jective that improves training stability without requiring a fully
second-order trust-region method [34, 38, 39]. In portfolio alloca-
tion problems with continuous actions, this makes PPO a practical
backbone for learning bounded position weights while retaining a
relatively simple training pipeline [20, 29, 36].
Specifically, PPO optimizes the clipped surrogate objective
𝐿CLIP(𝜃)=E 𝑡
h
min 𝜅𝑡(𝜃) ˆ𝐴𝑡,clip(𝜅 𝑡(𝜃),1−𝜖,1+𝜖) ˆ𝐴𝑡 i ,(1)
where the probability ratio is
𝜅𝑡(𝜃)= 𝜋𝜃(𝑎𝑡|𝑠 𝑡) 𝜋𝜃old(𝑎𝑡|𝑠 𝑡).(2)
The critic estimates the value function𝑉𝜋(𝑠) and the action-value
function
𝑄𝜋(𝑠,𝑎)=E 𝜋
"∞∑︁
𝑘=0
𝛾𝑘𝑟𝑡+𝑘|𝑠 𝑡 =𝑠,𝑎 𝑡 =𝑎
#
,(3)
which gives the advantage
𝐴𝜋(𝑠,𝑎)=𝑄 𝜋(𝑠,𝑎)−𝑉 𝜋(𝑠).(4)
This clipping mechanism constrains overly large policy updates
and is one reason PPO remains a practical baseline for financial
control tasks with noisy returns.
Another line of work focuses on risk-aware reward engineering.
In portfolio problems, performance is commonly summarized with
risk-adjusted measures such as the Sharpe ratio [35], Sortino ratio
[37], Calmar ratio, and maximum drawdown. RL trading systems
often embed volatility, downside risk, or drawdown penalties into
the reward, but reward shaping alone does not necessarily tell the
agent which market direction to favor when stress rises [3, 8, 11].
PPO-HRAP builds on this observation by retaining drawdown-
aware reward shaping while adding an explicit regime-derived
action prior.
Drawdown is especially important because it is path dependent.
Two policies can have similar final return but very different investor
experience if one reaches that return through deep interim losses.
Prior portfolio literature treats drawdown and related tail-risk mea-
sures as first-class risk objectives [ 7, 33]. In an RL environment,
however, path dependence also creates a modeling issue: current
drawdown and running peak must be part of the simulator state
used to compute reward. PPO-HRAP uses these quantities explic-
itly in the environment and penalizes only drawdown increases,
so the penalty targets worsening losses rather than permanently
punishing a policy for past market stress.
The proposed method also relates to hybrid trading systems that
combine learned policies with structured inductive biases. We do
not present PPO-HRAP as a purely learned trading rule. It is a
hybrid control-plus-RL design in which the final executed action
depends on both a deterministic regime prior and the PPO policy
output. This framing matters because the reported gains should be
interpreted as the joint effect of the prior and the learned correction.
3 Methodology
3.1 Problem formulation
We formulate daily ETF allocation as a discounted Markov decision
processM=(S,A,P,R,𝛾) . At date𝑡, the agent observes a state
𝑠𝑡 ∈S , chooses a continuous portfolio action 𝑎𝑡 ∈A=[− 1, 1],
receives reward𝑟𝑡 =R(𝑠 𝑡,𝑎𝑡,𝑠𝑡+1), and transitions according to the
market and portfolio simulatorP. The discount factor𝛾 is inherited
from the PPO training configuration and controls the horizon over
which future trading rewards affect the policy update.
The state is the concatenation of market and portfolio variables:
𝑠𝑡 =[𝑥 mkt 𝑡 ,𝑥 port 𝑡 ]∈R 13,(5)
where𝑥 mkt 𝑡 ∈R 9 and𝑥 port 𝑡 ∈R 4. The market vector is
𝑥 mkt 𝑡 =[ℓ 𝑡,sma 𝑡,rsi 14,𝑡,bb 𝑡, 𝑧vix 𝑡 ,
ret5 𝑡,ret 20 𝑡 ,ma 5,20 𝑡 ,Δ 5vix𝑡], (6)
and the portfolio vector is
𝑥 port 𝑡 =[𝑐 𝑡, 𝑤𝑡−1,upnl 𝑡, 𝑑𝑑𝑡].(7)
Here𝑐𝑡 is cash ratio,𝑤𝑡−1 is the current risky-asset weight, upnl𝑡 =
NA V𝑡−NA V0
NA V0 , and 𝑑𝑑𝑡 is current drawdown. The trading environ-
ment also tracks date, step, NAV, running peak, drawdown, current
weight, cash ratio, and unrealized PnL for reward computation and
diagnostics.
The inclusion of portfolio variables is important for the Markov-
ian interpretation of the environment. Market features describe the
external price process, but they do not describe the agent’s current

PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading
Figure 1: PPO-HRAP architecture.
exposure. The same price movement has different consequences
when the portfolio is fully invested, partially in cash, or short. By in-
cluding current weight, cash ratio, unrealized PnL, and drawdown,
the policy observes the variables that determine how the next trade
will affect NAV and future risk.
Figure 1 summarizes the full training-time data flow. During
inference the same feature computation, regime detector, action
blending, and execution steps are used, but the reward is not used
to update the policy. This distinction matters because reward is a
learning signal during training and an evaluation diagnostic during
testing, not an input required by the deployed policy.
Table 1: Regime-derived target exposure.
Regime Condition𝑤 ★ 𝑡
Bull, calm bull and not stress 1.0
Bull, stressed bull and stress 0.5
Neutral mixed trend 0.3
Neutral-negative weak negative trend 0.1
Bear, calm bear without stress 0.0
Bear, stressed bear and stress -0.1
Bear, crisis bear and crisis -0.8
3.2 Feature engineering
All features are computed from information available before the
trading action. The main formulas are
ℓ𝑡 =log
 𝐶𝑡
𝐶𝑡−1

,(8)
sma𝑡 = 𝐶𝑡 SMA50,𝑡 −1,(9)
rsi14,𝑡 =100− 100 1+RS 14,𝑡 ,(10)
bb𝑡 = 4𝜎20,𝑡 SMA20,𝑡 ,(11)
𝑧vix 𝑡 = VIX𝑡−𝜇 252,𝑡 𝜎252,𝑡 ,(12)
ret𝑘 𝑡 = 𝐶𝑡 𝐶𝑡−𝑘 −1, 𝑘∈{5,20},(13)
ma5,20 𝑡 = SMA5,𝑡 SMA20,𝑡 −1,(14)
Δ5vix𝑡 = VIX𝑡 VIX𝑡−5 −1.(15)
The RSI definition follows the 14-day relative-strength convention
[41], while the Bollinger bandwidth uses bands at SMA20,𝑡± 2𝜎20,𝑡
[4]. The observation includes nine market features and four portfo-
lio features, giving a 13-dimensional input to the actor.
The feature set intentionally mixes short-horizon and medium-
horizon signals. Daily log return captures immediate price move-
ment; the 5-day and 20-day returns summarize recent momentum
over roughly one trading week and one trading month; and the
moving-average spread gives a compact trend indicator [5]. RSI and
Bollinger bandwidth provide complementary information about
momentum and realized dispersion [ 12]. The VIX z-score and 5-
day VIX change are included because the proposed policy explicitly
treats volatility stress as a risk-sizing signal rather than as a tradable
asset.
3.3 Regime prior and action blending
The regime detector uses direction and stress signals separately.
Direction is defined by ret20 𝑡 and ma5,20 𝑡 : both positive indicates
a bullish regime, while both negative indicates a bearish regime.
Stress is identified from𝑧vix 𝑡 : values of at least 0.8 mark a stressed
market and values of at least 1.8 mark a crisis. These rules map to
the target exposure𝑤 ★ 𝑡 in Table 1.
The executed portfolio weight is
𝑤𝑡 =(1−𝜌)𝑎 𝑡+𝜌𝑤 ★ 𝑡 .(16)
This works as a behavioral prior: the actor can still adapt through𝑎𝑡 ,
but execution is biased toward a regime-consistent weight. Vanilla

Duong Hien Chi Kien and Huynh Thanh Trung
PPO must learn both direction and sizing entirely from delayed
reward; PPO-HRAP gives the policy a stable target when trend and
volatility agree.
The blend coefficient𝜌 controls how strongly this prior affects
execution. When𝜌= 0, the method reduces to executing the raw
PPO action. When 𝜌= 1, the learned actor is ignored and the
system becomes a deterministic regime rule. Intermediate values
preserve the adaptability of PPO while preventing the action from
drifting too far away from a stress-aware target. This is the main
mechanism by which PPO-HRAP separates the problem of learning
fine-grained allocation corrections from the problem of enforcing a
coarse risk regime.
3.4 Reward design and optimization
PPO-HRAP decomposes reward into four interpretable compo-
nents:
𝑟𝑡 =𝑟 return 𝑡 −𝑟 drawdown 𝑡 −𝑟 target 𝑡 −𝑟 turnover 𝑡 .(17)
The return term rewards profitability, the drawdown term discour-
ages worsening capital loss, the target term encourages regime
consistency, and the turnover term discourages unstable realloca-
tion. In implementation,
𝑟𝑡 =ℓ 𝑝 𝑡 −𝜆 rrc(𝑡)Δ𝑑𝑑𝑡−𝛽 target(𝑤𝑡−𝑤 ★ 𝑡)2−𝛽 turn𝜏𝑡,(18)
whereℓ 𝑝 𝑡 =log  NA V𝑡+1 NA V𝑡  and𝜏𝑡 =|𝑤 𝑡−𝑤𝑡−1|.
Each term addresses a different failure mode. The return term
prevents the policy from becoming a purely defensive cash strategy.
The drawdown-increase term penalizes new deterioration relative
to the running peak, which is more targeted than penalizing the
absolute drawdown level at every step. The target penalty discour-
ages the actor from fighting the regime prior when trend and stress
signals agree. The turnover penalty discourages excessive changes
in portfolio weight, which is important because transaction costs
are charged at each reallocation.
The dynamic drawdown coefficient starts from a base penalty
and scales it by market stress:
𝜆rrc(𝑡)=max{0,𝜆 base(1+𝛼·clip(𝑧 vix 𝑡 ,−3,3))}.(19)
Thus, when VIX z-score rises, the drawdown penalty increases;
when stress is low, the penalty relaxes toward its base level. Draw-
down is measured from the running peak𝑃𝑡 =max(𝑃 𝑡−1,NA V𝑡):
𝑑𝑑𝑡 = 𝑃𝑡−NA V𝑡 𝑃𝑡 ,Δ𝑑𝑑 𝑡 =max(𝑑𝑑 𝑡−𝑑𝑑𝑡−1,0).(20)
The VIX-conditioned coefficient can be interpreted as a first-order
stress adjustment to the base drawdown penalty. Starting from𝜆base,
the multiplier(1+𝛼𝑧 vix 𝑡 ) increases risk aversion when volatility
is above its trailing mean and reduces it when volatility is below
normal. Clipping the z-score avoids extreme coefficients during
rare spikes, while the outer maximum prevents the penalty from
becoming negative.
Training uses rewards for policy updates. During inference, the
environment still observes state and executes trades, but reward is
only logged for evaluation; no policy update is performed. Table 2
summarizes the training procedure.
Table 2: PPO-HRAP training loop (pseudocode).
Input:historical market data, VIX, feature set,𝜌.
Initialize PPO actor-critic parameters.
foreach training timestep𝑡do
Observe𝑠𝑡 =[𝑥 mkt 𝑡 ,𝑥 port 𝑡 ].
Compute regime from trend and VIX z-score.
Compute target exposure𝑤 ★ 𝑡 .
Sample raw PPO action𝑎𝑡 .
Blend𝑤𝑡 =(1−𝜌)𝑎 𝑡+𝜌𝑤 ★ 𝑡 .
Execute trade, update NAV, running peak, drawdown.
Compute reward𝑟𝑡 and store transition.
ifthe rollout buffer is fullthenupdate PPO actor-critic.
end for
Return:trained policy for inference-time trading.
Table 3: PPO-HRAP reproducibility settings.
Parameter Value
Total timesteps 30,000
Main seed 42
Learning rate1×10 −4
Rollout steps 1024
Batch size 128
PPO epochs/update 10
Entropy coefficient 0.0
Action-prior weight𝜌0.6
𝜆base,𝛼0.05, 0.5
𝛽target,𝛽 turn 0.02, 0.0015
Transaction cost 0.001
Table 4: Benchmark formulations.
Method Formulation
Buy and Hold𝑤 𝑡 =1after the initial allocation.
Risk parity𝑤 𝑡 =clip

𝜎★
ˆ𝜎60,𝑡,0,1

.
CPPI𝑤 𝑡 =clip
𝑚(NA V𝑡−𝐹)
NA V𝑡 ,0,1

.
PPO/SAC profit𝑟 𝑡 =ℓ𝑝 𝑡 .
PPO variance𝑟 𝑡 =ℓ𝑝 𝑡 −𝜆 var cVar𝑡(ℓ𝑝).
PPO static MDD𝑟 𝑡 =ℓ𝑝 𝑡 −𝜆 mdd𝑑𝑑𝑡 .
PPO-HRAP Return, dynamic drawdown, target-consistency, and turnover
terms with action blending.
4 Results
4.1 Experimental protocol and baselines
We use chronological splits: 2010–2017 for training, 2018–2019 for
validation, and 2020–2022 for testing. The SPY split contains 2013,
503, and 756 rows respectively. All methods use a 0.1% proportional
transaction cost. The main SPY result uses seed 42, the reliability
study uses{7, 11, 19, 23, 42}, and cross-asset transfer is evaluated
on QQQ and DIA.
Table 4 summarizes the benchmark formulations. Buy and Hold
fixes𝑤𝑡 = 1. Risk parity sets 𝑤𝑡 =clip

𝜎★
ˆ𝜎60,𝑡,0,1

at a 21-day
rebalance frequency [ 25]. CPPI uses 𝑤𝑡 =clip

𝑚(NA V𝑡−𝐹)
NA V𝑡 ,0,1

with floor 𝐹= 0.8NA V0 and multiplier 𝑚= 3[ 2]. RL baselines
share the same environment but differ by algorithm or reward.
4.2 Main SPY performance
We report total return, annualized return, Sharpe ratio [35], Sortino
ratio [37], Calmar ratio, and maximum drawdown. Table 5 removes
turnover to keep the main comparison focused on return and risk.
PPO-HRAP achieves the strongest total return, annualized return,
Sharpe, Sortino, and Calmar on SPY. Relative to Buy and Hold,
Sharpe improves from 0.3420 to 0.6447 and maximum drawdown

PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading
Figure 2: SPY return–drawdown trade-off.
decreases from 34.10% to 18.47%. The smallest drawdown is obtained
by PPO Static MDD (9.51%), but at the cost of a much lower total
return (5.91%). Figure 2 visualizes this risk-return trade-off directly
by comparing total return against maximum drawdown.
4.3 SPY multi-seed reliability
Single-run trading results can be sensitive to initialization, espe-
cially for policy-gradient methods trained on noisy financial re-
wards. To check whether the proposed behavior is tied to one favor-
able random seed, we rerun the RL methods on seeds{7, 11, 19, 23, 42}.
Table 6 reports the mean and standard deviation of the main risk-
return metrics.
The multi-seed results show two useful nuances. First, PPO-
HRAP has the best mean total return among the RL methods and a
small return standard deviation, indicating that the performance
improvement is not isolated to seed 42. Second, SAC profit has
stronger mean Sharpe, Calmar, and drawdown in this multi-seed
summary, but it also produces lower mean total return than PPO-
HRAP. We therefore interpret the proposed method as a return-
leading hybrid policy with improved drawdown control relative
to passive long exposure, not as a universal winner on every risk
metric.
4.4 Cross-asset evaluation
The cross-asset runs test whether the regime-guided prior transfers
beyond SPY. PPO-HRAP ranks first on total return and Sharpe
ratio for SPY, QQQ, and DIA. It also ranks first on Calmar ratio for
SPY and DIA; on QQQ, SAC profit has the best Calmar because it
produces a smaller drawdown. Figure 4 compares PPO-HRAP with
key baselines, and Figure 5 shows the Sharpe-ratio matrix across
all methods and assets.
Table 7 reports the full single-run QQQ and DIA test metrics
across the compared methods.
4.5 Action-prior sensitivity and behavior
The validation search over𝜌 selects𝜌= 0.6, with validation Calmar
0.2299 and validation total return 0.0800. Performance is not mono-
tonic in𝜌: a weak prior does not sufficiently regularize the actor,
while an overly strong prior can suppress learned correction. On
SPY test data, PPO-HRAP has average high-VIX exposure 0.4337
and average low-VIX exposure 0.8839, confirming that the policy
lowers exposure under stress. It still spends 54.10% of the test period
at full-long exposure, so the prior mitigates but does not eliminate
long bias.
5 Discussion
The main benefit of PPO-HRAP appears to come from decoupling
directional guidance from risk sizing. Reward-only baselines either
behave nearly identically to Buy and Hold or become too conserva-
tive. By blending the learned action with a regime-derived target,
PPO-HRAP injects a strong inductive bias that remains consistent
with market stress and trend direction while still allowing PPO to
fine-tune execution.
The behavioral diagnostics also help explain why PPO-HRAP
improves the aggregate metrics without eliminating long exposure
entirely. Under high-VIX conditions, average exposure falls from
0.8839 in calmer periods to 0.4337, which indicates that the hybrid
policy does react to stress rather than staying mechanically fully
invested. At the same time, the method still spends 54.10% of the
test period at full long exposure, so the current regime prior should
be viewed as a partial correction to vanilla PPO behavior rather
than a complete solution to long bias.
This practical benefit comes with clear trade-offs. First, turnover
is high: PPO-HRAP reaches 51.22 on the SPY test split and remains
around 39–56 across SPY, QQQ, and DIA, far above passive or
reward-only baselines. Second, although the five-seed SPY study
substantially strengthens the reliability story, the cross-asset ev-
idence on QQQ and DIA is still single-run and therefore should
be interpreted more cautiously. Third, the training budget remains
modest at 30,000 timesteps, so the reported results are best viewed
as a strong benchmark snapshot rather than a fully saturated op-
timization study. The paper therefore supports PPO-HRAP as a
promising engineering design, but not yet as a universally vali-
dated trading policy.
6 Conclusion
This paper presented PPO-HRAP, a PPO-based hybrid regime-
aware policy for risk-controlled trading. The method combines
dynamic drawdown control, regime-guided target exposure, and
action blending to address the limitations of reward-only RL trad-
ing on upward-drifting equity ETFs. In the main 2020–2022 SPY
run, PPO-HRAP improves total return and risk-adjusted metrics
over both financial and RL baselines while substantially reducing
maximum drawdown relative to Buy and Hold. The multi-seed SPY
results show that these gains are not confined to a single random
seed, and the single-run transfers to QQQ and DIA indicate that the
hybrid regime prior can remain useful beyond the original market.
The current findings support the practical value of hybrid control-
plus-learning policies in financial RL. The most important next
steps are broader multi-seed cross-asset evaluation, longer training
budgets, deeper turnover analysis, richer regime definitions, and
broader testing across additional assets and market conditions.

Duong Hien Chi Kien and Huynh Thanh Trung
Table 5: Held-out test performance on SPY, 2020–2022. Best values are bold.
Method Total Return Ann. Return Sharpe Sortino Calmar MDD
Buy and Hold 0.1760 0.0556 0.3420 0.4251 0.1630 -0.3410
Risk-Parity 0.0799 0.0260 0.2281 0.2848 0.0898 -0.2892
CPPI -0.0275 -0.0093 -0.0021 -0.0026 -0.0427 -0.2174
PPO Profit 0.1760 0.0556 0.3420 0.4251 0.1630 -0.3410
SAC Profit 0.1760 0.0556 0.3420 0.4251 0.1630 -0.3410
PPO Variance 0.1356 0.0434 0.3384 0.4208 0.1829 -0.2371
PPO Static MDD 0.0591 0.0193 0.3341 0.4153 0.2034-0.0951
PPO-HRAP0.2762 0.0848 0.6447 0.8588 0.4592-0.1847
Figure 3: SPY cumulative returns across methods.
Table 6: SPY multi-seed test summary across RL methods.
Method Ret. Mean Ret. Std Sharpe Mean Sharpe Std Calmar Mean Calmar Std MDD Mean MDD Std
PPO-HRAP0.27250.0109 0.6219 0.0565 0.4508 0.0499 -0.1876 0.0210
PPO Static MDD 0.0575 0.2008 0.1320 0.3882 0.0550 0.1829 -0.3554 0.0321
PPO Profit 0.17810.00590.34440.00670.16480.0053-0.34130.0005
PPO Variance -0.1126 0.1062 -0.3720 0.2117 -0.1512 0.0851 -0.2264 0.1560
SAC Profit 0.1978 0.08970.86440.24171.47330.6717-0.04690.0199
Table 7: QQQ and DIA single-run test performance across methods.
Asset Method Total Ret. Ann. Ret. Sharpe Sortino Calmar MDD Turnover
QQQ Buy and Hold 0.2306 0.0717 0.3826 0.5082 0.2014 -0.3562 1.0000
QQQ Risk Parity 0.1317 0.0422 0.2985 0.3954 0.1512 -0.2788 3.8472
QQQ CPPI -0.0072 -0.0024 0.1010 0.1361 -0.0067 -0.3605 9.7168
QQQ PPO Static MDD 0.2306 0.0717 0.3826 0.5082 0.2014 -0.3562 1.0000
QQQ PPO Profit 0.2306 0.0717 0.3826 0.5082 0.2014 -0.3562 1.0000
QQQ PPO Variance -0.1770 -0.0630 -0.5244 -0.8868 -0.1951 -0.3227 35.3054
QQQ SAC Profit 0.1084 0.0350 0.4684 0.6231 0.5739 -0.0609 10.0306
QQQ PPO-HRAP 0.4149 0.1228 0.7811 1.0697 0.4799 -0.2559 39.4215
DIA Buy and Hold 0.1468 0.0468 0.3088 0.3675 0.1263 -0.3706 1.0000
DIA Risk Parity 0.0441 0.0145 0.1727 0.2107 0.0482 -0.3013 2.7133
DIA CPPI -0.0407 -0.0138 -0.0900 -0.1085 -0.0813 -0.1696 7.3029
DIA PPO Static MDD 0.1468 0.0468 0.3088 0.3675 0.1263 -0.3706 1.0000
DIA PPO Profit 0.1468 0.0468 0.3088 0.3675 0.1263 -0.3706 1.0000
DIA PPO Variance -0.1266 -0.0442 -0.4967 -0.5515 -0.2245 -0.1967 52.6533
DIA SAC Profit 0.0568 0.0186 0.2677 0.2981 0.2586 -0.0720 7.2781
DIA PPO-HRAP 0.2811 0.0862 0.6623 0.8622 0.4838 -0.1782 55.5914

PPO-HRAP: Proximal Policy Optimization with a Hybrid Regime-Aware Policy for Risk-Controlled Trading
Figure 4: Cross-asset performance on SPY, QQQ, and DIA.
Figure 5: Cross-asset Sharpe-ratio heatmap.
Table 8: Validation sweep for action-prior weight𝜌on SPY.
𝜌Return Sharpe Calmar MDD Filter
0.3 0.0686 0.3770 0.1792 -0.1889 no
0.4 0.0729 0.4146 0.1941 -0.1854 no
0.5 0.0771 0.4537 0.2126 -0.1787 yes
0.60.0800 0.4863 0.2299-0.1713 yes
0.7 0.0767 0.4835 0.2291-0.1650yes
Code Availability
The implementation is available at https://github.com/chikien07012006/
PPO_Regime-Aware-Trading.
References
[1] Saud Almahdi and Steve Y. Yang. 2017. An Adaptive Portfolio Trading System:
A Risk-Return Portfolio Optimization Using Recurrent Reinforcement Learning
with Expected Maximum Drawdown.Expert Systems with Applications87 (2017),
267–279.
[2] Fischer Black and André F. Perold. 1992. Theory of Constant Proportion Portfolio
Insurance.Journal of Economic Dynamics and Control16, 3–4 (1992), 403–426.
[3] Tim Bollerslev. 1986. Generalized Autoregressive Conditional Heteroskedasticity.
Journal of Econometrics31, 3 (1986), 307–327.
Figure 6: Validation Calmar over action-prior weight𝜌.
[4] John Bollinger. 2002.Bollinger on Bollinger Bands. McGraw-Hill.
[5] William Brock, Josef Lakonishok, and Blake LeBaron. 1992. Simple Technical
Trading Rules and the Stochastic Properties of Stock Returns.The Journal of
Finance47, 5 (1992), 1731–1764.
[6] Enzo Busseti, Ernest K. Ryu, and Stephen Boyd. 2016. Risk-Constrained Kelly
Gambling.The Journal of Investing25, 3 (2016), 118–134.
[7] Alexei Chekhlov, Stanislav Uryasev, and Michael Zabarankin. 2005. Drawdown
Measure in Portfolio Optimization.International Journal of Theoretical and
Applied Finance8, 1 (2005), 13–58.
[8] Rama Cont. 2001. Empirical Properties of Asset Returns: Stylized Facts and
Statistical Issues.Quantitative Finance1, 2 (2001), 223–236.
[9] Thomas M. Cover. 1991. Universal Portfolios.Mathematical Finance1, 1 (1991),
1–29.
[10] Yue Deng, Feng Bao, Youyong Kong, Zhiquan Ren, and Qionghai Dai. 2017. Deep
Direct Reinforcement Learning for Financial Signal Representation and Trading.
IEEE Transactions on Neural Networks and Learning Systems28, 3 (2017), 653–664.
[11] Robert F. Engle. 1982. Autoregressive Conditional Heteroscedasticity with Esti-
mates of the Variance of United Kingdom Inflation.Econometrica50, 4 (1982),
987–1007.
[12] Thomas Fischer and Christopher Krauss. 2018. Deep Learning with Long Short-
Term Memory Networks for Financial Market Predictions.European Journal of
Operational Research270, 2 (2018), 654–669.
[13] Fengchen Gu, Zhengyong Jiang, Ángel F. García-Fernández, Angelos Stefani-
dis, Jionglong Su, and Huakang Li. 2025. MTS: A Deep Reinforcement Learn-
ing Portfolio Management Framework with Time-Awareness and Short-Selling.
arXiv:2503.04143 [q-fin.ST]
[14] Tuomas Haarnoja, Aurick Zhou, Pieter Abbeel, and Sergey Levine. 2018. Soft
Actor-Critic: Off-Policy Maximum Entropy Deep Reinforcement Learning with
a Stochastic Actor. InProceedings of the 35th International Conference on Machine
Learning.

Duong Hien Chi Kien and Huynh Thanh Trung
[15] David P. Helmbold, Robert E. Schapire, Yoram Singer, and Manfred K. Warmuth.
1998. On-Line Portfolio Selection Using Multiplicative Updates.Mathematical
Finance8, 4 (1998), 325–347.
[16] Yifu Jiang, Jose Olmo, and Majed Atwi. 2024. Deep Reinforcement Learning for
Portfolio Selection.Global Finance Journal62 (2024), 101016.
[17] Zhengyao Jiang, Dixing Xu, and Jinjun Liang. 2017. A Deep Reinforce-
ment Learning Framework for the Financial Portfolio Management Problem.
arXiv:1706.10059 [q-fin.ST]
[18] John L. Kelly. 1956. A New Interpretation of Information Rate.The Bell System
Technical Journal35, 4 (1956), 917–926.
[19] Zhipeng Liang, Hao Chen, Junhao Zhu, Kangkang Jiang, and Yanran Li.
2018. Adversarial Deep Reinforcement Learning in Portfolio Management.
arXiv:1808.09940 [q-fin.PM]
[20] Timothy P. Lillicrap, Jonathan J. Hunt, Alexander Pritzel, Nicolas Heess, Tom
Erez, Yuval Tassa, David Silver, and Daan Wierstra. 2015. Continuous Control
with Deep Reinforcement Learning. arXiv:1509.02971 [cs.LG]
[21] Xiao-Yang Liu, Ziyi Xia, Jiechao Rui, Jiechao Gao, Hongyang Yang, Ming Zhu,
Christina Dan Wang, Zhaoran Wang, and Jian Guo. 2022. FinRL-Meta: Market En-
vironments and Benchmarks for Data-Driven Financial Reinforcement Learning.
InAdvances in Neural Information Processing Systems, Vol. 35. 1835–1849.
[22] Xiao-Yang Liu, Hongyang Yang, Qian Chen, Runjia Zhang, Liuqing Yang, Bowen
Xiao, and Christina Dan Wang. 2020. FinRL: A Deep Reinforcement Learning
Library for Automated Stock Trading in Quantitative Finance. InDeep Reinforce-
ment Learning Workshop, NeurIPS.
[23] Xiao-Yang Liu, Hongyang Yang, Jiechao Gao, and Christina Dan Wang. 2021.
FinRL: Deep Reinforcement Learning Framework to Automate Trading in Quan-
titative Finance. InProceedings of the Second ACM International Conference on AI
in Finance. 1–9.
[24] Giorgio Lucarelli and Matteo Borrotti. 2020. A Deep Q-Learning Portfolio Man-
agement Framework for the Cryptocurrency Market.Neural Computing and
Applications32 (2020), 17229–17244.
[25] Sébastien Maillard, Thierry Roncalli, and Jérôme Teiletche. 2008. On the Proper-
ties of Equally-Weighted Risk Contributions Portfolios. Working paper.
[26] Harry Markowitz. 1952. Portfolio Selection.The Journal of Finance7, 1 (1952),
77–91.
[27] Robert C. Merton. 1971. Optimum Consumption and Portfolio Rules in a
Continuous-Time Model.Journal of Economic Theory3, 4 (1971), 373–413.
[28] Adrian Millea. 2021. Deep Reinforcement Learning for Trading–A Critical Survey.
Data6, 11 (2021), 119.
[29] Volodymyr Mnih, Koray Kavukcuoglu, David Silver, Andrei A. Rusu, Joel Veness,
Marc G. Bellemare, Alex Graves, Martin Riedmiller, Andreas K. Fidjeland, Georg
Ostrovski, et al . 2015. Human-Level Control Through Deep Reinforcement
Learning.Nature518, 7540 (2015), 529–533.
[30] John Moody and Matthew Saffell. 2001. Learning to Trade via Direct Reinforce-
ment.IEEE Transactions on Neural Networks12, 4 (2001), 875–889.
[31] John Moody, Lizhong Wu, Yuansong Liao, and Matthew Saffell. 1998. Perfor-
mance Functions and Reinforcement Learning for Trading Systems and Portfolios.
InAdvances in Neural Information Processing Systems, Vol. 11.
[32] Yuriy Nevmyvaka, Yi Feng, and Michael Kearns. 2006. Reinforcement Learning
for Optimized Trade Execution. InProceedings of the 23rd International Conference
on Machine Learning. 673–680.
[33] R. Tyrrell Rockafellar and Stanislav Uryasev. 2000. Optimization of Conditional
Value-at-Risk.The Journal of Risk2, 3 (2000), 21–41.
[34] John Schulman, Filip Wolski, Prafulla Dhariwal, Alec Radford, and Oleg Klimov.
2017. Proximal Policy Optimization Algorithms. arXiv:1707.06347 [cs.LG]
[35] William F. Sharpe. 1994. The Sharpe Ratio.The Journal of Portfolio Management
21, 1 (1994), 49–58.
[36] David Silver, Guy Lever, Nicolas Heess, Thomas Degris, Daan Wierstra, and
Martin Riedmiller. 2014. Deterministic Policy Gradient Algorithms. InProceedings
of the 31st International Conference on Machine Learning. 387–395.
[37] Frank A. Sortino and Lee N. Price. 1994. Performance Measurement in a Downside
Risk Framework.The Journal of Investing3, 3 (1994), 59–64.
[38] Richard S. Sutton and Andrew G. Barto. 2018.Reinforcement Learning: An Intro-
duction(2 ed.). MIT Press.
[39] Richard S. Sutton, David McAllester, Satinder Singh, and Yishay Mansour. 1999.
Policy Gradient Methods for Reinforcement Learning with Function Approxima-
tion. InAdvances in Neural Information Processing Systems, Vol. 12.
[40] Robert E. Whaley. 2009. Understanding the VIX.The Journal of Portfolio Man-
agement35, 3 (2009), 98–105.
[41] J. Welles Wilder. 1978.New Concepts in Technical Trading Systems. Trend
Research.
[42] Hongyang Yang, Xiao-Yang Liu, Shan Zhong, and Anwar Walid. 2020. Deep
Reinforcement Learning for Automated Stock Trading: An Ensemble Strategy.
InProceedings of the First ACM International Conference on AI in Finance. 1–8.
[43] Yunan Ye, Hengzhi Pei, Boxin Wang, Pin-Yu Chen, Yada Zhu, Jun Xiao, and
Bo Li. 2020. Reinforcement-Learning Based Portfolio Management with Aug-
mented Asset Movement Prediction States.Proceedings of the AAAI Conference
on Artificial Intelligence34, 01 (2020), 1112–1119.
