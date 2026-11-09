---
title: When do prophets profit in prediction markets?
url: https://arxiv.org/abs/2607.06166
category: ai-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Anri Gu
- Nicole Kagan
- Alec Sun
- Jibang Wu
- Haifeng Xu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.06166
pages: 30
chars: 109896
fetched_at: '2026-11-08T13:03:41+00:00'
kb_version: 1
---

# When do prophets profit in prediction markets?

When do prophets profit in prediction markets? ∗
Anri Gu
University of Chicago
anrigu@uchicago.edu
Nicole Kagan
Kalshi Research
nkagan@kalshi.com
Alec Sun
University of Chicago
alecsun@uchicago.edu
Jibang Wu
New York University, Shanghai
wujibang@nyu.edu
Haifeng Xu
University of Chicago
haifengxu@uchicago.edu
Abstract
Prediction markets aggregate dispersed beliefs into prices that act as probabilistic
forecasts of uncertain events. Classical theory establishes how a better-than-market
forecast can yield positive trading profit. However, it hinges crucially on the
specific automated market maker (AMM) design, and is not applicable to popular
exchanges today which are based on central limit order books. This paper fills that
gap. For any prediction market and any proper scoring ruleS, we exhibit a “proper”
betting strategy that depends only on the forecaster’s prediction p and the market
price q, and earns positive expected profitwhenever p outperforms q under S
and the market has sufficient liquidity. Moreover, this proper betting is essentially
the only strategy with such robust profitability guarantee. Our proof rests on
a decomposition of expected profit that strictly generalizes the classical AMM
guarantee and also explains how strategies can profit even without an accuracy
edge. Empirically, across thousands of forecasts by AI models, proper betting is
the only strategy that reliably converts accuracy into profit, and we further identify
systematic forecasting personas and show how the optimal proper strategy varies
across them. For feasibility demonstration, we run a monthlong live pilot test on
Kalshi; the encouraging preliminary results show that proper betting can survive
real-world spreads, fees, discrete fills, and limited liquidity.
Disclaimer. While this paper contains live trading results with real capital gain, these should
NOT be interpreted as trading suggestions. Instead, we conduct limited live experiments only
to test whether or not our theoretic mechanism could survive real-world spreads, fees, and
limited liquidity. Professional trading considers many more factors such as drawdown control,
variance minimization, leverage, capital allocation etc. which are out of this paper’s scope.
1 Introduction
Prediction markets let people trade contracts whose prices reflect the market’s estimated probability
of an event, aggregating dispersed beliefs in the spirit of Hayek [1945]’s “marvel of the price system.”
Empirical studies confirm that real prediction-market prices are well calibrated and often outperform
polls and expert panels [Berg et al., 2008, Rothschild, 2009, Wolfers and Zitzewitz, 2004, Arrow
et al., 2008]. The market scoring rule literature [Hanson, 2003, 2007, Chen and Pennock, 2007,
∗Authors are ordered alphabetically. The work by Jibang Wu is performed while visiting the University of Chicago.
Preprint.
arXiv:2607.06166v3  [cs.AI]  23 Sep 2026

Abernethy et al., 2013] formalizes the underlying incentive: an informed forecaster profits by trading
against the market, and that trade pushes the price closer to the truth, so information aggregation and
individual reward would go hand in hand.
This picture, however, was developed for one specific market design: an automated market maker
(AMM) [Hanson, 2003], in which an informed forecaster ensures profit by moving the market
price exactly to their own forecast, with expected profit equal to their accuracy edge. The largest
prediction markets today (e.g., Kalshi, Polymarket) instead use central limit order books [Kalshi,
2025, Polymarket, 2023, Ng et al., 2026], favored over AMMs for their scalability, adaptability, and
regulatory fit (see Section A). Prices arise from matching opposing limit orders, and a forecaster can
pick any bet size but faces whatever price impact the order book happens to deliver, plus bid-ask
spreads, finite liquidity, and platform fees. The link between accuracy and profit is no longer pinned
down by the price-formation rule, and converting accuracy into profit becomes a separate problem.
Recent empirical work makes this gap visible. Forecasters whose predictions outperform the market
on average routinely fail to convert that edge into trading profit [Della Vedova, 2026, Jang et al.,
2025]. On the AI leaderboards that turns AI forecasts into prediction-market trades, every agent
loses money despite several beating the market under standard proper scoring rules [Yang et al.,
2025]. One may attribute the failure to the market frictions, but even in the idealized setting (with no
price impact, bid-ask spread, or fees), we can observe that natural betting heuristics would produce
negative profit from reasonably good forecasts (see the failure of Kelly in Example 1, the failure of
max-margin-based betting in Example 2 and more empirical results in Section 4.1). Stranger still,
the converse also fails: simple strategies earn positive expected profit even when the underlying
forecaster has no accuracy edge at all (see Example 3). Translating accuracy into profit is therefore a
problem in its own right, distinct from forecasting accuracy.
The primary contribution of this paperis to establish a principled connection between predictive
accuracy and robust trading profitability in general prediction markets with an arbitrary price-impact
function. First, we exhibit a betting strategy that converts an accuracy edge over market into profits:
Theorem(Informal version of Theorem 1).If a forecaster could outperform a sufficiently liquid
prediction market under any strictly proper scoring rule S, then there exists a specific “proper”
betting strategy associated toSthat ensures positive expected profit for the forecaster.
The expected profit of this proper betting strategy decomposes into three explicit terms — score gap,
Bregman divergence, and liquidity loss — which explain how strategies can profit evenwithoutan
accuracy edge (the Bregman divergence alone can suffice). Furthermore, when instantiated in AMM
markets, our proper betting strategy corresponds precisely to the canonic betting strategy in AMM
that moves market price to the forecaster’s belief. The above result then recovers the classic AMM
guarantee as a boundary case where the Bregman divergence exactly absorbs liquidity loss. Notably,
the nature of Theorem 1 is a robust optimization result, while not expected profit maximization which
is not this paper’s goal.
Our second main result establishes that the above proper betting is essentially the only betting strategy
that robustly guarantees profitability on any sufficiently liquid market — in the sense of ensuring
positive profitwheneverthere is a score edge.
Theorem(Informal version of Theorem 2).Any robustly profitable betting strategy is “essentially”
(see formal Definition 3) the same as the above proper betting, up to profitability-invariant modifica-
tions such as proportionally rescaling bets and constant shifting.
The two main results above also yield a new characterization of proper scoring rules through the lens
of robust profitability – that is, a scoring rule is properif and only ifthere exists an associated betting
strategy that is robustly profitable (Proposition 2). Finally, we further extend our results to three
practically important settings: betting on a sequence of events based on empirical scores (instead of
the theoretical expectation), betting under nonzero bid-ask spreads, and long-horizon trading in which
the forecaster can buy and sell the same event’s contracts at different time as both the forecaster’s and
market’s predictions evolve.
2

Because testing our strategies requires vast amounts of prediction data, we experimentally evaluate
our proper betting strategies on thousands of AI-generated forecasts and find a clear advantage
over standard heuristic baselines. We identify systematic forecasting personas across models, with
different personas favoring different proper betting strategies. Finally, to demonstrate the practical
feasibility of our theory, we deployed an AI forecasting agent with real capital on the Kalshi prediction
market for a month. The agent achieved very encouraging return on investment (ROI) and Sharpe
ratio, which shows that our theoretically derived betting strategy can survive real-world spreads, fees,
discrete fills, and limited liquidity.
1.1 Additional related work
Proper scoring rules.Proper scoring rules originate in the statistical forecasting literature as a
mechanism for eliciting truthful probabilistic predictions [Brier, 1950, Good, 1952, McCarthy,
1956b, Savage, 1971]. Gneiting and Raftery [2007] formalize strictly proper scoring rules and their
relationship to Bregman divergences and convex analysis. Subsequent work extends these ideas
to more general prediction settings, including decision-theoretic elicitation [Lambert et al., 2008],
mechanism design [Chen and Vaughan, 2010], and optimal information acquisition [Li et al., 2022].
Prediction markets.Prediction markets themselves are a well-studied mechanism for aggregating
dispersed beliefs into a consensus probability [Wolfers and Zitzewitz, 2004, Arrow et al., 2008].
Hanson [2003, 2007] introduced market scoring rules, which use a proper scoring rule to automate
market making and provide subsidized liquidity; this framework underpins several implementation
proposals such as the Logarithmic Market Scoring Rule (LMSR) and its derivatives [Chen and
Pennock, 2007, Abernethy et al., 2013]. A parallel line of work examines price formation and
information aggregation under strategic trading [Chen et al., 2010]. Empirical studies of real
prediction markets [Berg et al., 2008, Rothschild, 2009] have documented that prices are calibrated
and often outperform expert forecasts.
Betting strategies.The problem of translating a probabilistic forecast into a bet size has a long
history, beginning with the Kelly criterion [Kelly, 1956, Thorp, 1975, MacLean et al., 2011], which
maximizes long-run log-wealth under known margin. Our work inherently is also about betting
strategy design, but ours differs from Kelly in a key aspect: our strategy is oblivious to the ground
truth probabilities and comes with robustness guarantees, whereas Kelly criterion assumes perfect
knowledge of the (usually unobservable) ground truth probabilities and can perform poorly otherwise
(see Example 1). More recent work has connected portfolio selection to online learning and proper
scoring rules [Cover, 1991, Abernethy et al., 2013], but typically assumes a single scoring-rule
objective rather than asking which scoring rule best converts predictions into profit. At the same time,
recent studies have highlighted a paradox in which models achieve strong predictive performance yet
fail to generate positive returns [Della Vedova, 2026, Jang et al., 2025].
2 Preliminaries
Notation.Define [K] :={1, . . . , K}. Let ∆[K] :={p∈[0,1] K : P k∈[K] pk = 1} denote the
probability simplex, 1y ∈ {0,1}K the one-hot vector with a 1 in y-th entry, 1∈R k the vector with
every entry equal to 1,∇Gthe gradient of a functionG, and∥·∥the Euclidean norm.
Prediction markets.Consider a probabilistic event with K disjointoutcomes andground truth
p∗ ∈∆ [K]. A prediction market on this event offers, for each outcome k∈[K] , acontractthat
pays 1 if outcome k occurs and 0 otherwise. Let q= (q k)k∈[K] ∈[0,1] K denote the price vector,
where qk is the price of the contract on outcome k. A forecaster’sbetting strategyis described by a
position vector s∈R K, where sk is the forecaster’s position on outcome k (sk >0 buys, sk <0
sells). When the outcomey∼p ∗ is realized, the forecaster receives payouts·1 y =s y.
For ease of presentation, we assume the price vector lies on the probability simplex, q∈∆ [K],
equivalently P k∈[K] qk = 1. Under this condition, the price vector q admits a natural interpretation
3

as the market’sconsensus belief[Arrow et al., 2008]. Thus a forecaster who believes that outcome k
realizes with probability exactly qk has zero expected return from this contract, i.e., −qk +q k ·1 = 0 .
We note that any arbitrage-free market must have P k∈[K] qk = 1, otherwise a trader can obtain a
riskless profit of

1− P k∈[K] qk

 by buying or selling one share of every contract. Real markets,
however, sidestep this by maintaining separate price for bid/buy and ask/sell, the gap of which is
called thespread. Section 3.3 will discuss how our main results naturally extend to the case of
non-zero bid-ask spread with minor modifications.
A market has finite liquidity at the quote price q, described by aprice-impact function ρ:R K →
∆[K], where ρ(s) is the post-trade spot price upon executing theposition vector s, satisfying the
boundary condition ρ(0) =q and the monotonicity condition(ρ(s)−ρ(s′))·(s−s′)≥0,∀s,s ′ ∈R K,
i.e., walking the order book in any direction shall move the marginal price in that same direction.
Executing s incurs the integrated cost
R 1
0 ρ(ts)·sdt , which can be decomposed into the spot-price
piece s·q plus a non-negativeliquidity loss(slippage) capturing the price impact along the trajectory:2
Lρ(s;q) :=
Z 1
0
ρ(ts)·sdt−s·q.(Liquidity Loss)
The monotonicity condition (ρ(s)−ρ(s ′))·(s−s ′)≥0 implies that liquidity loss is always non-
negative. Generally, the more liquid a market is, the smaller Lρ(s;q) is (often approaching 0 in
practice for reasonably liquid markets and sized bets). The forecaster collects a payout s·1 y for a
realized outcomey, so the expected profit is
π(s,p ∗) :=s·(p ∗ −q)−L ρ(s;q).(Expected Profits)
Remark 1.The form of ρ depends on the market design: the classic automated market makers
(AMMs) [Hanson, 2003] set ρ=∇C for a convex cost function C, whereas the largest prediction
markets today run a central limit order book for which ρ is piecewise constant and read directly
off the order book [Kalshi, 2025, Polymarket, 2023]. We discuss these two main prediction-market
implementations in detail in Section A, but our theory is applicable to any design. We also note
that ρ itself evolves over time as the order book updates with new resting orders and executions; we
suppress this time dependence since each of our analyses concerns a single instantaneous bet against
a snapshot of the book.
Scoring rules.Scoring rulesare a standard tool to measure the quality of a probabilistic fore-
cast. Given a forecaster’s prediction p∈∆ [K] and a realized outcome y∈[K] , ascoring
rule S(p, y)assigns a real-valued reward to the forecast p based on y, with expected score
S(p;p ∗) :=E y∼p∗ [S(p, y)]under a ground truth p∗. Scoring rules were introduced to truth-
fully elicit forecasts; a scoring rule is said to beproperif it incentivizes a forecaster to report their
true distributional beliefp.
Definition 1(Proper scoring rule).A scoring rule S isproperif a forecaster maximizes her expected
score by reporting her true belief p. Formally, for every p,p ′ ∈∆ [K], S(p;p)≥S(p ′;p). We say
the rule isstrictly properif the inequality is strict forp ′ ̸=p.
A proper scoring rule lets us compare any two probabilistic forecasts under some ground truth p∗.
For example, applying S to the market consensus q gives themarket score S(q;p ∗), and we say the
forecasteroutperformsthe market if S(p;p ∗)> S(q;p ∗). Importantly, the comparison of scores
depends on the ground truthp∗, which can never be observed in most market applications. Section 3.3
discusses how to compare forecasts based on empirical scoreS(p;y) on realized outcome y, averaged
across markets.
Every proper scoring rule corresponds to a convexpotential functionGas stated in a folklore result
below.
2Due to monotonicity condition of ρ(s), R 1 0 ρ(ts)·sdt is the least cost for purchasing s shares even ρ(s) may not
necessarily be a conservative vector field.
4

