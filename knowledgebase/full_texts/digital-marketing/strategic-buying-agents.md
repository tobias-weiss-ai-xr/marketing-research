---
title: Strategic Buying Agents
url: https://arxiv.org/abs/2607.04708
category: digital-marketing
subcategory: empirical
date: 2026-07
venue: ''
authors:
- Mingyang Fu
- Ming Hu
source: arxiv
pdf_url: https://arxiv.org/pdf/2607.04708
pages: 67
chars: 155963
fetched_at: '2026-11-08T13:21:32+00:00'
kb_version: 1
---

# Strategic Buying Agents

Strategic Buying Agents
Mingyang Fu
Rotman School of Management, University of Toronto, mingyang.fu@utoronto.ca
Ming Hu
Rotman School of Management, University of Toronto, ming.hu@rotman.utoronto.ca
The emergence of agentic AI is shifting online shopping from search and recommendation toward delegated
purchasing by autonomous buying agents that monitor markets, reason about uncertainty, and make purchase
decisions on behalf of consumers. We study the design of strategic buying agents that decide when to purchase
an item within a finite shopping window. The central challenge is to translate price observations, the shopping
window, and information about future price changes into a purchase policy. We formulate this problem
across three information regimes: stationary, Bayesian, and robust, and use the resulting optimal policies as a
policy menu for implementation. In the stationary regime, price adjustments follow an exogenously specified
Poisson arrival process, and post-adjustment prices are drawn from a known stationary distribution. We
show that the optimal policy is a dynamic purchase-threshold policy, with the threshold characterized by
an ordinary differential equation. In the Bayesian regime, the adjustment intensity is assumed known, but
the price-adjustment distribution is uncertain. We show that the optimal rule remains threshold-based, with
the threshold depending on posterior beliefs. We also bound the value of knowing the true price-adjustment
distribution. In the robust regime, the agent relies only on price bounds and seeks worst-case protection. We
show that randomized threshold policies yield optimal guarantees for both competitive ratio and minimax
regret. Finally, we evaluate our proposed policies using Amazon product price histories tracked by Keepa,
comprising 367 items and 48,933 time-stamped price observations. We also examine how these policies can be
incorporated into language-model buying agents. On our test instances, the stationary and Bayesian policies
perform competitively in terms of mean normalized consumer surplus despite their stylized assumptions,
while the robust policy performs best at the 10th percentile of the normalized surplus distribution. The
results also suggest that language models are better suited to choosing among the three information regimes
and selecting price samples for calibration than to making buy-or-wait decisions directly.
1. Introduction
Online shopping platforms have historically treated human consumers as the primary decision makers.
Consumers search, compare products, evaluate prices, and complete checkout, while platforms provide
search tools, recommendations, and payment systems. Recent developments in agentic commerce
suggest a different mode of interaction, in which consumers may delegate parts of the shopping
process to AI agents that monitor products, compare prices, and execute transactions subject to
user-specified conditions ( Bloomberg Odd Lots 2026, OpenAI 2025a, Stripe 2025a,b, 2026b,a). More
1
arXiv:2607.04708v1  [econ.TH]  6 Jul 2026

2
broadly, deployed web-agent systems show that agents can already navigate interfaces and execute
user-directed actions ( OpenAI 2025c,b).
Together, these AI technologies make delegated shopping feasible. A broad literature on online
commerce has generated rich insights into search, recommendation, and consumer choice. Recent
work on LLM-enabled operational decision support further shows how language models can structure
decision inputs, invoke analytical tools, and communicate recommendations ( Simchi-Levi et al. 2025,
Baek et al. 2026). These advances provide important functional ingredients for shopping agents:
an agent may be able to browse product pages, monitor price adjustments, interpret a consumer’s
request, update its assessment of the shopping task, and complete checkout through the payment
infrastructure. Yet they do not by themselves determine how the agent should act after observing
the current price. We study this buying-policy problem for an automated buyer facing uncertainty
about future price changes.
We focus on a basic delegated-purchase decision: when to buy a single item within a finite shopping
window. This decision arises naturally in e-commerce. A consumer may need to make a purchase
before a trip, a gift occasion, or a sale expiration date. During the shopping window, the posted
price can fluctuate. Thus, the agent’s problem is to decide whether the current price is suﬀiciently
attractive relative to the option value of waiting. Figure 1 illustrates the type of shopping instance
that motivates our problem. In the example, the consumer asks for a speaker, states a budget and
a deadline in natural language, and the agent observes the speaker’s product page together with its
price history.
Figure 1 Illustrative shopping instance with product information, price history, and consumer request.
Illustrative shopping instance: product page and price history
Online product page
Marshall
Product image
Marshall Acton III
Bluetooth Home Speaker
4.8⋆ ⋆ ⋆ ⋆⋆ (2,266)
$379.98
Colour name:Black
$379.98 $329.98 $329.98
I want the black Marshall Acton III speaker for a small gathering
next Sunday . I can pay up to $400, but I would rather wait if the
price is unusually high.
Price history
$184
$250
$316
$382
$448
May Sep Jan May
current price
recent low near $250
Consumer request
Item Black Marshall Acton III
Budget $400
Needed by next weekend
Seller-side theoretical models typically treat buyers’ strategic behavior as given, with sellers
responding under stylized informational assumptions. In many such models, for instance, the seller

3
commits to a deterministic, preannounced price trajectory that buyers treat as known. A buyer-side
agent operating in a real marketplace instead faces an online decision problem. It observes historical
prices and incoming price adjustments during the shopping window, but does not know the future
price path. The design problem is to construct a purchase policy. At each decision time, the agent
maps the consumer’s valuation, the current price, the remaining time, and its information or belief
about future price changes into a buy-or-wait decision. Figure 2 illustrates how we decompose this
design problem into two layers: formulation and optimization. The formulation layer converts the
shopping task and observed market information into a specific decision problem, while the optimiza-
tion layer solves this problem to obtain an implementable buy-or-wait rule.
Figure 2 Purchase-timing decision process for a buying agent. A shopping task provides the item, its value, and
a finite window. The decision process maps price information, time remaining, and regime-specific information or
belief into a buy-or-wait decision, with new observations updating the relevant state before subsequent decisions.
new observation
$
Shopping task
item, valuation,
shopping window
Decision process
Market
representation
price trajectory
time left
Formulation toolkit
Robust
Bayesian
HJB equation
Backward induction
Value iteration
=
->
DP...
 Decision
rule
thresholds, timing,
action choice
Action interface
buy, wait
task input
formulate optimize
execute
decision inputs
We construct the formulation layer of the agent-design problem based on the information the
agent can rely on about future price changes. Rather than imposing a single model, we study three
representative formulations under distinct informational assumptions. In implementation, we use a
heuristic selector or LLM to decide which model to use given the available information. The first
regime establishes a benchmark in which the agent believes the seller’s pricing behavior is stable and
can be calibrated using historical data. Specifically, the agent trusts that price adjustments arrive
at a constant rate and that each post-adjustment price is drawn from a stationary distribution fully
known in advance. In this environment, the optimal buying rule is a dynamic threshold: the agent
purchases when the current price falls to or below a threshold that depends on the remaining time. We

4
show that the purchase threshold is discontinuous at the deadline: immediately before the deadline,
it can lie below the consumer’s valuation, whereas at the deadline, the agent purchases whenever
the posted price does not exceed that valuation. The threshold characterization also identifies the
policy’s operational levers: longer windows and more frequent adjustments make the agent more
selective, while less attractive price-adjustment distributions and higher consumer valuations make
earlier purchases more likely. A simple extension in Section 4.3 allows the post-adjustment price
distribution to shift along a known deterministic trend. The optimal policy remains a threshold
rule, with the trend raising or lowering the purchase threshold through the expected future price
adjustments.
The second regime considers settings in which the agent still anticipates random price adjustments
at a constant arrival rate and believes the prices are drawn from a stable but unknown distribution.
Facing this uncertainty, the agent begins with a prior using historical data and updates its belief
as prices change during the shopping window. The optimal rule remains threshold-based, but the
threshold now depends on the posterior belief and the time left until the deadline. Each price adjust-
ment, therefore, plays two roles: it creates a new purchase opportunity and signals the seller’s latent
pricing regime. A high observed price reduces the current surplus and makes future price opportuni-
ties appear less favorable, thereby raising the subsequent purchase threshold through belief updating.
Beyond the form of the rule, the Bayesian regime asks when distributional uncertainty materially
changes the buying decision. Very short windows leave little opportunity for price adjustments and
belief updating, and long windows give the agent enough time to learn the latent regime. The diﬀicult
cases are intermediate windows, where the shopping window is too short for the agent to identify
the underlying price-adjustment distribution, yet long enough for stochastic price fluctuations to
noticeably affect the optimal surplus.
The third regime considers settings in which the agent cannot rely on a stable probabilistic model
of price changes. Instead, the agent knows only bounds on feasible prices, which can be observed
from historical data, and seeks worst-case protection. The worst-case price path resembles a flash
sale: the price can decline gradually, making delay attractive, and then jump back to a high level
when the sale ends at an unknown time. This tension points to the use of randomized threshold
policies as a robustly optimal response. The agent draws a purchase threshold at the beginning of
the window and makes a purchase the first time the observed price falls to or below the threshold,
with the threshold distribution calibrated to protect against adverse paths. We characterize optimal
guarantees for both the competitive ratio and minimax regret. Minimax regret is useful when the
initial price yields no positive surplus, because the competitive ratio collapses to zero in this case.
Table 1 summarizes the three information regimes. Throughout the paper, we refer to the stop-
ping rules induced by our three formulations as operations research (OR) policies. This terminology

5
separates these OR policies from purchasing policies that may also generate purchasing decisions but
are not derived from solving an explicit OR model.
Table 1 Information Regimes and Purchase Policies
Model Information regime Purchase policy
Stationary Known adjustment intensity; known price-adjustment distribution Time-dependent threshold
Bayesian Known adjustment intensity; unknown price-adjustment distribution Belief-dependent threshold
Robust Arbitrary adjustments; price bounds only Randomized threshold
Finally, we evaluate our stopping rules using tracked Amazon product price histories covering 367
items and 48,933 time-stamped posted-price observations. The evaluation compares several classes
of methods. Fixed OR policies apply a given stopping rule based on our models with parameters
estimated from pre-window price history. A heuristic selection method, referred to as the Heuristic
Selector policy, chooses among these OR policies using diagnostic screens computed from the pre-
window price history and then applies the selected OR policy to make the stopping decision. The
LLM-OR agent uses the language model to select the policy and primitive inputs, while the selected
OR policy makes the stopping decision. The remaining methods do not use OR policies. The LLM-
baseline specifies whether to buy the item now or at a target purchase time, and this query is repeated
after each price adjustment detected by an automated monitoring program. Other simple baselines
include purchase policies that buy the item immediately or only at the deadline, and statistical-
threshold rules that make a purchase before the deadline if the price falls to or below the pre-window
minimum, mean, or median, with terminal purchases when the price is no more than the consumer’s
valuation. The evaluation shows that stationary and Bayesian policies perform favorably relative to
simple baselines in terms of mean normalized consumer surplus, while the robust policy performs best
at the 10th percentile of the normalized surplus distribution. Moreover, language models are more
effective at selecting, calibrating, and explaining our OR policies than at making purchase-timing
decisions directly.
2. Literature Review
First, our paper relates to the literature on digital marketplaces and automated buying agents. Early
work on agent-mediated e-commerce, such as Maes et al. (1999) and He et al. (2003), envisioned
software agents that represent buyers and sellers, automate stages of the consumer buying process,
and negotiate subject to user-specified constraints such as reservation prices and deadlines. Digital

6
marketplaces and comparison shopping technologies reduce buyer search costs ( Bakos 1997), affect
price competition, and reshape the information environment in which consumers compare products,
sellers, and prices ( Brynjolfsson and Smith 2000, Kephart and Greenwald 2002). Recent language
models and autonomous agent systems extend the idea of delegated online shopping from information
retrieval toward agents that can navigate interfaces ( Yao et al. 2022), reason over instructions, and
take actions on behalf of users ( Yao et al. 2023). Weber et al. (2020) analyze business models for
highly autonomous consumer buying agents, emphasizing how delegation can reshape the roles of
consumers, platforms, and intermediaries. Allouah et al. (2025) evaluate AI shopping agents in con-
trolled e-commerce environments and document choice homogeneity and strong model dependence in
product selection. Complementary work studies the preference-acquisition side of agentic shopping:
Cao and Hu (2026) study a problem of first soliciting consumer preferences through conversation
and then recommending products based on learned preferences, while Kumar et al. (2026) examine
how much a conversational recommender should converse when elicitation improves matching but
imposes communication costs. We build on this stream by focusing on a consumer-side operational
decision that arises after observing the price path: the buyer-side agent’s intertemporal purchase
policy.
Our paper also belongs to the research stream on forward-looking consumers and dynamic pur-
chase behavior. In marketing and economics, consumers may time purchases in response to sales and
inventory considerations ( Hendel and Nevo 2006), as well as current and future prices and product
availability (Nair 2007). Assunção and Meyer (1993) derive a rational purchase and consumption pol-
icy under uncertain future promotions, showing how price expectations and inventory considerations
shape intertemporal purchasing. In operations management models of strategic consumers, sellers
anticipate that buyers may purchase the item immediately, wait for lower prices, or exit the market.
Su (2007) provides a formulation of seller pricing with strategic consumers, showing how heterogene-
ity in consumer valuations and patience shapes the seller’s optimal price path. Subsequent research
examines more specific seller-side levers such as announced discount commitments ( A viv and Pazgal
2008), capacity rationing ( Liu and van Ryzin 2008), and quick response ( Cachon and Swinney 2009).
More recent work emphasizes uncertainty and learning in these dynamic pricing environments. Moon
et al. (2017) study randomized markdowns in e-commerce environments with heterogeneous consumer
costs of monitoring prices and availability. A learning-oriented counterpart is Birge et al. (2025), who
analyze markdown policies when the seller learns demand while facing forward-looking customers.
Other seller-side studies examine markdown pricing with an unknown fraction of strategic consumers
(Mersereau and Zhang 2012) and randomized promotions as an intertemporal price-discrimination
mechanism (Chen et al. 2023). We share with this literature the premise that consumers are forward-
looking, but shift the focus from seller-side policies to consumer-side decision policies.

7
Our modeling of posted prices builds on the literature on price stickiness and dynamic price
adjustment. Macroeconomic models of sticky prices ( Golosov and Lucas 2007) and empirical work
using retail price microdata ( Nakamura and Steinsson 2008, Cavallo 2018) have documented that
posted prices often remain fixed for a while before being adjusted. Online retailing also features
algorithmic repricing and heterogeneous price-adjustment behavior among sellers ( Chen et al. 2016a).
Related dynamic-pricing settings study pricing policies with limited opportunities for adjustment
(Chen et al. 2016b) and the welfare effects of price adjustments in airline markets ( Williams 2022).
In the stationary and Bayesian information regimes, our modeling approach is closest in spirit to
Calvo (1983): prices remain fixed until random adjustment opportunities arise, after which a new
posted price is generated. We use this representation from the buyer’s perspective as an exogenous
price environment rather than as a structural model of seller behavior.
Methodologically, our OR policies are close to the literature on optimal stopping. One classical
branch studies timing decisions when the payoff-relevant state follows a Markov process; the decision
maker stops when the process crosses an endogenous threshold. This branch underlies real-options
and investment-timing models ( McDonald and Siegel 1986, Peskir and Shiryaev 2006). A second
branch examines sequential search using reservation rules to evaluate randomly arriving alternatives,
commonly applied to job search ( McCall 1970, Lippman and McCall 1976), price search ( Rothschild
1974), and asset selling ( Rosenfield et al. 1983). Our OR policies adopt this threshold logic in a
buyer-side posted-price setting. Our focus is on how the purchase threshold depends on the agent’s
information, with its form varying according to the agent’s model of future price changes and the
resulting decision problem.
Finally, the paper relates to learning and robust online decision-making. Our Bayesian policy
relates to learning in dynamic pricing. Much of this literature studies how sellers set prices while
learning an unknown demand function or demand model ( Besbes and Zeevi 2009, Keskin and Zeevi
2014). Bayesian formulations model demand uncertainty through priors over demand environments
and update beliefs as sales observations arrive ( Harrison et al. 2012). The literature also considers
richer intertemporal features, including discounted objectives ( Feng et al. 2024) and cyclic pricing
with patient customers (Zhang and Jasin 2022). For a broader review of dynamic pricing and learning,
see den Boer (2015). Our Bayesian model instead studies passive learning by a buying agent who
observes market-generated price adjustments. Our robust policy relates to online algorithms and
competitive analysis ( Borodin and El-Yaniv 1998), in which policies are evaluated on uncertain or
adversarial input sequences ( Karp et al. 1990, Mehta et al. 2007). In the context of online algorithms,
El-Yaniv et al. (2001) is methodologically close to this paper. They study a one-way trading problem
in which a trader observes prices sequentially and must act without knowing future realizations. This
framework is close to our robust setting, where the agent relies on price bounds rather than a full
probabilistic model.

8
3. Purchase-Timing Environment
Before introducing particular models of price evolution, we specify the common operating environ-
ment for the buying agent. The purchase-timing problem takes the item, valuation, and deadline as
exogenous task inputs. The models in Sections 4 to 6 differ in the information the agent can use
about future price changes, but share the same operating interface.
The agent has monitoring and transaction capabilities. It observes the posted price process sequen-
tially throughout the shopping window and, at any time before the deadline, can either purchase
at the currently posted price or continue monitoring. We abstract from monitoring and checkout
delays, so a purchase decision is implemented at the price observed when the decision is made. A
purchase terminates the task, and the agent’s action does not affect the future price process. Thus, an
implementable buying policy must be adapted to the price history, elapsed time, and the information
available under the relevant regime.
Decision primitives. The shopping window has a length T . We use elapsed time t 2 [0, T], where
t = 0 is the beginning of the shopping window and t = T is the deadline. The consumer has valuation
v for the item. If the agent purchases at price p, the consumer receives surplus (v  p)+. If the agent
exits the shopping window without making a purchase, the payoff is zero. This formulation isolates
the timing decision. The agent’s task is to decide when the current price is good enough to buy.
At any decision point, the relevant state consists of the current price, the time remaining until
the deadline, and the regime-specific information or belief about future prices. The current price
determines the payoff from buying immediately, the remaining time determines the opportunity to
wait, and the information regime determines how the agent evaluates that waiting option. A buying
policy maps this state into a buy-or-wait decision.
Information regimes. We organize the design problem around three informational regimes. Each
regime specifies a different information structure that the agent can use to model future price changes.
First, in the stationary price-adjustment regime, the agent knows both the adjustment intensity
and the price-adjustment distribution. This regime serves as the most structured benchmark for
computing the expected continuation value of waiting.
Second, in the Bayesian learning regime, the agent retains the assumption of the Poisson arrival
for price adjustments but does not know the price-adjustment distribution. The agent begins with a
prior over possible price environments and updates its belief as price changes are observed.
Third, in the robust regime, the agent does not rely on a probabilistic model of price evolution.
Instead, it knows only bounds on feasible prices and seeks protection against worst-case paths.
This regime is appropriate when historical data are sparse, price dynamics are unstable, or model
calibration is not credible.

