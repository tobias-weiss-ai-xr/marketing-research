---
title: 'ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading'
url: https://arxiv.org/abs/2609.13825
category: ai-marketing
subcategory: empirical
date: 2026-09
venue: ''
authors:
- Asser Moustafa
- Rares-Mihail Neagu
- Jugal Kalita
source: arxiv
pdf_url: https://arxiv.org/pdf/2609.13825
pages: 7
chars: 37194
fetched_at: '2026-11-08T13:20:28+00:00'
kb_version: 1
---

# ViperQ: Order Flow Pattern Recognition via Auction Market Theory for Reinforcement Learning Trading

ViperQ: Order Flow Pattern Recognition via
Auction Market Theory for Reinforcement Learning Trading
Asser Moustafaa,∗, Rares-Mihail Neagub, Jugal Kalitaa
aDepartment of Computer Science, University of Colorado, Colorado Springs, 1420 Austin Bluffs Pkwy, Colorado Springs, CO 80918, USA
bDepartment of Computer Science, University of Iowa, 101 Jessup Hall, Iowa City, IA 52242, USA
Abstract
Reinforcement learning trading systems published in the academic literature overwhelmingly rely on price-aggregate state repre-
sentations (OHLCV bars) or limit-order-book depth features, leaving microstructure pattern theories from the practitioner literature,
namely Auction Market Theory and Market Profile, without a peer-reviewed computational instantiation. We presentViperQ, a
reinforcement learning system whose state representation is built explicitly from Auction Market Theory primitives: V olume Point
of Control, Value Area position, Low V olume Node flags, Cumulative V olume Delta divergence, and tape-velocity signatures,
assembled into a 20-dimensional Z-normalised vector. Two Proximal Policy Optimisation agents are trained with a prospect-
theory-grounded asymmetric reward function that penalises losing holds at a magnitude consistent with Kahneman and Tversky’s
loss-aversion coefficient. Evaluated on a held-out twelve-month partition of institutional tick data the agents have never seen,
ViperQ achieves+163.6% ROI on TSLA (−27.5% max drawdown, 27,019 trades) and+116.5% ROI on NVDA (−47.8% max
drawdown, 12,892 trades) under zero leverage. The results establish Auction Market Theory features as a tractable structured input
modality for sequential decision-making on financial time series and motivate further work on microstructure-aware policy learning.
Keywords:Reinforcement learning, Pattern recognition, Time-series classification, Sequential decision-making, Order flow,
Market microstructure
1. Introduction
The application of deep reinforcement learning (RL) to fi-
nancial decision-making has expanded rapidly over the past
five years [1, 2], with documented systems spanning portfo-
lio rebalancing [3, 4], optimal trade execution [5, 6, 7], market
making [8, 9], and directional high-frequency trading [10, 11].
Across this body of work, the choice of state representation has
been remarkably homogeneous. Systems either consume price-
aggregate features (open-high-low-close bars, returns, volatil-
ity, technical indicators) or, when operating at higher resolution,
consume raw limit-order-book (LOB) depth snapshots [12, 13].
A parallel tradition reads the same data through the lens of
market microstructure theory: price discovery is the outcome
of strategic interaction between informed and uninformed or-
der flow [14], market makers update quotes to reflect the in-
formation content of incoming orders [15], and the resulting
microstructure dynamics determine when and how prices tran-
sition between equilibria [16, 17]. Within this microstruc-
ture framing, Steidlmayer’s Market Profile [18] and Dalton’s
Auction Market Theory [19] (AMT) operationalise two repeat-
able microstructure regimes that have been widely adopted
in proprietary-trading practice:balancestates (mean-reverting
∗Corresponding author.
Email addresses:amoustaf@uccs.edu(Asser Moustafa),
rneagu@uiowa.edu(Rares-Mihail Neagu),jkalita@uccs.edu(Jugal
Kalita)
consensus on fair value) andimbalancestates (one-sided liquid-
ity vacuums driving price discovery to a new equilibrium). De-
spite three-and-a-half decades of practitioner adoption, this mi-
crostructure pattern theory has not, so far as exhaustive search
of arXiv, Semantic Scholar, IEEE Xplore, ACM Digital Li-
brary, and ScienceDirect can determine, been instantiated as a
state representation for a peer-reviewed reinforcement learning
trading agent.
This paper closes that gap. We presentViperQ, to the best
of our knowledge, the first peer-reviewed reinforcement learn-
ing trading system whose state representation is built explic-
itly from Steidlmayer–Dalton Auction Market Theory primi-
tives. The state representation encodes V olume Point of Con-
trol (VPOC), Value Area boundaries, Low V olume Node flags,
Cumulative V olume Delta divergence, tape velocity, and order-
flow imbalance as a 20-dimensional Z-normalised vector that
is consumed directly by a Proximal Policy Optimisation [20]
agent operating at 1-second resolution on institutional tick data.
The framing of the problem is, deliberately, a pattern recog-
nition framing rather than a financial-engineering framing. The
classifier-equivalent task is the binary recognition ofbalance
versus imbalanceregimes from a stream of microstructure ob-
servations, with sequential policy learning conditional on that
recognition. The contribution we believe to be of broadest inter-
est to the pattern recognition community is therefore the struc-
tured state representation itself: a demonstration that a body
of practitioner pattern theory, encoded explicitly rather than
learned end-to-end, yields a state space on which a small neu-
arXiv:2609.13825v1  [cs.AI]  12 Sep 2026

