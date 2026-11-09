---
title: 'Learning to bid and bundle: a posterior-sampling agent for online retail'
url: https://arxiv.org/abs/2611.00165
category: digital-marketing
subcategory: empirical
date: 2026-10
venue: ''
authors: []
source: arxiv
pdf_url: https://arxiv.org/pdf/2611.00165
pages: 37
chars: 94434
fetched_at: '2026-11-08T13:23:57+00:00'
kb_version: 1
---

# Learning to bid and bundle: a posterior-sampling agent for online retail

Learning to bid and bundle: a posterior-sampling agent for online retail
Hadi Mohammadia,∗
aDepartment of Methodology, Statistics & Data Science, Utrecht University, Padualaan 14, 3584 CH Utrecht,
The Netherlands
Abstract
An online retailer launching a perishable product bids for sponsored-search clicks, discounts a
bundle with an always-stocked staple and displays its remaining stock, which raises willingness
to pay. It knows neither how clicks respond to its bid nor how strong and dispersed its market
is, and learns both over repeated seasons from data its own decisions censor: a zero bid reveals
nothing about paid clicks, and choices follow only clicks. We design a posterior-sampling agent
for it. Each period it draws a market from an exact posterior and posts the bid and discount of
that market’s exactly solved season plan, so every action is one a fully informed seller could take.
In a simulated online florist it has the lowest regret averaged over markets. In weak markets
it gives up 12% to 23% of one season’s revenue over 500 seasons, four to seven times less than
drawing once per season. A planner acting on point estimates can stop bidding and never learn
that bidding pays. The agent escapes after about three seasons on average, against fifty with
one draw per season. Where displayed scarcity keeps willingness to pay above the posted price,
the discount needs no learning. Customers waiting for the discount to return to its recent level
look like lost sales, so frequent waiting makes the agent underrate its market. One discount per
season removes waiting at a cost of 5.9% of clairvoyant revenue in a weak market and none in a
strong one.
Keywords:Online retailing, Sponsored search advertising, Bundle pricing, Dynamic pricing,
Thompson sampling, Reinforcement learning, Scarcity effect
1. Introduction
Online retailers buy traffic through sponsored search, offer a second item at a discount on the
product page, and show shoppers how many units are left. Each lever matters on its own: paid
listings partly take traffic that organic results would otherwise bring (Moshary, 2025), scarcity
cues raise booking intentions on hospitality platforms, partly through perceived value (Teubner
& Graul, 2020), and when to disclose limited inventory is itself a decision that shapes sales (Z.
∗Corresponding author.
Email address:h.mohammadi@uu.nl(Hadi Mohammadi)
arXiv:2611.00165v1  [cs.AI]  30 Oct 2026

Liu et al., 2026). An online florist with fresh-cut bouquets to sell before the week is out uses
all three. Each period it bids for the search keyword that brings shoppers to its page and sets
a discount on a bouquet bought with a glass vase, while the page shows how many bouquets
are left. With demand known, the bid and the discount can be planned together by dynamic
programming (Mohammadi, Akrami, et al., 2026; Tunuguntla et al., 2019; Ye et al., 2015). At
launch the florist knows little. It does not know how strongly clicks respond to its bid, how much
its shoppers will pay, or how dispersed they are, and it has to learn all three from the clicks and
sales that its own bids and discounts generate.
Two features make this harder than learning a posted price. The instruments censor the
data. Organic visitors keep arriving without a bid, but only a positive bid reveals how paid clicks
respond, and a purchase choice is seen only after a click. A seller that concludes advertising does
not pay and stops bidding will never see evidence to the contrary. The discount, in turn, reaches
customers who can wait: when it moves within the season, patient shoppers hold out for a better
one, and in the seller’s data a waiting shopper looks like a lost sale. Displayed scarcity adds a
twist of its own. Deep scarcity lifts every shopper’s willingness to pay above the posted price, so
low-stock periods say little about the market.
We design and test a decision agent for this setting, with an offline planning module and an
online learning loop. Offline, it solves the season program exactly by backward induction for
every candidate market and click curve on a grid and stores the plans. Online, it keeps an exact
posterior over the candidates, which splits into a click part and a choice part, and in each period
draws a candidate and posts the bid and discount that the candidate’s plan prescribes at the
current stock and time. A decision is a table lookup, and every action is one a fully informed
seller would take in some market the data still allow. Drawing once per season instead gives
posterior sampling for reinforcement learning (Osband et al., 2013), which is easier to analyze
and underlies a variant that holds one discount for the whole season. We test both in a seeded
simulation of an online florist against certainty equivalence, randomized and scripted exploration,
model-free learners, and oracles that know part of the truth.
Four findings stand out. Drawing every period is the version to deploy. It has the lowest
regret averaged over markets ($33.6 over 500 seasons, against $74.0 for certainty equivalence and
$109.4 for one draw per season), and in weak markets it gives up 12% to 23% of one season’s
revenue over 500 seasons, four to seven times less than drawing once per season. Certainty
equivalence does slightly better only where its own plans keep producing informative data, as in
the strong market ($11 against $25), and it is the policy that can stop bidding for good. Tabular
Q-learning, which needs no demand model, still earns 9% less than the oracle after 500 seasons in
2

the strong market. Under a pessimistic prior that trap occurs, and posterior sampling escapes it
at a rate we can predict. With 2% prior weight on responsive click curves, certainty equivalence
never bids and forgoes more than half of the clairvoyant revenue every season, while one draw
per season first bids after fifty seasons on average and one draw per period after three. Displayed
scarcity decides what must be learned. Where it keeps every shopper’s willingness to pay above
the posted price, the optimal discount is a harvest level that depends only on known quantities,
and the only market question left is whether the market is of that kind. Customers who wait
contaminate learning. Waited bundles are recorded as no-sales, so once waiting is frequent the
agent’s beliefs drift toward weaker markets, whichever schedule it uses. Holding one discount for
the season removes waiting at a cost of 5.9% of clairvoyant revenue in a weak market and none
in a strong one.
The paper adds to work on learning agents for e-commerce decisions in design, testing and
guidance. On design, the agent learns a per-click bid and a bundle discount together from
data censored twice, with an exact posterior and an offline library of exactly solved plans, so
its actions stay readable and its computation small. On testing, it is compared with standard
and model-free learners in strong and weak markets and under two stress tests: a pessimistic
prior that traps certainty equivalence, for which we derive how fast posterior sampling escapes
under each sampling schedule (Proposition 3), and customers who wait for a better discount,
whose waits bias the agent once they are frequent (Lemma 2 gives the threshold for a frozen
plan). The analysis also shows that displayed scarcity can make discount learning unnecessary
(Proposition 2). On guidance, Section 8 turns the results into deployment rules with the signals
a seller can watch.
Two unpublished manuscripts are closest to this one. Mohammadi, Akrami, et al. (2026)
solves the season model used here with demand known. We restate that model in full, so the
paper can be read on its own, with one change, and study it under learning, which that work does
not address. Mohammadi, Rabbani, and Nili Ahmadabadi (2026) studies a seller with unlimited
inventory that learns which of a few prices to post, with no bid or bundle, against customers who
wait. Section 7 applies its buy-wait-leave rule, which it takes from Nabi-Abdolyousefi (2018), to
the bundle discount. Section 2 sets out what each contributes here.
Section 2 reviews related work. Sections 3 to 5 present the model, the agent with its com-
puting cost, and the analytical results, Sections 6 and 7 the experiments, and Section 8 the rules
for deployment. Section 9 concludes. Proofs are in Appendix A. The online supplement holds
numerical checks and additional exhibits but no proofs.
3

2. Related literature
Learning agents for pricing.Reinforcement learning is a common tool for pricing in intelligent-
systems research. Q-learning has priced interdependent perishable products over a finite horizon
(Rana & Oliveira, 2015), deep reinforcement learning has set prices jointly with inventory under
reference-price effects (Zhou et al., 2022) and for perishable products that spoil (Kavoosi et
al., 2025), multi-agent learning has priced several perishable products at once (Qiao et al.,
2024), and policy-gradient methods have priced against online reviews (Wu et al., 2023). These
agents learn a value function or a policy from many simulated episodes and need no demand
model. A multi-armed bandit with Thompson sampling and upper confidence bounds prices a
delivery firm’s services from real data (Tajik et al., 2024), and reinforcement learning allocates
advertising budgets across channels (Wang & Zareeihemat, 2025). Our agent is model-based
instead: it learns three demand parameters and plans exactly, which keeps its actions readable
and its data needs small. In operations research, learning while pricing a fixed stock over a
finite season (Gallego & van Ryzin, 1994) is well studied (Araman & Caldentey, 2009; Aviv
& Pazgal, 2005; Besbes & Zeevi, 2009; den Boer, 2015), and with repeated selling seasons a
slightly modified certainty-equivalent policy learns on its own, because optimal prices vary with
the remaining stock (den Boer & Zwart, 2015). Learning while pricing extends to general choice
models (Broder & Rusmevichientong, 2012), perishable ordering (Keskin et al., 2022), priors
shared across products (Bastani et al., 2022), add-on discounts (Simchi-Levi et al., 2022) and
Thompson-sampling bundling of two products (Fang et al., 2025), none with an advertising lever
or scarcity-dependent willingness to pay. For perishable products without replenishment, Y.
Yang et al. (2022) learn the willingness-to-pay distribution from early-season sales with a neural
network, and for e-commerce promotions without price-elasticity history, Greenstein-Messica
and Rokach (2020) pair a demand model with gradient boosting. Thompson sampling entered
operational pricing with Ferreira et al. (2018) and is analyzed by Osband et al. (2013), Russo
and Van Roy (2014) and S. Agrawal and Goyal (2017). Closest in method, Shimizu et al. (2024)
apply posterior sampling to an episodic revenue-management problem whose prices come from a
linear program re-solved each episode. Learning can stop short of the truth even under optimal
experimentation (Rothschild, 1974), and does so when the seller acts on its estimates (den Boer
& Zwart, 2014; Harrison et al., 2012; Keskin & Zeevi, 2014), which Huh et al. (2022) remedy
by Bayesian dithering, finite parameter sets included. In our model the trap reappears on the
advertising side, where the instrument that generates information is bought per click.
Advertising and pricing.With demand known, Ye et al. (2015) optimize a sponsored-search
bid jointly with a posted price over a selling season, Tunuguntla et al. (2019) add inventory-
4