Proposition 1(Characterization of proper scoring rules [McCarthy, 1956a]).A scoring rule S is
(strictly) proper if and only if there exists a (strictly) convex functionG: ∆ K →R associated to S
such that
S(p, y) =G(p) +∇G(p)·(1 y −p).
Meanwhile, theBregman divergenceis defined for every strictly convex differentiable function G as
DG(q,p) :=G(q)−G(p)− ∇G(p)·(q−p),
where DG(q,p)≥0 with equality if and only if p=q . Table 1 below lists examples of proper
scoring rules along their associated convex functions (the last columnsG is introduced in Definition 2).
Table 1:Common proper scoring rules with their associated functions.
S(p, y)G(p)D G(q,p)s G(p,q)
Quadratic (Brier)−∥1 y −p∥ 2 ∥p∥2 −1∥q−p∥ 2 2(p−q)
Logarithmiclogp y
P
k pk logp k
P
k qk log(qk/pk) log(p)−log(q)
Sphericalp y/∥p∥ ∥p∥ ∥q∥ −p·q/∥p∥p/∥p∥ −q/∥q∥
3 A theory of proper betting for prediction markets
The goal of this paper is to translate a forecaster’s prediction p that outperforms the market into
a concrete betting strategy that guarantees profit in a general prediction market. There are several
natural strategies, such as betting on the highest-margin outcome, scaling inversely with margin, or
using Kelly criterion [Kelly, 1956]. Thehighest-marginstrategy places a bet on the outcome k for
which |pk −q k| is greatest, as this outcome intuitively has the most potential for profit: the difference
between the perceived value pk of the share and the actual price qk is greatest. Perhaps surprisingly,
we show below that both the Kelly criterion and the highest-margin strategy donotguarantee positive
expected profit, thus demonstrating that betting optimization is challenging even for a good forecaster.
In Section 4, we also empirically observe that all of these approaches perform poorly in practice.
Example 1(Accurate forecaster + Kelly can lose).Consider an event with three outcomes and let
p= (0.64,0.32,0.04) , q= (0.80,0.10,0.10) , and p∗ = (0.10,0.10,0.80) . Under the quadratic
scoring rule, since ∥p∗ −p∥<∥p ∗ −q∥ , the forecaster outperforms the market. The Kelly criterion
would spend pi to purchase pi/qi shares of contract i for each i= 1,2,3 ,3 and its expected profit
is (p⊘q)·(p ∗ −q)<0 . The intrinsic reason of this loss is that the Kelly criterion is derived by
assuming its forecast is the ground truth, which in practice can be very off from the forecast.
Example 2(Accurate forecaster + highest-margin trade can lose).Consider an event with three
outcomes and let p= (0.61,0.39,0.00) , q= (0.10,0.89,0.01) , and p∗ = (0.05,0.10,0.85) . Under
the quadratic scoring rule, since ∥p∗ −p∥<∥p ∗ −q∥ , the forecaster outperforms the market.
If the forecaster only places a bet on the highest-margin first outcome, their expected profit is
(1,0,0)·(p ∗ −q)<0.
On the other hand, a forecaster can profit even if their prediction underperforms the market:
Example 3(Inaccurate forecaster can profit).Consider an event with two outcomes and let p=
(0.9,0.1) , q= (0.5,0.5) , and p∗ = (0.6,0.4) . Under the quadratic scoring rule, since ∥p∗ −p∥>
∥p∗ −q∥ , the forecaster underperforms the market. If the forecaster places a bet on the first outcome,
which is a highest-margin outcome, their expected profit is(1,0)·(p ∗ −q)>0.
This paper resolves this seemingly broken link between statistical accuracy and profitability in the
examples above. We first define, for every proper scoring rule S, what we call aproperbetting
strategy corresponding toS.
3This is the generalized solution for many-outcome Kelly criterion. The familiar two-outcome Kelly formula of spending
p1−q1
1−q1 to bet onoutcome 1 (short it if negative) is a special case. To see this, observe that, given q∈∆ K, betting
p1−q1
1−q1 =p 1 −q 1 1−p1 1−q1 onoutcome 1and 0 onoutcome 2is equivalent to additionally buying 1−p1 1−q1 shares of bothoutcome 1at priceq 1 and2at price1−q 1, leading to total bet amountp 1, p2 onoutcome1,2respectively.
5

Definition 2(Proper betting strategy).Under a proper scoring rule S with potential function G, the
properbetting strategy for a forecastpand a market priceqis the position vector
sG(p,q) :=∇G(p)− ∇G(q).
Note that if some k’th entry of sG(p,q) is negative, the corresponding execution is to buy aNOT k
contract at the price of1−q k (assuming no bid-ask spread for now).
3.1 Proper betting and its robust profitability
On robust profitability.We now establish a formal link between a good forecast that outperforms
the market and its betting profitability. A fundamental challenge in designing good betting strategies
is that we almost never observe the ground truth probability p∗. Even when a forecast p is promised
to have better score than the market q — in the sense that S(p;p ∗)≥S(q;p ∗) for some proper
scoring rule S — this can hold true for infinitely many possible p∗’s. Thus, a desirable property of a
good betting strategy isrobust profitability: it is guaranteed to have positive profit for any p,p ∗,q
satisfying S(p;p ∗)≥S(q;p ∗). Conversely, we say a strategy s(p,q) is not robustly profitable
under S, if there exists some p̸=q,p ∗ such that S(p;p ∗)≥S(q;p ∗) but s(p,q) has non-positive
expected profit under p∗. Note that “profitability” here is a binary notion: it concerns only whether
positive profit can be guaranteed, not the magnitude of that profit.
Our first main result shows that robustly profitable betting strategy exists whenever the market’s
liquidity loss is relatively small; in fact, the proper betting sG(p,q) as defined in Definition 2 is such
a strategy.
Theorem 1(Robust profitability of proper betting).For any ground truth p∗, forecast p, market
price q, and strictly proper scoring rule S with potential function G, the expected profit π(s∗,p ∗) of
the proper betting strategys ∗ =s G(p,q)admits the following decomposition:
π(s∗,p ∗) =S(p;p ∗)−S(q;p ∗)| {z }
score gap
+D G(q,p)| {z }
Bregman divergence
−L ρ(s∗;q)| {z }
liquidity loss
.(1)
Therefore, if DG(q,p)≥L ρ(s∗;q) — i.e., the divergence offsets liquidity loss — then proper betting
isrobustly profitablein the sense that it ensures positive profit wheneverS(p;p ∗)> S(q;p ∗).
Proof. The proof hinges on an interesting profit decomposition lemma below that may be of indepen-
dent interest.
Lemma 1(Profit decomposition lemma).For any realized outcome y, forecast p, market price q,
and scoring ruleS(p, y)with potential functionG(not necessarily proper), we have
sG(p,q)·(1 y −q)| {z }
Idealized profit from outcomey
=S(p, y)−S(q, y)| {z }
Realized score gap
+D G(q,p)| {z }
Bregman divergence
.(2)
Proof of Lemma 1.We express
S(p, y)−S(q, y) = (G(p)−G(q)) +∇G(p)·(1 y −p)− ∇G(q)·(1 y −q)
= (−∇G(p)·(q−p)−D G(q,p)) +∇G(p)·(1 y −p)− ∇G(q)·(1 y −q)
= (∇G(p)− ∇G(q))·(1y −q)−D G(q,p)
=s G(p,q)·(1 y −q)−D G(q,p)
where
DG(q,p) =G(q)−G(p)− ∇G(p)·(q−p)
is theBregman divergencebetweenpandq.
6

Taking expectation of Equation (2) over y∼p ∗ yields the (frictionless) expected profit of the proper
bet,
sG(p,q)·(p ∗ −q) =S(p;p ∗)−S(q;p ∗)| {z }
score gap
+D G(q,p)| {z }
Bregman divergence
.
Notably, the term sG(p,q)·(p ∗ −q) is not the expected profit π(s∗,p ∗) yet since it counts the
betting cost using the same market price q for purchasing sG(p,q) contract shares, ignoring the
slippage. This gap is captured precisely by the third term in Eq. (1) Lρ(s;q) =
R 1
0 ρ(ts)·sdt−s·q .
These together prove the theorem.
Like the profit decomposition of Lemma 1, Theorem 1 also holds “point-wise” for each realized
outcome y∼p ∗. Indeed, this corresponds to the special case of p∗ =1 y. These point-wise
equalities will allow us to generalize the guarantee of proper betting to empirical scores as discussed
in Section 3.3.3.
Remark 2.The key insight from Theorem 1 is to realize that sG(p,q) :=∇G(p)− ∇G(q) is the
“proper” strategy to use and its profit admits a clean characterization. The decomposition of Lemma 1
formalizes a natural intuition: a profitable forecast is not merely about being accurate (i.e., having
big score gap), but is about sufficiently different from the market yet still remains sufficiently accurate.
Conversely, positive profit does not imply accuracy: it can be attributed entirely to the Bregman
bonus. This also explains the paradox in Example 3: when a forecaster’s prediction is far from the
market priceq, a large Bregman divergence can outweigh a negative score gap.
Remark 3(Beyond simplexes).Notably, Theorem 1 holds even when q̸∈∆ K. As an interesting
application, we can also apply it when Q:= PK k=1 qk <1 , i.e., there is trivial arbitrage opportunity
by buying s=1 at cost Q(<1) with a deterministic return 1 (assuming little liquidity loss).
Theorem 1 captures this situation as a special case. By choosing G(q) = (PK k=1 qk)2, we can verify
that the proper betting sG = 2[PK k=1(pk −q k)]·1 , leading to deterministic profit 2(1−Q) 2 for any
p∗. It can be further verified that both Bregman divergence and score gap term equal(1−Q) 2 in
this case, summing up to the2(1−Q) 2 profit.
3.2 Proper betting is (essentially) the only robustly profitable strategy
Theorem 1 establishes the robust profitability of proper betting in a market with low liquidity loss.
Our second main result further shows that it is the only robustly profitable strategy, essentially —
the reason of “essentially” is to rule out trivial transformations such as rescaling the strategy (i.e.,
λsG(p,q) ) or adding a constant shift (i.e., sG(p,q) +λ1 ), which will not change the profitability
nature of the strategy.
Definition 3(Essentially different betting).We say a betting strategy s(p,q) isessentially different
from another strategy s′(p,q) if, after any rescaling of s(p,q) via mapping s→λs and constant
shifting via s→s+λ1 , there always exists an interior market price q∈int(∆ K) such that
||s(pt,q)−s ′(pt,q)|| ≥ϵfor some forecast sequence{p t}∞ t=1 converging toq.
If two strategies are not essentially different, we say they areessentially the same.
It is natural that rescaling and constant shifting should not lead to an intrinsically different betting
strategy: rescaling only proportionally changes betting sizes, whereas placing the all-one bet 1 costs
1·q= 1 and pays off 1 deterministically. The only non-trivial requirement for essentially different
betting strategies is that they need to have non-negligible difference (i.e., at least ϵ difference)
for some sequence of forecasts {pt}∞ t=1 converging to q. This is a natural (and also necessary)
requirement because otherwise two robustly profitable betting strategies can be superficially different.
For instance, given any robustly profitable strategy, e.g., our proper betting sG(p,q) , one can
construct s(p,q) =s G(p,q) +ϵe 1 simply by additionally buying ϵ amount of the first contract for
some ϵ smaller than the profit of sG(p,q) , which is at least the Bregman divergence DG(q,p) as we
will show. This negligible modification can be done even for infinitely many pairs of p,q so long as
they are all separated apart by at least a constant distance. Thus the real test of difference is at the
7

limit when p→q . Definition 3 is introduced precisely for that: two strategies s,s ′ are essentially
different if their difference s(pt,q)−s ′(pt,q) does not converge to 0 – at least for some market
priceqand some sequence of forecasts{p t}∞ t=1 converging toq.
Our second main theorem is stated below.
Theorem 2.Any robustly profitable betting strategy is essentially the same as the proper betting
sG(p,q) . Formally, for any proper scoring rule S and any betting strategy s(p,q) that is essentially
different from sG(p,q) , there exists p,p ∗,q such that S(p,p ∗)> S(q,p ∗) but the expected profit
ofs(p,q)is strictly negative. This holds even for frictionless markets, i.e.,L ρ = 0.
Proof sketch of Theorem 2. The proof is somewhat technical. We defer full proof to Section B.1
and only overview the proof ideas here. First, observe that it suffices to prove the theorem for
frictionless markets since if any betting strategy is robustly profitable, then it must remain profitable
in a frictionless market simply due to lower cost. Our proof thus argues that any robustly profitable
betting strategy in a frictionless market is essentially the same as proper betting. Given a betting
strategy s(pt,q) that is essentially different from proper betting sG(pt,q) , our proof here features
an explicit construction of an infinite sequence of tuple (pt,p ∗ t ,q) and then leverages convergence
properties to prove the existence of tuples in this sequences that satisfies S(pt,p ∗ t )−S(q,p ∗ t )>0
but the expected profit ofs(p t,q)under the constructedp ∗ t is strictly negative.
A simple special case of Theorem 1 is for the K= 2 case, i.e., binary event betting. Note that
rescaling via mapping s→λs and constant shifting via s→s+λ1 will not change a betting
strategy s’s robust profitability. Then any betting strategy s, normalized to have ||s||= 1 and
s·1= 0 , is either s+ = (1/ √ 2,−1/ √ 2)⊤ (i.e., buying √ 2 ofYES) or s− = (−1/ √ 2,1/ √ 2)⊤ (i.e.,
buying
√
2 ofNO). If betting strategy s is essentially different from proper betting sG, then there
exists q and a sequence {pt}∞ t=1 converging to q such that thenormalized s(pt,q),s G(pt,q) satisfy
||s(pt,q)−s G(pt,q)|| ≥ϵfor some constant ϵ. This implies that s(pt,q),s G(pt,q) must equal
s+, s− respectively. Therefore, if sG(pt,q) is profitable, its opposite purchase behavior s(pt,q)
cannot be profitable, aligning with the theorem’s statement. While this case with K= 2 is easy to
see, the case with K >2 becomes much more non-trivial since there are infinitely many normalized
betting strategies. The formal proof in Section B.1 needs to leverage the geometry of the normalized
strategy space.
3.3 Implications and real market considerations
3.3.1 A new characterization of proper scoring rules via betting profitability.
A keen reader might observe that the proper betting strategy sG(p,q) is well-defined for any G, not
only those G that are convex and correspond to proper scoring rules. Is properness of the scoring
rule necessary to guarantee the robust profitability of sG(p,q) ? Our next proposition show that
properness of the scoring rule is indeed necessary, in a very strong sense. That is, ifp,q are compared
by some scoring rule S satisfying S(p;p ∗)> S(q;p ∗), the properness of S is necessary to guarantee
the existence of a robustly profitable betting strategy (and when it exists, proper betting is one such
strategy).
Proposition 2(Equivalence between score properness and robust profitability).A scoring rule
S(p, y)is strictly properif and only ifthere exists a robustly profitable betting strategy s(p,q) that
guarantees positive profit in a frictionless market (i.e., Lρ = 0) for any p∗ and p̸=q satisfying
S(p;p ∗)≥S(q;p ∗).
Proposition 2, proven in Section B.2, thus yields a novel characterization of proper scoring rules as
precisely those rules that yield robustly profitable betting strategy when a forecast p outperforms
marketqunder the scoring rule.
8