ral policy can converge to substantial out-of-sample profit. The
trading-domain application is, in this view, downstream of the
methodological point.
We summarise our contributions as follows.
•Auction-Market-Theory state representation.We de-
fine and operationalise a 20-dimensional state vectors t∈
R20 whose physics-derived components (VPOC, Value
Area position, Low V olume Node flags, CVD divergence,
tape velocity, order-flow imbalance) are direct computa-
tional analogues of constructs first formalised by Steidl-
mayer [18] and Dalton et al. [19]. To the best of our
knowledge, no prior peer-reviewed RL trading agent has
used this feature family as state input.
•Prospect-theory-grounded reward shaping.The Sniper
reward function applies asymmetric pain penalties con-
sistent with Kahneman and Tversky’s loss-aversion co-
efficient [21, 22], augmented by a synthetic in-training
transaction-fee inflation that forces the agent toward high-
conviction setups rather than micro-scalping.
•Asset-specific behavioural divergence.We show that a
single architecture, trained with two reward-function con-
figurations, converges to two distinct profitable policies (a
high-frequency scalper for TSLA and a trend-following
risk-averse agent for NVDA), demonstrating that asset-
specific reward shaping yields different and individually
profitable local optima from the same underlying state rep-
resentation.
•Out-of-sample empirical validation.On a strictly held-
out 12-month test partition, ViperQ produces+163.6%
ROI on TSLA and+116.5% ROI on NVDA with zero
leverage and regulatory-fee accounting. These figures lie
above the typical range surveyed by Pippas et al. [2], at
the cost of materially deeper drawdowns than conservative
portfolio-rebalancing systems (Section 6).
The remainder of the paper is organised as follows. Sec-
tion 2 situates ViperQ against the deep-learning-on-LOB and
RL-trading literature. Section 3 formalises the state represen-
tation, the reward function, and the dual-PPO training strategy.
Section 4 describes the risk-bounded execution layer. Section 5
details the experimental protocol; Section 6 presents results and
the comparison with prior systems. Section 7 states the limita-
tions of the present work, and Section 8 concludes.
2. Related Work
Deep learning on limit order books.The DeepLOB archi-
tecture [12] established convolutional networks as the canoni-
cal baseline for mid-price prediction from raw LOB snapshots,
and has been extended to transformer architectures (LiT [13])
and to multi-asset attention models. These systems treat the or-
der book as a structured but unannotated time series and learn
features end-to-end; they do not encode prior microstructure
theory and they typically operate as classifiers rather than as
control agents.
Reinforcement learning for trading and execution.A sec-
ond strand applies RL directly to trading or execution decisions.
Zhang et al. [11] compared DQN, policy-gradient, and A2C
agents on 50 futures contracts at daily resolution. Théate and
Ernst [23] introduced TDQN for daily equity trading. Yang et
al. [3] demonstrated an ensemble of PPO, A2C and DDPG on
the Dow 30 with daily rebalancing. Liu et al. [4] released the
FinRL library, which standardised much of the subsequent lit-
erature. At higher frequency, Briola et al. [10] trained PPO on
Intel LOB events; Lin and Beling [5] produced an end-to-end
PPO execution agent on Level-2 data; Hafsi and Vittori [6] and
Espana et al. [7] continue this line into queue-reactive simula-
tion environments. Coletta et al. [24] provided conditional gen-
erators for LOB environments; Wang et al. [8, 25, 9] addressed
RL market making. Two contemporary surveys [1, 2] catalogue
the field; Pippas et al. critically evaluate 167 publications and
identify microstructure-feature integration as a methodological
gap.
Microstructure-feature work.Jaddu and Bilokon [26]
combine deep-learning representations of order books with RL
using Order Flow Imbalance features in the sense of [27]. To
our knowledge this is the closest prior work to ViperQ in spirit,
but the feature family is OFI rather than Auction Market The-
ory; the constructs we use (VPOC, Value Area, LVN, bal-
ance/imbalance classification) do not appear in any reviewed
system.
Auction Market Theory.The theoretical tradition we draw
on originates with Steidlmayer’s Market Profile [18] and Dal-
ton’s Auction Market Theory [19], which frame intraday price
discovery as oscillation between balance (mean-reverting two-
way trade) and imbalance (one-sided liquidity vacuum) states.
These constructs have been extensively adopted in proprietary-
trading practice for over three decades, but a focused litera-
ture search across the major scholarly indexes returned no peer-
reviewed reinforcement-learning system that uses them as ex-
plicit state features. ViperQ closes that gap.
Pattern recognition precedents.Application-driven rein-
forcement learning has prior precedent in this journal. Liu et
al. [28] apply hierarchical RL to chip-macro placement; Tsan-
tekidis et al. [29] apply knowledge-distilled deep RL to finan-
cial trading in a related Elsevier venue. These works estab-
lish that domain-application RL contributions are within scope
when framed as pattern recognition methodology.
3. Method
We treat sequential trading as a Markov Decision Process
(S,A,P,R,γ) implemented as a custom Gymnasium [30] en-
vironment,1 with all execution priced at the next bar’s open to
eliminate look-ahead bias.
1Gymnasium:https://gymnasium.farama.org/
2

