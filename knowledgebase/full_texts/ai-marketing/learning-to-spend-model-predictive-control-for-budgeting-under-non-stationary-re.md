---
title: 'Learning to Spend: Model Predictive Control for Budgeting under Non-Stationary Returns'
url: https://arxiv.org/abs/2604.27186
category: ai-marketing
subcategory: empirical
date: 2026-04
venue: ''
authors:
- Nilavra Pathak
- Smriti Shyamal
- Prasant Mhasker
- Christopher Swartz
source: arxiv
pdf_url: https://arxiv.org/pdf/2604.27186
pages: 8
chars: 38548
fetched_at: '2026-11-08T13:01:26+00:00'
kb_version: 1
---

# Learning to Spend: Model Predictive Control for Budgeting under Non-Stationary Returns

Learning to Spend: Model Predictive Control for
Budgeting under Non-Stationary Returns
Nilavra Pathak∗, Smriti Shyamal ∗, Prasant Mhasker †, Christopher Swartz †
∗Marketing Data Science, Expedia Group
† Department of Chemical Engineering, McMaster University
npathak@expediagroup.com∗, sshyamal@expediagroup.com∗, mhaskar@mcmaster.ca†, swartzc@mcmaster.ca†
Abstract—We study finite-horizon budget allocation as a
closed-loop economic control problem and evaluate receding-
horizon Model Predictive Control (MPC) relative to reactive
budgeting policies. Budgets are allocated periodically under exe-
cution noise and operational constraints, while return efficiency
may evolve over time. Using a controlled simulation framework
motivated by digital marketing, we compare reactive pacing
to MPC across environments with increasing degrees of non-
stationarity. Our results show that non-stationarity alone does not
justify predictive control. When return dynamics are stationary
or evolve through unpredictable stochastic drift, MPC offers
no systematic advantage over reactive baselines. By contrast,
when return efficiency exhibits predictable structure over the
planning horizon, that is captured through an underlying model,
MPC consistently outperforms reactive budgeting by exploiting
intertemporal trade-offs.
Index Terms—Marketing budget allocation; Model Predictive
Control (MPC); Budget pacing; Non-stationary enviroment;
Forecasting Response Functions.
I. INTRODUCTION
Marketing budgets are allocated periodically under uncer-
tainty, execution noise, and operational constraints. Planned
spend does not translate deterministically into realized expo-
sure or conversions due to auction dynamics, pacing systems,
and competitive effects. At the same time, the effectiveness of
spend may evolve over time as a result of market conditions,
saturation, or platform behavior. These features make budget
allocation a closed-loop decision problem with delayed and
noisy feedback. Solving these problems is critical for large
companies that manage multi-billion-dollar marketing budgets;
for example, Expedia Group increased its annual marketing in-
vestment to approximately $6.8 billion in 2024, and marketing
expense represents one of the largest operating cost categories
for online travel agents. Such scale underscores the practical
and economic importance of principled budget allocation and
pacing strategies in commercial deployments [1], [2].
A large literature focuses on estimating spend–return rela-
tionships from historical data, including marketing mix models
and related econometric approaches [3], [4]. These methods
provide interpretable response curves and remain widely used
in practice. However, they are fundamentally descriptive:
response functions are estimated offline and treated as fixed
inputs to downstream planning, despite the underlying envi-
ronment being non-stationary and affected by prior allocation
decisions. Building on these response estimation models, bud-
get allocation decisions are typically performed by constrained
optimization, either statically or through periodic re-solving
[5], [6], [7]. While effective for short-term or marketing
channel-level decisions, these approaches generally assume
stable response behavior over the planning horizon and do not
explicitly account for closed-loop adaptation under execution
noise.
Sequential decision-making frameworks based on reinforce-
ment learning and bandits relax these assumptions by opti-
mizing long-run performance [8], [9], [10]. However, such
methods often require large volumes of logged data, rely on
implicit policies, and involve exploration risk that is difficult to
justify in high-stakes, low-frequency budgeting settings such
as quarterly planning. A complementary perspective arises
from control theory. Classical models such as Nerlove–Arrow
and Vidale–Wolfe explicitly model advertising as a dynamical
system [11], [12]. While analytically appealing, their open-
loop solutions are highly sensitive to model assumptions and
do not naturally incorporate operational constraints, execution
noise, or repeated re-planning.
Model Predictive Control (MPC) addresses these limitations
by repeatedly solving a finite-horizon optimization problem
using updated system information while respecting constraints
[13], [14]. MPC has proven effective in domains characterized
by delayed feedback, uncertainty, and feasibility constraints,
making it a natural candidate for budget allocation problems.
Despite this alignment, it remains unclear when predictive
control meaningfully outperforms simpler reactive budgeting
heuristics. Non-stationarity alone does not guarantee gains
from receding-horizon optimization: when changes in return
efficiency are irregular or difficult to forecast, predictive
control may offer little advantage. Conversely, when non-
stationarity exhibits predictable structure over the planning
horizon, anticipatory allocation may unlock substantial im-
provements [15], [16].
In this paper, we study budget allocation through this
control-theoretic lens. Using marketing budget planning as
a motivating application, we compare reactive pacing strate-
gies against receding-horizon MPC under execution noise
and budget constraints, with the goal of characterizing when
predictive control improves closed-loop allocation outcomes.
Core contributions of the paper are:
•We formulate finite-horizon budget allocation as a con-
strained closed-loop control problem and apply receding-
horizon MPC to periodic budgeting decisions.
arXiv:2604.27186v1  [eess.SY]  29 Apr 2026