3.3.2 Proper betting is a strict generalization of canonical betting in AMMs
All our results thus far are applicable to any prediction market. Here we illustrate what proper betting
strategy corresponds to in the special case ofautomated market makers(AMMs) and show that it is a
strict generalization of the canonical betting strategy in AMMs.
An AMM is governed by a strictly convex cost function C(x) such that the current market price
q∈∆ K and net number of shares of each contract x∈R K always satisfies ∇C(x) =q [Hanson,
2007, Chen and Pennock, 2007]. A key property of AMMs is that if a forecaster’s belief is some
p, then this forecaster maximizes their expected profit by purchasing shares sq→p that moves the
market price from q to p, i.e., ∇C(x+s q→p) =p (see Section A for more details). Interestingly,
we observe that the above canonical betting strategy in AMMs corresponds precisely to the proper
betting strategy of Definition 2 under the corresponding market scoring rule, or formally stated below
Fact 1.In automated market makers, we haves q→p =s G(p,q).
To see this, we recall that the convex conjugate of the cost function C(x) of an AMM, G(p) =
supx∈RK {p·x−C(x)} , is precisely the convex potential that induces the market scoring rule
S(p, y) =G(p) +∇G(p)·(1 y −p) . A basic fact about convex conjugates is that the inverse of
the gradient function ∇G: ∆ K →R K is precisely the ∇C(x) function. Observing x+s q→p =
(∇C) −1(p), we have the betting strategy
sq→p =x+s q→p −x= (∇C) −1(p)−(∇C) −1(q) =∇G(p)− ∇G(q) =sG(p,q).(3)
A basic fact in AMMs is that the profit π(p,q) for moving the market from current price q to new
price p is S(p,p ∗)−S(q,p ∗) for ground truth distribution p∗ [Hanson, 2007], which corresponds
precisely to the first term of Theorem 1. This is not a coincidence since, as it turns out, the divergence
term and liquidity loss term in Theorem 1 cancel out precisely in any AMM, as stated below (proved
in Section B.3).
Corollary 1(Instantiation of Theorem 1 in AMMs).Consider any AMM governed by a strictly
convex cost function C(x) and let S denote its corresponding market scoring rule determined by
C’s convex conjugate G(p). Then we have DG(q,p) =L ρ(s∗;q) for the proper betting strategy
s∗ =∇G(p)− ∇G(q). Hence the profit ofs∗ isS(p,p ∗)−S(q,p ∗).
Remark 4(Additional justification for the canonical betting strategy sq→p).The foundational result
of Hanson [2003, 2007] already implies that the betting strategy sq→p(=s G(p,q)) that moves the
market price from q to p in AMMs is robustly profitable in the sense that it guarantees positive profit
whenever the forecast p beats the market under the ground truth p∗. Our Theorem 2 provides an
additional justification and shows that this is essentially the only robustly profitable strategy.
3.3.3 Extensions to empirical scores
In practice the ground truth p∗ is unobservable, therefore a forecaster’s advantage over the market on
a single event in expectation can never be validated. What is validatable however is the advantage
on empirical scores. A practical question thus is whether proper betting can convert empirical score
advantages to realized profit. The answer turns out to beYes, inherently due to the fact that Theorem 1
holds also for realized outcome y and can then be averaged over a sequence of outcome realizations.
Suppose we only see realized outcomes y1, . . . , yn across a sequence of n events with predictions
p1, . . . ,pn and market pricesq 1, . . . ,qn. Let the empirical forecast and market scores be
ˆSF := 1 n X i S(pi, yi)and ˆSM := 1 n X i S(qi, yi).
Theorem 1 can be extended from a single-event to an empirical version below.
Corollary 2(Empirical version of Theorem 1).The sequential proper bet si :=s G(pi,q i) on a
realized sequence of outcomesy 1, . . . , yn yields the following realized average profit:
1
n
nX
i=1
si ·(1 yi −q i) = ˆSF − ˆSM + 1 n
nX
i=1
DG(qi,p i)− 1 n
nX
i=1
Lρ(si;q i).
9

Hence the sequential proper betting has positive profit if the gap ˆSF − ˆSM of empirical scores and
average divergence 1 n Pn i=1 DG(qi,p i) together offset the average liquidity loss 1 n Pn i=1 Lρ(si;q i).
In Section 4, we experimentally observe a few forecasting agents profiting due to divergence from
the market despite below-market accuracy.
Remark 5(Bet sizes should vary across events).A natural intuition is that a forecaster whose
accuracy is measured with equal weight across events should place equal bet size on these events.
Corollary 2 says otherwise: the correct bet sizes are proportional to si =∇G(p i)− ∇G(qi), with
larger bets on events where the forecaster’s prediction deviates more from the market.
3.3.4 Extension to non-zero bid-ask spreads and correlated market outcomes.
In real prediction markets, factors such as low liquidity or platform transaction fees imply a positive
difference between the lowest price at which someone will sell and the highest price at which someone
will buy. For the k-th outcome of an event, a real market has q+ k +q − k ≥1 , where q+ k denotes the
market price for buying the outcome (bid price) and q− k denotes the market price for selling the
outcome (ask price). Theorem 1 is not directly applicable to this situation because when any k’th
entry of the proper betting ∇G(p)− ∇G(q)is negative, its execution requires buyingNOT k at price
1−q + k , which is not possible here since the price ofNOTkisq − k (>1−q + k ).
The key idea to extend Theorem 1 to such real-world settings withq+ k +q − k >1 is to decompose each
outcome k∈[K] into twobinary outcomeevents,YES k andNOT k, that have prices equal to q+ k
and q− k respectively. It can be shown that a proper betting will buyYES k contracts when pk > q+ k ,
buyNO k contracts when pk <1−q − k , and not act when 1−q − k ≤p k ≤q + k . Moreover, this can
be further extended to situations when the K outcomes are not completely disjoint. For instance, a
popular event on prediction markets is to predict bitcoin price where the outcome could be “price at
least $7K”, “price at least $8K”, etc. In such cases, we treat each single outcome as a separate binary
market. The full details of the reductions can be found in Section C.1.
3.3.5 Extension to sequential betting.
Events in prediction markets often take days or weeks to resolve, during which both the forecaster’s
prediction pt and the market price qt evolve in response to the revelation of new information.
Section C.2 extends Theorem 1 to this dynamic setting via two strategies: afundamental-driven
strategy that executes the proper bet sG(pt,q t) at each round and holds positions to resolution, and a
momentum-driven strategy that maintains sG(pt,q t) as a rebalanced position. Both inherit the profit
decomposition of Theorem 1 summed across rounds, and the comparison reveals what each strategy
needs for its performance guarantee: a per-round accuracy edge against the unobservable ground
truth p∗ (fundamental), versus a per-round accuracy edge against the next-step market price qt+1
(momentum) — an operationally observable condition.
4 Experiments
Testing betting strategies requires data that pairs forecasts with contemporaneous market prices
and realized outcomes. Such data is hard to collect from human forecasters at scale, but recent
AI forecasting benchmarks built on real-money prediction markets—most notably Prophet Arena
[Yang et al., 2025]—provide a scalable alternative. We therefore use AI forecasts across thousands
of archived markets to evaluate how different betting strategies translate predictive accuracy into
realized returns. The evaluation has two stages: first, an offline study on the historical benchmark,
where we simulate each market under zero price impact; second, a live pilot test in real prediction
markets, exposing our strategy to the full set of real-market frictions.
4.1 How good are proper betting strategies?
We use forecasts made by 18 frontier models, each with predictions on at least 600 resolved Kalshi
and Polymarket events (up to approximately 3,900 events for the most heavily covered models), for a
10

Table 2:Pairwise comparison of the Proper Betting (Brier) strategy against each of the four baseline
heuristics for selected top forecasting agents, with each column reporting the difference between
Proper Betting and the corresponding heuristic. Confidence intervals are paired, event-clustered 95%
bootstrap intervals; bold values highlight the differences whose CI excludes zero.
Model∆S−Max (Mkt)−Max (Grp)−Inv-Margin−Kelly-Alike−Kelly
Gemini 3.1 Pro (B)+0.0076[+0.0014, +0.0136]+30.3[+20.7, +39.9]+30.1[+15.5, +42.9]+39.2[+27.7, +50.6]+24.3[+16.1, +32.8]+138.9[+127.3, +150.4]
Claude Fable 5+0.0039[+0.0008, +0.0073]+26.8[+15.3, +40.0]+48.3[+34.2, +63.1]+33.6[+20.0, +48.9]+16.8[+7.3, +27.4] +129.0 [−1.3×10 9, +141.8]
GPT-5.6 Sol+0.0033[+0.0003, +0.0067]+22.4[+12.2, +35.4]+39.9[+24.3, +55.7]+28.5[+15.7, +43.7]+15.7[+6.0, +27.1] -1220.4 [−2.2×10 8, +122.5]
GPT-5.5 (B) -0.0059 [-0.0129, +0.0009]+13.0[-1.2, +29.3]+20.3[-0.7, +41.1]+18.6[+0.1, +38.9] +8.6 [-2.7, +21.4]+116.8[+99.8, +136.0]
GPT-5.5 (C) -0.0056 [-0.0101, -0.0012] +8.8 [-1.5, +18.7] +3.6 [-28.4, +27.3] +7.0 [-5.5, +19.4] +2.0 [-6.3, +10.0]+107.3[+94.9, +119.2]
total of 94,453 forecasts4 collected in collaboration with Sooth Labs, spanning a variety of domains
such as sports, politics, economics, and crypto. Letters appended to model names denote distinct
prompt variants of the same underlying model.5 Each market includes a forecast, contemporaneous
market price, and realized outcome (YES/NO). For each model and betting strategy, we apply the
strategy to historical forecast–market (bid and ask) price pairs, simulate the resulting trades, and
compute the realized return after market resolution, allowing us to compare proper betting strategies
directly against standard heuristic baselines.
Specifically, each betting strategy is to determine a set of weights — how to allocate a fixed budget
and on what direction — over a collection of prediction markets with forecasts and market prices. We
implement the three proper betting strategies according to Table 1. We also consider a few baseline
strategies derived from a few intuitive heuristics: (i)Max-Margin, which concentrates capital
on the largest disagreements with the market, either across all markets or by selecting the single
largest-margin bet per event group; (ii)Inverse-Margin, which down-weights large disagreements
under the assumption that extreme deviations are less reliable; (iii)Kelly-Alike, which scales
exposure according to Kelly-style edge-to-odds ratios 6; and (iv)Kelly Criterion[Kelly, 1956],
which maximizes asymptotic log-wealth growth. Appendix D.2 expands on the formal setup and
implementation details of the betting strategies.
Table 2 reveals why proper betting strategies warrant study: heuristic allocations fail to yield consistent
positive returns, and for stronger models, Brier-weighted allocation is the only strategy that reliably
produces positive ROI. Inverse-Margin limits downside for weaker models by concentrating capital
on near-market (i.e., minimal risk) bets, but as a consequence of its design, also limits opportunities
for creating meaningful upside. More generally, these failures of heuristic betting strategies show that
predictive accuracy alone is insufficient to create profit. How probabilities are translated into position
sizes is a key determinant of returns, motivating the study of proper betting strategies. Appendix D.2
reports the results for all evaluated models.
4.2 How to choose proper betting strategies for different forecaster personas?
Score gap vs. divergence.Table 3 empirically illustrates the decomposition in Lemma 1. We report
the proper score gap and divergence terms summed across bets and normalized by total spend, which
exactly matches with the per-bet decomposition in Equation 1 in ROI units. This highlights how
proper betting strategies induce trade-offs between accuracy and divergence. Profitability depends
not only on the score gap (∆S), but also on the divergence term (D), so models with worse accuracy
can still achieve higher ROI if they generate sufficiently large divergence. For example, under the
Log rule, Gemini 3.1 Pro (B) achieves higher ROI than GPT 5.6 Sol despite a worse score gap.
Moreover, a model’s score under a given scoring rule does not by itself determine which rule yields
the best returns, since divergence is rule-dependent. For instance, for GPT 5.5 (B), Brier yields
a worse score gap than Log ( −15.4 vs. −9.5) but higher ROI (+16.8% vs. +11.7%), driven by a
4Many forecasts may be made per event at different times
5Full betting data is releasedhere.
6In empirical tests, we determine the Kelly criterion performs particularly poorly because it is highly sensitive to miscali-
brated probabilities. As a result, it becomes highly unstable under model error.
11