ASK $ 102.05 × 150
ASK $ 102.04 × 280
ASK $ 102.03 × 420
ASK $ 102.02 × 90
mid
BID $ 102.01 × 310
BID $ 102.00 × 520
BID $ 101.99 × 240
BID $ 101.98 × 180
Market BUY
90 shares
∆P
mid shifts up to
next ask level
Liquidity consumed:
aggressive order removes
the entire passive rest-
ing size at this level
Legend
Passive bids (resting limit orders)
Passive asks (resting limit orders)
Aggressive flow (market order)
Consumed level (price moves)
ViperQ detection
The agent observes the rate at which ag-
gressive flow consumes passive liquidity
(CVD slope, tape velocity, imbalance ra-
tio) and infers the probability that the
next level will break before ∆ P occurs.
Figure 1: Matching engine: aggressive market flow consumes passive resting
liquidity; price moves only when the resting size at the touch is fully consumed.
ViperQ observes the consumption rate via CVD slope, tape velocity, and im-
balance ratio (Section 3.2).
time
price
V alue Area A
V alue Area B
Imbalance
(transition state)
liquidity vacuum;
ViperQ target
Phase 1: Balance Transition Phase 2: Balance
Agent objective:
 Remain flat during
Phase 1
 Enter at Transition
 Hold through break-
out
 Exit at new balance
Figure 2: Auction Market Theory: the market oscillates between balance and
imbalance. The agent targets the transition from Value Area A to Value Area
B, remaining flat during balance phases and holding through breakouts.
3.1. Order flow patterns: matching engine and Auction Market
Theory
The state representation rests on two compositional patterns
from market microstructure theory. Figure 1 formalises the
matching engine: a continuous double auction [14, 31] in
which aggressive market orders consume passive resting liq-
uidity, with mid-price displacement∆Poccurring only when
the resting size at the touch is exhausted [27]. ViperQ mea-
sures aggression and passive depth directly, via the Cumulative
V olume Delta, tape velocity, and order-flow imbalance features
defined below, and so observes the consumption ratebefore∆P
becomes visible in price.
Figure 2 depicts Auction Market Theory’s second pattern:
intraday price discovery oscillates between balance regimes
(mean-reverting trade inside a value area; passive policy opti-
mal: remain flat) and imbalance regimes (one-sided aggression
creates a liquidity vacuum and price sprints to find a new value
area) [18, 19]. The agent’s objective is detecting the transition
state.
3.2. State representation
Each observations t ∈R 20 is a Z-score-normalised vector
grouped into three blocks (Table 1). Block A encodes the
AMT/microstructure patterns; Block B injects two dynamic
position-aware variables at runtime; Block C provides nine
Table 1: The 20-dimensional state vectors t. Block A encodes Auction Market
Theory and microstructure patterns; Block B is injected at runtime from the
agent’s position; Block C supplies short-horizon memory.
Dim Name Construct
Block A: AMT/microstructure patterns
1z_price_vwapZ(price−VW AP), gravity to fair
value
2z_price_vpocZ(price−VPOC), distance to V ol-
ume Point of Control
3dist_to_wallNormalised position within 300 s
high–low range
4cvd_slope60 s first-difference of CVD
5cvd_divergenceBinary flag on 300 s price–CVD
correlation<−0.5
6tape_velocityTrade count÷60 s rolling mean
7trade_size_zZ-score of volume over 300 s win-
dow
8imbalance_ratioδ/(V+ε), buy vs. sell dominance
9in_lvn_zoneBinary flag for Low V olume Node
(V<0.5 ¯V)
Block B: dynamic position state
10unrealized_pnl(P t−P entry)·pos
11time_in_tradeSeconds since entry
Block C: lagged log-returns
12–20lag_1 ... lag_9log(P t/Pt−k),k∈{1,...,9}
lagged log-returns to give a 9-second memory without recur-
rence.
VPOC is approximated by a one-hour rolling VW AP, follow-
ing standard practitioner usage; VW AP itself follows [32]. Z-
score normalisation over rolling windows ensures stationarity
across volatility regimes.
3.3. Sniper reward function
The action space isA={flat,long}; short positions are dis-
abled. The rewardR t aggregates six components.
(1) Realised PnL at trade close.
Rclose =α·(P exit−P entry)·n·m−α·f syn·n,(1)
whereα=0.01,nis share count,mthe contract multiplier,
andf syn =$0.50/share is a synthetic in-training transaction fee
approximately 2,500×the real regulatory fee.
(2) Asymmetric unrealised-PnL shaping.
Rhold =
 +0.001·U t,U t >0 −0.05−0.005·|U t|,U t≤0 (2)