•We characterize the performance of predictive control
under different forms of non-stationarity, distinguishing
unpredictable drift from structured, forecastable variation.
•Simulation experiments demonstrate that MPC provides
value only when non-stationarity is predictable over the
planning horizon, and offers no advantage otherwise.
II. PROBLEMSETUP
We study finite-horizon budgeting as a closed-loop decision
problem in which a planner sets weekly spend targets and a
downstream execution layer converts those targets into realized
spend under uncertainty, reflecting modern digital advertising
delivery systems [7], [17], [18], [19], [20]. Time is discretized
in weeks over an evaluation quartert= 1, . . . , W(with
W= 12). At the start of weekt, the planner selects a planned
weekly budgetb t ≥0given the remaining budgetB rem t (with
Brem 1 =B Q andB rem t+1 =B rem t −s t). Realized spend is a
noisy actuation of the plan,
st =σ t(bt,Ω t) +ω t,(1)
whereΩ t captures exogenous market conditions andω t is
execution noise. Weekly return is generated from realized
spend via a nonlinear, saturating response with latent efficiency
parameters that may vary over time,
rt =ρ(s t;θ t) +ε t,(2)
whereε t is observation noise. The planner solves the finite-
horizon stochastic program
max
b1:W
E
" WX
t=1
rt
#
s.t.
WX
t=1
bt ≤B Q, b t ≥0,(3)
optionally with additional operational guardrails such as
bounded week-to-week budget changes to enforce stable spend
plans.
III. DATAGENERATIONPROCESS
We construct a synthetic marketing environment that gener-
ates both historical and evaluation data independently of any
control policy. The environment specifies (i) how quarterly
budgets are constructed, (ii) how planned budgets translate
into realized spend through a noisy execution layer, and (iii)
how realized spend produces returns via a latent nonlinear
response that may evolve over time. This separation ensures
that all policies are evaluated on identical underlying system
dynamics and that performance differences arise from control
logic rather than simulator bias.
A. Timeline and interaction loop
Time is measured in days, while control decisions are made
at a weekly cadence. Each trial consists of two contiguous
segments
•Historical period:Yyears of daily spend and return
observations, used to initialize policies (e.g., fitting initial
spend–return predictors for MPC). No data from the
evaluation period is used for initialization. This mirrors
common practice in marketing systems, where historical
logs are used to initialize planning models before budgets
are executed online.
•Evaluation period: one held-out quarter ofW= 12
weeks, during which policies interact with the environ-
ment in closed loop
Weeks are indexed byt∈ {1, . . . , W}and days within a
week byd∈ {1, . . . ,7}. At the start of weekt, a policy
selects a planned weekly budgetb t. The environment generates
realized daily spend{s t,d}7 d=1 and daily returns{r t,d}7 d=1,
which are aggregated to weekly totals
st =
7X
d=1
st,d, r t =
7X
d=1
rt,d.
Policies observe(s t, rt), update internal state, and proceed to
weekt+ 1. Within a trial, all policies face identical budgets,
constraints, and stochastic realizations (paired evaluation).
B. Budget construction
LetB (q) denote the evaluation-quarter budget. To ensure
realistic budget magnitudes without leaking future informa-
tion,B (q) is constructed using only the final year of the
historical period. Specifically, annual spend is computed from
historical data, perturbed by a stochastic year-over-year scaling
factor, and allocated across months using historical monthly
proportions; the quarterly budget is defined as the sum of
the corresponding three months. Full construction details are
provided in Appendix B.
C. Execution layer: noisy spend tracking
In real advertising platforms, realized spend deviates from
planned budgets due to auction outcomes, inventory con-
straints, and pacing logic [17], [18], [7]. We model this via
a noisy tracking process that maps weekly budgets to daily
spend. Let¯st =b t/7denote the nominal daily target. Daily
spend evolves as
st,d =s t,d−1 +α t