Table 3: ROI decomposition on the expanded dataset, where ROI = ∆S+D for each model and
proper scoring rule. Bold denotes significantly positive score gaps (95% CI above zero), and bold
italic denotes significantly positive ROI.
Model Brier∆SBrierDBrier ROI Log∆SLogDLog ROI Sph∆SSphDSph ROI Events
Gemini 3.1 Pro (B)+11.7[+2.4, +21.1]+27.2[+22.7, +32.1]+38.9[+27.4, +50.9]+7.5[+0.8, +14.0]+20.9[+18.2, +23.8]+28.4[+20.4, +36.2]+11.3[+3.5, +19.5]+21.9[+18.3, +25.8]+33.2[+23.9, +42.9]1113
Claude Fable 5+12.3[+3.2, +22.0]+16.7[+11.8, +22.2]+29.0[+16.7, +42.7]+8.6[+1.3, +15.6]+12.9[+9.8, +16.5]+21.5[+12.2, +30.6]+10.2[+1.4, +18.6]+11.9[+8.5, +15.9]+22.1[+11.6, +33.0]1140
GPT-5.6 Sol+10.9[+1.0, +21.7]+15.9[+12.1, +21.9]+26.7[+14.4, +41.4]+10.7[+3.0, +18.5]+12.6[+10.1, +16.1]+23.3[+14.5, +32.4]+12.1[+3.2, +21.4]+11.4[+8.5, +15.7]+23.5[+13.0, +35.8]866
GPT-5.5 (B) -15.4[-29.6, -0.4]+32.2[+25.8, +39.5]+16.8[+2.3, +33.3]-9.5[-20.7, +0.5]+21.2[+17.9, +24.9]+11.7[+0.3, +22.2]-11.5[-23.0, -0.7]+24.4[+19.4, +30.1]+12.9[+0.9, +25.0]842
GPT-5.5 (C) -15.6[-26.3, -5.6]+22.9[+18.6, +27.3]+7.3[-3.3, +17.3]-13.1[-21.4, -5.5]+18.4[+15.2, +21.6]+5.2[-3.8, +13.9]-14.6[-23.4, -6.2]+16.5[+13.4, +20.1]+1.9[-6.6, +10.7]979
Aggressive Conservative
Dispersed Brittle
Low Proportion
Small-Margin Bets
High Proportion
Small-Margin Bets
High Accuracy
Consistency
Low Accuracy
Consistency
(a)Taxonomy of LLM forecasting personas by
proportion of forecasts at small margins and
accuracy consistency across margins.
0.0 0.1 0.2 0.3 0.4 0.5
Margin size
0.0
0.1
0.2
0.3Bet share
Conservative
0.4
0.5
0.6
0.7
0.8
Win rate
0.0 0.1 0.2 0.3 0.4 0.5
Margin size
0.0
0.1
0.2
0.3Bet share
Aggressive
0.4
0.5
0.6
0.7
0.8
Win rate
0.0 0.1 0.2 0.3 0.4 0.5
Margin size
0.0
0.1
0.2
0.3Bet share
Brittle
0.4
0.5
0.6
0.7
0.8
Win rate
0.0 0.1 0.2 0.3 0.4 0.5
Margin size
0.0
0.1
0.2
0.3Bet share
Dispersed
0.4
0.5
0.6
0.7
0.8
Win rate
(b)Each panel shows a persona’s margin distri-
bution (grey, left axis) and win-rate at different
margins (color, right axis).
Figure 1:Schematics for synthetic forecasting personas and their prediction profiles.
substantially larger divergence term (32.2 vs. 21.2). As such, identifying the most profitable models
and betting strategies is non-trivial, as profitability depends not only on accuracy but also on how
those strategies factor in disagreement with the market. Appendix D.3 reports the decomposition
results for all models.
Forecaster personas.As seen in Table 3, different scoring rules yield materially different returns. To
identify when each rule is preferable, we construct a controlled experiment using four synthetic model
“personas” that all achieve the same Brier score on the same set of real prediction markets, but differ
in how their predictions deviate from market prices. We focus on the margin range |p−q| ∈[0,0.5] ,
as higher-margin forecasts are too sparse in empirical models to support reliable or broadly applicable
analysis; although rare, such high-margin bets can occasionally be correct and highly profitable,
which we examine further in Section D.8. We run the experiment in two regimes—one where the
model beats the market and one where it loses—to examine how accuracy interacts with the choice
of proper betting strategy and the resulting implications.
Persona design and motivation.We use 27,516 markets across 3,511 questions collected from
the Prophet Arena pipeline between August 1, 2025 and April 15, 2026. Models differ in how
aggressively they deviate from market prices, and in whether those deviations tend to pay off. To
capture this variation, we construct personas defined by two features: (i) the proportion of small-
margin bets (i.e., |p−q| ≤0.15 ), and (ii) the accuracy drop-off across margins, measured by the
slope of the directional win rate (the fraction of bets whose chosen side matches the realized outcome)
as a function of margin size |p−q| . Both regimes are calibrated to a fixed ±0.05 relative quadratic
scoring rule gap. Section D.4 outlines the details of the synthetic forecast generation process.
We define four personas spanning representative combinations of these dimensions, as shown in
Figure 1.Conservativemodels concentrate most forecasts in the small-margin region and exhibit
flat accuracy across margins.Aggressivemodels place fewer small-margin bets, with accuracy
remaining flat across margins.Dispersedmodels spread bets broadly across margin sizes and show
a gradual decline in win-rate as margin increases.Brittlemodels have a significant proportion of
12

Model S-M Share∆SROI
GPT-5.2 (B) 0.82−0.044−4.4(L)
Grok 4.1 0.80−0.053−9.1(L)
Brittle 0.80 −0.054 −8.6 (L)
LLaMA 4 0.67−0.115−4.9(L)
DeepSeek R1 0.59−0.140−5.4(L)
Dispersed 0.64 -0.120 -7.2 (L)
Gemini 3 0.94 +0.002 +14.2 (B)
Claude Opus 0.89 +0.000 ∗ +17.5 (B)
Conservative 0.91 +0.001 +15.8 (B)
(a)Persona classification across models. ROI re-
ported is under the best proper scoring rule: Log
(L) or Brier (B). ∗ denotes a positive ∆S rounded
to+0.000.
0.0 0.1 0.2 0.3 0.4 0.5
Margin size  |p q|
0
10
20
30
40
50
60
70Win rate (%)
Dispersed ( = 3.6)
Brittle ( = 6.8)
Conservative ( = 0.0)
Brittle
Dispersed
Conservative
Profitable bin
Unprofitable bin
(b)Binned per-bet win rate vs. margin |p−q| . Each
dot has area proportional to profit for their persona.
Dashed lines are OLS fits where β denotes the slope.
Overlapping points are jittered horizontally for clarity.
Figure 2:Mapping real models to personas.
small-margin forecasts but exhibit a sharply declining win-rate as margin increases. For further
details, see Appendix D.4.
Table 4:Simulated persona ROI (%) under proper betting strategies. S-M Share denotes the share of
forecasts with small margin: |p−q| ≤0.15. Consistency is the OLS slope of per-bet directional win
rate against margin size.
Regime A (Outperforms) Regime B (Underperforms)
Persona S-M Share Consistency Brier Log Sph. Brier Log Sph.
Conservative 0.850.0 +48.8+46.2 +44.8 -76.8-71.5-82.7
Aggressive 0.580.0 +37.7+37.4 +31.3 -38.8-30.1-46.9
Dispersed 0.68−0.2 +44.3+42.5 +38.6 -30.4-20.7-38.1
Brittle 0.77−0.6 +45.4+43.8 +41.0 -60.2-52.2-67.9
We evaluate each persona under two regimes: Regime A, where the model outperforms the market
and all strategies yield positive ROI, and Regime B, where it underperforms and all strategies incur
losses. A symmetric ±0.05 quadratic score gap (market quadratic score = 0.839) isolates the effect
of persona and strategy while holding average accuracy constant.
As shown in Table 4, Brier is optimal in Regime A for all personas, while Log is optimal in Regime B.
In Regime A, the positive Brier gap implies that expected returns are positive across margin bins, so
linear scaling in |p−q| is optimal. In Regime B, losses are dominated by high-margin errors, making
Log’s sublinear weighting preferable as it attenuates exposure to large, costly mistakes. This effect
is most pronounced for Conservative personas, which must incur a high error rate on small-margin
bets to sustain a negative Brier gap, leading to broad losses. Additional analysis and weighting
visualizations are provided in Section D.5.
Mapping real models to personas.To map synthetic personas to real model behavior, we evaluate
each model along the two defining dimensions: small-margin forecasts and accuracy consistency.
Because these patterns only emerge reliably at scale, we evaluate each model on its full event history
rather than the standardized subset of events. Figure 2 summarizes these results, with Figure 2a
showing models’ proportion of small-margin forecasts and Figure 2b showing the win-rate profiles
as a function of margin size. For classification of all evaluated models and additional analysis, see
Appendix D.6.
13