The asymmetry between the two branches is grounded in
Prospect Theory [21, 22]: Tversky and Kahneman’s empiri-
cal estimate of the loss-aversion coefficientλ≈2.25 (losses
weighted approximately 2.25×more heavily than equivalent
gains) provides the theoretical basis for asymmetric reward
shaping. The effective asymmetry in Eq. (2) is stronger than
theλ≈2.25 baseline, deliberately so, to compensate for the
additional reward density produced by 1-second decision steps
and to suppress the disposition effect [5, 6].
3

Table 2: Asset-specific training configurations. The same architecture and state
vector yield two distinct profitable policies. All constants listed here, with their
selection mechanism, appear in Table 3.
Constraint TSLA agent NVDA agent
Min. hold (s) 300 300
Drawdown shock−2.0/step−2.0/step
Trend bonus none+0.10/step (U t >$100)
(3) Trend bonus.WhenU t >$100,R trend = +0.10 per step, en-
couraging the agent to hold through sustained momentum rather
than taking premature profits.
(4) Time decay.After 3600 s,R time =−0.001·(t hold−3600)
penalises stagnant positions.
(5) Stop loss.R stop =−50.0 ifU t <−$200, triggering forced
exit.
(6) Drawdown shock and termination.During training, when
portfolio drawdown<−2%, a continuous−2.0/step penalty is
applied. If drawdown breaches the episode limit,R dd =−100.0
and the episode terminates.
3.4. Asset-specific dual-PPO training
Two PPO agents [20] are trained from the same state rep-
resentation but with two reward configurations (Table 2). The
TSLA agent operates with the default trend bonus and draw-
down shock; the NVDA agent receives an additional+0.10/step
held-winner bonus and the continuous drawdown shock at the
same threshold, producing a more risk-averse trend-following
policy. Both share the 300-second minimum holding constraint.
PPO defaults follow Stable-Baselines3 implementation of [20].
Why PPO.The algorithm was selected over alternatives on
four grounds. (i) The action space is discrete ({flat,long}),
which rules out continuous-control methods such as DDPG
(used inside the Yang et al. [3] ensemble) and SAC without
an additional discretisation layer. (ii) DQN-family methods
including TDQN [23] rely on an off-policy replay buffer that
mixes transitions across non-stationary market regimes; PPO’s
on-policy clipped updates avoid this distributional-shift bias.
(iii) A2C exhibits higher gradient variance and is less sample-
efficient at the data volumes used here (49.9 M test bars across
both assets and roughly four times that in training). (iv) PPO
is the dominant choice in published microstructure-RL prece-
dents (Lin and Beling [5], Briola et al. [10], Wang et al. [8]),
supporting comparability with prior work. All numerical con-
stants in Eqs. (1)–(2) and items (3)–(6) above, together with the
per-asset configurations in Table 2, are summarised in Table 3
with their selection mechanism (validation slice, industry con-
vention, theory-derived, or library default).
The complete 5-layer pipeline is summarised in Figure 3: in-
gestion of institutional tick data, 1-second OHLCV aggregation
with order-flow metrics, the 20-dimensional state engineering
described above, dual PPO inference, and a risk-bounded exe-
cution layer detailed in Section 4.
Layer 1. Tick data ingestion institutional feed
Layer 2. 1 s OHLCV + Delta aggregator
Layer 3. 20-dim AMT statest Z-normalised
4a.
PPO (TSLA)
4b.
PPO (NVDA)
Layer 5. Risk engine sizing, breakers
Output. Discrete trade actions
Figure 3: ViperQ system architecture: pattern extraction (Layers 1–3), policy
inference (Layer 4, dual PPO), and risk-bounded execution (Layer 5 and out-
put).
4. Risk-bounded execution
The risk layer translates the agent’s discrete action into a final
share count and enforces three circuit breakers. Position size
follows volatility-adjusted sizing:
nideal =
$ Bt·r a
2·ATR t
%
,n final =min (nideal,⌊Ct/Pt⌋),(3)
whereB t is current equity,r a ∈ {0.25%,0.50%,1.0%}maps
conviction to dollar-risk, ATRt is the prevailing Average True
Range, andC t is available cash. The cash clamp in the sec-
ond term makes leverage impossible. Three additional hard
rules over-ride the agent: (i) daily loss limit of−2% of starting
equity locks trading until the next session; (ii) per-trade unre-
alised loss exceeding $200 triggers forced exit; (iii) all positions
are flattened at 15:55 ET to eliminate overnight gap risk. The
−2% daily loss limit, the 2-ATR stop distance, and the end-
of-day flatten are standard intraday proprietary-trading conven-
tions rather than hand-tuned parameters.
5. Experimental setup
Data.Institutional tick data for NVDA and TSLA from
Databento, January 2020 to February 2026, covering the
COVID-era volatility regime, the 2023–24 AI-driven rally, and
the 2025–26 rate-cycle period. Nanosecond ticks are aggre-
gated to 1-second OHLCV bars augmented with Delta (signed
aggressive volume) and trade count. An 80/20 chronological
partition holds out the final twelve months; no information from
the test partition enters training or hyperparameter selection.
Hyperparameter selection.Every numerical constant in-
troduced in Sections 3.3–4 is treated as a hyperparameter and
4