¯st −s t,d−1

+ξ t,d, d= 1, . . . ,7,(4)
whereα t ∈(0,1)is an adaptation (tracking) rate andξ t,d
is mean-zero delivery noise with variance proportional to the
target level. This execution layer induces realistic friction: even
identical plansb t yield stochastic realized spends t, which
affects both reactive and predictive controllers.
D. Return layer: latent nonlinear response
Returns are generated from realized spend via a nonlinear,
saturatingRichards-type response curve[21], which general-
izes exponential saturation by allowing asymmetric curvature
and variable saturation rates. This choice reflects empirical ev-
idence that advertising response curves deviate systematically
from simple exponential forms [22]. Daily returns satisfy
rt,d =ρ Richards

st,d;θ t

+ε t,d,(5)
whereθ t are time-varying parameters governing scale and
elasticity, andε t,d captures observation noise.

For control, MPC deliberately assumes a simpler
exponential-saturation response model. This intentional
functional misspecification isolates the role ofpredictability
in latent efficiencyrather than estimator fidelity: any
performance gains must arise from forecasting structure inθ t,
not from matching the true response shape. Unless otherwise
stated, the same environment class generates both historical
and evaluation data.
E. Operating regimes
We study threeoperating regimesthat differ in the pre-
dictability of return efficiency over the planning horizon
1)Static (stationary) regime.Parameters are fixed during
evaluation, withθ t =θandα t =α. Outcomes remain
noisy, but the underlying response and execution dynam-
ics do not drift.
2)Random-walk drift regime.Return efficiency evolves
smoothly but stochastically
logθ t+1 = logθ t +η t, η t ∼ N(0, σ2 η),(6)
whereη t is the random-walk innovation. Execution dy-
namics may also drift analogously throughα t. This
regime captures non-stationarity without exploitable pe-
riodic structure and primarily rewards adaptive tracking.
3)Seasonality-driven predictable decline regime.To con-
struct settings where intertemporal allocation decisions
matter, we introduce a repeatableweek-of-quarter ef-
ficiency factorg(w), wherew∈ {1, . . . ,12}indexes
the week within the quarter. The factorg(w)captures
systematic within-quarter declines in return efficiency and
is defined as
g(w) = exp(−δw), δ >0.(7)
The effective spend–return relationship in weekwis then
ρw(s;θ) =g(w)ρ(s;θ).(8)
Because this efficiency pattern repeats across quarters, it
is identifiable from historical data and can be exploited
by forward-looking control policies.
IV. BUDGETALLOCATION: CONTROLSTRATEGIES
We study how a fixed quarterly budget should be allocated
across weeks to maximize cumulative return in the presence
of (i)execution noise, where planned budgets do not trans-
late deterministically into realized spend, and (ii)operational
guardrails, such as smooth week-to-week budget changes. We
compare two policies: a reactive pacing baseline that relies
only on budget accounting, and a receding-horizonModel
Predictive Control(MPC) allocator that combines a control-
facing forward model (prediction module) with constrained
planning (optimization module). Both policies are evaluated
under the operating regimes in Section III-E.
A. Baseline: Reactive Weekly Pacing with Carryover
As a non-predictive reference, we consider a reactive pacing
strategy that allocates budget based solely on remaining funds
and time, without modeling or forecasting return efficiency.
This class of strategies is widely used in practice as a
feasibility-oriented approach to budget delivery under execu-
tion uncertainty.
The baseline operates at a weekly cadence and consists of
two steps: (i) defining nominal weekly targets using historical
pacing ratios, and (ii) updating these targets via carryover
based on realized spend.
a) Phase 1 (weekly targets from historical ratios).:
LetB Q denote the total quarterly budget and letWdenote
the number of weeks in the quarter. We define a set of
historical weekly pacing ratios{π 1, . . . , πW }, whereπ t ≥0
and PW t=1 πt = 1. Eachπ t represents the fraction of total
spend historically allocated to weekt, computed from the
previous year’s spend pattern over the same quarter (or a
comparable reference period). The nominal weekly budget is
defined as
B(0) t =π t BQ, t= 1, . . . , W.(9)
If historical ratios are unavailable, we use a uniform fallback
πt = 1/W.
b) Phase 2 (weekly carryover).:LetB rem t denote the
remaining budget at the start of weekt, initialized asB rem 1 =
BQ. To account for under- or over-delivery in previous weeks,
the planned weekly budget is computed by rescaling the
remaining budget according to the remaining pacing ratios:
bt =B rem t · πt PW
j=t πj
.(10)
After execution of weekt, the environment produces realized
spends t, and the remaining budget is updated via
Brem t+1 =B rem t −s t,(11)
so that any surplus or deficit is automatically carried forward
and absorbed into the remaining weeks.
Key property.The baseline is purely reactive: weekly
budgets depend only on historical pacing ratios, realized
spend, and remaining time, and do not use forecasts of future
return efficiency. It therefore provides a strong benchmark for
feasibility and budget utilization, but cannot exploit predictable
temporal structure in returns.
B. Model Predictive Control (MPC): Prediction and Opti-
mization
MPC treats budgeting as a receding-horizon control prob-
lem. At each weekτ, it (i) generates horizon forecasts of
realized spend and return under candidate budgets, (ii) solves
a constrained finite-horizon planning problem, (iii) executes
only the first weekly budget, and (iv) repeats after observing
realized spend and return. We explicitly separate
1)Prediction module: a control-facing forward model pro-
ducingbst(·)andbr t(·)over the horizon