linked willingness to pay for a perishable product, and Salehi and Mirmohammadi (2023) a
limited advertising budget. N. Agrawal et al. (2025) set campaign prices and exchange bids in
one exactly solved Markov decision process on an advertising agency’s side, with no retail price,
goods inventory or bundle, and H. Li and Yang (2022) feed Bayesian click-through estimates from
real campaign logs into a static keyword-targeting model. Mohammadi, Akrami, et al. (2026)
replaces the posted price with a bundle discount under scarcity-dependent reservation prices
and establishes the bid–discount separation and complementarity that our agent’s plans inherit.
With learning, the nearest published counterpart is Gurkan et al. (2026), who learn demand
and advertising response while setting price, advertising level and inventory, giving sufficient
conditions for fast learning and an asymptotically optimal policy. Their advertising decision is a
level, ours a per-click auction bid whose zero level leaves the click data uninformative about the
paid click response. J. Liu et al. (2026) price while learning an unknown advertising model from
a class that includes the Nerlove–Arrow and Vidale–Wolfe models and show that static policies
are near-optimal for the classic models. Online learning in repeated auctions studies bidders
who learn values or competition (Balseiro & Gur, 2019; Guo et al., 2026; Han et al., 2025; Weed
et al., 2016; W. Yang et al., 2025), and auto-bidding agents set each auction’s bid against value
or return-on-spend targets (Aggarwal et al., 2024). In all of these the bid is the only lever and
inventory is absent. Here the bid interacts with a pricing lever through a perishable stock, and
what the bid censors is the seller’s own demand data: a zero bid hides the click curve.
Bundling and displayed scarcity.Bundlingandcross-sellingmodelspriceasecondproductagainst
limited inventories without an advertising decision (Bulut et al., 2009; Gökgür & Karabatı, 2019;
Netessine et al., 2006; Song & Xue, 2021). With name-your-own-price bids and an uncertain
supplier cost, complementarity and marginal cost decide whether the bundle beats separate sale
(Hemmati et al., 2023), and Abdallah and Reed (2026) show that as inventory becomes scarce
relative to market size, optimal dynamic mixed bundling converges to component pricing. The
harvest discount of Mohammadi, Akrami, et al. (2026) points the same way: under deep scarcity
the discount only prices the abundant staple into the bundle. We read that result for learning.
Where displayed stock keeps willingness to pay above the posted price, the discount needs no
learning.
Customers who wait and learning sellers.Forward-looking customers who time purchases against
markdowns areclassic (Aviv &Pazgal, 2008; Cachon& Swinney, 2009; Su &Zhang, 2008). When
they know the stockout risk, a larger initial stock sends more of them to wait (Zhao et al., 2022).
Prices that move in one direction only are a known remedy (Y. Chen & Jasin, 2024), and e-
commerce platforms choose when coupons can be redeemed with strategic consumers in mind (C.
5

Table 1: How the closest learning studies differ from this paper.
Study Decisions Learned Feedback Customers
Rana and Oliveira
(2015); Qiao et al.
(2024)
prices of perishable
products
a policy or value
function, model-free
sales myopic
den Boer and
Zwart (2015)
price of a finite stock
over repeated seasons
demand parameters sales myopic
Ferreira et al.
(2018)
prices against finite
stocks
demand parameters sales myopic
Gurkan et al.
(2026)
price, advertising
level, inventory
demand and
advertising response
sales myopic
Zhang and Jasin
(2022)
prices valuations and
patience
purchases over time patient
This paper per-click bid and
bundle discount for a
fixed stock
click curve, market
strength and spread
clicks, informative only at
positive bids; choices only
after a click
myopic, or
waiting for a
better discount
Lietal., 2020). Foralearningseller, Avivetal.(2019)findthatcommittingtoapriceincreasingly
dominates responsive pricing as the share of strategic consumers grows. Near-optimal markdown
policies for demand learning with forward-looking customers delay markdowns (Birge et al.,
2025), Zhang and Jasin (2022) learn valuation and patience and converge to cyclic pricing, and
customers also react to experimentation visible in a learning seller’s prices (X. Chen et al., 2022;
Golrezaei et al., 2021). In Mohammadi, Rabbani, and Nili Ahmadabadi (2026) a seller with
unlimited inventory learns which of a few prices to post against patience-driven waiting. Its
benchmark posts one price throughout, so waiting there comes only from the learner’s own price
changes. We apply the buy-wait-leave rule it takes from Nabi-Abdolyousefi (2018) to the bundle
discount of a perishable stock, where the clairvoyant discount itself moves within the season,
and show that waits recorded as no-sales bias a myopic likelihood, a misspecification of the kind
studied by Berk (1966) and, in revenue management, by Cooper et al. (2006).
Table 1 sets the paper apart on what is learned and on what the data reveal. Model-free
agents need no demand model but many episodes. Model-based learners in operations research
learn a few parameters from sales that every posted price reveals. Here the instrument that buys
information is a per-click bid whose zero level reveals nothing, choices arrive only after a click,
and scarcity and waiting change what the choices say about the market. The results of the paper
are about these features: the trap and how fast sampling escapes it, what scarcity removes from
the learning task, and how waiting biases the learner.
3. Model and learning environment
3.1. The selling season
We adopt the season model of Mohammadi, Akrami, et al. (2026) and state it here in full, in
our notation and with one change: we anchor its click curve at the organic rate. An online retailer
6

sells two commodities over a season ofTperiods, indexed by the number of periods remaining
t=T, . . . ,1. Theprimarycommodity is perishable: the season starts withI 0 units, there is
no replenishment, and units left at the end have salvage valuesper unit (baselines= 0). The
secondarycommodity is an abundant staple that never stocks out. Component pricespP and
pS are fixed for the season. The two products are also offered as a bundle at pricepP +p S −d t,
where thebundle discountd t ∈[0, dmax]is one of the retailer’s two per-period controls.
The other control is a cost-per-clicksponsored-search bidb t ∈[0, bmax]. Periods are short
enough that at most one customer clicks per period; a click arrives with probabilityλ(b)and
costsbwhether or not a purchase follows. We use the S-shaped click curve
λ(b) =λ 0 + (λ ∞ −λ 0) σ(κb−η)−σ(−η) 1−σ(−η) , σ(z) = 1 1 +e −z ,(1)
anchored so thatλ(0) =λ0 exactly for every locationη: without a bid the retailer gets its organic
click rateλ 0 and learns nothing about the paid part of the curve. (The curve of Mohammadi,
Akrami, et al. (2026) is not anchored, and Section S1 of the online supplement re-solves the oracle
under it.) A positive floor matches the evidence that paid listings partly draw traffic that organic
listings would otherwise receive (Moshary, 2025), so a seller that stops bidding keeps selling and
never learns why. Every click is billed at the bid, organic ones included. This overstates the cost
of bidding, a limitation Section 9 returns to. The slopeκand the floor and capλ0, λ∞ describe
the retailer’s own listing and are known from history. The locationηreflects the competitiveness
of the keyword auction and is unknown for a new product. Competing advertisers enter through
it, so a single seller learning its click curve covers auction competition in reduced form.
A clicking customer sees the posted discount and the remaining inventoryI, and displayed
scarcity shifts willingness to pay (WTP): the reservation price for the primary commodity is
RP (I) =µ P (I) +σ P (I)X, µ P (I) =δ µe−kI , σ P (I) = 1 +δ σe−kI ,(2)
withX∼Gamma(K P , ϑP ), whileR S ∼Gamma(K S, ϑS)is inventory-independent and the
bundle reservation price is additive,RB(I) =R P (I) +R S (Adams & Yellen, 1976);FP (· |I;θw)
andF S denote the distribution functions ofRP (I)andR S. The scalersδµ andδ σ summarize the
market’sstrengthanddispersionand are unknown for a new product. The display sensitivityk,
the Gamma shapesK P , KS and the scalesϑ P , ϑS are known. The customer buys the surplus-
maximizing option among the primary alone (RP (I)−p P), the secondary alone (RS −p S), and
the bundle (RB(I)−p P −p S +d), provided its surplus is positive;α P , αS, αB, α∅ denote the
resulting choice probabilities at(I, d), the last for no purchase. Customers in the main model
7

are myopic. Section 7 lets them wait for a better discount.
3.2. The full-information oracle
Given the unknown primitivesθ(made precise below), letV t(I)be the optimal expected
remaining revenue withtperiods andIunits left, and∆(I, t) =V t−1(I)− Vt−1(I−1)the
marginal value of theI-th unit. The Bellman recursion is
Vt(I) =V t−1(I) + max b≤bmax, d≤dmax λ(b)
h
ψI

d; ∆(I, t), θ

−b
i
,(3)
ψI (d; ∆, θ) = (αP +α B) (pP −∆) + (α S +α B)p S −α B d,
withV t(0) = 0,V 0(I) =sI, and the choice probabilities in the inner objectiveψI evaluated at
(I, d;θw), so the state enters through the scarcity level and through the marginal value. Forevery
parameter value,ψ I does not depend on the bid, so each period’s maximization splits into two
one-dimensional searches, and both optimal controls are nonincreasing in∆(I, t)(Mohammadi,
Akrami, et al., 2026; Topkis, 1998): where stock is scarce relative to remaining time,∆is high
and paid traffic cannot pay for itself. Numerically this gives an on–off bid with aswitching curve
I ∗(t)(thelowestinventoryatwhichthebidisonwithtperiodsremaining)and, instrongmarkets,
a discount pinned at theharvest leveldH = arg maxd h(d)withh(d) = (p S −d)

1−F S(pS −d)

,
which prices the secondary commodity into the bundle (Section 5 makes this limit precise).
3.3. The learning problem
The retailer knows the model structure but not the demand primitives, which we collect in
θ= (θ c, θw)withθ c =ηandθ w = (δ µ, δσ). We letθrange over a finite gridΘ = Θ c ×Θ w of
candidate values withJ=|Θ|. The true parameter isθ∗. The grid spans weak to strong markets
and cheap to expensive click auctions, so learning means discovering which market regime the
product lives in, the question a merchandiser faces at launch.
Selling proceeds over repeated seasonsn= 1, . . . , N(fashion-like assortment cycles): each
season resets inventory toI0 and runsTperiods under the same unknownθ ∗. Within a period
at state(t, I)the retailer posts(b, d)and observes two signals:
c∼Bernoulli

λθc(b)

,and, only ifc= 1, y∈ {P, S, B,∅}with probabilitiesαy(I, d;θw).(4)
Clicks are billed, hence observed. Item-level sales identifyP,S, andB, and a billed click without
a sale identifies∅(Figure 1). The choice signal iscensored by the click: periods without a click
carry no information aboutθw and, by the anchoring in (1), periods without a bid carry none
8

aboutθ c. A season ends att= 0or at stockout, so successful policies self-censor late-season
choice data.
Table S.1 in the online supplement collects the notation. The retailer starts from a priorp0 on
Θand updates top n after seasonn. Performance is measured against the full-information oracle:
withV ∗(θ) =V T (I0)the oracle season value andVθ∗(π)the exact expected season revenue of a
policyπunder the true parameters, per-season regret and cumulative Bayes regret are
rn =V ∗(θ∗)−V θ∗(πn),R(N) =E h PN n=1 rn i ,(5)
whereπ n is the policy deployed in seasonnand the expectation is over the prior, the observation
noise, and the algorithm’s randomization. For a learner that plays one season plan,Vθ∗(πn)is
exact after one backward pass, so its regret estimates carry no simulation noise beyond which
plan was deployed. A learner whose actions respond to data within the season, the per-period
agent of Section 4,ε-greedy and Q-learning (Section 4.2), plays no fixed plan. Its regret is
estimated as the oracle’s realized revenue minus its own, with the same customers facing both
(common random numbers), which is unbiased.
4. The learning agent
Figure 1 shows the agent’s two parts. Offline, before the first season, it solves the season
program (3) for every candidate inΘand stores each plan as a bid map and a discount map
over the remaining time and stock. Online, it keeps the posterior as two vectors, one over click
curves and one over willingness-to-pay parameters, updates them after every click and choice,
and in each period draws a candidate and looks up that candidate’s action.
4.1. Likelihood and exact posterior
WriteH n for the history through seasonn: the posted controls, click outcomes, and post-click
choices at their visited states. The likelihood factors into a click part and a choice part,
L(Hn |θ) =
Y
periods
λθc(b) c  1−λ θc(b) 1−c
| {z }
depends only onθ c
×
Y
clicks
αy(I, d;θw)
| {z }
depends only onθ w
,(6)
because the click depends on the bid alone and the choice, given a click, on(I, d)alone. The
posted controls depend onθonly through past data, so they add no factor that involvesθ. A
product prior therefore stays a product under any policy: clicks update only theθc-marginal and
choices only theθ w-marginal. The agent keeps the posterior exactly as two vectors onΘc and
9