Along the margin dimension, models separate cleanly into the three persona groups: Brittle models
concentrate most bets at small margins, Dispersed models spread forecasts more broadly across
margins, and Conservative models place nearly all bets at small margins. Figure 2b further confirms
the taxonomy along the accuracy-consistency dimension: Brittle models exhibit a steep decline in
win rate as margins increase, Dispersed models decline more gradually, and Conservative models
remain roughly flat across margins. Taken together, these results show that personas provide a simple
way to summarize how model behavior translates into returns. This abstraction lets us reason about
profitability and select or adapt betting strategies based on these behavioral patterns.
4.3 A live pilot test under active portfolio management
We further evaluate proper betting in a live portfolio setting using the momentum-driven strategy
described in Section 3.3 (with details deferred to Appendix C.2). Notably, our main goal here is
NOT to establish statistically reliable trading alpha or optimal risk-adjusted performance, which is
impossible for us given both our resource and legal constraints. Instead, these experiments represent
our attempt to go beyond pure simulation studies andtest whether proper betting can survive live
executionwhich – unlike the previous backtests – must contend with bid–ask spreads, limited
liquidity, slippage, and discrete tick sizes. As a result, even accurate forecasts may not translate
cleanly into realized returns, since trades must be executed at available prices rather than idealized
market probabilities.
We deploy Gemini 3 using the Brier-derived betting strategy on Kalshi events for 26 days (April/May
2026) with an initial budget of $200. Operating on a fixed two-hour cadence, the agent evaluates all
open markets satisfying an ex-ante eligibility filter that excludes contracts with ambiguous resolution
criteria and settings known to impair LLM forecasting performance (see Section D.7.2). Summary
statistics and cumulative ROI from the live pilot test are shown in Figure 3, whereas the trading
historyis documented here, which logs performance of the trading agent over the trading period.
Over the trading period, the agent executed 236 orders across 129 markets, achieving a 3-trimmed
ROI (i.e., dropping both best 3 and worst 3 trades) of+24.2%, whereas the untrimed ROI is +80.33%
(a P&L-weighted Brier decomposition attributes ∆S= +0.7205 and D= +0.0828 . The Sharpe
ratio is3.35, with a 90% confidence interval of [0.9,6.12] . Note that we report the Sharpe ratio only
for the live test, where the daily returns form a continuous time series amenable to risk-adjusted
analysis; the previous offline experiments resolve each event independently and most models post
negative returns, so a Sharpe ratio there would be uninformative.
We document the full implementation, analysis of representative trades, and trading logs in Sec-
tion D.7.
5 Conclusion
We investigate the puzzle that forecasters can outperform prediction markets in accuracy yet still lose
money, by establishing a formal equivalence between predictive accuracy and trading profitability.
Key to our result is to identify a “proper” betting strategy for arbitrary prediction markets. Moreover,
we demonstrate that this strategy strictly generalizes the canonical betting strategy only applicable to
the special AMM markets, is essentially the only robustly profitable strategy, and has deep connection
to proper scoring rules. Through this lens, it is unsurprising that proper betting emerges as the only
strategy reliably converting accuracy into ROI across thousands of archived AI forecasts. While our
live experiments in the real Kalshi markets is limited, due to both resource and legal constraints, the
month-long live pilot test with +24.2% (trimed) ROI and 3.35 Sharpe ratio does hint on the promise
of practical viability of our theory.
Several future directions remain open. First, our persona analysis in Section 4.2 hints at the potential
ofdata-adaptive scoring-rule selection: identifying the most suitable rule for each forecaster. Second,
the framework opensmarket-designquestions on which scoring rules and market structures best
14

Starting capital $200.00
Trading days 26
Forecasts issued 1,605
Trade signals placed (filled) 396 (236)
Markets traded 129
Ending capital $360.67
ROI+80.33%
3-trimed ROI +24.2%
Sharpe ratio (
√
365)3.35
90% CI of Sharpe[0.90,6.12]
Shares transacted 2,657
Exchange fees paid $26.31
Win rate50.9%
maximum drawdown $31.47 (15.7%)
(a)Live trading statistics for the Gemini 3 agent
on Kalshi.
1 5 10 15 20 25
Trading day
−20%
0%
+20%
+40%
+60%
+80%ROI (%)
(b)ROI over trading days of the forecaster’s live Kalshi
trades over 26 trading days.
Figure 3:Live pilot results for the Gemini 3 trading agent on Kalshi prediction markets.
elicit accurate forecasting from participants at scale. Finally, our guarantees concernexpectedprofit;
extending them to risk-adjusted criteria would narrow the gap between theory and live deployment.
References
Jacob Abernethy, Yiling Chen, and Jennifer Wortman Vaughan. Efficient market making via con-
vex optimization, and a connection to online learning.ACM Transactions on Economics and
Computation (TEAC), 1(2):1–39, 2013.
Kenneth J. Arrow, Robert Forsythe, Michael Gorham, Robert Hahn, Robin Hanson, John O. Ledyard,
Saul Levmore, Robert Litan, Paul Milgrom, Forrest D. Nelson, et al.The Promise of Prediction
Markets. Science and Technology Policy Institute, 2008.
Joyce Berg, Robert Forsythe, Forrest Nelson, and Thomas Rietz. Results from a dozen years of
election futures markets research.Handbook of experimental economics results, 1:742–751, 2008.
Glenn W. Brier. Verification of forecasts expressed in terms of probability.Monthly Weather Review,
78(1):1–3, 1950.
Yiling Chen and David M. Pennock. A utility framework for bounded-loss market makers. In
Proceedings of the 23rd Conference on Uncertainty in Artificial Intelligence (UAI), pages 49–56,
2007.
Yiling Chen and Jennifer Wortman Vaughan. A new understanding of prediction markets via no-regret
learning. InProceedings of the 11th ACM conference on Electronic commerce, pages 189–198,
2010.
Yiling Chen, Stanko Dimitrov, Rahul Sami, Daniel M Reeves, David M Pennock, Robin D Hanson,
Lance Fortnow, and Rica Gonen. Gaming prediction markets: Equilibrium strategies with a market
maker.Algorithmica, 58(4):930–969, 2010.
Thomas M Cover. Universal portfolios.Mathematical finance, 1(1):1–29, 1991.
Joshua Della Vedova. Who profits from prediction markets? execution, not information. 2026.
Tilmann Gneiting and Adrian E Raftery. Strictly proper scoring rules, prediction, and estimation.
Journal of the American statistical Association, 102(477):359–378, 2007.
15

Irving John Good. Rational decisions.Journal of the Royal Statistical Society: Series B (Method-
ological), 14(1):107–114, 1952.
Robin Hanson. Combinatorial information market design.Information Systems Frontiers, 5(1):
107–119, 2003.
Robin Hanson. Logarithmic market scoring rules for modular combinatorial information aggregation.
Journal of Prediction Markets, 1(1):3–15, 2007.
Friedrich A. Hayek. The use of knowledge in society.The American Economic Review, 35(4):
519–530, 1945.
Youwon Jang, Joochan Kim, and Byoung-Tak Zhang. The losing winner: An llm agent that predicts
the market but loses money. InNeural Information Processing Systems (NeurIPS 2025) Workshop:
Generative AI in Finance, 2025.
Kalshi. Kalshi rulebook and contract specifications. https://kalshi.com/regulatory/
rulebook, 2025. Accessed: 2025-09-23.
John L Kelly. A new interpretation of information rate.the bell system technical journal, 35(4):
917–926, 1956.
Nicolas S Lambert, David M Pennock, and Yoav Shoham. Eliciting properties of probability
distributions. InProceedings of the 9th ACM Conference on Electronic Commerce, pages 129–138,
2008.
Yingkai Li, Jason D Hartline, Liren Shan, and Yifan Wu. Optimization of scoring rules. In
Proceedings of the 23rd ACM Conference on Economics and Computation, pages 988–989, 2022.
Leonard C MacLean, Edward O Thorp, and William T Ziemba.The Kelly capital growth investment
criterion: Theory and practice, volume 3. world scientific, 2011.
John McCarthy. Measures of the value of information.Proceedings of the National Academy of
Sciences, 42(9):654–655, 1956a.
John McCarthy. Measures of the value of information. InProceedings of the National Academy of
Sciences Symposium on Information Theory, pages 654–655, 1956b.
Hunter Ng, Lin Peng, Yubo Tao, and Dexin Zhou. Price discovery and trading in modern prediction
markets.Available at SSRN, 2026.
Polymarket. Polymarket CLOB documentation. https://docs.polymarket.com/concepts/
prices-orderbook, 2023. Accessed: 2026.
David Rothschild. Forecasting elections: Comparing prediction markets, polls, and their biases.
Public Opinion Quarterly, 73(5):895–916, 2009.
Leonard J. Savage. Elicitation of personal probabilities and expectations.Journal of the American
Statistical Association, 66(336):783–801, 1971. ISSN 01621459, 1537274X.
Edward O Thorp. Portfolio choice and the kelly criterion. InStochastic optimization models in
finance, pages 599–619. Elsevier, 1975.
Justin Wolfers and Eric Zitzewitz. Prediction markets.Journal of economic perspectives, 18(2):
107–126, 2004.
Qingchuan Yang, Simon Mahns, Sida Li, Anri Gu, Jibang Wu, and Haifeng Xu. Llm-as-a-prophet:
Understanding predictive intelligence with prophet arena. 2025. URL https://arxiv.org/
abs/2510.17638.
16

A Implementations of prediction markets
A prediction market needs an underlying matching mechanism that determines how buy and sell
orders interact and at what prices; the choice shapes the liquidity, transaction costs, and incentives
forecasters face. Two design families dominate practice—automated market makers and central limit
order books—and both are recovered as special cases of the price-impact-function abstraction in
Section 2 via specific choices ofρandL ρ.
Automated market makers.A classic implementation of a prediction market is anautomated market
maker(AMM) governed by a cost function [Hanson, 2003, 2007, Chen and Pennock, 2007, Abernethy
et al., 2013]. The AMM maintains a vector x∈R K recording the net number of shares of each
outcome it has sold so far, and commits to a strictly convex, differentiablecost function C:R K →R .
A forecaster who executes the position vectors∈R K pays the total cost C(x+s)−C(x) of moving
the share state to x+s , and receives the payout s·1 y for a realized outcome y, with expected profit
πAMM(s,p ∗) :=s·p ∗ −(C(x+s)−C(x)). The cost function C is chosen so that it always satisfies
∇C(x)∈∆ [K] for all x. The marginal cost q=∇C(x) is thespot price. In the price-impact
notation of Section 2, an AMM corresponds toρ(s) =∇C(x+s)andL ρ(s;q) =D C(x+s,x).
The key structural property of this construction is that the convex conjugate of C on the simplex,
G(p) = supx∈RK {p·x−C(x)} , is the convex potential that induces a strictly proper scoring rule
S(p, y) =G(p) +∇G(p)·(1 y −p).
Central limit order books.The largest prediction markets today (e.g. Kalshi, Polymarket) instead
adopt acentral limit order book(CLOB), the matching mechanism standard in equity and futures
exchanges: opposing limit orders are matched directly between participants, and liquidity is supplied
dynamically by the resting orders rather than by a designated maker. CLOBs are favored over
AMMs in practice because the cost-function approach is hard to scale and operate: liquidity must be
subsidized up front through a fixed parameter, making thousands of simultaneous markets infeasible;
the cost function cannot be updated post-deployment, whereas CLOB makers adjust quotes to news
and adverse selection in real time; and derivatives regulations—such as the CFTC’s, under which
Kalshi operates as a designated contract market—are written around order-book mechanics rather
than algorithmic counterparties. Polymarket itself migrated from an AMM to a CLOB after launch
[Polymarket, 2023, Ng et al., 2026], citing tighter spreads, native limit-order support, and scalability
without per-market subsidy. In a CLOB, ρ is the piecewise-constant function read directly off the
order book, andL ρ captures the depth-induced slippage as the trader walks the book.
B Omitted proofs
B.1 Proof of Theorem 2
For any strictly proper scoring rule S, we show that if a betting strategy s(p,q) is intrinsically
different from sG(p,q) , then we can find some p̸=q and p∗ such that S(p;p ∗)≥S(q;p ∗) but
s(p,q)has non-positive expected profit underp ∗.
Given any two intrinsically different betting strategies s(p,q) and sG(p,q) , we first apply constant
shifting and rescaling to both strategies to normalize them so that s(p,q)·1=s G(p,q)·1= 0
(via constant shifting) and ||s(p,q)||=||s G(p,q)||= 1 (via rescaling). No transformations are
needed if s(p,q) =0 . Since s(p,q) and sG(p,q) are intrinsically different, after normalizations
there still exists an interior market price q∈int(∆ [K] ), a sequence of forecasts converging to q, i.e.,
{pt}∞ t=1 →q , yet a small constant ϵ such that ||s(pt,q)−s G(pt,q)|| ≥ϵfor every t= 1,2,· · ·.
The sequences {s(pt,q)} ∞ t=1 and {sG(pt,q)} ∞ t=1 are all bounded, so there exists subsequences that
converge. Slightly overloading the notation, let
{s(pt,q)} ∞ t=1 →ˆ sand{s G(pt,q)} ∞ t=1 →s ∗.
17

We have ||ˆ s−s∗|| ≥ϵ. Next we shall construct a p∗ t for every t such that S(pt,p ∗ t )≥S(q,p ∗ t ) but
the expected profit of s(pt,q) is negative for large enough t, hence disproving the robust profitability
ofs(p t,q).
We start by handling the corner case withK= 2. In this case, after normalization via rescaling and
constant shifting, the betting strategy is either (1/
√
2,−1/
√
2)⊤ or (−1/ √ 2,1/ √ 2)⊤ or 0, which
essentially buys
√
2 ofYES, or buys
√
2 ofNO, or buys nothing. Since ||s(pt,q)−s G(pt,q)|| ≥ϵ,
they must correspond to these two of these three different strategies respectively. Since pt ̸=q ,
sG(pt,q) cannot be 0. If sG(pt,q) buysYES, then p∗ t = (1,0) ⊤ induces higher score for pt than
that of the market q but induces non-positive profit for the other betting strategy s(pt,q) , as desired.
The case whens G(pt,q)buysNOis symmetric.
In the remainder of the proof, we consider the non-trivial case K >2. We claim that there exists a
constant v such that (1) v+q∈∆ k or equivalently v·1= 0 , and (2) v·s ∗ > c >0>−c >v·ˆ s
for some small positive constant c. To see this, let 1⊥ ={v∈R K :v·1= 0} denote the subspace
that is perpendicular to the all one vector1. Sinceq∈int(∆ [K] ),∆ [K] contains a full-dimensional
unit ball within the subspace 1⊥ that is centered around q. Due to normalization of betting strategy
s,s G, we know ¯ s,¯ sG ∈1 ⊥ and so is their difference. Since ||ˆ s−s∗|| ≥ϵ, there must exist some
v∈1 ⊥ such thatv·s ∗ > c >0>−c >v·ˆ s, as desired.
We construct p∗ t =q+v∈∆ K (the same for every t), with the v as chosen above. The expected
profit of betting strategys(p t,q)under thisp ∗ t satisfies
(p∗ t −q)·s(p t,q) =v·s(p t,q)
=v·[s(p t,q)−ˆ s] +v·ˆ s
<0for anytlarge enough,
because the first term goes to 0 due to s(pt,q)→ˆ s, whereas the second term v·ˆ s(<−c) is a
negative constant.
However, we show thatpt’s expected score under ground truth probabilityp∗ t is positive. Let G be the
associated potential function of strictly proper scoring ruleS, i.e., S(p, y) =G(p)+∇G(p)·(1y−p).
Then we have
S(pt,p ∗ t )−S(q,p ∗ t )
=G(p t) +∇G(p t)·(p ∗ t −p t)−G(q)− ∇G(q)·(p ∗ t −q)
=G(p t)−G(q)− ∇G(q)·(p ∗ t −q) +∇G(p t)·(p ∗ t −p t)
=G(p t)−G(q)− ∇G(q)·(p t −q)− ∇G(q)·(p ∗ t −p t) +∇G(p t)·(p ∗ t −p t)
=D G(pt,q) + [∇G(pt)− ∇G(q)]·(p∗ t −p t)
=D G(pt,q) +s G(pt,q)·(q+v−p t)
=D G(pt,q) +s G(pt,q)·(q−p t) + (sG(pt,q)−s ∗)·v+s ∗ ·v
>0for anytlarge enough,
because the Bregman divergence DG(pt,q)≥0 for the convex G, the last term s∗ ·v is larger than
the positive constant c due to our choice of v, whereas the two middle terms both go to 0 since
pt →q,s G(pt,q)→s ∗ whereass G(pt,q),vare all bounded vectors.
This concludes the proof of the second part. That is, we have found pt,p ∗ t ,q for large enough t such
that S(pt,p ∗ t )−S(q,p ∗ t )>0 but the expected profit of the betting strategy s(pt,q) under this p∗ t ,
i.e.,(p ∗ t −q)·s(p t,q), is strictly negative.
B.2 Proof of Proposition 2
The “only if” direction is precisely Theorem 1 since proper betting guarantees robust profitability.
We thus only need to prove the “if” direction below. The challenge here is to show that ifG is not
strictly convex, any betting strategy – not just proper betting – cannot be robustly profitable. That is,
18

for any not strictly convex G and any betting strategy s(p,q) , there exists p∗ and p̸=q that satisfy
S(p;p ∗)≥S(q;p ∗) 7 but yield non-positive profit unders.
SinceGis not strictly convex, there must exist somepandqsuch thatq∈int(∆ [K] )and
DG(q,p) =G(q)−G(p)− ∇G(p)·(q−p) =−κ <0.(4)
Given the p,q pair satisfying the above condition, we now construct a corresponding p∗. Let s be
any betting strategy,ˆ s= s(p,q) ||s(p,q)|| denote the direction of the betting strategy at the above p,q , and
L=||s G(p,q)||denote 2-norm of the proper betting strategy. We constructp ∗ =q− κ 2Lˆ s.
Next we show that the constructed p,q,p ∗ have negative profit but satisfy S(p;p ∗)≥S(q;p ∗).
Notably, this is an interesting situation where the market price q may be much closer to the ground
truth p∗ than the forecast p, but has worse score than p. This is intrinsically due to the non-convexity
ofG.
The difference of the expected score is analyzed as follows:
S(p,p ∗)−S(q,p ∗) =G(p) +∇G(p)·(p ∗ −p)−G(q)− ∇G(q)·(p ∗ −q)
=G(p)−G(q) +∇G(p)·(q−p)−[∇G(q)− ∇G(p)]·(p ∗ −q)
=−D G(q,p) +s G(p,q)·(p ∗ −q)
≥κ−L·κ/(2L)>0
The profit ofs(p,q)is analyzed as follows:
(p∗ −q)·s(p,q) =− κ 2Lˆ s·s(p,q) =− κ 2L ||s(p,q)||<0
B.3 Proof of Corollary 1
We only need to show DG(q,p) =L ρ(s∗;q) in any AMM governed by a strictly convex cost
function C(x), whose convex conjugate is G(p). The rest of the statement then follows from
Theorem 1.
Lets ∗ =∇G(p)− ∇G(q)denote the proper betting. We compute
Lρ(s∗;q) =C(s ∗ +x)−C(x)− ∇C(x)·s ∗
=D C(s∗ +x,x)
=D G((∇C) −1(s∗ +x),(∇C) −1(x))
=D G(p,q)
where the third equation is due to the fact that if C, Gare convex conjugates, then DC(x′,x) =
DG((∇C) −1(x′),(∇C) −1(x)).
C Extensions of Theorem 1
C.1 Proper betting under nonzero bid-ask spread
In real prediction markets, low liquidity and platform fees create a positive gap between the prices
at which a contract can be bought and sold. We extend Theorem 1 to this setting via the following
bid-ask convention. For each outcome k∈[K] , let q+ k denote the ask price at which aYEScontract
on outcome k (paying 1 if y=k , otherwise 0) can be bought, and q− k the ask price at which the
correspondingNOcontract (paying 1 if y̸=k , otherwise 0) can be bought. Absence of riskless
arbitrage on outcome k requires q+ k +q − k ≥1 , with equality recovering the spread-free setting of
Section 2; in practice the inequality is strict.
7Scoring ruleSis defined asS(p, y) =G(p) +∇G(p)·(1 y −p).
19

Bid-ask-aware proper bet.Treat each outcome k as an independent binary event yk :=1[y=k]∈
{0,1}and extend the scoring rule to vectorsp∈[0,1] K coordinate-wise:
S(p, y) :=
KX
k=1
S(pk, yk),
where S(pk, yk) is the score for binary outcome ofYES/NO k, in reduced form with 1-D parameter
pk. Let G: [0,1]→R be its associated convex potential function. The Bregman divergence and
proper-bet construction extend coordinate-wise as well. Given a model prediction p∈[0,1] K and
prices(q +,q −), define the bid-ask-aware proper bets∈R K by
sk :=



∇G(pk)− ∇G(q+ k )ifp k > q+ k (buy YES onkatq + k ),
∇G(pk)− ∇G(1−q− k )ifp k <1−q − k (buy NO onkatq − k ),
0if1−q − k ≤p k ≤q + k .
To see this is a valid betting strategy under non-zero bid/ask spread, we observe that G(pk)−
∇G(q+ k )≥0 when pk > q+ k due to convexity of G and G(pk)− ∇G(1−q − k )>0 for similar
reasons. Hence, sk never needs to buy the other side (which may have inconsistent price due to
non-zero bid/ask spread). The middle case is the spread-induced no-bet zone: the model’s edge is too
small to overcome the spread on outcome k (the interval is non-empty since q+ k +q − k ≥1 ). Setting
˜qk :=q + k , 1−q − k , or pk in the three cases respectively, we always have sk =∇G(p k)− ∇G(˜qk),
and the realized profit is
s·(1 y − ˜q) =
KX
k=1
sk(yk −˜qk).
Corollary 3(Profitability under bid-ask spread (omitting liquidity loss)).Let s, ˜q be as defined above
and S( ˜q, y) =PK k=1 S(˜qk, yk) be the bid-ask-aware market score. Then the bid-ask-aware proper
bet has expected profit admits the following decomposition
Ey∼p∗ [s·(1 y − ˜q)] =E y∼p∗ [S(p, y)−S( ˜q, y)]| {z }
score gap
+
KX
k=1
DG(˜qk, pk)
| {z }
Bregman bonus
(5)
Proof. For each coordinate k, sk =∇G(p k)− ∇G(˜qk) is the binary proper bet with respect to the
reference˜qk. Apply the binary version of Lemma 1:
sk(yk −˜qk) = (∇G(p k)− ∇G(˜qk)) (yk −˜qk) = [S(p k, yk)−S(˜qk, yk)] +D G(˜qk, pk).
Summing over k∈[K] and taking expectation under y∼p ∗, minus the liquidity loss, yields
Eq. (5).
Remark 6(Correlated outcomes.).Corollary 3 holds even for outcomes {1,· · ·, K}that need not
to be disjoint but can be arbitrarily correlated. In this case, we simply treat each outcome k as a
separate (though possibly correlated) binary event.
Cost of spread.The reference ˜q depends on which side of the spread each coordinate lands on,
so an accuracy edge against ˜q is harder to attain than one against any spread-free price ¯q with
¯qk ∈[1−q − k , q+ k ]. Specifically, the score gap against ˜qdecomposes as
S(p, y)−S( ˜q, y) = [S(p, y)−S( ¯q, y)] + [S( ¯q, y)−S( ˜q, y)]| {z }
cost of spread≤0
,
where the spread cost vanishes when q+ k +q − k = 1 (zero spread). The bid-ask-aware result thus
interpolates between the spread-free guarantee of Theorem 1 and a strictly weaker condition that
absorbs the per-trade spread cost.
20

C.2 Proper betting for long time horizon
For events that take days or weeks to resolve, both forecaster and market predictions evolve over time.
A forecaster can make different prediction pt at different time t= 1,· · ·, Tand makes trades based
on pt as well as then market price qt. We extend Theorem 1 to two natural multi-period strategies,
each compounding the per-round proper bet but differing in what they hold and what accuracy edge
they require. In both corollaries below, we omit liquidity loss for simplicity.
Corollary 4(Fundamental-driven strategy).Thefundamentalstrategy executes the proper bet
st :=∇G(p t)− ∇G(qt) at each time t and holds all positions to resolution. Then the cumulative
expected profit at resolution decomposes as
TX
t=1
st ·(p ∗ −q t) =
TX
t=1

S(pt;p ∗)−S(q t;p ∗)  + TX
t=1
DG(qt,p t)(6)
Corollary 5(Momentum-driven strategy).Themomentumstrategy maintains the proper position
xt :=∇G(p t)− ∇G(qt) at each time t, rebalancing after every market update; the marginal trade
at time t is st :=x t −x t−1 with x0 :=0 . Then the cumulative mark-to-market return decomposes as
TX
t=1
xt ·(q t+1 −q t) =
TX
t=1

S(pt;q t+1)−S(q t;q t+1)  + TX
t=1
DG(qt,p t)(7)
Moreover, the accumulated profit of executing trades st at prices qt and settling at qT+1 can be
equivalently expressed in the following trade form
TX
t=1
xt ·(q t+1 −q t) =
TX
t=1
st ·(q T+1 −q t),
The two corollaries differ in what plays the role of the “ground truth” in the proper-bet decomposition:
Corollary 4 uses the unobservable p∗ that resolves the event, so the trader needs an accuracy edge
against the truth and is exposed across the entire horizon; Corollary 5 uses the next-period market
price qt+1, so the trader only needs to predict the market’s next move and is exposed only one period
at a time.
Proof.For Corollary 4, apply Lemma 1 at each round with realized outcomey:
st ·(1 y −q t) =  S(pt, y)−S(qt, y)  +D G(qt,p t).
Summing over t and taking expectation under y∼p ∗ gives Eq. (6). The score-gap sum is strictly
positive by hypothesis and the Bregman sum is non-negative, so the total is positive.
For Corollary 5, apply Lemma 1 (in expectation form) at each round with substitutions p∗ →q t+1,
p→p t,q→q t:
xt ·(q t+1 −q t) =  S(pt;q t+1)−S(q t;q t+1)  +D G(qt,p t).
Summing gives Eq. (7). The trade-form equivalence follows from substituting xt = Pt r=1 sr and
exchanging the order of summation:
TX
t=1
xt ·(q t+1 −q t) =
TX
r=1
sr ·
TX
t=r
(qt+1 −q t) =
TX
r=1
sr ·(q T+1 −q r),
where the inner sum telescopes by
TX
t=r
(qt+1 −q t) =q T+1 −q r.
Strict positivity follows similarly to the fundamental-driven strategy.
21

Table 5:Calibration and profitability metrics by model and persona group. N is the number of
market-level predictions per model. ECE is expected calibration error. Quad. Score represents the
model’s score under the quadratic scoring rule. ± values are the bootstrapped standard errors over
1,000resamples. Shaded rows report persona-group averages.
ModelNmarkets ECE Quad. Score ROI
GPT-5.2 (High) 11,789 0.021±0.0050.916±0.006−7.8%±3.6(Log)
GPT-5.2 (Base) 11,789 0.013±0.0030.916±0.005−4.4%±3.9(Log)
Grok 4.1 Fast 11,407 0.027±0.0040.913±0.005−9.1%±4.5(Log)
Claude Sonnet 4.5 11,785 0.023±0.0030.911±0.005−8.1%±3.5(Log)
Kimi K2 Thinking 11,811 0.024±0.0040.912±0.005−8.7%±3.8(Log)
DeepSeek V3.2 11,071 0.031±0.0050.899±0.006−12.8%±3.4(Log)
Minimax M2 11,688 0.028±0.0050.900±0.006−9.4%±3.8(Log)
Brittle (avg) 11,620 0.024 0.910 −8.6%(Log)
LLaMA 4 Maverick 29,613 0.069±0.0040.871±0.005−4.9%±2.2(Log)
Qwen 3 235B 29,923 0.078±0.0040.868±0.004−11.2%±1.9(Log)
DeepSeek R1 29,759 0.100±0.0050.848±0.005−5.4%±1.7(Log)
Dispersed (avg) 29,765 0.082 0.862 −7.2%(Log)
Gemini 3 9,721 0.017±0.0030.936±0.004+14.2%±8.8(Brier)
Claude Opus 4.6 3,172 0.011±0.0040.949±0.007+17.5%±7.2(Brier)
Conservative (avg) 6,446 0.014 0.942 +15.8%(Brier)
D Additional experiments
D.1 Model details
Table 5 reports the LLMs evaluated across three metrics – expected calibration error (ECE), the score
under the quadratic scoring rule, and ROI under each model’s best proper betting strategy. GPT-5.2
(Base/High) correspond to different reasoning levels of the same underlying model. The number
of markets varies across forecasters because models were released at different times, resulting in
differing amounts of collected data through the Prophet Arena pipeline; to ensure comparability, we
standardize evaluations in Section 4.
Interestingly, while the Brittle group has lower ECE and the higher aggregate Brier accuracy as
compared to the Dispersed group, it is also more unprofitable. As such, aggregate accuracy and
calibration can therefore coexist with systematic capital loss, due to the importance of the Bregman
divergence term.
D.2 Implementation details of betting strategies
Setup.We consider a collection of n markets with forecast–price pairs {pi, qi}i∈[n]. A betting
strategy is defined by a set of budget allocation weights {wi}i∈[n], which encode both direction and
size: if wi >0 , we buy YES on market i with allocation wi; if wi <0 , we buy NO (equivalently, sell
YES) with allocation −wi. Without loss of generality, we restrict wi ∈[−1,1] for all i∈[n] and
normalize total exposure such that P i∈[n] |wi|= 1.
Proper Betting Strategies.Proper betting strategies can be constructed as follows:
1.Brier:Allocates linearly in the margin:w i ∝p i −q i.
2.Logarithmic:Scales allocations according to:w i ∝logp i −logq i.
3. Spherical:Allocates based on the difference between the L2-normalized forecast and market
price vectors:w i ∝ pi ∥p∥ − qi ∥q∥ .
22

Baseline Betting Strategies.We also construct a few betting strategies from well-motivated heuristics
as baselines:
1.Max-Margin:Strategies that bet the margin.
• Market-Level: wi ∝sign(p i −q i),∀i∈[n] . This strategy places a unit bet on every market,
with direction determined by whetherp i > qi.
• Grouped:Let {Ik}m k=1 denote a partition of markets into groups corresponding to the same
underlying question. For each groupk, define
i⋆(k) = arg max
i∈Ik
|pi −q i|.
This strategy allocates the budget uniformly across groups, placing a single bet per group on the
market with the largest margin:
wi⋆(k) = sign(pi⋆(k) −q i⋆(k)) m , w i = 0,∀i /∈ {i⋆(k)}m k=1.
2. Inverse-Margin: wi ∝ sign(pi−qi) |pi−qi| ,∀i∈[n] . This heuristic places more weight on markets with smaller margins, under the hypothesis that forecasts are more reliable when deviations from the
market are modest.
3. Kelly-Alike: wi ∝ pi−qi 1−qi ,∀i∈[n] . This heuristic strategy mimics the ratio in the Kelly criterion.
4. Kelly Criterion [Kelly, 1956]:Unlike the previous strategies, which allocate a fixed budget B
across markets via weightswi with the goal of maximizing expected profit, Kelly sizing determines
the fraction of wealth to wager on each individual market sequentially to maximize the expected
log-growth rate. For a binary market with forecast pi and market price qi, a unit stake on YES
pays1/q i, giving net oddsb i = (1−q i)/qi. Maximizing
E[logW i+1] =p i log(1 +f ibi) + (1−p i) log(1−f i)
over the wealth fraction fi yields the closed form fi = |pi−qi| 1−qi . If fi exceeds 1, we allow for the use of leverage to purchase additional shares.
Table 6 reports the full comparison of evaluated models across all baseline betting strategies and
the proposed Proper (Brier) strategy. The Kelly criterion exhibits particularly high variance in ROI
because it compounds the bankroll while effectively treating the forecaster’s estimated disagreement
with the market as the true edge. When this edge is poorly estimated, Kelly can substantially oversize
individual positions. A single sufficiently large loss can therefore deplete the bankroll, causing
compounded returns to collapse to−100%for many models.
D.3 Empirical decomposition
Table 7 reports the full decomposition across all models and all evaluated proper betting strategies.
Divergence varies substantially across both models and rules, and often offsets large negative score
gaps, meaning models less accurate can still yield positive ROI. Rules such as Log tend to amplify
divergence, leading to higher upside but also greater dispersion in outcomes, while Brier and
Spherical are comparatively more stable. This reinforces that the mapping from forecasts to returns is
highly rule-dependent, and that profitability hinges as much on how aggressively a strategy exploits
disagreement as on the underlying predictive accuracy.
D.4 Synthetic persona generation
For each persona, we generate a synthetic forecast by perturbing the market price by a persona-specific
margin:
pi =q i ±m i (clipped to[ε,1−ε]),
where mi ≥0 is the margin magnitude drawn from a persona-specific distribution, and the sign is
chosen toward the realized outcome with probability ai. A single global offset on ai is calibrated per
persona so that all personas attain the same Brier score within each regime.
23

Table 6:Pairwise comparison of the Proper Betting (Brier) strategy against each of the five baselines
on the expanded dataset, with each column reporting the difference between Proper Betting and the
corresponding baseline. Confidence intervals are paired, event-clustered 95% bootstrap intervals;
bold indicates differences where the CI excludes zero.
Model∆S−Max (Mkt)−Max (Grp)−Inv-Margin−Kelly-Alike−Kelly
Gemini 3.1 Pro (B)+0.0076[+0.0014, +0.0136]+30.3[+20.7, +39.9]+30.1[+15.5, +42.9]+39.2[+27.7, +50.6]+24.3[+16.1, +32.8]+138.9[+127.3, +150.4]
Claude Fable 5+0.0039[+0.0008, +0.0073]+26.8[+15.3, +40.0]+48.3[+34.2, +63.1]+33.6[+20.0, +48.9]+16.8[+7.3, +27.4] +129.0 [−1.3×10 9, +141.8]
Gemini 3.1 Pro (A)+0.0039[+0.0016, +0.0063]+25.9[+20.4, +31.5]+36.6[+28.3, +44.5]+29.9[+23.5, +36.5]+16.3[+11.7, +21.0]+127.9[+121.5, +134.6]
GPT-5.6 Sol+0.0033[+0.0003, +0.0067]+22.4[+12.2, +35.4]+39.9[+24.3, +55.7]+28.5[+15.7, +43.7]+15.7[+6.0, +27.1] -1220.4 [−2.2×10 8, +122.5]
Claude Sonnet 5+0.0028[+0.0002, +0.0057]+20.1[+10.3, +32.1]+58.8[+45.0, +73.2]+25.7[+13.4, +40.1]+8.3[+1.3, +16.9] +125.9 [-5766.9, +133.1]
GPT-5.5 (B) -0.0059 [-0.0129, +0.0009]+13.0[-1.2, +29.3]+20.3[-0.7, +41.1]+18.6[+0.1, +38.9] +8.6 [-2.7, +21.4]+116.8[+99.8, +136.0]
GPT-5.5 (C) -0.0056 [-0.0101, -0.0012] +8.8 [-1.5, +18.7] +3.6 [-28.4, +27.3] +7.0 [-5.5, +19.4] +2.0 [-6.3, +10.0]+107.3[+94.9, +119.2]
Gemini 3.5 Flash -0.0188 [-0.0299, -0.0081] -2.4 [-11.9, +6.8] +1.8 [-19.5, +19.3] +1.3 [-10.8, +13.0] +0.1 [-7.5, +7.6]+105.9[+94.2, +117.7]
Qwen 3.5+ (B) -0.0342 [-0.0415, -0.0272]+8.3[+0.6, +16.0] +9.6 [-7.7, +24.2] +7.7 [-1.9, +17.4] -0.1 [-5.2, +5.2]+105.6[+96.4, +114.6]
Kimi K3 -0.0030 [-0.0065, +0.0004] +1.9 [-10.7, +15.5]+40.3[+24.2, +56.4] +4.5 [-12.6, +22.3] -1.9 [-10.9, +7.9]+104.8[+88.8, +121.6]
GPT-5.4 -0.0203 [-0.0258, -0.0159] +2.3 [-2.9, +7.6]+12.5[+1.9, +22.5] +5.1 [-2.5, +13.1] -2.5 [-5.6, +0.7]+99.8[+92.5, +107.4]
GPT-5.5 (D) -0.0065 [-0.0081, -0.0050] -0.3 [-3.8, +3.1]+15.7[+9.4, +21.7] +1.3 [-3.5, +6.3] -3.1 [-6.2, -0.0]+99.8[+95.2, +104.2]
Muse Spark 1.1 -0.0133 [-0.0203, -0.0066] -4.2 [-18.0, +11.4] +16.5 [-3.2, +35.5] -1.9 [-19.2, +16.1] -2.3 [-11.1, +7.9]+98.9[+82.6, +116.8]
GLM 5.2 -0.0194 [-0.0248, -0.0139] -2.3 [-10.0, +5.6]+22.7[+9.2, +34.9] -4.3 [-14.6, +6.3] -3.0 [-7.1, +1.4]+98.6[+88.8, +108.4]
Claude Sonnet 4.6 (A) -0.0292 [-0.0353, -0.0233] -1.2 [-7.9, +5.5] +7.6 [-5.8, +19.7] -1.1 [-10.9, +8.6] -2.8 [-6.5, +1.2]+94.9[+86.9, +103.0]
Grok 4.5 -0.0115 [-0.0164, -0.0067] -4.6 [-15.5, +8.3]+24.0[+7.8, +40.0] -4.4 [-18.6, +11.6] -5.1 [-11.9, +2.8]+94.5[+80.9, +110.0]
Claude Sonnet 4.6 (B) -0.0236 [-0.0346, -0.0128] -0.9 [-13.8, +13.2] -16.0 [-63.5, +19.5] -10.5 [-37.6, +12.6] -2.4 [-9.2, +6.1]+94.2[+78.5, +110.9]
Gemma 4 31B -0.0339 [-0.0410, -0.0268] -3.3 [-9.3, +2.8] +10.1 [-0.6, +19.9] -5.8 [-13.7, +2.4]-4.5[-8.5, -0.4]+93.2[+85.4, +100.8]
Table 7: ROI decomposition on the expanded dataset, where ROI = ∆S+D for each model and
proper scoring rule. Bold denotes significantly positive score gaps (95% CI above zero), and bold
italic denotes significantly positive ROI.
Model Brier∆SBrierDBrier ROI Log∆SLogDLog ROI Sph∆SSphDSph ROI
Gemini 3.1 Pro (B)+11.7[+2.4, +21.1]+27.2[+22.7, +32.1]+38.9[+27.4, +50.9]+7.5[+0.8, +14.0]+20.9[+18.2, +23.8]+28.4[+20.4, +36.2]+11.3[+3.5, +19.5]+21.9[+18.3, +25.8]+33.2[+23.9, +42.9]
Claude Fable 5+12.3[+3.2, +22.0]+16.7[+11.8, +22.2]+29.0[+16.7, +42.7]+8.6[+1.3, +15.6]+12.9[+9.8, +16.5]+21.5[+12.2, +30.6]+10.2[+1.4, +18.6]+11.9[+8.5, +15.9]+22.1[+11.6, +33.0]
Gemini 3.1 Pro (A)+8.7[+3.3, +13.7]+19.2[+17.0, +21.7]+27.9[+21.1, +34.3]+4.8[+0.8, +8.5]+16.4[+14.7, +18.2]+21.2[+16.4, +25.8]+6.5[+2.1, +10.8]+13.6[+12.1, +15.4]+20.1[+14.9, +25.7]
GPT-5.6 Sol+10.9[+1.0, +21.7]+15.9[+12.1, +21.9]+26.7[+14.4, +41.4]+10.7[+3.0, +18.5]+12.6[+10.1, +16.1]+23.3[+14.5, +32.4]+12.1[+3.2, +21.4]+11.4[+8.5, +15.7]+23.5[+13.0, +35.8]
Claude Sonnet 5+10.2[+0.2, +19.9]+15.8[+11.8, +20.9]+25.9[+13.4, +38.9]+9.1[+1.9, +16.4]+12.4[+9.9, +15.6]+21.5[+13.0, +30.7]+12.3[+2.9, +21.7]+12.4[+9.5, +16.4]+24.7[+13.9, +36.4]
GPT-5.5 (B) -15.4[-29.6, -0.4]+32.2[+25.8, +39.5]+16.8[+2.3, +33.3]-9.5[-20.7, +0.5]+21.2[+17.9, +24.9]+11.7[+0.3, +22.2]-11.5[-23.0, -0.7]+24.4[+19.4, +30.1]+12.9[+0.9, +25.0]
GPT-5.5 (C) -15.6[-26.3, -5.6]+22.9[+18.6, +27.3]+7.3[-3.3, +17.3]-13.1[-21.4, -5.5]+18.4[+15.2, +21.6]+5.2[-3.8, +13.9]-14.6[-23.4, -6.2]+16.5[+13.4, +20.1]+1.9[-6.6, +10.7]
Gemini 3.5 Flash -26.3[-39.9, -14.1]+32.2[+26.1, +39.2]+5.9[-4.4, +15.8]-17.4[-26.8, -8.2]+25.5[+21.8, +29.8]+8.1[-0.5, +16.4]-22.5[-35.4, -10.3]+27.4[+21.8, +33.5]+4.9[-5.0, +14.8]
Qwen 3.5+ (B) -58.4[-68.9, -48.4]+64.0[+57.7, +70.8]+5.6[-2.1, +13.3]-33.1[-39.6, -27.0]+38.9[+35.6, +41.8]+5.8[-0.6, +11.7]-48.6[-57.5, -40.5]+48.9[+43.5, +54.4]+0.3[-6.4, +6.5]
Kimi K3 -15.0[-29.1, -0.7]+19.9[+15.2, +25.1]+4.8[-8.2, +18.4]-7.4[-18.9, +3.7]+13.7[+11.7, +16.0]+6.4[-4.6, +17.4]-10.4[-22.4, +1.5]+14.2[+10.4, +18.7]+3.8[-7.3, +15.3]
GPT-5.4 -65.0[-82.5, -51.3]+64.8[+55.1, +79.3]-0.2[-7.8, +7.3]-32.0[-39.2, -24.8]+33.2[+30.9, +35.7]+1.2[-5.4, +8.0]-50.8[-63.9, -39.1]+50.4[+42.3, +60.6]-0.4[-7.0, +6.8]
GPT-5.5 (D) -23.8[-28.9, -18.4]+23.6[+21.4, +26.1]-0.2[-4.6, +4.4]-15.1[-19.4, -10.7]+16.6[+15.6, +17.7]+1.5[-2.5, +5.7]-18.1[-22.9, -13.4]+17.4[+15.6, +19.5]-0.7[-4.8, +3.3]
Muse Spark 1.1 -35.3[-50.4, -19.5]+34.2[+27.7, +41.1]-1.1[-15.2, +13.9]-23.5[-35.1, -11.4]+24.4[+20.7, +28.1]+0.9[-10.2, +12.3]-31.1[-44.6, -17.4]+28.5[+23.2, +34.6]-2.6[-14.7, +10.2]
GLM 5.2 -50.3[-61.5, -39.1]+48.8[+42.4, +56.0]-1.4[-9.2, +6.9]-27.2[-34.5, -19.8]+27.9[+25.3, +30.4]+0.7[-6.1, +7.4]-38.8[-47.7, -29.9]+37.2[+32.1, +42.6]-1.6[-8.7, +5.7]
Claude Sonnet 4.6 (A) -50.4[-58.5, -42.5]+45.3[+41.0, +49.9]-5.1[-11.5, +1.4]-35.9[-41.6, -29.8]+31.6[+29.4, +33.7]-4.3[-9.7, +1.4]-42.1[-49.5, -34.9]+35.8[+32.2, +39.6]-6.3[-12.0, +0.0]
Grok 4.5 -37.5[-50.3, -24.8]+32.0[+25.1, +39.4]-5.5[-17.4, +7.4]-25.0[-33.6, -16.0]+20.4[+17.4, +23.6]-4.6[-13.6, +4.8]-31.1[-42.3, -19.7]+25.5[+20.3, +31.2]-5.6[-15.8, +5.4]
Claude Sonnet 4.6 (B) -38.7[-52.8, -24.4]+32.8[+26.8, +39.6]-5.8[-19.0, +8.5]-34.3[-45.6, -22.7]+28.0[+24.6, +31.3]-6.3[-16.8, +4.2]-35.1[-47.4, -23.1]+25.8[+21.1, +31.2]-9.3[-20.9, +2.3]
Gemma 4 31B -52.4[-60.9, -43.4]+45.6[+40.7, +50.7]-6.8[-13.2, -0.1]-33.6[-40.3, -27.0]+29.8[+27.4, +32.2]-3.8[-9.7, +1.8]-41.6[-49.0, -34.3]+35.8[+31.8, +40.1]-5.9[-11.5, -0.2]
Synthetic persona construction.Conservative uses m∼Beta(mode = 0.12,conc = 60) with
uniform accuracy a(m) =a 0; Aggressive uses m∼Beta(0.20,25) with uniform a(m) =
a0; Dispersed uses m∼Beta(0.10,6) with linearly declining accuracy a(m) = clip(a 0 −
0.20m,0.01,0.99), wherem=|p−q|denotes the margin.
In all cases, a0 is calibrated via Brent’s method on mean Brier so that the quadratic score matches the
market within ±0.05 in Regime A/B. The calibrated values are a0 = 0.999/0.073 for Conservative,
0.877/0.338 for Aggressive, and 0.971/0.473 for Dispersed, where the first number corresponds to
Regime A (model beats market) and the second to Regime B (model loses to market). Empirically,
these yield Pr[m≤0.15] = 0.85,0.58,0.68 and OLS win-rate slopes of +0.00,−0.01,−0.20 ,
respectively.
For Brittle, matching the same ∆S (Brier) cannot be achieved with a single linear win-rate schedule:
slopes steep enough to capture the empirical tail decline reduce mean accuracy below the Regime A
target, while flatter slopes eliminate the pattern. We therefore use a two-piece schedule
a(m) = clip

a0 −s·max(0, m−τ),0.01,0.99

,
with τ= 0.20 , s= 1.0 , and m∼Beta(0.12,20) , calibrated to a0 = 0.999/0.223 for Regimes A/B.
In Figure 1b, we visualize this fitting a linear regression (OLS) for comparability with the other
personas.
24

D.5 Proper betting rule capital allocation surfaces
The three proper scoring rules evaluated – Brier, logarithmic, and spherical – differ inhow much
capitalthey allocate to each bet (i.e., the number of shares purchased). Figure 4 visualizes these
weight functions across the full(q, m)plane, where m is the signed margin.
Under the Brier rule, the weight is simply w=|p−q| , so capital scales linearly with divergence
and is independent of q, producing vertical contour lines. As a result, Brier is the most aggressive
strategy at large divergences, concentrating capital where model overconfidence is most pronounced.
In contrast, the logarithmic rule, w=|logp−logq| , grows sublinearly in divergence and depends
on the price level. The inward curvature of its contours at large margins reflects this diminishing
sensitivity, so weight increases more slowly as divergence grows. These features make the log rule
more conservative. The spherical rule lies between these extremes: its weight is nonlinear in both
divergence and price, allocating more than log at moderate divergences—amplifying smaller, more
reliable signals—but less than Brier at extreme divergences. It also exhibits mild price dependence,
with slightly higher weights nearq= 0.5, where normalization effects are weakest.
Generally, Brier favors personas whose accuracy holds across margin sizes (e.g., Conservative), but
in the regime in which all personas can outperform the market in terms of accuracy, the performance
gap is sufficiently large that even less stable personas benefit from linear scaling. For smaller (though
still positive) Brier gaps, sharp deterioration in win rate at higher margins can cause linear scaling to
over-weight large-margin forecasts, leading to outsized losses. In such cases, Log may be preferable
due to its stronger penalization of extreme probabilities.
0.9
 0.6
 0.3
 0.0 0.3 0.6 0.9
Margin
0.1
0.2
0.3
0.4
0.5
0.6
0.7
0.8
0.9Market price
Brier
0.05
0.05
0.10
0.10
0.15
0.15
0.20
0.20
0.30
0.30
0.40
0.40
0.9
 0.6
 0.3
 0.0 0.3 0.6 0.9
Margin
Log
0.05
0.05
0.10
0.10
0.15
0.15
0.20
0.20
0.30
0.30
0.9
 0.6
 0.3
 0.0 0.3 0.6 0.9
Margin
Spherical
0.05
0.050.10
0.10
0.15
0.15
0.20
0.20
0.30
0.30
0.40
0.40
0.0
0.2
0.4
0.6
0.8
Bet weight (shares)
Figure 4:Capital allocation (bet weight in shares) as a function of signed margin and market price
(q, y-axis) for the three proper betting strategies. Warmer colors indicate larger bets. Grey regions
are infeasible (p /∈(0,1)). Contour lines mark constant weight levels.
D.6 Mapping empirical forecasters to personas
As shown in Table 8, along the margin dimension, models separate into three clear groups: seven
place 75%–85% of bets below 0.15 (Brittle), three distribute more mass across margins (Dispersed,
<70% below 0.15), and two concentrate over 85% at small margins (Conservative). Second,
Figure 2b confirms the persona assignments along the accuracy consistency dimension. The models
exhibiting the Brittle persona exhibit a steep win-rate slope (β=−6.8 ), with win-rate falling from
over 50% to below 30% by margin 0.50. Dispersed models decline more gradually ( β=−3.6 ),
while Conservative models are essentially flat (β= 0).
D.7 Details about live pilot test
We deploy a portfolio-management version of the forecasting framework in Yang et al. [2025]. The
agent runs on a fixed two-hour cadence; on each cycle it (i) refreshes prices and lifecycle state
for every market it currently tracks, (ii) discovers a batch of new markets, (iii) queries the LLM
forecaster on each eligible market through a standardized prediction context, and (iv) hands the
resulting probabilities to an executor that places limit orders on Kalshi.
25

Table 8:Language model margin concentration. Entries report the share of bets (%) in each margin
bin. ∆S denotes the aggregate score difference relative to the market. Greyed columns correspond to
high-margin bins with sparse data and are excluded from the win-rate analysis. Shares are rounded to
the nearest integer; ∗ indicates a value that is positive but rounds to+0.000.
Model [0,.05) [.05,.15) [.15,.25) [.25,.50) [.50,.70) [.70,.90) [.90,1.0)∆S
GPT-5.2 (High) 61 23 7 5 2 1 1−0.038
GPT-5.2 (Base) 59 23 7 6 2 2 1−0.044
Grok 4.1 Fast 58 22 7 7 3 2 1−0.053
Claude Sonnet 4.5 54 25 8 7 3 2 1−0.055
Kimi K2 Thinking 57 24 6 7 2 2 1−0.053
DeepSeek V3.2 50 25 8 9 4 3 1−0.069
Minimax M2 52 25 8 8 3 3 2−0.064
Brittle (avg) 56 24 7 7 3 2 1 −0.054
LLaMA 4 Maverick 46 21 9 10 5 4 5−0.115
Qwen 3 235B 45 21 9 12 5 4 3−0.106
DeepSeek R1 37 22 10 14 8 6 5−0.140
Dispersed (avg) 43 21 9 12 6 5 4 −0.120
Gemini 3 81 13 2 1 0 0 2+0.002
Claude Opus 4.6 69 20 5 3 1 1 0+0.000 ∗
Conservative (avg) 75 16 4 2 0 0 1 +0.001
A Kalshi market is pulled for analysis on a given cycle if it is open and itsclose time lies between 2
and 14 days (we impose a 14-day maximum horizon to facilitate capital turnover and avoid positions
being tied up in long-dated markets). To limit exposure to trading fees and LLM-driven variance, a
market is skipped on a given cycle if the market price has not moved by at least 10¢ since the last fill;
markets we have never traded on are always re-evaluated.
For each eligible market we issue a single forecast call. The model is given the market’s title,
resolution rules, and contemporaneous market data and is asked to return a JSON object containing a
rationale and the probability that the contract resolves YES. We use the same prompting template and
prediction context as Yang et al. [2025]. The deployed forecaster is Gemini 3 Pro with high-effort
thinking and Google Search grounding enabled.
D.7.1 Prediction context and methodology
Let p denote the model’s probability of YES. We do not trade whenp lies within the bid–ask band
(a consequence of the occasional non-zero bid-ask spread in real-world prediction markets), as this
implies no actionable margin.
Whenever a market is traded, we rebalance the position toward the new target τ on each cycle, as is
detailed in Section C.2.
All orders are placed as limit orders at the prevailing ask, so execution is not guaranteed: on thin
Kalshi books, a portion of the requested size often remains unfilled at the end of the cycle. If they do
not fill, they expire and are cancelled at the next cycle when updated prices and forecasts produce a
new target. The next-cycle delta is then computed based on the positions that actually filled.
Figure 3a presents the full detailed performance and trading statistics for the strategy over the
evaluation period. We also provide access to the trading historyhere, which logs performance of the
trading agent over the trading period.
26

D.7.2 Eligibility criteria
Eligibility is determined ex-ante; we exclude three categories of markets and halt trading three hours
prior to event resolution, the latter reflecting the reduced informational advantage of LLMs close
to resolution time [Yang et al., 2025]. First, we exclude the MENTIONScategory, where contracts
resolve based on unstructured public statements (e.g., “will X mention Y”), as we find that LLMs
perform substantially worse on these questions in tests over publicly available data released by Yang
et al. [2025]. Second, we exclude events for which a Kalshi market’s listedclose_time is more than
one hour after the true resolution time of the event8, creating a mismatch between the LLM’s belief
about market closure and the actual outcome realization.
In addition to eligibility criteria, we also drop a market from consideration due to an underspecified
resolution rule. We have contacted Kalshi about contracts of this kind, and we view such situations as
an artifact of the novelty of prediction markets that will phase out as venues mature and resolution-
rule conventions standardize; this is not a limitation of our betting strategy but of the underlying
contract specification. The event was titled“What will be the top AI model this month?”and the
published resolution rule reads in full:“If claude-opus-4-6-thinking is the top-ranked AI model
on Apr 30, 2026 at 10:00 AM ET, then the market resolves to Yes. ”The rule does not specify which
leaderboard, benchmark, or evaluation suite determines “top-ranked,” nor does it name the operator
that produces such a ranking. Furthermore, plausible benchmarks — LMArena, Artificial Analysis,
the OpenLLM Leaderboard, MMLU, etc. — can even disagree on a given day, so the market’s
outcome is determined by the market operator’s discretionary choice of ranking source rather than
by any externally verifiable fact. We therefore treat this market as failing the resolution-clarity
precondition for forecasting and exclude it from the agent’s eligible set 9.
D.7.3 Case studies
We present two representative case studies drawn from live trading runs to illustrate how the proposed
strategy operates in practice. These examples highlight both the decision-making process and the
resulting performance.
Case 1: Weekly Executive Order count (KXEOWEEK-26APR25-0).This contract asked whether the
President of the United States would sign more than 0 Executive Orders between April 19–25, 2026.
By the time the agent first evaluated the market on April 21, public news cycles were dominated by a
recent executive order (EO) accelerating medical treatments for serious mental illness, and Kalshi
traded YES at 0.77. Gemini 3 priced YES essentially in line with the market, but on April 22 issued
aBUY_NOsignal with the rationale:
“That specific Executive Order (accelerating medical treatments for serious mental illness)
was signed on Saturday, April 18, which falls just outside the April 19–25 window. No
new Executive Orders have been signed so far between April 19 and April 22, leaving only
three days in the market period. The current prediction market probability of66%is likely
inflated by traders conflating the April 18 signing with this week’s news cycle, so the true
probability of an additional EO being signed in the remaining window is materially lower.”
Eight prior forecasts in which model and market had agreed onpyes ≈0.77 , the model’spyes collapsed
to 0.31 in a single cycle while Kalshi’s yes_ask still sat at 0.66, opening a 35-cent edge on the NO
side. The strategy converted that edge into35NO shares at$0.37per share.
As the market then drifted in the model’s direction over the following five days—first tono_ask=
0.68 on April 24, then to no_ask= 0.99 by April 27—the position was gradually reduced as the
edge decayed. Rather than holding a fixed exposure, the rebalancer continuously reassessed whether
8Kalshi’s close_time is the trading deadline and does not always coincide with when the underlying event resolves.
While these align for most events, some have a close_time set hours or days after the outcome is publicly known. This
discrepancy is observable ex ante via a field in the API deemed the expected_expiration_time, which indicates the
event’s resolution time.
9Subsequent monthly versions of this contract now explicitly specify the LM Arena leaderboard as the resolution source.
27

additional upside remained. It sold part of the position as soon as the mispricing meaningfully
narrowed, taking 7 shares at $0.67 (+$1.87), and later unwound most of the remaining exposure near
certainty at$0.98(+$4.35), where further gains were negligible.
The remaining 23 shares, accumulated at an average cost of $0.43, were held into resolution: the
President signed zero Executive Orders that week, the contract resolved NO, and the residual position
paid out at $1.00 per share for an additional +$13.01. The per-market net P&L of +$19.23 on a
peak cost basis of $15.21 (+126%) reflects gains accrued both through early liquidation at improving
prices and through the final resolution payoff.
Case 2: U.S. Strategic Petroleum Reserve level (KXSPRLVL-26APR01-T415).This contract asked
whether the U.S. Strategic Petroleum Reserve (SPR) level on April 1, 2026, would be above 415
million barrels. The reserve had been stable at 415.44 million barrels for several weeks, but on
March 11 the Department of Energy announced a 172-million-barrel emergency drawdown, which
led the market to price in a high probability of the level falling below415.
By March 28, Gemini 3 was already assigning low probability to YES (around 0.13), and the agent
initially accumulated NO positions. However, on March 30 at 14:06 UTC, the agent reversed sharply
after identifying a timing mismatch in how the data is measured. It recognized that the EIA Weekly
Petroleum Status Report records inventory as of 7:00 a.m. on Fridays, while the early phase of the
announced drawdown had not yet been formally recorded in contract awards or physical accounting
at that cutoff:
“The Department of Energy did not award the initial contracts for the first 45.2 million barrels
until Friday, March 27. The EIA’s Weekly Petroleum Status Report measures inventory
strictly as of 7:00 a.m. on Fridays, meaning any physical shipments that commenced later
that day will not be captured in the data for the week ending March 27. Consequently, the
SPR level—which has held perfectly steady at 415.44 million barrels for several weeks—will
almost certainly print above 415 in the upcoming release.”
In other words, although drawdown activity had been announced, it had not yet entered the official
measurement window used for settlement. This meant that the upcoming report would still reflect the
pre-drawdown level.
Acting on this insight, the agent closed its NO position and bought 81 YES shares at $0.12. The
following day, the EIA release confirmed the SPR level remained at 415.44 MMbbl, and the contract
repriced to $0.87, allowing the agent to sell the full position for a +$60.75 profit on that leg alone (a
+625%return).
After accounting for earlier position adjustments and small late-cycle bets, the net realized P&L
was +$45.65 on a $10.92 cost basis. The key driver of performance was not disagreement about the
drawdown itself, but the agent’s correct identification of the measurement cutoff: it exploited the fact
that announced changes had not yet entered the reporting window used for settlement.
D.8 Profitability at extreme margins
While most large margin bets are wrong (Table 9 illustrates a win rate ≪50% for each high-margin
bin for each model), the ROI can remain positive because the payoff on the rare correct bets scales
sharply with margin. In these extreme bins, favorable prices mean that a small number of correct,
high-conviction bets can more than offset the many losses, yielding positive returns despite low
directional accuracy. This effect is most pronounced in the [0.70,0.9) bin for Conservative personas,
where even a handful of correct predictions drives substantial gains. We highlight two such cases
below from Claude Opus 4.6 and Gemini 3.
Case 1: Kirk Cousins’s next team ( KXNEXTTEAMNFL-26KCOUSINS).This 32-way market asked
which NFL team Kirk Cousins would sign with after his March 11, 2026 release by the Atlanta
Falcons. On the “Stays with Atlanta or Retires” contract, Kalshi traded YES at 0.78, while Claude
28

Table 9:Per-bin profitability at high margins ( |p−q| ≥0.50). For each persona and each margin bin,
we report the (%) share of total bets, directional win rate, and ROI under the corresponding scoring
rule (Log for Brittle / Dispersed, Brier for Conservative).
Persona Bin Share (%) Win % ROI (%)
Brittle
[.50, .70) 3 16.2−17.3
[.70, .90) 2 7.0−57.4
[.90, 1.0) 1 15.6+191.6
Dispersed
[.50, .70) 6 34.3+0.3
[.70, .90) 5 14.3−25.5
[.90, 1.0) 4 2.7−57.9
Conservative
[.50, .70) 0 17.6+25.8
[.70, .90) 0 10.5+197.8
[.90, 1.0) 1 2.9+76.3
Table 10:Per-market Brier-strategy economics for two extreme-margin case studies. pyes is the
model’s predicted probability for YES; qyes is the YES-side ask price; y is the realized outcome.
Weight is the margin|p−q yes|.
Market (Kalshi ID) Predicted Resolvedp yes qyes yWeight ROI (%)
Case 1: Kirk Cousins’s next team – “Stays with Atlanta or Retires” (Claude Opus 4.6)
Stays with Atlanta or retires 2026-03-11 2026-03-250.03 0.78NO0.75 +21%
Case 2: Rain in Dallas, January 2026 – “Above 2 inches” (Gemini 3)
Above 2 inches 2026-01-25 2026-02-010.22 0.98NO0.76 +1900%
Opus 4.6 assigned p= 0.03 , an implied disagreement of 0.75. Its rationale (recorded same-day,
2026-03-11):
“Kirk Cousins is being released March 11, 2026 and wants to play. The Arizona Cardinals
have the clearest QB vacancy after releasing Kyler Murray, with strong scheme fit under
new HC Mike LaFleur (Shanahan/McVay system). Multiple insiders from NBC Sports, SI,
and PFT have identified Arizona as the top landing spot, with Cousins offering a bridge
starter option alongside weapons like Marvin Harrison Jr. Pittsburgh is the main alternative
if Rodgers retires, while most other QB-needy teams (Vikings targeting Murray, Dolphins
signed Willis, Jets got Geno Smith) have already addressed the position. Cousins may take
his time signing, but Arizona’s need is clear and urgent.”
The model’s edge here is real-time news synthesis: same-day reports confirming Cousins’s intent to
keep playing, combined with insider coverage identifying Arizona as the destination, and elimination
of competing QB-needy teams that the market price had implicitly assumed were still in play. Cousins
did not remain in Atlanta and did not retire. Under the Brier strategy, the position bought 0.75 NO
shares at$0.83, costing$0.622; the contract resolved NO, paying$0.75, for a return of+21%.
Case 2: Rain in Dallas, January 2026 (KXRAINDALM-26JAN).This 7-way ladder market asked the
cumulative January precipitation in Dallas. On the “Above 2 inches” contract, Kalshi priced YES at
0.98(with NO at0.05), while Gemini 3 assignedp= 0.22. Its rationale (recorded 2026-01-25):
“NWS data confirms recorded precipitation of 0.48 inches through Jan 23, with a winter
storm forecast to add ∼0.5–0.8 inches of liquid equivalent, making the total likely to reach
1.0–1.5 inches. The provided market data was discounted due to internal inconsistencies
(P(>3) > P(>2)) and contradiction with verified meteorological reports. Probabilities favor
exceeding 1 inch but decline sharply for 2+ inches given the dry start to the month and
limited remaining forecast precipitation.”
29

The actual January total fell short of two inches. The Brier strategy bought 0.76 NO shares at
0.05, staking 0.038 and paying out 0.76—a return of +1900%. Two factors made the disagreement
actionable: (i) verifiable third-party meteorology directly contradicted the market’s near-certainty,
and (ii) the model identified an internal inconsistency in the order book—specifically, the probability
for P(>3) inches was greater than that of P(>2) inches, violating monotonicity (due to factors like
thin liquidity or delayed updates across related contracts). By detecting this structural mismatch, the
model effectively inferred that at least one of the prices must be miscalibrated, and correspondingly
discounted the market signal rather than treating it as fully informative.
In both cases, the model’s advantage stems from combining verifiable public data with effective
information synthesis. The models identify and integrate disparate signals – real-time reporting
(Cousins), structured third-party data (NWS) – into coherent forecasts that the market had not yet
fully incorporated. The Dallas precipitation case further illustrates an additional capability: detecting
and reasoning about internal inconsistencies in market prices themselves.
As such, these examples suggest that LLM forecasters are particularly well-suited to settings with a
large, readily available body of public information that is dispersed across sources, or where market
prices contain internal inconsistencies. In these environments, LLMs can aggregate, cross-reference,
and reconcile information more efficiently than humans, forming a coherent view faster than the
market updates.
30