2)Optimization module: a constrained planner that maps
forecasts into implementable weekly budgets under
guardrails
1) Optimization module (finite-horizon planning):At week
τ, MPC selects a horizon-Hbudget sequenceb τ:τ+H−1 =
{bτ , . . . , bτ+H−1 }by solving
max
bτ:τ+H−1
H−1X
h=0
brτ+h

bτ+h ; bθτ+h|τ

(12)
s.t.
H−1X
h=0
bsτ+h

bτ+h

≤B rem τ ,(13)
bτ+h ≥0, h= 0, . . . , H−1,(14)
(1−γ L)bτ+h−1 ≤b τ+h ≤(1 +γ U )bτ+h−1 .
(15)
The objective (12) maximizes predicted cumulative return
over the planning horizon using the control-facing forward
model. The budget constraint (13) enforces feasibility with
respect to the remaining quarter budgetB rem τ =B Q−P t<τ st
based on realized spend, and is written as an inequality to
accommodate execution frictions. Constraints (14)–(15) en-
force nonnegativity and impose a relative smoothness guardrail
that limits week-to-week changes in planned spend,γ L and
γU provides the lower and upper percentage change bounds.
MPC operates in receding horizon by applying the first action
bmpc τ =b ⋆ τ , observing realized spend and return(s τ , rτ ),
updating forecasts, and re-solving (12)–(15) atτ←τ+ 1.
Oracle vs. Estimated MPC:To disentangle the value of
receding-horizon planning from the limits of prediction, we
evaluate two MPC variants. We define them as follows:
1)Oracle MPC:forms the predicted return modelbr t(·)
using the simulator’s true latent stateθ t and the true
generating functional form. This provides an upper-bound
on the results.
2)Learned MPC:formsbr t(·)using parameter estimates
bθt|τ computed from historical data and accrued on-
line observations under the regime-specific estimation
procedures, together with the assumed functional form
in IV-B2.
2) Prediction module (nominal nonlinear spend–return
model):Returns are modeled as a nonlinear saturating func-
tion of realized spend with latent parametersθ t that may
evolve over time. As a nominal model, we use exponential
saturation withθ t = (ρ max,t, κt), whereρ max,t >0is the
saturation return andκ t >0controls the rate of saturation.
For realized spends≥0,
ρ(s;θ t) =ρ max,t

1−e −κts .(16)
The return predictor supplied to the optimization module is
brt

b; bθt|τ  =ρ  bst(b); bθt|τ  ,(17)
which makes the role of predictability explicit: MPC can
only outperform reactive pacing when the forecast sequence
{bθτ+h|τ }H−1 h=0 contains exploitable structure over the planning
horizon.
a) Implicit saturation spend:Define theη-saturation
spends η as the spend required to reach a fractionη∈(0,1)
of the saturation return,ρ(s η;ρ max,t, κt) =η ρ max,t, which
yields
sη(ρmax,t, κt) =− 1 κt log(1−η).(18)
3) Forecastingθ t across operating regimes:The regimes
in Section III-E differ only in how the prediction module
constructs the horizon forecasts bθτ+h|τ used in (12).
R1: Static:Estimate a single response curve on historical
data and hold parameters fixed within the quarter
bθτ+h|τ = bθτ|τ , h= 0, . . . , H−1.(19)
R2: Random-walk drift regime (PF-MPC):In this
regime latent return efficiency evolves stochastically with
no exploitable periodicity. MPC therefore relies onadaptive
tracking rather than forecasting. We implement this using a
particle-filter-based MPC (PF-MPC), where a latent efficiency
state is updated sequentially under a log-space random-walk
assumption and treated as locally persistent over the planning
horizon. The particle filter is updated once per week using
realized spend–return observations, and MPC replans using the
current posterior mean state without assuming future structure.
R3: Forecastable seasonal dynamics:When latent pa-
rameter trajectories exhibit repeatable structure such as trends
or seasonality, we explicitly forecast them. Time-series pre-
dictors are fit to identified parameter sequences (after suitable
transformation, e.g., log space) and extrapolated over the
MPC horizon. For parametersθ t = (ρmax,t, κt), we generate
forecasts
ρmax,t+h =f ρ