offline, before launch
candidate markets θ
(click curve,
strength, spread)
exact season
program for
each θ
plan library
πθ(t, I) ↦ (b, d)
online, each period
posterior
click part ×
choice part
draw ̃θ
(PSRL: once
per season)
look up
(b, d) = π ̃θ(t, I)
post bid and discount,
show stock; see click
and choice
update both
parts
post (b, d) at state (t, I)
click?
λη(b), costs b
no click:
no choice seen
choice P, S, B, ∅
α(I, d; θw)
sale: revenue;
I falls for P, B
no sale
(billed click)
b = 0: organic
rate only; the
click curve is
never identified
Figure 1: The learning agent (left) and the events within a period (right); solid outcomes are observed.
Θw, with one log-likelihood update per observation. Draws, means and modes are exact up to a
10−12 floor on choice likelihoods for numerical stability (Section S1 of the online supplement).
4.2. The agent and its benchmarks
The plansπ θ are solved by backward induction with ties broken toward the smallest control.
With the discount separated from the bid and the choice tables precomputed, each plan takes
milliseconds (Section 4.3). Algorithm 1 then draws a candidate from the posterior in every period
and posts the action that the candidate’s plan prescribes at the current state. We call thists-
update. Like the Thompson-sampling algorithms of Ferreira et al. (2018), it samples every
period, and the stored plans already respond to the remaining stock and time. Drawing only at
the start of each season and playing that plan to the end is posterior sampling for reinforcement
learning (psrl) of Osband et al. (2013), the form that Proposition 4 covers and that Section 7
restricts to one discount per season. Either way every action is one that the full-information
plan of some candidate prescribes, which at our calibration means a bid that switches on and off
along the plan’s switching curve and a harvest or clearance discount (Section 3.2).psrlfollows
one plan for a whole season;ts-updatemay switch plans within the season as the data arrive,
which is what lets it act on early evidence.
Benchmarks.We compare against theclairvoyant oracleπ θ∗;certainty equivalence(ce), which
solves (3) each season for the posterior-mean click curve and choice tables;ε-greedy,cewith a
decayingper-periodprobabilityofauniformrandomcontrolpair;explore-then-commit, ascripted
10

Algorithm 1:The learning agent (ts-update; the boxed line is skipped bypsrl,
which draws only at season start)
Input:gridΘ, priorp 0, stored plans{πθ}θ∈Θ
1forseasonn= 1, . . . , Ndo
2draw ˜θ∼current posterior; setI←I 0;
3fort=T, . . . ,1whileI >0do
4post(b, d) =π ˜θ(t, I); observe clickcand, ifc= 1, the choicey; collect revenue;
5update the click posterior with(b, c)and, ifc= 1, the choice posterior with
(I, d, y);
6 re-draw ˜θ∼current posterior ;
Table 2: Computing cost of the agent by grid sizeJ: choice tables and all season plans (offline), plan memory,
and time per decision and per update (online).
Offline Online
JTables (s) Plans (s) MiB Decision (µs) Update (µs)
27 1.5 0.007 0.03 2.7 0.64
125 4.2 0.033 0.16 2.9 0.63
405 13.6 0.106 0.52 3.7 0.68
891 16.6 0.237 1.14 4.1 0.70
control sweep for a fixed number of seasons followed byce;static-pair Thompson sampling, a
model-free yardstick that treats each constant(b, d)pair on a coarse grid as an arm with the
season return as reward; thebest static pairunder the true parameters, the strongest clairvoyant
benchmark that does not adjust within the season; twohalf oraclesthat know one block ofθ∗
and learn the other; andtabular Q-learning, a model-free reinforcement learner in the manner of
Rana and Oliveira (2015) that learns action values over the states(t, I)and 36 fixed bid–discount
pairs from the revenue it earns, exploringε-greedily.
4.3. Computing cost
Table 2 reports what the agent costs to run, measured in Python with one process on an
Apple M4 Max. Most of the offline time goes into the choice tables, about0.17seconds per
willingness-to-pay candidate. Once they exist, a season plan takes about0.26milliseconds, so
the125plans of the main grid take0.03seconds and0.16MiB. Online, a decision (one posterior
draw and one table lookup) takes about3microseconds and an update after an observation
under one, whatever the grid size. The agent never solves anything while it sells.
5. Design properties
This section states what the agent can rely on: which data inform which part of the posterior,
what displayed scarcity removes from the task, how fast sampling leaves a pessimistic prior, and
11

the regret guarantee of the once-per-season form. Proofs are in Appendix A. Throughout,Θis
finite and a season’s revenue lies in an interval of length¯V= (p P +p S +b max)T+sI 0: each
period earns at mostpP +p S and pays at mostbmax for a click, and salvage adds at mostsI0.
5.1. What scarcity removes from the learning task
Where scarcity carries the price, the discount can be frozen at a level that needs no learning:
Proposition 1(Harvest limit: strong markets need no discount learning).FixIand letε=
FP (pP |I), the probability that the primary reservation price fails to clear the undiscounted
primary price. Then, uniformly overdand over compact∆-sets,

 ψI (d; ∆, θ)−  (pP −∆) +h(d) 

 ≤2ε  |pP −∆|+ 2p S +d max  ,
h(d) = (pS −d)

1−F S(pS −d)

,
andhdepends only on theknownsecondary taste distribution. Asε→0the optimal discount
converges to the harvest leveld H = arg max d h(d), independent of∆,I,t, andθ w. (At the
baseline calibration the residual is below10−13 andd H = 5.4withh(d H ) = 10.17.)
Withε= 0at every reachable inventory level this is the harvest discount of Mohammadi,
Akrami, et al. (2026). The bound carries it to markets that are only nearly saturated. When
scarcity keeps willingness to pay high, the discount only prices the secondary commodity into
the bundle, and that trade-off involves nothing the retailer needs to learn.
The bid is the agent’s only source of click-curve data, and the stock extremes say little about
the market:
Lemma 1(Censoring and saturation).(i) A policy that never bids generates data whose like-
lihood is constant inθ c, so under a product prior the click-curve posterior never moves. (ii)
Conditional on the secondary draw, the choice is a piecewise-constant function ofRP whose de-
cisive thresholds all lie in the windowW(d) = [p P −d, p P ]. Hence, for any twoθ w, θ′ w, the
total-variation distance of the choice laws satisfies
TV

α(I, d;θw), α(I, d;θ′ w)  ≤2 sup
x∈W(d)

 FP (x|I;θ w)−F P (x|I;θ ′ w)

.
In particular, if both reservation-price distributions place at mostεof their mass below the top
of the window (deep scarcity), or both at mostεabove its bottom (dead market), the choice laws
differ by at most2ε: both inventory extremes are uninformative aboutθw.
Part (i) is exact because of the anchored click curve (1). Part (ii) is visible at the calibration
of Section 6.1: the choice laws of the strongest and weakest markets are indistinguishable at low
12

inventory, where scarcity lifts every market’s willingness to pay above the window, and separate
almost completely at season-start inventory (FP (pP |I)is below10 −5 for both atI≤2, against
0.00and1.00atI= 15).
Season-start states are informative, and every new season revisits them, so learning is fast.
In strong markets the willingness-to-pay side reduces to a single yes-or-no question:
Proposition 2(Saturated markets: one class, one policy, one bit).Callθw saturatedifF P (pP |
I;θ w) = 0at every inventory level the season can reach; sinceX≥0in(2),µ P (I)is the smallest
valueR P (I)can take and the condition is the closed-form oneδµe−kI0 ≥p P, and letΘsat ⊆Θ w
collect the saturated grid points. Then (i) for every saturatedθw and every(I, d),α S =α ∅ = 0
andα P =F S(pS −d) = 1−α B: all saturated parameters share a single choice law, free ofθw
and ofI; (ii) their season programs coincide and reduce toVt(I) =V t−1(I) + maxb,d λ(b)

(pP −
∆(I, t)) +h(d)−b

, so value, optimal bid and optimal discount are common to all of them, and
the optimal discount is the harvest discountdH in every state; (iii) hence the choice likelihood is
constant onΘ sat: under any policy and any product prior, theθw-posterior restricted toΘsat is
the prior restricted toΘsat for everyn, and in a season in which the sampled and the true WTP
blocks are both saturated the regret is exactly that of the click-curve sample; (iv) the boundary is
identified one-sidedly: a single no-purchase or secondary-only purchase has probability zero under
every saturated parameter and eliminatesΘsat at once, while a saturated truth never generates
one, so the class separates from the rest of the grid only at the rate of its Kullback–Leibler (KL)
divergence.
Thecondition, thechoicelawofpart(i), andthereducedseasonprogramandharvestdiscount
of part (ii) come from the full-information analysis of Mohammadi, Akrami, et al. (2026), where
the condition is an assumption. Parts (iii) and (iv) give them their learning meaning. For a
given click curve the saturated points share one season plan, so the seller has no need to tell
them apart: on the willingness-to-pay side the question is the single bit “is the market saturated”
(Section 6.3).
5.2. The no-bidding trap and how fast sampling escapes it
The sampling schedule sets how fast the agent leaves a pessimistic prior.
Proposition 3(The no-bidding trap).Let the prior be a product prior, fix a set of click curves,
calledresponsive, with prior massm, and suppose (a) the posterior-mean model’s optimal bid
is zero in every state, along every posterior reachable without bidding, and (b) at every state a
season reaches without a bid, a sampled plan bids if its click curve is responsive and does not bid
otherwise. Then: (i)cenever bids, its click-curve posterior stays at the prior forever, and if
13

bidding is profitable underθ∗ it loses at least a fixed positive amount every season: its regret grows
linearly inN. (ii)psrlfirst bids in a season whose index is geometric with success probability
m, so the mean is1/mseasons. (iii)ts-updatefirst bids in a period whose index is geometric
with success probabilitym. If seasons without a bid lastTperiods, its first bidding season is
geometric with success probability1−(1−m) T, with mean1/[1−(1−m) T ], close to1/(T m)
whenT mis small.
Premise (a) can be checked by season solves and holds, for example, when enough prior mass
sits on a click curve whose midpoint lies beyond the feasible bid range. This is the episodic,
advertising-side analogue of the uninformative-price traps of Harrison et al. (2012) and Keskin
and Zeevi (2014): acting on the belief that clicks are unresponsive destroys the only data that
could refute it. Parts (ii) and (iii) show why the sampling schedule matters. Drawing every
period gives the agentTchances per season to try a responsive click curve, so for smallT mits
expected wait is aboutTtimes shorter. One bidding period moves the click-curve posterior, and
learning proceeds from there. Section 6.4 quantifies the trap at a calibration where the frozen
belief costs more than half of the oracle revenue per season. Premise (b) fails there only for a
few plans of the weakest market, which post no bid at the start of a season, and the observed
escape times match both formulas (S1, Figure S.1).
Part (iii) also tells the seller how to set the prior. Under the premises, and if seasons without
a bid lastTperiods,ts-updatehas posted no bid afterKseasons with probability(1−m) T K, so
it bids withinKseasons with probability at least1−δonce the prior puts massm≥1−δ 1/(T K)
on responsive click curves.psrlneedsm≥1−δ 1/K for the same guarantee. WithT= 20,
K= 3andδ= 0.05the two floors are0.049and0.632.
5.3. A regret guarantee
Proposition 4(Bayes regret ofpsrl).Under the protocol of Section 3.3 with finiteΘof size
J, any prior andθ∗ drawn from it, the cumulative Bayes regret ofpsrlsatisfies
R(N)≤ ¯V
q
1
2 |Π|H(π ∗)N≤ ¯V
q
1
2 J NlogJ ,
whereΠ ={π θ :θ∈Θ}is the set of distinct season plans,π ∗ =π θ∗ is the optimal one, and
H(π ∗)≤log|Π|is its entropy under the prior.
This is the information-theoretic bound of Russo and Van Roy (2016) with seasons as rounds
and season plans as actions, applied to the exact posterior; we claim no new rate. It rules out
freezing but forecasts little. At our calibration the right-hand side is about6.6×105 over 500
seasons, more than the passive policy’s regret, while the regret ofpsrlis37at the baseline
14