9
These regimes form a hierarchy of informational assumptions. The stationary regime represents
the most structured case in which the agent can evaluate future opportunities through a specified
stochastic model. The Bayesian model relaxes this structure by treating the price-adjustment distri-
bution as unknown, so new price observations update the agent’s belief about the price environment.
The robust model imposes the least structure and replaces expected optimality with worst-case per-
formance guarantees.
4. Buying in a Stationary Price-Adjustment Environment
This section studies a stationary stochastic environment for seller price adjustments. The agent
observes the seller’s current posted price, while future prices remain stochastic and outside the agent’s
control. The current price remains available until the seller revises it, and the agent must decide
whether to purchase now or continue monitoring for a more favorable price before the deadline. This
OR model reduces the monitoring problem to computing a threshold policy once the adjustment
intensity, price-adjustment distribution, valuation, and deadline are specified.
4.1. Stationary Price-Adjustment Model
The central primitive is a stationary price process. The posted price remains fixed until an adjustment
opportunity arrives. Adjustments arrive according to a homogeneous Poisson process with rate λ,
and each adjustment redraws the posted price from a stationary distribution H. This follows the
Calvo formulation of price stickiness, where price adjustment opportunities arise randomly and are
memoryless ( Calvo 1983).
Let P  R+ denote the feasible price space equipped with its Borel sigma-field B(P). Write Pt for
the posted price at elapsed time t, so P0 is the window-start price and PT is the deadline price.
Assumption 1. The price path is generated by the following primitives.
(i) Poisson adjustment. Adjustment opportunities arrive over elapsed time according to a homo-
geneous Poisson process fNr : r  0g with rate λ 2 (0, 1).
(ii) Stationary price-adjustment distribution. At each adjustment time, the post-adjustment
price is drawn independently from a time-invariant distribution H on P.
(iii) Price stickiness. Given a window-start price P0, elapsed adjustment times frngn≥1, and post-
adjustment prices fYngn≥1, the posted price is piecewise constant:
Pt =
(
P0, 0  t < r1,
Yn, r n  t < rn+1, n  1.
The distribution H is the agent’s predictive distribution for the next post-adjustment price;
throughout the paper, we refer to H as the price-adjustment distribution. This framework allows the
agent to aggregate heterogeneous adjustment triggers, such as competitor promotions and stochastic

10
demand shocks, without requiring the agent to identify the specific drivers behind each price change.
Formally, we represent each unique category of adjustment triggers as an event e 2 E and assume
events arrive according to a memoryless point process with relative intensities µ(de). Conditioned
on the occurrence of event e, the seller’s response is captured by an event-specific price-adjustment
distribution He. The composite predictive distribution is H(A) =
R
E He(A) µ(de), A 2 B(P). Since
the agent’s stopping problem depends on future adjustments only through the aggregate arrival rate
and the predictive price-adjustment distribution, we adopt (λ, H) as the environment’s primitives.
Throughout this section, we restrict our focus to nondegenerate buying environments in which the
price-adjustment distribution can generate a price no higher than the consumer’s valuation, i.e.,
inf supp(H)  v. Otherwise, all future post-adjustment prices exceed the valuation, so waiting is
never beneficial, and the problem is degenerate.
4.2. Buying-Agent Problem
At elapsed time t 2 [0, T], suppose the current posted price is Pt = p. Let Tt denote the set of admis-
sible stopping times taking values in [t, T]. Since both the price-adjustment arrivals and the price-
adjustment distribution are stationary, elapsed time affects the continuation problem only through
the time left until the deadline, T  t. Thus, the agent’s value function can be written as
V (T  t, p) := sup
τ ∈Tt
E
h
(v  Pτ )+

 Pt = p i , (1)
where Pτ denotes the posted price at the purchase time. If the agent does not stop before the deadline,
the terminal payoff is (v  PT )+.
4.2.1. Optimal Buying Policy. Denote the time-to-go T  t by s for convenience. The value
function ( 1) satisfies the finite-horizon optimal stopping variational inequality
max

(v  p)+  V (s, p), ∂sV (s, p) + λ EH [V (s, P)]  λ V (s, p) 	 = 0, s 2 (0, T], (2)
with terminal condition V (0, p) = (v  p)+. The stopping set is S :=  (s, p) : V (s, p) = (v  p)+	 and
the continuation set is W :=

(s, p) : V (s, p) > (v  p)+	 .
Lemma 1. Under Assumption 1 , the value function V (s, p) is non-increasing and 1-Lipschitz in
p and non-decreasing and continuous in s.
The price monotonicity and Lipschitz property imply that the relative option value of waiting,
W (s, p) := V (s, p)  (v  p), is non-decreasing in p on [0, v]. Hence, for each fixed s, there exists a
threshold b(s) such that the stopping set takes the form [0, b(s)].
Proposition 1 (Optimal Purchase-Threshold Policy). Under Assumption 1, the follow-
ing hold.

11
(i) There exists an optimal threshold function b : [0, T] ! [0, v] such that, at each elapsed time
t  T , the agent makes a purchase whenever the current price satisfies Pt  b(T  t) and waits
otherwise.
(ii) Let m(s) := EP ∼H [V (s, P)]. For every s > 0, the threshold satisfies b(s) = v  m(s). Conse-
quently, b solves the ODE
b′(s) = λ EP ∼H  (b(s)  P )+ , (3)
for almost every s > 0, with initial condition lim
s↓0
b(s) = EH [minfv, P g].
(iii) The purchase threshold b(s) is non-increasing and convex on (0, T].
At the deadline, the agent purchases if and only if PT  v, so the terminal threshold is v. Imme-
diately before the deadline, however, the dynamic threshold has right limit b(0+) = EH[minfv, P g].
Hence, the optimal purchasing threshold is discontinuous at the deadline whenever H places positive
mass below v. The jump arises because waiting briefly does not immediately forfeit the current price:
if no adjustment occurs, the agent can still purchase at the unchanged price; if an adjustment occurs,
the agent observes a new post-adjustment price draw. Thus, even an arbitrarily short positive horizon
gives the agent a one-sided opportunity to obtain a lower price, lowering the pre-deadline threshold
from v to b(0+).
The limiting thresholds also clarify how simple static rules can be interpreted. A mean-price rule,
which purchases when the current price is no larger than the average post-adjustment price EH[P ],
reflects a short remaining time logic: it coincides with the pre-deadline limit when the valuation is
high enough, v  sup supp(H), in which case b(0+) = EH[P ]. At the other extreme, the ODE implies
lims→∞ b(s) = inf supp(H), so the lower-support rule captures the long remaining time logic: with
many future adjustment opportunities, the agent can afford to wait for unusually favorable prices.
4.2.2. Comparative Statics and Illustration. Having characterized the optimal policy for a
fixed buying environment, we next ask how it changes when the primitives vary. This comparative-
statics question is important for both implementation and interpretation: the arrival rate, the price-
adjustment distribution, and the consumer valuation each enter the stopping rule through a distinct
economic channel. To compare price-adjustment distributions without imposing a parametric family,
we order them by first-order stochastic dominance (FSD, also known as the usual stochastic order):
we write H1 FSD H2 if H2 first-order stochastically dominates H1 (cf. Hadar and Russell 1969, Bawa
1975, Shaked and Shanthikumar 2007).
This order provides a nonparametric way to compare future price opportunities. A stochastically
larger price-adjustment distribution makes low future prices less likely, while changes in λ and v alter
the frequency of opportunities and the payoff from purchase. The next result demonstrates how these
three primitives impact the optimal purchase threshold.

12
Proposition 2 (Stationary Threshold Monotonicity). For every s > 0, the optimal
threshold b(s; λ, H, v) satisfies the following monotonicity properties.
(i) b(s; λ, H, v) is non-increasing in λ: if λ1  λ2, then b(s; λ2, H, v)  b(s; λ1, H, v).
(ii) b(s; λ, H, v) is non-decreasing (in the sense of FSD) in H: if H1 FSD H2, then b(s; λ, H1, v) 
b(s; λ, H2, v).
(iii) b(s; λ, H, v) is non-decreasing in v: if v1  v2, then b(s; λ, H, v1)  b(s; λ, H, v2).
The comparative statics highlight three distinct effects. First, a larger λ makes the next price
adjustment arrive sooner, reducing the cost of waiting. The agent, therefore, becomes more selective
and stops only at a lower posted price. Second, a stochastically higher price-adjustment distribution H
makes waiting less attractive. The stopping threshold, therefore, increases. Third, a higher consumer
valuation v raises the stopping threshold. A larger v weakly increases the value of future opportunities,
but this effect is realized only in future states where the price is low enough to generate a positive
surplus. For a current purchase opportunity that already yields a nonnegative surplus, a higher v
directly raises the surplus from stopping one-for-one, so the agent is willing to accept a higher price.
Figure 3 Time-dependent purchase threshold b(T − t) as a function of the time t, together with two illustrative
sample paths of the posted price.
0 2 4 6 8 10
Time t
25
50
75
100
125
150
175
200Price / Threshold
threshold b
price path 1
price path 2
The following example illustrates the threshold dynamics in closed form.
Example 1 (Uniform distribution). To illustrate the structure of the optimal policy, con-
sider the case in which the effective price-adjustment distribution is uniform: H = Unif[p−, p+] with
0  p− < p+ and p− < v. For a positive time-to-go s, on the region where b(s) 2 [p−, p+], the ODE ( 3)
becomes
b′(s) =  λ p+  p−
Z b(s)
p−
(b(s)  p) dp =  λ (b(s)  p−)2
2(p+  p−) .

13
This is a separable ODE with a solution
b(s) = p− + 2(p+  p−)

b(0+)  p− 
2(p+  p−) + λs

b(0+)  p−
 ,
where b(0+) = EH[minfv, P g]. Since b(0+)  p+ and b is non-increasing with lims→∞ b(s) = p−, the
threshold remains in [p−, b(0+)]  [p−, p+] for all s > 0, so the closed form above applies globally on
the positive-horizon branch. For v  p+, this simplifies to b(0+) = (p− + p+)/2 and
b(s) = p− + 2(p+  p−) 4 + λs .
The right limit of the purchase threshold at short positive horizons is the midpoint of the support,
and the threshold decays hyperbolically toward the lower endpoint p− as the time-to-go s grows.
This closed-form solution illustrates the general properties established in Proposition 1 : for s > 0, b
is strictly decreasing and strictly convex, with lims→∞ b(s) = p− = inf supp(H).
4.3. Extension: Time-Varying Price-Adjustment Distribution
The stationary benchmark above assumes that the price-adjustment distribution is time invariant.
In some applications, however, part of the seller’s price movement over the shopping window is pre-
dictable. Examples include life-cycle markdown schedules, pre-stockout price run-ups, and calendar-
based promotional campaigns. A simple extension is therefore to let the price-adjustment distribution
shift with elapsed time through a known deterministic trend.
In the trend-aware extension of the stationary benchmark, whenever a price adjustment occurs
at elapsed time t, the post-adjustment price is g(t) + X, X  H0, where g : [0, T] ! R is a given
deterministic trend and H0 is a baseline price-adjustment distribution. Thus the effective price-
adjustment distribution becomes time dependent: Ht(A) = H0

fx : g(t) + x 2 Ag

, A 2 B(P). For
the dynamic program, write s := T  t. The buying problem remains an optimal stopping problem,
but now future adjustment opportunities depend on the current elapsed time, as reflected in HT −s.
The dynamic programming logic of Proposition 1 still holds. Denoting by V tr(s, p) the value
function under the trend-aware dynamics, we have the variational inequality as follows:
max
((v  p)+  V tr(s, p),
 ∂sV tr(s, p) + λ EX∼H0  V tr(s, g (T  s) + X)   λV tr(s, p)
)
= 0, s 2 (0, T], (4)
with terminal condition V tr(0, p) = (v  p)+. Specializing to g  0 recovers (2).
The deterministic trend changes the price-adjustment distribution over time but does not make
those post-adjustment prices depend on the current posted price p. Hence the monotonicity argument
of Lemma 1 carries over: for each fixed time-to-go s, the value function V tr(s, p) is non-increasing in
p. Therefore, the optimal purchase policy is represented by a trend-aware threshold btr(s). At elapsed
time t  T , the agent purchases whenever Pt  btr(T  t).

14
Operationally, the trend component shifts the stopping threshold through the expected level of
future price adjustments. A downward trend makes waiting more attractive by lowering future price
draws; an upward trend has the opposite effect. Figure 4 illustrates how the purchase threshold
changes across several deterministic trend environments, together with sample price paths under each
specification.
Figure 4 Trend-aware purchase thresholds under deterministic linear trend specifications with slope β, together
with two illustrative sample price paths in each case.
30
40
50
60
70
80
90
100
110Price / Threshold
(a) Strong markdown = 2.0
trend g(t)
threshold btr
path 1
path 2
(b) Mild markdown = 0.5
trend g(t)
threshold btr
path 1
path 2
0 2 4 6 8 10
Time t
30
40
50
60
70
80
90
100
110Price / Threshold
(c) Flat (stationary) = 0
trend g(t)
threshold btr
path 1
path 2
0 2 4 6 8 10
Time t
(d) Uptrend = +1.5
trend g(t)
threshold btr
path 1
path 2
5. Buying Under Bayesian Learning
The previous section treats both the adjustment intensity λ and the price-adjustment distribution
H as known. We keep the Poisson adjustment process from Assumption 1 , but replace the known
distribution with a latent one. The true price-adjustment distribution is H˜θ, where ˜θ 2 Θ is fixed over
the shopping window and drawn from a prior belief ˆπ. Conditional on ˜θ, the price process satisfies
Assumption 1 with H = H˜θ. The agent observes realized post-adjustment prices and updates its
posterior belief.

15
5.1. Bayesian Learning of the Price-Adjustment Distribution
We model uncertainty about future price changes through a family of candidate distributions fHθ :
θ 2 Θg, where (Θ, B(Θ)) is a measurable parameter space. A latent pricing environment ˜θ 2 Θ
is drawn once from a prior belief ˆπ 2 P (Θ) and remains fixed throughout the shopping window.
Conditional on ˜θ = θ, adjustment times still arrive according to the Poisson process with rate λ, and
each post-adjustment price is drawn i.i.d. from Hθ. The latent environment can encode one or several
persistent features of the post-adjustment price distribution, such as markdown aggressiveness or
dispersion in price changes. The buying agent does not observe ˜θ directly. Instead, it updates beliefs
from the realized sequence of posted prices observed at adjustment times.
In empirical implementations, the prior ˆπ can be built from contextual predictors, including
comparable-item prices, seller characteristics, and platform-side covariates. We treat the window-
start price P0 as the first in-horizon Bayesian signal rather than as part of prior learning data. This
convention yields a unified formulation for products with and without historical price records. Let
πt() := P(θ 2  j price history observed up to elapsed time t)
be the posterior belief at elapsed time t. Because the adjustment intensity is treated as known,
learning in this section comes entirely from price observations. Hence, the posterior remains constant
between consecutive adjustment times and changes only when a new posted price is observed.
When each distribution Hθ admits a density hθ with respect to a reference measure, Bayes’ rule
implies that, upon observing a post-adjustment price p, the posterior updates according to
Φ(π, p)(dϑ) := hϑ(p)π(dϑ)R
Θ hu(p)π(du) .
We apply Bayes’ rule only to price histories that can arise under the model; for those histories,
the denominator is positive and finite. Prices outside the predictive support are irrelevant for the
dynamic program. Given a belief π, the agent’s predictive distribution of the next post-adjustment
price is
¯Hπ() :=
Z
Θ
Hθ() π(dθ).
Accordingly, the agent’s state is summarized by the pair (p, π): the current posted price and the
current belief about the distribution of the next post-adjustment price.
5.2. Bayesian Buying-Agent Problem
At time t, the buying agent observes the current posted price Pt = p and holds a posterior belief
πt = π. Let Tt denote the set of admissible stopping rules taking values in [t, T]. The Bayesian value
function can be written as
V B(T  t, p, π) := sup
τ ∈Tt
E

(v  Pτ )+ j Pt = p, π t = π  .

16
The terminal condition is V B(0, p, π) = (v  p)+. Because the posterior changes only at adjustment
times, the Bayesian continuation problem is Markovian in the state (s, p, π), where s = T  t denotes
the time-to-go. The corresponding variational inequality is
max
((v  p)+  V B(s, p, π),
 ∂sV B(s, p, π) + λEP ∼ ¯Hπ  V B s, P, Φ(π, P )   λV B(s, p, π)
)
= 0, s 2 (0, T].
5.2.1. Belief-Dependent Threshold Policy. The next proposition shows that the optimal
policy retains a threshold structure, but the threshold now depends on both the time-to-go and
posterior belief.
Proposition 3 (Belief-Dependent Purchase Threshold). Under the Bayesian learning
model, for each fixed (s, π), the mapping p 7! V B(s, p, π) is non-increasing. Moreover, there exists
a belief-dependent purchase threshold b(s, π) 2 [0, v] such that an agent with the current state (p, π)
stops whenever p  b(s, π) and continues whenever p > b(s, π). Equivalently, at elapsed time t  T ,
the optimal policy purchases whenever Pt  b(T  t, πt).
Proposition 3 is the Bayesian analog of Proposition 1 . Learning enlarges the state from the current
price to the pair (p, π), but conditional on the belief, the current price affects the pre-adjustment
decision only through the surplus from buying now. An adjustment both changes the price and
updates the posterior through Φ, so an observed price adjustment can shift the threshold used for
subsequent decisions. Figure 5 illustrates this belief-dependent updating: the purchase threshold is
re-evaluated as the posterior state changes, rather than following a fixed threshold path.
Figure 5 Two belief-dependent dynamic purchase thresholds as functions of time, together with corresponding
illustrative sample paths of the posted price.
0 2 4 6 8 10
Time t
0
20
40
60
80
100
120
140Price / Threshold
threshold path 1
price path 1
threshold path 2
price path 2

17
5.2.2. Comparative Statics. The threshold structure also makes the comparative statics pos-
sible. Holding the current belief fixed, the arrival rate still governs how often the agent expects
new opportunities to arrive, while the valuation scales the payoff from purchasing. The next result
demonstrates the corresponding monotonicity of the Bayesian threshold.
Proposition 4 (Bayesian Threshold Monotonicity). The optimal belief-dependent
threshold b(s, π; λ, v) satisfies the following monotonicity properties.
(i) b(s, π; λ, v) is non-increasing in λ: if λ1  λ2, then b(s, π; λ2, v)  b(s, π; λ1, v).
(ii) b(s, π; λ, v) is non-decreasing in v: if v1  v2, then b(s, π; λ, v1)  b(s, π; λ, v2).
We now consider how the threshold changes as the belief becomes more pessimistic. To formalize
this comparison, we need an order on posterior beliefs that is compatible with both predictive price
distributions and Bayesian updating. The following monotone-information condition provides such
an order for one-dimensional distributions.
Definition 1 (Monotone Likelihood-Ratio Order). Let F1 and F2 be distributions on an
ordered set X  R, and suppose they admit densities f1 and f2 with respect to a common dominating
measure. We write F1 MLR F2 if, for every x1 < x2, f2(x2)f1(x1)  f2(x1)f1(x2). We use the same
notation for price distributions on P and for beliefs on the ordered parameter space Θ.
Assumption 2 (Monotone Likelihood-Ratio). The parameter space is an ordered subset
Θ  R. Each Hθ admits a density hθ with respect to a common dominating measure on P. For every
θ1 < θ2, Hθ1 MLR Hθ2.
Assumption 2 is a natural monotone-information condition. It states that higher values of the
latent parameter θ shift the price distribution toward higher prices in a likelihood-ratio sense. Since
MLR order is stronger than first-order stochastic dominance ( Milgrom 1981), a higher θ makes higher
price realizations more likely. In economic terms, θ indexes the “costliness” of the seller’s pricing
regime. A higher θ corresponds to a seller that tends to post higher prices, perhaps due to stronger
demand conditions, lower competitive pressure, or more conservative markdown policies.
The MLR structure also ensures that observed prices are informative about θ in an order-preserving
way: a high observed price is a signal that θ is likely high, and vice versa. This is the informational
regularity that makes the posterior behave monotonically, as the next lemma establishes.
Lemma 2. Under Assumption 2, the following properties hold:
(i) If π1 FSD π2, then ¯Hπ1 FSD ¯Hπ2.
(ii) For every observed price p for which both posteriors are defined and π1 MLR π2, Φ(π1, p) MLR
Φ(π2, p).

18
(iii) More generally, if π1 MLR π2 and p1  p2, then Φ(π1, p1) MLR Φ(π2, p2) whenever both pos-
teriors are defined. In particular, for every prior π and prices p1  p2, Φ(π, p1) MLR Φ(π, p2)
whenever both posteriors are defined.
Lemma 2 establishes the monotonicity properties used in the Bayesian comparative statics. Part (i)
links beliefs to predictive price distributions: if π2 places relatively more weight on high- θ regimes
than π1, then the predictive distribution under π2 first-order stochastically dominates that under π1.
Part (ii) shows that this belief ordering is preserved under Bayesian updating, so a more pessimistic
prior leads to a more pessimistic posterior after the same price observation. Part (iii) adds a cross-
monotonicity property: a more pessimistic prior combined with a higher observed price leads to a
more pessimistic posterior. Together, these properties ensure that the ordering on P(Θ) is compatible
with the dynamic program, which enables the comparative statics in Proposition 5 .
Proposition 5 (Belief Monotonicity of the Bayesian Threshold). Under the
Bayesian learning model and Assumption 2 , if π1 MLR π2, then
(i) The Bayesian value satisfies V B(s, p, π1)  V B(s, p, π2) for all (s, p).
(ii) The belief-dependent threshold satisfies b(s, π1)  b(s, π2) for all s.
Proposition 5 identifies how posterior pessimism changes stopping incentives. In this buying prob-
lem, a pessimistic belief lowers the option value of future adjustments, making buying at the current
price relatively more attractive and raising the purchase threshold. A realized price adjustment affects
the buy-or-wait decision in two ways. First, the newly observed price determines the immediate
surplus, which is then compared with the threshold. Second, as a signal, the same price updates
the posterior belief that determines the threshold. Under the MLR condition, a higher observed
price shifts the posterior belief toward higher values of θ, induces a stochastically higher predictive
distribution for future prices, and thereby raises the threshold.
5.2.3. Information Gap. We now quantify the payoff loss due to uncertainty about which
price-adjustment distribution governs future price adjustments. Let V θ(s, p) denote the oracle value
function when the true price-adjustment distribution Hθ is known, and let V B(s, p, π) denote the
Bayesian value function under posterior belief π. The information gap
G(T, ˆπ) := E˜θ∼ˆπ
h
EP ∼H ˜θ
h
V
˜θ(T, P )  V B(T, P, Φ(ˆπ, P )) ii
measures the expected loss from acting under posterior uncertainty rather than full knowledge.
Lemma 3 (Short-Window Information Gap). Under the Bayesian learning model, for every
prior ˆπ and every T  0, 0  G(T, ˆπ)  v(1  e−λT )  vλT .

19
The intuition behind Lemma 3 is that when the shopping window is short, a price adjustment is
unlikely to occur, so even an oracle with full knowledge of the price-adjustment distribution has little
opportunity to improve on immediate purchase when the valuation is no less than the current price.
For long shopping windows, we impose the following regularity assumption.
Assumption 3. The parameter space Θ = [ θ, ¯θ]  R is a compact interval. Each Hθ admits a
density hθ, and the following conditions hold.
(i) Lower-tail support. There exist common constants c > 0, α > 0, and ε > 0, and a lower endpoint
pθ L  0 for each θ, such that v > pθ L, Hθ([0, pθ L)) = 0, and Hθ([pθ L, pθ L+x])  c xα for all x 2 [0, ε].
(ii) Distributional Lipschitz continuity. There exists L < 1 such that for all θ, θ′ 2 Θ,
W∞(Hθ, Hθ′)  Ljθ  θ′j. For one-dimensional price distributions, we use W∞ to denote the
infinity-Wasserstein distance.
(iii) Posterior regularity. There exist constants a0, a1 > 0 satisfying the following conditions. First, the
prior ˆπ has a strictly positive C 2 density on the relative interior of Θ and satisfies ∂2 θ log ˆπ(θ) 
a0 there. Second, for every price x, the effective parameter set Θ(x) := fθ 2 Θ : hθ(x) > 0g is
an interval. On the relative interior of Θ(x), the map θ 7! log hθ(x) is twice differentiable and
satisfies ∂2 θ log hθ(x)  a1.
Assumption 3 supports the long-window bound in three ways. First, the lower-tail condition ensures
that, with many adjustment opportunities left, the oracle threshold is close to the lowest attain-
able price, so setting aside time for learning is not too costly. Second, the W∞-Lipschitz condition
makes the oracle threshold stable under small changes in θ. Third, the likelihood and prior are suf-
ficiently curved in the parameter, so observed price adjustments concentrate the posterior at the
usual parametric rate. To gain intuition, in a Gaussian location family Yi j θ  N (θ, σ2), each post-
adjustment price adds 1/σ2 units of precision, so the posterior standard deviation shrinks at rate
n−1/2. Assumption 3(iii) imposes the analogous curvature requirement for the general family.
Next, we present a long-window bound under a learn-then-act policy. Because this policy is feasible,
its payoff gives a lower bound on the Bayesian value V B. The policy reserves a portion of the window
for passive learning, during which it observes post-adjustment prices, updates the posterior, and
forms a confidence set for the unknown price-adjustment distribution. It then switches to an acting
phase and follows an upper-envelope threshold: the largest oracle threshold over parameters that
remain statistically plausible. With high probability, the true parameter lies in the confidence set,
and the upper-envelope threshold is weakly above the true oracle threshold at every remaining time,
so the policy stops no later than the oracle along every realized continuation path. The analysis then
separates the information gap into two terms: the opportunity cost of reserving time for learning and
the acting-phase loss from using a confidence-envelope threshold rather than the true oracle threshold.

20
The regularity assumptions control these terms through lower-tail mass, Lipschitz continuity of the
oracle thresholds, and posterior concentration.
Proposition 6 (Long-Window Information Gap). Suppose Assumption 3 holds. Then
there exists a constant C < 1 such that, for every T  1,
G(T, ˆπ)  C

T −1/α +
r
log(eT )
T
!
,
and hence G(T, ˆπ) ! 0 as T ! 1.
The bound reflects two forces. A longer learning phase provides the agent with price adjustments
and reduces posterior uncertainty, thereby reducing the loss from using an estimated threshold during
the acting phase. At the same time, delaying action is costly because the agent may miss buying
opportunities. The learn-then-act policy balances these effects: the lower-tail condition controls the
cost of postponing purchase, while posterior concentration controls the error in the acting phase.
Thus, the information gap is bounded by a learning-delay term T −1/α and a posterior-uncertainty
term
p
log(eT )/T .
The short- and long-window bounds identifies the horizons in which model uncertainty can mat-
ter most. In short windows, adjustments are unlikely to occur, so the value of knowing the price-
adjustment distribution is limited. In long windows, adjustments make the latent regime learnable
while leaving enough time to use the learned policy. Between these two extremes, model uncertainty
can be more consequential: the agent may observe enough price adjustments for beliefs to affect the
stopping rule, but not enough to resolve the latent state before the opportunity expires.
5.3. Extension: Learning the Trend
The same learning logic can also accommodate deterministic trends in price adjustments. Concretely,
suppose that when a price adjustment occurs at elapsed time t, the post-adjustment price has the
form gη(t) +Xθ, where gη is a parametric trend function indexed by η 2 H and Xθ  Hθ is a residual
price component indexed by θ 2 Θ. The joint latent state is therefore ξ := (η, θ) 2 Ξ := H  Θ, with
prior belief π 2 P (Ξ). Price adjustment times still follow the Poisson process with arrival rate λ,
while post-adjustment prices are drawn from the shifted distribution gη(t) + Hθ.
Posterior updating is likewise joint. Let hθ denote the density associated with Hθ. If the agent
observes a post-adjustment price p at elapsed time t, then each candidate pair (η, θ) assigns likelihood
hθ

p  gη(t)

, so Bayes’ rule updates the joint belief over trend and residual regime simultaneously.
Intuitively, the agent uses the timing pattern of observed prices to learn whether prices are drifting
upward or downward over the window, and uses detrended residuals to learn whether the seller’s
pricing regime is systematically aggressive or conservative.

21
The threshold structure carries over by the same monotonicity argument as in Proposition 3 . For
each time-to-go and joint posterior, the buy region in the current price remains a lower interval.
Trend learning changes the predictive price-adjustment distribution and the belief state, but not the
threshold form of the stopping rule.
This joint-learning formulation remains conceptually close to the baseline Bayesian model because,
after writing s = T  t, the dynamic-programming state remains (s, p, π), with elapsed time entering
the distribution of the post-adjustment price through T  s. The belief’s domain expands from Θ to
Ξ. The main cost is computational rather than conceptual: the posterior now evolves over a higher-
dimensional parameter space, and the purchase threshold depends on beliefs about both the trend
and the residual noise. For this reason, the extension is most attractive when the trend family is low-
dimensional. A fully nonparametric trend specification would substantially enlarge the state space
and would likely require a separate approximation method.
6. Robust Buying Under Minimal Information
The previous two sections rely on a probabilistic adjustment model of future prices. The Bayesian
model relaxes assumptions about the price-adjustment distribution, but it still assumes that the
timing of price changes follows a Poisson process. In some applications, however, price histories may
be short, market conditions may shift abruptly, or seller behavior may be too unstable to support such
a structure. These considerations motivate a robust OR model that drops the Poisson, independence,
and stationarity assumptions from the adjustment models above and asks what guarantees remain
when the agent trusts only coarse price information.
In this section, we work directly with realized price paths in elapsed time t 2 [0, T]. The analysis
is model-free: no stochastic model is imposed on the price path’s evolution. Prices may change
irregularly or even in an adversarial manner. The only assumption we impose is that the realized
price path p : [0, T] ! [pL, pU ] is bounded, with 0  pL  p0  pU .
The buying agent observes the path sequentially and must decide online whether and when to
purchase. As in the earlier sections, the agent has valuation v, but now the only trusted market
information consists of the observed price history, the known bounds (pL, pU ), and the initial price
p0. Throughout this section, we focus on the nondegenerate case v > p L. If v  pL, every feasible
price is weakly above the valuation, so OPT(p) = 0 for all paths and the competitive-ratio problem
is trivial.
6.1. Online Policy and Benchmark
An online policy A chooses a purchase time τ A 2 [0, T] [ f1g, expressed in elapsed-time units, based
only on the observed portion of the price path. If the agent purchases by the deadline, its payoff
under path p() is
U A(p) =  v  p(τ A) + .

22
If no purchase occurs by the deadline, the payoff is zero.
To evaluate the quality of an online buying policy, we compare it with an offline benchmark that
observes the entire realized price path in advance. The offline value is
OPT(p) = sup
t∈[0,T ]

v  p(t)
+
.
This benchmark represents the best possible purchase timing decision. The performance criterion is
the competitive ratio
CR(A) = inf
p(·)
E[U A(p)]
OPT(p) ,
with the usual convention that the ratio equals 1 when OPT(p) = 0 . The expectation is over the
internal randomization of the policy, if randomization is allowed. This multiplicative criterion asks
what fraction of the offline surplus can be guaranteed uniformly over all feasible price paths. We later
complement it with minimax regret, which evaluates the absolute surplus loss relative to the same
offline benchmark.
6.2. Worst-Case Price Trajectories
To derive performance limits, it is enough to consider a simple subclass of feasible paths. The adver-
sary can let the price decline gradually, making waiting attractive, while retaining the ability to end
the markdown and revert to a high price at an unknown time. This creates the central online tension:
buying early sacrifices possible future savings, but waiting long risks missing a sale.
Definition 2 (Flash-Sale Process). A flash-sale process is characterized by a pair (ˆp, σ) con-
sisting of:
(i) A skimming trajectory ˆp : [t1, t2] ! [pL, pU ], which is a continuous linear 1 function with ˆp(t1) = p0
and ˆp(t2) = pL, representing the posted price while the sale is active;
(ii) An end-sale time σ, which is a random variable supported on [t1, t2], representing the random
instant at which the sale terminates;
Conditional on a realization of σ, the realized price path is
p(t) =
8
><
>:
p0, t 2 [0, t1),
ˆp(t) = p0  p0−pL t2−t1 (t  t1), t 2 [t1, σ),
pU , t 2 [σ, T].
The agent observes p(t) sequentially. At each instant t < σ, the observed price p(t) = ˆp(t) is consistent
with the sale still being active, but the agent does not know the realization of σ before the sale ends
and cannot distinguish “the sale continues” from “the sale will end soon. ” Once the price jumps to
the reversion price pU at time σ, the agent learns that the sale has ended.
1 A linear trajectory is not essential; rather, any continuous decreasing trajectory is admissible. We adopt a linear
function for analytical convenience.

23
For each realized end-sale time, the offline optimum under the corresponding price path is
OPT(p) =

v  ˆp(σ−) + =  v  ˆp(σ) + ,
since ˆp is non-increasing and the best achievable price is the last sale price ˆp(σ−) just before expiry.
An online policy that has not made a purchase by time σ faces the reversion price pU for the remainder
of the horizon.
6.3. Randomized Threshold Policies
Definition 3 (Random Purchase Threshold Policy). A random purchase threshold pol-
icy is an online policy that draws a random threshold b from a distribution on [pL, pU ] at time 0,
before observing the future price path, and then keeps this threshold fixed until the deadline. Given
the realized threshold b, the policy uses the static threshold before the deadline and defines
τb = inff t 2 [0, T) : p(t)  b g,
with the convention that τb = 1 if the set is empty. If τb < 1, the policy purchases at τb. If no
such crossing occurs before the deadline, the policy applies the terminal valuation rule at time T : it
purchases if and only if p(T )  v.
Equivalently, the policy is fully characterized by a distribution over thresholds together with the
terminal action. Conditional on the draw of b, the agent follows the corresponding deterministic static
threshold rule on [0, T).
Figure 6 Two sampled randomized thresholds and price trajectories.
0 2 4 6 8 10
Time t
20
40
60
80
100
120
140
160Price / Threshold
sale window
b1
b2
p0
pU
pL
threshold b1
threshold b2
price path 1
price path 2
buy
σ1
buy
σ2

24
6.4. Competitive Ratio
We first characterize the optimal competitive ratio CR∗. The expression depends on how the con-
sumer’s valuation compares with the initial price and the upper price bound, because these compar-
isons determine both the value of buying immediately and the consequence of missing a temporary
markdown. To characterize CR∗, we define ρ(v) as follows.
If pL < v  p0, set ρ(v) = 0. If p0 < v  pU , set
ρ(v) := 1
1 + log

v−pL
v−p0
 .
If v > pU , let x0 denote the unique solution to x v−pU + log x = log(pU  pL)  1 and set
ρ(v) :=
8
>>><
>>>:
v  pU
x0 + v  pU
, x0  pU  p0,
v  p0
v  p0 + (pU  p0) log

pU −pL
pU −p0
 , x 0 < pU  p0.
Proposition 7 (Optimal Competitive Ratio). For v > pL, the optimal competitive ratio is
CR∗ = ρ(v). Moreover, for v > p0, the ratio is achieved by a randomized threshold policy.
The proof proceeds by establishing matching upper and lower bounds. The upper bound constructs
flash-sale processes under which no online policy can earn more than a ρ(v) fraction of the offline
payoff. The lower bound constructs randomized threshold policies that guarantee ρ(v) against every
feasible path. The upper-bound construction is related to the equalizing distributions used in online
booking ( Ball and Queyranne 2009), but the mathematical primitives differ. In the online-booking
model, the adversary distribution is governed by a single fare bound. In our buying model, three
price primitives matter: the initial price p0, the lower price bound pL, and the upper price bound pU .
Moreover, missing the markdown has different consequences depending on whether v  pU or v > pU ,
which is why ρ(v) has valuation-dependent regimes rather than reducing directly to the competitive
ratio in Ball and Queyranne (2009).
Lemma 4 (Flash-Sale Upper Bound). For every online policy A, CR(A)  ρ(v). Specifically,
the upper bound is witnessed by the following flash-sale process. For the nondegenerate case p0 > pL,
fix a reference time ˜t on the sale trajectory and write q := ˆp(˜t). The sale remains active until ˜t, and
the random end-sale time after ˜t has distribution
P [σ  t] =
8
>>>><
>>>>:
0, t1  t < ˜t,
(p0  pL)(t  ˜t)
A(t2  t1) + (p0  pL)(t  ˜t) , ˜t  t < t2,
1, t = t2.
(5)
The regime-specific choices are:

25
(i) If pL < v  p0, take q = v  ε and A = ε; the resulting upper bound tends to zero as ε # 0.
(ii) If p0 < v  pU , take q = p0 and A = v  p0.
(iii) If v > pU and x0 < pU  p0, take q = p0 and A = pU  p0.
(iv) If v > pU and x0  pU  p0, take q = pU  x0 and A = x0.
Under these distributions, any deterministic online rule can be viewed as choosing a target mark-
down. The induced markdown-depth distribution equalizes the online payoff across target mark-
downs, while the offline oracle captures the final sale price just before expiry. The proof applies Yao’s
principle and computes the resulting expected payoff ratios.
The matching lower bound is constructive: a randomized static threshold, with distribution chosen
by valuation regime, balances the potential gain from waiting for lower prices against the risk of
missing the eventual best price.
Lemma 5 (Robustly Optimal Randomized Threshold Policies). There exists a ran-
domized threshold policy whose competitive ratio is at least ρ(v). The policy draws a random threshold
b before the price path is revealed, and purchases at the first pre-deadline time when the observed price
falls to or below b. If the threshold is not reached before the deadline, the policy applies the terminal
valuation rule at T , purchasing if and only if p(T )  v.
For pL < v  p0, the claim is immediate because ρ(v) = 0. For v > p 0, write a := minfv, pU g and
define
c(v) :=
8
><
>:
p0, p0 < v  pU ,
p0, v > pU and x0 < pU  p0,
pU  x0, v > p U and x0  pU  p0.
Draw b from the distribution
Fb(z) :=
8
>>><
>>>:
0, z < pL,
ρ(v) log
 a  pL
a  z

, p L  z < c(v),
1, z  c(v).
This policy achieves a competitive ratio of ρ(v).
Together, Lemmas 4 and 5 imply CR∗  ρ(v) and CR∗  ρ(v), respectively, and therefore prove
Proposition 7 . The zero guarantee for pL < v  p0 reflects the multiplicative nature of competitive
analysis: the initial price yields no positive surplus, and an adversary can make any attractive mark-
down arbitrarily small. The payoff ratio can therefore collapse even when the absolute loss remains
meaningful. This motivates the minimax regret criterion below.

26
6.5. Minimax Regret
In this subsection, we introduce and characterize minimax regret under the same primitives. This
additive criterion compares the online payoff to the same offline benchmark in terms of a surplus
value, rather than as a payoff ratio.
For a price path p() and an online policy A with purchase time τ A, the regret of policy A against
path p is
Reg(A, p) = OPT(p)  E

U A(p)  .
The associated minimax regret is
Reg∗ = inf
A
sup
p(·)
Reg(A, p),
where the infimum is over all possibly randomized online policies and the supremum is over all feasible
price paths in [pL, pU ].
For v > p L, write a := minfv, pU g, γ := minfp0, a  (a  pL)/eg, and ∆ := a  γ. We will show
that the minimax regret is
¯R(v) := ∆ log a  pL
∆ .
Proposition 8 (Minimax Regret). For v > pL, the minimax regret is Reg∗ = ¯R(v). Moreover,
the robustly optimal policy is a randomized threshold policy.
The proof again proceeds by establishing matching upper and lower bounds. The lower bound
constructs flash-sale distributions under which every online policy incurs regret at least ¯R(v). The
upper bound constructs randomized threshold policies whose worst-case regret is at most ¯R(v).
Lemma 6 (Adversarial Regret Lower Bound). For every online policy A,
sup
p(·)
Reg(A, p)  ¯R(v).
The lower bound is witnessed by the following flash-sale process. With a, γ, and ∆ as defined above,
fix a skimming trajectory ˆp and a reference time ˜tR such that ˆp(˜tR) = γ. The sale remains active until
˜tR, and the end-sale time after ˜tR is chosen according to
P [σ  t] =
8
>>>><
>>>>:
0, t1  t < ˜tR,
(p0  pL)(t  ˜tR)
∆(t2  t1) + (p0  pL)(t  ˜tR) , ˜tR  t < t2,
1, t = t2.
The realized path follows ˆp until σ and then jumps to pU .

27
Lemma 7 (Achievable Regret Bound). There exists a randomized static threshold policy A
such that
sup
p(·)
Reg(A, p)  ¯R(v).
The policy is constructed as follows. If pL < v  p0, set ¯p := v  (v  pL)/e and draw b with density
1/(v  b) on [pL, ¯p].
If v > p0, let La := log((a  pL)/(a  p0)), with the convention that La = +1 when a = p0. When
La  1, draw b with density 1/(a  b) on [pL, p0) and put an atom 1  La at p0. When La > 1, set
¯pa := a  (a  pL)/e and draw b with density 1/(a  b) on [pL, ¯pa]. In all regimes, the drawn threshold
governs purchases only on [0, T); if it is not reached before the deadline, the policy buys at T if and
only if p(T )  v.
Together, Lemmas 6 and 7 imply Reg∗  ¯R(v) and Reg∗  ¯R(v), respectively, and therefore prove
Proposition 8 .
6.6. Extension: Decreasing Price Trend
The robust construction also applies when the trusted price information takes the form of decreasing
price envelopes rather than constant bounds. Suppose the agent knows two non-increasing functions
pL() and pU () such that every feasible price path satisfies pL(t)  p(t)  pU (t), t 2 [0, T], with
p(0) = p0. This specification captures settings in which prices are expected to move downward over
the shopping window, but the realized path may still fluctuate within a time-varying band. The
terminal lower envelope pL(T ) is the lowest price that the adversary can make available, while the
terminal upper envelope pU (T ) is the worst price the agent must face if it waits until the deadline.
Thus, the decreasing-trend problem reduces to the constant-bound problem with the effective
primitives peﬀ L := pL(T ), peﬀ U := pU (T ), peﬀ 0 := minfp0, pU (T )g. The effective initial price reflects the
fact that the agent can always wait until the deadline and face a price no higher than pU (T ).
The randomized threshold policies and the competitive-ratio and minimax-regret expressions above
therefore carry over after replacing (pL, pU , p0) by (peﬀ L , peﬀ U , peﬀ 0 ). Operationally, the agent draws a
static price threshold from the same distribution as in the constant-bound model, calibrated to the
terminal band, and makes a purchase the first time the realized price falls to or below that threshold
before the deadline. If the threshold is not reached before the deadline, the agent applies the terminal
valuation rule at T , buying if and only if p(T )  v. The guarantee uses peﬀ U to bound the missed-
threshold continuation payoff. Section EC.4 explains how the adversarial and achievability arguments
map to this envelope formulation.

28
7. Empirical Evaluation of Buying-Agent Policies
This section evaluates a set of buying policies, including our OR policies and several comparison
policies, using real price histories. We construct 1,000 shopping instances from posted-price histories
of 367 items on Amazon. We use prior observations to estimate parameters and choose among candi-
date models, and reserve the subsequent price path for sequential evaluation. In the remainder of this
section, we first describe the construction of the evaluation instances, then introduce the evaluated
policies and selection mechanisms, report their surplus performance, and finally illustrate the agent
workflow on a common shopping instance.
7.1. Instance Construction
We construct the evaluation instances from time-stamped posted-price histories from Keepa, an
Amazon price-tracking service. The final evaluation set contains 1,000 shopping instances spanning
367 items, with underlying records that include 48,933 time-stamped price observations. To form
the instance pool, we randomly sample 3 shopping windows per item and 3 valuations per window,
discarding windows with no in-window price change, and then randomly select 1,000 instances.
For each instance, we split the price path into a pre-window history and a held-out 30-day shop-
ping window. The pre-window history is the only price information available for calibration, model
selection, and language-model prompts at the beginning of the shopping window. During evaluation,
each policy observes shopping-window prices only sequentially as they become available. The full
held-out path is reserved for ex-post computation of the offline benchmark.
We require each selected instance to have at least five pre-window price observations for parameter
calibration. We also require at least two shopping-window observations, counting the window-start
price, to ensure a non-trivial sequential decision problem. When the price is not observed exactly at
the window start, the window-start price is taken to be the last posted price before the window begins.
The consumer valuation is generated as a multiple of the window-start price, with the multiplier
drawn uniformly from [1.01, 1.50].
7.2. Candidate Policies and Selection
This subsection defines the decision mechanisms evaluated in the numerical study.
Fixed OR policies. The Fixed OR policies apply a common stopping-rule specification to all
instances, but calibrate the model inputs separately using each instance’s pre-window price history.
We evaluate four such policies: Stationary, Bayesian, Robust, and Trend-aware. Stationary is an
implementation of the stationary model in Section 4: it estimates the adjustment intensity and price-
adjustment distribution from the pre-window history and solves the model’s threshold equation.
Bayesian implements the Bayesian learning model in Section 5 , using the same adjustment-intensity

29
estimate and a discretized Bayesian predictive model for uncertainty in the price-adjustment distri-
bution; prior counts are initialized from pre-window prices and updated as shopping-window prices
are observed. Robust implements the robust buying model in Section 6 : it constructs feasible lower
and upper price bounds from the pre-window history and the window-start price, and applies the
model’s randomized threshold policy. Trend-aware implements the time-varying price-adjustment
extension in Section 4.3: it fits a deterministic price trend on the pre-window history and applies the
stopping computation to detrended residual prices. Section EC.1 reports the calibration details.
Heuristic Selector. We also evaluate a Heuristic Selector, which implements model selection
through a sequence of pre-specified diagnostic screens and serves as a simple rule-based benchmark for
automated policy selection. The selector uses only the pre-window history to assign each instance to
one of the candidate OR policies: Stationary, Bayesian, Robust, or Trend-aware. It applies the screens
sequentially. The selector first checks the stability of the adjustment intensity and routes histories
with unreliable timing to Robust. Then it applies a multiple-break screen for level shifts in pre-window
prices, in the spirit of Bai and Perron (1998, 2003), and a linear-trend screen. Among non-trending
histories, unexplained level shifts trigger Robust; otherwise, suﬀiciently long histories are routed to
Stationary, and shorter histories to Bayesian. Among trending histories, the selector detrends the
prices and then reapplies the level-shift screen to the residuals; stable residuals yield Trend-aware,
while unstable residuals yield Robust. The screening details are reported in Section EC.2 , and the
diagnostic cutoffs used in the reported run are fixed across instances.
Language-model agents. The third benchmark group consists of two language-model agents: LLM-
baseline and LLM-OR. In the reported implementation, both agents call the DeepSeek API with
the deepseek-v4-flash model. LLM-baseline is a direct-prompting agent. At the beginning of each
shopping instance, the LLM receives the decision context, including the pre-window price history,
valuation, and deadline. In a live deployment, the agent operates alongside an automatic price-
monitoring program that calls the LLM at the start of the shopping window and after every price
change. When queried at time t, the LLM receives the conversation history of this shopping task, the
current price Pt, and the remaining time T  t. It then chooses either to purchase immediately or
to wait and schedule a future purchase time ξ 2 (t, T]. If the price remains unchanged before ξ, the
purchase is triggered. Otherwise, if a new price P˜t arrives at ˜t < ξ, the LLM is re-queried with the
updated price P˜t and the new remaining time T  ˜t appended to the ongoing conversation history. 2
In our numerical study, rather than using a live price monitor, we emulate this process on held-out
historical price paths. The simulation directly compares the scheduled purchase time ξ with the next
2 We do not query the LLM continuously. Suppose each query independently carries a positive probability of recom-
mending a purchase; then, highly frequent querying would increase the chance that a purchase is triggered early. The
scheduled purchase time thus serves as a commitment device for more disciplined execution.

30
price-adjustment time ˜t to decide whether to purchase or to query the LLM again. LLM-OR uses the
language model at the beginning of the shopping window to select an OR model and the calibration
samples, that is, the subset of pre-window price observations used to estimate the model inputs.
Specifically, the LLM chooses a lookback horizon and a maximum number of recent price observations
to use. The selected OR model then computes the threshold policy for making buy-or-wait decisions
along the realized price path.
Simple baselines. We also include several simple policies that do not use our OR policies. The first
group consists of two naive rules: Buy Now, which buys immediately when the initial price is no
greater than the valuation, and Buy Last, which waits until the deadline and buys only if the last
price is no greater than the valuation. The second group consists of three historical-price heuristics:
Historical Mean, Historical Median, and Historical Min, which buy once the current price falls to or
below the corresponding historical benchmark. If no purchase is triggered before the deadline, these
waiting policies make a terminal purchase only when the last observed price is at most the valuation.
7.3. Performance Measures and Results
Consistent with the payoff convention in Section 3 , we measure performance by realized consumer
surplus: (v  pτ )+ for a purchase at time τ with price pτ , and zero if no purchase is made. To compare
outcomes across products with different price and valuation scales, we use normalized surplus, defined
as realized surplus divided by the ex-post optimal surplus in the same shopping window whenever
the latter is positive. When the offline best surplus is 0, we simply set the normalized surplus to 1.
The offline best price is used only for ex-post evaluation. All methods are evaluated independently
on the same set of shopping instances for comparability.
Table 2 reports the two rate-based measures. The win rate is tie-aware and measures relative
performance: any method that achieves the highest normalized surplus among all evaluated methods
on an instance earns a win (i.e., if multiple methods tie for the best performance in the evaluated
pool, all receive a win, hence the sum of win rates may exceed one). The optimal-hit rate counts
instances on which a method attains the ex-post optimal surplus (i.e., buying at the lowest price
along the whole shopping window, rather than merely outperforming other methods). The table
shows a tight leading group on these measures: LLM-OR, Bayesian, Stationary, and Historical Min
all attain win rates above 48% and optimal-hit rates of at least 43%. LLM-OR belongs to this group,
with a win rate of 48.9% and an optimal-hit rate of 44.1%, indicating that language-model-assisted
model selection can recover competitive stopping decisions when the selected OR policy controls
purchase timing. The Stationary policy remains competitive despite its restrictive price-adjustment
assumption, suggesting that a calibrated threshold rule captures much of the value of waiting in these
instances.

31
Table 2 Win Rates Across 1,000 Instances. Win rate is tie-aware and counts all methods attaining the
instance-level maximum surplus. Opt. hit rate counts instances with zero regret relative to the offline best surplus.
Method Policy type Win rate Opt. hit rate
LLM-OR LLM-agent 48.9% 44.1%
Stationary Fixed OR 48.3% 43.2%
Bayesian Fixed OR 48.3% 43.1%
Historical Min Simple baseline 48.1% 43.0%
LLM-baseline LLM-agent 46.8% 40.4%
Buy Last Simple baseline 44.9% 40.9%
Trend-aware Fixed OR 43.9% 38.8%
Historical Median Simple baseline 43.6% 38.5%
Historical Mean Simple baseline 43.4% 38.6%
Buy Now Simple baseline 30.4% 25.8%
Heuristic Selector Heuristic selector 26.5% 21.6%
Robust Fixed OR 21.9% 17.6%
Figure 7 complements the rate-based comparison in Table 2 by showing the cross-instance distri-
bution of normalized surplus. Because normalized surplus is measured relative to the ex-post optimal
surplus in the same instance, values near one indicate decisions that nearly match the offline bench-
mark. The leading methods are close over much of the distribution, but their quantile performance
differs more substantially. For example, Historical Min and Buy Last score well on optimal-hit rates,
a pattern consistent with instances in which the lowest observed price occurs near an endpoint of the
shopping window, but their lower tails are weaker. By contrast, Robust and Heuristic Selector have
lower win rates but stronger 10th-percentile normalized surplus than the methods with the highest
win and optimal-hit rates, reflecting more conservative downside protection. These contrasts suggest
that policy quality depends not only on how often a rule attains an ex-post hit, but also on how it
trades off hit frequency against tail risk. The gap between Heuristic Selector and the strongest fixed
policies suggests room for improved selection rules.
7.4. Illustration of Buying-Agent Trace
We conclude the numerical study with an illustrative trace comparing the LLM baseline and LLM-
OR on the same shopping instance. As described in Section 7.2 , LLM-baseline is queried at the
window start and after each price change to make purchase-timing decisions, with any scheduled
action superseded by a new price adjustment. LLM-OR uses the language model to select the OR
model, choose the calibration history, and generate user-facing communication, while the selected
OR policy controls the sequential purchasing decisions along the realized price path.
As part of the implementation diagnostic, we also record token usage. Across the 1,000 instances,
LLM-OR uses 5.26 million total tokens (2.12 million input + 3.14 million output), compared with
21.80 million (19.26 million input + 2.53 million output) for LLM-baseline. This difference comes
from using the OR policy rather than repeated LLM queries.

32
Figure 7 Distribution of normalized surplus across the 1,000 instances. For each method, the light segment
spans the 10th to 90th percentiles, the dark segment spans the interquartile range, the black dot marks the
median, and the orange diamond marks the mean. Methods are sorted by mean normalized surplus.
0.0 0.2 0.4 0.6 0.8 1.0
Normalized surplus
Stationary
LLM-OR
Bayesian
Heuristic selector
Robust
LLM-baseline
Trend-aware
Historical mean
Historical median
Historical min
Buy last
Buy now
P10-P90 P25-P75 P50 Mean
8. Conclusion
We develop a buyer-side operations framework for designing automated buying agents. We formulate
purchase timing as a finite-horizon stopping problem and study how the optimal purchasing policy
changes as the agent’s information about future prices weakens. In the stationary price-adjustment
benchmark, the optimal policy is a dynamic threshold characterized by an ordinary differential equa-
tion. Under Bayesian uncertainty about the price-adjustment distribution, the threshold becomes
belief-dependent, and the information gap quantifies the value of knowing the true price-adjustment
distribution. Under minimal information, randomized threshold policies provide competitive-ratio
and minimax-regret guarantees. Together, these results show how the structure of the purchase pol-
icy changes as the agent moves from a calibrated stochastic model to learning and then to robust
protection.
The numerical study complements the analytical results by applying these policies to real price
histories. The comparison indicates that the OR policies proposed in this paper, especially the Sta-
tionary policy, perform competitively on the evaluation instances. The LLM-OR implementation
illustrates a complementary role for language models in buying-agent design: the LLM can select a
model, choose calibration data, and generate user-facing explanations, while the selected OR policy
retains control of the sequential purchase-timing decision.
Our analysis isolates the purchase-timing decision in a setting with a single item, a known valu-
ation, and an exogenous price path. This abstraction separates the core timing problem from other

33
Figure 8 Decision trace for one evaluation instance. Price panels show pre-window history, shopping-window
prices, and realized purchase outcomes; the LLM-OR panel also highlights the truncated price data chosen by the
LLM and used by the OR policy. Message strips report the corresponding summaries and purchase explanations.
-500 -250 0 10 20 30
Date (normalized)
10
20
30Price
history
valuation $32.75
LLM-Baseline
I W W WW W W W W W P
Initial feedback
day 0 | posted price $23.06 | value $32.75
The current price of $23.06 is below your valuation of $32.75, so it's a good deal. However, historical data
shows that this item often drops to lower prices, sometimes below $10. With 30 days left, you can likely get an
even better price by waiting. If no lower price appears, I'll automatically buy at $23.06 when only 1 day
remains, ensuring you don't miss out.
Repeated wait updates
Waiting for a better price.
Purchase notification
day 29.00 | buy at $23.06 | surplus $9.69
We planned to buy this item when the price hit $23.06. Since the price never changed, we went ahead and
purchased it on day 29, saving you $9.69 off your estimated value.
I
W
P
-500 -250 0 10 20 30
Date (normalized)
10
20
30Price
history
last 180d
computed threshold
valuation $32.75
LLM-OR
WI P
Initial feedback
Stationary | lookback 180 days | 72 events | value $32.75
Based on past price patterns, this item frequently drops to around $12. Since you have 30 days to shop and the
current price is $23.06, we recommend waiting for a better deal. Our strategy will set a target price that
balances the chance of a drop with the risk of missing the deadline, so you can buy at a good value without
waiting too long.
OR algorithm
Stationary stopping rule | buy trigger day 16.81 | threshold price $11.41
The OR policy monitors the realized price against the computed stopping threshold and triggers the purchase
when the rule is met.
Purchase notification
day 16.81 | buy at $11.41 | surplus $21.34
We waited and snagged this item for $11.41—far below its estimated $32.75 value and the current $23.06 price.
By holding out for a price drop, you saved over $21 and got an excellent deal within your 30-day window.
I
W
P
Note: The message excerpts are reproduced directly from the LLM output. The red boxes mark two minor factual
errors in the raw purchase notification: the first should indicate that the price is the same as the initial observed
price, rather than that it never changed; the second should refer to the initial price at the start of monitoring, rather
than to a current price of 23.06.

34
market frictions and allows us to focus on how the agent’s information about future prices shapes
the purchasing policy. It also defines the limits of the current framework and points to several natu-
ral extensions. Relaxing the memoryless price-adjustment assumption yields richer autoregressive or
contextual price dynamics. Relaxing the single-item assumption yields multi-item formulations that
allow substitution across products. Finally, incorporating stock-out risk would make the purchase-
timing decision account for both future prices and product availability.
References
Allouah A, Besbes O, Figueroa JD, Kanoria Y, Kumar A (2025) What is your AI agent buying? Evaluation,
biases, model dependence, and emerging implications for agentic e-commerce. ArXiv:2508.02630v3.
Assunção JL, Meyer RJ (1993) The rational effect of price promotions on sales and consumption. Management
Sci. 39(5):517–535.
A viv Y, Pazgal A (2008) Optimal pricing of seasonal products in the presence of forward-looking consumers.
Manufacturing & Service Oper. Management 10(3):339–359.
Baek J, Fu Y, Ma W, Peng T (2026) AI agents for inventory control: Human-LLM-OR complementarity.
ArXiv:2602.12631v2.
Bai J, Perron P (1998) Estimating and testing linear models with multiple structural changes. Econometrica
47–78.
Bai J, Perron P (2003) Computation and analysis of multiple structural change models. J. Appl. Econom.
18(1):1–22.
Bakos Y (1997) Reducing buyer search costs: Implications for electronic marketplaces. Management Sci.
43(12):1676–1692.
Ball MO, Queyranne M (2009) Toward robust revenue management: Competitive analysis of online booking.
Oper. Res. 57(4):950–963.
Bawa VS (1975) Optimal rules for ordering uncertain prospects. J. Financ. Econ. 2(1):95–121.
Besbes O, Zeevi A (2009) Dynamic pricing without knowing the demand function: Risk bounds and near-
optimal algorithms. Oper. Res. 57(6):1407–1420.
Birge JR, Chen HK, Keskin NB (2025) Markdown policies for demand learning with forward-looking cus-
tomers. Oper. Res. 73(5):2550–2566, URL http://dx.doi.org/10.1287/opre.2019.0402.
Bloomberg Odd Lots (2026) Stripe’s john collison on how agentic commerce will reshape
the internet. Apple Podcasts, URL https://podcasts.apple.com/ca/podcast/
stripes-john-collison-on-how-agentic-commerce-will/id1056200096?i=1000768091736 ,
accessed May 17, 2026.
Borodin A, El-Yaniv R (1998) Online Computation and Competitive Analysis (Cambridge: Cambridge Uni-
versity Press).

35
Brynjolfsson E, Smith MD (2000) Frictionless commerce? A comparison of Internet and conventional retailers.
Management Sci. 46(4):563–585.
Cachon GP, Swinney R (2009) Purchasing, pricing, and quick response in the presence of strategic consumers.
Management Sci. 55(3):497–511.
Calvo GA (1983) Staggered prices in a utility-maximizing framework. J. Monet. Econ. 12(3):383–398.
Cao S, Hu M (2026) A solicit-then-suggest model of agentic purchasing. ArXiv:2603.20972v1.
Cavallo A (2018) Scraped data and sticky prices. Rev. Econ. Stat. 100(1):105–119.
Chen H, Hu M, Wu J (2023) Intertemporal price discrimination via randomized promotions. Manufacturing
& Service Oper. Management 25(3):1176–1194, URL http://dx.doi.org/10.1287/msom.2023.1194.
Chen L, Mislove A, Wilson C (2016a) An empirical analysis of algorithmic pricing on Amazon marketplace.
Proceedings of the 25th International Conference on World Wide Web , 1339–1349 (ACM).
Chen Q, Jasin S, Duenyas I (2016b) Real-time dynamic pricing with minimal and flexible price adjustment.
Management Sci. 62(8):2437–2455, URL http://dx.doi.org/10.1287/mnsc.2015.2238.
den Boer A V (2015) Dynamic pricing and learning: Historical origins, current research, and new directions.
Surveys in Operations Research and Management Science 20(1):1–18.
El-Yaniv R, Fiat A, Karp RM, Turpin G (2001) Optimal search and one-way trading online algorithms.
Algorithmica 30(1):101–139.
Feng Z, Dawande M, Janakiraman G, Qi A (2024) Technical note—dynamic pricing and learning with
discounting. Oper. Res. 72(2):481–492, URL http://dx.doi.org/10.1287/opre.2023.2477.
Golosov M, Lucas RE Jr (2007) Menu costs and Phillips curves. J. Polit. Econ. 115(2):171–199.
Hadar J, Russell WR (1969) Rules for ordering uncertain prospects. Amer. Econ. Rev. 59(1):25–34.
Harrison JM, Keskin NB, Zeevi A (2012) Bayesian dynamic pricing policies: Learning and earning under a
binary prior distribution. Management Sci. 58(3):570–586, URL http://dx.doi.org/10.1287/mnsc.
1110.1426.
He M, Jennings NR, Leung HF (2003) On agent-mediated electronic commerce. IEEE Trans. Knowl. Data
Eng. 15(4):985–1003, URL http://dx.doi.org/10.1109/TKDE.2003.1209014.
Hendel I, Nevo A (2006) Measuring the implications of sales and consumer inventory behavior. Econometrica
74(6):1637–1673.
Karp RM, Vazirani UV, Vazirani VV (1990) An optimal algorithm for on-line bipartite matching. Proceedings
of the Twenty-Second Annual ACM Symposium on Theory of Computing , 352–358 (ACM).
Kephart JO, Greenwald AR (2002) Shopbot economics. Autonomous Agents and Multi-Agent Systems
5(3):255–287.
Keskin NB, Zeevi A (2014) Dynamic pricing with an unknown demand model: Asymptotically optimal
semi-myopic policies. Oper. Res. 62(5):1142–1167.

36
Kumar A, Manshadi V, Tumu A (2026) How much should a conversational recommender system converse?
A vailable at SSRN: https://ssrn.com/abstract=6481459.
Lippman SA, McCall JJ (1976) The economics of job search: A survey. Econ. Inq. 14(3):347–368, part II.
Liu Q, van Ryzin G (2008) Strategic capacity rationing to induce early purchases. Management Sci.
54(6):1115–1131.
Maes P, Guttman RH, Moukas AG (1999) Agents that buy and sell. Commun. ACM 42(3):81–87, URL
http://dx.doi.org/10.1145/295685.295716.
McCall JJ (1970) Economics of information and job search. Q. J. Econ. 84(1):113–126.
McDonald R, Siegel D (1986) The value of waiting to invest. Q. J. Econ. 101(4):707–727.
Mehta A, Saberi A, Vazirani U, Vazirani V (2007) AdWords and generalized online matching. J. ACM.
54(5):22–es.
Mersereau AJ, Zhang D (2012) Markdown pricing with unknown fraction of strategic customers. Manufactur-
ing & Service Oper. Management 14(3):355–370, URL http://dx.doi.org/10.1287/msom.1120.0376.
Milgrom PR (1981) Good news and bad news: Representation theorems and applications. Bell J. Econ.
12(2):380–391.
Moon K, Bimpikis K, Mendelson H (2017) Randomized markdowns and online monitoring. Management
Sci. 64(3):1271–1290, URL http://dx.doi.org/10.1287/mnsc.2016.2661.
Nair H (2007) Intertemporal price discrimination with forward-looking consumers: Application to the US
market for console video-games. Quant. Mark. Econ. 5(3):239–292.
Nakamura E, Steinsson J (2008) Five facts about prices: A reevaluation of menu cost models. Q. J. Econ.
123(4):1415–1464.
OpenAI (2025a) Buy it in chatgpt: Instant checkout and the agentic commerce protocol. URL https:
//openai.com/index/buy-it-in-chatgpt/ , accessed May 17, 2026.
OpenAI (2025b) Introducing ChatGPT agent: Bridging research and action. URL https://openai.com/
index/introducing-chatgpt-agent/ , accessed April 20, 2026.
OpenAI (2025c) Introducing operator. URL https://openai.com/index/introducing-operator/,
accessed April 20, 2026.
Peskir G, Shiryaev A (2006) Optimal Stopping and Free-Boundary Problems (Basel: Birkhäuser).
Rosenfield DB, Shapiro RD, Butler DA (1983) Optimal strategies for selling an asset. Management Sci.
29(9):1051–1061.
Rothschild M (1974) Searching for the lowest price when the distribution of prices is unknown. J. Polit.
Econ. 82(4):689–711.
Shaked M, Shanthikumar JG (2007) Stochastic Orders. Springer Series in Statistics (New York: Springer).

37
Simchi-Levi D, Mellou K, Menache I, Pathuri J (2025) Large language models for supply chain decisions.
ArXiv:2507.21502v1.
Stripe (2025a) Developing an open standard for agentic commerce. URL https://stripe.com/blog/
developing-an-open-standard-for-agentic-commerce , accessed May 17, 2026.
Stripe (2025b) Introducing the agentic commerce suite: A complete solution for selling on AI agents. URL
https://stripe.com/blog/agentic-commerce-suite , accessed May 17, 2026.
Stripe (2026a) Agentic commerce: How AI agents are changing the way businesses buy and sell. URL https:
//stripe.com/en-sg/resources/more/agentic-commerce , accessed May 17, 2026.
Stripe (2026b) Giving agents the ability to pay. URL https://stripe.com/blog/
giving-agents-the-ability-to-pay , accessed May 17, 2026.
Su X (2007) Intertemporal pricing with strategic customer behavior. Management Sci. 53(5):726–741.
Weber M, Kowalkiewicz M, Weking J, Böhm M, Krcmar H (2020) When algorithms go shopping: Analyzing
business models for highly autonomous consumer buying agents. Gronau N, Krasnova H, Pousttchi K,
Heine M, eds., Entwicklungen, Chancen und Herausforderungen der Digitalisierung: Band 1, Proceedings
der 15. Internationalen Tagung Wirtschaftsinformatik 2020 , 1–16 (Potsdam, Germany: Institut für
Wirtschaftsinformatik und Digitale Gesellschaft e.V.).
Williams KR (2022) The welfare effects of dynamic pricing: Evidence from airline markets. Econometrica
90(2):831–858.
Yao S, Chen H, Yang J, Narasimhan K (2022) WebShop: Towards scalable real-world web interaction with
grounded language agents. Adv. Neural Inf. Process. Syst. , volume 35, 20744–20757.
Yao S, Zhao J, Yu D, Du N, Shafran I, Narasimhan K, Cao Y (2023) ReAct: Synergizing reasoning and
acting in language models. International Conference on Learning Representations .
Zhang H, Jasin S (2022) Online learning and optimization of (some) cyclic pricing policies in the presence
of patient customers. Manufacturing & Service Oper. Management 24(2):1165–1182, URL http://dx.
doi.org/10.1287/msom.2021.0979.

ec1
E-Companion for
“Strategic Buying Agents”
EC.1. Details of OR Policies
This section records how the candidate OR policies in Section 7.2 are calibrated from the pre-window
history. For an evaluation instance, let (ti, pi)nh i=1 denote the pre-window price observations, with
times measured relative to the start of the shopping window, and let p0 denote the window-start
price. The held-out shopping-window prices are not used for calibration, except that p0 is part of the
online state faced by every policy at the beginning of the window.
Stationary. The Stationary policy implementation estimates the Poisson adjustment intensity
bλ by the empirical frequency of price-adjustment timestamps over the historical span. The price-
adjustment distribution H is replaced by the empirical distribution
bH = 1 nh
nhX
i=1
δpi.
The policy then solves the stationary threshold ODE in Section 4 with (bλ,bH, v, T ) and makes a
purchase when the current price is no larger than the resulting time-to-go threshold.
Bayesian. The Bayesian policy implementation uses the same adjustment intensity estimate bλ,
but replaces the unknown price-adjustment distribution by a finite Bayesian predictive model. The
implementation discretizes prices into bins scaled to the pre-window price level and places a Dirichlet
prior over the bin probabilities. Pre-window prices initialize the prior counts, and observed price
adjustments during the shopping window update the posterior count vector. The dynamic program is
then solved on this finite belief-state representation to obtain the belief-dependent threshold policy.
Robust. The Robust policy calibrates only price bounds. The lower bound is set by the smallest
price observed in the pre-window history together with p0. For the upper bound, the implementation
screens the pre-window history to remove isolated extremely high prices that are not representative
of the feasible price range for the shopping window, and then uses the upper end of the screened
history, enlarged if needed to include p0. Thus, the robust model is calibrated only on information
available at the start of the shopping window. The resulting primitives (bpL, p0,bpU , v) are substituted
into the randomized robust threshold distribution in Section 6. The numerical evaluation reports the
expected performance of this randomized policy by averaging over its threshold randomization.
Trend-aware. Trend-aware fits the pre-window linear trend
pi = α + βti + εi

ec2
by least squares, forms residual prices xi = pi  (α + βti), and uses the empirical residual distribution
as the price-adjustment distribution around the deterministic trend. The fitted intercept is shifted
to the shopping-window start, the adjustment intensity is set to bλ, and the threshold is computed in
original price units by combining the deterministic trend with the residual continuation calculation.
When the fitted trend is numerically negligible, or the pre-window history is too short to estimate
it, the implementation falls back to Stationary.
EC.2. Heuristic Selector
Heuristic Selector in Section 7.2 maps each pre-window price history to one candidate model. It first
screens the history for evidence about adjustment timing, level shifts, and deterministic trends, and
then routes the instance to Stationary, Bayesian, Trend-aware, or Robust according to the decision
logic described in Section 7.2 . All screening cutoffs are fixed before evaluation and are held constant
across instances.
The timing screen partitions the pre-window observation span into at most five equal-length bins
and computes Pearson’s statistic
X 2 =
KX
j=1
(Nj  ¯n)2
¯n ,
where Nj is the number of observed price-adjustment timestamps in bin j and ¯n =
n/K. The statistic is compared with a χ2 K−1 benchmark using the two-sided p-value pχ =
2 minfPr

χ2 K−1  X 2 , Pr  χ2 K−1  X 2 g. The reported run uses αχ = 0.5 and requires at least 10 pre-
window timestamps for the timing screen. When fewer timestamps are available, the timing screen
is skipped. The number of bins is reduced when needed to keep the expected cell count at least five.
The level-shift screen is Bai–Perron-style ( Bai and Perron 1998, 2003) in the following sense. For
each candidate number of breaks, it fits a piecewise-constant mean model by dynamic programming,
minimizing within-segment squared deviations subject to a minimum segment length. The imple-
mentation allows at most five breaks, requires each segment to contain at least three observations
and, when feasible, at least 10% of the pre-window sample, and selects the number of breaks by BIC.
We use this screen only for routing diagnostics and do not use the estimated break dates for formal
inference. The selector treats the pre-window price sequence as having unexplained level shifts when
the selected number of breaks exceeds the tolerance κ = 1.
The trend screen fits a linear regression of pre-window price on time and flags a trend when the
absolute t-statistic of the slope exceeds 2. If a trend is flagged, the selector applies the same level-shift
screen to detrended residuals. Histories with unreliable timing, unexplained raw breaks, or unstable
detrended residuals are routed to Robust; trending histories with stable residuals are routed to Trend-
aware; and stable non-trending histories are routed to Stationary when the pre-window sample has
at least n0 = 15 observations and to Bayesian otherwise.

ec3
EC.3. Proofs
EC.3.1. Proof of Lemma 1
Proof. Fix s 2 [0, T] and let 0  p1  p2. Couple the two systems on the same probability space
so that they share the same future event times and, at each future event, the same post-adjustment
price draw. Let σ denote the first future event time.
For any admissible stopping time τ , let J(s, p; τ ) denote the expected payoff obtained from the
initial state (s, p) under τ .
Let τ2 be an ε-optimal stopping time for the problem starting from (s, p2), where ε > 0 is arbitrary.
We construct an admissible stopping rule τ1 for the problem starting from (s, p1) as follows: before
the first future event, the agent ignores the fact that the current price is lower and behaves exactly as
under τ2; if τ2 < σ, then set τ1 = τ2; if τ2  σ, then after time σ the two systems have the same time-
to-go and the same posted price, so from that point onward τ1 follows exactly the same continuation
rule as τ2.
Under this construction, if τ2 < σ, then both agents stop before any price change, and hence the
payoff satisfies (v  p1)+  (v  p2)+. If τ2  σ, then from time σ onward the two systems are in the
same state and generate the same continuation payoff. Therefore, the payoff under τ1 is almost surely
no smaller than that under τ2. Taking expectations gives
V (s, p1)  J(s, p1; τ1)  J(s, p2; τ2)  V (s, p2)  ε.
Letting ε # 0 yields V (s, p1)  V (s, p2). Hence V (s, p) is non-increasing in p. Using the same
method, we also have V (s, p2)  V (s, p1)  (p2  p1), hence V (s, p) is 1-Lipschitz with respect to p.
Next fix p and let 0  s1 < s2  T . Starting from state (s2, p), the agent can always ignore the last
s2  s1 units of time-to-go (i.e., move the deadline forward) and then implement an optimal policy for
state (s1, p). This shows V (s2, p)  V (s1, p). Moreover, the extra value from the additional interval
of length s2  s1 can arise only if at least one event occurs during that interval, and the total payoff
is bounded above by v. Hence
0  V (s2, p)  V (s1, p)  v P (N (s2  s1)  1) = v

1  e−λ(s2−s1) .
Thus V (, p) is non-decreasing and continuous in s. In particular, m(s) := EH[V (s, P)] is also con-
tinuous in s. □
EC.3.2. Proof of Proposition 1
Proof. Part (i): Threshold structure. For p 2 [0, v], define the option value of waiting by W (s, p) :=
V (s, p)  (v  p). Because immediate purchase is always feasible, W (s, p)  0 for all p 2 [0, v]. In
addition, for 0  p1  p2  v, we have W (s, p2)  W (s, p1) =

V (s, p2)  V (s, p1)

+ (p2  p1)  0,

ec4
where the inequality follows from the 1-Lipschitz property in Lemma 1. The same Lipschitz property
gives continuity of W (s, ), so W (s, ) is continuous and non-decreasing on [0, v].
At price p = 0, the agent can secure a payoff v by purchasing immediately, and no policy can
generate more than v. Hence V (s, 0) = v and W (s, 0) = 0. By continuity and monotonicity of W (s, ),
the set Ss := fp 2 [0, v] : W (s, p) = 0 g is a nonempty closed interval of the form [0, b(s)] for some
b(s) 2 [0, v]. For p > b(s) the inequality W (s, p) > 0 is strict: if W (s, p) = 0 for some p > b(s), then
p 2 S s, contradicting b(s) = sup Ss. For p > v , immediate purchase yields (v  p)+ = 0 while the
option value of waiting is non-negative, so waiting is always weakly preferred and b(s)  v on the
entire price space.
We adopt the convention of stopping at the threshold p = b(s), so that at each state (s, p) the
optimal action is to purchase if and only if p  b(s). Equivalently, from elapsed time T  s, the
optimal stopping rule is τ ⋆ = infft 2 [T  s, T] : Pt  b(T  t)g.
Part (ii): Boundary identity and ODE. Fix s > 0. The variational inequality ( 2) gives the usual
complementarity conditions for this obstacle problem. At a stopping point, where V (s, p) = (v  p)+,
the HJB residual of the immediate-purchase payoff must be non-positive. This residual is λm(s)
λ(v  p)+. Hence, any stopping point with p  v must satisfy p  v  m(s). In particular, since the
boundary point is included in the stopping region by convention, b(s)  v  m(s). If, instead, no
continuation point can lie strictly below v  m(s). To see this, suppose that p > b(s) and p < v  m(s).
Then p  v and V (s, p) > v  p > m (s). At points where the continuation equation in ( 2) holds,
∂sV (s, p) = λ

m(s)  V (s, p)

< 0, which contradicts the monotonicity of V in time-to-go established
in Lemma 1 . Thus, regular continuation points must satisfy p  v  m(s), and the same inequality
extends to all continuation points by continuity of V and m. Taking p # b(s) gives b(s)  v  m(s).
Combining the two inequalities yields the boundary identity
b(s) = v  m(s), s > 0. (EC.1)
We next derive the ODE. Since V (, p) is Lipschitz in s uniformly in p, differentiation under the
expectation is valid for almost every s > 0, and m′(s) = EH[∂sV (s, P)]. On the stopping region
fP  b(s)g, we have V (s, P) = v  P , so ∂sV (s, P) = 0. On the continuation region fP > b (s)g, the
variational inequality ( 2) implies ∂sV (s, P) = λ

m(s)  V (s, P)

for a.e. s > 0. Therefore m′(s) =
λ EH[(m(s)  V (s, P))1{P >b(s)}].
On fP  b(s)g, the stopping rule is optimal, so V (s, P) = v  P = m(s) + b(s)  P , where the
second equality uses ( EC.1). Hence EH[V (s, P)1{P ≤b(s)}] = m(s) H(b(s)) + EH[(b(s)  P )+]. Since
m(s) = EH[V (s, P)], it follows that EH[V (s, P)1{P >b(s)}] = m(s)(1  H(b(s)))  EH[(b(s)  P )+].
Substituting this expression into the expression for m′(s) and using b(s) = v  m(s) gives
b′(s) = λ EH  (b(s)  P )+ = λ Z b(s)
0
(b(s)  p) H(dp).

ec5
Finally, the terminal condition is immediate. At s = 0, V (0, p) = (v  p)+, so m(0) = EH[(v  P )+].
Therefore,
lim
s↓0
b(s) = v  m(0) = v  EH[(v  P )+] = EH[minfv, P g].
At the exact deadline, the agent purchases if and only if p  v, so b(0) = v.
Part (iii): Monotonicity and convexity of b. Define GH(x) := EH[(x  P )+] for x  0. Then GH(x)  0
for all x, and the ODE established above can be written as b′(s) = λGH(b(s)) for a.e. s > 0. Since
GH  0, we have b′(s)  0 almost everywhere, so b is non-increasing.
Moreover, GH is non-decreasing in x. Because b is non-increasing in s, the composition s 7!
GH(b(s)) is non-increasing. Hence b′(s) = λGH(b(s)) is non-decreasing almost everywhere. This
implies that b is convex on (0, T]. □
EC.3.3. Proof of Proposition 2
Proof of Proposition 2. For a price-adjustment distribution H, define GH(x) := EH[(x  P )+].
The map GH is non-negative, non-decreasing, and 1-Lipschitz in x, so the ODE characterizing b in
Proposition 1 has a unique absolutely continuous solution given the right-limit initial condition. At
the exact deadline, b(0) = v regardless of λ and H, so Parts (i) and (ii) hold at s = 0 with equality;
Part (iii) holds at s = 0 because bi(0) = vi and v1  v2. It remains to be verified that the ordering
holds for s > 0. For notational convenience, we write bi for the optimal threshold corresponding to
parameter tuple i. Part (i). Fix H and v. By Proposition 1 , for each arrival rate λ, the threshold
solves
b′(s) = λ GH(b(s)), s > 0,
with the same right-limit initial condition
lim
s↓0
b(s) = EH[minfv, P g].
Thus, changing λ does not change the initial level of the threshold; it only changes the speed at
which the same autonomous dynamics evolves. More precisely, let β solve
β′(u) = GH(β(u)), β (0) = EH[minfv, P g].
Then bi(s) = β(λis) for s > 0. Since GH  0, the function β is non-increasing. Therefore, if λ1  λ2,
then for every s > 0,
b2(s) = β(λ2s)  β(λ1s) = b1(s).
Part (ii). Fix λ and v. From the ODE characterization, we have
b′ i(s) = λ GHi(bi(s)), s > 0,

ec6
and
lim
s↓0
bi(s) = EHi[minfv, P g], i = 1, 2.
By the expectation characterization of FSD ( Shaked and Shanthikumar 2007, Section 1.A.1), H1 FSD
H2 implies that, for every increasing function ϕ for which the expectations exist, one has EH1[ϕ(P )] 
EH2[ϕ(P )]. Applying this first to ϕ(p) = minfv, pg, which is increasing in p, gives
lim
s↓0
b1(s) = EH1[minfv, P g]  EH2[minfv, P g] = lim s↓0 b2(s).
Next, fix any x  0. Since p 7! (x  p)+ is decreasing in p, monotonicity under decreasing trans-
formations and the expectation characterization of FSD imply GH1(x)  GH2(x) (Shaked and Shan-
thikumar 2007, Theorem 1.A.3(a) and Section 1.A.1). We now show that b1(s)  b2(s) for all s. If
this were not the case, then by continuity, there exists a first time
s∗ := inffs > 0 : b1(s) > b2(s)g.
At this time, b1(s∗) = b2(s∗). Moreover, for s > s∗ suﬀiciently close to s∗, one has b1(s)  b2(s). On
such an interval,
b′ 1(s)  b′ 2(s) = λ GH1(b1(s)) + λ GH2(b2(s)).
Because b1(s)  b2(s), GH2 is non-decreasing, and GH1  GH2 pointwise, we obtain b′ 1(s)  b′ 2(s)  0.
This contradicts the first crossing of b1 above b2. Therefore b1(s)  b2(s) for all s > 0.
Part (iii). Fix λ and H. The two thresholds satisfy the same ODE,
b′ i(s) = λ GH(bi(s)), s > 0,
but have different right-limit initial conditions,
lim
s↓0
bi(s) = EH[minfvi, Pg], i = 1, 2.
Since v1  v2 and v 7! minfv, pg is non-decreasing for each fixed p, it follows that
lim
s↓0
b1(s) = EH[minfv1, Pg]  EH[minfv2, Pg] = lim s↓0 b2(s).
Suppose, for contradiction, that b1(s) > b2(s) for some s > 0, and let
s∗ := inffs > 0 : b1(s) > b2(s)g.
Then b1(s∗) = b2(s∗), and for s > s∗ suﬀiciently close to s∗, one has b1(s)  b2(s). On such an interval,
b′ 1(s)  b′ 2(s) = λ GH(b1(s)) + λ GH(b2(s))  0,
because GH is non-decreasing. This contradicts the first crossing of b1 above b2. Therefore b1(s) 
b2(s) for all s > 0. □

ec7
EC.3.4. Proof of Proposition 3
Proof of Proposition 3. Given a state (p, π), define M (s, π) := EP ∼ ¯Hπ

V B s, P, Φ(π, P )  . Here,
M (s, π) is the continuation value immediately after a price adjustment when the time-to-go is s,
before observing the realized new posted price.
Because the adjustment process is Poisson with rate λ, the current posted price remains equal
to p until the first adjustment arrives. Moreover, no new information is revealed before that first
adjustment. Hence, prior to the first adjustment, any admissible policy is equivalent to a two-step
rule for some deterministic waiting duration w 2 [0, s]. The policy waits for w units of time. If no
adjustment has occurred by then, it purchases at price p when the time-to-go has fallen to s  w. If
an adjustment occurs earlier, it switches to an optimal policy from the post-adjustment state.
Let Js,w(p, π) denote the value of this policy. Conditioning on the first adjustment time yields
Js,w(p, π) = e−λw(v  p)+ +
Z w
0
λe−λzM (s  z, π) dz.
Therefore,
V B(s, p, π) = sup
w∈[0,s]
Js,w(p, π).
For each fixed w, the only term in Js,w(p, π) that depends on p is e−λw(v  p)+, which is non-
increasing in p. Hence p 7! Js,w(p, π) is non-increasing for every w, and taking the supremum over w
shows that p 7! V B(s, p, π) is non-increasing.
Immediate purchase corresponds to w = 0, for which
Js,0(p, π) = (v  p)+.
For any fixed w 2 (0, s], write
As,w(π) :=
Z w
0
λe−λzM (s  z, π) dz,
which is independent of p. Then
Js,w(p, π) = e−λw(v  p)+ + As,w(π).
If p  v, then
Js,0(p, π)  Js,w(p, π) = (1  e−λw)(v  p)  As,w(π),
which is non-increasing in p. Therefore, if immediate purchase weakly dominates waiting time w at
some price p0, then it also weakly dominates waiting time w at every lower price p  p0.
Restrict attention first to prices p 2 [0, v]. For each fixed (s, π) and each w > 0, the set fp 2 [0, v] :
Js,0(p, π)  Js,w(p, π)g is therefore a lower interval. It is nonempty because immediate purchase at

ec8
p = 0 attains the maximal possible surplus v. Since immediate purchase is optimal exactly when it
weakly dominates every waiting time w 2 (0, s], the set of prices in [0, v] at which buying is optimal
is the intersection of lower intervals and hence is itself a lower interval. Let b(s, π) 2 [0, v] denote its
upper endpoint.
For prices p > v, immediate purchase yields zero surplus. Waiting is weakly optimal because it also
yields a nonnegative payoff, and ties can be resolved in favor of purchasing. Thus, one can select an
optimal policy that buys for p  b(s, π) and waits for p > b(s, π). □
EC.3.5. Proof of Proposition 4
Proof of Proposition 4. We give the argument briefly because it follows the same comparison
logic as Proposition 2 . Fix a belief π and valuation v. The arrival rate affects the Bayesian dynamic
program only through the Poisson process. After the time change ˜s = λs, the problem with rate
λ and time-to-go s is equivalent to a unit-rate problem with effective time-to-go ˜s, with the same
posterior update rule and predictive price-adjustment distributions. Hence
b(s, π; λ, v) = ˜b(λs, π; v),
where ˜b denotes the threshold in the unit-rate formulation.
It remains to note that the Bayesian stopping boundary is non-increasing in effective time-to-go.
A longer time horizon weakly expands the set of admissible waiting policies while leaving immediate
purchase feasible. Thus, the option value of waiting is weakly larger at every current price. Since
the stopping region is a lower interval by Proposition 3 , the upper endpoint of this interval cannot
increase with the time-to-go. Therefore, if λ1  λ2, then
b(s, π; λ2, v) = ˜b(λ2s, π; v)  ˜b(λ1s, π; v) = b(s, π; λ1, v).
For valuation monotonicity, fix λ and π, and let v1  v2. Write Vi and bi for the Bayesian value
function and threshold under valuation vi, and set ∆ := v2  v1. The posterior dynamics, adjustment
process, and admissible stopping rules are identical under the two valuations; only the purchase
payoff changes. For any admissible stopping rule τ , the pathwise bound (v2  Pτ )+  (v1  Pτ )+ + ∆
implies, after taking expectations and optimizing over stopping rules, that
V2(s, p, π)  V1(s, p, π) + ∆.
Now take any price p  b1(s, π). By Proposition 3 , purchase is optimal under valuation v1; since
b1(s, π)  v1, this gives V1(s, p, π) = v1  p. The preceding inequality then yields V2(s, p, π)  v2  p.
Immediate purchase is feasible under valuation v2, so V2(s, p, π)  v2  p. Hence equality holds, and p

ec9
is also in the stopping region under valuation v2. Therefore the stopping region under v1 is contained
in the stopping region under v2, which implies
b(s, π; λ, v1)  b(s, π; λ, v2) for all s.
□
EC.3.6. Proof of Lemma 2
Proof of Lemma 2. Part (i). By Assumption 2 and the fact that MLR order implies FSD ( Shaked
and Shanthikumar 2007, Theorem 1.C.1), θ1  θ2 implies Hθ1 FSD Hθ2. Let ϕ be any increas-
ing function for which the expectations below exist, and define mϕ(θ) := EP ∼Hθ [ϕ(P )]. By the
expectation characterization of FSD ( Shaked and Shanthikumar 2007, Section 1.A.1), the preceding
implication makes mϕ increasing in θ. Therefore, by the same characterization, if π1 FSD π2, then
EP ∼ ¯Hπ1 [ϕ(P )] =
R
Θ mϕ(θ) π1(dθ) 
R
Θ mϕ(θ) π2(dθ) = EP ∼ ¯Hπ2 [ϕ(P )]. This is exactly ¯Hπ1 FSD ¯Hπ2.
Part (ii). Let qi denote densities of πi in the MLR definition, and fix an observed price p for which
both posteriors are defined. The posterior density is proportional to hθ(p)qi(θ). For θ1 < θ 2, the
MLR ordering π1 MLR π2 gives q2(θ2)q1(θ1)  q2(θ1)q1(θ2). Multiplying both sides by the common
nonnegative factor hθ2(p)hθ1(p) and dividing by the positive product Z1(p)Z2(p) yields
hθ2(p)q2(θ2)
Z2(p)
hθ1(p)q1(θ1)
Z1(p)  hθ1(p)q2(θ1) Z2(p) hθ2(p)q1(θ2) Z1(p) ,
where Zi(p) is the normalizing constant in Bayes’ rule for Φ(πi, p). This is the cross-product condition
for Φ(π1, p) MLR Φ(π2, p).
Part (iii). Fix prior densities q1, q2 with π1 MLR π2 and prices p1  p2 for which the two posteriors
are defined. For θ1 < θ2, Assumption 2 gives
hθ2(p2)hθ1(p1)  hθ2(p1)hθ1(p2).
The prior ordering gives
q2(θ2)q1(θ1)  q2(θ1)q1(θ2).
Multiplying the two inequalities and dividing by the positive posterior normalizing constants yields
hθ2(p2)q2(θ2)
Z2(p2)
hθ1(p1)q1(θ1)
Z1(p1)  hθ1(p2)q2(θ1) Z2(p2) hθ2(p1)q1(θ2) Z1(p1) .
Here Zi(pi) is the normalizing constant for Φ(πi, pi). The displayed inequality is the cross-product
condition for Φ(π1, p1) MLR Φ(π2, p2). Taking π1 = π2 = π gives the stated monotonicity in the
observed signal. This proves all three claims. □

ec10
EC.3.7. Proof of Proposition 5
Proof of Proposition 5. We use a finite-adjustment approximation and then pass to the original
Poisson model. For each n  0, let Vn(s, p, π) be the value when the agent can use at most n future
price adjustments before the deadline. If no future adjustment can be used, the agent must decide
immediately, so V0(s, p, π) := (v  p)+. For n + 1 available adjustments,
Vn+1(s, p, π) = sup
0≤t≤s

e−λt(v  p)+ +
Z t
0
λe−λu EP ∼ ¯Hπ  Vn  s  u, P, Φ(π, P )  du  .
The sequence is non-decreasing in n, and the Poisson process generates only finitely many adjust-
ments before the deadline almost surely. Hence Vn(s, p, π) " V B(s, p, π) pointwise as n ! 1.
The key step is an induction showing that two monotonicity properties are preserved by the
dynamic program. For every n,
(a) for each fixed (s, π), the map p 7! Vn(s, p, π) is non-increasing;
(b) if π1 MLR π2, then
Vn(s, p, π1)  Vn(s, p, π2) for all (s, p).
The base case is immediate because V0(s, p, π) = ( v  p)+ is non-increasing in p and does not
depend on π. Assume the two properties hold for some n  0.
To prove price monotonicity for Vn+1, fix (s, π) and write, for each t 2 [0, s],
Jn(t; s, p, π) := e−λt(v  p)+ +
Z t
0
λe−λu EP ∼ ¯Hπ  Vn  s  u, P, Φ(π, P )  du.
Since Vn+1(s, p, π) = sup 0≤t≤s Jn(t; s, p, π) and the current price enters Jn only through the non-
increasing term e−λt(v  p)+, the supremum is also non-increasing in p. This proves Part (a) for
n + 1.
It remains to prove belief monotonicity. Fix π1 MLR π2. For each u 2 [0, s], let
Di :=

p :
Z
Θ
hθ(p)πi(dθ) > 0

, i = 1, 2,
be the positive predictive support under belief πi. On Di, define
gi(u, p) := Vn

s  u, p,Φ(πi, p)

, i = 1, 2.
The continuation comparison has two moving parts: the predictive distribution is worse under π2,
and the posterior after a given signal is also worse. We map these effects to a common price domain
using the following envelope. For each fixed u, the function g2(u, ) admits a bounded non-increasing
extensioneg2(u, ) to the full price space such that
eg2(u, p) = g2(u, p) ¯Hπ2-a.s., g 1(u, p) eg2(u, p) ¯Hπ1-a.s.

ec11
Indeed, g2(u, ) is non-increasing on D2: if p1, p2 2 D2 and p1  p2, then Part (iii) gives Φ(π2, p1) MLR
Φ(π2, p2), and the induction hypothesis applied first to beliefs and then to prices gives g2(u, p1) 
g2(u, p2). Define
eg2(u, p) :=
8
>><
>>:
g2(u, p), p 2 D2,
sup fg2(u, q) : q 2 D2, q  pg , p / 2 D2 and fq 2 D2 : q  pg 6= ;,
0, fq 2 D2 : q  pg = ;.
This construction preserves g2 on D2, fills support gaps by the upper envelope generated by π2-
possible prices, and assigns the payoff lower bound above the π2 predictive support. Hence eg2 is
bounded, non-increasing, and equal to g2 ¯Hπ2-a.s. Moreover, if p 2 D1 and q 2 D2 with q  p, then
Part (iii) gives Φ(π1, p) MLR Φ(π2, q), so the induction hypothesis yields
g1(u, p) = Vn

s  u, p,Φ(π1, p)

 Vn

s  u, p,Φ(π2, q)

 Vn

s  u, q, Φ(π2, q)

= g2(u, q).
Taking the supremum over such q proves the desired envelope inequality in the first two cases of the
definition; in the last case, eg2(u, p) = 0 and the inequality follows from nonnegativity.
We can now compare the continuation expectations. Since π1 MLR π2 implies π1 FSD π2 (Shaked
and Shanthikumar 2007, Theorem 1.C.1), Item (i) yields ¯Hπ1 FSD ¯Hπ2.
For each fixed u, we have
EP ∼ ¯Hπ1 [g1(u, P)]  EP ∼ ¯Hπ1 [eg2(u, P)]  EP ∼ ¯Hπ2 [eg2(u, P)] = EP ∼ ¯Hπ2 [g2(u, P)].
The first inequality follows from g1(u, p) eg2(u, p) ¯Hπ1-a.s. The second follows from ¯Hπ1 FSD ¯Hπ2
and the fact that eg2(u, ) is non-increasing, using monotonicity under decreasing transformations and
the expectation characterization of FSD ( Shaked and Shanthikumar 2007, Theorem 1.A.3(a) and
Section 1.A.1). The equality follows from eg2 = g2 ¯Hπ2-a.s.
Thus, for every waiting time t, Jn(t; s, p, π1)  Jn(t; s, p, π2) for all t 2 [0, s]. Taking the supremum
over t gives
Vn+1(s, p, π1)  Vn+1(s, p, π2).
Thus Part (b) also holds for n + 1.
By induction, both properties hold for all n  0. Passing to the pointwise limit Vn(s, p, π) "
V B(s, p, π) preserves the belief comparison, so
V B(s, p, π1)  V B(s, p, π2) for all (s, p).
Finally, translate the value comparison into a threshold comparison. By Proposition 3 , for each
(s, π) the stopping region is of the form fp : p  b(s, π)g. If p is in the stopping region under π1,

ec12
then V B(s, p, π1) = (v  p)+. The value comparison gives V B(s, p, π2)  V B(s, p, π1), while immediate
purchase is feasible under π2, so V B(s, p, π2)  (v  p)+. Hence V B(s, p, π2) = (v  p)+, and p is also
in the stopping region under π2. Therefore the stopping region under π1 is contained in the stopping
region under π2, and
b(s, π1)  b(s, π2) for all s.
This proves both claims. □
EC.3.8. Proofs for Information Gap
We organize the argument in two layers. The short-window bound follows directly from a deadline-
purchase comparison. For longer windows, we compare the oracle with a feasible learn-then-act policy:
the loss first splits into a learning-delay term and an acting-phase term; the learning-delay term
is controlled by the lower tail of the price distribution near its support endpoint; and the acting-
phase term is controlled by posterior concentration together with Lipschitz continuity of the oracle
threshold. The final proof chooses the learning length and confidence level to balance these bounds.
EC.3.8.1. Short-Window Bound.
Proof of Lemma 3. The lower bound is the value of information. For the upper bound, compare
the oracle with the feasible Bayesian policy that waits until the deadline and then purchases if the
posted price is smaller than or equal to the consumer’s valuation. Let NT denote the number of
adjustments during the shopping window. On fNT = 0g, the price never changes, so the deadline
policy attains the same payoff as the oracle, (v  PT )+. On fNT  1g, the oracle’s advantage over
this feasible policy is at most v. Since the Bayesian value is at least the payoff from the deadline
policy,
G(T, ˆπ)  v P(NT  1) = v(1  e−λT )  vλT,
where the last inequality uses 1  e−x  x. □
EC.3.8.2. Long-Window Setup: Posterior Confidence Set and LTA Policy. For the long-
window bound, we first construct the posterior confidence set used by the learn-then-act policy. For
a realized price history x1:n, the posterior effective support is
Θn(x1:n) := fθ 2 Θ : ˆπ(θ)
nY
i=1
hθ(xi) > 0g.
The posterior-regularity condition in Assumption 3 implies that, after any n observed prices, the
posterior is (a0+a1n)-strongly log-concave on its effective support, which is an interval. Let ¯θn denote
the posterior mean and, for δ 2 (0, 1), define
dn(δ) :=
s
2 log(2/δ)
a0 + a1n , I n(δ) := [¯θn  dn(δ), ¯θn + dn(δ)] \ Θ.

ec13
The proof of Proposition 6 compares the oracle’s expected payoff with that of a feasible learn-
then-act (LTA) policy. Fix a split time ℓ 2 (0, T). We use elapsed-time notation: P0 is the entry price
and Pℓ is the price at the end of the learning phase. The LTA policy operates in two phases:
(a) Learning phase (elapsed time [0, ℓ]): starting from the posterior Φ(ˆπ, P0) after observing the entry
price, observe prices without purchasing. After ℓ units of time, the agent has seen nℓ := 1 + Nℓ
prices, where Nℓ  Poisson(λℓ), and formed the posterior mean ¯θnℓ.
(b) Acting phase (elapsed time [ℓ, T]): construct the posterior confidence interval Inℓ(δ) and follow
the upper-envelope threshold
¯bInℓ (δ)(s) := sup η∈Inℓ (δ) bη(s), s 2 [0, T  ℓ].
At elapsed time t 2 [ℓ, T], the policy stops whenever the current price satisfies Pt  ¯bInℓ (δ)(T  t).
Since V B is the value of the optimal Bayesian policy from the entry state (T, P0, Φ(ˆπ, P0)), it is at
least as large as the expected payoff of any feasible policy from the same state, including the LTA
policy. Hence,
G(T, ˆπ)  E

V
˜θ(T, P0)   E  LTA payoff  .
We decompose the right-hand side into two terms:
G(T, ˆπ)  E

V
˜θ(T, P0)  V ˜θ(T ℓ, Pℓ)  | {z }
E(ℓ)
+ E

V
˜θ(T ℓ, Pℓ)  J ˜θ T −ℓ  Pℓ, τ¯bInℓ (δ)  | {z }
R(ℓ)
, (EC.2)
where J θ s (p, τ) is the expected payoff of stopping rule τ under θ-dynamics from a state with time-to-go
s and current price p, and τ¯bInℓ (δ) denotes the stopping rule using the confidence-envelope threshold.
The first term E(ℓ) is the learning-delay gap ; the second term R(ℓ) is the acting-phase regret.
EC.3.8.3. Learning-Delay Bound.
Lemma EC.1 (Learning Delay). Under Assumption 3(i), there exists CE < 1 such that for
every ℓ 2 [0, T),
E(ℓ)  CE(1 + T  ℓ)−1/α.
Proof of Lemma EC.1 . Fix ℓ < T . Conditional on ˜θ = θ, both P0 and Pℓ have marginal Hθ (the
initial price is drawn from Hθ, and at any later time the current price is either unchanged or the
most recent adjustment, both distributed as Hθ). Hence,
E(ℓ) = E

m
˜θ(T )  m ˜θ(T ℓ)  = E  b ˜θ(T ℓ)  b ˜θ(T )  ,
using mθ(s) = EHθ [V θ(s, P)] = v  bθ(s) from Proposition 1 .

ec14
The threshold remains above the lower endpoint pθ L. Indeed, bθ(0+) = EHθ [minfv, P g]  pθ L, and
the ODE has zero drift at and below pθ L because Hθ([0, pθ L)) = 0. Thus, the solution cannot cross
below pθ L. Define yθ(s) := bθ(s)  pθ L  0. Let c > 0, α > 0, and ε > 0 be the common constants in
Assumption 3, the ODE from Proposition 1 gives, for a.e. s > 0,
y′ θ(s) = λ EHθ  (pθ L+yθ(s)  P )+  λ Z min{y,ε}
0
cuα du =  λc α + 1 min  yθ(s)α+1, ε α+1	 .
The inequality follows by writing EHθ [(pθ L + y  P )+] = R y 0 Hθ([pθ L, pθ L + u]) du and applying the
lower-tail condition for u  ε. Let K := λc/(α + 1). When yθ(s) > ε, the preceding inequality implies
y′ θ(s)  Kε α+1. Since pθ L  bθ(s)  v, the hitting time of [0, ε] is bounded above by the common
constant τ0 := (v  ε)+/(Kε α+1). Let τθ denote this hitting time. For s  τθ, comparison with the
solution of z′ = Kz α+1 starting from z(τθ) = ε gives
yθ(s) 

ε−α + αK(s  τθ) −1/α .
If s  2τ0 + 1, then s  τθ  (1 + s)/2, so yθ(s) is bounded by (2/(αK))1/α(1 + s)−1/α. If s < 2τ0 + 1,
then yθ(s)  v  v(2τ0 + 2)1/α(1 + s)−1/α. Taking
CE  max
( 2
αK
1/α
, v(2τ0 + 2)1/α
)
yields yθ(s)  CE(1 + s)−1/α uniformly in θ and s. Since bθ(T )  pθ L,
bθ(T ℓ)  bθ(T )  bθ(T  ℓ)  pθ L = yθ(T  ℓ)  CE(1 + T  ℓ)−1/α.
Taking expectations over Θ completes the proof. □
EC.3.8.4. Posterior Concentration Bound.
Lemma EC.2 (Brascamp–Lieb V ariance Bound). Let µ be a probability measure on an
interval I with density proportional to expfφ(θ)g on I. If φ′′(θ)  κ > 0 on the relative interior of
I, then, for every absolutely continuous function f ,
Varµ(f (θ))  1 κ Z I jf ′(θ)j2 µ(dθ).
In particular, Varµ(θ)  1/κ.
Proof. This is the one-dimensional Brascamp–Lieb variance inequality ( Brascamp and Lieb 1976);
see also the treatment in Bobkov and Ledoux (2000). The final statement follows from taking f (θ) = θ.
□

ec15
Lemma EC.3. Under Assumption 3 , for every ℓ  0 and δ 2 (0, 1), the interval Inℓ(δ) satisfies
P
h
˜θ 2 Inℓ(δ)
i
 1  δ, and there exists CI < 1 such that
E[diam(Inℓ(δ))]  CI
r
log(2/δ)
1 + ℓ .
Proof of Lemma EC.3 . Fix a realized history with n observed prices x1, . . . , xn. Its posterior
effective support is
Θn(x1:n) =
(
θ 2 Θ : ˆπ(θ)
nY
i=1
hθ(xi) > 0
)
.
The posterior-regularity part of Assumption 3 implies that this set is an interval and that the posterior
density qn, defined by πn(dθ j x1:n) = qn(θ)dθ, is strongly log-concave on its relative interior:
∂2 θ log qn(θ)  a0 + a1n.
Let κn := a0 + a1n and write qn(θ) / expfφn(θ)g, so that φ′′ n(θ)  κn.
This gives sub-Gaussian posterior tails around the posterior mean. For t  0, let
Mn(t) :=
Z
Θn(x1:n)
expftugqn(u) du
be the posterior moment generating function, conditional on x1:n. The compactness of Θ makes Mn(t)
finite. The exponentially tilted posterior density
˜qn,t(θ) := expftθgqn(θ) Mn(t)
has negative log-density φn(θ)  tθ up to an additive constant, so the same curvature lower bound
applies. By Lemma EC.2 , Var˜qn,t(θ)  1/κn. For the centered log-moment generating function
Λn(t) := log Mn(t)  t¯θn,
we have Λn(0) = Λ′ n(0) = 0 and
Λ′′ n(t) = Var˜qn,t(θ)  1 κn .
Integrating twice gives Λn(t)  t2/(2κn) for all t  0. Therefore, for any z > 0, Chernoff’s inequality
gives
πn(θ  ¯θn > z j x1:n)  inf t>0 expftz + Λn(t)g  inf t>0 exp

tz + t2
2κn

= exp

 κnz2
2

.
Applying the same argument to the tilt proportional to expftθgqn(θ) gives the same lower-tail
bound. A union bound then yields
πn

jθ  ¯θnj > z

 x1:n   2 exp   κnz2
2

.

ec16
With z = dn(δ) =
p
2 log(2/δ)/κn, the right-hand side equals δ, so πn(In(δ) j x1:n)  1  δ for every
realized history and every fixed n. Let Hℓ be the random history observed during the learning phase.
A veraging the conditional coverage bound over Hℓ gives
P(˜θ 2 Inℓ(δ)) = E
h
P(˜θ 2 Inℓ(δ) j Hℓ)
i
 1  δ.
It remains to convert this concentration radius into an expected diameter bound. Since In(δ) is
the intersection of Θ with an interval of radius dn(δ),
diam(Inℓ(δ))  2dnℓ(δ) = 2
s
2 log(2/δ)
a0 + a1nℓ
.
Thus it suﬀices to control E[(a0 + a1nℓ)−1/2]. Since nℓ = 1 + Nℓ with Nℓ  Poisson(λℓ), define Aℓ :=
fNℓ  λℓ/2g. Splitting on Aℓ,
E[(a0 + a1nℓ)−1/2]  1p a0 + a1(1 + λℓ/2) + P(Ac ℓ)pa0 + a1 .
The Poisson Chernoff bound gives P(Ac ℓ)  exp(λℓ/8). The first term in the preceding display is at
most c−1/2(1 + ℓ)−1/2 with c := minfa0 + a1, a1λ/2g, and the exponential term is also bounded by a
constant multiple of (1 + ℓ)−1/2. Hence, for a constant C depending only on (a0, a1, λ),
E[(a0 + a1nℓ)−1/2]  C(1 + ℓ)−1/2.
Combining this bound with the radius inequality gives
E[diam(Inℓ(δ))]  2
p
2 C
r
log(2/δ)
1 + ℓ .
Taking CI := 2
p
2 C yields the desired result. □
EC.3.8.5. Threshold and Acting-Regret Bounds.
Lemma EC.4 (Lipschitz Continuity of Oracle Thresholds). Suppose Assumption 3
holds. Then, for all θ, θ′ 2 Θ,
sup
s>0
jbθ(s)  bθ′ (s)j  W∞(Hθ, Hθ′)  Ljθ  θ′j.
Proof. Fix θ, θ′ 2 Θ, and write H := Hθ and G := Hθ′. Define
FH(x) := λ EP ∼H[(x  P )+], F G(x) := λ EQ∼G[(x  Q)+].
By Proposition 1 , the corresponding oracle thresholds satisfy b′ H(s) = FH(bH(s)) and b′ G(s) =
FG(bG(s)) for a.e. s > 0, with right-limit initial conditions bH(0+) = EP ∼H[minfv, P g] and bG(0+) =
EQ∼G[minfv, Qg].

ec17
Let d := W∞(H, G). For any ε > 0, choose a coupling (P, Q) with marginals H and G such that
jP  Qj  d + ε almost surely. Then Q  P  (d + ε), and hence, for every x, (x  Q)+  (x + d + ε
P )+. Taking expectations gives FG(x)  FH(x + d + ε).
The same coupling also gives
bH(0+)  bG(0+)  E[j minfv, P g  minfv, Qgj]  d + ε,
because p 7! minfv, pg is 1-Lipschitz.
Now define yε(s) := bG(s) + d + ε. The previous inequality implies
y′ ε(s) = FG(bG(s))  FH(bG(s) + d + ε) = FH(yε(s))
for a.e. s > 0, while yε(0+)  bH(0+). The function FH is non-decreasing in its argument, so FH is
non-increasing. Therefore the scalar comparison argument applies: if z(s) := bH(s)  yε(s), then on
the set fz(s) > 0g,
z′(s)  FH(bH(s)) + FH(yε(s))  0.
Since z(0+)  0, the positive part z+(s) cannot increase from zero, and thus bH(s)  yε(s) for all
s > 0. Hence bH(s)  bG(s) + d + ε. Letting ε # 0 gives bH(s)  bG(s) + d for all s > 0.
Repeating the same argument with H and G interchanged gives bG(s)  bH(s) + d for all s > 0.
Therefore
sup
s>0
jbH(s)  bG(s)j  W∞(H, G).
Assumption 3(ii) then yields sups>0 jbθ(s)  bθ′ (s)j  Ljθ  θ′j.
Lemma EC.5 (Acting Regret). Suppose Assumption 3 holds. There exists CR < 1 such that,
for every learning length ℓ 2 [0, T] and confidence level δ 2 (0, 1),
R(ℓ)  CR
r
log(2/δ)
1 + ℓ + vδ.
Proof of Lemma EC.5 . Fix the realized confidence interval I := Inℓ(δ) and let τI be the stopping
rule generated by the upper-envelope threshold ¯bI. On the event f˜θ 2 Ig, condition on a realization
˜θ = θ. Then θ 2 I, so ¯bI(s)  bθ(s) for every s 2 [0, T  ℓ], hence τI  τ ∗ θ pathwise. Therefore, up to
time τI, both the confidence-envelope policy and the θ-oracle take the same action, namely to wait.
Consider an acting-phase initial state (s, p) with s > 0; the case s = 0 is trivial. Let (U, P) denote
the time-to-go horizon and current price at the random state where τI stops. The terminal condition
gives V θ(0, P) = (v  P )+. Thus, if U = 0, both the confidence-envelope policy and the oracle face
the same terminal decision, and the local loss from stopping at (U, P) is zero. It remains to consider

ec18
the case U > 0. Since the confidence-envelope policy stops only when P  ¯bI(U ) and ¯bI(U )  v, its
stopping payoff is v  P .
If P  bθ(U ), then the oracle threshold policy also stops at (U, P), so V θ(U, P) = v  P and the
local loss is zero. If P > b θ(U ), threshold value matching gives
V θ(U, bθ(U )) = v  bθ(U ).
Because p 7! V θ(U, p) is non-increasing,
V θ(U, P)  V θ(U, bθ(U )) = v  bθ(U ).
Therefore,
V θ(U, P)  (v  P )  P  bθ(U )  ¯bI(U )  bθ(U )  sup
u∈(0,s]
(¯bI(u)  bθ(u)).
Taking conditional expectations over the stopping state gives, on fθ 2 Ig,
V θ(s, p)  J θ s (p, τI)  sup
u∈(0,s]
(¯bI(u)  bθ(u)).
By Lemma EC.4 , for every η 2 I and every u > 0,
bη(u)  bθ(u)  jbη(u)  bθ(u)j  Ljη  θj.
On fθ 2 Ig, it follows that
sup
u∈(0,s]
(¯bI(u)  bθ(u))  L diam(I).
On the complement event f˜θ /2 Ig, the regret is trivially bounded by v. Taking expectations gives
R(ℓ)  L E[diam(Inℓ(δ))] + v P(˜θ /2 Inℓ(δ)).
By Lemma EC.3 , the first term is bounded by LCI
p
log(2/δ)/(1 + ℓ) and the second probability is
at most δ. Taking CR := LCI proves the claim. □
EC.3.8.6. Proof of the Long-Window Bound.
Proof of Proposition 6. Set ℓ = T /2 and δ = 1/(eT ). By ( EC.2) and Lemmas EC.1 and EC.5, for
T  1,
G(T, ˆπ)  CE(1 + T /2)−1/α + CR
s
log(2eT )
1 + T /2 + v eT .
Absorbing constants yields the stated bound. □

ec19
EC.3.8.7. Example: Bounded Exponential-Tilt Price-Adjustment Distribution. We
give a simple bounded-support family satisfying both the monotone-likelihood-ratio condition and
the regularity conditions used in the long-window information-gap bound. Fix ¯p > 0 and let
hθ(p) = θeθp
eθ ¯p  1 , 0  p  ¯p, θ 2 [θ, ¯θ]  (0, 1).
Higher values of θ tilt probability mass toward higher prices. Indeed, for θ2 > θ1, the likelihood ratio
hθ2(p)/hθ1(p) is proportional to e(θ2−θ1)p and is increasing in p, so Assumption 2 holds.
The family also satisfies Assumption 3 . First, with pθ L = 0,
Hθ([0, x]) = eθx  1 eθ ¯p  1  θ e¯θ ¯p  1 x, 0  x  ¯p,
so the lower-tail condition holds with α = 1. Second, the quantile function is
Qθ(u) = 1 θ log  1 + u(eθ ¯p  1)  , u 2 [0, 1].
Because (θ, u) 7! Qθ(u) is continuously differentiable on the compact set [θ, ¯θ]  [0, 1], there exists
L < 1 such that
W∞(Hθ, Hθ′) = sup
u∈[0,1]
jQθ(u)  Qθ′(u)j  Ljθ  θ′j.
Third, Θ(x) = [θ, ¯θ] for x 2 [0, ¯p], and
∂2 θ log hθ(x) = 1 θ2  ¯p2e−θ ¯p (1  e−θ ¯p)2 > 0.
The last expression is continuous and strictly positive on the compact Θ, so it is bounded below by
some a1 > 0. Finally, a truncated Gamma prior on Θ with density proportional to θα0−1e−β0θ and
α0 > 1 satisfies
 d2
dθ2 log ˆπ(θ) = α0  1 θ2  α0  1 ¯θ2 =: a0.
Thus Proposition 6 applies with α = 1, giving G(T, ˆπ) = O(T −1 + p log T /T) = O( p log T /T).
EC.3.9. Adversarial upper bound for Proposition 7
We prove Lemma 4 using the sale-termination rule in ( 5).
Proof of Lemma 4. We first record the reduction behind the upper bound. By Yao’s minimax
principle ( Yao 1977), it is enough to construct a flash-sale process under which every deterministic
online policy satisfies E[ALG]/E[OPT]  ρ. Equivalently, if a randomized online algorithm guaran-
teed competitive ratio ρ on every price path, then under any distribution over price paths its expected
payoff would be at least ρ E[OPT]; but a randomized policy is a mixture of deterministic policies,
so an upper bound that holds for every deterministic policy under the constructed distribution also
holds for every randomized policy.

ec20
If p0 = pL, the initial price already attains the lowest feasible price. Hence, buying immediately
matches the offline oracle on every feasible path, and the competitive ratio is 1. Thus, the upper
bound is immediate in this boundary case. In the remainder of the proof, assume p0 > pL.
The first step is to convert the random end-sale time into the markdown reached by the price path
before the sale expires. Fix one such distribution and write
q := ˆp(˜t), M := q  pL.
Define the realized markdown depth from the reference price q by
X := q  ˆp(σ) 2 [0, M].
For any x 2 [0, M], let
t(x) := ˜t + t2  t1
p0  pL
x,
so that ˆp(t(x)) = q  x. By construction,
P(X  x) = P(σ  t(x)) = A A + x , x 2 [0, M].
For x < M , this follows directly from the distribution of σ; at x = M , it uses the atom at t2. Thus
the sale-termination rule ( 5) is equivalently a distribution over the realized markdown depth X with
survival function
P(X  x) = A A + x , x 2 [0, M].
Therefore,
E[X] =
Z M
0
P(X  x) dx =
Z M
0
A
A + x dx = A log
 A + M
A

.
It remains to bound the payoff of an arbitrary deterministic online policy. Since σ  ˜t almost surely
and ˆp is strictly decreasing, buying before ˜t is weakly dominated by waiting until ˜t. After ˜t, while
the sale is still active, the policy observes no new uncertainty beyond the deterministic decline of ˆp:
the only random event is the sale ending. Therefore, a deterministic policy is characterized, during
the active sale, by the first sale price at which it would buy. We write this target price as q  y, or
equivalently, use the target markdown y 2 [0, M]. If a policy would never buy during the sale, we
may upper-bound its payoff by assigning it the target y = M , which only makes the policy weakly
better for the upper-bound calculation. When v > p U , if the target is missed, we also upper bound
the policy’s continuation payoff by allowing it to buy at the reversion price pU .
We now consider the four parameter choices separately.

ec21
Case (i): pL < v  p0. Fix ε 2 (0, v  pL). Here A = ε and q = v  ε, so M = v  ε  pL. If the
algorithm chooses target markdown y 2 [0, M], then it buys at price q  y on the event fX  yg and
earns surplus
v  (q  y) = ε + y.
If X < y , then the sale ends before the target is reached, and buying later at pU is not beneficial
because v  p0  pU ; hence, the payoff is 0. Thus
E[ALG] = ε ε + y (ε + y) = ε.
Since this is independent of y, every deterministic online algorithm has expected payoff at most ε.
The offline oracle observes σ and buys just before the sale ends, hence its payoff is
v  ˆp(σ−) = v  ˆp(σ) = ε + X,
where the middle equality follows from the continuity of ˆp. Therefore
E[OPT] = ε + E[X] = ε + ε log
 ε + v  ε  pL
ε

= ε

1 + log
 v  pL
ε

.
Hence
E[ALG]
E[OPT]  1 1 + log  v−pL ε  .
Letting ε # 0 gives a zero upper bound for this valuation regime.
Case (ii): p0 < v  pU . Now A = v  p0 and q = p0, so M = p0  pL. If the algorithm chooses
markdown y 2 [0, M], then on fX  yg it buys at price p0  y and earns
v  (p0  y) = A + y.
If X < y , then the sale ends too early and buying later at pU yields a non-positive surplus, since
v  pU . Thus
E[ALG] = A A + y (A + y) = A = v  p0.
The oracle again buys just before termination, so its payoff is
v  ˆp(σ−) = v  ˆp(σ) = A + X.
Hence
E[OPT] = A + A log
 A + p0  pL
A

= (v  p0)

1 + log
 v  pL
v  p0

.
Therefore
E[ALG]
E[OPT]  1 1 + log  v−pL v−p0  .

ec22
Case (iii): v > pU and x0 < pU  p0. Here A = pU  p0 and q = p0, so M = p0  pL. If the algorithm
chooses markdown y 2 [0, M], then on fX  yg it buys during the sale at price p0  y and earns
v  (p0  y) = v  pU + A + y.
If X < y , the sale ends first. For the purpose of an upper bound, we allow the algorithm to buy at
price pU and obtain a surplus of v  pU . Thus
E[ALG]  (v  pU ) + A A + y (A + y) = v  pU + A = v  p0.
The oracle buys just before termination, so its payoff is
v  ˆp(σ−) = v  ˆp(σ) = v  pU + A + X = v  p0 + X.
Therefore
E[OPT] = v  p0 + A log
 A + p0  pL
A

= v  p0 + (pU  p0) log
 pU  pL
pU  p0

.
Hence
E[ALG]
E[OPT]  v  p0 v  p0 + (pU  p0) log  pU −pL pU −p0  .
Case (iv): v > pU and x0  pU  p0. The equation defining x0 has a unique positive solution because
x/(v  pU ) + log x is strictly increasing on (0, 1). Moreover, x0 < pU  pL, since the left-hand side
evaluated at pU  pL exceeds log(pU  pL)  1. Thus q = pU  x0 lies above pL; when x0  pU  p0,
it also satisfies q  p0, so the corresponding ˜t is well defined on the flash-sale path. Now A = x0 and
q = pU  x0, so
M = q  pL = pU  pL  x0.
If the algorithm chooses markdown y 2 [0, M], then on fX  yg it buys during the sale at price q  y
and earns
v  (q  y) = v  pU + x0 + y.
If X < y , the sale ends first. For the purpose of an upper bound, we allow the algorithm to buy at
pU , obtaining surplus v  pU . Hence
E[ALG]  (v  pU ) + x0
x0 + y (x0 + y) = v  pU + x0.
The oracle buys just before termination, and its payoff is v  ˆp(σ−) = v  ˆp(σ) = v  pU + x0 + X.
Thus
E[OPT] = v  pU + x0 + E[X] = v  pU + x0 + x0 log
 x0 + M
x0

.

ec23
Since x0 + M = pU  pL, this becomes
E[OPT] = v  pU + x0 + x0 log
 pU  pL
x0

.
Using the defining equation of x0,
log
 pU  pL
x0

= 1 + x0
v  pU
,
and therefore
E[OPT] = v  pU + x0 + x0

1 + x0
v  pU

= (v  pU + x0)2
v  pU
.
It follows that
E[ALG]
E[OPT]  v  pU + x0 (v  pU + x0)2/(v  pU ) = v  pU v  pU + x0 .
Combining the four cases proves CR(A)  ρ(v) for every online policy A. □
EC.3.10. Proof of Lemma 5
Proof of Lemma 5. The case v  p0 is immediate because the target ratio is 0. Consider v > p0,
and fix an arbitrary feasible price path p(). Let
p⋆ := inf
t∈[0,T ]
p(t).
Since p(0) = p0, we have p⋆  p0. Because v > p0, the offline value is OPT(p) = v  p⋆. If the threshold
b is reached before the deadline, the purchase price is at most b. If the threshold is not reached before
the deadline and v > p U , the terminal valuation rule purchases at T and yields a payoff of at least
v  pU . Thus, it suﬀices to lower-bound the randomized policy’s payoff as a function of p⋆. Boundary
events where b = p⋆ do not affect the integrals below; the only atom is at p0, and that threshold is
reached at the initial price.
Case (i): p0 < v  pU . The CDF is valid because
Fb(p0) = ρ log
 v  pL
v  p0

= 1  ρ < 1.
Hence there is an atom of size ρ at p0, and on [pL, p0) the distribution has density
fb(z) = F ′ b(z) = ρ v  z .
Since v  pU , any payoff from the terminal valuation rule can only improve the lower bound. When
b  p⋆, the policy obtains realized surplus at least v  b: either the threshold is reached before the
deadline, or the terminal valuation rule buys at T if the relevant crossing occurs only at the endpoint.
Therefore
E[ALG j p⋆]  ρ(v  p0) +
Z p0
p⋆
(v  z) ρ v  z dz = ρ(v  p0) + ρ(p0  p⋆) = ρ(v  p⋆).

ec24
Thus
E[ALG j p⋆]
OPT(p)  ρ
for every feasible price path.
Case (ii): v > pU and x0 < pU  p0. Let
D := v  pU , C := pU  p0, L := log
 pU  pL
pU  p0

.
Then
ρ = D + C D + C + CL .
We first check that the CDF is valid. Since x0 < C and the function
h(x) := x v  pU + log x
is strictly increasing on (0, 1), the defining equation
h(x0) = log(pU  pL)  1
implies
h(C) > h(x0),
that is,
C
v  pU
+ log C > log(pU  pL)  1.
Rearranging gives
L < 1 + C D .
Hence
Fb(p0) = ρL = (D + C)L D + C + CL < 1.
So the CDF indeed has an atom of size 1  ρL at p0, and density
fb(z) = ρ pU  z on [pL, p0).
If the threshold is reached before the deadline, the agent pays at most b and gets a payoff of at
least v  b = D + (pU  b). If the threshold is not reached before the deadline, the terminal valuation
rule buys at T and yields a payoff of at least D. Therefore
E[ALG j p⋆]  D + E[(pU  b)1fb  p⋆g] .
Using the atom at p0 and the density on [pL, p0),
E[ALG j p⋆]  D + (1  ρL)(pU  p0) +
Z p0
p⋆
(pU  z) ρ pU  z dz.

ec25
That is,
E[ALG j p⋆]  D + (1  ρL)C + ρ(p0  p⋆).
Since
1  ρL = 1  D + C D + C + CL L,
we obtain
D + (1  ρL)C = D + C  ρCL = ρ(D + C) = ρ(v  p0).
Therefore
E[ALG j p⋆]  ρ(v  p0) + ρ(p0  p⋆) = ρ(v  p⋆).
Thus
E[ALG j p⋆]
OPT(p)  ρ
for every feasible price path.
Case (iii): v > pU and x0  pU  p0. Let
D := v  pU , q := pU  x0, ρ := D D + x0 .
The cutoff q is admissible. The case condition gives q  p0. Moreover, x 7! x/D + log x is strictly
increasing, and at x = pU  pL its value is larger than log(pU  pL)  1. The defining equation for x0
therefore implies x0 < pU  pL, so q > pL. By the defining equation of x0,
log
 pU  pL
x0

= 1 + x0
D ,
and hence
ρ log
 pU  pL
x0

= D D + x0  1 + x0 D  = 1.
Therefore, the CDF is valid and continuous at q, with density
fb(z) = ρ pU  z on [pL, q).
If p⋆  q, then the event fb  p⋆g is the same as b 2 [p⋆, q], up to a boundary event. The terminal
valuation rule contributes at least D whenever the threshold is not reached before the deadline, and
a reached threshold contributes the additional term pU  b. Hence
E[ALG j p⋆]  D +
Z q
p⋆
(pU  z) ρ pU  z dz = D + ρ(q  p⋆).
Since q = pU  x0 and D = ρ(D + x0),
E[ALG j p⋆]  D + ρ(pU  x0  p⋆) = ρ(D + pU  p⋆) = ρ(v  p⋆).

ec26
If p⋆ > q, then no threshold in the support is reached before the deadline, so the terminal valuation
rule yields payoff at least D:
E[ALG j p⋆]  D.
Because p⋆ > q = pU  x0, we have pU  p⋆ < x0, and thus
v  p⋆ = D + (pU  p⋆) < D + x0.
Therefore
E[ALG j p⋆]  D > D D + x0 (v  p⋆) = ρ(v  p⋆).
Combining the two subcases yields
E[ALG j p⋆]  ρ(v  p⋆)
for every feasible price path. Since OPT(p) = v  p⋆, the policy achieves competitive ratio at least
ρ = v  pU
v  pU + x0
.
This completes the proof. □
EC.3.11. Proofs for Minimax Regret
Proof of Lemma 6. It suﬀices, by Yao’s principle, to construct a distribution over feasible price
paths under which every deterministic online policy has expected regret at least ¯R(v). Throughout
the proof, a, γ, and ∆ are the quantities defined immediately before ¯R(v); let σ be defined as in
Lemma 6 . By construction, pL  γ  p0, ∆ > 0, and
∆ log a  pL
∆ = ¯R(v). (EC.3)
Indeed, if γ = p0, then ∆ = a  p0; if γ < p 0, then ∆ = ( a  pL)/e, so equation ( EC.3) equals
(a  pL)/e.
Let X := ˆp(σ) be the terminal sale price. For x 2 (pL, γ), let t(x) be the unique time satisfying
ˆp(t(x)) = x. The end-sale distribution gives
P(X  x) = P(σ  t(x)) = ∆ a  x , p L < x < γ.
At x = pL, the same CDF value is induced by the atom at t2. Thus X has CDF
G(x) :=
8
>>><
>>>:
0, x < p L,
∆
a  x , p L  x < γ,
1, x  γ.

ec27
Consider any deterministic online policy. Before the jump, all paths share the same declining price
history. Hence, the policy’s first purchase along this common history can be represented by a target
price y: the first price at which it would buy if the decline continued all the way to pL. If the policy
would not buy before pL, set y = 0 < pL.
If y  γ, every path reaches γ before reversion and the policy buys before reversion at a price at
least γ. Its online payoff is therefore at most v  γ, whereas the offline payoff is v  X. Its regret is
at least γ  X, and hence its expected regret is at least
E[γ  X] =
Z γ
pL
G(x) dx = ∆ log a  pL
∆ = ¯R(v).
If pL  y < γ, then the policy buys before reversion on fX  yg and misses the target on fX > y g.
In the first event, regret is at least y  X. In the second event, even granting the policy the best
possible continuation payoff after reversion, regret is at least a  X: when v  pU , this is v  X, and
when v > pU , it is pU  X. Thus, its expected regret is at least
r(y) :=
Z y
pL
(y  x) dG(x) +
Z γ
y
(a  x) dG(x).
The CDF has an atom at pL and density g(x) = ∆/(a  x)2 on (pL, γ). For y 2 (pL, γ), the atom
contributes to the first integral and is already captured by G(y). Hence
r′(y) = G(y)  (a  y)g(y) = 0,
so r(y) is constant on (pL, γ). Taking the limit as y " γ gives r(y) = E[γ  X] = ¯R(v). Finally, if
y < pL, the policy does not buy before reversion on any path, and its regret is at least a  X  γ  X
pathwise. Its expected regret is therefore also at least ¯R(v).
Thus, every deterministic policy has expected regret at least ¯R(v) under the constructed distribu-
tion. A randomized online policy is a mixture of deterministic policies, so its expected regret under
the same path distribution is also at least ¯R(v). Consequently, for every online policy A, there exists
a feasible path with Reg(A, p)  ¯R(v), proving the claim. □
Proof of Lemma 7. For a feasible price path, write
p∗ := inf
t∈[0,T ]
p(t).
Since p(0) = p0, we have p∗  p0. Boundary events at which the path attains exactly the realized
threshold do not affect the integrals below.
If a threshold b is reached before the deadline, the policy purchases at a price no higher than b,
so its regret relative to the offline minimum is at most b  p∗. If the threshold is not reached before
the deadline, the terminal valuation rule yields a nonnegative payoff when v  pU , so the regret is

ec28
at most v  p∗. When v > p U , the terminal valuation rule purchases at the deadline; because the
deadline price is no higher than pU , the regret is at most pU  p∗. Thus the missed-threshold penalty
is governed by a  p∗; in Case (i), this reduces to v  p∗.
Case (i): pL < v  p0. Set ¯p := v  (v  pL)/e, draw b with density
f (b) = 1 v  b 1{pL≤b≤ ¯p},
This is a probability density because
Z ¯p
pL
db
v  b = log v  pL v  ¯p = 1.
If p∗  ¯p, then with F (x) := R x pL f (b) db,
Reg(A, p) 
Z ¯p
p∗
(b  p∗) db v  b + F (p∗)(v  p∗).
Since F (p∗) = log((v  pL)/(v  p∗)), the right-hand side equals
(¯p  p∗) + (v  p∗) log v  pL
v  ¯p = v  ¯p = v  pL e .
If p∗ > ¯p, then no threshold in the support is reached and the regret is at most (v  p∗)+ < v  ¯p.
Hence supp(·) Reg(A, p)  (v  pL)/e.
Case (ii): p0 < v  pU . Let Lv := log((v  pL)/(v  p0)). If Lv  1, draw b with density f (b) =
1/(v  b) on [pL, p0) and put an atom q0 := 1  Lv at p0. If p∗ 2 [pL, p0], then
Reg(A, p)  q0(p0  p∗) +
Z p0
p∗
(b  p∗) db v  b + F (p∗)(v  p∗),
where F (p∗) = R p∗ pL db/(v  b). The derivative of the right-hand side with respect to p∗ is zero, so the
bound is constant on [pL, p0]. Evaluating at p∗ = p0 gives
Reg(A, p)  (1  q0)(v  p0) = (v  p0) log v  pL
v  p0
.
If Lv > 1, set ¯p := v  (v  pL)/e. Then ¯p < p0, and the truncated density f (b) = 1/(v  b) on [pL, ¯p]
is a probability density. The same calculation as in Case (i) gives supp(·) Reg(A, p)  (v  pL)/e. The
two subcases imply supp(·) Reg(A, p)  ¯R(v).
Case (iii): v > pU . The same construction applies with pU replacing v, together with the terminal
valuation rule if the threshold is not reached before the deadline. Since v > p U , this terminal rule
always purchases at T . Let LU := log((pU  pL)/(pU  p0)), with the convention that LU = +1 when

ec29
pU = p0. If LU  1, draw b with density f (b) = 1/(pU  b) on [pL, p0) and put an atom q0 := 1  LU
at p0. Since a missed threshold costs at most pU  p∗, the same derivative calculation gives
Reg(A, p)  (pU  p0) log pU  pL
pU  p0
.
If LU > 1, use the truncated density f (b) = 1/(pU  b) on [pL, ¯pU ], where ¯pU := pU  (pU  pL)/e.
Then supp(·) Reg(A, p)  (pU  pL)/e. Hence supp(·) Reg(A, p)  ¯R(v). □
EC.4. Decreasing Price Envelopes
This subsection explains the reduction used in Section 6.6 . Let pL() and pU () be non-increasing
envelopes. Define the effective primitives
peﬀ L := pL(T ), p eﬀ U := pU (T ), p eﬀ 0 := minfp0, pU (T )g.
For every feasible path, the ex-post minimum p⋆ := inf t∈[0,T ] p(t) satisfies p⋆  peﬀ L . In addition,
because the agent observes p0 at the beginning and can wait until the deadline, the best realized
price is no higher than peﬀ 0 ; equivalently, p⋆  peﬀ 0 whenever the effective interval is nondegenerate.
If a randomized threshold is not reached before the deadline, the deadline price is at most peﬀ U , so
the missed-threshold continuation bound used in the constant-bound proof remains valid with pU
replaced by peﬀ U .
The achievability arguments for Lemmas 5 and 7 therefore go through verbatim after replacing
(pL, pU , p0) by (peﬀ L , peﬀ U , peﬀ 0 ).
The randomized threshold distributions depend only on the lower bound for p⋆, the largest relevant
upper bound on the best realized price, and the upper bound on the deadline price when the threshold
is not reached before the deadline. These are precisely peﬀ L , peﬀ 0 , and peﬀ U , respectively.
The adversarial optimality constructions can also be embedded in the decreasing-trend class. Fix a
small terminal interval [T  η, T ]. Because the envelopes are non-increasing and continuous at T , their
values on this interval can be made arbitrarily close to the terminal band [peﬀ L , peﬀ U ] by taking η small.
The adversary first chooses a feasible decreasing path that reaches the effective initial level peﬀ 0 at the
beginning of the markdown experiment. From that point, the path follows a decreasing trajectory from
peﬀ 0 toward peﬀ L . The random interruption time is the end-sale time σ from the flash-sale construction:
at σ, the markdown expires, the price jumps upward to the upper-envelope path, and then follows
p(t) = pU (t) until the deadline. Thus, the only uncertainty faced by the online rule is the realized
markdown depth before the end of the sale. Up to an arbitrarily small envelope-approximation error,
the same randomization over this markdown depth equalizes deterministic target-threshold rules
exactly as in Lemma 4 and Lemma 6 . Hence, the formulas remain the optimal guarantees for the
decreasing-trend problem under the effective primitives (peﬀ L , peﬀ U , peﬀ 0 ).

ec30
References
Bai J, Perron P (1998) Estimating and testing linear models with multiple structural changes. Econometrica
47–78.
Bai J, Perron P (2003) Computation and analysis of multiple structural change models. J. Appl. Econom.
18(1):1–22.
Bobkov SG, Ledoux M (2000) From Brunn–Minkowski to Brascamp–Lieb and to logarithmic Sobolev inequal-
ities. Geom. Funct. Anal. 10(5):1028–1052.
Brascamp HJ, Lieb EH (1976) On extensions of the Brunn–Minkowski and Prékopa–Leindler theorems,
including inequalities for log concave functions, and with an application to the diffusion equation. J.
Funct. Anal. 22(4):366–389.
Shaked M, Shanthikumar JG (2007) Stochastic Orders. Springer Series in Statistics (New York: Springer).
Yao ACC (1977) Probabilistic computations: Toward a unified measure of complexity.Proc. 18th Annu. Symp.
Found. Comput. Sci. (FOCS) , 222–227 (IEEE), URL http://dx.doi.org/10.1109/SFCS.1977.24.