{ρmax,τ }τ≤t , h

,(20)
κt+h =f κ

{κτ }τ≤t , h

,(21)
for horizonsh∈ {1, . . . , H}. In practice, we employ SARI-
MAX models to capture both autoregressive structure and
seasonal effects in parameter evolution. When returns exhibit
systematic within-quarter decline, accurate forecasting enables
MPC to anticipate future conditions and allocate budget
proactively rather than reactively. These forecasts are supplied
to (17) and optimized via (12)–(15).
V. EXPERIMENTALSETUP
All experiments are conducted in the synthetic marketing
system defined in Section III. Unless otherwise stated, all
environment dynamics, noise processes, operating regimes,
and budget construction procedures follow that section exactly.
The experimental setup below specifies only the evaluation
protocol and statistical reporting.
A. Evaluation protocol
Each trial consists of a historical period used solely for
policy initialization, followed by a held-out evaluation quarter
ofW= 12weeks. During the evaluation period, policies
interact with the system in closed loop and select weekly
budgets based only on past realized observations. Within each
trial, all policies are evaluated under identical initial conditions
and stochastic realizations (paired evaluation).

B. Evaluation metrics
To enable comparison across budgets and operating regimes
without reporting absolute monetary values, we reportmean
returns in oracle-normalized form. LetR oracle denote the total
return achieved by the oracle allocation under a given trial
realization. For any policyπ, we define the oracle-normalized
return
eRπ = Rπ
Roracle .(22)
By construction, eRoracle = 1. We reportE[ eRπ]as a scale-free
summary of average performance.
In addition,performance differencesare computed on the
original return scale on a per-trial basis and reported as
percentages. Specifically, for each trial we compute:
∆π base = 100· Rπ −R base Rbase ,(23)
Gapπ oracle = 100· Roracle −R π Roracle .(24)
Confidence intervals for∆ π base andGap π oracle are obtained
from their empirical distributions across trials using a paired
design.
We report the following control-oriented metrics:
•Normalized return (mean):E[ eRπ]
•Budget utilization: PW t=1 st / B(q)
•Improvement over baseline (%):∆ π base with 95% con-
fidence intervals
•Oracle gap (%):Gap π oracle with 95% confidence inter-
vals
C. Monte Carlo evaluation
Each configuration is evaluated overNindependent trials.
For each trial, all policies share the same historical data and
the same evaluation realization. We report the mean and 95%
confidence intervals for∆using both a pairedt-interval and
a nonparametric bootstrap. Statistical significance is assessed
using a pairedt-test on per-trial return differences.
VI. EXPERIMENTALRESULTS
We evaluate reactive budgeting and receding-horizon Model
Predictive Control (MPC) under increasingly structured forms
of non-stationarity. Our objective is not to compare estimation
accuracy in isolation, but to determinewhen predictive control
materially improves closed-loop allocation performance. All
results are computed using paired Monte Carlo evaluation un-
der identical budgets, constraints, and stochastic realizations.
We organize the analysis around three research questions:
RQ1.In astatic, time-invariantresponse regime, do reac-
tive and predictive controllers achieve equivalent perfor-
mance under identical constraints?
RQ2.When latent response parameters evolve as a stochastic
random walk without forecastable structure, can predic-
tive control outperform reactive adaptation?
RQ3.When latent parameters exhibit learnable seasonal or
trend structure, under what conditions does MPC exploit
forecasts to reduce regret relative to myopic policies?
A. RQ1: Static Regime Sanity Check
Key finding:MPC provides no meaningful advantage in
static environments.In stable, time-invariant spend–return
regimes with no exploitable temporal structure, reactive pacing
heuristics and receding-horizon MPC converge to equivalent
uniform allocations under identical constraints. Because there
is no predictability to exploit, MPC’s forecasting and looka-
head capabilities do not translate into improved closed-loop
performance. Detailed results are reported in Appendix C.
B. RQ2: Stochastic Drift Without Predictability
We next examine regimes in which return efficiency evolves
over time but lacks exploitable temporal structure. Latent
response parameters follow a stochastic random walk in log
space,
logθ t+1 = logθ t +η t, η t ∼ N(0, σ2 rw),(25)
producing smooth yet intrinsically unpredictable dynamics
beyond the current state. This regime isolatesadaptation
fromanticipation: parameters drift, but there is no repeatable
structure that a predictive controller can reliably exploit over
the planning horizon.
We compare a particle-filter-based MPC (PF-MPC) against
the reactive baseline under two levels of drift intensity:mild
(σrw ∈[0.02,0.03]) andmoderate(σ rw ∈[0.05,0.08]). Mean
returns are reported in oracle-normalized form to remove scale
effects, while performance gaps and confidence intervals are
computed on the original per-trial return scale and reported as
percentages.
Key findings:
•No gain from prediction without predictability.PF-
MPC underperforms the reactive baseline under both drift
intensities, with mean performance gaps on the order
of0.3–0.4%, despite both policies fully exhausting the
available budget.
•Limits of adaptive tracking.While PF-MPC adapts
to local parameter changes, model misspecification and
tracking error lead to conservative allocations that forgo
upside relative to reactive pacing.
•Downside mitigation in difficult realizations.PF-MPC
outperforms the baseline in a nontrivial fraction of trials,
primarily when baseline performance is poor. This indi-
cates that adaptivity can reduce downside risk even when
it does not deliver consistent average gains.
•Oracle gap reflects missing predictability.The oracle
gap increases with drift intensity, revealing substantial
theoretical headroom that cannot be realized in the ab-
sence of forecastable temporal structure.
Interpretation:In stochastic drift regimes, efficiency fluc-
tuations average out over the planning horizon, leaving little
structure for anticipatory control. As a result, receding-horizon
MPC effectively collapses to a re-optimized reactive policy.
Time variation alone is therefore insufficient for long-horizon
gains; predictive control requires predictable structure to de-
liver systematic improvements.