truth and109averaged over the prior, and it does not grow with the grid size (S1). Since|Π|
counts distinct plans, grid points that share one, such as the saturated class of Proposition 2
at a given click curve, leave|Π|unchanged. We know of no comparable bound forts-update,
whose draws within a season are not independent rounds. Its case rests on Proposition 3(iii) and
on the numerical study.
6. Experimental evaluation
6.1. Test case and protocol
The calibration describes an online florist and takes its season and taste primitives from
Mohammadi, Akrami, et al. (2026). The perishable product is a fresh-cut bouquet listed at
$50: it cannot be restocked once the season has started, and bouquets still unsold at the end
are worth nothing. The staple is a glass vase listed at $20 that is always in stock, and each
period the florist chooses a discount for buying the two together and a bid for its search keyword.
Monetary amounts throughout are in U.S. dollars. No retailer’s records informed the calibration.
Component prices are fixed for the season, so in the strong market the $50 list price sits far below
what shoppers would pay and the bid and the discount are the only levers.
Table 3 collects the calibration and the experimental design. Unless stated otherwise, a
season hasT= 20periods andI 0 = 15units, the season of the two weak-market scenarios
of Mohammadi, Akrami, et al. (2026) (its own baseline season is shorter and smaller,T= 15
andI 0 = 10). The parameter grid isδ µ ∈ {50,60,80,110,170},δ σ ∈ {2,6,12,22,42}, and
η∈ {4,4.75,5.5,6.25,7}, givingJ= 125candidates from near-dead to strong markets and cheap
to expensive click auctions. Priors are uniform unless stated. Thebaselinetruth is the strong
market(δ µ, δσ;η) = (170,42; 5.5), thelow-meantruth(50,6; 5.5), and thelow-dispersiontruth
(60,2; 5.5). The saturation condition of Proposition 2 readsδ µ ≥p P ekI0 = 105.85here, so
the baseline truth is saturated together with nine of the other twenty-four market grid points,
while both weak truths are not. Under the anchored click curve (1) the oracle season values
are $804.3 (baseline), $747.2 (low mean), and $686.1 (low dispersion). The oracle bids on–off
with switching curveI∗(t)≈t/2and posts a harvest discountd H = 5.4at the baseline (a $64.60
bundle, with the vase at $14.60) against clearance-deep discounts in the weak markets, where bid-
only revenue collapses to the passive level while the joint policy earns 13 to 14 times as much, the
complementarity of Mohammadi, Akrami, et al. (2026) recomputed under the anchored curve.
Conditions run paired replicates under common random numbers (identical customer uni-
forms per replicate and season),M= 200unless Table 3 says otherwise; the agent,psrl,ce
andε-greedy run2,000replicates in the four main settings. Regret is computed as Section 3.3
15

Table 3: Calibration and experimental design.
SeasonT= 20,I 0 = 15,s= 0;b max =d max = 15, controls on0.1-grid
Prices, tastesp P = 50,p S = 20;X∼Gamma(40,0.1),R S ∼Gamma(5,4);k= 0.05
Click curveλ 0 = 0.3,λ ∞ = 1,κ= 1;ηunknown
GridΘδ µ ∈ {50, . . . ,170} ×δσ ∈ {2, . . . ,42} ×η∈ {4, . . . ,7},J= 125
Truths baseline(170,42; 5.5); low mean(50,6; 5.5); low dispersion(60,2; 5.5)
ReplicatesM= 200, paired;2,000for the four main learners in the main settings,100in
robustness and scaling; seeds(seed,replicate,season)
Seasons headline, weak marketsN= 500; trap1000; waiting300; robustness300
Trap truth(170,42; 4); prior mass0.98(0.95,0.90) on an added unresponsive curve,
η= 20
describes: exactly for learners that play one plan per season, against the oracle under common
random numbers for the others. Differences between learners are reported as paired means with
95% confidence intervals.
6.2. Headline: regret against the clairvoyant
Figure 2 sets the learners side by side in every test case and Table 4 gives the numbers at
the strong baseline truth and averaged over the prior. The agent (ts-update) has the lowest
regret in four of the five settings. Averaged over the prior (Bayes mode, the truth drawn from
the prior) it gives up33.6over 500 seasons, belowceby40.4(paired 95% interval[29.7,51.1])
and belowpsrlby75.8([67.7,84.0]). At the strong baseline truth it gives up25.4, about 3%
of one season’s oracle revenue of $804.3, and22.1of that in the first ten seasons; drawing once
per season gives up12.0more ([9.9,14.2]). Certainty equivalence does better at this truth, at
11.4, below the agent by14.0([12.0,15.9]). With a uniform prior its mean model already bids,
so its clicks keep correcting its beliefs, and it never plays a deliberately sampled plan, so it pays
nothing for exploration. The trap of Proposition 3 stays silent here.
Exploration without the model is expensive. Explore-then-commit pays1,175, nearly all of
it in its ten sweep seasons, and decayingε-greedy keeps paying for exploration long after it stops
learning (722). The model-free bandit, Thompson sampling over256fixed bid–discount pairs
with the season’s revenue as its reward, pays63,190and still sits 6.5% below the oracle after 500
seasons. Tabular Q-learning needs no demand model at all and pays for it: it gives up49,456
over 500 seasons at the baseline and still earns 9% less than the oracle at the end, and in the
weak markets it ends at 45% and 18% of the oracle’s revenue. Run for 20,000 seasons, its greedy
policy reaches 95% of the oracle at the baseline after 6,500 seasons and stays near 82% in the
low-mean market (Table S.5). Which half of the truth is costly to learn depends on the market.
At the saturated baseline it is the click side: knowing the willingness to pay still leaves31.0,
knowing the click curve only6.5. Averaged over the prior it is the willingness-to-pay side (65.3
against37.1). These half oracles draw once per season.
16

101 102 103 104 105
cumulative regret (log scale; 95% intervals)
trap (1,000 seasons)
averaged over markets
low dispersion
low mean
strong market
TS-update (agent) PSRL CE ε-greedy ETC Q-learning
Figure 2: Cumulative regret over 500 seasons (the trap: 1,000) with 95% intervals. The agent,ε-greedy and
Q-learning are scored against the oracle under common random numbers, the others exactly.
Table 4: Cumulative regret. The first four learners:2,000replicates; the others:200. The agent,ε-greedy and
Q-learning are scored against the oracle under common random numbers. Bayes mode draws the truth from the
prior; the half oracles draw once per season.
Baseline truth Bayes mode
Policy 10 seasons 500 seasons (s.e.) 500 seasons (s.e.)
Agent (ts-update) 22.1 25.4 (1.0) 33.6 (1.6)
One draw per season (psrl) 33.0 37.4 (0.6) 109.4 (4.5)
Certainty equivalence 9.5 11.4 (0.3) 74.0 (5.6)
ε-greedy 47.7 721.5 (3.5) 887.8 (13.7)
Explore-then-commit 1,169.6 1,175.4 (0.6) 1,574.2 (80.8)
Thompson sampling, 256 fixed pairs 2,007.1 63,190.1 (45.5) 72,904.8 (2,151.3)
Tabular Q-learning, 36 pairs 2,790.0 49,456.1 (398.7)
Known click curve (learn WTP) 6.5 6.5 (1.3) 65.3 (13.5)
Known WTP (learn click curve) 27.2 31.0 (1.2) 37.1 (2.5)
Best static pair (clairvoyant) 4,674.1 7,442.6
Passive 225,716.6
6.3. Recovering the switching curve
Figure 3 showswhatis learned, at the harder low-mean truth underpsrl. The posterior-
expected bid policy is already recognizably on–off after one season and visually indistinguishable
from the oracle by season 30. The meanL1 distance between the expected and oracle bid policies
falls from0.35(season 1) to0.0075(season 30) to numerical zero by season 200. Posterior mass
on the true market-strength row reaches0.88within five seasons and1.00by season 30, because
season-start states separate weak from strong almost perfectly; the click-curve location, learnable
only through bids, lags (mass0.91at season 20,1.00by season 200). At the baseline truth the
posteriorneverconcentrates, yet regret vanishes, as Propositions 1 and 2 predict: the truth and
the nine other saturated market grid points prescribe the same season plan, and after500seasons
17

5 10 15 20
periods remaining t
3
6
9
12
15inventory I
season 1
5 10 15 20
periods remaining t
season 5
5 10 15 20
periods remaining t
season 30
5 10 15 20
periods remaining t
season 300
0
2
4
6
8
expected bid
100 101 102
season (log scale)
0.2
0.4
0.6
0.8
1.0posterior mass
true δμ row
true δσ column
true η
100 101 102
season (log scale)
0.0
0.2
0.4
0.6policy distance to oracle
bid L1
discount L1
Figure 3: Policy recovery at the low-mean truth underpsrl. Top: posterior-expected bid policy afternseasons
(white: oracle switching curve). Bottom: posterior mass on the true parameters (left) and distance to the oracle
policies (right).
they hold0.595of the posterior in tenequalshares of0.0595(S1). At the low-mean truth the
class holds0.011of the posterior after one season and5×10 −22 after two (Proposition 2(iv)).
6.4. Weak markets and the trap
Weak markets are where learning costs money. At the low-mean truth, where bid-only
revenue collapses to the passive level (52.9against the joint oracle’s747.2), the agent gives up
91.3over 500 seasons, and160.7at the low-dispersion truth, about 12% and 20% of one season’s
oracle revenue (Figure 4, left). It earns99.7%and99.5%of the oracle over its first fifty seasons,
more than the best static pair chosen with full knowledge of demand (92.5%and93.4%; both in
Table S.3). One draw per season costs four to seven times as much (680.5and712.5). Certainty
equivalence lies in between at the low mean (349.2) and above both at the low dispersion (723.7),
andε-greedy pays1,736and3,528. The gap between the two sampling schedules comes from
the first seasons. A draw from a strong market posts harvest discounts that a weak market
cannot convert, and the first no-sales at those discounts already refute it.ts-updateacts on
that evidence in the next period,psrlonly in the next season.
The right panel of Figure 4 shows the trap of Proposition 3 at a strong market with cheap
clicks (η= 4, oracle value825.9), under a prior with mass0.98on a click curve whose midpoint
lies beyond the feasible bid range, so that the mean-model bid is zero in every state. Certainty
18

0 100 200 300 400 500
season
100
200
300
400
500
600
700cumulative regret
PSRL
CE
TS-update
low mean
low dispersion
0 200 400 600 800 1000
season
102
103
104
105
106
cumulative regret (log scale)
0 1000
0
1ever bid
CE
PSRL
ε-greedy
TS-update
Figure 4: Left: cumulative regret at the two weak-market truths. Right: the trap, under prior mass0.98on an
unresponsive click curve (log scale); inset: share of replicates that have ever bid.
equivalence never bids in any of200replicates over1,000seasons and loses464.9per season,
more than half of the oracle’s revenue, so its cumulative regret grows linearly.psrldraws a
responsive click curve with probability0.02per season. It first bids in season50.9on average
(predicted:50) and gives up23,210in total.ts-updatedraws twenty times a season, first bids
in season2.9on average (predicted:3.0) and gives up2,004. At live mass0.05and0.10the mean
first-bid seasons are21.1and10.0forpsrland1.5and1.1forts-update, against predicted20,
10,1.6and1.1(Figure S.1). Randomized exploration also escapes (ε-greedy:2,552) but keeps
paying its exploration tax where nothing is left to learn (722at the baseline). A point-estimate
system that recommends “do not advertise” produces data that can never contradict it.
6.5. How the results compare with existing findings
Certainty equivalence does well wherever its own decisions keep producing informative data.
den Boer and Zwart (2015) show that with finite inventories and repeated selling seasons a
slightly modified certainty-equivalent pricing policy learns, because optimal prices vary with the
remaining stock. Here the bid switches on and off with stock and time in the same way, so
clicks keep informing the click-curve estimate, which is whycewins at the strong baseline.
That endogenous learning stops once the plan stops bidding, because a zero bid makes clicks
uninformative. The trap is the incomplete learning of Harrison et al. (2012) and Keskin and
Zeevi (2014) moved from the price to the bid, and the remedy changes with it: those papers force
deviations from the myopic price, while here a single positive bid informs, so one responsive draw
suffices. The Thompson-sampling algorithms of Ferreira et al. (2018) also sample every period
and re-solve a linear program each period, in one variant with inventory constraints that follow
the remaining stock. With exactly solved plans the stock and time are already handled, and the
19