Table 3: Master hyperparameter table.Mech.:VAL=selected on the valida-
tion slice of the training partition;CONV=industry convention for intraday
proprietary trading, taken without tuning;TH=theory-derived with literature
anchor;LIT=library default (Stable-Baselines3).
Element Value Mech. Source/rationale
Reward function (Eqs. 1–2, items (3)–(6))
α(PnL scaling) 0.01 V AL PPO gradient stability
fsyn $0.50/share V AL suppresses sub-tick scalping (§6.3)
Hold gain branch+0.001·U t V AL disposition-effect tuning
Hold loss branch−0.05−0.005|U t|TH Tversky–Kahnemanλ≈2.25 [22]
Trend bonus+0.10/step V AL held-winner reinforcement
Trend threshold $100 (U t) CONV 1% of $10k capital
Time-decay rate−0.001/step V AL validation
Time-decay onset 3600 s CONV 1 h intraday cap
Stop-loss penalty−50.0 V AL validation
Stop-loss threshold−$200 (U t) CONV 2% of capital
Drawdown shock−2.0/step V AL validation
Drawdown threshold−2% CONV prop daily-loss limit
Episode-end penalty−100.0 V AL validation
Risk-bounded execution (§4, Eq. 3)
Per-trade riskr a {0.25,0.50,1.0}% CONV conviction sizing
ATR stop multiplier 2×CONV 2-ATR distance
Daily loss cap−2% CONV prop daily limit
EOD flatten 15:55 ET CONV gap-risk hedge
State construction (Table 1)
VW AP/VPOC window 3600 s CONV practitioner default
Microstructure window 300 s CONV 5-min standard
CVD/velocity window 60 s CONV 1-min standard
Lag depth 9 steps V AL memory/dim. tradeoff
Training
PPO architecture SB3 defaults LIT Stable-Baselines3 [20]
Min. hold (training) 300 s CONV 5-min HFT/momentum cut
listed in Table 3 with the mechanism by which its value was
fixed. Four mechanisms are used:V AL(selected on the valida-
tion portion of the training split, in the spirit of [5, 10, 11, 3]);
CONV(industry convention for intraday proprietary trading,
taken without tuning);TH(theory-derived, with a literature an-
chor);LIT(library default, used as-is from Stable-Baselines3
for the PPO architecture, following [20]). A formal one-factor-
at-a-time sensitivity sweep is reserved for future work, in line
with Lin and Beling [5], who in a comparable setting note that
they “did not perform an exhaustive grid search on the hyper-
parameter space, but rather [drew] random samples from the
hyperparameter space due to limited computing resources”.
Evaluation.Initial capital is $10,000 per asset. Backtests
are deterministic; all trades clear at the next bar’s open. Real
regulatory fees ($0.0002/share) are charged at evaluation time.
The synthetic feef syn used during training (Eq. 1) isnotactive
at evaluation.
6. Results
6.1. Out-of-sample performance
Table 4 reports performance on the held-out twelve-month
partition. The TSLA agent achieves+163.6% ROI with
−27.5% maximum drawdown across 27,019 trades; the NVDA
agent achieves+116.5% ROI with−47.8% maximum draw-
down across 12,892 trades. Both are produced with zero lever-
age and full regulatory-fee accounting.
6.2. Comparison with published RL trading systems
Direct head-to-head comparison is precluded by the absence
of standardised HFT-RL benchmarks: published papers differ
in assets, time horizons, data resolution, capital assumptions,
Table 4: ViperQ performance on the held-out test partition (final 20% of data,
never seen during training). Initial capital $10,000 per asset; zero leverage;
$0.0002/share regulatory fees applied.
Metric TSLA NVDA
Final balance $26,364.87 $21,652.86
PnL+$16,364.87+$11,652.86
ROI+163.6%+116.5%
Maximum drawdown−27.5%−47.8%
Total trades 27,019 12,892
Test-set bars 33.4 M 16.5 M
Table 5: ViperQ vs. recently published RL trading systems with retrievable
performance numbers. Typical published range [2]: ROI [5%,40%], MDD
[−5%,−25%]. “n.r.”=not reported; “n.a.”=not applicable.
System Algorithm Asset/Horizon ROI % MDD %
DeepLOB [12] CNN sup. LOB/events n.a. n.a.
DRL-Trade [11] DQN/PG/A2C 50 fut/daily pos. Sharpe n.r.
FinRL [3] Ensemble Dow 30/daily≈30−10.2
PPO-Exec [5] PPO/LSTM LOB/per-step beats TW AP n.r.
TDQN [23] DQN 30 eq/daily beats pass. n.r.
HFT-PPO [10] PPO INTC/events stable+n.r.
RL-Exec [6] DQN ABIDES/HFT beats TW AP n.r.
Q-React [7] DDQN LOB sim/HFT beats AC n.r.
DL+RL [26] TD-learn FX/idx/multi-h multi-horiz n.r.
ViperQ TSLAPPO+AMT TSLA/1 s+163.6−27.5
ViperQ NVDAPPO+AMT NVDA/1 s+116.5−47.8
and reporting conventions. Pippas et al. [2] survey 167 RL-
finance papers and observe that consistent benchmarking is it-
self an open methodological problem. We therefore position
ViperQ within the published landscape rather than claim dom-
inance over it. Table 5 lists peer-comparable systems with re-
trievable performance numbers; Figure 4 plots ViperQ along-
side those points in the ROI/MDD plane.
ViperQ’s+163.6% TSLA ROI is, to the best of our knowl-
edge, the highest reported on a held-out test partition by any
peer-reviewed RL trading system operating at sub-daily reso-
lution. The figure is more than 4×the upper bound of the
[5%,40%] ROI range surveyed across 167 RL-finance papers
by Pippas et al. [2] for daily-horizon US-equity systems, and the
only peer-reviewed point in Table 5 with a numerically reported
MDD (FinRL Ensemble [3],≈+30%/−10.2%) is dominated
on ROI by more than a factor of five. We do not claim Pareto
dominance over prior work: ViperQ’s drawdowns are materi-
ally deeper than those of daily portfolio-rebalancing systems
on low-volatility universes, and it operates at a time resolution
two orders of magnitude finer than any system in Table 5 that
reports both ROI and MDD, so direct comparison on either axis
alone is incomplete. What we claim is the existence of a previ-
ously unreported operating point in the published sub-daily RL
landscape: absolute returns exceeding the surveyed range at the
price of higher drawdown, achieved by encoding microstruc-
ture pattern theory explicitly into the state vector rather than
learning end-to-end from raw LOB events.
6.3. Behavioural divergence between the two agents
Although a formal ablation is reserved for future work, three
observations from development are worth documenting. First,
5