Table I: Performance under stochastic random-walk drift.
Mean returns are reported relative to the oracle allocation.
Percentage improvements and oracle gaps are computed on
the original return scale.
Drift Strength Baseline PF-MPC PF-MPC Improve. Oracle Gap
Mild 0.696 0.694−0.38% +45.2%
[−0.48,−0.28]% [41.9,48.5]%
Moderate 0.678 0.675−0.31% +51.9%
[−0.53,−0.08]% [46.8,57.1]%
C. RQ3: Predictable Seasonal Dynamics
We finally consider regimes in which return efficiency
exhibits a repeatable within-quarter decline, capturing effects
such as ad fatigue or lifecycle decay. LetL t denote the
multiplicative return-efficiency level in weekt, withL 0 >0
representing the initial efficiency at the start of the quarter.
Efficiency evolves deterministically according to
Lt =L 0(1−δ) t,(26)
whereδ∈ {0.05,0.10,0.15,0.20}controls the rate of within-
quarter decline, spanning weak to strong seasonal structure.
Because this pattern repeats across quarters, it is identifiable
from historical data and forecastable by forward-looking con-
trol policies.
Mean total returns are reported in oracle-normalized form
for scale-free comparison. Performance improvements relative
to the baseline and oracle gaps are computed on the original
per-trial return scale and reported as percentages with 95%
confidence intervals.
Key findings:
•Threshold behavior.MPC underperforms reactive pac-
ing under weak seasonality (δ= 5%), but consistently
outperforms the baseline once the decline exceeds ap-
proximatelyδ≈10%.
•Scaling with predictability.Performance gains increase
sharply with the strength of seasonal structure, indicat-
ing that intertemporal reallocation becomes increasingly
valuable as predictability strengthens.
•Intertemporal allocation mechanism.MPC shifts spend
toward earlier, higher-efficiency weeks, while the baseline
spreads spend uniformly and incurs increasing opportu-
nity cost as decline intensifies.
•High efficiency relative to the oracle.Across all decline
rates, MPC captures the majority of the achievable gains.
The oracle gap remains stable and modest, indicating
that operational smoothness constraints—not forecasting
limitations—are the dominant bottleneck.
a) Interpretation.:Predictable seasonal decline provides
a stable forecast signal that enables effective long-horizon
planning. MPC exploits this structure by reallocating spend
toward earlier, higher-efficiency periods, yielding increasing
gains as seasonality strengthens. The stable and modest oracle
gap across all decline rates indicates that under the imposed
±20%smoothness constraints, MPC already captures most of
the theoretically achievable benefit from predictability. Further
Table II: Performance under predictable seasonal decline.
Mean returns are reported relative to the oracle allocation.
Percentage improvements and oracle gaps are computed on
the original return scale.
δBaseline MPC MPC Improve. 95% CI Oracle Gap
5% 0.972 0.939−3.2% [−3.53,−2.92]% +6.0%
10% 0.905 0.933+4.2% [3.98,4.38]% +6.9%
15% 0.852 0.931+11.2% [10.68,11.72]% +7.2%
20% 0.808 0.944+14.0% [13.13,14.89]% +6.8%
gains would therefore require relaxing operational constraints
rather than improving forecasting accuracy.
Interpretation:Predictable seasonal decline provides a
stable forecast signal that enables effective long-horizon plan-
ning. MPC exploits this structure by reallocating spend toward
earlier, higher-efficiency periods, yielding increasing gains as
the strength of seasonality increases. The consistently mod-
est oracle gap across all decline rates, together with tight
confidence intervals, indicates that under the imposed±20%
smoothness constraints MPC already captures most of the
theoretically achievable benefit from predictability. Further
gains would therefore require relaxing operational constraints
rather than improving forecasting accuracy.
VII. CONCLUSION
This work studies dynamic system identification for mar-
keting spend–return processes, emphasizing the role of iden-
tifiable temporal structure in enabling predictive optimization
rather than fitting static response curves. Through simulation
under execution noise, parameter drift, and model misspecifi-
cation, we show that state-space identification can approximate
the data-generating process and narrow the gap between real-
ized and oracle behavior, with MPC gains emerging only when
predictable dynamics are present. The experimental scope is
intentionally constrained, focusing on a controlled form of
seasonality and simplified assumptions such as homoskedastic
Gaussian noise and limited latent-state structure. Extending
this framework to richer identification choices—including
alternative state parameterizations, non-Gaussian and het-
eroskedastic noise, regime shifts, and more complex seasonal
patterns—remains an important direction for future work and
is necessary to fully characterize when improved identification
fidelity translates into actionable control value in realistic
budget planning settings.
REFERENCES
[1] Expedia Group, Inc. Expedia group, inc. form 10-k annual
report. https://www.sec.gov/ixviewer/documents/20240208/
0001637459-24-000014.xhtml, 2024. Accessed via U.S. SEC
EDGAR.
[2] Expedia Group, Inc. Expedia group, inc. form 10-q quarterly re-
ports. https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&
CIK=0001637459&type=10-Q, 2024. Accessed via U.S. SEC EDGAR.
[3] Dominique M. Hanssens, Leonard J. Parsons, and Randall L. Schultz.
Market Response Models: Econometric and Time Series Analysis.
Springer, 2003.
[4] Marnik G. Dekimpe and Dominique M. Hanssens. The persistence of
marketing effects on sales.Marketing Science, 14(1):1–21, 1995.