samplingscheduleisthedesignchoiceleft. Itmattersmostwherethefirstobservationscontradict
the draw, in weak markets and in the trap. Gurkan et al. (2026) give sufficient conditions for
exponentially fast learning when price, advertising and inventory are set together, and find that
departing from them to avoid experimentation costs profit. A zero bid is the extreme case:
it avoids experimentation on the advertising side altogether, and learning about clicks stops.
Model-free agents, such as the reinforcement-learning pricers of Zhou et al. (2022) and Qiao et
al. (2024), learn a policy from many simulated episodes. The two model-free learners here show
what that costs without the season structure: the bandit over fixed pairs gives up63,190and
tabular Q-learning49,456over 500 seasons, and Q-learning needs thousands of seasons to come
within 5% of the oracle. A model-based agent avoids that cost by learning three parameters
rather than a value function. Section 7 adds two comparisons on the customer side.
6.6. Prior misspecification and robustness
In every robustness variant the agent either beats once-per-season sampling or matches it
within sampling error (Table S.2). An off-grid truth leaves a regret plateau that tracks the mesh:
a roughly sevenfold finer grid cuts it from0.42to0.10per season (Table S.2). The picture is
unchanged across(T, I0)and positive salvage, but not when the display sensitivitykis learned
as well: at a fast-decay truth off a coarse81-point grid posterior sampling settles at90.2%of the
oracle. When the market weakens every 40 seasons, every learner that keeps all its data pays
once the market turns weak, and keeping only the last 40 seasons of data cuts the regret by a
third (S2). Regret is flat in the grid size (36.6atJ= 27,31.9atJ= 405; Figure S.1), far from
the √JlogJof Proposition 4, because every observation updates all candidates at once.
7. Customers who wait for a better discount
7.1. Waiting on the discount margin
Component prices are fixed within a season, so the only price a customer can hope to improve
by waiting is the bundle’s. Following the three-way choice model of Mohammadi, Rabbani, and
NiliAhmadabadi(2026), itselfadoptedfromNabi-Abdolyousefi(2018), aclickingcustomerwhose
surplus-maximizing option is the bundle, with surplusu=RP +RS −(pP +pS −dt)≥0, compares
buying now, worthu, with waiting one period for a deeper discount, worthφ(u+ ˆdt −d t)at
patienceφ∈[0,1)and a forecast ˆdt of the posted discount. The customer therefore waits exactly
when
u < τt = φ
 ˆdt −d t +
1−φ ,(7)
20

buys otherwise, and, having waited, returns next period with probabilityρ, purchasing its
surplus-best option at the then-posted discount and displayed inventory. As in Mohammadi,
Rabbani, and Nili Ahmadabadi (2026), the forecast weights recent prices most. Here it expo-
nentially smooths the posted discount within the season,ˆdt−1 = (1−ν) ˆdt +ν dt, starting afresh
at each season’s first posted discount. Customers thus hold adaptive expectations: they respond
to the posted price path and never see the seller’s algorithm, and they wait when the discount
falls below its recent level. This is a scope choice. A discount that deepens through the season,
the classic markdown, never makes them wait, whereas customers with rational expectations
would wait for it (Aviv & Pazgal, 2008; Su & Zhang, 2008). Settingφ= 0recovers the myopic
environment of Section 3 exactly.
Waiting is priced entirely by the discount path:
Proposition 5(Immunity of constant discount paths).Under the waiting rule(7): (i)τ t is
nondecreasing inφand in the forecast gap( ˆdt −d t)+ and zero wheneverd t ≥ ˆdt. (ii) If the
posted discount is constant within the season,dt ≡d, then ˆdt =dandτ t = 0in every period:
no customer waits, revenue and transitions coincide with the myopic environment’s for every
φ∈[0,1)and every bid path, and hence the season value of any policy posting season-constant
discounts is invariant toφ. (iii) In a saturated market the full-information plan is such a policy,
since by Proposition 2(ii) it posts the harvest discountdH in every state: every saturated market’s
oracle isimmune to waiting, and any waiting observed there under a learner is caused by whoever
varies the discount, that is, by learning itself.
Parts (i) and (ii) follow directly from (7), and (ii) carries to the discount the observation of
Mohammadi, Rabbani, and Nili Ahmadabadi (2026) that a price held constant leaves customers
nothing to wait for. Part (iii) ties immunity to the saturated class. Off that class the oracle’s
own discount moves with the state, taking37distinct levels at the low-mean truth and43at the
low-dispersion truth, so there even the clairvoyant seller trains waiting.
Theseller’slikelihoodstaysmyopic: acustomerwhowaitsisrecordedasaclickwithoutasale,
indistinguishable from a genuine∅, and returning purchases arrive outside the click-attributed
data stream. Waiting therefore alsocontaminates the seller’s beliefs, with a sharp threshold:
Lemma 2(A dichotomy for belief contamination).Fix two WTP candidates, the truthθ ∗ w
and a rivalθ ′ w, both with all four outcome probabilities positive at every visited state, and let
each clicking customer whose surplus-best option is the bundle wait with probabilityw. (i) At
any state(I, d)the expected per-click increment of the log-likelihood ratio ofθ′ w againstθ ∗ w is
21

−KL(α(θ∗ w), α(θ′ w)) +w SI,d, with slope
SI,d =α B(θ∗ w) log α∅(θ′ w)α B(θ∗ w) α∅(θ∗w)α B(θ′w) ;
it is linear inw, negative atw= 0, and, wheneverS I,d >0(for whichα B(θ′ w)< αB(θ∗ w)and
α∅(θ′ w)> α∅(θ∗ w)at that state suffice), positive exactly abovew∗ I,d = KL(α(θ∗ w), α(θ′ w))/S I,d. (ii)
Aggregate over a frozen season plan’s visited states, weighting by expected clicks with the visit
measure held at its myopic benchmark and seasons i.i.d., and suppose the aggregated slopeSis
positive, a computable condition on known quantities. Then the posterior odds ofθ′ w againstθ ∗ w
converge to0almost surely when the waiting rate is below¯w∗ = KL/Sand diverge almost surely
when it is above.
Waited bundles become recorded no-sales, so beliefs drift toward weaker markets once the
waiting rate crosses the threshold. This is the learning counterpart of the spiral-down effect of
Cooper et al. (2006), in which a revenue manager who ignores customers’ substitution reads it
as weaker demand. Under the frozen clairvoyant plan at the weak truth only the weakest rival
(50,2)has a positive aggregated slope, with¯w∗ = 0.275. Forcing exogenous waiting on that plan
keeps posterior mass on the truth at1.00up tow= 0.32and drives it to0.00fromw= 0.45, so
for a frozen plan the computed threshold is conservative (S1, Figure S.2). For a learner, whose
plans vary, it is a guide only: atφ= 0.9the season-level learner’s realized waiting rate is about
0.27, just below the threshold, and its mass on the truth has already fallen to0.33.
7.2. Results
Figure 5 reports the waiting experiments, and Table S.4 gives the weak-truth results by pa-
tience level. The protocol of Section 6.1 applies, withρ= 0.5andν= 0.3. Alongside the learners
of Section 6 we run theflat-discount learner, the variant ofpsrlthat Proposition 5(ii) suggests:
drawθfrom the posterior once per season, then play the best season plan whose discount is one
constant level (the level is optimized at the draw and the bid stays state-dependent).
Exposure to waiting.At the strong-market truth the oracle’s simulated revenue is804.1per sea-
son (exact value804.3) ateverypatience level, because the flat harvest discount gives customers
nothing to wait for. Both sampling learners match it forφ≤0.9, since their discount settles
within a few seasons. Atφ= 0.99early exploration trains waiting (0.94events per season for
psrl,1.10forts-update), and both lose2.5%of revenue on average while the oracle loses
nothing. The average mixes two outcomes. In 150 (psrl) and 137 (ts-update) of the 200
runs no customer ever waits and nothing is lost; in the rest an early wait refutes the saturated
22

class, and revenue settles at90.2%and92.2%of the oracle’s (S1). weak-market truth the oracle
itself discounts less as stock clears, so all are exposed. Atφ= 0.9the oracle reaches85.4%of
the myopic-clairvoyant value,ce83.7%,psrl80.1%andts-update79.5%, and atφ= 0.99
the three learners all reach69.4%. Drawing every period buys nothing here: once the posterior
settles, both schedules post the same plans.
What trains waiting.Waiting needs a discount that varies within the season. Where it does not
vary, nobody waits; where it does, patience drives how many do (Figure 5, right). Clamping
the learner’s discount (at the capdmax = 15at the weak truth and atd H = 5.4at the strong
truth) while the bid keeps learning eliminates waiting at both truths and, at the weak market
withφ= 0.9, recovers revenue to93.6%of the clairvoyant, above both the unclamped learners
and the oracle. Waiting also contaminates inference. At the weak truth, posterior mass on the
trueθ w after300seasons falls from1.00(φ≤0.3) to0.98,0.33and0.00asφrises to0.6,0.9
and0.99underpsrl, and to0.29and0.00at the two highest levels underts-update. At the
saturated truth a waited bundle is the no-purchase observation that every saturated parameter
rules out (Proposition 2(iv)), so a single wait refutes the whole class (S1).
Committing the discount.The flat-discount learner turns Proposition 5(ii) into a design rule. Its
waiting count is zero at every patience level by construction, and its beliefs stay clean: posterior
mass on the trueθw at the weak truth is1.00for everyφ. The price is the flatness itself. At the
weak truth the best flat plan earns94.1%of the clairvoyant value, so under myopic customers
commitment gives up5.9points that the unrestricted learners keep. Atφ= 0.9it earns more
than the unrestricted learners, the learner with a clamped discount and the myopic-optimal
oracle, and atφ= 0.99it leads the unrestricted learners by24.7points (94.1%against69.4%).
At the strong truth commitment is free: the optimal plan is already flat (Proposition 2(ii)), and
the flat-discount learner earns the oracle’s simulated804.1at every patience level. Committing
the discount need not slow the bid. An agent that keeps drawing the bid every period but holds
the discount drawn at the start of the season makes nobody wait either, earns94.1%of the
clairvoyant value in the weak market at every patience level and, in the trap, first bids after2.9
seasons on average, as the agent does. Its price is a slower start on the discount, about800in
the weak markets on top of the cost of flatness, most of it in the first ten seasons (S2). seller can
watch for waiting directly: returning customers buy outside the click-attributed data, so bundle
purchases without a click that rise after the discount falls are its signature. Committing the
discount mirrors Aviv et al. (2019), who find that committing to a price increasingly dominates
responsive pricing as strategic customers become more common, and it keeps learning across
seasons while committing within each.
23