0 25 50 75 100 125 150 175 200
Return on Investment (%)
50
40
30
20
10
0
Maximum Drawdown (%)
Typical published
RL trading range
(Pippas et al. 2025)
FinRL Ensemble
(Yang et al. 2020)
ViperQ TSLA
163.6% / -27.5%
ViperQ NVDA
116.5% / -47.8%
higher return,
shallower drawdown
(ideal)
ViperQ (this work)
Figure 4: ViperQ in the ROI/MDD plane against published RL trading systems
with concrete numbers. The shaded region marks the typical published range
surveyed in [2].
the synthetic in-training transaction feef syn =$0.50/share
(Eq. 1) is necessary, not optional: without it, the agent con-
verges on a degenerate policy that trades thousands of times
per second to capture sub-tick noise and then accumulates
losses entirely through commission drag once realistic fees
are restored at evaluation. Second, removing the 300-second
minimum-hold constraint causes the TSLA policy to collapse
into rapid scalping that fails to capture the longer momentum
moves the AMT state features were designed to detect. Third,
the continuous drawdown shock of−2.0/step is what makes the
NVDA agent risk-averse; without it, both agents converge to
similar high-frequency behaviour and the asset-specific diver-
gence visible in Table 4 disappears.
6.4. A note on Sharpe-style metrics
Sharpe-style annualised risk-adjusted metrics are intention-
ally omitted. At 1-second bar resolution, the standard annu-
alisation factor √252·23,400 amplifies microstructure noise
rather than isolating signal, and produces values that are not
comparable to the daily-horizon Sharpe figures dominant in Ta-
ble 5. We follow [10, 11] in reporting absolute ROI and maxi-
mum drawdown as the more interpretable metrics at this reso-
lution.
7. Limitations
Three limitations qualify the results above.First, the empir-
ical evaluation is restricted to two highly volatile US single-
name equities (NVDA, TSLA) over a single 80/20 temporal
split; generalisation to lower-volatility names, to non-US mar-
kets, or to other intraday regimes is untested.Second, although
the dual-agent design (Table 2) provides a form of cross-asset
behavioural ablation and Section 6.3 documents three qualita-
tive findings from development, we do not present a formal one-
factor-at-a-time ablation of the reward components or a hyper-
parameter sensitivity sweep; both are reserved for future work,
consistent with the practice in the systems we cite (Section 5).
Third, the NVDA agent’s−47.8% maximum drawdown is ma-
terially higher than the−5% to−15% range typical of portfolio-
rebalancing RL systems on daily horizons [2]. ViperQ trades
drawdown depth for absolute-return magnitude (Figure 4); it is
not pareto-superior to conservative portfolio systems and would
be inappropriate for capital-preservation mandates.
8. Conclusion
We have presented ViperQ, to the best of our knowledge,
the first peer-reviewed reinforcement learning trading system
whose state representation is built explicitly from Steidlmayer–
Dalton Auction Market Theory primitives. The 20-dimensional
state vector encodes V olume Point of Control, Value Area posi-
tion, Low V olume Node flags, Cumulative V olume Delta di-
vergence, tape-velocity signatures and order-flow imbalance,
which are the computational analogues of constructs first
formalised by Steidlmayer and Dalton. A prospect-theory-
grounded asymmetric reward function, together with asset-
specific behavioural constraints, drives two Proximal Policy
Optimisation agents to substantial out-of-sample performance:
+163.6% ROI on TSLA and+116.5% ROI on NVDA over a
held-out twelve-month partition, under zero leverage and full
regulatory-fee accounting. The broader contribution is that
AMT, treated as a microstructure inductive prior, yields a state
space on which a small neural policy converges to interpretable,
profitable out-of-sample behaviour. Four properties make this
prior productive for sub-daily RL trading: (i)sample efficiency,
since a 20-dimensional engineered state needs far fewer pa-
rameters than end-to-end LOB ingestion at the same horizon,
easing the data demands of policy-gradient updates; (ii)inter-
pretability, since every dimension ofs t corresponds to a named
microstructure construct (Table 1), so policy behaviour can be
inspected against human trading intuition; (iii) anempirical fil-
ter, since three decades of proprietary-trading usage [18, 19]
pre-select constructs that encode persistent microstructure reg-
ularities rather than noise; and (iv)cross-reward generalisation,
since the same state vector supports two distinct profitable poli-
cies (Table 2) without feature re-engineering, evidence that the
structure absorbs reward-shaping changes rather than being co-
adapted to them. Future work targets formal reward-component
sensitivity analysis, a broader asset universe, and transfer of the
AMT state representation to alternative policy classes.
References
[1] B. Hambly, R. Xu, H. Yang, Recent advances in reinforce-
ment learning in finance, Mathematical Finance 33 (3)
(2023) 437–503.doi:10.1111/mafi.12382.
[2] N. Pippas, E. A. Ludvig, C. Turkay, The evolution of re-
inforcement learning in quantitative finance: A survey,
ACM Computing Surveys 57 (11) (2025) Article 295.
doi:10.1145/3733714.
[3] H. Yang, X.-Y . Liu, S. Zhong, A. Walid, Deep reinforce-
ment learning for automated stock trading: An ensem-
ble strategy, in: Proceedings of the First ACM Interna-
6