[5] Daisuke Hatano, Takuro Fukunaga, Takanori Maehara, and Ken-ichi
Kawarabayashi. Lagrangian decomposition algorithm for allocating
marketing channels. InProceedings of the AAAI Conference on Artificial
Intelligence, 2015.
[6] Virginia Luzon. Dynamic budget allocation in social media advertising
campaigns.European Journal of Operational Research, 298(1):327–
341, 2022.
[7] Qingpeng Zhao, Yu Liu, Wenyu Wei, Wei Chen, and Jun Wang. A
unified framework for advertising bidding and budget allocation. In
Proceedings of the 25th ACM SIGKDD International Conference on
Knowledge Discovery & Data Mining, pages 2185–2194, 2019.
[8] Nikolay Archak, Vahab Mirrokni, and Shanmugavelayutham Muthukr-
ishnan. Budget optimization for online campaigns with positive car-
ryover effects. InInternational Workshop on Internet and Network
Economics, pages 86–99. Springer, 2012.
[9] Hongyi Cai, Wei Chen, and Jun Wang. Budget-constrained marketing
optimization via automated bidding. InProceedings of the 29th ACM
SIGKDD Conference on Knowledge Discovery and Data Mining, 2023.
[10] Ziang Yan, Shusen Wang, Guorui Zhou, Jingjian Lin, and Peng Jiang. An
end-to-end framework for marketing effectiveness optimization under
budget constraint.arXiv preprint arXiv:2302.04477, 2023.
[11] Marc Nerlove and Kenneth J. Arrow. Optimal advertising policy under
dynamic conditions.Economica, 29(114):129–142, 1962.
[12] Suresh P. Sethi. Optimal control of the vidale–wolfe advertising model.
Operations Research, 21(4):998–1013, 1973.
[13] Manfred Morari and Jay H. Lee.Model predictive control: past, present
and future. Elsevier, 1999.
[14] James B. Rawlings, David Q. Mayne, and Moritz Diehl.Model Predic-
tive Control: Theory, Computation, and Design. Nob Hill Publishing,
2nd edition, 2017.
[15] Yingying Li, Xin Chen, and Na Li. Online optimal control with linear
dynamics and predictions: Algorithms and regret analysis.Advances in
Neural Information Processing Systems, 32, 2019.
[16] Chenkai Yu, Guanya Shi, Soon-Jo Chung, Yisong Yue, and Adam
Wierman. The power of predictions in online control.Advances in
Neural Information Processing Systems, 33:1994–2004, 2020.
[17] Ye Chen, Pavel Berkhin, Bo Anderson, and Nikhil R Devanur. Real-
time bidding algorithms for performance-based display ad allocation.
InProceedings of the 17th ACM SIGKDD international conference on
Knowledge discovery and data mining, 2011.
[18] Hongyi Cai, Kan Ren, Weinan Zhang, Kleanthis Malialis, Jun Wang,
Yong Yu, and Dawei Guo. Real-time bidding by reinforcement learning
in display advertising. InProceedings of the Tenth ACM International
Conference on Web Search and Data Mining, pages 661–670, 2017.
[19] Deepak Agarwal et al. Budget pacing for targeted online advertisements
at linkedin. InProceedings of the 20th ACM SIGKDD international
conference on Knowledge discovery and data mining, pages 1613–1619,
2014.
[20] Santiago R Balseiro, Kshipra Bhawalkar, Zhe Feng, Haihao Lu, Vahab
Mirrokni, Balasubramanian Sivan, and Di Wang. A field guide for pacing
budget and ros constraints.arXiv preprint arXiv:2302.08530, 2023.
[21] Francis J Richards. A flexible growth function for empirical use.Journal
of experimental Botany, 10(2):290–301, 1959.
[22] Jing Wang, Chris Swartz, Kai Huang, Smriti Shyamal, Roopesh Ranjan,
Dan Friedman, and Joel Brooks. Data-driven budget allocation optimiza-
tion for digital marketing. InProceedings of the 65th Annual Canadian
Operational Research Society Conference, London, Ontario, 2024.
APPENDIXA
IMPLEMENTATIONDETAILS
The optimization problem (12)–(15) is a small nonlinear
program solved on a weekly cadence using standard solvers
(e.g., CasADi/IPOPT). All results report end-to-end closed-
loop performance. Forecasting components are not tuned in
isolation; identification quality is evaluated solely through its
downstream impact on control outcomes.
APPENDIXB
BUDGETCONSTRUCTIONDETAILS
Let{s d}D d=1 denote daily realized spend in the final year
of the historical period, whereDis the number of days in
that year under the simulation discretization. Annual spend is
computed as
Syear =
DX
d=1
sd.(27)
To introduce realistic year-over-year variation without in-
corporating any information from the evaluation period, we
apply a multiplicative scaling factorλ∼ Dλ, yielding a scaled
annual budget
eSyear =λ Syear.(28)
Monthly allocation proportions{ρ m}12 m=1 are estimated
from historical data as
ρm = Hm P12
j=1 Hj
,(29)
whereH m denotes total spend in monthmof the historical
year. The budget assigned to monthmis then
Bm =ρ m eSyear.(30)
For an evaluation quarterq⊂ {1, . . . ,12}consisting of
three consecutive months, the quarterly budget is defined as
B(q) = X
m∈q
Bm.(31)
All allocation policies are initialized using historical data
only and make decisions during the evaluation quarter based
exclusively on past realized spend and return observations, en-
suring a strict separation between initialization and evaluation.
APPENDIXC
RQ1 DETAILS: STATIC(STATIONARY) ENVIRONMENT
We first consider a static regime in which the spend–return
relationship is time-invariant over the evaluation horizon. In
this setting, response parameters can be consistently estimated
from historical data, and under concave returns the optimal
feasible allocation is approximately uniform across time, up to
budget feasibility and smoothness constraints. In the absence
of predictable temporal variation, receding-horizon planning
offers no strategic advantage over reactive pacing.
Consistent with this expectation, MPC and the baseline
achieve nearly identical performance when evaluated relative
to the oracle benchmark. Table III reports oracle-normalized
mean returns, defined as the ratio of cumulative return
achieved by a policy to that of the oracle allocation under
identical realizations. By construction, the oracle attains a
normalized return of one. Both MPC and the baseline lie
within approximately0.5%of this upper bound.
Performance differences are small and statistically signifi-
cant only due to constraint friction and forecast noise rather
than anticipatory reallocation. The oracle gap is negligible,
confirming that even perfect foresight provides little benefit

in static environments. Both MPC and the oracle operate
under identical quarterly budget constraints and±30%relative
smoothness limits, which restrict aggressive back-loading even
when the true response function is known. As a result, looka-
head optimization does not improve outcomes over reactive
pacing when no exploitable temporal structure is present.
Table III: Allocator performance in the static regime. Mean
returns are reported relative to the oracle allocation.
Percentage improvements and oracle gaps are computed on
the original return scale.
Strategy Normalized Return 95% CI Improvement Oracle Gap
Baseline 1.000[0.986,1.014]—+0.00%
MPC 0.997[0.981,1.011]−0.37% +0.34%