0.0 0.2 0.4 0.6 0.8 1.0
patience φ
500
550
600
650
700
750
800revenue per season (final 100)
oracle, strong
PSRL, strong
flat-discount PSRL, strong
oracle, weak
PSRL, weak
flat-discount PSRL, weak
0 1 2 3 4
within-season discount s.d. (mean)
0
2
4
6
8waiting events per season
PSRL
oracle
CE
PSRL, clamped d
flat-discount PSRL
Figure 5: Customers who wait. Left: revenue per season (final 100 seasons) against patienceφ. Right: waiting
incidence against the within-season standard deviation of the discount.
8. Rules for deployment
Table 5 turns the results into six rules for a seller who launches a perishable product into an
unknown market, each with a signal the seller can watch. The numbers come from the simulated
florist of Section 6.1.
Two of the rules have a price. The prior floor makes the agent bid in seasons where a
pessimistic seller would not, which costs money if clicks really are unresponsive. Commitment
gives up the discount’s response to stock: at patience0.3and0.6the unrestricted learner still
earns99.6%and98.3%of the clairvoyant value, so committing would cost5.5and4.2points
there, and it pays only once patience is high.
9. Conclusions
We designed and tested a learning agent for an online retailer that must learn how clicks
respond to its sponsored-search bid and what shoppers will pay for a perishable product as dis-
played stock runs down. Sampling a candidate market every period and following its exactly
solved plan learns fastest where learning is expensive, escapes a planner’s decision to stop ad-
vertising within a few seasons, and leaves every action readable. Where displayed scarcity keeps
willingness to pay above the posted price, the discount needs no learning, and where shoppers
wait for a better discount, one discount per season keeps their waits from biasing the agent.
Limitations and future research
The evidence is simulated from an illustrative calibration, so a field test on a retailer’s click
and sales logs is the natural next step. Three modeling choices deserve that test. Every click is
24

Table 5: Rules for deploying the agent.
Rule Signal to watch Action Evidence here
Draw every period always draw a market from the
posterior in each period and
post its plan’s bid and
discount
regret 91.3 and 160.7 in the weak
markets against 680.5 and 712.5
with one draw per season; 33.6
against 109.4 averaged over
markets (Sections 6.2 and 6.4)
Keep a prior floor
on bidding
before launch put prior mass
m≥1−δ 1/(T K)on click
curves whose plans bid
m≥0.049bids within three
seasons with probability0.95
(Proposition 3); without bidding,
$464.9 is lost every season
Distrust a plan to
stop advertising
the posterior-mean
plan bids zero
everywhere
keep sampling until a bid has
moved the click-curve
posterior
a zero bid reveals nothing about
paid clicks (Lemma 1)
Freeze the discount
where scarcity
carries the price
the estimated share of
full-stock shoppers
who would not buy the
product at its list price
is below a smallε
post the harvest discount
($5.40here) and learn only
the bid
the loss is at most of orderε
(Proposition 1); tuning buys
nothing there
Commit the
discount when
shoppers wait
bundle purchases
without a click rise
after the discount falls
hold the discount drawn at
the start of the season and
keep drawing the bid every
period
94.1%of clairvoyant revenue at
every patience level, against80.1%
and69.4%at patience0.9and
0.99; the bid still leaves the trap
after2.9seasons; costs5.9points
when nobody waits, nothing in
the strong market (Section 7.2)
Refine the grid
when learning stalls
the posterior settles
between neighbouring
candidates
add candidates near the
posterior mode and re-solve
offline
a sevenfold finer grid cuts the late
regret from0.42to0.10per
season (Table S.2)
billed at the bid, organic ones included, which overstates the cost of bidding. Customers who
wait hold adaptive expectations, so a classic markdown that deepens through the season does
not make them wait. Customers who anticipate the seller’s plan would, and a learner facing
them would need a model of their timing. The scarcity response is assumed: scarcity cues
raise booking intention on hospitality platforms (Teubner & Graul, 2020), which supports the
assumption, but its exponential form and the display sensitivitykare taken as known. Whenkis
learned as well, at a fast-decay truth off a coarse grid, posterior sampling settles at90.2%of the
oracle (Section 6.6). The parameter grid is finite. Refining it is cheap and the misspecification
plateau tracks the mesh, but fully continuous posteriors would need approximate season solves.
Component prices are fixed within the season, one product pair is bundled, and the stock is
displayed in every period, although whether and when to disclose it is itself a decision (Z. Liu
et al., 2026). Competition enters only through a stationary click curve for a single keyword.
A learner over several keywords would answer the call of H. Li and Yang (2022) for keyword
targeting that adjusts to market responses. Our model-free benchmarks are a bandit over fixed
pairs and tabular Q-learning; deep reinforcement learning, which needs simulated training at a
25

scale the agent avoids, is left for problems with richer state. On the theory side, a regret bound
for sampling within the season and instance-dependent regret under censoring remain unresolved.
Appendix A. Proofs
This appendix proves the claims of Section 3.2 and the results of Sections 5 and 7, in the
order in which they appear.
Separation and monotonicity of the season program (Section 3.2).(i) In (3) the bid enters only
throughλ(b)and the per-click cost, andψ I depends on(I, d)alone, somax b,d λ(b)[ψI (d; ∆, θ)−
b] = max b λ(b)[ψ∗ I (∆, θ)−b]withψ ∗ I = maxd ψI. (ii)ψ ∗ I is a maximum of functions affine and
nonincreasing in∆(the coefficient of−∆isα P +α B ≥0), hence nonincreasing in∆. As
λ(·)is nondecreasing,λ(b)(v−b)has increasing differences in(b, v), so by Topkis’s theorem
(Topkis, 1998) the largest and smallest maximizersb∗ are nondecreasing inv=ψ ∗ I (∆), hence
nonincreasing in∆. A deeper discount raises only the bundle’s surplus, so the no-purchase and
secondary-only events shrink:α P +α B = 1−α S −α ∅ is nondecreasing ind,ψ I has decreasing
differences in(d,∆), andd ∗ is nonincreasing in∆.
Proof of Proposition 1.WriteF≡F P (· |I;θw)and letε=F(p P ): the probability that the
primary reservation price fails to clear the undiscounted primary price. On the eventRP >
pP, the primary-alone surplus is positive, the bundle beats the secondary alone (their surplus
differenceisR P −(pP −d)>0), andthebundlebeatstheprimaryaloneexactlywhenR S > pS −d;
sothechoiceisthebundlewithprobability ¯FS(pS −d)andtheprimaryaloneotherwise, regardless
ofthe finelocationofR P. Hence|α S| ≤ε,|α∅| ≤ε,|αP −FS(pS −d)| ≤ε, and|αB − ¯FS(pS −d)| ≤
ε, uniformly ind. Substituting intoψ I (d; ∆, θ) = (αP +α B)(pP −∆) + (α S +α B)p S −α B d,

ψI (d; ∆, θ)−  (pP −∆) + ¯FS(pS −d)(p S −d) 

 ≤(|p P −∆|+ 2p S +d max) 2ε,
usingα S +α B =α B +O(ε)and ¯FS(pS −d)p S − ¯FS(pS −d)d=h(d)after collecting terms. The
bound is uniform on compact∆-sets and vanishes asε→0. The limit objective is(pP −∆)+h(d),
whosed-dependence is all inh(d) = (pS −d) ¯FS(pS −d), so every selection of maximizers converges
tod H = arg maxd h(d)(unique at the calibration), which involves only the knownFS.
Proof of Lemma 1.(i) By the anchored curve (1),λ θc(0) =λ 0 for everyθ c, so withb t ≡0
every click factor in (6) equalsλc 0(1−λ 0)1−c, independent ofθ c, so under a product prior the
θc-posterior never moves.
(ii) Fix(I, d)and couple the two models through a commonRS draw. Condition onRS =r
and trace the choice as a function ofRP. Two cases exhaust the possibilities.Caser < pS −d.
26

The bundle’s surplus is below the primary’s (sB −s P =r−(p S −d)<0) and the secondary’s
is negative (sS =r−p S <−d≤0), so the choice isPifR P > pP and∅otherwise: one
decisive threshold,p P ∈W(d).Caser≥p S −d.The bundle weakly dominates the primary,
so the choice is amongB,S,∅: the bundle beats the secondary alone exactly whens B > sS,
i.e.R P > pP −d, and beats no-purchase exactly whenRP > pP +p S −d−r; when the bundle
loses both comparisons the choice isSifr > p S and∅otherwise, with no further dependence
onR P. The two decisive thresholds arep P −dandp P +p S −d−r, and the latter matters
only while it exceedsp P −d, i.e. forr≤p S, and is at mostpP becauser≥p S −d: both lie
inW(d) = [p P −d, p P ]. In both cases the conditional choice law is a function of at most
two values ofF P (· |I)evaluated insideW(d), so its total variation acrossθ w, θ′ w is at most
2 supx∈W(d) |FP (x|I;θ w)−F P (x|I;θ ′ w)|. Integrating over the commonrpreserves the bound
and gives the display in the lemma.
For the two inventory extremes, note0≤F P (x|I;·)≤F P (pP |I;·)onW(d): if both
distributions place at mostεof their mass belowp P, both distribution functions are at mostε
throughout the window and the sup difference is at mostε(deep scarcity: every customer clears
every threshold and the choice reduces to the secondary-membership comparison of Proposi-
tion 1). Symmetrically, if both place at mostεabovepP −d, both distribution functions are at
least1−εon the window (dead market: the primary never sells and the choice degenerates to
the secondary-alone comparison).
Proof of Proposition 2.Saturation givesFP (x|I;θ w) = 0for everyx≤p P and every reachable
I, hence alsof P (· |I) = 0there. (i) Integrating the case analysis in the proof of Lemma 1
overR S givesα S =F P (pP −d|I) ¯FS(pS) = 0becaused≥0;α ∅ =F S(pS)FP (pP −d|
I) +
R pP
pP −d FS(pP +p S −d−x)f P (x|I)dx= 0because the integration range lies in(−∞, p P ];
αP =

1−F P (pP |I)

FS(pS −d) =F S(pS −d); andα B = 1−α P by adding up. None of the
four involvesθ w orI. (ii) Substitutingα S =α ∅ = 0,α P +α B = 1into (3) leaves the inner
objectiveλ(b)

(pP −∆) +α B(pS −d)−b

, andα B(pS −d) =h(d)gives the stated recursion.
Its data arep P,F S and the click curve only. WithV0(I) =IsandV t(0) = 0, also free ofθ w,
the value function, both maximizers (under the fixed tie-breaking rule) and therefore the whole
season policy are common to all saturated parameters, and the discount maximizeshalone, so it
equalsd H in every state. (iii) By (i) the choice factor of the likelihood (6) is identical acrossΘsat
for every observation, and under a product prior theθw-posterior is the prior times the choice
factor, so the posterior odds between two saturated points never move from their prior value.
Renormalizing gives the claim. If˜θn,w andθ ∗ w are both saturated then, by (ii),πn =π (˜θn,c,θ∗w) and
both the played and the optimal season value underθ∗ are unchanged if˜θn,w is replaced byθ∗ w:
27