tional Conference on AI in Finance (ICAIF ’20), 2020.
doi:10.1145/3383455.3422540.
[4] X.-Y . Liu, H. Yang, Q. Chen, R. Zhang, L. Yang, B. Xiao,
C. D. Wang, FinRL: A deep reinforcement learning li-
brary for automated stock trading in quantitative finance,
arXiv preprint arXiv:2011.09607 (NeurIPS 2020 Deep RL
Workshop) (2020).
[5] S. Lin, P. A. Beling, An end-to-end optimal trade execu-
tion framework based on proximal policy optimization, in:
Proceedings of the Twenty-Ninth International Joint Con-
ference on Artificial Intelligence (IJCAI-20), 2020, pp.
4548–4554.doi:10.24963/ijcai.2020/627.
[6] Y . Hafsi, E. Vittori, Optimal execution with reinforcement
learning, arXiv preprint arXiv:2411.06389 (2024).
[7] T. Espana, Y . Hafsi, F. Lillo, E. Vittori, Reinforcement
learning in queue-reactive models: Application to optimal
execution, arXiv preprint arXiv:2511.15262 (2025).
[8] Y . Wang, R. Savani, A. Gu, C. Mascioli, T. L. Turocy,
M. P. Wellman, Market making with learned beta policies,
in: Proceedings of the 5th ACM International Conference
on AI in Finance (ICAIF ’24), 2024, pp. 643–651.doi:
10.1145/3677052.3698623.
[9] R. Zimmer, O. L. V . Costa, Reinforcement learning-
based market making as a stochastic control on non-
stationary limit order book dynamics, arXiv preprint
arXiv:2509.12456 (2025).
[10] A. Briola, J. Turiel, R. Marcaccioli, A. Cauderan, T. Aste,
Deep reinforcement learning for active high frequency
trading, arXiv preprint arXiv:2101.07107 (2021).
[11] Z. Zhang, S. Zohren, S. Roberts, Deep reinforcement
learning for trading, The Journal of Financial Data Sci-
ence 2 (2) (2020) 25–40.doi:10.3905/jfds.2020.1.
030.
[12] Z. Zhang, S. Zohren, S. Roberts, DeepLOB: Deep con-
volutional neural networks for limit order books, IEEE
Transactions on Signal Processing 67 (11) (2019) 3001–
3012.doi:10.1109/TSP.2019.2907260.
[13] Y . Xiao, C. Ventre, Y . Wang, H. Li, Y . Huan, B. Liu, LiT:
limit order book transformer, Frontiers in Artificial Intel-
ligence 8 (2025) 1616485.doi:10.3389/frai.2025.
1616485.
[14] A. S. Kyle, Continuous auctions and insider trading,
Econometrica 53 (6) (1985) 1315–1335.doi:10.2307/
1913210.
[15] L. R. Glosten, P. R. Milgrom, Bid, ask and trans-
action prices in a specialist market with heteroge-
neously informed traders, Journal of Financial Economics
14 (1) (1985) 71–100.doi:10.1016/0304-405X(85)
90044-3.
[16] M. O’Hara, Market Microstructure Theory, Blackwell,
Cambridge, MA, 1995.
[17] D. Easley, M. M. López de Prado, M. O’Hara, Flow toxic-
ity and liquidity in a high-frequency world, Review of Fi-
nancial Studies 25 (5) (2012) 1457–1493.doi:10.1093/
rfs/hhs053.
[18] J. P. Steidlmayer, K. Koy, Markets and Market Logic, The
Porcupine Press, Chicago, 1986.
[19] J. F. Dalton, E. T. Jones, R. B. Dalton, Mind Over Mar-
kets: Power Trading with Market Generated Information,
Probus Publishing, Chicago, 1990.
[20] J. Schulman, F. Wolski, P. Dhariwal, A. Radford,
O. Klimov, Proximal policy optimization algorithms,
arXiv preprint arXiv:1707.06347 (2017).
[21] D. Kahneman, A. Tversky, Prospect theory: An analysis
of decision under risk, Econometrica 47 (2) (1979) 263–
291.doi:10.2307/1914185.
[22] A. Tversky, D. Kahneman, Advances in prospect theory:
Cumulative representation of uncertainty, Journal of Risk
and Uncertainty 5 (4) (1992) 297–323.doi:10.1007/
BF00122574.
[23] T. Théate, D. Ernst, An application of deep reinforcement
learning to algorithmic trading, Expert Systems with Ap-
plications 173 (2021) 114632.doi:10.1016/j.eswa.
2021.114632.
[24] A. Coletta, J. Jerome, R. Savani, S. Vyetrenko, Condi-
tional generators for limit order book environments: Ex-
plainability, challenges, and robustness, in: Proceedings
of the 4th ACM International Conference on AI in Finance
(ICAIF ’23), 2023, pp. 27–35.doi:10.1145/3604237.
3626854.
[25] C. Mascioli, A. Gu, Y . Wang, M. Chakraborty, M. P. Well-
man, A financial market simulation environment for trad-
ing agents using deep reinforcement learning, in: Pro-
ceedings of the 5th ACM International Conference on
AI in Finance (ICAIF ’24), 2024, pp. 117–125.doi:
10.1145/3677052.3698639.
[26] K. S. Jaddu, P. A. Bilokon, Deep learning with reinforce-
ment learning on order books, The Journal of Financial
Data Science 6 (1) (2024) 61–84.doi:10.3905/jfds.
2024.1.157.
[27] R. Cont, A. Kukanov, S. Stoikov, The price impact of or-
der book events, Journal of Financial Econometrics 12 (1)
(2014) 47–88.doi:10.1093/jjfinec/nbt003.
[28] T. Liu, Y . Pu, D. Lei, Y . Ge, Z. Chen, L. Wang, Hierarchi-
cal reinforcement learning for chip-macro placement in
integrated circuit, Pattern Recognition Letters 180 (2024)
19–25.doi:10.1016/j.patrec.2024.02.002.
[29] A. Tsantekidis, N. Passalis, A. Tefas, Diversity-driven
knowledge distillation for financial trading using deep re-
inforcement learning, Neural Networks 140 (2021) 193–
202.doi:10.1016/j.neunet.2021.02.026.
[30] M. Towers, A. Kwiatkowski, J. K. Terry, J. U. Balis,
G. De Cola, T. Deleu, M. Goulão, A. Kallinteris, M. Krim-
mel, A. KG, R. Perez-Vicente, A. Pierré, S. Schulhoff,
J. J. Tai, H. Tan, O. G. Younis, Gymnasium: A standard
interface for reinforcement learning environments, arXiv
preprint arXiv:2407.17032 (2024).
[31] M. D. Gould, M. A. Porter, S. Williams, M. McDonald,
D. J. Fenn, S. D. Howison, Limit order books, Quantita-
tive Finance 13 (11) (2013) 1709–1742.doi:10.1080/
14697688.2013.803148.
[32] Á. Cartea, S. Jaimungal, J. Penalva, Algorithmic and
High-Frequency Trading, Cambridge University Press,
2015.
7