the season’s regret is the click-curve sample’s alone. (iv) A post-click observation ofSor∅carries
likelihood factorα S = 0orα ∅ = 0under every saturated parameter, so one such observation
sets the mass of the whole class to zero. Under a saturated truth neither outcome ever occurs,
while every non-saturated parameter gives the observed outcomes positive probability, so it is
down-weighted only at its Kullback–Leibler rate.
Proof of Proposition 3.(i) Suppose the posterior-mean model at the prior has optimal bid0in
every state. Thencepostsb t ≡0in season 1. By Lemma 1(i) theθ c-posterior after season
1 equals the prior. Theθ w-posterior may move (organic clicks still arrive at rateλ0), but by
assumption the mean-model bid is zero in every statefor everyθ w-posterior reachable under
the frozenθ c-prior (the checkable premise). At our calibration it holds because the pessimistic
click curve makes paid traffic unprofitable at every demand model on the grid. By inductionce
never bids, its click-curve beliefs never move, and it plays a no-bidding policy every season. If
the optimal no-bidding value underθ∗ falls short ofV ∗(θ∗)byg >0, its regret is at leastgper
season. (ii) While no bid has been posted, the click posterior equals the prior (Lemma 1(i)),
and since the posterior is a product, the click part of every draw has the prior law whatever its
willingness-to-pay part. By the premise apsrldraw bids during the season exactly when its
click curve is one whose plans bid, which has probabilitym, and draws in different seasons use
independentrandomness. Theindexofthefirstbiddingseasonisthereforegeometricwithsuccess
probabilitym. (iii) The same argument applies period by period.ts-updatedraws afresh in
every period, each draw’s click curve has the prior law until the first bid, and by the premise
the draw bids at the current state exactly when its click curve is one whose plans bid. The first
bidding period is therefore geometric with success probabilitym. If a season without a bid lasts
Tperiods, it passes without a bid with probability(1−m) T, independently across seasons, so
the first bidding season is geometric with success probability1−(1−m)T =T m+O  (T m)2 .
After the first bid, click probabilities at the posted bid differ across the click curves in the prior’s
support, so the click-curve posterior moves.
Proof of Proposition 4.Treat each season as one round of the Thompson-sampling problem of
Russo and Van Roy (2016). The action in seasonnis the season planπn ∈Π, the observation
Yn is the season’s record of posted controls, clicks and choices, and the reward is the season’s
revenue, a function ofYn that lies in an interval of length¯V. The setΠis finite, and each plan
πθ is a function ofθunder the fixed tie-breaking rule. Givenθ ∗ and the plan, the records of
different seasons are independent and identically distributed, because every season restarts from
I0 under the sameθ∗ (Section 3.3).psrldraws ˜θn from the posteriorpn−1 and playsπ n =π ˜θn.
28

Since ˜θn andθ ∗ have the same law given the historyHn−1,
Pr

πn =π|H n−1

= Pr

π∗ =π|H n−1  for everyπ∈Π,(A.1)
so the algorithm is Thompson sampling overΠin their sense (the plans already played add no
likelihood factor that involvesθ; Section 4.1), and the regret (5) is their Bayesian regret. Write
En andI n for expectation and mutual information givenHn−1, and let
Γn =

En

Vθ∗(π∗)−V θ∗(πn) 2
In

π∗; (πn, Yn) 
be the information ratio of seasonn. Russo and Van Roy (2016) show that a policy satisfying
(A.1) hasR(N)≤
p¯ΓH(π ∗)NwheneverΓ n ≤ ¯Γin every season (their Proposition 1), and that
Γn ≤ |Π|/2when the actions are finitely many and the rewards lie in an interval of unit length
(their Proposition 3). Dividing the revenue by¯Vdivides the numerator ofΓ n by ¯V 2 and leaves
the denominator unchanged, soΓn ≤ ¯V 2|Π|/2, which gives the first bound. The second follows
fromH(π ∗)≤log|Π|and|Π| ≤J.
Proof of Proposition 5.(i) With surplusu≥0and forecast gapδ= ( ˆdt −d t)+, waiting is
preferred exactly whenφ(u+δ)> u, i.e.u < φδ/(1−φ) =τ t;τ t is nondecreasing inφand inδ
and zero atδ= 0. (ii) Ifd t ≡dfor allt, the forecast recursion ˆdt−1 = (1−ν) ˆdt +νd t, initialized
at the first posted discount, gives ˆdt =dfor allt, soδ≡0andτ t ≡0: no customer waits,
no returning pool forms, and revenue and transitions coincide with the myopic environment’s
for every bid path, so the season value of any season-constant policy is invariant toφ. (iii) By
Proposition 2(ii) the full-information plan at a saturated parameter postsdH in every state, a
season-constant discount, so (ii) applies to it.
Proof of Lemma 2.Fix the state(I, d)and writeα∗ =α(· |I, d;θ∗ w),α ′ =α(· |I, d;θ′ w)over the
four outcomes{P, S,∅, B}. With waiting ratew, a clicked customer produces the outcome law
Qw =α ∗ +w α∗ B (e∅ −e B),
the truth’s law with aw-fraction of bundle outcomes recorded as no-sales. The myopic likelihood
accumulateslogα y at the observed outcomey, so the expected per-click increment oflog(L′/L∗)
is
DI,d (w) =
X
y
Qw(y) log α′ y α∗y =−KL  α∗, α′ +w α∗ B log α′ ∅ α∗ B α∗ ∅ α′ B ,
29

by direct substitution: thew-term collects the coefficient of the mass moved fromBto∅. This
proves (i):D I,d is linear inwand strictly negative atw= 0(a Kullback–Leibler divergence
between distinct laws). IfS I,d >0it is strictly increasing and crosses zero exactly atw ∗ I,d,
and the displayed bracket is positive wheneverαB(θ′ w)< α B(θ∗ w)andα ∅(θ′ w)> α ∅(θ∗ w)at the
state, the sufficient ordering quoted in the statement. For (ii), weight each state by its expected
clicks under the plan’s myopic occupancy (season-start mass one atI0, depletion with probability
λ(b) (αP +αB), stockout absorbing) and sum: the season drift is−KL+w S, withKL>0because
the two laws differ at some visited state, andS >0by hypothesis. The hypothesis is a finite sum
of known quantities, so it is checkable at any calibration, and the pointwise ordering at every
visited state is one sufficient condition for it. Seasons under a frozen plan are i.i.d., and each
season’s increment is bounded (finitely many states, all outcome probabilities positive at visited
states by hypothesis), so the strong law of large numbers givesn−1 log(L′ n/L∗ n)→ −KL +w S
almost surely. The log-posterior odds differ fromlog(L′ n/L∗ n)by the constant log-prior odds, so
they diverge to−∞below¯w ∗ = KL/Sand to+∞above.
Declarations
The author declares no known competing financial interests or personal relationships that
could have appeared to influence the work reported in this paper. This research did not receive
any specific grant from funding agencies in the public, commercial, or not-for-profit sectors.
Data and code availability.All results are simulated from the parameter values reported in the
articleanditsonlinesupplement. Thecode, seededconfigurationsandresultsummariesareavail-
able at https://anonymous.4open.science/r/bid-bundle-agent-code-17D7 and will be deposited
in a public repository on acceptance. The online supplement is included with this preprint as an
ancillary file.
Declaration of generative AI and AI-assisted technologies in the manuscript
preparation process
During the preparation of this work the author used Claude (Anthropic) in order to help edit
the text and check the consistency of reported results. After using this tool, the author reviewed
and edited the content as needed and takes full responsibility for the content of the published
article.
30

References
Abdallah, T., & Reed, J. (2026). The diminishing value of bundling under inventory scarcity.
Management Science. Advance online publication. https://doi.org/10.1287/mnsc.2025.
03120
Adams, W. J., & Yellen, J. L. (1976). Commodity bundling and the burden of monopoly.The
Quarterly Journal of Economics,90(3), 475–498. https://doi.org/10.2307/1886045
Aggarwal, G., Badanidiyuru, A., Balseiro, S. R., Bhawalkar, K., Deng, Y., Feng, Z., Goel, G.,
Liaw, C., Lu, H., Mahdian, M., Mao, J., Mehta, A., Mirrokni, V., Paes Leme, R., Perlroth,
A., Piliouras, G., Schneider, J., Schvartzman, A., Sivan, B., ... Zuo, S. (2024). Auto-
bidding and auctions in online advertising: A survey.ACM SIGecom Exchanges,22(1),
159–183. https://doi.org/10.1145/3699824.3699838
Agrawal, N., Najafi-Asadolahi, S., & Smith, S. A. (2025). Dynamic pricing and bidding for
display advertising campaigns.Manufacturing & Service Operations Management,27(3),
843–861. https://doi.org/10.1287/msom.2023.0600
Agrawal, S., & Goyal, N. (2017). Near-optimal regret bounds for Thompson sampling.Journal
of the ACM,64(5), Article 30. https://doi.org/10.1145/3088510
Araman,V.F.,&Caldentey,R.(2009).Dynamicpricingfornonperishableproductswithdemand
learning.Operations Research,57(5),1169–1188.https://doi.org/10.1287/opre.1090.0725
Aviv, Y., & Pazgal, A. (2005). A partially observed Markov decision process for dynamic pricing.
Management Science,51(9), 1400–1416. https://doi.org/10.1287/mnsc.1050.0393
Aviv, Y., & Pazgal, A. (2008). Optimal pricing of seasonal products in the presence of forward-
looking consumers.Manufacturing & Service Operations Management,10(3), 339–359.
https://doi.org/10.1287/msom.1070.0183
Aviv, Y., Wei, M. M., & Zhang, F. (2019). Responsive pricing of fashion products: The effects
of demand learning and strategic consumer behavior.Management Science,65(7), 2982–
3000. https://doi.org/10.1287/mnsc.2018.3114
Balseiro, S. R., & Gur, Y. (2019). Learning in repeated auctions with budgets: Regret minimiza-
tion and equilibrium.Management Science,65(9), 3952–3968. https://doi.org/10.1287/
mnsc.2018.3174
Bastani, H., Simchi-Levi, D., & Zhu, R. (2022). Meta dynamic pricing: Transfer learning across
experiments.Management Science,68(3), 1865–1881. https://doi.org/10.1287/mnsc.
2021.4071
31

Berk, R. H. (1966). Limiting behavior of posterior distributions when the model is incorrect.
The Annals of Mathematical Statistics,37(1), 51–58. https://doi.org/10.1214/aoms/
1177699597
Besbes, O., & Zeevi, A. (2009). Dynamic pricing without knowing the demand function: Risk
bounds and near-optimal algorithms.Operations Research,57(6), 1407–1420. https://
doi.org/10.1287/opre.1080.0640
Birge, J. R., Chen, H., & Keskin, N. B. (2025). Markdown policies for demand learning with
forward-looking customers.Operations Research,73(5), 2550–2566. https://doi.org/10.
1287/opre.2019.0402
Broder, J., & Rusmevichientong, P. (2012). Dynamic pricing under a general parametric choice
model.Operations Research,60(4), 965–980. https://doi.org/10.1287/opre.1120.1057
Bulut, Z., Gürler, Ü., & Şen, A. (2009). Bundle pricing of inventories with stochastic demand.
European Journal of Operational Research,197(3), 897–911. https://doi.org/10.1016/j.
ejor.2006.09.106
Cachon, G. P., & Swinney, R. (2009). Purchasing, pricing, and quick response in the presence
of strategic consumers.Management Science,55(3), 497–511. https://doi.org/10.1287/
mnsc.1080.0948
Chen, X., Gao, J., Ge, D., & Wang, Z. (2022). Bayesian dynamic learning and pricing with
strategic customers.Production and Operations Management,31(8), 3125–3142. https:
//doi.org/10.1111/poms.13741
Chen, Y., & Jasin, S. (2024). Simple monotonic readjustment policies with applications to mark-
down pricing and pricing in the presence of strategic customers.Operations Research,
72(5), 1893–1905. https://doi.org/10.1287/opre.2020.0774
Cooper, W. L., Homem-de-Mello, T., & Kleywegt, A. J. (2006). Models of the spiral-down effect
in revenue management.Operations Research,54(5), 968–987. https://doi.org/10.1287/
opre.1060.0304
den Boer, A. V. (2015). Dynamic pricing and learning: Historical origins, current research, and
new directions.Surveys in Operations Research and Management Science,20(1), 1–18.
https://doi.org/10.1016/j.sorms.2015.03.001
den Boer, A. V., & Zwart, B. (2014). Simultaneously learning and optimizing using controlled
variance pricing.Management Science,60(3), 770–783. https://doi.org/10.1287/mnsc.
2013.1788
den Boer, A. V., & Zwart, B. (2015). Dynamic pricing and learning with finite inventories.
Operations Research,63(4), 965–978. https://doi.org/10.1287/opre.2015.1397
32

Fang, L., Tang, J., & Pan, Z. (2025). Learning-based bundling strategy for two products under
uncertain consumer’s valuations.IEEE Transactions on Engineering Management,72,
1970–1982. https://doi.org/10.1109/TEM.2025.3567326
Ferreira, K. J., Simchi-Levi, D., & Wang, H. (2018). Online network revenue management using
Thompson sampling.Operations Research,66(6), 1586–1602. https://doi.org/10.1287/
opre.2018.1755
Gallego, G., & van Ryzin, G. (1994). Optimal dynamic pricing of inventories with stochastic
demand over finite horizons.Management Science,40(8), 999–1020. https://doi.org/10.
1287/mnsc.40.8.999
Gökgür, B., & Karabatı, S. (2019). Dynamic and targeted bundle pricing of two independently
valued products.European Journal of Operational Research,279(1), 184–198. https://
doi.org/10.1016/j.ejor.2019.05.022
Golrezaei, N., Javanmard, A., & Mirrokni, V. (2021). Dynamic incentive-aware learning: Robust
pricing in contextual auctions.Operations Research,69(1), 297–314. https://doi.org/10.
1287/opre.2020.1991
Greenstein-Messica, A., & Rokach, L. (2020). Machine learning and operation research based
method for promotion optimization of products with no price elasticity history.Electronic
Commerce Research and Applications,40, Article 100914. https://doi.org/10.1016/j.
elerap.2019.100914
Guo, M., Zhang, W., Shen, Y., & Zhang, Q. (2026). Bid shading in first-price auction: Nonsta-
tionary Bayesian multiarmed bandit methods for real-time bidding.Information Systems
Research. Advance online publication. https://doi.org/10.1287/isre.2025.1837
Gurkan, H., Keskin, N. B., & Parker, R. P. (2026). Dynamic learning for joint pricing, advertising,
and inventory management.Manufacturing & Service Operations Management. Advance
online publication. https://doi.org/10.1287/msom.2024.1182
Han, Y., Weissman, T., & Zhou, Z. (2025). Optimal no-regret learning in repeated first-price
auctions.Operations Research,73(1), 209–238. https://doi.org/10.1287/opre.2020.0282
Harrison, J. M., Keskin, N. B., & Zeevi, A. (2012). Bayesian dynamic pricing policies: Learning
and earning under a binary prior distribution.Management Science,58(3), 570–586.
https://doi.org/10.1287/mnsc.1110.1426
Hemmati, M., Fatemi Ghomi, S. M. T., & Sajadieh, M. S. (2023). Separate and bundling selling
strategies for complementary products in a participative pricing mechanism.Computers
& Industrial Engineering,177, Article 109018. https://doi.org/10.1016/j.cie.2023.109018
33

Huh, W. T., Kim, M. J., & Lin, M. (2022). Bayesian dithering for learning: Asymptotically op-
timal policies in dynamic pricing.Production and Operations Management,31(9), 3576–
3593. https://doi.org/10.1111/poms.13786
Kavoosi, A., Tavakkoli-Moghaddam, R., Sajedi, H., Tajik, N., & Tafakkori, K. (2025). Dynamic
pricing and inventory control of perishable products by a deep reinforcement learning
algorithm.Expert Systems with Applications,291, Article 128570. https://doi.org/10.
1016/j.eswa.2025.128570
Keskin, N. B., Li, Y., & Song, J.-S. (2022). Data-driven dynamic pricing and ordering with
perishable inventory in a changing environment.Management Science,68(3), 1938–1958.
https://doi.org/10.1287/mnsc.2021.4011
Keskin, N. B., & Zeevi, A. (2014). Dynamic pricing with an unknown demand model: Asymp-
totically optimal semi-myopic policies.Operations Research,62(5), 1142–1167. https:
//doi.org/10.1287/opre.2014.1294
Li, C., Chu, M., Zhou, C., & Zhao, L. (2020). Two-period discount pricing strategies for an e-
commerce platform with strategic consumers.Computers & Industrial Engineering,147,
Article 106640. https://doi.org/10.1016/j.cie.2020.106640
Li, H., & Yang, Y. (2022). Keyword targeting optimization in sponsored search advertising:
Combining selection and matching.Electronic Commerce Research and Applications,56,
Article 101209. https://doi.org/10.1016/j.elerap.2022.101209
Liu, J., Sun, Q., Xie, J., & Yuan, S. (2026). Joint dynamic advertising and pricing: Near-
optimality of static policies and demand learning.Production and Operations Manage-
ment. Advance online publication. https://doi.org/10.1177/10591478261481053
Liu, Z., Chen, S., Moinzadeh, K., & Tan, Y. (2026). When to broadcast? Inventory disclosure
policies for online sales of limited inventory.Information Systems Research,37(1), 117–
137. https://doi.org/10.1287/isre.2023.0746
Mohammadi, H., Akrami, E., Sazvar, Z., & Ghaderi, S. F. (2026).Dynamic sponsored search
bidding and bundle discounting for online retailers under inventory-dependent consumer
behavior[Manuscript submitted for publication].
Mohammadi, H., Rabbani, M., & Nili Ahmadabadi, M. (2026).Dynamic pricing with demand
learning and advertising in a nonstationary environment with forward-looking customers
[Manuscript submitted for publication].
Moshary, S. (2025). Does sponsored search advertising augment organic search? Evidence from
an e-commerce platform.Management Science,71(11), 9687–9709. https://doi.org/10.
1287/mnsc.2024.04792
34

Nabi-Abdolyousefi, S. (2018).Study of customer behavior in a revenue management setting using
data-driven approaches[Doctoral dissertation, University of Washington]. https://hdl.
handle.net/1773/42218
Netessine, S., Savin, S., & Xiao, W. (2006). Revenue management through dynamic cross selling
in e-commerce retailing.Operations Research,54(5), 893–913. https://doi.org/10.1287/
opre.1060.0296
Osband, I., Russo, D., & Van Roy, B. (2013). (More) efficient reinforcement learning via posterior
sampling.Advances in Neural Information Processing Systems,26, 3003–3011.
Qiao, W., Huang, M., Gao, Z., & Wang, X. (2024). Distributed dynamic pricing of multiple
perishable products using multi-agent reinforcement learning.Expert Systems with Ap-
plications,237, Article 121252. https://doi.org/10.1016/j.eswa.2023.121252
Rana, R., & Oliveira, F. S. (2015). Dynamic pricing policies for interdependent perishable prod-
ucts or services using reinforcement learning.Expert Systems with Applications,42(1),
426–436. https://doi.org/10.1016/j.eswa.2014.07.007
Rothschild, M. (1974). A two-armed bandit theory of market pricing.Journal of Economic The-
ory,9(2), 185–202. https://doi.org/10.1016/0022-0531(74)90066-0
Russo, D., & Van Roy, B. (2014). Learning to optimize via posterior sampling.Mathematics of
Operations Research,39(4), 1221–1243. https://doi.org/10.1287/moor.2014.0650
Russo, D., & Van Roy, B. (2016). An information-theoretic analysis of Thompson sampling.
Journal of Machine Learning Research,17(68), 1–30. https://jmlr.org/papers/v17/14-
087.html
Salehi, S., & Mirmohammadi, S. H. (2023). A solution approach for sponsored search advertising
and dynamic pricing for a perishable product and an online retailer with budget con-
straint.Computers & Industrial Engineering,177, Article 109086. https://doi.org/10.
1016/j.cie.2023.109086
Shimizu, K., Honda, J., Ito, S., & Nakadai, S. (2024). Learning with posterior sampling for
revenue management under time-varying demand.Proceedings of the 33rd International
Joint Conference on Artificial Intelligence, 4911–4919. https://doi.org/10.24963/ijcai.
2024/543
Simchi-Levi, D., Sun, R., & Zhang, H. (2022). Online learning and optimization for revenue
management problems with add-on discounts.Management Science,68(10), 7402–7421.
https://doi.org/10.1287/mnsc.2021.4222
35

Song, J.-S., & Xue, Z. (2021). Demand shaping through bundling and product configuration:
A dynamic multiproduct inventory-pricing model.Operations Research,69(2), 525–544.
https://doi.org/10.1287/opre.2020.2062
Su, X., & Zhang, F. (2008). Strategic customer behavior, commitment, and supply chain perfor-
mance.Management Science,54(10), 1759–1773. https://doi.org/10.1287/mnsc.1080.
0886
Tajik, M., Tosarkani, B. M., Makui, A., & Ghousi, R. (2024). A novel two-stage dynamic pricing
model for logistics planning using an exploration–exploitation framework: A multi-armed
bandit problem.Expert Systems with Applications,246, Article 123060. https://doi.org/
10.1016/j.eswa.2023.123060
Teubner, T., & Graul, A. (2020). Only one room left! How scarcity cues affect booking in-
tentions on hospitality platforms.Electronic Commerce Research and Applications,39,
Article 100910. https://doi.org/10.1016/j.elerap.2019.100910
Topkis, D. M. (1998).Supermodularity and complementarity. Princeton University Press.
Tunuguntla, V., Basu, P., Rakshit, K., & Ghosh, D. (2019). Sponsored search advertising and
dynamic pricing for perishable products under inventory-linked customer willingness to
pay.European Journal of Operational Research,276(1), 119–132. https://doi.org/10.
1016/j.ejor.2018.12.026
Wang,B.,&Zareeihemat,P.(2025).Multi-channeladvertisingbudgetallocation:Anovelmethod
using Q-learning and mutual learning-based artificial bee colony.Expert Systems with
Applications,271, Article 126649. https://doi.org/10.1016/j.eswa.2025.126649
Weed, J., Perchet, V., & Rigollet, P. (2016). Online learning in repeated auctions.Proceedings
of Machine Learning Research,49, 1562–1583.
Wu, C., Bi, W., & Liu, H. (2023). Proximal policy optimization algorithm for dynamic pricing
with online reviews.Expert Systems with Applications,213, Article 119191. https://doi.
org/10.1016/j.eswa.2022.119191
Yang, W., Xiao, B., & Wu, L. (2025). Learning unknown private valuation in Generalized Sec-
ond Price position auction.Electronic Commerce Research and Applications,72, Arti-
cle 101507. https://doi.org/10.1016/j.elerap.2025.101507
Yang, Y., Chu, W.-L., & Wu, C.-H. (2022). Learning customer preferences and dynamic pricing
for perishable products.Computers & Industrial Engineering,171, Article 108440. https:
//doi.org/10.1016/j.cie.2022.108440
36

Ye, S., Aydin, G., & Hu, S. (2015). Sponsored search marketing: Dynamic pricing and advertising
for an online retailer.Management Science,61(6), 1255–1274. https://doi.org/10.1287/
mnsc.2014.1915
Zhang, H., & Jasin, S. (2022). Online learning and optimization of (some) cyclic pricing policies
in the presence of patient customers.Manufacturing & Service Operations Management,
24(2), 1165–1182. https://doi.org/10.1287/msom.2021.0979
Zhao, N., Wang, Q., & Wu, J. (2022). The reference effect on a retailer’s selling strategy with
limited initial inventory level and strategic consumer behavior.Computers & Industrial
Engineering,169, Article 108260. https://doi.org/10.1016/j.cie.2022.108260
Zhou, Q., Yang, Y., & Fu, S. (2022). Deep reinforcement learning approach for solving joint pric-
ing and inventory problem with reference price effects.Expert Systems with Applications,
195, Article 116564. https://doi.org/10.1016/j.eswa.2022.116564
37
